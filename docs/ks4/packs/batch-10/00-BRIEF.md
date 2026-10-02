# KS4 Batch 10 — Design input pack

Mide's ruling, 2 Oct 2026: **Design authors and draws every KS4 lesson from batch 4 on.** Code built this pack, will port your pages, check the science and ship them, exactly as for the pilot.

## Read first

- `docs/ks4/architecture.md` — the ten laws, the families, the CFIFA amendment, and **the two amendments of 2 Oct 2026** (Design writes the lessons; the four lesson rules).
- The pilot, as the bar and the template: `docs/ks4/design-reference/pilot/` (your delivery, unmodified) and the live pages it became.
- This file, then `FLAGS.md` (science you must not repeat), then each lesson's `04-checked-science-source/` file, then `05-diagram-library/README.md`.

## The four lesson rules (Mide, 2 Oct 2026) — apply to every lesson here

1. **Start here is a two-option guess**, framed as a guess, answerable from everyday experience on every route; the reveal is encouraging either way and leads straight into the teaching.
2. **Equations are formula triangles you can cover** — in the equation block, the equation-sheet panel and CFIFA's Formula step. A square or a ½ gets its own extra line (square-root, ×2).
3. **Teach every step before you test it.** A calculation that chains two equations gets its own "Step 1 … Step 2 …" worked example before any pupil does one; CFIFA on each step.
4. **Practice is the same size in every lesson** — same number of questions at each rung of the end practice and the exam ladder. Set the number once (at least the content-standards floor) and keep it across the batch.

Each lesson below says which calculations chain, which equations need triangles, and how many verbatim quiz items are usable; the rest of each bank is yours to write to the fixed size.

## Lessons

| # | lesson | slug | subject · topic | source file |
|---|---|---|---|---|
| 1 | Ecosystems | `ecosystems` | Biol · ecology | `04-checked-science-source/biology-4.7.1-ecosystems.md` |
| 2 | Population and Competition | `population-competition` | Biol · ecology | `04-checked-science-source/biology-4.7.1-population-competition.md` |
| 3 | Abiotic and Biotic Factors | `abiotic-biotic-factors` | Biol · ecology | `04-checked-science-source/biology-4.7.1-abiotic-biotic-factors.md` |
| 4 | Adaptations | `adaptations` | Biol · ecology | `04-checked-science-source/biology-4.7.2-adaptations.md` |
| 5 | Food Chains and Food Webs | `food-chains-webs` | Biol · ecology | `04-checked-science-source/biology-4.7.1-food-chains-webs.md` |
| 6 | Sampling Techniques | `sampling-techniques` | Biol · ecology | `04-checked-science-source/biology-4.7.1-sampling-techniques.md` |
| 7 | The Impact of Environmental Change | `environmental-change` | Biol · ecology | `04-checked-science-source/biology-4.7.4-environmental-change.md` |
| 8 | Deforestation | `deforestation` | Biol · ecology | `04-checked-science-source/biology-4.7.3.4-deforestation.md` |
| 9 | Maintaining Biodiversity | `maintaining-biodiversity` | Biol · ecology | `04-checked-science-source/biology-4.7.3.6-maintaining-biodiversity.md` |
| 10 | Trophic Levels | `trophic-levels` | Biol · ecology | `04-checked-science-source/biology-4.7.4.1-trophic-levels.md` |
| 11 | Pyramids of Biomass | `pyramids-of-biomass` | Biol · ecology | `04-checked-science-source/biology-4.7.4.2-pyramids-of-biomass.md` |
| 12 | Transfer of Biomass | `transfer-of-biomass` | Biol · ecology | `04-checked-science-source/biology-4.7.4.3-transfer-of-biomass.md` |
| 13 | Farming Techniques | `farming-techniques` | Biol · ecology | `04-checked-science-source/biology-4.7.5.2-farming-techniques.md` |
| 14 | Sustainable Fisheries | `sustainable-fisheries` | Biol · ecology | `04-checked-science-source/biology-4.7.5.3-sustainable-fisheries.md` |
| 15 | The Role of Biotechnology | `role-of-biotechnology` | Biol · ecology | `04-checked-science-source/biology-4.7.5.4-role-of-biotechnology.md` |

True routes, layers and families are in each lesson's entry below; they come from the AQA specification's own labels, checked by an examiner, and where they differ from what the site ships today the entry says so.

## Per lesson

### 1. Ecosystems
`ecosystems` · Biology / ecology · AQA 8464 4.7.1.1; 8461 4.7.1.1 · CF CH TF TH

- **Family:** SYSTEM — interdependence: take one species out and follow the knock-on through the community (BATCH-PLAN kept).
- **Flagship (a suggestion, not a spec):** a woodland web where the pupil removes one species and watches which populations rise and which fall.
- **Route layers:**
  - None. Every point is base. The `higher` field is not HT (ECO-F1): explaining a factor change from data is taught on every route.
