# -*- coding: utf-8 -*-
"""figlib.ks4lean_chemfig: lean Quantitative chemistry lesson figures that REPLACE five kept Design
figures (`legacy-fig:<prop>`), which sat in sideways scrollers on a phone. DRAFT, 16 Nov 2026.
Pure standard library. REGISTRY: name -> no-arg fn returning SVG.

Drawn in figlib/ks4lean_eco.py's conventions and with its helpers (one 720 viewBox, Georgia 28,
the same palette, own #FFFDF8 background rect, path commands M L H V Q Z only, no text on a dark
fill). Each figure keeps the labels and science of the Design figure it replaces (the logic after
the batch-11 port rulings, the science rulings and the record's logic_edits); only the layout
changes. Formulae carry real subscripts (CO₂, H₂O, O₂).
"""
try:
    from .ks4lean_eco import (INK, RED, GREEN, GREY, BG, FS, f, svg, line, txt, lines, circ, rect,
                              poly, pathel, arrow)
except ImportError:                      # the scratch draft, imported with figlib on sys.path
    from figlib.ks4lean_eco import (INK, RED, GREEN, GREY, BG, FS, f, svg, line, txt, lines, circ,
                                    rect, poly, pathel, arrow)

# the Design figures' own fills (batch-11 logic: TAN, SKY, LEAF, PAPER, the chip and carbon greys)
TAN, SKY, LEAF, PAPER = "#F2C9AE", "#DDEEF6", "#A9D9BE", "#FFFDF8"
CHIP, CARBON = "#D8D2C4", "#5B5B5B"
P = 36                                   # line pitch: two different labels, 28 high, never touch


def ellipse(cx, cy, rx, ry, fill, stroke=INK, w=3):
    return '<ellipse cx="%s" cy="%s" rx="%s" ry="%s" fill="%s" stroke="%s" stroke-width="%s"/>' % (
        f(cx), f(cy), f(rx), f(ry), fill, stroke, w)


def stack(x, y, rows, anchor="middle"):
    """rows: (text, fill, weight). One label block, P apart."""
    return "".join(txt(x, y + i * P, s, FS, anchor, c, w) for i, (s, c, w) in enumerate(rows))


# ------------------------------------------------------------------ chemical-measurements: nlFig
def measurement_number_line():
    W, H = 720, 300
    x0, x1, lo, hi = 80, 640, 24.0, 24.4
    X = lambda v: x0 + (v - lo) / (hi - lo) * (x1 - x0)
    yl = 172
    b = []
    # the range bracket over the readings
    b.append(txt(X(24.2), 44, "range 0.20", FS, "middle", RED, 700))
    b.append(pathel("M%s,88 V66 H%s V88" % (f(X(24.1)), f(X(24.3))), RED, 4))
    # the three readings
    for v in (24.10, 24.30, 24.20):
        b.append(circ(X(v), 116, 12, GREEN, INK, 2.6))
    # the mean marker, pointing down at 24.20
    b.append(poly([(X(24.2), 164), (X(24.2) - 13, 138), (X(24.2) + 13, 138)], INK, INK, 1))
    # the number line
    b.append(line(x0, yl, x1, yl, INK, 4, "butt"))
    for v in (24.0, 24.1, 24.2, 24.3, 24.4):
        b.append(line(X(v), yl - 10, X(v), yl + 10, INK, 3, "butt"))
        b.append(txt(X(v), yl + 46, "%.2f" % v, FS))
    b.append(txt(X(24.2), 274, "mean 24.20 ± 0.10 cm³", FS, "middle", INK, 700))
    return svg(W, H, "Three readings 24.10, 24.30 and 24.20 cm³ on a number line; the range bracket "
                     "spans 0.20 and the mean 24.20 sits in the middle, so the result is "
                     "24.20 ± 0.10 cm³.", b)


