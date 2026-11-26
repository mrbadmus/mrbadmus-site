# microscopy

Sources: AQA 8464 4.1.1.5 (CF, CH) and 8461 4.1.1.5 (TF, TH), word for word the same, no HT-only or "(biology only)" lines: the calculations and standard form are on every route. "Limited to the differences in magnification and resolution." Skills: WS 1.1; MS 1a, 1b, 2h, 3b; WS 4.4 prefixes. **Required practical 1** (8464 RP 1 = 8461 RP 1) sits under 4.1.1.2 in the spec; its method is taught here.

Old page: Design batch-3 (`microscopy.dc.html`), family Quantitative, routes CF CH TF TH. The header binds its spec per route ("AQA {{ specName }} ({{ specCode }}) 4.1.1.5"); lean_ks4 now reads that form as the literal. **Practice set = the route's subtopic `quiz` list via `K.bank`; Rung 1 = `K.find(slug, route, 'difference between magnification and resolution')`.** Fixes are quiz-data edits, all four routes the same.

| Spec statement | Where it is covered (lean record) | Route | Ticked |
|---|---|---|---|
| Understand how microscopy techniques have developed over time | Card 'How electron microscopes changed biology'; Start here | CF CH TF TH | ✓ |
| Explain how electron microscopy has increased understanding of sub-cellular structures | Same card; reveal 'Light and electron microscopes'; Key fact; Rung 3; practice Q3 | CF CH TF TH | ✓ |
| An electron microscope has much higher magnification and resolving power than a light microscope ... study cells in much finer detail | Card 'Magnification and resolution'; reveal; Rung 1; practice Q1, Q4 | CF CH TF TH | ✓ |
| Carry out calculations involving magnification, real size and image size using magnification = size of image ÷ size of real object | Card 'The magnification equation' (triangle:EQ_MAG); card 'Calculating with magnification' (CFIFA); Easy mistakes; Rung 2; practice Q2, Q5 | CF CH TF TH | ✓ |
| Use prefixes centi, milli, micro and nano | Card 'The magnification equation' (1 mm = 1000 µm, 1 µm = 1000 nm); Rung 2 Higher (nm) | CF CH TF TH | ✓ |
| Express answers in standard form if appropriate | Card 'Calculating with magnification'; worked example 5 | CF CH TF TH | ✓ |
| RP 1 (from 4.1.1.2): observe, draw and label cells, magnification scale | Card 'Required practical 1: observing cells' (slideFig, method); Rung 4 | CF CH TF TH | ✓ |

**Misconceptions taught against (Easy mistakes).** Resolution is how big the image is; dividing mm by µm without converting (12 ÷ 40 = ×0.3; it is 12 000 ÷ 40 = ×300); magnification has a unit.

**Gaps and mismatches.** The spec limits the comparison to magnification and resolution, so "the specimen must be dead / in a vacuum" is not taught (it was on the old page). The magnification and resolution figures (×2000, ×2 000 000, 200 nm, 0.1 nm) are not spec numbers; they are the usual ones and quiz Q1 asks the first.

**Practice set source.** Subtopic quiz list, five items, identical on all four routes. Every stem kept.

**Audit of the ladder and practice set (faults found and fixed).**
- Q1, Q2, Q5: replies in capitals with dashes. Rewritten; stems and options kept.
- Q3 (why ribosomes were not seen): credited the longest, with "~20 nm" and "~200 nm"; the "living cells" distractor's reply was beyond the spec. Options rewritten to equal length.
- Q4 (the K.find needle, magnification vs resolution): credited the longest, with "=" shorthand. Options rewritten to equal length.
- Worked example 1 was built from the subtopic `fifas` (Fine-tune "Both values are in mm — no unit conversion needed"). Written out, same numbers (54 ÷ 0.018 = 3000).
- Rungs checked, no fault: Rung 2 Higher 0.6 mm = 600 000 nm, 600 000 ÷ 30 000 = 20 nm; Foundation 32 mm = 32 000 µm, 32 000 ÷ 40 = ×800. Rung 3 is one order (resolution → distinguish closer points → structures seen).

**Old subtopic data.** spec "4.1.1.5" ✓. The CH/TH `higher` block (SEM/TEM, "light microscopes are limited by the wavelength of light") is beyond the spec; the page never rendered it.

**Unsure (left out until checked).** "First electron microscopes in the 1930s": history, not a spec statement; kept as one clause.

**Removed or moved.**
- Design benches (resolve it, run the practical with the field-of-view count and mean, check the drawing), Think again panels: off the page.
- Total magnification (eyepiece × objective), the practical's risks, command words: Dive deeper.

**Examiner fix round (26 Nov 2026).**
- Header chip: 'Required practical 1 · observing cells' (RP 1 on all four routes), through a new lean_ks4 `template_edits` list.
- Rung 3 herring 'An electron microscope can be used to study living cells' (outside the spec's limit) is now 'A light microscope has a higher resolution than an electron microscope'. It contradicts link 1, so the chain keeps one order.
- Rung 1 why, in the spec's words.
