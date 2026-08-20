"""ks3_art.b4 — B4's drawers, instruments and registrations.

ONE UNIT, ONE FILE. Nothing here is read by any other unit; nothing
here may be added to any other unit's module. Moved verbatim out of
``build_ks3.py`` by MRB-271 so that two content lanes can build two
units at once without editing the same file.
"""

import math
import re
from ks3_art.kit import (
    _SVG_ACCENT_TEXT,
    _SVG_ACCENT_TINT,
    _SVG_BAND,
    _SVG_BLUE_TEXT,
    _SVG_CARD,
    _SVG_DISPLAY,
    _SVG_GROUND,
    _SVG_INK,
    _SVG_INK_BODY,
    _SVG_INK_FAINT,
    _SVG_INK_GHOST,
    _SVG_INSET,
    _SVG_RULE,
    _circle,
    _label,
    _mono,
    _n,
    _path,
    _rect,
    _svg_open,
    e,
    option_letter,
    rich,
    t,
)


# ── ⊕ MRB-254 · WS1 #11 · the same pair of guard cells, twice ───────────
#
# The three numbers the leaf strip is generated from. Design computes the
# strip rather than placing it, so these are the only literals: the pores'
# centres, how far the two guard cells sit either side of a pore, and how much
# lower epidermis each pore eats. Every run, cell and circle below is derived
# from them, which is what lets a parity row assert "three pores, all of them
# in the LOWER surface" against the drawing instead of against a caption.
_B4_GUARD_PORES = (250, 430, 610)
_B4_GUARD_DX = 20            # guard-cell centre offset either side of a pore
_B4_GUARD_GAP = 36           # half-width of the break a pore makes in the run
def _guard_cells(fig):
    """One pair of guard cells drawn twice — turgid and open, flaccid and shut
    — over a leaf in section that says every pore is on the UNDERSIDE.

    ⚖️ WHY THIS LESSON GETS A DIAGRAM. `stomata-and-gas-exchange-in-plants`
    carries the mechanism as a single prose sentence about a shape change, and
    a shape change described in words is a shape change a student memorises
    rather than sees. The claim is irreducibly spatial: a cell that fills with
    water BENDS instead of swelling evenly, and the bend is the only thing that
    opens the hole. Two panels do that; no sentence does.

    ⛔ IT IS THE SAME PAIR, TWICE — the drawing's whole argument, and the thing
    that would be cheapest to lose. Both panels draw the pair over the same
    180-unit span (60 to 240 on the left, 480 to 660 on the right), the same
    wall weights, the same everything: only the bend differs. Draw the
    closed pair
    shorter or thinner and the figure quietly starts teaching that guard cells
    shrink, which is the misconception it exists to remove. `data-state` on
    every shape in each panel is what lets a row check the two against each
    other rather than eyeball them.

    ⚖️ THE THICKENED INNER WALL IS THE MECHANISM, so it is a hook and not just
    a stroke weight. Inner walls are drawn at 5.5 (open) and 6.5 (closed, where
    the two meet as one line); outer walls at 2, in both. That asymmetry is the
    REASON the cell curves — the stiff inside cannot stretch, the outside can,
    so the cell can only bow away from its partner. A defect that dropped the
    thickening from ONE panel would still look entirely correct in the other,
    which is exactly why `data-wall="inner"/"outer"` goes on all of them and
    the assertion is made in both panels rather than once.

    ⚠️ THE PORE IS A HOLE, AND A HOLE IS A CONTRAST, NOT A SHAPE. The
    open pore is `--ks3-ink-body` under cell bodies in `--ks3-band`, measured
    at 10.2:1, so it reads as a gap THROUGH the leaf rather than as a dark
    lozenge lying on it. The words "pore open" sit ON that dark fill in
    `--ks3-ground`, 11.1:1. Both hold only while the pore stays the darkest
    thing in the panel; lighten it and the label goes first, silently.

    ⊕ THE STRIP UNDERNEATH CARRIES THE SECOND CLAIM, and carries it by
    CONSTRUCTION. The lower epidermis and the lower cuticle are built as runs
    BETWEEN the pores — so each break is a real absence of leaf, not a dark
    rectangle painted over a solid row. The upper cuticle is one rect spanning
    the whole strip and cannot be broken by accident. `data-run="1"` marks the
    surface runs (not the epidermis cells, whose 4-unit gaps are cell walls and
    not pores), so a row can assert: the upper surface is one unbroken span,
    the lower surface is four runs with three gaps, and every `data-pore="1"`
    sits in one of those gaps and carries `data-surface="lower"`.

    ⊕ EVERY HOOK IS SPELLED `data_<name>` AT THE CALL SITE, and `_data_attrs`
    strips the prefix to emit `data-<name>`. A bare keyword raises there rather
    than landing as a presentation attribute — so the name written in this file
    is the name a content-truth row will look for, with no translation step in
    between. That is the whole reason the prefix is written twice.

    ⊕ THE LABELS CARRY THE STATE TOO, not just the shapes. `_label` and
    `_mono` take `**data` like every other emitter, so "pore open" and "no gap
    left" answer to the same `data-state` as the paths they annotate — a row
    that walks one panel gets the drawing AND the words for it, and a label
    orphaned into the wrong panel becomes findable rather than merely wrong.
    The `<g data-state="…">` wrappers stay as the container a row can select
    on; the elements repeat the hook so neither is the single point of truth.

    """
    W, H = 860, 580
    out = [_svg_open(fig, W, H)]
    out.append('<g stroke-linecap="round" stroke-linejoin="round">')

    # ── the two panels, seen from the surface of the leaf ────────────────
    out.append(_mono(24, 42, "THE SAME PAIR OF GUARD CELLS, SEEN FROM THE "
                             "SURFACE", size=14, weight="400", spacing="1.4"))

    # ── open ──
    out.append('<g data-state="open">')
    out.append(_rect(30, 60, 380, 320, rx=18, fill=_SVG_CARD,
                     stroke=_SVG_INK, w=2.5, data_state="open",
                     data_panel="open"))
    out.append(_label(54, 98, "Open", size=26, weight="800", anchor="start",
                      family=_SVG_DISPLAY, spacing="-.5",
                      data_state="open"))
    out.append(_mono(54, 120, "water in · firm", size=15,
                     fill=_SVG_ACCENT_TEXT, weight="400",
                     data_state="open"))

    # The hole first, then the two cell bodies over it: the pore is the sliver
    # of dark left showing between them, so it can never be wider than the gap
    # the two bodies actually leave.
    out.append(_path("M 60,240 C 82,200 218,200 240,240 "
                     "C 218,280 82,280 60,240 Z",
                     fill=_SVG_INK_BODY, data_state="open", data_gap="open"))
    out.append(_path("M 60,240 C 82,174 218,174 240,240 "
                     "C 218,200 82,200 60,240 Z",
                     fill=_SVG_BAND, data_state="open", data_cell="upper"))
    out.append(_path("M 60,240 C 82,306 218,306 240,240 "
                     "C 218,280 82,280 60,240 Z",
                     fill=_SVG_BAND, data_state="open", data_cell="lower"))
    out.append(_path("M 60,240 C 82,174 218,174 240,240", stroke=_SVG_INK,
                     w=2, data_state="open", data_cell="upper",
                     data_wall="outer"))
    out.append(_path("M 60,240 C 82,306 218,306 240,240", stroke=_SVG_INK,
                     w=2, data_state="open", data_cell="lower",
                     data_wall="outer"))
    out.append(_path("M 60,240 C 82,200 218,200 240,240", stroke=_SVG_INK,
                     w=5.5, data_state="open", data_cell="upper",
                     data_wall="inner"))
    out.append(_path("M 60,240 C 82,280 218,280 240,240", stroke=_SVG_INK,
                     w=5.5, data_state="open", data_cell="lower",
                     data_wall="inner"))
    out.append(_label(150, 246, "pore open", size=17, fill=_SVG_GROUND,
                      weight="700", data_state="open", data_gap="open"))

    # Design hand-placed both heads rather than deriving them, so they are
    # reproduced as her literal triangles — a drawn head either way, never a
    # glyph, but hers to the coordinate.
    out.append(_path("M 110,150 V 190", stroke=_SVG_INK, w=3,
                     data_state="open", data_water="in"))
    out.append(_path("M 103,188 L 117,188 L 110,202 Z", fill=_SVG_INK,
                     data_state="open", data_water="in"))
    out.append(_label(110, 142, "water in", size=16, weight="400",
                      data_state="open", data_water="in"))
    out.append(_path("M 190,344 V 296", stroke=_SVG_INK, w=3,
                     data_state="open", data_water="in"))
    out.append(_path("M 183,298 L 197,298 L 190,284 Z", fill=_SVG_INK,
                     data_state="open", data_water="in"))
    out.append(_label(190, 366, "water in", size=16, weight="400",
                      data_state="open", data_water="in"))

    out.append(_label(256, 204, "thicker", size=16, weight="700",
                      anchor="start", data_state="open", data_wall="inner"))
    out.append(_label(256, 226, "inner wall", size=16, weight="700",
                      anchor="start", data_state="open", data_wall="inner"))
    out.append(_path("M 252,214 L 218,210", stroke=_SVG_INK, w=1.4,
                     data_state="open"))
    out.append('</g>')

    # ── closed ──
    out.append('<g data-state="closed">')
    out.append(_rect(450, 60, 380, 320, rx=18, fill=_SVG_CARD,
                     stroke=_SVG_INK, w=2.5, data_state="closed",
                     data_panel="closed"))
    out.append(_label(474, 98, "Closed", size=26, weight="800",
                      anchor="start", family=_SVG_DISPLAY, spacing="-.5",
                      data_state="closed"))
    out.append(_mono(474, 120, "water out · limp", size=15,
                     fill=_SVG_ACCENT_TEXT, weight="400",
                     data_state="closed"))

    # No dark shape at all on this side. The absence IS the claim, so the
    # closed pair's `data-gap` rides the one line where the two inner walls
    # have met — a row asking "where did the pore go" finds a stroke, not a
    # fill, and that is the answer.
    out.append(_path("M 480,240 C 502,210 638,210 660,240 Z", fill=_SVG_BAND,
                     data_state="closed", data_cell="upper"))
    out.append(_path("M 480,240 C 502,270 638,270 660,240 Z", fill=_SVG_BAND,
                     data_state="closed", data_cell="lower"))
    out.append(_path("M 480,240 C 502,210 638,210 660,240", stroke=_SVG_INK,
                     w=2, data_state="closed", data_cell="upper",
                     data_wall="outer"))
    out.append(_path("M 480,240 C 502,270 638,270 660,240", stroke=_SVG_INK,
                     w=2, data_state="closed", data_cell="lower",
                     data_wall="outer"))
    out.append(_path("M 480,240 H 660", stroke=_SVG_INK, w=6.5,
                     data_state="closed", data_cell="both",
                     data_wall="inner", data_gap="closed"))

    out.append(_path("M 530,232 V 190", stroke=_SVG_INK, w=3,
                     data_state="closed", data_water="out"))
    out.append(_path("M 523,192 L 537,192 L 530,178 Z", fill=_SVG_INK,
                     data_state="closed", data_water="out"))
    out.append(_label(530, 170, "water out", size=16, weight="400",
                      data_state="closed", data_water="out"))
    out.append(_path("M 610,248 V 290", stroke=_SVG_INK, w=3,
                     data_state="closed", data_water="out"))
    out.append(_path("M 603,288 L 617,288 L 610,302 Z", fill=_SVG_INK,
                     data_state="closed", data_water="out"))
    out.append(_label(610, 324, "water out", size=16, weight="400",
                      data_state="closed", data_water="out"))

    out.append(_label(676, 204, "the two inner", size=16, weight="700",
                      anchor="start", data_state="closed",
                      data_wall="inner"))
    out.append(_label(676, 226, "walls meet —", size=16, weight="700",
                      anchor="start", data_state="closed",
                      data_wall="inner"))
    out.append(_label(676, 248, "no gap left", size=16, weight="700",
                      anchor="start", data_state="closed",
                      data_gap="closed"))
    out.append(_path("M 672,232 L 646,239", stroke=_SVG_INK, w=1.4,
                     data_state="closed"))
    out.append('</g>')

    # ── and where they are: the same leaf, sliced ────────────────────────
    out.append(_mono(24, 424, "THE SAME LEAF, SLICED — TOP OF THE LEAF "
                              "AT THE TOP", size=14, weight="400",
                     spacing="1.4"))
    out.append(_rect(30, 440, 800, 106, fill=_SVG_GROUND))

    # The upper cuticle: ONE rect, 30 to 830. Not a loop, deliberately — the
    # claim is that it is unbroken, and a run that is generated is a run that
    # a future edit can break. It carries `data-run="1"` so the assertion has
    # a span to measure rather than a shape to trust.
    out.append(_rect(30, 440, 800, 10, fill=_SVG_BAND, stroke=_SVG_INK, w=2,
                     data_surface="upper", data_layer="cuticle", data_run="1"))

    # Upper epidermis. The 4-unit gaps between these are CELL WALLS, not
    # pores, which is why they get no `data-run` — the surface claim is made
    # on the cuticle, and these would fail an "unbroken" test for the wrong
    # reason if they answered to the same hook.
    x = 34
    while x + 96 <= 826:
        out.append(_rect(x, 452, 96, 26, rx=7, fill=_SVG_CARD,
                         stroke=_SVG_INK, w=1.8, data_surface="upper",
                         data_layer="epidermis"))
        x += 100

    # Mesophyll: neither surface, so no `data-surface` at all. A cell that
    # answered to "upper" or "lower" here would make both claims unmeasurable.
    cx = 74
    while cx <= 796:
        out.append(_circle(cx, 494, 14, fill=_SVG_CARD, stroke=_SVG_INK,
                           w=1.8, data_layer="mesophyll"))
        cx += 103

    # Lower epidermis, built as runs BETWEEN the pores. Whole cells at 58 wide
    # while there is room for one, then whatever is left over if it is at
    # least 20 — below that it would draw as a sliver that reads as a crack.
    cursor = 34
    for p in _B4_GUARD_PORES:
        stop = p - _B4_GUARD_GAP
        x = cursor
        while stop - x >= 62:
            out.append(_rect(x, 510, 58, 26, rx=7, fill=_SVG_CARD,
                             stroke=_SVG_INK, w=1.8, data_surface="lower",
                             data_layer="epidermis"))
            x += 62
        if stop - x >= 20:
            out.append(_rect(x, 510, stop - x, 26, rx=7, fill=_SVG_CARD,
                             stroke=_SVG_INK, w=1.8, data_surface="lower",
                             data_layer="epidermis"))
        cursor = p + _B4_GUARD_GAP
    x = cursor
    while 826 - x >= 62:
        out.append(_rect(x, 510, 58, 26, rx=7, fill=_SVG_CARD,
                         stroke=_SVG_INK, w=1.8, data_surface="lower",
                         data_layer="epidermis"))
        x += 62
    if 826 - x >= 20:
        out.append(_rect(x, 510, 826 - x, 26, rx=7, fill=_SVG_CARD,
                         stroke=_SVG_INK, w=1.8, data_surface="lower",
                         data_layer="epidermis"))

    # The pores themselves — the same dark as the open pore above, so the two
    # halves of the figure agree about what a hole looks like. Every one of
    # them carries `data-surface="lower"`: that pairing, walked across all
    # three, is the claim.
    for i, p in enumerate(_B4_GUARD_PORES):
        out.append(_rect(p - 8, 510, 16, 36, rx=6, fill=_SVG_INK_BODY,
                         data_pore="1", data_pore_index=i + 1,
                         data_surface="lower"))

    # Two guard cells per pore, in section — the same cells the panels above
    # draw from the surface, which is why they take the same body fill.
    for i, p in enumerate(_B4_GUARD_PORES):
        for cxg in (p - _B4_GUARD_DX, p + _B4_GUARD_DX):
            out.append(_circle(cxg, 523, 12, fill=_SVG_BAND, stroke=_SVG_INK,
                               w=2, data_guard="1", data_pore_index=i + 1,
                               data_surface="lower"))

    # Lower cuticle, broken at every pore for the same reason as the
    # epidermis: the gap is an absence, not an overlay.
    cx0 = 30
    for p in _B4_GUARD_PORES:
        out.append(_rect(cx0, 536, (p - _B4_GUARD_GAP) - cx0, 10,
                         fill=_SVG_BAND, stroke=_SVG_INK, w=2,
                         data_surface="lower", data_layer="cuticle",
                         data_run="1"))
        cx0 = p + _B4_GUARD_GAP
    out.append(_rect(cx0, 536, 830 - cx0, 10, fill=_SVG_BAND, stroke=_SVG_INK,
                     w=2, data_surface="lower", data_layer="cuticle",
                     data_run="1"))

    out.append(_label(30, 572, "Three pores, every one of them on the "
                               "underside — and the top surface "
                               "unbroken.", size=17, weight="700",
                      anchor="start"))
    out.append(_path("M 430,560 V 548", stroke=_SVG_INK, w=1.4))

    out.append('</g>')
    out.append('</svg>')
    return "".join(out)
