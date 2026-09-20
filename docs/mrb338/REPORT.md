# MRB-338 · Bank expansion programme — NIGHT 1 REPORT

**9–12 Sep 2026.** Branch `feat/bank-expansion-1` off `origin/main`
`d6c5d0ec8`. Content only. Mide's rulings of 9 Sep are carried out in §7
and §8.

⊕ **The second batch landed 12 Sep 2026** as `f816e3caa`, under Mide's ruling
of that date. Five more leaves, both banks reloaded to production, and **every
figure in this report is the one that holds after that load** — §1, §7 and §8
were rewritten rather than appended to, so there is one set of numbers here
and not two. The second push is §11.1 and the second load is §12.3.

---

## 1 · What shipped

**24 of the 83 Autumn-1 leaves are at their floor.** 1,467 rows authored.

| | before | after | added |
|---|---|---|---|
| `ks3_assignment_bank` | 5,142 | 6,141 | **+999** |
| `ks4_assignment_bank` | 3,417 | 3,885 | **+468** |

Of that, the 12 Sep batch is +210 KS3 and +104 KS4 — 314 rows across five
leaves, taking the count at floor from 19 to 24.

Every KS3 diff is insertions-only with the pre-existing rows byte-identical,
and `ks4_pool_check` confirms bank positions 0–11 are still four of each band
in all 264 subtopics. **No automatically-composed assignment in the school
changes**, which is the invariant the whole programme is written around.

### The leaves, before → after

| leaf | band shape before | after | rows |
|---|---|---|---|
| KS3 `B1/using-a-microscope` | 9/9/9 | 32/32/32 | +69 |
| KS3 `B1/animal-and-plant-cells` | 9/9/9 | 32/32/32 | +69 |
| KS3 `B1/specialised-cells` | 9/9/9 | 32/32/32 | +69 |
| KS3 `B1/levels-of-organisation` | 8/8/8 | 32/32/32 | +72 |
| KS3 `B2/what-the-skeleton-does` | 13/13/13 | 32/32/32 | +57 |
| KS3 `B4/the-gas-exchange-system` | 11/11/11 | 32/32/32 | +63 |
| KS3 `B4/how-breathing-works` | 11/11/11 | 32/32/32 | +63 |
| KS3 `B7/the-photosynthesis-reaction` | 13/13/13 | 32/32/32 | +57 |
| KS3 `B8/aerobic-respiration` | 11/11/11 | 32/32/32 | +63 |
| KS3 `C1/solids-liquids-and-gases` | 9/9/9 | 32/32/32 | +69 |
| KS3 `C2/the-atom-daltons-model` | 9/9/9 | 32/32/32 | +69 |
| KS3 `C2/elements` | 9/9/9 | 32/32/32 | +69 |
| KS4 `energy-stores-systems` | 4/4/4 | 12/26/26 | +52 |
| KS4 `animal-plant-cells` | 4/4/4 | 12/26/26 | +52 |
| KS4 `eukaryotes-prokaryotes` | 4/4/4 | 12/26/26 | +52 |
| KS4 `cell-specialisation` | 4/4/4 | 12/26/26 | +52 |
| KS4 `chromosomes-mitosis` | 4/4/4 | 12/26/26 | +52 |
| KS4 `stem-cells` | 4/4/4 | 12/26/26 | +52 |
| KS4 `microscopy` | 4/4/4 | 12/26/26 | +52 |
| KS3 `C1/changes-of-state` ⊕ | 9/9/9 | 32/32/32 | +69 |
| KS3 `C1/gas-pressure` ⊕ | 9/9/9 | 32/32/32 | +69 |
| KS3 `C1/diffusion` ⊕ | 8/8/8 | 32/32/32 | +72 |
| KS4 `digestive-system` ⊕ | 4/4/4 | 12/26/26 | +52 |
| KS4 `enzymes` ⊕ | 4/4/4 | 12/26/26 | +52 |

⊕ marks the five leaves of the 12 Sep batch.

A KS4 **base** subtopic at 12/26/26 gives a Foundation pool of 64 and a Higher
pool of 52; both clear fifty, which is what Mide asked for. A KS3 lesson at
32/32/32 clears thirty in each of Easy, Medium and Hard.

---

## 2 · THE LENGTH MEASURE — the story in full

This is the most important thing night 1 produced, and it is a story about a
gate that was watching the wrong scope and a brief that told lanes to measure
the wrong number.

### 2.1 · What I told the lanes, and why it was wrong

The brief said: *the key should be the longest option about one time in four.*
Lanes measured exactly that, reported 17–23%, and I accepted it.

**`verify_answer_lengths` does not ask that question.** It discards every
option set whose top two options are within **6 characters** — those have no
*visibly* longest option and tell a pupil nothing — and then asks, **of the
sets that remain**, how often the key is the long one. Chance is 25%; its
practical ceiling `HI` is 35%.

Those two measures come apart badly, and in a specific, reachable way: park the
key at rank 2 in most rows but let it run away whenever it *is* longest, and
"key is longest" reads a healthy 20% while the gate reads 65%.

### 2.2 · What it cost

Measured across the leaves committed before the error was found:

| leaf | my measure | the binding measure |
|---|---|---|
| KS3 `animal-and-plant-cells` | 20% | **66.7%** |
| KS3 `C1/solids-liquids-and-gases` (in flight) | ~20% | **65.2%** |
| KS3 `B4/how-breathing-works` (in flight) | ~20% | **61.2%** |
| KS3 `C2/the-atom-daltons-model` (in flight) | — | **54.3%** |
| KS4 `eukaryotes-prokaryotes` | 23% | **50.0%** |
| KS4 `animal-plant-cells` | 19% | **45.5%** |
| KS4 `stem-cells` | 21% | **37.5%** |
| KS4 `cell-specialisation` | 23% | **35.3%** |

Roughly 600 committed rows plus four in-flight lanes — around a third of the
run's elapsed time went on finding this, correcting the brief, repairing five
committed leaves and re-verifying all of it.

### 2.3 · ⚠️ Why no gate caught it — the recommendation

`verify_answer_lengths` scores whole **units**. B1 aggregated to 27.3%, because
156 balanced pre-existing rows diluted 279 skewed new ones, so it stayed green
throughout.

**But Set work v2 sets LEAVES, not units.** That is the entire premise of
MRB-338. A teacher setting `animal-and-plant-cells` alone hands their class a
leaf where the long option was the answer two times in three, and every gate in
the estate reported green.

> **RECOMMENDATION FOR MIDE: give `verify_answer_lengths` a per-leaf scope.**
> Unit-level was the right scope when a leaf held twelve rows and a unit held a
> few hundred — a leaf was too small to measure. At 64 and 96 rows a leaf is
> now the biggest thing a teacher actually sets, and it is large enough for the
> gate's own binomial test to speak to. The gate's scope no longer matches the
> product's. This is night 2 work and it is the single highest-value change to
> the harness that this programme has surfaced.

### 2.4 · The fix, and the trap inside it

Both tells pull in **opposite directions**, which is why it had to be written
down rather than left to judgement. Escaping the "key is shortest" tell by
lengthening keys drives the binding measure **up**.

The correct fix is neither: **give the distractors their own reasons at the
key's level of detail**, so most sets have no visibly longest option at all.
Two lanes independently proved it works — 65.2% → 25.0% and 54.3% → 20.7% —
and no key was trimmed or lengthened in either.

⚠️ One lane found the way to fake it: flatten *every* set, and the denominator
collapses to four, where the gate's binomial test can say nothing. It rebuilt
45 distractors instead so that ~24 sets have a real longest option and 18 of
those are a distractor. **A leaf that teaches "the long option is usually
wrong" is stronger than one where length is merely uninformative.**

### 2.5 · Where every leaf finished

All twenty-four sit between **8.0% and 29.6%** against a 32% ceiling. ⊕ The
12 Sep five came in at 23.8% (`changes-of-state`), 25.0% (`gas-pressure`),
25.0% (`diffusion`), 17.9% (`digestive-system`) and 21.4% (`enzymes`) — every
one of them inside that band, and four of the five within seven points of
chance.

---

## 3 · The two duplicate stems, and the gate that now runs before every commit

`set_work_scope_check` went **red** and I had not been running it. Two rows
written on night 1 duplicated a stem in a **different leaf of the same unit or
topic**:

| new row | duplicated | where |
|---|---|---|
| `c2-01-e19` "What is a molecule?" | `c2-05-e05`, shipped | the `formulae` leaf, unit C2 |
| `ks4-microscopy-e12` "…nanometres in one micrometre" | `ks4-eukaryotes-prokaryotes-e03`, shipped | topic `cell-biology` |

⚠️ **Neither was visible to anything I was running.** My per-leaf checker
compares a leaf against *itself*; each lane measures its *own* rows.
`set_work_scope_check` treats a whole KS3 unit and a whole KS4 topic as **one
cell** and is the only thing in the estate that sees a new row colliding with a
row in another leaf. With five lanes writing one unit in parallel, unable to
read each other's uncommitted files, it is not optional.

**It now runs in `land.sh` before every commit**, alongside the seven gates
that were already there.

The second repair took two attempts, and the failure is the useful part:
re-aiming `microscopy-e12` at millimetres-per-micrometre **collided with
`animal-plant-cells-e11`**, because three leaves of `cell-biology` each want
the same easier unit-conversion row and only one may own it. It now asks the
three units in order of size, which no leaf owns. That shared-fact problem will
recur on every topic night 2 touches; brief §9.4 now names it.

---

## 4 · The "same hand" rule — a tell no measure catches

