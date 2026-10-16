# KS4 batch 10: 15 lessons (ecology)

Written from `docs/ks4/packs/batch-10/` (00-BRIEF.md, FLAGS.md, 04-checked-science-source/, 05-diagram-library/README.md), main, 12 Oct 2026. The V8 prompt’s updates win over the pack. No lesson text comes from old site data: pages don’t load `ks4-source.js`; every quiz item is written into its lesson.

Before this batch: the batch 6 transpiration fix is delivered again as `Design's Output/Batch 6 fix/lessons/ks4-biology-4.2.3.2-transpiration.dc.html` (with the batch-6 blocks so it runs alone); batch 9 is complete in `Design's Output/Batch 9/lessons/`.

## Files and routes

One runnable `.dc.html` per lesson in `Batch 10/lessons/`, named `ks4-biology-<spec>-<slug>` with the 8461 number. Order is the prompt’s.

1. Ecosystems · `ks4-biology-4.7.1.1-ecosystems` · CF CH TF TH
2. Population and competition · `ks4-biology-4.7.1.1-population-competition` · CF CH TF TH
3. Abiotic and biotic factors · `ks4-biology-4.7.1.2-abiotic-biotic-factors` · CF CH TF TH
4. Adaptations · `ks4-biology-4.7.1.4-adaptations` · CF CH TF TH
5. Food chains and food webs · `ks4-biology-4.7.2.1-food-chains-webs` · CF CH TF TH · Triple layer (trophic levels, 10%)
6. Sampling techniques · `ks4-biology-4.7.2.1-sampling-techniques` · CF CH TF TH · RP7/RP9 · calculates · Triple line (continuous belt transect)
7. The impact of environmental change · `ks4-biology-4.7.2.4-environmental-change` · **TH only** (the picker offers only Triple Higher)
8. Deforestation · `ks4-biology-4.7.3.4-deforestation` · CF CH TF TH
9. Maintaining biodiversity · `ks4-biology-4.7.3.6-maintaining-biodiversity` · CF CH TF TH
10. Trophic levels · `ks4-biology-4.7.4.1-trophic-levels` · TF TH
11. Pyramids of biomass · `ks4-biology-4.7.4.2-pyramids-of-biomass` · TF TH · calculates (drawing scale)
12. Transfer of biomass · `ks4-biology-4.7.4.3-transfer-of-biomass` · TF TH · calculates
13. Farming techniques · `ks4-biology-4.7.5.2-farming-techniques` · TF TH
14. Sustainable fisheries · `ks4-biology-4.7.5.3-sustainable-fisheries` · TF TH
15. The role of biotechnology · `ks4-biology-4.7.5.4-role-of-biotechnology` · TF TH

Triple-only pages (10–15) offer only TF and TH in the picker, as monoclonal antibodies did in batch 7. Lesson 7 offers only TH. Prev/next skip pages a route doesn’t have: on Combined, Sampling techniques → Deforestation, and Maintaining biodiversity has no Next; on Triple Foundation, Sampling techniques → Deforestation; on Triple Higher the full order. No Higher badge appears anywhere in the batch: every `higher` field was ruled base or off-spec (ECO-F1, PC-F1, ABF-F1, SAMP-F4, TL-F1, PB-F1, TB-F5, FT-F1, SF-F1, RB-F1).

## Page order (every lesson)

Header (AQA ref, route chips, route picker) → Start here (`Ks4Guess`) → video slot → two to four teaching sections, each with a figure and an interaction → on the calculating lessons: equation block with `Ks4Triangle`, CFIFA (`Ks4Cfifa`), then Step 1 / Step 2 (`Ks4Steps`, worked then attempt) → Think again (`Ks4Choice`) → Sort (`Ks4Sort`) → command words → key fact → exam ladder (`Ks4Practice`) → key note → practice set (`Ks4QuizBank`) → end. No examiner tips: none approved.

## Shared blocks

