# Examination — Land Use and Peat Bogs (land-use) — AQA 8464 4.7.3.3 / 8461 4.7.3.3
Verdict: SOURCE OK WITH FLAGS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-5/04-checked-science-source/biology-4.7.3.3-land-use.md`.
Spec sources read as text: `AQA-8464-spec.txt` (Combined Trilogy v1.1, 4.7.3.1–4.7.3.6, 4.7.2.2), `AQA-8461-spec.txt` (Biology v1.0, same, plus 4.7.2.3 Decomposition (biology only), 4.7.5.1 food security link). Route audit row `land-use` (OK, CF CH TF TH). Runtime convention checked in `generate_site_v5.py`: `wrong_explanations` key n is shown for `opts[n]` (0-based; key 0 is the answer).

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n, shown for `opts[n]`; T1–T3 = theory blocks. No route copy differs.

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 | **4.7.3.3** | Land use | base |
| 8461 | **4.7.3.3** | Land use | base |
| Supporting | 4.7.3.1 biodiversity (definition); 4.7.3.5 global warming (spec's own link); 8461 4.7.2.3 Decomposition (biology only) — oxygen and decay rate; 8461 4.7.5.1 food security (biology only) — spec's own link | | base / triple context |

Spec statements (verbatim, 8464 = 8461): "Humans reduce the amount of land available for other animals and plants by building, quarrying, farming and dumping waste. The destruction of peat bogs, and other areas of peat to produce garden compost, reduces the area of this habitat and thus the variety of different plant, animal and microorganism species that live there (biodiversity). The decay or burning of the peat releases carbon dioxide into the atmosphere." Skills: "WS 1.4, 1.5 Understand the conflict between the need for cheap available compost to increase food production and the need to conserve peat bogs and peatlands as habitats for biodiversity and to reduce carbon dioxide emissions."

## 2. Route table
| # | teachable point | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Humans reduce land for other species: building, quarrying, farming, dumping waste (T1; key_note) | base | 4.7.3.3 | all four | OK |
| R2 | Habitat lost → biodiversity falls (T1) | base | 4.7.3.3; 4.7.3.1 | all four | OK |
| R3 | What peat is: waterlogged, too little oxygen for decomposers, partly-decayed plants build up, stores carbon (T2) | base (context — explains R5) | 4.7.3.3; decay factors are 8461 4.7.2.3 (biology only) | all four | OK as context; no triple layer needed |
| R4 | Peat bogs are a habitat for specialised plants, animals, microorganisms (T2) | base | 4.7.3.3 | all four | OK |
| R5 | Peat extracted for compost (garden and commercial food production), also burned as fuel (T3; common_mistake) | base | 4.7.3.3 | all four | OK |
| R6 | Destroying peat bogs: habitat area falls → biodiversity falls; decay or burning releases CO₂ (T3; common_mistake; key_note; q1) | base | 4.7.3.3 | all four | OK |
| R7 | Link to global warming (T3) | base | 4.7.3.3 → 4.7.3.5 | all four | OK |
| R8 | Peat-free compost protects bogs (T3; key_note; q2) | base | 4.7.3.3; 4.7.3.6 | all four | OK |
| R9 | Conflict: cheap compost for food production vs conserving bogs and cutting CO₂ (WS 1.4, 1.5) | base | 4.7.3.3 WS | — (only hinted at in T3) | **GAP** (LAND-USE-F3) |
| — | equations, RP, FIFA, `higher` | none | — | — | correct: 4.7.3.3 has no HT, no separate-science content, no RP |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | T1 | building, quarrying, farming, dumping waste reduce land for other species | OK | Spec's four, verbatim in substance. | 4.7.3.3 |
| C2 | T1 | quarrying = digging out rock and minerals; landfill = dumping | OK | — | — |
| C3 | T1 | habitats destroyed → less space for wild species → biodiversity falls | OK | — | 4.7.3.1 |
| C4 | T2 | peat bogs waterlogged; not enough oxygen for decomposers; plants do not fully decay | OK | Acidic conditions also slow decay; not needed. | 8461 4.7.2.3 |
| C5 | T2 | peat builds up over thousands of years; stores a large amount of carbon | OK | — | — |
| C6 | T2 | peat bogs are a habitat for specialised plants, animals and microorganisms | OK | Spec names all three groups. | 4.7.3.3 |
| C7 | T3 | peat sold as compost for gardens and commercial food production; can be burned as fuel | OK | — | 4.7.3.3 |
| C8 | T3 | destroying bogs reduces habitat → biodiversity decreases | OK | — | 4.7.3.3 |
| C9 | T3 | drained peat decays, or burns → stored carbon released as CO₂ → global warming | OK | — | 4.7.3.3; 4.7.3.5 |
| C10 | T3 | peat-free compost helps protect peat bogs | OK | — | — |
| C11 | common_mistake | two harms: biodiversity AND CO₂; peat extracted mainly for compost | OK | "Mainly for compost" is true for the UK and is AQA's framing; peat is a significant fuel elsewhere (Ireland, Finland) — not wrong as written. | 4.7.3.3 |
| C12 | key_note | as above | OK | — | — |
| C13 | q1 stem, options, key | peat stores carbon from partly-decayed plants; decay or burning releases it as CO₂ | OK | Key correct. Option 3 (petrol machines) is true-but-minor; key is clearly the best answer. | 4.7.3.3 |
| C14 | q1 wx1 (shown for "pure carbon dioxide gas") | "Peat is partly-decayed plant material that locked away carbon…" | OK | Rebuts the option. | — |
| C15 | q1 wx2 (shown for "Machines … run on petrol") | "Peat is solid plant material, not CO₂ gas…" | **WRONG (mismatched)** | Answers option 1, not option 2. A pupil who picks "machines" is told peat is not a gas. | — |
| C16 | q1 wx3 (shown for "Peat reflects sunlight") | "The machinery is a minor factor…" | **WRONG (mismatched)** | Answers option 2. Nothing rebuts "reflects sunlight" (peat is dark; reflection is not how it adds CO₂). | — |
| C17 | q2 stem, options, key | peat-free compost best protects peat bog biodiversity | OK | — | 4.7.3.3 |
| C18 | q2 wx1 (shown for "Extracting peat faster") | "If gardeners choose peat-free compost, demand for peat falls…" | IMPRECISE | True, but explains the key rather than rebutting the option chosen. | — |
| C19 | q2 wx2 (shown for "Burning peat instead") | "Extracting peat faster destroys the habitat sooner…" | **WRONG (mismatched)** | Answers option 1. | — |
| C20 | q2 wx3 (shown for "Draining more bogs") | "Burning peat still destroys the bog and releases CO₂." | **WRONG (mismatched)** | Answers option 2. Nothing rebuts "draining more bogs". | — |
| C21 | matching (to be replaced) | three land uses; three consequences of peat destruction | OK | All correct. | 4.7.3.3 |

The q1 and q2 explanations are attached one option late: wx2's text belongs to opt 1, wx3's to opt 2, wx1 explains the key, and opt 3 has no explanation. Stems, options and keys are all correct.

Count: **4 WRONG** (all mismatched wrong-answer explanations: C15, C16, C19, C20); IMPRECISE: C18. Science in theory, common_mistake and key_note: no errors.

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| q1 | wx2, wx3 mismatched (LAND-USE-F1) | **Do not use as written.** Science of stem/options/key is right; a rung needs every explanation to answer its own option. |
| q2 | wx2, wx3 mismatched (LAND-USE-F2) | **Do not use as written.** As q1. |

## 5. Convert lines
None in this file (no calculations).

## 6. Verdict
SOURCE OK WITH FLAGS. The theory is accurate and on-spec. Both frozen quiz items have the right stem, options and key, but their wrong-answer explanations are attached one option late, so neither is usable as written. The WS 1.4/1.5 conflict (cheap compost for food vs conserving peat) is only hinted at and needs teaching. Nothing for Mide.
