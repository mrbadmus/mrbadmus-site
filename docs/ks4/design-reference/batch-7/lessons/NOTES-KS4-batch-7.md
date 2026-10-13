# KS4 batch 7: 16 lessons

Written from `docs/ks4/packs/batch-7/` (00-BRIEF.md, FLAGS.md, 04-checked-science-source/, 05-diagram-library/README.md), main, 5 Oct 2026. The V5 prompt's updates override the pack. No lesson text comes from old site data: these pages don't load `ks4-source.js`; every quiz item is written into its lesson.

Also this turn: Batch 6 transpiration now calculates (rate, mean, volume chain). See 13.3 in `Batch 6/lessons/NOTES-KS4-batch-6.md`.

## Files and routes

One runnable `.dc.html` per lesson in `Batch 7/lessons/`, named `ks4-biology-<spec>-<slug>` with the true AQA reference from the brief and FLAGS. Order is the prompt's.

1. Communicable diseases and defences · `ks4-biology-4.3.1.1-communicable-diseases-defence` · CF CH TF TH
2. Viral diseases · `ks4-biology-4.3.1.2-viral-diseases` · CF CH TF TH
3. Bacterial diseases · `ks4-biology-4.3.1.3-bacterial-diseases` · CF CH TF TH
4. Fungal and protist diseases · `ks4-biology-4.3.1.4-fungal-protist-diseases` · CF CH TF TH
5. Vaccination · `ks4-biology-4.3.1.7-vaccination` · CF CH TF TH
6. Antibiotics and painkillers · `ks4-biology-4.3.1.8-antibiotics-painkillers` · CF CH TF TH
7. Drug discovery and development · `ks4-biology-4.3.1.9-drug-discovery-development` · CF CH TF TH
8. Monoclonal antibodies · `ks4-biology-4.3.2.1-monoclonal-antibodies` · TH only
9. Plant disease and defences · `ks4-biology-4.3.3.1-plant-disease-detection-defence` · TF TH · Higher layer TH
10. Photosynthesis · `ks4-biology-4.4.1.1-photosynthesis` · CF CH TF TH
11. Rate of photosynthesis · `ks4-biology-4.4.1.2-rate-of-photosynthesis` · CF CH TF TH · RP5 (Combined) / RP6 (Biology) · calculates · Higher layer CH TH
12. Uses of glucose · `ks4-biology-4.4.1.3-uses-of-glucose` · CF CH TF TH
13. Aerobic respiration · `ks4-biology-4.4.2.1-aerobic-respiration` · CF CH TF TH
14. Anaerobic respiration · `ks4-biology-4.4.2.1-anaerobic-respiration` · CF CH TF TH
15. Response to exercise · `ks4-biology-4.4.2.2-response-to-exercise` · CF CH TF TH · Higher layer CH TH
16. Metabolism · `ks4-biology-4.4.2.3-metabolism` · CF CH TF TH · Higher (CH TH), Triple (TF TH) and Triple Higher (TH) layers

Aerobic and anaerobic respiration share 4.4.2.1, so the slug tells them apart. The monoclonal page has one route, so it shows "Triple Higher only" and no picker; plant disease offers the two Triple routes.

## Page order (every lesson)

Header (AQA ref, route chips, RP badge where there is one, route picker) → Start here (`Ks4Guess`) → video slot → two teaching sections (three on vaccination, monoclonal antibodies and rate of photosynthesis), each with a figure and one interaction, route layers as `sc-if` → equation block (`Ks4Triangle`) and CFIFA (`Ks4Cfifa`) on rate of photosynthesis only → Think again (`Ks4Choice`) → Sort (`Ks4Sort`) → command words → key fact → exam ladder (`Ks4Practice`) → key note → practice set (`Ks4QuizBank`) → end. No examiner tips: none approved.

## Shared blocks

