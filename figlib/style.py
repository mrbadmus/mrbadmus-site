"""figlib.style — the LOCKED style core, shared by every figlib module.

Moved here verbatim from the library's chem_diagrams.py (see figlib/README.md
for provenance), so physics, chemistry and biology import ONE Canvas and ONE
STYLE instead of each other. Two deliberate changes, both recorded in the
README: `cairosvg` is imported lazily inside `export()` only (the site build
never rasterises and must not need it), and nothing else.
"""

import math
import os

# ====================================================================
# LOCKED STYLE CORE  (inherited by every diagram — never re-styled)
# ====================================================================
STYLE = {
    "cream":   "#F3F0E7",   # paper background
    "label":   "#2E5E45",   # element/diagram labels (dark sage)
    "stroke":  "#1A1A1A",   # shells, outlines (hand-drawn near-black)
    "electron":"#2E5E45",   # electrons (dots & crosses)
    "h_fill":  "#F2C9AE",   # hydrogen / metal-ion nucleus (salmon)
    "nm_fill": "#A9D9BE",   # non-metal nucleus (mint)
    "arrow":   "#2E8B7F",   # transfer / process arrow (teal)
    "bracket": "#A9D9BE",   # decorative bracket accents
    "muted":   "#5B6B82",   # captions, weak-force dashed lines
    "font":    "Georgia, serif",
    "shell_w": 2,
    "elec_r":  6.5,
    "cross_s": 7,
    "cross_w": 3.4,
}

# ====================================================================
# PRIMITIVES  (built once — reused by every builder forever)
# ====================================================================
class Canvas:
    def __init__(self, w, h):
        self.w, self.h, self.S = w, h, []
        self.S.append(
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
            f'viewBox="0 0 {w} {h}">')
        self.S.append(f'<rect width="{w}" height="{h}" fill="{STYLE["cream"]}"/>')

    def label(self, x, y, txt, size=34, weight="normal", anchor="middle"):
        txt = (str(txt).replace("&", "&amp;")
                       .replace("<", "&lt;").replace(">", "&gt;"))
        self.S.append(
            f'<text x="{x}" y="{y}" font-family="{STYLE["font"]}" '
            f'font-size="{size}" font-weight="{weight}" fill="{STYLE["label"]}" '
            f'text-anchor="{anchor}">{txt}</text>')

    def shell(self, cx, cy, r):
        self.S.append(
            f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" '
            f'stroke="{STYLE["stroke"]}" stroke-width="{STYLE["shell_w"]}"/>')

    def nucleus(self, cx, cy, txt, fill, r=30):
        self.S.append(
            f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" '
            f'stroke="{STYLE["stroke"]}" stroke-width="2"/>')
        self.S.append(
            f'<text x="{cx}" y="{cy+r*0.32}" font-family="{STYLE["font"]}" '
            f'font-size="{r*0.95:.0f}" fill="{STYLE["label"]}" '
            f'text-anchor="middle" font-weight="bold">{txt}</text>')

    def dot(self, x, y):
        self.S.append(
            f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{STYLE["elec_r"]}" '
            f'fill="{STYLE["electron"]}"/>')

    def cross(self, x, y):
        s = STYLE["cross_s"]
        self.S.append(
            f'<g stroke="{STYLE["electron"]}" stroke-width="{STYLE["cross_w"]}" '
            f'stroke-linecap="round">'
            f'<line x1="{x-s:.1f}" y1="{y-s:.1f}" x2="{x+s:.1f}" y2="{y+s:.1f}"/>'
            f'<line x1="{x-s:.1f}" y1="{y+s:.1f}" x2="{x+s:.1f}" y2="{y-s:.1f}"/></g>')

    def arrow(self, x1, y1, x2, y2):
        self.S.append(
            f'<g stroke="{STYLE["arrow"]}" stroke-width="9" fill="none" '
            f'stroke-linecap="round"><line x1="{x1}" y1="{y1}" x2="{x2}" '
            f'y2="{y2}"/></g>')
        a = math.atan2(y2-y1, x2-x1)
        for da in (math.radians(150), math.radians(-150)):
            self.S.append(
                f'<line x1="{x2}" y1="{y2}" x2="{x2+22*math.cos(a+da):.1f}" '
                f'y2="{y2+22*math.sin(a+da):.1f}" stroke="{STYLE["arrow"]}" '
                f'stroke-width="9" stroke-linecap="round"/>')

    def bracket(self, x, y_top, y_bot, side, scale=1.0):
        d = 22*scale
        if side == "L":
            self.S.append(
                f'<path d="M{x} {y_top} q{-d} 0 {-d} {d} L{x-d} {y_bot-d} '
                f'q0 {d} {d} {d}" stroke="{STYLE["bracket"]}" stroke-width="6" '
                f'fill="none" stroke-linecap="round"/>')
        else:
            self.S.append(
                f'<path d="M{x} {y_top} q{d} 0 {d} {d} L{x+d} {y_bot-d} '
                f'q0 {d} {-d} {d}" stroke="{STYLE["bracket"]}" stroke-width="6" '
                f'fill="none" stroke-linecap="round"/>')

    def svg(self):
        return "\n".join(self.S + ["</svg>"])


