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
| `GENE` | Variation, inheritance, and what a gene actually is | 2026-08-18, by B10 |
| `EVOL` | Natural selection, extinction and biodiversity | 2026-08-18, by B11 |
| `MIX` | Purity, mixtures, dissolving and what a separation technique can and cannot do | 2026-08-20, by C3 |
| `REACT` | Chemical reactions — what counts as one, what happens to the atoms, and how one is written down | 2026-08-20, by C4 |
| `ACID` | Acids, alkalis and the pH scale — what the words mean, what the scale measures, and what a catalyst does | 2026-08-21, by C6 |
| `ENER` | Energy in a change: which way it travels, where it is stored, and what a thermometer is and is not measuring | 2026-08-21, by C7 |
| `FORCE` | Forces and motion — what a speed is and what it is measured against; and what a force is, what it takes to make one, what is left over when they are added, and what that leftover does | 2026-08-24, by P3; widened 24 Aug 2026 by P4 |
| `PRESS` | Pressure — what a force does to a surface, which way a fluid pushes, and what happens where there is nothing to push | 2026-08-25, by P5 |
| `WAVE` | Waves — what travels and what stays put, what a wave's two measurements are, and how sound is made, carried, reflected, heard and put to work | 2026-08-25, by P6 |
| `LIGHT` | Light — what travels, how fast, what a surface does to it, how an image forms, and what colour is | 2026-08-25, by P7 |
| `CIRC` | Current and circuits — what a current is and what it is not, what a battery does, what happens at a junction, what a resistance is, and what a meter measures | 2026-08-25, by P8 |

Suggested starting families, from the misconception fields architecture.md §1 and §9 name explicitly
— **not yet opened, listed so numbering starts consistently**: ~~`FORCE` (forces and motion)~~
and ~~`CIRC` (current and circuits)~~. **Both are now open and the list is empty.**

⊕ **`FORCE` IS OPEN AS OF 24 Aug 2026, BY P3.** The strikethrough is kept rather than the line
deleted, because the sentence is what a later lane would read to decide whether to mint a new
family — and the answer is now no.

Design's `NOTES-P3.md` §4 asks for a ruling in as many words: *"open `FORCE` as below, or mint a
separate `MOT` family for describing-motion and leave `FORCE` for P4?"* **`FORCE` opens, and no
`MOT` family is minted**, for the reason the table above already gives: the family is declared as
*forces AND MOTION*, so motion is inside it as reserved. That is the same ruling this register
already made for `ENER` against `ENERGY` — the reservation is discharged into the family that
exists rather than left standing beside it — and applying it consistently is the point. A lane
that minted `MOT` here would leave the next lane with two plausible families and no rule.

P4 continues from `FORCE-12`.

⊕ **`CIRC` IS OPEN AS OF 25 Aug 2026, BY P8.** The strikethrough is kept rather than the line
deleted, for the reason `FORCE`'s is: the sentence is what a later lane would read to decide
whether to mint a new family, and the answer is now no. Design's `NOTES-P8-P9.md` §7 wrote
her sixteen proposed entries against `CIRC` and cited none of them, because access was read-only
and the family was not open. It is open now, on her numbers and in her words, and the same
ruling that discharged `ENERGY` into `ENER` and `MOT` into `FORCE` applies here: a reservation is
discharged INTO the family that exists rather than left standing beside a new one. **No `ELEC`
family is minted.**

⊕ **`ENERGY` IS GONE FROM THAT LIST, AND THE FAMILY IT RESERVED IS OPEN UNDER A SHORTER
NAME.** The reserved prefix was `ENERGY` (energy and temperature); Design's C7 delivery
proposed `ENER` and drew eight entries against it, and `ENER` is what C7 authored on
21 Aug 2026. It is the same family — a wrong idea about which way energy travels is the
same wrong idea whether it is met in a beaker or on a ramp — so the reservation is
DISCHARGED rather than left standing beside it. A physics lane meeting an energy
misconception adds to `ENER`; it does not open `ENERGY`.

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
| `CELL-14` | Specialised cells are made of different parts from ordinary cells. | `s-tuned` | `same-seven-tuned` | `specialised-cells` |
| `CELL-15` | A red blood cell is not really a cell, then. | `s-hook` | `same-seven-tuned` | `specialised-cells` |

⊕ **`CELL-14` and `CELL-15` registered 21 Aug 2026 (MRB-279), closing the same
silent gap MIX was closed for.** Both were authored in `specialised-cells`, both
have shipped to students, and neither had a row here. The pages were correct the
whole time — the joins resolve against the DOM, so `elicited_by` and
`confronted_by` both landed — but nothing could check that the ids existed, were
unique, or were still referenced. An unregistered id is not a broken page; it is
a page nothing is watching, which is how it stays broken once it breaks.

They were found by the bidirectional assertion added under MRB-279, which is now
the thing that stops this recurring: **every id an authored lesson references
must have a row here, and every row whose lesson is authored must be referenced
by it.** `CELL-09`–`CELL-12` are deliberately NOT failures of the second half —
they are registered against `stem-cells-and-meristems` and `enzymes-and-rate`,
which are not authored yet. Registering ahead of authoring is legal and useful;
the gate distinguishes it from an id registered against nothing at all.

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
| `NOS-03` | A great discovery is one person's flash of insight. | — | `s-think` | `how-we-worked-out-dna` |
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
| `NOS-06` | *(reserved)* | a future chemistry reactions unit | `REACT-18` |

⊕ **`NOS-04` MINTED 18 Aug 2026 by B9** and struck from the reserved table above, which is
what that table said would happen: a reserved id is minted by the pass that authors its page.
It is elicited at `s-ladder` — rung 2's first option is the belief in a student's own words —
and confronted at `s-think`. It reappears in `substance-misuse-and-decisions`, whose
claim-check bench holds the same fault in a health costume. `ECO-12` stays a permanent gap.

⊕ **`NOS-03` MINTED 18 Aug 2026 by B10 `how-we-worked-out-dna`**, and struck from the reserved
table above — the same treatment as `NOS-04` one entry earlier, and for the same reason: a reserved
id is minted by the pass that authors its page. It declares no `elicited_by`, and that is measured
rather than lazy. Nothing on `how-we-worked-out-dna` asks the student to commit to the belief: the
hook asks how you see something too small to see, and the model-builder bench requires all four
people's evidence to solve, which *performs* the counter rather than surfacing the belief. Absence
is legal under MRB-248 and is the honest answer; inventing an anchor would fail the gate that
checks it names a real place. Its `reappears_in` carries `testing-the-model`, where `NOS-01` and
`NOS-02` live. **`GENE-06` is now a permanent gap** — see below.

#### ⚖️ THE `NOS-03` / `GENE-06` RULING — DECIDED 18 Aug 2026 by the commander. Do not re-open.

The register and B10's schema contradicted each other and the register was carrying one side
silently. This section, written 17 Aug 2026, reserved `NOS-03` for b10-03's second belief and
listed `GENE-06` among the numbers never to be issued.
`docs/ks3/b10-inventory/PAYLOAD-SCHEMA.md` §12, written 18 Aug 2026, allocated `GENE-06` to that
same belief and handed the allocation to five parallel authoring passes who could not see each
other. Both could not stand.

**Ruled: `NOS-03` wins. `GENE-06` is a permanent gap and is never issued to anything.** The
reasoning is recorded because a future pass has to be able to see WHY, not only what:

1. **The belief is a nature-of-science belief.** *"A great discovery is one person's flash of
   insight"* is about how a claim gets settled and who settles it — not about genes, inheritance or
   variation. That is what `NOS` exists for, and it is why the family was opened at all.
2. **The precedent is already law here, and this is its third application, not a new decision.**
   `ECO-12`'s belief became `NOS-04` and `ECO-12` is a permanent gap. `REACT-18` → `NOS-06` is the
   same shape, reserved ahead of its unit. `GENE-06` → `NOS-03` is that pattern a third time. A
   register that applied it twice and then declined it once would mean the family boundary is
   negotiable, which is precisely the accident-of-build-order failure `NOS` was opened to undo.
3. **The schema is the document that was wrong, and it is the commander's own.** §12 is dated a day
   after this section and contradicts it; the commander is correcting §12 directly. **No pass edits
   §12 on the strength of this entry** — read the ruling here and build against it.

`NOS-01`, `NOS-02`, `NOS-04` and `NOS-05` are unaffected, and nothing else in the re-home list
moves.

⚠️ **b10-03's two beliefs are `GENE-05` and `NOS-03`.** Not `GENE-05` and `GENE-06`. An author
picking up `how-we-worked-out-dna` before the §12 correction lands will read the old allocation
there; **this file wins**. The `GENE` table below carries the same warning at the point of the gap,
because that is the other place an author will look. b10-03's pre-allocated spare is `GENE-13` and
is unaffected by the ruling — it remains an unclaimed permanent spare like the other four.

⚠️ **`NOTES-B11.md` §5 item 3 reproduces the `DRUG-06` error and must not be followed.** It lists
the open `NOS` question as affecting *"`PART-12`/`PART-13` in C1, `GENE-06` in B10, and arguably
`ECO-12`/`DRUG-06`"*. `DRUG-06` is a SOCIAL-NORM belief — *"Everyone my age is doing it."* — and
stays in `DRUG`, for the reasons already argued above; `ECO-12` is not open at all, it was settled
as `NOS-04` on 18 Aug; and `GENE-06` was settled as `NOS-03` on the same day. **None of the three
the note names is open.** The note stays uncorrected — Design's notes are not ours to edit — so a
pass reading it must come here rather than act on it.

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

- **`GENE-06`** — is `NOS-03`. **Settled 18 Aug 2026, see the ruling above.** Never issued, to this
  belief or to any other.
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

---

### `GENE` — variation, inheritance, and what a gene actually is

Opened 18 Aug 2026 by **B10 *Inheritance and variation*** (MRB-248). **Nine
entries across five lessons — two per lesson except b10-03, whose second belief
is a nature-of-science fault and lives in `NOS` as `NOS-03`.** Exactly the shape
`ECO` has, and for the same reason. All `review_state: draft` —
`statement` is science-bearing under §5.10 and needs Mide's review before any
of these freeze.

**Ids were pre-allocated per lesson before dispatch**, two per lesson with a
named spare each, in `docs/ks3/b10-inventory/PAYLOAD-SCHEMA.md` §12, so five
parallel authoring passes could not collide. Same discipline as `REPRO`,
`DRUG` and `RESP`. No id collided.

Every statement is Claude Design's own quoted belief, lifted byte-identical
from the two `.ks3-mis-quote` elements in each page's `#s-think`.

| ID | Statement (as a student holds it) | Elicited by | Confronted by | Lesson |
|---|---|---|---|---|
| `GENE-01` | Continuous variation is caused by the environment; discontinuous variation is genetic. | `s-ladder` | `s-think` | `variation-continuous-and-discontinuous` |
| `GENE-02` | If you can measure it with a ruler it is continuous. | `s-hook` | `s-think` | `variation-continuous-and-discontinuous` |
| `GENE-03` | Chromosomes, genes and DNA are three different things in the nucleus. | `s-ladder` | `s-think` | `chromosomes-genes-and-dna` |
| `GENE-04` | Only the cells that need a gene contain it. | `s-ladder` | `s-think` | `chromosomes-genes-and-dna` |
| `GENE-05` | Watson and Crick discovered DNA. | `s-ladder` | `s-think` | `how-we-worked-out-dna` |
| ~~`GENE-06`~~ | **PERMANENT GAP — the belief is `NOS-03`.** Never issued. See below. | — | — | — |
| `GENE-07` | Characteristics blend — a tall parent and a short parent give a medium child. | `s-hook` | `s-think` | `passing-it-on-heredity` |
| `GENE-08` | It skipped a generation, so the gene must have disappeared and come back. | `s-ladder` | `s-think` | `passing-it-on-heredity` |
| `GENE-09` | Organisms that look alike are the same species. | `s-hook` | `s-think` | `what-makes-a-species` |
| `GENE-10` | If two animals can have a baby together, they are the same species. | `s-hook` | `s-think` | `what-makes-a-species` |

⛔ **`GENE-06` IS A PERMANENT GAP AND IS NEVER ISSUED. Ruled 18 Aug 2026 by the commander.** Its
belief — *"A great discovery is one person's flash of insight."* — is a nature-of-science belief
and lives in `NOS` as `NOS-03`. The row is struck through above rather than deleted, so that the
gap at `06` reads as a decision and not as an id somebody forgot; a family that simply skipped a
number would invite the next author to assume it was free. It is in the same class as `ECO-12`,
`DRUG-07` and `REPRO-17`/`20`/`21`/`23`: **never re-pointed at a different belief, in this family
or any other.** The ruling and its three-case precedent are recorded in full in the `NOS` section
above.

⚠️ **b10-03's two beliefs are therefore `GENE-05` and `NOS-03` — not `GENE-05` and `GENE-06`.**
`docs/ks3/b10-inventory/PAYLOAD-SCHEMA.md` §12 still shows the old allocation until the commander's
correction to it lands, so an author picking up `how-we-worked-out-dna` may read `GENE-06` there.
**This file wins.** b10-03's pre-allocated spare, `GENE-13`, is untouched by the ruling and remains
an unclaimed permanent spare exactly like the other four.

**`NOS-03` declares no `elicited_by`, and that is measured rather than lazy.** Nothing on
`how-we-worked-out-dna` asks the student to commit to the flash-of-insight belief: the hook asks
how you see something too small to see, and the model-builder bench requires all four people's
evidence to solve — which *performs* the counter rather than surfacing the belief. Absence is legal
under MRB-248 and is the honest answer here; inventing an anchor to fill the column would fail the
gate that checks it names a real place. Same shape as `ECO-08`, `ECO-11`, `RESP-01` and `RESP-05`.

**⚠️ `GENE-11` to `GENE-15` are ALL deliberately unused and must stay unused.** One spare was
pre-allocated per lesson before dispatch so that a pass finding a third belief had an id to take
without asking; the pages carry two confrontable beliefs each and no pass claimed one. Ids are
permanent and a gap is cheaper than a renumber. **Never re-point a spare at a different belief** —
same rule as `DRUG-07`, `REPRO-17`/`20`/`21`/`23` and `PLANT-09`–`PLANT-12`, and the schema that
allocated them says so in the same words.

**`GENE-01` and `GENE-02` are two halves of one confusion and are deliberately separate.**
`GENE-01` is about *cause* — that a smooth range must be environmental — and is elicited at rung 2,
whose first distractor is the belief in a student's own words. `GENE-02` is about *how you tell*,
and is elicited at the hook, whose option B offers measurement-with-an-instrument as the test. The
page's KEY FACT keeps them apart in one sentence: whether variation is continuous is a question
about the data, and what caused it is a separate question with a separate answer.

**`CELL-05` reappears in `chromosomes-genes-and-dna` and is NOT re-minted.** The `CELL` list above
predicted it would land here, *"where it does real damage"*, and the prediction is now met — but
only glancingly. The page's ladder says *"every cell **with a nucleus** carries the complete set"*,
which presupposes the correction rather than confronting it; `GENE-04` is the belief this page
actually takes apart, and it is a different one. Under the cite-do-not-re-declare rule that makes
this a reappearance, recorded here rather than a second `CELL-05` row.

### ⚑ STANDING NOTE — a delivery's §4 is an ALLOCATION PROPOSAL, not a record of register work

Recorded once here, and it applies to every unit past, present and future. Four deliveries have now
stated that their misconception entries were *"written into `docs/ks3/misconception-register.md`
with a new prefix row"* when no such row and no such entry existed: **`NOTES-B5`, `NOTES-B7`,
`NOTES-B10` and `NOTES-B11`.** In the B11 case the delivery's own
`docs/ks3/b11-inventory/PAYLOAD-SCHEMA.md` §11 item 5 caught it independently — `grep -n "EVOL"`
on this file returned nothing.

**Four occurrences is a pattern, not four slips**, and the pattern has a cause worth naming: a
delivery's §4 is written by the pass that *decides* the ids, and deciding them feels like recording
them. It is not. This file is hand-maintained, has no generator, and nothing writes to it except a
pass that opens it and types.

So the rule for every pass that reads a NOTES §4 or a schema §12:

- Read it as **the allocation being proposed** — which ids, for which beliefs, on which lessons.
- **Never read it as evidence the register contains them.** Check this file. `grep` the prefix.
- If the family is absent, the register work is outstanding and is yours; write it from the
  approved pages, which are the authority on wording, not from NOTES.
- If NOTES and this file disagree on an id, **this file wins** — see the `NOS-03`/`GENE-06` ruling
  above for what happens when they do, and how expensive it is once authors are already building.

---

### `EVOL` — natural selection, extinction and biodiversity

Opened 18 Aug 2026 by **B11 *Evolution and inheritance*** (MRB-248). Eight
entries across four lessons, two per lesson. All `review_state: draft`, as
above.