Copied unchanged from the batch-9 delivery into `lessons/`: Ks4Triangle, Ks4Guess, Ks4Steps, Ks4Practice, Ks4Chain, Ks4Write, Ks4Chrome, Ks4Cfifa, Ks4Choice, Ks4Sort, Ks4KeyNote, Ks4QuizBank, Ks4End, Ks4Video, ks4-lib.js, ks4-diagrams.js, ks4-theme.css, support.js. No `_ds` inside; pages link `../../_ds/…`.

No block changes this batch. New page-level patterns (not blocks): a per-item classifier (a row of type buttons under each feature, used for adaptations, harms/helps, trophic levels, pyramid bar widths), a two-lever graph (fisheries), and a two-date range map (environmental change). The page helpers (`seg`, `btns`, `cards`, `pick`, `stepper`, `multi`, `flags`, `common`) are identical on every page; `common` now filters ORDER by a route code (0 all, 1 Triple, 2 Triple Higher).

## Rules 1–4

- **Rule 1.** Every opener is “If you had to guess, …?” with exactly two options, built on the brief’s access note: bees vanishing from a park; two seedlings in one pot; sunny field or dark wood; a polar bear in a desert; foxes gone from a field; counting every daisy; an earlier spring; forest to ranch; hedges pulled out; grass, rabbit, fox; one oak and its caterpillars; a big dinner; a cold day and a warm, still animal; emptying a pond; a meat-free nugget. Titles, scenes and big questions don’t give the answer away. The wrong option’s reply is encouraging and leads into the teaching.
- **Rule 2.** Formula triangles on the two biology equations: population = mean per m² × habitat area (sampling), and efficiency = biomass at the next level ÷ biomass at this level (transfer). Both use `source: 'none'`, so the panel reads “Written out” with no chip. “Learn this one” and “Learn it” appear nowhere. The extra lines (mean per m² = mean per quadrat ÷ quadrat area; 50 cm → 0.25 m²; efficiency % = decimal × 100) are their own boxes under the triangle. Pyramids of biomass has no triangle: bar width = biomass ÷ scale value is taught as a step with a worked example.
- **Rule 3.** Every step is taught before it is tested:
  - Sampling: random coordinates taught in a gated stepper; mean, mode and median taught on one made-up table with two picks before any calculation; the triangle; CFIFA with two worked examples (1 m² quadrat, then a 50 cm quadrat with the cm → m conversion as the Convert line) and two attempts; then Ks4Steps worked Step 1 (mean per quadrat) / Step 2 (scale up), then the attempt with a 50 cm quadrat. The ladder’s two calc items repeat both cases.
  - Transfer: losses taught, then the triangle with the × 100 line, then CFIFA (the pack’s FIFA verbatim with its examined Convert line; a kg → g example; a fraction example) and three attempts (one reverse: next level = efficiency × this level); then Ks4Steps worked two-transfer chain (grain → beef → people, 10% × 10% = 1%) and an attempt (algae → small fish → large fish, 8% × 10% = 0.8%). “Divide the bigger by the smaller” is faced in the equation block, the Think again, Question 1’s close and the attempt’s close: over 100% is impossible.
  - Pyramids: the scale step is worked (1 cm = 40 g/m² → 10, 2, 0.4 cm) with the kg → g conversion, before the pupil picks three bar widths and watches the pyramid draw.
  - CFIFA on every calculation, in Ks4Cfifa, Ks4Steps and the ladder’s calc items.
- **Rule 4.** Ladder 2 · 2 · 2 · 1 on every page and route; rung 4 is one 4- or 6-mark answer (6 on lessons 6, 7, 8, 9, 12, 13, 14, 15; 4 elsewhere). Practice set: five per route on every page. Food chains is the only page whose bank differs by route (TF TH get q1; CF CH get a secondary-consumer item instead); the ladder is the same on all routes everywhere.

## Quiz items (practice set, five per route)

“Rebuilt” = same stem, options and key, with FLAGS’ corrected explanations. Options are shuffled by `KS4.item()`.

