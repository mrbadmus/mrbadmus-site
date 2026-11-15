# -*- coding: utf-8 -*-
"""figlib.ks4lean_eco: lean Ecology lesson figures, examined by the lead 13 Nov 2026 (9). Pure standard library. REGISTRY: name -> no-arg fn returning SVG.

Drawn directly in the repo-checked conventions (figlib/ks4lean_mag.py): Georgia, no text on a dark
fill, path commands M L H V C Q Z only, labels >= 27 at a 720 viewBox, own #FFFDF8 background rect.
Arrows ALWAYS point food -> eater in food webs; carbon arrows point the way carbon moves.
"""
import math

INK = "#221E1B"; RUST = "#A93411"; BLUE = "#1D4E89"; GREEN = "#1F6F64"
RED = "#C8102E"; BG = "#FFFDF8"; GREY = "#6B6B6B"; AMBER = "#D98E00"
FONT = "Georgia, serif"
FS = 28


def f(x):
    return ("%.1f" % x).rstrip("0").rstrip(".")


import re as _re


def _floor(s):
    return _re.sub(r'stroke-width="([\d.]+)"', lambda m: 'stroke-width="%s"' % f(max(float(m.group(1)), 2.6)), s)


def svg(W, H, label, body):
    return _floor('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" role="img" aria-label="%s">'
            '<rect x="0" y="0" width="%d" height="%d" fill="%s"/>%s</svg>' % (W, H, label, W, H, BG, "".join(body)))


def line(x1, y1, x2, y2, c=INK, w=4, cap="round", dash=None):
    d = ' stroke-dasharray="%s"' % dash if dash else ""
    return '<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s" stroke-linecap="%s"%s/>' % (
        f(x1), f(y1), f(x2), f(y2), c, w, cap, d)


def poly_line(pts, c=INK, w=4, dash=None):
    d = ' stroke-dasharray="%s"' % dash if dash else ""
    return '<polyline points="%s" fill="none" stroke="%s" stroke-width="%s" stroke-linejoin="round" stroke-linecap="round"%s/>' % (
        " ".join("%s,%s" % (f(x), f(y)) for x, y in pts), c, w, d)


def txt(x, y, s, size=FS, anchor="middle", fill=INK, weight=600):
    return '<text x="%s" y="%s" font-family="%s" font-size="%s" font-weight="%s" text-anchor="%s" fill="%s">%s</text>' % (
        f(x), f(y), FONT, size, weight, anchor, fill, s)


def lines(x, y, rows, size=FS, anchor="middle", fill=INK, weight=600, pitch=36):
    return "".join(txt(x, y + i * pitch, s, size, anchor, fill, weight) for i, s in enumerate(rows))


def circ(x, y, r, fill="none", stroke=INK, w=4):
    return '<circle cx="%s" cy="%s" r="%s" fill="%s" stroke="%s" stroke-width="%s"/>' % (f(x), f(y), f(r), fill, stroke, w)


def rect(x, y, w, h, fill="none", stroke=INK, sw=3, rx=0):
    return '<rect x="%s" y="%s" width="%s" height="%s" rx="%s" fill="%s" stroke="%s" stroke-width="%s"/>' % (
        f(x), f(y), f(w), f(h), rx, fill, stroke, sw)


def poly(pts, fill, stroke=INK, w=3):
    return '<polygon points="%s" fill="%s" stroke="%s" stroke-width="%s" stroke-linejoin="round"/>' % (
        " ".join("%s,%s" % (f(x), f(y)) for x, y in pts), fill, stroke, w)


def pathel(d, c, w=4, fill="none", dash=None):
    d2 = ' stroke-dasharray="%s"' % dash if dash else ""
    return '<path d="%s" fill="%s" stroke="%s" stroke-width="%s" stroke-linecap="round" stroke-linejoin="round"%s/>' % (d, fill, c, w, d2)


def head(x, y, dx, dy, c, s=26):
    n = math.hypot(dx, dy); dx /= n; dy /= n
    bx, by = x - dx * s, y - dy * s
    px, py = -dy, dx
    return poly([(x, y), (bx + px * s * 0.5, by + py * s * 0.5), (bx - px * s * 0.5, by - py * s * 0.5)], c, c, 1)


