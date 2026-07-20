"""glyphlab — parametric glyph geometry engine.

Glyphs are defined as skeletons (centerline stroke paths, box-rings, dots)
on a 1000-UPM grid, y-up, baseline at 0. A style dict controls stroke
weight, corner-cut size and corner smoothing, so the same skeletons can
render as sharp/angular, square/retro, or smooth/clean letterforms.

Grid conventions (all values are CENTERLINE coordinates; outlines extend
half a stroke-weight beyond them):
  advance      600 (monospace)
  glyph box    x in [70+w/2 .. 530-w/2] -> outer edges 70..530
  caps/digits  outer top 700
  x-height     outer top 540
  ascenders    outer top 730
  descenders   outer bottom -210
"""

import math

# ---------------------------------------------------------------- vectors

def _sub(a, b): return (a[0] - b[0], a[1] - b[1])
def _add(a, b): return (a[0] + b[0], a[1] + b[1])
def _mul(a, k): return (a[0] * k, a[1] * k)

def _norm(a):
    l = math.hypot(a[0], a[1])
    return (a[0] / l, a[1] / l)

def _perp(a): return (-a[1], a[0])

def _isect(p1, d1, p2, d2):
    den = d1[0] * d2[1] - d1[1] * d2[0]
    if abs(den) < 1e-9:
        return None
    t = ((p2[0] - p1[0]) * d2[1] - (p2[1] - p1[1]) * d2[0]) / den
    return _add(p1, _mul(d1, t))

# ---------------------------------------------------------------- strokes

MITER_LIMIT = 2.05  # in multiples of |dist|; sharper joins fall back to bevel


def _offset_open(pts, dist):
    """Offset an open polyline to its left by dist, mitered with bevel fallback."""
    n = len(pts)
    dirs = [_norm(_sub(pts[i + 1], pts[i])) for i in range(n - 1)]
    out = [_add(pts[0], _mul(_perp(dirs[0]), dist))]
    for i in range(1, n - 1):
        a = _add(pts[i], _mul(_perp(dirs[i - 1]), dist))
        b = _add(pts[i], _mul(_perp(dirs[i]), dist))
        p = _isect(a, dirs[i - 1], b, dirs[i])
        if p is None:
            out.append(b)
        elif math.hypot(*_sub(p, pts[i])) > abs(dist) * MITER_LIMIT:
            out.extend([a, b])  # bevel: avoid miter spikes on acute joints
        else:
            out.append(p)
    out.append(_add(pts[-1], _mul(_perp(dirs[-1]), dist)))
    return out


def stroke(pts, w):
    """Expand an open centerline polyline into a filled polygon of width w."""
    left = _offset_open(pts, w / 2.0)
    right = _offset_open(pts, -w / 2.0)
    return left + right[::-1]

# ------------------------------------------------------------- corners

def cornerize(pts, cuts, segs=1, closed=False):
    """Replace corners with 45-degree cuts (segs=1) or sampled fillets (segs>1).

    cuts: scalar, or per-corner list. For closed polygons the list matches
    point order; for open paths it matches interior points (len(pts)-2).
    """
    n = len(pts)
    if isinstance(cuts, (int, float)):
        cuts = [cuts] * (n if closed else n - 2)
    out = []
    idxs = range(n) if closed else range(1, n - 1)
    if not closed:
        out.append(pts[0])
    for k, i in enumerate(idxs):
        p = pts[i]
        a = pts[(i - 1) % n]
        b = pts[(i + 1) % n]
        cut = cuts[k]
        if cut <= 0.5:
            out.append(p)
            continue
        da = _norm(_sub(p, a))
        db = _norm(_sub(b, p))
        la = math.hypot(*_sub(p, a))
        lb = math.hypot(*_sub(b, p))
        c = min(cut, la * 0.46, lb * 0.46)
        A = _sub(p, _mul(da, c))
        B = _add(p, _mul(db, c))
        out.append(A)
        if segs > 1:  # quadratic fillet sampled through the corner
            for s in range(1, segs):
                t = s / float(segs)
                q = _add(_add(_mul(A, (1 - t) ** 2), _mul(p, 2 * (1 - t) * t)),
                         _mul(B, t * t))
                out.append(q)
        out.append(B)
    if not closed:
        out.append(pts[-1])
    return out

# ---------------------------------------------------------------- shapes
# A glyph is a list of shapes: ('fill', pts) or ('hole', pts), drawn in order.

def bar_h(y, x0, x1, w):
    return [('fill', [(x0, y - w / 2), (x1, y - w / 2), (x1, y + w / 2), (x0, y + w / 2)])]


def bar_v(x, y0, y1, w):
    return [('fill', [(x - w / 2, y0), (x + w / 2, y0), (x + w / 2, y1), (x - w / 2, y1)])]


def path(pts, w, cuts=0, segs=1):
    sk = cornerize(pts, cuts, segs) if cuts else list(pts)
    return [('fill', stroke(sk, w))]


