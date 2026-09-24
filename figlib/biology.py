"""
AQA GCSE Biology — schematic / data diagrams only.

Inherits STYLE, Canvas, export from chem_diagrams so the style core
is identical. Anatomical diagrams (heart, leaf, cell, etc.) are
deliberately NOT covered here — use textbook images for those.

Provides:
  punnett_square(parent_a, parent_b, ...)
  food_chain(organisms)
  pyramid_of_biomass(levels)
  biomass_flow(...)  -- reuses Sankey concept
  dna_schematic()
  mitosis_stages()
  reflex_arc()
  carbon_cycle_bio() / water_cycle() / nitrogen_cycle()
"""
import math
from .style import Canvas, STYLE, export
from .chemistry import _note  # noqa: F401

FONT = STYLE["font"]
LBL = STYLE["label"]
ST = STYLE["stroke"]
RED = "#C8102E"
ACC = STYLE["arrow"]
GREEN = STYLE["nm_fill"]
YELL = "#FBBF24"
AMB = "#E0892E"
BLUE = "#3B82F6"


def _clabel(c, x, y, txt, size=22, fill=None, weight="bold",
            anchor="middle"):
    txt = (str(txt).replace("&", "&amp;").replace("<", "&lt;")
                   .replace(">", "&gt;"))
    fill = fill or LBL
    c.S.append(
        f'<text x="{x:.1f}" y="{y:.1f}" font-family="{FONT}" '
        f'font-size="{size}" fill="{fill}" text-anchor="{anchor}" '
        f'font-weight="{weight}">{txt}</text>')


def _arrow(c, x1, y1, x2, y2, col=None, width=5):
    col = col or ACC
    c.S.append(
        f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" '
        f'stroke="{col}" stroke-width="{width}" stroke-linecap="round"/>')
    ang = math.atan2(y2-y1, x2-x1)
    ax = x2 - 18*math.cos(ang); ay = y2 - 18*math.sin(ang)
    nx, ny = -math.sin(ang)*11, math.cos(ang)*11
    c.S.append(
        f'<polygon points="{x2},{y2} {ax+nx:.1f},{ay+ny:.1f} '
        f'{ax-nx:.1f},{ay-ny:.1f}" fill="{col}"/>')


# ====================================================================
# 1) PUNNETT SQUARE
# ====================================================================
def punnett_square(parent_a="Bb", parent_b="Bb", trait="brown / blue eyes",
                   title=None):
    """2x2 Punnett square for two heterozygous (or any) parents.
    parent_a, parent_b : two-character genotype strings (e.g. 'Bb', 'BB')."""
    if len(parent_a) != 2 or len(parent_b) != 2:
        raise ValueError("genotypes must be 2 characters (e.g. 'Bb')")
    W, H = 1100, 760
    c = Canvas(W, H)
    _clabel(c, W/2, 56,
            title or f"Punnett square \u2014 {trait}", 36, weight="bold")

    # build the 4 offspring
    a1, a2 = parent_a[0], parent_a[1]
    b1, b2 = parent_b[0], parent_b[1]
    # 4 combinations
    cells = [
        a1+b1, a1+b2,
        a2+b1, a2+b2,
    ]
    # sort each pair so dominant (uppercase) comes first
    def sort_pair(p):
        if p[0].lower() == p[1].lower():
            # same letter — uppercase first
            if p[0].isupper(): return p
            return p[::-1]
        return p
    cells = [sort_pair(c2) for c2 in cells]

    # 3x3 grid: top-left blank, top row = parent A alleles, left col = parent B
    gx, gy = 250, 200
    cell = 180
    # outer border
    c.S.append(
        f'<rect x="{gx}" y="{gy}" width="{cell*3}" height="{cell*3}" '
        f'fill="none" stroke="{ST}" stroke-width="3"/>')
    # internal lines
    for k in (1, 2):
        c.S.append(
            f'<line x1="{gx+k*cell}" y1="{gy}" x2="{gx+k*cell}" '
            f'y2="{gy+3*cell}" stroke="{ST}" stroke-width="2"/>')
        c.S.append(
            f'<line x1="{gx}" y1="{gy+k*cell}" x2="{gx+3*cell}" '
            f'y2="{gy+k*cell}" stroke="{ST}" stroke-width="2"/>')

    # top header (parent A)
    _clabel(c, gx + cell + cell/2, gy - 30,
            f"Parent A ({parent_a})", 24, LBL, "bold")
    _clabel(c, gx + cell + cell/2, gy + cell*0.35,
            a1, 44, LBL, "bold")
    _clabel(c, gx + 2*cell + cell/2, gy + cell*0.35,
            a2, 44, LBL, "bold")

    # left header (parent B), rotated
    c.S.append(
        f'<text x="{gx - 60}" y="{gy + cell + cell/2}" '
        f'font-family="{FONT}" font-size="24" fill="{LBL}" '
        f'text-anchor="middle" font-weight="bold" '
        f'transform="rotate(-90 {gx-60} {gy + cell + cell/2})">'
        f'Parent B ({parent_b})</text>')
    _clabel(c, gx + cell*0.35, gy + cell + cell*0.65,
            b1, 44, LBL, "bold")
    _clabel(c, gx + cell*0.35, gy + 2*cell + cell*0.65,
            b2, 44, LBL, "bold")

    # offspring cells (bottom-right 2x2)
    for i, off in enumerate(cells):
        col = i % 2; row = i // 2
        cx = gx + (col+1)*cell + cell/2
        cy = gy + (row+1)*cell + cell/2
        # colour cells: homozygous dominant = green, heterozygous = yellow,
        # homozygous recessive = red-ish
        is_dom = off[0].isupper() and off[1].isupper()
        is_rec = off[0].islower() and off[1].islower()
        if is_dom:
            fill = GREEN
        elif is_rec:
            fill = "#E8B4B4"
        else:
            fill = YELL
        c.S.append(
            f'<rect x="{gx+(col+1)*cell+4}" y="{gy+(row+1)*cell+4}" '
            f'width="{cell-8}" height="{cell-8}" fill="{fill}" '
            f'opacity="0.55"/>')
        _clabel(c, cx, cy+15, off, 56, RED, "bold")

    # ratio summary in red
    dom_count = sum(1 for c2 in cells if "A" not in c2.lower()
                    and not c2.islower())
    counts = {"dom_dom": 0, "het": 0, "rec_rec": 0}
    for c2 in cells:
        if c2[0].isupper() and c2[1].isupper(): counts["dom_dom"] += 1
        elif c2[0].islower() and c2[1].islower(): counts["rec_rec"] += 1
        else: counts["het"] += 1
    ratio = (f"{counts['dom_dom']} : {counts['het']} : {counts['rec_rec']}"
             f"   (homozygous dominant : heterozygous : "
             f"homozygous recessive)")
    _clabel(c, W/2, H-60, ratio, 22, RED, "bold")
    _clabel(c, W/2, H-30,
            "Each offspring has equal probability of any combination.",
            20, LBL, "normal")
    return c.svg()


