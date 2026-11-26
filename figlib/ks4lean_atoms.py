# -*- coding: utf-8 -*-
"""figlib.ks4lean_atoms: lean Chemistry Atomic structure and the periodic table lesson figures,
drafted 26 Nov 2026. Pure standard library. REGISTRY: name -> no-arg fn returning SVG.

Drawn in figlib/ks4lean_eco.py's, figlib/ks4lean_org.py's and figlib/ks4lean_cell.py's
conventions and with their helpers (one 720 viewBox, Georgia, the same palette, own #FFFDF8
background rect, path commands M L H V C Q Z only, no text on a dark fill, labels >= 27 at a 720
viewBox, every label outside a small drawing with a leader line).

Shared helpers for the unit (every lesson's figures use them):
  shell_atom      a nucleus with its symbol, concentric shells and the electrons on them,
                  electron count per shell from ELECTRONS (asserted to sum to Z)
  electrons_of    the GCSE electronic structure of Z = 1..20 (2, 8, 8, 2 filling)
  pt_cells        the cells of the 18-column, 7-period outline of the periodic table
                  (period 1: groups 1 and 0; periods 2 and 3: groups 1, 2, 3 to 0; periods
                  4 to 7: all 18 columns), as (period, column) pairs, column 1..18
  PT_SYMBOL       the symbol at (period, column) for the elements a figure may label

The figures, by lesson part; every number a figure shows is computed from the record's own
data and asserted.

Part A (atoms-elements-compounds, mixtures, model-of-the-atom, group-7):
  Every number a figure shows is computed from the record's own data and asserted:
  aec-balance-water        2H2 + O2 -> 2H2O: 4 H and 2 O on each side (atoms_elements_compounds.py,
                           card "Balancing an equation")
  halogen-boiling-points   F2 -188, Cl2 -34, Br2 59, I2 184 degrees C (group_7.py, card "Trends down
                           the group"); bars drawn to one scale from 0 degrees C
  halogen-pull             fluorine 2,7 and chlorine 2,8,7 from electrons_of(9) and electrons_of(17)
  bohr-atom                lithium: 3 protons, 4 neutrons, electrons 2,1 = electrons_of(3)

Part B (subatomic-particles, relative-atomic-mass, electronic-structure, transition-metals):
  Every number a figure shows is computed and asserted from the record's data:
  atom-particles       lithium-7: 3 protons, 7 - 3 = 4 neutrons, 3 electrons as 2,1
  nuclear-symbol       sodium-23: atomic number 11, 23 - 11 = 12 neutrons, 11 electrons
  isotopes-hydrogen    hydrogen-1, -2, -3: 1 proton each, 0, 1, 2 neutrons, mass numbers 1, 2, 3
  atom-scale           atom radius 1e-10 m, nucleus radius 1e-14 m = 1/10 000 of it
  chlorine-abundance   3 of every 4 atoms Cl-35 (75 %), 1 of 4 Cl-37 (25 %): mean 142 / 4 = 35.5
  sodium-shells        2,8,1 = electrons_of(11)
  shell-examples       lithium 2,1; oxygen 2,6; chlorine 2,8,7 = electrons_of(3, 8, 17)
  transition-block     the central block (columns 3 to 12, periods 4 to 7) and Group 1; the
                       period 4 strip Sc to Zn with the spec's six (Cr Mn Fe Co Ni Cu) marked
  transition-colours   the colours named in transition_metals.py's "Coloured compounds" card

Part C (periodic-table, development-periodic-table, metals-non-metals, group-0, group-1):
  Every number a figure shows is computed from the data below and asserted:
  pt-first-twenty        the first 20 elements placed by electronic structure (period = shells,
                         group = outer electrons, full shell = Group 0) (periodic_table.py)
  na-cl-shells           Na 2,8,1 and Cl 2,8,7 from electrons_of(11), electrons_of(17)
  pt-metals-nonmetals    the 18-column outline; non-metals = H, He and the cells right of the
                         staircase (metals_non_metals.py)
  te-i-swap              Te 52 protons, Ar 127.6; I 53 protons, Ar 126.9 (development_periodic_table.py)
  mendeleev-gap          C, Si, a gap, then Ge in the same column
  noble-gas-shells       He 2; Ne 2,8; Ar 2,8,8 (group_0.py)
  noble-gas-boiling      He -269, Ne -246, Ar -186, Kr -153, Xe -108, Rn -62 degC (group_0.py)
  alkali-shells          Li 2,1; Na 2,8,1; K 2,8,8,1, outer electron marked (group_1.py)
"""
import math

from .ks4lean_eco import (INK, RUST, BLUE, GREEN, BG, GREY, FS, f, svg, line, poly_line, txt,
                          lines, circ, rect, pathel, leader, arrow, poly)
from .ks4lean_org import num, vtxt, ellipse, cross, grid
from .style import STYLE

LS = 27
NUC = "#F2C9AE"          # a nucleus (light, so its symbol is ink on a light fill)
PROTON = "#F4B8A6"       # a proton in a drawn nucleus (light; no text on it)
NEUTRON = "#E8E1D3"      # a neutron
ELEC = BLUE              # an electron (a dark dot, never under text)
METAL = "#DCE6F2"        # metal cells
NONMETAL = "#F6E2C8"     # non-metal cells
TRANS = "#E3EEDC"        # transition-metal cells
NOBLE = "#EFE3F3"        # Group 0 cells
HILITE = "#FFE7A3"       # a highlighted cell (light; ink text)

SYMBOLS = ["H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al", "Si", "P", "S",
           "Cl", "Ar", "K", "Ca"]
NAMES = ["hydrogen", "helium", "lithium", "beryllium", "boron", "carbon", "nitrogen", "oxygen",
         "fluorine", "neon", "sodium", "magnesium", "aluminium", "silicon", "phosphorus", "sulfur",
         "chlorine", "argon", "potassium", "calcium"]


def electrons_of(z):
    """GCSE electronic structure for Z = 1..20: shells fill 2, 8, 8, 2."""
    assert 1 <= z <= 20, z
    out, n = [], z
    for cap in (2, 8, 8, 2):
        if n <= 0:
            break
        out.append(min(cap, n))
        n -= cap
    assert sum(out) == z
    return out


# Spot checks against the spec's own example (sodium 2,8,1) and the end of the twenty.
assert electrons_of(11) == [2, 8, 1]
assert electrons_of(18) == [2, 8, 8]
assert electrons_of(19) == [2, 8, 8, 1]
assert electrons_of(20) == [2, 8, 8, 2]


def electron_points(cx, cy, r, n, start=-90.0):
    """n electron positions spaced evenly round a shell of radius r, the first at `start` degrees."""
    pts = []
    for k in range(n):
        a = math.radians(start + 360.0 * k / n)
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    return pts


def shell_atom(cx, cy, sym, shells, r0=40, step=30, er=7, sym_size=28, nuc_r=None):
    """A shell (energy level) diagram: a nucleus circle with the symbol, a circle per occupied
    shell, and the electrons on each as dark dots. Returns (body list, outer radius)."""
    b = []
    nr = nuc_r if nuc_r is not None else max(22, r0 - 16)
    assert nr < r0, (nr, r0)
    for i, n in enumerate(shells):
        r = r0 + i * step
        b.append(circ(cx, cy, r, "none", INK, 2.6))
        # inner shell of two: one at the top and one at the bottom; others evenly from the top
        for (x, y) in electron_points(cx, cy, r, n):
            b.append(circ(x, y, er, ELEC, ELEC, 1))
    b.append(circ(cx, cy, nr, NUC, INK, 2.6))
    if sym:
        b.append(txt(cx, cy + sym_size * 0.36, sym, sym_size))
    return b, r0 + (len(shells) - 1) * step


# ── the periodic table outline ───────────────────────────────────────────

def pt_cells():
    """(period, column) of every cell in the 18-column outline, periods 1..7."""
    cells = [(1, 1), (1, 18)]
    for p in (2, 3):
        cells += [(p, 1), (p, 2)] + [(p, c) for c in range(13, 19)]
    for p in (4, 5, 6, 7):
        cells += [(p, c) for c in range(1, 19)]
    return cells


def _pos_first20():
    pos = {}
    for z in range(1, 21):
        sh = electrons_of(z)
        period, outer = len(sh), sh[-1]
        if z == 1:
            col = 1
        elif z == 2:
            col = 18
        elif outer <= 2 and not (period == 1):
            col = outer
        else:
            col = outer + 10            # groups 3..7 -> columns 13..17, Group 0 (8) -> 18
        pos[(period, col)] = SYMBOLS[z - 1]
    return pos


