"""ks4_art.circuits — the AQA GCSE physics circuit-symbol set.

Two things live here, because the coordinator's review of the 43
circuit-symbols rows this module ultimately serves found that a flat palette
of single symbols covers only about a third of them:

  1. THE SYMBOL PALETTE — one drawer per AQA symbol, used standalone for the
     "name this component" family of questions ("Which component is drawn
     as a rectangle with an arrow through it?").

  2. `_circuit(...)` — a PARAMETRISED whole-circuit drawer, because the
     majority of the confirmed rows describe a whole circuit and ask about
     it: a meter placed in series in a named branch, a meter bridged ACROSS
     a component, cell/battery orientation, a deliberate gap in a named wire
     ("one wire stops short of the cell"), a labelled component. A
     per-question hand-drawn circuit would be ~25 bespoke drawers and would
     not be maintainable; this is the one drawer that takes a topology and a
     component list instead.

Two accuracy points the audit turns on, checked against the AQA symbol
sheet:
  * the FUSE is a rectangle with a line running through/along it, extending
    slightly beyond both ends; the plain rectangle with no extra mark is the
    FIXED RESISTOR.
  * the THERMISTOR is a rectangle with a plain diagonal line through it, NO
    arrowhead. The VARIABLE RESISTOR is the same rectangle with the same
    diagonal, but WITH an arrowhead — the arrowhead is the only thing that
    tells the two apart. The LDR is a rectangle with two SEPARATE diagonal
    arrows pointing INTO it from outside (incident light), which is a
    different shape from either.

Every symbol is built from a fixed local coordinate frame — the component
lies along its own local x-axis, leads run out to +/-`_HALF`, and the body
sits within +/-`_BODY` — so the whole-circuit drawer can place one at any
point and any rotation with `<g transform="translate(...) rotate(...)">`
and get an identical drawing to the standalone symbol. Colour is never the
only channel telling two symbols apart: every distinguishing mark (an
arrowhead, a second arrow, a line's presence or absence) is drawn in plain
ink, the same ink every symbol uses, exactly as the AQA sheet does — the
sheet itself is monochrome, and re-introducing colour as a second AQA-sheet
convention nobody drew would be its own inaccuracy.

⚠️ ROTATION CONVENTION, so a caller does not have to re-derive it: components
are rotated with `rotate(-90)` to run vertically. Under that rotation, local
+x (a component's "right" lead) maps to global "up", and local -x ("left")
maps to global "down". So a cell drawn `orientation="long-left"` on a
vertical wire shows its long bar toward the BOTTOM of that wire.
"""

import math

from ks3_art.kit import (
    e, _n, _svg_open, _rect, _circle, _ellipse, _line, _path, _label,
    _SVG_INK, _SVG_INK_MUTED, _SVG_ACCENT_TEXT,
)

# ── the local coordinate frame every symbol is drawn in ───────────────────
_HALF = 28.0            # a component's total half-length along its own axis
_BODY = 13.0            # a rect/circle body's half-extent


def _leads(inner=_BODY):
    """The wire stubs either side of a body, out to the frame's edge."""
    return (_line(-_HALF, 0, -inner, 0, stroke=_SVG_INK, w=2.5)
            + _line(inner, 0, _HALF, 0, stroke=_SVG_INK, w=2.5))


def _arrowhead(x, y, angle_deg, size=6.5):
    """A filled triangle, tip at `(x, y)`, pointing along `angle_deg`
    (0deg = local +x, angle grows the SVG way since y already grows down)."""
    a1 = math.radians(angle_deg + 150)
    a2 = math.radians(angle_deg - 150)
    x1, y1 = x + size * math.cos(a1), y + size * math.sin(a1)
    x2, y2 = x + size * math.cos(a2), y + size * math.sin(a2)
    return _path("M %s,%s L %s,%s L %s,%s Z"
                 % (_n(x), _n(y), _n(x1), _n(y1), _n(x2), _n(y2)),
                 fill=_SVG_INK, stroke=None)


