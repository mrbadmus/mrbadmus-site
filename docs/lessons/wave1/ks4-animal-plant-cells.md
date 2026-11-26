# animal-plant-cells

Sources: AQA 8464 4.1.1.2 (CF, CH) and 8461 4.1.1.2 (TF, TH), word for word the same, no HT-only or "(biology only)" lines. **Required practical 1 in both specs** (8464 RP 1, 8461 RP 1): "use a light microscope to observe, draw and label a selection of plant and animal cells. A magnification scale must be included." (AT 1 and 7). Skills: WS 1.2 recognise, draw and interpret images of cells; MS 1d, 3a estimations; AT 7.

Old page: Design batch-6 (`ks4-biology-4.1.1.2-animal-plant-cells.dc.html`), family Quantitative, routes CF CH TF TH. Practice set = hard-coded `bankSrc` (5 items, same on every route), so its fixes are `logic_edits`.

| Spec statement | Where it is covered (lean record) | Route | Ticked |
|---|---|---|---|
| Explain how the main sub-cellular structures, including the nucleus, cell membranes, mitochondria, chloroplasts in plant cells and plasmids in bacterial cells are related to their functions | Reveal 'What each part does'; card 'Plasmids in bacteria'; Rung 1; Rung 3; practice Q1, Q3, Q5 | CF CH TF TH | ✓ |
| Most animal cells have a nucleus, cytoplasm, a cell membrane, mitochondria, ribosomes | Card 'Parts of animal and plant cells' (fig:animal-plant-cells); reveal 'Animal cell or plant cell'; Key fact; Rung 4 | CF CH TF TH | ✓ |
| In addition, plant cells often have chloroplasts and a permanent vacuole filled with cell sap | Same; Easy mistakes (root cells); practice Q2, Q4 | CF CH TF TH | ✓ |
| Plant and algal cells also have a cell wall made of cellulose, which strengthens the cell | Card 'Parts of animal and plant cells'; reveal; Start here; Rung 1 | CF CH TF TH | ✓ |
| Use estimations and explain when they should be used to judge the relative size or area of sub-cellular structures | Card 'Estimating sizes' | CF CH TF TH | ✓ |
| RP 1: observe, draw and label plant and animal cells, with a magnification scale | Card 'Required practical 1: looking at cells' (what can be seen, stains); full method on Microscopy; card 'Magnification' (triangle, CFIFA); Rung 2 | CF CH TF TH | ✓ |

**Misconceptions taught against (Easy mistakes).** Every plant cell has chloroplasts; plant cells have a wall instead of a membrane; plant cells have no mitochondria.

**Gaps and mismatches.** None. The RP 1 method is written once, on Microscopy (the Design pages had it on both).

**Practice set source.** Hard-coded `bankSrc`, five items, same on all routes. Every stem kept.

**Audit of the ladder and practice set (faults found and fixed).**
- Q1 (protein synthesis) and Q4 (in both cells): replies in capitals with dashes. Rewritten; options kept.
- Q2 (root cell, no chloroplasts): credited option the longest (+33) with a dash. Options rewritten to equal length.
- Q3 (vacuole): credited the longest (+40), "turgor pressure" (not in the spec). Options rewritten.
- Q5 (muscle mitochondria): credited the longest, "ATP" (not in the spec). Options rewritten.
- Rung 3 (ii) muscle chain: links 1 and 2 could go in either order. Each link now names the one before.
- Rung 2: 16 mm = 16 000 µm, 16 000 ÷ 8 = ×2000; 10 mm = 10 000 µm, 10 000 ÷ 250 = 40 µm. Worked examples: 20 000 ÷ 50 = ×400; 15 000 ÷ 100 = 150 µm. Your turn: 30 000 ÷ 60 = ×500; 4000 ÷ 400 = 10 µm. All correct.

**Old subtopic data.** spec "4.1.1.2" ✓.

**Unsure (left out until checked).** Rung 3 (i) "why a plant cell does not burst" leans on osmosis (4.1.3.2); the spec line here is only "the cell wall strengthens the cell". Kept, since the wall is the answer.

**Removed or moved.**
- Design side-by-side tap figure (a highlight, unlabelled), vacuole estimate, Think again, sort: off the page. A labelled figure is drawn instead (`figlib/ks4lean_cell.py`).
- Algae: in the card's wall sentence only. Command words: Dive deeper.

**Examiner fix round (26 Nov 2026).**
- Card 'Parts of animal and plant cells' names chloroplasts and the permanent vacuole again (they had become 'often three more').
- Start here setup: 'Your skin is soft and bendy, but a raw carrot snaps cleanly.' (options and reply unchanged; they still fit).
