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

`NOS` (nature of science — how models, evidence and theories actually work) is a **candidate family,
not yet opened**. The call belongs before `B10 how-we-worked-out-dna` and `C8 mendeleev` are
authored; see the ruling under the `PART` entries below. Note that opening it would not move
`PART-12`/`PART-13` — IDs are permanent.

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
| `PART-01` | Matter is continuous — you could keep cutting something in half forever and never reach a smallest piece. | `mixing-volumes` | `keep-cutting` | `particle-model` |
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

### `PART-12` / `PART-13` — RULED: stay as they are; a `NOS` family may be wanted later

**Decision, 26 Jul 2026 — `PART-12` and `PART-13` keep their IDs permanently. They are not renamed,
not renumbered, and not moved.** IDs are permanent once assigned (§5.3, and the `id` row in the entry
format above); an ID that has been referenced anywhere cannot be reissued, and these two are already
referenced by `testing-the-model`'s authored activities. Renaming to tidy a taxonomy is precisely the
failure §5.3 exists to prevent — it breaks the join silently, with no error anywhere.

The observation behind the flag stands and is worth recording: neither one is a misconception about
*particles*. `PART-12` ("a model is either true or false") and `PART-13` ("scientists' models never
change") are misconceptions about **how science works** — nature of science, not matter. They sit
under `PART` only because C1 was the unit that opened the register, which is an accident of build
order rather than a conceptual claim.

**What this means for future authoring, not for these two entries:**

- A separate **`NOS` (nature of science) family may be wanted**, and the moment to decide is **before
  `B10 how-we-worked-out-dna` and `C8 mendeleev` are authored** — those are the next two lessons
  whose central wrong ideas are nature-of-science ones, and they are where a `NOS` family would
  either earn its place or prove unnecessary. Deciding then costs nothing; deciding after they are
  authored means either a third home for the same idea or a rename that §5.3 forbids.
- If `NOS` is opened, `PART-12` and `PART-13` **still do not move**. They stay where they are, and
  the register carries a cross-reference instead. A family boundary that is slightly wrong is a much
  smaller problem than an ID that means two different things depending on when you read it.
- Until that call is made, nature-of-science misconceptions discovered while authoring should be
  noted here rather than assigned an ID, so nothing is minted into the wrong family in the meantime.

This is recorded as a decision rather than a question so the next author does not re-open it.

---

## Review question

§10.3 adds one question to every KS3 lesson review:

> *"Which wrong idea does this lesson kill, and would a student holding that idea be forced to
> notice?"*

If the answer is no, the lesson is not finished, however attractive it looks. This register is the
record of the answers.
