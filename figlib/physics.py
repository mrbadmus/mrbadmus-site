"""
Rainford High School — Physics Paper 1 Diagram Library
=======================================================
Mr Badmus house style (inherited from chem_diagrams style core).

PHASE 1: circuit engine.

Describe a circuit as a netlist; the engine lays it out on a
rectangular loop with no wire crossings, AQA-convention symbols,
meters placed correctly, and clear value labels.

Usage:
    from physics_diagrams import circuit, parallel, export
    svg = circuit([("cell",), ("switch",),
                    ("lamp","L1"),
                    parallel([[("resistor","R1","10 \u03a9")],
                              [("lamp","L2")]]),
                    ("ammeter",)])
    export(svg, "demo")
"""

import math
from .style import STYLE, Canvas, export   # inherit style + export
from .style import label_font as _label_font

ST = STYLE["stroke"]
LBL = STYLE["label"]
RED = "#C8102E"           # FIFA red — copy-this values
ACC = STYLE["arrow"]      # teal accent
FONT = STYLE["font"]


# ====================================================================
# WIRE + LABEL HELPERS
# ====================================================================
def _wire(c, x1, y1, x2, y2, w=3):
    c.S.append(
        f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
        f'stroke="{ST}" stroke-width="{w}" stroke-linecap="round"/>')


def _dot(c, x, y, r=6):
    c.S.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{ST}"/>')


def _clabel(c, x, y, txt, size=22, fill=None, weight="bold"):
    """⊕ MRB-352 b1 fix: a circuit label carrying a digit ("A1", "V1",
    "10 Ω") takes style.NUM_FONT like every other figlib label. This helper
    predates style.text() and hard-coded Georgia, whose old-style "1" is
    x-height tall and read as "AI"/"VI" at phone size (visual review 5)."""
    fill = fill or LBL
    txt = (str(txt).replace("&", "&amp;")
                   .replace("<", "&lt;").replace(">", "&gt;"))
    c.S.append(
        f'<text x="{x:.1f}" y="{y:.1f}" font-family="{_label_font(txt)}" '
        f'font-size="{size}" fill="{fill}" text-anchor="middle" '
        f'font-weight="{weight}">{txt}</text>')


# ====================================================================
# COMPONENT SYMBOLS  (AQA convention). Each draws a symbol of total
# horizontal span SPAN centred on (x,y), wires entering/leaving at
# y on the left/right ends. Returns nothing; the engine handles wires
# between components.
# ====================================================================
SPAN = 120          # horizontal length each component occupies
GAP = 14            # symbol body inset from the component cell ends


def _leads(c, x, y, body_w):
    """Draw the short lead wires either side of a centred symbol body."""
    half = body_w/2
    _wire(c, x-SPAN/2, y, x-half, y)
    _wire(c, x+half, y, x+SPAN/2, y)
    return half


# ⊕ figlib (MRB-352 run 2): every symbol below was checked against the
# settled reference, AQA GCSE Physics 8463 spec v1.1 §4.2.1.1 p.24, and
# redrawn where the library's version differed from it. The library's
# originals are in the source file named in figlib/README.md. Differences:
#   cell        AQA marks only "+" (library also printed "–"); both plates
#               the SAME line weight, the short plate only shorter — as
#               p.24 draws them. (⊕ fix round 1: this comment once said the
#               short plate was "a little thicker", which misread the sheet;
#               the thick short plate is a BS convention, not AQA's.)
#   battery     cell, dashed wire, cell — AQA's drawing (library drew two
#               cells touching).
#   switch      open circles for the contacts; open = lever hinged at the
#               left contact and dropped clear of the right one; closed =
#               lever joining both contacts (library: filled dots, lever up).
#   diode, LED  the wire runs through the circle and the triangle to the
#               bar (library stopped the wire at the circle).
#   thermistor  diagonal line fully through the body, no arrowhead, with a
#               short horizontal tail at its lower-left end.
#   LDR         the wire runs into the circle to the small rectangle; two
#               arrows point IN from the upper left.
# `sym_motor` and `sym_power` stay for the library's own teaching sheets,
# but are NOT in AQA_SYMBOLS: neither is on the AQA 8463 list, so no
# question figure may draw one (figlib.checks refuses a circled M or a
# "d.c." box in the manifest).
_HOLLOW = STYLE["cream"]


def sym_cell(c, x, y, name=None, value=None):
    half = _leads(c, x, y, 18)
    _wire(c, x-9, y-26, x-9, y+26, 3)               # long plate (+)
    _wire(c, x+9, y-14, x+9, y+14, 3)               # short plate, same weight
    _clabel(c, x-24, y-24, "+", 26)
    if value:
        _clabel(c, x, y+52, value, 22, RED)


def sym_battery(c, x, y, name=None, value=None):
    half = _leads(c, x, y, 78)
    _wire(c, x-39, y-26, x-39, y+26, 3)             # first cell, +
    _wire(c, x-25, y-14, x-25, y+14, 3)
    c.S.append(
        f'<line x1="{x-19}" y1="{y}" x2="{x+19}" y2="{y}" stroke="{ST}" '
        f'stroke-width="3" stroke-dasharray="6 5"/>')  # "more cells here"
    _wire(c, x+25, y-26, x+25, y+26, 3)             # last cell
    _wire(c, x+39, y-14, x+39, y+14, 3)
    _wire(c, x-25, y, x-19, y)
    _wire(c, x+19, y, x+25, y)
    _clabel(c, x-54, y-24, "+", 26)
    if value:
        _clabel(c, x, y+52, value, 22, RED)


def sym_power(c, x, y, name=None, value=None):
    half = _leads(c, x, y, 70)
    c.S.append(
        f'<rect x="{x-35}" y="{y-26}" width="70" height="52" rx="6" '
        f'fill="none" stroke="{ST}" stroke-width="3"/>')
    _clabel(c, x, y+6, "d.c.", 20)
    if value:
        _clabel(c, x, y+52, value, 22, RED)


def sym_resistor(c, x, y, name=None, value=None):
    half = _leads(c, x, y, 80)
    c.S.append(
        f'<rect x="{x-40}" y="{y-17}" width="80" height="34" '
        f'fill="none" stroke="{ST}" stroke-width="3"/>')
    if name:
        _clabel(c, x, y-30, name, 22)
    if value:
        _clabel(c, x, y+44, value, 22, RED)


def sym_variable_resistor(c, x, y, name=None, value=None):
    half = _leads(c, x, y, 80)
    c.S.append(
        f'<rect x="{x-40}" y="{y-17}" width="80" height="34" '
        f'fill="none" stroke="{ST}" stroke-width="3"/>')
    # a straight line FULLY through the body and out beyond both sides,
    # with its arrowhead at the upper right
    c.S.append(
        f'<line x1="{x-34}" y1="{y+34}" x2="{x+26}" y2="{y-26}" '
        f'stroke="{ST}" stroke-width="3" stroke-linecap="round"/>')
    c.S.append(
        f'<polygon points="{x+38},{y-38} {x+18},{y-30} {x+30},{y-18}" '
        f'fill="{ST}" stroke="none"/>')
    if name:
        _clabel(c, x, y-46, name, 22)
    if value:
        _clabel(c, x, y+56, value, 22, RED)


def sym_lamp(c, x, y, name=None, value=None):
    half = _leads(c, x, y, 56)
    r = 26
    c.S.append(
        f'<circle cx="{x}" cy="{y}" r="{r}" fill="none" '
        f'stroke="{ST}" stroke-width="3"/>')
    d = r/math.sqrt(2)
    _wire(c, x-d, y-d, x+d, y+d, 3)
    _wire(c, x-d, y+d, x+d, y-d, 3)
    if name:
        _clabel(c, x, y-36, name, 22)
    if value:
        _clabel(c, x, y+50, value, 22, RED)


def sym_switch(c, x, y, name=None, value=None, closed=False):
    half = _leads(c, x, y, 64)
    for cx_ in (x-26, x+26):
        c.S.append(
            f'<circle cx="{cx_}" cy="{y}" r="6" fill="{_HOLLOW}" '
            f'stroke="{ST}" stroke-width="3"/>')
    if closed:
        _wire(c, x-21, y+3, x+21, y-4, 3)            # lever on both contacts
    else:
        _wire(c, x-21, y+3, x+18, y+26, 3)           # lever dropped clear
    if name:
        _clabel(c, x, y-40, name, 22)


def sym_switch_closed(c, x, y, name=None, value=None):
    sym_switch(c, x, y, name, value, closed=True)


def sym_ammeter(c, x, y, name=None, value=None):
    half = _leads(c, x, y, 52)
    c.S.append(
        f'<circle cx="{x}" cy="{y}" r="26" fill="none" '
        f'stroke="{ST}" stroke-width="3"/>')
    _clabel(c, x, y+9, "A", 26, ST)   # ⊕ symbol ink: part of the symbol (AQA p24), never an answer letter
    if value:
        _clabel(c, x, y+50, value, 22, RED)


def sym_voltmeter(c, x, y, name=None, value=None, leads=True):
    if leads:
        _leads(c, x, y, 52)
    c.S.append(
        f'<circle cx="{x}" cy="{y}" r="26" fill="none" '
        f'stroke="{ST}" stroke-width="3"/>')
    _clabel(c, x, y+9, "V", 26, ST)   # ⊕ symbol ink: part of the symbol (AQA p24), never an answer letter
    if value:
        _clabel(c, x, y+50, value, 22, RED)


def sym_thermistor(c, x, y, name=None, value=None):
    half = _leads(c, x, y, 80)
    c.S.append(
        f'<rect x="{x-40}" y="{y-17}" width="80" height="34" '
        f'fill="none" stroke="{ST}" stroke-width="3"/>')
    # a short horizontal tail at the lower left, then a straight diagonal
    # fully through the body and out above it — no arrowhead
    c.S.append(
        f'<polyline points="{x-40},{y+30} {x-22},{y+30} {x+26},{y-34}" '
        f'fill="none" stroke="{ST}" stroke-width="3" '
        f'stroke-linecap="round" stroke-linejoin="round"/>')
    if name:
        _clabel(c, x, y-46, name, 22)


def sym_ldr(c, x, y, name=None, value=None):
    _wire(c, x-SPAN/2, y, x-20, y)                   # wire into the circle
    _wire(c, x+20, y, x+SPAN/2, y)                   # … to the rectangle
    c.S.append(
        f'<rect x="{x-20}" y="{y-8}" width="40" height="16" '
        f'fill="none" stroke="{ST}" stroke-width="3"/>')
    c.S.append(
        f'<circle cx="{x}" cy="{y}" r="30" fill="none" '
        f'stroke="{ST}" stroke-width="3"/>')
    # two parallel arrows, side by side, pointing IN from the upper left
    for k in (0, 1):
        sx = x - 58 + k*16
        sy = y - 58 - k*6
        ex = sx + 26
        ey = sy + 26
        _wire(c, sx, sy, ex-6, ey-6, 2.5)
        c.S.append(
            f'<polygon points="{ex},{ey} {ex-13},{ey-4} '
            f'{ex-4},{ey-13}" fill="{ST}" stroke="none"/>')
    if name:
        _clabel(c, x, y+56, name, 22)


def sym_diode(c, x, y, name=None, value=None):
    half = _leads(c, x, y, 56)
    c.S.append(
        f'<circle cx="{x}" cy="{y}" r="28" fill="none" '
        f'stroke="{ST}" stroke-width="3"/>')
    _wire(c, x-28, y, x+13, y, 3)                    # the wire runs through
    c.S.append(
        f'<polygon points="{x-13},{y-15} {x-13},{y+15} {x+13},{y}" '
        f'fill="none" stroke="{ST}" stroke-width="3" '
        f'stroke-linejoin="round"/>')
    _wire(c, x+13, y-16, x+13, y+16, 3)
    _wire(c, x+13, y, x+28, y, 3)
    if name:
        _clabel(c, x, y-40, name, 22)


def sym_led(c, x, y, name=None, value=None):
    sym_diode(c, x, y, name)
    # two parallel emission arrows, side by side, pointing OUT (up-right)
    for k in (0, 1):
        ax = x + 10 + k*16
        ay = y - 30 + k*6
        _wire(c, ax, ay, ax+18, ay-18, 2.5)
        c.S.append(
            f'<polygon points="{ax+24},{ay-24} {ax+11},{ay-21} '
            f'{ax+20},{ay-11}" fill="{ST}" stroke="none"/>')


def sym_fuse(c, x, y, name=None, value=None):
    half = _leads(c, x, y, 70)
    c.S.append(
        f'<rect x="{x-35}" y="{y-15}" width="70" height="30" '
        f'fill="none" stroke="{ST}" stroke-width="3"/>')
    _wire(c, x-35, y, x+35, y, 2)
    if name:
        _clabel(c, x, y-28, name, 22)


def sym_motor(c, x, y, name=None, value=None):
    half = _leads(c, x, y, 52)
    c.S.append(
        f'<circle cx="{x}" cy="{y}" r="26" fill="none" '
        f'stroke="{ST}" stroke-width="3"/>')
    _clabel(c, x, y+8, "M", 26)


SYMBOLS = {
    "cell": sym_cell, "battery": sym_battery, "power": sym_power,
    "resistor": sym_resistor, "variable_resistor": sym_variable_resistor,
    "lamp": sym_lamp, "switch": sym_switch,
    "switch_closed": sym_switch_closed, "ammeter": sym_ammeter,
    "voltmeter": sym_voltmeter, "thermistor": sym_thermistor,
    "ldr": sym_ldr, "diode": sym_diode, "led": sym_led,
    "fuse": sym_fuse, "motor": sym_motor,
}

# The AQA 8463 §4.2.1.1 list, in the spec's own order, and nothing else.
# A question figure may only draw these (figlib.physics.circuit refuses
# anything outside it when called with aqa_only=True, as every question
# figure is).
AQA_SYMBOLS = (
    ("switch", "switch (open)"), ("switch_closed", "switch (closed)"),
    ("cell", "cell"), ("battery", "battery"), ("diode", "diode"),
    ("resistor", "resistor"), ("variable_resistor", "variable resistor"),
    ("led", "LED"), ("lamp", "lamp"), ("fuse", "fuse"),
    ("voltmeter", "voltmeter"), ("ammeter", "ammeter"),
    ("thermistor", "thermistor"), ("ldr", "LDR"),
)


# ====================================================================
# NETLIST + LAYOUT ENGINE
# ====================================================================
class parallel:
    """Marks a parallel section: a list of branches, each a list of
    series component tuples."""
    def __init__(self, branches):
        self.branches = branches


def _series_width(items):
    """Total horizontal width a series run of items needs."""
    w = 0
    for it in items:
        if isinstance(it, parallel):
            w += max(_series_width(b) for b in it.branches) + 80
        elif it[0] == "voltmeter":
            continue            # ⊕ figlib: bridges the previous span
        else:
            w += SPAN
    return w


class _Tmp:
    def __init__(self):
        self.S = []


# ⊕ fix round 1 — geometry of emitted fragments, for centring a symbol
# (visual m7) and for merging butted wire segments (visual m5).
def _frag_el(frag):
    import xml.etree.ElementTree as _ET
    try:
        root = _ET.fromstring('<svg xmlns="http://www.w3.org/2000/svg">%s</svg>'
                              % frag)
    except _ET.ParseError:
        return None
    kids = list(root)
    return kids[0] if len(kids) == 1 else None


def _bbox(el):
    """(x0, y0, x1, y1) of one element, stroke included; None if unknown."""
    if el is None:
        return None
    tag = el.tag.split("}")[-1]
    g = lambda k: float(el.get(k, 0))  # noqa: E731
    hw = float(el.get("stroke-width", 0)) / 2 if el.get("stroke", "none") != "none" else 0
    if tag == "line":
        xs, ys = (g("x1"), g("x2")), (g("y1"), g("y2"))
    elif tag == "circle":
        xs, ys = (g("cx") - g("r"), g("cx") + g("r")), (g("cy") - g("r"), g("cy") + g("r"))
    elif tag == "ellipse":
        xs, ys = (g("cx") - g("rx"), g("cx") + g("rx")), (g("cy") - g("ry"), g("cy") + g("ry"))
    elif tag == "rect":
        xs, ys = (g("x"), g("x") + g("width")), (g("y"), g("y") + g("height"))
    elif tag in ("polygon", "polyline", "path"):
        import re as _re
        v = [float(n) for n in _re.findall(r"-?\d*\.?\d+",
                                            el.get("points") or el.get("d") or "")]
        if len(v) < 2:
            return None
        xs, ys = v[0::2], v[1::2]
    elif tag == "text":
        s = float(el.get("font-size", 16))
        n = len("".join(el.itertext()))
        x, y = g("x"), g("y")
        w = 0.6 * s * n
        a = el.get("text-anchor", "start")
        x0 = x - (w/2 if a == "middle" else w if a == "end" else 0)
        return (x0, y - 0.75*s, x0 + w, y + 0.2*s)
    else:
        return None
    return (min(xs) - hw, min(ys) - hw, max(xs) + hw, max(ys) + hw)


def _extent_y(frags):
    boxes = [b for b in (_bbox(_frag_el(f)) for f in frags) if b]
    return min(b[1] for b in boxes), max(b[3] for b in boxes)


def _merge_wires(frags):
    """Join collinear wire segments that meet end to end into one <line>.

    ⊕ fix round 1 (visual m5). The engine draws a straight run of wire as
    several butted <line>s (a lead, the next symbol's lead, a corner
    stub); at a fractional phone scale every join shows a darker 1px dot.
    Only identical, undashed, axis-aligned lines are joined, and a join is
    made only when it cannot change what is painted over what: the merged
    line takes the EARLIEST segment's place in paint order, so it is
    refused if anything painted between that place and a later segment
    touches that later segment (a diode's circle, a junction dot, a hollow
    switch contact)."""
    els = [_frag_el(f) for f in frags]
    boxes = [_bbox(e) for e in els]

    def seg(i):
        e = els[i]
        if e is None or e.tag.split("}")[-1] != "line" or e.get("stroke-dasharray"):
            return None
        x1, y1, x2, y2 = (float(e.get(k)) for k in ("x1", "y1", "x2", "y2"))
        key = tuple(sorted((k, v) for k, v in e.attrib.items()
                           if k not in ("x1", "y1", "x2", "y2")))
        if abs(y1 - y2) < 0.05 and abs(x1 - x2) > 0.05:
            return ("h", round(y1, 1), key), min(x1, x2), max(x1, x2)
        if abs(x1 - x2) < 0.05 and abs(y1 - y2) > 0.05:
            return ("v", round(x1, 1), key), min(y1, y2), max(y1, y2)
        return None

    def hits(a, b):
        return (a is not None and b is not None and a[0] < b[2] - 0.05
                and b[0] < a[2] - 0.05 and a[1] < b[3] - 0.05
                and b[1] < a[3] - 0.05)

    out = list(frags)
    changed = True
    while changed:
        changed = False
        live = [i for i in range(len(out)) if out[i]]
        segs = {i: seg(i) for i in live}
        for i in live:
            if not segs[i]:
                continue
            for j in live:
                if j <= i or not segs[j] or segs[j][0] != segs[i][0]:
                    continue
                (gi, a0, a1), (_, b0, b1) = segs[i], segs[j]
                if b0 > a1 + 0.05 or a0 > b1 + 0.05:
                    continue            # not touching
                if any(hits(boxes[k], boxes[j]) for k in range(i + 1, j)
                       if out[k]):
                    continue            # would change the paint order
                lo, hi = min(a0, b0), max(a1, b1)
                e = els[i]
                if gi[0] == "h":
                    e.set("x1", "%.1f" % lo); e.set("x2", "%.1f" % hi)
                else:
                    e.set("y1", "%.1f" % lo); e.set("y2", "%.1f" % hi)
                attrs = " ".join('%s="%s"' % kv for kv in e.attrib.items())
                out[i] = "<line %s/>" % attrs
                els[i] = _frag_el(out[i])
                boxes[i] = _bbox(els[i])
                out[j] = ""
                changed = True
                break
            if changed:
                break
    return [f for f in out if f]