# ====================================================================
# 2) FOOD CHAIN
# ====================================================================
def food_chain(organisms=None):
    """A linear food chain with arrows showing energy flow.
    organisms : list of dicts {"name": ..., "role": "producer"/...}"""
    if organisms is None:
        organisms = [
            {"name": "Grass",   "role": "Producer"},
            {"name": "Rabbit",  "role": "Primary consumer"},
            {"name": "Fox",     "role": "Secondary consumer"},
            {"name": "Eagle",   "role": "Tertiary consumer"},
        ]
    n = len(organisms)
    W = max(1100, 220 + n * 270)
    H = 540
    c = Canvas(W, H)
    _clabel(c, W/2, 56, "Food chain \u2014 energy flow", 36, weight="bold")
    bw, bh = 220, 130
    by = 260
    gap = (W - 80 - bw*n) / (n - 1) if n > 1 else 0
    colours = [GREEN, YELL, AMB, "#C8102E", "#9333EA"]
    for i, org in enumerate(organisms):
        bx = 40 + i*(bw + gap)
        col = colours[min(i, len(colours)-1)]
        c.S.append(
            f'<rect x="{bx}" y="{by}" width="{bw}" height="{bh}" rx="14" '
            f'fill="{col}" opacity="0.6" stroke="{ST}" '
            f'stroke-width="2.5"/>')
        _clabel(c, bx+bw/2, by+bh/2-6, org["name"], 26, LBL, "bold")
        _clabel(c, bx+bw/2, by+bh/2+30, org["role"], 18, LBL, "normal")
        if i < n - 1:
            _arrow(c, bx+bw+8, by+bh/2,
                   bx+bw+gap-8, by+bh/2, ACC, 6)
            # "eaten by" caption above arrow
            _clabel(c, bx+bw+gap/2, by+bh/2-22, "eaten by",
                    18, ACC, "bold")
    _clabel(c, W/2, H-50,
            "Arrows show the direction of energy transfer.",
            22, RED, "bold")
    _clabel(c, W/2, H-22,
            "Only ~10% of energy passes to the next trophic level "
            "\u2014 the rest is lost as heat, movement, waste.",
            18, LBL, "normal")
    return c.svg()


# ====================================================================
# 3) PYRAMID OF BIOMASS
# ====================================================================
def pyramid_of_biomass(levels=None):
    """Stack of trapezoidal layers, each proportional to biomass."""
    if levels is None:
        levels = [
            {"name": "Producers (grass)",            "biomass": 1000},
            {"name": "Primary consumers (rabbits)",  "biomass": 100},
            {"name": "Secondary consumers (foxes)",  "biomass": 10},
            {"name": "Tertiary consumers (eagles)",  "biomass": 1},
        ]
    W, H = 1400, 760
    c = Canvas(W, H)
    _clabel(c, W/2, 56, "Pyramid of Biomass", 36, weight="bold")
    # max biomass sets the base width
    max_biomass = max(L["biomass"] for L in levels)
    base_w = 800
    layer_h = 100
    cx = W/2
    # draw bottom-up
    n = len(levels)
    by_bottom = 200 + n * layer_h
    colours = [GREEN, YELL, AMB, "#C8102E", "#9333EA"]
    # reverse so producers at bottom
    for i, L in enumerate(levels):
        w = base_w * (L["biomass"] / max_biomass) ** 0.5
        # scale via sqrt so even small layers visible
        ytop = by_bottom - (i+1) * layer_h
        ybot = by_bottom - i * layer_h
        col = colours[min(i, len(colours)-1)]
        # trapezoid: narrower at top
        next_w = base_w * (levels[i+1]["biomass"]/max_biomass) ** 0.5 \
                 if i+1 < n else 0
        pts = [(cx - w/2, ybot), (cx + w/2, ybot),
               (cx + next_w/2, ytop), (cx - next_w/2, ytop)]
        c.S.append(
            f'<polygon points="{pts[0][0]:.0f},{pts[0][1]} '
            f'{pts[1][0]:.0f},{pts[1][1]} '
            f'{pts[2][0]:.0f},{pts[2][1]} '
            f'{pts[3][0]:.0f},{pts[3][1]}" fill="{col}" opacity="0.7" '
            f'stroke="{ST}" stroke-width="2"/>')
        # label to the side
        side_x = cx + w/2 + 30
        _clabel(c, side_x, (ytop+ybot)/2 + 4, L["name"], 22, LBL,
                "bold", "start")
        _clabel(c, side_x, (ytop+ybot)/2 + 28,
                f"biomass \u2248 {L['biomass']} kg", 18, RED, "bold",
                "start")
    # arrow from bottom up
    c.S.append(
        f'<line x1="160" y1="{by_bottom}" x2="160" y2="{200}" '
        f'stroke="{ACC}" stroke-width="4"/>')
    c.S.append(
        f'<polygon points="160,200 150,220 170,220" fill="{ACC}"/>')
    _clabel(c, 220, (by_bottom+200)/2,
            "biomass", 20, LBL, "bold", "start")
    _clabel(c, 220, (by_bottom+200)/2 + 24,
            "decreases \u2191", 20, LBL, "bold", "start")
    _clabel(c, W/2, H-30,
            "Biomass and energy decrease as you move up trophic levels.",
            22, RED, "bold")
    return c.svg()


