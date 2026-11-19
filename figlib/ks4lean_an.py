# -*- coding: utf-8 -*-
"""figlib.ks4lean_an: lean Chemical analysis lesson figures (3), drafted 19 Nov 2026.
Pure standard library. REGISTRY: name -> no-arg fn returning SVG.

Drawn in figlib/ks4lean_eco.py's conventions and with its helpers (one 720 viewBox, Georgia 28,
own #FFFDF8 background rect, path commands M L H V C Q Z only, no text on a dark fill, labels
>= 27 at a 720 viewBox). Every plotted number is computed from the record's own data and asserted:
  chromatogram      start line 2 cm up the paper (40 px per cm); lane A spots 1.5, 3.6 and 6.0 cm
                    above it, lane B one spot at 3.6 cm; solvent front 8.0 cm; Rf 3.6 / 8.0 = 0.45
                    (chromatography.py, card "Reading a chromatogram")
  limewater-test    the carbon dioxide test rig (testing_for_gases.py, card "Carbon dioxide")
  emission-spectra  line positions in nm (instrumental_methods.py, card "Reading a line spectrum")
"""
from .ks4lean_eco import (INK, RUST, BLUE, BG, FS, f, svg, line, txt, lines, circ, rect, pathel,
                          leader, arrow)
from .style import NUM_FONT

PAPER = "#F6F0DE"
LIQ = "#CFE3EE"
K = 0.5523


def _tube(cx, hw, top, bot_c):
    """an open-topped test tube outline: straight walls to y = bot_c, then a round bottom."""
    x0, x1 = cx - hw, cx + hw
    yb = bot_c + hw
    return ("M%s,%s V%s C%s,%s %s,%s %s,%s C%s,%s %s,%s %s,%s V%s" % (
        f(x0), f(top), f(bot_c), f(x0), f(bot_c + hw * K), f(cx - hw * K), f(yb), f(cx), f(yb),
        f(cx + hw * K), f(yb), f(x1), f(bot_c + hw * K), f(x1), f(bot_c), f(top)))


def _tube_fill(cx, hw, level, bot_c):
    """the liquid inside a tube, from `level` down to the round bottom."""
    x0, x1 = cx - hw, cx + hw
    yb = bot_c + hw
    return ("M%s,%s V%s C%s,%s %s,%s %s,%s C%s,%s %s,%s %s,%s V%s Z" % (
        f(x0), f(level), f(bot_c), f(x0), f(bot_c + hw * K), f(cx - hw * K), f(yb), f(cx), f(yb),
        f(cx + hw * K), f(yb), f(x1), f(bot_c + hw * K), f(x1), f(bot_c), f(level)))


# ------------------------------------------------------------------ 1  chromatography
def chromatogram():
    W, H = 720, 630
    CM = 40.0
    xl, xr = 60, 260                       # the paper
    yb = 590                               # bottom edge of the paper (in the solvent)
    y0 = 490                               # the pencil start line: 2 cm... see below
    assert (yb - y0) / CM == 2.5           # drawn 2.5 cm of paper below the line: the paper dips in
    Y = lambda cm: y0 - cm * CM            # a height in cm above the start line
    front = 8.0
    spotsA = [(1.5, "#F2C318"), (3.6, "#2F5DAA"), (6.0, "#D23A2E")]
    spotB = [(3.6, "#2F5DAA")]
    assert abs(3.6 / front - 0.45) < 1e-9
    b = []
    # the solvent in the beaker, and the paper standing in it
    b.append(rect(30, 548, 400, 62, LIQ, INK, 3))
    b.append(rect(xl, Y(front) - 40, xr - xl, yb - (Y(front) - 40), PAPER, INK, 3))
    b.append(txt(280, 592, "solvent", FS, "start"))
    # the pencil start line and the solvent front
    b.append(line(xl, y0, xr, y0, INK, 4, "butt"))
    b.append(line(xr, y0, 640, y0, "#8C8268", 2.6, "butt", "6 8"))
    b.append(line(xl, Y(front), 640, Y(front), RUST, 4, "butt", "14 10"))
    b.append(txt(290, Y(front) - 14, "solvent front", FS, "start", RUST))
    b.append(txt(290, y0 + 34, "start line (pencil)", FS, "start"))
    for cx, name, spots in ((110, "A", spotsA), (210, "B", spotB)):
        b.append(txt(cx, y0 + 34, name, FS))
        for cm, col in spots:
            b.append(circ(cx, Y(cm), 15, col, INK, 2.6))
    # the two distances
    xa = 330
    b.append(line(232, Y(3.6), xa + 8, Y(3.6), "#8C8268", 2.6, "butt", "6 8"))
    b.append(arrow(xa, y0, xa, Y(3.6), INK, 4, 20))
    b.append(arrow(xa, Y(3.6), xa, y0, INK, 4, 20))
    b.append(lines(xa + 24, Y(1.8) - 8, ["distance moved by", "substance = 3.6 cm"], FS, "start", INK, 600, 34))
    xs = 660
    b.append(arrow(xs, y0, xs, Y(front), INK, 4, 20))
    b.append(arrow(xs, Y(front), xs, y0, INK, 4, 20))
    b.append(lines(xs - 24, Y(4.0) - 8, ["distance moved by", "solvent = 8.0 cm"], FS, "end", INK, 600, 34))
    return svg(W, H, "A strip of chromatography paper standing in a shallow band of solvent. A pencil start line is drawn across it, with two lanes labelled A and B. Lane A has three spots: yellow, blue and red, going up the paper. Lane B has one blue spot, level with the blue spot in lane A, 3.6 cm above the start line. A dashed line marks the solvent front, 8.0 cm above the start line. A double-headed arrow shows the distance moved by the blue substance, 3.6 cm, and another shows the distance moved by the solvent, 8.0 cm.", b)


