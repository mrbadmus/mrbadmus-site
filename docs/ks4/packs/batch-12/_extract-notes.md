> **Raw extraction notes, written before the examination.** Where they disagree with `examination/`, `FLAGS.md` or `00-BRIEF.md` (spec references, required-practical numbers, quiz-key alignment), those win.

# Batch 12 — extraction notes

Facts only, read straight from the 14 extracted files in
`04-checked-science-source/` (each file's header gives the routes; `##`
section presence gives everything else). No route-copy `quiz` section exists
in ANY of the 14 files — every route a lesson appears on serves the identical
TH quiz list, so "quiz count per route" below is one number covering every
route listed. The only field that ever differs by route is `higher`.

| # | Lesson | Routes | Quiz count (same on every route) | examiner_tip | fifas | equations | rp (verbatim) | variables |
|---|---|---|---|---|---|---|---|---|
| 1 | electrolysis-extraction | CF CH TF TH | 2 | no | 0 | 4 — Al³⁺/O²⁻ cathode+anode; Cu→Cu²⁺/Cu²⁺→Cu | none | none |
| 2 | electrolysis-aqueous | CF CH TF TH | 2 | no | 0 | 4 — cathode H₂/Cu; anode O₂/Cl₂ | verbatim (RP4 — electrolysis of aqueous solutions, see below) | none |
| 3 | half-equations | CH TH | 2 | no | **1** | 5 — cathode/anode half-equations | none | none |
| 4 | exothermic-endothermic | CF CH TF TH | 2 | no | **1** | 1 — `Q = m × c × ΔT` | verbatim (RP5 — temperature-change variables, see below) | 4 — `Q`, `m`, `c`, `ΔT` |
| 5 | reaction-profiles | CF CH TF TH | 2 | no | 0 | 2 — ΔH=products−reactants; activation energy | none | 2 |
| 6 | bond-energy-calculations | CH TH | 2 | no | **1** | 3 — ΔH=in−out; exo/endo sign rules | none | 1 — `ΔH` |
| 7 | cells-and-batteries | TF TH | 2 | no | 0 | none | none | none |
| 8 | fuel-cells | TF TH | 2 | no | 0 | 1 — `2H₂ + O₂ → 2H₂O` | none | none |
| 9 | calculating-rates | CF CH TF TH | 2 | no | **1** | 2 — rate=quantity÷time; rate=gradient | verbatim (RP6 — thiosulfate/HCl or marble chips, see below) | 1 — `rate` |
| 10 | factors-affecting-rate | CF CH TF TH | 2 | no | 0 | none | verbatim (RP6 — concentration/surface area/temperature, see below) | none |
| 11 | collision-theory | CF CH TF TH | 2 | no | 0 | none | none | 1 |
| 12 | catalysts | CF CH TF TH | 2 | no | 0 | none | none | none |
| 13 | reversible-reactions-equilibrium | CF CH TF TH | 2 | no | 0 | 2 — NH₄Cl⇌NH₃+HCl; CuSO₄·5H₂O⇌... | none | none |
| 14 | effect-of-conditions-equilibrium | CH TH | 2 | no | 0 | 1 — N₂+3H₂⇌2NH₃ ΔH=−92 kJ/mol (Haber) | none | none |

