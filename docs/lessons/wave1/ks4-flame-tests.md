# flame-tests

Sources: AQA 8462 4.8.3.1 (TF, TH), in 4.8.3 "Identification of ions by chemical and spectroscopic means (chemistry only)". There is no 8464 section, so the lesson exists on TF and TH only. No HT-only line. Skills: AT 8 (investigate flame colours), WS 2.2. Required practical 7 (8462) covers 4.8.3.1 to 4.8.3.5. NEW record, no legacy page (old generate_site_v5 page). Rainford KS4 SOW, Year 10 Chemistry lesson 24, "(CHEM) Tests for positive ions (Flame Tests) & Flame Emission Spectroscopy" (one SOW lesson; the platform splits it into flame-tests and instrumental-methods). No LO-sheet rows for this unit. Unit tests in the SOW: Year 10 lessons 32 and 33 "(CHEM) Chemical Analysis & Atmosphere Test" and review (Triple), lessons 43 and 44 "Chemical Analysis, Chemistry of the Atmosphere & Using Resources Test" and review (Combined).

| Spec statement | Where it is covered | Route | Ticked |
|---|---|---|---|
| Flame tests can be used to identify some metal ions (cations). | Card: What a flame test shows (verbatim); Key words; Key fact | TF TH | ✓ |
| Lithium, sodium, potassium, calcium and copper compounds produce distinctive colours in flame tests: lithium crimson, sodium yellow, potassium lilac, calcium orange-red, copper green. | Reveal: The five flame colours (AQA's colours, verbatim); Start here (lilac); Easy mistakes 1, 2, 3; Key fact; Rung 1 (both); Rung 2 (first); Rung 3 (second); Rung 4; Practice Q1, Q3, Q4 | TF TH | ✓ |
| If a sample containing a mixture of ions is used some flame colours can be masked. | Card: Mixtures can mask colours (verbatim, sodium hides potassium); Easy mistakes 4; Key fact; Rung 2 (second); Practice Q2 | TF TH | ✓ |
| Students should be able to identify species from the results of the tests in 4.8.3.1 to 4.8.3.5. | Card: Required practical 7 (sodium chloride example); Rung 3 (second, lithium iodide); Rung 4 | TF TH | ✓ |
| Flame colours of other metal ions are not required knowledge. | Respected: only the five are taught. | TF TH | ✓ |
| AT 8: an opportunity to investigate flame colours | Card: How to do a flame test (clean loop, sample, blue flame, record); Rung 3 (first); Rung 4; Practice Q5 | TF TH | ✓ |
| Required practical 7: use of chemical tests to identify the ions in unknown single ionic compounds (4.8.3.1 to 4.8.3.5) | Card: Required practical 7 (named here; the sodium hydroxide and negative-ion parts are taught in Metal hydroxides and Tests for carbonates, halides and sulfates) | TF TH | ✓ |

**Gaps and mismatches.**
- None. "Yellow" for sodium is AQA's word; the old page's "yellow/orange" is kept only inside the kept stem of practice Q1 (its id depends on it).

**Removed or moved.**
- Removed: the electron explanation (excitation to higher levels, emission on falling back, energy-level spacing). Not in 8462 4.8.3.1; it is the CH/TH "higher" box, and is not HT content either.
- Removed: "copper green/blue-green", "lilac/purple", "crimson/red" double colours. AQA gives one colour for each.
- Moved to Instrumental methods: flame emission spectroscopy (4.8.3.7). One line in Dive deeper points there.
- Removed: the old rp field "RP Chemistry 4" (wrong number: it is Required practical 7 in 8462; not rendered).
- Removed: the "Flame Test Colours" matching activity (ks4c:flame-tests:match-1..5).

**Practice set source.** `K.bank(slug, R.route)`: the route's `quiz` list in all_subtopics_chemistry*.py, from quiz-flame-tests.json (written by quiz_an.py). Five per route, the same on every route; correct option first (the build shuffles).

| Q | Origin | ks4q: id | Stem | Credited |
|---|---|---|---|---|
| 1 | kept (stem unchanged, options rewritten) | `eb863683f9` | A flame test on a solution gives a persistent yellow/orange colour. Which ion is most likely present? | Sodium |
| 2 | kept (stem unchanged, options rewritten) | `168554e21f` | Why might sodium contamination cause problems during a flame test for potassium? | Its yellow flame can mask potassium's lilac |
| 3 | new | `d9c288776d` | Which metal ion gives a green flame? | Copper |
| 4 | new | `a8b1f8f7b1` | Which flame colour shows potassium ions? | Lilac |
| 5 | new | `72e25b5960` | Why is the wire loop cleaned before each flame test? | So the last sample does not change the colour |

**Ladder (Ks4Practice, 2·2·2·1, new).**

| Item | Prompt | Answer |
|---|---|---|
| Rung 1 (first) mcq | State the flame colour of lithium compounds. | Crimson |
| Rung 1 (second) mcq | A compound gives an orange-red flame. Identify the metal ion it contains. | Calcium |
| Rung 2 (first) mcq | Solid A gives a green flame. Solid B gives a yellow flame. Solid C gives a lilac flame. Identify the metal ion in each solid. | A copper, B sodium, C potassium |
| Rung 2 (second) mcq | A solid contains sodium ions and potassium ions. Its flame test shows only a yellow flame. Explain why. | Sodium's yellow masks potassium's lilac |
| Rung 3 (first) chain | Describe how to carry out a flame test on a solid. Put the links in order. | Clean a wire loop until it gives no colour in the flame. → Dip the clean loop into the solid, then hold it in a blue Bunsen flame. → Record the flame colour and compare it with the known colours. |
| Rung 3 (second) chain | A white solid gives a crimson flame. With dilute nitric acid and silver nitrate solution it gives a yellow precipitate. Identify the compound. Put the links in order. | The flame test identifies the metal ion: a crimson flame is lithium. → The silver nitrate test then identifies the negative ion: yellow is iodide. → Lithium ions with iodide ions make lithium iodide. |
| Rung 4 (first) write | A technician has three unlabelled white solids: lithium chloride, sodium chloride and potassium chloride. Describe how flame tests could identify each one. Give the result for each. | 5 marking points |

Every chain has one right order: each link uses what the link before it established. Every MCQ passes the length rule (validate.py).

**Assignment pool.** 64 rows for this slug in ks4_data/questions/chemistry/analysis*.py (12 at positions 0–11, the auto window). Faults found are listed in BRIEF-AN.md; none is changed here.
