"""figlib.ks4phys — question builders for KS4 physics (MRB-352 run 2, batch 4).

Specified by the examiner in `spec174_ks4_physics_other.md` ("Builders"),
drawn in the library's style: its STYLE, its Canvas, its primitives, text
sizes from `q_font(W)`, arrowheads as polygons, no <g>, no class, no
opacity. They live in their own module, registered into `figlib.ART` by
`ART_KS4PHYS` below, so batches editing `figlib` in parallel cannot collide
in one file (the same shape as batch 2's `biochem.py`).

Every builder is parametrised; none draws an answer. What each must NEVER
draw (a resultant, a needle, a pole letter on a solenoid, a label on a
graph section, …) is said in its docstring, and the catalogue records rely
on that.

Departures from the spec's text, each marked ⊕ below:
  * `magnet_compasses` colours the magnet with the library's own `_pole`
    (N salmon, S blue) rather than the spec's sand/blue, so a KS4 magnet
    looks like every other magnet figlib draws.
  * `free_body` wraps a label that would run off the card onto a second
    line at the same tip (the parachutist's "pull of the parachute" on the
    spec's 380-wide canvas).
  * `magnet_compasses` direction key: the spec's origin (400, 210) puts the
    "east" label off the right edge of a 460 card; the key's origin is a
    parameter and the record moves it left.
"""

import math

from .style import (MUTED, STYLE, TINT, Canvas, arrow, box, line, q_font,
                    q_stroke, text, text_width)

ST = STYLE["stroke"]
LBL = STYLE["label"]
ACC = STYLE["arrow"]
CREAM = STYLE["cream"]
GRID_INK = "#948A70"       # the batch-1 force grid: 3.0:1 on the card
WIDE = 1.15                # Georgia table -> widest fallback face, for layout


def _tw(s, fs, bold=True):
    return text_width(s, fs, bold) * WIDE


def _poly(c, pts, fill, stroke="none", width=0):
    sw = f' stroke-width="{width}"' if stroke != "none" else ""
    c.S.append('<polygon points="%s" fill="%s" stroke="%s"%s '
               'stroke-linejoin="round"/>'
               % (" ".join("%.1f,%.1f" % p for p in pts), fill, stroke, sw))


def _mid_head(c, x0, y0, x1, y1, col, head=14):
    """A solid arrowhead at the midpoint of a segment, pointing along it."""
    ang = math.atan2(y1 - y0, x1 - x0)
    mx, my = (x0 + x1) / 2, (y0 + y1) / 2
    tx, ty = mx + math.cos(ang) * head / 2, my + math.sin(ang) * head / 2
    bx, by = tx - head * math.cos(ang), ty - head * math.sin(ang)
    nx, ny = -math.sin(ang) * head * 0.5, math.cos(ang) * head * 0.5
    _poly(c, [(tx, ty), (bx + nx, by + ny), (bx - nx, by - ny)], col)


def _label_lines(c, x, y, lines, fs, anchor, fill=LBL, pitch=1.25):
    for k, ln in enumerate(lines):
        text(c, x, y + k * fs * pitch, ln, fs, fill, "bold", anchor)


# ── force-grid, two-dimensional ───────────────────────────────────────────

def _backed(c, x, y, txt, fs, anchor):
    """⊕ b4 fix (visual 4): a label on a paper-coloured patch, so it never
    sits on a grid line. The patch is only as big as the label's own box."""
    w = _tw(txt, fs)
    x0 = {"start": x, "middle": x - w / 2, "end": x - w}[anchor]
    box(c, x0 - 3, y - fs * 0.85, w + 6, fs * 1.1, CREAM, "none", 0)
    text(c, x, y, txt, fs, LBL, "bold", anchor)


_SIDES = {
    "left": (-1, 0), "right": (1, 0), "above": (0, -1), "below": (0, 1),
    "upper-left": (-1, -1), "upper-right": (1, -1),
    "lower-left": (-1, 1), "lower-right": (1, 1),
}