# ------------------------------------------------------------------ chemical-measurements: apFig
def volume_apparatus():
    W, H = 720, 940
    b = []
    # ---- burette (top left): scale 0 at the top, running down; a tap above the jet
    bx, bt, bb = 140, 24, 262
    b.append(rect(bx - 16, bt, 32, bb - bt, SKY, INK, 3, 3))
    b.append(poly([(bx - 16, bb), (bx + 16, bb), (bx + 5, bb + 22), (bx - 5, bb + 22)], SKY, INK, 3))
    b.append(line(bx, bb + 22, bx, bb + 54, INK, 6, "butt"))                 # stem
    b.append(rect(bx - 34, bb + 35, 68, 12, PAPER, INK, 3, 5))              # stopcock handle
    b.append(circ(bx, bb + 41, 11, PAPER, INK, 3))                          # stopcock barrel
    b.append(poly([(bx - 6, bb + 54), (bx + 6, bb + 54), (bx, bb + 74)], SKY, INK, 2.6))   # jet
    for i in range(5):
        y = bt + 26 + i * 50
        b.append(line(bx + 16, y, bx + 32, y, INK, 3, "butt"))
        b.append(txt(bx + 42, y + 10, str(i * 10), FS, "start"))
    b.append(stack(180, 390, [("burette", INK, 700), ("±0.05 cm³ a reading", GREY, 600)]))
    # ---- pipette (top right): the red fill mark on the upper stem
    px = 540
    b.append(line(px, 24, px, 132, INK, 6, "butt"))
    b.append(ellipse(px, 184, 28, 54, SKY, INK, 3))
    b.append(line(px, 238, px, 330, INK, 6, "butt"))
    b.append(line(px - 18, 92, px + 18, 92, RED, 4, "butt"))
    b.append(stack(540, 390, [("pipette", INK, 700), ("the smallest uncertainty", GREY, 600),
                              ("for that volume", GREY, 600)]))
    # ---- measuring cylinder (bottom left): scale 0 at the bottom, running up
    cx, ct, cb = 140, 516, 756
    b.append(rect(cx - 32, ct, 64, cb - ct, SKY, INK, 3, 4))
    b.append(rect(cx - 56, cb - 4, 112, 16, PAPER, INK, 3, 3))
    for i in range(5):
        y = cb - 26 - i * 50
        b.append(line(cx + 32, y, cx + 48, y, INK, 3, "butt"))
        b.append(txt(cx + 58, y + 10, str(i * 25), FS, "start"))
    b.append(stack(180, 820, [("measuring cylinder", INK, 700), ("scale runs up", GREY, 600),
                              ("marks further apart,", GREY, 600), ("bigger uncertainty", GREY, 600)]))
    # ---- meniscus close-up (bottom right): read the bottom of the curve, at eye level
    mx0, mx1, my0, my1 = 410, 630, 540, 700
    mid, top = (mx0 + mx1) // 2, my0 + 60
    b.append(rect(mx0, my0, mx1 - mx0, my1 - my0, PAPER, INK, 3, 10))
    b.append(pathel("M%d,%d Q%d,%d %d,%d V%d H%d Z" % (mx0 + 4, top, mid, top + 52, mx1 - 4, top, my1 - 4, mx0 + 4),
                    "none", 2.6, SKY))
    b.append(pathel("M%d,%d Q%d,%d %d,%d" % (mx0 + 4, top, mid, top + 52, mx1 - 4, top), INK, 3))
    b.append(arrow(712, top + 26, mid + 8, top + 26, RED, 4, 22))
    b.append(stack(540, 756, [("read the bottom", GREY, 600), ("of the meniscus,", GREY, 600),
                              ("at eye level", GREY, 600)]))
    return svg(W, H, "Burette (scale running downwards, with a tap above the jet), pipette (one fixed "
                     "volume) and measuring cylinder (scale running upwards), with a close-up of a "
                     "meniscus read from its bottom at eye level.", b)