Copied from the batch-6 delivery into `lessons/` so each page runs on its own: Ks4Triangle, Ks4Guess, Ks4Steps, Ks4Practice, Ks4Chain, Ks4Write, Ks4Chrome, Ks4Cfifa, Ks4Choice, Ks4Sort, Ks4KeyNote, Ks4QuizBank, Ks4End, Ks4Video, ks4-lib.js, ks4-diagrams.js, ks4-theme.css, support.js. No `_ds` inside; pages link `../../_ds/…`.

One change: **Ks4Triangle** now accepts `fixed: true` on the top item as well as on a bottom item. It is used once, for the 1 in light intensity = 1 ÷ d²: greyed, can't be picked, read as "one, a fixed number". Bottom-item behaviour and every earlier equation are unchanged. Ks4Steps is copied but unused this batch (no chained calculation).

The 16 pages share one page shell (header, Start here, Think again, Sort, command words, key fact, ladder, key note, bank, end) and the same few logic helpers (route, rail, button and card state) written into each file, so each page still runs alone.

## Rules 1–4

- **Rule 1.** Every opener is "If you had to guess, …?" with two options from everyday life (germs on hands, catching measles, a pink chicken burger, a mosquito bite, chickenpox once, paracetamol for a fever, who tries a new medicine first, a pregnancy test, a yellowing houseplant, a plant in a dark cupboard, a windowsill basil, a potato, getting out of breath, a sprint and rising dough, running for a bus, how much food you eat). Titles and scenes set up the situation without the answer. The monoclonal opener is a lateral-flow question that reads as a fair adult guess. On plant disease both options are marked right (yellowing can be either) and the reply says how to tell.
- **Rule 2.** Two triangles, both on rate of photosynthesis, `source: 'none'`, "Written out", no chip: rate = amount of oxygen ÷ time (A over R × t); (Higher) light intensity = 1 ÷ d² (1 over L × d², 1 fixed, square-root extra line on d). Each sits in the equation block and under the Formula step of every worked CFIFA example. No other lesson has a calculation or a triangle, per each pack entry. Word equations (photosynthesis, respiration) are written out, not triangles. "Learn this one" appears nowhere.
- **Rule 3.** Rate: s ↔ min taught in the equation block; worked "nothing to convert" then "convert first" before either attempt. Inverse square (Higher): "both distances in the same unit" taught first; worked same-unit then convert-first; one line per distance then a comparison line; then two attempts; all before the ladder. No chained calculation in this batch, so no Step 1 / Step 2. Every calculation is CFIFA.
- **Rule 4.** Ladder 2 · 2 · 2 · 1 on every page and route (checked by script on all 61 page–route pairs); rung 4 is one 4- or 6-mark answer. Practice set: five questions per route. Where a layer swaps items (plant disease TH, rate CH TH, exercise CH TH, metabolism CH and TH), the count stays the same.

## Quiz items (practice set, five per route)

