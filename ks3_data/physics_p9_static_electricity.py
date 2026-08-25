"""P9 — Static electricity. The unit where nothing is made and nothing
touches.

The lesson records live in `ks3_data/p9/`, one module each; this file is
the unit's identity and the seam `ks3_data._authored_modules()` discovers.

── THE UNIT IS ONE ARGUMENT ───────────────────────────────────────────

**Charge is never created. It is separated, by moving electrons and only
electrons — and once it is separated it reaches across a gap with nothing
in between, because the charged object has changed the space itself.**

L1 is the separation: two neutral insulators, one transfer, two equal and
opposite results, and a total that has not moved. L2 is what the two
separated objects then do to each other — and, in the half everybody
forgets, what a charged object does to something with no charge at all.
L3 asks what is actually in the gap, and answers that nothing is: the
field is the answer physics gives to a question the first two lessons are
careful to leave open.

A student who finishes the unit should stop saying that rubbing makes
charge, and should stop reading attraction as proof of it.

⚠️ **NO FORMULA BLOCK ANYWHERE IN P9, AND NO WORKED EXAMPLE.**
Design's §3 table gives all three lessons *no block*, and her audit says
in terms that "P9 and P10 have no worked examples, correctly: nothing in
either unit is quantitative, and the rule is not to invent a calculation
to fill the block". `Q = n × e` would take a triangle cleanly and needs
the coulomb and the elementary charge, both GCSE and neither named by
`STAT.01`. **Ruled by Mide, 21 Aug 2026: `p9-01` carries no block, and
BOTH of its readouts stay** — the electron count in words and the charge
in nanocoulombs — with no arithmetic asked of the student. Her FLAG 4 is
resolved that way and not by dropping the nanocoulomb figure: the count
of electrons alone would weaken the "equal and opposite" point, which is
the reason both are there.

⚠️ **`p9-01`'s CHARGE MODEL HAS A CEILING, AND IT IS DESIGN'S OWN.**
Her FLAG 8 says the model has none and "would keep climbing if the slider
went further". Her PAGE says otherwise: `STROKE_CEIL = 26.3` and
`STROKE_TAU = 14`, so the stroke term is `26.3 × (1 − e^(−r/14))` and is
visibly flattening by twenty strokes. Her legal line says so too. **The
drawing was measured and the drawing is what is built**; the note is
recorded as a contradiction in `DEPARTURES-P9.md` rather than followed.

⚠️ **INDUCED ATTRACTION IS REPORTED IN RELATIVE WORDS ONLY.**
Ruled by Mide, 21 Aug 2026: her chosen coefficient (FLAG 9) is accepted,
and no absolute force in newtons appears anywhere on `p9-02` — not in a
tile, not in the note, not in the legal line, not in a rung. Her page
already holds that line: the strength tile for a neutral pair reads *"a
small fraction of the charged pair at this gap"* and never a figure. The
like/unlike cases keep her relative scale, on which 100 is the closest
fully charged pair and which the legal line declares as a scale rather
than a measurement.

⚠️ **NO SAFEGUARDING BLOCK ON ANY P9 PAGE.** Ruled: `p9-03` explains why
a car is safe in a thunderstorm and rung 4 asks for it, but that is safety
information a student is being GIVEN, not a risk they are being asked to
disclose. Adding the block here would dilute a block that means something
where it is used. Design's §6 reaches the same conclusion for the same
reason.

⚠️ **FOUR RAIL STOPS ON EVERY PAGE**, measured off her own `RAIL`:

    p9-01  s-hook  s-rub      s-think  s-ladder
    p9-02  s-hook  s-spheres  s-matrix s-ladder
    p9-03  s-hook  s-field    s-reach  s-ladder

`p9-01` is the only page in the key stage whose THIRD stop is the
confrontation rather than a figure beside the bench — her `DONE` for
`s-think` reads `s.gate !== null`, and her triboelectric ladder sits off
the rail. See `ks3_data/p9/__init__.py` for what that costs and how it is
paid.
"""

from .p9 import lessons as _p9_lessons

UNIT = {
    "code":            "P9",
    "slug":            "static-electricity",
    "title":           "Static electricity",
    "discipline":      "physics",
    # ⚠️ DECORATIVE HERE, AND DELIBERATELY MATCHING `structure.py`.
    "statutory_area":  "Electricity and electromagnetism",
    "split_rationale": "Two statutory statements over three slots — the "
                       "surplus case at 0.67. STAT.01 is split at the "
                       "clause, because how an object becomes charged and "
                       "what two charged objects do to each other are two "
                       "lessons in every scheme of work and because the "
                       "second one has to carry induction. STAT.02 is whole "
                       "and is p9-03's.",
    "intro":           "Rubbing does not make charge — it moves electrons, "
                       "and leaves two objects equally and oppositely "
                       "charged. Follow that from a duster to the field "
                       "that reaches across an empty gap.",
    "lessons": _p9_lessons(),
}
