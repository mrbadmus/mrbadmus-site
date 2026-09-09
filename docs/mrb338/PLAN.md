# MRB-338 · Bank expansion programme — NIGHT 1

**9 Sep 2026.** Branch `feat/bank-expansion-1`, off `origin/main` `d6c5d0ec8`
(which contains MRB-336). Content only.

Mide, 8 Sep: *"teachers will most likely set assignment on each topics, but
these topics don't have enough questions … at least 50 questions on each topic
for both foundation and for higher … the same thing should apply to ks3 for
each tier."*

"Topic" is the leaf a teacher taps in Set work v2 — a **KS4 subtopic**, a **KS3
lesson**. Topic and unit level have been ≥ 50 since MRB-335; the leaves have
not, and the leaf is what the sheet actually sets work on.

---

## §1 · Did night 1 already start? — No.

Checked before anything else, and all four say the same thing:

| probe | result |
|---|---|
| `git branch -a \| grep bank-expansion` | nothing |
| `git worktree list` | 13 worktrees, none of them this one |
| `ls docs/mrb338/` | did not exist |
| TEST bank counts | **KS3 5,142 / KS4 3,417** — the stated baseline, to the row |

So this branch is new, and nothing from this programme has been authored or
loaded. Worktree created at `d6c5d0ec8`.

---

## §2 · Two corrections to the brief, both found in the data

### ⚠️ 2.1 · There is no "16 Aug Rainford KS3 override seed"

The brief's §4.1 names one. It does not exist — the oldest Rainford-specific
seed in the repo is three weeks later. What exists is:

| file | rows | what it is |
|---|---|---|
| `supabase/seeds/20260906234500_rainford_ks4_overrides.sql` | 670 | Rainford KS4, Y9–Y11, **both tiers** |
| `supabase/seeds/20260907003000_rainford_ks3_overrides.sql` | 162 | Rainford KS3, Y7–Y9, from their own spreadsheet |

Both were used. ⚠️ The KS3 override's own header carries a **collision warning**
worth repeating: it and `20260726182000_ks3_school_schemes.sql` both open with
the same scoped DELETE of Rainford's KS3 rows, so *whichever is applied last
wins, silently*. That does not change this plan — the override is the later
file and is built from Rainford's real scheme — but it is a live ambiguity
about what the school's scheme actually is, and it is on Mide.

### ⚠️ 2.2 · `academic_week` is a LESSON ORDINAL, and at KS3 it restarts per subject

This one changes the leaf list, so it is the important one. The brief says
"every leaf taught in weeks 1–8". Taking `academic_week BETWEEN 1 AND 8`
literally would have authored **the wrong content for two of the three
sciences**.

At KS4 the column is the lesson ordinal from the start of the year and the
subjects run together, so `≤ 8` is Autumn 1 and the brief's reading holds.

At KS3 it restarts at 1 for **each subject**, and Rainford staggers the three:
the true calendar week is written into each row's `notes`.

| Y7/Y8 subject | first row's calendar week | `academic_week ≤ 8` would mean |
|---|---|---|
| Biology | week **1a** | weeks 1–4 ✔ Autumn 1 |
| Chemistry | week **5a** | weeks 5–8 ✔ Autumn 1 |
| Physics | week **9a** | weeks 9–12 ✘ **after October half-term** |

So the leaf list below is cut on the **calendar week parsed from `notes`** at
KS3, and on `academic_week` at KS4. The visible consequence: **KS3 physics has
no Autumn-1 work at all**, correctly — Rainford does not teach it this half
term. It leads the continuation queue instead.

---

## §3 · The floors, and the arithmetic behind each target

Recomputed per leaf from the MRB-335 pool definitions rather than eyeballed.
Because `classify()` sets tier and `triple_only` **per subtopic**, every row of
a KS4 subtopic carries the same two flags, and that collapses the KS4 floor to
exactly two cases:

- **base subtopic** — every row is `tier='foundation'`, so the Foundation pool
  is *all* its rows and the Higher pool is its `standard|harder` rows only.
  Higher is therefore the binding constraint: **standard + harder ≥ 50**.
  Target **12 / 26 / 26 = 64** → Foundation 64, Higher 52.
- **higher-only subtopic** — every row is `tier='higher'`, so the Foundation
  pool is empty *by construction* (this is `set_work_scope_check`'s existing
  derived exception, not a hole) and the Higher pool is all rows.
  Target **18 / 18 / 18 = 54**.

`triple_only` never changes a count — it decides whether a cohort sees the leaf
at all, not how many rows it sees.

**KS3**: ≥ 30 per band. Target **32 / 32 / 32 = 96** per lesson. Written as one
constant, `KS3_LEAF_FLOOR` in `set_work_scope_check.py`, so if Mide raises 30
to 50 it is that line and nothing else.