The family sits directly on top of `GENE` and is the point of it: `GENE`
establishes that variation exists and is inherited unchanged, and `EVOL` is
what follows once an environment does the choosing. The unit's hardest problem
is **agency in the wrong place** — the idea that an organism or a population
changes itself because it needs to. `EVOL-03` and `EVOL-04` are that instinct
undisguised, `EVOL-02` is its cousin, and it is the Lamarckian error the whole
of `natural-selection` is built to take apart.

Every statement is Claude Design's own quoted belief, lifted byte-identical
from the two `.ks3-mis-quote` elements in each page's `#s-think`.

| ID | Statement (as a student holds it) | Elicited by | Confronted by | Lesson |
|---|---|---|---|---|
| `EVOL-01` | Survival of the fittest means the strongest survive. | `s-hook` | `s-think` | `variation-and-competitive-success` |
| `EVOL-02` | Some individuals are just better than others. | `s-ladder` | `s-think` | `variation-and-competitive-success` |
| `EVOL-03` | Animals change themselves to suit their environment, and pass the change on. | `s-hook` | `s-think` | `natural-selection` |
| `EVOL-04` | The population needed to change, so it did. | `s-hook` | `s-think` | `natural-selection` |
| `EVOL-05` | Extinction is unnatural — it only happens because of us. | `s-ladder` | `s-think` | `when-the-environment-changes-extinction` |
| `EVOL-06` | If a species goes extinct, another one just takes its place. | — | `s-think` | `when-the-environment-changes-extinction` |
| `EVOL-07` | Biodiversity means how many different species there are. | `s-ladder` | `s-think` | `biodiversity-and-gene-banks` |
| `EVOL-08` | We have gene banks, so it does not matter if species are lost in the wild. | `s-ladder` | `s-think` | `biodiversity-and-gene-banks` |

**⚠️ `EVOL-09` to `EVOL-12` are ALL deliberately unused and must stay unused.** One spare per
lesson, pre-allocated in `docs/ks3/b11-inventory/PAYLOAD-SCHEMA.md` §12 before any author started;
none was claimed. **Never re-point a spare at a different belief** — the same rule as `DRUG-07`,
`REPRO-17`/`20`/`21`/`23`, `PLANT-09`–`PLANT-12` and `RESP-11`–`RESP-15`. The schema also records
the escalation an author must take instead: a pass needing a SECOND spare stops and reports rather
than reaching past the table, because two lessons minting from the same next-free number is a
collision permanent ids cannot undo.

**`EVOL-06` declares no `elicited_by`, and that is measured.** *"Takes its place"* occurs exactly
once on `when-the-environment-changes-extinction`, in the `#s-think` quote itself. The hook asks
which species survives a change, the ladder's two marked rungs are about risk factors and about
whether extinction is natural, and the pressure bench has no commit gate. Nothing asks the student
to state the belief before it is taken apart. Absence is legal under MRB-248 and the honest answer;
inventing an anchor would fail the gate.

**Two `reappears_in` edges are load-bearing and were asked for by name.**

- `EVOL-01` (strongest survive) → `natural-selection`. The moth runner is the same claim under a
  live counter: no moth is strong, and the one that survives is the one that happens to match the
  bark.
- `EVOL-06` (another species takes its place) → B9 `disturbing-a-food-web`, which owns `ECO-05`
  (*removing a species only affects the things directly above and below it*). They are the same
  instinct at two scales — that a web absorbs a loss — and B9's removal bench is where a student
  has already watched it fail.

**`EVOL-03` and `EVOL-04` are the Lamarckian pair and are elicited at the hook, together.** The
giraffe hook offers stretching-and-inheriting as option A and needed-so-it-developed as option C,
which is Design putting both costumes of one wrong idea in front of the student before the lesson
starts. They carry separate ids because the confrontations differ — `EVOL-03` fails on the
mechanism of inheritance, `EVOL-04` on a population having no way to want anything — but an author
touching either should have both in view.

**`EVOL-02` is `REPRO-15`/`REPRO-16`'s relative, and the family's quietest problem.** It is
teleology again: that there is a general ranking of organisms and that being *better* is a property
an animal carries around. The page kills it by reversal rather than by assertion — the thick-coated
mouse is best in winter and worst in the drought, and the same mouse did not change. Rung 3 asks
the student to say what that means for the idea of a *better* animal, which is where the belief is
committed to; the confrontation is `#s-think` as everywhere else in this unit.

⚑ **NOTES-B11 §4 states these eight were already written into this file "with a new prefix row".**
They were not. See the standing note under `GENE` above — B11 is the fourth delivery to say so, and
the rows above are written from the approved pages rather than from NOTES.

---

### `MIX` — purity, mixtures, and what a separation technique can actually do

Opened by **C3 *Mixtures and separation*** (2026-08-20, authored by Claude Design, MRB-272).
All thirteen are `review_state: draft`.

⚑ **THESE ROWS WERE MISSING UNTIL 2026-08-20 (MRB-246), AND C3 HAD ALREADY SHIPPED.** C3 authored
thirteen `MIX` ids across seven lessons, referenced them in every lesson record, and passed every
gate — because **nothing in the build reads this file.** The `elicited_by` / `confronted_by` joins
are gated (MRB-244/248) against the built page; the register itself is not gated against anything.
So a unit can ship a whole family that exists only in its own lesson records, which is exactly what
happened, and it is the fifth time a delivery's own notes claimed register work that was never
done — see the standing note under `GENE`.

The rows below are written from the AUTHORED LESSON RECORDS, not from NOTES-C3, and were generated
by reading `ks3_data/c3/` rather than retyped. That is the only source that cannot be wrong about
what the pages actually say.

| ID | Statement (as a student holds it) | Elicited by | Confronted by | Lesson |
|---|---|---|---|---|
| `MIX-01` | It says 100% pure on the carton, and there is nothing bad in it, so it is pure. | `s-hook` | `think-again-juice` | `pure-or-mixture` |
| `MIX-02` | If it looks the same all the way through, it is pure. | `eight-samples` | `eight-samples` | `pure-or-mixture` |
| `MIX-03` | Dissolving destroys the solute, or turns it into liquid. | `s-hook` | `think-again-melting` | `dissolving-and-solutions` |
| `MIX-04` | Stirring harder makes more dissolve. | `gate-which-dial` | `dissolve-lab` | `dissolving-and-solutions` |
| `MIX-05` | Dissolving is melting. | `s-think` | `think-again-melting` | `dissolving-and-solutions` |
| `MIX-06` | I filtered the pond water and it came out clear, so it is clean water now. | `think-commit-pond` | `think-commit-pond` | `filtration` |
| `MIX-07` | A fine enough filter would separate salt from water. | `s-ladder` | `s-particles` | `filtration` |
| `MIX-08` | The water has gone. It evaporated, so it is not anywhere any more. | `think-commit-water` | `think-commit-water` | `evaporation-and-crystallisation` |
| `MIX-09` | Faster evaporation gives more product. | `crystallising-bench` | `crystallising-bench` | `evaporation-and-crystallisation` |
| `MIX-10` | Steam off boiling sea water tastes salty, so some salt must come over with it. | `think-commit-spray` | `think-commit-spray` | `distillation` |
| `MIX-11` | The dye or colour is made by the paper or the solvent. | `s-hook` | `chroma-run` | `chromatography` |
| `MIX-12` | The spot that travels furthest is the one there is most of. | `think-commit-furthest` | `think-commit-furthest` | `chromatography` |
| `MIX-13` | One measurement is enough if it is the right answer. | `think-commit-one-run` | `melting-points` | `proving-something-is-pure` |

**`MIX-02` is claimed by TWO lessons and that is correct, not a duplicate row.** `pure-or-mixture`
elicits it at the eight-sample sorter, where a uniform-looking mixture is the trap; and
`proving-something-is-pure` confronts it again four lessons later against a melting point, where
looking the same all the way through is finally beaten by a measurement. The id is one belief; the
two lessons are two different arguments against it, and the second is the one that settles it.

**Where these are expected to resurface:**

- `MIX-01` (the food-label meaning of *pure*) → C6 acids and alkalis, wherever a concentration is
  described, and every KS4 lesson that says *pure* about a reagent.
- `MIX-07` (a fine enough filter stops anything) is the size argument, and it is the one that
  travels furthest → KS4 separation techniques, and reverse osmosis wherever desalination appears.
- `MIX-13` (one measurement is enough) is `NOS`-shaped and is flagged as such: it is a belief about
  evidence, not about chemistry. It sits here rather than in `NOS` only because the `NOS` re-homing
  pass has not run since C3 landed. An author opening `NOS` next should take it.

---

### `REACT` — chemical reactions: what counts as one, what happens underneath, and how one is written

Opened by **C4 *Chemical reactions*** (2026-08-20, authored by Claude Design, MRB-246).
`REACT-01` to `REACT-09` are C4's; `REACT-10` to `REACT-18` are C5 *Types of reaction*, added
with that unit on 2026-08-21. All are `review_state: draft`.

⚠️ **THE ROWS BELOW ARE GENERATED FROM `ks3_data/c4/`, NOT FROM NOTES-C4 §6, AND THEY DIFFER FROM
IT IN FIVE PLACES.** NOTES proposed the ids a delivery *expects* to emit; these are the ids the
pages *do* emit, checked against the built HTML. Writing NOTES' names here would have reproduced
exactly the defect this file was just repaired for under `MIX` — a register recording intent
rather than fact.

Four of the five differences have ONE structural cause, and it is worth stating because the next
chemistry unit will hit it too. `build_ks3.py` emits a confrontation's reveal as
`<div class="ks3-reveal ks3-reveal-panel" hidden data-reveal>` with **no `id`**. MRB-244/248 gate
these joins against `id="…"` and `data-activity="…"` on the built page, so a name like
`think-reveal-glass`, `think-reveal-no-such-atom` or `think-reveal-peroxide` **cannot be made to
resolve from inside a content lane** — the reveal has no name to point at. Those three joins name
the ACTIVITY that owns both the commitment and the reveal instead, which is c3-03's `MIX-06` form
and is also what satisfies Law 3 (the gate wants a `confronted_by` that is a real activity id).

The fifth, `REACT-04`, is different and better: **two** asks are refused, and an id must be unique,
so the join names gold's refusal specifically — and that suffix is DERIVED from the atoms on the
table, so a payload edit that put gold within reach would rename the element and turn the MRB-244
gate red. The register is a guard on the chemistry there, not just a record of it.

⚑ **Open engine item, logged not fixed:** giving the generic reveal panel an `id` would let all
three joins name the thing that actually does the confronting. It is a one-line change in a SHARED
file that moves bytes on every KS3 page in the key stage, so it belongs to an engine run on main,
not to a content lane.

| ID | Statement (as a student holds it) | Elicited by | Confronted by | Lesson |
|---|---|---|---|---|
| `REACT-01` | If you can undo it, it is physical. If you cannot undo it, it is chemical. | `think-commit-reverse` | `think-commit-reverse` | `chemical-vs-physical-change` |
| `REACT-02` | Something disappearing into a liquid is always the same kind of change. | `pair-2-commit` | `pair-2-reveal-marble` | `chemical-vs-physical-change` |
| `REACT-03` | When magnesium burns, the magnesium atoms turn into magnesium oxide atoms. | `think-commit-mgo-atom` | `think-commit-mgo-atom` | `reactions-rearrange-atoms` |
| `REACT-04` | New atoms can be made if the conditions are right. | `ask-gold` | `ask-gold-refusal` | `reactions-rearrange-atoms` |
| `REACT-05` | The arrow is like an equals sign, so you could write the equation the other way round. | `s-think` | `think-reveal-direction` | `word-equations` |
| `REACT-06` | Heat, energy or a flame can be written into an equation as a reactant. | `builder-distractor` | `builder-check` | `word-equations` |
| `REACT-07` | Gases do not weigh anything, so the missing 2.20 g cannot be the carbon dioxide. | `think-commit-gas` | `sealed-flask-run` | `mass-in-a-reaction` |
| `REACT-08` | An equation can be balanced by changing the small numbers in a formula. | `forbidden-small-2` | `forbidden-reveal` | `symbol-equations-and-balancing` |
| `REACT-09` | Balancing is just a maths puzzle — as long as the numbers add up, the equation is right. | `think-commit-maths` | `think-commit-maths` | `symbol-equations-and-balancing` |
| `REACT-10` | The big yellow flame is hotter — you can see more fire. | `think-commit-yellow` | `think-commit-yellow` | `combustion` |
| `REACT-11` | Shutting the air off makes a flame burn hotter or more fiercely. | `gate-air-shut` | `shut-hole-run` | `combustion` |
| `REACT-12` | It went black, so the copper carbonate burnt. | `think-commit-black` | `think-commit-black` | `thermal-decomposition` |
| `REACT-13` | A decomposition reverses when it cools. | `cool-gate` | `stage-4-reveal` | `thermal-decomposition` |
| `REACT-14` | Aluminium does not corrode — that is why drinks cans and window frames are made of it. | `s-think` | `think-reveal-oxide-layer` | `oxidation` |
| `REACT-15` | Rusting needs water only, or air only. | `tube-predictions` | `four-tube-summary` | `oxidation` |
| `REACT-16` | The copper on the nail came out of the nail — the iron turned into copper on the outside. | `think-commit-nail` | `think-commit-nail` | `displacement` |
| `REACT-17` | A less reactive metal will displace a more reactive one if you heat it or wait longer. | `grid-predict` | `grid-reveal` | `displacement` |
| `REACT-18` | A reaction can only be one of the four types, so if it is oxidation it cannot be combustion. | `think-commit-one-box` | `think-commit-one-box` | `which-reaction-is-this` |

**Three of these are `ATOM` ids grown up, and they are cross-referenced rather than re-minted.**

- `REACT-03` is `ATOM-01` at the next level. An atom that carries the properties of its substance
  becomes an atom that *becomes* another substance when the substance does. Same belief, one year
  older, and a student who still holds `ATOM-01` will reach `REACT-03` on their own.
- `REACT-08` is `ATOM-09` in its balancing costume — the small number in a formula read as a
  quantity you may adjust. The confrontation is **deliberately the same substance**, H₂O₂, as
  `ATOM-10`'s, so C2 and C4 reinforce each other instead of each teaching it once.
- `REACT-07` cross-references `ATOM-11` (burning destroys matter) and `PART-05`. That chain is now
  four ids long across three units, and it is the strongest argument yet that this register needs a
  **cross-family "same belief" link type** rather than a prose paragraph under each family. Design
  raised it in NOTES-C4 §6 as a request rather than a decision, and it is recorded here as still
  open — the prose above is doing a job a field should do.

⚖️ **`REACT-18` STAYS IN `REACT`, RULED 2026-08-21 (MRB-246).** Design flagged it (NOTES-C5 §5)
as the register's fifth `NOS`-shaped entry living in a content family — it is not a factual error at
all, it is a wrong idea about how CLASSIFICATION works — and asked for the `NOS` call before C8,
which is the next chemistry unit in the queue.

The ruling is to leave it here, and the reason is not that Design is wrong. She is right that it is
`NOS`-shaped. But whether `NOS` ABSORBS entries out of content families is a decision about the
register's taxonomy that changes PERMANENT IDS across several units at once, and taking it one
entry at a time in the middle of authoring a content unit is how a taxonomy fragments — you end up
with two entries re-homed, three not, and no principle recorded anywhere.

So it is recorded instead. **There are now TWO `NOS`-shaped entries parked in content families:**

  · `REACT-18` — each reaction has exactly one type, so two names cannot both be right
  · `MIX-13` — one measurement is enough if it is the right answer

**The next `NOS` pass takes BOTH, together, with the principle written down.** That pass is a
register job, not a lesson job, and nothing in C5 changes either way: `c5-05` authors `REACT-18`
and confronts it whatever family it eventually sits in.

**`REACT-01` is the unit's load-bearing entry.** Irreversibility as the test for a chemical change
is the single most common wrong rule at this age, and it survives most teaching because most
teaching accidentally confirms it: the examples chosen are usually irreversible. C4's answer is to
choose the examples the other way — melting glass, dissolving, and a rust that a steelworks
reverses every day — so the rule fails in front of the student rather than being contradicted at
them. Nothing in `c4-01` may be justified by "you cannot get it back", including the hook, or the
lesson confirms on one line what it breaks on the next.

---

### `ENER` — energy in a change: which way it travels, where it is stored, and what a thermometer measures

Opened by **C7 *Energy changes in reactions*** (2026-08-21, drawn by Claude Design, MRB-272).
`ENER-01` to `ENER-08` are C7's, four lessons, two entries each. All are `review_state: draft`.

