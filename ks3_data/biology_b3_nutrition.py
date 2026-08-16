"""B3 — Nutrition and digestion. Eight lessons, Year 7 Biology.

The thin unit wrapper. The lesson records live one per module under
`ks3_data/b3/`, authored against Claude Design's approved reference screens in
`KS3 B3 lessons/` under the MRB-220 build contract.

**Statutory coverage: six statements, eight lessons, and one SPLIT.**

    L1 a-balanced-diet                    KS3.B.NUT.01
    L2 food-tests                         KS3.WS.* (INVESTIGATION, §5.7.1)
    L3 energy-in-food-and-what-you-need   KS3.B.NUT.02a  (the B3 half)
    L4 when-diet-goes-wrong               KS3.B.NUT.03
    L5 the-digestive-system               KS3.B.NUT.04a  (tissues and organs)
    L6 enzymes-in-digestion               KS3.B.NUT.04b  (enzymes as catalysts)
    L7 absorption-and-the-small-intestine KS3.B.NUT.04c  (adaptations to function)
    L8 bacteria-in-the-gut                KS3.B.NUT.05

`KS3.B.NUT.04` splits three ways at the grain its own bullet prints — tissues
and organs / enzymes as catalysts / adaptations to function are three clauses
and three lessons. `substatements.py` rule 3 says to mint lazily, per unit, at
authoring time, which is what this is.

`KS3.B.NUT.02` splits between B3 and Physics P2, ruled by Mide on 16 Aug 2026
(MRB-232). B3 owns what you need and why; P2 keeps comparing energy values from
labels in kJ. The full ruling is in `docs/ks3/statutory-register.md` and it is
not to be re-opened from one file — the two sources disagreed for months and
each read as self-consistent alone.

**L2 anchors `covers` on a Working Scientifically statement**, which is the
rule at architecture.md §5.7.1 rather than a judgement made here: it is an
INVESTIGATION lesson that teaches no new subject content by design, and WS is
exempt from the exactly-once rule (§5.7).

**review_state is `draft` on every lesson.** Mide is the sole science gate
(§5.10); `draft` → `examiner-reviewed` → `frozen`. ⊕ MRB-221 — the field no
longer gates publishing: §5.10.1's carve-out is revoked and no page carries a
review marker. It records review position, nothing more.
"""

from .b3 import lessons as _b3_lessons

UNIT = {
    "code":            "B3",
    "slug":            "nutrition-and-digestion",
    "title":           "Nutrition and digestion",
    "discipline":      "biology",
    "statutory_area":  "Structure and function of living organisms",
    "split_rationale": None,
    "intro":           "Everything you have ever eaten was taken apart and "
                       "rebuilt into you. This unit is about what your body "
                       "needs, what happens to food after you swallow it, and "
                       "why a gut full of bacteria is a good thing.",
    "lessons": _b3_lessons(),
}
