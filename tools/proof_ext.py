"""QA sheet for the extended coverage, rendered from the compiled TTF.

Box-drawing is rendered with the line step set to the font's cell height so
seamless vertical tiling can be verified.
"""

import os
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), '..'))
TTF = os.path.join(ROOT, 'dist', 'ttf')
BG = (11, 16, 24)
FG = (226, 233, 240)
ACCENT = (126, 211, 211)
DIM = (138, 152, 166)


def font(style, px):
    return ImageFont.truetype(os.path.join(TTF, f'TerminalWorkbenchMono-{style}.ttf'), px)


TABLE = [
    "┌────────────┬───────────┐",
    "│ host       │ status    │",
    "├────────────┼───────────┤",
    "│ 10.0.1.7   │ 0wned     │",
    "│ workbench  │ Il1 5S 8B │",
    "╰────────────┴───────────╯",
]
DOUBLE = [
    "╔═══════════╗",
    "║ secure ░▒▓ ║",
    "╚═══════════╝",
]


def main():
    W, H = 1180, 1180
    img = Image.new('RGB', (W, H), BG)
    d = ImageDraw.Draw(img)
    x = 44
    y = 34
    d.text((x, y), "Terminal Workbench Mono — extended coverage", font=font('Bold', 30), fill=ACCENT)
    y += 64

    d.text((x, y), "accented latin-1", font=font('Regular', 13), fill=DIM); y += 22
    for line in ["à á â ã ä å  è é ê ë  ì í î ï  ñ  ò ó ô õ ö",
                 "ù ú û ü  ý ÿ ç  ø Ø ß  À É Î Ñ Ö Ü Ç"]:
        d.text((x, y), line, font=font('Regular', 26), fill=FG); y += 38
    y += 14

    d.text((x, y), "symbols", font=font('Regular', 13), fill=DIM); y += 22
    d.text((x, y), "© ® ™  € £ ¥ ¢ µ  « » ·  § ¶  † ‡  ✓ ✗  ¿ ¡",
           font=font('Regular', 26), fill=FG); y += 46

    d.text((x, y), "box-drawing (line step = cell height; lines should connect)",
           font=font('Regular', 13), fill=DIM); y += 22
    bf = font('Regular', 26)
    step = sum(bf.getmetrics())          # exact px line height -> seamless tiling
    fy = float(y)
    for line in TABLE:
        d.text((x, fy), line, font=bf, fill=FG, anchor='la'); fy += step
    fy2 = float(y)
    bf2 = font('Bold', 26)
    for line in DOUBLE:
        d.text((x + 470, fy2), line, font=bf2, fill=ACCENT, anchor='la'); fy2 += step
    y = int(fy) + 16

    d.text((x, y), "blocks · eighths · shades", font=font('Regular', 13), fill=DIM); y += 22
    d.text((x, y), "█ ▉ ▊ ▋ ▌ ▍ ▎ ▏   ▁▂▃▄▅▆▇█   ░ ▒ ▓   ▖▗▘▙▚▛▜▝▞▟",
           font=font('Regular', 26), fill=FG); y += 44

    d.text((x, y), "powerline separators (E0B0–E0B3)", font=font('Regular', 13), fill=DIM); y += 22
    d.text((x, y), "   ", font=font('Regular', 30), fill=FG)
    # composed prompt segment: solid block then a right-triangle hand-off
    seg = font('Regular', 30)
    d.rectangle([x + 250, y - 4, x + 250 + d.textlength(" usr ", font=seg), y + 32], fill=ACCENT)
    d.text((x + 250, y), " usr ", font=seg, fill=BG)
    d.text((x + 250 + d.textlength(" usr ", font=seg), y), "", font=seg, fill=ACCENT)
    y += 50

    d.text((x, y), "medium weight (new)", font=font('Regular', 13), fill=DIM); y += 22
    d.text((x, y), "Regular vs Medium vs Bold — the tide turns",
           font=font('Regular', 24), fill=FG); y += 34
    d.text((x, y), "Regular vs Medium vs Bold — the tide turns",
           font=font('Medium', 24), fill=FG); y += 34
    d.text((x, y), "Regular vs Medium vs Bold — the tide turns",
           font=font('Bold', 24), fill=FG); y += 40

    out = os.path.join(ROOT, 'preview', 'proof-ext.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