def force_grid_2d(arrows, dot, cols, rows, side=40, key=None,
                  ground_row=None, ground_label="ground", margin=20):
    """Forces drawn TO SCALE on squared paper, from one dot at a grid
    point, each to a grid point — "use vector diagrams … (scale drawings
    only)", AQA 8463 §4.5.1.4. Grid points count from the BOTTOM-LEFT
    corner. `arrows` is [{"to": (gx, gy), "label", "label_side"}], ink,
    polygon heads. `key` is written under the grid ("1 square = 10 N").
    `ground_row` draws a solid ground line along that grid row, the full
    width, hatched below, with `ground_label` at its right end.

    NEVER drawn: a component, a projection, a resultant, a completed
    triangle, a parallelogram, an angle mark — reading the grid is the
    task. Reached through `physics.force_grid(..., dot=…)` so there is ONE
    force-grid art; the batch-1 horizontal form is untouched."""
    W = int(2 * margin + cols * side)
    fs = q_font(W)
    top = margin
    gh = rows * side
    H = int(top + gh + (fs * 2.4 if key else margin))
    c = Canvas(W, H)
    x0, yb = margin, top + gh

    def G(gx, gy):
        return x0 + gx * side, yb - gy * side

    for i in range(cols + 1):
        line(c, x0 + i * side, top, x0 + i * side, yb, GRID_INK,
             q_stroke(W, 1.2), None, "butt")
    for j in range(rows + 1):
        line(c, x0, top + j * side, x0 + cols * side, top + j * side,
             GRID_INK, q_stroke(W, 1.2), None, "butt")
    box(c, x0, top, cols * side, gh, "none", ST, q_stroke(W, 2))

    if ground_row is not None:
        gx0, gy0 = G(0, ground_row)
        gx1 = x0 + cols * side
        # ⊕ b4 fix (examiner m3): hatching runs the FULL width; the label
        # sits under it, on a paper patch, inside the row below the ground.
        hx = gx0 + 4
        while hx + 8 <= gx1 - 2:
            line(c, hx + 8, gy0 + 2, hx, gy0 + 10, ST, q_stroke(W, 1.6))
            hx += 14
        line(c, gx0, gy0, gx1, gy0, ST, q_stroke(W, 4), None, "butt")
        _backed(c, gx1 - 6, gy0 + fs + 8, ground_label, fs, "end")

    ox, oy = G(*dot)
    sw = q_stroke(W, 4)
    for a in arrows:
        tx, ty = G(*a["to"])
        arrow(c, ox, oy, tx, ty, ST, sw, 18)
        if a.get("label"):
            ux, uy = _SIDES[a.get("label_side", "upper-left")]
            n = math.hypot(ux, uy)
            ux, uy = ux / n, uy / n
            mx, my = (ox + tx) / 2, (oy + ty) / 2
            lw = _tw(a["label"], fs)
            # push the label's centre out until its box clears the arrow
            dist = side * 0.35 + abs(ux) * lw / 2 + abs(uy) * fs * 0.6
            cx, cy = mx + ux * dist, my + uy * dist
            _backed(c, cx, cy + fs * 0.35, a["label"], fs, "middle")
    c.S.append(f'<circle cx="{ox:.1f}" cy="{oy:.1f}" r="7" fill="{ST}" '
               f'stroke="none"/>')
    if key:
        text(c, W / 2, yb + fs * 1.6, key, fs, LBL, "bold")
    return c.svg()


# ── free body diagram ─────────────────────────────────────────────────────

