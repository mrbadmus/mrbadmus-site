# KS4 topics with no exam question

_Generated 26 Oct 2026 (fix/b2c-small) from the backend's own pure code, read only: `consumer/work.js` `examTopicsAvailable()` / `examScope()` (both exported), run over (a) the KS4 scheme rows `ks4_seed_sow.build_block()` emits — the source of `supabase/seeds/20260902001000_ks4_default_sequence.sql`, i.e. the global `scheme_of_work_entries` a family child's scheme is read from — and (b) the KS4 `exam_questions` rows built by the table's only writer, the backend's `scripts/seed-exam-questions.js`: `bonding_v2` (the five `shared/exam-content/*.js` files) + `code_seed` (`scripts/exam-seed-code.js`). No database was read. If production holds KS4 rows those builders do not make, this list over-reports; if the production scheme was seeded from an older run of `ks4_seed_sow.py` (865 rows, against 876 today) a few subtopic names differ but no topic does._

A topic is listed when `GET /api/consumer/children/:id/picker` returns `exam: false` for it: no active KS4 question that fits the child's tier and pathway (`examFitsFor`) is placed in that topic by `examScope`. A child's scheme is one year group, so the cohorts are pathway × tier × year.

## Summary

- KS4 exam questions in the pool: **41** (Chemistry 31, Biology 5, Physics 5). Chemistry's are almost all Bonding (the five `bonding_v2` pages); Biology and Physics have five each (`code_seed`).
- Distinct KS4 scheme topics: **25**. With at least one question on some route: **11**. With **no question on any route: 14**:
  - Biology — Bioenergetics
  - Biology — Cell Biology
  - Biology — Ecology
  - Chemistry — Atomic Structure and the Periodic Table
  - Chemistry — Chemical Analysis
  - Chemistry — Chemistry of the Atmosphere
  - Chemistry — Energy Changes
  - Chemistry — Organic Chemistry
  - Chemistry — Quantitative Chemistry
  - Chemistry — Using Resources
  - Physics — Atomic Structure
  - Physics — Magnetism and Electromagnetism
  - Physics — Particle Model of Matter
  - Physics — Space Physics
- Every other topic has 1–2 questions, except Bonding (21 Foundation / 28 Higher). A topic's availability is the same on every route that teaches it; Homeostasis and Chemical Changes move between Year 10 and Year 11 by pathway, which is why the per-year lists differ.
- Effect today: a child whose week has no unit-ending lesson and whose subjects' topics are all on this list gets no Friday exam item (`notes: ['no_exam_questions']`); the parent's picker must not offer "An exam question" on a listed topic (`u.exam === false`).

## By cohort

### Combined Foundation, Year 10

| Subject | Topic | Exam questions | Subtopics |
|---|---|---|---|
| Biology | Cell Biology | **none** | 7 |
| Biology | Organisation | 2 | 11 |
| Biology | Infection and Response | 1 | 7 |
| Biology | Bioenergetics | **none** | 7 |
| Chemistry | Atomic Structure and the Periodic Table | **none** | 12 |
| Chemistry | Bonding, Structure and Properties of Matter | 21 | 11 |
| Chemistry | Quantitative Chemistry | **none** | 5 |
| Physics | Energy | 1 | 8 |
| Physics | Electricity | 1 | 10 |
| Physics | Particle Model of Matter | **none** | 6 |

### Combined Foundation, Year 11

| Subject | Topic | Exam questions | Subtopics |
|---|---|---|---|
| Biology | Homeostasis and Response | 1 | 8 |
| Biology | Inheritance, Variation and Evolution | 1 | 14 |
| Biology | Ecology | **none** | 15 |
| Chemistry | Chemical Changes | 1 | 10 |
| Chemistry | Energy Changes | **none** | 2 |
| Chemistry | Rate and Extent of Chemical Change | 2 | 5 |
| Chemistry | Organic Chemistry | **none** | 4 |
| Chemistry | Chemical Analysis | **none** | 4 |
| Chemistry | Chemistry of the Atmosphere | **none** | 4 |
| Chemistry | Using Resources | **none** | 4 |
| Physics | Atomic Structure | **none** | 7 |
| Physics | Forces | 2 | 11 |
| Physics | Waves | 1 | 6 |
| Physics | Magnetism and Electromagnetism | **none** | 3 |