def arrow(x1, y1, x2, y2, c=INK, w=6, s=26):
    n = math.hypot(x2 - x1, y2 - y1); ux, uy = (x2 - x1) / n, (y2 - y1) / n
    return line(x1, y1, x2 - ux * s * 0.8, y2 - uy * s * 0.8, c, w, "butt") + head(x2, y2, ux, uy, c, s)


def parrow(pts, c=INK, w=6, s=26):
    """polyline arrow: head on the last segment."""
    (xa, ya), (xb, yb) = pts[-2], pts[-1]
    n = math.hypot(xb - xa, yb - ya); ux, uy = (xb - xa) / n, (yb - ya) / n
    body = list(pts[:-1]) + [(xb - ux * s * 0.8, yb - uy * s * 0.8)]
    return poly_line(body, c, w).replace('stroke-linecap="round"', 'stroke-linecap="butt"') + head(xb, yb, ux, uy, c, s)


def leader(x1, y1, x2, y2):
    return line(x1, y1, x2, y2, INK, 2.5) + circ(x2, y2, 4.5, INK, INK, 1)


def bez(p0, c1, c2, p3):
    return "M%s,%s C%s,%s %s,%s %s,%s" % (f(p0[0]), f(p0[1]), f(c1[0]), f(c1[1]), f(c2[0]), f(c2[1]), f(p3[0]), f(p3[1]))


def edge(cx, cy, hw, hh, tx, ty, gap=6):
    """point on the boundary of the box (centre cx,cy half sizes hw,hh) towards (tx,ty), pushed out by gap."""
    dx, dy = tx - cx, ty - cy
    k = min(hw / abs(dx) if dx else 1e9, hh / abs(dy) if dy else 1e9)
    n = math.hypot(dx, dy)
    return cx + dx * k + dx / n * gap, cy + dy * k + dy / n * gap


# ------------------------------------------------------------------ 1
def cod_stock_recovery():
    W, H = 720, 580
    x0, x1, yb, yt = 140, 672, 430, 90
    X = lambda yr: x0 + (yr - 1990) * (x1 - x0) / 25.0
    Y = lambda v: yb - v * (yb - yt) / 300.0
    b = []
    for v in range(0, 301, 50):
        b.append(line(x0, Y(v), x1, Y(v), "#E4DDCE", 2, "butt"))
        b.append(txt(124, Y(v) + 10, str(v), FS, "end"))
    for yr in range(1990, 2016, 5):
        b.append(line(X(yr), yb, X(yr), yb + 10, INK, 3, "butt"))
        b.append(txt(X(yr), 484, str(yr), FS))
    b.append(line(x0, yt - 10, x0, yb, INK, 4, "butt")); b.append(line(x0, yb, x1 + 6, yb, INK, 4, "butt"))
    b.append(txt(20, 48, "Cod stock (thousand tonnes)", FS, "start"))
    b.append(txt(405, 526, "Year", FS))
    b.append(txt(405, 562, "Made-up data for practice", FS))
    b.append(line(X(2001), yt, X(2001), yb, RUST, 4, "butt", "14 10"))
    b.append(lines(X(2001) + 16, 125, ["Quota and larger", "mesh introduced", "(2001)"], FS, "start", RUST))
    data = [(1990, 250), (1995, 150), (2000, 60), (2005, 70), (2010, 110), (2015, 160)]
    b.append(poly_line([(X(a), Y(v)) for a, v in data], BLUE, 5))
    for a, v in data:
        b.append(circ(X(a), Y(v), 8, BLUE, BLUE, 1))
    return svg(W, H, "Line graph of cod stock from 1990 to 2015: it falls to a low around 2000 and then recovers after quotas and larger mesh were introduced in 2001.", b)


