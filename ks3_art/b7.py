"""ks3_art.b7 — B7's drawers, instruments and registrations.

ONE UNIT, ONE FILE. Nothing here is read by any other unit; nothing
here may be added to any other unit's module. Moved verbatim out of
``build_ks3.py`` by MRB-271 so that two content lanes can build two
units at once without editing the same file.
"""

import json
import re
from ks3_art.kit import (
    _SVG_BAND,
    _SVG_CARD,
    _SVG_GROUND,
    _SVG_INK,
    _SVG_INK_BODY,
    _b7_dial_block,
    _b7_dials,
    _b7_need,
    _b7_suffix,
    _b7_verdict_ids,
    _circle,
    _ellipse,
    _label,
    _line,
    _mono,
    _path,
    _pctnum,
    _rect,
    _svg_open,
    e,
    rich,
    t,
)


# ── ⊕ MRB-254 · WS1 #3 · a leaf, sliced through ─────────────────────────
#
# The literals Design's `renderVals()` generates the slice's interior from.
# Everything inside the section is derived here rather than placed, which is
# what gives a content-truth row something to bite on: the palisade count, the
# chloroplast count per cell, and the one gap in the underside are all
# properties of these tuples, not of a caption that says so.
#
# ⚠️ THE LAYER ORDER IS THE FIGURE'S WHOLE CLAIM, so it lives in one dict and
# every band, every cell and every label reads its rank out of it. Rung 1 of
# this lesson asks WHY palisade cells are at the top; the rule block gives each
# feature an explicit position. A defect that swapped palisade and spongy
# mesophyll would still look exactly like a leaf, and would teach the answer to
# rung 1 backwards. Nothing in the drawing may know its own rank independently.
_B7_LEAF_ORDER = {
    "upper-cuticle":    1,
    "upper-epidermis":  2,
    "palisade":         3,
    "spongy-mesophyll": 4,
    "lower-epidermis":  5,
    "lower-cuticle":    6,
}
# Ten palisade cells across the 420-unit slice, and the four rows of
# chloroplasts inside each. The COUNT is the fact — most of a leaf's
# chloroplasts are in this layer — so Design places them rather than
# suggesting them, and so does this.
_B7_LEAF_PAL_X = (152, 194, 236, 278, 320, 362, 404, 446, 488, 530)
_B7_LEAF_CHL_ROWS = (166, 186, 206, 226)
# The spongy mesophyll: cx, cy, rx, ry. Nine cells, hand-placed by Design at
# two staggered depths so the air between them reads as space rather than as
# grout.
_B7_LEAF_SPONGY = (
    (180, 270, 27, 20), (176, 322, 25, 18),
    (238, 264, 24, 18), (246, 318, 27, 20),
    (400, 268, 24, 18), (398, 322, 22, 17),
    (470, 266, 26, 19), (474, 320, 24, 18),
    (536, 290, 26, 20),
)
# Eight of those nine cells keep ONE chloroplast, offset (+6, +2) off centre.
# Eight against eighty is the comparison the caption asks a student to make.
_B7_LEAF_SPONGY_CHL = (
    (180, 270), (238, 264), (400, 268), (470, 266),
    (176, 322), (246, 318), (474, 320), (536, 290),
)
# Upper epidermis: seven whole cells. Lower epidermis: six, and the sixth run
# starts at 488 because the pore has eaten what would have been between them.
_B7_LEAF_UPPER_EPI = (152, 212, 272, 332, 392, 452, 512)
_B7_LEAF_LOWER_EPI = ((152, 56), (212, 56), (272, 56), (332, 48),
                      (488, 38), (530, 38))
