"""B4 — Breathing and gas exchange. Five lessons, Year 8 Biology.

The thin unit wrapper. The lesson records live one per module under
`ks3_data/b4/`, authored against Claude Design's approved reference screens in
`KS3 B4 lessons/` under the MRB-220 build contract.

**Statutory coverage: four statements, five lessons, and one SPLIT.**

    L1 the-gas-exchange-system              KS3.B.GAS.01a  (the parts)
    L2 how-breathing-works                  KS3.B.GAS.02
    L3 alveoli-built-for-exchange           KS3.B.GAS.01b  (adaptations)
    L4 exercise-asthma-and-smoking          KS3.B.GAS.03
    L5 stomata-and-gas-exchange-in-plants   KS3.B.GAS.04

`KS3.B.GAS.01` splits at the grain its own bullet prints — *structure and
functions … including adaptations to function* is two clauses and two lessons,
taught two lessons apart. `substatements.py` rule 3 says to mint lazily, per
unit, at authoring time, which is what this is.

**⚑ A STATUTORY GAP IS OPEN AND IT IS RULED — for Mide, not for silent fixing.**

`KS3.B.GAS.02` asks for *"simple measurements of lung volume"* and this unit
contains none. Design's `how-breathing-works` is a pressure model with volume
READOUTS; the student takes no measurement. Design's own NOTES-B4.md flag 1
raises it and offers three fixes (a fifth section on b4-02, a sixth lesson, or
accept the gap), recommending the first. Ruled on 16 Aug 2026 (MRB-244): build
what is on disk, record the gap, ship. Design patches it later.

The statement is owned WHOLE by `how-breathing-works` rather than narrowed to
the clauses that are taught, so the register reads as covered-with-a-gap rather
than as covered. Narrowing it would make the gap disappear from every gate that
reads the register, which is the one outcome nobody wants.

**Figures are declared at `needed` and nothing is invented to fill them.**
Design's legal lines name diagram slots that have no artwork. They are declared
so `docs/ks3/diagram-manifest.md` counts them as sourcing tasks (§4.10, not a
build blocker) rather than losing them.

**review_state is `draft` on every lesson.** Mide is the sole science gate
(§5.10); `draft` → `examiner-reviewed` → `frozen`. ⊕ MRB-221 — the field no
longer gates publishing: §5.10.1's carve-out is revoked and no page carries a
review marker. It records review position, nothing more.
"""

from .b4 import lessons as _b4_lessons

UNIT = {
    "code":            "B4",
    "slug":            "breathing-and-gas-exchange",
    "title":           "Breathing and gas exchange",
    "discipline":      "biology",
    "statutory_area":  "Structure and function of living organisms",
    "split_rationale": None,
    "intro":           "You breathe about twenty thousand times a day without "
                       "deciding to. This unit is about what the air is for, "
                       "how it gets in and out when your lungs contain no "
                       "muscle at all, and why the same problem has the same "
                       "solution in a lung and in a leaf.",
    "lessons": _b4_lessons(),
}
