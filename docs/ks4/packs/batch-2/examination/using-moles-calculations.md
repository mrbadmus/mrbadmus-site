# Examination — Using Moles: Calculations and Limiting Reactants (using-moles-calculations) — AQA 8464 5.3.2.3–5.3.2.4 / 8462 4.3.2.3–4.3.2.4 (HT only)
Verdict: SOURCE OK WITH FLAGS. **The pack does not teach its own first spec point.**
Examiner: Opus, 1 Oct 2026. Pack examined: `docs/ks4/packs/batch-2/chemistry-5.3.2.3-using-moles-calculations.md`.
Spec sources fetched from filestore.aqa.org.uk and read as text: AQA-8462-SP-2016.PDF and AQA-8464-SP-2016.PDF, both Version 1.1, 04 Oct 2019.
Route copies: the record exists only in `all_subtopics_chemistry_higher.py` (CH) and `all_subtopics_chemistry_triple_higher.py` (TH), and the two are identical in every field. The whole lesson is on Higher routes, which is correct for 4.3.2.3–4.3.2.4.

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n; th1–th3 = theory chunks.

## 1. Spec reference
| spec | section | title | page | label |
|---|---|---|---|---|
| 8464 | **5.3.2.3** | Using moles to balance equations (HT only) | p.87 | higher |
| 8464 | **5.3.2.4** | Limiting reactants (HT only) | p.88 | higher |
| 8462 | **4.3.2.3** | Using moles to balance equations (HT only) | p.39 | higher |
| 8462 | **4.3.2.4** | Limiting reactants (HT only) | p.40 | higher |
| what th1 actually teaches | 8462 **4.3.4** | Using concentrations of solutions in mol/dm³ (chemistry only) (HT only) | p.42 | **triple-higher**, and not in 8464 |
| what th1 actually teaches | 8462 **4.4.2.5** | Titrations (chemistry only), "(HT Only) calculate the chemical quantities in titrations…" | p.48 | **triple-higher**, and not in 8464 |
| prerequisite | 8464 5.3.2.1–5.3.2.2 / 8462 4.3.2.1–4.3.2.2 | Moles; Amounts of substances in equations (both HT only) | p.86–87 / p.38–39 | higher; taught in the `moles` and `amounts-in-equations` lessons |

BATCH-PLAN ("5.3.2.3–5.3.2.4 · CH TH · balancing from masses; limiting reactant") is right about the spec. The data does not match it.

Spec statements (verbatim, identical in 8462 and 8464):
- 4.3.2.3: "The balancing numbers in a symbol equation can be calculated from the masses of reactants and products by converting the masses in grams to amounts in moles and converting the numbers of moles to simple whole number ratios. Students should be able to balance an equation given the masses of reactants and products."
- 4.3.2.4: "In a chemical reaction involving two reactants, it is common to use an excess of one of the reactants to ensure that all of the other reactant is used. The reactant that is completely used up is called the limiting reactant because it limits the amount of products. Students should be able to explain the effect of a limiting quantity of a reactant on the amount of products it is possible to obtain in terms of amounts in moles or masses in grams."
- 8462 4.3.4 (chemistry only, HT only): "The concentration of a solution can be measured in mol/dm3 … If the volumes of two solutions that react completely are known and the concentration of one solution is known, the concentration of the other solution can be calculated."

