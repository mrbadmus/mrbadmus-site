# Examination — Current, Resistance and Potential Difference (current-resistance-pd) — AQA 8464 6.2.1.3 / 8463 4.2.1.3
Verdict: SOURCE HAS ERRORS (q1's fourth option has wrong working; the `rp` line names the wrong practical and mislabels its number)
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-15/04-checked-science-source/physics-6.2.1.3-current-resistance-pd.md`.
Spec sources read: `AQA-8464-spec.txt` §6.2.1.3, §6.2.1.4, §6.2.2, RP15 (§10.2.15); `AQA-8463-spec.txt` §4.2.1.3, RP3 (§8.2.3). Equation sheets read: `8464-equation-sheet.txt` (June 2026), `8463-equation-sheet-Jun26.txt`. Route audit: `ks4-routes/docs/ks4/route-audit/physics.md` row `current-resistance-pd` (base / base). Pilot neighbours read: `design-reference/pilot/.../src/physics-6.2.1.4-resistors.md`, `physics-6.2.2-series-parallel-circuits.md` and both built `.dc.html` pages.

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n (option 0 is the key on both items). All four route copies identical.

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 | **6.2.1.3** | Current, resistance and potential difference | base; RP15 sited here |
| 8463 | **4.2.1.3** | Current, resistance and potential difference | base; RP3 sited here |
| Neighbour (pilot `resistors`) | 8464 6.2.1.4 / 8463 4.2.1.4 | Resistors (ohmic conductors, I–V graphs, RP16 / RP4) | base |
| Neighbour (pilot `series-parallel-circuits`) | 8464 6.2.2 / 8463 4.2.2 | Series and parallel circuits | base |

Spec statements (verbatim, 8463 = 8464): "The current (I) through a component depends on both the resistance (R) of the component and the potential difference (V) across the component. The greater the resistance of the component the smaller the current for a given potential difference (pd) across the component." "Questions will be set using the term potential difference. Students will gain credit for the correct use of either potential difference or voltage." "potential difference = current × resistance  V = I R" — "Students should be able to recall and apply this equation." Units V, A, Ω.

Required practical (verbatim, 8464 RP15 = 8463 RP3): "use circuit diagrams to set up and check appropriate circuits to investigate the factors affecting the resistance of electrical circuits. This should include: • the length of a wire at constant temperature • combinations of resistors in series and parallel." AT 1, 6, 7.

Equation sheets (June 2026): V = I R printed on **both** the 8464 and the 8463 sheet → "On the sheet" on all four routes.

## 2. Route table
| # | teachable point | true layer | spec | verdict |
|---|---|---|---|---|
| R1 | pd = energy per unit charge, 1 V = 1 J/C (theory 1) | base | 6.2.4.2 (E = QV) | OK (supporting; not a 6.2.1.3 statement) |
| R2 | Resistance opposes current; unit Ω (theory 1) | base | 6.2.1.3 | OK |
| R3 | V = IR and rearrangements; greater R → smaller I for given V (theory 1; equations; variables; key_note; common_mistake) | base | 6.2.1.3 | OK |
| R4 | Ohmic conductor, I ∝ V, straight I–V line, gradient (theory 2; q2) | base | **6.2.1.4** | OK — belongs to pilot `resistors`; recap only |
| R5 | Measuring R: ammeter in series, voltmeter in parallel, R = V/I (theory 2) | base | 6.2.1.4 ("explain the design and use of a circuit to measure the resistance of a component"); RP15 | OK |
| R6 | Series pd splits, parallel pd same; series worked example (theory 3; key_note) | base | **6.2.2** | OK — belongs to pilot `series-parallel-circuits`; recap only |
| R7 | FIFA: R = 12 ÷ 0.4 = 30 Ω | base | 6.2.1.3 | OK |
| R8 | `rp` line | base | RP15 (8464) / RP3 (8463) | **WRONG** (CRP-F2) |
| R9 | q1 V = 3 × 6 | base | 6.2.1.3 | key OK; option 4 **WRONG** (CRP-F1) |
| R10 | q2 I–V gradient | base | 6.2.1.4 | OK, usable all routes (neighbour content) |
| — | `higher` | none | — | correct: 6.2.1.3 has no HT and no physics-only content |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | theory 1 | pd (voltage) = energy transferred per unit charge; 1 V = 1 J/C | OK | Follows from E = QV. | 6.2.4.2 |
| C2 | theory 1 | resistance = opposition to current; ohm | OK | GCSE-level definition. | 6.2.1.3 |
| C3 | theory 1; equations; variables | V = I × R; I = V ÷ R; R = V ÷ I; V, A, Ω | OK | — | 6.2.1.3 |
| C4 | theory 1 | higher R → lower I for a given pd; higher pd → higher I for given R | OK | Spec wording. | 6.2.1.3 |
| C5 | theory 2 | ohmic conductor (resistor at constant temperature): I ∝ V, R constant | OK | — | 6.2.1.4 |
| C6 | theory 2 | straight line through origin; steeper = lower resistance | OK | True with I on the y-axis (the standard I–V layout). | 6.2.1.4 |
| C7 | theory 2 | ammeter in series, voltmeter in parallel; 6 V, 2 A → 3 Ω | OK | 6 ÷ 2 = 3 ✓ | 6.2.1.4 |
| C8 | theory 3 | series pd splits, sum = supply; larger R takes larger share; parallel pd same | OK | — | 6.2.2 |
| C9 | theory 3 | 12 V; 4 Ω + 8 Ω = 12 Ω; I = 1 A; V₁ = 4 V, V₂ = 8 V | OK | All ✓. A three-step chain (see brief). | 6.2.2 |
| C10 | common_mistake | R = V ÷ I not V × I; "voltage" acceptable but precise term is pd | OK | Spec credits either term. | 6.2.1.3 |
| C11 | key_note | as above | OK | — | — |
| C12 | FIFA | 12 V, 0.4 A → R = 30 Ω | OK | 12 ÷ 0.4 = 30 ✓ | 6.2.1.3 |
| C13 | CFIFA Convert `[NEW]` | "Nothing to convert — V and I are both already given in SI units (volts, amps)." | OK | Examined ✓. A second worked example should carry mA → A (e.g. 250 mA = 0.25 A). | CFIFA amendment |
| C14 | rp | "RP15 (Physics) — Measure V and I for different components; calculate resistance using R = V/I." | **WRONG** | RP15 is the **Combined** number; the separate-Physics number is **RP3**. The activity described (V and I for different components) is the I–V practical (RP16 / Physics RP4), owned by the pilot `resistors`. The practical sited at 6.2.1.3 is "factors affecting the resistance of electrical circuits": length of a wire at constant temperature; combinations of resistors in series and parallel. | 8464 RP15; 8463 RP3 |
| C15 | q1 key | 6 Ω, 3 A → V = 18 V | OK | ✓ | 6.2.1.3 |
| C16 | q1 opt 2 / wx1 | "2 V — V = R ÷ I = 6 ÷ 3" / "R ÷ I gives Ω/A — not volts" | OK | Aligned; 6 ÷ 3 = 2 ✓ | — |
| C17 | q1 opt 3 / wx2 | "0.5 V — V = I ÷ R = 3 ÷ 6" / "I ÷ R gives A/Ω — not volts" | OK | Aligned; 3 ÷ 6 = 0.5 ✓ | — |
| C18 | q1 opt 4 / wx3 | "9 V — V = (I + R) / 2" / "There is no averaging formula in Ohm's Law." | **WRONG** | Aligned, but the option's own working is false: (3 + 6) ÷ 2 = **4.5**, not 9. The 9 V error is I + R = 3 + 6. Do not use as written. | — |
| C19 | q2 key | steeper I–V gradient = lower resistance | OK | — | 6.2.1.4 |
| C20 | q2 opt 2 / wx1 | "Higher resistance — steeper means more opposition" / "steeper … LOWER resistance" | OK | Aligned. | 6.2.1.4 |
| C21 | q2 opt 3 / wx2 | "Higher pd — the axes are swapped" / "On a standard I–V graph (I on y-axis…)" | OK | Aligned. | 6.2.1.4 |
| C22 | q2 opt 4 / wx3 | "Non-ohmic — only curved graphs are ohmic" / "Ohmic conductors produce straight-line I–V graphs" | OK | Aligned. | 6.2.1.4 |
| C23 | matching (to be replaced) | 12 ÷ 2 = 6 Ω; 3 ÷ 6 = 0.5 A; 3 × 3 = 9 V; pd doubles → I doubles | OK | All ✓ | — |
| C24 | coverage | RP15/RP3 method and analysis | GAP | Not in the frozen data at all (CRP-F3). Spec core added to the source file. | RP15 / RP3 |

Count: **2 WRONG** (C14 `rp`, C18 q1 opt 4). All arithmetic ✓ (9 calculations rechecked).

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| q1 | option 4's working is false ((3 + 6) ÷ 2 = 4.5) | Do not use as written. Usable once Design rewrites option 4 as "9 V — V = I + R = 3 + 6" (wx: "Adding a current to a resistance has no meaning; V = I × R"). |
| `rp` | wrong practical, wrong separate-science number | Do not use as written. Use the spec RP text (source file's "Spec core missing" section). |
| q2 | correct; base | Usable on all four routes; it is `resistors` content — Design may leave it to that lesson. |

## 5. For the lesson author
**Keep distinct from the pilot.** `resistors` (6.2.1.4) owns ohmic/non-ohmic components, I–V graphs and RP16/RP4. `series-parallel-circuits` (6.2.2) owns the series/parallel current and pd rules and R_total = R1 + R2; its built page does **not** teach the RP. This lesson owns: V = IR, "greater R → smaller I", and RP15/RP3 (wire length + resistors in series/parallel). Theory 2 and theory 3 are recap at most.

**Misconceptions seen in AQA marking:** R = V × I; current "used up" by a resistor; voltmeter in series; length in cm treated as resistance; heating the wire (big current, left on) blamed on nothing; "resistors in parallel add up".

**RP15/RP3 method (examiner summary):** wire taped to a metre rule; crocodile clip moved to set length; ammeter in series, voltmeter across the length of wire in use; low pd / switch off between readings so the wire stays at constant temperature; R = V ÷ I at each length; plot R against length — straight line (through the origin, or a small positive intercept from contact resistance) → R ∝ length. Second part: measure R of two resistors in series (larger than either) and in parallel (smaller than the smaller one).

**Typical questions** ⚑ examiner-drafted
- *Write down the equation that links current, potential difference and resistance. [1]* — V = IR.
- *A 0.20 A current flows through a 15 Ω resistor. Calculate the pd across it. [2]* — 15 × 0.20 (1); 3.0 V (1).
- *Describe how the student should make sure the wire stays at a constant temperature. [1]* — switch off between readings / use a small current.
- *Explain why the line on the R–length graph does not pass through the origin. [2]* — resistance of connections/crocodile clips (1); zero error added to every reading (1).

## 6. Verdict
SOURCE HAS ERRORS. Core science (V = IR) is right and every calculation checks. Two frozen items wrong: q1 option 4's working and the `rp` line. The RP's spec core is missing from the frozen data and has been added. No question for Mide.
