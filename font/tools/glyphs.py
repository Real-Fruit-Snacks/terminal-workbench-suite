"""Full glyph set for the font, built on the glyphlab engine.

Adds every remaining ASCII glyph, typographic extras and coding ligatures
to the seed set defined in glyphlab. All shapes are parametric in the
style dict P (w = stroke weight, cut = corner radius, segs = corner
smoothing), so Regular and Bold come from the same definitions.
"""

import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from glyphlab import (GLYPHS as _SEED, ADV, XL, XR, CX, OL, OR,
                      CAP_C, XH_C, ASC_C, BASE_C,
                      bar_h, bar_v, path, boxring, dot, stroke, cornerize)

GLYPHS = dict(_SEED)

# ----------------------------------------------------------- capitals


def _g_A(P):
    body = path([(95, BASE_C), (262, CAP_C), (338, CAP_C), (505, BASE_C)], P['w'] * 0.96)
    return body + bar_h(235, 150, 450, P['w'])


def _g_B(P):
    mid = 350
    c = P['cut'] * 0.72
    return (bar_v(XL, 0, 700, P['w'])
            + boxring(OL, 0, OR, mid + P['w'] / 2, P['w'], [0, c, c, 0], P['segs'])
            + boxring(OL, mid - P['w'] / 2, OR, 700, P['w'], [0, c, c, 0], P['segs']))


def _g_C(P):
    c = P['cut'] * 1.18
    pts = [(XR, 482), (XR, CAP_C), (XL, CAP_C), (XL, BASE_C), (XR, BASE_C), (XR, 218)]
    return path(pts, P['w'], cuts=[c, c, c, c], segs=P['segs'])


def _g_D(P):
    c = P['cut'] * 1.25
    return (bar_v(XL, 0, 700, P['w'])
            + boxring(OL, 0, OR, 700, P['w'], [0, c, c, 0], P['segs']))


def _g_E(P):
    return (bar_v(XL, 0, 700, P['w'])
            + bar_h(CAP_C, OL, 508, P['w'])
            + bar_h(355, OL, 462, P['w'])
            + bar_h(BASE_C, OL, 508, P['w']))


def _g_F(P):
    return (bar_v(XL, 0, 700, P['w'])
            + bar_h(CAP_C, OL, 508, P['w'])
            + bar_h(345, OL, 452, P['w']))


def _g_G(P):
    c = P['cut'] * 1.18
    pts = [(XR, 482), (XR, CAP_C), (XL, CAP_C), (XL, BASE_C), (XR, BASE_C), (XR, 330), (322, 330)]
    return path(pts, P['w'], cuts=[c, c, c, c, 48], segs=P['segs'])


def _g_H(P):
    return (bar_v(XL, 0, 700, P['w']) + bar_v(XR, 0, 700, P['w'])
            + bar_h(350, XL, XR, P['w']))


def _g_J(P):
    pts = [(XR, CAP_C + P['w'] / 2 - 1), (XR, BASE_C), (XL, BASE_C), (XL, 195)]
    return (path(pts, P['w'], cuts=[P['cut'] * 0.9, P['cut'] * 0.9], segs=P['segs'])
            + bar_h(CAP_C, 330, OR, P['w']))


def _g_K(P):
    return (bar_v(XL, 0, 700, P['w'])
            + path([(125, 340), (465, CAP_C)], P['w'] * 0.96)
            + path([(244, 452), (480, BASE_C)], P['w'] * 0.96))


def _g_L(P):
    return bar_v(XL, 0, 700, P['w']) + bar_h(BASE_C, OL, 508, P['w'])


def _g_M(P):
    return (bar_v(XL, 0, 700, P['w']) + bar_v(XR, 0, 700, P['w'])
            + path([(118, CAP_C), (300, 295), (482, CAP_C)], P['w'] * 0.88))


def _g_N(P):
    return (bar_v(XL, 0, 700, P['w']) + bar_v(XR, 0, 700, P['w'])
            + path([(120, 626), (480, 74)], P['w'] * 0.96))


def _g_P(P):
    c = P['cut'] * 0.8
    return (bar_v(XL, 0, 700, P['w'])
            + boxring(OL, 312, OR, 700, P['w'], [0, c, c, 0], P['segs']))


def _g_Q(P):
    return (boxring(OL, 0, OR, 700, P['w'], P['cut'] * 1.18, P['segs'])
            + path([(352, 218), (520, -78)], P['w'] * 0.98))


