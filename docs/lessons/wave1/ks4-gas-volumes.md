# gas-volumes

Sources: AQA Chemistry 8462 4.3.5 Use of amount of substance in relation to volumes of gases, "(chemistry only) (HT only)", read from spec-8462-4.3.txt. There is no 8464 section for it, so the lesson exists on TH only, never Combined and never Foundation. Recall it needs: amount = mass ÷ Mr (8462 4.3.2.1) and the mole ratio from a balanced equation (4.3.2.2), both TH content with their own lessons. Rainford SOW Y11 Chem lesson 80 "(CHEM) Gas Calculations" (rainford_sow.py marks it `absent()`, "no platform subtopic"; this lesson is that page). NEW record, no legacy page (Ks4Practice, rungs from the record).

| Spec statement | Where it is covered | Route | Ticked |
|---|---|---|---|
| Equal amounts in moles of gases occupy the same volume under the same conditions of temperature and pressure. | Start here; Card: Equal moles, equal volumes (verbatim); Card: Gas volumes from a balanced equation; Key fact; Easy mistakes 2; Rung 1 (first); Rung 3 (second); Practice Q2 | TH | ✓ |
| The volume of one mole of any gas at room temperature and pressure (20 °C and 1 atmosphere pressure) is 24 dm³. | Card: One mole of gas at room temperature and pressure (verbatim); Card: cm³ and dm³ (24 000 cm³); Card: The equation (triangle EQ_V); Key fact; Rung 1 (both); Practice Q1, Q3 | TH | ✓ |
| The volumes of gaseous reactants and products can be calculated from the balanced equation for the reaction. | Card: Gas volumes from a balanced equation (verbatim, N₂ + 3H₂ → 2NH₃); Reveal table: Burning 50 cm³ of methane; Easy mistakes 4 and 5; Rung 3 (second, 2CO + O₂); Practice Q4 | TH | ✓ |
| Calculate the volume of a gas at room temperature and pressure from its mass and relative formula mass | Card: Volume from a mass (two steps, triangle EQ_N); cfifa Step 1 / Step 2 (8.8 g CO₂ → 0.2 mol → 4.8 dm³); cfifa Question 3 (3.2 g O₂); Rung 2 (second, 0.68 g NH₃); Practice Q5 | TH | ✓ |
| Calculate volumes of gaseous reactants and products from a balanced equation and a given volume of a gaseous reactant or product | Card: Gas volumes from a balanced equation (volume wanted = volume given × wanted ÷ given); Reveal table (100 cm³ O₂, 50 cm³ CO₂, water not a gas); Rung 3 (second: 80 cm³ CO → 40 cm³ O₂); Practice Q4 (40 cm³ H₂ → 20 cm³ O₂) | TH | ✓ |
| Change the subject of a mathematical equation | Card: The equation (amount = volume ÷ 24); triangle EQ_V; cfifa Moles from cm³ (n = V ÷ 24); cfifa Question 2 (9.6 dm³ → 0.4 mol); Practice Q3 | TH | ✓ |
| MS 1a decimal form; MS 1c ratios; MS 3b change the subject; MS 3c substitute with units | cfifa (decimals 0.015 mol, 0.096 dm³); every ratio item (1 : 3 : 2, 2 : 1, 1 : 1); the cm³/dm³ card and cfifa Question 4 (units carried, × 1000 at the end) | TH | ✓ |
| (Recall, 4.3.2.2, HT) a volume of gas from the MASS of a REACTANT and the balanced equation | Card: From the mass of a reactant to a volume of gas (5.0 g CaCO₃ → 1.2 dm³); Rung 3 (first, 1.3 g Zn → 0.48 dm³); Rung 4 (4.2 g NaHCO₃, 2 : 1 → 600 cm³) | TH | ✓ |

**Gaps and mismatches.**
- The spec gives no symbol and no equation sheet for this. The record writes it in words, "volume of gas (dm³) = amount of gas (mol) × 24", and gives it a triangle with 24 as a fixed value. It never names "molar volume" and never uses 22.4.
- The mass-of-a-reactant chain (last row) combines 4.3.5 with 4.3.2.2. It is not a separate spec bullet, but it is how AQA most often asks 4.3.5, and both halves are TH content. Listed in NOTES.md for Mide's check.
- Removed on the lead's ruling (examiner pass, 14 Nov 2026): the Dive deeper cards on gas volume changing with temperature and pressure, and on particle spacing. Both beyond 8462 4.3.5. "Room temperature and pressure" is written in full wherever a pupil reads it; "(RTP)" appears once, in the key word.
- No required practical. No figure: nothing on the page needs a diagram (a gas syringe is named, not drawn).

