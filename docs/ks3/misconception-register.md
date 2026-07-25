# KS3 misconception register

**Status: empty by design.** Created in Phase 0 (`docs/ks3/architecture.md` §10.1) ready to fill
during authoring. Entries are added as lessons are written, never invented ahead of the lesson that
needs them.

Unlike `statutory-register.md`, this file is **hand-maintained**. There is no generator, because
entries come from authoring judgement and examiner review, not from a source document.

---

## What this file is for

Architecture.md §5.3 makes misconceptions **structured data, cross-referenced across the whole key
stage** rather than prose asides in individual lessons.

Three things a register buys that per-lesson prose cannot:

1. **A later lesson can name the repeat.** "This is the same wrong idea you met in Year 7" is only
   possible if the earlier occurrence has an ID.
2. **We can check we are actually killing misconceptions** rather than dodging the same one in twelve
   places.
3. **The AI tutor gets something precise to work with** — §5.9 passes the lesson's misconceptions
   into the KS3 system prompt so the tutor recognises and corrects a wrong belief instead of
   validating it.

Law 3 (§5.0) makes this load-bearing: every lesson names its target misconception(s), and **at least
one activity must confront one head-on** — eliciting it, making its wrongness visible, and replacing
it. A lesson with an empty `misconceptions` list must justify itself at review, and §5.3 notes that
almost none legitimately can.

---

## Entry format

Per §5.3, an entry is:

```python
{"id": "PART-03",
 "statement": "The particles themselves get bigger when a substance is heated.",
 "elicited_by": "predict-expansion",     # the activity that surfaces it
 "confronted_by": "expansion-lab",       # the activity that kills it
 "reappears_in": ["thermal-expansion", "gas-pressure", "density"]}
```

| Field | Meaning |
|---|---|
| `id` | `<FAMILY>-<nn>`, permanent once assigned. See the family prefixes below. |
| `statement` | The wrong belief, written **as a student would hold it** — a plain assertion, not a description of an error. |
| `elicited_by` | Slug of the activity that surfaces it. A misconception the student never commits to stays invisible to its owner (Law 4). |
| `confronted_by` | Slug of the activity that kills it. Required for at least one misconception per lesson (Law 3). |
| `reappears_in` | Lesson slugs where the same wrong idea resurfaces. This is the cross-referencing the register exists for. |

`statement` is a **science-bearing field** under §5.10 — it requires Mide's examiner review before
publish, and is frozen afterwards.

---

## ID family prefixes

Assign as needed during authoring; add a row here when a new family is opened. Families are
conceptual, not disciplinary — the same wrong idea crosses subject boundaries, which is the point.

| Prefix | Domain | Opened |
|---|---|---|
| _(none yet)_ | | |

Suggested starting families, from the misconception fields architecture.md §1 and §9 name explicitly
— **not yet opened, listed so numbering starts consistently**: `PART` (particles and states),
`FORCE` (forces and motion), `ENERGY` (energy and temperature), `PLANT` (plant nutrition and
photosynthesis), `CIRC` (current and circuits).

---

## Entries

_None yet._

Add entries below, grouped by family, as lessons are authored. Every distractor in every ladder
question and quiz should map to an entry here or be a non-diagnostic distractor by explicit choice
(§5.3).

---

## Review question

§10.3 adds one question to every KS3 lesson review:

> *"Which wrong idea does this lesson kill, and would a student holding that idea be forced to
> notice?"*

If the answer is no, the lesson is not finished, however attractive it looks. This register is the
record of the answers.
