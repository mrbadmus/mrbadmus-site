# -*- coding: utf-8 -*-
"""figlib.ks4lean_cell: lean Biology Cell biology lesson figures (10), drafted 25 Nov 2026.
Pure standard library. REGISTRY: name -> no-arg fn returning SVG.

Drawn in figlib/ks4lean_eco.py's and figlib/ks4lean_org.py's conventions and with their helpers
(one 720 viewBox, Georgia, the same palette, own #FFFDF8 background rect, path commands M L H V C Q
Z only, no text on a dark fill, labels >= 27 at a 720 viewBox, every label outside the drawing
with a leader line). The Design pages' own figures for these lessons were either drawn for a bench
(a highlight that only made sense mid-activity) or set at 13 px in a 520-644 viewBox (about 7 px on
a phone), so each lean card that needs a diagram gets one drawn here.

Every number a figure shows is computed from the record's own data and asserted:
  cell-bacterium-scale    20 um liver cell, 2 um bacterium, 10 um scale bar, all at 14 px per um
                          (eukaryotes_prokaryotes.py, card "Size")
  osmosis-mass-graph      the six points of the Design page's own graph, 0 to 1.0 mol/dm3; the
                          drawn line crosses 0 % at 0.37 mol/dm3 (transport_in_cells.py, RP card)
  agar-plate-zones        clear zones 18 mm (A) and 28 mm (B) across, none round C or the
                          control W, on a 90 mm dish, all at one scale (culturing_microorganisms.py)
"""
import math

from .ks4lean_eco import (INK, RUST, BLUE, GREEN, BG, GREY, FS, f, svg, line, poly_line, txt,
                          lines, circ, rect, pathel, leader, arrow, poly)
from .ks4lean_org import num, vtxt, grid, ellipse, cross
from .style import STYLE, text_width_wide

LS = 27
CYTO = "#F6E7D3"        # cytoplasm
NUC = "#DCCFEA"         # nucleus
MITO = "#F2C9AE"        # mitochondria
WALL = "#CFE3B4"        # plant cell wall (cellulose)
BWALL = "#E4D3AE"       # bacterial cell wall
BCYTO = "#EAF2DA"       # bacterial cytoplasm
VAC = "#DDEEF6"         # permanent vacuole
CHL = "#5E9F55"         # chloroplasts (no text ever sits on them)
AGAR = "#E8D58A"
LAWN = "#C2A94E"
ZONE = "#F6EFD6"


def _blob(cx, cy, rx, ry):
    """a rounded, slightly irregular animal-cell outline (cubic Beziers, closed)."""
    k = 0.5523
    pts = [(cx, cy - ry), (cx + rx, cy - ry * 0.05), (cx + rx * 0.08, cy + ry), (cx - rx, cy + ry * 0.08)]
    d = "M%s,%s " % (f(pts[0][0]), f(pts[0][1]))
    d += "C%s,%s %s,%s %s,%s " % (f(cx + rx * k * 1.05), f(cy - ry), f(cx + rx), f(cy - ry * k), f(pts[1][0]), f(pts[1][1]))
    d += "C%s,%s %s,%s %s,%s " % (f(cx + rx), f(cy + ry * k * 1.1), f(cx + rx * k * 1.05), f(cy + ry), f(pts[2][0]), f(pts[2][1]))
    d += "C%s,%s %s,%s %s,%s " % (f(cx - rx * k), f(cy + ry), f(cx - rx), f(cy + ry * k), f(pts[3][0]), f(pts[3][1]))
    d += "C%s,%s %s,%s %s,%s Z" % (f(cx - rx), f(cy - ry * k * 1.1), f(cx - rx * k), f(cy - ry), f(pts[0][0]), f(pts[0][1]))
    return d


def _rrect_path(x0, y0, x1, y1, r):
    return ("M%s,%s H%s Q%s,%s %s,%s V%s Q%s,%s %s,%s H%s Q%s,%s %s,%s V%s Q%s,%s %s,%s Z"
            % (f(x0 + r), f(y0), f(x1 - r), f(x1), f(y0), f(x1), f(y0 + r), f(y1 - r), f(x1), f(y1),
               f(x1 - r), f(y1), f(x0 + r), f(x0), f(y1), f(x0), f(y1 - r), f(y0 + r), f(x0), f(y0),
               f(x0 + r), f(y0)))


