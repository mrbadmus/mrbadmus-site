# particle-motion-pressure

Sources: AQA 8464 6.3.3.1 (CF CH); AQA 8463 4.3.3.1, 4.3.3.2 (physics only) and 4.3.3.3 (physics only, HT only) (TF TH). 6.3.3.1 and 4.3.3.1 are word for word the same; 8464 has no 6.3.3.2 or 6.3.3.3. Read from the 2016 specification PDFs on Mide's Mac (AQA-8464-SP-2016.pdf v1.1, AQA-8463-SP-2016.pdf v1.1). Skills: WS 1.2; MS 3b, c (pV). Rainford KS4 SOW, Year 10 Physics lessons 26 "Particle model and pressure" and 27 "(PHYS) Pressure and volume" (both map here); Physics LO sheet: the relationship between temperature and pressure for a gas; Brownian motion; how to investigate pressure and temperature; (SEPS) why pressure rises when volume falls, calculate pressure or volume, problems.
Routes: CF CH TF TH.
Legacy status: LEGACY, Design batch 3 (`particle-motion-pressure.dc.html`, family Model). Ladder: Ks4Ladder r1..r4 from the page (they differ by route: Triple Rungs 2 and 3 are pV, Triple Higher Rung 4 is the bicycle pump). Worked examples and Your turn: the page's own cfExamples / cfQuestions (pV), placed by the `cfifa` slot in a TF TH card. Practice set: K.bank, the route's `quiz` list. Eyebrow already route-aware: "AQA Combined Science (8464) 6.3.3.1 · Model"; "AQA Physics (8463) 4.3.3.1–4.3.3.2 · Model" (TF); "4.3.3.1–4.3.3.3" (TH).

**The 4.3.3.2 / 4.3.3.3 finding.** Both are already taught on the Triple pages, inside this lesson: the Design page's piston bench, "net force at right angles" explainer, pV equation box and pV worked examples are `data-route="triple"`, and its fast-push stage and the bicycle-pump Rung 4 are Triple Higher only. No spec gap and no new lesson. The lean record keeps them here as route-gated cards ('Pressure in gases', 'Pressure and volume', 'Worked examples' on TF TH; 'Doing work on a gas' on TH).

| Spec statement (AQA wording) | Where it is covered | Route | Flag | Ticked |
|---|---|---|---|---|
| The molecules of a gas are in constant random motion. | Card 'How gas molecules move' (AQA words); Key words; Easy mistakes 3; Rung 1 | CF CH TF TH | all | ✓ |
| The temperature of the gas is related to the average kinetic energy of the molecules. | Card 'Temperature and the molecules' (AQA words); Card 'Heating a gas at constant volume'; Key fact; Practice Q3 | CF CH TF TH | all | ✓ |
| Changing the temperature of a gas, held at constant volume, changes the pressure exerted by the gas. | Start here; Card 'Heating a gas at constant volume' (AQA words, both directions); Key fact; Rung 2 CF CH (data: pressure against temperature); Rung 3 CF CH (tyre on a frosty morning); Practice Q1, Q2, Q4, Q5 (CF CH) | CF CH TF TH | all | ✓ |
| Explain how the motion of the molecules in a gas is related to both its temperature and its pressure (WS 1.2). | Cards 'Where gas pressure comes from', 'Temperature and the molecules', 'Heating a gas at constant volume'; Easy mistakes 1, 2; Rung 4 CF CH TF (explain how molecules produce a pressure) | CF CH TF TH | all | ✓ |
| Explain qualitatively the relation between the temperature of a gas and its pressure at constant volume (WS 1.2). | Card 'Heating a gas at constant volume'; Key fact; Rung 3 CF CH; Practice Q2, Q4 | CF CH TF TH | all | ✓ |
| (Physics only) A gas can be compressed or expanded by pressure changes. The pressure produces a net force at right angles to the wall of the gas container (or any surface). | Card 'Pressure in gases' (AQA words) | TF TH | Triple only | ✓ |
| (Physics only) Use the particle model to explain how increasing the volume in which a gas is contained, at constant temperature, can lead to a decrease in pressure (WS 1.2). | Card 'Pressure in gases' (same speed, further between hits, hit less often); Rung 3 TF TH (chain: gas expands at constant temperature) | TF TH | Triple only | ✓ |
| (Physics only) For a fixed mass of gas held at a constant temperature: pressure × volume = constant, p V = constant (p in pascals, Pa; V in metres cubed, m³). Apply this equation, which is given on the Physics equation sheet (MS 3b, c). | Card 'Pressure and volume' (AQA words, units, "on the Physics equation sheet", p₁ V₁ = p₂ V₂, unit matching); legacy cfifa | TF TH | Triple only | ✓ |
| (Physics only) Calculate the change in the pressure of a gas or the volume of a gas (a fixed mass held at constant temperature) when either the pressure or volume is increased or decreased. | Card 'Worked examples' (legacy cfExamples: compress; find a volume (TH); convert first; Your turn ×2); Rung 2 TF TH (calc: 250 kPa / 360 kPa); Practice Q5 (TF TH: 200 kPa) | TF TH | Triple only | ✓ |
| (Physics only, HT only) Work is the transfer of energy by a force. Doing work on a gas increases the internal energy of the gas and can cause an increase in the temperature of the gas. | Card 'Doing work on a gas' (AQA words) | TH | Triple Higher only | ✓ |
| (Physics only, HT only) Explain how, in a given situation eg a bicycle pump, doing work on an enclosed gas leads to an increase in the temperature of the gas (WS 1.2). | Card 'Doing work on a gas' (bicycle pump, outlet blocked); Rung 4 TH (6 marks: bicycle pump) | TH | Triple Higher only | ✓ |

