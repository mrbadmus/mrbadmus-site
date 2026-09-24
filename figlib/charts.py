"""figlib.charts — data charts in the library's house style, for any subject.

New in figlib (MRB-352 run 2). The library draws each graph by hand inside
the diagram that needs it (`half_life_curve`, `hookes_law_graph`,
`motion_graphs`): black axes at stroke 3, a teal curve at stroke 4, dark-
sage bold labels, Georgia, cream paper. These builders are that same
drawing, parametrised, so a question can plot its own data without anyone
retyping an axis.

Every builder takes `W` and derives its text size from it (`q_font`), so a
chart is legible on a phone by construction rather than by luck. Every axis
takes a label AND a unit as separate, required arguments: a graph without
units cannot be drawn by accident.
"""

import math

from .style import (AMBER, MUTED, RED, STYLE, TINT, Canvas, arrow, box, esc,
                    line, num_width_wide, q_font, q_stroke, text, text_width,
                    wrap, wrap_wide)
from .style import grid_line  # ⊕ MRB-352 run 2 (174)

ST = STYLE["stroke"]
LBL = STYLE["label"]
ACC = STYLE["arrow"]
# ⊕ MRB-352 run 2 (174, visual review): gridlines are drawn by
# style.grid_line (>= 3:1 on the card, WCAG 1.4.11); this was #CFC7B2,
# 1.48:1. GRID is kept as a name for anything importing it.
GRID = STYLE["grid"]
SERIES = (ACC, RED, "#1A1A1A")
DASHES = (None, "10 7", "3 6")


def _axis_title(label, unit):
    if not label:
        raise ValueError("an axis needs a label")
    return "%s / %s" % (label, unit) if unit else label


def _fmt(v):
    return ("%g" % v).replace("-", "−")


def _corner_drop(first_x_label, fn):
    """⊕ MRB-352 run 2, batch-2 fix round (figlib.checks rule 8). The first
    x-axis numeral is centred on the origin and the lowest y-axis numeral
    ends 11 units left of it, level with the axis. A numeral of two digits
    or more then reaches back under that "0" (e.g. "145" beneath "0" at a
    histogram's corner), so the pair crowd together and read as one. Drop
    the x numerals this many units lower whenever that is so; 0 otherwise,
    so a graph whose axis starts at a single digit is unchanged."""
    return 4 if num_width_wide(first_x_label, fn) / 2 > 8 else 0


# ── horizontal bars, one row per item: label above, bar below ────────────

def _num_size(fs):
    """⊕ fix round 1 (visual M3): tick and value numerals one step larger
    than the running text — 20 against 17 on a 480 canvas, ~13.7 CSS px on
    a phone. They are what the pupil reads a value from."""
    return int(round(fs * 20 / 17.0))