# THE PORE IS THE SINGLE SOURCE OF TRUTH FOR THE UNDERSIDE. It is the 30
# units between x 420 and x 450, and it is an absence rather than a shape: the
# two runs of lower cuticle and the two guard cells are all derived from it, so
# a defect that moved the pore moves everything that defines it rather than
# leaving a hole and a lid in different places. Design's literals — cuticle
# runs at 150 wide 270 and 450 wide 120, guard cells at 400 and 470 radius 20 —
# come back out of these three numbers exactly.
_B7_LEAF_PORE = (420, 450)
_B7_LEAF_GUARD_R = 20
_B7_LEAF_SECTION_X = (150, 570)
# The number the dimension line prints, held once so the label and the mark
# cannot drift apart. `data-scale-mm` on both is the same value read twice.
_B7_LEAF_MM = "0.5"
def _leaf_section(fig):
    """A leaf in cross-section — cuticle, epidermis, palisade, spongy
    mesophyll, vein, stoma — with carbon dioxide in through the pore and water
    up the vein, over a slice marked less than half a millimetre thick.

    ⚖️ WHY THIS LESSON NEEDS IT AT ALL. `leaves-built-for-the-job` is anatomy
    end to end: its rule block hands every feature an explicit POSITION
    ("Palisade cells · Top layer", "Stomata · Underside") and rung 1 asks why
    the palisade cells are the ones at the top. The bench turns four dials into
    two percentages and a habitat verdict — it never draws the leaf. And no
    leaf cross-section exists anywhere else on the site, so this plate is the
    only place a student ever sees the thing the whole lesson describes. A
    position stated in a table and never drawn is a position that gets
    memorised in whatever order it was read.

    ⛔ THE ORDER OF THE LAYERS IS THE ENCODING, and it is the one defect that
    would be invisible. Swap palisade and spongy mesophyll and the drawing is
    still recognisably a leaf, still labelled, still pretty — and it now
    teaches rung 1's answer backwards. So every band, every cell inside it and
    every label naming it carries `data-layer` AND `data-order`, read out of
    `_B7_LEAF_ORDER`, and a row walks all six by drawn y rather than checking
    that one label exists somewhere. The labels are safe to carry the hooks
    because their own baselines run in the same order as the bands they name;
    a row taking min-y or mean-y per rank gets a monotonic sequence either way.

    ⚖️ THE SURFACE HOOK IS SPELLED ON THE CUTICLE AND THE EPIDERMIS ONLY.
    `data-surface="upper"/"lower"` goes on exactly the layers that HAVE a
    surface, so "everything marked lower is in the bottom of the slice" stays
    an assertion with content. Palisade and spongy mesophyll get no
    `data-surface` at all — a mesophyll cell answering to "upper" would make
    the stoma claim unmeasurable by flooding it.

    ⚠️ THE PORE IS AN ABSENCE, SO THE HOOK RIDES WHAT DEFINES IT. Design draws
    no stoma shape — and she is right not to: a hole painted on as a dark
    lozenge is a hole a later edit can move without breaking anything. What she
    draws is a lower cuticle in TWO runs with 30 units of nothing between them,
    and two guard cells either side of that nothing. So `data-stoma="1"` sits
    on the two guard cells, `data-run` + `data-run-index` on the cuticle runs
    (one run on top, two underneath), and a row asserts the stoma is in the
    LOWER surface from the guard cells' own `data-surface`, and that the gap
    between run 1 and run 2 is where the carbon-dioxide route crosses. Guard
    cells carrying `data-layer="lower-epidermis"` is not a convenience: guard
    cells ARE modified epidermal cells, and the rank is true.

    ⊕ BOTH ROUTES ARE WALKED SEGMENT BY SEGMENT, not asserted at their start.
    `data-route` + `data-step` is on every piece of both arrows, so a row
    checks continuity as well as endpoints: carbon dioxide from outside the
    leaf (step 1) through the pore (step 2) up an air space into a palisade
    cell (step 3), and water in along the vein (step 1) then upward inside it
    (step 2). Design drew the carbon-dioxide run as ONE straight path; it is
    subdivided here at the two boundaries it actually crosses — the underside
    of the leaf and the top of the guard cells. Three collinear segments of the
    same weight and the same round cap render as the line she drew, to the
    pixel, and the last one still stops at 250 so her arrowhead is the only
    thing at the tip. A route hooked only at its first segment is a route a row
    can only check the beginning of, which is the assertion that measures the
    frame again.

    ⚠️ ONE THING IS DRAWN IN A DIFFERENT ORDER FROM DESIGN'S DELIVERY, and it
    is a defect fix, not a preference. Her SVG paints the chloroplast loop —
    which carries the palisade's eighty AND the spongy layer's eight — BEFORE
    the spongy cell bodies, and those bodies are opaque `--ks3-card`. All eight
    spongy chloroplasts are therefore painted over and none of them renders. Her
    own source comment beside them reads "the spongy layer keeps a few, and
    visibly fewer", and her figcaption asks the student to count the palisade's
    against the spongy cells below — so the delivery contradicts both. The
    spongy bodies are painted first here and every chloroplast after them.
    Nothing else moves: no palisade chloroplast reaches y 244, no chloroplast
    at all falls inside the vein, so the rest of the plate is byte-for-byte the
    same drawing. The `<desc>` is amended to match, because it now walks a
    drawing with eight visible chloroplasts in it that hers did not.

    ⊕ THE THICKNESS PRINTS ITS OWN MARK. `_B7_LEAF_MM` is formatted into the
    label and emitted as `data-scale-mm` on both the dimension path and the
    text, so the number a student reads and the number a row measures against
    are one string. Two literals would drift the first time either is edited.
    """
    W, H = 860, 500
    out = [_svg_open(fig, W, H)]
    out.append('<g stroke-linecap="round" stroke-linejoin="round">')

    out.append(_mono(24, 44, "A SLICE THROUGH THE LEAF · TOP OF THE LEAF AT "
                             "THE TOP", size=14, weight="400", spacing="1.4"))

    # The slice's own ground, then the clip. Nothing currently overruns the
    # section — Design's clip is belt and braces against a future edit that
    # widens a cell — so it is kept, and kept keyed to the figure id so two
    # figures on one page cannot collide on it.
    out.append(_rect(150, 90, 420, 306, fill=_SVG_GROUND, data_section="1"))
    clip = "%s-sec" % e(fig["id"])
    out.append('<defs><clipPath id="%s">%s</clipPath></defs>'
               % (clip, _rect(150, 90, 420, 306)))
    out.append('<g clip-path="url(#%s)">' % clip)

    # ── 1 · the upper cuticle: ONE run, and unbroken is the point ────────
    out.append(_rect(150, 90, 420, 10, fill=_SVG_BAND, stroke=_SVG_INK, w=2,
                     data_layer="upper-cuticle",
                     data_order=_B7_LEAF_ORDER["upper-cuticle"],
                     data_surface="upper", data_run="1", data_run_index="1"))

    # ── 2 · upper epidermis ─────────────────────────────────────────────
    for x in _B7_LEAF_UPPER_EPI:
        out.append(_rect(x, 102, 56, 38, rx=8, fill=_SVG_CARD,
                         stroke=_SVG_INK, w=2,
                         data_layer="upper-epidermis",
                         data_order=_B7_LEAF_ORDER["upper-epidermis"],
                         data_surface="upper", data_cell="epidermis"))

    # ── 3 · palisade: ten tall cells, standing on end, first in the light ─
    for i, x in enumerate(_B7_LEAF_PAL_X):
        out.append(_rect(x, 146, 38, 96, rx=10, fill=_SVG_CARD,
                         stroke=_SVG_INK, w=2, data_layer="palisade",
                         data_order=_B7_LEAF_ORDER["palisade"],
                         data_cell="palisade", data_cell_index=i + 1))

    # ── 4 · spongy mesophyll, painted BEFORE the chloroplasts ───────────
    for cx, cy, rx, ry in _B7_LEAF_SPONGY:
        out.append(_ellipse(cx, cy, rx, ry, fill=_SVG_CARD, stroke=_SVG_INK,
                            w=2, data_layer="spongy-mesophyll",
                            data_order=_B7_LEAF_ORDER["spongy-mesophyll"],
                            data_cell="spongy"))

    # The chloroplasts, Design's generator ported exactly. Eight per palisade
    # cell — two per row, four rows — jittered by an integer modulus rather
    # than by anything random, so the build is byte-identical run to run. Each
    # one answers to the layer it sits in, which is what lets a row COUNT
    # eighty against eight instead of trusting the caption that says so.
    for i, x in enumerate(_B7_LEAF_PAL_X):
        for r, y in enumerate(_B7_LEAF_CHL_ROWS):
            out.append(_ellipse(x + 11, y + ((i * 7 + r * 3) % 5) - 2, 6, 4,
                                fill=_SVG_BAND, stroke=_SVG_INK, w=1.5,
                                data_chloroplast="1", data_layer="palisade",
                                data_order=_B7_LEAF_ORDER["palisade"],
                                data_cell_index=i + 1))
            out.append(_ellipse(x + 27, y + ((i * 5 + r * 11) % 5) + 6, 6, 4,
                                fill=_SVG_BAND, stroke=_SVG_INK, w=1.5,
                                data_chloroplast="1", data_layer="palisade",
                                data_order=_B7_LEAF_ORDER["palisade"],
                                data_cell_index=i + 1))
    for cx, cy in _B7_LEAF_SPONGY_CHL:
        out.append(_ellipse(cx + 6, cy + 2, 6, 4, fill=_SVG_BAND,
                            stroke=_SVG_INK, w=1.5, data_chloroplast="1",
                            data_layer="spongy-mesophyll",
                            data_order=_B7_LEAF_ORDER["spongy-mesophyll"]))

    # ── the vein, embedded among the spongy cells ───────────────────────
    # No `data-layer`: a vein is not a mesophyll cell, and if it answered to
    # the spongy rank then "every spongy-mesophyll element is a rounded cell
    # with air around it" would stop being checkable.
    out.append(_ellipse(340, 294, 44, 32, fill=_SVG_CARD, stroke=_SVG_INK,
                        w=2.5, data_vein="1"))
    out.append(_label(340, 284, "vein", size=16, weight="700",
                      data_vein="1"))
    out.append(_line(340, 322, 340, 306, stroke=_SVG_INK, w=3,
                     data_route="water", data_step="2", data_in="vein"))
    out.append(_path("M 333,306 L 347,306 L 340,294 Z", fill=_SVG_INK,
                     data_route="water", data_step="2", data_in="vein"))

    # ── 5 · lower epidermis, interrupted once ───────────────────────────
    for x, wid in _B7_LEAF_LOWER_EPI:
        out.append(_rect(x, 346, wid, 38, rx=8, fill=_SVG_CARD,
                         stroke=_SVG_INK, w=2,
                         data_layer="lower-epidermis",
                         data_order=_B7_LEAF_ORDER["lower-epidermis"],
                         data_surface="lower", data_cell="epidermis"))

    # The two guard cells. They are the stoma's hook because they are what the
    # drawing actually contains: the pore itself is the 30 units of nothing
    # between them, at x 420 to 450.
    for cx in (_B7_LEAF_PORE[0] - _B7_LEAF_GUARD_R,
               _B7_LEAF_PORE[1] + _B7_LEAF_GUARD_R):
        out.append(_circle(cx, 362, _B7_LEAF_GUARD_R, fill=_SVG_BAND,
                           stroke=_SVG_INK,
                           w=2.5, data_layer="lower-epidermis",
                           data_order=_B7_LEAF_ORDER["lower-epidermis"],
                           data_surface="lower", data_guard="1",
                           data_stoma="1"))

    # ── 6 · lower cuticle: TWO runs, and the gap between them is the pore ─
    for i, (x0, x1) in enumerate(((_B7_LEAF_SECTION_X[0], _B7_LEAF_PORE[0]),
                                  (_B7_LEAF_PORE[1], _B7_LEAF_SECTION_X[1]))):
        out.append(_rect(x0, 386, x1 - x0, 10, fill=_SVG_BAND, stroke=_SVG_INK,
                         w=2, data_layer="lower-cuticle",
                         data_order=_B7_LEAF_ORDER["lower-cuticle"],
                         data_surface="lower", data_run="1",
                         data_run_index=i + 1))
    out.append('</g>')

    out.append(_rect(150, 90, 420, 306, stroke=_SVG_INK, w=2.5,
                     data_section="1"))

    # ── carbon dioxide: outside, through the pore, up an air space, in ──
    # One straight run of Design's, cut at the two boundaries it crosses. The
    # x is 434, which is inside the pore (420–450) and inside the seventh
    # palisade cell (404–442): the route is aimed, not decorative.
    out.append(_line(434, 444, 434, 396, stroke=_SVG_INK, w=3,
                     data_route="co2", data_step="1", data_start="outside"))
    out.append(_line(434, 396, 434, 342, stroke=_SVG_INK, w=3,
                     data_route="co2", data_step="2", data_through="stoma"))
    out.append(_line(434, 342, 434, 250, stroke=_SVG_INK, w=3,
                     data_route="co2", data_step="3", data_end="palisade"))
    out.append(_path("M 427,252 L 441,252 L 434,238 Z", fill=_SVG_INK,
                     data_route="co2", data_step="3", data_end="palisade"))

    # ── water, in along the vein ────────────────────────────────────────
    out.append(_line(132, 294, 292, 294, stroke=_SVG_INK, w=3,
                     data_route="water", data_step="1", data_end="vein"))
    out.append(_path("M 292,287 L 292,301 L 304,294 Z", fill=_SVG_INK,
                     data_route="water", data_step="1", data_end="vein"))
    out.append(_label(24, 258, "water arrives", size=16, weight="700",
                      anchor="start", data_route="water"))
    out.append(_label(24, 280, "along the vein", size=16, weight="700",
                      anchor="start", data_route="water"))

    # ── how thick the whole thing is ────────────────────────────────────
    out.append(_path("M 584,90 V 396 M 576,90 H 592 M 576,396 H 592",
                     stroke=_SVG_INK, w=2, data_scale_mm=_B7_LEAF_MM))
    out.append(_mono(584, 78, "less than %s mm thick" % _B7_LEAF_MM, size=16,
                     fill=_SVG_INK, weight="400", anchor="middle",
                     data_scale_mm=_B7_LEAF_MM))

    # ── the labels, each one carrying the rank of the band it names ─────
    out.append(_label(600, 100, "cuticle — waxy, keeps water in", size=16,
                      weight="400", anchor="start",
                      data_layer="upper-cuticle",
                      data_order=_B7_LEAF_ORDER["upper-cuticle"],
                      data_surface="upper"))
    out.append(_path("M 596,96 L 574,95", stroke=_SVG_INK, w=1.4))
    out.append(_label(600, 132, "upper epidermis", size=16, weight="400",
                      anchor="start", data_layer="upper-epidermis",
                      data_order=_B7_LEAF_ORDER["upper-epidermis"],
                      data_surface="upper"))
    out.append(_path("M 596,128 L 574,121", stroke=_SVG_INK, w=1.4))

    out.append(_label(600, 182, "palisade cells — the top layer", size=16,
                      weight="700", anchor="start", data_layer="palisade",
                      data_order=_B7_LEAF_ORDER["palisade"]))
    out.append(_label(600, 204, "packed with chloroplasts, and", size=16,
                      fill=_SVG_INK_BODY, weight="400", anchor="start",
                      data_layer="palisade",
                      data_order=_B7_LEAF_ORDER["palisade"]))
    out.append(_label(600, 226, "first in the way of the light", size=16,
                      fill=_SVG_INK_BODY, weight="400", anchor="start",
                      data_layer="palisade",
                      data_order=_B7_LEAF_ORDER["palisade"]))
    out.append(_path("M 596,190 L 574,190", stroke=_SVG_INK, w=1.4))

    out.append(_label(600, 288, "spongy mesophyll", size=16, weight="400",
                      anchor="start", data_layer="spongy-mesophyll",
                      data_order=_B7_LEAF_ORDER["spongy-mesophyll"]))
    out.append(_path("M 596,284 L 574,286", stroke=_SVG_INK, w=1.4))
    out.append(_label(600, 320, "air spaces between the cells", size=16,
                      fill=_SVG_INK_BODY, weight="400", anchor="start",
                      data_layer="spongy-mesophyll",
                      data_order=_B7_LEAF_ORDER["spongy-mesophyll"]))
    out.append(_path("M 596,316 L 574,322", stroke=_SVG_INK, w=1.4))

    out.append(_label(600, 368, "lower epidermis", size=16, weight="400",
                      anchor="start", data_layer="lower-epidermis",
                      data_order=_B7_LEAF_ORDER["lower-epidermis"],
                      data_surface="lower"))
    out.append(_path("M 596,364 L 574,365", stroke=_SVG_INK, w=1.4))

    out.append(_label(150, 430, "the stoma and its two guard cells", size=16,
                      weight="700", anchor="start", data_stoma="1",
                      data_surface="lower"))
    out.append(_label(150, 452, "— on the underside, and nowhere on top",
                      size=16, weight="700", anchor="start", data_stoma="1",
                      data_surface="lower"))
    out.append(_path("M 400,424 L 414,400", stroke=_SVG_INK, w=1.4))

    out.append(_label(452, 470, "carbon dioxide, in through the stoma",
                      size=16, weight="400", anchor="start",
                      data_route="co2"))
    out.append(_path("M 448,466 L 436,450", stroke=_SVG_INK, w=1.4))

    out.append('</g>')
    out.append('</svg>')
    return "".join(out)
