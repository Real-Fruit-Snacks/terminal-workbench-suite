"""Compile the Terminal Workbench Mono family (TTF + WOFF2).

Six static styles: Regular, Medium, Bold and their italics. Styles past
the RIBBI four use typographic-family name records (16/17) so all six group
under one family in modern apps while staying installable on legacy ones.

Usage:  py tools/build.py
"""

import math
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

import math as _math

from fontTools.fontBuilder import FontBuilder
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.feaLib.builder import addOpenTypeFeaturesFromString
from fontTools.otlLib.builder import buildStatTable
from fontTools.ttLib import newTable
from fontTools.ttLib.tables import ttProgram
from fontTools.ttLib.removeOverlaps import removeOverlaps

from glyphs import GLYPHS, LIGATURES, ALTERNATES, NOTDEF, EXTRA_NAMES
from glyphlab import ADV

FAMILY = "Terminal Workbench Mono"
VERSION = "2.000"
COPYRIGHT = "Copyright 2026 Real-Fruit-Snacks"
UPM = 1000
ASCENT, DESCENT = 960, -260

ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), '..'))

# Nice (AGL) names for ASCII + typographic glyphs; everything else falls
# back to uniXXXX (box-drawing, blocks, Powerline, dingbats).
NICE_NAMES = {
    ' ': 'space', '!': 'exclam', '"': 'quotedbl', '#': 'numbersign',
    '$': 'dollar', '%': 'percent', '&': 'ampersand', "'": 'quotesingle',
    '(': 'parenleft', ')': 'parenright', '*': 'asterisk', '+': 'plus',
    ',': 'comma', '-': 'hyphen', '.': 'period', '/': 'slash',
    '0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
    '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine',
    ':': 'colon', ';': 'semicolon', '<': 'less', '=': 'equal',
    '>': 'greater', '?': 'question', '@': 'at',
    '[': 'bracketleft', '\\': 'backslash', ']': 'bracketright',
    '^': 'asciicircum', '_': 'underscore', '`': 'grave',
    '{': 'braceleft', '|': 'bar', '}': 'braceright', '~': 'asciitilde',
    '–': 'endash', '—': 'emdash',
    '‘': 'quoteleft', '’': 'quoteright',
    '“': 'quotedblleft', '”': 'quotedblright',
    '…': 'ellipsis', '•': 'bullet', '°': 'degree',
    '×': 'multiply', '÷': 'divide', '≠': 'notequal.uni',
    '≤': 'lessequal.uni', '≥': 'greaterequal.uni', '±': 'plusminus',
    '←': 'arrowleft.uni', '↑': 'arrowup.uni',
    '→': 'arrowright.uni', '↓': 'arrowdown.uni',
}
for _c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz':
    NICE_NAMES[_c] = _c
NICE_NAMES.update(EXTRA_NAMES)

REG = 0x40 | 0x80       # REGULAR | USE_TYPO_METRICS
BOLD = 0x20 | 0x80      # BOLD    | USE_TYPO_METRICS
ITAL = 0x01 | 0x80      # ITALIC  | USE_TYPO_METRICS
BDIT = 0x21 | 0x80      # BOLD | ITALIC | USE_TYPO_METRICS
MEDFAM = "Terminal Workbench Mono Medium"  # legacy family for the Medium pair

INSTANCES = [
    # sub, params, skew, weight, legacy_family, ribbi_style, typo_sub, fsSel, macStyle
    ('Regular',       dict(w=86,  cut=165, segs=6), 0.0, 400, FAMILY, 'Regular',     None,            REG,  0x00),
    ('Medium',        dict(w=106, cut=168, segs=6), 0.0, 500, MEDFAM, 'Regular',     'Medium',        REG,  0x00),
    ('Bold',          dict(w=124, cut=172, segs=6), 0.0, 700, FAMILY, 'Bold',        None,            BOLD, 0x01),
    ('Italic',        dict(w=86,  cut=165, segs=6), 8.0, 400, FAMILY, 'Italic',      None,            ITAL, 0x02),
    ('Medium Italic', dict(w=106, cut=168, segs=6), 8.0, 500, MEDFAM, 'Italic',      'Medium Italic', ITAL, 0x02),
    ('Bold Italic',   dict(w=124, cut=172, segs=6), 8.0, 700, FAMILY, 'Bold Italic', None,            BDIT, 0x03),
]