## 2. Route table
| # | teachable point | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Concentration in mol/dm³, c = n ÷ V, rearrangements, cm³→dm³ (th1; equations 1–2; variables; key_note; summary; q1) | **triple-higher** | 8462 4.3.4 (chemistry only, HT only); absent from 8464 | CH, TH | **Chemistry-only content served on Combined Higher.** Tag it `triple-higher`. It does not render on CH. |
| R2 | Titration calculation (25.0 cm³ NaOH vs 20.0 cm³ 0.1 mol/dm³ HCl) (th1) | **triple-higher** | 8462 4.4.2.5 (HT) + 4.3.4 | CH, TH | **Chemistry-only on CH.** Tag it `triple-higher`. Its natural home is `titrations` (TH layer). |
| R3 | Limiting reactant and excess: definition (th2; common_mistake; key_note) | higher | 4.3.2.4 | CH, TH | OK |
| R4 | Limiting-reactant calculation, Mg + 2HCl (th2; FIFA; q2) | higher | 4.3.2.4; 4.3.2.1–4.3.2.2 | CH, TH | OK |
| R5 | Empirical formula from masses (th3, mislabelled "Using Moles to Balance Equations") | higher, if kept | The term is not in 4.3. The procedure (masses → moles → simplest whole-number ratio) is exactly 4.3.2.3's. | CH, TH | Keep as an illustration of the ratio skill only, never as the spec point itself. |
| R6 | Molecular formula from empirical formula and Mr (th3; key_note; matching) | NOT-IN-SPEC | absent from 8462/8464 | CH, TH | Cut. |
| R7 | **Balancing an equation from reacting masses** | higher | **4.3.2.3**, the lesson's own spec point | **absent** | **MISSING.** The author must write it new. See §5 for a checked example. |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | th1 | c = n ÷ V; n = c × V; V = n ÷ c; 1 dm³ = 1000 cm³ | OK (science) / route **triple-higher** | — | 4.3.4 |
| C2 | th1 | 0.5 mol in 250 cm³ → 0.25 dm³ → 2 mol/dm³ | OK | — | 4.3.4 |
| C3 | th1 | 100 cm³ of 2 mol/dm³ → 0.2 mol | OK | — | 4.3.4 |
| C4 | th1 | titration: n(HCl) = 0.1 × 0.020 = 0.002; 1:1; c(NaOH) = 0.002 ÷ 0.025 = 0.08 mol/dm³ | OK / IMPRECISE (sig figs) | The arithmetic is correct. The volumes are given to 3 s.f., so an AQA answer would be 0.0800 mol/dm³ if the acid were 0.100 mol/dm³. As written, with 0.1, it is 0.08. Give the acid as 0.100 mol/dm³ and the answer as 0.0800 when this moves to `titrations`. | 4.4.2.5; MS 2a |
| C5 | th2 | definitions of limiting reactant and excess | OK | Matches the spec. | 4.3.2.4 |
| C6 | th2 / FIFA | n(Mg) = 2.4 ÷ 24 = 0.1; n(HCl) = 3.65 ÷ 36.5 = 0.1; HCl limiting; n(H₂) = 0.05; mass = 0.1 g | OK | All correct. Mr(HCl) = 36.5 and Mr(H₂) = 2. Sig figs: the data's least precise value is 2 s.f. (2.4 g), so 0.10 g is the best form. 0.1 g is acceptable. | 4.3.2.1–4.3.2.4 |
| C7 | th3 heading | "Using Moles to Balance Equations" | **WRONG (mislabelled)** | The chunk under this heading teaches empirical and molecular formulae, not balancing. See R7. | 4.3.2.3 |
| C8 | th3 | 4.0 g S + 4.0 g O → S 0.125, O 0.25 → 1:2 → SO₂ | OK (science) | The arithmetic is correct. Treat it as an illustration of the ratio skill (R5). | 4.3.2.3 (method) |
| C9 | th3 | CH₂ (14), Mr 56 → factor 4 → C₄H₈ | OK (arithmetic) / NOT-IN-SPEC | Cut. | — |
| C10 | common_mistake | "the one that runs out — not the one in smaller quantity … only the molar comparison matters" | OK | — | 4.3.2.4 |
| C11 | key_note | "c (mol/dm³) = n ÷ V" | route **triple-higher** | Must not render on CH. | 4.3.4 |
| C12 | key_note | "whichever runs out first limits yield" | IMPRECISE | "Yield" is a chemistry-only term (4.3.3.1). For CH, write "limits the amount of product", which is the spec's wording. | 4.3.2.4; 4.3.3 |
| C13 | key_note / equations 3 | empirical formula and molecular formula | NOT-IN-SPEC (molecular) / higher illustration (empirical) | See R5/R6. The "equation" "Empirical formula: divide masses by Ar → find simplest ratio" is a method, not an equation. | — |
| C14 | variables | c mol/dm³; n mol; V dm³ | OK / route triple-higher | — | 4.3.4 |
| C15 | matching 1–2 (to be replaced) | 0.2 mol in 500 cm³ → 0.4 mol/dm³; 2 mol/dm³ × 0.25 dm³ → 0.5 mol | OK / triple-higher | — | 4.3.4 |
| C16 | matching 3 | HCl limiting | OK | — | 4.3.2.4 |
| C17 | matching 4 | "SO — n(S)=50/32=1.56, n(O)=50/16=3.12, ratio 1:2 → SO₂ wait: …" | **WRONG** | It contradicts itself (it opens with "SO") and has a rounding slip (50/16 = 3.125 → 3.13). The matching is being replaced anyway. Do not carry this text over. | — |
| C18 | q1 stem | "dissolving 0.3 mol of KOH in 300 cm³ of water" | IMPRECISE | Concentration uses the volume of **solution**, not of the water added. AQA stems say "to make 300 cm³ of solution". | 4.3.4 |
| C19 | q1 key and distractors | 1 mol/dm³; 0.001 (÷300); 90 (×300); 0.3 (moles as concentration) | OK | All arithmetic matches its label. | 4.3.4 |
| C20 | q1 wx1–3 | convert to dm³; multiplies instead of divides; divide by volume in dm³ | OK | — | — |
| C21 | q2 key | 0.1 mol Na + 0.05 mol Cl₂ (2:1) → "Neither" is limiting | OK | The amounts are exactly stoichiometric, so both are completely used up and neither is in excess. AQA defines the limiting reactant as "the reactant that is completely used up", and in a stoichiometric mix that is both. "Neither is limiting / no excess" is the defensible key. AQA itself avoids this case. | 4.3.2.4 |
| C22 | q2 option 1 text + wx1 | Option: "Sodium — there is more Cl₂ than Na in molar terms". wx1: "Cl₂ is not in excess…" | IMPRECISE | The option text is numerically false (0.05 < 0.1), and wx1 answers a different claim from the one the option makes. wx1 is not untrue. | — |
| C23 | q2 wx2, wx3 | compare against the equation ratio; masses would be converted to moles | OK | — | 4.3.2.4 |
| C24 | FIFA structure | F / I / F / A | OK | **CFIFA Convert step:** "Nothing to convert: masses are already in grams." | — |

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| **CH** · q1 · "What is the concentration of a solution made by dissolving 0.3 mol of KOH…" | mol/dm³ is 8462 4.3.4 (chemistry only, HT). Combined Higher pupils are never taught or examined on it. | Keep verbatim. **Do not use it as a ladder rung or body item on CH.** It is usable on **TH** as rung 2, with the C18 wording caveat. Better placed in `concentration-of-solutions` (TH layer). |
| CH, TH · q2 · "A student mixes 0.1 mol Na with 0.05 mol Cl₂…" | Route is correct (higher). The stoichiometric "neither" case is a boundary case that AQA does not normally set. | Usable on both routes, as a misconception check in the body. **Prefer not to use it as rung 1 or 2.** A rung should use a clear limiting case like the FIFA. |

