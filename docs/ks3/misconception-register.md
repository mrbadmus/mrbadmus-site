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

### ⊕ MRB-244 — `confronted_by` must name a place on its OWN page, and this is now gated

`confronted_by` is a claim about where a student is standing when a wrong idea is taken apart, so
it has to be true **on the page the student is on**. It may name an activity id from that lesson's
`activities[]`, or a block `anchor` that lesson declares. It may **never** name a lesson slug, an
element on another page, or a place that exists only in the author's description of the page.

B6 surfaced the shape of it: `b6-02`'s first cut named a lesson slug, because that page's big
question *is* `b6-01`'s belief and pointing back at `b6-01` felt like the honest thing. It is not —
a cross-page pointer is one no page can resolve, and it reads as working precisely because nothing
checked it. Asking the question of all thirty values found two more that had drifted the same way,
`BODY-06` and `ATOM-02`, both naming a real place in the author's head and no element in the
document.

`verify_ks3.py` now resolves every value against the **built page**, so a name that renders to
nothing cannot satisfy it: a value counts only where it is emitted as `id="…"` or
`data-activity="…"`. Note the two keys are not interchangeable in authored data — `id` on a block
names the **activity** it renders, `anchor` names the **section**; `ATOM-02` failed because a
section name had been authored on the activity key and was therefore emitted nowhere.

### ⊕ MRB-248 — `elicited_by` is gated by the same rule, with one difference

`elicited_by` carries the identical defect and was never checked when `confronted_by` was fixed:
the ticket said `confronted_by`, and the sibling key on the same dict line went past three audits
untouched. It now resolves against the same universe of names on the same built page.

**The difference, and it is deliberate: absence is LEGAL for `elicited_by` and is not legal for
`confronted_by`.** Law 3 requires a wrong idea to be taken apart somewhere the student is standing,
so a missing `confronted_by` is itself the failure. Eliciting is a different claim. This register
already documents pages where a belief is stated in static markup with nothing in front of it
asking the student to commit — `CELL-13`'s row carries `—` and the note under it calls that honest
rather than an omission, and `CELL-08` has the same shape. Recording the gap is the right answer
there, and a gate that demanded a value would be a gate that made an author invent one. So: absent
or empty passes; a value that is **present** must be true.

The gate reports both counts separately, so a reader can see that both keys were measured and how
many of each declared a value.

**And the standing rule this sits under: CITE, DO NOT RE-DECLARE.** A `misconceptions` row is not a
citation. A borrowed id is re-declared only where the page genuinely **re-confronts** the belief
with an activity of its own — the `CELL-08` precedent. Opening on a belief and moving on is a
*reappearance*, and reappearances live in `reappears_in`, here, not in a second declaration.

---

## ID family prefixes

Assign as needed during authoring; add a row here when a new family is opened. Families are
conceptual, not disciplinary — the same wrong idea crosses subject boundaries, which is the point.

