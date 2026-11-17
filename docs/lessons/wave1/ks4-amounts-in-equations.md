# amounts-in-equations

Sources: AQA Combined Science Trilogy 8464 5.3.2.2 Amounts of substances in equations (HT only), read from spec-8464.txt (CH), and AQA Chemistry 8462 4.3.2.2 (HT only), read from spec-8462.txt (TH). Word for word the same. The lesson exists on CH and TH only, so everything is Higher content and no route gating is needed. Rainford SOW "Reacting masses": (H) calculate the masses of substances shown in a balanced symbol equation; (H) calculate the masses of reactants and products from the balanced symbol equation and the mass of a given reactant or product. LEGACY page (batch 11).

| Spec statement | Where it is covered | Route | Ticked |
|---|---|---|---|
| The masses of reactants and products can be calculated from balanced symbol equations. | Card: Reacting masses in three steps (steps-worked, steps-attempt); Card: Each step on its own (cfifa); Key fact; Rung 2; Rung 4; Practice Q3, Q5 | CH TH | ✓ |
| Chemical equations can be interpreted in terms of moles. Mg + 2HCl → MgCl₂ + H₂ shows that one mole of magnesium reacts with two moles of hydrochloric acid to produce one mole of magnesium chloride and one mole of hydrogen gas. | Start here; Card: Reading an equation in moles (verbatim); Card: The mole ratio (legacy-fig:rFig); Rung 1 Q1, Q2; Practice Q1 | CH TH | ✓ |
| Calculate the masses of substances shown in a balanced symbol equation | Reveal: 2Mg + O₂ → 2MgO in grams; Card: Masses in a balanced equation; Rung 3 chain 2; Practice Q2 | CH TH | ✓ |
| Calculate the masses of reactants and products from the balanced symbol equation and the mass of a given reactant or product | Card: Moles from mass (triangle:EQ_N); Card: Each step on its own (cfifa); Card: Reacting masses in three steps (steps slots); Easy mistakes; Rung 2; Rung 3 chain 1; Rung 4; Practice Q3, Q4, Q5; Dive deeper: Check your answer | CH TH | ✓ |
| MS 1a decimals, MS 1c ratios, MS 3b change the subject, MS 3c substitute with units | Card: The mole ratio (moles wanted = moles given × wanted ÷ given); triangle:EQ_N; cfifa; steps | CH TH | ✓ |

**Gaps and mismatches.**
- The old generator page taught percentage yield and atom economy on this lesson, on CH too. Both are 8462 4.3.3 (chemistry only), so they are not on the Combined spec. The Design page had already moved them out; they stay out (they have their own Triple lessons).
- "Mole ratio" is not AQA's phrase; AQA says the equation "can be interpreted in terms of moles". The card gives AQA's sentence word for word first, then names the ratio.
- Eyebrow: the legacy literal "AQA Chemistry 5.3.2.2 · Higher only" shows the Combined number on TH (Triple is 4.3.2.2). Builder item for the lead, as for moles.

**Practice set source.** The page's own `BANK`, the same five on CH and TH. It does not read the subtopic `quiz` list, so fixes are `logic_edits` and there is no quiz-amounts-in-equations.json. No stem edited, so all five ids survive.

**Worked examples.** `cfifa` is the legacy page's own cfExamples and cfQuestions (Step 1, Step 2 and Step 3 each alone). `steps-worked` is aie-w (1.2 g of Mg with excess HCl) and `steps-attempt` is aie-a (8.0 g of CaCO₃). The record adds EQ_N (the legacy page's own triangle). Every number checked: 2400 ÷ 24 = 100; 0.6 × 2 ÷ 3 = 0.4; 0.05 × 2 = 0.1; 5.6 ÷ 56 = 0.1; 0.3 × 1 ÷ 2 = 0.15; 0.15 × 32 = 4.8; 1.2 ÷ 24 = 0.05, 0.05 × 2 = 0.1 g; 8.0 ÷ 100 = 0.08, 0.08 × 44 = 3.52 g. Cards: 2 × 24 = 48, 32, 2 × 40 = 80, 48 + 32 = 80; 0.2 × 1 ÷ 2 = 0.1; 4.8 + 3.2 = 8.0. Equations balanced: 2Mg + O₂ → 2MgO; N₂ + 3H₂ → 2NH₃; Mg + 2HCl → MgCl₂ + H₂; CaCO₃ → CaO + CO₂; Fe₂O₃ + 3CO → 2Fe + 3CO₂.

