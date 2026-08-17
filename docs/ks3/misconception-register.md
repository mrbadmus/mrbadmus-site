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
| `LIFE` | What counts as living, and the life processes | 2026-08-09, by B1 |
| `CELL` | Cells, microscopy and the organisation of living things | 2026-08-09, by B1 |
| `BODY` | Body systems, and how they do mechanical work | 2026-08-16, by B2 |
| `ATOM` | Atoms having kinds, and substances versus their ingredients | 2026-08-16, by B2's sibling delivery, C2 |
| `DIET` | Food, what a body needs from it, and what the gut does to it | 2026-08-16, by B3 |

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
- `PART-10`/`PART-11` (diffusion needs a push / particles intend to spread) → B1 `specialised-cells`
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
| `BODY-06` | A joint could rotate further if the muscles were stronger or the ligaments looser. | `ladder-r2` | `ladder-r2-feedback` | `joints` |
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
| `ATOM-02` | A model that turns out to be wrong about something has been disproved and should be discarded. | `ladder-r2` | `stretch-boundary` | `the-atom-daltons-model` |
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
- `ATOM-02` belongs with `PART-12`/`PART-13` and is **the third piece of evidence that a `NOS`
  family is wanted**. The ruling under the `PART` entries says the call should be made before
  `C8 mendeleev` is authored; `the-atom-daltons-model` has now made the same shape of argument a
  second time. The call is still open and is Mide's.

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
evidence. Confronting them is closer to the nature-of-science pair `PART-12`/
`PART-13` than to anything in `DIET` or `BREATH`.

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

| ID | Statement (as a student holds it) | Elicited by | Confronted by | Lesson |
|---|---|---|---|---|
| `DRUG-01` | Drugs are illegal substances. | `hook` | `two-wrong-ideas` | `what-drugs-do-to-the-body` |
| `DRUG-02` | A painkiller goes to the part that hurts. | `follow-the-dose` | `two-wrong-ideas` | `what-drugs-do-to-the-body` |
| `DRUG-03` | Coffee, a cold shower or fresh air will sober you up. | `beat-the-liver` | `two-wrong-ideas` | `alcohol-and-smoking` |
| `DRUG-04` | A few cigarettes now and then is basically fine. | `two-wrong-ideas` | `two-wrong-ideas` | `alcohol-and-smoking` |
| `DRUG-05` | If it's natural, it's safe — it's the chemicals that hurt you. | `find-the-fault` | `two-wrong-ideas` | `substance-misuse-and-decisions` |
| `DRUG-06` | Everyone my age is doing it. | `find-the-fault` | `two-wrong-ideas` | `substance-misuse-and-decisions` |
| `DRUG-08` | Filters make cigarettes safer. | `two-wrong-ideas` | `two-wrong-ideas` | `alcohol-and-smoking` |
| `DRUG-09` | One person who came to no harm disproves a risk. | `find-the-fault` | `find-the-fault` | `substance-misuse-and-decisions` |

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
that names something on a different page. The other twenty-nine values in KS3
all name a place on their own page (`hook`, `ladder`, `s-think`,
`stretch-boundary`, or a real activity id), so a slug is a pointer no page can
resolve and a join that reads as working precisely because nothing checks it.

The precedent is `CELL-08` in the `DIET` table above: a borrowed id is
re-declared only where the page genuinely **re-confronts** the belief with a real
activity of its own. Neither b6-02 nor b6-03 does — they open on it and move on.
So the reappearance lives here, which is what NOTES-B6 §5 asked for in the first
place:

> `DRUG-01` reappears in `alcohol-and-smoking` (its big question IS the belief)
> and in `substance-misuse-and-decisions` (hook option B). Confronted once, in
> `what-drugs-do-to-the-body`.

**⚠️ Every `confronted_by` in this family except `DRUG-09` names
`two-wrong-ideas`.** That is not a copy-paste error: Design draws exactly one
"Think again" block per page in this unit, carrying two quotes, and the block is
the activity. `DRUG-09` is the exception because b6-03 confronts it inside the
claim bench itself and hits it again at the ladder — the only belief in the unit
attacked twice.
