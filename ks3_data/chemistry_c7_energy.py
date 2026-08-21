"""C7 — Energy changes in reactions. Four lessons, Year 9 Chemistry.

The thin unit wrapper. The lesson records live one per module under
`ks3_data/c7/`, authored against Claude Design's approved reference screens
(`docs/ks3/design-reference/c7/`) under MRB-220.

**TWO statutory bullets, four lessons.** `KS3.C.ENER.01` is one bullet and one
lesson. `KS3.C.ENER.02` is one bullet claimed by three, so its clauses are
minted in `ks3_data/substatements.py`:

    L1 energy-and-changes-of-state      KS3.C.ENER.01   (parent, owned whole)
    L2 exothermic-reactions             KS3.C.ENER.02a
    L3 endothermic-reactions            KS3.C.ENER.02b
    L4 measuring-a-temperature-change   KS3.C.ENER.02c

**The third lesson is not a footnote, and that is Design's argument.** NOTES-C7
§1: *"`ENER.02` is one bullet naming two opposite behaviours, and the split
into a PROCESS lesson and a CONTRAST lesson is the only way to give the
endothermic case a hook of its own — otherwise it arrives as a footnote to
exothermic and stays one."* Endothermic reactions are the rarer half and the
harder half, and a lesson that meets them at the bottom of the exothermic page
teaches them as an exception rather than as a direction.

⚖️ **Clause `c` is a commander's ruling (MRB-272) and the second entry in
`substatements.py` that is not a phrase of its own bullet.** `c7-04` owns no
new content — NOTES §1 says so outright — and exists because §7 asks for an
INVESTIGATION here and because every energy figure in the unit is produced by
an apparatus that leaks. All three legal alternatives were worse: owning the
parent alongside a and b is forbidden by `validate()` rule 5, sharing a clause
is forbidden by rule 4, and `beyond_statutory` is simply false. The word that
settles it is **"(qualitative)"**, which is in the bullet: a temperature change
is how a KS3 student decides which of the two a reaction is, and a lesson on
reading it is the bullet's own evidential demand. The full reasoning is written
against `KS3.C.ENER.02` in that file.

⚠️ **Clause `c` must never be read as a third kind of energy change. There are
two.**

**One statutory bullet in this unit is a state change and three are reactions,
and the unit is deliberately ordered that way.** `c7-01` is about water, which
every student has boiled, and it establishes the one idea the other three
depend on: a temperature reading is not an energy reading. Everything after it
— the hand warmer, the cold pack, the leaking beaker — is that same claim in
chemistry's clothes.

**Four lessons, four shapes, and the difference is load-bearing.** A
minute-by-minute heating-curve stepper, a five-beaker predict-then-run bench, an
eight-item sorter, and a plan critique followed by a three-dial rig builder. §6
warns that an identical block lineup should be a coincidence of need and never
a default; the one instrument that IS repeated — the "Three judgements" block
on the first three pages — is Design's own repetition and is modelled as one
family placed three times rather than as three families that look alike. See
`ks3_data/c7/__init__.py` for that argument in full.

**The unit assumes C1 and C6 throughout.** `c7-01` argues entirely in the
particle model, and every reaction on `c7-02`'s bench is one the student has
already run in C5 or C6 without naming its energy.
"""

from .c7 import lessons as _c7_lessons

UNIT = {
    "code":            "C7",
    "slug":            "energy-changes-in-reactions",
    "title":           "Energy changes in reactions",
    "discipline":      "chemistry",
    # ⚠️ DECORATIVE HERE, AND DELIBERATELY MATCHING `structure.py`.
    # `ks3_data.build_units()` takes `statutory_area` from the SKELETON
    # (`structure.py` line 233, "Energetics"), never from this dict, so a value
    # that disagreed with the skeleton would be a lie nothing could catch. The
    # unit's four lessons are chemical-reaction lessons, but the strand code is
    # `ENER` and the register files them under Energetics; that is the record.
    "statutory_area":  "Energetics",
    "split_rationale": "Two statutory bullets — one on changes of state and "
                       "one naming both directions of energy transfer in a "
                       "reaction — taught together everywhere because the "
                       "second is unteachable without the first.",
    "intro":           "Every reaction moves energy. Some push it out into "
                       "the room and some pull it in, and a thermometer in "
                       "the beaker is how you tell which. This unit is about "
                       "which way the energy goes, why nothing is ever "
                       "created or destroyed doing it, and how much a leaking "
                       "beaker costs you when you try to measure it.",
    "lessons": _c7_lessons(),
}