FEA = """
lookup codeligs {
    sub exclam equal equal by notidentical.liga;
    sub equal equal equal by equalequalequal.liga;
    sub colon equal by colonequal.liga;
    sub colon colon by coloncolon.liga;
    sub hyphen greater by arrowright.liga;
    sub less hyphen by arrowleft.liga;
    sub equal greater by darrowright.liga;
    sub exclam equal by notequal.liga;
    sub equal equal by equalequal.liga;
    sub less equal by lessequal.liga;
    sub greater equal by greaterequal.liga;
} codeligs;

feature calt { lookup codeligs; } calt;
feature liga { lookup codeligs; } liga;
feature ss01 { sub zero by zero.dotted; } ss01;
"""


def signed_area(pts):
    s = 0.0
    for i in range(len(pts)):
        x0, y0 = pts[i]
        x1, y1 = pts[(i + 1) % len(pts)]
        s += x0 * y1 - x1 * y0
    return s / 2.0


def draw_glyph(shapes, skew_tan):
    """Return (Glyph, xMin) for a shape list."""
    pen = TTGlyphPen(None)
    xmin = None
    for kind, pts in shapes:
        a = signed_area(pts)
        if (kind == 'fill' and a < 0) or (kind == 'hole' and a > 0):
            pts = pts[::-1]
        out = []
        for x, y in pts:
            if skew_tan:
                x = x + (y - 300.0) * skew_tan
            xi, yi = round(x), round(y)
            out.append((xi, yi))
            xmin = xi if xmin is None else min(xmin, xi)
        pen.moveTo(out[0])
        for p in out[1:]:
            pen.lineTo(p)
        pen.closePath()
    return pen.glyph(), (0 if xmin is None else xmin)


def gname(ch):
    return NICE_NAMES.get(ch) or ('uni%04X' % ord(ch))


def make_glyphs(P, skew_tan):
    """Build all glyphs for one style; return order/cmap/glyphs/metrics + bbox."""
    glyph_order = ['.notdef', 'space']
    cmap = {0x0020: 'space', 0x00A0: 'space'}
    glyphs, metrics = {}, {}
    ymax, ymin = ASCENT, DESCENT

    def add(name, shapes, adv):
        nonlocal ymax, ymin
        g, xmin = draw_glyph(shapes, skew_tan)
        glyph_order.append(name)
        glyphs[name] = g
        metrics[name] = (adv, xmin)
        for _k, pts in shapes:
            for _x, y in pts:
                ymax = max(ymax, y); ymin = min(ymin, y)
        return g

    g, _ = draw_glyph(NOTDEF(P), skew_tan)
    glyphs['.notdef'] = g
    metrics['.notdef'] = (ADV, 100)
    glyphs['space'] = TTGlyphPen(None).glyph()
    metrics['space'] = (ADV, 0)

    for ch in sorted((c for c in GLYPHS if len(c) == 1 and c != ' '), key=ord):
        add(gname(ch), GLYPHS[ch](P), ADV)
        cmap[ord(ch)] = gname(ch)
    for name, fn, adv in ALTERNATES:          # ss01 etc., reached via GSUB
        add(name, fn(P), adv)
    for name, comps, fn, adv in LIGATURES:
        add(name, fn(P), adv)

    return dict(order=glyph_order, cmap=cmap, glyphs=glyphs, metrics=metrics,
                ymax=ymax, ymin=ymin)


