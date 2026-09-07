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
