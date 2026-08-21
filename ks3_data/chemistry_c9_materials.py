"""C9 — Metals and materials. Four lessons, four authored, Year 9 Chemistry.

The thin unit wrapper. The lesson records live one per module under
`ks3_data/c9/`, authored against Claude Design's approved reference screens
(`docs/ks3/design-reference/c9/`).

    L1 the-reactivity-series             KS3.C.MATS.01
    L2 predicting-displacement           KS3.WS.EXP.02
    L3 getting-metals-out-of-rocks       KS3.C.MATS.02
    L4 ceramics-polymers-and-composites  KS3.C.MATS.03

All three subject statements are owned exactly once and whole; no sub-ID is
minted. The reasoning, and why `predicting-displacement` anchors on WS rather
than teaching new subject content, is in `ks3_data/c9/__init__.py`.

── THE UNIT IS ONE ARGUMENT, TOLD FOUR TIMES ────────────────────────────

An order derived from evidence (L1) becomes a prediction (L2), becomes the
reason a metal is expensive or cheap to obtain (L3) — and then L4 changes the
subject deliberately, from which metal to which MATERIAL, because "strong" and
"tough" are two words a student uses as one and a bicycle frame does not care
about the reactivity series at all.

⚠️ **THE UNIT ASSUMES C5 AND C8.** L1's bench is C5-04's argument run on two
liquids instead of a grid; L2's rule is C5-04's displacement rule with the
series behind it; L3 needs C8's metal/non-metal divide to say why carbon is in
a list of metals. Nothing here re-teaches them.
"""

from .c9 import lessons as _c9_lessons

UNIT = {
    "code":            "C9",
    "slug":            "metals-and-materials",
    "title":           "Metals and materials",
    "discipline":      "chemistry",
    # ⚠️ DECORATIVE HERE, AND DELIBERATELY MATCHING `structure.py`.
    "statutory_area":  "Materials",
    "split_rationale": "Three statutory bullets on one heading, taught as "
                       "four lessons because the order of the metals has to "
                       "be DERIVED before it can be used, and deriving it and "
                       "using it are two different demands on a student.",
    "intro":           "Some metals sit in the ground as the metal itself "
                       "and some have to be torn out of a rock with "
                       "electricity, and the difference is one order that was "
                       "worked out by putting metals into liquids and "
                       "watching. This unit is about that order, what it "
                       "predicts, what it costs — and then about the "
                       "materials that are not metals at all.",
    "lessons": _c9_lessons(),
}