### The gate that measures it

`set_work_scope_check.py` gained `--leaf` this run. It **reports** at leaf level
and still **gates** at topic/unit level only — flooring the leaves today would
be red on all 1,053 cells and would say nothing new each run. `--leaf --strict`
turns the gap red, and the finishing night runs it strict.

Whole-estate position at the start of night 1:

```
KS4 — 264 leaves, 498 cells, 498 short, 19,434 row(s) to author
KS3 — 185 leaves, 555 cells, 555 short, 11,508 row(s) to author
```

**30,942 rows is the whole programme.** Night 1 is the 4,718 of them Rainford
is teaching now.

---

## §4 · Night 1 — the must-complete

**83 leaves, 4,718 rows.**

| lane | leaves | rows |
|---|---|---|
| KS4 biology | 15 | 780 |
| KS4 chemistry | 21 | 1,035 |
| KS4 physics | 14 | 686 |
| KS3 biology | 15 | 924 |
| KS3 chemistry | 18 | 1,293 |
| KS3 physics | 0 | 0 — *see §2.2* |

### KS4 — 50 subtopics, 2,501 rows

Aim per subtopic: **base 12/26/26 = 64** (Foundation pool 64, Higher pool 52);
**higher-only 18/18/18 = 54** (Foundation empty by construction, Higher 54).

| subtopic | subject | class | now E/S/H | F pool | H pool | to author |
|---|---|---|---|---|---|---|
| `eukaryotes-prokaryotes` | biology | base | 4/4/4 | 12 → 50 | 8 → 50 | **52** |
| `animal-plant-cells` | biology | base | 4/4/4 | 12 → 50 | 8 → 50 | **52** |
| `cell-specialisation` | biology | base | 4/4/4 | 12 → 50 | 8 → 50 | **52** |
| `microscopy` | biology | base | 4/4/4 | 12 → 50 | 8 → 50 | **52** |
| `chromosomes-mitosis` | biology | base | 4/4/4 | 12 → 50 | 8 → 50 | **52** |
| `stem-cells` | biology | base | 4/4/4 | 12 → 50 | 8 → 50 | **52** |
| `principles-of-organisation` | biology | base | 4/4/4 | 12 → 50 | 8 → 50 | **52** |
| `digestive-system` | biology | base | 4/4/4 | 12 → 50 | 8 → 50 | **52** |
| `enzymes` | biology | base | 4/4/4 | 12 → 50 | 8 → 50 | **52** |
| `adaptations` | biology | base | 4/4/4 | 12 → 50 | 8 → 50 | **52** |
| `food-chains-webs` | biology | base | 4/4/4 | 12 → 50 | 8 → 50 | **52** |
| `population-competition` | biology | base | 4/4/4 | 12 → 50 | 8 → 50 | **52** |
| `carbon-cycle` | biology | base | 4/4/4 | 12 → 50 | 8 → 50 | **52** |
| `decomposition` | biology | base | 4/4/4 | 12 → 50 | 8 → 50 | **52** |
| `trophic-levels` | biology | base/triple | 4/4/4 | 12 → 50 | 8 → 50 | **52** |
| `atoms-elements-compounds` | chemistry | base | 4/4/4 | 12 → 50 | 8 → 50 | **52** |
| `mixtures` | chemistry | base | 4/4/4 | 12 → 50 | 8 → 50 | **52** |
| `model-of-the-atom` | chemistry | base | 4/4/4 | 12 → 50 | 8 → 50 | **52** |
| `subatomic-particles` | chemistry | base | 4/4/4 | 12 → 50 | 8 → 50 | **52** |
| `relative-atomic-mass` | chemistry | base | 4/4/4 | 12 → 50 | 8 → 50 | **52** |
| `electronic-structure` | chemistry | base | 4/4/4 | 12 → 50 | 8 → 50 | **52** |
| `conservation-of-mass` | chemistry | base | 4/4/4 | 12 → 50 | 8 → 50 | **52** |
| `relative-formula-mass` | chemistry | base | 4/4/4 | 12 → 50 | 8 → 50 | **52** |
| `percentage-yield` | chemistry | base/triple | 4/4/4 | 12 → 50 | 8 → 50 | **52** |
| `atom-economy` | chemistry | base/triple | 4/4/4 | 12 → 50 | 8 → 50 | **52** |
| `concentration-of-solutions` | chemistry | base | 4/4/4 | 12 → 50 | 8 → 50 | **52** |
| `titrations` | chemistry | base/triple | 4/4/4 | 12 → 50 | 8 → 50 | **52** |
| `flame-tests` | chemistry | base/triple | 4/4/4 | 12 → 50 | 8 → 50 | **52** |
| `metal-hydroxides` | chemistry | base/triple | 4/4/4 | 12 → 50 | 8 → 50 | **52** |
| `carbonates-halides-sulfates` | chemistry | base/triple | 4/4/4 | 12 → 50 | 8 → 50 | **52** |
| `pure-substances` | chemistry | base | 5/7/6 | 18 → 50 | 13 → 50 | **46** |
| `early-atmosphere` | chemistry | base | 5/8/7 | 20 → 50 | 15 → 50 | **44** |
| `moles` | chemistry | higher-only | 4/4/4 | 0 → 50 | 12 → 50 | **42** |
| `amounts-in-equations` | chemistry | higher-only | 4/4/4 | 0 → 50 | 12 → 50 | **42** |
| `using-moles-calculations` | chemistry | higher-only | 4/4/4 | 0 → 50 | 12 → 50 | **42** |
| `chromatography` | chemistry | base | 6/10/9 | 25 → 50 | 19 → 50 | **39** |
| `energy-stores-systems` | physics | base | 4/4/4 | 12 → 50 | 8 → 50 | **52** |
| `changes-in-energy` | physics | base | 4/4/4 | 12 → 50 | 8 → 50 | **52** |
| `energy-transfers-in-a-system` | physics | base | 4/4/4 | 12 → 50 | 8 → 50 | **52** |
| `work-done-energy-transfer` | physics | base | 4/4/4 | 12 → 50 | 8 → 50 | **52** |
| `lenses` | physics | base/triple | 4/4/4 | 12 → 50 | 8 → 50 | **52** |
| `density-of-materials` | physics | base | 4/5/5 | 14 → 50 | 10 → 50 | **50** |
| `changes-of-state` | physics | base | 4/5/5 | 14 → 50 | 10 → 50 | **50** |
| `internal-energy` | physics | base | 4/5/5 | 14 → 50 | 10 → 50 | **50** |
| `properties-em-waves-1` | physics | base | 4/6/5 | 15 → 50 | 11 → 50 | **49** |
| `temperature-changes-shc` | physics | base | 5/6/5 | 16 → 50 | 11 → 50 | **48** |
| `specific-latent-heat` | physics | base | 5/6/5 | 16 → 50 | 11 → 50 | **48** |
| `properties-of-waves` | physics | base | 5/6/6 | 17 → 50 | 12 → 50 | **47** |
| `sound-waves-hearing` | physics | higher-only/triple | 4/4/4 | 0 → 50 | 12 → 50 | **42** |
| `waves-detection-exploration` | physics | higher-only/triple | 4/4/4 | 0 → 50 | 12 → 50 | **42** |

