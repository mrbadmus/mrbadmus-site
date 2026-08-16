"""C2 — Atoms, elements and compounds. Six lessons, Year 7 Chemistry.

The thin unit wrapper. The lesson records live one per module under
`ks3_data/c2/`, authored against Claude Design's approved reference screens
(`docs/ks3/design-reference/c2/`) and the measured payload map
(`docs/ks3/c2-inventory/PAYLOAD-MAP.md`) under MRB-220.

**Statutory coverage needs no split, and that is worth saying.** C2 has six
lessons and four `AEC` statements, and NOTES §1 records the allocation
Design authored to:

    L1 the-atom-daltons-model   KS3.C.AEC.01
    L2 elements                 KS3.C.AEC.02a   (the element half)
    L3 compounds                KS3.C.AEC.02b   (the compound and mixture half)
    L4 chemical-symbols         KS3.C.AEC.03a   (the symbols half)
    L5 formulae                 KS3.C.AEC.03b   (the formulae half)
    L6 conservation-of-mass     KS3.C.AEC.04

Two statements are split, both at the grain the bullet itself prints, and both
for the reason NOTES §1 gives: *"AEC.03 is deliberately split across two
lessons: symbols are a notation to be read, formulae are a model of what is in
a particle, and teaching them in one sitting is what makes students think a
formula is just a longer symbol."* AEC.02 splits on the same argument — an
element lesson and a compound lesson are one bullet and two ideas.

`ks3_data/substatements.py` rule 3 says to mint lazily, per unit, at authoring
time, which is what this is. §4.4 rule 3's exactly-once property holds: every
clause is owned by exactly one lesson, and no lesson claims a parent whose
other clause is claimed elsewhere.

**This is a curriculum-mapping judgement, not a rendering one, and it is
Mide's to confirm or reverse.** Reversing either split costs two `covers`
lines and two dict entries in `substatements.py`.
"""

from .c2 import lessons as _c2_lessons

UNIT = {
    "code":            "C2",
    "slug":            "atoms-elements-and-compounds",
    "title":           "Atoms, elements and compounds",
    "discipline":      "chemistry",
    "statutory_area":  "Atoms, elements and compounds",
    "split_rationale": None,
    "intro":           "Everything there has ever been is built from about a "
                       "hundred kinds of atom. This unit is about how you tell "
                       "one kind from another, what happens when they join, and "
                       "the one thing that never changes no matter what you do "
                       "to them.",
    "lessons": _c2_lessons(),
}
