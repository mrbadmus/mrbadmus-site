"""ks3_art.b5 — B5's drawers, instruments and registrations.

ONE UNIT, ONE FILE. Nothing here is read by any other unit; nothing
here may be added to any other unit's module. Moved verbatim out of
``build_ks3.py`` by MRB-271 so that two content lanes can build two
units at once without editing the same file.
"""

import math
import re
from ks3_art.kit import (
    _SVG_ACCENT,
    _SVG_ACCENT_TEXT,
    _SVG_ACCENT_TINT,
    _SVG_BAND,
    _SVG_BLUE_TEXT,
    _SVG_CARD,
    _SVG_GROUND,
    _SVG_INK,
    _SVG_INK_BODY,
    _SVG_INK_FAINT,
    _SVG_INK_GHOST,
    _SVG_INK_MUTED,
    _SVG_INSET,
    _SVG_RULE,
    _SVG_RULE_STRONG,
    _circle,
    _ellipse,
    _label,
    _mono,
    _n,
    _num,
    _path,
    _pctnum,
    _rect,
    _svg_open,
    e,
    option_letter,
    rich,
    t,
)


# ── b5-placenta-exchange · the two circulations ─────────────────────────────
#
# THE WHOLE FIGURE IS ONE NEGATIVE CLAIM: nothing joins. Every constant below
# exists so that the claim is a property of the geometry rather than of a
# sentence beside it, and so that a parity row can measure it.

# The three villi, each as (number, outline, feed-branch y, return-branch y,
# capillary loop). ⚖️ THE OUTLINE IS ONE CLOSED `Z` PATH PER VILLUS and the
# loop is one stroke that leaves and returns — that is the drawing's proof.
# A villus split into two arcs, or a loop drawn as two strokes meeting, would
# render identically and would have a seam in it, and the seam is exactly the
# thing a student is being asked to look for and not find. Kept as single
# paths for that reason, not for brevity.
_B5_PLACENTA_VILLI = (
    (1,
     "M 444,170 H 470 L 470,148 Q 481,132 492,148 L 492,170 H 556 L 556,152 "
     "Q 569,138 582,152 L 582,170 H 620 C 652,170 652,234 620,234 H 444 Z",
     188, 216,
     "M 444,188 H 596 C 626,188 626,216 596,216 H 444"),
    (2,
     "M 444,302 H 470 L 470,280 Q 481,264 492,280 L 492,302 H 556 L 556,284 "
     "Q 569,270 582,284 L 582,302 H 652 C 684,302 684,366 652,366 H 582 "
     "L 582,384 Q 569,398 556,384 L 556,366 H 492 L 492,388 Q 481,404 470,388 "
     "L 470,366 H 444 Z",
     320, 348,
     "M 444,320 H 628 C 658,320 658,348 628,348 H 444"),
    (3,
     "M 444,434 H 592 C 624,434 624,498 592,498 H 582 L 582,508 Q 569,520 "
     "556,508 L 556,498 H 492 L 492,512 Q 481,524 470,512 L 470,498 H 444 Z",
     452, 480,
     "M 444,452 H 568 C 598,452 598,480 568,480 H 444"),
)
# The four labelled crossings, as
# (substance, direction, label, label x, label y, arrow x, y from, y to, head y).
#
# ⚠️ DIRECTION IS NOT A FUNCTION OF WHICH WAY THE ARROW POINTS ON THE PAGE.
# All four point DOWN. The top two start in the mother's blood above the villus
# and end inside it — that is `in`. The bottom two start inside the villus and
# end in the mother's blood below it — that is `out`. Reading the arrowhead
# alone gets three of the four wrong, which is why `data-direction` is written
# down here beside the coordinates rather than inferred anywhere.
#
# ⊕ `label x` is not `arrow x`: urea's word is set at 628 against an arrow at
# 612, because at 612 it would have collided with the villus's right lobe.
# Design moved the word, not the arrow, and the two columns keep that apart.
_B5_PLACENTA_CROSSINGS = (
    ("oxygen",         "in",  "oxygen",         520, 258, 520, 272, 320, 318),
    ("glucose",        "in",  "glucose",        612, 258, 612, 272, 320, 318),
    ("carbon-dioxide", "out", "carbon dioxide", 520, 428, 520, 346, 392, 390),
    ("urea",           "out", "urea",           628, 428, 612, 346, 392, 390),
)
# The uterus wall's hatching, as one path. Ten parallel ticks: the wall is a
# MATERIAL, and the hatch is what says so without a second colour.
_B5_PLACENTA_HATCH = (
    "M 764,96 L 798,66 M 764,146 L 798,116 M 764,196 L 798,166 "
    "M 764,246 L 798,216 M 764,296 L 798,266 M 764,346 L 798,316 "
    "M 764,396 L 798,366 M 764,446 L 798,416 M 764,496 L 798,466 "
    "M 764,546 L 798,516"
)
def _placenta(fig):
    """Where the placenta is, and what happens inside it: two bloodstreams
    interlocked across an enormous surface and never once joined.

    The lesson's flagship misconception — *"the baby's blood mixes with the
    mother's"* — is PURELY SPATIAL, and that is the whole reason this is a
    drawing rather than a paragraph. Prose can assert non-contact; only a
    drawing can be looked at and found not to contain a join. So the figure is
    built to be searched for the join and to survive the search.

    Two plates, because the misconception has two halves and they need
    different scales. The left plate answers *where* — a uterus in section, the
    placenta as a pad against the wall, the cord running down to the foetus —
    and a dashed marker on the pad opens into the right plate through a flare,
    so the zoom is a drawn relationship rather than two unrelated pictures on
    one sheet. The right plate answers *what is happening*, at the only scale
    where interdigitation is visible at all.

    ⚖️ WHY THE ENCODING IS WHAT IT IS. Three channels carry the claim, and no
    single one of them is trusted:

      · SHAPE — each villus is one closed path. The foetal vessel inside it is
        one stroke that arrives, turns at the tip and returns. Neither has an
        end anywhere except at the cord.
      · POSITION — the mother's blood is a field that the villi reach into and
        that reaches back between them. Every point where the two get close is
        a point where placenta tissue is drawn between them.
      · WORDS — three key lines name the three things, and the label on the
        plate says *the wall — never open*.

    ⚠️ THE TWO HUES ARE THE ONE EXCEPTION TO "NO CATEGORY HUE", AND THEY ARE
    DECLARED ON THE DRAWING'S OWN FACE. `--ks3-blue-text` for the baby's blood
    and `--ks3-accent` for the mother's are a category distinction, which the
    kit otherwise forbids. They earn it here because *whose blood is whose* is
    the entire subject and there is no shape available to carry it — both are
    blood, both are in vessels, both are red in life. So the exception is paid
    for three times over: each hue has a key line naming it in words, each has
    drawn direction arrows, and the caption states outright that the colours
    say only whose is whose. Removing the colour would lose nothing a reader
    could not recover from the key and the arrows. Design shipped this pair in
    an earlier session and fig-07 matches the blue; both are kept as delivered.

    ⛔ THE HOOKS ARE THE POINT OF THIS DRAWER, not decoration on it. A defect
    here is silent: a stray vessel that overshoots into the mother's field, or
    a villus outline that fails to close, still looks like a diagram of a
    placenta. So every element belonging to a circulation carries
    `data-stream`, every element drawn as the barrier carries `data-gap`, and
    the four crossings carry `data-crosses` with `data-direction`. That lets a
    parity row assert what the drawing actually claims — no element is in both
    streams, the two sets never share a boundary, and all four substances go
    the way the science says — rather than asserting that a figure was emitted.

      · `data-stream`  — "mother" | "foetus". On EVERY fill, vessel and arrow
        belonging to a circulation, including the key chips, not only the two
        the labels touch. A gate that measures a subset measures nothing.
      · `data-gap`     — on the placenta tissue: the plate, the plate's face,
        each villus outline, and the tissue chip in the key.
      · `data-flow`    — "arriving" | "returning", in ONE frame for both
        streams: travelling into the exchange region, or back out of it. The
        three-sided villus loops carry neither, because a single path holds
        both halves; their direction lives on the two drawn triangles.
      · `data-panel`   — "where" | "inside". A non-contact measurement is only
        meaningful within the plate that draws the exchange; the left plate's
        cord vessels are the same circulation at a scale where the mother's
        blood is not drawn at all, and would otherwise poison the measurement.

    Note the crossing arrows carry NO `data-stream`. They are substances, and
    a substance belongs to neither circulation — which is the sentence the
    whole figure exists to make visible.
    """
    W, H = 860, 650
    out = [_svg_open(fig, W, H)]

    # Two clips, named off the figure id. ⚠️ A bare `id="f5L"` would collide
    # the moment a second figure landed on the same page, and `url(#f5L)`
    # resolves to whichever came first in the document — so one lesson's plate
    # would silently take another's clip rectangle.
    clip_l = "%s-clip-where" % e(fig["id"])
    clip_r = "%s-clip-inside" % e(fig["id"])
    out.append(
        '<defs>'
        '<clipPath id="%s"><rect x="30" y="60" width="290" height="410" '
        'rx="18"/></clipPath>'
        '<clipPath id="%s"><rect x="380" y="60" width="450" height="500" '
        'rx="18"/></clipPath>'
        '</defs>' % (clip_l, clip_r))

    # Round caps and joins for the whole drawing, once. Design set them on her
    # single wrapping `<g>`; every thick stroke in here — the 6px vessels, the
    # 7px maternal arrows, the villus corners — is shaped by them, so they are
    # geometry, not polish. They are the only presentation attributes on this
    # group: paint stays in `style`, on every element, as the law requires.
    out.append('<g stroke-linecap="round" stroke-linejoin="round">')

    # ── the flare, joining the two plates ────────────────────────────────
    # Drawn FIRST so both cards sit on top of it. It is the zoom, not the
    # mother's blood, and it deliberately carries no `data-stream`: it is tinted
    # with the same accent tint as her blood field, and a gate that took it for
    # a circulation would find the mother's blood spilling across the gutter.
    out.append(_path("M 250,182 L 380,60 L 380,560 L 250,240 Z",
                     fill=_SVG_ACCENT_TINT))
    out.append(_path("M 250,182 L 380,60", stroke=_SVG_RULE_STRONG, w=1.6,
                     dash="6 5"))
    out.append(_path("M 250,240 L 380,560", stroke=_SVG_RULE_STRONG, w=1.6,
                     dash="6 5"))

    out.append(_mono(30, 42, "WHERE IT IS", size=14, weight="400",
                     spacing="1.4"))
    out.append(_mono(380, 42, "WHAT IS HAPPENING INSIDE IT", size=14,
                     weight="400", spacing="1.4"))

    # ── plate one · where it is ──────────────────────────────────────────
    out.append(_rect(30, 60, 290, 410, rx=18, fill=_SVG_CARD, stroke=_SVG_INK,
                     w=2.5))
    out.append('<g clip-path="url(#%s)">' % clip_l)
    # Uterus wall as a band with a lining inside it, so "wall" is a thickness
    # rather than a line — the same reading the right plate then magnifies.
    out.append(_ellipse(175, 300, 118, 130, fill=_SVG_BAND, stroke=_SVG_INK,
                        w=3))
    out.append(_ellipse(175, 300, 104, 116, fill=_SVG_INSET, stroke=_SVG_INK,
                        w=1.6))
    # The placenta pad. No `data-gap`: at this scale it is the whole organ
    # against the wall, not the one-cell barrier between two bloods, and the
    # barrier is what `data-gap` names.
    out.append(_path("M 105,214 A 104,116 0 0 1 245,214 Q 175,248 105,214 Z",
                     fill=_SVG_CARD, stroke=_SVG_INK, w=2.5))
    # The two cord vessels, drawn as two so the cord is visibly a bundle
    # carrying blood BOTH WAYS — the fact the right plate then opens up.
    for d in ("M 168,236 C 188,266 150,292 172,322 C 186,342 166,352 164,366",
              "M 178,236 C 198,268 160,294 182,324 C 194,342 176,354 174,366"):
        out.append(_path(d, stroke=_SVG_BLUE_TEXT, w=4,
                         data_stream="foetus", data_panel="where"))
    out.append(_path(
        "M 206,352 C 220,368 216,392 194,400 C 170,408 144,396 138,378 "
        "C 132,358 148,340 166,340 C 162,322 174,308 190,311 "
        "C 205,314 212,330 204,342 C 205,345 206,348 206,352 Z",
        fill=_SVG_CARD, stroke=_SVG_INK, w=2.5))
    # The dashed marker: the region the right plate is a magnification of.
    # Dashed, and it lines up with the flare, so the relationship is drawn.
    out.append(_rect(90, 176, 160, 68, rx=16, stroke=_SVG_INK, w=1.6,
                     dash="6 5"))
    out.append('</g>')

    # Labels sit OUTSIDE the clip, with leaders reaching in. A label clipped to
    # the card would lose its last word to the rounded corner and nothing would
    # warn: SVG text simply draws outside the box and is cut.
    out.append(_label(44, 140, "placenta", size=16, weight="700",
                      anchor="start"))
    out.append(_path("M 110,146 L 142,198", stroke=_SVG_INK, w=1.4))
    out.append(_label(250, 268, "cord", size=16, weight="700", anchor="start"))
    out.append(_path("M 246,272 L 198,282", stroke=_SVG_INK, w=1.4))
    out.append(_label(232, 416, "the baby", size=16, weight="700",
                      anchor="start"))
    out.append(_path("M 228,410 L 206,392", stroke=_SVG_INK, w=1.4))
    out.append(_label(44, 452, "uterus wall", size=16, weight="400",
                      anchor="start"))
    out.append(_path("M 110,446 L 132,418", stroke=_SVG_INK, w=1.4))

    # ── plate two · what is happening inside it ──────────────────────────
    out.append('<g clip-path="url(#%s)">' % clip_r)
    # Three bands, left to right: the placenta's own tissue, the mother's
    # blood, the uterus wall. The tissue band is the plate the villi grow from
    # and the cord arrives at, so it is barrier all the way down.
    out.append(_rect(380, 60, 64, 500, fill=_SVG_CARD,
                     data_gap="1", data_panel="inside"))
    out.append(_rect(444, 60, 318, 500, fill=_SVG_ACCENT_TINT,
                     data_stream="mother", data_panel="inside"))
    out.append(_rect(762, 60, 68, 500, fill=_SVG_BAND))
    out.append(_path(_B5_PLACENTA_HATCH, stroke=_SVG_RULE_STRONG, w=2))
    out.append(_path("M 762,60 V 560", stroke=_SVG_INK, w=2.5))

    # The tissue plate's face, in the four stretches between the villi. Drawn
    # as one path so that the face and the three outlines together are a single
    # unbroken frontier — there is no stretch of it that is merely absent.
    out.append(_path("M 444,60 V 170 M 444,234 V 302 M 444,366 V 434 "
                     "M 444,498 V 560",
                     stroke=_SVG_INK, w=2.5,
                     data_gap="1", data_panel="inside"))

    # All three outlines before any vessel, exactly as Design layered them: the
    # tissue is the ground the blue is drawn ON, and reversing the order would
    # let a later villus's fill cover an earlier villus's vessel.
    for n, outline, _feed, _ret, _loop in _B5_PLACENTA_VILLI:
        out.append(_path(outline, fill=_SVG_CARD, stroke=_SVG_INK, w=2.5,
                         data_gap="1", data_villus=n, data_panel="inside"))

    # The cord's two trunks, running the height of the tissue plate.
    out.append(_path("M 380,110 C 400,110 416,142 416,188 V 452",
                     stroke=_SVG_BLUE_TEXT, w=6, data_stream="foetus",
                     data_flow="arriving", data_panel="inside"))
    out.append(_path("M 396,480 V 176 C 396,148 392,138 380,138",
                     stroke=_SVG_BLUE_TEXT, w=6, data_stream="foetus",
                     data_flow="returning", data_panel="inside"))
    for n, _outline, feed, ret, _loop in _B5_PLACENTA_VILLI:
        out.append(_path("M 416,%d H 444" % feed, stroke=_SVG_BLUE_TEXT, w=6,
                         data_stream="foetus", data_flow="arriving",
                         data_villus=n, data_panel="inside"))
    for n, _outline, feed, ret, _loop in _B5_PLACENTA_VILLI:
        out.append(_path("M 444,%d H 396" % ret, stroke=_SVG_BLUE_TEXT, w=6,
                         data_stream="foetus", data_flow="returning",
                         data_villus=n, data_panel="inside"))
    # ⚖️ ONE PATH PER LOOP, carrying both halves of the journey. No `data-flow`
    # on these, because the path is genuinely both; the two triangles below say
    # which end is which.
    for n, _outline, _feed, _ret, loop in _B5_PLACENTA_VILLI:
        out.append(_path(loop, stroke=_SVG_BLUE_TEXT, w=6,
                         data_stream="foetus", data_villus=n,
                         data_panel="inside"))

    # Four drawn triangles on the foetal circuit — one pair on the first
    # villus's loop, one pair where the cord meets the plate. Triangles, not a
    # typed arrow character: the latin subsets carry no arrow glyph and a typed
    # one falls back silently to whatever the system has.
    out.append(_path("M 536,180 L 536,196 L 552,188 Z", fill=_SVG_BLUE_TEXT,
                     data_stream="foetus", data_flow="arriving",
                     data_villus=1, data_panel="inside"))
    out.append(_path("M 552,208 L 552,224 L 536,216 Z", fill=_SVG_BLUE_TEXT,
                     data_stream="foetus", data_flow="returning",
                     data_villus=1, data_panel="inside"))
    out.append(_path("M 404,102 L 404,118 L 420,110 Z", fill=_SVG_BLUE_TEXT,
                     data_stream="foetus", data_flow="arriving",
                     data_panel="inside"))
    out.append(_path("M 396,130 L 396,146 L 380,138 Z", fill=_SVG_BLUE_TEXT,
                     data_stream="foetus", data_flow="returning",
                     data_panel="inside"))

    # The mother's blood, arriving through the uterus wall at the top and
    # leaving through the same wall at the bottom. Her stream crosses the
    # uterus wall and stops dead at the tissue plate; it has no branch that
    # enters a villus, and there is nothing for it to join.
    out.append(_path("M 812,150 C 776,150 750,142 706,152", stroke=_SVG_ACCENT,
                     w=7, data_stream="mother", data_flow="arriving",
                     data_panel="inside"))
    out.append(_path("M 706,144 L 706,160 L 690,152 Z", fill=_SVG_ACCENT,
                     data_stream="mother", data_flow="arriving",
                     data_panel="inside"))
    out.append(_path("M 700,536 C 754,528 780,536 812,536", stroke=_SVG_ACCENT,
                     w=7, data_stream="mother", data_flow="returning",
                     data_panel="inside"))
    out.append(_path("M 812,528 L 812,544 L 828,536 Z", fill=_SVG_ACCENT,
                     data_stream="mother", data_flow="returning",
                     data_panel="inside"))

    # The four crossings, in ink — neither stream's colour, because a substance
    # belongs to neither. Shaft and head carry the same two hooks so that
    # `[data-crosses="urea"]` selects a whole arrow, not half of one.
    for sub, direction, _lab, _lx, _ly, ax, y1, y2, hy in \
            _B5_PLACENTA_CROSSINGS:
        out.append(_path("M %d,%d V %d" % (ax, y1, y2), stroke=_SVG_INK, w=3,
                         data_crosses=sub, data_direction=direction,
                         data_panel="inside"))
        out.append(_path("M %d,%d L %d,%d L %d,%d Z"
                         % (ax - 7, hy, ax + 7, hy, ax, hy + 14),
                         fill=_SVG_INK,
                         data_crosses=sub, data_direction=direction,
                         data_panel="inside"))
    out.append('</g>')

    out.append(_rect(380, 60, 450, 500, rx=18, stroke=_SVG_INK, w=2.5))

    # ── the words on plate two ───────────────────────────────────────────
    out.append(_label(452, 94, "the cord — the baby's own", size=16,
                      weight="700", anchor="start"))
    out.append(_label(452, 116, "blood, out and back", size=16, weight="700",
                      anchor="start"))
    out.append(_label(452, 546, "the wall — never open", size=16,
                      weight="700", anchor="start"))
    out.append(_path("M 648,540 L 620,504", stroke=_SVG_INK, w=1.4))
    out.append(_label(690, 126, "mother's blood in", size=16, weight="400"))
    out.append(_label(690, 516, "and out again", size=16, weight="400"))
    # ⚠️ THE SAME TUPLE THAT DREW THE ARROWS. The words and the arrows are two
    # loops over one list for the reason `_food_web` records: two loops that
    # each spell their own coordinates are two things free to drift, and the
    # drift here would print "urea" over an arrow carrying oxygen inward.
    for _sub, _direction, lab, lx, ly, _ax, _y1, _y2, _hy in \
            _B5_PLACENTA_CROSSINGS:
        out.append(_label(lx, ly, lab, size=16, weight="400"))
    out.append(_mono(770, 84, "uterus", size=14, weight="400"))
    out.append(_mono(770, 104, "wall", size=14, weight="400"))

    # ── the key ──────────────────────────────────────────────────────────
    # Three chips, three names. This is what pays for the two hues: with the
    # key read once, the drawing is legible with the colour discarded.
    out.append(_rect(30, 600, 34, 20, rx=5, fill=_SVG_ACCENT_TINT,
                     stroke=_SVG_INK, w=2, data_stream="mother",
                     data_key="legend"))
    out.append(_path("M 34,610 H 60", stroke=_SVG_ACCENT, w=5,
                     data_stream="mother", data_key="legend"))
    out.append(_label(74, 616, "The mother's blood", size=17, weight="700",
                      anchor="start"))
    out.append(_path("M 250,610 H 284", stroke=_SVG_BLUE_TEXT, w=6,
                     data_stream="foetus", data_key="legend"))
    out.append(_label(294, 616, "The baby's blood", size=17, weight="700",
                      anchor="start"))
    out.append(_rect(470, 600, 34, 20, rx=5, fill=_SVG_CARD, stroke=_SVG_INK,
                     w=2.5, data_gap="1", data_key="legend"))
    out.append(_label(514, 616, "The placenta's tissue — the wall",
                      size=17, weight="400", anchor="start"))

    out.append('</g>')
    out.append('</svg>')
    return "".join(out)
