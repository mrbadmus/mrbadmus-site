# Examination — Metabolism (metabolism) — AQA 8464 4.4.2.3 / 8461 4.4.2.3
Verdict: SOURCE HAS ERRORS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-7/04-checked-science-source/biology-4.4.2.4-metabolism.md`.
Spec sources read as text: `AQA-8464-spec.txt` (Trilogy v1.1, 4.4.2.3; 4.1.1.2; 4.2.2.1; 4.2.3.2; 4.5.3.6), `AQA-8461-spec.txt` (Biology v1.0, 4.4.2.3; 4.5.3.3 (biology only); 4.5.3.7). Route audit row `metabolism` (OK, CF CH TF TH). Runtime convention checked in `generate_site_v5.py`: `wrong_explanations` key n is shown for `opts[n]` (0-based).

Conventions: q1–q3 = quiz items; "wx n" = `wrong_explanations` key n; T1–T4 = theory blocks. Route copies: `higher` null on CF and TF (served CH/TH only). No FIFA, no `[NEW — to be examined]` line. **wx alignment checked: all three items correctly paired; no shift.**

**Spec ref:** the file and site label 4.4.2.4; true ref **4.4.2.3** in both specs (F8).

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 | **4.4.2.3** | Metabolism | base |
| 8461 | **4.4.2.3** | Metabolism | base |
| Layer | 8461 4.5.3.3 (deamination → ammonia → urea in liver) | Maintaining water and nitrogen balance | **(biology only)** + **(HT only)** |
| Layer | 8461 4.5.3.3 (kidneys filter urea) | | **(biology only)** |
| Layer | 8464 4.5.3.6 / 8461 4.5.3.7 (thyroxine stimulates basal metabolic rate) | Feedback systems / Negative feedback | **(HT only)** |
| Supporting | 4.1.1.2 (ribosomes); 4.2.2.1 (digestive enzymes); 4.2.3.2 (plasma carries urea to kidney) | | base |

Spec statements (verbatim, 8464 = 8461): "Students should be able to explain the importance of sugars, amino acids, fatty acids and glycerol in the synthesis and breakdown of carbohydrates, proteins and lipids. Metabolism is the sum of all the reactions in a cell or the body. The energy transferred by respiration in cells is used by the organism for the continual enzyme controlled processes of metabolism that synthesise new molecules. Metabolism includes: conversion of glucose to starch, glycogen and cellulose; the formation of lipid molecules from a molecule of glycerol and three molecules of fatty acids; the use of glucose and nitrate ions to form amino acids which in turn are used to synthesise proteins; respiration; breakdown of excess proteins to form urea for excretion." 8461 4.5.3.3: "(HT only) … In the liver these amino acids are deaminated to form ammonia. Ammonia is toxic and so it is immediately converted to urea for safe excretion." 4.5.3.6/4.5.3.7 (HT only): "Thyroxine from the thyroid gland stimulates the basal metabolic rate."

## 2. Route table
| # | teachable point | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Definition: sum of all reactions (T1; key_note; common_mistake; q1) | base | 4.4.2.3 | all four | OK |
| R2 | Anabolism/catabolism labels (T1–T3; key_note; q3) | off-spec labels for base content (synthesis/breakdown) | 4.4.2.3 | all four | OK (F7) |
| R3 | Protein synthesis at ribosomes (T2; q3) | base | 4.4.2.3; 4.1.1.2 | all four | OK |
| R4 | Glucose → cellulose, starch, glycogen (T2) | base | 4.4.2.3 | all four | OK |
| R5 | Fatty acids + glycerol → lipid (T2) | base | 4.4.2.3 | all four | WRONG detail (F1) |
| R6 | Glucose + nitrate ions → amino acids | base | 4.4.2.3 | **missing** | GAP (F3) |
| R7 | Respiration (T3) | base | 4.4.2.3 | all four | OK |
| R8 | Digestion (T3; q3 opt) | base (link) | 4.2.2.1 | all four | IMPRECISE (F2) |
| R9 | Deamination, ammonia, liver (T3, T4; `higher`; matching 5; q2) | **triple-higher** | 8461 4.5.3.3 | all four (`higher` CH/TH) | ROUTE (F4) |
| R10 | Urea in blood to kidneys (T4) | base; filtration = **triple** | 4.2.3.2; 8461 4.5.3.3 | all four | ROUTE (F4) |
| R11 | Thyroxine → BMR (T4; `higher`) | **higher** | 8464 4.5.3.6 / 8461 4.5.3.7 | T4 all four; `higher` CH/TH | ROUTE (F5) |
| R12 | Metabolic-rate factors, ectotherms, glycolysis, DNA replication (T2–T4; `higher`) | off-spec | — | all four | OK (F7) |
| R13 | q1, q3 | base | 4.4.2.3 | all four | OK |
| R14 | q2 | **triple-higher** | 8461 4.5.3.3 | all four | ROUTE (F4); wx2 IMPRECISE (F6) |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | T1 | metabolism = sum of all reactions in a cell or organism | OK | Spec wording. | 4.4.2.3 |
| C2 | T1 | catabolism releases energy; anabolism requires energy | OK (off-spec labels) | — | — |
| C3 | T2 | amino acids → proteins, needs ATP, at ribosomes | OK | ATP off-spec; spec: energy from respiration. | 4.4.2.3; 4.1.1.2 |
| C4 | T2 | glucose → cellulose (cell walls) | OK | — | 4.4.2.3 |
| C5 | T2 | glucose → starch (plants), glycogen (liver, muscles) | OK | — | 4.4.2.3; 4.5.3.2 |
| C6 | T2 | "Fatty acids + glycerol → triglycerides (for cell membranes, energy storage, insulation)" | WRONG | Membranes are built from phospholipids, not triglycerides. Spec: "lipid molecules from a molecule of glycerol and three molecules of fatty acids" — for energy storage and insulation. | 4.4.2.3 |
| C7 | T2 | nucleotides → DNA before division | OK (off-spec) | — | — |
| C8 | T3 | respiration: glucose + oxygen → CO₂ + water | OK | — | 4.4.2.1 |
| C9 | T3 | "Starch → maltose → glucose (by amylase)" | IMPRECISE | Amylase gives maltose; maltase gives glucose. Spec: carbohydrases → simple sugars; amylase breaks down starch. | 4.2.2.1 |
| C10 | T3 | proteins → amino acids (proteases); fats → fatty acids + glycerol (lipase) | OK | — | 4.2.2.1 |
| C11 | T3 | glycolysis first step, in cytoplasm | OK (off-spec) | — | — |
| C12 | T3; T4 | deamination in liver; amino group removed → ammonia → urea; carbon skeleton respired | OK, **triple-higher** | — | 8461 4.5.3.3 (HT only) |
| C13 | T3 | all reactions enzyme-controlled → temperature/pH matter | OK | Spec: "continual enzyme controlled processes". | 4.4.2.3; 4.2.2.1 |
| C14 | T4 | body size: higher total, lower per gram | OK (off-spec) | — | — |
| C15 | T4 | muscle mass, exercise raise metabolic rate; ectotherms | OK (off-spec) | — | — |
| C16 | T4 | "thyroxine … controls the basal metabolic rate" | OK, **HT** | Spec verb is "stimulates". | 8464 4.5.3.6 / 8461 4.5.3.7 |
| C17 | T4 | excess amino acids can't be stored | OK | — | 8461 4.5.3.3 |
| C18 | T4 | urea carried in blood to kidneys, filtered, excreted in urine | OK | Blood→kidney base (4.2.3.2); filtration triple (8461 4.5.3.3). | 4.2.3.2; 8461 4.5.3.3 |
| C19 | `higher` | rate affected by size, muscle, age, temperature, thyroxine; anabolism/catabolism examples; deamination → urea | OK | Thyroxine = HT; deamination = TH; rest base/off-spec. | as above |
| C20 | common_mistake | metabolism ≠ respiration; includes many reactions | OK | — | 4.4.2.3 |
| C21 | key_note | "Catabolism = breaking down (releases ATP)" | IMPRECISE | Releases energy, some used to make ATP (off-spec). | — |
| C22 | matching (to be replaced) | six pairs | OK | Pair 5 triple-higher. | — |
| C23 | q1 key | sum of all chemical reactions in a cell or organism | OK | — | 4.4.2.3 |
| C24 | q1 wx1 | metabolism includes both releasing and using reactions | OK | — | 4.4.2.3 |
| C25 | q1 wx2 | digestion is one part | OK | — | — |
| C26 | q1 wx3 | breathing/movement are consequences | OK | — | — |
| C27 | q2 key | excess amino acids can't be stored; deamination → urea | OK, **triple-higher** | Base form: "breakdown of excess proteins to form urea for excretion". | 8461 4.5.3.3 (HT only) |
| C28 | q2 wx1 | anaerobic in animals → lactic acid, not urea | OK | — | 4.4.2.1 |
| C29 | q2 wx2 | "CO₂ … is not converted to urea" | IMPRECISE | In the liver urea's carbon does come from CO₂ (as hydrogencarbonate). The real rebuttal: urea's nitrogen comes from amino acids; CO₂ and water contain no nitrogen. Key unaffected. | — |
| C30 | q2 wx3 | fat breakdown → fatty acids + glycerol, not urea | OK | — | 4.2.2.1 |
| C31 | q3 key | amino acids joined at ribosomes → protein (anabolic) | OK | Stem glosses "ANABOLIC (building)". | 4.4.2.3 |
| C32 | q3 wx1 | respiration breaks down glucose — catabolic | OK | — | — |
| C33 | q3 wx2 | digestion breaks down starch — catabolic | OK | Option 2 "starch → maltose by amylase in the mouth" ✓. | 4.2.2.1 |
| C34 | q3 wx3 | lactic acid from glucose breakdown — catabolic | OK | — | — |

Count: **1 WRONG** (C6, theory, re-cuttable). IMPRECISE: C9, C21, C29. ROUTE: deamination/liver, kidney filtration, thyroxine. GAP: glucose + nitrate → amino acids.

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| q2 | Stem places urea production in the liver; key names deamination — both 8461 4.5.3.3 (biology only)(HT only) | **Usable on TH only.** wx2 imprecise (F6). |
| q1, q3 | correct, base | Usable on all four routes. |

## 5. Verdict
SOURCE HAS ERRORS. One wrong theory claim (triglycerides for membranes). The spec's own list is missing "glucose and nitrate ions → amino acids → proteins" (added to the source from the spec). Deamination/liver/ammonia is Triple Higher and thyroxine is HT; both are currently served on all routes in theory. Ref should read 4.4.2.3. **For Mide:** nothing.
