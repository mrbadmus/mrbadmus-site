# Batch 10 — diagram library audit

Method: grepped `figlib/biology.py`, `figlib/biochem.py`, `figlib/chemistry.py`,
`figlib/physics.py`, `figlib/ks4phys.py`, `figlib/charts.py`,
`shared/ks4-diagrams.js`, `ks3_art/*.py` and `ks4_lessons/authored/batch-2/`
+ `batch-3/*.dc.html` for function names and docstrings naming each lesson's
subject matter, then read the matching function/docstring to confirm it is a
real match and not a substring collision. One genuine forward reference found:
`ks4_lessons/authored/batch-2/carbon-cycle.dc.html`'s own `connects` array
links forward to `['deforestation', 'Deforestation']` via `K.hrefFor` (line
384) and its activity's model answer references "deforestation affect"
(line 451) — a real link to a page that does not yet exist, same pattern as
batch-6's stem-cells link and batch-8's lenses→the-eye links. Near-hits
checked and ruled out: `ks4_lessons/authored/batch-2/decomposition.dc.html`
(promising by name for ecosystems/trophic content — it is entirely about the
carbon-cycle decay process, not food webs or population ecology, and makes no
reference to any Batch-10 slug). `figlib/chemistry.py:2304 carbon_cycle()` is
cited below under deforestation as a contingent reuse, not a direct match.
`shared/ks4-diagrams.js` remains entirely circuit-symbol and bonding/
particle-model primitives — nothing in it concerns any Batch-10 topic; listed
here as checked, not cited again below.

