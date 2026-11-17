# -*- coding: utf-8 -*-
"""figlib.ks4lean_ecofig: lean Ecology lesson figures that REPLACE the kept Design figures
(`legacy-fig:<prop>`), which sat in sideways scrollers on a phone. DRAFT, 14 Nov 2026.
Pure standard library. REGISTRY: name -> no-arg fn returning SVG.

Drawn in figlib/ks4lean_eco.py's conventions and with its helpers (one 720 viewBox, Georgia 28,
the same palette, own #FFFDF8 background rect, path commands M L H V C Q Z only, no text on a dark
fill). Each figure keeps the science of the Design figure it replaces; FIGS.md lists every
difference. Arrows ALWAYS point from the eaten to the eater (the way biomass moves); carbon arrows
point the way carbon dioxide moves.
"""
try:
    from .ks4lean_eco import (INK, RUST, BLUE, GREEN, RED, BG, GREY, AMBER, FS, f, svg, line,
                              poly_line, txt, lines, circ, rect, poly, pathel, head, arrow, parrow,
                              leader, edge)
except ImportError:                      # the scratch draft, imported with figlib on sys.path
    from figlib.ks4lean_eco import (INK, RUST, BLUE, GREEN, RED, BG, GREY, AMBER, FS, f, svg, line,
                                    poly_line, txt, lines, circ, rect, poly, pathel, head, arrow,
                                    parrow, leader, edge)
import math

PROD, CONS, CONS2, TOP = "#CFE8C8", "#F6E3B4", "#F7D9B8", "#F3CBBE"
DEAD, SKYF, SOIL, TAPE = "#E7D9BD", "#DCE9F5", "#E6D8B8", "#F7E9A8"
DARKLEAF, WOOD = "#2E5E45", "#8A5A2B"


def ellipse(cx, cy, rx, ry, fill, stroke=INK, w=3):
    return '<ellipse cx="%s" cy="%s" rx="%s" ry="%s" fill="%s" stroke="%s" stroke-width="%s"/>' % (
        f(cx), f(cy), f(rx), f(ry), fill, stroke, w)


def box_label(cx, cy, w, h, rows, fill, sw=3, weight=600):
    """a rounded box centred on (cx, cy) holding one or two centred lines"""
    n = len(rows)
    y0 = cy + 10 - (n - 1) * 17
    return rect(cx - w / 2, cy - h / 2, w, h, fill, INK, sw, 12) + lines(cx, y0, rows, FS, "middle", INK, weight, 34)


def web(nodes, links, colour=INK, w=5, s=24):
    """nodes: name -> (cx, cy, w, h, rows, fill); links: (food, eater). Arrows first, boxes on top."""
    out = []
    for a, c in links:
        A, B = nodes[a], nodes[c]
        sx, sy = edge(A[0], A[1], A[2] / 2, A[3] / 2, B[0], B[1], 4)
        ex, ey = edge(B[0], B[1], B[2] / 2, B[3] / 2, A[0], A[1], 6)
        out.append(arrow(sx, sy, ex, ey, colour, w, s))
    for k, (cx, cy, bw, bh, rows, fill) in nodes.items():
        out.append(box_label(cx, cy, bw, bh, rows, fill))
    return out


