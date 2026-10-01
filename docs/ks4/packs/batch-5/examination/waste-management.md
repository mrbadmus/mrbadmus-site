# Examination — Waste Management and Pollution (waste-management) — AQA 8464 4.7.3.2 / 8461 4.7.3.2
Verdict: SOURCE OK WITH FLAGS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-5/04-checked-science-source/biology-4.7.3.2-waste-management.md`.
Spec sources read as text: `AQA-8464-spec.txt` (Combined Trilogy v1.1, 4.7.3.1–4.7.3.6; chemistry 5.9.3.1–5.9.3.2 atmospheric pollutants), `AQA-8461-spec.txt` (Biology v1.0, 4.7.3.1–4.7.3.6), `AQA-8462-spec.txt` (4.9.3 link). Searched both biology specs for "eutrophication": absent. Route audit row `waste-management` (OK, CF CH TF TH). Runtime convention checked in `generate_site_v5.py`: `wrong_explanations` key n is shown for `opts[n]`.

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n, shown for `opts[n]`; T1–T3 = theory blocks. No route copy differs.

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 | **4.7.3.2** | Waste management | base |
| 8461 | **4.7.3.2** | Waste management | base |
| Supporting | 4.7.3.1 biodiversity (definition); 4.7.3.6 ("recycling resources rather than dumping waste in landfill"); chemistry 8464 5.9.3.2 / 8462 4.9.3.2 (sulfur dioxide → acid rain) — the spec's own link | | base |

Spec statements (verbatim, 8464 = 8461): "Rapid growth in the human population and an increase in the standard of living mean that increasingly more resources are used and more waste is produced. Unless waste and chemical materials are properly handled, more pollution will be caused. Pollution can occur: in water, from sewage, fertiliser or toxic chemicals; in air, from smoke and acidic gases; on land, from landfill and from toxic chemicals. Pollution kills plants and animals which can reduce biodiversity." Supporting, 4.7.3.1: "Biodiversity is the variety of all the different species of organisms on earth, or within an ecosystem." Chemistry 5.9.3.2: "Sulfur dioxide and oxides of nitrogen cause respiratory problems in humans and cause acid rain."

## 2. Route table
| # | teachable point | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Population growth + rising standard of living → more resources, more waste (T1; key_note; common_mistake; q1) | base | 4.7.3.2 | all four | OK |
| R2 | Unless handled properly → more pollution (T1) | base | 4.7.3.2 | all four | OK |
| R3 | Pollution kills plants and animals → reduces biodiversity (T1, T3) | base | 4.7.3.2 | all four | OK — biodiversity defined loosely (C2, C11) |
| R4 | Water: sewage, fertiliser, toxic chemicals (T2; key_note; q2) | base | 4.7.3.2 | all four | OK |
| R5 | Eutrophication (T2; q2 wx1; matching) | OFF-SPEC (not in 8464 or 8461) | — | all four | Context only; as written the chain is incomplete (C5) |
| R6 | Air: smoke, acidic gases (sulfur dioxide → acid rain) (T2) | base | 4.7.3.2; chem 5.9.3.2 | all four | OK |
| R7 | Land: landfill, toxic chemicals (pesticides, herbicides) (T2) | base | 4.7.3.2 | all four | OK |
| R8 | Managing waste reduces pollution: treating sewage, filtering gases, recycling (T3) | base | 4.7.3.2 ("unless … properly handled"); 4.7.3.6 (recycling) | all four | OK |
| — | equations, RP, FIFA, `higher` | none | — | — | correct: 4.7.3.2 has no HT, no separate-science content, no RP |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | T1 | growing population and rising standard of living → more resources used, more waste | OK | Spec wording. | 4.7.3.2 |
| C2 | T1 | "biodiversity (the variety of living things in an area)" | IMPRECISE | Use the spec definition: "the variety of all the different species of organisms on earth, or within an ecosystem". | 4.7.3.1 |
| C3 | T1 | pollution kills plants and animals → reduces biodiversity | OK | Spec: "can reduce". | 4.7.3.2 |
| C4 | T2 | water pollution from sewage, fertiliser washed off fields, toxic chemicals | OK | — | 4.7.3.2 |
| C5 | T2 | "Fertiliser causes eutrophication (algae bloom → less oxygen → fish die)" | IMPRECISE; OFF-SPEC | Not in the AQA biology specs. The chain skips the step that uses the oxygen: algae block light, plants below die, **decomposers (bacteria) feeding on the dead material respire and use up the oxygen**, fish die. Teach it complete or leave it as "fertiliser in water harms the organisms living there". | — |
| C6 | T2 | air pollution from smoke and acidic gases e.g. sulfur dioxide → acid rain | OK | — | 4.7.3.2; chem 5.9.3.2 |
| C7 | T2 | land pollution from landfill and toxic chemicals (pesticides, herbicides) washing into soil and water | OK | — | 4.7.3.2 |
| C8 | T3 | "Every source of pollution damages HABITATS and directly KILLS organisms." | IMPRECISE | Overstated ("every", "directly"). Spec: "Pollution kills plants and animals which can reduce biodiversity." | 4.7.3.2 |
| C9 | T3 | "the number of species and their numbers fall — biodiversity DECREASES" | IMPRECISE | Biodiversity falls when species are lost from the area; fewer individuals alone is not lower biodiversity. | 4.7.3.1 |
| C10 | T3 | treating sewage, filtering gases, recycling reduce pollution | OK | Recycling rather than landfill is a spec measure. | 4.7.3.6 |
| C11 | common_mistake | invisible pollution often does most damage; population AND standard of living both raise waste | OK | "Often does the most damage" is a judgement, not a spec claim; harmless. | 4.7.3.2 |
| C12 | key_note | as spec, plus examples | OK | — | 4.7.3.2 |
| C13 | q1 key | higher standard of living → more resources used, more waste per person | OK | — | 4.7.3.2 |
| C14 | q1 wx1–wx3 | birth rate; "no effect"; moving to countryside | OK | Each paired to its own option. | — |
| C15 | q2 key | fertiliser in a river = water pollution | OK | — | 4.7.3.2 |
| C16 | q2 wx1 (shown for "Air") | "Fertiliser in a river is water pollution — it causes eutrophication…" | OK | Rebuts "Air". Eutrophication is context (C5). | — |
| C17 | q2 wx2 (shown for "Land only") | "Fertiliser run-off enters water, not the air." | IMPRECISE (mismatched) | Written for "Air". Still true, and "enters water" rules out "land only". Usable. | — |
| C18 | q2 wx3 (shown for "None — fertiliser is not a pollutant") | "Fertiliser is a pollutant when it reaches water…" | OK | — | 4.7.3.2 |
| C19 | matching (to be replaced) | sewage, fertiliser → water; SO₂, smoke → air; landfill, pesticides → land | OK | Pesticides: spec "toxic chemicals" on land ✓. | 4.7.3.2 |

Count: **0 WRONG**; IMPRECISE: C2, C5, C8, C9, C17; OFF-SPEC: eutrophication (context).

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| none | q1 and q2 correct and base | **Both usable on all four routes** (q1 Explain, q2 Apply). q2 wx2 mismatched but true (C17). |

## 5. Convert lines
None in this file (no calculations).

## 6. Verdict
SOURCE OK WITH FLAGS. On-spec and accurate. Both quiz items are usable on every route. Things to fix in the re-cut: biodiversity is defined loosely (use the spec definition, and the idea that it falls when species are lost); the eutrophication chain is incomplete and off-spec; "every source … directly kills" is overstated. Nothing for Mide.