**Practice set source.** `K.bank(slug, R.route)`: the TH `quiz` list in subtopic_gas_volumes.py (five, all new, TH only).

| Route | Q | Origin | Note |
|---|---|---|---|
| TH | 1 | new | 2.5 mol → 60 dm³. Distractors 24 ÷ 2.5 = 9.6, 2.5 ÷ 24 = 0.10, 2.5 × 22.4 = 56 (feedback names only 24 dm³). |
| TH | 2 | new | Equal amounts in moles have equal volumes. Credited option 41 characters against 42, 40, 45. |
| TH | 3 | new | 120 cm³ → 0.12 dm³ → 0.005 mol. Distractors 120 ÷ 24 = 5, 0.12 × 24 = 2.88, 0.012 ÷ 24 = 0.0005 (÷ 10 000 slip; examiner pass replaced 1.2 ÷ 24 = 0.05 so the credited option is not the longest). |
| TH | 4 | new | 2H₂ + O₂ → 2H₂O(l), 40 cm³ H₂ → 20 cm³ O₂. Distractors 80 (inverted), 40 (1 : 1), 960 (× 24). |
| TH | 5 | new | 7.1 g Cl₂ (Mr 71) → 0.1 mol → 2.4 dm³. Distractors 0.1, 71 ÷ 7.1 × 24 = 240, 0.1 ÷ 24 = 0.0042. |

**Worked examples.** `cfifa` examples: 0.25 mol O₂ × 24 = 6 dm³; 360 cm³ ÷ 1000 = 0.36 dm³, 0.36 ÷ 24 = 0.015 mol; Step 1: 8.8 ÷ 44 = 0.2 mol; Step 2: 0.2 × 24 = 4.8 dm³. Questions gv-q1 1.5 × 24 = 36 dm³; gv-q2 9.6 ÷ 24 = 0.4 mol; gv-q3 3.2 ÷ 32 = 0.1 mol, 0.1 × 24 = 2.4 dm³; gv-q4 0.004 × 24 = 0.096 dm³ = 96 cm³.

**Ladder (Ks4Practice, 2·2·2·1, new).**

| Item | Verdict |
|---|---|
| Rung 1 (first) volume of one mole at RTP | 24 dm³; distractors 24 cm³, "depends on the gas". Credited not the longest. |
| Rung 1 (second) AQA's RTP | 20 °C and 1 atmosphere; distractors 0 °C / 1 atm, 20 °C / 24 atm. Credited not the longest. |
| Rung 2 (first) 0.75 mol CO₂ | 0.75 × 24 = 18 dm³. Convert: nothing to convert (answer asked in dm³). |
| Rung 2 (second) 0.68 g NH₃, Mr 17 | 0.68 ÷ 17 = 0.04 mol; 0.04 × 24 = 0.96 dm³. Convert: mass to moles first, divide by Mr. |
| Rung 3 (first) 1.3 g Zn, Zn + 2HCl → ZnCl₂ + H₂ | 1.3 ÷ 65 = 0.020 mol; 1 : 1; 0.020 × 24 = 0.48 dm³. One order: each link uses the number the one before it works out. Zinc, not magnesium: Ar of Mg is 24, so a magnesium mass in g always equals the hydrogen volume in dm³, which hides the method. |
| Rung 3 (second) 2CO + O₂ → 2CO₂, 80 cm³ CO | ratio 2 : 1; same ratio by volume ("also" needs the link before it); 80 × 1 ÷ 2 = 40 cm³. One order. |
| Rung 4 (4 marks, points-marked) 4.2 g NaHCO₃ | 4.2 ÷ 84 = 0.050 mol; 2 : 1 → 0.025 mol CO₂; 0.025 × 24 = 0.60 dm³; × 1000 = 600 cm³. 2NaHCO₃ → Na₂CO₃ + H₂O + CO₂ balanced (Na 2, H 2, C 2, O 6). |

**Equations balanced.** N₂ + 3H₂ → 2NH₃; CH₄ + 2O₂ → CO₂ + 2H₂O; CaCO₃ + 2HCl → CaCl₂ + H₂O + CO₂; Zn + 2HCl → ZnCl₂ + H₂; 2CO + O₂ → 2CO₂; 2NaHCO₃ → Na₂CO₃ + H₂O + CO₂; 2H₂ + O₂ → 2H₂O.

**Assignment pool.** 12 rows, ks4-gas-volumes-e01..e04, s01..s04, h01..h04 (bank positions 0–11), tier higher, triple_only True. None restates a page `quiz` item, the `fifas` example (8.8 g CO₂) or a cfifa number.

**IDs.** All new: the page, its five quiz items, cfifa questions gv-q1..gv-q4, the ladder and the 12 bank rows. Nothing kept, changed or retired.
