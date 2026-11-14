# using-moles-calculations

Sources: AQA Combined Science Trilogy 8464 5.3.2.3 Using moles to balance equations (HT only) and 5.3.2.4 Limiting reactants (HT only), read from spec-8464.txt (CH); AQA Chemistry 8462 4.3.2.3 and 4.3.2.4 (both HT only), read from spec-8462.txt (TH). Word for word the same. The lesson exists on CH and TH only, so everything is Higher content and no route gating is needed. Rainford SOW "Mass to balanced equations": (H) balance an equation given the masses of reactants and products; "Limiting reactants": (HT) explain the effect of a limiting quantity of a reactant on the amount of products in terms of moles or masses; identify a limiting reactant. LEGACY page (batch 2, Ks4Ladder).

| Spec statement | Where it is covered | Route | Ticked |
|---|---|---|---|
| The balancing numbers in a symbol equation can be calculated from the masses of reactants and products by converting the masses in grams to amounts in moles and converting the numbers of moles to simple whole number ratios. | Card: Balancing an equation from masses (verbatim, then the method); Reveal: 11.2 g of iron and 21.3 g of chlorine; Card: Whole numbers only; Key fact; cfifa examples 1 and 2, question um-q1; Rung 4 (a); Practice Q1 | CH TH | ✓ |
| Students should be able to balance an equation given the masses of reactants and products. | as above; Easy mistakes (1 : 1.5 : 1; Mr of H₂) | CH TH | ✓ |
| Students should be able to change the subject of a mathematical equation. | m = n × Mr in Card: The limiting reactant sets the amount of product; cfifa example 3 and um-q2; Rung 2; Rung 4 (b) | CH TH | ✓ |
| In a chemical reaction involving two reactants, it is common to use an excess of one of the reactants to ensure that all of the other reactant is used. | Card: Limiting reactants (verbatim); Dive deeper: Excess in the lab; Rung 3 | CH TH | ✓ |
| The reactant that is completely used up is called the limiting reactant because it limits the amount of products. | Card: Limiting reactants (verbatim); Key fact; Start here; Rung 1; Practice Q2, new Q4 | CH TH | ✓ |
| Explain the effect of a limiting quantity of a reactant on the amount of products it is possible to obtain in terms of amounts in moles or masses in grams. | Card: Finding the limiting reactant; Reveal: Which reactant runs out first; Card: The limiting reactant sets the amount of product; Easy mistakes; cfifa example 3 and um-q2; Rung 2; Rung 4 (b); Practice new Q3, Q4, Q5 | CH TH | ✓ |

**Gaps and mismatches.**
- The old generator page taught concentration in mol/dm³, a titration calculation, and empirical and molecular formulae here, on CH too. mol/dm³ and titration calculations are 8462 4.3.4 (chemistry only, HT): never on Combined, and taught in Concentration of solutions. Working out an empirical formula from masses is on neither spec (8462 4.2.1.3 and 8464 5.2.1.3 only ask for the empirical formula of an ionic compound from a model or diagram). All of it is gone. The old matching activity also had a broken answer ("SO ... wait: ... SO₂").
- The Design page had a Triple-only "Moles in solution · AQA 4.3.4" section and a TH-only key line about c = n ÷ V. Dropped from this lesson for the same reason. The old TH practice Q1 (KOH in mol/dm³) tested it, so it was replaced (see the practice table).
- AQA's definition makes a reactant "limiting" when it is completely used up. When two reactants are mixed in exactly the equation ratio, both are used up, so "Which is the limiting reactant?" has no single right answer. The old Q2 asked exactly that (0.1 mol Na with 0.05 mol Cl₂, credited "Neither"); "Sodium" also meets AQA's definition. Replaced with an unambiguous mix (see below).
- The eyebrow is already route-aware (`{{ eyebrowLine }}`: 8464 5.3.2.3–5.3.2.4 on CH, 8462 4.3.2.3–4.3.2.4 on TH). No edit.

**Practice set source.** `K.bank(slug, R.route)`: the route's `quiz` list. Fixes are in quiz-using-moles-calculations.json (five per route).