PT_SYMBOL = _pos_first20()
PT_SYMBOL.update({
    (4, 3): "Sc", (4, 4): "Ti", (4, 5): "V", (4, 6): "Cr", (4, 7): "Mn", (4, 8): "Fe",
    (4, 9): "Co", (4, 10): "Ni", (4, 11): "Cu", (4, 12): "Zn",
    (4, 13): "Ga", (4, 14): "Ge", (4, 15): "As", (4, 16): "Se", (4, 17): "Br", (4, 18): "Kr",
    (5, 1): "Rb", (5, 2): "Sr", (5, 17): "I", (5, 18): "Xe", (6, 1): "Cs", (6, 17): "At",
    (6, 18): "Rn", (7, 1): "Fr",
})
assert PT_SYMBOL[(3, 1)] == "Na" and PT_SYMBOL[(3, 17)] == "Cl" and PT_SYMBOL[(2, 18)] == "Ne"
assert PT_SYMBOL[(4, 1)] == "K" and PT_SYMBOL[(4, 2)] == "Ca" and PT_SYMBOL[(1, 18)] == "He"
assert len(pt_cells()) == 2 + 2 * 8 + 4 * 18


def pt_outline(x0, y0, cw, ch, fill_for, label_for=None, size=LS, sw=2.6):
    """The 18 x 7 outline. fill_for(period, col) -> fill; label_for(period, col) -> text or None.
    Labels are ink on the cell's (light) fill."""
    b = []
    for (p, c) in pt_cells():
        x, y = x0 + (c - 1) * cw, y0 + (p - 1) * ch
        b.append(rect(x, y, cw, ch, fill_for(p, c), INK, sw))
        if label_for:
            s = label_for(p, c)
            if s:
                b.append(txt(x + cw / 2.0, y + ch / 2.0 + size * 0.36, s, size))
    return b


# ==================================================================
# Part A: atoms-elements-compounds, mixtures, model-of-the-atom, group-7
# ==================================================================

ATOM_A = "#F2C9AE"       # an atom of one element (light)
ATOM_B = BLUE            # an atom of another element (dark: never under text)
ATOM_H = "#DDEEF6"       # hydrogen in the balancing figure (light)
LIQ = "#DDEEF6"          # a clear solution or water
GLASS = "#FFFFFF"
JACKET = "#E3F1F8"       # condenser water jacket
SAND = "#C2A94E"
CRYSTAL = "#2F5DAA"
POS = "#F7DCD2"          # the plum pudding's ball of positive charge (light)
GOLD = "#E8C77A"
AMBER = "#B26B00"


# ------------------------------------------------------------------ atoms-elements-compounds
def _atom(x, y, fill, r=15):
    return circ(x, y, r, fill, INK, 2.6)


def _pair(x, y, fill, vertical=False, r=15):
    d = r * 0.9
    if vertical:
        return [_atom(x, y - d, fill, r), _atom(x, y + d, fill, r)]
    return [_atom(x - d, y, fill, r), _atom(x + d, y, fill, r)]


def _triple(x, y, mid, end, vertical=False, r=15):
    d = r * 1.8
    if vertical:
        return [_atom(x, y - d, end, r), _atom(x, y + d, end, r), _atom(x, y, mid, r)]
    return [_atom(x - d, y, end, r), _atom(x + d, y, end, r), _atom(x, y, mid, r)]


def aec_particle_boxes():
    W, H = 720, 500
    xs = [12, 252, 492]
    bw, top = 216, 20
    b = []
    for x0 in xs:
        b.append(rect(x0, top, bw, bw, "#FFFFFF", INK, 3, 12))
    # element: molecules of two atoms of the SAME element
    x0 = xs[0]
    for (dx, dy, v) in [(54, 62, False), (150, 58, True), (66, 150, True), (156, 166, False)]:
        b += _pair(x0 + dx, top + dy, ATOM_A, v)
    # compound: every particle the same, one B atom joined to two A atoms (fixed proportions)
    x0 = xs[1]
    for (dx, dy, v) in [(66, 52, False), (162, 112, True), (70, 166, False)]:
        b += _triple(x0 + dx, top + dy, ATOM_B, ATOM_A, v)
    # mixture: A2 molecules and single B atoms, not joined to each other
    x0 = xs[2]
    for (dx, dy, v) in [(52, 56, False), (164, 150, True), (64, 176, False)]:
        b += _pair(x0 + dx, top + dy, ATOM_A, v)
    for (dx, dy) in [(160, 46), (110, 108), (40, 118)]:
        b.append(_atom(x0 + dx, top + dy, ATOM_B))
    names = [("element", ["one type", "of atom"]), ("compound", ["elements", "combined"]),
             ("mixture", ["not", "combined"])]
    for x0, (n, sub) in zip(xs, names):
        cx = x0 + bw / 2.0
        b.append(txt(cx, 280, n, FS, "middle", INK, 700))
        b.append(lines(cx, 318, sub, LS, "middle", INK, 400, 32))
    b.append(_atom(40, 418, ATOM_A))
    b.append(txt(68, 428, "an atom of one element", LS, "start", INK, 400))
    b.append(_atom(40, 466, ATOM_B))
    b.append(txt(68, 476, "an atom of a different element", LS, "start", INK, 400))
    return svg(W, H, "Three boxes of particles. Element: every particle is two atoms of the same "
                     "kind joined together. Compound: every particle is the same, one atom of one "
                     "element joined to two atoms of another. Mixture: pairs of one kind of atom and "
                     "single atoms of another kind, side by side and not joined.", b)


def aec_balance_water():
    W, H = 720, 400
    # the record's equation: 2H2 + O2 -> 2H2O
    left = {"H": 2 * 2, "O": 1 * 2}
    right = {"H": 2 * 2, "O": 2 * 1}
    assert left == right == {"H": 4, "O": 2}
    rh, ro = 15, 21
    b = []
    for y in (110, 210):                                   # 2 H2
        b.append(_atom(70, y, ATOM_H, rh))
        b.append(_atom(96, y, ATOM_H, rh))
    b.append(txt(165, 172, "+", 40, "middle", INK, 700))
    b.append(_atom(220, 160, ATOM_A, ro))                  # O2
    b.append(_atom(256, 160, ATOM_A, ro))
    b.append(arrow(310, 160, 410, 160, INK, 6, 24))
    for (x, y) in ((540, 110), (540, 220)):                # 2 H2O
        b.append(_atom(x - 26, y + 18, ATOM_H, rh))
        b.append(_atom(x + 26, y + 18, ATOM_H, rh))
        b.append(_atom(x, y, ATOM_A, ro))
    b.append(txt(83, 290, "2H₂", FS, "middle", INK, 700))
    b.append(txt(238, 290, "O₂", FS, "middle", INK, 700))
    b.append(txt(540, 300, "2H₂O", FS, "middle", INK, 700))
    b.append(txt(160, 360, "4 H and 2 O", FS, "middle", INK, 400))
    b.append(txt(540, 360, "4 H and 2 O", FS, "middle", INK, 400))
    return svg(W, H, "The balanced equation 2H2 + O2 makes 2H2O, drawn as atoms. On the left, two "
                     "hydrogen molecules and one oxygen molecule: 4 hydrogen atoms and 2 oxygen atoms. "
                     "On the right, two water molecules, each one oxygen atom joined to two hydrogen "
                     "atoms: also 4 hydrogen atoms and 2 oxygen atoms.", b)


# ------------------------------------------------------------------ mixtures
def mix_filtration():
    W, H = 720, 560
    b = []
    # filter paper (a cone inside the funnel), then the funnel
    b.append(poly([(214, 96), (426, 96), (320, 246)], "#FFFFFF", INK, 2.6))
    b.append(pathel("M196,86 L444,86 L336,246 L336,330 L304,330 L304,246 Z", INK, 3.5))
    # residue: sand caught in the paper
    for i, (x, y) in enumerate([(300, 214), (318, 222), (336, 214), (310, 200), (330, 200),
                                 (320, 186), (296, 196), (344, 198)]):
        b.append(circ(x, y, 7, SAND, INK, 2.6))
    # the beaker and the filtrate
    b.append(rect(234, 432, 172, 96, LIQ, LIQ, 2.6))
    b.append(pathel("M228,350 L228,530 L412,530 L412,350", INK, 3.5))
    b.append(circ(320, 372, 7, LIQ, INK, 2.6))
    # labels
    b.append(txt(470, 100, "filter paper", FS, "start"))
    b.append(leader(462, 92, 400, 110))
    b.append(lines(470, 196, ["residue", "(the sand)"], FS, "start", INK, 600, 34))
    b.append(leader(462, 190, 352, 206))
    b.append(txt(180, 300, "funnel", FS, "end"))
    b.append(leader(188, 292, 304, 292))
    b.append(lines(470, 456, ["filtrate", "(the water)"], FS, "start", INK, 600, 34))
    b.append(leader(462, 450, 400, 470))
    return svg(W, H, "Filtration. A funnel lined with a cone of filter paper sits in a beaker. The "
                     "sand is caught in the filter paper as the residue. The water runs through into "
                     "the beaker as the filtrate.", b)


