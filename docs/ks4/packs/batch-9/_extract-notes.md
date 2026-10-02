# Batch 9 — extraction notes

Facts only, read straight from the 15 extracted files in
`04-checked-science-source/` (each file's header gives the routes; `##`
section presence gives everything else). No route-copy `quiz` section exists
in ANY of the 15 files — every route a lesson appears on serves the identical
TH quiz list, so "quiz count per route" below is one number covering every
route listed. The only field that ever differs by route is `higher`.

| # | Lesson | Routes | Quiz count (same on every route) | examiner_tip | fifas | equations | rp (verbatim) | variables |
|---|---|---|---|---|---|---|---|---|
| 1 | dna-structure | TF TH | 2 | no | 0 | none | none | none |
| 2 | genetic-inheritance | CF CH TF TH | 3 | no | **1** | none | none | none |
| 3 | inherited-disorders | CF CH TF TH | 2 | no | **1** | none | none | none |
| 4 | sex-determination | CF CH TF TH | 2 | no | 0 | none | none | none |
| 5 | variation | CF CH TF TH | 3 | no | 0 | none | none | none |
| 6 | evolution-natural-selection | CF CH TF TH | 3 | no | 0 | none | none | none |
| 7 | selective-breeding | CF CH TF TH | 2 | no | 0 | none | none | none |
| 8 | genetic-engineering | CF CH TF TH | 2 | no | 0 | none | none | none |
| 9 | cloning | TF TH | 2 | no | 0 | none | none | none |
| 10 | theory-of-evolution | TF TH | 2 | no | 0 | none | none | none |
| 11 | understanding-genetics | TF TH | 2 | no | 0 | none | none | none |
| 12 | evidence-for-evolution | CF CH TF TH | 2 | no | 0 | none | none | none |
| 13 | fossils-extinction | CF CH TF TH | 2 | no | 0 | none | none | none |
| 14 | resistant-bacteria | CF CH TF TH | 3 | no | 0 | none | none | none |
| 15 | classification-living-organisms | TF TH | 2 | no | 0 | none | none | none |

Exactly two `fifas` lessons, matching BATCH-PLAN's FIFA column exactly
(#2 genetic-inheritance, #3 inherited-disorders — both score a Punnett-square
cross through to a probability). The CFIFA form (step C) was appended to both
files, four FIFA steps kept byte-identical, Convert step added: both are pure
genetics-probability questions with no physical quantity to convert (no
length, mass or time anywhere in either FIFA), so both Convert steps state
that nothing needs converting — same shape as batch-8's blood-glucose-diabetes
case, not its reaction-time one.

## wrong_explanations key check

All 34 quiz items across the 15 files were checked mechanically: every item
has exactly 4 options, `correct_index` is 0 on all 34, and every item's
`wrong_explanations` keys match exactly the indices of its 3 wrong options
(`1,2,3`) — no shifted index anywhere. A word-overlap pass additionally
flagged 15 of the 34 items (spanning 20 individual explanation keys, some
items flagged on more than one key) as "low overlap" between an option's text
and its own explanation's text, purely because the explanations paraphrase
rather than reuse the option's wording (e.g. `classification-living-organisms`
q1's option "Woese discovered a new type of organism" is explained by "Archaea
were already known — but rRNA sequencing revealed..." — zero shared words,
correct content). **Every one of the 15 flagged items was read in full and is
correctly aligned** — key `n`'s text genuinely answers why option `n` is
wrong, never a neighbour's option. **No shifted-key defect found anywhere in
this batch.**

## Anything odd

