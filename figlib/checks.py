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
 6. Georgia first in every font stack — or exactly `style.NUM_FONT`, the
    lining-figure serif for a label that carries a number. ⊕ fix round 1
    (visual M3): Georgia's old-style digits made "0" a small "o" at 11px
    on the chart labels a pupil reads values from. The rule was widened by
    that ONE named, all-serif stack (which the worksheet maps to the same
    DejaVu Serif as Georgia) and nothing else. ⊕ fix round 2 (visual n1):
    the stack gained Noto Serif before the generic, so Android and Chrome
    OS (no Times) still land on lining figures.
 7. NUMERALS CLEAR THE CARD EDGE. Every unrotated numeral label (one set
    in NUM_FONT) keeps >= NUM_EDGE_CLEAR units from the left and right
    edges of the canvas, measured at the WIDEST face the stack can fall
    back to (`style.num_width_wide`) — so an end-of-axis tick like "180"
    cannot touch or clip the card on a device without Times.
 8. EVERY LABEL'S WHOLE BOX IS ON THE CARD AND CLEAR OF EVERY OTHER LABEL.
    ⊕ MRB-352 run 2, batch-2 fix round (visual review, recommended check).
    Rule 7 covers only unrotated numerals, and `_text_samples()` only five
    interior points — so nothing checked that a rotated axis title stays on
    the canvas or clears the tick numerals beside it. For EVERY <text>,
    rotated or not, the box is the label at the WIDEST face its stack can
    fall back to (`num_width_wide` for NUM_FONT, the Georgia table x 1.15
    for DejaVu Serif otherwise) by the line box (0.92 em above the
    baseline, 0.24 em below — Chrome's measured box), rotated with the
    label's rotate(a cx cy). It fails within TEXT_EDGE_CLEAR units of any
    canvas edge, and it fails when two labels' boxes, each padded by
    TEXT_GAP / 2, intersect — naming both. ONE precise exemption, not a
    loosening: consecutive lines of one wrapped label (same x, anchor,
    size, weight, fill and rotation; baselines between STACK_PITCH em
    apart) are one block of type, so their own line boxes may abut —
    every line is still checked against every OTHER label and the edge.
    Lines closer than STACK_PITCH[0] em still fail. ⊕ fix round 2: the
    two lines must also be ADJACENT in document order, the second directly
    after the first and below it — which is how every builder emits a
    wrapped label — so two SEPARATE labels that merely share a style and
    sit about 1 em apart are not exempt.
"""

import math
import re
import xml.etree.ElementTree as ET

from .style import (GEORGIA_WIDE, MIN_STROKE_PX, MIN_TEXT_PX, NUM_FONT,
                    num_width_wide, screen_scale, text_width)

_Q = "{http://www.w3.org/2000/svg}"

MIN_CONTRAST = 4.5
NUM_EDGE_CLEAR = 6           # rule 7: units between a numeral and the edge
TEXT_EDGE_CLEAR = 4          # rule 8: units between any label box and the edge
TEXT_GAP = 3                 # rule 8: minimum units between two label boxes
STACK_PITCH = (1.05, 1.6)    # rule 8: em between baselines of one wrapped label
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


def _text_box(el, label, size, fam):
    """Rule 8: the label's line box at its widest fallback face, rotated
    with the label, as (x0, y0, x1, y1) plus whether it was rotated."""
    bold = el.get("font-weight") in ("bold", "700")
    w = (num_width_wide(label, size, bold) if fam == NUM_FONT
         else text_width(label, size, bold) * GEORGIA_WIDE)
    x, y = float(el.get("x", 0)), float(el.get("y", 0))
    anchor = el.get("text-anchor", "start")
    x0 = x - (w / 2 if anchor == "middle" else w if anchor == "end" else 0)
    corners = [(x0, y - 0.92 * size), (x0 + w, y - 0.92 * size),
               (x0, y + 0.24 * size), (x0 + w, y + 0.24 * size)]
    m = _ROTATE.match(el.get("transform", "") or "")
    if m:
        a = math.radians(float(m.group(1)))
        cx, cy = float(m.group(2)), float(m.group(3))
        corners = [(cx + (px - cx) * math.cos(a) - (py - cy) * math.sin(a),
                    cy + (px - cx) * math.sin(a) + (py - cy) * math.cos(a))
                   for px, py in corners]
    return (min(p[0] for p in corners), min(p[1] for p in corners),
            max(p[0] for p in corners), max(p[1] for p in corners)), bool(m)


def _stack_key(el, size):
    """Rule 8: what two lines of ONE wrapped label share, plus baseline."""
    return ((el.get("x"), el.get("text-anchor", "start"), size,
             el.get("font-weight"), el.get("fill"),
             (el.get("transform") or "").split(" ")[0]),
            float(el.get("y", 0)), size)


def _one_block(ka, kb):
    """Rule 8: the next line of one wrapped label (the caller also requires
    the two to be adjacent in document order) — same x, anchor,
    size, weight, fill and angle, unrotated, baselines STACK_PITCH em
    apart. Nothing else is exempt."""
    (sa, ya, za), (sb, yb, _) = ka, kb
    if sa != sb or sa[5]:
        return False
    return STACK_PITCH[0] * za - 1e-6 <= yb - ya <= STACK_PITCH[1] * za


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
    boxes = []                  # rule 8: (label, padded box) per <text>

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
        if not fam.startswith("Georgia") and fam != NUM_FONT:
            probs.append("%s: text %r font-family %r does not start with "
                         "Georgia (nor is it the lining-figure stack %r)"
                         % (fid, label, fam, NUM_FONT))
        fill = el.get("fill")
        if fill in (None, "none"):
            probs.append("%s: text %r has no fill" % (fid, label))
            continue
        size = float(el.get("font-size", 16))
        if fam == NUM_FONT and not el.get("transform"):
            tw = num_width_wide(label, size,
                                el.get("font-weight") in ("bold", "700"))
            tx = float(el.get("x", 0))
            anchor = el.get("text-anchor", "start")
            x_l = tx - (tw if anchor == "end" else
                        tw / 2 if anchor == "middle" else 0)
            x_r = x_l + tw
            if x_l < NUM_EDGE_CLEAR - 1e-6 or x_r > W - NUM_EDGE_CLEAR + 1e-6:
                probs.append("%s: numeral %r spans x %.1f–%.1f in its widest "
                             "fallback face — under %g units from the card "
                             "edge (canvas 0–%g)" % (fid, label, x_l, x_r,
                                                      NUM_EDGE_CLEAR, W))
        # rule 8: the whole (rotated) box on the card, 4 units in
        (bx0, by0, bx1, by1), rot = _text_box(el, label, size, fam)
        e = TEXT_EDGE_CLEAR - 1e-6
        if bx0 < vb[0] + e or by0 < vb[1] + e or \
                bx1 > vb[0] + W - e or by1 > vb[1] + vb[3] - e:
            probs.append("%s: text %r box %.1f,%.1f–%.1f,%.1f (%s, widest "
                         "fallback face) is under %g units from the canvas "
                         "edge (viewBox %s)" % (
                             fid, label, bx0, by0, bx1, by1,
                             "rotated" if rot else "flat", TEXT_EDGE_CLEAR,
                             " ".join("%g" % v for v in vb)))
        g = TEXT_GAP / 2.0
        boxes.append((label, (bx0 - g, by0 - g, bx1 + g, by1 + g),
                      _stack_key(el, size)))
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
    # rule 8: no two padded label boxes intersect
    for i in range(len(boxes)):
        la, (ax0, ay0, ax1, ay1), ka = boxes[i]
        for j in range(i + 1, len(boxes)):
            lb, (cx0, cy0, cx1, cy1), kb = boxes[j]
            if j == i + 1 and _one_block(ka, kb):
                continue
            if min(ax1, cx1) > max(ax0, cx0) and min(ay1, cy1) > max(ay0, cy0):
                probs.append("%s: text %r and text %r overlap (their boxes at "
                             "the widest fallback face, each padded %g units, "
                             "intersect)" % (fid, la, lb, TEXT_GAP / 2.0))
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


# ── rule 8 proves itself on every build ──────────────────────────────────

_ST_SVG = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200">'
           '<rect data-role="paper" x="0" y="0" width="200" height="200" '
           'fill="#FBF7EE" stroke="none"/>%s</svg>')
_ST_TEXT = ('<text x="%s" y="%s" font-family="Georgia, serif" font-size="17" '
            'font-weight="700" fill="#2E5E45" text-anchor="middle"%s>%s</text>')


def self_test():
    """Rule 8 against drawings whose verdict is known. Returns a list of
    problems (empty = the rule behaves). `build_figures.py` runs it before
    the manifest, so the figure_manifest gate fails if the rule is ever
    weakened or broken."""
    T = _ST_TEXT
    rot = ' transform="rotate(-90 %s %s)"'
    cases = [
        # (name, body, must_fail)
        ("rotated label off the left edge",
         T % (8, 100, rot % (8, 100), "energy"), True),
        ("rotated label clear of the edge",
         T % (21, 100, rot % (21, 100), "energy"), False),
        ("two overlapping labels",
         T % (100, 100, "", "alpha") + T % (110, 108, "", "beta"), True),
        ("two lines of one wrapped label, adjacent, 21 units apart",
         T % (100, 100, "", "alpha") + T % (100, 121, "", "beta"), False),
        ("two lines of one wrapped label packed too tight (14 units)",
         T % (100, 100, "", "alpha") + T % (100, 114, "", "beta"), True),
        # ⊕ fix round 2: the same two same-style lines, 21 units apart, but
        # NOT adjacent in document order — a separate label sits between
        # them — are two separate labels, and must not be exempt.
        ("two separate same-style labels ~1 em apart, not adjacent",
         T % (100, 100, "", "alpha") + T % (40, 180, "", "x")
         + T % (100, 121, "", "beta"), True),
        # ...nor when the second is drawn ABOVE the first.
        ("same-style labels ~1 em apart, second drawn above the first",
         T % (100, 121, "", "beta") + T % (100, 100, "", "alpha"), True),
    ]
    out = []
    for name, body, must_fail in cases:
        failed = any("overlap" in p or " box " in p
                     for p in check_figure("self-test", _ST_SVG % body))
        if failed != must_fail:
            out.append("figlib.checks self-test: %r should %s rule 8 but "
                       "did%s" % (name, "fail" if must_fail else "pass",
                                  "n't" if must_fail else " not"))
    return out


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
