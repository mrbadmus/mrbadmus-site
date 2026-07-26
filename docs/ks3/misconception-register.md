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
| `PART` | Particles, states and the particle model | 2026-07-26, by C1 (Phase 1 slice) |

Suggested starting families, from the misconception fields architecture.md §1 and §9 name explicitly
— **not yet opened, listed so numbering starts consistently**: `PART` (particles and states),
`FORCE` (forces and motion), `ENERGY` (energy and temperature), `PLANT` (plant nutrition and
photosynthesis), `CIRC` (current and circuits).

---

## Entries

Add entries below, grouped by family, as lessons are authored. Every distractor in every ladder
question and quiz should map to an entry here or be a non-diagnostic distractor by explicit choice
(§5.3).

### `PART` — particles, states and the particle model

Opened by **C1 *Particles and their behaviour*** (Phase 1 slice, 2026-07-26). All thirteen are
`review_state: draft` — the `statement` field is science-bearing (§5.10) and needs Mide's review
before any of these freeze.

| ID | Statement (as a student holds it) | Elicited by | Confronted by | Lesson |
|---|---|---|---|---|
| `PART-01` | Matter is continuous — you could keep cutting something in half forever and never reach a smallest piece. | `keep-cutting` | `mixing-volumes` | `particle-model` |
| `PART-02` | There is air (or dust, or something) in the gaps between particles. | `what-is-in-the-gap` | `gap-reveal` | `particle-model` |
| `PART-03` | The particles themselves change — they melt, or get softer, or expand — when a substance changes state. | `what-changed` | `same-particles-reveal` | `solids-liquids-and-gases` |
| `PART-04` | Particles in a solid are completely still. | `predict-solid-motion` | `vibration-sim` | `solids-liquids-and-gases` |
| `PART-05` | When a substance melts or evaporates, some of it is lost or destroyed. | `predict-mass` | `sealed-bag-weigh` | `changes-of-state` |
| `PART-06` | Melting and dissolving are the same thing. | `sort-melting-dissolving` | `two-routes-compare` | `changes-of-state` |
| `PART-07` | Bubbles in boiling water are made of air, or of nothing. | `what-is-in-the-bubble` | `bubble-reveal` | `changes-of-state` |
| `PART-08` | Gas pressure is the particles pushing against each other. | `what-causes-pressure` | `collision-count-sim` | `gas-pressure` |
| `PART-09` | Heating a gas makes the particles themselves get bigger, which is why the pressure rises. | `predict-heated-can` | `speed-not-size` | `gas-pressure` |
| `PART-10` | Diffusion needs a draught, a current, or someone to waft it — something has to push the particles along. | `predict-still-room` | `random-walk-sim` | `diffusion` |
| `PART-11` | Particles move in order to spread out — they 'want' to fill the space. | `why-spread` | `both-directions-sim` | `diffusion` |
| `PART-12` | A scientific model is either true or false, and one exception proves it wrong. | `verdict-vote` | `model-limits-sort` | `testing-the-model` |
| `PART-13` | Scientists' models never change once they are agreed. | `predict-history` | `model-history-timeline` | `testing-the-model` |

**Where these are expected to resurface** (`reappears_in`, filled as the units are authored):

- `PART-03` (particles change size/state) → P11 `temperature-and-internal-energy`, P1
  `heating-and-thermal-equilibrium`, C7 `energy-and-changes-of-state`. This is the single most
  persistent wrong idea in KS3 physical science and it should be re-confronted, not just re-stated.
- `PART-05` (matter is destroyed) → C4 `mass-in-a-reaction`, C2 `conservation-of-mass`. It changes
  costume from "the puddle dried up" to "the mass went down when it burned"; it is the same belief.
- `PART-09` (heating makes particles bigger) → P5 `pressure-in-liquids`, P11 `density`.
- `PART-10`/`PART-11` (diffusion needs a push / particles intend to spread) → B1 `animal-and-plant-cells`
  and B4 `alveoli-built-for-exchange`, where diffusion does real biological work.
- `PART-12`/`PART-13` (how models and theories work) → C2 `the-atom-daltons-model`, C8 `mendeleev`,
  B10 `how-we-worked-out-dna`. These are the nature-of-science pair and they recur in every
  INVESTIGATION lesson.

⚑ **For Mide's review.** `PART-12` and `PART-13` are not misconceptions about *particles* — they are
about how science works. They sit under `PART` because C1 opened them, which is arguably the wrong
home. A separate `NOS` (nature of science) family may be the better call before B10 and C8 are
authored. Flagged rather than decided, because renaming an ID after it is referenced is exactly what
§5.3 says must not happen.

---

## Review question

§10.3 adds one question to every KS3 lesson review:

> *"Which wrong idea does this lesson kill, and would a student holding that idea be forced to
> notice?"*

If the answer is no, the lesson is not finished, however attractive it looks. This register is the
record of the answers.