def _flame(x, base, h=56):
    return pathel("M%s,%s C%s,%s %s,%s %s,%s C%s,%s %s,%s %s,%s Z" % (
        f(x), f(base - h), f(x + 24), f(base - h * 0.4), f(x + 20), f(base), f(x), f(base),
        f(x - 20), f(base), f(x - 24), f(base - h * 0.4), f(x), f(base - h)), INK, 2.6, "#F2A03D")


def _burner(x, base, h=40):
    """the barrel of a Bunsen burner under a flame whose base is at `base`."""
    return rect(x - 11, base, 22, h, "#C9C4B8", INK, 2.6)


def _basin(cx, top, fill):
    return pathel("M%s,%s Q%s,%s %s,%s Z" % (f(cx - 110), f(top), f(cx), f(top + 100), f(cx + 110), f(top)),
                  INK, 3, fill)


def mix_crystallisation():
    W, H = 720, 560
    b = []
    # 1: heating the solution in an evaporating basin
    cx = 180
    b.append(_basin(cx, 150, LIQ))
    b.append(line(cx - 120, 204, cx + 120, 204, INK, 4, "butt"))          # gauze
    b.append(line(cx - 80, 206, cx - 104, 330, INK, 4))                    # tripod legs
    b.append(line(cx + 80, 206, cx + 104, 330, INK, 4))
    b.append(_flame(cx, 296))
    b.append(_burner(cx, 296))
    b.append(lines(cx, 60, ["evaporating", "basin"], FS, "middle", INK, 600, 34))
    b.append(leader(cx + 52, 104, cx + 70, 156))
    b.append(txt(cx, 380, "heat gently", FS))
    b.append(lines(cx, 440, ["1  some water", "evaporates"], FS, "middle", INK, 400, 34))
    # 2: leave to cool: crystals form
    cx = 540
    b.append(_basin(cx, 150, LIQ))
    b.append(line(cx - 130, 200, cx + 130, 200, INK, 4, "butt"))          # the bench
    for (x, y) in [(500, 166), (530, 176), (562, 168), (588, 160), (515, 156), (548, 158)]:
        b.append(poly([(x, y - 9), (x + 9, y), (x, y + 9), (x - 9, y)], CRYSTAL, INK, 2.6))
    b.append(txt(cx, 84, "crystals", FS))
    b.append(leader(cx, 92, 548, 150))
    b.append(lines(cx, 440, ["2  leave to cool:", "crystals form"], FS, "middle", INK, 400, 34))
    return svg(W, H, "Crystallisation in two steps. First, a solution in an evaporating basin is "
                     "heated gently on a tripod and gauze over a flame, so some of the water "
                     "evaporates. Second, the basin is left on the bench to cool, and crystals form "
                     "in the solution.", b)


def _circle_path(cx, cy, r):
    k = 0.5523 * r
    return ("M%s,%s C%s,%s %s,%s %s,%s C%s,%s %s,%s %s,%s C%s,%s %s,%s %s,%s C%s,%s %s,%s %s,%s Z" % (
        f(cx), f(cy - r), f(cx + k), f(cy - r), f(cx + r), f(cy - k), f(cx + r), f(cy),
        f(cx + r), f(cy + k), f(cx + k), f(cy + r), f(cx), f(cy + r),
        f(cx - k), f(cy + r), f(cx - r), f(cy + k), f(cx - r), f(cy),
        f(cx - r), f(cy - k), f(cx - k), f(cy - r), f(cx), f(cy - r)))


def _distil(column):
    """A distillation rig. Returns (body, label anchors)."""
    b = []
    cx, cy, r = (250, 410, 66) if column else (210, 370, 70)
    neck_top = 126 if column else 222
    hw = 18 if column else 14
    # liquid in the flask: the part of the circle below a chord
    chord = cy + 18
    t1 = math.asin((chord - cy) / (r - 3))
    pts = [(cx + (r - 3) * math.cos(t), cy + (r - 3) * math.sin(t))
           for t in [t1 + (math.pi - 2 * t1) * i / 24.0 for i in range(25)]]
    b.append(poly(pts, LIQ, LIQ, 2.6))
    b.append(pathel(_circle_path(cx, cy, r), INK, 3.5))
    join = cy - math.sqrt(r * r - hw * hw)
    b.append(rect(cx - hw + 2, join - 4, 2 * hw - 4, 10, BG, BG, 2.6))        # opens the flask into the neck
    b.append(line(cx - hw, neck_top, cx - hw, join, INK, 3.5, "butt"))
    b.append(line(cx + hw, neck_top, cx + hw, join, INK, 3.5, "butt"))
    if column:
        for i in range(9):                                                     # glass beads in the column
            y = 170 + i * 15
            b.append(circ(cx - 7 if i % 2 else cx + 7, y, 6, GLASS, INK, 2.6))
    b.append(_flame(cx, cy + r + 62))
    b.append(_burner(cx, cy + r + 62, 34))
    # stopper, thermometer, bulb level with the side arm
    arm_y = neck_top + 26
    b.append(rect(cx - hw - 6, neck_top - 18, 2 * hw + 12, 20, "#C9C4B8", INK, 2.6))
    b.append(rect(cx - 5, neck_top - 96, 10, 96 + arm_y - neck_top - 8, GLASS, INK, 2.6))
    b.append(circ(cx, arm_y, 8, RUST, INK, 2.6))
    # side arm and condenser
    p1 = (cx + 76, arm_y + 34)
    p2 = (p1[0] + 260, p1[1] + 130)
    b.append(line(cx + hw, arm_y, p1[0], p1[1], INK, 3.5))
    L = math.hypot(p2[0] - p1[0], p2[1] - p1[1])
    u = ((p2[0] - p1[0]) / L, (p2[1] - p1[1]) / L)
    n = (-u[1], u[0])                                                          # points down and left

    def at(p, a, s):
        return (p[0] + u[0] * a + n[0] * s, p[1] + u[1] * a + n[1] * s)
    b.append(poly([at(p1, 0, 24), at(p2, 0, 24), at(p2, 0, -24), at(p1, 0, -24)], JACKET, INK, 3))
    b.append(line(p1[0], p1[1], p2[0] + u[0] * 26, p2[1] + u[1] * 26, INK, 3.5))
    w_in0, w_in1 = at(p2, -36, 24), at(p2, -36, 62)
    w_out0, w_out1 = at(p1, 36, -24), at(p1, 36, -62)
    b.append(line(w_in0[0], w_in0[1], w_in1[0], w_in1[1], INK, 6, "butt"))
    b.append(line(w_out0[0], w_out0[1], w_out1[0], w_out1[1], INK, 6, "butt"))
    # the receiving beaker and the distillate
    tip = (p2[0] + u[0] * 26, p2[1] + u[1] * 26)
    bx = tip[0] - 50
    b.append(rect(bx + 3, tip[1] + 92, 94, 40, LIQ, LIQ, 2.6))
    b.append(pathel("M%s,%s L%s,%s L%s,%s L%s,%s" % (f(bx), f(tip[1] + 40), f(bx), f(tip[1] + 134),
                                                    f(bx + 100), f(tip[1] + 134), f(bx + 100), f(tip[1] + 40)),
                    INK, 3.5))
    return b, dict(cx=cx, cy=cy, r=r, neck_top=neck_top, arm_y=arm_y, p1=p1, p2=p2, at=at,
                   w_in1=w_in1, w_out1=w_out1, tip=tip, bx=bx, hw=hw)