# ====================================================================
# 4) BIOMASS / ENERGY FLOW
#    A simple proportional flow: producer -> primary -> secondary, with
#    losses (heat, waste, movement) at each step.
# ====================================================================
def biomass_flow():
    """Sankey-style flow showing 10% biomass transfer up trophic levels."""
    W, H = 1320, 780
    c = Canvas(W, H)
    _clabel(c, W/2, 56,
            "Biomass / energy transfer up trophic levels", 34,
            weight="bold")

    # input bar (producers, 1000 units)
    levels = [
        ("Producers",            1000, GREEN),
        ("Primary consumers",     100, YELL),
        ("Secondary consumers",    10, AMB),
        ("Tertiary consumers",      1, "#C8102E"),
    ]
    # scale: max height 280 px for 1000 units, sqrt scale so small ones visible
    band_max = 280
    def H_for(b): return max(8, band_max * (b/1000) ** 0.5)
    bx = 100
    by_base = 480
    band_w = 230
    gap = 70
    for i, (name, biomass, col) in enumerate(levels):
        h = H_for(biomass)
        x = bx + i*(band_w + gap)
        y = by_base - h/2
        c.S.append(
            f'<rect x="{x}" y="{y}" width="{band_w}" height="{h}" '
            f'fill="{col}" opacity="0.75" stroke="{ST}" '
            f'stroke-width="2"/>')
        _clabel(c, x + band_w/2, by_base - h/2 - 18, name,
                22, LBL, "bold")
        _clabel(c, x + band_w/2, by_base + h/2 + 28,
                f"\u2248 {biomass} kg biomass", 20, RED, "bold")
        # losses arrow downward
        if i < len(levels) - 1:
            # tapering connector to next level
            nh = H_for(levels[i+1][1])
            ny = by_base - nh/2
            c.S.append(
                f'<path d="M {x+band_w} {y} L {x+band_w+gap} {ny} '
                f'L {x+band_w+gap} {ny+nh} L {x+band_w} {y+h} Z" '
                f'fill="{ACC}" opacity="0.3" stroke="{ST}" '
                f'stroke-width="1"/>')
            # loss arrow drops down
            lx = x + band_w + gap/2
            c.S.append(
                f'<line x1="{lx}" y1="{by_base + nh/2 + 10}" '
                f'x2="{lx}" y2="{by_base + 170}" '
                f'stroke="#E0892E" stroke-width="4"/>')
            c.S.append(
                f'<polygon points="{lx},{by_base+170} '
                f'{lx-9},{by_base+150} {lx+9},{by_base+150}" '
                f'fill="#E0892E"/>')
            _clabel(c, lx, by_base + 200,
                    "heat, waste,", 16, "#E0892E", "bold")
            _clabel(c, lx, by_base + 220, "movement",
                    16, "#E0892E", "bold")

    _clabel(c, W/2, H-50,
            "Only ~10% of biomass / energy passes to the next level.",
            22, RED, "bold")
    _clabel(c, W/2, H-22,
            "The rest is lost as heat (respiration), waste, "
            "and uneaten parts.",
            18, LBL, "normal")
    return c.svg()


# ====================================================================
# 5) DNA SCHEMATIC
#    Double helix shown as ladder with colour-coded base pairs.
# ====================================================================
def dna_schematic():
    """DNA as a ladder with sugar-phosphate backbone and base pairs."""
    W, H = 900, 880
    c = Canvas(W, H)
    _clabel(c, W/2, 56, "DNA structure (schematic)", 36, weight="bold")

    # two vertical strands
    cy_top, cy_bot = 130, H - 130
    left_x, right_x = 280, 620
    # backbone: zig-zag with sugar (pentagon) and phosphate (circle)
    n_rungs = 8
    step = (cy_bot - cy_top) / (n_rungs - 1)

    # base pairs: A-T (red-blue) and G-C (yellow-green)
    pairs = [("A","T"),("G","C"),("T","A"),("C","G"),
             ("A","T"),("G","C"),("T","A"),("C","G")]
    base_colours = {"A": "#C8102E", "T": "#3B82F6",
                    "G": "#FBBF24", "C": "#2E5E45"}

    # draw backbones first
    c.S.append(
        f'<line x1="{left_x}" y1="{cy_top}" x2="{left_x}" '
        f'y2="{cy_bot}" stroke="{STYLE["bracket"]}" stroke-width="5"/>')
    c.S.append(
        f'<line x1="{right_x}" y1="{cy_top}" x2="{right_x}" '
        f'y2="{cy_bot}" stroke="{STYLE["bracket"]}" stroke-width="5"/>')

    for i in range(n_rungs):
        y = cy_top + i*step
        # base pair as two coloured boxes meeting in the middle
        b1, b2 = pairs[i]
        mid = (left_x + right_x) / 2
        # left half
        c.S.append(
            f'<rect x="{left_x+10}" y="{y-22}" width="{mid-left_x-15}" '
            f'height="44" rx="6" fill="{base_colours[b1]}" '
            f'opacity="0.85" stroke="{ST}" stroke-width="1.5"/>')
        _clabel(c, (left_x + mid)/2, y+8, b1, 26, "#FFFFFF", "bold")
        # right half
        c.S.append(
            f'<rect x="{mid+5}" y="{y-22}" width="{right_x-mid-15}" '
            f'height="44" rx="6" fill="{base_colours[b2]}" '
            f'opacity="0.85" stroke="{ST}" stroke-width="1.5"/>')
        _clabel(c, (mid + right_x)/2, y+8, b2, 26, "#FFFFFF", "bold")

    # backbone label
    _clabel(c, left_x - 70, (cy_top+cy_bot)/2,
            "sugar-phosphate", 18, STYLE["bracket"], "bold")
    _clabel(c, left_x - 70, (cy_top+cy_bot)/2 + 22,
            "backbone", 18, STYLE["bracket"], "bold")
    # base pair label arrow
    _clabel(c, right_x + 90, (cy_top+cy_bot)/2 - 50,
            "base pairs", 20, LBL, "bold", "start")
    _clabel(c, right_x + 90, (cy_top+cy_bot)/2 - 26,
            "A \u2014 T", 18, LBL, "bold", "start")
    _clabel(c, right_x + 90, (cy_top+cy_bot)/2 - 4,
            "G \u2014 C", 18, LBL, "bold", "start")

    _clabel(c, W/2, H-50,
            "DNA is a double helix: two strands held by complementary "
            "base pairs.", 20, RED, "bold")
    _clabel(c, W/2, H-22,
            "A pairs with T; G pairs with C.",
            18, LBL, "normal")
    return c.svg()


