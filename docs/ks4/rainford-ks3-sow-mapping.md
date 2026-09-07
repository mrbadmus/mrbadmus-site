# Rainford High School — KS3 scheme of work, mapped to platform lessons

**MRB-332 addition · 6 September 2026 · for Mide**

Source: `Rainford SOW/Ks3 SOW 25-26 (NEW).xlsx`, sheets *Year 7 SoW*, *Year 8 SoW*,
*Year 9 SoW*. Generator: `rainford_ks3_sow.py`. Seed:
`supabase/seeds/20260907003000_rainford_ks3_overrides.sql`. Target table:
`public.scheme_of_work_overrides`, KS3 rows, Rainford only.

> **This is one school's scheme. It is seed data and reference evidence, never
> the platform default.** No KS3 default data was touched — not
> `scheme_of_work_entries`, not `ks3_seed_sow.py`, not `ks3_data/`, not
> `ks3_art/`, not `build_ks3.py`. The 185-row KS3 default was verified unchanged
> before and after (see *TEST verification* below).

---

## Read these four things first

### 1. Two lessons per week IS representable — because `academic_week` is not a week

Rainford teaches two content lessons in most weeks ("1a" and "1b", both Year 7
Biology, both week 1), and the KS3 uniqueness rule is
`(school_id, year_group, subject_id, academic_week)`. On a naive reading half of
Rainford's scheme has nowhere to go.

**That reading is wrong.** `academic_week` at KS3 is a per-(year, subject)
teaching **order**, 1..n — not a calendar week. Both ends of the estate say so
in their own words:

- `ks3_seed_sow.py`: *"academic_week runs 1..n. That is a teaching ORDER, not a
  calendar: week 1 is the first lesson of that subject in that year, whenever the
  school actually starts it."*
- the backend, `consumer/work.js`: *"POSITION IS A CURSOR PER SUBJECT, NOT A
  DATE… Year 8 Physics runs to 35 and Year 8 Biology to 22, in the same year."*

So Rainford's 1a and 1b are simply lessons 1 and 2 of Year 7 Biology. Nothing
collides, nothing is dropped, and the longest block is 24 against a ceiling of
39. **No schema change is needed.**

**What IS lost, and it is real.** The calendar week has no column, so neither
does the *interleaving* between subjects. Rainford teaches in blocks — Y7 Biology
in calendar weeks 1–4, then Chemistry 5–8, then Physics 9–12, then Biology again
13–16 — and that braiding is invisible in the rows. A reader sees Rainford's
Biology **order** correctly and their Biology **timing** not at all.

Mitigation, not a fix: every row carries its Rainford week label verbatim in
`notes` ("Rainford Y7 week 13a"), so a human can reconstruct the calendar. A
query cannot. Making it queryable is a `calendar_week` column — a schema change,
recorded here as the honest cost rather than smuggled into `academic_week`.

### 2. ✅ RULED 7 Sep 2026 — THIS SEED IS PARKED. DO NOT APPLY IT.

> **Mide's ruling, 7 September.** Production's **183 live Rainford KS3 override
> rows stay** for the 14 September go-live. This seed is parked as **MRB-333**,
> post-go-live, and the blocker is *not* the honesty test below — the rows are
> honest. The blocker is §1's own "honest cost": the calendar-week
> representation has to be decided first, because that decision may change what
> these rows should contain.
>
> ⚠️ **What made this urgent rather than theoretical.** The paragraph below says
> "on TEST the old seed had never been applied, so applying this one caused no
> live conflict." That is true of TEST and **false of production**, which was
> not checked when this was written. Production holds **183 Rainford KS3
> override rows** (Y7 90, Y8 90, Y9 3, created 16 Aug 2026, weeks 1–37). This
> seed opens with a scoped `DELETE` and would have removed all 183 before
> writing 162 different ones — a real school's live scheme, replaced, on a
> choice this document itself parks on Mide.
>
> The generator and the seed file **stay in the repo**, retired nothing. See
> finding 12 in `findings-for-mide.md`: nothing reads
> `scheme_of_work_overrides` yet, so neither row set currently affects what a
> teacher or child sees.

