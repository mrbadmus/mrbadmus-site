"""ks3_art.b3 — B3's drawers, instruments and registrations.

ONE UNIT, ONE FILE. Nothing here is read by any other unit; nothing
here may be added to any other unit's module. Moved verbatim out of
``build_ks3.py`` by MRB-271 so that two content lanes can build two
units at once without editing the same file.
"""

import html
import json
import math
import re
from ks3_art.kit import (
    _SVG_ACCENT,
    _SVG_ACCENT_TEXT,
    _SVG_ACCENT_TINT,
    _SVG_BAND,
    _SVG_BLUE_TEXT,
    _SVG_CARD,
    _SVG_INK,
    _SVG_INK_BODY,
    _SVG_INK_MUTED,
    _SVG_INSET,
    _SVG_RULE,
    _SVG_RULE_STRONG,
    _circle,
    _ellipse,
    _label,
    _mono,
    _n,
    _path,
    _rect,
    _self_check,
    _svg_open,
    e,
    r_activity_options,
    rich,
    t,
)


# ── ⊕ MRB-254 · WS1 #4, b3-villus-labelled — Design's fig-04, ported ─────
#
# Every number below is Design's. The four tables are the four `<sc-for>`
# loops from her `renderVals()`, moved out of the function body because they
# are the parts a reader might want to check against her file, and burying a
# fourteen-element coordinate list inside 200 lines of drawing hides it.

# Dissolved food in the gut lumen, above and below the villus. Literal in her
# delivery too — the scatter is composed, not generated, so there is no jitter
# function to port and nothing here can drift run to run.
#
# ⊕ FIVE OF THE FOURTEEN ARE MOVED FROM DESIGN'S COORDINATES, and the reason is
# always the same: in her delivery they sit ON a word. A 5px disc struck
# through "digested food, in the gut" does not read as a scatter dot with a
# label near it, it reads as a typo in the label. Their exact positions carry
# nothing — this is the one thing on the plate that is decoration rather than
# anatomy, so it is the thing that gets out of the way of the words. Her
# originals are in the comment on each line; count, radius, paint and the
# above/below-the-villus distribution are all unchanged.
_VILLUS_FOOD = ((90, 422),    # was (90, 400)  — was inside "digested food…"
                (150, 416),
                (220, 417),   # was (220, 398) — was inside "…in the gut"
                (300, 414),
                (360, 400),
                (470, 414),
                (560, 416),   # was (560, 400) — was inside "amino acids"
                (700, 470), (740, 520), (96, 600), (200, 604), (330, 596),
                (712, 606),   # was (470, 606) — was inside the closing line
                (770, 598))   # was (600, 598) — was inside the closing line
# The three things that cross the wall. `(x, label, hook)` — the hook is the
# label slugged, and it is what `data-crossing` carries, so a parity row can
# name the three molecules rather than counting three anonymous arrows.
_VILLUS_CROSSINGS = ((400, "glucose", "glucose"),
                     (520, "amino acids", "amino-acids"),
                     (640, "fatty acids", "fatty-acids"))
# The callout wedges, in Design's drawing order: `(wedge, upper edge, lower
# edge, opened FROM, opened INTO)`. The last two are the whole point of the
# figure expressed as data — see the note on nesting in the docstring.
_VILLUS_CALLOUTS = (
    ("M 200,178 L 310,70 L 310,300 L 200,222 Z",
     "M 200,178 L 310,70", "M 200,222 L 310,300", "tube", "villi"),
    ("M 458,168 L 590,70 L 590,300 L 458,212 Z",
     "M 458,168 L 590,70", "M 458,212 L 590,300", "villi", "microvilli"),
    # ⊕ MRB-254 · THIS ONE'S MOUTH WAS 120–700 AT y=378 AND IS NOW 199–583 AT
    # y=352. Read the note in the docstring before changing it back.
    ("M 386,300 L 199,352 L 583,352 L 430,300 Z",
     "M 386,300 L 199,352", "M 430,300 L 583,352", "villi", "section"),
)
def _villus(fig):
    """Folding at three scales, each opened out of the one before it, then one
    villus cut lengthways so the wall can be counted.

    ⚖️ THE NESTING IS THE FIGURE, and it is drawn rather than stated. "The gut
    is ridged, the ridges carry villi, the villi carry microvilli" is three
    sentences, and three sentences are three things to memorise — a student
    who meets them as a list has no reason to believe they are the same fact
    at three magnifications, and routinely comes away thinking villi and
    microvilli are two different structures somewhere else in the gut. So each
    frame is entered through a wedge whose narrow end sits on the exact spot in
    the previous frame that it magnifies: frame 2 opens out of the dashed ring
    on the tube, frame 3 opens out of the dashed rings round two villi, and the
    section below opens out of the same row of villi. The chain is physically
    on the page, and a reader can follow it backwards.

    ⚖️ AND THE CHAIN IS ASSERTABLE, not just drawn. Each frame carries
    `data-scale` (`tube`, `villi`, `microvilli`; the section panel carries
    `data-section` instead, since it is a cut rather than a magnification), and
    each wedge carries `data-zoom-from` / `data-zoom-to`. A content-truth row
    can then check that every wedge starts at the scale before the one it ends
    at and at no other — which is the one defect that would be invisible in a
    screenshot, because a wedge drawn from the WRONG frame still looks like a
    wedge. That is the ENCODING rather than the frame, in MRB-257 decision 4's
    sense.

    ⚖️ THE WALL IS ONE CELL THICK, AND THE DRAWING LETS THAT BE COUNTED. The
    reason the folding is worth doing at all is on the other side of it: the
    barrier between the gut and the blood is a single cell. A drawing can claim
    that with a label and a leader — and a label points at ONE PLACE, so a wall
    that was one cell thick where the arrow lands and vaguely two cells thick
    further along would pass. Design divides the wall with cross lines that
    each run the FULL thickness, from the outer outline to the inner one, along
    the whole length of the villus and on both faces of it. So every cross line
    carries `data-wall-cell` (its index), `data-wall-edge` (which face) and
    `data-wall-span` (30 units — the gap between the outer and inner wall
    paths, which carry `data-wall="outer"` and `data-wall="inner"`). A row can
    count the cells and assert that not one of them is subdivided, anywhere.

    ⚠️ `Math.round`, NOT `round`. The villi stand on a fold, so their bases sit
    on a half sine — `250 - Math.round(Math.sin(i / 11 * π) * 8)`. Python's
    `round` is banker's rounding and JavaScript's `Math.round` is round-half-up,
    so the two disagree on any exact `.5`. None of these twelve values is a tie
    today, which is exactly why this would have been safe until somebody
    changed the amplitude from 8 and then quietly lost a pixel on one villus.
    `math.floor(v + 0.5)` is `Math.round` for non-negative `v`, which all of
    these are, so the port is the JS rather than a near-miss of it.

    ⚠️ THE ONE HUE, AND WHY IT IS NOT CARRYING A FACT ALONE. `--ks3-blue-text`
    paints the capillary, and nothing else on the plate. It never has to be
    seen as blue: the capillary is named in a bold label with a leader line
    onto it, the direction of flow is two DRAWN triangles rather than a tint,
    and the three crossing arrows are ink like everything else. Design's own
    NOTES-FIGURES says this hue appears "in #7 only" — her delivery uses it
    here too, and under MRB-205 the delivery wins. Recorded in the port report.

    ⛔ EVERY ARROWHEAD IS A DRAWN TRIANGLE AT DESIGN'S OWN COORDINATES, not
    `_arrow`. She placed all five heads by hand — three crossing the wall, two
    inside the capillary — and `_arrow` would recompute them from an angle and
    land them a fraction off her line. `_arrow` is for a head this file
    computes; these are hers.

    ⊕ THREE COLLISIONS IN DESIGN'S DELIVERY ARE REPAIRED HERE, and nothing
    else about the drawing is touched: with these three reverted, a render of
    this drawer is byte-identical to a render of her SVG. Each was a collision
    rather than a composition — the three crossing arrows drawn through the
    words that name them, five food discs struck through two labels, and the
    third frame's heading running four units off the edge of the viewBox. The
    rule applied each time was that the thing carrying the science holds its
    position and the thing carrying none moves: the shafts stay and the labels
    step aside; the words stay and the scatter moves; the heading is re-anchored
    rather than re-worded. Each site says what it was.

    ⚠️ CLIP IDS ARE DERIVED FROM THE FIGURE ID. Design's are `f4A`…`f4D`, which
    are unique inside a review file that holds one figure. A lesson page can
    hold several of these drawings, `id` is document-scoped, and a duplicate
    `clipPath` id means the second figure silently clips to the first one's
    rectangle. Nothing warns; the drawing just loses half of itself.
    """
    W, H = 860, 640
    cid = e(fig["id"])
    out = [_svg_open(fig, W, H)]

    # The four windows. Raw markup rather than an emitter call because a
    # <clipPath> carries no paint — there is no paint law to keep here, and
    # `r_triangle` already sets this precedent in this file.
    out.append(
        '<defs>'
        '<clipPath id="%s-c-tube"><rect x="30" y="70" width="240" '
        'height="230" rx="16"/></clipPath>'
        '<clipPath id="%s-c-villi"><rect x="310" y="70" width="240" '
        'height="230" rx="16"/></clipPath>'
        '<clipPath id="%s-c-micro"><rect x="590" y="70" width="240" '
        'height="230" rx="16"/></clipPath>'
        '<clipPath id="%s-c-section"><rect x="30" y="378" width="800" '
        'height="252" rx="16"/></clipPath>'
        '</defs>' % (cid, cid, cid, cid))

    # Design's root group. Round caps and joins on everything: the villi, the
    # microvilli and the folds are all organic outlines, and a mitred join on a
    # 2px stroke round a 14-unit finger reads as a spike.
    out.append('<g stroke-linecap="round" stroke-linejoin="round">')

    # ── the callout wedges, drawn first so every frame sits on top of them ──
    #
    # ⚠️ EVERY HOOK IS SPELLED `data_…` AT THE CALL SITE, and `_data_attrs`
    # strips the prefix back off. A bare `zoom_from=` now raises. Both halves
    # matter: the call site reads as the attribute it produces, and a keyword
    # that is NOT a hook cannot slip through and land as a presentation
    # attribute that does nothing while looking like it does something.
    for wedge, edge_hi, edge_lo, src, dst in _VILLUS_CALLOUTS:
        out.append(_path(wedge, fill=_SVG_ACCENT_TINT, stroke="none",
                         data_zoom_from=src, data_zoom_to=dst))
        for edge in (edge_hi, edge_lo):
            out.append(_path(edge, stroke=_SVG_RULE_STRONG, w=1.6, dash="6 5",
                             data_zoom_from=src, data_zoom_to=dst))

    # ── 1 · the tube, cut open at the near end ──────────────────────────────
    out.append(_mono(30, 58, "1 · RINGED FOLDS", size=14, weight="400",
                     spacing="1.4"))
    out.append(_rect(30, 70, 240, 230, rx=16, fill=_SVG_CARD, stroke=_SVG_INK,
                     w=2.5, data_scale="tube"))
    out.append('<g clip-path="url(#%s-c-tube)">' % cid)
    out.append(_path("M 60,150 H 262 M 60,250 H 262", stroke=_SVG_INK, w=2.5))
    # Five ring-folds down the run of the tube. Half-ellipse arcs, so they read
    # as rings seen in perspective rather than as bars across a flat strip.
    out.append(_path(
        "M 100,150 A 16,50 0 0 1 100,250 M 140,150 A 16,50 0 0 1 140,250 "
        "M 180,150 A 16,50 0 0 1 180,250 M 220,150 A 16,50 0 0 1 220,250 "
        "M 260,150 A 16,50 0 0 1 260,250", stroke=_SVG_INK, w=2.5))
    out.append(_ellipse(60, 200, 16, 50, fill=_SVG_BAND, stroke=_SVG_INK,
                        w=2.5))
    out.append('</g>')
    # The ring the next frame is opened from, drawn outside the clip so it can
    # sit on the frame's own edge.
    out.append(_circle(180, 200, 30, stroke=_SVG_INK, w=1.6, dash="6 5"))
    out.append(_label(30, 326, "Not a smooth pipe. The wall", size=17,
                      fill=_SVG_INK_BODY, weight="400", anchor="start"))
    out.append(_label(30, 348, "is thrown into ridges.", size=17,
                      fill=_SVG_INK_BODY, weight="400", anchor="start"))

    # ── 2 · villi standing on one fold ──────────────────────────────────────
    out.append(_mono(310, 58, "2 · VILLI ON EVERY FOLD", size=14,
                     weight="400", spacing="1.4"))
    out.append(_rect(310, 70, 240, 230, rx=16, fill=_SVG_CARD, stroke=_SVG_INK,
                     w=2.5, data_scale="villi"))
    out.append('<g clip-path="url(#%s-c-villi)">' % cid)
    for i in range(12):
        x = 322 + i * 19
        # See ⚠️ in the docstring: this is `Math.round`, spelled so.
        base = 250 - int(math.floor(math.sin((i / 11) * math.pi) * 8 + 0.5))
        top = base - 74
        out.append(_path(
            "M %s,%s V %s Q %s,%s %s,%s V %s Z"
            % (_n(x), _n(base), _n(top + 9), _n(x + 7), _n(top - 2),
               _n(x + 14), _n(top + 9), _n(base)),
            fill=_SVG_BAND, stroke=_SVG_INK, w=2))
    # The fold the villi stand on, drawn after them so it closes their bases.
    out.append(_path("M 310,246 C 380,238 480,238 550,246", stroke=_SVG_INK,
                     w=3))
    out.append(_path("M 310,272 C 380,264 480,264 550,272", stroke=_SVG_INK,
                     w=2))
    out.append('</g>')
    out.append(_circle(404, 190, 26, stroke=_SVG_INK, w=1.6, dash="6 5"))
    out.append(_circle(470, 190, 26, stroke=_SVG_INK, w=1.6, dash="6 5"))
    # ⊕ MRB-254 · THREE LINES FROM x=360, WHERE THERE WERE TWO FROM x=310.
    # This caption and the third callout wedge cannot both be where Design put
    # them, and the arithmetic is in the docstring. The short version: the
    # wedge's apex sits at x 386–430 on this frame's bottom edge, this caption
    # begins 9.7 units below that edge and runs 310–502, and a straight edge
    # leaving the apex is still inside those numbers when it gets there. So the
    # caption is set narrow enough to sit BETWEEN the two edges rather than
    # across them — 'Every ridge' is 81 units against a 107-unit opening at the
    # first line's top, which is the tightest of the three and the reason the
    # first line is that short.
    out.append(_label(360, 326, "Every ridge", size=17,
                      fill=_SVG_INK_BODY, weight="400", anchor="start"))
    out.append(_label(360, 348, "is furred with villi,", size=17,
                      fill=_SVG_INK_BODY, weight="400", anchor="start"))
    out.append(_label(360, 370, "standing upright.", size=17,
                      fill=_SVG_INK_BODY, weight="400", anchor="start"))

    # ── 3 · microvilli on one villus cell ───────────────────────────────────
    # ⊕ PINNED TO THE FRAME'S RIGHT EDGE, NOT ITS LEFT. Headings 1 and 2 are
    # short enough to start at their frame's left edge; this one is 274 units
    # of tracked mono and, started at 590, its last letter lands at 864 — four
    # units OUTSIDE an 860 viewBox, so the "L" is simply cut off. Anchored to
    # the frame's right edge instead it ends at 830, which is the same 30-unit
    # margin frame 1 keeps on the left, and it ends there whatever the font
    # does: an end anchor spends a metric change on the far end of the string,
    # where there is 20 units of clear air before heading 2, rather than on the
    # plate edge, where there is none.
    out.append(_mono(830, 58, "3 · MICROVILLI ON EVERY CELL", size=14,
                     weight="400", spacing="1.4", anchor="end"))
    out.append(_rect(590, 70, 240, 230, rx=16, fill=_SVG_CARD, stroke=_SVG_INK,
                     w=2.5, data_scale="microvilli"))
    out.append('<g clip-path="url(#%s-c-micro)">' % cid)
    for i in range(22):
        x = 614 + i * 9
        out.append(_path(
            "M %s,200 V 174 Q %s,168 %s,174 V 200 Z"
            % (_n(x), _n(x + 2.5), _n(x + 5)),
            fill=_SVG_BAND, stroke=_SVG_INK, w=1.6))
    # The cell body they stand on, and its nucleus — so the frame is legible as
    # ONE CELL rather than as a strip of texture.
    out.append(_path("M 610,196 H 812 V 268 H 610 Z", fill=_SVG_BAND,
                     stroke=_SVG_INK, w=2.5))
    out.append(_circle(710, 238, 11, fill=_SVG_CARD, stroke=_SVG_INK, w=2))
    out.append('</g>')
    out.append(_label(590, 326, "And every cell of every", size=17,
                      fill=_SVG_INK_BODY, weight="400", anchor="start"))
    out.append(_label(590, 348, "villus is furred again.", size=17,
                      fill=_SVG_INK_BODY, weight="400", anchor="start"))

    # ── the section: one villus, cut lengthways ─────────────────────────────
    out.append(_mono(30, 370, "ONE VILLUS, CUT LENGTHWAYS", size=14,
                     weight="400", spacing="1.4"))
    out.append(_rect(30, 378, 800, 252, rx=16, fill=_SVG_BAND, stroke=_SVG_INK,
                     w=2.5, data_section="one-villus"))
    out.append('<g clip-path="url(#%s-c-section)">' % cid)
    for cx, cy in _VILLUS_FOOD:
        out.append(_circle(cx, cy, 5, fill=_SVG_CARD, stroke=_SVG_INK, w=1.6))
    # Outer outline and inner face. The 30 units between them ARE the wall, and
    # `data-wall-span` on every cross line below is measured against this gap.
    out.append(_path("M 30,432 H 640 C 706,432 706,576 640,576 H 30 Z",
                     fill=_SVG_CARD, stroke=_SVG_INK, w=2.5,
                     data_wall="outer"))
    out.append(_path("M 30,462 H 628 C 676,462 676,546 628,546 H 30",
                     stroke=_SVG_INK, w=2.5, data_wall="inner"))
    for i, x in enumerate(range(74, 605, 44)):
        out.append(_path("M %s,432 V 462" % _n(x), stroke=_SVG_INK, w=1.6,
                         data_wall_cell=i + 1, data_wall_edge="top",
                         data_wall_span=30))
        out.append(_path("M %s,546 V 576" % _n(x), stroke=_SVG_INK, w=1.6,
                         data_wall_cell=i + 1, data_wall_edge="bottom",
                         data_wall_span=30))
    # The capillary, and the blood going up the villus and back down it.
    out.append(_path("M 30,492 H 592 C 622,492 622,516 592,516 H 30",
                     stroke=_SVG_BLUE_TEXT, w=7, data_capillary="1"))
    out.append(_path("M 120,485 L 120,499 L 136,492 Z", fill=_SVG_BLUE_TEXT,
                     stroke="none"))
    out.append(_path("M 136,509 L 136,523 L 120,516 Z", fill=_SVG_BLUE_TEXT,
                     stroke="none"))
    # The three crossings: shaft, then Design's own head triangle.
    for x, _text, hook in _VILLUS_CROSSINGS:
        out.append(_path("M %s,392 V 448" % _n(x), stroke=_SVG_INK, w=3,
                         data_crossing=hook))
        out.append(_path("M %s,446 L %s,446 L %s,460 Z"
                         % (_n(x - 7), _n(x + 7), _n(x)),
                         fill=_SVG_INK, stroke="none", data_crossing=hook))
    out.append('</g>')

    # ── the labels on the section, outside the clip ─────────────────────────
    # ⊕ BESIDE THE SHAFT, NOT ON IT. Design centres each of these three on its
    # own arrow at the same y the arrow starts, so every shaft is drawn
    # straight down through the middle of the word that names it. The shafts
    # stay exactly where she put them — they are the science — and the labels
    # step 10 units to the right of them, reading away from the arrow they
    # belong to. Nothing else fits: the shaft spans the full depth of the
    # lumen at that x, and there is no room above it between the panel edge
    # and the cap-height of a 16px label.
    for x, text, _hook in _VILLUS_CROSSINGS:
        out.append(_label(x + 10, 404, text, size=16, fill=_SVG_INK,
                          weight="400", anchor="start"))
    out.append(_label(52, 404, "digested food, in the gut", size=16,
                      fill=_SVG_INK, weight="400", anchor="start"))
    out.append(_label(52, 482, "the wall — one cell thick", size=16,
                      fill=_SVG_INK, weight="700", anchor="start"))
    out.append(_path("M 240,472 L 262,462", stroke=_SVG_INK, w=1.4))
    out.append(_label(160, 540, "a capillary, right inside the villus",
                      size=16, fill=_SVG_INK, weight="700", anchor="start"))
    out.append(_path("M 300,530 L 320,518", stroke=_SVG_INK, w=1.4))
    out.append(_mono(700, 608, "one cell, and the food is in the blood",
                     size=14, weight="400", anchor="end"))

    out.append('</g>')
    out.append('</svg>')
    return "".join(out)