# ── ⊕ MRB-254 · WS1 #9, b5-flower-parts-labelled — Design's fig-09, ported ──
#
# The two feathery-stigma plumes, as cubic Béziers, exactly as her `PLUMES`
# const holds them. BOTH the drawn curve and the barbs along it are emitted
# from this one table, where her delivery held the curve in the SVG and the
# barb sampler in the JS. That is the only structural liberty in this port and
# it is taken on purpose: a barb is placed by sampling its curve, so if the two
# copies of the curve could disagree the drawing would grow a fringe that hangs
# off nothing, and it would still look like a feathery stigma. One table, one
# curve, and the assertion in the docstring can never be satisfied by accident.
_FLOWER_PLUMES = (
    ((712, 400), (700, 340), (690, 270), (694, 206)),
    ((728, 400), (742, 340), (754, 270), (750, 206)),
)
# The badges on the insect-pollinated flower: leader path, badge centre,
# numeral, part slug. NINE ROWS, and nine is a claim the figure makes — the
# key below names the same nine, and the floret re-uses three of the same
# numbers rather than minting its own.
_FLOWER_BADGES_INSECT = (
    ("M 210,272 L 240,290", 196, 266, "01", "anther"),
    ("M 210,402 L 252,398", 196, 404, "02", "filament"),
    ("M 332,250 L 300,260", 346, 246, "03", "stigma"),
    ("M 338,322 L 290,322", 352, 322, "04", "style"),
    ("M 366,432 L 320,432", 380, 432, "05", "ovary"),
    ("M 366,492 L 296,452", 380, 496, "06", "ovule"),
    ("M 134,302 L 158,306", 120, 300, "07", "petal"),
    ("M 164,520 L 198,500", 150, 524, "08", "sepal"),
    ("M 160,448 L 228,446", 146, 448, "09", "nectary"),
)
# The three on the floret. Each carries the word "outside" under it — the one
# word the right-hand drawing exists to make checkable. Design set that word at
# 12px; it is raised to 13 here, and the report says so.
#
# ⊕ MRB-254 · THE LAST COLUMN IS HOW FAR THE WORD SITS UNDER THE BADGE, and it
# is a column rather than a constant because two of these three leaders pass
# through the space Design's constant put the word in. Reasoning at the call
# site, where the coordinates it has to clear are also written down.
_FLOWER_BADGES_WIND = (
    ("M 600,332 L 608,368", 592, 318, "01", "anther", 94),
    ("M 800,334 L 782,376", 806, 318, "02", "filament", 94),
    ("M 662,222 L 690,234", 648, 216, "03", "stigma", 30),
)
# The key: (badge cx, text x, row centre y, numeral, slug, name, job).
_FLOWER_KEY = (
    (38, 64, 700, "01", "anther", "Anther",
     "Makes pollen, each grain carrying a male nucleus"),
    (38, 64, 744, "02", "filament", "Filament",
     "Holds the anther where pollen can be taken away"),
    (38, 64, 788, "03", "stigma", "Stigma",
     "Catches pollen. Sticky, or feathery"),
    (38, 64, 832, "04", "style", "Style",
     "Raises the stigma; the pollen tube’s route down"),
    (38, 64, 876, "05", "ovary", "Ovary",
     "Holds the ovules, and becomes the fruit"),
    (494, 520, 700, "06", "ovule", "Ovule",
     "One ovule becomes one seed"),
    (494, 520, 744, "07", "petal", "Petal",
     "Advertising. Not a reproductive organ"),
    (494, 520, 788, "08", "sepal", "Sepal",
     "Protected the bud before it opened"),
    (494, 520, 832, "09", "nectary", "Nectary",
     "Makes nectar — the payment for the visit"),
)
def _flower_parts(fig):
    """The same nine parts drawn twice — an insect-pollinated flower cut in
    half, beside a wind-pollinated floret — so that WHERE the anthers and the
    stigma sit is something a student can look at instead of something a table
    tells them.

    ⚖️ THE POSITIONS ARE THE WHOLE FIGURE, and they are the one thing a table
    cannot carry. The lesson's comparison rows say the anthers are "held inside
    the flower" or "dangling outside on long thin filaments", and a student who
    reads that has two phrases to memorise and no way to check either. So both
    drawings are numbered from the SAME key — 01 anther, 02 filament, 03 stigma
    — and each drawing has a dashed line round the flower itself: the inside of
    the petal cup on the left, the pair of bracts on the right. On the left the
    anthers and the stigma are inside that line. On the right they are outside
    it. Nothing else about the numbering changes, which is what makes the
    position the only variable and therefore the readable one.

    ⛔ AND THAT CLAIM IS MEASURED, not labelled. A drawing can put the word
    "outside" beside an anther that is drawn inside, and it will look right to
    anybody who reads the word rather than the picture — the exact defect a
    screenshot cannot catch, because a mislabelled anther is still a
    well-drawn anther. So:

      · each dashed boundary carries `data-envelope` ("insect" | "wind") with
        the `data-flower` it belongs to, and it is emitted as real geometry (a
        cubic path on the left, an ellipse on the right) so a row can flatten
        it and test containment;
      · EVERY anther on both drawings carries `data-anther-position`
        ("inside" | "outside") beside its `data-flower` — all two on the left
        and all three on the right, not the one a label happens to point at.
        A row that measured a single anther would measure the frame again;
      · the stigma of each drawing carries `data-flower` for the same reason:
        the sticky knob and the feathery plumes are the same numbered part in
        two positions, and a row should be able to say which is which without
        reading a word off the plate.

    ⚠️ THE PRINTED WORD AND THE MEASURED FACT CARRY DIFFERENT HOOKS. The three
    "outside" strings under the floret's badges carry `data-position`, NOT
    `data-anther-position`. A row that selects `[data-anther-position]` must
    get anthers and only anthers — five shapes with real coordinates — because
    the moment a `<text>` node joins that set, the row is quietly measuring a
    label's baseline against an envelope and calling it geometry. The two hooks
    exist so the row can also compare them: the word says outside, the drawing
    puts it outside, and the check is that both are true rather than either.

    ⚖️ NINE PARTS, EACH ONCE. `data-part` and `data-number` sit on the drawn
    organ, on its badge (`data-badge="1"`) and on its row in the key
    (`data-key="1"`), so a row can assert the numbering is 01–09 with no gap
    and no repeat, that the badge set and the key set name the same nine, and
    that the floret's three re-use numbers the insect flower already has. Parts
    drawn more than once — two anthers, two filaments, two petals, two sepals,
    three ovules — all carry the same pair, because they are the same part.

    ⚠️ ONLY LABELLED PARTS CARRY `data-part`. The receptacle, the stem, the
    floret's bracts and its tiny ovary are drawn and not numbered, so they are
    left unhooked rather than given a slug the key cannot back. A hook naming a
    part no badge names would break the very count it exists to support.

    ⚖️ THE BARBS ARE SAMPLED, NOT PLACED — Design's named assertion for this
    figure. "Feathery" is not a texture at the tip: the whole length of each
    plume is fringed, and that is the wind-pollinated row's positional claim,
    because a net that catches drifting pollen has to be a net everywhere. So
    nine points are taken along each curve at t = 0.1 … 0.9, the tangent is
    taken from the point 0.02 further on, and the two barbs at each point are
    drawn along the normal to it. Every barb carries `data-plume` (the curve it
    was sampled from), `data-barb` (its index in drawing order) and `data-t`
    (the parameter it was sampled at), and the two plume paths carry the same
    `data-plume` — so a row can take each barb's start point, evaluate its own
    plume's cubic at its own `t`, and assert the barb begins ON the curve
    rather than near it, for all thirty-six of them. That is the difference
    between a drawing that computes its fringe and a drawing that was hand-
    placed to look as if it did.

    ⚠️ `Math.round`, NOT `round`. Her sampler rounds each coordinate to one
    decimal with `Math.round(v * 10) / 10`. Python's `round` is banker's
    rounding and JavaScript's `Math.round` is half-UP, so the two disagree on
    any exact `.5` — and none of these seventy-two coordinates is a tie today,
    which is precisely what would have made the wrong one safe until somebody
    changed the barb length from 13. `math.floor(v * 10 + 0.5) / 10` is
    `Math.round`, so the port is her arithmetic rather than a near-miss of it.
    Nothing here is random and nothing reads the clock: the build is
    byte-identical run to run.

    ⚖️ THE SEPALS ARE POINTED FLAPS, AND THEY ARE NOT GREEN. `--ks3-ok` is
    marks-and-fills for correctness only, so a sepal drawn in it would be
    saying "correct" in a drawing with nothing to be correct about, and the
    student who learns "sepal = the green one" has learned a colour rather than
    a position. They are drawn as two small pointed flaps angling down and out
    below the petals, numbered 08, and the plate says so on its own face: no
    colour in this figure carries a fact on its own. That sentence stays — it
    is addressed to the student about the thing in front of them, so §8.10
    keeps it rather than removing it.
    """
    W, H = 900, 992
    out = [_svg_open(fig, W, H)]

    # Two clips, named off the figure id. ⚠️ A bare `id="f9L"` would collide the
    # moment a second figure landed on the same page — `url(#f9L)` resolves to
    # whichever came first in the document, so one lesson's plate would take
    # another's clip rectangle and nothing would warn.
    clip_l = "%s-clip-insect" % e(fig["id"])
    clip_r = "%s-clip-wind" % e(fig["id"])
    out.append(
        '<defs>'
        '<clipPath id="%s"><rect x="24" y="54" width="520" height="560" '
        'rx="18"/></clipPath>'
        '<clipPath id="%s"><rect x="564" y="54" width="312" height="560" '
        'rx="18"/></clipPath>'
        '</defs>' % (clip_l, clip_r))

    # Round caps and joins once, on the wrapping group, as Design set them.
    # They are geometry here rather than polish: the 9px stem, the 4.5px
    # filaments and the 6px style all end in the open, and a butt cap on any of
    # them reads as a cut rather than a stalk. They are the only presentation
    # attributes on this group — paint stays in `style`, per element.
    out.append('<g stroke-linecap="round" stroke-linejoin="round">')

    out.append(_mono(24, 44, "INSECT-POLLINATED, CUT IN HALF", size=13,
                     weight="400", spacing="1.2"))
    out.append(_mono(564, 44, "WIND-POLLINATED FLORET", size=13,
                     weight="400", spacing="1.2"))

    out.append(_rect(24, 54, 520, 560, rx=18, fill=_SVG_CARD, stroke=_SVG_INK,
                     w=2.5))
    out.append(_rect(564, 54, 312, 560, rx=18, fill=_SVG_CARD, stroke=_SVG_INK,
                     w=2.5))

    # ── the insect-pollinated flower, cut in half ────────────────────────
    out.append('<g clip-path="url(#%s)">' % clip_l)
    out.append(_path("M 284,480 V 566", stroke=_SVG_INK, w=9))

    # The sepals: pointed flaps, below the petals, angled down and out. See the
    # docstring — this shape is doing the work a green fill would otherwise be
    # asked to do, and it is doing it better, because a shape survives being
    # photocopied and a hue does not.
    for d in ("M 266,452 C 232,466 206,486 192,506 C 220,502 254,482 272,464 Z",
              "M 302,452 C 336,466 362,486 376,506 C 348,502 314,482 296,464 Z"):
        out.append(_path(d, fill=_SVG_BAND, stroke=_SVG_INK, w=2.2,
                         data_part="sepal", data_number="08",
                         data_flower="insect"))

    for d in ("M 266,448 C 214,438 172,392 158,320 C 152,286 156,258 168,238 "
              "C 184,272 210,330 240,388 C 252,412 262,432 268,444 Z",
              "M 302,448 C 354,438 396,392 410,320 C 416,286 412,258 400,238 "
              "C 384,272 358,330 328,388 C 316,412 306,432 300,444 Z"):
        out.append(_path(d, fill=_SVG_ACCENT_TINT, stroke=_SVG_INK, w=2.5,
                         data_part="petal", data_number="07",
                         data_flower="insect"))

    # The boundary the left-hand claim is made against: the inside of the petal
    # cup. Dashed, ghost-weight, and labelled in words above it, so a student
    # reads it as "the inside of the flower" rather than as another organ.
    out.append(_path("M 190,250 C 214,336 246,412 284,442 "
                     "C 322,412 354,336 378,250",
                     stroke=_SVG_INK_GHOST, w=2.4, dash="7 6",
                     data_envelope="insect", data_flower="insect"))

    # The receptacle — drawn, unnumbered, unhooked. It is where the parts stand,
    # not one of the nine.
    out.append(_path("M 262,450 C 262,472 274,482 284,482 C 294,482 306,472 "
                     "306,450 Z", fill=_SVG_BAND, stroke=_SVG_INK, w=2.2))

    out.append(_path("M 230,442 C 238,436 248,438 250,446 C 244,454 234,454 "
                     "230,448 Z", fill=_SVG_ACCENT_TINT, stroke=_SVG_INK,
                     w=1.8, data_part="nectary", data_number="09",
                     data_flower="insect"))

    for d in ("M 266,456 C 254,404 246,352 250,320",
              "M 302,456 C 314,404 322,352 318,320"):
        out.append(_path(d, stroke=_SVG_INK, w=4.5, data_part="filament",
                         data_number="02", data_flower="insect"))

    # ⛔ THE TWO ANTHERS, AND BOTH OF THEM CARRY THE POSITION. They sit at
    # y 282–322 between the two arms of the dashed cup, which at that height
    # runs at roughly x 205 and x 363 — so containment is true of the drawn
    # rectangles and not only of the word beside them.
    for x in (238, 306):
        out.append(_rect(x, 282, 24, 40, rx=11, fill=_SVG_BAND,
                         stroke=_SVG_INK, w=2.2, data_part="anther",
                         data_number="01", data_flower="insect",
                         data_anther_position="inside"))
    for cx, cy in ((246, 294), (254, 304), (246, 312),
                   (314, 294), (322, 304), (314, 312)):
        out.append(_circle(cx, cy, 2.6, fill=_SVG_ACCENT_TEXT))

    out.append(_ellipse(284, 432, 34, 28, fill=_SVG_CARD, stroke=_SVG_INK, w=3,
                        data_part="ovary", data_number="05",
                        data_flower="insect"))
    for cx, cy in ((272, 428), (288, 442), (298, 426)):
        out.append(_circle(cx, cy, 7, fill=_SVG_BAND, stroke=_SVG_INK, w=1.8,
                           data_part="ovule", data_number="06",
                           data_flower="insect"))

    out.append(_path("M 284,406 V 278", stroke=_SVG_INK, w=6,
                     data_part="style", data_number="04",
                     data_flower="insect"))
    out.append(_path("M 270,266 C 270,254 278,248 284,248 C 290,248 298,254 "
                     "298,266 C 298,276 290,280 284,280 C 278,280 270,276 "
                     "270,266 Z", fill=_SVG_BAND, stroke=_SVG_INK, w=2.2,
                     data_part="stigma", data_number="03",
                     data_flower="insect"))
    # Sticky dots. The counterpart of the plumes opposite: same part, same
    # number, a different way of catching pollen — dots against a fringe.
    for cx, cy in ((276, 252), (286, 246), (294, 254)):
        out.append(_circle(cx, cy, 2.4, fill=_SVG_ACCENT_TEXT))
    out.append('</g>')

    # The envelope's name, OUTSIDE the clip. A label inside it would lose its
    # last word to the rounded corner, and SVG text simply draws past the box
    # and is cut with no warning.
    out.append(_mono(284, 220, "inside the flower", size=13, weight="400",
                     anchor="middle"))

    for d, cx, cy, num, slug in _FLOWER_BADGES_INSECT:
        out.append(_path(d, stroke=_SVG_INK, w=1.4))
        out.append(_circle(cx, cy, 14, fill=_SVG_BAND, stroke=_SVG_INK, w=2,
                           data_part=slug, data_number=num,
                           data_flower="insect", data_badge="1"))
        out.append(_mono(cx, cy + 6, num, size=15, weight="400",
                         anchor="middle", fill=_SVG_INK, data_part=slug,
                         data_number=num, data_flower="insect",
                         data_badge="1"))

    # ── the wind-pollinated floret ───────────────────────────────────────
    out.append('<g clip-path="url(#%s)">' % clip_r)
    out.append(_path("M 720,470 V 566", stroke=_SVG_INK, w=8))

    # Two papery bracts round a tiny ovary. Drawn, unnumbered, unhooked: they
    # are what the dashed line encloses, and the point of the drawing is how
    # little that is.
    for d in ("M 700,404 C 686,428 690,456 706,470 C 716,452 716,424 710,404 Z",
              "M 740,404 C 754,428 750,456 734,470 C 724,452 724,424 730,404 Z"):
        out.append(_path(d, fill=_SVG_BAND, stroke=_SVG_INK, w=2.2))
    out.append(_ellipse(720, 446, 15, 17, fill=_SVG_CARD, stroke=_SVG_INK,
                        w=2.4))

    # The floret's boundary — an ellipse, so containment on this side is one
    # comparison rather than a flattened curve. It encloses the bracts and
    # nothing else, which is the sentence the right-hand drawing makes.
    out.append(_ellipse(720, 440, 48, 52, stroke=_SVG_RULE_STRONG, w=2,
                        dash="7 6", data_envelope="wind", data_flower="wind"))

    for d in ("M 706,404 C 682,388 646,378 622,384",
              "M 718,398 C 704,354 676,320 650,306",
              "M 734,404 C 758,388 794,378 818,384"):
        out.append(_path(d, stroke=_SVG_INK, w=3, data_part="filament",
                         data_number="02", data_flower="wind"))
    # ⛔ ALL THREE ANTHERS, ALL THREE HOOKED. The nearest of them is more than
    # its own width clear of the dashed ellipse; a row measures that rather
    # than trusting it.
    for x, y in ((596, 374), (626, 292), (814, 374)):
        out.append(_rect(x, y, 30, 19, rx=9, fill=_SVG_BAND, stroke=_SVG_INK,
                         w=2.2, data_part="anther", data_number="01",
                         data_flower="wind", data_anther_position="outside"))
    for cx, cy in ((606, 383), (616, 383), (636, 301), (646, 301),
                   (824, 383), (834, 383)):
        out.append(_circle(cx, cy, 2.4, fill=_SVG_ACCENT_TEXT))

    # ── the feathery stigmas: two curves, and a fringe sampled along them ──
    def _bez(p, t):
        """Design's `bez`, unchanged: one cubic, evaluated at t."""
        u = 1.0 - t
        return (u * u * u * p[0][0] + 3 * u * u * t * p[1][0]
                + 3 * u * t * t * p[2][0] + t * t * t * p[3][0],
                u * u * u * p[0][1] + 3 * u * u * t * p[1][1]
                + 3 * u * t * t * p[2][1] + t * t * t * p[3][1])

    def _r1(v):
        """`Math.round(v * 10) / 10` — half-UP, which `round` is not."""
        return math.floor(v * 10 + 0.5) / 10.0

    for pi, p in enumerate(_FLOWER_PLUMES):
        out.append(_path("M %s,%s C %s,%s %s,%s %s,%s"
                         % (_n(p[0][0]), _n(p[0][1]), _n(p[1][0]), _n(p[1][1]),
                            _n(p[2][0]), _n(p[2][1]), _n(p[3][0]), _n(p[3][1])),
                         stroke=_SVG_INK, w=3.4, data_part="stigma",
                         data_number="03", data_flower="wind",
                         data_plume=pi))
    barb = 0
    for pi, p in enumerate(_FLOWER_PLUMES):
        for i in range(1, 10):
            t = i / 10
            ax, ay = _bez(p, t)
            bx, by = _bez(p, t + 0.02)
            dx, dy = bx - ax, by - ay
            m = math.sqrt(dx * dx + dy * dy) or 1
            nx, ny = -dy / m, dx / m
            ln = 13
            # Both sides of the same sample point, in her order: the fringe is
            # symmetrical about the curve, so one side alone would read as a
            # comb rather than a net.
            for side in (1, -1):
                out.append(_path(
                    "M %s,%s L %s,%s"
                    % (_n(_r1(ax)), _n(_r1(ay)),
                       _n(_r1(ax + side * nx * ln - dx)),
                       _n(_r1(ay + side * ny * ln - dy))),
                    stroke=_SVG_INK, w=1.5, data_barb=barb, data_plume=pi,
                    data_flower="wind", data_t="%.2f" % t))
                barb += 1
    out.append('</g>')

    out.append(_mono(688, 500, "the floret", size=13, weight="400",
                     anchor="end"))
    # What is ABSENT is a fact too, and an absence cannot be labelled with a
    # leader line — there is nothing to point at. So it is stated, in the
    # accent text voice, against the two numbers the key holds.
    out.append(_mono(720, 540, "no petals, no nectary —", size=13,
                     weight="400", anchor="middle", fill=_SVG_ACCENT_TEXT))
    out.append(_mono(720, 558, "07 and 09 are not here", size=13,
                     weight="400", anchor="middle", fill=_SVG_ACCENT_TEXT))

    for d, cx, cy, num, slug, drop in _FLOWER_BADGES_WIND:
        out.append(_path(d, stroke=_SVG_INK, w=1.4))
        out.append(_circle(cx, cy, 14, fill=_SVG_BAND, stroke=_SVG_INK, w=2,
                           data_part=slug, data_number=num,
                           data_flower="wind", data_badge="1"))
        out.append(_mono(cx, cy + 6, num, size=15, weight="400",
                         anchor="middle", fill=_SVG_INK, data_part=slug,
                         data_number=num, data_flower="wind",
                         data_badge="1"))
        # ⚠️ `data-position`, deliberately NOT `data-anther-position` — see the
        # docstring. This is the printed word; the shape carries the measured
        # fact, and a row should be able to compare them without the word
        # joining the set of things being measured.
        #
        # ⊕ MRB-254 · `drop` REPLACES A FLAT +30. Badges 01 and 02 both send
        # their leader straight down past the word — 01 from 600,332 as far as
        # 608,368, and 02 from 800,334 as far as 782,376 — and at +30 the word
        # sat at y 338–351 with those leaders passing through x 602–604 and
        # 794–797. A line down the middle of the one word this drawing exists
        # to make checkable. Sideways is not available on either: 01's word
        # already begins at x 565 against a frame edge at 564, and 02's ends at
        # 833 against 876. Down is, because both leaders STOP at the organ they
        # name, at y 368 and 376, so at +94 the word clears the whole leader
        # and lands directly beneath the anther or the filament instead of
        # beneath the badge. 03's leader leaves to the RIGHT, from 662,222 as
        # far as 690,234, and never crosses its word at all, so it keeps
        # Design's +30: the drop is per badge and not applied to all three.
        out.append(_mono(cx, cy + drop, "outside", size=13, weight="400",
                         anchor="middle", data_part=slug, data_number=num,
                         data_flower="wind", data_position="outside"))

    out.append(_mono(852, 120, "large, and feathery", size=13, weight="400",
                     anchor="end"))
    out.append(_mono(852, 138, "the whole length", size=13, weight="400",
                     anchor="end"))

    # ── the key ──────────────────────────────────────────────────────────
    out.append(_mono(24, 654,
                     "NINE PARTS · 01–02 MALE · "
                     "03–06 FEMALE · 07–09 NEITHER",
                     size=13, weight="400", spacing="1.2"))
    out.append(_path("M 24,666 H 876", stroke=_SVG_RULE, w=2))

    for cx, tx, cy, num, slug, name, job in _FLOWER_KEY:
        out.append(_circle(cx, cy, 14, fill=_SVG_BAND, stroke=_SVG_INK, w=2,
                           data_part=slug, data_number=num, data_key="1"))
        out.append(_mono(cx, cy + 6, num, size=15, weight="400",
                         anchor="middle", fill=_SVG_INK, data_part=slug,
                         data_number=num, data_key="1"))
        out.append(_label(tx, cy - 1, name, size=18, weight="700",
                          anchor="start", data_part=slug, data_number=num,
                          data_key="1"))
        out.append(_label(tx, cy + 19, job, size=15, weight="400",
                          anchor="start", fill=_SVG_INK_BODY,
                          data_part=slug, data_key="1"))

    out.append(_path("M 24,918 H 876", stroke=_SVG_RULE, w=2))
    out.append(_label(24, 948,
                      "The same nine parts, drawn twice. Only where 01, 02 "
                      "and 03 sit has changed.",
                      size=16, weight="700", anchor="start"))
    out.append(_label(24, 970,
                      "The sepals are drawn as pointed flaps rather than in "
                      "green: no colour in this figure carries a fact on its "
                      "own.",
                      size=15, weight="400", anchor="start",
                      fill=_SVG_INK_BODY))

    out.append('</g>')
    out.append('</svg>')
    return "".join(out)
# ── b5-reproductive-systems · nine structures, where the body puts them ─────
#
# ⛔ THE NINE ARE ONE TABLE AND EVERY STRING IN IT IS A LITERAL. Design's own
# build of this figure rendered its nine-row key as nine empty badges — an
# interpolated hole inside `<text>` produces nothing at all, and a `<text>`
# with no content is invisible rather than broken, so the drawing looked
# finished. `_label` now refuses an empty string, but a refusal is the second
# line of defence and not the first. The first is here: there is no source of
# a key row's words other than this table, no concatenation, no lookup that
# can miss, no field that is computed from another figure's state. A blank in
# the key would have to be typed into this table, in quotes, on purpose.
#
# Fields, per row:
#   number       "01".."09". The printed numeral AND the sort order.
#   slug         the `data-structure` value. Stable; a gate names it.
#   system       "male" | "female". Which frame it is drawn in, and which key
#                column it is listed in — the same value does both, so the two
#                cannot disagree.
#   counterpart  "none" | "paired". ⚖️ THIS IS THE MEANING, AND THE BADGE FILL
#                IS DERIVED FROM IT — never the other way round. See the
#                drawer's docstring; this is the whole point of the column.
#   plate        (leader `d` or None, badge cx, badge cy, word x, word y,
#                word anchor) — where the badge lands ON THE DRAWING. `None`
#                for the leader on 07 only: the uterus badge sits inside the
#                uterus, so there is nothing for a leader to reach.
#   word         the short name printed on the plate, lower case.
#   title        the key row's name, sentence case.
#   job          the key row's one line of function.
_B5_REPRO_STRUCTURES = (
    ("01", "testes", "male", "paired",
     ("M 88,400 L 138,398", 74, 400, 74, 432, "middle"),
     "testes", "Testes", "Make sperm cells, from puberty onwards"),
    ("02", "sperm-duct", "male", "paired",
     ("M 86,268 L 160,290", 72, 266, 72, 296, "middle"),
     "sperm duct", "Sperm duct", "Carries sperm towards the urethra"),
    ("03", "glands", "male", "paired",
     ("M 124,186 L 178,214", 110, 180, 110, 212, "middle"),
     "glands", "Glands", "Add fluid; sperm plus fluid is semen"),
    ("04", "penis", "male", "paired",
     ("M 322,432 L 256,452", 336, 428, 336, 460, "middle"),
     "penis", "Penis", "Transfers semen into the vagina"),
    ("05", "ovaries", "female", "paired",
     ("M 512,338 L 518,316", 506, 352, 506, 384, "middle"),
     "ovaries", "Ovaries", "Contain the egg cells; release one a month"),
    ("06", "oviduct", "female", "paired",
     ("M 528,132 L 566,172", 514, 122, 532, 128, "start"),
     "oviduct", "Oviduct", "Carries the egg. Fertilisation happens here"),
    ("07", "uterus", "female", "none",
     (None, 670, 238, 670, 266, "middle"),
     "uterus", "Uterus", "Holds and supplies the developing embryo"),
    ("08", "cervix", "female", "none",
     ("M 730,338 L 700,340", 744, 338, 762, 344, "start"),
     "cervix", "Cervix", "Closes the uterus; opens for birth"),
    ("09", "vagina", "female", "none",
     ("M 730,420 L 700,424", 744, 420, 762, 426, "start"),
     "vagina", "Vagina", "Receives semen; the birth canal"),
)
# The two key columns: (system, left edge, rule right edge, badge cx).
# The words' x is the badge cx plus 26 in both columns, so it is derived once
# below rather than typed twice and allowed to drift.
_B5_REPRO_KEY_COLUMNS = (("male", 24, 420, 38), ("female", 480, 876, 494))
_B5_REPRO_KEY_TOP = 588      # baseline of the first key badge in each column
_B5_REPRO_KEY_STEP = 44      # ⚠️ Design's row pitch; five rows must clear 806
_B5_REPRO_BADGE_R = 14       # every numbered badge, plate and key alike
_B5_REPRO_NUMERAL_DY = 6     # numeral baseline below the badge centre, always
# The column headings count the structures beneath them, so the count is taken
# from the table and spelled from here. Index 0 is the empty string and would
# be a blank heading; it is unreachable — the guard in the drawer refuses a
# column outside 1..9 before this is indexed, and `_label` refuses "" after.
# Two refusals around one array is deliberate: this is the exact shape of the
# hole that produced Design's nine empty badges.
_B5_REPRO_COUNT_WORDS = ("", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX",
                         "SEVEN", "EIGHT", "NINE")
# The male frame, inside its clip. Order is Design's, and order is load-bearing
# here: the sperm ducts are drawn as a dark 9px casing with a 4px inset lumen
# laid over it, so a duct swapped ahead of its casing becomes a flat dark line.
_B5_REPRO_DUCTS = ("M 170,366 C 164,320 178,268 194,246",
                   "M 290,366 C 296,320 282,268 266,246")
# The two oviducts, same casing-then-lumen construction at 10px / 4.5px.
_B5_REPRO_OVIDUCTS = (
    "M 616,192 C 580,166 542,164 524,190 C 508,214 512,244 532,254",
    "M 724,192 C 760,166 798,164 816,190 C 832,214 828,244 808,254")
# The fringed funnel at the end of each oviduct — three strokes, splayed. Drawn
# as three separate line segments in one `d`, exactly as Design has them.
_B5_REPRO_FIMBRIAE = (
    "M 532,256 L 510,270 M 532,256 L 518,280 M 532,256 L 540,282",
    "M 808,256 L 830,270 M 808,256 L 822,280 M 808,256 L 800,282")
# The egg cells already present in each ovary, as (cx, cy). Four per ovary.
# ⚠️ These are CONTENTS, not the organ, and they carry `data-organ="contents"`
# for that reason: a row counting the shapes that make up an ovary must not
# find twelve of them.
_B5_REPRO_EGGS = ((506, 286), (521, 281), (514, 299), (528, 296),
                  (814, 286), (829, 281), (822, 299), (836, 296))