# ====================================================================
# 6) MITOSIS STAGES
# ====================================================================
def mitosis_stages():
    """Five-panel strip of mitosis stages with sketch nuclei + chromosomes."""
    W, H = 1500, 600
    c = Canvas(W, H)
    _clabel(c, W/2, 56, "Mitosis \u2014 stages", 36, weight="bold")
    pw, ph = 270, 320
    py = 130
    n = 5
    gap = (W - 80 - pw*n) / (n - 1)
    titles = ["Interphase", "Prophase", "Metaphase", "Anaphase", "Telophase"]

    for i, ttl in enumerate(titles):
        px = 40 + i*(pw + gap)
        # panel
        c.S.append(
            f'<rect x="{px}" y="{py}" width="{pw}" height="{ph}" rx="10" '
            f'fill="{STYLE["cream"]}" stroke="{ST}" stroke-width="2"/>')
        cx, cy = px + pw/2, py + ph/2
        # cell membrane (large circle)
        c.S.append(
            f'<circle cx="{cx}" cy="{cy}" r="100" fill="none" '
            f'stroke="{ST}" stroke-width="2.5"/>')

        if i == 0:
            # Interphase: nucleus visible, DNA replicates
            c.S.append(
                f'<circle cx="{cx}" cy="{cy}" r="58" fill="{BLUE}" '
                f'opacity="0.35" stroke="{ST}" stroke-width="2"/>')
            _clabel(c, cx, cy + 6, "nucleus", 16, LBL, "normal")
        elif i == 1:
            # Prophase: nucleus dissolving, chromosomes condense (Xs)
            for ang in (40, 130, 220, 310):
                x = cx + 38*math.cos(math.radians(ang))
                y = cy + 38*math.sin(math.radians(ang))
                _draw_chromosome(c, x, y, RED, 22)
        elif i == 2:
            # Metaphase: chromosomes line up at equator
            for ox in (-50, 0, 50):
                _draw_chromosome(c, cx + ox, cy, RED, 22)
            c.S.append(
                f'<line x1="{cx-90}" y1="{cy}" x2="{cx+90}" y2="{cy}" '
                f'stroke="{ST}" stroke-width="1" stroke-dasharray="3 4"/>')
        elif i == 3:
            # Anaphase: chromatids pulled to poles
            for ox in (-65, -45, -25):
                _draw_chromatid(c, cx + ox, cy + (ox+45)*0.1,
                                RED, 18)
            for ox in (25, 45, 65):
                _draw_chromatid(c, cx + ox, cy + (ox-45)*0.1,
                                RED, 18)
        else:
            # Telophase: two nuclei forming, cell pinching
            c.S.append(
                f'<circle cx="{cx-40}" cy="{cy}" r="34" fill="{BLUE}" '
                f'opacity="0.35" stroke="{ST}" stroke-width="2"/>')
            c.S.append(
                f'<circle cx="{cx+40}" cy="{cy}" r="34" fill="{BLUE}" '
                f'opacity="0.35" stroke="{ST}" stroke-width="2"/>')
            # cleavage furrow
            c.S.append(
                f'<line x1="{cx}" y1="{cy-100}" x2="{cx}" y2="{cy+100}" '
                f'stroke="{ST}" stroke-width="1.5" '
                f'stroke-dasharray="4 5"/>')

        # title
        _clabel(c, cx, py - 14, ttl, 22, LBL, "bold")

    _clabel(c, W/2, H-30,
            "Mitosis produces two genetically identical daughter cells. "
            "Used in growth, repair, asexual reproduction.",
            21, RED, "bold")
    return c.svg()


def _draw_chromosome(c, cx, cy, col, r):
    """X-shaped chromosome."""
    c.S.append(
        f'<line x1="{cx-r}" y1="{cy-r}" x2="{cx+r}" y2="{cy+r}" '
        f'stroke="{col}" stroke-width="6" stroke-linecap="round"/>')
    c.S.append(
        f'<line x1="{cx-r}" y1="{cy+r}" x2="{cx+r}" y2="{cy-r}" '
        f'stroke="{col}" stroke-width="6" stroke-linecap="round"/>')


def _draw_chromatid(c, cx, cy, col, r):
    """Single I-shaped chromatid (anaphase)."""
    c.S.append(
        f'<line x1="{cx}" y1="{cy-r}" x2="{cx}" y2="{cy+r}" '
        f'stroke="{col}" stroke-width="6" stroke-linecap="round"/>')