def _mito(cx, cy, rx=18, ry=9):
    return ellipse(cx, cy, rx, ry, MITO, INK, 2.6)


def _ribo(cx, cy, r=4.5):
    return circ(cx, cy, r, INK, INK, 1)


# ------------------------------------------------------------------ 1  eukaryotes, card "Prokaryotic cells"
def prokaryote_cell():
    W, H = 720, 400
    x0, y0, x1, y1 = 220, 110, 500, 290            # the cell wall's outside
    t = 14                                          # wall thickness
    b = []
    b.append(rect(x0, y0, x1 - x0, y1 - y0, BWALL, INK, 3, 90))
    b.append(rect(x0 + t, y0 + t, x1 - x0 - 2 * t, y1 - y0 - 2 * t, BCYTO, INK, 3, 76))
    # the single DNA loop, free in the cytoplasm (one closed loop that never crosses itself)
    b.append(pathel("M300,200 C300,166 338,160 364,174 C392,160 424,176 420,204 "
                    "C416,236 382,242 356,230 C330,242 300,232 300,200 Z", RUST, 4.5))
    # plasmids: small separate rings of DNA
    b.append(circ(452, 164, 13, "none", BLUE, 4.5))
    b.append(circ(456, 240, 11, "none", BLUE, 4.5))
    for p in [(262, 170), (256, 234), (330, 256), (392, 150), (412, 258), (300, 146)]:
        b.append(_ribo(*p))
    # labels: left column right-aligned at LX, right column left-aligned at RX
    LX, RX = 196, 524
    b.append(lines(LX, 92, ["cell", "wall"], FS, "end", INK, 600, 32))
    b.append(leader(LX + 6, 104, 300, y0 + 7))
    b.append(lines(LX, 196, ["cell", "membrane"], FS, "end", INK, 600, 32))
    b.append(leader(LX + 6, 206, x0 + t, 200))
    b.append(txt(LX, 334, "cytoplasm", FS, "end"))
    b.append(leader(LX + 6, 326, 282, 262))
    b.append(lines(RX, 92, ["single", "DNA loop"], FS, "start", INK, 600, 32))
    b.append(leader(RX - 6, 104, 410, 178))
    b.append(txt(RX, 214, "plasmids", FS, "start"))
    b.append(leader(RX - 6, 206, 465, 166))
    b.append(txt(RX, 334, "ribosomes", FS, "start"))
    b.append(leader(RX - 6, 326, 416, 261))
    return svg(W, H, "A bacterial cell. A cell wall surrounds the cell membrane, which holds the "
                     "cytoplasm. In the cytoplasm are a single loop of DNA, two small rings of DNA "
                     "called plasmids, and ribosomes. There is no nucleus.", b)


# ------------------------------------------------------------------ 2  eukaryotes, card "Size"
PX_PER_UM = 14.0
LIVER_UM, BACT_UM, BAR_UM = 20.0, 2.0, 10.0


def cell_bacterium_scale():
    W, H = 720, 420
    r = LIVER_UM * PX_PER_UM / 2.0                 # 140 px: a 20 um liver cell
    bl, bh = BACT_UM * PX_PER_UM, BACT_UM * PX_PER_UM / 2.0
    bar = BAR_UM * PX_PER_UM
    assert abs(2 * r - 280) < 1e-9 and abs(bl - 28) < 1e-9 and abs(bar - 140) < 1e-9
    assert abs((2 * r) / bl - 10) < 1e-9              # one order of magnitude
    cx, cy = 190, 190
    b = []
    b.append(pathel(_blob(cx, cy, r, r * 0.96), INK, 3, CYTO))
    b.append(circ(cx - 12, cy - 6, 38, NUC, INK, 2.6))
    for p in [(cx + 70, cy - 70), (cx - 80, cy + 60), (cx + 66, cy + 70)]:
        b.append(_mito(*p))
    bx, by = 560, 190
    b.append(rect(bx - bl / 2, by - bh / 2, bl, bh, BWALL, INK, 2.6, bh / 2))
    b.append(lines(cx, 370, ["liver cell", "about 20 µm"], FS, "middle", INK, 600, 34))
    b.append(lines(bx, 104, ["bacterium", "about 2 µm"], FS, "middle", INK, 600, 34))
    b.append(leader(bx, 146, bx, by - bh / 2 - 4))
    # scale bar: 10 um
    sx0, sy = bx - bar / 2, 300
    b.append(line(sx0, sy, sx0 + bar, sy, INK, 5, "butt"))
    b.append(line(sx0, sy - 12, sx0, sy + 12, INK, 3, "butt"))
    b.append(line(sx0 + bar, sy - 12, sx0 + bar, sy + 12, INK, 3, "butt"))
    b.append(txt(bx, sy + 48, "10 µm", FS))
    return svg(W, H, "A liver cell about 20 micrometres across, with a nucleus and mitochondria, "
                     "beside a rod-shaped bacterium about 2 micrometres long, drawn to the same "
                     "scale. A scale bar shows 10 micrometres. The liver cell is about ten times "
                     "longer than the bacterium.", b)


