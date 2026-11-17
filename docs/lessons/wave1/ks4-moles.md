# moles

Sources: AQA Combined Science Trilogy 8464 5.3.2.1 Moles (HT only), read from spec-8464.txt (CH), and AQA Chemistry 8462 4.3.2.1 Moles (HT only), read from spec-8462.txt (TH). The two are word for word the same. The lesson exists on CH and TH only, so every card, rung and practice question is Higher content and no route gating is needed. Neither spec writes the moles relation as an equation; the record uses "number of moles = mass (g) ÷ Mr", the form in this unit's brief, with n = m ÷ Mr beside it. Rainford SOW "Moles": (HT) calculate the number of moles given the mass, or the mass given the number of moles; use Avogadro's constant. LEGACY page (batch 11).

| Spec statement | Where it is covered | Route | Ticked |
|---|---|---|---|
| Chemical amounts are measured in moles. The symbol for the unit mole is mol. | Card: The mole (verbatim); Key fact; Rung 1 | CH TH | ✓ |
| The mass of one mole of a substance in grams is numerically equal to its relative formula mass. | Card: The mole (verbatim, three examples, legacy-fig:pFig); Key fact; Rung 1 Q2; Rung 3 chain 2; Easy mistakes | CH TH | ✓ |
| One mole of a substance contains the same number of the stated particles, atoms, molecules or ions as one mole of any other substance. | Card: The Avogadro constant (verbatim); Start here; Rung 3 chain 2 | CH TH | ✓ |
| The number of atoms, molecules or ions in a mole of a given substance is the Avogadro constant. The value of the Avogadro constant is 6.02 × 10²³ per mole. | Card: The Avogadro constant (verbatim); Card: Particles from moles (triangle:EQ_P); Key fact; Rung 1 Q1; Rung 4 | CH TH | ✓ |
| Amounts in moles can apply to atoms, molecules, ions, electrons, formulae and equations; one mole of C has the same number of atoms as one mole of CO₂ has molecules | Card: The Avogadro constant (verbatim, with AQA's example); Card: Say which particle you are counting; Easy mistakes; Practice Q5 | CH TH | ✓ |
| Use the relative formula mass of a substance to calculate the number of moles in a given mass of that substance and vice versa (MS 1c) | Card: Moles from mass (triangle:EQ_N); Card: Worked examples (cfifa); Card: Between a mass and a number of particles (steps-worked, steps-attempt); Rung 2; Rung 3 chain 1; Rung 4; Practice Q1 to Q4 | CH TH | ✓ |
| MS 1a decimal form, MS 1b standard form, MS 2a significant figures | Card: Standard form; cfifa examples 4 and 5, questions 4 and 5; Rung 4 ("Give your answer in standard form"); Dive deeper: Command words | CH TH | ✓ |
| MS 3b change the subject of an equation | triangle:EQ_N and EQ_P (tap to find); cfifa example 3 and question 3 (m = n × Mr); Dive deeper: Finding Mr from moles | CH TH | ✓ |
| MS 3a understand and use the symbols =, <, <<, >>, >, ∝, ~ | Not taught. A skills opportunity, not content; see Gaps | CH TH | gap noted |
| (SOW) calculate moles from mass and mass from moles; use Avogadro's constant | as above | CH TH | ✓ |

**Gaps and mismatches.**
- MS 3a (the symbols <, <<, ∝, ~) is listed against 4.3.2.1 as a skills opportunity. Neither the old page nor this one teaches it. I did not add it: nothing in the content statement needs it.
- The legacy header eyebrow is the literal "AQA Chemistry 5.3.2.1 · Higher only". On TH that is the Combined number; the Triple number is 4.3.2.1. lean_ks4 has eyebrow rules for physics (6.x to 4.x) and biology only, so the literal stays as it is on both routes. Builder item for the lead: a chemistry rule 5.3.x to 4.3.x (same sub-numbers in this unit).
- The old generator page taught percentage by mass here. That is 5.3.1.2 / 4.3.1.2 (Relative formula mass), so it stays out of this lesson (Dive deeper points to it).
- The old generator page said the mole was chosen because 12 g of carbon-12 is one mole, and gave units "mol⁻¹" and "molar mass in g/mol". None of these is on either spec. Left out.

**Practice set source.** The page's own `BANK` (`BANK.map((q) => K.item(q))`), the same five on CH and TH. It does not read the subtopic `quiz` list, so fixes are `logic_edits` and there is no quiz-moles.json. No stem edited, so all five practice ids survive.

**Worked examples.** The legacy page split its CFIFA into two blocks (cf1 and cf2), so the `cfifa` slot had nothing named `cfExamples` to reuse. The record carries its own `cfifa`: the same five examples and five questions, ids mol-q1, mol-q2, mol-q3, mol-p1, mol-p2 kept. Two text changes from the legacy copy: the first Convert line lost its dash aside ("Nothing to convert: the mass is in grams." with the note "Ar has no unit."), and Formula lines use n = m ÷ Ar for an element throughout. Every number rechecked: 27 ÷ 27 = 1; 2700 ÷ 27 = 100; 0.25 × 100 = 25; 2 × 6.02 = 12.04 so 1.204 × 10²⁴; 3.01 ÷ 6.02 = 0.5; 9 ÷ 18 = 0.5; 500 ÷ 100 = 5; 2 × 44 = 88; 0.1 × 6.02 = 0.602 so 6.02 × 10²²; 12.04 ÷ 6.02 = 2. Steps slots (legacy mol-w1, mol-a): 3.01 × 10²³ ÷ 6.02 × 10²³ = 0.5, 0.5 × 40 = 20 g; 4.4 ÷ 44 = 0.1, 0.1 × 6.02 × 10²³ = 6.02 × 10²². Cards: 3 × 6.02 = 18.06 so 1.806 × 10²⁴; 20 ÷ 0.5 = 40.

**Figure.** legacy-fig:pFig kept. Read its drawer: three one-mole piles labelled carbon, C (Ar 12, 12 g, 6.02 × 10²³ atoms), water, H₂O (Mr 18, 18 g, molecules), sodium chloride, NaCl (Mr 58.5, 58.5 g, formula units), with the caption "different masses, the same number of particles". All values right; pile size grows with mass. It is static (no state), so the first render is the whole figure.

**Audit of the ladder and practice set.**

| Item | Verdict |
|---|---|
| Rung 1 Q1 Particles in one mole | ok (6.02 × 10²³; distractors are 0.1 mol and 2 mol) |
| Rung 1 Q2 Mass of one mole of water | ok (18 g) |
| Rung 2 calc 1 9.8 g H₂SO₄ | ok (0.1 mol) |
| Rung 2 calc 2 0.2 mol MgO | ok for the answer (8 g). Fault: the Convert choice "Convert mol to g" was not definitely wrong (the whole calculation goes from mol to g). Fix: "Convert g to kg"; same index, same answer. |
| Rung 3 chain 1 Molecules in 22 g of CO₂ | ok. One order: "Then" and "So multiply: 0.5 ×" need the links before them. 22 ÷ 44 = 0.5; 0.5 × 6.02 × 10²³ = 3.01 × 10²³. |
| Rung 3 chain 2 Same number, different masses | ok. One order ("But", then the worked case). |
| Rung 4 Atoms in 0.048 kg Mg, 4 marks | ok. 48 ÷ 24 = 2; 2 × 6.02 × 10²³ = 1.204 × 10²⁴. Levels and rejects right. |
| Practice Q1 9.8 g H₂SO₄ | ok (shown labels 0.1, 10, 960.4, 0.01 mol). Explanations 1 and 2 shouted (WRONG, DIVIDE) and used a dash: rewritten plainly. Options unchanged. |
| Practice Q2 CaCO₃, 3.01 × 10²³ | ok (50 g). Explanations 1 and 3 shouted or used dashes: rewritten plainly. Options unchanged. |
| Practice Q3 2.7 kg Al | ok (100 mol). Fault: credited option visibly the longest (46 against 18). Fix: "100 mol: 2700 ÷ 27" (18). |
| Practice Q4 Molecules in 36 g of water | ok (1.204 × 10²⁴). Fault: credited option visibly the longest (48 against 11). Fix: "1.204 × 10²⁴". |
| Practice Q5 Atoms in a mole of water | ok (3 × 6.02 × 10²³). Fault: credited option visibly the longest (61 against 15). Fix: "3 × 6.02 × 10²³". |

**Removed or moved.**
- Removed: the Two dozens hook (the Start here is now the mole question itself); the video; the standard-form pick (now the Standard form card); the Think again choice (now the first Easy mistake); the Sort "Which line first?" (its rule is in the Moles from mass and Between cards); the "Also on the specification, taught elsewhere" box (now Dive deeper: Where this goes next); the Key note; the second worked Step 1 / Step 2 example mol-w2 (the steps-worked slot shows mol-w1, and the attempt mol-a is the mass-to-particles direction).
- Kept: pFig; both triangles (as the record's EQ_N and EQ_P); all CFIFA examples and questions; Ks4Steps mol-w1 and mol-a.
- Key changes (options reworded with no `{stored}` text, so their answers get new keys): Practice Q3, Q4, Q5 credited options.
- New id (stem changed): none.
- Rung prompts reworded: none. Rung 2 calc 2 Convert choice 1 text changed (index and answer unchanged).
- Logic seam: `return Object.assign(c, {` rewritten to `const R = c; return Object.assign({}, R, {` so the pilot builder can add LEAN_PROPS (the eco builder accepts either).

**Fixes after the examiner and blind checks (13 Nov).** EX = EXAMINER.md item; BLIND = blind pass. Where this list and the tables above disagree, this list is current.
- EX SHOULD 1: practice Q2 feedback for the "30100 g" option rewritten (logic_edits). Keys unchanged.