def free_body(obj, arrows, W=360, H=360):
    """An object — {"kind": "dot", "at": (x, y), "r"} or {"kind": "square",
    "at": (cx, cy), "size"} — and its forces as arrows
    [{"from": (x, y), "dx", "dy", "label", "label_side": "right"|"left"}],
    each labelled at its TIP. All arrows are ink and the same weight, so
    no arrow is singled out. NEVER drawn: a resultant, "= 0", a picture of
    the real object. ⊕ A label too long for the card beside its tip is
    wrapped onto a second line there."""
    fs = q_font(W)
    c = Canvas(W, H)
    sw = q_stroke(W, 4)
    for a in arrows:
        fx, fy = a["from"]
        tx, ty = fx + a.get("dx", 0), fy + a.get("dy", 0)
        arrow(c, fx, fy, tx, ty, ST, sw, 16)
        lab = a.get("label")
        if not lab:
            continue
        right = a.get("label_side", "right") == "right"
        lx = tx + 10 if right else tx - 10
        room = (W - 8 - lx) if right else (lx - 8)
        lines = [lab]
        if _tw(lab, fs) > room:
            words, lines, cur = lab.split(), [], ""
            for w_ in words:
                t_ = (cur + " " + w_).strip()
                if cur and _tw(t_, fs) > room:
                    lines.append(cur)
                    cur = w_
                else:
                    cur = t_
            lines.append(cur)
        _label_lines(c, lx, ty + fs * 0.35, lines, fs,
                     "start" if right else "end")
    kind = obj.get("kind", "dot")
    cx, cy = obj["at"]
    if kind == "dot":
        c.S.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{obj.get("r", 7)}" '
                   f'fill="{ST}" stroke="none"/>')
    elif kind == "square":
        s = obj.get("size", 40)
        box(c, cx - s / 2, cy - s / 2, s, s, TINT["white"], ST, q_stroke(W, 3))
    else:
        raise ValueError("free_body: object kind is dot or square")
    return c.svg()


# ── a bar magnet with plotting-compass positions ──────────────────────────

def magnet_compasses(magnet, compasses, W=460, H=240, key=None, r=18):
    """A bar magnet — {"x0", "x1", "y0", "y1", "left": "S"|"N"}, two
    halves lettered N and S — and plotting compasses drawn as EMPTY circles
    at `compasses` [{"at": (x, y), "label", "label_pos": "upper-right"|
    "lower-right"|"above"|…}]. `key` {"at": (x, y), "len"} adds a
    direction key: an arrow up to "north" and an arrow right to "east".
    NEVER drawn: a needle, a field line, a field arrow — where each needle
    points is the answer."""
    from .physics import _pole
    fs = q_font(W)
    c = Canvas(W, H)
    x0, x1, y0, y1 = magnet["x0"], magnet["x1"], magnet["y0"], magnet["y1"]
    left = magnet.get("left", "S")
    right = "N" if left == "S" else "S"
    half = (x1 - x0) / 2.0
    pf = max(fs, int((y1 - y0) * 0.5))
    _pole(c, x0, y0, half, y1 - y0, left, pf)
    _pole(c, x0 + half, y0, half, y1 - y0, right, pf)
    for cp in compasses:
        cx, cy = cp["at"]
        c.S.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r}" '
                   f'fill="{TINT["white"]}" stroke="{ST}" '
                   f'stroke-width="{q_stroke(W, 2.5)}"/>')
        lab = cp.get("label")
        if lab:
            pos = cp.get("label_pos", "upper-right")
            d = r + 6
            if pos == "above":
                text(c, cx, cy - d - 2, lab, fs, LBL, "bold")
            elif pos == "below":
                text(c, cx, cy + d + fs * 0.8, lab, fs, LBL, "bold")
            elif pos == "upper-right":
                text(c, cx + d * 0.75, cy - d * 0.75, lab, fs, LBL, "bold",
                     "start")
            elif pos == "lower-right":
                text(c, cx + d * 0.75, cy + d * 0.75 + fs * 0.7, lab, fs, LBL,
                     "bold", "start")
            else:
                raise ValueError("magnet_compasses: label_pos %r" % pos)
    if key:
        kx, ky = key["at"]
        n = key.get("len", 30)
        sw = q_stroke(W, 2.5)
        arrow(c, kx, ky, kx, ky - n, ST, sw, 11)
        arrow(c, kx, ky, kx + n, ky, ST, sw, 11)
        text(c, kx, ky - n - 7, "north", fs, LBL, "bold")
        text(c, kx + n + 6, ky + fs * 0.35, "east", fs, LBL, "bold", "start")
    return c.svg()