# ── ⊕ MRB-254 · WS1 #7, b4-gas-exchange-labelled — Design's fig-07, ported ──
#
# Every number below is Design's. Two of her three `<sc-for>` loops are pure
# tables and live up here, out of the drawing body, because they are the parts
# a reader might want to check against her `renderVals()` line by line. The
# third loop — the airway — is not a table at all and cannot be one; it is a
# recursion, and it stays inside the function beside the reason it exists.

# Six pairs of ribs, sweeping down and out from the centre line. `y0` steps by
# 42 and every control point is an offset from it, exactly as she wrote them,
# so the sweep is one shape repeated rather than twelve hand-placed curves.
_B4_THORAX_RIB_PAIRS = 6
_B4_THORAX_RIB_STEP = 42
_B4_THORAX_RIB_TOP = 240
# One inter-rib gap filled, on the right, outside the lung outline. Her
# comment: "positions taken from the rib curve itself so the hatches land
# BETWEEN rib 1 and rib 2 rather than near them" — which is why the x values
# and the y offsets march together instead of the hatches being a plain
# vertical comb.
_B4_THORAX_HATCH = ((464, 27), (474, 33), (483, 39))
# The five sacs of the magnified rosette, and the bronchiole that opens into
# them. Literal in her delivery: this is the one tip drawn large, so nothing
# about it is generated and there is nothing here that can drift run to run.
_B4_THORAX_ROSETTE = ((734, 172, 31), (794, 170, 31), (816, 216, 29),
                      (762, 238, 31), (712, 214, 29))