### 2. ⚠️ This seed COLLIDES with the existing Rainford seed — the original note

`supabase/seeds/20260726182000_ks3_school_schemes.sql` already claims **exclusive**
ownership of Rainford's KS3 override rows and opens with the same scoped
`DELETE`. So does this one. **Both cannot be applied; whichever runs last wins,
silently.**

| | old seed (`20260726182000`) | this seed (`20260907003000`) |
|---|---|---|
| derived from | MRB-103's locked *unit → year* map | Rainford's actual 2025-26 spreadsheet |
| rows | 185 — every platform lesson | 162 — every lesson Rainford teaches |
| order within a unit | the **platform's** | **Rainford's** |
| gaps | none (synthetic completeness) | 34, each named with a reason |
| what it answers well | which units Rainford does in which year | what Rainford actually teaches, in what order |

Neither is wrong; they answer the same question at two resolutions. **Apply
exactly one.** I did not modify `ks3_seed_sow.py` or `ks3_data/school_schemes.py`
— that is your call, not mine.

On TEST the old seed had never been applied (`scheme_of_work_overrides` held zero
rows when this run started), so applying this one caused no live conflict. The
file-level collision outlives that fact.

### 3. The Skills track writes no rows — and is listed here in full

Each sheet is two parallel tracks: Teacher A teaches **Content** (substantive
knowledge), Teacher B teaches **Skills** (disciplinary knowledge). **The Skills
track emits no override rows.** Three reasons, any one sufficient:

1. **It has nowhere to sit.** The unique key is (school, year, subject, week).
   Skills runs *in parallel with* Content — same year, same banner, same week, a
   different teacher. There is no column for "which of the two parallel
   teachers", so every skills row would either collide with a content row or need
   a fabricated `academic_week` asserting a sequence position Rainford does not
   teach.
2. **Most of it has no subject.** "Variables", "Percentages", "Mean, median &
   mode", "SI units & conversion", "Anomalous results" are working-scientifically
   teaching. They inherit a unit banner only because of where the week fell.
   Recording "Percentages" as Year 8 *Biology* would invent a fact.
3. **`subtopic` carries a lesson slug**, and 74 of 82 skills entries have no
   platform lesson. They would be rows pointing at nothing.

**It is not silently dropped.** All 82 entries are in the generator's `MAPPING`
with `track="skills"`, and the 8 that ARE full platform lessons carry their real
slug (listed below). If you rule the track in, the mapping is already done — the
only change is the emit filter, plus an answer to reason 1.

### 4. An unmapped lesson still gets a row, with `subtopic` NULL

34 of Rainford's 162 content lessons have no platform equivalent. They are **not**
skipped — each gets a row with `subtopic = null` and its reason in `notes`,
because (a) `ks3_seed_sow.py`'s own rule is *"a scheme of work describes teaching,
not pages"* and Rainford does teach Puberty, and (b) skipping them would compress
`academic_week` so the ordinals stopped being Rainford's real positions. Every
gap is visible **in the data**, not only in this file.

The only content cells that get no row are the school's own blanks: Y7
"36a (extra) ?????" and "36b (extra) ??????", plus Y8's two empty week-36 cells.

---

## Counts

**246 workbook entries — 164 content, 82 skills.**
**162 rows emitted** (content track; 2 placeholder cells dropped).
**128 carry a platform lesson slug · 34 are gaps.**