def hbar_chart(rows, W=480, axis=None, log=False, boundary=None,
               heading=None, bar_h=22, fill=None, value_side="label"):
    """Rows of horizontal bars, stacked down the page so long labels never
    have to share a line with a bar — the layout that reads on a phone.

    rows      [{"label", "value", "display"?, "fill"?}] top to bottom
    axis      {"label", "unit", "ticks": [v, ...], "tick_labels"?,
               "min", "max", "note"?} — or None for bars drawn to scale with no
               axis (then `max` is the largest value)
    log       plot log10(value) — for quantities spanning many powers of ten
    boundary  {"value", "lines": [...]} a dashed vertical marker
    heading   a short line above the chart
    """
    fs = q_font(W)
    fn = _num_size(fs)
    sw = q_stroke(W, 2)
    left, right = 22, W - 22
    y = 22
    if axis:
        lo, hi = axis["min"], axis["max"]
    else:
        lo, hi = 0.0, max(r["value"] for r in rows)

    def X(v):
        if log:
            f = (math.log10(v) - math.log10(lo)) / (math.log10(hi) - math.log10(lo))
        else:
            f = (v - lo) / float(hi - lo)
        return left + max(0.0, min(1.0, f)) * (right - left)

    note_lines = wrap(axis["note"], fs, W - 40) if axis and axis.get("note") else []
    # height first, then draw
    h = y + (fs + 8 if heading else 0) + len(note_lines) * (fs + 6) \
        + (len(boundary["lines"]) * (fs + 4) + 8 if boundary else 0) \
        + len(rows) * (max(fs, fn) + 8 + bar_h + 14) \
        + (fs + fn + 34 if axis else 4) + 14
    c = Canvas(W, int(h))
    if heading:
        y += fs
        text(c, left, y, heading, fs, LBL, "bold", "start")
        y += 10
    if boundary:
        for ln in boundary["lines"]:
            y += fs + 4
            text(c, X(boundary["value"]), y, ln, fs, MUTED, "normal", "middle")
        y += 8
    plot_top = y
    for i, r in enumerate(rows):
        y += max(fs, fn) + 4
        text(c, left, y, r["label"], fs, LBL, "bold", "start")
        if r.get("display") and value_side == "label":
            text(c, right, y, r["display"], fn, LBL, "normal", "end")
        y += 6
        x1 = X(r["value"])
        c.S.append(
            f'<rect x="{left:.1f}" y="{y:.1f}" width="{max(2.0, x1-left):.1f}" '
            f'height="{bar_h}" fill="{r.get("fill") or fill or TINT["mint"]}" '
            f'stroke="{ST}" stroke-width="{sw}"/>')
        y += bar_h + 14
    plot_bot = y - 6
    if boundary:
        bx = X(boundary["value"])
        line(c, bx, plot_top + 2, bx, plot_bot, MUTED, sw, "7 6")
    if axis:
        ay = plot_bot + 4
        line(c, left, ay, right, ay, ST, sw)
        labels = axis.get("tick_labels") or [_fmt(t) for t in axis["ticks"]]
        for t, lab in zip(axis["ticks"], labels):
            tx = X(t)
            line(c, tx, ay, tx, ay + 8, ST, sw)
            anchor = "middle"
            # ⊕ fix round 2: judged in the widest face NUM_FONT can fall
            # back to, against figlib.checks' 6-unit edge clearance
            half = num_width_wide(lab, fn) / 2
            if tx - half < 8:
                anchor = "start"
            elif tx + half > W - 8:
                anchor = "end"
            text(c, tx, ay + 10 + fn, lab, fn, LBL, "normal", anchor)
        text(c, (left + right) / 2, ay + 22 + fn + fs,
             _axis_title(axis["label"], axis.get("unit")), fs, LBL, "bold")
        yy = ay + 22 + fn + fs
        for ln in note_lines:
            yy += fs + 6
            text(c, (left + right) / 2, yy, ln, fs, LBL, "normal")
    return c.svg()


# ── a histogram / bar chart with vertical bars ───────────────────────────

