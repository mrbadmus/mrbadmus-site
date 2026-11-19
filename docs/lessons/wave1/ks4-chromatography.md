# chromatography

Sources: AQA 8464 5.8.1.3 (CF, CH) and 8462 4.8.1.3 (TF, TH), word for word the same, Rf on every route. No HT-only or chemistry-only line. Skills: WS 2.2, 3.1, 2, 3; MS 1a, 1c, 1d, 2a. Required practical: 8464 Required practical activity 12 (CF, CH); 8462 Required practical 6 (TF, TH); the same practical (AT 1 and 4). Equation: Rf = distance moved by substance ÷ distance moved by solvent (given in the spec, no symbols). NEW record, no legacy page (old generate_site_v5 page). Rainford KS4 SOW, Year 10 Chemistry lessons 22 and 23, "Chromatography RP" and "Chromatography RP 2" (two lessons on the required practical). No LO-sheet rows for this unit. Unit tests in the SOW: Year 10 lessons 32 and 33 "(CHEM) Chemical Analysis & Atmosphere Test" and review (Triple), lessons 43 and 44 "Chemical Analysis, Chemistry of the Atmosphere & Using Resources Test" and review (Combined).

| Spec statement | Where it is covered | Route | Ticked |
|---|---|---|---|
| Chromatography can be used to separate mixtures and can give information to help identify substances. | Card: What chromatography does (verbatim); Start here; Card: Identifying a substance | CF CH TF TH | ✓ |
| Chromatography involves a stationary phase and a mobile phase. | Card: Two phases (verbatim, paper and solvent); Key words; Key fact; Rung 1 (first); Rung 3 (first, herring) | CF CH TF TH | ✓ |
| Separation depends on the distribution of substances between the phases. | Card: Two phases (verbatim); Card: How paper chromatography separates a mixture; Key fact; Rung 3 (first) | CF CH TF TH | ✓ |
| The ratio of the distance moved by a compound (centre of spot from origin) to the distance moved by the solvent can be expressed as its Rf value: Rf = distance moved by substance ÷ distance moved by solvent | Card: Rf value (verbatim, triangle EQ_RF); Card: Reading a chromatogram (fig:chromatogram); Card: Worked examples (cfifa: 0.45, 27 mm with 6.0 cm, 0.60 × 7.5); Easy mistakes 1, 2; Key fact; Rung 1 (second); Rung 2 (both); Rung 4; Practice Q3 | CF CH TF TH | ✓ |
| Different compounds have different Rf values in different solvents, which can be used to help identify the compounds. | Card: Identifying a substance (verbatim, then the reference-spot method); Practice Q4 | CF CH TF TH | ✓ |
| The compounds in a mixture may separate into different spots depending on the solvent but a pure compound will produce a single spot in all solvents. | Card: Pure or a mixture (verbatim); Easy mistakes 4; Key fact; Rung 3 (second); Practice Q1 | CF CH TF TH | ✓ |
| Explain how paper chromatography separates mixtures | Card: How paper chromatography separates a mixture (five steps); Rung 3 (first) | CF CH TF TH | ✓ |
| Suggest how chromatographic methods can be used for distinguishing pure substances from impure substances | Card: Pure or a mixture (run in two or three solvents); Rung 3 (second); Dive deeper: Command words | CF CH TF TH | ✓ |
| Interpret chromatograms and determine Rf values from chromatograms | Card: Reading a chromatogram (fig:chromatogram: start line, solvent front, distances); Card: Rf value; cfifa; Rung 2 (both); Practice Q3, Q4 | CF CH TF TH | ✓ |
| Provide answers to an appropriate number of significant figures (MS 2a) | Card: Rf value ("usually two, like the distances you measured"); every worked answer to 2 s.f. (0.45, 0.40, 0.50, 0.70, 0.30) | CF CH TF TH | ✓ |
| MS 1a decimal form; MS 1c ratios; MS 1d estimates | Rf as a decimal ratio throughout; "always less than 1" (an estimate check) in Card: Rf value and Easy mistakes 1 | CF CH TF TH | ✓ |
| Required practical activity 12 (8464) / Required practical 6 (8462): investigate how paper chromatography can be used to separate and tell the difference between coloured substances. Students should calculate Rf values. | Card: Required practical activity 12 (CF CH, notTriple) / Card: Required practical 6 (TF TH, isTriple), same six-step method; Reveal: Why each step is done; Easy mistakes 3; Rung 4 (method); Practice Q2, Q5 | CF CH (RP 12) / TF TH (RP 6) | ✓ |