# ====================================================================
# 7) REFLEX ARC
# ====================================================================
def reflex_arc():
    """Box-and-arrow diagram of a reflex arc."""
    W, H = 1380, 620
    c = Canvas(W, H)
    _clabel(c, W/2, 56, "The Reflex Arc", 36, weight="bold")
    steps = [
        ("Stimulus",       "e.g. hot object",              "#C8102E"),
        ("Receptor",       "in skin",                       "#E0892E"),
        ("Sensory neurone","carries impulse to CNS",        "#FBBF24"),
        ("Relay neurone",  "in spinal cord",                "#A9D9BE"),
        ("Motor neurone",  "carries impulse to effector",   "#3B82F6"),
        ("Effector",       "muscle / gland",                "#9333EA"),
        ("Response",       "e.g. pull hand away",           "#2E5E45"),
    ]
    n = len(steps)
    bw, bh = 170, 110
    by = 220
    gap = (W - 80 - bw*n) / (n - 1)
    for i, (label, sub, col) in enumerate(steps):
        bx = 40 + i*(bw + gap)
        c.S.append(
            f'<rect x="{bx}" y="{by}" width="{bw}" height="{bh}" rx="12" '
            f'fill="{col}" opacity="0.6" stroke="{ST}" '
            f'stroke-width="2.5"/>')
        _clabel(c, bx+bw/2, by+bh/2-6, label, 19, LBL, "bold")
        _clabel(c, bx+bw/2, by+bh/2+22, sub, 14, LBL, "normal")
        if i < n - 1:
            _arrow(c, bx+bw+4, by+bh/2,
                   bx+bw+gap-4, by+bh/2, ACC, 5)
    _clabel(c, W/2, H-50,
            "Reflex actions are AUTOMATIC and FAST \u2014 they bypass "
            "the conscious brain.",
            22, RED, "bold")
    _clabel(c, W/2, H-22,
            "Pathway: stimulus \u2192 receptor \u2192 sensory \u2192 "
            "relay \u2192 motor \u2192 effector \u2192 response.",
            18, LBL, "normal")
    return c.svg()


# ====================================================================
# 8) ECOLOGICAL CYCLES (water + nitrogen, plus a bio carbon cycle)
# ====================================================================
def water_cycle():
    """Schematic with sun, sea, clouds, mountain, river — labelled
    processes: evaporation, condensation, precipitation, run-off."""
    W, H = 1380, 760
    c = Canvas(W, H)
    _clabel(c, W/2, 56, "The Water Cycle", 36, weight="bold")
    # sun (top right)
    c.S.append(
        f'<circle cx="{W-180}" cy="160" r="48" fill="#FBBF24" '
        f'opacity="0.9" stroke="{ST}" stroke-width="2"/>')
    _clabel(c, W-180, 168, "Sun", 22, LBL, "bold")
    # mountain (left)
    c.S.append(
        f'<polygon points="120,560 380,260 640,560" '
        f'fill="{STYLE["bracket"]}" opacity="0.5" stroke="{ST}" '
        f'stroke-width="2"/>')
    _clabel(c, 380, 530, "Mountain", 20, LBL, "bold")
    # sea (bottom right)
    c.S.append(
        f'<rect x="700" y="560" width="{W-720}" height="120" '
        f'fill="{BLUE}" opacity="0.5" stroke="{ST}" stroke-width="2"/>')
    _clabel(c, (700+W-20)/2, 630, "Sea / Ocean", 22, LBL, "bold")
    # clouds (top middle)
    for cx_c, cy_c, r in ((700, 180, 50), (760, 165, 60), (820, 185, 50)):
        c.S.append(
            f'<circle cx="{cx_c}" cy="{cy_c}" r="{r}" fill="#FFFFFF" '
            f'stroke="{ST}" stroke-width="2"/>')
    _clabel(c, 760, 190, "Clouds", 20, LBL, "bold")
    # arrows: evaporation (sea up to clouds)
    _arrow(c, 950, 560, 830, 240, BLUE)
    _clabel(c, 950, 400, "evaporation", 19, BLUE, "bold", "start")
    # condensation (in clouds — small downward arrows from cloud level)
    _clabel(c, 760, 250, "condensation", 18, "#5B6B82", "bold")
    # precipitation (cloud onto mountain)
    for off in (-30, 0, 30):
        _arrow(c, 680 + off, 220, 480 + off, 380, BLUE, 3)
    _clabel(c, 500, 320, "precipitation", 19, BLUE, "bold", "end")
    # run-off (mountain to sea)
    _arrow(c, 600, 480, 880, 560, AMB)
    _clabel(c, 740, 530, "run-off / rivers",
            19, AMB, "bold")
    _clabel(c, W/2, H-30,
            "Sun drives evaporation \u2192 condensation \u2192 "
            "precipitation \u2192 run-off (continuous cycle).",
            22, RED, "bold")
    return c.svg()


