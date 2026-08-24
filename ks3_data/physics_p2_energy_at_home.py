"""P2 — Energy at home. The unit where energy stops being a story and
becomes a number on a bill.

The lesson records live in `ks3_data/p2/`, one module each; this file is the
unit's identity and the seam `ks3_data._authored_modules()` discovers. Same
shape as `physics_p1_energy_transfers.py` and every unit before it.

── THE UNIT IS ONE ARGUMENT ────────────────────────────────────────────

P1 established that energy is a quantity and that the quantity is conserved.
P2 asks the only question that leaves: **how much, and what does it cost?**

Four of the five lessons are QUANTITATIVE — the highest concentration
anywhere in the key stage — and they build one habit in one order. L1
measures a store and finds the measurement honest but low. L2 separates the
two quantities everything else depends on: power is a RATE, energy is a
TOTAL, and a rating cannot tell you a bill. L3 multiplies them, in seconds,
and shows why doing it in minutes is out by sixty. L4 puts five of those
products on one page and adds them up, which is where the triangle stops
being the right picture and a balance takes over. L5 steps back and asks
which store you were emptying in the first place, and whether it refills.

A student who finishes the unit should be able to pick up a real electricity
bill and say what every line on it means.

⚠️ **THE UNIT OWNS THE FOOD-ENERGY FIGURES.** `p2-01 energy-in-food` is the
single source under §4.6: Biology B3's `a-balanced-diet` references it and
must not restate the numbers. Design's endmatter on `p2-01` names B3 under
"Also used by".

⚠️ **THE UNIT ASSUMES P1.** `p2-01`'s `#s-think` re-confronts `ENER-09` by
name — the rolling ball, the braking car and the flat battery in one
sentence — so a student meets it as one belief rather than four unrelated
corrections. `p2-05`'s second quote does the same work for `ENER-10`, the
store/pathway distinction, applied to resources rather than to torches.
"""

from .p2 import lessons as _p2_lessons

UNIT = {
    "code":            "P2",
    "slug":            "energy-at-home",
    "title":           "Energy at home",
    "discipline":      "physics",
    # ⚠️ DECORATIVE HERE, AND DELIBERATELY MATCHING `structure.py`.
    "statutory_area":  "Energy",
    "split_rationale": "None needed. Five statutory bullets, five lessons, "
                       "one for one — the only physics unit so far where "
                       "the national curriculum's own grain and a workable "
                       "scheme of work already agree, so this unit mints no "
                       "substatements at all.",
    "intro":           "Energy has a price. This unit is where the quantity "
                       "you learned to conserve turns into a number on a "
                       "meter, a rating on a plug and a line on a bill.",
    "lessons": _p2_lessons(),
}