# ------------------------------------------------------------------ deforestation: fFig
def deforestation_carbon():
    W, H = 720, 700
    b = []
    b.append(rect(20, 20, 680, 120, SKYF, INK, 3, 14))
    b.append(txt(360, 68, "atmosphere", FS, "middle", INK, 700))
    b.append(txt(360, 110, "carbon dioxide rising", FS, "middle", RUST))
    # ground
    b.append(rect(0, 600, 720, 100, SOIL, "none", 1))
    b.append(line(0, 600, 720, 600, INK, 4, "butt"))
    c1, c2, c3 = 132, 360, 592
    # column 1: stumps; a THIN arrow down: less carbon dioxide taken in by photosynthesis
    for x in (c1 - 48, c1 + 48):
        b.append(rect(x - 12, 560, 24, 40, WOOD, INK, 3, 2))
        b.append(line(x - 16, 560, x + 16, 560, INK, 3, "butt"))
    b.append(arrow(c1, 146, c1, 398, GREEN, 4, 22))
    b.append(lines(c1, 438, ["less", "photosynthesis,", "less taken in"], FS, "middle", GREEN, 600, 34))
    b.append(txt(c1, 654, "tree stumps", FS))
    # column 2: burning; a THICK arrow up
    b.append(pathel("M318,600 C318,560 336,548 344,520 C352,544 360,536 362,508 C376,532 392,548 "
                    "396,600 Z", RED, 3, "#F6C24A"))
    b.append(arrow(c2, 392, c2, 146, RED, 10, 34))
    b.append(lines(c2, 446, ["burning", "releases"], FS, "middle", RED, 600, 34))
    # column 3: rotting wood; a THICK arrow up
    b.append(rect(c3 - 70, 562, 140, 36, WOOD, INK, 3, 10))
    for (px, py) in ((c3 - 46, 556), (c3 - 14, 554), (c3 + 18, 556), (c3 + 48, 555)):
        b.append(ellipse(px, py, 13, 7, "#E9DDBB", INK, 2.6))
    b.append(arrow(c3, 392, c3, 146, RED, 10, 34))
    b.append(lines(c3, 428, ["decay:", "microorganisms", "respire and", "release"], FS, "middle", RED, 600, 34))
    b.append(txt(c3, 654, "rotting wood", FS))
    return svg(W, H, "A cleared forest under the atmosphere: tree stumps with a thin photosynthesis arrow taking in less carbon dioxide, and thick arrows releasing carbon dioxide from burning and from microorganisms decaying the rotting wood. Atmospheric carbon dioxide is rising.", b)


# ------------------------------------------------------------------ ecosystems: wFig
def woodland_web():
    W, H = 720, 580
    b = []
    X1, X2, X3 = 125, 360, 595
    T, M, B = 92, 300, 500
    bw, bh = 210, 84
    nodes = {
        "shrews": (X1, T, bw, bh, ["shrews"], TOP),
        "worms": (X1, M, bw, bh, ["earthworms"], CONS),
        "litter": (X1, B, bw, bh, ["leaf litter"], DEAD),
        "wolves": (X2, T, bw, bh, ["wolves"], TOP),
        "deer": (X2, M, bw, bh, ["deer"], CONS),
        "grass": (X2, B, bw, bh, ["grass and", "shrubs"], PROD),
        "bees": (X3, M, bw, bh, ["bees"], CONS),
        "flowers": (X3, B, bw, bh, ["flowering", "plants"], PROD),
    }
    links = [("litter", "worms"), ("worms", "shrews"), ("grass", "deer"), ("flowers", "deer"),
             ("deer", "wolves")]
    b += [x for x in web(nodes, links) if x.startswith("<line") or x.startswith("<polygon")]
    # flowers -> bees (nectar), solid; bees -> flowers (pollination), dashed green
    top_f, bot_b = B - bh / 2, M + bh / 2
    b.append(arrow(X3 - 30, top_f - 4, X3 - 30, bot_b + 6, INK, 5, 24))
    b.append(line(X3 + 40, bot_b + 4, X3 + 40, top_f - 6 - 24 * 0.8, GREEN, 5, "butt", "12 9"))
    b.append(head(X3 + 40, top_f - 6, 0, 1, GREEN, 24))
    for k, (cx, cy, w_, h_, rows, fill) in nodes.items():
        b.append(box_label(cx, cy, w_, h_, rows, fill))
    # key for the dashed arrow, in the empty top cell
    b.append(line(X3 - 60, 64, X3 + 40, 64, GREEN, 5, "butt", "12 9"))
    b.append(head(X3 + 64, 64, 1, 0, GREEN, 24))
    b.append(txt(X3, 116, "pollinates", FS, "middle", GREEN))
    return svg(W, H, "A woodland food web in three columns: leaf litter to earthworms to shrews; grass and shrubs to deer to wolves; flowering plants to deer and to bees. A dashed arrow from the bees to the flowering plants shows pollination.", b)