**Equations and units.**

| Equation (AQA words) | Symbols | Units | Recall or apply | Equation sheet (8463) |
|---|---|---|---|---|
| pressure × volume = constant (for a fixed mass of gas at constant temperature) | p V = constant (p₁ V₁ = p₂ V₂) | p in Pa (kPa in the examples, matched on both sides); V in m³ (cm³ matched on both sides) | apply; physics only, TF TH | On the sheet: equation 12 ("For gases: pressure × volume = constant") |

**Faults in the current pages and data.**
- The old subtopic data (never shown on the Design page, batch-3 DEPARTURES) has kelvin, absolute zero and p ÷ T = constant, none of which is in 8463 or 8464, and tags pV = constant as Higher on the Combined data. Not shown on the lean page; the data is left as it is.
- Two rails and a per-route done[]: the legacy logic picks RAIL_BASE or RAIL_TRIPLE per route, a shape lean_ks4 could not read. The record's `pre_edits` (new in lean_ks4) fold them into one rail before the rail edits. Not a pupil-facing fault.
- Old quiz options: the tyre correct option was far the longest. Options rewritten; stems kept.

**Gaps and mismatches.**
- None in the AQA lines on any route (see the finding above).
- Rainford LO "Explain Brownian motion ... smoke particles and air molecules": not in 8463 or 8464 section 4.3 / 6.3 (it is KS3 prior learning in the same sheet). Left out.
- Rainford LO "Describe the linear relationship between changes in temperature and pressure" and "how it can be investigated": AQA asks only for the qualitative relation (and no kelvin). The Design's Combined Rung 2 (pressure rises steadily with °C, not proportional to °C) stays; no new card.

**Unsure (left out until checked).**
- Card 'Doing work on a gas' ends "the pressure rises by more than the smaller volume alone would cause". Physically right (the gas is not at constant temperature, so p₁V₁ = p₂V₂ does not hold), and it is the Design Rung 4's own marking point. Check the wording suits Higher pupils.
- The Start here reply says a can of air, which cannot burn, would burst too: true for an aerosol can in a fire; kept from the Design hook.

**Removed or moved.**
- Removed from the page: the gas bench (benchFig, two stages, Think again ×2), "Mark it like an examiner" (Ks4Sort), the piston bench (pistonFig, p3 and the TH fast push p4), the equation box, the Key note and the video. Their teaching is in the cards. Their activity ids go: `#bpick`, `#p3`, `#p4`, `#sort-1-1..8`, on all four routes.
- Removed: the classic matching cards (ks4c:particle-motion-pressure:match-1..4).
- The page's Ks4End `legal` line (about the benches) is emptied by lean_ks4.
- `activity_save_drive` cases `ks4-form-piston` (`#bpick-1`, `#p3`) and `ks4-form-piston-push` (`#p4`) will need retiring with absent-marker proof.

**Practice set source.** `K.bank(slug, R.route)`: the route's `quiz` list in all_subtopics_physics*.py. Five per route: Q1 to Q4 the same on every route, Q5 differs (CF CH qualitative, TF TH a pV calculation); correct option first (the build shuffles).

| Q | Origin | ks4q: id | Stem | Credited | Routes |
|---|---|---|---|---|---|
| 1 | kept (stem unchanged, options rewritten) | `7749378092` | Why does the pressure inside a tyre increase when a car has been driven for a while? | The air gets hotter, so its molecules move faster and hit the walls more often and harder | all |
| 2 | kept (stem unchanged, options rewritten) | `23f5ebc20e` | A gas is heated in a sealed, rigid container, so its volume stays the same. What happens to the pressure of the gas, and why? | It increases: the molecules move faster and hit the walls more often and harder | all |
| 3 | new | `fd688feb0a` | The temperature of a gas is related to which property of its molecules? | Their average kinetic energy | all |
| 4 | new | `520b48b721` | A sealed can of gas is cooled. Its volume does not change. What happens to the pressure? | It decreases | all |
| 5 | new | `a7de9759ba` | Which of these increases the pressure of a gas in a sealed, rigid container? | Heating the gas | CF CH |
| 5 | new | `0cd51798cd` | A fixed mass of gas at constant temperature has a pressure of 100 kPa and a volume of 0.50 m³. It is compressed to 0.25 m³. What is its new pressure? | 200 kPa | TF TH |

**Ladder.** Ks4Ladder r1..r4 from the Design page, positions kept, unchanged: Rung 1 (all: gas molecules' motion); Rung 2 (CF data 0–60 °C, CH data 10–50 °C, TF calc 250 kPa, TH calc 360 kPa with cm³ conversion); Rung 3 (CF CH tyre on a frosty morning; TF TH gas expands at constant temperature); Rung 4 (CF CH TF explain how molecules produce a pressure, 4 marks; TH bicycle pump, 6 marks).

**Assignment pool.** 64 rows for this slug in ks4_data/questions/physics/particle_model*.py (12 at positions 0–11, the auto window). None is changed here.