def _draw_rotated(c, fn, x, y, name=None, value=None):
    """Draw a symbol turned a quarter-turn clockwise, centred on (x, y),
    for a component on a vertical wire. Shapes are turned by rewriting
    their coordinates (a rect stays a rect, a circle a circle) — never by a
    transform attribute, which the manifest's element set does not carry.
    Labels are moved with the drawing but stay upright."""
    import xml.etree.ElementTree as _ET
    tmp = _Tmp()
    _draw_centered(tmp, fn, 0, 0, name, value)

    def rot(px, py):
        return x - py, y + px

    ns = "{http://www.w3.org/2000/svg}"
    for frag in tmp.S:
        root = _ET.fromstring('<svg xmlns="http://www.w3.org/2000/svg">%s</svg>'
                              % frag)
        for el in root:
            tag = el.tag.replace(ns, "")
            a = dict(el.attrib)
            if tag == "line":
                a["x1"], a["y1"] = ("%.1f" % v for v in rot(float(a["x1"]), float(a["y1"])))
                a["x2"], a["y2"] = ("%.1f" % v for v in rot(float(a["x2"]), float(a["y2"])))
            elif tag == "circle":
                a["cx"], a["cy"] = ("%.1f" % v for v in rot(float(a["cx"]), float(a["cy"])))
            elif tag == "rect":
                x0, y0 = float(a["x"]), float(a["y"])
                w, h = float(a["width"]), float(a["height"])
                pts = [rot(x0, y0), rot(x0 + w, y0 + h)]
                a["x"] = "%.1f" % min(q[0] for q in pts)
                a["y"] = "%.1f" % min(q[1] for q in pts)
                a["width"], a["height"] = "%.1f" % h, "%.1f" % w
            elif tag in ("polygon", "polyline"):
                vals = [float(v) for v in a["points"].replace(",", " ").split()]
                a["points"] = " ".join("%.1f,%.1f" % rot(vx, vy) for vx, vy
                                       in zip(vals[0::2], vals[1::2]))
            elif tag == "text":
                size = float(a.get("font-size", 22))
                vx, vy = rot(float(a["x"]), float(a["y"]) - 0.35*size)
                a["x"], a["y"] = "%.1f" % vx, "%.1f" % (vy + 0.35*size)
            else:
                raise ValueError("cannot rotate <%s>" % tag)
            attrs = " ".join('%s="%s"' % kv for kv in a.items())
            if tag == "text":
                c.S.append("<text %s>%s</text>" % (attrs, esc_text(el.text or "")))
            else:
                c.S.append("<%s %s/>" % (tag, attrs))


