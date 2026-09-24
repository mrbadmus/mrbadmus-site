"""figlib.biochem — question-figure builders for biology and chemistry.

⊕ MRB-352 run 2, batch 2 (the biology and chemistry rows of the 174). A new
module rather than additions to `biology.py` / `chemistry.py`, so that a
lane editing those files in parallel cannot collide with this one. The
builders are the library's house style, parametrised — cream paper, ink
outlines at the library's weights, dark-sage Georgia labels (lining-figure
`NUM_FONT` on any label with a digit, via `style.text`), and a text size
derived from the canvas width (`q_font`) so every label is >= 11 CSS px in
a 320px phone column. Every shape states its own fill; arrowheads are
polygons; there are no arcs (a curve is a quadratic or cubic Bezier, or a
polygon of many points).

Registered in `figlib.ART` through `ART_BIOCHEM` below.

    xray_pattern        a drawing of an X-ray diffraction photograph of DNA
    cycle_clock         a cycle drawn as a clock face, ticks + one marker
    pyramid             a pyramid of numbers (stacked, centred bars)
    particle_grid       a box of touching particles of two kinds + a key
    distillation_flask  a flask, neck, thermometer and side arm
    column_temps        a fractionating column with temperatures by outlets
    bar_model           a whole bar above its parts (conservation sums)
    ph_strip            a pH scale as numbered cells, with a pointer
    body_glands         a body outline with glands lettered A, B, C, D
    ionic_ions          two ions in square brackets, dot-and-cross
    profile_sketch      a sketched energy profile through given points
    box_repeat_unit     a repeat unit in box notation, in brackets, n
"""

import math

from .charts import _smooth_path
from .style import (NUM_FONT, STYLE, TINT, Canvas, _pol, arrow, box,
                    label_font, line, q_font, q_stroke, text, text_width)

INK = STYLE["stroke"]
LBL = STYLE["label"]


def _poly(c, pts, fill, stroke="none", width=0):
    sw = f' stroke-width="{width}"' if stroke != "none" else ""
    c.S.append('<polygon points="%s" fill="%s" stroke="%s"%s/>'
               % (" ".join("%.1f,%.1f" % p for p in pts), fill, stroke, sw))


def _head(c, tip, ang, col, size=14):
    """A solid arrowhead with its tip at `tip`, pointing along `ang` (rad)."""
    tx, ty = tip
    bx, by = tx - size * math.cos(ang), ty - size * math.sin(ang)
    nx, ny = -math.sin(ang) * size * 0.5, math.cos(ang) * size * 0.5
    _poly(c, [(tx, ty), (bx + nx, by + ny), (bx - nx, by - ny)], col)


# ── DNA X-ray pattern (Franklin and Gosling's "Photo 51", drawn) ──────────

def xray_pattern(W=320, H=340, centre=(160, 170), oval=(128, 150),
                 arms=(55, 125, 235, 305), radii=(24, 44, 64, 84, 104),
                 arc_x=(125, 195), arc_y=(40, 300), arc_bow=20):
    """Dark dashes along the four arms of an X on a pale oval, a thick arc
    at the top and bottom, the centre blank. No text at all — naming the
    shape would answer the question it is drawn for."""
    c = Canvas(W, H)
    cx, cy = centre
    c.S.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{oval[0]}" ry="{oval[1]}" '
               f'fill="none" stroke="#b9b2a4" stroke-width="2"/>')
    for a in arms:
        for r in radii:
            x = cx + r * math.cos(math.radians(a))
            y = cy - r * math.sin(math.radians(a))
            box(c, x - 9, y - 3, 18, 6, "#2b2b2b", "none", 0, 3)
    x0, x1 = arc_x
    xm = (x0 + x1) / 2.0
    for y, bow in ((arc_y[0], -arc_bow), (arc_y[1], arc_bow)):
        c.S.append(f'<path d="M {x0} {y} Q {xm} {y + bow} {x1} {y}" '
                   f'fill="none" stroke="#2b2b2b" stroke-width="8" '
                   f'stroke-linecap="round"/>')
    return c.svg()


# ── a cycle drawn as a clock face ─────────────────────────────────────────