# ------------------------------------------------------------------ 3  animal and plant cells
def animal_plant_cells():
    W, H = 720, 880
    b = []
    # ---- animal cell (top)
    cx, cy, rx, ry = 360, 220, 140, 130
    b.append(txt(cx, 40, "Animal cell", FS, "middle", INK, 700))
    b.append(pathel(_blob(cx, cy, rx, ry), INK, 3.5, CYTO))
    b.append(circ(330, 200, 44, NUC, INK, 2.6))
    for p in [(430, 140), (300, 300), (420, 290)]:
        b.append(_mito(*p))
    for p in [(270, 150), (260, 236), (360, 120), (452, 214), (380, 268), (400, 180)]:
        b.append(_ribo(*p))
    LX, RX = 196, 524
    b.append(txt(LX, 150, "nucleus", FS, "end"))
    b.append(leader(LX + 6, 142, 300, 186))
    b.append(lines(LX, 246, ["cell", "membrane"], FS, "end", INK, 600, 32))
    b.append(leader(LX + 6, 256, cx - rx + 2, 236))
    b.append(txt(LX, 360, "cytoplasm", FS, "end"))
    b.append(leader(LX + 6, 352, 262, 286))
    b.append(txt(RX, 96, "mitochondria", LS, "start"))
    b.append(leader(RX + 20, 108, 440, 133))
    b.append(txt(RX, 230, "ribosomes", FS, "start"))
    b.append(leader(RX - 6, 222, 457, 214))
    # ---- plant cell (bottom)
    x0, y0, x1, y1, t = 220, 480, 500, 820, 14
    b.append(txt(360, 450, "Plant cell", FS, "middle", INK, 700))
    b.append(rect(x0, y0, x1 - x0, y1 - y0, WALL, INK, 3, 8))
    b.append(rect(x0 + t, y0 + t, x1 - x0 - 2 * t, y1 - y0 - 2 * t, CYTO, INK, 2.6, 6))
    vx0, vy0, vx1, vy1 = 300, 540, 450, 750
    b.append(rect(vx0, vy0, vx1 - vx0, vy1 - vy0, VAC, INK, 2.6, 26))
    b.append(circ(267, 590, 24, NUC, INK, 2.6))
    for (ex, ey) in [(267, 670), (267, 748), (340, 516), (410, 516), (375, 774)]:
        b.append(ellipse(ex, ey, 16, 9, CHL, INK, 2.6))
    b.append(ellipse(468, 610, 9, 16, CHL, INK, 2.6))
    b.append(_mito(468, 700, 9, 14))
    for p in [(250, 520), (288, 790), (470, 520), (470, 790)]:
        b.append(_ribo(*p))
    b.append(lines(LX, 506, ["cell wall", "(cellulose)"], FS, "end", INK, 600, 32))
    b.append(leader(LX + 6, 518, x0 + 7, 540))
    b.append(txt(LX, 600, "nucleus", FS, "end"))
    b.append(leader(LX + 6, 592, 243, 590))
    b.append(txt(LX, 690, "chloroplast", FS, "end"))
    b.append(leader(LX + 6, 682, 251, 670))
    b.append(txt(LX, 786, "cytoplasm", FS, "end"))
    b.append(leader(LX + 6, 778, 252, 770))
    b.append(lines(RX, 610, ["permanent", "vacuole"], FS, "start", INK, 600, 32))
    b.append(leader(RX - 6, 622, 430, 650))
    b.append(lines(RX, 760, ["cell", "membrane"], FS, "start", INK, 600, 32))
    b.append(leader(RX - 6, 770, x1 - t, 770))
    return svg(W, H, "Two labelled cells, not to scale. An animal cell with a nucleus, cytoplasm, "
                     "a cell membrane, mitochondria and ribosomes. A plant cell with the same parts, "
                     "plus a cellulose cell wall outside the cell membrane, a large permanent "
                     "vacuole and chloroplasts.", b)