# The key beneath the plate. `(badge x, badge y, numeral, title, gloss)`.
# 01–05 are the route in, in order; 06 is the machinery around it, and the
# gloss says so in as many words — the figure's whole argument in one row.
_B4_THORAX_KEY = (
    (38, 758, "01", "Nose and mouth",
     "Air warmed, moistened and filtered"),
    (38, 814, "02", "Trachea",
     "Held open by C-shaped rings of cartilage"),
    (38, 870, "03", "Bronchi",
     "One to each lung. No exchange here"),
    (494, 758, "04", "Bronchioles",
     "Divide, and divide again, about 23 times"),
    (494, 814, "05", "Alveoli",
     "Gas exchange — the only place it happens"),
    (494, 870, "06", "Ribs, intercostal muscles and diaphragm",
     "Not the airway. The machinery that moves air"),
)
def _thorax(fig):
    """The route air takes in — nose and mouth to alveoli — with the ribs, the
    intercostal muscles and the diaphragm drawn AROUND the lungs rather than
    along the way in, and one terminal cluster magnified beside it.

    ⚖️ THE BRANCHING IS GENERATED, AND THAT IS THE TEACHING. The lesson's
    punchline is "the bronchi divide about twenty-three times… every one of
    those divisions exists to turn a bag into a surface", and a drawing can
    make that claim two ways. It can hand-draw a plausible-looking tree and
    print the sentence beside it — in which case the sentence is doing all the
    work and the picture is decoration. Or the tree can BE a division: one
    function, called on its own output, each branch 0.7 of its parent's length
    and 1.7 units narrower, until the fourth generation. Design chose the
    second, so "divide, and divide again" is a property of the geometry that a
    student can trace with a finger, and the lung comes out looking full
    rather than hollow because it IS full — thirty branches ending in sixteen
    tips, none of them placed by hand.

    ⚖️ FOUR DIVISIONS, NOT TWENTY-THREE, AND THE DRAWING SAYS SO. Twenty-three
    generations is 8.4 million branches; four is what reads at 576 units wide.
    The simplification is therefore DISCLOSED on the plate — "Four divisions
    are drawn opposite. A real lung has about twenty-three, and only the last
    end in sacs" — rather than left for a student to discover is wrong. That
    note is load-bearing and must survive any future re-cut of this figure:
    without it the drawing quietly asserts a lung has sixteen alveolar
    clusters.

    ⚖️ SACS EXIST ONLY AT TERMINAL TIPS, NEVER ON A BRONCHUS — the named
    assertion, and the one defect a screenshot could not catch. A tree with a
    rosette hung off a mid-tree branch still looks exactly like a lung, and it
    teaches that gas exchange happens along the tubes, which is the
    misconception the whole "route in runs 01 to 05 and STOPS there" framing
    exists to remove. So the encoding is hooked rather than the frame: every
    branch carries `data-branch`, `data-generation`, `data-terminal` and a
    `data-branch-id`, and every sac circle carries `data-sacs` plus the
    `data-branch-id` of the branch it sits on. A row can then collect all 48
    sac circles, resolve each to its branch, and assert that branch is
    terminal — for all of them — and assert the converse both ways: no
    terminal tip without sacs, no non-terminal branch with any.

    ⚖️ AND THE CONVERSE OF THAT, FOR THE MACHINERY. The ribs, the intercostal
    hatching and the diaphragm carry `data-around` and no `data-branch` at
    all. "These are around the lungs, not part of the airway" is then a
    property of the markup rather than a sentence in the key, and a row can
    assert that nothing carrying `data-around` also carries `data-branch`.
    `data-route-step` runs 1–5 on the five numbered callouts, so the order
    (nose and mouth, trachea, bronchi, bronchioles, alveoli) is assertable
    from the drawing itself, against the printed label rather than against a
    position; 06 deliberately has no route step, which is the same fact said a
    third way.

    ⚖️ THE CALLOUT IS DERIVED, NOT PLACED. The ringed cluster is chosen by
    rule — the lowest tip with x > 330, i.e. the lowest tip in the right lung,
    with a fallback to any right-lung tip if the first pass never leaves
    tips[0]. The dashed ring's centre and the leader into badge 05 are both
    computed from that tip. Porting the RESULT (a ring at 396.7, 419.8) would
    have looked identical today and silently detached the ring from the tree
    the first time anyone changed the spread, the trunk length or GENS — the
    ring would go on pointing at empty lung tissue and nothing would warn. So
    the rule is ported, and the ring and leader carry the picked branch's
    `data-branch-id` so a row can check the ring is centred on a tip that is
    actually terminal.

    ⚠️ `Math.round`, NOT `round`. Every coordinate in the tree goes through
    her `r(v) = Math.round(v * 10) / 10`. Python's `round` is banker's
    rounding and JavaScript's `Math.round` is round-half-up, so the two
    disagree on any exact `.5` — and `math.floor(v * 10 + 0.5) / 10` is the JS
    rather than a near-miss of it. None of these sixty coordinates is a tie
    today, which is exactly why this would have stayed safe until somebody
    changed the trunk length from 62 and then quietly lost a tenth on one
    branch.

    ⚠️ THE STROKE WIDTHS GO THROUGH `_n`. `9 - 3 * 1.7` is
    `3.9000000000000004` in IEEE doubles, in JavaScript and in Python alike,
    and `_svg_attrs` interpolates `w` straight into the attribute. Unrouted,
    that is a seventeen-significant-figure stroke width in the shipped file
    and a byte-diff between two builds that differ only in how a number was
    reached. Same width, so nothing visible — which is the point.

    ⛔ EVERY ARROWHEAD IS DESIGN'S OWN TRIANGLE AT HER OWN COORDINATES, not
    `_arrow`. She placed both heads on the magnified rosette by hand, at
    exactly the point where the sac wall meets the capillary, and `_arrow`
    would recompute them from an angle and land them a fraction off her line.
    `_arrow` is for a head this file computes; these are hers.

    ⚠️ THE ONE HUE, AND WHY IT IS NOT CARRYING A FACT ALONE.
    `--ks3-blue-text` paints the capillary in the magnified panel and nothing
    else on the plate. It never has to be seen as blue: it is named in a
    legend line under its own rule ("Blood in the capillary", with the swatch
    drawn at the same 9-unit weight as the vessel), and both directions of
    exchange are DRAWN triangles with bold labels rather than tints. A student
    who cannot separate the blue from the ink loses nothing.

    ⚠️ CLIP IDS ARE DERIVED FROM THE FIGURE ID. Design's are `f7L` and `f7R`,
    which are unique inside a review file holding one figure. A lesson page
    can hold several of these drawings, `id` is document-scoped, and a
    duplicate `clipPath` id means the second figure silently clips to the
    first one's rectangle. Nothing warns; the drawing just loses half of
    itself.
    """
    W, H = 900, 970
    cid = e(fig["id"])
    out = [_svg_open(fig, W, H)]

    # The two frames. Raw markup rather than an emitter call because a
    # <clipPath> carries no paint — there is no paint law to keep here, and
    # `_villus` already sets this precedent in this file.
    out.append(
        '<defs>'
        '<clipPath id="%s-c-chest"><rect x="24" y="54" width="576" '
        'height="620" rx="18"/></clipPath>'
        '<clipPath id="%s-c-tip"><rect x="620" y="54" width="256" '
        'height="620" rx="18"/></clipPath>'
        '</defs>' % (cid, cid))

    # Round caps and joins on everything: ribs, airway and diaphragm are all
    # organic curves, and a mitred join where a 7-unit bronchus meets a
    # 5-unit branch reads as a spike.
    out.append('<g stroke-linecap="round" stroke-linejoin="round">')

    out.append(_rect(24, 54, 576, 620, rx=18, fill=_SVG_CARD, stroke=_SVG_INK,
                     w=2.5))
    out.append(_rect(620, 54, 256, 620, rx=18, fill=_SVG_CARD, stroke=_SVG_INK,
                     w=2.5))

    # ── the chest, seen from the front ──────────────────────────────────────
    out.append('<g clip-path="url(#%s-c-chest)">' % cid)

    # The ribs go down FIRST, so both lung outlines cover them where they
    # overlap: the ribs are in front of the lungs in life, but a drawing that
    # showed them crossing the lung would read as ribs INSIDE it, which is the
    # opposite of the one thing 06 exists to say.
    for i in range(_B4_THORAX_RIB_PAIRS):
        y0 = _B4_THORAX_RIB_TOP + i * _B4_THORAX_RIB_STEP
        for side, d in (
                ("left", "M 300,%s C 238,%s 158,%s 132,%s"
                 % (_n(y0), _n(y0 - 4), _n(y0 + 18), _n(y0 + 48))),
                ("right", "M 324,%s C 386,%s 466,%s 492,%s"
                 % (_n(y0), _n(y0 - 4), _n(y0 + 18), _n(y0 + 48)))):
            out.append(_path(d, stroke=_SVG_INK_FAINT, w=5,
                             data_around="1", data_around_part="rib",
                             data_around_pair=i + 1, data_around_side=side))
    for x, off in _B4_THORAX_HATCH:
        out.append(_path("M %s,%s L %s,%s"
                         % (_n(x), _n(240 + off), _n(x), _n(282 + off)),
                         stroke=_SVG_INK_GHOST, w=3,
                         data_around="1", data_around_part="intercostal"))

    out.append(_path("M 172,300 C 172,268 214,258 292,262 L 296,494 "
                     "C 250,506 190,494 176,452 C 164,412 168,344 172,300 Z",
                     fill=_SVG_INSET, stroke=_SVG_INK, w=2.5,
                     data_lung="left"))
    out.append(_path("M 452,300 C 452,268 410,258 332,262 L 328,494 "
                     "C 374,506 434,494 448,452 C 460,412 456,344 452,300 Z",
                     fill=_SVG_INSET, stroke=_SVG_INK, w=2.5,
                     data_lung="right"))

    out.append(_path("M 128,548 C 200,488 424,488 496,548 "
                     "C 424,506 200,506 128,548 Z",
                     fill=_SVG_BAND, stroke=_SVG_INK, w=2.5,
                     data_around="1", data_around_part="diaphragm"))

    # Every tube is drawn twice — a wide ink stroke, then a narrower inset
    # stroke laid on top of it. That is a lumen, not an outline: the airway
    # reads as a pipe with air inside it and a wall around it, at four
    # different bores, without a single closed path being constructed.
    for d in ("M 262,74 C 262,64 278,60 288,72 L 306,98",
              "M 362,74 C 362,64 346,60 336,72 L 318,98"):
        out.append(_path(d, stroke=_SVG_INK, w=17))
    for d in ("M 262,74 C 262,64 278,60 288,72 L 306,98",
              "M 362,74 C 362,64 346,60 336,72 L 318,98"):
        out.append(_path(d, stroke=_SVG_INSET, w=11))

    out.append(_path("M 312,96 V 228", stroke=_SVG_INK, w=24))
    out.append(_path("M 312,96 V 228", stroke=_SVG_INSET, w=18))
    # The cartilage rings, drawn ACROSS the lumen rather than as C-shapes on
    # its edge — seven of them, evenly spaced, so "held open by rings" is
    # something on the drawing and not only a line in the key.
    out.append(_path("M 303,112 H 321 M 303,128 H 321 M 303,144 H 321 "
                     "M 303,160 H 321 M 303,176 H 321 M 303,192 H 321 "
                     "M 303,208 H 321", stroke=_SVG_INK_GHOST, w=2.4))

    for d in ("M 312,226 C 300,240 280,252 262,268",
              "M 312,226 C 324,240 344,252 362,268"):
        out.append(_path(d, stroke=_SVG_INK, w=18))
    for d in ("M 312,226 C 300,240 280,252 262,268",
              "M 312,226 C 324,240 344,252 362,268"):
        out.append(_path(d, stroke=_SVG_INSET, w=12))

    # ── the recursion ───────────────────────────────────────────────────────
    #
    # Her `tree()`, unchanged: push a segment, and unless this is the last
    # generation, call twice from its far end at ±spread radians, at 0.7 the
    # length. `spread` narrows by 0.06 per generation, which is what stops the
    # fourth generation from splaying out through the lung wall. Both trunks
    # start at the foot of a bronchus, so the tree is physically continuous
    # with the route in rather than a texture placed inside the outline.
    gens = 4
    branches = []
    tips = []

    def _round1(v):
        # `Math.round(v * 10) / 10`. See ⚠️ in the docstring.
        return math.floor(v * 10 + 0.5) / 10

    def _grow(x, y, dx, dy, length, gen):
        nx = x + dx * length
        ny = y + dy * length
        branches.append({
            "d": "M %s,%s L %s,%s" % (_n(_round1(x)), _n(_round1(y)),
                                      _n(_round1(nx)), _n(_round1(ny))),
            "w": max(1.8, 9 - gen * 1.7),
            "gen": gen,
            "terminal": gen >= gens,
        })
        if gen >= gens:
            tips.append({"x": nx, "y": ny, "branch": len(branches) - 1})
            return
        spread = 0.62 - gen * 0.06
        c, s = math.cos(spread), math.sin(spread)
        _grow(nx, ny, dx * c - dy * s, dx * s + dy * c, length * 0.7, gen + 1)
        _grow(nx, ny, dx * c + dy * s, -dx * s + dy * c, length * 0.7, gen + 1)

    def _unit(dx, dy):
        m = math.sqrt(dx * dx + dy * dy)
        return dx / m, dy / m

    ldx, ldy = _unit(-0.5, 1)
    rdx, rdy = _unit(0.5, 1)
    _grow(262, 268, ldx, ldy, 62, 1)
    _grow(362, 268, rdx, rdy, 62, 1)

    for i, b in enumerate(branches):
        out.append(_path(b["d"], stroke=_SVG_INK, w=_n(b["w"]),
                         data_branch="1", data_branch_id="b%d" % (i + 1),
                         data_generation=b["gen"],
                         data_terminal="1" if b["terminal"] else "0"))

    # A rosette of three sacs on every terminal tip, and on nothing else. The
    # centre one is fractionally larger, so the cluster reads as a bunch seen
    # end-on rather than as three beads in a row.
    for t in tips:
        bid = "b%d" % (t["branch"] + 1)
        for dx, dy, r in ((0, 0, 4.4), (-7, 6, 4), (7, 6, 4)):
            out.append(_circle(_round1(t["x"] + dx), _round1(t["y"] + dy), r,
                               fill=_SVG_ACCENT_TINT, stroke=_SVG_ACCENT_TEXT,
                               w=1.4, data_sacs="1", data_branch_id=bid))

    # The ring, by rule. See ⚖️ in the docstring — the fallback is hers and is
    # kept: without it a tree whose lowest tip happened to be in the LEFT lung
    # would leave `pick` at tips[0] and ring a cluster the badge does not
    # point at.
    pick = tips[0]
    for t in tips:
        if t["x"] > 330 and t["y"] > pick["y"]:
            pick = t
    if pick["x"] < 330:
        for t in tips:
            if t["x"] > 330:
                pick = t
    pick_id = "b%d" % (pick["branch"] + 1)
    ring_x = _round1(pick["x"])
    ring_y = _round1(pick["y"] + 4)
    out.append(_circle(ring_x, ring_y, 27, stroke=_SVG_INK, w=2, dash="6 5",
                       data_callout="ring", data_branch_id=pick_id))
    out.append('</g>')

    out.append(_mono(250, 88, "nose", size=13, weight="400", anchor="end"))
    out.append(_mono(374, 88, "mouth", size=13, weight="400"))

    # ── the route in, 01 to 05 ──────────────────────────────────────────────
    #
    # Built as one list so the ORDER is a property of the data rather than of
    # where four blocks of markup happen to sit, and so step 05 — whose badge
    # leader is computed from the ring above — joins the same loop as the four
    # placed ones instead of being a special case emitted somewhere else.
    badge_x, badge_y = 496, 438
    route = (
        (1, "nose-and-mouth", 200, 148, "01", "M 214,150 L 300,152",
         "nose and mouth", 200, 122, "middle"),
        (2, "trachea", 200, 204, "02", "M 214,204 L 298,206",
         "trachea", 200, 236, "middle"),
        (3, "bronchi", 412, 212, "03", "M 398,218 L 356,254",
         "bronchi", 436, 218, "start"),
        (4, "bronchioles", 540, 330, "04", "M 526,332 L 444,340",
         "bronchioles", 512, 306, "start"),
        (5, "alveoli", badge_x, badge_y, "05",
         "M %s,%s L %s,%s" % (_n(badge_x - 14), _n(badge_y + 4),
                              _n(ring_x + 24), _n(ring_y - 8)),
         "alveoli", 504, 470, "start"),
    )
    for step, part, bx, by, num, leader, name, nx, ny, anchor in route:
        hook = {"data_route_step": step, "data_route_part": part}
        if step == 5:
            hook["data_branch_id"] = pick_id
            hook["data_callout"] = "leader"
        out.append(_path(leader, stroke=_SVG_INK, w=1.4, **hook))
        hook.pop("data_callout", None)
        out.append(_circle(bx, by, 14, fill=_SVG_BAND, stroke=_SVG_INK, w=2,
                           **hook))
        out.append(_mono(bx, by + 6, num, size=15, fill=_SVG_INK, weight="400",
                         anchor="middle", **hook))
        out.append(_label(nx, ny, name, size=15, weight="700", anchor=anchor,
                          **hook))

    # ── 06, the machinery — no route step, deliberately ─────────────────────
    out.append(_path("M 526,560 L 498,550", stroke=_SVG_INK, w=1.4,
                     data_around="1"))
    out.append(_circle(540, 562, 14, fill=_SVG_BAND, stroke=_SVG_INK, w=2,
                       data_around="1"))
    out.append(_mono(540, 568, "06", size=15, fill=_SVG_INK, weight="400",
                     anchor="middle", data_around="1"))

    out.append(_label(506, 266, "ribs", size=15, weight="700", anchor="start",
                      data_around="1", data_around_part="rib"))
    out.append(_path("M 502,262 L 484,272", stroke=_SVG_INK, w=1.4,
                     data_around="1", data_around_part="rib"))
    out.append(_label(506, 200, "intercostal", size=15, weight="700",
                      anchor="start", data_around="1",
                      data_around_part="intercostal"))
    out.append(_label(506, 218, "muscles", size=15, weight="700",
                      anchor="start", data_around="1",
                      data_around_part="intercostal"))
    out.append(_path("M 502,224 L 468,262", stroke=_SVG_INK, w=1.4,
                     data_around="1", data_around_part="intercostal"))
    out.append(_label(312, 588, "diaphragm", size=15, weight="700",
                      data_around="1", data_around_part="diaphragm"))

    out.append(_mono(48, 644, "The lungs are drawn full of branching because "
                              "a lung is not", size=13, weight="400"))
    out.append(_mono(48, 662, "a bag with air in it. It is closer to a "
                              "sponge.", size=13, weight="400"))

    # ── one tip, magnified ──────────────────────────────────────────────────
    out.append('<g clip-path="url(#%s-c-tip)">' % cid)
    out.append(_path("M 632,132 C 660,138 692,150 722,164", stroke=_SVG_INK,
                     w=14))
    out.append(_path("M 632,132 C 660,138 692,150 722,164", stroke=_SVG_INSET,
                     w=8))
    for cx, cy, r in _B4_THORAX_ROSETTE:
        out.append(_circle(cx, cy, r, fill=_SVG_ACCENT_TINT,
                           stroke=_SVG_ACCENT_TEXT, w=2.5, data_sac_wall="1"))
    # The capillary: an ink stroke with the blue laid inside it, the same
    # lumen construction as the airway. It crosses IN FRONT of the sacs, which
    # is what makes "the wall between air and blood is one cell thick" a thing
    # you can point at rather than a measurement.
    cap = ("M 630,286 C 676,266 700,300 744,288 C 788,276 802,306 848,294")
    out.append(_path(cap, stroke=_SVG_INK, w=15))
    out.append(_path(cap, stroke=_SVG_BLUE_TEXT, w=9, data_capillary="1"))
    # Both exchange arrows are hers, shaft and head. See ⛔ in the docstring.
    out.append(_path("M 706,244 V 276", stroke=_SVG_INK, w=2.6,
                     data_exchange="oxygen-in"))
    out.append(_path("M 700,272 L 712,272 L 706,284 Z", fill=_SVG_INK,
                     stroke="none", data_exchange="oxygen-in"))
    out.append(_path("M 812,282 V 250", stroke=_SVG_INK, w=2.6,
                     data_exchange="carbon-dioxide-out"))
    out.append(_path("M 806,254 L 818,254 L 812,242 Z", fill=_SVG_INK,
                     stroke="none", data_exchange="carbon-dioxide-out"))
    # ⊕ MRB-254 · SAME HEAD, DIFFERENT ROUTE. The leader used to climb the
    # right-hand side — 824,394 up to 816,248 — and "carbon dioxide out" spans
    # x 731–864 at y 316–334, so it went in the bottom of that label and out
    # the top: a hairline drawn through the words naming the arrow beside it.
    # The head does not move. It sits at 816,248, three units under the lower
    # right sac, which is where the wall between air and blood actually is, and
    # moving it would trade a legible label for a wrong one.
    #
    # What moves is the climb. There is exactly one clear corridor through the
    # exchange-label line: "oxygen in" ends at 704.8 and "carbon dioxide out"
    # begins at 730.7, so the leader now leaves the note's leading edge at
    # x=724 and threads that 26-unit gap at x 721–725 before turning right for
    # the sacs. It crosses the capillary on the way, as Design's did.
    out.append(_path("M 724,392 C 714,320 716,286 816,248", stroke=_SVG_INK,
                     w=1.4))
    out.append('</g>')

    out.append(_mono(636, 86, "ONE TIP, MAGNIFIED", size=13, weight="400",
                     spacing="1.2"))
    out.append(_label(636, 330, "oxygen in", size=15, weight="700",
                      anchor="start", data_exchange="oxygen-in"))
    out.append(_label(864, 330, "carbon dioxide out", size=15, weight="700",
                      anchor="end", data_exchange="carbon-dioxide-out"))
    out.append(_mono(864, 408, "wall one cell thick", size=13,
                     fill=_SVG_ACCENT_TEXT, weight="400", anchor="end"))

    out.append(_path("M 636,438 H 864", stroke=_SVG_RULE, w=2))
    out.append(_mono(636, 468, "about 500 million of these,", size=13,
                     fill=_SVG_INK, weight="400"))
    out.append(_mono(636, 486, "each wrapped in capillaries", size=13,
                     fill=_SVG_INK, weight="400"))

    # The disclosure. See ⚖️ in the docstring: this is the note that keeps the
    # four drawn generations honest, and it is the last thing to cut.
    out.append(_path("M 636,516 H 864", stroke=_SVG_RULE, w=2))
    for i, line in enumerate(("Four divisions are drawn",
                              "opposite. A real lung has",
                              "about twenty-three, and",
                              "only the last end in sacs.")):
        out.append(_mono(636, 546 + i * 18, line, size=13, weight="400"))

    # The legend line the one hue depends on, at the vessel's own weight.
    out.append(_path("M 636,626 H 864", stroke=_SVG_RULE, w=2))
    out.append(_path("M 640,656 h 28", stroke=_SVG_BLUE_TEXT, w=9))
    out.append(_label(680, 662, "Blood in the capillary", size=16,
                      weight="700", anchor="start"))

    # ── the key ─────────────────────────────────────────────────────────────
    out.append(_mono(24, 712, "THE ROUTE IN, AND THE MACHINERY AROUND IT",
                     size=13, weight="400", spacing="1.2"))
    out.append(_path("M 24,724 H 876", stroke=_SVG_RULE, w=2))
    for bx, by, num, title, gloss in _B4_THORAX_KEY:
        out.append(_circle(bx, by, 14, fill=_SVG_BAND, stroke=_SVG_INK, w=2))
        out.append(_mono(bx, by + 6, num, size=15, fill=_SVG_INK,
                         weight="400", anchor="middle"))
        out.append(_label(bx + 26, by - 1, title, size=18, weight="700",
                          anchor="start"))
        out.append(_label(bx + 26, by + 19, gloss, size=15,
                          fill=_SVG_INK_BODY, weight="400", anchor="start"))

    out.append(_path("M 24,922 H 876", stroke=_SVG_RULE, w=2))
    out.append(_label(24, 954, "Every one of those divisions exists to turn a "
                               "bag into a surface.", size=16, weight="700",
                      anchor="start"))

    out.append('</g>')
    out.append('</svg>')
    return "".join(out)