def _g_R(P):
    c = P['cut'] * 0.8
    return (bar_v(XL, 0, 700, P['w'])
            + boxring(OL, 312, OR, 700, P['w'], [0, c, c, 0], P['segs'])
            + path([(292, 334), (478, BASE_C)], P['w'] * 0.96))


def _g_S(P):
    pts = [(XR, 612), (XL, 612), (XL, 353), (XR, 353), (XR, 88), (XL, 88)]
    return path(pts, P['w'], cuts=P['cut'] * 0.75, segs=P['segs'])


def _g_T(P):
    return bar_h(CAP_C, OL, OR, P['w']) + bar_v(CX, 0, CAP_C + P['w'] / 2, P['w'])


def _g_U(P):
    c = P['cut'] * 0.95
    pts = [(XL, CAP_C + P['w'] / 2 - 1), (XL, BASE_C), (XR, BASE_C), (XR, CAP_C + P['w'] / 2 - 1)]
    return path(pts, P['w'], cuts=[c, c], segs=P['segs'])


def _g_V(P):
    return path([(102, CAP_C), (300, 52), (498, CAP_C)], P['w'] * 0.94, cuts=22)


def _g_X(P):
    return (path([(108, CAP_C), (492, BASE_C)], P['w'] * 0.94)
            + path([(492, CAP_C), (108, BASE_C)], P['w'] * 0.94))


def _g_Y(P):
    return (path([(108, CAP_C), (300, 338), (492, CAP_C)], P['w'] * 0.94, cuts=20)
            + bar_v(CX, 0, 372, P['w']))


def _g_Z(P):
    return path([(125, 612), (475, 612), (125, 88), (475, 88)], P['w'], cuts=42)

# ---------------------------------------------------------- lowercase


def _g_c(P):
    c = P['cut'] * 0.9
    pts = [(XR, 372), (XR, XH_C), (XL, XH_C), (XL, BASE_C), (XR, BASE_C), (XR, 168)]
    return path(pts, P['w'], cuts=[c, c, c, c], segs=P['segs'])


def _g_f(P):
    return (path([(265, 0), (265, 642), (455, 642)], P['w'], cuts=78, segs=P['segs'])
            + bar_h(XH_C, 95, 440, P['w']))


def _g_g(P):
    c = P['cut'] * 0.95
    return (boxring(OL, 0, OR, 540, P['w'], c, P['segs'])
            + path([(XR, 495), (XR, -167), (160, -167)], P['w'], cuts=62, segs=P['segs']))


def _g_j(P):
    return (path([(330, 497), (330, -167), (150, -167)], P['w'], cuts=60, segs=P['segs'])
            + bar_h(497, 235, 330, P['w'])
            + dot(330, 652, P['w'] * 1.3, P))


def _g_k(P):
    return (bar_v(XL, 0, ASC_C + P['w'] / 2, P['w'])
            + path([(125, 272), (452, 517)], P['w'] * 0.94)
            + path([(236, 355), (470, BASE_C)], P['w'] * 0.94))


def _g_m(P):
    c = P['cut'] * 0.45
    return (bar_v(105, 0, XH_C + P['w'] / 2, P['w'] * 0.92)
            + path([(105, XH_C), (300, XH_C), (300, 0)], P['w'] * 0.92, cuts=c, segs=P['segs'])
            + path([(300, XH_C), (495, XH_C), (495, 0)], P['w'] * 0.92, cuts=c, segs=P['segs']))


def _g_p(P):
    c = P['cut'] * 0.95
    return (bar_v(XL, -210, XH_C + P['w'] / 2, P['w'])
            + boxring(OL, 0, OR, 540, P['w'], [0, c, c, 0], P['segs']))


def _g_q(P):
    c = P['cut'] * 0.95
    return (bar_v(XR, -210, XH_C + P['w'] / 2, P['w'])
            + boxring(OL, 0, OR, 540, P['w'], [c, 0, 0, c], P['segs']))


def _g_v(P):
    return path([(112, 540), (300, 50), (488, 540)], P['w'] * 0.92, cuts=20)


def _g_y(P):
    return (path([(112, 540), (296, 60)], P['w'] * 0.92)
            + path([(488, 540), (300, 50), (300, -10)], P['w'] * 0.92, cuts=18)
            + path([(300, 60), (300, -167), (140, -167)], P['w'], cuts=58, segs=P['segs']))


def _g_z(P):
    return path([(125, 497), (475, 497), (125, 43), (475, 43)], P['w'], cuts=38)

# ------------------------------------------------------------- digits


