> **Raw extraction notes, written before the examination.** Where they disagree with `examination/`, `FLAGS.md` or `00-BRIEF.md` (spec references, required-practical numbers, quiz-key alignment), those win.

# Batch 16 — extraction notes

Facts only, read straight from the 16 extracted files in
`04-checked-science-source/` (each file's header gives the routes; `##`
section presence gives everything else). No route-copy `quiz` section exists
in ANY of the 16 files — every route a lesson appears on serves the identical
TH quiz list, so "quiz count per route" below is one number covering every
route listed. The only field that ever differs by route is `higher`.

| # | Lesson | Routes | Quiz count (same on every route) | examiner_tip | fifas | equations | rp (verbatim) | variables |
|---|---|---|---|---|---|---|---|---|
| 1 | mass-number-isotopes | CF CH TF TH | 2 | no | **1** | 1 — Protons=Z; Neutrons=A−Z; Electrons=protons | none | 0 |
| 2 | nuclear-equations | CF CH TF TH | 2 | no | **1** | 3 — alpha/beta/gamma decay balancing rules | none | 0 |
| 3 | half-lives | CF CH TF TH | 2 | no | **1** | 1 — n = time ÷ half-life; N = N₀×(½)ⁿ | none | 0 |
| 4 | radioactive-contamination | CF CH TF TH | 2 | no | 0 | none | none | 0 |
| 5 | background-radiation | TF TH | 2 | no | 0 | 1 — corrected count rate / dose | none | 0 |
| 6 | uses-of-nuclear-radiation | TF TH | 2 | no | 0 | none | none | 0 |
| 7 | nuclear-fission | TF TH | 2 | no | 0 | 1 — chain-reaction relation | none | 0 |
| 8 | nuclear-fusion | TF TH | 2 | no | 0 | 1 — fusion relation | none | 0 |
| 9 | scalar-vector-quantities | CF CH TF TH | 2 | no | 0 | 1 | none | 0 |
| 10 | contact-noncontact-forces | CF CH TF TH | 2 | no | 0 | none | none | 0 |
| 11 | gravity | CF CH TF TH | 2 | no | **1** | 1 — W = m × g | none | 3 |
| 12 | resultant-forces | CF CH TF TH | 2 | no | 0 | none | none | 0 |
| 13 | resolving-forces | TH | 2 | no | **1** | 3 — R=√(Fx²+Fy²); θ=arctan(Fy/Fx) | none | 4 |
| 14 | free-body-diagrams | TH | 2 | no | 0 | 2 | none | 0 |
| 15 | work-done-energy-transfer | CF CH TF TH | 2 | no | **1** | 1 — W = F × s | none | 3 |
| 16 | forces-elasticity | CF CH TF TH | 2 | no | **1** | 1 — F = k × e | verbatim (RP18 — F–e for a spring, see below) | 3 |

Seven `fifas` lessons (#1, #2, #3, #11, #13, #15, #16), matching BATCH-PLAN's
FIFA column exactly. The CFIFA form (step C) was appended to all seven files,
the four FIFA steps kept byte-identical, Convert step added to each.

**No FIFA in this batch needed a real unit conversion.** #1 and #2 (mass
number / atomic number) are dimensionless counts, not measured quantities —
there is no unit to convert at all. #3 half-lives gives both times in hours,
and `n = total time ÷ half-life` is a same-unit ratio that cancels before any
seconds conversion would apply. #11, #13, #15, #16 all give every quantity
already in SI (kg/N/kg, N, m, N/m) — nothing to convert on any of them.

## One worked example chains two equations (rule 3)