### Combined Higher, Year 10

| Subject | Topic | Exam questions | Subtopics |
|---|---|---|---|
| Biology | Cell Biology | **none** | 7 |
| Biology | Organisation | 2 | 11 |
| Biology | Infection and Response | 1 | 7 |
| Biology | Bioenergetics | **none** | 7 |
| Chemistry | Atomic Structure and the Periodic Table | **none** | 12 |
| Chemistry | Bonding, Structure and Properties of Matter | 28 | 11 |
| Chemistry | Quantitative Chemistry | **none** | 8 |
| Physics | Energy | 1 | 8 |
| Physics | Electricity | 1 | 10 |
| Physics | Particle Model of Matter | **none** | 6 |
| Physics | Atomic Structure | **none** | 7 |

### Combined Higher, Year 11

| Subject | Topic | Exam questions | Subtopics |
|---|---|---|---|
| Biology | Homeostasis and Response | 1 | 8 |
| Biology | Inheritance, Variation and Evolution | 1 | 14 |
| Biology | Ecology | **none** | 15 |
| Chemistry | Chemical Changes | 1 | 12 |
| Chemistry | Energy Changes | **none** | 3 |
| Chemistry | Rate and Extent of Chemical Change | 2 | 6 |
| Chemistry | Organic Chemistry | **none** | 4 |
| Chemistry | Chemical Analysis | **none** | 4 |
| Chemistry | Chemistry of the Atmosphere | **none** | 4 |
| Chemistry | Using Resources | **none** | 5 |
| Physics | Forces | 2 | 15 |
| Physics | Waves | 1 | 7 |
| Physics | Magnetism and Electromagnetism | **none** | 5 |

### Triple Foundation, Year 10

| Subject | Topic | Exam questions | Subtopics |
|---|---|---|---|
| Biology | Cell Biology | **none** | 8 |
| Biology | Organisation | 2 | 11 |
| Biology | Infection and Response | 1 | 8 |
| Biology | Bioenergetics | **none** | 7 |
| Biology | Homeostasis and Response | 1 | 12 |
| Chemistry | Atomic Structure and the Periodic Table | **none** | 13 |
| Chemistry | Bonding, Structure and Properties of Matter | 21 | 12 |
| Chemistry | Quantitative Chemistry | **none** | 7 |
| Chemistry | Chemical Changes | 1 | 11 |
| Physics | Energy | 1 | 8 |
| Physics | Electricity | 1 | 12 |
| Physics | Particle Model of Matter | **none** | 6 |
| Physics | Atomic Structure | **none** | 11 |

### Triple Foundation, Year 11

| Subject | Topic | Exam questions | Subtopics |
|---|---|---|---|
| Biology | Inheritance, Variation and Evolution | 1 | 19 |
| Biology | Ecology | **none** | 22 |
| Chemistry | Energy Changes | **none** | 4 |
| Chemistry | Rate and Extent of Chemical Change | 2 | 5 |
| Chemistry | Organic Chemistry | **none** | 10 |
| Chemistry | Chemical Analysis | **none** | 8 |
| Chemistry | Chemistry of the Atmosphere | **none** | 4 |
| Chemistry | Using Resources | **none** | 9 |
| Physics | Forces | 2 | 13 |
| Physics | Waves | 1 | 8 |
| Physics | Magnetism and Electromagnetism | **none** | 3 |
| Physics | Space Physics | **none** | 4 |

### Triple Higher, Year 10

