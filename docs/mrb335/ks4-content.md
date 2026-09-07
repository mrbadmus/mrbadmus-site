# MRB-335 — the KS4 content lane

What this lane did, in one line: **249 new questions across 38 subtopics, so
that every KS4 (topic, tier) cell holds at least 50 questions and a teacher
setting work can pick twenty from a pool worth picking from.**

Branch `feat/set-work-v2`. Files touched: `ks4_data/__init__.py`,
`ks4_pool_check.py`, nine new `ks4_data/questions/**/<topic>__setwork.py`
modules, `docs/ks4/pool-authoring.md`, and this file. Nothing else.

---

## 1. Why the pool grew, and why it grew unevenly

The 7 Sep 2026 availability table (PLAN.md §5) found twenty-two (topic, tier)
cells below fifty. Set work v2 lets a teacher hand-pick up to twenty
questions from a whole TOPIC at one tier; a cell of twenty-four is not a
choice, it is a list.

The cells are defined by the v2 pool rule, and the rule is what makes the
arithmetic uneven:

| cell | rows it draws |
|---|---|
| Foundation | `tier='foundation'`, **all three bands** (combined also excludes `triple_only`) |
| Higher | `tier='higher'` any band **∪** `tier='foundation'` in `standard`/`harder` |

Two consequences drove every decision below.

**A Higher cell is fed only by `standard` and `harder`.** So a topic short at
Higher and comfortable at Foundation — `particle-model`, `waves` — needed no
`easier` questions at all, and got none.

**`tier` and `triple_only` are DERIVED per subtopic by `ks4_data.classify()`,
never chosen.** You cannot author a higher-only question inside a base
subtopic. A Higher gap in a base topic is therefore filled with base
`standard`/`harder` rows, which also count for Foundation — which is why
`atmosphere` finished at 82/60 rather than 60/60. The alternative would have
been to invent a higher-tier subtopic, and the curriculum is the authority on
what those are.

---

## 2. The loader change

`ks4_data/__init__.py`, three edits:

| what | where |
|---|---|
| `load_pool` docstring — the "at least twelve" rule and the emission order | `ks4_data/__init__.py:228-280` |
| strict check: `!= PER_SUBTOPIC` → `< PER_SUBTOPIC`, `!= PER_BAND` → `< PER_BAND` | `ks4_data/__init__.py:293`, `:301` |
| emission order: first `PER_BAND` of each band first, extras after | `ks4_data/__init__.py:317-336` |

The rule is now **at least four per band, and the first four of each band sit
at bank positions 0–11**.

⚠️ **The emission-order change is the load-bearing half, and the obvious
implementation is wrong.** The old loop emitted all `easier`, then all
`standard`, then all `harder`. With six easier questions that puts the first
`standard` at position 6 and pushes a thirteenth question INTO the 0–11
window — and `bankFor` (JS) and `compose_assignment` (Python) both read
`bank_position < 12` and take every row of a band they find there, so every
automatically composed weekly set in the estate would have changed silently
(RISKS D7). Emitting `[:4]` of each band first and the extras afterwards
leaves the original twelve at their original positions in their original
order, for every subtopic. Proved rather than asserted: the pre-change
checksum over the untouched 3,168 rows was `5cf8085c…`, and check 4a below
measures the window directly.

`ks4_pool_check.py` follows:

- check 3 relaxed to "at least twelve per subtopic, at least four per band",
  and it now reports how many subtopics hold more than twelve (38);
- check 4 relaxed from `bank_position` 0..11 to 0..n-1;
- **check 4a is new** — *positions 0-11 are still four of each band* — which
  is RISKS D7 measured against the rows rather than trusted.

⚠️ **Open, not mine to fix:** `gate_registry.py:565` describes
`ks4_pool_check` as asserting "bank_position contiguous 0..11". That string is
now wrong. `gate_registry.py` is outside this lane's allowed paths, so it is
left for the commander — it is a description, not an assertion, so nothing is
red because of it.

