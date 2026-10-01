# Examination — Atoms, Elements and Compounds (atoms-elements-compounds) — AQA 8464 5.1.1.1 / 8462 4.1.1.1
Verdict: SOURCE OK WITH FLAGS
Examiner: Opus, 1 Oct 2026. Pack examined: `docs/ks4/packs/batch-2/chemistry-5.1.1.1-atoms-elements-compounds.md`.
Spec sources fetched from filestore.aqa.org.uk and read as text (`pdftotext -layout`): AQA-8462-SP-2016.PDF and AQA-8464-SP-2016.PDF, both Version 1.1, 04 Oct 2019.
Route copies: I checked the four `all_subtopics_chemistry*.py` records directly. All four (CF, CH, TF, TH) are byte-identical in every field, and none has a `higher` field. No examiner tip, FIFA, equations or RP exist for this lesson.

Conventions: q1–q4 = quiz items in pack order; "wx n" = `wrong_explanations` key n; th1–th3 = theory chunks.

## 1. Spec reference
| spec | section | title | page | label |
|---|---|---|---|---|
| 8464 | **5.1.1.1** | Atoms, elements and compounds | p.68 | base |
| 8462 | **4.1.1.1** | Atoms, elements and compounds | p.18 | base |
| supporting | 8464 5.1.1.2 / 8462 4.1.1.2 | Mixtures | p.69 / p.19 | base |
| supporting | 8464 5.3.1.1 / 8462 4.3.1.1 | Conservation of mass and balanced chemical equations | p.85 / p.37 | base |

BATCH-PLAN "5.1.1.1" is right, and the pack filename agrees. The text of 5.1.1.1 and 4.1.1.1 is identical word for word.

Spec statements relied on (verbatim, identical in both specs): "All substances are made of atoms. An atom is the smallest part of an element that can exist. … There are about 100 different elements. Elements are shown in the periodic table. Compounds are formed from elements by chemical reactions. Chemical reactions always involve the formation of one or more new substances, and often involve a detectable energy change. Compounds contain two or more elements chemically combined in fixed proportions … Compounds can only be separated into elements by chemical reactions." Students should be able to: "use the names and symbols of the first 20 elements … name compounds of these elements from given formulae or symbol equations; write word equations …; write formulae and balanced chemical equations …" and "(HT only) write balanced half equations and ionic equations where appropriate."
4.1.1.2: "A mixture consists of two or more elements or compounds not chemically combined together. The chemical properties of each substance in the mixture are unchanged. Mixtures can be separated by physical processes such as filtration, crystallisation, simple distillation, fractional distillation and chromatography."

**Overlap to manage.** Separation techniques are the subject of batch-3 `mixtures` (5.1.1.2), and balancing equations is the subject of batch-3 `conservation-of-mass` (5.3.1.1). In this lesson both should stay at the depth of a definition and a first example.

## 2. Route table
| # | teachable point | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Atom definition; symbols; about 100 elements; periodic table (th1) | base | 4.1.1.1 | all four | OK |
| R2 | Element = one type of atom; cannot be broken down chemically (th1, th3) | base | 4.1.1.1 | all four | OK |
| R3 | Compound = elements chemically combined in fixed proportions; new properties; separated only by chemical reactions (th1, th3; common_mistake) | base | 4.1.1.1 | all four | OK |
| R4 | Mixture: not chemically combined, properties unchanged, physical separation, variable proportions (th1, th3) | base | 4.1.1.2 | all four | OK |
| R5 | Formulae and subscripts (th2) | base | 4.1.1.1; 4.3.1.1 ("multipliers … in subscript within a formula") | all four | OK |
| R6 | Balanced equations; conservation of mass (th2; q3; key_note) | base | 4.1.1.1; 4.3.1.1 | all four | OK |
| R7 | Ionic equations and half equations | higher | 4.1.1.1 (HT only) | not in pack | Nothing to fix. Do not add them to this lesson. |
| R8 | Element sorting (q1, q2, q4; matching) | base | 4.1.1.1–4.1.1.2 | all four | OK |
| R9 | Electrolysis of water (common_mistake, as an example) | base, as an illustration only | 4.4.3 (electrolysis), not examined here | all four | OK as an example. Do not make it a rung. |

