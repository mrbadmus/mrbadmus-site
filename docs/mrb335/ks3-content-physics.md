# MRB-335 — KS3 physics bank top-up (P1–P12)

The physics lane's log. One section per unit, in Rainford's autumn teaching
order (P3, P1, P4, P2, P8, P5, then P6…P12). Every unit here reaches **52 rows
in each of the three bands**, appended at `bank_position` 12 and upwards, so
the twelve rows AUTO composition reads are byte-identical to what they were.

Both gates are run after every unit, from the worktree root:

```bash
python3 -m ks3_data.question_bank
python3 verify_questions.py
```

⚠️ **This worktree has a co-tenant.** A chemistry lane is topping up
`ks3_data/c*/` in the same checkout, so the bank totals printed by the gates
include its rows as well as this lane's, and every commit here is scoped by
hand (`git add ks3_data/p<n>/ docs/mrb335/ks3-content-physics.md`) rather than
with `-A`.

---

## P3 · Describing motion — 3 lessons, 120 new rows (40 per band)

Unit total after the top-up: **52 easier / 52 standard / 52 harder**.

| lesson | easier | standard | harder |
|---|---|---|---|
| 01 speed | e05–e17 (13) | s05–s17 (13) | h05–h17 (13) |
| 02 distance–time graphs | e05–e17 (13) | s05–s17 (13) | h05–h17 (13) |
| 03 relative motion | e05–e18 (14) | s05–s18 (14) | h05–h18 (14) |

**Where the demand sits.** Easier rows are one-step recall — the unit, the
division, reading one point off a line, one relative-speed rule. Standard rows
apply the idea in a context the lesson used: light gates, a river, a walkway, a
graph section. Harder rows are two-step or unfamiliar: a unit conversion plus a
rearrangement (`p3-01-h06`, `p3-03-h09`), an average across legs of different
duration (`p3-01-h05`, `p3-02-h14`), or an explain-why with a number attached
(`p3-02-h13`, `p3-03-h18`).

**Lesson 02 and the no-diagrams rule.** Distance–time graphs are described in
words throughout — "a line runs straight from 10 m at 5 s to 40 m at 15 s" —
never "the graph above". That follows the twelve rows already in the file, and
it is what makes the row readable on the assignment page, away from the lesson.

**Review fixes before commit** (cold re-read of all 120 rows, plus a mechanical
length/markup/spelling/position sweep):

- *Length parity, correct option conspicuously the longest* — `p3-01-s11`,
  `p3-01-s16`, `p3-01-h10`, `p3-01-h13`, `p3-01-h16`, `p3-01-e13`,
  `p3-02-e13`, `p3-02-e14`, `p3-03-h12`. Reworded so no option can be picked
  by length alone; the claims themselves are unchanged.
- *Correct option conspicuously the SHORTEST* — `p3-01-e12` ("0 m/s"),
  `p3-02-e09` ("0 m"), `p3-02-h05` ("4 m/s"), `p3-03-s16`. A bare number
  sitting among three wordy distractors is the same tell in reverse; each was
  given the short reason its distractors already carried.
- *Every calculation re-worked from the stem*, including the distractor
  arithmetic each `why` names — the average-speed legs (h05 in lessons 01 and
  02, `p3-02-h14`), the two river/walkway pairs, the passing-trains 400 m, and
  the 630 km headwind leg. All divide cleanly.
- No duplicate stem or answer set inside a lesson (gated), no ladder rung
  restated (gated), no markup, UK spellings, a unit on every quantity.

Gates after P3: `question_bank` OK, `verify_questions` OK — nine checks clean.

---

## P1 · Energy transfers — 8 lessons, 60 new rows (20 per band)

Unit total: **52 / 52 / 52**. Three per band on lessons 01–04, two per band on
05–08.

| lesson | ids added (each band) |
|---|---|
| 01 energy stores | e05–e07, s05–s07, h05–h07 |
| 02 energy transfers: before and after | e05–e07, s05–s07, h05–h07 |
| 03 conservation of energy | e05–e07, s05–s07, h05–h07 |
| 04 heating and thermal equilibrium | e05–e07, s05–s07, h05–h07 |
| 05 conduction | e05–e06, s05–s06, h05–h06 |
| 06 radiation | e05–e06, s05–s06, h05–h06 |
| 07 insulation | e05–e06, s05–s06, h05–h06 |
| 08 simple machines | e05–e06, s05–s06, h05–h06 |

