# -*- coding: utf-8 -*-
"""figlib.ks4lean_org: lean Biology Organisation lesson figures (6), drafted 18 Nov 2026.
Pure standard library. REGISTRY: name -> no-arg fn returning SVG.

Drawn in figlib/ks4lean_eco.py's conventions and with its helpers (one 720 viewBox, Georgia 28,
the same palette, own #FFFDF8 background rect, path commands M L H V C Q Z only, no text on a dark
fill, labels >= 27 at a 720 viewBox: 11.8px+ in a 314px card). Tick numerals are set in
style.NUM_FONT (lining figures, checks rule 6/7). Gridlines a pupil reads values off are
data-role="grid" in the library's readable grid colour (checks: >= 3:1 on the paper).

Every plotted number is computed from the record's own data and asserted:
  enzyme-rate-temperature  peak at 37 °C, zero by 60 °C (enzymes.py, card "Temperature")
  enzyme-rate-ph           peaks at pH 2 and pH 7, each zero 3 pH units from its peak
                           (enzymes.py, card "pH"; EXAMINER ruling 9)
  lung-cancer-bar-chart    15, 60, 150 per 100 000 (health_disease.py, "From a table to a bar chart")
  chd-age-histogram        12, 30, 58, 70, 30 people in 10-year classes, 40 to 90 (health_disease.py,
                           "Reading a histogram"; spec 4.2.2.5 and MS 2c; supervising ruling 18 Nov)
  leaf-cross-section       the nine parts the brief names plus "air spaces" (plant_tissues.py's
                           reveal row "Loosely packed cells with air spaces between them")
  transpiration-temperature-graph  15, 30, 45 mm in 5 min -> 3, 6, 9 mm/min (transpiration.py,
                           card "Reading results")
"""
import math

from .ks4lean_eco import (INK, RUST, BLUE, GREEN, BG, GREY, FS, f, svg, line, poly_line, txt,
                          lines, circ, rect, pathel, leader)
from .style import NUM_FONT, STYLE

GRID = STYLE["grid"]                     # #8C8268, 3.35:1 on the card
LS = 27                                  # axis and tick label size
BAR = "#A9C7E8"
CUTICLE, EPI, PALI, SPONGY, CHLORO = "#F2E7B8", "#F4F6EE", "#B9DBA4", "#CFE6BE", "#3E8A3A"
SHEATH, XYL, PHL = "#EEE2C6", "#FFFFFF", "#E8C9A0"


def num(x, y, s, anchor="middle", size=LS):
    """a tick numeral, in the lining-figure stack."""
    return '<text x="%s" y="%s" font-family="%s" font-size="%s" font-weight="600" text-anchor="%s" fill="%s">%s</text>' % (
        f(x), f(y), NUM_FONT, size, anchor, INK, s)


def vtxt(x, y, s, size=LS, fill=INK):
    """a y-axis title, rotated to read upwards."""
    return '<text x="%s" y="%s" font-family="Georgia, serif" font-size="%s" font-weight="600" text-anchor="middle" fill="%s" transform="rotate(-90 %s %s)">%s</text>' % (
        f(x), f(y), size, fill, f(x), f(y), s)


def grid(x1, y1, x2, y2):
    return '<line x1="%s" y1="%s" x2="%s" y2="%s" data-role="grid" stroke="%s" stroke-width="2.6" stroke-linecap="butt"/>' % (
        f(x1), f(y1), f(x2), f(y2), GRID)


def ellipse(cx, cy, rx, ry, fill, stroke=INK, w=2.6):
    return '<ellipse cx="%s" cy="%s" rx="%s" ry="%s" fill="%s" stroke="%s" stroke-width="%s"/>' % (
        f(cx), f(cy), f(rx), f(ry), fill, stroke, w)


def cross(x, y, s=11, c=INK):
    return line(x - s, y - s, x + s, y + s, c, 3.5, "butt") + line(x - s, y + s, x + s, y - s, c, 3.5, "butt")


