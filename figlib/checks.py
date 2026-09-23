"""figlib.checks — what every manifest figure must satisfy, as hard failures.

`build_figures.py` runs `check_figure()` on every figure it is about to
write and refuses to write ANY of them if one fails. These are gates, not
warnings, because every one of them is a defect a pupil sees:

 1. SELF-PAINTING (figure-contract §8). No `class=`, no `style=`, no `var(`.
    Every shape names its own fill (and a line its own stroke) as an
    attribute. The four surfaces that drew a figure as a black disc, an
    invisible outline or a blank PNG all failed the same way: the paint
    lived in a stylesheet the surface did not have.
 2. A SMALL, NAMED ELEMENT SET — the subset the worksheet translator
    (backend `figure-render.js`) has to understand, and nothing else: no
    groups, no defs, no markers, no gradients, no filters, no opacity, no
    arcs. Colours are `#hex` or `none`.
 3. CONTRAST. Every <text> is >= 4.5:1 (WCAG AA) against the fill it
    actually sits on — found geometrically, topmost filled shape under the
    glyphs — and no text sits on a DARK fill at all.
 4. LEGIBLE AT 360px. Scaled into a 320 CSS-px box, every label is >= 11px
    and every stroke >= 1px.
 5. AQA SYMBOLS ONLY. No motor (a circled M) and no "d.c." box: neither is
    on the AQA 8463 §4.2.1.1 list.
 6. Georgia first in every font stack.
"""

import math
import re
import xml.etree.ElementTree as ET

from .style import (MIN_STROKE_PX, MIN_TEXT_PX, screen_scale, text_width)

_Q = "{http://www.w3.org/2000/svg}"

MIN_CONTRAST = 4.5
DARK_LUMINANCE = 0.18        # a fill darker than this carries no text at all

PAINT = {"fill", "stroke", "stroke-width", "stroke-linecap",
         "stroke-linejoin", "stroke-dasharray"}
ALLOWED = {
    "svg":      {"viewBox", "role", "aria-labelledby", "preserveAspectRatio"},
    "title":    {"id"},
    "desc":     {"id"},
    "rect":     {"x", "y", "width", "height", "rx", "data-role"} | PAINT,
    "circle":   {"cx", "cy", "r"} | PAINT,
    "ellipse":  {"cx", "cy", "rx", "ry"} | PAINT,
    "line":     {"x1", "y1", "x2", "y2"} | PAINT,
    "polyline": {"points"} | PAINT,
    "polygon":  {"points"} | PAINT,
    "path":     {"d"} | PAINT,
    "text":     {"x", "y", "font-family", "font-size", "font-weight",
                 "text-anchor", "fill", "transform"},
}
SHAPES = {"rect", "circle", "ellipse", "polygon", "path", "polyline"}
_HEX = re.compile(r"^#[0-9A-Fa-f]{6}$|^#[0-9A-Fa-f]{3}$")
_PATH_CMDS = set("MmLlHhVvCcQqZz")
_ROTATE = re.compile(r"^rotate\(\s*(-?[\d.]+)[\s,]+(-?[\d.]+)[\s,]+(-?[\d.]+)\s*\)$")
_NUMBER = re.compile(r"^-?\d+(\.\d+)?$")


# ── colour ────────────────────────────────────────────────────────────────

def _rgb(hexs):
    h = hexs.lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    return tuple(int(h[i:i + 2], 16) / 255.0 for i in (0, 2, 4))


