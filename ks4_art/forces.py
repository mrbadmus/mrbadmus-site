"""ks4_art.forces — free-body diagrams and force-resolution triangles.

The triangle half is `ks3_art.kit._triangle` with `shape="resolution"`,
verbatim — the only thing this module adds is a free-body diagram, which
`_triangle` was never shaped to draw (it has one body, not two below it).
"""

import math

from ks3_art.kit import _svg_open, _circle, _line, _path, _label, _triangle, _n, _SVG_INK


def _fb_arrowhead(x, y, angle_deg, size=8):
    a1 = math.radians(angle_deg + 150)
    a2 = math.radians(angle_deg - 150)
    x1, y1 = x + size * math.cos(a1), y + size * math.sin(a1)
    x2, y2 = x + size * math.cos(a2), y + size * math.sin(a2)
    return _path("M %s,%s L %s,%s L %s,%s Z"
                 % (_n(x), _n(y), _n(x1), _n(y1), _n(x2), _n(y2)),
                 fill=_SVG_INK, stroke=None)


def draw_free_body(fig):
    """`fig["forces"]` — a list of `{"angle": deg, "length": px, "label":
    str}`. `angle` is 0 = pointing right, growing clockwise (SVG's own
    convention, since y already grows downward) — 90 points down, -90 (or
    270) points up. Every arrow is drawn to a length proportional to
    `length`, so two forces given different `length`s are visibly
    different arrows, never the same arrow relabelled — the confusion a
    free-body question most often tests.
    """
    forces = fig.get("forces") or []
    if not forces:
        raise ValueError("free-body figure %r has no forces." % fig.get("id"))
    w, h = fig.get("w", 300), fig.get("h", 300)
    cx, cy = w / 2.0, h / 2.0
    body_r = fig.get("body_r", 22)
    out = [_circle(cx, cy, body_r, stroke=_SVG_INK, w=2.5)]
    if fig.get("body_label"):
        out.append(_label(cx, cy + 5, fig["body_label"], size=14, weight="700"))
    for f in forces:
        if "angle" not in f or "label" not in f:
            raise ValueError(
                "free-body figure %r has a force with no `angle` or no "
                "`label`." % fig.get("id"))
        ang = f["angle"]
        length = f.get("length", 70)
        rad = math.radians(ang)
        x1 = cx + body_r * math.cos(rad)
        y1 = cy + body_r * math.sin(rad)
        x2 = cx + (body_r + length) * math.cos(rad)
        y2 = cy + (body_r + length) * math.sin(rad)
        out.append(_line(x1, y1, x2, y2, stroke=_SVG_INK, w=3))
        out.append(_fb_arrowhead(x2, y2, ang))
        lx, ly = x2 + 16 * math.cos(rad), y2 + 16 * math.sin(rad)
        out.append(_label(lx, ly + 5, f["label"], size=14, weight="700"))
    return _svg_open(fig, w, h) + "".join(out) + "</svg>"


def draw_resolution_triangle(fig):
    """`_triangle(shape="resolution")`, verbatim — reads `fig["angle"]`,
    `fig["hyp_label"]`, `fig["horiz_label"]`, `fig["vert_label"]`,
    `fig.get("angle_label")`."""
    for key in ("angle", "hyp_label", "horiz_label", "vert_label"):
        if fig.get(key) is None:
            raise ValueError(
                "resolution-triangle figure %r has no `%s`." % (fig.get("id"), key))
    return _triangle(fig, fig.get("w", 260), fig.get("h", 240), shape="resolution",
                     relationship="product", angle=fig["angle"],
                     hyp_label=fig["hyp_label"], horiz_label=fig["horiz_label"],
                     vert_label=fig["vert_label"], angle_label=fig.get("angle_label"))


def draw_formula_triangle(fig):
    """`_triangle(shape="formula")`, verbatim — speed/distance/time,
    weight/mass/gravity, density, and any other product-only formula.
    Reads `fig["top"]`, `fig["bottom_left"]`, `fig["bottom_right"]`."""
    for key in ("top", "bottom_left", "bottom_right"):
        if not fig.get(key):
            raise ValueError(
                "formula-triangle figure %r has no `%s`." % (fig.get("id"), key))
    return _triangle(fig, fig.get("w", 220), fig.get("h", 200), shape="formula",
                     relationship="product", top=fig["top"],
                     bottom_left=fig["bottom_left"], bottom_right=fig["bottom_right"])


ART = {
    "free-body-diagram": draw_free_body,
    "resolution-triangle": draw_resolution_triangle,
    "formula-triangle": draw_formula_triangle,
}


if __name__ == "__main__":
    import xml.etree.ElementTree as ET

    def _check(name, svg):
        ET.fromstring(svg)
        print("ok: %-28s %6d bytes" % (name, len(svg)))

    _check("free-body · humpback bridge", draw_free_body({
        "id": "sc-fb", "title": "t", "desc": "d", "body_label": "car",
        "forces": [{"angle": 90, "length": 60, "label": "weight"},
                  {"angle": -90, "length": 50, "label": "normal"}]}))
    _check("resolution triangle", draw_resolution_triangle({
        "id": "sc-res", "title": "t", "desc": "d", "angle": 35,
        "hyp_label": "F", "horiz_label": "F cos θ", "vert_label": "F sin θ",
        "angle_label": "θ"}))
    _check("formula triangle · speed", draw_formula_triangle({
        "id": "sc-fml", "title": "t", "desc": "d",
        "top": "s", "bottom_left": "d", "bottom_right": "t"}))
    print("forces.py self-check: every drawer renders well-formed SVG")