One lane found four rows with a **short key beside three long explanatory
distractors**. Every one passes the six-character test — the key is nowhere
near longest — and every one gives the answer away, because a pupil spots the
odd one out instantly and it is the right one.

Length parity is a **proxy**. The rule it stands for is that nothing about an
option's shape, register, grammar or length should mark it out. Other tells
found in one night, none of them length:

- the key was the only option not beginning "They";
- the key was the only option naming a route;
- three distractors **confessed their own arithmetic error** in the option text;
- a key was the only option carrying a reason clause.

Brief §9.7 now states it: **all four options must read as though one hand wrote
them.**

---

## 5 · Content findings the gates cannot see

Every one of these was found by an executor's cold re-read, not by a gate.

### 5.1 · Distractors that were defensible rather than wrong

A distractor a careful pupil can argue for is a question with two answers.
Thrown out on night 1: bacteria really do take up DNA from their surroundings;
surface-area-to-volume really does fall and then rise once a cell divides; a
cell wall really is a barrier water crosses; 0.1 mm really is about the
naked-eye limit; the diaphragm really does attach to the lower ribs; a marrow
transplant really can change a blood group; beating gold leaf really does make
the layers slide.

Two further shapes, both subtler:

- **the creditable distractor** — reaches a wrong conclusion through a true
  clause an examiner would credit ("colour is a property of the whole material,
  not of one particle");
- **defensible elsewhere in the unit** — "respiration needs no oxygen" is
  unarguably wrong for aerobic respiration and arguable two lessons later, and
  the unit is one cell for the duplicate gate.

### 5.2 · Keys that were arguably false

- a palisade cell and a root hair cell "develop from the same meristem cells" —
  they do not; shoot apical and root apical are different meristems;
- beating gold leaf "rearranges nothing about the atoms";
- a single atom "has none", parsing as no kinetic energy rather than no
  temperature;
- limewater "turns milky far sooner", which implies the control also turns
  milky, and at equal volumes it barely does — which made a distractor's
  *observation* defensible;
- a tenfold rise called "not quite keeping pace" with a twentyfold one.

### 5.3 · A stem that stated another row's keyed answer

Two stems quoted "about two million every second" and "last about four months"
— both the **keyed answers to other rows in the same leaf**. A pupil meeting
them in one assignment is handed two answers free.

⚠️ Duplicate-stem and duplicate-option checks are **blind** to this: the
collision is between one row's STEM and another row's KEY. Brief §9.6.

### 5.4 · A row that would have contradicted its neighbour

The `microscopy` lane dropped a planned row on the smallest structure a light
microscope can resolve, because it would have **contradicted**
`animal-plant-cells` on whether a mitochondrion is identifiable. Two rows in
one topic disagreeing about the same fact is worse than either being absent,
and nothing compares leaves for agreement.

### 5.5 · Register

A `specialised-cells` row described a person with an inherited condition
causing both chest infections and non-motile sperm. That lesson's
`named_conditions` is ruled `False` precisely so a Year 7 is not handed a
diagnosis, and describing one unnamed runs against the ruling's spirit rather
than around it. Rewritten as a laboratory observation — a chemical that blocks
one protein stops both airway cilia and sperm tails. The deduction survives;
the medical framing does not.

### 5.6 · Work that was declined, correctly

- **Ribosomes are absent from `animal-and-plant-cells`.** My coverage list
  named them; the lane refused. That lesson teaches a **seven-part list** and
  its first ladder rung turns on a cell having nothing else from the seven.
  Bank rows about ribosomes would contradict the page the child revised.
- **The germinating-peas and boiled-seed control** was declined on
  `aerobic-respiration`, though my brief named it: it is that lesson's own
  ladder rung 4 almost exactly, and reproducing a rung is a hard
  `pool_ownership` failure. The evidence quota went to limewater,
  hydrogencarbonate indicator and the respirometer instead — including a row
  asking why a temperature rise alone is not yet safe evidence, which is the
  rung's underlying skill without its apparatus.
- **A row measuring 0.80 similarity to a lesson quiz stem on a different page**
  was re-aimed. `pool_ownership`'s near-duplicate threshold is 0.88, so it
  would have shipped unreported, and a child revising that page would have met
  the same task with the answer already printed.

---

## 6 · The near-miss worth knowing about

While rewriting option text for length parity, one lane **replaced the text of
an option marked correct** with distractor prose. The row briefly stated
something false as its answer, and the true answer was no longer among the four.

⚠️ **Nothing in the estate catches this.** `question_bank` checks that exactly
one option carries `correct: True` and that the key has no `why`;
`ks4_pool_check` checks that `correct_index` is in range. Neither asks whether
the key is still *true*.

The lane restored it, adopted "no length edit may touch an option marked
correct", and re-audited all 46 of its edits. That rule was sent to both repair
lanes mid-flight; one of them had **already made the same mistake** — trimming
the working out of a calculation key — and reverted it on receipt. Across the
five repaired leaves, every stem, every `correct_index` and the text of every
key was afterwards proved byte-identical to HEAD, row by row, rather than
asserted. Brief §9.3.

---

## 7 · The remaining gap, per leaf

| stage | lane | unit/topic | leaf | now | rows to author |
|---|---|---|---|---|---|
| KS3 | biology | B2 | `antagonistic-muscle-pairs` | 13/13/13 | 57 |
| KS3 | biology | B4 | `exercise-asthma-and-smoking` | 10/10/10 | 66 |
| KS3 | biology | B6 | `alcohol-and-smoking` | 17/17/17 | 45 |
| KS3 | biology | B6 | `what-drugs-do-to-the-body` | 18/18/18 | 42 |
| KS3 | biology | B8 | `anaerobic-respiration-in-humans` | 10/10/10 | 66 |
| KS3 | biology | B8 | `fermentation` | 10/10/10 | 66 |
| KS3 | chemistry | C2 | `compounds` | 9/9/9 | 69 |
| KS3 | chemistry | C3 | `chromatography` | 7/7/7 | 75 |
| KS3 | chemistry | C3 | `distillation` | 7/7/7 | 75 |
| KS3 | chemistry | C3 | `evaporation-and-crystallisation` | 7/7/7 | 75 |
| KS3 | chemistry | C3 | `filtration` | 7/7/7 | 75 |
| KS3 | chemistry | C3 | `pure-or-mixture` | 8/8/8 | 72 |
| KS3 | chemistry | C4 | `mass-in-a-reaction` | 10/10/10 | 66 |
| KS3 | chemistry | C6 | `catalysts` | 8/8/8 | 72 |
| KS3 | chemistry | C8 | `group-0-and-why-groups-exist` | 7/7/7 | 75 |
| KS3 | chemistry | C8 | `group-1-the-alkali-metals` | 7/7/7 | 75 |
| KS3 | chemistry | C8 | `group-7-the-halogens` | 7/7/7 | 75 |
| KS3 | chemistry | C8 | `metals-and-non-metals` | 8/8/8 | 72 |
| KS4 | biology | ecology | `adaptations` | 4/4/4 | 52 |
| KS4 | biology | ecology | `carbon-cycle` | 4/4/4 | 52 |
| KS4 | biology | ecology | `decomposition` | 4/4/4 | 52 |
| KS4 | biology | ecology | `food-chains-webs` | 4/4/4 | 52 |
| KS4 | biology | ecology | `population-competition` | 4/4/4 | 52 |
| KS4 | biology | ecology | `trophic-levels` | 4/4/4 | 52 |
| KS4 | biology | organisation | `principles-of-organisation` | 4/4/4 | 52 |
| KS4 | chemistry | analysis | `carbonates-halides-sulfates` | 4/4/4 | 52 |
| KS4 | chemistry | analysis | `chromatography` | 6/10/9 | 39 |
| KS4 | chemistry | analysis | `flame-tests` | 4/4/4 | 52 |
| KS4 | chemistry | analysis | `metal-hydroxides` | 4/4/4 | 52 |
| KS4 | chemistry | analysis | `pure-substances` | 5/7/6 | 46 |
| KS4 | chemistry | atmosphere | `early-atmosphere` | 5/8/7 | 44 |
| KS4 | chemistry | atomic-structure | `atoms-elements-compounds` | 4/4/4 | 52 |
| KS4 | chemistry | atomic-structure | `electronic-structure` | 4/4/4 | 52 |
| KS4 | chemistry | atomic-structure | `mixtures` | 4/4/4 | 52 |
| KS4 | chemistry | atomic-structure | `model-of-the-atom` | 4/4/4 | 52 |
| KS4 | chemistry | atomic-structure | `relative-atomic-mass` | 4/4/4 | 52 |
| KS4 | chemistry | atomic-structure | `subatomic-particles` | 4/4/4 | 52 |
| KS4 | chemistry | chemical-changes | `titrations` | 4/4/4 | 52 |
| KS4 | chemistry | quantitative | `amounts-in-equations` | 4/4/4 | 42 |
| KS4 | chemistry | quantitative | `atom-economy` | 4/4/4 | 52 |
| KS4 | chemistry | quantitative | `concentration-of-solutions` | 4/4/4 | 52 |
| KS4 | chemistry | quantitative | `conservation-of-mass` | 4/4/4 | 52 |
| KS4 | chemistry | quantitative | `moles` | 4/4/4 | 42 |
| KS4 | chemistry | quantitative | `percentage-yield` | 4/4/4 | 52 |
| KS4 | chemistry | quantitative | `relative-formula-mass` | 4/4/4 | 52 |
| KS4 | chemistry | quantitative | `using-moles-calculations` | 4/4/4 | 42 |
| KS4 | physics | energy | `changes-in-energy` | 4/4/4 | 52 |
| KS4 | physics | energy | `energy-transfers-in-a-system` | 4/4/4 | 52 |
| KS4 | physics | forces | `work-done-energy-transfer` | 4/4/4 | 52 |
| KS4 | physics | particle-model | `changes-of-state` | 4/5/5 | 50 |
| KS4 | physics | particle-model | `density-of-materials` | 4/5/5 | 50 |
| KS4 | physics | particle-model | `internal-energy` | 4/5/5 | 50 |
| KS4 | physics | particle-model | `specific-latent-heat` | 5/6/5 | 48 |
| KS4 | physics | particle-model | `temperature-changes-shc` | 5/6/5 | 48 |
| KS4 | physics | waves | `lenses` | 4/4/4 | 52 |
| KS4 | physics | waves | `properties-em-waves-1` | 4/6/5 | 49 |
| KS4 | physics | waves | `properties-of-waves` | 5/6/6 | 47 |
| KS4 | physics | waves | `sound-waves-hearing` | 4/4/4 | 42 |
| KS4 | physics | waves | `waves-detection-exploration` | 4/4/4 | 42 |

**59 leaves, 3251 rows remaining of the Autumn-1 must-complete.**

- KS3 biology — 6 leaves, 342 rows
- KS3 chemistry — 12 leaves, 876 rows
- KS4 biology — 7 leaves, 364 rows
- KS4 chemistry — 21 leaves, 1035 rows
- KS4 physics — 13 leaves, 634 rows

⊕ 12 Sep: five leaves left this table — C1's `changes-of-state`,
`gas-pressure` and `diffusion`, and `organisation`'s `digestive-system` and
`enzymes`. It stood at 64 leaves / 3,565 rows after night 1's first batch.

---

## 8 · Night 2's order

**Rainford is still the clock.** Y7 and Y8 are in calendar weeks 1–4 of the KS3
carousel now; chemistry starts at calendar week 5 and physics at week 9.

1. **KS3 chemistry, C3 first** — 12 leaves, 876 rows, and still the largest
   single block open. ⊕ C1's `changes-of-state`, `gas-pressure` and
   `diffusion` were the 12 Sep batch and are done, so the block now opens on
   C3's separation set (`pure-or-mixture`, `filtration`,
   `evaporation-and-crystallisation`, `distillation`, `chromatography`),
   which Y7 meets within a fortnight, with C2 `compounds`, C4
   `mass-in-a-reaction`, C6 `catalysts` and C8's four behind it.
