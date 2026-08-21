"""C8 — The periodic table. Seven lesson slots, six authored, Year 8 Chemistry.

The thin unit wrapper. The lesson records live one per module under
`ks3_data/c8/`, authored against Claude Design's approved reference screens
(`docs/ks3/design-reference/c8/`).

⚠️ **`KS3.C.PT.06` — the chemical properties of metal and non-metal oxides
with respect to acidity — HAS NO LESSON, AND IS THE ONLY UNCOVERED STATUTORY
STATEMENT IN C1–C8.** Its slot exists (`metal-and-non-metal-oxides`, slot 7)
and renders as an honest coming-soon page. It is a real hole in the
curriculum, it is recorded as one here and in `NOTES-C8.md` §1, and this run
did not close it.

── SEVEN SLOTS, NOT §7's FIVE (MRB-281, R1) ─────────────────────────────

§7 planned five lessons and folded groups 1, 7 and 0 into one MODEL lesson,
*Patterns you can predict*. Design built the three separately and the split is
kept. The argument is `PTAB-08`:

    "reactivity always increases going down a group"

is the unit's most valuable misconception entry and it EXISTS ONLY because
c8-04 builds that trend on a water trough and c8-05 breaks it on a
displacement grid. Merged, the reversal stops being a grid the student fills
in and is surprised by, and becomes a paragraph they read. §7 is a plan;
`structure.py` is the skeleton; the plan loses.

── SIX BULLETS, AND TWO OF THEM SPLIT AT CLAUSE GRAIN ───────────────────

    L1 metals-and-non-metals         PT.01, PT.03b, PT.05
    L2 mendeleev                     PT.02
    L3 groups-and-periods            PT.03a
    L4 group-1-the-alkali-metals     PT.04a
    L5 group-7-the-halogens          PT.04b
    L6 group-0-and-why-groups-exist  PT.04c
    L7 metal-and-non-metal-oxides    PT.06        ← NOT AUTHORED

`PT.03` prints two ideas and every scheme teaches them as two lessons.
`PT.04` is one sentence split by the PREDICTIVE MOVE rather than by example —
the reasoning, and why that distinction matters, is written against both
parents in `ks3_data/substatements.py`.

── THE UNIT ASSUMES C1, C2 AND C5 ───────────────────────────────────────

Every square on c8-03's table is an element from C2, the trough on c8-04 is a
reaction of the kind C5 named, and the displacement grid on c8-05 is C5-04's
argument run on non-metals. Nothing here re-teaches them.
"""

from .c8 import lessons as _c8_lessons

UNIT = {
    "code":            "C8",
    "slug":            "the-periodic-table",
    "title":           "The periodic table",
    "discipline":      "chemistry",
    # ⚠️ DECORATIVE HERE, AND DELIBERATELY MATCHING `structure.py`.
    # `ks3_data.build_units()` takes `statutory_area` from the SKELETON, never
    # from this dict, so a value that disagreed would be a lie nothing catches.
    "statutory_area":  "The periodic table",
    "split_rationale": "Six statutory bullets on one heading, taught as seven "
                       "lessons because two of the bullets are compound: one "
                       "carries both the table's address system and the "
                       "metal / non-metal divide, and one carries three "
                       "different predictive moves that a student can hold "
                       "any one of without the others.",
    "intro":           "There are about ninety elements that occur on Earth, "
                       "and for most of the nineteenth century nobody could "
                       "say why some of them behaved alike. This unit is "
                       "about the arrangement that answered it — what a "
                       "column means, what a row means, and how a table can "
                       "let you describe an element nobody has found yet.",
    "lessons": _c8_lessons(),
}
