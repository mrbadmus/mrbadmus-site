# Examination — Transpiration (transpiration) — AQA 8464 4.2.3.2 / 8461 4.2.3.2
Verdict: SOURCE OK WITH FLAGS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-6/04-checked-science-source/biology-4.2.5.2-transpiration.md`.
Spec sources read as text: `AQA-8464-spec.txt` (Combined Trilogy v1.1: 4.2.3.1, 4.2.3.2), `AQA-8461-spec.txt` (Biology v1.0, same sections). Route audit row `transpiration` (OK, CF CH TF TH, 4.2.3.2). Batch-5 `plant-tissues` examination (cohesion-tension ruled A-level there; same ruling here). Runtime convention checked in `generate_site_v5.py`: `wrong_explanations` key n is shown for `opts[n]`.

**Spec reference settled.** The frozen spec field "4.2.5.2" is the site's internal numbering. The AQA reference is **4.2.3.2 Plant organ system** in both 8464 and 8461. Measuring transpiration with a potometer is a **skills point (AT 3, 4, 5)**, not a numbered required practical, on both specs. No conflict.

Conventions: q1–q3 = quiz items; "wx n" = `wrong_explanations` key n, shown for `opts[n]`; T1–T4 = theory blocks. Route copies identical except `higher`, which is `null` on CF and TF.

**wrong_explanations alignment (batch-5 defect check):** all 9 keys in q1–q3 checked; every key n explains `opts[n]`. No shift.

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 / 8461 | **4.2.3.2** | Plant organ system | base |
| Supporting | 4.2.3.1 (leaf tissues; guard cells surrounding stomata); 4.1.3.1 (leaf as exchange surface) | | base |

Spec statements (verbatim, 8464 = 8461), 4.2.3.2: "Students should be able to explain the effect of changing temperature, humidity, air movement and light intensity on the rate of transpiration." "Students should be able to understand and use simple compound measures such as the rate of transpiration." "Students should be able to: • translate information between graphical and numerical form • plot and draw appropriate graphs, selecting appropriate scales for axes • extract and interpret information from graphs, charts and tables." "The roots, stem and leaves form a plant organ system for transport of substances around the plant. Students should be able to describe the process of transpiration and translocation, including the structure and function of the stomata. Root hair cells are adapted for the efficient uptake of water by osmosis, and mineral ions by active transport. Xylem tissue transports water and mineral ions from the roots to the stems and leaves. It is composed of hollow tubes strengthened by lignin adapted for the transport of water in the transpiration stream. The role of stomata and guard cells are to control gas exchange and water loss." Skills: "AT 3, 4, 5 Measure the rate of transpiration by the uptake of water." "AT 6, 7 Investigate the distribution of stomata and guard cells." "MS 2a, 2d, 5c Process data from investigations involving stomata and transpiration rates to find arithmetic means, understand the principles of sampling and calculate surface areas and volumes." "MS 1a, 1c" (compound measures).

## 2. Route table
| # | teachable point | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Transpiration = evaporation of water from leaves; roots → xylem → leaves → stomata; transpiration stream (T1; key_note; q1) | base | 4.2.3.2 | all four | OK |
| R2 | Transpiration pull; cohesion; adhesion (T1) | **OFF-SPEC** (A-level mechanism) | — | all four | context only (F2) |
| R3 | Uses: water for photosynthesis, mineral ions, cooling; wilting; adaptations (T2) | base | 4.2.3.2 | all four | OK |
| R4 | Four factors: temperature, light, humidity, air movement (T3; common_mistake; key_note; q2; q3; matching) | base | 4.2.3.2 | all four | OK |
| R5 | Potometer: bubble distance per unit time = uptake; uptake ≈ transpiration; varying factors (T4; `higher`) | base (AT 3, 4, 5) | 4.2.3.2 | all four (T4); CH TH (`higher`) | OK; `higher` is base → ROUTE (F1) |
| R6 | Rate calculation; volume = πr² × distance; means; graphs | base | 4.2.3.2 MS 1a, 1c, 2a, 5c, 2c, 4a, 4c | — (absent) | GAP (F3) |
| R7 | Structure and function of stomata — guard cells open/close; stomata distribution investigation | base | 4.2.3.2; AT 6, 7 | — (stomata named, guard cells absent) | GAP (F4) |
| R8 | Root hair cells: water by osmosis, mineral ions by active transport | base | 4.2.3.2 | — (absent) | GAP — in `cell-specialisation`/`transport-in-cells`; one line here (F4) |
| — | RP, equation-sheet equations, FIFA | none | — | — | correct: no numbered RP |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | T1 | transpiration = evaporation of water from leaves (and other aerial parts) | OK | AQA accepts "loss of water (vapour) from the leaves / through stomata". | 4.2.3.2 |
| C2 | T1 | roots → xylem → leaves → out through stomata as vapour; transpiration stream | OK | — | 4.2.3.2 |
| C3 | T1 | cells lose water, take water from neighbours by osmosis, pull up the xylem; cohesion and adhesion | OFF-SPEC | Correct A-level science; not required (plant-tissues F3 ruled the same). | — |
| C4 | T2 | water for photosynthesis; mineral ions carried; cooling | OK | Cooling is a true extra. | 4.2.3.2 |
| C5 | T2 | excess loss → wilting; waxy cuticle, closing stomata, reduced leaf area | OK | — | 4.2.3.1–2 |
| C6 | T3 | higher temperature → faster evaporation and diffusion → faster transpiration | OK | — | 4.2.3.2 |
| C7 | T3 | brighter light → stomata open wider (for CO₂) → faster; dark → stomata close, transpiration almost stops | OK | — | 4.2.3.2 |
| C8 | T3 | low humidity → steeper gradient → faster; high humidity → slower | OK | — | 4.2.3.2 |
| C9 | T3 | wind removes water vapour near stomata → steeper gradient → faster | OK | — | 4.2.3.2 |
| C10 | T4 | potometer: shoot in sealed water-filled tube; bubble moves towards plant; distance per unit time = rate of uptake | OK | Bubble moves *towards the shoot* as water is drawn up ✓. Strictly, volume = πr² × distance (F3). | 4.2.3.2 AT 3–5 |
| C11 | T4 | potometer measures uptake, not transpiration directly | OK | Some water is used in photosynthesis / kept in cells. | 4.2.3.2 |
| C12 | T4 | vary temperature, light (lamp distance), humidity (bag/dry air), air movement (fan) | OK | Lamp distance also changes temperature — control it (e.g. heat shield / LED). | WS 2.2 |
| C13 | `higher` | potometer investigation, one factor varied, controls, rate, graph | ROUTE | Base skills point on both specs; Foundation must have it. | 4.2.3.2 AT 3–5 |
| C14 | common_mistake | fastest hot, bright, dry, windy; low humidity increases rate | OK | "dry air 'pulls' the water out" is a metaphor — it is a diffusion gradient. Minor. | 4.2.3.2 |
| C15 | q1 key | evaporation of water from leaves through stomata | OK | — | 4.2.3.2 |
| C16 | q1 wx1, wx2 | sugars = translocation; root uptake = osmosis | OK | — | 4.2.3.2 |
| C17 | q1 wx3 | photosynthesis produces oxygen; water is a reactant | OK | GCSE equation. | 4.4.1.1 |
| C18 | q2 key; wx1–3 | humid → dry windy: transpiration increases; both factors act the same way | OK | — | 4.2.3.2 |
| C19 | q3 key | brighter light → stomata open wider → more water vapour escapes | OK | AQA mark-scheme point: "(more) stomata open / open wider". | 4.2.3.2 |
| C20 | q3 opt 1 / wx1 | "Brighter light increases the temperature of the leaf, causing faster evaporation" | IMPRECISE | Partly true (wx1 admits it), so the distractor is not cleanly wrong. Key is still the best answer; usable. | — |
| C21 | q3 wx2, wx3 | photosynthesis uses water; chlorophyll absorbs light, not water | OK | — | 4.4.1.1 |
| C22 | matching (to be replaced) | six increase/decrease pairs | OK | — | 4.2.3.2 |
| C23 | `05-diagram-library/README.md` #12 (not frozen) | potometer called "RP2/investigation content" | IMPRECISE | Not an RP on either spec (8464 RP2 = osmosis; 8461 RP2 = antibiotics). Call it "Measuring transpiration (AT 3–5)". | 4.2.3.2 |

Count: **0 WRONG**; IMPRECISE: C20, C23; OFF-SPEC: C3; ROUTE: C13; GAP: rate calculations, stomata/guard cells, root hair cells.

## 4. Verdict
SOURCE OK WITH FLAGS. The four factors are correct and well explained; all three quiz items usable on all routes. Drop cohesion/adhesion, teach the potometer and its rate calculation on every route, add guard cells. Nothing for Mide.
