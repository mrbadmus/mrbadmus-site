"""
Rainford High School — Chemistry Paper 1 Diagram Library
=========================================================
Mr Badmus house style. Accurate, parametrised AQA diagrams.

PHASE 1: style core + covalent dot-and-cross engine.

Usage:
    from chem_diagrams import covalent_dotcross, export
    svg = covalent_dotcross("H2O")
    export(svg, "h2o", formats=("png","svg","pdfpng"))

Driving it in chat:
    "use the chem diagram library — give me the dot-and-cross for ammonia"
"""

import math
import os

from .style import STYLE, Canvas, _pol, export  # noqa: F401 — the shared core


# ====================================================================
# MOLECULE DATA TABLE
#   Each entry: central atom + list of (bonded atom, bond order).
#   lone_pairs = lone pairs on the CENTRAL atom.
#   The engine places bonds evenly around the centre and draws each
#   bond order as that many shared (dot+cross) pairs in the overlap.
# ====================================================================
MOLECULES = {
    "H2O": {"centre": "O", "fill": "nm",
            "bonds": [("H", 1), ("H", 1)], "lone_pairs": 2,
            "name": "Water, H\u2082O", "spread": 104},
    "NH3": {"centre": "N", "fill": "nm",
            "bonds": [("H", 1), ("H", 1), ("H", 1)], "lone_pairs": 1,
            "name": "Ammonia, NH\u2083", "spread": 107},
    "CH4": {"centre": "C", "fill": "nm",
            "bonds": [("H", 1), ("H", 1), ("H", 1), ("H", 1)], "lone_pairs": 0,
            "name": "Methane, CH\u2084", "spread": 109},
    "CO2": {"centre": "C", "fill": "nm",
            "bonds": [("O", 2), ("O", 2)], "lone_pairs": 0,
            "name": "Carbon dioxide, CO\u2082", "spread": 180,
            "outer_lp": {"O": 2}},
    "Cl2": {"centre": "Cl", "fill": "nm",
            "bonds": [("Cl", 1)], "lone_pairs": 3,
            "name": "Chlorine, Cl\u2082", "spread": 180, "outer_lp": {"Cl": 3}},
    "O2":  {"centre": "O", "fill": "nm",
            "bonds": [("O", 2)], "lone_pairs": 2,
            "name": "Oxygen, O\u2082", "spread": 180, "outer_lp": {"O": 2}},
    "N2":  {"centre": "N", "fill": "nm",
            "bonds": [("N", 3)], "lone_pairs": 1,
            "name": "Nitrogen, N\u2082", "spread": 180, "outer_lp": {"N": 1}},
    "HCl": {"centre": "Cl", "fill": "nm",
            "bonds": [("H", 1)], "lone_pairs": 3,
            "name": "Hydrogen chloride, HCl", "spread": 180},
}

_R = {"H": 50, "O": 96, "N": 96, "C": 96, "Cl": 100}  # shell radii


# ====================================================================
# COVALENT DOT-AND-CROSS ENGINE
# ====================================================================
def covalent_dotcross(formula, title=True, compact=False, incomplete=(),
                      angles=None, detached=(), dashed=False, nuclei=True,
                      seat="nucleus"):
    """Return SVG string for the covalent dot-and-cross of `formula`.

    ⊕ figlib parameters (defaults = the library's own drawing):
      title       False drops the heading (a question supplies its own stem).
      compact     True crops the canvas to the molecule instead of the
                  library's fixed 900x620 slide, so the same drawing is
                  legible in a phone's 320px column.
      incomplete  indices of bonds drawn WRONG on purpose: that bond's
                  shared pair shows only the outer atom's cross, with no dot
                  from the central atom — for "what has the student done
                  wrong?" questions. Never used for a correct drawing.
      angles      the bond directions, overriding the table's layout.
      detached    indices of outer atoms drawn APART from the centre, not
                  bonded at all: their circle does not touch the centre's,
                  and their one electron sits at their own centre.
      dashed      dashed outer-shell circles (the exam-paper look).
      nuclei      False: no filled nucleus discs, just the element letter.
      seat        "nucleus" (library) puts each shared pair just outside the
                  central nucleus; "lens" puts it in the middle of the
                  overlap between the two shells, so both electrons of the
                  pair sit visibly INSIDE the overlap.
    """
    if formula not in MOLECULES:
        raise KeyError(
            f"'{formula}' not in molecule table. Available: "
            f"{', '.join(MOLECULES)}. Ask to add it.")
    m = MOLECULES[formula]
    OR = _R[m["centre"]]
    centre_fill = STYLE["nm_fill"] if m["fill"] == "nm" else STYLE["h_fill"]

    n = len(m["bonds"])
    linear = (m["spread"] >= 180 and n <= 2)
    if angles is not None:
        angles = list(angles)
    elif linear:
        angles = [180, 0][:n] if n == 2 else [0]
    elif n == 2:
        angles = [212, 328]
    elif n == 3:
        angles = [210, 330, 90]
    elif n == 4:
        angles = [45, 135, 225, 315]
    else:
        angles = [i * 360/n for i in range(n)]

    if compact:
        overlap = 18 if linear else 30
        boxes = [(0, 0, OR + 10)]
        for (atom, order), ang in zip(m["bonds"], angles):
            BR = _R[atom]
            dist = OR + BR + 14 if len(boxes) - 1 in detached else OR + BR - overlap
            bx, by = _pol(0, 0, dist, ang)
            boxes.append((bx, by, BR + 10))
        minx = min(x - r for x, y, r in boxes)
        maxx = max(x + r for x, y, r in boxes)
        miny = min(y - r for x, y, r in boxes)
        maxy = max(y + r for x, y, r in boxes)
        pad = 14
        W, H = int(maxx - minx + 2*pad), int(maxy - miny + 2*pad)
        Ox, Oy = pad - minx, pad - miny
        top = 0
    else:
        W, H = 900, 620
        Ox, Oy = W/2, H/2 + 30
    c = Canvas(W, H)
    if title and not compact:
        c.label(W/2, 70, m["name"], 40, "bold")

    def shell(x, y, r):
        if dashed:
            c.S.append(
                f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="none" '
                f'stroke="{STYLE["stroke"]}" stroke-width="{STYLE["shell_w"]}" '
                f'stroke-dasharray="7 5"/>')
        else:
            c.shell(x, y, r)

    shell(Ox, Oy, OR)

    bond_geo = []
    for k_bond, ((atom, order), ang) in enumerate(zip(m["bonds"], angles)):
        BR = _R[atom]
        # diatomic/linear: light overlap. bent/pyramidal/tetrahedral:
        # moderate overlap — a clear lens without burying the shared pair.
        overlap = 18 if linear else 30
        gap = OR + BR + 14 if k_bond in detached else OR + BR - overlap
        bx, by = _pol(Ox, Oy, gap, ang)
        shell(bx, by, BR)
        bond_geo.append((atom, order, ang, bx, by, BR, gap))

    # central-atom lone pairs — placed on the freest arc, away from bonds.
    # central atom always uses dots.
    used = [g[2] % 360 for g in bond_geo]
    free = _free_angle(used)
    _draw_lone_pairs(c, Ox, Oy, OR, m["lone_pairs"], free, symbol="dot")

    # shared pairs: anchored on the bond axis at a fixed distance just
    # OUTSIDE the central nucleus (AQA textbook convention). Anchoring to
    # the nucleus radius — not the lens — guarantees the pair is always in
    # clear visible space and never buried under either nucleus, whatever
    # the relative shell sizes.
    NUC_C = 34                                        # central nucleus radius
    seat_mode_lens = (seat == "lens")
    for k_bond, (atom, order, ang, bx, by, BR, gap) in enumerate(bond_geo):
        dx, dy = bx-Ox, by-Oy
        d = math.hypot(dx, dy); ux, uy = dx/d, dy/d   # along bond axis
        px, py = -uy, ux                              # perpendicular
        NUC_O = 23 if atom == "H" else 30             # outer nucleus radius
        near = NUC_C + 16                             # just past central nuc
        far  = d - NUC_O - 16                         # just before outer nuc
        seat = (near + far) / 2                        # midway in clear gap
        if seat_mode_lens:
            seat = (OR + (d - BR)) / 2                 # middle of the lens
        if k_bond in detached:
            c.cross(bx, by)                            # its own, unshared
            continue
        lx, ly = Ox + ux*seat, Oy + uy*seat
        for off in _pair_offsets(order):
            cxp, cyp = lx + px*off, ly + py*off
            if seat_mode_lens:
                # the lens is narrow ALONG the bond and tall across it, so
                # the pair sits across it, side by side, both clearly inside
                ax_, ay_ = px*10, py*10
            else:
                ax_, ay_ = ux*7, uy*7
            if k_bond not in incomplete:
                c.dot(cxp - ax_, cyp - ay_)           # central atom electron
            c.cross(cxp + ax_, cyp + ay_)             # outer atom electron

    # outer-atom lone pairs. For homonuclear diatomics (N2, O2, Cl2) the
    # second atom's electrons are shown as CROSSES so the two atoms are
    # distinguishable (AQA convention). Heteronuclear keeps dots.
    for atom, order, ang, bx, by, BR, gap in bond_geo:
        if "outer_lp" in m and atom in m["outer_lp"]:
            away = math.degrees(math.atan2(by-Oy, bx-Ox))
            homonuclear = (atom == m["centre"])
            sym = "cross" if homonuclear else "dot"
            _draw_lone_pairs(c, bx, by, BR, m["outer_lp"][atom],
                             away, symbol=sym)

    # nuclei on top
    if nuclei:
        c.nucleus(Ox, Oy, m["centre"], centre_fill, 34)
        for atom, order, ang, bx, by, BR, gap in bond_geo:
            fill = STYLE["h_fill"] if atom == "H" else STYLE["nm_fill"]
            c.nucleus(bx, by, atom, fill, 23 if atom == "H" else 30)
    else:
        # letters only: the centre's at its centre, each outer atom's on the
        # side of its circle AWAY from the centre (its middle may hold an
        # electron)
        fs = max(26, int(W * 11.5 / 320) + 1)
        c.S.append(
            f'<text x="{Ox:.1f}" y="{Oy + fs*0.36:.1f}" font-family="{STYLE["font"]}" '
            f'font-size="{fs}" font-weight="bold" fill="{STYLE["label"]}" '
            f'text-anchor="middle">{m["centre"]}</text>')
        for atom, order, ang, bx, by, BR, gap in bond_geo:
            lx, ly = _pol(bx, by, BR * 0.55, ang)
            c.S.append(
                f'<text x="{lx:.1f}" y="{ly + fs*0.36:.1f}" font-family="{STYLE["font"]}" '
                f'font-size="{fs}" font-weight="bold" fill="{STYLE["label"]}" '
                f'text-anchor="middle">{atom}</text>')

    return c.svg()


def _pair_offsets(order):
    """Perpendicular offsets for `order` shared pairs in one bond."""
    if order == 1: return [0]
    if order == 2: return [-15, 15]
    if order == 3: return [-22, 0, 22]
    return [0]


def _free_angle(used):
    """Find the angle of the largest gap between used bond angles."""
    if not used:
        return 90
    s = sorted(used)
    best_gap, best_mid = -1, 90
    for i in range(len(s)):
        a = s[i]
        b = s[(i+1) % len(s)] + (360 if i == len(s)-1 else 0)
        gap = b - a
        if gap > best_gap:
            best_gap, best_mid = gap, (a + b)/2 % 360
    return best_mid


def _draw_lone_pairs(c, cx, cy, r, n_pairs, centre_deg, arc=None, symbol="dot"):
    """Draw n_pairs lone pairs (each = two electrons together) on the free
    arc centred on centre_deg. `arc` sets the total angular spread; `symbol`
    is "dot" or "cross" so homonuclear diatomics can show one atom's
    electrons as dots and the other's as crosses (AQA convention)."""
    if n_pairs <= 0:
        return
    if arc is None:
        arc = {1: 0, 2: 90, 3: 150}.get(n_pairs, 60 * (n_pairs - 1))
    start = centre_deg - arc/2
    step = arc/(n_pairs-1) if n_pairs > 1 else 0
    mark = c.dot if symbol == "dot" else c.cross
    for i in range(n_pairs):
        a = start + step*i
        mark(*_pol(cx, cy, r, a - 6.5))
        mark(*_pol(cx, cy, r, a + 6.5))


# ====================================================================
# PHASE 2 — IONIC DOT-AND-CROSS
#   Metal atom(s) lose electron(s) -> non-metal(s) gain them.
#   Shows BEFORE (atoms, outer electrons) -> arrow -> AFTER (ions in
#   square brackets with charges). Metal electrons = crosses, non-metal
#   electrons = dots, so transferred electrons are visually distinct.
# ====================================================================
# Each compound: metal symbol + outer e-, non-metal symbol + outer e-,
# and the stoichiometry (how many of each ion in the formula unit).
IONIC = {
    "NaCl": {"metal": ("Na", 1, 1), "nonmetal": ("Cl", 7, 1),
             "name": "Sodium chloride, NaCl"},
    "MgO":  {"metal": ("Mg", 2, 1), "nonmetal": ("O", 6, 1),
             "name": "Magnesium oxide, MgO"},
    "MgCl2":{"metal": ("Mg", 2, 1), "nonmetal": ("Cl", 7, 2),
             "name": "Magnesium chloride, MgCl\u2082"},
    "CaCl2":{"metal": ("Ca", 2, 1), "nonmetal": ("Cl", 7, 2),
             "name": "Calcium chloride, CaCl\u2082"},
    "Na2O": {"metal": ("Na", 1, 2), "nonmetal": ("O", 6, 1),
             "name": "Sodium oxide, Na\u2082O"},
    "CaF2": {"metal": ("Ca", 2, 1), "nonmetal": ("F", 7, 2),
             "name": "Calcium fluoride, CaF\u2082"},
    "LiF":  {"metal": ("Li", 1, 1), "nonmetal": ("F", 7, 1),
             "name": "Lithium fluoride, LiF"},
    "K2O":  {"metal": ("K", 1, 2), "nonmetal": ("O", 6, 1),
             "name": "Potassium oxide, K\u2082O"},
}

# inner-shell electron counts so we can show the FULL ion correctly
_INNER = {  # electrons in shells below the valence shell after ion forms
    "Na": 10, "Mg": 10, "Ca": 18, "K": 18, "Li": 2,
    "Cl": 10, "O": 2, "F": 2,
}
# how many electrons the ion's OUTER (shown) shell has after transfer
_ION_OUTER = {"Na": 8, "Mg": 8, "Ca": 8, "K": 8, "Li": 2,
              "Cl": 8, "O": 8, "F": 8}


def _draw_atom(c, cx, cy, symbol, n_outer, fill, sym="dot", r=78,
               full_inner=False):
    """Outer-shell atom: nucleus + one shell + n_outer electrons spread
    evenly. Used for the BEFORE atoms and AFTER ions."""
    c.shell(cx, cy, r)
    mark = c.dot if sym == "dot" else c.cross
    for i in range(n_outer):
        ang = -90 + i * (360 / max(n_outer, 1))
        mark(*_pol(cx, cy, r, ang))
    nr = 30 if symbol not in ("H",) else 23
    c.nucleus(cx, cy, symbol, fill, nr)


