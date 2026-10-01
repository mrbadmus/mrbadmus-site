# Examination — Percentage Yield (percentage-yield) — not in 8464 · AQA 8462 4.3.3.1 (chemistry only)
Verdict: SOURCE OK WITH FLAGS
Examiner: Opus, 1 Oct 2026. Pack examined: `docs/ks4/packs/batch-2/chemistry-4.3.3.1-percentage-yield.md`.
Spec sources fetched from filestore.aqa.org.uk and read as text: AQA-8462-SP-2016.PDF and AQA-8464-SP-2016.PDF, both Version 1.1, 04 Oct 2019. 8464 was searched for "yield" and has no percentage-yield section, which confirms the lesson is chemistry only.

Route copies, checked directly: the record exists only in the triple modules, TF and TH. They differ only in `higher` (TF `null`). Theory, quiz, FIFA, common_mistake and key note are identical on both.

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n; th1–th3 = theory chunks.

## 1. Spec reference
| spec | section | title | page | label |
|---|---|---|---|---|
| 8464 | — | **not in 8464** | — | — |
| 8462 | **4.3.3.1** | Percentage yield (in 4.3.3 "Yield and atom economy of chemical reactions (chemistry only)") | p.41 | triple, plus one HT bullet |
| supporting | 8462 4.3.2.1–4.3.2.4 | Moles; amounts in equations; limiting reactants (HT only) | p.38–40 | higher (used by the HT bullet) |
| supporting | 8462 4.3.3.2 | Atom economy, "(HT only) explain why a particular reaction pathway is chosen … given appropriate data such as atom economy …, yield, rate, equilibrium position and usefulness of by-products" | p.41 | triple-higher |

BATCH-PLAN ("— · 8462 4.3.3.1 · TF TH") is right.

Spec statement (verbatim): "Even though no atoms are gained or lost in a chemical reaction, it is not always possible to obtain the calculated amount of a product because: the reaction may not go to completion because it is reversible; some of the product may be lost when it is separated from the reaction mixture; some of the reactants may react in ways different to the expected reaction. The amount of a product obtained is known as the yield. When compared with the maximum theoretical amount as a percentage, it is called the percentage yield. % Yield = Mass of product actually made ÷ Maximum theoretical mass of product × 100. Students should be able to: calculate the percentage yield of a product from the actual yield of a reaction; (HT only) calculate the theoretical mass of a product from a given mass of reactant and the balanced equation for the reaction."