⚠️ **THE ROWS BELOW ARE GENERATED FROM `ks3_data/c7/`, NOT FROM NOTES-C7 §5, AND THEY DIFFER FROM
IT IN SIX PLACES.** NOTES proposed the ids a delivery *expects* to emit; these are the names the
pages *do* emit, checked against the renderers in `ks3_art/c7.py`. Writing NOTES' names here would
reproduce exactly the defect this file was repaired for under `MIX` — a register recording intent
rather than fact.

The six differences fall into two causes, and both will recur in the next chemistry unit.

**Cause one, four rows: no `think-reveal-*` id can be emitted from a content lane.**
`build_ks3.py`'s shared `r_activity` draws a confrontation's reveal as
`<div class="ks3-reveal ks3-reveal-panel" hidden data-reveal>` with **no `id`**, and `build_ks3.py`
is not a file a lane may touch. So `think-reveal-latent`, `think-reveal-balance`,
`think-reveal-absence` and `think-reveal-systematic` **cannot be made to resolve**. All four joins
name the ACTIVITY that owns both the commitment and the reveal instead — c3-03's `MIX-06` form,
C4's and C5's too — which is also what satisfies Law 3, since the gate wants a `confronted_by`
that is a real activity id. This is the same open engine item C4 and C5 both logged: giving the
generic reveal panel an `id` is a one-line change in a SHARED file that moves bytes on every KS3
page, so it belongs to an engine run on `main`, not to a content lane.

**Cause two, two rows: a ladder rung is not a name any page carries.** NOTES proposes
`rung-2` / `rung-2-feedback` for `ENER-06` and `ENER-08`. The ladder emits no per-rung `id` at all,
so those joins could never have resolved — and unlike cause one, the fix is not a workaround but a
better site. Both beliefs are taken apart by an INSTRUMENT on their own page, and both instruments
already had to emit a named panel:

  · `ENER-06` — the eight-item sorter puts melting and freezing three rows apart and then names
    the pair in its closing panel. `sort-eight` elicits, `sort-close` confronts.
  · `ENER-08` — the rig builder produces eight readings that agree in being too low, and its
    payoff panel says the error runs one way. `rig-build` elicits, `rig-close` confronts.

`curve-close`, `sort-close`, `rig-close` and `use-fireworks-reveal` are all authored in the lesson
record and emitted by C7's renderers from that value, rather than composed inside a renderer — so
the register's join and the markup have one source, and a payload edit that renamed a panel would
turn the MRB-244 gate red rather than quietly breaking the pointer.

| ID | Statement (as a student holds it) | Elicited by | Confronted by | Lesson |
|---|---|---|---|---|
| `ENER-01` | While ice is melting it has stopped absorbing heat. | `think-commit-plateau` | `think-commit-plateau` | `energy-and-changes-of-state` |
| `ENER-02` | A thermometer measures how much energy something has. | `curve-run` | `curve-close` | `energy-and-changes-of-state` |
| `ENER-03` | A reaction that needs heating to start cannot be exothermic. | `think-commit-spark` | `think-commit-spark` | `exothermic-reactions` |
| `ENER-04` | Chemical reactions create energy. | `use-fireworks` | `use-fireworks-reveal` | `exothermic-reactions` |
| `ENER-05` | An endothermic reaction produces cold. | `think-commit-cold` | `think-commit-cold` | `endothermic-reactions` |
| `ENER-06` | Melting and freezing both take energy in, because both involve ice. | `sort-eight` | `sort-close` | `endothermic-reactions` |
| `ENER-07` | Repeating an experiment and averaging makes the result accurate. | `think-commit-average` | `think-commit-average` | `measuring-a-temperature-change` |
| `ENER-08` | Results that agree closely with each other must be correct. | `rig-build` | `rig-close` | `measuring-a-temperature-change` |
| `ENER-09` | Energy gets used up. When something stops, the energy it had has been spent and is gone. | `s-hook` | `store-audit-ledger` | `energy-stores` |
| `ENER-10` | Light, sound and electricity are kinds of energy that things store. | `store-pathway-sort` | `store-pathway-sort` | `energy-stores` |
| `ENER-11` | There is energy inside the battery, and using the phone lets it leak out until there is none left. | `s-hook` | `before-after-tally` | `energy-transfers-before-and-after` |
| `ENER-12` | The car has stopped, so it has run out of energy — a quantity that stops being visible has stopped existing. | `s-hook` | `running-total` | `conservation-of-energy` |
| `ENER-13` | Temperature and energy are the same thing — if something is hotter it must hold more energy. | `s-hook` | `two-quantities` | `heating-and-thermal-equilibrium` |
| `ENER-14` | Cold is a substance that travels — put ice in a drink and the cold moves out of the ice into the drink. | `think-cold-travels` | `one-way-flow` | `heating-and-thermal-equilibrium` |
| `ENER-15` | Metal is a colder material than wood — some materials are inherently colder than others. | `s-hook` | `touch-test` | `conduction` |
| `ENER-16` | Heat rises, so heating always travels upwards. | `three-routes` | `think-heat-rises` | `radiation` |
| `ENER-17` | Radiation means the dangerous kind — anything called radiation can harm you. | `radiation-word-sort` | `radiation-word-sort` | `radiation` |
| `ENER-18` | A blanket, a woolly hat or a coat is a source of warmth — insulation adds heat to what it wraps. | `s-hook` | `ice-trial` | `insulation` |
| `ENER-19` | A machine that multiplies force gives you energy for free. | `s-hook` | `lever-bench` | `simple-machines` |
| `ENER-20` | A calorie on a food label is the same calorie a physicist uses. | `s-think` | `s-think` | `energy-in-food` |
| `ENER-21` | A higher-wattage appliance uses more electricity, so switching to a lower-wattage one always saves energy. | `s-hook` | `power-bench` | `power-ratings-in-watts` |
| `ENER-22` | An appliance on standby is off, so it costs nothing. | `s-think` | `s-think` | `power-ratings-in-watts` |
| `ENER-23` | The time in E = P × t goes in as it was given, so a 2000 W kettle for 3 minutes transfers 2000 × 3 = 6000 J. | `s-think` | `s-think` | `calculating-energy-transferred` |
| `ENER-24` | A joule is a decent amount of energy, so a few thousand joules sounds about right for boiling a kettle. | `s-think` | `s-think` | `calculating-energy-transferred` |
| `ENER-25` | A kilowatt-hour is a measure of power — it has kilowatt in the name. | `s-hook` | `kwh-rectangles` | `reading-a-fuel-bill` |
| `ENER-26` | Switch everything off and the bill goes to zero. | `s-think` | `s-think` | `reading-a-fuel-bill` |
| `ENER-27` | Renewable means clean, and non-renewable means polluting. | `s-hook` | `two-axis-grid` | `fuels-and-energy-resources` |

⊕ **`ENER-09` ONWARD ARE PHYSICS, IN THE SAME FAMILY.** The prefix table's ruling is
explicit — *"A physics lane meeting an energy misconception adds to `ENER`; it does not
open `ENERGY`"* — and P1 is the first lane to act on it. Design's `NOTES-P1.md` §1 calls
these `ENERGY-01` and `ENERGY-02` and says they were added to this register on 15 Aug 2026;
no such id was ever added, and the ruling above forbids the prefix. They are minted here as
`ENER-09` and `ENER-10`, continuing C7's numbering.

⊕ **`ENER-11` ADDED 24 Aug 2026 BY `p1-02`.** Design's `NOTES-P1.md` §2 calls it
`ENERGY-03`. Same ruling, same reason: the prefix is `ENER` and the numbering
continues. Her §1 announces fourteen ids, `ENERGY-01`..`ENERGY-14`, but her §2
coverage table names only ELEVEN distinct beliefs across the eight lessons — so
the block was never fourteen entries wide, and P1 mints eleven, `ENER-09`
through `ENER-19`, one per belief her table actually confronts.

⊕ **`ENER-12`..`ENER-19` ADDED 24 Aug 2026 BY `p1-03`..`p1-08`.** Design's `NOTES-P1.md` §2 calls them `ENERGY-04`..`ENERGY-11`; the prefix is `ENER` and the numbering continues, for the reason above.

