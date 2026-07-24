# Phase 1 content audit — summary

Source: the 12 `all_subtopics_*.py` files (audited at source, not generated HTML).
Coverage: **264 unique subtopic pages**, **865 page-variants** (subject × pathway × tier).

## Defects by severity

| severity | count |
|---|---|
| critical | 791 |
| major | 2055 |
| minor | 2112 |
| info | 962 |

## Defects by rule

| rule | severity | count |
|---|---|---|
| 1-count | critical | 791 |
| 1-count | major | 28 |
| 1-length-parity | minor | 1331 |
| 1-register | minor | 781 |
| 1-triple-depth | major | 345 |
| 2-example-count | major | 206 |
| 2-practice-absent | major | 210 |
| 2-tier-duplication | major | 96 |
| 3-mistake-first | major | 781 |
| 4-menu | info | 143 |
| 5-tier-integrity | major | 389 |
| 8-examiner-tip | info | 819 |

## Worst 25 page-variants (by severity score)

| page | pathway | tier | score |
|---|---|---|---|
| biology/homeostasis/blood-glucose-diabetes | triple | higher | 31 |
| biology/inheritance/inherited-disorders | triple | higher | 31 |
| chemistry/atomic-structure/relative-atomic-mass | triple | higher | 31 |
| physics/atomic-structure/half-lives | triple | higher | 31 |
| physics/electricity/energy-transfers-appliances | triple | higher | 31 |
| physics/electricity/national-grid | triple | higher | 31 |
| physics/electricity/series-parallel-circuits | triple | higher | 31 |
| physics/energy/changes-in-energy | triple | higher | 31 |
| physics/energy/energy-changes-in-systems | triple | higher | 31 |
| physics/forces/forces-elasticity | triple | higher | 31 |
| physics/particle-model/particle-motion-pressure | triple | higher | 31 |
| physics/particle-model/temperature-changes-shc | triple | higher | 31 |
| biology/inheritance/genetic-inheritance | triple | higher | 30 |
| chemistry/analysis/chromatography | triple | higher | 30 |
| chemistry/quantitative/chemical-measurements | triple | higher | 30 |
| chemistry/quantitative/concentration-of-solutions | triple | higher | 30 |
| chemistry/quantitative/mass-changes-reactions | triple | higher | 30 |
| chemistry/rates-equilibrium/calculating-rates | triple | higher | 30 |
| physics/electricity/current-resistance-pd | triple | higher | 30 |
| physics/electricity/electrical-charge-current | triple | higher | 30 |
| physics/electricity/power-electricity | triple | higher | 30 |
| physics/energy/efficiency | triple | higher | 30 |
| physics/energy/power | triple | higher | 30 |
| physics/forces/distance-speed-velocity | triple | higher | 30 |
| physics/forces/work-done-energy-transfer | triple | higher | 30 |

## Lineup fingerprint clusters (rule 4, informational)

Optional-block lineups shared by ≥15 page-variants — check the lineup is a coincidence of need, not a default. Key: variables, equations, key_note, common_mistake, higher, triple_only, rp, matching, fifas, quiz

- `0011000101` × 285 (e.g. biology/combined/foundation/cell-biology/cell-specialisation)
- `0011100101` × 109 (e.g. biology/combined/higher/cell-biology/chromosomes-mitosis)
- `1111000111` × 74 (e.g. biology/combined/foundation/cell-biology/eukaryotes-prokaryotes)
- `0111000101` × 48 (e.g. biology/combined/foundation/bioenergetics/aerobic-respiration)
- `1111001111` × 46 (e.g. biology/combined/foundation/cell-biology/microscopy)
- `0011001101` × 32 (e.g. biology/combined/foundation/cell-biology/animal-plant-cells)
- `0011110101` × 32 (e.g. biology/triple/higher/inheritance/meiosis)
- `0111100101` × 30 (e.g. biology/combined/higher/bioenergetics/aerobic-respiration)
- `0011010101` × 24 (e.g. biology/triple/foundation/inheritance/meiosis)
- `0011101101` × 16 (e.g. biology/combined/higher/organisation/digestive-system)
- `0111000111` × 16 (e.g. chemistry/combined/foundation/atomic-structure/relative-atomic-mass)
- `0111110101` × 16 (e.g. chemistry/triple/higher/energy-changes/fuel-cells)
