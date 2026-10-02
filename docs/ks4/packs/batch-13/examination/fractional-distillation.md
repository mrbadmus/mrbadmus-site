# Examination — Fractional Distillation of Crude Oil (fractional-distillation) — AQA 8464 5.7.1.2 / 8462 4.7.1.2
Verdict: SOURCE HAS ERRORS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-13/04-checked-science-source/chemistry-5.7.1.2-fractional-distillation.md`.
Spec sources read as text: AQA-8464 (v1.1) §5.7.1.2, 5.7.1.3, 5.2.2.4, 5.9; AQA-8462 (v1.1) §4.7.1.2, 4.7.1.3, 4.2.2.4, 4.9. Route audit `route-audit/chemistry.md` row 79 (base, OK).

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n, read against option n. `higher` CF/TF copies `null` → `higher` served on CH and TH only.

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 | **5.7.1.2** | Fractional distillation and petrochemicals | base |
| 8462 | **4.7.1.2** | Fractional distillation and petrochemicals | base |
| Supporting | 5.7.1.3 / 4.7.1.3 (boiling point, viscosity, flammability vs size); 5.2.2.4 / 4.2.2.4 (intermolecular forces increase with molecule size) | | base |

Spec statements (verbatim, 8464 = 8462): "The many hydrocarbons in crude oil may be separated into fractions, each of which contains molecules with a similar number of carbon atoms, by fractional distillation." "The fractions can be processed to produce fuels and feedstock for the petrochemical industry." "Many of the fuels on which we depend for our modern lifestyle, such as petrol, diesel oil, kerosene, heavy fuel oil and liquefied petroleum gases, are produced from crude oil." "Many useful materials on which modern life depends are produced by the petrochemical industry, such as solvents, lubricants, polymers, detergents." "The vast array of natural and synthetic carbon compounds occur due to the ability of carbon atoms to form families of similar compounds." "Students should be able to explain how fractional distillation works in terms of evaporation and condensation." "Knowledge of the names of other specific fractions or fuels is not required." 5.2.2.4: "The intermolecular forces increase with the size of the molecules, so larger molecules have higher melting and boiling points."

## 2. Route table
| # | teachable point | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Process: heat, evaporate, rise, cool, condense at boiling point (theory 1; key_note) | base | 5.7.1.2 / 4.7.1.2 | all four | OK |
| R2 | Fractions = similar number of C atoms / similar bp; long chains low, short chains high (theory 1; common_mistake) | base | 5.7.1.2 / 4.7.1.2 | all four | OK |
| R3 | Named fractions and uses (theory 2) | base (LPG, petrol, kerosene, diesel oil, heavy fuel oil); naphtha, bitumen, chain ranges and bp ranges: beyond spec | 5.7.1.2 / 4.7.1.2 | all four | IMPRECISE (C6) |
| R4 | Trends: bp ↑, viscosity ↑, flammability ↓ with chain length (theory 3) | base | 5.7.1.3 / 4.7.1.3 | all four | WRONG in one word (C8); IMPRECISE terminology (C7) |
| R5 | Supply/demand → cracking (theory 3) | base | 5.7.1.4 / 4.7.1.4 | all four | OK |
| R6 | q1 (petrol vs diesel level) | base | 5.7.1.2 / 4.7.1.2 | all four | key OK; wx1 WRONG (C14) |
| R7 | q2 (why bitumen has higher bp) | base | 5.7.1.3; 5.2.2.4 | all four | OK |
| R8 | `higher`: London dispersion, electron clouds, temporary dipoles | none (A-level) | — | CH TH | OFF-SPEC (F4) |
| R9 | `higher`: environmental/economic issues of fossil fuels | base | 5.9.2.4, 5.9.3 / 4.9.2.4, 4.9.3 | CH TH | ROUTE (F4) |
| R10 | `higher`: biofuels and alternatives | none | — | CH TH | OFF-SPEC (F4) |
| — | rp, fifas, equations, examiner_tip | none | — | — | correct |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | theory 1 | crude oil heated to ~350 °C, most vaporises | OK | — | — |
| C2 | theory 1 | column hot at bottom, cool at top; vapours cool as they rise | OK | — | 5.7.1.2 |
| C3 | theory 1 | each fraction condenses at its boiling point and is collected | OK | Better: "condenses where the column is cooler than its boiling point". Spec wants "evaporation and condensation" named — it is. | 5.7.1.2 |
| C4 | theory 1 | longer chains condense lower; shorter chains near the top; refinery gases leave as gases | OK | — | — |
| C5 | theory 1 | bitumen does not vaporise, stays at bottom | OK | — | — |
| C6 | theory 2 | fraction table: naphtha "C₅–C₁₀ … bp 75–120 °C" alongside petrol "C₅–C₁₀ … bp 25–75 °C"; kerosene 150–250 °C | IMPRECISE | Naphtha is given the same chain range as petrol but a different bp range, and 120–150 °C is missing — internally inconsistent. Chain and bp ranges vary between textbooks and are **not required** ("Knowledge of the names of other specific fractions or fuels is not required"). Design: show the order and the trend, not number ranges; drop naphtha or give it no numbers. | 5.7.1.2 |
| C7 | theory 3; `higher` | "London dispersion forces (intermolecular)" | IMPRECISE | A-level term. AQA GCSE wording is "intermolecular forces" / "forces between molecules", which "increase with the size of the molecules". | 5.2.2.4 |
| C8 | theory 3 | "VISCOSITY INCREASES (gets thicker/runnier)" | WRONG | Higher viscosity = thicker, **less** runny. Re-cut: "gets thicker — flows less easily". | 5.7.1.3 |
| C9 | theory 3 | flammability decreases; shorter chains more volatile | OK | — | 5.7.1.3 |
| C10 | theory 3 | colour darker down the column | OK | Beyond spec. | — |
| C11 | theory 3 | demand for petrol/diesel exceeds supply; cracking converts larger to smaller | OK | — | 5.7.1.4 |
| C12 | common_mistake | short chains low bp, top; long chains high bp, bottom | OK | — | 5.7.1.2 |
| C13 | key_note | as theory | OK | Lists naphtha (beyond spec; harmless). | — |
| C14 | q1 wx1 ↔ opt 1 ("more dense") | "Density does affect placement somewhat, but the key factor is BOILING POINT" | WRONG | Aligned ✓, but the first clause is false: where a fraction condenses is set only by its boiling point against the column temperature gradient — density plays no part (and petrol is the *less* dense). The explanation affirms the misconception it should kill. Do not use q1 as written. | 5.7.1.2 |
| C15 | q1 key | petrol higher — shorter chains, lower bp | OK | — | — |
| C16 | q1 wx2 ↔ opt 2 (same level) | C₅–C₁₀ vs C₁₅–C₂₅, different levels | OK | Aligned ✓ | — |
| C17 | q1 wx3 ↔ opt 3 (bottom with bitumen) | bitumen at bottom; petrol higher | OK | Aligned ✓ ("much lighter" loose but not false) | — |
| C18 | q2 key | longer chains → stronger intermolecular forces → more energy | OK | Exactly 5.2.2.4. | 5.2.2.4 |
| C19 | q2 wx1 ↔ opt 1 (more oxygen) | fractions are hydrocarbons, no oxygen | OK | Aligned ✓ (GCSE idealisation; spec "H and C only") | 5.7.1.1 |
| C20 | q2 wx2 ↔ opt 2 (denser) | cause is chain length and IMF, not density | OK | Aligned ✓ | — |
| C21 | q2 wx3 ↔ opt 3 (petrol double bonds) | alkanes single bonds only | OK | Aligned ✓ | 5.7.1.1 |
| C22 | matching (to be replaced) | chain ranges and uses | OK | Ranges as C6 caveat. | — |

No `[NEW — to be examined]` Convert lines in this file. Count: **2 WRONG** (C8 theory, re-cuttable; C14 frozen wx → q1 not usable as written); IMPRECISE C6, C7.

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| q1 | wx1 states density "does affect placement somewhat" — false | Do not use as written (F2). |
| q2 | — | Usable on all four routes. |

## 5. Verdict
SOURCE HAS ERRORS. One wrong word in theory ("thicker/runnier", re-cuttable) and one wrong frozen wrong-explanation (q1 wx1, density). Fraction number ranges inconsistent and not required. `higher` is A-level and off-spec content. Nothing for Mide.