def _g_two(P):
    c = P['cut'] * 0.85
    pts = [(XL, 548), (XL, CAP_C), (XR, CAP_C), (XR, 432), (XL, BASE_C), (XR, BASE_C)]
    return path(pts, P['w'], cuts=[c, c, 52, 40], segs=P['segs'])


def _g_three(P):
    c = P['cut'] * 0.72
    pts = [(120, 562), (120, 612), (480, 612), (480, 88), (120, 88), (120, 138)]
    return (path(pts, P['w'], cuts=[34, c, c, c, 34], segs=P['segs'])
            + bar_h(368, 268, 480, P['w']))


def _g_four(P):
    return (bar_v(390, 0, CAP_C + P['w'] / 2, P['w'])
            + path([(372, 648), (128, 218)], P['w'] * 0.94)
            + bar_h(180, OL, OR, P['w']))


def _g_five(P):
    c = P['cut'] * 0.82
    pts = [(XR, 612), (XL, 612), (XL, 388), (XR, 388), (XR, 88), (XL, 88)]
    return path(pts, P['w'], cuts=[26, 26, c, c], segs=P['segs'])


def _g_six(P):
    return (boxring(OL, 0, OR, 445, P['w'], P['cut'] * 0.95, P['segs'])
            + path([(113, 320), (113, CAP_C), (455, CAP_C)], P['w'], cuts=P['cut'] * 0.9,
                   segs=P['segs']))


def _g_eight(P):
    mid = 360
    return (boxring(OL, 0, OR, mid + P['w'] / 2, P['w'], P['cut'] * 0.95, P['segs'])
            + boxring(88, mid - P['w'] / 2, 512, 700, P['w'], P['cut'] * 0.85, P['segs']))


def _g_nine(P):
    return (boxring(OL, 255, OR, 700, P['w'], P['cut'] * 0.95, P['segs'])
            + path([(487, 380), (487, BASE_C), (165, BASE_C)], P['w'], cuts=P['cut'] * 0.9,
                   segs=P['segs']))

# -------------------------------------------------------- punctuation


def _g_quotedbl(P):
    return bar_v(225, 530, 700, P['w'] * 0.85) + bar_v(375, 530, 700, P['w'] * 0.85)


def _g_quotesingle(P):
    return bar_v(CX, 530, 700, P['w'] * 0.85)


def _g_numbersign(P):
    wl = P['w'] * 0.82
    return (bar_v(233, 80, 620, wl) + bar_v(367, 80, 620, wl)
            + bar_h(452, 85, 515, wl) + bar_h(248, 85, 515, wl))


def _g_percent(P):
    wl = P['w'] * 0.68
    return (boxring(75, 415, 295, 700, wl, P['cut'] * 0.5, P['segs'])
            + boxring(305, 0, 525, 285, wl, P['cut'] * 0.5, P['segs'])
            + path([(455, 645), (145, 55)], P['w'] * 0.78))


def _g_ampersand(P):
    # one continuous stroke: tail -> top loop -> long diagonal -> bottom bowl
    sk = [(486, 150), (250, 330), (250, 478), (332, 566), (412, 506),
          (412, 432), (165, 205), (206, 84), (352, 84), (486, 220)]
    return path(sk, P['w'] * 0.9, cuts=78, segs=P['segs'])


def _g_parenleft(P):
    pts = [(420, 712), (300, 552), (300, 8), (420, -152)]
    return path(pts, P['w'] * 0.9, cuts=148, segs=P['segs'])


def _g_parenright(P):
    pts = [(180, 712), (300, 552), (300, 8), (180, -152)]
    return path(pts, P['w'] * 0.9, cuts=148, segs=P['segs'])


def _g_asterisk(P):
    wl = P['w'] * 0.8
    return (bar_v(CX, 320, 640, wl)
            + path([(170, 405), (430, 555)], wl)
            + path([(170, 555), (430, 405)], wl))


def _g_plus(P):
    return bar_h(280, 115, 485, P['w']) + bar_v(CX, 95, 465, P['w'])


def _g_comma(P):
    return (dot(305, 62, P['w'] * 1.42, P)
            + path([(296, 12), (252, -98)], P['w'] * 0.78))


def _g_slash(P):
    return path([(425, 758), (175, -58)], P['w'] * 0.95)


def _g_semicolon(P):
    return (dot(CX, 400, P['w'] * 1.42, P) + dot(305, 62, P['w'] * 1.42, P)
            + path([(296, 12), (252, -98)], P['w'] * 0.78))


def _g_less(P):
    return path([(445, 462), (155, 266), (445, 70)], P['w'])