def ionic_dotcross(formula):
    """SVG for the ionic dot-and-cross: before atoms -> ions w/ charges.
    Each ion gets its own square brackets + superscript charge. Stacks of
    identical ions are spaced so brackets/labels never collide."""
    if formula not in IONIC:
        raise KeyError(
            f"'{formula}' not in ionic table. Available: "
            f"{', '.join(IONIC)}. Ask to add it.")
    d = IONIC[formula]
    msym, mout, mn = d["metal"]
    nsym, nout, nn = d["nonmetal"]

    nmax = max(mn, nn)
    R = 78 if nmax == 1 else 62          # shrink shells when stacking
    pitch = 2*R + 110                    # vertical gap between stacked ions
    W = 1560
    H = 530 + (nmax - 1) * pitch
    c = Canvas(W, H)
    c.label(W/2, 70, d["name"], 40, "bold")

    cy = 215 + ((nmax - 1) * pitch) / 2 + 40
    metal_fill = STYLE["h_fill"]
    nm_fill = STYLE["nm_fill"]

    def stack_y(n, i):
        if n == 1:
            return cy
        return cy - (n-1)*pitch/2 + i*pitch

    nuc_r = 28 if R < 78 else 30

    # ---------- BEFORE: atoms ----------
    bx_metal, bx_nm = 165, 475
    for i in range(mn):
        y = stack_y(mn, i)
        c.label(bx_metal, y - R - 24, f"{msym} atom", 24)
        c.shell(bx_metal, y, R)
        _spread_marks(c, bx_metal, y, R, mout, "cross")
        c.nucleus(bx_metal, y, msym, metal_fill, nuc_r)
    for i in range(nn):
        y = stack_y(nn, i)
        c.label(bx_nm, y - R - 24, f"{nsym} atom", 24)
        c.shell(bx_nm, y, R)
        _spread_marks(c, bx_nm, y, R, nout, "dot")
        c.nucleus(bx_nm, y, nsym, nm_fill, nuc_r)

    # ---------- transfer arrow ----------
    c.arrow(690, cy, 830, cy)
    c.label(760, cy - 34, "electron", 22)
    c.label(760, cy - 10, "transfer", 22)

    # ---------- AFTER: ions in brackets ----------
    mcharge = mout if mout <= 3 else mout - 8
    ncharge = nout - 8
    ax_metal, ax_nm = 1075, 1385

    def brackets(cx, cyc, r, charge):
        bw = r + 26
        top = cyc - bw
        ear = 13
        c.S.append(
            f'<path d="M{cx-bw} {top} h{-ear} v{2*bw} h{ear}" '
            f'stroke="{STYLE["stroke"]}" stroke-width="2.5" fill="none"/>')
        c.S.append(
            f'<path d="M{cx+bw} {top} h{ear} v{2*bw} h{-ear}" '
            f'stroke="{STYLE["stroke"]}" stroke-width="2.5" fill="none"/>')
        c.label(cx + bw + 34, top + 30, _sup(charge), 36, "bold")

    for i in range(mn):
        y = stack_y(mn, i)
        c.label(ax_metal, y - R - 48, f"{msym}{_sup(mcharge)} ion", 24)
        c.shell(ax_metal, y, R)
        # metal ion: full stable outer shell (8, or 2 for Li/Be-like)
        ion_outer = 2 if msym in ("Li",) else 8
        _spread_marks(c, ax_metal, y, R, ion_outer, "dot")
        c.nucleus(ax_metal, y, msym, metal_fill, nuc_r)
        brackets(ax_metal, y, R, mcharge)
    for i in range(nn):
        y = stack_y(nn, i)
        c.label(ax_nm, y - R - 48, f"{nsym}{_sup(ncharge)} ion", 24)
        c.shell(ax_nm, y, R)
        gained = -ncharge
        own = nout
        # interleave: own electrons (dots) then gained (crosses) fill the
        # remaining octet slots — evenly spaced around the 8 positions
        for k in range(own):
            c.dot(*_pol(ax_nm, y, R, -90 + k*(360/8)))
        for k in range(gained):
            c.cross(*_pol(ax_nm, y, R, -90 + (own+k)*(360/8)))
        c.nucleus(ax_nm, y, nsym, nm_fill, nuc_r)
        brackets(ax_nm, y, R, ncharge)

    return c.svg()


def _spread_marks(c, cx, cy, r, n, sym):
    """Evenly space n electrons (dot/cross) around a shell, starting top."""
    mark = c.dot if sym == "dot" else c.cross
    for i in range(n):
        mark(*_pol(cx, cy, r, -90 + i*(360/max(n, 1))))


def _sup(charge):
    """Superscript charge string e.g. 2+ -> superscript-2 plus, - -> minus."""
    if charge == 0:
        return ""
    supdig = {"1": "\u00b9", "2": "\u00b2", "3": "\u00b3", "4": "\u2074"}
    mag = "" if abs(charge) == 1 else supdig.get(str(abs(charge)),
                                                 str(abs(charge)))
    return mag + ("\u207a" if charge > 0 else "\u207b")


# ====================================================================
# PHASE 2 — METALLIC BONDING
#   Regular lattice of positive ions in a 'sea' of delocalised
#   electrons (small crosses scattered between ions).
# ====================================================================
def metallic_bonding(metal="Cu", rows=3, cols=4):
    """SVG: lattice of positive metal ions + delocalised electron sea."""
    W, H = 1100, 760
    c = Canvas(W, H)
    c.label(W/2, 64, f"Metallic bonding \u2014 {metal}", 40, "bold")

    x0, y0 = 230, 200
    dx, dy = 200, 175
    ion_r = 46

    # delocalised electron sea: crosses scattered on a jittered grid
    import random
    random.seed(42)
    for gx in range(cols + 1):
        for gy in range(rows + 1):
            ex = x0 + gx*dx - dx/2 + random.uniform(-26, 26)
            ey = y0 + gy*dy - dy/2 + random.uniform(-22, 22)
            if W*0.07 < ex < W*0.93 and 110 < ey < H - 80:
                c.cross(ex, ey)

    # positive ions
    for r in range(rows):
        for col in range(cols):
            cx = x0 + col*dx
            cy = y0 + r*dy
            c.S.append(
                f'<circle cx="{cx}" cy="{cy}" r="{ion_r}" '
                f'fill="{STYLE["h_fill"]}" stroke="{STYLE["stroke"]}" '
                f'stroke-width="2"/>')
            c.label(cx, cy + 9, f"{metal}", 26, "bold")
            c.label(cx + ion_r - 4, cy - ion_r + 14, "+", 24, "bold")

    # legend
    ly = H - 46
    c.cross(W/2 - 220, ly)
    c.label(W/2 - 70, ly + 7, "= delocalised electrons", 24, anchor="middle")
    c.S.append(
        f'<circle cx="{W/2+120}" cy="{ly}" r="18" fill="{STYLE["h_fill"]}" '
        f'stroke="{STYLE["stroke"]}" stroke-width="2"/>')
    c.label(W/2 + 235, ly + 7, "= positive metal ions", 24, anchor="middle")
    return c.svg()


# ====================================================================
# PHASE 3 — GIANT STRUCTURES & CARBON ALLOTROPES
#   Bond/atom primitives + builders for: simple molecular, giant ionic
#   lattice, polymers, diamond, graphite, graphene, silicon dioxide,
#   buckminsterfullerene (C60), carbon nanotube.
#   Each builder optionally annotates the property explanation AQA
#   examines (conductivity, melting point, hardness).
# ====================================================================
def _bond(c, x1, y1, x2, y2, w=3):
    c.S.append(
        f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
        f'stroke="{STYLE["stroke"]}" stroke-width="{w}" '
        f'stroke-linecap="round"/>')


def _ball(c, x, y, r, fill, txt=None, fs=22):
    c.S.append(
        f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{fill}" '
        f'stroke="{STYLE["stroke"]}" stroke-width="2"/>')
    if txt:
        c.S.append(
            f'<text x="{x:.1f}" y="{y+fs*0.34:.1f}" '
            f'font-family="{STYLE["font"]}" font-size="{fs}" '
            f'fill="{STYLE["label"]}" text-anchor="middle" '
            f'font-weight="bold">{txt}</text>')


def _note(c, W, H, lines, max_chars=78):
    """Property explanation strip along the bottom (AQA exam framing).
    Long lines auto-wrap so text never overflows the canvas width."""
    wrapped = []
    for ln in lines:
        words = ln.split()
        cur = ""
        for w in words:
            if len(cur) + len(w) + 1 <= max_chars:
                cur = (cur + " " + w).strip()
            else:
                wrapped.append(cur); cur = w
        if cur:
            wrapped.append(cur)
    y = H - 28 - 25*(len(wrapped)-1)
    for ln in wrapped:
        c.label(W/2, y, ln, 21, anchor="middle")
        y += 25


def _hex_pts(cx, cy, s):
    """Pointy-top hexagon vertices."""
    return [(cx + s*math.cos(math.radians(60*i - 90)),
             cy + s*math.sin(math.radians(60*i - 90))) for i in range(6)]


# ---- simple molecular (e.g. iodine / water as a lattice of molecules) --
def simple_molecular(name="Iodine, I\u2082"):
    W, H = 1040, 760
    c = Canvas(W, H)
    c.label(W/2, 60, f"Simple molecular \u2014 {name}", 36, "bold")
    positions = [(300, 230), (620, 215), (790, 360),
                 (360, 430), (660, 450), (500, 320)]
    # weak intermolecular forces first (so bonds/atoms sit on top)
    pairs = [(0,5),(5,1),(1,2),(5,4),(3,4),(0,3),(4,2)]
    for a,b in pairs:
        x1,y1 = positions[a]; x2,y2 = positions[b]
        c.S.append(
            f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" '
            f'stroke="{STYLE["muted"]}" stroke-width="2" '
            f'stroke-dasharray="6 7"/>')
    for (x, y) in positions:
        _bond(c, x-32, y, x+32, y, 5)
        _ball(c, x-32, y, 28, STYLE["nm_fill"], "I", 18)
        _ball(c, x+32, y, 28, STYLE["nm_fill"], "I", 18)
    c.label(W/2, H-140,
            "Solid line = strong covalent bond within each molecule",
            22, anchor="middle")
    c.label(W/2, H-112,
            "Dashed line = weak intermolecular forces between molecules",
            22, anchor="middle")
    _note(c, W, H, ["Low melting and boiling point: only the weak forces "
                    "between molecules are overcome, not the strong "
                    "covalent bonds.",
                    "Does not conduct electricity \u2014 no free electrons "
                    "or ions."])
    return c.svg()


# ---- giant ionic lattice (NaCl 3D-ish) ---------------------------------
def giant_ionic_lattice(cation="Na", anion="Cl"):
    W, H = 1040, 880
    c = Canvas(W, H)
    c.label(W/2, 64, f"Giant ionic lattice \u2014 {cation}{anion}", 38, "bold")
    n = 4
    sp = 150
    ox, oy = 250, 180
    sk = 0.5            # 3D skew
    r = 34

    def proj(i, j, k):
        x = ox + i*sp + k*sp*sk
        y = oy + j*sp + k*sp*sk*0.6
        return x, y
    # draw back-to-front for correct overlap
    for k in range(2):
        for j in range(n):
            for i in range(n):
                if (i+j+k) % 2 == 0:
                    fill, lab = STYLE["h_fill"], f"{cation}\u207a"
                else:
                    fill, lab = STYLE["nm_fill"], f"{anion}\u207b"
                x, y = proj(i, j, k)
                # connecting rods to neighbours
                if i < n-1:
                    x2,y2 = proj(i+1,j,k); _bond(c,x,y,x2,y2,2)
                if j < n-1:
                    x2,y2 = proj(i,j+1,k); _bond(c,x,y,x2,y2,2)
                if k < 1:
                    x2,y2 = proj(i,j,k+1); _bond(c,x,y,x2,y2,2)
    for k in range(2):
        for j in range(n):
            for i in range(n):
                if (i+j+k) % 2 == 0:
                    fill, lab = STYLE["h_fill"], f"{cation}\u207a"
                else:
                    fill, lab = STYLE["nm_fill"], f"{anion}\u207b"
                x, y = proj(i, j, k)
                _ball(c, x, y, r, fill, lab, 20)
    _note(c, W, H, ["Giant lattice of oppositely charged ions held by "
                    "strong electrostatic forces in all directions.",
                    "High melting point; conducts when molten or "
                    "dissolved (ions free to move), not when solid."])
    return c.svg()


# ---- addition polymer --------------------------------------------------
def polymer(monomer="ethene", n_units=3):
    W, H = 1180, 760
    c = Canvas(W, H)
    c.label(W/2, 64, "Addition polymer \u2014 poly(ethene)", 38, "bold")
    y = 300
    x = 150
    seg = 250
    c.label(W/2, 150, "\u2014 repeating unit shown in brackets, n = many \u2014",
            24, anchor="middle")
    for u in range(n_units):
        cx = x + u*seg
        # carbon backbone (two C per unit)
        _bond(c, cx, y, cx+seg, y, 4)
        for dxc in (cx+seg*0.28, cx+seg*0.72):
            _ball(c, dxc, y, 30, STYLE["nm_fill"], "C", 22)
            _bond(c, dxc, y, dxc, y-70, 3)   # H up
            _bond(c, dxc, y, dxc, y+70, 3)   # H down
            _ball(c, dxc, y-70, 20, STYLE["h_fill"], "H", 16)
            _ball(c, dxc, y+70, 20, STYLE["h_fill"], "H", 16)
    # bracket the middle repeat unit
    bx1, bx2 = x+seg*0.95, x+seg*1.95
    for bx, d in ((bx1,-1),(bx2,1)):
        c.S.append(
            f'<path d="M{bx} {y-150} h{14*d} v300 h{-14*d}" '
            f'stroke="{STYLE["stroke"]}" stroke-width="3" fill="none"/>')
    c.label(bx2+44, y+150, "n", 30, "bold")
    _note(c, W, H, ["Many small monomers (ethene) join to form one long "
                    "polymer chain \u2014 addition polymerisation.",
                    "Strong covalent C\u2013C backbone; weak forces between "
                    "chains \u2192 flexible, low melting point."])
    return c.svg()


# ---- diamond -----------------------------------------------------------
def diamond():
    W, H = 1000, 820
    c = Canvas(W, H)
    c.label(W/2, 64, "Diamond \u2014 giant covalent", 38, "bold")
    r = 26
    # tetrahedral repeating network, drawn as a 2D projection
    nodes = {}
    def add(idn, x, y): nodes[idn] = (x, y)
    add("c", 500, 380)
    add("a", 500, 230)
    add("b", 360, 470)
    add("d", 640, 470)
    add("e", 500, 530)
    # second-shell carbons
    add("a1", 500, 110); add("b1", 250, 540); add("d1", 750, 540)
    add("e1", 360, 620); add("e2", 640, 620)
    bonds = [("c","a"),("c","b"),("c","d"),("c","e"),
             ("a","a1"),("b","b1"),("d","d1"),("e","e1"),("e","e2"),
             ("b","e1"),("d","e2")]
    for u,v in bonds:
        x1,y1 = nodes[u]; x2,y2 = nodes[v]; _bond(c,x1,y1,x2,y2,3)
    for (x,y) in nodes.values():
        _ball(c, x, y, r, STYLE["nm_fill"], "C", 18)
    c.label(W/2, H-150, "Each carbon forms 4 strong covalent bonds",
            24, anchor="middle")
    _note(c, W, H, ["Giant covalent: every C bonded to 4 others in a rigid "
                    "3D network \u2192 very hard, very high melting point.",
                    "No free electrons \u2192 does not conduct electricity."])
    return c.svg()


