# Examination — Resistant Bacteria (resistant-bacteria) — AQA 8464 4.6.3.4 / 8461 4.6.3.7
Verdict: SOURCE OK WITH FLAGS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-9/04-checked-science-source/biology-4.6.5-resistant-bacteria.md`.
Spec sources read as text: `AQA-8464-spec.txt` (Version 1.1, 04 Oct 2019) 4.3.1.8, 4.6.3.1, 4.6.3.4; `AQA-8461-spec.txt` (Version 1.0) 4.3.1.8, 4.6.3.4, 4.6.3.7. No equation sheet applies. Route audit read: row `resistant-bacteria`.

Conventions: q1–q3 = quiz items; "wx n" = `wrong_explanations` key n; th1–th3 = theory chunks. The data's "4.6.5" is the site's internal number. CF and TF copies differ only in `higher` (`null`).

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 Combined Trilogy | **4.6.3.4** | Resistant bacteria | base |
| 8461 Biology | **4.6.3.7** | Resistant bacteria | base |
| Supporting | 8464/8461 4.3.1.8 Antibiotics and painkillers; 8464 4.6.3.1 / 8461 4.6.3.4 Evidence for evolution | | base |

Spec statement (verbatim, 8464 = 8461): "Bacteria can evolve rapidly because they reproduce at a fast rate. Mutations of bacterial pathogens produce new strains. Some strains might be resistant to antibiotics, and so are not killed. They survive and reproduce, so the population of the resistant strain rises. The resistant strain will then spread because people are not immune to it and there is no effective treatment. MRSA is resistant to antibiotics. To reduce the rate of development of antibiotic resistant strains: • doctors should not prescribe antibiotics inappropriately, such as treating non-serious or viral infections • patients should complete their course of antibiotics so all bacteria are killed and none survive to mutate and form resistant strains • the agricultural use of antibiotics should be restricted. The development of new antibiotics is costly and slow. It is unlikely to keep up with the emergence of new resistant strains."

**Route verdict:** base on all four routes, as the site ships. No HT, no biology-only content.

## 2. Route table
| # | teachable point (pack location) | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Variation (random mutation) → antibiotic kills non-resistant → survivors reproduce → resistant population rises (th1; key_note) | base | 4.6.3.4 | all four | OK; "existed BEFORE" over-firm (F3) |
| R2 | Fast reproduction (every 20 min) → rapid evolution (th1) | base | 4.6.3.4 | all four | OK |
| R3 | Spread between people: not immune, no effective treatment | base | 4.6.3.4 | — | GAP (F4) |
| R4 | MRSA (th2) | base | 4.6.3.4 | all four | OK; "acquired resistance through repeated exposure" IMPRECISE (F2) |
| R5 | Causes: over-prescription, incomplete courses, agriculture, global spread (th3) | base | 4.6.3.4 | all four | OK |
| R6 | New antibiotics slow/costly, unlikely to keep up (th3) | base | 4.6.3.4 | all four | OK (spec wording "costly and slow" should be used) |
| R7 | Reducing resistance: prescribe only when needed, complete course, restrict agricultural use (th3) | base | 4.6.3.4 | all four | OK |
| R8 | Phage therapy, hygiene (th3) | context | — | all four | OK, beyond spec |
| R9 | `higher` field | base content, **not HT** | 4.6.3.4 | CH TH | ROUTE (F1) |
| R10 | q1, q2, q3 | base | 4.6.3.4 | all four | OK, usable |
| — | RP, equations, FIFA, examiner_tip | none | — | — | correct |

## 3. Check table
| # | item | claim (verbatim or abridged) | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | th1 | resistance = natural selection now; four steps | OK | — | 4.6.3.4 |
| C2 | th1 | "bacteria can double every 20 minutes" | OK | Under ideal conditions. | 4.6.3.4 ("reproduce at a fast rate") |
| C3 | th1 | "The resistant mutation existed BEFORE the antibiotic was used — the antibiotic didn't create the mutation" | IMPRECISE (minor) | The core point (antibiotics do not cause mutations; they select) is right. But mutations are random and can arise at any time, including during treatment — the spec itself says survivors may "mutate and form resistant strains". Say: the mutation is random; the antibiotic does not cause it. (F3) | 4.6.3.4 |
| C4 | th2 | MRSA = methicillin-resistant Staphylococcus aureus; S. aureus carried by ~30% of people | OK | (Mostly in the nose.) | 4.6.3.4 |
| C5 | th2 | "MRSA has acquired resistance through repeated exposure to antibiotics" | IMPRECISE | Reads as if exposure made the bacteria resistant. Say: repeated antibiotic use in hospitals selected resistant strains. (F2) | 4.6.3.4 |
| C6 | th2 | dangers: sepsis, pneumonia, wounds; few antibiotics remain | OK | — | — |
| C7 | th3 | WHO: one of the greatest threats | OK | — | — |
| C8 | th3 | over-prescription for viral infections; incomplete courses leave most resistant alive; agriculture; global spread | OK | Spec's course reason: "so all bacteria are killed and none survive to mutate and form resistant strains". Both credited. | 4.6.3.4 |
| C9 | th3 | slow development, reduced investment, low profit | OK | Spec wording: "costly and slow … unlikely to keep up with the emergence of new resistant strains". | 4.6.3.4 |
| C10 | th3 | remedies incl. phage therapy, hygiene | OK | Phage therapy beyond spec. | 4.6.3.4 |
| C11 | — | resistant strain spreads because people are not immune and there is no effective treatment | GAP | Spec sentence missing. (F4) | 4.6.3.4 |
| C12 | higher | MRSA by selection in hospitals; strategies; resistance inevitable with overuse | OK science, ROUTE | Not HT — base on all four. (F1) | 4.6.3.4 |
| C13 | common_mistake | antibiotics select, do not cause; "happened randomly, long before the antibiotic was used" | OK / IMPRECISE | "long before" over-firm, as C3. | 4.6.3.4 |
| C14 | key_note | summary; MRSA hospital-acquired | OK | — | 4.6.3.4 |
| C15 | matching (to be replaced) | four steps | OK | — | — |
| C16 | q1 key | random mutation; antibiotics kill non-resistant; resistant survive and reproduce | OK | — | 4.6.3.4 |
| C17 | q1 wx1 | (opt 1 deliberately mutate) mutations random | OK, aligned | — | — |
| C18 | q1 wx2 | (opt 2 antibiotics cause the mutation) selection pressure | OK, aligned | — | — |
| C19 | q1 wx3 | (opt 3 resistant bacteria migrate in) migration can spread, not the primary mechanism | OK, aligned | — | — |
| C20 | q2 key | stopping early leaves the most resistant alive to reproduce | OK | Credited; spec reason is "so all bacteria are killed and none survive to mutate and form resistant strains". | 4.6.3.4 |
| C21 | q2 wx1 | (opt 1 prevent infection returning) can happen; resistance is the more important reason | OK, aligned | Option 1 is partly true; the stem ("why is it important") plus the lesson's focus make the key the best answer. Acceptable. | 4.6.3.4 |
| C22 | q2 wx2 | (opt 2 wasted medicine) resistance is the primary reason | OK, aligned | — | — |
| C23 | q2 wx3 | (opt 3 side effects worse) not affected | OK, aligned | — | — |
| C24 | q3 key | repeated hospital antibiotic use selected resistance mutations, which multiplied | OK | — | 4.6.3.4 |
| C25 | q3 wx1 | (opt 1 engineered as weapon) arose naturally | OK, aligned | — | — |
| C26 | q3 wx2 | (opt 2 from animals, more mutations) S. aureus mainly human; resistance by selection | OK, aligned | Livestock-associated strains exist; fine at GCSE. | — |
| C27 | q3 wx3 | (opt 3 cleaning products) select disinfectant resistance, not antibiotic resistance | OK, aligned | — | — |

Count: **0 WRONG**; IMPRECISE C3, C5, C13; GAP C11. All nine wrong_explanation keys read and aligned.

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| None | q1–q3 correct and base | Usable on all four routes. |

## 5. Verdict
SOURCE OK WITH FLAGS. Science correct; the `higher` field is not HT, the spread-between-people sentence is missing, two wordings imply exposure creates resistance. No call for Mide (the "complete the course" reason is the spec's own and is examined as written).
