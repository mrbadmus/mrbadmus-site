# instrumental-methods

Sources: AQA 8462 4.8.3.6 and 4.8.3.7 (TF, TH), chemistry only; no 8464 section. No HT-only line. Skills: AT 8 (observe flame spectra with a hand-held spectroscope), WS 3.6, MS 4a. No required practical. NEW record, no legacy page (old generate_site_v5 page). Rainford KS4 SOW, Year 10 Chemistry lesson 24, "(CHEM) Tests for positive ions (Flame Tests) & Flame Emission Spectroscopy" (the FES half of that lesson; rainford_sow.py maps the lesson to flame-tests only). No LO-sheet rows for this unit. Unit tests in the SOW: Year 10 lessons 32 and 33 "(CHEM) Chemical Analysis & Atmosphere Test" and review (Triple), lessons 43 and 44 "Chemical Analysis, Chemistry of the Atmosphere & Using Resources Test" and review (Combined).

| Spec statement | Where it is covered | Route | Ticked |
|---|---|---|---|
| Elements and compounds can be detected and identified using instrumental methods. Instrumental methods are accurate, sensitive and rapid. | Card: Instrumental methods (verbatim); Start here; Key fact; Practice Q3 | TF TH | ✓ |
| Students should be able to state advantages of instrumental methods compared with the chemical tests in this specification. | Reveal: Instrumental methods compared with chemical tests; Easy mistakes 1; Rung 1 (first); Rung 2 (second); Rung 3 (second); Rung 4; Practice Q1, Q3 | TF TH | ✓ |
| Flame emission spectroscopy is an example of an instrumental method used to analyse metal ions in solutions. | Card: Flame emission spectroscopy (verbatim); Key words | TF TH | ✓ |
| The sample is put into a flame and the light given out is passed through a spectroscope. The output is a line spectrum that can be analysed to identify the metal ions in the solution and measure their concentrations. | Card: Flame emission spectroscopy (four points, verbatim); Card: Reading a line spectrum (brighter lines, higher concentration); Easy mistakes 2; Key fact; Rung 1 (second); Rung 3 (first); Rung 4; Practice Q1, Q2, Q4 | TF TH | ✓ |
| Students should be able to interpret an instrumental result given appropriate data in chart or tabular form, when accompanied by a reference set in the same form, limited to flame emission spectroscopy (WS 3.6, MS 4a). | Card: Reading a line spectrum (fig:emission-spectra, reference set and two samples); Reveal: Which metal ions are in each sample; Easy mistakes 3; Rung 2 (first, tabular lines); Practice Q5 | TF TH | ✓ |
| Intro to 4.8: instrumental methods are particularly useful when the amount of chemical being analysed is small; forensic scientists and drug control scientists rely on them. | Card: Instrumental methods; Rung 3 (second, drug control) | TF TH | ✓ |

**Gaps and mismatches.**
- None. The spec gives no wavelengths; the figure, Rung 2 and practice Q5 give lines as data, as a reference set would (UNSURE.md, the line positions).

**Removed or moved.**
- Removed: electrons excited to higher levels and falling back (the CH/TH "higher" box and theory). Not in 8462 4.8.3.7.
- Removed: mass spectrometry, infrared spectroscopy, gas chromatography, retention times. Not in the spec.
- Removed: named wavelengths to learn (sodium 589 nm doublet, potassium 766/404 nm, lithium 671 nm, calcium 422/616 nm). They now appear only as data in a question or the reference figure.
- Removed: "objective" and "less material needed" as named advantages; the spec's three words are accurate, sensitive and rapid. Drawbacks (cost, trained staff, calibration) moved to Dive deeper.
- Removed: the "Instrumental Analysis" matching activity (ks4c:instrumental-methods:match-1..5).

**Practice set source.** `K.bank(slug, R.route)`: the route's `quiz` list in all_subtopics_chemistry*.py, from quiz-instrumental-methods.json (written by quiz_an.py). Five per route, the same on every route; correct option first (the build shuffles).

| Q | Origin | ks4q: id | Stem | Credited |
|---|---|---|---|---|
| 1 | kept (stem unchanged, options rewritten) | `90c4fdc08b` | What additional information does flame emission spectroscopy give that a simple flame test cannot? | The concentration of the metal ions |
| 2 | kept (stem unchanged, options rewritten) | `cba8eb8c66` | A flame emission spectrum shows a line of high intensity at 589 nm. What does the high intensity indicate? | A high concentration of that metal ion |
| 3 | new | `2a2d83516b` | Which three words describe instrumental methods? | Accurate, sensitive and rapid |
| 4 | new | `8bb6075824` | What is the output of flame emission spectroscopy? | A line spectrum |
| 5 | new | `1afa20a222` | Lithium ions give lines at 610 nm and 671 nm. A sample's spectrum has lines at 589 nm, 610 nm and 671 nm. What does this show? | Lithium ions are present, with another metal ion |

**Ladder (Ks4Practice, 2·2·2·1, new).**

| Item | Prompt | Answer |
|---|---|---|
| Rung 1 (first) mcq | Give one advantage of instrumental methods compared with chemical tests. | They are more sensitive |
| Rung 1 (second) mcq | A sample is put into a flame. The light given out is analysed to identify the metal ions. What is the light passed through? | A spectroscope |
| Rung 2 (first) mcq | Reference lines: sodium 589 nm; potassium 404 nm and 766 nm; lithium 610 nm and 671 nm. A sample's spectrum has lines at 404, 589 and 766 nm. Which metal ions are in the sample? | Sodium and potassium |
| Rung 2 (second) mcq | A solution contains sodium ions and potassium ions. Explain why flame emission spectroscopy can identify both, but a flame test may not. | Its spectrum has lines for both ions, but in a flame test yellow masks lilac |
| Rung 3 (first) chain | Describe how flame emission spectroscopy identifies the metal ions in a solution. Put the links in order. | The sample is put into a flame. → The light given out is passed through a spectroscope, which gives a line spectrum. → The line spectrum is compared with reference spectra to identify the metal ions. |
| Rung 3 (second) chain | A drug control scientist tests hundreds of urine samples a day for tiny amounts of a banned drug. Explain why an instrumental method is used. Put the links in order. | Each sample may contain only a tiny amount of the drug. → Instrumental methods are sensitive, so they can detect very small amounts. → They are also rapid and accurate, so many samples can be tested quickly and the results trusted. |
| Rung 4 (first) write | A scientist must find which metal ions are in a solution, and how much of each. Compare using flame tests with using flame emission spectroscopy. | 5 marking points |

Every chain has one right order: each link uses what the link before it established. Every MCQ passes the length rule (validate.py).

**Assignment pool.** 64 rows for this slug in ks4_data/questions/chemistry/analysis*.py (12 at positions 0–11, the auto window). Faults found are listed in BRIEF-AN.md; none is changed here.
