# Examination — Electronic Structure (electronic-structure) — AQA 8464 5.1.1.7 / 8462 4.1.1.7
Verdict: SOURCE OK WITH FLAGS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-11/04-checked-science-source/chemistry-5.1.1.7-electronic-structure.md`.
Spec sources read as text: `AQA-8464-spec.txt` (v1.1) 5.1.1.7, 5.1.2.1, 5.1.2.3, 5.1.2.4; `AQA-8462-spec.txt` (v1.1) 4.1.1.7, 4.1.2.1, 4.1.2.3, 4.1.2.4. No equation sheet applies. Route audit row `electronic-structure`: base, OK.

Conventions: as in model-of-the-atom. Route copies identical except `higher`: TH text on CH/TH, `null` on CF/TF.

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 | **5.1.1.7** | Electronic structure | base |
| 8462 | **4.1.1.7** | Electronic structure | base |
| Supporting | 8464 5.1.2.1 / 8462 4.1.2.1 (same group = same outer electrons; position ↔ electron arrangement); 5.1.2.3 / 4.1.2.3 (metals form positive ions); 5.1.2.4 / 4.1.2.4 (noble gases) | | base |

Spec statements (verbatim, 8464 = 8462):
- 5.1.1.7: "The electrons in an atom occupy the lowest available energy levels (innermost available shells). The electronic structure of an atom can be represented by numbers or by a diagram. For example, the electronic structure of sodium is 2,8,1 or [diagram] showing two electrons in the lowest energy level, eight in the second energy level and one in the third energy level. Students may answer questions in terms of either energy levels or shells." "Students should be able to represent the electronic structures of the first twenty elements of the periodic table in both forms."
- 5.1.2.1: "Elements in the same group in the periodic table have the same number of electrons in their outer shell (outer electrons) and this gives them similar chemical properties." "Students should be able to: • explain how the position of an element in the periodic table is related to the arrangement of electrons in its atoms and hence to its atomic number • predict possible reactions and probable reactivity of elements from their positions in the periodic table."
- 5.1.2.4: "The noble gases have eight electrons in their outer shell, except for helium, which has only two electrons."

## 2. Route table
| # | teachable point (pack location) | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Lowest available levels fill first; 2, 8, 8 for Z ≤ 20 (th1; common_mistake; key_note) | base | 5.1.1.7 | all four | OK |
| R2 | Numbers notation (2.8.1) (th1; th2; key_note) | base | 5.1.1.7 | all four | OK; spec writes commas (F3) |
| R3 | Diagram form (dots/crosses on circles) | base | 5.1.1.7 "in both forms" | — | GAP (F3) |
| R4 | Configurations H–Ca (th2) | base | 5.1.1.7 | all four | OK (all 20 checked) |
| R5 | Same group = same outer electrons = similar chemistry (th3; q2; key_note) | base | 5.1.2.1 | all four | OK |
| R6 | Group 0 full outer shell, unreactive (th3) | base | 5.1.2.4 | all four | IMPRECISE: helium (F2) |
| R7 | Metals lose / non-metals gain or share electrons (th3) | base | 5.1.2.3; 5.2.1 | all four | OK |
| R8 | `higher`: configs 1–20; predict from structure; period = shells, group = outer electrons | **base** (no HT in 5.1.1.7 or 5.1.2.1) | 5.1.1.7; 5.1.2.1 | CH TH only | ROUTE (F1) |
| R9 | q1 group from 2.8.6 | base | 5.1.2.1 | all four | OK (F4 note) |
| R10 | q2 Li and Na similar | base | 5.1.2.1 | all four | OK |
| — | FIFA, equations, RP | none | — | — | correct |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | th1 | electrons fill from innermost (lowest energy) shell | OK | Spec: "lowest available energy levels (innermost available shells)". | 5.1.1.7 |
| C2 | th1 | capacities 2, 8, 8 for first 20 | OK | The GCSE model. | 5.1.1.7 |
| C3 | th1 | Na: 2.8.1 | OK | Spec writes "2,8,1". AQA accepts dots or commas (F3). | 5.1.1.7 |
| C4 | th2 | H 1, He 2, Li 2.1, Be 2.2, B 2.3, C 2.4, N 2.5, O 2.6, F 2.7, Ne 2.8, Na 2.8.1, Mg 2.8.2, Al 2.8.3, Si 2.8.4, P 2.8.5, S 2.8.6, Cl 2.8.7, Ar 2.8.8, K 2.8.8.1, Ca 2.8.8.2 | OK | All 20 checked ✓ (each sums to Z). | 5.1.1.7 |
| C5 | th2 | 4th shell starts at K because the 3rd fills to 8 first | OK | Right within the GCSE model. | 5.1.1.7 |
| C6 | th3 | outer electrons decide chemical properties; same group same number | OK | — | 5.1.2.1 |
| C7 | th3 | Group 1 Li 2.1, Na 2.8.1, K 2.8.8.1; Group 7 F 2.7, Cl 2.8.7 | OK | ✓ | — |
| C8 | th3 | "Group 0: 8 outer electrons (full shell) — He: 2, Ne: 2.8, Ar: 2.8.8" | IMPRECISE | The heading says 8 and then lists He with 2. Spec: "eight… except for helium, which has only two". Say so (F2). | 5.1.2.4 |
| C9 | th3 | metals lose electrons → positive ions; non-metals gain or share | OK | — | 5.1.2.3 |
| C10 | th3 | noble gases full outer shells → very unreactive | OK | Spec: "stable arrangements of electrons". | 5.1.2.4 |
| C11 | `higher` | configurations 1–20; period = number of shells; group = outer electrons | ROUTE | All true and all **base**. 5.1.1.7 and 5.1.2.1 have no HT label. Teach on every route (F1). | 5.1.1.7; 5.1.2.1 |
| C12 | common_mistake | fill in order; 3rd shell up to 8 before the 4th for Z ≤ 20 | OK | — | 5.1.1.7 |
| C13 | key_note | 2, 8, 8; dot notation; same group similar chemistry; full outer shell stable | OK | — | — |
| C14 | matching (to be replaced) | Na 2.8.1; Cl 2.8.7; Ca 2.8.8.2; Ne 2.8; Mg 2.8.2 | OK | ✓ | — |
| C15 | q1 key (opt 0) | 2.8.6 → Group 6 | OK | Sulfur. ✓ | 5.1.2.1 |
| C16 | q1 wx1 ↔ opt 1 "Group 2 — 2 complete shells below" | complete inner shells relate to the period (2 inner → Period 3); groups come from outer electrons | OK, aligned ✓ | — | 5.1.2.1 |
| C17 | q1 wx2 ↔ opt 2 "Group 16 — add all electrons" | 16 is the total = atomic number, not the group | OK, aligned ✓ | Note: sulfur's IUPAC group number **is** 16. On the AQA periodic table (groups 1–7 and 0) the item is right, and the option's reasoning ("add all the electrons") is wrong either way. Usable (F4). | 5.1.2.1 |
| C18 | q1 wx3 ↔ opt 3 "Period 3 — 3 shells" | shells → period; group → outer electrons (6) | OK, aligned ✓ | The option is a true fact that answers a different question. A fair distractor. | 5.1.2.1 |
| C19 | q2 key (opt 0) | both 1 outer electron, react similarly | OK | — | 5.1.2.1 |
| C20 | q2 wx1 ↔ opt 1 "same total electrons" | Li 3, Na 11 | OK, aligned ✓ | — | — |
| C21 | q2 wx2 ↔ opt 2 "same period" | Li Period 2, Na Period 3 | OK, aligned ✓ | — | — |
| C22 | q2 wx3 ↔ opt 3 "same mass number" | Li 7, Na 23 | OK, aligned ✓ | — | — |

Count: **0 WRONG**. IMPRECISE: C8, C17 (note only). ROUTE: C11. GAP: R3. All six wrong_explanations are aligned, checked by reading each one.

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| q1 | — | Usable on all four routes. |
| q2 | — | Usable on all four routes. |

## 5. For the lesson author
**Misconceptions seen in AQA marking**
- More than 8 in the third shell for K or Ca, e.g. "2,8,9".
- Group read as the number of shells, or period read as the number of outer electrons (q1 opt 3).
- Electron diagrams with the wrong total, or electrons drawn inside the nucleus.
- "Helium is in Group 2 because it has 2 outer electrons."
- "Same group because same number of shells."

**Command words**: Give the electronic structure, Draw the electronic structure (diagram), Explain why elements in the same group have similar properties, Explain how the position of an element relates to its electrons.

**Typical questions** ⚑ examiner-drafted
- *Give the electronic structure of aluminium. [1]*: 2,8,3.
- *Complete the diagram to show the electronic structure of a sulfur atom. [1]*: 2, 8, 6 on three circles.
- *Element X has electronic structure 2,8,8,2. Give the group and period of X. [2]*: Group 2 (1); Period 4 (1).
- *Explain why lithium and potassium have similar chemical properties. [2]*: both have one electron in the outer shell (1); so react in a similar way / both lose one electron (1).

**Required practical**: none. **Equations**: none.

## 6. Verdict
SOURCE OK WITH FLAGS. All 20 configurations and both frozen quiz items are correct; both items are usable on all four routes. The `higher` field holds base content (no HT in 5.1.1.7 or 5.1.2.1), so it must reach Foundation pupils too. Gap: the spec's diagram form of electronic structure. Imprecise: Group 0 "8 outer electrons" alongside helium's 2.

**For Mide:** nothing.
