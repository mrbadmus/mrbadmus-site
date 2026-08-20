"""C3 — Mixtures and separation. Seven lessons, Year 7 Chemistry.

The thin unit wrapper. The lesson records live one per module under
`ks3_data/c3/`, authored against Claude Design's approved reference screens
(`docs/ks3/design-reference/c3/`) under MRB-220.

**Five statements, seven lessons, and two of the splits are the teaching.**
NOTES-C3 §1 records the allocation Design authored to:

    L1 pure-or-mixture                   KS3.C.PIS.01, KS3.C.PIS.02 (mixture half)
    L2 dissolving-and-solutions          KS3.C.PIS.02 (dissolving half)
    L3 filtration                        KS3.C.PIS.04
    L4 evaporation-and-crystallisation   KS3.C.PIS.04
    L5 distillation                      KS3.C.PIS.04
    L6 chromatography                    KS3.C.PIS.04
    L7 proving-something-is-pure         KS3.C.PIS.05

`PIS.03` is diffusion, it belongs to C1, and it is deliberately not re-covered
here.

**PIS.04 names four techniques and gets four lessons, one each.** The
alternative — a single "separating mixtures" lesson — is what §4.2 calls two
lessons wearing one title, and here it would be four.

**PIS.02 is split on the same argument AEC.02 was.** `pure-or-mixture` teaches
what a mixture *is*; `dissolving-and-solutions` teaches the one kind of mixture
the statutory wording singles out. In Design's words: teaching both in one
sitting "is what produces students who think dissolving is the definition of
mixing."

⚠️ **Four lessons claim PIS.04 and that is correct, not a defect.** Coverage
asserts that a statement has at least one owner, never exactly one. A student
who meets the same statutory idea in four techniques has met it four times,
which is the point. Nothing here needs a clause-level split of PIS.04 and none
is minted for it.

The unit runs as a separation toolkit: L1 sets the pure/mixture question, L2
explains why anything dissolves at all, L3–L6 are the four techniques in order
of what they can separate, and L7 turns the toolkit back on itself — melting
point as proof, not appearance.
"""

from .c3 import lessons as _c3_lessons

UNIT = {
    "code":            "C3",
    "slug":            "mixtures-and-separation",
    "title":           "Mixtures and separation",
    "discipline":      "chemistry",
    "statutory_area":  "Pure and impure substances",
    "split_rationale": None,
    "intro":           "Almost nothing you meet is one pure substance. This "
                       "unit is about telling what is in a sample, getting the "
                       "parts back out again, and the one test that settles "
                       "whether something is pure when looking at it cannot.",
    "lessons": _c3_lessons(),
}
