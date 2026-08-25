"""P12 — Space. The unit where one number changes and one does not.

The lesson records live in `ks3_data/p12/`, one module each; this file is
the unit's identity and the seam `ks3_data._authored_modules()` discovers.

── THE UNIT IS ONE ARGUMENT ───────────────────────────────────────────

**Gravity is an attraction between any two masses, and it never switches
off. Weight is what that attraction does to a particular object in a
particular place — so weight travels and mass does not, and everything
else in the unit is that one distinction at a larger and larger scale.**

L1 defines the two quantities and puts a number on the difference. L2
takes the same object to four places and shows one column moving while
the other stands still. L3 lets go of the surface entirely: the same
force, between bodies nothing is standing on, falling off as the square
of the distance and always arriving in equal and opposite pairs — which
is what an orbit is made of. L4 asks what is out there and in what order
of size. L5 explains the one astronomical fact every student already
thinks they know and almost all of them have wrong. L6 gives them the
ruler the rest of it is measured with, and the sting in it: a light year
is a distance, and every distance in space is also a delay.

A student who finishes the unit should stop saying that astronauts float
because there is no gravity, stop reading a bathroom scale as a
measurement of matter, and stop hearing "four light years" as a length of
time.

⚠️ **THREE PAGES CARRY A FORMULA BLOCK AND THREE CARRY NONE.**

    p12-01  W = m × g   triangle + two worked examples + two attempts
    p12-02  W = m × g   the same block, and her README says why
    p12-06  d = c × t   triangle + two worked examples + two attempts

Both relationships are PRODUCTS, so both take Design's triangle; neither
takes a beam or a bar, which are for sums (MRB-204 as amended). Design's
README states the `p12-02` case in terms: *"p12-02 is declared CONTRAST
rather than QUANTITATIVE and still carries the block: W = m × g is the
whole content of the contrast, and the gram-to-kilogram trap is where the
distinction between mass and weight is actually lost."*

Her audit's other half is honoured too: *"p12-03, p12-04 and p12-05 have
no calculation in them and no worked example has been invented to fill the
slot."* Nothing is invented for them.

⚠️ **`p12-03`'s FORCES ARE READOUTS, NOT ARITHMETIC.** Her NOTES §6 asks
for a ruling on `1.98 × 10^20 N` at KS3. **Ruled: they stand as drawn.**
The bench computes them; rung 2 asks whether the Earth pulls the Sun as
hard as the Sun pulls the Earth, which is a question about equality and
not about a calculation; and standard form is on the KS3 maths curriculum.
Powers of ten are typed `10^20` throughout, which is Design's own §5
convention: U+2070 and U+2074–U+2079 are absent from every shipped font
subset and fall back to a system face mid-number.

⚠️ **`p12-04`'s STAR COUNTS STAND.** Her NOTES §6 asks whether to quote
figures at all. **Ruled: keep them.** "About 200 billion" for the Milky
Way, "about a trillion" for Andromeda and "around two trillion galaxies"
are already hedged in her own words, and her legal line records that
galaxy star counts are estimates with wide error bars. An order of
magnitude with no number attached is harder for a student to hold, not
easier.

⚠️ **`p12-05` IS REAL ASTRONOMY AND IT IS CHECKED.** Solar declination is
0° at the equinoxes and ±23.44° at the solstices; daylight comes from the
standard sunrise equation; noon altitude is `90 − |latitude −
declination|`; energy per square metre is the sine of that altitude.
London on 21 June falls out at 16.5 hours and 61°, and both figures are
asserted by the unit's own content-truth check rather than taken on
trust.

⚠️ **NO SAFEGUARDING BLOCK ON ANY P12 PAGE.** Nothing in the unit asks a
student to disclose anything about themselves. Design's delivery carries
none and none is added; the block means something where it is used.

⚠️ **FOUR RAIL STOPS ON EVERY PAGE**, measured off her own `RAIL` and
matching `docs/ks3/rail-manifest.md` row for row:

    p12-01  s-hook  s-bench  s-formula  s-ladder
    p12-02  s-hook  s-bench  s-formula  s-ladder
    p12-03  s-hook  s-bench  s-think    s-ladder
    p12-04  s-hook  s-bench  s-think    s-ladder
    p12-05  s-hook  s-bench  s-think    s-ladder
    p12-06  s-hook  s-bench  s-formula  s-ladder

Three of the six put the confrontation on the rail, on a predicate that
the bench cannot satisfy and that `mirrors` cannot express. See
`ks3_data/p12/__init__.py` for what that costs and how it is paid.
"""

from .p12 import lessons as _p12_lessons

UNIT = {
    "code":            "P12",
    "slug":            "space",
    "title":           "Space",
    "discipline":      "physics",
    # ⚠️ DECORATIVE HERE, AND DELIBERATELY MATCHING `structure.py`.
    "statutory_area":  "Space physics",
    "split_rationale": "Four statutory statements over six slots — the "
                       "surplus case at 1.5. SPACE.01 is split at the "
                       "clause into three, because defining weight, showing "
                       "that it travels while mass does not, and treating "
                       "gravity between bodies nobody is standing on are "
                       "three lessons in every scheme of work and the third "
                       "one has to carry orbits. SPACE.02, .03 and .04 are "
                       "whole and are p12-04's, p12-05's and p12-06's.",
    "intro":           "Gravity never switches off and never pushes. Follow "
                       "it from a bathroom scale that measures newtons and "
                       "prints kilograms, out to the pull between the Earth "
                       "and the Sun, and on to a ruler made of light.",
    "lessons": _p12_lessons(),
}