# The wrinkled skin on each testis. Surface texture on a shape that is already
# hooked, and deliberately unhooked itself.
_B5_REPRO_SCROTUM_TEXTURE = (
    "M 148,388 q 10,-8 20,0 q 10,8 20,0 M 148,402 q 10,-8 20,0 q 10,8 20,0",
    "M 268,388 q 10,-8 20,0 q 10,8 20,0 M 268,402 q 10,-8 20,0 q 10,8 20,0")
def _repro_systems(fig):
    """The two human reproductive tracts side by side, nine structures
    numbered where the body actually puts them, above a shared key.

    THE LESSON NAMES NINE STRUCTURES AND ITS BENCH IS A NAME-TO-FUNCTION
    MATCHING QUIZ, which contains not one item of spatial information. A
    student can score full marks on it holding a completely wrong picture of
    where any of these things are — that the testes are inside the abdomen,
    that fertilisation happens in the uterus, that the two systems are mirror
    images of one another with a different part in each slot. This figure is
    the only place in the lesson where the structures get positions, so it is
    drawn to be READ POSITIONALLY and not as decoration beside the list.

    Three claims are carried by geometry rather than by a sentence:

      · THE TESTES ARE BELOW THE DASHED LINE. The line is labelled *body
        cavity ends*, and 01 sits at y=396 against a boundary at y=330 — the
        testes are outside the body, which is why they are drawn in a pouch
        and why the glands at y=224 are not. `data-boundary="body-cavity"` on
        the line lets a row measure that rather than trust it.
      · THE ORANGE RING IS ON THE OVIDUCT. Fertilisation is marked once, at
        (774, 170), on the right oviduct's arc and nowhere near the uterus at
        (670, 238). The single most common wrong answer in this topic is
        *the uterus*, and the ring exists to be found in the wrong place if
        the drawing ever drifts.
      · THE TWO SYSTEMS ARE NOT MIRROR IMAGES. Three of the nine have no
        counterpart at all, and that is what the filled badge says.

    ⊕ THE FILLED BADGE IS A HOUSE CONVENTION FROM HERE ON. Design invented it
    for this figure and it is adopted as reusable: **a badge drawn solid, with
    its numeral reversed out of the fill, means THIS ONE HAS NO COUNTERPART IN
    THE OTHER SET.** An open badge means it has one. It is stated in words once,
    in the legend along the bottom, and nowhere else — a device explained twice
    is a device the reader has stopped trusting. It carries no colour and it
    never will: the whole distinction is fill versus no fill, so it survives
    greyscale, print, and a reader who cannot separate the accent from the ink.
    The next drawer that needs *this one has no partner* should use this and not
    invent a second device.

    ⚠️ THE FILL IS DERIVED FROM THE MEANING, NOT THE POSITION. `counterpart` is
    a column in `_B5_REPRO_STRUCTURES` and the badge's paint is computed from
    it, once, in one expression. This matters because the three unpaired
    structures happen to be the LAST three in the table and the LAST three in
    the right-hand key column — so a badge whose fill was keyed to its index,
    or to its column position, would render this figure pixel-identically and
    be wrong the moment a tenth structure or a re-order arrived. That is the
    base-pair failure mode exactly: correct on every row you look at, for a
    reason that has nothing to do with the science. `data-counterpart` is on
    every badge and every numeral so a row can assert the fill and the meaning
    agree on all nine, rather than on the first one it finds.

    ⚖️ TWO DIFFERENT RELATIONS LIVE ON THIS PLATE AND THEY ARE NOT THE SAME
    ONE. `data-counterpart` is the badge device above — does the other system
    contain anything corresponding to this. `data-pair="01-05"` is the dashed
    link under the key, which marks the one pairing Design draws as a link:
    testes and ovaries, because both make gametes. Six badges are open and only
    one link is drawn, and that is not a contradiction — a correspondence is
    not a drawn pairing. A gate that conflated the two would report the figure
    broken while it is right.

    ⚠️ THE GREY TUBE INSIDE THE PENIS IS NOT MARKED
    `data-role="no-reproductive-job"`, and the bladder above it is. They are
    the same grey on purpose — Design uses the tone to say *this is the urine
    route* — but the urethra carries semen as well, which is the whole reason
    the male tract has a shared final tube, and marking it as having no
    reproductive job would put a false claim into the markup where a gate would
    then enforce it. `data-role` is on the bladder, its neck, its leader and
    its two label lines: the four things that genuinely have no reproductive
    job and must not be counted among the nine.

    The hooks, and what each is for:

      · `data-structure` / `data-number` / `data-system` — on every element
        belonging to one of the nine: the plate badge, its numeral, its printed
        word, the shape or shapes it names, its leader, and its key row. A row
        can assert there are exactly nine, numbered 01–09, none missing and
        none repeated, by counting `data-badge="key"` or `data-badge="plate"`;
        each set holds nine and the two must agree.
      · `data-badge` / `data-numeral` / `data-word` — "plate" | "key" (and
        "key-job" for the key's function line). These separate the FOUR places
        a number appears, so a count is never ambiguous about which nine it is
        counting.
      · `data-counterpart` — "none" | "paired". On badge circles and numerals
        only, because that is where the device lives: a filled circle must have
        a reversed numeral, and both carry the value that says why.
      · `data-organ` — "drawn" for a shape the number names, "contents" for
        things drawn inside one. ⚠️ PLURAL IS NORMAL HERE AND IS NOT A DEFECT:
        there are two testes, two ovaries, two oviducts and two sperm ducts,
        and each duct is drawn twice over (casing, then lumen). Count by
        `data-structure`, never by element.
      · `data-role="no-reproductive-job"` — the bladder. Design draws it in
        grey and says so in words, and it must not be counted among the nine.
      · `data-boundary="body-cavity"` — the dashed line and its label.
      · `data-marks="fertilisation"` — the ring, its leader, its label, and the
        legend chip that explains it.
      · `data-count` — on each key column heading, so the spelled-out word can
        be checked against the number of badges beneath it.

    ⚠️ ONE LABEL RAISED. Design sets *one pair* at 12px; the kit's floor is 13
    and `_label` refuses below it. Raised to 13. It is anchored middle at x=455
    in the gutter between the two key columns, so it grows symmetrically and
    stays clear of both.
    """
    W, H = 900, 860

    # ⛔ THE TABLE IS CHECKED BEFORE IT IS DRAWN. `_label` catches a blank at
    # the call site, where the message can only name the coordinates; this
    # catches it at the row, where the message can name the structure — and it
    # also catches the two things `_label` cannot see at all: a missing number
    # and a repeated one. The encoding claim is NINE, NUMBERED 01–09, EACH
    # ONCE, so it is asserted in the build and not only in a parity row.
    numbers = [r[0] for r in _B5_REPRO_STRUCTURES]
    if numbers != ["%02d" % i for i in range(1, 10)]:
        raise ValueError(
            "b5-reproductive-systems is numbered %r. The lesson names NINE "
            "structures and the drawing numbers them 01 to 09, each once: the "
            "numbering is the figure's claim, not a caption on it." % numbers)
    for row in _B5_REPRO_STRUCTURES:
        blank = [i for i, v in enumerate(row) if isinstance(v, str)
                 and not v.strip()]
        if blank:
            raise ValueError(
                "structure %r has an empty field at %r. A `<text>` with no "
                "content renders as nothing at all — this figure's nine-row "
                "key came out as nine empty badges exactly that way."
                % (row[0], blank))

    out = [_svg_open(fig, W, H)]

    # Two clips, named off the figure id. ⚠️ A bare `id="f2L"` collides the
    # moment a second figure lands on the same page, and `url(#f2L)` resolves
    # to whichever came first in the document — so one lesson's frame would
    # silently take another's clip rectangle.
    clip_m = "%s-clip-male" % e(fig["id"])
    clip_f = "%s-clip-female" % e(fig["id"])
    out.append(
        '<defs>'
        '<clipPath id="%s"><rect x="24" y="54" width="412" height="440" '
        'rx="18"/></clipPath>'
        '<clipPath id="%s"><rect x="464" y="54" width="412" height="440" '
        'rx="18"/></clipPath>'
        '</defs>' % (clip_m, clip_f))

    # Round caps and joins for the whole drawing, once, as Design set them on
    # her wrapping `<g>`. Every thick stroke here is shaped by them — the 9px
    # duct casings, the 10px oviducts, the 7px bladder neck — so they are
    # geometry, not polish. They are the only presentation attributes on this
    # group; paint stays in `style`, on every element, as the law requires.
    out.append('<g stroke-linecap="round" stroke-linejoin="round">')

    out.append(_mono(24, 40, "MALE SYSTEM · FROM THE FRONT", size=14,
                     weight="400", spacing="1.4", data_system="male"))
    out.append(_mono(464, 40, "FEMALE SYSTEM · FROM THE FRONT", size=14,
                     weight="400", spacing="1.4", data_system="female"))

    out.append(_rect(24, 54, 412, 440, rx=18, fill=_SVG_CARD, stroke=_SVG_INK,
                     w=2.5, data_system="male"))
    out.append(_rect(464, 54, 412, 440, rx=18, fill=_SVG_CARD, stroke=_SVG_INK,
                     w=2.5, data_system="female"))

    # ── the male frame ───────────────────────────────────────────────────
    out.append('<g clip-path="url(#%s)">' % clip_m)

    # The pouch. Drawn first and unnumbered: it is skin, and it is here so that
    # "outside the body cavity" is a place a student can see, not a phrase.
    out.append(_path("M 126,352 C 112,414 146,452 200,447 C 240,444 262,444 "
                     "300,447 C 356,452 386,414 372,352 Z",
                     fill=_SVG_INSET, stroke=_SVG_INK_FAINT, w=2))

    # ⚖️ The boundary. Everything the figure claims about the testes is a claim
    # about which side of this line they are on.
    out.append(_path("M 40,330 H 420", stroke=_SVG_RULE_STRONG, w=2,
                     dash="7 6", data_boundary="body-cavity"))

    # The bladder and its neck. Grey, unnumbered, and hooked as having no
    # reproductive job so a gate can hold it out of the nine.
    out.append(_ellipse(230, 166, 52, 34, fill=_SVG_BAND,
                        stroke=_SVG_INK_FAINT, w=2,
                        data_role="no-reproductive-job"))
    out.append(_path("M 230,200 V 244", stroke=_SVG_INK_GHOST, w=7,
                     data_role="no-reproductive-job"))

    # The sperm ducts: dark casing first, inset lumen over it. Both strokes
    # belong to 02.
    for d in _B5_REPRO_DUCTS:
        out.append(_path(d, stroke=_SVG_INK, w=9, data_structure="sperm-duct",
                         data_number="02", data_system="male",
                         data_organ="drawn"))
    for d in _B5_REPRO_DUCTS:
        out.append(_path(d, stroke=_SVG_INSET, w=4,
                         data_structure="sperm-duct", data_number="02",
                         data_system="male", data_organ="drawn"))

    for cx in (196, 264):
        out.append(_circle(cx, 224, 20, fill=_SVG_BAND, stroke=_SVG_INK,
                           w=2.2, data_structure="glands", data_number="03",
                           data_system="male", data_organ="drawn"))

    # The penis: outline, then the tube down its centre, then the urethra as a
    # grey thread over it. See the docstring on why the grey one is NOT marked
    # as having no reproductive job.
    out.append(_path("M 208,244 V 450 Q 208,474 230,474 Q 252,474 252,450 "
                     "V 244 Z", fill=_SVG_CARD, stroke=_SVG_INK, w=2.5,
                     data_structure="penis", data_number="04",
                     data_system="male", data_organ="drawn"))
    out.append(_path("M 230,248 V 462", stroke=_SVG_BAND, w=9,
                     data_structure="penis", data_number="04",
                     data_system="male", data_organ="drawn"))
    out.append(_path("M 230,248 V 462", stroke=_SVG_INK_GHOST, w=2,
                     data_structure="penis", data_number="04",
                     data_system="male", data_organ="drawn"))

    for cx in (170, 290):
        out.append(_ellipse(cx, 396, 34, 28, fill=_SVG_CARD, stroke=_SVG_INK,
                            w=2.5, data_structure="testes", data_number="01",
                            data_system="male", data_organ="drawn"))
    for d in _B5_REPRO_SCROTUM_TEXTURE:
        out.append(_path(d, stroke=_SVG_INK_FAINT, w=1.6))

    out.append('</g>')

    # Labels sit OUTSIDE the clip, with leaders reaching in. A label clipped to
    # the frame loses its last word to the rounded corner and nothing warns:
    # SVG text simply draws past the box and is cut.
    out.append(_mono(44, 322, "body cavity ends", size=13, weight="400",
                     data_boundary="body-cavity"))

    out.append(_path("M 292,160 L 272,164", stroke=_SVG_INK_FAINT, w=1.4,
                     data_role="no-reproductive-job"))
    # ⊕ MRB-254 · RE-BROKEN AFTER "no", NOT MOVED. The lines were
    # `bladder —` / `no reproductive job`, both end-anchored at 424, and the
    # second one is nineteen mono characters — 148 units — so it began at
    # x≈276. The bladder's right edge is 282 and the leader's tail is 292, so
    # the word ran back over both: the label lay on the organ it names and the
    # leader lay inside the label, which is what the sweep calls a
    # strikethrough. Sixteen characters is 125 units and starts at 299, seven
    # clear of the leader and seventeen clear of the ellipse. The break is
    # ugly to read aloud and it is the only move available: end-anchoring at
    # 424 already leaves twelve units to the frame, so the label cannot go
    # right, and the 13px floor is enforced at source so it cannot shrink.
    out.append(_mono(424, 153, "bladder — no", size=13, weight="400",
                     anchor="end", data_role="no-reproductive-job"))
    out.append(_mono(424, 171, "reproductive job", size=13, weight="400",
                     anchor="end", data_role="no-reproductive-job"))

    out.extend(_repro_systems_plate_badges("male"))

    # ── the female frame ─────────────────────────────────────────────────
    out.append('<g clip-path="url(#%s)">' % clip_f)

    for d in _B5_REPRO_OVIDUCTS:
        out.append(_path(d, stroke=_SVG_INK, w=10, data_structure="oviduct",
                         data_number="06", data_system="female",
                         data_organ="drawn"))
    for d in _B5_REPRO_OVIDUCTS:
        out.append(_path(d, stroke=_SVG_INSET, w=4.5,
                         data_structure="oviduct", data_number="06",
                         data_system="female", data_organ="drawn"))
    for d in _B5_REPRO_FIMBRIAE:
        out.append(_path(d, stroke=_SVG_INK, w=2.2, data_structure="oviduct",
                         data_number="06", data_system="female",
                         data_organ="drawn"))

    # The uterus is drawn AFTER the oviducts so its body covers their roots —
    # the tubes leave the uterus, they do not sit on top of it.
    out.append(_path("M 612,196 Q 616,172 670,172 Q 724,172 728,196 L 700,306 "
                     "Q 694,330 670,330 Q 646,330 640,306 Z",
                     fill=_SVG_CARD, stroke=_SVG_INK, w=3,
                     data_structure="uterus", data_number="07",
                     data_system="female", data_organ="drawn"))
    # The lining, as a thickness inside the wall rather than a line on it.
    out.append(_path("M 628,202 Q 640,188 670,188 Q 700,188 712,202 L 692,300 "
                     "Q 686,316 670,316 Q 654,316 648,300 Z",
                     fill=_SVG_ACCENT_TINT, stroke="none",
                     data_structure="uterus", data_number="07",
                     data_system="female", data_organ="drawn"))

    out.append(_rect(648, 322, 44, 32, rx=9, fill=_SVG_BAND, stroke=_SVG_INK,
                     w=2.5, data_structure="cervix", data_number="08",
                     data_system="female", data_organ="drawn"))
    out.append(_path("M 650,354 L 644,448 Q 644,462 658,462 L 682,462 "
                     "Q 696,462 696,448 L 690,354 Z",
                     fill=_SVG_CARD, stroke=_SVG_INK, w=2.5,
                     data_structure="vagina", data_number="09",
                     data_system="female", data_organ="drawn"))

    for cx in (516, 824):
        out.append(_ellipse(cx, 292, 30, 24, fill=_SVG_CARD, stroke=_SVG_INK,
                            w=2.5, data_structure="ovaries", data_number="05",
                            data_system="female", data_organ="drawn"))
    # The egg cells already present — the fact the key line rests on.
    for cx, cy in _B5_REPRO_EGGS:
        out.append(_circle(cx, cy, 4.5, fill=_SVG_BAND, stroke=_SVG_INK_FAINT,
                           w=1.4, data_structure="ovaries", data_number="05",
                           data_system="female", data_organ="contents"))

    # ⚖️ THE ONE PLACE FERTILISATION IS MARKED. On the right oviduct's arc, at
    # (774, 170) — 68 units above the uterus badge and outside the uterus
    # outline entirely. The ring is the only accent stroke in the drawing.
    out.append(_circle(774, 170, 13, stroke=_SVG_ACCENT, w=3.4,
                       data_marks="fertilisation", data_structure="oviduct",
                       data_number="06", data_system="female"))

    out.append('</g>')

    out.append(_path("M 790,152 L 780,160", stroke=_SVG_ACCENT_TEXT, w=1.4,
                     data_marks="fertilisation"))
    out.append(_mono(866, 146, "fertilisation happens here", size=13,
                     weight="400", anchor="end", fill=_SVG_ACCENT_TEXT,
                     data_marks="fertilisation"))

    out.extend(_repro_systems_plate_badges("female"))

    # ── the shared key ───────────────────────────────────────────────────
    # ⚠️ BOTH HEADINGS AND BOTH RULES FIRST, THEN THE ROWS — Design's own
    # document order, kept even though nothing here overlaps and the render is
    # identical either way. A structural differ compares the element sequence,
    # and a port that reorders a region for the author's convenience makes that
    # differ useless for finding the reorderings that DO change a drawing.
    columns = []
    for system, x0, x1, cx in _B5_REPRO_KEY_COLUMNS:
        rows = [r for r in _B5_REPRO_STRUCTURES if r[2] == system]
        n = len(rows)
        # The heading spells the count of the rows beneath it, so the words and
        # the drawing cannot disagree — remove a structure and the heading
        # follows. Guarded because index 0 of the word list is "", and a blank
        # heading is the failure this figure is on record for.
        if not 1 <= n <= 9:
            raise ValueError(
                "the %s key column holds %d structures. The heading spells the "
                "count in words, and there is no word for that." % (system, n))
        columns.append((system, x0, x1, cx, rows, n))

    for system, x0, _x1, _cx, _rows, n in columns:
        out.append(_mono(x0, 546, "%s STRUCTURES" % _B5_REPRO_COUNT_WORDS[n],
                         size=13, weight="400", spacing="1.2",
                         data_system=system, data_count=n))
    for _system, x0, x1, _cx, _rows, _n in columns:
        out.append(_path("M %d,556 H %d" % (x0, x1), stroke=_SVG_RULE, w=2))

    for system, _x0, _x1, cx, rows, _n in columns:
        for i, (num, slug, _sys, counter, _plate, _word, title,
                job) in enumerate(rows):
            y = _B5_REPRO_KEY_TOP + _B5_REPRO_KEY_STEP * i
            out.extend(_repro_systems_badge(cx, y, num, slug, system, counter,
                                            "key"))
            out.append(_label(cx + 26, y - 1, title, size=18, weight="700",
                              anchor="start", data_structure=slug,
                              data_number=num, data_system=system,
                              data_word="key"))
            out.append(_label(cx + 26, y + 19, job, size=15, weight="400",
                              fill=_SVG_INK_BODY, anchor="start",
                              data_structure=slug, data_number=num,
                              data_system=system, data_word="key-job"))

    # The one pairing drawn as a link — testes to ovaries, both make gametes.
    # NOT the same relation as the badge fill; see the docstring.
    out.append(_path("M 430,588 H 480", stroke=_SVG_INK, w=1.8, dash="6 5",
                     data_pair="01-05"))
    # ⚠️ Design sets this at 12px. Raised to the kit's 13px floor.
    out.append(_mono(455, 574, "one pair", size=13, weight="400",
                     anchor="middle", data_pair="01-05"))

    # ── the legend ───────────────────────────────────────────────────────
    # The two devices, each stated once, in words, on the drawing's own face.
    out.append(_path("M 24,806 H 876", stroke=_SVG_RULE, w=2))
    out.append(_circle(38, 834, 13, fill=_SVG_INK, stroke=_SVG_INK, w=2,
                       data_legend="filled-badge"))
    out.append(_label(60, 840,
                      "A filled badge — nothing in the male system "
                      "corresponds to it",
                      size=16, weight="700", anchor="start",
                      data_legend="filled-badge"))
    out.append(_circle(556, 834, 13, stroke=_SVG_ACCENT, w=3.4,
                       data_legend="fertilisation",
                       data_marks="fertilisation"))
    out.append(_label(578, 840, "The one place fertilisation happens",
                      size=16, weight="400", anchor="start",
                      data_legend="fertilisation",
                      data_marks="fertilisation"))

    out.append('</g>')
    out.append('</svg>')
    return "".join(out)
def _repro_systems_badge(cx, cy, num, slug, system, counterpart, where):
    """One numbered badge: the circle and the numeral reversed out of it.

    ⚖️ THE FILL IS COMPUTED FROM `counterpart` AND FROM NOTHING ELSE. Filled
    means *the other system has no counterpart for this*; the numeral inverts
    to the ground so it stays legible, and both elements carry the value that
    explains the fill. Plate badge and key badge come through this one function
    so the two can never disagree about which three are solid — the failure
    that would look correct on the plate and wrong in the key, or the reverse,
    is not reachable.
    """
    solid = counterpart == "none"
    hooks = dict(data_structure=slug, data_number=num, data_system=system,
                 data_counterpart=counterpart)
    return [
        _circle(cx, cy, _B5_REPRO_BADGE_R,
                fill=_SVG_INK if solid else _SVG_BAND, stroke=_SVG_INK, w=2,
                data_badge=where, **hooks),
        _mono(cx, cy + _B5_REPRO_NUMERAL_DY, num, size=15, weight="400",
              fill=_SVG_GROUND if solid else _SVG_INK, anchor="middle",
              data_numeral=where, **hooks),
    ]
def _repro_systems_plate_badges(system):
    """The badges that sit ON the drawing, for one system: leader, badge,
    numeral, printed word — in Design's order, which puts the leader under the
    badge so the line never crosses the numeral.

    07 alone has no leader: its badge sits inside the uterus it names, so there
    is nothing to reach. That is why a gate must expect EIGHT leaders and nine
    badges, and why `data-leader` is a separate hook rather than an assumed
    companion of `data-badge="plate"`.
    """
    out = []
    for num, slug, sys_, counter, plate, word, _t, _j in _B5_REPRO_STRUCTURES:
        if sys_ != system:
            continue
        leader, cx, cy, wx, wy, anchor = plate
        if leader:
            out.append(_path(leader, stroke=_SVG_INK, w=1.4,
                             data_leader=slug, data_number=num,
                             data_system=sys_))
        out.extend(_repro_systems_badge(cx, cy, num, slug, sys_, counter, "plate"))
        out.append(_label(wx, wy, word, size=15, weight="700", anchor=anchor,
                          data_structure=slug, data_number=num,
                          data_system=sys_, data_word="plate"))
    return out
# ── b5-gametes-journey · five steps, one tract, two of them days apart ──────
#
# THE CLAIM IS SPATIAL AND IT IS NUMERIC AT THE SAME TIME: fertilisation and
# implantation are DIFFERENT PLACES a MEASURED NUMBER OF DAYS APART, on ONE
# tract. Five prose blocks cannot be looked at and found to say that; a map
# numbered along the route can. Every constant below exists so that the two
# halves of the claim — different place, different day — are properties of the
# geometry and of one another, rather than of two sentences free to drift.

# The tract's left half, ONCE. The right half is this mirrored about x = W/2,
# generated rather than spelled, because the two tubes are the same tube and a
# second literal copy is a second thing free to drift: Design's own right-hand
# `d` is her left-hand `d` with every x replaced by 900 − x, exactly, and the
# mirror reproduces it to the digit. Points, not a `d` string, because the same
# points are also flattened to measure arc length — see `_G10_JOURNEY`.
_G10_OVIDUCT = ((376, 224),
                (("C", (320, 186), (250, 182), (220, 216)),
                 ("C", (192, 248), (200, 296), (232, 312))))
# The fringed funnel, as three strokes from the tube's mouth.
_G10_FUNNEL_FROM = (232, 314)
_G10_FUNNEL_TO = ((208, 330), (220, 340), (242, 342))
_G10_OVARY = (196, 352)
# Follicles as OFFSETS from the ovary's centre, so both ovaries carry the same
# four in the same places — the symmetry is drawn once and cannot fall out of
# step on one side only.
_G10_FOLLICLES = ((-10, -6), (6, -10), (-2, 8), (14, 6))
# ⚖️ ONE PATH, BECAUSE IT IS ONE JOURNEY. The caption says "the solid orange
# line is one journey"; a line split into a stretch per step would render
# identically and would have four seams in it, and the seam is the thing this
# figure exists NOT to contain — the misconception is that fertilisation and
# implantation are one event in one place, and the answer is a single
# uninterrupted route that visibly passes through both.
_G10_JOURNEY = ((202, 338),
                (("C", (214, 330), (226, 322), (232, 312)),
                 ("C", (200, 296), (192, 248), (220, 216)),
                 ("C", (250, 182), (320, 186), (376, 224)),
                 ("C", (396, 238), (410, 268), (420, 300)),
                 ("C", (426, 318), (428, 326), (430, 332))))
# The sperm's route in, from 02 up to the meeting point beside 03. Design drew
# the first stretch as `V 420`; it is written as a line to the same point,
# which is the same geometry and lets one flattener measure both routes.
_G10_SPERM = ((450, 516),
              (("L", (450, 420)),
               ("C", (450, 380), (438, 300), (416, 262)),
               ("C", (396, 228), (340, 204), (262, 198))))