def _diagonal(x1, y1, x2, y2, arrow=False):
    """A straight line from `(x1,y1)` to `(x2,y2)`, with an optional
    arrowhead at the second point — the ONE difference between a variable
    resistor's diagonal and a thermistor's."""
    ang = math.degrees(math.atan2(y2 - y1, x2 - x1))
    out = _line(x1, y1, x2, y2, stroke=_SVG_INK, w=2.2)
    if arrow:
        out += _arrowhead(x2, y2, ang)
    return out


# ── the body drawers, one per AQA symbol ───────────────────────────────────

def _body_wire(**_kw):
    return _line(-_HALF, 0, _HALF, 0, stroke=_SVG_INK, w=2.5)


def _body_junction(**_kw):
    return _circle(0, 0, 3, fill=_SVG_INK)


def _body_cell(orientation="long-left", **_kw):
    flip = orientation == "long-right"
    long_x, short_x = (-4, 4) if not flip else (4, -4)
    return (_leads(inner=8)
            + _line(long_x, -11, long_x, 11, stroke=_SVG_INK, w=2)
            + _line(short_x, -6, short_x, 6, stroke=_SVG_INK, w=5))


def _body_battery(orientation="long-left", cells=2, **_kw):
    n = max(2, int(cells))
    flip = orientation == "long-right"
    span = 17.0
    step = (span * 2) / (2 * n - 1)
    xs = [-span + step * i for i in range(2 * n)]
    first = "long" if not flip else "short"
    bars = ""
    for i, x in enumerate(xs):
        kind = first if i % 2 == 0 else ("short" if first == "long" else "long")
        if kind == "long":
            bars += _line(x, -11, x, 11, stroke=_SVG_INK, w=2)
        else:
            bars += _line(x, -6, x, 6, stroke=_SVG_INK, w=5)
    return _leads(inner=span + 3) + bars


def _body_switch(state="open", **_kw):
    x1, x2 = -14.0, 14.0
    dots = _circle(x1, 0, 2.4, fill=_SVG_INK) + _circle(x2, 0, 2.4, fill=_SVG_INK)
    if state == "closed":
        lever = _line(x1, 0, x2, 0, stroke=_SVG_INK, w=2.2)
    elif state == "open":
        lever = _line(x1, 0, x1 + 22, -13, stroke=_SVG_INK, w=2.2)
    else:
        raise ValueError(
            "switch state %r is not drawn. Only 'open' and 'closed' are."
            % state)
    return (_line(-_HALF, 0, x1, 0, stroke=_SVG_INK, w=2.5)
            + _line(x2, 0, _HALF, 0, stroke=_SVG_INK, w=2.5) + dots + lever)


def _body_resistor(**_kw):
    return _leads() + _rect(-13, -9, 26, 18, stroke=_SVG_INK, w=2.5)


def _body_variable_resistor(**_kw):
    return (_leads() + _rect(-13, -9, 26, 18, stroke=_SVG_INK, w=2.5)
            + _diagonal(-16, 11, 15, -12, arrow=True))


def _body_thermistor(**_kw):
    # ⚠️ NOT a plain diagonal (that is the variable resistor, minus its
    # arrowhead, and the two are easy to confuse — MRB-352 coordinator
    # review). The AQA symbol is a line that enters at the LOWER LEFT, runs
    # along inside the rectangle, and turns UP at the right-hand end, with
    # no arrowhead anywhere on it.
    return (_leads() + _rect(-13, -9, 26, 18, stroke=_SVG_INK, w=2.5)
            + _path("M -13,7 L 10,7 L 10,-13", stroke=_SVG_INK, w=2.2))


def _body_ldr(**_kw):
    return (_leads() + _rect(-13, -9, 26, 18, stroke=_SVG_INK, w=2.5)
            + _diagonal(28, -22, 12, -9, arrow=True)
            + _diagonal(34, -14, 18, -1, arrow=True))


def _body_fuse(**_kw):
    return (_leads() + _rect(-13, -7, 26, 14, stroke=_SVG_INK, w=2.5)
            + _line(-19, 0, 19, 0, stroke=_SVG_INK, w=2))


def _body_lamp(**_kw):
    return (_leads() + _circle(0, 0, 13, stroke=_SVG_INK, w=2.5)
            + _line(-9.2, -9.2, 9.2, 9.2, stroke=_SVG_INK, w=2)
            + _line(-9.2, 9.2, 9.2, -9.2, stroke=_SVG_INK, w=2))


