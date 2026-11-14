# percentage-yield

Sources: AQA Chemistry 8462 4.3.3.1 Percentage yield, read from spec-8462.txt. The whole of 4.3.3 is "(chemistry only)", so the lesson exists on TF and TH only, never Combined. One bullet is "(HT only)": calculate the theoretical mass of a product from a given mass of reactant and the balanced equation; it is on TH only. Rainford SOW "SEPS percentage yield": calculate the percentage yield from the actual yield; calculate the theoretical amount of a product from a given amount of reactant and the balanced equation. LEGACY page (batch 2, Ks4Ladder).

| Spec statement | Where it is covered | Route | Ticked |
|---|---|---|---|
| Even though no atoms are gained or lost in a chemical reaction, it is not always possible to obtain the calculated amount of a product because: the reaction may not go to completion because it is reversible; some of the product may be lost when it is separated from the reaction mixture; some of the reactants may react in ways different to the expected reaction. | Start here; Card: Why you get less than you calculated (verbatim); Key fact; Easy mistakes; Rung 1; Rung 3; Rung 4; Practice Q2, new Q4 (TF) | TF TH | ✓ |
| The amount of a product obtained is known as the yield. When compared with the maximum theoretical amount as a percentage, it is called the percentage yield. | Card: Yield and percentage yield (verbatim) | TF TH | ✓ |
| % Yield = Mass of product actually made ÷ Maximum theoretical mass of product × 100 | Card: The equation (AQA's words); Key fact; Easy mistakes | TF TH | ✓ |
| Calculate the percentage yield of a product from the actual yield of a reaction | Card: Worked examples (cfifa: 77.5%, 76%; TF questions py-q1 85%, py-q2 80%; TH questions py-q1h, py-q2h rearranged); Card: A yield over 100%; Rung 2 (TF); Rung 4; Practice Q1, new Q3, new Q5 (TF) / Q4 (TH) | TF TH | ✓ |
| (HT only) calculate the theoretical mass of a product from a given mass of reactant and the balanced equation for the reaction | Card: Theoretical mass from a reactant (routes TH); cfifa on TH only (two Higher worked examples and question py-h2, appended by logic_edits); Rung 2 (TH, MgCO₃); Practice new Q5 (TH) | TH | ✓ |
| MS 1a, 1c, 2a significant figures, 3b change the subject | cfifa (83.3% to 3 s.f.; TH questions rearrange to find the actual yield) | TF TH | ✓ |
| (SOW) theoretical amount from a given amount of reactant | as the HT row | TH | ✓ |

**Gaps and mismatches.**
- The old generator page gave five reasons for a low yield, two of them not AQA's ("impure reactants"; "incomplete reactions: insufficient time, temperature or contact"). The lean page gives AQA's three, word for word.
- The old page and the Design page gave Haber process figures (about 15% per pass, about 98% overall). Not on the spec, and I could not check the exact figures against an AQA source, so they are left out.
- The ladder's Rung 2 is route-aware on the legacy page: TF gets a percentage-yield calculation (3.20 kg, 2600 g) and TH gets a theoretical-mass calculation (MgCO₃). That keeps HT content off TF, so it stays as it is. It is the one place on this page where a rung differs by route.
- The legacy eyebrow "AQA Chemistry (8462) 4.3.3.1 · Quantitative" is right on both routes (Triple only).

**Practice set source.** `K.bank(slug, R.route)`: the route's `quiz` list. Fixes are in quiz-percentage-yield.json (five per route). TF and TH old lists were identical.

| Route | Q | Origin | Note |
|---|---|---|---|
| TF TH | 1 | kept | 20 g theoretical, 14 g obtained: 70%. Stem and options verbatim. Explanations 2 and 3 had a dash and capitals: rewritten plainly. |
| TF TH | 2 | fixed | Stem kept (id kept). Fault: credited option visibly the longest (140 against 76) and not AQA's reasons; distractor "Products decompose after forming" was arguable. New credited "Some product is lost when it is separated from the reaction mixture" (67); distractor 3 now "The catalyst is used up during the reaction". Distractors 1 and 2 verbatim. |
| TF TH | 3 | new | 40 g of a 50 g maximum: 80%. |
| TF | 4 | new | Which is a reason: "The reaction is reversible". |
| TF TH | 5 (TH 4) | new | A yield of 112%: "The product was not fully dried". |
| TH | 5 | new | HT: 10 g CaCO₃ → maximum 5.6 g CaO. |

Numbers: 14 ÷ 20 × 100 = 70; 40 ÷ 50 × 100 = 80; 50 ÷ 40 × 100 = 125; 10 ÷ 100 = 0.1 mol, 0.1 × 56 = 5.6 g, 0.1 × 44 = 4.4 g CO₂.

**Worked examples.** `cfifa` shows the legacy cfExamples (6.2 ÷ 8.0 × 100 = 77.5%; 1900 ÷ 2500 × 100 = 76%) and cfQuestions (TF: 34 ÷ 40 × 100 = 85%, 960 ÷ 1200 × 100 = 80%; TH: 72 × 45 ÷ 100 = 32.4 g, 85 × 2400 ÷ 100 = 2040 g). On TH the logic_edits append the legacy Higher examples (12.0 g CaCO₃: 0.120 mol, 6.72 g, 5.6 ÷ 6.72 × 100 = 83.3%; 1.00 kg: 10.0 mol, 560 g, 476 ÷ 560 × 100 = 85%) and question py-h2 (16 kg Fe₂O₃: 100 mol, 200 mol Fe, 11 200 g, 9800 ÷ 11 200 × 100 = 87.5%; with the ratio missed, 9800 ÷ 5600 = 175%). One note corrected in the copy: "Mr is in grams per mole" became "The mass of one mole in grams equals Mr" (Mr has no unit). The last standard example's "Your turn below" now reads "Now the theoretical mass from a reactant." on TH, where two more examples follow. Equations balanced: CaCO₃ → CaO + CO₂; MgCO₃ → MgO + CO₂; Fe₂O₃ + 3CO → 2Fe + 3CO₂.

**Figures.** None kept. stageFig (the yield bench) only makes sense with its step buttons; at its first state it shows the "React" stage. The page describes no diagram in words.

**Audit of the ladder (Ks4Ladder).**

| Item | Verdict |
|---|---|
| Rung 1 One reason for a low yield | ok. Fault: credited option visibly the longest (65 against 60). Fix: "Some product is lost when it is separated from the mixture" (58); same position. |
| Rung 2 (TF) 3.20 kg maximum, 2600 g collected | ok. 2600 ÷ 3200 × 100 = 81.25% (rounds to 81%); Convert choice "multiply by 1000" right. |
| Rung 2 (TH) MgCO₃, 2.10 g to 0.80 g MgO | ok. 2.10 ÷ 84 = 0.025 mol; 0.025 × 40 = 1.00 g; 0.80 ÷ 1.00 × 100 = 80%. |
| Rung 3 Zinc sulfate at 70% | ok. One order: the "still somewhere" premise, then where it went ("Some of it"), then "So". |
| Rung 4 12.0 g maximum, 9.0 g collected, 4 marks | ok. 9.0 ÷ 12.0 × 100 = 75%; two of AQA's three reasons. |

**Removed or moved.**
- Removed: the "8.0 g on paper" hook (kept as the Start here question, shorter); the yield bench and its five stages (the losses are now in the Start here reply and the first card); the 108% Think again (now Card: A yield over 100%); the reasons Sort (now the first card and Easy mistakes, catalyst included); the "why maximising yield matters" paragraph (now Dive deeper); the which-working choice (now Easy mistakes); the Equations box; the Higher theory section (now Card: Theoretical mass from a reactant, TH, and the cfifa slot on TH); the Command words grid (now Dive deeper); the Key note; the video.
- Not kept: htQuestions py-h1 (the Haber question). Its close line rests on the "about 15% per pass" figure, which I could not check (see Gaps).
- Key changes: Rung 1 credited option; Practice Q2 credited option and distractor 3 (stem kept, so its id is kept).
- New ids: Practice Q3, Q4, Q5 (new questions). Rung prompts reworded: none.

**Fixes after the examiner and blind checks (13 Nov).** EX = EXAMINER.md item; BLIND = blind pass. Where this list and the tables above disagree, this list is current.
- EX SHOULD 1: Foundation rung 2 unit chips are %, g, kg, no unit (no "mol"). Answer and unit unchanged; id kept.
