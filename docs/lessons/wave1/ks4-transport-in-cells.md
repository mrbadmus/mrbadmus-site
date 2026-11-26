# transport-in-cells

Sources: AQA 8464 4.1.3.1 Diffusion, 4.1.3.2 Osmosis, 4.1.3.3 Active transport (CF, CH) and 8461 4.1.3.1–4.1.3.3 (TF, TH), word for word the same, no HT-only or "(biology only)" lines. **Required practical: 8464 RP 2 / 8461 RP 3** "investigate the effect of a range of concentrations of salt or sugar solutions on the mass of plant tissue" (AT 1, 3 and 5). The numbers differ because 8461 RP 2 is microbiology (4.1.1.6). Skills: WS 1.2 diagrams of diffusion and osmosis; WS 1.5 isotonic and high energy drinks; MS 1a, 1c rate of water uptake, percentages; MS 1c, 5c SA:V; MS 4a–4d graphs.

Old page: Design batch-4 (`ks4-biology-4.1.3-transport-in-cells.dc.html`), family Classify, routes CF CH TF TH. The header chip already reads "Required practical 2" (Combined) or "3" (Triple) per route (`rpLabel`). Practice set = hard-coded `bankSrc` (5 items, same on every route).

| Spec statement | Where it is covered (lean record) | Route | Ticked |
|---|---|---|---|
| Substances may move into and out of cells across the cell membranes via diffusion | Card 'Three ways across a membrane' (fig:transport-processes); card 'Diffusion' | CF CH TF TH | ✓ |
| Diffusion is the spreading out of the particles of any substance in solution, or particles of a gas, resulting in a net movement from higher to lower concentration | Card 'Diffusion'; Start here; Key fact | CF CH TF TH | ✓ |
| Oxygen and carbon dioxide in gas exchange, and urea from cells into the blood plasma for excretion in the kidney | Card 'Diffusion' | CF CH TF TH | ✓ |
| Explain how different factors affect the rate of diffusion: concentration gradient, temperature, surface area of the membrane | Card 'What makes diffusion faster' | CF CH TF TH | ✓ |
| A single-celled organism has a relatively large surface area to volume ratio ... | Card 'Surface area to volume ratio' | CF CH TF TH | ✓ |
| Calculate and compare surface area to volume ratios | Card 'Surface area to volume ratio' (worked and attempt steps, sav-w, sav-a); reveal 'Bigger cube, smaller SA:V'; Rung 2 (ii) | CF CH TF TH | ✓ |
| Explain the need for exchange surfaces and a transport system in multicellular organisms in terms of SA:V | Card 'Why large organisms need exchange surfaces'; Rung 3 (ii) | CF CH TF TH | ✓ |
| Explain how the small intestine and lungs in mammals, gills in fish, and the roots and leaves in plants, are adapted for exchanging materials | Reveal 'Exchange surfaces' | CF CH TF TH | ✓ |
| Effectiveness of an exchange surface: large surface area; thin membrane; (animals) efficient blood supply; (animals, gas exchange) ventilated | Card 'Why large organisms need exchange surfaces' | CF CH TF TH | ✓ |
| Osmosis is the diffusion of water from a dilute solution to a concentrated solution through a partially permeable membrane | Card 'Osmosis'; Key fact; Easy mistakes; practice Q5 | CF CH TF TH | ✓ |
| Use simple compound measures of rate of water uptake; use percentages; calculate percentage gain and loss of mass of plant tissue | Card 'Calculations' (CFIFA); RP card; Rung 2 (i) | CF CH TF TH | ✓ |
| Plot, draw and interpret appropriate graphs | RP card (fig:osmosis-mass-graph, reading where it crosses 0%) | CF CH TF TH | ✓ |
| RP 2 (8464) / RP 3 (8461): concentrations of salt or sugar solutions and the mass of plant tissue | Card 'Required practical 2: osmosis in potato' (CF CH) / 'Required practical 3: osmosis in potato' (TF TH); Rung 3 (i); practice Q2 | CF CH TF TH | ✓ |
| Active transport moves substances from a more dilute solution to a more concentrated solution (against a concentration gradient). This requires energy from respiration | Card 'Active transport'; reveal 'Comparing the three'; Rung 1; practice Q1, Q3 | CF CH TF TH | ✓ |
| Mineral ions into root hairs from very dilute soil solutions; sugar from lower concentrations in the gut into the blood | Card 'Active transport' | CF CH TF TH | ✓ |
| Describe how substances are transported by diffusion, osmosis and active transport; explain the differences | Reveal 'Comparing the three'; Rung 4 | CF CH TF TH | ✓ |
| (skills) WS 1.5 isotonic and high energy drinks | Left out (skills opportunity) | — | left out |

**Misconceptions taught against (Easy mistakes).** Water moves from concentrated to dilute; osmosis is the movement of salt or sugar; active transport goes down the gradient; bigger organisms have a bigger SA:V.

**Gaps and mismatches.** None in the content lines. "Turgid", "flaccid" and the membrane pulling away from the wall are not spec words: Dive deeper.

**Practice set source.** Hard-coded `bankSrc`, five items, same on all routes.

**Audit of the ladder and practice set (faults found and fixed).**
- Q1 "Which process requires ATP energy ...": ATP is not in the spec. **Replaced** by the same item asked as "energy from respiration" (new id; old id in `REPLACED`). Same options, same answer.
- Q2 (potato in pure water): credited the longest (+40), dash; a reply said "salt does diffuse slightly" (no salt in pure water). Options and replies rewritten.
- Q3 (oxygen removed): credited the longest. Options rewritten; "transferred" now "released".
- Q4 (plant cell in concentrated salt): credited the longest (+50), arrows, "plasmolysis". Options rewritten to equal length.
- Q5 (definition of osmosis): credited the longest (+48). Now the spec's wording, with three distractors of the same length.
- Worked example 1: Convert and Answer lines wordy, with dashes. Shortened; same numbers.
- Rung 3 (i) and (ii): link 2 could swap with link 1. Each link 2 now starts "So ...".
- Numbers checked: (3.4 − 4.0) ÷ 4.0 × 100 = −15%; 2800 mg = 2.80 g, (2.80 − 2.50) ÷ 2.50 × 100 = +12%; 0.60 g ÷ 120 min = 0.005 g/min; (2.8 − 3.2) ÷ 3.2 × 100 = −12.5%; 0.90 ÷ 90 = 0.01 g/min; Rung 2 (2.3 − 2.0) ÷ 2.0 × 100 = +15%; cube 4 cm: 96 ÷ 64 = 1.5 : 1; cubes 1, 2, 3 cm: 6 : 1, 24 ÷ 8 = 3 : 1, 54 ÷ 27 = 2 : 1.

**Old subtopic data.** spec "4.1.3" (the lesson is 4.1.3.1–4.1.3.3). The CH/TH `higher` block ("isotonic point", "water potential") is beyond the spec and the % change formula is on every route, not Higher; never rendered.

**Unsure (left out until checked).** The graph's crossing point, 0.37 mol/dm³, comes from the Design page's own six points (a line through them crosses 0% at 0.37); real potato varies.

**Removed or moved.**
- Design's three small figures (13 px labels in a 520–644 viewBox) are redrawn at 720 (`figlib/ks4lean_cell.py`); the plant/animal cells-in-solutions figure is now two lines in the Osmosis card. Think again, sort: off the page.
- Turgid, flaccid: Dive deeper. Command words: Dive deeper.