def _body_diode(**_kw):
    return (_leads(inner=10)
            + _path("M -10,-9 L -10,9 L 10,0 Z", stroke=_SVG_INK, w=2.2)
            + _line(10, -9, 10, 9, stroke=_SVG_INK, w=2.5))


def _body_led(**_kw):
    return (_body_diode()
            + _diagonal(1, -13, 8, -21, arrow=True)
            + _diagonal(7, -9, 14, -17, arrow=True))


def _meter(letter):
    def draw(**_kw):
        return (_leads() + _circle(0, 0, 13, stroke=_SVG_INK, w=2.5)
                + _label(0, 5, letter, size=15, weight="700", fill=_SVG_INK))
    return draw


_body_ammeter = _meter("A")
_body_voltmeter = _meter("V")
_body_motor = _meter("M")
_body_generator = _meter("G")


def _body_ac_supply(**_kw):
    return (_leads() + _circle(0, 0, 13, stroke=_SVG_INK, w=2.5)
            + _path("M -8,0 Q -4,-9 0,0 Q 4,9 8,0", stroke=_SVG_INK, w=2))


def _body_loudspeaker(**_kw):
    return (_leads()
            + _rect(-13, -7, 10, 14, stroke=_SVG_INK, w=2.2)
            + _path("M -3,-7 L 10,-13 L 10,13 L -3,7 Z", stroke=_SVG_INK, w=2.2))


def _body_microphone(**_kw):
    return (_leads()
            + _ellipse(0, -2, 8, 12, stroke=_SVG_INK, w=2.2)
            + _line(0, 10, 0, 16, stroke=_SVG_INK, w=2.2))


_BODY_FN = {
    "wire": _body_wire, "junction": _body_junction,
    "cell": _body_cell, "battery": _body_battery, "switch": _body_switch,
    "resistor": _body_resistor, "variable-resistor": _body_variable_resistor,
    "thermistor": _body_thermistor, "ldr": _body_ldr, "fuse": _body_fuse,
    "lamp": _body_lamp, "diode": _body_diode, "led": _body_led,
    "ammeter": _body_ammeter, "voltmeter": _body_voltmeter,
    "motor": _body_motor, "generator": _body_generator,
    "loudspeaker": _body_loudspeaker, "microphone": _body_microphone,
    "ac-supply": _body_ac_supply,
}

# The keyword each body drawer actually reads. `_component` uses this so a
# caller's stray key (a typo'd `stete=`) is silently dropped rather than
# raising deep inside a `**kw` some drawer never asked for.
_BODY_KW = {
    "cell": ("orientation",), "battery": ("orientation", "cells"),
    "switch": ("state",),
}


# ── one symbol, standalone (the "name this component" family) ─────────────

_SYM_W, _SYM_H = 160, 90


def _draw_symbol(fig, name, **kw):
    if name not in _BODY_FN:
        raise ValueError(
            "circuit symbol %r is not drawn. Known: %s."
            % (name, ", ".join(sorted(_BODY_FN))))
    inner = _BODY_FN[name](**kw)
    cx, cy = _SYM_W / 2.0, _SYM_H / 2.0
    g = '<g transform="translate(%s,%s)">%s</g>' % (_n(cx), _n(cy), inner)
    return _svg_open(fig, _SYM_W, _SYM_H) + g + "</svg>"


def draw_wire(fig):
    return _draw_symbol(fig, "wire")


def draw_junction(fig):
    return _draw_symbol(fig, "junction")


def draw_cell(fig):
    return _draw_symbol(fig, "cell", orientation=fig.get("orientation", "long-left"))


def draw_battery(fig):
    return _draw_symbol(fig, "battery",
                        orientation=fig.get("orientation", "long-left"),
                        cells=fig.get("cells", 2))


def draw_switch_open(fig):
    return _draw_symbol(fig, "switch", state="open")


def draw_switch_closed(fig):
    return _draw_symbol(fig, "switch", state="closed")


def draw_resistor(fig):
    return _draw_symbol(fig, "resistor")


