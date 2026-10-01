# Examination — Cell Specialisation and Differentiation (cell-specialisation) — AQA 8464 4.1.1.3–4.1.1.4 / 8461 4.1.1.3–4.1.1.4
Verdict: SOURCE HAS ERRORS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-6/04-checked-science-source/biology-4.1.1.3-cell-specialisation.md`.
Spec sources read as text: `AQA-8464-spec.txt` (Combined Trilogy v1.1, 4.1.1.3, 4.1.1.4, 4.1.3.3, 4.2.2.3 Blood, 4.2.3.1–4.2.3.2 plant tissues and organ system), `AQA-8461-spec.txt` (Biology v1.0, same sections; identical text). ATP and "water potential": grep of both specs finds neither. Route audit row `cell-specialisation` (OK, CF CH TF TH, 4.1.1.3–4). Runtime convention checked in `generate_site_v5.py` (`render_quiz`): `wrong_explanations` key n is shown for `opts[n]` (0-based).

Conventions: q1–q4 = quiz items; "wx n" = `wrong_explanations` key n, shown for `opts[n]`; T1–T3 = theory blocks. No route copy differs. No `[NEW — to be examined]` lines (no FIFA). **wx alignment checked: all four items correctly keyed (wx n addresses opt n); no one-option-late shift.** Two explanations are wrong in content (F1, F2).

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 / 8461 | **4.1.1.3** | Cell specialisation | base |
| 8464 / 8461 | **4.1.1.4** | Cell differentiation | base |
| Supporting | 4.2.2.3 Blood (red blood cells); 4.2.3.2 Plant organ system (root hair, xylem, phloem adaptations); 4.1.3.3 Active transport (root hair mineral ions) | | base |

Spec statements (verbatim, 8464 = 8461). 4.1.1.3: "Students should be able to, when provided with appropriate information, explain how the structure of different types of cell relate to their function in a tissue, an organ or organ system, or the whole organism. Cells may be specialised to carry out a particular function: sperm cells, nerve cells and muscle cells in animals; root hair cells, xylem and phloem cells in plants." 4.1.1.4: "Students should be able to explain the importance of cell differentiation. As an organism develops, cells differentiate to form different types of cells. Most types of animal cell differentiate at an early stage. Many types of plant cells retain the ability to differentiate throughout life. In mature animals, cell division is mainly restricted to repair and replacement. As a cell differentiates it acquires different sub-cellular structures to enable it to carry out a certain function. It has become a specialised cell." 4.2.3.2: "Root hair cells are adapted for the efficient uptake of water by osmosis, and mineral ions by active transport. … [Xylem] is composed of hollow tubes strengthened by lignin … Phloem is composed of tubes of elongated cells. Cell sap can move from one phloem cell to the next through pores in the end walls. Detailed structure of phloem tissue or the mechanism of transport is not required."

## 2. Route table
| # | teachable point | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Differentiation: zygote → specialised cells; animals early, plants (meristems) throughout life (T1; key_note) | base | 4.1.1.4 | all four | OK; repair-and-replacement line missing (F5) |
| R2 | Sperm cell (T2; q1) | base | 4.1.1.3 | all four | OK (off-spec terms, F7) |
| R3 | Red blood cell (T2; q2) | base | 4.2.2.3 | all four | OK in theory; q2 WRONG (F1) |
| R4 | Neurone (T2) | base | 4.1.1.3 | all four | **WRONG** "brain to toe" (F3) |
| R5 | Muscle cell (T2) | base | 4.1.1.3 | all four | OK |
| R6 | Root hair cell (T3; common_mistake; q3) | base | 4.1.1.3; 4.2.3.2; 4.1.3.3 | all four | IMPRECISE (F4); GAP (F5) |
| R7 | Xylem (T3; q4) | base | 4.1.1.3; 4.2.3.2 | all four | OK in theory; q4 WRONG (F2) |
| R8 | Phloem (T3) | base | 4.1.1.3; 4.2.3.2 | all four | OFF-SPEC detail (F6) |
| R9 | Palisade cell (T3) | base | 4.2.3.1 (palisade mesophyll) | all four | OK |
| — | equations, FIFA, RP, `higher` | none | — | — | correct: no HT, no separate-science content, no RP |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | T1 | zygote divides by mitosis; cells become specialised = differentiation | OK | — | 4.1.1.4; 4.1.2.2 |
| C2 | T1 | differentiation switches genes on and off | OK | Beyond spec, true. | — |
| C3 | T1 | animals differentiate early and lose the ability; plants keep it in meristems | OK | Missing spec line: "In mature animals, cell division is mainly restricted to repair and replacement" (F5). | 4.1.1.4 |
| C4 | T2 sperm | streamlined head; flagellum; many mitochondria in midpiece | OK | "ATP energy" off-spec (F7). | 4.1.1.3 |
| C5 | T2 sperm | acrosome enzymes "digest through the egg's outer membrane" | IMPRECISE | They digest the egg's outer layers (jelly coat) so the head can reach and fuse with the membrane. F7. | — |
| C6 | T2 sperm | haploid nucleus, 23 chromosomes, 46 restored | OK | "Haploid" off-spec; AQA says "half the number of chromosomes". | 4.6.1.2 |
| C7 | T2 RBC | biconcave; no nucleus → more haemoglobin; flexible; ~270 million haemoglobin | OK | ~270 million is the standard figure. | 4.2.2.3 |
| C8 | T2 neurone | "axon … over a metre long (e.g. sciatic nerve), allowing signals to travel from brain to toe without interruption" | **WRONG** | No neurone runs from brain to toe. The longest axons (~1 m) run from the spinal cord to the foot; an impulse from the brain crosses at least one synapse. F3. | 4.5.2.1 |
| C9 | T2 neurone | myelin, nodes of Ranvier, dendrites, synaptic terminals | OK | Beyond spec, true. | — |
| C10 | T2 muscle | actin and myosin; many mitochondria; glycogen store | OK | — | 4.1.1.3; 4.4.2.3 (glycogen) |
| C11 | T3 root hair | long projection → large surface area; no chloroplasts | OK | — | 4.2.3.2 |
| C12 | T3 root hair | "Thin cell wall — short diffusion distance" | OK | — | — |
| C13 | T3 root hair | "Large permanent vacuole — maintains a low water potential inside the cell to draw water in by osmosis" | IMPRECISE | Water potential is not GCSE. Say: cell sap is more concentrated than soil water, so water moves in by osmosis. F4. | 4.1.3.2; 4.2.3.2 |
| C14 | T3 root hair | — (absent) | GAP | Many mitochondria release energy for active transport of mineral ions. F5. | 4.1.3.3; 4.2.3.2 |
| C15 | T3 xylem | dead; hollow; lignin; no end walls | OK | Spec: "hollow tubes strengthened by lignin". "Prevents collapse under pressure" — under tension, minor. | 4.2.3.2 |
| C16 | T3 phloem | transports dissolved sugars (sucrose) from leaves | OK | — | 4.2.3.2 |
| C17 | T3 phloem | "Living cells with little cytoplasm"; sieve plates; companion cells provide ATP for active loading | OFF-SPEC | True, but "detailed structure of phloem tissue or the mechanism of transport is not required". Spec content: tubes of elongated cells; sap moves through pores in the end walls. F6. | 4.2.3.2 |
| C18 | T3 palisade | many chloroplasts; top of leaf; column shape | OK | — | 4.2.3.1 |
| C19 | common_mistake | water enters by osmosis, mineral ions by active transport | OK | Spec wording. | 4.2.3.2 |
| C20 | key_note | as above | OK | — | 4.1.1.4 |
| C21 | q1 key | many mitochondria → ATP energy for flagellum | OK | "ATP" off-spec (F7). | 4.1.1.3 |
| C22 | q1 wx1–wx3 | acrosome digests; sperm small and streamlined; DNA in nucleus, mitochondria have a little DNA | OK | Paired correctly. | — |
| C23 | q2 key | no nucleus → more space for haemoglobin → more oxygen | OK | — | 4.2.2.3 |
| C24 | q2 wx1 (opt 1 "cannot be destroyed by white blood cells") | "red blood cell lifespan (~120 days) is determined by membrane wear — not by whether they have a nucleus" | IMPRECISE | Does not rebut the option. Old red blood cells ARE removed by phagocytes (in the spleen and liver), so the option is false for that reason. F1. | — |
| C25 | q2 wx2 | cells without a nucleus cannot divide; RBCs made in bone marrow | OK | — | 4.1.2.3 |
| C26 | q2 wx3 | "Red blood cells actually have very few mitochondria and mainly use anaerobic respiration." | **WRONG** | Mature human red blood cells have **no** mitochondria and respire **only** anaerobically. F1. | — |
| C27 | q3 key | underground, no light | OK | — | — |
| C28 | q3 wx1–wx3 | size not the reason; chloroplasts don't block water; plant cells are eukaryotic | OK | Paired correctly. | 4.1.1.1 |
| C29 | q4 key | dead and hollow, continuous water column | OK | — | 4.2.3.2 |
| C30 | q4 wx1 (opt 1 "many chloroplasts … energy for pumping water") | "Chloroplasts would only be present if the xylem cell was exposed to light …" | **WRONG** | Xylem cells are dead and contain no organelles whatever the light; and water moves up xylem passively in the transpiration stream — no cell pumps it. The explanation implies a lit xylem cell would have chloroplasts. F2. | 4.2.3.2 |
| C31 | q4 wx2 | xylem doesn't store water; vacuoles in living cells | OK | — | — |
| C32 | q4 wx3 | xylem walls thick, lignified, resist tension | OK | — | 4.2.3.2 |
| C33 | matching (to be replaced) | six pairs | OK | — | — |

Count: **3 WRONG** (C8 theory — re-cuttable; C26 → q2; C30 → q4); IMPRECISE: C5, C13, C24; OFF-SPEC: C17; GAP: C14, C3.

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| q2 | wx3 says RBCs have "very few mitochondria" (they have none); wx1 does not rebut its option. | **Do not use as written** (F1). |
| q4 | wx1 implies a lit xylem cell would have chloroplasts and leaves "pumping" unrebutted. | **Do not use as written** (F2). |
| q1, q3 | Correct and correctly paired. | Usable on all four routes. |

## 5. Verdict
SOURCE HAS ERRORS. The six spec cells are all present and the structure–function links are sound, but the neurone "brain to toe" claim is false, and two frozen quiz items (q2, q4) carry wrong explanations. Root hair cells need their mitochondria/active-transport point and lose the A-level "water potential" wording; phloem detail exceeds the spec. Nothing for Mide.