- 1 Ecosystems: q1 q2 q3 verbatim + 2 new (what the rock-pool crabs compete for; dragonfly-larvae data).
- 2 Population and competition: q1 verbatim; q2 verbatim (the page glosses the terms as “within a species” / “between species”, PC-F3) + 3 new (lag from a graph, pondweed compete-for, what limits a population).
- 3 Abiotic and biotic: q1 q2 verbatim + 3 new (pond temperature/oxygen data, leaning trees and wind direction, ash fungus as a new pathogen).
- 4 Adaptations: q1 q2 verbatim + 3 new (extremophiles, antifreeze fish from given information, musk ox SA:V).
- 5 Food chains: CF CH q2 + 4 new (reversed arrows, algae as producer, shrews gone → owls, which is the secondary consumer); TF TH q1 q2 + 3 new (the first three).
- 6 Sampling: q1 q3 verbatim + 3 new (mode and median, transect against light, 50 cm quadrat area). q2 not used (SAMP-F1).
- 7 Environmental change: q2 verbatim + 4 new given-information items (mayfly larvae with the oxygen fact given, mountain plant range, oak–caterpillar–bird timing, which change is atmospheric gases). q1 not used (ENV-F2).
- 8 Deforestation: q1 q2 rebuilt (DEF-F1, DEF-F2 explanations) + 3 new (reason, biodiversity, benefit and cost).
- 9 Maintaining biodiversity: q1 q2 rebuilt (MB-F1, MB-F2 explanations) + 3 new (nature-reserve data evaluation, recycling, negative interaction).
- 10 Trophic levels: q1 q2 verbatim + 3 new (which level, decomposer enzymes, apex predator).
- 11 Pyramids: q2 verbatim + 4 new (construct from data, kg → g bar width, level 1 at the bottom, describe and explain). q1 not used (PB-F2).
- 12 Transfer: q2 verbatim + a replacement efficiency item whose inverted distractor prints 1000% (TB-F1) + 3 new (fraction, two-step, how biomass is lost). q1 not used.
- 13 Farming: q1 verbatim + 4 new (temperature, high-protein feed, cattle data evaluation, antibiotics). q2 not used (FT-F3).
- 14 Fisheries: q1 verbatim + 4 new (what a quota is, stock-graph data, why collapse, why recovery is slow). q2 not used (SF-F2).
- 15 Biotechnology: q1 q2 verbatim + 3 new (mycoprotein process, insulin, golden rice).

## Science flags

**G · Global**
- G1. Subscripts: CO₂ appears in figures as text and renders in the figure font (checked in the transfer-of-biomass split figure and the deforestation chain). Body text writes “carbon dioxide” in words. No CH₄ or H₂O appears.
- G2. Glyphs: JS-built text (quiz, ladder, sort) falls back to a system font for “→” and “≤”; my new text avoids them, verbatim items keep theirs.
- G3. Made-up teaching data, labelled on each page: the wood after the wolves, the hares and lynx, the stream and hedge readings, the quadrat counts and light readings, the hedge brown butterfly and its map, the river flow, the biofuel plan, the hedgerow scheme, the biomass tables, the chicken shed and free-range figures, the cod stock.
- G4. One job per spec point; siblings get a pointer: competition → Population and competition (from Ecosystems, ECO-F5); measuring light and counting along a line → Sampling (from Abiotic and biotic); SA:V calculation → Transport in cells (from Adaptations); trophic levels and the 10% → Trophic levels and Transfer of biomass (from Food chains, one Triple preview block); the three losses and the efficiency calculation → Transfer of biomass (from Trophic levels, Pyramids, Farming); biodiversity programmes → Maintaining biodiversity (from Deforestation); how the gene is moved → Genetic engineering (from Biotechnology). Deforestation and Environmental change each stay on their own spec sentence; Maintaining biodiversity teaches the five programmes and the trade-off only.
- G5. Every figure is mine, in the ks4-diagrams style; nothing was ported from `figlib` or `ks3_art`. The diagram README’s “still needed” list is followed except where FLAGS disagree: no indicator-species figure (ENV-F1); no pyramid of numbers (PB-F2).
- G6. Off-spec detail in the sources left out: cascade effect as a term, productivity, nature reserves as artificial ecosystems (ECO-F2); exponential growth, carrying capacity, density dependence (PC-F2); indicator species (ABF-F1, ENV-F1); parasitism; keystone species; mark-recapture (SAMP-F1); line transects; phenology, extirpation, gene flow (ENV-F5); coral bleaching and sea level; pyramids of numbers and energy, inverted pyramids (PB-F2); the 60–70% / 20–30% split (TB-F4); biological control and crop methods (FT-F3), antibiotics as growth promoters (FT-F4), battery cages and veal crates (FT-F5), eutrophication (FT-F6); fish farming, exclusion zones, closed seasons (SF-F2); Bt crops and herbicide-tolerant crops as taught content, patents, labelling (RB).
- G7. Links to earlier batches use `../../KS4 Batch 4/…`, `../../Batch 6/lessons/…`, `../../Batch 7/lessons/…`, `../../Batch 9/lessons/…`. Code to re-point: Batch 4 Biodiversity, Batch 9 Evolution and natural selection, and batch-2 Carbon cycle forward-link to pages that now exist (Maintaining biodiversity, Adaptations, Deforestation).