def draw_variable_resistor(fig):
    return _draw_symbol(fig, "variable-resistor")


def draw_thermistor(fig):
    return _draw_symbol(fig, "thermistor")


def draw_ldr(fig):
    return _draw_symbol(fig, "ldr")


def draw_fuse(fig):
    return _draw_symbol(fig, "fuse")


def draw_lamp(fig):
    return _draw_symbol(fig, "lamp")


def draw_diode(fig):
    return _draw_symbol(fig, "diode")


def draw_led(fig):
    return _draw_symbol(fig, "led")


def draw_ammeter(fig):
    return _draw_symbol(fig, "ammeter")


def draw_voltmeter(fig):
    return _draw_symbol(fig, "voltmeter")


def draw_motor(fig):
    return _draw_symbol(fig, "motor")


def draw_generator(fig):
    return _draw_symbol(fig, "generator")


def draw_loudspeaker(fig):
    return _draw_symbol(fig, "loudspeaker")


def draw_microphone(fig):
    return _draw_symbol(fig, "microphone")


def draw_ac_supply(fig):
    return _draw_symbol(fig, "ac-supply")


# ── the whole-circuit drawer ────────────────────────────────────────────
#
# `loop` / `supply` / each branch's list is `[component, ...]`, where a
# component is `{"symbol": <name>, "id": str (optional, auto-assigned),
# "label": str (optional), plus whatever that symbol's own body reads —
# `orientation` for cell/battery, `cells` for battery, `state` for switch}`.
#
# `meters_across`: `[{"symbol": "voltmeter"|"ammeter", "target": <id>,
# "side": "auto"|<ignored today>}]` — a meter wired in PARALLEL with the
# named component, drawn as a small dashed bridge standing off the main
# wire, never merged into the main wire's own colour so a bridged meter
# reads as "an extra loop" rather than as part of the circuit it measures.
#
# `gap`: `{"after": <id> | "return"}` — a deliberate break in the wire
# immediately after that component (or, `"return"`, in the wire that runs
# back to the supply) — drawn as two bare ends that do not meet, for the
# "one wire stops short of the cell" family of stems, where the diagram
# must be drawable as WRONG on purpose.

def _auto_id(prefix, i):
    return "%s%d" % (prefix, i)


def _component(cx, cy, comp, rot, positions):
    name = comp.get("symbol")
    if name not in _BODY_FN:
        raise ValueError(
            "circuit component names unknown symbol %r. Known: %s."
            % (name, ", ".join(sorted(_BODY_FN))))
    kw = {k: comp[k] for k in _BODY_KW.get(name, ()) if k in comp}
    inner = _BODY_FN[name](**kw)
    out = ('<g transform="translate(%s,%s) rotate(%s)">%s</g>'
           % (_n(cx), _n(cy), _n(rot), inner))
    if comp.get("label"):
        lx, ly = (cx, cy + 26) if rot == 0 else (cx + 24, cy + 5)
        out += _label(lx, ly, comp["label"], size=13, fill=_SVG_INK_MUTED,
                      weight="600", anchor="middle" if rot == 0 else "start")
    cid = comp.get("id") or _auto_id("c", len(positions))
    if cid in positions:
        raise ValueError("circuit declares component id %r twice." % cid)
    positions[cid] = (cx, cy, rot)
    return out


def _bridge(target_pos, comp):
    """A meter in PARALLEL with the component at `target_pos` — two short
    dashed stubs to a small bridging wire carrying the meter, standing off
    the main wire so it reads as a separate loop rather than as part of the
    branch it measures."""
    cx, cy, rot = target_pos
    span, stand_off = _HALF - 6, 34
    if rot == 0:
        fx1, fx2, fy = cx - span, cx + span, cy - stand_off
        stubs = (_line(fx1, cy, fx1, fy, stroke=_SVG_ACCENT_TEXT, w=2, dash="4,3")
                 + _line(fx2, cy, fx2, fy, stroke=_SVG_ACCENT_TEXT, w=2, dash="4,3")
                 + _line(fx1, fy, fx2, fy, stroke=_SVG_ACCENT_TEXT, w=2, dash="4,3"))
        meter_xy, meter_rot = ((fx1 + fx2) / 2.0, fy), 0
    else:
        side = 1 if rot > 0 else -1
        fy1, fy2, fx = cy - span, cy + span, cx + side * stand_off
        stubs = (_line(cx, fy1, fx, fy1, stroke=_SVG_ACCENT_TEXT, w=2, dash="4,3")
                 + _line(cx, fy2, fx, fy2, stroke=_SVG_ACCENT_TEXT, w=2, dash="4,3")
                 + _line(fx, fy1, fx, fy2, stroke=_SVG_ACCENT_TEXT, w=2, dash="4,3"))
        meter_xy, meter_rot = (fx, (fy1 + fy2) / 2.0), 0
    dummy = {}
    meter = _component(meter_xy[0], meter_xy[1], comp, meter_rot, dummy)
    return stubs + meter


