# -*- coding: utf-8 -*-
"""figlib.ks4lean_pm: lean Particle model of matter lesson figures (3), drafted 24 Nov 2026.
Pure standard library. REGISTRY: name -> no-arg fn returning SVG.

Drawn in figlib/ks4lean_eco.py's conventions and with its helpers (one 720 viewBox, Georgia 28,
own #FFFDF8 background rect, path commands M L H V C Q Z only, no text on a dark fill, labels
>= 27 at a 720 viewBox). Every plotted number is the record's own and is asserted:
  particle-states       solid, liquid and gas, the simple GCSE particle diagram (AQA 8463 4.3.1.1 /
                        8464 6.3.1.1: "recognise/draw simple diagrams to model the difference
                        between solids, liquids and gases"); density_of_materials.py, card
                        "Density and the particle model"; changes_of_state.py, card "States of matter"
  displacement-volume   a measuring cylinder before and after a stone is lowered in: 50 cm³ to
                        62 cm³, so the stone's volume is 12 cm³ (density_of_materials.py, card
                        "Required practical: an irregular solid")
  state-changes         the five changes of state AQA names (melt, freeze, boil or evaporate,
                        condense, sublimate) between the three states (changes_of_state.py,
                        card "The changes of state")
"""
from .ks4lean_eco import (INK, RUST, BLUE, BG, FS, f, svg, line, txt, lines, circ, rect, pathel,
                          leader, arrow)

PART = "#E9B44C"     # particle fill: a light amber with ink outline (labels never sit on it)
WATER = "#CFE3EE"


def _no_overlap(pts, r):
    for i, (x1, y1) in enumerate(pts):
        for (x2, y2) in pts[i + 1:]:
            assert (x1 - x2) ** 2 + (y1 - y2) ** 2 >= (2 * r - 0.5) ** 2, ((x1, y1), (x2, y2))


# ------------------------------------------------------------------ 1  solid, liquid, gas
def particle_states():
    W, H = 720, 330
    r = 15
    bw, top, bh = 210, 30, 210
    xs = [20, 255, 490]
    assert xs[-1] + bw <= W - 20
    b = []
    # solid: a regular arrangement, every particle touching its neighbours
    sx, sy = xs[0] + 15, top + 15
    solid = [(sx + r + c * 2 * r, sy + r + k * 2 * r) for k in range(6) for c in range(6)]
    # liquid: still touching, but no regular pattern; it sits in the bottom of its container
    lx, ly = xs[1], top
    liquid = [(lx + x, ly + y) for x, y in [
        (22, 194), (52, 192), (83, 195), (114, 193), (145, 195), (176, 193),
        (34, 165), (66, 163), (98, 166), (129, 164), (161, 166), (192, 160),
        (20, 137), (50, 135), (81, 136), (113, 135), (144, 137), (176, 133),
        (36, 107), (68, 106), (99, 107), (131, 106), (162, 106), (192, 104),
        (55, 77), (100, 77), (140, 77), (175, 75)]]
    # gas: far apart, filling the whole container
    gx, gy = xs[2], top
    gas = [(gx + x, gy + y) for x, y in [(40, 40), (150, 30), (100, 95), (180, 120),
                                         (35, 150), (120, 180), (180, 190), (60, 92)]]
    for pts in (solid, liquid, gas):
        _no_overlap(pts, r)
    for i, x in enumerate(xs):
        b.append(rect(x, top, bw, bh, "none", INK, 3))
    for pts in (solid, liquid, gas):
        for (cx, cy) in pts:
            b.append(circ(cx, cy, r, PART, INK, 2.6))
    for x, name in zip(xs, ("solid", "liquid", "gas")):
        b.append(txt(x + bw / 2, top + bh + 46, name, FS))
    return svg(W, H, "Three boxes of particles. Solid: the particles are in a regular pattern, all "
               "touching, in fixed positions. Liquid: the particles are still touching but have no "
               "regular pattern, and the liquid sits in the bottom of its box. Gas: a few particles "
               "far apart, spread through the whole box.", b)