# ---- graphite ----------------------------------------------------------
def graphite():
    W, H = 1180, 860
    c = Canvas(W, H)
    c.label(W/2, 60, "Graphite \u2014 layered giant covalent", 38, "bold")
    s = 46
    def layer(x0, y0):
        centres = [(x0 + i*s*math.sqrt(3), y0) for i in range(5)]
        seen = {}
        for (hx, hy) in centres:
            pts = _hex_pts(hx, hy, s)
            for i in range(6):
                x1,y1 = pts[i]; x2,y2 = pts[(i+1)%6]
                _bond(c, x1,y1,x2,y2, 3)
            for p in pts:
                seen[(round(p[0],1),round(p[1],1))] = p
        for p in seen.values():
            _ball(c, p[0], p[1], 11, STYLE["nm_fill"])
        return centres[0], centres[-1]

    layer_y = [200, 380, 560]
    layer_x = [250, 210, 170]
    for lx, ly in zip(layer_x, layer_y):
        layer(lx, ly)
        c.label(lx - 95, ly, "layer", 22, anchor="middle")
    # weak interlayer forces — vertical dashed connectors between layers
    for col in range(3):
        bx = 360 + col*230
        for a, b in ((0,1),(1,2)):
            c.S.append(
                f'<line x1="{bx}" y1="{layer_y[a]+40}" '
                f'x2="{bx-40}" y2="{layer_y[b]-40}" '
                f'stroke="{STYLE["muted"]}" stroke-width="2" '
                f'stroke-dasharray="5 7"/>')
    c.label(W-170, 380, "weak forces", 21, anchor="middle")
    c.label(W-170, 405, "between layers", 21, anchor="middle")
    _note(c, W, H, ["Each carbon is bonded to only 3 others, leaving 1 "
                    "delocalised electron per atom \u2014 so graphite "
                    "conducts electricity.",
                    "Layers slide over each other because forces between "
                    "layers are weak \u2014 making graphite soft and "
                    "slippery (a good lubricant)."])
    return c.svg()


# ---- graphene ----------------------------------------------------------
def graphene():
    W, H = 1100, 680
    c = Canvas(W, H)
    c.label(W/2, 64, "Graphene \u2014 single layer", 38, "bold")
    s = 58
    rows, cols = 3, 5
    pts_seen = {}
    def key(x,y): return (round(x,1), round(y,1))
    for r in range(rows):
        for col in range(cols):
            cx = 230 + col*s*math.sqrt(3) + (r%2)*(s*math.sqrt(3)/2)
            cy = 230 + r*s*1.5
            pts = _hex_pts(cx, cy, s)
            for i in range(6):
                x1,y1 = pts[i]; x2,y2 = pts[(i+1)%6]
                _bond(c, x1,y1,x2,y2, 3)
            for p in pts: pts_seen[key(*p)] = p
    for p in pts_seen.values():
        _ball(c, p[0], p[1], 12, STYLE["nm_fill"])
    _note(c, W, H, ["A single layer of graphite: one sheet of hexagonally "
                    "arranged carbon atoms, one atom thick.",
                    "Strong, light, conducts electricity (delocalised "
                    "electrons) \u2014 used in electronics & composites."])
    return c.svg()


# ---- silicon dioxide ---------------------------------------------------
def silicon_dioxide():
    W, H = 1080, 780
    c = Canvas(W, H)
    c.label(W/2, 60, "Silicon dioxide, SiO\u2082 \u2014 giant covalent",
            34, "bold")
    si = STYLE["h_fill"]; oxf = STYLE["nm_fill"]
    # grid of Si centres; each Si bonded to 4 O; O bridge adjacent Si
    si_pos = [(330,260),(620,260),(910,260),
              (330,500),(620,500),(910,500)]
    sp = 290
    for (sx, sy) in si_pos:
        # 4 oxygens around each Si (up, down, left, right) at half-spacing
        for dx, dy in [(-sp/2,0),(sp/2,0),(0,-sp/3),(0,sp/3)]:
            ox_, oy_ = sx+dx, sy+dy
            if 120 < ox_ < W-120 and 150 < oy_ < 560:
                _bond(c, sx, sy, ox_, oy_, 3)
    # draw O atoms (dedup by rounded position)
    seen = {}
    for (sx, sy) in si_pos:
        for dx, dy in [(-sp/2,0),(sp/2,0),(0,-sp/3),(0,sp/3)]:
            ox_, oy_ = sx+dx, sy+dy
            if 120 < ox_ < W-120 and 150 < oy_ < 560:
                seen[(round(ox_),round(oy_))] = (ox_,oy_)
    for (ox_,oy_) in seen.values():
        _ball(c, ox_, oy_, 21, oxf, "O", 15)
    for (sx, sy) in si_pos:
        _ball(c, sx, sy, 27, si, "Si", 16)
    c.label(W/2, H-150,
            "Each Si bonded to 4 O atoms; each O bonded to 2 Si "
            "\u2014 a giant network",
            22, anchor="middle")
    _note(c, W, H, ["A giant covalent network like diamond: very high "
                    "melting point, very hard, and does not conduct "
                    "electricity."])
    return c.svg()


# ---- buckminsterfullerene C60 -----------------------------------------
def fullerene():
    W, H = 940, 900
    c = Canvas(W, H)
    c.label(W/2, 60, "Buckminsterfullerene, C\u2086\u2080", 38, "bold")
    cx, cy = W/2, 440
    R1, R2, R3 = 290, 200, 95
    # sphere outline hint
    c.S.append(
        f'<circle cx="{cx}" cy="{cy}" r="{R1+8}" fill="none" '
        f'stroke="{STYLE["muted"]}" stroke-width="1.5" '
        f'stroke-dasharray="3 9"/>')
    ring1 = [(cx + R1*math.cos(math.radians(30*i-90)),
              cy + R1*math.sin(math.radians(30*i-90))) for i in range(12)]
    ring2 = [(cx + R2*math.cos(math.radians(30*i-90+15)),
              cy + R2*math.sin(math.radians(30*i-90+15))) for i in range(12)]
    ring3 = [(cx + R3*math.cos(math.radians(60*i-90)),
              cy + R3*math.sin(math.radians(60*i-90))) for i in range(6)]
    # bonds: ring1 perimeter, ring1->ring2 spokes, ring2 perimeter,
    # ring2->ring3 spokes, ring3 perimeter
    for i in range(12):
        _bond(c, *ring1[i], *ring1[(i+1)%12], w=3)
        _bond(c, *ring1[i], *ring2[i], w=2.5)
    for i in range(12):
        _bond(c, *ring2[i], *ring2[(i+1)%12], w=2.5)
    for i in range(12):
        _bond(c, *ring2[i], *ring3[i % 6], w=2)
    for i in range(6):
        _bond(c, *ring3[i], *ring3[(i+1)%6], w=2.5)
    for p in ring1 + ring2 + ring3:
        _ball(c, p[0], p[1], 11, STYLE["nm_fill"])
    _note(c, W, H, ["A hollow ball of 60 carbon atoms arranged in hexagons "
                    "and pentagons. It is simple molecular \u2014 weak "
                    "forces between molecules.",
                    "Used in drug delivery, as lubricants, and as "
                    "catalysts."])
    return c.svg()


# ---- carbon nanotube ---------------------------------------------------
def nanotube():
    W, H = 1180, 620
    c = Canvas(W, H)
    c.label(W/2, 64, "Carbon nanotube", 38, "bold")
    cx, cy = W/2, 330
    L, Rx, Ry = 760, 70, 150
    # cylinder body
    c.S.append(
        f'<path d="M{cx-L/2} {cy-Ry} L{cx+L/2} {cy-Ry} '
        f'A{Rx} {Ry} 0 0 1 {cx+L/2} {cy+Ry} L{cx-L/2} {cy+Ry} '
        f'A{Rx} {Ry} 0 0 0 {cx-L/2} {cy-Ry} Z" '
        f'fill="none" stroke="{STYLE["stroke"]}" stroke-width="2.5"/>')
    # end ellipse
    c.S.append(
        f'<ellipse cx="{cx-L/2}" cy="{cy}" rx="{Rx}" ry="{Ry}" '
        f'fill="none" stroke="{STYLE["stroke"]}" stroke-width="2.5" '
        f'stroke-dasharray="4 6"/>')
    # hexagonal mesh hint on the surface
    s = 40
    for col in range(9):
        for row in range(4):
            hx = cx - L/2 + 70 + col*s*1.5
            hy = cy - 90 + row*s*1.1 + (col%2)*(s*0.55)
            if hx < cx + L/2 - 30:
                pts = _hex_pts(hx, hy, s*0.6)
                for i in range(6):
                    x1,y1=pts[i]; x2,y2=pts[(i+1)%6]
                    _bond(c,x1,y1,x2,y2,1.5)
    _note(c, W, H, ["A cylinder of hexagonally bonded carbon \u2014 huge "
                    "length:diameter ratio.",
                    "Very strong, conducts electricity \u2192 electronics, "
                    "high-strength composites."])
    return c.svg()


# ====================================================================
# PHASE 4 — ELECTRONIC CONFIGURATION (any element, Z = 1..20)
#   Nucleus (protons + neutrons) with electron shells filled 2,8,8,2.
#   AQA covers H..Ca. Electrons drawn in pairs around each shell.
# ====================================================================
_ELEMENTS = {
    1:("H","Hydrogen",0), 2:("He","Helium",2), 3:("Li","Lithium",4),
    4:("Be","Beryllium",5), 5:("B","Boron",6), 6:("C","Carbon",6),
    7:("N","Nitrogen",7), 8:("O","Oxygen",8), 9:("F","Fluorine",10),
    10:("Ne","Neon",10), 11:("Na","Sodium",12), 12:("Mg","Magnesium",12),
    13:("Al","Aluminium",14), 14:("Si","Silicon",14), 15:("P","Phosphorus",16),
    16:("S","Sulfur",16), 17:("Cl","Chlorine",18), 18:("Ar","Argon",22),
    19:("K","Potassium",20), 20:("Ca","Calcium",20),
}


def _config(z):
    """Return shell occupancy list for atomic number z (2,8,8,2 rule)."""
    caps = [2, 8, 8, 2]
    left, shells = z, []
    for cap in caps:
        if left <= 0:
            break
        shells.append(min(cap, left))
        left -= min(cap, left)
    return shells


def electronic_configuration(symbol):
    """SVG: electronic configuration (shell diagram) for an element.
    Accepts a symbol ('Mg') or name ('Magnesium')."""
    key = None
    for z,(sym,name,_) in _ELEMENTS.items():
        if symbol.strip().lower() in (sym.lower(), name.lower()) \
           or symbol.strip() == str(z):
            key = z; break
    if key is None:
        raise KeyError(
            f"'{symbol}' not found. AQA range is H..Ca (Z=1..20). "
            f"Ask to extend if needed.")
    z = key
    sym, name, neutrons = _ELEMENTS[z]
    shells = _config(z)

    n_shells = len(shells)
    W = 900
    H = 820 if n_shells <= 3 else 960
    c = Canvas(W, H)
    c.label(W/2, 62, f"{name}  ({sym})", 40, "bold")
    cx = W/2
    cy = 400 if n_shells <= 3 else 470
    radii = [70, 130, 195, 255][:n_shells]

    # shells
    for r in radii:
        c.shell(cx, cy, r)

    # electrons — drawn in PAIRS, evenly spaced, starting at the top
    for si, count in enumerate(shells):
        r = radii[si]
        n_pairs = (count + 1) // 2
        # angular position of each pair centre
        for p in range(n_pairs):
            base = -90 + p * (360 / n_pairs)
            in_this_pair = 2 if (p*2 + 2) <= count else (count - p*2)
            if in_this_pair == 2:
                for off in (-7, 7):
                    c.dot(*_pol(cx, cy, r, base + off))
            else:
                c.dot(*_pol(cx, cy, r, base))

    # nucleus with proton / neutron count
    nr = 46
    c.S.append(
        f'<circle cx="{cx}" cy="{cy}" r="{nr}" fill="{STYLE["h_fill"]}" '
        f'stroke="{STYLE["stroke"]}" stroke-width="2"/>')
    c.S.append(
        f'<text x="{cx}" y="{cy-6}" font-family="{STYLE["font"]}" '
        f'font-size="22" fill="{STYLE["label"]}" text-anchor="middle" '
        f'font-weight="bold">{z}p</text>')
    c.S.append(
        f'<text x="{cx}" y="{cy+22}" font-family="{STYLE["font"]}" '
        f'font-size="22" fill="{STYLE["label"]}" text-anchor="middle" '
        f'font-weight="bold">{neutrons}n</text>')

    # configuration caption + AQA framing
    cfg = ",".join(str(s) for s in shells)
    c.label(W/2, H-150, f"Electronic configuration:  {cfg}", 28, "bold")
    period = n_shells
    noble = z in (2, 10, 18)
    group = "0" if noble else str(shells[-1])
    _note(c, W, H, [f"{name} has {z} electrons arranged {cfg}. "
                    f"Outer shell: {shells[-1]} \u2192 Group {group}, "
                    f"Period {period}.",
                    "Group = number of outer-shell electrons "
                    "(noble gases are Group 0); "
                    "Period = number of occupied shells."])
    return c.svg()


# ====================================================================
# PHASE 5 — ELECTROLYSIS CELL
#   Beaker + electrolyte + two inert electrodes + power supply.
#   Labelled cathode (-) and anode (+), ion-movement arrows, and the
#   products / half-equation callouts. Molten and aqueous variants.
# ====================================================================
ELECTROLYSIS = {
    "molten_PbBr2": {
        "name": "Molten lead bromide, PbBr\u2082",
        "type": "molten",
        "electrolyte": "Molten PbBr\u2082",
        "cathode": ("Pb", "Lead metal forms at the (\u2013) cathode",
                    "Pb\u00b2\u207a + 2e\u207b \u2192 Pb"),
        "anode": ("Br\u2082", "Bromine gas forms at the (+) anode",
                  "2Br\u207b \u2192 Br\u2082 + 2e\u207b"),
        "cat_ion": "Pb\u00b2\u207a", "an_ion": "Br\u207b",
    },
    "molten_Al2O3": {
        "name": "Molten aluminium oxide, Al\u2082O\u2083",
        "type": "molten",
        "electrolyte": "Molten Al\u2082O\u2083 (in cryolite)",
        "cathode": ("Al", "Aluminium forms at the (\u2013) cathode",
                    "Al\u00b3\u207a + 3e\u207b \u2192 Al"),
        "anode": ("O\u2082", "Oxygen forms at the (+) anode",
                  "2O\u00b2\u207b \u2192 O\u2082 + 4e\u207b"),
        "cat_ion": "Al\u00b3\u207a", "an_ion": "O\u00b2\u207b",
    },
    "aqueous_CuSO4": {
        "name": "Copper sulfate solution, CuSO\u2084(aq)",
        "type": "aqueous",
        "electrolyte": "CuSO\u2084 solution",
        "cathode": ("Cu", "Copper deposits at the (\u2013) cathode",
                    "Cu\u00b2\u207a + 2e\u207b \u2192 Cu"),
        "anode": ("O\u2082", "Oxygen forms at the (+) anode",
                  "4OH\u207b \u2192 O\u2082 + 2H\u2082O + 4e\u207b"),
        "cat_ion": "Cu\u00b2\u207a", "an_ion": "OH\u207b",
    },
    "aqueous_NaCl": {
        "name": "Sodium chloride solution, NaCl(aq)",
        "type": "aqueous",
        "electrolyte": "NaCl solution (brine)",
        "cathode": ("H\u2082", "Hydrogen forms at the (\u2013) cathode",
                    "2H\u207a + 2e\u207b \u2192 H\u2082"),
        "anode": ("Cl\u2082", "Chlorine forms at the (+) anode",
                  "2Cl\u207b \u2192 Cl\u2082 + 2e\u207b"),
        "cat_ion": "H\u207a", "an_ion": "Cl\u207b",
    },
}


