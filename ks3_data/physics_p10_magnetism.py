"""P10 — Magnetism and electromagnetism. The unit where a force acts across a
gap, and where a current is what makes one.

The lesson records live in `ks3_data/p10/`, one module each; this file is the
unit's identity and the seam `ks3_data._authored_modules()` discovers.

── THE UNIT IS ONE ARGUMENT ───────────────────────────────────────────

**A magnet fills the space around it with a field, and that field is what
another magnet — or a piece of iron — responds to. A current makes one too,
which means magnetism can be switched, reversed, and made to turn something.**

L1 is what a magnet does and, more importantly, what it does NOT prove: only
repulsion settles the question, because attraction is what plain steel does.
L2 answers what is in the gap, by plotting it: a field, mapped by a compass,
drawn as lines that are a record of readings rather than objects. L3 says the
planet has one, which is why a needle settles at all, and takes the naming
problem head-on — the pole in the Arctic is magnetically a south pole. L4 is
the discovery that a current makes a field, so a magnet can be built and
switched off. L5 is what a field does back to a current: it pushes it
sideways, and two opposite pushes either side of an axle turn a motor.

A student who finishes the unit should stop saying that metals are magnetic,
should stop reading attraction as proof, and should be able to say what the
split ring is for without saying it makes the motor turn.

⚠️ **NO FORMULA BLOCK ANYWHERE IN P10, AND NO WORKED EXAMPLE.**
Design's §2 gives all five lessons no block, and her audit says in terms that
"P9 and P10 have no worked examples, correctly: nothing in either unit is
quantitative, and the rule is not to invent a calculation to fill the block".
The turns-and-current relationship on `p10-04` is a genuine product and would
take a triangle cleanly — and it has no named quantity and no unit at this
stage, so the badges could only be filled with notation invented for the
purpose, which MRB-204's own setup rule forbids. It is stated in words and the
bench shows it by letting the two controls move independently.

⚠️ **NO TESLA AND NO NEWTON, ANYWHERE IN THE UNIT.**
Ruled by Design under standing rule 1 (her §9.2) and applied here without
re-asking. Every figure a student can read on these five pages is one of four
things: a real angle in degrees, a real current in amps, a count of paper
clips, or a RELATIVE figure whose readout names its reference in words. Each
bench drawer walks its whole payload and refuses one that names either unit,
so the ruling cannot be lost to a later edit that only looks like tidying.

⚠️ **THE PULL ON UNMAGNETISED STEEL IS RELATIVE WORDS ONLY, NEVER A FIGURE.**
Her §8, and the same discipline `p9-02` holds for induced attraction: how
strongly a piece of steel magnetises depends on its shape, its carbon content
and its history, so a coefficient here would be a guess dressed as a
measurement. `p10-01`'s strength tile prints *"reported in words, not on the
scale"* for all twenty-four magnet-and-steel states.

⚠️ **CHILDLINE IS ON `p10-01` AND NOWHERE ELSE IN THE UNIT.**
Ruled by Design (§5) and applied. Her *Going further* names neodymium magnets
and magnet ingestion — a risk to a student's own body, in their own home,
rather than in a lab. It sits in the engine's `safeguarding_note` slot: small
type, bottom edge, above the legal line, never a callout, which is MRB-257
audit 6.4 as Mide ruled it. The other four pages carry none; `p10-04`'s MRI
paragraph is information about a hazard in a hospital, not a risk the student
is being asked to disclose.

⚠️ **FOUR RAIL STOPS ON EVERY PAGE**, measured off her own `RAIL`:

    p10-01  s-hook  s-bench  s-proof  s-ladder
    p10-02  s-hook  s-bench  s-rules  s-ladder
    p10-03  s-hook  s-bench  s-earth  s-ladder
    p10-04  s-hook  s-bench  s-uses   s-ladder
    p10-05  s-hook  s-bench  s-parts  s-ladder

The third stop on every page is the figure beside the bench, and it ticks on
the bench's own commit gate — earlier than the bench itself. See
`ks3_data/p10/__init__.py` for why that is `band_anchor` and not `mirrors`.
"""

from .p10 import lessons as _p10_lessons

UNIT = {
    "code":            "P10",
    "slug":            "magnetism-and-electromagnetism",
    "title":           "Magnetism and electromagnetism",
    "discipline":      "physics",
    # ⚠️ DECORATIVE HERE, AND DELIBERATELY MATCHING `structure.py`.
    "statutory_area":  "Electricity and electromagnetism",
    "split_rationale": "Four statutory statements over five slots — the "
                       "surplus case at 0.80. MAG.04 is split at its own "
                       "comma, because the magnetic effect of a current and "
                       "the D.C. motor are two lessons in every scheme of "
                       "work and because the motor needs the force on a "
                       "current-carrying wire, which the electromagnet lesson "
                       "does not use at all. MAG.01, MAG.02 and MAG.03 are "
                       "whole and are p10-01's, p10-02's and p10-03's.",
    "intro":           "A magnet does not have to touch anything to act on "
                       "it — and only one of the things it does is proof "
                       "that the other object is a magnet too. Follow that "
                       "from two bars on a track to the field a current "
                       "makes, and to the motor that field turns.",
    "lessons": _p10_lessons(),
}
