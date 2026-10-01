# Batch 5 — diagram library audit

Method: grepped `figlib/biology.py`, `figlib/biochem.py`, `figlib/chemistry.py`,
`figlib/physics.py`, `figlib/ks4phys.py`, `figlib/charts.py`,
`shared/ks4-diagrams.js`, `ks3_art/*.py` and `ks4_lessons/authored/batch-2/`
+ `batch-3/*.dc.html` for function names and docstrings naming each lesson's
subject matter, then read the matching function/docstring to confirm it is a
real match and not a substring collision. Several near-hits turned out to be
false positives or only loosely related: `figlib/chemistry.py`'s `atmosphere_pie()`
and `carbon_cycle()` are the CHEMISTRY atmosphere unit's causes-of-warming
figures, not this batch's BIOLOGY ecology "effects on ecosystems" lesson;
`ks3_art/b3.py`'s `r_system_switch` levelled chain (`Cell`/`Tissue`/`Organ`/
`Organism`) is wired to a specific immune-system job-sort scenario, not a
general hierarchy diagram, so it is not counted as a match for any Batch-5
lesson. Function names and line numbers below are exact, from this
worktree's working tree.

`shared/ks4-diagrams.js` was checked in full again and remains entirely
circuit-symbol and bonding/particle-model primitives — nothing in it concerns
any Batch-5 topic; listed here as checked, not cited again below.

| # | Lesson | Existing drawing code that already covers it |
|---|---|---|
| 1 | land-use | None found anywhere searched (figlib, ks3_art, batch-2/3 `.dc.html`). No peat-bog, land-use or conservation-vs-extraction figure exists. |
| 2 | metals-non-metals | No static figure. `ks3_art/c8.py:276 r_property_sorter()` ("c8-01 `#s-bench`") is a KS3 interactive instrument sorting six unlabelled samples as metal/non-metal by physical property — same content, DOM instrument not a figure. `figlib/chemistry.py:362 ionic_dotcross(formula)` draws the metal-loses/non-metal-gains electron-transfer picture for specific compounds (NaCl, MgO, etc.) — covers the ELECTRON-TRANSFER half of this lesson, not a general metal-vs-non-metal properties comparison. |
| 3 | reactivity-series | **Direct match:** `figlib/chemistry.py:1181 reactivity_series()` — "vertical reactivity-series ladder, most reactive at top. Carbon and Hydrogen marked as non-metal reference points" — exactly this lesson's classification content. |
| 4 | energy-resources | No static figure. `ks3_art/p2.py:825 r_renewable_sort()` ("p2-05 `#s-sort`") is a KS3 interactive instrument sorting eight resources on renewable-vs-non-renewable only (deliberately not mixing in the pollution question) — same classification, DOM instrument not a figure. |
| 5 | structure-of-atom | **Direct match:** `figlib/physics.py:1390 atom_diagram(symbol, protons, neutrons)` — "Atom with labelled nucleus (protons + neutrons) and electron shells filled 2,8,8,2 from the proton count" — exactly the nuclear-model content this lesson teaches. `figlib/physics.py:1455 isotope_notation()` (the ᴬZX notation card) is the companion figure for this spec point's isotope sub-content. |
| 6 | plant-tissues | **Reusable match:** `ks3_art/b7.py:99 _leaf_section()` — a labelled leaf cross-section (cuticle, epidermis, palisade mesophyll, spongy mesophyll, vein, stoma) with CO₂ in through the pore and water up the vein — this is exactly the "leaf tissues working as one organ" content, KS3-styled. |
| 7 | waste-management | None found anywhere searched. No pollutant-source-to-effect or land/air/water pollution figure exists for this BIOLOGY ecology lesson (distinct from the chemistry `water_treatment()` figure matched under #13 below, which is a different lesson/spec point). |
| 8 | earths-resources | **Direct match:** `figlib/chemistry.py:2421 life_cycle_assessment()` — "Flow strip: extraction -> manufacture -> use -> disposal" — this is precisely the life-cycle-assessment content named in AQA 5.10.1.1. |
| 9 | development-atomic-model | **Direct match:** `figlib/physics.py:1497 history_of_atom()` — "Three-panel strip: plum pudding -> nuclear (Rutherford) -> Bohr" — exactly this lesson's model-development content. (Not to be confused with batch-4's `development-periodic-table`, which needed a DIFFERENT — still-missing — Newlands/Mendeleev figure.) |
| 10 | global-warming | No direct match for this lesson's content (effects on ecosystems). `figlib/chemistry.py:2304 carbon_cycle()` and `:2257 atmosphere_pie()` are the sibling CHEMISTRY atmosphere-unit figures (causes of warming, not ecosystem effects) — wrong content, same general subject area. `ks4_lessons/authored/batch-3/early-atmosphere.dc.html` and `greenhouse-gases.dc.html` are the sibling KS4 chemistry atmosphere lessons' Design deliveries, worth opening for visual-style consistency, as neither draws ecosystem-effects content. |
| 11 | group-0 | No static figure. `figlib/chemistry.py:934 electronic_configuration(symbol)` is general-purpose (any element) and can draw a noble gas's full outer shell on request — reusable, not noble-gas-specific. `ks3_art/c8.py` `c8-06 #s-uses` is a KS3 interactive instrument judging three real uses of the noble gases — DOM instrument, not a figure. |
| 12 | extraction-of-metals | **Direct match (electrolysis half):** `figlib/chemistry.py:1068 electrolysis(setup="molten_Al2O3")` — a ready-made labelled electrolysis-cell setup for exactly "Molten aluminium oxide, Al₂O₃ (in cryolite)" with cathode/anode half-equations, covering the electrolysis-extraction half of this lesson. No static figure for the carbon-reduction/blast-furnace half. `ks3_art/c9.py:551 r_extraction_route()` ("c9-03 `#s-bench`") is a KS3 interactive instrument choosing among four extraction methods for six metals — same classification content, DOM instrument not a figure. |
| 13 | potable-water | **Direct match:** `figlib/chemistry.py:2461 water_treatment()` — "Potable water treatment flow: reservoir -> screen -> sediment -> filter -> chlorinate -> tap" — exactly this lesson's main treatment-process content. `figlib/biochem.py:177 distillation_flask()` covers the desalination-by-distillation sub-content of this spec point (5.10.1.2–5.10.1.3 names both methods). |
| 14 | radioactive-decay | **Direct match:** `figlib/physics.py:1580 radiation_penetration()` — "Alpha, beta, gamma penetration through paper/aluminium/lead" — exactly this lesson's dangers/shielding content (this is the SAME function batch-4 flagged as a false positive for infrared-black-bodies; here it is a genuine, direct match). Also `figlib/physics.py:1633 half_life_curve()` — "Exponential decay curve with half-life ticks" — direct match for the half-life sub-content; `figlib/physics.py:1455 isotope_notation()` is reusable for this lesson's notation too. |
| 15 | red-shift-big-bang | **Direct match:** `figlib/physics.py:2610 red_shift()` — "Spectrum from a nearby galaxy vs a distant galaxy showing red shift" — exactly this lesson's evidence-for-expansion content. |