# ── ⊕ MRB-254 · WS1 #6, b3-gut-labelled — Design's fig-06, ported ────────
#
# Every coordinate below is Design's, to the control point. Her `renderVals()`
# holds nothing but the review-width switcher, which ruling 6 drops entirely,
# so there is no `<sc-for>` to port here — the drawing is literal throughout.
#
# The tables exist because the four things a content-truth row has to WALK —
# the tube in path order, the seven stops, the four ducts, and the key's seven
# rows — are the parts a reader will want to check against her file, and
# burying a fifteen-curve path inside 200 lines of drawing hides it.

# ── the tube, as three stroked runs ─────────────────────────────────────
#
# `(segment, part, d, wall width, lumen width)`. Each run is drawn twice: an
# ink stroke, then a narrower inset stroke down the middle of it, which is how
# a flat stroke reads as a tube with a hole in it rather than as a line.
#
# ⚠️ THE SEGMENT NUMBERS ARE PATH ORDER, NOT PAINT ORDER. Segment 2 is the
# stomach, which Design paints AFTER the intestines so its bag closes over the
# start of the coils. The numbers are what a row walks; the order of `out` is
# what the reader sees. They are allowed to differ and here they do.
_GUT_TUBE_RUNS = (
    ("1", "oesophagus", "M 500,100 V 256", 21, 15),
    ("3", "small-intestine",
     "M 466,362 C 452,376 448,398 456,416 C 464,434 482,440 498,436 "
     "C 556,430 628,440 632,466 C 636,494 570,504 490,504 "
     "C 410,504 364,512 362,536 C 360,562 426,572 504,572 "
     "C 582,572 636,580 636,606 C 636,632 568,640 488,640 "
     "C 408,640 364,648 364,672 C 364,694 410,702 444,700", 21, 15),
    ("4", "large-intestine",
     "M 444,700 C 396,700 364,718 364,746 C 364,776 440,788 520,788 "
     "C 556,788 574,784 580,774 V 800", 34, 28),
)
# Segment 2. The stomach is a bag, not a stroked run, so it is three paths:
# the fill, the outer wall from where the oesophagus enters to where the tube
# leaves, and the inner face of the muscular wall that gives it its thickness.
_GUT_TUBE_STOMACH_FILL = (
    "M 496,254 C 562,254 618,292 616,344 C 614,396 560,426 510,414 "
    "C 484,408 466,386 460,364 L 490,356 C 496,374 510,386 528,390 "
    "C 560,396 588,374 586,340 C 584,300 548,280 490,280 Z")
_GUT_TUBE_STOMACH_WALL = (
    "M 496,254 C 562,254 618,292 616,344 C 614,396 560,426 510,414 "
    "C 484,408 466,386 460,364")
_GUT_TUBE_STOMACH_INNER = (
    "M 490,280 C 548,280 584,300 586,340 C 588,374 560,396 528,390 "
    "C 510,386 496,374 490,356")
# The food's route: ONE `<path>`, one `M`, from the mouth to the anus. See the
# docstring — this element is the figure's whole claim, and it is the only one
# on the plate that cannot be broken without the break being visible.
_GUT_TUBE_FOOD = (
    "M 500,100 V 254 C 540,262 574,296 572,340 C 570,382 540,404 510,398 "
    "C 488,394 472,380 466,362 C 452,376 448,398 456,416 "
    "C 464,434 482,440 498,436 C 556,430 628,440 632,466 "
    "C 636,494 570,504 490,504 C 410,504 364,512 362,536 "
    "C 360,562 426,572 504,572 C 582,572 636,580 636,606 "
    "C 636,632 568,640 488,640 C 408,640 364,648 364,672 "
    "C 364,694 410,702 444,700 C 396,700 364,718 364,746 "
    "C 364,776 440,788 520,788 C 556,788 574,784 580,774 V 800")
