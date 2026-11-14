# mass-changes-reactions

Sources: AQA 8464 5.3.1.3 (CF CH) and 8462 4.3.1.3 (TF TH), "Mass changes when a reactant or product is a gas", read from spec-8464.txt and spec-8462.txt. Same wording in both; skills AT 1, 2, 6 (investigating mass changes). No HT-only or chemistry-only lines. Rainford SOW lesson "Conservation of mass and balancing equations" (explain why there can be an apparent loss or gain in mass; the calcium carbonate and acid demo). LEGACY page (batch 11, Ks4Practice 2·2·2·1).

| Spec statement | Where it is covered | Route | Ticked |
|---|---|---|---|
| Some reactions may appear to involve a change in mass but this can usually be explained because a reactant or product is a gas and its mass has not been taken into account | Card: Mass is still conserved; Key fact; Rung 1 Q1; Quiz Q1, Q3, Q4 | CF CH TF TH | ✓ |
| When a metal reacts with oxygen the mass of the oxide produced is greater than the mass of the metal | Card: When the reading rises; Card: Use the balanced equation; Easy mistakes; Rung 1 Q2; Rung 3 chain 2; Rung 4; Quiz Q2, Q5 (Foundation) | CF CH TF TH | ✓ |
| In thermal decompositions of metal carbonates carbon dioxide is produced and escapes into the atmosphere leaving the metal oxide as the only solid product | Card: When the reading falls (legacy-fig:bFig); Card: Use the balanced equation; Reveal; Rung 4; Quiz Q1 | CF CH TF TH | ✓ |
| Explain any observed changes in mass in non-enclosed systems during a chemical reaction given the balanced symbol equation for the reaction | Card: Use the balanced equation; Card: When the reading stays the same; Reveal: Falls, rises or stays the same; Rung 3; Rung 4 | CF CH TF TH | ✓ |
| ... and explain these changes in terms of the particle model | Card: Explaining it with particles; Rung 3 chains 1 and 2; Rung 4 | CF CH TF TH | ✓ |
| AT 1, 2, 6: investigating mass changes with a balance | Card: The mass of gas (cfifa); Rung 2 | CF CH TF TH | ✓ |
| 5.3.2.2 / 4.3.2.2 (HT only): masses from the balanced equation | Dive deeper: Predicting the mass gained (routes CH TH; steps-worked, steps-attempt); Quiz Q5 on Higher routes | CH TH | ✓ |

**Gaps and mismatches.** The old page's hook was an open bottle of fizzy drink losing mass. That is dissolved gas escaping, not a chemical reaction, so it does not show the spec point; the new Start here uses marble chips and acid. The spec's own example, thermal decomposition of a metal carbonate, was only in the practice set; it is now a card.

**Practice set source.** The page's own hard-coded bank: `(F.H ? htBank : baseBank).map((q) => K.item(q))`. baseBank (Foundation routes) is five questions; htBank (Higher routes) is baseBank's first four plus a moles question. It does not read the subtopic `quiz` list, so fixes are logic_edits and there is no quiz-mass-changes-reactions.json.

**Audit of the ladder, worked examples and practice set.**

