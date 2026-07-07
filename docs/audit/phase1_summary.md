# Phase 1 content audit — summary

Source: the 12 `all_subtopics_*.py` files (audited at source, not generated HTML).
Coverage: **264 unique subtopic pages**, **865 page-variants** (subject × pathway × tier).

## Defects by severity

| severity | count |
|---|---|
| critical | 837 |
| major | 2146 |
| minor | 819 |
| info | 143 |

## Defects by rule

| rule | severity | count |
|---|---|---|
| 1-count | critical | 837 |
| 1-count | major | 28 |
| 1-register | minor | 819 |
| 1-triple-depth | major | 367 |
| 2-example-count | major | 206 |
| 2-practice-absent | major | 210 |
| 2-tier-duplication | major | 96 |
| 3-mistake-first | major | 827 |
| 4-menu | info | 143 |
| 5-tier-integrity | major | 412 |

## Worst 25 page-variants (by severity score)

| page | pathway | tier | score |
|---|---|---|---|
| biology/homeostasis/blood-glucose-diabetes | triple | higher | 29 |
| biology/inheritance/genetic-inheritance | triple | higher | 29 |
| biology/inheritance/inherited-disorders | triple | higher | 29 |
| chemistry/analysis/chromatography | triple | higher | 29 |
| chemistry/atomic-structure/mixtures | triple | higher | 29 |
| chemistry/atomic-structure/relative-atomic-mass | triple | higher | 29 |
| chemistry/energy-changes/exothermic-endothermic | triple | higher | 29 |
| chemistry/quantitative/chemical-measurements | triple | higher | 29 |
| chemistry/quantitative/concentration-of-solutions | triple | higher | 29 |
| chemistry/quantitative/mass-changes-reactions | triple | higher | 29 |
| chemistry/quantitative/relative-formula-mass | triple | higher | 29 |
| chemistry/rates-equilibrium/calculating-rates | triple | higher | 29 |
| physics/atomic-structure/half-lives | triple | higher | 29 |
| physics/atomic-structure/mass-number-isotopes | triple | higher | 29 |
| physics/atomic-structure/nuclear-equations | triple | higher | 29 |
| physics/electricity/current-resistance-pd | triple | higher | 29 |
| physics/electricity/direct-alternating-pd | triple | higher | 29 |
| physics/electricity/electrical-charge-current | triple | higher | 29 |
| physics/electricity/energy-transfers-appliances | triple | higher | 29 |
| physics/electricity/national-grid | triple | higher | 29 |
| physics/electricity/power-electricity | triple | higher | 29 |
| physics/electricity/series-parallel-circuits | triple | higher | 29 |
| physics/energy/changes-in-energy | triple | higher | 29 |
| physics/energy/efficiency | triple | higher | 29 |
| physics/energy/energy-changes-in-systems | triple | higher | 29 |

## Lineup fingerprint clusters (rule 4, informational)

Optional-block lineups shared by ≥15 page-variants — check the lineup is a coincidence of need, not a default. Key: variables, equations, key_note, common_mistake, higher, triple_only, rp, matching, fifas, quiz

- `0011000101` × 286 (e.g. biology/combined/foundation/cell-biology/cell-specialisation)
- `0011100101` × 110 (e.g. biology/combined/higher/cell-biology/chromosomes-mitosis)
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