# ------------------------------------------------------------------ mass-changes-reactions: bFig
def _flask(b, x, sealed, before, after, label):
    # reading on the balance
    b.append(rect(x - 160, 340, 320, 100, PAPER, INK, 3, 10))
    b.append(txt(x, 380, before + " then", FS, "middle", RED, 700))
    b.append(txt(x, 418, after, FS, "middle", RED, 700))
    # the conical flask of acid and marble chips
    b.append(pathel("M%s,156 V214 L%s,334 H%s L%s,214 V156 Z" % (f(x - 26), f(x - 104), f(x + 104), f(x + 26)),
                    INK, 3, SKY))
    b.append(circ(x - 16, 314, 11, CHIP, INK, 2.6))
    b.append(circ(x + 18, 320, 11, CHIP, INK, 2.6))
    if sealed:
        b.append(rect(x - 34, 136, 68, 30, TAN, INK, 3, 5))
    else:
        b.append(arrow(x, 148, x, 70, GREEN, 5, 22))
        b.append(arrow(x - 20, 150, x - 48, 80, GREEN, 4, 20))
        b.append(arrow(x + 20, 150, x + 48, 80, GREEN, 4, 20))
        b.append(txt(x, 46, "CO₂ leaves", FS, "middle", GREEN, 700))
    b.append(txt(x, 490, label, FS, "middle", INK, 700))


def open_sealed_flasks():
    W, H = 720, 516
    b = []
    _flask(b, 180, False, "152.40 g", "150.20 g", "open: reading falls")
    _flask(b, 540, True, "152.40 g", "152.40 g", "sealed: reading stays")
    return svg(W, H, "Two flasks of marble chips in acid on balances: the open flask’s reading falls "
                     "from 152.40 g to 150.20 g as carbon dioxide leaves; the sealed flask stays at "
                     "152.40 g.", b)


# ------------------------------------------------------------------ amounts-in-equations: rFig
def mole_ratio_bars():
    W, H = 720, 512
    mg, scale, base = 2, 120, 368              # the lean page's state: mg = MG[0] = 2 mol
    b = []
    b.append(txt(360, 44, "ratio 2 : 1 : 2", FS, "middle", INK, 700))
    bars = [("Mg", 2, mg, TAN), ("O₂", 1, mg / 2.0, SKY), ("MgO", 2, mg, LEAF)]
    for i, (name, coef, n, fill) in enumerate(bars):
        x, h = 130 + i * 230, n * scale
        b.append(rect(x - 70, base - h, 140, h, fill, INK, 3, 6))
        b.append(txt(x, base - h - 16, "%g mol" % n, FS, "middle", INK, 700))
        b.append(txt(x, base + 44, name, FS, "middle", INK, 700))
        b.append(lines(x, base + 44 + P, ["balancing", "number %d" % coef], FS, "middle", GREY, 600, 34))
    return svg(W, H, "Bars for Mg, O₂ and MgO at 2, 1 and 2 moles, keeping the 2 : 1 : 2 ratio of the "
                     "balancing numbers.", b)


# ------------------------------------------------------------------ moles: pFig
def one_mole_masses():
    W, H = 720, 664
    rows = [("carbon, C", "12 g", 40, CARBON, "atoms"),
            ("water, H₂O", "18 g", 54, SKY, "molecules"),
            ("sodium chloride, NaCl", "58.5 g", 86, PAPER, "formula units")]
    b = []
    cx, tx = 140, 280
    for i, (name, mass, w, fill, unit) in enumerate(rows):
        y0 = 16 + i * 196
        pan = y0 + 128
        # a one-mole pile on a balance showing its mass
        b.append(pathel("M%s,%s Q%s,%s %s,%s Z" % (f(cx - w), f(pan), f(cx), f(pan - 2.2 * w), f(cx + w), f(pan)),
                        INK, 2.6, fill))
        b.append(rect(cx - 110, pan, 220, 54, PAPER, INK, 3, 8))
        b.append(txt(cx, pan + 38, mass, FS, "middle", RED, 700))
        b.append(stack(tx, y0 + 62, [(name, INK, 700), ("1 mol contains", GREEN, 700),
                                     ("6.02 × 10²³ " + unit, GREEN, 700)], "start"))
    b.append(txt(360, 640, "different masses, the same number of particles", FS, "middle", GREY))
    return svg(W, H, "Three one-mole piles on balances: 12 g of carbon atoms, 18 g of water molecules, "
                     "58.5 g of sodium chloride formula units, each containing 6.02 × 10²³ particles.", b)


REGISTRY = {
    "measurement-number-line": measurement_number_line,
    "volume-apparatus": volume_apparatus,
    "open-sealed-flasks": open_sealed_flasks,
    "mole-ratio-bars": mole_ratio_bars,
    "one-mole-masses": one_mole_masses,
}
