"""C1 — Particles and their behaviour. Six lessons, Year 7 Chemistry.

The thin unit wrapper. The lesson records live one per module under
`ks3_data/c1/`, authored against Claude Design's approved reference screens
(`docs/ks3/design-reference/c1/`) and the measured payload map
(`docs/ks3/c1-inventory/PAYLOAD-MAP.md`) under MRB-220 / MRB-228.

**This file used to hold all six lessons inline, and that body is superseded,
not deleted.** It is reachable in git history, which is the record. C1 was the
Phase 1 vertical slice (architecture.md §9) and then the subject of MRB-177's
structural revision; both are in the history of this path, and the MRB-177
revision is what Design's delivery now closes at the level of shape rather
than instance-by-instance (PAYLOAD-MAP §7.5). `biology_b1_cells.py` made the
same move for the same reason.

**Nothing about the unit's identity moves in the rebuild.** All six slugs,
titles and families are identical live vs Design and match
`ks3_data/structure.py:156–164` character for character — verified rather than
assumed, PAYLOAD-MAP §7.1. So there are no URL breaks, no `requires` edges to
repoint, no redirects and no scheme-of-work row moves.

**Statutory allocation is unchanged by the rebuild.** C1 has six lessons and
five statutory statements, so §11 decision 11 bites here first: `KS3.C.PNM.01`
is split into three clause-level sub-IDs (see `substatements.py`); nothing else
needed splitting. Every subject-content clause is owned exactly once:

    L1 particle-model            KS3.C.PNM.01a
    L2 solids-liquids-and-gases  KS3.C.PNM.01b
    L3 changes-of-state          KS3.C.PNM.02, KS3.P.PHYC.01
    L4 gas-pressure              KS3.C.PNM.01c
    L5 diffusion                 KS3.C.PIS.03, KS3.P.PHYC.04
    L6 testing-the-model         KS3.WS.ATT.02

**L6 anchors `covers` on a Working Scientifically statement**, which is the
rule at architecture.md §5.7.1 rather than a judgement made here. It is an
INVESTIGATION lesson that teaches no new subject content by design — it tests
the model built in L1–L5 — but §10.2 requires `covers` non-empty. Anchoring on
`KS3.WS.ATT.02` (*theories develop as earlier explanations are modified to take
account of new evidence*) is honest, because it is exactly what the lesson
does, and legal, because WS is exempt from the exactly-once rule (§5.7). That
was raised by this slice as a design decision, ruled 26 Jul 2026, and promoted
to a general rule so all 18 INVESTIGATION lessons follow one pattern.

**Misconception coverage is unchanged too.** PART-01 to PART-13 are elicited
and confronted in both the superseded and the rebuilt version, and each lands
in the same lesson in both (PAYLOAD-MAP §7.4). Nothing in
`docs/ks3/misconception-register.md` moves.

**review_state is `draft` on every lesson.** Mide is the sole science gate
(§5.10); `draft` → `examiner-reviewed` → `frozen`.
"""

from .c1 import lessons as _c1_lessons

UNIT = {
    "code":            "C1",
    "slug":            "particles-and-their-behaviour",
    "title":           "Particles and their behaviour",
    "discipline":      "chemistry",
    "statutory_area":  "The particulate nature of matter",
    "split_rationale": None,
    "intro":           "Everything around you — this page, the air in your lungs, "
                       "the water in a glass — is built from particles far too "
                       "small to see. This unit builds that idea, then pushes it "
                       "until it nearly breaks.",
    "lessons": _c1_lessons(),
}
