"""ks4_art.bonding — dot-and-cross molecule diagrams.

Covers H2, CH4, CO2, NH3, H2O (covalent), MgO (ionic, with charges), and a
polyester/polymer repeat unit.

CONVENTION, fixed across every drawer here so a reader never has to guess
which mark belongs to which atom: the CENTRAL (or, for H2, the LEFT) atom's
own outer electrons are drawn as DOTS; every OTHER atom's own electrons are
drawn as CROSSES. A SHARED (bonding) pair is one dot next to one cross,
drawn together in the overlap between the two atoms' shells. A LONE pair
belongs to one atom only, so it is drawn as two dots (or two crosses) side
by side — never one of each, which is the bonding pair's own signature and
would misstate whose electrons they are.
"""

import math

from ks3_art.kit import (
    e, _n, _svg_open, _circle, _line, _path, _label, _SVG_INK, _SVG_INK_MUTED,
)


def _shell(cx, cy, r):
    return _circle(cx, cy, r, stroke=_SVG_INK_MUTED, w=1.5, dash="3,2")


def _dot(x, y, r=2.6):
    return _circle(x, y, r, fill=_SVG_INK)


def _cross(x, y, size=3.4):
    return (_line(x - size, y - size, x + size, y + size, stroke=_SVG_INK, w=1.8)
            + _line(x - size, y + size, x + size, y - size, stroke=_SVG_INK, w=1.8))


def _mark(kind, x, y):
    return _dot(x, y) if kind == "dot" else _cross(x, y)


def _bond_pairs(mx, my, n, perp_dx, perp_dy, gap=8.0):
    """`n` SHARED electron pairs (each one dot + one cross) centred on
    `(mx, my)`, stacked along the perpendicular unit vector `(perp_dx,
    perp_dy)` — a double bond's two pairs sit side by side, never one on
    top of the other."""
    out = []
    start = -(n - 1) / 2.0
    for i in range(n):
        off = (start + i) * gap
        px, py = mx + perp_dx * off, my + perp_dy * off
        out.append(_dot(px - 3.4, py))
        out.append(_cross(px + 3.4, py))
    return "".join(out)


def _lone_pair(x, y, kind, axis="h", gap=6.6):
    """Two electrons belonging to ONE atom — both `kind` ('dot' or
    'cross'), side by side along `axis`."""
    dx, dy = (gap / 2.0, 0) if axis == "h" else (0, gap / 2.0)
    return _mark(kind, x - dx, y - dy) + _mark(kind, x + dx, y + dy)


def _bracket(cx, cy, half_w, h_half, tick=7):
    lx, rx = cx - half_w, cx + half_w
    left = _path("M %s,%s L %s,%s L %s,%s L %s,%s"
                  % (_n(lx + tick), _n(cy - h_half), _n(lx), _n(cy - h_half),
                     _n(lx), _n(cy + h_half), _n(lx + tick), _n(cy + h_half)),
                  stroke=_SVG_INK, w=2.2)
    right = _path("M %s,%s L %s,%s L %s,%s L %s,%s"
                   % (_n(rx - tick), _n(cy - h_half), _n(rx), _n(cy - h_half),
                      _n(rx), _n(cy + h_half), _n(rx - tick), _n(cy + h_half)),
                   stroke=_SVG_INK, w=2.2)
    return left + right


def draw_h2(fig):
    w, h = fig.get("w", 220), fig.get("h", 140)
    cy = h / 2.0
    cx1, cx2 = w / 2.0 - 24, w / 2.0 + 24
    r = 26
    out = [_shell(cx1, cy, r), _shell(cx2, cy, r),
           _label(cx1 - r - 12, cy + 5, "H", size=16, weight="700"),
           _label(cx2 + r + 12, cy + 5, "H", size=16, weight="700"),
           _bond_pairs((cx1 + cx2) / 2.0, cy, 1, 0, 1)]
    return _svg_open(fig, w, h) + "".join(out) + "</svg>"