| Subject | Topic | Exam questions | Subtopics |
|---|---|---|---|
| Biology | Cell Biology | **none** | 8 |
| Biology | Organisation | 2 | 11 |
| Biology | Infection and Response | 1 | 9 |
| Biology | Bioenergetics | **none** | 7 |
| Biology | Homeostasis and Response | 1 | 12 |
| Chemistry | Atomic Structure and the Periodic Table | **none** | 13 |
| Chemistry | Bonding, Structure and Properties of Matter | 28 | 12 |
| Chemistry | Quantitative Chemistry | **none** | 10 |
| Chemistry | Chemical Changes | 1 | 13 |
| Physics | Energy | 1 | 8 |
| Physics | Electricity | 1 | 12 |
| Physics | Particle Model of Matter | **none** | 6 |
| Physics | Atomic Structure | **none** | 11 |

### Triple Higher, Year 11

| Subject | Topic | Exam questions | Subtopics |
|---|---|---|---|
| Biology | Inheritance, Variation and Evolution | 1 | 19 |
| Biology | Ecology | **none** | 23 |
| Chemistry | Energy Changes | **none** | 5 |
| Chemistry | Rate and Extent of Chemical Change | 2 | 6 |
| Chemistry | Organic Chemistry | **none** | 12 |
| Chemistry | Chemical Analysis | **none** | 8 |
| Chemistry | Chemistry of the Atmosphere | **none** | 4 |
| Chemistry | Using Resources | **none** | 10 |
| Physics | Forces | 2 | 18 |
| Physics | Waves | 1 | 12 |
| Physics | Magnetism and Electromagnetism | **none** | 10 |
| Physics | Space Physics | **none** | 5 |

## Subtopics inside the no-question topics

