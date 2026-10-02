# Examination — Reversible Reactions and Equilibrium (reversible-reactions-equilibrium) — AQA 8464 5.6.2.1–5.6.2.3 / 8462 4.6.2.1–4.6.2.3
Verdict: SOURCE OK WITH FLAGS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-12/04-checked-science-source/chemistry-5.6.2.1-reversible-reactions-equilibrium.md`.
Spec sources read as text: `AQA-8464-spec.txt` (v1.1) 5.6.2.1–5.6.2.7; `AQA-8462-spec.txt` (v1.1) 4.6.2.1–4.6.2.7, 4.10.4.1. The two worked spec examples in 4.6.2.1 and 4.6.2.2 are printed as images and are blank in the text extraction. They are the AQA specification's ammonium chloride and hydrated copper sulfate examples, matched here to the source's two equations. No equation sheet applies. Route audit read: `ks4-routes/docs/ks4/route-audit/chemistry.md` row `reversible-reactions-equilibrium` (CF CH TF TH, base, OK; "`higher` field (Le Chatelier) duplicates the HT page").

Conventions: q1–q2 quiz items; wx n = `wrong_explanations` key n (option 0 is the key on both items); th1–th3 theory chunks. Every route copy of `higher` is `null`; the TH `higher` text is served on CH and TH.

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 / 8462 | **5.6.2.1 / 4.6.2.1** | Reversible reactions | base |
| 8464 / 8462 | **5.6.2.2 / 4.6.2.2** | Energy changes and reversible reactions | base |
| 8464 / 8462 | **5.6.2.3 / 4.6.2.3** | Equilibrium | base |
| 8464 / 8462 | 5.6.2.4–5.6.2.7 / 4.6.2.4–4.6.2.7 | Effect of changing conditions (forward link; page `effect-of-conditions-equilibrium`) | **(HT only)** |

Spec statements (verbatim, 8464 = 8462): 5.6.2.1 "In some chemical reactions, the products of the reaction can react to produce the original reactants. Such reactions are called reversible reactions and are represented: A + B ⇌ C + D. The direction of reversible reactions can be changed by changing the conditions. For example: [ammonium chloride ⇌ ammonia + hydrogen chloride, heat / cool]." 5.6.2.2 "If a reversible reaction is exothermic in one direction, it is endothermic in the opposite direction. The same amount of energy is transferred in each case. For example: [hydrated copper sulfate (blue) ⇌ anhydrous copper sulfate (white) + water; endothermic forward, exothermic reverse]." 5.6.2.3 "When a reversible reaction occurs in apparatus which prevents the escape of reactants and products, equilibrium is reached when the forward and reverse reactions occur at exactly the same rate." WS 1.2.

## 2. Route table
| # | teachable point (pack location) | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Reversible reaction definition; ⇌ (th1; key_note) | base | 5.6.2.1 | all four | OK |
| R2 | NH₄Cl ⇌ NH₃ + HCl, heat/cool (th1; equations) | base | 5.6.2.1 | all four | OK |
| R3 | CuSO₄·5H₂O ⇌ CuSO₄ + 5H₂O; blue/white; test for water (th1; equations) | base | 5.6.2.1–5.6.2.2 | all four | OK |
| R4 | Direction depends on conditions (th1) | base | 5.6.2.1 | all four | OK |
| R5 | Closed system → equilibrium; rates equal; reaction continues; concentrations constant, not equal (th2; common_mistake; key_note; q1) | base | 5.6.2.3 | all four | OK |
| R6 | "If products are removed, the reaction shifts to produce more products" (th2) | **higher** | 5.6.2.5 (HT only) | all four | ROUTE (REVERSIBLE-REACTIONS-EQUILIBRIUM-F1) |
| R7 | Open systems cannot reach equilibrium — "burning fuel in open air" (th2) | base | 5.6.2.3 | all four | IMPRECISE example (F2) |
| R8 | Exo one way, endo the other, same amount (th3; key_note; q2) | base | 5.6.2.2 | all four | OK |
| R9 | Haber forward exothermic as an example (th3) | base (as a given example) | 5.6.2.2 | all four | OK |
| R10 | `higher`: qualitative Le Chatelier; catalyst doesn't change position | **higher** | 5.6.2.4–5.6.2.7 (HT only) | CH TH | OK as HT. It duplicates `effect-of-conditions-equilibrium` (F4) |
| R11 | quiz q1, q2 | base | 5.6.2.2; 5.6.2.3 | all four | OK |
| — | RP, FIFA, calculations | none | — | — | correct |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | th1 | products can react to form the original reactants; ⇌ | OK | Spec definition. | 5.6.2.1 |
| C2 | th1; equations | NH₄Cl(s) ⇌ NH₃(g) + HCl(g); heat forward, cool reverse | OK | Balanced ✓; state symbols ✓. The spec's own example. | 5.6.2.1 |
| C3 | th1; equations | CuSO₄·5H₂O(s) ⇌ CuSO₄(s) + 5H₂O(l); blue → white on heating; water → blue | OK | Balanced ✓. Water leaves as steam on heating; (l) is acceptable for the equation as written. The spec's own example. | 5.6.2.2 |
| C4 | th1 | white anhydrous copper sulfate turns blue with water — test for water | OK (context) | A test for the presence of water, not its purity. | — |
| C5 | th1 | direction depends on conditions (temperature, pressure, concentration) | OK | — | 5.6.2.1 |
| C6 | th2 | closed system (nothing enters or leaves) → equilibrium | OK | Spec: "apparatus which prevents the escape of reactants and products". | 5.6.2.3 |
| C7 | th2 | at equilibrium, forward and reverse continue at equal rates; concentrations constant, not necessarily equal | OK | — | 5.6.2.3 |
| C8 | th2 | "'equilibrium' because the concentrations are balanced (not changing)" | IMPRECISE | "Balanced" invites "equal". The balance is in the **rates**; the concentrations are constant. | F3 |
| C9 | th2 | "If products are removed, the reaction shifts to produce more products … If reactants are removed, the reaction shifts to produce more reactants." | ROUTE; IMPRECISE | This is Le Chatelier (HT only), placed in base theory under a "closed system requirement" heading it does not belong to. Removing a substance means the system is no longer closed. | F1 |
| C10 | th2 | "Open systems (like burning fuel in open air) cannot reach equilibrium — products escape" | IMPRECISE | Combustion is not a reversible reaction, so it cannot illustrate this. Use a reversible reaction in an open container, e.g. heating calcium carbonate: the CO₂ escapes, so equilibrium is never reached. | F2 |
| C11 | th3 | forward exothermic ⇒ reverse endothermic; same amount of energy | OK | Spec sentence. | 5.6.2.2 |
| C12 | th3 | dehydration of hydrated CuSO₄ endothermic; rehydration exothermic ("hand gets warm") | OK | Matches the spec example. | 5.6.2.2 |
| C13 | th3 | N₂ + 3H₂ → 2NH₃ exothermic; reverse endothermic; same value, opposite signs | OK | Balanced ✓. | 5.6.2.2 |
| C14 | `higher` | concentration increase → shift to use up the added species; temperature increase → endothermic direction; pressure increase → fewer moles of gas; catalyst doesn't change position | OK (HT) | All correct. The spec says "smaller number of molecules"; "moles of gas" is accepted. | 5.6.2.4–5.6.2.7 |
| C15 | common_mistake | not stopped; equal rates; constant not equal; "equal concentrations" is wrong | OK | — | 5.6.2.3 |
| C16 | key_note | as above | OK | — | 5.6.2.1–5.6.2.3 |
| C17 | q1 key (opt 0) | both reactions continue at equal rates; concentrations constant | OK | — | 5.6.2.3 |
| C18 | q1 opt 1 / wx1 | reaction stopped / dynamic — both continue | OK | Aligned. | — |
| C19 | q1 opt 2 / wx2 | concentrations equal / constant, not equal | OK | Aligned. | — |
| C20 | q1 opt 3 / wx3 | only forward occurs / both directions at equal rates | OK | Aligned. | — |
| C21 | q2 key (opt 0) | forward releases 50 kJ/mol → reverse absorbs 50 kJ/mol | OK | — | 5.6.2.2 |
| C22 | q2 opt 1 / wx1 | reverse also releases 50 / would create energy from nothing | OK | Aligned. | — |
| C23 | q2 opt 2 / wx2 | absorbs 100 / same magnitude, reversed direction | OK | Aligned. | — |
| C24 | q2 opt 3 / wx3 | zero / always equal and opposite | OK | Aligned. | — |
| C25 | matching (to be replaced) | five pairs | OK | Prints its own answers; replace. | — |

Count: **0 WRONG**. One ROUTE (HT content in base theory, F1). IMPRECISE: C8, C10. Both frozen quiz items are correct and aligned.

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| none | q1 and q2 are both correct and base | Usable verbatim on all four routes. |

## 5. Verdict
SOURCE OK WITH FLAGS. The base science (⇌, the spec's two examples, equal and opposite energy changes, dynamic equilibrium in a closed system) is right, and both quiz items are clean. Theory 2 slips HT Le Chatelier into base text and uses combustion as an "open system" example. The `higher` field is correct HT content but is the next page's lesson. Nothing is Mide's call.
