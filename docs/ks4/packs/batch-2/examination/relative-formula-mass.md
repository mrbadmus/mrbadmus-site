# Examination — Relative Formula Mass (relative-formula-mass) — AQA 8464 5.3.1.2 / 8462 4.3.1.2
Verdict: SOURCE OK WITH FLAGS
Examiner: Opus, 1 Oct 2026. Pack examined: `docs/ks4/packs/batch-2/chemistry-5.3.1.2-relative-formula-mass.md`.
Spec sources fetched from filestore.aqa.org.uk and read as text: AQA-8462-SP-2016.PDF and AQA-8464-SP-2016.PDF, both Version 1.1, 04 Oct 2019.
Route copies: I checked these directly in `all_subtopics_chemistry*.py`. CH and TH are identical. CF and TF differ **only** in `higher`, which is `null` on both. Quiz, theory, FIFA and key note are identical on all four routes.

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n; th1–th3 = theory chunks.

## 1. Spec reference
| spec | section | title | page | label |
|---|---|---|---|---|
| 8464 | **5.3.1.2** | Relative formula mass | p.85 | base (whole section; no HT marker) |
| 8462 | **4.3.1.2** | Relative formula mass | p.37 | base |
| HT neighbours | 8464 5.3.2.1 / 8462 4.3.2.1 | Moles (HT only) | p.86 / p.38 | higher |
| | 8464 5.3.2.2 / 8462 4.3.2.2 | Amounts of substances in equations (HT only) | p.87 / p.39 | higher |

Spec statement (verbatim, identical in both): "The relative formula mass (Mr) of a compound is the sum of the relative atomic masses of the atoms in the numbers shown in the formula. In a balanced chemical equation, the sum of the relative formula masses of the reactants in the quantities shown equals the sum of the relative formula masses of the products in the quantities shown. Students should be able to calculate the percentage by mass in a compound given the relative formula mass and the relative atomic masses."
4.3.2.2 (HT only): "The masses of reactants and products can be calculated from balanced symbol equations … calculate the masses of reactants and products from the balanced symbol equation and the mass of a given reactant or product."

