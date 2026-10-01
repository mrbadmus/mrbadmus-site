# Examination — Atom economy (atom-economy) — AQA 8462 4.3.3.2 (not in 8464)
Verdict: SOURCE WRONG IN PLACES — formula's denominator contradicts AQA's in two fields; one theory label wrong
Examiner: Opus, 1 Oct 2026. Pack examined: `docs/ks4/packs/batch-3/chemistry-4.3.3.2-atom-economy.md`.
Spec sources fetched from filestore.aqa.org.uk and read as text: AQA-8462-SP-2016.PDF and AQA-8464-SP-2016.PDF, both Version 1.1, 04 Oct 2019. "Atom economy" does not occur anywhere in the 8464 text (searched). Mark-scheme conventions are from examiner knowledge of AQA 8462 papers 2018–2024; not fetched.

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n (option index; 0 = keyed); th1–th3 = theory chunks. Route copies: the lesson appears on TF and TH only. TF differs **only** in `higher` (`null`). There is no rp and no examiner_tip.

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8462 Chemistry | **4.3.3.2** | Atom economy | **triple** (inside 4.3.3 "Yield and atom economy of chemical reactions (chemistry only)"). The second bullet is **(HT only)**, so **triple-higher**. |
| 8464 Combined | — | — | absent |
| Supporting | 8462 4.3.1.2 Relative formula mass (base); 4.3.3.1 Percentage yield (triple; theoretical mass HT); 4.7.3.1 Addition polymerisation (chemistry only); 4.7.2.2 Reactions of alkenes — addition of water (chemistry only) | | |

Pack filename 4.3.3.2 is correct. BATCH-PLAN "— · 8462 4.3.3.2", TF TH, is correct.

Spec statement (verbatim): "The atom economy (atom utilisation) is a measure of the amount of starting materials that end up as useful products. It is important for sustainable development and for economic reasons to use reactions with high atom economy. The percentage atom economy of a reaction is calculated using the balanced equation for the reaction as follows: **Relative formula mass of desired product from equation ÷ Sum of relative formula masses of all reactants from equation × 100.** Students should be able to: calculate the atom economy of a reaction to form a desired product from the balanced equation; (HT only) explain why a particular reaction pathway is chosen to produce a specified product given appropriate data such as atom economy (if not calculated), yield, rate, equilibrium position and usefulness of by-products."