def column_chart(bins, x_label, x_unit, y_label, y_unit=None, W=480, H=380,
                 touching=True, edges=None, y_max=None, y_step=None,
                 fill=None, values=False, caption=None, min_bar=0,
                 y_title="side", edge_label_every=1):
    """Vertical bars.

    With `touching=True` and `edges` (the class boundaries, one more than
    there are bins) this is a histogram of a continuous quantity: bars
    share their sides, and the axis is numbered at the boundaries, never
    under a bar — the convention that says every value in between exists.

    With `touching=False` it is a bar chart of categories: gaps between
    bars, each category named under its bar (wrapped to the bar's width),
    and `values=True` prints each bin's `display` (or its number) above it.
    `min_bar` gives a bar too small to see a minimum drawn height, so a
    near-zero category is still visibly THERE. `caption` is a line of
    small print under the chart. A bin's `display` may be a list of lines.
    `x_label=None` omits the x-axis title (a bar chart of named categories
    needs none); `y_title="top"` writes a long y-axis title above the plot,
    wrapped, instead of rotating it up the side where it would not fit.
    ⊕ MRB-352 run 2 (batch 2): `edge_label_every=k` numbers only every k-th
    class boundary of a histogram (every boundary still gets its tick) —
    for many narrow classes, whose numerals cannot all fit at 360px.
    """
    fs = q_font(W)
    fn = _num_size(fs)
    sw = q_stroke(W, 2)
    n = len(bins)
    vmax = y_max or max(b["n"] for b in bins)
    step = y_step or max(1, int(math.ceil(vmax / 5.0)))
    top = step * int(math.ceil(vmax / float(step)))
    ox = 30 + fs * 1.3 + text_width(_fmt(top), fn)
    # ⊕ fix round 2 (visual n1): a histogram's last boundary numeral is
    # centred on the plot's right edge. At a fixed 18-unit margin "180" ran
    # to within ~2 units of the card, and past it in Noto Serif (Android).
    # The margin now fits half that numeral in its widest fallback face,
    # plus figlib.checks' edge clearance and a little air.
    rpad = 18
    if touching and edges:
        rpad = max(rpad, num_width_wide(_fmt(edges[-1]), fn) / 2 + 8)
    aw = W - ox - rpad
    gapw = 0 if touching else aw / n * 0.28
    bw = (aw - gapw * (n + 1)) / n
    cat_lines = ([wrap_wide(b["label"], fs, bw + gapw * 0.9) for b in bins]
                 if not (touching and edges) else [[""]])
    cap_lines = wrap_wide(caption, fs, W - 40) if caption else []
    # ⊕ batch-2 fix round (checks rule 8): a histogram's x-axis title sat
    # with its descenders about 1 unit off the card's bottom edge; its
    # budget is now the numeral row, the title's own line box and 6 units.
    drop = _corner_drop(_fmt(edges[0]), fn) if touching and edges else 0

    def _below(cl):
        if touching and edges:
            return max((fs + 10) + fs + 26,
                       10 + drop + fn + fs + 18 + 0.24 * fs + 6)
        return (fs + 10) * max(len(c_) for c_ in cl) + fs + 26
    below = _below(cat_lines)
    oy = H - below - (len(cap_lines) * (fs + 5) + 8 if cap_lines else 0)
    top_lines = (wrap_wide(_axis_title(y_label, y_unit), fs, W - 30, True)
                 if y_title == "top" else [])
    head = len(top_lines) * (fs + 5) + (8 if top_lines else 0)
    if y_title == "top":
        ox = 24 + text_width(_fmt(top), fn) + 14
        aw = W - ox - rpad
        gapw = 0 if touching else aw / n * 0.28
        bw = (aw - gapw * (n + 1)) / n
        cat_lines = ([wrap_wide(b["label"], fs, bw + gapw * 0.9)
                      for b in bins]
                     if not (touching and edges) else [[""]])
        below = _below(cat_lines)
        oy = H - below - (len(cap_lines) * (fs + 5) + 8 if cap_lines else 0)
    nval = max((len(b["display"]) if isinstance(b.get("display"), list) else 1)
               for b in bins) if values else 0
    ah = oy - 26 - head - (nval * (fn + 4) + 6 if values else 0)
    c = Canvas(W, H)
    yy = 14 + fs
    for ln in top_lines:
        text(c, 16, yy, ln, fs, LBL, "bold", "start")
        yy += fs + 5
    for k in range(0, int(top) + 1, int(step)):
        yy = oy - ah * k / float(top)
        grid_line(c, ox, yy, ox + aw, yy, W)
        line(c, ox - 7, yy, ox, yy, ST, sw)
        text(c, ox - 11, yy + fn * 0.35, _fmt(k), fn, LBL, "normal", "end")
    for i, b in enumerate(bins):
        x = ox + gapw + i * (bw + gapw)
        hh = max(min_bar, ah * b["n"] / float(top))
        c.S.append(
            f'<rect x="{x:.1f}" y="{oy-hh:.1f}" width="{bw:.1f}" '
            f'height="{hh:.1f}" fill="{b.get("fill") or fill or TINT["mint"]}" '
            f'stroke="{ST}" stroke-width="{sw}"/>')
        if values:
            disp = b.get("display", _fmt(b["n"]))
            disp = disp if isinstance(disp, list) else [disp]
            yy = oy - hh - 8 - (len(disp) - 1) * (fn + 4)
            for ln in disp:
                text(c, x + bw / 2, yy, ln, fn, LBL, "bold")
                yy += fn + 4
    line(c, ox, oy, ox + aw, oy, ST, q_stroke(W, 3))
    line(c, ox, oy, ox, oy - ah, ST, q_stroke(W, 3))
    if touching and edges:
        for i, e in enumerate(edges):
            xx = ox + gapw + i * (bw + gapw)
            line(c, xx, oy, xx, oy + 7, ST, sw)
            if i % edge_label_every == 0:
                text(c, xx, oy + 10 + drop + fn, _fmt(e), fn, LBL, "normal")
        lab_y = oy + 10 + drop + fn
    else:
        lab_y = oy
        for i, b in enumerate(bins):
            xx = ox + gapw + i * (bw + gapw) + bw / 2
            yy = oy + 8 + fs
            for ln in cat_lines[i]:
                text(c, xx, yy, ln, fs, LBL, "normal")
                yy += fs + 4
            lab_y = max(lab_y, yy - fs - 4)
    if x_label:
        text(c, ox + aw / 2, lab_y + fs + 18, _axis_title(x_label, x_unit), fs,
             LBL, "bold")
    if y_title != "top":
        text(c, fs + 6, oy - ah / 2, _axis_title(y_label, y_unit), fs, LBL,
             "bold", "middle", rotate=-90)
    yy = H - 12 - (len(cap_lines) - 1) * (fs + 5)
    for ln in cap_lines:
        text(c, W / 2, yy, ln, fs, MUTED, "normal")
        yy += fs + 5
    return c.svg()