# renderers: ═══ END B3 ═══


# renderers: ═══ BEGIN B4 ═══
#
# Five lessons, five instruments, and every one of them on ink.
#
# ⚠️ THAT UNIFORMITY IS THE HAZARD, NOT A CONVENIENCE. `.ks3-dark p` is (0,1,1)
# and a bare instrument class is (0,1,0), so an unscoped colour rule LOSES —
# and because all five B4 practicals are `ks3-block ks3-dark ks3-practical`,
# that trap would bite all five lessons at once rather than one. Every colour
# rule these five hang on is scoped `.ks3-dark …` in `shared/ks3.css`, and the
# panels that invert to the CREAM ground inside the ink block (gas-compare's
# closing paragraph, bell-jar's chain, crossing-counter's note,
# fault-bench's reveal, two-process-ledger's verdict) are the ones that would
# silently lose: `.ks3-dark p` would paint #E7DECE on #FBF3E6 at about 1.2:1.
#
# ⚠️ NOTHING IN B4 ANIMATES AND NOTHING USES A TIMER. All five instruments are
# pure functions of their controls' state; the only motion in the unit is a CSS
# transition, and the stylesheet's reduced-motion block removes every one. There
# is no rAF loop in this unit to check `prefers-reduced-motion` inside.


def r_gas_compare(a, act_id):
    """⊕ b4-01 `#s-air` — four gases, a prediction on each, then both bags.

    ⚖️ THE NUMERAL IS NOT A CAPTION FOR THE BAR, IT IS THE CORRECTION TO IT.
    Carbon dioxide is 0.04% inhaled, and a bar drawn honestly at 0.04% of its
    track is zero pixels wide — so the bar is clamped to `min_bar_pct`, which
    on Design's payload makes it about thirty-seven times too wide. That clamp
    is the one dishonest pixel in the unit. It is survivable only because the
    figure sits beside the bar in every cell, which is why `in_label` and
    `out_label` are required and why this renderer will not compose them.

    ⚖️ `in_label` / `out_label` ARE AUTHORED, NOT FORMATTED FROM THE PERCENT.
    Water vapour's two cells read "variable, often low" and "saturated" —
    Design's deliberate refusal to give a percentage for a figure that has
    none. A template filling "{pct}%" would print "1%" there and invent a
    measurement. The percents drive the BARS and nothing else.

    ⚠️ THE PREDICTION IS NOT MARKED WHILE IT IS BEING MADE. Only the mastery
    ladder marks correctness (R3), so the three buttons per row take
    `aria-pressed` and no verdict class until the reveal opens. What happens at
    the reveal is not marking either: the row that predicted correctly keeps
    its panel and its border goes to alert, and the row that did not loses the
    panel. Design draws exactly that, and the count beside the button changes
    from "committed" to "predicted correctly" in the same instant.
    """
    gases = a.get("gases") or []
    if len(gases) < 2:
        raise ValueError(
            "gas-compare %r declares %d gas(es). The block is a comparison of "
            "two bags across the gases in them, and one row cannot make it."
            % (act_id, len(gases)))

    choices = a.get("choices") or []
    if len(choices) < 2:
        raise ValueError(
            "gas-compare %r declares %d choice(s). A prediction needs "
            "something to choose between." % (act_id, len(choices)))
    for c in choices:
        if not (c.get("id") and c.get("label")):
            raise ValueError(
                "gas-compare %r choice %r needs `id` and `label`."
                % (act_id, c.get("id")))
    choice_ids = [c["id"] for c in choices]

    for g in gases:
        for key in ("id", "name", "change", "in_label", "out_label", "verdict"):
            if not g.get(key):
                raise ValueError(
                    "gas-compare %r gas %r is missing %r. `in_label` and "
                    "`out_label` are the printed figures and are authored: "
                    "water vapour's read “variable, often low” and "
                    "“saturated”, and composing them from the "
                    "percentages would print a measurement Design refused to "
                    "give." % (act_id, g.get("id"), key))
        if g["change"] not in choice_ids:
            raise ValueError(
                "gas-compare %r gas %r predicts %r, which is not one of the "
                "offered choices %s. A row whose right answer is not on the "
                "buttons can never be predicted correctly, and the closing "
                "count would be wrong for every student."
                % (act_id, g["id"], g["change"], choice_ids))
        for key in ("in_pct", "out_pct"):
            v = g.get(key)
            if not isinstance(v, (int, float)) or isinstance(v, bool) or v < 0:
                raise ValueError(
                    "gas-compare %r gas %r has %s %r; it is the bar's width as "
                    "a percentage of its track and cannot be negative."
                    % (act_id, g["id"], key, v))

    count = a.get("count") or {}
    if not (count.get("committed") and count.get("scored")):
        raise ValueError(
            "gas-compare %r needs both `count.committed` and `count.scored`. "
            "The line beside the button says how many rows are committed "
            "before the reveal and how many were right after it — one "
            "string cannot do both, and a blank one is a readout that goes "
            "dark at the moment the block pays off." % act_id)

    table = a.get("table") or {}
    missing = sorted({"gas", "inhaled", "exhaled"} - set(table))
    if missing:
        raise ValueError(
            "gas-compare %r table is missing %s. The two data headings are "
            "also the per-cell captions on a narrow screen, where the columns "
            "stack and an uncaptioned figure is a number with nothing saying "
            "which bag it came from." % (act_id, ", ".join(missing)))

    for key in ("reveal_label", "close_lead", "close"):
        if not a.get(key):
            raise ValueError(
                "gas-compare %r declares no %r." % (act_id, key))

    min_bar = float(a.get("min_bar_pct") or 1.5)

    rows = "".join(
        '<li class="ks3-gas-row" data-gasrow="%s" data-change="%s">'
        '<p class="ks3-gas-rowname">%s</p>'
        '<div class="ks3-gas-choices">%s</div></li>'
        % (e(g["id"]), e(g["change"]), t(g["name"]),
           "".join(
               '<button type="button" class="ks3-gas-choice" data-gas="%s" '
               'data-choice="%s" aria-pressed="false">%s</button>'
               % (e(g["id"]), e(c["id"]), t(c["label"]))
               for c in choices))
        for g in gases)

    def cell(g, side):
        pct = float(g["in_pct"] if side == "in" else g["out_pct"])
        label = g["in_label"] if side == "in" else g["out_label"]
        cap = table["inhaled"] if side == "in" else table["exhaled"]
        return ('<div class="ks3-gas-cell" data-side="%s">'
                '<p class="ks3-gas-cap">%s</p>'
                '<p class="ks3-gas-num">%s</p>'
                '<span class="ks3-gas-track">'
                '<span class="ks3-gas-bar" style="width:%s%%"></span>'
                '</span></div>'
                % (side, t(cap), t(label), ("%.2f" % max(min_bar, pct))))

    body = "".join(
        '<div class="ks3-gas-grid ks3-gas-body" data-gasout="%s" data-band="%d">'
        '<div class="ks3-gas-name">'
        '<p class="ks3-gas-gname">%s</p>'
        '<p class="ks3-gas-verdict">%s</p></div>%s%s</div>'
        % (e(g["id"]), i % 2, t(g["name"]), t(g["verdict"]),
           cell(g, "in"), cell(g, "out"))
        for i, g in enumerate(gases))

    return ('<div class="ks3-gas" data-gas data-total="%d" '
            'data-committed="%s" data-scored="%s">'
            '<ul class="ks3-gas-rows" role="list">%s</ul>'
            '<div class="ks3-gas-foot">'
            '<button type="button" class="ks3-reveal-btn ks3-gas-open" '
            'data-gas-open disabled>%s</button>'
            '<span class="ks3-gas-count" data-gas-count role="status">%s</span>'
            '</div>'
            '<div class="ks3-gas-table" data-gas-table hidden>'
            '<div class="ks3-gas-grid ks3-gas-head">'
            '<p class="ks3-gas-hname">%s</p>'
            '<p class="ks3-gas-hcell">%s</p>'
            '<p class="ks3-gas-hcell" data-side="out">%s</p></div>%s</div>'
            '<p class="ks3-gas-close" data-gas-close hidden>'
            '<strong>%s</strong> %s</p></div>'
            % (len(gases), e(count["committed"]), e(count["scored"]), rows,
               t(a["reveal_label"]),
               t(count["committed"].replace("{n}", "0")
                 .replace("{total}", str(len(gases)))),
               t(table["gas"]), t(table["inhaled"]), t(table["exhaled"]), body,
               t(a["close_lead"]), rich(a["close"])))
