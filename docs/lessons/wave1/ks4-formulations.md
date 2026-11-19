# formulations

Sources: AQA 8464 5.8.1.2 (CF, CH) and 8462 4.8.1.2 (TF, TH), word for word the same. No HT-only or chemistry-only line. Skills: WS 1.4, 2.2. No required practical, no equation. NEW record, no legacy page (old generate_site_v5 page). Rainford KS4 SOW, Year 10 Chemistry lesson 21, "Pure Substances, Formulations & Testing For Gases" (shared with pure-substances and testing-for-gases). No LO-sheet rows for this unit. Unit tests in the SOW: Year 10 lessons 32 and 33 "(CHEM) Chemical Analysis & Atmosphere Test" and review (Triple), lessons 43 and 44 "Chemical Analysis, Chemistry of the Atmosphere & Using Resources Test" and review (Combined).

| Spec statement | Where it is covered | Route | Ticked |
|---|---|---|---|
| A formulation is a mixture that has been designed as a useful product. | Start here; Card: What a formulation is (verbatim); Key fact; Rung 1 (first); Rung 3 (first); Rung 4; Practice Q1, Q4 | CF CH TF TH | ✓ |
| Many products are complex mixtures in which each chemical has a particular purpose. | Card: What a formulation is (verbatim); Card: Examples (one line per product); Rung 3 (second) | CF CH TF TH | ✓ |
| Formulations are made by mixing the components in carefully measured quantities to ensure that the product has the required properties. | Card: Carefully measured quantities (verbatim); Easy mistakes 3; Key fact; Rung 1 (second); Rung 2 (second); Rung 3 (both); Rung 4; Practice Q2, Q4, Q5 | CF CH TF TH | ✓ |
| Formulations include fuels, cleaning agents, paints, medicines, alloys, fertilisers and foods. | Card: Examples (the spec's list, verbatim, then paint, tablet, alloy, fertiliser); Reveal: Formulation or not; Practice Q3, Q5 | CF CH TF TH | ✓ |
| Students should be able to identify formulations given appropriate information. | Card: Identifying a formulation (three things to look for); Reveal: Formulation or not; Rung 2 (first); Rung 3 (first, hand-cream label); Rung 4; Practice Q1, Q3 | CF CH TF TH | ✓ |
| Students do not need to know the names of components in proprietary products. | Respected: no brand and no named additive anywhere. Components are described by their job ("one keeps the paint runny"). | CF CH TF TH | ✓ |

**Gaps and mismatches.**
- None. "Component" is not defined in the spec; the record defines it once ("Each chemical in the mixture is called a component").

**Removed or moved.**
- Removed: binder, filler, coating, preservative, anti-knock agents, corrosion inhibitors, electrolytes, NPK ratios, SPF, emollients. Named components of products, which the spec says are not needed.
- Removed: the CH/TH "higher" box (atom economy in drug synthesis, green chemistry). Not in 5.8.1.2, and atom economy is 8462 4.3.3.2, Triple only.
- Removed: "chemical tests can identify the components" (flame tests and pH in a formulations lesson).
- Removed: the "Formulation Components" matching activity (ks4c:formulations:match-1..5).
- Tap water is used nowhere as a "not a formulation" example: water companies add measured amounts of chemicals, so it is arguable. Old practice Q1's tap-water distractor is replaced by muddy river water.

**Practice set source.** `K.bank(slug, R.route)`: the route's `quiz` list in all_subtopics_chemistry*.py, from quiz-formulations.json (written by quiz_an.py). Five per route, the same on every route; correct option first (the build shuffles).

| Q | Origin | ks4q: id | Stem | Credited |
|---|---|---|---|---|
| 1 | kept (stem unchanged, options rewritten) | `2d89373008` | Which of the following is a formulation? | Toothpaste |
| 2 | kept (stem unchanged, options rewritten) | `8c51ad1bc5` | Why must the amount of active ingredient in a medicine be precise? | Too little does not work, and too much can be harmful |
| 3 | new | `731b610f34` | Which list contains only formulations? | Paint, fuel and fertiliser |
| 4 | new | `c83c229207` | A fertiliser is a formulation. What does this tell you about it? | It is a mixture of measured amounts of components |
| 5 | new | `56e28cb129` | Why is an alloy such as steel described as a formulation? | Measured amounts of elements are mixed to give its properties |

**Ladder (Ks4Practice, 2·2·2·1, new).**

| Item | Prompt | Answer |
|---|---|---|
| Rung 1 (first) mcq | What is a formulation? | A mixture designed as a useful product |
| Rung 1 (second) mcq | State why the components of a formulation are mixed in measured quantities. | So the product has the required properties |
| Rung 2 (first) mcq | Which of these is a formulation? | Gloss paint for a front door |
| Rung 2 (second) mcq | A company changes the amounts of the chemicals in its paint. Explain why the paint may no longer do its job. | Its properties depend on the measured amounts of each component |
| Rung 3 (first) chain | A label on a hand cream reads: water 70%, oil 20%, wax 8%, perfume 2%. Explain how the label shows that the hand cream is a formulation. Put the links in order. | The label lists four substances, so the hand cream is a mixture. → This mixture has each substance in a measured amount, given as a percentage. → So it is a mixture designed as a useful product: a formulation. |
| Rung 3 (second) chain | Explain why a medicine tablet must contain a measured amount of its drug. Put the links in order. | The drug is the component of the tablet that treats the illness. → So the amount matters: too little and the tablet does not work; too much and it can be harmful. → So the drug is mixed in a carefully measured quantity, to give the tablet the required properties. |
| Rung 4 (first) write | A student says: “Sea water and paint are both mixtures, so both are formulations.” Explain whether the student is right. | 5 marking points |

Every chain has one right order: each link uses what the link before it established. Every MCQ passes the length rule (validate.py).

**Assignment pool.** 64 rows for this slug in ks4_data/questions/chemistry/analysis*.py (12 at positions 0–11, the auto window). Faults found are listed in BRIEF-AN.md; none is changed here.