### KS3 — 33 lessons, 2,217 rows

Aim per lesson: **32/32/32 = 96** (Easy/Medium/Hard each ≥ 30).

| unit | lesson | now E/S/H | to author |
|---|---|---|---|
| B1 | `levels-of-organisation` | 8/8/8 | **72** |
| B1 | `animal-and-plant-cells` | 9/9/9 | **69** |
| B1 | `specialised-cells` | 9/9/9 | **69** |
| B1 | `using-a-microscope` | 9/9/9 | **69** |
| B2 | `antagonistic-muscle-pairs` | 13/13/13 | **57** |
| B2 | `what-the-skeleton-does` | 13/13/13 | **57** |
| B4 | `exercise-asthma-and-smoking` | 10/10/10 | **66** |
| B4 | `how-breathing-works` | 11/11/11 | **63** |
| B4 | `the-gas-exchange-system` | 11/11/11 | **63** |
| B6 | `alcohol-and-smoking` | 17/17/17 | **45** |
| B6 | `what-drugs-do-to-the-body` | 18/18/18 | **42** |
| B7 | `the-photosynthesis-reaction` | 13/13/13 | **57** |
| B8 | `anaerobic-respiration-in-humans` | 10/10/10 | **66** |
| B8 | `fermentation` | 10/10/10 | **66** |
| B8 | `aerobic-respiration` | 11/11/11 | **63** |
| C1 | `diffusion` | 8/8/8 | **72** |
| C1 | `changes-of-state` | 9/9/9 | **69** |
| C1 | `gas-pressure` | 9/9/9 | **69** |
| C1 | `solids-liquids-and-gases` | 9/9/9 | **69** |
| C2 | `compounds` | 9/9/9 | **69** |
| C2 | `elements` | 9/9/9 | **69** |
| C2 | `the-atom-daltons-model` | 9/9/9 | **69** |
| C3 | `chromatography` | 7/7/7 | **75** |
| C3 | `distillation` | 7/7/7 | **75** |
| C3 | `evaporation-and-crystallisation` | 7/7/7 | **75** |
| C3 | `filtration` | 7/7/7 | **75** |
| C3 | `pure-or-mixture` | 8/8/8 | **72** |
| C4 | `mass-in-a-reaction` | 10/10/10 | **66** |
| C6 | `catalysts` | 8/8/8 | **72** |
| C8 | `group-0-and-why-groups-exist` | 7/7/7 | **75** |
| C8 | `group-1-the-alkali-metals` | 7/7/7 | **75** |
| C8 | `group-7-the-halogens` | 7/7/7 | **75** |
| C8 | `metals-and-non-metals` | 8/8/8 | **72** |

