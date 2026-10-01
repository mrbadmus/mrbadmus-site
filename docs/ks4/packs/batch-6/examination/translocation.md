# Examination — Translocation (translocation) — AQA 8464 4.2.3.2 / 8461 4.2.3.2
Verdict: SOURCE OK WITH FLAGS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-6/04-checked-science-source/biology-4.2.5.3-translocation.md`.
Spec sources read as text: `AQA-8464-spec.txt` (Combined Trilogy v1.1: 4.2.3.1, 4.2.3.2), `AQA-8461-spec.txt` (Biology v1.0, same sections). Route audit row `translocation` (OK, CF CH TF TH, 4.2.3.2). Batch-5 `plant-tissues` examination (companion cells / active loading ruled OFF-SPEC there; same ruling here). Runtime convention checked in `generate_site_v5.py`: `wrong_explanations` key n is shown for `opts[n]`.

**Spec reference settled.** The frozen spec field "4.2.5.3" is the site's internal numbering. The AQA reference is **4.2.3.2 Plant organ system** in both 8464 and 8461. The spec says outright: "Detailed structure of phloem tissue or the mechanism of transport is not required." No conflict.

Conventions: q1–q3 = quiz items; "wx n" = `wrong_explanations` key n, shown for `opts[n]`; T1–T3 = theory blocks. Route copies identical except `higher`, which is `null` on CF and TF.

**wrong_explanations alignment (batch-5 defect check):** all 9 keys in q1–q3 checked; every key n explains `opts[n]`. No shift.

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 / 8461 | **4.2.3.2** | Plant organ system | base |
| Supporting | 4.2.3.1 (xylem and phloem as plant tissues) | | base |

Spec statements (verbatim, 8464 = 8461): "Students should be able to explain how the structure of root hair cells, xylem and phloem are adapted to their functions." "Students should be able to describe the process of transpiration and translocation, including the structure and function of the stomata." "Xylem tissue transports water and mineral ions from the roots to the stems and leaves. It is composed of hollow tubes strengthened by lignin adapted for the transport of water in the transpiration stream." "Phloem tissue transports dissolved sugars from the leaves to the rest of the plant for immediate use or storage. The movement of food molecules through phloem tissue is called translocation. Phloem is composed of tubes of elongated cells. Cell sap can move from one phloem cell to the next through pores in the end walls. Detailed structure of phloem tissue or the mechanism of transport is not required."

## 2. Route table
| # | teachable point | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Translocation = movement of dissolved sugars in phloem from leaves to where used or stored (T1; key_note; q1) | base | 4.2.3.2 | all four | OK |
| R2 | Source / sink vocabulary; sinks: growing tips, roots (respiration, starch store), fruits, seeds, flowers (T1; q3) | base idea; "source/sink" words beyond spec | 4.2.3.2 ("for immediate use or storage") | all four | OK as idea; vocabulary OFF-SPEC (F3) |
| R3 | Both directions in phloem; xylem upwards only (T1; T3; common_mistake; q2) | base | 4.2.3.2 | all four | OK |
| R4 | Mechanism: active loading, ATP, companion cells, osmosis, pressure, unloading (T2; T3 "Driving force", "Energy"; key_note "uses ATP"; `higher`; matching) | **OFF-SPEC** | 4.2.3.2 ("mechanism of transport is not required") | all four (T2–T3); CH TH (`higher`) | do not teach (F1, F2) |
| R5 | Xylem vs phloem contrast: substance, vessel, direction, dead/living (T3; common_mistake) | base | 4.2.3.2 | all four | OK |
| R6 | Phloem = tubes of elongated cells, sap through pores in end walls; xylem = hollow tubes strengthened by lignin | base | 4.2.3.2 | — (phloem structure absent; lignin only in matching) | GAP — spec core missing (F4) |
| — | RP, equations, FIFA | none | — | — | correct |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | T1 | translocation = transport of dissolved sugars (mainly sucrose) through phloem | OK | Spec: "dissolved sugars". | 4.2.3.2 |
| C2 | T1 | source mainly leaves; sinks: shoot tips, roots (respiration, starch), fruits, seeds, flowers | OK | Spec: "from the leaves to the rest of the plant for immediate use or storage". | 4.2.3.2 |
| C3 | T1; q2 | phloem moves sugars both directions; transpiration stream upward only | OK | — | 4.2.3.2 |
| C4 | T2 | sucrose actively loaded using ATP from companion cells; water in by osmosis from xylem; pressure drives flow; active unloading | OFF-SPEC | Correct A-level pressure-flow account; spec: "Detailed structure of phloem tissue or the mechanism of transport is not required." | 4.2.3.2 |
| C5 | T3 (transpiration column) | water and minerals; xylem; upwards; dead cells; evaporation pull; passive | OK | "No ATP needed" is true; beyond spec. | 4.2.3.2 |
| C6 | T3 (translocation column) | sugars; phloem; both directions; living cells | OK | — | 4.2.3.2 |
| C7 | T3 (translocation column) | "Driving force: active loading of sucrose creates pressure"; "Energy: ACTIVE (ATP required …)" | OFF-SPEC | As C4. | 4.2.3.2 |
| C8 | `higher` | active loading, companion cells, osmotic and hydrostatic pressure gradient | OFF-SPEC; ROUTE | Not HT GCSE; excluded by the spec. | 4.2.3.2 |
| C9 | common_mistake | sugars/phloem vs water/xylem; both directions vs upwards; living vs dead | OK | — | 4.2.3.2 |
| C10 | key_note | "…living cells, uses ATP. NOT the same as transpiration (… passive)" | OFF-SPEC (part) | "uses ATP" / "passive" are mechanism; rest OK. | 4.2.3.2 |
| C11 | q1 key; wx1–3 | phloem carries sucrose; water/minerals = xylem; O₂ and CO₂ diffuse via stomata | OK | — | 4.2.3.2 |
| C12 | q2 key; wx1–3 | both directions; upwards only = xylem; shoot tips need sugar; along the plant not outwards | OK | — | 4.2.3.2 |
| C13 | q3 key; wx1–3 | "sink" = any part where sugars are used or stored; leaves = source | OK science; OFF-SPEC vocabulary | The idea is spec; the word "sink" is not. Usable only if the page teaches "sink" as a label. | 4.2.3.2 |
| C14 | matching (to be replaced) | six pairs; "Requires ATP energy — companion cells supply energy to sieve tubes" | OFF-SPEC (one pair) | Replace anyway. | 4.2.3.2 |

Count: **0 WRONG**; OFF-SPEC: C4, C7, C8, C10, C13 (vocab), C14; GAP: phloem/xylem structure (spec core).

## 4. Verdict
SOURCE OK WITH FLAGS. Everything stated is correct science, but a whole theory block (T2), the `higher` field and parts of T3/key_note teach the mechanism the spec excludes; the spec's own phloem structure statement is missing (written out in the source). q1, q2 usable on all routes; q3 conditional on "sink" being taught. Nothing for Mide.