def nitrogen_cycle():
    """4-box cycle: atmosphere (N2), plants (proteins), animals (proteins),
    decomposers + bacteria roles."""
    W, H = 1380, 800
    c = Canvas(W, H)
    _clabel(c, W/2, 56, "The Nitrogen Cycle", 36, weight="bold")

    def box(cx, cy, w, h, txt, fill):
        c.S.append(
            f'<rect x="{cx-w/2}" y="{cy-h/2}" width="{w}" height="{h}" '
            f'rx="14" fill="{fill}" opacity="0.55" stroke="{ST}" '
            f'stroke-width="2.5"/>')
        _clabel(c, cx, cy+8, txt, 22, LBL, "bold")

    # 4 boxes
    atm = (W/2,   170)
    pln = (310,   430)
    ani = (W-310, 430)
    dec = (W/2,   690)
    box(atm[0], atm[1], 380, 90, "N\u2082 in atmosphere",  BLUE)
    box(pln[0], pln[1], 300, 90, "Plants (proteins)",      GREEN)
    box(ani[0], ani[1], 300, 90, "Animals (proteins)",     AMB)
    box(dec[0], dec[1], 380, 90, "Decomposers + bacteria", YELL)

    def labelled_arrow(x1, y1, x2, y2, label, col, off=(0, -10)):
        _arrow(c, x1, y1, x2, y2, col, 4)
        midx, midy = (x1+x2)/2, (y1+y2)/2
        # cream halo
        pad = len(label) * 11 + 16
        c.S.append(
            f'<rect x="{midx + off[0] - pad/2:.1f}" '
            f'y="{midy + off[1] - 11:.1f}" width="{pad}" '
            f'height="22" rx="4" fill="{STYLE["cream"]}" opacity="0.95"/>')
        _clabel(c, midx + off[0], midy + off[1] + 6,
                label, 18, col, "bold")

    # N2 -> plants (fixation, lightning + nitrogen-fixing bacteria)
    labelled_arrow(atm[0]-150, atm[1]+45, pln[0]+50, pln[1]-50,
                   "nitrogen fixation", "#2E8B7F")
    # plants -> animals (feeding)
    labelled_arrow(pln[0]+150, pln[1], ani[0]-150, ani[1],
                   "feeding", AMB)
    # animals -> decomposers
    labelled_arrow(ani[0], ani[1]+45, dec[0]+90, dec[1]-50,
                   "death + waste", "#5B6B82")
    # plants -> decomposers
    labelled_arrow(pln[0], pln[1]+45, dec[0]-90, dec[1]-50,
                   "death", "#5B6B82")
    # decomposers -> atmosphere (denitrification)
    labelled_arrow(dec[0]+150, dec[1]-30, atm[0]+150, atm[1]+45,
                   "denitrification", "#C8102E")
    # decomposers -> plants (nitrification + ammonification)
    labelled_arrow(dec[0]-150, dec[1]-30, pln[0]+50, pln[1]+45,
                   "nitrification", "#3B82F6")

    _clabel(c, W/2, H-30,
            "Bacteria are essential at every step: fixing, nitrifying, "
            "decomposing, denitrifying.",
            21, RED, "bold")
    return c.svg()


# ====================================================================
# DEMO / RENDER ALL
# ====================================================================
def _render_all():
    export(punnett_square("Bb", "Bb", "brown / blue eyes"),
           "bio_punnett_Bb_Bb", formats=("png",))
    export(food_chain(), "bio_food_chain", formats=("png",))
    export(pyramid_of_biomass(), "bio_pyramid", formats=("png",))
    export(biomass_flow(), "bio_biomass_flow", formats=("png",))
    export(dna_schematic(), "bio_dna", formats=("png",))
    export(mitosis_stages(), "bio_mitosis", formats=("png",))
    export(reflex_arc(), "bio_reflex_arc", formats=("png",))
    export(water_cycle(), "bio_water_cycle", formats=("png",))
    export(nitrogen_cycle(), "bio_nitrogen_cycle", formats=("png",))
    for nm in ("bio_punnett_Bb_Bb","bio_food_chain","bio_pyramid",
               "bio_biomass_flow","bio_dna","bio_mitosis","bio_reflex_arc",
               "bio_water_cycle","bio_nitrogen_cycle"):
        print("bio", nm)


if __name__ == "__main__":
    _render_all()


# ====================================================================
# ⊕ FIGLIB EXTENSIONS (MRB-352 run 2) — question figures
#
# New builders in the library's style for the question figures the
# library had no drawing for. Phone-width canvases; text size derived
# from the canvas (`q_font`), labels always dark sage on paper or on a
# light tint — never on a dark fill.
# ====================================================================
from .style import (GEORGIA_WIDE, MUTED, TINT, arrow as _q_arrow,  # noqa: E402
                    box as _q_box,
                    line as _q_line, q_font, q_stroke, text as _q_text,
                    text_width as _tw, wrap as _wrap)


def _edge_point(cx, cy, hw, hh, tx, ty):
    """Where the line from a box's centre towards (tx, ty) leaves the box."""
    dx, dy = tx - cx, ty - cy
    if dx == 0 and dy == 0:
        return cx, cy
    s = min(hw / abs(dx) if dx else 1e9, hh / abs(dy) if dy else 1e9)
    return cx + dx * s, cy + dy * s


def _seg_box_gap(x1, y1, x2, y2, bx, by, hw, hh):
    """Smallest distance from a line segment to an axis-aligned box
    (0 if they touch or cross). Sampled — exact enough for a layout guard."""
    best = 1e9
    for k in range(201):
        t = k / 200.0
        px, py = x1 + (x2 - x1) * t, y1 + (y2 - y1) * t
        dx = max(abs(px - bx) - hw, 0.0)
        dy = max(abs(py - by) - hh, 0.0)
        best = min(best, math.hypot(dx, dy))
    return best