def mix_simple_distillation():
    W, H = 720, 680
    b, a = _distil(False)
    cx, cy, r = a["cx"], a["cy"], a["r"]
    b.append(txt(cx + 30, 92, "thermometer", FS, "start"))
    b.append(leader(cx + 24, 86, cx + 6, 140))
    c = a["at"](((a["p1"][0] + a["p2"][0]) / 2.0, (a["p1"][1] + a["p2"][1]) / 2.0), 0, -24)
    b.append(txt(c[0] + 40, c[1] - 52, "condenser", FS, "start"))
    b.append(leader(c[0] + 34, c[1] - 58 + 6, c[0] + 4, c[1] - 4))
    wo = a["w_out1"]
    b.append(txt(wo[0] + 20, wo[1] - 6, "water out", FS, "start"))
    wi = a["w_in1"]
    b.append(txt(wi[0] - 10, wi[1] + 34, "water in", FS, "end"))
    b.append(lines(cx - r - 14, cy - 10, ["salt", "water"], FS, "end", INK, 600, 34))
    b.append(leader(cx - r - 8, cy, cx - 30, cy + 34))
    b.append(txt(cx + 40, cy + r + 56, "heat", FS, "start"))
    tip = a["tip"]
    b.append(lines(tip[0], tip[1] + 172, ["pure water", "(distillate)"], FS, "middle", INK, 600, 34))
    return svg(W, H, "Simple distillation. Salt water is heated in a flask. A thermometer's bulb sits "
                     "level with the side arm. The steam passes into a sloping condenser, which has "
                     "cold water flowing in at the bottom and out at the top. The steam condenses and "
                     "drips into a beaker as pure water, the distillate. The salt stays in the flask.", b)


def mix_fractional_distillation():
    W, H = 720, 620
    b, a = _distil(True)
    cx, cy, r = a["cx"], a["cy"], a["r"]
    b.append(txt(cx + 24, 50, "thermometer", FS, "start"))
    b.append(leader(cx + 18, 44, cx + 6, 66))
    b.append(lines(cx - a["hw"] - 16, 200, ["fractionating", "column"], FS, "end", INK, 600, 34))
    b.append(leader(cx - a["hw"] - 10, 206, cx - a["hw"] - 1, 220))
    c = a["at"](((a["p1"][0] + a["p2"][0]) / 2.0, (a["p1"][1] + a["p2"][1]) / 2.0), 0, -24)
    b.append(txt(c[0] + 30, c[1] - 52, "condenser", FS, "start"))
    b.append(leader(c[0] + 24, c[1] - 52, c[0] + 4, c[1] - 4))
    b.append(lines(cx - r - 14, cy - 10, ["ethanol", "and water"], FS, "end", INK, 600, 34))
    b.append(leader(cx - r - 8, cy, cx - 30, cy + 34))
    b.append(txt(cx + 40, cy + r + 56, "heat", FS, "start"))
    tip = a["tip"]
    b.append(lines(tip[0] - 60, tip[1] + 172, ["ethanol", "collected first"], FS, "middle", INK, 600, 34))
    return svg(W, H, "Fractional distillation. A mixture of ethanol and water is heated in a flask. "
                     "Above the flask is a tall fractionating column packed with glass beads, with a "
                     "thermometer at the top level with the side arm. The vapour passes into a sloping "
                     "condenser and drips into a beaker. Ethanol, with the lower boiling point, is "
                     "collected first.", b)


# ------------------------------------------------------------------ model of the atom
def plum_pudding_nuclear():
    W, H = 720, 520
    b = []
    # plum pudding: a ball of positive charge with electrons embedded in it
    cx, cy, R = 180, 210, 130
    b.append(circ(cx, cy, R, POS, INK, 3))
    for (x, y) in [(-70, -60), (10, -90), (70, -40), (-20, -10), (-90, 30), (40, 40), (-40, 80), (80, 80)]:
        b.append(circ(cx + x, cy + y, 11, ELEC, ELEC, 1))
    for (x, y) in [(-30, -60), (40, -80), (-70, -15), (25, -20), (95, 10), (-55, 50), (0, 65), (55, 95)]:
        b.append(txt(cx + x, cy + y + 10, "+", FS, "middle", INK, 700))
    b.append(txt(cx, 50, "plum pudding", FS, "middle", INK, 700))
    b.append(lines(cx, 384, ["positive charge", "spread through", "the whole atom"], LS, "middle", INK, 400, 32))
    # nuclear model: a tiny charged nucleus, electrons around it, mostly empty space
    cx = 540
    b.append(circ(cx, cy, R, "none", GREY, 2.6).replace('stroke-width="2.6"', 'stroke-width="2.6" stroke-dasharray="10 10"'))
    b.append(circ(cx, cy, 9, NUC, INK, 2.6))
    for (x, y) in electron_points(cx, cy, 96, 8, -70):
        b.append(circ(x, y, 11, ELEC, ELEC, 1))
    b.append(txt(cx, 50, "nuclear model", FS, "middle", INK, 700))
    b.append(lines(cx, 384, ["tiny charged", "nucleus; mostly", "empty space"], LS, "middle", INK, 400, 32))
    b.append(circ(250, 496, 11, ELEC, ELEC, 1))
    b.append(txt(272, 506, "electron", LS, "start", INK, 400))
    return svg(W, H, "Two models of the atom side by side. Plum pudding: a ball of positive charge "
                     "with negative electrons embedded all through it. Nuclear model: a tiny charged "
                     "nucleus at the centre with electrons around it, and the rest of the atom empty "
                     "space.", b)


def alpha_scattering():
    W, H = 720, 660
    b = []
    fx0, fx1 = 330, 346
    b.append(rect(fx0, 70, fx1 - fx0, 360, GOLD, INK, 2.6))
    ys = [100, 150, 200, 250, 300, 350, 400]
    for y in ys:
        b.append(line(40, y, fx0, y, GREEN if y not in (100, 250, 400) else (AMBER if y != 250 else RUST), 4, "butt"))
    straight = [150, 200, 300, 350]
    for y in straight:
        b.append(arrow(fx1, y, 690, y, GREEN, 4, 20))
    b.append(arrow(fx1, 100, 660, 36, AMBER, 4, 20))                   # deflected up
    b.append(arrow(fx1, 400, 660, 466, AMBER, 4, 20))                  # deflected down
    b.append(arrow(fx0, 258, 70, 284, RUST, 4, 20))                    # comes back
    assert len(straight) > len(ys) - len(straight)                      # most go straight through
    b.append(txt(40, 52, "alpha particles", FS, "start"))
    b.append(lines(338, 470, ["thin", "gold foil"], FS, "middle", INK, 600, 34))
    rows = [(GREEN, "most go straight through"), (AMBER, "some are deflected"), (RUST, "a very few bounce back")]
    for i, (col, s) in enumerate(rows):
        y = 572 + i * 36
        b.append(line(40, y - 9, 100, y - 9, col, 6, "butt"))
        b.append(txt(116, y, s, LS, "start", INK, 400))
    return svg(W, H, "The alpha particle scattering experiment. Alpha particles are fired from the "
                     "left at a thin sheet of gold foil. Most go straight through. Some are deflected "
                     "through an angle. A very few bounce back towards where they came from.", b)


def bohr_atom():
    W, H = 720, 480
    Z, N = 3, 4
    shells = electrons_of(Z)
    assert shells == [2, 1]
    b = []
    cx, cy = 220, 220
    for i, rr in enumerate((90, 150)):
        b.append(circ(cx, cy, rr, "none", INK, 2.6))
        for (x, y) in electron_points(cx, cy, rr, shells[i], -90 if i == 0 else 0):
            b.append(circ(x, y, 9, ELEC, ELEC, 1))
    nuc = [(-12, -12, PROTON), (12, -12, NEUTRON), (-18, 10, NEUTRON), (6, 8, PROTON),
           (26, 10, NEUTRON), (-4, 28, PROTON), (18, 30, NEUTRON)]
    assert sum(1 for p in nuc if p[2] == PROTON) == Z and sum(1 for p in nuc if p[2] == NEUTRON) == N
    for (x, y, col) in nuc:
        b.append(circ(cx + x, cy + y, 12, col, INK, 2.6))
    b.append(lines(430, 110, ["protons and", "neutrons in", "the nucleus"], FS, "start", INK, 600, 34))
    b.append(leader(424, 130, cx + 38, cy + 6))
    b.append(lines(430, 330, ["electrons at", "specific", "distances"], FS, "start", INK, 600, 34))
    b.append(leader(424, 330, cx + 150 + 10, cy + 2))
    b.append(circ(60, 440, 12, PROTON, INK, 2.6))
    b.append(txt(82, 450, "proton", LS, "start", INK, 400))
    b.append(circ(250, 440, 12, NEUTRON, INK, 2.6))
    b.append(txt(272, 450, "neutron", LS, "start", INK, 400))
    b.append(txt(700, 450, "not to scale", LS, "end", GREY, 400))
    return svg(W, H, "A lithium atom in the model with protons and neutrons: a nucleus of 3 protons "
                     "and 4 neutrons, with 2 electrons on the inner shell and 1 on the outer shell, "
                     "each shell at a specific distance from the nucleus. Not to scale.", b)


