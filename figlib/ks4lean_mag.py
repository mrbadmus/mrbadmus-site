# -*- coding: utf-8 -*-
"""figlib.ks4lean_mag: the 17 figures of the lean Magnetism lesson.

Pure standard library. Each function returns an SVG string; REGISTRY maps the lean figure name
to its drawer. The lead examined every arrow, direction and label of these drawings on 13 Nov
2026. Do not change a drawing's geometry, directions or labels here. figlib/ks4lean.py wraps
each one in the manifest conversion and the figlib checks before a lean card may place it.
Each figure carries its own #FFFDF8 background rect.
"""
import math

INK = "#221E1B"; RUST = "#A93411"; BLUE = "#1D4E89"; GREEN = "#1F6F64"
NRED = "#C8102E"; SBLUE = "#2B5FA8"; BG = "#FFFDF8"; GREY = "#6B6B6B"
NTINT = "#F2A7B0"; STINT = "#A9C4EC"   # pole fills that carry a letter (check: no text on a dark fill)
COPPER = "#C77B30"; COPPER_D = "#7A4A1E"
FONT = "Georgia, serif"


def f(x):
    return ("%.1f" % x).rstrip("0").rstrip(".")


def svg(W, H, label, body):
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" role="img" aria-label="%s">'
            '<rect x="0" y="0" width="%d" height="%d" fill="%s"/>%s</svg>' % (W, H, label, W, H, BG, "".join(body)))


def line(x1, y1, x2, y2, c=INK, w=4, cap="round", dash=None):
    d = ' stroke-dasharray="%s"' % dash if dash else ""
    return '<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s" stroke-linecap="%s"%s/>' % (
        f(x1), f(y1), f(x2), f(y2), c, w, cap, d)


def poly_line(pts, c=INK, w=4):
    return '<polyline points="%s" fill="none" stroke="%s" stroke-width="%s" stroke-linejoin="round" stroke-linecap="round"/>' % (
        " ".join("%s,%s" % (f(x), f(y)) for x, y in pts), c, w)


def txt(x, y, s, size=30, anchor="middle", fill=INK, weight=700):
    return '<text x="%s" y="%s" font-family="%s" font-size="%s" font-weight="%s" text-anchor="%s" fill="%s">%s</text>' % (
        f(x), f(y), FONT, size, weight, anchor, fill, s)


def circ(x, y, r, fill="none", stroke=INK, w=4):
    return '<circle cx="%s" cy="%s" r="%s" fill="%s" stroke="%s" stroke-width="%s"/>' % (f(x), f(y), f(r), fill, stroke, w)


def rect(x, y, w, h, fill="none", stroke=INK, sw=3, rx=0):
    return '<rect x="%s" y="%s" width="%s" height="%s" rx="%s" fill="%s" stroke="%s" stroke-width="%s"/>' % (
        f(x), f(y), f(w), f(h), rx, fill, stroke, sw)


def poly(pts, fill, stroke=INK, w=3):
    return '<polygon points="%s" fill="%s" stroke="%s" stroke-width="%s" stroke-linejoin="round"/>' % (
        " ".join("%s,%s" % (f(x), f(y)) for x, y in pts), fill, stroke, w)


def head(x, y, dx, dy, c, s=24):
    n = math.hypot(dx, dy); dx /= n; dy /= n
    bx, by = x - dx * s, y - dy * s
    px, py = -dy, dx
    return poly([(x, y), (bx + px * s * 0.5, by + py * s * 0.5), (bx - px * s * 0.5, by - py * s * 0.5)], c, c, 1)


def arrow(x1, y1, x2, y2, c, w=6, s=26):
    n = math.hypot(x2 - x1, y2 - y1); ux, uy = (x2 - x1) / n, (y2 - y1) / n
    return line(x1, y1, x2 - ux * s * 0.8, y2 - uy * s * 0.8, c, w, "butt") + head(x2, y2, ux, uy, c, s)


def dotsym(x, y, r=18, w=4):
    return circ(x, y, r, BG, INK, w) + circ(x, y, r * 0.3, INK, INK, 1)


def crosssym(x, y, r=18, w=4):
    d = r * 0.62
    return circ(x, y, r, BG, INK, w) + line(x - d, y - d, x + d, y + d, INK, 4) + line(x - d, y + d, x + d, y - d, INK, 4)


def leader(x1, y1, x2, y2):
    return line(x1, y1, x2, y2, INK, 2.5) + circ(x2, y2, 4.5, INK, INK, 1)


def bez_pts(p0, c1, c2, p3, n=160):
    out = []
    for i in range(n + 1):
        t = i / n; u = 1 - t
        out.append((u**3 * p0[0] + 3 * u * u * t * c1[0] + 3 * u * t * t * c2[0] + t**3 * p3[0],
                    u**3 * p0[1] + 3 * u * u * t * c1[1] + 3 * u * t * t * c2[1] + t**3 * p3[1]))
    return out


def bez_d(p0, c1, c2, p3):
    return "M%s,%s C%s,%s %s,%s %s,%s" % (f(p0[0]), f(p0[1]), f(c1[0]), f(c1[1]), f(c2[0]), f(c2[1]), f(p3[0]), f(p3[1]))


def pathel(d, c, w=4, fill="none"):
    return '<path d="%s" fill="%s" stroke="%s" stroke-width="%s" stroke-linecap="round" stroke-linejoin="round"/>' % (d, fill, c, w)


def tangent_at(pts, frac):
    i = max(1, min(len(pts) - 2, int(frac * (len(pts) - 1))))
    (x0, y0), (x1, y1) = pts[i - 1], pts[i + 1]
    return pts[i][0], pts[i][1], x1 - x0, y1 - y0


