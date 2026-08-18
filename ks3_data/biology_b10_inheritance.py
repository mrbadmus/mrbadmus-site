"""B10 — Inheritance and DNA. Five lessons, Biology.

The thin unit wrapper. The lesson records live one per module under
`ks3_data/b10/`, authored against Claude Design's approved reference screens in
`docs/ks3/design-reference/b10/` under the MRB-220 build contract, and against the
payload schema written before dispatch at
`docs/ks3/b10-inventory/PAYLOAD-SCHEMA.md`.

    L1 variation-continuous-and-discontinuous  variation-plotter
    L2 chromosomes-genes-and-dna               zoom-bench
    L3 how-we-worked-out-dna                   model-builder
    L4 passing-it-on-heredity                  pea-cross
    L5 what-makes-a-species                    species-cases

**Slugs match `ks3_data/structure.py` character for character.** They are the
join for scheme-of-work rows, progress records and every `requires` edge, and
they are permanent (§8.4).

**Four rail stops per page, all four tick (MRB-249).** The third stop is the
band section and borrows its completion from the instrument via `mirrors`. Full
treatment in `ks3_data/b10/__init__.py`.

**review_state is `draft` on every lesson.** Mide is the sole science gate
(§5.10); `draft` → `examiner-reviewed` → `frozen`. Since MRB-221 the field no
longer gates publishing and no page carries a review marker — it records review
position, nothing more.
"""

from .b10 import lessons as _b10_lessons

UNIT = {
    "code":            "B10",
    "slug":            "inheritance-and-dna",
    "title":           "Inheritance and DNA",
    "discipline":      "biology",
    "statutory_area":  "Genetics and evolution",
    "split_rationale": None,
    # ⚖️ The unit intro is the commander's, not lifted: Design's deliveries are
    # lesson pages and draw no unit card. It has one job — say what the five
    # lessons add up to, in the order they are met, without naming a year.
    "intro":           "Every one of your characteristics arrived from "
                       "somewhere, and most of them arrived twice. This unit "
                       "starts with the variation you can measure in a room "
                       "full of people, works down through chromosomes and "
                       "genes to the molecule the instructions are written in, "
                       "follows how that structure was worked out, and ends "
                       "with the question of what makes two organisms the same "
                       "species at all.",
    "lessons": _b10_lessons(),
}