**The store/pathway discrimination carries the unit**, so it is tested from
several sides rather than once: which of four is a store (`p1-01-e05`), which
item on a child's own list of "kinds of energy" is one (`p1-01-h06`), why
electricity is not (`p1-01-s07`), and a wind-up radio whose whole chain has to
be sorted (`p1-01-s06`).

**`ks3_data/quantities.py` was read and not retyped.** No new row states a
definition of temperature; the two lesson-04 rows that come near it ask instead
what a thermal store depends on besides temperature (`p1-04-e06`) and what
thermal equilibrium is (`p1-04-e05`), so the single owned definition is not
duplicated at a fifth site.

**Review fixes:** thirteen length-parity flags (nine where the correct option
was longest — `p1-02-s07`, `p1-02-h06`, `p1-03-s07`, `p1-03-h05`, `p1-03-h07`,
`p1-04-e05`, `p1-04-s06`, `p1-07-s05`; four where it was conspicuously
shortest — `p1-01-h06`, `p1-03-e06`, `p1-06-e05`, `p1-06-e06`, `p1-08-s06`),
all reworded without changing a claim. One authoring slip caught before the
gate: `p1-05-e06` had been written with a `True if False else False` in a
`correct` field — it evaluated correctly but is not something to leave in a
content file, and it is now a plain `False`. Arithmetic re-worked from the
stems: the 1800 J hairdryer split, the 200 kJ kettle tenth, and all four
machine calculations (`50 N × 2 m`, `150 N × 0.80 m ÷ 600 N`, the 4 m ramp,
the 800 N pulley).

---

## P4 · Forces — 9 lessons, 48 new rows (16 per band)

Unit total: **52 / 52 / 52**. Two per band on lessons 01–07, one per band on
08–09.

| lesson | ids added (each band) |
|---|---|
| 01 what a force is | e05–e06, s05–s06, h05–h06 |
| 02 drawing and adding forces | e05–e06, s05–s06, h05–h06 |
| 03 balanced and unbalanced | e05–e06, s05–s06, h05–h06 |
| 04 what forces do to motion | e05–e06, s05–s06, h05–h06 |
| 05 friction | e05–e06, s05–s06, h05–h06 |
| 06 air and water resistance | e05–e06, s05–s06, h05–h06 |
| 07 moments | e05–e06, s05–s06, h05–h06 |
| 08 springs and Hooke's law | e05, s05, h05 |
| 09 non-contact forces | e05, s05, h05 |

Every weight is worked from `mass × 10 N/kg` and the classic slip — reading the
mass in kilograms as a force in newtons — is a distractor at every band.
Moments carry their unit (N m, never N), and the cm-not-converted error is a
named distractor at `p4-07-s05`.