`verify_answer_positions.py` needed no change: it measures the authored pool
by subject and by subtopic and both stayed healthy (worst index 25%).

---

## 3. What was written, per topic and subtopic

Bands are shown `easier / standard / harder`. Every subtopic held 4/4/4 = 12
before; ids continue each band's sequence from `e05`, `s05`, `h05`, and
`bank_position` continues from 12.

### chemistry · energy-changes — `energy_changes__setwork.py`, +43

| subtopic | added | after |
|---|---|---|
| exothermic-endothermic (base) | 8/8/7 | 12/12/11 = 35 |
| reaction-profiles (base) | 4/4/3 | 8/8/7 = 23 |
| bond-energy-calculations (higher) | 3/3/3 | 7/7/7 = 21 |

The most lopsided split in the run, and deliberate. Combined Foundation on
this topic can only be fed by its two base subtopics, and 24 → 56 needs
thirty-two rows between them. Exothermic/endothermic carries RP5, the fuel
comparison and every calorimetry rearrangement; reaction profiles is one
diagram with four features on it. Loading the two equally would have meant
reaction-profile questions differing only in their numbers.

### chemistry · organic — `organic__setwork.py`, +32

Four base subtopics × 1/4/3 each: `crude-oil-hydrocarbons`,
`fractional-distillation`, `properties-of-hydrocarbons`, `cracking-alkenes`
(each 5/8/7 = 20 after). The topic's other eight subtopics are Triple.

⚠️ Deliberately NOT used: the hydration of ethene to ethanol, and addition
polymerisation. Both appear in the base pages' `equations` blocks, and both
belong to Triple-only subtopics under `classify()`. Examining them in a base
row would put Chemistry-only content in front of a Foundation Combined class.

### chemistry · analysis — `analysis__setwork.py`, +33

| subtopic | added | after |
|---|---|---|
| pure-substances | 1/3/2 | 5/7/6 = 18 |
| formulations | 1/3/3 | 5/7/7 = 19 |
| chromatography | 2/6/5 | 6/10/9 = 25 |
| testing-for-gases | 1/3/3 | 5/7/7 = 19 |

Weighted by content, not by arithmetic. Chromatography carries a required
practical, an equation with two rearrangements and a set of real technique
errors; pure-substances is one idea about melting and boiling points. An even
split would have produced four more purity questions, which grows a pool's
size without growing its coverage.

### chemistry · atmosphere — `atmosphere__setwork.py`, +34

All four subtopics are base, so Combined and Triple share one pool and all
four cells moved together: composition 5/7/7, early-atmosphere 5/8/7,
greenhouse-gases 6/8/8, atmospheric-pollutants 6/8/7.

### chemistry · resources — `resources__setwork.py`, +25

Four base subtopics at 1/2/2 each, plus `alternative-metal-extraction`
(higher, non-triple) at 1/2/2. The only topic where a Higher-tier subtopic was
extended, because it is the only short topic that has one.

### physics · particle-model — `particle_model__setwork.py`, +17

Both Higher cells were short (48) and both Foundation cells were fine (72), so
fifteen of the seventeen rows are `standard`/`harder`. The two `easier` ones
are the same discrimination twice — ΔE = mcΔθ or E = mL — which is the
declared common mistake in two subtopics at once.

### physics · waves — `waves__setwork.py`, +17

Combined Higher only. Sixteen `standard`/`harder` rows and one `easier` (the
v = f λ statement), spread across the six base subtopics.

### physics · magnetism — `magnetism__setwork.py`, +24

The only topic where FOUNDATION was short (36). Seven of its ten subtopics are
Higher, so Combined Foundation sees exactly three, and each took 4/2/2.

### physics · space — `space__setwork.py`, +24