def _apply_meters_across(meters_across, positions):
    out = []
    for m in (meters_across or []):
        target = m.get("target")
        if target not in positions:
            raise ValueError(
                "a meter-across names target %r, which no component in this "
                "circuit declares as its `id`." % target)
        out.append(_bridge(positions[target], m))
    return out


def _wire_seg(x1, y1, x2, y2, broken_at_2=False):
    """One wire segment, optionally left unjoined at its second end — the
    deliberate-gap primitive every `gap` resolves to."""
    if not broken_at_2:
        return _line(x1, y1, x2, y2, stroke=_SVG_INK, w=2.5)
    short = 10.0
    dist = math.hypot(x2 - x1, y2 - y1) or 1.0
    ex = x1 + (x2 - x1) * (dist - short) / dist
    ey = y1 + (y2 - y1) * (dist - short) / dist
    return (_line(x1, y1, ex, ey, stroke=_SVG_INK, w=2.5)
            + _circle(ex, ey, 2.2, fill=_SVG_INK))


def _circuit_series(fig, width, height, loop, meters_across, gap):
    if not loop:
        raise ValueError(
            "_circuit %r: a series loop needs at least one component "
            "(conventionally the cell)." % fig.get("id"))
    for i, comp in enumerate(loop):
        comp.setdefault("id", _auto_id("c", i))
    pad = 34
    top, bottom = pad, height - pad
    left, right = pad + 8, width - pad
    mid_y = (top + bottom) / 2.0
    gap_after = (gap or {}).get("after")

    positions = {}
    out = []
    supply, rest = loop[0], loop[1:]
    out.append(_line(left, top, left, mid_y - _HALF, stroke=_SVG_INK, w=2.5))
    out.append(_line(left, mid_y + _HALF, left, bottom, stroke=_SVG_INK, w=2.5))
    out.append(_component(left, mid_y, supply, -90, positions))

    n = len(rest)
    step = (right - left) / float(n) if n else 0
    xs = [left + step * (i + 0.5) for i in range(n)]
    prev_x = left
    for i, (x, comp) in enumerate(zip(xs, rest)):
        broken = gap_after == comp.get("id")
        out.append(_wire_seg(prev_x, top, x - _HALF, top, broken_at_2=broken))
        out.append(_component(x, top, comp, 0, positions))
        prev_x = x + _HALF
    out.append(_wire_seg(prev_x, top, right, top,
                        broken_at_2=(gap_after == "top-end")))

    return_broken = gap_after == "return"
    out.append(_line(right, top, right, bottom, stroke=_SVG_INK, w=2.5))
    out.append(_wire_seg(right, bottom, left, bottom, broken_at_2=return_broken))

    out.extend(_apply_meters_across(meters_across, positions))
    return _svg_open(fig, width, height) + "".join(out) + "</svg>"