# ── the ducts: `(slug, from, to, d)` ────────────────────────────────────
#
# Three tributaries, one for each organ, joining into one common duct that
# runs right and meets the tube just past the stomach. `to` is set on the
# common duct only, because it is the only one of the four that touches the
# tube — which is the drawn form of "the juices go in there, and only there".
_GUT_TUBE_DUCTS = (
    ("liver", "liver", None, "M 268,320 C 276,336 282,346 290,354"),
    ("gall-bladder", "gall-bladder", None,
     "M 268,364 C 278,366 286,368 292,370"),
    ("pancreas", "pancreas", None, "M 314,392 C 330,396 344,398 360,398"),
    ("common", "junction", "tube",
     "M 290,354 C 312,372 342,390 382,396 C 414,400 440,400 458,400"),
)
# ── the seven stops, in position on the plate ───────────────────────────
#
# `(numeral, organ, on the tube, leader d, badge cx, badge cy)`. 05 is the
# odd one and everything about it says so: a dashed badge, a card fill instead
# of a band fill, a leader that points at the dashed boundary rather than at
# the tube, and `data-on-tube="0"`.
_GUT_TUBE_STOPS = (
    ("01", "mouth", True, "M 566,112 L 514,112", 580, 110),
    ("02", "oesophagus", True, "M 566,202 L 514,202", 580, 200),
    ("03", "stomach", True, "M 674,344 L 620,344", 688, 344),
    ("04", "small-intestine", True, "M 700,472 L 638,466", 714, 470),
    ("05", "pancreas-liver-gall-bladder", False,
     "M 116,300 L 106,300", 72, 300),
    ("06", "large-intestine", True, "M 654,760 L 598,776", 668, 756),
    ("07", "rectum-anus", True, "M 638,792 L 596,798", 652, 790),
)
# The notes that hang off three of the badges: `(x, y, text, anchor, muted)`.
# `muted` picks the ink; the tokens themselves are resolved in the function,
# so this table can sit above their definitions without caring where the
# splice lands it.
_GUT_TUBE_NOTES = {
    "04": ((858, 510, "6–7 m of narrow", "end", False),
           (858, 528, "tube, coiled", "end", False)),
    "05": ((72, 330, "off the tube", "middle", True),),
    "06": ((858, 762, "wider, and shorter", "end", False),),
}
# ── the key: `(numeral, organ, on the tube, badge x, text x, cy, title,
# body)`. Two columns, 01–04 left and 05–07 right, as Design sets them.
_GUT_TUBE_KEY = (
    ("01", "mouth", True, 38, 64, 898, "Mouth",
     "Chewed and mixed with saliva"),
    ("02", "oesophagus", True, 38, 64, 954, "Oesophagus",
     "Squeezed down by muscle. Nothing is broken here"),
    ("03", "stomach", True, 38, 64, 1010, "Stomach",
     "Churned in acid. Protein begins"),
    ("04", "small-intestine", True, 38, 64, 1066, "Small intestine",
     "Every nutrient finished, and almost all absorption"),
    ("05", "pancreas-liver-gall-bladder", False, 494, 520, 898,
     "Pancreas, liver and gall bladder", "Juices in. No food passes through"),
    ("06", "large-intestine", True, 494, 520, 954, "Large intestine",
     "Water absorbed. The nutrients have gone"),
    ("07", "rectum-anus", True, 494, 520, 1010, "Rectum and anus",
     "Stored, then out. Never absorbed"),
)
def _gut_tube(fig):
    """The whole gut as one continuous tube coiled down the frame, seven stops
    numbered in position on it, and the three organs that feed it drawn beside
    it rather than in it.

    ⚖️ THE ANATOMICAL SIMPLIFICATION IS RULED IN, AND SO IS THE SENTENCE THAT
    DISCLOSES IT. The coils are not in anatomical position: the colon does not
    frame the small intestine, and there is no torso outline. Drawn properly,
    the transverse colon has to cross in FRONT of the small intestine and the
    duodenum has to cross back BEHIND it, and at that point the reader is
    untangling two tubes instead of following one — which destroys the single
    claim the figure exists to make. Design chose one legible run down the
    frame, and disclosed the choice on the plate itself, bottom right, in two
    mono lines carrying `data-disclosure`. Both halves were ruled in together
    and the second is the reason the first is allowed: an undisclosed
    simplification is a drawing that quietly says something untrue about where
    the organs are. The disclosure is addressed to the student about the thing
    in front of them, not to a reviewer about how the page works, so it passes
    §8.10 on exactly that test. It does not move to the caption, it does not
    shrink, and its absence is a red gate.

    ⚖️ ONE PATH, AND IT IS ONE ELEMENT. The orange line is a single `<path>`
    with a single `M`, from (500,100) at the mouth to (580,800) at the anus. A
    row can assert continuity on it exactly — one move command, endpoints at
    the tube's own ends — which is a stronger check than any walk of the tube
    wall, because a path with one `M` CANNOT be discontinuous. It carries
    `data-path="food"` and no `data-tube`: it is what moves through the tube,
    not the tube.

    ⚖️ AND THE TUBE ITSELF IS STILL WALKABLE, because the defect this figure
    has to survive is a tube broken at one coil, which still looks like a gut.
    Every element of the tube carries `data-tube="1"`, `data-segment` (1–4, in
    PATH order), `data-tube-part` and `data-tube-layer`. The four elements
    where the layer is `wall` are the spine, one per segment, and they chain:

        1 oesophagus      starts (500,100)  ends (500,256)
        2 stomach         starts (496,254)  ends (460,364)
        3 small intestine starts (466,362)  ends (444,700)
        4 large intestine starts (444,700)  ends (580,800)

    ⚠️ THE JOINTS OVERLAP; THEY DO NOT MEET AT A POINT. Design's measured gaps
    are 4.47 units (1 into 2), 6.32 (2 into 3) and 0 (3 into 4). That is
    deliberate drawing, not sloppiness: the oesophagus is a 21-unit stroke
    running INTO the stomach bag, and the bag's outline starts a few units
    inside it, so the ink overlaps and no seam is visible. A continuity row
    therefore needs a tolerance, and the honest one is half the tube's stroke
    width — 10.5 — because a gap smaller than that is inside the ink and a gap
    larger than it is a hole a reader could see. A zero-tolerance row would
    fail Design's own drawing, which is the wrong thing for a gate to do.

    ⊕ THE SMALL INTESTINE IS TRUNCATED AT THE CAECUM, and the render is
    unchanged. Design draws the narrow 21/15 run all the way to (580,800) and
    then paints the wide 34/28 colon over its last third along the same centre
    line. Every pixel of that tail is inside the wider stroke drawn after it,
    so cutting the narrow path at (444,700) — where the colon begins — is
    invisible in the output and makes segments 3 and 4 meet exactly instead of
    ending at the same point as each other. It is a refinement inside her
    shape, not a new one: the junction it now encodes is the caecum, which is
    where she drew the widening anyway. Recorded in the port report.

    ⚖️ FOOD PASSES BY THE ACCESSORY ORGANS, AND THAT IS DRAWN AS AN ABSENCE.
    The liver, gall bladder and pancreas carry `data-accessory` and NOT
    `data-tube` — there is no element on the plate that is both. They sit
    inside a dashed boundary well clear of the run, and they reach the tube
    only through ducts: three tributaries, one per organ, joining into one
    common duct that is the single duct touching the tube. So "juices in, food
    never through" is checkable three ways — no accessory is part of the tube,
    every accessory has a duct, and the orange line's least x is 360 while the
    boundary's right edge is 340, so the food's route never enters the box.

    ⚠️ 05 IS A STOP THAT IS NOT ON THE TUBE, and a row asserting the stops run
    in order down the drawn path has to know that before it sorts them. Its
    badge sits at y=300, between 02 and 03, because it is beside the tube
    rather than along it. Hence `data-on-tube` on every badge: filter to `1`
    and the six remaining numerals are strictly increasing in y, which is the
    assertion; without the hook the row either fails on Design's correct
    drawing or is written to skip "05" by name, which is a row that has
    memorised the answer.

    ⚠️ THE KEY REPEATS ALL SEVEN NUMERALS AND MUST NOT REPEAT THE HOOK. The
    seven rows at the bottom carry `data-key-stop` / `data-key-organ`, not
    `data-stop` / `data-organ`, so "seven stops, no gaps and no repeats" stays
    an assertion about the seven badges IN POSITION on the drawing — which is
    the teaching claim — while a second row can still check that the key names
    the same seven. Sharing one hook name would have made the natural count
    fourteen and the natural repeat-check fail on a correct figure. Same
    reason the leader lines carry `data-stop-leader` and the numerals
    `data-stop-numeral`: one element per stop owns `data-stop`, and it is the
    badge, which has the position a row needs.

    ⚠️ ONE 12px LABEL RAISED TO 13, AND IT NOW USES ALL THE ROOM THERE IS.
    "off the tube", under badge 05. It sits in the 96-unit channel between the
    plate frame at x=24 and the dashed boundary at x=120, and at 13px in DM
    Mono the string measures 93 units — measured off the render, not guessed.
    Design centred it at x=72, which is the midpoint of that channel, so the
    raise consumes the slack (about 5 units a side at 12px, about 1 at 13) and
    still fits without touching either line. Her x is kept rather than nudged:
    it is the only value that fits, and it is also the badge's own centre, so
    moving it to buy clearance would cost the alignment instead. Reported, not
    fixed.

    ⚠️ CLIP IDS ARE DERIVED FROM THE FIGURE ID. Design's is `f6P`, unique
    inside a review file holding one figure. A lesson page can hold several of
    these drawings, `id` is document-scoped, and a duplicate `clipPath` id
    means the second figure silently clips to the first one's rectangle.
    Nothing warns; the drawing just loses half of itself.
    """
    W, H = 900, 1250
    cid = e(fig["id"])
    out = [_svg_open(fig, W, H)]

    # The plate window. Raw markup rather than an emitter call because a
    # <clipPath> carries no paint — there is no paint law to keep here.
    out.append(
        '<defs><clipPath id="%s-c-plate"><rect x="24" y="54" width="852" '
        'height="760" rx="18"/></clipPath></defs>' % cid)

    # Design's root group. Round caps and joins on everything: every line on
    # the plate is either a tube or an organ outline, and a mitred join on a
    # 21-unit stroke turning through a coil reads as a spike.
    out.append('<g stroke-linecap="round" stroke-linejoin="round">')

    out.append(_rect(24, 54, 852, 760, rx=18, fill=_SVG_CARD, stroke=_SVG_INK,
                     w=2.5))

    out.append('<g clip-path="url(#%s-c-plate)">' % cid)

    # ── the tube: ink wall, then inset lumen, run by run ────────────────
    for seg, part, d, w_wall, w_lumen in _GUT_TUBE_RUNS:
        out.append(_path(d, stroke=_SVG_INK, w=w_wall, data_tube="1",
                         data_segment=seg, data_tube_part=part,
                         data_tube_layer="wall"))
        out.append(_path(d, stroke=_SVG_INSET, w=w_lumen, data_tube="1",
                         data_segment=seg, data_tube_part=part,
                         data_tube_layer="lumen"))

    # ── segment 2, the stomach, painted over the start of the coils ─────
    out.append(_path(_GUT_TUBE_STOMACH_FILL, fill=_SVG_BAND, stroke="none",
                     data_tube="1", data_segment="2", data_tube_part="stomach",
                     data_tube_layer="fill"))
    out.append(_path(_GUT_TUBE_STOMACH_WALL, stroke=_SVG_INK, w=2.5,
                     data_tube="1", data_segment="2", data_tube_part="stomach",
                     data_tube_layer="wall"))
    out.append(_path(_GUT_TUBE_STOMACH_INNER, stroke=_SVG_INK, w=2.5,
                     data_tube="1", data_segment="2", data_tube_part="stomach",
                     data_tube_layer="inner-wall"))

    # ── stop 05: three organs, inside a dashed boundary, off the tube ───
    out.append(_rect(120, 218, 220, 218, rx=20, stroke=_SVG_INK, w=2,
                     dash="8 6", data_accessory_boundary="1"))
    out.append(_path("M 132,240 C 180,222 262,228 314,252 L 318,314 "
                     "C 262,336 180,332 136,312 Z",
                     fill=_SVG_BAND, stroke=_SVG_INK, w=2.5,
                     data_accessory="liver"))
    out.append(_ellipse(256, 350, 15, 20, fill=_SVG_BAND, stroke=_SVG_INK,
                        w=2.2, data_accessory="gall-bladder"))
    out.append(_path("M 150,380 C 196,368 268,370 316,382 "
                     "C 268,398 196,400 150,392 Z",
                     fill=_SVG_BAND, stroke=_SVG_INK, w=2.2,
                     data_accessory="pancreas"))

    # The ducts, in Design's two passes: every wall first, then every lumen,
    # so the four join into one without a seam where they cross.
    for slug, src, dst, d in _GUT_TUBE_DUCTS:
        out.append(_path(d, stroke=_SVG_INK, w=7, data_duct=slug,
                         data_duct_from=src, data_duct_to=dst,
                         data_duct_layer="wall"))
    for slug, src, dst, d in _GUT_TUBE_DUCTS:
        out.append(_path(d, stroke=_SVG_INSET, w=2.4, data_duct=slug,
                         data_duct_from=src, data_duct_to=dst,
                         data_duct_layer="lumen"))

    # ── the food's route, over everything ───────────────────────────────
    out.append(_path(_GUT_TUBE_FOOD, stroke=_SVG_ACCENT, w=3.6,
                     data_path="food"))
    out.append('</g>')

    # ── the organ names, outside the clip ───────────────────────────────
    out.append(_label(224, 286, "liver", size=16, weight="700",
                      data_accessory_label="liver"))
    out.append(_label(232, 356, "gall bladder", size=16, weight="700",
                      anchor="end", data_accessory_label="gall-bladder"))
    out.append(_label(224, 424, "pancreas", size=16, weight="700",
                      data_accessory_label="pancreas"))
    out.append(_mono(352, 440, "ducts in", size=13, weight="400"))

    # ── the seven badges, in position ───────────────────────────────────
    for num, organ, on_tube, leader, cx, cy in _GUT_TUBE_STOPS:
        out.append(_path(leader, stroke=_SVG_INK, w=1.4,
                         data_stop_leader=num))
        out.append(_circle(cx, cy, 14,
                           fill=_SVG_BAND if on_tube else _SVG_CARD,
                           stroke=_SVG_INK, w=2,
                           dash=None if on_tube else "5 4",
                           data_stop=num, data_organ=organ,
                           data_on_tube="1" if on_tube else "0"))
        out.append(_mono(cx, cy + 6, num, size=15, fill=_SVG_INK,
                         weight="400", anchor="middle",
                         data_stop_numeral=num))
        for nx, ny, s, anchor, muted in _GUT_TUBE_NOTES.get(num, ()):
            out.append(_mono(nx, ny, s, size=13, weight="400", anchor=anchor,
                             fill=_SVG_INK_MUTED if muted
                             else _SVG_ACCENT_TEXT))

    # ── the key ─────────────────────────────────────────────────────────
    out.append(_mono(24, 852, "SEVEN STOPS, IN ORDER", size=13, weight="400",
                     spacing="1.2"))
    out.append(_path("M 24,864 H 876", stroke=_SVG_RULE, w=2))
    for num, organ, on_tube, bx, tx, cy, title, body in _GUT_TUBE_KEY:
        out.append(_circle(bx, cy, 14,
                           fill=_SVG_BAND if on_tube else _SVG_CARD,
                           stroke=_SVG_INK, w=2,
                           dash=None if on_tube else "5 4",
                           data_key_stop=num, data_key_organ=organ))
        out.append(_mono(bx, cy + 6, num, size=15, fill=_SVG_INK,
                         weight="400", anchor="middle",
                         data_key_numeral=num))
        out.append(_label(tx, cy - 1, title, size=18, weight="700",
                          anchor="start", data_key_title=num))
        out.append(_label(tx, cy + 19, body, size=15, fill=_SVG_INK_BODY,
                          weight="400", anchor="start"))

    # ── the two legend lines: what the orange is, what the dashes are ───
    out.append(_path("M 24,1112 H 876", stroke=_SVG_RULE, w=2))

    out.append(_path("M 28,1146 h 30", stroke=_SVG_ACCENT, w=3.6,
                     data_legend="food-path"))
    out.append(_label(70, 1152, "One path, 01 to 07 — the food’s route",
                      size=16, weight="700", anchor="start",
                      data_legend_label="food-path"))
    out.append(_label(70, 1174, "It never enters 05.", size=15,
                      fill=_SVG_INK_BODY, weight="400", anchor="start"))

    out.append(_rect(480, 1134, 34, 26, rx=8, stroke=_SVG_INK, w=2, dash="8 6",
                     data_legend="accessory"))
    out.append(_label(524, 1152, "Alongside the tube, not part of it",
                      size=16, weight="700", anchor="start",
                      data_legend_label="accessory"))
    out.append(_label(524, 1174, "Ducts in. Nothing comes back out.", size=15,
                      fill=_SVG_INK_BODY, weight="400", anchor="start"))

    # ── the disclosure. Ruled in; its absence is a red gate ─────────────
    out.append(_mono(24, 1216,
                     "The coils are drawn as one run down the frame rather "
                     "than in their anatomical positions, so that", size=13,
                     weight="400", data_disclosure="1",
                     data_disclosure_line="1"))
    out.append(_mono(24, 1236,
                     "the order and the continuity read without one tube "
                     "crossing another.", size=13, weight="400",
                     data_disclosure="1", data_disclosure_line="2"))

    out.append('</g>')
    out.append('</svg>')
    return "".join(out)
# renderers: ═══ END B2 ═══

# renderers: ═══ BEGIN B3 ═══
# DISPATCH: "band-commit": ("ks3-plate-block", ' data-instrument data-plateblock data-stage-done="0"'),
#
# and in ACTIVITY_KIND_FN, beside the other B3 rows:
#     "band-commit":            r_band_commit,
#
# Place `r_band_commit` at the head of the B3 group (after the B2 rows,
# ~build_ks3.py 7056). Needs `e`, `t`, `rich`.
#
# ⚠️ THIS RENDERER DOES NOT CONSUME `options` OR `reveal`, and it must not
# start to. The block's controls are seven three-way band pickers, which are
# not answer buttons and are not `.ks3-option`; the activity authors neither
# key, so `_kinds_consuming()` correctly leaves both generic branches off.


def r_band_commit(a, act_id):
    """⊕ b3-01 `#s-plate` — commit all seven, then open all seven at once.

    ⚖️ THE GATE IS THE PEDAGOGY. Nothing opens until every one of the seven
    nutrients has been placed in a band, and the lede says why in as many
    words: *a guess you did not make cannot be wrong, and a guess that is never
    wrong teaches you nothing.* A per-row reveal — which is what `job-sort`
    does, and what this looks like from a distance — would let a student read
    row one's answer before committing on row two, and the whole argument of
    the block is that the SPREAD is the surprise. You cannot be surprised by a
    spread you were shown a seventh at a time.

    ⚖️ THE THREE-BRANCH VERDICT, and the branch that must not be dropped.
    NOTES-B3 §3.1 names it: a student who puts all seven in the same band gets
    a verdict that says so. That is the only place in the lesson where the
    target misconception — *balanced means equal amounts* — is read back to the
    student in their own answer rather than in the abstract. `verdicts` takes
    exactly three keys and this renderer raises without all three, because a
    missing branch is invisible: the block still works, it simply stops
    catching the one student it was built for.

    ⚠️ R3 / MRB-196 R10 — READ THIS BEFORE "TIDYING" THE MARKING.
    Nothing here is a `.ks3-option` and nothing takes a marking colour. The
    band buttons keep ONE chosen treatment whether the choice was right or
    wrong, before the reveal and after it; what changes on open is the ROW,
    which gains Design's own dark-ground selected treatment, and the row's why
    panel, which says "You had it" or "Actually tens of grams" in words. There
    is no `--ks3-ok`, no green, no drawn ✓ and no ✕ anywhere in this
    instrument. Design draws it exactly this way on the approved page and the
    distinction is real: the student is being told what the answer WAS, not
    being scored on having found it.

    ⚠️ EVERY TEXT RULE IN THE STYLESHEET IS SCOPED `.ks3-dark …`. This block is
    on ink on Design's page (`ks3-block ks3-dark ks3-practical`), `.ks3-dark p`
    is (0,1,1) and a bare `.ks3-plate-note` is (0,1,0) and loses. See the CSS.

    Emit-both-show-one throughout: all seven why panels, both band verdicts per
    row and all three closing branches are in the document, hidden, and the
    wiring only ever changes which is shown. No authored sentence is rebuilt in
    the browser, so the em dashes, the right single quotes and the `<em>`
    survive intact — and every one of these sentences is science.
    """
    bands = a.get("bands") or []
    if len(bands) < 2:
        raise ValueError(
            "band-commit %r offers %d band(s). The block asks a student to "
            "place a nutrient on a SCALE, and one band is not a scale."
            % (act_id, len(bands)))
    band_by_id = {}
    for i, b in enumerate(bands):
        for key in ("id", "label", "miss_label"):
            if not b.get(key):
                raise ValueError(
                    "band-commit %r band %d is missing %r. `miss_label` is the "
                    "sentence a student who missed this band reads back "
                    "(“Actually tens of grams”); composing it from "
                    "`label` in the browser would lower-case it there and put "
                    "an authored sentence inside the engine."
                    % (act_id, i, key))
        band_by_id[b["id"]] = b

    rows = a.get("rows") or []
    if not rows:
        raise ValueError("band-commit %r declares no rows[]." % act_id)
    for r in rows:
        for key in ("name", "hint", "band", "mass", "why"):
            if not r.get(key):
                raise ValueError(
                    "band-commit %r row %r is missing %r." % (act_id, r.get("name"), key))
        if r["band"] not in band_by_id:
            raise ValueError(
                "band-commit %r row %r sits in band %r, which is not one of "
                "%s. A row whose band no band offers can never be got right, "
                "and the verdict would be unreachable by construction."
                % (act_id, r["name"], r["band"], sorted(band_by_id)))

    verdicts = a.get("verdicts") or {}
    missing = sorted({"all_same", "close", "spread"} - set(verdicts))
    if missing:
        raise ValueError(
            "band-commit %r declares no %s verdict branch. All three are "
            "required: `all_same` is the only place the lesson's target "
            "misconception is named back to the student in their own answer, "
            "and a block that silently drops it still looks finished."
            % (act_id, ", ".join(missing)))

    hit_label = a.get("hit_label")
    if not hit_label:
        raise ValueError(
            "band-commit %r declares no `hit_label`." % act_id)

    row_html = []
    for i, r in enumerate(rows):
        band = band_by_id[r["band"]]
        picks = "".join(
            '<button type="button" class="ks3-plate-band" data-band="%s" '
            'aria-pressed="false">%s</button>' % (e(b["id"]), t(b["label"]))
            for b in bands)
        row_html.append(
            '<li class="ks3-plate-row" data-row="%d" data-answer="%s">'
            '<div class="ks3-plate-head">'
            '<p class="ks3-plate-name">%s</p>'
            '<p class="ks3-plate-hint">%s</p></div>'
            '<div class="ks3-plate-bands">%s</div>'
            '<div class="ks3-plate-why" hidden data-why>'
            '<p class="ks3-plate-real">'
            '<span data-real="hit" hidden>%s</span>'
            '<span data-real="miss" hidden>%s</span>'
            '<span class="ks3-plate-sep" aria-hidden="true"> · </span>'
            '<span class="ks3-plate-mass">%s</span></p>'
            '<p class="ks3-plate-note">%s</p></div></li>'
            % (i, e(r["band"]), t(r["name"]), t(r["hint"]), picks,
               t(hit_label), t(band["miss_label"]), t(r["mass"]),
               rich(r["why"])))

    # The three closing branches, all in the document and all hidden. `data-v`
    # is the branch name and nothing else — the sentences themselves never move
    # through an attribute.
    branches = "".join(
        '<p class="ks3-plate-vwhy" data-v="%s" hidden>%s</p>'
        % (e(k), rich(verdicts[k])) for k in ("all_same", "close", "spread"))

    return ('<div class="ks3-plate" data-plate data-total="%d">'
            '<ul class="ks3-plate-rows" role="list">%s</ul>'
            '<div class="ks3-plate-foot">'
            '<button type="button" class="ks3-reveal-btn ks3-plate-open" '
            'data-plate-open disabled aria-expanded="false">%s</button>'
            '<span class="ks3-plate-count" data-plate-count data-format="%s" '
            'data-done="%s">%s</span></div>'
            '<div class="ks3-plate-verdict" hidden data-plate-verdict>'
            '<p class="ks3-plate-vlabel">%s</p>'
            '<p class="ks3-plate-vhead" data-vhead data-format="%s" '
            'role="status"></p>%s</div></div>'
            % (len(rows), "".join(row_html),
               t(a.get("open_label") or "Show the real amounts"),
               e(a.get("commit_format") or "{n} of {total} committed"),
               e(a.get("commit_done") or "Opened"),
               t((a.get("commit_format") or "{n} of {total} committed")
                 .replace("{n}", "0").replace("{total}", str(len(rows)))),
               t(a.get("verdict_eyebrow") or "Your day, scored"),
               e(a.get("verdict_format") or "{n} of {total} in the right band."),
               branches))
