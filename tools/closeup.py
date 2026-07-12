"""Large close-up of a few glyphs from the compiled font for inspection."""
import os, sys
from PIL import Image, ImageDraw, ImageFont
ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), '..'))
TTF = os.path.join(ROOT, 'dist', 'ttf')
text = sys.argv[1] if len(sys.argv) > 1 else "@ & § © ® € µ ø ß ¶ ¢ £"
f = ImageFont.truetype(os.path.join(TTF, 'TerminalWorkbenchMono-Regular.ttf'), 130)
img = Image.new('RGB', (1500, 230), (11, 16, 24))
ImageDraw.Draw(img).text((30, 30), text, font=f, fill=(226, 233, 240))
out = os.path.join(ROOT, 'preview', 'closeup.png')
img.save(out); print('wrote', out)