# ------------------------------------------------------------------ group 7
HALOGEN_BP = [("F₂", -188), ("Cl₂", -34), ("Br₂", 59), ("I₂", 184)]


def halogen_boiling_points():
    W, H = 720, 520
    lo, hi = -200, 200
    y_hi, y_lo = 70, 410
    k = (y_lo - y_hi) / float(hi - lo)
    Y = lambda v: y_lo - (v - lo) * k
    x0, x1 = 130, 690
    b = []
    for v in (-200, -100, 0, 100, 200):
        if v:
            b.append(grid(x0, Y(v), x1, Y(v)))
        b.append(num(x0 - 12, Y(v) + 9, ("−%d" % -v) if v < 0 else str(v), "end"))
    b.append(line(x0, y_hi, x0, y_lo, INK, 3, "butt"))
    b.append(line(x0, Y(0), x1, Y(0), INK, 3, "butt"))
    b.append(vtxt(34, (y_hi + y_lo) / 2.0, "boiling point in °C"))
    xs = [220, 340, 460, 580]
    vals = [v for _, v in HALOGEN_BP]
    assert vals == sorted(vals)                                   # rises down the group
    for x, (name, v) in zip(xs, HALOGEN_BP):
        top, bot = min(Y(0), Y(v)), max(Y(0), Y(v))
        assert bot - top > 0
        b.append(rect(x - 34, top, 68, bot - top, "#A9C7E8" if v < 0 else "#F2C9AE", INK, 2.6))
        lab = ("−%d" % -v) if v < 0 else str(v)
        b.append(num(x, (bot + 32) if v < 0 else (top - 12), lab))
        b.append(txt(x, 490, name, FS, "middle", INK, 700))
    return svg(W, H, "A bar chart of the boiling points of the halogens. Fluorine minus 188 °C, "
                     "chlorine minus 34 °C, bromine 59 °C, iodine 184 °C. The boiling point rises "
                     "going down the group.", b)


def halogen_pull():
    W, H = 720, 480
    b = []
    sf, sc = electrons_of(9), electrons_of(17)
    assert sf == [2, 7] and sc == [2, 8, 7]
    fb, fr = shell_atom(170, 220, "F", sf, r0=52, step=40)
    cb, cr = shell_atom(520, 220, "Cl", sc, r0=48, step=36)
    b += fb + cb
    # an incoming electron for each, drawn the same distance outside its outer shell
    for (cx, R) in ((170, fr), (520, cr)):
        ex = cx + R + 58
        b.append(circ(ex, 220, 8, ELEC, ELEC, 1))
        b.append(arrow(ex - 12, 220, cx + R + 10, 220, RUST, 4, 18))
    b.append(txt(170, 70, "fluorine 2,7", FS, "middle", INK, 700))
    b.append(txt(520, 52, "chlorine 2,8,7", FS, "middle", INK, 700))
    b.append(lines(170, 400, ["outer shell close:", "stronger pull"], LS, "middle", INK, 400, 32))
    b.append(lines(520, 400, ["outer shell further", "away: weaker pull"], LS, "middle", INK, 400, 32))
    return svg(W, H, "Shell diagrams of fluorine, 2,7, and chlorine, 2,8,7, each with one electron "
                     "arriving from outside. Fluorine's outer shell is close to its nucleus, so the "
                     "pull on the incoming electron is stronger. Chlorine's outer shell is further "
                     "away, so the pull is weaker.", b)


_REGISTRY_A = {
    "aec-particle-boxes": aec_particle_boxes,
    "aec-balance-water": aec_balance_water,
    "mix-filtration": mix_filtration,
    "mix-crystallisation": mix_crystallisation,
    "mix-simple-distillation": mix_simple_distillation,
    "mix-fractional-distillation": mix_fractional_distillation,
    "plum-pudding-nuclear": plum_pudding_nuclear,
    "alpha-scattering": alpha_scattering,
    "bohr-atom": bohr_atom,
    "halogen-boiling-points": halogen_boiling_points,
    "halogen-pull": halogen_pull,
}


# ==================================================================
# Part B: subatomic-particles, relative-atomic-mass, electronic-structure, transition-metals
# ==================================================================

P_FILL = RUST          # a proton: dark, never under text
N_FILL = "#D9D4C7"     # a neutron: light grey


def _nucleus(cx, cy, protons, neutrons, r=13):
    """A small cluster of protons and neutrons, alternating, packed round (cx, cy)."""
    kinds = []
    p, n = protons, neutrons
    while p or n:
        if p:
            kinds.append("p"); p -= 1
        if n:
            kinds.append("n"); n -= 1
    pts = [(cx, cy)]
    ring = 1
    while len(pts) < len(kinds):
        k = 6 * ring
        pts += electron_points(cx, cy, 2 * r * ring * 0.92, k, start=-90 + 30 * (ring % 2))
        ring += 1
    b = []
    where = {"p": [], "n": []}
    for kind, (x, y) in zip(kinds, pts):
        b.append(circ(x, y, r, P_FILL if kind == "p" else N_FILL, INK, 2.6))
        where[kind].append((x, y))
    return b, where


# ------------------------------------------------------------------ subatomic-particles
LI_Z, LI_A = 3, 7


def atom_particles():
    W, H = 720, 460
    cx, cy = 200, 220
    n = LI_A - LI_Z
    assert n == 4 and electrons_of(LI_Z) == [2, 1]
    b = []
    r0, step = 82, 52
    for i, k in enumerate(electrons_of(LI_Z)):
        r = r0 + i * step
        b.append(circ(cx, cy, r, "none", INK, 2.6))
        for (x, y) in electron_points(cx, cy, r, k, start=0 if i == 1 else -90):
            b.append(circ(x, y, 8, ELEC, ELEC, 1))
    nb, where = _nucleus(cx, cy, LI_Z, n)
    b += nb
    assert len(where["p"]) == 3 and len(where["n"]) == 4
    LX = 400
    # the cluster: centre proton, then a ring from -60 degrees: n, p, n, p, n, n
    b.append(txt(LX, cy - 132, "nucleus", FS, "start"))
    b.append(leader(LX - 8, cy - 140, cx + 14, cy - 36))
    b.append(txt(LX, cy - 40, "proton", FS, "start"))
    b.append(leader(LX - 8, cy - 48, cx + 37, cy))
    b.append(txt(LX, cy + 70, "neutron", FS, "start"))
    b.append(leader(LX - 8, cy + 62, cx + 24, cy + 30))
    ex, ey = cx + r0 + step, cy
    b.append(txt(LX, cy + 160, "electron", FS, "start"))
    b.append(leader(LX - 8, cy + 152, ex + 6, ey + 8))
    b.append(txt(360, 428, "lithium-7: 3 protons, 4 neutrons, 3 electrons", LS))
    return svg(W, H, "A lithium atom, not to scale. The nucleus at the centre holds 3 protons and 4 "
                     "neutrons. 3 electrons move around it: 2 on the inner shell and 1 on the outer shell.", b)


NA_Z, NA_A = 11, 23


def nuclear_symbol():
    W, H = 720, 420
    n = NA_A - NA_Z
    assert n == 12
    b = []
    # the symbol: mass number top left, atomic number bottom left
    b.append(txt(150, 220, "Na", 96, "start"))
    b.append(txt(140, 152, str(NA_A), 40, "end"))
    b.append(txt(140, 222, str(NA_Z), 40, "end"))
    RX = 340
    b.append(lines(RX, 92, ["mass number:", "protons + neutrons"], LS, "start", INK, 600, 34))
    b.append(leader(RX - 8, 100, 146, 140))
    b.append(lines(RX, 252, ["atomic number:", "number of protons"], LS, "start", INK, 600, 34))
    b.append(leader(RX - 8, 246, 124, 238))
    b.append(lines(360, 342, ["%d protons, %d electrons" % (NA_Z, NA_Z),
                              "%d − %d = %d neutrons" % (NA_A, NA_Z, n)], LS, "middle", INK, 600, 36))
    return svg(W, H, "The nuclear symbol for sodium-23: Na with the mass number 23 at the top left "
                     "and the atomic number 11 at the bottom left. The mass number is protons plus "
                     "neutrons; the atomic number is the number of protons. Sodium-23 has 11 protons, "
                     "11 electrons and 23 minus 11, which is 12, neutrons.", b)


