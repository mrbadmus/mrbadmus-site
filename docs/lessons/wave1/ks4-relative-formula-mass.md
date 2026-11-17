# relative-formula-mass

Sources: AQA 8464 5.3.1.2 (CF CH) and 8462 4.3.1.2 (TF TH), "Relative formula mass", read from spec-8464.txt and spec-8462.txt. Same wording in both. No HT-only or chemistry-only lines. Rainford SOW lesson "Relative formula mass" (use relative atomic masses; calculate Mr from a formula, given the Ar values). Ar values are the AQA periodic table's (Cl = 35.5). LEGACY page (batch 2, Ks4Ladder).

| Spec statement | Where it is covered | Route | Ticked |
|---|---|---|---|
| The relative formula mass (Mr) of a compound is the sum of the relative atomic masses of the atoms in the numbers shown in the formula | Card: Relative atomic mass, Ar; Card: Relative formula mass, Mr; Card: Brackets; Reveal: Work out the Mr; Key fact; Worked examples (cfifa, H₂SO₄); Rung 1; Quiz Q1, Q2, Q3 | CF CH TF TH | ✓ |
| In a balanced chemical equation, the sum of the relative formula masses of the reactants in the quantities shown equals the sum of the relative formula masses of the products in the quantities shown | Card: Mr in a balanced equation; Key fact; Rung 3; Quiz Q5 | CF CH TF TH | ✓ |
| Calculate the percentage by mass in a compound given the relative formula mass and the relative atomic masses | Card: Percentage by mass; Worked examples (cfifa); Rung 2 (Foundation); Rung 4; Quiz Q4 | CF CH TF TH | ✓ |
| (SOW) use Ar values; calculate Mr from a formula | Card: Relative atomic mass, Ar; Reveal: Work out the Mr | CF CH TF TH | ✓ |
| 5.3.2.2 / 4.3.2.2 (HT only): masses from a balanced equation | Dive deeper: Mr and reacting masses (routes CH TH); the page's own Higher worked example and Higher CFIFA Q2, inside the cfifa slot, which the logic shows on Higher routes only. Taught in amounts-in-equations. | CH TH | ✓ |

**Gaps and mismatches.** The old generator data for CH and TH had a `higher` note saying percentage by mass is Higher, and adding empirical formulae. Percentage by mass is on every tier in both specs; empirical formulae are not in 5.3 / 4.3 at all. Neither note is carried. The old theory called Mr "a ratio relative to carbon-12"; that is not in this statement and is left out.

**Practice set source.** `K.bank(slug, R.route)`: the route's `quiz` list. Fixes are in quiz-relative-formula-mass.json. Rung 1 is the same list's calcium carbonate question, read by `K.find(slug, route, 'relative formula mass of calcium carbonate')`, so that stem and its options are kept exactly.

**Ladder.** Ks4Ladder, one item per rung. Rung 2 is tier-split in the logic (`H ?`), under one rung id: Foundation sees percentage by mass of carbon in CO₂. The Higher version asked for reacting masses (5.3.2.2 / 4.3.2.2, HT only), which is not this all-route lesson's content; it is rewritten in place (logic_edits) to the mass of iron in 0.320 kg of Fe₂O₃, a percentage-by-mass application with the same convert step and marks.

**Audit of the ladder, worked examples and practice set.**

| Item | Verdict |
|---|---|
| Rung 1 (= Quiz Q1) Mr of CaCO₃ | ok (100). Its wrong-option feedback is the quiz item's wrong_explanations, and the first was garbled ("CaCO₃ has only ONE oxygen"). Fixed in the quiz JSON; stem and options untouched, so the K.find needle, the question id and the answer keys all survive. |
| Rung 2 Foundation: % C in CO₂, 3 s.f. | ok (12 ÷ 44 × 100 = 27.27, 27.3%) |
| Rung 2 Higher: 0.50 kg CaCO₃ → CaO | Arithmetic ok (280 g). Fault: reacting masses from an equation (HT only, another lesson) as a rung on an all-route lesson. Fix (logic_edits): mass of iron in 0.320 kg of Fe₂O₃, Mr 160, 112 ÷ 160 × 320 = 224 g; same convert choice (multiply by 1000), same unit chips, 3 marks. |
| Rung 3 chain: 2Mg + O₂ → 2MgO totals | ok. One forced order: link 2 starts "So" from link 1, and link 3's equal totals need link 2's balance. |
| Rung 4 (NH₄)₂SO₄, 4 marks | ok (wrong 114 = 14 + 4 + 32 + 64; right 132; % N = 28 ÷ 132 × 100 = 21.2%) |
| CFIFA example 1 (old fifa) H₂SO₄ | ok (98) |
| CFIFA example 2: % Mg in MgO | ok (60%) |
| CFIFA example 3: Mg in 2.0 kg MgO | ok (1200 g) |
| CFIFA Higher example: 12 g Mg → MgO | ok (20 g) |
| CFIFA Foundation Q1: % Ca in CaCO₃ | ok (40%) |
| CFIFA Foundation Q2: Ca in 0.50 kg CaCO₃ | ok (200 g) |
| CFIFA Higher Q1: % N in NH₄NO₃ | ok (Mr 80, 35%) |
| CFIFA Higher Q2: 3.0 kg Mg → MgO | ok (3000 ÷ 48 = 62.5; × 80 = 5000 g) |
| Quiz Q1 Mr of CaCO₃ ("fixed") | Stem and options verbatim. Fault: wrong_explanations 1 to 3 read as if CaCO₃ had one oxygen, and used capitals and dashes. Rewritten plainly. origin "fixed", old_q = the same stem. |
| Quiz Q2 Mr of Mg(NO₃)₂ (kept) | ok (148; 86, 100 and 116 each recounted) |
| Quiz Q3 Mr of CO₂ (new) | ok (44) |
| Quiz Q4 % O in H₂O (new) | ok (16 ÷ 18 × 100 = 88.9%) |
| Quiz Q5 total Mr of reactants in 2H₂ + O₂ (new) | ok (36) |

**Removed or moved.**
- Removed: the formula unpacker (now the Brackets card and the Work out the Mr reveal); the balance pans (now Mr in a balanced equation); the Think again on reacting masses (Ks4Choice, 6 g Mg → 10 g MgO; the idea is now Dive deeper, Higher only); the Key note; the video; the command words.
- Not kept: `upFig` and `panFig`. Both are animation figures: at their first state one is an empty mass scale ("Count first, then unpack") and the other an empty balance.
- Moved to Dive deeper: Mr and reacting masses (routes CH TH).
- Key changes: none (no option reworded).
- New id (stem changed): none. New questions: Q3, Q4, Q5 (identical on every route).
- Rung prompts reworded, position kept (id kept): relative-formula-mass#r2 (Higher version only).

**Words.** Old Design page prose about 685 (old generator theory 330). New knowledge + key fact + Dive deeper about 457.
