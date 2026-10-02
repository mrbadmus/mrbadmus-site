# Examination — Mass Changes in Reactions (mass-changes-reactions) — AQA 8464 5.3.1.3 / 8462 4.3.1.3
Verdict: SOURCE HAS ERRORS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-11/04-checked-science-source/chemistry-5.3.1.3-mass-changes-reactions.md`.
Spec sources read as text: `AQA-8462-spec.txt` 4.3.1.1–4.3.2.2, 4.10.3.1; `AQA-8464-spec.txt` 5.3.1.1–5.3.2.2 (identical wording to 8462 4.3.1–4.3.2). No equation sheet applies (chemistry). Route audit read: `ks4-routes/docs/ks4/route-audit/chemistry.md` row `mass-changes-reactions` (OK, base, CF CH TF TH).

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n; th1–th3 = theory chunks. All four route copies identical; no `higher` field.

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 | **5.3.1.3** | Mass changes when a reactant or product is a gas | base |
| 8462 | **4.3.1.3** | Mass changes when a reactant or product is a gas | base |
| Supporting | 8464 5.3.1.1 / 8462 4.3.1.1 conservation of mass; 5.3.1.2 / 4.3.1.2 relative formula mass | | base |
| Supporting (calculation) | 8464 5.3.2.1–5.3.2.2 / 8462 4.3.2.1–4.3.2.2 moles; masses from balanced equations | | **(HT only)** |
| Context (q2) | 8462 4.10.3.1 corrosion — "Both air and water are necessary for iron to rust." | | (chemistry only) |

Spec statement (verbatim, 8464 = 8462): "Some reactions may appear to involve a change in mass but this can usually be explained because a reactant or product is a gas and its mass has not been taken into account. For example: when a metal reacts with oxygen the mass of the oxide produced is greater than the mass of the metal or in thermal decompositions of metal carbonates carbon dioxide is produced and escapes into the atmosphere leaving the metal oxide as the only solid product. Students should be able to explain any observed changes in mass in non-enclosed systems during a chemical reaction given the balanced symbol equation for the reaction and explain these changes in terms of the particle model."

8464 5.3.2.2 / 8462 4.3.2.2 (HT only): "The masses of reactants and products can be calculated from balanced symbol equations … calculate the masses of reactants and products from the balanced symbol equation and the mass of a given reactant or product."

## 2. Route table
| # | teachable point | true layer | spec | verdict |
|---|---|---|---|---|
| R1 | Apparent mass change is a gas entering/leaving, not a breach of conservation (th1; key_note) | base | 5.3.1.3; 5.3.1.1 | OK |
| R2 | Gas produced escapes → measured mass falls; CaCO₃ + 2HCl (th1) | base | 5.3.1.3 | OK |
| R3 | Mg ribbon example under "mass appears to decrease" (th1) | — | 5.3.1.3 | **WRONG** (C3) |
| R4 | Metal + oxygen from air → oxide heavier (th1; common_mistake; key_note) | base | 5.3.1.3 | OK |
| R5 | Predicting the mass change by moles (th2) | **higher** | 5.3.2.1, 5.3.2.2 (HT only) | OK science; route flag |
| R6 | Open vs closed systems; precipitation; decomposition; hydrocarbons (th3) | base | 5.3.1.3 | OK |
| R7 | FIFA — mass of MgO from 4.8 g Mg | **higher** | 5.3.2.2 (HT only) | OK; route flag |
| R8 | q1 — CaCO₃ heated in open crucible | base | 5.3.1.3 (spec's own example) | OK |
| R9 | q2 — iron rusting gains mass | base (rust context is 8462 4.10.3.1, chemistry only; the reasoning asked is base) | 5.3.1.3 | OK; wx1 IMPRECISE |
| — | rp, `higher`, equations | none | — | correct: no RP; nothing labelled HT in the data although R5/R7 are HT |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | th1 | measured mass changes because a gas enters or leaves; conservation not violated | OK | — | 5.3.1.3 |
| C2 | th1 | CaCO₃(s) + 2HCl(aq) → CaCl₂(aq) + H₂O(l) + CO₂(g); CO₂ escapes, mass falls | OK | Balanced ✓, state symbols ✓ | 5.3.1.3 |
| C3 | th1 | "Mg ribbon burning — ash (MgO) seems lighter than the ribbon, but this is because oxygen from AIR was added. Without accounting for the oxygen, mass appears lost." (listed under DECREASE) | **WRONG** | Self-contradictory, and contradicts th1's own INCREASE section. The oxide is heavier than the metal (spec's own example). If a real crucible reading falls, it is MgO smoke escaping when the lid is lifted — a loss of product, not of oxygen. Delete from the decrease list. | 5.3.1.3 |
| C4 | th1 | 2Mg(s) + O₂(g) → 2MgO(s); oxygen joins the solid, mass up | OK | — | 5.3.1.3 |
| C5 | th2 | 4.8 ÷ 24 = 0.2 mol Mg; 0.1 mol O₂; 0.1 × 32 = 3.2 g; 4.8 + 3.2 = 8.0 g; 0.2 × 40 = 8.0 g ✓ | OK (HT) | All arithmetic ✓. Moles = HT only. | 5.3.2.1–5.3.2.2 |
| C6 | th3 | precipitation in closed container: no mass change | OK | — | 5.3.1.1 |
| C7 | th3 | metal heated in a sealed container with air: mass constant | OK | — | 5.3.1.3 |
| C8 | th3 | CaCO₃ → CaO + CO₂: open falls, closed constant | OK | Balanced ✓ | 5.3.1.3 |
| C9 | th3 | burning hydrocarbon in open container: CO₂ and H₂O escape → mass falls | OK | (Oxygen is also taken in, but the products leave; the fuel's mass reading falls.) | 5.3.1.3 |
| C10 | th1–th3 | particle-model explanation | GAP (minor) | Spec asks to "explain these changes in terms of the particle model"; th1 only says "gas molecules leave the container". Needs: gas particles move freely and spread out of an open vessel; oxygen particles from the air bond to metal atoms and become part of the solid. | 5.3.1.3 |
| C11 | common_mistake | metal burning in air gains mass; oxygen added | OK | — | 5.3.1.3 |
| C12 | key_note | as R1, R2, R4; "Closed container: mass always stays the same" | OK | — | 5.3.1.1, 5.3.1.3 |
| C13 | FIFA F | "2 × Mr(Mg) : 2 × Mr(MgO) = 48 : 80" | OK (IMPRECISE wording) | Ratio ✓ (2 × 24 : 2 × 40). Mg is an element: Ar(Mg), not Mr. Frozen — stays. | 5.3.1.2 |
| C14 | FIFA I/F/A | scale factor 4.8 ÷ 48 = 0.1; 80 × 0.1 = 8.0 g; increase 3.2 g | OK | ✓. Chains three operations (ratio → scale factor → mass). HT. | 5.3.2.2 |
| C15 | Convert (NEW) | "Nothing to convert — the mass of magnesium is already in grams, matching the g basis of the Mr ratio." | OK | Examined ✓ (the 48 : 80 ratio is read in grams). | CFIFA amendment |
| C16 | q1 key | open crucible: mass decreases, CO₂ escapes | OK | Spec's own example | 5.3.1.3 |
| C17 | q1 opt1 / wx1 | "increases — oxygen absorbed" / decomposition, not combustion | OK | Aligned ✓ | — |
| C18 | q1 opt2 / wx2 | "stays the same — conservation" / open system loses CO₂; total conserved | OK | Aligned ✓ | 5.3.1.1 |
| C19 | q1 opt3 / wx3 | "first increases, then decreases" / no increase phase | OK | Aligned ✓ | — |
| C20 | q2 key | oxygen combines with iron; adds to the solid's mass | OK | Creditable at base (metal + oxygen → heavier oxide). | 5.3.1.3 |
| C21 | q2 opt1 / wx1 | "Humidity can contribute, but the primary reason is oxygen… 4Fe + 3O₂ → 2Fe₂O₃" | IMPRECISE | Aligned ✓. Rust is hydrated iron(III) oxide; water is required and its mass is gained too (8462 4.10.3.1). The equation given is for anhydrous iron(III) oxide. Not wrong enough to bar the item: the key is right and wx1 does say humidity contributes. | 4.10.3.1 |
| C22 | q2 opt2 / wx2 | density / mass = density × volume | OK | Aligned ✓ | — |
| C23 | q2 opt3 / wx3 | atoms per formula unit irrelevant; mass of oxygen absorbed | OK | Aligned ✓ | — |
| C24 | matching (to be replaced) | Zn + H₂SO₄ open tube → H₂ escapes → decrease; CaCO₃ sealed tube → same | OK | All five ✓ | — |

Count: **1 WRONG** (C3, theory — re-cuttable). IMPRECISE: C13, C21. GAP: C10. ROUTE: R5, R7 (HT calculation on a base page, unbadged). 5 calculations rechecked, all ✓.

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| FIFA | Reacting-mass calculation = 5.3.2.2 (HT only) | Show on CH TH only, HT-badged. Foundation needs a base calculation instead: mass of gas = mass before − mass after (5.3.1.1), and the 4.3.1.2 check 2 × 24 + 32 = 2 × 40. |
| q1, q2 | base | Usable on all four routes. |

## 5. Calculations and chains (rule 3)
- **Base:** mass of gas lost/gained = mass before − mass after. One step; no chain.
- **HT, chain A (th2):** Step 1 n(Mg) = 4.8 ÷ 24 = 0.2 mol → Step 2 ratio 2 : 1 → n(O₂) = 0.1 mol → Step 3 m(O₂) = 0.1 × 32 = 3.2 g (mass gained).
- **HT, chain B (FIFA):** Step 1 masses from the equation 48 g : 80 g → Step 2 scale factor 4.8 ÷ 48 = 0.1 → Step 3 80 × 0.1 = 8.0 g.
- Two different methods for one answer. amounts-in-equations teaches the mole method (chain A); Design should teach one method here and show the other only as a check.

## 6. Verdict
SOURCE HAS ERRORS — one wrong theory example (C3, re-cuttable); all quiz items and the FIFA correct. The reacting-mass calculation is HT and must be badged; Foundation needs a subtraction calculation. No conflict between AQA sources; nothing for Mide.
