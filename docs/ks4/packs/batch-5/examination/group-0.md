# Examination — Group 0, Noble Gases (group-0) — AQA 8464 5.1.2.4 / 8462 4.1.2.4
Verdict: SOURCE OK WITH FLAGS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-5/04-checked-science-source/chemistry-5.1.2.4-group-0.md`.
Spec sources read as text: `AQA-8464-spec.txt` (v1.1, 04 Oct 2019) 5.1.2.4, 5.2.2.4; `AQA-8462-spec.txt` (v1.1, 04 Oct 2019) 4.1.2.4 (identical wording). Route audit `ks4-routes/docs/ks4/route-audit/chemistry.md` row `group-0` (base, CF CH TF TH, OK). Boiling points checked against standard data (He 4.2 K, Ne 27.1 K, Ar 87.3 K, Kr 119.9 K, Xe 165.0 K).

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n (= opts index n). T1–T3 = theory chunks. No route copies differ. No `[NEW — to be examined]` Convert lines in the file (no calculations).

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 | **5.1.2.4** | Group 0 | base |
| 8462 | **4.1.2.4** | Group 0 | base |
| Supporting | 8464 5.2.2.4 / 8462 4.2.2.4 small molecules — intermolecular forces increase with size; 5.2.1.2 / 4.2.1.2 ions with noble-gas structure | | base |

Spec statements (verbatim, 8464 = 8462): "The elements in Group 0 of the periodic table are called the noble gases. They are unreactive and do not easily form molecules because their atoms have stable arrangements of electrons. The noble gases have eight electrons in their outer shell, except for helium, which has only two electrons. The boiling points of the noble gases increase with increasing relative atomic mass (going down the group)." Students should be able to: "explain how properties of the elements in Group 0 depend on the outer shell of electrons of the atoms"; "predict properties from given trends down the group." (WS 1.2)

5.2.2.4: "The intermolecular forces increase with the size of the molecules, so larger molecules have higher melting and boiling points."

## 2. Route table
| # | teachable point | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Members; colourless gases; monatomic; unreactive (T1; common_mistake) | base | 5.1.2.4 | all four | OK |
| R2 | Density down the group / relative to air (T1, T3) | base (context) | 5.1.2.4 (predict trends) | all four | IMPRECISE (C6) |
| R3 | Full outer shell: 8, He 2; stable arrangement → unreactive (T2; key_note) | base | 5.1.2.4 | all four | OK |
| R4 | Other elements react to gain a noble-gas structure (T2) | base | 5.2.1.2 | all four | IMPRECISE (C11) |
| R5 | Boiling point increases down the group; data (T3; key_note) | base | 5.1.2.4 | all four | OK; spec link to relative atomic mass missing (C15) |
| R6 | "London dispersion forces", "temporary dipoles" (T3; key_note; q2) | off-spec term | — (5.2.2.4 says "intermolecular forces") | all four | OFF-SPEC (C14) |
| R7 | Predict properties from trends | base | 5.1.2.4 (WS 1.2) | — (data present, skill not taught) | GAP (C16) |
| R8 | q1 | base | 5.1.2.4 | all four | OK — usable on all routes |
| R9 | q2 | base | 5.1.2.4; 5.2.2.4 | all four | OK — usable on all routes (key uses an off-spec term, C24) |
| — | RP, FIFA, equations, `higher`, examiner_tip | none | — | — | correct: none on spec |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | T1 | Group 0 "also called Group 18" | OK | True (IUPAC); AQA uses Group 0 throughout. | 5.1.2.4 |
| C2 | T1 | He 2, Ne 10, Ar 18, Kr 36, Xe 54, Rn 86 | OK | All ✓. | — |
| C3 | T1 | colourless gases at room temperature | OK | — | — |
| C4 | T1 | monatomic — single atoms, not molecules | OK | Spec: "do not easily form molecules". | 5.1.2.4 |
| C5 | T1 | extremely unreactive — no compounds under normal conditions | OK | (Xe compounds exist under special conditions — not needed.) | 5.1.2.4 |
| C6 | T1 | "DENSER than air as you go down the group" | IMPRECISE | Reads as "all denser than air". Helium and neon are less dense than air; argon onwards denser. Say "density increases down the group". | — |
| C7 | T1 | very low boiling points | OK | — | 5.1.2.4 |
| C8 | T2 | full outer shells: He 2; Ne 2.8; Ar 2.8.8 | OK | GCSE shell model (first 20 elements). | 5.1.2.4; 5.1.1.7 |
| C9 | T2 | full outer shell is the most stable arrangement; no tendency to gain, lose or share electrons | OK | Spec: "stable arrangements of electrons". | 5.1.2.4 |
| C10 | T2 | Group 1 lose 1, Group 7 gain 1, non-metals share → noble-gas structure | OK | — | 5.2.1.2 |
| C11 | T2 | other elements react because "they are trying to ACHIEVE" a full shell | IMPRECISE (minor) | Atoms do not try. "When they react, atoms gain, lose or share electrons and end with a noble-gas structure." | 5.2.1.2 |
| C12 | T3 | atomic radius increases down the group — more shells | OK | — | — |
| C13 | T3 | b.p. He −269, Ne −246, Ar −186, Kr −153, Xe −108 °C | OK | All ✓ to the nearest degree. | — |
| C14 | T3; key_note | "LONDON DISPERSION FORCES … temporary dipoles in electron clouds" | OFF-SPEC term | Science is right; the term and the dipole mechanism are A-level. AQA credits "forces between atoms / intermolecular forces get stronger as the atoms get bigger". | 5.2.2.4 |
| C15 | T3; key_note | b.p. increases because atoms are bigger | GAP (minor) | Spec phrase: boiling points "increase with increasing relative atomic mass". Teach both: bigger atoms, higher relative atomic mass, stronger forces between atoms, more energy to separate them. | 5.1.2.4 |
| C16 | (absent) | predict properties from given trends | GAP | Data in T3 supports it: e.g. predict radon's boiling point (real value −62 °C) or state. | 5.1.2.4 (WS 1.2) |
| C17 | T3 | density increases down the group | OK | — | — |
| C18 | T3 | reactivity very low throughout | OK | — | 5.1.2.4 |
| C19 | common_mistake | monatomic, not He₂ or Ne₂; O₂, N₂ diatomic because they share electrons | OK | — | 5.1.2.4 |
| C20 | key_note | He 2 outer electrons; all others 8 | OK | — | 5.1.2.4 |
| C21 | matching (to be replaced) | "Helium has only 2 electrons and 2 protons — very low density" | IMPRECISE | Low density is from low relative atomic mass (4: 2 protons + 2 neutrons); electrons are irrelevant. Replaced anyway. | — |
| C22 | q1 key | full outer shells — no tendency to gain, lose or share electrons | OK | — | 5.1.2.4 |
| C23 | q1 wx1–wx3 | gases can be reactive (Cl₂, O₂); shells are full not empty (He 2, others 8); size is not the reason | OK | — | 5.1.2.4 |
| C24 | q2 key | argon larger with more electrons → "stronger London dispersion forces between atoms need more energy to overcome" | OK (term off-spec) | Correct and credit-worthy ("stronger forces between atoms"). The only option about forces between atoms, so it is answerable without the term. | 5.1.2.4; 5.2.2.4 |
| C25 | q2 wx1 | stronger nuclear attraction would not directly raise boiling point; forces between atoms matter | OK | Leaves unchallenged the option's premise that argon's electrons are held more strongly (they are held less strongly than neon's), but makes no false claim itself. | — |
| C26 | q2 wx2 | all noble gases monatomic | OK | — | 5.1.2.4 |
| C27 | q2 wx3 | argon not radioactive; radon is the radioactive noble gas | OK | — | — |

Count: **0 WRONG**. OFF-SPEC term: C14 (and in q2's key, C24). GAP: C15, C16. IMPRECISE: C6, C11, C21. No calculations.

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| none | q1 and q2 are correct and base | **Both usable on all four routes** (q1 Explain, q2 Explain). q2's key says "London dispersion forces" — the lesson should call them "forces between atoms" and not teach the term (flag F1). |

## 5. For the lesson author
**Misconceptions seen in AQA marking**
- "Noble gases have no outer electrons / an empty shell" (q1 option 3).
- "Boiling point rises because the bonds inside the molecule are stronger" — they are single atoms; it is the forces between atoms.
- "All noble gases have 8 outer electrons" — helium has 2.
- "Noble gases exist as He₂, Ne₂."
- "Unreactive because they are gases."
- "Boiling point decreases down the group" (confused with Group 1 melting points).

**Command words**: Explain why … unreactive; Explain the trend in boiling points; Predict / Estimate (from a table); Give the electronic structure.

**Typical questions** ⚑ examiner-drafted
- *Explain why argon is unreactive. [2]* — full outer shell / 8 outer electrons (1); stable arrangement, so does not easily gain, lose or share electrons (1).
- *Use the table (He to Xe boiling points) to predict the boiling point of radon. [1]* — any value from about −80 °C to −40 °C (real −62 °C).
- *Explain why the boiling point of xenon is higher than that of neon. [2]* — xenon atoms are larger / higher relative atomic mass (1); stronger forces between atoms, more energy to overcome (1).

**Required practical**: none. **Equations**: none.

## 6. Verdict
SOURCE OK WITH FLAGS. All facts and all five boiling points are correct; both frozen quiz items usable on all routes. The boiling-point explanation uses A-level vocabulary ("London dispersion forces", "temporary dipoles") — the science is right but the spec's words are "intermolecular forces" / "forces between atoms" and "relative atomic mass". The spec's "predict properties from given trends" skill is not taught. Three minor imprecisions in re-cuttable text.

**For Mide:** nothing. All points are settled science.
