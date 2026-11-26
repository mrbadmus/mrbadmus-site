# cell-specialisation

Sources: AQA 8464 4.1.1.3 Cell specialisation and 4.1.1.4 Cell differentiation (CF, CH) and 8461 4.1.1.3–4.1.1.4 (TF, TH), word for word the same, no HT-only or "(biology only)" lines. No required practical, no equation.

Old page: Design batch-6 (`ks4-biology-4.1.1.3-cell-specialisation.dc.html`), family Classify, routes CF CH TF TH. Practice set = hard-coded `bankSrc` (5 items, same on every route).

| Spec statement | Where it is covered (lean record) | Route | Ticked |
|---|---|---|---|
| When provided with appropriate information, explain how the structure of different types of cell relate to their function in a tissue, an organ or organ system, or the whole organism | Cards for each cell; card 'A cell you have not met'; Rung 2; Rung 4; practice Q2 (red blood cell) | CF CH TF TH | ✓ |
| Cells may be specialised: sperm cells, nerve cells and muscle cells in animals | Cards 'Sperm cells' (fig:sperm-cell), 'Nerve cells' (fig:nerve-cell), 'Muscle cells'; Rung 4; practice Q1 | CF CH TF TH | ✓ |
| Root hair cells, xylem and phloem cells in plants | Card 'Root hair cells' (fig:root-hair-cell); reveal 'Xylem and phloem cells'; Rung 1; Rung 3; practice Q3, Q4 | CF CH TF TH | ✓ |
| Explain the importance of cell differentiation | Card 'Differentiation' (last line); Key fact | CF CH TF TH | ✓ |
| As an organism develops, cells differentiate. Most animal cells differentiate at an early stage; many plant cells retain the ability throughout life | Card 'Differentiation'; Key fact; Rung 1 | CF CH TF TH | ✓ |
| In mature animals, cell division is mainly restricted to repair and replacement. As a cell differentiates it acquires different sub-cellular structures ... It has become a specialised cell | Card 'Differentiation'; practice Q5 | CF CH TF TH | ✓ |

**Misconceptions taught against (Easy mistakes).** Root hair cells take in water by active transport; mitochondria make energy; xylem cells are living.

**Gaps and mismatches.** The spec names the six cells but not their features; the features taught are the standard textbook ones (tail, mitochondria, enzymes, half the chromosomes; long axon, branched endings; contracting protein fibres; root hair, mitochondria; lignin, no end walls; pores in the end walls). Phloem wording follows 8461 4.2.3.1 ("elongated cells with pores in the end walls to allow cell sap to move from one phloem cell to the next").

**Practice set source.** Hard-coded `bankSrc`, five items, same on all routes. Every stem kept.

**Audit of the ladder and practice set (faults found and fixed).**
- Q1 (sperm mitochondria): credited the longest (+30), "ATP", "flagellum", "acrosome" (not in the spec). Options and replies rewritten.
- Q2 (red blood cell, no nucleus): credited the longest (+16). Options rewritten.
- Q3 (root hair, no chloroplasts) and Q4 (xylem): credited the longest, with dashes. Options rewritten.
- Rung 2 (i) small-intestine folds: credited the longest (+28). Rung 2 (ii) muscle mitochondria: credited the longest (+19). Distractors lengthened; replies kept.
- Rung 3 (i) root hair chain: the surface-area link could go first or last. Now the energy reasoning, one order: ions more concentrated inside → so active transport, which needs energy → mitochondria release that energy.
- Rung 3 (ii) xylem chain: the lignin link could go anywhere. Now: dead, no end walls → so they join into hollow tubes → water flows up these tubes, strengthened by lignin.

**Old subtopic data.** spec "4.1.1.3" (the lesson is 4.1.1.3–4.1.1.4; the eyebrow uses `BIO_EYEBROW`).

**Unsure (left out until checked).** "A nucleus with half the number of chromosomes" for sperm is meiosis content (4.6.1.2); it is the standard sperm adaptation, so kept.

**Removed or moved.**
- Design benches (design the cell, compare with the real cell), Think again, sort: off the page. Three cells drawn (`figlib/ks4lean_cell.py`); muscle, xylem and phloem are taught in words and a table.
- The synapse pointer: Dive deeper. Command words: Dive deeper.

**Examiner fix round (26 Nov 2026).**
- Practice Q3 credited option: 'Roots get no light, so the cell cannot photosynthesise' (was 'so it'). Animal-plant's similar item reads 'Roots get no light, so they cannot photosynthesise': 'they' is the roots, so it is left.
