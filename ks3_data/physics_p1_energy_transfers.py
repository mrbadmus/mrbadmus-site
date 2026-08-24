"""P1 — Energy transfers. The first physics unit in the key stage.

The lesson records live in `ks3_data/p1/`, one module each; this file is the
unit's identity and the seam `ks3_data._authored_modules()` discovers. Same
shape as `chemistry_c10_earth.py` and every unit before it.

── THE UNIT IS ONE ARGUMENT ────────────────────────────────────────────

Energy is a number, not a substance — and the number does not change. Every
lesson in the unit is that sentence met somewhere new: a ledger that refuses
to grow (L1), a tally that will not move however the slider is set (L2), a
beam that stays level (L3), a difference that shrinks to nothing (L4), and
finally a machine that buys force with distance and cannot buy energy at all
(L8). A student who finishes the unit should find "where did the energy go?"
an answerable question rather than a rhetorical one.

⚠️ **THE UNIT ASSUMES C1.** L4 re-confronts `PART-03` — the fixed-size
reference particle — rather than restating it, and L3's `#s-think` names
`c1-03`'s sealed-bag result explicitly and calls the two "the same belief in
different clothes". That cross-reference is deliberate and load-bearing; see
the `ENER-12` / `PART-05` lock in `docs/ks3/misconception-register.md`.

⚠️ **NOTHING HERE IS QUANTITATIVE UNTIL L8.** Design draws seven conceptual
lessons and one QUANTITATIVE one, and the CFIFA block appears in `p1-08` and
nowhere else in the unit. Joules are named in L1 and counted in L3, but no
lesson before L8 asks a student to calculate anything.
"""

from .p1 import lessons as _p1_lessons

UNIT = {
    "code":            "P1",
    "slug":            "energy-transfers",
    "title":           "Energy transfers",
    "discipline":      "physics",
    # ⚠️ DECORATIVE HERE, AND DELIBERATELY MATCHING `structure.py`.
    "statutory_area":  "Energy",
    "split_rationale": "Six statutory bullets, eight lessons, because two of "
                       "the six are compound: the stores bullet names both "
                       "the list and the before-and-after comparison, and the "
                       "heating bullet names thermal equilibrium, conduction, "
                       "radiation and insulators — four ideas no scheme of "
                       "work teaches in one sitting.",
    "intro":           "Energy is a number you can work out for a situation, "
                       "and the discovery is that the number never changes. "
                       "Everything else in this unit follows from that.",
    "lessons": _p1_lessons(),
}
