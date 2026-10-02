# Batch 13 — extraction notes

Facts only, read straight from the 12 extracted files in
`04-checked-science-source/` (each file's header gives the routes; `##`
section presence gives everything else). No route-copy `quiz` section exists
in ANY of the 12 files — every route a lesson appears on serves the identical
TH quiz list, so "quiz count per route" below is one number covering every
route listed. The only field that ever differs by route is `higher`.

| # | Lesson | Routes | Quiz count (same on every route) | examiner_tip | fifas | equations | rp (verbatim) | variables |
|---|---|---|---|---|---|---|---|---|
| 1 | crude-oil-hydrocarbons | CF CH TF TH | 2 | no | 0 | 3 — CₙH₂ₙ₊₂; CH₄+2O₂→CO₂+2H₂O; C₃H₈+5O₂→3CO₂+4H₂O | none | none |
| 2 | fractional-distillation | CF CH TF TH | 2 | no | 0 | none | none | none |
| 3 | properties-of-hydrocarbons | CF CH TF TH | 2 | no | 0 | 2 — hydrocarbon+O₂→CO₂+H₂O; 2C₈H₁₈+25O₂→16CO₂+18H₂O | none | none |
| 4 | cracking-alkenes | CF CH TF TH | 2 | no | 0 | 4 — C₁₀H₂₂→C₈H₁₈+C₂H₄; CₙH₂ₙ; C₂H₄+H₂O→C₂H₅OH; nCH₂=CH₂→[−CH₂−CH₂−]ₙ | none | none |
| 5 | structure-of-alkenes | TF TH | 2 | no | 0 | 1 — CₙH₂ₙ | none | none |
| 6 | reactions-of-alkenes | TF TH | 2 | no | 0 | 3 — hydrogenation; hydration; halogenation | none | none |
| 7 | alcohols | TF TH | 2 | no | 0 | 3 — fermentation; hydration; combustion | none | none |
| 8 | carboxylic-acids | TF TH | 2 | no | 0 | 2 — acid+carbonate→salt+water+CO₂; acid+alcohol→ester+water | none | none |
| 9 | addition-polymerisation | TF TH | 2 | no | 0 | 1 — n(CH₂=CH₂)→(—CH₂—CH₂—)ₙ | none | none |
| 10 | condensation-polymerisation | TH | 2 | no | 0 | 2 — diol+diacid→polyester+water; diamine+diacid→polyamide+water | none | none |
| 11 | amino-acids | TH | 2 | no | 0 | 2 — –COOH+H₂N–→–CO–NH–+H₂O; protein+H₂O→amino acids | none | none |
| 12 | dna-naturally-occurring-polymers | TF TH | 2 | no | 0 | none | none | none |

Zero `fifas` lessons in this batch, matching BATCH-PLAN's FIFA column exactly
(every cell blank). No CFIFA form section was added to any file as a result —
step C of the task produced no output this batch, which is itself the
correct outcome rather than an omission.

## wrong_explanations key check

All 24 quiz items across the 12 files were checked mechanically: every item
has exactly 4 options, the `true` option sits at index 0 on all 24, and every
item's `wrong_explanations` keys match exactly the indices of its 3 wrong
options (`1,2,3`) — no shifted index anywhere. **No shifted-key defect found
anywhere in this batch.**

## Anything odd

1. **Spec-number agreement with BATCH-PLAN.md is perfect — all 12 of 12 rows
   match exactly**, including the four separate-science-prefixed rows
   (`structure-of-alkenes`, `reactions-of-alkenes`, `alcohols`,
   `carboxylic-acids`, `addition-polymerisation`, `condensation-
   polymerisation`, `amino-acids`, `dna-naturally-occurring-polymers`, all
   `— · 8462 4.7.x.x`). Continues batch-12's zero-disagreement run.

2. **FIFA/RP/equations columns also match BATCH-PLAN exactly on all 12
   rows** — BATCH-PLAN's FIFA and RP columns are blank for every one of
   this batch's 12 lessons, and the extracted files agree (0 fifas, 0 rp
   everywhere); the `eq` column numbers match the extracted `equations`
   list lengths exactly on every row that has one.

3. **No `examiner_tip` anywhere in this batch** — same pattern as every
   prior batch (4–12). All 12 files omit the `## examiner_tip` section
   entirely.

4. **No filename needed renaming** — all 12 extracted filenames were already
   clean (no spaces, no parentheses). Step B of the task was not needed.

5. **No subject:slug collisions were actually tested** — all 12 slugs were
   passed as `chemistry:<slug>` from the start (BATCH-PLAN marks every row
   `Chem`), so the extractor never searched biology/physics for them. This
   differs from batches 9–12's notes, which searched bare slugs first; here
   the subject was known up front and qualified immediately, which is also
   why the console output was 12 clean `wrote …` lines with no collision
   error printed for any slug.

6. **`higher` is present on all 12 lessons, but only 10 of them have another
   route to diff against.** Unlike batch-12 (where 4 lessons omitted the
   `## higher` section entirely), every one of this batch's 12 files HAS a
   `## higher` section. `condensation-polymerisation` and `amino-acids` are
   TH-only routes, so there is no sibling route for a copy section to exist
   against (their diff line reads "none" for that reason, not because the
   content is identical across routes that don't exist). The other 10
   lessons each carry one or two `## higher — <route> copy` sections.

7. **Every `higher — … copy` section renders `null`** across all 10 lessons
   that have one (14 copy-sections total: 6 lessons with a single Triple-
   Foundation-only copy since they are TF/TH routes, 4 lessons with both a
   Combined Foundation and a Triple Foundation copy since they are the
   CF/CH/TF/TH-route crude-oil/fractional-distillation/properties-of-
   hydrocarbons/cracking-alkenes group). No route actually diverges in its
   `higher` wording within this batch — same finding as batches 9–12.

8. **No `canonical_record` WARNING was printed by the extractor** — the
   extraction run's console output was 12 `wrote …` lines and nothing else.

9. **All 12 lessons' routes match BATCH-PLAN's routes column exactly** — no
   CF/CH/TF/TH discrepancy anywhere.

10. **This is the first all-organic-chemistry batch (topic 7, 8462 §4.7) seen
    9–13** — every lesson sits in `figlib/chemistry.py`'s `ORGANIC` table or
    its neighbouring box-notation polymer functions, which is why the
    diagram-library audit (`05-diagram-library/README.md`) found far more
    direct, purpose-built matches than batches 9–12 did (displayed
    formulae for every alkane/alkene/alcohol/carboxylic-acid named, plus an
    addition-polymer and a condensation-polymer figure built against this
    batch's own spec numbers). The gaps that remain are specific and
    narrow: no ester drawer exists despite a stub implying one does (flagged
    for `carboxylic-acids`), no addition-reaction mechanism or bromine-water
    test figure exists (`reactions-of-alkenes`), and no chain-length-vs-
    property trend chart is authored with real data (`properties-of-
    hydrocarbons`).