Four `fifas` lessons (#3 half-equations, #4 exothermic-endothermic, #6
bond-energy-calculations, #9 calculating-rates), matching BATCH-PLAN's FIFA
column exactly. The CFIFA form (step C) was appended to all four files, four
FIFA steps kept byte-identical, Convert step added. **None of the four
needed a real conversion** — half-equations balances atoms/charge, not a
measured quantity, so there is no unit to convert at all; exothermic-
endothermic's mass (g), specific heat capacity (J/g°C) and ΔT (°C) are
already matching units for Q=mcΔT; bond-energy-calculations' bond energies
are all already in kJ/mol; calculating-rates' volume (cm³) and time
(already in seconds) match the cm³/s answer directly — notably this is the
one lesson in batches 11–12 whose own QUIZ (q1) does require a cm³/min→
cm³/s-style conversion (4 minutes → 240 seconds), but that conversion sits
in the quiz, not in this FIFA. Same shape as batch-10/11's "nothing to
convert" cases, not batch-8's reaction-time one. `rp` is a dedicated,
populated field on electrolysis-aqueous (RP4), exothermic-endothermic (RP5),
calculating-rates (RP6) and factors-affecting-rate (RP6) — the latter two
share the RP6 practical (rate of reaction) but describe different variables
(concentration/surface area/temperature for factors-affecting-rate;
concentration specifically, with the thiosulfate cross method named, for
calculating-rates) — kept verbatim on both.

## wrong_explanations key check

All 28 quiz items across the 14 files were checked mechanically: every item
has exactly 4 options, `correct_index` is 0 on all 28, and every item's
`wrong_explanations` keys match exactly the indices of its 3 wrong options
(`1,2,3`) — no shifted index anywhere. **No shifted-key defect found
anywhere in this batch.**

## Anything odd

1. **Spec-number agreement with BATCH-PLAN.md is perfect — all 14 of 14
   rows match exactly**, including the two ranged specs
   (`5.6.2.1–5.6.2.3` for reversible-reactions-equilibrium,
   `5.6.2.4–5.6.2.7` for effect-of-conditions-equilibrium, both reproduced
   verbatim in the header) and the two separate-science-prefixed rows
   (`cells-and-batteries` and `fuel-cells`, both `— · 8462 4.5.2.x`). This is
   the first batch seen (9–12) with zero spec disagreements.

2. **FIFA/RP/equations columns also match BATCH-PLAN exactly on all 14
   rows** — no mismatch anywhere in this batch's plan at all, continuing
   batch-11's accuracy.

3. **No `examiner_tip` anywhere in this batch** — same pattern as every
   prior batch (4–11). All 14 files omit the `## examiner_tip` section
   entirely.

4. **No filename needed renaming** — all 14 extracted filenames were already
   clean (no spaces, no parentheses). Step B of the task was not needed.

5. **No subject:slug collisions, despite the expectation.** All 14 slugs
   were searched across `all_subtopics_biology*.py`, `all_subtopics_
   chemistry*.py` and `all_subtopics_physics*.py` by `id`; every one exists
   ONLY under chemistry. The extractor ran cleanly on bare slugs with no
   `subject:slug` qualification needed anywhere, and printed no collision
   error for any of the 14.

6. **`higher` differs on 10 of the 14 lessons** — cells-and-batteries,
   fuel-cells, electrolysis-extraction, electrolysis-aqueous, exothermic-
   endothermic, reaction-profiles, calculating-rates, collision-theory,
   catalysts, reversible-reactions-equilibrium. The other 4 have no `higher`
   section at all (half-equations, bond-energy-calculations, factors-
   affecting-rate, effect-of-conditions-equilibrium) — identical content
   across every tier they appear on. Notably all 4 of the no-`higher`
   lessons already carry an explicit quantitative/HT-flavoured treatment in
   their main `theory` (bond energies, half-equation balancing, rate
   factors, equilibrium shift), so the absence is not a sign of thin content.

7. **Every `higher — … copy` section renders `null`** across all 10 lessons
   that have one (18 copy-sections total: 8 lessons with both a Combined
   Foundation and a Triple Foundation copy, 2 with a Triple-Foundation-only
   copy since cells-and-batteries and fuel-cells are TF/TH only). No route
   actually diverges in its `higher` wording within this batch — same
   finding as batches 9–11.

8. **No `canonical_record` WARNING was printed by the extractor** — the
   extraction run's console output was 14 `wrote …` lines and nothing else.

9. **All 14 lessons' routes match BATCH-PLAN's routes column exactly** — no
   CF/CH/TF/TH discrepancy anywhere.

10. **factors-affecting-rate and calculating-rates share the RP6 practical
    but are NOT duplicate content** — factors-affecting-rate's `rp` names
    concentration, surface area (marble chips vs powder) and temperature as
    the three variables to investigate; calculating-rates' `rp` is scoped to
    the thiosulfate/HCl cross-disappearing method (or the marble-chips mass-
    loss/gas-collection alternative) specifically for its own rate
    calculation. Worth flagging so a reader does not assume one `rp` can be
    copied onto the other lesson unread.
