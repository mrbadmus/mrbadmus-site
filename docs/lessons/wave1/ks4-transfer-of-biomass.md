# transfer-of-biomass

Sources: AQA 8461 4.7.4.3 Transfer of biomass (biology only), read from `~/Desktop/Rainford/Curriculum/AQA/AQA-8461-SP-2016.pdf` (also checked against the `spec-8461.txt` in SCRATCH, which holds this section). Rainford SOW, Biology Unit 7, "Trophic levels in an ecosystem, transfer of biomass". Routes: TF, TH only (Triple only, no Combined page). No HT-only lines in 4.7.4.3. No required practical.

Kind: LEGACY (batch 10). The ladder (Ks4Practice rungs) and the practice set stay from the live page. The practice set is the hard-coded `BANK` in the legacy logic (it does not read `K.bank`), so every practice-set fix is a `logic_edits` pair, not a quiz JSON.

| Spec statement | Where it is covered | Route | Ticked |
|---|---|---|---|
| Describe pyramids of biomass | Card: Pyramids of biomass | TF TH | ✓ |
| Explain how biomass is lost between the different trophic levels | Card: Where the rest goes; Reveal: Egested or excreted?; Key fact | TF TH | ✓ |
| Producers are mostly plants and algae which transfer about 1% of the incident energy from light for photosynthesis | Card: Light into producers | TF TH | ✓ |
| Only approximately 10% of the biomass from each trophic level is transferred to the level above it | Card: About 10% is passed on (with the live page's figure, legacy-fig:lFig); Key fact | TF TH | ✓ |
| Losses: not all the ingested material is absorbed, some is egested as faeces | Card: Where the rest goes; Reveal | TF TH | ✓ |
| Losses: some absorbed material is lost as waste, such as carbon dioxide and water in respiration and water and urea in urine | Card: Where the rest goes; Reveal; Key fact | TF TH | ✓ |
| Large amounts of glucose are used in respiration | Card: Where the rest goes | TF TH | ✓ |
| MS 1c: calculate the efficiency of biomass transfers between trophic levels by percentages or fractions of mass | Card: Efficiency of biomass transfer (triangle:EQ_BIO); Card: Worked examples (cfifa: three examples, three questions); Easy mistakes; Dive deeper: Two transfers in a row | TF TH | ✓ |
| Explain how this affects the number of organisms at each trophic level | Card: Fewer organisms higher up | TF TH | ✓ |

SOW rows: "Calculate the efficiency of biomass transfer between trophic levels" ✓; "Explain what losses of biomass are due to" ✓. "Identify the trophic levels on food chains and pyramids" and "Construct and interpret pyramids of biomass from data" belong to the trophic-levels and pyramids-of-biomass lessons.

**Equation.** AQA gives no written equation for this (biology has no equation sheet); the spec only says "by percentages or fractions of mass". The record writes it the way the live page's own EQ_E, the other two worked examples and the ladder already do: efficiency = biomass at the next level ÷ biomass at this level, as a fraction, × 100 for a percentage. `EQ_BIO` is a copy of the legacy EQ_E so the triangle can sit inside a card.

**Worked example check.** Live first example (grass 2000 g/m², rabbits 160 g/m²): the numbers are right (160 ÷ 2000 = 0.08, 8%), but its Formula line said "current level" where every other line on the page says "this level", its Convert line had a dash tail, and its Insert line listed the values instead of inserting them. Replaced with `cfifa_first`, same numbers, same tab and `next`. The other two examples recomputed: 6 kg/m² = 6000 g/m², 480 ÷ 6000 = 0.08, 8% ✓; 100 ÷ 1000 = 1/10 ✓. The three CFIFA questions: 240 ÷ 3000 = 0.08, 8% ✓ (close line 3000 ÷ 240 = 12.5, 1250% ✓); 300 ÷ 2000 = 0.15, 15% ✓ (close 300 ÷ 2 = 150, 15 000% ✓); 0.12 × 1500 = 180 g/m² ✓, but its close line "1500 ÷ 12 = 125 divides; ..." was garbled, so it is rewritten. Steps worked: 2000 ÷ 20 000 = 0.1, 200 ÷ 2000 = 0.1, 0.1 × 0.1 = 0.01 = 1% ✓ (check 200 ÷ 20 000 = 0.01 ✓). Steps attempt: 400 ÷ 5000 = 0.08, 40 ÷ 400 = 0.1, 0.008 × 100 = 0.8% ✓ (check 40 ÷ 5000 = 0.008 ✓; close 5000 ÷ 400 = 12.5, 1250% ✓).

## Audit of the kept ladder and practice set

| Item | Verdict | Fix |
|---|---|---|
| Rung 1 Q1 (State ~10%) | ok | |
| Rung 1 Q2 (Give one way biomass is lost) | ok ("Lost as heat" is wrong for biomass; the reply says why, and the Easy mistakes card teaches it) | |
| Rung 2 Q1 (calc 300 ÷ 2500 = 12%) | ok, recomputed | |
| Rung 2 Q2 (calc 4 kg/m² → 4000 g/m², 360 ÷ 4000 = 9%) | ok, recomputed | |
| Rung 3 Q1 (chain: why chains rarely pass 4 or 5 levels) | ok; one forced order (10% passed on → little left after a few transfers → too little for another level). Now taught in "Fewer organisms higher up". | |
| Rung 3 Q2 (chain: grain vs beef) | ok; one forced order. Now taught in "Eating lower down the chain". | |
| Rung 4 (6-mark, foxes and rabbits) | Science ok. Level 3 text said "in the spec’s words" | logic_edits: level text without "spec" |
| CFIFA question 3 close line | garbled | logic_edits: "Do not divide by 12. Next level = efficiency as a decimal × this level = 0.12 × 1500." |
| Practice 1 "Why do intensive farming methods restrict farm animals' movement…" | Credited option 135 characters against at most 64, every option had a dash tail, and the feedback said "energy… retained as BIOMASS". Content is farming-techniques, but the live page teaches it, and the record now does too (card: Farm animals). | Stem kept (id kept). logic_edits replace all four options and three explanations. |
| Practice 2 (5000 → 500 g/m², 10%) | ok; recomputed | |
| Practice 3 (800 → 80 g/m², as a fraction 1/10) | ok | |
| Practice 4 (grain → cattle → people, 1%) | Credited option "1%: 10% of 10%" carried its working and was the longest | logic_edits: "1%" |
| Practice 5 "Explain how biomass is lost between a rabbit and the fox that eats it." | Credited option 113 characters against 18 to 41; "The fox leaves most of the rabbit uneaten" is a real loss, so arguable | Stem kept. logic_edits: credited "Egested as faeces, and lost in respiration and urine"; distractors "It is all turned into heat by the fox", "The fox gains more biomass than it eats", "None is lost: all the rabbit becomes fox". |

Chains: both ladder chains have one forced order; no `orders` needed.

**Gaps and mismatches.** The old generator page said energy and biomass interchangeably ("efficiency of energy transfer… about 10%"), listed "movement" as a fourth separate loss, and gave a split of the 90% ("60–70% respiration, 20–30% egestion"). None of that is AQA's wording and the split is not on the spec; it is gone. The legacy figure (lFig) is kept: its labels are right and it says on its face that the split is illustrative. Its band widths are decorative, not to scale.

**Removed or moved.** Removed from the live page: the hook scene (replaced by the record's Start here), the video embed, the "Which is egested?" pick (now the Egested or excreted? reveal), the Ks4Choice "over 100%" (now an Easy mistakes line), the Ks4Sort (its content is the reveal), the Key note (its lines are now cards and the Key fact), the Command words block (moved to Dive deeper). The two-step worked and attempt examples (Ks4Steps) moved to Dive deeper. The equation box's "efficiency (%) = decimal × 100" and "always divide the next level by this level" lines are now in the Efficiency card.
- Key changes (13 Nov fixes): these options were reworded with no `{stored}` text, so their answers get new keys, which the knowledge-point top-up re-places. Practice Q1 movement (quiz-TF-1, TF TH): credited option; Practice Q5 losses (quiz-TF-5, TF TH): three distractors.
- New id (stem changed): None.
- Builder: `cfifa_first` names `"eq": "EQ_E"` (the legacy constant); the triangle slot uses the record's `EQ_BIO`. Same content; confirm the builder resolves `EQ_E`.

**Fixes after the examiner and blind checks (13 Nov).** One line per finding (EX = examiner item number in EXAMINER.md, BLIND = blind/notes.md). Where this list and an audit row above disagree, this list is current.

- EX1 MUST practice Q1 (transfer-of-biomass#quiz-TF-1): credited option now "Less of the food is respired, so more becomes body mass" (edit #3 new text). KEY CHANGE.
- EX2 MUST practice Q5 (quiz-TF-5): distractors now "It is all turned into heat as the fox runs about", "The fox gains more biomass than the rabbit it eats", "None is lost: all of the rabbit’s biomass becomes fox" (edits #12–#14 new text, typographic apostrophe); replies kept (the heat reply says energy, not biomass, is lost as heat). KEY CHANGE (distractors).
- EX3 NOTE Q2 working in options: not applied (not wrong; recognising the right formula is a fair test, and it would change four answer keys for no accuracy gain).
- EX4 NOTE cfifa_first "eq": "EQ_E": left; flagged for the builder (EQ_E is the legacy constant, same content as EQ_BIO).
- EX5/EX6 NOTEs: md sentence on spec-8461 corrected; lFig kept.
