# periodic-table

Sources: AQA 8464 5.1.2.1 (CF, CH) and 8462 4.1.2.1 (TF, TH), word for word the same, no HT-only or "(chemistry only)" lines. Skills: WS 1.2. No required practical.

Old page: Design batch-4 (`ks4-chemistry-5.1.2.1-periodic-table.dc.html`), family Classify, routes CF CH TF TH. **Practice set = the page's own `bankSrc` (five items, the same on every route); Rung 1 is authored in the logic (no `K.find`).** So every fix is a logic edit in the lean record; no subtopic-data edit.

| Spec statement | Where it is covered (lean record) | Route | Ticked |
|---|---|---|---|
| The elements in the periodic table are arranged in order of atomic (proton) number | Card 'In order of atomic number' (fig:pt-first-twenty); Key fact; Rung 1 Q1; practice Q3 | CF CH TF TH | ✓ |
| ... and so that elements with similar properties are in columns, known as groups | Card 'In order of atomic number'; Start here | CF CH TF TH | ✓ |
| The table is called a periodic table because similar properties occur at regular intervals | Card 'In order of atomic number' | CF CH TF TH | ✓ |
| Elements in the same group have the same number of electrons in their outer shell (outer electrons) and this gives them similar chemical properties | Card 'Groups and outer electrons'; Key fact; practice Q2 | CF CH TF TH | ✓ |
| Explain how the position of an element is related to the arrangement of electrons in its atoms and hence to its atomic number | Card 'Position from the electrons' (fig:na-cl-shells, phosphorus 2,8,5 example); Easy mistakes; Rung 1 Q2; Rung 2 Q1; Rung 4; practice Q1, Q4 | CF CH TF TH | ✓ |
| Predict possible reactions and probable reactivity of elements from their positions in the periodic table | Reveal 'Predicting reactivity from position'; card 'Why the two trends go opposite ways'; Easy mistakes; Rung 2 Q2; Rung 3 (both chains); practice Q5 | CF CH TF TH | ✓ |

**Misconceptions taught against (Easy mistakes).** The group number is the number of shells; Group 0 atoms have no outer electrons; every group gets more reactive going down.

**Gaps and mismatches.** None. The Design page's "metals left, non-metals right" line is 5.1.2.3; it is a one-line Dive deeper pointer here.

**Practice set source.** The page's own `bankSrc`, five items, identical on all four routes.

**Audit of the ladder and practice set (faults found and fixed).**
- Practice Q1 (Period 3, Group 2): every option carried its reasoning after an em dash, and the credited one was the longest (59 against 53). Options now the bare structures 2,8,2 / 3,2 / 2,2 / 2,8,3; feedback rewritten to teach the reasoning. Stem kept.
- Practice Q2 (why Group 7 elements react alike): credited option 117 characters against 53. Now 'They all have 7 electrons in their outer shell' (46). Feedback plain (no capitals, no dashes).
- Practice Q4 (noble gases unreactive): credited 48 against 38. Now 'Their atoms have a full outer shell' (35); distractor 'no outer electrons' reworded to 'no electrons in an outer shell' (same misconception).
- Practice Q5 (potassium below sodium): credited 106 against 63. Now 'More reactive: its outer electron is lost more easily' (52); the longest is now the 'holds its electron tighter' distractor.
- Rungs: checked, no fault. Rung 2 Q1: 2.8.5 → 3 shells, Period 3; 5 outer, Group 5 (phosphorus, 2 + 8 + 5 = 15). Rung 3 chains: each link needs the one before; one order.
- Blind key pass (every rung item and the five practice items, all four routes): all keys agree.

**Old subtopic data.** spec "5.1.2.1" ✓.

**Unsure (left out until checked).** None in the content. Hydrogen is drawn on its own above the middle of the short table (as on the AQA data sheet), not at the top of Group 1.

**Removed or moved.**
- Design bench 'Build an atom · find its square' (the − / + atom stepper and live table), the Think again panel (down a group), the Group or period sort, the video and the "Equation/keyLines" summary: off the page. Their teaching is in the cards, the figures and Easy mistakes.
- "Metals on the left, non-metals on the right" and the transition-metal pointer (TF/TH only): Dive deeper.
- Command words: Dive deeper.

**Words (approximate; teaching text, Design count from template text plus logic strings outside the ladder and bank).** Design about 607 → lean 422 (−30%), plus 86 in Dive deeper.

**Examiner fix round (26 Nov 2026).**
- M5 (new logic edit): Rung 2 item 1 (2.8.5) distractor 'Period 3, Group 15' is now 'Period 3, Group 2', reply '2 is the number of electrons in the first shell. The group is the outer count: 5.' Key unchanged.
- S6 and S8: Dive deeper 'Where the metals are' now reads 'Metals are to the left and towards the bottom of the table. Non-metals are towards the right and top.'; 'They have their own lesson.' removed from 'The transition metals'.