def _cell_symbol(c, x, y):
    """Battery / d.c. power supply symbol (long line +, short line -)."""
    c.S.append(
        f'<line x1="{x-22}" y1="{y-26}" x2="{x-22}" y2="{y+26}" '
        f'stroke="{STYLE["stroke"]}" stroke-width="3"/>')       # long +
    c.S.append(
        f'<line x1="{x+22}" y1="{y-14}" x2="{x+22}" y2="{y+14}" '
        f'stroke="{STYLE["stroke"]}" stroke-width="6"/>')       # short -
    c.label(x-22, y-40, "+", 30, "bold")
    c.label(x+22, y-40, "\u2013", 30, "bold")


def electrolysis(setup="molten_PbBr2"):
    """SVG of a labelled electrolysis cell for the named setup."""
    if setup not in ELECTROLYSIS:
        raise KeyError(
            f"'{setup}' not in electrolysis table. Available: "
            f"{', '.join(ELECTROLYSIS)}. Ask to add it.")
    d = ELECTROLYSIS[setup]
    W, H = 1180, 900
    c = Canvas(W, H)
    c.label(W/2, 58, f"Electrolysis of {d['name']}", 34, "bold")

    # ---- power supply + circuit wires ----
    psx, psy = W/2, 165
    _cell_symbol(c, psx, psy)
    c.label(psx, psy + 58, "d.c. power supply", 22, anchor="middle")

    # beaker geometry
    bx, by, bw, bh = 340, 360, 500, 360      # x,y(top),width,height
    liq_top = by + 70
    # electrode x positions
    cath_x = bx + 130          # cathode (-) wired to + side? No: cathode to -.
    an_x   = bx + bw - 130     # anode (+)

    # wires: power supply (+) -> anode ; (-) -> cathode
    # left terminal of supply is +, right is -
    plus_x, minus_x = psx - 22, psx + 22
    # + to anode
    c.S.append(
        f'<polyline points="{plus_x},{psy+26} {plus_x},{psy+90} '
        f'{an_x},{psy+90} {an_x},{by+20}" fill="none" '
        f'stroke="{STYLE["stroke"]}" stroke-width="3"/>')
    # - to cathode
    c.S.append(
        f'<polyline points="{minus_x},{psy+26} {minus_x},{psy+120} '
        f'{cath_x},{psy+120} {cath_x},{by+20}" fill="none" '
        f'stroke="{STYLE["stroke"]}" stroke-width="3"/>')

    # ---- beaker ----
    c.S.append(
        f'<path d="M{bx} {by} L{bx} {by+bh} Q{bx} {by+bh+24} {bx+24} '
        f'{by+bh+24} L{bx+bw-24} {by+bh+24} Q{bx+bw} {by+bh+24} '
        f'{bx+bw} {by+bh} L{bx+bw} {by}" fill="none" '
        f'stroke="{STYLE["stroke"]}" stroke-width="3"/>')
    # electrolyte fill
    c.S.append(
        f'<path d="M{bx+3} {liq_top} L{bx+3} {by+bh} Q{bx+3} {by+bh+21} '
        f'{bx+24} {by+bh+21} L{bx+bw-24} {by+bh+21} Q{bx+bw-3} {by+bh+21} '
        f'{bx+bw-3} {by+bh} L{bx+bw-3} {liq_top} Z" '
        f'fill="{STYLE["nm_fill"]}" opacity="0.45"/>')
    # ---- electrodes (inert carbon rods) ----
    er_w = 26
    for ex, lab, sign in ((cath_x, "Cathode", "\u2013"),
                          (an_x, "Anode", "+")):
        c.S.append(
            f'<rect x="{ex-er_w/2}" y="{by+18}" width="{er_w}" '
            f'height="{bh-10}" rx="5" fill="{STYLE["stroke"]}" '
            f'opacity="0.78"/>')
        c.label(ex, by - 2, f"{lab} ({sign})", 24, "bold", "middle")
    # 'carbon electrode' note placed in clear space above the liquid,
    # offset outward so it never sits on the rod
    c.label(cath_x - 70, by + 44, "carbon", 18, anchor="middle")
    c.label(an_x + 70, by + 44, "carbon", 18, anchor="middle")

    # ---- product callouts: offset to the OUTER side of each electrode,
    #      in clear electrolyte, never overlapping the rod ----
    cat = d["cathode"]; an = d["anode"]
    c.label(cath_x - 78, liq_top + 95, cat[0], 30, "bold", "middle")
    c.label(an_x + 78, liq_top + 95, an[0], 30, "bold", "middle")

    # ---- ion-movement arrows: each stays in its own half (no crossing) ----
    centre_x = bx + bw/2
    # cation -> cathode (negative electrode). Upper line, left half.
    yc = liq_top + 150
    c.arrow(centre_x - 20, yc, cath_x + 28, yc)
    c.label((centre_x - 20 + cath_x + 28)/2, yc - 22,
            d["cat_ion"], 24, anchor="middle")
    # anion -> anode (positive electrode). Lower line, right half.
    ya = liq_top + 230
    c.arrow(centre_x + 20, ya, an_x - 28, ya)
    c.label((centre_x + 20 + an_x - 28)/2, ya - 22,
            d["an_ion"], 24, anchor="middle")
    # electrolyte name at the very bottom of the liquid, clear of arrows
    c.label(centre_x, by + bh - 18, d["electrolyte"], 22, anchor="middle")

    # ---- half-equation panel (red = copy this) ----
    ey = by + bh + 80
    c.label(W/2, ey, "Half equations  (write these down)", 24, "bold",
            "middle")
    c.S.append(
        f'<text x="{W/2}" y="{ey+40}" font-family="{STYLE["font"]}" '
        f'font-size="26" fill="#C8102E" text-anchor="middle" '
        f'font-weight="bold">Cathode (\u2013):  {cat[2]}</text>')
    c.S.append(
        f'<text x="{W/2}" y="{ey+78}" font-family="{STYLE["font"]}" '
        f'font-size="26" fill="#C8102E" text-anchor="middle" '
        f'font-weight="bold">Anode (+):  {an[2]}</text>')
    return c.svg()


# ====================================================================
# PHASE 6 — REACTIVITY LADDER, pH SCALE, CONSERVATION OF MASS,
#           GAS-SYRINGE SETUP
# ====================================================================

# ---- reactivity series ladder -----------------------------------------
_REACTIVITY = [
    ("Potassium", "K"), ("Sodium", "Na"), ("Lithium", "Li"),
    ("Calcium", "Ca"), ("Magnesium", "Mg"), ("Carbon", "C"),
    ("Zinc", "Zn"), ("Iron", "Fe"), ("Hydrogen", "H"),
    ("Copper", "Cu"), ("Silver", "Ag"), ("Gold", "Au"),
]


def reactivity_series():
    """SVG: vertical reactivity-series ladder, most reactive at top.
    Carbon and Hydrogen marked as non-metal reference points."""
    W, H = 1000, 980
    c = Canvas(W, H)
    c.label(W/2, 60, "The Reactivity Series", 40, "bold")
    n = len(_REACTIVITY)
    top, bot = 130, H - 150
    rung_h = (bot - top) / n
    bx = W/2 - 210
    for i, (name, sym) in enumerate(_REACTIVITY):
        y = top + i*rung_h
        ref = sym in ("C", "H")
        fill = "#FBBF24" if ref else STYLE["nm_fill"]
        c.S.append(
            f'<rect x="{bx}" y="{y:.1f}" width="420" '
            f'height="{rung_h-8:.1f}" rx="8" fill="{fill}" '
            f'stroke="{STYLE["stroke"]}" stroke-width="2"/>')
        txt = f"{name}  ({sym})" + ("   \u2013 non-metal" if ref else "")
        c.label(bx+210, y + rung_h/2 + 2, txt, 25, "bold", "middle")
    # reactivity arrow up the left side
    ax = bx - 70
    c.S.append(
        f'<line x1="{ax}" y1="{bot-10}" x2="{ax}" y2="{top+6}" '
        f'stroke="{STYLE["arrow"]}" stroke-width="7" '
        f'stroke-linecap="round"/>')
    c.S.append(
        f'<polygon points="{ax},{top-14} {ax-13},{top+16} '
        f'{ax+13},{top+16}" fill="{STYLE["arrow"]}"/>')
    # vertical "increasing reactivity" label beside the arrow
    c.S.append(
        f'<text x="{ax-34}" y="{(top+bot)/2}" '
        f'font-family="{STYLE["font"]}" font-size="22" '
        f'fill="{STYLE["label"]}" text-anchor="middle" '
        f'transform="rotate(-90 {ax-34} {(top+bot)/2})">'
        f'increasing reactivity</text>')
    _note(c, W, H, ["More reactive metals lose electrons more easily and "
                    "displace less reactive metals from their compounds.",
                    "Carbon and hydrogen are included as reference points "
                    "for extraction and displacement."])
    return c.svg()


# ---- pH scale strip ----------------------------------------------------
def ph_scale():
    """SVG: 0-14 pH scale with acid / neutral / alkali zones."""
    W, H = 1280, 620
    c = Canvas(W, H)
    c.label(W/2, 60, "The pH Scale", 40, "bold")
    x0, x1 = 90, W-90
    y = 230
    bh = 110
    seg = (x1 - x0) / 15
    # colour ramp 0..14 (red->green->purple), kept readable
    ramp = ["#C8102E","#E0431F","#EF6C1A","#F39C12","#E8B713",
            "#C9C61A","#8FBF26","#3FA535","#2E8B57","#2E8B7F",
            "#2C7FB8","#3457A8","#4B3FA8","#6A2FA0","#7A1F90"]
    for i in range(15):
        c.S.append(
            f'<rect x="{x0+i*seg:.1f}" y="{y}" width="{seg+1:.1f}" '
            f'height="{bh}" fill="{ramp[i]}" stroke="{STYLE["stroke"]}" '
            f'stroke-width="1"/>')
        c.S.append(
            f'<text x="{x0+i*seg+seg/2:.1f}" y="{y+bh+34}" '
            f'font-family="{STYLE["font"]}" font-size="26" '
            f'fill="{STYLE["label"]}" text-anchor="middle" '
            f'font-weight="bold">{i}</text>')
    # zone brackets
    def zone(a, b, txt):
        xa, xb = x0+a*seg, x0+b*seg
        c.S.append(
            f'<line x1="{xa}" y1="{y-22}" x2="{xb}" y2="{y-22}" '
            f'stroke="{STYLE["stroke"]}" stroke-width="2"/>')
        c.label((xa+xb)/2, y-34, txt, 24, "bold", "middle")
    zone(0, 7, "ACIDIC")
    zone(7, 8, "")
    zone(8, 15, "ALKALINE")
    c.label(x0+7.5*seg, y-34, "NEUTRAL", 22, "bold", "middle")
    c.label(W/2, y+bh+90,
            "Acids: pH < 7   |   Neutral: pH 7   |   Alkalis: pH > 7",
            26, "bold", "middle")
    _note(c, W, H, ["Lower pH = more acidic (higher H\u207a concentration). "
                    "Higher pH = more alkaline (higher OH\u207b "
                    "concentration).",
                    "Universal indicator shows these colours; a pH probe "
                    "gives an exact value."])
    return c.svg()


# ---- conservation of mass: sealed flask --------------------------------
def conservation_sealed():
    """SVG: sealed conical flask on a balance (mass unchanged)."""
    W, H = 1120, 760
    c = Canvas(W, H)
    c.label(W/2, 60, "Conservation of Mass \u2014 closed system", 36, "bold")
    # two balances: before and after, both reading the same
    def flask(cx, base_y, label):
        # conical flask
        c.S.append(
            f'<path d="M{cx-18} {base_y-150} L{cx-18} {base_y-110} '
            f'L{cx-70} {base_y} L{cx+70} {base_y} L{cx+18} {base_y-110} '
            f'L{cx+18} {base_y-150} Z" fill="{STYLE["nm_fill"]}" '
            f'opacity="0.45" stroke="{STYLE["stroke"]}" '
            f'stroke-width="2.5"/>')
        # stopper (sealed!)
        c.S.append(
            f'<rect x="{cx-22}" y="{base_y-168}" width="44" height="22" '
            f'rx="4" fill="{STYLE["h_fill"]}" stroke="{STYLE["stroke"]}" '
            f'stroke-width="2"/>')
        # liquid
        c.S.append(
            f'<path d="M{cx-52} {base_y-26} L{cx+52} {base_y-26} '
            f'L{cx+70} {base_y} L{cx-70} {base_y} Z" '
            f'fill="{STYLE["arrow"]}" opacity="0.5"/>')
        # balance pan + display
        c.S.append(
            f'<rect x="{cx-110}" y="{base_y+8}" width="220" height="14" '
            f'rx="4" fill="{STYLE["stroke"]}" opacity="0.5"/>')
        c.S.append(
            f'<rect x="{cx-90}" y="{base_y+30}" width="180" height="60" '
            f'rx="8" fill="{STYLE["cream"]}" stroke="{STYLE["stroke"]}" '
            f'stroke-width="2"/>')
        c.label(cx, base_y+70, "120.0 g", 30, "bold", "middle")
        c.label(cx, base_y-200, label, 26, "bold", "middle")

    flask(310, 360, "Before reaction")
    flask(810, 360, "After reaction")
    # equals sign between
    c.label(W/2, 380, "=", 60, "bold", "middle")
    _note(c, W, H, ["In a sealed (closed) container no atoms can enter or "
                    "leave, so the total mass is unchanged by the reaction.",
                    "Mass of reactants = mass of products. Atoms are "
                    "rearranged, never created or destroyed."])
    return c.svg()


