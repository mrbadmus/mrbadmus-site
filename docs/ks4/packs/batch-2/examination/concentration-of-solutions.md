# Examination — Concentration of Solutions (concentration-of-solutions) — AQA 8464 5.3.2.5 / 8462 4.3.2.5 (+ 8462 4.3.4 triple-higher)
Verdict: SOURCE OK WITH FLAGS
Examiner: Opus, 1 Oct 2026. Pack examined: `docs/ks4/packs/batch-2/chemistry-5.3.2.5-concentration-of-solutions.md`.
Spec sources fetched from filestore.aqa.org.uk and read as text: AQA-8462-SP-2016.PDF and AQA-8464-SP-2016.PDF, both Version 1.1, 04 Oct 2019.

Route copies, checked directly:
- CH and TH are identical, and both carry the `higher` field (mol/dm³ and titration).
- CF and TF differ **only** in `higher` (`null`).
- Theory, quiz, FIFA, equations and key note are identical on all four routes.

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n; th1–th3 = theory chunks.

## 1. Spec reference
| spec | section | title | page | label |
|---|---|---|---|---|
| 8464 | **5.3.2.5** | Concentration of solutions | p.88 | base, plus one HT bullet |
| 8462 | **4.3.2.5** | Concentration of solutions | p.40 | base, plus one HT bullet |
| 8462 | **4.3.4** | Using concentrations of solutions in mol/dm³ (chemistry only) (HT only) | p.42 | triple-higher; no 8464 equivalent |
| 8462 | 4.4.2.5 | Titrations (chemistry only), HT calculation bullet | p.48 | triple-higher |

BATCH-PLAN ("5.3.2.5 · CF CH TF TH · g/dm³ (mol/dm³ triple HT)") is right.

Spec statement (verbatim, identical in both): "Many chemical reactions take place in solutions. The concentration of a solution can be measured in mass per given volume of solution, eg grams per dm3 (g/dm3). Students should be able to: calculate the mass of solute in a given volume of solution of known concentration in terms of mass per given volume of solution; (HT only) explain how the mass of a solute and the volume of a solution is related to the concentration of the solution."
For 8462 4.3.4, see the quotation in `using-moles-calculations.md` §1.

