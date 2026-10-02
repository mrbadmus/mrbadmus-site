> **Raw extraction notes, written before the examination.** Where they disagree with `examination/`, `FLAGS.md` or `00-BRIEF.md` (spec references, required-practical numbers, quiz-key alignment), those win.

# Batch 6 — extraction notes

Facts only, read straight from the 14 extracted files in
`04-checked-science-source/` (each file's header gives the routes; `##`
section presence gives everything else). No route-copy `quiz` section exists
in ANY of the 14 files — every route a lesson appears on serves the identical
TH quiz list, so "quiz count per route" below is one number covering every
route listed. The only field that ever differs by route across this whole
batch is `higher`, and only on Combined Foundation and/or Triple Foundation —
Combined Higher never differs from Triple Higher in any of the 14 files.

| # | Lesson | Routes | Quiz count (same on every route) | examiner_tip | fifas | equations | rp (verbatim) | variables |
|---|---|---|---|---|---|---|---|---|
| 1 | factors-affecting-food-security | TF TH | 2 | no | 0 | none | none | none |
| 2 | group-1 | CF CH TF TH | 2 | no | 0 | 4 — `2M + 2H₂O → 2MOH + H₂`; `2Li + 2H₂O → 2LiOH + H₂`; `2Na + 2H₂O → 2NaOH + H₂`; `2K + 2H₂O → 2KOH + H₂` | none | none |
| 3 | reactions-of-acids | CF CH TF TH | 2 | no | 0 | 6 — `Acid + metal → salt + hydrogen`; `Acid + metal oxide → salt + water`; `Acid + metal hydroxide → salt + water`; `Acid + metal carbonate → salt + water + carbon dioxide`; `Mg + 2HCl → MgCl₂ + H₂`; `CaCO₃ + 2HCl → CaCl₂ + H₂O + CO₂` | none | none |
| 4 | stellar-evolution | TF TH | 2 | no | 0 | none | none | none |
| 5 | animal-plant-cells | CF CH TF TH | 5 | no | 0 | none | "RP1 — Use a light microscope to observe, draw and label plant and animal cells. Include a scale bar and calculate magnification." | none |
| 6 | cell-specialisation | CF CH TF TH | 4 | no | 0 | none | none | none |
| 7 | culturing-microorganisms | TF TH | 3 | no | **1** | 1 — `Area of inhibition zone = π × r²` | "RP6 — Required practical: investigate the effect of antiseptics or antibiotics on bacterial growth using agar plates and measuring inhibition zones." | none |
| 8 | stem-cells | CF CH TF TH | 4 | no | 0 | none | none | none |
| 9 | principles-of-organisation | CF CH TF TH | 4 | no | 0 | none | none | none |
| 10 | digestive-system | CF CH TF TH | 5 | no | 0 | none | "RP4 — Food tests: iodine solution tests for starch (blue-black = positive), Benedict's solution tests for glucose (brick red = positive), Biuret reagent tests for protein (purple = positive), ethanol emulsion test for fat (cloudy white = positive)." | none |
| 11 | health-disease | CF CH TF TH | 3 | no | 0 | none | none | none |
| 12 | cancer | CF CH TF TH | 3 | no | 0 | none | none | none |
| 13 | transpiration | CF CH TF TH | 3 | no | 0 | none | none | none |
| 14 | translocation | CF CH TF TH | 3 | no | 0 | none | none | none |

## Anything odd

1. **No `examiner_tip` anywhere in this batch** — same pattern as batches 4
   and 5. All 14 files omit the `## examiner_tip` section entirely.

2. **Exactly one `fifas` lesson, and it matches BATCH-PLAN.md exactly.**
   #7 culturing-microorganisms is the only one of the 14 BATCH-PLAN rows
   marked FIFA=1, and it is the only file with a `## fifas` section (one
   worked example, "Inhibition Zone Area": diameter 18 mm → radius 9 mm →
   area = π × 9² ≈ 254 mm²). The CFIFA form (step B) was appended to this
   file only, with the four FIFA steps kept byte-identical and a Convert
   step added ("Nothing to convert — the diameter is given in millimetres
   (mm) ... no unit conversion is needed") since the radius-from-diameter
   arithmetic is already inside the verbatim "I" step, not a unit
   conversion.

3. **One spec disagrees with BATCH-PLAN.md's own table, same failure mode as
   batch 4 #2 and batch 5 #3.** #7 culturing-microorganisms: plan guesses
   `— · 8461 4.1.1.6`; the actual extracted record's spec is `4.1.2`. The
   extractor took the spec straight off the data; the plan's spec column for
   this row should not be cited directly.

4. **`quiz` never varies by route in this batch — only `higher` does.**
   Checked across all 14 files: no `## quiz — <route> copy` section exists
   anywhere. Where `## higher — <route> copy` sections appear (9 of the 14
   lessons: stem-cells, digestive-system, health-disease, cancer,
   transpiration, translocation, group-1, reactions-of-acids — all Combined
   Foundation AND Triple Foundation; factors-affecting-food-security and
   stellar-evolution each have only a Triple Foundation copy, since neither
   has a Combined route), it is always a Foundation route that differs from
   Triple Higher. Combined Higher is never listed as differing in this
   batch (checked: zero `## higher — Combined Higher` headers in any of the
   14 files — true across batches 4, 5 and 6 combined, 42 files).

5. **Two Triple-only lessons.** #1 factors-affecting-food-security and #4
   stellar-evolution and #7 culturing-microorganisms all appear on Triple
   Foundation/Triple Higher only — three of the fourteen, matching
   BATCH-PLAN's `TF TH` routes column exactly for all three.

6. **Filename with a space and parentheses**, same pattern as batches 2 and
   4: `physics-8463-4.8.1.2-stellar-evolution.md` carries
   `(physics only)` inside the spec string itself, needing quoting in any
   shell command (as done throughout this pack's build). No other Batch-6
   filename needed it.

7. **Theory headings are on-topic for every lesson** — checked all 14
   files' `theory` JSON arrays' `heading` fields; none reads as off-topic
   for its lesson title (e.g. digestive-system: Mouth / Stomach / Small
   Intestine / Large Intestine, Rectum and Anus in digestive order;
   cell-specialisation: Differentiation / Specialised Animal Cells /
   Specialised Plant Cells). No stray or mismatched content found.

8. **No `canonical_record` WARNING was printed by the extractor** for any of
   the 14 slugs — the extraction run's console output was 14 `wrote …`
   lines and nothing else.

9. **`common_mistake` and `key_note` are present and truthy on every one of
   the 14 files** — same completeness pattern as batches 4 and 5, versus the
   sparser `rp`/`fifas`/`equations`/`examiner_tip` columns (3 of 14 have
   equations, 3 have rp, 1 has fifas, 0 have examiner_tip or variables).

10. **No subject:slug collisions needed resolving.** All 14 slugs (and all 15
    in batch 5) extracted cleanly as bare slugs — none of the batch-5/6 list
    hit the chem/phys `atomic-structure` topic-id collision the task brief
    warned about by name (`structure-of-atom` is a Physics-only slug in the
    underlying data; there is no chemistry subtopic sharing that exact
    slug), so `--out`-only invocations with no `subject:slug` prefix were
    sufficient for both batches.