def bez_field(p0, c1, c2, p3, c=RUST, w=4, frac=0.5, hs=24, rev=False):
    pts = bez_pts(p0, c1, c2, p3)
    x, y, dx, dy = tangent_at(pts, frac)
    if rev:
        dx, dy = -dx, -dy
    return pathel(bez_d(p0, c1, c2, p3), c, w) + head(x, y, dx, dy, c, hs)


def magnet(x, y, w, h, n_left=True, fs=34):
    a, b = ("N", "S") if n_left else ("S", "N")
    ca, cb = (NTINT, STINT) if n_left else (STINT, NTINT)
    return (rect(x, y, w / 2, h, ca, INK, 3) + rect(x + w / 2, y, w / 2, h, cb, INK, 3) +
            txt(x + w / 4, y + h / 2 + fs * 0.35, a, fs, fill=INK) +
            txt(x + 3 * w / 4, y + h / 2 + fs * 0.35, b, fs, fill=INK))


# ---------------------------------------------------------------- 1
def bar_magnet_field():
    W, H, cy = 720, 440, 220
    xl, xr = 250, 470
    b = []
    cx = (xl + xr) / 2
    for sgn in (-1, 1):
        for d, h, p, q in ((14, 50, 30, 80), (29, 100, 70, 110), (43, 150, 110, 140)):
            y0 = cy + sgn * d; ya = y0 + sgn * h
            pts = bez_pts((xl, y0), (xl - p, y0), (cx - q, ya), (cx, ya)) + bez_pts((cx, ya), (cx + q, ya), (xr + p, y0), (xr, y0))
            b.append(pathel(bez_d((xl, y0), (xl - p, y0), (cx - q, ya), (cx, ya)) + " " +
                            bez_d((cx, ya), (cx + q, ya), (xr + p, y0), (xr, y0)).replace("M", "C", 1).split("C", 1)[1].join(["C", ""]) if False else
                            bez_d((xl, y0), (xl - p, y0), (cx - q, ya), (cx, ya)) + " C%s,%s %s,%s %s,%s" % (f(cx + q), f(ya), f(xr + p), f(y0), f(xr), f(y0)), RUST, 4))
            b.append(head(cx, ya, 1, 0, RUST, 24))
    b.append(arrow(xl, cy, 90, cy, RUST, 4, 24))
    b.append(arrow(630, cy, xr, cy, RUST, 4, 24))
    b.append(magnet(xl, cy - 44, xr - xl, 88, True, 40))
    return svg(W, H, "A bar magnet with field lines leaving the N end, looping round and entering the S end.", b)


# ---------------------------------------------------------------- 2
def two_magnets():
    W, H = 720, 400
    b = []
    # top row
    y = 60
    b.append(magnet(110, y, 150, 60, True, 30)); b.append(magnet(420, y, 150, 60, True, 30))
    b.append(arrow(268, y + 30, 330, y + 30, GREEN, 7, 26)); b.append(arrow(412, y + 30, 350, y + 30, GREEN, 7, 26))
    b.append(txt(340, y + 120, "attract", 34))
    y = 240
    b.append(magnet(110, y, 150, 60, False, 30)); b.append(magnet(420, y, 150, 60, True, 30))
    b.append(arrow(102, y + 30, 40, y + 30, GREEN, 7, 26)); b.append(arrow(578, y + 30, 640, y + 30, GREEN, 7, 26))
    b.append(txt(340, y + 120, "repel", 34))
    return svg(W, H, "Two bar magnets: unlike poles facing attract, like poles facing repel.", b)


# ---------------------------------------------------------------- 3
def compass_plotting():
    W, H = 720, 420
    b = []
    mx, my, mw, mh = 210, 320, 300, 70
    seg1 = ((210, 350), (60, 350), (70, 110), (360, 110))
    seg2 = ((360, 110), (650, 110), (660, 350), (510, 350))
    pts = bez_pts(*seg1) + bez_pts(*seg2)[1:]
    cum = [0]
    for i in range(1, len(pts)):
        cum.append(cum[-1] + math.hypot(pts[i][0] - pts[i - 1][0], pts[i][1] - pts[i - 1][1]))
    tot = cum[-1]

    def at(s):
        i = 1
        while i < len(cum) - 1 and cum[i] < s:
            i += 1
        (x0, y0), (x1, y1) = pts[i - 1], pts[i]
        t = (s - cum[i - 1]) / max(1e-9, cum[i] - cum[i - 1])
        dx, dy = pts[min(i + 2, len(pts) - 1)][0] - pts[max(i - 3, 0)][0], pts[min(i + 2, len(pts) - 1)][1] - pts[max(i - 3, 0)][1]
        n = math.hypot(dx, dy)
        return x0 + (x1 - x0) * t, y0 + (y1 - y0) * t, dx / n, dy / n
    b.append(pathel(bez_d(*seg1), RUST, 4) + pathel(bez_d(*seg2), RUST, 4))
    for fr in (0.07, 0.93):
        x, y, dx, dy = at(tot * fr)
        b.append(head(x, y, dx, dy, RUST, 26))
    comps = []
    for k in range(6):
        s = tot / 2 + (k - 2.5) * 80
        comps.append(at(s))
    r = 33
    for x, y, dx, dy in comps:
        b.append(circ(x, y, r, BG, INK, 3.5))
    for x, y, dx, dy in comps:
        nx, ny = -dy, dx
        L = 27
        b.append(poly([(x + dx * L, y + dy * L), (x + nx * 6, y + ny * 6), (x - nx * 6, y - ny * 6)], NRED, NRED, 1))
        b.append(poly([(x - dx * L, y - dy * L), (x + nx * 6, y + ny * 6), (x - nx * 6, y - ny * 6)], "#555555", "#555555", 1))
        b.append(circ(x + dx * (L + 1), y + dy * (L + 1), 4.5, INK, INK, 1))
    b.append(magnet(mx, my, mw, mh, True, 38))
    x, y, dx, dy = comps[0]
    b.append(txt(30, 58, "plotting compass", 30, "start"))
    b.append(leader(110, 68, x - 12, y - r + 2))
    return svg(W, H, "A bar magnet with one field line and small plotting compasses along it, each needle pointing along the line.", b)


