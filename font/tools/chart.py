"""Render a full glyph chart + text samples for visual QA (pre-compile)."""

import os, sys
sys.path.insert(0, os.path.dirname(__file__))

from PIL import Image, ImageDraw
from glyphs import GLYPHS, LIGATURES, NOTDEF
from glyphlab import ADV

SS = 3
BG = (11, 16, 24)
FG = (226, 233, 240)
GRID = (28, 38, 52)

REG = dict(w=86, cut=165, segs=6)
BOLD = dict(w=124, cut=172, segs=6)

CHART_ORDER = (
    "ABCDEFGHIJKLM" "NOPQRSTUVWXYZ"
    "abcdefghijklm" "nopqrstuvwxyz"
    "0123456789" + '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    + '–—‘’“”…•°×÷≠≤≥±←↑→↓'
)


def draw_glyph(d, shapes, ox_px, base_px, sc, color):
    for kind, pts in shapes:
        poly = [(ox_px + x * sc, base_px - y * sc) for x, y in pts]
        d.polygon(poly, fill=(color if kind == 'fill' else BG))


def draw_text(d, text, x_px, base_px, em, P, color):
    sc = em / 1000.0
    for ch in text:
        fn = GLYPHS.get(ch)
        if fn:
            draw_glyph(d, fn(P), x_px, base_px, sc, color)
        x_px += ADV * sc
    return x_px


def main():
    cols, cell = 13, 110 * SS
    rows = (len(CHART_ORDER) + cols - 1) // cols
    em = 76 * SS
    sc = em / 1000.0

    W = cols * cell + 80 * SS
    H = rows * cell + 540 * SS
    img = Image.new('RGB', (W, H), BG)
    d = ImageDraw.Draw(img)

    # glyph grid
    for i, ch in enumerate(CHART_ORDER):
        r, c = divmod(i, cols)
        ox = 40 * SS + c * cell + 18 * SS
        base = 40 * SS + r * cell + 86 * SS
        d.rectangle([ox - 14 * SS, base - 86 * SS, ox - 14 * SS + cell - 8 * SS, base + 20 * SS],
                    outline=GRID, width=SS)
        draw_glyph(d, GLYPHS[ch](REG), ox, base, sc, FG)

    y = 40 * SS + rows * cell + 70 * SS
    draw_text(d, 'Sphinx of black quartz, judge my vow! 0123456789', 40 * SS, y, 42 * SS, REG, FG)
    y += 78 * SS
    draw_text(d, 'how vexingly quick daft zebras jump? {[(|/\\)]} *&^%#@', 40 * SS, y, 42 * SS, REG, FG)
    y += 90 * SS
    draw_text(d, 'Sphinx of black quartz — judge my vow. “Quotes’ test”…', 40 * SS, y, 42 * SS, BOLD, FG)
    y += 100 * SS

    # ligatures
    x = 40 * SS
    for name, comps, fn, adv in LIGATURES:
        draw_glyph(d, fn(REG), x, y, sc, FG)
        x += adv * sc + 30 * SS
    draw_glyph(d, NOTDEF(REG), x, y, sc, FG)

    img = img.resize((W // SS, H // SS), Image.LANCZOS)
    out = os.path.join(os.path.dirname(__file__), '..', 'preview', 'chart.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