# ------------------------------------------------------------------ 1  enzymes, card "Temperature"
def _rate_temperature(T):
    """Collisions speed up (e^kT) while the fraction of enzyme not yet denatured falls (logistic).
    k and the logistic are chosen so the peak is EXACTLY 37 °C: the peak is where
    k = sigma(37) / s, sigma(37) = 1 / (1 + e^((Tm - 37) / s))."""
    s, Tm = 3.0, 41.0
    sig37 = 1.0 / (1.0 + math.exp((Tm - 37.0) / s))
    k = sig37 / s
    return math.exp(k * T) / (1.0 + math.exp((T - Tm) / s))


def enzyme_rate_temperature():
    W, H = 720, 500
    x0, x1, yb, yt = 120, 690, 400, 40
    X = lambda T: x0 + T * (x1 - x0) / 70.0
    peak_y = 96
    r0, r37, r60 = _rate_temperature(0), _rate_temperature(37), _rate_temperature(60)
    # the curve reaches zero at 60 °C: subtract the tiny tail so it lands on the axis there
    norm = lambda T: (_rate_temperature(T) - r60) / (r37 - r60)
    Y = lambda v: yb - v * (yb - peak_y)
    ts = [i / 4.0 for i in range(0, 241)]
    best = max(ts, key=norm)
    assert abs(best - 37.0) < 0.26, best                  # the peak is at 37 °C
    assert abs(norm(60.0)) < 1e-9 and norm(50.0) < 0.2   # steep fall, zero by 60 °C
    assert norm(0) < 0.12                                 # low at 0 °C, rises gently
    b = []
    b.append(line(x0, yt, x0, yb, INK, 4, "butt"))
    b.append(line(x0, yb, x1 + 6, yb, INK, 4, "butt"))
    for T in range(0, 71, 10):
        b.append(line(X(T), yb, X(T), yb + 10, INK, 3, "butt"))
        b.append(num(X(T), yb + 40, str(T)))
    b.append(txt((x0 + x1) / 2, 478, "temperature in °C", LS))
    b.append(vtxt(64, (yt + yb) / 2, "rate of reaction"))
    # optimum: dashed vertical at the peak
    b.append(line(X(37), yb, X(37), 82, GREY, 3, "butt", "12 9"))
    b.append(txt(X(37), 66, "optimum", FS, "middle", INK, 700))
    b.append(poly_line([(X(T), Y(norm(T))) for T in ts], RUST, 5))
    # the falling side: label to its right, with a leader to the curve at 46 °C
    T_l = 46.0
    b.append(lines(560, 206, ["enzyme", "denatured"], FS, "start", RUST, 600, 34))
    b.append(leader(554, 222, X(T_l) + 5, Y(norm(T_l))))
    return svg(W, H, "A graph of rate of reaction against temperature in degrees Celsius, from 0 to 70. The rate rises gently from a low value at 0 degrees to a peak at 37 degrees, marked by a dashed line labelled optimum. Above the optimum the rate falls steeply and reaches zero by about 60 degrees; this falling side is labelled enzyme denatured.", b)


# ------------------------------------------------------------------ 2  enzymes, card "pH"
def _bell(p, peak, half=3.0):
    """a smooth bell: 1 at the peak, 0 (with zero slope) half pH units either side."""
    d = (p - peak) / half
    return math.cos(math.pi * d / 2.0) ** 2 if abs(d) <= 1 else 0.0


