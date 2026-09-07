# MRB-335 — KS3 biology bank top-up (B1–B11)

The biology content lane's log. One section per unit, in the order the lane
worked them (Rainford's autumn sequence): B1, B4, B2, B7, B3, B8, B9, B5, B10,
B11, B6.

## What every unit got

Each `(unit, band)` was taken to **52** rows — two clear of the ruled floor of
50, so no unit sits exactly on the line — spread evenly across the unit's
lessons. New ids continue each lesson's band sequence from `05`, and every new
row lands at `bank_position >= 12` by construction, because a position IS an
index and every row was **appended**. The first twelve rows of every file are
byte-identical to `HEAD`, proved two ways per unit: `git diff --numstat`
reporting zero deleted lines, and the first twelve question dicts parsed out of
the working tree compared against the same twelve parsed out of `git show HEAD:`.

That is what keeps the top-up invisible to AUTO composition (RISKS D7):
`auto_pool()` reads `bank_position < 12`, so every auto-composed assignment the
estate has ever produced is unchanged. Set work reads every position, which is
what these rows exist for.

| unit | lessons | new rows | easier | standard | harder | total |
|---|---|---|---|---|---|---|
| B1 | 6 | 84 | 52 | 52 | 52 | 156 |
| B4 | 5 | 96 | 52 | 52 | 52 | 156 |
| B2 | 4 | 108 | 52 | 52 | 52 | 156 |
| B7 | 4 | 108 | 52 | 52 | 52 | 156 |
| B3 | 8 | 60 | 52 | 52 | 52 | 156 |
| B8 | 5 | 96 | 52 | 52 | 52 | 156 |
| B9 | 6 | 84 | 52 | 52 | 52 | 156 |
| B5 | 8 | 60 | 52 | 52 | 52 | 156 |
| B10 | 5 | 96 | 52 | 52 | 52 | 156 |
| B11 | 4 | 108 | 52 | 52 | 52 | 156 |
| B6 | 3 | 120 | 52 | 52 | 52 | 156 |

**1,020 new biology rows.**

## The review method, and the one thing it changed

Every unit was read twice: once by its author as a cold examiner re-read, and
once by the lane against a set of mechanical checks — length parity (the
`1-length-parity` rule from `content_standards.md` §1), thin `why` fields,
self-containment, units on numeric harder stems, correct-option position
spread, and near-duplicate stems.

⚠️ **The self-containment rule applies to `why` fields, not just stems.** This
was the lane's largest finding about its own work. A `why` is rendered to the
child the moment they answer — on the assignment page, away from the lesson —
so a `why` that says "the belief this lesson exists to break" is exactly as
unmoored as a stem that says it. The first sweep checked stems only and found
~20 instances across the lane; extending it to option texts and `why` fields
found roughly three times as many again. Two of B9's three, and four of B10's
four, would not have surfaced from a stems-only scan.

A second refinement, contributed by the B10 author: **string similarity on
stems alone cannot tell a duplicate from a shared vocabulary frame.** Two short
stems ("What is a gene?" / "What is a gamete?") score 87% and are different
questions. A real duplicate repeats the question, so it also reuses the option
pool. The detector now reports stem similarity *and* shared-option count, which
separates the two cleanly and cleared three false alarms.

---

## B4 — breathing and gas exchange (5 lessons, +96 rows)

| lesson | easier | standard | harder |
|---|---|---|---|
| 01 the-gas-exchange-system | e05–e11 | s05–s11 | h05–h11 |
| 02 how-breathing-works | e05–e11 | s05–s11 | h05–h11 |
| 03 alveoli-built-for-exchange | e05–e10 | s05–s10 | h05–h10 |
| 04 exercise-asthma-and-smoking | e05–e10 | s05–s10 | h05–h10 |
| 05 stomata-and-gas-exchange-in-plants | e05–e10 | s05–s10 | h05–h10 |

Harder-band calculations carry their units throughout — a pressure difference
in kPa from a 2.4 → 2.9 litre chest volume change, alveolar surface area, and
the 78%/21%/16% composition figures.

**Review fixes.** Five self-containment defects, all pointing at things the
child cannot see on an assignment page: `b4-04-h10`'s stem asked "which two
factors from this lesson", and `b4-01-s08` said "using the figures" while
supplying none — that stem now states the composition figures itself.
`b4-03-s10` and `b4-03-h07` both appealed to "the four requirements" as a
numbered list; they now name the feature in words, which the options already
did, so nothing was lost. `b4-03-s09`'s distractor and its `why` appealed to
"the first of the four requirements". Six softer uses of "the route" as if it
were a named list became "the airway", the unit's own term. One length-parity
regression introduced by the h10 rewrite was closed afterwards by lengthening a
distractor rather than trimming the key.

---

## B2 — the skeleton and movement (4 lessons, +108 rows)

Every lesson took 9 per band: `e05–e13`, `s05–s13`, `h05–h13`. Lesson 04's
levers and forces carry the calculation rows, with units stated.

**Review fixes.** Two science corrections found by the cold read before any
reviewer saw the unit: `b2-02-h06`'s stem claimed "a horse's leg joints are
almost all hinges", which is false — a horse's hip and shoulder are
ball-and-socket — now scoped to the lower leg; and `b2-03-s06`'s key said a
held biceps is "matching the weight exactly", which is only true of turning
effects and so reached into lesson 04.

Four flagged stems in `questions_02_joints.py` said "this lesson". Sweeping the
whole unit found the defect at **10 sites across 3 files**, two of them in
`why` fields — the finding that made the lane extend the rule to whys
everywhere. All ten fixed; all four rewritten stems keep their original four
options and original correct answer.

⚠️ **A re-wrap artefact worth knowing about.** The author's helper used
`textwrap` with default `break_on_hyphens`, so a hyphenated word split across
source lines gained a spurious space and `b2-02-s11` rendered to the child as
"range-against- stability". Caught by reading the rows back as a child sees
them, not by any gate. The helper was hardened with `break_on_hyphens=False`
and all 108 rows swept for the signature. The lane's reviewer now checks for it
(`\w-\s` and doubled spaces) across stems, options and whys.

---

## B7 — photosynthesis (4 lessons, +108 rows)

Every lesson took 9 per band: `e05–e13`, `s05–s13`, `h05–h13`. Formulae are
written flat (`CO2`, `O2`) and no row carries markup.

**Review fixes.** `b7-04-e09` was a near-paraphrase of the existing frozen
`b7-04-e01`, and worse, e01's stem gave away half of e09's answer — replaced
outright with a new question on what a wheat grain is. Eighteen length tells
were repaired by lengthening a distractor into a wrong rule of the same shape
rather than by shortening the key, so no misconception was diluted.

Ten self-containment defects, all naming the lesson page's own interactive:
six flagged stems said "the bench" (a glucose counter, a dial, a leaf "set to
Broad"), and a sweep found four more in `why` fields citing "the counter" and
"the two readouts". Each was recast into a real situation carrying the same
science — a pot plant under a dimmed lamp, a grower's glasshouse short of
carbon dioxide, a pine needle against a broad oak leaf, a class investigation.
Where the question genuinely is about a model's limits rather than a real
plant, the stem now says "a simple computer model of a leaf", which is
self-contained.

⚠️ `b7-03-h09` was flagged and deliberately **kept**: its "bench" is a
laboratory bench in a real ethanol spill, which is correct and self-contained.
The lane ruled on this rather than letting a regex decide it.

**Open, passed upward:** `b7-01-h08` and `b7-04-h05` use the 10:1 figure that
`NOTES-B7` flag 19 says B9 may eventually own. If Mide moves it, two more sites
move with it.

---

## B3 — diet and digestion (8 lessons, +60 rows)

Lessons 01–04 took 3 per band (`e05–e07`), lessons 05–08 took 2 (`e05–e06`).
Energy rows carry kJ throughout.

**Review fixes.** Fifteen self-containment defects — eleven flagged, four more
found by the unit's own sweep. Two of the four are worth naming: `b3-06-s05`'s
`why` said "the counter still reads forty", which is the lesson page's enzyme
readout rather than a laboratory instrument; and `b3-02-e06`'s stem opened "All
four of these tests", which has no referent once the row is read on its own.

Four keys were conspicuously shorter than every distractor — a real tell,
because the odd one out is pickable without reading. `b3-03-s07`'s key was
"A surplus of 1250 kJ, which is stored." (8 words) against distractors of 13 to
16; `b3-04-e06`'s was "The body tissue that stores lipid." (6) against 11 to 12.
Both keys were lengthened rather than the distractors cut. Sweeping the unit at
`key < 0.8 × shortest distractor` caught two further instances.

⚠️ `b3-02-h05` and `b3-02-e07`'s "bench" were flagged and deliberately **kept**
— both are laboratory benches, one holding two unlabelled white powders and one
in a sentence about keeping a naked flame away from a water bath.

---

## B8 — respiration (5 lessons, +96 rows)

| lesson | easier | standard | harder |
|---|---|---|---|
| 01 aerobic-respiration | e05–e11 | s05–s11 | h05–h11 |
| 02 why-every-cell-respires | e05–e11 | s05–s11 | h05–h11 |
| 03 anaerobic-respiration-in-humans | e05–e10 | s05–s10 | h05–h10 |
| 04 fermentation | e05–e10 | s05–s10 | h05–h10 |
| 05 aerobic-vs-anaerobic | e05–e10 | s05–s10 | h05–h10 |

Eight harder-band calculations, each with a named wrong move behind every
distractor: masses from the 180:192:264:108 ratio, 15.6 kJ per gram, the
demand−supply gap, lactate clearance time, a twentyfold yield.

**Review fixes — including the lane's worst content defect.**

⚠️ **`b8-05-e08` had two defensible answers.** It asked which case is supplied
almost entirely by *anaerobic* respiration, keyed to yeast in sealed dough, but
also offered "a sprinter in the last three seconds of a race" — which is the
lactic-acid case the unit itself teaches, and therefore also correct. Fixed by
replacing that option with "a resting muscle with blood flowing normally
through it", whose `why` names the misconception: being a muscle is not what
makes respiration anaerobic, running short of oxygen is. Its partner
`b8-05-e07` (the aerobic version) is a deliberate contrast pair and stays.

Two further science fixes came from the author's own cold read: `b8-01-e10`'s
key overclaimed that window mist is mostly metabolic water, and `b8-04-h05`
carried an arithmetic error inside a distractor's `why` (60 less 12% is 52.8,
not 48) so the named wrong move was not the one actually made. `b8-04-e10` had
a second defensible answer — "warmth, so that it runs at a useful rate" — since
cold only slows fermentation; replaced with a genuinely non-optional condition.

Eleven self-containment defects: four stems naming "the ledger", five rows
appealing to "the four jobs" as a list the child was never given, and three
using "the ceiling" as jargon their own stems never introduce. The term was
deliberately **kept** in `b8-03-s05`, `h05` and `h10`, whose stems state the
ceiling of 80 units themselves, so it is grounded in the row.

---

## B9 — ecosystems (6 lessons, +84 rows)

Lessons 01–04 took 5 per band, lessons 05–06 took 4. Lesson 06's harder band
carries the sampling calculations — quadrat-area scaling, sample size against
estimate, and a capture–mark–recapture estimate — all with units.

**Review fixes.** `b9-02-h05` said a reindeer herd reached six thousand "in
thirty years"; the introduction-to-peak interval was under twenty. `b9-04-h06`
(cocoa midges) had a distractor saying the midges fed on the litter, which is
close enough to the key to be arguable — replaced with a root-damage
distractor. Fifteen length tells were trimmed or balanced, and two more
(`b9-04-e08`, `b9-05-h08`) were closed by the lane afterwards.

Three self-containment defects, **two of which a stems-only scan would have
missed** — they were in `why` fields. This unit is where that lesson was
learned, because its existing frozen rows lean heavily on "the bench" and
"presses Ten years", and the author was explicitly told not to copy the habit.

**Deviation, and it was the right call.** The lane's brief named transects as
scope for lesson 06. The lesson file puts transects in `ks4_becomes`
("Required practical fieldwork: … transects along an environmental gradient"),
i.e. explicitly beyond KS3 here, so no transect rows were written. The harder
band took quadrat scaling and capture–mark–recapture instead, both of which the
lesson's own stretch layer and existing `h01` already establish as in scope.

---

## B5 — reproduction, human and plant (8 lessons, +60 rows)

Lessons 01–04 took 3 per band, lessons 05–08 took 2. Register held throughout:
correct scientific terms, clinical and matter-of-fact, nothing that could
embarrass a child reading it in class.

**Review fixes.** Three named rows plus a wider sweep. `b5-03-h05`'s key was
three words against distractors of nine or more; all four options now carry a
method clause of the same shape ("About day 14, the day that applies to every
cycle" / "About day 17, a fortnight back from the end of the cycle"), which
preserves the actual demand — which end of the cycle the fortnight is counted
from. Eight further parity outliers were fixed on the same principle, and two
were judged false positives and left: in `b5-01-e07` and `b5-02-e06` another
distractor is exactly as short as the key, so the key is not the odd one out
and a length strategy fails.

Two self-containment defects, one of them a **copied habit**: `b5-08-e06`'s
stem opened "In one of the five dispersal methods…", which is exactly what the
frozen `b5-08-e04` does. The author had copied the frozen rows' style and
corrected it rather than propagating it.

---

## B10 — variation and inheritance (5 lessons, +96 rows)

Lessons 01–02 took 7 per band, lessons 03–05 took 6.

**Ruling respected:** lesson 04 carries a NOTES flag holding "dominant",
"recessive", "allele", "Punnett", "genotype" and "phenotype" back to GCSE. All
18 lesson-04 rows were grepped clean and use the page's own vocabulary (P/p,
"version of a gene", pure-breeding, 3:1).

**Review fixes.** `b10-01-s07` had an arguably-defensible distractor — a bimodal
height graph in a mixed-sex class is a real phenomenon — replaced with a
clearly wrong one about group width. `b10-05-h06`'s key relied on a fact the
stem never gave, so the fact moved into the stem. Fourteen length tells fixed,
then seven more on the lane's stricter measure.

⚠️ **A measurement disagreement worth recording.** The author called
`b10-03-s09` a false positive at 18 words against 15. It is 22 against 15 —
`str.split()` counts "DNA's", "X-ray", "King's" and "Franklin's" as one token
each, and splitting on punctuation gives the true count. The row was over both
thresholds. The author's *substantive* point stood, though: trimming the key
would have cost "and it was he who showed Franklin's image to Watson", which is
the half that places Wilkins accurately against Franklin. So the fix lengthened
the Chargaff distractor instead, and the tell now runs the safe way round — the
longest option is a distractor, which helps no guesser.