# ── b7-01 `#s-bench` · reactant-remover ──────────────────────────────────

def r_reactant_remover(a, act_id):
    """⊕ b7-01 `#s-bench` — four things it needs, and rate is their PRODUCT.

    ⚖️ THE MODEL IS A PRODUCT, NOT A SUM, and that is the whole bench: remove
    any one of the four and the rate is zero, because the four are not weighted
    contributors but jointly necessary. A sum would let a student switch the
    light off and still make three-quarters of the starch, which is the belief
    the lesson exists to kill.

    ⚖️ SEVEN BRANCHES, NOT SIX. The schema declares one per dial plus
    `multiple` and `none`; the page has a seventh, because "nothing removed"
    splits in two. Dim light is a REDUCTION rather than a removal and has its
    own verdict — "the plant is limited, not stopped" — and it is the only
    place on the page a student meets a rate between zero and full. Design's
    own threshold is `ratePct < 50`, kept here character for character rather
    than rewritten as "rate < 1": the two agree on the authored dial values and
    only one of them is what the approved page does.

    ⚠️ PRECEDENCE IS NOT LOAD-BEARING HERE, and it is on b7-03. Every
    single-dial branch is guarded by `missing.length === 1` on Design's page, so
    at most one can ever match. The sibling instrument's ordering IS
    load-bearing, and the two must not be maintained as though they were the
    same problem — which is why this says so rather than leaving the reader to
    infer it from an absence.

    ⚠️ THE BENCH OPENS INTACT — the first option of every dial, which is
    Design's own `DEFAULTS` and what `chosen()` falls back to. This is the
    OPPOSITE of b7-02's tuner, which opens on a deliberately bad leaf: here the
    student's move is to take something away, so the opening state has to be
    whole. Asserted rather than assumed, because an opening state that is
    already broken puts the bench in a verdict before the student has touched
    it.
    """
    dials = _b7_dials(a, act_id, ("f",))
    _b7_need(a, act_id, ("test_label", "tested_label", "reset_label",
                         "setup", "rate", "readouts"))

    start = {d["id"]: d["options"][0]["id"] for d in dials}
    intact = 1.0
    for d in dials:
        intact *= float(d["options"][0]["f"])
    if intact != 1.0:
        raise ValueError(
            "reactant-remover %r opens at %g of its maximum rate. The first "
            "option of every dial is the opening state and the bench opens "
            "INTACT — a bench already in a verdict has answered its own "
            "question." % (act_id, intact))

    for d in dials:
        if not any(float(o["f"]) == 0 for o in d["options"]):
            raise ValueError(
                "reactant-remover %r dial %r offers no setting with f = 0, so "
                "its own verdict can never be reached. Every dial on this "
                "bench is a thing that can be taken away."
                % (act_id, d["id"]))
    if not any(0 < float(o["f"]) < 1
               for d in dials for o in d["options"]):
        raise ValueError(
            "reactant-remover %r offers no partial setting, so the `low` "
            "verdict — the only non-binary reading on the page — can never be "
            "reached." % act_id)

    verdicts = _b7_verdict_ids(
        a, act_id, [d["id"] for d in dials] + ["multiple", "low", "none"],
        "One branch per dial, plus `multiple` (more than one thing removed), "
        "`low` (nothing removed and the light dim) and `none`.")
    for key, v in sorted(verdicts.items()):
        for f in ("tag", "head", "why"):
            if not v.get(f):
                raise ValueError(
                    "reactant-remover %r verdict %r declares no %r."
                    % (act_id, key, f))

    setup = a["setup"]
    for f in ("all_present", "missing_prefix"):
        if not setup.get(f):
            raise ValueError(
                "reactant-remover %r setup declares no %r. The line names what "
                "the jar is holding, and both states of it are on screen."
                % (act_id, f))
    rate = a["rate"]
    for f in ("label", "suffix"):
        if not rate.get(f):
            raise ValueError("reactant-remover %r rate declares no %r."
                             % (act_id, f))

    readouts = a["readouts"]
    if len(readouts) < 2:
        raise ValueError(
            "reactant-remover %r draws %d readout(s). The block's own prompt "
            "promises three." % (act_id, len(readouts)))
    tones, rows = [], []
    for r in readouts:
        for f in ("id", "label", "suffix", "zero", "tone"):
            if not r.get(f):
                raise ValueError(
                    "reactant-remover %r readout %r declares no %r. `zero` is "
                    "NOT uniform across the three — two read \"none\" and the "
                    "bubbles read \"0 per minute\" — and `tone` is the only "
                    "thing telling three identical bars apart."
                    % (act_id, r.get("id"), f))
        if "scale" not in r:
            raise ValueError(
                "reactant-remover %r readout %r declares no `scale`. Without "
                "it the oxygen counter reads 100 bubbles a minute at full rate "
                "instead of 40." % (act_id, r["id"]))
        if r["tone"] in tones:
            raise ValueError(
                "reactant-remover %r gives tone %r to two readouts. Design "
                "paints each bar its own colour and the distinction is the "
                "only thing separating three bars of identical width."
                % (act_id, r["tone"]))
        tones.append(r["tone"])
        # The opening render is the INTACT bench, so every readout is at full
        # scale and none of them is at its `zero` string.
        rows.append(
            '<li class="ks3-rr-readout" data-tone="%s">'
            '<div class="ks3-rr-readrow">'
            '<p class="ks3-rr-rolabel">%s</p>'
            '<p class="ks3-rr-rovalue" data-rr-readout data-scale="%s" '
            'data-suffix="%s" data-zero="%s">%s</p></div>'
            '<span class="ks3-rr-track"><span class="ks3-rr-fill" '
            'data-rr-bar style="width:100%%"></span></span></li>'
            % (e(r["tone"]), t(r["label"]), e(_pctnum(r["scale"])),
               e(r["suffix"]), e(r["zero"]),
               t(_b7_suffix(int(round(float(r["scale"]))), r["suffix"]))))

    panels = "".join(
        '<div class="ks3-rr-verdict" data-rr-verdict="%s" hidden>'
        '<p class="ks3-rr-tag">%s</p>'
        '<p class="ks3-rr-head">%s</p>'
        '<p class="ks3-rr-why">%s</p></div>'
        % (e(key), t(verdicts[key]["tag"]), t(verdicts[key]["head"]),
           rich(verdicts[key]["why"]))
        for key in sorted(verdicts))

    return ('<div class="ks3-rr" data-rr data-all-present="%s" '
            'data-missing-prefix="%s" data-rate-suffix="%s" '
            'data-test-label="%s" data-tested-label="%s">%s'
            '<div class="ks3-rr-panel">'
            '<div class="ks3-rr-setuprow">'
            '<p class="ks3-rr-setup" data-rr-setup>%s</p>'
            '<p class="ks3-rr-rate"><span class="ks3-rr-ratelabel">%s</span> '
            '<span data-rr-rate>%s</span></p></div>'
            '<ul class="ks3-rr-readouts" role="list">%s</ul>'
            '<div class="ks3-rr-foot">'
            '<button type="button" class="ks3-reveal-btn ks3-rr-test" '
            'data-rr-test>%s</button>'
            '<button type="button" class="ks3-reveal-btn ks3-rr-reset" '
            'data-rr-reset>%s</button></div>%s</div></div>'
            % (e(setup["all_present"]), e(setup["missing_prefix"]),
               e(rate["suffix"]), e(a["test_label"]), e(a["tested_label"]),
               # MRB-257 (5.32) — `data-missing` names WHAT IS ABSENT when
               # the option says something different from its dial. Three
               # dials name the thing they remove; the fourth is "The leaf
               # tested" and its zero option is "White part of a variegated
               # leaf", so the bench printed "Missing: the leaf tested" with
               # the leaf plainly present. `missingName()` falls back to the
               # lower-cased dial name when an option does not author one.
               _b7_dial_block("rr", act_id, dials, start,
                              lambda d, o: ' data-f="%s"%s'
                              % (e(_pctnum(o["f"])),
                                 (' data-missing="%s"' % e(o["missing"]))
                                 if o.get("missing") else "")),
               t(setup["all_present"]), t(rate["label"]),
               t(_b7_suffix(100, rate["suffix"])),
               "".join(rows), t(a["test_label"]), t(a["reset_label"]),
               panels))