def enzyme_rate_ph():
    W, H = 720, 500
    x0, x1, yb, yt = 110, 690, 400, 40
    X = lambda p: x0 + p * (x1 - x0) / 14.0
    peak_y = 150
    Y = lambda v: yb - v * (yb - peak_y)
    assert _bell(2, 2) == 1 and _bell(7, 7) == 1
    assert max(_bell(5, 2), _bell(4, 7), _bell(10, 7)) < 1e-12
    b = []
    b.append(line(x0, yt, x0, yb, INK, 4, "butt"))
    b.append(line(x0, yb, x1 + 6, yb, INK, 4, "butt"))
    for p in range(0, 15, 2):
        b.append(line(X(p), yb, X(p), yb + 10, INK, 3, "butt"))
        b.append(num(X(p), yb + 40, str(p)))
    b.append(txt((x0 + x1) / 2, 478, "pH", LS))
    b.append(vtxt(56, (yt + yb) / 2, "rate of reaction"))
    # protease from the stomach: peak at pH 2, zero by pH 5 (the curve starts on the axis at pH 0)
    pp = [i / 20.0 for i in range(0, 101)]               # pH 0 to 5
    b.append(poly_line([(X(p), Y(_bell(p, 2))) for p in pp], RUST, 5))
    # amylase: peak at pH 7, zero at pH 4 and pH 10
    pa = [4 + i / 20.0 for i in range(0, 121)]           # pH 4 to 10
    b.append(poly_line([(X(p), Y(_bell(p, 7))) for p in pa], BLUE, 5))
    b.append(lines(X(2) + 44, 72, ["protease from", "the stomach"], FS, "middle", RUST, 700, 34))
    b.append(txt(X(8.3), 162, "amylase", FS, "start", BLUE, 700))
    return svg(W, H, "A graph of rate of reaction against pH, from 0 to 14. Two bell-shaped curves of the same height. The curve labelled protease from the stomach peaks at pH 2 and falls to zero by pH 5. The curve labelled amylase peaks at pH 7 and falls to zero at pH 4 and at pH 10.", b)


# ------------------------------------------------------------------ 3  health-disease, bar chart
def lung_cancer_bar_chart():
    W, H = 720, 680
    x0, x1, yb, yt = 150, 700, 560, 40
    Y = lambda v: yb - v * (yb - yt) / 160.0
    data = [(["never", "smoked"], 15), (["smoked in", "the past"], 60), (["smoke now"], 150)]
    assert [v for _, v in data] == [15, 60, 150] and 150 / 15 == 10
    b = []
    for v in range(20, 161, 20):
        b.append(grid(x0, Y(v), x1, Y(v)))
    slot = (x1 - x0) / 3.0
    bw = 112
    for i, (rows, v) in enumerate(data):
        cx = x0 + slot * (i + 0.5)
        b.append(rect(cx - bw / 2, Y(v), bw, Y(0) - Y(v), BAR, INK, 3))
        b.append(lines(cx, yb + 44, rows, LS, "middle", INK, 600, 32))
    b.append(line(x0, yt - 6, x0, yb, INK, 4, "butt"))
    b.append(line(x0, yb, x1, yb, INK, 4, "butt"))
    for v in range(0, 161, 20):
        b.append(line(x0 - 10, Y(v), x0, Y(v), INK, 3, "butt"))
        b.append(num(x0 - 16, Y(v) + 10, str(v), "end"))
    b.append(vtxt(52, (yt + yb) / 2, "lung cancer cases per 100 000 people"))
    return svg(W, H, "A bar chart with gaps between the bars. The vertical axis is lung cancer cases per 100 000 people, from 0 to 160 in steps of 20. Never smoked: 15. Smoked in the past: 60. Smoke now: 150.", b)


# ------------------------------------------------------------------ 3b health-disease, a histogram
CHD_AGES = [(40, 50, 12), (50, 60, 30), (60, 70, 58), (70, 80, 70), (80, 90, 30)]