# Design's three arrowheads on that route, as she drew them — literal
# triangles, kept to the digit rather than recomputed through `_arrow_head`,
# because `_arrow_head` would place them by angle and hers are placed by eye
# between the dashes. ⛔ They are drawn triangles either way: an arrow is
# never a typed character here or anywhere, the latin subsets do not carry one.
#
# ⊕ MRB-254 · THE THIRD ONE MOVED BACK DOWN THE ROUTE, from 328–344 × 204–216
# to 442–454 × 370–386. It was invisible. Marker 04 is a 15-unit disc centred
# on (341, 205) and it is drawn AFTER the heads, so its card fill covered the
# triangle entirely: the sperm's route lost a third of its direction marks and
# the plate still looked right, because a missing arrowhead leaves nothing
# behind. The sweep found it as geometry rather than as paint — a hairline
# lying wholly inside the numeral "04" — which is the same defect counted from
# the other side.
#
# Nowhere on the upper half of the route will take it. From the corner at
# (416, 262) all the way to 03 the dashed line runs six to ten units from the
# solid orange one, and a head is thirteen across: every seat tried up there
# put a black triangle on the EGG's route, which on a plate whose one job is
# to keep the two journeys apart is a worse fault than the one being fixed.
# Between 05 and head two the line is alone, so that is where it goes — very
# nearly midway between the other two heads, on the stretch where "the sperm
# swim up" is the whole claim. The cost is honest and recorded: the arc from
# 04 to 03 now carries no head at all. It carried none before either; it just
# looked as though it might.
_G10_SPERM_HEADS = ("M 444,462 L 456,462 L 450,448 Z",
                    "M 428,308 L 440,304 L 430,292 Z",
                    "M 454,385 L 442,386 L 446,370 Z")
# The same embryo, drawn three times along the stretch between 03 and 04: one
# cell, then two, then four. (radius, (centres…)) — the count IS the label
# here, so `data-cells` carries it and a parity row can count the circles it
# selects instead of trusting a word.
_G10_DIVIDING = ((4.4, ((272, 194),)),
                 (4.4, ((298, 190), (306, 192))),
                 (4, ((322, 194), (330, 192), (324, 202), (332, 200))))
# Which two markers the dividing happens BETWEEN. It happens while the embryo
# is travelling, not at a stop, and `data-between` says so on every cell.
_G10_DIVIDING_BETWEEN = (3, 4)
# The ball of cells, embedded in the lining at 05.
_G10_BALL = ((424, 326), (434, 324), (428, 336), (438, 334))
# The five steps. Each is
#   (n, cx, cy, route, event, day, place, leader-d, ((x, y, text), …))
#
# ⚠️ `day` IS NOT A STRING HERE AND THE LABEL DOES NOT SPELL ITS OWN NUMBER.
# The two label templates carrying `%(day)s` are filled from this column, and
# `data-day` on the marker comes from the same column, so the printed "day 0"
# and the hook a gate reads are one value. That is the whole defence against
# the failure this figure is most exposed to: a marker moved or renumbered
# while the sentence beside it keeps the old number, which looks entirely
# correct and is the misconception restated.
#
# ⊕ `route` is "egg" or "sperm", and it is load-bearing for the ordering
# assertion. Steps 1, 3, 4 and 5 sit on the orange journey and are strictly
# increasing along it. Step 2 sits on the DASHED route, because the sperm
# start at the far end of the tract and travel up: the five steps are in
# chronological order, and no single drawn line can be monotone in them.
# `data-along` is therefore measured along the route the marker is on, and an
# order check runs per route.
_G10_STEPS = (
    (1, 232, 312, "egg", None, None, None, None,
     ((164, 300, "one egg leaves", "end"),
      (164, 318, "the ovary", "end"))),
    (2, 450, 500, "sperm", None, None, None, None,
     ((496, 498, "semen transferred;", "start"),
      (496, 516, "the sperm swim up", "start"))),
    (3, 249, 198, "egg", "fertilisation", 0, "oviduct", None,
     ((249, 140, "in the oviduct", "middle"),
      (249, 158, "day %(day)s · fertilisation", "middle"))),
    (4, 341, 205, "egg", None, None, None, "M 424,166 L 356,196",
     ((424, 142, "days 1–5 · dividing,", "start"),
      (424, 160, "and still travelling", "start"))),
    (5, 430, 332, "egg", "implantation", 6, "uterus-lining",
     "M 528,336 L 448,336",
     ((536, 330, "about day %(day)s ·", "start"),
      (536, 348, "implantation", "start"))),
)
# The key, bottom of the plate. (n, cx, cy, heading, place-line, place, body)
# `place` repeats the map marker's slug on rows 3 and 5 so the two zones can be
# joined and checked against each other; the other three rows name a movement,
# not a site, and carry none.
_G10_KEY = (
    (1, 38, 700, "Release", "Ovary to oviduct", None,
     "One egg leaves, and can be fertilised for about a day"),
    (2, 38, 760, "Transfer and travel", "Vagina to uterus to oviduct", None,
     "Sperm swim up through the cervix and the uterus"),
    (3, 38, 820, "Fertilisation", "The oviduct — and nowhere else", "oviduct",
     "One sperm nucleus fuses with the egg nucleus. 23 and 23 makes 46"),
    (4, 494, 700, "Dividing", "Travelling down the oviduct", None,
     "Two cells, then four, then eight, over about five days"),
    (5, 494, 760, "Implantation", "The uterus lining", "uterus-lining",
     "The ball of cells embeds where it can be supplied"),
)
# The anatomy words, outside the clip with leaders reaching in.
# (x, y, text, anchor, part, side, leader-d)
_G10_PARTS = (
    (196, 404, "ovary", "middle", "ovary", "left", None),
    (704, 404, "ovary", "middle", "ovary", "right", None),
    (620, 252, "oviduct", "start", "oviduct", "right", "M 616,248 L 596,230"),
    (492, 296, "uterus", "middle", "uterus", None, None),
    (504, 418, "cervix", "start", "cervix", None, "M 500,414 L 480,412"),
    (392, 552, "vagina", "end", "vagina", None, "M 398,548 L 418,542"),
)
# The gap, in words, for the closing line. Indexed by the number of days, so
# the sentence is a function of the two day marks and cannot disagree with
# them. Deliberately short: an index error here is a figure whose two events
# have drifted a week apart, and it should stop the build rather than print.
_G10_GAP_WORDS = ("no", "one", "two", "three", "four", "five", "six", "seven")
def _gametes_journey(fig):
    """The five-step journey mapped on one tract, numbered along the route.

    The lesson's key discrimination is that **fertilisation and implantation
    are different places, days apart**. That is a claim about a map, and prose
    cannot be checked against it: five paragraphs, each correct, leave a
    student free to believe the sperm meets the egg in the uterus and settles
    there — which is the misconception, and it is a misconception about
    geography and about time at once. So the figure puts one tract on the page
    and walks the process across it, and both halves of the discrimination
    become things you can look at and fail to find.

    ⚖️ WHY THE NUMBERS STAY. Design flagged (NOTES-FIGURES §4.4) that the
    lesson says dividing takes "about five days" and implantation is "several
    days later" — a range, not a day — and offered to drop `day 0` and
    `about day 6` for "five or six days later". Ruled: they stay. *Days apart*
    is only checkable against a number; two marks reading "some days" and "some
    days later" restate the vagueness the figure exists to remove. The cost is
    that the figure now asserts a precision the page does not, and the cost is
    paid on purpose.

    ⚠️ ONE WORD OF DESIGN'S IS AMENDED, AND IT IS THE ARITHMETIC. Her closing
    line read *"about five days apart"* under marks reading day 0 and about
    day 6, which is six. Five is the length of the DIVIDING stretch — her 04
    label, "days 1–5", and her key line, "over about five days", are both
    right — and the closing line had taken that number for the gap. The
    sentence is now generated from the two day columns via `_G10_GAP_WORDS`,
    so it prints "six" because the marks say 0 and 6, and no future edit can
    move a mark without moving the word. Reported to the commander as an
    amendment, not made quietly: it is one word and one number, and Mide's
    science gate can put it back with a one-line patch.

    ⛔ THERE IS NO DRAWN DIMENSION BETWEEN 03 AND 05, AND ONE WAS NOT INVENTED.
    A bracket spanning the two markers is a shape Design did not draw, and
    MRB-205 is the rule that stops a port adding furniture. What the drawing
    already contains is better: the orange route runs the whole way from one to
    the other, so the distance between them is an arc along the tract rather
    than a straight line across unrelated organs. `data-along` on every marker
    is that arc, measured off the same point list the path is drawn from, so
    the "runs visibly between them" claim is a subtraction a parity row can do.

    THE HOOKS, AND WHAT EACH EXISTS TO CATCH:

      · `data-step`  — 1…5, on the marker, its numeral, its label lines and its
        key row, with `data-zone` separating the map from the key. Five steps,
        no gaps, no repeats, twice over, and the two zones checkable against
        each other. A renumbered marker whose key row kept the old number is
        the defect, and it is invisible to the eye.
      · `data-route` + `data-along` — which drawn line the marker sits on, and
        how far along it, in user units from that line's start. Steps 1, 3, 4,
        5 must increase along "egg". Step 2 is the only one on "sperm", where
        it sits 16 units from that route's start — the sperm begin at the far
        end and swim up, which is why a single monotone 1-to-5 check would be
        asserting something the science does not say.
      · `data-event` / `data-day` / `data-place` — on the two marked events and
        on the labels that print them. The whole claim reduces to: these two
        rows differ in `place` AND differ in `day`. Both being one place, or
        one day, is the misconception; the figure is built so that both are
        visibly false and mechanically false at the same time.
      · `data-gap-days` — on the closing line, with the two days it was
        computed from beside it, so mark and sentence cannot drift.
      · `data-tract` — on every element of the anatomy, both routes and all
        five markers. "One tract" is half the teaching claim: two events in two
        organs that turned out to be on two different diagrams would prove
        nothing at all.
      · `data-part` — the structure slug, so `data-place="oviduct"` on an event
        names something actually drawn rather than a word nobody rendered.
    """
    W, H = 900, 960
    out = [_svg_open(fig, W, H)]

    # ── measurement: one flattener, both routes ─────────────────────────
    # The `d` that is DRAWN and the polyline that is MEASURED come out of the
    # same tuples. Storing a `d` string and a separate point list would be two
    # descriptions of one line, and `data-along` would go on quietly reporting
    # positions along a path that had been edited out from under it.
    def flatten(route, n=96):
        start, segs = route
        pts = [(float(start[0]), float(start[1]))]
        for seg in segs:
            p0 = pts[-1]
            if seg[0] == "L":
                # ⚠️ SAMPLED, NOT JUST APPENDED. A straight run added as its
                # two endpoints has no interior for a marker to be nearest to,
                # so 02 — which sits sixteen units up a straight stretch of the
                # sperm's route — snapped back to the route's start and
                # reported an arc position of zero. A hook that returns a
                # plausible number for the wrong point is the failure these
                # hooks exist to close, so both segment kinds are sampled at
                # the same rate.
                p1 = (float(seg[1][0]), float(seg[1][1]))
                for i in range(1, n + 1):
                    t = i / float(n)
                    pts.append((p0[0] + (p1[0] - p0[0]) * t,
                                p0[1] + (p1[1] - p0[1]) * t))
                continue
            p1, p2, p3 = seg[1], seg[2], seg[3]
            for i in range(1, n + 1):
                t = i / float(n)
                u = 1.0 - t
                a, b = u * u * u, 3 * u * u * t
                c, dd = 3 * u * t * t, t * t * t
                pts.append((a * p0[0] + b * p1[0] + c * p2[0] + dd * p3[0],
                            a * p0[1] + b * p1[1] + c * p2[1] + dd * p3[1]))
        acc = [0.0]
        for j in range(1, len(pts)):
            acc.append(acc[-1] + math.hypot(pts[j][0] - pts[j - 1][0],
                                            pts[j][1] - pts[j - 1][1]))
        return pts, acc

    def path_d(route):
        start, segs = route
        bits = ["M %s,%s" % (_n(start[0]), _n(start[1]))]
        for seg in segs:
            if seg[0] == "L":
                bits.append("L %s,%s" % (_n(seg[1][0]), _n(seg[1][1])))
            else:
                bits.append("C %s,%s %s,%s %s,%s"
                            % (_n(seg[1][0]), _n(seg[1][1]),
                               _n(seg[2][0]), _n(seg[2][1]),
                               _n(seg[3][0]), _n(seg[3][1])))
        return " ".join(bits)

    def mirror(route):
        """The same tube on the other side. x becomes W − x; y is untouched."""
        start, segs = route
        return ((W - start[0], start[1]),
                tuple((seg[0],) + tuple((W - p[0], p[1]) for p in seg[1:])
                      for seg in segs))

    def along(route_pts_acc, x, y):
        """Arc position of the nearest sampled point on a route, in units."""
        pts, acc = route_pts_acc
        best, bd = 0.0, None
        for j in range(len(pts)):
            dx, dy = pts[j][0] - x, pts[j][1] - y
            d2 = dx * dx + dy * dy
            if bd is None or d2 < bd:
                bd, best = d2, acc[j]
        return "%.1f" % best

    routes = {"egg": flatten(_G10_JOURNEY), "sperm": flatten(_G10_SPERM)}

    # The two events, pulled out of the step table rather than restated, so
    # every downstream number — the gap, the closing line, the step numbers in
    # it — is the step table's own.
    events = dict((s[4], s) for s in _G10_STEPS if s[4])
    fert, impl = events["fertilisation"], events["implantation"]
    gap = impl[5] - fert[5]
    if gap <= 0 or gap >= len(_G10_GAP_WORDS):
        raise ValueError(
            "fertilisation is marked day %s and implantation day %s, a gap of "
            "%s. The whole figure is the claim that these are days apart; a "
            "gap of zero, a negative one, or one this table has no word for "
            "means the marks have moved and the sentence beneath them has "
            "not." % (fert[5], impl[5], gap))
    if fert[6] == impl[6]:
        raise ValueError(
            "fertilisation and implantation are both marked %r. Two different "
            "places is half of what this figure asserts; drawn in one "
            "place it "
            "teaches the misconception it exists to remove." % fert[6])

    sperm_step = [s[0] for s in _G10_STEPS if s[3] == "sperm"][0]

    clip = "%s-clip-plate" % e(fig["id"])
    out.append('<defs><clipPath id="%s">'
               '<rect x="24" y="54" width="852" height="560" rx="18"/>'
               '</clipPath></defs>' % clip)

    # Round caps and joins once, on the wrapping group, exactly as Design set
    # them. The 13px oviduct wall and the 4.4px journey are both shaped by
    # them, so they are geometry rather than polish. Paint stays in `style`, on
    # every element, as the law requires.
    out.append('<g stroke-linecap="round" stroke-linejoin="round">')

    out.append(_rect(24, 54, 852, 560, rx=18, fill=_SVG_CARD, stroke=_SVG_INK,
                     w=2.5))

    out.append('<g clip-path="url(#%s)">' % clip)

    # ── the tract ────────────────────────────────────────────────────────
    # Each oviduct is drawn twice: a thick ink stroke, then a narrower inset
    # stroke inside it. That is what makes the tube a TUBE WITH A LUMEN rather
    # than a line — the egg travels *inside* it, and 03 and 04 are both marked
    # on that inside.
    sides = (("left", _G10_OVIDUCT), ("right", mirror(_G10_OVIDUCT)))
    for w, paint, lumen in ((13, _SVG_INK, None), (7, _SVG_INSET, "1")):
        for side, route in sides:
            out.append(_path(path_d(route), stroke=paint, w=w,
                             data_tract="1", data_part="oviduct",
                             data_side=side, data_lumen=lumen))

    for side, sign in (("left", 1), ("right", -1)):
        fx = _G10_FUNNEL_FROM[0] if sign > 0 else W - _G10_FUNNEL_FROM[0]
        d = " ".join("M %s,%s L %s,%s"
                     % (_n(fx), _n(_G10_FUNNEL_FROM[1]),
                        _n(tx if sign > 0 else W - tx), _n(ty))
                     for tx, ty in _G10_FUNNEL_TO)
        out.append(_path(d, stroke=_SVG_INK, w=2.4, data_tract="1",
                         data_part="funnel", data_side=side))

    out.append(_path("M 372,236 Q 378,196 450,196 Q 522,196 528,236 "
                     "L 496,376 Q 488,404 450,404 Q 412,404 404,376 Z",
                     fill=_SVG_CARD, stroke=_SVG_INK, w=3,
                     data_tract="1", data_part="uterus"))
    # The lining, drawn as a thickness inside the wall. 05 is marked ON this,
    # which is why it is a filled area and not a second outline: "in the
    # uterus lining" is a place with an inside to be in.
    out.append(_path("M 392,244 Q 408,220 450,220 Q 492,220 508,244 "
                     "L 484,368 Q 478,388 450,388 Q 422,388 416,368 Z",
                     fill=_SVG_ACCENT_TINT, stroke="none",
                     data_tract="1", data_part="uterus-lining"))

    out.append(_rect(424, 394, 52, 38, rx=11, fill=_SVG_BAND, stroke=_SVG_INK,
                     w=2.5, data_tract="1", data_part="cervix"))
    out.append(_path("M 428,432 L 420,544 Q 420,560 438,560 L 462,560 "
                     "Q 480,560 480,544 L 472,432 Z",
                     fill=_SVG_CARD, stroke=_SVG_INK, w=2.5,
                     data_tract="1", data_part="vagina"))

    ovaries = (("left", _G10_OVARY), ("right", (W - _G10_OVARY[0],
                                                _G10_OVARY[1])))
    for side, (ox, oy) in ovaries:
        out.append(_ellipse(ox, oy, 34, 27, fill=_SVG_CARD, stroke=_SVG_INK,
                            w=2.5, data_tract="1", data_part="ovary",
                            data_side=side))
    for side, (ox, oy) in ovaries:
        for dx, dy in _G10_FOLLICLES:
            out.append(_circle(ox + dx, oy + dy, 5, fill=_SVG_BAND,
                               stroke=_SVG_INK_FAINT, w=1.4, data_tract="1",
                               data_part="follicle", data_side=side))

    # ── the sperm's route in ─────────────────────────────────────────────
    # Dashed, and it ENDS at the meeting point beside 03. The dash is the whole
    # category distinction — there is no second hue in this figure — and the
    # legend names it in words.
    out.append(_path(path_d(_G10_SPERM), stroke=_SVG_INK, w=3, dash="9 7",
                     data_tract="1", data_route="sperm",
                     data_from_step=sperm_step,
                     data_meets_step=fert[0]))
    for d in _G10_SPERM_HEADS:
        out.append(_path(d, fill=_SVG_INK, data_route="sperm"))

    # ── the journey ──────────────────────────────────────────────────────
    out.append(_path(path_d(_G10_JOURNEY), stroke=_SVG_ACCENT, w=4.4,
                     data_tract="1", data_route="egg"))

    # The same embryo, three times, between 03 and 04. `data-cells` is the
    # count a reader can make of each cluster; `data-between` says which two
    # markers the dividing happens between, which is the point — it happens
    # WHILE TRAVELLING, not at a stop.
    for i, (r, centres) in enumerate(_G10_DIVIDING, 1):
        for cx, cy in centres:
            out.append(_circle(cx, cy, r, fill=_SVG_CARD, stroke=_SVG_INK,
                               w=1.6, data_route="egg", data_cluster=i,
                               data_cells=len(centres),
                               data_between="%d-%d"
                               % _G10_DIVIDING_BETWEEN))

    for cx, cy in _G10_BALL:
        out.append(_circle(cx, cy, 5, fill=_SVG_CARD, stroke=_SVG_INK, w=1.8,
                           data_tract="1", data_event=impl[4],
                           data_place=impl[6], data_cells=len(_G10_BALL)))

    out.append('</g>')

    # ── the five markers ─────────────────────────────────────────────────
    # Outside the clip, so no badge loses an edge to the rounded corner. Each
    # is a ringed circle plus a numeral: the ring is orange, the numeral is
    # ink, and neither carries a fact the other does not — the number is the
    # channel, the colour is emphasis.
    for n, cx, cy, route, event, day, place, leader, lines in _G10_STEPS:
        hooks = dict(data_step=n, data_zone="map", data_tract="1",
                     data_route=route, data_along=along(routes[route], cx, cy),
                     data_event=event, data_day=day, data_place=place)
        if leader:
            out.append(_path(leader, stroke=_SVG_ACCENT_TEXT, w=1.4,
                             data_step=n, data_zone="map"))
        out.append(_circle(cx, cy, 15, fill=_SVG_CARD, stroke=_SVG_ACCENT,
                           w=3, **hooks))
        out.append(_mono(cx, cy + 6, "%02d" % n, size=15, fill=_SVG_INK,
                         weight="400", anchor="middle", **hooks))
        for lx, ly, tmpl, anchor in lines:
            if "%(day)" in tmpl and day is None:
                raise ValueError(
                    "step %s prints a day and has none. A label built from a "
                    "template with no value for it is the `{brace}` hole in "
                    "another costume: it renders, it looks deliberate, "
                    "and the "
                    "number the whole figure turns on is missing." % n)
            out.append(_mono(lx, ly, tmpl % {"day": day} if "%(day)" in tmpl
                             else tmpl,
                             size=13,
                             fill=_SVG_ACCENT_TEXT if event or leader
                             else _SVG_INK_MUTED,
                             weight="400", anchor=anchor, data_step=n,
                             data_zone="map", data_event=event, data_day=day,
                             data_place=place))

    # ── the anatomy, named ───────────────────────────────────────────────
    for x, y, text, anchor, part, side, leader in _G10_PARTS:
        if leader:
            out.append(_path(leader, stroke=_SVG_INK, w=1.4))
        out.append(_label(x, y, text, size=15, weight="700", anchor=anchor,
                          data_tract="1", data_part=part, data_side=side))

    # ── the legend ───────────────────────────────────────────────────────
    # Two lines, two words. This is what pays for the solid/dashed distinction:
    # read once, the drawing stays legible with both strokes in the same ink.
    out.append(_path("M 570,556 h 32", stroke=_SVG_ACCENT, w=4.4,
                     data_route="egg", data_key="legend"))
    out.append(_label(614, 562, "The egg, then the embryo", size=16,
                      weight="700", anchor="start", data_route="egg",
                      data_key="legend"))
    out.append(_path("M 570,590 h 32", stroke=_SVG_INK, w=3, dash="9 7",
                     data_route="sperm", data_key="legend"))
    out.append(_label(614, 596, "The sperm’s route in", size=16, weight="400",
                      anchor="start", data_route="sperm", data_key="legend"))

    # ── the key ──────────────────────────────────────────────────────────
    out.append(_mono(24, 654, "FIVE STEPS, IN ORDER", size=13, weight="400",
                     anchor="start", spacing="1.2"))
    out.append(_path("M 24,666 H 876", stroke=_SVG_RULE, w=2))

    for n, cx, cy, heading, place_line, place, body in _G10_KEY:
        hooks = dict(data_step=n, data_zone="key", data_place=place)
        out.append(_circle(cx, cy, 14, fill=_SVG_CARD, stroke=_SVG_ACCENT,
                           w=3, **hooks))
        out.append(_mono(cx, cy + 6, "%02d" % n, size=15, fill=_SVG_INK,
                         weight="400", anchor="middle", **hooks))
        out.append(_label(cx + 26, cy - 1, heading, size=18, weight="700",
                          anchor="start", **hooks))
        out.append(_mono(cx + 26, cy + 19, place_line, size=13,
                         fill=_SVG_ACCENT_TEXT, weight="400", anchor="start",
                         **hooks))
        out.append(_label(cx + 26, cy + 39, body, size=15,
                          fill=_SVG_INK_BODY, weight="400", anchor="start",
                          **hooks))

    # ── the closing statement ────────────────────────────────────────────
    # The sentence is assembled from the step table: both step numbers, and the
    # gap in words computed from the two day marks. Nothing here is typed
    # twice.
    out.append(_path("M 24,890 H 876", stroke=_SVG_RULE, w=2))
    out.append(_label(24, 920,
                      "%02d and %02d are different events, in different "
                      "organs, about %s days apart."
                      % (fert[0], impl[0], _G10_GAP_WORDS[gap]),
                      size=16, weight="700", anchor="start",
                      data_gap_days=gap, data_from_step=fert[0],
                      data_to_step=impl[0], data_from_day=fert[5],
                      data_to_day=impl[5], data_from_place=fert[6],
                      data_to_place=impl[6]))
    out.append(_label(24, 942,
                      "Fertilisation is one nucleus fusing with another — not "
                      "a sperm arriving. Many arrive; one fuses.",
                      size=15, fill=_SVG_INK_BODY, weight="400",
                      anchor="start"))

    out.append('</g>')
    out.append('</svg>')
    return "".join(out)
