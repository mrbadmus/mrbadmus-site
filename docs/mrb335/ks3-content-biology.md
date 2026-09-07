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