def _pol(cx, cy, r, deg):
    a = math.radians(deg)
    return cx + r*math.cos(a), cy + r*math.sin(a)


# ====================================================================
# EXPORT  — one SVG master → PowerPoint / website / PDF
# ====================================================================
def _cairosvg():
    """Imported on first use, never at module load: `cairosvg` is a desktop
    export dependency (PowerPoint/PDF PNGs) and the site build, which only
    ever emits SVG, must run on a machine that does not have it."""
    import cairosvg
    return cairosvg


def export(svg, name, outdir="output", formats=("png", "svg", "pdfpng")):
    os.makedirs(outdir, exist_ok=True)
    paths = {}
    if "svg" in formats:
        p = os.path.join(outdir, f"{name}.svg")
        open(p, "w").write(svg); paths["svg"] = p
    if "png" in formats:                       # PowerPoint (2000px)
        p = os.path.join(outdir, f"{name}.png")
        _cairosvg().svg2png(bytestring=svg.encode(), write_to=p, output_width=2000)
        paths["png"] = p
    if "pdfpng" in formats:                    # ReportLab embed (300dpi-ish)
        p = os.path.join(outdir, f"{name}@3x.png")
        _cairosvg().svg2png(bytestring=svg.encode(), write_to=p, output_width=3000)
        paths["pdfpng"] = p
    return paths


# ====================================================================
# FIGLIB ADDITIONS — question-figure (phone) layout helpers
#
# Everything above this banner is the library's own style core, moved
# verbatim. Everything below is new, and exists for one reason: the
# library draws for a projector and a printed A4 sheet (canvases 900-1400
# wide, 22px labels), and a question figure is read on a phone. Drawn
# 1300 wide and shrunk into a 320px column, a 22px label lands at 5px.
# So a question figure uses a NARROW canvas, and its text size is derived
# from the canvas width rather than typed — `q_font(W)` is the smallest
# size that is still >= 11 CSS px once the figure is scaled into a
# 320px-wide box, the floor `figlib.checks` enforces.
# ====================================================================
PHONE_BOX = 320          # CSS px: the narrowest box a question figure gets
MIN_TEXT_PX = 11.0       # smallest on-screen label, after scaling
MIN_STROKE_PX = 1.0      # thinnest on-screen line, after scaling

MUTED = STYLE["muted"]   # #5B6B82 — 4.8:1 on cream, legal for a label
RED = "#C8102E"          # the library's exam red — 5.1:1 on cream
AMBER = "#E0892E"        # the library's amber — NEVER a text colour (2.6:1)

# Light tints that keep dark-sage text >= 4.5:1 (checked by figlib.checks,
# not assumed): every box a label sits in is PAPER, never a dark fill.
TINT = {
    "mint":   "#CFEBDB",
    "sand":   "#EDE5D0",
    "salmon": "#F7DCCB",
    "blue":   "#D6E4F5",
    "lilac":  "#E4DDF0",
    "white":  "#FFFFFF",
}


def screen_scale(W):
    """How much a W-wide canvas is scaled in the narrowest box: a canvas
    wider than the box shrinks to fit it; a narrower one is drawn 1:1
    (consumers cap a figure at its own width, never stretch it)."""
    return PHONE_BOX / float(W) if W > PHONE_BOX else 1.0