# ------------------------------------------------------------------ 4  cell specialisation, sperm
def sperm_cell():
    W, H = 720, 330
    cy = 190
    b = []
    # tail: a wave from the mid-piece to the right
    d = "M330,%s" % f(cy)
    x = 330
    for i in range(4):
        d += " Q%s,%s %s,%s" % (f(x + 44), f(cy - 34 if i % 2 == 0 else cy + 34), f(x + 88), f(cy))
        x += 88
    b.append(pathel(d, INK, 6))
    # mid-piece packed with mitochondria
    b.append(rect(236, cy - 16, 100, 32, CYTO, INK, 2.6, 10))
    for mx in (256, 286, 316):
        b.append(ellipse(mx, cy, 12, 9, MITO, INK, 2.6))
    # head: nucleus inside, enzyme cap at the front
    b.append(ellipse(160, cy, 82, 52, CYTO, INK, 3))
    b.append(pathel("M100,%s Q102,%s 140,%s Q118,%s 118,%s Q118,%s 140,%s Q102,%s 100,%s Z"
                    % (f(cy - 36), f(cy - 50), f(cy - 51), f(cy - 30), f(cy), f(cy + 30), f(cy + 51),
                       f(cy + 50), f(cy + 36)), INK, 2.6, "#F2E7B8"))
    b.append(ellipse(176, cy, 50, 34, NUC, INK, 2.6))
    b.append(lines(84, 58, ["enzymes"], FS, "middle", INK, 600, 32))
    b.append(leader(84, 70, 106, cy - 30))
    b.append(txt(250, 58, "nucleus", FS, "middle"))
    b.append(leader(236, 70, 186, cy - 14))
    b.append(txt(470, 58, "mitochondria", FS, "middle"))
    b.append(leader(420, 70, 290, cy - 10))
    b.append(txt(560, 300, "tail", FS, "middle"))
    b.append(leader(560, 270, 562, cy + 6))
    return svg(W, H, "A sperm cell. The head holds a nucleus, with a cap of enzymes at the front. "
                     "Behind the head, a short section is packed with mitochondria. A long tail "
                     "makes up the rest of the cell.", b)


# ------------------------------------------------------------------ 5  cell specialisation, nerve
def nerve_cell():
    W, H = 720, 340
    cy = 180
    b = []
    # dendrites from the cell body (branches)
    for (x2, y2, x3, y3) in [(70, 96, 40, 70), (54, 156, 26, 140), (64, 236, 34, 270), (130, 270, 120, 306),
                              (150, 92, 160, 60)]:
        b.append(line(140, cy, x2, y2, INK, 4))
        b.append(line(x2, y2, x3, y3, INK, 3))
    # the long axon
    b.append(line(186, cy, 600, cy, INK, 7, "butt"))
    # branched endings
    for (x2, y2) in [(660, 120), (676, 170), (672, 222), (648, 264)]:
        b.append(line(600, cy, x2, y2, INK, 4))
        b.append(circ(x2, y2, 7, INK, INK, 1))
    b.append(circ(140, cy, 52, CYTO, INK, 3))
    b.append(circ(140, cy, 22, NUC, INK, 2.6))
    b.append(txt(300, 60, "nucleus", FS, "middle"))
    b.append(leader(260, 72, 152, cy - 14))
    b.append(txt(400, 250, "long axon", FS, "middle"))
    b.append(leader(400, 222, 400, cy + 6))
    b.append(lines(560, 60, ["branched", "endings"], FS, "end", INK, 600, 32))
    b.append(leader(566, 66, 655, 124))
    return svg(W, H, "A nerve cell. A cell body with a nucleus has short branches. A long axon "
                     "runs from the cell body, and its far end splits into branched endings.", b)


