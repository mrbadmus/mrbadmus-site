# Examination — Using Electrolysis to Extract Metals (electrolysis-extraction) — AQA 8464 5.4.3.3 / 8462 4.4.3.3 (+ HT 8464 5.4.3.1, 5.4.3.5 / 8462 4.4.3.1, 4.4.3.5)
Verdict: SOURCE HAS ERRORS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-12/04-checked-science-source/chemistry-5.4.3.3-electrolysis-extraction.md`.
Spec sources read as text: `AQA-8464-spec.txt` (v1.1) 5.4.3.1–5.4.3.5, 5.10.1.4; `AQA-8462-spec.txt` (v1.1) 4.4.3.1–4.4.3.5, 4.10.1.4, 4.10.3.1. No equation sheet applies (chemistry). Route audit row `electrolysis-extraction` (CF CH TF TH, base, OK) read; it did not tag the half equations as HT or the copper/electroplating content as off-spec.

Conventions: q1–q2 quiz items; wx n = `wrong_explanations` key n; th1–th3 theory chunks. CF and TF copies differ only in `higher` (`null`), so `higher` is served on CH TH; every other section is served on all four.

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 / 8462 | **5.4.3.3 / 4.4.3.3** | Using electrolysis to extract metals | base |
| 8464 / 8462 | 5.4.3.1 / 4.4.3.1 | The process of electrolysis (HT para: half equations) | base / **HT only** para |
| 8464 / 8462 | 5.4.3.5 / 4.4.3.5 | Half equations at electrodes | **(HT only)** |
| 8464 / 8462 | 5.10.1.4 / 4.10.1.4 | Alternative methods of extracting metals — "copper can be obtained from solutions of copper compounds … by electrolysis" | **(HT only)** |
| 8462 | 4.10.3.1 | Corrosion and its prevention — electroplating named as a barrier coating | **(chemistry only)** |

Spec statement (verbatim, 8464 = 8462) 5.4.3.3: "Metals can be extracted from molten compounds using electrolysis. Electrolysis is used if the metal is too reactive to be extracted by reduction with carbon or if the metal reacts with carbon. Large amounts of energy are used in the extraction process to melt the compounds and to produce the electrical current. Aluminium is manufactured by the electrolysis of a molten mixture of aluminium oxide and cryolite using carbon as the positive electrode (anode). Students should be able to: • explain why a mixture is used as the electrolyte • explain why the positive electrode must be continually replaced."
5.4.3.1 (HT para): "(HT only) Throughout Section 4.4.3 Higher Tier students should be able to write half equations for the reactions occurring at the electrodes during electrolysis, and may be required to complete and balance supplied half equations."

## 2. Route table
| # | teachable point (pack location) | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Al too reactive for carbon reduction → electrolysis (th1; key_note) | base | 5.4.3.3 | all four | OK; "or if the metal reacts with carbon" missing (EX-F6) |
| R2 | Al₂O₃ in molten cryolite lowers the operating temperature (why a mixture) (th1; key_note) | base | 5.4.3.3 | all four | OK |
| R3 | Graphite cathode lining, graphite anodes; Al at cathode, O₂ at anode (th1; key_note) | base | 5.4.3.3 | all four | OK |
| R4 | Anode burns: C + O₂ → CO₂, so anodes replaced (th1; key_note; q1) | base | 5.4.3.3 | all four | OK |
| R5 | Half equations Al³⁺ + 3e⁻ → Al; 2O²⁻ → O₂ + 4e⁻ (th1; equations 1–2; `higher`) | higher | 5.4.3.1 (HT para); 5.4.3.5 | th1, equations: all four; `higher`: CH TH | ROUTE (EX-F4) |
| R6 | Energy cost of melting + current (`higher` "Evaluate costs and benefits") | base | 5.4.3.3 | CH TH only | ROUTE (EX-F5); not stated in theory (EX-F6) |
| R7 | Copper purification: impure anode, pure cathode, anode sludge (th2; common_mistake; key_note; equations 3–4; `higher`; q2) | off-spec (nearest: copper from solution by electrolysis, HT, 5.10.1.4) | — | all four | OFF-SPEC (EX-F1) |
| R8 | Electroplating (th3; key_note) | off-spec (named only as a corrosion barrier, chemistry only, 4.10.3.1) | — | all four | OFF-SPEC (EX-F2) |
| R9 | quiz q1 (why anode replaced) | base | 5.4.3.3 | all four | OK |
| R10 | quiz q2 (copper purification cathode) | off-spec | — | all four | OFF-SPEC (EX-F1) |
| — | rp, fifas, examiner_tip | none | — | — | correct: 5.4.3.3 has no RP and no calculation |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | th1 | Aluminium is the most abundant metal in the Earth's crust | OK | — | — |
| C2 | th1 | Al cannot be extracted by carbon reduction (above carbon) | OK | Spec gives a second reason — "or if the metal reacts with carbon" — not in source (EX-F6). | 5.4.3.3 |
| C3 | th1 | Al₂O₃ melts at about 2050 °C | OK | Literature ≈ 2072 °C; "about 2050" acceptable. | — |
| C4 | th1 | Cryolite lowers operating temperature to about 950 °C | OK | (≈ 940–980 °C.) Answers "why a mixture" — lower temperature, less energy, lower cost. | 5.4.3.3 |
| C5 | th1 | Cryolite does not react and is recovered — acts as a solvent | OK | — | — |
| C6 | th1 | Steel tank lined with graphite (cathode); graphite anodes | OK | — | 5.4.3.3 |
| C7 | th1 | Al³⁺ + 3e⁻ → Al; molten Al sinks and is tapped off | OK (HT eq) | Balanced ✓. HT only (EX-F4). | 5.4.3.5 |
| C8 | th1 | 2O²⁻ → O₂ + 4e⁻ | OK (HT eq) | Balanced ✓ (charge −4 = −4). | 5.4.3.5 |
| C9 | th1 | C + O₂ → CO₂; anodes burn away, replaced regularly | OK | Answers "why the positive electrode must be continually replaced". | 5.4.3.3 |
| C10 | th2 | Crude copper impurities Zn, Fe, Ag, Au; purified to 99.99 % | OK science / OFF-SPEC | Not on AQA (EX-F1). | 5.10.1.4 (nearest) |
| C11 | th2 | Impure Cu anode dissolves Cu → Cu²⁺ + 2e⁻; Au, Ag, Pt fall as anode sludge; Cu²⁺ + 2e⁻ → Cu at cathode; [Cu²⁺] approx. constant | OK science / OFF-SPEC | All correct; [Cu²⁺] falls slightly (Zn, Fe dissolve instead of Cu) — "approximately" covers it. | — |
| C12 | th3 | Electroplating set-up for Ag on Cu spoon; Ag⁺ + e⁻ → Ag; Ag → Ag⁺ + e⁻; anode loses = cathode gains | OK science / OFF-SPEC | EX-F2. | 4.10.3.1 (named only) |
| C13 | th3 | "zinc plating of steel (galvanising)" | IMPRECISE | AQA's galvanising is a zinc coating giving sacrificial protection (4.10.3.1), usually by hot-dipping — not an electroplating example. | 4.10.3.1 |
| C14 | `higher` | Half equations for Al cell and Cu purification; "Evaluate costs and benefits" | ROUTE / OFF-SPEC | Al half equations HT ✓; Cu off-spec; costs/benefits base (EX-F4, F5). | 5.4.3.3; 5.4.3.5 |
| C15 | common_mistake s1–2 | impure Cu = anode; pure Cu builds on cathode | OK science / OFF-SPEC | EX-F1. | — |
| C16 | common_mistake s3 | "The anions in the electrolyte (SO₄²⁻) do not move to either electrode in copper purification" | WRONG | Every ion in an electrolyte moves when current flows; SO₄²⁻ moves towards the anode — it is simply not discharged (EX-F3). | 5.4.3.1 |
| C17 | key_note | Al: cryolite ~950 °C, graphite electrodes, Al at cathode, O₂ at anode burns graphite anodes | OK | — | 5.4.3.3 |
| C18 | equations 1–4 | as C7, C8, C11 | OK | 1–2 HT; 3–4 off-spec. | 5.4.3.5 |
| C19 | q1 key | O₂ at anode reacts with hot graphite, C + O₂ → CO₂, anode burns away | OK | Mark-scheme answer. | 5.4.3.3 |
| C20 | q1 opt 2 / wx1 | "anode dissolves into the melt" / graphite reacts chemically with O₂, doesn't dissolve | OK, aligned | — | — |
| C21 | q1 opt 3 / wx2 | "high temperature melts graphite" / "Graphite melts at ~3600 °C" | OK, aligned; IMPRECISE (minor) | Graphite sublimes (≈ 3650 °C) at atmospheric pressure rather than melting; the point (far above 950 °C) stands. Usable. | — |
| C22 | q1 opt 4 / wx3 | "Al deposits on the anode" / Al forms at the cathode lining | OK, aligned | — | 5.4.3.3 |
| C23 | q2 key | Cu²⁺ gain electrons, pure Cu deposits at cathode | OK science / OFF-SPEC | EX-F1. | — |
| C24 | q2 wx1–wx3 | opt 2 dissolving = anode; opt 3 O₂ not produced; opt 4 Au/Ag fall as sludge | OK, aligned | Keys 1–3 match options 2–4. | — |
| C25 | matching (to be replaced) | 5 pairs | OK science | Rows 3–5 off-spec. | — |

Count: **1 WRONG** (C16); **OFF-SPEC**: copper purification (th2, q2, eqs 3–4), electroplating (th3); **IMPRECISE**: C13, C21. All equations balanced in atoms and charge.

## 4. Frozen items for their route
| item | usable on | note |
|---|---|---|
| q1 | CF CH TF TH | Base; the spec's own "why replace the anode". |
| q2 | none as a rung | Off-spec (EX-F1). Science and key alignment correct. |

## 5. Verdict
SOURCE HAS ERRORS. The aluminium content — the whole of 5.4.3.3 — is correct and base, with its half equations HT. Two of the three theory chunks (copper purification, electroplating) are not AQA content; one sentence of the common_mistake is wrong. One frozen quiz item is usable on all routes. No item is Mide's call.
