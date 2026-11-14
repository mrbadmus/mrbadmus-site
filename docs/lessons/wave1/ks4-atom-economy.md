# atom-economy

Sources: AQA Chemistry 8462 4.3.3.2 Atom economy, read from spec-8462.txt. The whole of 4.3.3 is "(chemistry only)", so the lesson exists on TF and TH only, never Combined. One bullet is "(HT only)": explain why a particular reaction pathway is chosen to produce a specified product given appropriate data; it is on TH only. Addition of water (steam) to alkenes is 8462 4.7.2.3 (chemistry only), so the ethene and steam example is on both of this lesson's routes. Rainford SOW "SEPS atom economy": calculate the atom economy of a reaction; explain its importance to sustainable development and economic reasons. LEGACY page (batch 3, Ks4Ladder).

| Spec statement | Where it is covered | Route | Ticked |
|---|---|---|---|
| The atom economy (atom utilisation) is a measure of the amount of starting materials that end up as useful products. | Start here; Card: What atom economy means (verbatim); Rung 1 | TF TH | ✓ |
| It is important for sustainable development and for economic reasons to use reactions with high atom economy. | Card: Why a high atom economy matters (verbatim); Key fact; Rung 4 (TF, part b); Practice new Q5 (TF); Dive deeper: brine | TF TH | ✓ |
| The percentage atom economy of a reaction is calculated using the balanced equation: (relative formula mass of desired product from equation ÷ sum of relative formula masses of all reactants from equation) × 100 | Card: The equation (AQA's words); Key fact; Easy mistakes | TF TH | ✓ |
| Calculate the atom economy of a reaction to form a desired product from the balanced equation | Reveal: Three reactions; Card: One product means 100%; Card: Worked examples (cfifa: ethanol 100%, copper 74.3%; route-aware ae-q1, ae-q2); Rung 2; Rung 3; Rung 4 (TF); Practice Q1, Q2, new Q3, Q4; Dive deeper: brine | TF TH | ✓ |
| (HT only) explain why a particular reaction pathway is chosen to produce a specified product given appropriate data such as atom economy (if not calculated), yield, rate, equilibrium position and usefulness of by-products | Card: Choosing a reaction pathway (routes TH); Reveal: Choose a route (routes TH, the data Rung 4 asks for); Rung 4 (TH); Practice new Q5 (TH) | TH | ✓ |
| MS 1a, 1c, 3b | cfifa; answers to 3 s.f. | TF TH | ✓ |

**Gaps and mismatches.**
- The old generator page labelled Fe₂O₃ + 3CO → 2Fe + 3CO₂ (45.9%) "high atom economy". It is the lowest of the three examples. The reveal table now shows it as 45.9% with no label.
- The "Choose a route" figures (about 30 °C; 300 °C and 60–70 atm; 51% and 100%) are given data for the TH Rung 4, copied from the Design page. 51% and 100% I recomputed (92 ÷ 180 × 100 = 51.1%; 46 ÷ 46 × 100 = 100%). The conditions are the usual textbook values for fermentation and for the hydration of ethene; 8462 4.7.2.3 asks for "conditions" but does not print numbers, so these are data in a question, not spec facts. Flag for Mide's check.
- The cfifa slot's first example comes from the subtopic `fifas`; its Answer line reads "Atom economy = 100% — addition reaction, one product only" (a dash). It lives in all_subtopics data, not in the logic, so no logic_edit can reach it. Left for the lead.
- The legacy eyebrow "AQA Chemistry (8462) 4.3.3.2 · Quantitative" is right on both routes.

**Practice set source.** `K.bank(slug, R.route)` (shown when the list is not empty): the route's `quiz` list. Fixes are in quiz-atom-economy.json (five per route). TF and TH old lists were identical.

| Route | Q | Origin | Note |
|---|---|---|---|
| TF TH | 1 | kept | Total Mr 100, desired 80: 80%. Stem and options verbatim. All three explanations had capitals or dashes: rewritten plainly. |
| TF TH | 2 | kept | Why addition reactions are 100% (shown label "Only one product is formed"). Stem and options verbatim. Explanation 1 had capitals and a dash: rewritten plainly. |
| TF TH | 3 | new | CaCO₃ → CaO + CO₂: 56%. |
| TF TH | 4 | new | Zn + H₂SO₄ → ZnSO₄ + H₂, hydrogen: 1.2%. |
| TF | 5 | new | Why a high atom economy matters: "Less of the starting materials is wasted". |
| TH | 5 | new | HT: Route B (60%, by-product sold) "may still be chosen". |

Numbers: 80 ÷ 100 × 100 = 80; 56 ÷ 100 × 100 = 56; 100 ÷ 56 × 100 = 179; 65 + 98 = 163, 2 ÷ 163 × 100 = 1.2, 2 ÷ 98 × 100 = 2.0, ZnSO₄ = 65 + 32 + 64 = 161 so 161 ÷ 163 × 100 = 98.8, 1 ÷ 163 × 100 = 0.6. Zn + H₂SO₄ → ZnSO₄ + H₂ balances.

**Worked examples.** `cfifa` is the legacy page's own: ethanol (28 + 18 = 46, 100%); 2CuO + C → 2Cu + CO₂ (127 ÷ 171 × 100 = 74.3%); TF questions 2H₂O → 2H₂ + O₂ (4 ÷ 36 = 11.1%) and Mg + 2HCl → MgCl₂ + H₂ (95 ÷ 97 = 97.9%); TH questions 2NH₄Cl + Ca(OH)₂ → CaCl₂ + 2NH₃ + 2H₂O (34 ÷ 181 = 18.8%) and CH₄ + H₂O → CO + 3H₂ (6 ÷ 34 = 17.6%). Every equation balanced and every number rechecked. Record reveal: 46 ÷ 46 = 100%; 56 ÷ 100 = 56%; 112 ÷ 244 = 45.9%. Easy mistakes: 2 × 23 = 46, 46 ÷ 117 = 39.3%. Brine: 2NaCl + 2H₂O → 2NaOH + Cl₂ + H₂ balances; 117 + 36 = 153; 80 ÷ 153 = 52.3%, 71 ÷ 153 = 46.4%, 2 ÷ 153 = 1.3%.

**Figures.** None kept. stripFig and brineFig sit in sized divs (max-width), not the plain bordered figure div the legacy-fig slot needs, and both are animations whose first state shows only the reactants. The reveal table carries the three reactions instead.

**Audit of the ladder (Ks4Ladder).**

| Item | Verdict |
|---|---|
| Rung 1 Meaning of atom economy | Fault: credited option visibly the longest (79 against 72). Fix: "The percentage of the reactants’ mass that ends up in the desired product" (73). Fault: the reply to the waste-share option named "the strip", which this page no longer has. Fix: "That is the waste share. Atom economy is the useful share." |
| Rung 2 (TF) Copper sulfate from CuCO₃ | ok. 63.5 + 12 + 48 = 123.5; 63.5 + 32 + 64 = 159.5; 159.5 ÷ 221.5 × 100 = 72.0%. Equation balances. |
| Rung 2 (TH) Titanium from TiCl₄ | ok. 48 + 4 × 35.5 = 190; 48 ÷ 238 × 100 = 20.2%. Equation balances. Not HT content; it is simply a different calculation on TH. |
| Rung 3 Ethanol from ethene and steam is 100% | Fault: links 1 and 2 ("react by addition", "Ethanol is the only product formed") could be read in either order. Fix: link 2 now "So ethanol is the only product formed.", so the single product follows from the addition reaction and only one order is right. Position kept. |
| Rung 4 (TF) 2Fe₂O₃ + 3C, 4 marks | ok. 4 × 56 = 224; 2 × 160 + 3 × 12 = 356; 62.9%. Equation balances. |
| Rung 4 (TH) Evaluate fermentation against hydration, 6 marks | ok, with the record's TH reveal "Choose a route" carrying the table its prompt names (the Design table goes with its section). Levels and points match the table rows. |

**Removed or moved.**
- Removed: the two-factories hook (kept as the Start here question, shorter); the mass strip and its three tabs (now the Three reactions reveal); the sodium Think again (now Easy mistakes); the brine activity (now Dive deeper); the explainer paragraphs (now cards); the Choose a route table and Sort (the table is now a TH reveal; the Sort's judgement is in the Choosing a reaction pathway card); the Equations box; the Command words grid (now Dive deeper); the Key note; the video.
- Kept: cfExamples and route-aware cfQuestions (`cfifa`).
- Key changes: Rung 1 credited option; Rung 3 link 2.
- New ids: Practice Q3, Q4, Q5 (new questions). Rung prompts reworded: none.

**Fixes after the examiner and blind checks (13 Nov).** EX = EXAMINER.md item; BLIND = blind pass. Where this list and the tables above disagree, this list is current.
- EX SHOULD 1: Foundation rung 2 unit chips are %, g, kg, no unit (no "g/mol"). Answer and unit unchanged; id kept.
