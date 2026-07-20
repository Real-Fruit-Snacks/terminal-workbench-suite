"""Show box-drawing tiling at line-height 1.5 (gappy) vs 1.2 (the fix)."""
import os
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), '..'))
TTF = os.path.join(ROOT, 'dist', 'ttf')
BG, FG, DIM = (11, 16, 24), (226, 233, 240), (138, 152, 166)
TABLE = ["┌──────────┬──────────┐",
         "│ host     │ status   │",
         "├──────────┼──────────┤",
         "│ 10.0.1.7 │ 0wned    │",
         "╰──────────┴──────────╯"]
sz = 30
f = ImageFont.truetype(os.path.join(TTF, 'TerminalWorkbenchMono-Regular.ttf'), sz)
img = Image.new('RGB', (760, 320), BG)
d = ImageDraw.Draw(img)
for col, (lh, label) in enumerate([(1.5, "line-height 1.5  (gaps)"),
                                   (1.2, "line-height 1.2  (fixed)")]):
    x = 30 + col * 380
    d.text((x, 16), label, font=ImageFont.truetype(os.path.join(TTF, 'TerminalWorkbenchMono-Regular.ttf'), 13), fill=DIM)
    y = 56.0
    for line in TABLE:
        d.text((x, y), line, font=f, fill=FG, anchor='la')
        y += sz * lh
out = os.path.join(ROOT, 'preview', 'lineheight.png')
img.save(out); print('wrote', out)
