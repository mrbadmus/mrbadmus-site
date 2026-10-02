# Examination — Catalysts (catalysts) — AQA 8464 5.6.1.4 / 8462 4.6.1.4
Verdict: SOURCE OK WITH FLAGS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-12/04-checked-science-source/chemistry-5.6.1.4-catalysts.md`.
Spec sources read as text: `AQA-8464-spec.txt` (v1.1) 5.6.1.3, 5.6.1.4, 5.5.1.2, whole-file search for every catalyst name; `AQA-8462-spec.txt` (v1.1) 4.6.1.4, 4.1.3.2 (chemistry only), 4.10.4.1 (chemistry only), the same whole-file search; `AQA-8461-spec.txt` 4.2.2.1 (enzymes, for the denaturation claim). No equation sheet applies. Route audit read: `ks4-routes/docs/ks4/route-audit/chemistry.md` row `catalysts` (CF CH TF TH, base, OK).

Conventions: q1–q2 quiz items; wx n = `wrong_explanations` key n (option 0 is the key on both items); th1–th3 theory chunks. Every route copy of `higher` is `null`; the TH `higher` text is served on CH and TH.

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 / 8462 | **5.6.1.4 / 4.6.1.4** | Catalysts | base |
| 8462 | 4.10.4.1 | The Haber process (iron catalyst) | **(chemistry only)** |
| 8462 | 4.1.3.2 | Typical properties of transition metals ("useful as catalysts") | **(chemistry only)** |
| 8464 / 8462 | 5.5.1.2 / 4.5.1.2 | Reaction profiles (prerequisite) | base |

Spec statements (verbatim, 8464 = 8462): "Catalysts change the rate of chemical reactions but are not used up during the reaction. Different reactions need different catalysts. Enzymes act as catalysts in biological systems. Catalysts increase the rate of reaction by providing a different pathway for the reaction that has a lower activation energy. A reaction profile for a catalysed reaction can be drawn in the following form: [profile figure]. Students should be able to identify catalysts in reactions from their effect on the rate of reaction and because they are not included in the chemical equation for the reaction. Students should be able to explain catalytic action in terms of activation energy. Students do not need to know the names of catalysts other than those specified in the subject content." AT 5: "An opportunity to investigate the catalytic effect of adding different metal salts to a reaction such as the decomposition of hydrogen peroxide."
8462 4.10.4.1 (chemistry only): "The purified gases are passed over a catalyst of iron at a high temperature (about 450°C) and a high pressure (about 200 atmospheres)." 8462 4.1.3.2 (chemistry only): "Many transition elements have ions with different charges, form coloured compounds and are useful as catalysts."
A search of the full 8464 and 8462 texts finds **no** mention of vanadium(V) oxide, the Contact process, platinum, rhodium, catalytic converters or nickel hydrogenation.

## 2. Route table
| # | teachable point (pack location) | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Catalyst changes (increases) rate, not used up (th1; common_mistake; key_note; q1) | base | 5.6.1.4 | all four | OK |
| R2 | Different pathway with lower Ea; greater proportion of collisions ≥ Ea (th1; q1; q2) | base | 5.6.1.4 | all four | OK |
| R3 | ΔH and products unchanged (th1; common_mistake; q1) | base | 5.6.1.4 (profile); 5.5.1.2 | all four | OK |
| R4 | Specific: different reactions need different catalysts (th1) | base | 5.6.1.4 | all four | OK |
| R5 | Small quantities (th1) | base (context) | — | all four | OK |
| R6 | Heterogeneous / homogeneous; Fe²⁺ with H₂O₂ (th2) | not in spec (A-level) | — | all four | OFF-SPEC (CATALYSTS-F1) |
| R7 | Enzymes as biological catalysts (th2; key_note) | base | 5.6.1.4 | all four | OK; "denature above ~40 °C" imprecise (F3) |
| R8 | Iron in the Haber process (th2; th3; key_note) | **triple** | 8462 4.10.4.1 (chemistry only) | all four | ROUTE (F2) |
| R9 | V₂O₅/Contact, Pt/Rh converters, Ni hydrogenation (th2; th3; key_note) | not in spec | — | all four | OFF-SPEC (F2) |
| R10 | Economic and environmental benefits; lower temperature (th3; q2) | base (application of 5.6.1.4) | 5.6.1.4 | all four | OK |
| R11 | Catalyst poisoning (th3; `higher`) | not in spec | — | all four / CH TH | OFF-SPEC (F4) |
| R12 | `higher`: adsorb/desorb; poisoning; enzymes | no HT content in 5.6.1.4; enzymes = base | 5.6.1.4 | CH TH | ROUTE / OFF-SPEC (F4) |
| R13 | Catalysed reaction profile; identify a catalyst because it is not in the equation | base | 5.6.1.4 | **profile in words only; identify rule absent** | GAP (F5) |
| R14 | quiz q1, q2 | base | 5.6.1.4 | all four | OK |
| — | RP, equations, FIFA | none | — | — | correct. Metal salts + H₂O₂ is an AT 5 opportunity, not an RP |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | th1 | catalyst increases rate without being used up or permanently changed | OK | Spec: "change the rate … not used up". | 5.6.1.4 |
| C2 | th1 | lower-Ea pathway; same at end as start; small quantities; specific | OK | — | 5.6.1.4 |
| C3 | th1 | alternative pathway → greater proportion of collisions ≥ the lower Ea → faster | OK | The spec's "explain catalytic action in terms of activation energy". | 5.6.1.4 |
| C4 | th1 | ΔH not affected — same reactants and products | OK | — | 5.6.1.4 profile |
| C5 | th2 | heterogeneous/homogeneous definitions; reaction on the surface | OFF-SPEC (true) | A-level. | F1 |
| C6 | th2 | iron, Haber, N₂ + 3H₂ ⇌ 2NH₃ | OK — triple layer | Iron is named only in 8462 4.10.4.1 (chemistry only). | F2 |
| C7 | th2 | Pt/Rh converters convert CO, NO, hydrocarbons → CO₂, N₂, H₂O | OFF-SPEC (true) | Not in either spec. | F2 |
| C8 | th2 | nickel in margarine (hydrogenation of vegetable oils) | OFF-SPEC (true) | Not in the current spec (it was in the pre-2016 specification). | F2 |
| C9 | th2 | Fe²⁺ ions catalyse H₂O₂ decomposition | OFF-SPEC (true) | Context; the spec's AT 5 suggests metal salts with H₂O₂. | F1 |
| C10 | th2 | enzymes are proteins; amylase (starch), catalase (H₂O₂); specific | OK | Biology context. | 8461 4.2.2.1 |
| C11 | th2; `higher` | enzymes "denature above ~40°C" | IMPRECISE | Optimum temperatures vary (human enzymes ~37 °C); denaturation increases at high temperatures and there is no single cut-off. | F3 |
| C12 | th3 | Haber without catalyst too slow; with iron fast enough at ~450 °C | OK — triple layer | 8462 4.10.4.1: "about 450°C". | F2 |
| C13 | th3 | Contact process: 2SO₂ + O₂ ⇌ 2SO₃, V₂O₅ | OFF-SPEC (true) | Not in the 2016 spec. Equation balanced ✓. | F2 |
| C14 | th3 | benefits: lower temperature → less energy → lower cost; fewer by-products; smaller reactors; reusable | OK (context) | — | 5.6.1.4 |
| C15 | th3 | catalysts can be poisoned — impurities block active sites | OFF-SPEC (true) | — | F4 |
| C16 | `higher` | adsorb → bonds weaken → lower Ea → desorb; poisoning "permanently" | OFF-SPEC; IMPRECISE | A-level. Some poisoning is reversible. No HT content exists for this clause. | F4 |
| C17 | common_mistake | not used up; does not change products or ΔH; lower-Ea pathway | OK | — | 5.6.1.4 |
| C18 | key_note | definition; heterogeneous; enzymes; iron, platinum, V₂O₅; lower temperature | OK except names (F2) and "heterogeneous" (F1) | — | 5.6.1.4 |
| C19 | q1 key (opt 0) | rate up, Ea lowered, products and ΔH unchanged | OK | — | 5.6.1.4 |
| C20 | q1 opt 1 / wx1 | products change / same products, alternative pathway | OK | Aligned. | — |
| C21 | q1 opt 2 / wx2 | ΔH decreases / ΔH unchanged because reactants and products unchanged | OK | Aligned. | — |
| C22 | q1 opt 3 / wx3 | used up / not consumed, regenerated; a used-up substance is a reactant | OK | Aligned. | 5.6.1.4 |
| C23 | q2 key (opt 0) | lower Ea → enough particles have sufficient energy at lower temperature | OK | — | 5.6.1.4 |
| C24 | q2 opt 1 / wx1 | catalysts generate heat / "If they released heat, they would be acting as reactants." | OK (minor) | Aligned. The second sentence is loose reasoning but not false. | — |
| C25 | q2 opt 2 / wx2 | better quality products / reason is kinetic | OK | Aligned. | — |
| C26 | q2 opt 3 / wx3 | catalysts compress gases / they don't affect pressure | OK | Aligned. | — |
| C27 | matching (to be replaced) | iron–Haber; V₂O₅–Contact; Pt/Rh–converter; Ni–hydrogenation; amylase | OK as facts; 3 of 5 off-spec | Replace anyway; do not rebuild it on off-spec names. | F2 |

Count: **0 WRONG**. IMPRECISE: C11, C16. OFF-SPEC: heterogeneous/homogeneous, four catalyst names, poisoning, adsorption. One ROUTE: iron/Haber is a triple fact. Both frozen quiz items are correct.

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| none | q1 and q2 are both correct, aligned and base | Usable verbatim on all four routes. |

## 5. Verdict
SOURCE OK WITH FLAGS. The core (lower-Ea pathway, not used up, ΔH unchanged, enzymes) is right and both quiz items are clean. The source loads the page with A-level classification and catalyst names the spec says pupils need not know. Iron/Haber is a Triple fact. The spec's catalysed reaction profile and its "not in the equation" identification rule need drawing and teaching. Nothing is Mide's call.