def r_bell_jar(a, act_id):
    """⊕ b4-02 `#s-model` — the bell jar, and the chain that is the instrument.

    ⚖️ THE CHAIN IS THE INSTRUMENT, NOT THE PICTURE. NOTES-B4 §3.2 says it in
    one line and it decides the whole shape of this renderer: the jar drawing
    is a rectangle whose height scales and a circle that scales with it, and if
    that were the block, the block would be decoration. The chain's job is that
    its FIRST line is always the muscle and its LAST line is always the air —
    the exact order `#s-ladder` rung 1 then asks for. Rendering it as static
    text loses the lesson's central confrontation, so all three phases are
    authored in full and the live numbers are filled into them.

    ⚖️ THREE PHASES, ALL THREE AUTHORED, BECAUSE ALL THREE ARE REACHABLE. The
    slider passes through `rest` on its way anywhere, and Design writes a
    distinct four-line chain for it — "No net air movement in either
    direction." A missing phase is not a rare state, it is the state the
    instrument opens in.

    ⚠️ `{pressure}` IS SIGNED AND `{pressure_abs}` IS NOT, and the difference is
    a sentence's meaning. Design's `out` chain reads "rises to 0.18 kPa above
    atmospheric" from `Math.abs(pressure)`; its `in` chain reads "falls to
    -0.79 kPa below atmospheric" from the signed value — a double negative on
    the drawn page. Both placeholders exist here and the renderer takes no
    view: which one a sentence uses is a property of that sentence, and the
    sentence is the author's. See `docs/ks3/b4-inventory/PAYLOAD-SCHEMA.md` §2.

    ⚠️ `pressure_zero` MUST AGREE WITH `rest`. The phase a chain shows is
    decided by the slider against `rest`; the pressure printed inside that
    chain is decided by the slider against `pressure_zero`. Let them differ and
    there is a band of the slider that says "at rest between breaths" while
    printing a pressure difference, or says "breathing in" at 0.00 kPa. The
    renderer raises rather than shipping a model that disagrees with its own
    readout.
    """
    model = a.get("model") or {}
    for key in ("volume_base", "volume_span", "pressure_zero", "pressure_span"):
        v = model.get(key)
        if not isinstance(v, (int, float)) or isinstance(v, bool):
            raise ValueError(
                "bell-jar %r model.%s is %r. The four numbers are the model's "
                "physics and are authored, because they are the figures the "
                "chain quotes and the science owner has to be able to correct "
                "them without opening the generator."
                % (act_id, key, v))

    start = int(a.get("start", 20))
    rest = int(a.get("rest", 20))
    for name, v in (("start", start), ("rest", rest)):
        if not 0 <= v <= 100:
            raise ValueError(
                "bell-jar %r %s is %d; the slider runs 0–100."
                % (act_id, name, v))
    if abs(float(model["pressure_zero"]) * 100 - rest) > 1e-9:
        raise ValueError(
            "bell-jar %r has rest=%d but model.pressure_zero=%r (which is "
            "%.1f on the slider). The phase and the pressure would then "
            "disagree: there would be slider positions reading “at "
            "rest” with a pressure difference printed under them."
            % (act_id, rest, model["pressure_zero"],
               float(model["pressure_zero"]) * 100))

    readouts = a.get("readouts") or {}
    missing = sorted({"volume_label", "volume_format", "pressure_label",
                      "pressure_format", "outside_label", "outside_value",
                      "air_label"} - set(readouts))
    if missing:
        raise ValueError(
            "bell-jar %r readouts is missing %s. Four rows are drawn and every "
            "one of them is a claim: the outside pressure row is FIXED at "
            "atmospheric and is the reference the inside row is read against, "
            "so an unlabelled or absent one leaves the inside figure meaning "
            "nothing." % (act_id, ", ".join(missing)))

    for key in ("slider_label", "slider_aria", "jar_label", "readouts_label",
                "chain_label"):
        if not a.get(key):
            raise ValueError(
                "bell-jar %r declares no %r. `slider_aria` is the "
                "visually-hidden label on the range input and is the only "
                "thing a screen-reader user has to go on."
                % (act_id, key))

    presets = a.get("presets") or []
    if not presets:
        raise ValueError(
            "bell-jar %r declares no presets. Design draws two — breathe "
            "in and breathe out — and they are what make the two ends of "
            "the slider reachable in one press." % act_id)
    for p in presets:
        if not p.get("label"):
            raise ValueError(
                "bell-jar %r preset %r has no label." % (act_id, p.get("id")))
        v = p.get("value")
        if not isinstance(v, int) or isinstance(v, bool) or not 0 <= v <= 100:
            raise ValueError(
                "bell-jar %r preset %r has value %r; it is a slider position "
                "0–100." % (act_id, p.get("id"), v))

    phases = a.get("phases") or {}
    missing = sorted({"in", "out", "rest"} - set(phases))
    if missing:
        raise ValueError(
            "bell-jar %r declares no %s phase. The slider passes through all "
            "three and opens in one of them; a phase with no text is a chain "
            "that goes blank while the student is holding the control."
            % (act_id, ", ".join(missing)))
    for name in ("in", "out", "rest"):
        ph = phases[name] or {}
        for key in ("phase_label", "dia_label", "air", "note"):
            if not ph.get(key):
                raise ValueError(
                    "bell-jar %r phase %r is missing %r."
                    % (act_id, name, key))
        chain = ph.get("chain") or []
        if len(chain) != 4:
            raise ValueError(
                "bell-jar %r phase %r declares %d chain line(s), not 4. The "
                "four steps are muscle → volume → pressure → "
                "air, and the count is the argument: drop one and the "
                "remaining three no longer say that the air is last."
                % (act_id, name, len(chain)))

    def figures(dia):
        """Volume, signed pressure and its magnitude at a slider position."""
        f = dia / 100.0
        vol = float(model["volume_base"]) + f * float(model["volume_span"])
        pres = -(f - float(model["pressure_zero"])) * float(model["pressure_span"])
        return vol, pres

    def fill(tpl, dia):
        vol, pres = figures(dia)
        return (tpl.replace("{volume}", "%.1f" % vol)
                .replace("{pressure_abs}", "%.2f" % abs(pres))
                .replace("{pressure}", "%.2f" % pres))

    open_phase = "in" if start > rest else ("out" if start < rest else "rest")

    def switched(cls, attr, value_of):
        """Emit every authored variant, show the one the slider opens on."""
        return "".join(
            '<span class="%s" data-%s="%s"%s>%s</span>'
            % (cls, attr, name, "" if name == open_phase else " hidden",
               value_of(phases[name]))
            for name in ("in", "out", "rest"))

    chains = "".join(
        '<ol class="ks3-bell-chain" data-chain="%s"%s>%s</ol>'
        % (name, "" if name == open_phase else " hidden",
           "".join(
               '<li class="ks3-bell-step"%s>%s</li>'
               % ((' data-format="%s"' % e(line))
                  if ("{volume}" in line or "{pressure" in line) else "",
                  t(fill(line, start)))
               for line in phases[name]["chain"]))
        for name in ("in", "out", "rest"))

    notes = "".join(
        '<p class="ks3-bell-note" data-note="%s"%s>%s</p>'
        % (name, "" if name == open_phase else " hidden",
           rich(phases[name]["note"]))
        for name in ("in", "out", "rest"))

    preset_html = "".join(
        '<button type="button" class="ks3-reveal-btn ks3-bell-preset" '
        'data-preset="%d">%s</button>' % (p["value"], t(p["label"]))
        for p in presets)

    vol0, pres0 = figures(start)
    sid = "bell-" + str(act_id)

    return ('<div class="ks3-bell" data-bell data-rest="%d" data-vbase="%s" '
            'data-vspan="%s" data-pzero="%s" data-pspan="%s">'
            '<div class="ks3-bell-panels">'
            '<div class="ks3-bell-card">'
            '<p class="ks3-bell-cap">%s</p>'
            '<div class="ks3-bell-jar" aria-hidden="true">'
            '<span class="ks3-bell-chest" data-chest>'
            '<span class="ks3-bell-lung" data-lung></span></span></div>'
            '<p class="ks3-bell-phase" role="status">%s</p></div>'
            '<div class="ks3-bell-card">'
            '<p class="ks3-bell-cap">%s</p>'
            '<dl class="ks3-bell-reads">'
            '<div class="ks3-bell-read"><dt>%s</dt>'
            '<dd data-read="volume" data-format="%s">%s</dd></div>'
            '<div class="ks3-bell-read"><dt>%s</dt>'
            '<dd data-read="pressure" data-format="%s">%s</dd></div>'
            '<div class="ks3-bell-read"><dt>%s</dt><dd>%s</dd></div>'
            '<div class="ks3-bell-read"><dt>%s</dt><dd>%s</dd></div>'
            '</dl></div></div>'
            '<div class="ks3-bell-control">'
            '<div class="ks3-bell-controlhead">'
            '<p class="ks3-bell-cap">%s</p>'
            '<p class="ks3-bell-dia">%s</p></div>'
            '<label class="ks3-sr-only" for="%s">%s</label>'
            '<input class="ks3-b4slider ks3-bell-slider" type="range" id="%s" '
            'min="0" max="100" step="1" value="%d" data-bell-slider>'
            '<div class="ks3-bell-presets">%s</div></div>'
            '<div class="ks3-bell-chainpanel">'
            '<p class="ks3-bell-chainlabel">%s</p>%s%s</div></div>'
            % (rest, model["volume_base"], model["volume_span"],
               model["pressure_zero"], model["pressure_span"],
               t(a["jar_label"]),
               switched("ks3-bell-phaseval", "phase",
                        lambda ph: t(ph["phase_label"])),
               t(a["readouts_label"]),
               t(readouts["volume_label"]), e(readouts["volume_format"]),
               t(readouts["volume_format"].replace("{volume}", "%.1f" % vol0)),
               t(readouts["pressure_label"]), e(readouts["pressure_format"]),
               t(readouts["pressure_format"].replace(
                   "{pressure}", "%+.2f" % pres0)),
               t(readouts["outside_label"]), t(readouts["outside_value"]),
               t(readouts["air_label"]),
               switched("ks3-bell-airval", "air", lambda ph: t(ph["air"])),
               t(a["slider_label"]),
               switched("ks3-bell-diaval", "dia", lambda ph: t(ph["dia_label"])),
               e(sid), t(a["slider_aria"]), e(sid), start, preset_html,
               t(a["chain_label"]), chains, notes))