# ── b7-02 `#s-tuner` · leaf-tuner ────────────────────────────────────────
#
# ⚖️ THE CASCADE IS AUTHORED HERE, ONCE, AND SERIALISED. Design evaluates the
# six habitats as an if/else chain on the two percentages, so an earlier branch
# wins outright and the ORDER is the instrument. The thresholds are the
# renderer's — the record records them in a comment and deliberately does not
# author them, because a key with no read site is a dead key (R5) — and they are
# needed in two places: the resting render, which must show the verdict the
# opening leaf actually earns, and the runtime. Writing them twice is how the
# static page and the live page come to disagree about which habitat a leaf can
# live in, so they are written once, in Python, and shipped to the runtime as
# `data-rules`. There is no expression to parse at either end: a rule is a set
# of bounds and the matcher is four comparisons.
# Design's own template constant above the verdict panel (b7-02 page line 142).
# It is the SAME on all six branches, so it is the block's chrome rather than
# per-branch data — the record says so and deliberately authors no `tag`.
# Lifting it here keeps it authored exactly once without pretending it varies;
# `_WHY_LABEL` in the B5 section is the same decision for the same reason.
_LT_VERDICT_LABEL = "Where this leaf could live"
_LEAF_RULES = (
    {"id": "swamp",    "water_gt": 150, "rate_gte": 90},
    {"id": "worst",    "water_gt": 150},
    {"id": "desert",   "rate_lt": 45, "water_lt": 60},
    {"id": "oak",      "rate_gte": 85, "water_lte": 115},
    {"id": "slow",     "rate_lt": 45},
    {"id": "middling"},
)
def _leaf_verdict(rate_pct, water_pct):
    """The first rule whose bounds the leaf satisfies. Order is the cascade."""
    for rule in _LEAF_RULES:
        ok = True
        for key, bound in rule.items():
            if key == "id":
                continue
            value = rate_pct if key.startswith("rate") else water_pct
            test = key.split("_", 1)[1]
            if test == "gt" and not value > bound:
                ok = False
            elif test == "gte" and not value >= bound:
                ok = False
            elif test == "lt" and not value < bound:
                ok = False
            elif test == "lte" and not value <= bound:
                ok = False
        if ok:
            return rule["id"]
    raise ValueError("the leaf-tuner cascade has no final branch")