def cycle_clock(days=35, marker_at=0.5, start_label="Day 1",
                marker_label="egg released", W=340, H=340, centre=(170, 175),
                r=120):
    """A circle with `days` evenly spaced ticks running clockwise from the
    top, `start_label` above the top tick, ONE filled marker on the circle
    `marker_at` of the way round (0.5 = the bottom) labelled below/beside
    it, and a small curved arrow inside near the top right showing the
    direction of time. No other day numbers are drawn."""
    fs = q_font(W)
    sw = q_stroke(W, 2)
    c = Canvas(W, H)
    cx, cy = centre
    c.S.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#FFFFFF" '
               f'stroke="{INK}" stroke-width="3"/>')
    for i in range(days):
        a = -90 + i * 360.0 / days
        x1, y1 = _pol(cx, cy, r, a)
        x2, y2 = _pol(cx, cy, r - 10, a)
        line(c, x1, y1, x2, y2, INK, sw, None, "butt")
    text(c, cx, cy - r - 12, start_label, fs, LBL, "bold")
    ma = -90 + marker_at * 360.0
    mx, my = _pol(cx, cy, r, ma)
    c.S.append(f'<circle cx="{mx:.1f}" cy="{my:.1f}" r="9" fill="{INK}" '
               f'stroke="none"/>')
    lx, ly = _pol(cx, cy, r + 14 + fs * 0.7, ma)
    text(c, lx, ly + fs * 0.36, marker_label, fs, LBL, "bold")
    # the direction of time: a clockwise curved arrow just inside the rim
    ra, a0, a1 = r - 28, -72, -28
    p0 = _pol(cx, cy, ra, a0)
    p1 = _pol(cx, cy, ra, a1)
    pc = _pol(cx, cy, ra / math.cos(math.radians((a1 - a0) / 2.0)),
              (a0 + a1) / 2.0)
    tip_ang = math.radians(a1 + 90)
    back = (p1[0] - 12 * math.cos(tip_ang), p1[1] - 12 * math.sin(tip_ang))
    c.S.append(f'<path d="M {p0[0]:.1f} {p0[1]:.1f} Q {pc[0]:.1f} {pc[1]:.1f} '
               f'{back[0]:.1f} {back[1]:.1f}" fill="none" stroke="{INK}" '
               f'stroke-width="{q_stroke(W, 2.5)}" stroke-linecap="round"/>')
    _head(c, p1, tip_ang, INK, 14)
    return c.svg()


# ── a pyramid of numbers ─────────────────────────────────────────────────

def pyramid(levels, W=500, H=260, cx=170, bar_h=44, label_x=330,
            note=None):
    """Stacked, centred, touching horizontal bars drawn BOTTOM to TOP from
    `levels` [{"width", "label"}], each labelled to its right (left-aligned
    at `label_x`, centred on its bar); `note` is small print under the
    base. White bars, ink outline — no colour coding by level."""
    fs = q_font(W)
    sw = q_stroke(W, 2.5)
    c = Canvas(W, H)
    base = H - 24 - (fs + 14 if note else 0)
    for i, lv in enumerate(levels):
        y = base - (i + 1) * bar_h
        w = lv["width"]
        box(c, cx - w / 2.0, y, w, bar_h, TINT["white"], INK, sw)
        text(c, label_x, y + bar_h / 2.0 + fs * 0.36, lv["label"], fs, LBL,
             "bold", "start")
    if note:
        text(c, cx, base + fs + 12, note, fs, STYLE["muted"], "normal")
    return c.svg()


# ── particles of two kinds in a box ──────────────────────────────────────

