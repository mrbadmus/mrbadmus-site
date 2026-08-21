"""C4 — Chemical reactions. Five lessons, Year 8 Chemistry.

The thin unit wrapper. The lesson records live one per module under
`ks3_data/c4/`, authored against Claude Design's approved reference screens
(`docs/ks3/design-reference/c4/`) under MRB-220.

**Three statements, five lessons, and every split is a seam the bullet names
out loud.** NOTES-C4 §1 records the allocation Design authored to, and the
clauses are minted in `ks3_data/substatements.py`:

    L1 chemical-vs-physical-change     KS3.C.CR.01a  (what counts as a reaction)
    L2 reactions-rearrange-atoms       KS3.C.CR.01b  (the rearrangement itself)
    L3 word-equations                  KS3.C.CR.02a  (the words half)
    L4 mass-in-a-reaction              KS3.C.AEC.04b (conservation, in reactions)
    L5 symbol-equations-and-balancing  KS3.C.CR.02b  (the symbols half)

The unit is ONE ARGUMENT IN FIVE STEPS: tell a reaction from a change, see
that atoms are rearranged rather than made, write that in words, weigh it,
then write it in symbols and balance it. L5 depends on C2's formulae.

**CR.01 is split because the recognition half has to be taught wrong-first.**
`REACT-01` is the belief that irreversibility is what makes a change chemical,
and a student who meets "what counts" and "it is a rearrangement" in one
sitting never has that belief elicited at all. L1 exists to draw it out and
break it; L2 can then say what a reaction actually is.

**CR.02 is split on the argument AEC.03 was.** A word equation is a SENTENCE;
a symbol equation is a MODEL WITH NUMBERS IN IT. Design's words: the students
who meet them together learn that a formula is a longer name.

⚖️ **L4 owns `KS3.C.AEC.04b`, and that clause was minted for it (MRB-246).**
NOTES-C4 §1 asked for a §4.6 ruling — may a QUANTITATIVE lesson REFERENCE a
statement an earlier unit owns, without double-counting coverage? The answer
is no, and not as a matter of taste: `validate()` rule 3 requires non-empty
`covers` on every authored lesson, so "reference and own nothing" is not a
shape this build has. The alternative Design offered — fold the lesson into C2
and lose the four-part treatment — was the worse trade, because MRB-204's
treatment is the entire point of a QUANTITATIVE lesson and mass in a REACTION
belongs in the reactions unit.

So the bullet was split instead, at the seam it names out loud: "conservation
of mass changes of state **and** chemical reactions". C2's
`conservation-of-mass` owns clause `a` and establishes the principle where
nothing new is made; this unit's `mass-in-a-reaction` owns clause `b` and
carries it into the case where something is. c2-06's `covers` narrowed from
the parent to clause `a` as part of that ruling and not one student-facing
byte of it moved — `covers` records which lesson is ANSWERABLE for a clause,
never which lesson may mention it.

⚠️ **L4 is seven rail stops, the most in the course so far.** That is the
four-part treatment costing three stops of its own, and it is correct rather
than generous: the rule, the drawing, the worked example and the student's own
run are four separate things a student does, and MRB-249 matches Design
stop-for-stop.
"""

from .c4 import lessons as _c4_lessons

UNIT = {
    "code":            "C4",
    "slug":            "chemical-reactions",
    "title":           "Chemical reactions",
    "discipline":      "chemistry",
    "statutory_area":  "Chemical reactions",
    "split_rationale": "Eight statutory bullets spanning representation, "
                       "reaction types and acid chemistry; universally taught "
                       "as separate units and too large to schedule as one.",
    "intro":           "Some changes make something new and some only move "
                       "what was already there. This unit is about telling "
                       "which is which, seeing what a reaction does to the "
                       "atoms underneath, and learning the two ways chemists "
                       "write one down.",
    "lessons": _c4_lessons(),
}
