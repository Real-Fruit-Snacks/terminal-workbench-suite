"""Sanity-check every compiled TTF: naming, monospace, metrics, cmap, GSUB."""
import os
from fontTools.ttLib import TTFont

ROOT = os.path.join(os.path.dirname(__file__), '..')
TTF = os.path.join(ROOT, 'dist', 'ttf')

STYLES = {
    'Regular': 400, 'Medium': 500, 'Bold': 700,
    'Italic': 400, 'MediumItalic': 500, 'BoldItalic': 700,
}
CELL_ADVANCES = {600, 1200, 1800}   # single + double/triple-wide ligatures

ok = True
for st, expect_weight in STYLES.items():
    path = os.path.join(TTF, f'TerminalWorkbenchMono-{st}.ttf')
    f = TTFont(path)
    post, os2, head = f['post'], f['OS/2'], f['head']
    name, hmtx = f['name'], f['hmtx']

    glyph_advs = {g: w for g, (w, _) in hmtx.metrics.items()}
    bad_adv = {g: w for g, w in glyph_advs.items() if w not in CELL_ADVANCES}

    problems = []
    if post.isFixedPitch != 1:
        problems.append('post.isFixedPitch != 1')
    if bad_adv:
        problems.append(f'non-cell advances: {bad_adv}')
    if os2.usWeightClass != expect_weight:
        problems.append(f'weightClass={os2.usWeightClass} != {expect_weight}')
    if ('Italic' in st) != bool(head.macStyle & 0x2):
        problems.append('macStyle italic mismatch')
    if ('Bold' in st) != bool(head.macStyle & 0x1):
        problems.append('macStyle bold mismatch')
    if 'gasp' not in f:
        problems.append('no gasp table')
    if 'GSUB' not in f:
        problems.append('no GSUB')
    else:
        feats = {r.FeatureTag for r in f['GSUB'].table.FeatureList.FeatureRecord}
        for need in ('calt', 'liga', 'ss01'):
            if need not in feats:
                problems.append(f'missing feature {need}')

    cmap = f.getBestCmap()
    needed = list('AZaz09@&#$') + ['é', '─', '█', '€', '✓']
    for ch in needed:
        if ord(ch) not in cmap:
            problems.append(f'missing cmap U+{ord(ch):04X} ({ch})')

    if problems:
        ok = False
    print(f'{"OK " if not problems else "XX "}{st:13} '
          f'w={os2.usWeightClass} italic={post.italicAngle:>4} '
          f'glyphs={len(glyph_advs)} advances={sorted(set(glyph_advs.values()))}')
    for p in problems:
        print('      !', p)

print('\nALL PASS' if ok else '\nFAILURES ABOVE')
