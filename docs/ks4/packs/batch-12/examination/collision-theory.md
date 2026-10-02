# Examination — Collision Theory and Activation Energy (collision-theory) — AQA 8464 5.6.1.3 / 8462 4.6.1.3
Verdict: SOURCE OK WITH FLAGS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-12/04-checked-science-source/chemistry-5.6.1.3-collision-theory.md`.
Spec sources read as text: `AQA-8464-spec.txt` (v1.1) 5.6.1.2, 5.6.1.3, 5.6.1.4; `AQA-8462-spec.txt` (v1.1) 4.6.1.2, 4.6.1.3, 4.6.1.4 (wording identical; layout only differs). No equation sheet applies. Route audit read: `ks4-routes/docs/ks4/route-audit/chemistry.md` row `collision-theory` (CF CH TF TH, base, OK).

Conventions: q1–q2 quiz items; wx n = `wrong_explanations` key n (keys index `opts`, 0-based; option 0 is the key on both items); th1–th3 theory chunks. Every route copy of `higher` is `null`; the TH `higher` text is served on CH and TH.

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 / 8462 | **5.6.1.3 / 4.6.1.3** | Collision theory and activation energy | base |
| 8464 / 8462 | 5.6.1.2 / 4.6.1.2 | Factors which affect the rates of chemical reactions (prerequisite) | base |
| 8464 / 8462 | 5.6.1.4 / 4.6.1.4 | Catalysts (forward link) | base |

Spec statements (verbatim, 8464 = 8462): "Collision theory explains how various factors affect rates of reactions. According to this theory, chemical reactions can occur only when reacting particles collide with each other and with sufficient energy. The minimum amount of energy that particles must have to react is called the activation energy. Increasing the concentration of reactants in solution, the pressure of reacting gases, and the surface area of solid reactants increases the frequency of collisions and so increases the rate of reaction. Increasing the temperature increases the frequency of collisions and makes the collisions more energetic, and so increases the rate of reaction. Students should be able to: predict and explain using collision theory the effects of changing conditions of concentration, pressure and temperature on the rate of a reaction; predict and explain the effects of changes in the size of pieces of a reacting solid in terms of surface area to volume ratio [MS 5c]; use simple ideas about proportionality when using collision theory to explain the effect of a factor on the rate of a reaction [MS 1c]." WS 1.2.

There is **no (HT only) and no (chemistry only) content** in 5.6.1.3.

## 2. Route table
| # | teachable point (pack location) | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Reaction needs collision with energy ≥ Ea; most collisions unsuccessful (th1; key_note; q1) | base | 5.6.1.3 | all four | OK |
| R2 | Correct orientation as a third condition (th1; th3; key_note) | not in spec (A-level) | — | all four | OFF-SPEC (COLLISION-THEORY-F4) |
| R3 | Temperature: more frequent AND more energetic collisions (th1; common_mistake) | base | 5.6.1.3 | all four | OK |
| R4 | Concentration, surface area → more frequent collisions (th1; common_mistake) | base | 5.6.1.3 | all four | OK |
| R5 | Pressure of reacting gases → more frequent collisions (th3 only, as "industrial") | base | 5.6.1.3 | all four | GAP — not in th1's factor list (F5) |
| R6 | Activation energy = minimum energy; petrol + spark; high Ea slow, low Ea fast (th2; key_note; variables; q2) | base | 5.6.1.3 | all four | OK |
| R7 | Boltzmann distribution; "10 °C rise" (th2) | not in spec (A-level) | — | all four | OFF-SPEC (F3) |
| R8 | Catalyst lowers Ea (th3; common_mistake; key_note) | base | 5.6.1.4 | all four | OK (forward link) |
| R9 | Size of pieces → surface area to volume ratio (MS 5c) | base | 5.6.1.3 | **absent** | GAP (F5) |
| R10 | Proportionality (e.g. double concentration → double collision frequency) (MS 1c) | base | 5.6.1.3 | **absent** | GAP (F5) |
| R11 | `higher`: Maxwell–Boltzmann curve, "10 °C doubles rate", frequency vs successful proportion | frequency-vs-energy = base; the rest not in spec | 5.6.1.3 | CH TH | WRONG + ROUTE (F1, F2) |
| R12 | quiz q1 | base | 5.6.1.3 | all four | key OK; wx1–wx3 IMPRECISE (F6) |
| R13 | quiz q2 | base | 5.6.1.3 | all four | OK (wx2 minor, F7) |
| — | RP, equations, FIFA | none | — | — | correct: RP 11 (Combined) / RP 5 (Chemistry) belongs to 5.6.1.2, served on `factors-affecting-rate` |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | th1 | reaction needs collision with energy ≥ activation energy | OK | Spec wording. | 5.6.1.3 |
| C2 | th1 | "particles must be in the CORRECT ORIENTATION (for some reactions)" | OFF-SPEC (true) | Not in the AQA statement; never required for marks. | F4 |
| C3 | th1 | most collisions are unsuccessful — not enough energy | OK | — | 5.6.1.3 |
| C4 | th1 | higher T → faster particles → more collisions AND more above Ea | OK | Spec: "increases the frequency of collisions and makes the collisions more energetic". | 5.6.1.3 |
| C5 | th1 | higher concentration → more particles per volume → more collisions | OK | Say "more frequent collisions" (spec word is frequency). | 5.6.1.3 |
| C6 | th1 | larger surface area → more exposed particles → more collisions | OK | — | 5.6.1.3 |
| C7 | th2 | Ea = minimum energy colliding particles must have to react | OK | Spec definition. | 5.6.1.3 |
| C8 | th2 | exothermic reactions still need Ea; energy to break bonds first | OK | — | 5.5.1.2 |
| C9 | th2 | petrol stable at room temperature; spark supplies Ea | OK | — | — |
| C10 | th2 | low Ea → many particles have enough energy → fast; high Ea → slow | OK | — | 5.6.1.3 |
| C11 | th2 | Boltzmann distribution; "even a 10 °C rise significantly increases the proportion above Ea" | OFF-SPEC | Qualitatively true; A-level (7405 kinetics). Replace with the spec's "collisions are more energetic". | F3 |
| C12 | th3 | A-B + C orientation example | OFF-SPEC | As C2. | F4 |
| C13 | th3 | industrial: high T costs energy; catalyst lowers Ea; high pressure → more collisions; concentration → more collisions | OK | Pressure belongs in the main factor list, not only here. | F5 |
| C14 | `higher` | "temperature increases the curve height and shifts it right" | **WRONG** | Raising temperature makes the peak **lower** and moves it right; the area (number of particles) is unchanged. Off-spec anyway. | F1 |
| C15 | `higher` | "a 10 °C rise approximately doubles rate — the fraction of particles above Ea at least doubles" | OFF-SPEC; IMPRECISE | A rule of thumb that holds only for some reactions near room temperature; "at least doubles" is unsupported. | F2 |
| C16 | `higher` | distinguish frequency of collisions from proportion of successful collisions | OK — but **base** | This is the spec's own base distinction (frequency vs more energetic). | F2 |
| C17 | common_mistake | concentration/SA raise frequency, not Ea; only a catalyst changes Ea (pathway); T raises frequency AND proportion ≥ Ea | OK | "Changes Ea" — strictly, a catalyst provides a different pathway with lower Ea (5.6.1.4); fine at GCSE. | 5.6.1.3; 5.6.1.4 |
| C18 | key_note | collision + energy ≥ Ea + orientation; Ea definition; T; catalyst lowers Ea | OK except orientation (F4) | — | 5.6.1.3 |
| C19 | variables | Ea, activation energy, kJ/mol | OK | — | 5.5.1.2 |
| C20 | q1 key (opt 0) | most collisions lack energy ≥ Ea | OK | — | 5.6.1.3 |
| C21 | q1 opt 1 / wx1 | "too fast — bounce off" / "Collision speed doesn't determine success directly — it's whether the ENERGY meets the activation energy threshold." | IMPRECISE | Aligned. But speed IS what gives the collision its energy (spec: hotter → "more energetic" collisions); faster collisions are **more** likely to succeed. Replace. | F6 |
| C22 | q1 opt 2 / wx2 | "only two particles can react" / "Many reactions are bimolecular (two particles) but this isn't why…" | IMPRECISE | Aligned. "Bimolecular" is A-level vocabulary. Replace. | F6 |
| C23 | q1 opt 3 / wx3 | "same type of particle" / "in a mixture, most collisions do involve different reactant species" | IMPRECISE | Aligned. The claim is unsupported — in solution most collisions are with water molecules. Replace. | F6 |
| C24 | q2 key (opt 0) | very high Ea → slow, small proportion of collisions succeed | OK | — | 5.6.1.3 |
| C25 | q2 opt 1 / wx1 | "fast — particles very energetic" / threshold is high, few exceed it | OK | Aligned. | — |
| C26 | q2 opt 2 / wx2 | "exothermic" / "Activation energy and ΔH are independent — high Ea and still endothermic, or low Ea and highly exothermic" | OK (minor) | Aligned. "Independent" is loose (an endothermic reaction's Ea must exceed its ΔH) but nothing a pupil is taught is contradicted. | F7 |
| C27 | q2 opt 3 / wx3 | "will not occur" / high-Ea reactions still occur slowly; temperature can provide the energy; explosives | OK | Aligned. | — |
| C28 | matching (to be replaced) | five pairs | OK | Correct; prints its own answers (to be replaced anyway). | — |

Count: **1 WRONG** (C14, in the `higher` text — not frozen). IMPRECISE frozen: q1 wx1–wx3 (F6). OFF-SPEC: orientation, Boltzmann. No calculation in the source; the spec's SA:V calculation (MS 5c) is missing (F5).

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| q1 | key correct; all three wrong_explanations imprecise (F6) | Do not use as written. Usable on all four routes with wx1–wx3 replaced (wording in F6). |
| q2 | correct | Usable verbatim on all four routes. |

## 5. Verdict
SOURCE OK WITH FLAGS. Core science (collision + sufficient energy, Ea, frequency vs energy) is right. The `higher` field is not Higher content and carries one wrong statement about the distribution curve; there is no HT layer for this lesson. Two spec "should be able to" bullets (SA:V ratio, proportionality) and pressure are missing. Nothing is Mide's call.