# ---- gas-syringe / mass-loss setup -------------------------------------
def gas_syringe():
    """SVG: conical flask + delivery tube + gas syringe to measure gas."""
    W, H = 1200, 720
    c = Canvas(W, H)
    c.label(W/2, 60, "Measuring rate \u2014 gas syringe", 36, "bold")
    # flask
    fx, fy = 330, 470
    c.S.append(
        f'<path d="M{fx-18} {fy-150} L{fx-18} {fy-110} L{fx-80} {fy} '
        f'L{fx+80} {fy} L{fx+18} {fy-110} L{fx+18} {fy-150} Z" '
        f'fill="{STYLE["nm_fill"]}" opacity="0.4" '
        f'stroke="{STYLE["stroke"]}" stroke-width="2.5"/>')
    # reaction mixture
    c.S.append(
        f'<path d="M{fx-58} {fy-30} L{fx+58} {fy-30} L{fx+80} {fy} '
        f'L{fx-80} {fy} Z" fill="{STYLE["arrow"]}" opacity="0.5"/>')
    c.label(fx, fy+34, "acid + metal", 22, "normal", "middle")
    # bung + delivery tube
    c.S.append(
        f'<rect x="{fx-22}" y="{fy-168}" width="44" height="22" rx="4" '
        f'fill="{STYLE["h_fill"]}" stroke="{STYLE["stroke"]}" '
        f'stroke-width="2"/>')
    c.S.append(
        f'<polyline points="{fx},{fy-168} {fx},{fy-230} {fx+260},'
        f'{fy-230} {fx+260},{fy-210}" fill="none" '
        f'stroke="{STYLE["stroke"]}" stroke-width="3"/>')
    # gas syringe (barrel + plunger)
    sx, sy = fx+260, fy-210
    sw, sh = 420, 90
    c.S.append(
        f'<rect x="{sx}" y="{sy}" width="{sw}" height="{sh}" rx="10" '
        f'fill="none" stroke="{STYLE["stroke"]}" stroke-width="2.5"/>')
    # plunger pushed partway out (gas collected)
    pp = sx + sw*0.55
    c.S.append(
        f'<rect x="{sx}" y="{sy+6}" width="{pp-sx}" height="{sh-12}" '
        f'fill="{STYLE["nm_fill"]}" opacity="0.4"/>')
    c.S.append(
        f'<line x1="{pp}" y1="{sy-12}" x2="{pp}" y2="{sy+sh+12}" '
        f'stroke="{STYLE["stroke"]}" stroke-width="3"/>')
    c.S.append(
        f'<line x1="{pp}" y1="{sy+sh/2}" x2="{sx+sw+40}" '
        f'y2="{sy+sh/2}" stroke="{STYLE["stroke"]}" stroke-width="3"/>')
    # scale marks on the barrel
    for k in range(1, 9):
        mx = sx + sw*k/9
        c.S.append(
            f'<line x1="{mx:.0f}" y1="{sy}" x2="{mx:.0f}" y2="{sy+14}" '
            f'stroke="{STYLE["stroke"]}" stroke-width="1.5"/>')
    c.label(sx+sw/2, sy-26, "gas syringe (cm\u00b3 of gas)", 22,
            "bold", "middle")
    c.label(sx + (pp-sx)/2, sy+sh/2+8, "gas", 22, "bold", "middle")
    _note(c, W, H, ["Gas produced pushes the plunger out; the volume is "
                    "read from the syringe scale at set time intervals.",
                    "Steeper graph = faster rate. Rate = volume of gas \u00f7 "
                    "time."])
    return c.svg()


# ====================================================================
# CHEMISTRY P2 — PHASE 1: ORGANIC MOLECULE ENGINE
#   Displayed & skeletal formulae for hydrocarbons and key
#   functional groups: alkanes, alkenes, alcohols, carboxylic acids,
#   esters. Each molecule is a list of carbons with substituents;
#   one engine draws either displayed or skeletal form.
# ====================================================================
# A molecule is defined as a list of carbons. Each carbon is a dict:
#   {"sub": [...], "double_next": bool}
# sub is a list of substituent strings attached to this carbon (other
# than the backbone bonds and any implicit Hs); double_next means the
# bond from this carbon to the next is a double bond.

def _alkane(n):
    """Build a straight-chain alkane CnH(2n+2)."""
    chain = []
    for i in range(n):
        # endpoints have 3 H + 1 backbone; interiors have 2 H + 2 backbone
        h_count = 3 if (i == 0 or i == n-1) else 2
        chain.append({"sub": ["H"] * h_count, "double_next": False})
    return chain


def _alkene(n, pos=1):
    """Straight-chain alkene with C=C between carbons `pos` and `pos+1`
    (1-indexed). CnH2n."""
    chain = []
    for i in range(n):
        # in alkenes, carbons on the C=C have one fewer H
        is_double_end_a = (i == pos - 1)
        is_double_end_b = (i == pos)
        if i == 0 or i == n-1:
            h_count = 3
        else:
            h_count = 2
        if is_double_end_a or is_double_end_b:
            h_count -= 1
        chain.append({"sub": ["H"] * max(h_count, 0),
                      "double_next": (i == pos - 1)})
    return chain


def _alcohol(n, oh_pos=1):
    """Straight-chain alcohol with -OH at carbon `oh_pos` (1-indexed)."""
    chain = _alkane(n)
    # replace one H on that carbon with OH
    target = oh_pos - 1
    if chain[target]["sub"] and "H" in chain[target]["sub"]:
        chain[target]["sub"].remove("H")
    chain[target]["sub"].append("OH")
    return chain


def _carboxylic_acid(n):
    """Straight-chain carboxylic acid CnH2n+1-COOH (n carbons total,
    including the COOH carbon)."""
    chain = _alkane(n)
    # the terminal carbon (last) becomes COOH: replace its 3 H with =O and OH
    last = chain[-1]
    last["sub"] = ["=O", "OH"]
    return chain


def _ester(n_acid, n_alcohol):
    """Methyl/ethyl ester etc. Not implemented as a chain — handled by
    a dedicated drawer below."""
    return None


ORGANIC = {
    # alkanes
    "methane":  {"chain": _alkane(1), "name": "Methane (CH\u2084)"},
    "ethane":   {"chain": _alkane(2), "name": "Ethane (C\u2082H\u2086)"},
    "propane":  {"chain": _alkane(3), "name": "Propane (C\u2083H\u2088)"},
    "butane":   {"chain": _alkane(4), "name": "Butane (C\u2084H\u2081\u2080)"},
    "pentane":  {"chain": _alkane(5), "name": "Pentane (C\u2085H\u2081\u2082)"},
    # alkenes
    "ethene":   {"chain": _alkene(2, 1), "name": "Ethene (C\u2082H\u2084)"},
    "propene":  {"chain": _alkene(3, 1), "name": "Propene (C\u2083H\u2086)"},
    "butene":   {"chain": _alkene(4, 1), "name": "But-1-ene (C\u2084H\u2088)"},
    # alcohols
    "methanol": {"chain": _alcohol(1), "name": "Methanol (CH\u2083OH)"},
    "ethanol":  {"chain": _alcohol(2), "name": "Ethanol (C\u2082H\u2085OH)"},
    "propanol": {"chain": _alcohol(3), "name": "Propan-1-ol "
                                              "(C\u2083H\u2087OH)"},
    # carboxylic acids
    "methanoic_acid": {"chain": _carboxylic_acid(1),
                       "name": "Methanoic acid (HCOOH)"},
    "ethanoic_acid":  {"chain": _carboxylic_acid(2),
                       "name": "Ethanoic acid (CH\u2083COOH)"},
    "propanoic_acid": {"chain": _carboxylic_acid(3),
                       "name": "Propanoic acid (C\u2082H\u2085COOH)"},
}


# ---- Displayed-formula engine ----
def displayed_formula(key, title=None):
    """Draw the displayed formula (every atom + every bond shown)."""
    if key not in ORGANIC:
        raise KeyError(f"'{key}' not in organic table. Available: "
                       f"{', '.join(ORGANIC)}.")
    mol = ORGANIC[key]
    chain = mol["chain"]
    n = len(chain)

    W = max(900, 220 + n * 220)
    H = 560
    c = Canvas(W, H)
    c.label(W/2, 64, title or mol["name"], 38, "bold")

    cy = H/2 + 20
    bond_len = 100
    cspan = 180                  # x-spacing between adjacent carbons
    x0 = (W - (n-1) * cspan) / 2

    ATOM_FS = 36
    BOND_W = 3
    # carbon positions
    xs = [x0 + i*cspan for i in range(n)]

    # ---- backbone bonds first (drawn underneath atoms) ----
    for i in range(n-1):
        x1, x2 = xs[i] + 26, xs[i+1] - 26
        if chain[i]["double_next"]:
            c.S.append(
                f'<line x1="{x1}" y1="{cy-7}" x2="{x2}" y2="{cy-7}" '
                f'stroke="{STYLE["stroke"]}" stroke-width="{BOND_W}"/>')
            c.S.append(
                f'<line x1="{x1}" y1="{cy+7}" x2="{x2}" y2="{cy+7}" '
                f'stroke="{STYLE["stroke"]}" stroke-width="{BOND_W}"/>')
        else:
            c.S.append(
                f'<line x1="{x1}" y1="{cy}" x2="{x2}" y2="{cy}" '
                f'stroke="{STYLE["stroke"]}" stroke-width="{BOND_W}"/>')

    # ---- substituents around each carbon ----
    for i, carbon in enumerate(chain):
        cx = xs[i]
        subs = list(carbon["sub"])
        # choose positions: up first, then down, then any remaining 'side'
        # positions only on terminal carbons (where there isn't a backbone)
        positions = []
        # always allow up and down for each carbon
        used = []
        for s in subs:
            if "up" not in used:
                positions.append(("up", s)); used.append("up")
            elif "down" not in used:
                positions.append(("down", s)); used.append("down")
            else:
                # leftover Hs go to the side (only meaningful for end Cs)
                if i == 0 and "left" not in used:
                    positions.append(("left", s)); used.append("left")
                elif i == n-1 and "right" not in used:
                    positions.append(("right", s)); used.append("right")
                else:
                    # extra H beyond available slots — stack diagonally
                    positions.append(("up2", s)); used.append("up2")

        for pos, atom in positions:
            _draw_sub(c, cx, cy, pos, atom, BOND_W, ATOM_FS)

        # finally the carbon atom label on top
        _atom_label(c, cx, cy, "C", ATOM_FS)

    return c.svg()


def _atom_label(c, x, y, txt, fs=36):
    """White-haloed atom symbol so bonds appear to terminate at the atom."""
    # cream-coloured background rectangle behind the atom
    pad = fs * 0.32
    w = fs * 0.78 * len(txt)
    c.S.append(
        f'<rect x="{x-w/2-2}" y="{y-fs*0.55}" width="{w+4}" '
        f'height="{fs*0.95}" fill="{STYLE["cream"]}"/>')
    c.S.append(
        f'<text x="{x}" y="{y+fs*0.34}" font-family="{STYLE["font"]}" '
        f'font-size="{fs}" fill="{STYLE["label"]}" text-anchor="middle" '
        f'font-weight="bold">{txt}</text>')


def _draw_sub(c, cx, cy, pos, atom, BOND_W, ATOM_FS):
    """Draw a substituent bond from carbon at (cx,cy) in direction `pos`
    and place its atom label at the bond end."""
    L = 92
    ST_ = STYLE["stroke"]
    # bond endpoints depend on pos
    dirs = {
        "up":    (0, -1),
        "down":  (0, 1),
        "left":  (-1, 0),
        "right": (1, 0),
        "up2":   (0.7, -0.7),
    }
    dx, dy = dirs.get(pos, (0, -1))
    # bond starts 26 px from C, ends 26 px before atom
    x1 = cx + dx * 26
    y1 = cy + dy * 26
    x2 = cx + dx * (L - 26)
    y2 = cy + dy * (L - 26)
    is_double = atom.startswith("=")
    label = atom[1:] if is_double else atom
    # if the group sits to the left of the carbon, flip multi-char labels
    # so the bonding atom is adjacent to the bond (e.g. "OH" -> "HO" on
    # the left so the O is next to the C-O bond, not the H).
    if pos == "left" and len(label) > 1:
        label = label[::-1]
    if is_double:
        # double bond (two parallel lines, perpendicular offset)
        px, py = -dy, dx
        c.S.append(
            f'<line x1="{x1+px*5}" y1="{y1+py*5}" '
            f'x2="{x2+px*5}" y2="{y2+py*5}" '
            f'stroke="{ST_}" stroke-width="{BOND_W}"/>')
        c.S.append(
            f'<line x1="{x1-px*5}" y1="{y1-py*5}" '
            f'x2="{x2-px*5}" y2="{y2-py*5}" '
            f'stroke="{ST_}" stroke-width="{BOND_W}"/>')
    else:
        c.S.append(
            f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" '
            f'stroke="{ST_}" stroke-width="{BOND_W}"/>')
    _atom_label(c, cx + dx*L, cy + dy*L, label, ATOM_FS)


def _render_chemp2_phase1():
    samples = ["methane", "ethane", "propane", "butane",
               "ethene", "propene",
               "methanol", "ethanol",
               "ethanoic_acid"]
    for k in samples:
        export(displayed_formula(k), "org_" + k, formats=("png",))
        print("chemp2 phase1", k)