# DISPATCH: "clinic-cases": ("ks3-clinic-block", ' data-instrument data-clinicblock data-stage-done="0"'),
#
# and in `ACTIVITY_KIND_FN`, beside the other B3 rows:
#     "clinic-cases":           r_clinic_cases,
#
# Place `r_clinic_cases` beside `r_settles_it` — it is CONTRAST's other
# flagship and shares the ruling that shapes it. Needs `e`, `t`, `rich` and
# `_self_check`, all of which build_ks3.py already defines.
#
# ⚠️ THIS RENDERER DOES NOT CONSUME `options`. The three imbalance buttons are
# a MULTI-SELECT and are authored as `kinds[]`, not as `options[]`, so
# `_KIND_FN_OWNS_OPTIONS` does not pick this kind up and must not: a lesson
# that ever authors a genuine single-answer `options` list beside this block
# still gets the generic list, which is correct. The `self_check` options are
# drawn by `_self_check` and are not `a["options"]` either.


def r_clinic_cases(a, act_id):
    """⊕ b3-04 `#s-cases` — five clinics, and two of them have two answers.

    ⚖️ THE MULTI-SELECT IS THE LESSON. Every other case instrument in the key
    stage asks for ONE answer per item — `job-sort`, `verdict-cards`,
    `sort-task`. This one asks the student to tick *every* imbalance that
    applies, and clinics 2 and 5 have two. NOTES-B3 §2 states the pedagogy in
    one line: "Refusing to tick two is the error being taught." Rendering this
    as a one-of-three picker would remove the only thing the block exists for,
    which is why it is not `verdict-cards` with three options.

    ⚖️ CLINIC 5 IS NOT A DIET PROBLEM AT ALL — an adequate plate and a
    shortened intestine — and it is deliberately inside a diet lesson, because
    it is the bridge into lessons 5 to 7. `min_multi` below refuses a payload
    in which no case carries more than one answer: a five-clinic set where
    every clinic has exactly one answer is a different exercise wearing this
    one's markup, and it would pass every other gate silently.

    ⚠️ MRB-196 R10, AND IT MOVES DESIGN'S COPY. Design computes whether the
    student's ticks matched exactly and spends it on the verdict LABEL —
    "You had it exactly" / "Two imbalances apply here" / "Not quite". Two of
    those three branches are the page marking an activity, which R3 forbids
    and R10 replaces with a self-check the student answers for themselves.

    The third branch is not a verdict on the student at all: "Two imbalances
    apply here" is a fact about the CASE. So it survives — as `verdict_label`,
    authored per case and shown to everyone identically. That also fixes a
    defect in Design's own logic, and it is the more serious half: a student
    who ticked BOTH answers on clinic 2 took the `exact` branch and therefore
    never saw the line telling them two imbalances apply. The page's own
    teaching sentence was shown only to the students who got it wrong.

    ⚠️ NOTHING MARKS. The pick buttons are `.ks3-clinic-pick`, not
    `.ks3-option`, so the reveal may disable them without failing R3's runtime
    assertion — the same construction `settles-it` uses for its two choice
    buttons. After the diagnosis the UNCHOSEN picks dim, which records what was
    spent and not whether it was right; nothing anywhere carries `data-correct`
    and nothing green or red appears on any control in this block.

    ⚠️ INK-DARK. `.ks3-dark p` is (0,1,1) and beats a bare instrument class at
    (0,1,0), so every colour rule in the stylesheet is scoped `.ks3-dark …`.
    On this block the intake line is the one that would visibly break: amber
    mono is how a student finds the number, and unscoped it falls to on-dark
    body copy and reads as another sentence of the description.

    Emit-all-show-one: five panels are in the document and one is shown. No
    authored sentence is ever rebuilt in JS from an attribute, so the em
    dashes, the right single quotes and the ⚠️-flagged tone of this lesson
    survive exactly as written.
    """
    cases = a.get("cases") or []
    kinds = a.get("kinds") or []
    if len(cases) < 2:
        raise ValueError(
            "clinic-cases %r declares %d case(s). The block is a run of "
            "judgements read against each other and one case is not a run."
            % (act_id, len(cases)))
    if len(kinds) < 2:
        raise ValueError(
            "clinic-cases %r offers %d kind(s) to tick. The whole exercise is "
            "choosing among them — and choosing more than one."
            % (act_id, len(kinds)))

    known = []
    for k in kinds:
        if not k.get("id") or not k.get("label"):
            raise ValueError(
                "clinic-cases %r kind %r needs both `id` and `label`."
                % (act_id, k))
        known.append(k["id"])

    multi = 0
    for c in cases:
        for key in ("id", "label", "description", "intake", "verdict_label",
                    "answer", "why"):
            if not c.get(key):
                raise ValueError(
                    "clinic-cases %r case %r is missing %r. Every one of the "
                    "seven is drawn, and an empty one renders as a gap in the "
                    "panel." % (act_id, c.get("id"), key))
        picks = c.get("kinds") or []
        if not picks:
            raise ValueError(
                "clinic-cases %r case %r names no correct kinds[]; a clinic "
                "with no answer cannot be diagnosed."
                % (act_id, c.get("id")))
        for p in picks:
            if p not in known:
                raise ValueError(
                    "clinic-cases %r case %r names kind %r, which is not one "
                    "of the %d offered: %s."
                    % (act_id, c["id"], p, len(known), ", ".join(known)))
        if len(picks) > 1:
            multi += 1

    # ⚖️ Build time only, and it never reaches the page. See the docstring:
    # a set in which nothing has two answers is a different exercise.
    if not multi:
        raise ValueError(
            "clinic-cases %r has no case with more than one correct kind. "
            "This instrument exists because refusing to tick two is the error "
            "being taught; with one answer everywhere it is a picker."
            % act_id)

    counts = a.get("count_labels") or {}
    for key in ("none", "some", "done"):
        if not counts.get(key):
            raise ValueError(
                "clinic-cases %r count_labels is missing %r. The readout has "
                "three states and a missing one renders as an empty span."
                % (act_id, key))
    if "{n}" not in counts["some"]:
        raise ValueError(
            "clinic-cases %r count_labels['some'] is %r and carries no {n}. "
            "It is the live one." % (act_id, counts["some"]))

    tabs = "".join(
        '<button type="button" class="ks3-sim-seg-btn ks3-clinic-tab" '
        'data-case="%s" aria-pressed="%s">%s</button>'
        % (e(c["id"]), "true" if i == 0 else "false",
           t(c.get("tab_label") or c["label"]))
        for i, c in enumerate(cases))

    panels = []
    for i, c in enumerate(cases):
        picks = "".join(
            '<button type="button" class="ks3-sim-seg-btn ks3-clinic-pick" '
            'data-kind="%s" aria-pressed="false">%s</button>'
            % (e(k["id"]), t(k["label"])) for k in kinds)
        panels.append(
            '<div class="ks3-clinic-panel" data-case="%s" data-open="0"%s>'
            '<div class="ks3-clinic-brief">'
            '<p class="ks3-clinic-label">%s</p>'
            '<p class="ks3-clinic-desc">%s</p>'
            '<p class="ks3-clinic-intake">%s</p></div>'
            '<p class="ks3-clinic-picklabel">%s</p>'
            '<div class="ks3-clinic-picks">%s</div>'
            '<div class="ks3-clinic-foot">'
            '<button type="button" class="ks3-reveal-btn ks3-clinic-reveal" '
            'data-clinic-reveal disabled>%s</button>'
            '<span class="ks3-clinic-count" data-clinic-count role="status" '
            'data-none="%s" data-some="%s" data-done="%s">%s</span></div>'
            '<div class="ks3-clinic-verdict" hidden data-reveal>'
            '<p class="ks3-clinic-verdict-label">%s</p>'
            '<p class="ks3-clinic-answer">%s</p>'
            '<p class="ks3-clinic-why">%s</p></div></div>'
            % (e(c["id"]), "" if i == 0 else " hidden",
               t(c["label"]), rich(c["description"]), t(c["intake"]),
               t(a.get("pick_label") or "Tick every imbalance that applies"),
               picks,
               t(a.get("reveal_label") or "Show the diagnosis"),
               e(counts["none"]), e(counts["some"]), e(counts["done"]),
               t(counts["none"]),
               t(c["verdict_label"]), rich(c["answer"]), rich(c["why"])))

    return ('<div class="ks3-clinic" data-clinic data-total="%d">'
            '<div class="ks3-clinic-tabs" role="list">%s</div>%s</div>%s'
            % (len(cases), tabs, "".join(panels), _self_check(a, act_id)))
# DISPATCH: "enzyme-run": ("ks3-erun-block", ' data-instrument data-erunblock data-stage-done="0"'),
#
# and in `ACTIVITY_KIND_FN`, beside the other B3 rows:
#     "enzyme-run":             r_enzyme_run,
#
# Place `r_enzyme_run` and `_erun_rate` beside `r_gut_journey`. Needs `e`, `t`,
# `rich` and `json`, all of which build_ks3.py already imports or defines.
#
# ⚠️ THE ONLY TIMER IN THE UNIT. NOTES-B3 §6 says so in as many words:
# "`enzyme-run` is the only one with a timer. Nothing else in the unit
# animates." That is why this is the one B3 fragment with a reduced-motion
# contract to honour, and why `reduced_motion_scale` is authored rather than
# assumed.


def _erun_rate(model, temp, ph, opt_ph):
    """The rate curve, as a fraction of maximum — Design's own model.

    ⚠️ `rateFor()` in `shared/ks3.js` is THIS FUNCTION, and the two must agree
    exactly. It exists in Python for one reason: the resting page has to print
    the same rate the first repaint computes, or the number visibly jumps on
    load and the shipped HTML — which is what a crawler and a reader with JS
    off get — carries a figure the instrument disagrees with. Same reason
    `heating-bench` duplicates its rounding rule.

    It is deliberately not a second MODEL: every constant comes from the
    authored `model` dict, so a corrected curve is one data edit and the two
    evaluations move together.
    """
    denature = float(model["denature_c"])
    if temp >= denature:
        return 0.0
    opt = float(model["optimum_c"])
    if temp <= opt:
        t_term = (temp / opt) ** float(model["rise_exponent"]) if opt else 0.0
    else:
        t_term = max(0.0, 1.0 - ((temp - opt) / float(model["fall_divisor"])) ** 2)
    # MRB-255 S4 — `opt_ph` IS A SET, not a scalar, and the gap is to the
    # NEAREST optimum in it. One protease with `opt_ph` 2 and a span of 4.5
    # put pepsin's optimum 6 units from pH 8, so protease in the small
    # intestine read 0% under a rule card saying "Best at pH 2 in the stomach,
    # 8 in the small intestine" — the bench denied the one pairing the lesson
    # most wants a student to try. Pepsin is ~2 and trypsin ~8; it is why the
    # lesson teaches the pancreatic alkali at all, and it is what AQA asks.
    # A scalar is still accepted and means a one-element set.
    opts = opt_ph if isinstance(opt_ph, (list, tuple)) else [opt_ph]
    if not opts:
        raise ValueError("enzyme-run: opt_ph is an empty set.")
    gap = min(abs(float(ph) - float(o)) for o in opts)
    p_term = max(0.0, 1.0 - gap / float(model["ph_span"]))
    return max(0.0, min(1.0, t_term * p_term))
def _erun_band(bands, denatured, temp, denature_c):
    """Which of the six temperature notes is showing, at rest.

    Same branch order as `noteFor()` in shared/ks3.js, for the same reason
    `_erun_rate` exists: the note on the shipped page must be the note the
    first repaint chooses.
    """
    if denatured and temp >= denature_c:
        return "denatured_hot"
    if denatured:
        return "denatured_cool"
    if temp >= bands["past_optimum"]:
        return "past_optimum"
    if temp >= bands["optimum"]:
        return "optimum"
    if temp >= bands["cold"]:
        return "cold"
    return "freezing"