## 2. Route table
| # | teachable point | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Theoretical vs actual yield (th1; th2) | triple | 4.3.3.1 | TF, TH | OK |
| R2 | The spec's three reasons: reversible / lost on separation / side reactions (th1 1–3; q2; key_note) | triple | 4.3.3.1 | TF, TH | OK |
| R3 | Extra reasons "impure reactants", "incomplete reactions (time, temperature, contact)" (th1 4–5) | triple (beyond the spec's list) | — | TF, TH | Acceptable as extras, but keep the spec's three as the taught set. "Incomplete" overlaps with "may not go to completion". |
| R4 | % yield equation and calculation (th2; equations; FIFA; q1; matching) | triple | 4.3.3.1 | TF, TH | OK |
| R5 | Why a high yield matters: cost, waste, sustainability (th2; th3) | triple | 4.3.3 (sustainable development); 4.10 | TF, TH | OK |
| R6 | **Choosing or evaluating a process using yield** (`higher`: "Evaluate the economic and environmental importance…") | triple-higher | 4.3.3.2 (HT only) | TH | OK |
| R7 | Haber example: ~15 % per pass, recycling, ~98 % overall (th3) | triple (Haber is 8462 4.10.4.1, chemistry only) | 4.10.4.1; the numbers are not in the spec | TF, TH | OK as context. **Not a rung** (the numbers are not examinable). |
| R8 | **Theoretical mass from reactant mass via moles** (`higher`; **common_mistake**) | **triple-higher** | 4.3.3.1 (HT only) | `higher`: TH ✓. **common_mistake: TF and TH** | **HT content in a field TF sees.** common_mistake tells every pupil to "Use moles: find moles of limiting reactant…". Tag the moles sentence `triple-higher`. For TF, the theoretical mass is given in the question. |
| R9 | Limiting reactant to find the maximum theoretical yield (`higher`) | triple-higher | 4.3.2.4 (HT) + 4.3.3.1 (HT) | TH | OK |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | th1 | theoretical yield = maximum possible amount from the equation; actual yield = amount collected | OK | — | 4.3.3.1 |
| C2 | th1 | "actual yield is almost always LESS than theoretical yield" | OK | — | 4.3.3.1 |
| C3 | th1 reasons 1–3 | reversible; side reactions; practical losses | OK | These match the spec's list. | 4.3.3.1 |
| C4 | th1 reason 4 | "IMPURE REACTANTS — some reactants may not react if they contain impurities" | IMPRECISE | Impurities mean the mass weighed out is not all reactant, so the *calculated* theoretical yield is too high. That is not quite "some reactants may not react". It is not in the spec's list. | — |
| C5 | th1 reason 5 | "INCOMPLETE REACTIONS — insufficient time, temperature or contact" | OK | Overlaps with "may not go to completion". | 4.3.3.1 |
| C6 | th2 | % yield = actual ÷ theoretical × 100 | OK | — | 4.3.3.1 |
| C7 | th2 | 38 ÷ 50 × 100 = 76 % | OK | — | — |
| C8 | th2 | "A percentage yield of 100% would mean no product was lost — impossible in practice." | IMPRECISE | The spec says it is "not always possible", not that it is impossible. Write "very rarely achieved in practice". Note also the exam case: a measured yield **over** 100 % means the product is impure or still wet. | 4.3.3.1 |
| C9 | th2 / th3 | high yield → less waste, lower cost, more sustainable | OK | — | 4.3.3 |
| C10 | th3 Haber | N₂ + 3H₂ ⇌ 2NH₃ reversible; ~15 % per pass; unreacted gases recycled; ~98 % overall | OK | The figures are the usual textbook values, are not in the spec, and are not examinable. The equation and the recycling are in 4.10.4.1. | 4.10.4.1 |
| C11 | th3 "PRACTICAL TIP" | "Ensure complete reactions: sufficient time, temperature, **catalyst**" | **WRONG (catalyst part)** / IMPRECISE (temperature) | A catalyst increases the **rate**. It does not increase the maximum yield of a reversible reaction, because it does not change the position of equilibrium. A higher temperature can **lower** the yield of an exothermic equilibrium (the Haber process, in this same chunk). Rewrite as "allow enough time; recycle unreacted starting materials; minimise losses during separation". "Catalysts increase yield" is a classic misconception that AQA mark schemes do not credit. | 8462 4.6.1.4 ("Catalysts change the rate of chemical reactions"); 4.6.2.6 (temperature and equilibrium, HT); 4.10.4.1 |
| C12 | `higher` | moles → molar ratio → product mass; limiting reactant; evaluate | OK | — | 4.3.3.1 HT; 4.3.2.4 |
| C13 | common_mistake | "theoretical yield must be calculated from the balanced equation … Use moles…" | OK (science) / route **triple-higher** | See R8. For TF: "Divide the actual mass by the theoretical mass, never the other way round." | 4.3.3.1 HT |
| C14 | key_note | "Always less than 100% in practice." | IMPRECISE | Write "Usually less than 100 %". | 4.3.3.1 |
| C15 | key_note | reasons list includes "impurities" | IMPRECISE | See C4. | — |
| C16 | key_note | "Chemistry-only spec point." | OK | — | 4.3.3 |
| C17 | equations | % yield = actual ÷ theoretical × 100 | OK | Recalled. AQA prints it in the spec, but GCSE Chemistry has no exam equation sheet. | 4.3.3.1 |
| C18 | FIFA | 6.2 ÷ 8.0 × 100 = 77.5 % | OK / IMPRECISE (sig figs) | The arithmetic is correct. The data are to 2 s.f., so 78 % (2 s.f.) is the strictly consistent answer. AQA mark schemes accept 77.5 unless a precision is asked for. Add the instruction "give your answer to 2 significant figures" only in a new item, never in the frozen FIFA. **CFIFA Convert step:** "Nothing to convert: both masses are in g." | MS 2a |
| C19 | matching (to be replaced) | 76 %; reversible; losses; high yield desirable | OK | — | 4.3.3.1 |
| C20 | q1 key | 14 ÷ 20 × 100 = 70 % | OK | — | 4.3.3.1 |
| C21 | q1 option 1 | "43% — (14 ÷ 20) × 3 = 42%" | **WRONG** | The option contradicts itself (43 vs 42), and its own working gives 2.1, not 42 (0.7 × 3 = 2.1). It models no real misconception. wx1 does not diagnose it either. | — |
| C22 | q1 option 2 + wx2 | 20 ÷ 14 × 100 = 143 % (142.9); "over 100%, which is impossible for yield" | OK | It is correct to say a calculated yield cannot exceed 100 % for a pure, dry product. | — |
| C23 | q1 option 3 + wx3 | 30 % is the loss | OK | — | — |
| C24 | q2 key | losses, incomplete reactions, side reactions, reversible reactions | OK | — | 4.3.3.1 |
| C25 | q2 wx1–3 | conservation of mass; theoretical yields don't overestimate; not all products decompose | OK | — | 4.3.1.1; 4.3.3.1 |

On C11: 8462 4.6.1.4 states only that "Catalysts change the rate of chemical reactions but are not used up". The spec does not spell out "a catalyst does not shift the position of equilibrium" in those words. The science is settled, so this is not a flag.

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| TF, TH · q1 · "A reaction has a theoretical yield of 20 g but only 14 g is obtained…" | The keyed answer is right, but one distractor (index 1) contradicts itself and its working is wrong. | Keep verbatim. **Do not use it as a ladder rung on either route.** Write a new rung-2 item with a CFIFA Convert case, for example theoretical 2.5 kg and actual 1.9 kg → 76 %. |
| TF, TH · q2 · "Why is the actual yield of a reaction almost always less…" | Clean. | Usable as rung 1 on both routes. |

No frozen quiz item is route-wrong.

## 5. For the lesson author

**Misconceptions commonly seen**
- **Inverting the fraction:** theoretical ÷ actual gives more than 100 %.
- **Yield over 100 % accepted without comment.** The AQA answer is that the product was not dry, or was impure.
- **"Mass is lost in the reaction"** given as the reason for a low yield. This contradicts conservation of mass, and the spec's opening clause pre-empts it.
- **"A catalyst increases the yield."** It increases the rate only (see C11).
- **Confusing percentage yield with atom economy**, which is the neighbouring lesson in batch 3.
- **HT:** using the reactant's mass as the theoretical yield; not using the mole ratio; using the excess reactant instead of the limiting one.

**Command words:** Calculate, Suggest (a reason for a low yield or a yield over 100 %), Explain, Give, Evaluate (HT, choice of process).

**Typical questions (⚑ examiner-drafted)**
- ⚑ examiner-drafted, 2 marks, Calculate, **triple**: *"The maximum theoretical mass of copper sulfate is 8.0 g. The student obtains 6.2 g. Calculate the percentage yield."*
  - (1) 6.2 ÷ 8.0 × 100.
  - (1) 77.5 %, or 78 %.
- ⚑ examiner-drafted, 3 marks, Suggest / Give, **triple**: *"Give three reasons why the percentage yield is less than 100 %."*
  - (1) each, up to 3: reversible, or did not go to completion; product lost when separated (for example during filtering or transferring); side reactions, or reactants reacted in a different way.
  - Do not accept "mass lost in the reaction" or "the reactants evaporated" without a qualifier.
- ⚑ examiner-drafted, 1 mark, Suggest, **triple**: *"A student's percentage yield was 108 %. Suggest why."*
  - (1) The product was still wet, or was not dried, or was impure.
- ⚑ examiner-drafted, 4 marks, Calculate, **triple-higher**: *"Calcium carbonate decomposes: CaCO₃ → CaO + CO₂. A student heats 12.0 g of CaCO₃ and obtains 5.6 g of CaO. Calculate the percentage yield. (Mr CaCO₃ = 100, CaO = 56)"*
  - (1) n(CaCO₃) = 0.120 mol.
  - (1) Theoretical mass of CaO = 0.120 × 56 = 6.72 g.
  - (1) 5.6 ÷ 6.72 × 100.
  - (1) 83 % (83.3).
  - Allow error carried forward from a wrong theoretical mass.
- ⚑ examiner-drafted, 6 marks, levels of response, Evaluate, **triple-higher**: *"Two reactions can make the same product. Use the data (yield, atom economy, rate, by-product use) to evaluate which a manufacturer should choose."*
  - Level 3 (5–6): uses every data type, compares the two routes on each, and reaches a justified conclusion that weighs the factors against each other.
  - Level 2 (3–4): compares on at least two factors with some reasoning, and makes a conclusion.
  - Level 1 (1–2): simple statements about one factor.
  - This belongs to 4.3.3.2 HT. Use it here only if the atom-economy lesson does not already carry it.

**Required practical:** none of its own. Percentage yield is the natural data-processing step of **RP8 Combined / RP1 Chemistry** (preparing a pure, dry sample of a soluble salt from an insoluble oxide or carbonate). The FIFA's copper sulfate fits that practical. The yield calculation itself is chemistry only.

**Equations to learn (recalled)**
- % yield = mass of product actually made ÷ maximum theoretical mass × 100. **Triple.**
- **Triple-higher:** n = m ÷ Mr, the mole ratio, then mass = n × Mr.

## 6. Verdict
**SOURCE OK WITH FLAGS.**
- **Route corrections (1).** common_mistake carries the HT moles method onto TF.
- **WRONG (2).**
  - The "catalyst" advice in th3.
  - q1's self-contradictory distractor, which is frozen.
- **IMPRECISE (5).** C4, C8, C11 (temperature), C14, C18.

Only Mide can rule: **none.**

Note for the commander: there is no `examiner_tip`.
