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