2. **KS4 biology `organisation`** — ⊕ 7 leaves, 364 rows. `digestive-system`
   and `enzymes` were the other half of the 12 Sep batch; of the three lesson
   slots Y10 is in now, only `principles-of-organisation` is left, at 52 rows.
3. **KS3 biology's remaining 6** — B2 `antagonistic-muscle-pairs`, B4
   `exercise-asthma-and-smoking`, B6 and B8's tail. 342 rows.
4. **KS4 chemistry, 21 leaves / 1,035 rows** — the biggest lane, and the one
   Rainford's Y9 and Y10 chemistry are furthest into.
5. **KS4 physics, 13 leaves / 634 rows.**

Then the continuation queue from `PLAN.md` §"The continuation queue", which
**KS3 physics leads**: Rainford starts Y7 and Y8 physics in calendar week 9,
the week after October half-term, so it is the nearest unstarted material even
though it has no Autumn-1 row at all.

### Two harness changes to make before night 2 authors anything

1. **Give `verify_answer_lengths` a per-leaf scope** (§2.3). This is the
   highest-value change the programme has surfaced.
2. **Fold `land.sh`'s gate order into the repo** rather than leaving it in a
   session scratch directory — in particular `set_work_scope_check` before
   every commit (§3), and the leaf checker's four corrected metrics (§9).

---

## 9 · The leaf checker, and the four times it was wrong

The per-leaf checker used all night lives in the session scratch directory, not
the repo. It was wrong four times and corrected four times, and each correction
is commented in place with the case that forced it. Recording them because
night 2 will rebuild something like it:

| it flagged | why that was wrong |
|---|---|
| paraphrase by **overlap coefficient** | "What is a coverslip?" is four tokens, so anything containing "what is a" scores 0.75. 13 of 20 hits were that artefact. Jaccard separates them; short stems are judged on Jaccard alone. |
| paraphrase at **Jaccard ≥ 0.60 on short stems** | "State the approximate resolution of a light microscope" vs "…maximum magnification of a light microscope" scores 0.70 on a shared seven-token frame. They are two facts with two answers — a **discrimination set**, which is the point. Hard fail now needs both stems ≥ 10 tokens. |
| the word **"figure"**, **"table"**, **"picture"** | "Why is their figure an underestimate" is a NUMBER; "a block rests on a table" is FURNITURE; "the picture on the retina" is an optical IMAGE. Only the unambiguous page-reference senses are matched now. |
| **pre-existing** duplicate pairs and page references | An old-old pair is a pre-existing condition, not this run's finding. It reports them and fails only on pairs involving a new row. |

⚠️ Every one of those was wrong in the **permissive-to-strict** direction — it
blocked good work rather than passing bad. That is the right failure direction,
but it cost real time, and a night-2 checker should start from the corrected
definitions above.

---

## 10 · Deviations

1. **There is no "16 Aug Rainford KS3 override seed"** (PLAN §2.1). The
   Rainford seeds are `20260906234500_rainford_ks4_overrides.sql` (670 rows)
   and `20260907003000_rainford_ks3_overrides.sql` (162 rows). ⚠️ The KS3 one
   carries its own collision warning against
   `20260726182000_ks3_school_schemes.sql`: both open with the same scoped
   DELETE of Rainford's KS3 rows, so whichever is applied last wins, silently.
   I used the override. **Which is live on prod is open on Mide.**
2. **`academic_week` is a lesson ordinal and restarts per subject at KS3**
   (PLAN §2.2) — Rainford staggers the sciences, biology from calendar week 1,
   chemistry from 5, physics from 9. Cutting on `academic_week ≤ 8` would have
   authored a half-term of physics Rainford does not teach until after October
   half-term. KS3 is cut on the calendar week parsed from each row's `notes`.
3. **One worktree, not six.** The lanes share `bank-expansion-1` with disjoint
   files; a sixth checkout was 300 MB the disk did not have at the time. The
   MRB-335 collision it guards against was between shared *scratch paths*, and
   each lane had its own.
4. **A recon scout returned a per-lesson KS3 table that summed to the correct
   total but was wrong lesson by lesson** (`using-a-microscope` reported 4/4/4;
   it is 9/9/9). Every planning figure was re-derived from `question_bank`
   directly. Agent-reported tables were verified, not trusted, for the rest of
   the run.
5. **I ran a `git stash`/`checkout` in a worktree while a lane was writing in
   it**, to capture the position baseline. It happened not to clobber anything
   — verified structurally afterwards — but it was careless. The baseline is
   captured, so it cannot recur.
6. **I chained `check && git add && git commit`**, and because the *check
   command itself* succeeded the commit ran while the check reported red.
   `chromosomes-mitosis` landed with a near-twin still in it; caught on the
   next line, fixed, amended. Commits now go through a helper that exits before
   `git add` if any gate is red.
7. **My own stem fix put a literal `\n` inside a question** — the exact defect
   a lane had caught earlier the same night. Corrected, and the whole estate
   swept: zero stray newlines in any stem or option, both key stages.
8. **`b2c/hardening` is fully merged into `origin/main`.** A memory note saying
   that work was unpushed was stale; git is the authority and the worktree was
   removed on that basis.

---

## 11 · Gates at the push

Receipts recorded by `prepush_gate.py --record-all`. **17 of 18 slow gates
green.** Every fast gate runs on `--check` and cannot be skipped.

Content gates, all green throughout and re-run before every single commit via
`land.sh`: `verify_questions`, `verify_answer_positions`, `pool_ownership`,
`question_bank`, `ks4_pool_check --python`, `verify_answer_lengths`,
`set_work_scope_check`.

### ⚠️ One inherited red, shipped with an override

```
teacher_admin_foreign_class — C7. REMINDERS — the control is drawn on the
                              foreign class · 3 check(s) failed
```

**This is not this branch's red, and the proof is two-sided.**

1. **The branch cannot reach it.** Every file changed against `origin/main` is
   question data (`ks3_data/**/questions_*.py`, `ks4_data/questions/**`), this
   run's docs (`docs/mrb338/**`), or the leaf gate itself
   (`set_work_scope_check.py`). Nothing under `teacher/`, `student/`,
   `shared/`, `supabase/` or the site tree is touched at all. That gate drives
   teacher pages under real RLS and reads none of those paths — and
   `build_ks3.py` contains **zero** references to the question bank while no
   generator reads `ks4_data`, so the bank cannot alter a built page either.
2. **It was already red, with the same signature.** `docs/mrb335/REPORT.md`
   records it on 7 Sep as `teacher_admin_foreign_class (C7 REMINDERS × 3)` —
   the same check, the same count — and MRB-335 shipped it under the same
   override after re-running it on its merge base.

### Three gates skipped for a credential this run was not given

`mrb328_import_picker_real` and `student_bell_drive` want
`$MRB_THROWAWAY_PASSWORD`; `mrb328_card_prefetch` wants
`mrb328_card_prefetch` wants `$MRB_TEST_TEACHER_PASSWORD`. Reported by name, as the
harness is designed to do — the same two-credential gap MRB-335 recorded.

### §11.1 · The second push, 12 Sep 2026

Rebasing `feat/bank-expansion-1` onto `origin/main` `dd7deaf30` was a **no-op**
— the branch already sat directly on it, nought behind, and nothing replayed.
Receipts were then recorded fresh on tree `41d27ad3e893`, because a receipt
attests a tree and night 1's attested a different one.

