# Examination — Upthrust and Floating (upthrust-floating) — AQA 8463 4.5.5.1.2 (physics only, HT only); not in 8464
Verdict: SOURCE HAS ERRORS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-17/04-checked-science-source/physics-6.5.5.1.2-upthrust-floating.md`.
Spec sources read as text: `AQA-8463-spec.txt` (v1.1, 30 Sep 2019) 4.5.5.1.2, 4.5.5.1.1; `AQA-8464-spec.txt` — searched, no upthrust content; `8463-equation-sheet-Jun26.txt` (prints p = F/A and p = h ρ g (HT); no upthrust equation). Route audit read: `ks4-routes/docs/ks4/route-audit/physics.md` row `upthrust-floating` (TH, OK).

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n; th1–th3 = theory chunks. Site's "6.5.5.1.2 (HT only)" is internal; true ref 8463 **4.5.5.1.2**, labelled (physics only) by its parent 4.5.5 and (HT only). Single route copy (TH).

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8463 | **4.5.5.1.2** | Pressure in a fluid 2 | (physics only) **(HT only)** |
| Supporting | 8463 4.5.5.1.1 p = F/A; 4.3.1.1 density; 4.5.1.4 resultant force | | triple / base |

Spec statements (verbatim, 8463 4.5.5.1.2, HT only):
- "The pressure due to a column of liquid can be calculated using the equation: pressure = height of the column × density of the liquid × gravitational field strength [p = hρg]" — "apply this equation which is given on the Physics equation sheet."
- "Students should be able to calculate the differences in pressure at different depths in a liquid."
- "A partially (or totally) submerged object experiences a greater pressure on the bottom surface than on the top surface. This creates a resultant force upwards. This force is called the upthrust."
- "Students should be able to describe the factors which influence floating and sinking."

The spec gives no upthrust equation and does not name Archimedes' principle.

## 2. Route table
| # | teachable point (pack location) | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Upthrust = upward force; bottom pressure > top; resultant up (th1) | triple-higher | 4.5.5.1.2 | TH | OK |
| R2 | Net force = pressure difference × area (th1) | triple-higher | 4.5.5.1.2 + 4.5.5.1.1 | TH | IMPRECISE (F3) |
| R3 | Archimedes; Upthrust = ρ V g (th1, th2, th3; equations; variables; key_note; common_mistake; `higher`) | off-spec | — | TH | OFF-SPEC (F1) |
| R4 | Floats when upthrust = weight; sinks lower until it does (th1; key_note) | triple-higher | 4.5.5.1.2 | TH | OK |
| R5 | "A denser object displaces less volume before sinking" (th1) | triple-higher | 4.5.5.1.2 | TH | WRONG (F2) |
| R6 | Worked example, block 60% submerged (th2) | off-spec | — | TH | OFF-SPEC (F1) |
| R7 | Density comparison: float / neutral / sink (th2; key_note) | triple-higher | 4.5.5.1.2 | TH | OK |
| R8 | Ships: hollow hull, average density; flooding (th2) | triple-higher | 4.5.5.1.2 | TH | OK |
| R9 | Finding density by weighing in water (th3) | off-spec | — | TH | OFF-SPEC (F4) |
| R10 | Submarines, ballast tanks (th3; key_note) | triple-higher | 4.5.5.1.2 | TH | OK |
| R11 | FIFA (upthrust 50 N) | off-spec | — | TH | OFF-SPEC (F1) |
| R12 | q1 (20 N vs 30 N) | off-spec calculation | — | TH | OFF-SPEC (F1) |
| R13 | q2 (iceberg 89.5%) | off-spec | — | TH | OFF-SPEC (F1) |
| — | RP | none | — | — | correct |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | th1 | upthrust = upward force on a submerged object | OK | — | 4.5.5.1.2 |
| C2 | th1 | pressure increases with depth, P = hρg; bottom > top | OK | — | 4.5.5.1.2 |
| C3 | th1 | net upward force = pressure difference × cross-sectional area | IMPRECISE | true for a block with vertical sides (top and bottom faces of equal area); fine if the figure is such a block | 4.5.5.1.1–2 |
| C4 | th1 | Archimedes: upthrust = weight of fluid displaced = ρ V g | OFF-SPEC | correct physics; not in 8463 | 4.5.5.1.2 |
| C5 | th1 | floats when upthrust = weight; sinks until enough displaced | OK | — | 4.5.5.1.2 |
| C6 | th1 | "A denser object displaces less volume before sinking — if density > fluid, it fully submerges and still sinks" | WRONG (first clause) | For the same volume a denser object is heavier, so it must displace MORE fluid to float: it floats lower. Second clause OK. | 4.5.5.1.2 |
| C7 | th2 | block 0.01 m³, 600 kg/m³: weight 60 N; V displaced 0.006 m³; 60% | OFF-SPEC (arithmetic OK) | 600 × 0.01 × 10 = 60 ✓; 60 ÷ (1000 × 10) = 0.006 ✓ | — |
| C8 | th2 | density < fluid floats; = neutrally buoyant; > sinks | OK | — | 4.5.5.1.2 |
| C9 | th2 | ship: average density of hull + air < water; flooding → sinks | OK | — | 4.5.5.1.2 |
| C10 | th3 | Upthrust = ρ V g; V_sub = V_object when fully submerged | OFF-SPEC | — | — |
| C11 | th3 | density by weighing in air and in water | OFF-SPEC (method correct) | AQA's density method is the displacement can (RP, 4.3.1.1) | 4.3.1.1 |
| C12 | th3 | submarine ballast tanks; neutral buoyancy at seawater density | OK | average density | 4.5.5.1.2 |
| C13 | `higher` | calculate upthrust by Archimedes; fraction submerged | OFF-SPEC | "compare upthrust with weight" is on-spec | 4.5.5.1.2 |
| C14 | common_mistake | upthrust = weight of displaced fluid; 100 N steel block upthrust "much less than 100 N" | OFF-SPEC framing, physics OK | ρ steel ≈ 7800 kg/m³ → upthrust ≈ 13 N ✓ | — |
| C15 | key_note | ρVg; float/sink by density; ship; submarine | OFF-SPEC (ρVg) / OK | — | 4.5.5.1.2 |
| C16 | equations; variables | Upthrust = ρ_fluid × V_submerged × g; U, ρ, V, g | OFF-SPEC | not on spec or June 2026 sheet; no formula triangle | 8463 sheet |
| C17 | FIFA | 1000 × 0.005 × 10 = 50 N | OFF-SPEC (arithmetic OK) | ✓ | — |
| C18 | Convert `[NEW]` | "Nothing to convert — volume … m³, density … kg/m³ and g … N/kg" | OK | line itself correct, marked examined ✓; the FIFA it fronts is off-spec (F1) | CFIFA amendment |
| C19 | q1 key | 1000 × 0.002 × 10 = 20 N < 30 N → sinks | OFF-SPEC (arithmetic OK) | ✓ | — |
| C20 | q1 opt 2 / wx1 | floats | OK aligned | its second sentence ("would hover only if…") belongs to opt 3, harmless | — |
| C21 | q1 opt 3 / wx2 | hovers | OK aligned | — | — |
| C22 | q1 opt 4 / wx3 | rises | OK aligned | — | — |
| C23 | q2 key | 917 ÷ 1025 = 0.895 → 89.5% below | OFF-SPEC (arithmetic OK) | 0.8946 ✓ | — |
| C24 | q2 opt 2 / wx1 | 10.5% is above water | OK aligned | ✓ | — |
| C25 | q2 opt 3 / wx2 | half only if half the density | OK aligned | — | — |
| C26 | q2 opt 4 / wx3 | ice less dense, floats | OK aligned | — | — |
| C27 | matching (to be replaced) | float/sink by density; ρVg; submarine | OK / OFF-SPEC row 3 | replaced anyway | — |
| C28 | header routes | TH | OK | (physics only, HT only) | 4.5.5.1.2 |

Count: **WRONG 1** (C6); OFF-SPEC: Archimedes/ρVg throughout incl. FIFA, q1, q2; weighing method. IMPRECISE 1 (C3). wrong_explanations: all 6 read and aligned. All 6 arithmetic results rechecked ✓.

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| q1 | needs Upthrust = ρVg (off-spec) | Not usable on any route |
| q2 | fraction-submerged calculation (off-spec) | Not usable on any route |
| FIFA | Upthrust = ρVg (off-spec) | Not usable; see §5 for an on-spec calculation |

## 5. Calculations (rule 3)
The spec requires no upthrust calculation. On-spec option if Design wants one (HT): upthrust on a block with vertical sides — **chains** — Step 1 pressure difference Δp = Δh × ρ × g (Δh = block height); Step 2 upthrust F = Δp × A. Convert cm → m, cm² → m². Every frozen calculation (ρVg, fraction submerged) is off-spec.

## 6. Verdict
SOURCE HAS ERRORS. The spec's explanation (bottom pressure greater than top → resultant upward force) and the floating/sinking factors are present and correct. The frozen data builds the lesson on Archimedes' principle and Upthrust = ρVg, which 8463 does not contain, so the FIFA and both quiz items are off-spec (correct arithmetic, not usable). One WRONG theory clause on denser objects. Nothing for Mide: the spec text is unambiguous.