**1 · Ecosystems**
- 1.1 The data skill (“explain how a change … affects a community, using data”) is taught on all four routes; nothing badged Higher; the inputs/outputs sentence dropped (ECO-F1).
- 1.2 Definitions are the spec’s: ecosystem “the interaction of a community of living organisms (biotic) with the non-living (abiotic) parts of their environment”; stable community “all the species and environmental factors are in balance so that population sizes remain fairly constant” (ECO-F3).
- 1.3 q3 (farmland monoculture) kept; nature reserves and productivity not taught (ECO-F2). q2 used verbatim (ECO-F4).
- 1.4 Competition pointed to Population and competition, with one compete-for item in the bank as the brief asks (ECO-F5).
- 1.5 The web (leaf litter, earthworms, shrews; grass and shrubs, deer, wolves; flowering plants, bees) is mine; the bee dependence is pollination, not feeding.

**2 · Population and competition**
- 2.1 Predator–prey graph reading and the lag taught on all four routes; nothing badged Higher (PC-F1).
- 2.2 Carrying capacity, exponential growth and density terms cut; “what limits a population” re-cut as food, water, space, predators, disease (PC-F2, PC-F4).
- 2.3 Intraspecific / interspecific never appear as vocabulary; the page says “within a species” and “between species” in brackets so q2 is answerable (PC-F3). Code may prefer to drop q2 and the gloss; the replacement would be a second compete-for item.
- 2.4 The spec’s two lists verbatim (light and space; water and mineral ions from the soil; food, mates and territory), with a “given this habitat, suggest” pick, bank item and ladder item (PC-F5).
- 2.5 The hare–lynx curves are sine waves with a 1.5-year lag, labelled made up; year notes say “about a year and a half”.

**3 · Abiotic and biotic factors**
- 3.1 Indicator species dropped entirely; the data skill taught on all four routes; nothing badged Higher (ABF-F1, ABF-F2). The pond and stream examples are oxygen examples without the indicator label.
- 3.2 The spec’s seven abiotic and four biotic factors word for word, including “wind intensity and direction” and “so the numbers are no longer sufficient to breed” (ABF-F3).
- 3.3 “Animals whose body temperature follows their surroundings”; heather on acidic soil only; no nettles, no limpets (ABF-F4).
- 3.4 The rocky shore isn’t used.

**4 · Adaptations**
- 4.1 Extremophiles taught in the spec’s sentence on all four routes, with a pick, a bank item and a ladder item (AD-F1).
- 4.2 “Small surface area compared with its volume” throughout; never “small surface area” alone (AD-F2).
- 4.3 The sorter uses clean examples only: fur, blubber, cactus spines; nocturnal, migrating, herding; antifreeze proteins, concentrated urine (AD-F3). The fox feature-classifier avoids bioluminescence and hibernation; reduced blood flow to the paws is the Arctic fox’s functional example: Code to check.
- 4.4 Natural selection is a pointer to batch 9; the Think again confronts “grew big ears because it was hot”.