# ---------------------------------------------------------------- 4
def earth_field():
    W, H = 720, 570
    cx, cy, r = 360, 290, 105
    b = []
    for s in (-1, 1):
        for a, K, ky in ((60, 157, 200), (26, 258, 262)):
            y0 = cy + math.sqrt(r * r - a * a); y3 = cy - math.sqrt(r * r - a * a)
            p0 = (cx + s * a, y0); p3 = (cx + s * a, y3)
            b.append(bez_field(p0, (cx + s * K, cy + ky), (cx + s * K, cy - ky), p3, RUST, 4, 0.5, 24, False))
    b.append(circ(cx, cy, r, "#DCE9F5", INK, 4))
    # compass at equator on right
    kx = cx + 0.75 * 157 + 0.25 * 60
    b.append(circ(kx, cy, 24, BG, INK, 3.5))
    b.append(poly([(kx, cy - 22), (kx - 6, cy), (kx + 6, cy)], NRED, NRED, 1))
    b.append(poly([(kx, cy + 22), (kx - 6, cy), (kx + 6, cy)], "#555555", "#555555", 1))
    b.append(txt(cx, 70, "Geographic North", 32))
    b.append(txt(cx, 540, "Geographic South", 32))
    return svg(W, H, "The Earth with magnetic field lines like a bar magnet's, and a compass at the equator pointing towards Geographic North.", b)


# ---------------------------------------------------------------- 5
def wire_field():
    W, H = 640, 600
    cx, cy = 320, 270
    b = []
    for r in (60, 130, 220):
        b.append(circ(cx, cy, r, "none", RUST, 4))
        a = math.radians(45)
        x, y = cx + r * math.cos(a), cy - r * math.sin(a)
        b.append(head(x, y, -math.sin(a), -math.cos(a), RUST, 26))
    b.append(dotsym(cx, cy, 20, 4))
    b.append(dotsym(150, 545, 18, 4))
    b.append(txt(185, 556, "current out of the page", 28, "start"))
    return svg(W, H, "Top view of a wire carrying current out of the page, with circular field lines anticlockwise around it.", b)


def _wire_pair_circle(cx, cy, sense):
    # sense +1 anticlockwise, -1 clockwise (as seen)
    b = []
    for r in (45, 95, 160):
        b.append(circ(cx, cy, r, "none", RUST, 4))
        a = math.radians(45)
        x, y = cx + r * math.cos(a), cy - r * math.sin(a)
        dx, dy = -math.sin(a) * sense, -math.cos(a) * sense
        b.append(head(x, y, dx, dy, RUST, 26))
    return b


def wire_cross_section():
    W, H = 760, 470
    b = []
    cl, cr, cy = 195, 565, 200
    b += _wire_pair_circle(cl, cy, 1)
    b += _wire_pair_circle(cr, cy, -1)
    b.append(dotsym(cl, cy, 18)); b.append(crosssym(cr, cy, 18))
    b.append(txt(cl, 440, "current out of the page", 27))
    b.append(txt(cr, 440, "current into the page", 27))
    return svg(W, H, "Two wires end-on: current out of the page has anticlockwise field circles, current into the page has clockwise ones.", b)


# ---------------------------------------------------------------- 6
def solenoid_field():
    W, H = 780, 540
    b = []
    xs = [250 + 52 * i for i in range(6)]
    yt, yb = 200, 340
    xl, xr = 215, 545
    cx = (xl + xr) / 2
    for sgn, y0 in ((-1, 238), (1, 302)):
        for p, q, ya in ((60, 120, y0 + sgn * 100), (120, 150, y0 + sgn * 165)):
            d1 = "M%s,%s C%s,%s %s,%s %s,%s C%s,%s %s,%s %s,%s" % (
                f(xr), f(y0), f(xr + p), f(y0), f(cx + q), f(ya), f(cx), f(ya),
                f(cx - q), f(ya), f(xl - p), f(y0), f(xl), f(y0))
            b.append(pathel(d1, RUST, 4))
            b.append(head(cx, ya, -1, 0, RUST, 24))
    for y0 in (238, 270, 302):
        b.append(line(xl, y0, xr, y0, RUST, 4))
        b.append(head(380, y0, 1, 0, RUST, 24)); b.append(head(540, y0, 1, 0, RUST, 1) if False else "")
    for x in xs:
        b.append(dotsym(x, yt, 19, 4)); b.append(crosssym(x, yb, 19, 4))
    b.append(txt(598, 288, "N", 46)); b.append(txt(162, 288, "S", 46))
    return svg(W, H, "Side view of a solenoid: straight parallel field lines inside, looping round outside like a bar magnet, N at the right end.", b)


