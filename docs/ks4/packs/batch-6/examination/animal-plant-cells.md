# Examination — Animal and Plant Cells (animal-plant-cells) — AQA 8464 4.1.1.2 / 8461 4.1.1.2
Verdict: SOURCE OK WITH FLAGS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-6/04-checked-science-source/biology-4.1.1.2-animal-plant-cells.md`.
Spec sources read as text: `AQA-8464-spec.txt` (Combined Trilogy v1.1, 4.1.1.1–4.1.1.5, RP1), `AQA-8461-spec.txt` (Biology v1.0, same sections, RP1, §8.2.1). Both texts are identical for 4.1.1.2. ATP: grep of both specs finds no occurrence. Route audit row `animal-plant-cells` (OK, CF CH TF TH). Sibling lessons: `eukaryotes-prokaryotes` (4.1.1.1), `microscopy` (4.1.1.5; batch-3 examination R9 gives it the full RP1 block). Runtime convention checked in `generate_site_v5.py` (`render_quiz`): `wrong_explanations` key n is shown for `opts[n]` (0-based).

Conventions: q1–q5 = quiz items; "wx n" = `wrong_explanations` key n, shown for `opts[n]`; T1–T4 = theory blocks. No route copy differs. No `[NEW — to be examined]` lines (no FIFA). **wx alignment checked: all five items correctly paired; no one-option-late shift.**

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 | **4.1.1.2** | Animal and plant cells | base |
| 8461 | **4.1.1.2** | Animal and plant cells | base |
| RP | Required practical activity 1 (8464 RP1 = 8461 RP1), printed under 4.1.1.2 | | base |
| Supporting | 4.1.1.5 Microscopy (magnification = size of image ÷ size of real object); 4.1.1.1 (plasmids, bacterial cells) | | base |

Spec statements (verbatim, 8464 = 8461): "Students should be able to explain how the main sub-cellular structures, including the nucleus, cell membranes, mitochondria, chloroplasts in plant cells and plasmids in bacterial cells are related to their functions. Most animal cells have the following parts: a nucleus; cytoplasm; a cell membrane; mitochondria; ribosomes. In addition to the parts found in animal cells, plant cells often have: chloroplasts; a permanent vacuole filled with cell sap. Plant and algal cells also have a cell wall made of cellulose, which strengthens the cell. Students should be able to use estimations and explain when they should be used to judge the relative size or area of sub-cellular structures." RP1: "use a light microscope to observe, draw and label a selection of plant and animal cells. A magnification scale must be included."

## 2. Route table
| # | teachable point | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Five animal-cell parts and their functions (T1; key_note; q1, q4, q5) | base | 4.1.1.2 | all four | OK (ATP wording, F2) |
| R2 | Plant extras: cell wall (cellulose), chloroplasts, permanent vacuole with cell sap (T2; key_note; q3) | base | 4.1.1.2 | all four | OK |
| R3 | Not every plant cell has chloroplasts (T2; common_mistake; q2) | base | 4.1.1.2 ("often have") | all four | OK |
| R4 | Structure matches function (T3) | base | 4.1.1.2 | all four | OK (F3 number) |
| R5 | Light-microscope method (T4) | base | RP1 | all four | **F1 WRONG stain colour**; F4 method gaps |
| R6 | RP1 (rp field): observe, draw, label, scale bar, magnification | base | 8464 RP1 / 8461 RP1 | all four | OK |
| R7 | Estimation of relative size of sub-cellular structures (MS 1d) | base | 4.1.1.2 | — | **GAP** (F5) |
| R8 | Plasmids in bacterial cells related to function | base | 4.1.1.2 | — | owned by `eukaryotes-prokaryotes` (4.1.1.1); not a gap here |
| — | equations, FIFA, `higher` | none | — | — | correct: 4.1.1.2 has no HT and no separate-science content |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | T1 | nucleus contains DNA in chromosomes; controls cell activity | OK | — | 4.1.1.2; 4.1.2.1 |
| C2 | T1 | nuclear envelope, double membrane with pores | OK | Beyond spec, true. | — |
| C3 | T1 | membrane of phospholipids and proteins; controls entry/exit; selectively permeable | OK | Spec word is "partially permeable" (4.1.3.2); either accepted. | — |
| C4 | T1 | cytoplasm: most chemical reactions; enzymes | OK | — | — |
| C5 | T1 | mitochondria: aerobic respiration, glucose + oxygen, "release energy as ATP" | IMPRECISE | ATP is not in AQA 8461/8464. Say "aerobic respiration takes place here, releasing energy". F2. | 4.1.1.2; 4.4.2.1 |
| C6 | T1 | active cells (muscle, sperm, liver) have more mitochondria | OK | — | — |
| C7 | T1 | ribosomes: free or on ER; protein synthesis | OK | ER beyond spec, true. | 4.1.1.2 |
| C8 | T2 | cell wall of cellulose; rigid; prevents bursting | OK | Spec: "strengthens the cell". Algal cells also have one (spec). | 4.1.1.2 |
| C9 | T2 | chloroplasts: chlorophyll absorbs light for photosynthesis; CO₂ + water → glucose | OK | — | 4.4.1.1 |
| C10 | T2 | only light-exposed cells have chloroplasts; roots, potato storage cells, deep stem cells have none | OK | Matches spec "often have". | 4.1.1.2 |
| C11 | T2 | permanent vacuole, cell sap (sugars, salts, pigments); turgor; wilting | OK | — | 4.1.1.2 |
| C12 | T3 | "Palisade mesophyll cells in leaves have up to 70 chloroplasts" | IMPRECISE | Published counts vary widely (tens to over 100). Say "many chloroplasts". F3. | — |
| C13 | T3 | high-demand cells have most mitochondria; large vacuole → turgor; wall + vacuole support | OK | — | — |
| C14 | T4 step 1 | "thin section of tissue (e.g. onion epidermis, cheek cells)" | IMPRECISE | Onion epidermis is peeled; cheek cells are a scraping smeared on the slide, not a section. F4. | RP1 |
| C15 | T4 step 4 | "iodine solution stains starch and nuclei blue/purple" | **WRONG** | Iodine turns starch blue-black; in onion cells it stains the nucleus and cytoplasm yellow-brown. Methylene blue stains animal-cell nuclei blue ✓. F1. | RP1; 4.2.2.1 (iodine test) |
| C16 | T4 step 5 | coarse focus first, then fine | OK | Missing: start on the lowest-power objective. F4. | RP1 |
| C17 | T4 | visible: nucleus, cytoplasm, cell wall, vacuole, chloroplasts; not ribosomes or mitochondrial detail | OK | — | 4.1.1.5 |
| C18 | common_mistake | not all plant cells have chloroplasts; plant cells have wall AND membrane | OK | — | 4.1.1.2 |
| C19 | key_note | lists | OK | — | 4.1.1.2 |
| C20 | rp | "RP1 — … Include a scale bar and calculate magnification." | OK | Spec: "A magnification scale must be included." Number correct in both specs. | RP1 |
| C21 | q1 key | ribosomes = protein synthesis | OK | — | 4.1.1.2 |
| C22 | q1 wx1–wx3 | mitochondria = respiration; nucleus holds instructions, ribosomes assemble; chloroplasts = photosynthesis | OK | Paired correctly. | — |
| C23 | q2 key | root underground, no light, no chloroplasts | OK | — | — |
| C24 | q2 wx1–wx3 | size not the reason; plant cells are eukaryotic; chloroplasts in plant not animal cells | OK | Paired correctly. | 4.1.1.1 |
| C25 | q3 key | vacuole: cell sap, turgor | OK | — | 4.1.1.2 |
| C26 | q3 wx1–wx3 | chlorophyll in chloroplasts; respiration in mitochondria; membrane controls entry | OK | Paired correctly. | — |
| C27 | q4 key | mitochondria in both | OK | Only one true option (ribosomes etc. not offered). | 4.1.1.2 |
| C28 | q4 wx1–wx3 | walls in plants, bacteria, fungi; chloroplasts plant only; animal cells may have small temporary vacuoles | OK | Paired correctly. | — |
| C29 | q5 key | active muscle cells need more ATP energy; more mitochondria | OK (IMPRECISE term) | Key correct; "ATP" off-spec (F2). | 4.1.1.2 |
| C30 | q5 wx1–wx3 | energy demand decides; oxygen enters by diffusion, mitochondria use it; all cells respire | OK | Paired correctly. | 4.1.3.1 |
| C31 | matching (to be replaced) | seven organelle–function pairs | OK | — | — |

Count: **1 WRONG** (C15, theory — re-cuttable); IMPRECISE: C5, C12, C14, C29. All five quiz items correct and correctly paired.

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| none | q1–q5 correct, base, explanations paired correctly. | All five usable on all four routes. q5 says "ATP" — acceptable, but teach "energy released by respiration" as the exam wording. |

## 5. Verdict
SOURCE OK WITH FLAGS. Organelles, functions and the plant extras are right and on-spec; all five quiz items usable. One wrong theory fact (iodine stains nuclei "blue/purple" — it stains them yellow-brown), plus off-spec ATP wording, an unsupported chloroplast count, and RP1 method gaps. The spec prints RP1 under 4.1.1.2; batch 3 gave the full RP1 block to `microscopy` — this page should observe and label, and link there. Nothing for Mide.
