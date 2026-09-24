"""figlib.ks4elec — KS4 electricity question builders.

⊕ MRB-352 run 2, batch 3 (KS4 physics electricity, the 174 flagged rows).
Kept in its own module so parallel lanes editing `physics.py` cannot collide
with it; `figlib/__init__.py` merges `ART_KS4ELEC` into `figlib.ART`.

`radial_field` is specified by the examiner (spec174_ks4_electricity.md, B5):
the electric field around a charged sphere, AQA 8463 §4.2.5.2 (physics
only) — "The electric field is strongest close to the charged object. The
further away from the charged object, the weaker the field." What the pupil
reads is the SPACING of straight radial lines, so nothing else is drawn: no
force arrows, no "strong"/"weak" words, no distances, no numbers.
"""

import math

from .style import STYLE, Canvas, q_font, q_stroke, text as _q_text

ST = STYLE["stroke"]
LBL = STYLE["label"]
CREAM = STYLE["cream"]


def radial_field(W=420, n_lines=12, sign="+", points=()):
    """A charged sphere at the centre of a square card, with `n_lines`
    straight, evenly spaced radial field lines (the first pointing right),
    each carrying one solid arrowhead at 55 % of its length — pointing AWAY
    from the sphere for sign "+", towards it for "-".

    `points` is [{"label", "r", "angle"}]: a filled dot at polar (r × W
    from the centre, `angle` degrees anticlockwise from the right), its bold
    label just outside the dot on the side away from the sphere. A point or
    label that would touch a line is refused, not drawn."""
    if sign not in ("+", "-"):
        raise ValueError("radial_field: sign is '+' or '-'")
    c = Canvas(W, W)
    cx = cy = W / 2.0
    R = 0.09 * W                       # the sphere
    inset = 18                         # lines end this far inside the card
    sw = q_stroke(W, 2.5)
    head, half = 16.0, 7.0             # arrowhead length and half-width
    fs = q_font(W, floor=22)
    angles = [360.0 * k / n_lines for k in range(n_lines)]

    for a in angles:
        t = math.radians(a)
        ux, uy = math.cos(t), -math.sin(t)          # SVG y runs down
        reach = (W / 2.0 - inset) / max(abs(ux), abs(uy))
        x0, y0 = cx + R * ux, cy + R * uy
        x1, y1 = cx + reach * ux, cy + reach * uy
        c.S.append(f'<line x1="{x0:.1f}" y1="{y0:.1f}" x2="{x1:.1f}" '
                   f'y2="{y1:.1f}" stroke="{ST}" stroke-width="{sw}" '
                   f'stroke-linecap="round"/>')
        # one solid head, its centre at 55 % of the line's length
        rm = R + 0.55 * (reach - R)
        d = 1 if sign == "+" else -1
        tip = rm + d * head / 2
        base = rm - d * head / 2
        tx, ty = cx + tip * ux, cy + tip * uy
        bx, by = cx + base * ux, cy + base * uy
        nx, ny = -uy * half, ux * half
        c.S.append(f'<polygon points="{tx:.1f},{ty:.1f} {bx+nx:.1f},'
                   f'{by+ny:.1f} {bx-nx:.1f},{by-ny:.1f}" fill="{ST}" '
                   f'stroke="none"/>')

    # the sphere, drawn over the line ends, with its sign
    c.S.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{R:.1f}" '
               f'fill="{CREAM}" stroke="{ST}" stroke-width="{sw}"/>')
    _q_text(c, cx, cy + 0.36 * fs * 1.3, sign, int(fs * 1.3), ST, "bold")

    for p in points:
        t = math.radians(p["angle"])
        ux, uy = math.cos(t), -math.sin(t)
        r = p["r"] * W
        # clearance from the nearest line, perpendicular
        off = min(abs(((p["angle"] - a + 180) % 360) - 180) for a in angles)
        dot_clear = r * math.sin(math.radians(off))
        rl = r + 6 + 0.75 * fs                      # label centre, outward
        lab_clear = rl * math.sin(math.radians(off))
        if off <= 0 or dot_clear < 6 + 4 or lab_clear < 0.62 * fs + 4:
            raise ValueError("radial_field: point %r would touch a field "
                             "line" % p["label"])
        if r <= R + 12:
            raise ValueError("radial_field: point %r is inside the sphere"
                             % p["label"])
        x, y = cx + r * ux, cy + r * uy
        c.S.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="6" fill="{ST}" '
                   f'stroke="none"/>')
        lx, ly = cx + rl * ux, cy + rl * uy
        _q_text(c, lx, ly + 0.35 * fs, p["label"], fs, LBL, "bold")
    return c.svg()


ART_KS4ELEC = {
    "radial-field": radial_field,
}