def r_crossing_counter(a, act_id):
    """⊕ b4-03 `#s-gradient` — four states, and neither bar ever reads zero.

    ⚖️ THE OUTWARD BAR IS THE LESSON. `PART-10`/`PART-11` have been confronted
    twice before this and survive because every picture a student has seen of
    diffusion shows movement one way. Here the outward count is on screen in
    all four states, including the one where both flows are stopped and the
    two counts are IDENTICAL — molecules still crossing, nothing settled,
    nothing finished, only the imbalance gone. A state whose outward count fell
    to zero would teach the belief this instrument exists to remove, so
    `blood_kpa` must be positive and the renderer raises when it is not.

    ⚖️ FOUR STATES, ENUMERATED, NOT SIMULATED. NOTES-B4 §6 is explicit: the
    table is a lookup and the four narrative notes are hand-written per state.
    Computing the pair from two rate terms would make the four notes
    unwritable, because each one says something different about WHY the two
    counts came together, and only three of the four are the same mechanism.

    ⚖️ EVERY NUMBER ON THIS INSTRUMENT IS COMPUTED HERE, AT BUILD TIME, and
    ships as a finished string on the state's own element. The two bar widths
    and the five printed figures come out of one pair of kPa values per state,
    in one place, so a bar and the figure beside it cannot disagree. The wiring
    copies them; it computes nothing. This is `gut-journey`'s rule and it holds
    for the same reason.

    ⚠️ THE BOTH-ON NOTE QUOTES ITS OWN NUMBERS — "1197 in, 477 out" —
    and they are `13.3 × 90` and `5.3 × 90`. Nothing can check a
    figure embedded in prose, and nothing here tries. If a science review moves
    a kPa value, that sentence moves with it.
    """
    states = a.get("states") or []
    switches = a.get("switches") or []
    if len(switches) != 2:
        raise ValueError(
            "crossing-counter %r declares %d switch(es), not 2. Four states is "
            "two switches squared, and the lookup table is built from the pair."
            % (act_id, len(switches)))
    for w in switches:
        for key in ("id", "on_label", "off_label"):
            if not w.get(key):
                raise ValueError(
                    "crossing-counter %r switch %r is missing %r. The caption "
                    "IS the state — Design's switch says “Breathing: "
                    "stopped” rather than greying out — so both "
                    "halves are authored."
                    % (act_id, w.get("id"), key))
    if [w["id"] for w in switches] != ["breathing", "blood_flow"]:
        raise ValueError(
            "crossing-counter %r switches are %s; they must be `breathing` "
            "then `blood_flow`, because `states[]` is keyed on those two names."
            % (act_id, [w.get("id") for w in switches]))

    if len(states) != 4:
        raise ValueError(
            "crossing-counter %r declares %d state(s), not 4."
            % (act_id, len(states)))
    seen = {}
    for st in states:
        for key in ("breathing", "blood_flow"):
            if not isinstance(st.get(key), bool):
                raise ValueError(
                    "crossing-counter %r state %r has %s=%r; it is a bool."
                    % (act_id, st.get("note", "")[:24], key, st.get(key)))
        key = (st["breathing"], st["blood_flow"])
        if key in seen:
            raise ValueError(
                "crossing-counter %r declares breathing=%s blood_flow=%s "
                "twice. Both switches are reachable, so a duplicated state "
                "means a missing one." % (act_id, key[0], key[1]))
        seen[key] = st
        if not st.get("note"):
            raise ValueError(
                "crossing-counter %r state breathing=%s blood_flow=%s has no "
                "note. Each of the four says something different about why the "
                "counts came together, and a state with none is the readout "
                "going silent exactly where the argument is."
                % (act_id, key[0], key[1]))
        for field in ("alveolar_kpa", "blood_kpa"):
            v = st.get(field)
            if not isinstance(v, (int, float)) or isinstance(v, bool) or v <= 0:
                raise ValueError(
                    "crossing-counter %r state breathing=%s blood_flow=%s has "
                    "%s=%r. It must be positive: it is a bar width as well as "
                    "a readout, and an outward bar that disappears teaches the "
                    "one-way picture the block exists to kill."
                    % (act_id, key[0], key[1], field, v))
    missing = [k for k in ((True, True), (True, False), (False, True),
                           (False, False)) if k not in seen]
    if missing:
        raise ValueError(
            "crossing-counter %r declares no state for %s. Every combination "
            "is one tap away from every other." % (act_id, missing))

    tiles = a.get("tiles") or {}
    tmissing = sorted({"alveolar", "blood", "net"} - set(tiles))
    if tmissing:
        raise ValueError(
            "crossing-counter %r tiles is missing %s."
            % (act_id, ", ".join(tmissing)))
    bars = a.get("bars") or {}
    bmissing = sorted({"into", "out_of"} - set(bars))
    if bmissing:
        raise ValueError(
            "crossing-counter %r bars is missing %s. The outward bar is named "
            "as explicitly as the inward one because a student who reads only "
            "one label reads only one direction."
            % (act_id, ", ".join(bmissing)))
    # `kpa_format` still does real work — it feeds the footnote line (6.15),
    # which is where the audit puts the partial pressures. `kpa_foot_format`
    # is the sentence around them.
    for key in ("kpa_format", "kpa_foot_format", "crossing_format",
                "net_zero"):
        if not a.get(key):
            raise ValueError(
                "crossing-counter %r declares no %r." % (act_id, key))

    # ── MRB-257 (6.15) · THE SIDE LABEL IS DERIVED, NEVER AUTHORED ────────
    # The audit asks for the two tiles to read "more oxygen here" / "less
    # oxygen here" instead of "13.3 kPa" / "5.3 kPa", because partial pressure
    # is not met until A-level and the bench works without the numbers.
    #
    # ⚠️ APPLIED LITERALLY THAT SHIPS A FALSE STATEMENT, which is why 3b-i
    # refused it and MRB-257 then ruled the shape rather than the strings. The
    # tile labels are static; the VALUES are per-state; and in the both-stopped
    # state both sides read 9.3 kPa, so a fixed "more oxygen here" is wrong
    # there. That is precisely the prose-contradicts-instrument class this run
    # exists to kill.
    #
    # RULED: compare the two values per state and emit more / less / the same.
    # True in every reachable state BY CONSTRUCTION, including the equal one —
    # which is a state worth a student seeing, because it is what "diffusion
    # has stopped" looks like. The kPa figures move to the footnote.
    #
    # ⚖️ THE GENERAL RULE THIS IS AN INSTANCE OF (build contract, decision 8):
    # any comparative label over per-state values is COMPUTED from those
    # values, never authored beside them. An authored comparative is a second
    # source for a fact the numbers already carry, and the two drift the moment
    # a state is added or a number moves.
    sides = a.get("side_labels") or {}
    smissing = sorted({"more", "less", "same"} - set(sides))
    if smissing:
        raise ValueError(
            "crossing-counter %r side_labels is missing %s. All three are "
            "reachable — the two switches both off leaves the sides EQUAL — "
            "and a comparative that cannot say 'the same' is false in that "
            "state (6.15)." % (act_id, ", ".join(smissing)))

    per_kpa = float(a.get("crossings_per_kpa") or 90)
    max_cross = float(a.get("max_crossings") or 1250)
    if per_kpa <= 0 or max_cross <= 0:
        raise ValueError(
            "crossing-counter %r needs positive `crossings_per_kpa` and "
            "`max_crossings`." % act_id)
    biggest = max(max(st["alveolar_kpa"], st["blood_kpa"]) for st in states)
    if biggest * per_kpa > max_cross:
        raise ValueError(
            "crossing-counter %r scales its bars against max_crossings=%s, but "
            "the largest count is %d. A bar wider than its track is a readout "
            "that has run off the end of the instrument."
            % (act_id, max_cross, round(biggest * per_kpa)))

    zero_below = float(a.get("net_zero_below") or 20)

    def fmt_kpa(v):
        return a["kpa_format"].replace("{v}", "%.1f" % v)

    def side(mine, theirs):
        """More / less / the same, from the two values and nothing else."""
        if abs(mine - theirs) < 1e-9:
            return sides["same"]
        return sides["more"] if mine > theirs else sides["less"]

    def foot_kpa(st):
        """The two partial pressures, for the footnote line (6.15).

        The figures are correct and worth keeping — they are simply not a
        Year 7 readout. Derived per state from the same pair the tiles are,
        so the footnote cannot disagree with the sides above it.
        """
        return (a["kpa_foot_format"]
                .replace("{alveolar}", fmt_kpa(st["alveolar_kpa"]))
                .replace("{blood}", fmt_kpa(st["blood_kpa"])))

    def fmt_cross(n):
        return a["crossing_format"].replace("{n}", str(int(n)))

    panels = []
    for st in states:
        sid = "%d-%d" % (1 if st["breathing"] else 0,
                         1 if st["blood_flow"] else 0)
        into = round(st["alveolar_kpa"] * per_kpa)
        out_of = round(st["blood_kpa"] * per_kpa)
        net = into - out_of
        panels.append(
            '<p class="ks3-cross-note" data-state="%s" data-alveolar="%s" '
            'data-blood="%s" data-in="%s" data-out="%s" data-net="%s" '
            'data-inw="%s" data-outw="%s" data-kpa="%s"%s>%s</p>'
            % (sid,
               e(side(st["alveolar_kpa"], st["blood_kpa"])),
               e(side(st["blood_kpa"], st["alveolar_kpa"])),
               e(fmt_cross(into)), e(fmt_cross(out_of)),
               e(a["net_zero"] if net <= zero_below else fmt_cross(net)),
               ("%.1f" % (into / max_cross * 100)),
               ("%.1f" % (out_of / max_cross * 100)),
               e(foot_kpa(st)),
               "" if st is states[0] else " hidden",
               rich(st["note"])))

    first = states[0]
    first_in = round(first["alveolar_kpa"] * per_kpa)
    first_out = round(first["blood_kpa"] * per_kpa)
    first_net = first_in - first_out

    switch_html = "".join(
        '<button type="button" class="ks3-cross-switch" data-switch="%s" '
        'aria-pressed="%s" data-on-label="%s" data-off-label="%s">%s</button>'
        % (e(w["id"]),
           "true" if w.get("start", True) else "false",
           e(w["on_label"]), e(w["off_label"]),
           t(w["on_label"] if w.get("start", True) else w["off_label"]))
        for w in switches)

    def tile(key, value, tone=""):
        return ('<div class="ks3-cross-tile"%s>'
                '<p class="ks3-cross-tilelabel">%s</p>'
                '<p class="ks3-cross-tileval" data-tile="%s">%s</p></div>'
                % (tone, t(tiles[key]), key, t(value)))

    def bar(side, name, value, width):
        return ('<li class="ks3-cross-barrow">'
                '<div class="ks3-cross-barhead">'
                '<p class="ks3-cross-barname">%s</p>'
                '<p class="ks3-cross-barval" data-bar="%s">%s</p></div>'
                '<span class="ks3-cross-track">'
                '<span class="ks3-cross-fill" data-fill="%s" '
                'style="width:%s%%"></span></span></li>'
                % (t(name), side, t(value), side, width))

    return ('<div class="ks3-cross" data-cross data-state="%d-%d">'
            '<div class="ks3-cross-switches">%s</div>'
            '<div class="ks3-cross-panel">'
            '<div class="ks3-cross-tiles">%s%s%s</div>'
            '<ul class="ks3-cross-bars" role="list">%s%s</ul>'
            '<p class="ks3-cross-kpa" data-cross-kpa>%s</p>%s</div></div>'
            % (1 if first["breathing"] else 0, 1 if first["blood_flow"] else 0,
               switch_html,
               tile("alveolar", side(first["alveolar_kpa"],
                                    first["blood_kpa"])),
               tile("blood", side(first["blood_kpa"],
                                  first["alveolar_kpa"])),
               tile("net",
                    a["net_zero"] if first_net <= zero_below
                    else fmt_cross(first_net),
                    ' data-tone="net"'),
               bar("in", bars["into"], fmt_cross(first_in),
                   "%.1f" % (first_in / max_cross * 100)),
               bar("out", bars["out_of"], fmt_cross(first_out),
                   "%.1f" % (first_out / max_cross * 100)),
               t(foot_kpa(first)),
               "".join(panels)))
