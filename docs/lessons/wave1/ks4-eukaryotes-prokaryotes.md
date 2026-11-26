# eukaryotes-prokaryotes

Sources: AQA 8464 4.1.1.1 (CF, CH) and 8461 4.1.1.1 (TF, TH), word for word the same, no HT-only or "(biology only)" lines. Skills: MS 1b (standard form), 2a, 2h (order of magnitude); WS 4.4 (prefixes centi, milli, micro and nano). No required practical. Magnification is 4.1.1.5 (Microscopy); the page keeps the CFIFA it already had, because working out a real size from an image is how the scale of cells is examined.

Old page: Design batch-2 (`eukaryotes-prokaryotes.dc.html`), family Contrast, routes CF CH TF TH. **Practice set = the route's subtopic `quiz` list via `K.bank(slug, R.route)`; Rung 1 = `K.find(slug, route, 'key structural difference')`.** So their fixes are quiz-data edits in `all_subtopics_biology*.py` (all four routes carry the same five items), and the needle survives in exactly one stem per route.

| Spec statement | Where it is covered (lean record) | Route | Ticked |
|---|---|---|---|
| Plant and animal cells (eukaryotic cells) have a cell membrane, cytoplasm and genetic material enclosed in a nucleus | Card 'Eukaryotic cells'; reveal 'Animal cell and bacterium compared'; Key fact; Rung 1; practice Q1 | CF CH TF TH | ✓ |
| Bacterial cells (prokaryotic cells) are much smaller in comparison. They have cytoplasm and a cell membrane surrounded by a cell wall | Card 'Prokaryotic cells' (fig:prokaryote-cell); reveal; practice Q2 | CF CH TF TH | ✓ |
| The genetic material is not enclosed in a nucleus. It is a single DNA loop and there may be one or more small rings of DNA called plasmids | Card 'Prokaryotic cells'; reveal; Easy mistakes; Rung 4; practice Q3, Q5 | CF CH TF TH | ✓ |
| Demonstrate an understanding of the scale and size of cells and be able to make order of magnitude calculations, including the use of standard form | Cards 'Size and orders of magnitude' (fig:cell-bacterium-scale), 'Standard form', 'Working out sizes from an image' (CFIFA); Rung 2; Rung 3 | CF CH TF TH | ✓ |
| Use prefixes centi, milli, micro and nano | Card 'Units for very small things'; Easy mistakes; practice Q4 | CF CH TF TH | ✓ |

**Misconceptions taught against (Easy mistakes).** Bacteria have a small nucleus; a bacterium has a cellulose cell wall; 1 mm = 100 µm.

**Gaps and mismatches.** None in the content lines. The Higher routes' CFIFA questions use standard form and the Foundation ones do not: standard form is on every route in this spec point, and every route still meets it in card 'Standard form' and in the worked examples.

**Practice set source.** Subtopic quiz list, five items, identical on all four routes.

**Audit of the ladder and practice set (faults found and fixed).**
- Quiz Q1 (the K.find needle): "membrane-bound" (beyond the spec), replies in capitals with dashes. Options reworded to the spec's words, stem kept.
- Quiz Q2 (2 µm bacterium): credited option the longest, with a dash. Options now the same length; stem kept.
- Quiz Q3, Q4: replies in capitals with dashes and "Remember:". Rewritten plainly; stems and options kept.
- Quiz Q5 "What is a flagellum in a bacterial cell?": flagella are not in 4.1.1.1 (and "nucleoid", "capsule" in its replies). **Replaced** by "What is a plasmid?" (new id; old id retires).
- Worked example 1 was built from the subtopic `fifas`, with the Fine-tune line "Both values already in mm — no conversion needed". Written out by a logic edit, same numbers (30 ÷ 0.003 = 10 000 = 1 × 10⁴).
- Rungs: checked, no fault. Rung 2 Higher: 18 ÷ 6000 = 0.003 mm = 3 µm. Rung 2 Foundation: 24 ÷ 400 = 0.06 mm = 60 µm. Rung 3: 0.1 mm = 100 µm; 100 ÷ 1 = 100 = 10², one order only (each link needs the one before).

**Old subtopic data.** spec "4.1.1.1" ✓. `common_mistake` says the bacterial wall is "peptidoglycan": true, but beyond the spec; the lean page says only that it is not cellulose.

**Unsure (left out until checked).** Bacteria having ribosomes but no mitochondria is in the comparison table (standard, and needed for the Rung 4 compare); neither is a 4.1.1.1 statement.

**Removed or moved.**
- Design benches (build the two cells, how many fit across), both Think again panels, the "Equation · Learn it" box: off the page. Their teaching is in the cards and Easy mistakes.
- "Fungi and protists are eukaryotic too": Dive deeper.
- Command words: Dive deeper.

**Examiner fix round (26 Nov 2026).**
- Standard form card: '×(1 × 10⁴)'. Units card: 'nano (n) means a billionth (a thousand-millionth)'. ep-q1 close: '60 µm is a sensible size for a plant cell, which is usually 10–100 µm long'.