# ── a line graph ─────────────────────────────────────────────────────────

def _smooth_path(pts, start_slope=None):
    """A MONOTONE cubic through the points (Fritsch–Carlson), as cubic
    Beziers (C only). Unlike a Catmull-Rom spline it never overshoots: a
    curve through data that levels off at 55 never pokes above 55, and a
    flat run stays exactly flat."""
    n = len(pts)
    if n < 3:
        return "M " + " L ".join("%.1f %.1f" % p for p in pts)
    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]
    d = [(ys[i+1] - ys[i]) / (xs[i+1] - xs[i]) for i in range(n - 1)]
    def end_slope(h0, h1, d0, d1):
        # the shape-preserving three-point end slope (Moler, "Numerical
        # Computing with MATLAB", pchip): using the first chord's slope
        # alone put a false S-bend at the origin of a decelerating curve
        s = ((2 * h0 + h1) * d0 - h0 * d1) / (h0 + h1)
        if s * d0 <= 0:
            return 0.0
        if d0 * d1 <= 0 and abs(s) > abs(3 * d0):
            return 3 * d0
        return s
    hs = [xs[i+1] - xs[i] for i in range(n - 1)]
    m = ([end_slope(hs[0], hs[1], d[0], d[1])]
         + [0.0 if d[i-1] * d[i] <= 0 else (d[i-1] + d[i]) / 2.0
            for i in range(1, n - 1)]
         + [end_slope(hs[-1], hs[-2], d[-1], d[-2])])
    if start_slope is not None:
        # ⊕ MRB-352 run 2 (174): continue a straight run with no kink
        m[0] = start_slope
    for i in range(n - 1):
        if d[i] == 0:
            m[i] = m[i+1] = 0.0
            continue
        a, b = m[i] / d[i], m[i+1] / d[i]
        s = a * a + b * b
        if s > 9:
            t = 3.0 / math.sqrt(s)
            m[i], m[i+1] = t * a * d[i], t * b * d[i]
    out = "M %.1f %.1f" % pts[0]
    for i in range(n - 1):
        h = xs[i+1] - xs[i]
        c1 = (xs[i] + h / 3.0, ys[i] + m[i] * h / 3.0)
        c2 = (xs[i+1] - h / 3.0, ys[i+1] - m[i+1] * h / 3.0)
        out += " C %.1f %.1f %.1f %.1f %.1f %.1f" % (c1 + c2 + pts[i+1])
    return out


def _markers(c, pts, kind, col, W):
    """⊕ MRB-352 batch 4: per-series data markers — "x" a cross, "dot" a
    filled circle — for plotted readings (with `"line": False`, a scatter)."""
    if not kind:
        return
    for x, y in pts:
        if kind == "x":
            h = 6
            for dx in (-h, h):
                c.S.append(f'<line x1="{x - h:.1f}" y1="{y + dx:.1f}" '
                           f'x2="{x + h:.1f}" y2="{y - dx:.1f}" stroke="{col}" '
                           f'stroke-width="{q_stroke(W, 2.5)}" '
                           f'stroke-linecap="round" fill="none"/>')
        elif kind == "dot":
            c.S.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4.5" '
                       f'fill="{col}" stroke="none"/>')
        else:
            raise ValueError("line_graph: markers is 'x' or 'dot'")