# ------------------------------------------------------------------ 6  cell specialisation, root hair
def root_hair_cell():
    W, H = 720, 380
    b = []
    wall = "M60,120 H260 V190 H636 Q680,190 680,210 Q680,230 636,230 H260 V300 H60 Z"
    memb = "M72,132 H248 V202 H636 Q668,202 668,210 Q668,218 636,218 H248 V288 H72 Z"
    b.append(pathel(wall, INK, 3, WALL))
    b.append(pathel(memb, INK, 2.6, CYTO))
    b.append(rect(116, 160, 116, 100, VAC, INK, 2.6, 20))
    b.append(circ(93, 186, 15, NUC, INK, 2.6))
    for p in [(93, 250), (174, 146), (174, 274)]:
        b.append(_mito(p[0], p[1], 11, 6))
    b.append(_mito(420, 210, 11, 4))
    b.append(lines(460, 104, ["root hair: a large", "surface area"], FS, "middle", INK, 600, 32))
    b.append(leader(462, 150, 470, 192))          # starts clear below "surface area" (baseline 136)
    b.append(txt(124, 90, "cell wall", FS, "middle"))
    b.append(leader(124, 100, 124, 124))
    b.append(txt(93, 352, "nucleus", FS, "middle"))
    b.append(leader(93, 322, 93, 202))
    b.append(txt(330, 352, "mitochondria", FS, "middle"))
    b.append(leader(300, 324, 182, 277))
    return svg(W, H, "A root hair cell. A plant cell with a cell wall, nucleus, vacuole and "
                     "mitochondria, with a long thin root hair growing out from one side. The root "
                     "hair gives a large surface area.", b)


# ------------------------------------------------------------------ 7  chromosomes and mitosis
def _chrom_x(cx, cy, c, s=10):
    """a copied chromosome: two identical copies joined, drawn as an X."""
    return line(cx - s * 0.5, cy - s, cx + s * 0.5, cy + s, c, 6) + line(cx + s * 0.5, cy - s, cx - s * 0.5, cy + s, c, 6)


def _chrom_bar(cx, cy, c, s=10):
    return line(cx, cy - s, cx, cy + s, c, 6)


def cell_cycle_stages():
    W, H = 720, 400
    cy = 160
    b = []
    # stage 1: the cell has grown and its DNA has replicated (each chromosome now two copies)
    b.append(circ(112, cy, 84, CYTO, INK, 3))
    b.append(circ(112, cy, 46, NUC, INK, 2.6))
    for (dx, dy, c) in [(-18, -16, RUST), (16, -16, BLUE), (-18, 18, RUST), (16, 18, BLUE)]:
        b.append(_chrom_x(112 + dx, cy + dy, c))
    for p in [(70, 96), (164, 112), (66, 220), (160, 212)]:
        b.append(_mito(p[0], p[1], 12, 6))
    b.append(arrow(204, cy, 266, cy, INK, 5, 18))
    # stage 2: mitosis, one set of chromosomes pulled to each end, the nucleus divides
    b.append(ellipse(360, cy, 88, 70, CYTO, INK, 3))
    for nx in (320, 400):
        b.append(circ(nx, cy, 28, NUC, INK, 2.6))
        for (dx, dy, c) in [(-9, -10, RUST), (9, -10, BLUE), (-9, 12, RUST), (9, 12, BLUE)]:
            b.append(_chrom_bar(nx + dx, cy + dy, c, 8))
    b.append(arrow(452, cy, 496, cy, INK, 5, 18))
    # stage 3: the cytoplasm and cell membrane divide: two identical cells
    for ccx in (552, 652):
        b.append(circ(ccx, cy, 50, CYTO, INK, 3))
        b.append(circ(ccx, cy, 24, NUC, INK, 2.6))
        for (dx, dy, c) in [(-8, -8, RUST), (8, -8, BLUE), (-8, 10, RUST), (8, 10, BLUE)]:
            b.append(_chrom_bar(ccx + dx, cy + dy, c, 7))
    b.append(lines(112, 290, ["1  cell grows,", "DNA replicates"], FS, "middle", INK, 600, 34))
    b.append(lines(360, 290, ["2  mitosis:", "nucleus divides"], FS, "middle", INK, 600, 34))
    b.append(lines(602, 290, ["3  cytoplasm", "divides"], FS, "middle", INK, 600, 34))
    return svg(W, H, "The three stages of the cell cycle. Stage 1: the cell grows and its DNA "
                     "replicates, so each chromosome is now two copies. Stage 2: mitosis, one set "
                     "of chromosomes is pulled to each end of the cell and the nucleus divides. "
                     "Stage 3: the cytoplasm and cell membrane divide to form two identical cells, "
                     "each with the same chromosomes.", b)


