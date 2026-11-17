# -*- coding: utf-8 -*-
"""figlib.ks4lean_waves: lean Physics Waves lesson figures (12: nine examiner-checked, three
added 14 Nov 2026 for the new physics-only lessons), drafted 14 Nov 2026. Pure standard
library. REGISTRY: name -> no-arg fn returning SVG.

Same conventions as figlib/ks4lean_eco.py and ks4lean_mag.py: Georgia, no text on a dark fill,
labels >= 27 at a 720 viewBox (11.25px+ in a 300px card), own #FFFDF8 background rect.
Rays carry an arrow showing the direction light travels; normals are dashed and at 90° to the
boundary; wave fronts are at 90° to the direction of travel. Lens symbols follow AQA 8463
(convex: arrowheads pointing outwards; concave: arrowheads pointing inwards).
"""
import math
import re as _re

INK = "#221E1B"; RUST = "#A93411"; BLUE = "#1D4E89"; GREEN = "#1F6F64"
RED = "#C8102E"; BG = "#FFFDF8"; GREY = "#6B6B6B"; AMBER = "#B86E00"
GLASS = "#DCEAF7"; GROUND = "#B9D9B0"; SUNC = "#F2C14E"
FONT = "Georgia, serif"
FS = 28


def f(x):
    return ("%.1f" % x).rstrip("0").rstrip(".")


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


def lines(x, y, rows, size=FS, anchor="middle", fill=INK, weight=600, pitch=34):
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


def head(x, y, dx, dy, c, s=24):
    n = math.hypot(dx, dy); dx /= n; dy /= n
    bx, by = x - dx * s, y - dy * s
    px, py = -dy, dx
    return poly([(x, y), (bx + px * s * 0.5, by + py * s * 0.5), (bx - px * s * 0.5, by - py * s * 0.5)], c, c, 1)


def arrow(x1, y1, x2, y2, c=INK, w=5, s=24):
    n = math.hypot(x2 - x1, y2 - y1); ux, uy = (x2 - x1) / n, (y2 - y1) / n
    return line(x1, y1, x2 - ux * s * 0.8, y2 - uy * s * 0.8, c, w, "butt") + head(x2, y2, ux, uy, c, s)


def darrow(x1, y1, x2, y2, c=INK, w=4, s=20):
    """double-headed arrow."""
    n = math.hypot(x2 - x1, y2 - y1); ux, uy = (x2 - x1) / n, (y2 - y1) / n
    return (line(x1 + ux * s * 0.8, y1 + uy * s * 0.8, x2 - ux * s * 0.8, y2 - uy * s * 0.8, c, w, "butt")
            + head(x2, y2, ux, uy, c, s) + head(x1, y1, -ux, -uy, c, s))


def mid_head(x1, y1, x2, y2, c, s=22):
    """an arrowhead at the middle of a ray segment, pointing from (x1,y1) to (x2,y2)."""
    mx, my = (x1 + x2) / 2.0, (y1 + y2) / 2.0
    dx, dy = x2 - x1, y2 - y1; n = math.hypot(dx, dy)
    return head(mx + dx / n * s / 2, my + dy / n * s / 2, dx, dy, c, s)


def ray(pts, c=RED, w=4.5):
    """a ray: a solid polyline with a direction arrowhead on the middle of every segment."""
    out = poly_line(pts, c, w)
    for (a, b) in zip(pts, pts[1:]):
        out += mid_head(a[0], a[1], b[0], b[1], c)
    return out


def leader(x1, y1, x2, y2):
    return line(x1, y1, x2, y2, INK, 2.5) + circ(x2, y2, 4.5, INK, INK, 1)


def arc(cx, cy, r, a0, a1, c=INK, w=3):
    """arc of radius r about (cx,cy) from angle a0 to a1 (degrees, 0 = +x, measured clockwise on screen)."""
    p0 = (cx + r * math.cos(math.radians(a0)), cy + r * math.sin(math.radians(a0)))
    p1 = (cx + r * math.cos(math.radians(a1)), cy + r * math.sin(math.radians(a1)))
    large = 1 if abs(a1 - a0) > 180 else 0
    sweep = 1 if a1 > a0 else 0
    # path commands are limited to M L H V C Q Z: approximate the arc with a polyline
    n = 24
    pts = [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * k / n)), cy + r * math.sin(math.radians(a0 + (a1 - a0) * k / n)))
           for k in range(n + 1)]
    del p0, p1, large, sweep
    return poly_line(pts, c, w)


def sine(x0, x1, ym, amp, lam, phase=0.0, step=4):
    pts = []
    x = x0
    while x <= x1 + 0.01:
        pts.append((x, ym - amp * math.sin(2 * math.pi * (x - x0) / lam + phase)))
        x += step
    return pts


