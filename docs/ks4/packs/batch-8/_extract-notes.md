# Batch 8 — extraction notes

Facts only, read straight from the 16 extracted files in
`04-checked-science-source/` (each file's header gives the routes; `##`
section presence gives everything else). No route-copy `quiz` section exists
in ANY of the 16 files — every route a lesson appears on serves the identical
TH quiz list, so "quiz count per route" below is one number covering every
route listed. The only field that ever differs by route is `higher`.

| # | Lesson | Routes | Quiz count (same on every route) | examiner_tip | fifas | equations | rp (verbatim) | variables |
|---|---|---|---|---|---|---|---|---|
| 1 | homeostasis | CF CH TF TH | 3 | no | 0 | none | none | none |
| 2 | nervous-system | CF CH TF TH | 3 | no | 0 | none | none | none |
| 3 | reflex-actions | CF CH TF TH | 3 | no | 0 | none | none | none |
| 4 | reaction-time | CF CH TF TH | 2 | no | **1** | 2 — `d = ½ × g × t²`; `t = √(2d ÷ g)` | none (see "Anything odd" #1) | 3 — `d` distance ruler falls (m); `t` reaction time (s); `g` gravitational field strength (m/s²) |
| 5 | the-brain | TF TH | 2 | no | 0 | none | none | none |
| 6 | the-eye | TF TH | 2 | no | 0 | none | none | none |
| 7 | defects-of-the-eye | TF TH | 2 | no | 0 | none | none | none |
| 8 | thermoregulation | TF TH | 3 | no | 0 | none | none | none |
| 9 | endocrine-system | CF CH TF TH | 3 | no | 0 | none | none | none |
| 10 | blood-glucose-diabetes | CF CH TF TH | 3 | no | **1** | none | none | none |
| 11 | human-reproduction-hormones | CF CH TF TH | 3 | no | 0 | none | none | none |
| 12 | contraception-fertility | CF CH TF TH | 3 | no | 0 | none | none | none |
| 13 | sexual-asexual-reproduction | CF CH TF TH | 3 | no | 0 | none | none | none |
| 14 | meiosis | TF TH | 2 | no | 0 | none | none | none |
| 15 | advantages-sexual-asexual | TF TH | 2 | no | 0 | none | none | none |
| 16 | dna-genome | CF CH TF TH | 3 | no | 0 | none | none | none |

Exactly two `fifas` lessons, matching BATCH-PLAN's FIFA column exactly
(#4 reaction-time, #10 blood-glucose-diabetes). The CFIFA form (step C) was
appended to both files, four FIFA steps kept byte-identical, Convert step
added: reaction-time's genuinely converts units (20 cm → 0.20 m, since the
conversion is a real part of its "I" step, unlike batch-6's
culturing-microorganisms diameter-already-in-mm case); blood-glucose-diabetes
has no numbers or units at all (a descriptive negative-feedback answer), so
its Convert step states nothing needs converting.

## wrong_explanations key check

All 42 quiz items across the 16 files were checked: every item's
`wrong_explanations` uses exactly the keys matching its wrong options (4
options → keys `1,2,3`; the credited answer, always option 0, carries no
key). **No shifted-key defect found anywhere in this batch.** Manually
verified on blood-glucose-diabetes q1 (insulin-tablet item): key `1`
explains option 1 ("tablets haven't been invented"), key `2` explains option
2 (stomach-acid speed), key `3` explains option 3 (pancreas-location
confusion) — all correctly aligned to their own index. `correct_index` is 0
for all 42 items, matching the estate-wide index-0-by-design pattern.

## Anything odd

1. **reaction-time's required practical has no `rp` field at all** — unlike
   every other RP-bearing lesson seen so far (batch-6's animal-plant-cells,
   digestive-system, culturing-microorganisms; batch-7's
   photosynthesis/rate-of-photosynthesis), the ruler-drop method is written
   out in full inside the SECOND `theory` block ("Measuring Reaction Time —
   The Ruler Drop Test"), not in a dedicated `rp` field, even though
   BATCH-PLAN's family column calls this "REQUIRED PRACTICAL — ruler-drop RP
   and its data" and the lesson plainly is one. BATCH-PLAN's own RP column is
   correctly left blank for this row, so the data and the plan agree — the
   oddity is only that the content is real-RP content living in `theory`
   rather than `rp`.

2. **No `examiner_tip` anywhere in this batch** — same pattern as every prior
   batch (4–7). All 16 files omit the `## examiner_tip` section entirely.

3. **Heavy spec-number disagreement with BATCH-PLAN.md, same failure mode as
   batch 7.** 11 of the 16 rows differ from the plan's guess:
   - #2 nervous-system, #3 reflex-actions, #4 reaction-time: plan `4.5.2.1`
     (all three identical in the plan) → actual `4.5.2` for all three.
   - #5 the-brain: plan `— · 8461 4.5.2.2` → actual `4.5.2.4`.
   - #6 the-eye: plan `— · 8461 4.5.2.3` → actual `4.5.2.5`.
   - #7 defects-of-the-eye: plan `— · 8461 4.5.2.3` (same guess as #6) →
     actual `4.5.2.6`.
   - #8 thermoregulation: plan `— · 8461 4.5.2.4` → actual `4.5.1` — the
     biggest jump in the batch, and actual collides with #1 homeostasis's
     spec (see #4 below).
   - #9 endocrine-system: plan `4.5.3.1` → actual `4.5.3`.
   - #10 blood-glucose-diabetes: plan `4.5.3.2` → actual `4.5.3` (same
     actual as #9, a different lesson).
   - #11 human-reproduction-hormones: plan `4.5.3.3` → actual `4.5.4`.
   - #12 contraception-fertility: plan `4.5.3.4–4.5.3.5` → actual `4.5.4`
     (same actual as #11).
   - #13 sexual-asexual-reproduction: plan `4.6.1.1` → actual `4.6.1`.
   - #16 dna-genome: plan `4.6.1.3` → actual `4.6.2`.
   Only #1 homeostasis, #14 meiosis and #15 advantages-sexual-asexual match
   the plan exactly. As with batch 7, the extractor's spec comes straight off
   the data; BATCH-PLAN's spec column should not be cited directly for any of
   these 11 rows.

4. **Two pairs of actual specs collide across different lessons** (beyond
   what BATCH-PLAN itself guessed): #1 homeostasis and #8 thermoregulation
   both carry `4.5.1`; #9 endocrine-system and #10 blood-glucose-diabetes
   both carry `4.5.3`; #11 human-reproduction-hormones and #12
   contraception-fertility both carry `4.5.4`. These read as the data's
   subtopic numbering being coarser than one-spec-per-lesson in this stretch
   (several lessons sharing one AQA sub-clause number), not as an
   extraction error — same shape as batch-6's #7/#9 spec note, just more
   pairs of it.

5. **BATCH-PLAN's own table has a spec collision between two different
   rows**, independent of the extracted data: #15 advantages-sexual-asexual
   is guessed `— · 8461 4.6.1.3` and #16 dna-genome is guessed `4.6.1.3` —
   identical guessed spec strings for two different lessons. The actual
   extracted specs resolve cleanly apart (`4.6.1.3` vs `4.6.2`), so this
   caused no real ambiguity in extraction, but the plan table itself should
   not be read as internally disambiguating these two rows by spec number.

6. **Three Triple-only pairs, all TF+TH.** #5 the-brain, #6 the-eye, #7
   defects-of-the-eye, #8 thermoregulation, #14 meiosis, #15
   advantages-sexual-asexual all appear on Triple Foundation + Triple Higher
   only — six of sixteen, matching BATCH-PLAN's routes column exactly for
   all six.

7. **`higher` differs on 10 of the 16 lessons** — always Combined Foundation
   and/or Triple Foundation, never Combined Higher, same pattern as every
   prior batch: homeostasis, nervous-system, blood-glucose-diabetes,
   endocrine-system, contraception-fertility, human-reproduction-hormones,
   sexual-asexual-reproduction, dna-genome all have both a Combined
   Foundation and Triple Foundation `higher` copy; thermoregulation and
   meiosis (both TF TH only) have a Triple-Foundation-only `higher` copy.
   reaction-time, reflex-actions, the-brain, the-eye, defects-of-the-eye and
   advantages-sexual-asexual have no `higher` section at all.

8. **No filename needed renaming.** All 16 extracted filenames are already
   clean — step B of the task was not needed for this batch.

9. **No subject:slug collisions.** All 16 slugs are Biology-only and
   extracted cleanly as bare slugs.

10. **No `canonical_record` WARNING was printed by the extractor** — the
    extraction run's console output was 16 `wrote …` lines and nothing else.