# ── a solenoid, front solid and back dashed, with the current marked ──────

def solenoid(turns=6, pitch=50, radius=60, x0=90, axis_y=130,
             current="down-front", lead=60, W=480, H=300, key=True):
    """A coil with a horizontal axis. Each turn's FRONT is a solid stroke
    from the top to the bottom of the coil, slanting half a pitch to the
    right, with an arrowhead at its middle; its BACK is a dashed stroke up
    to the next turn's top. A lead joins each end, with an arrowhead.

    `current` "down-front": the current runs DOWN each front stroke (so
    over the top it comes towards the viewer) and the leads point right.
    Right-hand grip: fingers down the front and towards you over the top,
    thumb to the RIGHT — so the field inside points right and the RIGHT
    end is north. "up-front" is the reverse of all of it.

    NEVER drawn: N or S, field lines, a compass, a hand, a core, a cell."""
    if current not in ("down-front", "up-front"):
        raise ValueError("solenoid: current is down-front or up-front")
    fs = q_font(W)
    c = Canvas(W, H)
    top, bot = axis_y - radius, axis_y + radius
    down = current == "down-front"
    xa = x0
    xz = x0 + turns * pitch
    sw_f, sw_b = q_stroke(W, 3), q_stroke(W, 2)
    for k in range(turns):
        fx0, fx1 = x0 + k * pitch, x0 + k * pitch + pitch / 2.0
        line(c, fx1, bot, x0 + (k + 1) * pitch, top, ST, sw_b, "6 5", "butt")
    for k in range(turns):
        fx0, fx1 = x0 + k * pitch, x0 + k * pitch + pitch / 2.0
        line(c, fx0, top, fx1, bot, ST, sw_f)
        if down:
            _mid_head(c, fx0, top, fx1, bot, ST, 16)
        else:
            _mid_head(c, fx1, bot, fx0, top, ST, 16)
    for (ax, bx) in ((xa - lead, xa), (xz, xz + lead)):
        line(c, ax, top, bx, top, ST, sw_f)
        if down:
            _mid_head(c, ax, top, bx, top, ST, 16)
        else:
            _mid_head(c, bx, top, ax, top, ST, 16)
    if key:
        ky = H - 38
        items = (("front of each turn", None), ("back of each turn", "6 5"))
        widths = [30 + 8 + _tw(t, fs) for t, _ in items]
        gap = 28
        x = (W - (sum(widths) + gap)) / 2
        for (t, dash), w_ in zip(items, widths):
            line(c, x, ky - fs * 0.35, x + 30, ky - fs * 0.35, ST,
                 sw_f if dash is None else sw_b, dash, "butt")
            text(c, x + 38, ky, t, fs, LBL, "bold", "start")
            x += w_ + gap
    return c.svg()


# ── nuclear notation ──────────────────────────────────────────────────────

def nuclide(symbol, mass, atomic, W=240, H=150, size=72, num=28):
    """A nuclear symbol: the element symbol, its mass number at the upper
    left and its atomic number at the lower left, right-aligned to one x —
    AQA 8463 §4.4.1.2's own notation. NEVER drawn: "mass number", "atomic
    number", "protons", "neutrons", leader lines, the element's name."""
    from .style import NUM_FONT
    c = Canvas(W, H)
    sym_w = text_width(symbol, size, True)
    num_w = max(len(str(mass)), len(str(atomic))) * 0.60 * num
    gap = 8
    total = num_w + gap + sym_w
    xs = (W - total) / 2 + num_w + gap          # symbol's left edge
    base = H / 2 + size * 0.69 / 2              # symbol baseline, centred
    cap_top = base - size * 0.69
    xn = xs - gap
    c.S.append(f'<text x="{xs:.1f}" y="{base:.1f}" font-family="Georgia, serif" '
               f'font-size="{size}" font-weight="700" fill="{ST}" '
               f'text-anchor="start">{symbol}</text>')
    for val, y in ((mass, cap_top + num * 0.66), (atomic, base)):
        c.S.append(f'<text x="{xn:.1f}" y="{y:.1f}" font-family="{NUM_FONT}" '
                   f'font-size="{num}" font-weight="400" fill="{ST}" '
                   f'text-anchor="end">{val}</text>')
    return c.svg()


