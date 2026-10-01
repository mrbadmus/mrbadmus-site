# Batch 7 — diagram library audit

Method: grepped `figlib/biology.py`, `figlib/biochem.py`, `figlib/chemistry.py`,
`figlib/physics.py`, `figlib/ks4phys.py`, `figlib/charts.py`,
`shared/ks4-diagrams.js`, `ks3_art/*.py` and `ks4_lessons/authored/batch-2/`
+ `batch-3/*.dc.html` for function names and docstrings naming each lesson's
subject matter, then read the matching function/docstring to confirm it is a
real match and not a substring collision. Near-hits checked and ruled out:
`ks4_lessons/authored/batch-3/early-atmosphere.dc.html`,
`ks4_lessons/authored/batch-2/carbon-cycle.dc.html` and
`ks4_lessons/authored/batch-2/decomposition.dc.html` all mention
"photosynthesis"/"respiration" repeatedly in prose (the carbon cycle's gas
exchange) — none of the three draws a photosynthesis or respiration figure;
they are a different unit's content citing these processes in passing.
`shared/ks4-diagrams.js` was checked in full and remains entirely
circuit-symbol and bonding/particle-model primitives — nothing in it concerns
any Batch-7 topic; listed here as checked, not cited again below.

| # | Lesson | Existing drawing code that already covers it |
|---|---|---|
| 1 | communicable-diseases-defence | None found anywhere searched. No skin/mucus/stomach-acid/phagocyte/lymphocyte defence-system figure exists in figlib or ks3_art. |
| 2 | viral-diseases | None found anywhere searched. No HIV/AIDS, measles or tobacco-mosaic-virus figure exists. |
| 3 | bacterial-diseases | None found anywhere searched. No salmonella/gonorrhoea figure exists. |
| 4 | fungal-protist-diseases | None found anywhere searched. No rose-black-spot/malaria figure exists. |
| 5 | vaccination | None found anywhere searched. No antigen/antibody/herd-immunity figure exists. |
| 6 | antibiotics-painkillers | None found anywhere searched. No antibiotic-resistance figure exists. |
| 7 | drug-discovery-development | None found anywhere searched. No clinical-trial-stages/placebo/thalidomide figure exists. |
| 8 | monoclonal-antibodies | None found anywhere searched. No hybridoma-production figure exists. |
| 9 | plant-disease-detection-defence | None found anywhere searched. No plant-defence (physical/chemical/mechanical) figure exists. |
| 10 | photosynthesis | None found anywhere searched for the reaction itself. No `photosynthesis()`/`chloroplast()` figure exists in `figlib/biology.py` or `figlib/biochem.py` — the only two files in the whole estate with a bare "photosynthesis" docstring hit (`early-atmosphere.dc.html`, `carbon-cycle.dc.html`) cite it as prose, not drawing code. |
| 11 | rate-of-photosynthesis | **Reusable match:** `figlib/charts.py:352 line_graph()` — "Axes, a light grid, and one or more series" — generic, reusable for a light-intensity-vs-rate curve with a limiting-factor plateau; not photosynthesis-specific, a general chart builder. No dedicated limiting-factors or inverse-square-law figure exists. |
| 12 | uses-of-glucose | None found anywhere searched. No starch/lipid/protein/cellulose fate-of-glucose figure exists. |
| 13 | aerobic-respiration | None found anywhere searched. No mitochondrion/aerobic-equation figure exists. |
| 14 | anaerobic-respiration | None found anywhere searched. No lactic-acid/fermentation figure exists. |
| 15 | response-to-exercise | **Reusable match:** `figlib/charts.py:352 line_graph()` / `figlib/charts.py:480 graph_panels()` — generic line-chart builders, reusable for a heart-rate/breathing-rate-over-time or oxygen-debt recovery curve; not exercise-specific. |
| 16 | metabolism | None found anywhere searched. No build-up/breakdown classification figure exists. |

## Figures still needed

1. **communicable-diseases-defence** — a "lines of defence" figure: skin (barrier), mucus/cilia in airways, stomach acid, clotting, with phagocytes and lymphocytes as the second line once a pathogen breaches the first.
2. **viral-diseases** — a disease → pathogen → spread → control summary figure for measles, HIV/AIDS and tobacco mosaic virus, each with its symptoms and control measure.
3. **bacterial-diseases** — a salmonella vs gonorrhoea contrast figure: toxin production vs direct damage, and why antibiotics treat one but resistance is rising.
4. **fungal-protist-diseases** — a pathogen-type classification figure (fungus vs protist) with the vector/symptom that identifies each (rose black spot vs malaria via mosquito).
5. **vaccination** — a primary-vs-secondary immune response figure: antigen exposure, antibody production curve over time, memory cells, and the faster/bigger secondary response.
6. **antibiotics-painkillers** — a contrast figure: antibiotics kill bacteria (mechanism) vs painkillers treat symptoms only, plus a resistance-emerging-by-selection figure.
7. **drug-discovery-development** — a trial-stages flowchart in order (cells → animals → healthy volunteers (phase 1) → patients (phase 2/3), placebo and double-blind controls).
8. **monoclonal-antibodies** — a hybridoma-production figure: mouse immunised → antibody-producing cell fused with tumour cell → hybridoma → cloned → monoclonal antibodies harvested.
9. **plant-disease-detection-defence** — a plant-defence classification figure: physical (waxy cuticle, bark, cell wall), chemical (antimicrobial substances, poisons) and mechanical (thorns, leaf drop) defences, paired with the detection methods (observation, lab testing, microscopy).
10. **photosynthesis** — an inputs-to-outputs process figure: CO₂ + water + light energy → (chloroplast, chlorophyll) → glucose + oxygen, the word and symbol equations side by side.
11. **rate-of-photosynthesis** — (contingent on reusing `line_graph()`) a limiting-factors figure: three curves (light intensity, CO₂ concentration, temperature) each plateauing at a different limiting factor, matching the RP5 light-intensity-distance practical.
12. **uses-of-glucose** — a "fate of glucose" branching figure: respiration, starch (storage), cellulose (cell walls), fats/oils, amino acids (with nitrate), each with its one-line use.
13. **aerobic-respiration** — a mitochondrion-location figure with the word equation (glucose + oxygen → carbon dioxide + water (+ energy)) and where in the cell it happens.
14. **anaerobic-respiration** — an aerobic-vs-anaerobic contrast figure: oxygen needed/not needed, products (CO₂+water vs lactic acid in animals, ethanol+CO₂ in plants/yeast), energy released (more vs less).
15. **response-to-exercise** — (contingent on reusing `line_graph()`/`graph_panels()`) a heart-rate/breathing-rate rise during exercise, oxygen debt building during anaerobic respiration, then recovery curve after exercise stops.
16. **metabolism** — a build-up vs breakdown classification figure: synthesis reactions (glucose → starch/glycogen, amino acids → proteins, fatty acids+glycerol → lipids) vs breakdown reactions (respiration, breakdown of excess protein → urea).
