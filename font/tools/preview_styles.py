"""Render the three style candidates to PNGs for the comparison page."""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from PIL import Image, ImageDraw

from glyphlab import GLYPHS, STYLES, ADV

SS = 3  # supersample factor

BG = (11, 16, 24)
FG = (223, 231, 239)
ACCENT = (126, 211, 211)
DIM = (130, 145, 160)


def draw_line(draw, text, x_px, baseline_px, em_px, P, color):
    sc = em_px / 1000.0
    pen_x = x_px
    for ch in text:
        fn = GLYPHS.get(ch)
        if fn is not None:
            for kind, pts in fn(P):
                poly = [(pen_x + px * sc, baseline_px - py * sc) for px, py in pts]
                draw.polygon(poly, fill=(color if kind == 'fill' else BG))
        pen_x += ADV * sc
    return pen_x


def render_style(name, P, out_path):
    W, H = 1480 * SS, 760 * SS
    img = Image.new('RGB', (W, H), BG)
    d = ImageDraw.Draw(img)
    pad = 56 * SS

    y = pad + 120 * SS
    draw_line(d, 'West$ ssh root@10.0.1.7', pad, y, 92 * SS, P, FG)

    y += 150 * SS
    draw_line(d, '0O 1lI {x} != ~', pad, y, 92 * SS, P, ACCENT)

    y += 122 * SS
    draw_line(d, 'obsidian watershed notes -> threat detail', pad, y, 46 * SS, P, FG)

    y += 86 * SS
    draw_line(d, 'shell root tide data harbor shoreline :: lateral?', pad, y, 36 * SS, P, DIM)

    y += 96 * SS
    draw_line(d, 'the tide drains north and washes data ashore - isolate inbound hosts',
              pad, y, 25 * SS, P, DIM)

    img = img.resize((W // SS, H // SS), Image.LANCZOS)
    img.save(out_path)
    print('wrote', out_path)


def main():
    out_dir = os.path.join(os.path.dirname(__file__), '..', 'preview')
    os.makedirs(out_dir, exist_ok=True)
    for name, P in STYLES.items():
        render_style(name, P, os.path.join(out_dir, f'style-{name}.png'))


if __name__ == '__main__':
    main()