# ── b5-dispersal-specimens · eight specimens, one scale, no answers ─────────
#
# ⚖️ THE SCALE IS THE FIGURE. Everything below exists so that "one scale" is a
# measurable property of the geometry and not a sentence printed under it.
#
# The plate's scale, in user units per millimetre, DERIVED from the one
# specimen whose real size is ruled rather than drawn:
#
#     the coconut is 250 mm — the whole fruit, husk and all — and it is drawn
#     380 units wide, so the plate runs at 380 / 250 = 1.52 units per mm.
#
# Design drew the plate at 1.9 and sized the coconut at 200 mm, saying in her
# notes that 200 was HER number and that "the whole plate rescales from it,
# which is a one-line change". The ruling made it 250, because the husk is
# drawn and the husk IS the dispersal mechanism, so the stated dimension has to
# include it. This constant is that one line. The coconut's drawn size does not
# move — it already fills the plate, and it is the fixed point of the rescale —
# so raising its real width lowers the plate's scale by a fifth, and every
# other specimen is redrawn at its own stated width against the new scale.
_B5_DISPERSAL_MM = 380.0 / 250.0
# The ground line every specimen stands on, and the anchor every rescale turns
# about. Design put all eight bottoms on y=470 — the coconut's ellipse bottom,
# the poppy's stem foot, the sycamore's seed — so scaling a specimen about
# (its own station, 470) keeps it standing on the line and centred under its
# numbered badge. Nothing has to be re-placed by hand.
_B5_DISPERSAL_GROUND = 470
# The eight specimens, as
# (slug, number, real width in mm, station x, width Design drew it, in units).
#
# ⚠️ THE mm COLUMN IS A WIDTH, MEASURED ACROSS x, FOR ALL EIGHT. It has to be:
# `data-mm` and `data-drawn-w` are divided by one another to recover the scale,
# and a specimen quoting its LENGTH against a drawn WIDTH would read as a
# different scale and fail a check it should pass. That bites exactly once, on
# the gorse pod: Design's comment says 22 mm, which is a gorse pod's length —
# she drew it 18.75 units across, i.e. 9.9 mm wide at her own 1.9, which is a
# gorse pod's actual width. Her DRAWING is right and her comment is on the
# other axis, so the width column takes 10 and the report says so.
#
# ⊕ The last column is measured off Design's delivery, curves included, not
# copied from her comments — the two disagree by up to 55% (she drew the
# goosegrass 14 mm wide and called it 9). The measurement is what the rescale
# has to divide into, because it is what is actually on the paper.
_B5_DISPERSAL_SPECIMENS = (
    ("goosegrass", 1,   9,  70,  26.682),
    ("dandelion",  2,  14, 125,  21.149),
    ("poppy",      3,  18, 185,  30.000),
    ("blackberry", 4,  20, 248,  38.800),
    ("burdock",    5,  20, 310,  44.000),
    ("gorse",      6,  10, 372,  18.750),
    ("sycamore",   7,  40, 434,  72.276),
    ("coconut",    8, 250, 670, 380.000),
)
# The blackberry's segments, as (cx, cy, r). Design's own cluster, kept as a
# list rather than nine spelled circles because each one carries a pip drawn
# from the same centre — the segment and its pip are one fact, and separating
# them into two hand-written blocks is how a tenth segment ends up pipless.
_B5_DISPERSAL_CLUSTER = (
    (240, 442, 6.4), (252, 439, 6.4), (262, 446, 6.4),
    (236, 452, 6.4), (248, 450, 6.8), (260, 456, 6.4),
    (242, 461, 6.0), (254, 461, 6.0), (248, 432, 5.6),
)
# The key: (number, name, badge x, baseline y). Two columns of four.
#
# ⛔ NAMES ONLY. No structural description, no "the tell", no method. This is
# ruled, and it is the whole figure: a student asked to infer mechanism from
# structure has to be given the structure AS STRUCTURE, and a sentence
# describing hooks set beside a drawing of hooks quietly converts the task back
# into reading comprehension — which is the defect this figure exists to
# remove. The only qualifier here names WHICH PART of a specimen is drawn
# (08, the whole fruit with its husk), because that is what its 250 mm measures
# and it is not a clue to anything.
_B5_DISPERSAL_KEY = (
    (1, "Goosegrass, or cleavers",     38, 662),
    (2, "Dandelion",                   38, 704),
    (3, "Poppy capsule",               38, 746),
    (4, "Blackberry",                  38, 788),
    (5, "Burdock burr",               494, 662),
    (6, "Gorse pod",                  494, 704),
    (7, "Sycamore key",               494, 746),
    (8, "Coconut, whole fruit with husk", 494, 788),
)
def _dispersal(fig):
    """Eight fruits and seeds on one ground line at one scale, numbered, named,
    and told nothing else about themselves.

    The bench page hands the student the structures as PROSE — "hooks that
    catch on fur", "a wing that spins" — and then asks them to infer the
    mechanism. That is the exam skill turned inside out: inference from
    structure becomes reading comprehension, and the student never has to look
    at anything. This plate removes the crutch. Everything a mechanism can be
    read from is DRAWN — the hooks, the pappus, the ring of pores under the
    poppy's rim, the flesh around a hard pip, the wing set off to one side of
    its seed, the fibrous husk full of voids — and nothing is captioned with a
    method. So anything that puts the structure back into words undoes the
    figure, which is why the key names the specimens and stops.

    ⚖️ ONE SCALE, AND THE RANGE IS 250:9. Design's argument, upheld in full.
    Two scales would make the plate a lie — the comparison is the point, and
    the whole reason a coconut is not moved by wind is that it is that size —
    so every specimen is drawn at `_B5_DISPERSAL_MM` units per millimetre and
    the goosegrass comes out 13.7 units across. The cost is a plate with a lot
    of empty paper in it. That emptiness IS the size difference, and it is the
    fact the prose version cannot deliver, so it is kept rather than composed
    away.

    The one thing the scale cannot carry is the goosegrass's hooks, which at
    13.7 units are below the width of the stroke that would have to draw them.
    So there is ONE magnified detail, at ×4, MARKED ×4 on the drawing, tied to
    its specimen by a dashed leader. ⊕ A stated magnification is not a broken
    scale; an unstated one would be. It is drawn ×4 as well as labelled ×4 —
    the dashed frame is exactly four times the specimen's drawn width — so the
    number on the plate is a measurement of the plate rather than a claim about
    it.

    ⚠️ EVERY SPECIMEN IS A GROUP WITH A RESCALE ON IT, NOT A SET OF RETYPED
    COORDINATES. Design's paths are reproduced unit for unit inside the group
    and the group carries `transform="… scale(k) …"` about the specimen's foot
    on the ground line. Two reasons, both of them about being able to check
    this later: her geometry stays diffable against her delivery, and the
    correction each specimen needed to land on the one scale is a single
    readable number instead of being smeared through forty rewritten
    coordinates. Stroke widths scale with the group, which is correct — a
    specimen drawn smaller is drawn thinner.

    Hooks a content-truth row can measure, because the claim that guards the
    250 mm ruling is a claim about DRAWN GEOMETRY:

      · `data-specimen`, `data-mm`, `data-drawn-w` on all eight groups. Walk
        them, divide drawn-w by mm, and every one of the eight lands on 1.52.
        All eight, not the coconut and the goosegrass alone — one scale means
        one scale, and a specimen quietly drawn at its own convenient size is
        invisible to a two-specimen check.
      · `data-magnified` and `data-detail-of` on the goosegrass detail, which
        carries NO `data-specimen` and is therefore excluded from that walk by
        construction. Its own `data-drawn-w` divided by the goosegrass's is 4,
        which is what the printed ×4 says.
      · `data-scale-bar-mm` and `data-scale-bar-px` on the bar, carrying the
        number its label prints and the length it is drawn — separately named
        so the bar cannot wander into the specimen walk.
    """
    W, H = 900, 870
    out = [_svg_open(fig, W, H)]

    def rnd(v):
        """Design's `Math.round(v * 10) / 10`, to the bit.

        ⚠️ NOT Python's `round`, which is banker's rounding and turns
        `Math.round(2.25 * 10) / 10` from 2.3 into 2.2. Half goes UP in JS, and
        towards +∞ for negatives too, which is what `floor(x + 0.5)` is."""
        return math.floor(v * 10 + 0.5) / 10.0

    def hook(cx, cy, angle, r1, r2, curl):
        """Design's `hook()`, ported: a stiff bristle from r1 to r2, then a
        quadratic that turns back on itself. The BACKWARD turn is the whole
        point of a hook and it is generated, not drawn — twenty-two of these
        make the burdock and fourteen make the goosegrass, and hand-drawing
        thirty-six of them is thirty-six chances for one to hook forwards."""
        c, s = math.cos(angle), math.sin(angle)
        x1, y1 = cx + c * r1, cy + s * r1
        x2, y2 = cx + c * r2, cy + s * r2
        hx, hy = x2 - s * curl, y2 + c * curl
        return ("M %s,%s L %s,%s Q %s,%s %s,%s"
                % (_n(rnd(x1)), _n(rnd(y1)), _n(rnd(x2)), _n(rnd(y2)),
                   _n(rnd(hx)), _n(rnd(hy)),
                   _n(rnd(x2 - s * curl * 0.4 - c * curl * 0.8)),
                   _n(rnd(y2 + c * curl * 0.4 - s * curl * 0.8))))

    def scale_about(k, ax, ay):
        """The transform attribute, or nothing at all when k is 1.

        `scale(1)` renders identically and reads as though something happened,
        so the coconut — the one specimen the ruling leaves untouched — gets no
        transform and is visibly the fixed point of the rescale."""
        if abs(k - 1.0) < 1e-9:
            return ""
        return (' transform="translate(%s,%s) scale(%.6f) translate(%s,%s)"'
                % (_n(ax), _n(ay), k, _n(-ax), _n(-ay)))

    scale = {}   # slug -> units per mm correction applied to Design's drawing
    drawn = {}   # slug -> drawn width in user units, after the rescale

    def open_specimen(slug):
        """The group tag for one specimen, with the three hooks on it.

        The hooks go on the GROUP because the group is the specimen: a row that
        put them on the outermost body shape would be measuring the coconut's
        husk wall rather than the coconut, and on the sycamore it would name the
        seed and miss the wing that is four fifths of the width."""
        for s, _num, mm, ax, her_w in _B5_DISPERSAL_SPECIMENS:
            if s != slug:
                continue
            width = mm * _B5_DISPERSAL_MM
            k = width / her_w
            scale[slug] = k
            drawn[slug] = width
            return ('<g data-specimen="%s" data-mm="%s" data-drawn-w="%s"%s>'
                    % (e(slug), _n(mm), _n(width),
                       scale_about(k, ax, _B5_DISPERSAL_GROUND)))
        raise ValueError("no specimen %r on the plate" % slug)

    # ⚠️ The clip id is built off the figure id. A bare `id="f14P"` collides the
    # moment two figures share a page, and `url(#f14P)` then resolves to
    # whichever landed first in the document — so one plate silently takes
    # another's clip rectangle and half a drawing disappears.
    clip = "%s-clip-plate" % e(fig["id"])
    out.append('<defs><clipPath id="%s">'
               '<rect x="24" y="54" width="852" height="520" rx="18"/>'
               '</clipPath></defs>' % clip)

    # Round caps and joins for the whole drawing, once, as Design set them on
    # her single wrapping group. Every bristle tip and every hook turn is
    # shaped by them, so they are geometry here, not polish.
    out.append('<g stroke-linecap="round" stroke-linejoin="round">')

    out.append(_rect(24, 54, 852, 520, rx=18, fill=_SVG_CARD, stroke=_SVG_INK,
                     w=2.5))
    out.append('<g clip-path="url(#%s)">' % clip)

    # ── 08 · coconut, 250 mm, the whole fruit with its husk ───────────────
    # Drawn first and largest, so everything else is laid over its edge rather
    # than under it. Four walls, outside in: husk, husk lining, shell, cavity —
    # and the husk is drawn as a MATERIAL, fibres running through its thickness
    # with voids among them, because the husk is what floats and a husk drawn as
    # an outline would be a claim with nothing behind it.
    out.append(open_specimen("coconut"))
    out.append(_ellipse(670, 299, 190, 171, fill=_SVG_BAND, stroke=_SVG_INK,
                        w=3))
    out.append(_ellipse(670, 299, 150, 133, fill=_SVG_INSET, stroke=_SVG_INK,
                        w=2))
    # 34 fibres and, on every third one, a void. Generated: the husk's texture
    # is a PROPERTY of it, and thirty-four hand-placed strokes would drift into
    # a pattern that means something it does not.
    voids = []
    for i in range(34):
        a = (i / 34.0) * math.pi * 2
        c, s = math.cos(a), math.sin(a)
        out.append(_path("M %s,%s L %s,%s"
                         % (_n(rnd(670 + c * 186)), _n(rnd(299 + s * 167)),
                            _n(rnd(670 + c * 138)), _n(rnd(299 + s * 122))),
                         stroke=_SVG_INK_GHOST, w=1.6))
        if i % 3 == 0:
            t = 0.62 + (i % 2) * 0.14
            voids.append((rnd(670 + c * (150 + 36 * (t - 0.5))),
                          rnd(299 + s * (133 + 32 * (t - 0.5))),
                          3.4 + (i % 4) * 0.6))
    for cx, cy, r in voids:
        out.append(_circle(cx, cy, r, fill=_SVG_CARD, stroke=_SVG_INK_GHOST,
                           w=1.2))
    out.append(_ellipse(670, 299, 134, 118, fill=_SVG_CARD, stroke=_SVG_INK,
                        w=2.8))
    out.append(_ellipse(670, 299, 112, 96, fill=_SVG_INSET, stroke=_SVG_INK,
                        w=1.6))
    out.append(_path("M 566,330 C 606,346 734,346 774,330 C 762,378 720,395 "
                     "670,395 C 620,395 578,378 566,330 Z",
                     fill=_SVG_BAND, stroke=_SVG_INK, w=1.6))
    out.append('</g>')

    # ── 01 · goosegrass, 9 mm, the pair ──────────────────────────────────
    # 13.7 units across, which is the honest size of a 9 mm fruit beside a
    # 250 mm one and is very nearly a dot. It is meant to be. The hooks are
    # generated at full size inside the group and then taken down with it, so
    # what is drawn here is a true small copy rather than a simplified one.
    out.append(open_specimen("goosegrass"))
    out.append(_circle(65, 462, 4.6, fill=_SVG_BAND, stroke=_SVG_INK, w=1.6))
    out.append(_circle(75, 462, 4.6, fill=_SVG_BAND, stroke=_SVG_INK, w=1.6))
    for i in range(7):
        a = (i / 7.0) * math.pi * 2 + 0.3
        out.append(_path(hook(65, 462, a, 4.4, 8.4, 2.2), stroke=_SVG_INK,
                         w=1.2))
        out.append(_path(hook(75, 462, a + 0.45, 4.4, 8.4, 2.2),
                         stroke=_SVG_INK, w=1.2))
    out.append('</g>')

    # ── the ×4 detail ────────────────────────────────────────────────────
    # ⚖️ THE MAGNIFICATION IS DRAWN, NOT ASSERTED. The dashed frame is sized to
    # exactly four times the goosegrass's drawn width, so `data-magnified="4"`,
    # the printed "×4" and the geometry are one number measured three ways.
    # Design drew this frame 80 units across against a specimen she drew 26.7
    # wide — a stated ×4 sitting over an actual ×3.0 — and the rescale is what
    # closes that. It carries no `data-specimen`: it is not a ninth specimen and
    # it must not be walked as one, or the one-scale check finds a ×4 outlier
    # and reports the figure broken for doing exactly what it says it does.
    det_k = (4 * drawn["goosegrass"] / 2.0) / 40.0
    det_bottom = 200 + 40 * det_k
    out.append('<g data-detail-of="goosegrass" data-magnified="4" '
               'data-drawn-w="%s"%s>'
               % (_n(4 * drawn["goosegrass"]), scale_about(det_k, 70, 200)))
    out.append(_circle(70, 200, 40, fill=_SVG_INSET, stroke=_SVG_INK, w=2,
                       dash="6 5"))
    out.append(_circle(60, 204, 15, fill=_SVG_BAND, stroke=_SVG_INK, w=2))
    out.append(_circle(84, 200, 13, fill=_SVG_BAND, stroke=_SVG_INK, w=2))
    for d in ("M 47,192 C 40,186 34,186 32,190 C 31,193 34,195 36,193",
              "M 52,218 C 46,226 42,230 38,229 C 35,228 36,224 39,224",
              "M 95,188 C 102,182 108,182 110,186 C 111,189 108,191 106,189"):
        out.append(_path(d, stroke=_SVG_INK, w=2))
    out.append('</g>')
    # The leader, from the frame down to the specimen it came off. Dashed,
    # because it is a relationship and not a part of either drawing, and it
    # stops six units short of the specimen so the two never touch.
    #
    # ⊕ MRB-254 · IT NOW STARTS SHORT AS WELL AS STOPPING SHORT, at
    # `det_bottom + 26` rather than at `det_bottom`. The printed "×4" is
    # centred on the same x=70 at `det_bottom + 16`, so the dash ran from the
    # frame straight down through the magnification it was carrying — the one
    # number on this plate that a stated scale has to be readable to mean
    # anything. Twenty-six clears the numeral's descender by six and loses
    # nothing: the frame, the "×4" and the dash are now stacked on one axis, so
    # the eye still travels the same line down to the specimen.
    goose_top = (_B5_DISPERSAL_GROUND
                 + (453.6 - _B5_DISPERSAL_GROUND) * scale["goosegrass"])
    out.append(_path("M 70,%s V %s" % (_n(det_bottom + 26), _n(goose_top - 6)),
                     stroke=_SVG_RULE_STRONG, w=1.6, dash="5 5"))

    # ── 02 · dandelion, 14 mm ────────────────────────────────────────────
    # One seed, a stalk, and eleven hairs generated as a fan about the stalk's
    # head — a spray, not a disc, because what is being shown is that the hairs
    # are separate and that there is a great deal of air between them.
    out.append(open_specimen("dandelion"))
    out.append(_ellipse(125, 464, 3.4, 6, fill=_SVG_BAND, stroke=_SVG_INK,
                        w=1.6))
    out.append(_path("M 125,458 V 448", stroke=_SVG_INK, w=1.4))
    for i in range(11):
        a = -math.pi / 2 + (i - 5) * 0.19
        out.append(_path("M 125,448 L %s,%s"
                         % (_n(rnd(125 + math.cos(a) * 13)),
                            _n(rnd(448 + math.sin(a) * 13))),
                         stroke=_SVG_INK, w=1.2))
    out.append('</g>')

    # ── 03 · poppy capsule, 18 mm ────────────────────────────────────────
    # The ring of pores sits UNDER the rim, which is the whole structure: they
    # are drawn as four filled dots below the lid line rather than as notches in
    # the outline, so the capsule stays closed and the seeds have to come out of
    # holes rather than out of a split.
    out.append(open_specimen("poppy"))
    out.append(_path("M 185,470 V 452", stroke=_SVG_INK, w=2))
    out.append(_path("M 171,450 C 171,438 174,428 178,424 L 192,424 "
                     "C 196,428 199,438 199,450 C 199,456 193,459 185,459 "
                     "C 177,459 171,456 171,450 Z",
                     fill=_SVG_BAND, stroke=_SVG_INK, w=2))
    out.append(_path("M 170,428 C 176,424 194,424 200,428", stroke=_SVG_INK,
                     w=2))
    for cx, cy in ((175, 434), (181, 433), (189, 433), (195, 434)):
        out.append(_circle(cx, cy, 1.7, fill=_SVG_INK, stroke="none"))
    out.append('</g>')

    # ── 04 · blackberry, 20 mm ───────────────────────────────────────────
    # Every segment carries one pip, drawn from the segment's own centre. The
    # pip is the seed and the segment is the flesh around it, and the two are
    # generated together for that reason.
    out.append(open_specimen("blackberry"))
    out.append(_path("M 248,470 V 464", stroke=_SVG_INK, w=1.8))
    for cx, cy, r in _B5_DISPERSAL_CLUSTER:
        out.append(_circle(cx, cy, r, fill=_SVG_BAND, stroke=_SVG_INK, w=1.6))
    for cx, cy, _r in _B5_DISPERSAL_CLUSTER:
        out.append(_circle(cx, cy, 2.2, fill=_SVG_CARD, stroke=_SVG_INK,
                           w=1.2))
    out.append('</g>')

    # ── 05 · burdock burr, 20 mm ─────────────────────────────────────────
    # Twenty-two bracts around the whole circumference, every one of them
    # turning back. Generated from the same `hook()` as the goosegrass, which is
    # the point: two specimens that look nothing alike are drawn by one function
    # because they are doing one thing.
    out.append(open_specimen("burdock"))
    out.append(_circle(310, 452, 16, fill=_SVG_BAND, stroke=_SVG_INK, w=2))
    for i in range(22):
        a = (i / 22.0) * math.pi * 2
        out.append(_path(hook(310, 452, a, 15, 22, 3.4), stroke=_SVG_INK,
                         w=1.5))
    out.append('</g>')

    # ── 06 · gorse pod, 10 mm across ─────────────────────────────────────
    # Split along its length and slightly twisted, with the seeds still in it.
    # The split is dashed because it is a line the pod opens ALONG rather than a
    # line drawn on it.
    out.append(open_specimen("gorse"))
    out.append(_path("M 366,470 C 360,450 362,432 372,426 C 382,432 384,450 "
                     "378,470 Z", fill=_SVG_BAND, stroke=_SVG_INK, w=2))
    out.append(_path("M 370,468 C 366,450 368,434 372,428", stroke=_SVG_INK,
                     w=1.5, dash="4 3"))
    for cx, cy in ((371, 440), (373, 450), (371, 460)):
        out.append(_circle(cx, cy, 3, fill=_SVG_CARD, stroke=_SVG_INK, w=1.2))
    out.append('</g>')

    # ── 07 · sycamore key, 40 mm ─────────────────────────────────────────
    # ⚖️ THE WING IS OFF TO ONE SIDE OF THE SEED, not balanced about it. That
    # asymmetry is the entire mechanism — a blade with its mass at one end spins
    # — and a sycamore drawn symmetrically would show a student a thing that
    # falls straight down. The seed sits at 404 and the wing runs out to 467.
    out.append(open_specimen("sycamore"))
    out.append(_ellipse(404, 462, 9, 7.5, fill=_SVG_BAND, stroke=_SVG_INK,
                        w=2))
    out.append(_path("M 411,458 C 428,446 450,424 464,402 C 470,412 468,432 "
                     "456,448 C 444,462 424,466 411,464 Z",
                     fill=_SVG_INSET, stroke=_SVG_INK, w=2))
    out.append(_path("M 413,459 C 430,448 450,428 462,408",
                     stroke=_SVG_INK_GHOST, w=1.4))
    out.append(_path("M 424,462 C 434,450 446,436 454,424 "
                     "M 436,462 C 444,452 452,442 458,432",
                     stroke=_SVG_INK_GHOST, w=1.1))
    out.append('</g>')

    # The ground line, drawn last and over everything, so all eight are
    # standing on one line rather than floating near it.
    out.append(_path("M 44,470 H 856", stroke=_SVG_INK, w=2.5))
    out.append('</g>')

    # The magnification, printed. Accent-text rather than accent: 13px in
    # `--ks3-accent` is 3.4:1 and `_label` refuses it, correctly.
    out.append(_mono(70, det_bottom + 16, "×4", size=13, weight="400",
                     anchor="middle", fill=_SVG_ACCENT_TEXT,
                     data_magnified="4", data_detail_of="goosegrass"))

    # ── the numbered stations ────────────────────────────────────────────
    # Outside the clip, so a badge cannot lose its second digit to the rounded
    # corner. Numbers only — smallest first is a fact about the row, and saying
    # so in eight captions would be the prose this figure exists to remove.
    for slug, num, _mm, ax, _her_w in _B5_DISPERSAL_SPECIMENS:
        out.append(_circle(ax, 496, 13, fill=_SVG_BAND, stroke=_SVG_INK, w=2))
        out.append(_mono(ax, 502, "%02d" % num, size=14, weight="400",
                         anchor="middle", fill=_SVG_INK,
                         data_badge_for=slug))

    # ── the scale bar ────────────────────────────────────────────────────
    # 100 mm, drawn at the plate's own scale, which is what makes it a bar and
    # not a decoration: 100 × 1.52 = 152 units, ten steps of 15.2. Design drew
    # it 190 long for 1.9, and it rescales with everything else — a scale bar
    # left at the old scale is the one error on a plate like this that a reader
    # cannot see and cannot recover from.
    bar_px = 100 * _B5_DISPERSAL_MM
    out.append(_path("M 60,538 H %s" % _n(60 + bar_px), stroke=_SVG_INK,
                     w=2.5, data_scale_bar_mm="100",
                     data_scale_bar_px=_n(bar_px)))
    out.append(_path("M 60,530 V 546 M %s,530 V 546" % _n(60 + bar_px),
                     stroke=_SVG_INK, w=2.5))
    ticks = " ".join("M %s,534 V 542" % _n(60 + bar_px * i / 10.0)
                     for i in range(1, 10))
    out.append(_path(ticks, stroke=_SVG_INK, w=1.6))
    out.append(_mono(60 + bar_px + 16, 544,
                     "100 mm, in 10 mm steps — every specimen on this one "
                     "scale", size=14, weight="400", fill=_SVG_INK,
                     data_scale_bar_mm="100"))

    # ── the key ──────────────────────────────────────────────────────────
    out.append(_mono(24, 614, "EIGHT SPECIMENS · SMALLEST FIRST", size=13,
                     weight="400", spacing="1.2"))
    out.append(_path("M 24,626 H 876", stroke=_SVG_RULE, w=2))
    for num, name, bx, by in _B5_DISPERSAL_KEY:
        out.append(_circle(bx, by, 14, fill=_SVG_BAND, stroke=_SVG_INK, w=2))
        out.append(_mono(bx, by + 6, "%02d" % num, size=15, weight="400",
                         anchor="middle", fill=_SVG_INK))
        out.append(_label(bx + 26, by + 6, name, size=18, weight="700",
                          anchor="start"))
    out.append(_path("M 24,820 H 876", stroke=_SVG_RULE, w=2))
    out.append(_label(24, 848,
                      "Names only. Nothing here says how any of them travels "
                      "— that is what the structure is for.",
                      size=16, weight="700", anchor="start"))

    out.append('</g>')
    out.append('</svg>')
    return "".join(out)
# ── ⊕ MRB-254 · WS1 #13, b5-pollen-tube — Design's fig-13, ported ───────
#
# Every coordinate below is Design's. Her `renderVals()` builds nothing inside
# the SVG — it drives only the Full/768/390 review switcher, which ruling 6
# drops — so there is no `<sc-for>` loop to port and every string in this
# drawing is a literal in her delivery too.

# The sticky pad on top of the stigma. Six dots, composed rather than
# scattered by a generator, so there is no jitter function here and nothing
# can drift run to run.
_POLLEN_TUBE_STICKY = ((252, 126), (268, 118), (286, 122),
                       (264, 140), (284, 142), (316, 132))
# `(cx, cy, index, draws its own nucleus ring)`. The first ovule is the one
# the tube reaches, and its nucleus is drawn as one of the two filled fusion
# dots rather than as the outlined ring the other two carry — which is the
# drawing saying "this one is mid-fertilisation" without a word.
_POLLEN_TUBE_OVULES = ((254, 426, 1, False),
                       (286, 456, 2, True),
                       (318, 486, 3, True))
# Design's pollen tube is ONE `<path>` of three cubic segments. Split here at
# her own segment boundaries so each carries a `data-route-step` — see the
# docstring. The coordinates are untouched: segment n starts exactly where
# segment n-1 ended.
_POLLEN_TUBE_ROUTE = ((2, "M 314,123 C 306,150 288,180 286,220"),
                      (3, "M 286,220 C 284,270 288,330 292,380"),
                      (4, "M 292,380 C 292,396 274,410 260,422"))