## 5. For the lesson author

**Content that must be written new (R7).** This is the lesson's own spec point, 4.3.2.3, and it is checked below.

*"4.8 g of magnesium reacts with 14.6 g of hydrogen chloride to make 19.0 g of magnesium chloride and 0.4 g of hydrogen. Use these masses to balance the equation Mg + HCl → MgCl₂ + H₂. (Ar: Mg 24, H 1, Cl 35.5)"*

| step | working |
|---|---|
| moles | Mg 4.8/24 = 0.20; HCl 14.6/36.5 = 0.40; MgCl₂ 19.0/95 = 0.20; H₂ 0.4/2 = 0.20 |
| divide by the smallest | 1 : 2 : 1 : 1 |
| answer | Mg + 2HCl → MgCl₂ + H₂ |
| mass check | 4.8 + 14.6 = 19.4 = 19.0 + 0.4 ✓ |

A second example, with a Convert step:

*"0.92 kg of sodium reacts with 0.32 kg of oxygen to make 1.24 kg of sodium oxide. Use the masses to balance Na + O₂ → Na₂O. (Ar: Na 23, O 16)"*

| step | working |
|---|---|
| Convert | 0.92 kg = 920 g; 0.32 kg = 320 g; 1.24 kg = 1240 g |
| moles | Na 920/23 = 40; O₂ 320/32 = 10; Na₂O 1240/62 = 20 |
| divide by the smallest | 4 : 1 : 2 |
| answer | 4Na + O₂ → 2Na₂O |
| mass check | 920 + 320 = 1240 ✓ |