# ------------------------------------------------------------------ 1
def transverse_wave():
    W, H = 720, 360
    ym, amp, lam, x0, x1 = 150, 72, 240, 40, 520
    b = [poly_line(sine(x0, x1, ym, amp, lam), BLUE, 5)]
    # one point on the wave, and its oscillation at 90° to the travel
    b.append(darrow(x1, ym - amp - 6, x1, ym + amp + 6, RUST, 4.5, 22))
    b.append(circ(x1, ym, 9, RUST, RUST, 2))
    b.append(txt(546, ym + 10, "oscillation", FS, "start"))
    # direction of travel
    b.append(arrow(70, 290, 500, 290, INK, 5, 26))
    b.append(txt(285, 338, "direction of travel"))
    return svg(W, H, "A transverse wave drawn along a horizontal line. A long arrow below it points along the line, labelled direction of travel. At one point on the wave a short double-headed arrow points up and down, at right angles to the direction of travel, labelled oscillation.", b)


# ------------------------------------------------------------------ 2
def longitudinal_wave():
    W, H = 720, 450
    lam, A, d0 = 320.0, 24.0, 16.0
    xs = []
    xe = 40.0
    while xe <= 680:
        xs.append(xe + A * math.sin(2 * math.pi * (xe - 40) / lam))
        xe += d0
    b = []
    top, bot = 100, 188
    for x in xs:
        b.append(line(x, top, x, bot, BLUE, 4, "round"))
    # the lines bunch where x_e - 40 = lam/2 (compression) and spread where x_e - 40 = lam (rarefaction)
    comp = 40 + lam / 2          # 200
    rare = 40 + lam              # 360
    b.append(txt(comp, 54, "compression"))
    b.append(leader(comp, 64, comp, top - 6))
    b.append(txt(rare, 252, "rarefaction"))
    b.append(leader(rare, 222, rare, bot + 6))
    # oscillation: parallel to the travel
    b.append(darrow(60, 312, 170, 312, RUST, 4.5, 20))
    b.append(txt(190, 322, "oscillation", FS, "start"))
    # direction of travel
    b.append(arrow(80, 372, 640, 372, INK, 5, 26))
    b.append(txt(360, 420, "direction of travel"))
    return svg(W, H, "A longitudinal wave drawn as a row of vertical lines, like the coils of a stretched spring. Where the lines are bunched close together is labelled compression; where they are spread apart is labelled rarefaction. A short double-headed arrow pointing left and right is labelled oscillation, parallel to a long arrow labelled direction of travel.", b)


# ------------------------------------------------------------------ 3
def wave_amplitude_wavelength():
    W, H = 720, 500
    ax, ay_top, ay_bot = 96, 40, 450      # axes: displacement up the left, distance along the bottom
    ym, amp, lam, x0 = 250, 110, 260, ax
    b = []
    b.append(arrow(ax, ay_bot, ax, ay_top, INK, 4, 22))
    b.append(arrow(ax, ay_bot, 690, ay_bot, INK, 4, 22))
    b.append('<text x="60" y="%s" font-family="%s" font-size="27" font-weight="600" text-anchor="middle" fill="%s" transform="rotate(-90 60 %s)">displacement</text>' % (f(ym), FONT, INK, f(ym)))
    b.append(txt(690, 488, "distance", FS, "end"))
    # undisturbed position (displacement zero)
    b.append(line(ax, ym, 700, ym, GREY, 3, "butt", "12 9"))
    b.append(lines(704, ym - 52, ["undisturbed", "position"], 27, "end", GREY, 600, 32))
    # the wave: starts at the undisturbed position, peaks at x0 + lam/4
    b.append(poly_line(sine(x0, x0 + 1.75 * lam, ym, amp, lam), BLUE, 5))
    p1 = x0 + lam / 4.0; p2 = p1 + lam
    # amplitude: from the undisturbed line up to a peak
    b.append(darrow(p1, ym - 4, p1, ym - amp + 4, RUST, 4, 18))
    b.append(txt(p1 + lam / 2, ym - 44, "amplitude", FS, "middle", RUST, 600))
    b.append(leader(p1 + lam / 2 - 72, ym - 54, p1 + 6, ym - amp / 2))
    # wavelength: peak to next peak
    yw = ym - amp - 22
    b.append(line(p1, ym - amp - 6, p1, yw - 10, INK, 2.5, "butt"))
    b.append(line(p2, ym - amp - 6, p2, yw - 10, INK, 2.5, "butt"))
    b.append(darrow(p1, yw, p2, yw, INK, 4, 18))
    b.append(txt((p1 + p2) / 2, yw - 14, "wavelength", FS, "middle", INK, 700))
    # a second wavelength between two equivalent points that are not peaks (two troughs)
    t1 = x0 + 0.75 * lam; t2 = t1 + lam
    yt = ym + amp + 24
    b.append(line(t1, ym + amp + 6, t1, yt + 10, INK, 2.5, "butt"))
    b.append(line(t2, ym + amp + 6, t2, yt + 10, INK, 2.5, "butt"))
    b.append(darrow(t1, yt, t2, yt, INK, 4, 18))
    b.append(txt((t1 + t2) / 2, yt + 40, "wavelength", FS, "middle", INK, 700))
    return svg(W, H, "A graph of displacement against distance for a wave. A dashed horizontal line through the middle is the undisturbed position. A double arrow from that line up to a peak is labelled amplitude. A double arrow from one peak to the next is labelled wavelength, and a second double arrow from one trough to the next is also labelled wavelength.", b)


