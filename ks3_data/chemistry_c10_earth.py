"""C10 — The Earth and its atmosphere. Six lessons, Year 9 Chemistry.

The thin unit wrapper. The lesson records live one per module under
`ks3_data/c10/`, authored against Claude Design's approved reference screens
(`docs/ks3/design-reference/c10/`).

    L1 inside-the-earth                   KS3.C.EA.01 + KS3.C.EA.02
    L2 three-ways-to-make-a-rock          KS3.C.EA.03a
    L3 the-rock-cycle                     KS3.C.EA.03b
    L4 a-planet-with-limits               KS3.C.EA.04
    L5 whats-in-the-air                   KS3.C.EA.05
    L6 carbon-dioxide-humans-and-climate  KS3.C.EA.06

`KS3.C.EA.03` is clause-split under §11.11; the ruling, the reason the two
sub-IDs are NOT minted ahead of the lessons that need them, and the finding
about the delivery's unstatutory seventh page are all in
`ks3_data/c10/__init__.py`.

── THE UNIT IS ONE ARGUMENT ─────────────────────────────────────────────

The Earth is a closed box of finite stuff with a thin skin of gas round it.
L1–L3 are about the rock: what the box is made of, and how the same atoms are
made into three kinds of rock and then unmade again. L4 turns that on the
student — one-way extraction out of a fixed stock — and L5–L6 do the same
thing for the gas, which is the other finite thing on the list and the one we
are changing fastest.

⚠️ **THE UNIT ASSUMES C9.** L4's loop is C9-03's extraction argument run
backwards: C9 asks what it costs to get a metal out of a rock, and L4 asks
what it costs not to have to. Nothing here re-teaches reduction or the
reactivity series.
"""

from .c10 import lessons as _c10_lessons

UNIT = {
    "code":            "C10",
    "slug":            "the-earth-and-its-atmosphere",
    "title":           "The Earth and its atmosphere",
    "discipline":      "chemistry",
    # ⚠️ DECORATIVE HERE, AND DELIBERATELY MATCHING `structure.py`.
    "statutory_area":  "Earth and atmosphere",
    "split_rationale": "Six statutory bullets under one heading, taught as "
                       "six lessons because the compound rock bullet names "
                       "two ideas — making the three rock types, and the "
                       "cycle that unmakes them — that no scheme of work "
                       "teaches in one sitting.",
    "intro":           "Everything we build with came out of the crust, and "
                       "the thin skin of gas above it is the other finite "
                       "thing on the list.",
    "lessons": _c10_lessons(),
}