## 2. Route table
| # | teachable point | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Concentration = mass of solute per volume of solution; g/dm³ (th1; key_note) | base | 4.3.2.5 | all four | OK |
| R2 | c = m ÷ V and both rearrangements; cm³ → dm³ (th2; equations; FIFA; q1; q2; common_mistake) | base | 4.3.2.5 ("calculate the mass of solute…"; MS 3b change the subject) | all four | OK |
| R3 | "Concentrated" and "dilute" as words (th1) | base (vocabulary) | 4.3.2.5 | all four | OK |
| R4 | **Explaining** how mass of solute and volume of solution relate to concentration (th1 qualitative lines; th3 "amount same, volume up, concentration down"; key_note "Dilution: same mass, larger volume, lower concentration") | **higher** | 4.3.2.5 "(HT only) explain how the mass of a solute and the volume of a solution is related to the concentration" | all four | **HT explanation shown as base on CF and TF.** Tag it `higher`. Foundation keeps the calculation and the vocabulary, but not the "explain the relationship" task as a rung. |
| R5 | c₁V₁ = c₂V₂ dilution formula (th3; key_note) | NOT-IN-SPEC | absent from 4.3.2.5 and 4.3.4 | all four | Cut it from the key note. If it is kept at all, keep it as an untested aside on H routes. **Never a rung.** |
| R6 | Serial dilution (th3) | NOT-IN-SPEC (chemistry) | — | all four | Cut. |
| R7 | g/cm³ as a second unit (th1) | NOT-IN-SPEC | 4.3.2.5 names g/dm³ only | all four | Cut. It invites unit confusion with density. |
| R8 | mol/dm³; converting g/dm³ ↔ mol/dm³ with Mr; "mol/dm³ is the standard unit in Higher-level calculations" (`higher`) | **triple-higher** | 8462 4.3.4 (chemistry only, HT only) | CH, TH | **Chemistry-only on Combined Higher.** Tag it `triple-higher`. The sentence "standard unit in Higher-level calculations" is **false for Combined Higher**, who never use mol/dm³. |
| R9 | Titration data → unknown concentration (`higher`) | **triple-higher** | 8462 4.4.2.5 (HT) | CH, TH | **Chemistry-only on CH.** Its home is `titrations`. |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | th1 | "how much solute is dissolved per unit volume of solution" | OK | — | 4.3.2.5 |
| C2 | th1 | "two ways at Foundation level … g/cm³ … less common" | IMPRECISE / NOT-IN-SPEC | AQA uses g/dm³ only, at both tiers. Drop g/cm³ and "at Foundation level". | 4.3.2.5 |
| C3 | th1 | "1 dm³ = 1000 cm³ = 1 litre" | OK | — | MS |
| C4 | th2 | c = m/V; m = c × V; V = m/c; 250 cm³ = 0.250 dm³; 500 cm³ = 0.500 dm³ | OK | — | 4.3.2.5 |
| C5 | th2 ex.1 | "10 g of NaCl dissolved in 0.5 dm³ (500 cm³) of water … 20 g/dm³" | IMPRECISE | The arithmetic is right. Concentration uses the volume of **solution**, so write "to make 0.5 dm³ of solution". | 4.3.2.5 ("volume of solution") |
| C6 | th2 ex.2 | 50 g/dm³ × 0.2 dm³ = 10 g | OK | — | — |
| C7 | th2 ex.3 | 8 ÷ 16 = 0.5 dm³ = 500 cm³ | OK | — | — |
| C8 | th3 | dilution: solute amount same, volume up, concentration down | OK (science) / route **higher** | See R4. | 4.3.2.5 HT |
| C9 | th3 | 40 × 0.1 = c₂ × 0.4 → c₂ = 10 g/dm³ | OK (arithmetic) / NOT-IN-SPEC | See R5. | — |
| C10 | th3 | serial dilution 100 → 10 → 1 g/dm³ | OK (arithmetic) / NOT-IN-SPEC | See R6. | — |
| C11 | `higher` | "c (mol/dm³) = mass (g) ÷ (Mr × V (dm³))" | OK (science) / route **triple-higher** | Correct. | 8462 4.3.4 |
| C12 | `higher` | "mol/dm³ is the standard unit in Higher-level calculations" | **WRONG for CH** / IMPRECISE for TH | It is false for Combined Higher. For TH, write "Triple Higher papers also use mol/dm³". | 8462 4.3.4; 8464 (absent) |
| C13 | common_mistake | forgetting ÷1000 gives answers 1000 times too large or too small | OK | — | — |
| C14 | key_note | first four sentences | OK | — | 4.3.2.5 |
| C15 | key_note | "Dilution: same mass, larger volume, lower concentration. c₁V₁ = c₂V₂." | route **higher** / NOT-IN-SPEC | Keep the dilution sentence on H routes only. Cut c₁V₁ = c₂V₂. | 4.3.2.5 HT |
| C16 | equations 1–3 | the three g/dm³ forms | OK | All must be recalled; there is no chemistry equation sheet. | 4.3.2.5 |
| C17 | FIFA | 15 g in 500 cm³ → 0.5 dm³ → 30 g/dm³ | OK | Arithmetic correct. Sig figs: 2 s.f. data gives 30 g/dm³ ✓. **CFIFA Convert step:** "500 cm³ ÷ 1000 = 0.5 dm³". The verbatim I step, which repeats the conversion, then follows unchanged. | 4.3.2.5 |
| C18 | variables | c g/dm³; m g; V dm³ | OK | — | — |
| C19 | matching (to be replaced) | 10 g/dm³; 5 g; 0.2 dm³; 20 g/dm³ (dilution) | OK (arithmetic) | Item 4 is a c₁V₁ dilution item, which is NOT-IN-SPEC. Do not carry it into the replacement. | — |
| C20 | q1 stem | "25 g of glucose is dissolved in 500 cm³ of water" | IMPRECISE | Same issue as C5, the volume of water versus the volume of solution. The keyed number is unaffected at GCSE. | 4.3.2.5 |
| C21 | q1 key | 50 g/dm³ | OK | — | — |
| C22 | q1 distractors + wx | 0.05 (÷500, "1000× too small") ✓; 12500 (×500) ✓; 2.5 (÷10) ✓ | OK | All arithmetic and diagnoses are correct. | — |
| C23 | q2 key | 80 g/dm³ × 0.25 dm³ = 20 g | OK | — | 4.3.2.5 |
| C24 | q2 option 1 + wx1 | 20000 g = 80 × 250 | OK | — | — |
| C25 | q2 option 2 + wx2 | "0.32 g — mass = 80 ÷ 250"; wx2 "Dividing gives volume, not mass." | **WRONG (wx2)** | 80 ÷ 250 = 0.32 is right, but concentration ÷ volume is not a volume. Volume = mass ÷ concentration. The feedback teaches a false relationship. It should say: "Mass = concentration × volume; dividing concentration by volume gives nothing meaningful." | 4.3.2.5 |
| C26 | q2 option 3 | "320 g — mass = 80 × (250 ÷ 10)" | **WRONG (arithmetic)** | 80 × 25 = 2000, not 320. The distractor's own working does not produce its answer. wx3 ("250 ÷ 10 = 25 — but the conversion is ÷ 1000") is itself correct. | — |

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| all routes · q2 · "A solution has a concentration of 80 g/dm³. What mass of solute is in 250 cm³…" | The keyed answer (20 g) is right. One distractor's working gives 2000, not its stated 320, and wx2 teaches a false relationship ("dividing gives volume"). | Keep verbatim. **Do not use it as a ladder rung on any route.** Write a new rung-2 apply item: mass from concentration and volume, with a Convert step. |
| all routes · q1 · "25 g of glucose is dissolved in 500 cm³ of water…" | The "of water" wording is imprecise, but every number and explanation is right. | Usable as rung 2 on all four routes. |

