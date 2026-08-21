"""C5 — Types of reaction. Five lessons, Year 8 Chemistry.

The thin unit wrapper. The lesson records live one per module under
`ks3_data/c5/`, authored against Claude Design's approved reference screens
(`docs/ks3/design-reference/c5/`) under MRB-220.

**ONE statutory statement, five lessons.** `KS3.C.CR.03` names four reaction
types in a single bullet; the clauses are minted in `ks3_data/substatements.py`:

    L1 combustion              KS3.C.CR.03a
    L2 thermal-decomposition   KS3.C.CR.03b
    L3 oxidation               KS3.C.CR.03c
    L4 displacement            KS3.C.CR.03d
    L5 which-reaction-is-this  KS3.C.CR.03e

**The fifth lesson is the unit's whole value, and it is why clause `e` exists.**
Naming four types is not the same as telling them apart — that is what an exam
asks and what §5.8 rung 2 is for. Design put the argument in NOTES-C5 §1 and it
is ratified: *"If that reads as over-provision, the compression to lose is
c5-05, and I would argue against it."*

⚖️ **Clause `e` is a commander's ruling (MRB-246) and the one entry in
`substatements.py` that is not a phrase of its own bullet.** `c5-05` teaches the
bullet as a SET rather than as any member of it, and all three legal
alternatives were worse: owning the parent alongside a–d is forbidden by
`validate()` rule 5, sharing a clause is forbidden by rule 4, and
`beyond_statutory` is simply false — telling the four apart is what the bullet
demands, not off-spec content. The full reasoning is written against
`KS3.C.CR.03` in that file.

⚠️ **Clause `e` must never be read as a fifth reaction type. There is no fifth
type.** It is the bullet's integrative demand, and `c5-05`'s eighth item — a
reaction whose honest answer is *none of the four* — is the lesson teaching
that a useful set is not the same as a complete one.

**Four consecutive PROCESS lessons, and each has a different flagship.** §6
warns that identical block lineups should be a coincidence of need, never a
default, and four PROCESS lessons in a row is exactly the shape that produces
one. A parameter bench, a staged run with a cooling gate, a four-tube
controlled investigation and a 4×4 grid: the difference is load-bearing, and a
later pass that harmonises them would be undoing what makes them four lessons.

**The unit assumes C4 throughout** — every reaction here is written as an
equation, and `c5-05` expects the other four to have been met.
"""

from .c5 import lessons as _c5_lessons

UNIT = {
    "code":            "C5",
    "slug":            "types-of-reaction",
    "title":           "Types of reaction",
    "discipline":      "chemistry",
    "statutory_area":  "Chemical reactions",
    "split_rationale": "Eight statutory bullets spanning representation, "
                       "reaction types and acid chemistry; universally taught "
                       "as separate units and too large to schedule as one.",
    "intro":           "Most of the reactions you will ever meet are one of a "
                       "small number of kinds. This unit is about four of them "
                       "— what each one does, what it needs, and how to tell "
                       "which one you are looking at when nobody says.",
    "lessons": _c5_lessons(),
}