def esc_text(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


LIBRARY_LAYOUT = dict(min_w=900, margin=140, title_size=34)
# ⊕ figlib: the phone layout for a question figure. The engine is the same;
# only the frame around it tightens, so a three-component loop is ~480
# wide instead of 900 and its 26px symbol letters stay >= 11px on a phone.
QUESTION_LAYOUT = dict(min_w=360, margin=40, title_size=None)


def _comp(it):
    """(type, name, value, opts) from a netlist tuple/list of any length.
    A 4th element is an options dict: {"voltmeter": True} bridges a
    voltmeter across THIS component."""
    it = list(it)
    ctype = it[0]
    name = it[1] if len(it) > 1 else None
    value = it[2] if len(it) > 2 else None
    opts = it[3] if len(it) > 3 and isinstance(it[3], dict) else {}
    return ctype, name, value, opts


def _bridge_voltmeter(c, x0, x1, top_y, name=None, value=None):
    """A voltmeter above the span x0..x1 of the top wire, joined to the
    wire at both ends of that span — i.e. in parallel with whatever is
    drawn there."""
    xpos = (x0 + x1) / 2
    vy = top_y - 110
    sym_voltmeter(c, xpos, vy, name, value, leads=False)
    _wire(c, x0+10, top_y, x0+10, vy)
    _wire(c, x1-10, top_y, x1-10, vy)
    _wire(c, x0+10, vy, xpos-26, vy)
    _wire(c, xpos+26, vy, x1-10, vy)
    _dot(c, x0+10, top_y, 5)
    _dot(c, x1-10, top_y, 5)


def circuit(elements, title=None, layout=None, gap=None, aqa_only=False,
            left=None, right=None):
    """Lay out a circuit from a netlist. `elements` is a list of
    component tuples ("type","name","value"[, opts]) and/or parallel(...).

    ⊕ figlib additions, all keyword-only in effect and all defaulting to the
    library's own behaviour:
      layout    LIBRARY_LAYOUT (default) or QUESTION_LAYOUT — the frame.
      gap       "start": the wire coming up the left side stops short of
                the first component, so the loop is visibly NOT complete.
      aqa_only  refuse any component outside AQA_SYMBOLS (motor, d.c.).
      left, right  components drawn on the loop's left / right side,
                turned a quarter-turn (question frame only).
      ("voltmeter",) on its own now bridges the component BEFORE it. The
                library drew it across a plain length of wire of its own —
                a voltmeter across nothing, which would read zero. A
                component can also carry {"voltmeter": True} as a 4th item.
    """
    L = dict(LIBRARY_LAYOUT)
    L.update(layout or {})
    aqa = {k for k, _ in AQA_SYMBOLS}
    top_items = list(elements)

    def _check(ct):
        if ct not in SYMBOLS:
            raise KeyError(f"Unknown component '{ct}'. "
                           f"Known: {', '.join(SYMBOLS)}")
        if aqa_only and ct not in aqa:
            raise ValueError(
                f"'{ct}' is not on the AQA 8463 circuit-symbol list "
                f"(§4.2.1.1) and cannot appear in a question figure.")

    # geometry: components run along the TOP edge; the loop closes
    # down the right, along the bottom, and up the left.
    series = [it for it in top_items
              if isinstance(it, parallel) or _comp(it)[0] != "voltmeter"]
    total_w = _series_width(series)
    has_v = any((not isinstance(it, parallel)) and
                (_comp(it)[0] == "voltmeter" or _comp(it)[3].get("voltmeter"))
                for it in top_items)
    has_par = any(isinstance(it, parallel) for it in top_items)
    # ⊕ fix round 1 (visual m4): when a parallel section ENDS the top run
    # (and nothing is drawn on the right side), the return wire drops from
    # that section's right-hand junction column itself. The library ran a
    # short tail out to a separate corner and dropped from there, which
    # drew two parallel verticals a few pixels apart — a doubled wire.
    par_last = (bool(top_items) and isinstance(top_items[-1], parallel)
                and len(top_items[-1].branches) > 1 and not right
                and not L.get("title_size"))
    max_branches = max(
        [len(it.branches) for it in top_items
         if isinstance(it, parallel)] + [1])
    par_extra = max(0, (max_branches - 2)) * 95
    left_x = L["margin"]
    if L.get("title_size"):
        # the library's frame, unchanged
        title_w_est = len(title or "") * 19 + 140
        W = int(max(L["min_w"], total_w + 2*left_x - 40, title_w_est))
        H = (510 if (has_v or has_par) else 470) + par_extra
        top_y = (235 if (has_v or has_par) else 175) + par_extra/2
        bot_y = top_y + 165 + par_extra/2
    else:
        # the question frame: as tight as the drawing allows
        above = 78
        if has_v:
            above = max(above, 150)
        spread = 95 * (max_branches - 1) if has_par else 0
        if has_par:
            above = max(above, spread/2 + 70)
        side_n = max(len(left or ()), len(right or ()))
        top_y = above
        bot_y = top_y + max(118, spread/2 + 70, side_n*SPAN + 40)
        W = int(max(L["min_w"], left_x + total_w + 40 + left_x))
        if par_last:
            W = int(max(L["min_w"], left_x + total_w + 20 + left_x))
        H = int(bot_y + 34)
    c = Canvas(W, H)
    if title and L.get("title_size"):
        c.label(W/2, 50, title, L["title_size"], "bold")

    if L.get("title_size"):
        if left or right:
            raise ValueError("left/right components need the question frame")
        cx = left_x
    else:
        # centre the top run between the two corners
        cx = left_x + (W - 2*left_x - total_w) / 2.0
        _wire(c, left_x, top_y, cx, top_y)
        for items, xs in ((left, left_x), (right, W - left_x)):
            n = len(items or ())
            if not n:
                continue
            ys = [top_y + (bot_y - top_y) * (k + 0.5) / n for k in range(n)]
            for k, (yc, it) in enumerate(zip(ys, items)):
                ct, nm, vl, _o = _comp(it)
                _check(ct)
                _draw_rotated(c, SYMBOLS[ct], xs, yc, nm, vl)
            edges = [top_y] + [yc for yc in ys] + [bot_y]
            for k in range(len(edges) - 1):
                a = edges[k] + (SPAN/2 if k else 0)
                b = edges[k + 1] - (SPAN/2 if k + 1 < len(edges) - 1 else 0)
                if xs == left_x and k == 0 and gap == "start":
                    continue
                if xs == left_x and k == len(edges) - 2:
                    pass
                if b > a:
                    _wire(c, xs, a, xs, b)
    prev_span = None
    for it in top_items:
        if not isinstance(it, parallel):
            ctype, name, value, opts = _comp(it)
            if ctype == "voltmeter":
                if prev_span is None:
                    raise ValueError("a voltmeter must follow the component "
                                     "it is connected across")
                _bridge_voltmeter(c, prev_span[0], prev_span[1], top_y,
                                  name, value)
                continue
            _check(ctype)
            _draw_centered(c, SYMBOLS[ctype], cx + SPAN/2, top_y, name, value)
            if opts.get("voltmeter"):
                _bridge_voltmeter(c, cx, cx + SPAN, top_y)
            prev_span = (cx, cx + SPAN)
            cx += SPAN
        else:  # parallel section
            par = it
            bw = max(_series_width(b) for b in par.branches) + 80
            n = len(par.branches)
            jin_x = cx
            jout_x = cx + bw
            _dot(c, jin_x, top_y)
            if not (par_last and it is top_items[-1]):
                _dot(c, jout_x, top_y)
            if n == 1:
                ys = [top_y]
            else:
                spread = 95 * (n - 1)
                ys = [top_y - spread/2 + spread*i/(n-1) for i in range(n)]
            for by, branch in zip(ys, par.branches):
                _wire(c, jin_x, top_y, jin_x, by)
                if not (par_last and it is top_items[-1]):
                    _wire(c, jout_x, top_y, jout_x, by)
                bwid = _series_width(branch)
                start = jin_x + (bw - bwid)/2
                _wire(c, jin_x, by, start, by)
                bx = start
                for comp in branch:
                    ct, nm, vl, _o = _comp(comp)
                    _check(ct)
                    _draw_centered(c, SYMBOLS[ct], bx+SPAN/2, by, nm, vl)
                    bx += SPAN
                _wire(c, bx, by, jout_x, by)
            if par_last and it is top_items[-1]:
                # the right column: first branch down to the last, then on
                # down to the bottom wire; the junction is the last
                # branch's corner, where three wires now meet
                _wire(c, jout_x, ys[0], jout_x, ys[-1])
                _dot(c, jout_x, ys[-1])
            prev_span = (jin_x, jout_x)
            cx += bw

    end_x = max(cx + 40, left_x + 200) if L.get("title_size") else W - left_x
    if par_last:
        end_x = cx
        _wire(c, end_x, ys[-1], end_x, bot_y)       # down from the junction
    else:
        _wire(c, cx, top_y, end_x, top_y)           # short tail to corner
    if not right and not par_last:
        _wire(c, end_x, top_y, end_x, bot_y)        # down right side
    _wire(c, end_x, bot_y, left_x, bot_y)           # along the bottom
    if not left:
        if gap == "start":
            # up the left side, stopping short: a visible break in the loop
            _wire(c, left_x, bot_y, left_x, top_y + 30)
        else:
            _wire(c, left_x, bot_y, left_x, top_y)  # up the left side
    if not L.get("title_size"):
        c.S = _merge_wires(c.S)
    return c.svg()


def _draw_centered(c, fn, x, y, name, value):
    """Most symbols draw their own leads spanning SPAN. Meters/voltmeter
    differ but are handled in circuit(). Just call through."""
    try:
        fn(c, x, y, name, value)
    except TypeError:
        fn(c, x, y, name)


def symbol_bank():
    """Reference sheet: every circuit symbol with its name beneath it."""
    # ⊕ figlib: the AQA 8463 list, in the spec's order. The library's sheet
    # also carried "d.c. power supply" and "Motor", neither of which is on
    # the AQA list, under a heading that said AQA.
    items = list(AQA_SYMBOLS)
    cols = 4
    rows = (len(items) + cols - 1) // cols
    cell_w, cell_h = 320, 230
    W = cols * cell_w + 60
    H = rows * cell_h + 150
    c = Canvas(W, H)
    c.label(W/2, 60, "Circuit Symbols \u2014 AQA", 40, "bold")
    for i, (key, name) in enumerate(items):
        r, col = divmod(i, cols)
        cx = 30 + col*cell_w + cell_w/2
        cy = 150 + r*cell_h + cell_h/2 - 20
        # draw symbol centred (symbols draw their own leads over SPAN)
        fn = SYMBOLS[key]
        try:
            fn(c, cx, cy, None, None)
        except TypeError:
            fn(c, cx, cy, None)
        _clabel(c, cx, cy + 78, name, 24, LBL)
    return c.svg()


# ---- expanded scenario set ----
def scenario_circuits():
    """Return a dict of name -> svg for a broad spread of series and
    parallel circuits used across AQA P1."""
    s = {}

    s["s1_lamp_series"] = circuit(
        [("cell", None, "6 V"), ("switch",), ("lamp", "L1")],
        title="Series: cell, switch, lamp")

    s["s2_two_lamps_series"] = circuit(
        [("battery", None, "12 V"), ("switch",),
         ("lamp", "L1"), ("lamp", "L2")],
        title="Series: two lamps (dimmer than one)")

    s["s3_resistor_lamp"] = circuit(
        [("cell", None, "1.5 V"), ("resistor", "R1", "4 \u03a9"),
         ("lamp", "L1")],
        title="Series: resistor and lamp")

    s["s4_rheostat_lamp"] = circuit(
        [("cell", None, "6 V"), ("variable_resistor", "Rheostat"),
         ("lamp", "L1")],
        title="Series: variable resistor controls brightness")

    s["s5_ammeter_voltmeter"] = circuit(
        [("cell", None, "6 V"), ("ammeter",),
         ("resistor", "R1", "10 \u03a9"), ("voltmeter",)],
        title="Measuring V and I for a resistor")

    s["s6_diode_series"] = circuit(
        [("cell", None, "3 V"), ("diode", "D1"),
         ("resistor", "R1", "100 \u03a9"), ("lamp", "L1")],
        title="Series: diode (one-way current)")

    s["s7_thermistor"] = circuit(
        [("power", None, "5 V"), ("thermistor", "Th"),
         ("resistor", "R1", "1 k\u03a9"), ("voltmeter",)],
        title="Thermistor potential divider sensor")

    s["s8_ldr"] = circuit(
        [("power", None, "5 V"), ("ldr", "LDR"),
         ("resistor", "R1", "10 k\u03a9"), ("voltmeter",)],
        title="LDR light-sensing circuit")

    s["s9_fuse_motor"] = circuit(
        [("power", None, "230 V"), ("fuse", "F 3 A"),
         ("switch",), ("motor", "M")],
        title="Series: fuse protects a motor")

    s["p1_two_lamps_parallel"] = circuit(
        [("cell", None, "6 V"), ("switch",),
         parallel([[("lamp", "L1")], [("lamp", "L2")]])],
        title="Parallel: two lamps (same brightness)")

    s["p2_three_lamps_parallel"] = circuit(
        [("battery", None, "6 V"),
         parallel([[("lamp", "L1")], [("lamp", "L2")],
                   [("lamp", "L3")]])],
        title="Parallel: three lamps")

    s["p3_resistors_parallel"] = circuit(
        [("cell", None, "6 V"), ("ammeter",),
         parallel([[("resistor", "R1", "10 \u03a9")],
                   [("resistor", "R2", "10 \u03a9")]])],
        title="Parallel resistors (lower total resistance)")

    s["p4_branch_switches"] = circuit(
        [("battery", None, "9 V"),
         parallel([[("switch",), ("lamp", "L1")],
                   [("switch",), ("lamp", "L2")]])],
        title="Parallel: each branch independently switched")

    s["p5_mixed_rseries"] = circuit(
        [("cell", None, "6 V"), ("ammeter",),
         ("resistor", "R1", "10 \u03a9"),
         parallel([[("resistor", "R2", "20 \u03a9")],
                   [("resistor", "R3", "20 \u03a9")]])],
        title="Mixed: R1 in series with R2 \u2225 R3")

    s["p6_mixed_lamp_branch"] = circuit(
        [("battery", None, "12 V"), ("switch",),
         ("lamp", "L1"),
         parallel([[("lamp", "L2")],
                   [("resistor", "R1", "15 \u03a9")]])],
        title="Mixed: lamp in series, lamp \u2225 resistor")

    return s


# ====================================================================
# (demo harness)
# ====================================================================
def _render_all():
    export(symbol_bank(), "symbol_bank", formats=("png",))
    print("symbol_bank")
    for nm, svg in scenario_circuits().items():
        export(svg, nm, formats=("png",))
        print("scenario", nm)


# ====================================================================
# PHASE 2 — SANKEY DIAGRAMS & ENERGY TRANSFER
#   Sankey: input band splits into useful + wasted, widths exactly
#   proportional to the joules. Efficiency framing built in.
# ====================================================================
def sankey(input_label, input_J, outputs, title=None):
    """Proportional Sankey diagram.
    input_J  : total energy in (joules)
    outputs  : list of (label, joules, kind) where kind is
               "useful" or "wasted". Useful continues straight on;
               wasted bands peel downward but still flow rightward.
    """
    total = input_J
    useful = [(l, j) for (l, j, k) in outputs if k == "useful"]
    wasted = [(l, j) for (l, j, k) in outputs if k == "wasted"]
    eff = round(100 * sum(j for _, j in useful) / total) if total else 0

    # canvas grows when there are multiple wasted bands (they stack)
    nW = max(1, len(wasted))
    W = 1320
    H = 720 + (nW - 1) * 200
    c = Canvas(W, H)
    c.label(W/2, 56, title or f"Sankey diagram \u2014 {input_label}",
            34, "bold")

    band_max = 300                       # px height for the full input
    ppj = band_max / total
    in_w = total * ppj

    x_in = 230
    x_split = 620
    x_out = W - 120
    cy = 280
    top = cy - in_w/2

    GREEN = STYLE["nm_fill"]
    AMBER = "#E0892E"

    # ---- input band ----
    c.S.append(
        f'<rect x="{x_in}" y="{top:.1f}" width="{x_split-x_in}" '
        f'height="{in_w:.1f}" fill="{GREEN}" opacity="0.55" '
        f'stroke="{ST}" stroke-width="2"/>')
    _clabel(c, x_in+ (x_split-x_in)/2, top-20, input_label, 23, LBL)
    _clabel(c, x_in+(x_split-x_in)/2, cy+8, f"{input_J} J", 26, LBL)

    # ---- useful: straight band continuing right from the TOP slice ----
    cur = top
    for (lab, j) in useful:
        h = j * ppj
        c.S.append(
            f'<path d="M{x_split} {cur:.1f} L{x_out} {cur:.1f} '
            f'L{x_out} {cur+h:.1f} L{x_split} {cur+h:.1f} Z" '
            f'fill="{GREEN}" opacity="0.7" stroke="{ST}" '
            f'stroke-width="2"/>')
        _clabel(c, (x_split+x_out)/2, cur+h/2-4, lab, 22, LBL)
        _clabel(c, (x_split+x_out)/2, cur+h/2+22, f"{j} J", 22, RED)
        cur += h
    useful_h = cur - top

    # ---- wasted: each peels DOWNWARD then runs rightward as its own
    #      horizontal band at a stepped-down level ----
    w_top = top + useful_h               # wasted slices start below useful
    level = cy + in_w/2 + 70             # first wasted band's top y
    for (lab, j) in wasted:
        h = j * ppj
        # smooth S-curve from the split down to this band's level
        c.S.append(
            f'<path d="M{x_split} {w_top:.1f} '
            f'C {x_split+90} {w_top:.1f} {x_split+30} {level:.1f} '
            f'{x_split+130} {level:.1f} '
            f'L{x_out} {level:.1f} '
            f'L{x_out} {level+h:.1f} '
            f'L{x_split+130} {level+h:.1f} '
            f'C {x_split+30} {level+h:.1f} {x_split+90} '
            f'{w_top+h:.1f} {x_split} {w_top+h:.1f} Z" '
            f'fill="{AMBER}" opacity="0.6" stroke="{ST}" '
            f'stroke-width="2"/>')
        _clabel(c, (x_split+150+x_out)/2, level+h/2-4, lab, 22, LBL)
        _clabel(c, (x_split+150+x_out)/2, level+h/2+22, f"{j} J", 22, RED)
        w_top += h
        level += h + 60                  # stack next wasted band lower

    # ---- efficiency callout (red = copy this) ----
    c.S.append(
        f'<text x="{W/2}" y="{H-78}" font-family="{FONT}" '
        f'font-size="27" fill="{RED}" text-anchor="middle" '
        f'font-weight="bold">Efficiency = useful \u00f7 total '
        f'\u00d7 100 = {sum(j for _,j in useful)} \u00f7 {total} '
        f'\u00d7 100 = {eff}%</text>')
    c.label(W/2, H-40,
             "Total energy in = total energy out "
             "(energy is conserved \u2014 only transferred).",
             22, anchor="middle")
    return c.svg()


def energy_transfer(store_in, device, store_out_useful, store_out_wasted,
                     title=None):
    """Simple energy-store transfer diagram: store -> device -> stores."""
    W, H = 1200, 520
    c = Canvas(W, H)
    c.label(W/2, 58, title or f"Energy transfer \u2014 {device}",
            34, "bold")
    cy = 290

    def box(cx, w, txt, fill, sub=None):
        c.S.append(
            f'<rect x="{cx-w/2}" y="{cy-55}" width="{w}" height="110" '
            f'rx="10" fill="{fill}" opacity="0.5" stroke="{ST}" '
            f'stroke-width="2.5"/>')
        _clabel(c, cx, cy-2, txt, 24, LBL)
        if sub:
            _clabel(c, cx, cy+28, sub, 20, LBL, "normal")

    GREEN = STYLE["nm_fill"]
    box(190, 240, store_in, GREEN, "energy store")
    # device
    c.S.append(
        f'<rect x="{600-90}" y="{cy-55}" width="180" height="110" '
        f'rx="10" fill="{STYLE["h_fill"]}" opacity="0.55" '
        f'stroke="{ST}" stroke-width="2.5"/>')
    _clabel(c, 600, cy+4, device, 24, LBL)
    # arrows in
    c.S.append(
        f'<line x1="310" y1="{cy}" x2="500" y2="{cy}" '
        f'stroke="{ACC}" stroke-width="7" stroke-linecap="round"/>')
    c.S.append(
        f'<polygon points="500,{cy} 478,{cy-12} 478,{cy+12}" '
        f'fill="{ACC}"/>')
    # useful out (straight)
    c.S.append(
        f'<line x1="690" y1="{cy}" x2="930" y2="{cy}" '
        f'stroke="{ACC}" stroke-width="7" stroke-linecap="round"/>')
    c.S.append(
        f'<polygon points="930,{cy} 908,{cy-12} 908,{cy+12}" '
        f'fill="{ACC}"/>')
    box(1050, 230, store_out_useful, GREEN, "useful")
    # wasted out (down)
    c.S.append(
        f'<line x1="600" y1="{cy+55}" x2="600" y2="{cy+150}" '
        f'stroke="#E0892E" stroke-width="7" stroke-linecap="round"/>')
    c.S.append(
        f'<polygon points="600,{cy+150} 588,{cy+128} 612,{cy+128}" '
        f'fill="#E0892E"/>')
    _clabel(c, 600, cy+180, f"wasted: {store_out_wasted}", 22, LBL)
    return c.svg()


def _render_phase2():
    export(sankey("chemical energy in petrol", 100,
                  [("kinetic energy (useful)", 30, "useful"),
                   ("heat to surroundings", 60, "wasted"),
                   ("sound", 10, "wasted")],
                  title="Sankey diagram \u2014 a car engine"),
           "sankey_car", formats=("png",))
    export(sankey("electrical energy in", 100,
                  [("light (useful)", 20, "useful"),
                   ("heat (wasted)", 80, "wasted")],
                  title="Sankey diagram \u2014 a filament lamp"),
           "sankey_filament", formats=("png",))
    export(sankey("electrical energy in", 100,
                  [("light (useful)", 80, "useful"),
                   ("heat (wasted)", 20, "wasted")],
                  title="Sankey diagram \u2014 an LED lamp"),
           "sankey_led", formats=("png",))
    export(energy_transfer("Chemical (battery)", "Electric motor",
                           "Kinetic (lifted load)", "heat & sound",
                           title="Energy transfer \u2014 motor lifting a load"),
           "energy_transfer_motor", formats=("png",))
    for nm in ("sankey_car", "sankey_filament", "sankey_led",
               "energy_transfer_motor"):
        print("phase2", nm)


# ====================================================================
# PHASE 3 — PARTICLE MODEL
#   States of matter (particle arrangement), heating/cooling curve,
#   specific heat capacity / latent heat apparatus.
# ====================================================================
import random as _rnd


def states_of_matter(W=1320, H=720, box_w=360, box_h=320, pr=17,
                     title="The Particle Model — States of Matter",
                     title_size=36, label_size=28, top=150, gap=50,
                     descs=True, desc_size=19, reference=None, seed=1,
                     solid_grid=None, liquid_drop=3, liquid_n=None,
                     gas_n=None, gas_min=4.2):
    """Three boxes: solid (regular, touching), liquid (touching, irregular),
    gas (far apart, random) with the particle-model descriptors.

    ⊕ figlib: parametrised (every default is the library's own value) so a
    question figure can draw the SAME model on a phone-width canvas, and
    `reference=("one particle,", "actual size")` adds a lone particle under
    each box — the same size in all three, which is the point.

    ⊕ figlib correction — the LIQUID. The library scattered liquid particles
    at least 46 units apart centre to centre with radius 17: never touching,
    which is the gas picture at a higher density. A liquid's particles touch
    most of their neighbours and are only slightly further apart on average
    than a solid's; what changes is the ORDER. `_liquid_pack` starts from a
    touching lattice and randomises it without ever pulling particles apart
    by more than a few percent of their size.
    """
    c = Canvas(W, H)
    if title:
        c.label(W/2, 56, title, title_size, "bold")
    ys = top
    x0 = (W - (3*box_w + 2*gap)) / 2
    xs = [x0 + i*(box_w + gap) for i in range(3)]
    titles = ["SOLID", "LIQUID", "GAS"] if descs else ["Solid", "Liquid", "Gas"]

    for bi, (bx, ttl) in enumerate(zip(xs, titles)):
        _clabel(c, bx+box_w/2, ys-14, ttl, label_size, LBL)
        c.S.append(
            f'<rect x="{bx}" y="{ys}" width="{box_w}" height="{box_h}" '
            f'rx="8" fill="none" stroke="{ST}" stroke-width="2.5"/>')
        if bi == 0:                       # solid: regular lattice, touching
            step = 2*pr
            cols = int((box_w - 2*pr) // step) + 1
            rows = int((box_h - 2*pr) // step) + 1
            cols, rows = min(cols, int((box_w - 8) // step)), \
                min(rows, int((box_h - 8) // step))
            if solid_grid:
                cols, rows = solid_grid
            grid_w = (cols-1)*step
            grid_h = (rows-1)*step
            gx = bx + (box_w - grid_w)/2
            gy = ys + box_h - pr - 4 - grid_h
            for r in range(rows):
                for col in range(cols):
                    _particle(c, gx + col*step, gy + r*step, pr)
        elif bi == 1:                     # liquid: touching, irregular
            for (px, py) in _liquid_pack(bx, ys, box_w, box_h, pr, seed,
                                         drop=liquid_drop, n=liquid_n):
                _particle(c, px, py, pr)
        else:                             # gas: sparse, random
            n = gas_n or max(5, int(box_w * box_h / (pr * pr * 40)))
            for (px, py) in _scatter(bx+pr+6, ys+pr+6, box_w-2*pr-12,
                                     box_h-2*pr-12, pr*gas_min, n, seed + 1):
                _particle(c, px, py, pr)
        if reference:
            ry = ys + box_h + pr + 16
            _particle(c, bx+box_w/2, ry, pr)
            yy = ry + pr + desc_size + 6
            for ln in reference:
                _clabel(c, bx+box_w/2, yy, ln, desc_size, LBL, "normal")
                yy += desc_size + 4

    if descs:
        dl_all = [
            ["Fixed positions, regular pattern",
             "Vibrate about fixed points",
             "Strong forces — fixed shape & volume"],
            ["Touching, irregular",
             "Move around each other",
             "Fixed volume, takes container shape"],
            ["Far apart, random",
             "Move quickly in all directions",
             "No fixed shape or volume — fills space"],
        ]
        for bx, dl in zip(xs, dl_all):
            yy = ys + box_h + 36
            for ln in dl:
                _clabel(c, bx+box_w/2, yy, ln, desc_size, LBL, "normal")
                yy += 26
    return c.svg()


def _scatter(x0, y0, w, h, rmin, n, seed):
    """Exactly `n` points, every pair at least `rmin` apart — the first
    seeded attempt that manages it. Raises rather than quietly drawing a
    gas with fewer particles, or closer ones, than asked for."""
    for s in range(400):
        pts = _poisson(x0, y0, w, h, rmin, n, _rnd.Random(seed * 1009 + s))
        if len(pts) == n:
            return pts
    raise ValueError("cannot scatter %d particles %g apart in %gx%g"
                     % (n, rmin, w, h))


def _liquid_pack(bx, by, bw, bh, r, seed=1, fill=0.78, drop=3, touch=2.2,
                 n=None):
    """Touching, disordered particles in the lower part of a box, every
    one of them within `touch`*r (centre to centre) of at least two others
    — i.e. touching, or all but touching, two neighbours. The first seeded
    shake that satisfies that is used; none satisfying it is an error."""
    for s in range(60):
        pts = _liquid_try(bx, by, bw, bh, r, seed * 97 + s, fill, drop, n)
        if all(sum(1 for j, q in enumerate(pts) if j != i and
                   (q[0]-p[0])**2 + (q[1]-p[1])**2 <= (touch*r)**2) >= 2
               for i, p in enumerate(pts)):
            return pts
    raise ValueError("_liquid_pack: no arrangement kept every particle "
                     "touching two neighbours")


def _liquid_try(bx, by, bw, bh, r, seed=1, fill=0.78, drop=3, n=None):
    """One attempt: scatter particles loosely in the box, then let them
    SETTLE — a Monte Carlo walk whose moves may go sideways freely but only
    ever downward, never overlapping. What comes to rest is a random heap
    at the bottom of the box: every particle resting on others, no rows and
    no columns, open space above. That is a liquid in a container.
    `n` defaults to what a touching lattice would put in the lower `fill`
    of the box, less `drop`."""
    rng = _rnd.Random(seed)
    lo_x, hi_x = bx + r + 2, bx + bw - r - 2
    lo_y, hi_y = by + r + 2, by + bh - r - 2
    if n is None:
        per_row = int((hi_x - lo_x) // (2*r)) + 1
        rows = int((bh*fill - 2*r) // (2*r*0.866)) + 1
        n = per_row * rows - drop
    pts = []
    tries = 0
    while len(pts) < n and tries < 20000:
        tries += 1
        q = [rng.uniform(lo_x, hi_x), rng.uniform(lo_y, hi_y)]
        if all((q[0]-o[0])**2 + (q[1]-o[1])**2 >= (2*r)**2 for o in pts):
            pts.append(q)
    for sweep in range(700):
        a = r * max(0.04, 0.9 * (1 - sweep / 700.0))
        for i in range(len(pts)):
            nx = pts[i][0] + rng.uniform(-a, a)
            ny = pts[i][1] + rng.uniform(0, a)          # never upward
            nx = min(max(nx, lo_x), hi_x)
            ny = min(ny, hi_y)
            if all((nx-q[0])**2 + (ny-q[1])**2 >= (2*r)**2
                   for j, q in enumerate(pts) if j != i):
                pts[i] = [nx, ny]
    return [tuple(q) for q in pts]


def _particle(c, x, y, r):
    c.S.append(
        f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" '
        f'fill="{STYLE["nm_fill"]}" stroke="{ST}" stroke-width="2"/>')


def _poisson(x0, y0, w, h, rmin, n, rng=None):
    """Cheap scattered points kept roughly rmin apart. ⊕ figlib: `rng` lets a
    caller pass its own seeded generator instead of the module's shared one,
    so two figures built in one process cannot perturb each other."""
    rng = rng or _rnd
    pts = []
    tries = 0
    while len(pts) < n and tries < n*40:
        px = x0 + rng.uniform(0, w)
        py = y0 + rng.uniform(0, h)
        if all((px-qx)**2+(py-qy)**2 > rmin*rmin for qx, qy in pts):
            pts.append((px, py))
        tries += 1
    return pts


def heating_curve(substance="water"):
    """Temperature vs time heating curve with melting & boiling plateaus."""
    W, H = 1240, 760
    c = Canvas(W, H)
    c.label(W/2, 56, f"Heating curve \u2014 {substance}", 36, "bold")
    ox, oy = 170, 600           # axis origin
    aw, ah = 940, 460
    # axes
    c.S.append(
        f'<line x1="{ox}" y1="{oy}" x2="{ox+aw}" y2="{oy}" '
        f'stroke="{ST}" stroke-width="3"/>')
    c.S.append(
        f'<line x1="{ox}" y1="{oy}" x2="{ox}" y2="{oy-ah}" '
        f'stroke="{ST}" stroke-width="3"/>')
    _clabel(c, ox+aw/2, oy+58, "Time / energy supplied \u2192", 24, LBL)
    c.S.append(
        f'<text x="{ox-110}" y="{oy-ah/2}" font-family="{FONT}" '
        f'font-size="24" fill="{LBL}" text-anchor="middle" '
        f'font-weight="bold" transform="rotate(-90 {ox-110} '
        f'{oy-ah/2})">Temperature / \u00b0C \u2192</text>')
    # curve segments: solid-rise, melt-plateau, liquid-rise,
    # boil-plateau, gas-rise. x fractions and y levels.
    P = [(0.00, 0.10), (0.14, 0.26),     # solid heating
         (0.34, 0.26),                   # melting (flat)
         (0.50, 0.60),                   # liquid heating
         (0.74, 0.60),                   # boiling (flat)
         (0.90, 0.82), (1.00, 0.92)]     # gas heating
    def X(f): return ox + f*aw
    def Y(f): return oy - f*ah
    d = f'M {X(P[0][0])} {Y(P[0][1])} '
    for (fx, fy) in P[1:]:
        d += f'L {X(fx)} {Y(fy)} '
    c.S.append(
        f'<path d="{d}" fill="none" stroke="{ACC}" '
        f'stroke-width="4"/>')
    # plateau labels
    _clabel(c, X(0.24), Y(0.26)-22, "melting point", 20, LBL, "normal")
    _clabel(c, X(0.62), Y(0.60)-22, "boiling point", 20, LBL, "normal")
    # state-band annotations under curve
    bands = [(0.0, 0.14, "solid"), (0.14, 0.34, "solid + liquid"),
             (0.34, 0.50, "liquid"), (0.50, 0.74, "liquid + gas"),
             (0.74, 1.0, "gas")]
    for a, b, lab in bands:
        _clabel(c, X((a+b)/2), oy-14, lab, 18, LBL, "normal")
    # red exam point
    c.S.append(
        f'<text x="{W/2}" y="{H-40}" font-family="{FONT}" '
        f'font-size="24" fill="{RED}" text-anchor="middle" '
        f'font-weight="bold">Flat sections: energy breaks bonds '
        f'(changes state) \u2014 temperature stays constant.</text>')
    return c.svg()


def shc_apparatus():
    """Specific heat capacity: insulated block, heater, thermometer."""
    W, H = 1040, 720
    c = Canvas(W, H)
    c.label(W/2, 56, "Specific Heat Capacity \u2014 apparatus", 34, "bold")
    bx, by, bw, bh = 380, 240, 280, 340
    # insulation
    c.S.append(
        f'<rect x="{bx-26}" y="{by-26}" width="{bw+52}" '
        f'height="{bh+52}" rx="14" fill="{STYLE["h_fill"]}" '
        f'opacity="0.35" stroke="{ST}" stroke-width="2" '
        f'stroke-dasharray="6 6"/>')
    _clabel(c, bx+bw+96, by+bh-20, "insulation", 20, LBL, "normal")
    # metal block
    c.S.append(
        f'<rect x="{bx}" y="{by}" width="{bw}" height="{bh}" rx="6" '
        f'fill="{STYLE["nm_fill"]}" opacity="0.55" stroke="{ST}" '
        f'stroke-width="2.5"/>')
    _clabel(c, bx+bw/2, by+bh-30, "metal block", 22, LBL)
    # heater (immersion) in left hole
    hx = bx+bw*0.34
    c.S.append(
        f'<rect x="{hx-14}" y="{by-90}" width="28" height="{bh*0.55+90}" '
        f'rx="6" fill="none" stroke="{ST}" stroke-width="2.5"/>')
    _clabel(c, hx, by-104, "heater", 20, LBL, "normal")
    # thermometer in right hole
    tx = bx+bw*0.7
    c.S.append(
        f'<line x1="{tx}" y1="{by-110}" x2="{tx}" y2="{by+bh*0.45}" '
        f'stroke="{ST}" stroke-width="4"/>')
    c.S.append(
        f'<circle cx="{tx}" cy="{by+bh*0.45}" r="12" '
        f'fill="{RED}" stroke="{ST}" stroke-width="2"/>')
    _clabel(c, tx+4, by-124, "thermometer", 20, LBL, "normal")
    # power supply wires up from heater
    c.S.append(
        f'<polyline points="{hx},{by-90} {hx},{by-150} {bx-120},'
        f'{by-150}" fill="none" stroke="{ST}" stroke-width="3"/>')
    sym_power(c, bx-200, by-150, None, None)
    _clabel(c, bx-200, by-86, "joulemeter / power", 18, LBL, "normal")
    c.S.append(
        f'<text x="{W/2}" y="{H-40}" font-family="{FONT}" '
        f'font-size="23" fill="{RED}" text-anchor="middle" '
        f'font-weight="bold">E = m c \u0394\u03b8   '
        f'(energy = mass \u00d7 specific heat capacity '
        f'\u00d7 temperature change)</text>')
    return c.svg()


def _render_phase3():
    export(states_of_matter(), "states_of_matter", formats=("png",))
    export(heating_curve("water"), "heating_curve", formats=("png",))
    export(shc_apparatus(), "shc_apparatus", formats=("png",))
    for nm in ("states_of_matter", "heating_curve", "shc_apparatus"):
        print("phase3", nm)


# ====================================================================
# PHASE 4 — ATOMIC STRUCTURE & RADIOACTIVITY
#   Atom diagram (nucleus + shells), isotope notation card, the
#   history-of-the-atom strip (plum pudding -> nuclear -> Bohr),
#   alpha/beta/gamma penetration table, half-life decay curve.
# ====================================================================
def atom_diagram(symbol="Li", protons=3, neutrons=4):
    """Atom with labelled nucleus (protons + neutrons) and electron
    shells filled 2,8,8,2 from the proton count."""
    W, H = 900, 900
    c = Canvas(W, H)
    c.label(W/2, 60, f"The Atom \u2014 {symbol}", 38, "bold")
    cx, cy = W/2, 440
    # determine shell counts (2,8,8,2 rule)
    caps = [2, 8, 8, 2]; left = protons; shells = []
    for cap in caps:
        if left <= 0: break
        shells.append(min(cap, left)); left -= min(cap, left)
    # radii scale with number of shells so the diagram fills space
    radii_table = {
        1: [180],
        2: [120, 240],
        3: [100, 200, 300],
        4: [90, 175, 260, 340],
    }
    radii = radii_table[len(shells)]
    for r in radii:
        c.S.append(
            f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" '
            f'stroke="{ST}" stroke-width="2"/>')
    # electrons in pairs around each shell
    for si, count in enumerate(shells):
        r = radii[si]
        n_pairs = (count + 1) // 2
        for p in range(n_pairs):
            base = -90 + p * (360 / n_pairs)
            inpr = 2 if (p*2 + 2) <= count else 1
            if inpr == 2:
                for off in (-7, 7):
                    ang = base + off
                    px = cx + r*math.cos(math.radians(ang))
                    py = cy + r*math.sin(math.radians(ang))
                    c.S.append(
                        f'<circle cx="{px:.1f}" cy="{py:.1f}" r="9" '
                        f'fill="{ST}"/>')
            else:
                ang = base
                px = cx + r*math.cos(math.radians(ang))
                py = cy + r*math.sin(math.radians(ang))
                c.S.append(
                    f'<circle cx="{px:.1f}" cy="{py:.1f}" r="9" '
                    f'fill="{ST}"/>')
    # nucleus with proton/neutron counts (larger to match scaled atom)
    nr = 72
    c.S.append(
        f'<circle cx="{cx}" cy="{cy}" r="{nr}" fill="{STYLE["h_fill"]}" '
        f'stroke="{ST}" stroke-width="2.5"/>')
    _clabel(c, cx, cy-10, f"{protons} p", 28, LBL)
    _clabel(c, cx, cy+28, f"{neutrons} n", 28, LBL)
    # legend along the bottom, well below the atom
    ly = H - 60
    c.S.append(
        f'<circle cx="160" cy="{ly}" r="13" fill="{STYLE["h_fill"]}" '
        f'stroke="{ST}" stroke-width="1.5"/>')
    _clabel(c, 350, ly+8, "nucleus (protons + neutrons)", 22,
            LBL, "normal")
    c.S.append(f'<circle cx="620" cy="{ly}" r="9" fill="{ST}"/>')
    _clabel(c, 720, ly+8, "electron", 22, LBL, "normal")
    return c.svg()


def isotope_notation(symbol="C", mass=14, atomic=6, name="Carbon-14"):
    """Big AZX notation card with labelled parts."""
    W, H = 1100, 600
    c = Canvas(W, H)
    c.label(W/2, 58, f"Isotope notation \u2014 {name}", 34, "bold")
    cx, cy = W/2 - 60, 330
    # big symbol + mass/atomic numbers
    c.S.append(
        f'<text x="{cx}" y="{cy+34}" font-family="{FONT}" '
        f'font-size="180" fill="{LBL}" text-anchor="middle" '
        f'font-weight="bold">{symbol}</text>')
    c.S.append(
        f'<text x="{cx-120}" y="{cy-50}" font-family="{FONT}" '
        f'font-size="70" fill="{RED}" text-anchor="middle" '
        f'font-weight="bold">{mass}</text>')
    c.S.append(
        f'<text x="{cx-120}" y="{cy+50}" font-family="{FONT}" '
        f'font-size="70" fill="{RED}" text-anchor="middle" '
        f'font-weight="bold">{atomic}</text>')
    # explanatory leaders
    bx = cx + 200
    by1, by2 = cy-50, cy+50
    c.S.append(
        f'<line x1="{cx-70}" y1="{by1}" x2="{bx-20}" y2="{by1}" '
        f'stroke="{ST}" stroke-width="2"/>')
    c.S.append(
        f'<line x1="{cx-70}" y1="{by2}" x2="{bx-20}" y2="{by2}" '
        f'stroke="{ST}" stroke-width="2"/>')
    _clabel(c, bx+170, by1-4, "mass number", 24, LBL)
    _clabel(c, bx+170, by1+22, "(protons + neutrons)", 20, LBL, "normal")
    _clabel(c, bx+170, by2-4, "atomic number", 24, LBL)
    _clabel(c, bx+170, by2+22, "(number of protons)", 20, LBL, "normal")
    # red exam point
    neutrons = mass - atomic
    c.S.append(
        f'<text x="{W/2}" y="{H-40}" font-family="{FONT}" '
        f'font-size="24" fill="{RED}" text-anchor="middle" '
        f'font-weight="bold">Neutrons = mass \u2212 atomic = '
        f'{mass} \u2212 {atomic} = {neutrons}</text>')
    return c.svg()


def history_of_atom():
    """Three-panel strip: plum pudding -> nuclear (Rutherford) -> Bohr."""
    W, H = 1380, 700
    c = Canvas(W, H)
    c.label(W/2, 58, "History of the Atom", 36, "bold")
    pw = 420; py = 150; ph = 320
    xs = [40, 480, 920]
    titles = ["Plum Pudding (Thomson)",
              "Nuclear (Rutherford)",
              "Bohr"]
    for x, ttl in zip(xs, titles):
        c.S.append(
            f'<rect x="{x}" y="{py}" width="{pw}" height="{ph}" '
            f'rx="10" fill="none" stroke="{ST}" stroke-width="2.5"/>')
        _clabel(c, x+pw/2, py-16, ttl, 24, LBL)

    # plum pudding: big positive sphere with embedded electrons
    pcx = xs[0] + pw/2; pcy = py + ph/2
    c.S.append(
        f'<circle cx="{pcx}" cy="{pcy}" r="120" '
        f'fill="{STYLE["h_fill"]}" opacity="0.6" stroke="{ST}" '
        f'stroke-width="2"/>')
    _rnd.seed(7)
    for _ in range(9):
        ex = pcx + _rnd.uniform(-90, 90)
        ey = pcy + _rnd.uniform(-90, 90)
        c.S.append(f'<circle cx="{ex:.0f}" cy="{ey:.0f}" r="8" fill="{ST}"/>')
    _clabel(c, pcx, pcy+150,
            "Positive 'dough' with electrons embedded", 18,
            LBL, "normal")

    # Rutherford: tiny dense nucleus, electrons orbiting at distance
    rcx = xs[1] + pw/2; rcy = py + ph/2
    for r in (60, 110):
        c.S.append(
            f'<circle cx="{rcx}" cy="{rcy}" r="{r}" fill="none" '
            f'stroke="{ST}" stroke-width="1.5" '
            f'stroke-dasharray="4 6"/>')
    c.S.append(
        f'<circle cx="{rcx}" cy="{rcy}" r="14" fill="{STYLE["h_fill"]}" '
        f'stroke="{ST}" stroke-width="2"/>')
    for ang in (30, 150, 270):
        ex = rcx + 60*math.cos(math.radians(ang))
        ey = rcy + 60*math.sin(math.radians(ang))
        c.S.append(f'<circle cx="{ex:.0f}" cy="{ey:.0f}" r="7" fill="{ST}"/>')
    for ang in (90, 210, 330):
        ex = rcx + 110*math.cos(math.radians(ang))
        ey = rcy + 110*math.sin(math.radians(ang))
        c.S.append(f'<circle cx="{ex:.0f}" cy="{ey:.0f}" r="7" fill="{ST}"/>')
    _clabel(c, rcx, rcy+150,
            "Tiny dense positive nucleus; electrons orbit",
            18, LBL, "normal")

    # Bohr: same nucleus + shells in fixed orbits with electrons in pairs
    bcx = xs[2] + pw/2; bcy = py + ph/2
    for r in (50, 95, 140):
        c.S.append(
            f'<circle cx="{bcx}" cy="{bcy}" r="{r}" fill="none" '
            f'stroke="{ST}" stroke-width="2"/>')
    c.S.append(
        f'<circle cx="{bcx}" cy="{bcy}" r="16" fill="{STYLE["h_fill"]}" '
        f'stroke="{ST}" stroke-width="2"/>')
    # 2 e on inner, 8 on next, 2 on outer (mock)
    for cnt, rad in ((2, 50), (8, 95), (2, 140)):
        for i in range(cnt):
            ang = -90 + i*360/cnt
            ex = bcx + rad*math.cos(math.radians(ang))
            ey = bcy + rad*math.sin(math.radians(ang))
            c.S.append(f'<circle cx="{ex:.0f}" cy="{ey:.0f}" r="6" '
                       f'fill="{ST}"/>')
    _clabel(c, bcx, bcy+165,
            "Electrons in fixed shells at set energies",
            18, LBL, "normal")

    # red exam line
    c.S.append(
        f'<text x="{W/2}" y="{H-40}" font-family="{FONT}" '
        f'font-size="23" fill="{RED}" text-anchor="middle" '
        f'font-weight="bold">Alpha-scattering showed atoms are mostly '
        f'empty space with a tiny, dense, positive nucleus.</text>')
    return c.svg()


def radiation_penetration():
    """Alpha, beta, gamma penetration through paper/aluminium/lead."""
    W, H = 1280, 660
    c = Canvas(W, H)
    c.label(W/2, 56, "Penetration of Alpha, Beta and Gamma Radiation",
            34, "bold")
    # three barriers: paper, aluminium, lead
    sx = 280
    barriers = [(sx,        "paper",      "#FBBF24"),
                (sx + 320,  "aluminium",  STYLE["bracket"]),
                (sx + 640,  "lead",       STYLE["muted"])]
    for bx, lab, col in barriers:
        c.S.append(
            f'<rect x="{bx}" y="180" width="40" height="320" '
            f'fill="{col}" opacity="0.7" stroke="{ST}" stroke-width="2"/>')
        _clabel(c, bx+20, 520, lab, 22, LBL)
    # source label on the left
    _clabel(c, 130, 200, "source", 22, LBL)
    c.S.append(
        f'<circle cx="130" cy="240" r="22" fill="{STYLE["h_fill"]}" '
        f'stroke="{ST}" stroke-width="2"/>')
    # three rays fan out from the source toward each barrier
    rays = [
        ("alpha (\u03b1)", 240, sx,         "#C8102E"),
        ("beta (\u03b2)",  340, sx + 320,   "#2E5E45"),
        ("gamma (\u03b3)", 440, sx + 640,   "#3B82F6"),
    ]
    for name, ry, stop_x, col in rays:
        c.S.append(
            f'<line x1="155" y1="240" x2="{stop_x}" y2="{ry}" '
            f'stroke="{col}" stroke-width="5" stroke-linecap="round"/>')
        # arrowhead aligned with the ray's direction
        dx, dy = stop_x - 155, ry - 240
        d = math.hypot(dx, dy); ux, uy = dx/d, dy/d
        px, py = -uy, ux
        tx, ty = stop_x, ry
        c.S.append(
            f'<polygon points="{tx},{ty} '
            f'{tx-18*ux+9*px},{ty-18*uy+9*py} '
            f'{tx-18*ux-9*px},{ty-18*uy-9*py}" fill="{col}"/>')
        # ray label sits a little above where it ends
        _clabel(c, stop_x - 60, ry - 16, name, 22, col, "bold")

    # red exam summary
    c.S.append(
        f'<text x="{W/2}" y="{H-40}" font-family="{FONT}" '
        f'font-size="23" fill="{RED}" text-anchor="middle" '
        f'font-weight="bold">\u03b1 stopped by paper. '
        f'\u03b2 stopped by a few mm of aluminium. '
        f'\u03b3 reduced by thick lead.</text>')
    return c.svg()


def half_life_curve(half_life_min=10, initial=800):
    """Exponential decay curve with half-life ticks."""
    W, H = 1240, 740
    c = Canvas(W, H)
    c.label(W/2, 56, f"Radioactive Decay \u2014 half-life = "
                     f"{half_life_min} minutes", 34, "bold")
    ox, oy = 170, 580
    aw, ah = 960, 440
    c.S.append(
        f'<line x1="{ox}" y1="{oy}" x2="{ox+aw}" y2="{oy}" '
        f'stroke="{ST}" stroke-width="3"/>')
    c.S.append(
        f'<line x1="{ox}" y1="{oy}" x2="{ox}" y2="{oy-ah}" '
        f'stroke="{ST}" stroke-width="3"/>')
    _clabel(c, ox+aw/2, oy+60, "Time / minutes \u2192", 24, LBL)
    c.S.append(
        f'<text x="{ox-110}" y="{oy-ah/2}" font-family="{FONT}" '
        f'font-size="24" fill="{LBL}" text-anchor="middle" '
        f'font-weight="bold" transform="rotate(-90 {ox-110} '
        f'{oy-ah/2})">Count rate / Bq \u2192</text>')

    # exponential curve sampled
    n_steps = 6
    total_T = half_life_min * n_steps
    pts = []
    for i in range(81):
        t = (i / 80) * total_T
        cr = initial * (0.5 ** (t / half_life_min))
        x = ox + (t / total_T) * aw
        y = oy - (cr / initial) * (ah - 30)
        pts.append((x, y))
    d = "M " + " L ".join(f"{x:.1f} {y:.1f}" for x, y in pts)
    c.S.append(
        f'<path d="{d}" fill="none" stroke="{ACC}" stroke-width="4"/>')

    # half-life markers (vertical dashes at t = T, 2T, 3T)
    for k in (1, 2, 3):
        t = k * half_life_min
        cr = initial * (0.5 ** k)
        x = ox + (t / total_T) * aw
        y = oy - (cr / initial) * (ah - 30)
        c.S.append(
            f'<line x1="{x}" y1="{oy}" x2="{x}" y2="{y}" '
            f'stroke="{ST}" stroke-width="2" stroke-dasharray="4 6"/>')
        c.S.append(
            f'<line x1="{ox}" y1="{y}" x2="{x}" y2="{y}" '
            f'stroke="{ST}" stroke-width="2" stroke-dasharray="4 6"/>')
        _clabel(c, x, oy+24, f"{k}T", 20, LBL)
        _clabel(c, ox-30, y+6, f"{int(cr)}", 18, RED)
    _clabel(c, ox-30, oy-ah+10, f"{initial}", 18, RED)

    c.S.append(
        f'<text x="{W/2}" y="{H-40}" font-family="{FONT}" '
        f'font-size="23" fill="{RED}" text-anchor="middle" '
        f'font-weight="bold">Half-life = time taken for the count rate '
        f'(or number of nuclei) to halve.</text>')
    return c.svg()


def _render_phase4():
    export(atom_diagram("Li", 3, 4), "atom_lithium", formats=("png",))
    export(isotope_notation("C", 14, 6, "Carbon-14"),
           "isotope_carbon14", formats=("png",))
    export(history_of_atom(), "history_of_atom", formats=("png",))
    export(radiation_penetration(), "radiation_penetration",
           formats=("png",))
    export(half_life_curve(10, 800), "half_life_curve", formats=("png",))
    for nm in ("atom_lithium", "isotope_carbon14", "history_of_atom",
               "radiation_penetration", "half_life_curve"):
        print("phase4", nm)


# ====================================================================
# PHYSICS P2 — MODULE 1: FORCES
# ====================================================================
def _force_arrow(c, x1, y1, x2, y2, col, label=None, label_offset=(0, -14)):
    c.S.append(
        f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" '
        f'stroke="{col}" stroke-width="6" stroke-linecap="round"/>')
    ang = math.atan2(y2-y1, x2-x1)
    ax = x2 - 22*math.cos(ang); ay = y2 - 22*math.sin(ang)
    nx, ny = -math.sin(ang)*13, math.cos(ang)*13
    c.S.append(
        f'<polygon points="{x2},{y2} {ax+nx:.1f},{ay+ny:.1f} '
        f'{ax-nx:.1f},{ay-ny:.1f}" fill="{col}"/>')
    if label:
        midx, midy = (x1+x2)/2, (y1+y2)/2
        c.S.append(
            f'<text x="{midx + label_offset[0]:.1f}" '
            f'y="{midy + label_offset[1]:.1f}" '
            f'font-family="{FONT}" font-size="22" fill="{col}" '
            f'text-anchor="middle" font-weight="bold">{label}</text>')


def resultant_force():
    """Single object with two horizontal forces and the resultant."""
    W, H = 1240, 640
    c = Canvas(W, H)
    c.label(W/2, 56, "Resultant force", 36, "bold")
    cx, cy = W/2, 340
    # the object
    c.S.append(
        f'<rect x="{cx-70}" y="{cy-50}" width="140" height="100" rx="10" '
        f'fill="{STYLE["nm_fill"]}" opacity="0.6" stroke="{ST}" '
        f'stroke-width="3"/>')
    _clabel(c, cx, cy+8, "10 kg", 24, LBL)
    # left force 30 N pulling left
    _force_arrow(c, cx-70, cy, cx-360, cy, "#C8102E", "30 N (left)",
                 (0, -22))
    # right force 50 N pulling right
    _force_arrow(c, cx+70, cy, cx+430, cy, "#2E5E45", "50 N (right)",
                 (0, -22))
    # resultant
    _clabel(c, W/2, H-100, "Resultant = 50 \u2212 30 = 20 N to the right",
            28, RED, "bold")
    _clabel(c, W/2, H-50,
            "Resultant force = single force that has the same effect "
            "as all the forces combined.", 21, LBL, "normal")
    return c.svg()


def free_body_diagram():
    """Box on a surface with weight, normal reaction, thrust, friction."""
    W, H = 1100, 720
    c = Canvas(W, H)
    c.label(W/2, 56, "Free-body diagram", 36, "bold")
    cx, cy = W/2, 380
    # ground line
    c.S.append(
        f'<line x1="80" y1="{cy+80}" x2="{W-80}" y2="{cy+80}" '
        f'stroke="{ST}" stroke-width="4"/>')
    # ground hatching
    for x in range(120, W-100, 38):
        c.S.append(
            f'<line x1="{x}" y1="{cy+80}" x2="{x-18}" y2="{cy+108}" '
            f'stroke="{ST}" stroke-width="2"/>')
    # the object
    c.S.append(
        f'<rect x="{cx-80}" y="{cy-30}" width="160" height="110" rx="8" '
        f'fill="{STYLE["nm_fill"]}" opacity="0.6" stroke="{ST}" '
        f'stroke-width="3"/>')
    _clabel(c, cx, cy+30, "object", 22, LBL)
    # weight (down)
    _force_arrow(c, cx, cy+30, cx, cy+200, "#C8102E", "weight (W)",
                 (60, 0))
    # normal reaction (up)
    _force_arrow(c, cx, cy+30, cx, cy-150, "#2E5E45", "normal (N)",
                 (60, 0))
    # thrust right
    _force_arrow(c, cx+80, cy+25, cx+330, cy+25, "#3B82F6",
                 "thrust (T)", (0, -22))
    # friction left
    _force_arrow(c, cx-80, cy+25, cx-330, cy+25, "#E0892E",
                 "friction (F)", (0, -22))
    _clabel(c, W/2, H-50,
            "If forces balance \u2192 object at rest or constant velocity. "
            "If they don't \u2192 acceleration.", 21, LBL, "normal")
    return c.svg()


def hookes_law_graph():
    """Force vs extension for a spring, linear with limit of proportionality."""
    W, H = 1200, 700
    c = Canvas(W, H)
    c.label(W/2, 56, "Hooke's law \u2014 force vs extension", 36, "bold")
    ox, oy = 170, 560
    aw, ah = 880, 420
    c.S.append(
        f'<line x1="{ox}" y1="{oy}" x2="{ox+aw}" y2="{oy}" '
        f'stroke="{ST}" stroke-width="3"/>')
    c.S.append(
        f'<line x1="{ox}" y1="{oy}" x2="{ox}" y2="{oy-ah}" '
        f'stroke="{ST}" stroke-width="3"/>')
    _clabel(c, ox+aw/2, oy+58, "Extension, e (m) \u2192", 24, LBL)
    c.S.append(
        f'<text x="{ox-110}" y="{oy-ah/2}" font-family="{FONT}" '
        f'font-size="24" fill="{LBL}" text-anchor="middle" '
        f'font-weight="bold" transform="rotate(-90 {ox-110} '
        f'{oy-ah/2})">Force, F (N) \u2192</text>')
    # linear portion (0 to 60% of axis)
    x_lin_end = ox + 0.60 * aw
    y_lin_end = oy - 0.65 * ah
    c.S.append(
        f'<line x1="{ox}" y1="{oy}" x2="{x_lin_end}" y2="{y_lin_end}" '
        f'stroke="{ACC}" stroke-width="4"/>')
    # curve (limit of proportionality onward) — gentle curve flattening
    c.S.append(
        f'<path d="M {x_lin_end} {y_lin_end} '
        f'Q {ox+0.78*aw} {oy-0.78*ah} {ox+aw-20} {oy-0.85*ah}" '
        f'fill="none" stroke="{ACC}" stroke-width="4"/>')
    # mark limit of proportionality
    c.S.append(
        f'<circle cx="{x_lin_end}" cy="{y_lin_end}" r="10" '
        f'fill="#C8102E" stroke="{ST}" stroke-width="2"/>')
    c.S.append(
        f'<line x1="{x_lin_end}" y1="{y_lin_end}" x2="{x_lin_end+90}" '
        f'y2="{y_lin_end-50}" stroke="{ST}" stroke-width="2"/>')
    _clabel(c, x_lin_end+150, y_lin_end-58,
            "limit of proportionality", 20, RED, "bold")
    _clabel(c, W/2, H-40,
            "F = k e  (force = spring constant \u00d7 extension) \u2014 "
            "only while the spring obeys Hooke's law.",
            22, RED, "bold")
    return c.svg()


def motion_graphs():
    """Two side-by-side panels: distance-time and velocity-time, each
    with three labelled segments."""
    W, H = 1380, 720
    c = Canvas(W, H)
    c.label(W/2, 56, "Motion graphs", 36, "bold")

    def draw_axes(ox, oy, aw, ah, xlab, ylab):
        c.S.append(
            f'<line x1="{ox}" y1="{oy}" x2="{ox+aw}" y2="{oy}" '
            f'stroke="{ST}" stroke-width="3"/>')
        c.S.append(
            f'<line x1="{ox}" y1="{oy}" x2="{ox}" y2="{oy-ah}" '
            f'stroke="{ST}" stroke-width="3"/>')
        _clabel(c, ox+aw/2, oy+44, xlab, 22, LBL)
        c.S.append(
            f'<text x="{ox-44}" y="{oy-ah/2}" font-family="{FONT}" '
            f'font-size="22" fill="{LBL}" text-anchor="middle" '
            f'font-weight="bold" transform="rotate(-90 {ox-44} '
            f'{oy-ah/2})">{ylab}</text>')

    # Distance-time (left): rising line, flat, rising steeper
    ox1, oy1 = 130, 560; aw1 = 520; ah1 = 380
    draw_axes(ox1, oy1, aw1, ah1, "Time \u2192", "Distance \u2192")
    pts1 = [(0,0),(0.25,0.30),(0.55,0.30),(0.85,0.70)]
    d1 = "M " + " L ".join(f"{ox1+x*aw1} {oy1-y*ah1}" for x,y in pts1)
    c.S.append(f'<path d="{d1}" fill="none" stroke="{ACC}" stroke-width="4"/>')
    _clabel(c, ox1+0.13*aw1, oy1-0.20*ah1, "constant speed", 18, LBL)
    _clabel(c, ox1+0.40*aw1, oy1-0.40*ah1, "stationary", 18, LBL)
    _clabel(c, ox1+0.70*aw1, oy1-0.55*ah1, "faster", 18, LBL)
    _clabel(c, ox1+aw1/2, 100, "Distance-time graph", 24, LBL, "bold")

    # Velocity-time (right): rising line (acceleration), flat (constant
    # velocity), falling (deceleration)
    ox2, oy2 = ox1+aw1+200, 560; aw2 = 480; ah2 = 380
    draw_axes(ox2, oy2, aw2, ah2, "Time \u2192", "Velocity \u2192")
    pts2 = [(0,0),(0.30,0.60),(0.60,0.60),(0.95,0.05)]
    d2 = "M " + " L ".join(f"{ox2+x*aw2} {oy2-y*ah2}" for x,y in pts2)
    c.S.append(f'<path d="{d2}" fill="none" stroke="{ACC}" stroke-width="4"/>')
    _clabel(c, ox2+0.16*aw2, oy2-0.30*ah2, "accelerating", 18, LBL)
    _clabel(c, ox2+0.45*aw2, oy2-0.68*ah2, "constant velocity", 18, LBL)
    _clabel(c, ox2+0.78*aw2, oy2-0.35*ah2, "decelerating", 18, LBL)
    _clabel(c, ox2+aw2/2, 100, "Velocity-time graph", 24, LBL, "bold")

    _clabel(c, W/2, H-30,
            "Distance-time: gradient = speed. "
            "Velocity-time: gradient = acceleration; area under = distance.",
            22, RED, "bold")
    return c.svg()


def moments():
    """Pivot with two forces at different distances; principle of moments."""
    W, H = 1240, 640
    c = Canvas(W, H)
    c.label(W/2, 56, "Moments \u2014 principle of balance", 36, "bold")
    cx, cy = W/2, 360
    # beam
    c.S.append(
        f'<rect x="{cx-440}" y="{cy-12}" width="880" height="24" '
        f'fill="{STYLE["nm_fill"]}" opacity="0.6" stroke="{ST}" '
        f'stroke-width="2.5"/>')
    # pivot (triangle below the centre)
    c.S.append(
        f'<polygon points="{cx},{cy+12} {cx-30},{cy+80} {cx+30},{cy+80}" '
        f'fill="{ST}"/>')
    _clabel(c, cx, cy+108, "pivot", 20, LBL, "normal")
    # left force 40 N at 0.5 m
    lx = cx - 320
    _force_arrow(c, lx, cy-12, lx, cy-150, "#C8102E", "40 N", (-26, 0))
    _clabel(c, lx, cy+40, "0.5 m", 18, LBL, "normal")
    # right force 20 N at 1.0 m
    rx = cx + 320
    _force_arrow(c, rx, cy-12, rx, cy-150, "#2E5E45", "20 N", (28, 0))
    _clabel(c, rx, cy+40, "1.0 m", 18, LBL, "normal")
    # distance bars
    for x, lbl in ((lx, ""), (rx, "")):
        c.S.append(
            f'<line x1="{x}" y1="{cy+30}" x2="{cx}" y2="{cy+30}" '
            f'stroke="{ST}" stroke-width="2" stroke-dasharray="4 5"/>')
    # principle written out in red
    _clabel(c, W/2, H-110,
            "Moment = force \u00d7 perpendicular distance from pivot",
            24, LBL, "bold")
    _clabel(c, W/2, H-72,
            "Balanced: 40 \u00d7 0.5 = 20 \u00d7 1.0  \u2192  20 N\u00b7m "
            "(anticlockwise) = 20 N\u00b7m (clockwise)",
            22, RED, "bold")
    return c.svg()


def _render_p2_forces():
    export(resultant_force(), "p2_resultant_force", formats=("png",))
    export(free_body_diagram(), "p2_free_body", formats=("png",))
    export(hookes_law_graph(), "p2_hookes_law", formats=("png",))
    export(motion_graphs(), "p2_motion_graphs", formats=("png",))
    export(moments(), "p2_moments", formats=("png",))
    for nm in ("p2_resultant_force", "p2_free_body", "p2_hookes_law",
               "p2_motion_graphs", "p2_moments"):
        print("p2 forces", nm)


# ====================================================================
# PHYSICS P2 — MODULE 2: WAVES
# ====================================================================
def transverse_wave():
    """Sine wave with wavelength + amplitude labelled."""
    W, H = 1200, 620
    c = Canvas(W, H)
    c.label(W/2, 56, "Transverse wave", 36, "bold")
    cx_axis_y = 330
    ox, oxend = 130, W-130
    amp = 110
    cycles = 2
    L = oxend - ox
    pts = []
    for i in range(241):
        t = i/240
        x = ox + t*L
        y = cx_axis_y - amp*math.sin(t*cycles*2*math.pi)
        pts.append((x, y))
    d = "M " + " L ".join(f"{x:.1f} {y:.1f}" for x, y in pts)
    c.S.append(f'<path d="{d}" fill="none" stroke="{ACC}" stroke-width="4"/>')
    # axis
    c.S.append(
        f'<line x1="{ox}" y1="{cx_axis_y}" x2="{oxend}" y2="{cx_axis_y}" '
        f'stroke="{ST}" stroke-width="2" stroke-dasharray="6 6"/>')
    # wavelength bracket (one full cycle)
    wlx1 = ox + L*0.25/cycles
    wlx2 = ox + L*1.25/cycles
    for x in (wlx1, wlx2):
        c.S.append(
            f'<line x1="{x}" y1="{cx_axis_y-amp-30}" x2="{x}" '
            f'y2="{cx_axis_y-amp-60}" stroke="{ST}" stroke-width="2"/>')
    c.S.append(
        f'<line x1="{wlx1}" y1="{cx_axis_y-amp-45}" x2="{wlx2}" '
        f'y2="{cx_axis_y-amp-45}" stroke="{ST}" stroke-width="2"/>')
    _clabel(c, (wlx1+wlx2)/2, cx_axis_y-amp-60,
            "wavelength, \u03bb", 22, LBL, "bold")
    # amplitude bracket
    ax_amp = oxend - 70
    c.S.append(
        f'<line x1="{ax_amp}" y1="{cx_axis_y}" x2="{ax_amp}" '
        f'y2="{cx_axis_y-amp}" stroke="{ST}" stroke-width="2"/>')
    c.S.append(
        f'<polygon points="{ax_amp},{cx_axis_y-amp} {ax_amp-7},'
        f'{cx_axis_y-amp+12} {ax_amp+7},{cx_axis_y-amp+12}" fill="{ST}"/>')
    c.S.append(
        f'<polygon points="{ax_amp},{cx_axis_y} {ax_amp-7},'
        f'{cx_axis_y-12} {ax_amp+7},{cx_axis_y-12}" fill="{ST}"/>')
    _clabel(c, ax_amp+50, cx_axis_y-amp/2, "amplitude", 20, LBL, "bold")
    # crest & trough
    crest_x = ox + L*0.25/cycles
    trough_x = ox + L*0.75/cycles
    _clabel(c, crest_x, cx_axis_y-amp-12, "crest", 18, LBL)
    _clabel(c, trough_x, cx_axis_y+amp+24, "trough", 18, LBL)
    _clabel(c, W/2, H-40,
            "Transverse: particles vibrate at 90\u00b0 to wave direction. "
            "v = f \u03bb", 22, RED, "bold")
    return c.svg()


def longitudinal_wave():
    """Compressions and rarefactions along a horizontal axis."""
    W, H = 1200, 540
    c = Canvas(W, H)
    c.label(W/2, 56, "Longitudinal wave", 36, "bold")
    cy = 290
    ox, oxend = 130, W-130
    L = oxend - ox
    # Particles with sine-modulated positions: 2 cycles of compression/rarefaction
    for i in range(120):
        t = i/120
        x = ox + (t + 0.08*math.sin(t*2*math.pi*2))*L
        c.S.append(
            f'<circle cx="{x:.1f}" cy="{cy}" r="6" fill="{ST}"/>')
    # compressions (dense regions)
    comp_xs = [ox + L*0.25, ox + L*0.75]
    for x in comp_xs:
        c.S.append(
            f'<line x1="{x}" y1="{cy-60}" x2="{x}" y2="{cy-30}" '
            f'stroke="#C8102E" stroke-width="2"/>')
        _clabel(c, x, cy-74, "compression", 18, "#C8102E", "bold")
    # rarefactions (sparse regions)
    rar_xs = [ox + L*0.5]
    for x in rar_xs:
        c.S.append(
            f'<line x1="{x}" y1="{cy+30}" x2="{x}" y2="{cy+60}" '
            f'stroke="#3B82F6" stroke-width="2"/>')
        _clabel(c, x, cy+82, "rarefaction", 18, "#3B82F6", "bold")
    # wave direction arrow
    c.S.append(
        f'<line x1="{ox}" y1="{cy+130}" x2="{oxend-30}" y2="{cy+130}" '
        f'stroke="{ACC}" stroke-width="4"/>')
    c.S.append(
        f'<polygon points="{oxend-30},{cy+130} {oxend-50},{cy+120} '
        f'{oxend-50},{cy+140}" fill="{ACC}"/>')
    _clabel(c, W/2, cy+158, "wave direction", 18, LBL)
    _clabel(c, W/2, H-30,
            "Longitudinal: particles vibrate parallel to the wave "
            "direction (e.g. sound).", 22, RED, "bold")
    return c.svg()


def reflection_ray():
    """Incident ray, normal (dashed), reflected ray on a mirror."""
    W, H = 1100, 700
    c = Canvas(W, H)
    c.label(W/2, 56, "Reflection of light", 36, "bold")
    # mirror (horizontal at bottom)
    mx1, mx2 = 150, W-150
    my = 480
    c.S.append(
        f'<line x1="{mx1}" y1="{my}" x2="{mx2}" y2="{my}" '
        f'stroke="{ST}" stroke-width="4"/>')
    for x in range(mx1+18, mx2, 30):
        c.S.append(
            f'<line x1="{x}" y1="{my}" x2="{x-14}" y2="{my+22}" '
            f'stroke="{ST}" stroke-width="2"/>')
    _clabel(c, mx2-50, my+50, "mirror", 20, LBL)
    # contact point
    cpx, cpy = W/2, my
    # normal (dashed vertical)
    c.S.append(
        f'<line x1="{cpx}" y1="{my-330}" x2="{cpx}" y2="{my+10}" '
        f'stroke="{ST}" stroke-width="2" stroke-dasharray="6 6"/>')
    _clabel(c, cpx+50, my-310, "normal", 18, LBL, "normal")
    # incident ray
    in_x = cpx - 300; in_y = my - 300
    _force_arrow(c, in_x, in_y, cpx-10, cpy-12, "#C8102E", None)
    _clabel(c, in_x+50, in_y-12, "incident ray", 20, "#C8102E", "bold")
    # reflected ray
    rf_x = cpx + 300; rf_y = my - 300
    _force_arrow(c, cpx+10, cpy-12, rf_x, rf_y, "#2E5E45", None)
    _clabel(c, rf_x-60, rf_y-12, "reflected ray", 20, "#2E5E45", "bold")
    # angle arcs
    c.S.append(
        f'<path d="M {cpx-70} {cpy} A 70 70 0 0 1 {cpx-50} {cpy-50}" '
        f'fill="none" stroke="{ST}" stroke-width="2"/>')
    _clabel(c, cpx-90, cpy-40, "i", 22, LBL, "bold")
    c.S.append(
        f'<path d="M {cpx+50} {cpy-50} A 70 70 0 0 1 {cpx+70} {cpy}" '
        f'fill="none" stroke="{ST}" stroke-width="2"/>')
    _clabel(c, cpx+90, cpy-40, "r", 22, LBL, "bold")
    _clabel(c, W/2, H-40,
            "Law of reflection: angle of incidence = angle of reflection "
            "(both measured from the normal).", 21, RED, "bold")
    return c.svg()


def refraction_ray():
    """Light bending as it enters a denser medium."""
    W, H = 1100, 720
    c = Canvas(W, H)
    c.label(W/2, 56, "Refraction of light", 36, "bold")
    # boundary (horizontal in middle)
    bx1, bx2 = 130, W-130
    by = 380
    c.S.append(
        f'<line x1="{bx1}" y1="{by}" x2="{bx2}" y2="{by}" '
        f'stroke="{ST}" stroke-width="3"/>')
    # medium labels
    c.S.append(
        f'<rect x="{bx1}" y="{by}" width="{bx2-bx1}" height="240" '
        f'fill="{STYLE["arrow"]}" opacity="0.18"/>')
    _clabel(c, bx1+80, by-20, "air", 22, LBL, "bold")
    _clabel(c, bx1+80, by+30, "(less dense)", 18, LBL, "normal")
    _clabel(c, bx1+80, by+140, "water / glass", 22, LBL, "bold")
    _clabel(c, bx1+80, by+170, "(more dense)", 18, LBL, "normal")
    # contact point
    cpx, cpy = W/2, by
    # normal
    c.S.append(
        f'<line x1="{cpx}" y1="{by-280}" x2="{cpx}" y2="{by+220}" '
        f'stroke="{ST}" stroke-width="2" stroke-dasharray="6 6"/>')
    _clabel(c, cpx+50, by-260, "normal", 18, LBL, "normal")
    # incident ray (from upper-left)
    in_x = cpx - 290; in_y = by - 260
    _force_arrow(c, in_x, in_y, cpx-10, cpy-10, "#C8102E", None)
    _clabel(c, in_x+50, in_y-14, "incident ray", 20, "#C8102E", "bold")
    # refracted ray (bends toward normal) — shallower angle into denser
    rf_x = cpx + 130; rf_y = by + 220
    _force_arrow(c, cpx+8, cpy+10, rf_x, rf_y, "#2E5E45", None)
    _clabel(c, rf_x+60, rf_y, "refracted ray", 20, "#2E5E45", "bold")
    # angle arcs
    c.S.append(
        f'<path d="M {cpx-60} {cpy} A 60 60 0 0 1 {cpx-44} {cpy-42}" '
        f'fill="none" stroke="{ST}" stroke-width="2"/>')
    _clabel(c, cpx-78, cpy-30, "i", 22, LBL, "bold")
    c.S.append(
        f'<path d="M {cpx+44} {cpy+42} A 60 60 0 0 1 {cpx+22} {cpy+58}" '
        f'fill="none" stroke="{ST}" stroke-width="2"/>')
    _clabel(c, cpx+62, cpy+58, "r", 22, LBL, "bold")
    _clabel(c, W/2, H-40,
            "Entering a denser medium: ray bends TOWARD the normal "
            "(slows down).", 21, RED, "bold")
    return c.svg()


def convex_lens():
    """Object outside focal length producing a real inverted image."""
    W, H = 1240, 660
    c = Canvas(W, H)
    c.label(W/2, 56, "Convex lens \u2014 real image", 36, "bold")
    cx_axis_y = 380
    # principal axis
    c.S.append(
        f'<line x1="80" y1="{cx_axis_y}" x2="{W-80}" y2="{cx_axis_y}" '
        f'stroke="{ST}" stroke-width="2" stroke-dasharray="6 6"/>')
    # lens at centre
    lcx = W/2
    c.S.append(
        f'<ellipse cx="{lcx}" cy="{cx_axis_y}" rx="22" ry="170" '
        f'fill="{STYLE["arrow"]}" opacity="0.25" stroke="{ST}" '
        f'stroke-width="2.5"/>')
    # focal points
    F = 220
    for fx, lab in ((lcx-F, "F"), (lcx+F, "F'"),
                    (lcx-2*F, "2F"), (lcx+2*F, "2F'")):
        c.S.append(
            f'<circle cx="{fx}" cy="{cx_axis_y}" r="5" fill="{ST}"/>')
        _clabel(c, fx, cx_axis_y+28, lab, 18, LBL, "normal")
    # object: arrow upward at left of 2F
    ox_pos = lcx - 2*F - 60
    obj_top = cx_axis_y - 140
    _force_arrow(c, ox_pos, cx_axis_y, ox_pos, obj_top, "#2E5E45", None)
    _clabel(c, ox_pos-40, cx_axis_y-90, "object", 20, "#2E5E45", "bold")
    # image: arrow downward at right of 2F' (real, inverted)
    img_x = lcx + 2*F + 30
    img_bot = cx_axis_y + 70
    _force_arrow(c, img_x, cx_axis_y, img_x, img_bot, "#C8102E", None)
    _clabel(c, img_x+40, cx_axis_y+60, "image", 20, "#C8102E", "bold")
    _clabel(c, img_x+40, cx_axis_y+90, "(real, inverted)",
            16, "#C8102E", "normal")
    # 3 principal rays from object tip
    # ray 1: parallel to axis -> through F'
    c.S.append(
        f'<polyline points="{ox_pos},{obj_top} {lcx},{obj_top} '
        f'{img_x},{img_bot}" fill="none" stroke="#C8102E" stroke-width="2"/>')
    # ray 2: through centre of lens (straight through)
    c.S.append(
        f'<line x1="{ox_pos}" y1="{obj_top}" x2="{img_x}" y2="{img_bot}" '
        f'stroke="#3B82F6" stroke-width="2"/>')
    # ray 3: through F -> emerges parallel
    fy_int_x = lcx
    fy_int_y = cx_axis_y - ((cx_axis_y-obj_top) * (lcx-(lcx-F))/(lcx-F-ox_pos))
    c.S.append(
        f'<polyline points="{ox_pos},{obj_top} {fy_int_x},{cx_axis_y} '
        f'{img_x},{cx_axis_y}" fill="none" stroke="#FBBF24" '
        f'stroke-width="2"/>')
    _clabel(c, W/2, H-40,
            "Object beyond 2F: image is real, inverted, smaller, "
            "between F' and 2F'.", 21, RED, "bold")
    return c.svg()


def _render_p2_waves():
    export(transverse_wave(),  "p2_transverse_wave", formats=("png",))
    export(longitudinal_wave(), "p2_longitudinal_wave", formats=("png",))
    export(reflection_ray(),  "p2_reflection_ray", formats=("png",))
    export(refraction_ray(),  "p2_refraction_ray", formats=("png",))
    export(convex_lens(),      "p2_convex_lens", formats=("png",))
    for nm in ("p2_transverse_wave","p2_longitudinal_wave",
               "p2_reflection_ray","p2_refraction_ray","p2_convex_lens"):
        print("p2 waves", nm)


# ====================================================================
# PHYSICS P2 — MODULE 3: MAGNETISM & ELECTROMAGNETISM
# ====================================================================
def bar_magnet_field():
    """Single bar magnet with field lines looping N -> S."""
    W, H = 1100, 700
    c = Canvas(W, H)
    c.label(W/2, 56, "Magnetic field around a bar magnet", 36, "bold")
    # magnet
    mx, my = W/2, 380
    mw, mh = 300, 80
    # N (red) half, S (blue) half
    c.S.append(
        f'<rect x="{mx-mw/2}" y="{my-mh/2}" width="{mw/2}" height="{mh}" '
        f'fill="#C8102E" opacity="0.85" stroke="{ST}" stroke-width="2"/>')
    c.S.append(
        f'<rect x="{mx}" y="{my-mh/2}" width="{mw/2}" height="{mh}" '
        f'fill="#3B82F6" opacity="0.85" stroke="{ST}" stroke-width="2"/>')
    _clabel(c, mx-mw/4, my+8, "N", 36, "#FFFFFF", "bold")
    _clabel(c, mx+mw/4, my+8, "S", 36, "#FFFFFF", "bold")
    # field lines (loops from N to S outside the magnet)
    for r in (90, 150, 210, 270):
        # upper arc
        c.S.append(
            f'<path d="M {mx-mw/2} {my} '
            f'C {mx-mw/2} {my-r} {mx+mw/2} {my-r} {mx+mw/2} {my}" '
            f'fill="none" stroke="{ACC}" stroke-width="2.5"/>')
        # lower arc
        c.S.append(
            f'<path d="M {mx-mw/2} {my} '
            f'C {mx-mw/2} {my+r} {mx+mw/2} {my+r} {mx+mw/2} {my}" '
            f'fill="none" stroke="{ACC}" stroke-width="2.5"/>')
        # arrowhead on upper arc going S->N is wrong direction; field
        # lines go N -> S externally. Place arrowhead near right side
        # pointing toward S (which is right pole).
        # On upper arc, halfway, arrow pointing rightward+down
        ax_up = mx + 20; ay_up = my - r*0.78
        c.S.append(
            f'<polygon points="{ax_up+10},{ay_up+8} {ax_up-6},{ay_up} '
            f'{ax_up-6},{ay_up+18}" fill="{ACC}"/>')
        ax_dn = mx + 20; ay_dn = my + r*0.78
        c.S.append(
            f'<polygon points="{ax_dn+10},{ay_dn-8} {ax_dn-6},{ay_dn} '
            f'{ax_dn-6},{ay_dn-18}" fill="{ACC}"/>')
    _clabel(c, W/2, H-30,
            "Field lines run from N to S OUTSIDE the magnet; closer "
            "together = stronger field.", 21, RED, "bold")
    return c.svg()


def two_magnets():
    """Two-magnet interaction - attraction (S face N) on left,
    repulsion (N face N) on right."""
    W, H = 1280, 640
    c = Canvas(W, H)
    c.label(W/2, 56, "Magnetic interaction", 36, "bold")
    mw, mh = 180, 64

    def magnet(cx, cy, left_pole, right_pole):
        col_l = "#C8102E" if left_pole == "N" else "#3B82F6"
        col_r = "#C8102E" if right_pole == "N" else "#3B82F6"
        c.S.append(
            f'<rect x="{cx-mw/2}" y="{cy-mh/2}" width="{mw/2}" '
            f'height="{mh}" fill="{col_l}" opacity="0.85" '
            f'stroke="{ST}" stroke-width="2"/>')
        c.S.append(
            f'<rect x="{cx}" y="{cy-mh/2}" width="{mw/2}" '
            f'height="{mh}" fill="{col_r}" opacity="0.85" '
            f'stroke="{ST}" stroke-width="2"/>')
        _clabel(c, cx-mw/4, cy+8, left_pole, 28, "#FFFFFF", "bold")
        _clabel(c, cx+mw/4, cy+8, right_pole, 28, "#FFFFFF", "bold")

    # Left: attraction. Left magnet N-S, right magnet N-S
    # => S of left faces N of right => unlike poles => ATTRACT
    cyA = 280
    magnet(280, cyA, "N", "S")
    magnet(550, cyA, "N", "S")
    # arrows pulling inward
    _force_arrow(c, 400, cyA, 440, cyA, "#2E5E45", None)
    _force_arrow(c, 470, cyA, 430, cyA, "#2E5E45", None)
    _clabel(c, 415, cyA-60, "Unlike poles ATTRACT",
            22, "#2E5E45", "bold")
    _clabel(c, 415, cyA+70, "(S meets N)",
            18, LBL, "normal")

    # Right: repulsion. Left magnet S-N, right magnet N-S
    # => N of left faces N of right => like poles => REPEL
    magnet(820, cyA, "S", "N")
    magnet(1090, cyA, "N", "S")
    # arrows pushing outward
    _force_arrow(c, 940, cyA, 900, cyA, "#C8102E", None)
    _force_arrow(c, 970, cyA, 1010, cyA, "#C8102E", None)
    _clabel(c, 955, cyA-60, "Like poles REPEL",
            22, "#C8102E", "bold")
    _clabel(c, 955, cyA+70, "(N meets N)",
            18, LBL, "normal")

    _clabel(c, W/2, H-40,
            "Two magnets: opposites attract, likes repel.",
            22, RED, "bold")
    return c.svg()


def current_wire_field():
    """Field circles around a wire carrying current out of the page."""
    W, H = 1100, 700
    c = Canvas(W, H)
    c.label(W/2, 56, "Field around a current-carrying wire", 36, "bold")
    cx, cy = W/2, 380
    # wire (current coming out of page) shown as circle with dot
    c.S.append(
        f'<circle cx="{cx}" cy="{cy}" r="22" fill="{STYLE["cream"]}" '
        f'stroke="{ST}" stroke-width="3"/>')
    c.S.append(
        f'<circle cx="{cx}" cy="{cy}" r="6" fill="{ST}"/>')
    _clabel(c, cx+50, cy-30, "current out of page", 18, LBL, "normal")
    # concentric field circles
    for r, has_arrow in ((70, True), (120, True), (170, True), (220, False)):
        c.S.append(
            f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" '
            f'stroke="{ACC}" stroke-width="2.5"/>')
        if has_arrow:
            # arrowhead at top of circle pointing right (anticlockwise
            # field when current comes out of page — right-hand rule)
            ax, ay = cx, cy-r
            c.S.append(
                f'<polygon points="{ax+10},{ay} {ax-2},{ay-8} '
                f'{ax-2},{ay+8}" fill="{ACC}"/>')
    _clabel(c, W/2, H-40,
            "Right-hand grip rule: thumb = current direction, "
            "fingers curl in field direction.", 21, RED, "bold")
    return c.svg()


def solenoid_field():
    """Solenoid (coil of wire) with field lines like a bar magnet."""
    W, H = 1200, 660
    c = Canvas(W, H)
    c.label(W/2, 56, "Field around a solenoid", 36, "bold")
    cx, cy = W/2, 360
    # solenoid coil — series of small ellipses
    sx1, sx2 = cx-200, cx+200
    n_coils = 10
    for i in range(n_coils):
        ex = sx1 + i*(sx2-sx1)/(n_coils-1)
        c.S.append(
            f'<ellipse cx="{ex}" cy="{cy}" rx="18" ry="50" '
            f'fill="none" stroke="{ST}" stroke-width="2"/>')
    # ends
    _clabel(c, sx1-30, cy, "S", 28, LBL, "bold")
    _clabel(c, sx2+30, cy, "N", 28, LBL, "bold")
    # field lines like bar magnet (loops from N -> S externally,
    # straight inside)
    for r in (90, 160, 230):
        c.S.append(
            f'<path d="M {sx1} {cy} '
            f'C {sx1} {cy-r} {sx2} {cy-r} {sx2} {cy}" '
            f'fill="none" stroke="{ACC}" stroke-width="2.5"/>')
        c.S.append(
            f'<path d="M {sx1} {cy} '
            f'C {sx1} {cy+r} {sx2} {cy+r} {sx2} {cy}" '
            f'fill="none" stroke="{ACC}" stroke-width="2.5"/>')
        # arrowheads going from N (right) externally back to S (left)
        ax = cx - 30; ay = cy - r*0.78
        c.S.append(
            f'<polygon points="{ax-12},{ay+8} {ax+4},{ay} '
            f'{ax+4},{ay+18}" fill="{ACC}"/>')
        ax2 = cx - 30; ay2 = cy + r*0.78
        c.S.append(
            f'<polygon points="{ax2-12},{ay2-8} {ax2+4},{ay2} '
            f'{ax2+4},{ay2-18}" fill="{ACC}"/>')
    # inside: straight line N->S (drawn going right -> left)
    c.S.append(
        f'<line x1="{sx2-30}" y1="{cy}" x2="{sx1+30}" y2="{cy}" '
        f'stroke="{ACC}" stroke-width="2.5"/>')
    c.S.append(
        f'<polygon points="{sx1+30},{cy} {sx1+50},{cy-9} '
        f'{sx1+50},{cy+9}" fill="{ACC}"/>')
    _clabel(c, W/2, H-40,
            "A current-carrying solenoid produces a field like a bar "
            "magnet \u2014 strong, uniform inside.", 21, RED, "bold")
    return c.svg()


def motor_effect():
    """Wire carrying current in a magnetic field: Fleming's left-hand
    rule (force, field, current as perpendicular axes)."""
    W, H = 1200, 680
    c = Canvas(W, H)
    c.label(W/2, 56, "The motor effect", 36, "bold")
    cx, cy = W/2, 380
    # Show: vertical wire (current up) between N and S poles -> force out
    # of page or to the side
    # Two magnets either side
    mw, mh = 80, 220
    # N pole on left
    c.S.append(
        f'<rect x="{cx-260}" y="{cy-mh/2}" width="{mw}" height="{mh}" '
        f'fill="#C8102E" opacity="0.85" stroke="{ST}" stroke-width="2"/>')
    _clabel(c, cx-260+mw/2, cy+8, "N", 36, "#FFFFFF", "bold")
    # S pole on right
    c.S.append(
        f'<rect x="{cx+180}" y="{cy-mh/2}" width="{mw}" height="{mh}" '
        f'fill="#3B82F6" opacity="0.85" stroke="{ST}" stroke-width="2"/>')
    _clabel(c, cx+180+mw/2, cy+8, "S", 36, "#FFFFFF", "bold")
    # field lines N -> S (left to right) between poles
    for y_off in (-70, -20, 30, 80):
        c.S.append(
            f'<line x1="{cx-180}" y1="{cy+y_off}" x2="{cx+180}" '
            f'y2="{cy+y_off}" stroke="{ACC}" stroke-width="2" '
            f'stroke-dasharray="5 5"/>')
        c.S.append(
            f'<polygon points="{cx+180},{cy+y_off} {cx+165},'
            f'{cy+y_off-7} {cx+165},{cy+y_off+7}" fill="{ACC}"/>')
    _clabel(c, cx, cy-130, "magnetic field (N \u2192 S)",
            18, ACC, "bold")
    # wire (vertical, current going up)
    c.S.append(
        f'<line x1="{cx}" y1="{cy-130}" x2="{cx}" y2="{cy+130}" '
        f'stroke="#C8102E" stroke-width="6"/>')
    _force_arrow(c, cx, cy+50, cx, cy-80, "#C8102E", None)
    _clabel(c, cx-46, cy+150, "current (I)", 20, "#C8102E", "bold")
    # ⊕ figlib correction (MRB-352 run 2) — the force is INTO the page.
    # The library drew it OUT of the page. F = I L x B with x right, y up,
    # z out of the page: the current runs up (L = +y), the field runs N to S,
    # left to right (B = +x), and (+y) x (+x) = -z. Fleming's left-hand rule
    # agrees: First finger right, seCond finger up, thuMb points into the
    # page. Drawn as a cross in a circle (into the page).
    _clabel(c, cx, cy-180, "force (F) on wire", 20, "#2E5E45", "bold")
    c.S.append(
        f'<circle cx="{cx}" cy="{cy-160}" r="14" fill="{STYLE["cream"]}" '
        f'stroke="#2E5E45" stroke-width="3"/>')
    for s in (-1, 1):
        c.S.append(
            f'<line x1="{cx-8}" y1="{cy-160-8*s}" x2="{cx+8}" '
            f'y2="{cy-160+8*s}" stroke="#2E5E45" stroke-width="3"/>')
    _clabel(c, cx+50, cy-160, "(into page)", 16, "#2E5E45", "normal")
    _clabel(c, W/2, H-40,
            "Fleming's left-hand rule: First finger = Field, "
            "seCond = Current, thuMb = Motion.",
            21, RED, "bold")
    return c.svg()


def _render_p2_magnetism():
    export(bar_magnet_field(), "p2_bar_magnet", formats=("png",))
    export(two_magnets(), "p2_two_magnets", formats=("png",))
    export(current_wire_field(), "p2_wire_field", formats=("png",))
    export(solenoid_field(), "p2_solenoid", formats=("png",))
    export(motor_effect(), "p2_motor_effect", formats=("png",))
    for nm in ("p2_bar_magnet","p2_two_magnets","p2_wire_field",
               "p2_solenoid","p2_motor_effect"):
        print("p2 magnetism", nm)


# ====================================================================
# PHYSICS P2 — MODULE 4: SPACE
# ====================================================================
def solar_system():
    """Sun + 8 planets in order, labelled, not to scale."""
    W, H = 1380, 580
    c = Canvas(W, H)
    c.label(W/2, 56, "The Solar System (not to scale)", 36, "bold")
    cy = 320
    # sun
    sx = 90
    c.S.append(
        f'<circle cx="{sx}" cy="{cy}" r="48" fill="#FBBF24" '
        f'opacity="0.9" stroke="{ST}" stroke-width="2"/>')
    _clabel(c, sx, cy+90, "Sun", 22, LBL, "bold")
    # planets (name, radius, colour)
    planets = [
        ("Mercury", 10, "#5B6B82"),
        ("Venus",   16, "#E0892E"),
        ("Earth",   18, "#3B82F6"),
        ("Mars",    14, "#C8102E"),
        ("Jupiter", 38, "#A67042"),
        ("Saturn",  32, "#FBBF24"),
        ("Uranus",  24, "#A9D9BE"),
        ("Neptune", 24, "#3457A8"),
    ]
    px = sx + 100
    for name, r, col in planets:
        c.S.append(
            f'<circle cx="{px+r}" cy="{cy}" r="{r}" fill="{col}" '
            f'opacity="0.85" stroke="{ST}" stroke-width="2"/>')
        _clabel(c, px+r, cy+r+30, name, 18, LBL, "bold")
        px += r*2 + 50
    # rings on saturn
    sat_idx = 5
    sat_x = 90 + 100
    for nm, rr, _ in planets[:sat_idx]:
        sat_x += rr*2 + 50
    sat_x += planets[sat_idx][1]
    c.S.append(
        f'<ellipse cx="{sat_x}" cy="{cy}" rx="48" ry="8" '
        f'fill="none" stroke="{STYLE["muted"]}" stroke-width="2"/>')
    _clabel(c, W/2, H-40,
            "Order from the Sun: Mercury, Venus, Earth, Mars, "
            "Jupiter, Saturn, Uranus, Neptune.",
            21, RED, "bold")
    return c.svg()


def star_life_cycle():
    """Two branches: low/medium-mass star and high-mass star."""
    W, H = 1380, 760
    c = Canvas(W, H)
    c.label(W/2, 56, "Life cycle of a star", 36, "bold")

    def disc(cx, cy, r, col, label, sublabel=None):
        c.S.append(
            f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{col}" '
            f'opacity="0.75" stroke="{ST}" stroke-width="2"/>')
        _clabel(c, cx, cy+r+24, label, 19, LBL, "bold")
        if sublabel:
            _clabel(c, cx, cy+r+46, sublabel, 16, LBL, "normal")

    # Common start: nebula -> protostar -> main sequence
    disc(120, 380, 40, "#9333EA", "Nebula", "cloud of dust & gas")
    _force_arrow(c, 175, 380, 245, 380, ACC, None)
    disc(300, 380, 26, "#E0892E", "Protostar")
    _force_arrow(c, 340, 380, 410, 380, ACC, None)
    disc(465, 380, 22, "#FBBF24", "Main sequence", "(like our Sun)")
    _force_arrow(c, 510, 380, 600, 380, ACC, None)

    # Branch: low/medium mass (top), high mass (bottom)
    # Low/medium-mass branch upward
    _force_arrow(c, 600, 360, 670, 250, ACC, None)
    disc(700, 230, 34, "#C8102E", "Red giant")
    _force_arrow(c, 760, 230, 830, 230, ACC, None)
    disc(880, 230, 16, "#FFFFFF", "White dwarf")
    _force_arrow(c, 905, 230, 970, 230, ACC, None)
    disc(1010, 230, 14, "#5B6B82", "Black dwarf",
         "(cool remnant)")
    _clabel(c, 800, 120, "LOW / MEDIUM MASS STAR",
            22, "#C8102E", "bold")

    # High-mass branch downward
    _force_arrow(c, 600, 400, 670, 510, ACC, None)
    disc(720, 530, 44, "#C8102E", "Red supergiant")
    _force_arrow(c, 780, 530, 850, 530, ACC, None)
    disc(900, 530, 28, "#FBBF24", "Supernova",
         "(massive explosion)")
    _force_arrow(c, 940, 530, 1010, 530, ACC, None)
    disc(1060, 530, 14, "#3457A8", "Neutron star",
         "or")
    disc(1180, 530, 18, "#000000", "Black hole")
    _clabel(c, 900, 640, "HIGH MASS STAR",
            22, "#C8102E", "bold")

    _clabel(c, W/2, H-30,
            "Star's final fate depends on its mass.",
            21, RED, "bold")
    return c.svg()


def em_spectrum():
    """EM spectrum band: radio -> gamma."""
    W, H = 1380, 540
    c = Canvas(W, H)
    c.label(W/2, 56, "The Electromagnetic Spectrum", 36, "bold")
    bands = [
        ("Radio",      "#C8102E", "TV, radio"),
        ("Microwave",  "#E0892E", "cooking, satellites"),
        ("Infrared",   "#FBBF24", "heaters, remote controls"),
        ("Visible",    "#A9D9BE", "what we see"),
        ("UV",         "#3B82F6", "sun beds, fluorescence"),
        ("X-ray",      "#9333EA", "medical imaging"),
        ("Gamma",      "#3A2B1F", "treating cancer"),
    ]
    n = len(bands)
    bw = (W - 80) / n
    by = 170
    bh = 130
    for i, (name, col, use) in enumerate(bands):
        bx = 40 + i*bw
        c.S.append(
            f'<rect x="{bx}" y="{by}" width="{bw}" height="{bh}" '
            f'fill="{col}" opacity="0.85" stroke="{ST}" '
            f'stroke-width="2"/>')
        text_col = "#FFFFFF" if col in ("#3A2B1F","#9333EA","#3457A8") \
                              else LBL
        _clabel(c, bx+bw/2, by+bh/2-4, name, 22, text_col, "bold")
        _clabel(c, bx+bw/2, by+bh/2+24, use, 14, text_col, "normal")
    # wavelength label
    _clabel(c, 80, by-30, "long \u03bb / low frequency",
            18, LBL, "bold")
    _clabel(c, W-80, by-30, "short \u03bb / high frequency",
            18, LBL, "bold")
    # arrow
    c.S.append(
        f'<line x1="160" y1="{by-12}" x2="{W-160}" y2="{by-12}" '
        f'stroke="{ACC}" stroke-width="3"/>')
    c.S.append(
        f'<polygon points="{W-160},{by-12} {W-180},{by-22} '
        f'{W-180},{by-2}" fill="{ACC}"/>')
    _clabel(c, W/2, H-40,
            "All EM waves travel at the same speed in vacuum "
            "(3 \u00d7 10\u2078 m/s).",
            21, RED, "bold")
    return c.svg()


def red_shift():
    """Spectrum from a nearby galaxy vs a distant galaxy showing red
    shift."""
    W, H = 1240, 700
    c = Canvas(W, H)
    c.label(W/2, 56, "Red shift \u2014 expanding universe",
            36, "bold")
    # Two spectra panels
    spec_w = 760
    spec_h = 90
    sx = (W - spec_w) / 2

    def spectrum(y, shift_frac, label):
        # full visible spectrum band
        c.S.append(
            f'<defs><linearGradient id="spec{int(shift_frac*100)}" '
            f'x1="0%" x2="100%"><stop offset="0%" stop-color="#9333EA"/>'
            f'<stop offset="20%" stop-color="#3B82F6"/>'
            f'<stop offset="40%" stop-color="#A9D9BE"/>'
            f'<stop offset="60%" stop-color="#FBBF24"/>'
            f'<stop offset="80%" stop-color="#E0892E"/>'
            f'<stop offset="100%" stop-color="#C8102E"/>'
            f'</linearGradient></defs>')
        c.S.append(
            f'<rect x="{sx}" y="{y}" width="{spec_w}" height="{spec_h}" '
            f'fill="url(#spec{int(shift_frac*100)})" stroke="{ST}" '
            f'stroke-width="2"/>')
        # absorption lines (black) — shift toward the red end with shift_frac
        line_xs = [0.18, 0.32, 0.52, 0.70]  # reference positions
        for lx in line_xs:
            ax = sx + (lx + shift_frac) * spec_w * (1 - shift_frac)
            ax = sx + (lx + shift_frac*0.18) * spec_w
            if sx < ax < sx + spec_w:
                c.S.append(
                    f'<line x1="{ax:.1f}" y1="{y}" x2="{ax:.1f}" '
                    f'y2="{y+spec_h}" stroke="#1A1A1A" '
                    f'stroke-width="3"/>')
        c.S.append(
            f'<text x="{sx-20:.1f}" y="{y+spec_h/2+10:.1f}" '
            f'font-family="{FONT}" font-size="22" fill="{LBL}" '
            f'text-anchor="end" font-weight="bold">{label}</text>')

    spectrum(180, 0.0, "Nearby galaxy")
    spectrum(360, 1.0, "Distant galaxy")
    # arrow showing how lines have moved
    _clabel(c, W/2, 310, "lines SHIFT toward the red end \u2192",
            22, "#C8102E", "bold")
    _clabel(c, W/2, H-60,
            "Light from distant galaxies is red-shifted \u2192 "
            "they are moving away from us.",
            21, RED, "bold")
    _clabel(c, W/2, H-30,
            "The further the galaxy, the bigger the red shift "
            "(Hubble's observation).",
            21, RED, "bold")
    return c.svg()


def _render_p2_space():
    export(solar_system(), "p2_solar_system", formats=("png",))
    export(star_life_cycle(), "p2_star_life_cycle", formats=("png",))
    export(em_spectrum(), "p2_em_spectrum", formats=("png",))
    export(red_shift(), "p2_red_shift", formats=("png",))
    for nm in ("p2_solar_system","p2_star_life_cycle",
               "p2_em_spectrum","p2_red_shift"):
        print("p2 space", nm)


if __name__ == "__main__":
    # four proof-of-concept circuits stressing the engine
    demos = {
        "series_basic": circuit(
            [("cell", None, "6 V"), ("switch",),
             ("lamp", "L1")],
            title="Series circuit"),
        "series_meters": circuit(
            [("cell", None, "6 V"), ("ammeter",),
             ("resistor", "R1", "10 \u03a9"), ("voltmeter",)],
            title="Series circuit with ammeter and voltmeter"),
        "parallel_two": circuit(
            [("cell", None, "6 V"), ("switch",),
             parallel([[("lamp", "L1")], [("lamp", "L2")]])],
            title="Parallel circuit \u2014 two branches"),
        "mixed": circuit(
            [("cell", None, "6 V"), ("ammeter",),
             ("resistor", "R1", "10 \u03a9"),
             parallel([[("resistor", "R2", "20 \u03a9")],
                       [("resistor", "R3", "20 \u03a9")]])],
            title="Mixed series and parallel"),
    }
    for nm, svg in demos.items():
        export(svg, nm, formats=("png",))
        print("circuit", nm)
    _render_all()
    _render_phase2()
    _render_phase3()
    _render_phase4()
    _render_p2_forces()
    _render_p2_waves()
    _render_p2_magnetism()
    _render_p2_space()


# ====================================================================
# ⊕ FIGLIB EXTENSIONS (MRB-352 run 2) — question figures
#
# Everything below is new. It is drawn in the library's style (its STYLE,
# its Canvas, its symbols and engine) on phone-width canvases, so a
# question figure is legible in a 320px column: text sizes come from
# `q_font(W)`, never typed. Each builder is parametrised — none is a
# one-off for a single question.
# ====================================================================
from .style import (MUTED, TINT, arrow as _q_arrow, box as _q_box,  # noqa: E402
                    line as _q_line, q_font, q_stroke, text as _q_text)


def symbol_figure(key, W=240, H=150):
    """One AQA circuit symbol on its own, in a short length of wire."""
    if key not in {k for k, _ in AQA_SYMBOLS}:
        raise ValueError(f"'{key}' is not on the AQA 8463 symbol list")
    c = Canvas(W, H)
    # ⊕ fix round 1 (visual m7): centre what is actually drawn, not the
    # wire. A lamp or resistor is symmetric about its wire; a cell's "+",
    # an LDR's or LED's arrows and an open switch's lever are not, so a
    # fixed wire height left most symbols sitting low in the card.
    tmp = _Tmp()
    SYMBOLS[key](tmp, 0, 0, None, None)
    y0, y1 = _extent_y(tmp.S)
    SYMBOLS[key](c, W/2, H/2 - (y0 + y1)/2, None, None)
    return c.svg()


def symbol_panel(items, cell_w=210, H=190, cols=None, fs=None):
    """Two or more AQA symbols, each captioned underneath — for "which of
    A / B is …" comparison questions. `items` is [(caption, key), ...]; a
    caption names the DRAWING ("Student A"), never the component.

    ⊕ fix round 1 (visual M1): `cols` lays the symbols out in a grid of
    that many columns, `H` being the height of one ROW. Four symbols in one
    row made a 700-wide strip that shrank to 0.47 on a phone, and the
    detail the questions turn on (an LED's arrows against a diode's) went
    to a few pixels. Default: one row, as before."""
    cols = cols or len(items)
    rows = -(-len(items) // cols)
    W = int(cell_w * cols + 20)
    c = Canvas(W, int(H * rows))
    fs = fs or q_font(W, floor=20)
    for i, (caption, key) in enumerate(items):
        if key not in {k for k, _ in AQA_SYMBOLS}:
            raise ValueError(f"'{key}' is not on the AQA 8463 symbol list")
        col, row = i % cols, i // cols
        x = 10 + cell_w*col + cell_w/2
        y0 = H*row
        SYMBOLS[key](c, x, y0 + H - 94, None, None)   # wire 94 above the foot
        _q_text(c, x, y0 + H - 20, caption, fs, LBL, "bold")
    return c.svg()

def question_circuit(netlist, gap=None, left=None, right=None):
    """The library's circuit engine in the phone frame, AQA symbols only.
    `netlist` is JSON-friendly: a component is a list ["lamp"] /
    ["resistor", null, null, {"voltmeter": true}], and a parallel section
    is {"parallel": [[comp, ...], [comp, ...]]}."""
    def conv(it):
        if isinstance(it, dict) and "parallel" in it:
            return parallel([[tuple(x) for x in br] for br in it["parallel"]])
        return tuple(it)
    return circuit([conv(it) for it in netlist], layout=QUESTION_LAYOUT,
                   gap=gap, aqa_only=True,
                   left=[tuple(x) for x in (left or [])],
                   right=[tuple(x) for x in (right or [])])


def _block_arrow(c, x0, x1, y, h, direction, fill, lines, fs):
    """A bar with a pointed end — a force drawn to scale, labelled inside."""
    tip = min(h * 0.55, abs(x1 - x0) * 0.3)
    if direction == "right":
        pts = [(x0, y), (x1 - tip, y), (x1, y + h/2), (x1 - tip, y + h),
               (x0, y + h)]
        tx = (x0 + x1 - tip) / 2
    else:
        pts = [(x1, y), (x0 + tip, y), (x0, y + h/2), (x0 + tip, y + h),
               (x1, y + h)]
        tx = (x0 + tip + x1) / 2
    c.S.append('<polygon points="%s" fill="%s" stroke="%s" '
               'stroke-width="2.5" stroke-linejoin="round"/>'
               % (" ".join("%.1f,%.1f" % p for p in pts), fill, ST))
    yy = y + h/2 - (len(lines) - 1) * (fs + 2) / 2 + fs * 0.35
    for ln in lines:
        _q_text(c, tx, yy, ln, fs, LBL, "bold")
        yy += fs + 2


def force_beam(whole, parts, W=480):
    """A force and the parts it splits into, every bar to ONE scale, so
    the parts visibly fill the whole. `whole` / each part is
    {"label", "newtons", "dir": "left"|"right"}."""
    fs = q_font(W)
    x0, x1 = 26, W - 26
    k = (x1 - x0) / float(whole["newtons"])
    h = 2 * fs + 20
    H = int(24 + h + 30 + h + 24)
    c = Canvas(W, H)
    y1 = 24
    y2 = y1 + h + 30
    _q_line(c, x0, y1 - 8, x0, y2 + h + 8, MUTED, q_stroke(W, 2), "6 6")
    _q_line(c, x1, y1 - 8, x1, y2 + h + 8, MUTED, q_stroke(W, 2), "6 6")
    _block_arrow(c, x0, x1, y1, h, whole["dir"], TINT["mint"],
                 [whole["label"], "%g N" % whole["newtons"]], fs)
    fills = [TINT["salmon"], TINT["blue"], TINT["lilac"]]
    x = x0
    total = 0
    for i, part in enumerate(parts):
        span = part["newtons"] * k
        _block_arrow(c, x, x + span, y2, h, part["dir"], fills[i % 3],
                     [part["label"], "%g N" % part["newtons"]], fs)
        x += span
        total += part["newtons"]
    if abs(total - whole["newtons"]) > 1e-9:
        raise ValueError("force_beam: the parts (%g N) do not add up to the "
                         "whole (%g N)" % (total, whole["newtons"]))
    return c.svg()


def _pole(c, x, y, w, h, letter, fs):
    fill = TINT["salmon"] if letter == "N" else TINT["blue"]
    _q_box(c, x, y, w, h, fill, ST, 2.5)
    _q_text(c, x + w/2, y + h/2 + fs*0.36, letter, fs, LBL, "bold")


def horseshoe_gap(lines=5, W=420):
    """A horseshoe magnet seen from the front, opening upward, its two
    jaws' inner faces (N left, S right) facing each other across a gap.
    Straight, parallel, evenly spaced field lines cross the gap from the N
    face to the S face, touching both, each with one arrowhead at its
    middle. No field is drawn outside the gap."""
    fs = q_font(W, floor=26)
    H = 330
    c = Canvas(W, H)
    aw, arm_top, base_y = 90, 30, 250
    lx, rx = 40, W - 40 - aw
    body = TINT["sand"]
    pts = [(lx, arm_top), (lx + aw, arm_top), (lx + aw, base_y - 10),
           (rx, base_y - 10), (rx, arm_top), (rx + aw, arm_top),
           (rx + aw, base_y + 50), (lx, base_y + 50)]
    c.S.append('<polygon points="%s" fill="%s" stroke="%s" stroke-width="2.5" '
               'stroke-linejoin="round"/>'
               % (" ".join("%.1f,%.1f" % p for p in pts), body, ST))
    pole_h = 140
    _pole(c, lx, arm_top, aw, pole_h, "N", fs)
    _pole(c, rx, arm_top, aw, pole_h, "S", fs)
    x0, x1 = lx + aw, rx
    for i in range(lines):
        y = arm_top + pole_h * (i + 0.5) / lines
        _q_line(c, x0, y, x1, y, ACC, q_stroke(W, 3), None, "butt")
        mx = (x0 + x1) / 2
        c.S.append('<polygon points="%.1f,%.1f %.1f,%.1f %.1f,%.1f" fill="%s" '
                   'stroke="none"/>' % (mx + 9, y, mx - 8, y - 8, mx - 8,
                                        y + 8, ACC))
    return c.svg()

def _conductor(c, x, y, r, into):
    """A wire seen end-on: a cross (current into the page) or a dot
    (current out of it) inside a circle."""
    c.S.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{TINT["white"]}" '
               f'stroke="{ST}" stroke-width="3"/>')
    if into:
        d = r * 0.6
        _q_line(c, x - d, y - d, x + d, y + d, ST, 3)
        _q_line(c, x - d, y + d, x + d, y - d, ST, 3)
    else:
        c.S.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r*0.28:.1f}" '
                   f'fill="{ST}" stroke="none"/>')


def motor_coil_forces(W=460, field_lines=4):
    """A motor coil seen END-ON between N (left) and S (right): the left
    side carries current into the page (a cross), the right side out of it
    (a dot), the two joined by a straight line through the axle. Each side
    has its force arrow — identical length and colour, opposite directions,
    no labels.

    The directions are F = I L x B, x right, y up, z out of the page, and
    the field B = +x (N to S). Left side, current into the page: L = -z,
    (-z) x (+x) = -y, a DOWNWARD force. Right side, current out: L = +z,
    (+z) x (+x) = +y, UPWARD. Fleming's left-hand rule agrees on both.
    (The first KS3 drawing of this figure had them the other way round;
    see docs/diagrams/fix-run-report.md §6.)
    """
    H = 360
    c = Canvas(W, H)
    pw, top, bot = 64, 24, 336
    fsp = q_font(W, floor=26)
    _pole(c, 16, top, pw, bot - top, "N", fsp)
    _pole(c, W - 16 - pw, top, pw, bot - top, "S", fsp)
    x0, x1 = 16 + pw, W - 16 - pw
    ys = [top + (bot - top) * (i + 0.5) / field_lines
          for i in range(field_lines)]
    for y in ys:
        _q_line(c, x0, y, x1, y, ACC, q_stroke(W, 2.5), None, "butt")
        mx = (x0 + x1) / 2
        c.S.append('<polygon points="%.1f,%.1f %.1f,%.1f %.1f,%.1f" fill="%s" '
                   'stroke="none"/>' % (mx + 9, y, mx - 8, y - 8, mx - 8,
                                        y + 8, ACC))
    cy = (top + bot) / 2
    xl, xr, r = W/2 - 64, W/2 + 64, 17
    _q_line(c, xl + r, cy, xr - r, cy, ST, 3)            # the coil, edge-on
    c.S.append(f'<circle cx="{W/2:.1f}" cy="{cy:.1f}" r="5" fill="{ST}" '
               f'stroke="none"/>')                       # the axle
    _conductor(c, xl, cy, r, into=True)
    _conductor(c, xr, cy, r, into=False)
    # ⊕ fix round 1 (visual m2): each tip lands midway between two field
    # lines, not on one, so the red head never merges with a teal line.
    flen = 0.75 * (bot - top) / field_lines
    _q_arrow(c, xl, cy + r + 3, xl, cy + r + 3 + flen, RED, q_stroke(W, 5), 18)
    _q_arrow(c, xr, cy - r - 3, xr, cy - r - 3 - flen, RED, q_stroke(W, 5), 18)
    return c.svg()

def field_point(W=420, rows=3, cols=3, label="P"):
    """Part of a uniform field map: a grid of equal arrows all pointing
    right, the middle one drawn bold from a filled dot, and that point
    lettered above-left. No force on a charge is drawn: which way a charge
    there is pushed is the question, not the picture."""
    fs = q_font(W, floor=22)
    H = 270
    c = Canvas(W, H)
    _q_box(c, 16, 16, W - 32, H - 32, "none", MUTED, q_stroke(W, 2), 0, "8 7")
    L = 70
    for i in range(rows):
        for j in range(cols):
            x = 40 + (W - 80) * (j + 0.5) / cols - L / 2
            y = 16 + (H - 32) * (i + 0.5) / rows
            centre = (i == rows // 2 and j == cols // 2)
            if centre:
                # ⊕ fix round 1 (visual m3): P's arrow is a field arrow
                # like every other — teal, same weight. Only the POINT is
                # singled out; a heavy black arrow read as a force on it.
                _q_arrow(c, x, y, x + L, y, ACC, q_stroke(W, 2.5), 13)
                c.S.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="7" '
                           f'fill="{ST}" stroke="none"/>')
                _q_text(c, x - 16, y - 14, label, fs, LBL, "bold")
            else:
                _q_arrow(c, x, y, x + L, y, ACC, q_stroke(W, 2.5), 13)
    return c.svg()

def resolution_triangle(angle=35, hyp="F", horiz="F cos θ",
                        vert="F sin θ", ang_label="θ", W=420):
    """A force resolved into two perpendicular components: a right-angled
    triangle with the right angle marked."""
    fs = max(q_font(W), 19)     # ⊕ fix round 1 (visual m9): was 15
    H = 280
    c = Canvas(W, H)
    x0, y0 = 50, H - 60
    base = W - 150
    x1 = x0 + base
    y1 = y0 - base * math.tan(math.radians(angle))
    c.S.append('<polygon points="%.1f,%.1f %.1f,%.1f %.1f,%.1f" fill="none" '
               'stroke="%s" stroke-width="3" stroke-linejoin="round"/>'
               % (x0, y0, x1, y0, x1, y1, ST))
    s = 16
    c.S.append('<polyline points="%.1f,%.1f %.1f,%.1f %.1f,%.1f" fill="none" '
               'stroke="%s" stroke-width="2"/>'
               % (x1 - s, y0, x1 - s, y0 - s, x1, y0 - s, ST))
    _q_text(c, (x0 + x1)/2 - 14, (y0 + y1)/2 - 10, hyp, fs, LBL, "bold", "end")
    _q_text(c, (x0 + x1)/2, y0 + fs + 10, horiz, fs, LBL, "bold")
    _q_text(c, x1 + 12, (y0 + y1)/2 + fs*0.35, vert, fs, LBL, "bold", "start")
    _q_text(c, x0 + 64, y0 - 14, ang_label, fs, LBL, "bold", "start")
    return c.svg()


def oscilloscope_compare(traces, W=440, divisions=(10, 5), amplitude=2):
    """One oscilloscope screen per trace, stacked, each captioned — the
    screens share a width and a time-base, so their cycles can be compared
    by eye. Cream screens gridded in divisions with a darker centre line;
    no numbers on any axis. `traces` is [{"cycles", "caption"}].

    ⊕ fix round 1 (visual M2): screens are 2:1 (10 × 5 divisions), not
    4:3 — two 4:3 screens stacked made a figure taller than a phone, so the
    stem, the traces and the options could never be on screen together.
    With an odd number of rows the centre line is drawn on its own."""
    fs = q_font(W)
    dx, dy = divisions
    div = (W - 40) / float(dx)
    sh = div * dy
    block = fs + 10 + sh + 14
    H = int(14 + block * len(traces))
    c = Canvas(W, H)
    y = 14
    for t in traces:
        _q_text(c, W / 2, y + fs, t["caption"], fs, LBL, "bold")
        sy0 = y + fs + 12
        sx0 = 20
        _q_box(c, sx0, sy0, div*dx, sh, TINT["white"], ST, q_stroke(W, 2.5), 6)
        for i in range(1, dx):
            _q_line(c, sx0 + i*div, sy0, sx0 + i*div, sy0 + sh, "#D5CDB8",
                    q_stroke(W, 1.2), None, "butt")
        for j in range(1, dy):
            centre = dy % 2 == 0 and j == dy // 2
            col = "#8C8472" if centre else "#D5CDB8"
            _q_line(c, sx0, sy0 + j*div, sx0 + dx*div, sy0 + j*div, col,
                    q_stroke(W, 1.6 if centre else 1.2), None, "butt")
        if dy % 2:
            _q_line(c, sx0, sy0 + sh/2, sx0 + dx*div, sy0 + sh/2, "#8C8472",
                    q_stroke(W, 1.6), None, "butt")
        cy = sy0 + sh/2
        n = max(200, t["cycles"] * 40)
        pts = [(sx0 + dx*div*i/float(n),
                cy - amplitude*div*math.sin(2*math.pi*t["cycles"]*i/float(n)))
               for i in range(n + 1)]
        d = "M " + " L ".join("%.1f %.1f" % p for p in pts)
        c.S.append(f'<path d="{d}" fill="none" stroke="{ACC}" '
                   f'stroke-width="{q_stroke(W, 3)}" stroke-linejoin="round"/>')
        y += block
    return c.svg()


def crate_forces(forces, W=460, label=None):
    """A crate on the ground with horizontal forces acting on it, every
    arrow to ONE scale and on one line of action, each labelled with its
    size. `forces` is [{"newtons", "dir": "left"|"right"}]; nothing else is
    drawn — no resultant, no sum."""
    fs = q_font(W)
    H = 230
    c = Canvas(W, H)
    ground = H - 50
    size = 110
    cx = W / 2
    k = (W / 2 - size / 2 - 40) / float(max(f["newtons"] for f in forces))
    _q_line(c, 20, ground, W - 20, ground, ST, q_stroke(W, 3), None, "butt")
    for gx in range(34, int(W - 20), 26):
        _q_line(c, gx, ground, gx - 12, ground + 14, ST, q_stroke(W, 1.6),
                None, "butt")
    _q_box(c, cx - size/2, ground - size, size, size, TINT["sand"], ST, 3, 4)
    if label:
        _q_text(c, cx, ground - size/2 + fs*0.36, label, fs, LBL, "bold")
    y = ground - size / 2
    for f in forces:
        L = f["newtons"] * k
        if f["dir"] == "right":
            x0, x1 = cx + size/2, cx + size/2 + L
        else:
            x0, x1 = cx - size/2, cx - size/2 - L
        _q_arrow(c, x0, y, x1, y, RED, q_stroke(W, 5), 18)
        _q_text(c, (x0 + x1) / 2, y - 16, "%g N" % f["newtons"], fs, LBL,
                "bold")
    return c.svg()

# ====================================================================
# ⊕ MRB-352 run 2, batch 1 (KS3 physics) — five more question builders:
# force_grid, wave_line, longitudinal, bar_field here; graph_panels in
# charts.py. Specified in full by the examiner (spec174_ks3_physics.md,
# "New builders"); every departure from that text is marked ⊕ and says why.
# ====================================================================
from .style import text_width as _q_tw  # noqa: E402

_FORCE_GRID = "#948A70"    # ⊕ b1 fix: 3.0:1 on the card — squares are counted


def force_grid(arrows, caption=None, W=456, dot=None, **grid2d):
    """A box on squared paper with horizontal force arrows drawn a whole
    number of squares long — "forces drawn to scale" read by counting.
    `arrows` is [{"dir": "left"|"right", "squares": n, "label": str|None}].
    Nothing else is drawn: no resultant, no sum, no scale unless `caption`
    states one.

    ⊕ MRB-352 batch 4 (KS4 physics): with `dot` (a grid point) this is the
    two-dimensional form — arrows from a dot to grid points, a scale key,
    optional ground row — drawn by `ks4phys.force_grid_2d`. Without `dot`
    nothing here changes."""
    if dot is not None:
        from .ks4phys import force_grid_2d
        return force_grid_2d(arrows, dot, key=caption, **grid2d)
    # ⊕ b1 fix (examiner m2, visual 3): the grid is always ONE square wider
    # than the longest arrow on each side, so no arrow tip ever lands on
    # the frame, where it merges with the border and a pupil cannot tell
    # whether the arrow ends there. Up to 6 squares this is the old
    # 16-column grid, byte for byte; a 7-square arrow widens it to 18.
    longest = max([int(a["squares"]) for a in arrows] + [6])
    sq, rows, gx, gy = 26, 6, 20, 20
    cols = 2 * (longest + 1) + 2
    W = max(W, int(2 * gx + cols * sq))
    fs = q_font(W)
    H = int(gy + rows * sq + (40 if caption else 20))
    c = Canvas(W, H)
    # ⊕ b1 fix (visual 4): counting squares IS the task, so the grid is
    # drawn at 3:1 against the card (WCAG 1.4.11), not the faint house grid.
    grid = _FORCE_GRID
    for i in range(cols + 1):
        _q_line(c, gx + i * sq, gy, gx + i * sq, gy + rows * sq, grid,
                q_stroke(W, 1.2), None, "butt")
    for j in range(rows + 1):
        _q_line(c, gx, gy + j * sq, gx + cols * sq, gy + j * sq, grid,
                q_stroke(W, 1.2), None, "butt")
    _q_box(c, gx, gy, cols * sq, rows * sq, "none", ST, q_stroke(W, 2))
    bx0 = gx + (cols // 2 - 1) * sq
    bx1 = bx0 + 2 * sq
    by0 = gy + 2 * sq
    _q_box(c, bx0, by0, 2 * sq, 2 * sq, TINT["sand"], ST, 3)
    y = by0 + sq
    for a in arrows:
        n = a["squares"]
        if n != int(n) or not 1 <= n <= 7:
            raise ValueError("force_grid: an arrow is 1-7 whole squares, "
                             "not %r" % (n,))
        if a["dir"] == "left":
            x0, x1 = bx0, bx0 - n * sq
        elif a["dir"] == "right":
            x0, x1 = bx1, bx1 + n * sq
        else:
            raise ValueError("force_grid: dir is left or right")
        _q_arrow(c, x0, y, x1, y, RED, q_stroke(W, 5), 18)
        if a.get("label"):
            _q_text(c, (x0 + x1) / 2, y - sq + fs * 0.35, a["label"], fs, LBL,
                    "bold")
    if caption:
        _q_text(c, W / 2, gy + rows * sq + 14 + fs * 0.8, caption, fs, LBL,
                "bold")
    return c.svg()


def wave_line(cycles, start_phase=0.0, dots=(), dimension=None, W=460,
              H=220):
    """A transverse wave along a dashed centre line — no axes. `dots` are
    points on the curve (in cycles, u); `dimension` {from, to, label}
    measures along the wave between two u-positions, with dashed drop
    lines to a double-headed arrow under it."""
    fs = q_font(W)
    c = Canvas(W, H)
    x0, x1, yc, amp = 30.0, W - 30.0, 90.0, 40.0

    def X(u):
        return x0 + (x1 - x0) * u / float(cycles)

    def Y(u):
        return yc - amp * math.sin(2 * math.pi * (u + start_phase))

    _q_line(c, x0, yc, x1, yc, MUTED, q_stroke(W, 1.5), "6 6", "butt")
    n = int(max(40, 48 * cycles))
    pts = [(X(cycles * i / float(n)), Y(cycles * i / float(n)))
           for i in range(n + 1)]
    c.S.append('<polyline points="%s" fill="none" stroke="%s" '
               'stroke-width="%s" stroke-linecap="round" '
               'stroke-linejoin="round"/>'
               % (" ".join("%.1f,%.1f" % p for p in pts), ACC,
                  q_stroke(W, 3.5)))
    if dimension:
        ya = 165.0
        for u in (dimension["from"], dimension["to"]):
            _q_line(c, X(u), Y(u), X(u), ya + 8, MUTED, q_stroke(W, 1.5),
                    "5 5", "butt")
        xa, xb = X(dimension["from"]), X(dimension["to"])
        _dim_arrow(c, xa, xb, ya, W)
        _q_text(c, (xa + xb) / 2, ya + 30, dimension["label"], fs, LBL,
                "bold")
    for u in dots:
        c.S.append(f'<circle cx="{X(u):.1f}" cy="{Y(u):.1f}" r="7" '
                   f'fill="{ST}" stroke="none"/>')
    return c.svg()


def _dim_arrow(c, xa, xb, y, W, head=12):
    """A double-headed measuring arrow from xa to xb (heads are polygons,
    tips exactly on xa and xb)."""
    sw = q_stroke(W, 2.5)
    _q_line(c, xa + head, y, xb - head, y, ST, sw, None, "butt")
    for tip, back in ((xa, xa + head), (xb, xb - head)):
        c.S.append('<polygon points="%.1f,%.1f %.1f,%.1f %.1f,%.1f" '
                   'fill="%s" stroke="none"/>'
                   % (tip, y, back, y - head * 0.5, back, y + head * 0.5, ST))


def longitudinal(compressions, dimension=None, W=460, H=None, per_wave=12):
    """A sound wave drawn as a row of vertical lines, squeezed together at
    evenly spaced compressions and spread apart between them. The row
    starts 0.4 of a wavelength before the first compression and ends 0.4
    after the last, so each compression is a whole bunch. `dimension`
    {label} measures from the first compression's centre to the second's.
    No text but that label, no shading, no direction arrow."""
    n = int(compressions)
    if n < 2:
        raise ValueError("longitudinal: at least two compressions")
    fs = q_font(W)
    H = H or (190 if dimension else 150)
    c = Canvas(W, H)
    # ⊕ b1 fix (visual 2, examiner m3): the row runs 0.4 of a wavelength
    # past the first and last compressions, so every compression — the
    # two at the ends included — is a full, symmetric bunch rather than a
    # half-sliver at the edge. The dimension still runs centre to centre.
    pad = 0.4
    lam = (W - 60) / (n - 1 + 2 * pad)

    def X(u):
        return 30 + pad * lam + lam * (u - 0.12 * math.sin(2 * math.pi * u))

    for k in range(-per_wave, per_wave * n + 1):
        u = k / float(per_wave)
        if -pad - 1e-9 <= u <= (n - 1) + pad + 1e-9:
            _q_line(c, X(u), 30, X(u), 120, ST, q_stroke(W, 2.5), None, "butt")
    if dimension:
        xa, xb = X(0.0), X(1.0)
        _dim_arrow(c, xa, xb, 145, W)
        for x in (xa, xb):
            _q_line(c, x, 136, x, 154, ST, q_stroke(W, 2), None, "butt")
        _q_text(c, (xa + xb) / 2, 175, dimension["label"], fs, LBL, "bold")
    return c.svg()


# ── bar_field: the field of a bar magnet, traced, not drawn by eye ────────
# ⊕ b1 fix (visual 9): the pole points sit 10 units inside each end, not
# 20, and the catalogue's launch angles were re-spread, so the lines leave
# across the end region and fan out (the outermost from the corner and the
# end face), as in a textbook map — not all from one spot on the long face.
_BF_POLE_X = 90.0
_BF_POLES = ((1.0, -_BF_POLE_X), (-1.0, _BF_POLE_X))   # (+N, -S)
_BF_HALF_L, _BF_HALF_H = 100.0, 25.0


def _bf_dir(x, y):
    bx = by = 0.0
    for q, px in _BF_POLES:
        dx, dy = x - px, y
        r3 = (dx * dx + dy * dy) ** 1.5
        bx += q * dx / r3
        by += q * dy / r3
    m = math.hypot(bx, by)
    return bx / m, by / m


def _bf_inside(x, y):
    return abs(x) <= _BF_HALF_L and abs(y) <= _BF_HALF_H


def _bf_trace(angle, inside_panel, h=2.0, max_steps=6000):
    """RK4 along the unit field direction from the N pole point, launched
    at `angle` degrees (from +x towards S, anticlockwise = up). Returns
    (points in magnet coords, y up; closed) — closed when the trace comes
    within 22 units of the S pole point; not closed when it leaves the
    panel (`inside_panel(x, y)` false).

    ⊕ b1 fix: "closed" now means the trace has re-entered the magnet on
    its S half (it arrives at the S end), rather than coming within 22
    units of the S pole point — with the poles 10 units in, that radius
    reached 12 units BEYOND the end face, and a line along the axis would
    have stopped short of the magnet."""
    a = math.radians(angle)
    x, y = -_BF_POLE_X + math.cos(a), math.sin(a)
    pts = [(x, y)]
    for _ in range(max_steps):
        k1 = _bf_dir(x, y)
        k2 = _bf_dir(x + h / 2 * k1[0], y + h / 2 * k1[1])
        k3 = _bf_dir(x + h / 2 * k2[0], y + h / 2 * k2[1])
        k4 = _bf_dir(x + h * k3[0], y + h * k3[1])
        x += h / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0])
        y += h / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])
        if not inside_panel(x, y):
            return pts, False
        pts.append((x, y))
        if x > 0 and _bf_inside(x, y):
            return pts, True
    raise ValueError("bar_field: a %g° line neither closed nor left the "
                     "panel" % angle)


def _bf_outside_run(pts):
    """The first run of the trace outside the magnet body, with its ends
    moved onto the body's outline (linear interpolation), so a drawn line
    touches the magnet instead of stopping short of it."""
    run, started = [], False
    for i, p in enumerate(pts):
        if not _bf_inside(*p):
            if not started and i > 0:
                run.append(_bf_edge(pts[i - 1], p))
            started = True
            run.append(p)
        elif started:
            run.append(_bf_edge(p, pts[i - 1]))
            break
    return run


def _bf_edge(pin, pout):
    """The point on the body outline between an inside and an outside
    point (bisection — the outline is a rectangle, the step is 2 units)."""
    a, b = pin, pout
    for _ in range(30):
        m = ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2)
        if _bf_inside(*m):
            a = m
        else:
            b = m
    return b


def _arc(pts):
    out = [0.0]
    for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
        out.append(out[-1] + math.hypot(x1 - x0, y1 - y0))
    return out


def _at_length(pts, cum, s):
    """(point, unit direction) at arc length s along pts."""
    for i in range(1, len(pts)):
        if cum[i] >= s:
            (x0, y0), (x1, y1) = pts[i - 1], pts[i]
            seg = cum[i] - cum[i - 1] or 1.0
            t = (s - cum[i - 1]) / seg
            d = math.hypot(x1 - x0, y1 - y0) or 1.0
            return ((x0 + t * (x1 - x0), y0 + t * (y1 - y0)),
                    ((x1 - x0) / d, (y1 - y0) / d))
    (x0, y0), (x1, y1) = pts[-2], pts[-1]
    d = math.hypot(x1 - x0, y1 - y0) or 1.0
    return pts[-1], ((x1 - x0) / d, (y1 - y0) / d)


def _cut(pts, cum, s):
    out = [p for p, l in zip(pts, cum) if l < s]
    out.append(_at_length(pts, cum, s)[0])
    return out


def _wiggle(pts, amp, period):
    """Offset each point along the line's normal by amp·sin(2π s/period):
    the same path, drawn wavy."""
    cum = _arc(pts)
    out = []
    for i, (p, s) in enumerate(zip(pts, cum)):
        a, b = pts[max(0, i - 1)], pts[min(len(pts) - 1, i + 1)]
        d = math.hypot(b[0] - a[0], b[1] - a[1]) or 1.0
        nx, ny = -(b[1] - a[1]) / d, (b[0] - a[0]) / d
        w = amp * math.sin(2 * math.pi * s / period)
        out.append((p[0] + nx * w, p[1] + ny * w))
    return out


def _head(c, x, y, ux, uy, col, size=13):
    """A solid arrowhead centred on (x, y), pointing along (ux, uy) in
    canvas coordinates."""
    tx, ty = x + ux * size * 0.55, y + uy * size * 0.55
    bx, by = x - ux * size * 0.45, y - uy * size * 0.45
    nx, ny = -uy * size * 0.5, ux * size * 0.5
    c.S.append('<polygon points="%.1f,%.1f %.1f,%.1f %.1f,%.1f" fill="%s" '
               'stroke="none"/>' % (tx, ty, bx + nx, by + ny, bx - nx,
                                    by - ny, col))


_BF_AT = {"axis_left": (-1, 0), "axis_right": (1, 0),
          "above_centre": (0, 1), "below_centre": (0, -1)}


def bar_field(panels, W=460, panel_h=300, clip=False):
    """The magnetic field of a bar magnet (N left, S right), each line
    TRACED from a two-pole model (+1 and -1 at 20 units inside each end;
    B = Σ q r̂/r²) with RK4, launched from the N pole point at a given
    angle — so crowding at the poles is the physics, not a hand's guess.

    A panel is {"caption", "upper": [deg, ...], "lower": [deg, ...],
    "faulty": {angle, fraction, label} | None, "points": [...],
    "wavy": {amp, period} | None, "inside": n}. Lines are drawn only
    outside the magnet (it occludes them), each with one arrowhead at the
    middle of its drawn length, pointing N to S along the line.

      * `faulty` — one more line, drawn only for the first `fraction` of
        its length and ending in mid-air, lettered beyond its free end.
      * `points` — [{label, at, r}] with `at` one of axis_left, axis_right,
        above_centre, below_centre at r half-lengths from the centre; or
        [{label, x, y}] in half-lengths (x right, y up).
      * ⊕ `wavy` — every line drawn with a sinusoidal wiggle about its
        true path (a "drawn for effect" map), for p10-02-h21.
      * ⊕ `even` {n, step} — a student's evenly spaced map: n concentric
        semicircles above and below, radius step·k, from the N half to the S
        half, with no crowding anywhere (for p10-02-e25).
      * ⊕ `reversed` {angle, label} — one more COMPLETE line, N to S, with
        its arrowhead pointing back towards N (a student's error), lettered
        beside it a quarter of the way along, where clearest, or at
        `label_xy` (canvas units) when given (p10-02-h13).
      * ⊕ `inside` — n straight lines drawn INSIDE the magnet from the N end
        to the S end, arrowheads pointing to S (a student's addition), for
        p10-02-h26. Nothing is drawn inside the magnet otherwise.

    `clip` False: a correct line that leaves the panel is a BUILD ERROR (a
    clipped line would look like the faulty one). `clip` True: lines are
    cut at a 12-unit inner margin, as in any textbook field map.

    ⊕ A caption gets its own band above the panel (fs + 14 units), rather
    than sitting inside it: centred at the top of a 320 panel it landed on
    the outermost line, which peaks ~21 units below the panel's top edge."""
    fs = q_font(W)
    fsp = q_font(W, floor=22)
    bands = [(fs + 14 if p.get("caption") else 0) for p in panels]
    H = int(sum(panel_h + b for b in bands))
    c = Canvas(W, H)
    top = 0.0
    sw = q_stroke(W, 2.5)
    for p, band in zip(panels, bands):
        if p.get("caption"):
            _q_text(c, W / 2, top + fs + 4, p["caption"], fs, LBL, "bold")
        ptop = top + band
        cx, cy = W / 2.0, ptop + panel_h / 2.0
        m = 12.0

        def inside_panel(x, y, cx=cx, cy=cy, ptop=ptop):
            X, Y = cx + x, cy - y
            return m <= X <= W - m and ptop + m <= Y <= ptop + panel_h - m

        def C(q, cx=cx, cy=cy):
            return (cx + q[0], cy - q[1])

        # the marked points first: an arrowhead must keep clear of them
        dots = []
        for pt in p.get("points", []):
            if "at" in pt:
                ux, uy = _BF_AT[pt["at"]]
                px, py = ux * pt["r"] * _BF_HALF_L, uy * pt["r"] * _BF_HALF_L
            else:
                px, py = pt["x"] * _BF_HALF_L, pt["y"] * _BF_HALF_L
            dots.append((C((px, py)), pt["label"]))

        drawn = []          # (run, label, reversed-arrow)
        for ang in list(p.get("upper", [])) + list(p.get("lower", [])):
            pts, closed = _bf_trace(ang, inside_panel)
            if not closed and not clip:
                raise ValueError("bar_field: the %g° line leaves the panel "
                                 "before reaching S — raise panel_h, or pass "
                                 "clip=True" % ang)
            run = _bf_outside_run(pts)
            if len(run) < 2:
                continue
            drawn.append((run, None, False))
            if not closed:
                # ⊕ a line cut at the panel edge would have come round to S
                # off the card. The two-pole field is mirror-antisymmetric
                # (x -> -x reverses it), so the line arriving at S from off
                # the card is this one mirrored and reversed. Without it a
                # clipped map crowds lines at N and leaves S bare — which
                # reads as a stronger N pole than S (it is not).
                drawn.append(([(-x, y) for x, y in reversed(run)], None,
                              False))
        ev = p.get("even")
        if ev:
            # a student's EVENLY SPACED map: concentric semicircles on the
            # magnet's long faces, leaving the N half and entering the S
            # half — equally spaced everywhere, no crowding.
            # ⊕ b1 fix (visual 9): the OUTERMOST arch now starts at the
            # magnet's corner and each one inside it is `step` smaller, so
            # the arches leave near the ends (the innermost used to start
            # 20 units from the magnet's middle).
            for side in (1, -1):
                for k in range(int(ev["n"])):
                    r = _BF_HALF_L - ev["step"] * k
                    arc = [(-r * math.cos(math.pi * i / 90.0),
                            side * (_BF_HALF_H + r * math.sin(math.pi * i / 90.0)))
                           for i in range(91)]
                    drawn.append((arc, None, False))
        f = p.get("faulty")
        if f:
            pts, _ = _bf_trace(f["angle"], inside_panel)
            run = _bf_outside_run(pts)
            cum = _arc(run)
            run = _cut(run, cum, cum[-1] * f["fraction"])
            drawn.append((run, f.get("label"), False))
        rv = p.get("reversed")
        if rv:
            # ⊕ b1 fix (examiner m4): one COMPLETE line, N to S like the
            # rest, whose arrowhead points the wrong way — back towards N.
            pts, closed = _bf_trace(rv["angle"], inside_panel)
            if not closed:
                raise ValueError("bar_field: the reversed line must close")
            drawn.append((_bf_outside_run(pts), rv.get("label"), True))
        wv = p.get("wavy")
        allpts, heads, line_labels = [], [], []
        dot_xy = [xy for xy, _ in dots]
        for run, label, backwards in drawn:
            if wv:
                run = _wiggle(run, wv["amp"], wv["period"])
            cpts = [C(q) for q in run]
            allpts.extend(cpts)
            dec = cpts[::2] + ([cpts[-1]] if len(cpts) % 2 == 0 else [])
            c.S.append('<polyline points="%s" fill="none" stroke="%s" '
                       'stroke-width="%s" stroke-linecap="round" '
                       'stroke-linejoin="round"/>'
                       % (" ".join("%.1f,%.1f" % q for q in dec), ACC, sw))
            cum = _arc(cpts)
            # ⊕ b1 fix (visual 1, 7): the arrowhead goes at the middle of
            # the line unless that is within 18 units of a marked point or
            # of another line's arrowhead — then the nearest clear place
            # along the line. A dot no longer half-hides a head, and heads
            # on neighbouring lines no longer stack into a column.
            best = None
            for frac in (0.5, 0.42, 0.58, 0.35, 0.65, 0.28, 0.72):
                (hx, hy), (ux, uy) = _at_length(cpts, cum, cum[-1] * frac)
                clear = min([math.hypot(hx - a, hy - b)
                             for a, b in dot_xy + heads] + [99.0])
                if best is None or clear > best[0]:
                    best = (clear, hx, hy, ux, uy)
                if clear >= 18:
                    break
            _, hx, hy, ux, uy = best
            heads.append((hx, hy))
            if backwards:
                ux, uy = -ux, -uy
            _head(c, hx, hy, ux, uy, ACC)
            if label and not backwards:
                (ex, ey), (ux, uy) = _at_length(cpts, cum, cum[-1])
                d = 14 + fs * 0.5
                _q_text(c, ex + ux * d, ey + uy * d + fs * 0.35, label, fs,
                        LBL, "bold")
            elif label and rv.get("label_xy"):
                # ⊕ b1 fix 2 (visual R2): a hand-placed letter, set just
                # outside the loop it names
                lx, ly = rv["label_xy"]
                _q_text(c, lx, ly, label, fs, LBL, "bold")
            elif label:
                # lettered beside the line a quarter of the way along it,
                # wherever is clearest (placed with the point letters below)
                line_labels.append((_at_length(cpts, cum, cum[-1] * 0.25)[0],
                                    label))
        # the magnet, over the lines' inner ends
        _pole(c, cx - _BF_HALF_L, cy - _BF_HALF_H, _BF_HALF_L, 2 * _BF_HALF_H,
              "N", fsp)
        _pole(c, cx, cy - _BF_HALF_H, _BF_HALF_L, 2 * _BF_HALF_H, "S", fsp)
        n_in = int(p.get("inside", 0) or 0)
        for i in range(n_in):
            yy = cy - _BF_HALF_H + 2 * _BF_HALF_H * (i + 0.5) / n_in
            if n_in == 2:      # clear of the N/S letters and of the outline
                yy = cy + (-1 if i == 0 else 1) * 13
            _q_line(c, cx - _BF_HALF_L, yy, cx + _BF_HALF_L, yy, ACC, sw,
                    None, "butt")
            # ⊕ b1 fix (visual 8): 40% along from N, clear of the N|S join
            _head(c, cx - 0.2 * _BF_HALF_L, yy, 1.0, 0.0, ACC, 11)
        # obstacles a letter must keep clear of: every line, the magnet's
        # outline (sampled) and every dot
        obst = list(allpts)
        for k in range(41):
            fx = cx - _BF_HALF_L + 2 * _BF_HALF_L * k / 40.0
            obst += [(fx, cy - _BF_HALF_H), (fx, cy + _BF_HALF_H)]
        for k in range(11):
            fy = cy - _BF_HALF_H + 2 * _BF_HALF_H * k / 10.0
            obst += [(cx - _BF_HALF_L, fy), (cx + _BF_HALF_L, fy)]
        for (X, Y), _ in dots:
            obst += [(X + 7 * math.cos(a / 8.0 * math.pi),
                      Y + 7 * math.sin(a / 8.0 * math.pi)) for a in range(16)]
        for (X, Y), label in dots:
            c.S.append(f'<circle cx="{X:.1f}" cy="{Y:.1f}" r="7" '
                       f'fill="{ST}" stroke="none"/>')
            _bf_letter(c, X, Y, label, fs, obst,
                       (cx - _BF_HALF_L, cy - _BF_HALF_H, cx + _BF_HALF_L,
                        cy + _BF_HALF_H), (W, H))
        for (X, Y), label in line_labels:
            _bf_letter(c, X, Y, label, fs, obst,
                       (cx - _BF_HALF_L, cy - _BF_HALF_H, cx + _BF_HALF_L,
                        cy + _BF_HALF_H), (W, H))
        top = ptop + panel_h
    return c.svg()


def _bf_letter(c, X, Y, label, fs, lines, body, card=None):
    """Letter a point where it is clearest of every drawn line, the magnet
    and every dot, preferring above-left (the house position) when that is
    clear enough. A position on the magnet itself is never taken, nor
    (⊕ b1 fix, visual M1) one whose letter would touch or cross the card's
    edge — "A" used to sit on the top border of points-abcd."""
    tw = _q_tw(label, fs, True)
    best, best_d = None, -1.0
    base = [(-16, -12), (16, -12), (-16, 14 + fs * 0.7), (16, 14 + fs * 0.7),
            (0, -16), (0, 16 + fs * 0.7), (-22, 5), (22, 5)]
    cands = base + [(dx * 1.6, dy * 1.5) for dx, dy in base]
    for k, (dx, dy) in enumerate(cands):
        anchor_x = X + dx - (tw if dx < 0 else 0 if dx > 0 else tw / 2)
        box = (anchor_x - 3, Y + dy - fs * 0.75, anchor_x + tw + 3, Y + dy + 3)
        if (box[0] < body[2] and box[2] > body[0] and box[1] < body[3]
                and box[3] > body[1]):
            continue
        if card and (box[0] < 6 or box[1] < 6 or box[2] > card[0] - 6
                     or box[3] > card[1] - 6):
            continue
        d = min((max(box[0] - px, 0, px - box[2]) ** 2 +
                 max(box[1] - py, 0, py - box[3]) ** 2) ** 0.5
                for px, py in lines) if lines else 99.0
        if k == 0 and d >= 5:
            best = (dx, dy)
            break
        if d > best_d:
            best, best_d = (dx, dy), d
    dx, dy = best
    anchor = "end" if dx < 0 else "start" if dx > 0 else "middle"
    _q_text(c, X + dx, Y + dy, label, fs, LBL, "bold", anchor)
