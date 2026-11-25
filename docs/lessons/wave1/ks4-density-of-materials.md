# density-of-materials

Sources: AQA 8464 6.3.1.1 + Required practical activity 17 (CF CH) / 8463 4.3.1.1 + Required practical activity 5 (TF TH); the content is word for word the same, only the practical's number differs. Read from the 2016 specification PDFs on Mide's Mac (AQA-8464-SP-2016.pdf v1.1, AQA-8463-SP-2016.pdf v1.1). No HT-only or physics-only line. Skills: MS 1a, b, c, 3b, c; WS 1.2; AT 1. Rainford KS4 SOW, Year 10 Physics lessons 18 "Density" and 19 "Density RP"; Physics LO sheet: explain why some materials float on water; calculate density; appropriate significant figures; measure the density of a solid and a liquid; evaluate the measurement.
Routes: CF CH TF TH.
Legacy status: none (old generate_site_v5 page; no Design batch holds this slug). NEW lean FULL record. Eyebrow derived: "AQA Combined Science (8464) 6.3.1.1 · Quantitative" / "AQA Physics (8463) 4.3.1.1 · Quantitative".

| Spec statement (AQA wording) | Where it is covered | Route | Flag | Ticked |
|---|---|---|---|---|
| The density of a material is defined by the equation: density = mass / volume, ρ = m / V (density, ρ, in kilograms per metre cubed, kg/m³; mass, m, in kilograms, kg; volume, V, in metres cubed, m³). | Card 'What density means' (AQA words, units, triangle); Key fact; Rung 1 (first); Practice Q1, Q3, Q4 | CF CH TF TH | all | ✓ |
| Students should be able to recall and apply this equation to changes where mass is conserved (MS 1a, b, c, 3b, c). | Card 'What density means' ("You need to remember this equation"); worked examples 1-3; Your turn 1-2; Card 'When the mass stays the same' (air squeezed: same mass, new volume, new density); Rung 2 (second, calc); Rung 3 (second) | CF CH TF TH | all | ✓ |
| The particle model can be used to explain the different states of matter and differences in density. | Card 'Density and the particle model' (AQA words, fig:particle-states); Reveal 'Solid, liquid and gas'; Key fact; Rung 1 (second); Rung 2 (first); Rung 3 (second) | CF CH TF TH | all | ✓ |
| Students should be able to recognise/draw simple diagrams to model the difference between solids, liquids and gases (WS 1.2). | fig:particle-states (drawn, not described); Reveal 'Solid, liquid and gas' | CF CH TF TH | all | ✓ |
| Students should be able to explain the differences in density between the different states of matter in terms of the arrangement of atoms or molecules (WS 1.2). | Card 'Density and the particle model'; Reveal (How close, Arrangement, Density); Rung 2 (first: steam and water); Rung 3 (second: gas and solid); Practice Q2 (ice) | CF CH TF TH | all | ✓ |
| Required practical (8464 RP 17 / 8463 RP 5): use appropriate apparatus to make and record the measurements needed to determine the densities of regular and irregular solid objects and liquids. Volume should be determined from the dimensions of regularly shaped objects, and by a displacement technique for irregularly shaped objects. Dimensions to be measured using appropriate apparatus such as a ruler, micrometer or Vernier callipers (AT 1). | Card 'The displacement method' (fig:displacement-volume); Card 'Required practical 17: density' (CF CH) and 'Required practical 5: density' (TF TH): regular solid (ruler, Vernier callipers, micrometer), irregular solid (displacement), liquid (balance and measuring cylinder), meniscus; Rung 3 (first); Rung 4; Practice Q5; worked example 2 (the stone in the figure) | CF CH TF TH | all; each route's own RP number | ✓ |

**Equations and units.**

| Equation (AQA words) | Symbols | Units | Recall or apply | Equation sheet (8463) |
|---|---|---|---|---|
| density = mass / volume | ρ = m / V | ρ in kg/m³; m in kg; V in m³ | recall and apply | Not on the sheet: recall list, equation 23 |

**Faults in the current pages and data.**
- The old `rp` field and theory call the practical "RP17 (Physics)" on every route. That is the 8464 number; 8463 numbers it Required practical activity 5. Each lean card carries its own route's number. The data field is not rendered on the lean page and is left as it is.
- Old common mistake "Convert to kg/m³ by multiplying by 1000" (from g/cm³): right, but the old page gave no conversion for volume alone; the lean 'Units' card gives 1 m³ = 1 000 000 cm³ and 1 g/cm³ = 1000 kg/m³.
- Old quiz options carried their own working ("0.8 g/cm³ — ρ = m ÷ V = 800 ÷ 1000"), which gave the answer away, and the ice option was far the longest. Options rewritten; stems kept.