Triple-only in its entirety, so it has no Combined cells at all. Three of its
five subtopics are `tier='foundation'` and only those can feed Triple
Foundation, so all twenty-four rows land there, eight each at 4/2/2.

---

## 4. The cold review — what a second pass found and fixed

Read back one subject at a time as an examiner, against the authored files
rather than against the plan. Five findings, in descending order of how much
they mattered.

### 4.1 ⚠️ The longest option was the answer in 65% of the new rows

**The gate did not catch this, and could not have.** `ks4_pool_check`'s
longest-option check measures the WHOLE corpus against a 40% threshold, and
249 skewed rows inside 3,417 read as 24% — at chance, green, and wrong. It
took measuring the new rows on their own to see it.

The cause was structural rather than careless: a correct option kept the form
"*claim*, because *reason*" while its distractors were bare claims, so the
answer was the long one every time. A student who has learned that heuristic
scores above chance without knowing any science, which is precisely the class
of playable skew MRB-278 exists to stop.

**Fixed on 105 rows**, by giving the most plausible distractor a reason of its
own (better distractors as well as balanced ones) or by moving a correct
option's reason into the `why`, where the authoring standard says it belongs.

Measured after, on the 249 new rows alone:

| metric | before | after |
|---|---|---|
| correct option uniquely longest | 65% | 62% |
| …longest by ≥ 20 characters | 42% | **1%** (3 rows) |
| **correct option occupies more wrapped lines than any other, at 390 px** | not measured | **24%** — chance |

The raw character count barely moves and that is honest: what a student can
SEE is a longer-looking option, and an option four characters longer wraps to
the same number of lines. The rendered-lines figure is the playability
measure, and it sits at chance. The corpus figure the gate reads is 24%.

### 4.2 A same-question-different-numbers pair, and four mirror pairs

A within-subtopic similarity sweep (≥ 0.90 on normalised stems) found six
pairs involving new rows. One was a genuine defect —
`ks4-chromatography-s05` was `ks4-chromatography-e03` with different numbers
(0.97) — and five were mirror pairs where the surface shape was identical
even though the question was not (x-axis/y-axis, breaking/forming a bond,
viscosity/flammability with chain length, the hydrogen test/the oxygen test).
All six reworded; the sweep is now clean for this lane.

⚠️ **Five near-duplicate pairs remain and are NOT this lane's** — they sit in
the frozen first twelve, so this lane must not touch them:
`nuclear-equations-s01 ~ s02`, `scalar-vector-quantities-e01 ~ e04`,
`lenses-s02 ~ s03`, `flemings-left-hand-rule-e03 ~ h01`,
`flame-tests-e01 ~ e03`. Three subtopics also carry a duplicate OPTION SET —
`electrolysis-aqueous-e02/e03`, `classification-living-organisms-e04/s02`,
`metal-hydroxides-e01/e02`. All eight pre-date MRB-335.

### 4.3 A self-contradictory option, introduced by the length fix itself

`ks4-magnetic-fields-h06` asks for a method comparing two magnets with a
plotting compass. Trimming its correct option for length left it reading
"measure the DISTANCE at which each magnet just deflects the needle, keeping
the compass's POSITION the same" — which cannot both be done. Rewritten to
control the needle's starting direction instead. Worth recording because the
edit that caused it was a fix for 4.1: a mechanical pass over 105 rows will
introduce something, and the second read is what catches it.

### 4.4 Six distractors that were noise rather than errors

The authoring standard says a calculation's distractors come from the ERROR,
not from noise. Six did not:

| row | was | now, and the error it models |
|---|---|---|
| `bond-energy-calculations-s05` | −1470 | **−1644** — only two of the four C-H bonds broken |
| `bond-energy-calculations-s06` | −1050 | **−559** — the H-H bond not broken |
| `bond-energy-calculations-h05` | −1450 | **+175** — only one of the two C-Br bonds formed |
| `temperature-changes-shc-s05` | 195 J | **390 J** — Δθ left out of mcΔθ |
| `specific-latent-heat-s05` | 201 500 J | **99 500 J** — L halved instead of × 2.5 |
| `specific-latent-heat-h05` | 27 kg | **4.5 kg** — a power-of-ten slip |
| `particle-motion-pressure-s06` | 150 kPa | **135 kPa** — volumes subtracted, not divided |