# ---------------------------------------------------------------- 7
def electric_bell():
    W, H = 830, 560
    ox = 60
    X = lambda x: x + ox
    b = []
    wire = []
    w = 4.5
    # wires
    wire.append(poly_line([(X(370), 140), (X(370), 122), (X(464), 122)], INK, w))          # upper coil -> strip
    wire.append(poly_line([(X(375), 190), (X(375), 230)], INK, w))                          # link between coils
    wire.append(poly_line([(X(290), 280), (X(290), 470), (250, 470)], INK, w))              # lower coil -> switch
    wire.append(poly_line([(106, 470), (180, 470)], INK, w))                                # battery -> switch
    wire.append(poly_line([(X(651), 372), (X(651), 520), (40, 520), (40, 470), (62, 470)], INK, w))  # screw -> battery
    b += wire
    # core
    b.append(rect(X(200), 152, 26, 116, GREY, INK, 3))
    b.append(rect(X(200), 152, 220, 26, GREY, INK, 3))
    b.append(rect(X(200), 242, 220, 26, GREY, INK, 3))
    # coils
    for y in (140, 230):
        b.append(rect(X(250), y, 130, 50, COPPER, INK, 3, 5))
        for xx in range(X(262), X(380), 14):
            b.append(line(xx, y + 4, xx, y + 46, COPPER_D, 3, "butt"))
    # armature, strip
    b.append(rect(X(442), 130, 22, 166, "#9A9A9A", INK, 3))
    b.append(rect(X(464), 62, 8, 323, "#3A3A3A", INK, 1))
    b.append(rect(X(448), 385, 40, 24, INK, INK, 1))
    # gong (left, above the electromagnet) and hammer reaching it from the armature top
    b.append(line(X(205), 105, X(205), 152, INK, 6))
    b.append(pathel("M%s,105 A62 62 0 0 1 %s,105 Z" % (X(193), X(317)), INK, 4, "#E0B84A"))
    b.append(line(X(464), 72, X(330), 72, INK, 7, "butt"))
    b.append(circ(X(318), 72, 13, INK, INK, 1))
    # contact screw
    b.append(line(X(473), 330, X(662), 330, INK, 8, "butt"))
    b.append(rect(X(640), 300, 22, 72, GREY, INK, 3))
    b.append(rect(X(662), 316, 18, 28, "#9A9A9A", INK, 3))
    # battery
    for x, h, sw in ((62, 20, 5), (76, 36, 5), (92, 20, 5), (106, 36, 5)):
        b.append(line(x, 470 - h, x, 470 + h, INK, sw + (2 if h > 25 else 3), "butt"))
    # switch
    b.append(circ(180, 470, 6, INK, INK, 1)); b.append(circ(250, 470, 6, INK, INK, 1))
    b.append(line(180, 470, 243, 448, INK, 5)); b.append(line(212, 459, 212, 430, INK, 5)); b.append(line(198, 428, 226, 428, INK, 7))
    # labels
    b.append(txt(215, 400, "switch", 30))
    b.append(txt(X(186), 200, "electro-", 30, "end")); b.append(txt(X(186), 233, "magnet", 30, "end")); b.append(leader(X(190), 212, X(205), 210))
    b.append(txt(X(306), 335, "iron", 30, "start")); b.append(txt(X(306), 368, "armature", 30, "start"))
    b.append(leader(X(400), 320, X(447), 292))
    b.append(txt(X(490), 288, "contact screw", 30, "start")); b.append(leader(X(540), 296, X(540), 326))
    b.append(txt(X(490), 425, "spring", 30, "start")); b.append(leader(X(488), 408, X(474), 372))
    b.append(txt(X(180), 88, "gong", 30, "end")); b.append(leader(X(183), 82, X(197), 88))
    return svg(W, H, "An electric bell: battery, switch, electromagnet, iron armature on a spring, contact screw, and a hammer that swings left to strike the gong, all in one series circuit.", b)


# ---------------------------------------------------------------- 8
def motor_effect():
    W, H = 720, 480
    b = []
    nx0, sx0 = 60, 560
    b.append(rect(nx0, 130, 100, 200, NTINT, INK, 3)); b.append(txt(nx0 + 50, 245, "N", 46, fill=INK))
    b.append(rect(sx0, 130, 100, 200, STINT, INK, 3)); b.append(txt(sx0 + 50, 245, "S", 46, fill=INK))
    for y in (170, 290):
        b.append(line(160, y, 560, y, RUST, 4)); b.append(head(250, y, 1, 0, RUST, 26)); b.append(head(470, y, 1, 0, RUST, 26))
    b.append(line(160, 230, 332, 230, RUST, 4)); b.append(line(388, 230, 560, 230, RUST, 4))
    b.append(head(250, 230, 1, 0, RUST, 26)); b.append(head(470, 230, 1, 0, RUST, 26))
    b.append(dotsym(360, 230, 26, 5))
    b.append(arrow(360, 196, 360, 70, GREEN, 8, 30))
    b.append(txt(385, 108, "force", 32, "start", GREEN))
    b.append(dotsym(150, 425, 18)); b.append(txt(185, 436, "current out of the page", 28, "start"))
    return svg(W, H, "A wire seen end-on between N and S poles with current out of the page; the force on it points up.", b)


# ---------------------------------------------------------------- 8b
def flhr_question():
    W, H = 720, 480
    b = []
    b.append(rect(60, 130, 100, 200, NTINT, INK, 3)); b.append(txt(110, 245, "N", 46, fill=INK))
    b.append(rect(560, 130, 100, 200, STINT, INK, 3)); b.append(txt(610, 245, "S", 46, fill=INK))
    for y in (170, 230, 290):
        b.append(line(160, y, 560, y, RUST, 4)); b.append(head(240, y, 1, 0, RUST, 26)); b.append(head(480, y, 1, 0, RUST, 26))
    b.append(arrow(360, 365, 360, 95, BLUE, 9, 32))
    b.append(txt(360, 425, "current", 32, "middle", BLUE))
    b.append(txt(412, 150, "?", 52))
    return svg(W, H, "A vertical wire carrying current upwards between an N pole on the left and an S pole on the right; the direction of the force is left for the pupil to find.", b)


