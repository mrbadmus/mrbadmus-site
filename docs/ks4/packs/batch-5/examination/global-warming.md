# Examination — Global Warming and Its Effects on Ecosystems (global-warming) — AQA 8464 4.7.3.5 / 8461 4.7.3.5
Verdict: SOURCE OK WITH FLAGS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-5/04-checked-science-source/biology-4.7.3.5-global-warming.md`.
Spec sources read as text: `AQA-8464-spec.txt` (Combined Trilogy v1.1, 4.7.3.1–4.7.3.6; chemistry 5.9.2.1–5.9.2.4), `AQA-8461-spec.txt` (Biology v1.0, 4.7.3.5, 4.7.2.4 Impact of environmental change (biology only) (HT only)), `AQA-8462-spec.txt` (4.9.2.3). Route audit row `global-warming` (OK, CF CH TF TH). Sibling lessons: `environmental-change` (8461 4.7.2.4, TH); chemistry `greenhouse-gases`. Runtime convention checked in `generate_site_v5.py`: `wrong_explanations` key n is shown for `opts[n]`.

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n, shown for `opts[n]`; T1–T3 = theory blocks. No route copy differs.

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 | **4.7.3.5** | Global warming | base |
| 8461 | **4.7.3.5** | Global warming | base |
| Supporting | chemistry 8464 5.9.2.2–5.9.2.3 / 8462 4.9.2.2–4.9.2.3 (human activities raising CO₂ and methane; four potential effects of climate change); 8461 4.7.2.4 (biology only) (HT only) — environmental change and species distribution, own lesson | | base / triple-higher (own lesson) |

Spec statements (verbatim, 8464 = 8461): "Students should be able to describe some of the biological consequences of global warming. Levels of carbon dioxide and methane in the atmosphere are increasing, and contribute to 'global warming'." Skills: "WS 1.6 Understand that the scientific consensus about global warming and climate change is based on systematic reviews of thousands of peer reviewed publications. WS 1.3 Explain why evidence is uncertain or incomplete in a complex context."
Supporting, 8461 4.7.2.4 (biology only) (HT only): "Environmental changes affect the distribution of species in an ecosystem. These changes include: temperature; availability of water; composition of atmospheric gases." Chemistry 5.9.2.2: "Students should be able to recall two human activities that increase the amounts of each of the greenhouse gases carbon dioxide and methane."

The spec does not list the biological consequences. Those AQA mark schemes credit: species distribution changes (range shifts towards the poles or uphill), changed migration patterns, loss of habitat (including low-lying coastal habitats flooded by rising sea level), extinction and reduced biodiversity, and spread of pests and diseases into new areas. This is examiner knowledge (AQA 8461/8464 papers), not fetched.

## 2. Route table
| # | teachable point | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | CO₂ and methane levels increasing; they contribute to global warming (T1; key_note) | base | 4.7.3.5 | all four | OK |
| R2 | Greenhouse gases trap heat (T1) | base (mechanism is chemistry 5.9.2.1) | 4.7.3.5; chem 5.9.2.1 | all four | OK at this level |
| R3 | Human activities: burning fossil fuels, deforestation, livestock (T1) | base | chem 5.9.2.2 | all four | OK |
| R4 | Biological consequences: distribution, migration, sea level → coastal habitats flooded, reduced biodiversity/extinction (T2; common_mistake; key_note; q1; q2) | base | 4.7.3.5 | all four | OK (one imprecision, C7) |
| R5 | Evaluating distribution change from given data | **triple-higher** — own lesson `environmental-change` | 8461 4.7.2.4 (biology only) (HT only) | — | Not in this source; keep it out of this page |
| R6 | Evidence, data, uncertainty, models (T3) | base | 4.7.3.5 WS 1.3 | all four | OK |
| R7 | Scientific consensus from systematic reviews of thousands of peer-reviewed publications | base | 4.7.3.5 WS 1.6 | — (absent) | **GAP** (GLOBAL-WARMING-F3) |
| — | equations, RP, FIFA, `higher` | none | — | — | correct: 4.7.3.5 has no HT, no separate-science content, no RP |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | T1 | CO₂ and methane levels in the atmosphere are increasing | OK | Spec wording. | 4.7.3.5 |
| C2 | T1 | greenhouse gases trap heat energy near the Earth's surface; more gas → more heat trapped → average temperature rises | OK | GCSE-level summary; the mechanism (absorbing long-wavelength radiation) is chemistry 5.9.2.1. | 5.9.2.1 |
| C3 | T1 | burning fossil fuels, deforestation, livestock farming (methane) | OK | Two per gas available: CO₂ — fossil fuels, deforestation; methane — livestock, (rice fields, landfill). | 5.9.2.2 |
| C4 | T2 | distribution changes; ranges shift towards poles or higher ground | OK | — | 4.7.3.5 |
| C5 | T2 | migration patterns change (e.g. birds arrive earlier) | OK | — | 4.7.3.5 |
| C6 | T2 | species that cannot move or adapt fast enough may become extinct → reduced biodiversity | OK | — | 4.7.3.1; 4.7.3.5 |
| C7 | T2; common_mistake; key_note | sea level rises from "melting ice" and expansion of warmer water | IMPRECISE (minor) | Only melting **land** ice (glaciers, ice sheets) raises sea level; floating sea ice does not. q2 wx1 already says "land ice". | — |
| C8 | T3 | data on temperature, CO₂, ice cover, species ranges; strong evidence of human cause; uncertainties, models | OK | WS 1.3 ✓. WS 1.6 (consensus from systematic reviews of thousands of peer-reviewed publications) missing. | 4.7.3.5 WS |
| C9 | common_mistake | distribution = where a species lives, not how many | OK | — | — |
| C10 | key_note | as theory | OK | "Melting ice" — C7. | — |
| C11 | q1 stem, options, key | distribution = the geographic area where a species is found | OK | Key correct. | 4.7.3.5 |
| C12 | q1 wx1 (shown for "total number of individuals") | "Distribution is the range — the places on Earth where a species lives…" | OK | Rebuts the option. | — |
| C13 | q1 wx2 (shown for "How the food is shared within a population") | "That is population size, not distribution." | **WRONG (mismatched)** | Written for opt 1 (number of individuals). Food-sharing is not population size. | — |
| C14 | q1 wx3 (shown for "The genetic variety within the species") | "That is not what distribution means in ecology." | IMPRECISE | Written for opt 2; generic but true for opt 3. | — |
| C15 | q2 stem, options, key | sea level rises from melting ice and thermal expansion | OK | Key correct. | — |
| C16 | q2 wx1 (shown for "Photosynthesis and respiration") | "Warming melts land ice … and makes existing sea water expand…" | IMPRECISE | Explains the key rather than rebutting the option; true. | — |
| C17 | q2 wx2 (shown for "More rain falling on land") | "Photosynthesis and respiration cycle carbon; they do not raise sea level." | **WRONG (mismatched)** | Written for opt 1. | — |
| C18 | q2 wx3 (shown for "Fish releasing carbon dioxide") | "Rainfall does not cause the long-term rise…" | **WRONG (mismatched)** | Written for opt 2. Nothing rebuts "fish releasing CO₂". | — |
| C19 | matching (to be replaced) | causes: CO₂ from fossil fuels, methane from livestock, deforestation; effects: range shift, migration timing, coastal habitats lost | OK | All correct. | 4.7.3.5; 5.9.2.2 |

The explanations on both items are attached one option late (as in `land-use`): wx2's text belongs to opt 1, wx3's to opt 2, wx1 explains the key, and opt 3 has no explanation. Stems, options and keys are all correct.

Count: **3 WRONG** (all mismatched wrong-answer explanations: C13, C17, C18); IMPRECISE: C7, C14, C16; GAP: WS 1.6.

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| q1 | wx2 mismatched (GLOBAL-WARMING-F1) | **Do not use as written.** Stem, options and key correct. |
| q2 | wx2, wx3 mismatched (GLOBAL-WARMING-F2) | **Do not use as written.** Stem, options and key correct. |

## 5. Convert lines
None in this file (no calculations).

## 6. Verdict
SOURCE OK WITH FLAGS. The theory is accurate and on-spec; only "melting ice" should say land ice. Both frozen quiz items have the right stem, options and key, but their wrong-answer explanations are attached one option late, so neither is usable as written. WS 1.6 (consensus from systematic reviews of peer-reviewed papers) is missing and should be taught. The HT, biology-only evaluation of distribution change (8461 4.7.2.4) is its own lesson and stays off this page. Nothing for Mide.