def chd_age_histogram():
    """Made-up data (health_disease.py, card "Reading a histogram"): the ages at which 200 people
    were diagnosed with coronary heart disease, in equal 10-year class intervals. Continuous data,
    so the bars touch; the x-axis is a number line marked at the class boundaries."""
    W, H = 720, 710
    x0, x1, yb, yt = 150, 670, 560, 40
    lo, hi = CHD_AGES[0][0], CHD_AGES[-1][1]
    X = lambda age: x0 + (age - lo) * (x1 - x0) / float(hi - lo)
    Y = lambda v: yb - v * (yb - yt) / 80.0
    assert sum(n for _, _, n in CHD_AGES) == 200
    assert all(b - a == 10 for a, b, _ in CHD_AGES)
    assert max(CHD_AGES, key=lambda c: c[2])[:2] == (70, 80)
    b = []
    for v in range(10, 81, 10):
        b.append(grid(x0, Y(v), x1, Y(v)))
    for a, c, n in CHD_AGES:                                    # touching bars: no gaps
        b.append(rect(X(a), Y(n), X(c) - X(a), Y(0) - Y(n), BAR, INK, 3))
    b.append(line(x0, yt - 6, x0, yb, INK, 4, "butt"))
    b.append(line(x0, yb, x1, yb, INK, 4, "butt"))
    for v in range(0, 81, 10):
        b.append(line(x0 - 10, Y(v), x0, Y(v), INK, 3, "butt"))
        b.append(num(x0 - 16, Y(v) + 10, str(v), "end"))
    for age in range(lo, hi + 1, 10):                           # boundaries, not bar centres
        b.append(line(X(age), yb, X(age), yb + 10, INK, 3, "butt"))
        b.append(num(X(age), yb + 56, str(age)))
    b.append(txt((x0 + x1) / 2.0, yb + 116, "age at diagnosis in years", FS, "middle"))
    b.append(vtxt(52, (yt + yb) / 2, "number of people"))
    return svg(W, H, "A histogram with no gaps between the bars. The horizontal axis is age at "
               "diagnosis in years, marked 40, 50, 60, 70, 80 and 90. The vertical axis is number of "
               "people, from 0 to 80 in steps of 10. 40 to 50 years: 12. 50 to 60: 30. 60 to 70: 58. "
               "70 to 80: 70. 80 to 90: 30.", b)


# ------------------------------------------------------------------ 4  plant-tissues, the leaf
def _guard_cell(cx, top, bot, side):
    """a kidney-shaped guard cell; side -1 = left of the pore, +1 = right. Its inner (pore-side)
    wall is the thicker one, drawn as a second stroke."""
    o = 7 * side                                           # inner wall edge, beside the pore
    w = 26 * side                                          # outer bulge
    d = "M%s,%s C%s,%s %s,%s %s,%s C%s,%s %s,%s %s,%s Z" % (
        f(cx + o), f(top),
        f(cx + o + w * 1.25), f(top - 6), f(cx + o + w * 1.25), f(bot + 6), f(cx + o), f(bot),
        f(cx + o + w * 0.12), f(bot - 12), f(cx + o + w * 0.12), f(top + 12), f(cx + o), f(top))
    return d