def q_font(W, floor=15):
    """The label size for a W-wide question canvas: >= 11 CSS px on
    screen at 320px, with a little headroom, never below `floor`."""
    need = MIN_TEXT_PX / screen_scale(W)
    return max(floor, int(math.ceil(need + 0.3)))


def q_stroke(W, want=2.0):
    """A stroke width that stays >= 1 CSS px on screen at 320px."""
    need = MIN_STROKE_PX / screen_scale(W)
    return round(max(want, need * 1.05), 2)


# Georgia's advance widths, in ems, MEASURED (headless Chrome,
# getComputedTextLength at 100px, macOS Georgia, 24 Sep 2026) rather than
# guessed — a guess 8% short let "Attract weakly" run out of its table
# cell. Used for LAYOUT (sizing a box to its label, wrapping a line) and by
# the checks to find what a label sits on; never to decide legibility —
# font size does that. An unmeasured glyph counts as a wide capital.
_ADV = {
    " ": 0.241, "!": 0.331, "\"": 0.412, "#": 0.643, "$": 0.610, "%": 0.817,
    "&": 0.710, "'": 0.215, "(": 0.375, ")": 0.375, "*": 0.472, "+": 0.643,
    ",": 0.270, "-": 0.374, ".": 0.270, "/": 0.469, "0": 0.614, "1": 0.430,
    "2": 0.559, "3": 0.552, "4": 0.565, "5": 0.528, "6": 0.566, "7": 0.502,
    "8": 0.596, "9": 0.566, ":": 0.312, ";": 0.312, "<": 0.643, "=": 0.643,
    ">": 0.643, "?": 0.479, "@": 0.929, "A": 0.671, "B": 0.654, "C": 0.642,
    "D": 0.749, "E": 0.653, "F": 0.599, "G": 0.725, "H": 0.815, "I": 0.390,
    "J": 0.518, "K": 0.694, "L": 0.604, "M": 0.927, "N": 0.767, "O": 0.744,
    "P": 0.610, "Q": 0.744, "R": 0.702, "S": 0.561, "T": 0.619, "U": 0.756,
    "V": 0.667, "W": 0.976, "X": 0.710, "Y": 0.615, "Z": 0.602, "[": 0.375,
    "\\": 0.469, "]": 0.375, "^": 0.643, "_": 0.643, "`": 0.500, "a": 0.504,
    "b": 0.560, "c": 0.454, "d": 0.574, "e": 0.483, "f": 0.325, "g": 0.509,
    "h": 0.582, "i": 0.293, "j": 0.292, "k": 0.536, "l": 0.286, "m": 0.881,
    "n": 0.591, "o": 0.539, "p": 0.571, "q": 0.560, "r": 0.410, "s": 0.432,
    "t": 0.345, "u": 0.575, "v": 0.497, "w": 0.737, "x": 0.505, "y": 0.492,
    "z": 0.444, "{": 0.430, "|": 0.375, "}": 0.430, "~": 0.643, "°": 0.419,
    "²": 0.500, "³": 0.500, "·": 0.279, "×": 0.643, "Δ": 0.661, "Ω": 0.779,
    "θ": 0.556, "μ": 0.579, "–": 0.643, "—": 0.857, "₂": 0.500, "₃": 0.500,
    "→": 1.000, "≈": 0.643,
}
_ADV_BOLD = {
    " ": 0.254, "!": 0.376, "\"": 0.510, "#": 0.703, "$": 0.641, "%": 0.879,
    "&": 0.799, "'": 0.269, "(": 0.447, ")": 0.447, "*": 0.482, "+": 0.703,
    ",": 0.328, "-": 0.379, ".": 0.328, "/": 0.472, "0": 0.701, "1": 0.490,
    "2": 0.626, "3": 0.625, "4": 0.649, "5": 0.599, "6": 0.648, "7": 0.554,
    "8": 0.676, "9": 0.648, ":": 0.367, ";": 0.367, "<": 0.703, "=": 0.703,
    ">": 0.703, "?": 0.548, "@": 0.967, "A": 0.758, "B": 0.757, "C": 0.715,
    "D": 0.834, "E": 0.721, "F": 0.671, "G": 0.807, "H": 0.913, "I": 0.446,
    "J": 0.595, "K": 0.817, "L": 0.686, "M": 1.023, "N": 0.839, "O": 0.820,
    "P": 0.701, "Q": 0.820, "R": 0.797, "S": 0.649, "T": 0.684, "U": 0.834,
    "V": 0.762, "W": 1.126, "X": 0.809, "Y": 0.732, "Z": 0.689, "[": 0.447,
    "\\": 0.472, "]": 0.447, "^": 0.703, "_": 0.703, "`": 0.500, "a": 0.596,
    "b": 0.646, "c": 0.531, "d": 0.663, "e": 0.572, "f": 0.393, "g": 0.577,
    "h": 0.680, "i": 0.354, "j": 0.346, "k": 0.632, "l": 0.344, "m": 1.016,
    "n": 0.690, "o": 0.636, "p": 0.658, "q": 0.648, "r": 0.520, "s": 0.513,
    "t": 0.397, "u": 0.677, "v": 0.567, "w": 0.863, "x": 0.588, "y": 0.562,
    "z": 0.525, "{": 0.500, "|": 0.388, "}": 0.500, "~": 0.703, "°": 0.420,
    "²": 0.552, "³": 0.552, "·": 0.338, "×": 0.703, "Δ": 0.739, "Ω": 0.875,
    "θ": 0.640, "μ": 0.670, "–": 0.703, "—": 0.928, "₂": 0.552, "₃": 0.552,
    "→": 1.000, "≈": 0.703,
}