| # | Lesson | Existing drawing code that already covers it |
|---|---|---|
| 1 | ecosystems | **Direct match, KS3 bench:** `ks3_art/b9.py:1154 r_remove_a_species()` — "take one out of an oak wood and follow it" — exactly this lesson's interdependence content (remove one species, follow the knock-on effect through the web), including a deliberate non-feeding dependency (bees pollinate but are not eaten) to teach that feeding is not the only kind of dependence. Built on `ks3_art/b9.py:44 _food_web()`, a reusable food-web drawer. |
| 2 | population-competition | **Direct match, KS3 bench:** `ks3_art/b9.py:986 r_cycle_runner()` — "two rules, twenty-six years, and a lag" — a predator-prey population-cycle model with carrying capacity, exactly this lesson's competition-and-population-change content. |
| 3 | abiotic-biotic-factors | None found anywhere searched. No figure classifies factors as abiotic vs biotic specifically; the closest material (`r_cycle_runner()`'s carrying capacity, `r_remove_a_species()`'s web) concerns competition and interdependence (cited under #1/#2), not the abiotic/biotic classification itself. |
| 4 | adaptations | None found anywhere searched. No structural/behavioural/functional adaptation classification figure exists in figlib or ks3_art. |
| 5 | food-chains-webs | **Direct match, three pieces:** `figlib/biology.py:166 food_chain()` (linear chain with energy-flow arrows) and `figlib/biology.py:730 food_web()` (labelled boxes joined by one-way arrows, feeder's box gets the arrowhead) are both generic, reusable figlib figures drawn for exactly this content. `ks3_art/b9.py:44 _food_web()` / `r_remove_a_species()` (cited under #1) is the same content as a KS3 DOM bench, built around the identical rule that arrow direction points at the EATER — named as the topic's most commonly lost mark. |
| 6 | sampling-techniques | **Direct match, KS3 bench:** `ks3_art/b9.py:1720 r_quadrat_bench()` — "a field you can check your answer against" — a random-vs-biased quadrat-placement bench showing why random sampling and larger sample size matter, exactly this lesson's content (the lesson's own RP6 and FIFA are quadrat/mark-recapture, see `_extract-notes.md`). |
| 7 | environmental-change | None found anywhere searched for a distribution-data-over-time figure specific to environmental change (e.g. indicator species, pH/temperature trend). **Reusable, contingent match:** `ks3_art/b9.py:1487 r_bioaccumulation()` ("one lake, six levels, and a persistence dial") models how a persistent pollutant concentrates up a food chain over time — a genuine environmental-change mechanism, but framed around bioaccumulation/toxicity rather than this lesson's indicator-species/distribution-shift content. `figlib/charts.py:352 line_graph()` is a generic, reusable chart for any measured-quantity-over-time data. |
| 8 | deforestation | **Reusable, contingent match:** `figlib/chemistry.py:2304 carbon_cycle()` — "boxes and labelled arrows for the carbon cycle... photosynthesis, respiration, feeding, decay, combustion" — the sibling KS4 lesson `ks4_lessons/authored/batch-2/carbon-cycle.dc.html` forward-links to this slug (see Method above) and already states deforestation's double effect (fewer trees photosynthesising + felled trees burned/rotting) in its own text — worth opening for content consistency, but `carbon_cycle()` itself draws the whole cycle, not deforestation's specific tree-clearing/biodiversity-loss chain. |
| 9 | maintaining-biodiversity | **Reusable, contingent match:** `ks3_art/b9.py:1302 r_supermarket_shelf()` — "twelve foods, and two numbers that fall differently" — models insect-pollinator loss reducing food availability and nutritional variety, a genuine biodiversity/ecosystem-service angle, but framed around pollinators specifically rather than this lesson's conservation-programme/hedgerow/trade-off content. |
| 10 | trophic-levels | **Direct match, two pieces:** `figlib/biology.py:166 food_chain()` (organisms labelled by role: producer, primary consumer, etc. — exactly a trophic-level classification) and `ks3_art/b9.py:754 r_chain_ledger()` ("ten thousand kilojoules, and what is left at the top" — levels stacked bottom-up, producer at the bottom, a tenth surviving each step) — the same trophic-level structure as a KS3 bench. |
| 11 | pyramids-of-biomass | **Direct match:** `figlib/biology.py:213 pyramid_of_biomass()` — "stack of trapezoidal layers, each proportional to biomass" — the function name and content match this lesson exactly (constructing a pyramid from biomass data at each level). **Reusable alternative:** `figlib/biochem.py:125 pyramid()` is a generic stacked-horizontal-bar pyramid (white bars, no colour coding) usable for the same data in a different visual style. |
| 12 | transfer-of-biomass | **Direct match, two pieces:** `figlib/biology.py:280 biomass_flow()` — "Sankey-style flow showing 10% biomass transfer up trophic levels" — the exact mechanism and ~10% figure this lesson teaches. `ks3_art/b9.py:754 r_chain_ledger()` (cited under #10) is the identical 10%-per-step rule as a KS3 bench ("ten thousand kilojoules, and what is left at the top"). |
| 13 | farming-techniques | None found anywhere searched. No intensive-vs-free-range/organic comparison figure exists. `ks3_art/b9.py`'s `r_supermarket_shelf()` (pollinators, cited under #9) and `r_bioaccumulation()` (persistent chemicals, cited under #7) are farming-adjacent but neither classifies or contrasts farming methods. |
| 14 | sustainable-fisheries | None found anywhere searched. No fish-stock/quota/net-size figure exists in figlib or ks3_art. |
| 15 | role-of-biotechnology | None found anywhere searched. No mycoprotein-fermenter or GM-crop-production figure exists in figlib or ks3_art. |

## Figures still needed

1. **ecosystems** — none needed for species-removal/interdependence; `r_remove_a_species()` already covers it directly as a KS3 bench (a KS4-styled static version would still be useful for consistency, but the content figure exists).
2. **population-competition** — none needed for the predator-prey cycle; `r_cycle_runner()` already covers it. A simpler static intraspecific-vs-interspecific competition contrast figure would complement it.
3. **abiotic-biotic-factors** — a factor-classification figure: abiotic (temperature, light, pH, moisture, wind) vs biotic (predation, disease, competition, food availability), the one genuinely missing figure for this lesson.
4. **adaptations** — a three-column classification figure: structural (camel's hump) vs behavioural (migration) vs functional (antifreeze proteins), each with one named example.
5. **food-chains-webs** — none needed; `food_chain()`/`food_web()` already cover this directly, in the correct arrow-points-at-the-eater convention.
6. **sampling-techniques** — none needed; `r_quadrat_bench()` already covers random vs biased placement directly. A labelled transect/belt-transect set-up figure (distinct from the quadrat bench) would complete the RP6 picture.
7. **environmental-change** — an indicator-species figure (e.g. mayfly larvae present/absent against water quality) distinct from `r_bioaccumulation()`'s pollutant-concentration angle, since this lesson is about interpreting distribution data as evidence of change, not about bioaccumulation itself.
8. **deforestation** — a deforestation-specific chain figure (fewer trees → less photosynthesis → less CO₂ removed, AND felled trees burned/rotting → more CO₂ released, converging on rising atmospheric CO₂) plus a biodiversity-loss side-effect, distinct from the whole-cycle `carbon_cycle()` figure.
9. **maintaining-biodiversity** — a conservation-programme figure showing the trade-off named in this lesson's quiz (habitat protection vs land for farming/building, funding costs), distinct from `r_supermarket_shelf()`'s pollinator-specific framing.
10. **trophic-levels** — none needed for level classification; `food_chain()`/`r_chain_ledger()` already cover it. A trophic-level LABELS figure (producer, primary/secondary/tertiary consumer, decomposer) as a standalone reference card would still help.
11. **pyramids-of-biomass** — none needed; `pyramid_of_biomass()` already covers constructing a pyramid from data directly.
12. **transfer-of-biomass** — none needed; `biomass_flow()` already covers the ~10% efficiency mechanism directly. A respiration/egestion/excretion three-way loss breakdown (this lesson's `common_mistake` content) would complement it.
13. **farming-techniques** — an intensive vs free-range contrast figure (space, feed efficiency, welfare, yield), the one genuinely missing figure for this lesson.
14. **sustainable-fisheries** — a quota/net-size/no-catch-zone figure showing how each measure lets a fish stock recover, with one named case of overfishing a stock to collapse.
15. **role-of-biotechnology** — a mycoprotein-fermenter figure (Fusarium grown on glucose syrup in large fermentation vessels, aerobic conditions, harvested and purified) alongside a GM-crop-production figure (herbicide resistance or pest resistance gene inserted), the two production routes this lesson covers.