| Item | Verdict |
|---|---|
| Rung 1 Q1 Why the reading falls in an open flask | ok |
| Rung 1 Q2 Mass of a metal heated in air | ok |
| Rung 2 calc 1: 210.50 g → 208.30 g | ok for the answer (2.20 g). Fault: the unit chips (g, kg, mol) and a Convert choice "Convert g to mol" put moles, Higher only, on every route. Fix (logic_edits): chips g, kg, cm³; choice "Convert kg to g". Same correct choice (index 0) and unit. |
| Rung 2 calc 2: 0.3 kg → 298 g | ok (2 g). Same unit chip fix. |
| Rung 3 chain 1 Open flask, marble chips | ok. One forced order: the gas must be made before it spreads out, and the reading falls because it left. |
| Rung 3 chain 2 Magnesium in an open crucible | ok. One forced order: the reaction, then the oxygen joining, then the reading. |
| Rung 4 Copper rises, CaCO₃ falls, 6 marks | ok |
| CFIFA example 1: 152.40 g → 150.20 g | ok (2.20 g) |
| CFIFA example 2: 0.5 kg → 487 g | ok (13 g) |
| CFIFA example 3: 24.00 g → 26.40 g | ok (2.40 g gained) |
| CFIFA Q1: 98.75 g → 97.65 g | ok (1.10 g) |
| CFIFA Q2: 0.2 kg → 196 g | ok (4 g) |
| Higher steps-worked: 4.8 g Mg | ok (0.2 mol; 0.1 mol O₂; 3.2 g; MgO 8.0 g; check 4.8 ÷ 48 × 80 = 8.0) |
| Higher steps-attempt: 2.4 g Mg | ok (0.1 mol; 0.05 mol O₂; 1.6 g; MgO 4.0 g) |
| Higher hExamples / hQuestions (4.8 g, 0.1 mol O₂, 12 g, 0.25 mol O₂) | ok (0.2 mol, 3.2 g, 0.5 mol, 8 g). Not placed on the lean page. |
| Quiz Q1 CaCO₃ in an open crucible | ok |
| Quiz Q2 Iron rusting | Fault: rust forms only with water and oxygen, so the distractor "Water from humidity ... adding extra mass" was arguably right, and the feedback's 4Fe + 3O₂ → 2Fe₂O₃ is not the rusting reaction. Rusting is not this spec point. Fix (logic_edits): "Why does the mass of magnesium ribbon increase when it burns in air?" / "Oxygen from the air joins the magnesium" / "Heat is added, and heat has mass" / "Hot atoms are heavier than cold atoms" / "The magnesium gives off a gas". NEW ID. Both banks. |
| Quiz Q3 120.60 g → 119.50 g | ok (1.10 g; 240.10 is the sum) |
| Quiz Q4 Sealed flask | Fault: the credited option was visibly the longest (51 against 20 to 29). Fix: "It stays the same: no gas can leave" / "It falls, because a gas is made" / "It rises, because a gas is made" / "It falls at first, then rises again". Stem and feedback kept. KEY CHANGE. |
| Quiz Q5 (Foundation) Copper heated in air | Fault: the credited option was visibly the longest (95 against 28 to 40). Fix: "Oxygen particles bond to the copper atoms". Stem, distractors and feedback kept. KEY CHANGE. |
| Quiz Q5 (Higher) 0.2 mol Mg, moles of O₂ | ok (0.1 mol) |

**Removed or moved.**
- Removed: the fizzy-drink hook (see Gaps); the three tap cards (open, sealed, metal in air; now three cards); the four predict-the-reading scenarios and the Sort (now the reveal table); the Think again on burning magnesium (now an Easy mistake); the Higher moles layer with its triangle and CFIFA (now Dive deeper, the two Step widgets only, routes CH TH); the Key note; the video; the command words (now Dive deeper).
- Kept: `legacy-fig:bFig`, two flasks of marble chips and acid on balances: open, reading 152.40 g then 150.20 g with carbon dioxide leaving; sealed with a bung, 152.40 g then 152.40 g. Checked against its drawer: it is static (no state), and the readings match CFIFA example 1.
- Key changes (options reworded with no `{stored}` text, so their answers get new keys): Quiz Q4 (all four options), Quiz Q5 Foundation (credited option).
- New id (stem changed): Quiz Q2 (both banks).
- Rung prompts reworded, position kept (id kept): mass-changes-reactions r2 calc 1 and calc 2 (unit chips; calc 1's third Convert choice). No prompt wording changed.

**Builder seams for the lead (not fixable by logic_edits).**
- `const done = F.H ? [ ... ] : [ ... ];` is not matched by lean_ks4's `const done = \[[^\n]*\];`, so the build stops at "cannot find the rail done[] array".
- The spec eyebrow is the template literal "AQA Chemistry 5.3.1.3 · Combined and Triple": the Triple routes show the 8464 number. 8462's number is 4.3.1.3. lean_ks4's eyebrow rules cover physics and biology only.

**Words.** Old Design page prose about 605 (old generator theory 418). New knowledge + key fact + Dive deeper about 637.

**Fixes after the examiner and blind checks (13 Nov).** EX = EXAMINER.md item; BLIND = blind pass. Where this list and the tables above disagree, this list is current.
- EX SHOULD 1: practice Q1 wrong_explanations rewritten (logic_edits; both banks). Stem and options kept.
- EX SHOULD 2: the kilogram readings are now 0.300 kg (rung 2 calc 2), 0.500 kg (CFIFA example 2) and 0.200 kg (CFIFA Q2). Answers unchanged. Rung id kept; CFIFA ids are explicit.
- EX NOTE 3: the unit-chip edit is split into two pairs (one per calc rung), so every logic_edits target now occurs exactly once.
- BLIND: practice Q4 stem now "Marble chips react with acid in a sealed flask. What happens to the balance reading?" (it said "The same reaction", leaning on Q3). Both banks. NEW ID.