# ------------------------------------------------------------------ 2
def mycoprotein_fermenter():
    W, H = 720, 930
    tx0, tx1, ty0, ty1, liq = 240, 460, 230, 660, 330
    b = []
    b.append(rect(tx0, ty0, tx1 - tx0, ty1 - ty0, "#EEF3F6", INK, 3, 26))
    b.append('<path d="M%d,%d H%d V%d C%d,%d %d,%d %d,%d H%d Z" fill="#F4E4B0" stroke="none"/>' % (
        tx0, liq, tx1, ty1 - 26, tx1, ty1, tx1 - 26, ty1, tx1 - 26 * 1.0, ty1, tx0 + 26) if False else "")
    b.append(rect(tx0 + 2, liq, tx1 - tx0 - 4, ty1 - liq - 3, "#F4E4B0", "none", 1, 24))
    b.append(rect(tx0, ty0, tx1 - tx0, ty1 - ty0, "none", INK, 5, 26))
    b.append(line(tx0 + 4, liq, tx1 - 4, liq, "#B89A4A", 3, "butt"))
    # fungal threads
    TH = "#8A5A2B"
    for (ax, ay, dx, dy) in ((268, 400, 46, 36), (350, 380, 50, -30), (420, 420, -52, 40), (276, 520, 52, 40),
                             (360, 500, 60, 30), (410, 560, -46, -34), (290, 600, 56, -20), (385, 610, 40, -30)):
        b.append(pathel(bez((ax, ay), (ax + dx * .5, ay - dy * .7), (ax + dx * .6, ay + dy * 1.1), (ax + dx, ay + dy)), TH, 4))
    # bubbles
    for (bx, by, r) in ((330, 600, 9), (362, 560, 11), (345, 515, 8), (372, 470, 10), (336, 430, 8), (358, 385, 9), (322, 480, 7)):
        b.append(circ(bx, by, r, "none", BLUE, 3.5))
    b.append(line(310, 628, 390, 628, GREY, 6, "butt"))
    b.append(line(350, 628, 350, ty1 + 4, GREY, 6, "butt"))
    # glucose in (top-left)
    b.append(lines(20, 186, ["glucose", "syrup in"], FS, "start"))
    b.append(arrow(130, 272, tx0 + 2, 272, RUST, 7, 28))
    # gas out (top)
    b.append(arrow(330, ty0 - 4, 330, 96, BLUE, 7, 28))
    b.append(lines(358, 112, ["air and carbon", "dioxide out"], FS, "start"))
    # air in (bottom)
    b.append(arrow(350, 760, 350, ty1 + 4, BLUE, 7, 28))
    b.append(txt(350, 808, "air in", FS))
    # fungus label
    b.append(lines(215, 420, ["Fusarium", "(fungus)"], FS, "end"))
    b.append(leader(224, 436, 286, 452))
    # product line
    b.append(parrow([(tx1 + 2, 600), (590, 600), (590, 700)], RUST, 7, 28))
    b.append(txt(470, 566, "fungal biomass", FS, "start") if False else lines(480, 552, ["fungal", "biomass"], FS, "start"))
    b.append(rect(480, 706, 220, 110, "#F7E3C6", INK, 3, 10))
    b.append(lines(590, 750, ["harvested", "and purified"], FS))
    b.append(arrow(590, 818, 590, 872, RUST, 7, 28))
    b.append(txt(590, 906, "mycoprotein", FS, "middle", INK, 700))
    return svg(W, H, "A fermenter part-filled with liquid: glucose syrup and air go in, Fusarium fungus grows, air and carbon dioxide leave, and fungal biomass is harvested and purified into mycoprotein.", b)


