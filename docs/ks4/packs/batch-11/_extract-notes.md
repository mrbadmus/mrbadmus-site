> **Raw extraction notes, written before the examination.** Where they disagree with `examination/`, `FLAGS.md` or `00-BRIEF.md` (spec references, required-practical numbers, quiz-key alignment), those win.

# Batch 11 — extraction notes

Facts only, read straight from the 16 extracted files in
`04-checked-science-source/` (each file's header gives the routes; `##`
section presence gives everything else). No route-copy `quiz` section exists
in ANY of the 16 files — every route a lesson appears on serves the identical
TH quiz list, so "quiz count per route" below is one number covering every
route listed. The only field that ever differs by route is `higher`.

| # | Lesson | Routes | Quiz count (same on every route) | examiner_tip | fifas | equations | rp (verbatim) | variables |
|---|---|---|---|---|---|---|---|---|
| 1 | model-of-the-atom | CF CH TF TH | 2 | no | 0 | none | none | none |
| 2 | subatomic-particles | CF CH TF TH | 2 | no | 0 | none | none | none |
| 3 | relative-atomic-mass | CF CH TF TH | 2 | no | **1** | 3 — mass number; neutrons; `Ar = Σ(% abundance × mass number) ÷ 100` | none | none |
| 4 | electronic-structure | CF CH TF TH | 2 | no | 0 | none | none | none |
| 5 | group-7 | CF CH TF TH | 3 | no | 0 | 3 — halogen displacement equations (Cl₂+NaBr, Cl₂+KI, Br₂+KI) | none | none |
| 6 | transition-metals | TF TH | 2 | no | 0 | none | none | none |
| 7 | mass-changes-reactions | CF CH TF TH | 2 | no | **1** | none | none | none |
| 8 | chemical-measurements | CF CH TF TH | 2 | no | **1** | 1 — `% uncertainty = (uncertainty ÷ measured value) × 100` | none | 1 — `% uncertainty` |
| 9 | moles | CH TH | 2 | no | **1** | 4 — n=m÷Mr; m=n×Mr; particles=n×Nₐ; %mass | none | 4 — `n`, `m`, `Mr`, `Nₐ` |
| 10 | amounts-in-equations | CH TH | 2 | no | **1** | 3 — n=m÷Mr; % yield; atom economy | none | 3 — `n`, `m`, `Mr` |
| 11 | oxidation-reduction | CF CH TF TH | 2 | no | 0 | 3 — OIL RIG definitions | none | none |
| 12 | salts-neutralisation | CF CH TF TH | 2 | no | 0 | 3 — H⁺+OH⁻→H₂O; acid+alkali; BaCl₂+Na₂SO₄ | verbatim (RP3 — soluble salt by add-excess-solid, see below) | none |
| 13 | ph-scale | CF CH TF TH | 2 | no | 0 | none | none | none |
| 14 | strong-weak-acids | CH TH | 2 | no | 0 | 2 — HCl full dissociation; CH₃COOH ⇌ partial | none | none |
| 15 | electrolysis-principles | CF CH TF TH | 2 | no | 0 | none | none | none |
| 16 | electrolysis-molten | CF CH TF TH | 2 | no | 0 | 4 — 2NaCl→2Na+Cl₂; PbBr₂→Pb+Br₂; cathode/anode half-eqns | verbatim (RP4 — electrolysis of lead(II) bromide, see below) | none |

Five `fifas` lessons (#3 relative-atomic-mass, #7 mass-changes-reactions, #8
chemical-measurements, #9 moles, #10 amounts-in-equations), matching
BATCH-PLAN's FIFA column exactly. The CFIFA form (step C) was appended to
all five files, four FIFA steps kept byte-identical, Convert step added.
**None of the five needed a real conversion** — relative-atomic-mass's
percentages and mass numbers are already dimensionless/matching; mass-
changes-reactions and amounts-in-equations keep mass in grams throughout;
chemical-measurements' volume and its uncertainty are both already in cm³;
moles' mass is already in grams against Ar in g/mol. Same shape as
batch-10's two cases (both "nothing to convert"), not batch-8's
reaction-time case. `rp` is a dedicated, populated field on
salts-neutralisation (RP3) and electrolysis-molten (RP4), both kept
verbatim.

## wrong_explanations key check

All 33 quiz items across the 16 files were checked mechanically: every item
has exactly 4 options, `correct_index` is 0 on all 33, and every item's
`wrong_explanations` keys match exactly the indices of its 3 wrong options
(`1,2,3`) — no shifted index anywhere. **No shifted-key defect found
anywhere in this batch.**

## Anything odd

1. **Spec-number disagreement with BATCH-PLAN.md is almost gone in this
   batch — only 1 of 16 rows disagrees**, a sharp improvement on batch-10's
   7-of-15. #12 salts-neutralisation: the plan guessed the fine sub-clause
   `5.4.2.3`; the data's own header gives the coarser range
   `5.4.2.2–5.4.2.3` (and the extracted filename, by the extractor's own
   first-number-of-a-range rule, takes `5.4.2.2`). All other 15 rows match
   BATCH-PLAN's spec column exactly, including the two deliberately-blank-
   core rows `transition-metals` (`— · 8462 4.1.3.1–4.1.3.2`) and
   `cells-and-batteries`-style separate-science prefix convention. As with
   every prior batch, the extractor's spec comes straight off the data;
   BATCH-PLAN's spec column should not be cited directly for row #12.

2. **FIFA/RP/equations columns match BATCH-PLAN exactly on all 16 rows** —
   no mismatch anywhere in that part of the plan, unlike the spec-number
   column. This batch's plan is unusually accurate.

3. **No `examiner_tip` anywhere in this batch** — same pattern as every
   prior batch (4–10). All 16 files omit the `## examiner_tip` section
   entirely.

4. **No filename needed renaming** — all 16 extracted filenames were already
   clean (no spaces, no parentheses). Step B of the task was not needed.

5. **No subject:slug collisions, despite the expectation.** All 16 slugs
   were searched across `all_subtopics_biology*.py`, `all_subtopics_
   chemistry*.py` and `all_subtopics_physics*.py` by `id`; every one of them
   exists ONLY under chemistry — including `model-of-the-atom` and
   `subatomic-particles`, which sit in the `atomic-structure` topic that
   physics also uses a topic of the same NAME for, but the lesson `id`s
   themselves never collide. The extractor ran cleanly on bare slugs with no
   `subject:slug` qualification needed anywhere, and printed no collision
   error for any of the 16.

6. **`higher` differs on 8 of the 16 lessons** — relative-atomic-mass,
   electronic-structure, group-7, transition-metals, oxidation-reduction,
   ph-scale, electrolysis-principles, electrolysis-molten. The other 8 have
   no `higher` section at all (model-of-the-atom, subatomic-particles,
   mass-changes-reactions, chemical-measurements, moles, amounts-in-
   equations, salts-neutralisation, strong-weak-acids) — identical content
   across every tier they appear on.

7. **Every `higher — … copy` section renders `null`** across all 8 lessons
   that have one (14 copy-sections total: 6 lessons with both a Combined
   Foundation and a Triple Foundation copy, 2 with a Triple-Foundation-only
   copy since transition-metals is TF/TH only). No route actually diverges
   in its `higher` wording within this batch — same finding as batch-9 and
   batch-10.

8. **No `canonical_record` WARNING was printed by the extractor** — the
   extraction run's console output was 16 `wrote …` lines and nothing else.

9. **All 16 lessons' routes match BATCH-PLAN's routes column exactly** — no
   CF/CH/TF/TH discrepancy anywhere, unlike the spec-number column.