**5 · Food chains and food webs**
- 5.1 “Trophic level”, the 10% and short chains sit in one Triple-only preview block with pointers; absent on CF and CH (FCW-F1). q1 on TF TH only.
- 5.2 Pyramids and efficiency not shown on any route here; no pyramids of number (FCW-F2).
- 5.3 Losses in the Triple block use the spec’s substances, “egested”, and never “heat” for biomass (FCW-F3, FCW-F4).
- 5.4 “Green plant or alga” (FCW-F5). q2 verbatim (FCW-F6).
- 5.5 The field web (grass; rabbits, grasshoppers; foxes, shrews; owls) is mine.

**6 · Sampling techniques**
- 6.1 Mark-recapture not taught, not in the bank; the FIFA, equation and variables not used (SAMP-F1). The lesson’s worked examples are quadrat scale-ups, one with nothing to convert and one with a 50 cm quadrat.
- 6.2 Labelled “Required practical 7 (Combined) / 9 (Biology)” throughout; both halves taught (SAMP-F2).
- 6.3 Throwing the quadrat is confronted as not random and unsafe; random coordinates from two tapes taught on all four routes; nothing badged Higher (SAMP-F3, SAMP-F4).
- 6.4 Mean, mode and median on one table (1, 2, 2, 2, 3, 4, 5, 6, 7, 8: mean 4, mode 2, median 3.5); plotting is a stated step with a “plot daisies against distance or light” note; distribution vs abundance is a pick and the Sort (SAMP-F5).
- 6.5 “Interrupted belt transect” named; continuous belt transect is one Triple-only line (SAMP-F6).
- 6.6 The equation is written as population = mean per m² × habitat area, with mean per m² = mean per quadrat ÷ quadrat area as its own line; the brief’s form (mean × habitat area ÷ quadrat area) is the same calculation. Code to check the preferred wording.

**7 · The impact of environmental change**
- 7.1 TH only; AQA number 4.7.2.4 in the header (the site’s “4.7.4” not used).
- 7.2 Indicator species not taught; the page says a species fact may be given in a question and the mayfly bank item gives it in the stem (ENV-F1, ENV-F2).
- 7.3 The lake chain is the full one: algae block light → plants die → bacteria decompose and respire → oxygen falls → fish die; “eutrophication” not used (ENV-F3).
- 7.4 Leads with the three named changes and three causes; every evaluation is from given data with “what else could explain it” and “what would strengthen it” (ENV-F4).
- 7.5 Extirpation, phenology and gene flow not used (ENV-F5). The Think again confronts “evolved in 50 years”.
- 7.6 The hedge brown butterfly, its map, and the river are made up and say so.

**8 · Deforestation**
- 8.1 q1 and q2 rebuilt with FLAGS’ re-matched explanations (DEF-F1, DEF-F2).
- 8.2 The weigh-up taught on every route (gains: food, fuel; costs: carbon dioxide, biodiversity) with a judgement pick, a bank item asking for a benefit and a cost, and the 6-mark rung (DEF-F3).
- 8.3 Both carbon dioxide reasons are a two-select check (“select both”); decay is always “microorganisms respire”.

**9 · Maintaining biodiversity**
- 9.1 q1 and q2 rebuilt with FLAGS’ re-matched explanations (MB-F1, MB-F2).
- 9.2 Negative and positive interactions taught as a harms/helps classifier on every route; a given-data evaluation (hedgerow scheme: 9 → 17 bird species, 400 → 372 tonnes, £18 000 half paid) as a pick, the bank and the 6-mark rung (MB-F3).
- 9.3 The five programmes in the spec’s words. “Ecosystem services” not used.

