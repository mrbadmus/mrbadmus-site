"""ks4_art.bonding_frozen — a dot-and-cross ammonia diagram with a bonding
pair deliberately left out.

Added for the MRB-352 frozen-window repair of `ks4-covalent-bonding-s04`,
whose stem is "A student's dot-and-cross diagram of ammonia shows the
nitrogen atom with only six electrons in its outer shell. Explain what has
gone wrong." — a diagram described in words instead of shown.

`ks4_art.bonding.draw_nh3` cannot serve this row: it draws the CORRECT NH3
diagram (three bonding pairs + one lone pair on N, a full octet), and this
question is specifically about a diagram that is wrong on purpose. A new
drawer is needed, not a new catalogue record reusing the existing one.

A new module rather than an addition to `ks4_art/bonding.py`: this is a
shared worktree and another lane may be editing that file concurrently, so
a new module (discovered automatically) is the safe way in. The small
dot/cross/shell/bond-pair helpers below are RE-IMPLEMENTED rather than
imported, because `ks4_art.bonding`'s versions are underscore-private to
that module — same convention, restated: the CENTRAL atom's (N's) own
electrons are dots, each H's own electron is a cross, a shared pair is one
dot + one cross together, a lone pair is two dots side by side.

The chemistry the drawing must get right: nitrogen has 3 electrons of its
own still needing partners plus a lone pair, for 8 in a complete NH3. Draw
two of the three N–H bonds with a full shared pair (dot + cross) and leave
the THIRD hydrogen's shell with no shared pair — its own electron (a cross)
sits alone, unmatched by any dot from nitrogen. Counting what falls inside
N's own shell: 2 complete bonding pairs (4 electrons, each bond counted in
full toward nitrogen) + 1 lone pair (2 electrons) = 6 — exactly the error
the stem describes, and exactly why the fix is "one bonding pair was left
out", never "the lone pair is missing" or any other reading.
"""

import math

from ks3_art.kit import _svg_open, _circle, _line, _label, _SVG_INK, _SVG_INK_MUTED


def _shell(cx, cy, r):
    return _circle(cx, cy, r, stroke=_SVG_INK_MUTED, w=1.5, dash="3,2")


def _dot(x, y, r=2.6):
    return _circle(x, y, r, fill=_SVG_INK)


def _cross(x, y, size=3.4):
    return (_line(x - size, y - size, x + size, y + size, stroke=_SVG_INK, w=1.8)
            + _line(x - size, y + size, x + size, y - size, stroke=_SVG_INK, w=1.8))


def _bond_pair(mx, my):
    """A complete shared pair — one dot (nitrogen's own electron) next to
    one cross (that hydrogen's own electron) — centred on the bond
    midpoint, exactly as `ks4_art.bonding._bond_pairs(n=1, ...)` places one."""
    return _dot(mx - 3.4, my) + _cross(mx + 3.4, my)


def _lone_pair(x, y):
    """Nitrogen's own lone pair — two dots side by side, belonging to N
    alone, never one dot and one cross (that would misstate whose
    electrons they are)."""
    return _dot(x - 3.3, y) + _dot(x + 3.3, y)


def draw_nh3_missing_bond(fig):
    """The same fan layout as `ks4_art.bonding.draw_nh3` — nitrogen centred,
    three hydrogens fanned downward at 90/210/330 degrees so the lone pair
    has the top of the shell free — but the LAST hydrogen (330 degrees) has
    no shared pair drawn: its shell carries only its own unmatched cross.
    `fig["missing_index"]` (default 2) picks which of the three H atoms, in
    fan order, is left unbonded — kept adjustable rather than hard-coded to
    a screen position, in case a future row needs a different one drawn
    wrong."""
    w, h = fig.get("w", 280), fig.get("h", 280)
    cx, cy = w / 2.0, h / 2.0 + 12
    rn, rh, dist = 30, 20, 62
    missing = fig.get("missing_index", 2)
    out = [_shell(cx, cy, rn), _label(cx, cy + 5, "N", size=16, weight="700")]
    for i, ang in enumerate((90, 210, 330)):
        rad = math.radians(ang)
        hx, hy = cx + dist * math.cos(rad), cy + dist * math.sin(rad)
        out.append(_shell(hx, hy, rh))
        lx = cx + (dist + rh + 16) * math.cos(rad)
        ly = cy + (dist + rh + 16) * math.sin(rad)
        out.append(_label(lx, ly + 5, "H", size=15, weight="700"))
        mx, my = cx + (dist / 2.0) * math.cos(rad), cy + (dist / 2.0) * math.sin(rad)
        if i == missing:
            # only the hydrogen's own electron is drawn — no dot from N,
            # so this bond carries no shared pair at all.
            out.append(_cross(mx, my))
        else:
            out.append(_bond_pair(mx, my))
    out.append(_lone_pair(cx, cy - rn + 8))
    return _svg_open(fig, w, h) + "".join(out) + "</svg>"


ART = {
    "molecule-nh3-missing-bond": draw_nh3_missing_bond,
}


if __name__ == "__main__":
    import xml.etree.ElementTree as ET

    svg = draw_nh3_missing_bond({
        "id": "sc-nh3-missing", "title": "t", "desc": "d",
    })
    ET.fromstring(svg)
    print("ok: molecule-nh3-missing-bond %6d bytes" % len(svg))
    print("bonding_frozen.py self-check: renders well-formed SVG")