def isotopes_hydrogen():
    W, H = 720, 400
    b = []
    for i, nn in enumerate((0, 1, 2)):
        cx, cy = 120 + i * 240, 150
        nb, where = _nucleus(cx, cy, 1, nn, r=12)
        b.append(circ(cx, cy, 74, "none", INK, 2.6))
        b.append(circ(cx + 74, cy, 8, ELEC, ELEC, 1))
        b += nb
        a = 1 + nn
        assert len(where["p"]) == 1 and len(where["n"]) == nn
        b.append(lines(cx, 278, ["hydrogen-%d" % a, "1 proton",
                                 "%d neutron%s" % (nn, "" if nn == 1 else "s")], LS, "middle", INK, 600, 34))
    return svg(W, H, "Three isotopes of hydrogen, each with 1 proton and 1 electron. Hydrogen-1 has no "
                     "neutrons, hydrogen-2 has 1 neutron and hydrogen-3 has 2 neutrons.", b)


ATOM_R_M, NUC_R_M = 1e-10, 1e-14


def atom_scale():
    W, H = 720, 460
    assert abs(ATOM_R_M / NUC_R_M - 10000) < 1e-6
    cx, cy, R = 180, 200, 150
    b = []
    b.append(circ(cx, cy, R, "#F3F0E7", INK, 2.6))
    b.append(circ(cx, cy, 5, RUST, RUST, 1))
    for (x, y) in electron_points(cx, cy, R * 0.72, 3, start=-60):
        b.append(circ(x, y, 7, ELEC, ELEC, 1))
    b.append(line(cx, cy, cx, cy + R, INK, 3, "butt"))
    RX = 370
    b.append(lines(RX, 80, ["atom radius about", "1 × 10⁻¹⁰ m (0.1 nm)"], LS, "start", INK, 600, 34))
    b.append(leader(RX - 8, 92, cx + R * 0.74, cy - R * 0.67))
    b.append(lines(RX, 232, ["nucleus radius about", "1 × 10⁻¹⁴ m"], LS, "start", INK, 600, 34))
    b.append(leader(RX - 8, 226, cx + 8, cy - 2))
    b.append(lines(360, 400,["not to scale: the real nucleus", "would be too small to see"], LS, "middle", INK, 600, 34))
    return svg(W, H, "An atom drawn as a circle with a radius of about 1 times 10 to the minus 10 metres, "
                     "0.1 nanometres, with a tiny nucleus at the centre of radius about 1 times 10 to the "
                     "minus 14 metres, and electrons in the space around it. Not to scale: the real "
                     "nucleus would be far too small to see.", b)


# ------------------------------------------------------------------ relative-atomic-mass
CL35, CL37 = "#DCE6F2", "#F6E2C8"


def chlorine_abundance():
    W, H = 720, 360
    atoms = [35, 35, 35, 37]
    assert atoms.count(35) * 100 // len(atoms) == 75 and atoms.count(37) * 100 // len(atoms) == 25
    mean = sum(atoms) / float(len(atoms))
    assert abs(mean - 35.5) < 1e-9
    assert abs((75 * 35 + 25 * 37) / 100.0 - 35.5) < 1e-9
    b = []
    for i, a in enumerate(atoms):
        x = 135 + i * 150
        b.append(circ(x, 120, 56, CL35 if a == 35 else CL37, INK, 2.6))
        b.append(txt(x, 130, "Cl-%d" % a, LS))
    b.append(lines(360, 236, ["3 in every 4 atoms are chlorine-35 (75%)",
                              "1 in every 4 is chlorine-37 (25%)",
                              "average mass 35.5"], LS, "middle", INK, 600, 38))
    return svg(W, H, "Four chlorine atoms: three are chlorine-35 and one is chlorine-37. So 75% of "
                     "chlorine atoms are chlorine-35 and 25% are chlorine-37, and the average mass is 35.5.", b)


# ------------------------------------------------------------------ electronic-structure
def sodium_shells():
    W, H = 720, 470
    sh = electrons_of(11)
    assert sh == [2, 8, 1]
    cx, cy = 220, 220
    b, R = shell_atom(cx, cy, "Na", sh, r0=62, step=52)
    RX = 460
    import math as _m
    for i, (k, y, ang) in enumerate(zip(sh, (96, 196, 316), (-45.0, -22.5, 45.0))):
        r = 62 + i * 52
        b.append(lines(RX, y, ["shell %d: %d" % (i + 1, k)], LS, "start"))
        b.append(leader(RX - 8, y - 8, cx + r * _m.cos(_m.radians(ang)), cy + r * _m.sin(_m.radians(ang))))
    b.append(txt(360, 438, "sodium 2,8,1", FS))
    return svg(W, H, "A diagram of a sodium atom: the nucleus, then a first shell with 2 electrons, a "
                     "second shell with 8 electrons and a third shell with 1 electron. In numbers, 2,8,1.", b)


def shell_examples():
    W, H = 720, 340
    b = []
    for i, (z, sym, name) in enumerate(((3, "Li", "lithium"), (8, "O", "oxygen"), (17, "Cl", "chlorine"))):
        sh = electrons_of(z)
        cx = 120 + i * 240
        body, R = shell_atom(cx, 140, sym, sh, r0=40, step=28, er=6, sym_size=27, nuc_r=24)
        assert R <= 100
        b += body
        b.append(lines(cx, 280, [name, ",".join(str(k) for k in sh)], LS, "middle", INK, 600, 34))
    assert electrons_of(3) == [2, 1] and electrons_of(8) == [2, 6] and electrons_of(17) == [2, 8, 7]
    return svg(W, H, "Electron shell diagrams: lithium 2,1 with 2 electrons on the first shell and 1 on "
                     "the second; oxygen 2,6; chlorine 2,8,7.", b)


# ------------------------------------------------------------------ transition-metals
STRIP = ["Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn"]
SPEC_SIX = ["Cr", "Mn", "Fe", "Co", "Ni", "Cu"]


def transition_block():
    W, H = 720, 560
    cw, ch = 38, 30
    x0, y0 = (W - 18 * cw) / 2.0, 96

    def fill(p, c):
        if 3 <= c <= 12:
            return TRANS
        if c == 1 and p >= 2:
            return METAL
        return "#FFFFFF"
    b = pt_outline(x0, y0, cw, ch, fill)
    # labels above, with leaders down to the columns
    g1x = x0 + cw / 2.0
    b.append(txt(x0, 46, "Group 1", LS, "start"))
    b.append(leader(g1x, 54, g1x, y0 + ch + 8))
    tx = x0 + 7.5 * cw
    b.append(txt(tx + 40, 46, "transition metals", LS, "middle"))
    b.append(leader(tx, 54, tx, y0 + 3 * ch + 8))
    # period 4 row of the block, opened out below
    sx0, sw, sy, sh_ = 30, 66, 370, 64
    assert len(STRIP) * sw + 2 * sx0 == W
    bx0, bx1, by = x0 + 2 * cw, x0 + 12 * cw, y0 + 4 * ch
    b.append(line(bx0, by, sx0, sy, GREY, 2.6))
    b.append(line(bx1, by, sx0 + len(STRIP) * sw, sy, GREY, 2.6))
    b.append(rect(bx0, y0 + 3 * ch, bx1 - bx0, ch, "none", INK, 4))
    for i, s in enumerate(STRIP):
        x = sx0 + i * sw
        b.append(rect(x, sy, sw, sh_, HILITE if s in SPEC_SIX else TRANS, INK, 2.6))
        b.append(txt(x + sw / 2.0, sy + 42, s, LS))
    assert [s for s in STRIP if s in SPEC_SIX] == SPEC_SIX
    b.append(lines(360, 476, ["period 4: Cr, Mn, Fe, Co, Ni and Cu", "are the examples to learn"],
                   LS, "middle", INK, 600, 36))
    return svg(W, H, "The outline of the periodic table. Group 1 is the first column. The transition "
                     "metals are the wide central block between Group 2 and Group 3. Period 4 of that block "
                     "is shown larger: scandium, titanium, vanadium, chromium, manganese, iron, cobalt, "
                     "nickel, copper and zinc, with chromium, manganese, iron, cobalt, nickel and copper "
                     "marked as the examples to learn.", b)