## 2. Route table
| # | teachable point | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Mr = sum of Ar (th1; equations; key_note; FIFA; q1; q2) | base | 4.3.1.2 | all four | OK |
| R2 | Brackets multiply everything inside (th2; common_mistake; q2) | base | 4.3.1.2; 4.3.1.1 (multipliers) | all four | OK |
| R3 | Sum of Mr of reactants (× coefficients) = sum of Mr of products: 48 + 32 = 80 (th3, first half) | base | 4.3.1.2 | all four | OK. Teach it as base. |
| R4 | Reading the ratio as grams ("48 g of Mg reacts with 32 g of O₂…") and scaling from a given mass (12 g Mg → 20 g MgO) (th3, second half; key_note "Mr is used to calculate mass ratios in reactions") | **higher** | 4.3.2.2 (HT only); grams per mole is 4.3.2.1 (HT only) | all four | **HT content shown as base on CF and TF.** Tag it `higher`. A Foundation pupil keeps only "the Mr totals balance". |
| R5 | Percentage by mass of an element in a compound (`higher` field) | **base** | 4.3.1.2 (no HT marker) | CH, TH only (CF/TF `higher` = null) | **Base content withheld from Foundation.** Tag it `base`. Foundation papers set this. The author must write it new, because no worked example exists in the pack. |
| R6 | Empirical formula from percentage composition (`higher` field) | higher (if taught) | Not named in 4.3. The term appears only in 4.2.1.3 (empirical formula of an ionic compound *from a diagram*). The masses → moles → whole-number-ratio procedure is 4.3.2.3 (HT only). | CH, TH | Out of scope for this lesson. It belongs with `using-moles-calculations` (batch 2 #5), tagged `higher`. **Not a rung here.** |
| R7 | Molecular formula from empirical formula and Mr (`higher` field) | NOT-IN-SPEC | absent from 8462/8464 | CH, TH | Cut. |
| R8 | Mr has no units; relative to carbon-12 (th1; key_note) | base | 4.3.1.2 (the unitless Mr is implied); C-12 not in spec | all four | OK. C-12 is harmless, but keep it out of the ladder. |

No chemistry-only content.

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | th1 | definition of Mr | OK | Near-verbatim spec. | 4.3.1.2 |
| C2 | th1 | "Mr has no units — it is a ratio (relative to carbon-12)" | OK | True. "Carbon-12" is beyond the spec but correct. | — |
| C3 | th1 | Ar list H 1, C 12, N 14, O 16, Na 23, Mg 24, S 32, Cl 35.5, Ca 40, Fe 56 | OK | Matches the AQA data-sheet periodic table. | — |
| C4 | th1 | H₂O 18; CO₂ 44; NaCl 58.5; MgO 40; H₂SO₄ 98; CaCO₃ 100 | OK | All arithmetic correct. | 4.3.1.2 |
| C5 | th2 | Ca(OH)₂ 74; Mg(NO₃)₂ 148; Al₂(SO₄)₃ 342 (Al = 27) | OK | 40+32+2; 24+28+96; 54+96+192. All correct. Al = 27 is not in th1's list, so add it where it is used. | 4.3.1.2 |
| C6 | th3 | "ratio of masses … equals the ratio of their Mr values (multiplied by the coefficients)"; 2 × 24 : 32 : 2 × 40 = 48 : 32 : 80 | OK | Correct. Here 48 + 32 = 80 is the base statement of 4.3.1.2. | 4.3.1.2 |
| C7 | th3 | "48 g of Mg reacts with 32 g of O₂ to produce 80 g of MgO"; "12 g Mg … scale factor 0.25 … 20 g" | OK (science) / **route: higher** | The arithmetic is correct (12 ÷ 48 = 0.25; 80 × 0.25 = 20). It is the HT 4.3.2.2 skill, so see R4. | 4.3.2.2 (HT) |
| C8 | th3 | "This is the foundation for all quantitative chemistry calculations." | OK | Rhetorical. | — |
| C9 | `higher` | "percentage mass of an element in a compound: (Ar × number of atoms ÷ Mr) × 100" | OK (science) / **route: base** | The formula is correct. See R5. | 4.3.1.2 |
| C10 | `higher` | empirical formula from % composition; molecular formula from Mr | NOT-IN-SPEC | See R6/R7. | 4.2.1.3; 4.3.2.3 |
| C11 | common_mistake | Ca(OH)₂ = 40 + 32 + 2 = 74 | OK | — | 4.3.1.2 |
| C12 | key_note | "Mr = sum of all Ar … Mr has no units" | OK | The clause "Mr is used to calculate mass ratios in reactions" is HT. On CF/TF, write "the Mr totals on each side of a balanced equation are equal" instead. | 4.3.1.2; 4.3.2.2 |
| C13 | equations | "Mr = sum of all Ar values in the formula" | OK | Must be recalled. GCSE Chemistry has no equation sheet. | 4.3.1.2 |
| C14 | FIFA | H₂SO₄: H 2, S 32, O 64 → 98 | OK | Arithmetic is correct, and an integer needs no significant-figure decision. **CFIFA Convert step:** "Nothing to convert: Ar values have no units." | 4.3.1.2 |
| C15 | variables | Mr, Ar with no unit | OK | — | — |
| C16 | matching (to be replaced) | H₂O 18; CO₂ 44; NaCl 58.5; CaCO₃ 100; Ca(OH)₂ 74 | OK | All correct. | — |
| C17 | q1 key | CaCO₃ = 100 | OK | — | 4.3.1.2 |
| C18 | q1 distractors | 68, 116, 52 | OK | 40+12+16; 40+12+64; 40+12. Arithmetic matches each label. | — |
| C19 | q1 wx1 | "CaCO₃ has only ONE oxygen — but the subscript 3 after O means THREE oxygens" | IMPRECISE | Read literally, the first clause asserts the misconception as a fact. The intended meaning is "You counted only one oxygen". | — |
| C20 | q1 wx2, wx3 | 3 O not 4; oxygen cannot be ignored | OK | — | — |
| C21 | q2 key | Mg(NO₃)₂ = 148 | OK | — | 4.3.1.2 |
| C22 | q2 distractors | 86, 100, 116 | OK | 24+14+48; 24+28+48; 24+28+64. All correct for their labels. | — |
| C23 | q2 wx1 | "So there is 1 N, NOT 2 — wait: NO₃ has 1 N and 3 O, multiplied by 2 = 2N and 6O." | **WRONG** | It contradicts itself on screen: it first asserts 1 N, then corrects itself mid-sentence. For the 86 distractor it should say: "The 2 outside the bracket doubles everything inside: 2 N and 6 O, not 1 N and 3 O." | 4.3.1.2 |
| C24 | q2 wx2, wx3 | 2N and 6O | OK | — | — |

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| all routes · q2 · "What is the Mr of Mg(NO₃)₂?" | The keyed answer is right, but wx1 contradicts itself ("1 N, NOT 2 — wait:") and is shown to any pupil who picks 86. | Keep verbatim. **Do not use it as a ladder rung on any route.** The bracket skill it tests must be trained with a new CFIFA "do" item instead. |
| all routes · q1 · "What is the relative formula mass of calcium carbonate…" | wx1 is badly worded but not false in intent. | Usable as rung 2 (apply) on all routes. |

No frozen item is route-wrong: both quiz items are base.

## 5. For the lesson author

**Misconceptions commonly seen**
- **Brackets.** Multiplying only the atom next to the subscript: Ca(OH)₂ → 40 + 16 + 2 = 58, or forgetting the bracket entirely.
- **Coefficient changes Mr.** Writing Mr(2H₂O) = 36. The coefficient multiplies the amount in the equation, not the Mr of one formula unit.
- **Diatomic elements.** Taking Mr(O₂) = 16 or Mr(Cl₂) = 35.5.
- **Using atomic number instead of Ar,** read from the wrong number on the periodic table.
- **Rounding Cl to 35** or Cu to 63.
- **Giving Mr a unit** (g or g/mol).
- **Percentage by mass:** forgetting the number of atoms (%H in H₂O as 1/18 instead of 2/18), or inverting the fraction (Mr ÷ Ar).

**Command words:** Calculate, Show that, Determine, Give (your answer to n significant figures).

**Typical questions (⚑ examiner-drafted)**
- ⚑ examiner-drafted, 2 marks, Calculate, **base**: *"Calculate the relative formula mass of magnesium nitrate, Mg(NO₃)₂."*
  - (1) A correct method showing the ×2 on N and O.
  - (1) 148.
- ⚑ examiner-drafted, 2 marks, Calculate, **base**: *"Calculate the percentage by mass of nitrogen in ammonium nitrate, NH₄NO₃."*
  - (1) Mr = 80 and N = 2 × 14 = 28.
  - (1) 28 ÷ 80 × 100 = 35 %.
  - Give the second mark for the correct answer even without working.
- ⚑ examiner-drafted, 3 marks, Show that, **base**: *"2Mg + O₂ → 2MgO. Show that the total Mr of the reactants equals the total Mr of the products."*
  - (1) 2 × 24 = 48 and 32.
  - (1) 2 × 40 = 80.
  - (1) 48 + 32 = 80.
- ⚑ examiner-drafted, 3 marks, Calculate, **higher only**: *"Calculate the mass of magnesium oxide formed from 12 g of magnesium."*
  - (1) 48 : 80, or moles of Mg = 0.5.
  - (1) Scale factor or ratio: 0.5 mol of MgO.
  - (1) 20 g.
- A 6-mark extended response is not typical for this content. Rung 4 should be a multi-step calculation explained in words, or the lesson's own produce task.

**Required practical:** none.

**Equations to learn (all must be recalled; there is no chemistry equation sheet)**
- Mr = Σ (Ar × number of atoms). **Base.**
- % by mass of element = (Ar × number of atoms of that element) ÷ Mr × 100. **Base.**
- Σ Mr(reactants, × coefficients) = Σ Mr(products, × coefficients). **Base.**
- Masses from equations (scale factor / moles). **Higher.**

**CFIFA examples the author must write new** (the pack has only H₂SO₄)
- One with "nothing to convert", for example %Mg in MgO = 24/40 × 100 = 60 %.
- One where a quantity arrives in the wrong unit. A pure Mr task never has a unit to convert, so build it on percentage by mass. For example: "What mass of magnesium, in grams, is in 2.0 kg of magnesium oxide?"
  - Convert: 2.0 kg → 2000 g.
  - Formula: %Mg = 60 %.
  - Answer: 0.60 × 2000 = 1200 g.
  - Base. Do not make it a ladder item unless it is reviewed.

## 6. Verdict
**SOURCE OK WITH FLAGS.**
- **Route corrections (2).** Reacting masses (th3 second half, key_note clause) are HT, but are served to CF and TF. Percentage by mass is base, but is withheld from CF and TF.
- **NOT-IN-SPEC (2).** Empirical formula from % composition (move it to `using-moles-calculations`, `higher`), and molecular formula (cut).
- **WRONG (1).** q2 wx1, frozen.
- **IMPRECISE (1).** q1 wx1.

Only Mide can rule: **none.**

Note for the commander: there is no `examiner_tip` in any route copy.