# ------------------------------------------------------------------ 3
def insulin_gm_bacteria():
    W, H = 720, 880
    b = []
    GENE = "#E4572E"
    # human cell
    cx, cy = 120, 215
    b.append(circ(cx, cy, 92, "#F6DDD6", INK, 4))
    b.append(circ(cx, cy, 52, "#E5D4EC", INK, 3))
    b.append(pathel(bez((cx - 40, cy + 6), (cx - 20, cy - 24), (cx + 0, cy + 30), (cx + 40, cy - 4)), GREY, 5))
    b.append(line(cx - 14, cy - 2, cx + 18, cy + 4, GENE, 9, "butt"))
    b.append(lines(cx, 52, ["human insulin", "gene"], FS))
    b.append(leader(cx, 92, cx, cy - 4))
    # gene inserted
    b.append(txt(340, 180, "gene inserted", FS))
    b.append(arrow(228, 215, 462, 215, INK, 7, 30))
    # bacterium
    bx0, by0, bw, bh = 480, 160, 190, 110
    b.append(rect(bx0, by0, bw, bh, "#D6E9D0", INK, 4, 52))
    b.append(circ(bx0 + 95, by0 + 55, 30, "none", GREY, 4))
    b.append(line(bx0 + 82, by0 + 36, bx0 + 108, by0 + 36, GENE, 9, "butt"))
    b.append(txt(bx0 + 95, 318, "GM bacterium", FS))
    # Z flow down to row 2
    b.append(parrow([(bx0 + 95, 336), (bx0 + 95, 390), (112, 390), (112, 436)], INK, 6, 28))
    # fermenter with many bacteria
    fx0, fy0, fw, fh = 38, 446, 150, 190
    b.append(rect(fx0, fy0, fw, fh, "#EEF3F6", INK, 3, 22))
    b.append(rect(fx0 + 2, fy0 + 52, fw - 4, fh - 55, "#F4E4B0", "none", 1, 20))
    b.append(rect(fx0, fy0, fw, fh, "none", INK, 5, 22))
    for (px, py) in ((70, 520), (110, 510), (150, 525), (88, 560), (130, 565), (66, 600), (108, 602), (150, 598), (90, 530), (128, 540)):
        b.append(rect(px - 11, py - 6, 22, 12, "#7FBF73", INK, 1.5, 6))
    b.append(lines(112, 676, ["GM bacteria", "multiply and", "make human", "insulin"], FS))
    # harvested and purified
    b.append(arrow(196, 545, 262, 545, INK, 7, 28))
    b.append(rect(268, 490, 214, 110, "#F7E3C6", INK, 3, 10))
    b.append(lines(375, 534, ["harvested", "and purified"], FS))
    b.append(arrow(488, 545, 550, 545, INK, 7, 28))
    # vial
    vx = 612
    b.append(rect(vx - 38, 470, 76, 150, "#DCEAF5", INK, 4, 10))
    b.append(rect(vx - 38, 530, 76, 90, "#BBD8EE", "none", 1, 10))
    b.append(rect(vx - 38, 470, 76, 150, "none", INK, 4, 10))
    b.append(rect(vx - 30, 446, 60, 28, "#D9D1BD", INK, 4, 4))
    b.append(lines(vx, 668, ["insulin", "to treat", "diabetes"], FS))
    return svg(W, H, "Human insulin gene cut from a human cell and inserted into a bacterium; the GM bacteria multiply in a fermenter and make human insulin, which is harvested and purified to treat diabetes.", b)


# ------------------------------------------------------------------ 4
def biodiversity_webs():
    W, H = 720, 880
    b = []
    PROD, CONS, TOP = "#CFE8C8", "#F6E3B4", "#F3CBBE"
    bw, bh = 200, 54

    def node(name, cx, cy, fill, w=bw):
        return dict(name=name, cx=cx, cy=cy, w=w, fill=fill)

    def draw(nodes, arrows):
        out = []
        pos = {n["name"]: n for n in nodes}
        for a, c in arrows:
            A, B = pos[a], pos[c]
            sx, sy = edge(A["cx"], A["cy"], A["w"] / 2, bh / 2, B["cx"], B["cy"], 4)
            ex, ey = edge(B["cx"], B["cy"], B["w"] / 2, bh / 2, A["cx"], A["cy"], 6)
            out.append(arrow(sx, sy, ex, ey, RUST, 4, 20))
        for n in nodes:
            out.append(rect(n["cx"] - n["w"] / 2, n["cy"] - bh / 2, n["w"], bh, n["fill"], INK, 3, 12))
            out.append(txt(n["cx"], n["cy"] + 10, n["name"], FS))
        return out
    b.append(txt(360, 44, "High biodiversity", FS, "middle", INK, 700))
    high = [node("grass", 105, 520, PROD, 170), node("bramble", 300, 520, PROD, 190), node("oak tree", 585, 520, PROD, 190),
            node("rabbit", 105, 370, CONS, 170), node("mouse", 300, 370, CONS, 170), node("caterpillar", 585, 370, CONS, 200),
            node("fox", 105, 215, TOP, 170), node("blue tit", 585, 245, TOP, 190), node("owl", 400, 120, TOP, 170)]
    b += draw(high, [("grass", "rabbit"), ("grass", "mouse"), ("bramble", "rabbit"), ("bramble", "mouse"),
                     ("oak tree", "caterpillar"), ("caterpillar", "blue tit"), ("rabbit", "fox"),
                     ("mouse", "fox"), ("mouse", "owl"), ("blue tit", "owl")])
    b.append(line(30, 622, 690, 622, "#D9D1BD", 3, "butt"))
    b.append(txt(360, 678, "Low biodiversity", FS, "middle", INK, 700))
    low = [node("grass", 110, 790, PROD, 170), node("rabbit", 360, 790, CONS, 170), node("fox", 610, 790, TOP, 170)]
    b += draw(low, [("grass", "rabbit"), ("rabbit", "fox")])
    return svg(W, H, "Two food webs with arrows from food to eater: a high biodiversity web with many linked food chains, and a low biodiversity web with one chain, grass to rabbit to fox.", b)


