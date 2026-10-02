# Examination — The National Grid (national-grid) — AQA 8464 6.2.4.3 / 8463 4.2.4.3
Verdict: SOURCE OK WITH FLAGS (no WRONG item; the transformer turns-ratio content is triple-higher and is served to all four routes; the Combined Higher equation VpIp = VsIs is missing)
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-15/04-checked-science-source/physics-6.2.4.3-national-grid.md`.
Spec sources read: `AQA-8464-spec.txt` (v1.1, 04 Oct 2019) §6.2.4.1, §6.2.4.3; `AQA-8463-spec.txt` (v1.1, 30 Sep 2019) §4.2.4.1, §4.2.4.3, §4.7.3.4; June 2026 equation sheets `8464-equation-sheet.txt`, `8463-equation-sheet-Jun26.txt`. Route audit `physics.md` row `national-grid`; `site-routes.tsv` (`transformers` = 6.7.3.4, TH, is a separate site lesson).

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n (option 0 is the key on both items). All four route copies identical.

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 | **6.2.4.3** | The National Grid | base; one **HT only** statement (VpIp = VsIs) |
| 8463 | **4.2.4.3** | The National Grid | base (no HT statement; transformers are cross-referenced to 4.7.3.4) |
| 8463 | 4.7.3.4 | Transformers | **(physics only) (HT only)** |
| Supporting | 8464 6.2.4.1 / 8463 4.2.4.1 | Power (P = VI, P = I²R) | base |

Spec statements (verbatim, 8464 = 8463 except where marked): "The National Grid is a system of cables and transformers linking power stations to consumers." "Electrical power is transferred from power stations to consumers using the National Grid." "Step-up transformers are used to increase the potential difference from the power station to the transmission cables then step-down transformers are used to decrease, to a much lower value, the potential difference for domestic use." "Students should be able to explain why the National Grid system is an efficient way to transfer energy." 8464 only: "Detailed knowledge of the structure of a transformer is not required." 8464 only: "Higher tier only: Students should be able to select and use the equation: potential difference across primary coil x current in primary coil = potential difference across secondary coil x current in secondary coil as given on the equation sheet."

8463 4.7.3.4 (physics only, HT only): "A basic transformer consists of a primary coil and a secondary coil wound on an iron core." "The ratio of the potential differences across the primary and secondary coils of a transformer Vp and Vs depends on the ratio of the number of turns on each coil, np and ns." Vp/Vs = np/ns — "apply this equation which is given on the Physics equation sheet." "In a step-up transformer Vs > Vp. In a step-down transformer Vs < Vp." Vs × Is = Vp × Ip — given on the sheet. Students should be able to "calculate the current drawn from the input supply to provide a particular power output" and "apply the equation linking the p.d.s and number of turns … to the currents and the power transfer involved, and relate these to the advantages of power transmission at high potential differences."

Equation sheets (June 2026): P = VI, P = I²R — both sheets, base. VpIp = VsIs — both sheets, **HT**. Vp/Vs = np/ns — 8463 sheet only, **HT**; absent from 8464.

## 2. Route table
| # | teachable point | true layer | spec | verdict |
|---|---|---|---|---|
| R1 | Grid = cables + transformers, power station → consumer; path (theory 1; key_note) | base | 6.2.4.3 / 4.2.4.3 | OK |
| R2 | Step-up at power station, step-down to 230 V for homes (theory 1, 3; key_note) | base | 6.2.4.3 / 4.2.4.3 | OK |
| R3 | Transmission p.d. values (theory 1) | base (context) | — | OK; minor (C3) |
| R4 | Why high p.d. is efficient: same P → lower I → less I²R heating (theory 2; common_mistake; key_note; q1) | base | 6.2.4.3 + 6.2.4.1 / 4.2.4.3 + 4.2.4.1 | OK |
| R5 | Worked loss example: I = P/V, then P_lost = I²R (theory 2) | base | 6.2.4.1; 6.2.4.3 | IMPRECISE (C6) |
| R6 | P_lost = I²R (equations[1]) | base | 6.2.4.1 | OK |
| R7 | Transformers work on ac only (theory 3; common_mistake; key_note) | **triple-higher** | 8463 4.7.3.4 | OK science; ROUTE (NATIONAL-GRID-F1) |
| R8 | Step-up decreases current, step-down increases it (theory 3) | base as a consequence of P = VI; the quantitative form is HT | 6.2.4.1; 6.2.4.3 HT | OK |
| R9 | Step-up: more secondary turns; step-down: fewer (key_note) | **triple-higher** | 8463 4.7.3.4 | ROUTE (NATIONAL-GRID-F1) |
| R10 | Vp/Vs = np/ns + example (theory 3; equations[0]; variables np, ns) | **triple-higher** | 8463 4.7.3.4 | ROUTE (NATIONAL-GRID-F1) |
| R11 | FIFA (turns-ratio, 230 kV → 11.5 kV) | **triple-higher** | 8463 4.7.3.4 | OK; ROUTE (NATIONAL-GRID-F1) |
| R12 | q1 (why high voltage) | base | 6.2.4.3 | OK; usable all four routes |
| R13 | q2 (turns-ratio calculation) | **triple-higher** | 8463 4.7.3.4 | OK; usable TH only |
| R14 | VpIp = VsIs | **higher** (8464 6.2.4.3 HT; 8463 4.7.3.4 HT) | — | **MISSING** (NATIONAL-GRID-F2) |
| — | RP, `higher` | none in source | — | No RP is correct. No `higher` field, yet the lesson has HT content (R14) and TH content (R7, R9–R11, R13) |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | theory 1 | Grid = network of cables and transformers, power stations to consumers | OK | Spec wording. | 6.2.4.3 |
| C2 | theory 1 | path: stations → step-up → HV cables → step-down → homes (230 V) | OK | — | 6.2.4.3; 6.2.3.2 (230 V) |
| C3 | theory 1 | "very high voltages (132 kV to 400 kV)" | OK (minor) | The GB transmission network runs at 275 kV and 400 kV (132 kV is transmission only in Scotland). "Up to 400 kV" is safer. Not examined. | — |
| C4 | theory 2 | same P: high V → low I → less I²R heating → less energy wasted | OK | The spec's "efficient" explanation. | 6.2.4.1; 6.2.4.3 |
| C5 | theory 2 | P_lost ∝ I²; halving I cuts losses by ¾ | OK | (½)² = ¼, so a reduction of ¾ ✓ | 6.2.4.1 |
| C6 | theory 2 | 1 MW at 1000 V through 10 Ω: I = 1000 A, P_lost = 10 MW "(more than transmitted!)" | IMPRECISE | Arithmetic ✓ (1000² × 10 = 10⁷ W), but the scenario is physically impossible: a cable cannot waste more power than is sent. It teaches "the numbers break", not "the loss is a big fraction". Use 1 MW at 10 000 V: I = 100 A, loss = 100² × 10 = 100 000 W (10 %); at 100 000 V: I = 10 A, loss = 1000 W (0.1 %). See NATIONAL-GRID-F3. | 6.2.4.1 |
| C7 | theory 2 | 1 MW at 100 000 V: I = 10 A; P_lost = 10² × 10 = 1000 W | OK | ✓ | — |
| C8 | theory 3; common_mistake | transformers change the p.d. of ac only; dc gives no output | OK | Correct (no changing field with steady dc). Triple-higher content. | 8463 4.7.3.4 |
| C9 | theory 3 | step-up raises V (lowers I) at power stations; step-down lowers V (raises I) at substations | OK | — | 6.2.4.3; 4.7.3.4 |
| C10 | theory 3; equations[0] | Vp ÷ Vs = np ÷ ns | OK | 8463 sheet, HT. Not in 8464. | 8463 4.7.3.4 |
| C11 | theory 3 | 500 : 50 turns, Vp = 10 000 V → Vs = 10 000 × (50 ÷ 500) = 1000 V, step-down | OK | ✓ | — |
| C12 | equations[1] | P_lost = I² × R | OK | P = I²R, both sheets. | 6.2.4.1 |
| C13 | key_note | step-up: more secondary turns; step-down: fewer | OK | Triple-higher. | 4.7.3.4 |
| C14 | variables | Vp, Vs (V); np, ns (no unit); I (A); P (W) | OK | R (Ω) is used in theory 2 and equations[1] but not listed — minor. | — |
| C15 | FIFA | 2000 : 100 turns, Vp = 230 000 V: Vs = 230 000 × 0.05 = 11 500 V | OK | ✓. Step-down ✓. | 4.7.3.4 |
| C16 | CFIFA Convert | "Nothing to convert — turns … dimensionless ratio and Vp is already … volts" | OK | Correct. Marked examined ✓. | CFIFA amendment |
| C17 | q1 key | high V → lower I for same P → far less I²R heating | OK | — | 6.2.4.3 |
| C18 | q1 wx1 | P = IV; same P, high V means low I | OK | Aligned with option 1. | 6.2.4.1 |
| C19 | q1 wx2 | cable design is mechanical/safety; efficiency set by current | OK | Aligned. | — |
| C20 | q1 wx3 | voltage has no effect on corrosion | OK | Aligned. | — |
| C21 | q2 key | 4000 : 200 turns, Vp = 20 000 V → Vs = 1000 V | OK | 200/4000 = 0.05 ✓; × 20 000 = 1000 ✓ | 4.7.3.4 |
| C22 | q2 opt 1 / wx1 | 400 000 V = 20 000 × (4000/200), inverted ratio | OK | 20 000 × 20 = 400 000 ✓. wx1 aligned. | — |
| C23 | q2 opt 2 / wx2 | 100 V, ratio error | OK | Aligned (a power-of-ten slip). | — |
| C24 | q2 opt 3 / wx3 | 20 000 V, unchanged | OK | Aligned. | — |
| C25 | matching (to be replaced) | ~400 kV; pylons/underground; 230 V; reduces I → I²R | OK | — | — |

Count: **0 WRONG**; IMPRECISE: C6 (theory, re-cuttable). All arithmetic ✓ (7 calculations rechecked).

Chained calculations (rule 3): theory 2 chains two equations — Step 1 I = P ÷ V (P = VI), Step 2 P_lost = I²R. Base. It needs its own Step 1 … Step 2 worked example, with a Convert step (MW → W, kV → V). The extraction notes said this batch has no chaining; that is true of the FIFAs only, not of this theory example. Triple Higher also has a chain: Step 1 Vs from the turns ratio, Step 2 Is from VpIp = VsIs (or Ip = P_out ÷ Vp, the spec's "current drawn from the input supply").

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| q2 | Correct, but triple-higher (turns ratio, 8463 4.7.3.4 HT). | Use on TH only. |
| FIFA | Correct, but triple-higher. | TH layer only. CF/CH/TF need a base worked example (the I = P/V → I²R chain) and CH needs a VpIp = VsIs example (NATIONAL-GRID-F2). |

## 5. Verdict
SOURCE OK WITH FLAGS. All science and arithmetic correct. The turns-ratio equation, its FIFA and q2 are triple-higher and are served to every route (the site also has a separate TH `transformers` lesson). The Combined Higher equation VpIp = VsIs (8464 6.2.4.3 HT) is missing. The 1 MW / 1000 V loss example is arithmetically right and physically impossible. Spec core added to the source for VpIp = VsIs.

**For Mide:** nothing. All points are settled by the spec.