def _circuit_parallel(fig, width, height, supply, branches, meters_across, gap):
    if not supply:
        raise ValueError(
            "_circuit %r: a parallel circuit needs a `supply` list — at "
            "least the cell or battery on the left rail." % fig.get("id"))
    if not branches:
        raise ValueError(
            "_circuit %r: a parallel circuit needs at least one branch."
            % fig.get("id"))
    for i, comp in enumerate(supply):
        comp.setdefault("id", _auto_id("s", i))
    names = [bn for bn, _ in branches]
    if len(set(names)) != len(names):
        raise ValueError(
            "_circuit %r declares two branches with the same name." % fig.get("id"))
    for bn, comps in branches:
        for i, comp in enumerate(comps):
            comp.setdefault("id", "%s-%d" % (bn, i))

    pad = 34
    top, bottom = pad, height - pad
    left, right = pad + 8, width - pad
    gap_spec = gap or {}

    positions = {}
    out = []
    cell, extra = supply[0], supply[1:]
    mid_y = (top + bottom) / 2.0
    out.append(_line(left, top, left, mid_y - _HALF, stroke=_SVG_INK, w=2.5))
    out.append(_line(left, mid_y + _HALF, left, bottom, stroke=_SVG_INK, w=2.5))
    out.append(_component(left, mid_y, cell, -90, positions))

    n_branches = len(branches)
    branch_span = right - left
    xs = [left + branch_span * (i + 1) / float(n_branches) for i in range(n_branches)]

    m = len(extra)
    if m:
        step = (xs[0] - left) / float(m)
        ex = [left + step * (i + 0.5) for i in range(m)]
        prev_x = left
        for x, comp in zip(ex, extra):
            broken = gap_spec.get("after") == comp.get("id")
            out.append(_wire_seg(prev_x, top, x - _HALF, top, broken_at_2=broken))
            out.append(_component(x, top, comp, 0, positions))
            prev_x = x + _HALF
        out.append(_wire_seg(prev_x, top, xs[0], top,
                             broken_at_2=(gap_spec.get("after") == "top-end")))
    else:
        out.append(_wire_seg(left, top, xs[0], top,
                             broken_at_2=(gap_spec.get("after") == "top-end")))

    for i in range(1, n_branches):
        out.append(_line(xs[i - 1], top, xs[i], top, stroke=_SVG_INK, w=2.5))
    out.append(_line(xs[0], top, xs[0], top, stroke=_SVG_INK, w=0))  # no-op, keeps symmetry obvious

    bottom_xs_drawn = []
    for bn, comps in branches:
        x = xs[names.index(bn)]
        bx_broken = gap_spec.get("branch") == bn
        n_c = len(comps)
        if n_c == 0:
            out.append(_wire_seg(x, top, x, bottom,
                                broken_at_2=bx_broken and gap_spec.get("after") == "return"))
        else:
            step_y = (bottom - top) / float(n_c)
            ys = [top + step_y * (i + 0.5) for i in range(n_c)]
            prev_y = top
            for y, comp in zip(ys, comps):
                broken = bx_broken and gap_spec.get("after") == comp.get("id")
                out.append(_wire_seg(x, prev_y, x, y - _HALF, broken_at_2=broken))
                out.append(_component(x, y, comp, 90, positions))
                prev_y = y + _HALF
            out.append(_wire_seg(x, prev_y, x, bottom,
                                broken_at_2=(bx_broken and gap_spec.get("after") == "return")))
        bottom_xs_drawn.append(x)

    for x in bottom_xs_drawn:
        out.append(_line(x, bottom, x, bottom, stroke=_SVG_INK, w=0))  # explicit rail point
    out.append(_line(left, bottom, xs[-1], bottom, stroke=_SVG_INK, w=2.5))

    out.extend(_apply_meters_across(meters_across, positions))
    return _svg_open(fig, width, height) + "".join(out) + "</svg>"


def draw_circuit(fig):
    """The ART entry point: reads `fig["circuit"]`, a plain dict shaped
    `{"topology": "series"|"parallel", "loop": [...], "supply": [...],
    "branches": [[name, [...]], ...], "meters_across": [...], "gap": {...}}`
    — a plain-data description a catalogue record authors directly, kept
    OFF the `fig` dict's own top level so `fig["title"]`/`fig["desc"]` stay
    exactly where `_svg_open` and every other figure already expect them.
    """
    c = fig.get("circuit") or {}
    topology = c.get("topology")
    width, height = fig.get("w", 420), fig.get("h", 260)
    if topology == "series":
        return _circuit_series(fig, width, height, list(c.get("loop") or []),
                               c.get("meters_across"), c.get("gap"))
    if topology == "parallel":
        return _circuit_parallel(
            fig, width, height, list(c.get("supply") or []),
            [(bn, list(comps)) for bn, comps in (c.get("branches") or [])],
            c.get("meters_across"), c.get("gap"))
    raise ValueError(
        "_circuit %r asked for topology %r. Only 'series' and 'parallel' "
        "are drawn." % (fig.get("id"), topology))