def leaf_cross_section():
    W, H = 720, 620
    L, R = 214, 532                                        # the section's left and right edges
    yc0, yc1 = 40, 54                                      # waxy cuticle
    ye0, ye1 = 54, 94                                      # upper epidermis
    yp0, yp1 = 94, 238                                     # palisade mesophyll
    ys0, ys1 = 238, 448                                    # spongy mesophyll (and the vein)
    yl0, yl1 = 448, 486                                    # lower epidermis
    SX = 304                                               # the stoma's centre
    b = []
    # waxy cuticle (upper), one strip
    b.append(rect(L, yc0, R - L, yc1 - yc0, CUTICLE, INK, 2.6))
    # upper epidermis: one row of flat, clear cells (wider than tall)
    n = 6; cw = (R - L) / float(n)
    for i in range(n):
        b.append(rect(L + i * cw, ye0, cw, ye1 - ye0, EPI, INK, 2.6))
    # palisade mesophyll: tall cells packed with chloroplasts
    n = 12; pw = (R - L) / float(n)
    for i in range(n):
        x = L + i * pw
        b.append(rect(x + 2, yp0 + 3, pw - 4, yp1 - yp0 - 6, PALI, INK, 2.6, 9))
        for k in range(8):
            b.append(circ(x + pw / 2 + (-4.5 if k % 2 else 4.5), yp0 + 20 + k * 16, 4, CHLORO, CHLORO, 1))
    # spongy mesophyll: loosely packed rounded cells; the gaps between them are the air spaces.
    # The lower-left corner is the air space above the stoma, kept clear for the stoma's leader.
    cells = [(244, 268, 26), (306, 262, 24), (368, 270, 26), (420, 262, 20), (502, 266, 22),
             (262, 330, 24), (334, 316, 22), (388, 340, 22),
             (234, 392, 18), (352, 404, 22), (412, 420, 20), (468, 424, 22), (514, 406, 16)]
    for i, (cx, cy, rx) in enumerate(cells):
        b.append(ellipse(cx, cy, rx, 16 + (i % 2) * 2, SPONGY))
        b.append(circ(cx - 7, cy - 2, 3.6, CHLORO, CHLORO, 1))
        b.append(circ(cx + 7, cy + 3, 3.6, CHLORO, CHLORO, 1))
    # the vein: a bundle with xylem above phloem
    VX = 460
    b.append(rect(VX - 40, 290, 80, 104, SHEATH, INK, 3, 22))
    for dx in (-22, 0, 22):
        b.append(circ(VX + dx, 320 + (2 if dx else -2), 10, XYL, INK, 4.5))  # thick, lignified walls
    for dx in (-17, 0, 17):
        b.append(circ(VX + dx, 368 + (0 if dx else 3), 7.5, PHL, INK, 2.6))
    # lower epidermis, with a gap for the stoma
    # Each cell keeps only its part outside the gap; a part under 12 px is folded into its
    # neighbour on the same side, so no sliver (or negative width) is ever drawn.
    n = 6; cw = (R - L) / float(n)
    GL, GR = SX - 34, SX + 34
    left, right = [], []
    for i in range(n):
        x0 = L + i * cw; x1 = x0 + cw
        if x0 < GL:
            left.append([x0, min(x1, GL)])
        if x1 > GR:
            right.append([max(x0, GR), x1])
    if len(left) > 1 and left[-1][1] - left[-1][0] < 12:
        sliver = left.pop(); left[-1][1] = sliver[1]
    if len(right) > 1 and right[0][1] - right[0][0] < 12:
        sliver = right.pop(0); right[0][0] = sliver[0]
    for x0, x1 in left + right:
        b.append(rect(x0, yl0, x1 - x0, yl1 - yl0, EPI, INK, 2.6))
    # lower cuticle, broken at the pore
    b.append(rect(L, yl1, SX - 7 - L, 6, CUTICLE, INK, 2.6))
    b.append(rect(SX + 7, yl1, R - SX - 7, 6, CUTICLE, INK, 2.6))
    # the two guard cells either side of the stoma (the pore between them)
    for side in (-1, 1):
        b.append(pathel(_guard_cell(SX, yl0 - 4, yl1 + 4, side), INK, 2.6, PALI))
        b.append(circ(SX + side * 16, yl0 + 10, 3.4, CHLORO, CHLORO, 1))
        b.append(circ(SX + side * 16, yl1 - 10, 3.4, CHLORO, CHLORO, 1))
    # ---- labels: all outside the section, each with a leader line
    LX = L - 22                                            # left column: right-aligned here
    b.append(lines(LX, 64, ["upper", "epidermis"], FS, "end", INK, 600, 32))
    b.append(leader(LX + 6, 74, L + 26, (ye0 + ye1) / 2))
    b.append(lines(LX, 150, ["palisade", "mesophyll"], FS, "end", INK, 600, 32))
    b.append(leader(LX + 6, 160, L + 11, 166))
    b.append(lines(LX, 264, ["spongy", "mesophyll"], FS, "end", INK, 600, 32))
    b.append(leader(LX + 6, 274, 236, 270))
    b.append(txt(LX, 350, "air spaces", FS, "end"))
    b.append(leader(LX + 6, 341, 236, 352))
    b.append(txt(LX, 414, "stoma", FS, "end"))
    b.append(leader(LX + 6, 412, SX, (yl0 + yl1) / 2))
    b.append(lines(LX, 470, ["lower", "epidermis"], FS, "end", INK, 600, 32))
    b.append(leader(LX + 6, 480, L + 22, (yl0 + yl1) / 2))
    RX = R + 22                                            # right column: left-aligned here
    b.append(lines(RX, 54, ["waxy", "cuticle"], FS, "start", INK, 600, 32))
    b.append(leader(RX - 6, 46, R - 18, (yc0 + yc1) / 2))
    b.append(txt(RX, 326, "xylem", FS, "start"))
    b.append(leader(RX - 6, 317, VX + 22, 322))
    b.append(txt(RX, 380, "phloem", FS, "start"))
    b.append(leader(RX - 6, 371, VX + 17, 368))
    # guard cells: one label under the stoma, a leader to each cell
    b.append(txt(SX, 576, "guard cells", FS, "middle"))
    b.append(leader(SX - 22, 548, SX - 20, yl1 + 2))
    b.append(leader(SX + 22, 548, SX + 20, yl1 + 2))
    return svg(W, H, "A transverse section through a leaf, top to bottom: the waxy cuticle; the upper epidermis, one row of flat clear cells; the palisade mesophyll, tall cells packed with chloroplasts; the spongy mesophyll, loosely packed cells with air spaces between them, with a vein in which the xylem is above the phloem; and the lower epidermis, with a stoma between two guard cells. Every part is labelled outside the section with a leader line.", b)