- 1 Communicable: q1–q4 verbatim; 1 new (antitoxins)
- 2 Viral: q1–q3 verbatim; 2 new (TMV spread, HIV first sign)
- 3 Bacterial: q1 verbatim; q2 rebuilt (F1); 3 new (toxins, condoms, poultry vaccination)
- 4 Fungal and protist: q1 q2 verbatim; 3 new (black spot treatment, malaria pathogen type, malaria control)
- 5 Vaccination: q1–q3 verbatim; 2 new (what a vaccine contains, cases-graph conclusion)
- 6 Antibiotics: q1 q2 verbatim; 3 new (painkillers, antivirals, slowing resistance)
- 7 Drug discovery: q1–q3 verbatim; 2 new (digitalis, peer review)
- 8 Monoclonal: q1 q2 verbatim; q3 rebuilt (F1); 2 new (fluorescent dye, side effects)
- 9 Plant disease: q1 q2 verbatim; 3 new (magnesium, nitrate, mechanical; TH swaps mechanical for testing kits)
- 10 Photosynthesis: q1 q3 q4 verbatim; 2 new (endothermic, glucose symbol)
- 11 Rate: CF TF q3 verbatim, q2 rebuilt (F1), 3 new (chlorophyll, rate calculation, one-factor graph); CH TH q1 q3 verbatim, 3 new (chlorophyll, rate calculation, inverse square)
- 12 Uses of glucose: q1 rebuilt (F1); q2 q3 verbatim; 2 new (cellulose, oils)
- 13 Aerobic: q1 q2 verbatim; 3 new (exothermic, energy uses, mitochondria number); q3 not used
- 14 Anaerobic: q1–q3 verbatim; 2 new (energy per glucose, replacing q4; plant roots)
- 15 Exercise: CF TF q1 verbatim + 4 new; CH TH q1–q3 verbatim + 2 new
- 16 Metabolism: CF TF q1 q3 verbatim + 3 new (amino acids, lipid, energy); CH swaps energy for thyroxine; TH q1 q2 q3 verbatim + 2 new (amino acids, thyroxine)

Options are shuffled by `KS4.item()`, as before. "Rebuilt" = same stem and key, with the flagged option or explanation replaced by FLAGS' wording.

## Science flags

**G · Global**
- G1. Arrows, subscripts and superscripts inside JS-built text (quiz, ladder, sort, key note) are plain characters and fall back to a system font, as in batches 5–6. In template markup, arrows are inline SVG and superscripts use `<sup>`. Verbatim items keep their own glyphs.
- G2. Teaching data are made-up and labelled on each page: vaccination cases graph and 25-person grid, RP bubble counts, limiting-factor curves, greenhouse costs, heart- and breathing-rate curves.
- G3. Prev/next follow this batch's order. Lesson 1 points back to Translocation (batch 6). Combined-route pupils on drug discovery meet a Triple Higher neighbour (monoclonal), and photosynthesis's back link is Triple-only (plant disease); both are labelled. Earlier-batch links use `../../Batch 4|5|6/lessons/…` as the prompt says; in this project batches 4 and 5 still sit at `KS4 Batch 4/` and `KS4 Batch 5/`, so the two links to them (Plant tissues, Heart and blood vessels) resolve only in Code's layout.
- G4. Drawings are mine in the ks4-diagrams style; `figlib/charts.py line_graph()` is Python and wasn't ported. FLAGS win over the diagram README where they disagree (no clotting box; temperature curve without a plateau; no hypersensitive response).
- G5. Sibling overlap, pointers not re-teaching: memory/fast response → Vaccination; named diseases → the three disease pages; why antibiotics don't kill viruses → Antibiotics; how a resistant strain takes over → Bacterial diseases; how to slow resistance → Antibiotics; plant chemicals as medicines → Drug discovery; RP → Rate of photosynthesis; why starch → Uses of glucose; aerobic vs anaerobic compare → Anaerobic; lactic acid afterwards → Response to exercise; translocation, food tests, culturing (RP2) → batch 6 links.
- G6. Mide's bar: two teaching sections per page, three where the spec point has three distinct parts. Off-spec detail in the sources (ATP numbers, B-cells, schedules, Koplik's spots, SAR, EPOC, anabolism labels) is left out of my text throughout.

**1 · Communicable diseases and defences**
- 1.1 Badge 4.3.1.1 · 4.3.1.6. No Higher layer on any route; the source `higher` (memory B-cells, plasma cells) is not shown (F1). Memory cells stay as a one-line pointer to Vaccination, and in verbatim q2.
- 1.2 Antitoxins taught with phagocytosis and antibodies, and in the sort, rung 1 and a new bank item (F2).
- 1.3 Reducing spread (F3): each route maps to the control that breaks it (air: cover, isolate; water: treat; contact: hygiene, condoms, remove infected plants; vector: control vectors, nets). Vaccination is a pointer.
- 1.4 Re-cuts (F4): TMV is the plant direct-contact example; stomach acid "kills most pathogens". No clotting box.
- 1.5 Barrier sites are the spec's four: skin, nose, trachea and bronchi, stomach. "The nose traps particles" is my spec-level wording; no nose hairs or goblet cells.
- 1.6 Named diseases are one-line examples only (measles, cholera, gonorrhoea, TMV, malaria); each is taught in its own lesson.

