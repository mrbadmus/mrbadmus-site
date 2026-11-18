# principles-of-organisation

Sources: AQA 8464 4.2.1 (CF, CH) and 8461 4.2.1 (TF, TH), read from spec-8464-4.2.txt (Version 1.1, 4 Oct 2019) and spec-8461-4.2.txt (Version 1.0). Word for word the same; no HT-only or "(biology only)" lines, so every item serves every route. Skills: MS 1c, size and scale of cells, tissues, organs and systems. Rainford SOW Unit 2 "Cells Tissues and organs" (explain cell, tissue, organ, organ system, organism with examples; size and scale; the main human body systems and their functions; key words organism, organ system, tissue). No required practical. No AQA equation.

Old page: Design batch-6 lesson (`ks4-biology-4.2.1-principles-of-organisation.dc.html`), family Quantitative, routes CF CH TF TH, practice set = the page's own hard-coded `bankSrc` (4 items), not the subtopic quiz list.

| Spec statement | Where it is covered (lean record) | Route | Ticked |
|---|---|---|---|
| Cells are the basic building blocks of all living organisms | Card 'Cells, tissues and organs'; reveal 'The five levels'; Key fact | CF CH TF TH | ✓ |
| A tissue is a group of cells with a similar structure and function | Card 'Cells, tissues and organs'; reveal; Easy mistakes; Rung 3 chain 1; practice Q2 | CF CH TF TH | ✓ |
| Organs are aggregations of tissues performing specific functions | Card 'Cells, tissues and organs' (AQA's words, then the plain gloss); card 'The stomach is an organ'; Rung 1 Q1 | CF CH TF TH | ✓ |
| Organs are organised into organ systems, which work together to form organisms | Card 'Cells, tissues and organs'; reveal; Rung 1 Q2; Rung 3 chain 2; practice Q4 | CF CH TF TH | ✓ |
| MS 1c: size and scale of cells, tissues, organs and systems | Card 'Size and scale' (ladderFig, conversions, CFIFA); Rung 2; practice Q5 | CF CH TF TH | ✓ |
| (SOW) the main systems in the human body and their functions | Left out (SOW only); the digestive system is the worked example | — | left out |

**Gaps and mismatches.**
- Spec wording: the page says "groups of tissues performing a specific function"; AQA says "aggregations of tissues performing specific functions". Keep AQA's words in the definition card; the plain gloss may follow.
- The SOW asks for the main human body systems and their functions; the spec does not list them. One example system (digestive) is enough for 4.2.1.
- "This is a comparison by division, not an AQA equation, so it has no triangle" is platform self-explanation on a pupil page.

**Practice set source.** The page's own `bankSrc` (`bankSrc.map((q) => K.item(q))`), the same four on every route. Fixes are `logic_edits`. No quiz JSON needed.

**Audit of the ladder and practice set (faults found).**
- Quiz "What is a tissue?": credited option visibly longest (+28); replies use capitals ("ORGAN SYSTEM", "GROUP") and dash tails.
- Quiz "Which of these is an example of an organ system?": credited option visibly longest (+21), every option carries a dash tail.
- Quiz "Put the levels in order": dash-tailed replies; fine otherwise (one right order).
- Rung 1 Q1 "Define an organ.": credited option visibly longest (+25).
- Think again "is muscle an organ?" and the Rung 4 reject "Muscle is an organ.": a whole muscle (for example the biceps) is an organ in biology (muscle tissue, connective tissue, nerves, blood vessels). The page's own prompt defines muscle as "a group of muscle cells", i.e. muscle tissue. As worded, the misconception is arguably true. Reword throughout to "muscle tissue", or drop it; do not mark "Muscle is an organ" as wrong.
- Stomach sort "Covers the outside of the stomach → epithelial": AQA's own teaching material says epithelial tissue covers the inside and outside of the stomach; ok.
- CFIFA and Rung 2 numbers recomputed: 50 000 ÷ 50 = 1000 ✓; 150 ÷ 12 = 12.5 ✓; 4000 ÷ 40 = 100 ✓; 200 ÷ 25 = 8 ✓; 5000 ÷ 25 = 200 ✓; 100 ÷ 2 = 50 ✓.

**Old subtopic data (all four routes).** spec "4.2.1" ✓; 4 quiz items (not read by the page). No HT content.

**Unsure (left out until checked).**
- Typical sizes ("cell about 50 µm; tissue layer about 1 mm; organ a few cm; human about 1.5 m"): not spec; reasonable orders of magnitude. Keep as "about".

**Removed or moved.**
- Design benches (classify the examples, stomach tissue sort), Think again: off the page. Their teaching is in the cards.
- "Muscle is an organ" (Think again and Rung 4 reject): arguably true (a whole muscle is an organ); the reject is replaced by "A tissue is made of several organs".
- "This is a comparison by division, not an AQA equation, so it has no triangle": platform self-explanation, gone.
- SOW 'main human body systems': left out (not in 4.2.1).
- Practice set: options and replies tidied (capitals, dash tails, credited option no longer the longest). Stems kept, so ids kept.
- Examiner/blind (18 Nov): Rung 1 (ii) options 'Tissue layer' / 'Single cell' (credited 'Organ system' was double length); practice Q2 and Q4 wrong options lengthened (credited no longer visibly longest).
- Rung 3 (i) chain rewritten so it has ONE order: tissues in the stomach → they work together to digest food → several tissues make an organ, so the stomach is an organ. Prompt unchanged.
- Practice Q5 '0.1 times' reply corrected (that is 2 ÷ 20 unconverted). Ladder figure organ size 'about 10 cm'; Rung 4 point 'a muscle cell, tens of µm across'.
