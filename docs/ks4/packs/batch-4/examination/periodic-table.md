# Examination — The Periodic Table (periodic-table) — AQA 8464 5.1.2.1 / 8462 4.1.2.1
Verdict: SOURCE OK WITH FLAGS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-4/04-checked-science-source/chemistry-5.1.2.1-periodic-table.md`.
Spec sources read as text: `AQA-8464-spec.txt` (v1.1, 04 Oct 2019) 5.1.1.7, 5.1.2.1–5.1.2.6; `AQA-8462-spec.txt` (v1.1, 04 Oct 2019) 4.1.2.1–4.1.2.6, 4.1.3.1–4.1.3.2. Route audit `ks4-routes/docs/ks4/route-audit/chemistry.md` rows `periodic-table` (base) and `transition-metals` (chem-only, TF TH).

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n (= opts index n). T1–T3 = theory chunks. Only the `higher` field has route copies (CF, TF = null).

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 | **5.1.2.1** | The periodic table | base |
| 8462 | **4.1.2.1** | The periodic table | base |
| Supporting | 8464 5.1.1.7 / 8462 4.1.1.7 electronic structure; 5.1.2.3 / 4.1.2.3 metals and non-metals; 5.1.2.4–5.1.2.6 / 4.1.2.4–4.1.2.6 Groups 0, 1, 7 | | base |
| Supporting | 8462 **4.1.3.1–4.1.3.2** Properties of transition metals | | **(chemistry only)** |

Spec statements (verbatim, 8464 = 8462): "The elements in the periodic table are arranged in order of atomic (proton) number and so that elements with similar properties are in columns, known as groups. The table is called a periodic table because similar properties occur at regular intervals. Elements in the same group in the periodic table have the same number of electrons in their outer shell (outer electrons) and this gives them similar chemical properties." Students should be able to: "explain how the position of an element in the periodic table is related to the arrangement of electrons in its atoms and hence to its atomic number"; "predict possible reactions and probable reactivity of elements from their positions in the periodic table." (WS 1.2)

8462 4.1.3 (chemistry only): "The transition elements are metals with similar properties which are different from those of the elements in Group 1 … describe the difference compared with Group 1 in melting points, densities, strength, hardness and reactivity with oxygen, water and halogens … exemplify … by reference to Cr, Mn, Fe, Co, Ni, Cu." 4.1.3.2: "Many transition elements have ions with different charges, form coloured compounds and are useful as catalysts."

## 2. Route table
| # | teachable point | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Arranged by atomic number; groups; "periodic" (T1; key_note) | base | 5.1.2.1 | all four | OK |
| R2 | Period number = number of shells (T1; common_mistake; q1) | base | 5.1.2.1; 5.1.1.7 | all four | OK (C3 minor) |
| R3 | Group number = outer electrons; same group → similar properties (T1; common_mistake; q2) | base | 5.1.2.1 | all four | OK |
| R4 | Group 0 full outer shell (8; 2 for He) (T1) | base | 5.1.2.4 | all four | OK |
| R5 | Metals left/centre, non-metals top right (T1) | base | 5.1.2.3 | all four | OK |
| R6 | Metalloids (Si, Ge) (T1) | off-spec context | — | all four | OK (true) |
| R7 | Trends across a period (T2) | base | 5.1.2.1; 5.1.2.3 | all four | OK |
| R8 | Down a group: more shells; metals more reactive, non-metals less reactive (T2) | base | 5.1.2.1; 5.1.2.5; 5.1.2.6 | all four | IMPRECISE (C9) |
| R9 | Predict properties from position (T2; `higher`) | base | 5.1.2.1 (WS 1.2) | all four | OK |
| R10 | Transition metals: position, properties, coloured compounds, catalysts, ions of different charge, comparison with Group 1 (T3) | **triple** | 8462 4.1.3.1–4.1.3.2 (chemistry only) | all four | **ROUTE** — shipped to Combined (C11) |
| R11 | `higher`: Group 1/7 trend explanations; predict unknown elements | **base**, not HT | 5.1.2.5; 5.1.2.6 | TH, CH only (CF/TF null) | **ROUTE** (C15) |
| R12 | `higher`: "lower ionisation energy" | off-spec | — | TH, CH | OFF-SPEC (C15) |
| R13 | q1, q2 | base | 5.1.2.1 | all four | OK — usable on all routes |
| — | RP, FIFA, equations, examiner_tip | none | — | — | correct: none on spec |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | T1 | arranged in order of increasing atomic number | OK | — | 5.1.2.1 |
| C2 | T1 | rows = periods, columns = groups; same group → same outer electrons, similar properties | OK | — | 5.1.2.1 |
| C3 | T1 | "each period represents a new electron shell being filled" | IMPRECISE (minor) | True for Periods 1–3, which is all GCSE asks (5.1.1.7: first 20 elements). Safer: "the period number is the number of occupied shells". | 5.1.1.7 |
| C4 | T1 | Period 1: H, He; Period 2: Li–Ne; Period 3: Na–Ar | OK | — | — |
| C5 | T1 | Group 1: 1 outer electron; Group 7: 7; Group 0: 8, or 2 for He | OK | — | 5.1.2.4 |
| C6 | T1 | metals left and centre, most elements are metals; non-metals top right | OK | Spec: metals "to the left and towards the bottom". | 5.1.2.3 |
| C7 | T1 | metalloids along the line (Si, Ge) | OK / OFF-SPEC | True; not on spec. | — |
| C8 | T2 | across a period: atomic number up; outer electrons 1→8; metallic character down | OK | — | 5.1.2.1; 5.1.2.3 |
| C9 | T2 | down a group: atoms larger, outer electrons further, less attracted; metals more reactive; "NON-METALS become LESS REACTIVE going down" | IMPRECISE | Spec states the non-metal trend for **Group 7** only; Group 0 is unreactive throughout. Say "Group 7 elements become less reactive going down". | 5.1.2.4; 5.1.2.6 |
| C10 | T3 | transition metals between Groups 2 and 3; harder, higher melting points, dense, strong, shiny | OK | Spec also lists densities, strength, reactivity with O₂, water, halogens vs Group 1. | 8462 4.1.3.1 |
| C11 | T3 | whole chunk on transition metals | ROUTE | 8462 4.1.3 is **chemistry only**; not in 8464. Site ships it to CF and CH. Separate lesson `transition-metals` (TF TH) already teaches it. | 8462 4.1.3 |
| C12 | T3 | examples Fe, Cu, **Zn**, Ti, Ni, Au, Ag | IMPRECISE | Zinc is a d-block metal but not usually classed as a transition element (its only ion, Zn²⁺, has a full d sub-shell; colourless compounds, no variable charge). Use the spec's six: Cr, Mn, Fe, Co, Ni, Cu. | 8462 4.1.3.1 |
| C13 | T3 | CuSO₄ blue; Fe(II) pale green; Fe(III) orange; Fe catalyst in Haber process; Ni in hydrogenation; Fe²⁺/Fe³⁺ | OK | Fe(III) compounds are usually described as orange-brown / yellow-brown — fine. "Oxidation states" is beyond spec wording ("ions with different charges"). | 8462 4.1.3.2 |
| C14 | T3 | Group 1 soft, very reactive, compounds usually white | OK | — | 8462 4.1.3.1 |
| C15 | `higher` (TH, CH) | Group 1 reactivity increases down (weaker attraction, "lower ionisation energy"); Group 7 decreases down; predict unknown elements | ROUTE + OFF-SPEC term | The explanations are **base** (8464 5.1.2.5, 5.1.2.6 "explain how properties … depend on the outer shell of electrons"; 5.1.2.1 "predict … reactivity"). Not HT. CF/TF copies are null, so Foundation pupils lose base content. "Ionisation energy" is A-level — do not use. | 5.1.2.1; 5.1.2.5; 5.1.2.6 |
| C16 | common_mistake | Period 3, Group 2 → 3 shells, 2 outer electrons → 2.8.2 (magnesium) | OK | Mg = 12 ✓. | 5.1.1.7 |
| C17 | key_note | summary | OK | — | 5.1.2.1 |
| C18 | q1 key | Period 3, Group 2 → 2.8.2 | OK | ✓ | 5.1.2.1 |
| C19 | q1 wx1 ("3.2") | group number gives outer electrons; fill inner shells first | OK | — | — |
| C20 | q1 wx2 ("2.2") | "Period 3 means 3 SHELLS, not 3 electrons in the outer shell. The shells fill as 2.8.2" | IMPRECISE (mismatched) | The text answers option "2.8.3"'s error, not "2.2"'s. It is still true and "Period 3 means 3 shells" does rule out 2.2 (two shells), so the item is usable. | — |
| C21 | q1 wx3 ("2.8.3") | Period 3 = 3 shells; group gives outer count | OK | — | — |
| C22 | q2 key | Group 7 all have 7 outer electrons; react by gaining one electron to fill the shell | OK | — | 5.1.2.1; 5.1.2.6 |
| C23 | q2 wx1–wx3 | F gas, I solid; F 9, Cl 17, Br 35 electrons; same group ≠ same period | OK | F = 9, Cl = 17, Br = 35 ✓. | 5.1.2.6 |

Count: **0 WRONG**. ROUTE: C11, C15. IMPRECISE: C3, C9, C12, C20. No calculations; no Convert lines in the file.

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| none | q1 and q2 are correct and base | **Both usable on all four routes** (q1 Apply, q2 Explain). q1 wx2 is mismatched but true (C20). |

## 5. For the lesson author
**Misconceptions seen in AQA marking**
- Periods and groups swapped ("Group 3 means 3 shells").
- "Ordered by atomic mass" — the modern table is by atomic (proton) number.
- Group number read as total electrons.
- "Elements in a group have the same number of electrons."
- "Non-metals get more reactive down the group like metals do."
- Group 0 "has 0 outer electrons".

**Command words**: Explain how the position … is related to …; Predict; Give the electronic structure; State the group / period.

**Typical questions** ⚑ examiner-drafted
- *Element X has the electronic structure 2.8.6. Give its group and period. [2]* — Group 6 (1); Period 3 (1).
- *Explain why sodium and potassium have similar chemical properties. [2]* — same group / Group 1 (1); both have one electron in the outer shell (1).
- *Rubidium is below potassium in Group 1. Predict how its reaction with water compares with potassium's. [1]* — more vigorous / more reactive.

**Required practical**: none. **Equations**: none.

## 6. Verdict
SOURCE OK WITH FLAGS. All base science and both frozen quiz items are correct and usable on all routes. Two route faults: the transition-metals chunk is chemistry-only and already has its own Triple lesson; the `higher` field holds base content (Group 1/7 trend explanations) that Foundation routes currently lose, and uses the off-spec term "ionisation energy". Four minor imprecisions in re-cuttable theory.

**For Mide:** nothing. All points are settled science.