**2 · Viral diseases**
- 2.1 HIV sequence opens with the flu-like illness (F1); AIDS in the spec's words, "other infections or cancers" (F2).
- 2.2 TMV spreads by contact: plant to plant, hands and tools. No insects anywhere (F3). Control shown as "remove infected plants".
- 2.3 "Often destroying the host cell" (F4). No paramyxovirus, Koplik's spots, CD4 cells or dose schedules.
- 2.4 Clue game fills a disease grid row on the first correct clue for that disease. "Most young children are vaccinated" is the measles control; MMR not named.
- 2.5 Antibiotics and viruses: in the sort and verbatim q3 only; the reason is a pointer to Antibiotics and painkillers.

**3 · Bacterial diseases**
- 3.1 Penicillin named in the gonorrhoea line (F2). Spec wording throughout: food or food prepared in unhygienic conditions; UK poultry vaccinated; bacteria and the toxins they secrete; thick yellow or green discharge, pain on urinating; antibiotics and condoms.
- 3.2 Bank q2 rebuilt per F1: same stem, key and two distractors; option 3 is now "The antibiotic makes the bacteria mutate", with a new wx2.
- 3.3 Resistance by selection is taught here as the penicillin story (4 steps, 8464 4.6.3.4 / 8461 4.6.3.7 wording). How to slow resistance is left to Antibiotics and painkillers (pointer). The two lessons share the mechanism; Antibiotics points back here rather than re-teaching it.
- 3.4 Contrast figure: spread, symptoms, control for each. Salmonella "symptoms 12–72 hours", Neisseria, PID and complications not used.

**4 · Fungal and protist diseases**
- 4.1 Badge 4.3.1.4–4.3.1.5 (F2).
- 4.2 Malaria cycle has a stage inside the mosquito, "the protist develops inside the mosquito" (F1). No Plasmodium species, liver stage or red-cell cycle; "Plasmodium" appears only in verbatim items.
- 4.3 Control in spec words: stop vectors breeding; nets. Black spot: fungicides and/or remove and destroy affected leaves.
- 4.4 Figures schematic; the rose stem drops two leaves at stage 3.

**5 · Vaccination**
- 5.1 Badge 4.3.1.7, not 4.3.2. No Higher badge; the herd-immunity threshold ("about 95%" for measles, from the source) and a before/after cases graph are base on all four routes (F1). No mRNA sentence.
- 5.2 Vaccines are taught only as the spec type, "small quantities of dead or inactive forms of a pathogen"; "can't cause the disease" is tied to that type, and the sort says so (F3). No attenuated or antigen-only types. No schedule ages; MMR not named (F2).
- 5.3 "Memory cells" are not in my text (the spec says white blood cells "respond quickly"); verbatim q1 and q2 keep the term. No primary/secondary curve labels; the figure compares unvaccinated and vaccinated antibody curves, with an "ill" band.
- 5.4 Flu line: "the flu virus changes, so a new vaccine is made each year." Nothing claims flu vaccines are never live (F4); verbatim q3's wx2 is as F4 allows.
- 5.5 The cases graph (800 a year falling to 40 after year 5) and the 25-person grid are made-up teaching data, labelled. The data reveal notes other factors could play a part (WS 1.4).