# ---------------------------------------------------------------- 9
def flemings_lhr():
    W, H = 720, 540
    ox, oy = 300, 330
    b = []
    b.append(arrow(ox, oy, 570, oy, RUST, 8, 32))
    b.append(arrow(ox, oy, ox, 100, GREEN, 8, 32))
    a = math.radians(210)
    L = 175
    tx, ty = ox + L * math.cos(a), oy - L * math.sin(a)
    b.append(arrow(ox, oy, tx, ty, BLUE, 8, 32))
    b.append(circ(ox, oy, 6, INK, INK, 1))
    # right-angle marks
    b.append(poly_line([(ox + 30, oy), (ox + 30, oy - 30), (ox, oy - 30)], INK, 2.5))
    b.append(txt(570, 385, "Field", 30, "middle", RUST)); b.append(txt(570, 426, "(First finger)", 28, "middle", RUST, 600))
    b.append(txt(ox + 25, 95, "Force", 30, "start", GREEN)); b.append(txt(ox + 25, 136, "(thuMb)", 28, "start", GREEN, 600))
    b.append(txt(tx + 20, ty + 52, "Current", 30, "middle", BLUE)); b.append(txt(tx + 20, ty + 93, "(seCond finger)", 28, "middle", BLUE, 600))
    return svg(W, H, "Fleming's left-hand rule: field to the right, current towards the viewer, force upwards.", b)


# ---------------------------------------------------------------- 10
def dc_motor():
    W, H = 830, 600
    b = []
    dx, dy = 100, -80

    def block(x, y, w, h, fill, dark, letter):
        s = poly([(x + w, y), (x + w + dx, y + dy), (x + w + dx, y + h + dy), (x + w, y + h)], dark, INK, 3)
        s += poly([(x, y), (x + dx, y + dy), (x + w + dx, y + dy), (x + w, y)], dark, INK, 3)
        s += rect(x, y, w, h, fill, INK, 3) + txt(x + w / 2, y + h / 2 + 16, letter, 50, fill=INK)
        return s
    b.append(block(40, 190, 110, 210, NTINT, "#E05A6E", "N"))
    b.append(block(600, 190, 110, 210, STINT, "#6F97D0", "S"))
    FL, FR, BL, BR = (250, 350), (440, 350), (350, 270), (540, 270)
    b.append(arrow(265, 205, 595, 205, RUST, 5, 26))
    b.append(poly_line([FL, BL, BR, FR, FL], COPPER_D, 8))
    ml, mr = (300, 310), (490, 310)
    b.append(arrow(ml[0], ml[1], BL[0] - 4, BL[1] + 4, BLUE, 8, 28))
    b.append(arrow(mr[0], mr[1], FR[0] + 4, FR[1] - 4, BLUE, 8, 28))
    b.append(arrow(ml[0], ml[1] + 2, ml[0], 395, GREEN, 8, 30))
    b.append(arrow(mr[0], mr[1] - 2, mr[0], 235, GREEN, 8, 30))
    cx, cy, ro, ri = 345, 445, 40, 24
    g = math.radians(9)

    def half(a0, a1, sweep):
        p = lambda r, a: (cx + r * math.cos(a), cy - r * math.sin(a))
        x0, y0 = p(ro, a0); x1, y1 = p(ro, a1); x2, y2 = p(ri, a1); x3, y3 = p(ri, a0)
        return "M%s,%s A%s %s 0 0 %d %s,%s L%s,%s A%s %s 0 0 %d %s,%s Z" % (
            f(x0), f(y0), ro, ro, sweep, f(x1), f(y1), f(x2), f(y2), ri, ri, 1 - sweep, f(x3), f(y3))
    b.append(pathel(half(math.pi / 2 + g, 3 * math.pi / 2 - g, 0), INK, 3, "#D9A441"))
    b.append(pathel(half(-math.pi / 2 + g, math.pi / 2 - g, 0), INK, 3, "#D9A441"))
    b.append(poly_line([FL, (312, 410)], COPPER_D, 6)); b.append(poly_line([FR, (378, 410)], COPPER_D, 6))
    b.append(rect(262, 430, 40, 30, "#4A4A4A", INK, 3)); b.append(rect(388, 430, 40, 30, "#4A4A4A", INK, 3))
    b.append(poly_line([(282, 460), (282, 520), (325, 520)], INK, 4.5)); b.append(poly_line([(408, 460), (408, 520), (365, 520)], INK, 4.5))
    b.append(line(333, 496, 333, 544, INK, 7, "butt")); b.append(line(355, 508, 355, 532, INK, 7, "butt"))
    b.append(txt(345, 584, "d.c. supply", 30))
    b.append(txt(410, 248, "coil", 30)); b.append(leader(410, 254, 410, 268))
    b.append(txt(238, 486, "split-ring", 28, "end")); b.append(txt(238, 526, "commutator", 28, "end"))
    b.append(leader(244, 474, 308, 458))
    b.append(txt(448, 440, "brush", 30, "start")); b.append(leader(446, 434, 430, 442))
    return svg(W, H, "A simple d.c. motor: a coil between N and S poles, a split-ring commutator, two brushes and a d.c. supply.", b)


# ---------------------------------------------------------------- 11 / 12
def _coil_rect(x, y, w, h):
    s = rect(x, y, w, h, COPPER, INK, 3, 4)
    for xx in range(int(x + 11), int(x + w - 4), 14):
        s += line(xx, y + 4, xx, y + h - 4, COPPER_D, 3, "butt")
    return s


def _arcs(cx, cy, radii, ang=36):
    s = ""
    a = math.radians(ang)
    for r in radii:
        x0, y0 = cx + r * math.cos(a), cy - r * math.sin(a)
        x1, y1 = cx + r * math.cos(a), cy + r * math.sin(a)
        s += pathel("M%s,%s A%s %s 0 0 1 %s,%s" % (f(x0), f(y0), r, r, f(x1), f(y1)), INK, 4)
    return s


