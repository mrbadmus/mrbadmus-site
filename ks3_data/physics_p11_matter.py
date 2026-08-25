"""P11 — Matter and the particle model. The unit that measures the model.

The lesson records live in `ks3_data/p11/`, one module each; this file is
the unit's identity and the seam `ks3_data._authored_modules()` discovers.

── THE UNIT IS ONE ARGUMENT ───────────────────────────────────────────

**Matter is particles, and how tightly they are packed and how fast they
are moving are two different questions with two different answers — one
gives you a density, the other gives you a temperature, and neither is
the amount of anything.**

L1 measures the packing: mass over volume, a property of the material and
not of the object, and the number that decides what floats. L2 is the
evidence that the particles are there at all — a speck you can see moving
in a way that only makes sense if something you cannot see is hitting it.
L3 separates the two questions that get confused: how fast one particle
is going, and how much energy all of them add up to. L4 is the exception
that proves the packing is real, because water packs LOOSER as it
freezes and the whole of a pond's winter follows from it.

A student who finishes the unit should stop saying that heavy means dense
and that hot means a lot.

── ⚖️ A REFERENCING UNIT ──────────────────────────────────────────────

`structure.REFERENCING_UNITS` lists P11 against C1 and C4. Four lessons,
five statements, and nothing restated:

    p11-01  density                          KS3.P.PHYC.02
    p11-02  brownian-motion                  KS3.P.PHYC.03
    p11-03  temperature-and-internal-energy  KS3.P.EIM.01, KS3.P.EIM.02
    p11-04  why-ice-floats                   KS3.P.PMOD.01

States of matter, changes of state, diffusion and gas pressure are C1's;
`KS3.P.PHYC.01` and `KS3.P.PHYC.04` are C1's rows in the register and are
NOT claimed here. Every lesson's Connects-to card links out to them.

⚠️ **ONE FORMULA BLOCK, ON `p11-01`, AND IT IS A TRIANGLE.** `m = d × V`
is a product, so MRB-204 gives it the triangle with the mass on top —
which is what Design drew. `p11-02` to `p11-04` are MODEL and CONTRAST
lessons with nothing quantitative in them, and her audit is explicit that
the rule is not to invent a calculation to fill the block.

⚠️ **FOUR RAIL STOPS ON EVERY PAGE**, measured off her own `RAIL`:

    p11-01  s-hook  s-bench  s-formula  s-ladder
    p11-02  s-hook  s-bench  s-think    s-ladder
    p11-03  s-hook  s-bench  s-think    s-ladder
    p11-04  s-hook  s-bench  s-think    s-ladder

Three of the four put `#s-think` on the rail — the second unit in the key
stage to do so after `p9-01`, and here from a PAGE-LEVEL predicate
(`s.answers.r1 !== null || s.hookChoice !== null`) rather than from a
sibling bench. See `ks3_data/p11/__init__.py` for what that costs and how
it is paid, and the misconception register for the note that keeps this
from re-raising `p9-01`'s open flag.

⚠️ **ONE BENCH SHELL, FOUR MODELS.** Design wrote `Bench.dc.html` once and
mounted it on all four pages: commit gate, tab row, slider, a dark panel
of proportional bars, readout cards, closing note. `matter-bench` is that
component; `model` selects the arithmetic. P12 is building the same shell
under its own family from the same payload schema.

⚠️ **RULED, AND APPLIED RATHER THAN RE-ASKED.** `p11-02`'s 500 m/s for air
and 590 m/s for water at 20 °C both stand; her legal line's claim that
both are root-mean-square figures does not, because 590 is the MEAN speed
of a water molecule. The line says *typical molecular speeds*. Weight is
not in this unit and no newton appears anywhere in it.
"""

from .p11 import lessons as _p11_lessons

UNIT = {
    "code":            "P11",
    "slug":            "matter-and-the-particle-model",
    "title":           "Matter and the particle model",
    "discipline":      "physics",
    # ⚠️ DECORATIVE HERE, AND DELIBERATELY MATCHING `structure.py`.
    "statutory_area":  "Matter",
    "intro":           "Density is what the particle model is for: how "
                       "tightly matter is packed, why a jiggling speck proves "
                       "the particles are there, why hot is not the same as a "
                       "lot, and why ice is the one solid that floats on its "
                       "own melt.",
    "lessons": _p11_lessons(),
}