# ------------------------------------------------------------------ 4
def refraction_ray_diagram():
    W, H = 720, 560
    ox, oy = 360, 280
    i_deg, r_deg = 50.0, 30.7          # glass n = 1.5: sin r = sin 50° / 1.5
    b = [rect(0, oy, W, H - oy, GLASS, GLASS, 1)]
    b.append(line(0, oy, W, oy, INK, 4, "butt"))
    b.append(txt(24, oy - 24, "air", FS, "start"))
    b.append(txt(24, oy + 50, "glass", FS, "start"))
    # dashed normal at 90° to the boundary
    b.append(line(ox, 40, ox, 520, INK, 3, "butt", "12 9"))
    b.append(txt(ox + 12, 34, "normal", FS, "start"))
    L1, L2 = 250, 250
    ix = ox - L1 * math.sin(math.radians(i_deg)); iy = oy - L1 * math.cos(math.radians(i_deg))
    rx = ox + L2 * math.sin(math.radians(r_deg)); ry = oy + L2 * math.cos(math.radians(r_deg))
    b.append(ray([(ix, iy), (ox, oy), (rx, ry)], RED, 5))
    # angle of incidence: between incident ray and normal (air side)
    b.append(arc(ox, oy, 70, -90 - i_deg, -90, INK, 3))
    b.append(txt(ox + 40, oy - 112, "angle of", 27, "start"))
    b.append(txt(ox + 40, oy - 80, "incidence", 27, "start"))
    b.append(leader(ox + 36, oy - 92, ox - 30, oy - 66))
    # angle of refraction: between refracted ray and normal (glass side)
    b.append(arc(ox, oy, 80, 90 - r_deg, 90, INK, 3))
    b.append(txt(ox - 40, oy + 160, "angle of", 27, "end"))
    b.append(txt(ox - 40, oy + 192, "refraction", 27, "end"))
    b.append(leader(ox - 36, oy + 150, ox + 16, oy + 82))
    b.append(txt(ix - 6, iy - 16, "incident ray", 27, "start"))
    b.append(txt(rx - 10, ry + 34, "refracted ray", 27, "middle"))
    return svg(W, H, "A ray diagram. Air is above a horizontal boundary and glass is below it. A ray with an arrow travels down through the air to a point on the boundary. A dashed line through that point at 90 degrees to the boundary is labelled normal. In the glass the refracted ray bends towards the normal. The angle of incidence is marked between the incident ray and the normal, and the angle of refraction between the refracted ray and the normal.", b)


