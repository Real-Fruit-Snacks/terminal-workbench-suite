"""Proof sheets rendered from the COMPILED TTFs via FreeType (PIL).

This exercises the real font files: windings, cmap, metrics, all four styles.
"""

import os
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), '..'))
TTF = os.path.join(ROOT, 'dist', 'ttf')

BG = (11, 16, 24)
FG = (226, 233, 240)
ACCENT = (126, 211, 211)
DIM = (138, 152, 166)

PANGRAM = 'Sphinx of black quartz, judge my vow.'
CODE = "nmap -sV --top-ports 1000 10.0.1.0/24 | grep 'open'"
HEX = '0x7FDE 0xDEADBEEF c2:5e:99 SHA256 d41d8cd98f00b204'
CONFUSE = '0O Il1 5S 8B rn/m cl/d g9 ~- {[()]} <>'
NOTES = ('Lateral movement via stolen kerberos tickets — the attacker '
         'pivoted from DMZ to the build server. “Contain first, ask later.”')


def font(style, px):
    return ImageFont.truetype(os.path.join(TTF, f'TerminalWorkbenchMono-{style}.ttf'), px)


def main():
    W, H = 1560, 1290
    img = Image.new('RGB', (W, H), BG)
    d = ImageDraw.Draw(img)
    x = 48
    y = 40

    d.text((x, y), 'Terminal Workbench Mono — compiled proof', font=font('Bold', 34), fill=ACCENT)
    y += 78

    for label, style, px, text, color in [
        ('Regular 28px', 'Regular', 28, PANGRAM + ' 0123456789', FG),
        ('Bold 28px', 'Bold', 28, PANGRAM, FG),
        ('Italic 28px', 'Italic', 28, PANGRAM, FG),
        ('BoldItalic 28px', 'BoldItalic', 28, PANGRAM, FG),
        ('code 24px', 'Regular', 24, CODE, ACCENT),
        ('hex 24px', 'Regular', 24, HEX, FG),
        ('confusables 28px', 'Regular', 28, CONFUSE, FG),
        ('confusables bold', 'Bold', 28, CONFUSE, FG),
    ]:
        d.text((x, y), label, font=font('Regular', 13), fill=DIM)
        y += 22
        d.text((x, y), text, font=font(style, px), fill=color)
        y += px + 26

    # body-size wrap test
    d.text((x, y), 'notes 17px', font=font('Regular', 13), fill=DIM)
    y += 22
    f17 = font('Regular', 17)
    words = NOTES.split()
    line = ''
    for w_ in words:
        t = (line + ' ' + w_).strip()
        if d.textlength(t, font=f17) > W - 96:
            d.text((x, y), line, font=f17, fill=FG)
            y += 26
            line = w_
        else:
            line = t
    d.text((x, y), line, font=f17, fill=FG)
    y += 44

    # tiny sizes
    for px in (14, 12):
        d.text((x, y), f'{px}px', font=font('Regular', 13), fill=DIM)
        y += 20
        d.text((x, y), CODE + '  ' + CONFUSE, font=font('Regular', px), fill=FG)
        y += px + 18

    # full charset at 22px
    y += 10
    charset = (' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ'
               '[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~–—‘’“”…•°×÷≠≤≥±←↑→↓')
    f22 = font('Regular', 22)
    for i in range(0, len(charset), 44):
        d.text((x, y), charset[i:i + 44], font=f22, fill=FG)
        y += 36

    out = os.path.join(ROOT, 'preview', 'proof.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