def particle_grid(kinds, n=6, r=18, pitch=36, origin=(40, 40),
                  frame=(20, 20, 224, 224), W=380, H=330, key_x=262,
                  key_y=(110, 150), pattern="checker"):
    """An n x n grid of touching circles in a box. `kinds` is
    [{"fill", "label"}, ...]; with pattern "checker" the kinds alternate
    along every row and column (kind 0 at top left), so every particle of
    one kind touches the other kind on all sides and the two are in equal
    numbers. A key to the right labels each kind on the paper."""
    fs = q_font(W)
    sw = q_stroke(W, 2)
    c = Canvas(W, H)
    fx, fy, fw, fh = frame
    box(c, fx, fy, fw, fh, "none", INK, q_stroke(W, 2.5))
    for row in range(n):
        for col in range(n):
            k = kinds[(row + col) % len(kinds)]
            x, y = origin[0] + col * pitch, origin[1] + row * pitch
            c.S.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{k["fill"]}" '
                       f'stroke="{INK}" stroke-width="{sw}"/>')
    for k, ky in zip(kinds, key_y):
        c.S.append(f'<circle cx="{key_x + 12}" cy="{ky}" r="12" '
                   f'fill="{k["fill"]}" stroke="{INK}" stroke-width="{sw}"/>')
        text(c, key_x + 30, ky + fs * 0.36, k["label"], fs, LBL, "normal",
             "start")
    return c.svg()


# ── simple distillation: the flask end ───────────────────────────────────

def distillation_flask(bulb_y=115, arm_y=160, W=380, H=420):
    """A round-bottomed flask of liquid over a flame, a stoppered neck, a
    side arm leaving the right of the neck at `arm_y` and sloping down to a
    condenser (off the drawing), and a thermometer through the stopper
    whose bulb centre is at `bulb_y`. Correct placement puts the bulb level
    with the side arm; a question may draw it elsewhere on purpose."""
    fs = q_font(W)
    sw = q_stroke(W, 2.5)
    c = Canvas(W, H)
    fcx, fcy, fr = 150, 300, 70
    nx0, nx1, ntop = 135, 165, 90
    # flame (drawn first, under the flask)
    c.S.append(f'<path d="M 150 376 C 170 394 168 414 150 414 '
               f'C 132 414 130 394 150 376 Z" fill="#f2a03d" stroke="{INK}" '
               f'stroke-width="2"/>')
    text(c, 176, 402, "heat", fs, LBL, "bold", "start")
    # flask body, then the liquid in its lower third, then the outline again
    c.S.append(f'<circle cx="{fcx}" cy="{fcy}" r="{fr}" fill="#FFFFFF" '
               f'stroke="{INK}" stroke-width="{sw}"/>')
    yl = fcy + fr - 2 * fr / 3.0
    th = math.degrees(math.asin((yl - fcy) / float(fr)))
    pts = [_pol(fcx, fcy, fr - 1, a) for a in
           [th + (180 - 2 * th) * k / 40.0 for k in range(41)]]
    _poly(c, pts, "#cfe3f2")
    line(c, pts[0][0], yl, pts[-1][0], yl, INK, 1.5, None, "butt")
    c.S.append(f'<circle cx="{fcx}" cy="{fcy}" r="{fr}" fill="none" '
               f'stroke="{INK}" stroke-width="{sw}"/>')
    # the neck: a white column over the top of the circle, two walls
    yj = fcy - math.sqrt(fr * fr - (fcx - nx0) ** 2)
    box(c, nx0 + 1.5, ntop, nx1 - nx0 - 3, yj - ntop + 4, "#FFFFFF", "none", 0)
    line(c, nx0, ntop, nx0, yj, INK, sw, None, "butt")
    # the side arm: a tube from the neck's right wall down to the right
    ex, ey = 360, arm_y + 70
    ang = math.atan2(ey - arm_y, ex - nx1)
    ox, oy = -math.sin(ang) * 6, math.cos(ang) * 6
    tube = [(nx1 - 1, arm_y - 6), (ex - ox, ey - oy), (ex + ox, ey + oy),
            (nx1 - 1, arm_y + 6)]
    _poly(c, tube, "#FFFFFF")
    line(c, nx1, arm_y - 6, ex - ox, ey - oy, INK, sw, None, "butt")
    line(c, nx1, arm_y + 6, ex + ox, ey + oy, INK, sw, None, "butt")
    line(c, nx1, ntop, nx1, arm_y - 6, INK, sw, None, "butt")
    line(c, nx1, arm_y + 6, nx1, yj, INK, sw, None, "butt")
    # "to condenser": an arrow alongside the tube's far end
    ax0, ay0 = ex - 95, ey + 8
    arrow(c, ax0, ay0 + 20, ax0 + 60 * math.cos(ang),
          ay0 + 20 + 60 * math.sin(ang), INK, q_stroke(W, 2.5), 12)
    text(c, W - 12, ey + 64, "to condenser", fs, LBL, "bold", "end")
    # thermometer rod, stopper, bulb
    box(c, 147, 20, 6, bulb_y - 8 - 20, "#FFFFFF", INK, 1.5, 3)
    box(c, nx0 - 4, ntop - 10, nx1 - nx0 + 8, 15, "#6b5a48", INK, 2)
    box(c, 147, ntop - 14, 6, 22, "#FFFFFF", INK, 1.5)
    c.S.append(f'<ellipse cx="150" cy="{bulb_y}" rx="6" ry="10" '
               f'fill="#c0504d" stroke="{INK}" stroke-width="1.5"/>')
    # label, on the paper to the left, with a leader to the bulb
    text(c, 14, bulb_y - 4, "thermometer", fs, LBL, "bold", "start")
    text(c, 14, bulb_y + fs, "bulb", fs, LBL, "bold", "start")
    line(c, 58, bulb_y + fs * 0.62, 141, bulb_y, INK, q_stroke(W, 1.5))
    return c.svg()