# ── a Sankey diagram with one output turning down ─────────────────────────

def sankey_simple(scale=2.0, energy_in=100, useful=35, x_in=30, x_split=190,
                  x_useful_end=410, y_top=50, drop_end=320,
                  labels=None, W=480, H=380, tints=("sand", "mint", "salmon"),
                  tip=35):
    """A Sankey diagram to scale (`scale` px per joule): an input band on
    the left; a useful band carrying straight on to the right; a wasted
    band turning down; each ending in a point. No internal line where the
    input band meets the other two — the tints meet there. `labels` is
    {"in": [...], "useful": [...], "wasted": [...]}, each a list of lines
    written inside its band. NEVER drawn: a scale bar or grid, a
    percentage, "efficiency" — unless a label says so."""
    wasted = energy_in - useful
    fs = q_font(W)
    c = Canvas(W, H)
    h_in = energy_in * scale
    h_u = useful * scale
    w_w = wasted * scale
    y_u1 = y_top + h_u
    x_w1 = x_split + w_w
    tip_u = tip_w = tip      # both points 35 deep, as the spec draws them
    tin, tu, tw_ = (TINT[t] for t in tints)
    # fills, no stroke
    _poly(c, [(x_in, y_top), (x_split, y_top), (x_split, y_top + h_in),
              (x_in, y_top + h_in)], tin)
    _poly(c, [(x_split, y_top), (x_useful_end, y_top),
              (x_useful_end + tip_u, y_top + h_u / 2), (x_useful_end, y_u1),
              (x_split, y_u1)], tu)
    _poly(c, [(x_split, y_u1), (x_w1, y_u1), (x_w1, drop_end),
              (x_split + w_w / 2, drop_end + tip_w), (x_split, drop_end)], tw_)
    # the outline of the whole shape, then the split between the outputs
    outline = [(x_in, y_top), (x_useful_end, y_top),
               (x_useful_end + tip_u, y_top + h_u / 2), (x_useful_end, y_u1),
               (x_w1, y_u1), (x_w1, drop_end),
               (x_split + w_w / 2, drop_end + tip_w), (x_split, drop_end),
               (x_split, y_top + h_in), (x_in, y_top + h_in)]
    _poly(c, outline, "none", ST, q_stroke(W, 2))
    line(c, x_split, y_u1, x_w1, y_u1, ST, q_stroke(W, 2), None, "butt")
    labels = labels or {}
    pitch = 1.3

    def block(lines, cx, cy):
        n = len(lines)
        y0 = cy - (n - 1) * fs * pitch / 2 + fs * 0.35
        _label_lines(c, cx, y0, lines, fs, "middle", ST, pitch)

    block(labels.get("in", []), (x_in + x_split) / 2, y_top + h_in / 2)
    block(labels.get("useful", []), (x_split + x_useful_end) / 2,
          y_top + h_u / 2)
    block(labels.get("wasted", []), (x_split + x_w1) / 2,
          (y_u1 + drop_end) / 2)
    return c.svg()


# ── an echo-sounder display ──────────────────────────────────────────────