**Figure.** legacy-fig:rFig kept. Read its drawer: three bars for Mg, O₂ and MgO with "coefficient 2/1/2" under them and the mole number over each; the title "2Mg + O₂ → 2MgO ratio 2 : 1 : 2" and the caption "whatever the amount, the ratio holds". The lean page renders its first state, 2 mol of Mg (2, 1 and 2 mol). The card text beside it describes that state and then the 0.2 mol case in words.

**Audit of the ladder and practice set.**

| Item | Verdict |
|---|---|
| Rung 1 Q1 What the big numbers tell you | ok |
| Rung 1 Q2 Ratio of hydrogen to ammonia | ok (3 : 2) |
| Rung 2 calc 1 4.8 g Mg to MgO | ok (8.0 g) |
| Rung 2 calc 2 10 g CaCO₃ to CaO | ok (5.6 g) |
| Rung 3 chain 1 Oxygen for 2.4 g of Mg | ok. One order (moles, ratio, mass). 2.4 ÷ 24 = 0.1; 0.1 × 1 ÷ 2 = 0.05; 0.05 × 32 = 1.6 g. |
| Rung 3 chain 2 Reading an equation in grams | ok. One order ("Then", then the conservation check that needs the masses). |
| Rung 4 Iron from 16 kg Fe₂O₃, 6 marks | ok. Mr 160; 16 000 ÷ 160 = 100 mol; 200 mol Fe; 11 200 g = 11.2 kg. |
| Practice Q1 N₂ + 3H₂, 0.6 mol | ok (0.4 mol; shown labels 0.4, 0.6, 0.9, 1.2 mol). Explanations used dashes: rewritten plainly. Options unchanged. |
| Practice Q2 Masses shown by 2Mg + O₂ → 2MgO | ok (48 g + 32 g → 80 g) |
| Practice Q3 4.8 g Mg to MgO | ok (8.0 g). Fault: credited option visibly the longest (71 against 24). Fix: "8.0 g: 0.2 × 40" (15). |
| Practice Q4 Mr of hydrogen gas | ok (2). Fault: credited option visibly the longest (21 against 4). Fix: "2". The stem's "used in Step 3" matches the three steps on the lean page. |
| Practice Q5 Method for CaO from CaCO₃ | ok. Fault: credited option visibly the longest (95 against 51). Fix: "Mass to moles, then the ratio, then moles to mass" (49). |

**Removed or moved.**
- Removed: the recipe hook (Start here is now AQA's Mg + 2HCl example); the video; the mole-ratio buttons and the NH₃ pick (the rule is now in The mole ratio card, the misconception in Easy mistakes); the N₂ + 3H₂ masses pick (now the 2Mg + O₂ reveal table); the Think again choice (now Easy mistakes); the Sort "Which step is this line?" (now the three-step card); the "Not on this page" box (now Dive deeper: Where this goes next); the Key note.
- Kept: rFig at its first state; the triangle (record EQ_N); cfExamples and cfQuestions; Ks4Steps aie-w and aie-a.
- Key changes (options reworded with no `{stored}` text): Practice Q3, Q4, Q5 credited options.
- New id (stem changed): none. Rung prompts reworded: none.
- Text fix inside a slot: the aie-w Convert line "Nothing to convert — the mass of magnesium is already in grams throughout the calculation." became "Nothing to convert: the mass is in grams."
- Logic seam: `return Object.assign(c, {` rewritten for LEAN_PROPS, as on moles.

**Fixes after the examiner and blind checks (13 Nov).** EX = EXAMINER.md item; BLIND = blind pass. Where this list and the tables above disagree, this list is current.
- EX NOTE 1, taken as a fix: the Steps-attempt answer is "3.5 g of carbon dioxide" (2 s.f. data); the Fine-tune line keeps m(CO₂) = 3.52.
- BLIND: practice Q4 stem now "Mg + 2HCl → MgCl₂ + H₂. What is the Mr of hydrogen gas, H₂? Ar: H = 1." (it said "used in Step 3"). NEW ID.