### The continuation queue (§4.2), in scheme order

Worked only after every leaf above is at its floor. **KS3 physics leads it** — Rainford
starts Y7/Y8 physics in calendar week 9, the week after October half-term, so it is the
nearest unstarted material even though it has no Autumn-1 row at all.

- **KS3, calendar weeks 9–14** — 21 lessons: `a-balanced-diet`, `chromosomes-genes-and-dna`, `conservation-of-energy`, `distance-time-graphs`, `drawing-and-adding-forces`, `energy-in-food-and-what-you-need`, `energy-stores`, `energy-transfers-before-and-after`, `food-tests`, `friction`, `fuels-and-energy-resources`, `how-we-worked-out-dna`, `mass-vs-weight`, `moments`, `passing-it-on-heredity`, `power-ratings-in-watts`, `reading-a-fuel-bill`, `simple-machines`, `speed`, `variation-continuous-and-discontinuous`, `what-a-force-is`

- **KS4, lesson ordinals 9–16** — 39 subtopics: `atmospheric-pollutants`, `biodiversity`, `blood`, `coronary-heart-disease`, `development-atomic-model`, `development-periodic-table`, `earths-resources`, `efficiency`, `energy-resources`, `extraction-of-metals`, `factors-affecting-food-security`, `global-warming`, `greenhouse-gases`, `group-0`, `group-1`, `heart-blood-vessels`, `infrared-black-bodies`, `ionic-bonding`, `land-use`, `metallic-bonding`, `metals-non-metals`, `particle-motion-pressure`, `periodic-table`, `plant-tissues`, `potable-water`, `power`, `properties-ionic-compounds`, `radioactive-decay`, `reactions-of-acids`, `reactivity-series`, `red-shift-big-bang`, `stellar-evolution`, `structure-of-atom`, `thermal-conductivity`, `transport-in-cells`, `types-of-em-waves`, `uses-em-waves`, `waste-management`, `water-cycle`
---

## §5 · How the lanes run

Five lanes, one per (subject × key stage) that has work. **One executor task per
leaf**, not per lane: a lane asked for 400 questions in one pass paraphrases,
and paraphrase is the failure mode these floors invite. A leaf is 42–75 rows,
which is a unit an author can hold whole and check for repetition.

Each lane owns disjoint files, so all five share ONE worktree — the MRB-335
scratch-name collision was between *shared* scratch paths, not shared
worktrees, and a sixth checkout is 300 MB this disk does not have (1.7 GB free
after this one).

Per leaf, in order:

1. **List the distinct teachable points first**, then map the quota onto them.
   Where a leaf runs out of points, go wider across its own material — named
   examples, data with units, the required practical, the misconception set —
   never reword an existing row.
2. Author to the target shape, continuing each band's id sequence from the
   leaf's current maximum. **Never touch a row at `bank_position ≤ 11`, and
   never one whose id suffix is ≤ 04** — that window is what every
   automatically-composed assignment in the school is drawn from.
3. Self-check: duplicate stems, duplicate answer-sets, and a **paraphrase
   check** — two stems in one leaf sharing ≥ 70% of their tokens is a finding.
4. Length parity as an authoring rule, not a post-hoc fix: the key is longest
   about a quarter of the time, its length rank varies, and three times in four
   the longest option is a distractor written to the key's level of detail.
5. Cold examiner re-read before commit; findings logged in
   `docs/mrb338/night1-<subject>.md`.

Commander (not the lanes) runs the gates and commits — pathspec only, one leaf
group per commit:

```
verify_questions.py · python3 -m ks3_data.question_bank · ks4_pool_check.py --python
verify_answer_positions.py · verify_answer_lengths.py · pool_ownership.py
verify_week_truth.py · set_work_scope_check.py --leaf
```

## §6 · Where this parks

The programme is 30,942 rows and night 1 is 4,718 of them. Work stops at a
**committed, validated leaf boundary** — never mid-leaf — and §7 of the report
carries the exact remaining gap per leaf plus the order for night 2.