| Year | Subject | Lessons | Mapped | Gap | max `academic_week` |
|---|---|---:|---:|---:|---:|
| 7 | Biology | 24 | 23 | 1 | 24 |
| 7 | Chemistry | 22 | 21 | 1 | 22 |
| 7 | Physics | 24 | 19 | 5 | 24 |
| 8 | Biology | 24 | 16 | 8 | 24 |
| 8 | Chemistry | 22 | 22 | 0 | 22 |
| 8 | Physics | 24 | 22 | 2 | 24 |
| 9 | Biology | 8 | 3 | 5 | 8 |
| 9 | Chemistry | 8 | 2 | 6 | 8 |
| 9 | Physics | 6 | 0 | 6 | 6 |
| | **total** | **162** | **128** | **34** | ceiling 39 |

⚠️ **Year 9 is 11 weeks, not 36.** Rainford's KS3 ends in the autumn of Year 9 and
the school moves to its KS4 scheme. The sheet ends cleanly at week 11 with a
complete unit — that is a fact about the school, not a truncated spreadsheet.

---

## The 34 unmapped content lessons, by reason

### Beyond statutory KS3 — 10 lessons (expected, and already recorded)

`ks3_data/school_schemes.py` already flags all three of these areas for this
school as `beyond_statutory`: *"KS4 content; not in the 2014 KS3 programme of
study."* The platform correctly has no lesson, and this is corroboration rather
than a gap.

| | Rainford lesson | recorded as |
|---|---|---|
| Y8 4a | The Circulatory system | `circulation` |
| Y8 4b | Blood & Vessels & KO quiz | `circulation` |
| Y9 5 | Rates of reaction | `rate-of-reaction` |
| Y9 5 | Measuring rate (colour change) | `rate-of-reaction` |
| Y9 6 | Measuring rate (gas collection) | `rate-of-reaction` |
| Y9 6 | Rates of reaction (Temperature) | `rate-of-reaction` |
| Y9 7 | KO Quiz/Rates of reaction (Concentration) | `rate-of-reaction` |
| Y9 7 | Rates of reaction (Surface area) | `rate-of-reaction` |
| Y9 9 | Nuclear fusion | `fusion-and-star-life-cycle` |
| Y9 9 | Life cycle of a star | `fusion-and-star-life-cycle` |

Two lessons inside Rainford's Chem 7 **do** have platform lessons and are mapped:
Catalysts → `catalysts` (C6), Conservation of mass → `mass-in-a-reaction` (C4).

### Genuinely absent from the platform — 19 lessons

Each was searched for in `ks3_data` before being called absent.

| | Rainford lesson | what the search found |
|---|---|---|
| Y7 20b | Testing for gases & KO quiz | no gas-tests lesson; limewater lives inside C5 `thermal-decomposition`, squeaky pop inside C6 `acid-plus-metal` |
| Y7 26a | Puberty | B5 has no puberty lesson; `human-reproductive-systems` mentions it only in passing |
| Y7 32a | Our Solar System | no lesson names or compares the planets (see near-miss below) |
| Y7 34a | The moon and eclipses | no moon-phases or eclipse lesson |
| Y7 34b | The origins and fate of the universe | "big bang" appears nowhere in `ks3_data` |
| Y8 16b | Selective breeding | "selective breeding" appears nowhere in `ks3_data` |
| Y8 24b | EM Spectrum | appears **only** as a `ks4_becomes` note on P7 `light-travels` and `colour-and-the-spectrum` — the platform names it as the KS4 successor and deliberately does not teach it at KS3 |
| Y8 25b | Pyramids of number | "pyramid" appears nowhere in `ks3_data` |
| Y8 26a | Pyramids of biomass | as above |
| Y8 28b | Transects | `sampling-an-ecosystem` is quadrats only — random placement and sample size |
| **Y8 34b** | **Convection** | **P1 has `conduction`, `radiation` and `insulation` but NO convection lesson.** Convection appears only as a distractor inside the radiation and insulation question sets |
| Y9 2 | Microbes & disease | "pathogen" appears nowhere; B6 is drugs, alcohol and substance misuse only |
| Y9 3 | Preventing transmission | same gap |
| Y9 3 | KO Quiz/Defence against disease | same gap — no immune-system lesson |
| Y9 4 | Vaccination | "vaccine" appears only in B5 `lifestyle-and-the-developing-foetus`, in passing |
| Y9 10 | Space exploration | P12 has no space-exploration lesson |
| Y9 10 | Living in space | no equivalent |
| Y9 11 | Living on Mars | no equivalent |
| Y9 11 | Cosmic radiation | no ionising-radiation lesson; P1 `radiation` is infrared/thermal |

