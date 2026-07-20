"""Large-size renders of tricky glyphs for close inspection."""

import os, sys
sys.path.insert(0, os.path.dirname(__file__))

from PIL import Image, ImageDraw
from glyphs import GLYPHS, LIGATURES
from glyphlab import ADV
from chart import REG, BOLD, draw_glyph, draw_text, BG, FG, SS


def main():
    lines = [
        ('&%@QRKMNW', REG),
        ('gjy359?!,;', REG),
        ('(){}[]<>/\\', REG),
        ("‘’“”`'\"^~*", REG),
        ('aegs&Q358', BOLD),
    ]
    em = 150 * SS
    W, H = 1500 * SS, (len(lines) * 180 + 60) * SS
    img = Image.new('RGB', (W, H), BG)
    d = ImageDraw.Draw(img)
    y = 150 * SS
    for text, P in lines:
        draw_text(d, text, 40 * SS, y, em, P, FG)
        y += 180 * SS
    img = img.resize((W // SS, H // SS), Image.LANCZOS)
    out = os.path.join(os.path.dirname(__file__), '..', 'preview', 'zoom.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