def r_enzyme_run(a, act_id):
    """⊕ b3-06 `#s-bench` — three counters, and one of them never moves.

    ⚖️ THE THIRD COUNTER IS THE LESSON. NOTES-B3 §2 puts it in one line: "a
    running reaction with three counters, one of which never moves. That
    counter *is* the lesson." So the enzyme count is emitted as an authored
    STRING with a full-width bar and NO `data-value` and NO `data-bar` handle
    for the runtime to take hold of. It is the same construction as
    `heating-bench`'s mass tile, and for the same reason: the one number the
    prose says must not move is wired to nothing, so it cannot move even by
    accident.

    ⚖️ THE DENATURE LATCH IS THE OTHER HALF, and it is the misconception the
    block exists to kill. Heat past the threshold and the enzyme is finished;
    cooling does not bring it back, switching enzyme does not bring it back
    while the tube is still hot, and only a fresh tube clears it. The latch
    fires on the TEMPERATURE control rather than inside the run tick —
    NOTES-B3 flag 16 records that a student who dragged to 60 °C, read 0%, and
    dragged back to 37 °C used to be shown a full recovery, so the instrument
    built to kill the idea was demonstrating it.

    ⚠️ ONE THRESHOLD, AUTHORED ONCE. `model.denature_c` is quoted in the key
    fact, in two of the six temperature notes, in the key note, in a ladder
    correction and in the stretch layer. It reaches the runtime through
    `data-cfg` and the prose through the lesson record; there is exactly one
    number, and the module docstring lists every sentence that repeats it.

    ⚠️ EVERY BRANCHING SENTENCE IS IN THE DOCUMENT. Six temperature notes and
    three verdicts, all nine emitted, eight hidden — emit-all-show-one. None is
    assembled in JS from an attribute, so the em dashes, right single quotes
    and degree signs survive and a science correction is a data edit. Only two
    live numbers are ever substituted: the tick count and the rate percentage.

    ⊕ ADDED INSIDE A COMPONENT DESIGN DREW, where the page is silent. Design
    shows the verdict on `clock >= ticks || (everRan && !running && denatured)`.
    A run at a rate of exactly zero that is NOT denatured — stomach protease
    dropped into pH 8, which is one press of one button — finishes on its first
    tick and shows no verdict at all: the bench goes quiet and says nothing,
    and the "slow" verdict that exists to send the student back to the pH dial
    never appears. The wiring shows the verdict whenever a run has FINISHED,
    whatever finished it. Design's three branches are unchanged.

    ⚠️ INK-DARK. `.ks3-dark p` is (0,1,1) and beats a bare instrument class at
    (0,1,0), so every colour rule in the stylesheet is scoped `.ks3-dark …`.
    Here the rate readout and the temperature figure are what would visibly
    break: amber mono is how a student reads a dial, and unscoped they fall to
    on-dark body copy and stop looking like numbers.

    ⚑ FOR MIDE, recorded here as well as in the lesson module: the enzyme
    counter's bar is `--ks3-ok`. That token's own comment in `tokens.css`
    reserves green for the ladder marking correctness, and this is a bar
    meaning "unchanged" on a block that marks nothing. Design drew it; it is
    reproduced as drawn and registered in a parity row, so the day the palette
    question is ruled the gate says exactly where the value lives. Same
    handling as `scale-cards`' amber distance label.
    """
    enzymes = a.get("enzymes") or []
    phs = a.get("phs") or []
    if len(enzymes) < 2:
        raise ValueError(
            "enzyme-run %r declares %d enzyme(s). One cannot show that each "
            "has its own substrate and its own best pH." % (act_id, len(enzymes)))
    if len(phs) < 2:
        raise ValueError(
            "enzyme-run %r offers %d pH setting(s); the pH dial is half the "
            "bench." % (act_id, len(phs)))

    for z in enzymes:
        missing = [k for k in ("id", "label", "equation", "counter_substrate",
                               "counter_product") if not z.get(k)]
        if missing:
            raise ValueError(
                "enzyme-run %r enzyme %r is missing %s. The counter names are "
                "authored per enzyme rather than built from a substrate word, "
                "because 'Fatty acids and glycerol made' is a sentence and not "
                "a capitalisation." % (act_id, z.get("id"), ", ".join(missing)))
        if z.get("opt_ph") is None:
            raise ValueError(
                "enzyme-run %r enzyme %r declares no opt_ph; the pH term is "
                "the gap to it." % (act_id, z["id"]))

    for p in phs:
        if p.get("value") is None or not p.get("label"):
            raise ValueError(
                "enzyme-run %r pH setting %r needs both `value` and `label`."
                % (act_id, p))

    model = a.get("model") or {}
    for key in ("denature_c", "optimum_c", "rise_exponent", "fall_divisor",
                "ph_span"):
        if model.get(key) is None:
            raise ValueError(
                "enzyme-run %r model is missing %r. The curve is a simplified "
                "model and all five constants are authored, so the legal line "
                "can say so truthfully." % (act_id, key))

    run = a.get("run") or {}
    for key in ("ticks", "tick_ms", "units_per_tick", "start_substrate",
                "reduced_motion_scale", "slow_below_pct"):
        if run.get(key) is None:
            raise ValueError("enzyme-run %r run is missing %r." % (act_id, key))
    labels = run.get("labels") or {}
    for key in ("start", "more", "running", "reset", "clock", "clock_fresh",
                "rate"):
        if not labels.get(key):
            raise ValueError(
                "enzyme-run %r run.labels is missing %r." % (act_id, key))
    if "{n}" not in labels["clock"] or "{total}" not in labels["clock"]:
        raise ValueError(
            "enzyme-run %r run.labels['clock'] is %r; it carries both live "
            "numbers and needs {n} and {total}." % (act_id, labels["clock"]))
    if "{pct}" not in labels["rate"]:
        raise ValueError(
            "enzyme-run %r run.labels['rate'] is %r and carries no {pct}."
            % (act_id, labels["rate"]))

    units = a.get("units_format")
    if not units or "{n}" not in units:
        raise ValueError(
            "enzyme-run %r units_format is %r; the counter values are authored "
            "copy and carry the live count as {n}." % (act_id, units))
    if not a.get("enzyme_counter_label") or not a.get("enzyme_counter_value"):
        raise ValueError(
            "enzyme-run %r needs enzyme_counter_label and "
            "enzyme_counter_value. The third counter's value is a CONSTANT "
            "string — it is the one readout nothing may compute." % act_id)

    # ⚠️ SIX BRANCHES, ALL NAMED. The wiring chooses among these keys and
    # nothing else; a missing one leaves the note blank at exactly the
    # temperature the student dragged to.
    notes = a.get("temp_notes") or {}
    for key in ("denatured_hot", "denatured_cool", "past_optimum", "optimum",
                "cold", "freezing"):
        if not notes.get(key):
            raise ValueError(
                "enzyme-run %r temp_notes is missing %r. Both denatured "
                "branches are required and they say different things: "
                "'cool it, then take a fresh tube' has to be distinguishable "
                "from 'cooling changes nothing'." % (act_id, key))
    bands = a.get("temp_bands") or {}
    for key in ("past_optimum", "optimum", "cold"):
        if bands.get(key) is None:
            raise ValueError(
                "enzyme-run %r temp_bands is missing %r." % (act_id, key))

    verdicts = a.get("verdicts") or {}
    # MRB-257 (5.7) — `nothing` is REQUIRED, not optional. Without it the
    # engine falls back to Design's three and prints "A little product,
    # slowly." over `Rate 0%` and `0 units made`. A future enzyme bench must
    # not be able to ship without the branch that says nothing happened.
    for key in ("denatured", "nothing", "slow", "worked"):
        if not verdicts.get(key):
            raise ValueError(
                "enzyme-run %r verdicts is missing %r. Four branches are "
                "drawn: the denatured one is the block's whole argument and "
                "`nothing` is the one that stops a run which produced zero "
                "units being described as having produced a little (5.7)."
                % (act_id, key))

    groups = a.get("group_labels") or {}
    for key in ("enzyme", "ph", "temp"):
        if not groups.get(key):
            raise ValueError(
                "enzyme-run %r group_labels is missing %r." % (act_id, key))

    temp = a.get("temp") or {}
    for key in ("min", "max", "start", "step", "format", "field_label"):
        if temp.get(key) is None:
            raise ValueError("enzyme-run %r temp is missing %r." % (act_id, key))
    if "{t}" not in temp["format"]:
        raise ValueError(
            "enzyme-run %r temp['format'] is %r and carries no {t}."
            % (act_id, temp["format"]))

    start_ph = a.get("start_ph", phs[0]["value"])
    if start_ph not in [p["value"] for p in phs]:
        raise ValueError(
            "enzyme-run %r opens at pH %r, which is not one of the %d offered."
            % (act_id, start_ph, len(phs)))

    cfg = {
        "denature_c": model["denature_c"],
        "optimum_c": model["optimum_c"],
        "rise_exponent": model["rise_exponent"],
        "fall_divisor": model["fall_divisor"],
        "ph_span": model["ph_span"],
        "ticks": run["ticks"],
        "tick_ms": run["tick_ms"],
        "units_per_tick": run["units_per_tick"],
        "start_substrate": run["start_substrate"],
        "reduced_motion_scale": run["reduced_motion_scale"],
        "slow_below_pct": run["slow_below_pct"],
        "temp_format": temp["format"],
        "units_format": units,
        "bands": {"past_optimum": bands["past_optimum"],
                  "optimum": bands["optimum"], "cold": bands["cold"]},
        "labels": dict(labels),
        "opt_ph": {z["id"]: z["opt_ph"] for z in enzymes},
    }

    # The resting readouts, from the same constants the runtime uses.
    rest_rate = int(round(_erun_rate(model, float(temp["start"]), start_ph,
                                     enzymes[0]["opt_ph"]) * 100))
    rest_note = _erun_band(bands, False, float(temp["start"]),
                           float(model["denature_c"]))
    field = "erun-temp-%s" % act_id

    ztabs = "".join(
        '<button type="button" class="ks3-sim-seg-btn ks3-erun-enzyme" '
        'data-enzyme="%s" aria-pressed="%s">%s</button>'
        % (e(z["id"]), "true" if i == 0 else "false", t(z["label"]))
        for i, z in enumerate(enzymes))

    ptabs = "".join(
        '<button type="button" class="ks3-sim-seg-btn ks3-erun-ph" '
        'data-ph="%s" aria-pressed="%s">%s</button>'
        % (e(p["value"]), "true" if p["value"] == start_ph else "false",
           t(p["label"]))
        for p in phs)

    # One equation per enzyme, all in the document. `t()` DRAWS the arrow:
    # U+2192 is absent from all five latin woff2 subsets, and typed as a
    # character it drops to a system font mid-line.
    equations = "".join(
        '<span class="ks3-erun-equation" data-enzyme="%s"%s>%s</span>'
        % (e(z["id"]), "" if i == 0 else " hidden", t(z["equation"]))
        for i, z in enumerate(enzymes))

    def names(key):
        return "".join(
            '<span class="ks3-erun-countername" data-enzyme="%s"%s>%s</span>'
            % (e(z["id"]), "" if i == 0 else " hidden", t(z[key]))
            for i, z in enumerate(enzymes))

    counters = (
        '<li class="ks3-erun-counter" data-counter="substrate">'
        '<div class="ks3-erun-counterhead">'
        '<p class="ks3-erun-counterlabel">%s</p>'
        '<p class="ks3-erun-countervalue" data-value="substrate">%s</p></div>'
        '<span class="ks3-erun-track">'
        '<span class="ks3-erun-bar" data-bar="substrate" style="width:100%%">'
        '</span></span></li>'
        '<li class="ks3-erun-counter" data-counter="product">'
        '<div class="ks3-erun-counterhead">'
        '<p class="ks3-erun-counterlabel">%s</p>'
        '<p class="ks3-erun-countervalue" data-value="product">%s</p></div>'
        '<span class="ks3-erun-track">'
        '<span class="ks3-erun-bar" data-bar="product" style="width:0%%">'
        '</span></span></li>'
        # ⚖️ NO HANDLE. No `data-value`, no `data-bar` — the counter the prose
        # says must not move has nothing for the runtime to take hold of.
        '<li class="ks3-erun-counter" data-counter="enzyme">'
        '<div class="ks3-erun-counterhead">'
        '<p class="ks3-erun-counterlabel">%s</p>'
        '<p class="ks3-erun-countervalue">%s</p></div>'
        '<span class="ks3-erun-track">'
        '<span class="ks3-erun-bar ks3-erun-bar-fixed" style="width:100%%">'
        '</span></span></li>'
        % (names("counter_substrate"),
           t(units.replace("{n}", str(run["start_substrate"]))),
           names("counter_product"), t(units.replace("{n}", "0")),
           t(a["enzyme_counter_label"]), t(a["enzyme_counter_value"])))

    tnotes = "".join(
        '<span class="ks3-erun-tempnote" data-note="%s"%s>%s</span>'
        % (key, "" if key == rest_note else " hidden", rich(notes[key]))
        for key in ("denatured_hot", "denatured_cool", "past_optimum",
                    "optimum", "cold", "freezing"))

    vnotes = "".join(
        '<span class="ks3-erun-verdicttext" data-verdict="%s" hidden>%s</span>'
        % (key, rich(verdicts[key]))
        # MRB-257 (5.7) — `nothing` between `denatured` and `slow`, matching
        # `verdictFor()`'s branch order in shared/ks3.js. The engine tests
        # `hasVerdict("nothing")` before it uses the branch, so this span
        # existing IS what turns the fix on.
        for key in ("denatured", "nothing", "slow", "worked"))

    return ('<div class="ks3-erun" data-erun data-cfg="%s">'
            '<div class="ks3-erun-dials">'
            '<div class="ks3-erun-dial"><p class="ks3-erun-diallabel">%s</p>'
            '<div class="ks3-erun-seg">%s</div></div>'
            '<div class="ks3-erun-dial"><p class="ks3-erun-diallabel">%s</p>'
            '<div class="ks3-erun-seg">%s</div></div></div>'

            '<div class="ks3-erun-temp">'
            '<div class="ks3-erun-temphead">'
            '<p class="ks3-erun-diallabel">%s</p>'
            '<p class="ks3-erun-tempvalue" data-temp-value>%s</p></div>'
            '<label class="ks3-erun-srlabel" for="%s">%s</label>'
            '<input class="ks3-erun-slider" type="range" id="%s" min="%s" '
            'max="%s" step="%s" value="%s" data-temp aria-valuetext="%s">'
            '<p class="ks3-erun-tempnotes" data-tempnotes role="status">%s</p>'
            '</div>'

            '<div class="ks3-erun-tube">'
            '<div class="ks3-erun-tubehead">'
            '<p class="ks3-erun-reaction">%s</p>'
            '<p class="ks3-erun-rate" data-rate>%s</p></div>'
            '<ul class="ks3-erun-counters" role="list">%s</ul>'
            '<div class="ks3-erun-controls">'
            '<button type="button" class="ks3-reveal-btn ks3-erun-run" '
            'data-run>%s</button>'
            '<button type="button" class="ks3-reveal-btn ks3-erun-reset" '
            'data-reset>%s</button>'
            '<span class="ks3-erun-clock" data-clock>%s</span></div>'
            '<p class="ks3-erun-verdict" hidden data-reveal>%s</p>'
            '</div></div>'
            % (e(json.dumps(cfg, sort_keys=True)),
               t(groups["enzyme"]), ztabs, t(groups["ph"]), ptabs,
               t(groups["temp"]),
               t(temp["format"].replace("{t}", str(temp["start"]))),
               e(field), t(temp["field_label"]), e(field),
               e(temp["min"]), e(temp["max"]), e(temp["step"]),
               e(temp["start"]),
               e(temp["format"].replace("{t}", str(temp["start"]))),
               tnotes, equations,
               t(labels["rate"].replace("{pct}", str(rest_rate))),
               counters, t(labels["start"]), t(labels["reset"]),
               t(labels["clock_fresh"]), vnotes))
# DISPATCH: "fold-builder": ("ks3-fold-block", ' data-instrument data-foldblock data-stage-done="0"'),
#
# and in ACTIVITY_KIND_FN, beside the other B3 rows:
#     "fold-builder":           r_fold_builder,
#
# Place `r_fold_builder` in the B3 group, after `r_enzyme_run`. Needs `e`, `t`,
# `rich` — and nothing else; there is no canvas, no timer and no third-party
# anything in this instrument.
#
# ⚠️ THIS RENDERER DOES NOT CONSUME `options` OR `reveal`. Its controls are
# three state toggles, which are not answer buttons and are not `.ks3-option`;
# the activity authors neither key, so `_kinds_consuming()` correctly leaves
# both generic branches off. Do not start reading `options` here — the block
# has no question in it and R3 would have nowhere to stand.


def _fold_area_text(value):
    """Design's own three-branch number format, for the RESTING render only.

    `wireFoldBuilder` carries the same four lines and recomputes on every
    toggle. Two copies is a real cost and it buys the thing `head_counter`'s
    `start` buys one level up: the HTML that ships already says `0.50 m²`, so a
    crawler, a reader with JS off and anything that quotes the page all get the
    number the page means rather than a placeholder or an empty element.

    ⚠️ `int(v + 0.5)` and NOT `round()`. Python rounds half to even and
    JavaScript's `Math.round` rounds half up, so `round(10.5)` is 10 here and
    11 there — a divergence that would be invisible at rest (0 levels reads
    0.50 either way) and visible the moment someone reused this helper for a
    driven state. The two implementations agree by construction instead.
    Areas and multiples are positive by construction, so truncation after the
    half-add is a floor, and `math` does not have to be imported for it.
    """
    if value < 1:
        return "%.2f" % value
    if value < 10:
        return "%.1f" % value
    return "%d" % int(value + 0.5)
def _fold_multiple_text(ratio):
    """The same rule at one decimal below ten, whole numbers above."""
    if ratio < 10:
        return "%.1f" % ratio
    return "%d" % int(ratio + 0.5)
def _fold_factor_text(factor):
    """A level's multiplier as it is printed on its own button face.

    Whole numbers print whole — Design's `'On · ×' + l.factor` on an integer
    factor gives `×3`, and `×3.0` would read as a measured quantity rather
    than as the count of times the sheet was folded.
    """
    return ("%d" % factor) if float(factor).is_integer() else ("%g" % factor)
