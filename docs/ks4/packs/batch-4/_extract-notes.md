> **Raw extraction notes, written before the examination.** Where they disagree with `examination/`, `FLAGS.md` or `00-BRIEF.md` (spec references, required-practical numbers, quiz-key alignment), those win.

# Batch 4 — extraction notes

Facts only, read straight from the 13 extracted files in
`04-checked-science-source/` (each file's header gives the routes; `##`
section presence gives everything else). No route-copy `quiz` section exists
in ANY of the 13 files — every route a lesson appears on serves the identical
TH quiz list, so "quiz count per route" below is one number covering every
route listed. The only field that ever differs by route across this whole
batch is `higher`, and only on Combined Foundation and Triple Foundation —
Combined Higher never differs from Triple Higher in any of the 13 files.

| # | Lesson | Routes | Quiz count (same on every route) | examiner_tip | fifas | equations | rp (verbatim) | variables |
|---|---|---|---|---|---|---|---|---|
| 1 | heart-blood-vessels | CF CH TF TH | 4 | no | 0 | none | none | none |
| 2 | water-cycle | CF CH TF TH | 2 | no | 0 | none | none | none |
| 3 | atmospheric-pollutants | CF CH TF TH | 2 | no | 0 | 4 — `S + O₂ → SO₂  (sulfur impurity burning)`; `N₂ + O₂ → 2NO  (in engines at high temperature)`; `2CO + 2NO → 2CO₂ + N₂  (catalytic converter reaction)`; `CaCO₃ + H₂SO₄ → CaSO₄ + H₂O + CO₂  (acid rain dissolving limestone)` | none | none |
| 4 | efficiency | CF CH TF TH | 2 | no | 1 | 3 — `efficiency = useful output energy ÷ total input energy`; `efficiency = useful power output ÷ total power input`; `efficiency (%) = (useful output ÷ total input) × 100` | none | none |
| 5 | infrared-black-bodies | TF TH | 2 | no | 0 | none | none | none |
| 6 | transport-in-cells | CF CH TF TH | 5 | no | 1 | none | "RP2 — Investigate osmosis: place potato cylinders in different concentrations of sucrose solution. Measure mass before and after. Calculate % change in mass." | none |
| 7 | blood | CF CH TF TH | 4 | no | 0 | none | none | none |
| 8 | periodic-table | CF CH TF TH | 2 | no | 0 | none | none | none |
| 9 | thermal-conductivity | TF TH | 2 | no | 0 | none | "RP2 (physics only) — Investigate effectiveness of different thermal insulators. Measure rate of cooling of hot water wrapped in different materials." | none |
| 10 | coronary-heart-disease | CF CH TF TH | 3 | no | 0 | none | none | none |
| 11 | biodiversity | CF CH TF TH | 2 | no | 0 | none | none | none |
| 12 | development-periodic-table | CF CH TF TH | 2 | no | 0 | none | none | none |
| 13 | uses-em-waves | CF CH TF TH | 2 | no | 0 | none | none | none |

## Anything odd

1. **No `examiner_tip` anywhere in this batch.** All 13 files omit the
   `## examiner_tip` section entirely — the field is simply falsy on every
   one of these subtopics' TH records, on every route. Not a bug (the
   generator only prints a section when the field is truthy), but worth
   flagging since the batch has zero of them, versus batches that have some.

2. **Two specs in BATCH-PLAN.md are guesses, and the real data disagrees.**
   `docs/ks4/BATCH-PLAN.md`'s own table marks these with a `?`:
   - #5 infrared-black-bodies: plan guesses `— · 8463 4.6.3.1–4.6.3.2?`; the
     actual `all_subtopics_*` record's spec is `6.6.5 (physics only)`.
   - #9 thermal-conductivity: plan guesses `6.1.2.1? · 8463 4.1.2.1`; the
     actual spec is `6.1.3 (physics only)`.
   The extractor took the spec straight off the data (the plan's guess was
   never consulted), so the extracted files are correct; the plan's own spec
   column for these two rows is stale/wrong and should not be trusted if
   anyone cites it directly.

3. **`quiz` never varies by route in this batch — only `higher` does, and
   only on CF/TF.** Checked across all 13 files: no `## quiz — <route> copy`
   section exists anywhere, so every quiz question, option and
   wrong-answer explanation served to a student is byte-identical no matter
   which of their routes they are on, for all 13 lessons. Where
   `## higher — <route> copy` sections do appear (10 of the 13 lessons —
   every one with a truthy `higher` field except water-cycle, blood and
   development-periodic-table, which have no `higher` field at all), it is
   always Combined Foundation and/or Triple Foundation that differ from
   Triple Higher; Combined Higher is never listed as differing in this
   batch.

4. **Filenames with a space and parentheses.** The two physics-only subtopics
   carry `(physics only)` inside the spec string itself, which the
   extractor's filename rule reproduces literally:
   `physics-8463-4.6.3-infrared-black-bodies.md` and
   `physics-6.1.2.1-thermal-conductivity.md`. Same pattern as
   the existing batch-2 file `physics-6.6.3 (physics only)-lenses.md`, so
   not new to this batch, but both filenames need quoting in any shell
   command that touches them (as done throughout this pack's build).

5. **Theory headings are on-topic for every lesson** — checked all 13
   files' `theory` JSON arrays' `heading` fields; none reads as off-topic
   for its lesson title (e.g. transport-in-cells: Diffusion / Osmosis /
   Active Transport / Exchange Surfaces; coronary-heart-disease: What is
   CHD? / How CHD Develops / Risk Factors / Treatments). No stray or
   mismatched content found.

6. **No `canonical_record` WARNING was printed by the extractor** for any of
   the 13 slugs, confirming every one has a genuine Triple Higher record
   (the script falls back and warns to stderr only when TH is missing; the
   extraction run's console output was 13 `wrote …` lines and nothing else).

7. **Pilot-format fields never present in this batch at all:** `matching`
   appears in all 13 (replaced per the pack's own instructions, not listed
   above since it is not one of the requested columns), but `common_mistake`
   and `key_note` are present and truthy on every one of the 13 — i.e. this
   batch is unusually complete on those two fields compared with the sparser
   `rp`/`fifas`/`equations`/`examiner_tip` columns.
