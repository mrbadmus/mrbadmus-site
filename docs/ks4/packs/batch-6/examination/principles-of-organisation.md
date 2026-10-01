# Examination — Principles of Organisation (principles-of-organisation) — AQA 8464 4.2.1 / 8461 4.2.1
Verdict: SOURCE OK WITH FLAGS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-6/04-checked-science-source/biology-4.2.1-principles-of-organisation.md`.
Spec sources read as text: `AQA-8464-spec.txt` (Combined Trilogy v1.1, 4.2.1; 4.2.3.1 for the leaf as an organ), `AQA-8461-spec.txt` (Biology v1.0, 4.2.1; 4.2.3.1). Route audit row `principles-of-organisation` (OK, CF CH TF TH, 4.2.1). Runtime convention checked in `generate_site_v5.py` (l. 4059, 4614): `wrong_explanations` key n is shown for `opts[n]`.

Conventions: q1–q4 = quiz items; "wx n" = `wrong_explanations` key n, shown for `opts[n]`; T1–T5 = theory blocks. No route copy differs (no `higher` field at all).

**wrong_explanations alignment (batch-5 defect check):** all 12 keys in q1–q4 checked; every key n explains `opts[n]`. No shift.

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 | **4.2.1** | Principles of organisation | base |
| 8461 | **4.2.1** | Principles of organisation | base |
| Supporting | 4.2.3.1 ("The leaf is a plant organ"); 4.2.2.1 (digestive system as an organ system) | | base |

Spec statements (verbatim, 8464 = 8461): "Cells are the basic building blocks of all living organisms. A tissue is a group of cells with a similar structure and function. Organs are aggregations of tissues performing specific functions. Organs are organised into organ systems, which work together to form organisms." Skills: "MS 1c Students should be able to develop an understanding of size and scale in relation to cells, tissues, organs and systems."

## 2. Route table
| # | teachable point | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Hierarchy cell → tissue → organ → organ system → organism (T1; key_note; q1) | base | 4.2.1 | all four | OK |
| R2 | Cell as basic unit; specialised cells (T2) | base | 4.2.1; 4.1.1.3 | all four | OK (C3 imprecise) |
| R3 | Tissue = group of similar cells, one function; animal and plant tissue examples (T3; q2; common_mistake) | base | 4.2.1; 4.2.3.1 | all four | OK (C5, C6 imprecise) |
| R4 | Organ = several tissues; stomach, leaf, heart (T4; q3) | base | 4.2.1; 4.2.3.1 | all four | OK (C8 imprecise) |
| R5 | Organ systems and organism (T5; q4) | base | 4.2.1; 4.2.2.1 | all four | OK |
| R6 | Size and scale of the levels (MS 1c) | base | 4.2.1 MS 1c | — (absent) | GAP (F3) |
| — | `higher`, RP, equations, FIFA | none | — | — | correct: 4.2.1 has no HT, no biology-only content, no RP |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | T1; key_note | levels in order, simplest → most complex | OK | — | 4.2.1 |
| C2 | T2 | "A cell is the smallest unit capable of carrying out all the processes of life"; every organism at least one cell | OK | Spec: "basic building blocks". | 4.2.1 |
| C3 | T2 | "All cells in one organism contain the same DNA, but different genes are switched on" | IMPRECISE (minor) | Red blood cells have no nucleus; gametes have half. Gene switching is beyond 4.2.1. Say "most body cells carry the same genes" or drop. | 4.1.1.3 |
| C4 | T2 | muscle cell contracts, red blood cell carries oxygen, root hair cell absorbs water | OK | — | 4.1.1.3 |
| C5 | T3 | "A tissue is a group of similar cells working together to carry out a particular function" | OK | Spec: "cells with a similar structure and function". | 4.2.1 |
| C6 | T4; common_mistake; q3 wx1 | "a tissue is made of ONE type of cell" | IMPRECISE | Overstated — many tissues hold more than one cell type (blood; xylem; phloem). Spec: "cells with a similar structure and function". | 4.2.1 |
| C7 | T3 | muscle, epithelial, glandular, nervous tissue; mesophyll, xylem, phloem | OK | Xylem "hollow dead cells", phloem "living cells" — consistent with 4.2.3.2. | 4.2.3.1–2 |
| C8 | T4 | heart "contains cardiac muscle tissue, valves, coronary blood vessels" | IMPRECISE | Valves and coronary vessels are structures, not tissues. Heart tissues: cardiac muscle, nervous, connective tissue, epithelial lining. | 4.2.1 |
| C9 | T4 | stomach: muscle tissue churns, epithelial lines, glandular secretes HCl and pepsin | OK | Classic AQA example. | 4.2.1; 4.2.2.1 |
| C10 | T4 | leaf: mesophyll, xylem, phloem, epidermis, "guard cells (gas exchange)" | OK | Leaf is an organ (spec). Guard cells are cells around stomata, listed fine. | 4.2.3.1 |
| C11 | T5 | digestive (mouth … pancreas), circulatory (heart, vessels, blood), respiratory, nervous systems and functions | OK | — | 4.2.1; 4.2.2.1 |
| C12 | q1 key; wx1–3 | Cell → Tissue → Organ → Organ system → Organism; wx each rebuts its option | OK | — | 4.2.1 |
| C13 | q2 key; wx1–3 | tissue = group of similar cells, specific function | OK | — | 4.2.1 |
| C14 | q3 key; wx1–3 | stomach = organ | OK | wx1 repeats C6's "ONE type of cell" — imprecise, item usable. | 4.2.1 |
| C15 | q4 key; wx1–3 | digestive system = organ system | OK | — | 4.2.1 |
| C16 | matching (to be replaced) | five level–example pairs | OK | — | — |

Count: **0 WRONG**; IMPRECISE: C3, C6, C8; GAP: size and scale (MS 1c). All four quiz items usable on all four routes.

## 4. Verdict
SOURCE OK WITH FLAGS. Science correct at GCSE; three re-cuttable imprecisions; one GAP (MS 1c size and scale). Nothing for Mide.