# ── a fractionating column with its temperatures ─────────────────────────

def column_temps(outlets, W=360, H=460, col=(130, 30, 80, 390),
                 inlet_y=358, inlet_label=("heated", "crude oil")):
    """A tall column (x, y, w, h), short unlabelled outlet pipes on its
    right at each `outlets` y, each ending in an arrow, and the temperature
    at that height written on the left, right-aligned. `outlets` is
    [(y, "350 °C"), ...]. Heated crude oil enters from the left at
    `inlet_y`. No fraction names — reading the column is the question."""
    fs = q_font(W)
    sw = q_stroke(W, 2.5)
    c = Canvas(W, H)
    x, y, w, h = col
    box(c, x, y, w, h, "#FFFFFF", INK, sw)
    for oy, lab in outlets:
        line(c, x + w, oy, x + w + 48, oy, INK, q_stroke(W, 4), None, "butt")
        arrow(c, x + w + 46, oy, x + w + 74, oy, INK, q_stroke(W, 2.5), 12)
        text(c, x - 10, oy + fs * 0.36, lab, fs, LBL, "bold", "end")
    arrow(c, 24, inlet_y, x - 2, inlet_y, INK, q_stroke(W, 2.5), 13)
    ly = inlet_y - 10 - (len(inlet_label) - 1) * (fs + 3)
    for ln in inlet_label:
        text(c, 24, ly, ln, fs, LBL, "normal", "start")
        ly += fs + 3
    return c.svg()


# ── a bar model (part + part = whole) ────────────────────────────────────

def bar_model(whole, parts, W=480, H=200, x0=20, x1=460, top=30,
              bar_h=50, gap=15):
    """The whole as one bar; directly beneath it, the parts as one bar split
    at their fractions, with the same left and right edges — so the parts
    visibly ADD UP to the whole. `whole` is a label; `parts` is
    [(label, fraction), ...] with fractions summing to 1. Text dark on
    white, inside the bars. No operators and no answer."""
    fs = q_font(W) + 3            # the values ARE the question: one step up
    sw = q_stroke(W, 2.5)
    c = Canvas(W, H)
    box(c, x0, top, x1 - x0, bar_h, "#FFFFFF", INK, sw)
    text(c, (x0 + x1) / 2.0, top + bar_h / 2.0 + fs * 0.36, whole, fs, LBL,
         "bold")
    y2 = top + bar_h + gap
    x = x0
    # ⊕ batch-2 fix round (visual m2): the part labels are siblings, so they
    # share ONE face — NUM_FONT for all of them if any carries a digit, or
    # "oxygen: ? g" sat in Georgia beside "magnesium: 2.4 g" in Times.
    fam = (NUM_FONT if any(label_font(lab) == NUM_FONT for lab, _ in parts)
           else None)
    for lab, frac in parts:
        wd = (x1 - x0) * frac
        box(c, x, y2, wd, bar_h, "#FFFFFF", INK, sw)
        if text_width(lab, fs, True) > wd - 10:
            raise ValueError("bar_model: %r does not fit its part" % lab)
        text(c, x + wd / 2.0, y2 + bar_h / 2.0 + fs * 0.36, lab, fs, LBL,
             "bold", family=fam)
        x += wd
    return c.svg()


