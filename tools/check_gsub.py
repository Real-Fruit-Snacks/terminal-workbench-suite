"""Confirm ligature substitution rules in the compiled font."""
import os
from fontTools.ttLib import TTFont

ttf = os.path.join(os.path.dirname(__file__), '..', 'dist', 'ttf',
                   'TerminalWorkbenchMono-Regular.ttf')
g = TTFont(ttf)['GSUB'].table
feats = sorted({r.FeatureTag for r in g.FeatureList.FeatureRecord})
print('features:', feats)
for lk in g.LookupList.Lookup:
    for s in lk.SubTable:
        if hasattr(s, 'ligatures'):          # ligature substitution
            for first, ligs in s.ligatures.items():
                for lig in ligs:
                    print('  lig', first, '+', ' + '.join(lig.Component), '->', lig.LigGlyph)
        elif hasattr(s, 'mapping'):           # single substitution (ss01)
            for src, dst in s.mapping.items():
                print('  alt', src, '->', dst)