# ------------------------------------------------------------------ 5
def greenhouse_effect():
    W, H = 720, 800
    b = []
    SUN = "#F6D860"
    b.append(rect(0, 250, 720, 190, "#DCE9F5", "none", 1))
    b.append(line(0, 250, 720, 250, "#8FB0CF", 3, "butt")); b.append(line(0, 440, 720, 440, "#8FB0CF", 3, "butt"))
    b.append(rect(0, 665, 720, 135, "#E9DDBB", "none", 1))
    b.append(line(0, 665, 720, 665, INK, 4, "butt"))
    b.append(txt(360, 745, "Earth&#8217;s surface", FS))
    # sun
    for k in range(10):
        a = k * math.pi / 5
        b.append(line(80 + 58 * math.cos(a), 80 + 58 * math.sin(a), 80 + 78 * math.cos(a), 80 + 78 * math.sin(a), AMBER, 6))
    b.append(circ(80, 80, 48, SUN, AMBER, 5))
    # short wavelength in
    b.append(arrow(135, 150, 205, 655, AMBER, 9, 34))
    b.append(arrow(215, 135, 285, 640, AMBER, 9, 34))
    b.append(lines(310, 70, ["short wavelength", "radiation from", "the Sun"], FS, "start", "#8A5A00"))
    b.append(leader(305, 112, 232, 190) if False else "")
    # long wavelength out
    b.append(arrow(315, 655, 315, 190, RED, 9, 34))
    b.append(txt(372, 180, "long wavelength", FS, "start", RED) if False else lines(342, 178, ["long wavelength", "radiation"], FS, "start", RED)[:])
    # absorbed
    b.append(arrow(385, 655, 385, 345, RED, 9, 34))
    b.append(lines(430, 520, ["absorbed: the", "atmosphere", "warms"], FS, "start", RED))
    b.append(leader(425, 500, 388, 470))
    b.append(lines(704, 305, ["atmosphere:", "carbon dioxide", "and methane"], FS, "end"))
    return svg(W, H, "Short wavelength radiation from the Sun passes through the atmosphere to the surface; long wavelength radiation from the surface either escapes or is absorbed in the atmosphere, which warms.", b)