**Two of these are worth your eye as possible platform gaps rather than
scope decisions:**

- **Convection (Y8 34b).** The platform teaches conduction, radiation and
  insulation but not convection. Every other school teaching KS3 physics will hit
  this. Rainford teaches it as a full lesson.
- **Disease and immunity (Y9, four lessons).** Microbes, transmission, defence
  and vaccination are a whole strand the platform has no KS3 coverage for. This
  may be deliberate — but it is four consecutive taught lessons.

### Ambiguous — 3 lessons, deliberately left unmapped

A wrong mapping silently points a teacher at the wrong lesson, which is worse
than a visible gap. In each of these the near-miss is named so you can overrule.

| | Rainford lesson | near-miss rejected, and why |
|---|---|---|
| Y8 26b | Animal adaptation | B11 `variation-and-competitive-success` does use "well adapted to a particular environment", but its subject is variation driving competitive success within a species, not adaptation to cold/hot/dry habitats. A close call. |
| Y8 27a | Plant adaptation | same near-miss; `leaves-built-for-the-job` (B7) is adjacent but is about photosynthesis, not habitat |
| Y9 4 | Uses of bacteria | B3 `bacteria-in-the-gut` is the only bacteria lesson and is specifically the gut microbiome; Rainford's is the general industrial and food uses |

Also worth naming, though it is mapped: **Y7 32a "Our Solar System"** was left
unmapped because `the-sun-stars-and-galaxies` *defines* what a solar system is,
as one rung of a star → solar system → galaxy → universe ladder, but it is not a
planets lesson — and Y7 32b "The wider universe" already carries it.

### Enrichment — 2 lessons

Y7 35a Alien life debate · Y7 35b Moon landing debate. No platform equivalent,
and none wanted.

### Placeholders — 2 cells, no row emitted

