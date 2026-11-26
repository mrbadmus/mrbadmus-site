# stem-cells

Sources: AQA 8464 4.1.2.3 (CF, CH) and 8461 4.1.2.3 (TF, TH), word for word the same, no HT-only or "(biology only)" lines. Skills: WS 1.3 evaluate the practical risks and benefits, and the social and ethical issues, of stem cells in medical research and treatment. "Knowledge and understanding of stem cell techniques are not required." No required practical.

Old page: Design batch-6 (`ks4-biology-4.1.2.3-stem-cells.dc.html`), family Classify, routes CF CH TF TH. Practice set = hard-coded `bankSrc` (5 items, same on every route).

| Spec statement | Where it is covered (lean record) | Route | Ticked |
|---|---|---|---|
| A stem cell is an undifferentiated cell ... capable of giving rise to many more cells of the same type, and from which certain other cells can arise from differentiation | Card 'What a stem cell is'; Key fact; Easy mistakes; Rung 1 | CF CH TF TH | ✓ |
| Describe the function of stem cells in embryos, in adult animals and in the meristems in plants | Card 'What stem cells do'; reveal 'Three sources of stem cells' | CF CH TF TH | ✓ |
| Stem cells from human embryos can be cloned and made to differentiate into most different types of human cells | Reveal; card 'Treating disease'; Rung 2; Rung 4 | CF CH TF TH | ✓ |
| Stem cells from adult bone marrow can form many types of cells including blood cells | Reveal; Easy mistakes; practice Q1 (new); Rung 2 | CF CH TF TH | ✓ |
| Meristem tissue in plants can differentiate into any type of plant cell, throughout the life of the plant | Reveal; Key fact; practice Q3; Rung 1 | CF CH TF TH | ✓ |
| Treatment with stem cells may be able to help conditions such as diabetes and paralysis | Card 'Treating disease'; reveal 'Weighing up'; Rung 4 | CF CH TF TH | ✓ |
| In therapeutic cloning an embryo is produced with the same genes as the patient. Stem cells from the embryo are not rejected | Card 'Treating disease'; Easy mistakes; Rung 3; practice Q4 | CF CH TF TH | ✓ |
| Potential risks such as transfer of viral infection; some people have ethical or religious objections | Reveal 'Weighing up stem cell treatment'; practice Q2, Q5; Rung 4 | CF CH TF TH | ✓ |
| Stem cells from meristems can produce clones of plants quickly and economically: rare species; crop plants with special features | Card 'Cloning plants'; Rung 2; Rung 3 | CF CH TF TH | ✓ |
| Techniques not required | Dive deeper 'What you do not need' | CF CH TF TH | ✓ |

**Misconceptions taught against (Easy mistakes).** Therapeutic cloning makes a baby; adult bone marrow stem cells become any cell; stem cells are already specialised.

**Gaps and mismatches.** The Design page said bone marrow stem cells form "a limited range"; the spec says "many types of cells including blood cells". The lean page and Rung 2 now say "many types, including blood cells, but fewer than embryonic stem cells".

**Practice set source.** Hard-coded `bankSrc`, five items, same on all routes.

**Audit of the ladder and practice set (faults found and fixed).**
- Q1 "How are stem cells used to treat leukaemia?": leukaemia is not in 4.1.2.3; credited option +50 characters. **Replaced** by "What can stem cells from adult bone marrow form?" (new id; old id in `REPLACED`, `tools/lean_id_map.py`).
- Q2 (ethics): credited the longest (+55), dash; replies in capitals. Options and replies rewritten.
- Rung 2 (i) compare: credited the longest (+23) and "a limited range". Credited option now "Embryonic form more types of cell than bone marrow"; distractors lengthened. Same answer.
- Rung 2 (ii) orchid: credited the longest (+27). Distractors lengthened.
- Rung 3 (both chains) checked: one order each.

**Old subtopic data.** spec "4.1.2.3" ✓. The CH/TH `higher` block ("enucleated egg", "totipotent") is beyond the spec and not Higher content; never rendered.

**Unsure (left out until checked).** "What stem cells do" says adult stem cells replace cells such as blood cells: the spec's "function in adult animals", in the usual words.

**Removed or moved.**
- Design benches (what can it become, weigh it up, Think again, sort): off the page; the three sources are a reveal table.
- Bone marrow transplants and leukaemia: Dive deeper. "Embryos about 5 days old": dropped. Command words: Dive deeper.

**Examiner fix round (26 Nov 2026).**
- Practice Q3 reply 2: 'many types of human cell, including blood cells, but not plant cells'. Practice Q4 distractor lengthened: 'The stem cells have no genes in them at all'.
- Rung 2 (i) options: 'Embryonic stem cells form more types than bone marrow ones' (key), 'Both kinds form exactly the same range of cells', 'Bone marrow stem cells form more types than embryonic ones', 'Embryonic stem cells form only blood cells'. The key ties for longest with a distractor.
- Card: 'In adult animals, stem cells repair and replace cells'.