# `(numeral, leader, badge cx, badge cy, first caption baseline, line 1,
# line 2)`. The numeral sits at cy + 6; caption line 2 at line 1 + 18.
_POLLEN_TUBE_MARKERS = (
    ("01", "M 344,108 L 334,112", 360, 106, 98,
     "pollination —", "the grain arrives"),
    ("02", "M 344,252 L 308,252", 360, 252, 244,
     "the tube grows down", "through the style"),
    ("03", "M 344,424 L 276,426", 360, 424, 416,
     "fertilisation —", "inside an ovule"),
)
_POLLEN_TUBE_SEEDS = ((690, 368, 1), (720, 404, 2), (750, 440, 3))
# The curled embryo inside a seed, as offsets from the seed's centre. Design
# spells all three out; they are the same seven points translated by (30, 36)
# each time, and writing that once is the only way a fourth seed could not
# quietly arrive with a different embryo in it.
_POLLEN_TUBE_EMBRYO = ((-8, 0), (-8, -6), (-2, -8), (2, -4),
                       (6, 0), (4, 6), (-2, 6))
# The two correspondence lines under the right frame. `(baseline, before
# part, after part, the note under it)`. The shaft sits at baseline - 6, the
# drawn head spans baseline - 12 to baseline, the note at baseline + 22.
_POLLEN_TUBE_BECOMES = (
    (580, "ovule", "seed", "one ovule becomes one seed"),
    (638, "ovary", "fruit", "the wall swells; seeds stay in"),
)
# `(badge cx, badge cy, numeral, heading, accent line, body line)`. Text sits
# at cx + 26; heading at cy - 1, accent at cy + 19, body at cy + 39.
_POLLEN_TUBE_KEY = (
    (38, 760, "01", "Pollen lands",
     "On the stigma — this is pollination",
     "A grain arrives, carried by an insect or the wind"),
    (38, 820, "02", "The pollen tube grows",
     "Down through the style",
     "The male gamete nucleus travels down inside it"),
    (38, 880, "03", "Fertilisation",
     "Inside an ovule — and nowhere else",
     "The two gamete nuclei fuse. That fusion is fertilisation"),
    (494, 760, "04", "Seeds form",
     "From the fertilised ovules",
     "An embryo plant, a food store, and a tough coat"),
    (494, 820, "05", "The fruit forms",
     "From the ovary around them",
     "The ovary wall swells; the rest of the flower withers"),
)
def _pollen_tube(fig):
    """The carpel cut open, before and after: pollen on the stigma, the tube
    down the style, and the fusion happening inside an ovule that never leaves
    the ovary it is drawn in.

    ⚖️ CONTAINMENT IS THE FIGURE, AND IT IS DRAWN RATHER THAN ASSERTED. The
    lesson carries this as a six-row before/after table — *ovule becomes seed,
    ovary becomes fruit, petals fall, style withers* — and a table is six
    things to memorise with nothing holding them together. A student who meets
    it that way routinely comes away believing the ovule travels somewhere to
    become a seed, or that the fruit forms around seeds that arrived from
    outside. Both frames here are the SAME chamber: the ovules sit inside the
    ovary wall on the left, and on the right the seeds sit inside the fruit
    wall, in the same three places on the page. Nothing moves out of anything.
    Put a finger on one ovule and the corresponding seed is under it.

    ⚖️ SO THE CONTAINMENT IS ASSERTABLE FROM THE GEOMETRY, NOT FROM A LABEL.
    Every ovule and every seed carries `data-contains` naming its container,
    and the ovary wall and the fruit wall carry `data-container="1"`; a
    content-truth row resolves the name to the shape and checks the bounding
    boxes. It must walk ALL THREE, in both panels, which is the point: a
    defect that put one of three ovules a few units outside the wall would
    look right at a glance and would be the exact error the figure exists to
    remove. The inner cavity outlines carry `data-cavity="1"` as well, so a
    stricter row can require containment in the cavity rather than merely
    inside the outer wall — both are true of this drawing (measured), and the
    cavity is the claim Design's own `<desc>` makes.

    ⚖️ THE BEFORE-TO-AFTER MAP IS SINGLE-VALUED, AND THAT IS THE SECOND
    HALF OF THE LESSON. Each labelled part in the left panel carries
    `data-becomes-to` and each in the right carries `data-becomes-from`, so a
    row can assert that the map is a function and that it is exactly
    ovule-to-seed and ovary-to-fruit. ⚠️ The map is TOTAL, not just those
    two: stigma and style also map, to `withered-remains`, because they do
    not vanish from the
    drawing — they are the shrivelled stub and the two dried scraps at the top
    of the right frame. Leaving them unhooked would make a row over "every
    part in the before panel" fail on two parts that are drawn correctly.
    `withered-remains` carries no reverse hook, since two parts converge on
    it and the reverse of a many-to-one is not a name.

    ⚖️ THE ROUTE IS NUMBERED FROM THE GRAIN TO THE OVULE. `data-route-step`
    runs 1 to 5: the grain on the stigma, three tube segments, then the two
    fusion dots. Steps 1 and 5 are circles, so a row can test "starts at the
    stigma" and "ends inside an ovule" against bounding boxes without parsing
    a cubic — the grain's centre inside the stigma outline, the fusion dots
    wholly inside ovule 1. That distance is the whole difference between
    pollination and fertilisation, and it is the one thing a table cannot
    show: 01 and 03 are a style's length apart on the page.

    ⊕ DESIGN'S ONE PATH IS THREE HERE, AND NOTHING ELSE ABOUT IT CHANGES. The
    tube is a single `<path>` of three cubics in her delivery; a single
    element cannot carry three step numbers. Split at her own segment
    boundaries, each sub-path starts exactly where the last ended, and the
    root group's `stroke-linecap="round"` closes the joins — a round cap is a
    half-disc centred on the endpoint, and two of them at the same point fill
    the join. Coordinates, paint and width are untouched.

    ⚠️ THE `<desc>` SAYS "MIDDLE OVULE" AND THE DRAWING FERTILISES THE FIRST.
    Her tube ends at (260, 422), inside the ovule at (254, 426) — the
    uppermost of the three, not the middle one at (286, 456). The drawing is
    right and self-consistent (the two fusion dots are drawn in that ovule and
    it is the one without a nucleus ring); it is the sentence that is wrong.
    Amended to "uppermost" in the record and reported: a `<desc>` is the whole
    drawing for a reader who cannot see it, and shipping a known-false one
    because it is Design's is the wrong reading of MRB-205.

    ⚠️ CLIP IDS ARE DERIVED FROM THE FIGURE ID. Hers are `f13L` / `f13R`,
    unique inside a review file holding one figure. `id` is document-scoped
    and a lesson page can hold several drawings; a duplicate `clipPath` id
    silently clips the second figure to the first one's rectangle. Both
    windows are in fact inert — every shape in both groups is comfortably
    inside its frame, measured — but they are kept rather than dropped,
    because they are the guard that keeps a later edit from spilling a
    petal over the frame edge without anyone noticing.

    ⛔ THE TWO ARROWHEADS ARE DESIGN'S OWN TRIANGLES, not `_arrow_head`. She
    placed both by hand on the correspondence lines; `_arrow_head` would
    recompute them from an angle and land them a fraction off her shaft.
    `_arrow` is for a head this file computes; these are hers.
    """
    W, H = 900, 1014
    cid = e(fig["id"])
    out = [_svg_open(fig, W, H)]

    # The two windows. Raw markup rather than an emitter call because a
    # <clipPath> carries no paint — there is no paint law to keep here.
    out.append(
        '<defs>'
        '<clipPath id="%s-c-before"><rect x="24" y="54" width="520" '
        'height="620" rx="18"/></clipPath>'
        '<clipPath id="%s-c-after"><rect x="564" y="54" width="312" '
        'height="620" rx="18"/></clipPath>'
        '</defs>' % (cid, cid))

    # Design's root group. Round caps and joins throughout: the stigma, the
    # ovary and every ovule are organic outlines, and a mitred join on a 3px
    # stroke round a 21-unit ellipse reads as a spike.
    out.append('<g stroke-linecap="round" stroke-linejoin="round">')

    # ── the two frames ──────────────────────────────────────────────────────
    out.append(_mono(24, 44, "THE CARPEL, IN SECTION", size=13, weight="400",
                     spacing="1.2"))
    out.append(_mono(564, 44, "AFTER FERTILISATION", size=13, weight="400",
                     spacing="1.2"))
    out.append(_rect(24, 54, 520, 620, rx=18, fill=_SVG_CARD, stroke=_SVG_INK,
                     w=2.5, data_frame="1", data_state="before"))
    out.append(_rect(564, 54, 312, 620, rx=18, fill=_SVG_CARD, stroke=_SVG_INK,
                     w=2.5, data_frame="1", data_state="after"))

    # ── BEFORE · the carpel in section ──────────────────────────────────────
    out.append('<g clip-path="url(#%s-c-before)">' % cid)

    # The style, drawn in section so both walls are visible: the tube grows
    # DOWN THE INSIDE of it, and a style drawn as a single line would make
    # that impossible to see.
    out.append(_rect(262, 150, 44, 256, fill=_SVG_CARD, stroke="none",
                     data_part="style", data_state="before",
                     data_becomes_to="withered-remains"))
    out.append(_path("M 262,150 V 406", stroke=_SVG_INK, w=2.5,
                     data_part="style", data_state="before",
                     data_wall="left"))
    out.append(_path("M 306,150 V 406", stroke=_SVG_INK, w=2.5,
                     data_part="style", data_state="before",
                     data_wall="right"))

    out.append(_path("M 236,138 C 236,114 258,102 284,102 C 310,102 332,114 "
                     "332,138 C 332,154 310,162 284,162 C 258,162 236,154 "
                     "236,138 Z",
                     fill=_SVG_BAND, stroke=_SVG_INK, w=2.5,
                     data_part="stigma", data_state="before",
                     data_becomes_to="withered-remains"))
    for i, (cx, cy) in enumerate(_POLLEN_TUBE_STICKY, 1):
        out.append(_circle(cx, cy, 2.6, fill=_SVG_ACCENT_TEXT, stroke="none",
                           data_part="stigma", data_state="before",
                           data_sticky=i))

    # The ovary: a wall with a thickness, and a shaded cavity inside it. The
    # thickness is what lets "inside the ovary" be a place rather than a word.
    out.append(_path("M 284,378 C 340,378 368,404 368,452 C 368,500 336,530 "
                     "284,530 C 232,530 200,500 200,452 C 200,404 228,378 "
                     "284,378 Z",
                     fill=_SVG_BAND, stroke=_SVG_INK, w=3,
                     data_part="ovary", data_state="before",
                     data_wall="outer", data_container="1",
                     data_becomes_to="fruit"))
    out.append(_path("M 284,392 C 332,392 356,414 356,452 C 356,490 328,516 "
                     "284,516 C 240,516 212,490 212,452 C 212,414 236,392 "
                     "284,392 Z",
                     fill=_SVG_INSET, stroke=_SVG_INK, w=1.8,
                     data_part="ovary", data_state="before",
                     data_wall="inner", data_cavity="1"))

    # Three ovules, and all three are hooked. One ovule drawn inside the wall
    # and two drawn anywhere would satisfy a spot check and teach the opposite
    # of the lesson.
    for cx, cy, idx, _ring in _POLLEN_TUBE_OVULES:
        out.append(_ellipse(cx, cy, 21, 17, fill=_SVG_BAND, stroke=_SVG_INK,
                            w=2.2, data_part="ovule", data_state="before",
                            data_index=idx, data_contains="ovary",
                            data_becomes_to="seed"))
    for cx, cy, idx, ring in _POLLEN_TUBE_OVULES:
        if not ring:
            continue
        out.append(_circle(cx, cy, 5, fill=_SVG_CARD, stroke=_SVG_INK, w=1.6,
                           data_part="ovule", data_state="before",
                           data_index=idx, data_nucleus="1"))

    # Step 1 of the route: the grain, sitting ON the stigma. Its spikes reach
    # above the pad, so a containment row on this one tests the CENTRE, not
    # the box — the grain has landed on the stigma, it is not inside it.
    out.append(_circle(316, 112, 11, fill=_SVG_ACCENT_TINT,
                       stroke=_SVG_ACCENT_TEXT, w=2, data_grain="1",
                       data_state="before", data_route_step=1,
                       data_route_start="stigma"))
    out.append(_path("M 316,99 V 93 M 327,105 L 332,101 M 329,119 L 334,123 "
                     "M 316,125 V 131 M 305,119 L 300,123 M 303,105 L 298,101",
                     stroke=_SVG_ACCENT_TEXT, w=1.8, data_grain="1",
                     data_state="before"))

    for step, d in _POLLEN_TUBE_ROUTE:
        out.append(_path(d, stroke=_SVG_ACCENT, w=3.6, data_tube="1",
                         data_state="before", data_route_step=step))
    # The male gamete nucleus, part of the way down the tube — the reason the
    # tube is worth drawing at all: something is IN it.
    out.append(_circle(290, 340, 5.2, fill=_SVG_INK, stroke="none",
                       data_tube="1", data_state="before",
                       data_travelling_nucleus="1"))
    # Step 5: the two nuclei, touching, inside ovule 1. Design paints one in
    # the tube's colour and one in ink; she does not label which is which, so
    # neither does the markup.
    out.append(_circle(250, 426, 5.6, fill=_SVG_ACCENT, stroke="none",
                       data_state="before", data_fusion=1,
                       data_route_step=5, data_route_end="ovule",
                       data_route_end_index=1))
    out.append(_circle(261, 429, 5.6, fill=_SVG_INK, stroke="none",
                       data_state="before", data_fusion=2,
                       data_route_step=5, data_route_end="ovule",
                       data_route_end_index=1))

    # The bracket down the left of the chamber: the containment claim, drawn.
    out.append(_path("M 176,392 H 166 V 516 H 176", stroke=_SVG_INK, w=1.8,
                     data_part="ovary", data_state="before",
                     data_annotation="containment"))
    out.append('</g>')

    # ── BEFORE · the words ──────────────────────────────────────────────────
    out.append(_label(216, 134, "stigma", size=15, weight="700", anchor="end",
                      data_part="stigma", data_state="before",
                      data_role="label"))
    out.append(_label(240, 278, "style", size=15, weight="700", anchor="end",
                      data_part="style", data_state="before",
                      data_role="label"))
    out.append(_label(284, 556, "ovary", size=15, weight="700",
                      data_part="ovary", data_state="before",
                      data_role="label"))
    # ⊕ MOVED FROM (286, 461, middle) — Design's own coordinates put this
    # word straight through ovule 2's nucleus ring: the ring lands on the "u"
    # and the letter and the nucleus destroy each other. The rule is the one
    # the villus port used — the thing carrying the science holds its
    # position and the thing carrying none moves — so the ring stays where
    # every ovule's nucleus is (its centre) and the word steps left, ending
    # three units short of the ring on Design's baseline. It stays in the
    # ovary cavity, which is not incidental: a label for a contained part,
    # parked outside its container, works against what this figure says.
    out.append(_label(262, 461, "ovule", size=14, weight="700", anchor="end",
                      data_part="ovule", data_state="before",
                      data_index=2, data_role="label"))
    out.append(_mono(160, 438, "the ovary", size=13, weight="400",
                     anchor="end", data_part="ovary", data_state="before",
                     data_role="note"))
    out.append(_mono(160, 456, "ovules inside it", size=13, weight="400",
                     anchor="end", data_part="ovary", data_state="before",
                     data_role="note"))

    # ── the three numbered markers ──────────────────────────────────────────
    #
    # 01 and 03 are a style's length apart on the page and that gap is the
    # argument: pollination is delivery, fertilisation is fusion, and a table
    # that lists them as two rows gives a student no reason to believe they
    # are not the same moment.
    for num, leader, bx, by, ty, line1, line2 in _POLLEN_TUBE_MARKERS:
        out.append(_path(leader, stroke=_SVG_ACCENT, w=1.4,
                         data_marker=num, data_state="before"))
        out.append(_circle(bx, by, 15, fill=_SVG_CARD, stroke=_SVG_ACCENT,
                           w=3, data_marker=num, data_state="before"))
        out.append(_mono(bx, by + 6, num, size=15, weight="400",
                         anchor="middle", fill=_SVG_INK, data_marker=num,
                         data_state="before"))
        out.append(_mono(536, ty, line1, size=13, weight="400", anchor="end",
                         fill=_SVG_ACCENT_TEXT, data_marker=num,
                         data_state="before"))
        out.append(_mono(536, ty + 18, line2, size=13, weight="400",
                         anchor="end", fill=_SVG_ACCENT_TEXT,
                         data_marker=num, data_state="before"))

    # ── what the two marks in the drawing mean ──────────────────────────────
    out.append(_path("M 60,600 h 30", stroke=_SVG_ACCENT, w=3.6,
                     data_legend="pollen-tube"))
    out.append(_label(102, 606, "The pollen tube — one cell, growing", size=16,
                      weight="700", anchor="start",
                      data_legend="pollen-tube"))
    out.append(_circle(75, 634, 5.2, fill=_SVG_INK, stroke="none",
                       data_legend="gamete-nuclei"))
    out.append(_label(102, 640, "The gamete nuclei, male and female", size=16,
                      weight="400", anchor="start",
                      data_legend="gamete-nuclei"))

    # ── AFTER · the same chamber, swollen ───────────────────────────────────
    out.append('<g clip-path="url(#%s-c-after)">' % cid)

    # What is left of the style and stigma, and two dried scraps of the rest
    # of the flower. Drawn, not omitted: a right-hand frame with nothing above
    # the fruit invites "the flower turned into a fruit", and this is instead
    # the same flower with most of it dead.
    out.append(_path("M 716,300 C 712,290 710,282 712,274 C 718,278 722,286 "
                     "724,298",
                     fill=_SVG_BAND, stroke=_SVG_INK, w=2,
                     data_part="withered-remains", data_state="after",
                     data_index=1))
    out.append(_path("M 682,268 C 668,258 660,246 660,236 C 674,242 684,254 "
                     "690,266 Z",
                     fill=_SVG_BAND, stroke=_SVG_INK_FAINT, w=1.8,
                     data_part="withered-remains", data_state="after",
                     data_index=2))
    out.append(_path("M 758,268 C 772,258 780,246 780,236 C 766,242 756,254 "
                     "750,266 Z",
                     fill=_SVG_BAND, stroke=_SVG_INK_FAINT, w=1.8,
                     data_part="withered-remains", data_state="after",
                     data_index=3))

    # The fruit: the ovary's wall, much thicker, around the same cavity.
    out.append(_path("M 720,300 C 792,300 828,336 828,398 C 828,462 788,502 "
                     "720,502 C 652,502 612,462 612,398 C 612,336 648,300 "
                     "720,300 Z",
                     fill=_SVG_ACCENT_TINT, stroke=_SVG_INK, w=3,
                     data_part="fruit", data_state="after",
                     data_wall="outer", data_container="1",
                     data_becomes_from="ovary"))
    out.append(_path("M 720,322 C 780,322 806,350 806,398 C 806,446 774,480 "
                     "720,480 C 666,480 634,446 634,398 C 634,350 660,322 "
                     "720,322 Z",
                     fill=_SVG_INSET, stroke=_SVG_INK, w=1.8,
                     data_part="fruit", data_state="after",
                     data_wall="inner", data_cavity="1"))

    # Three seeds, in the three places the three ovules occupied. Each is a
    # tough double coat with an embryo curled inside it — the thing the ovule
    # became, not a thing that arrived.
    for cx, cy, idx in _POLLEN_TUBE_SEEDS:
        out.append(_ellipse(cx, cy, 23, 18, fill=_SVG_BAND, stroke=_SVG_INK,
                            w=2.6, data_part="seed", data_state="after",
                            data_index=idx, data_contains="fruit",
                            data_becomes_from="ovule"))
        out.append(_ellipse(cx, cy, 17, 12, fill=_SVG_CARD, stroke=_SVG_INK,
                            w=1.4, data_part="seed", data_state="after",
                            data_index=idx, data_coat="inner"))
        pts = [(cx + dx, cy + dy) for dx, dy in _POLLEN_TUBE_EMBRYO]
        out.append(_path("M %s,%s C %s,%s %s,%s %s,%s C %s,%s %s,%s %s,%s"
                         % tuple(_n(v) for p in pts for v in p),
                         stroke=_SVG_INK, w=2, data_part="seed",
                         data_state="after", data_index=idx,
                         data_embryo="1"))
    out.append('</g>')

    # ── AFTER · the words ───────────────────────────────────────────────────
    # ⊕ MRB-254 · BOTH LINES RAISED 24 — baselines 232 and 250 become 208 and
    # 226, and the leader's tail follows them, from y=254 up to y=230. The
    # right-hand scrap is drawn from y=236 to y=268 across x 750–780, and
    # "withered and fell" — seventeen mono characters back from an end anchor
    # at 864 — occupied 731–864 at y 240–253. The scrap went in one side of the
    # word and out the other: the thing the note names was drawn through the
    # note. Twenty-four units puts the lower line's descender at 229, seven
    # clear of the scrap's tip, and the frame's own top is at 54, so the block
    # still has 150 units of clear paper above it. The leader's HEAD does not
    # move — it is on the scrap, and that is what it is for; only the tail
    # follows the words it leaves from.
    out.append(_mono(864, 208, "the rest of the flower", size=13,
                     weight="400", anchor="end",
                     data_part="withered-remains", data_state="after",
                     data_role="label"))
    out.append(_mono(864, 226, "withered and fell", size=13, weight="400",
                     anchor="end", data_part="withered-remains",
                     data_state="after", data_role="note"))
    out.append(_path("M 796,230 L 776,262", stroke=_SVG_INK_MUTED, w=1.4,
                     data_part="withered-remains", data_state="after",
                     data_leader="1"))
    out.append(_label(720, 536, "the fruit", size=15, weight="700",
                      data_part="fruit", data_state="after",
                      data_role="label"))
    # ⊕ MOVED FROM (720, 409, middle) — the same collision on the right: the
    # word sat on seed 2's curled embryo and neither survived it. Same repair,
    # same direction, and again inside the fruit cavity rather than out of it.
    out.append(_label(692, 409, "seed", size=14, weight="700", anchor="end",
                      data_part="seed", data_state="after", data_index=2,
                      data_role="label"))

    # ── the two correspondences, spelled out under the frame ────────────────
    for base, src, dst, note in _POLLEN_TUBE_BECOMES:
        out.append(_label(588, base, src, size=18, weight="700",
                          anchor="start", data_map="1",
                          data_becomes_from=src, data_becomes_to=dst))
        out.append(_path("M 652,%s H 690" % _n(base - 6), stroke=_SVG_INK,
                         w=2.4, data_map="1", data_becomes_from=src,
                         data_becomes_to=dst))
        # ⛔ Design's own triangle, at her coordinates. Not a typed arrow
        # character, and not a recomputed head.
        out.append(_path("M 688,%s L 700,%s L 688,%s Z"
                         % (_n(base - 12), _n(base - 6), _n(base)),
                         fill=_SVG_INK, stroke="none", data_map="1",
                         data_becomes_from=src, data_becomes_to=dst))
        out.append(_label(710, base, dst, size=18, weight="700",
                          anchor="start", data_map="1",
                          data_becomes_from=src, data_becomes_to=dst))
        out.append(_mono(588, base + 22, note, size=13, weight="400",
                         data_map="1", data_becomes_from=src,
                         data_becomes_to=dst))

    # ── the key: five steps, in order ───────────────────────────────────────
    out.append(_mono(24, 714, "FIVE STEPS, IN ORDER", size=13, weight="400",
                     spacing="1.2"))
    out.append(_path("M 24,726 H 876", stroke=_SVG_RULE, w=2))
    for cx, cy, num, head, accent, body in _POLLEN_TUBE_KEY:
        out.append(_circle(cx, cy, 14, fill=_SVG_CARD, stroke=_SVG_ACCENT,
                           w=3, data_step=num))
        out.append(_mono(cx, cy + 6, num, size=15, weight="400",
                         anchor="middle", fill=_SVG_INK, data_step=num))
        out.append(_label(cx + 26, cy - 1, head, size=18, weight="700",
                          anchor="start", data_step=num))
        out.append(_mono(cx + 26, cy + 19, accent, size=13, weight="400",
                         fill=_SVG_ACCENT_TEXT, data_step=num))
        out.append(_label(cx + 26, cy + 39, body, size=15, weight="400",
                          anchor="start", fill=_SVG_INK_BODY, data_step=num))

    # ── the closing claim ───────────────────────────────────────────────────
    out.append(_path("M 24,946 H 876", stroke=_SVG_RULE, w=2))
    out.append(_label(24, 976,
                      "Pollination is 01. Fertilisation is 03. Between them "
                      "the tube has to grow the whole length of the style.",
                      size=16, weight="700", anchor="start"))
    out.append(_label(24, 998,
                      "Counting the seeds in a fruit counts the ovules that "
                      "were fertilised inside the ovary it grew from.",
                      size=15, weight="400", anchor="start",
                      fill=_SVG_INK_BODY))

    out.append('</g>')
    out.append('</svg>')
    return "".join(out)
# renderers: ═══ END B6 ═══

# renderers: ═══ BEGIN B5 ═══
#
# ── B5 · Reproduction (⊕ MRB-244) ──
#
# Eight instruments, and ALL EIGHT ON INK. Measured off Design's own markup on
# all eight pages — `ks3-block ks3-dark ks3-practical`, no exceptions — which
# is what `ks3_data/b5/__init__.py::_INSTRUMENT_SEGMENTS` records and what
# every colour rule under `/* ═══ BEGIN B5 ═══ */` in `shared/ks3.css` is
# scoped for.
#
# NOTHING IN THIS UNIT ANIMATES, uses a timer, or draws to a canvas. NOTES-B5
# §2 says it of the unit and the eight pages bear it out, so there is no rAF
# tick here to consult `prefers-reduced-motion` inside (MRB-220 R4) — and, by
# the same decision, not one `transition` or `@keyframes` is added by this
# section either. Design's pages animate two things: `[data-arrive]` on a
# panel the runtime is already unhiding, and `[data-scalebar]` on a bar whose
# width never changes after load. Adopting either would create a reduced-motion
# obligation in order to interpolate something no student can see move.
#
# ⚠️ THE PAYLOADS WERE NEVER SCHEMA-CHECKED. The seven surviving lesson
# records were authored against Design's pages while the engine pass that owned
# these renderers was killed by a session limit, so
# `docs/ks3/b5-inventory/PAYLOAD-SCHEMA.md` is written FROM the records rather
# than the other way round. Where records name one idea differently — and four
# of them do — the helpers below accept every spelling that is actually
# authored and the schema document lists the union. Nothing is renamed in
# `ks3_data/`; a concurrent pass owns that tree.