# ------------------------------------------------------------------ food chains and webs: chFig
def _vertical_chain(items, levels=False, apex=None):
    """items bottom-up: (name, role, fill). Producer at the BOTTOM, arrows up (eaten -> eater)."""
    n = len(items)
    pitch, top = 160, 82
    bx0, bw, bh = (130, 240, 76) if levels else (40, 250, 76)
    cx = bx0 + bw / 2
    rx = bx0 + bw + 28
    ys = [top + (n - 1 - i) * pitch for i in range(n)]
    b = []
    for i in range(n - 1):
        b.append(arrow(cx, ys[i] - bh / 2 - 4, cx, ys[i + 1] + bh / 2 + 6, INK, 6, 26))
    for i, (name, role, fill) in enumerate(items):
        y = ys[i]
        b.append(box_label(cx, y, bw, bh, [name], fill))
        if levels:
            b.append(txt(20, y + 10, "level %d" % (i + 1), FS, "start", INK, 700))
        if apex and i == n - 1:
            b.append(txt(rx, y - 8, role, FS, "start"))
            b.append(lines(rx, y + 28, apex, FS, "start", RED, 600, 34))
        else:
            b.append(txt(rx, y + 10, role, FS, "start"))
    return b, ys[0] + bh / 2 + 24


def food_chain():
    b, H = _vertical_chain([("grass", "producer", PROD), ("rabbit", "primary consumer", CONS),
                            ("fox", "secondary consumer", CONS2), ("eagle", "tertiary consumer", TOP)])
    return svg(720, int(H), "A food chain drawn upwards: grass (producer), rabbit (primary consumer), fox (secondary consumer), eagle (tertiary consumer), with an arrow from each organism to the one that eats it.", b)


# ------------------------------------------------------------------ food chains and webs: wFig
def field_food_web():
    W, H = 720, 640
    b = []
    bw, bh = 230, 64
    nodes = {
        "owl": (540, 62, bw, bh, ["owls"], TOP),
        "fox": (180, 152, bw, bh, ["foxes"], TOP),
        "shrew": (540, 248, bw, bh, ["shrews"], CONS2),
        "rabbit": (180, 384, bw, bh, ["rabbits"], CONS),
        "hopper": (540, 424, bw, bh, ["grasshoppers"], CONS),
        "grass": (360, 586, 330, bh, ["grass (producer)"], PROD),
    }
    links = [("grass", "rabbit"), ("grass", "hopper"), ("rabbit", "fox"), ("hopper", "shrew"),
             ("shrew", "owl"), ("shrew", "fox")]
    b += web(nodes, links, INK, 5, 24)
    return svg(W, H, "A field food web: grass (producer) is eaten by rabbits and grasshoppers; foxes eat rabbits and shrews; shrews eat grasshoppers; owls eat shrews. Arrows point from the food to the eater.", b)


# ------------------------------------------------------------------ maintaining biodiversity: hFig
def hedgerow_field():
    W, H = 720, 590
    b = []
    b.append(txt(360, 44, "hedgerow", FS, "middle", INK, 700))
    hedge = []
    for y in (96, 540):
        for k in range(12):
            hedge.append(circ(48 + k * 57, y, 30, DARKLEAF, INK, 3))
    b += hedge[:12]
    b.append(rect(20, 130, 680, 64, "#C4E3AE", INK, 3))
    b.append(txt(360, 172, "field margin: wild flowers and grasses", FS))
    b.append(rect(20, 194, 680, 250, "#ECDD94", INK, 3))
    for y in (222, 254, 286, 362, 394, 422):
        b.append(line(44, y, 676, y, "#B59D3E", 3, "round"))
    b.append(txt(360, 334, "one crop: wheat", FS, "middle", INK, 700))
    b.append(rect(20, 444, 680, 64, "#C4E3AE", INK, 3))
    b.append(txt(360, 486, "field margin", FS))
    b += hedge[12:]
    return svg(W, H, "A wheat field of one crop with a field margin of wild flowers and grasses along each edge, and a hedgerow beyond each margin.", b)