def _tilde(x, y, s=1.0):
    return pathel("M%s,%s C%s,%s %s,%s %s,%s S%s,%s %s,%s" % (f(x - 16 * s), f(y), f(x - 10 * s), f(y - 14 * s), f(x - 4 * s), f(y - 14 * s), f(x), f(y),
                                                            f(x + 10 * s), f(y + 14 * s), f(x + 16 * s), f(y)), INK, 3.5)


def loudspeaker():
    W, H = 800, 470
    b = []
    b.append(poly_line([(392, 168), (392, 70), (60, 70), (60, 202)], INK, 4.5))
    b.append(poly_line([(392, 292), (392, 425), (60, 425), (60, 258)], INK, 4.5))
    b.append(rect(215, 124, 36, 212, GREY, INK, 3))
    b.append(rect(215, 124, 160, 38, STINT, INK, 3)); b.append(txt(295, 153, "S", 30, fill=INK))
    b.append(rect(215, 298, 160, 38, STINT, INK, 3)); b.append(txt(295, 327, "S", 30, fill=INK))
    b.append(rect(251, 205, 125, 50, NTINT, INK, 3)); b.append(txt(313, 243, "N", 32, fill=INK))
    b.append(_coil_rect(295, 168, 110, 30)); b.append(_coil_rect(295, 262, 110, 30))
    b.append(poly([(405, 168), (625, 78), (625, 382), (405, 292)], "#EFE3C4", INK, 6))
    b.append(line(405, 168, 405, 292, INK, 8))
    b.append(_arcs(590, 230, (70, 115, 160), 34))
    b.append(circ(60, 230, 30, BG, INK, 4)); b.append(_tilde(60, 232))
    b.append(txt(102, 224, "a.c.", 28, "start")); b.append(txt(102, 256, "supply", 28, "start"))
    b.append(txt(585, 50, "cone", 30)); b.append(leader(585, 58, 585, 90))
    b.append(txt(470, 238, "coil", 30)); b.append(leader(445, 250, 385, 278))
    b.append(txt(375, 392, "permanent magnet", 30, "end")); b.append(leader(300, 362, 300, 340))
    return svg(W, H, "A loudspeaker in cross-section: a coil on a paper cone between the poles of a permanent magnet, wired to an a.c. supply.", b)


def microphone():
    W, H = 840, 470
    b = []
    b.append(poly_line([(300, 168), (300, 70), (640, 70)], INK, 4.5))
    b.append(poly_line([(300, 292), (300, 425), (640, 425)], INK, 4.5))
    b.append(circ(640, 70, 7, INK, INK, 1)); b.append(circ(640, 425, 7, INK, INK, 1))
    b.append(rect(560, 124, 36, 212, GREY, INK, 3))
    b.append(rect(345, 124, 251, 38, STINT, INK, 3)); b.append(txt(470, 153, "S", 30, fill=INK))
    b.append(rect(345, 298, 251, 38, STINT, INK, 3)); b.append(txt(470, 327, "S", 30, fill=INK))
    b.append(rect(365, 205, 195, 50, NTINT, INK, 3)); b.append(txt(465, 243, "N", 32, fill=INK))
    for y in (168, 262):
        b.append(rect(282, y, 70, 30, "none", INK, 3))
        b.append(_coil_rect(352, y, 100, 30))
    b.append(pathel("M276,105 Q258,230 276,355", INK, 12))
    b.append(_arcs(40, 230, (95, 140, 185), 30))
    b.append(txt(655, 232, "to", 30, "start")); b.append(txt(655, 266, "amplifier", 30, "start"))
    b.append(txt(262, 45, "diaphragm", 30, "middle")); b.append(leader(272, 52, 272, 103))
    b.append(txt(330, 112, "coil", 30, "start")); b.append(leader(335, 118, 328, 166))
    b.append(txt(470, 392, "permanent magnet", 30)); b.append(leader(470, 362, 470, 340))
    return svg(W, H, "A microphone in cross-section: sound moves a diaphragm and the coil attached to it, which sits in a permanent magnet's field.", b)


# ---------------------------------------------------------------- 13
def induced_current():
    W, H = 760, 560
    b = []
    # coil helix
    x0, yc, rx, ry, p, turns = 340, 200, 16, 46, 38, 6
    pts = []
    n = 400
    for i in range(n + 1):
        th = 2 * math.pi * turns * i / n
        pts.append((x0 + p * th / (2 * math.pi) + rx * math.sin(th), yc + ry * math.cos(th)))
    start, end = pts[0], pts[-1]
    b.append(poly_line([(start[0], start[1] + 0), (start[0], 420), (380, 420)], INK, 4.5))
    b.append(poly_line([(end[0], end[1]), (end[0], 420), (520, 420)], INK, 4.5))
    b.append(poly_line(pts, COPPER_D, 6))
    # magnet
    b.append(magnet(60, 170, 200, 60, False, 34))
    b.append(arrow(80, 125, 250, 125, GREEN, 8, 30))
    b.append(txt(165, 85, "magnet moved in", 30))
    # meter
    mx, my = 450, 440
    b.append(circ(mx, my, 75, BG, INK, 4))
    px, py = mx, my + 25
    b.append(pathel("M%s,%s A55 55 0 0 1 %s,%s" % (f(px - 55 * math.sin(math.radians(50))), f(py - 55 * math.cos(math.radians(50))),
                                                   f(px + 55 * math.sin(math.radians(50))), f(py - 55 * math.cos(math.radians(50)))), INK, 3))
    for a in (-50, -25, 0, 25, 50):
        s, c = math.sin(math.radians(a)), math.cos(math.radians(a))
        L = 18 if a == 0 else 10
        b.append(line(px + 55 * s, py - 55 * c, px + (55 - L) * s, py - (55 - L) * c, INK, 3))
    b.append(txt(px, py - 78 + 6, "0", 28))
    a = math.radians(26)
    b.append(line(px, py, px + 50 * math.sin(a), py - 50 * math.cos(a), NRED, 5))
    b.append(circ(px, py, 6, INK, INK, 1))
    b.append(circ(380, 420, 6, INK, INK, 1)); b.append(circ(520, 420, 6, INK, INK, 1))
    b.append(txt(mx, 545, "ammeter (centre zero)", 28))
    return svg(W, H, "A bar magnet moved towards a coil connected to a centre-zero ammeter, whose needle is deflected.", b)


