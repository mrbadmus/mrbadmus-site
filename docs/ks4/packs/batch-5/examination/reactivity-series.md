# Examination — Reactivity of Metals and Metal Oxides (reactivity-series) — AQA 8464 5.4.1.1–5.4.1.2 / 8462 4.4.1.1–4.4.1.2
Verdict: SOURCE HAS ERRORS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-5/04-checked-science-source/chemistry-5.4.1.1-reactivity-series.md`.
Spec sources read as text: `AQA-8464-spec.txt` (v1.1, 04 Oct 2019) 5.4.1.1–5.4.1.4, 5.4.2.1–5.4.2.2; `AQA-8462-spec.txt` (v1.1, 04 Oct 2019) 4.4.1.1–4.4.1.4 (identical wording). Route audit `ks4-routes/docs/ks4/route-audit/chemistry.md` rows `reactivity-series` (base; "HT layer: ionic displacement equations (5.4.1.4)"), `oxidation-reduction`, `reactions-of-acids`.

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n (= opts index n). T1–T3 = theory chunks. Only `higher` has route copies (CF, TF = null). No `[NEW — to be examined]` Convert lines in the file (no calculations).

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 | **5.4.1.1** | Metal oxides | base |
| 8464 | **5.4.1.2** | The reactivity series | base |
| 8462 | **4.4.1.1–4.4.1.2** | (same) | base |
| Supporting | 8464 5.4.1.4 / 8462 4.4.1.4 Oxidation and reduction in terms of electrons | | **(HT only)** |
| Supporting | 8464 5.4.1.3 / 8462 4.4.1.3 extraction by carbon (own lesson `extraction-of-metals`); 5.4.2.1 / 4.4.2.1 acids + metals; 5.4.2.2 / 4.4.2.2 metal oxides are bases | | base |

Spec statements (verbatim, 8464 = 8462): 5.4.1.1 "Metals react with oxygen to produce metal oxides. The reactions are oxidation reactions because the metals gain oxygen. Students should be able to explain reduction and oxidation in terms of loss or gain of oxygen."

5.4.1.2 "When metals react with other substances the metal atoms form positive ions. The reactivity of a metal is related to its tendency to form positive ions. Metals can be arranged in order of their reactivity in a reactivity series. The metals potassium, sodium, lithium, calcium, magnesium, zinc, iron and copper can be put in order of their reactivity from their reactions with water and dilute acids. The non-metals hydrogen and carbon are often included in the reactivity series. A more reactive metal can displace a less reactive metal from a compound." Students should be able to: "recall and describe the reactions, if any, of potassium, sodium, lithium, calcium, magnesium, zinc, iron and copper with water or dilute acids and where appropriate, to place these metals in order of reactivity"; "explain how the reactivity of metals with water or dilute acids is related to the tendency of the metal to form its positive ion"; "deduce an order of reactivity of metals based on experimental results." "The reactions of metals with water and acids are limited to room temperature and do not include reactions with steam."

5.4.1.3 (limit): "Knowledge and understanding are limited to the reduction of oxides using carbon."

5.4.1.4 (HT only): "Oxidation is the loss of electrons and reduction is the gain of electrons. Student should be able to: write ionic equations for displacement reactions; identify in a given reaction, symbol equation or half equation which species are oxidised and which are reduced."

## 2. Route table
| # | teachable point | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Reactivity series order incl. C and H (T1; key_note) | base | 5.4.1.2 | all four | OK |
| R2 | Reactions with water (T2) | base | 5.4.1.2 | all four | IMPRECISE (C5); steam OFF-SPEC (C9, C10); zinc/iron at room temperature missing (C11) |
| R3 | Reactions with dilute acid (T2) | base | 5.4.1.2; 5.4.2.1 | all four | OK |
| R4 | Displacement from salt solutions; observations (T3; common_mistake) | base | 5.4.1.2 | all four | OK |
| R5 | Hydrogen reduces oxides of metals below it; CuO + H₂ (T3) | off-spec | 5.4.1.3 limit | all four | OFF-SPEC (C17) |
| R6 | Carbon reduces oxides of metals below it (T3) | base | 5.4.1.3 | all four | OK (own lesson `extraction-of-metals`) |
| R7 | Metal oxides basic; reactive metals' oxides harder to reduce (T3) | base | 5.4.2.2; 5.4.1.3 | all four | OK |
| R8 | Metal + oxygen → metal oxide is oxidation (gain of oxygen); reduction = loss of oxygen | base | 5.4.1.1 | — (equation only) | **GAP** (C29) |
| R9 | Reactivity ↔ tendency to form a positive ion | **base** | 5.4.1.2 | only inside `higher` (CH TH), as "ionisation energy" | **ROUTE + OFF-SPEC term** (C21) |
| R10 | `higher`: ionic equation Fe + Cu²⁺ → Fe²⁺ + Cu; spectator ions | higher | 5.4.1.4 (HT only) | CH TH | OK |
| R11 | Identify species oxidised/reduced in terms of electrons | higher | 5.4.1.4 (HT only) | — | GAP (C23) |
| R12 | equations ×4 (word / symbol) | base | 5.4.1.1; 5.4.1.2; 5.4.2.1 | all four | OK |
| R13 | q1 | base | 5.4.1.2 | all four | OK — usable on all routes |
| R14 | q2 | base | 5.4.1.2; 5.4.2.1 | all four | **WRONG** wx2 (C34) — do not use as written |
| — | RP, FIFA, examiner_tip | none | — | — | correct: none on spec (AT 6 is an apparatus technique, not an RP) |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | T1 | order K, Na, Li, Ca, Mg, Al, (C), Zn, Fe, Sn, Pb, (H), Cu, Ag, Au, Pt | OK | Spec's eight in spec order ✓; C between Al and Zn ✓; H between Pb and Cu ✓. Al, Sn, Pb, Ag, Au, Pt are context. | 5.4.1.2 |
| C2 | T1 | carbon and hydrogen "not a metal, included as reference" | OK | Spec: "often included". | 5.4.1.2 |
| C3 | T1 | mnemonic, 16 words, initials of English names | OK | P S L C M A C Z I T L H C S G P matches the list ✓. | — |
| C4 | T2 | reactivity established by observing how vigorously metals react | OK | — | 5.4.1.2 |
| C5 | T2 | "Potassium: explosive, ignites hydrogen gas (lilac flame)" | IMPRECISE | Very vigorous: floats, fizzes, melts, hydrogen ignites with a lilac flame, may spit. "Explosive" overstates it; AQA marks "very vigorous / lilac flame". | 5.4.1.2 |
| C6 | T2 | sodium: vigorous fizzing, melts into a ball, may ignite | OK | Also moves about on the surface; flame yellow-orange. | — |
| C7 | T2 | lithium: steady fizzing | OK | Floats. | — |
| C8 | T2 | calcium: steady bubbling, cloudy solution (Ca(OH)₂) | OK | — | — |
| C9 | T2 | "Magnesium: barely reacts with cold water; reacts well with steam" | OFF-SPEC (second half) | Cold-water half ✓. Spec: "do not include reactions with steam". | 5.4.1.2 |
| C10 | T2 | "Iron: reacts very slowly with steam to form iron oxide and hydrogen" | OFF-SPEC | Steam excluded. At room temperature iron does not react with water alone (rusting needs oxygen too). | 5.4.1.2 |
| C11 | T2 | (absent) zinc and iron with water at room temperature | GAP | Spec's eight must be described: zinc and iron — no (or no visible) reaction with cold water. | 5.4.1.2 |
| C12 | T2 | copper, silver, gold: no reaction with water | OK | — | — |
| C13 | T2 | dilute acid: Mg vigorous fizzing; Zn steady; Fe slow; Cu none; Au, Pt none | OK | Spec-limited set for acids is Mg, Zn, Fe (5.4.2.1) ✓. | 5.4.1.2; 5.4.2.1 |
| C14 | T3 | more reactive metal displaces less reactive from its compound | OK | Spec wording. | 5.4.1.2 |
| C15 | T3 | Fe + CuSO₄ → FeSO₄ + Cu; blue → pale green; copper deposits on the iron | OK | Balanced ✓. Deposit is red-brown/pink. | 5.4.1.2 |
| C16 | T3 | copper + iron sulfate: no reaction | OK | — | — |
| C17 | T3 | hydrogen displaces metals below it from their oxides; CuO + H₂ → Cu + H₂O | OFF-SPEC | True and balanced ✓, but spec limits oxide reduction to carbon. Context only; never examined. | 5.4.1.3 |
| C18 | T3 | carbon reduces oxides of metals below it | OK | Belongs to `extraction-of-metals` (batch 5 #12); a one-line link here is fine. | 5.4.1.3 |
| C19 | T3 | metal oxides are basic, neutralise acids | OK | — | 5.4.2.2 |
| C20 | T3 | more reactive metal → more stable oxide, harder to reduce | OK | Consistent with 5.4.1.3 (carbon reduces only metals below it). | 5.4.1.3 |
| C21 | `higher` (CH TH) | "Explain reactivity in terms of ionisation energy — more reactive metals have lower ionisation energies and lose electrons more easily" | ROUTE + OFF-SPEC term | The idea is **base**: "the reactivity of a metal is related to its tendency to form positive ions" (5.4.1.2, no HT label). CF/TF copies are null, so Foundation pupils lose it. "Ionisation energy" is A-level — never use. | 5.4.1.2 |
| C22 | `higher` | ionic equation Fe + Cu²⁺(aq) → Fe²⁺(aq) + Cu; spectator ions; net ionic equations | OK | HT ✓. Balanced in atoms and charge ✓. Add (s) to Fe and Cu if state symbols are shown. Sulfate is the spectator ion. | 5.4.1.4 (HT only) |
| C23 | `higher` (absent) | identify which species is oxidised and which reduced (electrons) | GAP | Fe loses electrons → oxidised; Cu²⁺ gains electrons → reduced. HT. Also taught in `oxidation-reduction`. | 5.4.1.4 (HT only) |
| C24 | common_mistake | a metal can only displace one below it; copper cannot displace iron | OK | — | 5.4.1.2 |
| C25 | key_note | order; displacement from solution or oxide; evidence from water, acid, displacement | OK | — | 5.4.1.2 |
| C26 | equations | Fe + CuSO₄ → FeSO₄ + Cu | OK | Balanced ✓. | 5.4.1.2 |
| C27 | equations | metal + oxygen → metal oxide; metal + water → metal hydroxide + hydrogen; metal + acid → salt + hydrogen | OK | Water equation is right at room temperature (steam gives the oxide — off-spec). | 5.4.1.1; 5.4.1.2; 5.4.2.1 |
| C28 | matching (to be replaced) | Zn/CuSO₄ yes; Cu/ZnSO₄ no; Mg/FeSO₄ yes; Fe/MgSO₄ no; Fe/CuSO₄ yes | OK | All five ✓. | 5.4.1.2 |
| C29 | (absent) | metal + oxygen is **oxidation** because the metal gains oxygen; reduction = loss of oxygen | GAP | The file claims 5.4.1.1 but never states it. Added as "Spec core missing" in the source. Also taught in `oxidation-reduction`. | 5.4.1.1 |
| C30 | q1 key | zinc in CuSO₄: blue fades, copper deposits on the zinc | OK | — | 5.4.1.2 |
| C31 | q1 wx1 | zinc is more reactive; blue (Cu²⁺) → colourless (Zn²⁺) | OK | — | — |
| C32 | q1 wx2, wx3 | no orange solution; zinc sulfate stays dissolved | OK | — | — |
| C33 | q2 key | copper is below hydrogen — cannot displace hydrogen from the acid | OK | — | 5.4.1.2; 5.4.2.1 |
| C33a | q2 wx1 | density does not decide reactivity; gold denser than magnesium | OK | Au 19.3, Mg 1.7 g/cm³ ✓. | — |
| C34 | q2 wx2 | "HCl reacts with many metals — magnesium, zinc, iron all react **vigorously** with HCl." | **WRONG** | Zinc reacts steadily and iron slowly (the file's own T2: "Zinc: steady bubbling. Iron: slow bubbling."). Describing these reactions is a spec recall point; "iron reacts vigorously" would not be credited. | 5.4.1.2 |
| C35 | q2 wx3 | copper does not react with dilute HCl at all | OK | — | — |

Count: **1 WRONG** (C34, q2 wx2). ROUTE: C21. OFF-SPEC: C9, C10, C17 (all true, context). GAP: C11, C23, C29. IMPRECISE: C5. No calculations.

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| q2 | wx2 states that magnesium, zinc **and iron** react vigorously with HCl — false for zinc and iron, a spec recall point | **Do not use as written** on any route (flag F1). Design writes a replacement on the same idea (copper below hydrogen). |
| q1 | correct, base | **Usable on all four routes** (Apply). |

## 5. For the lesson author
**Misconceptions seen in AQA marking**
- "The less reactive metal displaces the more reactive one" — direction reversed.
- "Copper reacts slowly with acid" — no reaction.
- Observations given as products ("copper sulfate is made") instead of what is seen (colour change, deposit, fizzing).
- "Metals gain electrons / form negative ions" when they react.
- Order deduced from one reaction only, or from size of metal pieces (fair test).
- Steam reactions recalled as cold-water reactions (Mg "reacts well with water").

**Command words**: Describe; Explain why … ; Deduce the order of reactivity; Predict whether … will react; Suggest an observation; (HT) Write an ionic equation; Identify which species is oxidised.

**Typical questions** ⚑ examiner-drafted
- *A student adds metals X, Y and Z to dilute hydrochloric acid. X fizzes rapidly, Y does not react, Z bubbles slowly. Give the order of reactivity, most reactive first. [1]* — X, Z, Y.
- *Magnesium is added to copper sulfate solution. Give two observations. [2]* — blue colour fades (1); red-brown / pink solid forms (1) (accept magnesium gets smaller).
- *Explain why potassium is more reactive than lithium in terms of ions. [1]* — potassium has a greater tendency to form a positive ion / loses its outer electron more easily.
- *(HT) Write the ionic equation for zinc reacting with copper sulfate solution and identify the species reduced. [2]* — Zn + Cu²⁺ → Zn²⁺ + Cu (1); Cu²⁺ (ions) reduced (1).

**Required practical**: none. **Equations**: word and symbol equations only — no formula triangles.

## 6. Verdict
SOURCE HAS ERRORS. One frozen wrong explanation is false on a spec recall point (q2 wx2: zinc and iron "vigorous") — q2 is not usable as written. The `higher` field holds base content (reactivity ↔ tendency to form a positive ion) in an off-spec term ("ionisation energy") and is missing on Foundation routes. The file never states 5.4.1.1's oxidation-as-gain-of-oxygen. Steam reactions and hydrogen reduction are true but explicitly outside the spec. All equations, the series order and q1 are correct.

**For Mide:** nothing. All points are settled science.