ART = {
    "circuit-symbol-wire": draw_wire,
    "circuit-symbol-junction": draw_junction,
    "circuit-symbol-cell": draw_cell,
    "circuit-symbol-battery": draw_battery,
    "circuit-symbol-switch-open": draw_switch_open,
    "circuit-symbol-switch-closed": draw_switch_closed,
    "circuit-symbol-resistor": draw_resistor,
    "circuit-symbol-variable-resistor": draw_variable_resistor,
    "circuit-symbol-thermistor": draw_thermistor,
    "circuit-symbol-ldr": draw_ldr,
    "circuit-symbol-fuse": draw_fuse,
    "circuit-symbol-lamp": draw_lamp,
    "circuit-symbol-diode": draw_diode,
    "circuit-symbol-led": draw_led,
    "circuit-symbol-ammeter": draw_ammeter,
    "circuit-symbol-voltmeter": draw_voltmeter,
    "circuit-symbol-motor": draw_motor,
    "circuit-symbol-generator": draw_generator,
    "circuit-symbol-loudspeaker": draw_loudspeaker,
    "circuit-symbol-microphone": draw_microphone,
    "circuit-symbol-ac-supply": draw_ac_supply,
    "circuit": draw_circuit,
}


if __name__ == "__main__":
    import xml.etree.ElementTree as ET

    def _check(name, svg):
        ET.fromstring(svg)
        print("ok: %-38s %6d bytes" % (name, len(svg)))

    for art_name, fn in ART.items():
        if art_name == "circuit":
            continue
        _check(art_name, fn({"id": "sc-%s" % art_name, "title": "t", "desc": "d"}))

    _check("circuit/series loop (h23-shaped)", draw_circuit({
        "id": "sc-series", "title": "t", "desc": "d",
        "circuit": {
            "topology": "series",
            "loop": [
                {"symbol": "cell", "id": "cell"},
                {"symbol": "ammeter", "id": "amm", "label": "A"},
                {"symbol": "variable-resistor", "id": "vr"},
                {"symbol": "lamp", "id": "lamp"},
            ],
        }}))

    _check("circuit/series with a gap (s21-shaped)", draw_circuit({
        "id": "sc-gap", "title": "t", "desc": "d",
        "circuit": {
            "topology": "series",
            "loop": [{"symbol": "cell", "id": "cell"},
                    {"symbol": "fuse", "id": "fuse"},
                    {"symbol": "lamp", "id": "lamp"}],
            "gap": {"after": "return"},
        }}))

    _check("circuit/voltmeter bridging a resistor (h07-shaped)", draw_circuit({
        "id": "sc-bridge", "title": "t", "desc": "d",
        "circuit": {
            "topology": "series",
            "loop": [{"symbol": "cell", "id": "cell"},
                    {"symbol": "ammeter", "id": "amm"},
                    {"symbol": "resistor", "id": "r1"}],
            "meters_across": [{"symbol": "voltmeter", "target": "r1"}],
        }}))

    _check("circuit/parallel two branches (h04-shaped)", draw_circuit({
        "id": "sc-parallel", "title": "t", "desc": "d", "w": 460, "h": 300,
        "circuit": {
            "topology": "parallel",
            "supply": [{"symbol": "battery", "id": "bat"},
                      {"symbol": "switch", "id": "sw", "state": "closed"},
                      {"symbol": "ammeter", "id": "amm-total", "label": "total"}],
            "branches": [
                ("lamp-branch", [{"symbol": "lamp", "id": "lamp1"}]),
                ("motor-branch", [{"symbol": "motor", "id": "motor1"}]),
            ],
            "meters_across": [{"symbol": "voltmeter", "target": "lamp1"}],
        }}))

    print("circuits.py self-check: every symbol and every sample circuit "
          "renders well-formed SVG")