# Design's own template constant on b5-02 and b5-07: the `<strong>` that opens
# the why line under an expanded comparison row. b5-02 authors it as
# `why_label` and b5-07 does not, because on Design's pages it is markup on
# both and data on neither. Lifting it here keeps the two blocks identical —
# which NOTES-B5 §6 requires of them — without inventing a word.
_WHY_LABEL = "Why:"
# ⚖️ THE FOUR CYCLE PHASES ARE A BRANCH, NOT A LIST, and these ids are what
# the branch is written in: day ≤ shed → `shed`; day < release → `build`;
# day = release → `release`; otherwise → `held`. A renamed id is a phase that
# can never show, in silence, so `r_cycle_dial` asserts the set both ways.
_DIAL_PHASES = ("shed", "build", "release", "held")
def _dial_pct(day, length):
    """Where day `n` sits along a `length`-day track, as a percentage.

    Design's own `pct = (n - 0.5) / len * 100`: the marker sits in the MIDDLE
    of its day rather than on the boundary, so day 1 is not flush against the
    left edge and the last day is not off the right.
    """
    return ((day - 0.5) / float(length)) * 100.0
def _dial_phase_at(day, length, shed, luteal):
    """Which of the four phases day `n` falls in. The release day is DERIVED."""
    release = length - luteal
    if day <= shed:
        return "shed"
    if day < release:
        return "build"
    if day == release:
        return "release"
    return "held"
# ── the commit family: five instruments, one chassis ─────────────────────
#
# ⚖️ b5-01, b5-04, b5-05, b5-06 and b5-08 are the SAME BLOCK five times, and
# NOTES-B5 §6 makes the repetition load-bearing rather than incidental:
# "b5-05 reuses b5-04's instrument shape deliberately … If Code refactors
# either one, keep them identical — the repetition is the argument." So they
# share one chassis, one stylesheet namespace and one wire function, and the
# only thing that varies is what Design drew INSIDE the reveal.
#
# Design's five blocks are, in order: tabs → a panel naming the item → a mono
# ask → the options → a check button with a hint beside it → a CREAM panel
# carrying a verdict word, an answer and a why. b5-05 adds a 0–40 week window
# under the why; b5-08 adds the deciding-feature line. Nothing else differs.
#
# ⚖️ EACH ITEM KEEPS ITS OWN PICK AND ITS OWN CHECKED FLAG, and the per-item
# state is in the DOM rather than in the wiring: one option list, one reveal
# and one panel row per item, all but the current one `hidden`. A student who
# checks the testes and moves to the sperm duct finds the duct uncommitted and
# the testes exactly as they left them.
#
# ⚖️ AND THE OPTIONS ARE NOT MARKED (MRB-196 R10, and Design's own pages). A
# chosen option takes the alert border `.ks3-dark .ks3-option[aria-pressed]`
# already gives it and nothing else — no green, no red, no `is-correct`, no
# `is-wrong`, open or not. What names the verdict is a mono eyebrow on the
# cream panel in `--ks3-accent-text`, and it appears whichever way the pick
# went, because the reveal is never withheld for a wrong answer.


def _b5_label(a, act_id, names, what):
    """The first of `names` this payload actually authors.

    ⚠️ THIS EXISTS BECAUSE THE PAYLOADS WERE NEVER SCHEMA-CHECKED, and it is
    not a convenience. Five records author the same handful of ideas under nine
    different key names — `check_label` on b5-01 and b5-05, `reveal_label` on
    b5-06 and b5-08; `options_label` / `options_lead` / `commit_label` /
    `choose_prompt` for the one mono line above the options. Renaming them in
    `ks3_data/` is not this pass's to do, and picking one spelling would fail
    four lessons for a defect that lives in the absent schema rather than in
    the data.

    So: accept every spelling that is authored, and RAISE if none is — a
    missing label is still a missing label. `PAYLOAD-SCHEMA.md` lists the
    accepted set per kind, which is what makes this a documented union rather
    than a shrug.
    """
    for n in names:
        if a.get(n):
            return a[n]
    raise ValueError(
        "%s %r declares no %s. Authored under any one of %s; the payload has "
        "none of them." % (a.get("kind") or "?", act_id, what,
                           ", ".join(map(repr, names))))
def _b5_roles(a, act_id, holders, roles, what):
    """A small map authored under one of several names, read by ROLE.

    `hints` is `{empty, ready, checked}` on b5-01, `{idle, ready, done}` on
    b5-05 and `{idle, ready, opened}` on b5-06 and b5-08 — three spellings of
    one three-state readout, under two container names. `roles` is a tuple of
    accepted-name tuples, one per role, in the order they are returned.
    """
    src = None
    for h in holders:
        if a.get(h):
            src = a[h]
            break
    if not isinstance(src, dict):
        raise ValueError(
            "%s %r declares no %s. Expected a map under one of %s."
            % (a.get("kind") or "?", act_id, what,
               ", ".join(map(repr, holders))))
    out = []
    for names in roles:
        for n in names:
            if src.get(n):
                out.append(src[n])
                break
        else:
            raise ValueError(
                "%s %r's %s names none of %s. Every one of these states is on "
                "screen at some point, and a blank one reads as the instrument "
                "having stopped responding."
                % (a.get("kind") or "?", act_id, what,
                   ", ".join(map(repr, names))))
    return out
def _b5_choices(a, act_id, holders=("choices",)):
    """`[{id, label}, …]` → `[(id, label), …]`, ORDER PRESERVED.

    The order IS the option order on the page and the A/B/C letters follow it,
    so this never sorts.
    """
    src = None
    for h in holders:
        if a.get(h):
            src = a[h]
            break
    if not src:
        raise ValueError(
            "%s %r declares no choice list under %s. These blocks offer the "
            "SAME options for every item, so the list is authored once."
            % (a.get("kind") or "?", act_id, " / ".join(map(repr, holders))))
    out, seen = [], set()
    for c in src:
        if not (c.get("id") and c.get("label")):
            raise ValueError("%s %r choice %r needs both `id` and `label`."
                             % (a.get("kind") or "?", act_id, c.get("id")))
        if c["id"] in seen:
            raise ValueError("%s %r declares choice id %r twice."
                             % (a.get("kind") or "?", act_id, c["id"]))
        seen.add(c["id"])
        out.append((c["id"], c["label"]))
    return out
def _b5_commit(act_id, items, ask, check_label, hints, verdicts):
    """The chassis. `items` is one dict per tab:

        id       the DOM key — tab, panel row, option list and reveal all
                 carry it, and it is what the wiring switches on
        label    the tab's own short label
        name     the panel's display-type heading
        meta     the mono line beside it (system / group / kind / specimen no.)
        context  an optional paragraph under the heading. Design draws one on
                 b5-04, b5-05 and b5-08 and none at all on b5-01 and b5-06
        options  [(key, text), …] in Design's own order
        answer   the key of the correct option
        line     the reveal's display-type answer line
        why      the reveal's reasoning paragraph
        extra    already-rendered HTML appended inside the reveal, or ""

    Everything student-facing arrives already lifted from the record; this
    invents no copy.
    """
    if len(items) < 2:
        raise ValueError(
            "%r offers %d item(s). A commit bench with one item has a tab row "
            "that does nothing and a counter that reads 1 of 1."
            % (act_id, len(items)))

    ids = []
    for it in items:
        if it["id"] in ids:
            raise ValueError("%r declares item id %r twice." % (act_id, it["id"]))
        ids.append(it["id"])
        keys = [k for k, _txt in it["options"]]
        if len(set(keys)) != len(keys):
            raise ValueError(
                "%r item %r offers the same option twice." % (act_id, it["id"]))
        if it["answer"] not in keys:
            raise ValueError(
                "%r item %r answers %r, which is not among the options it "
                "offers %s. Every option would read as the wrong one and the "
                "item would be unanswerable."
                % (act_id, it["id"], it["answer"], keys))

    start = items[0]["id"]

    tabs = "".join(
        '<button type="button" class="ks3-b5c-tab" data-b5c-pick="%s" '
        'aria-pressed="%s">%s</button>'
        % (e(it["id"]), "true" if it["id"] == start else "false", t(it["label"]))
        for it in items)

    # ⚠️ `.ks3-b5c-item` and `.ks3-b5c-opts` are the elements that carry
    # `[hidden]`, and NEITHER takes a `display` declaration in the stylesheet
    # (MRB-242 — an author `display` beats the UA's `[hidden]` rule regardless
    # of specificity, and that defect has now shipped seven times). The flex
    # row INSIDE the item takes one and never carries the attribute: its parent
    # does. And the option list keeps `.ks3-options`, which IS `display: flex`,
    # precisely because it is wrapped in a plain `<div>` that is hidden instead
    # of being hidden itself.
    panels = "".join(
        '<div class="ks3-b5c-item" data-for="%s"%s>'
        '<div class="ks3-b5c-headrow">'
        '<p class="ks3-b5c-name">%s</p>'
        '<p class="ks3-b5c-meta">%s</p></div>%s</div>'
        % (e(it["id"]), "" if it["id"] == start else " hidden",
           t(it["name"]), t(it["meta"]),
           ('<p class="ks3-b5c-context">%s</p>' % rich(it["context"]))
           if it.get("context") else "")
        for it in items)

    options = "".join(
        '<div class="ks3-b5c-opts" data-for="%s"%s><ul class="ks3-options" '
        'role="list">%s</ul></div>'
        % (e(it["id"]), "" if it["id"] == start else " hidden",
           "".join(
               '<li><button type="button" class="ks3-option ks3-b5c-opt" '
               'data-owner="%s" data-opt="%s" aria-pressed="false">'
               '<span class="ks3-opt-mark" aria-hidden="true">%s</span>'
               '<span class="ks3-opt-label">%s</span></button></li>'
               % (e(it["id"]), e(key), t(option_letter(i)), t(txt))
               for i, (key, txt) in enumerate(it["options"])))
        for it in items)

    reveals = "".join(
        '<div class="ks3-b5c-reveal" data-b5c-reveal="%s" data-answer="%s" '
        'hidden><p class="ks3-b5c-word">'
        '<span data-word="right" hidden>%s</span>'
        '<span data-word="wrong" hidden>%s</span></p>'
        '<p class="ks3-b5c-answer">%s</p>'
        '<p class="ks3-b5c-why">%s</p>%s</div>'
        % (e(it["id"]), e(it["answer"]), t(verdicts[0]), t(verdicts[1]),
           t(it["line"]), rich(it["why"]), it.get("extra") or "")
        for it in items)

    # ⚠️ NO `data-check-label`. The button's label is drawn once, in the
    # markup, and the wiring never changes it — Design keeps "Check it" on the
    # button at every state and moves the HINT beside it instead. Shipping the
    # label as an attribute too would be a second copy of a string that nothing
    # reads (R5).
    return ('<div class="ks3-b5c" data-b5c data-total="%d" data-item="%s" '
            'data-hint-idle="%s" data-hint-ready="%s" '
            'data-hint-done="%s">'
            '<div class="ks3-b5c-tabs">%s</div>'
            '<div class="ks3-b5c-panel">%s</div>'
            '<p class="ks3-b5c-ask">%s</p>%s'
            '<div class="ks3-b5c-foot">'
            '<button type="button" class="ks3-reveal-btn ks3-b5c-check" '
            'data-b5c-check disabled>%s</button>'
            '<span class="ks3-b5c-hint" data-b5c-hint role="status">%s</span>'
            '</div>%s</div>'
            % (len(items), e(start), e(hints[0]), e(hints[1]),
               e(hints[2]), tabs, panels, t(ask), options, t(check_label),
               t(hints[0]), reveals))
def r_job_match(a, act_id):
    """⊕ b5-01 `#s-jobs` — eight structures, nine functions, one shared pool.

    ⚖️ EIGHT STRUCTURES, NINE FUNCTIONS, AND THE MISMATCH IS DELIBERATE — so
    this deliberately does NOT assert the bijection `flower-jobs` does. Two of
    the nine belong to organs that are not tabs on this bench (`receive` is the
    vagina's job, and the oviduct owns two of its own), which is exactly what
    the block's prompt warns about: "Only one structure has more than one job,
    and the reveal says which." Asserting one-to-one here would fail Design's
    own approved data, and softening the pool to make it fit would remove the
    asymmetry the whole lesson is built on.

    What IS asserted is that every option offered comes from the declared pool.
    An option outside it is an invented distractor by another route, and the
    pool is the only thing making a wrong guess informative.
    """
    functions = a.get("functions") or []
    if len(functions) < 2:
        raise ValueError(
            "job-match %r declares %d function(s). The options are drawn from "
            "a shared pool, so there has to be a pool."
            % (act_id, len(functions)))
    text = {}
    for f in functions:
        if not (f.get("id") and f.get("text")):
            raise ValueError("job-match %r function %r needs `id` and `text`."
                             % (act_id, f.get("id")))
        if f["id"] in text:
            raise ValueError("job-match %r declares function id %r twice."
                             % (act_id, f["id"]))
        text[f["id"]] = f["text"]

    items = []
    for s in a.get("structures") or []:
        for key in ("id", "label", "name", "system", "func", "answer", "why",
                    "options"):
            if not s.get(key):
                raise ValueError(
                    "job-match %r structure %r is missing %r. `answer` is the "
                    "sentence the reveal leads with and `why` is the reasoning "
                    "under it; one without the other opens a panel that either "
                    "states nothing or explains nothing."
                    % (act_id, s.get("id"), key))
        unknown = [k for k in s["options"] if k not in text]
        if unknown:
            raise ValueError(
                "job-match %r structure %r offers option(s) %s that are not in "
                "the declared function pool. Every option on this bench is "
                "some organ's real job — one from outside the pool is an "
                "invented wrong answer, and a guess then teaches nothing."
                % (act_id, s["id"], unknown))
        if s["func"] not in text:
            raise ValueError(
                "job-match %r structure %r answers %r, which is not in the "
                "function pool." % (act_id, s["id"], s["func"]))
        items.append(dict(
            id=s["id"], label=s["label"], name=s["name"], meta=s["system"],
            options=[(k, text[k]) for k in s["options"]],
            answer=s["func"], line=s["answer"], why=s["why"]))

    return _b5_commit(
        act_id, items,
        ask=_b5_label(a, act_id, ("options_label", "options_lead"),
                      "options label"),
        check_label=_b5_label(a, act_id, ("check_label", "reveal_label"),
                              "check label"),
        hints=_b5_roles(a, act_id, ("hints", "hint"),
                        (("empty", "idle"), ("ready",),
                         ("checked", "opened", "done")), "hints"),
        verdicts=_b5_roles(a, act_id, ("verdicts", "verdict"),
                           (("right",), ("wrong",)), "verdicts"))
def r_flower_jobs(a, act_id):
    """⊕ b5-06 `#s-parts` — nine parts, nine jobs, and here it IS a bijection.

    ⚖️ EVERY DISTRACTOR IS THE CORRECT JOB OF A DIFFERENT PART. NOTES-B5 §2.4
    states it as the rule for this block, and the block's own prompt promises
    it to the student in as many words: "Every wrong option here is the right
    answer for a different part, so a guess still teaches you something." Add
    an invented distractor and that promise becomes false; drop a job and a
    part becomes unanswerable. So this raises unless the mapping is one-to-one
    and onto — which is the difference between this block and b5-01's, where
    the pool deliberately over-runs the tabs.

    ⚠️ THE REVEAL'S ANSWER LINE IS THE JOB'S OWN TEXT, not a per-part
    sentence: Design reads `JOBS[part.answer]`, so a student who picked wrongly
    is shown the right job named in full rather than only being told they were
    wrong. That is the whole reason the reveal is not withheld.
    """
    jobs = a.get("jobs") or {}
    if len(jobs) < 2:
        raise ValueError(
            "flower-jobs %r declares %d job(s). The options are drawn from a "
            "shared pool." % (act_id, len(jobs)))

    parts = a.get("parts") or []
    items, answers = [], []
    for p in parts:
        for key in ("id", "label", "name", "group", "answer", "options", "why"):
            if not p.get(key):
                raise ValueError("flower-jobs %r part %r is missing %r."
                                 % (act_id, p.get("id"), key))
        unknown = [k for k in p["options"] if k not in jobs]
        if unknown:
            raise ValueError(
                "flower-jobs %r part %r offers option(s) %s that are not in "
                "the job pool — an invented distractor (NOTES-B5 §2.4)."
                % (act_id, p["id"], unknown))
        if p["answer"] not in jobs:
            raise ValueError(
                "flower-jobs %r part %r answers %r, which is not a declared "
                "job." % (act_id, p["id"], p["answer"]))
        answers.append(p["answer"])
        items.append(dict(
            id=p["id"], label=p["label"], name=p["name"], meta=p["group"],
            options=[(k, jobs[k]) for k in p["options"]],
            answer=p["answer"], line=jobs[p["answer"]], why=p["why"]))

    # ⚖️ ONE-TO-ONE AND ONTO. Both halves are load-bearing and they fail
    # differently, so they are reported differently.
    if len(jobs) != len(parts):
        raise ValueError(
            "flower-jobs %r offers %d jobs for %d parts. The pool is exactly "
            "the set of the parts' own answers (NOTES-B5 §2.4): a spare job is "
            "an option true of nothing on the flower, and a missing one leaves "
            "a part unanswerable." % (act_id, len(jobs), len(parts)))
    duplicated = sorted({x for x in answers if answers.count(x) > 1})
    if duplicated:
        raise ValueError(
            "flower-jobs %r has job(s) %s answering more than one part. With "
            "nine of each that also means at least one job answers none — the "
            "invented distractor the pool exists to avoid."
            % (act_id, ", ".join(map(repr, duplicated))))

    return _b5_commit(
        act_id, items,
        ask=_b5_label(a, act_id, ("options_lead", "options_label"),
                      "options label"),
        check_label=_b5_label(a, act_id, ("reveal_label", "check_label"),
                              "check label"),
        hints=_b5_roles(a, act_id, ("hints", "hint"),
                        (("idle", "empty"), ("ready",),
                         ("opened", "checked", "done")), "hints"),
        verdicts=_b5_roles(a, act_id, ("verdict", "verdicts"),
                           (("right",), ("wrong",)), "verdicts"))
def r_crossing_bench(a, act_id):
    """⊕ b5-04 `#s-cross` — six substances, and one rule doing all the work.

    ⚖️ THE COMMIT IS A DIRECTION, NOT A YES/NO. Design draws two options,
    "Mother's blood → foetus" and "Foetus → mother's blood", and every answer
    on the bench comes from the same sentence: things move from where there is
    more of them to where there is less. `why` always names the concentration
    difference (NOTES-B5 §2.2), which is what makes the sixth substance
    predictable from the first three.

    ⚠️ `dir` NAMES THE ANSWER AND MAY BE EITHER SPELLING. Design's page stores
    an INDEX (`dir: 0` / `dir: 1`) into a two-element list; NOTES-B5 §2.2 names
    the key without saying which. This accepts an index into the declared
    choices or a choice `id`, because the record that declares it was being
    written by a concurrent pass while this renderer was — and a build that
    died over the spelling of one integer would have parked the unit a second
    time. Both forms are in `PAYLOAD-SCHEMA.md`.

    ⚠️ THIS BLOCK IS b5-05's TWIN ON PURPOSE. NOTES-B5 §6: "b5-05 reuses
    b5-04's instrument shape deliberately … If Code refactors either one, keep
    them identical — the repetition is the argument." They share `_b5_commit`
    for exactly that reason, and the only thing b5-05 adds is the week window.
    """
    choices = _b5_choices(a, act_id, ("choices", "directions"))
    if len(choices) < 2:
        raise ValueError(
            "crossing-bench %r offers %d direction(s). It is a two-way commit "
            "(NOTES-B5 §2.2); a single direction is not a decision."
            % (act_id, len(choices)))
    keys = [k for k, _lab in choices]

    items = []
    for s in a.get("subs") or []:
        for key in ("id", "label", "name", "kind", "context", "answer", "why"):
            if not s.get(key):
                raise ValueError(
                    "crossing-bench %r substance %r is missing %r. `context` "
                    "is the line that makes the direction predictable and "
                    "`why` always names the concentration difference "
                    "(NOTES-B5 §2.2)." % (act_id, s.get("id"), key))
        if "dir" not in s:
            raise ValueError(
                "crossing-bench %r substance %r declares no `dir`, so the "
                "bench has nothing to check the commitment against."
                % (act_id, s.get("id")))
        d = s["dir"]
        if isinstance(d, int) and not isinstance(d, bool):
            if not 0 <= d < len(keys):
                raise ValueError(
                    "crossing-bench %r substance %r has dir %r, which is not "
                    "an index into its %d directions."
                    % (act_id, s["id"], d, len(keys)))
            answer = keys[d]
        else:
            answer = d
        items.append(dict(
            id=s["id"], label=s["label"], name=s["name"], meta=s["kind"],
            context=s["context"], options=list(choices), answer=answer,
            line=s["answer"], why=s["why"]))

    return _b5_commit(
        act_id, items,
        ask=_b5_label(a, act_id,
                      ("commit_label", "options_label", "options_lead",
                       "choose_prompt"), "commit label"),
        check_label=_b5_label(a, act_id, ("check_label", "reveal_label"),
                              "check label"),
        hints=_b5_roles(a, act_id, ("hint", "hints"),
                        (("idle", "empty"), ("ready",),
                         ("done", "opened", "checked")), "hints"),
        verdicts=_b5_roles(a, act_id, ("verdict", "verdicts"),
                           (("right",), ("wrong",)), "verdicts"))
def r_crosses_panel(a, act_id):
    """⊕ b5-05 `#s-cross` — b5-04's bench again, and a week window under it.

    ⚖️ FIVE OF THE SIX CROSS AND ONE DOES NOT, AND THE IMBALANCE IS THE
    TEACHING POINT. NOTES-B5 §2.3: "five of the six cross and one does not.
    That imbalance is the teaching point — the rule is about molecule size — so
    do not 'balance' the set." A student who has met alcohol, carbon monoxide,
    caffeine, rubella and prescribed medicines and then meets insulin has the
    rule handed to them by the exception. Balance the set and the block becomes
    six independent facts, and the placenta starts to look as though it sorts.

    ⚠️ THE WINDOW IS A SECOND CLAIM AND IT IS NOT THE VERDICT. `win` is a
    percentage span across a 0–40 week bar and `win_text` is the sentence that
    reads it. Insulin's is [0, 0] and its sentence says so in words, which is
    why the bar may legitimately draw nothing while the text may never be
    empty.
    """
    choices = _b5_choices(a, act_id)
    if len(choices) != 2:
        raise ValueError(
            "crosses-panel %r offers %d choices. Design draws a yes/no commit."
            % (act_id, len(choices)))
    yes_id, no_id = choices[0][0], choices[1][0]

    window = a.get("window") or {}
    if not (window.get("label") and window.get("ticks")):
        raise ValueError(
            "crosses-panel %r needs `window.label` and `window.ticks`. The "
            "ticks caption the 0–40 week bar, and an uncaptioned bar is a "
            "coloured rectangle." % act_id)
    ticks = "".join("<span>%s</span>" % t(x) for x in window["ticks"])
    # The bar's full span, in the units `win_weeks` is written in. Authored so
    # the conversion is stated once and in the payload rather than assumed at
    # two places in this function.
    weeks_total = float(window.get("weeks_total") or 0)
    if weeks_total <= 0:
        raise ValueError(
            "crosses-panel %r needs `window.weeks_total` — the number of weeks "
            "the bar spans. `win_weeks` is divided by it, so it cannot be "
            "implied." % act_id)

    items, crossing = [], 0
    for s in a.get("subs") or []:
        for key in ("id", "label", "name", "kind", "context", "answer", "why"):
            if not s.get(key):
                raise ValueError("crosses-panel %r substance %r is missing %r."
                                 % (act_id, s.get("id"), key))
        if "crosses" not in s:
            raise ValueError("crosses-panel %r substance %r declares no "
                             "`crosses`." % (act_id, s.get("id")))
        # ⊕ MRB-257 (5.22) — `win` IS IN WEEKS, and that is the fix rather
        # than the two numbers it corrects. It used to be a pair of PERCENTAGES
        # of the 0–40 week bar while every `win_text` beside it is written in
        # WEEKS, so an author had to divide by 0.4 in their head on every row.
        # Two of six were wrong: prescribed medicines drew weeks 2.0–10.0 under
        # "weeks three to eight", and carbon monoxide drew 4.0–40.0 under
        # "mostly the growth half" (weeks 9–40, defined on this page). Both are
        # exactly the arithmetic slip the unit mismatch invites. In weeks the
        # payload reads straight off the sentence: [3, 8] and [9, 40].
        win = s.get("win_weeks")
        if win is None:
            raise ValueError(
                "crosses-panel %r substance %r needs `win_weeks` as "
                "[start, end] IN WEEKS. `win` (percentages of the bar) is "
                "retired: it did not match the units its own caption is "
                "written in, and two of six rows drifted (5.22)."
                % (act_id, s.get("id")))
        win_text = s.get("win_text") or s.get("winText")
        if not (isinstance(win, (list, tuple)) and len(win) == 2):
            raise ValueError(
                "crosses-panel %r substance %r needs `win_weeks` as "
                "[start, end] in weeks." % (act_id, s.get("id")))
        if not win_text:
            raise ValueError(
                "crosses-panel %r substance %r declares no `win_text`. Insulin "
                "draws an empty bar and its sentence is the only thing that "
                "says why, so a blank one is not a legitimate empty state."
                % (act_id, s.get("id")))
        w_lo, w_hi = float(win[0]), float(win[1])
        if not 0 <= w_lo <= w_hi <= weeks_total:
            raise ValueError(
                "crosses-panel %r substance %r has win_weeks %r, which is not "
                "a 0–%g week span in order."
                % (act_id, s["id"], list(win), weeks_total))
        lo = w_lo / weeks_total * 100.0
        hi = w_hi / weeks_total * 100.0
        if s["crosses"]:
            crossing += 1
        extra = ('<div class="ks3-b5c-window">'
                 '<p class="ks3-b5c-winlabel">%s</p>'
                 '<div class="ks3-b5c-wintrack">'
                 '<span class="ks3-b5c-winfill" aria-hidden="true" '
                 'style="left:%s%%;width:%s%%"></span></div>'
                 '<div class="ks3-b5c-winticks">%s</div>'
                 '<p class="ks3-b5c-wintext">%s</p></div>'
                 % (t(window["label"]), _pctnum(lo), _pctnum(hi - lo), ticks,
                    rich(win_text)))
        items.append(dict(
            id=s["id"], label=s["label"], name=s["name"], meta=s["kind"],
            context=s["context"], options=list(choices),
            answer=yes_id if s["crosses"] else no_id,
            line=s["answer"], why=s["why"], extra=extra))

    # ⚖️ NEVER BALANCE THE SET (NOTES-B5 §2.3). Both failure directions are
    # named because they are different mistakes: an all-crossing set has no
    # exception to prove the rule with, and a balanced one turns "it is about
    # size" into "it is about which half of the list you are on".
    if crossing == len(items):
        raise ValueError(
            "crosses-panel %r has every substance crossing. The rule is about "
            "molecule size and insulin is what proves it — a set with no "
            "exception cannot make the argument (NOTES-B5 §2.3)." % act_id)
    if crossing * 2 == len(items):
        raise ValueError(
            "crosses-panel %r splits %d/%d. The imbalance IS the teaching "
            "point: most things cross, and the one that does not is a large "
            "protein. A balanced set teaches that the placenta sorts."
            % (act_id, crossing, len(items) - crossing))

    return _b5_commit(
        act_id, items,
        ask=_b5_label(a, act_id,
                      ("commit_label", "options_label", "choose_prompt"),
                      "commit label"),
        check_label=_b5_label(a, act_id, ("check_label", "reveal_label"),
                              "check label"),
        hints=_b5_roles(a, act_id, ("hint", "hints"),
                        (("idle", "empty"), ("ready",),
                         ("done", "opened", "checked")), "hints"),
        verdicts=_b5_roles(a, act_id, ("verdict", "verdicts"),
                           (("right",), ("wrong",)), "verdicts"))
