"""Assert every compiled font is attributed only to the project handle.

Positive check (so this file never needs to spell any forbidden string):
the designer / manufacturer / copyright must be the handle, and no name
record may contain an '@' (i.e. no e-mail address leaked in). Exits non-zero
on any violation so CI fails loudly.
"""

import glob
import os
import sys

from fontTools.ttLib import TTFont

HANDLE = 'Real-Fruit-Snacks'
ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), '..'))

problems = []
fonts = glob.glob(os.path.join(ROOT, 'dist', 'ttf', '*.ttf'))
if not fonts:
    sys.exit('no fonts found — run tools/build.py first')

for path in fonts:
    base = os.path.basename(path)
    name = TTFont(path)['name']
    designer = name.getDebugName(9)
    manufacturer = name.getDebugName(8)
    copyright_ = name.getDebugName(0) or ''
    if designer != HANDLE:
        problems.append(f'{base}: designer is {designer!r}, expected {HANDLE!r}')
    if manufacturer != HANDLE:
        problems.append(f'{base}: manufacturer is {manufacturer!r}, expected {HANDLE!r}')
    if HANDLE not in copyright_:
        problems.append(f'{base}: copyright {copyright_!r} lacks {HANDLE!r}')
    for rec in name.names:
        s = rec.toUnicode()
        if '@' in s:
            problems.append(f'{base}: name ID {rec.nameID} contains an address: {s!r}')

if problems:
    print('IDENTITY CHECK FAILED:')
    for p in problems:
        print('  !', p)
    sys.exit(1)
print(f'identity OK: {len(fonts)} fonts attributed to {HANDLE} only')