def line_graph(series, x_label, x_unit, y_label, y_unit, x_range, y_range,
               x_ticks, y_ticks, W=480, H=380, grid=True, legend=False,
               x_grid=None, y_grid=None, end_dot=False, canvas=None, top=0,
               ox=None):
    """Axes, a light grid, and one or more series. A series is
    {"points": [(x, y), ...], "smooth": bool, "label": str}; the first is
    drawn in the library's teal, the second in red and dashed, so two
    series differ by more than colour alone.

    ⊕ MRB-352 batch 4, three optional series keys, all off by default:
    `markers` "x" | "dot" marks each point; `line` False draws no line
    (a scatter of readings); `colour` "ink" draws the series solid ink (a
    line of best fit). `x_ticks` / `y_ticks` may be empty lists.

    ⊕ MRB-352 batch 1: `canvas` / `top` draw the graph INTO an existing
    Canvas with every y shifted down by `top` (no <g>, no transform — the
    manifest forbids both), and return nothing. `graph_panels` stacks
    graphs this way, and `ox` pins the y axis's x so stacked graphs share
    one time axis.

    ⊕ MRB-352 run 2 (batch 2), two optional series keys, both off by
    default: `dots` True puts a filled marker on every data point (one
    reading per point, e.g. one per year); `arrows` [segment index, ...]
    puts a solid arrowhead at the midpoint of each listed segment, pointing
    along it — for a path whose ORDER matters (a loop is not x-monotone, so
    such a series is drawn with `smooth` False)."""
    fs = q_font(W)
    fn = _num_size(fs)
    sw = q_stroke(W, 2)
    ox = ox or (30 + fs * 1.3 + max((text_width(_fmt(t), fn) for t in y_ticks), default=0))
    # an empty x_ticks list (no numerals on the x axis) has no corner
    # numeral to crowd, so no drop.
    drop = _corner_drop(_fmt(x_ticks[0]), fn) if x_ticks else 0
    oy = top + H - (fs + fn + 34) - (fs + 14 if legend else 0) - drop
    aw = W - ox - 26
    ah = oy - top - 26
    (x0, x1), (y0, y1) = x_range, y_range

    def P(x, y):
        return (ox + aw * (x - x0) / float(x1 - x0),
                oy - ah * (y - y0) / float(y1 - y0))

    c = canvas if canvas is not None else Canvas(W, H)
    if grid:
        # ⊕ MRB-352 (174): a line at a labelled tick is major; one between
        # ticks (x_grid / y_grid finer than the ticks) is minor, thinner
        for t in (x_grid or x_ticks):
            px, _ = P(t, y0)
            grid_line(c, px, oy, px, oy - ah, W,
                      "major" if t in x_ticks else "minor")
        for t in (y_grid or y_ticks):
            _, py = P(x0, t)
            grid_line(c, ox, py, ox + aw, py, W,
                      "major" if t in y_ticks else "minor")
    for t in x_ticks:
        px, _ = P(t, y0)
        line(c, px, oy, px, oy + 7, ST, sw)
        text(c, px, oy + 10 + drop + fn, _fmt(t), fn, LBL, "normal")
    for t in y_ticks:
        _, py = P(x0, t)
        line(c, ox - 7, py, ox, py, ST, sw)
        text(c, ox - 11, py + fn * 0.35, _fmt(t), fn, LBL, "normal", "end")
    line(c, ox, oy, ox + aw, oy, ST, q_stroke(W, 3))
    line(c, ox, oy, ox, oy - ah, ST, q_stroke(W, 3))
    for k, s in enumerate(series):
        pts = [P(x, y) for x, y in s["points"]]
        col = SERIES[k % len(SERIES)]
        dash = DASHES[k % len(DASHES)]
        if s.get("colour") == "ink":      # ⊕ b4: a solid ink best-fit line
            col, dash = ST, None
        dd = f' stroke-dasharray="{dash}"' if dash else ""
        if s.get("smooth") and s.get("smooth_from") is not None:
            # ⊕ MRB-352 run 2 (174): exactly straight up to x = smooth_from,
            # then the monotone curve, leaving at the straight run's slope
            k0 = max(i for i, (x, _y) in enumerate(s["points"])
                     if x <= s["smooth_from"])
            if k0 < 1:
                raise ValueError("line_graph: smooth_from needs a straight "
                                 "run of at least one segment before it")
            (ax, ay), (bx, by) = pts[k0 - 1], pts[k0]
            head = "M " + " L ".join("%.1f %.1f" % q for q in pts[:k0 + 1])
            tail = _smooth_path(pts[k0:], start_slope=(by - ay) / (bx - ax))
            d = head + tail[tail.index(" ", tail.index(" ", 2) + 1):]
        elif s.get("smooth"):
            d = _smooth_path(pts)
        else:
            d = "M " + " L ".join("%.1f %.1f" % p for p in pts)
        if s.get("line", True):           # ⊕ b4: line=False is a scatter
            c.S.append(f'<path d="{d}" fill="none" stroke="{col}" '
                       f'stroke-width="{q_stroke(W, 3.5)}" stroke-linecap="round" '
                       f'stroke-linejoin="round"{dd}/>')
        _markers(c, pts, s.get("markers"), col, W)
        if s.get("dots"):
            for px_, py_ in pts:
                c.S.append(f'<circle cx="{px_:.1f}" cy="{py_:.1f}" r="5" '
                           f'fill="{col}" stroke="none"/>')
        for k_seg in (s.get("arrows") or ()):
            (ax_, ay_), (bx_, by_) = pts[k_seg], pts[k_seg + 1]
            ang = math.atan2(by_ - ay_, bx_ - ax_)
            hl = 16
            tx_, ty_ = ((ax_ + bx_) / 2 + math.cos(ang) * hl / 2,
                        (ay_ + by_) / 2 + math.sin(ang) * hl / 2)
            bx2, by2 = tx_ - hl * math.cos(ang), ty_ - hl * math.sin(ang)
            nx_, ny_ = -math.sin(ang) * hl * 0.5, math.cos(ang) * hl * 0.5
            c.S.append(f'<polygon points="{tx_:.1f},{ty_:.1f} '
                       f'{bx2+nx_:.1f},{by2+ny_:.1f} {bx2-nx_:.1f},{by2-ny_:.1f}" '
                       f'fill="{col}" stroke="none"/>')
        if end_dot:
            ex, ey = pts[-1]
            c.S.append(f'<circle cx="{ex:.1f}" cy="{ey:.1f}" r="5.5" '
                       f'fill="{col}" stroke="none"/>')
    text(c, ox + aw / 2, oy + 24 + drop + fn + fs,
         _axis_title(x_label, x_unit), fs, LBL, "bold")
    text(c, fs + 4, oy - ah / 2, _axis_title(y_label, y_unit), fs, LBL,
         "bold", "middle", rotate=-90)
    if legend:
        lx, ly = ox, top + H - 14
        for k, s in enumerate(series):
            col = SERIES[k % len(SERIES)]
            dash = DASHES[k % len(DASHES)]
            line(c, lx, ly - fs * 0.35, lx + 40, ly - fs * 0.35, col,
                 q_stroke(W, 3.5), dash)
            text(c, lx + 48, ly, s["label"], fs, LBL, "bold", "start")
            lx += 60 + text_width(s["label"], fs, True) + 24
    if canvas is None:
        return c.svg()