**Misconceptions commonly seen**
- **The limiting reactant is the one with the smaller mass, or fewer moles.** This ignores the equation ratio. It is the pack's own common_mistake, and the strongest one to confront.
- **The reactant in excess "limits" the product.**
- **Using masses directly as the balancing numbers** instead of converting to moles first.
- **Not dividing by the smallest number of moles**, or rounding 1.5 to 2 instead of doubling to get whole numbers.
- **Using Mr(H) = 1 for hydrogen gas** instead of Mr(H₂) = 2, and likewise O₂ and Cl₂.
- **Ignoring the coefficient when converting moles of product.** For example, n(H₂) = n(HCl) instead of n(HCl) ÷ 2.
- **TH only:** forgetting cm³ → dm³ in c = n/V (an error of 1000×), and using the volume of water instead of the volume of solution.

**Command words:** Calculate, Determine, Explain (the effect of a limiting reactant), Show that, Balance, Give your answer to n significant figures.

**Typical questions (⚑ examiner-drafted)**
- ⚑ examiner-drafted, 4 marks, Calculate / Balance: the Mg + HCl masses above.
  - (1) Moles of any two substances correct.
  - (1) All four moles correct.
  - (1) Divides to the simplest whole-number ratio.
  - (1) Mg + 2HCl → MgCl₂ + H₂.
  - The final mark goes for the balanced equation even if it is reached by ratio without full working.
- ⚑ examiner-drafted, 4 marks, Calculate + Explain: *"2.4 g Mg and 3.65 g HCl. Identify the limiting reactant and calculate the maximum mass of hydrogen."*
  - (1) n(Mg) = 0.1 and n(HCl) = 0.1.
  - (1) 0.1 mol Mg needs 0.2 mol HCl, so HCl is limiting.
  - (1) n(H₂) = 0.05.
  - (1) 0.1(0) g.
- ⚑ examiner-drafted, 3 marks, Explain: *"Explain why an excess of acid is used when reacting it with a metal."*
  - (1) So that all of the metal reacts, or is used up.
  - (1) The metal is the limiting reactant.
  - (1) The amount of product is decided by the amount of the limiting reactant, and so is maximised for the metal used.
- A 6-mark extended response on this content is rare. Rung 4 should be a multi-step "determine the balanced equation, then the limiting reactant" problem, with the reasoning written out.

**Required practical:** none. (The titration RP, 8462 RP2, owns the TH titration calculation.)

**Equations to learn (all recalled; there is no chemistry equation sheet)**
- n = m ÷ Mr. **Higher**, 4.3.2.1.
- Masses → moles → simplest whole-number ratio. **Higher**, 4.3.2.3.
- c (mol/dm³) = n ÷ V (dm³). **Triple-higher**, 4.3.4.
- Mass (g) = c (mol/dm³) × V (dm³) × Mr. **Triple-higher**, 4.3.4.

## 6. Verdict
**SOURCE OK WITH FLAGS.**
- **Route corrections (2).** th1 (mol/dm³ and the titration calculation) and q1 are chemistry-only HT content served on Combined Higher. Tag them `triple-higher`.
- **Missing spec point (1).** 4.3.2.3, balancing from masses, has no source content at all.
- **WRONG (2).** The th3 heading and matching item 4.
- **NOT-IN-SPEC (1).** Molecular formula.
- **IMPRECISE (3).** C4 sig figs, C12, C18/C22.
- **Frozen items wrong for route (1).** q1 on CH.

Only Mide can rule: **none.** The routing follows directly from the "(chemistry only)" and "(HT only)" labels on 8462 4.3.4.

I am not fully certain whether AQA papers have ever set "empirical formula from masses" under 4.3.2.3. The spec text never uses the term outside 4.2.1.3, so it is tagged as an illustration, not a rung. This is a reading of spec text, not a conflict between AQA sources.

Note for the commander: there is no `examiner_tip`. Once R1/R2 are tagged correctly, the CH page loses all of th1, so check that the CH lesson still meets the instrument and prose budget with 4.3.2.3 added.