**Gaps and mismatches.**
- None in the content lines. The spec gives no symbols for the Rf equation; the triangle uses d₁ and d₂, each named in full (UNSURE.md).
- The 8464 and 8462 practical numbers differ (12 and 6); each route shows only its own.

**Removed or moved.**
- Removed: "retention factor" as a name for Rf, two-way chromatography, HPLC, GC and GC-MS, forensic ink and sports-doping applications. None is in 5.8.1.3 / 4.8.1.3.
- Removed: the CH/TH "higher" box (relative solubility, two-way chromatography, HPLC, GC). Not HT content; the relative-solubility idea is taught on every route in the separation card, because the spec's "distribution between the phases" needs it.
- Removed: the old rp field "RP1 (Chemistry)" (wrong number; not rendered on the lean page).
- Removed: the "Chromatography Concepts" matching activity (ks4c:chromatography:match-1..5).
- Old practice Q2's stem writes "ABOVE"; the JSON writes "above". The ks4q: id is a hash of the lower-cased stem, so the id is unchanged (checked).

**Practice set source.** `K.bank(slug, R.route)`: the route's `quiz` list in all_subtopics_chemistry*.py, from quiz-chromatography.json (written by quiz_an.py). Five per route, the same on every route; correct option first (the build shuffles).

| Q | Origin | ks4q: id | Stem | Credited |
|---|---|---|---|---|
| 1 | kept (stem unchanged, options rewritten) | `e543b9c246` | A student runs chromatography on a food colouring and gets three spots. What does this tell them? | It is a mixture of at least three substances |
| 2 | kept (stem unchanged, options rewritten) | `e708850856` | In chromatography, why must the initial spot be placed above the solvent level? | So the spot does not dissolve into the solvent in the beaker |
| 3 | new | `c98c91f536` | A spot moves 3.0 cm from the start line. The solvent front is 7.5 cm from the start line. What is the Rf value? | 0.40 |
| 4 | new | `3cc4c51eb3` | A spot from an unknown dye has the same Rf value and colour as a known dye, in the same solvent. What does this suggest? | They are probably the same substance |
| 5 | new | `fc39c92b53` | Why is the start line drawn in pencil? | Pencil does not dissolve in the solvent |

**Ladder (Ks4Practice, 2·2·2·1, new).**

| Item | Prompt | Answer |
|---|---|---|
| Rung 1 (first) mcq | In paper chromatography, what is the mobile phase? | The solvent |
| Rung 1 (second) mcq | Give the equation for an Rf value. | distance moved by substance ÷ distance moved by solvent |
| Rung 2 (first) calc | A spot moves 4.2 cm from the start line. The solvent front is 6.0 cm from the start line. Calculate the Rf value. | 0.7 no unit |
| Rung 2 (second) calc | A spot moves 18 mm from the start line. The solvent front is 6.0 cm from the start line. Calculate the Rf value. | 0.3 no unit |
| Rung 3 (first) chain | Explain how paper chromatography separates the dyes in an ink. Put the links in order. | The solvent moves up the paper and dissolves the dyes in the ink spot. → The dissolved dyes are carried up the paper, but each dye is attracted to the paper by a different amount. → So each dye moves a different distance, and the dyes separate into different spots. |
| Rung 3 (second) chain | A food colouring gives one spot in water. Suggest how a student could find out whether it is a pure substance. Put the links in order. | One spot in water is not enough: two dyes could move the same distance in that solvent. → So run the food colouring again in a different solvent, and then in a third. → If it gives a single spot in every solvent, it is probably a pure substance. |
| Rung 4 (first) write | Describe how to use paper chromatography to find the Rf value of a dye in an ink. | 5 marking points |

Every chain has one right order: each link uses what the link before it established. Every MCQ passes the length rule (validate.py).

**Worked examples.** cfifa: 3.6 ÷ 8.0 = 0.45; 27 mm with 6.0 cm = 60 mm, 27 ÷ 60 = 0.45; d₁ = 0.60 × 7.5 = 4.5 cm. Questions rf-q1 2.4 ÷ 6.0 = 0.40; rf-q2 9.0 cm = 90 mm, 45 ÷ 90 = 0.50.

**Assignment pool.** 64 rows for this slug in ks4_data/questions/chemistry/analysis*.py (12 at positions 0–11, the auto window). Faults found are listed in BRIEF-AN.md; none is changed here.
