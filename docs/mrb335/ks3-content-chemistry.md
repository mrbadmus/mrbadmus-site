# MRB-335 — KS3 chemistry bank top-up (C1–C10)

The lane log. One section per unit, plus the adjacent defect that was fixed
before any authoring started. Written as the work happened, so the order below
is the order Rainford teaches the units in: C1, C2, C3, C6, C4, C8, then C5,
C7, C9, C10.

Quota per unit is `50 − 4 × lessons` new rows **per band**, spread evenly over
the unit's lessons, so every `(unit, band)` finishes at 50 or more. New ids
continue each lesson's band sequence from `05`; `bank_position` continues from
12 within the lesson; the first twelve rows of every lesson are untouched.

Gates after every unit: `python3 -m ks3_data.question_bank` and
`python3 verify_questions.py`, both clean, then a cold examiner re-read of that
unit's new rows before the commit.

---

## Adjacent defect — raw `<sub>` markup in three C8 bank rows

Found and named by MRB-335 in `MARKUP_KNOWN`; fixed here because it is a
content edit in `ks3_data/c8/` and this is the chemistry content lane.

Bank text is inserted into the assignment page with `document.createTextNode`,
so a tag in a bank row is shown to the child literally, angle brackets and
all. Three rows carried `<sub>2</sub>`:

| id | file | sites |
|---|---|---|
| `c8-02-s03` | `ks3_data/c8/questions_02_mendeleev.py` | stem ×2 (`SiO₂`, `SnO₂`), correct option ×1 (`XO₂`) |
| `c8-03-e02` | `ks3_data/c8/questions_03_groups_and_periods.py` | why 3 ×1 (`MgCl₂`) |
| `c8-03-h04` | `ks3_data/c8/questions_03_groups_and_periods.py` | stem ×2 (`CO₂`, `SiO₂`), why 0 ×1 (`SnO₂`), why 1 ×1 (`Na₂O`) |

**Eight sites, not six.** The brief said six; `c8-02-s03`'s stem carries two
formulae and `c8-03-h04`'s carries two more, so the count of *sites* is eight
across the three *rows*. Every one was `<sub>2</sub>` and every one became the
single character `₂`. No other text changed, and no option's meaning moved —
these are the rows where the notation IS the question (a group predicts a
combining ratio), which is the one case the authoring brief allows a real
subscript character in.

`MARKUP_KNOWN` in `ks3_data/question_bank.py` is now `frozenset()`, with its
comment rewritten to say the set stays empty rather than describing three
outstanding rows. That is the one edit this lane made outside `ks3_data/c*/`,
and it was named in the brief.

Gates after the fix: `question_bank` OK (185 lessons, 2220 questions),
`verify_questions` OK (all nine checks clean).

---
## C1 — Particles and their behaviour (6 lessons)

**Quota:** 28 new rows per band (52 per band across the unit), 84 rows total.
Spread 5 · 5 · 5 · 5 · 4 · 4 per band across the six lessons.

| lesson | easier | standard | harder |
|---|---|---|---|
| 01 particle-model | e05–e09 | s05–s09 | h05–h09 |
| 02 solids-liquids-and-gases | e05–e09 | s05–s09 | h05–h09 |
| 03 changes-of-state | e05–e09 | s05–s09 | h05–h09 |
| 04 gas-pressure | e05–e09 | s05–s09 | h05–h09 |
| 05 diffusion | e05–e08 | s05–s08 | h05–h08 |
| 06 testing-the-model | e05–e08 | s05–s08 | h05–h08 |

Final band totals: easier 52, standard 52, harder 52.

**Ladder avoidance.** Each lesson's four rungs were read before authoring and
worked around. Where a rung already owned an idea the top-up takes a different
cut at it: L3's rung 2 owns "what is the energy doing during the plateau", so
the new `s06` asks what it is doing during the CLIMB; L5's rung 4 owns the
hot-versus-cold glass, so the new rows take the squaring rule, the lung, the
Perrin measurement and the size of a cell instead.

### Review fixes before commit

**1 · The option-length tell — a gate I turned red, and the finding that
matters most in this log.** `verify_answer_lengths.py` (MRB-297) measures how
often the option that is visibly longest — six characters or more clear of the
runner-up — is the correct one. Chance is 25%; above 35% it fails. My first
draft of C1's 84 rows ran at **84.2%**, which took the whole unit to 71.1% and
turned the gate red on two scopes: `bank/C1` and `bank/whole corpus BIO+CHEM`.

