# Examination — Electrolysis of Aqueous Solutions (electrolysis-aqueous) — AQA 8464 5.4.3.4 / 8462 4.4.3.4 (+ HT 8464 5.4.3.1, 5.4.3.5 / 8462 4.4.3.1, 4.4.3.5)
Verdict: SOURCE HAS ERRORS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-12/04-checked-science-source/chemistry-5.4.3.4-electrolysis-aqueous.md`.
Spec sources read as text: `AQA-8464-spec.txt` (v1.1) 5.4.3.1–5.4.3.5, RP9, 5.8.2.1–5.8.2.4; `AQA-8462-spec.txt` (v1.1) 4.4.3.1–4.4.3.5, RP3 (and RP4 = temperature changes), 4.8.2.1–4.8.2.4. No equation sheet applies. Route audit row `electrolysis-aqueous` (CF CH TF TH, base, OK) read. Distinct from batch 11's `electrolysis-principles` / `electrolysis-molten`: this lesson owns the aqueous rule and the electrolysis RP.

Conventions: q1–q2 quiz items; wx n = `wrong_explanations` key n; th1–th3 theory chunks. `higher` is served on CH TH; every other section on all four.

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 / 8462 | **5.4.3.4 / 4.4.3.4** | Electrolysis of aqueous solutions | base |
| 8464 RP9 / 8462 RP3 | 5.4.3.4 / 4.4.3.4 | Required practical: electrolysis of aqueous solutions | base |
| 8464 / 8462 | 5.4.3.1 / 4.4.3.1 | The process of electrolysis (HT para: half equations) | base / **HT only** para |
| 8464 / 8462 | 5.4.3.5 / 4.4.3.5 | Half equations at electrodes | **(HT only)** |
| 8464 / 8462 | 5.8.2.1, 5.8.2.2, 5.8.2.4 / 4.8.2.1, 4.8.2.2, 4.8.2.4 | Tests for hydrogen, oxygen, chlorine | base |

Spec statement (verbatim, 8464 = 8462) 5.4.3.4: "The ions discharged when an aqueous solution is electrolysed using inert electrodes depend on the relative reactivity of the elements involved. At the negative electrode (cathode), hydrogen is produced if the metal is more reactive than hydrogen. At the positive electrode (anode), oxygen is produced unless the solution contains halide ions when the halogen is produced. This happens because in the aqueous solution water molecules break down producing hydrogen ions and hydroxide ions that are discharged. Students should be able to predict the products of the electrolysis of aqueous solutions containing a single ionic compound."
RP (8464 RP9 = 8462 RP3): "investigate what happens when aqueous solutions are electrolysed using inert electrodes. This should be an investigation involving developing a hypothesis."

## 2. Route table
| # | teachable point (pack location) | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Water supplies H⁺ and OH⁻; competing ions (th1; common_mistake; key_note) | base | 5.4.3.4 | all four | OK |
| R2 | Cathode: metal below H → metal; above H → H₂ (th1; th3; common_mistake; key_note) | base | 5.4.3.4 | all four | OK |
| R3 | Anode: halide → halogen, else O₂ (th1; th3; key_note) | base | 5.4.3.4 | all four | OK in outline; "high concentration" condition off-spec (EA-F5); "halogen gas" wrong (EA-F4) |
| R4 | Worked cases: dilute H₂SO₄, CuSO₄, brine (th2) | base | 5.4.3.4 | all four | two equations WRONG (EA-F2); "cuprous" WRONG (EA-F3) |
| R5 | Brine → H₂ + Cl₂ + NaOH solution; uses (th2; th3; key_note) | base (products) / context (uses, "chlor-alkali") | 5.4.3.4 | all four | OK; industrial-source line IMPRECISE (EA-F7) |
| R6 | Half equations (equations 1–4; `higher` s1) | higher | 5.4.3.1 (HT para); 5.4.3.5 | equations: all four; `higher`: CH TH | ROUTE (EA-F6) |
| R7 | `higher` s2–s3: product selection rules; brine products | base (concentration part off-spec) | 5.4.3.4 | CH TH | ROUTE (EA-F6) / OFF-SPEC (EA-F5) |
| R8 | `rp`: gas tests; electrolysis of solutions | base, RP on all four | RP9 / RP3; 5.8.2 / 4.8.2 | all four | label WRONG (EA-F1); tests OK |
| R9 | quiz q1 (CuSO₄ cathode) | base | 5.4.3.4 | all four | OK |
| R10 | quiz q2 (brine anode) | base answer; off-spec reasoning | 5.4.3.4 | all four | OFF-SPEC (EA-F5) |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | th1 | Water partially ionises H₂O ⇌ H⁺ + OH⁻ | OK | Spec: "water molecules break down producing hydrogen ions and hydroxide ions". | 5.4.3.4 |
| C2 | th1 | "POSITION IN THE REACTIVITY SERIES — less reactive ions are discharged preferentially" | IMPRECISE | The series ranks elements, not ions: the ion of the less reactive element is discharged (EA-F8). | 5.4.3.4 |
| C3 | th1 | "CONCENTRATION — a high concentration of an ion favours its discharge"; anode "If Cl⁻ ions are present in HIGH concentration → Cl₂ … If no Cl⁻ (or low concentration) → O₂" | OFF-SPEC | AQA rule has no concentration condition: halide present → halogen (EA-F5). | 5.4.3.4 |
| C4 | th1 | Cathode rule: below H → metal; above H → H₂ | OK | — | 5.4.3.4 |
| C5 | th2 | Dilute H₂SO₄ ions H⁺, OH⁻, SO₄²⁻; H₂ at cathode, O₂ at anode, 2:1 by volume | OK | 2H₂O → 2H₂ + O₂ gives 2:1 ✓. | 5.4.3.4 |
| C6 | th2 | "Cathode: H⁺ + e⁻ → H₂" | WRONG | Not balanced. 2H⁺ + 2e⁻ → H₂ (EA-F2). | 5.4.3.5 |
| C7 | th2 | "Anode: 4OH⁻ → O₂ + 2H₂O" | WRONG | Charge not balanced (−4 → 0). 4OH⁻ → O₂ + 2H₂O + 4e⁻, or 4OH⁻ − 4e⁻ → O₂ + 2H₂O (EA-F2). | 5.4.3.5 |
| C8 | th2 | "CUPROUS SULFATE SOLUTION (CuSO₄(aq))" | WRONG | Cuprous = copper(I). CuSO₄ is copper(II) sulfate (EA-F3). | — |
| C9 | th2 | CuSO₄: Cu at cathode (Cu below H), O₂ at anode | OK | — | 5.4.3.4 |
| C10 | th2 | Brine: H₂ at cathode (Na above H), Cl₂ at anode, NaOH left in solution | OK | "(not O₂ — Cl⁻ concentration effect)" off-spec reason (EA-F5). | 5.4.3.4 |
| C11 | th3 | Cathode rule lists (Cu²⁺, Ag⁺, Au³⁺ → metal; Na⁺ … Fe²⁺ → H₂) | OK | Per AQA rule. | 5.4.3.4 |
| C12 | th3 | "If halide ions present … AND in high concentration → HALOGEN gas (Cl₂, Br₂, I₂)" | WRONG | Br₂ and I₂ are not gases here. They form in solution (orange / brown). Spec says "the halogen is produced". Also the concentration condition is off-spec (EA-F4, EA-F5). | 5.4.3.4 |
| C13 | th3 | Uses: Cl₂ (PVC, disinfectants, bleach); H₂ (Haber, fuel cells); NaOH (paper, soap, cleaning) | OK (context) | — | — |
| C14 | th3 | "OXYGEN — from water/dilute sulfuric acid" as an important industrial product | IMPRECISE | Industrial O₂ comes from fractional distillation of liquid air, not electrolysis (EA-F7). | — |
| C15 | th3 | "ALUMINIUM — from molten Al₂O₃ in cryolite" | OK | Molten, not aqueous (cross-link to electrolysis-extraction). | 5.4.3.3 |
| C16 | `higher` | half equations; "product selection rules using reactivity and concentration"; chlor-alkali products | ROUTE / OFF-SPEC | Half equations HT ✓; product rules base; concentration off-spec (EA-F5, F6). | 5.4.3.4; 5.4.3.5 |
| C17 | common_mistake | Water's H⁺/OH⁻ compete; above H → H₂; no halide → O₂; Na never deposited from aqueous solution | OK | — | 5.4.3.4 |
| C18 | key_note | "Cl⁻ in high conc → Cl₂" | OFF-SPEC | AQA: halide present → halogen (EA-F5). | 5.4.3.4 |
| C19 | equations 1–4 | 2H⁺ + 2e⁻ → H₂; 4OH⁻ → O₂ + 2H₂O + 4e⁻; 2Cl⁻ → Cl₂ + 2e⁻; Cu²⁺ + 2e⁻ → Cu | OK (HT) | All balanced. Eqs 1–2 are the spec's own examples. HT only (EA-F6). | 5.4.3.5 |
| C20 | rp | "RP4 (Chemistry)" | WRONG | Chemistry RP4 is temperature changes. This is Combined RP9 = Chemistry RP3 (EA-F1). | 8464 5.4.3.4; 8462 4.4.3.4 |
| C21 | rp | H₂ lit splint squeaky pop; O₂ glowing splint relights; Cl₂ bleaches damp litmus | OK | Spec wording: "burning splint … pop"; "splint relights"; "damp litmus paper … bleached and turns white". | 5.8.2.1, .2, .4 / 4.8.2.1, .2, .4 |
| C22 | q1 key | Cu at cathode; Cu²⁺ "below hydrogen" preferentially discharged | OK | Answer ✓. "Cu²⁺ ions are below hydrogen" loose wording (EA-F8). | 5.4.3.4 |
| C23 | q1 opt 2 / wx1 | H₂ always discharged / Cu²⁺ "LESS REACTIVE than H⁺" | OK, aligned; IMPRECISE (EA-F8) | — | — |
| C24 | q1 opt 3 / wx2 | SO₂ from SO₄²⁻ at cathode / SO₄²⁻ not discharged | OK, aligned | — | — |
| C25 | q1 opt 4 / wx3 | O₂ at cathode / O₂ is at the anode | OK, aligned | — | — |
| C26 | q2 key | Cl₂ — "high concentration of Cl⁻ … preferentially discharged over OH⁻" | OFF-SPEC (reason) | Answer ✓. AQA reason: the solution contains halide (chloride) ions, so the halogen is produced (EA-F5). | 5.4.3.4 |
| C27 | q2 opt 2 / wx1 | O₂ always at anode / "O₂ IS produced if the Cl⁻ concentration is LOW" | OFF-SPEC; aligned | wx1 teaches a prediction (dilute NaCl → O₂) that contradicts the AQA rule and would lose the mark (EA-F5). | 5.4.3.4 |
| C28 | q2 opt 3 / wx2 | Na at anode / Na⁺ goes to cathode | OK, aligned | — | 5.4.3.1 |
| C29 | q2 opt 4 / wx3 | H₂ at anode / H⁺ discharged at cathode | OK, aligned | — | 5.4.3.1 |
| C30 | matching (to be replaced) | "Dilute NaCl → O₂ at anode" | OFF-SPEC | Contradicts AQA rule (EA-F5). | 5.4.3.4 |

Count: **5 WRONG rows** (C6, C7, C8, C12, C20) → **4 WRONG flags** (EA-F1–F4); **OFF-SPEC**: concentration rule throughout (EA-F5); **IMPRECISE**: C2, C14, C22–23.

## 4. Frozen items for their route
| item | usable on | note |
|---|---|---|
| q1 | CF CH TF TH | Base. |
| q2 | none as written | Correct answer, but the key's reason and wx1 rest on a concentration rule AQA does not use, and wx1 contradicts the AQA rule (EA-F5). |

## 5. Verdict
SOURCE HAS ERRORS. The two prediction rules and the three worked cases' products are right. Wrong: the RP number, two unbalanced half equations, "cuprous", and "halogen gas" for Br₂/I₂. The concentration condition that runs through the file is not the AQA rule. One quiz item is usable. No item is Mide's call: the RP is Combined RP9 = Chemistry RP3, settled from both specs.
