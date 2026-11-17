# conservation-of-mass

Sources: AQA 8464 5.3.1.1 (CF CH) and 8462 4.3.1.1 (TF TH), "Conservation of mass and balanced chemical equations", read from spec-8464.txt and spec-8462.txt. The wording is the same in both. No HT-only or chemistry-only lines. Linked statements used: 5.2.2.2 / 4.2.2.2 State symbols and 5.1.1.1 / 4.1.1.1 (write word equations and balanced equations), from full-8464.txt / full-8462.txt. Rainford SOW lesson "Conservation of mass and balancing equations" (describe how the mass of reactants compares with the mass of products; write balanced symbol equations including state symbols; key words mass, reactants, products, state; the lead nitrate + potassium iodide demo). LEGACY page (batch 3, Ks4Ladder).

| Spec statement | Where it is covered | Route | Ticked |
|---|---|---|---|
| The law of conservation of mass states that no atoms are lost or made during a chemical reaction so the mass of the products equals the mass of the reactants | Card: The law of conservation of mass; Card: Using it to find a missing mass; Key fact; Rung 1; Rung 3; Quiz Q1, Q2 | CF CH TF TH | ✓ |
| Chemical reactions can be represented by symbol equations which are balanced in terms of the numbers of atoms of each element involved on both sides of the equation | Card: Balanced symbol equations; Card: Balancing, step by step; Easy mistakes; Rung 4; Quiz Q3, Q5 | CF CH TF TH | ✓ |
| Understand the use of the multipliers in equations in normal script before a formula and in subscript within a formula | Card: Big numbers and small numbers; Reveal: Count the atoms; Easy mistakes; Quiz Q4 | CF CH TF TH | ✓ |
| 5.2.2.2 / 4.2.2.2: state symbols (s), (l), (g), (aq); include appropriate state symbols in equations | Card: Word equations, symbol equations and state symbols; Rung 4; Dive deeper: Seeing it on a balance | CF CH TF TH | ✓ |
| 5.1.1.1 / 4.1.1.1: write word equations; write formulae and balanced chemical equations | Card: Word equations, symbol equations and state symbols; Rung 4 | CF CH TF TH | ✓ |
| Calculating a missing mass from conservation of mass (the page's CFIFA, all tiers) | Card: Using it to find a missing mass; Card: Worked examples (cfifa); Rung 2 | CF CH TF TH | ✓ |
| (SOW) precipitation on a balance: no change in mass | Dive deeper: Seeing it on a balance | CF CH TF TH | ✓ |
| 5.3.2.2 / 4.3.2.2 (HT only): equations interpreted in moles | Dive deeper: The big numbers are amounts in moles (routes CH TH). Taught in amounts-in-equations. | CH TH | ✓ |

**Gaps and mismatches.** The old generator data for CH and TH carried a `higher` note on theoretical yield and atom economy. That is 4.3.3 (chemistry only), so it was wrong on Combined Higher and wrong for this lesson on every route; it is not carried. The SOW's "apparent loss / gain in mass" belongs to mass-changes-reactions (5.3.1.3 / 4.3.1.3), and is taught there.

**Practice set source.** `K.bank(slug, R.route)`: the route's `quiz` list. Fixes are in quiz-conservation-of-mass.json. The old list had three questions on every route, identical across routes. All three are correct and on-spec for every route, so all three are kept verbatim. Two new questions (identical on every route) make five.

**Ladder.** Ks4Ladder, one item per rung. Rung 2 is tier-split in the logic (`higher ?`): Higher sees the methane calculation, Foundation the copper carbonate one, under the same rung id. Both test all-tier content.

**Audit of the ladder, worked examples and practice set.**

| Item | Verdict |
|---|---|
| Rung 1 State the law | ok |
| Rung 2 Foundation: 6.2 g CuCO₃ → 4.0 g CuO + CO₂ | ok for the answer (2.2 g; checked against Mr: 6.2 × 79.5 ÷ 123.5 = 4.0 g CuO). Fault: the unit chips offered "mol" and "g/mol", Higher-only units, on Foundation. Fix (logic_edits): chips g, kg, cm³, g/dm³. Same answer and unit. |
| Rung 2 Higher: CH₄ + 2O₂, 0.16 kg → 0.44 kg + 0.36 kg | ok (160 + O₂ = 440 + 360, O₂ = 640 g) |
| Rung 3 chain: sealed flask | Fault: links 1 and 2 were two separate facts (atoms rearranged; flask sealed), so both orders were right. Fix (logic_edits): link 2 now starts "So the products contain exactly the same atoms ... and the sealed flask stops any of them getting in or out". One forced order. Herrings kept. |
| Rung 4 Mg + 2HCl with state symbols, 4 marks | ok (Mg(s) + 2HCl(aq) → MgCl₂(aq) + H₂(g); balanced) |
| CFIFA example 1: 25.0 g CaCO₃ → 14.0 g CaO | ok (11.0 g; matches Mr 100 : 56 : 44) |
| CFIFA example 2: 1.20 kg Mg → 2.00 kg MgO | ok (800 g; matches 48 : 80) |
| CFIFA Foundation Q1: 12.5 g ZnCO₃ → 8.1 g ZnO | ok (4.4 g; Mr 125 : 81 : 44) |
| CFIFA Foundation Q2: 0.84 kg MgCO₃ → 400 g MgO | ok (440 g; Mr 84 : 40 : 44) |
| CFIFA Higher Q1: 16.8 g NaHCO₃ → 10.6 g + 1.8 g | ok (4.4 g; 2 × 84 : 106 : 18 : 44) |
| CFIFA Higher Q2: Fe₂O₃ + 3CO, 1.60 kg + 840 g → 1.12 kg Fe | ok (1320 g; 160 : 84 : 112 : 132) |
| Quiz Q1 Why balance (kept) | ok |
| Quiz Q2 24 g Mg → 40 g MgO (kept) | ok (16 g) |
| Quiz Q3 4Fe + 3O₂ → 2Fe₂O₃ (kept) | ok (each distractor recounted: unbalanced) |
| Quiz Q4 Atoms in 3CO₂ (new) | ok |
| Quiz Q5 H₂O₂ is a changed formula (new) | ok (H₂ + O₂ → H₂O₂ is atom-balanced, so the only fault is the formula) |

**Removed or moved.**
- Removed: the sealed-flask animation and its atom-count picks (now Big numbers and small numbers, and the Count the atoms reveal); the Think again "three molecules become two" (now an Easy mistake); the three-move Word to symbol activity, including the state-symbol picker (now the Word equations, symbol equations and state symbols card); the equation panel (now Using it to find a missing mass); the Key note; the video; the Command words grid (now in Dive deeper).
- Not kept: `flaskFig`. It is drawn from the animation state (at its first state it shows only the reactant atoms), and its div carries `max-width: 520px`, so it is not the builder's figure div.
- Moved to Dive deeper: the moles reading of the big numbers (routes CH TH only; the old page showed it on every Higher route under the explainer); command words.
- Key changes: none (no practice option reworded).
- New id (stem changed): none. New questions: Q4, Q5 (identical on every route).
- Rung prompts reworded, position kept (id kept): conservation-of-mass#r3 (links), conservation-of-mass#r2 (Foundation unit chips only).
- Logic: the Ks4End `legal` line (about the flask animation) is cleared by the builder, since no legacy figure slot is used.

**Words.** Old Design page prose about 511 (old generator theory 371). New knowledge + key fact + Dive deeper about 657.

**Fixes after the examiner and blind checks (13 Nov).** EX = EXAMINER.md item; BLIND = blind pass. Where this list and the tables above disagree, this list is current.
- EX SHOULD 1: practice Q1, Q2 and Q3 (kept items) get plain wrong_explanations in quiz-conservation-of-mass.json, every route (12 items). Stems and options unchanged: ids and keys survive.