### 4.5 Two wordings that could be argued with

- `atmospheric-pollutants-s05` said a candle burns "the same kind of fuel" as
  a car engine. Loosely true, needlessly arguable. Now "a petrol engine …
  a candle burning hydrocarbon wax".
- `life-cycle-assessment-s06` used "this figure alone", meaning *this number*.
  The no-figures rule makes that word unsafe in this pool — a stem-scan for
  figure references flagged it, correctly in form if not in substance. Now
  "this number alone". (The other eleven figure-referencing stems in the pool
  are pre-existing: `circuit-symbols`, `ionic-bonding`, `covalent-bonding` and
  all six `free-body-diagrams` rows.)

### Checked and found clean

- Every calculation recomputed from its own stem; every `why` recomputed with
  it. No arithmetic corrections were needed.
- No new stem reuses a mass, a temperature, a voltage or an ANSWER from a
  lesson page's worked FIFA or printed quiz. The 27 °C/327 °C gas-law pair,
  the 50 g / 20→34 °C calorimetry example and the 100 g / 22→30 °C quiz
  numbers were all specifically avoided.
- `pool_ownership` reports zero exact collisions and zero near-duplicates
  against the lesson pages for this lane. Its three "same keyed answer" notes
  (`properties-small-molecules-e02`, `metals-alloys-e01`, `metals-alloys-e03`)
  are all pre-existing rows.
- No new row needs a figure. Every reaction profile, field pattern, refraction
  angle and heating curve is described in words.
- UK spellings throughout (sulfur, sulfuric, sulfate, aluminium, colour,
  litre, vaporise, practise/practice). Formulae stored FLAT.

---

## 5. Gates

Run on the final tree, after the last content edit.

```
ks4_pool_check.py --python
  ✅ flags match the curriculum — all 3417 row(s) agree with classify()
  ✅ combined foundation 2347 · combined higher 2493 · triple foundation 3043
     · triple higher 3417 — none forbidden
  ✅ the audiences are nested and distinct — 2347 ⊂ … ⊂ 3417
  ✅ at least twelve per subtopic, at least four per band — 264 subtopic(s),
     all ≥4/4/4 (38 hold more than twelve)
  ✅ ids unique — 3417 id(s)
  ✅ bank_position is 0..n-1 per subtopic — contiguous everywhere
  ✅ positions 0-11 are still four of each band — unchanged in all 264
  ✅ four distinct options, answer in range — every row
  ✅ the longest option is not the answer — 810 of 3417 (24%; chance is 25%)
  ✅ physics 82/82 · chemistry 93/93 · biology 89/89

verify_answer_positions.py
  ✅ KS4 assignment pool · by subject   — 3417 q, [871, 846, 852, 848], 25%
  ✅ KS4 assignment pool · by subtopic  — 3417 q, [871, 846, 852, 848], 25%
  ✅ (KS3 ladder, KS3 bank, KS4 built quiz cards, rd position-immunity)

pool_ownership.py
  ✅ one bank per surface — no exact collisions, no near-duplicates from this
     lane against any lesson page
```

---

## 6. The TEST load

```
python3 export_ks4_questions.py --check      → 3417 q across 264 subtopics
python3 export_ks4_questions.py --load test  → ✅ 3417 row(s) upserted into TEST
```

**Checksum: `939d1ae680af1a95af3e69b161c71ffc28214ebdf590bbb36c5da353dae4b0c0`**
(Python and database agree. The pre-MRB-335 pool checksummed
`5cf8085cbc6136c77eda1c28af83b93879b2139784c06e90ac2819f5e3f6f31e` over its
3,168 rows — recorded here because it is the value that proves the emission
reorder left the original twelve untouched.)