No HT content and no chemistry-only content is taught. No route is misplaced.

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | th1 | "ATOMS — the smallest particles that cannot be broken down by chemical means" | IMPRECISE | Use the spec's definition: "An atom is the smallest part of an element that can exist." The pack's wording also fits ions and molecules. | 4.1.1.1 |
| C2 | th1 | "only ONE type of atom … cannot be broken down into simpler substances by chemical reactions" | OK | — | 4.1.1.1 |
| C3 | th1 | "There are 118 known elements" | OK | True (IUPAC). The spec says "about 100". Either is creditable, so state it as "about 100 (118 known today)" so the page agrees with the spec. | 4.1.1.1 |
| C4 | th1 | symbols C, O, Fe, Na | OK | — | 4.1.1.1 |
| C5 | th1 | "arranged in the PERIODIC TABLE in order of atomic number" | OK | — | 4.1.2.1 |
| C6 | th1 | compound = "two or more DIFFERENT elements CHEMICALLY BONDED" | OK | "In fixed proportions" is missing here. th3 supplies it, so keep the two together. | 4.1.1.1 |
| C7 | th1 | "properties … completely different" | IMPRECISE | Write "different". "Completely" is not the spec's word, and some properties (such as the state at room temperature) can coincide. | 4.1.1.1 |
| C8 | th1 | Na (reactive metal) + chlorine (toxic green gas) → NaCl | OK | Chlorine is pale yellow-green, so "green" is acceptable. | — |
| C9 | th1 | "Compounds can only be separated by chemical reactions" | OK | Verbatim in substance. | 4.1.1.1 |
| C10 | th1 | mixture: "NOT chemically bonded — each keeps its own properties"; physical methods (filtering, distillation, chromatography); proportions can vary | OK | The spec's exact claim is that the *chemical* properties are unchanged. | 4.1.1.2 |
| C11 | th2 | H₂O, CO₂, NaCl, H₂SO₄ atom counts | OK | — | 4.3.1.1 |
| C12 | th2 | "Atoms cannot be created or destroyed … (law of conservation of mass)" | OK | — | 4.3.1.1 |
| C13 | th2 | 2H₂ + O₂ → 2H₂O "(4 H and 2 O on each side)"; H₂ + O₂ → H₂O unbalanced | OK | — | 4.3.1.1 |
| C14 | th3 | element "Has fixed properties"; examples Fe, O₂, Au, S | OK | O₂ is a good example: an element made of molecules. | 4.1.1.1 |
| C15 | th3 | compound examples H₂O, CO₂, MgO | OK | — | — |
| C16 | th3 | mixture examples: air, seawater, crude oil, bronze (copper + tin), ink | OK | Crude oil is "a mixture of a very large number of compounds" (4.7.1.1). Bronze as a metal mixture is consistent with the pilot ruling on alloys. | 4.1.1.2; 4.7.1.1 |
| C17 | common_mistake | electrolysis splits water into H₂ and O₂; "Water is a compound. Saltwater is a mixture." | OK | — | 4.1.1.1 |
| C18 | key_note | whole line | OK | — | 4.1.1.1–4.1.1.2; 4.3.1.1 |
| C19 | matching (to be replaced) | Cu element; H₂O compound; air mixture; CO₂ compound; crude oil mixture; Au element | OK | All six are correct. Reuse them as sort items in the replacement activity. | 4.1.1.1–4.1.1.2 |
| C20 | q1 key | "chemically bonded in fixed proportions — a mixture is not bonded and can be separated physically" | OK | — | 4.1.1.1–4.1.1.2 |
| C21 | q1 wx1/wx2/wx3 | one type of atom = element; state does not define; bonding is the distinction | OK | — | — |
| C22 | q2 key | iron + sulfur heated → iron sulfide, which is not magnetic, so a compound | OK | The product is typically a dark grey or black solid, so "grey" is acceptable. | 4.1.1.1 |
| C23 | q2 wx1 | still a mixture → separable by magnet | OK | — | — |
| C24 | q2 wx2 | "Elements cannot be destroyed by chemical reactions — only rearranged into compounds" | IMPRECISE | It is the *atoms* that are conserved. Elemental sulfur as a substance does stop existing. Better: "the sulfur atoms are still there, now bonded to iron." | 4.3.1.1 |
| C25 | q2 wx3 | "Sulfur is a solid at these temperatures — it does not dissolve into iron." | **WRONG** | Sulfur melts at about 115 °C, so it is liquid when the mixture is heated strongly. The real reason the product is not a "solution" is that a new substance with new properties has formed (it is no longer magnetic). | 4.1.1.1 |
| C26 | q3 stem + key | "Which equation is correctly balanced?" keyed 2H₂ + O₂ → 2H₂O | **WRONG (two correct answers)** | Option index 2, H₂ + O₂ → H₂O₂, is also correctly balanced, and its own wx2 admits this ("this equation is balanced"). The stem never says the product must be water. AQA would credit both answers. | 4.3.1.1 |
| C27 | q3 wx1, wx3 | O counts (2 vs 1; 4 vs 2) | OK | — | — |
| C28 | q4 key | bronze = copper + tin, not chemically bonded | OK | — | 4.1.1.2 |
| C29 | q4 wx1–3 | water, NaCl, CO₂ are compounds; ionic / covalent | OK | — | 4.2.1 |

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| all routes · q2 · "A student heats a mixture of iron filings and sulfur…" | The keyed answer is right, but wx3 states a false fact (that sulfur stays solid) and is shown to any pupil who picks the "solution" distractor. | Keep verbatim. **Do not use it as a ladder rung on any route.** Do not quote wx3 in the body. A new activity can reuse the iron + sulfur scenario with fresh feedback. |
| all routes · q3 · "Which equation is correctly balanced?" | It has two correct options (the H₂O₂ equation is balanced). | Keep verbatim. **Do not use it as a ladder rung on any route**, and do not use it in the body. Write a new balancing item whose stem names the product. |