def r_disperse_sort(a, act_id):
    """⊕ b5-08 `#s-sort` — eight specimens, five methods, structure only.

    ⚖️ THE DESCRIPTIONS NAME STRUCTURE AND NOTHING ELSE. NOTES-B5 §2.6: the
    specimens "are described by structure only and never pictured or named in
    the description text, so the sort has to be done on evidence". The TAB
    carries the plant's name, because a student has to be able to come back to
    one; the DESCRIPTION may not, or the classifying becomes a memory test.
    This raises if a specimen's own name appears inside its description.

    ⚖️ AND THE HARD CASE IS NOT SOFTENED. Three of the eight are wind-
    dispersed and one of those three — the poppy — has neither wing nor
    parachute. That is the block's argument, and it is why the deciding
    feature gets a line of its own in the reveal rather than a clause inside
    the why: the observable that settles it IS the thing being taught.

    ⚠️ THE SPECIMEN NUMBER IS DERIVED FROM POSITION, exactly as Design derives
    it (`String(idx + 1).padStart(2, '0')`). Authoring it would be a second
    source of truth for a list's own order.
    """
    choices = _b5_choices(a, act_id, ("choices", "methods"))
    if len(choices) < 3:
        raise ValueError(
            "disperse-sort %r offers %d method(s). A classification with two "
            "boxes is a yes/no question." % (act_id, len(choices)))
    labels = dict(choices)

    tell_label = _b5_label(a, act_id, ("tell_label",), "deciding-feature label")
    spec_label = _b5_label(a, act_id, ("specimen_label",), "specimen label")

    items, used = [], set()
    for i, s in enumerate(a.get("specimens") or []):
        for key in ("id", "label", "name", "answer", "desc", "tell", "why"):
            if not s.get(key):
                raise ValueError(
                    "disperse-sort %r specimen %r is missing %r. `tell` is the "
                    "observable that settles it and is a line of its own in "
                    "the reveal (NOTES-B5 §2.6)."
                    % (act_id, s.get("id"), key))
        if s["answer"] not in labels:
            raise ValueError(
                "disperse-sort %r specimen %r answers %r, which is not one of "
                "the methods offered %s."
                % (act_id, s["id"], s["answer"], sorted(labels)))
        low = s["desc"].lower()
        for word in (s["label"], s["name"]):
            first = str(word).split()[0].strip(",.").lower()
            if len(first) > 3 and first in low:
                raise ValueError(
                    "disperse-sort %r specimen %r names itself (%r) inside its "
                    "description. The specimens are described by STRUCTURE "
                    "only (NOTES-B5 §2.6) — naming the plant turns a "
                    "classification on evidence into a recall question."
                    % (act_id, s["id"], first))
        used.add(s["answer"])
        items.append(dict(
            id=s["id"], label=s["label"], name=s["name"],
            meta="%s %02d" % (spec_label, i + 1), context=s["desc"],
            options=list(choices), answer=s["answer"],
            line=labels[s["answer"]], why=s["why"],
            extra='<p class="ks3-b5c-tell">'
                  '<span class="ks3-b5c-telllabel">%s</span>%s</p>'
                  % (t(tell_label), t(s["tell"]))))

    unused = sorted(set(labels) - used)
    if unused:
        raise ValueError(
            "disperse-sort %r offers method(s) %s that no specimen is sorted "
            "into. An empty box is an option true of nothing on the bench."
            % (act_id, ", ".join(map(repr, unused))))

    return _b5_commit(
        act_id, items,
        ask=_b5_label(a, act_id, ("choose_prompt", "options_label"),
                      "choose prompt"),
        check_label=_b5_label(a, act_id, ("reveal_label", "check_label"),
                              "check label"),
        hints=_b5_roles(a, act_id, ("hints", "hint"),
                        (("idle", "empty"), ("ready",),
                         ("opened", "checked", "done")), "hints"),
        verdicts=_b5_roles(a, act_id, ("verdicts", "verdict"),
                           (("right",), ("wrong",)), "verdicts"))
# ── the comparison-row family: two instruments, one chassis ──────────────


def _b5_compare(act_id, rows, head, lead, why_label, tail=""):
    """b5-02's and b5-07's shared table.

    `head` is (row-name column, column A, column B); `lead` is 0 or 1 and says
    which DATA column Design paints in the alert.

    ⚖️ THE WHOLE ROW IS THE BUTTON. NOTES-B5 §2.5 states it for b5-07 — "the
    whole row is the button, as in `gamete-compare`. No separate chevron
    control" — and b5-02 is the block it points at. So the `<button>` wraps all
    three cells rather than sitting beside them, and the tap target spans the
    row's full width on a phone.

    ⚠️ THE PER-CELL CAPTIONS ARE REAL ELEMENTS, NOT GENERATED CONTENT. Below
    880px Design drops the header row and shows a caption inside each cell
    instead. Those captions are what a screen reader reads at EVERY width, so
    they ship in the markup and the media query only decides which of the two
    is visible — `content:` on a pseudo-element is not reliably announced.
    """
    if len(rows) < 2:
        raise ValueError(
            "%r declares %d row(s). A comparison needs something to compare."
            % (act_id, len(rows)))
    ids = []
    for r in rows:
        if r["id"] in ids:
            raise ValueError("%r declares row id %r twice." % (act_id, r["id"]))
        ids.append(r["id"])

    def cell(idx, value):
        return ('<span class="ks3-cmp-cell"%s>'
                '<span class="ks3-cmp-cap">%s</span>'
                '<span class="ks3-cmp-val">%s</span></span>'
                % (" data-lead" if idx == lead else "", t(head[idx + 1]),
                   t(value)))

    # ⚠️ THE ZEBRA IS AN ATTRIBUTE, NOT `:nth-child`. The header shares the
    # table's element list, so a positional selector counts it and shades the
    # wrong half — and it would go on being wrong quietly if the header ever
    # moved. Design alternates on the ROW's own index; so does this.
    body = "".join(
        '<div class="ks3-cmp-row" data-cmp-row="%s"%s>'
        '<button type="button" class="ks3-cmp-btn" data-cmp-open="%s" '
        'aria-pressed="false"><span class="ks3-cmp-grid">'
        '<span class="ks3-cmp-name">%s</span>%s%s</span></button>'
        '<p class="ks3-cmp-why" data-cmp-why="%s" hidden>'
        '<span class="ks3-cmp-whylabel">%s</span> %s</p></div>'
        % (e(r["id"]), " data-alt" if i % 2 else "", e(r["id"]), t(r["name"]),
           cell(0, r["a"]), cell(1, r["b"]), e(r["id"]), t(why_label),
           rich(r["why"]))
        for i, r in enumerate(rows))

    return ('<div class="ks3-cmp" data-cmprows data-total="%d">'
            '<div class="ks3-cmp-table">'
            '<div class="ks3-cmp-head"><span class="ks3-cmp-grid">'
            '<span class="ks3-cmp-name">%s</span>'
            '<span class="ks3-cmp-cell"%s><span class="ks3-cmp-val">%s</span>'
            '</span><span class="ks3-cmp-cell"%s>'
            '<span class="ks3-cmp-val">%s</span></span></span></div>%s</div>%s'
            '</div>'
            % (len(rows), t(head[0]),
               " data-lead" if lead == 0 else "", t(head[1]),
               " data-lead" if lead == 1 else "", t(head[2]),
               body, tail))
def r_gamete_compare(a, act_id):
    """⊕ b5-02 `#s-compare` — six features of two cells, and a why behind each.

    ⚖️ THE ROW WHERE THEY ARE IDENTICAL IS WHY THIS IS A TABLE AND NOT A LIST
    OF DIFFERENCES. Both cells carry 23 chromosomes, and that row is what makes
    "half a set" mean anything at all. Nothing here reorders or drops rows.

    ⚠️ THE SCALE BARS ARE DIAMETERS, AND THE NOTE DOES THE ARITHMETIC THEY
    CANNOT. `pct` is a percentage of the widest bar; drawing them by volume
    would make the sperm bar invisible and would contradict the note under
    them, which is where the eight-thousandfold figure lives.
    """
    columns = a.get("columns") or {}
    for key in ("feature", "sperm", "egg"):
        if not columns.get(key):
            raise ValueError("gamete-compare %r columns is missing %r."
                             % (act_id, key))

    # ⚖️ MRB-208 — NOTHING IS TICKED ON LOAD, and this block's stop is all six
    # rows opened. A row open at build time is a rail stage part-completed
    # before the student arrived, so the flag is read and refused rather than
    # ignored.
    if a.get("rows_open_on_load"):
        raise ValueError(
            "gamete-compare %r sets rows_open_on_load. MRB-208: nothing is "
            "ticked on load, and this block's stop ticks on all six rows "
            "opened — so opening any at build time completes part of a stage "
            "the student has not touched." % act_id)

    rows = []
    for r in a.get("rows") or []:
        for key in ("id", "name", "sperm", "egg", "why"):
            if not r.get(key):
                raise ValueError(
                    "gamete-compare %r row %r is missing %r. The `why` is the "
                    "reason the row exists — a difference with no reason "
                    "behind it is the list this block replaced."
                    % (act_id, r.get("id"), key))
        rows.append(dict(id=r["id"], name=r["name"], a=r["sperm"], b=r["egg"],
                         why=r["why"]))

    scale = a.get("scale") or {}
    tail = ""
    if scale:
        for key in ("label", "rows", "note"):
            if not scale.get(key):
                raise ValueError("gamete-compare %r scale is missing %r."
                                 % (act_id, key))
        bars = "".join(
            '<li class="ks3-cmp-scalerow">'
            '<div class="ks3-cmp-scalehead">'
            '<p class="ks3-cmp-scalename">%s</p>'
            '<p class="ks3-cmp-scalesize">%s</p></div>'
            '<span class="ks3-cmp-scaletrack">'
            '<span class="ks3-cmp-scalebar"%s style="width:%s%%"></span>'
            '</span></li>'
            % (t(s["name"]), t(s["size"]), " data-lead" if i else "",
               _pctnum(float(s["pct"])))
            for i, s in enumerate(scale["rows"]))
        tail = ('<div class="ks3-cmp-scale">'
                '<p class="ks3-cmp-scalelabel">%s</p>'
                '<ul class="ks3-cmp-scalelist" role="list">%s</ul>'
                '<p class="ks3-cmp-scalenote">%s</p></div>'
                % (t(scale["label"]), bars, rich(scale["note"])))

    return _b5_compare(
        act_id, rows,
        head=(columns["feature"], columns["sperm"], columns["egg"]), lead=0,
        why_label=a.get("why_label") or _WHY_LABEL, tail=tail)
def r_what_it_becomes(a, act_id):
    """⊕ b5-07 `#s-becomes` — six parts, before and after, and why.

    ⚖️ THE LEAD COLUMN IS *AFTER*, WHERE b5-02's IS THE FIRST. Design paints
    the column the lesson is about in the alert, and on this page that is what
    each part turns into. Mirroring b5-02's arrangement would put the emphasis
    on the flower that no longer exists.

    ⚖️ AND NOTHING IS OPEN ON LOAD. NOTES-B5 §2.5 authors `open: {}` as the
    starting state, and the stop is all six rows opened — so a row open at
    build time is a stage part-completed before the student arrived (MRB-208).
    """
    table = a.get("table") or {}
    for key in ("name", "before", "after"):
        if not table.get(key):
            raise ValueError("what-it-becomes %r table is missing %r."
                             % (act_id, key))

    if a.get("rows_open_on_load") or a.get("open"):
        raise ValueError(
            "what-it-becomes %r opens a row at build time. MRB-208: nothing "
            "is ticked on load, and this block's stop is all six rows opened."
            % act_id)

    rows = []
    for r in a.get("rows") or []:
        for key in ("id", "name", "before", "after", "why"):
            if not r.get(key):
                raise ValueError("what-it-becomes %r row %r is missing %r."
                                 % (act_id, r.get("id"), key))
        rows.append(dict(id=r["id"], name=r["name"], a=r["before"],
                         b=r["after"], why=r["why"]))

    return _b5_compare(
        act_id, rows,
        head=(table["name"], table["before"], table["after"]), lead=1,
        why_label=a.get("why_label") or _WHY_LABEL)
# ── cycle-dial ───────────────────────────────────────────────────────────


def r_cycle_dial(a, act_id):
    """⊕ b5-03 `#s-dial` — the release day is DERIVED and never stored.

    ⚖️ `release = length − luteal`, COMPUTED, at build time and again in the
    runtime, and there is nowhere in the payload to put one. NOTES-B5 §2.1:
    "the release day is derived as `length − 14`, never stored. That is the
    instrument's whole argument, and hard-coding release days would destroy
    it." A stored 7 / 14 / 21 would render pixel-identical and teach that day
    14 is a fact about people — which is `REPRO-05`, the misconception this
    lesson exists to confront. So a length that stores a release day is a
    build error, not a quietly ignored key.

    ⚖️ THE STOP TICKS ON TWO DIFFERENT LENGTHS SEEN, not on reaching the end
    of the slider. §2.1 again: "Rail credit is given for viewing two different
    lengths, not for reaching the end of the slider." Walking 28 days proves
    nothing; watching the release marker MOVE when the length changes is the
    entire lesson.

    ⚠️ AND THE OPENING LENGTH IS ALREADY SEEN. Design's state is
    `seen: { 28: true }`, so the readout opens at "1 of 3 lengths tried" and
    the stop is one length away rather than two. That is not a tick on load —
    nothing is complete — but it does mean the head counter's RESTING text is
    1 and not 0. See `_KIND_HEAD_START`, which is where that lands.
    """
    lengths = a.get("lengths") or []
    if len(lengths) < 2:
        raise ValueError(
            "cycle-dial %r declares %d cycle length(s). The instrument's whole "
            "argument is what happens to the release day when the length "
            "changes (NOTES-B5 §2.1)." % (act_id, len(lengths)))

    luteal, shed = a.get("luteal"), a.get("shed")
    if not isinstance(luteal, int) or isinstance(luteal, bool) or luteal <= 0:
        raise ValueError(
            "cycle-dial %r declares no whole-day `luteal`. It is the one "
            "number the release day is derived from." % act_id)
    if not isinstance(shed, int) or isinstance(shed, bool) or shed <= 0:
        raise ValueError(
            "cycle-dial %r declares no whole-day `shed` — the bleeding window "
            "the track draws and the first phase is bounded by." % act_id)

    days = []
    for L in lengths:
        for key in ("days", "label", "note"):
            if not L.get(key):
                raise ValueError(
                    "cycle-dial %r length %r is missing %r. The `note` reads "
                    "the release marker's position and changes with the chosen "
                    "length." % (act_id, L.get("days"), key))
        for banned in ("release", "release_day", "ovulation", "ovulation_day"):
            if banned in L:
                raise ValueError(
                    "cycle-dial %r length %r stores %r. The release day is "
                    "DERIVED as length − luteal and never stored (NOTES-B5 "
                    "§2.1): a stored one renders identically and teaches that "
                    "the day is a fact about people, which is the "
                    "misconception the lesson confronts."
                    % (act_id, L["days"], banned))
        n = int(L["days"])
        if n <= luteal:
            raise ValueError(
                "cycle-dial %r length %d is not longer than the %d-day luteal "
                "phase, so the derived release day is %d — not a day in the "
                "cycle." % (act_id, n, luteal, n - luteal))
        if n <= shed:
            raise ValueError(
                "cycle-dial %r length %d does not outlast its own %d-day "
                "bleeding window." % (act_id, n, shed))
        if n in days:
            raise ValueError("cycle-dial %r declares length %d twice."
                             % (act_id, n))
        days.append(n)

    by_id = {}
    for p in a.get("phases") or []:
        for key in ("id", "label", "ovary", "uterus"):
            if not p.get(key):
                raise ValueError(
                    "cycle-dial %r phase %r is missing %r. Both panels are on "
                    "screen at every day, and one of them reading blank says "
                    "the organ has stopped." % (act_id, p.get("id"), key))
        by_id[p["id"]] = p
    missing = [k for k in _DIAL_PHASES if k not in by_id]
    if missing:
        raise ValueError(
            "cycle-dial %r declares no phase %s. The four ids are a BRANCH, "
            "not a list — day ≤ shed, day < release, day = release, otherwise "
            "— so a missing or renamed id is a phase that can never show."
            % (act_id, ", ".join(map(repr, missing))))
    extra = sorted(set(by_id) - set(_DIAL_PHASES))
    if extra:
        raise ValueError(
            "cycle-dial %r declares phase(s) %s that the day branch never "
            "selects." % (act_id, ", ".join(map(repr, extra))))

    panels = a.get("panels") or {}
    for key in ("ovary", "uterus"):
        if not panels.get(key):
            raise ValueError("cycle-dial %r panels is missing %r."
                             % (act_id, key))

    track = a.get("track") or {}
    for key in ("start", "release", "last"):
        if not track.get(key):
            raise ValueError(
                "cycle-dial %r track is missing %r. The three labels under the "
                "bar are what say where the release marker IS."
                % (act_id, key))
    if "{n}" not in track["release"]:
        raise ValueError(
            "cycle-dial %r track.release carries no {n}. It is the one label "
            "that MOVES, and a fixed string there is a hard-coded release day "
            "by another route." % act_id)

    start_len = int(a.get("start_length") or days[0])
    if start_len not in days:
        raise ValueError(
            "cycle-dial %r opens on start_length %d, which is not one of %s."
            % (act_id, start_len, days))
    start_day = int(a.get("start_day") or 1)
    if not 1 <= start_day <= start_len:
        raise ValueError("cycle-dial %r opens on day %d of a %d-day cycle."
                         % (act_id, start_day, start_len))

    credit = int(a.get("credit_lengths") or 2)
    if not 2 <= credit <= len(days):
        raise ValueError(
            "cycle-dial %r credits the stop at %d length(s) seen. One is the "
            "length the block OPENS on, so crediting at 1 ticks the stop on "
            "load (MRB-208); crediting above %d makes it unreachable."
            % (act_id, credit, len(days)))

    day_format = a.get("day_format") or ""
    if "{n}" not in day_format:
        raise ValueError(
            "cycle-dial %r declares no `day_format` carrying {n} — the "
            "display-type readout of which day the student is standing on."
            % act_id)

    note_prompt = a.get("note_prompt")
    if not note_prompt:
        raise ValueError(
            "cycle-dial %r declares no `note_prompt`. It is what the note says "
            "BEFORE a second length has been tried, and it is the only line on "
            "the page asking for the one action the stop credits." % act_id)

    rel0 = start_len - luteal
    phase0 = by_id[_dial_phase_at(start_day, start_len, shed, luteal)]

    chips = "".join(
        '<button type="button" class="ks3-dial-len" data-dial-len="%d" '
        'data-note="%s" aria-pressed="%s">%s</button>'
        % (int(L["days"]), e(L["note"]),
           "true" if int(L["days"]) == start_len else "false", t(L["label"]))
        for L in lengths)

    cells = "".join(
        '<div class="ks3-dial-cell">'
        '<p class="ks3-dial-celllabel">%s</p>'
        '<p class="ks3-dial-celltext" data-dial-%s>%s</p></div>'
        % (t(panels[side]), side, t(phase0[side]))
        for side in ("ovary", "uterus"))

    # The four phases' text, carried as data rather than as four hidden copies
    # of two paragraphs. `hidden` and empty, so there is nothing to hide badly.
    phase_data = "".join(
        '<span class="ks3-dial-phasedata" data-dial-phase="%s" '
        'data-label="%s" data-ovary="%s" data-uterus="%s" hidden></span>'
        % (e(p["id"]), e(p["label"]), e(p["ovary"]), e(p["uterus"]))
        for p in a["phases"])

    return ('<div class="ks3-dial" data-dial data-luteal="%d" data-shed="%d" '
            'data-length="%d" data-day="%d" data-credit="%d" '
            'data-day-format="%s" data-track-release="%s" '
            'data-track-last="%s" data-note-prompt="%s">'
            '<p class="ks3-dial-lenlabel">%s</p>'
            '<div class="ks3-dial-lens">%s</div>'
            '<div class="ks3-dial-panel">'
            '<div class="ks3-dial-track">'
            '<span class="ks3-dial-shed" aria-hidden="true" data-dial-shed '
            'style="width:%s%%"></span>'
            '<span class="ks3-dial-release" aria-hidden="true" '
            'data-dial-release style="left:%s%%"></span>'
            '<span class="ks3-dial-marker" aria-hidden="true" '
            'data-dial-marker style="left:%s%%"></span></div>'
            '<div class="ks3-dial-ticks"><span>%s</span>'
            '<span data-dial-rellabel>%s</span>'
            '<span data-dial-lastlabel>%s</span></div>'
            '<div class="ks3-dial-controls">'
            '<button type="button" class="ks3-dial-step" data-dial-prev '
            'aria-label="%s">%s</button>'
            '<label class="ks3-sr-only" for="%s-day">%s</label>'
            '<input class="ks3-b4slider ks3-dial-slider" type="range" '
            'id="%s-day" min="1" max="%d" step="1" value="%d" data-dial-day>'
            '<button type="button" class="ks3-dial-step" data-dial-next '
            'aria-label="%s">%s</button></div>'
            '<div class="ks3-dial-readrow">'
            '<p class="ks3-dial-day" data-dial-dayread>%s</p>'
            '<p class="ks3-dial-phase" data-dial-phaseread>%s</p></div>'
            '<div class="ks3-dial-cells">%s</div>'
            '<p class="ks3-dial-note" data-dial-note>%s</p>%s</div></div>'
            % (luteal, shed, start_len, start_day, credit, e(day_format),
               e(track["release"]), e(track["last"]), e(note_prompt),
               t(_b5_label(a, act_id, ("length_label",), "cycle-length label")),
               chips,
               _pctnum(shed * 100.0 / start_len),
               _pctnum(_dial_pct(rel0, start_len)),
               _pctnum(_dial_pct(start_day, start_len)),
               t(track["start"]),
               t(track["release"].replace("{n}", str(rel0))),
               t(track["last"].replace("{n}", str(start_len))),
               e(_b5_label(a, act_id, ("prev_label",), "previous-day label")),
               t("−"), e(act_id),
               t(_b5_label(a, act_id, ("day_label",), "day label")),
               e(act_id), start_len, start_day,
               e(_b5_label(a, act_id, ("next_label",), "next-day label")),
               t("+"),
               t(day_format.replace("{n}", str(start_day))),
               t(phase0["label"]), cells, t(note_prompt), phase_data))


# ── registrations ────────────────────────────────────────────────────────
ART = {
    'dispersal': _dispersal,
    'flower-parts': _flower_parts,
    'gametes-journey': _gametes_journey,
    'placenta': _placenta,
    'pollen-tube': _pollen_tube,
    'repro-systems': _repro_systems,
}

KIND_SHELL = {
    'job-match': ("ks3-jmatch-block", ' data-instrument data-b5cblock data-stage-done="0"'),
    'crossing-bench': ("ks3-xbench-block", ' data-instrument data-b5cblock data-stage-done="0"'),
    'crosses-panel': ("ks3-xpanel-block", ' data-instrument data-b5cblock data-stage-done="0"'),
    'flower-jobs': ("ks3-fjobs-block", ' data-instrument data-b5cblock data-stage-done="0"'),
    'disperse-sort': ("ks3-dsort-block", ' data-instrument data-b5cblock data-stage-done="0"'),
    'gamete-compare': ("ks3-gcmp-block", ' data-instrument data-cmpblock data-stage-done="0"'),
    'what-it-becomes': ("ks3-becomes-block", ' data-instrument data-cmpblock data-stage-done="0"'),
    'cycle-dial': ("ks3-dial-block", ' data-instrument data-dialblock data-stage-done="0"'),
}

KIND_FN = {
    'job-match': r_job_match,
    'gamete-compare': r_gamete_compare,
    'cycle-dial': r_cycle_dial,
    'crossing-bench': r_crossing_bench,
    'crosses-panel': r_crosses_panel,
    'flower-jobs': r_flower_jobs,
    'what-it-becomes': r_what_it_becomes,
    'disperse-sort': r_disperse_sort,
}

KIND_HEAD_START = {
    'cycle-dial': 1,
}