# ------------------------------------------------------------------ population and competition: cFig
def competition_resources():
    W, H = 720, 800
    b = []
    # plants
    b.append(rect(20, 20, 680, 410, "#EEF6E8", INK, 3, 16))
    b.append(txt(360, 66, "Plants compete for", FS, "middle", INK, 700))
    for k in range(10):
        a = k * math.pi / 5
        b.append(line(92 + 40 * math.cos(a), 140 + 40 * math.sin(a), 92 + 54 * math.cos(a), 140 + 54 * math.sin(a), AMBER, 5))
    b.append(circ(92, 140, 30, "#F6D860", AMBER, 4))
    b.append(txt(160, 150, "light", FS, "start"))
    b.append(rect(22, 360, 676, 68, SOIL, "none", 1, 0))
    b.append(line(22, 360, 698, 360, INK, 3, "butt"))
    for (x, h) in ((230, 150), (330, 112), (440, 96), (560, 140)):
        b.append(line(x, 360, x, 360 - h, GREEN, 6))
        b.append(ellipse(x - 20, 360 - h * 0.55, 22, 10, "#8FC98A", INK, 2.6))
        b.append(ellipse(x + 20, 360 - h * 0.8, 22, 10, "#8FC98A", INK, 2.6))
        for d in (-18, 0, 18):
            b.append(line(x, 362, x + d, 378, WOOD, 3))
    b.append(txt(385, 206, "space", FS))
    b.append(txt(360, 412, "water and mineral ions from the soil", FS))
    # animals
    b.append(rect(20, 450, 680, 330, "#FBF0E6", INK, 3, 16))
    b.append(txt(360, 496, "Animals compete for", FS, "middle", INK, 700))

    def animal(x, y, face, fill=CONS):
        return ellipse(x, y, 34, 20, fill, INK, 3) + circ(x + face * 34, y - 18, 13, fill, INK, 3) + \
            circ(x + face * 38, y - 21, 3, INK, INK, 1)
    # food: two animals at one food item
    b.append(animal(62, 640, 1)); b.append(animal(182, 640, -1))
    b.append(circ(122, 652, 11, "#B5651D", INK, 3))
    b.append(txt(122, 738, "food", FS))
    # mates: two same-colour rivals on one baseline, facing the one mate between them
    b.append(animal(282, 640, 1)); b.append(animal(438, 640, -1))
    b.append(ellipse(360, 642, 24, 18, TOP, INK, 3) + circ(360, 614, 12, TOP, INK, 3) + circ(360, 612, 3, INK, INK, 1))
    b.append(txt(360, 738, "mates", FS))
    # territory: one animal holding a marked area
    b.append(rect(500, 552, 180, 140, "none", INK, 4, 0).replace('stroke-width="4"', 'stroke-width="4" stroke-dasharray="12 9"'))
    b.append(animal(586, 636, 1))
    b.append(txt(590, 738, "territory", FS))
    return svg(W, H, "Two panels. Plants compete for light, space, and water and mineral ions from the soil: four plants of different heights share one strip of soil under the Sun. Animals compete for food, mates and territory: two animals at one food item, two rivals facing one mate, and an animal holding a marked territory.", b)