def food_web(nodes, eats, W=640, H=420, legend=None, clearance=12):
    """A food web: labelled boxes joined by straight one-way arrows.

    nodes   [{"id", "name", "x", "y"}] — box centres, in canvas units.
    eats    [(food_id, feeder_id)] — each an arrow FROM the food TO the
            feeder, the direction energy flows, with a solid head at the
            feeder's box.
    legend  a line (or lines) of text under the web.

    Refuses to draw a web in which any arrow passes within `clearance`
    units of a box other than its own two — a line through a box reads as
    a link to it, which is how a food web gets misread.
    """
    fs = q_font(W)
    sw = q_stroke(W, 2)
    bh = fs + 16
    leg = []
    for ln in ([legend] if isinstance(legend, str) else (legend or [])):
        # ⊕ batch-2 fix round (checks rule 8): the legend starts at x=72, so
        # it wraps to what is left of the card less the edge clearance, at
        # the widest fallback face.
        leg.extend(_wrap(ln, fs, (W - 72 - 12) / GEORGIA_WIDE))
    Htot = int(H + (len(leg) * (fs + 7) + 10 if leg else 0))
    c = Canvas(W, Htot)
    pos = {}
    for nd in nodes:
        hw = (_tw(nd["name"], fs, True) + 24) / 2.0
        if nd["x"] - hw < 10 or nd["x"] + hw > W - 10:
            raise ValueError("food_web: box %r runs off the canvas" % nd["name"])
        pos[nd["id"]] = (nd["x"], nd["y"], hw, bh / 2.0, nd["name"])
    ids = list(pos)
    for i, a in enumerate(ids):
        for b_ in ids[i + 1:]:
            ax, ay, ahw, ahh, an = pos[a]
            bx, by, bhw, bhh, bn = pos[b_]
            gx = abs(ax - bx) - ahw - bhw
            gy = abs(ay - by) - ahh - bhh
            if max(gx, gy) < clearance:
                raise ValueError("food_web: boxes %r and %r are %.1f units "
                                 "apart (needs %g)" % (an, bn, max(gx, gy),
                                                       clearance))
    segs = []
    for a, b in eats:
        ax, ay, ahw, ahh, _ = pos[a]
        bx, by, bhw, bhh, _ = pos[b]
        sx, sy = _edge_point(ax, ay, ahw, ahh, bx, by)
        ex, ey = _edge_point(bx, by, bhw + 2, bhh + 2, ax, ay)
        for nid, (ox, oy, ohw, ohh, name) in pos.items():
            if nid in (a, b):
                continue
            g = _seg_box_gap(sx, sy, ex, ey, ox, oy, ohw, ohh)
            if g < clearance:
                raise ValueError(
                    "food_web: the arrow %s -> %s passes %.1f units from the "
                    "%r box (needs %g). Move a box." % (a, b, g, name, clearance))
        segs.append((sx, sy, ex, ey))
    for sx, sy, ex, ey in segs:
        # the head is >= 9px on a 390px phone, whatever the canvas width
        _q_arrow(c, sx, sy, ex, ey, ST, q_stroke(W, 2.5), max(16, W / 36.0))
    for nid, (x, yc, hw, hh, name) in pos.items():
        _q_box(c, x - hw, yc - hh, 2 * hw, 2 * hh, TINT["white"], ST, sw, 8)
        _q_text(c, x, yc + fs * 0.36, name, fs, LBL, "bold")
    if leg:
        ky = H + fs
        _q_arrow(c, 18, ky - fs * 0.35, 62, ky - fs * 0.35, ST,
                 q_stroke(W, 2.5), 12)
        for ln in leg:
            _q_text(c, 72, ky, ln, fs, LBL, "normal", "start")
            ky += fs + 7
    return c.svg()


# Big bases on a light fill, small bases on a MID-tone fill, both with ink
# letters (>= 10:1) — two fills a pupil can tell apart at a glance, neither
# of them dark. (The first drawing of this figure painted its small bases
# through a stylesheet class and they printed black-on-black off the
# lesson page — figure-contract §8.)
BIG_FILL = TINT["salmon"]
SMALL_FILL = STYLE["nm_fill"]


def dna_ladder(rungs, big=("A", "G"), guide="every rung the same width",
               W=420):
    """DNA untwisted into a ladder: two backbones and base-pair rungs,
    each base drawn to its SIZE — the large bases (A, G) wide, the small
    ones (C, T) narrow — so a big-with-small rung and every other
    big-with-small rung come out the same width."""
    fs = q_font(W)
    sw = q_stroke(W, 2)
    rh, rg = fs + 18, 14
    bb = 16                                   # backbone thickness
    xl, xr = 60, W - 60
    inner = xr - xl - 2 * bb
    top = 30 + fs + 12
    n = len(rungs)
    H = int(top + n * (rh + rg) + 26 + 2 * (fs + 8) + 30)
    c = Canvas(W, H)
    ladder_bot = top + n * (rh + rg) - rg + 10
    for x in (xl, xr - bb):
        _q_box(c, x, top - 10, bb, ladder_bot - top + 20, TINT["sand"], ST, sw, 4)
    big_w = inner * 0.6
    for i, (a, b) in enumerate(rungs):
        y = top + i * (rh + rg)
        wa = big_w if a in big else inner - big_w
        x0 = xl + bb
        for letter, x, w in ((a, x0, wa), (b, x0 + wa, inner - wa)):
            fillc = BIG_FILL if letter in big else SMALL_FILL
            _q_box(c, x, y, w, rh, fillc, ST, sw, 3)
            _q_text(c, x + w / 2, y + rh / 2 + fs * 0.36, letter, fs, ST)
    # the same width, measured at the top and the bottom
    for yy in (top - 22, ladder_bot + 14):
        _q_line(c, xl + bb, yy, xr - bb, yy, MUTED, sw)
        for x in (xl + bb, xr - bb):
            _q_line(c, x, yy - 7, x, yy + 7, MUTED, sw)
    _q_text(c, W / 2, top - 22 - 8, guide, fs, LBL, "normal")
    ky = ladder_bot + 14 + fs + 22
    _q_box(c, 30, ky - fs + 1, 22, fs, BIG_FILL, ST, sw, 2)
    _q_text(c, 60, ky, "large bases: " + " and ".join(big), fs, LBL,
             "normal", "start")
    ky += fs + 10
    small = sorted({x for r in rungs for x in r} - set(big))
    _q_box(c, 30, ky - fs + 1, 22, fs, SMALL_FILL, ST, sw, 2)
    _q_text(c, 60, ky, "small bases: " + " and ".join(small), fs, LBL,
             "normal", "start")
    return c.svg()


def _moth(c, x, y, fill, edge, s=1.0):
    """A resting moth seen from above: two wings and a body."""
    wing_l = [(x - 2*s, y - 12*s), (x - 22*s, y - 4*s), (x - 42*s, y + 16*s),
              (x - 38*s, y + 24*s), (x - 2*s, y + 20*s)]
    wing_r = [(2*x - px, py) for px, py in wing_l]
    for pts in (wing_l, wing_r):
        c.S.append('<polygon points="%s" fill="%s" stroke="%s" '
                   'stroke-width="2" stroke-linejoin="round"/>'
                   % (" ".join("%.1f,%.1f" % p for p in pts), fill, edge))
    c.S.append(f'<ellipse cx="{x:.1f}" cy="{y + 4*s:.1f}" rx="{5*s:.1f}" '
               f'ry="{18*s:.1f}" fill="{fill}" stroke="{edge}" '
               f'stroke-width="2"/>')
    for k in (-1, 1):                                 # antennae
        c.S.append(f'<line x1="{x + 2*k*s:.1f}" y1="{y - 12*s:.1f}" '
                   f'x2="{x + 12*k*s:.1f}" y2="{y - 26*s:.1f}" stroke="{edge}" '
                   f'stroke-width="2" stroke-linecap="round"/>')


