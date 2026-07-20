"""Per-user install of Terminal Workbench Mono on Windows (no admin needed).

Copies the TTFs into the per-user font directory and registers them in
HKCU so every app sees them immediately. Re-running is safe (idempotent).
"""

import os
import shutil
import sys

ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), '..'))
TTF_SRC = os.path.join(ROOT, 'dist', 'ttf')

FILES = {
    'TerminalWorkbenchMono-Regular.ttf': 'Terminal Workbench Mono (TrueType)',
    'TerminalWorkbenchMono-Medium.ttf': 'Terminal Workbench Mono Medium (TrueType)',
    'TerminalWorkbenchMono-Bold.ttf': 'Terminal Workbench Mono Bold (TrueType)',
    'TerminalWorkbenchMono-Italic.ttf': 'Terminal Workbench Mono Italic (TrueType)',
    'TerminalWorkbenchMono-MediumItalic.ttf': 'Terminal Workbench Mono Medium Italic (TrueType)',
    'TerminalWorkbenchMono-BoldItalic.ttf': 'Terminal Workbench Mono Bold Italic (TrueType)',
}


def _copy_unlocking(src, dst, gdi):
    """Copy over dst, unloading it from GDI first if Windows has it locked."""
    try:
        shutil.copyfile(src, dst)
        return
    except PermissionError:
        if gdi is not None and os.path.exists(dst):
            for _ in range(20):
                if gdi.RemoveFontResourceW(dst) == 0:
                    break
        shutil.copyfile(src, dst)   # retry; raises if still locked


def main():
    if sys.platform != 'win32':
        print('This installer is Windows-only.')
        return 1
    import ctypes
    import winreg

    gdi = ctypes.windll.gdi32
    user32 = ctypes.windll.user32

    local = os.environ['LOCALAPPDATA']
    fonts_dir = os.path.join(local, 'Microsoft', 'Windows', 'Fonts')
    os.makedirs(fonts_dir, exist_ok=True)

    key_path = r'Software\Microsoft\Windows NT\CurrentVersion\Fonts'
    key = winreg.CreateKeyEx(winreg.HKEY_CURRENT_USER, key_path, 0,
                             winreg.KEY_SET_VALUE)

    installed = 0
    for fname, display in FILES.items():
        src = os.path.join(TTF_SRC, fname)
        if not os.path.exists(src):
            print('  ! missing', src, '- run  py tools/build.py  first')
            continue
        dst = os.path.join(fonts_dir, fname)
        _copy_unlocking(src, dst, gdi)
        winreg.SetValueEx(key, display, 0, winreg.REG_SZ, dst)
        gdi.AddFontResourceW(dst)
        print('  installed', display)
        installed += 1

    winreg.CloseKey(key)
    user32.SendMessageW(0xFFFF, 0x001D, 0, 0)   # broadcast WM_FONTCHANGE
    print(f'\n{installed}/{len(FILES)} styles installed for user '
          f'{os.environ.get("USERNAME", "")}.')
    print('Broadcast sent; most apps see the font immediately.')
    print('Pick "Terminal Workbench Mono" in Obsidian / VS Code / Windows Terminal.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