def r_fold_builder(a, act_id):
    """⊕ b3-07 `#s-fold` — build the surface up, one folding level at a time.

    ⚖️ THE MODEL IS BUILT UP, NOT BROKEN DOWN, and that is the family. B3's
    other switch instrument (`job-switch`, b3-08) starts with everything
    working and takes things away; this one starts with a plain tube and adds.
    Same control, opposite direction, and the direction is the lesson: the
    student watches half a square metre become thirty while the length written
    beside it never moves.

    ⚖️ THE LENGTH NEVER CHANGES, AND THE COPY SAYS SO AT EVERY STEP. All four
    notes are authored (NOTES-B3 §3.5) and three of them name the six metres
    again. That repetition is the whole confrontation of `#s-think` — *"Villi
    make the intestine longer"* — done with a number instead of a sentence, so
    it is not something to tidy out of the payload.

    ⚠️ THE NOTES ARE INDEXED BY **HOW MANY** LEVELS ARE ON, NOT BY WHICH.
    Four strings, one per count, exactly as NOTES-B3 §3.5 specifies. A note per
    level would be three strings and would have nothing to say about the plain
    tube, which is the state the whole comparison is measured from.

    ⚠️ NOTHING MARKS. There is no right answer here and no `answer_index` to
    check: a level is on or off and both are legitimate places to stand. The
    three toggles are `aria-pressed` toggle buttons and are deliberately NOT
    `.ks3-option`, so no R3 gate has to make an exception for them.

    ⚠️ INK-DARK. `.ks3-dark p` is (0,1,1) and beats a bare instrument class at
    (0,1,0), so every text rule in the stylesheet is scoped to at least
    (0,2,0). See the CSS; the readout note is the row that would ship broken.

    Emit-both-show-one: all four notes are in the document, three hidden, and
    `wireFoldBuilder` swaps which is shown. No authored sentence is ever
    rebuilt in JS from an attribute — only the two NUMBERS are, which is what
    an arithmetic readout is for.
    """
    levels = a.get("levels") or []
    if len(levels) < 2:
        raise ValueError(
            "fold-builder %r declares %d level(s). The block's argument is "
            "that folding COMPOUNDS — folds on folds on folds — and one "
            "multiplier is not a compounding." % (act_id, len(levels)))

    base = a.get("base_area")
    if not isinstance(base, (int, float)) or isinstance(base, bool) or base <= 0:
        raise ValueError(
            "fold-builder %r needs a positive `base_area` — every number the "
            "block prints is a multiple of it." % act_id)

    for l in levels:
        for key in ("id", "name", "factor", "what", "scale"):
            if not l.get(key):
                raise ValueError(
                    "fold-builder %r level %r is missing %r. `scale` is not "
                    "optional: it is what tells a student that the three "
                    "levels are three different SIZES of the same trick, and "
                    "without it they read as three unrelated facts."
                    % (act_id, l.get("id") or l.get("name"), key))
        if not isinstance(l["factor"], (int, float)) or isinstance(l["factor"], bool):
            raise ValueError(
                "fold-builder %r level %r has factor %r, which is not a "
                "number." % (act_id, l["id"], l["factor"]))

    notes = a.get("notes") or []
    if len(notes) != len(levels) + 1:
        raise ValueError(
            "fold-builder %r declares %d note(s) for %d level(s); it needs "
            "%d — one per COUNT, including the plain tube at zero. A missing "
            "note is a state the instrument can reach with nothing to say "
            "about it." % (act_id, len(notes), len(levels), len(levels) + 1))

    # ── MRB-257 (5.18) · EVERY REACHABLE STATE HAS SOMETHING TRUE TO SAY ──
    # The note used to be chosen by HOW MANY levels are on. With three
    # independent toggles there are 2³ = 8 states and only 4 of them are
    # prefixes of the document order, so the other four printed a sentence
    # about a level that was switched off — villi-only said "Corrugating the
    # wall triples it", which is the folds.
    #
    # The gate is stated over the STATE SPACE, not over the note count: walk
    # all 2ⁿ subsets and require each to resolve, either to an authored set
    # note or — only when the subset is the first `k` levels in document
    # order — to the cumulative note for k. Asserting "n set notes exist"
    # would pass while leaving a state unresolved, which is the shape of
    # assertion this whole run exists to stop.
    set_notes = a.get("set_notes") or {}
    ids = [l["id"] for l in levels]
    unresolved, unused = [], set(set_notes)
    for mask in range(1 << len(ids)):
        on_ids = [ids[i] for i in range(len(ids)) if mask & (1 << i)]
        key = "+".join(on_ids)
        if key in set_notes:
            unused.discard(key)
            continue
        # a prefix state falls back to the cumulative note for its count
        if on_ids == ids[:len(on_ids)]:
            continue
        unresolved.append(key or "(none on)")
    if unresolved:
        raise ValueError(
            "fold-builder %r can reach %d state(s) with nothing true to say: "
            "%s. The cumulative `notes` are indexed by COUNT and are true "
            "only of the prefix states; every other combination needs a "
            "`set_notes` entry keyed by the '+'-joined ids of the levels that "
            "are on, in document order (5.18)."
            % (act_id, len(unresolved), ", ".join(sorted(unresolved))))
    if unused:
        raise ValueError(
            "fold-builder %r has `set_notes` key(s) no state can reach: %s. "
            "Keys are the '+'-joined level ids in DOCUMENT order."
            % (act_id, ", ".join(sorted(unused))))

    labels = a.get("labels") or {}
    off_label = labels.get("off")
    on_label = labels.get("on")
    if not off_label or not on_label:
        raise ValueError(
            "fold-builder %r needs `labels.off` and `labels.on` — the button "
            "face is the only thing that says what pressing it will do."
            % act_id)

    rows = []
    for l in levels:
        # `{factor}` is filled HERE rather than in JS, so the button carries
        # its two finished labels and the runtime only swaps between them.
        # Design writes `'On · ×' + l.factor`; the multiplication
        # sign is U+00D7 and IS in the five latin subsets (unlike → ✓ ✕), so
        # it is typed rather than drawn.
        lit = on_label.replace("{factor}", _fold_factor_text(l["factor"]))
        rows.append(
            '<li class="ks3-fold-level" data-level="%s" data-factor="%s" '
            'data-on="0">'
            '<div class="ks3-fold-levelmain">'
            '<div class="ks3-fold-levelwhat">'
            '<p class="ks3-fold-name">%s</p>'
            '<p class="ks3-fold-what">%s</p>'
            '<p class="ks3-fold-scale">%s</p></div>'
            '<button type="button" class="ks3-fold-toggle" data-fold-toggle '
            'aria-pressed="false" data-label-on="%s" data-label-off="%s">%s'
            '</button></div></li>'
            % (e(l["id"]), e(l["factor"]), t(l["name"]), rich(l["what"]),
               t(l["scale"]), e(lit), e(off_label), t(off_label)))

    # Emit-all-show-one. Index 0 is the plain tube and is the one shown.
    # ⚠️ The cumulative notes must NOT carry `data-note-set`: `wireFoldBuilder`
    # distinguishes the two families by that attribute's presence, and a
    # cumulative note wearing one would be picked for a state it is false of.
    note_html = "".join(
        '<p class="ks3-fold-note" data-note="%d"%s>%s</p>'
        % (i, "" if i == 0 else " hidden", rich(n))
        for i, n in enumerate(notes))
    note_html += "".join(
        '<p class="ks3-fold-note" data-note-set="%s" hidden>%s</p>'
        % (e(k), rich(set_notes[k])) for k in sorted(set_notes))

    area_format = a.get("area_format") or "{a}"
    multiple_format = a.get("multiple_format") or "{x}"
    if "{a}" not in area_format:
        raise ValueError(
            "fold-builder %r `area_format` %r has no {a} placeholder, so the "
            "area would never be printed." % (act_id, area_format))
    if "{x}" not in multiple_format:
        raise ValueError(
            "fold-builder %r `multiple_format` %r has no {x} placeholder."
            % (act_id, multiple_format))

    # The resting values, computed here so the shipped HTML is already right.
    total = base
    for l in levels:
        total *= l["factor"]
    rest_width = max(2.0, (base / total) * 100.0)

    return ('<div class="ks3-fold" data-fold data-base="%s" '
            'data-area-format="%s" data-multiple-format="%s">'
            '<ul class="ks3-fold-levels" role="list">%s</ul>'
            '<div class="ks3-fold-readout">'
            '<div class="ks3-fold-readhead">'
            '<p class="ks3-fold-readlabel">%s</p>'
            '<p class="ks3-fold-area" data-fold-area>%s</p></div>'
            '<span class="ks3-fold-track">'
            '<span class="ks3-fold-bar" data-fold-bar data-full="0" '
            'style="width:%.1f%%"></span></span>'
            # ⚠️ `role="status"` on the NOTE, never on the instrument root. A
            # live region wrapping the whole block would re-announce three
            # level descriptions and a bar every time a toggle moved.
            '<div class="ks3-fold-noteline" role="status">%s</div>'
            '<p class="ks3-fold-multiple" data-fold-multiple>%s</p>'
            '</div></div>'
            % (e(base), e(area_format), e(multiple_format), "".join(rows),
               t(a.get("readout_label") or ""),
               t(area_format.replace("{a}", _fold_area_text(base))),
               rest_width, note_html,
               t(multiple_format.replace("{x}", _fold_multiple_text(1.0)))))
# DISPATCH: "gut-journey": ("ks3-gut-block", ' data-instrument data-gutblock data-stage-done="0"'),
#
# and in `ACTIVITY_KIND_FN`, beside the other B3 rows:
#     "gut-journey":            r_gut_journey,
#
# Place `r_gut_journey` beside `r_clinic_cases`. Needs `e`, `t` and `rich`.
#
# ⚠️ THE THREE TILE LABELS AND THE NOTE LABEL ARE AUTHORED, not literals here.
# They are student-facing copy ("Molecules broken here", "Worth knowing:") and
# the same argument that keeps a reveal's sentences out of the engine keeps
# these out of it: a label that lives in Python cannot be corrected by the
# person who owns the science.


def r_gut_journey(a, act_id):
    """⊕ b3-05 `#s-journey` — seven stops, and a time chart that argues.

    ⚖️ THE CHART IS THE ARGUMENT, NOT A DECORATION, and it is why this is not
    `job-sort`, `verdict-cards` or the board. Those are runs of judgements;
    this is one journey with a quantity attached to each leg, and the quantity
    contradicts the intuition — the stomach, which every student names first,
    holds the meal about four hours, and the small intestine holds it sixteen.
    A tabbed panel set with no chart under it would teach the seven organs and
    lose the only thing the lesson is built to overturn.

    ⚖️ EVERY BAR COMES OUT OF `hours`, AT BUILD TIME. The widths are a pure
    function of the authored numbers against the longest of them, so the bar
    and the printed figure beside it cannot disagree — Design's page computes
    the width in one place and the printed string in another, from the same
    field, which is two chances for one number. Nothing in the wiring builds a
    width; the runtime moves the HIGHLIGHT and nothing else.

    ⚠️ `chart_name` AND `chart_hours` ARE AUTHORED, and Design derives both.
    Its chart name is `label.split(',')[0]` — which turns "Pancreas, liver,
    gall bladder" into "Pancreas" and would silently truncate any future stop
    whose label carries a comma for a different reason. Its hours string is a
    three-branch expression (`0 → '—'`, `<1 → '<1 h'`, else `n + ' h'`), which
    is a sentence about the data assembled in JS. Both are strings a student
    reads; both are authored once, here, where the science owner can see them.

    ⚠️ INK-DARK. `.ks3-dark p` is (0,1,1) and beats a bare instrument class at
    (0,1,0), so every colour rule in the stylesheet is scoped `.ks3-dark …`.
    The tiles are what would visibly break: three labels and three values in
    one undifferentiated on-dark body colour is a panel that has lost its
    structure, and it looks tidy.

    Emit-all-show-one: seven stop panels are in the document and one is shown.
    Going back to a stop finds it exactly as it was, no state lives anywhere
    but the DOM, and none of the fourteen authored sentences — several of which
    carry em dashes, a right single quote and a superscript ² — is ever rebuilt
    in JS from an attribute.
    """
    stops = a.get("stops") or []
    if len(stops) < 2:
        raise ValueError(
            "gut-journey %r declares %d stop(s). The block is a journey and "
            "one stop is a destination." % (act_id, len(stops)))

    tiles = a.get("tile_labels") or {}
    for key in ("time", "breaks", "absorbs"):
        if not tiles.get(key):
            raise ValueError(
                "gut-journey %r tile_labels is missing %r. All three tiles are "
                "drawn on every stop and an unlabelled one renders as a bare "
                "value with nothing saying what it is." % (act_id, key))

    chart = a.get("chart") or {}
    for key in ("label", "close"):
        if not chart.get(key):
            raise ValueError(
                "gut-journey %r chart is missing %r. Without the closing line "
                "the chart is seven bars and no argument." % (act_id, key))

    for s in stops:
        missing = [k for k in ("id", "label", "name", "kind", "time", "breaks",
                               "absorbs", "what", "note", "chart_name",
                               "chart_hours")
                   if not s.get(k)]
        if missing:
            raise ValueError(
                "gut-journey %r stop %r is missing %s. Every one is drawn, and "
                "an empty one renders as a gap in the panel."
                % (act_id, s.get("id"), ", ".join(missing)))
        if "hours" not in s:
            raise ValueError(
                "gut-journey %r stop %r declares no `hours`. The bar widths "
                "are derived from it; a stop with none has no place on the "
                "chart the block is built around." % (act_id, s["id"]))

    # ⚖️ ONE scale for all seven, taken from the data rather than authored, so
    # a corrected transit time re-scales the whole chart in one edit.
    longest = max(float(s["hours"]) for s in stops) or 1.0

    tabs = "".join(
        '<li><button type="button" class="ks3-gut-tab" data-stop="%s" '
        'aria-pressed="%s">'
        '<span class="ks3-gut-tabnum">%s</span>'
        '<span class="ks3-gut-tablabel">%s</span></button></li>'
        % (e(s["id"]), "true" if i == 0 else "false",
           t("%02d" % (i + 1)), t(s["label"]))
        for i, s in enumerate(stops))

    panels = []
    for i, s in enumerate(stops):
        cells = "".join(
            '<div class="ks3-gut-tile" data-tile="%s">'
            '<p class="ks3-gut-tilelabel">%s</p>'
            '<p class="ks3-gut-tilevalue">%s</p></div>'
            % (key, t(tiles[key]), t(s[val]))
            for key, val in (("time", "time"), ("breaks", "breaks"),
                             ("absorbs", "absorbs")))
        panels.append(
            '<div class="ks3-gut-stop" data-stop="%s"%s>'
            '<div class="ks3-gut-stophead" role="status">'
            '<p class="ks3-gut-name">%s</p>'
            '<p class="ks3-gut-kind">%s</p></div>'
            '<p class="ks3-gut-what">%s</p>'
            '<div class="ks3-gut-tiles">%s</div>'
            '<p class="ks3-gut-note"><strong>%s</strong> %s</p></div>'
            % (e(s["id"]), "" if i == 0 else " hidden",
               t(s["name"]), t(s["kind"]), rich(s["what"]), cells,
               t(a.get("note_label") or "Worth knowing:"), rich(s["note"])))

    rows = "".join(
        '<li class="ks3-gut-row" data-stop="%s"%s>'
        '<span class="ks3-gut-rowname">%s</span>'
        '<span class="ks3-gut-track">'
        '<span class="ks3-gut-bar" style="width:%s%%"></span></span>'
        '<span class="ks3-gut-rowhours">%s</span></li>'
        % (e(s["id"]), ' data-lit="1"' if i == 0 else "",
           t(s["chart_name"]),
           ("%.1f" % (float(s["hours"]) / longest * 100)),
           t(s["chart_hours"]))
        for i, s in enumerate(stops))

    return ('<div class="ks3-gut" data-gut data-total="%d">'
            '<ol class="ks3-gut-tabs">%s</ol>'
            '<div class="ks3-gut-stops">%s</div>'
            '<div class="ks3-gut-chart">'
            '<p class="ks3-gut-chartlabel">%s</p>'
            '<ul class="ks3-gut-rows">%s</ul>'
            '<p class="ks3-gut-chartclose">%s</p></div></div>'
            % (len(stops), tabs, "".join(panels),
               t(chart["label"]), rows, rich(chart["close"])))
