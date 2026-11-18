# enzymes

Sources: AQA 8464 4.2.2.1 (CF, CH) and 8461 4.2.2.1 (TF, TH), word for word the same, no HT-only or "(biology only)" lines. Required practical: **8464 RP 4 / 8461 RP 5** "investigate the effect of pH on the rate of reaction of amylase enzyme. Students should use a continuous sampling technique to determine the time taken to completely digest a starch solution at a range of pH values. Iodine reagent is to be used to test for starch every 30 seconds. Temperature must be controlled by use of a water bath or electric heater." (AT 1, 2, 5 on 8464; AT 1, 2, 5, 8 on 8461). Skills: MS 1a, 1c rate calculations; WS 1.2 lock and key as a simplified model. Rainford SOW Unit 2 "Catalysts and enzymes lock and key theory" (define catalyst and enzyme; properties; why specific; denatured by high temperature and extremes of pH; lock and key and collision theory; key words denatured, products, specific), "Factors affecting enzyme action" / "Bile" (interpret graphs for optimum temperature or pH), "Chemistry of Food" (calculate the rate of enzyme-controlled reactions).

Old page: Design batch-2 (`enzymes.dc.html`), family "Required practical", routes CF CH TF TH, review_state examiner-reviewed. Eyebrow routed: "AQA Biology (8461) 4.2.2.1 · Required practical" on Triple, "(8464)" on Combined. **Practice set = the route's subtopic `quiz` list via `K.bank(slug, R.route)`; Rung 1 = `K.find(slug, route, 'After an enzyme-catalysed reaction')`.** So the fixes to those items are quiz JSON edits, and the K.find needle must survive in exactly one stem per route.

| Spec statement | Where it is covered (lean record) | Route | Ticked |
|---|---|---|---|
| Relate knowledge of enzymes to Metabolism | Dive deeper 'Enzymes and metabolism' (link to Metabolism) | CF CH TF TH | ✓ |
| Describe the nature of enzyme molecules and relate their activity to temperature and pH changes | Cards 'What enzymes are', 'Temperature', 'pH'; Key fact; Rung 3; practice Q1, Q2, Q4 | CF CH TF TH | ✓ |
| Carry out rate calculations for chemical reactions (MS 1a, 1c) | Card 'Calculating the rate' (CFIFA, rate = 1 ÷ time as a processing step); Rung 2 | CF CH TF TH | ✓ |
| Enzymes catalyse specific reactions in living organisms due to the shape of their active site | Card 'What enzymes are'; card 'The lock and key model' (fitFig); practice Q3 | CF CH TF TH | ✓ |
| Use the 'lock and key theory' as a simplified model to explain enzyme action | Card 'The lock and key model'; Dive deeper 'Where the model is too simple' | CF CH TF TH | ✓ |
| RP 4 / RP 5: pH and amylase, continuous sampling, iodine every 30 s, water bath | Card 'Required practical 4: pH and amylase' (CF CH) / 'Required practical 5: pH and amylase' (TF TH) (rigFig, method); Rung 4 | CF CH TF TH | ✓ |
| Sites of production/action, bile, food tests | The digestive system lesson | CF CH TF TH | ✓ (other lesson) |

