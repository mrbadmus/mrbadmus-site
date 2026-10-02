# Examination — Transformers (transformers) — AQA 8463 4.7.3.4 (+ 8464 6.2.4.3 HT for Vp Ip = Vs Is)
Verdict: SOURCE HAS ERRORS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-18/04-checked-science-source/physics-6.7.3.4-transformers.md`.
Spec sources read as text: `AQA-8463-spec.txt` (v1.1, 30 Sep 2019) §4.2.4.3, 4.7.3, 4.7.3.4; `AQA-8464-spec.txt` (v1.1, 04 Oct 2019) §6.2.4.1, 6.2.4.3; June 2026 equation sheets `8463-equation-sheet-Jun26.txt` (HT: Vp/Vs = np/ns; Vp Ip = Vs Is; P = VI; P = I²R) and `8464-equation-sheet.txt` (HT: Vp Ip = Vs Is; P = VI; P = I²R; no turns-ratio equation). Route audit `ks4-routes/docs/ks4/route-audit/physics.md` rows 30, 89.

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n. One route copy (TH).

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8463 | **4.7.3.4** | Transformers | **(HT only)**, under 4.7.3 "(physics only) (HT only)" |
| 8464 | **6.2.4.3** | The National Grid | base; "Higher tier only: … Vp × Ip = Vs × Is … as given on the equation sheet"; "Detailed knowledge of the structure of a transformer is not required." |
| 8463 | 4.2.4.3 | The National Grid | base (= 8464 6.2.4.3 without the HT equation; points to 4.7.3.4) |
| Supporting | 8464 6.2.4.1 / 8463 4.2.4.1 Power (P = VI, P = I²R — base) | | |

Spec statements (verbatim, 8463 4.7.3.4): "A basic transformer consists of a primary coil and a secondary coil wound on an iron core." "Iron is used as it is easily magnetised." "Knowledge of laminations and eddy currents in the core is not required." "The ratio of the potential differences across the primary and secondary coils of a transformer Vp and Vs depends on the ratio of the number of turns on each coil, np and ns." Vp/Vs = np/ns — "Students should be able to apply this equation which is given on the Physics equation sheet." "In a step-up transformer Vs > Vp. In a step-down transformer Vs < Vp." "If transformers were 100% efficient, the electrical power output would equal the electrical power input." Vs × Is = Vp × Ip — "Where Vs × Is is the power output (secondary coil) and Vp × Ip is the power input (primary coil)." "Students should be able to: • explain how the effect of an alternating current in one coil in inducing a current in another is used in transformers • explain how the ratio of the potential differences across the two coils depends on the ratio of the number of turns on each • calculate the current drawn from the input supply to provide a particular power output • apply the equation linking the p.d.s and number of turns in the two coils of a transformer to the currents and the power transfer involved, and relate these to the advantages of power transmission at high potential differences."

8464 6.2.4.3 (verbatim, relevant part): "Step-up transformers are used to increase the potential difference from the power station to the transmission cables then step-down transformers are used to decrease, to a much lower value, the potential difference for domestic use. Students should be able to explain why the National Grid system is an efficient way to transfer energy. Higher tier only: Students should be able to select and use the equation: potential difference across primary coil x current in primary coil = potential difference across secondary coil x current in secondary coil as given on the equation sheet."

## 2. Route table
| # | teachable point | true layer | spec | verdict |
|---|---|---|---|---|
| R1 | Construction: primary, secondary, iron core (theory 1; key_note) | triple-higher | 8463 4.7.3.4 | OK; reason for iron IMPRECISE (F3) |
| R2 | How it works: ac in primary → changing field in core → pd induced in secondary; dc gives no output (theory 1; common_mistake; q1) | triple-higher | 8463 4.7.3.4 | OK (terminology F4) |
| R3 | Vs/Vp = Ns/Np; step-up / step-down by turns (theory 2; equations; FIFA; variables; key_note) | triple-higher | 8463 4.7.3.4 | OK |
| R4 | Vp Ip = Vs Is; voltage up → current down (theory 2; equations; common_mistake; key_note) | **higher** (8464 6.2.4.3 HT) — also 8463 4.7.3.4 | 8464 6.2.4.3; 8463 4.7.3.4 | OK |
| R5 | National Grid: step-up for transmission, step-down for homes (theory 3) | base | 8464 6.2.4.3; 8463 4.2.4.3 | OK |
| R6 | Why high pd: P = VI → lower current → lower I²R loss (theory 3; common_mistake; q2) | base | 8464 6.2.4.3, 6.2.4.1 | OK, but worked numbers WRONG (F1) |
| R7 | Grid voltages 25 kV / 400 kV / 33 kV / 11 kV / 230 V (theory 3) | base (context) | — | OK |
| R8 | Eddy currents, laminated core, flux leakage, 95–99 % (theory 3) | **explicitly excluded** | 8463 4.7.3.4 | OFF-SPEC (F2) |
| R9 | q1 | triple-higher | 8463 4.7.3.4 | usable |
| R10 | q2 | base | 8464 6.2.4.3 | usable |
| R11 | FIFA (turns ratio) | triple-higher | 8463 4.7.3.4 | OK |
| R12 | Current drawn from supply for a given output; chained turns → current problems | triple-higher (Vp Ip = Vs Is step alone: higher) | 8463 4.7.3.4 | **GAP** — no worked example (F5) |
| — | RP, examiner_tip | none | — | correct |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | theory 1 | transformer changes the voltage of an ac supply | OK | "potential difference" is AQA's word. | 4.7.3.4 |
| C2 | theory 1 | two coils on an iron core; primary = input, secondary = output | OK | — | 4.7.3.4 |
| C3 | theory 1 | "SOFT IRON CORE: channels magnetic flux between the coils efficiently" | IMPRECISE | The spec's reason: "Iron is used as it is easily magnetised." | F3; 4.7.3.4 |
| C4 | theory 1 | ac in primary → alternating field in core → threads secondary → changing field induces pd in secondary ("mutual induction", "Faraday's Law", "EMF") | OK (terminology) | Physics right. "Mutual induction", "flux", "emf", "Faraday's Law" are not AQA GCSE terms. | F4 |
| C5 | theory 1 | transformers only work with ac; dc → constant field → nothing induced | OK | Follows from 4.7.3.4 bullet 1 and 4.7.3.1. | 4.7.3.4 |
| C6 | theory 2 | Vs/Vp = Ns/Np, variables | OK | Same relation as the sheet's Vp/Vs = np/ns; show the **sheet's form and lowercase n** so pupils recognise it in the exam. | 4.7.3.4; 8463 sheet |
| C7 | theory 2 | step-up Ns > Np → Vs > Vp; step-down Ns < Np → Vs < Vp | OK | — | 4.7.3.4 |
| C8 | theory 2 | ideal transformer: power in = power out; Vp Ip = Vs Is | OK | — | 4.7.3.4; 8464 6.2.4.3 |
| C9 | theory 2 | Vp/Vs = Is/Ip; step-up voltage → step-down current | OK | ✓ rearrangement. | — |
| C10 | theory 2 | 230 V, 100 → 500 turns: Vs = 230 × 5 = 1150 V | OK | ✓ | — |
| C11 | theory 3 | power station → step-up → transmission → step-down → consumers | OK | — | 8464 6.2.4.3 |
| C12 | theory 3 | 25 kV → 400 kV → 33 kV → 11 kV → 230 V | OK (context) | Representative UK values (275 kV and 132 kV also used). | — |
| C13 | theory 3 | P = VI; high V → low I; P_lost = I²R | OK | — | 8464 6.2.4.1, 6.2.4.3 |
| C14 | theory 3 | 100 MW at 1000 V: I = 100,000 A ✓; at 1,000,000 V: I = 100 A ✓; "P_loss = 100² × R (10,000 times less)" | **WRONG** | Current falls by 1000×, so the loss falls by 1000² = **1,000,000×** (100,000² ÷ 100² = 10¹⁰ ÷ 10⁴ = 10⁶). "10,000 times less" is wrong. | F1 |
| C15 | theory 3 | eddy currents, laminated core, flux leakage, thick copper; 95–99 % efficient | OFF-SPEC | Spec: "Knowledge of laminations and eddy currents in the core is not required." Omit. | F2 |
| C16 | `higher` | turns ratio; power conservation; why high-voltage transmission; "calculate power losses at different voltages" | OK | Loss calculation uses base equations (P = VI, P = I²R), both on both sheets. | 4.7.3.4; 6.2.4.1 |
| C17 | common_mistake | ac only; step-up raises V, lowers I; grid high V reduces I²R loss | OK | — | 4.7.3.4; 6.2.4.3 |
| C18 | key_note | as above; "~400 kV" | OK | — | — |
| C19 | equations | "Vₛ/Vₚ = Nₛ/Nₚ"; "Vₚ × Iₚ = Vₛ × Iₛ" | OK | Both on the 8463 June 2026 sheet (HT). Only Vp Ip = Vs Is is on the 8464 sheet (HT). | sheets |
| C20 | variables | Vp, Vs (V); Np, Ns (no unit) | OK | Ip, Is (A) not listed — add if Design shows the power equation. | — |
| C21 | FIFA | 200 → 800 turns, 230 V: Vs = 230 × 4 = 920 V, step-up | OK | ✓ | 4.7.3.4 |
| C22 | CFIFA Convert line | "Nothing to convert — turns are dimensionless counts (nothing to convert at all) and the input voltage is already in volts, so …" | OK, tightened | Correct; repeats itself. Corrected line in the source file. | CFIFA amendment |
| C23 | q1 key | dc → constant field → no change → no induced pd in secondary | OK | — | 4.7.3.4 |
| C24 | q1 opt 1 / wx1 | dc not "too powerful"; constant field causes no induction | OK | Aligned. | — |
| C25 | q1 opt 2 / wx2 | dc flows through coils fine | OK | Aligned. | — |
| C26 | q1 opt 3 / wx3 | 0 Hz true, but the reason is no change | OK | Aligned. | — |
| C27 | q2 key | high V → low I for same power → less heat loss, P_loss = I²R | OK | — | 8464 6.2.4.3 |
| C28 | q2 opt 1 / wx1 | speed of transmission not voltage-dependent; "signals travel at nearly the speed of light" | OK | Acceptable at GCSE. Aligned. | — |
| C29 | q2 opt 2 / wx2 | radiation not the reason | OK | Aligned. | — |
| C30 | q2 opt 3 / wx3 | transformers work at any voltage | OK | Aligned. | — |
| C31 | matching (to be replaced) | four pairs | OK | — | — |

Count: **1 WRONG** (C14, theory — re-cuttable). IMPRECISE: C3, C4. OFF-SPEC: C15. All 6 calculations rechecked; 5 ✓, 1 wrong (C14).

## 4. Frozen items wrong for their route
None. q1 (triple-higher) and q2 (base) both correct and **usable on TH**. FIFA usable.

## 5. Route note
Vp Ip = Vs Is is **higher**, not triple-higher: Combined Higher is examined on it (8464 6.2.4.3 HT, 8464 sheet). This page stays TH (the rest is physics-only HT); Combined Higher must meet the equation on `national-grid`. Seen in passing: the site's CH/TF `national-grid` data carries the **turns-ratio** equation (8463 4.7.3.4, triple-higher — not on the 8464 sheet, and 8464 says "detailed knowledge of the structure of a transformer is not required") — for whoever examines `national-grid` (TRANSFORMERS-F6).

## 6. Verdict
SOURCE HAS ERRORS — one: the National Grid example's "10,000 times less" should be 1,000,000 times (theory, re-cuttable). Otherwise correct; both quiz items and the FIFA usable. Eddy currents/laminations must go (the spec excludes them). The spec's chained calculation (turns → p.d. → current) has no worked example yet.

**For Mide:** nothing.