| Prefix | Domain | Opened |
|---|---|---|
| `PART` | Particles, states and the particle model | 2026-07-26, by C1 (Phase 1 slice) |
| `LIFE` | What counts as living, and the life processes | 2026-08-09, by B1 |
| `CELL` | Cells, microscopy and the organisation of living things | 2026-08-09, by B1 |
| `BODY` | Body systems, and how they do mechanical work | 2026-08-16, by B2 |
| `ATOM` | Atoms having kinds, and substances versus their ingredients | 2026-08-16, by B2's sibling delivery, C2 |
| `DIET` | Food, what a body needs from it, and what the gut does to it | 2026-08-16, by B3 |
| `PLANT` | Plant nutrition, photosynthesis, and what a leaf is for | 2026-08-17, by B7 |
| `RESP` | Respiration: what it is, where it happens, and what it is not | 2026-08-18, by B8 |
| `ECO` | Ecosystems, feeding relationships and interdependence | 2026-08-18, by B9 |
| `NOS` | Nature of science — how models, evidence and theories actually work | 2026-08-17, by MRB-248 (commander's ruling), populated by re-homing from `PART` and `DRUG` |

Suggested starting families, from the misconception fields architecture.md §1 and §9 name explicitly
— **not yet opened, listed so numbering starts consistently**: `FORCE` (forces and motion),
`ENERGY` (energy and temperature), `CIRC` (current and circuits).

⊕ **`PLANT` opened 17 Aug 2026 by B7** (MRB-245), and `PART` was opened earlier by C1 — both have
been removed from the not-yet-opened list above rather than left there to contradict the entries
below. `PLANT` is added to the prefix table.

⊕ **`NOS` OPENED 17 Aug 2026 (MRB-248), and the ids in it MOVED.** This paragraph used to read
*"`NOS` … is a candidate family, not yet opened … opening it would not move `PART-12`/`PART-13` —
IDs are permanent."* The commander has ruled the other way, on the deadline the 26 Jul 2026 entry
itself set: the call was to be made before `B10 how-we-worked-out-dna` and `C8 mendeleev` were
authored, B10 is now imminent, and the family is opened **with** the three entries that belong in
it rather than alongside them. See `NOS` below for the re-homes, the reservations and the gaps.

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

⊕ **`PART-12` and `PART-13` are gone from this table and are PERMANENT GAPS.** They were re-homed
to `NOS-01` and `NOS-02` on 17 Aug 2026 by MRB-248; their rows now live in the `NOS` section below,
with the same statements and the same lesson. **Never reissue `PART-12` or `PART-13`** — a number
that has meant one thing and is later given to another is exactly the silent broken join §5.3
exists to prevent, and the fact that these two moved does not make the numbers free.

**Where these are expected to resurface** (`reappears_in`, filled as the units are authored):

- `PART-03` (particles change size/state) → P11 `temperature-and-internal-energy`, P1
  `heating-and-thermal-equilibrium`, C7 `energy-and-changes-of-state`. This is the single most
  persistent wrong idea in KS3 physical science and it should be re-confronted, not just re-stated.
- `PART-05` (matter is destroyed) → C4 `mass-in-a-reaction`, C2 `conservation-of-mass`. It changes
  costume from "the puddle dried up" to "the mass went down when it burned"; it is the same belief.
- `PART-09` (heating makes particles bigger) → P5 `pressure-in-liquids`, P11 `density`.
- `PART-10`/`PART-11` (diffusion needs a push / particles intend to spread) → B1 `specialised-cells`
  and B4 `alveoli-built-for-exchange`, where diffusion does real biological work.
- The nature-of-science pair that used to sit at `PART-12`/`PART-13` is now `NOS-01`/`NOS-02`, and
  its reappearances are listed in the `NOS` section below.

### ⊖ `PART-12` / `PART-13` — the 26 Jul 2026 ruling, REVERSED 17 Aug 2026 (MRB-248)

**This section is kept, marked, rather than deleted, per the reversal rule.** It ruled that
`PART-12` and `PART-13` keep their IDs permanently — not renamed, not renumbered, not moved — on
the ground that an ID once referenced cannot be reissued, and that renaming to tidy a taxonomy is
the failure §5.3 exists to prevent.

**What it got right, and what the reversal keeps.** The reasoning about reissue is correct and is
not weakened by the reversal: `PART-12` and `PART-13` are **permanent gaps** and will never be
given to anything else. What the ruling conflated is two different operations. *Reissuing* a number
— giving `PART-12` to a new belief — silently breaks a join. *Re-homing* a belief — moving one
statement from `PART-12` to `NOS-01` and never reusing `PART-12` — breaks nothing silently, because
every reference to the old number is updated in the same change and any that is missed is a name
that resolves to nothing. The register did not distinguish them, so the safe half of the rule was
applied to the whole.

**What it got right and the reversal acts on.** Its own observation stands, and is now the reason
it was reversed: neither belief is about *particles*. They sat under `PART` because C1 opened the
register — an accident of build order, not a conceptual claim. The ruling set the decision point at
*"before `B10 how-we-worked-out-dna` and `C8 mendeleev` are authored"*, and named the cost of
deciding late: **either a third home for the same idea or a rename**. B10 is now imminent. The
commander took the deadline the ruling set, and chose the rename while the count was three rather
than a third home for the same idea.

The re-homes and the gaps are recorded in the `NOS` section below. Nothing else in `PART` moves.

### `LIFE` — what counts as living

Opened by **B1 *Cells and organisation*** (2026-08-09, authored by Claude Design). All three are
`review_state: draft` — the `statement` field is science-bearing (§5.10) and needs Mide's review
before any of these freeze.

| ID | Statement (as a student holds it) | Elicited by | Confronted by | Lesson |
|---|---|---|---|---|
| `LIFE-01` | If something moves on its own it must be alive, and if it never moves it must not be. | `three-dishes-vote` | `seed-or-crystal` | `life-processes` |
| `LIFE-02` | Doing one of the life processes is enough to count as alive — if it grows on its own, it is alive. | `crystal-check` | `seven-out-of-seven` | `life-processes` |
| `LIFE-03` | A single cell cannot be a whole living thing — it must be part of something bigger. | `how-many-processes` | `one-cell-does-all-seven` | `unicellular-organisms` |

### `CELL` — cells, microscopy and organisation

Opened by **B1 *Cells and organisation*** (2026-08-09, authored by Claude Design). All twelve are
`review_state: draft`, as above.

| ID | Statement (as a student holds it) | Elicited by | Confronted by | Lesson |
|---|---|---|---|---|
| `CELL-01` | Those neat round circles in the field of view are the cells. | `count-the-cells` | `bubble-or-cell` | `using-a-microscope` |
| `CELL-02` | The highest magnification is always the best one to use, because it shows you the most. | `pick-a-lens` | `microscope-lab` | `using-a-microscope` |
| `CELL-03` | Every plant cell is green, because plants are green. | `plant-extras` | `not-all-green` | `animal-and-plant-cells` |
| `CELL-04` | The cell membrane and the cell wall are the same thing — animal cells have a wall, it is just called a membrane. | `whats-holding-it-up` | `wall-or-membrane` | `animal-and-plant-cells` |
| `CELL-05` | Every cell in your body has a nucleus. | `which-has-no-nucleus` | `no-nucleus-reveal` | `specialised-cells` |
| `CELL-06` | The levels are just about size: small things are cells, medium things are tissues and big things are organs. | `size-trap` | `not-about-size` | `levels-of-organisation` |
| `CELL-07` | Blood is not a tissue, because a tissue is solid and blood is a liquid. | `blood-check` | `blood-is-a-tissue` | `levels-of-organisation` |
| `CELL-08` | A single-celled organism is just a simpler version of one of our cells — the same parts, doing less. | `same-or-extra` | `more-not-fewer` | `unicellular-organisms` |
| `CELL-09` | A stem cell is a cell from the stem of a plant. | `where-does-the-word-come-from` | `stem-not-stem` | `stem-cells-and-meristems` |
| `CELL-10` | A specialised cell can change into a different kind whenever the body needs it — a skin cell can become a nerve cell. | `where-from` | `once-you-choose` | `stem-cells-and-meristems` |
| `CELL-11` | The enzymes were killed by the heat. | `what-did-boiling-do` | `not-killed-changed` | `enzymes-and-rate` |
| `CELL-12` | The hotter it is the faster any reaction goes, so an enzyme works best as hot as possible. | `predict-the-curve` | `two-halves-of-the-curve` | `enzymes-and-rate` |
| `CELL-13` | No nucleus means no instructions — so a bacterium cannot divide. | — (see below) | `s-think` | `unicellular-organisms` |

⊕ **`CELL-13` registered 2026-08-16 (MRB-220), closing a dead join.** The ID was authored and
referenced in `ks3_data/b1/lesson_06_unicellular_organisms.py` — with a full `statement` and a
`pairs_with` edge back to `specialised-cells` — but never given a row here, and that module's own
comment asked for it. A lesson naming an ID the register does not define is the same defect as an
ID with no lesson, read from the other end: the join is silently broken and nothing fails.

Its `elicited_by` is empty and that is **honest, not an omission**. On Design's approved page both
of `#s-think`'s misconceptions are static markup with no gate and no eliciting activity, so Law 3's
elicit-then-confront is discharged for `LIFE-03` by the settles-it activity and for this pair by
nothing at all. Recorded as a gap rather than papered over. `CELL-08` has the same shape.

**Where these are expected to resurface** (`reappears_in`, for filling as later units are
authored):

- `CELL-04` (wall/membrane) → B7 `leaves-built-for-the-job`, and again at KS4.
- `CELL-05` (every cell has a nucleus) → B10 `chromosomes-genes-and-dna`, where it does real
  damage.
- `CELL-06`/`CELL-07` (levels) → B3 `the-digestive-system`, B4 `the-gas-exchange-system`, B9
  `food-chains-and-food-webs`. Every SYSTEM lesson in Biology re-tests this pair.
- `CELL-11` (killed, not denatured) → B3 `enzymes-in-digestion`, C6 `catalysts`. It is a *wording*
  habit, and wording habits are killed early or not at all.

**Cross-family note.** B1 `specialised-cells` re-confronts `PART-10` (see the `PART` reappears
list above) with its own pair — `how-does-oxygen-get-in` and `membrane-diffusion-lab` — because a
register row records where an idea was *opened*, not everywhere it is fought. `PART-10`'s own row
keeps its C1 `elicited_by`/`confronted_by`.

### `BODY` — body systems, and how they do mechanical work

Opened by **B2 *Movement: skeleton and muscles*** (2026-08-16, authored by Claude Design, MRB-220).
All eleven are `review_state: draft` — the `statement` field is science-bearing (§5.10) and needs
Mide's review before any of these freeze.

`CELL` is about cells. These are about **body systems and how they do work**, which is why they are
a family rather than `CELL-13` onwards. Design requested a ruling on the family before any ID was
referenced; the family is opened here, and the IDs below are now permanent (§5.3).

| ID | Statement (as a student holds it) | Elicited by | Confronted by | Lesson |
|---|---|---|---|---|
| `BODY-01` | Bones are dead — they are the hard leftovers, like a tent frame. | `think-commit-alive` | `think-reveal-alive` | `what-the-skeleton-does` |
| `BODY-02` | The skeleton's job is holding you up; the other things bones do are extras. | `hook-two-breaks` | `switch-off-chains` | `what-the-skeleton-does` |
| `BODY-03` | How bad a break is depends on how big the bone is. | `hook-two-breaks` | `hook-reveal` | `what-the-skeleton-does` |
| `BODY-04` | Muscles hold the bones together at a joint. | `think-commit-achilles` | `think-reveal-achilles` | `joints` |
| `BODY-05` | All joints work the same way; some are just stiffer than others. | `bench-gate-knee-shoulder` | `joint-bench` | `joints` |
| `BODY-06` | A joint could rotate further if the muscles were stronger or the ligaments looser. | `s-ladder` | `s-ladder` | `joints` |
| `BODY-07` | Muscles push as well as pull. | `hook-commit-door` | `muscle-pair` | `antagonistic-muscle-pairs` |
| `BODY-08` | When a muscle relaxes it stretches itself back out. | `think-commit-stretch` | `think-reveal-stretch` | `antagonistic-muscle-pairs` |
| `BODY-09` | If both muscles of a pair contract, the movement is faster or stronger. | `bench-gate-both` | `muscle-pair-both` | `antagonistic-muscle-pairs` |
| `BODY-10` | A muscle pulls with the same force as the weight it is holding. | `hook-commit-bag` | `arm-lever-rig` | `biomechanics-forces-in-the-body` |
| `BODY-11` | Levers always make things easier, so the body's levers reduce the force needed. | `think-commit-lever` | `think-reveal-lever` | `biomechanics-forces-in-the-body` |

**Where these are expected to resurface** (`reappears_in`, filled as the units are authored):

- `BODY-01` (organs are just plumbing) → B3 `the-digestive-system` and B9. The same instinct, a
  different organ.
- `BODY-07` (muscles push) → P4's coming "forces are things objects have". It is the biology face
  of one wrong idea about force, and the two should be fought as one.
- `BODY-10`/`BODY-11` (levers make things easier) → P4 `moments` and P1 `simple-machines`, where
  the force-for-distance trade is the whole lesson. That is the natural place to say *this is the
  arm again*.

### `ATOM` — atoms having kinds, and substances versus their ingredients

Opened by **C2 *Atoms, elements and compounds*** (2026-08-16, authored by Claude Design, MRB-220).
All eleven are `review_state: draft`, as above.

`PART` is particles and states, opened by C1. These are about **atoms having kinds**, and about a
substance not keeping the properties of what went into it. Design requested a ruling on the family
before the IDs were referenced; it is opened here and the IDs are permanent.

| ID | Statement (as a student holds it) | Elicited by | Confronted by | Lesson |
|---|---|---|---|---|
| `ATOM-01` | An atom of a substance has the properties of the substance — a copper atom is orange and conducts. | `think-commit-copper` | `think-reveal-copper` | `the-atom-daltons-model` |
| `ATOM-02` | A model that turns out to be wrong about something has been disproved and should be discarded. | `s-ladder` | `stretch-boundary` | `the-atom-daltons-model` |
| `ATOM-03` | If it looks like a metal, it is an element. | `think-commit-brass` | `think-reveal-brass` | `elements` |
| `ATOM-04` | An element is a pure substance, so anything pure is an element. | `sample-water` | `sample-reveal` | `elements` |
| `ATOM-05` | Reacting violently means being broken down. | `sample-sodium` | `sample-reveal` | `elements` |
| `ATOM-06` | A compound is a very thoroughly mixed mixture. | `bench-gate-proportions` | `weigh-what-combines` | `compounds` |
| `ATOM-07` | The elements are still in there behaving as themselves, so the compound keeps their properties. | `think-commit-magnet` | `think-reveal-magnet` | `compounds` |
| `ATOM-08` | A symbol is the English name shortened, so any sensible abbreviation will do. | `think-commit-co` | `think-reveal-co` | `chemical-symbols` |
| `ATOM-09` | The small number in a formula changes how much of the substance there is. | `builder-gate` | `formula-builder` | `formulae` |
| `ATOM-10` | 2H₂O and H₂O₂ are the same thing written two ways. | `think-commit-big-small` | `think-reveal-big-small` | `formulae` |
| `ATOM-11` | Burning destroys matter — the mass turns into heat and light. | `think-commit-burning` | `sealed-flask-run` | `conservation-of-mass` |

**Where these are expected to resurface:**

- `ATOM-01` (an atom is a tiny lump of the substance) is the big one → C4
  `reactions-rearrange-atoms`, C8 `metals-and-non-metals`, P11 `density`, and every bonding lesson
  at KS4.
- `ATOM-02` belongs with `NOS-01`/`NOS-02` and was **the third piece of evidence that a `NOS`
  family was wanted**. The call has since been made — see `NOS` below — and `ATOM-02` was **not**
  re-homed with them: unlike the three that moved, it is load-bearing on a page whose whole subject
  is a specific model's boundary, and the commander's re-home list named three ids and only three.
  It stays in `ATOM` and is cross-referenced from `NOS`. If a later pass wants it moved, that is a
  fresh ruling, not a tidy-up.

  ⊕ **MRB-248 also corrected its `elicited_by`.** It read `ladder-r2` — the author's name for the
  apply rung, which is emitted inside the ladder's section and carries no id of its own. The rung
  is genuinely where the belief is committed to (all three of its distractors are versions of it),
  so only the name was wrong; it now reads `s-ladder`, which is what the page emits. Identical
  shape to `BODY-06` under MRB-244, one key across.

**Cross-family note — `ATOM-11` is `PART-05` in a chemical costume.** Exactly as the `PART` list
predicted when it wrote that *"the puddle dried up"* becomes *"the mass went down when it burned"*.
It is minted as its own ID because the confrontation is a different one — a sealed flask, not a
sealed bag — but it is the same belief, and `PART-05`'s row is where the idea was opened.
`c2-06 conservation-of-mass` may not be dropped on the grounds that C1 covers it, and `c1-03`'s
sealed-bag confrontation may not be dropped on the grounds that C2 covers it.

---

## Review question

§10.3 adds one question to every KS3 lesson review:

> *"Which wrong idea does this lesson kill, and would a student holding that idea be forced to
> notice?"*

If the answer is no, the lesson is not finished, however attractive it looks. This register is the
record of the answers.


### `DIET` — food, what a body needs from it, and what the gut does to it

Opened 16 Aug 2026 by B3 (MRB-228). Seventeen entries across eight lessons — the
largest family in the register, because nutrition is where a student arrives with
the most already believed. Almost none of it comes from a previous lesson; it
comes from packaging, from adults, and from years of being told which foods are
good ones.

⚠️ **`DIET-06`/`07` and `DIET-08`/`09` were nearly the same two numbers.** Three
authors worked this unit in parallel and two of them independently minted
`DIET-06` and `DIET-07`, for four different beliefs. Nothing had been registered
yet, so the family was renumbered into teaching order before any id became
permanent — which is the only window in which renumbering is allowed at all.
Recorded here because the next unit built by parallel authors meets the same
edge, and the fix is to open the family in THIS file before the lessons are
written rather than after.

| ID | Statement (as a student holds it) | Elicited by | Confronted by | Lesson |
|---|---|---|---|---|
| `DIET-01` | A balanced diet means equal amounts of each food group. | `seven-bands` | `think-balanced` | `a-balanced-diet` |
| `DIET-02` | Vitamins give you energy. | `think-balanced` | `think-balanced` | `a-balanced-diet` |
| `DIET-03` | Fat is bad for you, so a healthy diet has none in it. | `think-balanced` | `think-balanced` | `a-balanced-diet` |
| `DIET-04` | The deeper the colour, the more of the nutrient there was. | `twenty-combinations` | `think-colour` | `food-tests` |
| `DIET-05` | A negative result proves the nutrient is not there. | `twenty-combinations` | `think-colour` | `food-tests` |
| `DIET-06` | The energy in food gets used up and disappears. | `feed-a-day` | `think-requirement` | `energy-in-food-and-what-you-need` |
| `DIET-07` | Everyone needs about the same amount of food in a day. | `feed-a-day` | `think-requirement` | `energy-in-food-and-what-you-need` |
| `DIET-08` | Malnourished means not having enough to eat. | `three-wrong-ideas` | `three-wrong-ideas` | `when-diet-goes-wrong` |
| `DIET-09` | Deficiency diseases are all in the past. | `three-wrong-ideas` | `three-wrong-ideas` | `when-diet-goes-wrong` |
| `DIET-10` | You can tell what someone eats by looking at them. | `three-wrong-ideas` | `three-wrong-ideas` | `when-diet-goes-wrong` |
| `DIET-11` | Digestion is food being squashed into smaller and smaller pieces. | `two-wrong-ideas` | `two-wrong-ideas` | `the-digestive-system` |
| `DIET-12` | Food sits in your stomach until it is digested, then goes to the intestine. | `two-wrong-ideas` | `two-wrong-ideas` | `the-digestive-system` |
| `DIET-13` | Enzymes are killed by heat. | `the-bench` | `two-wrong-ideas` | `enzymes-in-digestion` |
| `DIET-14` | The enzyme gets used up as the food is digested. | `the-bench` | `two-wrong-ideas` | `enzymes-in-digestion` |
| `DIET-15` | Villi make the intestine longer. | `fold-builder` | `villi-and-length` | `absorption-and-the-small-intestine` |
| `DIET-16` | The muscles push the food through the gut wall into the blood. | `villi-and-length` | `villi-and-length` | `absorption-and-the-small-intestine` |
| `DIET-17` | Bacteria are germs. Having bacteria inside you means you are ill. | `hook` | `germs-and-simplicity` | `bacteria-in-the-gut` |
| `CELL-08` | A single-celled organism is just a simpler version of one of our cells — the same parts, doing less. | `job-switch` | `germs-and-simplicity` | `bacteria-in-the-gut` |

**`CELL-08` reappears here and is not re-minted.** `bacteria-in-the-gut`'s second
confrontation is the belief that a single-celled organism is a simpler version of
one of our cells — which `unicellular-organisms` already owns, and which Design's
own copy names on the page ("You met this in Unicellular organisms and it comes
back with a bigger consequence"). A second id for one belief is precisely what
this register exists to prevent, so the row above carries the existing id and the
costume the student reads comes from the lesson's own `statements[]`.

---

### `BREATH` — air, breathing, and what an exchange surface actually does

Opened 16 Aug 2026 by B4 (MRB-244). Fifteen entries across five lessons. The unit
is unusual in the register: three of its beliefs are not brought in from outside
at all but are manufactured by earlier *teaching* — "you breathe in oxygen and
breathe out carbon dioxide" is a sentence a student was taught, and it has to be
taken apart rather than corrected.

⚠️ **The `DIET` collision happened again, and it was avoidable.** Five authors
worked this unit in parallel and two pairs of them independently minted the same
ids — `BREATH-03` for two different beliefs, and `BREATH-08` for two more. The
`DIET` note above had already diagnosed this and written down the fix: *open the
family in THIS file before the lessons are written rather than after.* That fix
was recorded and then not applied, so the second unit built by parallel authors
met the identical edge.

Nothing had been registered yet, so the family was renumbered into teaching order
before any id became permanent — the only window in which renumbering is allowed.
For B5 and B6 the fix is applied rather than re-noted: their families are opened
in this file **before** their authors are dispatched.

**The family is fifteen, not Design's thirteen, and that was a decision.**
NOTES-B4 §5 mints thirteen ids; the five pages carry fifteen quotes. The two
surplus beliefs were authored inline in `statements[]` with no register entry,
which reaches the student perfectly well — an authored statement wins over the
register in `r_confrontation`. They were minted anyway, as `BREATH-14` and
`BREATH-15`. An id is not for the student; it is the JOIN. `BREATH-12`/`13` are
already marked as resurfacing in B7, and a belief with no id cannot be joined to
a later unit, counted, or re-confronted on purpose — it can only be rewritten
from scratch by an author who never knew it had been fought before.

| ID | Statement (as a student holds it) | Elicited by | Confronted by | Lesson |
|---|---|---|---|---|
| `BREATH-01` | You breathe in oxygen and breathe out carbon dioxide. | `two-bags` | `three-wrong-ideas` | `the-gas-exchange-system` |
| `BREATH-02` | Breathing and respiration are the same thing. | `three-wrong-ideas` | `three-wrong-ideas` | `the-gas-exchange-system` |
| `BREATH-03` | Your lungs are hollow bags that fill up like balloons. | `three-wrong-ideas` | `three-wrong-ideas` | `the-gas-exchange-system` |
| `BREATH-04` | The lungs expand and pull the air in. | `work-the-diaphragm` | `think-what-moves-first` | `how-breathing-works` |
| `BREATH-05` | Air rushes in, and that is what makes the chest get bigger. | `work-the-diaphragm` | `think-what-moves-first` | `how-breathing-works` |
| `BREATH-06` | Oxygen is pumped across into the blood. | `count-the-crossings` | `think-crossings` | `alveoli-built-for-exchange` |
| `BREATH-07` | Oxygen moves in because it wants to spread out evenly. | `count-the-crossings` | `think-crossings` | `alveoli-built-for-exchange` |
| `BREATH-08` | Alveoli are where the air is stored. | `count-the-crossings` | `think-crossings` | `alveoli-built-for-exchange` |
| `BREATH-09` | Being out of breath means your lungs cannot hold enough air. | `locate-the-fault` | `think-what-changed` | `exercise-asthma-and-smoking` |
| `BREATH-10` | During an asthma attack there is not enough oxygen in the air. | `hook` | `think-what-changed` | `exercise-asthma-and-smoking` |
| `BREATH-11` | Tar is the harmful part of cigarette smoke. | `locate-the-fault` | `think-what-changed` | `exercise-asthma-and-smoking` |
| `BREATH-12` | Plants take in carbon dioxide and give out oxygen. Animals do the opposite. | `light-ledger` | `think-net` | `stomata-and-gas-exchange-in-plants` |
| `BREATH-13` | Plants respire at night and photosynthesise in the day. | `light-ledger` | `think-net` | `stomata-and-gas-exchange-in-plants` |
| `BREATH-14` | Something sucks the air in. | `work-the-diaphragm` | `think-what-moves-first` | `how-breathing-works` |
| `BREATH-15` | Plants breathe through their stomata. | `think-net` | `think-net` | `stomata-and-gas-exchange-in-plants` |

**`PART-10`/`PART-11` are re-confronted here and are not re-minted.**
`alveoli-built-for-exchange` fights *diffusion needs a push* and *particles intend
to spread* for the third time in the key stage, now doing real biological work
against a live counter. The `PART` reappears list above already named this lesson
as the site, written before it existed; the claim is now true. `BREATH-06` and
`BREATH-07` are the costumes those two ideas wear in a biology lesson, and they
carry their own ids because the belief a student states here is about oxygen and
blood, not about particles in a room.

**`BREATH-10` is elicited by the hook, not by the bench.** The asthma inhaler
opens the lesson and the belief is stated in the student's own answer before any
instrument runs. Recorded because the pattern in this unit is otherwise
instrument-elicited, and a wrong `elicited_by` is a join that looks right.

---

### `DRUG` — what a drug is, what it does once it is in the blood, and how a claim about one is judged

Opened 17 Aug 2026 by B6 (MRB-244). Eight entries across three lessons. The
family is unlike every other in this register: most of its beliefs are not wrong
science a student worked out from experience, but wrong *categories* they were
handed — that a drug is a legal classification rather than a description of what
a molecule does, that "natural" is a claim about safety, that a story is
evidence. Confronting them is closer to the nature-of-science pair `NOS-01`/
`NOS-02` (which is what `PART-12`/`PART-13` are now) than to anything in `DIET`
or `BREATH` — and one of this family's own entries has since been re-homed there
for exactly that reason. See `NOS-05` below.

**The collision fix from `DIET` and `BREATH` was finally applied.** Three
authors worked this unit in parallel with `DRUG-01/02`, `03/04` and `05/06`
**pre-allocated per lesson before dispatch**, with a named spare each for a third
belief. No id collided. This is the third unit to meet the edge and the first not
to have to renumber afterwards — the fix was written down after B3, ignored
before B4, and applied here.

**⚠️ `DRUG-07` is deliberately unused and must stay unused.** It was the spare
allocated to b6-01, whose third belief turned out to live in the *Going further*
layer — that "poison" is a category of substance rather than a statement about
quantity. That is stretch material and is confronted there rather than in a
`#s-think` block, so it was not minted. Ids are permanent, and a gap is cheaper
than a renumber; do not reuse `07` for something else.

**⚠️ `DRUG-09` is a second permanent gap, for the opposite reason.** It was
minted, and then re-homed to `NOS-05` on 17 Aug 2026 by MRB-248 — see `NOS`
below. The number is now vacant and stays vacant.

| ID | Statement (as a student holds it) | Elicited by | Confronted by | Lesson |
|---|---|---|---|---|
| `DRUG-01` | Drugs are illegal substances. | `hook` | `two-wrong-ideas` | `what-drugs-do-to-the-body` |
| `DRUG-02` | A painkiller goes to the part that hurts. | `follow-the-dose` | `two-wrong-ideas` | `what-drugs-do-to-the-body` |
| `DRUG-03` | Coffee, a cold shower or fresh air will sober you up. | `beat-the-liver` | `two-wrong-ideas` | `alcohol-and-smoking` |
| `DRUG-04` | A few cigarettes now and then is basically fine. | `two-wrong-ideas` | `two-wrong-ideas` | `alcohol-and-smoking` |
| `DRUG-05` | If it's natural, it's safe — it's the chemicals that hurt you. | `find-the-fault` | `two-wrong-ideas` | `substance-misuse-and-decisions` |
| `DRUG-06` | Everyone my age is doing it. | `find-the-fault` | `two-wrong-ideas` | `substance-misuse-and-decisions` |
| `DRUG-08` | Filters make cigarettes safer. | `two-wrong-ideas` | `two-wrong-ideas` | `alcohol-and-smoking` |

**`DRUG-01` reappears in both later lessons and is NOT re-declared — a ruling,
because the two authors made opposite calls.**

b6-02 opens on it (*legal for adults … more illness than every illegal drug put
together*) and b6-03's hook offers it as option B (*it is legal to buy in this
country*). One author declared a second `DRUG-01` row on their own lesson; the
other cited it in a comment and declared nothing. Same instruction, opposite
readings, and the register is where that has to be settled.

**Ruled: cite, do not re-declare.** A `misconceptions` row is not a citation.
`confronted_by` names the thing that does the confronting, and the declaring
author had pointed it at a **lesson slug** — the first value in the key stage
that names something on a different page. A slug is a pointer no page can
resolve, and a join that reads as working precisely because nothing checks it.

> ⊕ **Corrected after the sweep.** This paragraph originally went on to say that
> *the other twenty-nine values in KS3 all name a place on their own page
> (`hook`, `ladder`, `s-think`, `stretch-boundary`, or a real activity id)*.
> That was written from reading the records, and it was wrong: when the question
> was actually asked of the built pages, **`ladder` and `stretch-boundary` were
> two of the three that failed** — see the gate note under *Entry format*. The
> claim was true of `hook`, `s-think` and the activity ids only. It is left here,
> corrected rather than deleted, because assuming a value resolves because it
> looks like a name is the whole defect.

The precedent is `CELL-08` in the `DIET` table above: a borrowed id is
re-declared only where the page genuinely **re-confronts** the belief with a real
activity of its own. Neither b6-02 nor b6-03 does — they open on it and move on.
So the reappearance lives here, which is what NOTES-B6 §5 asked for in the first
place:

> `DRUG-01` reappears in `alcohol-and-smoking` (its big question IS the belief)
> and in `substance-misuse-and-decisions` (hook option B). Confronted once, in
> `what-drugs-do-to-the-body`.

**⚠️ Every `confronted_by` in this family names `two-wrong-ideas`.** That is not
a copy-paste error: Design draws exactly one "Think again" block per page in
this unit, carrying two quotes, and the block is the activity. The one exception
was `DRUG-09`, which b6-03 confronts inside the claim bench itself and hits
again at the ladder — the only belief in the unit attacked twice — and it has
since left the family as `NOS-05`. With it gone the rule is now exceptionless,
which is worth noting rather than quietly enjoying: an exceptionless rule here
means a future b6 page whose `confronted_by` is anything else is either a new
block Design drew or a mistake, and it is worth checking which.

---

### `REPRO` — reproduction, in animals and in flowering plants

Opened 16–17 Aug 2026 by B5 (MRB-244). Twenty entries across eight lessons — the
largest family in the register, and the only one covering two kingdoms, because
B5 teaches the human and the plant halves of the same statutory idea in one unit.

**Written from the authored records, not from NOTES-B5.** NOTES described these
entries as already written when they were not; the table below is extracted from
`ks3_data/b5/lesson_*.py` and every row is a value the build can resolve.

**Eight authors, ranges pre-allocated `REPRO-01/02` … `15/16`, two per lesson,
with a spare each.** Same discipline as `DRUG`, applied one unit earlier. Four
spares went unclaimed and **`REPRO-17`, `REPRO-20`, `REPRO-21` and `REPRO-23`
are permanent gaps** — do not reuse them. Four third beliefs did land, at `18`,
`19`, `22` and `24`.

| ID | Statement (as a student holds it) | Elicited by | Confronted by | Lesson |
|---|---|---|---|---|
| `REPRO-01` | The two systems are mirror images — every part has a matching part in the other. | `match-the-job` | `think-not-mirrors` | `human-reproductive-systems` |
| `REPRO-02` | Egg cells are made all the time, like sperm cells. | `think-not-mirrors` | `think-not-mirrors` | `human-reproductive-systems` |
| `REPRO-03` | Fertilisation is when the sperm reaches the egg. | `two-wrong-ideas` | `two-wrong-ideas` | `gametes-and-fertilisation` |
| `REPRO-04` | Identical twins happen when two eggs are fertilised. | `two-wrong-ideas` | `two-wrong-ideas` | `gametes-and-fertilisation` |
| `REPRO-05` | The cycle is 28 days and the egg comes out on day 14. | `hook` | `think-twenty-eight` | `the-menstrual-cycle` |
| `REPRO-06` | A period is the unfertilised egg leaving the body. | `think-twenty-eight` | `think-twenty-eight` | `the-menstrual-cycle` |
| `REPRO-07` | The baby breathes and eats inside the uterus. | `hook` | `two-wrong-ideas` | `gestation-placenta-and-birth` |
| `REPRO-08` | The baby's blood mixes with the mother's blood in the placenta. | `hook` | `two-wrong-ideas` | `gestation-placenta-and-birth` |
| `REPRO-09` | The placenta filters out anything harmful. | `does-it-cross` | `two-wrong-ideas` | `lifestyle-and-the-developing-foetus` |
| `REPRO-10` | So anything that goes wrong is the mother's fault. | `two-wrong-ideas` | `two-wrong-ideas` | `lifestyle-and-the-developing-foetus` |
| `REPRO-11` | Flowers are the pretty part of the plant. | `two-wrong-ideas` | `two-wrong-ideas` | `flowers-and-pollination` |
| `REPRO-12` | All flowers are pollinated by insects. | `s-hook` | `two-wrong-ideas` | `flowers-and-pollination` |
| `REPRO-13` | A tomato is a vegetable. | `two-wrong-ideas` | `two-wrong-ideas` | `fertilisation-seeds-and-fruit` |
| `REPRO-14` | Pollination and fertilisation are the same thing. | `s-hook` | `two-wrong-ideas` | `fertilisation-seeds-and-fruit` |
| `REPRO-15` | Plants disperse their seeds so the species can spread to new places. | `hook` | `two-wrong-ideas` | `seed-dispersal` |
| `REPRO-16` | Fruit is food the plant provides for animals. | `two-wrong-ideas` | `two-wrong-ideas` | `seed-dispersal` |
| `REPRO-18` | The egg is bigger than the sperm because it carries more genetic material. | `hook` | `two-cells` | `gametes-and-fertilisation` |
| `REPRO-19` | Period blood is waste the body has been storing up and is getting rid of. | `think-twenty-eight` | `think-twenty-eight` | `the-menstrual-cycle` |
| `REPRO-22` | The ovule and the ovary are the same thing. | `nine-parts` | `nine-parts` | `flowers-and-pollination` |
| `REPRO-24` | A seed with no wing and no parachute cannot be dispersed by wind. | `sort-the-eight` | `sort-the-eight` | `seed-dispersal` |

**`REPRO-09` is set up in `gestation-placenta-and-birth` and confronted in
`lifestyle-and-the-developing-foetus` — cited, not re-declared.** b5-04's
`drugs` substance carries the belief in Design's own words and hands it forward
deliberately (*"What follows from that is the whole of the next lesson"*). Under
the `CELL-08` precedent that is a **reappearance**, because b5-04 sets it up and
moves on rather than re-confronting it with an activity of its own. It is
declared once, on b5-05, which is the page that kills it.

**`REPRO-15` and `REPRO-16` are the teleology pair, and they are the unit's
hardest.** Both are the same error — that a plant structure exists *in order to*
achieve an outcome — and NOTES-B5 flag 44 binds across both halves of the unit.
b5-08's rung 3 marks down *wants* / *tries* / *so that*. ⚑ **Design's own copy in
`fertilisation-seeds-and-fruit` contains seven instances of purposive language**,
lifted unchanged under MRB-205 and reported as drift rather than silently
corrected. Mide's to rule on.

**`REPRO-10` is a safeguarding row, not just a science row.** "So anything that
goes wrong is the mother's fault" is elicited and confronted inside the same
block, and the anti-blame paragraph that does the confronting is load-bearing
copy lifted whole. It is answerable only because b5-04 states the placenta's
exchange rule neutrally first — the two lessons are a pair, and neither should
be edited without the other in view.

---

### `PLANT` — plant nutrition, photosynthesis, and what a leaf is for

Opened by **B7 *Photosynthesis*** (2026-08-17, MRB-245). Eight entries, two per lesson, all
`review_state: draft` — `statement` is science-bearing under §5.10 and needs Mide's review before
any of these freeze.

| ID | Statement (as a student holds it) | Elicited by | Confronted by | Lesson |
|---|---|---|---|---|
| `PLANT-01` | Plants get their food from the soil. | `s-hook` | `s-think` | `the-photosynthesis-reaction` |
| `PLANT-02` | Photosynthesis makes energy. | `s-think` | `s-think` | `the-photosynthesis-reaction` |
| `PLANT-03` | Leaves are green because chlorophyll uses green light. | `s-think` | `s-think` | `leaves-built-for-the-job` |
| `PLANT-04` | The bigger the leaf, the better the plant. | `s-tuner` | `s-think` | `leaves-built-for-the-job` |
| `PLANT-05` | The leaf goes black because the iodine reacts with the chlorophyll. | `s-think` | `s-think` | `testing-a-leaf-for-starch` |
| `PLANT-06` | Just pick a leaf and test it — the destarching is a waste of two days. | `s-think` | `s-bench` | `testing-a-leaf-for-starch` |
| `PLANT-07` | Plants do the photosynthesising — trees are the lungs of the planet. | `s-think` | `s-think` | `why-almost-all-life-depends-on-it` |
| `PLANT-08` | Plants make oxygen for us to breathe. | `s-jobs` | `s-think` | `why-almost-all-life-depends-on-it` |

**`PLANT-09` to `PLANT-12` are pre-allocated spares that were never claimed, and they stay
permanently unused.** One was reserved per lesson before the authoring passes were dispatched, so
that a pass finding a third belief on its page had an id to take without asking. None of the four
took one. They are the same discipline as `DRUG-07` and `REPRO-17`/`20`/`21`/`23`: a gap in the
numbering is the cheap outcome, and re-using a spare later would silently move a permanent id.

**`PLANT-06` is the only entry in this family confronted somewhere other than `s-think`,** and
deliberately. `method-breaker` lets the student skip the destarching and then read a verdict that
says the positive result proves nothing — the belief is killed by running it, not by being told.
The register's rule is that `confronted_by` names the activity that *kills* it, so it names the
bench.

**`PLANT-08` is deliberately distinct from `BREATH-12`, and the line between them is purpose.**
`BREATH-12` ("plants take in carbon dioxide and give out oxygen; animals do the opposite") is about
the *direction* of gas exchange and is `b4-05`'s to keep. `PLANT-08` is about oxygen being a **waste
product rather than a service** — a plant that gave away useful material on purpose would be
out-competed by one that did not. B7 does not restate `BREATH-12` or `BREATH-13`; it cites them.

**`PLANT-02` is confronted by pointing out of biology.** The page answers "photosynthesis makes
energy" with conservation of energy from `p1-01` and forward at B8's respiration — energy is
transferred between stores and never created, and a plant is not an exception to the laws of
physics. That cross-disciplinary move is NOTES-B7 flag 7 and is on Mide's list.

⚑ **NOTES-B7 §4 states these eight were already "written into
`docs/ks3/misconception-register.md` with a new prefix row".** They were not — the file carried no
`PLANT` prefix and no `PLANT` entry when B7 was picked up, and `PLANT` was still listed among the
families *not yet opened*. The entries above are written from the four authored pages, not from
NOTES. This is the second delivery to describe register work as done when it was not; `NOTES-B5`
did the same thing and the B5 run recorded it. Worth one process note rather than eight.

---

### `ECO` — ecosystems, feeding relationships and interdependence

Opened by **B9 *Ecosystems and interdependence*** (2026-08-18, MRB-248). Eleven entries — two per
lesson for five lessons, one for `sampling-an-ecosystem`, whose second belief is a nature-of-science
fault and lives in `NOS` as `NOS-04`. All `review_state: draft`; `statement` is science-bearing
under §5.10 and needs Mide's review before any of these freeze.

Every statement is Claude Design's own quoted belief from the approved page, lifted byte-identical.

| ID | Statement (as a student holds it) | Elicited by | Confronted by | Lesson |
|---|---|---|---|---|
| `ECO-01` | The arrow points at what the animal eats. | `s-ladder` | `s-think` | `food-chains-and-food-webs` |
| `ECO-02` | Ninety per cent of the energy is lost at each level. | `s-ladder` | `s-think` | `food-chains-and-food-webs` |
| `ECO-03` | The two peaks happen at the same time — more rabbits, more foxes. | `s-ladder` | `s-think` | `predator-and-prey` |
| `ECO-04` | Remove the predators and the prey will do brilliantly. | `s-ladder` | `s-think` | `predator-and-prey` |
| `ECO-05` | Removing a species only affects the things directly above and below it. | `s-hook` | `s-think` | `disturbing-a-food-web` |
| `ECO-06` | If it goes wrong, you just put the species back. | `s-bench` | `s-think` | `disturbing-a-food-web` |
| `ECO-07` | No bees, no food — we would starve within a few years. | `s-hook` | `s-think` | `pollinators-and-food-security` |
| `ECO-08` | Save the bees — keep a hive of honeybees. | — | `s-think` | `pollinators-and-food-security` |
| `ECO-09` | The poison gets stronger as it goes up the chain. | `s-hook` | `s-think` | `toxic-build-up-in-a-food-chain` |
| `ECO-10` | If the level in the water is safe, the ecosystem is safe. | `s-bench` | `s-think` | `toxic-build-up-in-a-food-chain` |
| `ECO-11` | Throwing the quadrat over your shoulder makes the placement random. | — | `s-think` | `sampling-an-ecosystem` |

**`ECO-06` is elicited by a button, not a sentence.** The bench's reset is labelled *"Put it back"* —
Design's own words, and the confrontation quotes them back. Pressing it restores the wood instantly
and completely, so the belief is PERFORMED rather than stated, and that is a real elicitation.

**`ECO-08` and `ECO-11` declare no `elicited_by`, and that is measured rather than lazy.** Nothing on
either page asks a student to commit to the belief — `ECO-08`'s page never offers keeping a hive as
an option, and `ECO-11`'s hook asks how you get a number at all. Absence is legal under MRB-248 and
is the honest answer; inventing an anchor to fill the column would fail the gate that checks the
anchor names a real place.

⛔ **`ECO-12` is a permanent gap and is never minted.** Its belief — *a large sample is an accurate
sample* — is a nature-of-science fault, not an ecology one, and it lives as `NOS-04`. B9's own
`NOTES-B9.md` §4 asks for twelve entries, two per lesson; the register supersedes it and the family
stops at eleven.

### `NOS` — nature of science: how models, evidence and theories actually work

**Opened 17 Aug 2026 by MRB-248, on the commander's ruling.** It is the first family in the
register opened by a ruling rather than by a unit, and the first populated by **re-homing ids that
already existed** rather than by minting new ones. The 26 Jul 2026 entry under `PART` set the
decision point at *"before `B10 how-we-worked-out-dna` and `C8 mendeleev` are authored"* and named
the cost of missing it — *"either a third home for the same idea or a rename"*. B10 is imminent,
three beliefs of this shape are already on the record, and a fourth and fifth are about to be
written. The rename was taken while the count was three.

The family is not disciplinary and is not meant to be. Its members are the beliefs a student holds
about **what science is and how a claim gets settled** — that a model is true or false, that
agreement ends the argument, that one case decides a general question. They surface in chemistry,
in biology and in PSHE-adjacent health material, which is precisely why they need one home: a wrong
idea fought in three subjects under three prefixes is fought three times from scratch.

| ID | Statement (as a student holds it) | Elicited by | Confronted by | Lesson |
|---|---|---|---|---|
| `NOS-01` | A scientific model is either true or false, and one exception proves it wrong. | `the-verdict` | `the-verdict` | `testing-the-model` |
| `NOS-02` | Scientists' models never change once they are agreed. | `settled-science` | `settled-science` | `testing-the-model` |
| `NOS-04` | A large sample is an accurate sample. | `s-ladder` | `s-think` | `sampling-an-ecosystem` |
| `NOS-05` | One person who came to no harm disproves a risk. | `find-the-fault` | `find-the-fault` | `substance-misuse-and-decisions` |

#### The three re-homes, and where each came from

| Was | Is | Why it moved |
|---|---|---|
| `PART-12` | `NOS-01` | Not a belief about particles. It sat under `PART` because C1 opened the register. |
| `PART-13` | `NOS-02` | The same, and its twin — both are about what happens to a model under evidence. |
| `DRUG-09` | `NOS-05` | Not a belief about drugs. "One person came to no harm" is `NOS-01` in a health costume: one case taken to settle a general claim. |

**⚠️ `DRUG-06` was named in the first cut of this re-home and STAYS IN `DRUG`. Recorded so it is
not re-argued.** The list handed down read `DRUG-06`; the correct entry is `DRUG-09`. `DRUG-06` is
*"Everyone my age is doing it."* — a belief about social norms, about what other people are
assumed to be doing. It is wrong about the world, not about how evidence works, and nothing in it
concerns models, samples or what a single case can settle. Putting it in `NOS` would make the
family mean "beliefs b6-03 confronts", which is the accident-of-build-order failure the family
exists to undo. `DRUG-09` is the entry that is `NOS-01`'s exact twin — a single case taken to
settle a general claim — and it is the one that moved.

#### Reserved, not minted here

These numbers are **allocated and must not be given to anything else.** Each is a belief a
forthcoming lesson will confront; each would otherwise have been minted into a family it does not
belong in, which is the whole reason this family exists. They are minted by the pass that authors
the page, not by this one — nothing is registered ahead of the lesson that needs it (the standing
rule at the top of this file).

| ID | Belief | Lesson | Would otherwise have been |
|---|---|---|---|
| `NOS-03` | A great discovery is one person's flash of insight. | B10 `how-we-worked-out-dna` | `GENE-06` |
| `NOS-06` | *(reserved)* | a future chemistry reactions unit | `REACT-18` |

⊕ **`NOS-04` MINTED 18 Aug 2026 by B9** and struck from the reserved table above, which is
what that table said would happen: a reserved id is minted by the pass that authors its page.
It is elicited at `s-ladder` — rung 2's first option is the belief in a student's own words —
and confronted at `s-think`. It reappears in `substance-misuse-and-decisions`, whose
claim-check bench holds the same fault in a health costume. `ECO-12` stays a permanent gap.

#### Permanent gaps — never allocate any of these

Two different kinds of gap, and both are permanent.

**Vacated by this re-home** — these numbers were minted, referenced, and are now empty. Never
reuse them:

- **`PART-12`** — its belief is `NOS-01`.
- **`PART-13`** — its belief is `NOS-02`.
- **`DRUG-09`** — its belief is `NOS-05`.

**Re-homed before they were minted** — these numbers were never issued at all, and must never be.
A future author reaching for the next free number in `GENE`, `ECO` or `REACT` must skip them,
because the belief that would have taken each one is now recorded elsewhere and a second id for one
belief is exactly what this register exists to prevent:

- **`GENE-06`** — is `NOS-03`.
- **`ECO-12`** — is `NOS-04`.
- **`REACT-18`** — is `NOS-06`.

These join the existing permanent gaps: `DRUG-07`, `REPRO-17`/`20`/`21`/`23`, and
`PLANT-09`–`PLANT-12`.

#### `ATOM-02` is cross-referenced, not re-homed

`ATOM-02` (*"a model that turns out to be wrong … should be discarded"*) is the same shape as
`NOS-01` and was named, in the `ATOM` notes above, as the third piece of evidence that this family
was wanted. It has **not** moved. The commander's re-home list named three ids; `ATOM-02` was not
among them, and a pass does not widen its own ruling. It is also doing work `NOS-01` is not — it is
about one named model's boundary on the page that draws that boundary. Cross-referenced from both
ends; if it should move, that is a fresh ruling.

#### ⚠️ The `PART-12`/`PART-13` register-vs-code drift, resolved 17 Aug 2026

The rows above carry `the-verdict` and `settled-science`. Until this pass the register recorded
`verdict-vote`/`model-limits-sort` and `predict-history`/`model-history-timeline` for these two —
**four values, none of which exists anywhere in the codebase or on the built page.** They were
written before `testing-the-model` was rebuilt (contract §3: C1 is a rebuild over a live unit), and
they describe the *superseded* body's activities. The rebuild renamed the instruments and nobody
updated the register, because nothing read it.

Resolved **in favour of the code**, per the standing rule that the built page is the authority:
`the-verdict` is the `keyed-commit` block's id and `settled-science` is the `#s-think` activity's,
and both are emitted as `data-activity="…"` on the page a student loads. The four register values
resolve to nothing. This is the same defect MRB-244 and MRB-248 gate for, caught one layer up — in
the markdown rather than in the Python — and it is the argument for the gate reading the Python and
the Python alone.

---

### `RESP` — respiration: what it is, where it happens, and what it is not

Opened 18 Aug 2026 by **B8 *Respiration*** (MRB-248). Ten entries across five
lessons. The family's centre of gravity is a single confusion the other
families do not have: **respiration is confused with two entirely different
things at once** — with BREATHING (`RESP-04`, `RESP-06`) and with BURNING
(`RESP-01`). Both are inherited from ordinary English rather than worked out
from experience, which is why `b8-01` and `b8-05` both spend their `#s-think`
on a word rather than on a mechanism.

**Ids were pre-allocated per lesson before dispatch**, two per lesson with a
named spare each, so five parallel authoring passes could not collide. This is
the fix `DIET`, `BREATH` and `REPRO` each had to learn the hard way and the
second unit to apply it from the start. No id collided.

**⚠️ `RESP-11` to `RESP-15` are ALL deliberately unused and must stay unused.**
Every one of the five passes was allocated a spare for a third belief and every
one declined it — the pages carry two confrontable beliefs each and no more.
Ids are permanent and a gap is cheaper than a renumber: do not reuse any of the
five for something else. Same rule as `DRUG-07` and `REPRO-17/20/21/23`.

**Two entries deliberately declare no `elicited_by`, and that is legal.**
`RESP-01` and `RESP-05` name beliefs that nothing on their page asks the student
to state — they are confronted directly rather than surfaced first. Under the
MRB-248 gate an absent `elicited_by` passes and a PRESENT one that names no
element on its own page fails, precisely so that this case does not have to be
faked with an invented anchor.

| ID | Statement (as a student holds it) | Elicited by | Confronted by | Lesson |
|---|---|---|---|---|
| `RESP-01` | Respiration is just slow burning. | — | `s-think` | `aerobic-respiration` |
| `RESP-02` | The fat is converted into energy, so the mass disappears. | `s-hook` | `s-think` | `aerobic-respiration` |
| `RESP-03` | Plants photosynthesise, animals respire. | `s-bench` | `s-think` | `why-every-cell-respires` |
| `RESP-04` | You respire when you need energy — when you exercise. | `s-jobs` | `s-think` | `why-every-cell-respires` |
| `RESP-05` | Lactic acid is why your legs ache two days after a hard session. | — | `two-wrong-ideas` | `anaerobic-respiration-in-humans` |
| `RESP-06` | When you sprint, you switch from aerobic to anaerobic respiration. | `s-hook` | `two-wrong-ideas` | `anaerobic-respiration-in-humans` |
| `RESP-07` | Fermenting is just food going off in a controlled way. | `s-think` | `s-think` | `fermentation` |
| `RESP-08` | Yeast is a powder — a raising agent, like baking powder. | `s-bench` | `s-think` | `fermentation` |
| `RESP-09` | Aerobic respiration is the fast one, because that is the one athletes train for. | `s-bench` | `s-think` | `aerobic-vs-anaerobic` |
| `RESP-10` | Anaerobic respiration is the emergency backup — something has gone wrong when it happens. | `s-hook` | `s-think` | `aerobic-vs-anaerobic` |