# ── the pH scale as cells, with a pointer ────────────────────────────────

_PH_TINTS = ("#F6C9C4", "#F7D0C0", "#F9D8BE", "#FAE0BD", "#FBE8BF",
             "#F6EDC0", "#E8F0C4", "#D6EDC9", "#CDE8D6", "#CBE3E3",
             "#CFDDEE", "#D3D6F0", "#DBD2F0", "#E2CFEF", "#E8CDEC")


def ph_strip(pointer=12, pointer_label="solution X", W=480, H=170,
             x0=30, x1=450, y0=60, y1=100, tints=True):
    """Fifteen equal cells for pH 0-14 with the numerals centred UNDER them
    on the paper, and a downward arrow onto the cell for `pointer` with
    `pointer_label` beside its tail. Pastel tints only (every numeral is on
    the cream paper, never on a cell). No acid/alkali/neutral words."""
    fs = q_font(W)
    fn = int(round(fs * 20 / 17.0))
    sw = q_stroke(W, 2)
    c = Canvas(W, H)
    cw = (x1 - x0) / 15.0
    for k in range(15):
        fillc = _PH_TINTS[k] if tints else "#FFFFFF"
        box(c, x0 + k * cw, y0, cw, y1 - y0, fillc, INK, sw)
        text(c, x0 + k * cw + cw / 2.0, 125, str(k), fn, LBL, "normal")
    px = x0 + pointer * cw + cw / 2.0
    arrow(c, px, 20, px, y0 - 5, INK, q_stroke(W, 3), 14)
    text(c, px - 12, 20 + fs * 0.7, pointer_label, fs, LBL, "bold", "end")
    return c.svg()


# ── glands on a body outline, lettered ───────────────────────────────────

GLAND_FILL = "#c96f5a"


def body_glands(W=320, H=470, letter_x=280):
    """A simple human head-and-body outline with four glands drawn as small
    shapes and lettered A-D on the paper to the right, each with its own
    leader line (a pair of glands gets two leaders meeting at one letter).
    A: base of the brain (pituitary); B: front of the neck (thyroid);
    C: upper abdomen (pancreas); D: low abdomen, a pair (ovaries).
    No names, no other organs — adrenal glands especially, since a
    distractor names them."""
    fs = q_font(W)
    sw = q_stroke(W, 2.5)
    lw = q_stroke(W, 1.5)
    c = Canvas(W, H)
    # torso first, then the neck over its top edge, then the head
    c.S.append(f'<path d="M 124 150 L 76 154 C 62 156 58 168 60 184 '
               f'L 72 300 C 76 340 80 380 80 410 C 80 430 84 440 100 440 '
               f'L 180 440 C 196 440 200 430 200 410 C 200 380 204 340 208 300 '
               f'L 220 184 C 222 168 218 156 204 154 L 156 150 Z" '
               f'fill="#FFFFFF" stroke="{INK}" stroke-width="{sw}" '
               f'stroke-linejoin="round"/>')
    box(c, 124, 118, 32, 36, "#FFFFFF", "none", 0)
    line(c, 124, 120, 124, 151, INK, sw, None, "butt")
    line(c, 156, 120, 156, 151, INK, sw, None, "butt")
    c.S.append(f'<ellipse cx="140" cy="70" rx="46" ry="56" fill="#FFFFFF" '
               f'stroke="{INK}" stroke-width="{sw}"/>')

    def gland(cx, cy, rx, ry):
        c.S.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" '
                   f'fill="{GLAND_FILL}" stroke="{INK}" stroke-width="1.5"/>')

    def leader(pts, letter=None):
        c.S.append('<polyline points="%s" fill="none" stroke="%s" '
                   'stroke-width="%s" stroke-linejoin="round"/>'
                   % (" ".join("%.1f,%.1f" % p for p in pts), INK, lw))

    def letter_at(ch, y):
        text(c, letter_x, y + fs * 0.36, ch, fs + 2, LBL, "bold")

    gland(140, 84, 7, 5)                                   # A
    leader([(147, 84), (268, 84)])
    letter_at("A", 84)
    gland(132, 140, 7, 5)                                  # B (bow-tie)
    gland(148, 140, 7, 5)
    leader([(155, 140), (268, 140)])
    letter_at("B", 140)
    # C: an elongated, slightly tilted shape, as a closed cubic path
    c.S.append(f'<path d="M 128 272 C 132 258 176 250 188 258 '
               f'C 192 264 184 272 170 274 C 156 276 132 282 128 272 Z" '
               f'fill="{GLAND_FILL}" stroke="{INK}" stroke-width="1.5"/>')
    leader([(188, 262), (268, 265)])
    letter_at("C", 265)
    gland(112, 370, 9, 6)                                  # D, a pair
    gland(168, 370, 9, 6)
    leader([(177, 370), (254, 372)])
    leader([(112, 376), (126, 398), (240, 398), (254, 374)])
    line(c, 254, 372, 268, 370, INK, lw)
    letter_at("D", 370)
    return c.svg()