- **Required practical:** none.
- **Calculations:** none.
- **Equations that need formula triangles (rule 2):** none.
- **Misconceptions to confront:**
  - "A community and an ecosystem are the same thing." — an ecosystem is the community interacting with the non-living (abiotic) parts.
  - "Removing a predator helps everything else." — prey numbers rise, overgraze, and plants and the animals that need them decline.
  - "Species only depend on each other for food." — also shelter, pollination, seed dispersal.
  - "A stable community means nothing changes." — population sizes stay fairly constant because species and environmental factors are in balance.
  - "A population is all the animals in a place." — one species only.
- **"Start here" access note (rule 1):** if all the bees in a park vanished, would the flowers be fine or would they suffer?
- **Practice (rule 4):** q1, q2, q3 usable on CF CH TF TH (3 per route). q2 wx1's second sentence is oddly worded but correct (ECO-F4). Design tops the bank up to the batch's fixed size, including a "suggest what these organisms compete for, given this habitat" item and a data item (a population table or graph after a species is removed).
- **Diagrams:** `05-diagram-library/README.md` row 1 — `ks3_art/b9.py r_remove_a_species()` / `_food_web()` already cover species removal. Must draw: the levels-of-organisation ladder (organism → population → community → ecosystem, with the abiotic parts added at the last step).
- **Examiner tip:** none approved.

---

### 2. Population and Competition
`population-competition` · Biology / ecology · AQA 8464 4.7.1.1, 4.7.2.1; 8461 4.7.1.1, 4.7.2.1 · CF CH TF TH

- **Family:** MODEL — the predator–prey cycle is a model whose graph pupils must read: prey rise, predators follow with a lag (BATCH-PLAN kept).
- **Flagship (a suggestion, not a spec):** a predator–prey graph the pupil scrubs through, with the lag between the two peaks marked and explained.
- **Route layers:**
  - None. Every on-spec point is base. The `higher` field is not HT (PC-F1); its predator–prey graph skill belongs on every route.
- **Required practical:** none.
- **Calculations:** none. (Reading values off a predator–prey graph is graph interpretation, MS 4a, not a calculation.)
- **Equations that need formula triangles (rule 2):** none.
- **Misconceptions to confront:**
  - "Predators and prey go up and down at the same time." — predator numbers follow prey with a lag (4.7.2.1).
  - "More prey means more predators straight away." — predators take time to breed.
  - "Different species never compete." — red and grey squirrels compete for food and nesting sites.
  - "Plants don't compete — they just stand there." — they compete for light, space, water and mineral ions.
  - "Animals only compete for food." — also mates and territory.
- **"Start here" access note (rule 1):** two plants grown packed close together in one pot, or one plant alone in the same pot — which grows bigger?
- **Practice (rule 4):** q1 usable on CF CH TF TH. q2 usable only if the page glosses "intraspecific / interspecific" (PC-F3); otherwise 1 per route. Design tops the bank up to the batch's fixed size, including a predator–prey graph-reading item and a "suggest what these organisms compete for" item.
- **Diagrams:** `05-diagram-library/README.md` row 2 — `ks3_art/b9.py r_cycle_runner()` already models the cycle and the lag. Must draw: a KS4 predator–prey graph (two offset curves, lag marked); a simple competition picture (plants for light/space/water/mineral ions; animals for food/mates/territory).
- **Examiner tip:** none approved.

---

### 3. Abiotic and Biotic Factors
`abiotic-biotic-factors` · Biology / ecology · AQA 8464 4.7.1.2, 4.7.1.3; 8461 4.7.1.2, 4.7.1.3 · CF CH TF TH

- **Family:** CLASSIFY — every factor sorts into non-living or living, from the spec's own two lists; then explain one change's effect on a community (BATCH-PLAN kept).
- **Flagship (a suggestion, not a spec):** a sorter: drag each factor card into abiotic or biotic, then pick one and predict what happens to a community when it changes.
- **Route layers:**
  - None. Every on-spec point is base. The `higher` field (indicator species) is neither HT nor in the spec — drop it (ABF-F1).
- **Required practical:** none on this page. (RP7 Combined / RP9 Biology, "investigate the effect of a factor on the distribution of this species", 8464/8461 4.7.2.1, all four routes — taught in sampling-techniques.)
- **Calculations:** none.
- **Equations that need formula triangles (rule 2):** none.
- **Misconceptions to confront:**
  - "The fish dying is the abiotic factor." — the fish are living (biotic); the oxygen level is abiotic.
  - "A disease is non-living because a germ is tiny." — pathogens are living: a new pathogen is a biotic factor.
  - "Competition between red and grey squirrels is abiotic because it changes the habitat." — it is a biotic factor: one species outcompeting another.
  - "Wind only matters for how strong it is." — the spec factor is wind intensity and direction.
  - "Abiotic factors only matter to plants." — oxygen levels decide which aquatic animals survive; temperature affects all.