### ⚠️ `--verify` exited 3, and what was run instead

`export_ks4_questions.py --verify` signs in as a real student and reads the
table on that JWT, which proves CONTENT and REACH at once. The credential is
`MRB_TEST_STUDENT_PASSWORD` — **Mide's own account password**, deliberately not
in the repo. Without it the script exits **3 — "nobody looked"**, which is not
a pass and was not treated as one.

The two proofs were therefore made separately, exactly as the script's own
comments describe doing on production, and both pass:

```
CONTENT · service-role read: 3417 row(s) in ks4_assignment_bank on TEST
  missing from the database: 0
  present only in the database: 0
  field differences: 0        (all ten mirrored columns, row for row)
  python   checksum: 939d1ae680af1a95af3e69b161c71ffc28214ebdf590bbb36c5da353dae4b0c0
  database checksum: 939d1ae680af1a95af3e69b161c71ffc28214ebdf590bbb36c5da353dae4b0c0
  CONTENT: PASS

REACH · anon read: HTTP 200, rows=0        (RLS grants SELECT to
  REACH: PASS                               `authenticated` only — RISKS D9)
```

Service role bypasses RLS, which is wrong for a reach proof and right for a
content one: it reads every row that is there, including any a policy would
have hidden, so it cannot report a clean mirror over a table it saw half of.
The anon read is the negative control that needs no credential at all.

**Still owed at merge:** `--verify --project prod` after the production load,
with the production service key from `~/.mrbadmus/prod.env`. Nothing in this
lane touched production.

### Counts before and after, on TEST

Total **3168 → 3417** (+249). Every one of the 38 affected subtopics held
exactly 4/4/4 = 12 before.

| subject · tier · triple · band | before | after |
|---|---|---|
| biology (all nine rows) | 268/268/268, 80/80/80, 8/8/8 | unchanged |
| chemistry foundation base e/s/h | 244/244/244 | **275/310/300** |
| chemistry foundation triple e/s/h | 88/88/88 | unchanged |
| chemistry higher base e/s/h | 32/32/32 | **36/37/37** |
| chemistry higher triple e/s/h | 8/8/8 | unchanged |
| physics foundation base e/s/h | 200/200/200 | **215/223/220** |
| physics foundation triple e/s/h | 56/56/56 | **68/62/62** |
| physics higher base e/s/h | 12/12/12 | unchanged |
| physics higher triple e/s/h | 60/60/60 | unchanged |

Per affected subtopic, after (`easier`/`standard`/`harder`), read back from
TEST:

```
exothermic-endothermic       12/12/11 = 35   crude-oil-hydrocarbons        5/8/7 = 20
reaction-profiles              8/8/7 = 23    fractional-distillation       5/8/7 = 20
bond-energy-calculations       7/7/7 = 21    properties-of-hydrocarbons    5/8/7 = 20
chromatography                6/10/9 = 25    cracking-alkenes              5/8/7 = 20
greenhouse-gases               6/8/8 = 22    poles-of-a-magnet             8/6/6 = 20
atmospheric-pollutants         6/8/7 = 21    magnetic-fields               8/6/6 = 20
early-atmosphere               5/8/7 = 20    electromagnetism              8/6/6 = 20
formulations                   5/7/7 = 19    solar-system-gravity          8/6/6 = 20
testing-for-gases              5/7/7 = 19    stellar-evolution             8/6/6 = 20
composition-of-atmosphere      5/7/7 = 19    red-shift-big-bang            8/6/6 = 20
pure-substances                5/7/6 = 18    properties-of-waves           5/6/6 = 17
earths-resources               5/6/6 = 17    temperature-changes-shc       5/6/5 = 16
potable-water                  5/6/6 = 17    specific-latent-heat          5/6/5 = 16
life-cycle-assessment          5/6/6 = 17    particle-motion-pressure      4/6/5 = 15
reducing-use-of-resources      5/6/6 = 17    properties-em-waves-1         4/6/5 = 15
alternative-metal-extraction   5/6/6 = 17    properties-em-waves-2         4/5/6 = 15
density-of-materials           4/5/5 = 14    changes-of-state              4/5/5 = 14
internal-energy                4/5/5 = 14    transverse-longitudinal-waves 4/5/5 = 14
types-of-em-waves              4/5/5 = 14    uses-em-waves                 4/5/5 = 14
```

