# Examination — Pure Substances (pure-substances) — AQA 8464 5.8.1.1 / 8462 4.8.1.1
Verdict: SOURCE OK WITH FLAGS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-14/04-checked-science-source/chemistry-5.8.1.1-pure-substances.md`.
Spec sources read as text: `AQA-8464-spec.txt` (Combined Trilogy v1.1, 04 Oct 2019) §5.8.1.1; `AQA-8462-spec.txt` (Chemistry v1.1, 04 Oct 2019) §4.8.1.1. Route audit `ks4-routes/docs/ks4/route-audit/chemistry.md` row `pure-substances` (CF CH TF TH, base). No equation sheet applies (no equations).

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n; th1–th3 = theory chunks. Both `higher` route copies are `null`.

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 | **5.8.1.1** | Pure substances | base |
| 8462 | **4.8.1.1** | Pure substances | base |

Spec statements (verbatim, 8464 = 8462): "In chemistry, a pure substance is a single element or compound, not mixed with any other substance. Pure elements and compounds melt and boil at specific temperatures. Melting point and boiling point data can be used to distinguish pure substances from mixtures. In everyday language, a pure substance can mean a substance that has had nothing added to it, so it is unadulterated and in its natural state, eg pure milk. Students should be able to use melting point and boiling point data to distinguish pure from impure substances." (WS 2.2, 4.1)

## 2. Route table
| # | teachable point | true layer | spec | verdict |
|---|---|---|---|---|
| R1 | Chemical meaning: one element or compound only (th1, common_mistake, key_note, q2) | base | 5.8.1.1 / 4.8.1.1 | OK |
| R2 | Everyday meaning of "pure" (th1, common_mistake, q2) | base | 5.8.1.1 / 4.8.1.1 | OK (C3 imprecise) |
| R3 | Pure: sharp, fixed mp/bp; mixture: over a range (th1, th2, key_note, q1) | base | 5.8.1.1 / 4.8.1.1 | OK |
| R4 | Use mp/bp data to tell pure from impure, and to identify (th2, q1) | base | 5.8.1.1 / 4.8.1.1; WS 2.2, 4.1 | OK |
| R5 | Impurity lowers mp, raises bp (th1, key_note) | base (detail beyond the spec) | — | IMPRECISE (PS-F1) |
| R6 | Purity in context: medicines, food, semiconductors (th3) | base context | — | thalidomide line OFF-SPEC (PS-F2) |
| R7 | `higher`: mp-depression mechanism; "quantitatively"; compare with data tables; pharma QC | **not a layer** — 5.8.1.1 has no HT statement. Data comparison is base (R4); the mechanism is off-spec | 5.8.1.1 | ROUTE (PS-F3) |
| — | equations, fifas, rp | none | — | correct: none in 5.8.1.1 |

True page routes: CF CH TF TH, all base, no HT or triple layer. Matches what the site ships.

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | th1 | pure substance = only one element or compound | OK | Spec wording. | 5.8.1.1 |
| C2 | th1 | fixed, sharp mp and bp | OK | "specific temperatures". | 5.8.1.1 |
| C3 | th1 | everyday "pure" = "clean or natural" | IMPRECISE (minor) | Spec: "has had nothing added to it, so it is unadulterated and in its natural state, eg pure milk". Use the spec's wording. | 5.8.1.1 |
| C4 | th1 | water 100 °C / 0 °C at standard pressure; iron 1538 °C; ethanol 78.4 °C | OK | All correct. | data |
| C5 | th1 | impure melts and boils over a range | OK | — | 5.8.1.1 |
| C6 | th1; key_note | mp lower than pure | OK | True (beyond spec, harmless). | — |
| C7 | th1; key_note; matching pair 4 | "Boiling point is HIGHER than that of the pure substance" | IMPRECISE | True only for a dissolved non-volatile impurity (salt water boils above 100 °C). A mixture of liquids can boil below the higher-boiling component (ethanol–water). The spec only asks for "specific temperature" vs "range". | 5.8.1.1 (PS-F1) |
| C8 | th2 | pure starts and finishes melting "at the same temperature" | IMPRECISE (minor) | In practice a pure sample melts over a very narrow range (≈1 °C). "Sharp" is the right word. | — |
| C9 | th2 | pure aspirin 135 °C; impure 128–133 °C | OK | Aspirin mp ≈ 135–136 °C. | data |
| C10 | th2 | mixture's temperature changes during boiling | OK | — | — |
| C11 | th2 | compare measured mp/bp with data tables to identify | OK | WS 4.1 data use. | 5.8.1.1 |
| C12 | th3 | thalidomide: "one form was therapeutic, another caused birth defects" | OFF-SPEC / IMPRECISE | Stereochemistry is not GCSE content, and the two forms interconvert in the body, so the "pure form" story is a known oversimplification. | — (PS-F2) |
| C13 | th3 | food, semiconductor, analysis contexts | OK | Context only. | — |
| C14 | `higher` | "impurities disrupt lattice, requiring less energy to melt" | OFF-SPEC | Not in 5.8.1.1 at any tier. Not a layer. | (PS-F3) |
| C15 | common_mistake | "pure" ≠ natural; mixture of two pure chemicals is not pure; orange juice is a mixture | OK | — | 5.8.1.1 |
| C16 | q1 key | melts 118–125 °C, pure 135 °C → impure | OK | Lower and over a range = impure. | 5.8.1.1 |
| C17 | q1 opt 1 / wx1 | "different compound" — "context ... suggests the most likely explanation is impurity" | IMPRECISE (minor) | Aligned to option 1 ✓. The decisive reason is missing: a different *pure* compound would still melt sharply; a range means a mixture. Usable. | 5.8.1.1 |
| C18 | q1 opt 2 / wx2 | heated too quickly | OK | Aligned ✓. | — |
| C19 | q1 opt 3 / wx3 | pressure | OK | Aligned ✓. | — |
| C20 | q2 key | orange juice is a mixture of many compounds | OK | — | 5.8.1.1 |
| C21 | q2 opt 1 / wx1 | preservatives | OK | Aligned ✓. | — |
| C22 | q2 opt 2 / wx2 | distillation | OK | Aligned ✓. | — |
| C23 | q2 opt 3 / wx3 | "Many pure substances change colour (e.g. copper sulfate ...)" | OK | Aligned ✓. Hydrated→anhydrous makes a new substance, but the point (colour change says nothing about purity) holds. | — |
| C24 | matching (to be replaced) | pairs 1–3, 5 | OK | Pair 4 as C7. Pair 5 "only one type of compound": an element is also pure. | — |

Count: **0 WRONG**. IMPRECISE: C3, C7, C8, C17. OFF-SPEC: C12, C14. ROUTE: `higher` field (no HT content exists).

## 4. Frozen items wrong for their route
None. q1 and q2 are correct and base; **both usable on all four routes**.

## 5. For the lesson author
**Misconceptions seen in AQA marking:** "pure" = natural/healthy; a mixture of two pure substances is pure; "impure melts at a lower temperature" without "over a range"; reading a single higher/lower value as proof without comparing to a data value.

**Command words:** Define, Use the data, Explain how the data shows…, Suggest.

**Typical questions** ⚑ examiner-drafted
- *What is meant by a pure substance in chemistry? [1]* — a single element or compound (not mixed with any other substance).
- *Sample A melts at 80 °C. Sample B melts between 72 and 77 °C. Pure naphthalene melts at 80 °C. Which sample is pure? Explain. [2]* — A (1); melts at a specific/sharp temperature that matches the data / B melts over a range (1).

## 6. Verdict
SOURCE OK WITH FLAGS. Core spec content is all present and correct; both quiz items usable on every route. Fix in the re-cut: boiling-point clause (PS-F1), thalidomide line (PS-F2), and the `higher` field is not a Higher layer (PS-F3). No question for Mide.
