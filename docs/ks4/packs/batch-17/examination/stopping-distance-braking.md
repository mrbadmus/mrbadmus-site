# Examination — Stopping Distance and Braking (stopping-distance-braking) — AQA 8464 6.5.4.3.1–6.5.4.3.4 / 8463 4.5.6.3.1–4.5.6.3.4
Verdict: SOURCE HAS ERRORS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-17/04-checked-science-source/physics-6.5.4.3-stopping-distance-braking.md`.
Spec sources read as text: `AQA-8464-spec.txt` (v1.1, 04 Oct 2019) 6.5.4.3.1–6.5.4.3.4, 6.5.5; `AQA-8463-spec.txt` (v1.1, 30 Sep 2019) 4.5.6.3.1–4.5.6.3.4, 4.5.7.3. Equation sheets: `8464-equation-sheet.txt`, `8463-equation-sheet-Jun26.txt` (June 2026) — both print s = vt, W = Fs, Ek = ½mv², a = Δv/t, v² − u² = 2as, F = ma; only 8463 prints F = mΔv/Δt (HT). Route audit row `stopping-distance-braking` (base).

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n; th1–th3 = theory chunks. Route copies identical except `higher` (TH text on CH/TH; `null` on CF/TF).

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 | **6.5.4.3.1** | Stopping distance | base |
| 8464 | **6.5.4.3.2** | Reaction time | base |
| 8464 | **6.5.4.3.3** | Factors affecting braking distance 1 | base |
| 8464 | **6.5.4.3.4** | Factors affecting braking distance 2 | base; force estimate **(HT only)** |
| 8463 | **4.5.6.3.1–4.5.6.3.4** | same four | same labels; plus two **(physics only)** sentences in 4.5.6.3.1 |
| Supporting | 8463 4.5.7.3 Changes in momentum (physics only), inside 4.5.7 (HT only) | | triple-higher |

Spec statements (verbatim, both unless marked): "The stopping distance of a vehicle is the sum of the distance the vehicle travels during the driver's reaction time (thinking distance) and the distance it travels under the braking force (braking distance). For a given braking force the greater the speed of the vehicle, the greater the stopping distance." 8463 only: "(Physics only) Students should be able to estimate how the distance for a vehicle to make an emergency stop varies over a range of speeds typical for that vehicle. (Physics only) Students will be required to interpret graphs relating speed to stopping distance for a range of vehicles." "Reaction times vary from person to person. Typical values range from 0.2 s to 0.9 s. A driver's reaction time can be affected by tiredness, drugs and alcohol. Distractions may also affect a driver's ability to react." "explain methods used to measure human reaction times and recall typical results; interpret and evaluate measurements from simple methods to measure the different reaction times of students; evaluate the effect of various factors on thinking distance based on given data." "The braking distance of a vehicle can be affected by adverse road and weather conditions and poor condition of the vehicle. Adverse road conditions include wet or icy conditions. Poor condition of the vehicle is limited to the vehicle's brakes or tyres." "explain the factors which affect the distance required for road transport vehicles to come to rest in emergencies, and the implications for safety; estimate how the distance required for road vehicles to stop in an emergency varies over a range of typical speeds." "When a force is applied to the brakes of a vehicle, work done by the friction force between the brakes and the wheel reduces the kinetic energy of the vehicle and the temperature of the brakes increases. The greater the speed of a vehicle the greater the braking force needed to stop the vehicle in a certain distance. The greater the braking force the greater the deceleration of the vehicle. Large decelerations may lead to brakes overheating and/or loss of control." "explain the dangers caused by large decelerations; (HT only) estimate the forces involved in the deceleration of road vehicles in typical situations on a public road."

## 2. Route table
| # | teachable point | true layer | spec | verdict |
|---|---|---|---|---|
| R1 | Stopping = thinking + braking; definitions (th1, equations, key_note) | base | 6.5.4.3.1 | OK |
| R2 | Thinking distance = speed × reaction time (th1, th2, equations) | base | 6.5.4.1.2 (s = vt) + 6.5.4.3.2 | OK |
| R3 | Typical 30 / 60 mph figures (th1) | base | 6.5.4.3.3 (estimate over typical speeds) | IMPRECISE (C3) |
| R4 | Reaction-time factors: alcohol, drugs, tiredness, distraction; 0.2–0.9 s (th2, key_note) | base | 6.5.4.3.2 | OK |
| R5 | Measuring reaction time: ruler drop etc. (th2) | base | 6.5.4.3.2 | OK |
| R6 | Braking factors: speed, wet/icy, tyres, brakes (th3, key_note) | base | 6.5.4.3.3 | OK except C9 |
| R7 | Braking distance ∝ v² (th1, th3, common_mistake, equations, q1) | base | 6.5.4.3.1/.3.3 + 6.5.2 W = Fs + Ek | OK (for the same braking force) |
| R8 | Work by braking force removes Ek; d = mv² ÷ 2F (th3) | base (mechanism); force from it = **higher** | 6.5.4.3.4; (HT only) estimate forces | OK |
| R9 | Large decelerations → injury; seat belts, crumple zones (th3) | base (mention) | 6.5.4.3.4 | IMPRECISE — spec's dangers are overheating / loss of control (C13) |
| R10 | `higher`: F = Δp/Δt for deceleration forces | **triple-higher** | 8463 4.5.7.3 (physics only) in 4.5.7 (HT only) | ROUTE — never on CH |
| R11 | `higher`: worn tyres / water dispersal | **base** | 6.5.4.3.3 | ROUTE — not HT |
| R12 | `higher`: deceleration and injury risk | base ("explain the dangers") | 6.5.4.3.4 | ROUTE |
| R13 | FIFA (chains two relationships) | base | 6.5.4.3.1; 6.5.4.1.2 | OK; chain flagged (rule 3) |
| R14 | q1 doubling speed → ×4 braking | base | 6.5.4.3.1/.3.3 | OK |
| R15 | q2 alcohol | base | 6.5.4.3.2 | **WRONG item** (two defensible options) |
| R16 | Estimate deceleration forces | **higher** | 6.5.4.3.4 (HT only) | GAP — no worked example |
| R17 | Interpret speed–stopping-distance graphs for a range of vehicles | **triple** | 8463 4.5.6.3.1 (physics only) | GAP |
| R18 | Brake temperature rises; speed ↑ → braking force needed ↑; braking force ↑ → deceleration ↑; overheating / loss of control | base | 6.5.4.3.4 | GAP (partly) |
| — | RP | none (AT 1 activity "measure the effect of distractions on reaction time" is not an RP) | 6.5.4.3.2 | correct |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | th1 | stopping = thinking + braking; definitions | OK | spec wording | 6.5.4.3.1 |
| C2 | th1, th2 | thinking distance = speed × reaction time | OK | = s = vt (on both sheets) | 6.5.4.1.2 |
| C3 | th1 | "30 mph = 13.3 m/s" | IMPRECISE | 30 mph = 13.4 m/s (30 × 1609 ÷ 3600 = 13.41). Highway Code 9 m + 14 m = 23 m ✓. | — |
| C4 | th1 | 60 mph stopping ≈ 73 m; "much more than double" | OK | Highway Code 18 + 55 = 73 m ✓; 73/23 ≈ 3.2 ✓ | — |
| C5 | th2 | alcohol, drugs, tiredness, distraction | OK | spec list | 6.5.4.3.2 |
| C6 | th2 | "ALCOHOL — slows nerve impulse transmission" | OK | acceptable simplification (depressant) | — |
| C7 | th2 | 0.2–0.9 s; "average ~0.7 s" | OK | range is spec; 0.7 s is the Highway-Code-style typical value | 6.5.4.3.2 |
| C8 | th2 | ruler drop, electronic testers, computer tests | OK | — | 6.5.4.3.2 |
| C9 | th3 | "Under-inflated tyres: reduce contact area" | **WRONG** (theory, re-cuttable) | Under-inflation **increases** the contact patch; the hazard is poor grip/handling and overheating. Spec limits tyre condition to "poor condition"; teach worn/bald tread (less grip, especially in the wet). Cut the line. | 6.5.4.3.3 |
| C10 | th3 | wet, icy, gravel → less friction/grip; bald tyres → aquaplaning; worn pads, brake fade | OK | — | 6.5.4.3.3–4 |
| C11 | th3 | more mass → more Ek → longer braking distance for same braking force | OK | follows from W = Fs = ½mv² (spec's "poor condition" list is about brakes/tyres; mass is a valid extra factor) | 6.5.4.3.4 |
| C12 | th3; equations; common_mistake; q1 | F × d = ½mv² → d = mv² ÷ 2F → d ∝ v²; doubling v quadruples braking distance; thinking ∝ v | OK | Correct for a constant braking force — state that condition once. | 6.5.2; 6.1.1.2; 6.5.4.3.4 |
| C13 | th3 | "Hard braking → large deceleration → large forces on passengers… seat belts and crumple zones" | IMPRECISE | True, but the spec's named dangers of large decelerations are **brakes overheating and/or loss of control** — teach those. The momentum explanation of seat belts/crumple zones is triple-higher (8463 4.5.7.3). | 6.5.4.3.4 |
| C14 | `higher` | "F = Δp/Δt" | ROUTE | 8463 4.5.7.3 is (physics only) inside 4.5.7 (HT only): TH only. Not on the Combined spec or the 8464 sheet. On CH the HT force estimate uses F = ma with a from v² − u² = 2as, or W = Fs with Ek. | 8463 4.5.7.3; 8464 6.5.4.3.4 |
| C15 | `higher` | worn tyres, water dispersal | ROUTE | base (6.5.4.3.3), not HT | 6.5.4.3.3 |
| C16 | FIFA | 20 × 0.6 = 12 m; 12 + 40 = 52 m | OK | ✓. Chains two relationships (rule 3). | — |
| C17 | CFIFA Convert | "Nothing to convert…" + an editorial NOTE about the chain | IMPRECISE | The conversion statement is right; the NOTE is not a Convert step and must not reach pupils. → `[NEW — examiner-corrected]` (chain moved to SDB-F7). | CFIFA amendment |
| C18 | q1 key | ×4 because (20/10)² = 4 | OK | ✓ | — |
| C19 | q1 opt1 / wx1 | doubles | OK | aligned ✓ | — |
| C20 | q1 opt2 / wx2 | opt2 "+10 m, simple addition"; wx2 "Braking distance is not fixed — it depends on speed squared…" | IMPRECISE | wx2 does not say why adding 10 m is wrong (it reads as an answer to option 3). Not false. Item usable. | — |
| C21 | q1 opt3 / wx3 | stays the same | OK | aligned ✓ | — |
| C22 | q2 key | alcohol increases reaction time → thinking distance increases | OK | the mark-scheme answer | 6.5.4.3.2 |
| C23 | q2 opt2 / wx2 | "Alcohol blurs vision — the driver takes longer to see the hazard and applies brakes later"; wx2 "Vision is relevant but…" | **WRONG** | "Takes longer to see the hazard and applies brakes later" **is** a longer reaction time, i.e. a longer thinking distance — a defensible correct answer (and wx2 concedes it). Two defensible options. | 6.5.4.3.2 |
| C24 | q2 opt1 / wx1; opt3 / wx3 | muscles; vehicle mass | OK | aligned ✓ | — |
| C25 | matching (to be replaced) | five factor pairs | OK | ✓ | — |

Count: **1 WRONG item** (q2 — two defensible answers); **WRONG theory line**: C9 (re-cuttable); **ROUTE**: C14, C15 (+R12); **IMPRECISE**: C3, C13, C17, C20. **GAP**: HT force estimate, physics-only stopping-distance graphs, brake heating / loss of control. All arithmetic ✓ (6 calculations).

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| q1 | wx2 weak, not false | Usable on all four routes. |
| q2 | Option 2 is also a correct answer | **Do not use as written** (any route). |

## 5. Verdict
SOURCE HAS ERRORS. The stopping-distance physics and all arithmetic are right, but frozen q2 has two defensible answers, one theory line (under-inflated tyres) is backwards, and the `higher` field routes F = Δp/Δt (triple-higher only) onto Combined Higher. The worked example chains two relationships and needs a Step 1 / Step 2 example (rule 3). The spec's named dangers (overheating, loss of control), the HT force estimate and the physics-only stopping-distance graphs are missing from the frozen data.
