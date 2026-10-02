# Examination — Fuel Cells (fuel-cells) — AQA 8462 4.5.2.2 (chemistry only; half equations HT only)
Verdict: SOURCE OK WITH FLAGS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-12/04-checked-science-source/chemistry-4.5.2.2-fuel-cells.md`.
Spec sources read as text: `AQA-8462-spec.txt` 4.5.2.1, 4.5.2.2, 4.4.1.2 (oxidation/reduction by electrons, HT); `AQA-8464-spec.txt` 5.5 (no 5.5.2 — not in Combined). No equation sheet applies. Route audit read: `chemistry.md` row `fuel-cells` (OK, chem-only, TF TH; HT layer: electrode half equations).

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n; th1–th3 = theory chunks. TH copy carries a `higher` field; TF copy's `higher` is null.

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8462 | **4.5.2.2** | Fuel cells | 4.5.2 "(chemistry only)"; half-equation bullet "(HT only)" |
| 8464 | — | not in Combined Science | — |
| Supporting | 8462 4.5.2.1 cells and batteries (the comparison) | | triple |

Spec statement (verbatim): "Fuel cells are supplied by an external source of fuel (eg hydrogen) and oxygen or air. The fuel is oxidised electrochemically within the fuel cell to produce a potential difference. The overall reaction in a hydrogen fuel cell involves the oxidation of hydrogen to produce water. Hydrogen fuel cells offer a potential alternative to rechargeable cells and batteries. Students should be able to: • evaluate the use of hydrogen fuel cells in comparison with rechargeable cells and batteries • (HT only) write the half equations for the electrode reactions in the hydrogen fuel cell."

## 2. Route table
| # | teachable point | true layer | spec | verdict |
|---|---|---|---|---|
| R1 | Fuel cell supplied continuously with fuel and oxygen/air; fuel oxidised electrochemically → p.d. (th1; common_mistake) | triple | 4.5.2.2 | OK |
| R2 | Overall: hydrogen oxidised to water; 2H₂ + O₂ → 2H₂O (th1; equation; key_note; q1) | triple | 4.5.2.2 | OK (key_note unbalanced, C12) |
| R3 | H₂ oxidised at negative electrode, O₂ reduced at positive (th1) | triple (context for the HT half equations) | 4.5.2.2 | OK |
| R4 | Evaluate fuel cells vs rechargeable batteries (th2–th3; q2; `higher` second sentence) | triple — **not HT** | 4.5.2.2 bullet 1 | OK; ROUTE: the `higher` copy carries it TH-only (th3 carries it on both) |
| R5 | Half equations H₂ → 2H⁺ + 2e⁻; O₂ + 4H⁺ + 4e⁻ → 2H₂O (`higher`) | **triple-higher** | 4.5.2.2 bullet 2 (HT only) | OK |
| R6 | Steam reforming, green hydrogen, platinum, FCEV models, Apollo (th2–th3) | off-spec context (supports evaluation) | — | OK |
| R7 | q1, q2 | triple | 4.5.2.2 | OK |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | th1 | fuel cell converts chemical energy of fuel to electrical energy while fuel and O₂ supplied | OK | ✓ | 4.5.2.2 |
| C2 | th1 | fuel H₂; oxidant O₂ from air; only product water | OK | ✓ | 4.5.2.2 |
| C3 | th1 | H₂ + ½O₂ → H₂O; 2H₂ + O₂ → 2H₂O | OK | ✓ balanced | 4.5.2.2 |
| C4 | th1 | H₂ oxidised at negative electrode (anode); O₂ reduced at positive (cathode); electrons through external circuit | OK | ✓ (in a fuel cell the anode is negative — opposite of electrolysis; say "negative/positive electrode" to avoid confusion). | 4.5.2.2 |
| C5 | th1 | battery stores fixed reactants; fuel cell supplied continuously | OK | ✓ | 4.5.2.1; 4.5.2.2 |
| C6 | th2 | only product water; no CO₂/NOₓ/particulates in operation | OK | ✓ | 4.5.2.2 |
| C7 | th2 | more efficient than combustion engines; no moving parts in the cell | OK | ✓ (typical 40–60 % vs ~25–35 %). | — |
| C8 | th2 | fast refuelling; long range; high energy per kg; continuous operation | OK | ✓ (per kg high, per volume low — th3's storage point covers it). | — |
| C9 | th2 | Toyota Mirai, Hyundai Nexo; buses/HGVs; Apollo, water drunk by crew | OK | ✓ context | — |
| C10 | th3 | most H₂ from natural gas by steam reforming (CO₂ released); green H₂ by electrolysis | OK | ✓ | — |
| C11 | th3 | flammable; stored under pressure or liquid; few stations; platinum catalyst expensive; FCEVs dearer; battery EVs established grid; both zero direct emission | OK | ✓ — these are the standard AQA evaluation points. Add the battery side AQA credits: batteries hold toxic chemicals for disposal and degrade over recharge cycles (th3 of `cells-and-batteries` has this). | 4.5.2.2 |
| C12 | key_note | "Hydrogen fuel cell: H₂ + O₂ → H₂O." | IMPRECISE | Unbalanced as a symbol equation. Use 2H₂ + O₂ → 2H₂O (the frozen `equations` entry). | 4.5.2.2 |
| C13 | `higher` | anode "H₂ − 2e⁻ → 2H⁺"; cathode "O₂ + 4H⁺ + 4e⁻ → 2H₂O" | OK | Both balanced for charge and atoms (acidic electrolyte). AQA mark schemes credit H₂ → 2H⁺ + 2e⁻ and accept the "− 2e⁻" form; teach the "+ 2e⁻ on the right" form first. Combined, ×2 anode + cathode = 2H₂ + O₂ → 2H₂O ✓. | 4.5.2.2 (HT only); 4.4.3.5 (HT only) |
| C14 | `higher` | "Evaluate hydrogen fuel cells vs rechargeable batteries… using data" | ROUTE | Base triple (bullet 1 has no HT label); on TF too. th3 already gives TF the comparison, so the loss is small. | 4.5.2.2 |
| C15 | common_mistake | fuel cell ≠ battery; only product water; no CO₂ in operation | OK | ✓ | 4.5.2.2 |
| C16 | equations | 2H₂ + O₂ → 2H₂O | OK | ✓ | 4.5.2.2 |
| C17 | q1 key | water; H₂ oxidised, O₂ reduced | OK | ✓ | 4.5.2.2 |
| C18 | q1 opt1–3 / wx1–3 | CO₂ / H₂O₂ / O₂ released | OK | All aligned ✓ | — |
| C19 | q2 key | most H₂ from natural gas → CO₂ at production, not in operation | OK | ✓; an evaluation point within 4.5.2.2 bullet 1. | 4.5.2.2 |
| C20 | q2 opt1–3 / wx1–3 | cell makes CO₂ / platinum a carbon compound / start-up electricity | OK | All aligned ✓ | — |
| C21 | matching (to be replaced) | five advantage/disadvantage sorts | OK | ✓ | — |

Count: **0 WRONG**. IMPRECISE: C12. ROUTE: C14. No calculations; no CFIFA in this file.

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| q1 | correct | Usable on TF TH. |
| q2 | correct | Usable on TF TH. |
| equation | correct | Keep. |

## 5. Calculations
None. Half-equation writing (HT) is balancing atoms and charge, not a calculation.

## 6. Verdict
SOURCE OK WITH FLAGS. Science sound throughout; both quiz items correct and usable on both routes; half equations correct. key_note's symbol equation is unbalanced; the fuel-cell-vs-battery evaluation is base triple but the `higher` field puts it TH-only (theory still carries it on TF). The HT half equations are the page's only triple-higher layer. Nothing for Mide.
