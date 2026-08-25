"""P4 — Forces. The unit where a force gets both its ends named.

The lesson records live in `ks3_data/p4/`, one module each; this file is the
unit's identity and the seam `ks3_data._authored_modules()` discovers.

── THE UNIT IS ONE ARGUMENT ───────────────────────────────────────────

**A force is not a thing an object has. It is what two objects are doing
to each other, and the only one that matters is what is left over.**

L1 establishes the pair. L2 draws it and adds it up. L3 asks what happens
when the sum is zero and L4 what happens when it is not — and the answer
to L4 is the one nobody expects, because a resultant force changes motion
rather than causing it. L5 to L8 are the four things forces actually do in
a classroom: rub, resist, turn and deform. L9 takes away the touching.

A student who finishes the unit should find "what force is on it?" an
incomplete question, and reach for both objects before answering.

⚠️ **THE FIRST PRODUCT IN THE UNIT IS `p4-07`, AND IT IS THE ONLY
TRIANGLE.** Four of the first six relationships here are additive — a
difference, an equality, a leftover — and the reflex is to reach for a
triangle because physics has triangles. Design's own note flags it and
asks a reviewer to check that `moment = force × distance` is the first
one a student meets. As shipped, it is.

⚠️ **THE WORD "ACCELERATION" APPEARS NOWHERE IN THIS UNIT, DELIBERATELY.**
It is not in FORCES.01–08, and `F = ma` is GCSE. `p4-04` handles the
change of motion in words — faster, slower, bending — and names mass only
in the *Going further* layer, as a shape rather than an equation.

⚠️ **WEIGHT IS `mass in kilograms × 10 N/kg`, WRITTEN OUT, EVERY TIME.**
Design's hedge, and it is load-bearing: `p4-03`'s hook, its formula step,
its key note and its foot line all carry the full phrase rather than a
symbol, because the misconception it exists to kill is that the weight in
newtons is the same number as the mass in kilograms.
"""

from .p4 import lessons as _p4_lessons

UNIT = {
    "code":            "P4",
    "slug":            "forces",
    "title":           "Forces",
    "discipline":      "physics",
    # ⚠️ DECORATIVE HERE, AND DELIBERATELY MATCHING `structure.py`.
    "statutory_area":  "Motion and forces",
    "split_rationale": "None. Eleven statutory statements over nine slots, "
                       "with three compound bullets split at the clause — "
                       "friction, resistance and springs each own one clause "
                       "of FORCES.04, and each is a different practical.",
    "intro":           "A force is never something one object has. It takes "
                       "two, it is measured in newtons, and what an object "
                       "actually responds to is whatever is left over when "
                       "you have added them all up.",
    "lessons": _p4_lessons(),
}
