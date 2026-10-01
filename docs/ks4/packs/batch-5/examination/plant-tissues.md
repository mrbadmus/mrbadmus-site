# Examination — Plant Tissues and Organs (plant-tissues) — AQA 8464 4.2.3.1 / 8461 4.2.3.1
Verdict: SOURCE OK WITH FLAGS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-5/04-checked-science-source/biology-4.2.5-plant-tissues.md`.
Spec sources read as text: `AQA-8464-spec.txt` (Combined Trilogy v1.1, 4.2.3 Plant tissues, organs and systems: 4.2.3.1, 4.2.3.2; 4.1.2.3 stem cells), `AQA-8461-spec.txt` (Biology v1.0, same sections). Route audit row `plant-tissues` (OK, CF CH TF TH, 4.2.3.1). Sibling lessons on the site: `transpiration` and `translocation` (both 8464/8461 4.2.3.2). Runtime convention checked in `generate_site_v5.py`: `wrong_explanations` key n is shown for `opts[n]`.

**Spec reference settled.** The frozen spec field "4.2.5" is the site's internal numbering, not an AQA reference: neither 8464 nor 8461 has a 4.2.5 in Organisation. The true AQA reference is **4.2.3.1 Plant tissues** in both 8464 and 8461 (BATCH-PLAN and the route audit are right). Xylem/phloem adaptation and stomata/guard-cell function sit in **4.2.3.2 Plant organ system**, which this lesson borrows from and which has its own lessons. No conflict between AQA sources.

Conventions: q1–q3 = quiz items; "wx n" = `wrong_explanations` key n, shown for `opts[n]`; T1–T4 = theory blocks. Route copies identical except `higher`, which is `null` on CF and TF.

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 | **4.2.3.1** | Plant tissues | base |
| 8461 | **4.2.3.1** | Plant tissues | base |
| Supporting | 4.2.3.2 Plant organ system (xylem, phloem, stomata, guard cells — own lessons `transpiration`, `translocation`); 4.1.2.3 stem cells (meristem) | | base |

Spec statements (verbatim, 8464 = 8461), 4.2.3.1: "Students should be able to explain how the structures of plant tissues are related to their functions. Plant tissues include: epidermal tissues; palisade mesophyll; spongy mesophyll; xylem and phloem; meristem tissue found at the growing tips of shoots and roots. The leaf is a plant organ. Knowledge limited to epidermis, palisade and spongy mesophyll, xylem and phloem, and guard cells surrounding stomata." Skills: "AT 7 Observation and drawing of a transverse section of leaf."
4.2.3.2 (supporting): "Xylem tissue transports water and mineral ions from the roots to the stems and leaves. It is composed of hollow tubes strengthened by lignin adapted for the transport of water in the transpiration stream. The role of stomata and guard cells are to control gas exchange and water loss. Phloem tissue transports dissolved sugars from the leaves to the rest of the plant for immediate use or storage. The movement of food molecules through phloem tissue is called translocation. Phloem is composed of tubes of elongated cells. Cell sap can move from one phloem cell to the next through pores in the end walls. Detailed structure of phloem tissue or the mechanism of transport is not required."
4.1.2.3 (supporting): "Meristem tissue in plants can differentiate into any type of plant cell, throughout the life of the plant."

## 2. Route table
| # | teachable point | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Plant organs: leaf, stem, root, flower; organs made of tissues (T1) | base | 4.2.3.1; 4.2.3.2 ("roots, stem and leaves form a plant organ system") | all four | OK |
| R2 | Epidermis; waxy cuticle reduces water loss (T2; matching) | base | 4.2.3.1 | all four | OK |
| R3 | Palisade mesophyll: near top, many chloroplasts, main photosynthesis site (T2) | base | 4.2.3.1 | all four | OK |
| R4 | Spongy mesophyll: air spaces for CO₂/O₂ diffusion (T2) | base | 4.2.3.1 | all four | OK |
| R5 | Guard cells and stomata; open/close; gas exchange and water loss (T2; key_note; q3) | base | 4.2.3.1; 4.2.3.2 | all four | OK (one imprecision, C7) |
| R6 | Xylem and phloem in vascular bundles (T2) | base | 4.2.3.1 | all four | OK |
| R7 | Xylem: water + mineral ions upwards; dead, hollow, no end walls, lignin; transpiration stream (T3; common_mistake; key_note; q1; q2) | base | 4.2.3.1; 4.2.3.2 | all four | OK |
| R8 | Phloem: dissolved sugars, translocation, living cells, both directions, pores/sieve plates in end walls (T4; key_note) | base | 4.2.3.2 | all four | OK |
| R9 | Companion cells supply ATP for active loading (T4) | **OFF-SPEC** | 4.2.3.2 ("detailed structure of phloem tissue or the mechanism of transport is not required") | all four | Do not teach (PLANT-TISSUES-F2) |
| R10 | Meristem tissue at growing tips of shoots and roots | base | 4.2.3.1; 4.1.2.3 | — (absent) | **GAP — spec core missing** (PLANT-TISSUES-F1) |
| R11 | `higher`: cohesion-tension theory | OFF-SPEC (A-level) | — | CH TH only | **ROUTE** (F3) |
| R12 | `higher`: measuring transpiration rate with a potometer | base (4.2.3.2 AT 3–5 skills) — `transpiration` lesson | 4.2.3.2 | CH TH only | **ROUTE** (F3) — not HT, not this lesson |
| R13 | `higher`: active loading at source, pressure gradient to sinks | OFF-SPEC (spec excludes the mechanism) | 4.2.3.2 | CH TH only | **ROUTE** (F3) |
| — | RP, equations, FIFA | none | — | — | correct: 4.2.3 has no HT, no biology-only content, no RP |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | T1 | leaf = photosynthesis + gas exchange; stem = support + transport; root = anchor + absorb water and mineral ions; flower = reproduction | OK | — | 4.2.3.1–2 |
| C2 | T2 | epidermis thin, transparent; produces waxy cuticle, waterproof, reduces water loss | OK | "Transparent" is true of the upper epidermis (light passes to the palisade). | 4.2.3.1 |
| C3 | T2 | palisade cells tall, column-shaped, many chloroplasts, near upper surface, maximum light | OK | — | 4.2.3.1 |
| C4 | T2 | spongy mesophyll loosely arranged with air spaces; CO₂ diffuses in, O₂ diffuses out | OK | — | 4.2.3.1 |
| C5 | T2 | stomata on the lower leaf surface | IMPRECISE (minor) | "mostly on the lower surface" — most leaves have some on the upper surface too. | — |
| C6 | T2 | stomata let CO₂ in, O₂ and water vapour out | OK | Spec: "control gas exchange and water loss". | 4.2.3.2 |
| C7 | T2 | in light guard cells take up water, turgid → open; dark or dehydrated → lose water → close | OK | GCSE-level account; the mechanism (ions, osmosis) is not required. | 4.2.3.2 |
| C8 | T2 | xylem brings water to the leaf; phloem takes sugars away | OK | — | 4.2.3.2 |
| C9 | T3 | xylem transports water and dissolved mineral ions from roots up to leaves | OK | Spec: "from the roots to the stems and leaves". | 4.2.3.2 |
| C10 | T3 | xylem dead, no cytoplasm or nucleus, hollow; no end walls; continuous column | OK | Spec: "hollow tubes". | 4.2.3.2 |
| C11 | T3 | walls strengthened with lignin, hard, waterproof, prevents collapse | OK | Spec: "strengthened by lignin". | 4.2.3.2 |
| C12 | T3 | water moves one way only — upwards | OK | — | 4.2.3.2 |
| C13 | T3 | evaporation from leaves pulls water up — transpiration stream | OK | — | 4.2.3.2 |
| C14 | T4 | phloem transports dissolved sugars (mainly sucrose) from leaves to other parts; translocation | OK | — | 4.2.3.2 |
| C15 | T4 | phloem cells living | OK | — | — |
| C16 | T4 | sieve tubes with perforated end walls (sieve plates) | OK | Spec: "pores in the end walls". "Sieve plates" is beyond what is required; harmless. | 4.2.3.2 |
| C17 | T4 | companion cells provide ATP for active loading of sugars | **OFF-SPEC** | Science correct, but the spec says "Detailed structure of phloem tissue or the mechanism of transport is not required." | 4.2.3.2 |
| C18 | T4 | sugars travel in both directions, source to sinks | OK | Consistent with "to the rest of the plant for immediate use or storage". "Source/sink" is extension vocabulary. | 4.2.3.2 |
| C19 | `higher` | cohesion-tension theory | OFF-SPEC; ROUTE | A-level. Not HT GCSE. | — |
| C20 | `higher` | measure transpiration rate using a potometer | OK science; ROUTE | Base skills point of 4.2.3.2 ("measure the rate of transpiration by the uptake of water"); belongs to `transpiration`. | 4.2.3.2 |
| C21 | `higher` | active loading of sucrose → pressure gradient source to sink | OFF-SPEC; ROUTE | Mass-flow mechanism; spec excludes it. | 4.2.3.2 |
| C22 | common_mistake | xylem = water + minerals; phloem = sugars; xylem dead, phloem living | OK | The memory trick ("X for H2O is a stretch…") is weak but not false; Design need not reuse it. | 4.2.3.2 |
| C23 | key_note | xylem: water + minerals, upwards, dead, lignified; phloem: sugars, both ways, living; stomata: CO₂ in, O₂ and water vapour out, guard cells | OK | "CO₂ in, O₂ out" is the daytime picture; in the dark the leaf only respires. Fine for this lesson. | 4.2.3.2 |
| C24 | q1 | xylem transports water and dissolved mineral ions, upwards | OK | Key correct; wx1–wx3 paired correctly (phloem; O₂ via air spaces; CO₂ via stomata). | 4.2.3.2 |
| C25 | q2 | xylem cells dead → hollow tube, unobstructed flow | OK | Key correct; wx1 (lignin not toxic), wx2 (weight), wx3 (die as they mature) paired correctly and true. | 4.2.3.2 |
| C26 | q3 key | stomata let CO₂ in and O₂ out; water vapour escapes | OK | — | 4.2.3.2 |
| C27 | q3 wx1 | "Stomata can absorb some water vapour in humid conditions, but their primary function is gas EXCHANGE…" | IMPRECISE | The first clause is a needless, doubtful concession (water uptake into leaves is minor and is not mainly via stomata). The rebuttal itself is right. Usable. | — |
| C28 | q3 wx2 | waxy cuticle produced by the epidermis | OK | — | 4.2.3.1 |
| C29 | q3 wx3 | starch stored in chloroplasts and other cells; stomata are pores | OK | — | — |
| C30 | matching (to be replaced) | six tissue → function pairs | OK | All correct. | 4.2.3.1–2 |
| C31 | spec field | "4.2.5" | WRONG (ref) | AQA 8464/8461 **4.2.3.1** (PLANT-TISSUES-F4). | — |

Count: **0 WRONG science**; 1 wrong spec reference (C31); OFF-SPEC: C17, C19, C21; IMPRECISE: C5, C27. Spec core gap: meristem.

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| none | q1, q2, q3 correct and base | **All three usable on all four routes** (q1 Recall, q2 Explain, q3 Recall). q3 wx1 imprecise but its rebuttal is right (C27). |

## 5. Convert lines
None in this file (no calculations).

## 6. Verdict
SOURCE OK WITH FLAGS. All tissue science is right and all three quiz items are usable on every route. Four things to fix: meristem tissue, which is in the spec, is missing (added to the source from the spec); the companion-cell/ATP detail is beyond the spec; the `higher` field has no HT content (A-level theory plus a base skills point from `transpiration`), so nothing in this lesson is HT; and the spec field "4.2.5" should read AQA 4.2.3.1. Nothing for Mide.