# ------------------------------------------------------------------ 5  transpiration, the graph
def transpiration_temperature_graph():
    W, H = 720, 560
    x0, x1, yb, yt = 130, 690, 440, 40
    X = lambda T: x0 + T * (x1 - x0) / 35.0
    Y = lambda v: yb - v * (yb - yt) / 10.0
    moved = [(10, 15), (20, 30), (30, 45)]                 # mm the bubble moved in 5 minutes
    pts = [(T, d / 5.0) for T, d in moved]
    assert pts == [(10, 3.0), (20, 6.0), (30, 9.0)]
    b = []
    for T in range(5, 36, 5):
        b.append(grid(X(T), yt, X(T), yb))
    for v in range(2, 11, 2):
        b.append(grid(x0, Y(v), x1, Y(v)))
    b.append(line(x0, yt - 6, x0, yb, INK, 4, "butt"))
    b.append(line(x0, yb, x1 + 6, yb, INK, 4, "butt"))
    for T in range(0, 36, 5):
        b.append(line(X(T), yb, X(T), yb + 10, INK, 3, "butt"))
        b.append(num(X(T), yb + 40, str(T)))
    for v in range(0, 11, 2):
        b.append(line(x0 - 10, Y(v), x0, Y(v), INK, 3, "butt"))
        b.append(num(x0 - 16, Y(v) + 10, str(v), "end"))
    b.append(txt((x0 + x1) / 2, 534, "temperature in °C", LS))
    b.append(vtxt(52, (yt + yb) / 2, "rate of water uptake in mm/min"))
    # a straight ruled line through the three points (they lie on one line: 0.3 mm/min per °C)
    b.append(line(X(pts[0][0]), Y(pts[0][1]), X(pts[-1][0]), Y(pts[-1][1]), BLUE, 4, "butt"))
    for T, v in pts:
        b.append(cross(X(T), Y(v)))
    return svg(W, H, "A graph of rate of water uptake in millimetres per minute, from 0 to 10, against temperature in degrees Celsius, from 0 to 35. Three points are plotted as crosses: 3 at 10 degrees, 6 at 20 degrees and 9 at 30 degrees. A straight ruled line joins them: as the temperature increases, the rate of water uptake increases.", b)


REGISTRY = {
    "enzyme-rate-temperature": enzyme_rate_temperature,
    "enzyme-rate-ph": enzyme_rate_ph,
    "lung-cancer-bar-chart": lung_cancer_bar_chart,
    "chd-age-histogram": chd_age_histogram,
    "leaf-cross-section": leaf_cross_section,
    "transpiration-temperature-graph": transpiration_temperature_graph,
}