# DISPATCH: "job-switch": ("ks3-jobsw-block", ' data-instrument data-jobswblock data-stage-done="0"'),
#
# and in ACTIVITY_KIND_FN, beside the other B3 rows:
#     "job-switch":             r_job_switch,
#
# Place `r_job_switch` in the B3 group, after `r_fold_builder`. Needs `e`, `t`,
# `rich`.
#
# ⚠️ THIS RENDERER DOES NOT CONSUME `options` OR `reveal`. Its controls are
# five state toggles, not answer buttons; the activity authors neither key, so
# `_kinds_consuming()` correctly leaves both generic branches off.
#
# ── WHY THIS IS NOT A WIDENING OF `system-switch` OR `job-sort` ──────────
#
# NOTES-B3 §3.6 describes it as "the B2 `system-switch` shape with five rows
# and no prediction gate", and that reading was tested against both shipped
# components before a new kind was written. It does not hold, on four measured
# counts, and the fourth is on its own decisive:
#
#   1. `system-switch` is TABBED — one panel visible, chosen by
#      `.ks3-switch-tab`. Here all five rows are on screen at once, because
#      the payoff is a claim about all five TOGETHER and a student cannot see
#      five simultaneous states through a tab strip.
#   2. `system-switch` GATES on a prediction: `wireSwitch` leaves the switch
#      button `disabled` until an option in that panel is pressed. With no
#      options authored, `r_system_switch` still emits `.ks3-switch-predict`
#      with an empty `<ul class="ks3-options">` and the button stays disabled
#      for ever — a dead control, not a narrower version of a live one.
#   3. `system-switch` reveals a LEVELLED CHAIN (`chain[]`, `.ks3-switch-chip`
#      keyed on "Cell"/"Tissue"/"Organ"/"Organism"). B3 job 3 is "harmful
#      species have nowhere to settle", which is an ecological consequence and
#      sits at no level of organisation at all. `show_levels: False` collapses
#      the chip and still demands the chain.
#   4. ⚖️ THE STATE MODEL IS DIFFERENT, and this is the one that settles it.
#      `wireSwitch` and `wireJobSort` are both ONE-WAY and CUMULATIVE — they
#      count panels that have EVER been opened, and `close_all` fires on that
#      count. This block's summary panel is a claim about the configuration
#      the student is looking at RIGHT NOW ("You have just built the germ-free
#      mouse"), so switching a job back on has to take it away again. A
#      component that counts what has happened cannot express a component that
#      reports what is true.
#
# And a fifth, which is about blast radius rather than shape: `system-switch`
# is a LIGHT `.ks3-block` and every `.ks3-switch-*` text rule in
# shared/ks3.css is written for ink on cream. This instrument is ink-dark.
# Widening would mean re-scoping that whole rule set past `.ks3-dark p`, which
# moves b2-01 — a page Mide has already approved — to serve a page he has not
# seen.
#
# `job-sort` was never close: its control is a choice among CATEGORIES with a
# per-row answer, and this block has no answer to give.


def r_job_switch(a, act_id):
    """⊕ b3-08 `#s-jobs` — take one job away and see what breaks.

    ⚖️ THE PAYOFF IS THE WHOLE BLOCK. Five jobs switched off at once IS the
    germ-free mouse from the hook, and the summary panel says so in those
    words. Every other beat here — the five rows, the five consequences, the
    counter — exists to make that one sentence land on a configuration the
    student built themselves rather than on a fact they were told.

    ⚠️ THE GROUND INVERTS, and it is the opposite way round from
    `fold-builder` on the lesson before. There, a level that is ON lights up,
    because the student is building something. Here a job that is STILL BEING
    DONE sits on the panel and a job that has been switched off falls back to
    the block's bare ink with an alert rule round it — the row visibly stops
    being a working part. Two instruments, one control, opposite directions,
    and the direction is the family: b3-07 builds a model up, b3-08 breaks a
    system down.

    ⚠️ NOTHING MARKS. There is no right number of jobs to switch off and no
    `answer_index` to check. The five toggles are `aria-pressed` toggle
    buttons and are deliberately not `.ks3-option`.

    ⚠️ INK-DARK, and the consequence paragraph is CREAM INSIDE IT — the one
    place on this page where ink type sits on the page ground inside an
    ink-dark block. `.ks3-dark p` is (0,1,1) and would paint it
    `--ks3-on-dark-body` #E7DECE on `--ks3-ground` #FBF3E6, which is a 1.1:1
    sentence: present, correct, and unreadable. Every text rule in the
    stylesheet is scoped to at least (0,2,0), and the parity fragment's first
    row is that assertion.

    Emit-both-show-one: all five consequences are in the document, hidden, and
    `wireJobSwitch` unhides them. No authored sentence is rebuilt in JS.
    """
    jobs = a.get("jobs") or []
    if len(jobs) < 2:
        raise ValueError(
            "job-switch %r declares %d job(s). The block's argument is that "
            "the losses ADD UP to one animal, and one loss is not an "
            "accumulation." % (act_id, len(jobs)))
    for j in jobs:
        for key in ("id", "tag", "name", "what", "without"):
            if not j.get(key):
                raise ValueError(
                    "job-switch %r job %r is missing %r. `without` is the "
                    "half that teaches — a job with no stated consequence is "
                    "a label, and the whole method here is switch it off and "
                    "follow what breaks."
                    % (act_id, j.get("id") or j.get("name"), key))

    labels = a.get("labels") or {}
    on_label = labels.get("on")
    off_label = labels.get("off")
    without_label = labels.get("without")
    if not on_label or not off_label:
        raise ValueError(
            "job-switch %r needs `labels.on` and `labels.off` — the button "
            "face is the only thing that says what pressing it will do."
            % act_id)

    # ⚖️ REQUIRED, not defaulted. The summary is what the five rows are for
    # (NOTES-B3 §3.6: "the payoff is the all-five-off summary panel"), and an
    # instrument that could quietly render without it would be five facts and
    # no conclusion.
    summary = a.get("all_off") or {}
    for key in ("tag", "headline", "body"):
        if not summary.get(key):
            raise ValueError(
                "job-switch %r is missing `all_off.%s`. Switching every job "
                "off is the moment the lesson exists for and it may not "
                "arrive silently." % (act_id, key))

    rows = []
    for j in jobs:
        rows.append(
            '<li class="ks3-jobsw-job" data-job="%s" data-off="0">'
            '<div class="ks3-jobsw-main">'
            '<div class="ks3-jobsw-what">'
            '<p class="ks3-jobsw-tag">%s</p>'
            '<p class="ks3-jobsw-name">%s</p>'
            '<p class="ks3-jobsw-does">%s</p></div>'
            '<button type="button" class="ks3-jobsw-toggle" data-jobsw-toggle '
            'aria-pressed="false" data-label-on="%s" data-label-off="%s">%s'
            '</button></div>'
            '<p class="ks3-jobsw-without" hidden data-reveal>'
            '%s%s</p></li>'
            % (e(j["id"]), t(j["tag"]), t(j["name"]), rich(j["what"]),
               e(on_label), e(off_label), t(on_label),
               ('<strong>%s</strong> ' % t(without_label))
               if without_label else "",
               rich(j["without"])))

    return ('<div class="ks3-jobsw" data-jobsw data-total="%d">'
            '<ul class="ks3-jobsw-list" role="list">%s</ul>'
            '<div class="ks3-jobsw-all" hidden data-jobsw-all>'
            '<p class="ks3-jobsw-alltag">%s</p>'
            '<p class="ks3-jobsw-allhead">%s</p>'
            '<p class="ks3-jobsw-allbody">%s</p></div></div>'
            % (len(jobs), "".join(rows), t(summary["tag"]),
               t(summary["headline"]), rich(summary["body"])))
# DISPATCH: "person-ledger": ("ks3-ledger-block", ' data-instrument data-ledgerblock data-stage-done="0"'),
#
# and in ACTIVITY_KIND_FN, beside the other B3 rows:
#     "person-ledger":          r_person_ledger,
#
# Place `r_person_ledger` after `r_test_bench` in the B3 group. Needs `e`, `t`,
# `rich`.
#
# ⚠️ THIS RENDERER CONSUMES NEITHER `options` NOR `reveal`. The block has no
# commitment to make: it is a ledger, and its argument is made by the student
# moving the person under a plate they have already built.


def r_person_ledger(a, act_id):
    """⊕ b3-03 `#s-ledger` — the requirement is a property of the PERSON.

    ⚖️ THE PERSON IS A CONTROL, NOT A CONSTANT, and that is the whole
    instrument. NOTES-B3 §2 says it in one line: *requirement is a property of
    the person, so the person is a control.* The plate is built once and then
    the person is changed underneath it, and the same food turns from a
    shortfall into a surplus with nothing about the food having moved. A ledger
    with one fixed eater would be a calculator.

    ⚖️ THE MATCH PANEL'S COPY IS THE EXPERIMENT. It appears only within the
    tolerance and it tells the student to switch person **without changing the
    food** — NOTES-B3 §3.3 flags that instruction as the thing that must not be
    lost, because without it a student who lands on a match reads it as having
    finished. `match.why` is required and this renderer raises without it.

    ⚖️ MRB-232 — THIS BLOCK STAYS ON B3'S SIDE OF THE SPLIT. It reports an
    intake, a requirement and the gap between them, all in kJ. It does not
    teach what a joule is, it derives nothing from power and time, and it
    performs no unit conversion: that clause of `KS3.B.NUT.02` belongs to
    Physics P2 and is reached from this lesson by a `references` edge, never by
    prose and never by a control in here. A future pass that adds a kJ↔kcal
    toggle or an energy-transfer readout to this instrument has moved the seam.

    ⚠️ R3 — NOTHING MARKS, AND NOTHING HERE IS AN ANSWER. Twelve food buttons,
    five person tabs and a clear. No `.ks3-option`, no correct plate, no score.
    The bar changes colour at the tolerance because it is a MEASUREMENT
    readout — short, matched, over — and the panel beside it says in words that
    a match is not an achievement but the start of the experiment.

    ⚠️ ON INK. `.ks3-dark p` is (0,1,1); the match panel is CREAM inside the
    ink block and its three paragraphs are the ones that would silently lose.
    Every text rule in the stylesheet is scoped `.ks3-dark …`.

    Every authored sentence is emitted into the document and switched by
    hiding: the five names, the five requirement lines, the five explanations
    and the five match headlines. The only strings assembled at runtime are the
    three that quote a live NUMBER — the total line, the balance line and the
    portion count — and each is one authored template filled with digits, the
    same mechanism `_head_counter` already uses for every counter in the key
    stage.
    """
    people = a.get("people") or []
    if len(people) < 2:
        raise ValueError(
            "person-ledger %r declares %d person(s). The block's argument is "
            "that the same plate means different things to different bodies, "
            "and one body cannot make it." % (act_id, len(people)))
    for p in people:
        for key in ("id", "label", "name", "lower", "why"):
            if not p.get(key):
                raise ValueError(
                    "person-ledger %r person %r is missing %r. `lower` is the "
                    "in-sentence form (“That day matches an Olympic rower in "
                    "training.”); lower-casing `name` at runtime would strip "
                    "the capital from Olympic."
                    % (act_id, p.get("id"), key))
        if not isinstance(p.get("need"), int) or p["need"] <= 0:
            raise ValueError(
                "person-ledger %r person %r has need %r; it is a whole number "
                "of kilojoules per day." % (act_id, p["id"], p.get("need")))

    foods = a.get("foods") or []
    if len(foods) < 2:
        raise ValueError("person-ledger %r declares %d food(s)." % (act_id, len(foods)))
    for f in foods:
        if not f.get("id") or not f.get("name") or not f.get("kj_label"):
            raise ValueError(
                "person-ledger %r food %r needs `id`, `name` and `kj_label`. "
                "`kj_label` is authored rather than composed because the "
                "zero-energy row reads “0 kJ” and every other row reads "
                "“780 kJ each” — a single template would print “0 kJ each”, "
                "which claims a portion size for a glass of water."
                % (act_id, f.get("id")))
        if not isinstance(f.get("kj"), int) or f["kj"] < 0:
            raise ValueError(
                "person-ledger %r food %r has kj %r; it is a whole number of "
                "kilojoules per portion." % (act_id, f["id"], f.get("kj")))

    balance = a.get("balance") or {}
    missing = sorted({"empty", "matched", "surplus", "short"} - set(balance))
    if missing:
        raise ValueError(
            "person-ledger %r declares no %s balance line. All four states are "
            "reachable from the controls, and a state with no sentence is a "
            "readout that goes blank." % (act_id, ", ".join(missing)))
    match = a.get("match") or {}
    if not (match.get("head") and match.get("why")):
        raise ValueError(
            "person-ledger %r declares no match panel. Its copy is the "
            "experiment — *switch person without changing the food* — and "
            "without it a student who lands on a match reads it as having "
            "finished." % act_id)

    def grouped(n):
        """9500 → 9,500. A NUMBER format, applied to no authored text."""
        return "{:,}".format(int(n))

    first = people[0]
    for p in people:
        if p["id"] == a.get("start_person"):
            first = p
            break

    tabs = "".join(
        '<button type="button" class="ks3-ledger-tab" data-person="%s" '
        'data-need="%d" aria-pressed="%s">%s</button>'
        % (e(p["id"]), p["need"], "true" if p is first else "false",
           t(p["label"]))
        for p in people)

    need_fmt = a.get("need_format") or "Needs {need} kJ / day"

    def switched(cls, attr, value_of):
        return "".join(
            '<span class="%s" data-%s="%s"%s>%s</span>'
            % (cls, attr, e(p["id"]), "" if p is first else " hidden",
               value_of(p))
            for p in people)

    names = switched("ks3-ledger-nameval", "pname", lambda p: t(p["name"]))
    needs = switched("ks3-ledger-needval", "pneed",
                     lambda p: t(need_fmt.replace("{need}", grouped(p["need"]))))
    whys = switched("ks3-ledger-whyval", "pwhy", lambda p: rich(p["why"]))

    food_html = "".join(
        '<li><button type="button" class="ks3-ledger-food" data-food="%s" '
        'data-kj="%d" data-count="0">'
        '<span class="ks3-ledger-foodrow">'
        '<span class="ks3-ledger-foodname">%s</span>'
        '<span class="ks3-ledger-foodcount" data-count-label></span></span>'
        '<span class="ks3-ledger-foodkj">%s</span></button></li>'
        % (e(f["id"]), f["kj"], t(f["name"]), t(f["kj_label"]))
        for f in foods)

    heads = "".join(
        '<p class="ks3-ledger-mhead" data-mhead="%s" hidden>%s</p>'
        % (e(p["id"]), t(match["head"].replace("{person}", p["lower"])))
        for p in people)

    portions = a.get("portions") or {}
    total_fmt = a.get("total_format") or "{total} kJ of {need} kJ"

    # ⚠️ The four balance sentences and the two portion sentences ride as
    # attributes, which is the ONE place this instrument does not emit its text
    # as text. They have to: each quotes a number that does not exist until the
    # student has built a plate, so there is no finished string to emit. This is
    # `_head_counter`'s own mechanism — `data-format`, `data-zero`, `data-off`,
    # `data-on` — and it is safe for exactly the reason that is: the strings
    # carry no markup, so `textContent` loses nothing, and `e()` is the
    # attribute escaper. A sentence that carries `<em>` may never travel this
    # way, and none of these does.
    return ('<div class="ks3-ledger" data-ledger data-person="%s" '
            'data-tolerance="%d" data-max="%d" data-count-format="%s">'
            '<div class="ks3-ledger-who">'
            '<p class="ks3-ledger-grouplabel">%s</p>'
            '<div class="ks3-ledger-tabs">%s</div></div>'
            '<div class="ks3-ledger-panel">'
            '<div class="ks3-ledger-head">'
            '<p class="ks3-ledger-name">%s</p>'
            '<p class="ks3-ledger-need">%s</p></div>'
            '<p class="ks3-ledger-why">%s</p>'
            '<div class="ks3-ledger-bar">'
            '<span class="ks3-ledger-fill" data-bar data-state="short"></span>'
            '</div>'
            '<div class="ks3-ledger-figures">'
            '<p class="ks3-ledger-total" data-total data-format="%s">%s</p>'
            '<p class="ks3-ledger-balance" data-balance role="status" '
            'data-empty="%s" data-matched="%s" data-surplus="%s" '
            'data-short="%s">%s</p></div></div>'
            '<p class="ks3-ledger-foodlabel">%s</p>'
            '<ul class="ks3-ledger-foods" role="list">%s</ul>'
            '<div class="ks3-ledger-foot">'
            '<button type="button" class="ks3-reveal-btn ks3-ledger-clear" '
            'data-ledger-clear>%s</button>'
            '<span class="ks3-ledger-portions" data-portions data-empty="%s" '
            'data-format="%s" data-format-one="%s">%s</span></div>'
            '<div class="ks3-ledger-match" hidden data-match>'
            '<p class="ks3-ledger-mlabel">%s</p>%s'
            '<p class="ks3-ledger-mwhy">%s</p></div></div>'
            % (e(first["id"]), int(a.get("tolerance") or 5),
               int(a.get("max_per_food") or 6),
               e(a.get("count_format") or "×{n}"),
               t(a.get("group_label") or "Who is eating"), tabs,
               names, needs, whys,
               e(total_fmt),
               t(total_fmt.replace("{total}", "0")
                 .replace("{need}", grouped(first["need"]))),
               e(balance["empty"]), e(balance["matched"]),
               e(balance["surplus"]), e(balance["short"]),
               t(balance["empty"]),
               t(a.get("food_label") or ""), food_html,
               t(a.get("clear_label") or "Empty the day"),
               e(portions.get("empty") or ""),
               e(portions.get("some") or "{n} portions, {total} kJ"),
               # MRB-257 (5.44) — "1 portions, 2,400 kJ" is a state every
               # student passes through on the way to the second. Falls back
               # to the plural when a payload does not author it.
               e(portions.get("one") or portions.get("some")
                 or "{n} portions, {total} kJ"),
               t(portions.get("empty") or ""),
               t(match.get("eyebrow") or ""), heads, rich(match["why"])))
