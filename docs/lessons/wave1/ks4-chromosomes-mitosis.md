# chromosomes-mitosis

Sources: AQA 8464 4.1.2.1 Chromosomes and 4.1.2.2 Mitosis and the cell cycle (CF, CH) and 8461 4.1.2.1–4.1.2.2 (TF, TH), word for word the same, no HT-only or "(biology only)" lines. Skills: WS 1.2 use models and analogies to explain how cells divide. "Students need to understand the three overall stages of the cell cycle but do not need to know the different phases of the mitosis stage." No required practical.

Old page: Design batch-2 (`chromosomes-mitosis.dc.html`), family Process, routes CF CH TF TH. **Practice set = the route's subtopic `quiz` list via `K.bank`; Rung 1 = `K.find(slug, route, 'How many chromosomes will each daughter cell have')`.** Fixes are quiz-data edits, all four routes the same.

| Spec statement | Where it is covered (lean record) | Route | Ticked |
|---|---|---|---|
| The nucleus of a cell contains chromosomes made of DNA molecules. Each chromosome carries a large number of genes | Card 'Chromosomes and genes' | CF CH TF TH | ✓ |
| In body cells the chromosomes are normally found in pairs | Card 'Chromosomes and genes'; practice Q3 (new) | CF CH TF TH | ✓ |
| Cells divide in a series of stages called the cell cycle; describe the stages, including mitosis | Card 'The cell cycle' (fig:cell-cycle-stages); reveal 'The three stages'; Key fact; Rung 4 | CF CH TF TH | ✓ |
| During the cell cycle the genetic material is doubled and then divided into two identical cells | Card 'The cell cycle'; Rung 2; Rung 3; practice Q1, Q2 | CF CH TF TH | ✓ |
| Before a cell can divide it needs to grow and increase the number of sub-cellular structures such as ribosomes and mitochondria. The DNA replicates to form two copies of each chromosome | Reveal 'The three stages' (Stage 1); Easy mistakes; practice Q2 | CF CH TF TH | ✓ |
| In mitosis one set of chromosomes is pulled to each end of the cell and the nucleus divides | Reveal (Stage 2); figure; Rung 3 | CF CH TF TH | ✓ |
| Finally the cytoplasm and cell membranes divide to form two identical cells | Reveal (Stage 3); figure | CF CH TF TH | ✓ |
| Three overall stages only, not the phases of mitosis | Dive deeper 'What you do not need' | CF CH TF TH | ✓ |
| Cell division by mitosis is important in the growth and development of multicellular organisms | Card 'Why mitosis matters'; Key fact; Rung 4; practice Q4 | CF CH TF TH | ✓ |
| Recognise and describe situations in given contexts where mitosis is occurring | Card 'Why mitosis matters' (growth, repair, replacement); practice Q5 (new) | CF CH TF TH | ✓ |

**Misconceptions taught against (Easy mistakes).** DNA copied after the cell divides (was: 92 chromosomes after replication, removed 26 Nov); mitosis makes four cells with half the chromosomes (meiosis); mitosis is the whole cell cycle.

**Gaps and mismatches.** Cancer (benign/malignant, uncontrolled division) was taught and quizzed here; it is 8464/8461 4.2.2.7 (Organisation, its own lean lesson). Now one Dive deeper line with a pointer.

**Practice set source.** Subtopic quiz list, five items, identical on all four routes.

**Audit of the ladder and practice set (faults found and fixed).**
- Q1 (the needle, 46): reply used "chromatids" and capitals. Rewritten; stem and options kept.
- Q2 (DNA before mitosis): credited the longest, with a dash. Options rewritten.
- Q3 "What is the difference between a benign and a malignant tumour?": 4.2.2.7 content. **Replaced** by "How are chromosomes normally found in body cells?" (new id).
- Q4 (purpose of mitosis): credited the longest, with a dash. Options rewritten.
- Q5 "Cancer is caused by...": 4.2.2.7 content, "ATP" and "regulatory genes" in it. **Replaced** by "In which of these is mitosis happening?" (new id).
- Rung 2 (b): the credited option was the longest; one distractor lengthened (logic edit).
- Rung 3 checked: one order (DNA replicates → one copy of each chromosome to each end → each new cell has a full set).

**Old subtopic data.** spec "4.1.2.1" (the lesson is 4.1.2.1–4.1.2.2). The CH/TH `higher` block ("diploid", cancer) is not Higher content in this spec; the page never rendered it. `key_note` mentions cancer; not rendered on the lean page.

**Unsure (left out until checked).** "46 chromosomes, in 23 pairs" and "sperm and egg cells have one of each pair" go a little past 4.1.2.1 (the numbers are 4.6.1.2 context); kept as the usual worked numbers.

**Removed or moved.**
- Design benches (run the cell cycle with the DNA-mass graph, build the sequence, mitosis or meiosis sort), the cancer section and its Think again: off the page. The three stages are drawn (`figlib/ks4lean_cell.py`).
- Cancer: Dive deeper. Command words: Dive deeper.

**Examiner fix round (26 Nov 2026).**
- The chromatid count (46 'each made of two copies', the 92 trap) is beyond the spec and is gone: Easy mistake 1 is now 'The DNA is copied after the cell divides' / 'The DNA replicates before the cell divides, so each new cell gets a full set of chromosomes'.
- Rung 2 part (c) now asks how many chromosomes each new cell has at S (the flat stretch after the drop at R: one new cell, before its DNA replicates again from S to T). Options '92, double the full set' / '23, half the full set' / '46, the full set'; key '46, the full set'. Model line 3 and the 'wrong' line follow.
- Practice Q1 reply for '92' (quiz data): '92 would be double the full set. Mitosis gives each new cell the full set: 46.'