The cause is a drafting habit rather than an accident: the correct answer
carries the reasoning ("because the small water particles drop into the gaps
between the large ones") while a distractor only has to be wrong, so the key
ends up the longest line on the screen and a child who reads none of the
chemistry scores well above chance.

Forty-nine options were rewritten — in almost every case by giving a distractor
the same level of detail as the key, which is what §1 of `content_standards.md`
asks for anyway ("where the key must be precise, at least one distractor is
equally precise but wrong"). C1's new rows now sit at **0.0%** on this measure,
the unit at 27.5%, and the whole-corpus BIO+CHEM cell has come DOWN from its
52.7% baseline to 51.9%. Every unit after this one was authored with the
constraint in hand rather than repaired afterwards.

**2 · `c1-01-e05` — a `why` that contradicted `c1-01-h09`.** The distractor
"about two million" was corrected with "that is roughly how many particles lie
along the edge", but `h09` derives the edge count as about 17 million from the
bench's own two dozen halvings (2²⁴ ≈ 16.8 million, and 1 cm ÷ 0.6 nm ≈ 1.7 ×
10⁷ — the two agree, which is why the row is worth having). The `why` now makes
the point without a number.

**3 · `c1-01-h06` — two defensible answers.** The key was "under 100 ml" and a
distractor read "exactly 97 ml", which is itself under 100. Replaced with "it
cannot be predicted, because the model says nothing about how big a particle
is" — a real misconception, and no longer a second correct answer.

**4 · `c1-01-s06` — an impossible reading.** A distractor offered "less than 50
ml" for a mixture whose total is 97 ml. Now "well under 97 ml".

Gates at commit: `question_bank` OK, `verify_questions` OK (all nine checks),
`verify_answer_positions` OK, `verify_answer_lengths` green on every chemistry
scope.

---
## C1 follow-up — answer POSITION rebalanced

Committing C1 and then measuring C2 exposed a second tell of the same family,
in the other gate's territory. `verify_answer_positions.py` (MRB-278) passes on
the whole KS3 bank, so nothing went red — but C1's 84 new rows had landed
19 · 27 · 28 · 10 across the four option slots, and C2's first draft was worse
still at 19 · 48 · 14 · 3. Fifty-seven per cent of a unit's new rows with the
key in slot two is a strategy a child can find without reading any chemistry.

The cause is the same drafting habit as the length tell: you write the
plausible wrong answer first, then the key, then pad out the rest.

Both units' new rows were permuted — options reordered verbatim, the `why`
travelling with its own option, nothing at `bank_position` < 12 touched —
walking each band in bank order and cycling the target slot 0, 1, 2, 3. Both
units now sit at exactly 21 · 21 · 21 · 21. Every unit from C3 on is rebalanced
the same way before its commit.

---

## C2 — Atoms, elements and compounds (6 lessons)

**Quota:** 28 new rows per band (52 per band across the unit), 84 rows total.
Spread 5 · 5 · 5 · 5 · 4 · 4 per band.

| lesson | easier | standard | harder |
|---|---|---|---|
| 01 the-atom-daltons-model | e05–e09 | s05–s09 | h05–h09 |
| 02 elements | e05–e09 | s05–s09 | h05–h09 |
| 03 compounds | e05–e09 | s05–s09 | h05–h09 |
| 04 chemical-symbols | e05–e09 | s05–s09 | h05–h09 |
| 05 formulae | e05–e08 | s05–s08 | h05–h08 |
| 06 conservation-of-mass | e05–e08 | s05–s08 | h05–h08 |

Final band totals: easier 52, standard 52, harder 52.

**Subscripts.** C2's notation lessons are the case `ks3-authoring.md` §9 names:
`c2-05-s05` asks what the small 3 in NH₃ counts, and the question is
unanswerable written flat. Those rows carry the real character (₃, ₂, ₄) and
never `<sub>`. Rows where the formula is only mentioned in passing stay flat.

### Review fixes before commit

**1 · The mirror of the length tell — overcorrecting is also a fail.** Having
learnt the giveaway lesson on C1, I wrote every C2 row with a distractor longer
than the key. That took the unit to **5.9%** and `verify_answer_lengths` failed
it again, from the other side: *"the long option is never right — the mirror
tell"*. The gate's band is 12% to 35% around a chance rate of 25%, and a corpus
where the long option is reliably WRONG is exactly as exploitable as one where
it is reliably right.

Twenty padded distractors were trimmed back so the key is the longest in about
one question in four. C2 now measures 23.2%, C1 27.5% — both at chance. **The
authoring rule that comes out of this is not "keep the key short". It is: make
the key the longest in roughly a quarter of the rows, and nothing anywhere in
the four options should be decorative.**

**2 · `c2-02-e09` — two defensible answers, from an imprecise stem.** It asked
which pair of the body's six elements "makes up most of it". By mass that is
oxygen and carbon; the intended key was oxygen and hydrogen, which is the pair
the lesson names as being present almost entirely as water. Re-pointed to the
claim the lesson actually makes — "which two of them are almost all present as
water" — with the three distractors rewritten to match.

**3 · Nothing built on the "Latin symbols are the ancient elements" line.** The
lesson's key note says the elements with Latin symbols "are the elements people
knew first". That holds for Fe, Pb, Au and Cu; sodium and potassium were not
isolated until 1807, so Na and K are counter-examples inside the lesson's own
list. No new row asserts the generalisation, and none uses K. Flagged here
rather than fixed, because the lesson text is outside this lane.

Gates at commit: `question_bank` OK; `verify_answer_positions` OK;
`verify_answer_lengths` green on `bank/C1` and `bank/C2`.
`verify_questions.py` is RED for a reason outside chemistry — see the
cross-lane finding below.

---

## Cross-lane finding — `verify_questions.py` check 8 is wrong once ANY unit is topped up

Not a chemistry defect and not fixable from this lane (`verify_questions.py` is
outside the files I may edit), but it will stop every content lane from
reporting a clean full gate, so it is written down here.

Check 8 exercises `compose_assignment` against unit **B1** and builds its
expectation like this:

```python
own = [q["id"] for q in bank.get(keys[5], []) if q.get("band") == "standard"]
```

— the WHOLE lesson, not `auto_pool(...)`. The whole point of MRB-335's cap is
that composition reads only `bank_position < 12`, so the moment B1's lessons
grow past four standard rows the check expects eight ids and correctly receives
four:

```
expected ['b1-05-s01' … 'b1-05-s08']   got ['b1-04-s01' … 'b1-03-s03']
```

**`compose_assignment` is behaving correctly.** Proved directly: with every
lesson in the bank truncated to its original twelve, the same check passes
(own-first true, nearest-first true, length 15) on today's data. The two lines
that need `auto_pool(bank.get(...))` are `own` and `nearest` in check 8.

Check 8 only ever builds its keys from B1, so chemistry alone can never trip
it; the biology lane reached it first. C1 was committed while the gate was
still fully green, and C2 onwards are committed with this one check red for a
cause proven to be outside `ks3_data/c*/`.

`verify_answer_lengths` is separately red on `bank/B1 B2 B4 B6 B7 B8 B10 B11`
and on the whole-corpus BIO+CHEM cell: the biology lane's new rows carry the
giveaway tell that C1's first draft had. Worth passing on before that lane
commits much more of it.

---
## C3 — Separating mixtures (7 lessons)

**Quota:** 22 needed per band; 23 added, taking every band to **51** across the
unit. Spread 4 · 4 · 3 · 3 · 3 · 3 · 3 per band.

| lesson | easier | standard | harder |
|---|---|---|---|
| 01 pure-or-mixture | e05–e08 | s05–s08 | h05–h08 |
| 02 dissolving-and-solutions | e05–e08 | s05–s08 | h05–h08 |
| 03 filtration | e05–e07 | s05–s07 | h05–h07 |
| 04 evaporation-and-crystallisation | e05–e07 | s05–s07 | h05–h07 |
| 05 distillation | e05–e07 | s05–s07 | h05–h07 |
| 06 chromatography | e05–e07 | s05–s07 | h05–h07 |
| 07 proving-something-is-pure | e05–e07 | s05–s07 | h05–h07 |

Final band totals: easier 51, standard 51, harder 51 — over the floor of 50,
one short of the 52 the brief aims at. Left at 51 rather than padded: the
seven lessons divide 23 evenly at 4 · 4 · 3 · 3 · 3 · 3 · 3, and a
twenty-fourth row would have gone somewhere for the sake of the number.

Positions rebalanced to 18 · 20 · 16 · 15 across the four slots. Length tell
brought to 22.1% by trimming sixteen padded distractors — the same correction
C2 needed, applied before the commit this time rather than after it.

### Review fixes before commit

**1 · `c3-02-h08` — the stem let a bigger cause in.** It asked why an opened
can left in a warm room goes flat within an hour. The honest answer is *because
it was opened*; the lesson's point is about temperature. Rewritten to compare
two cans opened at the same moment, one warm and one in a fridge, so the only
variable left is the one the lesson teaches.

**2 · Two `why` fields left correcting something the child could no longer
see.** Trimming a padded distractor can orphan its `why`: `c3-03-e07`'s
correction still argued about a microscope the option no longer mentioned, and
`c3-03-h06`'s distractor had been trimmed into nonsense ("then wet the paper").
Both rewritten. A lesson for the remaining units: after a length trim, re-read
the `why` under it.

Gates at commit: chemistry-only `validate_lesson` clean across all ten units
(894 rows), `verify_answer_positions` OK, `verify_answer_lengths` green on
`bank/C3`.

---
## C6 — Acids and alkalis (7 lessons)

**Quota:** 22 needed per band; **28 added**, taking every band to **56**. Four
per lesson per band across all seven lessons — more than the brief asks for,
because four sits naturally on each of these lessons and dropping three of them
to three would have meant cutting a written row rather than not writing it.

| lesson | easier | standard | harder |
|---|---|---|---|
| 01 acids-and-alkalis | e05–e08 | s05–s08 | h05–h08 |
| 02 the-ph-scale-and-indicators | e05–e08 | s05–s08 | h05–h08 |
| 03 neutralisation | e05–e08 | s05–s08 | h05–h08 |
| 04 acid-plus-metal | e05–e08 | s05–s08 | h05–h08 |
| 05 acids-and-carbonates | e05–e08 | s05–s08 | h05–h08 |
| 06 making-a-pure-dry-salt | e05–e08 | s05–s08 | h05–h08 |
| 07 catalysts | e05–e08 | s05–s08 | h05–h08 |

Final band totals: easier 56, standard 56, harder 56. Positions 21 · 21 · 21 ·
21. Length tell 25.5% — and worth noting, because C6 carries a `BASELINE` row
in `verify_answer_lengths` at **65.4%**: the original twelve of this unit are
one of the estate's worst giveaway cells. The top-up has pulled the whole unit
from 65.4% to 25.5%, which is chance.

### Review fixes before commit

**1 · Three new rows asked a question the unit already asked — and the gate
could not see it.** This is the finding of the unit, and it is the reason the
cold re-read is not optional.

| new row | duplicated | how it slipped through |
|---|---|---|
| `c6-07-h07` | `c6-07-h02` | Same question, same answer: *which flask proves that coming back unchanged is not enough to be a catalyst.* The stems differ by four words — "on the five-flask bench" against "from the five flasks" — so `_normalise` treats them as different strings and the duplicate-stem check passes. |
| `c6-07-h08` | `c6-07-s03` | Both ask whether a catalyst could make copper react with dilute acid. Different band, same content. |
| `c6-03-h08` | `c6-03-s02` | Both explain why one drop moves the pH from 3 to 11. |

`validate_lesson`'s duplicate check compares normalised stems and normalised
answer sets. It catches a row written twice; it cannot catch a row written
twice in different words, which is what a top-up produces when the author is
working from the same lesson notes that produced the original twelve.
Replaced with a rate-versus-yield question, the possible-versus-worth-doing
distinction from the ammonia process, and a proportional titration
calculation (25 cm³ needs 20 cm³, so 50 cm³ needs 40 cm³).

**2 · `c6-05-h08` — a metal described as a white powder.** Changed to grey.
Magnesium and zinc powders are grey, and the row is about identifying a metal
from two gas tests.

**3 · A tooling note.** `rebalance` has to be run until it reports zero rows to
permute; a single pass converged for C1–C3 and left nine rows in C6, all of
them in one file. Running it again clears them. Worth knowing for the units
still to come.

Gates at commit: chemistry-only `validate_lesson` clean, `verify_answer_positions`
OK (whole KS3 bank, worst index 27%), `verify_answer_lengths` green on
`bank/C6` at 25.5% against a 65.4% baseline.

---
## C4 — Chemical reactions and equations (5 lessons)

**Quota:** 30 needed per band; 31 added, taking every band to **51**. Spread
7 · 6 · 6 · 6 · 6 per band, 93 rows.

| lesson | easier | standard | harder |
|---|---|---|---|
| 01 chemical-vs-physical-change | e05–e11 | s05–s11 | h05–h11 |
| 02 reactions-rearrange-atoms | e05–e10 | s05–s10 | h05–h10 |
| 03 word-equations | e05–e10 | s05–s10 | h05–h10 |
| 04 mass-in-a-reaction | e05–e10 | s05–s10 | h05–h10 |
| 05 symbol-equations-and-balancing | e05–e10 | s05–s10 | h05–h10 |

Formulae are FLAT throughout (`H2O`, `2H2`, `CH4`, `Fe2O3`), matching this
unit's original twelve. C2's subscript exception does not apply here: C4 is
about balancing, not about notation, and its existing rows are flat.

Positions 24 · 24 · 24 · 21. Length tell 18.9%.

### Review fixes before commit

**1 · A near-duplicate DETECTOR, written because C6 showed the eye is not
enough.** `nearpub.py` in the lane's scratch directory scores every new row
against every other row in its own lesson — 60% on the words of the stem, 40%
on the words of the correct option, both normalised and stopped — and lists the
close pairs for a person to judge. It is a shortlist, not a verdict: two rows
can share every content word and be different questions.

On C4 it found **ten** rows that repeated a question the unit already asked,
all of them invisible to `validate_lesson`:

| new row | duplicated | what was repeated |
|---|---|---|
| `c4-02-s08` | `c4-02-s01` | where the carbon atom in burning methane ends up |
| `c4-02-s09` | `c4-02-h03` | what has happened to the copper atoms in copper oxide |
| `c4-02-h10` | `c4-02-h01` | why a nuclear change is not a chemical reaction |
| `c4-03-h07` | `c4-03-h03` | why a word equation cannot tell an engineer how much oxygen |
| `c4-04-s06` | `c4-04-e03` | the missing unit on a mass answer |
| `c4-04-s09` | `c4-04-s02` | covering a bar and reading the calculation off |
| `c4-04-s10` | `c4-04-s03` | the football as evidence that a gas has mass |
| `c4-04-h07` | `c4-04-s04` | a gas loss too small for a school balance |
| `c4-05-s05` | the LADDER's explain rung | why 2Mg + O2 makes 2MgO needs its two |
| `c4-05-s10` | `c4-05-h01` | that balancing cannot tell you the products |

`c4-05-s05` is the one worth naming separately: it did not duplicate another
bank row, it restated **rung 3 of the lesson's own ladder**, which
`ks3-authoring.md` §10 forbids and no gate checks. Replaced with an
already-balanced equation (C + O2 makes CO2, no numbers needed), which is a
useful item this file did not have.

**2 · The replacement itself needed replacing.** The first rewrite of
`c4-05-s10` asked for a count of oxygen atoms and came to four — the same task
and the same answer as `c4-05-h03`. Re-pointed at 3NH3 and twelve. Worth
recording: a replacement written in the same sitting reaches for the same
material.

**3 · Two pairs left standing deliberately.** `c4-05-e02` (hydrogens in 3H2O)
and the new `c4-05-e09` (oxygens in 3CO2) score 0.76 and are a legitimate
parallel — different formula, different element, the same skill practised
twice, which is what a bank of fifty is for. `c4-04-s02` and the new
`c4-04-e09` score 1.00 on shared vocabulary and ask different questions about
the same diagram: one asks which bar is the whole, the other asks what covering
a part leaves you.

**4 · A syntax error I introduced and the gate caught.** One option in
`c4-05-s10`'s first draft was written `"correct": False",` with an empty `why`.
`python3 -m ks3_data.question_bank` failed to import the module and said which
line. Repaired before anything else was run.

Gates at commit: chemistry-only `validate_lesson` clean, `verify_answer_positions`
OK, `verify_answer_lengths` green on `bank/C4`.

---
## Retro sweep — the detector run back over C1, C2, C3 and C6

The near-duplicate detector was written during C4, so the four units committed
before it had never been through it. Running it back over them found five more
rows that repeated a question their own unit already asked. All five are fixed
here, in one commit, because a fix that spans three units is not a top-up and
splitting it three ways would only hide what it is.

| unit · row | duplicated | what was repeated |
|---|---|---|
| `c2-03-e09` | `c2-03-h04` | the Red Sea being saltier than the Baltic, and what that establishes |
| `c3-02-e06` | `c3-02-h04` | the nail-varnish-and-remover scenario |
| `c6-04-h08` | `c6-04-s02` | whether warming could make copper react with acid |
| `c6-06-h08` | `c6-06-e02` | reading a salt's name backwards to its acid and its metal |
| `c6-06-s06` | `c6-06-e03` | leftover solid on the bottom meaning the acid is used up |

`c3-02-e06` is the interesting one: the question was genuinely different — the
original asks what the word *insoluble* is worth, the new one asks what the
remover is CALLED — but both were set in nail varnish, so an assignment drawing
both would read as one question asked twice. Moved to grease and white spirit.
Same concept, different bench.

C1 came back clean at the threshold, which is worth recording: it was the unit
authored most slowly, before either calibration pass existed.

---
## C8 — The periodic table (7 lessons)

**Quota:** 22 needed per band; 23 added, taking every band to **51**. Spread
4 · 4 · 3 · 3 · 3 · 3 · 3 per band, 69 rows.

| lesson | easier | standard | harder |
|---|---|---|---|
| 01 metals-and-non-metals | e05–e08 | s05–s08 | h05–h08 |
| 02 mendeleev | e05–e08 | s05–s08 | h05–h08 |
| 03 groups-and-periods | e05–e07 | s05–s07 | h05–h07 |
| 04 group-1-the-alkali-metals | e05–e07 | s05–s07 | h05–h07 |
| 05 group-7-the-halogens | e05–e07 | s05–s07 | h05–h07 |
| 06 group-0-and-why-groups-exist | e05–e07 | s05–s07 | h05–h07 |
| 07 metal-and-non-metal-oxides | e05–e07 | s05–s07 | h05–h07 |

Positions 18 · 18 · 18 · 15. Length tell **22.1%**, against a `BASELINE` of
74.1% — this unit's original twelve are the third-worst giveaway cell in the
key stage, and the top-up brings the whole unit to chance.

This is the unit whose three `<sub>` rows were repaired at the top of this log.
None of the 69 new rows carries a subscript character: C8's formulae are
mentioned rather than examined, so they are written flat, and the three
repaired rows keep their real characters because in those the notation IS the
question.

### Review fixes before commit

Two near-duplicates, both caught by the detector:

- `c8-05-h07` asked what the bromine-on-potassium-bromide tube is for, which is
  `c8-05-h04` word for word in substance. Replaced with a transitivity
  question: chlorine displaces bromine and bromine displaces iodine, so what
  follows about chlorine and iodine without running that tube — which is what
  an order is actually for.
- `c8-07-h07` repeated `c8-07-h02` on aluminium oxide and the rule's boundary.
  Replaced with carbon dioxide: a non-metal oxide that is a gas, and whether
  the rule reaches it.

Nothing else scored above 0.68 in the unit.

Gates at commit: chemistry-only `validate_lesson` clean,
`verify_answer_positions` OK, `verify_answer_lengths` green on `bank/C8`.

---
## C5 — Types of reaction (5 lessons)

**Quota:** 30 needed per band; 31 added, taking every band to **51**. Spread
7 · 6 · 6 · 6 · 6 per band for easier and harder, 6 · 6 · 6 · 6 · 7 for
standard, 93 rows.

| lesson | easier | standard | harder |
|---|---|---|---|
| 01 combustion | e05–e11 | s05–s10 | h05–h11 |
| 02 thermal-decomposition | e05–e10 | s05–s10 | h05–h10 |
| 03 oxidation | e05–e10 | s05–s10 | h05–h10 |
| 04 displacement | e05–e10 | s05–s10 | h05–h10 |
| 05 which-reaction-is-this | e05–e10 | s05–s11 | h05–h10 |

Positions 24 · 24 · 24 · 21. Length tell **28.8%**, against a `BASELINE` of
70.6%.

### Review fixes before commit

Two near-duplicates:

- `c5-01-e08` asked what makes carbon monoxide dangerous in a house, which is
  `c5-01-s03`. Replaced with which gas incomplete combustion produces that
  complete combustion does not — a cleaner recall item that the lesson needed.
- `c5-05-e09` asked which of a list is NOT one of the four types, and the
  answer was neutralisation, which is `c5-05-s02`'s answer to a different
  question. Replaced with synthesis-run-backwards.

**Judged and kept.** The detector also flagged `c5-04-h04` (why copper sulfate
is not stored in steel drums) against the new `c5-04-h08` (what would happen in
a ZINC-lined drum). That is a deliberate pair: the same scenario, a different
metal, and the reasoning has to be done again rather than recalled. A bank of
fifty per band is exactly where a second instance of a skill belongs.

Gates at commit: chemistry-only `validate_lesson` clean,
`verify_answer_positions` OK, `verify_answer_lengths` green on `bank/C5`.

---
## C7 — Energy in reactions (4 lessons)

**Quota:** 34 needed per band; 39 added, taking every band to **51**. Spread
9 · 9 · 13 · 8 per band across four lessons, 117 rows — the largest top-up in
the unit list, because four lessons have to carry what seven carry elsewhere.

| lesson | easier | standard | harder |
|---|---|---|---|
| 01 energy-and-changes-of-state | e05–e13 | s05–s13 | h05–h13 |
| 02 exothermic-reactions | e05–e13 | s05–s13 | h05–h13 |
| 03 endothermic-reactions | e05–e13 | s05–s13 | h05–h13 |
| 04 measuring-a-temperature-change | e05–e12 | s05–s12 | h05–h12 |

Positions 27 · 27 · 27 · 24. Length tell **28.7%**, against a `BASELINE` of
85.7% — C7's original twelve are the second-worst giveaway cell in the key
stage.

### Review fixes before commit — the unit where the failure mode showed its size

**1 · The fast gate caught two EXACT stem repeats.** `c7-03-s08` and
`c7-03-s11` were written word for word as `c7-03-s03` and `c7-03-h03` already
stood. `python3 -m ks3_data.question_bank` names both, with the id they clash
with. That is the check working exactly as designed, and it is the first time
in this run it has fired on my own rows.

**2 · The detector then found TEN more that were not word-for-word.** Nine or
thirteen new rows per band in a four-lesson unit is roughly three times the
density of C3 or C8, and it exhausts a lesson's material: by the ninth standard
row on exothermic reactions there is very little the file does not already ask.

| new row | duplicated |
|---|---|
| `c7-01-s09` | its own new `c7-01-e08` — both on condensing giving energy out |
| `c7-02-e11` | `c7-02-e03` — where the thermometer goes |
| `c7-02-s08` | `c7-02-s04` — why a power station wants an exothermic reaction |
| `c7-02-s09` | `c7-02-s01` — the camping stove and the spark |
| `c7-03-s05` | `c7-03-e04` — where the energy from the cooled beaker went |
| `c7-03-s06` | `c7-03-s04` — why the decomposition stops with the flame |
| `c7-03-s07` | `c7-03-s01` — photosynthesis and respiration as a pair |
| `c7-03-s09` | `c7-03-s02` — the fridge and "making cold" |
| `c7-03-h06` | `c7-03-h02` — conservation of energy in an endothermic change |
| `c7-03-h07` | `c7-03-h04` — photosynthesis as the largest endothermic process |

All ten replaced with material the unit did not have: the energy cost of
melting against warming, the total energy of the universe, doubling both
volumes in a neutralisation, a control beaker beside a cold pack, which
evidence for endothermic is the stronger, the seed-to-tree objection, doubling
the powder, an insulated flask over an hour, and the growing tree against the
burning log.

**The rule this suggests for the units still to come:** a lesson has an
approximate ceiling of about eight or nine genuinely distinct questions per
band on top of its original four. Past that, the next row is a rewording rather
than a new question, and the detector finds it after the fact rather than the
author avoiding it. C9 has the same four-lesson shape and gets the same care.

**3 · A tooling note.** `rebalance` needed EIGHT passes to converge on C7,
against one or two elsewhere. Run it in a loop until it reports zero rather
than a fixed number of times.

Gates at commit: chemistry-only `validate_lesson` clean,
`verify_answer_positions` OK, `verify_answer_lengths` green on `bank/C7`.

---
## C9 — Metals and materials (4 lessons)

**Quota:** 34 needed per band; 36 added, taking every band to **52**. Nine per
lesson per band across all four lessons, 108 rows.

| lesson | easier | standard | harder |
|---|---|---|---|
| 01 the-reactivity-series | e05–e13 | s05–s13 | h05–h13 |
| 02 predicting-displacement | e05–e13 | s05–s13 | h05–h13 |
| 03 getting-metals-out-of-rocks | e05–e13 | s05–s13 | h05–h13 |
| 04 ceramics-polymers-and-composites | e05–e13 | s05–s13 | h05–h13 |

Positions 27 · 27 · 27 · 27. Length tell **22.5%**, against a `BASELINE` of
88.2% — C9's original twelve are the WORST option-length giveaway cell in the
whole key stage, and the top-up brings the unit to chance.

Written with C7's lesson in hand: nine rows per lesson per band is at the
ceiling, and the detector found five near-duplicates rather than C7's twelve.
`c9-01-e05` and `c9-01-e01` shared an answer; `c9-02-e12` was `c9-02-s03` with
lead swapped for copper; `c9-03-e11` repeated `c9-03-s01` on melting malachite;
`c9-04-h11` was `c9-04-h01` word for word in substance; and `c9-03-s07` asked
for the reasoning behind the definition `c9-03-e01` already gives. All five
replaced.

### ⚠️ A SCIENCE ERROR IN AN EXISTING ROW — for Mide, not fixed here

**`c9-04-h02` has its answer the wrong way round, and it is live.**

> Reinforced concrete is used for bridges. What is each of the two materials
> contributing?
> **Marked correct:** "The concrete takes the pull and the steel spreads the
> load across it"

That is backwards. Concrete is strong in compression and weak in tension;
**steel takes the pull** and the concrete holds the bars and spreads the load.

The row contradicts itself: its own distractor 0 ("The steel resists being
squashed and the concrete resists being pulled") is corrected with *"It is the
other way round. Concrete is strong in compression and weak in tension"* —
which states the correct physics while the key states the reverse. The lesson
page is right as well: the ladder's explain rung asks for "steel is strong when
stretched … the steel bars are placed where the bridge is being pulled apart …
the concrete holds the steel in place and spreads the load."

**Not fixed here, deliberately.** `c9-04-h02` sits at `bank_position` 9, inside
the original twelve that this run is required to leave byte-identical, and
correcting a shipped answer is science accuracy — Mide's gate, not a content
lane's. It needs one option's text and one `why` swapped, and it is worth doing
before the next load: any student drawn this row is being marked wrong for the
right answer.

No new row in this unit asks about the load-sharing in reinforced concrete, so
nothing added here stands next to it and contradicts it.

Gates at commit: chemistry-only `validate_lesson` clean,
`verify_answer_positions` OK, `verify_answer_lengths` green on `bank/C9`.

---
## C9 follow-up — a ladder restatement my own runner could not see

`verify_questions` check 6 refuses a bank row whose text restates one of its
lesson's four ladder rungs — `ks3-authoring.md` §10, and the one authoring rule
in the brief that a gate DOES enforce. `c9-03-e08` asked *"Which of these
metals CAN be obtained from its oxide by heating with carbon?"*, which is
C9 lesson 3's recall rung with a different option list.

**Why it survived to the end of the run.** During authoring I checked each unit
with a chemistry-only runner that calls `validate_lesson` — the same function
`python3 -m ks3_data.question_bank` uses. That was written because the full
gate spent most of this run red on another lane's B1 rows, and a red I could
not act on is a red I would learn to ignore. But `validate_lesson` holds checks
on shape, ids, positions and duplicates; **check 6 lives in
`verify_questions.py` and nowhere else**. Nine units went past the narrower
runner and the tenth exposed the gap.

Replaced with a question about why coke is loaded into a blast furnace. The
full gate is now clean: 185 lessons, 5142 questions, all nine checks.

**The rule for the next lane:** a unit-scoped runner is a convenience for
iterating, never the thing you commit against. Run `verify_questions.py` before
every commit even when it is red for somebody else's reasons, and read WHICH
findings are yours.

---
## C10 — Earth and atmosphere (6 lessons)

**Quota:** 26 needed per band; 27 added, taking every band to **51**. Spread
5 · 5 · 5 · 4 · 4 · 4 per band, 81 rows.

| lesson | easier | standard | harder |
|---|---|---|---|
| 01 inside-the-earth | e05–e09 | s05–s09 | h05–h09 |
| 02 three-ways-to-make-a-rock | e05–e09 | s05–s09 | h05–h09 |
| 03 the-rock-cycle | e05–e09 | s05–s09 | h05–h09 |
| 04 a-planet-with-limits | e05–e08 | s05–s08 | h05–h08 |
| 05 whats-in-the-air | e05–e08 | s05–s08 | h05–h08 |
| 06 carbon-dioxide-humans-and-climate | e05–e08 | s05–s08 | h05–h08 |

Positions 21 · 21 · 21 · 18. Length tell **22.0%**, against a `BASELINE` of
85.7% — C10's original twelve are joint second-worst in the key stage.

### Review fixes before commit

Seven near-duplicates, six of them word-for-word repeats of questions the unit
already asks: the phosphate-against-steel comparison, carbon dioxide's 0.04 per
cent, the nitrogen diluting the oxygen, why nitrogen and argon accumulated,
which two actions beat recycling, and the Everest fossils. `c10-02-h09`
repeated `c10-02-s03` with marble swapped for granite. All replaced.

**Note on where these clustered.** Four of the seven are in lessons 4 and 5,
which are the two lessons whose original twelve are the most tightly packed
with named facts — reserves, downcycling, the crisp packet, the composition of
air, banded iron. When a lesson's original rows already cover its named facts
one each, a top-up written from the same notes lands on them again. Reading the
existing stems immediately before writing is what prevents it, and I read L1–L3
that way and L4–L6 less carefully.

Gates at commit: `verify_questions` OK — 185 lessons, 5142 questions, all nine
checks clean; `verify_answer_positions` OK; `verify_answer_lengths` green on
every chemistry scope.

---
## Closing summary — the chemistry lane is complete

**870 new rows across ten units.** Every `(unit, band)` is at or above the
floor of 50.

| unit | lessons | easier | standard | harder | new rows |
|---|---|---|---|---|---|
| C1 | 6 | 52 | 52 | 52 | 84 |
| C2 | 6 | 52 | 52 | 52 | 84 |
| C3 | 7 | 51 | 51 | 51 | 69 |
| C4 | 5 | 51 | 51 | 51 | 93 |
| C5 | 5 | 51 | 51 | 51 | 93 |
| C6 | 7 | 56 | 56 | 56 | 84 |
| C7 | 4 | 51 | 51 | 51 | 117 |
| C8 | 7 | 51 | 51 | 51 | 69 |
| C9 | 4 | 52 | 52 | 52 | 108 |
| C10 | 6 | 51 | 51 | 51 | 81 |

Every row lands at `bank_position` ≥ 12 by construction, so `auto_pool()` sees
exactly what it saw before this run and no weekly assignment changes.

### Gates, at the end

- `python3 verify_questions.py` — **OK, 185 lessons, 5142 questions, all nine
  checks clean** across the whole key stage.
- `python3 verify_answer_positions.py` — healthy in both key stages.
- `python3 verify_answer_lengths.py` — **green on all ten chemistry scopes**,
  every one between 18.9% and 28.8% against a chance rate of 25%. Five of the
  ten carried recorded baselines of 65.4% to 88.2%; all five are now at chance.
  The file still fails overall on sixteen scopes, every one of them a biology
  or physics unit.

### Two things the next lane should take from this

1. **Both answer tells have to be aimed at, not avoided.** Fixing the giveaway
   by lengthening distractors produced its mirror — "the long option is never
   right" — which fails the same gate. The target is chance: make the key the
   longest in about a quarter of the rows.
2. **A near-duplicate is the top-up's characteristic defect, and no gate sees
   it.** `validate_lesson` refuses a repeated string; it cannot refuse a
   repeated QUESTION. Thirty-nine rows across this lane asked something their
   own unit already asked, in different words. The detector is in the lane's
   scratch directory and is thirty lines; it is worth keeping.

### Open for Mide

- **`c9-04-h02` marks the wrong answer correct** — steel and concrete swapped.
  Live, inside the untouchable first twelve, and written up in the C9 section
  above with exactly what needs changing.
