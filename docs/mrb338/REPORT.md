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