def draw_ch4(fig):
    w, h = fig.get("w", 260), fig.get("h", 260)
    cx, cy = w / 2.0, h / 2.0
    rc, rh, dist = 30, 20, 52
    out = [_shell(cx, cy, rc), _label(cx, cy + 5, "C", size=16, weight="700")]
    for dx, dy in ((0, -1), (0, 1), (-1, 0), (1, 0)):
        hx, hy = cx + dx * dist, cy + dy * dist
        out.append(_shell(hx, hy, rh))
        lx, ly = cx + dx * (dist + rh + 14), cy + dy * (dist + rh + 14)
        out.append(_label(lx, ly + 5, "H", size=15, weight="700"))
        mx, my = cx + dx * (dist / 2.0), cy + dy * (dist / 2.0)
        out.append(_bond_pairs(mx, my, 1, -dy, dx))
    return _svg_open(fig, w, h) + "".join(out) + "</svg>"


def draw_co2(fig):
    w, h = fig.get("w", 340), fig.get("h", 170)
    cy = h / 2.0
    cx = w / 2.0
    dist = 80
    rc, ro = 26, 30
    ox1, ox2 = cx - dist, cx + dist
    out = [_shell(cx, cy, rc), _label(cx, cy + 5, "C", size=16, weight="700"),
           _shell(ox1, cy, ro), _label(ox1 - ro - 14, cy + 5, "O", size=16, weight="700"),
           _shell(ox2, cy, ro), _label(ox2 + ro + 14, cy + 5, "O", size=16, weight="700"),
           _bond_pairs((cx + ox1) / 2.0, cy, 2, 0, 1),
           _bond_pairs((cx + ox2) / 2.0, cy, 2, 0, 1)]
    for ox, sign in ((ox1, -1), (ox2, 1)):
        out.append(_lone_pair(ox + sign * (ro - 8), cy - 15, "cross", axis="v"))
        out.append(_lone_pair(ox + sign * (ro - 8), cy + 15, "cross", axis="v"))
    return _svg_open(fig, w, h) + "".join(out) + "</svg>"


def draw_nh3(fig):
    w, h = fig.get("w", 280), fig.get("h", 280)
    cx, cy = w / 2.0, h / 2.0 + 12
    rn, rh, dist = 30, 20, 62
    out = [_shell(cx, cy, rn), _label(cx, cy + 5, "N", size=16, weight="700")]
    for ang in (90, 210, 330):          # fan downward — leaves the top free
        rad = math.radians(ang)
        hx, hy = cx + dist * math.cos(rad), cy + dist * math.sin(rad)
        out.append(_shell(hx, hy, rh))
        lx = cx + (dist + rh + 16) * math.cos(rad)
        ly = cy + (dist + rh + 16) * math.sin(rad)
        out.append(_label(lx, ly + 5, "H", size=15, weight="700"))
        mx, my = cx + (dist / 2.0) * math.cos(rad), cy + (dist / 2.0) * math.sin(rad)
        out.append(_bond_pairs(mx, my, 1, -math.sin(rad), math.cos(rad)))
    out.append(_lone_pair(cx, cy - rn + 8, "dot", axis="h"))
    return _svg_open(fig, w, h) + "".join(out) + "</svg>"


def draw_h2o(fig):
    w, h = fig.get("w", 260), fig.get("h", 260)
    cx, cy = w / 2.0, h / 2.0 - 6
    ro, rh, dist = 30, 20, 60
    out = [_shell(cx, cy, ro), _label(cx, cy + 5, "O", size=16, weight="700")]
    for ang in (55, 125):               # fan downward — leaves top/sides free
        rad = math.radians(ang)
        hx, hy = cx + dist * math.cos(rad), cy + dist * math.sin(rad)
        out.append(_shell(hx, hy, rh))
        lx = cx + (dist + rh + 16) * math.cos(rad)
        ly = cy + (dist + rh + 16) * math.sin(rad)
        out.append(_label(lx, ly + 5, "H", size=15, weight="700"))
        mx, my = cx + (dist / 2.0) * math.cos(rad), cy + (dist / 2.0) * math.sin(rad)
        out.append(_bond_pairs(mx, my, 1, -math.sin(rad), math.cos(rad)))
    out.append(_lone_pair(cx - ro + 6, cy - 6, "dot", axis="v"))
    out.append(_lone_pair(cx + ro - 6, cy - 6, "dot", axis="v"))
    return _svg_open(fig, w, h) + "".join(out) + "</svg>"