# ------------------------------------------------------------------ 5
def leslie_cube():
    W, H = 720, 560
    cx, cy, s = 230, 270, 220
    x0, y0, x1, y1 = cx - s / 2, cy - s / 2, cx + s / 2, cy + s / 2
    b = [txt(cx, 40, "seen from above", 27, "middle", GREY, 600)]
    b.append(rect(x0, y0, s, s, "#F4EFE6", INK, 3))
    b.append(lines(cx, cy - 4, ["hot", "water"], FS, "middle", INK, 600, 34))
    # the four faces, drawn as thick edges with their surface named outside
    b.append(line(x0, y0, x1, y0, INK, 12, "butt"))            # top: matt black
    b.append(txt(cx, y0 - 20, "matt black", FS))
    b.append(line(x0, y0, x0, y1, "#3A3A3A", 12, "butt"))      # left: shiny black
    b.append(line(x0 - 3, y0 + 30, x0 - 3, y1 - 30, "#9A9A9A", 2.6, "butt"))
    b.append(txt(x0 - 14, cy - 4, "shiny", FS, "end"))
    b.append(txt(x0 - 14, cy + 30, "black", FS, "end"))
    b.append(line(x0, y1, x1, y1, "#B5B5B5", 12, "butt"))      # bottom: matt white (outlined)
    b.append(line(x0, y1 + 7, x1, y1 + 7, INK, 2.6, "butt"))
    b.append(line(x0, y1 - 7, x1, y1 - 7, INK, 2.6, "butt"))
    b.append(txt(cx, y1 + 48, "matt white", FS))
    b.append(line(x1, y0, x1, y1, "#C9CED6", 12, "butt"))      # right: shiny silver
    b.append(line(x1 + 2, y0 + 30, x1 + 2, y1 - 30, "#FFFFFF", 2.6, "butt"))
    b.append(txt(x1 + 18, y0 + 24, "shiny", FS, "start"))
    b.append(txt(x1 + 18, y0 + 58, "silver", FS, "start"))
    # infrared detector facing the right face
    dx = 560
    b.append(rect(dx, cy - 50, 90, 100, "#F4EFE6", INK, 4, 8))
    b.append(lines(dx + 45, cy - 120, ["infrared", "detector"], FS, "middle", INK, 600, 34))
    b.append(leader(dx + 45, cy - 78, dx + 45, cy - 54))
    # same distance from every face
    b.append(line(x1 + 8, cy, dx - 4, cy, RUST, 3.5, "butt", "12 9"))
    b.append(line(x1 + 8, cy - 14, x1 + 8, cy + 14, RUST, 3, "butt"))
    b.append(line(dx - 4, cy - 14, dx - 4, cy + 14, RUST, 3, "butt"))
    b.append(lines((x1 + dx) / 2, cy + 50, ["same", "distance"], FS, "middle", RUST, 700, 34))
    return svg(W, H, "A Leslie cube seen from above: a square box of hot water whose four faces are matt black, shiny black, matt white and shiny silver. An infrared detector faces one face, with a dashed line showing it is placed the same distance from each face in turn.", b)


# ------------------------------------------------------------------ 6
def wave_fronts():
    W, H = 720, 400
    xs = [140, 230, 320, 410, 500]
    b = []
    for x in xs:
        b.append(line(x, 70, x, 300, BLUE, 5, "round"))
    b.append(txt(xs[2], 40, "wave front", FS, "middle", BLUE, 700))
    b.append(line(xs[2], 50, xs[2], 66, BLUE, 2.6, "butt"))
    # direction of travel at 90° to the fronts
    b.append(arrow(520, 185, 690, 185, INK, 5, 26))
    b.append(lines(605, 116, ["direction", "of travel"], FS, "middle", INK, 600, 32))
    # wavelength between two neighbouring fronts
    b.append(darrow(xs[0], 345, xs[1], 345, RUST, 4, 18))
    b.append(txt((xs[0] + xs[1]) / 2 + 60, 352, "wavelength", FS, "start", RUST, 700))
    b.append(line(xs[0], 304, xs[0], 360, RUST, 2.6, "butt"))
    b.append(line(xs[1], 304, xs[1], 360, RUST, 2.6, "butt"))
    return svg(W, H, "Five parallel straight lines, one labelled wave front. An arrow at 90 degrees to the lines is labelled direction of travel. A double arrow between two neighbouring lines is labelled wavelength.", b)