**#3 half-lives.** Its single FIFA's `F` step states BOTH relationships at
once — `Number of half-lives = total time ÷ half-life` AND
`remaining = initial × (½)ⁿ` — then genuinely uses the first to compute `n`
(the `I` step) before applying the second (the next `F` step) to reach the
activity. This is a real two-equation chain under the 2 Oct 2026 four-lesson-
rules ruling (rule 3: "a calculation that chains two equations… gets its own
worked example, set out as 'Step 1 … Step 2 …', before any pupil is asked to
do one"). The raw source data presents it as one F-I-F-A FIFA rather than
two labelled steps — flagged here for Design's lesson-writing to split
properly, not silently ported as a single FIFA. No other FIFA in either
batch 15 or 16 chains two equations.

## wrong_explanations key check

All 32 quiz items across the 16 files were checked mechanically: every item
has exactly 4 options, the `true` option sits at index 0 on all 32, and every
item's `wrong_explanations` keys match exactly the indices of its 3 wrong
options (`1,2,3`) — no shifted index anywhere. **No shifted-key defect found
anywhere in this batch.**

## Anything odd

1. **Spec-number agreement with BATCH-PLAN.md is perfect on slug/topic/route
   for all 16 of 16 rows, with the same by-design digit-string divergence
   noted in batch-15 on the triple-only/HT-only lessons.** `background-
   radiation`, `uses-of-nuclear-radiation`, `nuclear-fission` and
   `nuclear-fusion` are 8463-only (BATCH-PLAN cites `8463 4.4.3.1` etc.);
   the data's own `spec` field instead reads `6.4.3 (physics only)` and so
   on — the same internal "6." convention with an inline annotation rather
   than AQA's real separate-physics "4." numbering, as explained in
   batch-15's note 1. **`resolving-forces` and `free-body-diagrams` are a
   further wrinkle**: BATCH-PLAN itself marks their spec with a `?`
   (`6.5.1.4? · 8463 4.5.1.4`), flagging its own uncertainty about the exact
   sub-point — and the data's `spec` field agrees with that uncertainty
   rather than resolving it: both read only `6.5.1 (HT only)`, one digit
   short of BATCH-PLAN's guessed `6.5.1.4`. Not a mismatch to fix; the data
   is simply less granular than BATCH-PLAN's own speculative number.

2. **FIFA/equations columns match BATCH-PLAN exactly on all 16 rows** — no
   mismatch anywhere in this batch's plan at all. **RP**: BATCH-PLAN marks
   only `forces-elasticity` (#16) as RP=Y, and that is the only lesson in
   this batch with a populated `rp` field (RP18, spring force–extension) —
   exact agreement.

3. **No `examiner_tip` anywhere in this batch** — same pattern as every
   prior batch. All 16 files omit the `## examiner_tip` section entirely.

4. **Six filenames needed renaming** (step B): the four `(physics only)`
   nuclear lessons (`background-radiation`, `uses-of-nuclear-radiation`,
   `nuclear-fission`, `nuclear-fusion`) and the two `(HT only)` forces
   lessons (`resolving-forces`, `free-body-diagrams`) all had their
   parenthetical annotation stripped from the filename (spec digits only),
   kept verbatim in the header. `resolving-forces` and `free-body-diagrams`
   both reduce to the SAME spec stem `6.5.1` but remain distinct files
   because the slug differs (`physics-6.5.1-resolving-forces.md` vs
   `physics-6.5.1-free-body-diagrams.md`) — no collision.

5. **No subject:slug collisions were actually tested** — all 16 slugs were
   passed as `physics:<slug>` from the start, so the extractor never
   searched biology/chemistry for them; the console output was 16 clean
   `wrote …` lines with no collision error printed for any slug.

6. **Eight of sixteen lessons carry a `higher` section**: `half-lives`,
   `background-radiation`, `uses-of-nuclear-radiation`, `nuclear-fission`,
   `nuclear-fusion`, `resultant-forces`, `resolving-forces` and
   `free-body-diagrams`. Of these, **two (`resolving-forces`,
   `free-body-diagrams`) are Triple-Higher-ONLY and so have no sibling
   route to diff their `higher` field against** — no copy section at all,
   the same shape batch-13 found for its two TH-only lessons. The other six
   each produce one or two route-copy sections (one TF copy for the four
   TF/TH-only lessons; CF and TF copies for the two CF/CH/TF/TH lessons
   `half-lives` and `resultant-forces`) — six lessons × route-copies = 8
   copy sections total.

7. **Every `higher — … copy` section renders `null`** across all 8 copy
   sections — no route actually diverges in its `higher` wording within
   this batch, same finding as every prior batch.

8. **No `canonical_record` WARNING was printed by the extractor** — the
   extraction run's console output was 16 `wrote …` lines and nothing else.

9. **All 16 lessons' routes match BATCH-PLAN's routes column exactly** —
   including the two Triple-Higher-only lessons (`resolving-forces`,
   `free-body-diagrams`, both `TH` alone) — no discrepancy anywhere.

10. **Two authored batch-2/batch-3 lessons already link forward to this
    batch's slugs.** `ks4_lessons/authored/batch-2/changes-in-energy.
    dc.html` links to both `forces-elasticity` and `work-done-energy-
    transfer`; `ks4_lessons/authored/batch-3/power.dc.html` and `ks4_
    lessons/authored/batch-3/particle-motion-pressure.dc.html` both also
    link to `work-done-energy-transfer`. These are navigation `hrefFor`/
    `endConnects` links, not diagrams, and confirm these lessons are
    expected destinations from already-built pages.

11. **This batch spans two AQA topics** (atomic structure/radioactivity
    §6.4, forces §6.5). Radioactivity has NO KS3 unit at all (AQA's
    radioactive-decay content starts at KS4), so the diagram-library audit
    for lessons #1–#8 draws entirely on `figlib/physics.py`'s existing
    atomic/nuclear figures (`atom_diagram`, `isotope_notation`,
    `radiation_penetration`, `half_life_curve`) and `figlib/ks4phys.py`'s
    `nuclide()` — all four of the first eight lessons have at least a
    partial direct match. The forces lessons (#9–#16) are the
    best-covered of any batch seen so far: `figlib/physics.py`'s
    `resultant_force`, `free_body_diagram`, `hookes_law_graph`,
    `resolution_triangle`, `force_beam`, `crate_forces` and `force_grid`,
    plus `figlib/ks4phys.py`'s `force_grid_2d` and `free_body` (both
    explicitly docstring-cited to AQA 8463 §4.5.1.4, the resolving-forces/
    free-body-diagrams spec point), between them cover every forces lesson
    in this batch directly or partially. See `05-diagram-library/README.md`.
