# metal-hydroxides

Sources: AQA 8462 4.8.3.2 (TF, TH), chemistry only; no 8464 section. No HT-only line in 4.8.3.2. Ionic equations are HT only (8462 4.1.1.1, "(HT only) write balanced half equations and ionic equations where appropriate"), so the ionic-equation card is TH only. Skills: AT 8, WS 2.2. Required practical 7. LEGACY record: Design batch 2 (`metal-hydroxides.dc.html`, family Classify, routes TF TH). Ladder: Ks4Ladder r1..r4 from the page. Practice set: K.bank, the route's `quiz` list (quiz-metal-hydroxides.json). Rainford KS4 SOW, Year 10 Chemistry lesson 25, "(CHEM) Tests for positive ions (reaction with metal hydroxide)". No LO-sheet rows for this unit. Unit tests in the SOW: Year 10 lessons 32 and 33 "(CHEM) Chemical Analysis & Atmosphere Test" and review (Triple), lessons 43 and 44 "Chemical Analysis, Chemistry of the Atmosphere & Using Resources Test" and review (Combined).

| Spec statement | Where it is covered | Route | Ticked |
|---|---|---|---|
| Sodium hydroxide solution can be used to identify some metal ions (cations). | Card: Testing with sodium hydroxide (verbatim); Key words; Practice Q3 | TF TH | ✓ |
| Solutions of aluminium, calcium and magnesium ions form white precipitates when sodium hydroxide solution is added but only the aluminium hydroxide precipitate dissolves in excess sodium hydroxide solution. | Reveal: Precipitates with sodium hydroxide solution; Card: A few drops first, then excess (verbatim); Card: Calcium or magnesium; Easy mistakes 2, 4; Key fact; Rung 2; Rung 3; Rung 4; Practice Q2, Q4 | TF TH | ✓ |
| Solutions of copper(II), iron(II) and iron(III) ions form coloured precipitates when sodium hydroxide solution is added. Copper(II) forms a blue precipitate, iron(II) a green precipitate and iron(III) a brown precipitate. | Start here (copper(II) hydroxide); Reveal; Card: Iron(II) or iron(III); Easy mistakes 1, 3; Key fact; Rung 1 (green, iron(II)); Rung 2 (Q: iron(II)); Practice Q1, Q3 | TF TH | ✓ |
| Students should be able to write balanced equations for the reactions to produce the insoluble hydroxides. | Card: Writing the equation (word equation, rule, CuSO₄ and FeCl₃ with state symbols); Reveal: The formula of each hydroxide; Practice Q5 | TF TH | ✓ |
| Students are not expected to write equations for the production of sodium aluminate. | Respected: no aluminate equation (the old page's Al(OH)₃ + OH⁻ → Al(OH)₄⁻ is removed). | TF TH | ✓ |
| (HT, 8462 4.1.1.1) ionic equations where appropriate | Card: Ionic equations (TH only: M²⁺ and M³⁺ general forms, Cu²⁺ example, spectator ions) | TH | ✓ |
| Students should be able to identify species from the results of the tests in 4.8.3.1 to 4.8.3.5 (WS 2.2) | Card: Calcium or magnesium (flame test); Rung 2 (P, Q, R with a flame column); Rung 4 (plan); Practice Q4 | TF TH | ✓ |
| Required practical 7 (the sodium hydroxide part); AT 8 make precipitates of metal hydroxides | Card: Required practical 7 (three steps, eye protection); Rung 4 (plan) | TF TH | ✓ |

**Gaps and mismatches.**
- None. The live page already taught every line; the lean page keeps its ladder and moves its bench, forge and ionic builder text into cards and reveal tables.

**Removed or moved.**
- Removed from the page: the precipitate bench (six known tubes, four unknowns), the Think again (excess at once), the equation forge (worked copper(II) sulfate and two builds), the Higher ionic-equation builder, the Key note and the video. Their teaching is in the cards; their activity ids go (ID list in BRIEF-AN.md).
- Removed: ammonium ion test with warm sodium hydroxide (the old subtopic data's key note and theory). Not in 8462 4.8.3.2.
- Removed: "amphoteric", the aluminate ion and its equation. The spec says the aluminate equation is not expected.
- Removed: the old rp field "RP Chemistry 4" (it is Required practical 7; not rendered).
- Rung 1 changed: it was practice Q1 (K.find), so the page asked it twice. Now its own question (green precipitate, iron(II)) through K.item. Position kept, so `ks4:metal-hydroxides:<route>#r1` is kept; its options are new (answer key changes).
- The page's Ks4End `legal` line (about the bench's idealised colours) is emptied by lean_ks4, since no bench figure is on the page.
- The old Higher ionic builder (s-ionic) was `data-route="higher"`, so TH only; the lean ionic card has the same audience.

**Practice set source.** `K.bank(slug, R.route)`: the route's `quiz` list in all_subtopics_chemistry*.py, from quiz-metal-hydroxides.json (written by quiz_an.py). Five per route, the same on every route; correct option first (the build shuffles).

| Q | Origin | ks4q: id | Stem | Credited |
|---|---|---|---|---|
| 1 | kept (stem unchanged, options rewritten) | `f522a8493f` | An unknown solution gives a brown precipitate with NaOH solution. Which metal ion is present? | Iron(III), Fe³⁺ |
| 2 | kept (stem unchanged, options rewritten) | `edd6d812a1` | A white precipitate forms when NaOH is added to a solution, then dissolves when excess NaOH is added. Which ion is present? | Aluminium, Al³⁺ |
| 3 | new | `dea6d5a0d7` | Which metal ion gives a blue precipitate with sodium hydroxide solution? | Copper(II) |
| 4 | new | `b795731ef5` | Two solutions both give a white precipitate that stays in excess sodium hydroxide solution. Which test tells calcium ions from magnesium ions? | A flame test |
| 5 | new | `ad3211dcfc` | Which is the balanced equation for iron(III) chloride reacting with sodium hydroxide? | FeCl₃ + 3NaOH → Fe(OH)₃ + 3NaCl |

**Ladder.** Ks4Ladder r1..r4 from the Design page, positions kept. Rung 1 is rewritten through a logic_edit (see Removed or moved); r2 to r4 are unchanged.

**Assignment pool.** 64 rows for this slug in ks4_data/questions/chemistry/analysis*.py (12 at positions 0–11, the auto window). Faults found are listed in BRIEF-AN.md; none is changed here.