# ====================================================================
# CHEMISTRY P2 — PHASE 2: REACTION PROFILES & RATE GRAPHS
# ====================================================================
def reaction_profile(kind="exothermic", with_catalyst=False, title=None):
    """Energy vs reaction-progress profile.
    kind          : 'exothermic' or 'endothermic'
    with_catalyst : overlay an alternative path with lower Ea
    """
    if kind not in ("exothermic", "endothermic"):
        raise ValueError("kind must be 'exothermic' or 'endothermic'")
    W, H = 1240, 780
    c = Canvas(W, H)
    c.label(W/2, 56,
            title or f"Reaction profile \u2014 {kind}", 36, "bold")

    # axes
    ox, oy = 170, 600                # axis origin (bottom-left)
    aw, ah = 940, 460
    c.S.append(
        f'<line x1="{ox}" y1="{oy}" x2="{ox+aw}" y2="{oy}" '
        f'stroke="{STYLE["stroke"]}" stroke-width="3"/>')
    c.S.append(
        f'<line x1="{ox}" y1="{oy}" x2="{ox}" y2="{oy-ah}" '
        f'stroke="{STYLE["stroke"]}" stroke-width="3"/>')
    c.label(ox+aw/2, oy+58, "Reaction progress \u2192", 24, anchor="middle")
    c.S.append(
        f'<text x="{ox-110}" y="{oy-ah/2}" font-family="{STYLE["font"]}" '
        f'font-size="24" fill="{STYLE["label"]}" text-anchor="middle" '
        f'font-weight="bold" transform="rotate(-90 {ox-110} '
        f'{oy-ah/2})">Energy \u2192</text>')

    # reactant / product levels (fractions of axis height)
    if kind == "exothermic":
        r_level, p_level, peak_level = 0.45, 0.20, 0.85
    else:
        r_level, p_level, peak_level = 0.25, 0.50, 0.85
    cat_peak = 0.70                       # catalyst lowers Ea

    def X(f): return ox + f * aw
    def Y(f): return oy - f * ah

    # x positions for the plateaus
    rx1, rx2 = 0.05, 0.22                  # reactants plateau
    px1, px2 = 0.78, 0.95                  # products plateau
    px_peak = 0.50                          # peak position

    # main path (uncatalysed)
    path = (
        f'M {X(rx1)} {Y(r_level)} L {X(rx2)} {Y(r_level)} '
        f'Q {X(rx2+0.05)} {Y(r_level)} {X(px_peak)} {Y(peak_level)} '
        f'Q {X(px1-0.05)} {Y(p_level)} {X(px1)} {Y(p_level)} '
        f'L {X(px2)} {Y(p_level)}')
    c.S.append(
        f'<path d="{path}" fill="none" stroke="{STYLE["arrow"]}" '
        f'stroke-width="4"/>')

    # catalyst overlay (dashed, lower peak)
    if with_catalyst:
        path_c = (
            f'M {X(rx1)} {Y(r_level)} L {X(rx2)} {Y(r_level)} '
            f'Q {X(rx2+0.05)} {Y(r_level)} {X(px_peak)} {Y(cat_peak)} '
            f'Q {X(px1-0.05)} {Y(p_level)} {X(px1)} {Y(p_level)} '
            f'L {X(px2)} {Y(p_level)}')
        c.S.append(
            f'<path d="{path_c}" fill="none" stroke="#C8102E" '
            f'stroke-width="3.5" stroke-dasharray="9 7"/>')
        c.label(X(0.36), Y(cat_peak) - 14,
                "with catalyst (lower E\u2090)", 20, anchor="middle")

    # plateau labels
    c.label(X(0.13), Y(r_level) - 20, "reactants", 22, anchor="middle")
    c.label(X(0.87), Y(p_level) - 20, "products", 22, anchor="middle")

    # activation energy arrow (Ea)
    ax = X(px_peak) + 14
    c.S.append(
        f'<line x1="{ax}" y1="{Y(r_level)}" x2="{ax}" y2="{Y(peak_level)}" '
        f'stroke="{STYLE["stroke"]}" stroke-width="2" '
        f'stroke-dasharray="4 5"/>')
    # arrow caps
    for ay in (Y(r_level), Y(peak_level)):
        c.S.append(
            f'<polygon points="{ax-8},{ay} {ax+8},{ay} {ax},'
            f'{ay + (4 if ay==Y(r_level) else -4)*2}" '
            f'fill="{STYLE["stroke"]}"/>')
    c.label(ax + 50, (Y(r_level) + Y(peak_level)) / 2,
            "E\u2090 (activation energy)", 22, "bold")

    # ΔH arrow (energy change)
    dx = X(0.95) + 30
    ystart = Y(r_level)
    yend = Y(p_level)
    c.S.append(
        f'<line x1="{dx}" y1="{ystart}" x2="{dx}" y2="{yend}" '
        f'stroke="#C8102E" stroke-width="3"/>')
    arrow_dir = 1 if kind == "endothermic" else -1
    tip_y = yend
    c.S.append(
        f'<polygon points="{dx-9},{tip_y - arrow_dir*-10} '
        f'{dx+9},{tip_y - arrow_dir*-10} {dx},{tip_y}" '
        f'fill="#C8102E"/>')
    sign = "+" if kind == "endothermic" else "\u2212"
    c.label(dx + 70, (ystart + yend) / 2,
            f"\u0394H ({sign}ve)", 24, "bold", "middle")

    # red exam line
    msg = ("Exothermic: products lower in energy than reactants \u2192 "
           "energy released to surroundings."
           if kind == "exothermic"
           else "Endothermic: products higher in energy than reactants "
                "\u2192 energy taken in from surroundings.")
    c.S.append(
        f'<text x="{W/2}" y="{H-40}" font-family="{STYLE["font"]}" '
        f'font-size="22" fill="#C8102E" text-anchor="middle" '
        f'font-weight="bold">{msg}</text>')
    return c.svg()


def rate_graph(curves, title="Rate of reaction \u2014 effect of conditions",
                xlabel="Time / s", ylabel="Volume of gas / cm\u00b3"):
    """Plot one or more reaction-progress curves on shared axes.
    curves : list of dicts with keys
       label    -- legend label
       k        -- 1st-order rate constant (per second) controlling steepness
       plateau  -- maximum volume reached
       colour   -- hex string
    """
    W, H = 1240, 780
    c = Canvas(W, H)
    c.label(W/2, 56, title, 36, "bold")
    ox, oy = 170, 600
    aw, ah = 940, 460
    c.S.append(
        f'<line x1="{ox}" y1="{oy}" x2="{ox+aw}" y2="{oy}" '
        f'stroke="{STYLE["stroke"]}" stroke-width="3"/>')
    c.S.append(
        f'<line x1="{ox}" y1="{oy}" x2="{ox}" y2="{oy-ah}" '
        f'stroke="{STYLE["stroke"]}" stroke-width="3"/>')
    c.label(ox+aw/2, oy+58, xlabel + " \u2192", 24, anchor="middle")
    c.S.append(
        f'<text x="{ox-110}" y="{oy-ah/2}" font-family="{STYLE["font"]}" '
        f'font-size="24" fill="{STYLE["label"]}" text-anchor="middle" '
        f'font-weight="bold" transform="rotate(-90 {ox-110} '
        f'{oy-ah/2})">{ylabel} \u2192</text>')

    # plot curves: V(t) = plateau * (1 - exp(-k*t))
    T_total = 60                       # time axis range in 'seconds'
    plateau_max = max(c2["plateau"] for c2 in curves) * 1.1
    for ci, curve in enumerate(curves):
        pts = []
        for j in range(121):
            t = (j / 120) * T_total
            v = curve["plateau"] * (1 - math.exp(-curve["k"] * t))
            x = ox + (t / T_total) * aw
            y = oy - (v / plateau_max) * ah
            pts.append((x, y))
        d = "M " + " L ".join(f"{x:.1f} {y:.1f}" for x, y in pts)
        c.S.append(
            f'<path d="{d}" fill="none" stroke="{curve["colour"]}" '
            f'stroke-width="4"/>')
        # legend entry
        ly = 130 + ci * 38
        c.S.append(
            f'<line x1="{ox+aw-300}" y1="{ly}" x2="{ox+aw-240}" '
            f'y2="{ly}" stroke="{curve["colour"]}" stroke-width="4"/>')
        c.label(ox+aw-230, ly+7, curve["label"], 22, anchor="start")

    # red exam line — generic for rate graphs
    c.S.append(
        f'<text x="{W/2}" y="{H-40}" font-family="{STYLE["font"]}" '
        f'font-size="22" fill="#C8102E" text-anchor="middle" '
        f'font-weight="bold">Steeper curve = faster rate. '
        f'Same plateau = same amount of product.</text>')
    return c.svg()



# ====================================================================
# CHEMISTRY P2 — PHASE 3: FRACTIONAL DISTILLATION & CRACKING
# ====================================================================
def fractional_distillation():
    """Industrial fractional distillation column: tall labelled tower
    with fractions tapped off at different heights, temperature gradient
    hot at bottom -> cool at top."""
    W, H = 1320, 850
    c = Canvas(W, H)
    c.label(W/2, 56, "Fractional distillation of crude oil",
            36, "bold")

    # column geometry — tall trapezoid (wider at base, narrower at top)
    cxc = 600
    top_y, bot_y = 130, 720
    top_w, bot_w = 240, 360
    # 4 corners (the outline is drawn AFTER the bands so it stays crisp)
    pts = [(cxc - top_w/2, top_y), (cxc + top_w/2, top_y),
           (cxc + bot_w/2, bot_y), (cxc - bot_w/2, bot_y)]

    # crude oil + heater at the bottom
    fy = bot_y + 30
    c.label(cxc - bot_w/2 - 110, fy, "crude oil in", 20, anchor="middle")
    c.S.append(
        f'<line x1="{cxc - bot_w/2 - 30}" y1="{fy}" '
        f'x2="{cxc - bot_w/2}" y2="{fy}" '
        f'stroke="{STYLE["stroke"]}" stroke-width="3"/>')
    c.S.append(
        f'<polygon points="{cxc-bot_w/2},{fy} '
        f'{cxc-bot_w/2-12},{fy-7} {cxc-bot_w/2-12},{fy+7}" '
        f'fill="{STYLE["stroke"]}"/>')
    # heater symbol below the column base (kept tight underneath)
    hy = bot_y + 8
    c.S.append(
        f'<rect x="{cxc - 80}" y="{hy}" width="160" height="30" '
        f'rx="6" fill="#FBBF24" opacity="0.7" '
        f'stroke="{STYLE["stroke"]}" stroke-width="2"/>')
    c.label(cxc, hy + 20, "furnace (heated)", 18, anchor="middle")

    # fractions tapped off — each is a label + small horizontal pipe + box
    # ordered top (lightest) -> bottom (heaviest). Each gets its own colour
    # band in the column (light at top -> warm/dark at bottom).
    fractions = [
        ("LPG / refinery gases", "small molecules, very volatile",  0.08,
         "#C2DCFD"),  # very pale ice blue (very volatile, gas)
        ("Petrol",               "fuel for cars",                  0.22,
         "#A9D9BE"),  # mint (light fraction)
        ("Kerosene",             "aircraft fuel",                  0.40,
         "#F2C9AE"),  # salmon
        ("Diesel",               "fuel for lorries / trains",      0.58,
         "#FBBF24"),  # accent yellow
        ("Heating oil",          "central heating",                0.74,
         "#E0892E"),  # amber
        ("Fuel oil",             "ships / power stations",         0.88,
         "#A67042"),  # warm brown
        ("Bitumen",              "roads & roofs",                  1.00,
         "#3A2B1F"),  # near-black tar
    ]

    # Draw the coloured bands first, INSIDE the trapezoidal column.
    # Each band runs from the previous fraction's level to this one's.
    col_h = bot_y - top_y
    prev_frac = 0.0
    for (nm, use, frac, colour) in fractions:
        y_a = top_y + prev_frac * col_h
        y_b = top_y + frac * col_h
        # column width at y is interpolated
        def half_w(y):
            t = (y - top_y) / col_h
            return (top_w + (bot_w - top_w) * t) / 2
        ha = half_w(y_a); hb = half_w(y_b)
        c.S.append(
            f'<polygon points="{cxc - ha},{y_a} {cxc + ha},{y_a} '
            f'{cxc + hb},{y_b} {cxc - hb},{y_b}" '
            f'fill="{colour}" opacity="0.55" '
            f'stroke="{STYLE["stroke"]}" stroke-width="1"/>')
        prev_frac = frac

    # Draw the column outline ON TOP of the bands so it stays crisp
    c.S.append(
        f'<polygon points="{pts[0][0]},{pts[0][1]} '
        f'{pts[1][0]},{pts[1][1]} {pts[2][0]},{pts[2][1]} '
        f'{pts[3][0]},{pts[3][1]}" fill="none" '
        f'stroke="{STYLE["stroke"]}" stroke-width="3"/>')

    # Pipes + labels for each fraction
    for (nm, use, frac, colour) in fractions:
        y = top_y + frac * col_h
        w = top_w + (bot_w - top_w) * frac
        pipe_start = cxc + w/2
        pipe_end = pipe_start + 80
        c.S.append(
            f'<line x1="{pipe_start}" y1="{y}" x2="{pipe_end}" y2="{y}" '
            f'stroke="{STYLE["stroke"]}" stroke-width="3"/>')
        c.S.append(
            f'<polygon points="{pipe_end},{y} {pipe_end-14},{y-8} '
            f'{pipe_end-14},{y+8}" fill="{STYLE["stroke"]}"/>')
        # colour swatch next to each label
        c.S.append(
            f'<rect x="{pipe_end + 16}" y="{y - 12}" width="22" '
            f'height="22" rx="3" fill="{colour}" opacity="0.85" '
            f'stroke="{STYLE["stroke"]}" stroke-width="1.5"/>')
        c.label(pipe_end + 50, y + 4, nm, 22, "bold", "start")
        c.label(pipe_end + 50, y + 26, use, 18, "normal", "start")

    # temperature gradient arrow on the left
    ax = cxc - bot_w/2 - 110
    c.S.append(
        f'<line x1="{ax}" y1="{top_y + 20}" x2="{ax}" y2="{bot_y - 20}" '
        f'stroke="{STYLE["arrow"]}" stroke-width="6" '
        f'stroke-linecap="round"/>')
    c.S.append(
        f'<polygon points="{ax},{bot_y - 20} {ax-12},{bot_y - 44} '
        f'{ax+12},{bot_y - 44}" fill="{STYLE["arrow"]}"/>')
    c.label(ax - 26, top_y + 10, "cool", 22, "bold", "end")
    c.label(ax - 26, top_y + 38, "(~25 \u00b0C)", 18, "normal", "end")
    c.label(ax - 26, bot_y - 30, "hot", 22, "bold", "end")
    c.label(ax - 26, bot_y - 6, "(~350 \u00b0C)", 18, "normal", "end")

    # red exam line
    c.S.append(
        f'<text x="{W/2}" y="{H-40}" font-family="{STYLE["font"]}" '
        f'font-size="22" fill="#C8102E" text-anchor="middle" '
        f'font-weight="bold">Hydrocarbons with similar boiling points '
        f'condense at the same level. Shorter chains rise highest.</text>')
    return c.svg()


