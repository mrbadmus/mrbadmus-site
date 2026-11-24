# carbonates-halides-sulfates

Sources: AQA 8462 4.8.3.3, 4.8.3.4 and 4.8.3.5 (TF, TH), chemistry only; no 8464 section. No HT-only line. Ionic equations are HT only (8462 4.1.1.1), so that card is TH only. Required practical 7 (8462), AT 1 and 8. LEGACY record: Design batch 2 (`carbonates-halides-sulfates.dc.html`, family Required practical, routes TF TH). Ladder: Ks4Ladder r1..r4 from the page. Practice set: K.bank, the route's `quiz` list (quiz-carbonates-halides-sulfates.json). Rainford KS4 SOW, Year 10 Chemistry lesson 26, "(CHEM) Tests for negative ions". No LO-sheet rows for this unit. Unit tests in the SOW: Year 10 lessons 32 and 33 "(CHEM) Chemical Analysis & Atmosphere Test" and review (Triple), lessons 43 and 44 "Chemical Analysis, Chemistry of the Atmosphere & Using Resources Test" and review (Combined).

| Spec statement | Where it is covered | Route | Ticked |
|---|---|---|---|
| Carbonates react with dilute acids to form carbon dioxide gas. Carbon dioxide can be identified with limewater. | Reveal: The three tests; Card: Carbonates (verbatim, legacy-fig:rigFig, Na₂CO₃ + 2HCl); Easy mistakes 3; Key fact; Rung 2 (P); Rung 4; Practice Q4 | TF TH | ✓ |
| Halide ions in solution produce precipitates with silver nitrate solution in the presence of dilute nitric acid. Silver chloride is white, silver bromide is cream and silver iodide is yellow. | Start here; Reveal: The three tests; Card: Halides (verbatim); Reveal: The silver halide precipitates; Card: Why the acid goes in first; Easy mistakes 1, 2; Key fact; Rung 1 (cream, bromide); Rung 2 (Q); Rung 4; Practice Q1, Q3, Q5 | TF TH | ✓ |
| Sulfate ions in solution produce a white precipitate with barium chloride solution in the presence of dilute hydrochloric acid. | Reveal: The three tests; Card: Sulfates (verbatim); Card: Why the acid goes in first; Easy mistakes 4; Key fact; Rung 2 (R); Rung 3; Rung 4; Practice Q2 | TF TH | ✓ |
| Required practical 7: use of chemical tests to identify the ions in unknown single ionic compounds covering the ions from Flame tests to Sulfates. | Card: Required practical 7 (five steps, safety); Card: Naming a compound (iron(II) sulfate); Rung 4 (plan) | TF TH | ✓ |
| Students should be able to identify species from the results of the tests in 4.8.3.1 to 4.8.3.5. | Card: Naming a compound; Rung 2 (data table); Rung 4 | TF TH | ✓ |
| (HT, 8462 4.1.1.1) ionic equations where appropriate | Card: Ionic equations (TH only: silver chloride, barium sulfate, carbonate with acid; spectator ions) | TH | ✓ |

**Gaps and mismatches.**
- None. Why the acid goes in first (to remove carbonate ions, and never to add the ion tested for) is how AQA mark schemes credit the method; the spec's own words are only "in the presence of" (UNSURE.md).

**Removed or moved.**
- Removed from the page: the test rack (five unknown salts), the Think again (fizzing), the "Fair test or false positive?" sort, the Higher spectator-ion builder, the Key note and the video. Their teaching is in the cards; their activity ids go (ID list in BRIEF-AN.md).
- Removed: sulfites and sulfur dioxide (old theory). Not in 8462.
- Rung 1 changed: it was practice Q2 (K.find), so the page asked it twice. Now its own question (cream precipitate, bromide) through K.item. Position kept, so `ks4:carbonates-halides-sulfates:<route>#r1` is kept; its options are new.
- Removed: the old rp field "RP Chemistry 4" (it is Required practical 7; not rendered).

**Practice set source.** `K.bank(slug, R.route)`: the route's `quiz` list in all_subtopics_chemistry*.py, from quiz-carbonates-halides-sulfates.json (written by quiz_an.py). Five per route, the same on every route; correct option first (the build shuffles).

| Q | Origin | ks4q: id | Stem | Credited |
|---|---|---|---|---|
| 1 | kept (stem unchanged, options rewritten) | `63f65b45c4` | Why must solutions be acidified with nitric acid before adding silver nitrate to test for halides? | To remove carbonate ions, which would also give a precipitate |
| 2 | kept (stem unchanged, options rewritten) | `929d9cc10e` | A white precipitate forms when barium chloride is added to an acidified solution. What ion is present? | Sulfate, SO₄²⁻ |
| 3 | new | `8fe9fb678f` | Which colour of precipitate shows iodide ions in the silver nitrate test? | Yellow |
| 4 | new | `9fb712a77d` | A solid fizzes with dilute hydrochloric acid, and the gas turns limewater milky. Which ion is in the solid? | Carbonate |
| 5 | new | `20b6f4c495` | Why is hydrochloric acid not used before silver nitrate in the halide test? | It adds chloride ions, so a white precipitate always forms |

**Ladder.** Ks4Ladder r1..r4 from the Design page, positions kept. Rung 1 is rewritten through a logic_edit (see Removed or moved); r2 to r4 are unchanged.

**Assignment pool.** 64 rows for this slug in ks4_data/questions/chemistry/analysis*.py (12 at positions 0–11, the auto window). Faults found are listed in BRIEF-AN.md; none is changed here.