def graph_panels(panels, W=480):
    """Two or more line graphs stacked one above the other, each captioned
    above it ("Graph 1"). A panel is a full `line_graph` parameter set
    (its own H) plus `caption`. For comparing graphs whose SCALES differ —
    the drawing makes the pupil read each axis, not the slope's look."""
    fs = q_font(W)
    # ⊕ MRB-352 run 2 (batch-2 merge, checks rule 8): the first caption's
    # line box sat 1.4 units off the card's top edge; every panel now starts
    # PAD units down, and the card grows by the same.
    PAD = 8
    H = int(PAD + sum(p.get("H", 380) + fs + 34 for p in panels))
    c = Canvas(W, H)
    fn = _num_size(fs)
    ox = max(30 + fs * 1.3 + max((text_width(_fmt(t), fn) for t in p["y_ticks"]), default=0)
             for p in panels)          # one y-axis position: identical time axes
    y = float(PAD)
    for p in panels:
        p = dict(p)
        caption = p.pop("caption")
        ph = p.pop("H", 380)
        p.pop("W", None)
        text(c, W / 2, y + fs, caption, fs, LBL, "bold")
        line_graph(W=W, H=ph, canvas=c, top=y + fs + 10, ox=ox, **p)
        y += fs + 10 + ph + 24
    return c.svg()


# ── a table of short verdicts (a grid of combinations) ───────────────────