Y7 "36a (extra) ?????" · Y7 "36b (extra) ??????". Blanks in the school's own
plan. (Y8's week-36 cells are empty and were never entries.)

---

## Where Rainford's shape and the platform's shape disagree

These are all mapped — they are noted so the mapping is not mistaken for a
one-to-one correspondence. Each row's `notes` carries the same explanation.

### Rainford teaches over two lessons what the platform draws as one (9 pairs)

Both rows carry the same slug, which is legal (`subtopic` is not unique) and is
the true statement.

Animal cells + Plant cells → `animal-and-plant-cells` · Food tests:
Carbohydrates + Food tests: Protein & fat → `food-tests` · Combustion +
Incomplete combustion → `combustion` · Series + Parallel circuits →
`series-and-parallel` · Pregnancy + Birth → `gestation-placenta-and-birth` ·
Fossil fuels + Renewable energy → `fuels-and-energy-resources` · Salts + Making
a salt → `making-a-pure-dry-salt` · Sedimentary + Igneous & metamorphic →
`three-ways-to-make-a-rock` · Conduction + Thermal conductivity → `conduction`

### One Rainford lesson covers two or three platform lessons (7 merges)

The row carries the **primary** slug; the co-covered lesson is named in `notes`
and appears in the "never placed" list below.

| Rainford lesson | mapped to | also covers |
|---|---|---|
| Y7 18a Exo & Endothemric reactions | `exothermic-reactions` | `endothermic-reactions` |
| Y7 21b Potential difference and current | `potential-difference` | `current-and-circuits` (21a carries it) |
| Y7 24b Magnets & magnetic fields | `magnetic-fields` | `magnets-and-poles`, `the-earth-is-a-magnet` |
| Y7 6b Pure mixtures and solutions | `pure-or-mixture` | `dissolving-and-solutions` |
| Y8 5a Atoms | `the-atom-daltons-model` | `chemical-symbols` |
| Y8 22b Colours & filters | `colour-and-the-spectrum` | `why-things-look-coloured` |
| Y8 7a Metals and non-metals | `metals-and-non-metals` | `metal-and-non-metal-oxides` (20b also lands there) |

### Cross-discipline placements (3)

The row's **subject comes from Rainford's unit banner**, not from the platform
unit of the mapped lesson — that is a decision I took, and it is reversible.
Rainford teaches these as one subject; the platform draws them in another.

| | Rainford lesson | row subject | platform unit |
|---|---|---|---|
| Y7 3a | Diffusion in cells | Biology (Bio 1) | C1 Chemistry |
| Y8 32a | Forces in states of matter | Physics (Phys 6) | C1 Chemistry |
| Y8 33a | Gas Pressure | Physics (Phys 6) | C1 Chemistry |

### Lessons Rainford teaches twice, in different years

- `gas-pressure` — Y7 6a (Chem 1) and Y8 33a (Phys 6). A legitimate spiral.
- `simple-machines` — Y7 12a "Simple machines & moments" and Y8 10a "Work done".
  The platform defines work done inside `simple-machines`; there is no standalone
  work-done lesson.

Different years, so no key collision either way.

---

## The Skills track in full — 82 entries, 0 rows

### The 8 that ARE full platform lessons (mapped, not emitted)

| | entry | platform lesson |
|---|---|---|
| Y7 15c | Burning food | `energy-in-food` (P2) |
| Y7 25c | Electromagnets | `electromagnets` (P10) |
| Y7 28c | Seed dispersal | `seed-dispersal` (B5) |
| Y8 2c | Stomata investigation | `stomata-and-gas-exchange-in-plants` (B4) |
| Y8 4c | The periodic table | `groups-and-periods` (C8) |
| Y8 5c | Chemical formula | `formulae` (C2) |
| Y8 6c | More chemical formula | `formulae` (C2) |
| Y8 35c | Density practical | `density` (P11) |

### The other 74 — no platform lesson

**Working scientifically:** Intro to science · Scientific diagrams · Hazards &
Risk assessment · Steric acid & risk assessment · Hypothesis & prediction ·
Variables · Variables 2 · Observations · Graph types · Drawing graphs · Drawing
graphs 2 · Drawing graphs 3 · Resolution · Percentages · Evaluation · Method
writing · Mean, median & mode · Anomalous results · Repeatability &
reproducibility · SI units & conversion · Summarising · Extended answers 2 ·
Correlation & causation · Accuracy & precision · Describe & explain · Scientific
theories · Types of exam questions · FIFA practice · Writing equations · Identify
the pH

**Practical / activity:** Drawing specialised cells · Investigating friction ·
Investigating speed · Visking tubing · Investigating Exo & endothermic reactions
· Drawing & building circuits · Asteroids prac · Making an indicator · More
genetic crosses · Aseptic technique · Rocket science force diagrams · Lift off
investigation

**Assessment and review (14):** TEST 1 (AW1) · Test 1 review · TEST 2 (AW1) ·
Test 2 review · TEST 3 · Test 3 review (Y7) · TEST 1 · Test 1 review · TEST 2 ·
Test 2 review · TEST 3 · Test 3 review (Y8) · TEST 1 · Test 1 review (Y9)

**Revision:** Flashcard revision & self quizzing (×7)

**Reading:** Reading- Nanoparticles · Reading- Extremophiles · Reading- Black
holes

**School calendar:** Science Week (×2) · Careers week (×2)

**The school's own blanks:** "???" (×4, Y7 13c / 14c / 29c / 30c)

---

## Platform lessons Rainford's content track never places — 70 of 185

Most are not untaught: they are **co-covered** inside a merged Rainford lesson
(see the merge table above), or taught on the **skills** track. Six are flagged
because excluding the skills track would otherwise overstate the gap.

| unit | lesson |
|---|---|
| B1 | `life-processes`, `unicellular-organisms` |
| B2 | `joints`, `biomechanics-forces-in-the-body` |
| B3 | `bacteria-in-the-gut` |
| B4 | `alveoli-built-for-exchange`, `stomata-and-gas-exchange-in-plants` ⟵ *skills track* |
| B5 | `lifestyle-and-the-developing-foetus`, `seed-dispersal` ⟵ *skills track* |
| B6 | `substance-misuse-and-decisions` |
| B7 | `leaves-built-for-the-job`, `testing-a-leaf-for-starch`, `why-almost-all-life-depends-on-it` |
| B8 | `why-every-cell-respires`, `aerobic-vs-anaerobic` |
| B9 | `predator-and-prey`, `disturbing-a-food-web`, `pollinators-and-food-security`, `toxic-build-up-in-a-food-chain` |
| B11 | `variation-and-competitive-success` |
| C1 | `testing-the-model` |
| C2 | `chemical-symbols` *(co-covered by Y8 5a)*, `conservation-of-mass`, `formulae` ⟵ *skills track* |
| C3 | `dissolving-and-solutions` *(co-covered by Y7 6b)*, `proving-something-is-pure` |
| C4 | `reactions-rearrange-atoms`, `symbol-equations-and-balancing` |
| C5 | `which-reaction-is-this` |
| C7 | `endothermic-reactions` *(co-covered by Y7 18a)*, `energy-and-changes-of-state`, `measuring-a-temperature-change` |
| C8 | `mendeleev`, `groups-and-periods` ⟵ *skills track* |
| C9 | `predicting-displacement` |
| P1 | `heating-and-thermal-equilibrium`, `radiation` |
| P2 | `calculating-energy-transferred`, `energy-in-food` ⟵ *skills track* |
| P3 | `relative-motion` |
| P4 | `balanced-and-unbalanced`, `what-forces-do-to-motion`, `air-and-water-resistance`, `springs-and-hookes-law`, `non-contact-forces` |
| P5 | `pressure-in-liquids`, `upthrust-floating-and-sinking`, `atmospheric-pressure` |
| P6 | `transverse-waves-and-superposition`, `how-sound-is-made`, `sound-is-longitudinal`, `sound-needs-a-medium`, `echoes-reflection-and-absorption` |
| P7 | `light-travels`, `lenses-and-images`, `the-eye-and-the-camera`, `why-things-look-coloured` *(co-covered by Y8 22b)* |
| P8 | `current-at-a-junction`, `building-and-measuring-a-circuit` |
| P9 | `forces-between-charges`, `electric-fields` |
| P10 | `magnets-and-poles` *(co-covered by Y7 24b)*, `the-earth-is-a-magnet` *(co-covered)*, `electromagnets` ⟵ *skills track*, `how-a-motor-works` |
| P11 | `brownian-motion`, `temperature-and-internal-energy`, `why-ice-floats` |
| P12 | `gravity-and-weight`, `how-far-is-a-light-year` |

Regenerate this list any time with `python3 rainford_ks3_sow.py --report`.

---

## TEST verification

Applied to the TEST project (`qeppkiswvclkkwbxmlok`) via the `supabase-test` MCP
only. Production was never touched, and `supabase db push` was never run.

**The KS3 default is unchanged.** Baseline captured before the work, re-checked
after:

```
select 'sow_entries_ks3', count(*), md5(string_agg(id::text, ',' order by id))
  from public.scheme_of_work_entries where key_stage='KS3';

  before : 185 rows · 42b19ee6e8423699d524427f748d9fc2
  after  : 185 rows · 42b19ee6e8423699d524427f748d9fc2   ✓ identical
```

**The rows landed exactly as generated.** A collation-independent checksum —
`md5` of each `year|subject|week|topic|subtopic|notes` line, sorted, hashed —
computed in Python from the generator and in Postgres from the table:

```
  generator : 162 rows · abd7dac9a21502316c73e22ffc83cd2f
  TEST      : 162 rows · abd7dac9a21502316c73e22ffc83cd2f   ✓ identical
```

**Constraint checks, all clean:**

| check | result |
|---|---|
| Rainford KS3 override rows | 162 |
| carrying a lesson slug | 128 |
| `subtopic` NULL (a named gap) | 34 |
| `tier` or `pathway` not null | 0 ✓ (`..._ks3_no_tier_or_pathway`) |
| `subtopic` not kebab-case | 0 ✓ (`..._ks3_subtopic_is_slug`) |
| distinct (school, year, subject, week) | 162 = total ✓ (`..._ks3_unique`) |
| max `academic_week` | 24 (ceiling 39) ✓ |
| rows outside Rainford KS3 disturbed | 0 — the delete is scoped to `school_id` **and** `key_stage` |

⚠️ **Note for the KS4 lane:** 150 Rainford **KS4** override rows appeared in the
same table during this run — the concurrent MRB-332 KS4 agent's work. My scoped
delete did not touch them and they did not touch mine. Both sets coexist
correctly.

---

## Files

| file | what |
|---|---|
| `rainford_ks3_sow.py` | the generator. Frozen 246-row transcription, the reviewable `MAPPING` dict, `REASON`, `NOTES`, and the consistency gates |
| `supabase/seeds/20260907003000_rainford_ks3_overrides.sql` | generated seed, 162 rows |
| `docs/ks4/rainford-ks3-sow-mapping.md` | this file |

```bash
python3 rainford_ks3_sow.py                 # regenerate the seed
python3 rainford_ks3_sow.py --report        # print every table in this document
python3 rainford_ks3_sow.py --verify-source # re-read the workbook and diff
```

`--verify-source` was run and passes: **ENTRIES matches the workbook exactly, 246
rows.** It exits 0 with a message when the workbook is absent, which is the
normal state of a clean checkout — the file is untracked and lives outside every
worktree.

---

## Decisions I took under my own authority

All reversible, all a one-line change in the generator.

| | decision | why |
|---|---|---|
| A | `topic` carries **Rainford's own unit banner** ("Bio 1- Cells & Organisation"), not the platform unit title | it is the school's table and the school's label; and a Rainford unit spans several platform units (Bio 1 = B1 + B2), so no single platform title fits. The platform unit code goes in `notes` |
| B | `subject_id` comes from the **unit banner**, never from the platform unit of the mapped lesson | Rainford teaches "Diffusion in cells" as Biology; the platform draws it in C1. The row says Biology, and `notes` says the lesson is C1's |
| C | `school_id` looked up **by name**, never hardcoded | test and prod ids differ. Name rather than slug because `slug` is NULL on one of the two schools on TEST |
| D | Rainford's title text is **verbatim, typos included** ("Exo & Endothemric reactions", "Thermal decompositon", "Metals and recyling", "Recreactional drugs") | they are the `MAPPING` keys and must match the workbook byte for byte or `--verify-source` fails. Only transformation: whitespace runs collapsed to one space |
| E | On a merge, the row carries the **primary** slug and `notes` names the co-covered lesson. On a split, **both** rows carry the same slug | `subtopic` is not unique, and both are the true statement |
| F | Where a match would be a guess, the entry is `None` and the **near-miss is named** | a wrong mapping silently points a teacher at the wrong lesson; a visible gap does not |
| G | Unmapped lessons still get a row, with `subtopic` NULL | see finding 4 above |
| H | The workbook is **transcribed and frozen** into the generator rather than read at build time, with `--verify-source` as the gate | the file is untracked and outside every worktree, so a build-time read cannot run from a clean checkout |