**6 · Antibiotics and painkillers**
- 6.1 Badge 4.3.1.8. No Higher badge (F1). "Greatly reduced deaths ... however ... great concern" taught together (F2).
- 6.2 Three ways to slow resistance, equal weight, spec words (F3); "population of the resistant strain rises" lives in Bacterial diseases. No growth promoters. MRSA named. "New antibiotics costly and slow" added from 4.6.3.4.
- 6.3 Antibiotics fail on viruses because there is nothing in a virus for them to kill: taught via verbatim q1 and the sorter. "Difficult to develop drugs that kill viruses without damaging the body's tissues" is the antiviral line (F4). Antiviral examples (Tamiflu) not used.
- 6.4 Selection mechanism is a pointer to Bacterial diseases (G5). RP2 (antibiotics on agar) is a connects link to Culturing microorganisms (Triple).
- 6.5 Paracetamol is the hook's and sort's example painkiller (source names it; spec doesn't).

**7 · Drug discovery and development**
- 7.1 Badge 4.3.1.9. Digitalis/foxgloves, aspirin/willow, penicillin/Fleming/Penicillium in spec words, every route (F1). "Synthesised by chemists ... starting point may still be a plant chemical" (F2). No morphine, quinine or computer models.
- 7.2 Toxicity, efficacy, dose named; preclinical = cells, tissues, live animals (F2). Phase 1/2/3 numbering not used: the spec doesn't number phases.
- 7.3 Peer review taught on every route as the last gate (F3). No Higher badge.
- 7.4 Thalidomide kept as one sentence so verbatim q3 can be used, as the brief allows. It is context, not spec; Code may drop the line and q3 together.
- 7.5 The dots in the gate figure are illustrative, labelled; no attrition numbers.

**8 · Monoclonal antibodies**
- 8.1 TH only; the picker is hidden and the page shows "Triple Higher only". Badge 8461 4.3.2.1–4.3.2.2.
- 8.2 Bank q3 rebuilt: same stem, options and key, wx2 replaced with F1's wording.
- 8.3 Production in spec words: "single clone of cells", "single hybridoma cells are cloned" (F4); no B-lymphocytes, spleen, myeloma or polyclonal.
- 8.4 All four spec uses, including research with a fluorescent dye (F3). Evaluation uses the spec's own disadvantage, "more side effects than expected ... not as widely used as hoped"; "fewer side effects" appears nowhere in my text (F2). Verbatim q2's key "leaving healthy cells unaffected" kept.
- 8.5 hCG is named (source); the spec doesn't name the hormone. Mice as an ethical disadvantage is from F2 (WS 1.3).

**9 · Plant disease and defences**
- 9.1 Badge 8461 4.3.3.1–4.3.3.2, not 4.3.5. TF TH only; picker offers the two Triple routes.
- 9.2 Higher layer (TH only): the spec's detection list including "the presence of pests", and identification including "testing kits that contain monoclonal antibodies" (F1). On TH, bank q5 swaps to a testing-kit item; counts stay five.
- 9.3 Aphids, nitrate (protein synthesis, growth; stunted) and magnesium (chlorophyll; chlorosis) taught on TF and TH, with two bank items and a rung-3 chain (F2).
- 9.4 Defences on the spec's three categories; thorns and hairs are mechanical; bark is "layers of dead cells ... which fall off" (F3). No hypersensitive response, SAR or stomatal closure; q3 not used (F4). Cuticle in my text "stops microorganisms getting in"; verbatim q2 kept as F5 allows. No alkaloids or foxglove.
- 9.5 "Taking pathogens with them" (bark) is the brief's misconception note, not spec text. Mechanical reasons for drooping leaves and mimicry are my wording; Code to check.
- 9.6 Hook: both options are marked right, as yellowing can be either; the reply says how to tell.

**10 · Photosynthesis**
- 10.1 No RP block: one forward link to Rate of photosynthesis (F1, F2).
- 10.2 Word equation written out with "light" over the arrow (inline SVG arrow); endothermic in spec words; symbols to recognise only, no balanced equation.
- 10.3 q2 (why green) not used; no wavelengths (F3). No compensation point (F4). Root cells: "no light, no chloroplasts" (F5).
- 10.4 Bank: q1 q3 q4 verbatim (q4 keeps "ATP energy" in wx1, as F5 allows); new endothermic and symbol items.
- 10.5 Light-off toggle states that respiration carries on in every cell; respiration is otherwise a link.

**11 · Rate of photosynthesis**
- 11.1 RP labelled by route: "Required practical 5" on CF CH, "Biology required practical 6" on TF TH (F2), in the header chip, the section eyebrow and the key note.
- 11.2 Four factors including chlorophyll (F4), every route; magnesium kept off the base layer (link to Plant disease only). Temperature: "an optimum", no number; curve rises then falls, no plateau (README correction). Heat shield and thermometer, repeats and means, gas syringe as the improvement (F7). No ice, no sodium hydrogencarbonate.
- 11.3 Higher layer (CH TH): interacting factors with a two-CO₂-line graph (F3) and greenhouse economics with a two-step cost/yield choice (F5). Greenhouse figures are made-up, labelled.
- 11.4 rate = amount ÷ time triangle (A over R × t), "Written out", no chip. CFIFA worked: 48 bubbles in 4 min → 12 per min; 3.6 cm³ in 90 s → 1.5 min → 2.4 cm³/min (F6's own examples). Attempts: 75 in 5 min → 15; 4.2 cm³ in 120 s → 2.1 cm³/min.
- 11.5 Higher: light intensity (L) = 1 ÷ d² triangle, 1 on top as a fixed cell (new: Ks4Triangle now accepts `fixed` on the top item too), square-root extra line on d. CFIFA worked: 10 → 20 cm → a quarter (F6); 0.1 m → 30 cm, converting first → a ninth. Attempts: 15 → 30 cm → a quarter; 5 cm → 0.2 m → a sixteenth. Each sets out one line per distance then a comparison line, as the brief asks. No worked example finds d; the triangle shows that rearrangement only.
- 11.6 Ladder rung 2: 36 bubbles in 3 min (all); second item 2.7 cm³ in 90 s → 1.8 (CF TF) or 10 → 30 cm → 9 times lower (CH TH). Rung 3 second chain: temperature above optimum (CF TF) or greenhouse economics (CH TH).
- 11.7 Bank, five per route. CF TF: q3 verbatim, q2 rebuilt (same stem, key, distractors; wx1 and wx3 corrected per F1), chlorophyll, rate calculation, one-factor graph. CH TH: q1 verbatim (HT, F3), q3, chlorophyll, rate calculation, inverse-square. The brief's list (rate, chlorophyll, graph on all routes, plus inverse-square and greenhouse on HT) is more than five on HT: graph reading is in rung 3 and greenhouse in rung 3 and the Higher layer instead. Code to check.
- 11.8 RP bubble counts (10 cm 52, 20 cm 30, 30 cm 16, 40 cm 9) are made-up, labelled.

**12 · Uses of glucose**
- 12.1 Five uses in spec words, no ranking; respiration "in every living cell, all the time" (F3). Amino acids route is blocked until nitrate ions are supplied.
- 12.2 Bank q1 rebuilt per F1: same stem and key; option 1 is now "Starch dissolves more easily in cell sap"; wx2 corrected (dissolved sugars, as sucrose, move in the phloem; starch is not transported). q2, q3 verbatim (q3's "main use" stem as F3 allows; q3 key keeps "ATP").
- 12.3 Starch stores without carrots: potato tubers, parsnip roots, seeds, leaves (F2). Osmosis in words, no "water potential"; fats and oils "for storage", seed examples sunflower and rapeseed, no olive oil or membranes (F4).
- 12.4 Food tests are a connects link to Digestive system (batch 6), not taught.

**13 · Aerobic respiration**
- 13.1 Exothermic, continuous, "supplies all the energy needed for living processes", and the spec's three uses (F4, F6). No ATP anywhere in my text (F3); verbatim q2 keeps "ATP" in a distractor and wx2.
- 13.2 Energy is outside the word equation; the sort has an "energy: not in the equation" item. Symbols for recognition only; no balanced equation.
- 13.3 q3 not used (F1): its key and wx lean on ATP (F3). Replaced with a spec-worded mitochondria/energy-demand item. No cristae.
- 13.4 The "much more energy than anaerobic" comparison is a pointer to Anaerobic respiration, which owns the compare (F5 content stays base there).
- 13.5 No "all the energy in C–H bonds" line (F2).

**14 · Anaerobic respiration**
- 14.1 Badge 4.4.2.1, not 4.4.2.2 (F5). Three-column comparator: aerobic / muscles / plants and yeast; "fermentation" names only yeast's (F4).
- 14.2 q4 not used (F1); replaced with a "which transfers more energy and why" item (complete vs incomplete oxidation). No ATP numbers in my text; verbatim q3's wx1 keeps "~2 vs ~36", as the brief rules q3 usable.
- 14.3 Lactic acid to the liver is left to Response to exercise (one-line pointer, no HT layer here) (F2).
- 14.4 Fizz: "in beer and sparkling wine" (F3). Ethanol "evaporates when baked" is from the source.

**15 · Response to exercise**
- 15.1 Badge 4.4.2.2, not 4.4.2.3 (F5). Base: heart rate, breathing rate and breath volume rise to supply more oxygenated blood; lactic acid build-up "creates an oxygen debt" (term only); fatigue in spec words.
- 15.2 Higher layer (CH TH): liver conversion and the oxygen debt definition; the timeline shades the oxygen debt on CH TH only (F1). Recovery note, rung 3's second chain and rung 4's last point change by tier.
- 15.3 Bank: CF TF q1 verbatim + 4 new (breath volume, fatigue, when muscles respire anaerobically, oxygen debt term). CH TH q1 q2 q3 verbatim + 2 new. q2 kept as written (F4).
- 15.4 No EPOC (F2); no vasodilation, stroke volume, skin flushing or training adaptations (F3). Glycogen breakdown not used (4.5.3.2 link only).
- 15.5 Curves are made-up teaching data, labelled. Connects link to batch 4's heart page uses the prompt's path (G3).

**16 · Metabolism**
- 16.1 Badge 4.4.2.3, not 4.4.2.4 (F8). Spine is "building up / breaking down"; no anabolism/catabolism in my text (F7); verbatim q3 keeps "ANABOLIC (building)", glossed.
- 16.2 Lipid: "one molecule of glycerol and three molecules of fatty acids", no membranes or triglycerides (F1). No digestion chain (F2).
- 16.3 All three missing spec items taught (F3): glucose + nitrate to amino acids to proteins (with a bank item), the importance of the small units, and respiration's energy driving synthesis.
- 16.4 Layers: Higher (CH TH) thyroxine "stimulates" the basal metabolic rate (F5); Triple (TF TH) kidneys filter urea into urine; Triple Higher (TH) deamination in the liver to ammonia, then urea (F4). Base keeps "excess proteins broken down to form urea for excretion", carried in plasma to the kidneys.
- 16.5 Bank: CF TF q1 q3 + amino acids, lipid, respiration-energy. CH swaps the energy item for thyroxine. TH: q1 q3 amino acids, q2 (TH only, F4) and thyroxine. "Ammonia is toxic, so it is immediately converted" in the TH layer is standard 4.5.3.3 wording; Code to check.
- 16.6 Next is blank: 4.5 isn't in batches 4–7.

## Not done / for Code

- Videos: `KS4.VIDEOS` is empty, so the slot stays hidden.
- No examiner tips: none approved.
- Links to batches 4 and 5 resolve only in Code's layout (G3).
- Dark mode uses the existing remap; SVG plates stay cream.