# ------------------------------------------------------------------ 6
def carbon_cycle():
    W, H = 720, 1060
    b = []
    C = "#4A4A4A"
    def box(x, y, w, h, rows, fill):
        s = rect(x, y, w, h, fill, INK, 3, 12)
        n = len(rows)
        y0 = y + h / 2 - (n - 1) * 18 + 10
        return s + lines(x + w / 2, y0, rows, FS)
    AIR, PL, AN, DE, FO = (30, 30, 660, 80), (80, 330, 290, 90), (480, 330, 170, 90), (330, 700, 270, 110), (20, 930, 220, 90)
    # arrows first
    A = []
    # air -> plants (photosynthesis), plants -> air (respiration)
    A.append(arrow(240, 112, 240, 328, GREEN, 6, 26))
    A.append(arrow(320, 328, 320, 112, RUST, 6, 26))
    A.append(arrow(600, 328, 600, 112, RUST, 6, 26))
    A.append(arrow(30, 928, 30, 112, GREY, 6, 26) if False else arrow(45, 928, 45, 112, GREY, 6, 26))
    # plants -> animals feeding
    A.append(arrow(372, 375, 478, 375, INK, 6, 26))
    # plants -> dead
    A.append(arrow(225, 422, 340, 698, INK, 6, 26))
    # animals -> dead
    A.append(arrow(560, 422, 560, 698, INK, 6, 26) if False else arrow(540, 422, 540, 698, INK, 6, 26))
    # dead -> air (decay) along right edge
    A.append(parrow([(602, 760), (684, 760), (684, 112)], RUST, 6, 26))
    # dead -> fossil
    A.append(arrow(360, 812, 242, 928, GREY, 6, 26))
    b += A
    b.append(box(*AIR[:4], ["Carbon dioxide in the air"], "#E3EEF7"))
    b.append(box(*PL, ["Plants and algae"], "#CFE8C8"))
    b.append(box(*AN, ["Animals"], "#F6E3B4"))
    b.append(box(*DE, ["Dead material", "and waste"], "#E7D9BD"))
    b.append(box(*FO, ["Fossil fuels"], "#DADADA"))
    # labels
    b.append(txt(226, 238, "photosynthesis", FS, "end", GREEN))
    b.append(txt(336, 188, "respiration", FS, "start", RUST))
    b.append(txt(585, 262, "respiration", FS, "end", RUST))
    b.append(txt(62, 640, "combustion", FS, "start", "#555555"))
    b.append(txt(425, 322, "feeding", FS))
    b.append(txt(250, 520, "death", FS, "end"))
    b.append(lines(522, 520, ["death and", "waste"], FS, "end"))
    b.append(lines(676, 862, ["decay", "(microorganisms", "respire)"], FS, "end", RUST))
    b.append(lines(300, 872, ["millions", "of years"], FS, "end", "#555555"))
    return svg(W, H, "The carbon cycle: carbon dioxide in the air is taken in by plants and algae by photosynthesis and returned by respiration, passes to animals by feeding, to dead material by death and waste, returns by decay, and fossil fuels return it by combustion.", b)


# ------------------------------------------------------------------ 7
def water_cycle():
    W, H = 720, 700
    b = []
    SKYL = "#EAF3FA"
    b.append(rect(420, 450, 300, 250, "#BFD9EC", "none", 1))
    b.append(line(420, 450, 720, 450, "#6FA8D6", 4, "butt"))
    # land
    land = "M0,700 L0,450 C60,450 110,360 200,350 C290,340 340,440 420,450 L420,700 Z"
    b.append(pathel(land, INK, 4, "#D8E8C0"))
    b.append(rect(2, 560, 416, 138, "#E6D8B8", "none", 1))
    b.append(line(2, 560, 418, 560, "#B89A4A", 2.5, "butt", "10 8"))
    # river
    b.append(pathel("M232,362 C280,400 300,430 340,443 C380,453 405,458 445,470", "#6FA8D6", 14))
    b.append(head(448, 471, 1, 0.3, BLUE, 26))
    b.append(txt(296, 408, "run-off", FS, "start", BLUE))
    # tree
    b.append(rect(80, 340, 18, 68, "#8A5A2B", INK, 3))
    b.append(circ(89, 305, 50, "#8FC98A", INK, 4))
    b.append(arrow(89, 244, 89, 176, GREEN, 6, 26))
    b.append(txt(20, 160, "transpiration", FS, "start", GREEN))
    # sun
    for k in range(10):
        a = k * math.pi / 5
        b.append(line(62 + 42 * math.cos(a), 70 + 42 * math.sin(a), 62 + 58 * math.cos(a), 70 + 58 * math.sin(a), AMBER, 5))
    b.append(circ(62, 70, 34, "#F6D860", AMBER, 4))
    # cloud
    CL = "#F2F5F8"
    cl = ((310, 135, 50), (385, 105, 60), (465, 135, 50))
    for (x, y, r) in cl:
        b.append(circ(x, y, r, "none", INK, 4))
    b.append(rect(262, 95, 252, 85, "none", INK, 4, 42))
    for (x, y, r) in cl:
        b.append(circ(x, y, r - 2, CL, "none", 1))
    b.append(rect(264, 97, 248, 81, CL, "none", 1, 40))
    b.append(txt(388, 152, "condensation", FS))
    # rain
    for x in (310, 352, 394):
        b.append(arrow(x, 196, x - 14, 318, BLUE, 5, 22))
    b.append(txt(420, 252, "precipitation", FS, "start", BLUE))
    # evaporation / vapour
    b.append(parrow([(690, 440), (690, 150), (532, 150)], AMBER, 7, 28))
    b.append(lines(670, 316, ["water", "vapour"], FS, "end"))
    b.append(txt(704, 506, "evaporation", FS, "end"))
    b.append(txt(590, 574, "sea", FS, "middle", INK, 700))
    # percolation + underground
    b.append(arrow(150, 395, 150, 545, BLUE, 6, 26))
    b.append(txt(168, 530, "percolation", FS, "start", BLUE))
    b.append(arrow(150, 600, 452, 600, BLUE, 6, 26))
    return svg(W, H, "The water cycle: water evaporates from the sea, condenses into cloud, falls as precipitation, runs off into a river to the sea, soaks into the ground by percolation, and plants release water vapour by transpiration.", b)