COLOURS = [("Cu²⁺", "#3A78D6", "blue"), ("Fe²⁺", "#9CC79A", "green"),
           ("Fe³⁺", "#C8742A", "orange-brown"), ("Ni²⁺", "#5AA86A", "green"),
           ("Co²⁺", "#E58BB4", "pink"), ("MnO₄⁻", "#7A2C8E", "purple"),
           ("Cr₂O₇²⁻", "#E8923A", "orange"), ("Na⁺", "#FFFFFF", "colourless")]


def transition_colours():
    W, H = 720, 620
    b = []
    for i, (ion, col, word) in enumerate(COLOURS):
        r, c = divmod(i, 4)
        cx = 90 + c * 180
        top = 30 + r * 300
        b.append(rect(cx - 30, top, 60, 140, col, INK, 2.6, 26))
        b.append(lines(cx, top + 190, [ion, word], LS, "middle", INK, 600, 36))
    return svg(W, H, "Solutions of compounds drawn as coloured tubes: copper(II), Cu2+, blue; iron(II), "
                     "Fe2+, green; iron(III), Fe3+, orange-brown; nickel(II), Ni2+, green; cobalt(II), "
                     "Co2+, pink; manganate(VII), MnO4 minus, purple; dichromate, Cr2O7 2 minus, orange; "
                     "and, for comparison, a Group 1 compound, Na+, colourless.", b)


_REGISTRY_B = {
    "atom-particles": atom_particles,
    "nuclear-symbol": nuclear_symbol,
    "isotopes-hydrogen": isotopes_hydrogen,
    "atom-scale": atom_scale,
    "chlorine-abundance": chlorine_abundance,
    "sodium-shells": sodium_shells,
    "shell-examples": shell_examples,
    "transition-block": transition_block,
    "transition-colours": transition_colours,
}


# ==================================================================
# Part C: periodic-table, development-periodic-table, metals-non-metals, group-0, group-1
# ==================================================================

ROWTINT = "#E3EEDC"


# ------------------------------------------------------------------ periodic-table: first twenty
def _place(z):
    sh = electrons_of(z)
    outer = sh[-1]
    full = (len(sh) == 1 and outer == 2) or outer == 8
    return len(sh), (0 if full else outer)


def pt_first_twenty():
    W, H = 720, 470
    cw, ch = 72, 70
    x0, y0 = 128, 70                      # left edge of the Group 1 column, top of period 1
    cols = [1, 2, 3, 4, 5, 6, 7, 0]
    b = []
    for i, g in enumerate(cols):
        b.append(num(x0 + i * cw + cw / 2.0, y0 - 18, str(g)))
    b.append(txt(x0 - 52, y0 - 18, "Group", LS, "middle"))
    for p in (1, 2, 3, 4):
        b.append(num(x0 - 26, y0 + (p - 1) * ch + ch / 2.0 + 10, str(p)))
    seen = {}
    for z in range(1, 21):
        p, g = _place(z)
        sym = SYMBOLS[z - 1]
        if z == 1:
            x = x0 + 3.5 * cw                 # hydrogen sits on its own
        else:
            x = x0 + cols.index(g) * cw
        y = y0 + (p - 1) * ch
        fill = "#FFFFFF"
        if g == 1 and z != 1:
            fill = HILITE
        elif p == 3:
            fill = ROWTINT
        b.append(rect(x, y, cw, ch, fill, INK, 2.6))
        b.append(txt(x + cw / 2.0, y + ch / 2.0 + 10, sym, 28))
        seen[sym] = (p, g)
    assert seen["Na"] == (3, 1) and seen["Cl"] == (3, 7) and seen["Ar"] == (3, 0)
    assert seen["He"] == (1, 0) and seen["K"] == (4, 1) and seen["Ca"] == (4, 2)
    assert seen["Li"] == (2, 1) and seen["F"] == (2, 7)
    yb = y0 + 4 * ch + 34
    b.append(rect(x0, yb, 34, 30, HILITE, INK, 2.6))
    b.append(txt(x0 + 46, yb + 25, "a group (column): Group 1", LS, "start"))
    b.append(rect(x0, yb + 46, 34, 30, ROWTINT, INK, 2.6))
    b.append(txt(x0 + 46, yb + 71, "a period (row): Period 3", LS, "start"))
    return svg(W, H, "The first twenty elements in the periodic table. Groups 1 to 7 and 0 run across "
                     "the top and periods 1 to 4 down the side. Hydrogen sits on its own at the top. "
                     "The Group 1 column, lithium, sodium and potassium, is shaded, and so is the "
                     "Period 3 row, from sodium to argon.", b)


# ------------------------------------------------------------------ periodic-table: Na and Cl
def na_cl_shells():
    W, H = 720, 480
    na, cl = electrons_of(11), electrons_of(17)
    assert na == [2, 8, 1] and cl == [2, 8, 7]
    b = []
    for cx, sym, sh, row2 in ((180, "Na", na, ("1 outer electron:", "Group 1")),
                              (540, "Cl", cl, ("7 outer electrons:", "Group 7"))):
        body, R = shell_atom(cx, 150, sym, sh, r0=44, step=28, er=6.5, sym_size=27, nuc_r=27)
        b += body
        b.append(txt(cx, 150 + R + 50, "%s %s" % (sym, ",".join(str(n) for n in sh)), 28))
        b.append(txt(cx, 150 + R + 92, "3 shells: Period 3", LS))
        b.append(lines(cx, 150 + R + 130, list(row2), LS, "middle", INK, 600, 36))
    return svg(W, H, "Shell diagrams of sodium and chlorine. Sodium, 2,8,1, has three shells, so it "
                     "is in Period 3, and one outer electron, so it is in Group 1. Chlorine, 2,8,7, "
                     "has three shells, so Period 3, and seven outer electrons, so Group 7.", b)


# ------------------------------------------------------------------ metals and non-metals
def _nonmetal(p, c):
    if p == 1:
        return True                       # hydrogen and helium
    return c >= 11 + p                   # the staircase: B..Ne, Si..Ar, As..Kr, Te..Xe, At, Rn, period 7 col 18


def pt_metals_nonmetals():
    W, H = 720, 470
    cw, ch = 36, 40
    x0, y0 = 36, 60
    b = pt_outline(x0, y0, cw, ch, lambda p, c: NONMETAL if _nonmetal(p, c) else METAL)
    nm = [pc for pc in pt_cells() if _nonmetal(*pc)]
    met = [pc for pc in pt_cells() if not _nonmetal(*pc)]
    # the staircase lies right of B, Si, As, Te, At; metals are the majority
    assert (2, 13) in nm and (3, 14) in nm and (4, 15) in nm and (5, 16) in nm and (6, 17) in nm
    assert (3, 13) in met and (4, 14) in met and (5, 15) in met and (6, 16) in met
    assert len(met) > len(nm)
    # group numbers over the main groups
    for c, g in ((1, "1"), (2, "2"), (13, "3"), (14, "4"), (15, "5"), (16, "6"), (17, "7"), (18, "0")):
        b.append(num(x0 + (c - 0.5) * cw, y0 - 14, g))
    # the staircase line
    pts = [(x0 + 12 * cw, y0 + 1 * ch)]
    for p in range(2, 8):
        xl = x0 + (10 + p) * cw
        pts += [(xl, y0 + (p - 1) * ch), (xl, y0 + p * ch)]
    b.append(poly_line(pts[1:], RUST, 6))
    # one symbol only: a 2-letter symbol at 27 is wider than a 36-unit cell
    for (p, c), s in (((1, 1), "H"),):
        b.append(txt(x0 + (c - 0.5) * cw, y0 + (p - 0.5) * ch + 10, s, LS))
    yb = y0 + 7 * ch + 30
    b.append(rect(x0, yb, 40, 30, METAL, INK, 2.6))
    b.append(txt(x0 + 52, yb + 25, "metals: left and bottom", LS, "start"))
    b.append(rect(x0, yb + 44, 40, 30, NONMETAL, INK, 2.6))
    b.append(txt(x0 + 52, yb + 69, "non-metals: right and top", LS, "start"))
    return svg(W, H, "Outline of the periodic table. Metals, the majority, fill the left, the middle "
                     "and the bottom. Non-metals are towards the right and top, beyond a staircase "
                     "line, with hydrogen, a non-metal, at the top left.", b)


# ------------------------------------------------------------------ development: Te and I
TE = ("Te", 52, 127.6)
IOD = ("I", 53, 126.9)


