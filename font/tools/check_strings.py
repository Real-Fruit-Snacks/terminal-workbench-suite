"""Scan every name-table string in the built fonts for a given substring."""
import glob
import os
import sys

from fontTools.ttLib import TTFont

if len(sys.argv) < 2:
    sys.exit('usage: py tools/check_strings.py <substring>')
needle = sys.argv[1].lower()
ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), '..'))
hits = 0
for p in (glob.glob(os.path.join(ROOT, 'dist', '**', '*.ttf'), recursive=True)
          + glob.glob(os.path.join(ROOT, 'dist', '**', '*.woff2'), recursive=True)):
    f = TTFont(p)
    for rec in f['name'].names:
        s = rec.toUnicode()
        if needle in s.lower():
            print(f'HIT {os.path.basename(p)} nameID={rec.nameID}: {s}')
            hits += 1
print('clean' if hits == 0 else f'{hits} hits')