# ------------------------------------------------------------------ 7
def wavefront_refraction():
    W, H = 720, 620
    ox, oy = 330, 300
    i_deg = 45.0
    r_deg = math.degrees(math.asin(math.sin(math.radians(i_deg)) / 1.5))   # 28.1°: towards the normal
    si, ci = math.sin(math.radians(i_deg)), math.cos(math.radians(i_deg))
    sr, cr = math.sin(math.radians(r_deg)), math.cos(math.radians(r_deg))
    lam1 = 58.0
    lam2 = lam1 * sr / si                     # same frequency, slower: shorter wavelength
    wb = 230.0                                # beam width in air
    wb2 = wb * cr / ci                        # beam width in glass
    t1 = (ci, -si)                            # along a front, in air (towards upper right)
    t2 = (cr, -sr)                            # along a front, in glass
    b = [rect(0, oy, W, H - oy, GLASS, GLASS, 1)]
    b.append(line(0, oy, W, oy, INK, 4, "butt"))
    b.append(txt(712, oy - 18, "air (faster)", FS, "end"))
    b.append(txt(712, 598, "glass (slower)", FS, "end"))
    segs = []
    for k in range(-7, 7):
        Bx = k * lam1 / si                    # where front k meets the boundary (relative to O)
        # air part: B + s t1, s >= 0, inside the beam: |t1.B + s| <= wb/2, and not too far back
        if -k * lam1 <= 250:
            o = Bx * t1[0]
            s0, s1 = max(0.0, -wb / 2 - o), wb / 2 - o
            if s1 > s0 + 1:
                segs.append(((ox + Bx + s0 * t1[0], oy + s0 * t1[1]), (ox + Bx + s1 * t1[0], oy + s1 * t1[1])))
        # glass part: B - s t2, s >= 0, inside the beam: |t2.B - s| <= wb2/2
        if k * lam2 <= 230:
            o = Bx * t2[0]
            s0, s1 = max(0.0, o - wb2 / 2), o + wb2 / 2
            if s1 > s0 + 1:
                segs.append(((ox + Bx - s0 * t2[0], oy - s0 * t2[1]), (ox + Bx - s1 * t2[0], oy - s1 * t2[1])))
    for (a, c) in segs:
        b.append(line(a[0], a[1], c[0], c[1], BLUE, 4.5, "round"))
    # dashed normal at the centre ray
    b.append(line(ox, 50, ox, 590, INK, 3, "butt", "12 9"))
    b.append(txt(ox + 12, 44, "normal", FS, "start"))
    # centre ray at 90° to the fronts, above and below: bent towards the normal
    L = 270
    ax_, ay_ = ox - L * si, oy - L * ci
    gx, gy = ox + 250 * sr, oy + 250 * cr
    b.append(ray([(ax_, ay_), (ox, oy), (gx, gy)], RED, 4.5))
    # label one wave front in air
    # label the highest wave front in the air, beside its upper end
    top_end = min((pt for seg in segs for pt in seg if pt[1] < oy), key=lambda q: q[1])
    b.append(txt(top_end[0] - 12, top_end[1] + 4, "wave front", FS, "end", BLUE, 700))
    b.append(lines(560, 470, ["fronts closer", "together"], 27, "middle", INK, 600, 32))
    return svg(W, H, "A wave front diagram. Air, where waves are faster, is above a horizontal boundary; glass, where they are slower, is below. Straight wave fronts arrive at the boundary at an angle. In the glass the wave fronts are closer together and turned. A ray drawn at 90 degrees to the wave fronts bends towards the dashed normal as it crosses into the glass.", b)


# ------------------------------------------------------------------ 8
def earth_radiation_balance():
    W, H = 720, 700
    b = []
    gy = 600                                   # top of the Earth's surface
    b.append(rect(0, gy, W, H - gy, GROUND, GROUND, 1))
    b.append(line(0, gy, W, gy, INK, 3, "butt"))
    b.append(rect(160, gy, 200, H - gy, "#FFFFFF", INK, 3))
    b.append(txt(260, gy + 58, "ice and snow", 27))
    b.append(txt(560, gy + 58, "Earth's surface", 27))
    # atmosphere band
    b.append(line(0, 220, W, 220, GREY, 3, "butt", "12 9"))
    b.append(line(0, 300, W, 300, GREY, 3, "butt", "12 9"))
    b.append(txt(575, 270, "atmosphere", 27, "middle", GREY, 600))
    # Sun
    b.append(circ(70, 64, 40, SUNC, AMBER, 4))
    b.append(txt(140, 74, "Sun", FS, "start"))
    # sunlight absorbed by the surface
    b.append(arrow(62, 110, 34, gy - 4, AMBER, 5, 24))
    b.append(txt(58, 460, "absorbed", 27, "start"))
    # sunlight onto ice and snow, reflected back up into space
    b.append(arrow(96, 100, 232, gy - 4, AMBER, 5, 24))
    b.append(arrow(252, gy - 4, 318, 24, AMBER, 5, 24))
    b.append(lines(196, 150, ["reflected", "into space"], 27, "start", INK, 600, 32))
    # infrared emitted by the surface, out into space
    b.append(arrow(380, gy - 4, 380, 24, RED, 5, 24))
    b.append(lines(396, 44, ["infrared emitted", "into space"], 27, "start", INK, 600, 32))
    # infrared absorbed by the atmosphere, and emitted back towards the surface
    b.append(arrow(450, gy - 4, 450, 262, RED, 5, 24))
    b.append(lines(466, 360, ["absorbed by", "the atmosphere"], 27, "start", INK, 600, 32))
    b.append(arrow(700, 262, 700, gy - 4, RED, 5, 24))
    b.append(lines(680, 480, ["emitted back", "towards", "the surface"], 27, "end", INK, 600, 32))
    return svg(W, H, "The Earth's radiation balance. Radiation from the Sun, top left, travels down. Some is absorbed by the Earth's surface. Some reaches ice and snow and is reflected back into space. The surface emits infrared: some goes up through the atmosphere into space, some is absorbed by the atmosphere, and the atmosphere emits some back towards the surface.", b)