# ------------------------------------------------------------------ 8  transport in cells
def _dots(pts, r, fill):
    return "".join(circ(x, y, r, fill, INK, 2.6) for x, y in pts)


def _scatter(n, x0, x1, y0, y1, seed):
    """n points spread evenly over a box (a fixed lattice, jittered by a fixed rule)."""
    cols = max(1, int(round(math.sqrt(n * (x1 - x0) / float(y1 - y0)))))
    rows = int(math.ceil(n / float(cols)))
    out = []
    for i in range(n):
        c, r = i % cols, i // cols
        jx = ((i * 37 + seed * 11) % 13 - 6) * 0.9
        jy = ((i * 53 + seed * 7) % 11 - 5) * 0.9
        out.append((x0 + (c + 0.5) * (x1 - x0) / cols + jx, y0 + (r + 0.5) * (y1 - y0) / rows + jy))
    return out


def transport_processes():
    W, H = 720, 740
    MX = 360                                       # the membrane
    rows = [("Diffusion", "no energy needed", "higher", "lower"),
            ("Osmosis", "water only", "dilute", "concentrated"),
            ("Active transport", "needs energy", "lower", "higher")]
    b = []
    for k, (name, note, left, right) in enumerate(rows):
        y0 = 20 + k * 240
        b.append(txt(120, y0 + 210, left, LS, "middle"))
        b.append(txt(608, y0 + 210, right, LS, "middle"))
        b.append(txt(24, y0 + 30, name, FS, "start", INK, 700))
        b.append(txt(696, y0 + 30, note, LS, "end", INK, 600))
        top, bot = y0 + 54, y0 + 174
        b.append(line(MX, top, MX, bot, INK, 5, "butt", "14 8"))
        if k == 0:      # diffusion: many on the left, few on the right
            b.append(_dots(_scatter(14, 60, 340, top + 6, bot - 6, 1), 9, RUST))
            b.append(_dots(_scatter(4, 390, 680, top + 20, bot - 20, 2), 9, RUST))
            b.append(arrow(236, y0 + 200, 486, y0 + 200, RUST, 6, 22))
        elif k == 1:    # osmosis: water (small) dilute -> concentrated; solute (large) cannot cross
            # solute first, then water on top, each set on its own rows so none is hidden
            b.append(_dots([(110, top + 60), (220, top + 30), (300, top + 90)], 15, AGAR))
            b.append(_dots([(x, y) for y in (top + 22, top + 60, top + 98) for x in (70, 150, 180, 260, 330)
                            if (x, y) not in ((150, top + 60),)][:14], 6, VAC))
            b.append(_dots([(x, y) for y in (top + 26, top + 94) for x in (410, 480, 550, 620)], 15, AGAR))
            b.append(_dots([(445, top + 60), (515, top + 60), (585, top + 60), (655, top + 60), (660, top + 26)], 6, VAC))
            b.append(arrow(236, y0 + 200, 486, y0 + 200, BLUE, 6, 22))
        else:           # active transport: few on the left, many on the right
            b.append(_dots(_scatter(4, 60, 340, top + 20, bot - 20, 7), 9, GREEN))
            b.append(_dots(_scatter(14, 390, 680, top + 6, bot - 6, 8), 9, GREEN))
            b.append(arrow(236, y0 + 200, 486, y0 + 200, GREEN, 6, 22))
    return svg(W, H, "Three ways substances cross a cell membrane, each drawn with the membrane as "
                     "a dashed line. Diffusion: particles move from the side where their "
                     "concentration is higher to the side where it is lower, with no energy needed. "
                     "Osmosis: water molecules move from a dilute solution to a concentrated "
                     "solution, while the larger solute particles stay where they are. Active "
                     "transport: particles move from the side where their concentration is lower to "
                     "the side where it is higher, using energy from respiration.", b)