def r_leaf_tuner(a, act_id):
    """⊕ b7-02 `#s-tuner` — two readouts that disagree, and no winning setting.

    ⚖️ THE INSTRUMENT OPENS ON A DELIBERATELY BAD LEAF. `start` is enormous,
    thick, many stomata, no cuticle — 110% rate at 363% water — and that is not
    a default anybody forgot to tidy, it IS the lesson: the student's first
    instinct pushes the water readout further up, and `Set it to a real oak
    leaf` is the REVEAL rather than the starting point. The opposite of b7-01's
    bench, deliberately, and asserted here: an opening leaf that already lands
    on `oak` would have answered the question before it was asked.

    ⚖️ THE BAR IS THE PERCENTAGE HALVED AND CLAMPED AT 100, so a FULL bar means
    200% of an oak leaf. Design's own arithmetic, and it is what makes the
    opening leaf's water bar sit hard against the end of its track while its
    rate bar sits at 55% — the picture of the trade-off, before a word of the
    verdict is read.

    ⚠️ NO PER-BRANCH `tag`. The label above the verdict is "Where this leaf
    could live" and it is the SAME on all six, so it is the block's chrome
    rather than per-branch data and the ENGINE emits it. Authoring it six times
    would pretend it varies.
    """
    dials = _b7_dials(a, act_id, ("r", "w"))
    _b7_need(a, act_id, ("start", "oak", "oak_label", "reset_label",
                         "readouts"))

    dial_ids = [d["id"] for d in dials]
    for name in ("start", "oak"):
        preset = a[name]
        if sorted(preset) != sorted(dial_ids):
            raise ValueError(
                "leaf-tuner %r's `%s` sets %s but the bench has dials %s. A "
                "preset that misses a dial leaves it wherever it was, and a "
                "preset naming a dial that is not there is a setting nothing "
                "can apply." % (act_id, name, sorted(preset), sorted(dial_ids)))
        for d in dials:
            if preset[d["id"]] not in [o["id"] for o in d["options"]]:
                raise ValueError(
                    "leaf-tuner %r's `%s` sets dial %r to %r, which is not one "
                    "of its settings."
                    % (act_id, name, d["id"], preset[d["id"]]))

    def product(preset, key):
        out = 1.0
        for d in dials:
            opt = next(o for o in d["options"] if o["id"] == preset[d["id"]])
            out *= float(opt[key])
        return out

    def pcts(preset):
        return (int(round(product(preset, "r") * 100)),
                int(round(product(preset, "w") * 100)))

    start_rate, start_water = pcts(a["start"])
    oak_rate, oak_water = pcts(a["oak"])
    if _leaf_verdict(start_rate, start_water) == _leaf_verdict(oak_rate,
                                                               oak_water):
        raise ValueError(
            "leaf-tuner %r opens on a leaf that lands in the same habitat as "
            "the oak shortcut. The opening leaf is deliberately BAD and the "
            "oak button is the reveal; if the two agree, pressing it reveals "
            "nothing." % act_id)

    verdicts = _b7_verdict_ids(
        a, act_id, [r["id"] for r in _LEAF_RULES],
        "One branch per habitat in the cascade, in the renderer's own order.")
    for key, v in sorted(verdicts.items()):
        for f in ("head", "why"):
            if not v.get(f):
                raise ValueError("leaf-tuner %r verdict %r declares no %r."
                                 % (act_id, key, f))

    readouts = a["readouts"]
    if len(readouts) != 2:
        raise ValueError(
            "leaf-tuner %r draws %d readout(s). The bench is two readouts "
            "pulling against each other." % (act_id, len(readouts)))
    tone_for = {"rate": "ok", "water": "alert"}
    rows = []
    for r in readouts:
        for f in ("id", "label", "suffix"):
            if not r.get(f):
                raise ValueError("leaf-tuner %r readout %r declares no %r."
                                 % (act_id, r.get("id"), f))
        if r["id"] not in tone_for:
            raise ValueError(
                "leaf-tuner %r readout %r is neither `rate` nor `water`. The "
                "renderer keys the product it shows and the colour it takes "
                "off the readout's own id." % (act_id, r["id"]))
        pct = start_rate if r["id"] == "rate" else start_water
        rows.append(
            '<li class="ks3-lt-readout" data-tone="%s">'
            '<div class="ks3-lt-readrow">'
            '<p class="ks3-lt-rolabel">%s</p>'
            '<p class="ks3-lt-rovalue" data-lt-readout="%s" data-suffix="%s">'
            '%s</p></div>'
            '<span class="ks3-lt-track"><span class="ks3-lt-fill" '
            'data-lt-bar="%s" style="width:%s%%"></span></span></li>'
            % (e(tone_for[r["id"]]), t(r["label"]), e(r["id"]), e(r["suffix"]),
               t(_b7_suffix(pct, r["suffix"])), e(r["id"]),
               _pctnum(min(100, pct / 2.0))))

    opening = _leaf_verdict(start_rate, start_water)
    panels = "".join(
        '<div class="ks3-lt-verdict" data-lt-verdict="%s"%s>'
        '<p class="ks3-lt-verdictlabel">%s</p>'
        '<p class="ks3-lt-head">%s</p>'
        '<p class="ks3-lt-why">%s</p></div>'
        % (e(rule["id"]), "" if rule["id"] == opening else " hidden",
           t(_LT_VERDICT_LABEL), t(verdicts[rule["id"]]["head"]),
           rich(verdicts[rule["id"]]["why"]))
        for rule in _LEAF_RULES)

    return ('<div class="ks3-lt" data-lt data-rules="%s" data-start="%s" '
            'data-oak="%s">%s'
            '<div class="ks3-lt-panel">'
            '<ul class="ks3-lt-readouts" role="list">%s</ul>%s'
            '<div class="ks3-lt-foot">'
            '<button type="button" class="ks3-reveal-btn ks3-lt-oak" '
            'data-lt-oak>%s</button>'
            '<button type="button" class="ks3-reveal-btn ks3-lt-reset" '
            'data-lt-reset>%s</button></div></div></div>'
            % (e(json.dumps(list(_LEAF_RULES), separators=(",", ":"),
                            sort_keys=True)),
               e(json.dumps(a["start"], separators=(",", ":"), sort_keys=True)),
               e(json.dumps(a["oak"], separators=(",", ":"), sort_keys=True)),
               _b7_dial_block(
                   "lt", act_id, dials, a["start"],
                   lambda d, o: ' data-r="%s" data-w="%s"'
                   % (e(_pctnum(o["r"])), e(_pctnum(o["w"])))),
               "".join(rows), panels,
               t(a["oak_label"]), t(a["reset_label"])))