# ------------------------------------------------------------------ 2  volume by displacement
def displacement_volume():
    W, H = 720, 600
    before, after = 50, 62
    assert after - before == 12
    yb, yt = 520, 120                 # the cylinder's 0 and 100 cm³ marks
    Y = lambda v: yb - v * (yb - yt) / 100.0
    b = []
    for cx, level, stone in ((170, before, False), (500, after, True)):
        hw = 55
        # water, then the glass over it
        b.append(rect(cx - hw, Y(level), 2 * hw, yb - Y(level), WATER, "none", 2.6))
        if stone:
            b.append(pathel("M%s,%s L%s,%s L%s,%s L%s,%s Z" % (
                f(cx - 30), f(yb - 6), f(cx - 20), f(yb - 50), f(cx + 26), f(yb - 44), f(cx + 32), f(yb - 8)),
                INK, 3, "#8C8268"))
            b.append(line(cx + 2, yb - 47, cx + 2, Y(100) - 40, INK, 2.6, "butt"))
        b.append(pathel("M%s,%s V%s H%s V%s" % (f(cx - hw), f(Y(100) - 20), f(yb), f(cx + hw), f(Y(100) - 20)),
                        INK, 4))
        b.append(rect(cx - hw - 20, yb, 2 * hw + 40, 14, INK, INK, 3))
        for v in range(0, 101, 10):
            b.append(line(cx - hw, Y(v), cx - hw + (22 if v % 50 == 0 else 12), Y(v), INK, 2.6, "butt"))
        b.append(line(cx + hw + 8, Y(level), cx + hw + 30, Y(level), INK, 2.6, "butt"))
        b.append(txt(cx + hw + 38, Y(level) + 10, "%d cm³" % level, FS, "start"))
    b.append(txt(170, 584, "before", FS))
    b.append(txt(500, 584, "stone lowered in", FS))
    b.append(lines(360, 50, ["volume of stone = 62 cm³ − 50 cm³ = 12 cm³"], FS, "middle", RUST))
    return svg(W, H, "Two measuring cylinders. Before: water up to the 50 cm³ mark. After: a stone "
               "has been lowered in on a thread, and the water has risen to the 62 cm³ mark. The "
               "volume of the stone is 62 cm³ minus 50 cm³, which is 12 cm³.", b)


# ------------------------------------------------------------------ 3  the changes of state
def state_changes():
    W, H = 720, 560
    b = []
    boxes = {"gas": (360, 70), "solid": (120, 470), "liquid": (600, 470)}
    hw, hh = 82, 36
    for name, (cx, cy) in boxes.items():
        b.append(rect(cx - hw, cy - hh, 2 * hw, 2 * hh, "#FFFFFF", INK, 3, 10))
        b.append(txt(cx, cy + 10, name, FS))
    # solid <-> liquid along the bottom
    b.append(arrow(210, 448, 510, 448, INK, 5, 22))
    b.append(txt(360, 432, "melting", FS))
    b.append(arrow(510, 494, 210, 494, INK, 5, 22))
    b.append(txt(360, 538, "freezing", FS))
    # liquid <-> gas on the right
    b.append(arrow(612, 430, 452, 96, INK, 5, 22))
    b.append(lines(546, 250, ["boiling or", "evaporating"], FS, "start", INK, 600, 34))
    b.append(arrow(420, 112, 568, 426, INK, 5, 22))
    b.append(txt(486, 300, "condensing", FS, "end"))
    # solid -> gas on the left
    b.append(arrow(140, 430, 280, 104, RUST, 5, 22))
    b.append(txt(196, 250, "sublimating", FS, "end", RUST))
    return svg(W, H, "Three boxes: gas at the top, solid at the bottom left, liquid at the bottom "
               "right. Arrows join them. Solid to liquid is melting. Liquid to solid is freezing. "
               "Liquid to gas is boiling or evaporating. Gas to liquid is condensing. Solid "
               "straight to gas is sublimating.", b)


REGISTRY = {
    "particle-states": particle_states,
    "displacement-volume": displacement_volume,
    "state-changes": state_changes,
}