Exam availability is a TOPIC property (the picker's `u.exam` is per unit); a subtopic is only an extra name `examScope` matches a question's `topic` against. So every subtopic of a listed topic has no exam question either. Per pathway/tier, both years together:

- **combined/foundation Biology — Cell Biology**: `eukaryotes-prokaryotes`, `animal-plant-cells`, `cell-specialisation`, `microscopy`, `chromosomes-mitosis`, `stem-cells`, `transport-in-cells`
- **combined/foundation Biology — Bioenergetics**: `photosynthesis`, `rate-of-photosynthesis`, `uses-of-glucose`, `aerobic-respiration`, `anaerobic-respiration`, `response-to-exercise`, `metabolism`
- **combined/foundation Chemistry — Atomic Structure and the Periodic Table**: `atoms-elements-compounds`, `mixtures`, `model-of-the-atom`, `subatomic-particles`, `relative-atomic-mass`, `electronic-structure`, `periodic-table`, `development-periodic-table`, `metals-non-metals`, `group-0`, `group-1`, `group-7`
- **combined/foundation Chemistry — Quantitative Chemistry**: `conservation-of-mass`, `relative-formula-mass`, `mass-changes-reactions`, `chemical-measurements`, `concentration-of-solutions`
- **combined/foundation Physics — Particle Model of Matter**: `density-of-materials`, `changes-of-state`, `internal-energy`, `temperature-changes-shc`, `specific-latent-heat`, `particle-motion-pressure`
- **combined/foundation Biology — Ecology**: `ecosystems`, `abiotic-biotic-factors`, `adaptations`, `food-chains-webs`, `population-competition`, `biodiversity`, `waste-management`, `land-use`, `deforestation`, `global-warming`, `maintaining-biodiversity`, `carbon-cycle`, `water-cycle`, `decomposition`, `sampling-techniques`
- **combined/foundation Chemistry — Energy Changes**: `exothermic-endothermic`, `reaction-profiles`
- **combined/foundation Chemistry — Organic Chemistry**: `crude-oil-hydrocarbons`, `fractional-distillation`, `properties-of-hydrocarbons`, `cracking-alkenes`
- **combined/foundation Chemistry — Chemical Analysis**: `pure-substances`, `formulations`, `chromatography`, `testing-for-gases`
- **combined/foundation Chemistry — Chemistry of the Atmosphere**: `composition-of-atmosphere`, `early-atmosphere`, `greenhouse-gases`, `atmospheric-pollutants`
- **combined/foundation Chemistry — Using Resources**: `earths-resources`, `potable-water`, `life-cycle-assessment`, `reducing-use-of-resources`
- **combined/foundation Physics — Atomic Structure**: `structure-of-atom`, `mass-number-isotopes`, `development-atomic-model`, `radioactive-decay`, `nuclear-equations`, `half-lives`, `radioactive-contamination`
- **combined/foundation Physics — Magnetism and Electromagnetism**: `poles-of-a-magnet`, `magnetic-fields`, `electromagnetism`
- **combined/higher Biology — Cell Biology**: `eukaryotes-prokaryotes`, `animal-plant-cells`, `cell-specialisation`, `microscopy`, `chromosomes-mitosis`, `stem-cells`, `transport-in-cells`
- **combined/higher Biology — Bioenergetics**: `photosynthesis`, `rate-of-photosynthesis`, `uses-of-glucose`, `aerobic-respiration`, `anaerobic-respiration`, `response-to-exercise`, `metabolism`
- **combined/higher Chemistry — Atomic Structure and the Periodic Table**: `atoms-elements-compounds`, `mixtures`, `model-of-the-atom`, `subatomic-particles`, `relative-atomic-mass`, `electronic-structure`, `periodic-table`, `development-periodic-table`, `metals-non-metals`, `group-0`, `group-1`, `group-7`
- **combined/higher Chemistry — Quantitative Chemistry**: `conservation-of-mass`, `relative-formula-mass`, `mass-changes-reactions`, `chemical-measurements`, `concentration-of-solutions`, `moles`, `amounts-in-equations`, `using-moles-calculations`
- **combined/higher Physics — Particle Model of Matter**: `density-of-materials`, `changes-of-state`, `internal-energy`, `temperature-changes-shc`, `specific-latent-heat`, `particle-motion-pressure`
- **combined/higher Physics — Atomic Structure**: `structure-of-atom`, `mass-number-isotopes`, `development-atomic-model`, `radioactive-decay`, `nuclear-equations`, `half-lives`, `radioactive-contamination`
- **combined/higher Biology — Ecology**: `ecosystems`, `abiotic-biotic-factors`, `adaptations`, `food-chains-webs`, `population-competition`, `biodiversity`, `waste-management`, `land-use`, `deforestation`, `global-warming`, `maintaining-biodiversity`, `carbon-cycle`, `water-cycle`, `decomposition`, `sampling-techniques`
- **combined/higher Chemistry — Energy Changes**: `exothermic-endothermic`, `reaction-profiles`, `bond-energy-calculations`
- **combined/higher Chemistry — Organic Chemistry**: `crude-oil-hydrocarbons`, `fractional-distillation`, `properties-of-hydrocarbons`, `cracking-alkenes`
- **combined/higher Chemistry — Chemical Analysis**: `pure-substances`, `formulations`, `chromatography`, `testing-for-gases`
- **combined/higher Chemistry — Chemistry of the Atmosphere**: `composition-of-atmosphere`, `early-atmosphere`, `greenhouse-gases`, `atmospheric-pollutants`
- **combined/higher Chemistry — Using Resources**: `earths-resources`, `potable-water`, `life-cycle-assessment`, `reducing-use-of-resources`, `alternative-metal-extraction`
- **combined/higher Physics — Magnetism and Electromagnetism**: `poles-of-a-magnet`, `magnetic-fields`, `electromagnetism`, `flemings-left-hand-rule`, `electric-motors`
- **triple/foundation Biology — Cell Biology**: `eukaryotes-prokaryotes`, `animal-plant-cells`, `cell-specialisation`, `microscopy`, `chromosomes-mitosis`, `stem-cells`, `transport-in-cells`, `culturing-microorganisms`
- **triple/foundation Biology — Bioenergetics**: `photosynthesis`, `rate-of-photosynthesis`, `uses-of-glucose`, `aerobic-respiration`, `anaerobic-respiration`, `response-to-exercise`, `metabolism`
- **triple/foundation Chemistry — Atomic Structure and the Periodic Table**: `atoms-elements-compounds`, `mixtures`, `model-of-the-atom`, `subatomic-particles`, `relative-atomic-mass`, `electronic-structure`, `periodic-table`, `development-periodic-table`, `metals-non-metals`, `group-0`, `group-1`, `group-7`, `transition-metals`
- **triple/foundation Chemistry — Quantitative Chemistry**: `conservation-of-mass`, `relative-formula-mass`, `mass-changes-reactions`, `chemical-measurements`, `percentage-yield`, `atom-economy`, `concentration-of-solutions`
- **triple/foundation Physics — Particle Model of Matter**: `density-of-materials`, `changes-of-state`, `internal-energy`, `temperature-changes-shc`, `specific-latent-heat`, `particle-motion-pressure`
- **triple/foundation Physics — Atomic Structure**: `structure-of-atom`, `mass-number-isotopes`, `development-atomic-model`, `radioactive-decay`, `nuclear-equations`, `half-lives`, `radioactive-contamination`, `background-radiation`, `uses-of-nuclear-radiation`, `nuclear-fission`, `nuclear-fusion`
- **triple/foundation Biology — Ecology**: `ecosystems`, `abiotic-biotic-factors`, `adaptations`, `food-chains-webs`, `population-competition`, `biodiversity`, `waste-management`, `land-use`, `deforestation`, `global-warming`, `maintaining-biodiversity`, `carbon-cycle`, `water-cycle`, `decomposition`, `trophic-levels`, `pyramids-of-biomass`, `transfer-of-biomass`, `sampling-techniques`, `factors-affecting-food-security`, `farming-techniques`, `sustainable-fisheries`, `role-of-biotechnology`
- **triple/foundation Chemistry — Energy Changes**: `exothermic-endothermic`, `reaction-profiles`, `cells-and-batteries`, `fuel-cells`
- **triple/foundation Chemistry — Organic Chemistry**: `crude-oil-hydrocarbons`, `fractional-distillation`, `properties-of-hydrocarbons`, `cracking-alkenes`, `structure-of-alkenes`, `reactions-of-alkenes`, `alcohols`, `carboxylic-acids`, `addition-polymerisation`, `dna-naturally-occurring-polymers`
- **triple/foundation Chemistry — Chemical Analysis**: `pure-substances`, `formulations`, `chromatography`, `testing-for-gases`, `flame-tests`, `metal-hydroxides`, `carbonates-halides-sulfates`, `instrumental-methods`
- **triple/foundation Chemistry — Chemistry of the Atmosphere**: `composition-of-atmosphere`, `early-atmosphere`, `greenhouse-gases`, `atmospheric-pollutants`
- **triple/foundation Chemistry — Using Resources**: `earths-resources`, `potable-water`, `life-cycle-assessment`, `reducing-use-of-resources`, `corrosion-prevention`, `alloys-useful-materials`, `ceramics-polymers-composites`, `haber-process`, `npk-fertilisers`
- **triple/foundation Physics — Magnetism and Electromagnetism**: `poles-of-a-magnet`, `magnetic-fields`, `electromagnetism`
- **triple/foundation Physics — Space Physics**: `solar-system-gravity`, `stellar-evolution`, `red-shift-big-bang`, `dark-matter-dark-energy`
- **triple/higher Biology — Cell Biology**: `eukaryotes-prokaryotes`, `animal-plant-cells`, `cell-specialisation`, `microscopy`, `chromosomes-mitosis`, `stem-cells`, `transport-in-cells`, `culturing-microorganisms`
- **triple/higher Biology — Bioenergetics**: `photosynthesis`, `rate-of-photosynthesis`, `uses-of-glucose`, `aerobic-respiration`, `anaerobic-respiration`, `response-to-exercise`, `metabolism`
- **triple/higher Chemistry — Atomic Structure and the Periodic Table**: `atoms-elements-compounds`, `mixtures`, `model-of-the-atom`, `subatomic-particles`, `relative-atomic-mass`, `electronic-structure`, `periodic-table`, `development-periodic-table`, `metals-non-metals`, `group-0`, `group-1`, `group-7`, `transition-metals`
- **triple/higher Chemistry — Quantitative Chemistry**: `conservation-of-mass`, `relative-formula-mass`, `mass-changes-reactions`, `chemical-measurements`, `percentage-yield`, `atom-economy`, `concentration-of-solutions`, `moles`, `amounts-in-equations`, `using-moles-calculations`
- **triple/higher Physics — Particle Model of Matter**: `density-of-materials`, `changes-of-state`, `internal-energy`, `temperature-changes-shc`, `specific-latent-heat`, `particle-motion-pressure`
- **triple/higher Physics — Atomic Structure**: `structure-of-atom`, `mass-number-isotopes`, `development-atomic-model`, `radioactive-decay`, `nuclear-equations`, `half-lives`, `radioactive-contamination`, `background-radiation`, `uses-of-nuclear-radiation`, `nuclear-fission`, `nuclear-fusion`
- **triple/higher Biology — Ecology**: `ecosystems`, `abiotic-biotic-factors`, `adaptations`, `food-chains-webs`, `population-competition`, `biodiversity`, `waste-management`, `land-use`, `deforestation`, `global-warming`, `maintaining-biodiversity`, `carbon-cycle`, `water-cycle`, `decomposition`, `trophic-levels`, `pyramids-of-biomass`, `transfer-of-biomass`, `sampling-techniques`, `environmental-change`, `factors-affecting-food-security`, `farming-techniques`, `sustainable-fisheries`, `role-of-biotechnology`
- **triple/higher Chemistry — Energy Changes**: `exothermic-endothermic`, `reaction-profiles`, `cells-and-batteries`, `fuel-cells`, `bond-energy-calculations`
- **triple/higher Chemistry — Organic Chemistry**: `crude-oil-hydrocarbons`, `fractional-distillation`, `properties-of-hydrocarbons`, `cracking-alkenes`, `structure-of-alkenes`, `reactions-of-alkenes`, `alcohols`, `carboxylic-acids`, `addition-polymerisation`, `condensation-polymerisation`, `amino-acids`, `dna-naturally-occurring-polymers`
- **triple/higher Chemistry — Chemical Analysis**: `pure-substances`, `formulations`, `chromatography`, `testing-for-gases`, `flame-tests`, `metal-hydroxides`, `carbonates-halides-sulfates`, `instrumental-methods`
- **triple/higher Chemistry — Chemistry of the Atmosphere**: `composition-of-atmosphere`, `early-atmosphere`, `greenhouse-gases`, `atmospheric-pollutants`
- **triple/higher Chemistry — Using Resources**: `earths-resources`, `potable-water`, `life-cycle-assessment`, `reducing-use-of-resources`, `corrosion-prevention`, `alloys-useful-materials`, `ceramics-polymers-composites`, `haber-process`, `npk-fertilisers`, `alternative-metal-extraction`
- **triple/higher Physics — Magnetism and Electromagnetism**: `poles-of-a-magnet`, `magnetic-fields`, `electromagnetism`, `flemings-left-hand-rule`, `electric-motors`, `loudspeakers-headphones`, `induced-potential`, `uses-generator-effect`, `microphones`, `transformers`
- **triple/higher Physics — Space Physics**: `solar-system-gravity`, `gravity-stable-orbits`, `stellar-evolution`, `red-shift-big-bang`, `dark-matter-dark-energy`

## How to regenerate

Dump the scheme with `ks4_seed_sow.build_block()` for every `BLOCKS` entry, then call `require('<backend>/consumer/work.js').examTopicsAvailable(rows, schemeBySubject, fits)` per cohort with `fits` = the `examFitsFor` rule (a row's non-null tier/pathway must equal the child's). The script used is not kept in the repo; it is 40 lines and reads nothing but the files named above.
