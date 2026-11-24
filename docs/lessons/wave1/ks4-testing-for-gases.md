# testing-for-gases

Sources: AQA 8464 5.8.2.1 to 5.8.2.4 (CF, CH) and 8462 4.8.2.1 to 4.8.2.4 (TF, TH), word for word the same. No HT-only or chemistry-only line. No required practical (the tests are used in Required practical 7 on Triple), no equation. NEW record, no legacy page (old generate_site_v5 page). Rainford KS4 SOW, Year 10 Chemistry lesson 21, "Pure Substances, Formulations & Testing For Gases" (shared). No LO-sheet rows for this unit. Unit tests in the SOW: Year 10 lessons 32 and 33 "(CHEM) Chemical Analysis & Atmosphere Test" and review (Triple), lessons 43 and 44 "Chemical Analysis, Chemistry of the Atmosphere & Using Resources Test" and review (Combined).

| Spec statement | Where it is covered | Route | Ticked |
|---|---|---|---|
| The test for hydrogen uses a burning splint held at the open end of a test tube of the gas. Hydrogen burns rapidly with a pop sound. | Reveal: The four gas tests; Card: Hydrogen (verbatim); Easy mistakes 1; Key fact; Rung 2 (second); Rung 4; Practice Q3 | CF CH TF TH | ✓ |
| The test for oxygen uses a glowing splint inserted into a test tube of the gas. The splint relights in oxygen. | Start here; Reveal; Card: Oxygen (verbatim, what a glowing splint is); Key fact; Rung 1 (first); Rung 2 (first); Rung 3 (first); Rung 4; Practice Q1 | CF CH TF TH | ✓ |
| The test for carbon dioxide uses an aqueous solution of calcium hydroxide (lime water). When carbon dioxide is shaken with or bubbled through limewater the limewater turns milky (cloudy). | Reveal; Card: Carbon dioxide (verbatim, fig:limewater-test); Easy mistakes 2, 4; Key fact; Rung 1 (second); Rung 3 (second); Rung 4; Practice Q4 | CF CH TF TH | ✓ |
| The test for chlorine uses litmus paper. When damp litmus paper is put into chlorine gas the litmus paper is bleached and turns white. | Reveal; Card: Chlorine (verbatim); Easy mistakes 3; Key fact; Rung 4; Practice Q2, Q5 | CF CH TF TH | ✓ |

**Gaps and mismatches.**
- None. "Squeaky pop" is not AQA's phrase (the spec says "a pop sound"); the card gives AQA's words first and names "squeaky pop" as what it is often called.
- Practice Q2 (kept stem, "Why must the litmus paper be damp...") asks something the spec does not explain. The credited option is the safe one, "Chlorine needs water on the paper to bleach it", with no hypochlorous acid (UNSURE.md).

**Removed or moved.**
- Removed: H₂ + O₂ → H₂O as "explosive combustion" (and unbalanced), excess CO₂ clearing limewater (calcium hydrogencarbonate), Cl₂ + H₂O → HCl + HClO, "a lit splint would just burn faster in oxygen". Beyond 5.8.2 / 4.8.2.
- Moved to Dive deeper: why limewater turns milky (Ca(OH)₂ + CO₂ → CaCO₃ + H₂O), where the gases come from (metal and acid, carbonate and acid, electrolysis of sodium chloride solution).
- Removed: the CH/TH "higher" box (equations for each test, an ionic equation for the limewater test). 5.8.2 has no HT content.
- Removed: the "Gas Test Match" matching activity (ks4c:testing-for-gases:match-1..4).

**Practice set source.** `K.bank(slug, R.route)`: the route's `quiz` list in all_subtopics_chemistry*.py, from quiz-testing-for-gases.json (written by quiz_an.py). Five per route, the same on every route; correct option first (the build shuffles).

| Q | Origin | ks4q: id | Stem | Credited |
|---|---|---|---|---|
| 1 | kept (stem unchanged, options rewritten) | `eafdf73dc6` | A student collects a gas and holds a glowing splint near it. The splint relights. What gas is present? | Oxygen |
| 2 | kept (stem unchanged, options rewritten) | `7a8ba01e25` | Why must the litmus paper be damp when testing for chlorine? | Chlorine needs water on the paper to bleach it |
| 3 | new | `9789588fca` | A burning splint is held at the open end of a test tube of gas. The gas burns rapidly with a pop. Which gas is it? | Hydrogen |
| 4 | new | `c2238dd950` | What is limewater? | Calcium hydroxide solution |
| 5 | new | `89bd771fda` | What is seen when damp litmus paper is put into chlorine gas? | It is bleached and turns white |

**Ladder (Ks4Practice, 2·2·2·1, new).**

| Item | Prompt | Answer |
|---|---|---|
| Rung 1 (first) mcq | Describe the result of the test for oxygen. | A glowing splint relights |
| Rung 1 (second) mcq | Name the solution used to test for carbon dioxide. | Limewater |
| Rung 2 (first) mcq | A gas has no effect on damp litmus paper or on limewater. A glowing splint put into the gas relights. Identify the gas. | Oxygen |
| Rung 2 (second) mcq | Zinc reacts with dilute hydrochloric acid and gives off a gas. Describe how to show that the gas is hydrogen. | Hold a burning splint at the mouth of the tube: it pops |
| Rung 3 (first) chain | Hydrogen peroxide breaks down to give a gas. Describe how to show that the gas is oxygen. Put the links in order. | Light a splint, then blow it out so that it is only glowing. → Put the glowing splint into the test tube of gas. → The splint relights, so the gas is oxygen. |
| Rung 3 (second) chain | Describe how to show that a gas given off by a reaction is carbon dioxide. Put the links in order. | Collect the gas, or pass it through a delivery tube. → Bubble the gas through limewater, or shake it with limewater. → The limewater turns milky (cloudy), so the gas is carbon dioxide. |
| Rung 4 (first) write | Four test tubes each hold a different gas: hydrogen, oxygen, carbon dioxide and chlorine. Describe a test to identify each gas, and give the result for each. | 4 marking points |

Every chain has one right order: each link uses what the link before it established. Every MCQ passes the length rule (validate.py).

**Assignment pool.** 64 rows for this slug in ks4_data/questions/chemistry/analysis*.py (12 at positions 0–11, the auto window). Faults found are listed in BRIEF-AN.md; none is changed here.
