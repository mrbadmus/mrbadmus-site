# Examination — Stem Cells (stem-cells) — AQA 8464 4.1.2.3 / 8461 4.1.2.3
Verdict: SOURCE HAS ERRORS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-6/04-checked-science-source/biology-4.1.2.3-stem-cells.md`.
Spec sources read as text: `AQA-8464-spec.txt` (Combined Trilogy v1.1, 4.1.2.3; 4.1.1.4 differentiation; 4.2.3.1 meristem tissue), `AQA-8461-spec.txt` (Biology v1.0, same; text identical). Neither spec uses "totipotent", "pluripotent" or "multipotent" (grep). Route audit row `stem-cells` (OK, CF CH TF TH). Runtime convention checked in `generate_site_v5.py` (`render_quiz`): `wrong_explanations` key n is shown for `opts[n]` (0-based).

Conventions: q1–q4 = quiz items; "wx n" = `wrong_explanations` key n, shown for `opts[n]`; T1–T5 = theory blocks. Route copies: only `higher` differs (CF = null, TF = null). No `[NEW — to be examined]` lines (no FIFA). **wx alignment checked: all four items correctly keyed (wx n addresses opt n); no one-option-late shift.** One explanation is wrong in content (F2).

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 / 8461 | **4.1.2.3** | Stem cells | base — no HT or biology-only sentence |
| Supporting | 4.1.1.4 Cell differentiation; 4.2.3.1 meristem tissue | | base |

Spec statements (verbatim, 8464 = 8461): "A stem cell is an undifferentiated cell of an organism which is capable of giving rise to many more cells of the same type, and from which certain other cells can arise from differentiation. Students should be able to describe the function of stem cells in embryos, in adult animals and in the meristems in plants. Stem cells from human embryos can be cloned and made to differentiate into most different types of human cells. Stem cells from adult bone marrow can form many types of cells including blood cells. Meristem tissue in plants can differentiate into any type of plant cell, throughout the life of the plant. Knowledge and understanding of stem cell techniques are not required. Treatment with stem cells may be able to help conditions such as diabetes and paralysis. In therapeutic cloning an embryo is produced with the same genes as the patient. Stem cells from the embryo are not rejected by the patient's body so they may be used for medical treatment. The use of stem cells has potential risks such as transfer of viral infection, and some people have ethical or religious objections. Stem cells from meristems in plants can be used to produce clones of plants quickly and economically. Rare species can be cloned to protect from extinction. Crop plants with special features such as disease resistance can be cloned to produce large numbers of identical plants for farmers." Skills: "WS 1.3 Evaluate the practical risks and benefits, as well as social and ethical issues, of the use of stem cells in medical research and treatments."

## 2. Route table
| # | teachable point | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Stem cell = undifferentiated; divides to make more; can differentiate (T1) | base | 4.1.2.3 | all four | OK |
| R2 | Embryonic stem cells: most cell types; from IVF embryos; uses (T2; q3) | base | 4.1.2.3 | all four | **WRONG** "totipotent" (F1); q3 WRONG (F2) |
| R3 | Diabetes and paralysis treatments (T2) | base | 4.1.2.3 | all four | OK |
| R4 | Adult bone-marrow stem cells → blood cells; leukaemia transplant (T3; q2) | base | 4.1.2.3 | all four | OK (F6) |
| R5 | Plant meristems: any plant cell, throughout life; cloning rare species and crops (T4; q4) | base | 4.1.2.3; 4.2.3.1 | all four | OK |
| R6 | Ethical and religious objections; HFEA 14-day rule (T5; q3) | base | 4.1.2.3 WS 1.3 | all four | OK |
| R7 | Therapeutic cloning: embryo with the patient's genes, not rejected (`higher`) | **base** (no HT label) | 4.1.2.3 | CH TH only (CF, TF = null) | **ROUTE** (F4) |
| R8 | Risk: transfer of viral infection (`higher`) | **base** | 4.1.2.3 | CH TH only | **ROUTE** (F4) |
| R9 | Nucleus inserted into an enucleated egg (`higher`) | not required ("techniques are not required") | 4.1.2.3 | CH TH | OK as optional detail; not a route layer |
| R10 | totipotent / multipotent vocabulary (T2–T4; common_mistake; key_note; q1, q4) | not in spec | — | all four | OFF-SPEC (F3); wrongly applied to embryonic cells (F1) |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | T1 | undifferentiated; self-renewal by mitosis; differentiation | OK | Matches spec definition. | 4.1.2.3 |
| C2 | T1 | role in development and repair | OK | — | 4.1.1.4 |
| C3 | T2 | inner cell mass of a "3–5 days old" embryo, a blastocyst | IMPRECISE | The blastocyst forms at about 5 days; at 3–4 days the embryo is a morula. Say "about 5 days". F5. | — |
| C4 | T2 | "They are TOTIPOTENT — they can differentiate into ANY of the more than 200 cell types" | **WRONG** | Embryonic stem cells from the inner cell mass are pluripotent: they form most body cell types but not the placenta. Only the zygote and the earliest cells are totipotent. AQA: "differentiate into most different types of human cells". F1. | 4.1.2.3 |
| C5 | T2 | "more than 200 cell types" | OK | Standard figure. | — |
| C6 | T2 | embryo destroyed; usually spare IVF embryos | OK | — | — |
| C7 | T2 | uses: type 1 diabetes, Parkinson's, spinal injury, heart muscle, skin | OK | Spec: "may be able to help … diabetes and paralysis". | 4.1.2.3 |
| C8 | T2 | challenges: rejection; tumour risk | OK | Spec risk "transfer of viral infection" is missing here (only in `higher`, F4). | 4.1.2.3 |
| C9 | T3 | adult stem cells "can only differentiate into the cell types found in the tissue where they live"; multipotent | IMPRECISE | Spec: bone marrow stem cells "can form many types of cells including blood cells". Keep "a limited range of cell types". F6. | 4.1.2.3 |
| C10 | T3 | bone marrow → red cells, white cells, platelets; leukaemia transplant after chemo/radiotherapy | OK | — | 4.1.2.3 |
| C11 | T3 | adult cells: "no ethical controversy"; autologous | IMPRECISE | "Fewer ethical objections" — donor consent and risk are still issues. F6. | WS 1.3 |
| C12 | T4 | meristems at root and shoot tips; lateral meristems thicken stems | OK | Lateral meristems beyond spec, true. | 4.2.3.1 |
| C13 | T4 | meristem cells can become any plant cell; growth throughout life | OK | Spec wording. | 4.1.2.3 |
| C14 | T4 | cloning by tissue culture; rare species; disease-resistant crops; quick | OK | — | 4.1.2.3 |
| C15 | T5 | arguments for and against; HFEA; research to 14 days | OK | HFEA 14-day limit ✓. | WS 1.3 |
| C16 | `higher` | therapeutic cloning: patient's nucleus into enucleated egg → embryo genetically identical → no rejection; viral risk; objections; meristems | OK (science) / **ROUTE** | All base in the spec; Foundation copies are null. F4. Nucleus transfer is a technique (not required). | 4.1.2.3 |
| C17 | common_mistake | stem cells don't "replace organs", they make specific cell types | OK | — | — |
| C18 | common_mistake | "embryonic stem cells are TOTIPOTENT (any cell type). Adult stem cells are MULTIPOTENT" | **WRONG** | As C4. F1. | 4.1.2.3 |
| C19 | key_note | "Embryonic stem cells: totipotent (any cell type)" | **WRONG** | As C4. F1. | 4.1.2.3 |
| C20 | q1 key | totipotent = can differentiate into any type of cell in the organism | OK (OFF-SPEC term) | The definition is correct; the term is not in AQA. F3. | — |
| C21 | q1 wx1–wx3 | one tissue = multipotent; dividing indefinitely = self-renewal; specialised cells aren't stem cells | OK | Paired correctly. | — |
| C22 | q2 key | bone marrow transplant: cancerous cells destroyed, donor stem cells make healthy blood cells | OK | — | 4.1.2.3 |
| C23 | q2 wx1–wx3 | adult not embryonic; antibodies are a different therapy; stem cells don't repair DNA | OK | Paired correctly. | 8461 4.3.2 (biology only) (HT only) — only named |
| C24 | q3 key | embryo destroyed — potential human life | OK | — | 4.1.2.3 |
| C25 | q3 wx1 | cancer risk is technical, not ethical | OK | — | — |
| C26 | q3 wx2 (opt 2 "ineffective at treating disease") | "Embryonic stem cells are actually MORE effective than adult stem cells because they are totipotent" | **WRONG** | They are not totipotent (C4), and "more effective" is unsupported: they can form more cell types, and few treatments using them are yet established. F2. | 4.1.2.3 |
| C27 | q3 wx3 | cost a challenge; the controversy is ethical | OK | — | — |
| C28 | q4 key | meristem cells can form any plant cell; adult animal stem cells a limited range | OK | Matches spec ("any type of plant cell" vs "many types"). Uses off-spec terms (F3). | 4.1.2.3 |
| C29 | q4 wx1–wx3 | opposite; meristems in specific regions (root tips, shoot tips, cambium); potency differs | OK | Paired correctly. | 4.2.3.1 |
| C30 | matching (to be replaced) | "Embryonic stem cell — Totipotent" pair | WRONG | As C4; being replaced anyway. | — |

Count: **2 WRONG items/fields** — the totipotent claim (C4, C18, C19, C30: theory, common_mistake, key_note — all re-cuttable) and q3 wx2 (C26); IMPRECISE: C3, C9, C11; ROUTE: C16.

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| q3 | wx2 calls embryonic stem cells totipotent and "more effective". | **Do not use as written** (F2). |
| q1 | Correct definition of an off-spec term; the source attaches the term wrongly to embryonic cells. | Usable only if the page teaches "totipotent" correctly (meristems / zygote); otherwise skip. Not a core rung (F3). |
| q2, q4 | Correct and paired correctly. | Usable on all four routes. |

## 5. Verdict
SOURCE HAS ERRORS. Adult, embryonic and meristem stem cells, leukaemia transplants, plant cloning and the ethics are right. But the source calls embryonic stem cells "totipotent" in the theory, common_mistake, key_note and matching — they are pluripotent, and AQA says only "most different types of human cells" — and q3's wx2 repeats it. Therapeutic cloning and the viral-infection risk are base spec content, but they sit only in the `higher` field, which is null on both Foundation routes. Nothing for Mide.