q1 and q4 are clean on every route and can be rung-1 (recall) candidates.

## 5. For the lesson author

**Misconceptions AQA mark schemes and examiner reports commonly see**
- **A compound is a mixture.** Seen as "salt water is a compound" or "air is a compound".
- **An element must be single atoms.** O₂ and N₂ get called compounds because they contain "two atoms".
- **Molecule means compound.** In fact every compound has a fixed formula, and some molecules are elements.
- **Alloys are compounds.** Bronze and steel are mixtures.
- **Balancing by changing subscripts** (H₂O → H₂O₂) instead of adding multipliers. This is the error q3 accidentally rewards.
- **Mass is lost or made in a reaction.** This conflates atoms with substances. The batch-3 conservation lesson picks this up.
- **Lazy symbols:** Co for C + O, a lowercase second letter written as a capital (CO vs Co), or "Cl" for chlorine gas instead of Cl₂.
- **"A compound has the properties of its elements"** (salt is "a bit toxic" because chlorine is).

**Command words typically used:** Define, Give, Name, Identify, Describe, Explain, Complete (an equation), Balance, Suggest.

**Typical questions (⚑ examiner-drafted)**
- ⚑ examiner-drafted, 4 marks, Explain: *"A student heats iron filings and sulfur powder. The product is a black solid that is not attracted to a magnet. Explain how this shows that a compound has formed and not a mixture."*
  Marking points:
  - (1) Iron in a mixture would still be attracted to a magnet.
  - (1) The product has different properties from its elements: not magnetic, and a different colour.
  - (1) A chemical reaction has happened, or a new substance has formed.
  - (1) Iron and sulfur are chemically combined (bonded), in fixed proportions, and cannot be separated by a physical method.
- ⚑ examiner-drafted, 3 marks, Complete / Balance: *"Balance: __Na + Cl₂ → __NaCl. Name the product. Is the product an element, compound or mixture?"*
  Marking points:
  - (1) 2, 2.
  - (1) Sodium chloride.
  - (1) Compound.
- ⚑ examiner-drafted, 6 marks, levels of response, Compare: *"Compare elements, compounds and mixtures. Use examples."* This is uncommon at this depth as a 6-marker, and more often appears as 2–4 marks. Use it as rung 4 only if the ladder needs a produce item.
  - Level 3 (5–6): all three are defined correctly, including "fixed proportions" and "not chemically combined", with a correct example of each, **and** a comparison of how they are separated (compound: chemical reaction only; mixture: physical process) and of their properties.
  - Level 2 (3–4): correct definitions of at least two, with examples, and some comparison.
  - Level 1 (1–2): simple statements, for example "an element is one type of atom", with no comparison.
  - Indicative content: one type of atom; ≥2 elements chemically combined in fixed proportions; ≥2 substances not chemically combined; mixture properties unchanged; separation by filtration or distillation versus by chemical reaction or electrolysis; examples such as Cu, O₂, H₂O, CO₂, air and seawater.

**Required practical:** none. Separation of mixtures is AT 4 (an opportunity for practical skills, not a required practical). Chromatography is RP12 Combined / RP6 Chemistry, in another lesson.

**Equations to learn:** no quantitative equation. Pupils must write word equations and balanced symbol equations (base), and the pack's 2H₂ + O₂ → 2H₂O.

## 6. Verdict
**SOURCE OK WITH FLAGS.** All content is base, correctly routed to all four routes. There are 2 WRONG items (q2 wx3 and q3's double key, both frozen) and 3 IMPRECISE items (C1, C7, C24).

Only Mide can rule: **none.** "About 100" versus 118 elements is a fact, not a conflict between AQA sources (C3).

Note for the commander, not a science flag: this lesson has **no `examiner_tip`** in any route copy. The fixed exam-tip slot has no approved text, which is the same situation as pilot R13.