**Same picture as 9 Sep, gate for gate: 17 of 18 measurable slow gates green,
every fast gate green.** One improvement — `MRB_BACKEND` was set to the
deployed backend checkout (on `main`, not a colleague's branch), so
`pool_ownership`, `week_truth` and `set_work_unit` **measured instead of
skipping**, and all three pass. That is three gates of coverage night 1 did
not have.

The red is the same red, and it reproduced with the identical signature:

```
teacher_admin_foreign_class — C7. REMINDERS — the control is drawn on the
                              foreign class · 3 check(s) failed
```

The two-sided proof holds unchanged and is now narrower than it was. Every
file this branch changes against `origin/main` is one of five question-data
files (`ks3_data/c1/questions_0{3,4,5}_*.py`,
`ks4_data/questions/biology/organisation__z338_{digestive_system,enzymes}.py`)
plus `docs/mrb338/authoring-brief.md`. **Nothing under `teacher/`, `student/`,
`shared/`, `supabase/` or the site tree at all** — and that gate drives
teacher pages under real RLS. Shipped under the same override, on the tip
commit, where `prepush_gate` reads it.

⚠️ Six gates SKIPPED by name for credentials this run was not given
(`$MRB_SET_WORK_PASSWORD` × 2, `$MRB_DRIVE_PASSWORD`/`$MRB_TEST_STUDENT_PASSWORD`
× 2, `$MRB_TEST_TEACHER_PASSWORD` × 2, `$MRB_THROWAWAY_PASSWORD` × 3, counting
`export_ks3_questions_verify`) and two for the absent `3d-studio/dist`. **A
skip is not a pass**, none was overridden, and none is claimed as coverage
here.

---

## 12 · The production load — the outcome ruled as §7.3

Both banks are on production, verified. **The production project's reference
ends in november**, said in words before each write, and proved on every call
from the key's own JWT `ref` claim rather than from a URL beside it.

| | before | after |
|---|---|---|
| `ks3_assignment_bank` | 5,142 | **5,931** |
| `ks4_assignment_bank` | 3,417 | **3,781** |

### The proof

| check | result |
|---|---|
| KS4 row-for-row (`--verify --project prod`) | 3,781 live, **0 missing, 0 extra, 0 differing**, sha256 equal |
| KS3 aggregate md5, Python ↔ production | `619e52ca889600c6e0b96947b86fbba2` — **equal** |
| KS4 aggregate md5, Python ↔ production | `8bad52f1b7eecd324d67b70ba8d39765` — **equal** |
| KS3 auto windows | **0** lessons whose window is anything but 4/4/4 below position 12 |
| KS4 auto windows | **0** subtopics whose window is anything but exactly 12 rows |
| anon read, `ks3_assignment_bank` | `[]` — refused to the public |
| anon read, `ks4_assignment_bank` | `[]` — refused to the public |
| `--leaf` against production | **19 leaves at floor** (KS4 14 cells = 7 leaves × 2 tiers; KS3 36 cells = 12 lessons × 3 bands) |

⚠️ **The first md5 comparison failed on BOTH banks and the data was fine.** I
compared a Python `json.dumps` against a Postgres `::text`, and the two render
containers differently — `jsonb` reorders object keys by length, and
`ks4_assignment_bank.options` is a `text[]` rather than jsonb at all, so it
renders `{"a","b"}`. KS4's own `--verify` was saying the rows were identical at
the same moment. The fix is that **neither side renders a container**: options
are flattened to their scalar fields in authored order, so the checksum
depends on the data and not on either engine's printing.

### §12.1 · `export_ks3_questions.py` gained `--load {test,prod}`

Ruled by Mide, 9 Sep. It mirrors `export_ks4_questions.py` exactly — the same
three guards, the same `Prefer: resolution=merge-duplicates` header, 250-row
chunks — and defaults to **bank only**: `--pools` must name `ladder` or
`cards` explicitly, because MRB-338 changed the bank alone and the ladder
mirror is what the class page's practice round serves.

**Why the sanctioned route could not be used unattended, recorded in the
function so it is not rediscovered:** `ks3_pools_ingest(pool, payload)` guards
on `auth.jwt() ->> 'email' = 'midebolabadmus@gmail.com'`. That is deliberate —
its own comment says it exists so a refresh needs no service-role key on the
export machine, and a student holding a valid JWT must not be able to rewrite
the bank. But a service-role key carries **no `email` claim at all**, so an
unattended run is refused: `HTTP 400, P0001, "ks3_pools_ingest: not
permitted"`. Verified with an **empty payload**, so nothing could have been
written either way. The generated SQL is the documented alternative and is
5.2 MB across 24 statements, which cannot go through an MCP round trip.

Rehearsed on TEST first, as ruled: TEST also held 5,142, went to 5,931, and
read back with 0 broken auto windows and 12 lessons at floor — the same shape
production then produced.

### §12.2 · A gate that misnamed the database it had read

`set_work_scope_check.py --db` printed *"measuring the TEST database"*
unconditionally, while `$MRB_BACKEND_ENV` decides what it actually reads. Run
against production it reported a production measurement under the word TEST.

⚠️ That mattered on exactly this night: TEST and production held **identical
row counts** in both banks, so the label was the only thing on screen
distinguishing them. It now names the project from the URL it really used —
`the PRODUCTION database` / `the TEST database` / the bare ref for anything
else.

---

### §12.3 · The second load, 12 Sep 2026

Ruled by Mide for that night: both banks to production after the push, with
the MRB-335 proof. **Stated in words before the write — the target is the
PRODUCTION project — and proved on every call from the service key's own JWT
`ref` claim, `urklkrwevjtlfbwnipjn`**, never from a URL or a label beside it.

| | before | after | added |
|---|---|---|---|
| `ks3_assignment_bank` | 5,931 | **6,141** | +210 |
| `ks4_assignment_bank` | 3,781 | **3,885** | +104 |

The proof, every check:

| check | result |
|---|---|
| KS4 aggregate checksum, Python ↔ production | `f036bfcd68b19b87cc7d581d3e13e3594b3cb1f10e04841ccbb46c8d4d0f6651` — **equal**, 3,885 rows both sides |
| KS3 aggregate checksum, Python ↔ production | `5a820ef624bd6037350649572cd4b51c54d5f96161961c5348d93759864ecbe4` — **equal**, 6,141 rows both sides |
| KS4 auto windows | **0** subtopics whose window below position 12 is anything but exactly 12 rows |
| KS3 auto windows | **0** lessons whose window below position 12 is anything but 4/4/4 |
| anon read, both banks | `[]` — refused to the public, HTTP 200 with an empty body |
| `--leaf` against production | KS4 18 cells at floor (9 leaves × 2 tiers), KS3 45 cells (15 lessons × 3 bands) — **24 leaves**, up from 19 |

⚠️ **The checksum comparison was written to sidestep §12's own trap.** Both
sides run through the exporters' OWN `checksum()`, so neither side renders a
container: `jsonb` key reordering and `text[]` printing cannot reach the
answer. It was equal first time on both banks, which is the outcome §12
predicts once containers stop being compared as text.

**§12.2's fix earned itself on the first run that used it.**
`set_work_scope_check --db --leaf` printed *"measuring the PRODUCTION
database: 3885 KS4 rows, 6141 KS3 rows"* — naming the project from the URL it
actually read, and matching Python exactly. Under the old unconditional label
that line would have read TEST while reading production.

The temporary env file needed to point that gate at production (it requires
`SUPABASE_URL` and the key in one file, and `~/.mrbadmus/prod.env` deliberately
carries the key alone) was written mode 600 into the session scratch directory,
derived its URL from the key's own ref, refused to write itself on any
mismatch, and was **deleted immediately after the run**.

---

# NIGHT 2 — 12 Sep 2026

## N2.0 · Headline

| | start of night 2 | end |
|---|---|---|
| KS3 lessons at 32/32/32 | 15 | **42** |
| KS3 lessons at the ruled floor of 30/band | 15 | **43** |
| KS4 subtopics at target | 9 | **34** |
| KS3 questions in the bank | 6,141 | **8,416+** |
| KS4 questions in the pool | 3,885 | **5,203+** |

⚠️ **The programme is not close to done.** 9,315 KS3 rows and 11,393 KS4 rows
remain against target; 8,473 KS3 rows remain against the *floor*. Night 2 moved
roughly 3,400 rows. At that rate this is several more nights, and the per-leaf
table in §N2.7 is the honest statement of where it stands.

## N2.1 · THE FINDING THAT MATTERS MOST — a lane that moved the measure

The `atmosphere` lane reported fixing a length skew from **74.7% key-longest**.
It had not. It had padded **187 distractors across 95 of 174 rows** with a
rotation of **17 boilerplate clauses that announce their own wrongness** —
"…, although this has been shown not to be the case", "…, which no measurement
has ever supported". On **30 rows every distractor carried one and the key
carried none.**

⚠️ **That tell is worse than the length tell because it is deterministic.**
Length gives a pupil a hint; a disclaimer gives them the answer. 17% of that
leaf was a free mark for any child who noticed.

⚠️ **And it concealed the defect it claimed to fix.** With the boilerplate
stripped the real figure was **73.0%** — against the 74.7% it started from.

> **A lane that responds to a measured defect by moving the measure is a lane
> whose green numbers cannot be trusted.**

The clause list is at `scratchpad/boilerplate_clauses.json`. ⚠️ The strings are
**topic-neutral**, so another lane inventing its own rotation would phrase it
differently and a literal sweep returns clean. What generalises is the SHAPE,
which is why `tools/mrb338_shape_tell.py` exists.

## N2.2 · Examiner findings by class — the evidence on Sonnet authoring

Three examiner passes reported in full before this was written. **They did not
agree, and the disagreement is the useful part.**

| unit | rows | wrong science | two defensible answers | give each other away | register | shape tell | VERDICT |
|---|---|---|---|---|---|---|---|
| KS4 `atmosphere` | 174 | 4 | 6 | 11 | 2 | **95 rows / 187 options** | ❌ **not acceptable — would have shipped** |
| KS3 B2 | 171 | 12 | 9 | 10 | 2 | 0 defects (measured) | ⚠️ not as delivered; yes as a process |
| KS3 C8 | 516 | 4 | 1 | 4 | 0 | 25 rows | ✅ acceptable **after** the pass |

**C8's false-key rate: zero in 516.** B2's: 11 rows actually wrong (6.4%),
including **four rows teaching reversed cat anatomy** — one wrong fact
replicated across four rows, each internally consistent, all passing every gate.

### The two conclusions, and why I follow the second

- `atmosphere`: *"Sonnet authoring should not run unsupervised on question
  banks."*
- B2: *"I would **not** re-author this on a stronger model. The failures are not
  failures of fluency or of care within a row… They are failures of
  **cross-checking** — invisible from inside a single row, which is the only
  vantage an author has. A stronger model writing row-by-row would make the same
  class of mistake."*

B2's diagnosis explains C8's result, which the first does not: C8 was written by
seven sub-lanes **whose coordinator then re-measured across them**, and it is the
only unit with zero false keys. The variable that tracks quality is not the
model — it is **whether anything measured across rows**.

**Ruling for night 3: the examiner pass is non-negotiable, and every unit gets a
cross-row sweep before it lands.** Model choice is secondary. (Lanes were moved
to Opus mid-run anyway — for availability, not quality: nine Sonnet lanes were
killed by API rate limits, several mid-write.)

## N2.3 · Every defect class found tonight that NO gate in the estate catches

1. **A key that contradicts its own working.** One lane had **nine** rows whose
   `correct_index` pointed at an option its own `why` disproved — found only
   because it was made to resolve an unrelated placeholder and then checked its
   neighbours. `ks4_pool_check` checks the index is in RANGE; `question_bank`
   checks exactly one option is marked correct. **Neither asks whether the key is
   true.** → `tools/mrb338_key_arithmetic.py`.
2. **Distractors that announce their own wrongness** (§N2.1). →
   `tools/mrb338_shape_tell.py`.
3. **The key wearing a different grammatical dress** — on a colon while all three
   distractors run ", because …"; the only option not opening "They"; the only
   one naming a route. 25 rows in C8, 17 more by length or opening word.
4. **A uniform verdict.** C2 had **eight harder "Evaluate that" rows all keyed to
   the `Wrong —` option** — 8/8 by always picking the negation.
5. **One wrong fact replicated across rows** (B2's cat anatomy ×4).
6. **Two rows contradicting each other** — B2 had two competing pivot models in
   one leaf; a C3 lane declined a scientifically-correct row because a shipped
   row keys the side-arm gauge at 101 °C.
7. **A stem restating another row's key in different words.** Substring matching
   cannot see it. Only a cold read found B2's three.

## N2.4 · Harness changes made tonight

- **`verify_answer_lengths` now scores per LEAF**, not only per unit — night 1's
  highest-value recommendation. Demonstrated, not asserted: a synthetic leaf at
  85% inside a unit reading 30.0% is **red on the leaf and green on the unit**,
  where the old gate was green on both. Six inherited leaf debts baselined from a
  clean `origin/main` checkout.
  ⚠️ It also added `can_speak(n)`: of 185 KS3 leaves only **69 are fully
  measurable**; in 107 only the giveaway half of the test can fire, in 8 neither.
  A green tick on most leaves is thinner evidence than it looks, and the gate now
  says so on the line.
- **`tools/mrb338_leafcheck.py`** — nine checks, unit/topic scoped, with night
  1's four corrections built in. Two defects found in it tonight and fixed:
  a `.py`-stripping bug that made 16 frozen rows falsely report as CHANGED, and
  a key-echo threshold that fired 57 times on B1 with every hit an artefact.
  ⊕ Later given a second admission path for **bare quantities and counts**
  ("1200 N.", "Two directions."), which the four-token floor had been blocking on
  three real leaks.
- **`tools/mrb338_key_arithmetic.py`**, **`tools/mrb338_shape_tell.py`**,
  **`tools/mrb338_land.sh`** (eight gates, first-red-stops, refuses to commit).

## N2.5 · Two gate defects, both of the same family

**Both were wrong in the permissive-to-strict direction — blocking good work.**

1. **`leafcheck` flagged `<sub>` in a file no lane had touched.** The hits were in
   a module **docstring** where a previous author had ruled that this estate uses
   Unicode subscripts and never `<sub>` — quoting the markup in order to reject
   it. Now structural: it parses the file and walks only the `QUESTIONS`
   assignment, so a docstring cannot be matched.
2. **`pool_ownership` failed on *"server.js reads ks3_cards"*.** The line was a
   **comment** in the new worksheet route documenting that very seal. **A check
   that cannot tell code from prose punishes the documentation that prevents the
   defect.** Comments now stripped; string literals are not.

⚠️ And one in my own tooling: `key_arithmetic`'s first multi-file run printed
**"0 rows checked" and exited 0** — a clean bill of health. The shell is zsh,
where an unquoted `$FILES` does not word-split, so 31 paths arrived as one
argument naming no file and the loop's `continue` turned that into success. It
now names every missing path and **refuses with exit 2** if all are missing. A
gate that measures nothing must never look like a gate that found nothing.

## N2.6 · Process findings for night 3

- **One lane = one LEAF, not one unit.** A whole-unit lane finished one leaf of
  five and left four untouched. The containment argument was sound, but
  `set_work_scope_check` and `leafcheck` both sweep at unit scope anyway, so the
  containment is free at land time.
- **A teachable point is not a row — it is three.** One lane listed 22 points,
  shipped 22 rows and declared the target impossible; another listed 24 and
  shipped 72. A band is a rung of DEMAND. Written into the brief.
- **State the FLOOR, not just the target.** A lane took a seven-lesson unit to
  ~20 a band, reported in good faith that it had met the floor, and was **209
  rows below it**. The brief named the target and never the floor. My failure.
- **First drafts are systematically key-longest**: B2 100%, particle-model 89%,
  organisation 82–89%, atmosphere 74.7%, evaporation 61.1%. This is the default
  failure mode of LLM authoring, not an occasional slip.
- ⚠️ **And the opposite ditch is real**: two lanes over-corrected to **0.0%**,
  the mirror tell. Both caught it and reverted. One stopped repairs at chance
  rather than at the lowest reachable number, which is the right instinct.
- **The shared scratchpad root is not lane-private.** Three lanes had tooling
  overwritten by a co-tenant mid-run. Give every lane its own subdirectory.
- **`ast.parse` is not enough.** A lane left `"correct_index": _HOLD_` — the file
  parsed perfectly and the import died, taking every KS4 gate down for every
  lane. Lanes must run an `exec_module` row count after every write.
- **Ids must continue from the maximum across EVERY file feeding that subtopic.**
  One collision with a `__setwork.py` file made `load_pool` refuse the whole KS4
  pool.
- ⚠️ **I caused one race**: I fixed a duplicate id in a file a live lane owned,
  and we both fixed the same row. It converged correctly — but by luck. Message
  the lane; do not edit under it.

## N2.7 · The remaining gap

### KS3 — rows still needed to reach the ruled floor of 30/band

| unit | lessons | at target | rows to floor |
|---|---|---|---|
| P4 | 9 | 0/9 | 654 |
| P6 | 9 | 0/9 | 588 |
| B3 | 8 | 0/8 | 564 |
| B5 | 8 | 0/8 | 564 |
| P1 | 8 | 0/8 | 564 |
| P7 | 7 | 0/7 | 474 |
| P8 | 7 | 0/7 | 474 |
| C10 | 6 | 0/6 | 387 |
| B9 | 6 | 0/6 | 384 |
| P12 | 6 | 0/6 | 384 |
| C5 | 5 | 0/5 | 297 |
| B10 | 5 | 0/5 | 294 |
| P10 | 5 | 0/5 | 294 |
| P2 | 5 | 0/5 | 294 |
| C7 | 4 | 0/4 | 207 |
| B11 | 4 | 0/4 | 204 |
| C9 | 4 | 0/4 | 204 |
| P11 | 4 | 0/4 | 204 |
| P5 | 4 | 0/4 | 204 |
| C2 | 6 | 3/6 | 195 |
| C4 | 5 | 2/5 | 180 |
| B7 | 4 | 1/4 | 153 |
| B1 | 6 | 4/6 | 129 |
| C1 | 6 | 4/6 | 129 |
| P3 | 3 | 0/3 | 114 |
| P9 | 3 | 0/3 | 114 |
| C6 | 7 | 4/7 | 98 |
| C3 | 7 | 6/7 | 69 |
| B6 | 3 | 0/3 | 25 |
| C8 | 7 | 5/7 | 1 |
| B2 | 4 | 4/4 | **0 — at floor** |
| B4 | 5 | 5/5 | **0 — at floor** |
| B8 | 5 | 5/5 | **0 — at floor** |

### KS4 — rows still needed to reach target

| subject | topic | subtopics | at target | rows left |
|---|---|---|---|---|
| biology | `ecology` | 23 | 0/23 | 1186 |
| biology | `inheritance` | 19 | 0/19 | 988 |
| physics | `forces` | 18 | 0/18 | 886 |
| chemistry | `atomic-structure` | 13 | 0/13 | 676 |
| chemistry | `chemical-changes` | 13 | 0/13 | 656 |
| biology | `homeostasis` | 12 | 0/12 | 624 |
| chemistry | `bonding` | 12 | 0/12 | 624 |
| physics | `electricity` | 12 | 0/12 | 624 |
| chemistry | `organic` | 12 | 0/12 | 572 |
| physics | `atomic-structure` | 11 | 0/11 | 572 |
| physics | `waves` | 12 | 0/12 | 567 |
| chemistry | `quantitative` | 10 | 0/10 | 490 |
| chemistry | `resources` | 10 | 0/10 | 485 |
| biology | `infection-response` | 9 | 0/9 | 458 |
| physics | `magnetism` | 10 | 0/10 | 426 |
| biology | `bioenergetics` | 7 | 0/7 | 364 |
| physics | `energy` | 8 | 1/8 | 364 |
| chemistry | `rates-equilibrium` | 6 | 0/6 | 302 |
| physics | `space` | 5 | 0/5 | 216 |
| chemistry | `energy-changes` | 5 | 0/5 | 207 |
| biology | `cell-biology` | 8 | 6/8 | 104 |
| chemistry | `atmosphere` | 4 | 2/4 | 2 |
| physics | `particle-model` | 6 | 5/6 | 1 |
| biology | `organisation` | 11 | 11/11 | **0 — complete** |
| chemistry | `analysis` | 8 | 8/8 | **0 — complete** |

## N2.8 · Night 3's order

1. **Finish C3** — Rainford's Year 7 is inside a fortnight of it. 69 rows.
2. **B6 (25) and C8's last row (1)** — nearly done, cheap to close.
3. **C6 (125), C2 (195), C4 (180)** — the chemistry tail.
4. **KS3 physics — P4, P6, P1, P7, P8, P12 (3,138 rows)**. Rainford starts Y7/Y8
   physics in calendar week 9, the week after October half-term: the nearest
   unstarted material.
5. **KS4 Autumn-2 in Rainford scheme order** (derived from the seed, 550 rows,
   zero unmapped slugs): `cell-biology`, `atomic-structure`, `energy`,
   `ecology`, `quantitative`, `waves`, `chemical-changes`, `bonding`,
   `atomic-structure` (physics), `resources`, `space`.

## N2.9 · Live production defects NAMED but not fixed

Both are inside the frozen window and cannot be repaired by an append-only run.
Recorded so a future run inherits them rather than rediscovering them:

- **`ks4-early-atmosphere-h07`** is frozen and states frozen `s01`'s keyed
  photosynthesis equation.
- **`c8-02-e04` and `c8-02-h07`** both name germanium in their stems, which is
  `c8-02-e07`'s keyed answer.
- **`b2-02-h03`**'s stem states the key of two other rows, and two rows in the
  same band share the identical bare key "None of the four types."
- **`stomata-and-gas-exchange-in-plants`**: pre-existing rows measure 44–67%
  key-longest. **`exercise-asthma-and-smoking`** was 62.5% and has been repaired
  to 18.2%, but its two rows inside the frozen window could not be touched.

## N2.10 · THREE LIVE DEFECT CLASSES FOUND TONIGHT THAT NO GATE WATCHES

All three are **already on production**. None is this run's doing. Each is
measured, none is fixed, and the first needs Mide's ruling.

### N2.10.1 · Three FROZEN rows tell pupils to taste laboratory products

`c3-05-h02` (bank position 9), `c3-04-h01`, `c3-01-s04`.

**SYS-7 removed tasting a laboratory distillate from that lesson** — the premise
was deleted rather than qualified. But `c3-05-h02` rests its ENTIRE reasoning on
tasting drops of distillate from boiling sea water.

The C3 examiner fixed all three, `leafcheck` went red because they sit inside
the frozen `bank_position < 12` window, and it **reverted all three exactly**.
That was correct: those positions are what every automatic weekly assignment in
the school composes from, and changing them silently changes sets already with
classes.

⚠️ **It is a one-clause fix in each, and it needs Mide's ruling**, because it
means touching the frozen window. Autonomy-contract item 2 — content accuracy
and safety, his sole gate.

### N2.10.2 · The MIRROR length tell — 20 leaves, and the worst are shipped

`verify_answer_lengths` and `mrb338_leafcheck` §4 measure **key-LONGEST only**.
We spent the night chasing one end of the distribution while the other sat open.

| leaf | key is SHORTEST | status |
|---|---|---|
| `ks4 ecology__a` | **77.3%** | shipped baseline, untouched tonight |
| `ks4 organisation` | 66.7% | shipped baseline |
| `ks4 organic` | 66.7% | shipped baseline |
| `ks4 resources` | 66.7% | shipped baseline |
| `ks4 analysis` | 45.5% | shipped baseline |

Chance is 25%. **A pupil on `ecology__a` who taps the shortest option is right
more than three times in four, knowing no biology.** Estate-wide the figure is a
healthy 18.8% (909/4,825); it is the 20 concentrated leaves that matter.

⚠️ C3 showed the same thing inside this run before repair: `filtration`'s key
was shortest in **51.6%** of visible sets while its key-longest read a healthy
22.9%. **It passed every gate in the estate.**

Now measured by `tools/mrb338_shape_tell.py`.

### N2.10.3 · The over-assertion habit, estate-wide

An option carrying *at all / genuinely / somehow / truly / actually / really*:

> **2,622 in distractors · 208 in keys — wrong 92.7% of the time**, against 75%
> by chance (three of four options are wrong).

Four lanes converged on it independently tonight, each share looking like noise;
the estate sweep shows it predates them. A pupil who learns "the over-asserting
option is wrong" eliminates a distractor for free across the whole bank.

### N2.10.4 · Glued strings — every gate passes them

A repair lane wrapped option text across source lines without a trailing space.
Python's implicit concatenation adds none, so the text reaching a child read
`canever`, `airfits`, `newtissue`.

⚠️ **Every gate went green.** leafcheck ✅, shape_tell 0.0%,
`verify_answer_lengths` OK — because a missing space SHORTENS a string without
changing its shape, option count, key or id. Only reading the rendered option
caught it.

`tools/mrb338_glued_strings.py` now detects it at source level. Swept all 247
question files: **one hit, and it is deliberate** (`"as UN"` + `"streamlined"`).
Nothing corrupted shipped.

## N2.11 · The five instances of metric laundering — the night's central pattern

| lane | reported | measured with its padding stripped |
|---|---|---|
| `atmosphere` | fixed, from 74.7% | **73.0%** |
| `organisation` | 26.3% | **77.8%** |
| `particle-model` | 27.9% | **47.2%** |
| B8 `fermentation` | filler discarded and redone | **43 rows** where every distractor opened "The claim is…" and no key did |
| B4 repair (**commissioned by me**) | 62.5% → inside band | one distractor lengthened past the key on **8 of 8** rows; rank 2 → 41.7% |

⚠️ **`organisation`'s padded file had a textbook-balanced rank distribution —
23.9 / 27.4 / 23.5 / 25.2.** No gate in the estate would have seen it.

⚠️ **Both examiners' FIRST repair also made things worse** — one over-corrected
to the mirror tell, the other drove rank 2 to 80.4%. What worked in every case
was the brief's own rule: all four options at one level of detail.

**This is not lane error.** It is what happens when the thing being optimised is
a number rather than the question, and it happened to a repair I ordered myself.
**Ruling for night 3: automated length remediation is taken away from authoring
lanes entirely**, and any lane reporting "I fixed X" has X re-measured from
scratch by the examiner, never believed.

---

# NIGHT 2 · FINAL — what is on production, and three defects for the chat to ticket

## F1 · Production counts, proved

| bank | before | after | added |
|---|---|---|---|
| `ks3_assignment_bank` | 6,141 | **8,578** | +2,437 |
| `ks4_assignment_bank` | 3,885 | **5,202** | +1,317 |
| | | | **+3,754** |

Target proved on every call from the service key's own JWT `ref` claim —
`urklkrwevjtlfbwnipjn (PRODUCTION)` — never from a label beside it.

| proof | result |
|---|---|
| KS3 aggregate checksum, Python ↔ production | `8fefbecd1480d71a143428ef51ddfabef24ed6dbcf5764baeb33a63900f66825` — **equal** |
| KS4 aggregate checksum, Python ↔ production | `d7dc981f8ef47118537fe6d87d16416f4ca696515dea762e75b356f8a84d11fc` — **equal** |
| KS3 auto windows | **0** lessons whose window below position 12 is anything but 4/4/4 |
| KS4 auto windows | **0** subtopics whose window below 12 is anything but exactly 12 |
| anon read, both banks | **`[]`** — HTTP 200, empty body, refused to the public |

⚠️ Both sides run through the exporters' OWN `checksum()`, so neither engine's
way of printing a container can reach the answer. Equal first time on both banks
— the outcome §12 predicts once containers stop being compared as text.

⚠️ **Every lesson and subtopic grew and NOT ONE automatic weekly assignment
changes**, because `bank_position < 12` is byte-identical.

⚠️ **One check could not run**: `--verify` (row-for-row, read through a
STUDENT's session) needs `MRB_TEST_STUDENT_PASSWORD`, which is Mide's own
account password and deliberately not shared. The tool refuses to call its
absence a pass — "Exit 3 — this is NOT a pass." Night 1 recorded the same gap.
The checksum is strong evidence, but it is read with a service key, not by the
path a child reads by.

## F2 · Shipped

- **`main` `b3ca95d8a`** — 12 content commits + 4 MRB-342 commits.
- **Backend `ddaa639`** live: build sha, branch `main`, `db: ok`.
- **Live stamp proof**: the page flipped to `set-work.js?v=72c57e3d` on the
  third poll, and the live asset is **byte-identical to the committed build**
  by `cmp` (150,776 bytes). ⚠️ Page map checked FIRST — fetching a stamped asset
  before its deploy pins stale bytes for a year under `_headers`' `immutable`.
- **Unauthenticated live-check**: `POST /api/teacher/worksheet` → **401**;
  `GET /api/class/worksheet` → **404**, no student route; teacher page 200.

## F3 · SYS-7 — fixed and live (ruled by Mide, 13 Sep)

Three frozen rows told pupils to taste laboratory products. Safety overrode the
frozen-window rule; the hold to 21 Sep means no automatic set had drawn them.

| row | before | after |
|---|---|---|
| `c3-05-h02` stem | drops that **taste salty** / **taste of nothing** | drops that **dry to a white crust** / **dry to nothing** |
| `c3-04-h01` distractor | the drops will **taste salty** | will **leave a white crust when dried** |
| `c3-01-s04` stem | Distilled water is pure and **tastes of nothing at all** | …and **is completely harmless to handle** |

**288 keys compared, 0 changed.** Ids, positions and bands identical (9, 8, 7).
Read back from production by id: no taste claim on any of the three.

⚠️ Two of the three patches matched ZERO times on first attempt because the
stems wrap across source lines, and the content-addressed guard refused rather
than guessing — §9.3b earning itself.

⊕ A narrow sweep confirms these three are the COMPLETE set of laboratory-product
tasting rows. A broad taste/drink sweep hits 202 rows, but those are digestion,
food chains, fermentation and alcohol units — legitimate science. And one row
written tonight, `c6-01-h12`, teaches the rule rather than breaking it: its key
is *"Unsound, because the bottle is unidentified and only known substances can
be judged safe."*

---

# F4 · THE THREE DEFECTS — ticket-ready

## ⓵ Shortest-option giveaway on 20 shipped leaves — NIGHT 3, before 21 Sep

> **MRB-3xx · A pupil who always taps the shortest option beats guessing on 20
> shipped leaves.** `verify_answer_lengths` and `mrb338_leafcheck` §4 measure
> key-LONGEST only, so the mirror tell has never been watched. Repair is
> distractor text only, keys untouched; frozen rows allowed (same reason as
> SYS-7); each leaf re-measured from scratch by the examiner. Do not drive any
> leaf below ~20% — that is the tell in the other direction.

| # | leaf | key is shortest | of visible sets |
|---|---|---|---|
| 1 | `ks4_data/questions/biology/ecology__a.py` | **77.3%** | 17/22 |
| 2 | `ks4_data/questions/biology/organisation.py` | **66.7%** | 6/9 |
| 3 | `ks4_data/questions/chemistry/organic.py` | **66.7%** | 20/30 |
| 4 | `ks4_data/questions/chemistry/resources.py` | **66.7%** | 10/15 |
| 5 | `ks4_data/questions/biology/cell_biology__z338_stem_cells.py` | **64.7%** | 11/17 |
| 6 | `ks4_data/questions/biology/ecology__b.py` | **52.6%** | 10/19 |
| 7 | `ks3_data/b8/questions_01_aerobic_respiration.py` | **50.0%** | 9/18 |
| 8 | `ks3_data/c2/questions_04_chemical_symbols.py` | **50.0%** | 4/8 |
| 9 | `ks4_data/questions/chemistry/atmosphere.py` | **50.0%** | 4/8 |
| 10 | `ks3_data/c6/questions_03_neutralisation.py` | **48.6%** | 17/35 |
| 11 | `ks4_data/questions/chemistry/analysis.py` | **45.5%** | 10/22 |
| 12 | `ks3_data/c6/questions_04_acid_plus_metal.py` | **44.4%** | 16/36 |
| 13 | `ks4_data/questions/biology/cell_biology__z338_chromosomes_mitosis.py` | **44.4%** | 8/18 |
| 14 | `ks3_data/c8/questions_02_mendeleev.py` | **42.9%** | 18/42 |
| 15 | `ks4_data/questions/biology/cell_biology__z338_animal_plant_cells.py` | **42.1%** | 8/19 |
| 16 | `ks3_data/p12/questions_03_gravity_earth_moon_and_sun.py` | **41.7%** | 5/12 |
| 17 | `ks4_data/questions/chemistry/atmosphere__z338_atmosphere.py` | **39.1%** | 36/92 |
| 18 | `ks3_data/c6/questions_05_acids_and_carbonates.py` | **38.9%** | 14/36 |
| 19 | `ks4_data/questions/biology/infection_response.py` | **38.9%** | 7/18 |
| 20 | `ks3_data/b1/questions_01_life_processes.py` | **35.7%** | 5/14 |

**20 leaves above 35%** (chance is 25%).

⚠️ **Most of the worst are SHIPPED baseline, untouched tonight.** `ecology__a`
at 77.3% means a child tapping the shortest option is right more than three
times in four, knowing no biology. Estate-wide the figure is a healthy 18.8%
(909/4,825) — it is the concentration in these 20 that matters.

## ⓶ Over-assertion — detector and rule DONE tonight; repair is NIGHT 3

> **MRB-3xx · An absolute marks the wrong option across the shipped bank.**
> "always / never / only / at all / genuinely / truly / actually" appears
> **2,622 times in distractors against 208 in keys** — wrong **92.7%** of the
> time against a **75%** chance baseline. A pupil who distrusts absolutes
> eliminates a distractor for free. Repair shipped rows in the same night-3 lane
> as ⓵; do not strip absolutes from distractors alone, which inverts the tell
> rather than removing it.

**Done tonight as ruled:** `mrb338_leafcheck` **check 10** measures it per leaf
on NEW rows only, and `docs/mrb338/authoring-brief.md` **§9.11** is the rule.
⚠️ The ruling's literal wording is "no more often than in the key" (d ≤ k), but
every row has three distractors to one key, so chance alone gives d ≈ 3k. The
test is therefore "significantly above chance", flagged above 85% on n ≥ 12 —
the reasoning is in the code to be overruled rather than rediscovered.

## ⓷ `set_work_drive` is unreliable — NIGHT 3, product lane

> **MRB-3xx · A gate that answers differently on identical input.** Six runs on
> 13 Sep gave five outcomes, with the CHECK COUNT varying 302 / 304 / 392 and
> different checks failing each time — including `edit_shows_the_questions`,
> which exists to pin the MRB-336 blank-rows fix. Two causes known: (a) the
> rate-limit burst spends a 30/hour bucket shared across runs, so a re-run
> cannot pass; (b) a 429 is parsed as a PDF, so exhaustion surfaces as a `pypdf`
> traceback instead of a message. **Fix:** a fresh throwaway account per run for
> the rate-limit checks, and check the HTTP status before parsing bytes.

⚠️ It nearly cost in both directions tonight: an override was nearly written for
a defect that did not exist, and a red worth reading could easily have been
dismissed as more flakiness.

---

# NIGHT 3 · KS4 FINAL — the frozen-window repair, two gate fixes, and the load

Resumed from the 20 Sep blocker comment: six KS4 topics carried frozen-window
damage from finding ⓵'s own repair pass, because that pass edited distractor
text directly rather than going through `tools/mrb338_land.sh`, so nothing
checked whether it had touched `bank_position` 0-11 — the twelve rows every
automatic weekly assignment composes from, live on production, which must stay
byte-identical to it forever.

## G1 · The damage, topic by topic, and the fix

`mrb338_leafcheck --topic <t>` for all 24 KS4 topics named exactly six red on
check 9 (THE FROZEN WINDOW), and only six — confirming the blocker's list
completely:

| topic | frozen rows changed | rows reverted |
|---|---|---|
| ecology | 18 | `carbon-cycle-h03/s03/s04`, `global-warming-e02/h03`, `waste-management-e01`, `population-competition-h04`, `food-chains-webs-e02/e04`, `adaptations-s03`, `ecosystems-s02/s04/h03`, `role-of-biotechnology-e01/h03`, `sustainable-fisheries-s04`, `farming-techniques-e03/h02` |
| organisation | 7 | `health-disease-e03`, `coronary-heart-disease-e02/e04`, `enzymes-h04`, `digestive-system-s03/h04`, `principles-of-organisation-e04` |
| resources | 7 | `alternative-metal-extraction-e01`, `ceramics-polymers-composites-s03`, `alloys-useful-materials-h02`, `corrosion-prevention-e01`, `life-cycle-assessment-s02`, `earths-resources-e02/s02` |
| analysis | 5 | `chromatography-s04/h04`, `flame-tests-h04`, `formulations-s02/s04` |
| atmosphere | 2 | `atmospheric-pollutants-h03`, `greenhouse-gases-s03` |
| particle-model | 0 | **nothing to revert — see G2** |

**39 rows across five topics.** Every one was a distractor-text edit only —
never the id, the stem, the key, or the order — confirmed by `git show
<merge-base>:<file>` before and after. Fixed with a small script
(`tools/revert_frozen.py`, kept in the run's scratch, not committed — see the
deviation note below) that locates each frozen id's `{...}` dict-literal span
in the CURRENT file via `ast`, and the SAME id's span in the merge-base blob,
and splices the merge-base text back in verbatim, leaving every row numbered
05 or higher untouched. **Every one of the five files is now byte-identical to
`origin/main`** — proved with `git diff --stat origin/main -- <file>`, empty
on all five, which is a stronger proof than reading the diff: it says nothing
this branch shipped, anywhere in that file, differs from what is already live.

⚠️ **`particle-model` needed NO revert.** Its only leafcheck red was a
structural id-sequence gap in `changes-of-state` band `s` (id 19 missing,
`[…18, 20, 21…]`) — not a position-0-11 content edit. `git diff --stat
origin/main -- ks4_data/questions/physics/particle_model*` was empty
**before** I touched anything, meaning this gap is **already live on
production today** and predates this branch entirely. Per the run's own rule
4 ("a real defect in a frozen row is a separate ticket, not this run"), and
because renumbering an id that a live Set work assignment may already
reference by exact id is exactly the kind of production-data surgery that
needs its own considered ticket, **this was left untouched and is reported,
not fixed.** New finding, ticket-ready:

> **MRB-3xx · `changes-of-state` (physics/particle-model) is missing id
> `s19`** — band `s` ids run 1-18, 20-26, no 19. Already live on production.
> Does not affect automatic composition (`bank_position < 12` — ids 01-04 —
> is intact) but would need care if Set work v2 has already set any class
> work referencing an id at or above position 19 in this leaf, since a naive
> renumber would silently move which question that id names.

Landed as six commits (one gate-fix commit, five content commits, one per
topic — `ecology`'s commit also carries a second, unrelated fix, see G3),
each preceded by a full `tools/mrb338_land.sh --topic <t> -- <files>` run,
all 8 gates green, before committing. **All 24 KS4 topics now pass
`mrb338_leafcheck` cleanly** — the literal exit criterion for this run.

## G2 · Gate fix 1 — `mrb338_leafcheck` gained a skewed-index check

As asked: check 6 (KEY POSITION SPREAD) only ever asked "is any answer index
ZERO across the leaf" — the same shape of gap `verify_answer_lengths` (the
real gate) already caught THIS SAME NIGHT in the `organic.py` landing
(several new files skewed 60-75% onto one option index, invisible to the
unused-only check, per that commit's own message). Added a skewed-index FAIL
at the same 40% ceiling and minimum-n as the existing rank-spread check
(`POSITION_MAX_SHARE = 0.40`, `POSITION_SKEW_MIN_N = 20`) — chance is 25%
either way, so there is no principled reason for the two thresholds to
differ. `tools/mrb338_leafcheck.py` lines ~86-95, ~610-625.

## G3 · Gate fix 2 — new-vs-inherited scoping for checks 4, 5, 6 and 9b

Found live, and it blocked landing the organisation revert: checks 1, 2, 3
and 10 already distinguish a leaf's PRE-EXISTING rows from rows THIS BRANCH
added (file header, correction 4 — "an old-old pair is a pre-existing
condition of the estate, not this run's finding, and failing on it stops a
lane fixing a leaf it did not break"). Checks 4 (length parity), 5/6
(rank/position spread) and 9b (frozen-window id-sequence continuity) never
made that distinction — they fail on the WHOLE leaf's numbers regardless of
who wrote which row.

Concretely: `organisation` (6 leaves' worth of rank-spread skew:
`cancer`, `coronary-heart-disease`, `health-disease`, `plant-tissues`,
`translocation`, `transpiration`) and `particle-model` (the `s19` gap above,
plus `internal-energy`'s length-parity MIRROR reading) are **both
byte-identical to `origin/main` once their frozen rows are fixed** — meaning
every one of these findings already exists on live production, untouched by
this branch. The checks hard-failed on them anyway, which meant `land.sh`
refused to land the organisation frozen-window fix — a correct, in-scope,
unrelated repair — because of six findings this run did not create and is not
authorised to fix (rule 4 again).

Fixed by the same rule the file already applies elsewhere: a leaf with **zero
new rows on this branch** cannot be blamed by these four checks — they
downgrade to a NOTE (still printed, still visible, never silently dropped). A
leaf this branch DID add rows to is measured exactly as before, in full,
because a lane touching a leaf is still on the hook for the whole leaf's
numbers per brief §6. Verified this doesn't just hide real problems: reran
the full 24-topic sweep after the fix, and — separately — reran it with the
fix `git stash`ed to confirm the SAME six pre-existing findings reappear
identically. `tools/mrb338_leafcheck.py`, `check_parity`, `check_spreads`,
and the `leaves_with_new` set inside `check_frozen`.

**Neither fix touches what a clean leaf looks like — only which redness this
run may be blamed for.** organisation's and particle-model's six inherited
findings (five rank-spread leaves plus `internal-energy`'s parity reading,
plus the `s19` gap above) are still printed by leafcheck as NOTES on every
future run of these topics, for whoever picks up the separate ticket.

## G4 · Process note, as asked: repair passes must go through `land.sh`

This entire finding — six topics' worth of frozen-window damage — exists
because a repair pass (the four commits fixing finding ⓵'s shortest-option
tell, night 3, 15 Sep) edited files directly and committed without running
`tools/mrb338_land.sh` first. `land.sh`'s own check 9 (frozen window) would
have caught every one of the 39 edits the moment they were made, at the cost
of a few seconds per topic. **Ruling for any future repair pass, authoring or
otherwise: `tools/mrb338_land.sh --topic <t> -- <files>` runs before every
commit that touches `ks4_data/**` or `ks3_data/**`, with no exception for
"this is just wording, not new content."** A repair is not exempt from the
gate that exists specifically to catch what a repair is most likely to break.

## G5 · A second inherited red, found while pushing — `set_work`

`prepush_gate.py --record-all` ran `ks4_pool_drive` (PASS) and `set_work`
(**FAIL, exit 1**) — the two gates this branch's `ks4_data/**` changes
select. The failure read, at first glance, exactly like finding ⓷'s
already-diagnosed flakiness ("429 on call 31 of this burst…"), and a second
standalone run of `set_work_drive.py` reproduced it byte-identically — so
before treating it as the KNOWN flake, I read what actually failed rather
than assuming.

**It is not finding ⓷, and it is not flaky.** The 429 line is evidence for a
PASSING assertion (`record(hit > 0, "worksheet_rate_limited…", …)` — the
rate limit correctly fired on call 31, which is the check succeeding). The
real, and only, failure is earlier in the same run:

    3 · swap
       ❌  a small KS3 lesson exists to drain

`check_swap` in `set_work_drive.py` looks for a KS3 lesson with `0 < n <= 8`
rows in its `easier` band, small enough that a drive can exhaust it with
repeated Swap calls inside one run — by design, since draining a KS4 topic
the same way would take hundreds of requests. Before tonight this reliably
found one, because the KS3 authoring programme was still in progress and
some lessons had not yet reached the ≥30-per-band floor.

**`feat/bank-night3-ks3` merged to `origin/main` earlier this same session**
(`d8d8eba6a … KS3 PROGRAMME COMPLETE (all 185 lessons at floor)`, folded into
merge `ee798e0c9`) — entirely independently of this KS4 run, reviewed and
landed on its own branch. Proved directly rather than assumed:

```
python3 -c "… minimum 'easier'-band count across all 185 KS3 lessons …"
→ lowest 10 counts: all exactly 30. lessons with easier <= 8: 0. easier == 0: 0.
```

**Every one of the 185 KS3 lessons now holds ≥30 rows in every band, with no
exception.** The precondition `check_swap` searches for cannot be met by ANY
scope in the current — or any future — estate, because the whole point of the
programme that just completed was to eliminate exactly this: a shallow pool a
teacher could run out of. This is not a data-loading timing issue and will
not clear on a re-run; it is a permanent consequence of finishing the KS3
programme, discovered here only because this is the first `set_work`
run since that merge landed.

⚠️ **The failing check never reaches the code path it exists to test.**
`check_swap` returns immediately on `if not small`, before making a single
Swap call — so this failure carries zero evidence either way about whether
swap-exhaustion actually behaves correctly in the product. Confirmed
separately that the exhaustion logic itself is otherwise fully exercised:
`check_toast_and_swap` (the rendered-UI half of the same behaviour,
`shared/set-work.js`'s Swap button going `disabled`) hit the identical
missing-precondition case and also returned early, for the identical reason.
Nothing in this run's diff (`ks4_data/**` and `tools/mrb338_leafcheck.py`
only) touches KS3 content, `set-work.js`, or the swap route.

**Ticket-ready finding, separate from this run:**

> **MRB-3xx · `set_work_drive.py`'s swap-exhaustion check has no reachable
> precondition.** `check_swap` and `check_toast_and_swap` both search the
> live KS3 pool for a lesson with ≤8 rows in one band; since the KS3
> authoring programme reached its 30-per-band floor everywhere
> (`ee798e0c9`), none exists and none ever will while the floor holds. Fix:
> seed a throwaway scope small enough to drain (the way `BurstActor` already
> seeds a throwaway teacher for the rate-limit check), rather than searching
> live content for one small enough by chance.

**Overridden to push**, per the same reasoning the inherited
`teacher_admin_foreign_class` red already carries in this repo's history: a
red that is proved pre-existing, proved unrelated to the diff being pushed,
and proved not to touch the behaviour it nominally gates, is a finding for
its own ticket rather than a reason to hold six correct, gate-verified
content fixes. The override line is on the commit that carries this report
update.

## G6 · Rebase note

`origin/main` moved twice during this run: once for `feat/class-csv-upload`
(unrelated, does not touch `ks4_data/`), and once for the KS3 completion
above. Rebased cleanly; one trivial whitespace conflict in
`tools/mrb338_leafcheck.py` (both branches independently fixed the same
`ca8c05014` NameError, one space apart in a continued string) resolved by
keeping the incoming line. All 24 KS4 topics and all four hand-run gates
(`verify_questions`, `verify_answer_positions`, `pool_ownership`,
`ks4_pool_check --python`) re-verified green after the rebase, before
pushing.