def _g_bracketleft(P):
    return (bar_v(245, -10, 715, P['w'])
            + bar_h(672, 245, 428, P['w']) + bar_h(33, 245, 428, P['w']))


def _g_backslash(P):
    return path([(175, 758), (425, -58)], P['w'] * 0.95)


def _g_bracketright(P):
    return (bar_v(355, -10, 715, P['w'])
            + bar_h(672, 172, 355, P['w']) + bar_h(33, 172, 355, P['w']))


def _g_asciicircum(P):
    return path([(165, 490), (300, 662), (435, 490)], P['w'] * 0.85, cuts=16)


def _g_underscore(P):
    return bar_h(-80, OL, OR, P['w'])


def _g_grave(P):
    return path([(252, 702), (348, 588)], P['w'] * 0.85)


def _g_bar(P):
    return bar_v(CX, -100, 760, P['w'] * 0.9)

# ------------------------------------------------------------- extras


def _g_endash(P):
    return bar_h(272, 90, 510, P['w'])


def _g_emdash(P):
    return bar_h(272, 20, 580, P['w'])


def _g_quoteleft(P):
    return dot(295, 582, P['w'] * 1.32, P) + path([(298, 628), (332, 700)], P['w'] * 0.78)


def _g_quoteright(P):
    return dot(305, 668, P['w'] * 1.32, P) + path([(302, 622), (268, 550)], P['w'] * 0.78)


def _g_quotedblleft(P):
    return (dot(223, 582, P['w'] * 1.32, P) + path([(226, 628), (260, 700)], P['w'] * 0.78)
            + dot(367, 582, P['w'] * 1.32, P) + path([(370, 628), (404, 700)], P['w'] * 0.78))


def _g_quotedblright(P):
    return (dot(233, 668, P['w'] * 1.32, P) + path([(230, 622), (196, 550)], P['w'] * 0.78)
            + dot(377, 668, P['w'] * 1.32, P) + path([(374, 622), (340, 550)], P['w'] * 0.78))


def _g_ellipsis(P):
    s = P['w'] * 1.3
    return dot(135, 62, s, P) + dot(300, 62, s, P) + dot(465, 62, s, P)


def _g_bullet(P):
    return dot(CX, 280, 205, P)


def _g_degree(P):
    return boxring(195, 472, 405, 682, P['w'] * 0.85, P['cut'] * 0.5, P['segs'])


def _g_multiply(P):
    return (path([(185, 395), (415, 165)], P['w'] * 0.95)
            + path([(415, 395), (185, 165)], P['w'] * 0.95))


def _g_divide(P):
    return (bar_h(280, 120, 480, P['w'])
            + dot(CX, 428, P['w'] * 1.2, P) + dot(CX, 132, P['w'] * 1.2, P))


def _g_notequal(P):
    return (bar_h(352, 110, 490, P['w']) + bar_h(198, 110, 490, P['w'])
            + path([(368, 478), (232, 72)], P['w'] * 0.85))


def _g_lessequal(P):
    return (path([(430, 502), (170, 330), (430, 158)], P['w'] * 0.95)
            + bar_h(48, 175, 430, P['w']))


def _g_greaterequal(P):
    return (path([(170, 502), (430, 330), (170, 158)], P['w'] * 0.95)
            + bar_h(48, 170, 425, P['w']))


def _g_plusminus(P):
    return (bar_v(CX, 195, 525, P['w']) + bar_h(360, 130, 470, P['w'])
            + bar_h(45, 130, 470, P['w']))


def _g_arrowright(P):
    return (bar_h(280, 80, 450, P['w'])
            + path([(330, 432), (488, 280), (330, 128)], P['w'] * 0.92))


def _g_arrowleft(P):
    return (bar_h(280, 150, 520, P['w'])
            + path([(270, 432), (112, 280), (270, 128)], P['w'] * 0.92))


def _g_arrowup(P):
    return (bar_v(CX, 80, 460, P['w'])
            + path([(152, 320), (300, 472), (448, 320)], P['w'] * 0.92))


def _g_arrowdown(P):
    return (bar_v(CX, 100, 480, P['w'])
            + path([(152, 240), (300, 88), (448, 240)], P['w'] * 0.92))


def _g_notdef(P):
    return (boxring(100, 0, 500, 700, 58, 0, 1)
            + path([(165, 630), (435, 70)], 48)
            + path([(435, 630), (165, 70)], 48))

# ----------------------------------------------------------- registry