**Review fixes:** six length flags reworded. One finding that was not about
length: `p4-07-h06` (the wheelbarrow) had a distractor — "the handles are
further from the pivot, so a smaller lift gives a bigger moment" — that is
**true physics**, merely not the answer to the question asked. A distractor a
well-taught student can defend is a defective distractor however carefully the
`why` hedges, so it was replaced with a real misconception ("the wheel carries
the whole weight, so the handles take none of it").

**Two REF flags were reviewed and kept.** `p4-02-e05` and `p4-02-s06` use the
word *diagram* — but in the abstract ("where should an arrow start on a
diagram", "on a scale diagram a 20 N arrow is 4 cm long"), never pointing at
one the child is expected to look at. That is exactly how the twelve rows
already in the file read (`p4-02-e01`, `p4-02-s02`), and both new stems carry
every number they need. The lane's mechanical check was narrowed to deictic
references (*above*, *below*, *shown here*) rather than the bare word.

---

## P2 · Energy at home — 5 lessons, 96 new rows (32 per band)

Unit total: **52 / 52 / 52**. Seven per band on lessons 01–02, six per band on
03–05.

| lesson | ids added (each band) |
|---|---|
| 01 energy in food | e05–e11, s05–s11, h05–h11 |
| 02 power ratings in watts | e05–e11, s05–s11, h05–h11 |
| 03 calculating energy transferred | e05–e10, s05–s10, h05–h10 |
| 04 reading a fuel bill | e05–e10, s05–s10, h05–h10 |
| 05 fuels and energy resources | e05–e10, s05–s10, h05–h10 |

This is the unit where the arithmetic does the teaching, so every calculation
divides cleanly and each distractor is a **named** working error rather than a
near miss: the time left in minutes (`p2-03-s05`, `p2-03-h07`), the kilo
dropped or added twice (`p2-03-h05`, `p2-04-s10`), the division inverted, and
the order-of-magnitude check that catches all of them (`p2-03-s07`). The
rate-versus-total confusion that the unit exists to fix is tested from both
ends — a 5 W charger beating a 1200 W toaster over the day (`p2-02-s05`), and
two heaters of different ratings warming the same room to the same temperature
for the same energy (`p2-02-h05`, `p2-02-h07`).

**Review fixes.** Two duplicate stems were caught by the gate and rewritten
rather than nudged: `p2-02-h07` had reproduced the existing `h03` ("when does a
lower wattage genuinely save energy") and became the two-heaters comparison;
`p2-05-h06` had reproduced `h02` (the all-wind-and-solar objection) and became
a grid battery, which asks the same physics of intermittency from the solution
end instead. Both were visible in the stem list before writing and were
authored anyway — the fast gate is what caught them, which is the argument for
running it per lesson rather than per unit.

Two more distractor sets were rewritten on the cold read, not for length but
because they were **incoherent as written**: `p2-03-h06` had an option reading
"the lamp, at 3.6 MJ against the kettle's 3.6 MJ", which states a difference
and an equality in one line, and `p2-03-h08` had a `why` that contradicted its
own option. Both now carry the two symmetric errors (rating-wins and
time-wins) instead. Five length flags fixed, and one authoring slip of the same
shape as P1's: a `True if 0 else False` in a `correct` field, removed before
the append.

**The lane's length checker was corrected twice during this unit.** It had been
counting "18 000 J" as three words, so every large numeric answer looked
conspicuously long; it now collapses a thousands space before counting. It had
also been flagging the bare word *opposite* — `p2-05-h05` says wood and nuclear
sit in "opposite corners of the grid", which is a description, not a
page reference — so it now looks for deictic phrases only.

---

## ⚠️ A gate defect that is NOT content, found while topping up P1

From the moment the biology lane's B1 top-up landed in this worktree,
`python3 verify_questions.py` reports **two check-8 findings**:

```
[check 8] compose_assignment/nearest-first
[check 8] compose_assignment/thin-week
```

**`compose_assignment` is not the problem — it is correct.** It draws through
`auto_pool()`, so it still takes exactly four standard rows from a lesson that
now holds eight, and RISKS D7 holds: a topped-up lesson composes the identical
assignment it composed before. Measured, read-only:

```
B1 lesson 6 standard rows in the file : 8
B1 lesson 6 standard rows auto can see: 4
cap obeyed by compose_assignment      : True
```

**The check's EXPECTATION is what is uncapped.** In
`verify_questions.py::_check_composition`, the two comparisons build their
expected lists from the whole lesson:

```python
own     = [q["id"] for q in bank.get(keys[5], []) if q.get("band") == "standard"]
nearest = [q["id"] for q in bank.get(keys[4], []) if q.get("band") == "standard"]
```

so they expect eight ids where composition can only ever reach four. Re-running
the same two assertions with `qb.auto_pool(...)` wrapped round each expectation
makes both pass:

```
thin-week     (capped expectation): True
nearest-first (capped expectation): True
```

**Why it matters to every lane, not just biology.** B1 is check 8's fixture
unit. The check therefore goes red on the FIRST unit any lane tops up in B1 and
stays red for everyone in the worktree afterwards — including runs whose own
content is perfectly clean. It is the gate measuring the pre-MRB-335 world.

**The fix is two lines**, wrapping each expectation in `qb.auto_pool(...)`. It
is in `verify_questions.py`, which this lane may not edit (scope is
`ks3_data/p*/questions_*.py` plus this file), so it is reported rather than
made. **It must not be "fixed" by relaxing the assertion** — the property it
tests is real and is exactly what protects existing assignments.

**How this lane stayed honest in the meantime.** Every unit from P1 onwards is
gated with a wrapper that fails on any finding that is not that named B1
check-8 pair, so a physics defect cannot hide behind the known red. The fast
gate `python3 -m ks3_data.question_bank` — which runs `validate_lesson` over
every physics lesson, the ids, the positions, the duplicate stems and the
markup rule — stays **OK, unconditionally**, after every unit below.