# ── ions only: dot-and-cross, in square brackets ─────────────────────────

def ionic_ions(ions, W=480, H=240, cy=125, r=60):
    """Two (or more) ions side by side, each a circle shell holding four
    PAIRS of electrons at N, E, S, W, its symbol at the centre, square
    brackets round it and its charge at the top right. `ions` is
    [{"x", "symbol", "charge", "pairs": {"N": "cross"|"dot", ...}}].
    No atoms 'before', no transfer arrow, no key and no words."""
    fs = q_font(W)
    sw = q_stroke(W, 2)
    c = Canvas(W, H)
    base = {"N": -90, "E": 0, "S": 90, "W": 180}
    for ion in ions:
        cx = ion["x"]
        c.S.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" '
                   f'stroke="{INK}" stroke-width="{STYLE["shell_w"]}"/>')
        for side, sym in ion["pairs"].items():
            for d in (-11, 11):
                (c.dot if sym == "dot" else c.cross)(
                    *_pol(cx, cy, r, base[side] + d))
        text(c, cx, cy + 28 * 0.36, ion["symbol"], 28, LBL, "bold")
        bw, ear = r + 22, 13
        top = cy - bw
        for s_ in (-1, 1):
            xb = cx + s_ * bw
            c.S.append(f'<path d="M {xb} {top} H {xb + s_ * ear} '
                       f'V {top + 2 * bw} H {xb}" fill="none" stroke="{INK}" '
                       f'stroke-width="2.5"/>')
        text(c, cx + bw + ear + 4, top + fs + 2, ion["charge"], fs + 3, LBL,
             "bold", "start")
    return c.svg()


# ── a sketched reaction profile, through given points ────────────────────

def profile_sketch(points, left_label="reactants", right_label="products",
                   left_at=(0, 18), right_at=(64, 100), W=480, H=340,
                   y_label="energy", x_label="progress of reaction"):
    """Energy (up) against progress of reaction (across), both axes drawn
    as arrows with no numbers, and ONE smooth line through `points` given
    in axis units 0-100 (a monotone cubic: no overshoot, so a sketch shows
    exactly the levels it was given — including a wrong one, on purpose).
    The two flat runs `left_at` / `right_at` (u ranges) are labelled above.
    No activation-energy or energy-change arrows."""
    fs = q_font(W)
    sw = q_stroke(W, 3)
    c = Canvas(W, H)
    ox, oy, xr, yt = 56, H - 44, W - 20, 24

    def P(u, v):
        return (ox + 12 + (xr - ox - 40) * u / 100.0,
                oy - 20 - (oy - yt - 60) * v / 100.0)

    arrow(c, ox, oy, ox, yt, INK, sw, 14)
    arrow(c, ox, oy, xr, oy, INK, sw, 14)
    text(c, ox - 14, (oy + yt) / 2.0, y_label, fs, LBL, "bold", "middle",
         rotate=-90)
    text(c, (ox + xr) / 2.0, oy + fs + 14, x_label, fs, LBL, "bold")
    pts = [P(u, v) for u, v in points]
    c.S.append(f'<path d="{_smooth_path(pts)}" fill="none" '
               f'stroke="{STYLE["arrow"]}" stroke-width="{q_stroke(W, 3.5)}" '
               f'stroke-linecap="round" stroke-linejoin="round"/>')
    for (u0, u1), lab in ((left_at, left_label), (right_at, right_label)):
        v = [vv for uu, vv in points if u0 <= uu <= u1][0]
        x, y = P((u0 + u1) / 2.0, v)
        text(c, x, y - 12, lab, fs, LBL, "bold")
    return c.svg()


