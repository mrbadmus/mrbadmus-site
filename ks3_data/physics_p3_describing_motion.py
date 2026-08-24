"""P3 — Describing motion. The unit where a speed becomes a measurement.

The lesson records live in `ks3_data/p3/`, one module each; this file is the
unit's identity and the seam `ks3_data._authored_modules()` discovers.

── THE UNIT IS ONE ARGUMENT ───────────────────────────────────────────

**A speed is not a thing an object has. It is a number you make, out of
two measurements, against something you chose.**

L1 builds it: two measurements, one number, and an instrument that refuses
to do the division for you. L2 draws it: the same journey as a line, where
the speed is not plotted anywhere and lives only in the steepness. L3 takes
away the thing everyone was quietly measuring against — the ground —
and shows that the number changes while the object does not.

A student who finishes the unit should find "how fast is it going?" an
incomplete question.

⚠️ **THE QUANTITATIVE FAMILY PATTERN IS SET BY `p3-01`.** Design's
`NOTES-P3.md` §1 defines it, and its load-bearing step is (2): *the
instrument produces raw measurements and refuses to do the arithmetic.*
The light gates hand over a distance and a time and a third tile that reads
"speed — not measured — you work it out". An instrument that hands over
the answer has removed the lesson. Every QUANTITATIVE lesson after this one
inherits that, and P2's four already do.

⚠️ **THE WORD "VELOCITY" APPEARS NOWHERE IN THIS UNIT, DELIBERATELY**
(Design's flag 6). It is not in MOT.01–03, and direction-as-sign is not
taught at KS3. `p3-03` handles direction in words — "the same way",
"the opposite way" — and never with a negative number. That is the line
P4 then opens on.
"""

from .p3 import lessons as _p3_lessons

UNIT = {
    "code":            "P3",
    "slug":            "describing-motion",
    "title":           "Describing motion",
    "discipline":      "physics",
    # ⚠️ DECORATIVE HERE, AND DELIBERATELY MATCHING `structure.py`.
    "statutory_area":  "Motion and forces",
    "split_rationale": "None needed. Three statutory bullets, three lessons, "
                       "one for one — speed, its graph, and what happens "
                       "when the thing you measured against is itself "
                       "moving.",
    "intro":           "A speed is two measurements made into one number. "
                       "This unit builds that number, draws it, and then "
                       "asks the question nobody had needed to ask yet: "
                       "measured against what?",
    "lessons": _p3_lessons(),
}