def table(col_heads, rows, W=480, corner="", cell_fills=None,
          col_title=None, row_title=None, head_max=None):
    """A grid with a header row and a header column. `rows` is
    [{"head": str, "cells": [[line, ...], ...]}]; a cell is a list of lines
    (wrapped further if a line is still too wide). `cell_fills[r][c]` may
    tint a cell; headers sit on sand, cells on white or their tint.
    `col_title` spans the column headers from above; `row_title` runs up
    the side of the row headers. A cell given as [] is drawn EMPTY — for a
    grid the pupil fills in.

    ⊕ MRB-352 run 2, batch-2 fix round 2 (visual o2): `head_max` (default
    None = one line per row header, as before) wraps the row headers at
    that width in the widest fallback face, so a long row header gives
    its width to the data columns instead of forcing their headers into
    three or four lines."""
    fs = q_font(W)
    sw = q_stroke(W, 2)
    n = len(col_heads)
    row_heads = [wrap_wide(r["head"], fs, head_max, True) if head_max
                 else [r["head"]] for r in rows]
    head_w = max(text_width(ln, fs, True) for rh_ in row_heads
                 for ln in rh_) + 18
    side = fs + 18 if row_title else 0
    col_w = (W - 24 - side - head_w) / float(n)
    x0, y0 = 12 + side, 12 + (fs + 14 if col_title else 0)

    def lines_of(cell):
        """[(text, bold)] — a cell's first line is its verdict, in bold,
        however many lines it wraps to; the rest is the reason."""
        out = []
        for k, ln in enumerate(cell):
            if ln:
                out.extend((w, k == 0) for w in wrap(ln, fs, col_w - 14, True))
        return out or [("", False)]

    # ⊕ batch-2 fix round (checks rule 8): headers wrap at the widest
    # fallback face, so neighbouring headers cannot run into each other.
    head_lines = [wrap_wide(h, fs, col_w - 10, True) for h in col_heads]
    head_h = max(len(h) for h in head_lines) * (fs + 4) + 16
    row_hs = [max([len(lines_of(cl)) for cl in r["cells"]]
                  + [len(row_heads[i])]) * (fs + 4) + 18
              for i, r in enumerate(rows)]
    H = int(y0 + 12 + head_h + sum(row_hs))
    c = Canvas(W, H)
    if col_title:
        text(c, x0 + head_w + n * col_w / 2, 12 + fs, col_title, fs, LBL, "bold")
    if row_title:
        text(c, 12 + fs, y0 + head_h + sum(row_hs) / 2, row_title, fs, LBL,
             "bold", "middle", rotate=-90)
    box(c, x0, y0, head_w, head_h, TINT["sand"], ST, sw)
    if corner:
        text(c, x0 + head_w / 2, y0 + head_h / 2 + fs * 0.35, corner, fs, LBL)
    for j, hl in enumerate(head_lines):
        x = x0 + head_w + j * col_w
        box(c, x, y0, col_w, head_h, TINT["sand"], ST, sw)
        yy = y0 + (head_h - len(hl) * (fs + 4)) / 2 + fs
        for ln in hl:
            text(c, x + col_w / 2, yy, ln, fs, LBL, "bold")
            yy += fs + 4
    y = y0 + head_h
    for i, r in enumerate(rows):
        rh = row_hs[i]
        box(c, x0, y, head_w, rh, TINT["sand"], ST, sw)
        hl_ = row_heads[i]
        yy = (y + (rh - len(hl_) * (fs + 4)) / 2 + fs if head_max
              else y + rh / 2 + fs * 0.35)       # one line: as before
        for ln in hl_:
            text(c, x0 + head_w / 2, yy, ln, fs, LBL)
            yy += fs + 4
        for j, cell in enumerate(r["cells"]):
            x = x0 + head_w + j * col_w
            fillc = (cell_fills[i][j] if cell_fills else None) or TINT["white"]
            box(c, x, y, col_w, rh, fillc, ST, sw)
            ls = lines_of(cell)
            yy = y + (rh - len(ls) * (fs + 4)) / 2 + fs
            for ln, bold in ls:
                text(c, x + col_w / 2, yy, ln, fs, LBL,
                     "bold" if bold else "normal")
                yy += fs + 4
        y += rh
    return c.svg()


__all__ = ["hbar_chart", "column_chart", "line_graph", "graph_panels", "table", "esc",
           "arrow", "AMBER"]
