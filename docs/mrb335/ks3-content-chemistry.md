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