# ------------------------------------------------------------------ 8
def decomposer_feeding():
    W, H = 720, 1100
    b = []
    PANEL = "#F7F1E3"
    LEAF = "#D9C39A"
    BAC = "#CFE6C9"
    ys = (20, 395, 770)
    ph = 310
    for i, y in enumerate(ys):
        b.append(rect(20, y, 680, ph, PANEL, INK, 3, 14))
        b.append(circ(62, y + 42, 26, "#FFFDF8", INK, 3))
        b.append(txt(62, y + 53, str(i + 1), FS, "middle", INK, 700))
    for y in (ys[0] + ph, ys[1] + ph):
        b.append(arrow(360, y + 6, 360, y + 62, INK, 7, 28))
    # panel 1
    y = ys[0]
    b.append(pathel("M40,%d C150,%d 300,%d 400,%d C500,%d 600,%d 680,%d C600,%d 500,%d 400,%d C300,%d 150,%d 40,%d Z" % (
        y + 270, y + 240, y + 240, y + 250, y + 260, y + 245, y + 270, y + 295, y + 300, y + 292, y + 290, y + 305, y + 270), INK, 3, LEAF))
    b.append(rect(90, y + 168, 140, 62, BAC, INK, 3, 31))
    b.append(circ(130, y + 199, 8, "#8FBF86", INK, 2)); b.append(circ(185, y + 199, 8, "#8FBF86", INK, 2))
    for (x1, y1, x2, y2) in ((120, 232, 100, 262), (160, 232, 160, 268), (205, 232, 235, 262)):
        b.append(arrow(x1, y + y1 - 0, x2, y + y2, RED, 5, 20))
    b.append(lines(300, y + 90, ["enzymes secreted", "onto the dead", "matter"], FS, "start"))
    b.append(leader(290, y + 120, 228, y + 250))
    # panel 2
    y = ys[1]
    b.append(rect(40, y + 100, 640, 96, LEAF, INK, 3, 30))
    # long chain
    pts = [(80 + 36 * k, y + 148 + (14 if k % 2 else -14)) for k in range(9)]
    b.append(poly_line(pts, GREY, 4))
    for (px, py) in pts:
        b.append(circ(px, py, 11, "#C9A0DC", INK, 3))
    b.append(txt(250, y + 82, "chain breaks", FS, "start") if False else "")
    # arrow showing breaking
    b.append(arrow(385, y + 148, 440, y + 148, INK, 5, 22))
    sm = ((480, 128), (528, 168), (575, 130), (622, 170), (500, 175), (555, 150))
    for (px, py) in sm:
        b.append(circ(px, y + py, 11, "#C9A0DC", INK, 3))
    b.append(lines(300, y + 245, ["large molecules broken down", "into small soluble molecules"], FS, "middle"))
    b.append(leader(560, y + 218, 556, y + 164) if False else "")
    # panel 3
    y = ys[2]
    b.append(rect(120, y + 110, 330, 170, BAC, GREEN, 8, 60))
    b.append(circ(285, y + 195, 26, "#E5D4EC", INK, 3))
    for (px, py) in ((60, 150), (60, 215), (150, 85)):
        b.append(circ(px, y + py, 11, "#C9A0DC", INK, 3))
    b.append(arrow(80, y + 150, 150, y + 150, BLUE, 5, 20) if False else arrow(78, y + 168, 140, y + 178, BLUE, 5, 20))
    b.append(arrow(78, y + 225, 140, y + 225, BLUE, 5, 20))
    b.append(arrow(150, y + 98, 190, y + 140, BLUE, 5, 20))
    for (px, py) in ((200, 150), (180, 225), (230, 235)):
        b.append(circ(px, y + py, 11, "#C9A0DC", INK, 3))
    b.append(lines(490, y + 100, ["small soluble", "molecules", "diffuse in"], FS, "start"))
    b.append(leader(490, y + 150, 214, y + 232) if False else leader(495, y + 190, 244, y + 238))
    return svg(W, H, "Three steps of decay: a bacterium secretes enzymes onto a dead leaf, the large molecules break down into small soluble molecules, and the small molecules diffuse into the bacterium.", b)