**Gaps and mismatches.**
- None in the content lines. The old page never drew a particle diagram, which the spec asks pupils to recognise and draw: fig:particle-states is new (figlib/ks4lean_pm.py).
- Rainford LO "Explain why some materials will float on water" is not in 6.3.1.1 / 4.3.1.1 (floating is 8463 4.5.5.1.2, physics only, HT only). It is in Dive deeper only, with ice and steel as the examples; Practice Q2 (ice floats, kept stem) is answered from the density card.

**Unsure (left out until checked).**
- "Ice is about 920 kg/m³": the record uses a rounded value (917 kg/m³ at 0 °C). The old page's 917 is more precise; 920 is used so the number reads as an approximation.
- Rung 2 (first) and Rung 3 (second) say a gas has a much lower density "than the solid/liquid of the same substance". True for every substance GCSE uses; not checked for every substance.

**Removed or moved.**
- Pupil walk at 390 px (24 Nov 2026): the card states ρ = m ÷ V once in symbols and the Key fact once in words (the RP card's three "Then density = mass ÷ volume" lines became one closing line); Rung 2's conversion options say "the rise in volume" (no longer giving away 120 − 40); soft hyphens in the reveal table; no-break spaces in numbers and units.
- Removed: "Denser materials have heavier atoms or more tightly packed structures" (gold, aluminium, polystyrene); air "~800× less dense than water"; the density table of water, aluminium, iron, air, gold. None is in the spec.
- Removed: the classic matching activity (ks4c:density-of-materials:match-1..4).
- Removed: the old sources-of-error list as a list; meniscus at eye level is in the practical card, air bubbles and a better value are in Dive deeper.
- Moved to Dive deeper: floating and sinking (Rainford LO, not AQA 4.3.1.1).

**Practice set source.** `K.bank(slug, R.route)`: the route's `quiz` list in all_subtopics_physics*.py. Five per route, the same on every route; correct option first (the build shuffles).

| Q | Origin | ks4q: id | Stem | Credited |
|---|---|---|---|---|
| 1 | kept (stem unchanged, options rewritten) | `9058edbf67` | A liquid has mass 800 g and volume 1000 cm³. What is its density in g/cm³? | 0.8 g/cm³ |
| 2 | kept (stem unchanged, options rewritten) | `043ca445a6` | Why does ice float on water? | Ice is less dense than liquid water |
| 3 | new | `6bd25e1140` | Which unit is used for density when the mass is in kg and the volume is in m³? | kg/m³ |
| 4 | new | `5a78ff9878` | A block has a mass of 2.0 kg and a volume of 0.0010 m³. What is its density? | 2000 kg/m³ |
| 5 | new | `63f9fc0d3a` | How can you find the volume of an irregular stone? | Lower it into water in a measuring cylinder and find the rise in volume |

**Ladder (Ks4Practice, 2·2·2·1, new).**

| Item | Prompt | Answer |
|---|---|---|
| Rung 1 (first) mcq | State the equation that links density, mass and volume. | density = mass ÷ volume |
| Rung 1 (second) mcq | Identify the state of matter that has the lowest density for the same substance. | Gas |
| Rung 2 (first) mcq | Explain why steam has a much lower density than the same mass of liquid water. | Its particles are far apart, so the same mass takes up a bigger volume |
| Rung 2 (second) calc | A stone of mass 0.24 kg raises a measuring cylinder from 40 cm³ to 120 cm³. Density in kg/m³. | 3000 kg/m³ (convert 80 cm³ ÷ 1 000 000) |
| Rung 3 (first) chain | The mass of a stone has been measured. Describe how to find its volume, and then its density. | read volume → lower stone, read new volume → rise is the volume, density = mass ÷ volume |
| Rung 3 (second) chain | Explain why a substance has a much lower density as a gas than as a solid. | mass stays the same → particles far apart, bigger volume → ρ = m ÷ V, lower density |
| Rung 4 (first) write | Describe how to determine the density of a liquid, using a balance and a measuring cylinder. | 5 marking points |

Every chain has one right order: each link uses what the link before it established.

**Worked examples (CFIFA, new).** 5.4 kg in 0.0020 m³ → 2700 kg/m³; the stone in the figure, 30 g in 12 cm³ → 2500 kg/m³ (check 2.5 g/cm³); mass of 0.25 m³ of water → 250 kg. Your turn: 0.84 kg in 0.0010 m³ → 840 kg/m³; a 2.0 cm cube of mass 72 g → 9.0 g/cm³ (closing line: 9000 kg/m³, about the density of copper). The worked examples sit straight after 'The displacement method', so the conversions and the stone come before the examples that use them.

**Assignment pool.** 64 rows for this slug in ks4_data/questions/physics/particle_model*.py (12 at positions 0–11, the auto window). None is changed here.