def te_i_swap():
    W, H = 720, 500
    assert TE[1] < IOD[1] and TE[2] > IOD[2]
    cw, ch = 120, 70
    xa, xb, y0 = 150, 450, 90
    b = []
    b.append(txt(xa + cw / 2.0, y0 - 24, "Group 6", LS))
    b.append(txt(xb + cw / 2.0, y0 - 24, "Group 7", LS))
    for i, (s1, s2) in enumerate((("S", "Cl"), ("Se", "Br"))):
        for x, s in ((xa, s1), (xb, s2)):
            b.append(rect(x, y0 + i * ch, cw, ch, "#FFFFFF", INK, 2.6))
            b.append(txt(x + cw / 2.0, y0 + i * ch + 46, s, 30))
    yt = y0 + 2 * ch
    for x, (s, _p, _a) in ((xa, TE), (xb, IOD)):
        b.append(rect(x, yt, cw, ch, HILITE, INK, 3.5))
        b.append(txt(x + cw / 2.0, yt + 46, s, 30))
    b.append(arrow(xa + cw + 14, yt + ch / 2.0, xb - 14, yt + ch / 2.0, INK, 4, 18))
    b.append(arrow(xb - 14, yt + ch / 2.0 + 0.01, xa + cw + 14, yt + ch / 2.0 + 0.01, INK, 4, 18))
    y = yt + ch + 50
    b.append(lines(60, y, ["Te: 52 protons,", "relative atomic mass %.1f" % TE[2]], LS, "start", INK, 600, 36))
    b.append(lines(60, y + 92, ["I: 53 protons,", "relative atomic mass %.1f" % IOD[2]], LS, "start", INK, 600, 36))
    return svg(W, H, "Part of Mendeleev's table. Tellurium sits below sulfur and selenium in Group 6, "
                     "and iodine below chlorine and bromine in Group 7. Tellurium has 52 protons and a "
                     "relative atomic mass of 127.6; iodine has 53 protons and 126.9. By atomic weight "
                     "iodine would come first, so Mendeleev swapped the pair.", b)


# ------------------------------------------------------------------ development: the gap
def mendeleev_gap():
    W, H = 720, 460
    cw, ch = 130, 76
    xa, xb, y0 = 110, 480, 80
    b = []
    b.append(txt(xa + cw / 2.0, y0 - 26, "Mendeleev", LS))
    b.append(txt(xb + cw / 2.0, y0 - 26, "later", LS))
    for x in (xa, xb):
        for i, s in enumerate(("C", "Si")):
            b.append(rect(x, y0 + i * ch, cw, ch, "#FFFFFF", INK, 2.6))
            b.append(txt(x + cw / 2.0, y0 + i * ch + 50, s, 30))
    yg = y0 + 2 * ch
    b.append(rect(xa, yg, cw, ch, "none", INK, 3, 0).replace("/>", ' stroke-dasharray="10 8"/>'))
    b.append(txt(xa + cw / 2.0, yg + 50, "?", 34))
    b.append(rect(xb, yg, cw, ch, HILITE, INK, 3.5))
    b.append(txt(xb + cw / 2.0, yg + 50, "Ge", 30))
    b.append(arrow(xa + cw + 20, yg + ch / 2.0, xb - 20, yg + ch / 2.0, INK, 5, 22))
    y = yg + ch + 56
    b.append(lines(xa + cw / 2.0, y, ["a gap for an", "undiscovered", "element"], LS, "middle", INK, 600, 36))
    b.append(lines(xb + cw / 2.0, y, ["germanium fills", "the gap"], LS, "middle", INK, 600, 36))
    return svg(W, H, "Mendeleev's table had carbon, silicon and then a gap left for an element not "
                     "yet discovered. Later, germanium was discovered and filled the gap below silicon.", b)


# ------------------------------------------------------------------ Group 0: full outer shells
def noble_gas_shells():
    W, H = 720, 370
    he, ne, ar = electrons_of(2), electrons_of(10), electrons_of(18)
    assert he == [2] and ne == [2, 8] and ar == [2, 8, 8]
    b = []
    for cx, s, sh in ((100, "He", he), (290, "Ne", ne), (530, "Ar", ar)):
        body, R = shell_atom(cx, 150, s, sh, r0=40, step=28, er=6.5, sym_size=27, nuc_r=26)
        b += body
        b.append(txt(cx, 330, "%s %s" % (s, ",".join(str(n) for n in sh)), 28))
    return svg(W, H, "Shell diagrams of helium, neon and argon. Helium has 2 electrons, a full first "
                     "shell. Neon is 2,8 and argon is 2,8,8: each has a full outer shell of 8.", b)


# ------------------------------------------------------------------ Group 0: boiling points
NG = [("He", -269), ("Ne", -246), ("Ar", -186), ("Kr", -153), ("Xe", -108), ("Rn", -62)]


def noble_gas_boiling():
    W, H = 720, 540
    assert all(NG[i][1] < NG[i + 1][1] for i in range(len(NG) - 1))
    x0, x1, y0, y1 = 150, 690, 60, 400
    lo, hi = -300, -50
    Y = lambda t: y1 - (y1 - y0) * (t - lo) / float(hi - lo)
    b = []
    for t in (-300, -250, -200, -150, -100, -50):
        b.append(grid(x0, Y(t), x1, Y(t)))
        b.append(num(x0 - 12, Y(t) + 9, "−%d" % (-t), "end"))
    b.append(line(x0, y0, x0, y1, INK, 3, "butt"))
    b.append(line(x0, y1, x1, y1, INK, 3, "butt"))
    b.append(vtxt(34, (y0 + y1) / 2.0, "boiling point in °C"))
    step = (x1 - x0) / float(len(NG))
    pts = []
    for i, (s, t) in enumerate(NG):
        x = x0 + step * (i + 0.5)
        pts.append((x, Y(t)))
        b.append(txt(x, y1 + 40, s, LS))
    b.append(poly_line(pts, BLUE, 4))
    for x, y in pts:
        b.append(circ(x, y, 9, BLUE, BLUE, 1))
    b.append(arrow(x0 + 40, y1 + 84, x1 - 20, y1 + 84, INK, 4, 18))
    b.append(txt((x0 + x1) / 2.0, y1 + 120, "down the group", LS))
    return svg(W, H, "Line graph of the boiling points of the noble gases going down Group 0: helium "
                     "minus 269, neon minus 246, argon minus 186, krypton minus 153, xenon minus 108 "
                     "and radon minus 62 degrees Celsius. The boiling point rises down the group.", b)


# ------------------------------------------------------------------ Group 1: outer electron further out
def alkali_shells():
    W, H = 720, 460
    li, na, k = electrons_of(3), electrons_of(11), electrons_of(19)
    assert li == [2, 1] and na == [2, 8, 1] and k == [2, 8, 8, 1]
    b = []
    r0, step = 34, 22
    radii = []
    for cx, s, sh in ((95, "Li", li), (285, "Na", na), (545, "K", k)):
        body, R = shell_atom(cx, 190, s, sh, r0=r0, step=step, er=6, sym_size=27, nuc_r=22)
        b += body
        ox, oy = electron_points(cx, 190, R, 1)[0]
        b.append(circ(ox, oy, 10, RUST, INK, 2.6))
        radii.append(R)
        b.append(txt(cx, 340, "%s %s" % (s, ",".join(str(n) for n in sh)), 28))
    assert radii[0] < radii[1] < radii[2]
    b.append(arrow(60, 392, 680, 392, INK, 4, 18))
    b.append(txt(360, 432, "outer electron further from the nucleus", LS))
    return svg(W, H, "Shell diagrams of lithium 2,1, sodium 2,8,1 and potassium 2,8,8,1. Each has one "
                     "outer electron, marked. Going down the group the atom has more shells, so the "
                     "outer electron is further from the nucleus.", b)


_REGISTRY_C = {
    "pt-first-twenty": pt_first_twenty,
    "na-cl-shells": na_cl_shells,
    "pt-metals-nonmetals": pt_metals_nonmetals,
    "te-i-swap": te_i_swap,
    "mendeleev-gap": mendeleev_gap,
    "noble-gas-shells": noble_gas_shells,
    "noble-gas-boiling": noble_gas_boiling,
    "alkali-shells": alkali_shells,
}


REGISTRY = {}
for _part in (_REGISTRY_A, _REGISTRY_B, _REGISTRY_C):
    for _k, _v in _part.items():
        if _k in REGISTRY:
            raise ValueError("figlib.ks4lean_atoms: figure name %r is drawn twice" % _k)
        REGISTRY[_k] = _v