def luminance(hexs):
    def lin(c):
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (lin(c) for c in _rgb(hexs))
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast(a, b):
    la, lb = sorted((luminance(a), luminance(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


# ── geometry ──────────────────────────────────────────────────────────────

def _nums(s):
    return [float(v) for v in re.findall(r"-?\d*\.?\d+(?:e-?\d+)?", s or "")]


def _pts(s):
    v = _nums(s)
    return list(zip(v[0::2], v[1::2]))


def _path_pts(d):
    """The vertices (end and control points) of a path, absolute. For a
    backdrop test the control hull is a safe over-approximation."""
    toks = re.findall(r"[A-Za-z]|-?\d*\.?\d+(?:e-?\d+)?", d)
    out, x, y, sx, sy, cmd, i = [], 0.0, 0.0, 0.0, 0.0, None, 0
    arity = {"M": 2, "L": 2, "H": 1, "V": 1, "C": 6, "Q": 4, "Z": 0}
    while i < len(toks):
        t = toks[i]
        if t.isalpha():
            cmd = t
            i += 1
            if cmd in "Zz":
                x, y = sx, sy
                continue
        n = arity[cmd.upper()]
        args = [float(v) for v in toks[i:i + n]]
        i += n
        rel = cmd.islower()
        C = cmd.upper()
        if C == "H":
            x = x + args[0] if rel else args[0]
        elif C == "V":
            y = y + args[0] if rel else args[0]
        else:
            ps = list(zip(args[0::2], args[1::2]))
            if rel:
                ps = [(x + a, y + b) for a, b in ps]
            out.extend(ps[:-1])
            x, y = ps[-1]
        out.append((x, y))
        if C == "M":
            sx, sy = x, y
            cmd = "l" if rel else "L"
    return out


def _in_poly(px, py, poly):
    inside, n = False, len(poly)
    for k in range(n):
        x1, y1 = poly[k]
        x2, y2 = poly[(k + 1) % n]
        if (y1 > py) != (y2 > py):
            xi = x1 + (py - y1) * (x2 - x1) / (y2 - y1)
            if px < xi:
                inside = not inside
    return inside


def _contains(el, px, py):
    tag = el.tag[len(_Q):]
    g = lambda k, d=0.0: float(el.get(k, d))  # noqa: E731
    if tag == "rect":
        return g("x") <= px <= g("x") + g("width") and \
            g("y") <= py <= g("y") + g("height")
    if tag == "circle":
        return (px - g("cx")) ** 2 + (py - g("cy")) ** 2 <= g("r") ** 2
    if tag == "ellipse":
        rx, ry = g("rx"), g("ry")
        return rx > 0 and ry > 0 and \
            ((px - g("cx")) / rx) ** 2 + ((py - g("cy")) / ry) ** 2 <= 1
    if tag in ("polygon", "polyline"):
        return _in_poly(px, py, _pts(el.get("points")))
    if tag == "path":
        pts = _path_pts(el.get("d", ""))
        return len(pts) >= 3 and _in_poly(px, py, pts)
    return False


def _text_samples(el, size):
    """Five points inside the label's glyph box, rotated with the label."""
    x, y = float(el.get("x", 0)), float(el.get("y", 0))
    s = "".join(el.itertext())
    w = text_width(s, size, el.get("font-weight") in ("bold", "700"))
    anchor = el.get("text-anchor", "start")
    x0 = x - (w / 2 if anchor == "middle" else w if anchor == "end" else 0)
    top, bot = y - 0.70 * size, y - 0.05 * size
    pts = [(x0 + w * fx, top + (bot - top) * fy)
           for fx, fy in ((0.5, 0.5), (0.12, 0.25), (0.88, 0.25),
                          (0.12, 0.85), (0.88, 0.85))]
    m = _ROTATE.match(el.get("transform", "") or "")
    if m:
        a = math.radians(float(m.group(1)))
        cx = float(m.group(2) or 0)
        cy = float(m.group(3) or 0)
        pts = [(cx + (px - cx) * math.cos(a) - (py - cy) * math.sin(a),
                cy + (px - cx) * math.sin(a) + (py - cy) * math.cos(a))
               for px, py in pts]
    return pts


# ── the check ─────────────────────────────────────────────────────────────

def check_figure(fid, svg):
    """Every problem with one manifest figure, as strings. Empty = clean."""
    probs = []
    for bad, why in (("class=", "a class= (paint from a stylesheet)"),
                     ("style=", "a style= attribute"),
                     ("var(", "a CSS var()")):
        if bad in svg:
            probs.append("%s: carries %s — a manifest figure paints itself "
                         "with attributes, nothing else" % (fid, why))
    try:
        root = ET.fromstring(svg)
    except ET.ParseError as exc:
        return probs + ["%s: not well-formed XML (%s)" % (fid, exc)]

    vb = _nums(root.get("viewBox"))
    if len(vb) != 4:
        return probs + ["%s: <svg> has no viewBox" % fid]
    W = vb[2]
    scale = screen_scale(W)

    filled = []                 # paint-ordered shapes that can sit under text
    circles = []
    for el in root.iter():
        tag = el.tag[len(_Q):] if el.tag.startswith(_Q) else el.tag
        if tag not in ALLOWED:
            probs.append("%s: <%s> is not in the manifest's element set "
                         "(%s)" % (fid, tag, ", ".join(sorted(ALLOWED))))
            continue
        extra = set(el.attrib) - ALLOWED[tag]
        if extra:
            probs.append("%s: <%s> carries attribute(s) outside the set: %s"
                         % (fid, tag, ", ".join(sorted(extra))))
        for k in ("fill", "stroke"):
            v = el.get(k)
            if v is not None and v != "none" and not _HEX.match(v):
                probs.append("%s: <%s %s=%r> — colours are #hex or none"
                             % (fid, tag, k, v))
        if tag == "path":
            bad = set(re.findall(r"[A-Za-z]", el.get("d", ""))) - _PATH_CMDS
            if bad:
                probs.append("%s: <path> uses command(s) %s — only M L H V "
                             "C Q Z are in the set" % (fid, "".join(sorted(bad))))
        if el.get("transform") is not None and (
                tag != "text" or not _ROTATE.match(el.get("transform"))):
            probs.append("%s: <%s transform=%r> — the only transform in the "
                         "set is rotate(a cx cy) on a <text>"
                         % (fid, tag, el.get("transform")))
        for k in ("font-size", "font-weight", "stroke-width", "rx"):
            v = el.get(k)
            if v is not None and not _NUMBER.match(v):
                probs.append("%s: <%s %s=%r> — a bare number, no unit and no "
                             "name (the worksheet's PDF path reads numbers)"
                             % (fid, tag, k, v))
        if tag == "rect" and el.get("data-role") not in (None, "paper"):
            probs.append("%s: data-role=%r — only 'paper'" % (fid,
                                                               el.get("data-role")))
        if tag == "polyline" and el.get("fill") not in (None, "none"):
            probs.append("%s: a filled <polyline> — use a polygon" % fid)

        # self-painting: nothing may rely on a UA default colour
        if tag in SHAPES:
            if el.get("fill") is None:
                probs.append("%s: <%s> has no fill attribute, so it would "
                             "paint in the SVG default (black) — the black-"
                             "disc bug" % (fid, tag))
            if el.get("fill") == "none" and el.get("stroke") in (None, "none"):
                probs.append("%s: <%s> has no fill and no stroke — it draws "
                             "nothing" % (fid, tag))
        if tag in ("line", "polyline") and el.get("fill") is None:
            probs.append("%s: <%s> states no fill — every shape states its "
                         "fill, even an open one (fill=\"none\")" % (fid, tag))
        if tag == "line" and el.get("stroke") in (None, "none"):
            probs.append("%s: <line> has no stroke — it draws nothing" % fid)
        # legibility: strokes
        if tag in SHAPES | {"line"} and el.get("stroke") not in (None, "none"):
            sw = float(el.get("stroke-width", 1))
            if sw * scale < MIN_STROKE_PX - 1e-6:
                probs.append("%s: a <%s> stroke is %.2fpx on screen at 320px "
                             "(stroke-width %s on a %g-wide canvas) — under "
                             "%gpx" % (fid, tag, sw * scale,
                                       el.get("stroke-width", 1), W,
                                       MIN_STROKE_PX))
        if tag in SHAPES and el.get("fill") not in (None, "none"):
            filled.append(el)
        if tag == "circle":
            circles.append(el)

        if tag != "text":
            continue
        label = "".join(el.itertext()).strip()
        fam = el.get("font-family", "")
        if not fam.startswith("Georgia"):
            probs.append("%s: text %r font-family %r does not start with "
                         "Georgia" % (fid, label, fam))
        fill = el.get("fill")
        if fill in (None, "none"):
            probs.append("%s: text %r has no fill" % (fid, label))
            continue
        size = float(el.get("font-size", 16))
        if size * scale < MIN_TEXT_PX - 1e-6:
            probs.append("%s: text %r is %.1fpx on screen at 320px "
                         "(font-size %g on a %g-wide canvas) — under %gpx"
                         % (fid, label, size * scale, size, W, MIN_TEXT_PX))
        # contrast against what is actually underneath
        worst, worst_bg = None, None
        for px, py in _text_samples(el, size):
            under = next((s for s in reversed(filled)
                          if _contains(s, px, py)), None)
            bg = under.get("fill") if under is not None else None
            if bg is None:
                probs.append("%s: text %r is not on the paper card at all"
                             % (fid, label))
                break
            ratio = contrast(fill, bg)
            if worst is None or ratio < worst:
                worst, worst_bg = ratio, bg
            if luminance(bg) < DARK_LUMINANCE:
                probs.append("%s: text %r sits on a dark fill %s — no text "
                             "on a dark background, at all" % (fid, label, bg))
                break
        if worst is not None and worst < MIN_CONTRAST:
            probs.append("%s: text %r is %.2f:1 against %s — under %.1f:1 "
                         "(WCAG AA)" % (fid, label, worst, worst_bg,
                                        MIN_CONTRAST))
        # AQA: no motor, no d.c. box
        if label == "M":
            x, y = float(el.get("x", 0)), float(el.get("y", 0)) - size * 0.35
            for c in circles:
                if (x - float(c.get("cx"))) ** 2 + (y - float(c.get("cy"))) \
                        ** 2 <= float(c.get("r")) ** 2:
                    probs.append("%s: draws a circled M — the motor symbol "
                                 "is not on the AQA 8463 list" % fid)
                    break
        if label.lower().replace(" ", "") in ("d.c.", "dc", "d.c"):
            probs.append("%s: draws a 'd.c.' supply box — not on the AQA "
                         "8463 list" % fid)
    return probs


def check_paper(fid, svg):
    """The figure's first shape is its paper, marked for print renderers."""
    root = ET.fromstring(svg)
    shapes = [el for el in root if el.tag[len(_Q):] not in ("title", "desc")]
    papers = [el for el in root.iter() if el.get("data-role") == "paper"]
    if not shapes or shapes[0].get("data-role") != "paper" or len(papers) != 1:
        return ["%s: the first shape must be the one data-role=\"paper\" "
                "rect (the cream card)" % fid]
    return []


def check_manifest(manifest):
    """Every figure, plus the one cross-figure rule: no id attribute value
    appears in two figures (two figures on one page must never collide)."""
    probs, owner = [], {}
    for fid in sorted(manifest):
        svg = manifest[fid]["svg"]
        probs.extend(check_figure(fid, svg))
        probs.extend(check_paper(fid, svg))
        for idv in re.findall(r'\sid="([^"]+)"', svg):
            if idv in owner and owner[idv] != fid:
                probs.append("id %r appears in both %s and %s"
                             % (idv, owner[idv], fid))
            owner[idv] = fid
    return probs
