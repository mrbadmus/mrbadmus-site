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