---

## 7. The availability table AFTER

Derived from the rows now on TEST, not from Python, using the v2 cell rule:
Foundation = `tier='foundation'` rows (triple excluded for combined); Higher =
`tier='higher'` rows ∪ `tier='foundation'` rows in `standard`/`harder`.
A topic whose subtopics are all `triple_only` is absent from Combined
entirely (RISKS C7 — `space`).

| subject | topic | CF | CH | TF | TH |
|---|---|---:|---:|---:|---:|
| biology | cell-biology | 84 | 56 | 96 | 64 |
| chemistry | atomic-structure | 144 | 96 | 156 | 104 |
| physics | energy | 84 | 56 | 96 | 64 |
| biology | organisation | 132 | 88 | 132 | 88 |
| physics | electricity | 120 | 80 | 144 | 96 |
| chemistry | bonding | 132 | 88 | 144 | 96 |
| biology | infection-response | 84 | 56 | 96 | 76 |
| **physics** | **particle-model** | 89 | **63** | 89 | **63** |
| chemistry | quantitative | 60 | 76 | 84 | 92 |
| physics | atomic-structure | 84 | 56 | 132 | 88 |
| biology | bioenergetics | 84 | 56 | 84 | 56 |
| biology | homeostasis | 96 | 64 | 144 | 96 |
| chemistry | chemical-changes | 120 | 104 | 132 | 112 |
| physics | forces | 132 | 100 | 156 | 164 |
| **chemistry** | **energy-changes** | **58** | **59** | **82** | **75** |
| chemistry | rates-equilibrium | 60 | 52 | 60 | 52 |
| **physics** | **waves** | 89 | **64** | 113 | 128 |
| **chemistry** | **organic** | **80** | **60** | 152 | 132 |
| biology | ecology | 180 | 120 | 264 | 188 |
| **physics** | **magnetism** | **60** | **60** | **60** | 120 |
| **chemistry** | **analysis** | **81** | **60** | 129 | 92 |
| **physics** | **space** | — | — | **60** | **60** |
| **chemistry** | **atmosphere** | **82** | **60** | **82** | **60** |
| **chemistry** | **resources** | **68** | **65** | 128 | 105 |

**Bold = a cell this lane moved. Nothing is short.** All twenty-two target
cells cleared 50 with margin; the smallest of them is 58 and the aim was 56.
The lowest cell anywhere in the KS4 pool is now **52** —
`chemistry/rates-equilibrium` at Combined and Triple Higher, which was already
above the floor before this run and was not on the target list.

Nothing is left short, so there is no remaining gap to state.

---

## 8. Left for the commander

1. `gate_registry.py:565` still describes `ks4_pool_check` as proving
   "bank_position contiguous 0..11". It is 0..n-1 now. Outside this lane's
   paths; a description, so nothing is red.
2. Eight pre-existing content defects found by this lane's sweeps and left
   alone because they live in the frozen first twelve: five near-duplicate
   stem pairs (§4.2) and three duplicate option sets (§4.2).
3. `--verify --project prod` after the production load at merge (§6).
4. The KS3 half of PLAN.md §5 is a different lane; the KS3 bank grew from
   2,559 to 3,564 rows in this shared worktree while this lane was running,
   which is that lane working and not drift.