def r_fault_bench(a, act_id):
    """⊕ b4-04 `#s-bench` — the switch-a-part-off idiom, run backwards.

    ⚖️ THE STUDENT LOCATES, THEY DO NOT SWITCH. B2's `system-switch` removes a
    part and reports the symptom; this hands over the symptom and asks which
    part is at fault. Same anatomy of reasoning, opposite direction, and it is
    why this is not `system-switch` with different copy: there is no chain, no
    part to open, and the commitment is a DIAGNOSIS whose truth the block then
    settles.

    ⚖️ THE REVEAL IS NEVER WITHHELD FOR A WRONG ANSWER. The verdict line says
    which of the two happened and the four rows follow either way. A block that
    only explained itself to students who had already guessed right would teach
    nobody, and Design draws exactly one reveal per factor.

    ⚖️ EVERY FACTOR KEEPS ITS OWN PICK AND ITS OWN OPENED FLAG. Three tabs over
    one shared option list, and a student who opens exercise and moves to
    asthma must find asthma uncommitted and exercise exactly as they left it.
    Emit-all-show-one, with the state in the DOM and nowhere else.

    ⚠️ AN ANSWER THAT IS NOT ON THE LIST CANNOT BE LOCATED. Every factor's
    `part` is checked against the offered `parts` at build time; a typo there
    would produce a factor no student could ever get right, and the verdict
    line would read "Not the part you chose" on all four options.
    """
    parts = a.get("parts") or []
    if len(parts) < 2:
        raise ValueError(
            "fault-bench %r declares %d part(s). Locating a fault needs "
            "somewhere else it could have been." % (act_id, len(parts)))
    for p in parts:
        if not (p.get("id") and p.get("text")):
            raise ValueError(
                "fault-bench %r part %r needs `id` and `text`."
                % (act_id, p.get("id")))
    part_ids = [p["id"] for p in parts]

    factors = a.get("factors") or []
    if len(factors) < 2:
        raise ValueError(
            "fault-bench %r declares %d factor(s). The block's argument is "
            "that different factors hit different parts, and one factor cannot "
            "make it." % (act_id, len(factors)))
    for f in factors:
        for key in ("id", "label", "tag", "scenario", "part", "answer"):
            if not f.get(key):
                raise ValueError(
                    "fault-bench %r factor %r is missing %r."
                    % (act_id, f.get("id"), key))
        if f["part"] not in part_ids:
            raise ValueError(
                "fault-bench %r factor %r is at fault in %r, which is not one "
                "of the offered parts %s. Every option would read “not "
                "the part you chose” and the factor would be unanswerable."
                % (act_id, f["id"], f["part"], part_ids))
        rows = f.get("rows") or []
        if not rows:
            raise ValueError(
                "fault-bench %r factor %r declares no rows. The reveal is the "
                "explanation, and a headline with nothing under it is a "
                "verdict without a reason." % (act_id, f["id"]))
        for r in rows:
            if not (r.get("label") and r.get("text")):
                raise ValueError(
                    "fault-bench %r factor %r has a row missing `label` or "
                    "`text`." % (act_id, f["id"]))

    for key in ("question", "open_label"):
        if not a.get(key):
            raise ValueError("fault-bench %r declares no %r." % (act_id, key))
    hints = a.get("hints") or {}
    hmissing = sorted({"none", "ready", "opened"} - set(hints))
    if hmissing:
        raise ValueError(
            "fault-bench %r hints is missing %s. The line beside the button is "
            "the only thing telling a student why it is disabled."
            % (act_id, ", ".join(hmissing)))
    verdicts = a.get("verdicts") or {}
    vmissing = sorted({"right", "wrong"} - set(verdicts))
    if vmissing:
        raise ValueError(
            "fault-bench %r verdicts is missing %s."
            % (act_id, ", ".join(vmissing)))

    first = factors[0]
    for f in factors:
        if f["id"] == a.get("start_factor"):
            first = f
            break

    tabs = "".join(
        '<button type="button" class="ks3-fault-tab" data-factor="%s" '
        'aria-pressed="%s">%s</button>'
        % (e(f["id"]), "true" if f is first else "false", t(f["label"]))
        for f in factors)

    scenarios = "".join(
        '<div class="ks3-fault-scenario" data-factor="%s"%s>'
        '<p class="ks3-fault-tag">%s</p>'
        '<p class="ks3-fault-text">%s</p></div>'
        % (e(f["id"]), "" if f is first else " hidden", t(f["tag"]),
           rich(f["scenario"]))
        for f in factors)

    options = "".join(
        '<li><button type="button" class="ks3-option" data-part="%s" '
        'aria-pressed="false">'
        '<span class="ks3-opt-mark" aria-hidden="true">%s</span>'
        '<span class="ks3-opt-label">%s</span></button></li>'
        % (e(p["id"]), t(option_letter(i)), t(p["text"]))
        for i, p in enumerate(parts))

    reveals = "".join(
        '<div class="ks3-fault-reveal" data-factor="%s" data-answer="%s" hidden>'
        '<p class="ks3-fault-verdict">'
        '<span data-verdict="right" hidden>%s</span>'
        '<span data-verdict="wrong" hidden>%s</span></p>'
        '<p class="ks3-fault-answer">%s</p>'
        '<dl class="ks3-fault-rows">%s</dl></div>'
        % (e(f["id"]), e(f["part"]), t(verdicts["right"]), t(verdicts["wrong"]),
           t(f["answer"]),
           "".join(
               '<div class="ks3-fault-row"><dt>%s</dt><dd>%s</dd></div>'
               % (t(r["label"]), rich(r["text"])) for r in f["rows"]))
        for f in factors)

    return ('<div class="ks3-fault" data-fault data-total="%d" '
            'data-factor="%s" data-hint-none="%s" data-hint-ready="%s" '
            'data-hint-opened="%s">'
            '<div class="ks3-fault-tabs">%s</div>'
            '<div class="ks3-fault-scenarios">%s</div>'
            '<p class="ks3-fault-q">%s</p>'
            '<ul class="ks3-options">%s</ul>'
            '<div class="ks3-fault-foot">'
            '<button type="button" class="ks3-reveal-btn ks3-fault-open" '
            'data-fault-open disabled>%s</button>'
            '<span class="ks3-fault-hint" data-fault-hint role="status">%s'
            '</span></div>'
            '<div class="ks3-fault-reveals">%s</div></div>'
            % (len(factors), e(first["id"]), e(hints["none"]),
               e(hints["ready"]), e(hints["opened"]), tabs, scenarios,
               t(a["question"]), options, t(a["open_label"]),
               t(hints["none"]), reveals))