# ------------------------------------------------------------------ 2  testing for gases
def limewater_test():
    W, H = 720, 590
    b = []
    lx, rx, hw = 150, 540, 60
    top, bot_c = 170, 400
    # liquids first, then the glass over them
    b.append(pathel(_tube_fill(lx, hw, 300, bot_c), "none", 1, "#F0E2B8"))
    b.append(pathel(_tube_fill(rx, hw, 290, bot_c), "none", 1, "#FFFFFF"))
    b.append(pathel(_tube(lx, hw, top, bot_c), INK, 4))
    b.append(pathel(_tube(rx, hw, top, bot_c), INK, 4))
    b.append(line(lx - hw, 300, lx + hw, 300, INK, 2.6, "butt"))
    b.append(line(rx - hw, 290, rx + hw, 290, INK, 2.6, "butt"))
    # the bung, and the delivery tube that leaves it and dips into the limewater
    b.append(rect(lx - hw - 10, top - 40, 2 * hw + 20, 50, "#8A6A4A", INK, 3, 4))
    tube = "M%s,%s V%s H%s V%s" % (f(lx), top - 40, 80, f(rx), 380)
    b.append(pathel(tube, INK, 14))
    b.append(pathel(tube, "#FFFDF8", 6))
    for (bx, by, r) in ((rx - 14, 352, 9), (rx + 16, 326, 8), (rx - 6, 310, 7)):
        b.append(circ(bx, by, r, "#FFFFFF", INK, 2.6))
    # labels
    b.append(txt(330, 46, "delivery tube", FS))
    b.append(leader(330, 56, 330, 76))
    b.append(lines(lx, 520, ["reaction that", "gives off the gas"], FS, "middle", INK, 600, 34))
    b.append(lines(rx, 520, ["limewater turns", "milky (cloudy)"], FS, "middle", INK, 600, 34))
    return svg(W, H, "Apparatus for testing a gas. On the left, a test tube with a bung holds the reaction that gives off the gas. A delivery tube leaves the bung, runs across and dips into a second test tube on the right. The liquid in the second tube, limewater, has turned milky white, with a few bubbles rising from the end of the delivery tube.", b)


# ------------------------------------------------------------------ 3  instrumental methods
LINES_NM = {"lithium": [610, 671], "sodium": [589], "potassium": [404, 766],
            "sample X": [589, 610, 671], "sample Y": [404, 766]}
LINE_COL = {404: "#A77BFF", 589: "#FFD60A", 610: "#FF8A1F", 671: "#FF4040", 766: "#E02A2A"}


def emission_spectra():
    W, H = 720, 450
    x0, x1 = 190, 660
    X = lambda nm: x0 + (nm - 400) * (x1 - x0) / 400.0
    sh = 40
    rows = [("lithium", 62), ("sodium", 114), ("potassium", 166), ("sample X", 244), ("sample Y", 296)]
    assert set(LINES_NM["sample X"]) == set(LINES_NM["lithium"]) | set(LINES_NM["sodium"])
    assert set(LINES_NM["sample Y"]) == set(LINES_NM["potassium"])
    b = [txt(20, 38, "reference spectra", FS, "start")]
    for name, y in rows:
        b.append(rect(x0, y, x1 - x0, sh, "#1B1A22", INK, 2.6))
        b.append(txt(x0 - 14, y + 29, name, FS, "end"))
        for nm in LINES_NM[name]:
            b.append(line(X(nm), y + 3, X(nm), y + sh - 3, LINE_COL[nm], 4, "butt"))
    ya = rows[-1][1] + sh + 10
    b.append(line(x0, ya, x1, ya, INK, 4, "butt"))
    for nm in range(400, 801, 100):
        b.append(line(X(nm), ya, X(nm), ya + 10, INK, 3, "butt"))
        b.append('<text x="%s" y="%s" font-family="%s" font-size="27" font-weight="600" text-anchor="middle" fill="%s">%s</text>' % (
            f(X(nm)), f(ya + 42), NUM_FONT, INK, nm))
    b.append(txt((x0 + x1) / 2, ya + 84, "wavelength in nm", FS))
    return svg(W, H, "Five line spectra on a shared wavelength axis from 400 to 800 nanometres. Reference spectra: lithium has lines at 610 and 671; sodium has one line at 589; potassium has lines at 404 and 766. Sample X has lines at 589, 610 and 671. Sample Y has lines at 404 and 766.", b)


REGISTRY = {
    "chromatogram": chromatogram,
    "limewater-test": limewater_test,
    "emission-spectra": emission_spectra,
}
