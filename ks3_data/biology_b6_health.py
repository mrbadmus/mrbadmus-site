"""B6 — Health and drugs. Three lessons, Year 9 Biology.

The thin unit wrapper. The lesson records live one per module under
`ks3_data/b6/`, authored against Claude Design's approved reference screens in
`docs/ks3/design-reference/b6/` under the MRB-220 build contract.

**Statutory coverage: one statement, three lessons, one SPLIT.**

    L1 what-drugs-do-to-the-body           KS3.B.HLTH.01a
    L2 alcohol-and-smoking                 KS3.B.HLTH.01b
    L3 substance-misuse-and-decisions      KS3.B.HLTH.01c

⚑ The split is a curriculum-mapping call rather than a reading of the bullet's
punctuation, and it is the weakest-provenance mint in `substatements.py`.
Flagged for Mide there and in `ks3_data/b6/__init__.py`. The alternative is a
two-way split with two lessons sharing one clause, which §4.4 rule 3 forbids.

**⚠️ Tone is a gate on every page of this unit**, and Design's treatment is
ruled: clinical, no scare copy, no euphemism, no doses, no thresholds, no
methods. Two items are settled and must not be re-opened — **the vape paragraph
(NOTES-B6 flag 9) is approved by Mide and ships exactly as written**, and
**paracetamol's "may feel fine for a day or two" (flag 4) stays**, because it is
the clause that saves a life. Full treatment in `ks3_data/b6/__init__.py`.

**This unit opens the `DRUG` misconception family** — six entries, two per
lesson, with ranges pre-allocated per lesson so three parallel authors cannot
collide as B4's five did.

**No figures.** NOTES-B6 flag 14: the unit names no diagram slots and draws
none; its visuals are the three instruments. Measured, not omitted.

**review_state is `draft` on every lesson.** Mide is the sole science gate
(§5.10); `draft` → `examiner-reviewed` → `frozen`. ⊕ MRB-221 — the field no
longer gates publishing: §5.10.1's carve-out is revoked and no page carries a
review marker. It records review position, nothing more.
"""

from .b6 import lessons as _b6_lessons

UNIT = {
    "code":            "B6",
    "slug":            "health-and-drugs",
    "title":           "Health and drugs",
    "discipline":      "biology",
    "statutory_area":  "Structure and function of living organisms",
    "split_rationale": None,
    "intro":           "A drug is any substance that changes the way the body "
                       "works — which makes caffeine one, and paracetamol one, "
                       "and that is a description rather than a judgement. This "
                       "unit is about what these molecules actually do once "
                       "they are in your blood, and how to tell a claim about "
                       "them from evidence for it.",
    "lessons": _b6_lessons(),
}
