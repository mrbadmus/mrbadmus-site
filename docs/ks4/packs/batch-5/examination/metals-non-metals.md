# Examination — Metals and Non-metals (metals-non-metals) — AQA 8464 5.1.2.3 / 8462 4.1.2.3
Verdict: SOURCE OK WITH FLAGS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-5/04-checked-science-source/chemistry-5.1.2.3-metals-non-metals.md`.
Spec sources read as text: `AQA-8464-spec.txt` (v1.1, 04 Oct 2019) 5.1.2.3, 5.2.2.4, 5.2.2.7, 5.2.2.8, 5.2.3.2–5.2.3.3, 5.4.1.1, 5.4.2.2; `AQA-8462-spec.txt` (v1.1, 04 Oct 2019) 4.1.2.3 (identical wording). Route audit `ks4-routes/docs/ks4/route-audit/chemistry.md` row `metals-non-metals` (base, CF CH TF TH, OK).

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n (= opts index n). T1–T3 = theory chunks. No route copies differ. No `[NEW — to be examined]` Convert lines in the file (no calculations).

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 | **5.1.2.3** | Metals and non-metals | base |
| 8462 | **4.1.2.3** | Metals and non-metals | base |
| Supporting | 8464 5.2.2.7 / 8462 4.2.2.7 properties of metals; 5.2.2.8 / 4.2.2.8 metals as conductors; 5.2.2.4 / 4.2.2.4 small molecules; 5.2.3.2–5.2.3.3 / 4.2.3.2–4.2.3.3 graphite, graphene; 5.4.2.2 / 4.4.2.2 metal oxides are bases | | base |

Spec statements (verbatim, 8464 = 8462): "Elements that react to form positive ions are metals. Elements that do not form positive ions are non-metals. The majority of elements are metals. Metals are found to the left and towards the bottom of the periodic table. Non-metals are found towards the right and top of the periodic table." Students should be able to: "explain the differences between metals and non-metals on the basis of their characteristic physical and chemical properties"; "explain how the atomic structure of metals and non-metals relates to their position in the periodic table"; "explain how the reactions of elements are related to the arrangement of electrons in their atoms and hence to their atomic number."

5.2.2.8: "Metals are good conductors of electricity because the delocalised electrons in the metal carry electrical charge through the metal. Metals are good conductors of thermal energy because energy is transferred by the delocalised electrons." 5.2.2.7: "Metals have giant structures of atoms with strong metallic bonding. This means that most metals have high melting and boiling points. In pure metals, atoms are arranged in layers, which allows metals to be bent and shaped."

## 2. Route table
| # | teachable point | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Most elements are metals; position in the table (T1, T2) | base | 5.1.2.3 | all four | IMPRECISE (C1, C10) |
| R2 | Physical properties of metals, explained by delocalised electrons / metallic bonding / layers (T1, T3) | base | 5.1.2.3; 5.2.2.7; 5.2.2.8 | all four | OK |
| R3 | Metals form positive ions; basic oxides; react with water/acids → hydrogen (T1, T3) | base | 5.1.2.3; 5.4.2.2; 5.4.2.1 | all four | OK |
| R4 | Physical properties of non-metals (T2, T3) | base | 5.1.2.3; 5.2.2.4 | all four | IMPRECISE (C12) |
| R5 | Graphite/graphene conduct (T2, T3; common_mistake) | base | 5.2.3.2; 5.2.3.3 | all four | IMPRECISE (C22) |
| R6 | Non-metals form negative ions or share electrons; acidic oxides (T2, T3) | base | 5.1.2.3 | all four | IMPRECISE (C16) |
| R7 | Metalloids / silicon semiconductor (T3) | off-spec context | — | all four | OK (true) |
| R8 | Metallic character down a group / across a period (key_note) | base | 5.1.2.3 (position) | all four | OK |
| R9 | Atomic structure ↔ position; reactions ↔ outer electrons | base | 5.1.2.3 | — | **GAP** — not in the frozen data (C25); spec core section added |
| R10 | q1, q2 | base | 5.2.2.8; 5.1.2.3 | all four | OK — usable on all routes |
| — | RP, FIFA, equations, `higher`, examiner_tip | none | — | — | correct: none on spec |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | T1 | metals "on the left and in the centre" | IMPRECISE (minor) | Spec: "to the left and towards the bottom". | 5.1.2.3 |
| C2 | T1 | good conductors of electricity and heat — delocalised electrons carry charge and energy | OK | Spec wording. | 5.2.2.8 |
| C3 | T1 | high melting and boiling points — strong metallic bonds | OK | Spec: "most metals". Group 1 are the exception pupils meet. | 5.2.2.7 |
| C4 | T1 | shiny; malleable; ductile | OK | Layers that slide — 5.2.2.7. | 5.2.2.7 |
| C5 | T1 | solid at room temperature except mercury | OK | — | — |
| C6 | T1 | high density in most cases | OK | — | — |
| C7 | T1 | form positive ions — lose outer electrons | OK | The spec's defining property. | 5.1.2.3 |
| C8 | T1 | metal + oxygen → metal oxide; metal oxides basic, neutralise acids | OK | — | 5.4.1.1; 5.4.2.2 |
| C9 | T1 | many react with water and acids to produce hydrogen | OK | — | 5.4.1.2; 5.4.2.1 |
| C10 | T2 | non-metals "on the right side" | IMPRECISE (minor) | Spec: "towards the right and top" (hydrogen sits top left). | 5.1.2.3 |
| C11 | T2 | poor conductors except graphite and graphene | OK | — | 5.2.3.2–5.2.3.3 |
| C12 | T2; T3 | non-metals have low melting/boiling points — weak forces between molecules | IMPRECISE | True for simple molecular non-metals (5.2.2.4). Carbon (diamond, graphite) and silicon are giant covalent with very high melting points (5.2.3.1). T2 itself lists carbon as a typical solid. Say "most non-metals … because they are made of small molecules". | 5.2.2.4; 5.2.3.1 |
| C13 | T2 | brittle when solid; low density generally | OK | — | — |
| C14 | T2 | many are gases (O₂, N₂, Cl₂, H₂); solids C, S, P, I; bromine liquid | OK | — | — |
| C15 | T2 | (whole) | OK | — | — |
| C16 | T2; T3 | non-metals "FORM NEGATIVE IONS — gain electrons (or share in covalent bonds)" | IMPRECISE | The spec's definition is negative: non-metals "do not form positive ions". Group 0 forms neither; carbon and hydrogen mostly share. Lead with the spec sentence; "many non-metals gain electrons to form negative ions or share electrons" follows. | 5.1.2.3 |
| C17 | T2; T3 | non-metal oxides acidic — dissolve in water to form acids (CO₂, SO₂, NO₂) | OK | True for the examples given. Not every non-metal oxide is acidic (CO, H₂O are neutral) — do not write "all". | 5.1.2.3; 5.9.3.1 (SO₂, NOx → acid rain) |
| C18 | T3 | comparison table: conductivity, melting point, malleability, ions, oxides | OK | Subject to C12 and C16. | — |
| C19 | T3 | basic oxides MgO, Fe₂O₃ | OK | — | — |
| C20 | T3 | silicon is a metalloid / semiconductor, conducts but brittle | OK / OFF-SPEC | True; not on spec. Context only. | — |
| C21 | key_note | summary; "metallic character decreases across a period and increases down a group" | OK | Consistent with "left and towards the bottom". | 5.1.2.3 |
| C22 | common_mistake | "Graphite and graphene are non-metals … graphite has delocalised electrons between its layers" | IMPRECISE | Graphite and graphene are forms of the non-metal carbon, not separate non-metals. Spec: "one electron from each carbon atom is delocalised"; the electrons move along the layers. AQA marks "delocalised electrons"; "between the layers" invites the wrong picture. | 5.2.3.2 |
| C23 | matching (to be replaced) | six pairs | OK | CO₂ + water → carbonic acid ✓. | — |
| C24 | q1 key | metals have delocalised electrons that move and carry charge | OK | Spec wording. | 5.2.2.8 |
| C24a | q1 wx1–wx3 | size not the reason; proton count not the reason; solid metals conduct by electrons, not dissolved ions | OK | — | 5.2.2.8 |
| C24b | q2 key | SO₂ acidic → sulfur is a non-metal | OK | — | 5.1.2.3 |
| C24c | q2 wx1 | metal oxides are basic | OK | — | 5.4.2.2 |
| C24d | q2 wx2 | SO₂ not amphoteric | OK | "amphoteric" is off-spec but defined in the option itself. | — |
| C24e | q2 wx3 | oxide type "is a reliable indicator" of metal/non-metal | IMPRECISE (minor) | True for every oxide a GCSE pupil meets; some metal oxides are amphoteric (Al₂O₃, ZnO). Usable — do not extend it to "always". | — |
| C25 | (absent) | spec core: definition by positive ions; atomic structure ↔ position; reactions ↔ outer electrons | GAP | Metals have few outer electrons (1–3), lost to form positive ions; non-metals have 4–7 (gain or share) or a full shell. Added as "Spec core missing" in the source. | 5.1.2.3 |

Count: **0 WRONG**. GAP: C25. IMPRECISE: C1, C10, C12, C16, C22, C24e. No calculations.

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| none | q1 and q2 are correct and base | **Both usable on all four routes** (q1 Explain, q2 Apply). |

## 5. For the lesson author
**Misconceptions seen in AQA marking**
- "All non-metals are gases" / "non-metals have low melting points" — diamond, graphite, silicon.
- "Non-metals never conduct" — graphite.
- "Metals conduct because ions move" — solid metals conduct by delocalised electrons.
- "Metals gain electrons" — metals lose electrons to form positive ions.
- Definition given as a property list instead of the spec's: metals form positive ions.

**Command words**: Explain the difference …; Explain why … conducts; Give one physical property …; Suggest whether X is a metal (data given).

**Typical questions** ⚑ examiner-drafted
- *Element Y has a melting point of 1538 °C, conducts electricity and forms a basic oxide. Is Y a metal or a non-metal? Give two reasons. [3]* — metal (1); any two of conducts / high melting point / basic oxide (2).
- *Explain why magnesium is a metal in terms of its electrons. [2]* — two outer electrons (1); lost to form a positive ion (1).
- *Explain why copper is a good conductor of electricity. [2]* — delocalised electrons (1); carry charge through the metal (1).

**Required practical**: none. **Equations**: none.

## 6. Verdict
SOURCE OK WITH FLAGS. All property claims are true and both frozen quiz items are usable on all routes. The spec's own definition (positive ions vs not) and its atomic-structure link are missing from the frozen data — added from the spec. Six minor imprecisions in re-cuttable text.

**For Mide:** nothing. All points are settled science.