## Figures still needed

1. **land-use** — a figure contrasting land-use pressures (quarrying, farming, building, dumping waste) competing for the same land, plus a peat-bog-specific pair: an intact peat bog (carbon locked in waterlogged, undecomposed plant matter) vs a drained/burned one (carbon released as CO₂, habitat lost).
2. **metals-non-metals** — a general physical/chemical-properties comparison figure (lustre, conductivity, malleability, melting point, ions formed) for a metal and a non-metal side by side — `ionic_dotcross()` already covers the electron-transfer mechanism, so this gap is specifically the PROPERTIES comparison, not the bonding picture.
3. **energy-resources** — a renewable-vs-non-renewable figure showing the UK's (or a generic) energy mix, and/or a figure contrasting one renewable and one non-renewable resource's environmental impact side by side — `r_renewable_sort()` is KS3-interactive and classification-only, not an impact figure.
4. **plant-tissues** — (contingent on reusing `_leaf_section()`) if a KS4-styled version is wanted rather than the KS3 drawer directly, the only gap is restyling; the content (cuticle/epidermis/palisade/spongy mesophyll/vein/stoma) already matches this lesson's organ-level content exactly.
5. **waste-management** — a pollutant figure specific to the ecology topic: land pollution (landfill, litter), water pollution (sewage, fertiliser run-off, eutrophication), air pollution (acid rain, particulates) — each with its effect on biodiversity, distinct from the chemistry atmospheric-pollutants figure already flagged as needed in batch 4.
6. **earths-resources** — (contingent on reusing `life_cycle_assessment()`) no new figure strictly needed for the LCA flow; a companion figure contrasting a finite resource (crude oil, metal ores) with a renewable/sustainable one (timber grown for building) would round out the "finite vs renewable, natural vs synthetic" classification content.
7. **global-warming** — an ecosystem-effects figure: rising sea level flooding coastal habitats, a shifting species range/migration-pattern map, and coral bleaching or similar, so the BIOLOGY content (distinct from the chemistry causes-of-warming figures) has its own visual.
8. **group-0** — (contingent on reusing `electronic_configuration()`) a trend figure down Group 0 showing boiling point increasing with atomic number/more shells, next to the shared full-outer-shell explanation for inertness.
9. **extraction-of-metals** — a blast-furnace cross-section for the carbon-reduction half (iron ore + coke + limestone in, molten iron + slag out) to pair with the already-available `electrolysis(setup="molten_Al2O3")` figure for the electrolysis half.
10. **potable-water** — (contingent on reusing `water_treatment()` and `distillation_flask()`) no new figure strictly needed; a labelled desalination set-up specific to seawater (distinct from the generic lab distillation flask) would match the spec's own wording more closely if wanted.
11. **radioactive-decay** — (contingent on reusing `radiation_penetration()`, `half_life_curve()` and `isotope_notation()`) no new figure strictly needed; nothing in the existing set shows a nuclear equation (alpha/beta decay changing mass/atomic number) visually, which would be the one genuine gap if wanted.
12. **red-shift-big-bang** — (contingent on reusing `red_shift()`) no new figure strictly needed; a simple expanding-universe/raisin-bread-model figure (galaxies moving apart, more distant ones moving faster) would directly illustrate Hubble's Law alongside the existing spectrum figure.
