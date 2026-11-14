# chemical-measurements

Sources: AQA 8464 5.3.1.4 (CF CH) and 8462 4.3.1.4 (TF TH), "Chemical measurements", read from spec-8464.txt and spec-8462.txt (the brief's "5.3.1.3 / 4.3.1.3" is the mass-changes statement; the numbers here are the specs' own). Same wording in both, skills WS 3.4. Working Scientifically WS 3.7 (accuracy, precision, repeatability, reproducibility, random and systematic error, anomalies) and AT 1 (apparatus for volumes), read from full-8462.txt and full-8464.txt, are the same in both specs and are tested by the legacy ladder and practice set. No HT-only lines. Titration, pipettes and burettes are 8462 4.4.2.5 (chemistry only); 8464 never names them. LEGACY page (batch 11, Ks4Practice 2·2·2·1).

| Spec statement | Where it is covered | Route | Ticked |
|---|---|---|---|
| Whenever a measurement is made there is always some uncertainty about the result obtained | Card: There is always uncertainty; Key fact | CF CH TF TH | ✓ |
| Represent the distribution of results and make estimations of uncertainty | Card: Showing the spread (legacy-fig:nlFig); Reveal: Readings of 24.10, 24.30 and 24.20 cm³ | CF CH TF TH | ✓ |
| Use the range of a set of measurements about the mean as a measure of uncertainty | Card: The range about the mean; Reveal; Card: Worked examples (cfifa); Card: Anomalous results (steps-attempt); Easy mistakes; Key fact; Rung 2 calc 1; Rung 4; Quiz Q1 | CF CH TF TH | ✓ |
| WS 3.7: accurate, precise, repeatable, reproducible (AQA's definitions) | Reveal: Four words, used exactly; Rung 1 Q1; Quiz Q3 | CF CH TF TH | ✓ |
| WS 3.7: random error reduced by more measurements and a mean; systematic error a consistent difference | Card: Random and systematic error; Easy mistakes; Rung 1 Q2; Rung 4; Quiz Q4 | CF CH TF TH | ✓ |
| WS 3.7: anomalous values examined and, if a product of a poor measurement, ignored | Card: Anomalous results; Rung 2 calc 2; Rung 3 chain 1; Rung 4; Quiz Q2 | CF CH TF TH | ✓ |
| AT 1: appropriate apparatus to measure volumes of liquids | Card: Reading a measuring cylinder; Rung 3 chain 2; Quiz Q5 | CF CH TF TH | ✓ |
| 4.4.2.5 (chemistry only): pipette and burette in a titration | Dive deeper: Burettes and pipettes (legacy-fig:apFig), routes TF TH | TF TH | ✓ |

**Gaps and mismatches.** The spec gives the range about the mean as the measure of uncertainty but no formula. The page (and this record) state it as mean ± half the range. I believe that is how AQA mark schemes credit it, but I could not check a mark scheme here: flagged for Mide's examiner check. The old page taught percentage uncertainty as an "extension, not on the specification", with a formula triangle; it is removed. Titres, pipettes and burettes were on every route, in the practice set, a rung and a CFIFA question; they are now Triple-only Dive deeper, and the Combined items use measuring cylinders and plain volumes.

**Practice set source.** The page's own hard-coded `BANK` (`BANK.map((q) => K.item(q))`), the same five on every route. It does not read the subtopic `quiz` list (the old generator list is not used by this page), so fixes are logic_edits and there is no quiz-chemical-measurements.json.

**Audit of the ladder, worked examples and practice set.**

| Item | Verdict |
|---|---|
| Rung 1 Q1 Accurate | ok (AQA's words) |
| Rung 1 Q2 Un-zeroed balance: systematic error | ok |
| Rung 2 calc 1 Three titres 19.80, 20.00, 19.90 | ok for the answer (± 0.10 cm³; mean 19.90). Fault: "titres" (chemistry only) on every route. Fix: "Three volumes are 19.80, 20.00 and 19.90 cm³." |
| Rung 2 calc 2 6.2, 6.4, 9.1, 6.3 °C | ok (9.1 anomalous; 18.9 ÷ 3 = 6.3 °C) |
| Rung 3 chain 1 Leaving out an anomaly | ok. One forced order: far from the cluster, so anomalous, so it is left out. |
| Rung 3 chain 2 Pipette for a titration | Fault: chemistry-only apparatus and context on every route. Fix (logic_edits, same position): a 10 cm³ against a 100 cm³ measuring cylinder for 8.0 cm³. Links: marks closer together; so read to a smaller fraction of a cm³; so a smaller uncertainty. One forced order. New herrings. |
| Rung 4 Gas volumes 48, 50, 49, 61, 50 cm³, 6 marks | ok (61 left out; mean 197 ÷ 4 = 49.25, about 49; range 2; 49 ± 1 cm³) |
| CFIFA example 1: 0.025 dm³, 26 cm³, 24 cm³ | ok (25 cm³) |
| CFIFA example 2: mean 18.6 °C, range 0.6 °C | ok (18.6 ± 0.3 °C) |
| CFIFA Q1: 2.42, 2.46, 2.44 g | ok (2.44 g) |
| CFIFA Q2: mean 23.45 cm³, range 0.30 cm³ | ok (± 0.15). "A set of titres" changed to "A set of volume readings"; its id ('cm-q2') is explicit, so it survives. |
| Steps-attempt: 21.5, 21.3, 23.9, 21.4 °C | ok (23.9 out; 21.4 ± 0.1 °C) |
| Steps-worked: 24.10, 24.30, 24.20 | ok (24.20 ± 0.10 cm³). Not placed: its heading "Three titres" is template text. The record's reveal carries the same working. |
| Quiz Q1 Three titres 22.40, 22.60, 22.50 | ok for the answer (22.50 ± 0.10 cm³). Fault: "titres" on every route. Fix: "Three readings of a volume are ...". NEW ID. Options unchanged. |
| Quiz Q2 15.2, 15.4, 18.9, 15.3 g | ok |
| Quiz Q3 Precise | ok |
| Quiz Q4 Why repeat and take a mean | Fault: credited option visibly the longest (70 against 22 to 36). Fix: "It reduces random error". KEY CHANGE. |
| Quiz Q5 Exactly 25.0 cm³ | Fault: the answer (pipette) and one distractor (burette) are chemistry-only apparatus on Combined. Fix, stem kept: "A 25 cm³ measuring cylinder" / "A 250 cm³ measuring cylinder" / "A 250 cm³ beaker" / "A 100 cm³ measuring cylinder". KEY CHANGE. |

**Removed or moved.**
- Removed: the apparatus pick (now Reading a measuring cylinder, Quiz Q5 and Dive deeper); the four word cards and the "precise but not accurate" pick (now the Four words reveal and the Random and systematic error card); the equations panel (now the range-about-the-mean points); percentage uncertainty and its triangle (not on the spec); the Think again on the whole range (now an Easy mistake); the Sort (now the reveal); the Key note; the video; the command words (now Dive deeper).
- Kept: `legacy-fig:nlFig`, three readings 24.10, 24.30, 24.20 on a number line, the range bracket (0.20), the mean marked, "mean 24.20 ± 0.10 cm³". Static; checked against its drawer. Its alt text said "titres"; fixed by logic_edit.
- Kept, Triple only, Dive deeper: `legacy-fig:apFig`: burette (scale running down, ± 0.05 cm³ a reading), pipette (one fixed volume), measuring cylinder (scale running up), and a meniscus read from the bottom at eye level. Checked against its drawer: the meniscus curves down in the middle and the arrow points at its bottom.
- Key changes: Quiz Q4 (credited option), Quiz Q5 (all four options).
- New id (stem changed): Quiz Q1.
- Rung prompts reworded, position kept (id kept): chemical-measurements r2 calc 1 ("titres" to "volumes"), r3 chain 2 (rewritten).

**Builder seam for the lead.** The spec eyebrow is the template literal "AQA Chemistry 5.3.1.4 · Combined and Triple": Triple routes show the 8464 number (8462 is 4.3.1.4).

**Words.** Old Design page prose about 621 (old generator theory 364). New knowledge + key fact + Dive deeper about 524.

**Fixes after the examiner and blind checks (13 Nov).** EX = EXAMINER.md item; BLIND = blind pass. Where this list and the tables above disagree, this list is current.
- BLIND: rung 3 chain 1 (chemical-measurements r3.0), link 1 now starts "So it is anomalous: ...", so link 0 must come first. Prompt unchanged: id kept.