def boxring(x0, y0, x1, y1, w, cuts, segs=1):
    """Closed rectangular ring with per-corner outer cuts (BL,BR,TR,TL).

    x0..x1 / y0..y1 are OUTER edges.
    """
    if isinstance(cuts, (int, float)):
        cuts = [cuts] * 4
    outer_raw = [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]
    outer = cornerize(outer_raw, cuts, segs, closed=True)
    if segs > 1:
        icuts = [max(c - w, 6) if c > 0.5 else 0 for c in cuts]
    else:
        icuts = [max(c - 0.586 * w, 0) if c > 0.5 else 0 for c in cuts]
    inner_raw = [(x0 + w, y0 + w), (x1 - w, y0 + w), (x1 - w, y1 - w), (x0 + w, y1 - w)]
    inner = cornerize(inner_raw, icuts, segs, closed=True)
    return [('fill', outer), ('hole', inner)]


def dot(x, y, size, P):
    """Square-ish tittle/punctuation dot centered at (x, y)."""
    h = size / 2.0
    raw = [(x - h, y - h), (x + h, y - h), (x + h, y + h), (x - h, y + h)]
    if P['segs'] > 1:
        pts = cornerize(raw, size * 0.5, P['segs'], closed=True)
    elif P['cut'] > 0.5:
        pts = cornerize(raw, size * 0.24, 1, closed=True)
    else:
        pts = raw
    return [('fill', pts)]

# ---------------------------------------------------------------- glyphs
# Style dict P: w (stroke), cut (base corner cut), segs (1=angular, >1=smooth)

ADV = 600
XL, XR, CX = 115, 485, 300      # centerline left/right/center
OL, OR = 70, 530                # outer left/right
CAP_C, XH_C, ASC_C = 655, 495, 685   # centerline of cap top / x-height / ascender
BASE_C = 45                     # centerline of a stroke sitting on the baseline


def _g_space(P): return []


def _g_W(P):
    sk = cornerize([(100, CAP_C), (190, BASE_C), (300, 430), (410, BASE_C), (500, CAP_C)], 22)
    return [('fill', stroke(sk, P['w'] * 0.94))]


def _g_O(P):
    return boxring(OL, 0, OR, 700, P['w'], P['cut'] * 1.18, P['segs'])


def _g_I(P):
    return (bar_v(CX, BASE_C, CAP_C, P['w'])
            + bar_h(CAP_C, 165, 435, P['w'])
            + bar_h(BASE_C, 165, 435, P['w']))


def _g_zero(P):
    shapes = boxring(OL, 0, OR, 700, P['w'], P['cut'] * 1.18, P['segs'])
    shapes += path([(232, 196), (368, 504)], P['w'] * 0.72)
    return shapes


def _g_one(P):
    return (bar_v(CX, BASE_C, CAP_C, P['w'])
            + path([(300, 645), (182, 540)], P['w'])
            + bar_h(BASE_C, 150, 450, P['w']))


def _g_seven(P):
    return path([(XL, 610), (XR, 610), (255, BASE_C - 45)], P['w'], cuts=70)


def _g_e(P):
    loop = cornerize([(XR, 275), (XR, XH_C), (XL, XH_C), (XL, BASE_C), (XR, BASE_C)],
                     [P['cut'] * 0.9] * 3, P['segs'])
    return [('fill', stroke(loop, P['w']))] + bar_h(275, OL, OR, P['w'])


def _g_s(P):
    sk = cornerize([(XR, XH_C), (XL, XH_C), (XL, 277), (XR, 277), (XR, BASE_C), (XL, BASE_C)],
                   P['cut'] * 0.6, P['segs'])
    return [('fill', stroke(sk, P['w']))]


def _g_t(P):
    return (path([(255, ASC_C), (255, BASE_C), (470, BASE_C)], P['w'], cuts=58, segs=P['segs'])
            + bar_h(XH_C, 85, 430, P['w']))


def _g_dollar(P):
    sk = cornerize([(XR, 612), (XL, 612), (XL, 356), (XR, 356), (XR, 100), (XL, 100)],
                   P['cut'] * 0.55, P['segs'])
    return [('fill', stroke(sk, P['w']))] + bar_v(CX, -45, 757, P['w'] * 0.82)


def _g_h(P):
    return (bar_v(XL, 0, ASC_C + P['w'] / 2, P['w'])
            + path([(XL, XH_C), (XR, XH_C), (XR, 0)], P['w'], cuts=P['cut'] * 0.62, segs=P['segs']))


def _g_n(P):
    return (bar_v(XL, 0, XH_C + P['w'] / 2, P['w'])
            + path([(XL, XH_C), (XR, XH_C), (XR, 0)], P['w'], cuts=P['cut'] * 0.62, segs=P['segs']))


def _g_r(P):
    return (bar_v(140, 0, XH_C + P['w'] / 2, P['w'])
            + path([(140, XH_C), (415, XH_C), (468, 442)], P['w']))


def _g_o(P):
    return boxring(OL, 0, OR, 540, P['w'], P['cut'] * 0.95, P['segs'])


def _g_b(P):
    return (bar_v(XL, 0, ASC_C + P['w'] / 2, P['w'])
            + boxring(OL, 0, OR, 540, P['w'], [0, P['cut'] * 0.95, P['cut'] * 0.95, 0], P['segs']))


