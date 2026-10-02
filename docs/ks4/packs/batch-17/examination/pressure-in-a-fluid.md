# Examination — Pressure in a Fluid (pressure-in-a-fluid) — AQA 8463 4.5.5.1.1, 4.5.5.2 (physics only); HT layer 4.5.5.1.2 (physics only, HT only); not in 8464
Verdict: SOURCE OK WITH FLAGS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-17/04-checked-science-source/physics-6.5.5-pressure-in-a-fluid.md`.
Spec sources read as text: `AQA-8463-spec.txt` (v1.1, 30 Sep 2019) 4.5.5.1.1, 4.5.5.1.2, 4.5.5.2; `AQA-8464-spec.txt` — searched, no fluid-pressure content; `8463-equation-sheet-Jun26.txt` (prints p = F/A; p = h ρ g marked HT). Route audit read: `ks4-routes/docs/ks4/route-audit/physics.md` row `pressure-in-a-fluid` ("HT layer: p = hρg and upthrust (4.5.5.1.2 HT). The key note currently shows both to TF.").

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n; th1–th3 = theory chunks. Site's "6.5.5 (physics only)" is internal; true refs 8463 **4.5.5.1.1**, **4.5.5.1.2 (HT only)**, **4.5.5.2**. Two route copies (TF, TH); TF `higher` copy is `null`.

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8463 | **4.5.5.1.1** | Pressure in a fluid 1 | (physics only) |
| 8463 | **4.5.5.1.2** | Pressure in a fluid 2 | (physics only) **(HT only)** |
| 8463 | **4.5.5.2** | Atmospheric pressure | (physics only) |
| Supporting | 8463 4.5.1.3 W = mg; 4.3.1.1 density | | base |

Spec statements (verbatim):
- 4.5.5.1.1: "A fluid can be either a liquid or a gas. The pressure in fluids causes a force normal (at right angles) to any surface. The pressure at the surface of a fluid can be calculated using the equation: pressure = force normal to a surface / area of that surface, p = F/A … pressure, p, in pascals, Pa; force, F, in newtons, N; area, A, in metres squared, m²" — "recall and apply this equation."
- 4.5.5.1.2 (HT only): "The pressure due to a column of liquid can be calculated using the equation: pressure = height of the column × density of the liquid × gravitational field strength [p = hρg] … Students should be able to apply this equation which is given on the Physics equation sheet. … (In any calculation the value of the gravitational field strength (g) will be given.) Students should be able to explain why, in a liquid, pressure at a point increases with the height of the column of liquid above that point and with the density of the liquid. Students should be able to calculate the differences in pressure at different depths in a liquid. A partially (or totally) submerged object experiences a greater pressure on the bottom surface than on the top surface. This creates a resultant force upwards. This force is called the upthrust. Students should be able to describe the factors which influence floating and sinking."
- 4.5.5.2: "The atmosphere is a thin layer (relative to the size of the Earth) of air round the Earth. The atmosphere gets less dense with increasing altitude. Air molecules colliding with a surface create atmospheric pressure. The number of air molecules (and so the weight of air) above a surface decreases as the height of the surface above ground level increases. So as height increases there is always less air above a surface than there is at a lower height. So atmospheric pressure decreases with an increase in height." — describe a simple model of the atmosphere and of atmospheric pressure; explain why atmospheric pressure varies with height.

## 2. Route table
| # | teachable point (pack location) | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Pressure acts in all directions (th1; common_mistake) | triple | 4.5.5.1.1 ("force normal to any surface") | TF TH | OK; spec wording missing (F2) |
| R2 | P = F ÷ A; Pa; 1 Pa = 1 N/m² (th1; equations; variables; key_note) | triple | 4.5.5.1.1 | TF TH | OK |
| R3 | Pressure increases with depth; P = hρg; seawater example (th1; equations; key_note) | triple-higher | 4.5.5.1.2 (HT only) | TF TH | ROUTE (F1) |
| R4 | Atmospheric pressure: value, decreases with altitude, why (th2; key_note) | triple | 4.5.5.2 | TF TH | IMPRECISE cause (F3) |
| R5 | Suction cups, straws, barometer, weather, altitude values (th2) | triple (context) | 4.5.5.2 | TF TH | OK / weather OFF-SPEC |
| R6 | Upthrust, Archimedes, floating/sinking, density (th3; key_note; common_mistake) | triple-higher (Archimedes off-spec) | 4.5.5.1.2 (HT only) | TF TH | ROUTE (F1); OFF-SPEC (F4) |
| R7 | common_mistake: P = hρg is extra to atmospheric | triple-higher | 4.5.5.1.2 | TF TH | OK, ROUTE (F1) |
| R8 | `higher` — P = hρg; pressure differences | triple-higher | 4.5.5.1.2 (HT only) | TH | OK |
| R9 | `higher` — upthrust F = ρVg; fraction submerged | off-spec | — | TH | OFF-SPEC (F4) |
| R10 | FIFA (5 m fresh water, 49 kPa) | triple-higher | 4.5.5.1.2 (HT only) | TF TH | OK; ROUTE (F1) |
| R11 | q1 (why pressure increases with depth) | triple-higher | 4.5.5.1.2 (HT only) | TF TH | OK; ROUTE (F1) |
| R12 | q2 (steel ship floats) | triple-higher | 4.5.5.1.2 (HT only) | TF TH | OK; ROUTE (F1) |
| — | RP | none | — | — | correct |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | th1 | pressure in a fluid acts in all directions at a point | OK | true; spec's own statement is "causes a force normal (at right angles) to any surface" — teach that (F2) | 4.5.5.1.1 |
| C2 | th1; variables | P = F ÷ A; Pa, N, m²; 1 Pa = 1 N/m² | OK | spec uses lower-case p | 4.5.5.1.1 |
| C3 | th1 | deeper → more fluid above → greater weight → greater pressure | OK (HT) | — | 4.5.5.1.2 |
| C4 | th1 | P = h × ρ × g; h depth m; ρ kg/m³; g N/kg | OK (HT) | spec: "height of the column" | 4.5.5.1.2 |
| C5 | th1 | 10 m seawater, ρ 1025, g 9.8 → 100,450 Pa ≈ 100 kPa | OK | 10 × 1025 × 9.8 = 100,450 ✓ | — |
| C6 | th2 | atmospheric pressure "is caused by the weight of the air column above" | IMPRECISE | Spec: air molecules colliding with a surface create atmospheric pressure; fewer molecules (less weight of air) above at greater height → lower pressure. | 4.5.5.2 |
| C7 | th2 | sea level ≈ 101,325 Pa ≈ 100 kPa = 1 atm | OK | — | — |
| C8 | th2 | decreases with altitude — less air above | OK | — | 4.5.5.2 |
| C9 | th2 | suction cup; straw ("lungs create lower pressure"); barometer | OK | straw: lower pressure in the mouth; fine as context | — |
| C10 | th2 | "high pressure = fair weather; low pressure = storms" | OFF-SPEC | generalisation, not in spec; cut or leave as untested context | — |
| C11 | th2 | ~half sea-level pressure at 5500 m; ~26 kPa at 10,000 m | OK | standard atmosphere ≈ 50.5 kPa at 5.5 km, ≈ 26.5 kPa at 10 km ✓ | — |
| C12 | th3 | upthrust = upward force on submerged object; bottom pressure > top | OK (HT) | spec's explanation | 4.5.5.1.2 |
| C13 | th3 | Archimedes: upthrust = weight of fluid displaced; "pressure difference × area = weight of displaced fluid" | OFF-SPEC | correct physics; not in 8463 | 4.5.5.1.2 |
| C14 | th3 | floats when upthrust = weight; sinks when weight > upthrust | OK (HT) | — | 4.5.5.1.2 |
| C15 | th3 | ship; hot-air balloon; diver neutral buoyancy | OK | context | — |
| C16 | th3 | floats if density < fluid; ice 917 kg/m³ on water 1000 kg/m³ | OK (HT) | ✓ | 4.5.5.1.2 |
| C17 | `higher` | P = hρg; pressure differences | OK | — | 4.5.5.1.2 |
| C18 | `higher` | "Calculate upthrust: F = ρVg"; "fraction of a floating object submerged" | OFF-SPEC | — | 4.5.5.1.2 |
| C19 | common_mistake | acts in all directions; hρg is additional to atmospheric; upthrust = weight of displaced fluid | OK / OFF-SPEC (3rd sentence Archimedes) | sentences 2–3 HT | 4.5.5.1.2 |
| C20 | key_note | "Float when upthrust ≥ weight" | IMPRECISE | floating at rest: upthrust = weight; greater than weight means it rises | 4.5.5.1.2 |
| C21 | equations | P = F ÷ A; P = h × ρ × g | OK | both On the sheet (8463 June 2026; hρg marked HT) | 8463 sheet |
| C22 | variables | P, F, A, h, ρ | OK | g missing from the table (needed for hρg) | — |
| C23 | FIFA | 5 × 1000 × 9.8 = 49,000 Pa = 49 kPa | OK | ✓; no chain | 4.5.5.1.2 |
| C24 | Convert `[NEW]` | "Nothing to convert — depth … metres, density … kg/m³ and g … N/kg" | OK | marked examined ✓ | CFIFA amendment |
| C25 | q1 key | more fluid above, greater weight; pressure = weight of fluid per unit area above | OK | — | 4.5.5.1.2 |
| C26 | q1 opt 2 / wx1 | molecules faster at depth | OK aligned | — | — |
| C27 | q1 opt 3 / wx2 | water nearly incompressible | OK aligned | — | — |
| C28 | q1 opt 4 / wx3 | g effectively constant | OK aligned | — | — |
| C29 | q2 key | hollow ship displaces large volume; upthrust (weight of displaced water) = ship's weight | OK | the parenthesis is Archimedes (off-spec) but true; the on-spec core "upthrust equals the ship's weight" is the credited idea | 4.5.5.1.2 |
| C30 | q2 opt 2 / wx1 | salt water denser than steel | OK aligned | — | — |
| C31 | q2 opt 3 / wx2 | engines give forward thrust | OK aligned | — | — |
| C32 | q2 opt 4 / wx3 | hull shape "lift" | OK aligned | — | — |
| C33 | matching (to be replaced) | P = hρg; atmospheric; upthrust; floats | OK | replaced anyway | — |
| C34 | header routes | TF TH | OK | HT layer shown unbadged on TF (F1) | — |

Count: **WRONG 0**. ROUTE 1 (all HT material reaches TF). IMPRECISE 2 (atmospheric cause; "≥ weight"). OFF-SPEC 2 (Archimedes/ρVg/fraction; weather). GAP 2 (spec core wording; no TF worked example, no pressure-difference example). wrong_explanations: all 6 read and aligned. 2 calculations rechecked ✓.

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| q1 | HT explanation | TH only |
| q2 | floating/sinking is HT | TH only |
| FIFA | p = hρg is HT | TH only; TF needs its own p = F/A worked example (F6) |

## 5. Calculations (rule 3)
- p = F ÷ A: no chain. Convert cm² → m² (÷ 10,000), mm² → m², kN → N. Base (triple).
- p from a mass on an area: **chains** — Step 1 W = m g; Step 2 p = W ÷ A. Base (triple). Not in the source; any item that gives a mass needs this worked example first.
- p = h ρ g: no chain. Convert cm → m, g/cm³ → kg/m³ (× 1000); answer often in kPa. HT.
- Pressure difference between two depths: no chain when taught as Δp = Δh × ρ × g (recommended); **chains** if pupils find each pressure then subtract (Step 1 p at each depth; Step 2 subtract). HT.

## 6. Verdict
SOURCE OK WITH FLAGS. All numbers correct; both quiz items correct and aligned. Every HT point (p = hρg, depth explanation, upthrust, floating) is served to Triple Foundation unbadged — the route audit's finding confirmed. Atmospheric pressure is caused by molecules colliding, not "the weight of the air column" (the weight explains the change with height). The spec's own core sentences (force normal to a surface; fluid = liquid or gas; the atmosphere model) are written into the source. Upthrust overlaps the TH-only `upthrust-floating` page. Nothing for Mide.