# ------------------------------------------------------------------ 9
def concave_lens_image():
    W, H = 720, 470
    LX, AY = 430, 260                          # lens centre on the principal axis
    U = 22.0                                   # px per cm
    X = lambda cm: LX + cm * U
    Y = lambda cm: AY - cm * U
    F = 10.0; u = 15.0; h0 = 6.0
    v = -1.0 / (1.0 / F + 1.0 / u)             # concave, f = -10: image 6 cm in front of the lens
    hi = h0 * (-v) / u                          # upright, diminished
    b = []
    b.append(line(10, AY, 710, AY, INK, 2.6, "butt", "12 9"))
    b.append(txt(710, AY - 14, "principal axis", 27, "end", GREY, 600))
    # AQA concave lens symbol: a line with arrowheads pointing inwards at both ends
    top, bot = Y(8.2), Y(-7.6)
    b.append(line(LX, top, LX, bot, INK, 4.5, "butt"))
    b.append(poly_line([(LX - 15, top - 16), (LX, top), (LX + 15, top - 16)], INK, 4.5))
    b.append(poly_line([(LX - 15, bot + 16), (LX, bot), (LX + 15, bot + 16)], INK, 4.5))
    b.append(txt(LX, top - 34, "concave lens", 27))
    for cm in (-F, F):
        b.append(circ(X(cm), AY, 7, INK, INK, 1))
        b.append(txt(X(cm), AY + 38, "F", FS, "middle", INK, 700))
    # object: upright arrow beyond F on the left
    b.append(arrow(X(-u), AY, X(-u), Y(h0), BLUE, 5, 22))
    b.append(txt(X(-u), Y(h0) - 14, "object", 27, "middle", BLUE, 700))
    tip = (X(-u), Y(h0))
    # ray 1: parallel to the axis, then diverges as if from F on the object side
    slope = h0 / F                             # rises h0 over F after the lens (away from the axis)
    y_end = 10.6                               # stop the ray inside the canvas
    ex = LX + (y_end - h0) / slope * U
    b.append(ray([tip, (LX, Y(h0)), (ex, Y(y_end))], RED, 4))
    ex = 704
    b.append(line(X(-F), AY, LX, Y(h0), RED, 2.8, "butt", "10 8"))
    # ray 2: straight through the centre of the lens
    k = (ex - tip[0])
    y2 = h0 + (0 - h0) * (ex - tip[0]) / (LX - tip[0])
    b.append(ray([tip, (ex, Y(y2))], GREEN, 4))
    # image: dashed upright arrow between F and the lens, where the dashed line meets ray 2
    ix = X(v)
    b.append(line(ix, AY, ix, Y(hi) + 18, RUST, 4.5, "butt", "9 7"))
    b.append(head(ix, Y(hi), 0, -1, RUST, 20))
    b.append(lines(ix + 8, AY + 66, ["image", "(virtual)"], 27, "middle", RUST, 700, 30))
    del k
    return svg(W, H, "A concave lens, drawn with the AQA symbol: a line with arrowheads pointing inwards. A dashed principal axis has F marked on both sides. An upright object stands beyond F on the left. One ray travels parallel to the axis and spreads out after the lens; a dashed line traces it back to F on the object side. A second ray passes straight through the centre of the lens. A dashed upright arrow between F and the lens, smaller than the object, is labelled image (virtual).", b)

# ------------------------------------------------------------------ 10 (added 14 Nov 2026)
def _cross(x, y, s=10, c=INK):
    return line(x - s, y - s, x + s, y + s, c, 3.5) + line(x - s, y + s, x + s, y - s, c, 3.5)


def reflection_ray_diagram():
    """Plane mirror, normal dashed at 90 degrees, angle of incidence = angle of reflection = 40
    degrees, both measured from the normal (reflection-of-waves, required-practical-light)."""
    W, H = 720, 470
    ox, oy, i_deg, L = 360, 370, 40.0, 270
    b = []
    for x in range(84, 650, 26):                       # hatching on the back of the mirror
        b.append(line(x, oy + 2, x - 16, oy + 24, GREY, 2.6, "butt"))
    b.append(line(70, oy, 650, oy, INK, 5, "butt"))
    b.append(line(ox, 70, ox, oy, INK, 3, "butt", "12 9"))
    b.append(txt(ox + 12, 62, "normal", FS, "start"))
    sx = ox - L * math.sin(math.radians(i_deg)); sy = oy - L * math.cos(math.radians(i_deg))
    ex = ox + L * math.sin(math.radians(i_deg)); ey = sy
    b.append(ray([(sx, sy), (ox, oy), (ex, ey)], RED, 5))
    b.append(arc(ox, oy, 78, -90 - i_deg, -90, INK, 3))
    b.append(arc(ox, oy, 92, -90, -90 + i_deg, INK, 3))
    a1 = math.radians(-90 - i_deg / 2); a2 = math.radians(-90 + i_deg / 2)
    b.append(lines(250, 300, ["angle of", "incidence"], 27, "end", INK, 600, 32))
    b.append(leader(256, 306, ox + 78 * math.cos(a1), oy + 78 * math.sin(a1)))
    b.append(lines(470, 300, ["angle of", "reflection"], 27, "start", INK, 600, 32))
    b.append(leader(464, 306, ox + 92 * math.cos(a2), oy + 92 * math.sin(a2)))
    b.append(txt(sx, sy - 24, "incident ray", 27, "middle"))
    b.append(txt(ex, ey - 24, "reflected ray", 27, "middle"))
    b.append(txt(612, 438, "mirror", FS, "middle"))
    return svg(W, H, "A ray diagram for reflection. A plane mirror is a horizontal line, shaded on its back. A ray with an arrow travels down to a point on the mirror. A dashed line through that point at 90 degrees to the mirror is labelled normal. The reflected ray, with an arrow, leaves on the other side of the normal. The angle of incidence, between the incident ray and the normal, is the same size as the angle of reflection, between the reflected ray and the normal.", b)