# ---------------------------------------------------------------- 14
def ac_dc_output():
    W, H = 760, 370
    b = []
    for x0, kind, title in ((65, "ac", "alternator (a.c.)"), (440, "dc", "dynamo (d.c.)")):
        zy = 222
        b.append(txt(x0 + 130, 42, title, 30))
        b.append(txt(x0, 108, "p.d.", 28))
        b.append(line(x0, 118, x0, 335, INK, 3.5, "butt"))
        b.append(line(x0, zy, x0 + 235, zy, INK, 3.5, "butt")); b.append(head(x0 + 238, zy, 1, 0, INK, 14))
        b.append(head(x0, 114, 0, -1, INK, 14))
        b.append(txt(x0 - 12, zy + 9, "0", 26, "end"))
        b.append(txt(x0 + 236, zy + 10, "time", 28, "start"))
        pts = []
        for i in range(0, 211):
            t = i / 105.0
            v = math.sin(2 * math.pi * t) if kind == "ac" else abs(math.sin(math.pi * 2 * t))
            pts.append((x0 + i, zy - 72 * v))
        b.append(poly_line(pts[::2] + [pts[-1]], BLUE, 5))
    return svg(W, H, "Two graphs of p.d. against time: an alternating output crossing zero, and a direct output that stays above zero.", b)


# ---------------------------------------------------------------- 15
def transformer():
    W, H = 780, 500
    b = []
    b.append(poly_line([(236, 195), (110, 195), (110, 219)], INK, 4.5)); b.append(poly_line([(236, 315), (110, 315), (110, 291)], INK, 4.5))
    b.append(poly_line([(524, 190), (610, 190)], INK, 4.5)); b.append(poly_line([(524, 330), (610, 330)], INK, 4.5))
    b.append(circ(610, 190, 7, INK, INK, 1)); b.append(circ(610, 330, 7, INK, INK, 1))
    # core
    b.append('<path d="M250,120 H510 V400 H250 Z M300,170 V350 H460 V170 Z" fill="%s" stroke="%s" stroke-width="3" fill-rule="evenodd"/>' % (GREY, INK))
    for i in range(4):
        y = 195 + 40 * i
        b.append(line(236, y + 6, 314, y - 6, COPPER, 12, "butt")); b.append(line(236, y + 6, 314, y - 6, COPPER_D, 2, "butt") if False else "")
    for i in range(8):
        y = 190 + 20 * i
        b.append(line(446, y + 4, 524, y - 4, COPPER, 9, "butt"))
    b.append(circ(110, 255, 36, BG, INK, 4)); b.append(_tilde(110, 257, 1.1))
    b.append(txt(110, 370, "a.c. input", 28))
    b.append(txt(618, 266, "output", 28, "start"))
    b.append(txt(190, 85, "primary coil", 30)); b.append(leader(215, 94, 238, 190))
    b.append(txt(590, 85, "secondary coil", 30)); b.append(leader(560, 94, 526, 186))
    b.append(txt(380, 462, "iron core", 30)); b.append(leader(380, 432, 380, 402))
    def vn(cx, y, a, c):
        x = cx - 56
        return (txt(x, y, a, 30, "start") + txt(x + 30, y + 9, c, 20, "start") + txt(x + 57, y, ", n", 30, "start") +
                txt(x + 104, y + 9, c, 20, "start"))
    b.append(vn(185, 420, "V", "p")); b.append(vn(595, 420, "V", "s"))
    return svg(W, H, "A transformer: an iron core with a primary coil of 4 turns on the left limb and a secondary coil of 8 turns on the right.", b)


# ---------------------------------------------------------------- conformance
# The drawings above are the lead's approved ones. figlib/checks.py allows only M L H V C Q Z in a
# path, no fill-rule, and a stroke of at least 1px on screen at 320px. _conform rewrites those
# three things, geometry unchanged, on the way out: an arc or smooth-curve command becomes the
# identical cubic, an even-odd rect-in-rect already winds opposite ways so it needs no rule, and a
# hairline stroke is raised to just over 1px at 320px, and any label smaller than 11px in a 300px card
# is raised to 11px there (each raise is checked for collisions by ks4lean).
import re as _re


