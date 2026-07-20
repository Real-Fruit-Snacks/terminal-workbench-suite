"""Accented Latin-1 letters, common symbols, extra ligatures, dotted zero.

Exposes register(GLYPHS, LIGATURES, ALTERNATES) which mutates the three
in place, plus EXTRA_NAMES mapping the new characters to AGL glyph names.
Accented letters are composed from existing base letters + accent marks,
so they inherit weight/skew automatically.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from glyphlab import (bar_h, bar_v, path, boxring, dot, stroke, cornerize,
                      CX, XL, XR, OL, OR, CAP_C, XH_C, ASC_C, BASE_C)

CAPDY = 150  # lift marks from lowercase height to cap height


def _shift(shapes, dy):
    if not dy:
        return shapes
    return [(k, [(x, y + dy) for x, y in pts]) for k, pts in shapes]


def _rot180(shapes):
    # rotate 180 degrees about the glyph center (300, 350)
    return [(k, [(600 - x, 700 - y) for x, y in pts]) for k, pts in shapes]

# ----------------------------------------------------------- accent marks
# drawn at lowercase height (above x-height); dy lifts them for capitals


def _m_acute(P, dy): return _shift(path([(262, 566), (342, 676)], P['w'] * 0.92), dy)
def _m_grave(P, dy): return _shift(path([(258, 676), (338, 566)], P['w'] * 0.92), dy)
def _m_circ(P, dy):  return _shift(path([(244, 612), (300, 692), (356, 612)], P['w'] * 0.82, cuts=20), dy)
def _m_caron(P, dy): return _shift(path([(244, 692), (300, 612), (356, 692)], P['w'] * 0.82, cuts=20), dy)


def _m_tilde(P, dy):
    pts = [(240, 626), (286, 664), (314, 624), (360, 662)]
    if P['segs'] > 1:
        pts = cornerize(pts, 40, P['segs'])
    return _shift(path(pts, P['w'] * 0.78), dy)


def _m_diaer(P, dy):
    return _shift(dot(256, 632, P['w'] * 1.25, P) + dot(344, 632, P['w'] * 1.25, P), dy)


def _m_ring(P, dy):
    return _shift(boxring(262, 600, 338, 690, P['w'] * 0.58, P['cut'] * 0.4, P['segs']), dy)


def _m_cedilla(P, dy):
    return path([(312, 8), (300, -58), (250, -150)], P['w'] * 0.74, cuts=40, segs=P['segs'])

# ----------------------------------------------------------- extra bases


def _g_idotless(P):
    w = P['w']
    return (bar_v(CX, 0, XH_C + w / 2, w)
            + bar_h(XH_C, 205, 300, w) + bar_h(BASE_C, 160, 440, w))


def _g_oslash(P):
    return path([(108, -18), (492, 558)], P['w'] * 0.66) + __import__('glyphs').GLYPHS['o'](P)


def _g_Oslash(P):
    return path([(96, -26), (504, 690)], P['w'] * 0.72) + __import__('glyphs').GLYPHS['O'](P)


def _g_germandbls(P):
    w = P['w']
    return (bar_v(XL, 0, 540, w)
            + path([(XL, 470), (XL, 610), (385, 610), (385, 300), (470, 300),
                    (470, 120), (330, 58)], w, cuts=58, segs=P['segs']))

# ----------------------------------------------------------------- symbols


def _g_copyright(P):
    w = P['w']
    ring = boxring(70, 10, 530, 640, w * 0.6, 230, P['segs'])
    c = path([(388, 408), (286, 408), (286, 242), (388, 242)], w * 0.56, cuts=70, segs=P['segs'])
    return ring + c


def _g_registered(P):
    w = P['w']
    ring = boxring(70, 10, 530, 640, w * 0.6, 230, P['segs'])
    stem = bar_v(286, 242, 408, w * 0.5)
    bowl = path([(286, 408), (372, 408), (372, 330), (286, 330)], w * 0.5)
    leg = path([(330, 330), (388, 242)], w * 0.5)
    return ring + stem + bowl + leg


def _g_trademark(P):
    w = P['w']
    t = bar_h(640, 95, 250, w * 0.62) + bar_v(172, 470, 668, w * 0.62)
    m = path([(290, 470), (290, 668), (372, 560), (454, 668), (454, 470)],
             w * 0.62, cuts=18)
    return t + m


def _g_euro(P):
    import glyphs
    return (glyphs.GLYPHS['C'](P)
            + bar_h(392, 36, 430, P['w'] * 0.82) + bar_h(286, 36, 430, P['w'] * 0.82))


def _g_sterling(P):
    w = P['w']
    return (path([(452, 566), (332, 612), (236, 542), (236, 88)], w, cuts=60, segs=P['segs'])
            + bar_h(45, 120, 486, w) + bar_h(300, 150, 408, w * 0.85))


def _g_yen(P):
    import glyphs
    return (glyphs.GLYPHS['Y'](P)
            + bar_h(300, 150, 450, P['w'] * 0.8) + bar_h(208, 150, 450, P['w'] * 0.8))


def _g_cent(P):
    import glyphs
    return glyphs.GLYPHS['c'](P) + bar_v(CX, -38, 596, P['w'] * 0.66)


def _g_mu(P):
    import glyphs
    return glyphs.GLYPHS['u'](P) + bar_v(XL, -210, 70, P['w'])


def _g_guilleft(P):
    w = P['w'] * 0.85
    return (path([(286, 420), (168, 275), (286, 130)], w, cuts=18)
            + path([(420, 420), (302, 275), (420, 130)], w, cuts=18))


def _g_guilright(P):
    w = P['w'] * 0.85
    return (path([(314, 420), (432, 275), (314, 130)], w, cuts=18)
            + path([(180, 420), (298, 275), (180, 130)], w, cuts=18))


def _g_periodcentered(P):
    return dot(CX, 300, P['w'] * 1.5, P)


def _g_section(P):
    w = P['w'] * 0.88
    # upper bowl opening lower-right, lower bowl opening upper-left, crossed
    top = path([(414, 506), (414, 588), (300, 642), (190, 590), (300, 432),
                (420, 372)], w, cuts=120, segs=P['segs'])
    bot = path([(186, 222), (186, 140), (300, 86), (410, 138), (300, 296),
                (180, 356)], w, cuts=120, segs=P['segs'])
    return top + bot


def _g_paragraph(P):
    w = P['w']
    return (bar_v(420, -40, 660, w) + bar_v(300, -40, 660, w)
            + boxring(150, 350, 462, 660, w, 150, P['segs']))


def _g_dagger(P):
    return bar_v(CX, -50, 642, P['w'] * 0.85) + bar_h(508, 178, 422, P['w'] * 0.85)


def _g_daggerdbl(P):
    return (bar_v(CX, -50, 642, P['w'] * 0.85)
            + bar_h(528, 178, 422, P['w'] * 0.8) + bar_h(110, 178, 422, P['w'] * 0.8))


def _g_check(P):
    return path([(140, 322), (268, 150), (478, 588)], P['w'] * 1.05, cuts=20)


def _g_ballotx(P):
    return (path([(150, 560), (450, 110)], P['w'])
            + path([(450, 560), (150, 110)], P['w']))


def _mk_invert(base_ch):
    def fn(P, base_ch=base_ch):
        import glyphs
        return _rot180(glyphs.GLYPHS[base_ch](P))
    return fn

# ---------------------------------------------------------- wide ligatures


def _l_colonequal(P):
    return (dot(300, 400, P['w'] * 1.42, P) + dot(300, 62, P['w'] * 1.42, P)
            + bar_h(352, 690, 1110, P['w']) + bar_h(198, 690, 1110, P['w']))


def _l_coloncolon(P):
    s = P['w'] * 1.42
    return (dot(300, 400, s, P) + dot(300, 62, s, P)
            + dot(900, 400, s, P) + dot(900, 62, s, P))


def _l_eq3(P):
    return bar_h(352, 110, 1690, P['w']) + bar_h(198, 110, 1690, P['w'])


def _l_notid(P):
    return (bar_v(300, 245, 700, P['w']) + dot(300, 62, P['w'] * 1.42, P)
            + bar_h(352, 690, 1690, P['w']) + bar_h(198, 690, 1690, P['w']))

# ----------------------------------------------------------- dotted zero


def _g_zero_dotted(P):
    return (boxring(OL, 0, OR, 700, P['w'], P['cut'] * 1.18, P['segs'])
            + dot(CX, 350, P['w'] * 1.5, P))

# -------------------------------------------------------------- registry

_MARKS = {'grave': _m_grave, 'acute': _m_acute, 'circ': _m_circ,
          'tilde': _m_tilde, 'diaer': _m_diaer, 'ring': _m_ring,
          'cedilla': _m_cedilla, 'caron': _m_caron}

_COMPOSITES = [
    # (char, base, mark, dy)
    ('à', 'a', 'grave', 0), ('á', 'a', 'acute', 0), ('â', 'a', 'circ', 0),
    ('ã', 'a', 'tilde', 0), ('ä', 'a', 'diaer', 0), ('å', 'a', 'ring', 0),
    ('ç', 'c', 'cedilla', 0),
    ('è', 'e', 'grave', 0), ('é', 'e', 'acute', 0), ('ê', 'e', 'circ', 0),
    ('ë', 'e', 'diaer', 0),
    ('ì', 'idotless', 'grave', 0), ('í', 'idotless', 'acute', 0),
    ('î', 'idotless', 'circ', 0), ('ï', 'idotless', 'diaer', 0),
    ('ñ', 'n', 'tilde', 0),
    ('ò', 'o', 'grave', 0), ('ó', 'o', 'acute', 0), ('ô', 'o', 'circ', 0),
    ('õ', 'o', 'tilde', 0), ('ö', 'o', 'diaer', 0),
    ('ù', 'u', 'grave', 0), ('ú', 'u', 'acute', 0), ('û', 'u', 'circ', 0),
    ('ü', 'u', 'diaer', 0),
    ('ý', 'y', 'acute', 0), ('ÿ', 'y', 'diaer', 0),
    ('À', 'A', 'grave', CAPDY), ('Á', 'A', 'acute', CAPDY), ('Â', 'A', 'circ', CAPDY),
    ('Ã', 'A', 'tilde', CAPDY), ('Ä', 'A', 'diaer', CAPDY), ('Å', 'A', 'ring', CAPDY),
    ('Ç', 'C', 'cedilla', 0),
    ('È', 'E', 'grave', CAPDY), ('É', 'E', 'acute', CAPDY), ('Ê', 'E', 'circ', CAPDY),
    ('Ë', 'E', 'diaer', CAPDY),
    ('Ì', 'I', 'grave', CAPDY), ('Í', 'I', 'acute', CAPDY), ('Î', 'I', 'circ', CAPDY),
    ('Ï', 'I', 'diaer', CAPDY),
    ('Ñ', 'N', 'tilde', CAPDY),
    ('Ò', 'O', 'grave', CAPDY), ('Ó', 'O', 'acute', CAPDY), ('Ô', 'O', 'circ', CAPDY),
    ('Õ', 'O', 'tilde', CAPDY), ('Ö', 'O', 'diaer', CAPDY),
    ('Ù', 'U', 'grave', CAPDY), ('Ú', 'U', 'acute', CAPDY), ('Û', 'U', 'circ', CAPDY),
    ('Ü', 'U', 'diaer', CAPDY),
    ('Ý', 'Y', 'acute', CAPDY),
]

_SYMBOLS = {
    'ø': _g_oslash, 'Ø': _g_Oslash, 'ß': _g_germandbls,
    '©': _g_copyright, '®': _g_registered, '™': _g_trademark,
    '€': _g_euro, '£': _g_sterling, '¥': _g_yen, '¢': _g_cent, 'µ': _g_mu,
    '«': _g_guilleft, '»': _g_guilright, '·': _g_periodcentered,
    '§': _g_section, '¶': _g_paragraph, '†': _g_dagger, '‡': _g_daggerdbl,
    '✓': _g_check, '✗': _g_ballotx,
}

EXTRA_NAMES = {
    'ø': 'oslash', 'Ø': 'Oslash', 'ß': 'germandbls',
    '©': 'copyright', '®': 'registered', '™': 'trademark',
    '€': 'Euro', '£': 'sterling', '¥': 'yen', '¢': 'cent', 'µ': 'mu',
    '«': 'guillemotleft', '»': 'guillemotright', '·': 'periodcentered',
    '§': 'section', '¶': 'paragraph', '†': 'dagger', '‡': 'daggerdbl',
    '¿': 'questiondown', '¡': 'exclamdown',
}
_AGL_ACCENT = {
    'à': 'agrave', 'á': 'aacute', 'â': 'acircumflex', 'ã': 'atilde',
    'ä': 'adieresis', 'å': 'aring', 'ç': 'ccedilla', 'è': 'egrave',
    'é': 'eacute', 'ê': 'ecircumflex', 'ë': 'edieresis', 'ì': 'igrave',
    'í': 'iacute', 'î': 'icircumflex', 'ï': 'idieresis', 'ñ': 'ntilde',
    'ò': 'ograve', 'ó': 'oacute', 'ô': 'ocircumflex', 'õ': 'otilde',
    'ö': 'odieresis', 'ù': 'ugrave', 'ú': 'uacute', 'û': 'ucircumflex',
    'ü': 'udieresis', 'ý': 'yacute', 'ÿ': 'ydieresis',
    'À': 'Agrave', 'Á': 'Aacute', 'Â': 'Acircumflex', 'Ã': 'Atilde',
    'Ä': 'Adieresis', 'Å': 'Aring', 'Ç': 'Ccedilla', 'È': 'Egrave',
    'É': 'Eacute', 'Ê': 'Ecircumflex', 'Ë': 'Edieresis', 'Ì': 'Igrave',
    'Í': 'Iacute', 'Î': 'Icircumflex', 'Ï': 'Idieresis', 'Ñ': 'Ntilde',
    'Ò': 'Ograve', 'Ó': 'Oacute', 'Ô': 'Ocircumflex', 'Õ': 'Otilde',
    'Ö': 'Odieresis', 'Ù': 'Ugrave', 'Ú': 'Uacute', 'Û': 'Ucircumflex',
    'Ü': 'Udieresis', 'Ý': 'Yacute',
}
EXTRA_NAMES.update(_AGL_ACCENT)

# extra ligatures: (name, components, fn, advance) — longest sequences first
_EXTRA_LIGS = [
    ('notidentical.liga', ['exclam', 'equal', 'equal'], _l_notid, 1800),
    ('equalequalequal.liga', ['equal', 'equal', 'equal'], _l_eq3, 1800),
    ('colonequal.liga', ['colon', 'equal'], _l_colonequal, 1200),
    ('coloncolon.liga', ['colon', 'colon'], _l_coloncolon, 1200),
]


def register(GLYPHS, LIGATURES, ALTERNATES):
    GLYPHS['idotless'] = _g_idotless  # helper base for composites; not in cmap
    GLYPHS['ı'] = _g_idotless         # U+0131 dotless i (real, cmap'd)
    EXTRA_NAMES['ı'] = 'dotlessi'
    for ch, base, mark, dy in _COMPOSITES:
        GLYPHS[ch] = (lambda P, b=base, m=mark, d=dy:
                      GLYPHS[b](P) + _MARKS[m](P, d))
    GLYPHS.update(_SYMBOLS)
    GLYPHS['¿'] = _mk_invert('?')
    GLYPHS['¡'] = _mk_invert('!')
    # extra ligatures must precede the 2-glyph base ligatures already present
    LIGATURES[:0] = _EXTRA_LIGS
    ALTERNATES.append(('zero.dotted', _g_zero_dotted, 600))
