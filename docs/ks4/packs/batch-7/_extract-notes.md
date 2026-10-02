> **Raw extraction notes, written before the examination.** Where they disagree with `examination/`, `FLAGS.md` or `00-BRIEF.md` (spec references, required-practical numbers, quiz-key alignment), those win.

# Batch 7 — extraction notes

Facts only, read straight from the 16 extracted files in
`04-checked-science-source/` (each file's header gives the routes; `##`
section presence gives everything else). No route-copy `quiz` section exists
in ANY of the 16 files — every route a lesson appears on serves the identical
TH quiz list, so "quiz count per route" below is one number covering every
route listed. The only field that ever differs by route is `higher`.

| # | Lesson | Routes | Quiz count (same on every route) | examiner_tip | fifas | equations | rp (verbatim) | variables |
|---|---|---|---|---|---|---|---|---|
| 1 | communicable-diseases-defence | CF CH TF TH | 4 | no | 0 | none | none | none |
| 2 | viral-diseases | CF CH TF TH | 3 | no | 0 | none | none | none |
| 3 | bacterial-diseases | CF CH TF TH | 2 | no | 0 | none | none | none |
| 4 | fungal-protist-diseases | CF CH TF TH | 2 | no | 0 | none | none | none |
| 5 | vaccination | CF CH TF TH | 3 | no | 0 | none | none | none |
| 6 | antibiotics-painkillers | CF CH TF TH | 2 | no | 0 | none | none | none |
| 7 | drug-discovery-development | CF CH TF TH | 3 | no | 0 | none | none | none |
| 8 | monoclonal-antibodies | TH | 3 | no | 0 | none | none | none |
| 9 | plant-disease-detection-defence | TF TH | 3 | no | 0 | none | none | none |
| 10 | photosynthesis | CF CH TF TH | 4 | no | 0 | 1 — `6CO₂ + 6H₂O → C₆H₁₂O₆ + 6O₂ (light energy)` | "RP5 — Investigate the effect of light intensity on the rate of photosynthesis using aquatic plants (e.g. Elodea or Cabomba). Count oxygen bubbles per minute at different distances from a lamp." | none |
| 11 | rate-of-photosynthesis | CF CH TF TH | 3 | no | 0 | none | "RP5 — Investigate the effect of light intensity on rate of photosynthesis using aquatic plants. Count bubbles per minute. Move lamp to change light intensity. Control CO₂ (add sodium bicarbonate) and temperature." | none |
| 12 | uses-of-glucose | CF CH TF TH | 3 | no | 0 | none | none | none |
| 13 | aerobic-respiration | CF CH TF TH | 3 | no | 0 | 2 — `glucose + oxygen → carbon dioxide + water`; `C₆H₁₂O₆ + 6O₂ → 6CO₂ + 6H₂O` | none | none |
| 14 | anaerobic-respiration | CF CH TF TH | 4 | no | 0 | 2 — `Anaerobic (animals): glucose → lactic acid`; `Anaerobic (yeast): glucose → ethanol + carbon dioxide` | none | none |
| 15 | response-to-exercise | CF CH TF TH | 3 | no | 0 | none | none | none |
| 16 | metabolism | CF CH TF TH | 3 | no | 0 | none | none | none |

## wrong_explanations key check