GLYPHS.update({
    'A': _g_A, 'B': _g_B, 'C': _g_C, 'D': _g_D, 'E': _g_E, 'F': _g_F,
    'G': _g_G, 'H': _g_H, 'J': _g_J, 'K': _g_K, 'L': _g_L, 'M': _g_M,
    'N': _g_N, 'P': _g_P, 'Q': _g_Q, 'R': _g_R, 'S': _g_S, 'T': _g_T,
    'U': _g_U, 'V': _g_V, 'X': _g_X, 'Y': _g_Y, 'Z': _g_Z,
    'c': _g_c, 'f': _g_f, 'g': _g_g, 'j': _g_j, 'k': _g_k, 'm': _g_m,
    'p': _g_p, 'q': _g_q, 'v': _g_v, 'y': _g_y, 'z': _g_z,
    '2': _g_two, '3': _g_three, '4': _g_four, '5': _g_five, '6': _g_six,
    '8': _g_eight, '9': _g_nine,
    '"': _g_quotedbl, "'": _g_quotesingle, '#': _g_numbersign,
    '%': _g_percent, '&': _g_ampersand, '(': _g_parenleft, ')': _g_parenright,
    '*': _g_asterisk, '+': _g_plus, ',': _g_comma, '/': _g_slash,
    ';': _g_semicolon, '<': _g_less, '[': _g_bracketleft, '\\': _g_backslash,
    ']': _g_bracketright, '^': _g_asciicircum, '_': _g_underscore,
    '`': _g_grave, '|': _g_bar,
    '–': _g_endash, '—': _g_emdash,
    '‘': _g_quoteleft, '’': _g_quoteright,
    '“': _g_quotedblleft, '”': _g_quotedblright,
    '…': _g_ellipsis, '•': _g_bullet, '°': _g_degree,
    '×': _g_multiply, '÷': _g_divide, '≠': _g_notequal,
    '≤': _g_lessequal, '≥': _g_greaterequal, '±': _g_plusminus,
    '←': _g_arrowleft, '↑': _g_arrowup,
    '→': _g_arrowright, '↓': _g_arrowdown,
})

NOTDEF = _g_notdef

# --------------------------------------------------------- ligatures
# Each: (glyph_name, component glyph names, draw fn, advance)


def _lig_arrow_right(P):
    return (bar_h(280, 120, 900, P['w'])
            + path([(790, 470), (995, 280), (790, 90)], P['w'] * 0.95))


def _lig_arrow_left(P):
    return (bar_h(280, 300, 1080, P['w'])
            + path([(410, 470), (205, 280), (410, 90)], P['w'] * 0.95))


def _lig_darrow(P):
    return (bar_h(362, 130, 800, P['w']) + bar_h(198, 130, 840, P['w'])
            + path([(815, 500), (1055, 280), (815, 60)], P['w'] * 0.95))


def _lig_neq(P):
    return (bar_h(352, 250, 950, P['w']) + bar_h(198, 250, 950, P['w'])
            + path([(690, 488), (510, 62)], P['w'] * 0.88))


def _lig_eqeq(P):
    return bar_h(352, 170, 1030, P['w']) + bar_h(198, 170, 1030, P['w'])


def _lig_leq(P):
    return (path([(700, 520), (335, 318), (700, 116)], P['w'])
            + bar_h(30, 340, 700, P['w']))


def _lig_geq(P):
    return (path([(500, 520), (865, 318), (500, 116)], P['w'])
            + bar_h(30, 500, 860, P['w']))


LIGATURES = [
    ('arrowright.liga', ['hyphen', 'greater'], _lig_arrow_right, 1200),
    ('arrowleft.liga', ['less', 'hyphen'], _lig_arrow_left, 1200),
    ('darrowright.liga', ['equal', 'greater'], _lig_darrow, 1200),
    ('notequal.liga', ['exclam', 'equal'], _lig_neq, 1200),
    ('equalequal.liga', ['equal', 'equal'], _lig_eqeq, 1200),
    ('lessequal.liga', ['less', 'equal'], _lig_leq, 1200),
    ('greaterequal.liga', ['greater', 'equal'], _lig_geq, 1200),
]

ALTERNATES = []  # (glyph_name, draw_fn, advance) — reached via GSUB, not cmap

# ---- extended coverage: terminal pack, accents, symbols, extra ligatures
from box_glyphs import BOX_GLYPHS          # noqa: E402
GLYPHS.update(BOX_GLYPHS)

import glyphs_more                          # noqa: E402
glyphs_more.register(GLYPHS, LIGATURES, ALTERNATES)
EXTRA_NAMES = glyphs_more.EXTRA_NAMES