def assemble(sub, P, skew_deg, weight, legacy_fam, ribbi, typo_sub,
             fs_sel, mac_style, data, win_asc, win_desc):
    skew_tan = math.tan(math.radians(skew_deg))
    is_italic = skew_deg != 0
    glyph_order = data['order']
    ps_name = f"{FAMILY.replace(' ', '')}-{sub.replace(' ', '')}"

    fb = FontBuilder(UPM, isTTF=True)
    fb.setupGlyphOrder(glyph_order)
    fb.setupCharacterMap(data['cmap'])
    fb.setupGlyf(data['glyphs'])
    fb.setupHorizontalMetrics(data['metrics'])
    fb.setupHorizontalHeader(ascent=ASCENT, descent=DESCENT, lineGap=0)

    fb.setupNameTable({
        'copyright': COPYRIGHT,
        'familyName': legacy_fam,
        'styleName': ribbi,
        'uniqueFontIdentifier': f'{ps_name};{VERSION};2026',
        'fullName': f'{FAMILY} {sub}',
        'version': f'Version {VERSION}',
        'psName': ps_name,
        'designer': 'Real-Fruit-Snacks',
        'manufacturer': 'Real-Fruit-Snacks',
        'description': 'The official monospace of the Terminal Workbench '
                       'design system: clean geometric letterforms for '
                       'terminals, notes and code.',
        'licenseDescription': 'Licensed under the SIL Open Font License, '
                              'Version 1.1.',
        'licenseInfoURL': 'https://openfontlicense.org',
    }, mac=False)   # Windows-platform name records only
    # Typographic family/subfamily so the Medium pair groups under "Terminal
    # Workbench Mono" in modern apps; omitted for RIBBI styles to avoid redundant records.
    if typo_sub is not None:
        name = fb.font['name']
        name.setName(FAMILY, 16, 3, 1, 0x409)
        name.setName(typo_sub, 17, 3, 1, 0x409)

    fb.setupOS2(
        sTypoAscender=ASCENT, sTypoDescender=DESCENT, sTypoLineGap=0,
        usWeightClass=weight, usWidthClass=5,
        fsSelection=fs_sel,
        panose=dict(bFamilyType=2, bSerifStyle=11,
                    bWeight=8 if weight == 700 else (6 if weight == 500 else 5),
                    bProportion=9, bContrast=2, bStrokeVariation=2,
                    bArmStyle=3, bLetterForm=2, bMidline=2, bXHeight=4),
        sxHeight=540, sCapHeight=700,
        achVendID='RFSN',
        usWinAscent=win_asc, usWinDescent=win_desc,
        ulCodePageRange1=0x00000001,   # bit 0: Latin 1 (cp1252) — Windows needs this
    )
    fb.font['OS/2'].version = 4
    fb.font['OS/2'].fsSelection = fs_sel
    fb.font['OS/2'].recalcUnicodeRanges(fb.font, pruneOnly=False)
    fb.font['head'].macStyle = mac_style
    fb.font['head'].fontRevision = round(float(VERSION), 3)   # match name ID 5

    fb.setupPost(isFixedPitch=1, italicAngle=-skew_deg,
                 underlinePosition=-120, underlineThickness=60)
    if is_italic:
        hhea = fb.font['hhea']
        hhea.caretSlopeRise = 1000
        hhea.caretSlopeRun = round(skew_tan * 1000)

    addOpenTypeFeaturesFromString(fb.font, FEA)
    removeOverlaps(fb.font)

    # gasp: grid-fit + grayscale at every size for crisp small rendering
    gasp = newTable('gasp')
    gasp.version = 1
    gasp.gaspRange = {0xFFFF: 0x000F}
    fb.font['gasp'] = gasp

    # STAT: locate this static within the family's weight + italic axes
    wname = {400: 'Regular', 500: 'Medium', 700: 'Bold'}[weight]
    wval = {'name': wname, 'value': weight}
    if weight == 400:
        wval['flags'] = 0x2  # ELIDABLE
    if is_italic:
        ival = {'name': 'Italic', 'value': 1}
    else:
        ival = {'name': 'Roman', 'value': 0, 'flags': 0x2, 'linkedValue': 1}
    buildStatTable(fb.font,
                   [{'tag': 'wght', 'name': 'Weight', 'values': [wval]},
                    {'tag': 'ital', 'name': 'Italic', 'values': [ival]}],
                   elidedFallbackName=2)

    # prep program: enable dropout control + grayscale smoothing at all sizes
    prep = newTable('prep')
    prep.program = ttProgram.Program()
    prep.program.fromBytecode(b'\xb8\x01\xff\x85\xb0\x04\x8d')
    fb.font['prep'] = prep

    # keep Windows-platform name records only (STAT may have added Mac ones)
    nt = fb.font['name']
    nt.names = [n for n in nt.names if n.platformID == 3]

    ttf_dir = os.path.join(ROOT, 'dist', 'ttf')
    web_dir = os.path.join(ROOT, 'dist', 'webfonts')
    os.makedirs(ttf_dir, exist_ok=True)
    os.makedirs(web_dir, exist_ok=True)

    fb.font.save(os.path.join(ttf_dir, f'{ps_name}.ttf'))
    fb.font.flavor = 'woff2'
    fb.font.save(os.path.join(web_dir, f'{ps_name}.woff2'))
    print('built', ps_name, f'({len(glyph_order)} glyphs)')


def main():
    # pass 1: build every style's glyphs, find the family-wide ink bbox
    built = []
    gymax, gymin = ASCENT, DESCENT
    for inst in INSTANCES:
        sub, P, skew_deg = inst[0], inst[1], inst[2]
        data = make_glyphs(P, math.tan(math.radians(skew_deg)))
        gymax, gymin = max(gymax, data['ymax']), min(gymin, data['ymin'])
        built.append((inst, data))
    win_asc, win_desc = _math.ceil(gymax), _math.ceil(-gymin)
    # pass 2: assemble each style with identical Win metrics across the family
    for inst, data in built:
        assemble(*inst, data, win_asc, win_desc)


if __name__ == '__main__':
    main()