def text_width(s, size, bold=False):
    table = _ADV_BOLD if bold else _ADV
    return sum(table.get(ch, 1.08 if bold else 0.95) for ch in str(s)) * size


def wrap(s, size, max_w, bold=False):
    """Greedy word wrap to `max_w` user units."""
    lines, cur = [], ""
    for word in str(s).split():
        trial = (cur + " " + word).strip()
        if cur and text_width(trial, size, bold) > max_w:
            lines.append(cur)
            cur = word
        else:
            cur = trial
    if cur:
        lines.append(cur)
    return lines


def esc(txt):
    return (str(txt).replace("&", "&amp;")
                    .replace("<", "&lt;").replace(">", "&gt;"))


def text(c, x, y, txt, size, fill=None, weight="bold", anchor="middle",
         rotate=None):
    """One label, in the house font, painted by attribute (never a class)."""
    fill = fill or STYLE["label"]
    tr = (' transform="rotate(%s %.1f %.1f)"' % (rotate, x, y)
          if rotate is not None else "")
    c.S.append(
        f'<text x="{x:.1f}" y="{y:.1f}" font-family="{STYLE["font"]}" '
        f'font-size="{size}" font-weight="{weight}" fill="{fill}" '
        f'text-anchor="{anchor}"{tr}>{esc(txt)}</text>')


def line(c, x1, y1, x2, y2, stroke=None, width=3, dash=None, cap="round"):
    stroke = stroke or STYLE["stroke"]
    d = f' stroke-dasharray="{dash}"' if dash else ""
    c.S.append(
        f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
        f'stroke="{stroke}" stroke-width="{width}" stroke-linecap="{cap}"{d}/>')


def box(c, x, y, w, h, fill="none", stroke=None, width=2, rx=0, dash=None):
    stroke = stroke or STYLE["stroke"]
    r = f' rx="{rx}"' if rx else ""
    d = f' stroke-dasharray="{dash}"' if dash else ""
    c.S.append(
        f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}"{r} '
        f'fill="{fill}" stroke="{stroke}" stroke-width="{width}"{d}/>')


def arrow(c, x1, y1, x2, y2, col=None, width=3, head=14):
    """A line with a solid triangular head at (x2, y2) — a polygon, never
    an SVG <marker>, so every renderer (browser, PDFKit, resvg) draws the
    same head with no marker maths."""
    col = col or STYLE["arrow"]
    ang = math.atan2(y2 - y1, x2 - x1)
    bx, by = x2 - head * math.cos(ang), y2 - head * math.sin(ang)
    nx, ny = -math.sin(ang) * head * 0.5, math.cos(ang) * head * 0.5
    line(c, x1, y1, bx, by, col, width)
    c.S.append(
        f'<polygon points="{x2:.1f},{y2:.1f} {bx+nx:.1f},{by+ny:.1f} '
        f'{bx-nx:.1f},{by-ny:.1f}" fill="{col}" stroke="none"/>')
