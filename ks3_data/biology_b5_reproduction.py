"""⏸ PARKED — B5 Reproduction is INCOMPLETE and must not build. MRB-244.

Renamed with a leading underscore so `ks3_data/__init__.py::_authored_modules`
skips it (`if mod in _NON_UNIT_MODULES or mod.startswith("_")`). Nothing else
imports `ks3_data.b5`, so the seven authored lesson modules under `ks3_data/b5/`
are inert while this file is named this way.

WHY. Eight authoring passes and the engine pass that owned B5's eight
instrument renderers were killed together by a session limit on 16 Aug 2026.
Seven of the eight lesson records survived and are good work — every
student-facing string lifted byte-identical. The engine pass died before
writing a single renderer.

WHAT IS MISSING, exactly:
  - `ks3_data/b5/lesson_04_gestation_placenta_and_birth.py` — never written.
  - ALL EIGHT renderers: `r_job_match`, `r_gamete_compare`, `r_cycle_dial`,
    `r_crossing_bench`, `r_crosses_panel`, `r_flower_jobs`, `r_what_it_becomes`,
    `r_disperse_sort` — plus their `ACTIVITY_KIND_RENDERERS` /
    `ACTIVITY_KIND_FN` rows, CSS, `wire*` functions and parity rows.
  - `docs/ks3/b5-inventory/PAYLOAD-SCHEMA.md` — never written, so the seven
    surviving records authored their instrument payloads against Design's
    pages and `ks3_data/b5/__init__.py` rather than against an agreed schema.
    RE-CHECK EVERY PAYLOAD against the renderers when they land.

TO RESUME: build the eight instruments, write lesson_04, rename this file back
to `biology_b5_reproduction.py`, then run the full gate set. Do not rename it
back first — B5 currently fails the build BY DESIGN, via the empty-activity
gate added in this same commit, which is exactly the gate that caught this.

The misconception ids are pre-allocated and must not be re-derived:
REPRO-01/02 b5-01 · 03/04 b5-02 · 05/06 b5-03 · 07/08 b5-04 · 09/10 b5-05 ·
11/12 b5-06 · 13/14 b5-07 · 15/16 b5-08, with 17+ for any third belief.
The REPRO section of `docs/ks3/misconception-register.md` is NOT yet written —
write it from the authored data once the unit is complete, as BREATH was.
"""

"""B5 — Reproduction. Eight lessons, Year 8 Biology.

The thin unit wrapper. The lesson records live one per module under
`ks3_data/b5/`, authored against Claude Design's approved reference screens in
`KS3 B5 lessons/` under the MRB-220 build contract.

**Statutory coverage: two statements, eight lessons, and BOTH split.**

    L1 human-reproductive-systems            KS3.B.REP.01a
    L2 gametes-and-fertilisation             KS3.B.REP.01b
    L3 the-menstrual-cycle                   KS3.B.REP.01c
    L4 gestation-placenta-and-birth          KS3.B.REP.01d
    L5 lifestyle-and-the-developing-foetus   KS3.B.REP.01e
    L6 flowers-and-pollination               KS3.B.REP.02a
    L7 fertilisation-seeds-and-fruit         KS3.B.REP.02b
    L8 seed-dispersal                        KS3.B.REP.02c

Neither split needed interpreting. `REP.01` and `REP.02` are the two longest
bullets in the KS3 biology spine and both print their own clause lists; B5's
eight lessons are those lists, in that order. Minted in `substatements.py` in
one pass by the commander, because B3 records that parallel minting silently
loses keys.

**⚑ A STATUTORY GAP IS OPEN AND IT IS RULED — for Mide, not for silent fixing.**

`KS3.B.REP.02` asks for a *"quantitative investigation of some dispersal
mechanisms"*. Design's `seed-dispersal` is a CLASSIFY lesson: eight specimens
sorted by observable structure into five methods, and the student measures
nothing anywhere on the page. Design's own NOTES-B5 flag 43 raises it. Ruled on
16 Aug 2026 (MRB-244): build what is on disk, record the gap, ship. Design
patches it later.

`REP.02c` is minted at the bullet's FULL width — quantitative words included —
rather than narrowed to the classifying that is actually taught, so that what is
missing stays legible against what is claimed. A narrowed clause would make the
register read as fully covered and the gap would vanish from every gate that
reads it.

**⚠️ Tone on the five human lessons is a gate, and Design's treatment stands.**
Confirmed 16 Aug 2026. The register is clinical and function-first, third
person, with no normative language about family structure and no conflation of
sex with gender. `lifestyle-and-the-developing-foetus` carries the load-bearing
case: the placenta is taught as a NEUTRAL surface governed by size and
solubility, which is the only thing that makes its second confrontation — the
belief that anything that goes wrong is the mother's fault — answerable at all.
That refutation and that lesson's legal line are safeguarding copy and are
lifted whole or not at all. Full treatment in `ks3_data/b5/__init__.py`.

**Figures are declared at `needed` and nothing is invented to fill them.**
This unit names more diagram slots than any before it, because anatomy is where
a labelled drawing does work no prose can. Declared so
`docs/ks3/diagram-manifest.md` counts them as sourcing tasks (§4.10, not a
build blocker) rather than losing them.

**review_state is `draft` on every lesson.** Mide is the sole science gate
(§5.10); `draft` → `examiner-reviewed` → `frozen`. ⊕ MRB-221 — the field no
longer gates publishing: §5.10.1's carve-out is revoked and no page carries a
review marker. It records review position, nothing more.
"""

from .b5 import lessons as _b5_lessons

UNIT = {
    "code":            "B5",
    "slug":            "reproduction",
    "title":           "Reproduction",
    "discipline":      "biology",
    "statutory_area":  "Structure and function of living organisms",
    "split_rationale": None,
    "intro":           "Every living thing you have ever seen came from another "
                       "living thing. This unit is about how — in humans, and in "
                       "the flowering plants that solved the same problem "
                       "without being able to move.",
    "lessons": _b5_lessons(),
}
