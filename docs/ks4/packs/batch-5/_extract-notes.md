> **Raw extraction notes, written before the examination.** Where they disagree with `examination/`, `FLAGS.md` or `00-BRIEF.md` (spec references, required-practical numbers, quiz-key alignment), those win.

# Batch 5 — extraction notes

Facts only, read straight from the 15 extracted files in
`04-checked-science-source/` (each file's header gives the routes; `##`
section presence gives everything else). No route-copy `quiz` section exists
in ANY of the 15 files — every route a lesson appears on serves the identical
TH quiz list, so "quiz count per route" below is one number covering every
route listed. The only field that ever differs by route across this whole
batch is `higher`, and only on Combined Foundation and/or Triple Foundation —
Combined Higher never differs from Triple Higher in any of the 15 files.

| # | Lesson | Routes | Quiz count (same on every route) | examiner_tip | fifas | equations | rp (verbatim) | variables |
|---|---|---|---|---|---|---|---|---|
| 1 | land-use | CF CH TF TH | 2 | no | 0 | none | none | none |
| 2 | metals-non-metals | CF CH TF TH | 2 | no | 0 | none | none | none |
| 3 | reactivity-series | CF CH TF TH | 2 | no | 0 | 4 — `Fe + CuSO₄ → FeSO₄ + Cu  (displacement)`; `Metal + oxygen → metal oxide`; `Metal + water → metal hydroxide + hydrogen`; `Metal + acid → salt + hydrogen` | none | none |
| 4 | energy-resources | CF CH TF TH | 2 | no | 0 | none | none | none |
| 5 | structure-of-atom | CF CH TF TH | 2 | no | 0 | none | none | none |
| 6 | plant-tissues | CF CH TF TH | 3 | no | 0 | none | none | none |
| 7 | waste-management | CF CH TF TH | 2 | no | 0 | none | none | none |
| 8 | earths-resources | CF CH TF TH | 2 | no | 0 | none | none | none |
| 9 | development-atomic-model | CF CH TF TH | 2 | no | 0 | none | none | none |
| 10 | global-warming | CF CH TF TH | 2 | no | 0 | none | none | none |
| 11 | group-0 | CF CH TF TH | 2 | no | 0 | none | none | none |
| 12 | extraction-of-metals | CF CH TF TH | 2 | no | 0 | 3 — `Fe₂O₃ + 3CO → 2Fe + 3CO₂  (iron extraction)`; `ZnO + C → Zn + CO₂`; `2Al₂O₃ → 4Al + 3O₂  (electrolysis of aluminium oxide)` | none | none |
| 13 | potable-water | CF CH TF TH | 2 | no | 0 | none | "RP8 (Chemistry) — Analysis and purification of water samples from different sources, including testing for pH, dissolved ions (using flame tests or precipitation) and filtering/distillation." | none |
| 14 | radioactive-decay | CF CH TF TH | 2 | no | 0 | none | none | none |
| 15 | red-shift-big-bang | TF TH | 2 | no | 0 | 1 — `v = H₀ × d  (Hubble's Law)` | none | 3 — `v` (Recession speed, km/s); `H₀` (Hubble constant, km/s/Mpc); `d` (Distance to galaxy, Mpc) |

## Anything odd

1. **No `examiner_tip` anywhere in this batch** — same pattern as batch 4. All
   15 files omit the `## examiner_tip` section entirely; the field is falsy
   on every one of these subtopics' TH records, on every route.

2. **No `fifas` anywhere in this batch.** BATCH-PLAN.md's own FIFA column is
   blank for all 15 rows in Batch 5, and the extracted data agrees — zero of
   the 15 files carry a `## fifas` section. There is therefore nothing to
   append a CFIFA form to in this batch (step B of the build produced no
   output, by design, not by omission).

3. **Two specs disagree with BATCH-PLAN.md's own table, the same failure mode
   as batch 4's #2:**
   - #6 plant-tissues: plan says `4.2.3.1`; the extracted record's actual
     spec is `4.2.5`. (Note this is a DIFFERENT subtopic slot from the
     `4.2.5.2`/`4.2.5.3` transpiration/translocation lessons in Batch 6 —
     all three sit under the same `4.2.5` "Plant tissues, organs and
     systems" top-level spec point but are separate `all_subtopics_*`
     records.)
   - #15 red-shift-big-bang: plan guesses `— · 8463 4.8.2`; the actual spec
     on the extracted record is `6.8.3–6.8.4 (physics only)`.
   The extractor took the spec straight off the data in both cases; the
   plan's own spec column for these two rows should not be cited directly.

4. **`quiz` never varies by route in this batch — only `higher` does.**
   Checked across all 15 files: no `## quiz — <route> copy` section exists
   anywhere. Where `## higher — <route> copy` sections do appear (5 of the
   15 lessons: plant-tissues, earths-resources, potable-water,
   reactivity-series, extraction-of-metals — all Combined Foundation AND
   Triple Foundation; red-shift-big-bang has only a Triple Foundation copy,
   since it has no Combined route at all), it is always a Foundation route
   that differs from Triple Higher. Combined Higher is never listed as
   differing in this batch (checked: zero `## higher — Combined Higher`
   headers in any of the 15 files).

5. **One Triple-only lesson.** #15 red-shift-big-bang appears on Triple
   Foundation and Triple Higher only — no Combined route — matching
   BATCH-PLAN's `TF TH` routes column exactly.

6. **Filename with a space and parentheses**, same pattern as batch 2/4: none
   in this batch — all 15 Batch-5 filenames are plain (`red-shift-big-bang`'s
   spec string has an en-dash but no parenthetical, so the filename itself
   needed no quoting beyond the usual spaces-in-path handling). Flagged as
   checked, not as a new instance.

7. **Theory headings are on-topic for every lesson** — checked all 15 files'
   `theory` JSON arrays' `heading` fields; none reads as off-topic for its
   lesson title (e.g. structure-of-atom: Inside the Atom / Properties of
   Subatomic Particles / Electron Shells and Energy Levels;
   development-atomic-model: Solid Sphere / Plum Pudding / Nuclear Model —
   a clean historical progression). No stray or mismatched content found.

8. **No `canonical_record` WARNING was printed by the extractor** for any of
   the 15 slugs — the extraction run's console output was 15 `wrote …`
   lines and nothing else, confirming a genuine Triple Higher record exists
   for every one.

9. **`common_mistake` and `key_note` are present and truthy on every one of
   the 15 files** — same completeness pattern as batch 4, versus the
   sparser `rp`/`fifas`/`equations`/`examiner_tip`/`variables` columns (only
   3 of 15 have equations, 1 has rp, 1 has variables, 0 have fifas or
   examiner_tip).

10. **`variables` appears for the first time across batches 4–5** — only on
    #15 red-shift-big-bang (`v`, `H₀`, `d`), paired with its one equation
    (Hubble's Law). No other file in this batch or in batch 4 carries a
    `## variables` section.