# ------------------------------------------------------------------ population and competition: gFig
def predator_prey_graph():
    W, H = 720, 560
    x0, x1, yb, yt = 90, 690, 430, 120
    X = lambda t: x0 + t * (x1 - x0) / 8.0
    Y = lambda v: yb - v * (yb - yt) / 120.0
    prey = lambda t: 70 + 45 * math.sin(2 * math.pi * (t - 0.5) / 6)     # the Design curve: peak at 2
    pred = lambda t: 32 + 20 * math.sin(2 * math.pi * (t - 2) / 6)       # the Design curve: peak at 3.5
    b = []
    b.append(line(x0, yt - 20, x0, yb, INK, 4, "butt"))
    b.append(line(x0, yb, x1 + 6, yb, INK, 4, "butt"))
    for t in range(9):
        b.append(line(X(t), yb, X(t), yb + 10, INK, 3, "butt"))
        b.append(txt(X(t), yb + 44, str(t), FS))
    b.append(txt(390, 522, "time (years)", FS))
    b.append(txt(24, 70, "number", FS, "start"))
    ts = [i / 10.0 for i in range(81)]
    b.append(poly_line([(X(t), Y(prey(t))) for t in ts], GREEN, 5))
    b.append(poly_line([(X(t), Y(pred(t))) for t in ts], RED, 5))
    # the lag: from the prey peak (year 2) to the predator peak (year 3.5)
    b.append(line(X(2), Y(prey(2)) - 8, X(2), 96, GREY, 3, "butt", "8 8"))
    b.append(line(X(3.5), Y(pred(3.5)) - 8, X(3.5), 96, GREY, 3, "butt", "8 8"))
    b.append(arrow(X(2) + 4, 96, X(3.5) - 4, 96, INK, 4, 20))
    b.append(txt((X(2) + X(3.5)) / 2, 76, "lag", FS, "middle", INK, 700))
    # key
    b.append(line(380, 44, 420, 44, GREEN, 5, "butt"))
    b.append(txt(432, 54, "hares (prey)", FS, "start", GREEN))
    b.append(line(380, 90, 420, 90, RED, 5, "butt"))
    b.append(txt(432, 100, "lynx (predator)", FS, "start", RED))
    return svg(W, H, "Line graph of the numbers of hares (prey) and lynx (predator) over 8 years: both rise and fall in cycles, and each lynx peak comes after a hare peak. A lag arrow runs from the hare peak at year 2 to the lynx peak at year 3.5.", b)


# ------------------------------------------------------------------ pyramids of biomass: pFig
def biomass_pyramid():
    W, H = 720, 530
    CM = 48.0                      # 1 cm of the drawing; the scale is 1 cm = 40 g/m2
    cx, h = 420, 76
    bars = [(400, PROD, ["grass 400 g/m²"]), (80, CONS, ["grasshoppers", "80 g/m²"]),
            (16, CONS2, ["frogs", "16 g/m²"])]
    yb = 420
    b = []
    for i, (bio, fill, lab) in enumerate(bars):
        w = bio / 40.0 * CM
        y = yb - (i + 1) * h
        b.append(rect(cx - w / 2, y, w, h, fill, INK, 3))
        b.append(txt(165, y + h / 2 + 10, "level %d" % (i + 1), FS, "end", INK, 700))
        if i == 0:
            b.append(txt(cx, y + h / 2 + 10, lab[0], FS))
        else:
            b.append(lines(cx + w / 2 + 14, y + h / 2 - 7, lab, FS, "start", INK, 600, 34))
    ys = 462
    b.append(line(180, ys, 180 + CM, ys, INK, 4, "butt"))
    b.append(line(180, ys - 10, 180, ys + 10, INK, 3, "butt"))
    b.append(line(180 + CM, ys - 10, 180 + CM, ys + 10, INK, 3, "butt"))
    b.append(txt(180 + CM / 2, ys + 46, "1 cm", FS))
    b.append(txt(272, ys + 46, "scale: 1 cm = 40 g/m²", FS, "start"))
    return svg(W, H, "A pyramid of biomass drawn to scale, level 1 at the bottom: grass 400 g/m² is 10 cm wide, grasshoppers 80 g/m² is 2 cm, frogs 16 g/m² is 0.4 cm. Scale: 1 cm = 40 g/m².", b)