1. **Heaviest spec-number disagreement with BATCH-PLAN.md seen in any batch so
   far: all 15 of 15 rows differ from the plan's guess**, not a subset as in
   batches 7–8. The plan guessed specs across 4.6.1.4–4.6.4; the data's actual
   specs run 4.6.2.1–4.6.7, a block consistently shifted later and coarser.
   Full list: #1 dna-structure `— · 8461 4.6.1.5`→`4.6.2.1`; #2
   genetic-inheritance `4.6.1.4`→`4.6.3`; #3 inherited-disorders
   `4.6.1.5`→`4.6.3.2`; #4 sex-determination `4.6.1.6`→`4.6.3.3`; #5 variation
   `4.6.2.1`→`4.6.4`; #6 evolution-natural-selection `4.6.2.2`→`4.6.5`; #7
   selective-breeding `4.6.2.3`→`4.6.6`; #8 genetic-engineering
   `4.6.2.4`→`4.6.7`; #9 cloning `— · 8461 4.6.2.5`→`4.6.4`; #10
   theory-of-evolution `— · 8461 4.6.3.1–4.6.3.2`→`4.6.3.3`; #11
   understanding-genetics `— · 8461 4.6.3.3`→`4.6.3.4`; #12
   evidence-for-evolution `4.6.3.1`→`4.6.5`; #13 fossils-extinction
   `4.6.3.2–4.6.3.3`→`4.6.5`; #14 resistant-bacteria `4.6.3.4`→`4.6.5`; #15
   classification-living-organisms `4.6.4 · 8461 4.6.4`→`4.6.5`. As with
   batches 7 and 8, the extractor's spec comes straight off the data;
   BATCH-PLAN's spec column should not be cited directly for any row here.

2. **Five lessons share the actual spec `4.6.5`**: #6
   evolution-natural-selection, #12 evidence-for-evolution, #13
   fossils-extinction, #14 resistant-bacteria, #15
   classification-living-organisms. This is the data's own subtopic numbering
   being coarser than one-spec-per-lesson across this whole evolution/fossils/
   classification stretch, not an extraction error — same shape as batch-8's
   note #4, just five lessons deep instead of two. Two further pairs collide
   on their own: #5 variation and #9 cloning both `4.6.4`; #4 sex-determination
   and #10 theory-of-evolution both `4.6.3.3`.

3. **No `examiner_tip` anywhere in this batch** — same pattern as every prior
   batch (4–8). All 15 files omit the `## examiner_tip` section entirely.

4. **No filename needed renaming** — all 15 extracted filenames were already
   clean (no spaces, no parentheses). Step B of the task was not needed.

5. **No subject:slug collisions.** All 15 slugs are Biology-only and
   extracted cleanly as bare slugs with a single `wrote …` line each.

6. **Five Triple-only lessons, all TF+TH.** #1 dna-structure, #9 cloning, #10
   theory-of-evolution, #11 understanding-genetics, #15
   classification-living-organisms appear on Triple Foundation + Triple Higher
   only — matching BATCH-PLAN's routes column exactly for all five.

7. **`higher` differs on 14 of the 15 lessons** — always Combined Foundation
   and/or Triple Foundation, never Combined Higher, same pattern as every
   prior batch. The 9 CF+TF lessons (both copies): genetic-inheritance,
   inherited-disorders, sex-determination, variation,
   evolution-natural-selection, selective-breeding, genetic-engineering,
   evidence-for-evolution, resistant-bacteria. The 5 TF-only lessons (their
   one copy, since they carry no Combined route at all): dna-structure,
   cloning, theory-of-evolution, understanding-genetics,
   classification-living-organisms. Only #13 fossils-extinction has no
   `higher` section at all — the sole lesson in this batch with identical
   content across every tier it appears on.

8. **Every `higher — … copy` section renders `null`** across all 14 lessons
   that have one — i.e. every non-TH route's `higher` copy is identical to the
   canonical TH value (`null` meaning "no difference", not "no content";
   see the extractor's own note on how a route's `higher: None` would render
   fenced). No route actually diverges in its `higher` text within this
   batch — the field is present/absent per-route, never worded differently.

9. **No `canonical_record` WARNING was printed by the extractor** — the
   extraction run's console output was 15 `wrote …` lines and nothing else.