# ------------------------------------------------------------------ 9  transport in cells, RP
OSMO_PTS = [(0.0, 20.0), (0.2, 10.0), (0.4, -2.0), (0.6, -12.0), (0.8, -19.0), (1.0, -24.0)]


def _catmull(pts, steps=24):
    out = []
    P = [pts[0]] + list(pts) + [pts[-1]]
    for i in range(1, len(P) - 2):
        p0, p1, p2, p3 = P[i - 1], P[i], P[i + 1], P[i + 2]
        for s in range(steps):
            t = s / float(steps)
            t2, t3 = t * t, t * t * t
            out.append(tuple(0.5 * ((2 * p1[j]) + (-p0[j] + p2[j]) * t + (2 * p0[j] - 5 * p1[j] + 4 * p2[j] - p3[j]) * t2
                                    + (-p0[j] + 3 * p1[j] - 3 * p2[j] + p3[j]) * t3) for j in (0, 1)))
    out.append(pts[-1])
    return out


def osmosis_crossing():
    curve = _catmull(OSMO_PTS, 200)
    for (xa, ya), (xb, yb) in zip(curve, curve[1:]):
        if ya >= 0 > yb:
            return xa + (xb - xa) * ya / (ya - yb)
    raise ValueError("the osmosis curve does not cross 0")


def osmosis_mass_graph():
    W, H = 720, 560
    x0, x1, yt, yb = 130, 690, 40, 440
    vmin, vmax = -30.0, 30.0
    X = lambda c: x0 + c * (x1 - x0)
    Y = lambda v: yt + (vmax - v) * (yb - yt) / (vmax - vmin)
    cross0 = osmosis_crossing()
    assert abs(cross0 - 0.37) < 0.01, cross0
    b = []
    for v in range(-30, 31, 10):
        b.append(grid(x0, Y(v), x1, Y(v)))
        # 24 units left of the axis: the cross on the axis at (0, +20) reaches 13 units left of it
        b.append(num(x0 - 24, Y(v) + 9, ("+%d" % v) if v > 0 else ("−%d" % -v if v < 0 else "0"), "end"))
    for i in range(6):
        c = i * 0.2
        b.append(line(X(c), Y(0), X(c), Y(0) + 10, INK, 3, "butt"))
    b.append(line(x0, yt, x0, yb, INK, 4, "butt"))
    b.append(line(x0, Y(0), x1, Y(0), INK, 4, "butt"))
    for i in range(6):
        c = i * 0.2
        b.append(num(X(c), yb + 36, "0" if i == 0 else ("1.0" if i == 5 else "%.1f" % c)))
    b.append(txt((x0 + x1) / 2, yb + 78, "sugar concentration in mol/dm³", LS))
    b.append(vtxt(34, (yt + yb) / 2, "% change in mass"))   # 34: clears the moved tick numerals
    b.append(poly_line([(X(c), Y(v)) for c, v in _catmull(OSMO_PTS)], RUST, 4.5))
    for c, v in OSMO_PTS:
        b.append(cross(X(c), Y(v)))
    # where the line crosses 0 %
    b.append(circ(X(cross0), Y(0), 8, BG, INK, 3.5))
    # a plate in the paper colour under the label, so the +10 gridline does not strike through it
    lw = max(text_width_wide(t, LS, True) for t in ("no net movement", "of water"))
    b.append(rect(X(cross0) + 18, Y(0) - 92, lw + 18, 72, BG, "none", 0))
    b.append(lines(X(cross0) + 26, Y(0) - 62, ["no net movement", "of water"], LS, "start", INK, 600, 32))
    b.append(leader(X(cross0) + 22, Y(0) - 44, X(cross0) + 6, Y(0) - 6))
    return svg(W, H, "A graph of percentage change in mass of potato against sugar concentration, "
                     "from 0 to 1.0 mol per dm cubed. The points are +20 at 0, +10 at 0.2, minus 2 "
                     "at 0.4, minus 12 at 0.6, minus 19 at 0.8 and minus 24 at 1.0. A smooth line "
                     "through them crosses 0 per cent at about 0.37 mol per dm cubed, marked no net "
                     "movement of water.", b)


