"""Assemble release archives + SHA256SUMS into build/release/.

Cross-platform (pure Python) so local and CI builds are identical.
Run after build.py and make_obsidian_snippet.py.

Usage:  py tools/package.py
"""

import hashlib
import os
import zipfile

ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), '..'))
OUT = os.path.join(ROOT, 'build', 'release')


def _p(*parts):
    return os.path.join(ROOT, *parts)


def write_zip(zip_path, members):
    """members: list of (src_abs_path, arcname). Deterministic order."""
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as z:
        for src, arc in sorted(members, key=lambda m: m[1]):
            z.write(src, arc)


def main():
    os.makedirs(OUT, exist_ok=True)
    ttf = sorted(f for f in os.listdir(_p('dist', 'ttf')) if f.endswith('.ttf'))
    woff = sorted(f for f in os.listdir(_p('dist', 'webfonts')) if f.endswith('.woff2'))

    # 1) desktop TTFs
    write_zip(os.path.join(OUT, 'TerminalWorkbenchMono-TTF.zip'),
              [(_p('dist', 'ttf', f), f) for f in ttf]
              + [(_p('OFL.txt'), 'OFL.txt')])

    # 2) web fonts: terminal-workbench-mono.css at root, fonts under fonts/
    write_zip(os.path.join(OUT, 'TerminalWorkbenchMono-WOFF2.zip'),
              [(_p('dist', 'webfonts', f), f'fonts/{f}') for f in woff]
              + [(_p('docs', 'terminal-workbench-mono.css'), 'terminal-workbench-mono.css'),
                 (_p('OFL.txt'), 'OFL.txt')])

    # 3) Obsidian: single self-contained snippet
    write_zip(os.path.join(OUT, 'TerminalWorkbenchMono-Obsidian.zip'),
              [(_p('obsidian', 'terminal-workbench-mono.css'), 'terminal-workbench-mono.css'),
               (_p('OFL.txt'), 'OFL.txt')])

    # 4) checksums over the zips and the raw font binaries
    lines = []
    targets = ([os.path.join(OUT, z) for z in sorted(os.listdir(OUT))
                if z.endswith('.zip')]
               + [_p('dist', 'ttf', f) for f in ttf]
               + [_p('dist', 'webfonts', f) for f in woff])
    for t in targets:
        h = hashlib.sha256(open(t, 'rb').read()).hexdigest()
        lines.append(f'{h}  {os.path.basename(t)}')
    with open(os.path.join(OUT, 'SHA256SUMS.txt'), 'w', newline='\n') as f:
        f.write('\n'.join(lines) + '\n')

    print('packaged into', OUT)
    for n in sorted(os.listdir(OUT)):
        print('  ', n)


if __name__ == '__main__':
    main()