# ── b7-03 `#s-bench` · method-breaker ────────────────────────────────────

def _mb_parent(num):
    """The step a SUB-step belongs to: `3b` → `3`. `None` for a whole step.

    ⚖️ THE SUB-STEP RELATIONSHIP IS AUTHORED, in `num`, and it is the only
    thing in the data that says the flame branch depends on the ethanol step.
    Design's page encodes the same fact twice — the fault fires on
    `ethanol === 'yes' && heat === 'flame'`, and the `heat` row is DIMMED when
    the ethanol is skipped — and both fall out of this one derivation. Skip the
    ethanol and there is no fire to have; hard-coding that pair here instead
    would be a fact about b7-03 living in the engine.
    """
    digits = "".join(ch for ch in str(num) if ch.isdigit())
    return digits if digits and digits != str(num) else None
def r_method_breaker(a, act_id):
    """⊕ b7-03 `#s-bench` — break a working method and read what you get.

    ⚖️ THIS BENCH OPENS ON THE GOOD METHOD, which is the opposite of b7-02's
    tuner and the reason every verdict is a consequence of the student's own
    choice rather than a repair of somebody else's. `full` is both the opening
    state and the reset target, and it is authored rather than derived: it is
    the map behind the button labelled "Fresh leaf, full method".

    ⚖️ FAULT PRECEDENCE IS THE PEDAGOGY AND IT IS AUTHORED AS AN ORDERED LIST.
    Safety first — a naked flame stops the bench outright — then the faults that
    DESTROY the result, then the ones that only OBSCURE it. Report "the leaf
    crumbled" ahead of "you skipped the destarching" and the bench has taught
    that a torn leaf and an undatable result are the same size of mistake. Dict
    order would have said the same thing today and stopped saying it the first
    time somebody re-sorted a literal, so the order is read from `precedence`
    and never from the map.

    ⚠️ THE FLAME BRANCH IS A SAFETY BRANCH, NOT A DATA FAULT, and it is drawn
    as one. Its own `why` says the practical has ended and its `conclude` says
    the test never happened; rendering it in the same treatment as "the leaf
    crumbled" would file a fire at head height alongside a spoiled pattern.
    It takes `data-kind="safety"` and its own border, and it is the only
    branch that does. NOTES-B7 flag 14, MRB-233.
    """
    steps = a.get("steps") or []
    if len(steps) < 2:
        raise ValueError(
            "method-breaker %r declares %d step(s). The bench is a method, and "
            "a method with one step cannot be broken in more than one way."
            % (act_id, len(steps)))
    _b7_need(a, act_id, ("full", "precedence", "run_label", "run_done_label",
                         "reset_label", "conclude_label"))

    step_ids, opts_of, num_of = [], {}, {}
    for s in steps:
        for f in ("id", "num", "title", "detail", "options"):
            if not s.get(f):
                raise ValueError(
                    "method-breaker %r step %r declares no %r. `detail` is the "
                    "line that tells a student what the step actually is, and "
                    "a row without one is a switch with no label."
                    % (act_id, s.get("id"), f))
        if s["id"] in step_ids:
            raise ValueError("method-breaker %r declares step id %r twice."
                             % (act_id, s["id"]))
        step_ids.append(s["id"])
        num_of[s["id"]] = str(s["num"])
        ids = []
        for o in s["options"]:
            if not (o.get("id") and o.get("label")):
                raise ValueError(
                    "method-breaker %r step %r has an option missing `id` or "
                    "`label`." % (act_id, s["id"]))
            ids.append(o["id"])
        if len(set(ids)) != len(ids):
            raise ValueError(
                "method-breaker %r step %r offers the same option twice."
                % (act_id, s["id"]))
        opts_of[s["id"]] = ids

    full = a["full"]
    if sorted(full) != sorted(step_ids):
        raise ValueError(
            "method-breaker %r's `full` answers %s but the method has steps "
            "%s. `full` is the opening state AND the reset target, so a step "
            "it does not name opens with no setting at all."
            % (act_id, sorted(full), sorted(step_ids)))
    for sid, choice in sorted(full.items()):
        if choice not in opts_of[sid]:
            raise ValueError(
                "method-breaker %r's `full` sets step %r to %r, which is not "
                "one of its options." % (act_id, sid, choice))

    # A branch id is either a STEP id — the branch fires when that step is
    # skipped — or an OPTION id of a step, which is the SAFETY branch: `heat` is
    # never skipped, it is answered one of two ways, and naming the branch after
    # the wrong ANSWER keeps "the id names the fault" true for all five.
    by_option = {}
    for sid in step_ids:
        for oid in opts_of[sid]:
            by_option.setdefault(oid, []).append(sid)

    precedence, conditions = list(a["precedence"]), {}
    for branch in precedence:
        if branch in step_ids:
            skip = [o for o in opts_of[branch] if o != full[branch]]
            if len(skip) != 1:
                raise ValueError(
                    "method-breaker %r branch %r names a step offering %d "
                    "settings other than the full method's. The branch fires "
                    "when the step is SKIPPED, which needs exactly one way to "
                    "skip it." % (act_id, branch, len(skip)))
            conditions[branch] = [{"step": branch, "is": skip[0]}]
            continue
        owners = [s for s in by_option.get(branch, []) if full.get(s) != branch]
        if len(owners) != 1:
            raise ValueError(
                "method-breaker %r branch %r is neither a step id nor the "
                "wrong answer to exactly one step. A branch id names the "
                "fault, and a fault nothing on the bench can produce is a "
                "verdict no student will reach." % (act_id, branch))
        owner = owners[0]
        cond = [{"step": owner, "is": branch}]
        # The sub-step's parent, if it has one — see `_mb_parent`.
        parent_num = _mb_parent(num_of[owner])
        if parent_num:
            parents = [s for s in step_ids if num_of[s] == parent_num]
            if len(parents) != 1:
                raise ValueError(
                    "method-breaker %r step %r is numbered %r, so it is a "
                    "sub-step of step %r — and %d steps carry that number. The "
                    "numbering is what says which step this one depends on."
                    % (act_id, owner, num_of[owner], parent_num, len(parents)))
            cond.append({"step": parents[0], "is": full[parents[0]]})
        conditions[branch] = cond

    verdicts = _b7_verdict_ids(
        a, act_id, precedence + ["full"],
        "One branch per entry in `precedence`, plus `full` — the fallback when "
        "nothing is broken.")
    for key, v in sorted(verdicts.items()):
        for f in ("tag", "head", "why", "conclude"):
            if not v.get(f):
                raise ValueError(
                    "method-breaker %r verdict %r declares no %r. `conclude` "
                    "is the field the lesson turns on — it is what the result "
                    "licenses, and Design gives it its own rule and its own "
                    "label." % (act_id, key, f))

    # The SAFETY branch: the one whose id is an option rather than a step. It is
    # identified structurally rather than by name, so the treatment follows the
    # shape of the fault and not the spelling of `flame`.
    safety = [b for b in precedence if b not in step_ids]

    rows = "".join(
        '<li class="ks3-mb-step" data-step="%s"%s>'
        '<span class="ks3-mb-num" aria-hidden="true">%s</span>'
        '<span class="ks3-mb-stepmain">'
        '<span class="ks3-mb-steptitle" id="%s-%s-title">%s</span>'
        '<span class="ks3-mb-stepdetail">%s</span></span>'
        '<ul class="ks3-options ks3-mb-opts" role="list" '
        'aria-labelledby="%s-%s-title">%s</ul></li>'
        % (e(s["id"]),
           (' data-parent="%s"'
            % e(next(x for x in step_ids
                     if num_of[x] == _mb_parent(num_of[s["id"]])))
            ) if _mb_parent(num_of[s["id"]]) else "",
           t(s["num"]), e(act_id), e(s["id"]), t(s["title"]), t(s["detail"]),
           e(act_id), e(s["id"]),
           "".join(
               '<li><button type="button" class="ks3-option ks3-mb-opt" '
               'data-step="%s" data-opt="%s" aria-pressed="%s">'
               '<span class="ks3-opt-label">%s</span></button></li>'
               % (e(s["id"]), e(o["id"]),
                  "true" if full[s["id"]] == o["id"] else "false",
                  t(o["label"]))
               for o in s["options"]))
        for s in steps)

    panels = "".join(
        '<div class="ks3-mb-verdict" data-mb-verdict="%s"%s hidden>'
        '<p class="ks3-mb-tag">%s</p>'
        '<p class="ks3-mb-head">%s</p>'
        '<p class="ks3-mb-why">%s</p>'
        '<p class="ks3-mb-conclude"><strong>%s</strong> %s</p></div>'
        % (e(key), ' data-kind="safety"' if key in safety else "",
           t(verdicts[key]["tag"]), t(verdicts[key]["head"]),
           rich(verdicts[key]["why"]), t(a["conclude_label"]),
           rich(verdicts[key]["conclude"]))
        for key in sorted(verdicts))

    return ('<div class="ks3-mb" data-mb data-precedence="%s" '
            'data-conditions="%s" data-full="%s" data-run-label="%s" '
            'data-run-done-label="%s">'
            '<ul class="ks3-mb-steps" role="list">%s</ul>'
            '<div class="ks3-mb-panel">'
            '<div class="ks3-mb-foot">'
            '<button type="button" class="ks3-reveal-btn ks3-mb-run" '
            'data-mb-run>%s</button>'
            '<button type="button" class="ks3-reveal-btn ks3-mb-reset" '
            'data-mb-reset>%s</button></div>%s</div></div>'
            % (e(json.dumps(precedence, separators=(",", ":"))),
               e(json.dumps(conditions, separators=(",", ":"),
                            sort_keys=True)),
               e(json.dumps(full, separators=(",", ":"), sort_keys=True)),
               e(a["run_label"]), e(a["run_done_label"]), rows,
               t(a["run_label"]), t(a["reset_label"]), panels))
