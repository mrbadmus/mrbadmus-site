# electronic-structure

Sources: AQA 8464 5.1.1.7 (CF, CH) and 8462 4.1.1.7 (TF, TH), word for word the same, no HT-only or "(chemistry only)" lines. Skills: WS 1.2; MS 5b (2D representations of 3D objects). No required practical. Reading group and period from the structure is 5.1.2.1 / 4.1.2.1 (The periodic table); the Design page and its ladder use it, so it stays as one card.

Old page: Design batch-11 (`ks4-chemistry-5.1.1.7-electronic-structure.dc.html`), family Model, routes CF CH TF TH. **Practice set = the page's own `BANK` (five items, the same on every route); ladder = the page's own `rungs`.** Fixes are `logic_edits`; the subtopic `quiz` list is not read by this page.

| Spec statement | Where it is covered (lean record) | Route | Ticked |
|---|---|---|---|
| The electrons in an atom occupy the lowest available energy levels (innermost available shells) | Start here; card 'Filling the shells'; Key fact; Easy mistakes; Rung 1 item 1; practice Q5 | CF CH TF TH | ✓ |
| The electronic structure of an atom can be represented by numbers or by a diagram, e.g. sodium 2,8,1: two electrons in the lowest energy level, eight in the second and one in the third | Card 'Numbers and diagrams' (fig:sodium-shells); Key fact; Rung 1 item 2 | CF CH TF TH | ✓ |
| Represent the electronic structures of the first twenty elements of the periodic table in both forms | Card 'Numbers and diagrams' (fig:shell-examples: Li, O, Cl); reveal 'Write the electronic structure' (C, Mg, P, Ar, K, Ca); Rung 2 item 1; Rung 4; practice Q3 | CF CH TF TH | ✓ |
| Students may answer questions in terms of either energy levels or shells | Card 'Filling the shells' | CF CH TF TH | ✓ |
| (5.1.2.1, used by the ladder) Same group, same number of outer electrons; period from the number of shells | Card 'Group and period'; Rung 2 item 2; Rung 3; practice Q1, Q2, Q4 | CF CH TF TH | ✓ |

**Misconceptions taught against (Easy mistakes).** Potassium is 2,8,9; the outer shell fills first; 2,8,6 is in Group 3 because it has three shells.

**Gaps and mismatches.** None in the content line.

**Practice set source.** The page's own `BANK`, five items, identical on all four routes.

**Audit of the ladder and practice set (faults found and fixed).**
- Practice Q1 (2.8.6, which group): the credited option carried its reason with a dash; replies in capitals; one distractor ("Period 3 — it has 3 shells") was not a group. Options now four groups (6, 2, 16, 3); stem and key kept.
- Practice Q2 (lithium and sodium): credited option the longest (100 against 30 to 49). Now "Both have 1 electron in their outer shell"; stem kept.
- Practice Q3 (calcium): credited "2,8,8,2" was the longest by one character. "2,18" became "8,8,2,2" (writing the outer shell first), the same length; key unchanged.
- Practice Q4 (helium in Group 0): credited option the longest (53 against 13 to 24). Now "Its one shell is full with 2 electrons"; stem kept.
- Practice Q5 (how shells fill): credited option the longest (63 against 27 to 45). Now "The lowest energy level fills first" (the spec's words); stem kept.
- Rungs: checked on every route, no fault. Aluminium 13 = 2 + 8 + 3; 2,8,8,2 is 20 electrons, Group 2, period 4; magnesium 12 = 2,8,2, Group 2, period 3. Each chain has one valid order.

**Calculations (recomputed).** Every structure from the fill rule 2, 8, 8, 2 (`figlib.ks4lean_atoms.electrons_of`, asserted): Li 3 = 2,1; C 6 = 2,4; O 8 = 2,6; Na 11 = 2,8,1; Mg 12 = 2,8,2; Al 13 = 2,8,3; P 15 = 2,8,5; S 16 = 2,8,6; Cl 17 = 2,8,7; Ar 18 = 2,8,8; K 19 = 2,8,8,1; Ca 20 = 2,8,8,2.

**Unsure (left out until checked).** None.

**Removed or moved.**
- Design benches (the element picker with its structure pick, the group/period picks), the Think again panel and the sort: off the page. Activity state keys no longer on the page: `el`, `eq<symbol>` (eqLi, eqC, eqO, eqNa, eqMg, eqCl, eqAr, eqK, eqCa), `g1`, `g2`, `think`, `sort`.
- The Design's period-table figure (`ptFig`): The periodic table lesson carries the table; this page keeps one written example (sulfur).
- Commas or dots; command words: Dive deeper.

**Examiner fix round (26 Nov 2026).**
- M4: practice Q1 (2.8.6, which group) distractor 'Group 16' is now 'Group 8', with the reply '8 is the number of electrons in the second shell. The group comes from the 6 outer electrons.' Stem, id and key unchanged.