## 2. Route table
| # | teachable point (pack location) | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Definition: how much of the starting materials ends up as useful product (th1) | triple | 4.3.3.2 | TF, TH | OK |
| R2 | Calculating atom economy from the balanced equation (th1, th2; equations; FIFA; q1; `higher` "Calculate atom economy using Mr values") | triple | 4.3.3.2 bullet 1 | TF, TH (the `higher` line is TH only) | OK on route. The `higher` field's "calculate" line is **base-triple content tagged Higher**. No content is lost, since th1/th2 teach it on TF. Tag it `triple`. |
| R3 | High atom economy matters for sustainability and economics (th3; `higher` "Evaluate the economic and environmental importance") | triple | 4.3.3.2 ("important for sustainable development and for economic reasons") | TF, TH | The `higher` evaluate line is **triple content tagged Higher**. Tag it `triple`. |
| R4 | Addition reactions (one product) = 100 % (th2, th3; FIFA; q2) | triple | 4.3.3.2 + 4.7.3.1 (addition polymer: "no other molecule is formed") | TF, TH | OK |
| R5 | Comparing routes / choosing a pathway (th3 "COMPARING ROUTES"; `higher` "Compare atom economy of different synthetic routes") | **triple-higher** | 4.3.3.2 bullet 2 (HT only) | th3 on TF and TH; `higher` on TH | **HT content shown as base on TF (th3).** Badge **Higher · Triple**. The spec's version also weighs **yield, rate, equilibrium position and usefulness of by-products**. th3 implies atom economy alone decides (C14). |
| R6 | Atom economy vs percentage yield (th3; common_mistake; key_note) | triple | 4.3.3.1, 4.3.3.2 | TF, TH | OK |
| R7 | "Green chemistry"; substitution/elimination; pharmaceutical manufacturers (th3; `higher`) | NOT-IN-SPEC | — | TF, TH | Harmless. Keep out of the ladder; cut "pharmaceutical". |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | th1 | measures how much of the reactants' mass ends up in the desired product | OK | Matches the spec's definition. | 4.3.3.2 |
| C2 | th1 | "Atom economy (%) = (sum of Mr of desired products ÷ sum of Mr of ALL products) × 100. Note: this uses ALL products … not just the desired one." | **IMPRECISE (not AQA's form)** | AQA's denominator is the **sum of Mr of all reactants from the equation**. For a balanced equation, Σ Mr(reactants) = Σ Mr(products) (4.3.1.2), so every number in the pack comes out the same. But the pupil should be taught the form AQA prints and its mark schemes set out, plus the reason the products total is equal. | 4.3.3.2; 4.3.1.2 |
| C3 | th1 | high vs low atom economy = efficient vs wasteful | OK | — | 4.3.3.2 |
| C4 | th2 Ex 1 | Fe₂O₃ + 3CO → 2Fe + 3CO₂; 112 ÷ 244 × 100 = 45.9 % | OK arithmetic (✓ 112/244 = 0.4590; reactants 160 + 84 = 244 ✓) | — | 4.3.3.2 |
| C5 | th2 Ex 1 heading | "EXAMPLE 1 — high atom economy" (45.9 %) | **WRONG** | 45.9 % is the *lowest* value in the chunk, yet it is labelled high, while Example 3 at 56 % is labelled "low". The labels contradict each other. Re-cut: drop the high/low labels, or rank the three: 100 % > 56 % > 45.9 %. | — |
| C6 | th2 Ex 2 | nCH₂=CH₂ → (–CH₂–CH₂–)ₙ, one product, 100 % | OK | — | 4.7.3.1 |
| C7 | th2 | "addition reactions always have 100% atom economy because ALL reactant atoms form the single product" | OK | True when the addition gives one product, which is the GCSE case. | 4.3.3.2 |
| C8 | th2 Ex 3 | CaCO₃ → CaO + CO₂; 56 ÷ 100 × 100 = 56 %; "44 % of the mass becomes CO₂ waste" | OK (✓) | Label "low" — see C5. | — |
| C9 | th3 | green chemistry, economic and environmental benefits | OK | "Green chemistry" is not a spec term. | 4.3.3.2 |
| C10 | th3 | "Atom economy: a property of the EQUATION … Percentage yield: … how the EXPERIMENT is carried out" | OK | A clean, creditable distinction. | 4.3.3.1–2 |
| C11 | th3 | "Substitution/elimination reactions (multiple products): lower atom economy" | OK, NOT-IN-SPEC | The terms are not in GCSE; say "reactions with more than one product". | — |
| C12 | `higher` | "Calculate atom economy using Mr values" | OK / route: triple | See R2. | 4.3.3.2 |
| C13 | `higher` | "pharmaceutical manufacturers are encouraged…" | NOT-IN-SPEC | Cut. | — |
| C14 | th3 | "Chemists choose synthetic routes with higher atom economy when possible." | IMPRECISE / route: triple-higher | The spec's choice weighs atom economy *with* yield, rate, equilibrium position and usefulness of by-products. A high-atom-economy route with a slow rate or low yield may lose. | 4.3.3.2 (HT) |
| C15 | common_mistake | "Atom economy uses the relative formula masses of the PRODUCTS … — **not the reactants**. Divide the Mr of the DESIRED product by the sum of Mr of ALL products." | **WRONG** | This directly contradicts AQA's formula, whose denominator *is* the reactants. A pupil who learns it will think the formula AQA prints in the question stem or the mark scheme is a mistake. Re-cut: "Divide the Mr of the desired product (× its number in the equation) by the total Mr of all the reactants. Because mass is conserved, this equals the total Mr of all the products, so either total gives the same answer. The common slip is dividing by the desired product's Mr alone, or by the waste." The yield contrast in the second sentence is OK. | 4.3.3.2 |
| C16 | key_note | "Atom economy = (Mr desired product ÷ sum Mr all products) × 100" | IMPRECISE | Re-cut to AQA's form, as in C2. The rest of the key note is OK. | 4.3.3.2 |
| C17 | equations | "Atom economy (%) = (Mr of desired products ÷ sum of Mr of ALL products) × 100" | IMPRECISE (frozen) | Numerically valid, but not AQA's printed form. See §4. | 4.3.3.2 |
| C18 | FIFA | C₂H₄ + H₂O → C₂H₅OH; 46 ÷ 46 × 100 = 100 % | OK (✓ 28 + 18 = 46; 46/46) | The step labels are off. Step 2, labelled "I", only lists Mr values. Step 3, labelled "F", is the actual Insert. Keep the four verbatim steps. CFIFA C step: "Nothing to convert: Mr values have no units." Under AQA's form the denominator is C₂H₄ + H₂O = 28 + 18 = 46. A one-line Fine-tune note can show that this equals the product total. Hydration of ethene is an addition reaction ✓ (4.7.2.2). | 4.3.3.2 |
| C19 | matching (to be replaced) | 4 pairs | OK | "Lower atom economy — CaCO₃ decomposition" is consistent. Replace as the architecture requires. | — |
| C20 | q1 stem | "A reaction produces 80 g of desired product and 20 g of waste product. What is the atom economy?" | IMPRECISE | Atom economy is defined from the **equation**, not from collected masses. Masses that are actually collected are a *yield* idea, which is the confusion the lesson fights. It is only valid if these are the masses the equation predicts (complete reaction). | 4.3.3.2 |
| C21 | q1 key | 80 % | OK (✓) | — | — |
| C22 | q1 option 2 label | "20% — (20 ÷ 100) × 100 (calculated waste not yield)" | IMPRECISE | The label calls the desired-product fraction "yield", mixing the two terms the lesson separates. | 4.3.3.1–2 |
| C23 | q1 option 3 | "400 % — (80 ÷ 20) × 100" | OK (✓) | — | — |
| C24 | q1 option 4 + wx3 | "75 % — calculated incorrectly" / "No standard formula gives 75 % here" | IMPRECISE | No misconception is named (Law 10). | — |
| C25 | q2 key | only one product; all reactant atoms end up in it | OK | — | 4.3.3.2 |
| C26 | q2 wx1, wx2 | completeness is not the point; energy is not a product | OK | Good: wx1 separates atom economy from yield. | — |
| C27 | q2 option 4 + wx3 | Option: "The reactants have the same Mr as the products — so the ratio is always 1". wx3: "In addition reactions the product Mr equals the sum of reactant Mr exactly — but the key reason is …" | **WRONG (defensible distractor)** | Under **AQA's own formula** (desired Mr ÷ Σ reactant Mr), an addition reaction's ratio is 1 *precisely because* the single product's Mr equals the reactants' total. The wx itself concedes the statement is true. A pupil who reasons from the AQA formula picks a correct-in-substance option and is marked wrong. | 4.3.3.2 |

Count: **2 WRONG** in re-cuttable fields (C5 example label; C15 common_mistake). **1 WRONG** frozen (C27, q2 distractor). **6 IMPRECISE**: C2 and C16 (re-cuttable); C17 and C20 frozen; C22 and C24 (frozen distractor labels). **3 route mis-tags**: two triple lines tagged Higher (R2, R3), and route choice shown as base on TF (R5). FIFA arithmetic ✓.

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| TF, TH · q2 · "Why do addition reactions always have an atom economy of 100%?" | Option 4 is correct in substance under AQA's formula, and wx3 admits it (C27). That makes two defensible answers. | **Withhold on TF and TH** (precedent B2-W3: two creditable answers). |
| TF, TH · q1 · "A reaction produces 80 g of desired product…" | Stem conflates collected masses with equation masses (C20). One distractor carries no misconception (C24). | Keep in the bank. **Not a ladder rung** (Law 10). Rungs 1–2 must be authored from equations. |
| `equations[0]` (products denominator) | Frozen, numerically valid, not AQA's printed form (C17). | **Do not display** (precedent: lenses `equations[1]`, kept in data, never shown). Display AQA's form on the `equation` block, with a one-line note: "Σ Mr(reactants) = Σ Mr(products), because mass is conserved." Log it in DEPARTURES §2. |
| FIFA (ethanol) | Correct; labels slightly off (C18). | Keep verbatim with the C step in front. |
| (not frozen) common_mistake, key_note, th1 formula | C15 WRONG, C16 and C2 IMPRECISE. | Re-cut to AQA's reactant form. Do not show the common_mistake text verbatim. |
| (not frozen) th2 "high"/"low" labels | C5 WRONG. | Re-cut. |
| (not frozen) th3 "COMPARING ROUTES" | Triple-higher, and imprecise (R5, C14). | Badge **Higher · Triple**. Teach the full list of factors. |

## 5. For the lesson author

**What this lesson owns:** the definition, the calculation from a balanced equation (AQA's reactant form), why high atom economy matters (sustainability and economics), the contrast with percentage yield, and (Higher · Triple) choosing a pathway from atom economy, yield, rate, equilibrium position and by-product usefulness. Percentage yield itself is `percentage-yield` (batch 2).

**Misconceptions seen in AQA marking**
- Forgetting the coefficient on the desired product (using Mr(Fe) = 56, not 2 × 56 = 112).
- Dividing by the waste product only, or by the desired product only.
- Confusing atom economy with percentage yield, or using experimental masses.
- "Atom economy of 100 % means the reaction is complete or fast."
- Inverting the fraction, giving answers over 100 %.
- Rounding: giving 45.9 % as 46 % without saying so, or to 1 s.f.
- HT pathway questions answered with atom economy alone, ignoring rate, yield, equilibrium and by-products. Also, "the CO₂ by-product is waste" when the data says it can be sold or used.

**Command words:** Calculate, Give, Explain, Evaluate (HT), Suggest, Compare.

**Typical questions** ⚑ examiner-drafted
- ⚑ 3 marks, Calculate, **triple**: *"Ethanol can be made by fermentation: C₆H₁₂O₆ → 2C₂H₅OH + 2CO₂. Calculate the percentage atom economy for making ethanol. (Mr: C₆H₁₂O₆ = 180, C₂H₅OH = 46)"*
  - (1) 2 × 46 = 92.
  - (1) 92 ÷ 180 × 100.
  - (1) 51.1 %. Allow 51 %.
- ⚑ 1 mark, Give, **triple**: *"Give one reason why industry prefers reactions with a high atom economy."* — Accept any one of:
  - less waste;
  - more sustainable / conserves raw materials;
  - more economical / cheaper.
- ⚑ 2 marks, Explain, **triple**: *"Explain why the atom economy for making ethanol from ethene and steam is 100 %."*
  - (1) Only one product is formed (addition).
  - (1) So all the atoms in the reactants end up in the desired product / no waste products.
- ⚑ 6 marks, Evaluate, **Higher · Triple**: *"Ethanol can be made by fermentation or by hydration of ethene. Use the data to evaluate the two methods."* (Data table: atom economy 51 % vs 100 %; rate slow vs fast; conditions 30 °C vs 300 °C/60–70 atm; raw material renewable sugar vs crude oil; yield/purity; by-product CO₂.)
  - **Level 3 (5–6):** compares both methods on at least 4 factors, including atom economy, and reaches a justified conclusion.
  - **Level 2 (3–4):** compares both methods on some factors; conclusion weak or absent.
  - **Level 1 (1–2):** isolated points about one method.
  - Indicative content: 100 % vs 51 % atom economy; fermentation produces CO₂ waste (but it can be used); hydration is continuous and faster; fermentation uses renewable sugar, while ethene comes from finite crude oil; hydration needs high temperature and pressure, so it costs more energy; fermentation gives a dilute product that must be distilled.

**Required practical:** none.

**Equations to learn** (no chemistry equation sheet; all must be recalled)
- % atom economy = (Mr of desired product from equation ÷ Σ Mr of all reactants from equation) × 100. **Triple.**
- Equivalent check: Σ Mr(reactants) = Σ Mr(products). **Base** (4.3.1.2).

**CFIFA examples the author must write new**
- Nothing to convert: the ethanol FIFA, with C = "nothing to convert".
- A second worked example that exercises the coefficient on the desired product (iron: 2 × 56). For example: Fe₂O₃ + 3CO → 2Fe + 3CO₂ = 112 ÷ (160 + 84) × 100 = 45.9 %. Atom economy has no unit conversion. The CFIFA "wrong unit" example in this lesson can only be a value given in a different form, for example "0.459 → 45.9 %". Do not invent a mass-unit conversion where none exists.
- Significant figures: Mr data are integers, so answers to 3 s.f. are standard. Credit 2 s.f. where the data warrant it.

## 6. Verdict
**SOURCE WRONG IN PLACES.**
- **The formula's denominator.** The pack teaches the formula with all **products** as the denominator. Its common_mistake explicitly tells pupils **not** to use the reactants, which is the form AQA prints. The numbers agree (conservation of mass), so no keyed answer is wrong, but the explanation is. Re-cut to AQA's form, and do not display the frozen equation.
- **Wrong label.** th2 labels 45.9 % "high" and 56 % "low".
- **Frozen q2.** It has a correct-in-substance distractor: withhold it.
- **Route mis-tags.** Two triple lines are tagged Higher, and route choice (Higher · Triple) is shown on TF.

**For Mide:** none. This is not an AQA-source conflict: AQA's form is unambiguous, and the products form is equivalent. The departure is ours.