def cracking_apparatus():
    """Lab cracking apparatus: paraffin on mineral wool, broken pot
    catalyst, delivery tube into water trough, gas collection."""
    W, H = 1320, 700
    c = Canvas(W, H)
    c.label(W/2, 56, "Cracking of long-chain hydrocarbons (lab)",
            34, "bold")

    # boiling tube held horizontally on a stand (left)
    tx1, tx2 = 130, 600
    ty = 320
    tube_h = 80
    # tube body
    c.S.append(
        f'<rect x="{tx1}" y="{ty - tube_h/2}" width="{tx2-tx1}" '
        f'height="{tube_h}" rx="{tube_h/2}" fill="none" '
        f'stroke="{STYLE["stroke"]}" stroke-width="3"/>')
    # close the left end (flat opening with bung region)
    c.S.append(
        f'<line x1="{tx1}" y1="{ty - tube_h/2}" x2="{tx1}" '
        f'y2="{ty + tube_h/2}" stroke="{STYLE["stroke"]}" '
        f'stroke-width="3"/>')

    # mineral wool soaked in paraffin (left third)
    mw_w = 80
    c.S.append(
        f'<rect x="{tx1 + 30}" y="{ty - 18}" width="{mw_w}" '
        f'height="36" fill="#FBBF24" opacity="0.7" '
        f'stroke="{STYLE["stroke"]}" stroke-width="2"/>')
    c.label(tx1 + 30 + mw_w/2, ty - 28,
            "mineral wool +", 16, "normal", "middle")
    c.label(tx1 + 30 + mw_w/2, ty - 12,
            "paraffin oil", 16, "normal", "middle")
    # broken pot catalyst (right third inside tube)
    bp_x = tx1 + 240
    for i in range(7):
        c.S.append(
            f'<polygon points="{bp_x + i*22},{ty - 8} '
            f'{bp_x + 6 + i*22},{ty + 14} '
            f'{bp_x - 8 + i*22},{ty + 14}" '
            f'fill="{STYLE["bracket"]}" stroke="{STYLE["stroke"]}" '
            f'stroke-width="1.5"/>')
    c.label(bp_x + 70, ty - 26, "broken pot (catalyst)",
            18, "normal", "middle")

    # heater (Bunsen) underneath
    by = ty + tube_h/2 + 10
    bcx = bp_x + 70
    # flames
    for dx in (-22, 0, 22):
        c.S.append(
            f'<path d="M{bcx + dx} {by + 70} Q{bcx + dx - 14} {by + 35} '
            f'{bcx + dx} {by + 6} Q{bcx + dx + 14} {by + 35} '
            f'{bcx + dx} {by + 70} Z" '
            f'fill="#FBBF24" opacity="0.7" stroke="{STYLE["stroke"]}" '
            f'stroke-width="1.5"/>')
    c.S.append(
        f'<rect x="{bcx - 50}" y="{by + 70}" width="100" height="18" '
        f'rx="3" fill="{STYLE["stroke"]}" opacity="0.6"/>')
    c.label(bcx, by + 110, "heat", 22, "bold", "middle")

    # delivery tube from right end of boiling tube, down into water trough
    dt_start_x = tx2
    c.S.append(
        f'<polyline points="{dt_start_x},{ty} '
        f'{dt_start_x + 110},{ty} '
        f'{dt_start_x + 110},{ty + 220} '
        f'{dt_start_x + 240},{ty + 220} '
        f'{dt_start_x + 240},{ty + 130}" '
        f'fill="none" stroke="{STYLE["stroke"]}" stroke-width="3"/>')

    # water trough
    troy = ty + 200
    trox1 = dt_start_x + 60
    trox2 = dt_start_x + 320
    c.S.append(
        f'<path d="M{trox1} {troy} L{trox1} {troy + 90} '
        f'L{trox2} {troy + 90} L{trox2} {troy}" fill="none" '
        f'stroke="{STYLE["stroke"]}" stroke-width="3"/>')
    # water
    c.S.append(
        f'<rect x="{trox1 + 3}" y="{troy + 30}" '
        f'width="{trox2 - trox1 - 6}" height="58" '
        f'fill="{STYLE["arrow"]}" opacity="0.4"/>')
    c.label((trox1+trox2)/2, troy + 110, "water", 20, "normal", "middle")

    # gas-collection test tube over the delivery tube outlet
    gx = dt_start_x + 240
    gtop = ty + 90
    gbot = ty + 220
    c.S.append(
        f'<rect x="{gx - 28}" y="{gtop}" width="56" '
        f'height="{gbot - gtop}" rx="28" fill="none" '
        f'stroke="{STYLE["stroke"]}" stroke-width="3"/>')
    # half-full of collected gas / displaced water
    c.S.append(
        f'<rect x="{gx - 25}" y="{gtop + 70}" width="50" height="56" '
        f'fill="{STYLE["arrow"]}" opacity="0.4"/>')
    c.label(gx + 70, gtop + 30, "gas collected", 20, "bold", "middle")
    c.label(gx + 70, gtop + 56, "(e.g. ethene)", 18, "normal", "middle")

    # red exam line
    c.S.append(
        f'<text x="{W/2}" y="{H-40}" font-family="{STYLE["font"]}" '
        f'font-size="22" fill="#C8102E" text-anchor="middle" '
        f'font-weight="bold">Long-chain alkane \u2192 shorter alkane + '
        f'alkene. Heat + catalyst breaks the C\u2013C bonds.</text>')
    return c.svg()


def _render_chemp2_phase3():
    export(fractional_distillation(), "fractional_distillation",
           formats=("png",))
    export(cracking_apparatus(), "cracking_apparatus",
           formats=("png",))
    for nm in ("fractional_distillation", "cracking_apparatus"):
        print("chemp2 phase3", nm)


# ====================================================================
# CHEMISTRY P2 — PHASE 4: CHROMATOGRAPHY, FLAME TESTS, ION ID TABLES
# ====================================================================
def chromatography(spots=None):
    """Paper chromatography setup with an unknown beside reference spots.
    spots : optional list of dicts: {"label": str, "rf": 0..1, "colour": hex}
            The default illustrates an unknown matching two of three knowns."""
    if spots is None:
        spots = [
            {"label": "A",        "rf": 0.30, "colour": "#C8102E"},
            {"label": "B",        "rf": 0.55, "colour": "#3B82F6"},
            {"label": "C",        "rf": 0.78, "colour": "#2E5E45"},
            {"label": "unknown",  "rf": [0.30, 0.78],
             "colour": ["#C8102E", "#2E5E45"]},
        ]
    W, H = 1320, 820
    c = Canvas(W, H)
    c.label(W/2, 56, "Paper Chromatography", 38, "bold")

    # beaker
    bx, by, bw, bh = 280, 160, 760, 540
    c.S.append(
        f'<path d="M{bx} {by} L{bx} {by+bh} Q{bx} {by+bh+24} '
        f'{bx+24} {by+bh+24} L{bx+bw-24} {by+bh+24} '
        f'Q{bx+bw} {by+bh+24} {bx+bw} {by+bh} L{bx+bw} {by}" '
        f'fill="none" stroke="{STYLE["stroke"]}" stroke-width="3"/>')

    # solvent at the bottom
    solv_top = by + bh - 60
    c.S.append(
        f'<rect x="{bx+3}" y="{solv_top}" '
        f'width="{bw-6}" height="58" '
        f'fill="{STYLE["arrow"]}" opacity="0.35"/>')
    c.label(bx + bw - 80, solv_top + 38, "solvent", 20, anchor="end")

    # filter paper — rectangle, sits in solvent
    pw, ph = 580, 460
    px = bx + (bw - pw)/2
    py = by + 40
    c.S.append(
        f'<rect x="{px}" y="{py}" width="{pw}" height="{ph}" '
        f'fill="{STYLE["cream"]}" stroke="{STYLE["stroke"]}" '
        f'stroke-width="2"/>')
    # baseline (pencil)
    baseline_y = py + ph - 80
    c.S.append(
        f'<line x1="{px+30}" y1="{baseline_y}" x2="{px+pw-30}" '
        f'y2="{baseline_y}" stroke="{STYLE["stroke"]}" stroke-width="1.5" '
        f'stroke-dasharray="3 4"/>')
    c.label(px + 8, baseline_y + 22, "baseline (pencil)",
            16, "normal", "start")

    # solvent front (pencil at top of run)
    front_y = py + 40
    c.S.append(
        f'<line x1="{px+30}" y1="{front_y}" x2="{px+pw-30}" '
        f'y2="{front_y}" stroke="{STYLE["stroke"]}" stroke-width="1.5" '
        f'stroke-dasharray="3 4"/>')
    c.label(px + 8, front_y - 12, "solvent front",
            16, "normal", "start")

    # spots
    n = len(spots)
    col_w = pw / (n + 1)
    for i, s in enumerate(spots):
        sx = px + col_w * (i + 1)
        # baseline starting spot (always shown)
        c.S.append(
            f'<circle cx="{sx}" cy="{baseline_y}" r="9" '
            f'fill="{STYLE["stroke"]}" opacity="0.7"/>')
        # label below baseline
        c.label(sx, baseline_y + 50, s["label"], 22, "bold", "middle")
        # destination spots after running
        rfs = s["rf"] if isinstance(s["rf"], list) else [s["rf"]]
        cols = s["colour"] if isinstance(s["colour"], list) else [s["colour"]]
        for rf, colour in zip(rfs, cols):
            # rf measured from baseline to solvent front
            dy = baseline_y - rf * (baseline_y - front_y)
            c.S.append(
                f'<circle cx="{sx}" cy="{dy}" r="14" fill="{colour}" '
                f'opacity="0.78" stroke="{STYLE["stroke"]}" '
                f'stroke-width="1.5"/>')

    # Rf formula in red
    c.S.append(
        f'<text x="{W/2}" y="{H-72}" font-family="{STYLE["font"]}" '
        f'font-size="26" fill="#C8102E" text-anchor="middle" '
        f'font-weight="bold">R\u1da0 = distance moved by spot \u00f7 '
        f'distance moved by solvent</text>')
    c.label(W/2, H-34,
            "An unknown matches a reference when their R\u1da0 "
            "values are equal.", 22, anchor="middle")
    return c.svg()


def flame_tests():
    """Reference table: flame test colours for the common Group 1 / 2
    metal ions AQA expects students to know."""
    rows = [
        ("Lithium",   "Li\u207a",      "#C8102E", "Crimson red"),
        ("Sodium",    "Na\u207a",      "#FBBF24", "Yellow"),
        ("Potassium", "K\u207a",       "#9333EA", "Lilac"),
        ("Calcium",   "Ca\u00b2\u207a","#E0892E", "Orange-red"),
        ("Copper",    "Cu\u00b2\u207a","#2E8B7F", "Green"),
    ]
    W, H = 1160, 720
    c = Canvas(W, H)
    c.label(W/2, 56, "Flame Test Colours", 38, "bold")

    # column setup
    headers = ["Metal", "Ion", "Flame", "Colour"]
    cols_x = [80, 320, 560, 850]
    col_w = [220, 220, 270, 230]

    # header strip
    hy = 140
    c.S.append(
        f'<rect x="60" y="{hy}" width="{W-120}" height="56" rx="6" '
        f'fill="#1E3A5F" stroke="{STYLE["stroke"]}" stroke-width="2"/>')
    for x, head in zip(cols_x, headers):
        _cell_text(c, x, hy + 38, head, "#FFFFFF", 24, "bold")

    # rows
    ry = hy + 56
    rh = 90
    for i, (name, ion, hex_colour, label) in enumerate(rows):
        # alternating row backgrounds
        bg = "#FAF7F2" if i % 2 == 0 else "#F0EAD6"
        c.S.append(
            f'<rect x="60" y="{ry}" width="{W-120}" height="{rh}" '
            f'fill="{bg}" stroke="{STYLE["stroke"]}" stroke-width="1"/>')
        _cell_text(c, cols_x[0], ry + 56, name, STYLE["label"], 24)
        _cell_text(c, cols_x[1], ry + 56, ion, STYLE["label"], 26, "bold")
        # flame colour swatch
        sx = cols_x[2] + 30
        sy = ry + 18
        c.S.append(
            f'<rect x="{sx}" y="{sy}" width="180" height="54" rx="8" '
            f'fill="{hex_colour}" opacity="0.85" '
            f'stroke="{STYLE["stroke"]}" stroke-width="1.5"/>')
        _cell_text(c, cols_x[3], ry + 56, label, STYLE["label"], 22)
        ry += rh

    # exam note
    c.S.append(
        f'<text x="{W/2}" y="{H-30}" font-family="{STYLE["font"]}" '
        f'font-size="22" fill="#C8102E" text-anchor="middle" '
        f'font-weight="bold">Dip a clean nichrome wire in the salt, '
        f'then hold in a roaring blue flame.</text>')
    return c.svg()


def _cell_text(c, x, y, txt, colour, fs, weight="normal"):
    txt = (str(txt).replace("&", "&amp;").replace("<", "&lt;")
                   .replace(">", "&gt;"))
    c.S.append(
        f'<text x="{x:.1f}" y="{y:.1f}" font-family="{STYLE["font"]}" '
        f'font-size="{fs}" fill="{colour}" font-weight="{weight}">'
        f'{txt}</text>')


def ion_tests():
    """Reference table: AQA chemical tests for common ions and gases."""
    rows = [
        ("Cl\u207b",       "Silver nitrate + dilute nitric acid",
         "WHITE precipitate"),
        ("Br\u207b",       "Silver nitrate + dilute nitric acid",
         "CREAM precipitate"),
        ("I\u207b",        "Silver nitrate + dilute nitric acid",
         "YELLOW precipitate"),
        ("SO\u2084\u00b2\u207b", "Barium chloride + dilute HCl",
         "WHITE precipitate"),
        ("CO\u2083\u00b2\u207b", "Add dilute acid \u2192 collect gas in "
         "limewater", "Limewater turns CLOUDY (CO\u2082)"),
        ("Hydrogen (gas)", "Lit splint near mouth of test tube",
         "Squeaky POP"),
        ("Oxygen (gas)",  "Glowing splint",
         "Splint RELIGHTS"),
        ("Chlorine (gas)", "Damp litmus paper",
         "Bleaches white"),
    ]
    W, H = 1320, 780
    c = Canvas(W, H)
    c.label(W/2, 56, "Tests for Ions and Gases", 38, "bold")

    cols_x = [90, 360, 920]
    headers = ["Substance", "Test", "Positive result"]
    hy = 130
    c.S.append(
        f'<rect x="60" y="{hy}" width="{W-120}" height="56" rx="6" '
        f'fill="#1E3A5F" stroke="{STYLE["stroke"]}" stroke-width="2"/>')
    for x, head in zip(cols_x, headers):
        _cell_text(c, x, hy + 38, head, "#FFFFFF", 24, "bold")

    ry = hy + 56
    rh = 64
    for i, (sub, test, result) in enumerate(rows):
        bg = "#FAF7F2" if i % 2 == 0 else "#F0EAD6"
        c.S.append(
            f'<rect x="60" y="{ry}" width="{W-120}" height="{rh}" '
            f'fill="{bg}" stroke="{STYLE["stroke"]}" stroke-width="1"/>')
        _cell_text(c, cols_x[0], ry + 40, sub, STYLE["label"], 22, "bold")
        _cell_text(c, cols_x[1], ry + 40, test, STYLE["label"], 20)
        # results in red (the exam-critical bit)
        _cell_text(c, cols_x[2], ry + 40, result, "#C8102E", 20, "bold")
        ry += rh
    return c.svg()


def _render_chemp2_phase4():
    export(chromatography(), "chromatography", formats=("png",))
    export(flame_tests(), "flame_tests", formats=("png",))
    export(ion_tests(), "ion_tests", formats=("png",))
    for nm in ("chromatography", "flame_tests", "ion_tests"):
        print("chemp2 phase4", nm)


# ====================================================================
# CHEMISTRY P2 — PHASE 5: ATMOSPHERE, CARBON CYCLE, LCA, WATER TREATMENT
# ====================================================================
def atmosphere_pie():
    """Composition of today's atmosphere as a pie chart."""
    W, H = 1100, 760
    c = Canvas(W, H)
    c.label(W/2, 56, "Composition of today\u2019s atmosphere", 36, "bold")
    cx, cy, r = 410, 430, 240
    # AQA figures (approx)
    slices = [
        ("Nitrogen, N\u2082", 78, "#3B82F6"),
        ("Oxygen, O\u2082", 21, "#C8102E"),
        ("Argon + CO\u2082 + others", 1, "#FBBF24"),
    ]
    start = -90  # start at top
    for label, pct, col in slices:
        end = start + pct * 3.6
        # arc + radii forming a pie slice
        large = 1 if (end - start) > 180 else 0
        x1 = cx + r*math.cos(math.radians(start))
        y1 = cy + r*math.sin(math.radians(start))
        x2 = cx + r*math.cos(math.radians(end))
        y2 = cy + r*math.sin(math.radians(end))
        c.S.append(
            f'<path d="M{cx} {cy} L{x1:.1f} {y1:.1f} '
            f'A{r} {r} 0 {large} 1 {x2:.1f} {y2:.1f} Z" '
            f'fill="{col}" opacity="0.75" stroke="{STYLE["stroke"]}" '
            f'stroke-width="2"/>')
        start = end
    # legend on the right
    ly = 220
    for label, pct, col in slices:
        c.S.append(
            f'<rect x="760" y="{ly}" width="36" height="36" rx="4" '
            f'fill="{col}" opacity="0.85" stroke="{STYLE["stroke"]}" '
            f'stroke-width="1.5"/>')
        c.label(810, ly + 18, f"{label}",
                24, "bold", "start")
        c.label(810, ly + 46, f"\u2248 {pct}%", 22, "normal", "start")
        ly += 100
    # red exam note
    c.S.append(
        f'<text x="{W/2}" y="{H-40}" font-family="{STYLE["font"]}" '
        f'font-size="22" fill="#C8102E" text-anchor="middle" '
        f'font-weight="bold">Roughly 4/5 nitrogen, 1/5 oxygen, '
        f'plus traces of Ar, CO\u2082, water vapour.</text>')
    return c.svg()