# ── a repeat unit in box notation ────────────────────────────────────────

def box_repeat_unit(left=("O", "OH"), right=("HOOC", "C=O"), W=480, H=150,
                    gap=14):
    """One repeat unit, left to right, in AQA box notation (the style of
    `chemistry.box_monomers`: box 40 x 22, bond 16): an opening square
    bracket with a bond passing through it; `left` = (group, group) joined
    through a box; a `gap`; `right` = (group, end) through a box, where an
    end of "C=O" is a carbonyl carbon drawn the displayed way (C with a
    vertical double bond up to O); then a bond through the closing bracket
    and a subscript n. Drawn as given: it may be a deliberately wrong unit."""
    fs = q_font(W, floor=17)
    bw, bh, bond = 40, 22, 16
    tw = lambda s: text_width(s, fs, True)   # noqa: E731
    y = 96
    seq = [("bond", None), ("t", left[0]), ("bond", None), ("box", None),
           ("bond", None), ("t", left[1]), ("gap", None), ("t", right[0]),
           ("bond", None), ("box", None), ("bond", None),
           ("t", "C" if right[1] == "C=O" else right[1]), ("bond", None)]

    def width(kind, v):
        return {"bond": bond, "box": bw, "gap": gap}.get(kind) or tw(v) + 4

    total = 12 + sum(width(k, v) for k, v in seq) + 22 + tw("n")
    x = (W - total) / 2.0
    c = Canvas(W, H)
    brh = 26

    def bracket(xb, s_):
        c.S.append(f'<path d="M {xb + s_ * 8:.1f} {y - brh:.1f} H {xb:.1f} '
                   f'V {y + brh:.1f} H {xb + s_ * 8:.1f}" fill="none" '
                   f'stroke="{INK}" stroke-width="2.5"/>')

    bracket(x + 6, 1)
    x += 12
    first = True
    for kind, v in seq:
        if kind == "bond":
            x0 = x - (12 if first else 0)
            line(c, x0, y, x + bond - 1, y, INK, 2.5, None, "butt")
            first = False
            x += bond
        elif kind == "box":
            box(c, x, y - bh / 2.0, bw, bh, "none", INK, 2.5)
            x += bw
        elif kind == "gap":
            x += gap
        else:
            text(c, x + 2, y + fs * 0.36, v, fs, LBL, "bold", "start")
            if v == "C" and right[1] == "C=O":
                cxm = x + 2 + tw("C") / 2.0
                for dx in (-3.5, 3.5):
                    line(c, cxm + dx, y - fs * 0.75, cxm + dx, y - fs * 0.75
                         - 20, INK, 2.5, None, "butt")
                text(c, cxm, y - fs * 0.75 - 26, "O", fs, LBL, "bold")
            x += width(kind, v)
    line(c, x - 1, y, x + 20, y, INK, 2.5, None, "butt")   # through "]"
    bracket(x + 8, -1)
    text(c, x + 12, y + brh + 4, "n", fs, LBL, "bold", "start")
    return c.svg()


ART_BIOCHEM = {
    "xray-pattern":       xray_pattern,
    "cycle-clock":        cycle_clock,
    "pyramid":            pyramid,
    "particle-grid":      particle_grid,
    "distillation-flask": distillation_flask,
    "column-temps":       column_temps,
    "bar-model":          bar_model,
    "ph-strip":           ph_strip,
    "body-glands":        body_glands,
    "ionic-ions":         ionic_ions,
    "profile-sketch":     profile_sketch,
    "box-repeat-unit":    box_repeat_unit,
}