# ------------------------------------------------------------------ 9
def random_quadrats():
    W, H = 720, 800
    ox, oy, sx, sy = 110, 600, 54.0, 51.0   # origin px, px per metre
    X = lambda m: ox + m * sx
    Y = lambda m: oy - m * sy
    b = []
    b.append(rect(ox, Y(10), 10 * sx, 10 * sy, "#D7ECC8", INK, 3))
    # tapes
    b.append(rect(ox - 8, oy, 10 * sx + 16, 32, "#F7E9A8", INK, 3))
    b.append(rect(ox - 36, Y(10) - 8, 36, 10 * sy + 16, "#F7E9A8", INK, 3))
    for k in range(11):
        h = 14 if k % 5 == 0 else 10
        b.append(line(X(k), oy, X(k), oy + h + 6, INK, 2.5, "butt"))
        b.append(txt(X(k), oy + 70, str(k), FS))
        b.append(line(ox - 6 - h, Y(k), ox, Y(k), INK, 2.5, "butt"))
        b.append(txt(ox - 46, Y(k) + 10, str(k), FS, "end"))
    b.append(txt(X(10) + 36, oy + 70, "m", FS, "start"))
    b.append(txt(ox - 46, Y(10) - 46, "m", FS, "end"))
    side = 36
    quads = [(1.4, 8.6), (5.2, 9.0), (8.3, 8.0), (2.2, 4.8), (6.1, 6.3), (9.0, 4.4), (4.4, 2.8), (7.4, 1.8), (1.3, 1.5)]
    qs = []
    for (mx, my) in quads:
        qs.append((mx, my))
    # dashed guides from the (3, 7) quadrat
    gx, gy = X(3), Y(7)
    b.append(line(gx, gy + side / 2, gx, oy, RUST, 3, "butt", "10 8"))
    b.append(line(gx - side / 2, gy, ox, gy, RUST, 3, "butt", "10 8"))
    for (mx, my) in qs:
        b.append(rect(X(mx) - side / 2, Y(my) - side / 2, side, side, "none", INK, 4))
    b.append(rect(gx - side / 2, gy - side / 2, side, side, "none", RUST, 5))
    b.append(txt(gx + 30, gy - 24, "(3, 7)", FS, "start", RUST, 700))
    # quadrat label + leader
    qx, qy = X(9.0), Y(4.4)
    b.append(txt(560, 330, "quadrat", FS, "middle"))
    b.append(leader(qx, 340, qx, qy - side / 2 - 2))
    # tape measure label
    b.append(txt(360, 775, "tape measure", FS))
    b.append(leader(X(4.5), 744, X(4.5), oy + 32))
    return svg(W, H, "A square field with a tape measure along two edges marked 0 to 10 metres, ten small square quadrats at random positions, and one quadrat at (3, 7) with dashed lines to the tape measures.", b)


REGISTRY = {
    "cod-stock-recovery": cod_stock_recovery,
    "mycoprotein-fermenter": mycoprotein_fermenter,
    "insulin-gm-bacteria": insulin_gm_bacteria,
    "biodiversity-webs": biodiversity_webs,
    "greenhouse-effect": greenhouse_effect,
    "carbon-cycle": carbon_cycle,
    "water-cycle": water_cycle,
    "decomposer-feeding": decomposer_feeding,
    "random-quadrats": random_quadrats,
}