# ── b7-04 `#s-trace` · trace-it-back ─────────────────────────────────────

def r_trace_it_back(a, act_id):
    """⊕ b7-04 `#s-trace` — six foods, one destination, six different distances.

    ⚖️ THE CHAIN IS REVEALED BACKWARDS, one link per press, each with its own
    note, and the food's verdict lands only when the chain is complete. The
    chains are deliberately different LENGTHS — bread 3 links, salmon 5 — so the
    step count varies and the destination does not, which is the sentence the
    prompt makes to the student. Padding them to a common length would delete
    the argument.

    ⚖️ HONEY AND MUSHROOM ARE WHY THE INSTRUMENT EXISTS. The mushroom's first
    link says a fungus cannot photosynthesise at all and its last says the
    molecules it lives on were built in a leaf; honey is the shortest chemical
    journey on the plate and belongs to the food that looks least like one.
    Neither is smoothed into the shape of the other four, and nothing here
    sorts, groups or ranks the six.

    ⚠️ EVERY LINK OF EVERY CHAIN IS IN THE DOCUMENT, and the notes are hidden
    rather than absent. The row is drawn from the start — a student reads how
    far there is to go before taking a step — and what arrives on a press is the
    note, which is the answer to "where did that come from?".
    """
    foods = a.get("foods") or []
    if len(foods) < 2:
        raise ValueError(
            "trace-it-back %r declares %d food(s). The block's argument is that "
            "the number of steps changes and the destination does not, which "
            "needs more than one chain." % (act_id, len(foods)))
    _b7_need(a, act_id, ("options_label", "step_label", "done_label",
                         "reset_label", "steps_label"))

    steps_label = a["steps_label"]
    for f in ("idle", "done"):
        if not steps_label.get(f):
            raise ValueError(
                "trace-it-back %r steps_label declares no %r. Both are on "
                "screen — `idle` before a press and `done` when the producer "
                "is reached — and a blank one reads as the bench having "
                "stopped responding." % (act_id, f))
    if "{n}" not in steps_label["done"]:
        raise ValueError(
            "trace-it-back %r steps_label.done names no {n}. The count of "
            "steps back is the one number this instrument is for." % act_id)

    seen, tabs, panels = [], [], []
    for i, f in enumerate(foods):
        for key in ("id", "label", "name", "chain", "verdict"):
            if not f.get(key):
                raise ValueError(
                    "trace-it-back %r food %r declares no %r."
                    % (act_id, f.get("id"), key))
        if f["id"] in seen:
            raise ValueError("trace-it-back %r declares food id %r twice."
                             % (act_id, f["id"]))
        seen.append(f["id"])
        chain = f["chain"]
        if len(chain) < 3:
            raise ValueError(
                "trace-it-back %r food %r has a chain of %d link(s). A chain "
                "that arrives at a producer in one step is a caption, not a "
                "trace." % (act_id, f["id"], len(chain)))
        for link in chain:
            if not (link.get("name") and link.get("note")):
                raise ValueError(
                    "trace-it-back %r food %r has a link missing `name` or "
                    "`note`. The note is the whole reveal — a link that "
                    "unhides nothing is a press that does nothing."
                    % (act_id, f["id"]))

        first = i == 0
        tabs.append(
            '<li><button type="button" class="ks3-option ks3-tb-tab" '
            'data-tb-food="%s" aria-pressed="%s">'
            '<span class="ks3-opt-label">%s</span></button></li>'
            % (e(f["id"]), "true" if first else "false", t(f["label"])))

        links = "".join(
            '<li class="ks3-tb-link" data-i="%d"%s%s>'
            '<span class="ks3-tb-num" aria-hidden="true">%d</span>'
            '<span class="ks3-tb-linkmain">'
            '<span class="ks3-tb-linkname">%s</span>'
            '<span class="ks3-tb-note"%s>%s</span></span></li>'
            % (j, ' data-shown=""' if j == 0 else "",
               ' data-last=""' if j == len(chain) - 1 else "",
               j + 1, t(link["name"]), "" if j == 0 else " hidden",
               t(link["note"]))
            for j, link in enumerate(chain))

        panels.append(
            '<div class="ks3-tb-food" data-tb-panel="%s" data-total="%d"%s>'
            '<div class="ks3-tb-headrow">'
            '<p class="ks3-tb-name">%s</p>'
            '<p class="ks3-tb-steps" data-tb-steps>%s</p></div>'
            '<ol class="ks3-tb-chain" role="list">%s</ol>'
            '<p class="ks3-tb-verdict" data-tb-verdict hidden>%s</p></div>'
            % (e(f["id"]), len(chain), "" if first else " hidden",
               t(f["name"]), t(steps_label["idle"]), links,
               rich(f["verdict"])))

    # ⚠️ `ks3-reveal-btn` ON THE STEP BUTTON — Design's own class, and it is
    # also one of the five signals `check_rail_reachable` reads out of the
    # static page. The food tabs carry `class="ks3-option` for the same reason.
    return ('<div class="ks3-tb" data-tb data-food="%s" data-step-label="%s" '
            'data-done-label="%s" data-steps-idle="%s" data-steps-done="%s">'
            '<div class="ks3-tb-tabsgroup">'
            '<p class="ks3-tb-tabslabel" id="%s-plate">%s</p>'
            '<ul class="ks3-options ks3-tb-tabs" role="list" '
            'aria-labelledby="%s-plate">%s</ul></div>'
            '<div class="ks3-tb-panel">%s'
            '<div class="ks3-tb-foot">'
            '<button type="button" class="ks3-reveal-btn ks3-tb-back" '
            'data-tb-back>%s</button>'
            '<button type="button" class="ks3-reveal-btn ks3-tb-reset" '
            'data-tb-reset>%s</button></div></div></div>'
            % (e(foods[0]["id"]), e(a["step_label"]), e(a["done_label"]),
               e(steps_label["idle"]), e(steps_label["done"]),
               e(act_id), t(a["options_label"]), e(act_id), "".join(tabs),
               "".join(panels), t(a["step_label"]), t(a["reset_label"])))


# ── registrations ────────────────────────────────────────────────────────
ART = {
    'leaf-section': _leaf_section,
}

KIND_SHELL = {
    'reactant-remover': ("ks3-rr-block",
                         ' data-instrument data-rrblock data-stage-done="0"'),
    'leaf-tuner': ("ks3-lt-block",
                         ' data-instrument data-ltblock data-stage-done="0"'),
    'method-breaker': ("ks3-mb-block",
                         ' data-instrument data-mbblock data-stage-done="0"'),
    'trace-it-back': ("ks3-tb-block",
                         ' data-instrument data-tbblock data-stage-done="0"'),
}

KIND_FN = {
    'reactant-remover': r_reactant_remover,
    'leaf-tuner': r_leaf_tuner,
    'method-breaker': r_method_breaker,
    'trace-it-back': r_trace_it_back,
}

KIND_HEAD_START = {
    'trace-it-back': 1,
}

KIND_HEAD_TOTAL = {
    'trace-it-back': lambda a: len(((a.get("foods") or [{}])[0]).get("chain") or []),
}
