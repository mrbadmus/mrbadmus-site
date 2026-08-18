"""B11 — Evolution, extinction and biodiversity. Four lessons, Biology.

The thin unit wrapper. The lesson records live one per module under
`ks3_data/b11/`, authored against Claude Design's approved reference screens in
`docs/ks3/design-reference/b11/` under the MRB-220 build contract, and against the
payload schema written before dispatch at
`docs/ks3/b11-inventory/PAYLOAD-SCHEMA.md`.

    L1 variation-and-competitive-success        advantage-bench
    L2 natural-selection                        selection-runner
    L3 when-the-environment-changes-extinction   pressure-bench
    L4 biodiversity-and-gene-banks              blight-bench

**Slugs match `ks3_data/structure.py` character for character.** They are the
join for scheme-of-work rows, progress records and every `requires` edge, and
they are permanent (§8.4).

**Four rail stops per page, all four tick (MRB-249).** Schema §8 left this as
the commander's call between a rail of three and a mirror; the mirror is the
call, and the reasoning is recorded there and in `ks3_data/b11/__init__.py`.

**review_state is `draft` on every lesson.** Mide is the sole science gate
(§5.10).
"""

from .b11 import lessons as _b11_lessons

UNIT = {
    "code":            "B11",
    "slug":            "evolution-extinction-and-biodiversity",
    "title":           "Evolution, extinction and biodiversity",
    "discipline":      "biology",
    "statutory_area":  "Genetics and evolution",
    "split_rationale": None,
    # The commander's, for the same reason as B10's: no unit card is drawn.
    "intro":           "B10 ended with variation and what a species is. This "
                       "unit is what variation DOES over time. Which variation "
                       "helps depends entirely on the conditions, and the "
                       "conditions change — so populations change, some "
                       "species run out of the variation they need, and the "
                       "variety that is left turns out to be the thing worth "
                       "protecting.",
    "lessons": _b11_lessons(),
}