The `higher` field is not a quiz item but is frozen-adjacent. **Its CH copy must not render.** All of it is triple-higher (R8, R9).

## 5. For the lesson author

**Misconceptions commonly seen**
- **Not converting cm³ to dm³.** The answer comes out 1000× wrong. This is a recurring point in AQA examiner reports on concentration questions.
- **Converting the wrong way:** ×1000 instead of ÷1000.
- **Volume of solvent added versus final volume of solution.**
- **Inverting the formula:** V ÷ m.
- **"A larger volume of the same solution has a higher concentration"**, confusing amount with concentration. The HT explain bullet targets this directly.
- **"Diluting removes solute."**
- **Unit errors:** writing g/cm³ or g instead of g/dm³.
- **TH:** confusing g/dm³ with mol/dm³, and forgetting ×Mr or ÷Mr when converting.

**Command words:** Calculate, Give the unit, Explain (HT), Determine, Show that, Give your answer to n significant figures.

**Typical questions (⚑ examiner-drafted)**
- ⚑ examiner-drafted, 2 marks, Calculate, **base**: *"Calculate the mass of sodium chloride in 250 cm³ of a solution of concentration 40 g/dm³."*
  - (1) 250 cm³ = 0.25 dm³.
  - (1) 10 g.
- ⚑ examiner-drafted, 3 marks, Calculate, **base**: *"A student dissolves 6.0 g of copper sulfate to make 150 cm³ of solution. Calculate the concentration in g/dm³."*
  - (1) Converts: 0.150 dm³.
  - (1) 6.0 ÷ 0.150.
  - (1) 40 g/dm³.
- ⚑ examiner-drafted, 2 marks, Explain, **higher**: *"A student makes solution A by dissolving 5 g of salt in 100 cm³ of solution and solution B by dissolving 5 g in 200 cm³. Explain which is more concentrated."*
  - (1) A is more concentrated.
  - (1) Same mass of solute in a smaller volume of solution, or more mass per dm³ (50 vs 25 g/dm³).
- ⚑ examiner-drafted, 3 marks, Calculate, **triple-higher**: *"Calculate the concentration in mol/dm³ of a solution containing 4.0 g of NaOH in 250 cm³ (Mr 40)."*
  - (1) n = 4.0 ÷ 40 = 0.10 mol.
  - (1) V = 0.250 dm³.
  - (1) 0.40 mol/dm³.
- ⚑ examiner-drafted, 4 marks, Describe, **base** (practical context): *"Describe how to make 250 cm³ of a 20 g/dm³ solution of sodium chloride."*
  - (1) Calculate and weigh 5.0 g.
  - (1) Dissolve in a smaller volume of distilled water in a beaker.
  - (1) Transfer to a 250 cm³ volumetric flask, rinsing the beaker into it.
  - (1) Make up to the mark with distilled water and mix or invert.
  - This is a practical-skills context (AT 1). A volumetric flask is not named in 4.3.2.5, so flag it as an extension, not core.
- A 6-mark extended response on 4.3.2.5 alone is not typical. Use the 4-mark describe or HT explain item for rung 4.

**Required practical:** none. The `rp` field is empty, which is correct.

**Equations to learn (recalled)**
- concentration (g/dm³) = mass of solute (g) ÷ volume of solution (dm³), with both rearrangements. **Base.**
- cm³ ÷ 1000 = dm³. **Base.**
- concentration (mol/dm³) = moles ÷ volume (dm³); g/dm³ = mol/dm³ × Mr. **Triple-higher.**

**CFIFA pair, as the amendment requires:** the existing FIFA (15 g, 500 cm³) is the Convert case. The author needs a "nothing to convert" worked example, for example 12 g in 0.40 dm³ → 30 g/dm³.

## 6. Verdict
**SOURCE OK WITH FLAGS.**
- **Route corrections (3).**
  - The HT "explain the relationship" content (dilution reasoning) is shown as base on CF and TF.
  - The `higher` field (mol/dm³ and titration) is chemistry-only but is served on Combined Higher.
  - Its claim that "mol/dm³ is the standard unit in Higher-level calculations" is false for CH.
- **NOT-IN-SPEC (3).** c₁V₁ = c₂V₂, serial dilution, g/cm³.
- **WRONG (2).** q2 distractor arithmetic and q2 wx2, both frozen.
- **IMPRECISE (3).** "Of water" (C5, C20) and "at Foundation level" (C2).

Only Mide can rule: **none.**

Note for the commander: there is no `examiner_tip`. 8462 4.3.4 (mol/dm³) has no lesson of its own in the data, so this lesson's TH layer and `titrations` TH are where it must live. Tell the author which one owns the explanation, and have the other link to it.
