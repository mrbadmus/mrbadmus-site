# Batch 4 — diagram library audit

Method: grepped `figlib/biology.py`, `figlib/biochem.py`, `figlib/chemistry.py`,
`figlib/physics.py`, `figlib/ks4phys.py`, `figlib/charts.py`,
`shared/ks4-diagrams.js`, `ks3_art/*.py` and `ks4_lessons/authored/batch-2/`
+ `batch-3/*.dc.html` for function names and docstrings naming each lesson's
subject matter, then read the matching function/docstring to confirm it is a
real match and not a substring collision (several near-hits below turned out
to be false positives on a generic word — `_conductor` in `figlib/physics.py`
is an electromagnetism helper, not thermal conductivity; every "coronary /
atherosclerosis / plaque" grep hit in `ks3_art/*.py` was the word
"consistent"; `c4.py`'s "efficien" hits were all "coefficient"). Function
names and line numbers below are exact, from this worktree's working tree.

`shared/ks4-diagrams.js` (Design's pilot KS4 diagram module) was checked in
full: it is entirely circuit-symbol and bonding/particle-model primitives
(`atom`, `covalent`, `lattice`, `metallic`, `particles`, `circuit`, the `SYM`
electrical-component table). Nothing in it concerns any batch-4 topic
(circulation, cells, ecology, the periodic table, energy efficiency, thermal
conductivity, infrared/black bodies, or EM wave uses) — it is listed here as
checked, not cited again below.

| # | Lesson | Existing drawing code that already covers it |
|---|---|---|
| 1 | heart-blood-vessels | None found. `ks3_art/b3.py`, `b4.py`, `b7.py` mention "capillary"/"vein" but only for leaf veins and alveolar/villus gas-exchange capillaries — not the human heart or its own blood vessels. No heart, artery or vein structural figure exists anywhere searched. |
| 2 | water-cycle | **Direct match:** `figlib/biology.py:560 water_cycle()` — "Schematic with sun, sea, clouds, mountain, river — labelled processes: evaporation, condensation, precipitation, run-off." This is the lesson's figure already drawn. |
| 3 | atmospheric-pollutants | No direct match. `figlib/chemistry.py:2257 atmosphere_pie()` draws today's atmosphere composition (N₂/O₂/Ar pie) — same unit family (atmosphere) but the wrong figure (composition, not pollutant source → effect). `ks4_lessons/authored/batch-3/early-atmosphere.dc.html` and `greenhouse-gases.dc.html` are the sibling atmosphere lessons' Design deliveries, worth opening for visual-style consistency, but neither draws pollutant pathways. |
| 4 | efficiency | **Direct match:** `figlib/physics.py:924 sankey(input_label, input_J, outputs, title=None)` — general proportional Sankey diagram, input/useful/wasted bands. **Also:** `figlib/ks4phys.py:337 sankey_simple(...)` — a simpler to-scale Sankey (fixed px-per-joule), explicitly documents "NEVER drawn: a scale bar or grid, a percentage, 'efficiency' — unless a label says so." Either covers the lesson's Sankey-diagram theory content. |
| 5 | infrared-black-bodies | No match. `figlib/physics.py:1580 radiation_penetration()` draws alpha/beta/gamma barrier penetration — same general "physics radiation" family, wrong content (not infrared emission/absorption or black-body colour contrast). |
| 6 | transport-in-cells | No match. `ks3_art/b4.py`, `b8.py`, `c1.py` only mention "diffusion"/"osmosis" in prose/comments (gas-exchange rate discussion, mineral-uptake failure mode, a diffusion-timing example) — none draws a cell membrane with diffusion/osmosis/active-transport arrows. |
| 7 | blood | No match. `ks3_art/b1.py` and `b6.py` only use "white blood cell" / "plasma" in unrelated prose (immune-response discrimination test; excretion). No red cell / white cell / platelet / plasma figure exists. |
| 8 | periodic-table | **Reusable interactive pattern, not a static figure:** `ks3_art/c8.py:683 r_table_reader(a, act_id)` — the KS3 periodic-table instrument (20 elements, 4 periods, 8 groups; payload split into `elements` / `layout` / `families`). Its own docstring states: *"NOTES-C8 §4 asks for this explicitly so the same twenty elements can be redrawn as a long-form table without touching a single note, and says C9 and any KS4 table lesson want the same one."* — i.e. this data shape is the one Design/engineering already intend a KS4 periodic-table lesson to reuse. It is DOM markup (no canvas), so a KS4 version would need its own render, but the EL/LAYOUT/FAMILIES contract is designed to carry over. |
| 9 | thermal-conductivity | No static figure. Closest existing pattern: `ks3_art/p1.py:1229 r_conduction_bench(a, act_id)` and `p1.py:1451 r_insulation_trial(a, act_id)` — KS3 "Energy transfers" unit interactive benches for conduction and the wrapped-material insulation RP, the same RP2 investigation this lesson's `rp` field names. Both are interactive DOM instruments, not static diagrams, and are KS3-styled. |
| 10 | coronary-heart-disease | None found anywhere searched (ks3_art, figlib). No plaque/artery-narrowing/stent figure exists. |
| 11 | biodiversity | No direct match. Generic ecology primitives exist and could be adapted: `figlib/biology.py:730 food_web(nodes, eats, ...)` (labelled boxes + directional arrows, could show a food web losing a species), `figlib/biology.py:213 pyramid_of_biomass(...)`/`:280 biomass_flow()`. `ks3_art/b9.py:1720 r_quadrat_bench(a, act_id)` is a KS3 quadrat-sampling instrument (interactive, not a figure) for the closest practical-method overlap (sampling to measure species). None of these IS a biodiversity figure. |
| 12 | development-periodic-table | No match beyond the same `ks3_art/c8.py` table-reader noted for lesson 8 — this lesson is historical (Newlands/Mendeleev's table with gaps), and no figure anywhere draws an early/incomplete periodic table arrangement. |
| 13 | uses-em-waves | **Direct match:** `figlib/physics.py:2563 em_spectrum()` — "EM spectrum band: radio -> gamma," already drawn with each band's colour AND a named use per band (radio: TV/radio; microwave: cooking/satellites; infrared: heaters/remote controls; visible: what we see; UV: sun beds/fluorescence; X-ray: medical imaging; gamma: treating cancer) — this is exactly the lesson's "use → wave, and why" content. `ks4_lessons/authored/batch-3/types-of-em-waves.dc.html` is the sibling KS4 EM-waves lesson's Design delivery (inline `<svg>` elements at lines 42/49/86) — worth opening for visual-style consistency with this lesson, though it was not parsed for reusable function names (it is markup, not a figlib function). |

## Figures still needed

1. **heart-blood-vessels** — a heart cross-section showing all four chambers (left/right atrium, left/right ventricle) and the valves, labelled, with the direction of blood flow; a separate (or combined) figure contrasting artery / vein / capillary wall structure (thick muscular wall vs thin wall with valves vs one-cell-thick wall) and what each structural feature is for.
2. **atmospheric-pollutants** — a pollutant pathway figure: fuel burning → pollutant (CO, SO₂, NOₓ, particulates) → the effect each one causes (global dimming, acid rain, respiratory problems), plus a catalytic converter cross-section showing CO + NO → CO₂ + N₂ passing over the catalyst.
3. **infrared-black-bodies** — a matt-black vs shiny surface contrast showing which absorbs/emits more infrared (e.g. a Leslie's cube with one blackened and one shiny face, each face's relative emission indicated); a black body with the absorption = emission balance point labelled.
4. **transport-in-cells** — a single cell membrane figure with three labelled arrows/panels: diffusion (particles, high→low, no energy), osmosis (water only, through a partially permeable membrane, dilute→concentrated), active transport (low→high, against the gradient, ATP + carrier protein) — ideally also showing a plant cell turgid vs plasmolysed and an animal cell swollen/lysed vs crenated.
5. **blood** — the four blood components in one figure: red blood cells (biconcave, no nucleus), white blood cells (phagocyte/lymphocyte), platelets, plasma — each with its one-line job.
6. **periodic-table** — (contingent on 05's `r_table_reader` reuse decision) at minimum a figure showing an element's position (group, period) derived from its electron structure — e.g. the same element drawn both as an electron-shell diagram and as its periodic-table square, with the link between outer-shell electrons and group number made visible.
7. **thermal-conductivity** — a particle-vibration figure showing energy transfer along a solid by particle-to-particle collision (conduction), contrasted with a poor conductor/insulator slowing the same transfer; a labelled RP2 insulation-trial set-up (beaker, insulating material, thermometer, timer).
8. **coronary-heart-disease** — an artery cross-section showing fatty-plaque build-up (atherosclerosis) narrowing the lumen, progressing to a near-blocked artery; a stent holding an artery open, and a labelled statin/diet treatment-options figure.
9. **biodiversity** — a figure contrasting a high-biodiversity habitat (many species, interconnected food web) with a low-biodiversity one (monoculture or post-species-loss), and/or a figure showing the knock-on effect through a food web when one species is removed.
10. **development-periodic-table** — a timeline/table figure showing Newlands' table (with its octave groupings and known errors) next to Mendeleev's table (with its deliberate gaps for undiscovered elements), so the gap-prediction evidence is visible rather than only described.
11. **uses-em-waves** — (contingent on reuse of `em_spectrum()`, confirmed above) no new figure strictly needed; if a KS4-specific version is wanted, the only gap is matching this lesson's exact use-list (the lesson's `theory` groups radio/microwave, infrared/visible/UV, X-ray/gamma rather than `em_spectrum()`'s seven individual uses — a relabelling exercise, not a new drawing).