# ------------------------------------------------------------------ 11 (added 14 Nov 2026)
def rp_glass_block():
    """Top view of Required practical activity 9, refraction part: ray box, rectangular glass
    block drawn round on paper, dashed normal, i = 40 degrees, r = 25.4 degrees (sin r = sin 40 /
    1.5), the ray leaving parallel to the way it went in, and crosses marking the rays."""
    W, H = 720, 580
    bx0, by0, bx1, by1 = 150, 220, 570, 420
    px, py, i_deg = 290, by0, 40.0
    r_deg = math.degrees(math.asin(math.sin(math.radians(i_deg)) / 1.5))
    dx, dy = math.sin(math.radians(i_deg)), math.cos(math.radians(i_deg))
    b = [rect(bx0, by0, bx1 - bx0, by1 - by0, GLASS, INK, 3)]
    sx, sy = px - 170 * dx, py - 170 * dy
    qx, qy = px + (by1 - by0) * math.tan(math.radians(r_deg)), by1
    ex, ey = qx + 150 * dx, qy + 150 * dy
    # ray box: a grey box behind the start of the ray, lined up with it (no text on it)
    nx, ny = -dy * 20, dx * 20
    kx, ky = sx - 80 * dx, sy - 80 * dy
    b.append(poly([(sx + nx, sy + ny), (sx - nx, sy - ny), (kx - nx, ky - ny), (kx + nx, ky + ny)], GREY, INK, 3))
    b.append(txt(124, 100, "ray box", 27, "end"))
    b.append(line(px, 60, px, 340, INK, 3, "butt", "12 9"))
    b.append(txt(px + 12, 56, "normal", FS, "start"))
    b.append(ray([(sx, sy), (px, py), (qx, qy), (ex, ey)], RED, 5))
    for t in (40, 120):
        b.append(_cross(px - t * dx, py - t * dy))
    for t in (50, 120):
        b.append(_cross(qx + t * dx, qy + t * dy))
    b.append(arc(px, py, 70, -90 - i_deg, -90, INK, 3))
    b.append(arc(px, py, 80, 90 - r_deg, 90, INK, 3))
    a1 = math.radians(-90 - i_deg / 2); a2 = math.radians(90 - r_deg / 2)
    b.append(lines(312, 150, ["angle of", "incidence"], 27, "start", INK, 600, 32))
    b.append(leader(308, 160, px + 70 * math.cos(a1), py + 70 * math.sin(a1)))
    b.append(lines(420, 300, ["angle of", "refraction"], 27, "start", INK, 600, 32))
    b.append(leader(414, 308, px + 80 * math.cos(a2), py + 80 * math.sin(a2)))
    b.append(txt(166, 404, "glass block", 27, "start"))
    b.append(lines(500, 458, ["two crosses", "mark the ray"], 27, "start", INK, 600, 32))
    b.append(leader(494, 480, qx + 120 * dx + 8, qy + 120 * dy - 8))
    return svg(W, H, "A view from above of a rectangular glass block on a sheet of paper. A narrow ray from a ray box meets the top side of the block. A dashed normal is drawn at 90 degrees to that side. Inside the block the ray bends towards the normal: the angle of refraction is smaller than the angle of incidence. The ray leaves the opposite side travelling parallel to the way it went in. Two crosses mark the ray going in and two mark the ray coming out.", b)


# ------------------------------------------------------------------ 12 (added 14 Nov 2026)
def _reflect(d, theta_deg):
    """reflect direction d off a facet at screen angle theta (degrees, + = descending to the right)."""
    th = math.radians(theta_deg)
    n = (math.sin(th), -math.cos(th))                    # the facet's normal, pointing up
    k = d[0] * n[0] + d[1] * n[1]
    return (d[0] - 2 * k * n[0], d[1] - 2 * k * n[1])


