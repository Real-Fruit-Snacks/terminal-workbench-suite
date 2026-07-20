"""Terminal pack: box-drawing, block elements, shades, Powerline.

Every glyph fills a full terminal cell — width [0, 600], height
[DBOT, DTOP] = [-260, 960] (the font's descent..ascent) — so lines and
fills tile seamlessly across adjacent cells. Thicknesses scale with the
style weight so the pack looks right in Bold as well as Regular.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from glyphlab import stroke, cornerize

XC = 300                 # cell horizontal center
DTOP, DBOT = 960, -260   # cell top / bottom (== ascent / descent)
YC = (DTOP + DBOT) // 2  # cell vertical center = 350
DD = 100                 # double-line rail offset from axis

# ----------------------------------------------------------- helpers


def _rect(x0, y0, x1, y1):
    return ('fill', [(x0, y0), (x1, y0), (x1, y1), (x0, y1)])


def _strokes(paths, t, r=0, segs=1):
    out = []
    for p in paths:
        pts = cornerize(p, r, segs) if r else p
        out.append(('fill', stroke(pts, t)))
    return out


def _line(paths, kind):
    """Factory: a line glyph whose thickness derives from the weight."""
    def fn(P, paths=paths, kind=kind):
        w = P['w']
        if kind == 'heavy':
            return _strokes(paths, w * 1.72)
        if kind == 'round':
            return _strokes(paths, w * 0.86, r=170, segs=P['segs'])
        if kind == 'double':
            return _strokes(paths, w * 0.72)
        return _strokes(paths, w * 0.86)
    return fn


# ----------------------------------------------------- box-drawing
# paths are centerlines; junctions overlap and are unioned by removeOverlaps

H = [(0, YC), (600, YC)]
V = [(XC, DBOT), (XC, DTOP)]
_L = lambda *pts: list(pts)

SINGLE = {
    '─': [H], '│': [V],
    '┌': [_L((600, YC), (XC, YC), (XC, DBOT))],
    '┐': [_L((0, YC), (XC, YC), (XC, DBOT))],
    '└': [_L((600, YC), (XC, YC), (XC, DTOP))],
    '┘': [_L((0, YC), (XC, YC), (XC, DTOP))],
    '├': [V, [(XC, YC), (600, YC)]],
    '┤': [V, [(XC, YC), (0, YC)]],
    '┬': [H, [(XC, YC), (XC, DBOT)]],
    '┴': [H, [(XC, YC), (XC, DTOP)]],
    '┼': [H, V],
}
HEAVY = {
    '━': [H], '┃': [V],
    '┏': [_L((600, YC), (XC, YC), (XC, DBOT))],
    '┓': [_L((0, YC), (XC, YC), (XC, DBOT))],
    '┗': [_L((600, YC), (XC, YC), (XC, DTOP))],
    '┛': [_L((0, YC), (XC, YC), (XC, DTOP))],
    '┣': [V, [(XC, YC), (600, YC)]],
    '┫': [V, [(XC, YC), (0, YC)]],
    '┳': [H, [(XC, YC), (XC, DBOT)]],
    '┻': [H, [(XC, YC), (XC, DTOP)]],
    '╋': [H, V],
}
ROUND = {
    '╭': [_L((600, YC), (XC, YC), (XC, DBOT))],
    '╮': [_L((0, YC), (XC, YC), (XC, DBOT))],
    '╯': [_L((0, YC), (XC, YC), (XC, DTOP))],
    '╰': [_L((600, YC), (XC, YC), (XC, DTOP))],
}
DOUBLE = {
    '═': [[(0, YC + DD), (600, YC + DD)], [(0, YC - DD), (600, YC - DD)]],
    '║': [[(XC - DD, DBOT), (XC - DD, DTOP)], [(XC + DD, DBOT), (XC + DD, DTOP)]],
    '╔': [[(600, YC + DD), (XC - DD, YC + DD), (XC - DD, DBOT)],
               [(600, YC - DD), (XC + DD, YC - DD), (XC + DD, DBOT)]],
    '╗': [[(0, YC + DD), (XC + DD, YC + DD), (XC + DD, DBOT)],
               [(0, YC - DD), (XC - DD, YC - DD), (XC - DD, DBOT)]],
    '╚': [[(600, YC - DD), (XC - DD, YC - DD), (XC - DD, DTOP)],
               [(600, YC + DD), (XC + DD, YC + DD), (XC + DD, DTOP)]],
    '╝': [[(0, YC - DD), (XC + DD, YC - DD), (XC + DD, DTOP)],
               [(0, YC + DD), (XC - DD, YC + DD), (XC - DD, DTOP)]],
    '╠': [[(XC - DD, DBOT), (XC - DD, DTOP)],
               [(XC + DD, DTOP), (XC + DD, YC + DD), (600, YC + DD)],
               [(XC + DD, DBOT), (XC + DD, YC - DD), (600, YC - DD)]],
    '╣': [[(XC + DD, DBOT), (XC + DD, DTOP)],
               [(XC - DD, DTOP), (XC - DD, YC + DD), (0, YC + DD)],
               [(XC - DD, DBOT), (XC - DD, YC - DD), (0, YC - DD)]],
    '╦': [[(0, YC + DD), (600, YC + DD)],
               [(0, YC - DD), (XC - DD, YC - DD), (XC - DD, DBOT)],
               [(600, YC - DD), (XC + DD, YC - DD), (XC + DD, DBOT)]],
    '╩': [[(0, YC - DD), (600, YC - DD)],
               [(0, YC + DD), (XC - DD, YC + DD), (XC - DD, DTOP)],
               [(600, YC + DD), (XC + DD, YC + DD), (XC + DD, DTOP)]],
    '╬': [[(600, YC + DD), (XC + DD, YC + DD), (XC + DD, DTOP)],
               [(0, YC + DD), (XC - DD, YC + DD), (XC - DD, DTOP)],
               [(600, YC - DD), (XC + DD, YC - DD), (XC + DD, DBOT)],
               [(0, YC - DD), (XC - DD, YC - DD), (XC - DD, DBOT)]],
}

# ----------------------------------------------------- block elements


def _full(P):  return [_rect(0, DBOT, 600, DTOP)]
def _uphalf(P): return [_rect(0, YC, 600, DTOP)]
def _lowhalf(P): return [_rect(0, DBOT, 600, YC)]
def _lefthalf(P): return [_rect(0, DBOT, XC, DTOP)]
def _righthalf(P): return [_rect(XC, DBOT, 600, DTOP)]

_H = DTOP - DBOT  # cell height
_W = 600


def _lower_eighth(n):
    return lambda P, n=n: [_rect(0, DBOT, 600, DBOT + _H * n / 8.0)]


def _left_eighth(n):
    return lambda P, n=n: [_rect(0, DBOT, _W * n / 8.0, DTOP)]


def _upper_eighth(P): return [_rect(0, DTOP - _H / 8.0, 600, DTOP)]
def _right_eighth(P): return [_rect(600 - _W / 8.0, DBOT, 600, DTOP)]


def _shade(frac):
    """Stipple grid approximating a fill fraction (light/medium/dark)."""
    cols, rows = 6, 12
    gx, gy = _W / cols, _H / rows
    side = (frac ** 0.5) * min(gx, gy)
    def fn(P, side=side, gx=gx, gy=gy, cols=cols, rows=rows):
        out = []
        for r in range(rows):
            cy = DBOT + (r + 0.5) * gy
            for c in range(cols):
                cx = (c + 0.5) * gx
                out.append(_rect(cx - side / 2, cy - side / 2,
                                 cx + side / 2, cy + side / 2))
        return out
    return fn


_QUAD = {
    '▘': ['NW'], '▝': ['NE'], '▖': ['SW'], '▗': ['SE'],
    '▚': ['NW', 'SE'], '▞': ['NE', 'SW'],
    '▙': ['NW', 'SW', 'SE'], '▛': ['NW', 'NE', 'SW'],
    '▜': ['NW', 'NE', 'SE'], '▟': ['NE', 'SW', 'SE'],
}
_QBOX = {'NW': (0, YC, XC, DTOP), 'NE': (XC, YC, 600, DTOP),
         'SW': (0, DBOT, XC, YC), 'SE': (XC, DBOT, 600, YC)}


def _quad(parts):
    return lambda P, parts=parts: [_rect(*_QBOX[q]) for q in parts]


# ----------------------------------------------------- Powerline (PUA)


def _pl_rtri(P): return [('fill', [(0, DBOT), (600, YC), (0, DTOP)])]
def _pl_ltri(P): return [('fill', [(600, DBOT), (0, YC), (600, DTOP)])]
def _pl_rthin(P): return _strokes([[(0, DTOP), (600, YC), (0, DBOT)]], P['w'] * 1.15)
def _pl_lthin(P): return _strokes([[(600, DTOP), (0, YC), (600, DBOT)]], P['w'] * 1.15)


# ----------------------------------------------------------- registry

BOX_GLYPHS = {}
for _ch, _p in SINGLE.items():
    BOX_GLYPHS[_ch] = _line(_p, 'light')
for _ch, _p in HEAVY.items():
    BOX_GLYPHS[_ch] = _line(_p, 'heavy')
for _ch, _p in ROUND.items():
    BOX_GLYPHS[_ch] = _line(_p, 'round')
for _ch, _p in DOUBLE.items():
    BOX_GLYPHS[_ch] = _line(_p, 'double')

BOX_GLYPHS.update({
    '█': _full, '▀': _uphalf, '▄': _lowhalf,
    '▌': _lefthalf, '▐': _righthalf,
    '▔': _upper_eighth, '▕': _right_eighth,
    '▁': _lower_eighth(1), '▂': _lower_eighth(2),
    '▃': _lower_eighth(3), '▅': _lower_eighth(5),
    '▆': _lower_eighth(6), '▇': _lower_eighth(7),
    '▏': _left_eighth(1), '▎': _left_eighth(2),
    '▍': _left_eighth(3), '▋': _left_eighth(5),
    '▊': _left_eighth(6), '▉': _left_eighth(7),
    '░': _shade(0.25), '▒': _shade(0.5), '▓': _shade(0.75),
    '': _pl_rtri, '': _pl_rthin,
    '': _pl_ltri, '': _pl_lthin,
})
for _ch, _q in _QUAD.items():
    if _q is not None:
        BOX_GLYPHS[_ch] = _quad(_q)
