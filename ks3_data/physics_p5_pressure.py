"""P5 — Pressure. The unit where a force meets an area.

The lesson records live in `ks3_data/p5/`, one module each; this file is the
unit's identity and the seam `ks3_data._authored_modules()` discovers.

── THE UNIT IS ONE ARGUMENT ───────────────────────────────────────────

**A force on its own tells you nothing about what it will do to a surface.
What matters is how much surface it has to work through — and once you can
see that, a fluid turns out to be pressing on everything it touches, from
every direction, all the time.**

L1 builds the quantity from a drawing pin. L2 finds it inside a liquid and
shows it depends on depth and nothing else. L3 takes the pressure
difference across an object and gets a force out of it. L4 does the same
thing with the ocean of air nobody notices they are standing in.

A student who finishes the unit should stop saying *suck*.

⚠️ **THE ONLY TRIANGLE IS `p5-01`.** It is the unit's only product — and
even there the relationship taught is a division, allowed a triangle only
because `force = pressure × area` is the same statement rearranged.
`p5-02` and `p5-04` are sums of layers and take a stack; `p5-03` is a
difference and takes a beam. None of the three has cover buttons, because
covering a layer of water or one of two opposed arrows asks nothing.

⚠️ **THE WORD "DENSITY" IS USED IN NO LESSON'S CORE.** It is C1's, it is
`p11`'s, and floating at KS3 is taught as *the weight of what you push out
of the way* rather than as a density comparison — which is what
`PRES.02` says and what makes `p5-03`'s ship-and-bolt case work. The
densities on the benches are declared in the foot lines as model numbers,
never taught as the explanation.

⚠️ **`p5-02` REPORTS GAUGE PRESSURE AND SAYS SO.** The probe reads the
liquid alone; the atmosphere adds about 100 000 Pa everywhere in the tank.
Without that disclosure a reader takes the surface reading of 0 Pa as an
absolute vacuum, which is the one way that bench could actively mislead —
and it is also the seam `p5-04` then picks up.
"""

from .p5 import lessons as _p5_lessons

UNIT = {
    "code":            "P5",
    "slug":            "pressure",
    "title":           "Pressure",
    "discipline":      "physics",
    # ⚠️ DECORATIVE HERE, AND DELIBERATELY MATCHING `structure.py`.
    "statutory_area":  "Motion and forces",
    "split_rationale": "None. Three statutory statements over four slots — "
                       "the surplus case — with only PRES.02 split, because "
                       "it names two different physical ideas in one line "
                       "and they are a week apart in any scheme of work.",
    "intro":           "The same force can leave a dent or leave nothing at "
                       "all, and what decides it is the area it had to work "
                       "through. Follow that one idea into a tank, under a "
                       "hull and up a mountain.",
    "lessons": _p5_lessons(),
}