def specular_diffuse():
    """Left: a smooth surface; three parallel rays (i = 40 degrees) reflect parallel. Right: a rough
    surface of facets; the same parallel rays meet facets at different angles, and each reflects
    with angle of incidence = angle of reflection about its own facet's normal, so they scatter."""
    W, H = 720, 420
    SY = 290
    PALE = "#EDE6DA"
    i_deg = 40.0
    d = (math.sin(math.radians(i_deg)), math.cos(math.radians(i_deg)))
    b = [line(360, 24, 360, 400, GREY, 2.6, "butt", "8 8")]
    b.append(rect(30, SY, 300, 40, PALE, PALE, 1))
    b.append(line(30, SY, 330, SY, INK, 5, "butt"))
    for hx in (110, 180, 250):
        sx, sy = hx - 150 * d[0], SY - 150 * d[1]
        ex, ey = hx + 150 * d[0], SY - 150 * d[1]
        b.append(ray([(sx, sy), (hx, SY), (ex, ey)], RED, 4.5))
    # rough surface: a facet at each hit point, tilted a different way (screen angle, + =
    # descending to the right), joined by short slopes. Each ray reflects about its own facet's
    # normal (local angles of incidence 21, 32 and 43 degrees), so the three parallel rays leave
    # at 88, 66 and 44 degrees above the horizontal: up, up-right, and further right. The
    # leftmost leaves furthest left, so no ray crosses another (every gap is 30+ units), and none
    # grazes the surface (each leaves at 45 degrees or more to its own facet).
    hits = [(438, -19.0), (525, -8.0), (640, 3.0)]
    LIN, LOUT = 78, 88
    pts = [(392.0, SY + 4.0)]
    for k, (hx, th) in enumerate(hits):
        c, sn = math.cos(math.radians(th)) * 16, math.sin(math.radians(th)) * 16
        pts += [(hx - c, SY - sn), (hx + c, SY + sn)]
        if k == 0:
            pts.append((482.0, SY + 10.0))
        elif k == 1:
            pts.append((588.0, SY + 9.0))
    pts += [(668.0, SY - 7.0), (700.0, SY + 4.0)]
    b.append(poly(pts + [(700, SY + 40), (392, SY + 40)], PALE, PALE, 1))
    b.append(poly_line(pts, INK, 5))
    outs = []
    for hx, th in hits:
        rd = _reflect(d, th)
        n = (math.sin(math.radians(th)), -math.cos(math.radians(th)))
        assert rd[0] * n[0] + rd[1] * n[1] > 0.7, rd     # leaves at 45 deg or more to its facet
        assert rd[1] < -0.6, rd                          # every reflected ray leaves well upwards
        ex, ey = hx + LOUT * rd[0], SY + LOUT * rd[1]
        assert 375 < ex < 712 and hx - LIN * d[0] > 375, (hx, ex)
        outs.append(math.degrees(math.atan2(-rd[1], rd[0])))
        b.append(ray([(hx - LIN * d[0], SY - LIN * d[1]), (hx, SY), (ex, ey)], RED, 4.5))
    assert outs[0] > outs[1] + 20 and outs[1] > outs[2] + 20, outs   # clearly different, fanning out
    b.append(txt(180, 362, "smooth surface", 27, "middle"))
    b.append(txt(180, 398, "specular reflection", 27, "middle", INK, 700))
    b.append(txt(540, 362, "rough surface", 27, "middle"))
    b.append(txt(540, 398, "diffuse reflection", 27, "middle", INK, 700))
    return svg(W, H, "Two surfaces side by side. On the left, three parallel rays with arrows meet a smooth flat surface and are reflected in a single direction, still parallel: specular reflection. On the right, three parallel rays meet a rough surface made of tiny slopes facing different ways, and are reflected in different directions: the light is scattered. This is diffuse reflection.", b)


REGISTRY = {
    "transverse-wave": transverse_wave,
    "longitudinal-wave": longitudinal_wave,
    "wave-amplitude-wavelength": wave_amplitude_wavelength,
    "refraction-ray-diagram": refraction_ray_diagram,
    "leslie-cube": leslie_cube,
    "wave-fronts": wave_fronts,
    "wavefront-refraction": wavefront_refraction,
    "earth-radiation-balance": earth_radiation_balance,
    "concave-lens-image": concave_lens_image,
    # added 14 Nov 2026
    "reflection-ray-diagram": reflection_ray_diagram,
    "rp-glass-block": rp_glass_block,
    "specular-diffuse": specular_diffuse,
}