**Gaps and mismatches.**
- "Relate knowledge of enzymes to Metabolism" (4.4.2.3): no link from this page. One "Connects to" line is enough.
- The RP header reads "Required practical · RP4 Combined Science · RP5 Biology" on every route; key line "(RP4 Combined / RP5 Biology)" likewise. Correct numbers, but each route should show only its own.
- "rate = 1 ÷ time" is presented as "Equation · Learn it". It is a standard processing step (AQA's RP materials use rate = 1/time or 1000/time), not a spec equation. Keep the method; do not present it as an AQA equation to learn.

**Practice set source.** Subtopic quiz list, five items, identical on all four routes (`all_subtopics_biology*.py`). New quiz-enzymes.json needed.

**Audit of the ladder and practice set (faults found).**
- Every quiz item: credited option visibly the longest, with a dash tail.
- Quiz "An enzyme is heated to 80°C": credited "It denatures — the active site shape permanently changes…"; replies "~37°C" and capitals ("PERMANENT").
- Quiz "Why does pepsin work best at pH 2?": pepsin and pH 2 are not in the spec ("the protease made in the stomach"); distractor "Pepsin denatures at any pH above 2" — the reply concedes it is not instant, fine as wrong, but the item is off-spec. Replace.
- Quiz "why can amylase only digest starch — not proteins?": reply "Amylase is produced in the mouth AND pancreas" (the salivary glands, not the mouth; also the small intestine); capitals.
- Quiz "What happens to the rate … when substrate concentration increases?": substrate concentration is not in 4.2.2.1 (temperature and pH only). Replace.
- Quiz/Rung 1 "After an enzyme-catalysed reaction, what happens to the enzyme?" (the K.find needle): credited visibly longest with dash tail. Keep the stem (needle), fix the options.
- Lock and key bench, pick P reply: "AQA’s word is complementary, not 'the same shape'." The spec does not use "complementary" (it says "due to the shape of their active site"); mark schemes accept it. Reword so it does not claim to be AQA's word.
- Temperature sketch replies, CFIFA numbers and the practical's data: not re-audited here beyond reading; recompute in the examiner pass (e.g. 1 ÷ 75 = 0.0133 s⁻¹; 1 min 45 s = 105 s, 1 ÷ 105 = 0.0095 s⁻¹; 2.5 min = 150 s, 1 ÷ 150 = 0.0067 s⁻¹; 0.0125 s⁻¹ → 80 s; 3 min 15 s = 195 s; 1 ÷ 60 = 0.017 s⁻¹; 4 min = 240 s).

**Old subtopic data.** spec "4.2.2.2" on all routes: wrong (4.2.2.2 is the heart); want 4.2.2.1. rp "RP3 — Investigate the effect of pH…" on all routes: wrong number on every route (8464 RP 4, 8461 RP 5). The page does not render these fields, but the subtopic data is the source of truth elsewhere.

**Unsure (left out until checked).**
- "Enzymes are proteins": true, not stated in 4.2.2.1 ("describe the nature of enzyme molecules" covers it). Keep.
- "Enzyme–substrate complexes" (Rung 3 reply): beyond spec wording; acceptable, keep to one mention or say "fewer substrate molecules fit".
- Water bath 35 °C and "keep below 40 °C": method choice, not spec.

**Removed or moved.**
- Design benches (lock and key fit/heat/cool, run the practical, plot, anomaly), temperature sketch: off the page. fitFig and rigFig kept as figures; temperature and pH graphs requested as new figures.
- "AQA's word is complementary": in the removed bench; gone.
- "rate = 1 ÷ time · Learn it": now a processing step in 'Calculating the rate'; the four CFIFA placeholders 'learn it' become 'rate = …'.
- Eyebrow 'AQA Biology (8464)' on Combined routes: now 'AQA Combined Science (8464)'.
- RP header 'RP4 Combined · RP5 Biology' on every route: each route now sees only its own number.
- Quiz: 'Why does pepsin work best at pH 2?' and 'substrate concentration' replaced (new ids; old ids -> null). The other three stems kept, options and explanations rewritten. K.find needle kept in exactly one stem per route.
- Rung 3 link 'enzyme–substrate complexes': reworded to 'the substrate no longer fits the active site'.
- Examiner/blind (18 Nov): Rung 3 chain: 'The temperature rises above the optimum' → 'The shape of the active site changes, so the enzyme is denatured' → 'The substrate no longer fits…' (ONE order).
- Practice Q5 / Rung 1 credited option shortened to 'It is unchanged and can be used again' (quiz_org.py; stem kept).
- Rung 2 (Foundation) and both worked examples: 'the iodine first stayed orange-brown at N s: all the starch had been digested' (the old 'stayed orange-brown after N s' read as still reacting).
- 'Of the pH values tested, that one is closest to the optimum.'