def _arc_to_cubics(x1, y1, rx, ry, phi, fa, fs, x2, y2):
    """SVG endpoint arc -> list of cubic segments (c1x,c1y,c2x,c2y,x,y). rx==ry, phi==0 here."""
    rx, ry = abs(rx), abs(ry)
    cp, sp = math.cos(math.radians(phi)), math.sin(math.radians(phi))
    dx, dy = (x1 - x2) / 2, (y1 - y2) / 2
    x1p, y1p = cp * dx + sp * dy, -sp * dx + cp * dy
    lam = (x1p / rx) ** 2 + (y1p / ry) ** 2
    if lam > 1:
        rx *= math.sqrt(lam); ry *= math.sqrt(lam)
    num = rx * rx * ry * ry - rx * rx * y1p * y1p - ry * ry * x1p * x1p
    den = rx * rx * y1p * y1p + ry * ry * x1p * x1p
    co = math.sqrt(max(0, num / den)) * (-1 if fa == fs else 1)
    cxp, cyp = co * rx * y1p / ry, -co * ry * x1p / rx
    cx = cp * cxp - sp * cyp + (x1 + x2) / 2
    cy = sp * cxp + cp * cyp + (y1 + y2) / 2

    def ang(ux, uy, vx, vy):
        a = math.atan2(ux * vy - uy * vx, ux * vx + uy * vy)
        return a
    t1 = ang(1, 0, (x1p - cxp) / rx, (y1p - cyp) / ry)
    dt = ang((x1p - cxp) / rx, (y1p - cyp) / ry, (-x1p - cxp) / rx, (-y1p - cyp) / ry)
    if not fs and dt > 0:
        dt -= 2 * math.pi
    elif fs and dt < 0:
        dt += 2 * math.pi
    n = max(1, int(math.ceil(abs(dt) / (math.pi / 2) - 1e-9)))
    d = dt / n
    k = 4 / 3 * math.tan(d / 4)
    out = []
    for i in range(n):
        a0, a1 = t1 + i * d, t1 + (i + 1) * d
        def pt(a, dd=0):
            return (cx + rx * math.cos(a), cy + ry * math.sin(a))
        p0, p3 = pt(a0), pt(a1)
        c1 = (p0[0] - k * rx * math.sin(a0), p0[1] + k * ry * math.cos(a0))
        c2 = (p3[0] + k * rx * math.sin(a1), p3[1] - k * ry * math.cos(a1))
        out.append((c1[0], c1[1], c2[0], c2[1], p3[0], p3[1]))
    return out


def _fix_d(d):
    toks = _re.findall(r"[A-Za-z]|-?\d*\.?\d+(?:e-?\d+)?", d)
    out, i, cur, start, lastc2, lastcmd = [], 0, (0, 0), (0, 0), None, None
    cmd = None
    nargs = {"M": 2, "L": 2, "H": 1, "V": 1, "C": 6, "S": 4, "Q": 4, "A": 7, "Z": 0}
    while i < len(toks):
        if toks[i].isalpha():
            cmd = toks[i]; i += 1
            assert cmd in nargs, "relative path command %r not handled" % cmd
            if cmd == "Z":
                out.append("Z"); cur = start; lastcmd = "Z"; continue
        a = [float(v) for v in toks[i:i + nargs[cmd]]]; i += nargs[cmd]
        if cmd == "M":
            cur = start = (a[0], a[1]); out.append("M%s,%s" % (f(a[0]), f(a[1]))); cmd = "L"
        elif cmd == "L":
            cur = (a[0], a[1]); out.append("L%s,%s" % (f(a[0]), f(a[1])))
        elif cmd == "H":
            cur = (a[0], cur[1]); out.append("H%s" % f(a[0]))
        elif cmd == "V":
            cur = (cur[0], a[0]); out.append("V%s" % f(a[0]))
        elif cmd == "C":
            out.append("C%s,%s %s,%s %s,%s" % tuple(f(v) for v in a)); lastc2 = (a[2], a[3]); cur = (a[4], a[5])
        elif cmd == "S":
            c1 = (2 * cur[0] - lastc2[0], 2 * cur[1] - lastc2[1]) if lastcmd in ("C", "S") else cur
            out.append("C%s,%s %s,%s %s,%s" % tuple(f(v) for v in (c1[0], c1[1], a[0], a[1], a[2], a[3])))
            lastc2 = (a[0], a[1]); cur = (a[2], a[3])
        elif cmd == "Q":
            out.append("Q%s,%s %s,%s" % tuple(f(v) for v in a)); cur = (a[2], a[3])
        elif cmd == "A":
            for c in _arc_to_cubics(cur[0], cur[1], a[0], a[1], a[2], int(a[3]), int(a[4]), a[5], a[6]):
                out.append("C%s,%s %s,%s %s,%s" % tuple(f(v) for v in c))
            cur = (a[5], a[6])
        lastcmd = cmd
    return " ".join(out)


def _conform(svg_str):
    W = float(_re.search(r'viewBox="0 0 ([\d.]+)', svg_str).group(1))
    floor = round(W / 320.0 * 1.1, 2)
    tfloor = int(W * 11.0 / 300.0) + 1       # smallest label must draw at 11px in a 300px card

    def dfix(m):
        return 'd="%s"' % _fix_d(m.group(1))
    svg_str = _re.sub(r'\bd="([^"]*[ASas][^"]*)"', dfix, svg_str)
    svg_str = svg_str.replace(' fill-rule="evenodd"', "")

    def sw(m):
        v = float(m.group(1))
        return 'stroke-width="%s"' % f(max(v, floor))
    def fs(m):
        return 'font-size="%s"' % f(max(float(m.group(1)), tfloor))
    svg_str = _re.sub(r'stroke-width="([\d.]+)"', sw, svg_str)
    return _re.sub(r'font-size="([\d.]+)"', fs, svg_str)


_DRAWERS = {
    "bar-magnet-field": bar_magnet_field,
    "two-magnets": two_magnets,
    "compass-plotting": compass_plotting,
    "earth-field": earth_field,
    "wire-field": wire_field,
    "wire-cross-section": wire_cross_section,
    "solenoid-field": solenoid_field,
    "electric-bell": electric_bell,
    "motor-effect": motor_effect,
    "flhr-question": flhr_question,
    "flemings-lhr": flemings_lhr,
    "dc-motor": dc_motor,
    "loudspeaker": loudspeaker,
    "microphone": microphone,
    "induced-current": induced_current,
    "ac-dc-output": ac_dc_output,
    "transformer": transformer,
}


def _wrap(fn):
    return lambda: _conform(fn())


REGISTRY = {name: _wrap(fn) for name, fn in _DRAWERS.items()}