def r_two_process_ledger(a, act_id):
    """⊕ b4-05 `#s-ledger` — two processes, one net figure, and a flat bar.

    ⚖️ THE RESPIRATION BAR NEVER MOVES, AND THAT IS THE INSTRUMENT. Its width
    is written once, here, from `resp_rate`, and no code path anywhere can
    change it: the wiring never touches that fill. `BREATH-12`/`BREATH-13` are
    the belief that plants respire only at night, and the whole confrontation is
    a student dragging the light from one end to the other and watching the top
    bar refuse to move. A respiration bar computed per frame, even from a
    constant, would be one refactor away from acquiring a light term.

    ⚖️ THE MIDDLE BRANCH IS THE POINT. Net uptake and net release are the two
    readings a student expects; the compensation point is the one that overturns
    something, because it is a flat line produced by two processes at full rate
    rather than by nothing happening. Design's own copy for that branch opens
    "This is the dawn reading from the hook."

    ⚠️ THE BALANCED BRANCH MUST BE REACHABLE, and the renderer proves it rather
    than assuming it. `curve.max` must exceed `resp_rate` or the two never
    cross; some integer light level must land inside `balanced_window` or the
    branch is copy no student can reach. And when the payload NAMES a preset as
    the compensation point (`balanced_preset`), that preset is held to it —
    Design's `dawn = 21` gives a net of +2.33 against its own curve, which is
    firmly net uptake, while the balanced copy claims to be the dawn reading.
    The engine does not choose which side is right. It refuses to let the two
    disagree silently. See `docs/ks3/b4-inventory/PAYLOAD-SCHEMA.md` §5.
    """
    curve = a.get("curve") or {}
    for key in ("max", "constant", "scale"):
        v = curve.get(key)
        if not isinstance(v, (int, float)) or isinstance(v, bool) or v <= 0:
            raise ValueError(
                "two-process-ledger %r curve.%s is %r; it must be a positive "
                "number." % (act_id, key, v))
    resp = a.get("resp_rate")
    if not isinstance(resp, (int, float)) or isinstance(resp, bool) or resp <= 0:
        raise ValueError(
            "two-process-ledger %r resp_rate is %r. It is the flat bar and the "
            "thing the net figure is measured against." % (act_id, resp))
    if float(curve["max"]) <= float(resp):
        raise ValueError(
            "two-process-ledger %r has curve.max=%s and resp_rate=%s. "
            "Photosynthesis could never overtake respiration, so the net "
            "figure would be negative at every light level and the "
            "compensation point would not exist."
            % (act_id, curve["max"], resp))
    if float(curve["scale"]) < max(float(curve["max"]), float(resp)):
        raise ValueError(
            "two-process-ledger %r scales its bars against curve.scale=%s, "
            "which is smaller than curve.max=%s / resp_rate=%s. A bar wider "
            "than its track has run off the end of the instrument."
            % (act_id, curve["scale"], curve["max"], resp))

    window = float(a.get("balanced_window") or 0.25)
    if window <= 0:
        raise ValueError(
            "two-process-ledger %r balanced_window is %r; it is the half-width "
            "of the window and must be positive." % (act_id, window))

    def photo_at(light):
        return float(curve["max"]) * (
            1.0 - math.exp(-float(light) / float(curve["constant"])))

    reachable = [n for n in range(0, 101)
                 if abs(photo_at(n) - float(resp)) < window]
    if not reachable:
        raise ValueError(
            "two-process-ledger %r: no light level between 0 and 100 puts the "
            "net rate inside ±%s, so the balanced verdict is copy no "
            "student can reach. The curve and the respiration rate cross at "
            "light %.1f — either widen the window or move the rate."
            % (act_id, window,
               -float(curve["constant"]) * math.log(1 - float(resp) / float(curve["max"]))))

    presets = a.get("presets") or []
    if not presets:
        raise ValueError(
            "two-process-ledger %r declares no presets." % act_id)
    for p in presets:
        if not (p.get("id") and p.get("label")):
            raise ValueError(
                "two-process-ledger %r preset %r needs `id` and `label`."
                % (act_id, p.get("id")))
        v = p.get("value")
        if not isinstance(v, int) or isinstance(v, bool) or not 0 <= v <= 100:
            raise ValueError(
                "two-process-ledger %r preset %r has value %r; it is a light "
                "level 0–100." % (act_id, p["id"], v))
    preset_ids = [p["id"] for p in presets]

    named = a.get("balanced_preset")
    if named:
        if named not in preset_ids:
            raise ValueError(
                "two-process-ledger %r names %r as the compensation point and "
                "there is no such preset. The presets are %s."
                % (act_id, named, preset_ids))
        chosen = [p for p in presets if p["id"] == named][0]
        net_there = photo_at(chosen["value"]) - float(resp)
        if abs(net_there) >= window:
            raise ValueError(
                "two-process-ledger %r names preset %r (light %d) as the "
                "compensation point, but the net rate there is %+.2f, outside "
                "±%s. Pressing it reads as net %s, not as balance. The "
                "window reaches light %d–%d; move the preset rather than "
                "widening the window, which at ±%.2f would call every "
                "reading balanced."
                % (act_id, named, chosen["value"], net_there, window,
                   "uptake" if net_there > 0 else "release",
                   reachable[0], reachable[-1], abs(net_there)))

    start = int(a.get("start_light") or 0)
    if not 0 <= start <= 100:
        raise ValueError(
            "two-process-ledger %r start_light is %d; the slider runs "
            "0–100." % (act_id, start))

    for key in ("light_label", "light_aria", "dark_label", "light_format",
                "rate_format"):
        if not a.get(key):
            raise ValueError(
                "two-process-ledger %r declares no %r." % (act_id, key))
    resp_spec = a.get("respiration") or {}
    if not (resp_spec.get("name") and resp_spec.get("note")):
        raise ValueError(
            "two-process-ledger %r respiration needs `name` and `note`. The "
            "note is the sentence that tells a student to watch the bar NOT "
            "move, which is the only instruction the flat bar gets." % act_id)
    photo_spec = a.get("photosynthesis") or {}
    pmissing = sorted({"name", "note_dark", "note_light"} - set(photo_spec))
    if pmissing:
        raise ValueError(
            "two-process-ledger %r photosynthesis is missing %s. Darkness gets "
            "its own note because zero is the reading the misconception lives "
            "on." % (act_id, ", ".join(pmissing)))
    net_spec = a.get("net") or {}
    nmissing = sorted({"name", "in_format", "out_format", "note"} - set(net_spec))
    if nmissing:
        raise ValueError(
            "two-process-ledger %r net is missing %s. The two formats carry "
            "the DIRECTION in words — the bar's magnitude cannot, because "
            "it is drawn from an absolute value."
            % (act_id, ", ".join(nmissing)))
    verdicts = a.get("verdicts") or {}
    for branch in ("balanced", "uptake", "release"):
        spec = verdicts.get(branch) or {}
        for key in ("tag", "head", "why"):
            if not spec.get(key):
                raise ValueError(
                    "two-process-ledger %r verdicts.%s is missing %r. All "
                    "three branches are reachable from the slider."
                    % (act_id, branch, key))

    scale = float(curve["scale"])
    photo0 = photo_at(start)
    net0 = photo0 - float(resp)
    branch0 = ("balanced" if abs(net0) < window
               else ("uptake" if net0 > 0 else "release"))

    def rate(v):
        return a["rate_format"].replace("{v}", "%.1f" % v)

    def net_label(v):
        fmt = net_spec["in_format"] if v >= 0 else net_spec["out_format"]
        return fmt.replace("{v}", "%.1f" % abs(v))

    preset_html = "".join(
        '<button type="button" class="ks3-tpl-preset" data-preset="%d" '
        'aria-pressed="%s">%s</button>'
        % (p["value"], "true" if p["value"] == start else "false",
           t(p["label"]))
        for p in presets)

    verdict_html = "".join(
        '<div class="ks3-tpl-verdict" data-verdict="%s"%s>'
        '<p class="ks3-tpl-vtag">%s</p>'
        '<p class="ks3-tpl-vhead">%s</p>'
        '<p class="ks3-tpl-vwhy">%s</p></div>'
        % (branch, "" if branch == branch0 else " hidden",
           t(verdicts[branch]["tag"]), t(verdicts[branch]["head"]),
           rich(verdicts[branch]["why"]))
        for branch in ("balanced", "uptake", "release"))

    sid = "tpl-" + str(act_id)

    return ('<div class="ks3-tpl" data-tpl data-resp="%s" data-max="%s" '
            'data-const="%s" data-scale="%s" data-window="%s" '
            'data-rate-format="%s" data-in-format="%s" data-out-format="%s">'
            '<div class="ks3-tpl-control">'
            '<div class="ks3-tpl-controlhead">'
            '<p class="ks3-tpl-cap">%s</p>'
            '<p class="ks3-tpl-light" data-light data-dark="%s" '
            'data-format="%s" data-format-one="%s">%s</p></div>'
            '<label class="ks3-sr-only" for="%s">%s</label>'
            '<input class="ks3-b4slider ks3-tpl-slider" type="range" id="%s" '
            'min="0" max="100" step="1" value="%d" data-tpl-slider>'
            '<div class="ks3-tpl-presets">%s</div></div>'
            '<div class="ks3-tpl-panel">'
            '<ul class="ks3-tpl-flows" role="list">'
            '<li class="ks3-tpl-flow" data-flow="resp">'
            '<div class="ks3-tpl-flowhead"><p class="ks3-tpl-flowname">%s</p>'
            '<p class="ks3-tpl-flowval">%s</p></div>'
            '<span class="ks3-tpl-track">'
            '<span class="ks3-tpl-fill" data-fill="resp" style="width:%s%%">'
            '</span></span>'
            '<p class="ks3-tpl-flownote">%s</p></li>'
            '<li class="ks3-tpl-flow" data-flow="photo">'
            '<div class="ks3-tpl-flowhead"><p class="ks3-tpl-flowname">%s</p>'
            '<p class="ks3-tpl-flowval" data-val="photo">%s</p></div>'
            '<span class="ks3-tpl-track">'
            '<span class="ks3-tpl-fill" data-fill="photo" style="width:%s%%">'
            '</span></span>'
            '<p class="ks3-tpl-flownote" data-note="dark"%s>%s</p>'
            '<p class="ks3-tpl-flownote" data-note="light"%s>%s</p></li>'
            '<li class="ks3-tpl-flow" data-flow="net">'
            '<div class="ks3-tpl-flowhead"><p class="ks3-tpl-flowname">%s</p>'
            '<p class="ks3-tpl-flowval" data-val="net">%s</p></div>'
            '<span class="ks3-tpl-track">'
            '<span class="ks3-tpl-fill" data-fill="net" data-tone="%s" '
            'style="width:%s%%"></span></span>'
            '<p class="ks3-tpl-flownote">%s</p></li></ul>'
            '<div class="ks3-tpl-verdicts">%s</div></div></div>'
            % (resp, curve["max"], curve["constant"], curve["scale"], window,
               e(a["rate_format"]), e(net_spec["in_format"]),
               e(net_spec["out_format"]),
               t(a["light_label"]), e(a["dark_label"]), e(a["light_format"]),
               # MRB-257 (5.44) — "1 units" at the bottom of the slider's
               # travel, one step above "dark". Falls back to the plural.
               e(a.get("light_format_one") or a["light_format"]),
               t(a["dark_label"] if start == 0
                 else (a.get("light_format_one") if start == 1
                       and a.get("light_format_one") else a["light_format"])
                 .replace("{n}", str(start))),
               e(sid), t(a["light_aria"]), e(sid), start, preset_html,
               t(resp_spec["name"]), t(rate(float(resp))),
               ("%.1f" % (float(resp) / scale * 100)),
               rich(resp_spec["note"]),
               t(photo_spec["name"]), t(rate(photo0)),
               ("%.1f" % (photo0 / scale * 100)),
               "" if start == 0 else " hidden", rich(photo_spec["note_dark"]),
               " hidden" if start == 0 else "", rich(photo_spec["note_light"]),
               t(net_spec["name"]), t(net_label(net0)), branch0,
               ("%.1f" % (abs(net0) / scale * 100)), rich(net_spec["note"]),
               verdict_html))


# ── registrations ────────────────────────────────────────────────────────
ART = {
    'guard-cells': _guard_cells,
    'thorax': _thorax,
}

KIND_SHELL = {
    'gas-compare': ("ks3-gas-block", ' data-instrument data-gasblock data-stage-done="0"'),
    'bell-jar': ("ks3-bell-block", ' data-instrument data-bellblock data-stage-done="0"'),
    'crossing-counter': ("ks3-cross-block", ' data-instrument data-crossblock data-stage-done="0"'),
    'fault-bench': ("ks3-fault-block", ' data-instrument data-faultblock data-stage-done="0"'),
    'two-process-ledger': ("ks3-tpl-block", ' data-instrument data-tplblock data-stage-done="0"'),
}

KIND_FN = {
    'gas-compare': r_gas_compare,
    'bell-jar': r_bell_jar,
    'crossing-counter': r_crossing_counter,
    'fault-bench': r_fault_bench,
    'two-process-ledger': r_two_process_ledger,
}