# ------------------------------------------------------------------ sampling techniques: trFig
def belt_transect():
    W, H = 720, 500
    b = []
    b.append(rect(16, 60, 70, 350, DARKLEAF, INK, 3))
    b.append(rect(86, 60, 618, 350, "#DCEBC8", INK, 3))
    b.append(rect(86, 300, 618, 24, TAPE, INK, 3))
    counts = [0, 1, 3, 6, 9, 11]
    side = 72
    for k, n in enumerate(counts):
        x = 125 + k * 108
        b.append(rect(x - side / 2, 312 - side / 2, side, side, "none", INK, 4))
        for d in range(n):
            px = x - 24 + (d % 4) * 16
            py = 312 - 22 + (d // 4) * 22
            b.append(circ(px, py, 6, "#FFFFFF", INK, 2.6))
            b.append(circ(px, py, 2.4, AMBER, AMBER, 1))
        b.append(txt(x, 384, "%d m" % (2 * k), FS))
    # light meter above the 4 m quadrat
    lx = 125 + 2 * 108
    b.append(line(lx, 196, lx, 272, INK, 3, "butt", "8 7"))
    b.append(rect(lx - 32, 140, 64, 56, "#D9D1BD", INK, 3, 8))
    b.append(circ(lx, 162, 10, "#FFFFFF", INK, 3))
    b.append(txt(lx, 118, "light meter", FS))
    # quadrat label
    qx = 125 + 5 * 108
    b.append(txt(qx - 26, 202, "quadrat", FS))
    b.append(leader(qx, 214, qx, 312 - side / 2 - 2))
    b.append(txt(51, 452, "hedge", FS))
    b.append(txt(400, 452, "tape measure from the hedge", FS))
    return svg(W, H, "A belt transect from a hedge into a field: a tape measure with a quadrat every 2 m from 0 m to 10 m, holding 0, 1, 3, 6, 9 and 11 daisies, and a light meter used at each quadrat.", b)


# ------------------------------------------------------------------ transfer of biomass: lFig
def rabbit_biomass_losses():
    W, H = 720, 680
    b = []
    b.append(rect(20, 20, 360, 104, PROD, INK, 3, 12))
    b.append(lines(200, 62, ["1000 g of grass", "eaten by a rabbit"], FS, "middle", INK, 600, 34))
    rows = [(200, ["faeces (egested)"], CONS, 3),
            (334, ["carbon dioxide and water", "(respiration)"], TOP, 3),
            (468, ["urea and water (urine)"], SKYF, 3),
            (602, ["part of the rabbit’s body:", "about 100 g"], CONS2, 6)]
    tx = 70
    b.append(line(tx, 124, tx, rows[-1][0], INK, 6, "round"))
    for (y, lab, fill, sw) in rows:
        b.append(arrow(tx, y, 176, y, INK, 6, 26))
        b.append(rect(182, y - 48, 518, 96, fill, INK, sw, 12))
        n = len(lab)
        b.append(lines(441, y + 10 - (n - 1) * 17, lab, FS, "middle", INK, 700 if sw > 3 else 600, 34))
    return svg(W, H, "1000 g of grass eaten by a rabbit: some leaves as faeces (egested), some as carbon dioxide and water from respiration, some as urea and water in urine, and about 100 g becomes part of the rabbit’s body.", b)


# ------------------------------------------------------------------ trophic levels: lvFig
def oak_trophic_levels():
    b, H = _vertical_chain([("oak tree", "producer", PROD), ("caterpillar", "primary consumer", CONS),
                            ("blue tit", "secondary consumer", CONS2),
                            ("sparrowhawk", "tertiary consumer", TOP)],
                           levels=True, apex=["apex predator:", "no predators"])
    return svg(720, int(H), "A food chain drawn upwards with its trophic levels: oak tree level 1 (producer), caterpillar level 2 (primary consumer), blue tit level 3 (secondary consumer), sparrowhawk level 4 (tertiary consumer, the apex predator). Each arrow points from the organism eaten to the one that eats it.", b)


REGISTRY = {
    "deforestation-carbon": deforestation_carbon,
    "woodland-web": woodland_web,
    "food-chain": food_chain,
    "field-food-web": field_food_web,
    "hedgerow-field": hedgerow_field,
    "competition-resources": competition_resources,
    "predator-prey-graph": predator_prey_graph,
    "biomass-pyramid": biomass_pyramid,
    "belt-transect": belt_transect,
    "rabbit-biomass-losses": rabbit_biomass_losses,
    "oak-trophic-levels": oak_trophic_levels,
}