def carbon_cycle():
    """Boxes and labelled arrows for the carbon cycle. Five processes
    students must know (photosynthesis, respiration, feeding, decay,
    combustion) shown clearly without label collisions."""
    W, H = 1380, 820
    c = Canvas(W, H)
    c.label(W/2, 50, "The Carbon Cycle", 38, "bold")

    GREEN = STYLE["nm_fill"]; YELL = "#FBBF24"
    AMB = "#E0892E"; BLUE = "#3B82F6"

    def box(cx, cy, w, h, txt, fill):
        c.S.append(
            f'<rect x="{cx-w/2}" y="{cy-h/2}" width="{w}" height="{h}" '
            f'rx="14" fill="{fill}" opacity="0.55" '
            f'stroke="{STYLE["stroke"]}" stroke-width="2.5"/>')
        c.label(cx, cy+8, txt, 24, "bold", "middle")

    # 5 boxes: atmosphere at top, plants/animals in middle row,
    # fossil fuels / decay in bottom row
    atm = (W/2,   150)
    pln = (310,   430)
    ani = (W-310, 430)
    fos = (310,   680)
    dec = (W-310, 680)
    box(atm[0], atm[1], 380, 90, "CO\u2082 in atmosphere", BLUE)
    box(pln[0], pln[1], 260, 90, "Plants",                 GREEN)
    box(ani[0], ani[1], 260, 90, "Animals",                AMB)
    box(fos[0], fos[1], 260, 90, "Fossil fuels",           "#3A2B1F")
    box(dec[0], dec[1], 260, 90, "Decay (microbes)",       YELL)

    def edge_arrow(x1, y1, x2, y2, col, head_size=11):
        c.S.append(
            f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" '
            f'stroke="{col}" stroke-width="5" stroke-linecap="round"/>')
        ang = math.atan2(y2-y1, x2-x1)
        ax = x2 - 20*math.cos(ang); ay = y2 - 20*math.sin(ang)
        nx, ny = -math.sin(ang)*head_size, math.cos(ang)*head_size
        c.S.append(
            f'<polygon points="{x2},{y2} {ax+nx:.1f},{ay+ny:.1f} '
            f'{ax-nx:.1f},{ay-ny:.1f}" fill="{col}"/>')

    def tlabel(x, y, txt, col, fs=20):
        # background halo so labels stay readable when crossing arrows
        pad_w = len(txt) * fs * 0.6 + 16
        c.S.append(
            f'<rect x="{x - pad_w/2:.1f}" y="{y - fs*0.75:.1f}" '
            f'width="{pad_w}" height="{fs*1.2}" rx="4" '
            f'fill="{STYLE["cream"]}" opacity="0.95"/>')
        c.S.append(
            f'<text x="{x:.1f}" y="{y+fs*0.3:.1f}" '
            f'font-family="{STYLE["font"]}" font-size="{fs}" '
            f'fill="{col}" text-anchor="middle" '
            f'font-weight="bold">{txt}</text>')

    # === arrows + labels ===
    # 1) photosynthesis: atmosphere -> plants  (left blue arrow down)
    edge_arrow(atm[0] - 150, atm[1] + 45, pln[0] + 30, pln[1] - 50, BLUE)
    tlabel(atm[0] - 270, 270, "photosynthesis", BLUE, 21)

    # 2) respiration (plants): plants -> atmosphere (curve up-left)
    edge_arrow(pln[0] - 60, pln[1] - 50, atm[0] - 70, atm[1] + 45, AMB)
    tlabel(pln[0] + 20, 290, "respiration", AMB, 19)

    # 3) respiration (animals): animals -> atmosphere (up-right)
    edge_arrow(ani[0] + 60, ani[1] - 50, atm[0] + 70, atm[1] + 45, AMB)
    tlabel(ani[0] - 20, 290, "respiration", AMB, 19)

    # 4) feeding: plants -> animals
    edge_arrow(pln[0] + 130, pln[1], ani[0] - 130, ani[1], AMB)
    tlabel((pln[0]+ani[0])/2, pln[1] - 16, "feeding", AMB, 22)

    # 5) death/decay: animals -> decay
    edge_arrow(ani[0], ani[1] + 45, dec[0], dec[1] - 50, "#5B6B82")
    tlabel(ani[0] + 90, (ani[1]+dec[1])/2,
           "death \u2192 decay", "#5B6B82", 19)

    # 6) decay releases CO2 back: decay -> atmosphere (long curve right)
    edge_arrow(dec[0] + 60, dec[1] - 50, atm[0] + 170, atm[1] + 45, AMB)
    tlabel(dec[0] - 40, 470, "respiration", AMB, 19)

    # 7) fossil fuels combustion: fossil fuels -> atmosphere (long curve)
    edge_arrow(fos[0] - 60, fos[1] - 50, atm[0] - 170, atm[1] + 45,
               "#C8102E")
    tlabel(fos[0] - 100, 470, "combustion", "#C8102E", 20)

    # 8) plants/animals -> fossil fuels (geological time)
    edge_arrow(pln[0] - 60, pln[1] + 45, fos[0] - 60, fos[1] - 50,
               "#5B6B82")
    tlabel(pln[0] - 165, (pln[1]+fos[1])/2,
           "(millions of years)", "#5B6B82", 18)

    return c.svg()


def _flow_step(c, x, y, w, h, txt, fill, sub=None):
    c.S.append(
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" '
        f'fill="{fill}" opacity="0.55" stroke="{STYLE["stroke"]}" '
        f'stroke-width="2.5"/>')
    c.label(x + w/2, y + h/2 + 4, txt, 22, "bold", "middle")
    if sub:
        c.label(x + w/2, y + h/2 + 30, sub, 17, "normal", "middle")


def _flow_arrow(c, x1, y1, x2, y2, col="#2E8B7F"):
    c.S.append(
        f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" '
        f'stroke="{col}" stroke-width="6" stroke-linecap="round"/>')
    ang = math.atan2(y2-y1, x2-x1)
    ax = x2 - 18*math.cos(ang); ay = y2 - 18*math.sin(ang)
    nx, ny = -math.sin(ang)*11, math.cos(ang)*11
    c.S.append(
        f'<polygon points="{x2},{y2} {ax+nx:.1f},{ay+ny:.1f} '
        f'{ax-nx:.1f},{ay-ny:.1f}" fill="{col}"/>')


def life_cycle_assessment():
    """Flow strip: extraction -> manufacture -> use -> disposal."""
    W, H = 1380, 540
    c = Canvas(W, H)
    c.label(W/2, 56, "Life Cycle Assessment (LCA)", 38, "bold")
    bw, bh = 260, 140
    by = 220
    steps = [
        ("Extracting\nraw materials", "from the Earth",   "#A67042"),
        ("Manufacturing", "energy + waste at the plant",  "#FBBF24"),
        ("Use",           "transport, energy, lifetime",  "#A9D9BE"),
        ("Disposal",      "landfill, recycling, incineration", "#5B6B82"),
    ]
    gap = (W - 80 - bw*4) / 3
    for i, (label, sub, col) in enumerate(steps):
        bx = 40 + i*(bw + gap)
        # multi-line label support via newline
        if "\n" in label:
            top, bot = label.split("\n")
            c.S.append(
                f'<rect x="{bx}" y="{by}" width="{bw}" height="{bh}" '
                f'rx="12" fill="{col}" opacity="0.55" '
                f'stroke="{STYLE["stroke"]}" stroke-width="2.5"/>')
            c.label(bx+bw/2, by+bh/2-6, top, 22, "bold", "middle")
            c.label(bx+bw/2, by+bh/2+24, bot, 22, "bold", "middle")
            c.label(bx+bw/2, by+bh+30, sub, 18, "normal", "middle")
        else:
            _flow_step(c, bx, by, bw, bh, label, col, sub)
        if i < 3:
            _flow_arrow(c, bx + bw + 8, by + bh/2,
                        bx + bw + gap - 8, by + bh/2)
    # red exam line
    c.S.append(
        f'<text x="{W/2}" y="{H-50}" font-family="{STYLE["font"]}" '
        f'font-size="22" fill="#C8102E" text-anchor="middle" '
        f'font-weight="bold">An LCA evaluates the environmental impact '
        f'of a product across every stage of its life.</text>')
    return c.svg()


def water_treatment():
    """Potable water treatment flow: reservoir -> screen -> sediment ->
    filter -> chlorinate -> tap."""
    W, H = 1400, 560
    c = Canvas(W, H)
    c.label(W/2, 56, "Potable Water Treatment", 38, "bold")
    bw, bh = 200, 120
    by = 220
    steps = [
        ("Reservoir",        "fresh water source",       "#3B82F6"),
        ("Screening",        "remove twigs, debris",     "#A67042"),
        ("Sedimentation",    "particles settle out",     "#A9D9BE"),
        ("Filtration",       "sand & gravel filters",    "#FBBF24"),
        ("Chlorination",     "kill microbes",            "#C8102E"),
        ("Safe to drink",    "to homes",                 "#2E8B7F"),
    ]
    gap = (W - 80 - bw*6) / 5
    for i, (label, sub, col) in enumerate(steps):
        bx = 40 + i*(bw + gap)
        _flow_step(c, bx, by, bw, bh, label, col, sub)
        if i < 5:
            _flow_arrow(c, bx + bw + 4, by + bh/2,
                        bx + bw + gap - 4, by + bh/2)
    # red exam line
    c.S.append(
        f'<text x="{W/2}" y="{H-50}" font-family="{STYLE["font"]}" '
        f'font-size="22" fill="#C8102E" text-anchor="middle" '
        f'font-weight="bold">Potable water is safe to drink, not pure '
        f'chemically (it contains dissolved salts).</text>')
    return c.svg()


def _render_chemp2_phase5():
    export(atmosphere_pie(), "atmosphere_pie", formats=("png",))
    export(carbon_cycle(), "carbon_cycle", formats=("png",))
    export(life_cycle_assessment(), "life_cycle_assessment",
           formats=("png",))
    export(water_treatment(), "water_treatment", formats=("png",))
    for nm in ("atmosphere_pie", "carbon_cycle", "life_cycle_assessment",
               "water_treatment"):
        print("chemp2 phase5", nm)


if __name__ == "__main__":
    for f in MOLECULES:
        export(covalent_dotcross(f), f.lower(), formats=("png",))
        print("covalent", f)
    for f in IONIC:
        export(ionic_dotcross(f), "ionic_" + f.lower(), formats=("png",))
        print("ionic", f)
    export(metallic_bonding("Cu"), "metallic_cu", formats=("png",))
    print("metallic Cu")
    p3 = {
        "simple_molecular": simple_molecular(),
        "giant_ionic_lattice": giant_ionic_lattice(),
        "polymer": polymer(),
        "diamond": diamond(),
        "graphite": graphite(),
        "graphene": graphene(),
        "silicon_dioxide": silicon_dioxide(),
        "fullerene": fullerene(),
        "nanotube": nanotube(),
    }
    for nm, svg in p3.items():
        export(svg, nm, formats=("png",))
        print("phase3", nm)
    for el in ("Li", "C", "O", "Na", "Mg", "Cl", "Ar", "Ca"):
        export(electronic_configuration(el),
               "econf_" + el.lower(), formats=("png",))
        print("phase4", el)
    for s in ELECTROLYSIS:
        export(electrolysis(s), "electro_" + s.lower(), formats=("png",))
        print("phase5", s)
    p6 = {
        "reactivity_series": reactivity_series(),
        "ph_scale": ph_scale(),
        "conservation_sealed": conservation_sealed(),
        "gas_syringe": gas_syringe(),
    }
    for nm, svg in p6.items():
        export(svg, nm, formats=("png",))
        print("phase6", nm)



# ====================================================================
# ⊕ FIGLIB EXTENSIONS (MRB-352 run 2) — question figures
# ====================================================================
from .style import (arrow as _q_arrow, box as _q_box,  # noqa: E402
                    line as _q_line, q_font, q_stroke, text as _q_text,
                    text_width as _tw)


def box_monomers(parts, product=None, W=480):
    """Monomers in AQA's box notation (8462 §4.7.3.2): each carbon chain is
    an empty box, its functional groups written out in full on either end,
    joined to the box by real bond lines. `parts` is a list of monomers,
    each ("n", "HO", "OH") — coefficient, left group, right group — drawn
    in one line joined by "+"; `product` is a word written after an arrow
    on the line below (never a structure: drawing the product would print
    the answer to "how do they join?")."""
    fs = q_font(W, floor=17)
    bw, bh, bond = 40, 22, 16
    lab = STYLE["label"]
    ink = STYLE["stroke"]
    # measure one line
    items = []
    for i, (coef, lg, rg) in enumerate(parts):
        if i:
            items.append(("plus", "+"))
        items.append(("mono", (coef, lg, rg)))
    def width(it):
        kind, v = it
        if kind == "plus":
            return _tw("+", fs, True) + 18
        coef, lg, rg = v
        return (_tw(coef + " ", fs, True) + _tw(lg, fs, True) + bond + bw
                + bond + _tw(rg, fs, True) + 8)
    total = sum(width(it) for it in items)
    if total > W - 24:
        raise ValueError("box_monomers: %d units of formula do not fit a "
                         "%d-wide canvas" % (total, W))
    H = 40 + fs + (fs + 44 if product else 10)
    c = Canvas(W, int(H))
    y = 30 + fs * 0.7
    x = (W - total) / 2.0
    for kind, v in items:
        if kind == "plus":
            _q_text(c, x + width((kind, v)) / 2, y + fs * 0.36, "+", fs, lab,
                    "bold")
            x += width((kind, v))
            continue
        coef, lg, rg = v
        _q_text(c, x, y + fs * 0.36, coef + " " + lg, fs, lab, "bold", "start")
        x += _tw(coef + " ", fs, True) + _tw(lg, fs, True) + 2
        _q_line(c, x, y, x + bond - 2, y, ink, 2.5, None, "butt")
        x += bond
        _q_box(c, x, y - bh / 2, bw, bh, "none", ink, 2.5)
        x += bw
        _q_line(c, x + 2, y, x + bond, y, ink, 2.5, None, "butt")
        x += bond + 2
        _q_text(c, x, y + fs * 0.36, rg, fs, lab, "bold", "start")
        x += _tw(rg, fs, True) + 6
    if product:
        y2 = y + fs + 30
        aw = 54
        pw = _tw(product, fs, True)
        x0 = (W - (aw + 14 + pw)) / 2.0
        _q_arrow(c, x0, y2 - fs * 0.3, x0 + aw, y2 - fs * 0.3, ink,
                 q_stroke(W, 2.5), 12)
        _q_text(c, x0 + aw + 14, y2, product, fs, lab, "bold", "start")
    return c.svg()