# DISPATCH: "test-bench": ("ks3-tbench-block", ' data-instrument data-tbenchblock data-stage-done="0"'),
#
# and in ACTIVITY_KIND_FN, beside the other B3 rows:
#     "test-bench":             r_test_bench,
#
# Place `r_test_bench` after `r_band_commit` in the B3 group. Needs `e`, `t`,
# `rich`, `r_activity_options`.
#
# ⚠️ THIS RENDERER DOES NOT CONSUME the activity's own `options` key, because
# the activity does not author one — the two prediction buttons live under
# `predict.options`, where they belong to the gate rather than to the block.
# `_kinds_consuming()` will therefore NOT list this kind, which is correct:
# there is no top-level `options` for the generic branch to draw twice.


def r_test_bench(a, act_id):
    """⊕ b3-02 `#s-bench` — five foods, four tests, twenty honest results.

    ⚖️ PREDICTING **RUNS** THE TEST. There is no separate run button, and that
    is the mechanism rather than a saving: the commitment IS the action, so a
    student cannot watch the colour first and decide afterwards what they
    thought. Twenty combinations, each gated by its own two-option prediction.

    ⚖️ EVERY RESULT ENDS IN A CLAIM LINE, and for a negative it is the HEDGED
    wording. This is the whole lesson — *“No starch was detected in potato
    under these conditions.” Not “there is none”.* — and the four deliberate
    false negatives in Design's payload (potato/Biuret at 2% protein, apple
    juice/Biuret at 0.3%, and the two that are true negatives and say so) only
    teach anything if the sentence a student is licensed to write is printed
    under every one of them. `claims` is REQUIRED and this renderer raises
    without both halves.

    ⚠️ THE TUBE COLOUR IS REAL AND IS NOT A TOKEN. NOTES-B3 §3.2: the tube is
    the only colour-bearing element in the unit and the colours are the
    reagents' own — Benedict's blue #2E63B8 to brick red #B03A16. They are
    authored as literal hex on the test, never as `var(--ks3-accent)`, because
    an accent-tinted tube would be teaching a colour change that does not
    happen. They reach the page as an attribute on the test tab and are set on
    the tube's fill; that is a COLOUR travelling through an attribute, not a
    sentence.

    ⚠️ EVERYTHING A STUDENT READS IS COMPOSED HERE, AT BUILD TIME. The twenty
    prediction prompts and the twenty claim lines are filled from two authored
    templates and the foods' and tests' own names, in Python, and emitted into
    the document hidden. The browser only ever unhides one of them. Design's
    page assembles all forty in `renderVals()` with `+`, `.toLowerCase()` and
    `.split(' (')[0]`, which is how "Potato" becomes "potato" and "reducing
    sugar (glucose, fructose)" becomes "reducing sugar" — three string
    transformations applied to authored science in the browser. `lower` and
    `detects` are authored instead, so nothing is transformed anywhere.

    ⚠️ ON INK. `.ks3-dark p` is (0,1,1); every text rule in the stylesheet is
    scoped `.ks3-dark …`, and the result panel is CREAM inside the ink block,
    so its four paragraphs are the ones that would silently lose. See the CSS.
    """
    tests = a.get("tests") or []
    foods = a.get("foods") or []
    if len(tests) < 2 or len(foods) < 2:
        raise ValueError(
            "test-bench %r declares %d test(s) and %d food(s). The block's "
            "argument is that one test answers one question, and it cannot be "
            "made with a single row or a single column."
            % (act_id, len(tests), len(foods)))

    for tst in tests:
        for key in ("id", "label", "detects", "detects_full", "method"):
            if not tst.get(key):
                raise ValueError(
                    "test-bench %r test %r is missing %r. `detects` is the "
                    "short form the prompt and the claim line use "
                    "(“reducing sugar”) and `detects_full` is the one the "
                    "method panel prints (“reducing sugar (glucose, "
                    "fructose)”); deriving one from the other would put a "
                    "`.split()` between a student and an authored phrase."
                    % (act_id, tst.get("id"), key))
        for out in ("pos", "neg"):
            spec = tst.get(out) or {}
            for key in ("colour", "name", "headline"):
                if not spec.get(key):
                    raise ValueError(
                        "test-bench %r test %r %s.%s is missing. `name` is the "
                        "tube's own state line and `headline` is the finished "
                        "sentence over the result — both are authored, "
                        "because capitalising the first letter of a reagent "
                        "colour in the browser is a transformation of science "
                        "copy." % (act_id, tst["id"], out, key))

    test_ids = [tst["id"] for tst in tests]
    for f in foods:
        for key in ("id", "label", "lower"):
            if not f.get(key):
                raise ValueError(
                    "test-bench %r food %r is missing %r. `lower` is the form "
                    "the sentence uses (“…in apple juice…”); lower-casing "
                    "`label` at runtime would also lower-case a proper noun "
                    "the moment one is added." % (act_id, f.get("id"), key))
        has, notes = f.get("has") or {}, f.get("notes") or {}
        for tid in test_ids:
            if tid not in has:
                raise ValueError(
                    "test-bench %r: food %r declares no result for test %r. "
                    "Every combination is reachable from the tabs, so a "
                    "missing one is a tube that runs and reports nothing."
                    % (act_id, f["id"], tid))
            if not notes.get(tid):
                raise ValueError(
                    "test-bench %r: food %r has no note for test %r. The note "
                    "is where the honest reading of that result lives — four "
                    "of these are deliberate false negatives and the note is "
                    "the only thing that says so." % (act_id, f["id"], tid))

    predict = a.get("predict") or {}
    if not predict.get("prompt") or len(predict.get("options") or []) < 2:
        raise ValueError(
            "test-bench %r declares no prediction gate. Predicting is what "
            "RUNS the test in this block; without it the tube is a lookup "
            "table." % act_id)
    claims = a.get("claims") or {}
    if not (claims.get("positive") and claims.get("negative")):
        raise ValueError(
            "test-bench %r declares no %s claim line. The claim line is the "
            "lesson." % (act_id,
                         "positive" if not claims.get("positive") else "negative"))
    verdicts = a.get("verdicts") or {}
    if not (verdicts.get("hit") and verdicts.get("miss")):
        raise ValueError("test-bench %r needs both `verdicts` branches." % act_id)

    first_food, first_test = foods[0], tests[0]

    def fill(template, food, tst):
        """One authored template, twenty finished sentences, at BUILD time.

        `{food_lower}` is replaced first: `{food}` is a prefix of it, so the
        other order would leave a stray `_lower` in every negative claim line.
        """
        return (template
                .replace("{food_lower}", food["lower"])
                .replace("{food}", food["label"])
                .replace("{test}", tst["label"])
                .replace("{detects}", tst["detects"]))

    # ── the two tab groups ───────────────────────────────────────────────
    groups = a.get("groups") or {}
    food_tabs = "".join(
        '<button type="button" class="ks3-tbench-tab" data-food="%s" '
        'aria-pressed="%s">%s</button>'
        % (e(f["id"]), "true" if f is first_food else "false", t(f["label"]))
        for f in foods)
    # ⚠️ The two reagent colours ride on the TEST TAB, because the tube shows
    # the negative colour of the selected test before anything is run — so the
    # colours have to be reachable from the selection, not only from a result
    # panel that does not exist yet.
    test_tabs = "".join(
        '<button type="button" class="ks3-tbench-tab" data-test="%s" '
        'data-neg="%s" data-pos="%s" aria-pressed="%s">%s</button>'
        % (e(tst["id"]), e(tst["neg"]["colour"]), e(tst["pos"]["colour"]),
           "true" if tst is first_test else "false", t(tst["label"]))
        for tst in tests)

    # ── the tube ─────────────────────────────────────────────────────────
    # The label is TWO switched spans with a literal join between them, not a
    # string built in the browser: "Potato" and "Iodine" are both authored and
    # both already in the document, so there is nothing to concatenate.
    tube = a.get("tube") or {}
    lfoods = "".join(
        '<span class="ks3-tbench-lfood" data-lfood="%s"%s>%s</span>'
        % (e(f["id"]), "" if f is first_food else " hidden", t(f["label"]))
        for f in foods)
    ltests = "".join(
        '<span class="ks3-tbench-ltest" data-ltest="%s"%s>%s</span>'
        % (e(tst["id"]), "" if tst is first_test else " hidden", t(tst["label"]))
        for tst in tests)
    states = ['<span data-sname="rest">%s</span>' % t(tube.get("not_run") or "")]
    for tst in tests:
        for out in ("pos", "neg"):
            states.append('<span data-sname="%s:%s" hidden>%s</span>'
                          % (e(tst["id"]), out, t(tst[out]["name"])))

    # ── the method card ──────────────────────────────────────────────────
    methods = "".join(
        '<p class="ks3-tbench-method" data-method="%s"%s>%s</p>'
        '<p class="ks3-tbench-detects" data-detects="%s"%s>%s</p>'
        % (e(tst["id"]), "" if tst is first_test else " hidden", t(tst["method"]),
           e(tst["id"]), "" if tst is first_test else " hidden",
           t((a.get("detects_label") or "{detects}")
             .replace("{detects}", tst["detects_full"])))
        for tst in tests)

    # ── twenty prompts and twenty result panels ──────────────────────────
    prompts, results = [], []
    for f in foods:
        for tst in tests:
            key = "%s:%s" % (f["id"], tst["id"])
            cur = f is first_food and tst is first_test
            prompts.append(
                '<p class="ks3-commit ks3-tbench-prompt" data-prompt="%s"%s>%s</p>'
                % (e(key), "" if cur else " hidden",
                   t(fill(predict["prompt"], f, tst))))
            positive = bool(f["has"][tst["id"]])
            side = tst["pos"] if positive else tst["neg"]
            claim = fill(claims["positive"] if positive else claims["negative"],
                         f, tst)
            results.append(
                '<div class="ks3-tbench-result" data-result="%s" '
                'data-outcome="%s" data-colour="%s" hidden>'
                '<p class="ks3-tbench-verdict" data-verdict="hit" hidden>%s</p>'
                '<p class="ks3-tbench-verdict" data-verdict="miss" hidden>%s</p>'
                '<p class="ks3-tbench-head">%s</p>'
                '<p class="ks3-tbench-why">%s</p>'
                '<p class="ks3-tbench-claim"><strong>%s</strong> %s</p></div>'
                % (e(key), "pos" if positive else "neg", e(side["colour"]),
                   t(verdicts["hit"]), t(verdicts["miss"]),
                   t(side["headline"]), rich(f["notes"][tst["id"]]),
                   t(a.get("claim_label") or "What you may write down:"),
                   rich(claim)))

    return ('<div class="ks3-tbench" data-tbench data-food="%s" data-test="%s" '
            'data-target="%d">'
            '<div class="ks3-tbench-picks">'
            '<div class="ks3-tbench-group"><p class="ks3-tbench-grouplabel">%s</p>'
            '<div class="ks3-tbench-tabs">%s</div></div>'
            '<div class="ks3-tbench-group"><p class="ks3-tbench-grouplabel">%s</p>'
            '<div class="ks3-tbench-tabs">%s</div></div></div>'
            '<div class="ks3-tbench-readout">'
            '<div class="ks3-tbench-tubecard">'
            '<span class="ks3-tbench-tube" aria-hidden="true">'
            '<span class="ks3-tbench-fill" data-tube data-run="0" '
            'style="background:%s"></span></span>'
            '<div class="ks3-tbench-tubemeta">'
            '<p class="ks3-tbench-cap">%s</p>'
            '<p class="ks3-tbench-tubelabel">%s'
            '<span class="ks3-tbench-join" aria-hidden="true">%s</span>%s</p>'
            '<p class="ks3-tbench-state" data-state role="status">%s</p>'
            '</div></div>'
            '<div class="ks3-tbench-methodcard">'
            '<p class="ks3-tbench-cap">%s</p>%s</div></div>'
            '<div class="ks3-tbench-predict" data-predict>%s%s</div>'
            '<div class="ks3-tbench-results">%s</div></div>'
            % (e(first_food["id"]), e(first_test["id"]),
               int(a.get("rail_after") or 4),
               t(groups.get("food") or "Food"), food_tabs,
               t(groups.get("test") or "Test"), test_tabs,
               e(first_test["neg"]["colour"]),
               t(tube.get("caption") or "In the tube"),
               lfoods, t(tube.get("label_join") or " + "), ltests,
               "".join(states),
               t(a.get("method_label") or "Method"), methods,
               "".join(prompts), r_activity_options(predict["options"]),
               "".join(results)))


# ── registrations ────────────────────────────────────────────────────────
ART = {
    'gut-tube': _gut_tube,
    'villus': _villus,
}

KIND_SHELL = {
    'band-commit': ("ks3-plate-block", ' data-instrument data-plateblock data-stage-done="0"'),
    'clinic-cases': ("ks3-clinic-block", ' data-instrument data-clinicblock data-stage-done="0"'),
    'enzyme-run': ("ks3-erun-block", ' data-instrument data-erunblock data-stage-done="0"'),
    'fold-builder': ("ks3-fold-block", ' data-instrument data-foldblock data-stage-done="0"'),
    'gut-journey': ("ks3-gut-block", ' data-instrument data-gutblock data-stage-done="0"'),
    'job-switch': ("ks3-jobsw-block", ' data-instrument data-jobswblock data-stage-done="0"'),
    'person-ledger': ("ks3-ledger-block", ' data-instrument data-ledgerblock data-stage-done="0"'),
    'test-bench': ("ks3-tbench-block", ' data-instrument data-tbenchblock data-stage-done="0"'),
}

KIND_FN = {
    'band-commit': r_band_commit,
    'clinic-cases': r_clinic_cases,
    'enzyme-run': r_enzyme_run,
    'fold-builder': r_fold_builder,
    'gut-journey': r_gut_journey,
    'job-switch': r_job_switch,
    'person-ledger': r_person_ledger,
    'test-bench': r_test_bench,
}