- **"Start here" access note (rule 1):** why do you find different plants in a sunny field and under thick trees — the light, or the animals?
- **Practice (rule 4):** q1 usable on CF CH TF TH. q2 usable on all four if the page glosses "interspecific / intraspecific" (PC-F3); otherwise 1 per route. Design tops the bank up to the batch's fixed size, including a "how would a change in [factor] affect this community, given this data" item.
- **Diagrams:** `05-diagram-library/README.md` row 3 — nothing to reuse. Must draw: the two-column factor classification (the spec's seven abiotic and four biotic factors).
- **Examiner tip:** none approved.

---

### 4. Adaptations
`adaptations` · Biology / ecology · AQA 8464 4.7.1.4; 8461 4.7.1.4 · CF CH TF TH

- **Family:** CLASSIFY — every adaptation sorts as structural, behavioural or functional, the spec's own three types (BATCH-PLAN kept).
- **Flagship (a suggestion, not a spec):** an animal (polar bear, then fennec fox) whose features the pupil taps and drops into structural / behavioural / functional, each with what it does for survival.
- **Route layers:**
  - None. 4.7.1.4 has no HT and no biology-only content. Extremophiles are base and missing from the frozen data (AD-F1).
- **Required practical:** none.
- **Calculations:** none. (Surface area to volume ratio is used qualitatively here; the calculation lives in 4.1.3.1.)
- **Equations that need formula triangles (rule 2):** none.
- **Misconceptions to confront:**
  - "The fox grew big ears because it was hot." — individuals do not choose or grow adaptations; natural selection over many generations (4.6.2.2).
  - "Big animals lose heat faster because they're bigger." — small surface area to volume ratio keeps heat in.
  - "A camel's hump is full of water." — it stores fat.
  - "Adaptations are only body parts." — they may be structural, behavioural or functional.
  - "Nothing can live in boiling, crushing or salty places." — extremophiles do, e.g. bacteria in deep sea vents.
- **"Start here" access note (rule 1):** would a polar bear be comfortable in a desert, or would it overheat?
- **Practice (rule 4):** q1, q2 usable on CF CH TF TH (2 per route). Design tops the bank up to the batch's fixed size, including an extremophile item and a "given this information, explain how the organism is adapted" item.
- **Diagrams:** `05-diagram-library/README.md` row 4 — nothing to reuse. Must draw: the three-column structural / behavioural / functional figure with one clean example each (AD-F3); a cold-vs-desert ear-size comparison (SA:V).
- **Examiner tip:** none approved.

---

### 5. Food Chains and Food Webs
`food-chains-webs` · Biology / ecology · AQA 8464 4.7.2.1; 8461 4.7.2.1 (+ 8461 4.7.4.1, 4.7.4.3 biology only) · CF CH TF TH

- **Family:** SYSTEM — a web is a system: change one population and follow the knock-on effects along the arrows (BATCH-PLAN kept).
- **Flagship (a suggestion, not a spec):** a food web where the pupil removes or boosts one species and predicts which populations rise and fall, with arrows pointing at the eater.
- **Route layers:**
  - triple — "trophic level", energy/biomass lost at each level (~10%), why chains are short: 8461 4.7.4.1, 4.7.4.3 (biology only). Today on all four routes (FCW-F1).
  - triple — pyramids of biomass and transfer efficiency (the `higher` field): 8461 4.7.4.2, 4.7.4.3 (biology only), not HT. Today on CH TH (FCW-F2). Owned by pyramids-of-biomass and transfer-of-biomass; link only.
  - No HT content.
- **Required practical:** none on this page. (RP7 Combined / RP9 Biology, measuring population size and distribution with quadrats and transects, sits under 8464/8461 4.7.2.1, all four routes — taught in sampling-techniques.)
- **Calculations:** none on this page. (Efficiency of biomass transfer, 8461 4.7.4.3, triple, is taught in transfer-of-biomass.)
- **Equations that need formula triangles (rule 2):** none on this page.
- **Misconceptions to confront:**
  - "The arrow means 'eats'." — the arrow points from the food to the eater: the direction energy and biomass move.
  - "Plants aren't part of the food web." — producers start every food chain (4.7.2.1).
  - "Only plants are producers." — algae are producers too.
  - "If the foxes die, everything gets better for the grass." — more rabbits survive and eat more grass.
  - (TF TH) "Faeces are excreted." — they are egested (8461 4.7.4.3).
  - (TF TH) "Biomass is lost as heat." — energy is lost as heat; biomass is lost as CO₂, water, urea and faeces.
- **"Start here" access note (rule 1):** if all the foxes in a field disappeared, would there be more rabbits or fewer?
- **Practice (rule 4):** q2 usable on CF CH TF TH. q1 usable on TF TH only (FCW-F1). Per route: CF CH 1, TF TH 2. Design tops the bank up to the batch's fixed size, including a "draw / correct the arrows" item and a "species removed from this web — what happens to X" item on every route.
- **Diagrams:** `05-diagram-library/README.md` row 5 — `figlib/biology.py food_chain()` and `food_web()` (arrow points at the eater) and `ks3_art/b9.py r_remove_a_species()` cover it. Must draw: nothing new; a labelled chain (producer → primary → secondary → tertiary) on every route.
- **Examiner tip:** none approved.

---

### 6. Sampling Techniques
`sampling-techniques` · Biology / ecology · AQA 8464 4.7.2.1 (RP7); 8461 4.7.2.1 (RP9) · CF CH TF TH

**Family:** REQUIRED PRACTICAL — the lesson IS Combined RP7 / Biology RP9 (quadrats for population size, transect for distribution against a factor). BATCH-PLAN's INVESTIGATION changed: the AQA method and its exam questions are the point, and the architecture gives every RP its own family.

**Flagship (a suggestion, not a spec):** a field with tape-measure axes: generate random coordinates, drop quadrats, count, take the mean, scale up — then run a transect from hedge to open field with a light-meter reading at each quadrat.

**Route layers:**
- None HT; none labelled biology only. The `higher` field is base RP method, served CH TH only (SAMP-F4).
- triple (technique only): continuous sampling, 8461 8.2.9 AT 8 (RP9 only).
- Mark-recapture is in neither spec — cut (SAMP-F1).

**Required practical:** Combined RP7 (8464 4.7.2.1, 10.2.7) = Biology RP9 (8461 4.7.2.1, 8.2.9): "measure the population size of a common species in a habitat. Use sampling techniques to investigate the effect of a factor on the distribution of this species." All four routes. The frozen "RP6" label is wrong (SAMP-F2).

**Calculations:**
- Mean, mode and median of quadrat counts. No equation. **Chains equations? no.** Convert: nothing. Base.
- Population estimate from quadrats: population = mean per quadrat × (habitat area ÷ quadrat area). **Chains equations? yes** — Step 1 mean per quadrat (total counted ÷ number of quadrats); Step 2 scale up (mean × habitat area ÷ quadrat area). Needs its own "Step 1 … Step 2 …" worked example. Convert: quadrat side cm → m (50 cm → 0.5 m, so 0.25 m²); habitat and quadrat areas both in m². Base.
- Mark-recapture N = (n₁ × n₂) ÷ m: off-spec, not taught (SAMP-F1).

**Equations that need formula triangles (rule 2):**
- population = mean per m² × habitat area — Learn it (biology has no equation sheet). Triangle: population on top; mean per m² × area on the bottom. (Mean per m² = mean per quadrat ÷ quadrat area is its own line.)

**Misconceptions to confront:**
- "Throwing the quadrat is random." — the thrower chooses; use random coordinates (RP7/RP9).
- "The population is the number I counted." — the count is a sample; scale the mean up to the habitat area (MS 1d, 3a).
- "Put the quadrats where the plants are, so you find some." — biased placement overestimates; random avoids bias (MS 2d).
- "A transect tells you how many there are in the whole field." — transects show distribution, quadrats give abundance (4.7.2.1).
- "One quadrat is enough." — more quadrats give a more representative mean.

**"Start here" access note (rule 1):** counting every daisy on a school field — could you really count them all, or would you count a small patch and multiply?

**Practice (rule 4):** q1 (quadrat scale-up) and q3 (why random) usable on all four routes: 2. q2 not usable (SAMP-F1). Design tops the bank up to the batch's fixed size, including a mode/median item and a transect-graph-against-light item.

**Diagrams:** `05-diagram-library/README.md` row 6 (`ks3_art/b9.py r_quadrat_bench()` for random vs biased placement). Must draw: tape-measure grid with random coordinates; interrupted belt transect from shade to open ground with an abiotic-factor reading at each quadrat.

**Examiner tip:** none approved.

---

### 7. The Impact of Environmental Change
`environmental-change` · Biology / ecology · AQA 8461 4.7.2.4 (biology only) (HT only); not in 8464 · TH

**Family:** INVESTIGATION — the assessed skill is evaluating given distribution data (WS 1.4), not recall. BATCH-PLAN kept.

**Flagship (a suggestion, not a spec):** a species-range map with a time slider: pupils predict the shift for a temperature, water or atmospheric-gas change, then judge what the data does and does not show.

**Route layers:**
- triple-higher — the whole lesson, 8461 4.7.2.4 (biology only) (HT only). TH only is correct; the site's "4.7.4" label is not AQA's number.

**Required practical:** none.

**Calculations:** none.

**Equations that need formula triangles (rule 2):** none.

**Misconceptions to confront:**
- "The animals evolved to cope with the warming." — over decades, species mostly move or change timing; evolution takes many generations (4.6.2.1 link).
- "Only humans change the environment." — changes may be seasonal, geographic or caused by human interaction (4.7.2.4).
- "If a species is missing, pollution killed it." — evaluate the data: other factors (temperature, water, predators) could explain it (WS 1.4).
- "Warming just means everything moves north." — species at the warm edge can lose range; timing mismatches between species reduce survival.
- "Algae use up the oxygen." — light is blocked, plants die, and decomposing bacteria use the oxygen (ENV-F3).

**"Start here" access note (rule 1):** springs feel earlier than they used to — would a warmer spring make birds nest earlier or later?

**Practice (rule 4):** q2 (earlier bird breeding) usable on TH: 1. q1 not usable as written (ENV-F2). Design tops the bank up to the batch's fixed size, mostly given-data evaluation items across the three named changes.

**Diagrams:** `05-diagram-library/README.md` row 7 (`figlib/charts.py line_graph()` for data over time). Must draw: a species distribution/range map at two dates; a temperature-vs-time line paired with a species-count line.

**Examiner tip:** none approved.

---

### 8. Deforestation
`deforestation` · Biology / ecology · AQA 8464 4.7.3.4; 8461 4.7.3.4 · CF CH TF TH

**Family:** PROCESS — clearing → two CO₂ effects + habitat loss is a cause-and-effect chain, ending in the spec's evaluation. BATCH-PLAN kept.

**Flagship (a suggestion, not a spec):** fell a patch of forest and watch two CO₂ arrows change (photosynthesis in falls, burning and decay out rises) while the species count drops; then weigh food and biofuel against the cost.

**Route layers:**
- None. Every point is base on all four routes (8464/8461 4.7.3.4, with 4.7.2.2, 4.7.3.1, 4.7.3.5 links).

**Required practical:** none.

**Calculations:** none.

**Equations that need formula triangles (rule 2):** none.

**Misconceptions to confront:**
- "Trees make oxygen, so cutting them makes CO₂." — CO₂ rises because less is absorbed by photosynthesis and more is released by burning and decay (4.7.2.2).
- "Rotting wood doesn't give off CO₂ — only burning does." — decomposers respire and release CO₂ (4.7.2.2).
- "Forests are cleared for wood." — the spec's reasons are land for cattle and rice fields, and biofuel crops (4.7.3.4).
- "Biofuels are green, so clearing forest for them is fine." — evaluate: clearing releases CO₂ and destroys habitats (WS 1.4).
- "Only the trees are lost." — habitats for many species go, reducing biodiversity (4.7.3.1).

**"Start here" access note (rule 1):** a forest is cut down to make a cattle ranch — would the air end up with more carbon dioxide or less?

**Practice (rule 4):** 0 frozen items usable as written — q1 and q2 have correct stems, options and keys but every wrong_explanation is on the wrong option (DEF-F1, DEF-F2; corrected text is in the flags). Design tops the bank up to the batch's fixed size, including one evaluate (benefit + cost) item.

**Diagrams:** `05-diagram-library/README.md` row 8 (`figlib/chemistry.py carbon_cycle()` for consistency; batch-2 `carbon-cycle` page forward-links here). Must draw: the deforestation chain — fewer trees → less CO₂ absorbed; burning + decay → more CO₂ released; both → more atmospheric CO₂; habitat loss → less biodiversity.

**Examiner tip:** none approved.

---

### 9. Maintaining Biodiversity
`maintaining-biodiversity` · Biology / ecology · AQA 8464 4.7.3.6; 8461 4.7.3.6 · CF CH TF TH

**Family:** CLASSIFY — sort human interactions into positive and negative, and match each of the spec's five programmes to the problem it tackles; evaluation sits on top. BATCH-PLAN's INVESTIGATION changed: that family is method critique and data analysis, and this lesson has no method to design.

**Flagship (a suggestion, not a spec):** a farm-and-town scene where each human action is tapped as harming or helping biodiversity, then each programme is dragged onto the harm it fixes, with its cost showing.

**Route layers:**
- None. Every point is base on all four routes (8464/8461 4.7.3.6).

**Required practical:** none.

**Calculations:** none.

**Equations that need formula triangles (rule 2):** none.

**Misconceptions to confront:**
- "Maintaining biodiversity just means stop polluting." — the spec names five active programmes (4.7.3.6).
- "Hedgerows are there to help the crop grow." — they give wildlife food and shelter on single-crop farms (4.7.3.6).
- "Conservation is always the right answer." — it conflicts with land for food and housing, cost and jobs; evaluate (WS 1.5).
- "Zoos are only for visitors." — breeding programmes raise numbers of endangered species (4.7.3.6).
- "Recycling is about saving money, not wildlife." — less landfill means less land lost and less pollution (4.7.3.2, 4.7.3.6).

**"Start here" access note (rule 1):** a farmer pulls out the hedges to grow more wheat — would you expect more kinds of birds on the farm, or fewer?

**Practice (rule 4):** 0 frozen items usable as written — q1 and q2 have correct stems, options and keys but every wrong_explanation is on the wrong option (MB-F1, MB-F2; corrected text is in the flags). Design tops the bank up to the batch's fixed size, including a given-data evaluation item.

**Diagrams:** `05-diagram-library/README.md` row 9 (`ks3_art/b9.py r_supermarket_shelf()` — pollinator angle only). Must draw: single-crop field without vs with hedgerows and margins; a five-programme reference card; a trade-off balance (biodiversity vs land, cost, jobs).

**Examiner tip:** none approved.

---

### 10. Trophic Levels
`trophic-levels` · Biology / ecology · AQA 8461 4.7.4.1 (biology only); base link 8464/8461 4.7.2.1 · TF TH

**Family:** CLASSIFY — place each organism at level 1–4, apex predator or decomposer, and say why. BATCH-PLAN kept.

**Flagship (a suggestion, not a spec):** a food web where each organism is dropped onto a numbered level by what it eats; one organism that eats at two levels shows the number follows the chain, not the animal.

**Route layers:**
- triple — the whole lesson's numbered levels, apex predators and decomposer mechanism, 8461 4.7.4.1 (biology only). The producer/consumer names and food chains are base (8464/8461 4.7.2.1), re-used here.
- No HT content; the `higher` field is not HT and belongs to other lessons (TL-F1).

**Required practical:** none.

**Calculations:** none required by 4.7.4.1. (The 10 % transfer and efficiency calculation are 8461 4.7.4.3 — `transfer-of-biomass`.)

**Equations that need formula triangles (rule 2):** none.

**Misconceptions to confront:**
- "The arrow means 'eats', so it points at the food." — arrows point from the eaten to the eater: the direction of transfer (4.7.2.1).
- "A fox is always level 3." — the level depends on how far along the food chain it is feeding (4.7.4.1).
- "Decomposers eat dead things like animals do." — they secrete enzymes outside themselves; small soluble molecules diffuse in (4.7.4.1).
- "The top predator has the most energy because it eats everything." — only about 10 % of biomass passes up each level (4.7.4.3).
- "Apex predator just means biggest." — it is a carnivore with no predators (4.7.4.1).

**"Start here" access note (rule 1):** grass, rabbit, fox — which is first in the chain: the grass or the fox?

**Practice (rule 4):** q1 (arrow direction) and q2 (why few levels) usable on TF and TH: 2. Design tops the bank up to the batch's fixed size, including a "which level is this organism?" item and a decomposer-enzyme item.

**Diagrams:** `05-diagram-library/README.md` row 10 (`figlib/biology.py food_chain()`; `ks3_art/b9.py r_chain_ledger()`). Must draw: a four-level food chain with level numbers and names; a decomposer secreting enzymes with soluble molecules diffusing back in.

**Examiner tip:** none approved.

---

### 11. Pyramids of Biomass
`pyramids-of-biomass` · Biology / ecology · AQA 8461 4.7.4.2 (biology only); not in 8464 · TF TH

- **Family:** QUANTITATIVE — the spec skill is constructing an accurate, to-scale pyramid from data (MS 2c). BATCH-PLAN kept.
- **Flagship (a suggestion, not a spec):** pupils turn a table of biomass values into bars on a chosen scale, and see one oak tree outweigh thousands of caterpillars.
- **Route layers:** none. Whole lesson is 8461 4.7.4.2 (biology only); the `higher` field's construction skill is not HT (PB-F1).
- **Required practical:** none.
- **Calculations:**
  - Bar width = biomass ÷ scale value (e.g. 50 g/m² ÷ 50 g/m² per cm = 1 cm). Chains equations? no. Convert: biomass values into the scale's unit (kg/m² ↔ g/m²). Triple, both tiers.
- **Equations that need formula triangles (rule 2):** none (a drawing scale, not a spec equation).
- **Misconceptions to confront:**
  - "Producers go at the top — they come first." — trophic level 1 is at the bottom.
  - "The bar shows how many organisms there are." — it shows total mass; one oak outweighs all its caterpillars.
  - "Just draw each bar a bit smaller." — bars are drawn accurately to a stated scale.
  - "Biomass shrinks because top animals are small." — biomass is lost between levels (faeces; CO₂ and water from respiration; urea in urine).
- **"Start here" access note (rule 1):** one oak tree vs all the caterpillars living on it — which weighs more in total?
- **Practice (rule 4):** q2 usable on TF TH (1). q1 not an exam rung — off-spec numbers comparison (PB-F2). Design tops the bank up to the batch's fixed size, including a construct-from-data item and a "describe / explain why each level is smaller" item.
- **Diagrams:** `05-diagram-library/README.md` row 11 — `pyramid_of_biomass()` covers it; must draw a to-scale pyramid with its scale and units, and the oak/caterpillar contrast.
- **Examiner tip:** none approved.

---

### 12. Transfer of Biomass
`transfer-of-biomass` · Biology / ecology · AQA 8461 4.7.4.3 (biology only); not in 8464 · TF TH

- **Family:** QUANTITATIVE — the efficiency calculation (MS 1c) carries the idea that ~90 % is lost at each step. BATCH-PLAN kept.
- **Flagship (a suggestion, not a spec):** follow 1000 g of grass into a rabbit and split it into faeces, CO₂ + water, urine and new rabbit — then calculate the efficiency.
- **Route layers:** none. Whole lesson is 8461 4.7.4.3 (biology only); the `higher` field is base (TB-F5).
- **Required practical:** none.
- **Calculations:**
  - Efficiency (%) = (biomass at next level ÷ biomass at current level) × 100; also as a fraction (spec). Chains equations? no. Convert: both biomasses to one unit (kg/m² ↔ g/m²). Triple, both tiers.
  - Biomass not transferred = current − next. Chains? no.
  - Across two transfers (grain → beef → human: 10 % × 10 % = 1 %). Chains? **yes** — Step 1: efficiency (or mass) for level 1→2; Step 2: apply to level 2→3. Needs its own Step 1 … Step 2 worked example before practice.
  - Reverse: biomass at next level = efficiency (as decimal) × current biomass. Chains? no; Convert % → decimal.
- **Equations that need formula triangles (rule 2):** Efficiency = biomass transferred ÷ biomass at current level — **Learn it** (no biology sheet). Triangle: top = biomass transferred; bottom = efficiency (decimal) × current biomass. The × 100 (decimal → %) is its own line.
- **Misconceptions to confront:**
  - "10 % of what it eats is passed on." — 10 % of the level's biomass ends up as the next level's biomass, not what's eaten.
  - "Faeces are excreted." — faeces are egested; excretion is urea, water, CO₂.
  - "The lost biomass just disappears as heat." — the mass leaves as CO₂ and water from respiration, faeces and urine.
  - "Divide the bigger number by the smaller." — next level ÷ current level; an answer over 100 % is impossible.
  - "Plants capture all the sunlight." — producers transfer about 1 % of incident light energy.
- **"Start here" access note (rule 1):** you eat a big dinner but don't gain a dinner's weight — where did the rest go?
- **Practice (rule 4):** q2 usable on TF TH (1). q1 **not usable** (TB-F1, false distractor). Design tops the bank up to the batch's fixed size, including a percentage item, a fraction item, a two-step item (after its worked example) and an "explain how biomass is lost" item.
- **Diagrams:** `05-diagram-library/README.md` row 12 — `biomass_flow()` covers the 10 % flow; must draw the three-way loss split (faeces / CO₂ + water / urine) beside it.
- **Examiner tip:** none approved.

---

### 13. Farming Techniques
`farming-techniques` · Biology / ecology (food production) · AQA 8461 4.7.5.2 (biology only); not in 8464 · TF TH

- **Family:** CONTRAST — intensive vs free-range; the one discriminating difference is how much of the food's energy is transferred to the surroundings (movement, keeping warm). BATCH-PLAN kept.
- **Flagship (a suggestion, not a spec):** two chickens fed the same food, one free-range and one in a warm, crowded shed — predict which gains more mass, then weigh the welfare cost.
- **Route layers:** none. Whole lesson is 8461 4.7.5.2 (biology only); the `higher` field's ethics/evaluation is base (FT-F1).
- **Required practical:** none.
- **Calculations:** none required by 4.7.5.2. (Any efficiency figure reuses transfer-of-biomass's equation, already taught there.)
- **Equations that need formula triangles (rule 2):** none.
- **Misconceptions to confront:**
  - "Penned animals grow faster because they're lazy." — less movement means less energy used in respiration, so more becomes body mass.
  - "Keeping animals warm is just kindness." — warmth means less energy spent keeping body temperature up, so more becomes biomass.
  - "More efficient means better in every way." — some people have ethical objections to intensive methods (WS 1.3).
  - "Crowding has no downside." — disease spreads; agricultural antibiotic use should be restricted (resistance).
- **"Start here" access note (rule 1):** after a cold day running around you're starving — does an animal that sits still in the warm need more food or less?
- **Practice (rule 4):** q1 usable on TF TH (1). q2 not an exam rung — biological control is off-spec (FT-F3). Design tops the bank up to the batch's fixed size, including "explain how limiting movement/controlling temperature improves efficiency" and "evaluate intensive farming from given data".
- **Diagrams:** `05-diagram-library/README.md` row 13 — nothing exists; must draw the intensive vs free-range contrast (energy in feed → body mass vs movement + heat).
- **Examiner tip:** none approved.

---

### 14. Sustainable Fisheries
`sustainable-fisheries` · Biology / ecology (food production) · AQA 8461 4.7.5.3 (biology only); not in 8464 · TF TH

- **Family:** SYSTEM — a stock is a breeding system; change one lever (catch, mesh size) and predict whether it recovers or collapses. BATCH-PLAN kept.
- **Flagship (a suggestion, not a spec):** one fish stock over 20 years, with a quota dial and a mesh-size dial — overfish it to collapse, then manage it back.
- **Route layers:** none. Whole lesson is 8461 4.7.5.3 (biology only); the `higher` field's graph interpretation is base (SF-F1).
- **Required practical:** none.
- **Calculations:** none required by 4.7.5.3 (reading stock-over-time graphs, WS 1.4).
- **Equations that need formula triangles (rule 2):** none.
- **Misconceptions to confront:**
  - "The sea is so big we can't run out of fish." — stocks are declining; some species may disappear altogether in some areas.
  - "Big nets with small holes are better." — small mesh catches young fish before they breed, so next year's stock falls.
  - "Quotas are just numbers politicians pick." — set from population estimates so breeding continues.
  - "If you stop fishing for a year the stock is back." — recovery takes as long as the fish take to reach breeding age.
- **"Start here" access note (rule 1):** if you catch every fish in a pond, including the babies, will there be fish there next year?
- **Practice (rule 4):** q1 usable on TF TH (1). q2 not an exam rung — fish farming is off-spec (SF-F2). Design tops the bank up to the batch's fixed size, including a quota item and a "use the graph: explain how this measure helped the stock recover" item.
- **Diagrams:** `05-diagram-library/README.md` row 14 — nothing exists; must draw mesh size letting juveniles through, and a stock-over-time graph marking when a quota began.
- **Examiner tip:** none approved.

---

### 15. The Role of Biotechnology
`role-of-biotechnology` · Biology / ecology (food production) · AQA 8461 4.7.5.4 (biology only); links 8464/8461 4.6.2.4 · TF TH

- **Family:** PROCESS — the spec's spine is two production chains: Fusarium → mycoprotein, GM bacterium → insulin (grow, harvest, purify). BATCH-PLAN kept.
- **Flagship (a suggestion, not a spec):** run a fermenter: add glucose syrup and air, grow Fusarium, harvest and purify — then compare what one tonne of glucose makes as mycoprotein vs as beef.
- **Route layers:** none. Whole lesson is 8461 4.7.5.4 (biology only); GM concerns are base 4.6.2.4 (WS 1.3, 1.4); the `higher` field's evaluation is base (RB-F1).
- **Required practical:** none.
- **Calculations:** none required by 4.7.5.4.
- **Equations that need formula triangles (rule 2):** none.
- **Misconceptions to confront:**
  - "Quorn is made from soya / a plant." — it is the fungus Fusarium.
  - "Microorganisms for food grow by themselves in a tank." — grown on glucose syrup, in aerobic conditions, then harvested and purified.
  - "GM is the same as selective breeding." — GM inserts a gene from another organism; selective breeding only picks parents.
  - "Insulin for diabetics comes from animals." — today it is human insulin made by a GM bacterium, harvested and purified.
  - "GM crops are risk-free / always dangerous." — benefits (yield, golden rice) and concerns (wild flowers, insects, health not fully explored) both stand.
- **"Start here" access note (rule 1):** a meat-free "chicken" nugget — made from a plant, or from something that grows like a mushroom?
- **Practice (rule 4):** q1, q2 usable on TF TH (2). (q2 wx1 slightly overstated — RB-F4; item still usable.) Design tops the bank up to the batch's fixed size, including a mycoprotein-process item, an insulin item and a golden-rice item.
- **Diagrams:** `05-diagram-library/README.md` row 15 — nothing exists; must draw the Fusarium fermenter (glucose syrup in, air in, biomass harvested and purified) and the GM-bacterium → insulin chain.
- **Examiner tip:** none approved.