def _g_d(P):
    return (bar_v(XR, 0, ASC_C + P['w'] / 2, P['w'])
            + boxring(OL, 0, OR, 540, P['w'], [P['cut'] * 0.95, 0, 0, P['cut'] * 0.95], P['segs']))


def _g_a(P):
    c = P['cut'] * 0.55
    top = cornerize([(XL, 420), (XL, XH_C), (XR, XH_C), (XR, 0)], [c, c], P['segs'])
    bowl = cornerize([(XR, 262), (XL, 262), (XL, BASE_C), (XR, BASE_C)], [c, c], P['segs'])
    return [('fill', stroke(top, P['w'])), ('fill', stroke(bowl, P['w']))]


def _g_i(P):
    return (bar_v(CX, 0, XH_C + P['w'] / 2, P['w'])
            + bar_h(XH_C, 205, 300, P['w'])
            + bar_h(BASE_C, 160, 440, P['w'])
            + dot(CX, 652, P['w'] * 1.3, P))


def _g_l(P):
    return path([(280, ASC_C), (280, BASE_C), (462, BASE_C)], P['w'], cuts=52, segs=P['segs'])


def _g_x(P):
    return (path([(122, XH_C), (478, BASE_C)], P['w'])
            + path([(478, XH_C), (122, BASE_C)], P['w']))


def _g_u(P):
    return (path([(XL, 540), (XL, BASE_C), (XR, BASE_C)], P['w'],
                 cuts=P['cut'] * 0.62, segs=P['segs'])
            + bar_v(XR, 0, 540, P['w']))


def _g_w(P):
    sk = cornerize([(105, 540), (175, BASE_C), (300, 400), (425, BASE_C), (495, 540)], 20)
    return [('fill', stroke(sk, P['w'] * 0.9))]


def _g_at(P):
    wa = P['w'] * 0.68
    shapes = boxring(OL, -25, OR, 625, wa, P['cut'], P['segs'])
    spiral = cornerize([(345, 430), (195, 430), (195, 165), (345, 165)],
                       [P['cut'] * 0.35, P['cut'] * 0.35], P['segs'])
    shapes += [('fill', stroke(spiral, wa))]
    shapes += bar_v(385, 32, 438, wa)
    return shapes


def _g_period(P):
    return dot(CX, 62, P['w'] * 1.42, P)


def _g_colon(P):
    return dot(CX, 62, P['w'] * 1.42, P) + dot(CX, 400, P['w'] * 1.42, P)


def _g_hyphen(P):
    return bar_h(272, 135, 465, P['w'])


def _g_gt(P):
    return path([(155, 462), (445, 266), (155, 70)], P['w'])


def _g_braceleft(P):
    sk = [(432, 700), (345, 700), (300, 652), (300, 415), (252, 350), (300, 285),
          (300, 48), (345, 0), (432, 0)]
    return [('fill', stroke(sk, P['w'] * 0.9))]


def _g_braceright(P):
    sk = [(168, 700), (255, 700), (300, 652), (300, 415), (348, 350), (300, 285),
          (300, 48), (255, 0), (168, 0)]
    return [('fill', stroke(sk, P['w'] * 0.9))]


def _g_tilde(P):
    pts = [(110, 255), (218, 330), (382, 228), (490, 303)]
    if P['segs'] > 1:
        pts = cornerize(pts, 72, P['segs'])
    return path(pts, P['w'] * 0.95)


def _g_equal(P):
    return bar_h(352, 110, 490, P['w']) + bar_h(198, 110, 490, P['w'])


def _g_exclam(P):
    return bar_v(CX, 245, 700, P['w']) + dot(CX, 62, P['w'] * 1.42, P)


def _g_question(P):
    sk = cornerize([(XL, 555), (XL, CAP_C), (XR, CAP_C), (XR, 415), (300, 415), (300, 240)],
                   [55, P['cut'] * 0.7, P['cut'] * 0.7, 55], P['segs'])
    return [('fill', stroke(sk, P['w']))] + dot(CX, 62, P['w'] * 1.42, P)


GLYPHS = {
    ' ': _g_space, 'W': _g_W, 'O': _g_O, 'I': _g_I,
    '0': _g_zero, '1': _g_one, '7': _g_seven,
    'a': _g_a, 'b': _g_b, 'd': _g_d, 'e': _g_e, 'h': _g_h, 'i': _g_i,
    'l': _g_l, 'n': _g_n, 'o': _g_o, 'r': _g_r, 's': _g_s, 't': _g_t,
    'u': _g_u, 'w': _g_w, 'x': _g_x,
    '@': _g_at, '$': _g_dollar, '.': _g_period, ':': _g_colon,
    '-': _g_hyphen, '>': _g_gt, '{': _g_braceleft, '}': _g_braceright,
    '~': _g_tilde, '=': _g_equal, '!': _g_exclam, '?': _g_question,
}

STYLES = {
    'angular': dict(w=90,  cut=115, segs=1),
    'retro':   dict(w=120, cut=0,   segs=1),
    'clean':   dict(w=86,  cut=165, segs=6),
}