All 44 quiz items across the 16 files were checked: every item's
`wrong_explanations` uses exactly the keys matching its wrong options
(4-option items → keys `1,2,3`; the credited answer, always option 0, carries
no key). **No shifted-key defect found anywhere in this batch** — every
explanation reads as the reason that specific numbered option is wrong, not
as a restatement of the credited answer one index late. (An automated
word-overlap heuristic initially over-flagged ~30 items as "possible shifts";
manual reading of a sample — e.g. communicable-diseases-defence q0, the
phagocyte/lymphocyte item — showed the overlap was shared domain vocabulary
between the credited answer and its own correction text, not a real shift.
`correct_index` is 0 for all 44 items, confirming the estate-wide "KS4 is
100% index-0 by design" pattern.)

## Anything odd

1. **No `examiner_tip` anywhere in this batch** — same pattern as batches
   4–6. All 16 files omit the `## examiner_tip` section entirely.

2. **No `fifas` anywhere in this batch** — matches BATCH-PLAN's own FIFA
   column, which is blank for all 16 rows. No CFIFA-form appending was
   needed (step C of the task) for any Batch-7 file.

3. **Extensive spec-number disagreement with BATCH-PLAN.md, worse than any
   prior batch.** 9 of the 16 rows differ from the plan's guessed spec, and
   unlike batches 4–6 (where only TF/TH-only rows disagreed), several
   CF/CH/TF/TH rows disagree too:
   - #1 communicable-diseases-defence: plan `4.3.1.1` → actual `4.3.1`
   - #5 vaccination: plan `4.3.1.7` → actual `4.3.2`
   - #6 antibiotics-painkillers: plan `4.3.1.8` → actual `4.3.3`
   - #7 drug-discovery-development: plan `4.3.1.9` → actual `4.3.4`
   - #8 monoclonal-antibodies: plan `— · 8461 4.3.2.1–4.3.2.2` → actual `4.3.5`
   - #9 plant-disease-detection-defence: plan `— · 8461 4.3.3.1–4.3.3.2` → actual `4.3.5` (same actual spec number as #8, a different lesson)
   - #14 anaerobic-respiration: plan `4.4.2.1` (same as #13) → actual `4.4.2.2`
   - #15 response-to-exercise: plan `4.4.2.2` → actual `4.4.2.3`
   - #16 metabolism: plan `4.4.2.3` → actual `4.4.2.4`
   The extractor takes the spec straight off the data; BATCH-PLAN's spec
   column for these 9 rows should not be cited directly. The pattern (every
   row from #5 onward one or more steps off, as if the data's own numbering
   runs one subtopic ahead of the plan's guess from `4.3.1.7` onward) suggests
   the underlying `all_subtopics_biology.py` groups/numbers this stretch of
   4.3/4.4 differently from the plan's working assumption, not 9 independent
   typos.

4. **RP5 is shared verbatim-but-not-identical across two lessons.**
   #10 photosynthesis and #11 rate-of-photosynthesis both carry an `rp`
   field for the same required practical (light intensity vs rate of
   photosynthesis using aquatic plants), but the wording differs between the
   two files — #10's is shorter (bubbles per minute, distance from lamp);
   #11's adds the CO₂/temperature control detail. Matches BATCH-PLAN's RP
   column marking `Y` on both rows.

5. **Two Triple-only lessons, one Triple-plus-TH-only.** #8
   monoclonal-antibodies is Triple Higher only; #9
   plant-disease-detection-defence is Triple Foundation + Triple Higher —
   both matching BATCH-PLAN's routes column exactly.

6. **`higher` differs on 9 of the 16 lessons, always on Combined Foundation
   and/or Triple Foundation, never on Combined Higher** — same pattern as
   batches 4–6: communicable-diseases-defence, vaccination,
   antibiotics-painkillers, drug-discovery-development,
   rate-of-photosynthesis, aerobic-respiration, metabolism all have both a
   Combined Foundation and a Triple Foundation `higher` copy; the two
   TH-only/Triple-only lessons (monoclonal-antibodies,
   plant-disease-detection-defence) and the three fully-shared quiz-only
   lessons (viral-diseases, bacterial-diseases, fungal-protist-diseases,
   uses-of-glucose, anaerobic-respiration, response-to-exercise) have no
   `higher` section at all.

7. **No filename needed renaming.** All 16 extracted filenames are already
   clean (`<subject>-<spec>-<slug>.md`, no spaces or parentheses) — step B
   of the task was not needed for this batch, unlike batch-6's
   `stellar-evolution` filename.

8. **No subject:slug collisions.** All 16 slugs are Biology-only in this
   batch and extracted cleanly as bare slugs with no `--out`-prefix needed.

9. **No `canonical_record` WARNING was printed by the extractor** for any of
   the 16 slugs — the extraction run's console output was 16 `wrote …`
   lines and nothing else.

10. **Theory headings are on-topic for every lesson** — spot-checked across
    the 16 files' `theory` JSON arrays; no stray or off-topic heading found
    (e.g. reaction-time-adjacent content did not leak into aerobic/anaerobic
    respiration, and the FIFA-bearing photosynthesis/aerobic/anaerobic specs
    all keep their equations inside the `equations` field, not folded into
    `theory`).
