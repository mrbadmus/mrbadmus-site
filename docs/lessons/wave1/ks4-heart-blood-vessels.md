# heart-blood-vessels

Sources: AQA 8464 4.2.2.2 (CF, CH) and 8461 4.2.2.2 (TF, TH), word for word the same, no HT-only or "(biology only)" lines. Skills: MS 1a, 1c, simple compound measures such as rate, rate calculations for blood flow. Rainford SOW Unit 2 "Blood vessels" (structure adapted to function), "The heart" ×2 (functions of heart and circulation; label four chambers, vena cava, pulmonary artery, pulmonary vein, aorta; blood flow body → heart → lungs → body; heart as a double pump and why it is efficient; pacemaker cells and coronary arteries; heart dissection), "Breathing and gas exchange" (trachea, bronchi, alveoli, capillary network; alveoli adapted; lung dissection; key word bronchioles). No AQA equation sheet equation.

Old page: Design batch-4 (`ks4-biology-4.2.2.2-heart-blood-vessels.dc.html`), family Model, routes CF CH TF TH, port_rulings. Practice set = hard-coded `bankSrc` (5 items).

| Spec statement | Where it is covered (lean record) | Route | Ticked |
|---|---|---|---|
| Know the structure and functioning of the human heart and lungs, including how lungs are adapted for gaseous exchange | Cards 'A double circulatory system' (heartFig), 'The lungs' (lungFig); Rung 3 chain 2 | CF CH TF TH | ✓ |
| The heart pumps blood around the body in a double circulatory system. Right ventricle → lungs (gas exchange); left ventricle → rest of the body | Card 'A double circulatory system'; card 'The thicker left ventricle'; Key fact; Rung 3 chain 1; practice Q1 | CF CH TF TH | ✓ |
| Blood vessels limited to aorta, vena cava, pulmonary artery, pulmonary vein and coronary arteries; valve names not required | Reveal 'The blood vessels of the heart'; valves: 'You do not need their names'; Rung 1 Q1; practice Q2 | CF CH TF TH | ✓ |
| Lungs restricted to trachea, bronchi, alveoli and the capillary network surrounding the alveoli | Card 'The lungs' | CF CH TF TH | ✓ |
| Natural resting heart rate controlled by a group of cells in the right atrium acting as a pacemaker; artificial pacemakers are electrical devices that correct irregularities in the heart rate | Card 'Pacemakers'; Rung 1 Q2; practice Q5 | CF CH TF TH | ✓ |
| Three types of blood vessel: arteries, veins, capillaries; explain how structure relates to function | Card 'Arteries, veins and capillaries' (vesselFig); reveal 'How each blood vessel suits its job'; Rung 4; practice Q3, Q4 | CF CH TF TH | ✓ |
| Use simple compound measures such as rate; rate calculations for blood flow (MS 1a, 1c) | Card 'Rate calculations' (CFIFA; 'a rate is an amount divided by the time'); Rung 2 | CF CH TF TH | ✓ |

**Gaps and mismatches.**
- None in the spec lines.
- "rate of blood flow = volume of blood ÷ time" and "heart rate = number of beats ÷ time" are shown under "Equations". Neither is an AQA equation-sheet equation; they are the spec's "simple compound measures". Keep, but not as equations to learn by heart beyond "rate = amount ÷ time".
- Overlap with Coronary heart disease: artificial pacemakers and faulty valves. Pacemakers belong here (4.2.2.2); valve replacement belongs to CHD (4.2.2.4).
- Rainford "bronchioles": not in the spec's restricted list. Leave out.
- "Left ventricle has a thicker wall": not spec, standard explanation. Keep as one card.

**Practice set source.** Hard-coded `bankSrc`, five items, same on all routes. Fixes are `logic_edits`.

**Audit of the ladder and practice set (faults found).**
- Quiz "Why does the left ventricle have thicker walls…": credited visibly longest (+52) with dash tail; distractor "oxygenated blood which is heavier" ok as wrong.
- Quiz "The pulmonary artery … what type of blood": credited longest (+30), dash tails; reply "This is the most common mistake in this topic!" and capitals.
- Quiz "Why do veins have valves but arteries do not?": credited two sentences (+63), dash tail; reply "Valves in veins do slightly slow flow" muddles the item. Also arteries do have valves at their base (the semilunar valves where they leave the ventricles); "arteries do not [have valves]" needs "along their length", as the page's own card says.
- Quiz "What makes capillaries efficient…": credited longest (+33). Distractor "They carry both oxygenated and deoxygenated blood simultaneously" is not definitely wrong (blood gives up oxygen as it passes along a capillary). Replace.
- Quiz "What does an artificial pacemaker do?": credited longest (+23).
- CFIFA/Rung 2 recomputed: 6.0 ÷ 1.5 = 4.0 dm³/min ✓; 21 ÷ 0.25 = 84 ✓; 1500 cm³ = 1.5 dm³, 1.5 ÷ 0.30 = 5.0 dm³/min ✓; 36 ÷ 0.5 = 72 ✓; 2400 cm³ = 2.4 dm³, 2.4 ÷ 4.0 = 0.60 dm³/min ✓; 18 ÷ 0.25 = 72 ✓; 0.90 ÷ 0.20 = 4.5 dm³/min ✓ (answer key 4.5).
- Rung 4 reject "Capillaries have the lowest blood pressure." ✓ (veins are lowest).

**Old subtopic data.** spec "4.2.3" on all routes: wrong (want 4.2.2.2; 4.2.3 is plant tissues). CH and TH carry a "higher" block (artificial pacemakers, valves "from pigs or cows", artificial hearts, evaluate treatments): no HT content exists in 4.2, and most of it belongs to 4.2.2.4.

**Unsure (left out until checked).**
- Semilunar valves: name not required; say "valves where the arteries leave the heart" only if needed.
- "Pressure falls all the way round: highest in arteries, lower in capillaries, lowest in veins": true, beyond the spec words. Keep as one line.

**Removed or moved.**
- Design circuit bench, vessel sort, Think again: off the page; heartFig, lungFig, vesselFig kept as figures.
- 'Equations' header for blood flow and heart rate: gone; now 'a rate is an amount divided by the time' with the two rates written out.
- Rainford 'bronchioles': left out (not in the spec's list).
- Old subtopic data CH/TH 'higher' block (pacemakers, valves from pigs or cows, artificial hearts): not Higher content; the valve and artificial-heart parts belong to Coronary heart disease.
- Practice set: capillary distractor 'carry both oxygenated and deoxygenated blood' replaced; options and replies tidied. Stems kept, so ids kept.
- Examiner/blind (18 Nov): Rung 3 (i) chain left ventricle and Rung 3 (ii) chain alveoli rewritten as one-order cause-and-effect chains (prompts unchanged). The alveoli chain is thin walls → short diffusion distance → blood carries oxygen away, keeping the gradient steep.
- Practice Q5 credited 'It corrects irregularities in the heart rate' (was visibly longest).
- Rung 2 (i) conversion option 'Nothing to convert' → 'Nothing to convert: use 15 s as the time' (18 × 4 made it defensible).
- Heart figure: retired bench stop marker removed; 'valve' label now points at the right atrioventricular valve.