def moth_pair(panels, W=480):
    """The same pale moth and the same dark moth, on two barks, side by
    side. Every label sits on the paper OUTSIDE the panels, so none is
    ever on the dark bark. `panels` is [{"title", "bark": "lichen"|"soot"}]."""
    fs = q_font(W)
    pw = (W - 30 - 10 * (len(panels) - 1)) / float(len(panels))
    ph = 170
    top = 16 + fs + 8
    H = int(top + ph + 14 + fs + 16)
    c = Canvas(W, H)
    pale, pale_edge = "#E3DFCB", "#C9C4AC"
    dark, dark_edge = "#2F2D29", "#262421"
    for i, p in enumerate(panels):
        x = 15 + i * (pw + 10)
        _q_text(c, x + pw / 2, 16 + fs, p["title"], fs, LBL, "bold")
        if p["bark"] == "lichen":
            _q_box(c, x, top, pw, ph, "#D8D6C1", ST, 2.5, 6)
            for k, (fx, fy, rx, ry) in enumerate(
                    ((0.2, 0.2, 18, 11), (0.7, 0.15, 22, 12),
                     (0.45, 0.8, 26, 13), (0.85, 0.75, 16, 10),
                     (0.1, 0.7, 14, 9), (0.55, 0.45, 12, 8))):
                col = "#C2C8A2" if k % 2 else "#E6E3D1"
                c.S.append(f'<ellipse cx="{x + pw*fx:.1f}" cy="{top + ph*fy:.1f}" '
                           f'rx="{rx}" ry="{ry}" fill="{col}" stroke="none"/>')
        else:
            _q_box(c, x, top, pw, ph, "#34322E", ST, 2.5, 6)
            for k in range(7):
                sx = x + 14 + k * (pw - 28) / 6.0
                _q_line(c, sx, top + 10, sx + 4, top + ph - 10, "#28261F",
                        q_stroke(W, 3), None, "butt")
        _moth(c, x + pw * 0.3, top + ph * 0.48, pale, pale_edge)
        _moth(c, x + pw * 0.72, top + ph * 0.52, dark, dark_edge)
        ly = top + ph + 14 + fs
        _q_text(c, x + pw * 0.3, ly, "pale moth", fs, LBL, "normal")
        _q_text(c, x + pw * 0.72, ly, "dark moth", fs, LBL, "normal")
    return c.svg()


def plant_cell(W=460, labels=True):
    """A leaf (palisade-type) plant cell, schematic: cell wall, cell
    membrane, cytoplasm, a large permanent vacuole filling the middle, the
    nucleus pushed to one side by it, and chloroplasts in the cytoplasm.
    Labels on the paper to the right, each with a leader line."""
    fs = q_font(W)
    sw = q_stroke(W, 2)
    H = 380
    c = Canvas(W, H)
    x0, y0, cw, ch = 24, 24, 230, H - 48
    _q_box(c, x0, y0, cw, ch, "#CFE3C2", ST, 3, 22)          # cell wall
    m = 10
    _q_box(c, x0 + m, y0 + m, cw - 2*m, ch - 2*m, "#EEF3DF", ST, sw, 16)
    # ⊕ fix round 2 (examiner m3): the three left-edge chloroplasts sat
    # across the membrane, in the wall band. They moved inward (dx 214/
    # 214/212 → 205/205/203, cx 49/49/51), and the vacuole's left side
    # moved in from x0+26 to x0+40 (its right side unchanged) so they sit
    # in cytoplasm between membrane and vacuole, touching neither.
    vx, vy, vw, vh = x0 + 40, y0 + 40, cw - 102, ch - 80
    _q_box(c, vx, vy, vw, vh, TINT["blue"], ST, sw, 30)      # the vacuole
    nx, ny = x0 + cw - 36, y0 + ch * 0.46                    # pushed aside
    c.S.append(f'<ellipse cx="{nx:.1f}" cy="{ny:.1f}" rx="20" ry="30" '
               f'fill="{TINT["lilac"]}" stroke="{ST}" stroke-width="{sw}"/>')
    chloros = [(x0 + cw - dx, y0 + dy) for dx, dy in
               ((36, 34), (118, 26), (196, 30), (205, 110), (205, 200),
                (203, 290), (140, ch - 26), (60, ch - 28), (30, ch - 80))]
    for cx_, cy_ in chloros:
        c.S.append(f'<ellipse cx="{cx_:.1f}" cy="{cy_:.1f}" rx="11" ry="7" '
                   f'fill="#7FB98A" stroke="{ST}" stroke-width="{sw}"/>')
    if labels:
        lx = x0 + cw + 34
        # ⊕ fix round 1 (visual M4): the wall's anchor sits high on the
        # wall, so its leader runs nearly flat. At y0+64 the chloroplast
        # leader passed within ~1.5 units of it and read as pointing there.
        parts = [("cell wall", (x0 + cw - 1, y0 + 26)),
                 ("chloroplast", chloros[0]),
                 ("cell membrane", (x0 + cw - m, y0 + 118)),
                 ("nucleus", (nx + 8, ny)),
                 ("vacuole", (vx + vw - 24, vy + vh * 0.72)),
                 ("cytoplasm", (x0 + cw - 18, y0 + ch - 44))]
        for i, (name, (px, py)) in enumerate(parts):
            ly = y0 + 34 + i * ((ch - 50) / (len(parts) - 1))
            _q_line(c, lx - 6, ly - fs * 0.35, px, py, ST, sw)
            c.S.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="3.5" '
                       f'fill="{ST}" stroke="none"/>')
            _q_text(c, lx, ly, name, fs, LBL, "bold", "start")
    return c.svg()