⊕ **`ENER-20`..`ENER-27` ADDED 24 Aug 2026 BY P2 `p2-01`..`p2-05`.** Same
ruling, same prefix, numbering continues. Design's `NOTES-P2.md` §1 predicts
FOUR ids for the unit — her `ENERGY-01` re-confronted plus `ENERGY-12`,
`ENERGY-13` and `ENERGY-14` — and the unit mints EIGHT. The difference is
not a disagreement about the science; it is a date. Her notes are 15 Aug and
her own 23 Aug audit (§2) then added "a second misconception quote" to all
sixteen P1–P3 lessons. Those second quotes are what the extra four rows are,
and each was checked for being a genuinely different belief rather than the
first one re-dressed:

  · `ENER-20` is a UNITS error (label kcal vs physicist's calorie), not an
    energy-conservation one — a student can hold it while being perfectly
    sound on stores.
  · `ENER-22` is a factual claim about the appliance (standby draws nothing),
    not the rate/total confusion of `ENER-21`.
  · `ENER-24` is a belief about the SIZE of a joule, and it is what lets
    `ENER-23` survive: a student who knew a joule was tiny would reject
    6000 J for a kettle on sight.
  · `ENER-26` is about the BILL (a fixed standing charge), not about the
    unit misread of `ENER-25`.

⊖ **TWO OF P2'S SECOND QUOTES MINT NOTHING, DELIBERATELY.** `p2-01`'s first
quote ("you burn off the calories at the gym") is `ENER-09` re-confronted —
its `reappears_in` list predicted exactly this arrival — and `p2-05`'s second
quote ("electricity is a clean energy resource") is `ENER-10` doing work in a
new situation: electricity is a PATHWAY, not a store and not a resource. Both
follow P1's own precedent, where `p1-08`'s second quote ("a longer lever gets
the job done with less energy") took no row because it was `ENER-19` wearing
different clothes.

⚠️ **`ENER-21` IS RE-CONFRONTED BY `p2-03` ON REAL APPLIANCES AND MINTS
NOTHING THERE.** The fridge at 90 W outranking the oven at 2200 W is the same
belief meeting arithmetic instead of a bench, and `r_appliance_bench` asserts
that the inversion stays reachable — if a later edit to a wattage made
every appliance rank in the same order as its rating, the bench would quietly
agree with the belief `p2-02` spent a lesson killing.

### `FORCE` — forces and motion

Opened 24 Aug 2026 by P3 *Describing motion*. Every row below was checked against Design's
DELIVERED page rather than taken from her proposed table: her `NOTES-P3.md` §4 predates her own
23 Aug audit, which added a second misconception quote to all sixteen P1–P3 lessons.

| ID | Statement (as a student holds it) | Elicited by | Confronted by | Lesson |
|---|---|---|---|---|
| `FORCE-01` | Whichever one gets there first is going faster. | `compare-pairs` | `compare-pairs` | `speed` |
| `FORCE-02` | How fast something looks is how fast it is going. | `s-hook` | `compare-pairs` | `speed` |
| `FORCE-03` | The average speed for a journey is the average of the speeds you travelled at. | `s-think` | `s-think` | `speed` |
| `FORCE-04` | Speed is worked out by dividing the two numbers in the order you were given them. | `s-ladder` | `s-ladder` | `speed` |
| `FORCE-05` | A speed camera tells you how fast you were going on the journey. | `s-think` | `s-think` | `speed` |
| `FORCE-06` | A distance–time graph is a picture of the route: the line going up means going uphill. | `s-think` | `s-think` | `distance-time-graphs` |
| `FORCE-07` | A flat line on a distance–time graph means moving at a steady speed. | `graph-plot` | `graph-plot` | `distance-time-graphs` |
| `FORCE-08` | A curved line on a distance–time graph means the object is going round a bend. | `s-think` | `s-think` | `distance-time-graphs` |
| `FORCE-09` | An object has one true speed; a speed measured from a moving train is an illusion. | `s-hook` | `relative-frames` | `relative-motion` |
| `FORCE-10` | Two things moving towards each other pass at the speed of one of them. | `s-think` | `s-think` | `relative-motion` |
| `FORCE-11` | Sitting still in a train seat, you are not moving. | `s-think` | `s-think` | `relative-motion` |
| `FORCE-12` | A moving object has force in it, and the force runs out. | `s-hook` | `s-think` | `what-a-force-is` |
| `FORCE-13` | A table is not doing anything; it is just there. | *(none — nothing on the page asks for this commitment)* | `s-think` | `what-a-force-is` |
| `FORCE-14` | A force can only act between things that are touching. | `board` | `board` | `what-a-force-is` |
| `FORCE-15` | The force is in the movement of the object, and not in either object. | `s-ladder` | `s-ladder` | `what-a-force-is` |
| `FORCE-16` | The bigger arrow wins, so the object moves at the bigger force. | `s-hook` | `s-think` | `drawing-and-adding-forces` |
| `FORCE-17` | Force arrows should all be drawn the same length. | `s-ladder` | `s-think` | `drawing-and-adding-forces` |
| `FORCE-18` | Forces along a line always add up. | `sledge` | `sledge` | `drawing-and-adding-forces` |
| `FORCE-19` | Equal and opposite forces cancel out and stop existing. | `s-ladder` | `s-ladder` | `drawing-and-adding-forces` |
| `FORCE-20` | If something is not moving, there are no forces on it. | `s-hook` | `s-think` | `balanced-and-unbalanced` |
| `FORCE-21` | Balanced forces mean the object is stopped. | `s-ladder` | `s-think` | `balanced-and-unbalanced` |
| `FORCE-22` | Weight in newtons is the same number as the mass in kilograms. | `rig` | `s-ladder` | `balanced-and-unbalanced` |
| `FORCE-23` | A support pushes back as hard as it is able to, rather than as hard as it needs to. | `s-ladder` | `s-ladder` | `balanced-and-unbalanced` |
| `FORCE-24` | If something is moving, a force must be pushing it along. | `s-hook` | `s-think` | `what-forces-do-to-motion` |
| `FORCE-25` | A sideways force makes it go sideways instead. | `gates` | `s-think` | `what-forces-do-to-motion` |
| `FORCE-26` | At the top of its flight a thrown ball has no force on it. | `s-ladder` | `s-ladder` | `what-forces-do-to-motion` |
| `FORCE-27` | A force that is slowing something down has been used up by the time it stops. | `s-ladder` | `s-ladder` | `what-forces-do-to-motion` |
| `FORCE-28` | Starting something sliding and keeping it sliding need the same push. | `s-hook` | `drag` | `friction` |
| `FORCE-29` | A smooth surface has no friction. | `drag` | `s-think` | `friction` |
| `FORCE-30` | Friction only exists once something is moving. | `s-ladder` | `s-think` | `friction` |
| `FORCE-31` | A steady speed means the friction has been overcome, so there is none left. | `s-ladder` | `s-ladder` | `friction` |
| `FORCE-32` | Heavier things always fall faster. | `s-ladder` | `s-think` | `air-and-water-resistance` |
| `FORCE-33` | Air resistance is a fixed force, the same at any speed. | `fall` | `fall` | `air-and-water-resistance` |
| `FORCE-34` | When the parachute opens you are pushed back upwards. | *(none — nothing on the page asks for this commitment)* | `s-think` | `air-and-water-resistance` |
| `FORCE-35` | Terminal velocity is a speed limit that falling cannot pass. | `s-hook` | `fall` | `air-and-water-resistance` |
| `FORCE-36` | A longer spanner means you are pulling harder. | `spanner` | `s-think` | `moments` |
| `FORCE-37` | The distance is measured from where you are standing. | *(none — nothing on the page asks for this commitment)* | `s-think` | `moments` |
| `FORCE-38` | A moment is a force, so it is measured in newtons. | `s-ladder` | `s-ladder` | `moments` |
| `FORCE-39` | The distance from the pivot only decides which way something turns, not how much. | `s-ladder` | `s-ladder` | `moments` |
| `FORCE-40` | Extension is how long the spring is. | *(none — nothing on the page asks for this commitment)* | `s-think` | `springs-and-hookes-law` |
| `FORCE-41` | Double the load always doubles the extension. | `s-hook` | `plot` | `springs-and-hookes-law` |
| `FORCE-42` | Past the limit of proportionality the spring snaps. | `s-hook` | `s-think` | `springs-and-hookes-law` |
| `FORCE-43` | An overstretched spring goes back to its natural length if you leave it long enough. | `s-ladder` | `s-ladder` | `springs-and-hookes-law` |
| `FORCE-44` | A force needs something in between to carry it across. | `s-hook` | `s-think` | `non-contact-forces` |
| `FORCE-45` | There is no gravity in space. | *(none — nothing on the page asks for this commitment)* | `s-think` | `non-contact-forces` |
| `FORCE-46` | Magnets attract all metals. | *(none — nothing on the page asks for this commitment)* | `three-forces` | `non-contact-forces` |

⊖ **ONE OF DESIGN'S PROPOSED ROWS MINTS NOTHING.** Her table names *"a steeper line means it went
further"* as a row of its own, attached to `p3-02`'s rung 2. The belief IS on the page — it is
that rung's first distractor — but it is `FORCE-07` read from the other side: both are reading a
gradient as something other than a speed. It takes no row, following `p1-08`'s precedent for a
second quote that re-dresses an existing belief. `FORCE-08` takes the number instead.

⚠️ **`FORCE-04` IS THE ONE TO WATCH, AND DESIGN SAID SO FIRST.** Her notes: *"it is arguably the
same wrong idea as `PART-05`-style 'the numbers do what they are told', i.e. a mathematics
misconception wearing a science costume. It is the one on this list I would most expect to be
re-homed."* It is minted here because the belief is genuinely confronted on the page — `p3-01`
rung 1's second distractor is `0.60 ÷ 1.5`, with feedback naming the swap — and because ids
are permanent, so leaving it unminted while the page confronts it is the worse of the two errors.
If a mathematics-facing family is ever opened, this is the first row that should move to it.

⚠️ **`FORCE-03` CLOSES ITS OWN LOOP IN `p3-03`.** Rung 4 there asks for the round trip to be found
from total distance ÷ total time rather than by averaging 300 and 200 m/s — which is
`FORCE-03` met again in a different situation. It is re-confronted and mints nothing.

⊕ **`FORCE-12` … `FORCE-46` MINTED 24 Aug 2026 BY P4 *Forces*, exactly where this family's own
ruling said they would be:** *"P4 continues from `FORCE-12`."* Thirty-five rows over nine lessons.

⚠️ **DESIGN'S PROPOSED NUMBERS ARE NOT THE ONES USED, AND COULD NOT HAVE BEEN.** Her
`NOTES-P4-P6.md` §6 reserves `FORCE-01` … `FORCE-36`, four per lesson, opening `p4-01` at
`FORCE-01`. Those numbers were already spent three weeks' work earlier in the same family: P3 took
`FORCE-01`…`FORCE-11` and `FORCE-01` there is *"whichever one gets there first is going faster"*.
Her ranges are a reservation made without sight of this file, which she says in as many words —
*"access here is read-only, so no id is cited on any page"* — and the ranges are the only part
of her proposal that moved. **Every STATEMENT below is hers or is drawn from her delivered page.**

⊕ **EIGHT ROWS ARE NOT IN HER PROPOSED TABLE.** Each arrived from a delivered distractor or a
delivered correction rather than from her §6 list, and each is a genuinely separate belief rather
than a re-dressing of one already minted — which is the `p1-08` test this register applies:

  * `FORCE-15` the force is in the MOVEMENT, not in either object (`p4-01` rung 1 option D). A
    student can hold this while being perfectly sound that force does not run out.
  * `FORCE-19` equal and opposite forces cancel out and STOP EXISTING (`p4-02` rung 2 option D).
    Separate from `FORCE-18`: the arithmetic is accepted and the forces are thought to have gone.
  * `FORCE-23` a support pushes back as hard as it is ABLE to, not as hard as it NEEDS to
    (`p4-03` rung 1 option D, 80 N under a 40 N box). It is the belief the *Going further* layer
    answers.
  * `FORCE-27` a force that is slowing something down has been USED UP by the time it stops
    (`p4-04` rung 1 option C). The impetus theory in its second form — not "motion needs a
    force" but "the force drains".
  * `FORCE-31` a steady speed means friction has been OVERCOME, so there is none left
    (`p4-05` rung 1 option B). A `p4-03` idea meeting friction for the first time.
  * `FORCE-35` terminal velocity is a speed LIMIT rather than a balance. Design's own bench note
    corrects it in as many words — *"this is terminal velocity, and it is a balance, not a
    limit"* — which is a correction with no elicitation, and therefore a belief the page is
    answering.
  * `FORCE-39` the distance from the pivot only decides WHICH WAY it turns, not how much
    (`p4-07` rung 1 option D).
  * `FORCE-43` an overstretched spring recovers if you LEAVE IT LONG ENOUGH (`p4-08` rung 2
    option B). Separate from `FORCE-42`: the permanence is accepted as a rate rather than denied.

⊖ **THE PREDICTION ABOUT `FORCE-09` DID NOT COME TRUE, AND IT IS LEFT STANDING.** The note below
says *"`FORCE-09` in P4 (`what-forces-do-to-motion`)"* — that a student's belief in one true
speed would resurface there. It does not: `p4-04` never changes frame, and its hook is a curling
stone on ice rather than anything measured against a moving thing. The prediction is kept rather
than deleted because it is still a reasonable one for **P12** `gravity-earth-moon-and-sun`, which
is the other half of the same sentence, and because a register that quietly removes its own
wrong guesses stops being a record of what was expected.

⚠️ **`FORCE-12` IS THE OLDEST IDEA IN THIS SUBJECT AND IT IS CONFRONTED FOUR TIMES.** Impetus —
*a moving object has force in it, and the force runs out* — is elicited on `p4-01` and met again
on `p4-04` (rung 1 option C, as `FORCE-27`), on `p4-05` (the crate) and on `p4-09` (the kicked
ball, whose note says nothing is pushing the ball forwards once it has left the boot). Only the
first mints; the rest are the same belief in new clothes, which is what this family is for.

⚠️ **EXPECTED TO RESURFACE.** `FORCE-06`/`FORCE-07` in P6 (waves on a graph) and in ANY graph
lesson in biology or chemistry — `B10 variation` plots something completely different and the
same reading error arrives with it. `FORCE-09` in P4 (`what-forces-do-to-motion`) and P12
(`gravity-earth-moon-and-sun`).

⚠️ **`ENER-12` WAS ANTICIPATED BY THIS REGISTER BEFORE IT EXISTED.** The `PART-05` lock below names `ENER-12` as `p1-03`'s id while no such row was in the table — it was reserved in prose by the run that minted `ENER-09`/`ENER-10`, and `p1-03` has now filled it. The lock stands unchanged: `c1-03` and `p1-03` confront one underlying belief by two different instruments, a balance for mass and a thermometer for energy, and NEITHER may drop its confrontation on the grounds that the other covers it.

⊖ **`PART-03` IS RE-CONFRONTED BY `p1-04` AND MINTS NOTHING.** The closing paragraph of her `#s-think` is C1's fixed-size reference particle doing work in a new situation — heating changes how fast particles move and nothing else — rather than a new belief.

⚠️ **`ENER-12` (`p1-03`) AND `PART-05` WILL BE THE SAME UNDERLYING BELIEF** — that a
quantity stops existing when it stops being visible. Design's notes lock them together and
the lock stands: separate IDs because the confrontations genuinely differ (a balance for
mass, a thermometer for energy), but neither `c1-03` nor `p1-03` may drop its confrontation
on the grounds that the other covers it. Same shape as the `CELL-08` lock.

**`ENER-05` is the unit's load-bearing entry, and it is the one that reaches furthest.** "Cold is
not a substance" is not a chemistry fact — it is the sentence that makes a fridge, a cold pack, a
sweating body and a heat pump all one idea instead of four. `c7-03` states it flatly rather than
hedging it (Design's NOTES-C7 §4 flag 9 asked whether the bluntness was wanted; it is), because a
hedged version leaves the student holding exactly the belief.

**`ENER-02` is `ENER-01` one level up, and the pair is why `c7-01` needs two entries.** A student
who believes the ice has stopped absorbing heat believes it *because* they are reading the
thermometer as an energy meter. `ENER-01` is the observation and `ENER-02` is the instrument
mistake underneath it, so the page confronts them in that order: the flat step first, at
`#s-think`, and then the closing panel on the curve itself.

⚑ **`ENER-03` overlaps C8's `PTAB-07`** ("sodium melted because the water was hot"). Both
are heat coming OUT of a reaction being read as heat that went IN. NOTES-C8 §5 asks for the
cross-reference to be recorded rather than the two merged, and that is the right call: they are
elicited by different phenomena — a Bunsen you had to light against a metal that melted itself —
and a student can hold either without the other.

⊕ **Corrected 21 Aug 2026 (MRB-281). The edge is now recorded, below, in this section's
"Where these are expected to resurface" list — the form this file keeps `reappears_in` in.**
This entry previously read *"Recorded here rather than as a `reappears_in` value, because C8 is
drawn but **not yet authored**, and the slug NOTES-C8 names (`group-1-the-alkali-metals`) is not in
`ks3_data/structure.py`."* Both halves of that were false, and the superseded sentence is kept
because the way it was reached is the point.

C8 **was** authored — six lessons, author's notes and support, delivered 21 Aug — and had been
sitting in the main checkout's working directory the whole time. A git worktree shares `.git` but
**not** its working directory, so an untracked delivery dropped into one tree is invisible from
every other tree. Searching from this lane and finding nothing was read as the unit not existing,
and that reading was then written into this file as a reason. The slug was missing from
`structure.py` only because §7's five-slot plan had never been reconciled with C8's real lesson
list; reconciling it (MRB-281) added the three group slugs and the seventh slot.

The rule the original note invoked is the right rule — a `reappears_in` pointing at a slug that
does not exist is precisely the defect this file was repaired for under `MIX`. The error was in the
premise, not the rule. **Prose is the un-checkable form: no gate reads it, so nothing could
contradict it.** An edge is checked on every build, which is why the correction is an edge.

**Where these are expected to resurface** (`reappears_in`, filled as the units are authored):

- `ENER-03` (a reaction that needs heating to start cannot be exothermic) → C8
  `group-1-the-alkali-metals`, where the same belief arrives wearing different clothes as
  `PTAB-07`: a lump of sodium melts in cold water and the heat is read as having come from the
  trough. Both are heat coming OUT of a reaction being read as heat that went IN. They stay two
  entries, because they are elicited by different phenomena — a Bunsen you had to light against a
  metal that melted itself — and a student can hold either without the other.

⚠️ **`reappears_in` is a column of THIS FILE and not a key of a lesson record.** `build_ks3.py`
reads nothing by that name, so authoring one in `ks3_data/` is a dead key — `ks3_key_audit.py`
reports it as "read by nothing", which is how the first attempt at this correction was caught.
`ks3_data/b11/lesson_01_variation_and_competitive_success.py` had already ruled it.

⚑ **`ENER-07` and `ENER-08` are both `NOS`-shaped and both sit here by accident of build order.**
Neither is a factual error about energy: one is a wrong idea about what averaging does and the
other about what agreement proves. Design flagged this in NOTES-C7 §5 and put it plainly —
*"that is now eight nature-of-science entries across five content families. **The `NOS` call is
past due** — C5's notes said the last comfortable moment was before C8, and C8 is now built."*

The ruling is the same one MRB-246 made for `REACT-18`, and for the same reason: whether `NOS`
ABSORBS entries out of content families changes PERMANENT IDS across several units at once, and
taking it one entry at a time in the middle of authoring a content unit is how a taxonomy
fragments. So they stay, and the parked list grows to **four**:

  · `REACT-18` — each reaction has exactly one type, so two names cannot both be right
  · `MIX-13` — one measurement is enough if it is the right answer
  · `ENER-07` — repeating and averaging makes a result accurate
  · `ENER-08` — results that agree closely must be correct

**The next `NOS` pass takes all four, together, with the principle written down.** That pass is a
register job, not a lesson job, and nothing in C7 changes either way: `c7-04` authors both entries
and confronts both whatever family they eventually sit in.


---


### `PRESS` — pressure, and what a fluid is doing to everything in it

Opened 25 Aug 2026 by P5 *Pressure*. Every row below was checked against Design's DELIVERED page
rather than taken from her proposed table.

⚖️ **WHY A NEW FAMILY AND NOT `FORCE`.** `FORCE` is declared as *forces and motion*, and this
register's own rule is to discharge a reservation into the family that exists rather than open one
beside it — that is how `ENER` absorbed `ENERGY` and how `FORCE` absorbed `MOT`. It does not
reach here. Pressure is its own statutory strand (`KS3.P.PRES.*`), and the beliefs below are not
about forces and motion at all: they are about what a fluid does to a surface, which direction it
does it in, and what happens when there is nothing there to do it. Filing *"a vacuum sucks things
in"* under a family whose description is *"what a speed is and what it is measured against"* would
make the family name stop meaning anything.

The pattern this follows is the chemistry one — `MIX` for C3, `REACT` for C4, `ACID` for C6,
`ENER` for C7 — one family per strand of related beliefs, minted by the unit that first needs it.

| ID | Statement (as a student holds it) | Elicited by | Confronted by | Lesson |
|---|---|---|---|---|
| `PRESS-01` | A sharp point pushes harder than a blunt one. | `s-hook` | `s-think` | `pressure-force-over-area` |
| `PRESS-02` | Pressure only pushes downwards. | *(none — nothing on the page asks for this commitment)* | `s-think` | `pressure-force-over-area` |
| `PRESS-03` | Pressure is a force, so it is measured in newtons. | `s-ladder` | `s-ladder` | `pressure-force-over-area` |
| `PRESS-04` | More of the sole touching the floor means more pressure on it. | `s-ladder` | `sand` | `pressure-force-over-area` |
| `PRESS-05` | More liquid in total means more pressure at the bottom. | `s-ladder` | `s-think` | `pressure-in-liquids` |
| `PRESS-06` | Water is heavier, or packed tighter, deeper down. | `s-hook` | `s-think` | `pressure-in-liquids` |
| `PRESS-07` | Pressure in a liquid acts downwards only. | *(none — nothing on the page asks for this commitment)* | `probe` | `pressure-in-liquids` |
| `PRESS-08` | A narrow container concentrates the pressure, so its base takes more than a wide one at the same depth. | `s-ladder` | `s-ladder` | `pressure-in-liquids` |
| `PRESS-09` | Heavy things sink and light things float. | `s-ladder` | `s-think` | `upthrust-floating-and-sinking` |
| `PRESS-10` | Only things that float get upthrust. | *(none — nothing on the page asks for this commitment)* | `s-think` | `upthrust-floating-and-sinking` |
| `PRESS-11` | Upthrust depends on how heavy the object is. | `tank` | `tank` | `upthrust-floating-and-sinking` |
| `PRESS-12` | Being hollow is what makes something float. | `s-ladder` | `s-ladder` | `upthrust-floating-and-sinking` |
| `PRESS-13` | A vacuum sucks things in. | `s-hook` | `s-think` | `atmospheric-pressure` |
| `PRESS-14` | If air really pressed that hard, we would feel it. | *(none — nothing on the page asks for this commitment)* | `s-think` | `atmospheric-pressure` |
| `PRESS-15` | A sealed bag swells at altitude because gravity is weaker up there. | `climb` | `s-ladder` | `atmospheric-pressure` |
| `PRESS-16` | The air runs out at a definite height, and above it there is none at all. | `s-ladder` | `climb` | `atmospheric-pressure` |

⚠️ **FOUR ROWS ARE NOT IN DESIGN'S PROPOSED TABLE**, and each arrived from a delivered distractor
rather than from her §6 list. Each is a genuinely separate belief rather than a re-dressing of one
already minted, which is the `p1-08` test this register applies:

  * `PRESS-04` more of the sole touching the floor means MORE pressure on it (`p5-01` rung 2
    option C). Separate from `PRESS-01`: a student can have given up "sharp pushes harder" and
    still have the area the wrong way round.
  * `PRESS-08` a NARROW container concentrates the pressure, so its base takes more than a wide
    one at the same depth (`p5-02` rung 2 option B). It is `PRESS-05` from the other side — not
    "more water" but "a narrower tube concentrates it" — and it is a `p5-01` idea being
    misapplied one lesson later, which is exactly the kind of thing worth its own id.
  * `PRESS-12` being HOLLOW is what makes something float (`p5-03` rung 2 option D), whose
    correction is that a hollow object full of water sinks.
  * `PRESS-16` the air runs out at a definite height and above it there is none at all. It
    arrived with Design's own six-band stack, which thins upwards without ever reaching zero, and
    with the bench readout that never gets to 0 per cent.

⚠️ **`PRESS-02` AND `PRESS-14` HAVE NO `elicited_by`, WHICH §5.3 ALLOWS.** Nothing on either page
asks the student to commit to them; each is confronted because it sits underneath one that is.

⚠️ **EXPECTED TO RESURFACE.** `PRESS-13` — *a vacuum sucks* — in P11 (the particle model of a
gas) and anywhere a syringe, a pipette or a pump is drawn. `PRESS-06` — *the stuff is heavier
lower down* — is the same shape as `PART`'s compression beliefs and will meet them in P11.

⊖ **`p5-01` RE-CONFRONTS `ENER-19` AND MINTS NOTHING.** Design's FLAG 9 records that the register
routes a force-multiplication belief to a P5 `hydraulics` lesson that `structure.py` does not
have, and resolves it by putting the hydraulic jack in `p5-01`'s *Going further* with the distance
traded explicitly against the force. That resolution is kept. **The register was never pointing at
nothing**: the entry she names is `ENERGY-11`, the `ENERGY` prefix was discharged into `ENER` on
21 Aug, and the belief lives as `ENER-19` — *"a machine that multiplies force gives you energy
for free"* — owned by `p1-08 simple-machines` and confronted by its lever bench. `p5-01` meets it
in a second situation, which is what this register asks a lesson to do.

### `WAVE` — waves and sound

⊕ **OPENED 25 Aug 2026, BY P6.** `docs/ks3/design-reference/p6/NOTES-P6-P7.md` §7 pre-allocated `WAVE-01` … `WAVE-36`, four per
lesson in slot order, and authored 22 of them without citing one on any page — because access was read-only and this register had no
open family for waves or sound. **Every id she wrote is minted here on the number she gave it, in her words.** The fourteen gaps are
minted from the real lesson content, which is the register's own rule: an id is minted from what a page actually confronts, never
reserved against what one might.

⚠️ **TWO OF HERS ARE ON THE NUMBER SHE GAVE THEM BECAUSE THIS PASS CHECKED.** `WAVE-30` had been minted onto 31 and one of her own
statements pushed onto a spare; `WAVE-27` had been paraphrased. Both are back. A pre-allocation is only useful if the lane that
fills it reads it.

| ID | Statement, as a student holds it | Elicited by | Confronted by | Lesson |
|---|---|---|---|---|
| `WAVE-01` | The water travels along with the wave. | `s-hook` | `s-think` | `waves-on-water` |
| `WAVE-02` | A bigger wave is a longer wave. | `tank` | `s-think` | `waves-on-water` |
| `WAVE-03` | The amplitude runs from the trough up to the crest. | `s-ladder` | `parts` | `waves-on-water` |
| `WAVE-04` | A wave whose water only goes up and down is standing still. | `s-hook` | `s-hook` | `waves-on-water` |
| `WAVE-05` | When two waves cancel they destroy each other. | `meet` | `meet` | `transverse-waves-and-superposition` |
| `WAVE-06` | If the water is flat the energy has gone. | *(none — nothing on the page asks for this commitment)* | `meet` | `transverse-waves-and-superposition` |
| `WAVE-07` | Two waves meeting average out. | `s-ladder` | `s-ladder` | `transverse-waves-and-superposition` |
| `WAVE-08` | The stronger wave wins and the weaker one disappears. | `s-hook` | `s-think` | `transverse-waves-and-superposition` |
| `WAVE-09` | Sound is made by the air, not by the object. | `s-hook` | `chain` | `how-sound-is-made` |
| `WAVE-10` | If you cannot see it moving it is not vibrating. | `chain` | `s-think` | `how-sound-is-made` |
| `WAVE-11` | A microphone is a quiet loudspeaker. | `s-ladder` | `s-think` | `how-sound-is-made` |
| `WAVE-12` | Sound is stored inside an object and gets out. | `s-ladder` | `s-ladder` | `how-sound-is-made` |
| `WAVE-13` | Sound is transverse, because it is drawn as a wavy line. | `s-hook` | `slinky` | `sound-is-longitudinal` |
| `WAVE-14` | In a compression the air travels to your ear. | `slinky` | `s-think` | `sound-is-longitudinal` |
| `WAVE-15` | A longitudinal wave has no amplitude, because there is no hump to measure. | `s-ladder` | `slinky` | `sound-is-longitudinal` |
| `WAVE-16` | A compression is a place where the air is hotter. | *(none — nothing on the page asks for this commitment)* | `slinky` | `sound-is-longitudinal` |
| `WAVE-17` | A loud note is a high note. | `s-hook` | `signal` | `frequency-pitch-and-loudness` |
| `WAVE-18` | A higher note travels faster. | `s-ladder` | `s-think` | `frequency-pitch-and-loudness` |
| `WAVE-19` | Turning the volume up adds vibrations each second. | `signal` | `signal` | `frequency-pitch-and-loudness` |
| `WAVE-20` | A hertz measures how loud something is. | *(none — nothing on the page asks for this commitment)* | `s-think` | `frequency-pitch-and-loudness` |
| `WAVE-21` | Sound crosses a vacuum, faintly. | `s-hook` | `range` | `sound-needs-a-medium` |
| `WAVE-22` | Sound is fastest in air, because air is easiest to get through. | `range` | `range` | `sound-needs-a-medium` |
| `WAVE-23` | A vacuum stops sound because there is nothing for the source to push against. | *(none — nothing on the page asks for this commitment)* | `s-think` | `sound-needs-a-medium` |
| `WAVE-24` | Sound needs air specifically, rather than any material at all. | `s-ladder` | `range` | `sound-needs-a-medium` |
| `WAVE-25` | An echo is a new sound the wall makes. | `s-hook` | `s-think` | `echoes-reflection-and-absorption` |
| `WAVE-26` | Soft materials stop sound travelling. | *(none — nothing on the page asks for this commitment)* | `s-think` | `echoes-reflection-and-absorption` |
| `WAVE-27` | The distance to the cliff is speed × time. | `s-hook` | `your-turn-echo` | `echoes-reflection-and-absorption` |
| `WAVE-28` | A small room gives no echo because there is not enough room for the sound. | `s-ladder` | `cliff` | `echoes-reflection-and-absorption` |
| `WAVE-29` | A dog whistle makes no sound. | `s-hook` | `s-think` | `hearing-and-auditory-range` |
| `WAVE-30` | Losing the top of your hearing range just makes everything a bit quieter. | *(none — nothing on the page asks for this commitment)* | `s-think` | `hearing-and-auditory-range` |
| `WAVE-31` | Ultrasound is a different kind of sound from ordinary sound. | `range` | `range` | `hearing-and-auditory-range` |
| `WAVE-32` | Animals hear better than people do. | `s-ladder` | `range` | `hearing-and-auditory-range` |
| `WAVE-33` | Ultrasound is a special kind of wave that can get through solids where ordinary sound cannot. | `s-hook` | `s-think` | `ultrasound-at-work` |
| `WAVE-34` | A scan works by shining ultrasound through you and seeing what comes out the other side. | *(none — nothing on the page asks for this commitment)* | `s-think` | `ultrasound-at-work` |
| `WAVE-35` | Ultrasound is used because it travels faster than audible sound. | `s-ladder` | `gauge` | `ultrasound-at-work` |
| `WAVE-36` | The gel on the skin is there to help the probe slide about. | `s-ladder` | `s-think` | `ultrasound-at-work` |

### `MATL` — metals and materials: what an order of reactivity is, what it predicts, and the words a material is judged by

Opened by **C9 *Metals and materials*** (2026-08-21, drawn by Claude Design, MRB-281).
`MATL-01` to `MATL-13` are C9's, four lessons, two or three entries each. All are
`review_state: draft`.

⚠️ **THE ROWS BELOW ARE GENERATED FROM `ks3_data/c9/`, NOT FROM NOTES-C9 §6**, for the reason the
`ENER` and `PTAB` sections both give. Four rows differ, and all four are the `rung-2` cause that
`PTAB` met first: NOTES anchors `MATL-02`, `MATL-06` and `MATL-13` on `rung-2` /
`rung-2-feedback`, and the mastery ladder emits neither an `id` nor a `data-activity` per rung, so
none of them resolves. Each is moved to the instrument that actually elicits and confronts the
belief, and every value below is emitted on the page that declares it.

⊖ **`MATL-04`, `MATL-07`, `MATL-10` and `MATL-14` are NOT MINTED.** NOTES-C9 §6 pre-allocates one
spare per lesson under audit law 15. A spare that is never used is an id reserved against nothing,
and ids are permanent once referenced — so they are left unallocated rather than written into this
file, and the numbering below runs 01–03, 05–06, 08–09, 11–13 with the gaps intact. **The gaps are
deliberate and must not be closed up**: renumbering would move `MATL-11` onto a lesson it does not
belong to.

| ID | Statement (as a student holds it) | Elicited by | Confronted by | Lesson |
|---|---|---|---|---|
| `MATL-01` | A metal that does nothing in cold water is unreactive. | `think-commit-water` | `think-commit-water` | `the-reactivity-series` |
| `MATL-02` | Reactivity is the same thing as strength or hardness. | `bench-twelve` | `bench-close` | `the-reactivity-series` |
| `MATL-03` | Carbon cannot belong in an order of metals. | — | `s-series` | `the-reactivity-series` |
| `MATL-05` | Any metal will displace any other if it is left long enough. | `think-commit-time` | `think-commit-time` | `predicting-displacement` |
| `MATL-06` | A less reactive metal can push a more reactive one out of its compound. | `deck-eight` | `deck-close` | `predicting-displacement` |
| `MATL-08` | Metals are in the ground as metal, and extraction is digging and melting. | `hook` | `hook` | `getting-metals-out-of-rocks` |
| `MATL-09` | Any oxide gives up its oxygen to carbon if the furnace is hot enough. | `think-commit-hotter` | `think-commit-hotter` | `getting-metals-out-of-rocks` |
| `MATL-11` | If a material shatters, it must be weak. | `hook` | `hook` | `ceramics-polymers-and-composites` |
| `MATL-12` | Plastic is one material. | `think-commit-plastic` | `think-commit-plastic` | `ceramics-polymers-and-composites` |
| `MATL-13` | Strong and tough are the same property. | `bench-four` | `bench-close` | `ceramics-polymers-and-composites` |

**`MATL-03` has no `elicited_by`, deliberately, and that is audit law 15 working rather than a
hole.** Nothing on `c9-01` asks the student to commit to the belief that carbon does not belong in
an order of metals — the reference list simply presents it, marked "not a metal", with the reason
attached. Inventing an anchor to fill the column would be the dishonest version, and MRB-248 makes
absence legal precisely so that it need not be invented.

**`MATL-02` and `MATL-13` are the unit's spine, and they are the same mistake twice.** One says
reactivity is strength; the other says strength is toughness. Both are *a word from everyday life
doing service as a technical term*, and the unit is arranged so that the student meets the first on
metals and the second on materials — far enough apart that the second is not merely the first
again, close enough that a teacher can name the pattern.

⚑ **`MATL-05` overlaps `PTAB-08`'s neighbourhood in SHAPE ONLY and no cross-reference is
recorded.** Both are wrong beliefs about what a trend permits. But `PTAB-08` is about the DIRECTION
of a trend and `MATL-05` is about whether TIME can defeat one, and a `reappears_in` edge between
them would assert a relationship that does not survive being looked at. The register records
reappearances, not resemblances.

⚑ **`MATL-08` is the one a Year 9 class is most likely to arrive holding**, and it is the only
entry in this family confronted by the HOOK rather than by an instrument — because it is answered
the moment the student is told that half of the green stone is copper and none of it is copper yet.

### `PTAB` — the periodic table: what a column means, what a gap means, and why groups behave alike

Opened by **C8 *The periodic table*** (2026-08-21, drawn by Claude Design, MRB-281).
`PTAB-01` to `PTAB-13` are C8's, seven lessons, one to three entries each. All are
`review_state: draft`.

⊕ **`PTAB-11` to `PTAB-13` arrived on 23 August 2026 with `c8-07`**, the oxides
lesson, which closed `KS3.C.PT.06` — the last uncovered statutory statement in
C1–C8. `PTAB-11` is the load-bearing one of the three and is described below the
table.

⊖ **`PTAB-14` IS A NAMED SPARE, RESERVED FOR C9, AND HAS NO ROW.** NOTES-C8 §8
allocated `PTAB-11`–`PTAB-14` to `c8-07` and reserved the fourth against C9's
reactivity work, per §5.3. It is recorded here in prose and deliberately NOT in
the table below, because a row is a claim that some authored lesson references
the id and `ks3_parity.check_misconception_register` asserts exactly that in
both directions — a row for an id no lesson names is a broken join, and naming
it in `c8-07` to satisfy the row would create a live entry with no confrontation,
which is Law 3's own failure. This is the `EARTH-18` shape: the number is held
without being spent. It is **not yet minted** and it is **not** a permanent gap —
C9 may take it, and until it does, nothing else may.

⚠️ **THE ROWS BELOW ARE GENERATED FROM `ks3_data/c8/`, NOT FROM NOTES-C8 §6, AND THEY DIFFER FROM
IT IN SIX PLACES.** NOTES proposed the ids a delivery *expects* to emit; these are the names the
pages *do* emit, checked against the renderers in `ks3_art/c8.py`. Writing NOTES' names here would
reproduce exactly the defect this file was repaired for under `MIX` — a register recording intent
rather than fact.

The six differences fall into the two causes C7's section predicted would recur, and both did.

**Cause one, four rows: no `think-reveal-*` id can be emitted from a content lane.**
NOTES-C8 §6 proposes `think-reveal-graphite`, `think-reveal-predictions`,
`think-reveal-sodium-chlorine`, `think-reveal-exothermic` and `think-reveal-full-shell`.
`build_ks3.py`'s shared `r_activity` draws a confrontation's reveal with **no `id`**, and
`build_ks3.py` is not a file a lane may touch, so none of them can be made to resolve. Each join
names the ACTIVITY that owns both the commitment and the reveal instead — the `MIX-06` form, and
the one that satisfies Law 3.

**Cause two, and it is NEW: `rung-2` and `rung-2-feedback` are not emitted either.** NOTES-C8 §6
anchors `PTAB-02` and `PTAB-06` on the mastery ladder. The ladder draws no per-rung `id` and no
`data-activity`, so both values name a real place in the author's head and no element in the
document — the MRB-244 defect exactly. Both joins are moved to instruments that DO render and DO
confront the belief:

* `PTAB-02` — the bench on c8-01 elicits it (sample C is a liquid the student must judge) and the
  bench's own closing panel confronts it by name: *"Mercury is a metal that is liquid."* The panel
  id `bench-close` is authored on the payload, so the register and the markup have one source.
* `PTAB-06` — the periodic table on c8-03 elicits it (every square prints an atomic number beside
  a group number) and its closing panel `table-close` confronts it: *"The group number is not how
  many electrons the atom has."*

⚠️ **`PTAB-10` is anchored on the whole `uses-three` block rather than on a card.**
`r_predict_cards` gives each card a `data-pcard-card` value, which is neither an `id` nor a
`data-activity`, so a card-level join would not resolve. The block is the right grain anyway: all
three cards are somebody paying money for a gas BECAUSE it does nothing.

| ID | Statement (as a student holds it) | Elicited by | Confronted by | Lesson |
|---|---|---|---|---|
| `PTAB-01` | If it conducts electricity it must be a metal. | `think-commit-conduct` | `think-commit-conduct` | `metals-and-non-metals` |
| `PTAB-02` | A liquid element cannot be a metal. | `bench-six` | `bench-close` | `metals-and-non-metals` |
| `PTAB-03` | Mendeleev's table was accepted because it was tidy. | `think-commit-tidy` | `think-commit-tidy` | `mendeleev` |
| `PTAB-04` | A gap in a table is a weakness in it. | `rules-three` | `rules-three` | `mendeleev` |
| `PTAB-05` | Elements next to each other in the table are similar. | `think-commit-neighbours` | `think-commit-neighbours` | `groups-and-periods` |
| `PTAB-06` | The group number tells you how many electrons the atom has altogether. | `table-twenty` | `table-close` | `groups-and-periods` |
| `PTAB-07` | Sodium melted because the water was hot. | `think-commit-melt` | `think-commit-melt` | `group-1-the-alkali-metals` |
| `PTAB-08` | Reactivity always increases going down a group. | `grid-nine` | `grid-close` | `group-7-the-halogens` |
| `PTAB-09` | The noble gases are unreactive because they are gases. | `think-commit-gas` | `think-commit-gas` | `group-0-and-why-groups-exist` |
| `PTAB-10` | Unreactive means useless. | `uses-three` | `uses-three` | `group-0-and-why-groups-exist` |
| `PTAB-11` | The copper oxide left the pH at 7, so it cannot be a base. | `think-commit-basic` | `think-commit-basic` | `metal-and-non-metal-oxides` |
| `PTAB-12` | Alkaline and basic mean the same thing. | `think-commit-basic` | `think-commit-basic` | `metal-and-non-metal-oxides` |
| `PTAB-13` | All oxides dissolve in water. | `bench-six-oxides` | `bench-pattern` | `metal-and-non-metal-oxides` |

**`PTAB-08` is the unit's load-bearing entry, and it is the only one in the register that is
created by the PREVIOUS lesson.** c8-04 establishes "reactivity increases going down a group" on a
water trough the student runs three times, and c8-05 hands them a grid where it runs the other way.
The belief is not a mistake the student brings — it is one the course teaches them and then breaks,
on purpose, one lesson apart. §7's plan merged those two lessons into one; the merge was rejected
for this row (MRB-281, R1), because a trend and its reversal in a single lesson is a paragraph
rather than a surprise.

⚑ **`PTAB-07` reappears from `ENER-03`** (C7, *exothermic reactions*): both are heat coming OUT of
a reaction being read as heat that went IN. They are elicited by different phenomena — a Bunsen you
had to light against a metal that melted itself — and a student can hold either without the other,
so they stay separate. The cross-reference is recorded as a `reappears_in` edge on `ENER-03`'s own
record, pointing at `group-1-the-alkali-metals`; see the ⊕ note in the `ENER` section above for why
it is an edge and not this paragraph.

⊕ **`PTAB-11` is the entry the oxides lesson is built around, and `PTAB-12` is
the same belief with the case taken out.** `PTAB-11` is written concretely
because `_misconception_quote` prints the statement of whatever id the activity
`targets` as the amber block's quote — so this row IS the sentence on the page,
and it is Design's own. `PTAB-12` is the abstract form and is confronted by the
last paragraph of the same reveal, which does nothing else: *"Basic is what a
substance does to an acid. Alkaline is a description of a solution."* They are
kept separate on the `PTAB-02` / `PTAB-06` argument — a student can hold either
without the other, and a student who has never met the word `basic` outside the
phrase `basic solution` holds only the second.

⚠️ **`PTAB-13` is anchored on the BENCH and confronted by the bench's own
closing panel**, `bench-pattern`, not by the think block. It is the `PTAB-02`
form: the tray holds two oxides that dissolve completely, one that dissolves a
little, one that does not dissolve at all and two that are not solids in the
first place, so the belief is contradicted by the instrument the student worked
rather than by a sentence about it. `bench-pattern` is authored as `close_id`
on the payload, so the register and the markup have one source.

⚑ **`PTAB-02` and `PTAB-06` are cousins and are worth keeping separate.** One reads a state of
matter as settling a classification, the other reads one of two printed numbers as if it were the
other. Both are "a single fact is being asked to do more work than it can", which is the spine of
this whole unit — the same shape as `PTAB-01`, which is why c8-01 carries two of the three.

### `ACID` — acids, alkalis and the pH scale: what the words mean, what the scale measures, and what a catalyst does

Opened 21 August 2026 by C6, on Design's own proposal in NOTES-C6 §6 and on her own reasoning:
*"`REACT` is reaction types. These are about acids, alkalis and rates, and they need their own
family."* That is right, and the family is opened rather than the entries pushed into `REACT`,
because `REACT-01`…`REACT-18` are about what a reaction IS and these are about what two words on
a bottle mean.

⚠️ **THE FAMILY IS OPENED BEFORE C9, WHICH IS WHAT DESIGN ASKED FOR.** NOTES-C6 §6: *"Rule on
the prefix before C9, which will want to cross-reference `ACID-07`."* C9's `the-reactivity-series`
and `predicting-displacement` both argue from where a metal sits relative to hydrogen, and
`ACID-07` is the entry that owns the belief they have to defeat. It now has a permanent id to be
cross-referenced by.

⊕ **`ACID-08` IS LIVE AS OF 23 Aug 2026 (MRB-281).** The paragraph below is kept because it is an
instruction to leave the id empty, and following it now would delete a shipped join.

> ⚠️ **`ACID-08` IS DELIBERATELY UNUSED AND MUST STAY UNUSED.** Design's §6 assigns it to
> *"A gas that puts out a splint is carbon dioxide"*, on `acids-and-carbonates` — the lesson she
> drew into `structure.py`'s `acid-plus-alkali` slot and flagged herself for a ruling. The
> commander ruled that slot stays unauthored, so the belief has no page that elicits it and no page
> that confronts it, and an entry naming neither would fail MRB-244/248 the moment anything checked
> it. The number is left as a gap rather than the nine that follow being renumbered: **IDs are
> permanent, including the ones that never shipped.** If `acid-plus-alkali` is ever authored with
> the limewater test in it, `ACID-08` is waiting and means what Design said it means.

Mide overrode the retirement on 23 Aug 2026 and `acids-and-carbonates` is built — into that same
slot, renamed in place from `acid-plus-alkali` rather than added beside it. So the last sentence
above is what happened, exactly as written: **the id was waiting and means what Design said it
means.** It was never reissued, never renumbered, and its statement is unchanged from her §6 table.
That is the permanent-gap law working rather than being tested — an id held empty for two days is
the same thing as an id held empty for two years.

Its joins take the same repair as the other six `think-*` entries in this family: Design's proposed
`think-reveal-specificity` is unreachable, because the `#s-think` reveal panel is drawn by
`build_ks3.py`'s shared `r_activity` and carries no `id`. Both columns name `think-commit-splint`,
the activity that holds the commitment AND the two confronting paragraphs.

⚑ **`ACID-08` IS STILL THE ENTRY THAT WOULD JOIN `NOS` FIRST**, and Design says why: *"`ACID-08`
is `NOS`-shaped — it is about what counts as a specific test, not about carbonates."* She is right,
and its lesson now argues exactly that in prose — *"A good test has one answer. A test that dozens
of substances could pass is not evidence."* Nothing here opens `NOS` or moves anything into it. The
ruling stands from MRB-246 and from C7's notes: whether `NOS` absorbs entries out of content
families changes permanent ids across several units at once, and the next pass takes the parked
list together with the principle written down. **C6 adds one to that parked list**, where before it
added none — the sentence below the old paragraph said C6 added nothing "because the one entry that
would have joined it was never authored", and that is the half that has changed.

⚠️ **TWO JOINS ARE NOT DESIGN'S PROPOSED NAMES, AND BOTH CHANGES ARE FORCED.** MRB-244/248 resolve
`elicited_by` and `confronted_by` against the BUILT page, where the only legal names are `id="…"`
and `data-activity="…"`.

  · Every `think-reveal-*` name in §6 is unreachable. The `#s-think` reveal panel is drawn by
    `build_ks3.py`'s shared `r_activity`, which emits no `id`, and `build_ks3.py` is not a file a
    content lane may touch. Six entries therefore name the ACTIVITY that holds both the commitment
    and the two confronting paragraphs — the `c4-01` / `c5-02` reconciliation, and what satisfies
    Law 3's requirement for a real activity id.
  · `ACID-04`'s `rung-2` / `rung-2-feedback` are unreachable for the same reason: `r_ladder`
    numbers its rungs and gives them no id. It names `s-ladder`, the section that holds rung 2 and
    its correction — which is exactly the repair MRB-244 made for `b2-02`'s `BODY-06`.
  · `ACID-06`'s `titration-dial` is a FAMILY name rather than a DOM id. It names `s-titrate`, the
    section the dial is in, where the student commits by adding drops and watching the reading
    crawl. Its `confronted_by`, `curve-reveal`, is Design's own and IS emitted — authored on the
    instrument's payload rather than composed in the renderer, so the register and the markup have
    one source.
  · `ACID-02`'s `judgement-1` / `judgement-1-reveal` are renamed to `judgement-dilute` /
    `judgement-dilute-reveal` and both ARE emitted. A positional name is wrong the moment a
    judgement is inserted above it.

| ID | Statement (as a student holds it) | Elicited by | Confronted by | Lesson |
|---|---|---|---|---|
| `ACID-01` | Acids are the dangerous ones. Alkalis are what you use to make things safe. | `think-commit-danger` | `think-commit-danger` | `acids-and-alkalis` |
| `ACID-02` | A dilute acid is no longer really an acid. | `judgement-dilute` | `judgement-dilute-reveal` | `acids-and-alkalis` |
| `ACID-03` | pH 2 is twice as acidic as pH 4 — it is half the number, so it is double the strength. | `think-commit-scale` | `think-commit-scale` | `the-ph-scale-and-indicators` |
| `ACID-04` | More indicator gives a different pH reading. | `s-ladder` | `s-ladder` | `the-ph-scale-and-indicators` |
| `ACID-05` | Neutralising an acid destroys it; only water is left. | `think-commit-gone` | `think-commit-gone` | `neutralisation` |
| `ACID-06` | The pH climbs steadily as alkali is added. | `s-titrate` | `curve-reveal` | `neutralisation` |
| `ACID-07` | The bubbles are the metal turning into gas. | `think-commit-fizz` | `think-commit-fizz` | `acid-plus-metal` |
| `ACID-08` | A gas that puts out a splint is carbon dioxide. | `think-commit-splint` | `think-commit-splint` | `acids-and-carbonates` |
| `ACID-09` | Boiling a solution dry gives the best crystals. | `think-commit-boil` | `think-commit-boil` | `making-a-pure-dry-salt` |
| `ACID-10` | A catalyst is used up slowly, which is why it wears out. | `think-commit-consumed` | `think-commit-consumed` | `catalysts` |

**`ACID-01` is the unit's load-bearing entry.** "Acidic" and "dangerous" are the same word to most
twelve-year-olds, and every hazard film they have seen confirms it. C6's answer is not to
contradict it but to build the evidence first: `c6-01`'s eight-bottle bench puts four things a
student eats or drinks on one side and the cleaning cupboard on the other, tags each with where it
lives, and only opens its closing panel on the eighth bottle. By the time `#s-think` quotes the
belief, the student has already produced the distribution that refutes it. Nothing on that page may
be justified by "acids are the safe ones either", including the stretch layer, or the lesson
confirms the mirror image of what it breaks.

**`ACID-03` is the most-repeated misconception in the topic**, and it is the reason `c6-02` states
the factor of ten explicitly at KS3 rather than deferring it (NOTES-C6 §5 flag 4, ruled and kept).
The scale looks like an ordinary number line and nothing about the printed chart says otherwise, so
the page says it: the strip's own note reads "Every step of one is a factor of ten", the `#s-think`
reveal works it through to ten thousand, and the question bank's e04, s02, h01 and h04 each offer a
different wrong arithmetic on the same two readings — subtract them, divide them, rank them.

**`ACID-10` is the one whose real-world counter-example is TRUE.** Catalytic converters do stop
working, and a student who has noticed that is reasoning correctly from a real observation. The
confrontation cannot deny the observation and does not: it separates POISONED from CONSUMED, weighs
the platinum in a dead converter and finds it all there, and lands on "blocked is not the same as
consumed". MRB-225 applies squarely — the version that is true is more interesting than the version
that is famous, and nothing in `c6-07` retracts the definition it opened with.

---

### `EARTH` — the Earth and its atmosphere: what a fixed stock is, what a loop actually returns, and what a "reserve" is a fact about

Opened by **C10 *The Earth and its atmosphere*** (2026-08-22, drawn by Claude Design, MRB-281).
`EARTH-01` to `EARTH-17` are C10's, six lessons, two or three entries each. All are
`review_state: draft`.

⊕ **THE UNIT IS COMPLETE AND THE RANGE IS CLOSED AT `EARTH-17`.** All six lessons are authored,
so all seventeen rows are below. The allocation, kept because it is what stopped six lanes
colliding on a number: `EARTH-01`–`04` are c10-01's, `05`–`07` c10-02's, `08`–`10` c10-03's,
`11`–`13` c10-04's, `14`–`15` c10-05's, and `16`–`17` c10-06's. **An id appears in the table below
only when the lesson that references it exists** — registering ahead of authoring is legal
(`CELL-09`–`12` are the live example) but allocating a block and then filling it is how a number
ends up meaning two things.

⊖ **`EARTH-17` IS SPENT. `EARTH-18` IS THE SOLE REMAINING SPARE AND IS NOT MINTED.** Both were
reserved against a lesson needing a further entry, in exactly the sense `MATL-04/07/10/14` were
pre-allocated and then deliberately left unallocated. `c10-06` needed one and took `17`; the
justification is with the row. `EARTH-18` stays unwritten — a spare that is never used is an id
reserved against nothing, and ids are permanent once referenced, so with the unit finished the
numbering stops at 17. **Do not close the gap and do not mint 18.**

| ID | Statement (as a student holds it) | Elicited by | Confronted by | Lesson |
|---|---|---|---|---|
| `EARTH-01` | The mantle is a sea of molten lava, and volcanoes are holes that let it out. | `think-commit-mantle` | `think-reveal-mantle` | `inside-the-earth` |
| `EARTH-02` | Nobody has ever been down there, so what is inside the Earth is really only a guess. | `s-hook` | `s-evidence` | `inside-the-earth` |
| `EARTH-03` | Anything that hot must be melted, so the hottest part of the Earth is liquid. | — | `s-layers` | `inside-the-earth` |
| `EARTH-04` | The crust is a thick shell, and mines and boreholes have been most of the way through it. | — | `s-layers` | `inside-the-earth` |
| `EARTH-05` | If a rock has crystals in it, it must be igneous. | `think-commit-crystals` | `think-reveal-crystals` | `three-ways-to-make-a-rock` |
| `EARTH-06` | Rocks are grouped by what they look like, so two rocks that look alike are the same kind of rock. | `s-hook` | `bench-pattern` | `three-ways-to-make-a-rock` |
| `EARTH-07` | Metamorphic rock is rock that was melted and then set again as something new. | — | `bench-samples` | `three-ways-to-make-a-rock` |
| `EARTH-08` | Sedimentary rock becomes metamorphic, and metamorphic becomes igneous. It goes round one way, like a clock. | `think-commit-direction` | `think-reveal-direction` | `the-rock-cycle` |
| `EARTH-09` | A rock has to go through every stage of the cycle in turn, so nothing can become sedimentary without melting first. | — | `process-arrows` | `the-rock-cycle` |
| `EARTH-10` | A rock is a permanent thing, so the stone and the mountains around us have always been what they are now. | `s-hook` | `grain-order` | `the-rock-cycle` |
| `EARTH-11` | If we recycled everything, we would never run out of anything. | `think-commit-recycling` | `think-reveal-recycling` | `a-planet-with-limits` |
| `EARTH-12` | How much comes back depends on how carefully people sort their bins. | `loop-bench` | `loop-bench` | `a-planet-with-limits` |
| `EARTH-13` | “Years left” is a measured fact about how much is in the ground. | — | `s-stock` | `a-planet-with-limits` |
| `EARTH-14` | Air is mostly oxygen — that is the point of it. | `think-commit-oxygen` | `think-reveal-oxygen` | `whats-in-the-air` |
| `EARTH-15` | The air has always been roughly like this, so the oxygen was there from the start. | — | `s-history` | `whats-in-the-air` |
| `EARTH-16` | The planet is warming because of the hole in the ozone layer letting extra heat in. | `think-commit-ozone` | `think-reveal-ozone` | `carbon-dioxide-humans-and-climate` |
| `EARTH-17` | The greenhouse effect is the problem — it is what is causing the planet to warm. | — | `s-hook` | `carbon-dioxide-humans-and-climate` |

**`EARTH-01` is the one this whole topic turns on, and it is the reason `c10-01` refuses the famous
sentence.** A thin crust floating on a sea of magma is taught in a great many classrooms and it is
wrong, and the evidence three blocks above the confrontation is what makes it wrong: the earthquake
wave that cannot cross liquid crosses the entire mantle. The reveal carries
`id="think-reveal-mantle"` so `confronted_by` names the PANEL where the belief is answered rather
than the surrounding section — the MRB-277 pattern. What the reveal separates is SOLID from RIGID,
because a student who has been told the mantle moves has usually concluded it must be liquid, and
they are reasoning correctly from a true observation (MRB-225: the true version, not the famous
one).

**`EARTH-02` is elicited by the hook's fourth option, which offers the belief in plain words.** "So
how do we know what the inside is made of?" is a real question, and "Nobody knows; it is a guess"
is a real answer a twelve-year-old will pick — the honest form of it, from a student who has just
been told that the deepest hole ever drilled is two tenths of one per cent of the way down.
`confronted_by` is `s-evidence` rather than the hook's own reveal: the hook says the answer came
from earthquake waves, and saying so is not yet showing it. The evidence block makes the student
commit to three separate inferences and then walks each one, which is what turns "scientists say
so" into "here is how anyone could tell".

**`EARTH-03` and `EARTH-04` carry no `elicited_by`, deliberately, and that is audit law 15 working
rather than a hole.** Nothing on `c10-01` asks a student to commit to either belief. The inner-core
panel simply prints "About 5500 °C" and "Solid" in adjacent cards and lets the pair do the work;
the bar simply draws the crust at its real share and prints that share as a number underneath.
Inventing an anchor to fill the column would be the dishonest version, and MRB-248 makes absence
legal precisely so that it need not be invented. The question bank carries the elicitation instead
— `c10-01-e02` and `c10-01-h02` for `EARTH-03`, `c10-01-e01` and `c10-01-s04` for `EARTH-04`.

⚑ **`EARTH-04` IS ALSO WHY THE BAR ADMITS ITS OWN DISTORTION.** The crust is 0.5% of the distance
to the centre, which on a phone is under four pixels and is not a tappable target, so the segment
carries a minimum width. A page that exaggerates the crust and says nothing is teaching the
misconception it has just listed. The scale panel therefore prints the true share as a derived
number and says the bar is drawn wider than it, and `ks3_art/c10.py` refuses a scale panel that
does not name that number.

**`EARTH-05` is the belief Design quotes in her own words at `#s-think`, and it is the one a
student arrives with.** Crystals really do grow when molten rock cools, so the belief is a correct
observation over-extended into a rule — which is the shape that survives being told it is wrong and
has to be broken by a counter-example instead. Marble is that counter-example: packed with
interlocking crystals, and it never melted. The reveal carries `id="think-reveal-crystals"` so
`confronted_by` names the PANEL where the belief is answered rather than the surrounding section —
the MRB-277 pattern. What the reveal is careful NOT to say is that crystals mean metamorphic: it
says crystals narrow the answer to two and no further, because a lesson that replaces one
one-clue rule with another has taught the same mistake in a new colour.

**`EARTH-06` is elicited by the hook and confronted by the panel the bench opens at the end.** The
hook puts a granite worktop beside a marble statue — both hard, both shiny, both full of crystals —
and offers "That it is an igneous rock" as an option a student can pick on the look of the thing.
It is confronted at `bench-pattern` rather than at the hook's own reveal because by then the
student has decided six samples themselves, and the panel can say what actually settled each one:
not colour, not hardness, not weight, but texture, layers, fossils and how the rock breaks. Two of
the six are the same chemical compound as each other and are in different groups, and neither that
count nor the size of the set is typed anywhere — `ks3_art/c10.py` derives both from the samples'
own `compound` values and refuses to build a bench in which the sharers land in one group.

**`EARTH-07` carries no `elicited_by`, deliberately, and that is audit law 15 working rather than a
hole.** Nothing on `c10-02` asks a student to commit to the belief that metamorphic rock was melted
and re-set; the bench simply hands them a marble and a slate and says, in the verdict of each, that
it never melted. Inventing an anchor to fill the column would be the dishonest version, and MRB-248
makes absence legal precisely so that it need not be invented. The question bank carries the
elicitation instead, at `c10-02-s02` and `c10-02-h01`. ⚑ This is also the entry that decides the
whole classification: melt a metamorphic rock and what cools out of it is igneous, which is why
"without melting" appears in the reference panel, the key fact and the key note and is contradicted
nowhere.

**`EARTH-08` is the one `c10-03` is built to break, and it is the belief Design quotes in her own
words at `#s-think`.** The rock cycle in the front of every textbook is a ring with arrows drawn one
way round, and a student who has only ever seen that diagram holds it as an ORDER: sedimentary
becomes metamorphic, metamorphic becomes igneous, round and round like a clock face. What is true is
that there are arrows across the middle as well as round the edge, and that the route is decided by
where the rock ends up rather than by what it currently is — at the surface, weathering; buried
deep, heat and pressure; deeper and hotter still, melting. The confrontation is the reveal directly
under the commitment, and the reason the page carries no rock-cycle diagram at all is that shipping
the ring would hand the student the belief and then take it away eight blocks later.

⚠️ **`EARTH-08` IS ALSO WHY `#s-journey` IS FENCED.** The sequencer walks one grain through seven
stages in a fixed order, which is the one block on the page that could be read as confirming the
belief. It is closed twice: the panel's closing sentence says the journey starts again *because the
granite at the end is the granite at the beginning*, and `#s-think` is the very next rail stop. The
order is a journey one grain took, never the order every rock takes.

**`EARTH-09` carries no `elicited_by`, deliberately, and that is audit law 15 working rather than a
gap.** Nothing on the page asks a student to commit to "every rock must pass through every stage" as
a belief in its own right — `#s-think`'s four options are about DIRECTION, which is `EARTH-08`, and
inventing an anchor to fill the column would be the dishonest version. What confronts it is the
reference block: three of the six processes declare an input that is ANY rock in the right place
(`any rock at the surface`, `any buried rock`, `any rock, deep and hot enough`), which is the
skipping stated as a payload rather than as a sentence. The question bank carries the elicitation
instead, at `c10-03-s02` and `c10-03-h01`.

**`EARTH-10` is elicited by the hook and confronted by the sequencer.** Three of the hook's four
options offer a way for marine limestone to be sitting at 8800 metres without the rock itself having
changed — birds carried the fossils, the sea used to be that high, limestone forms anywhere. Each
one preserves the rock as a fixed thing and moves something else instead, which is exactly how the
belief survives contact with the evidence. What kills it is following one grain all the way round
and finding it in seven different rocks, the last of which is the first.

⚑ **`EARTH-10` and `EARTH-06` are neighbours and are not the same belief.** `EARTH-06` is about
CLASSIFICATION — two rocks that look alike must be the same kind — and it dies on a bench where
colour and hardness decide nothing. `EARTH-10` is about PERMANENCE, and it dies on a journey. A
student can hold either without the other, and `c10-02` needs the first while `c10-03` needs the
second.

**`EARTH-11` is the unit's load-bearing entry, and the page breaks it with arithmetic rather than
with an assertion.** By the time `#s-think` quotes the belief, the student has run 1000 kg round
the loop for at least three materials and watched the bars shrink every pass; aluminium at nine
collected in ten reaches 6.90 lifetimes per kilogram of ore, not infinite lifetimes. The reveal
carries `id="think-reveal-recycling"` so `confronted_by` names the PANEL where the belief is
answered rather than the surrounding section — the MRB-277 pattern.

**`EARTH-12` is elicited and confronted by the same instrument, which is unusual and is the point.**
The bench is the only place on the page where collection is held equal and the material is the only
thing that changes: nine in ten collected gives aluminium 6.90× and the crisp packet 1.02×. A
student holding this belief presses the packet expecting the dial to rescue it, and the verdict
sentence for that state says so in words — "collection is not the problem here, the material is".
No separate confrontation block would be as convincing as the one the student ran themselves.

**`EARTH-13` has no `elicited_by`, deliberately, and that is audit law 15 working rather than a
hole.** Nothing on `c10-04` asks the student to commit to the belief that a reserve is a measured
quantity of rock; the shelf and the going-further layer simply say what a reserve is — the part of
a resource that can be extracted at a profit with today's technology — and let the definition do
the work. Inventing an anchor to fill the column would be the dishonest version, and MRB-248 makes
absence legal precisely so that it need not be invented. The question bank carries the elicitation
instead, at `c10-04-h01`, where a country's copper reserves rise by a fifth with no new deposit
found.

**`EARTH-14` is the belief Design quotes in her own words at `#s-think`, and it is the one this
whole page is built to break.** "Air is mostly oxygen — that is the point of it" is not a careless
answer; it is a student reasoning correctly from a true premise. Oxygen IS the gas a body needs, it
IS the gas without which nothing burns, and it is the only one of the four that gets talked about.
Concluding that there must be most of it is the obvious next step, and it is wrong by a factor of
four. The hook elicits it first, in plain words — "Roughly what fraction of the air is oxygen?" with
"Almost all of it" and "About three quarters" both on offer — and `#s-think` is where the student
has to commit to it as a BELIEF rather than as a guess about a number. The reveal carries
`id="think-reveal-oxygen"` so `confronted_by` names the PANEL where the belief is answered rather
than the surrounding section — the MRB-277 pattern.

⚑ **What the reveal does NOT do is treat the nitrogen as filler**, and that is the difference
between correcting the number and correcting the belief. A student told "actually it is 78 per cent
nitrogen" has learned a swap. The reveal instead says what the nitrogen is FOR: in pure oxygen
everything that can burn burns ferociously, and the nitrogen dilutes the oxygen to a level at which
fire is possible but not automatic. Then it closes at the other extreme — carbon dioxide is 0.04 per
cent of the air and every plant on Earth is built out of it — because the belief underneath
`EARTH-14` is that "how much there is" and "how much it matters" are the same measurement, and one
end of the bar cannot break that on its own.

**`EARTH-15` carries no `elicited_by`, deliberately, and that is audit law 15 working rather than a
hole.** Nothing on `c10-05` asks a student to commit to the belief that the oxygen was always there.
Design's history block is a stepper — it reveals, it does not ask — and inventing an anchor to fill
the column would be the dishonest version. MRB-248 makes absence legal precisely so that it need not
be invented. The question bank carries the elicitation instead, at `c10-05-s02`, where rocks older
than two and a half billion years hold minerals that could not have survived in oxygen, and at
`c10-05-h01`, where photosynthesis has been running for three hundred million years and the air
still has none.

⚑ **`EARTH-15` and `EARTH-10` are neighbours and are not the same belief.** `EARTH-10` is about
ROCK being permanent and it dies on a journey round the cycle. `EARTH-15` is about the AIR being a
fixed backdrop that living things arrived into, and what kills it is the discovery that living
things made it. A student can hold either without the other, and joining them would blur the thing
C10's last two lessons add: that the atmosphere is not scenery, it is a product, and it is still
being changed.

**`EARTH-16` is the belief Design quotes in her own words at `#s-think`, and it is the single most
common error in this topic anywhere in the country.** Ozone depletion and the greenhouse effect are
two real problems with the atmosphere, they arrived in public conversation within a few years of
each other, and both are spoken about as "damage to the atmosphere" — so a student who merges them
is doing something reasonable with the evidence they have. They are not the same thing in any
respect that matters: different gas, different altitude, different radiation, different
consequence, and largely different solutions. Ozone blocks ULTRAVIOLET coming IN; the greenhouse
effect is about INFRARED going OUT. Ozone depletion does not "let the heat in" and never did.

The predict elicits the belief in plain words before the page says anything, and the reveal carries
`id="think-reveal-ozone"` so `confronted_by` names the PANEL where the belief is answered rather
than the surrounding section — the MRB-277 pattern.

⚑ **The confrontation ends on the ozone problem being the one humanity actually FIXED, and that
sentence is doing two jobs.** It is the reason the two are worth keeping apart — one has a treaty
and a recovering layer behind it and the other does not — and it is the page's only worked example
of an atmospheric problem being identified, understood, legislated against and reversed. The
lesson's safeguarding ruling (in `ks3_data/c10/lesson_06_*.py`) turns on that sentence being
science rather than reassurance, which it is: the Montreal Protocol was signed in 1987 and the
layer is measurably recovering.

**`EARTH-17` was one of the two NAMED SPARES, and this is why it was spent.** The belief is that
the greenhouse effect is itself the problem — that the thing to be got rid of is the effect rather
than the increase in it. It is not a careless answer. A student meets the phrase "the greenhouse
effect" exclusively in sentences about something going wrong, and concluding that the effect is the
wrong thing is the obvious next step. It is also completely wrong in the most consequential
direction available: without the natural effect the surface would average about −18 °C instead of
about 15 °C, and the oceans would be ice.

It earns an id rather than a paragraph because `c10-06` is BUILT around it. Design's hook is the
thirty-three degrees the effect already provides; her second ladder rung asks "Is the greenhouse
effect a bad thing?" directly; and the lesson adds a key fact of its own (`natural-and-enhanced`)
whose only job is to hold "natural and necessary" and "we have strengthened it" in the same
sentence. Four separate places on one page, which is the definition of a belief a lesson is built
to break rather than a slip a distractor can handle.

**`EARTH-17` carries no `elicited_by`, deliberately, and that is audit law 15 working rather than a
hole.** Nothing on `c10-06` asks a student to commit to it — the hook asks where the warmth comes
from, not whether it is welcome — and inventing an anchor to fill the column would be the dishonest
version. MRB-248 makes absence legal precisely so that it need not be invented. `confronted_by` is
`s-hook`, where the reveal says the planet would be frozen without it and then names the real
question. The bank carries the elicitation, at `c10-06-e02` and `c10-06-s01`.

⚑ **THREE MORE BELIEFS ARE CORRECTED ON `c10-06` AND NONE OF THEM IS MINTED, which is a decision
rather than an omission.** The page also handles "water vapour does most of it, so carbon dioxide
cannot be the cause", "two graphs rising together proves one causes the other", and "it was
freezing last week, so the planet is not warming". Each is corrected in the place it arises — an
explainer in the main flow, the evidence block's derived closing panel, and the vocabulary
definition of "climate", which is written AGAINST weather rather than beside it — and each is
elicited in the question bank at `c10-06-s02`, `s03` and `s04`.

They are not register entries because the register names the beliefs a page is BUILT to break, and
`c10-06` is built on two. A page with five declared misconceptions has stopped having a spine, and
`EARTH-18` is the only spare left in the range: spending it on the third-most-important belief on
one page would leave the next lane with nothing and would say that these three are the same kind of
thing as the ozone conflation. They are not. A student can be talked out of the water-vapour
argument in one sentence; the ozone conflation survives being told it is wrong, which is what a
misconception entry is for.

⚑ **`EARTH-16` and `EARTH-17` are neighbours and are not the same belief.** `EARTH-16` is about
which PROBLEM is happening and it dies when the two mechanisms are laid side by side. `EARTH-17` is
about whether the mechanism this page teaches is a good thing, and what kills it is the thirty-three
degrees. A student can hold either without the other — the commonest combination in a real class is
to have both — and joining them would blur the one thing this lesson has to leave behind: that the
greenhouse effect is not the problem, the change to it is, and neither of them is the ozone hole.

⚑ **`EARTH-11` overlaps `MATL-08`'s neighbourhood in SHAPE ONLY and no cross-reference is
recorded.** Both are wrong beliefs about where a material comes from. But `MATL-08` is about
EXTRACTION — metals are in the ground as metal, so getting them out is digging and melting — and
`EARTH-11` is about RETURN, and specifically about a loop the student believes is closed. A student
can hold either without the other, and joining them would blur the one thing C10 adds to C9: that
the interesting number is not what it costs to get a material out but what fraction of it ever
comes back.

### `LIGHT` — light

⊕ **OPENED 25 Aug 2026, BY P7.** `docs/ks3/design-reference/p7/NOTES-P6-P7.md` §7 pre-allocated `LIGHT-01` … `LIGHT-28`, four per
lesson in slot order, and authored FOURTEEN of them without citing one on any page — because access was read-only and this register
had no open family for light. **Every id she wrote is minted here on the number she gave it.** The fourteen gaps are minted from the
real lesson content, which is the register's own rule: an id is minted from what a page actually confronts, never reserved against
what one might.

⚠️ **HER STATEMENTS ARE TAKEN FROM THE PAGE, NOT FROM THE NOTES, WHERE THE TWO DIFFER.** Both are hers, and the page's wording is
the sentence a student actually meets — her `#s-think` quote is what appears in quotation marks in front of them. So `LIGHT-01` is
*"Light is instant — it takes no time at all"* rather than the notes' shorter *"Light is instant"*, and the same choice is made on
`LIGHT-02`, `LIGHT-06`, `LIGHT-09`, `LIGHT-10`, `LIGHT-13`, `LIGHT-18`, `LIGHT-21` and `LIGHT-25`. This is the `WAVE-33` / `WAVE-34`
precedent, applied on the way in rather than as a correction.

| ID | Statement, as a student holds it | Elicited by | Confronted by | Lesson |
|---|---|---|---|---|
| `LIGHT-01` | Light is instant — it takes no time at all. | `s-hook` | `s-think` | `light-travels` |
| `LIGHT-02` | Space is empty, so light has nothing to travel in and must be slowed down by it. | `s-ladder` | `s-think` | `light-travels` |
| `LIGHT-03` | Light is longitudinal, like sound is. | *(none — nothing on the page asks for this commitment)* | `light-vs-waves` | `light-travels` |
| `LIGHT-04` | The thunder is made a moment after the flash, so the two did not start together. | `s-hook` | `s-hook` | `light-travels` |
| `LIGHT-05` | Rough surfaces break the law of reflection. | `ray` | `s-think` | `reflection-mirrors-and-scattering` |
| `LIGHT-06` | Angles in reflection are measured from the mirror. | `s-ladder` | `s-think` | `reflection-mirrors-and-scattering` |
| `LIGHT-07` | The mirror sends back far more light than the paper does. | `s-hook` | `ray` | `reflection-mirrors-and-scattering` |
| `LIGHT-08` | Only shiny surfaces can reflect light. | `s-ladder` | `ray` | `reflection-mirrors-and-scattering` |
| `LIGHT-09` | The straw really does bend in water. | `s-hook` | `s-think` | `refraction` |
| `LIGHT-10` | Light bends because water is thicker and pushes it sideways. | `block` | `s-think` | `refraction` |
| `LIGHT-11` | Light speeds up when it enters glass, because glass is clearer than air. | `s-ladder` | `block` | `refraction` |
| `LIGHT-12` | Light only slows down when it bends, so a ray that carries straight on has not changed speed. | `block` | `block` | `refraction` |
| `LIGHT-13` | The pinhole flips the picture over, so a lens must flip it back. | `s-hook` | `s-think` | `lenses-and-images` |
| `LIGHT-14` | A bigger hole makes a bigger picture. | `s-ladder` | `camera` | `lenses-and-images` |
| `LIGHT-15` | A longer box spreads the light out, so the picture gets smaller. | `camera` | `camera` | `lenses-and-images` |
| `LIGHT-16` | A wider hole cannot blur the picture, because light travels in straight lines. | `s-ladder` | `lens-pair` | `lenses-and-images` |
| `LIGHT-17` | Your eyes send something out in order to see. | `s-ladder` | `s-think` | `the-eye-and-the-camera` |
| `LIGHT-18` | In a dark room your pupils open, and that is why you can eventually see. | `s-hook` | `s-think` | `the-eye-and-the-camera` |
| `LIGHT-19` | The retina focuses the light, the way a lens does. | `s-ladder` | `eye-camera-parts` | `the-eye-and-the-camera` |
| `LIGHT-20` | A camera's shutter does the same job as the iris. | `s-ladder` | `eye-camera-parts` | `the-eye-and-the-camera` |
| `LIGHT-21` | The prism adds the colour to the light. | `s-hook` | `s-think` | `colour-and-the-spectrum` |
| `LIGHT-22` | A rainbow has seven colours with lines between them. | *(none — nothing on the page asks for this commitment)* | `s-think` | `colour-and-the-spectrum` |
| `LIGHT-23` | High-frequency light is bent the least by a prism. | `s-ladder` | `spectrum-band` | `colour-and-the-spectrum` |
| `LIGHT-24` | The colours come off the coloured edges of the prism. | `s-hook` | `prism` | `colour-and-the-spectrum` |
| `LIGHT-25` | An object has a colour, and the light just lets you see it. | `lamp` | `s-think` | `why-things-look-coloured` |
| `LIGHT-26` | A red filter turns white light red. | *(none — nothing on the page asks for this commitment)* | `s-think` | `why-things-look-coloured` |
| `LIGHT-27` | The lamp's colour and the object's colour mix on the surface to give what you see. | `s-hook` | `lamp` | `why-things-look-coloured` |
| `LIGHT-28` | You cannot see red under a green lamp because the eye stops being able to, not because the light is not there. | `s-hook` | `colour-grid` | `why-things-look-coloured` |

⚠️ **FOURTEEN ROWS ARE NOT IN DESIGN'S PROPOSED TABLE.** Her §7 pre-allocates `LIGHT-01`, `02`, `05`, `06`, `09`, `10`, `13`, `14`,
`17`, `18`, `21`, `22`, `25` and `26` — the first two of each lesson's four — and leaves the rest of each range as a named spare.
A spare that is never used is an id reserved against nothing, so each of the fourteen below is minted from a delivered distractor or
a delivered quote instead, and each is a genuinely separate belief rather than a re-dressing of one already minted. That is the
`p1-08` test this register applies.

  * `LIGHT-03` light is LONGITUDINAL, like sound (`p7-01`'s comparison table, row four). Separate from `LIGHT-02`: a student can
    have accepted that light crosses a vacuum and still be drawing it as a squeeze passed along.
  * `LIGHT-04` the thunder is MADE a moment after the flash (`p7-01` hook option B). It is the one rival explanation that fits the
    observation exactly, and it survives being told that light is faster.
  * `LIGHT-07` the mirror sends back FAR MORE light than the paper (`p7-02` hook option C). This is how much against how ORDERED,
    and the bench answers it with two numbers that are nearly the same — 95% and 80%.
  * `LIGHT-08` only SHINY surfaces reflect (`p7-02` rung 2 option D, *"Paper is not shiny enough"*). Crumpled foil is the object
    that separates shiny from smooth, and it is on the tab row for that reason.
  * `LIGHT-11` light SPEEDS UP in glass because glass is clearer than air (`p7-03` rung 1 option C). Separate from `LIGHT-10`: this
    one has the direction of the speed change wrong rather than the mechanism of the bend.
  * `LIGHT-12` light only slows down WHEN IT BENDS (`p7-03` rung 2 option C, and her gate option C). It is the exact converse of the
    zero-angle state the bench is built around, and it is why that state has its own branch and its own verdict word.
  * `LIGHT-15` a LONGER box makes a SMALLER picture (`p7-04` rung 1 option B). Separate from `LIGHT-14`: that one is about the hole,
    this one is about the box, and a student can have the box the wrong way round while knowing the hole does nothing.
  * `LIGHT-16` a wider hole CANNOT blur, because light travels in straight lines (`p7-04` rung 2 option C). The premise is correct
    and the rule drawn from it is wrong, which is exactly why students reach for it.
  * `LIGHT-19` the RETINA focuses (`p7-05` rung 1 option B). It pairs the wrong two parts and it is the commonest mismatch in the
    five-job table.
  * `LIGHT-20` a camera's SHUTTER matches the iris (`p7-05` rung 1 option C). How WIDE against how LONG, and the eye has nothing at
    all that does the second.
  * `LIGHT-23` HIGH-frequency light is bent LEAST (`p7-06` rung 1 option B). It is the whole of dispersion pointing backwards, and
    the spectrum figure's two arrows are what settle it.
  * `LIGHT-24` the colours come off the prism's coloured EDGES (`p7-06` hook option D and rung 2 option D). Separate from
    `LIGHT-21`: it locates the colour in the glass's surface rather than in the glass at all, and the whole beam fanning out is what
    answers it.
  * `LIGHT-27` the lamp's colour and the object's colour MIX on the surface (`p7-07` hook option C, gate option D). What the bench
    computes is an INTERSECTION, and "red and green make yellow" is the arithmetic a student brings from paint.
  * `LIGHT-28` the failure is in the EYE, not in the light (`p7-07` hook option D). It is the only one of the four that keeps the
    physics of the surface intact and moves the fault into the observer, and the twenty-cell grid is what shows the lamp deciding.

⚠️ **`LIGHT-03`, `LIGHT-22` AND `LIGHT-26` HAVE NO `elicited_by`, WHICH §5.3 ALLOWS.** Nothing on those pages asks the student to
commit to them: `p7-01`'s table states the transverse row without asking, and `p7-06` and `p7-07` each carry their second Think-again
quote underneath a belief that IS elicited. Recording the gap is the honest answer, and MRB-248 makes absence legal precisely so
that it need not be invented.

⚠️ **EXPECTED TO RESURFACE.** `LIGHT-17` — *eyes send something out* — wherever seeing is drawn as a ray from an eye, which is most
of the way people sketch it. `LIGHT-25` — *an object HAS a colour* — in B7, where a leaf's greenness is the part of sunlight
chlorophyll throws away, and in any lesson that treats colour as a property of a substance.

⊖ **`LIGHT` DOES NOT RE-DECLARE `WAVE-21`.** `p7-01` opens by restating that sound needs a medium and light does not, which is
`p6-06`'s belief met from the other side. That is a REAPPEARANCE and not a re-confrontation: nothing on `p7-01` takes a student's
commitment about sound and takes it apart. The lesson carries `sound-needs-a-medium` as an edge instead, which is what the register
asks for.

### `CIRC` — current and circuits: what a current is and what it is not, what a battery does, what happens at a junction, what a resistance is, and what a meter measures

⊕ **OPENED 25 Aug 2026, BY P8.** `docs/ks3/design-reference/p8/NOTES-P8-P9.md` §7 pre-allocated `CIRC-01` … `CIRC-28`, four per
lesson in slot order, and authored 16 of them without citing one on any page — because access was read-only and this register had no
open family for electricity. **Every id she wrote is minted here on the number she gave it, in her words.** The twelve gaps are minted
from the real lesson content, which is the register's own rule: an id is minted from what a page actually confronts, never reserved
against what one might.

⚠️ **THE RESERVATION IS DISCHARGED, NOT LEFT STANDING BESIDE THE FAMILY.** The not-yet-opened list above reserved `CIRC` for
*current and circuits*; that is this family, so the reservation is struck exactly as `FORCE`'s was, and `ENER`'s before it. A physics
lane meeting a circuits misconception adds to `CIRC`; it does not open `ELEC`.

⚠️ **WHERE HER NOTES AND HER PAGE WORD A BELIEF DIFFERENTLY, THE PAGE WINS.** Eleven of the sixteen are stated at length in a
*Think again* quote on the page and more briefly in her §7 table. Both are hers; the page's is the sentence a student actually meets.
Same ruling as `WAVE-33` / `WAVE-34` in P6.

| ID | Statement, as a student holds it | Elicited by | Confronted by | Lesson |
|---|---|---|---|---|
| `CIRC-01` | The bulb uses up the current, so there is less of it coming back than going in. | `loop` | `loop` | `current-and-circuits` |
| `CIRC-02` | The electricity has to get from the cell to the bulb, which is why there is a tiny delay when you flick the switch. | `s-hook` | `s-think` | `current-and-circuits` |
| `CIRC-03` | A circuit only has to reach the bulb; what happens on the way back does not matter. | `s-hook` | `loop` | `current-and-circuits` |
| `CIRC-04` | A cell holds a store of current and sends it out into the wire. | `s-ladder` | `s-think` | `current-and-circuits` |
| `CIRC-05` | In parallel the current has to split between the two bulbs, so each one is dimmer. | `bench` | `bench` | `series-and-parallel` |
| `CIRC-06` | In series the first bulb gets the current first, so it is brighter than the second one. | *(none — nothing on the page asks for this commitment)* | `s-think` | `series-and-parallel` |
| `CIRC-07` | Two bulbs in series are each as bright as one, because the battery has not changed. | `s-ladder` | `bench` | `series-and-parallel` |
| `CIRC-08` | A fuse box is what keeps the other lights on when one bulb fails. | `s-hook` | `s-hook` | `series-and-parallel` |
| `CIRC-09` | At a junction the current halves, because it has two ways to go. | `junction` | `junction` | `current-at-a-junction` |
| `CIRC-10` | Adding a second branch means less current for the first one. | `s-ladder` | `s-think` | `current-at-a-junction` |
| `CIRC-11` | To find the total at a junction you add every reading you can see, including the main wire's. | `s-ladder` | `junction` | `current-at-a-junction` |
| `CIRC-12` | Some of the current is left behind in the branch that resists more. | `s-hook` | `s-hook` | `current-at-a-junction` |
| `CIRC-13` | Voltage flows round the circuit and gets used up by each bulb. | *(none — nothing on the page asks for this commitment)* | `s-think` | `potential-difference` |
| `CIRC-14` | A voltmeter goes in the circuit, like an ammeter. | *(none — see the note below)* | `s-think` | `potential-difference` |
| `CIRC-15` | A reading equal to the battery's p.d. across one component must be a fault. | `s-ladder` | `volt` | `potential-difference` |
| `CIRC-16` | The number stamped on a bulb says how much electricity it uses up while it is on. | `s-hook` | `s-hook` | `potential-difference` |
| `CIRC-17` | Resistance is a force pushing back against the current. | *(none — nothing on the page asks for this commitment)* | `s-think` | `resistance` |
| `CIRC-18` | A component has one resistance, so it does not matter what supply you test it on. | `bench` | `bench` | `resistance` |
| `CIRC-19` | You find a resistance by multiplying the voltmeter reading by the ammeter reading. | `s-ladder` | `your-turn-resistance` | `resistance` |
| `CIRC-20` | If one component gives two different resistances, one of the meters must be faulty. | `s-ladder` | `s-think` | `resistance` |
| `CIRC-21` | An insulator blocks electricity completely — absolutely nothing gets through. | `test` | `test` | `conductors-and-insulators` |
| `CIRC-22` | Materials are either conductors or insulators, with nothing between. | `s-hook` | `s-scale` | `conductors-and-insulators` |
| `CIRC-23` | Plastic insulates because it has no charged particles in it at all. | `s-ladder` | `s-ladder` | `conductors-and-insulators` |
| `CIRC-24` | A short enough piece of an insulator would conduct properly. | `test` | `test` | `conductors-and-insulators` |
| `CIRC-25` | The meter reads zero, so the meter must be broken. | `s-hook` | `wire` | `building-and-measuring-a-circuit` |
| `CIRC-26` | It cannot matter which way round the leads go on a meter. | *(none — nothing on the page asks for this commitment)* | `s-think` | `building-and-measuring-a-circuit` |
| `CIRC-27` | The order the components come in round a single loop changes what the meters read. | `s-hook` | `s-hook` | `building-and-measuring-a-circuit` |
| `CIRC-28` | A voltmeter reading close to the battery's value means the circuit is working. | `s-ladder` | `wire` | `building-and-measuring-a-circuit` |

⚠️ **TWELVE ROWS ARE NOT IN DESIGN'S PROPOSED TABLE**, and every one arrived from a delivered
distractor, hook option or bench state rather than from her §7 list. Each is a genuinely separate
belief rather than a re-dressing of one already minted, which is the `p1-08` test this register
applies:

  * `CIRC-03` a circuit only has to REACH the bulb (`p8-01` hook option B). Separate from
    `CIRC-01`: a student can have given up "the bulb uses it up" and still think the return wire
    is decoration.
  * `CIRC-04` a cell HOLDS a store of current (`p8-01` rung 2 option D, *"a cell … makes new ones
    in the wire as they are needed"*). It is about where the charge comes from, which `CIRC-01`
    and `CIRC-02` both take for granted.
  * `CIRC-08` a FUSE BOX is what keeps the other lights on (`p8-02` hook option D). The right
    verdict from the wrong mechanism, and it survives being told the answer is "parallel".
  * `CIRC-11` add EVERY reading you can see (`p8-03` rung 1 option B, *"1.55 A — add all three
    readings together"*). Design's own §8 calls it *"the single most common wrong answer to a
    three-branch junction question"*, and it is arithmetic rather than physics — separate from
    `CIRC-09`, which is about the split.
  * `CIRC-12` some current is LEFT BEHIND in the harder branch (`p8-03` hook option B). It is
    conservation, not sharing, and a student can hold it while getting the split right.
  * `CIRC-16` a rating says how much a bulb USES UP (`p8-04` hook option B). About what a printed
    number means, which is a different question from what a p.d. is.
  * `CIRC-19` MULTIPLY the two readings (`p8-05` rung 1 option B). The wrong operation rather than
    a wrong idea about what resistance is, which is `CIRC-17`.
  * `CIRC-20` two answers means a faulty METER (`p8-05` rung 2 option B). `CIRC-18` is a belief
    about the component; this is a belief about the instrument, and it is the one that stops a
    student trusting a correct measurement.
  * `CIRC-23` plastic has no charged particles AT ALL (`p8-06` rung 2 option D). `CIRC-21` is
    about how much gets through; this is about what is in the material, and correcting one leaves
    the other standing.
  * `CIRC-24` a SHORT ENOUGH piece of an insulator conducts (`p8-06`'s bench gate option D). It
    arrives with the length control, which really does change the resistance tenfold, and it is
    the misreading that control invites.
  * `CIRC-27` the ORDER of the components round a loop matters (`p8-07` hook option D). Her hook
    reveal answers it in a clause — *"the sequence, incidentally, does not matter at all in a
    single loop"* — which is what a belief being confronted looks like.
  * `CIRC-28` a NEAR-FULL voltmeter reading means it works (`p8-07` rung 2 option B). Separate
    from `CIRC-25`: this one is a student trusting a reading that is perfectly correct and about
    the wrong circuit.

⚠️ **`CIRC-14`'s `elicited_by` IS ABSENT, AND THAT IS A CORRECTION TO DESIGN'S TABLE RATHER THAN
A GAP.** Her §7 gives it *`r1` of `p8-07`* — a cross-page pointer. MRB-248 requires the value to
resolve on the page that DECLARES the entry, and `p8-04` cannot resolve a rung on `p8-07`, so it
is left absent, which §5.3 allows. The belief is still elicited on `p8-07`; what it may not do is
claim that from `p8-04`. `p8-07` does not re-declare it either — the standing rule is CITE, DO NOT
RE-DECLARE — so it appears there as a reappearance and nowhere as a second entry.

⚠️ **FOUR MORE HAVE NO `elicited_by`, WHICH §5.3 ALLOWS, AND ALL FOUR ARE HERS.** `CIRC-06`,
`CIRC-13`, `CIRC-17` and `CIRC-26` are marked *(none)* in her own §7 table, and the pages agree:
nothing on any of the four asks the student to commit to the belief. Each is confronted because it
sits underneath one that is.

⚠️ **EXPECTED TO RESURFACE.** `CIRC-13` — *voltage flows and is used up* — anywhere a p.d. is
named, and P10 will meet it again the moment a motor is driven. `CIRC-21` — *an insulator blocks
current completely* — in P9, where a charged rod on an insulating stand is the whole apparatus and
"insulator" has to mean *leaks slowly* rather than *never*.

⚑ **`CIRC-01` OVERLAPS `ENER`'s NEIGHBOURHOOD IN SHAPE ONLY and no cross-reference is recorded.**
Both are wrong beliefs about something being consumed. But `ENER` is about energy, which really IS
transferred out of a store, and `CIRC-01` is about CHARGE, which is not — the whole correction is
that the two are different quantities and only one of them is spent. A `reappears_in` edge between
them would blur exactly the distinction `p8-01` exists to draw.