def echo_sounder(seabed, patch, W=480, H=320, screen=(70, 20, 460, 270),
                 depth_max=50, depth_step=10, patch_label="X"):
    """An echo sounder's screen: depth down the side (0 at the top),
    "distance travelled by the boat →" underneath with no numbers. The
    seabed is a thick ink line through `seabed` (depths at evenly spaced
    points across the screen), labelled "seabed". `patch` is
    {"dashes": [(x_frac, depth, length_px), ...], "label_depth"} — short
    faint grey dashes, labelled X to their right. NEVER drawn: a fish, a
    colour scale, any mark at depth 0."""
    from .charts import _num_size
    fs = q_font(W)
    fn = _num_size(fs)
    c = Canvas(W, H)
    sx0, sy0, sx1, sy1 = screen
    ppm = (sy1 - sy0) / float(depth_max)

    def X(fr):
        return sx0 + (sx1 - sx0) * fr

    def Y(d):
        return sy0 + ppm * d

    box(c, sx0, sy0, sx1 - sx0, sy1 - sy0, CREAM, ST, q_stroke(W, 2.5))
    for d in range(0, depth_max + 1, depth_step):
        line(c, sx0 - 7, Y(d), sx0, Y(d), ST, q_stroke(W, 2))
        text(c, sx0 - 11, Y(d) + fn * 0.35, str(d), fn, LBL, "normal", "end")
    text(c, fs + 4, (sy0 + sy1) / 2, "depth / m", fs, LBL, "bold", "middle",
         rotate=-90)
    text(c, (sx0 + sx1) / 2, sy1 + 16 + fn * 0.35 + fs,
         "distance travelled by the boat →", fs, LBL, "bold")
    n = len(seabed) - 1
    pts = [(X(i / float(n)), Y(d)) for i, d in enumerate(seabed)]
    c.S.append('<polyline points="%s" fill="none" stroke="%s" '
               'stroke-width="%s" stroke-linecap="round" '
               'stroke-linejoin="round"/>'
               % (" ".join("%.1f,%.1f" % p for p in pts), ST, q_stroke(W, 5)))
    top_right = min(Y(seabed[-1]), Y(seabed[-2]))
    text(c, sx1 - 8, top_right - 14, "seabed", fs, ST, "bold", "end")
    right = 0
    for fr, d, ln in patch["dashes"]:
        xa = X(fr)
        line(c, xa, Y(d), xa + ln, Y(d), "#858585", q_stroke(W, 3), None,
             "butt")
        right = max(right, xa + ln)
    text(c, right + 10, Y(patch["label_depth"]) + fs * 0.35, patch_label, fs,
         ST, "bold", "start")
    return c.svg()


# ── a wave front diagram (refraction at a boundary) ───────────────────────