**10 · Trophic levels**
- 10.1 Nothing badged Higher; efficiency and food production left to their lessons (TL-F1).
- 10.2 The decomposer mechanism in the spec’s words, as a gated stepper and figure (TL-F2).
- 10.3 The 10% preview is in biomass, one line, with a pointer (TL-F3). q2’s “energy” wording kept verbatim.
- 10.4 Levels numbered “according to how far the organism is along the food chain”; the fox-in-two-chains example shows the number follows the chain (TL-F4).

**11 · Pyramids of biomass**
- 11.1 Construction taught and practised on TF and TH; nothing badged Higher (PB-F1).
- 11.2 No pyramids of numbers or energy, no inverted pyramids; the oak hook is kept as context only; q1 not used (PB-F2, PB-F5).
- 11.3 Data chosen to fit one scale with ratios of 0.2: grassland 400 / 80 / 16 g/m²; woodland 0.8 kg/m² / 160 / 40 g/m²; units on every value (PB-F3).
- 11.4 The three losses in the spec’s words wherever the shape is explained (PB-F4).

**12 · Transfer of biomass**
- 12.1 q1 not used; the replacement item’s inverted distractor prints 1000% (TB-F1).
- 12.2 “Egested as faeces” throughout; excretion kept for carbon dioxide, water and urea; the Sort is egested vs excreted (TB-F2).
- 12.3 Exactly three losses; heat never named as a biomass loss; movement not a separate loss (TB-F3). The split figure says it is illustrative and varies (TB-F4).
- 12.4 Everything on TF and TH (TB-F5). The 1% of incident light, efficiency as a fraction, and the effect on numbers at each level are all taught (TB-F6).
- 12.5 The pack’s FIFA is the first CFIFA example verbatim, including its examined Convert line.

**13 · Farming techniques**
- 13.1 Ethics and evaluation on TF and TH; nothing badged Higher (FT-F1).
- 13.2 Biological control, crop methods and the “no pesticide resistance” claim not used; q2 not used (FT-F2, FT-F3).
- 13.3 Antibiotics appear only as a disadvantage: crowding → disease → antibiotic use → resistance, “agricultural use should be restricted” (FT-F4).
- 13.4 Welfare example is high-density indoor sheds; no battery cages, veal crates or sow stalls (FT-F5). Eutrophication and organic farming not used (FT-F6).
- 13.5 The chicken figures (2.0 kg vs 1.3 kg per 4 kg feed, 20 vs 1 birds per m², £3 vs £6) are made up.

**14 · Sustainable fisheries**
- 14.1 Stock-recovery graphs on TF and TH; nothing badged Higher (SF-F1).
- 14.2 Fish farming, exclusion zones and seasonal bans not used; q2 not used (SF-F2).
- 14.3 “Fish is an important source of protein for billions of people” (SF-F3).
- 14.4 Quotas “agreed between countries each year on scientific advice”; no CFP (SF-F4).
- 14.5 The two-lever graph is a simple growth-minus-catch model, labelled made up; the cod stock table is made up.

**15 · The role of biotechnology**
- 15.1 Evaluation on TF and TH; nothing badged Higher (RB-F1).
- 15.2 Both chains in the spec’s words: Fusarium, glucose syrup, aerobic conditions, harvested and purified, suitable for vegetarians; GM bacterium, human insulin, harvested and purified, treats diabetes (RB-F2).
- 15.3 Concerns in the spec’s words, “wild flowers and insects” (RB-F3). q2 used verbatim; its first clause isn’t repeated in teaching (RB-F4).
- 15.4 Mycoprotein and GM crops kept apart; the Sort has three bins (RB-F5).
- 15.5 Micropropagation isn’t taught here (it is Cloning, batch 9).

## Not done / for Code

- Videos: `KS4.VIDEOS` is empty, so the slot stays hidden.
- No examiner tips: none approved.
- Links to batches 4, 6, 7 and 9 use relative paths as above.
- Dark mode uses the existing remap; SVG plates stay cream.