def draw_mgo(fig):
    """Ionic, not covalent: Mg gives up its 2 outer electrons to O, so
    Mg2+ is drawn with an EMPTY shell (nothing to place) and O2- is drawn
    with all 8 electrons round it — 6 its own (dots) plus the 2 gained
    from Mg (crosses) — the two crosses being what the question means by
    "the two crosses" on this figure."""
    w, h = fig.get("w", 340), fig.get("h", 240)
    cy = h / 2.0
    mgx, ox = w / 2.0 - 90, w / 2.0 + 60
    rmg, ro = 20, 36
    out = [_bracket(mgx, cy, rmg + 10, rmg + 16),
           _label(mgx, cy + 5, "Mg", size=15, weight="700"),
           _label(mgx + rmg + 20, cy - rmg - 10, "2+", size=13, weight="700"),
           _bracket(ox, cy, ro + 12, ro + 20),
           _label(ox, cy + 5, "O", size=16, weight="700"),
           _label(ox + ro + 22, cy - ro - 12, "2-", size=13, weight="700")]
    marks = ["dot"] * 6 + ["cross"] * 2
    for i, kind in enumerate(marks):
        ang = math.radians(360.0 * i / len(marks))
        ex, ey = ox + ro * math.cos(ang), cy + ro * math.sin(ang)
        out.append(_mark(kind, ex, ey))
    return _svg_open(fig, w, h) + "".join(out) + "</svg>"


def draw_polymer_unit(fig):
    """A generic repeat-unit chain in square brackets with a trailing
    `n` — `fig["chain"]` is the list of atom labels the CATALOGUE authors,
    so the exact monomer structure is the catalogue's call, not a
    chemistry fact hard-coded here."""
    chain = fig.get("chain")
    if not chain or len(chain) < 2:
        raise ValueError(
            "polymer-repeat-unit figure %r needs a `chain` of at least two "
            "atoms." % fig.get("id"))
    w = fig.get("w", 60 * len(chain) + 120)
    h = fig.get("h", 140)
    cy = h / 2.0
    step = (w - 140) / float(len(chain) - 1)
    xs = [70 + step * i for i in range(len(chain))]
    out = []
    for i, (x, label) in enumerate(zip(xs, chain)):
        out.append(_label(x, cy + 5, label, size=15, weight="700"))
        if i > 0:
            out.append(_line(xs[i - 1] + 10, cy, x - 10, cy, stroke=_SVG_INK, w=2))
    pad = 34
    out.append(_bracket(w / 2.0, cy, (xs[-1] - xs[0]) / 2.0 + pad, h / 2.0 - 14))
    out.append(_label(xs[-1] + pad + 16, cy + h / 2.0 - 20, "n", size=15,
                      weight="700", anchor="start"))
    return _svg_open(fig, w, h) + "".join(out) + "</svg>"


ART = {
    "molecule-h2": draw_h2,
    "molecule-ch4": draw_ch4,
    "molecule-co2": draw_co2,
    "molecule-nh3": draw_nh3,
    "molecule-h2o": draw_h2o,
    "molecule-mgo": draw_mgo,
    "polymer-repeat-unit": draw_polymer_unit,
}


if __name__ == "__main__":
    import xml.etree.ElementTree as ET

    def _check(name, svg):
        ET.fromstring(svg)
        print("ok: %-24s %6d bytes" % (name, len(svg)))

    base = {"title": "t", "desc": "d"}
    _check("H2", draw_h2(dict(base, id="sc-h2")))
    _check("CH4", draw_ch4(dict(base, id="sc-ch4")))
    _check("CO2", draw_co2(dict(base, id="sc-co2")))
    _check("NH3", draw_nh3(dict(base, id="sc-nh3")))
    _check("H2O", draw_h2o(dict(base, id="sc-h2o")))
    _check("MgO", draw_mgo(dict(base, id="sc-mgo")))
    _check("polyester repeat unit", draw_polymer_unit(
        dict(base, id="sc-poly", chain=["O", "C", "C", "O", "C", "C"])))
    print("bonding.py self-check: every molecule renders well-formed SVG")