def wavefront_diagram(i_deg=40, r_deg=60, O=(210, 190), incident_len=150,
                      refracted_len=150, incident_fronts=(30, 66, 102, 138),
                      refracted_fronts=(55, 75, 95, 115), front_len=50,
                      W=420, H=380, labels=("material 1", "material 2"),
                      incident_head_at=None, refracted_head_at=None):
    """A ray meeting a horizontal boundary at O, with a dashed normal, and
    its wave fronts drawn at right angles to it — `incident_fronts` and
    `refracted_fronts` are distances from O along each ray. The angles are
    free parameters, so a STUDENT'S wrong diagram can be drawn exactly.
    Wave fronts teal, rays ink. NEVER drawn: an angle arc or value, "fast",
    "slow", a tick or a cross. No front may cross the boundary (refused)."""
    fs = q_font(W)
    c = Canvas(W, H)
    ox, oy = O
    d1 = (math.sin(math.radians(i_deg)), math.cos(math.radians(i_deg)))
    d2 = (math.sin(math.radians(r_deg)), math.cos(math.radians(r_deg)))
    line(c, 20, oy, W - 20, oy, ST, q_stroke(W, 3), None, "butt")
    line(c, ox, 40, ox, H - 40, ST, q_stroke(W, 2), "8 6", "butt")
    text(c, ox + 6, 52, "normal", fs, LBL, "bold", "start")
    text(c, 30, 40, labels[0], fs, LBL, "bold", "start")
    text(c, 30, H - 30, labels[1], fs, LBL, "bold", "start")
    ix, iy = ox - d1[0] * incident_len, oy - d1[1] * incident_len
    line(c, ix, iy, ox, oy, ST, q_stroke(W, 2))
    # ⊕ b4 fix (visual 2): a head can be placed at a distance from O, so it
    # sits between two wave fronts instead of on one.
    hi = incident_head_at or incident_len / 2
    _mid_head(c, ox - d1[0] * (hi + 7), oy - d1[1] * (hi + 7),
              ox - d1[0] * (hi - 7), oy - d1[1] * (hi - 7), ST, 14)
    rx, ry = ox + d2[0] * refracted_len, oy + d2[1] * refracted_len
    line(c, ox, oy, rx, ry, ST, q_stroke(W, 2))
    hr = refracted_head_at or refracted_len / 2
    _mid_head(c, ox + d2[0] * (hr - 7), oy + d2[1] * (hr - 7),
              ox + d2[0] * (hr + 7), oy + d2[1] * (hr + 7), ST, 14)
    for (d, ss, sign) in ((d1, incident_fronts, -1), (d2, refracted_fronts, 1)):
        px, py = d[1], -d[0]            # perpendicular to the ray
        for s in ss:
            cx, cy = ox + sign * d[0] * s, oy + sign * d[1] * s
            ax, ay = cx - px * front_len / 2, cy - py * front_len / 2
            bx, by = cx + px * front_len / 2, cy + py * front_len / 2
            if (sign < 0 and max(ay, by) >= oy) or \
                    (sign > 0 and min(ay, by) <= oy):
                raise ValueError("wavefront_diagram: a front at %s crosses "
                                 "the boundary" % s)
            line(c, ax, ay, bx, by, ACC, q_stroke(W, 2.5))
    return c.svg()


# ── a wave drawn as a graph (no numbers) ──────────────────────────────────

def wave_graph(x_label, y_label, cycles=2.5, mid=0.55, amp=0.30, W=480,
               H=280):
    """A smooth sine curve on bare axes: arrowheads on both axes, NO ticks
    and NO numbers, the curve oscillating about a mid-level at `mid` of the
    axis height with amplitude `amp` of it (so it never touches the x-axis
    when mid > amp). A light dashed line marks the mid-level, unlabelled.
    NEVER drawn: compression/rarefaction labels, particles, "transverse"
    or "longitudinal"."""
    fs = q_font(W)
    c = Canvas(W, H)
    ox, oy = fs * 2 + 18, H - fs * 2 - 16
    ax1, ay1 = W - 24, 22
    aw, ah = ax1 - ox - 22, oy - ay1 - 18
    sw = q_stroke(W, 3)
    arrow(c, ox, oy, ax1, oy, ST, sw, 14)
    arrow(c, ox, oy, ox, ay1, ST, sw, 14)
    ym = oy - ah * mid
    line(c, ox, ym, ox + aw, ym, MUTED, q_stroke(W, 1.5), "6 6", "butt")
    n = 240
    pts = [(ox + aw * i / n,
            ym - ah * amp * math.sin(2 * math.pi * cycles * i / n))
           for i in range(n + 1)]
    c.S.append('<polyline points="%s" fill="none" stroke="%s" '
               'stroke-width="%s" stroke-linecap="round" '
               'stroke-linejoin="round"/>'
               % (" ".join("%.1f,%.1f" % p for p in pts), ACC,
                  q_stroke(W, 3.5)))
    text(c, ox + aw / 2, oy + fs + 12, x_label, fs, LBL, "bold")
    text(c, fs + 4, oy - ah / 2, y_label, fs, LBL, "bold", "middle",
         rotate=-90)
    return c.svg()


ART_KS4PHYS = {
    "free-body":         free_body,
    "magnet-compasses":  magnet_compasses,
    "solenoid":          solenoid,
    "nuclide":           nuclide,
    "sankey-simple":     sankey_simple,
    "echo-sounder":      echo_sounder,
    "wavefront-diagram": wavefront_diagram,
    "wave-graph":        wave_graph,
}
