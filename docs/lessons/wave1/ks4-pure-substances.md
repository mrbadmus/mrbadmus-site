# pure-substances

Sources: AQA 8464 5.8.1.1 (CF, CH) and 8462 4.8.1.1 (TF, TH), read from the PDFs on Mide's Mac (spec-8464-5.8.txt, spec-8462-4.8.txt in this folder), word for word the same. No HT-only or chemistry-only line. Skills: WS 2.2, 4.1. No required practical, no equation. NEW record, no legacy page (the old generate_site_v5 page; no Design batch holds this slug). Rainford KS4 SOW, Year 10 Chemistry lesson 21, "Pure Substances, Formulations & Testing For Gases" (one lesson for three subtopics; rainford_sow.py maps it to pure-substances). The SOW's Chemistry LO sheet has no Chemical analysis rows, so there are no Rainford outcomes beyond the lesson title. Unit tests in the SOW: Year 10 lessons 32 and 33 "(CHEM) Chemical Analysis & Atmosphere Test" and review (Triple), lessons 43 and 44 "Chemical Analysis, Chemistry of the Atmosphere & Using Resources Test" and review (Combined).

| Spec statement | Where it is covered | Route | Ticked |
|---|---|---|---|
| In chemistry, a pure substance is a single element or compound, not mixed with any other substance. | Start here; Card: Pure in chemistry (verbatim); Reveal: Pure substance or mixture; Key fact; Rung 1 (first); Rung 2 (second); Rung 4; Practice Q2, Q3 | CF CH TF TH | ✓ |
| Pure elements and compounds melt and boil at specific temperatures. | Card: Melting and boiling points (verbatim); Reveal (How it melts, How it boils); Easy mistakes 3; Key fact; Rung 1 (second); Rung 3 (both); Practice Q4 | CF CH TF TH | ✓ |
| Melting point and boiling point data can be used to distinguish pure substances from mixtures. | Card: Melting and boiling points; Card: Using melting point data; Key fact; Rung 2 (first); Rung 3 (both); Rung 4; Practice Q1, Q4 | CF CH TF TH | ✓ |
| In everyday language, a pure substance can mean a substance that has had nothing added to it, so it is unadulterated and in its natural state, eg pure milk. | Card: Pure in everyday language (verbatim, pure milk); Start here (100% pure juice); Easy mistakes 1; Rung 1 (first, distractor); Rung 2 (second, honey); Practice Q2, Q5 | CF CH TF TH | ✓ |
| Students should be able to use melting point and boiling point data to distinguish pure from impure substances. | Card: Using melting point data (122 °C worked example); Rung 2 (first, 81 °C); Rung 3 (first, 128–133 °C against 136 °C; second, boiling point of water); Rung 4; Practice Q1, Q4 | CF CH TF TH | ✓ |

**Gaps and mismatches.**
- None in the content lines. The spec says "mixtures" in one sentence and "impure substances" in the next; the record uses both, and says "impure: a mixture" where they meet.
- "A mixture melts over a range of temperatures" is how AQA mark schemes credit the purity test, but the spec's own words stop at "distinguish". It is taught as the test (cards, rungs). The direction of the change (an impurity lowers the melting point, raises the boiling point) is in Dive deeper only: UNSURE.md.

**Removed or moved.**
- Removed: thalidomide and stereochemistry, semiconductor silicon, sucrose food standards, "melting point depression" and "boiling point elevation" as named terms, pure iron (1538 °C) and ethanol (78.4 °C) as facts to learn. None is in 5.8.1.1 / 4.8.1.1.
- Removed: the CH/TH "higher" box (lattice disruption, pharmaceutical quality control). 5.8.1.1 has no HT content.
- Removed: the "Pure or Impure?" matching activity (ks4c:pure-substances:match-1..5).
- Old common-mistake line ("pure does NOT mean natural") kept as Easy mistakes 1, without capitals.

**Practice set source.** `K.bank(slug, R.route)`: the route's `quiz` list in all_subtopics_chemistry*.py, from quiz-pure-substances.json (written by quiz_an.py). Five per route, the same on every route; correct option first (the build shuffles).

| Q | Origin | ks4q: id | Stem | Credited |
|---|---|---|---|---|
| 1 | kept (stem unchanged, options rewritten) | `6b6f303d5e` | A student heats a solid and records that it melts between 118°C and 125°C. Pure samples of this compound melt at 135°C. What does this suggest? | The sample is impure: it is a mixture |
| 2 | kept (stem unchanged, options rewritten) | `5baa7da162` | Why is 'pure orange juice' not a pure substance in the chemical sense? | It is a mixture of water, sugars, acids and other compounds |
| 3 | new | `75628ad7bb` | Which of these is a pure substance in chemistry? | Oxygen gas |
| 4 | new | `23578c57ff` | Pure ethanol boils at 78 °C. Which liquid is most likely to be pure ethanol? | A liquid that boils at 78 °C |
| 5 | new | `434fa0de86` | In everyday language, what can a 'pure' substance mean? | Nothing has been added to it |

**Ladder (Ks4Practice, 2·2·2·1, new).**

| Item | Prompt | Answer |
|---|---|---|
| Rung 1 (first) mcq | Define a pure substance in chemistry. | A single element or compound, not mixed with any other substance |
| Rung 1 (second) mcq | State how a pure substance melts. | At a specific temperature |
| Rung 2 (first) mcq | Pure compound Y melts at 81 °C. Sample P melts at 81 °C. Sample Q melts from 74 °C to 78 °C. Which statement is correct? | P is pure Y, and Q is impure |
| Rung 2 (second) mcq | A shop sells “pure honey”. Explain why a chemist would not call it a pure substance. | Honey is a mixture of several compounds, such as sugars and water |
| Rung 3 (first) chain | Pure compound Z melts at 136 °C. A student heats a white solid that is thought to be Z. It starts to melt at 128 °C and has all melted at 133 °C. Explain what her results show. Put the links in order. | The solid starts to melt at 128 °C and has all melted at 133 °C. → So it melts over a range of temperatures, not at one specific temperature. → So the solid is a mixture: it is not pure Z. |
| Rung 3 (second) chain | A colourless liquid is thought to be pure water. Explain how its boiling point shows whether it is pure. Put the links in order. | Heat the liquid and measure the temperature at which it boils. → Compare it with the boiling point of pure water, 100 °C. → If it boils at 100 °C it is pure water; if it boils over a range of temperatures it is a mixture. |
| Rung 4 (first) write | Two bottles are labelled “pure water”. One holds distilled water. The other holds spring water, which has minerals dissolved in it. Explain which one is a pure substance in chemistry, and how boiling point data could show this. | 5 marking points |

Every chain has one right order: each link uses what the link before it established. Every MCQ passes the length rule (validate.py).

**Assignment pool.** 64 rows for this slug in ks4_data/questions/chemistry/analysis*.py (12 at positions 0–11, the auto window). Faults found are listed in BRIEF-AN.md; none is changed here.