# ------------------------------------------------------------------ 10  culturing microorganisms, RP2
DISH_MM = 90.0
ZONES = [("A", -90, -90, 18.0), ("B", 90, -90, 28.0), ("C", -90, 90, 0.0), ("W", 90, 90, 0.0)]


def agar_plate_zones():
    W, H = 720, 560
    cx, cy, R = 258, 280, 230                       # R: the agar's radius, a 90 mm dish
    k = R / (DISH_MM / 2.0)                         # px per mm
    disc_r = 24
    b = []
    b.append(circ(cx, cy, R + 12, "#EFEADB", INK, 3))
    b.append(circ(cx, cy, R, AGAR, INK, 2.6))
    zr = {}
    for name, dx, dy, d in ZONES:
        zr[name] = d * k / 2.0
    assert abs(zr["A"] / k * 2 - 18) < 1e-9 and abs(zr["B"] / k * 2 - 28) < 1e-9
    # the lawn: every spot outside the clear zones and the discs
    n = 420
    for i in range(n):
        a = i * 2.39996
        r = (R - 10) * math.sqrt((i + 0.5) / n)
        x, y = cx + r * math.cos(a), cy + r * math.sin(a)
        clear = False
        for name, dx, dy, d in ZONES:
            if math.hypot(x - (cx + dx), y - (cy + dy)) < max(zr[name], disc_r) + 6:
                clear = True
        if not clear:
            b.append(circ(x, y, 3.2, LAWN, LAWN, 1))
    for name, dx, dy, d in ZONES:
        if zr[name]:
            b.append(circ(cx + dx, cy + dy, zr[name], ZONE, INK, 2.6))
    for name, dx, dy, d in ZONES:
        b.append(circ(cx + dx, cy + dy, disc_r, "#FFFFFF", INK, 2.6))
        b.append(txt(cx + dx, cy + dy + 10, name, LS, "middle", INK, 700))
    RX = 522
    ax, ay = cx - 90, cy - 90
    end = (ax + 35 * math.cos(math.radians(-75)), ay + 35 * math.sin(math.radians(-75)))
    b.append(lines(430, 44, ["clear zone", "18 mm across"], LS, "start", INK, 600, 32))
    b.append(leader(422, 36, end[0], end[1]))
    # the leader ends in A's zone, outside disc A, and clears B's zone by more than 30 units
    bx, by = cx + 90, cy - 90
    dx, dy = end[0] - 422, end[1] - 36
    gap = abs(dx * (by - 36) - dy * (bx - 422)) / math.hypot(dx, dy) - zr["B"]
    assert disc_r < 35 < zr["A"] and gap > 30, gap
    b.append(lines(RX, 214, ["clear zone", "28 mm across"], LS, "start", INK, 600, 32))
    b.append(leader(RX - 6, 210, cx + 90 + 50, cy - 90 + 20))
    b.append(lines(RX, 316, ["lawn of", "bacteria"], LS, "start", INK, 600, 32))
    b.append(leader(RX - 6, 316, cx + 196, cy + 20))
    b.append(lines(RX, 430, ["paper", "disc"], LS, "start", INK, 600, 32))
    b.append(leader(RX - 6, 430, cx + 90 + disc_r, cy + 90))
    return svg(W, H, "An agar plate covered in a lawn of bacteria, with four paper discs. Disc A, "
                     "an antibiotic, has a clear zone 18 millimetres across. Disc B, another "
                     "antibiotic, has a clear zone 28 millimetres across. Disc C, a third antibiotic, "
                     "and disc W, the control soaked in sterile water, have no clear zone.", b)


REGISTRY = {
    "prokaryote-cell": prokaryote_cell,
    "cell-bacterium-scale": cell_bacterium_scale,
    "animal-plant-cells": animal_plant_cells,
    "sperm-cell": sperm_cell,
    "nerve-cell": nerve_cell,
    "root-hair-cell": root_hair_cell,
    "cell-cycle-stages": cell_cycle_stages,
    "transport-processes": transport_processes,
    "osmosis-mass-graph": osmosis_mass_graph,
    "agar-plate-zones": agar_plate_zones,
}