| Route | Q | Origin | Note |
|---|---|---|---|
| CH | 1 | kept | Balancing 2Mg + O₂ → 2MgO from masses. Stem and options verbatim. Explanations 1 and 3 had capitals and a dash: rewritten plainly. |
| CH | 2 | fixed | Old: 0.1 mol Na with 0.05 mol Cl₂, "Neither" (arguable, see Gaps). New: 0.1 mol Na with 0.1 mol Cl₂; "Sodium". |
| CH | 3 | new | Twice as much acid in excess: the mass of hydrogen stays the same. |
| CH | 4 | new | 2H₂ + O₂, 0.5 mol each: hydrogen is limiting. |
| CH | 5 | new | Mg + 2HCl, 0.2 mol each: 0.1 mol of H₂ (HCl limiting). |
| TH | 1 | fixed | Old: concentration of 0.3 mol KOH in 300 cm³ (4.3.4, not this lesson). New: the CH Q1 balancing question, identical text. |
| TH | 2 | fixed | As CH Q2. |
| TH | 3–5 | new | Identical to CH 3–5. |

Numbers: 4.8 ÷ 24 = 0.2, 3.2 ÷ 32 = 0.1, 8.0 ÷ 40 = 0.2; 0.1 mol Na needs 0.05 mol Cl₂; 0.5 mol H₂ needs 0.25 mol O₂; 0.2 mol Mg needs 0.4 mol HCl, so 0.2 mol HCl makes 0.2 ÷ 2 = 0.1 mol H₂.

**Worked examples.** `cfifa` is the legacy page's own: balancing Mg + 2HCl from 4.8 g, 14.6 g, 19.0 g, 0.4 g (0.20 : 0.40 : 0.20 : 0.20 = 1 : 2 : 1 : 1; 4.8 + 14.6 = 19.4 = 19.0 + 0.4); balancing 4Na + O₂ → 2Na₂O from kg (40 : 10 : 20 = 4 : 1 : 2; 920 + 320 = 1240); the limiting-reactant example from the subtopic `fifas` (2.4 g Mg, 3.65 g HCl, HCl limiting, 0.1 g H₂); um-q1 (N₂ + 3H₂ → 2NH₃: 0.10 : 0.30 : 0.20); um-q2 (2H₂ + O₂ → 2H₂O: 200 mol H₂, 75 mol O₂, O₂ limiting, 150 mol H₂O = 2700 g; 50 mol H₂ left). All rechecked. Record reveal: 11.2 ÷ 56 = 0.20, 21.3 ÷ 71 = 0.30, Mr FeCl₃ = 56 + 3 × 35.5 = 162.5, 32.5 ÷ 162.5 = 0.20; 11.2 + 21.3 = 32.5; 2Fe + 3Cl₂ → 2FeCl₃ balances (6 Cl each side). Reveal rows: 1.2 ÷ 24 = 0.05, 7.3 ÷ 36.5 = 0.20.

**Figures.** None kept. benchFig sits in a sized div (max-width), not the plain bordered figure div the legacy-fig slot needs, and at its first state it only shows unreacted counters. Nothing on this page describes a diagram in words.

**Audit of the ladder (Ks4Ladder, one item per rung).**

| Item | Verdict |
|---|---|
| Rung 1 Meaning of limiting reactant | ok. Fault: the reply to "fewest moles" named "Mix A", the reaction bench this page no longer has. Fix: "Moles must be compared with the equation ratio. A reactant with fewer moles can still be in excess." The reply to "smallest mass" refers to the start of the lesson; the lean Start here uses the same 2.4 g / 3.65 g mix, so it stays true. |
| Rung 2 3.6 g Mg with 3.2 g O₂ | ok. 0.15 mol Mg needs 0.075 mol O₂; 0.10 mol present; Mg limiting; 0.15 × 40 = 6.0 g. |
| Rung 3 Why an excess of acid is used | ok. One order ("So" and the final consequence). |
| Rung 4 Aluminium and chlorine, 6 marks | ok. 0.20 : 0.30 : 0.20 → 2Al + 3Cl₂ → 2AlCl₃ (balanced); 0.10 mol Al needs 0.15 mol Cl₂, 0.10 present, Cl₂ limiting; 0.10 × 2 ÷ 3 × 133.5 = 8.9 g. 5.4 + 21.3 = 26.7. |

**Removed or moved.**
- Removed: the reaction bench and its Mix A / Mix B / own mix (the method is the Finding card and the reveal); the limiting-reactant Sort (now the reveal table, same mixes); the Think again on Fe + Cl₂ (now the iron reveal and Whole numbers only card); the Moles in solution section (4.3.4, see Gaps); the Equations box (n = m ÷ Mr is in the balancing card; c = n ÷ V left); the Command words grid (now Dive deeper); the Key note; the video.
- Kept: cfExamples and cfQuestions (`cfifa`).
- Key changes: none in the ladder (only a reply changed). Practice set: CH Q2 and TH Q1, Q2 are new questions (new ids).
