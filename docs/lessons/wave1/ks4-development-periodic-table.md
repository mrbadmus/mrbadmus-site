# development-periodic-table

Sources: AQA 8464 5.1.2.2 (CF, CH) and 8462 4.1.2.2 (TF, TH), word for word the same, no HT-only or "(chemistry only)" lines. Skills: WS 1.1, 1.6 (explain how testing a prediction can support or refute a new scientific idea). No required practical.

Old page: Design batch-4 (`ks4-chemistry-5.1.2.2-development-periodic-table.dc.html`), family Process, routes CF CH TF TH. **Practice set = the page's own `bankSrc` (five items, every route); rungs authored in the logic.** Every fix is a logic edit in the lean record.

| Spec statement | Where it is covered (lean record) | Route | Ticked |
|---|---|---|---|
| Before the discovery of protons, neutrons and electrons, scientists attempted to classify the elements by arranging them in order of their atomic weights | Card 'Early tables: atomic weight'; reveal; Key fact; Easy mistakes; Rung 1 Q1 | CF CH TF TH | ✓ |
| The early periodic tables were incomplete and some elements were placed in inappropriate groups if the strict order of atomic weights was followed | Card 'Early tables: atomic weight'; reveal; practice Q3 (new) | CF CH TF TH | ✓ |
| Mendeleev overcame some of the problems by leaving gaps for elements that he thought had not been discovered | Card "Mendeleev's gaps" (fig:mendeleev-gap); Start here; Easy mistakes; Rung 1 Q2; practice Q2 | CF CH TF TH | ✓ |
| ... and in some places changed the order based on atomic weights | Card "Mendeleev's swaps" (fig:te-i-swap); reveal; Rung 2 Q1 | CF CH TF TH | ✓ |
| Elements with properties predicted by Mendeleev were discovered and filled the gaps | Card "Mendeleev's gaps"; card 'Why his table was accepted'; Rung 3 chain 1; practice Q1 | CF CH TF TH | ✓ |
| Knowledge of isotopes made it possible to explain why the order based on atomic weights was not always correct | Card 'Isotopes explain the swaps'; Key fact; Rung 2 Q2; Rung 3 chain 2; practice Q4, Q5 | CF CH TF TH | ✓ |
| Describe these steps in the development of the periodic table | Cards in order; reveal; Rung 4 | CF CH TF TH | ✓ |

**Misconceptions taught against (Easy mistakes).** Mendeleev used atomic number; the gaps were mistakes; isotopes have different numbers of protons.

**Gaps and mismatches.** None. "Why his table was accepted" is the WS 1.6 opportunity (a tested prediction supports the idea).

**Practice set source.** The page's own `bankSrc`, five items, identical on all four routes.

**Audit of the ladder and practice set (faults found and fixed).**
- Practice Q1 (why accepted): credited 106 characters with an em dash, against 61. Now 'Elements he predicted were found and matched his predictions' (60). Feedback plain; the Newlands and Ramsay asides go.
- Practice Q2 (why the gaps): credited the longest (51 against 42). Now 'For elements not yet discovered' (31); 'ran out of space' written 'ran out of space on the page'.
- Practice Q3 "Why was Newlands' table rejected?": Newlands is not in 5.1.2.2. **Replaced** by "Why did early periodic tables put some elements in the wrong groups?" (the spec's own line; credited 'They followed the strict order of atomic weights', 48, not the longest). New id `ks4q:development-periodic-table:1e1881d4cf`; old id `ks4q:development-periodic-table:a395029012` retires.
- Practice Q4 (tellurium heavier than iodine): credited 95 against 38. Now 'Much of it is made of heavier isotopes' (38); two distractors written longer.
- Rung 1 Q2: credited 'For elements not yet discovered' the longest (31 against 24); distractors written out longer.
- Rung 2 Q1: credited 58 against 36. Now 'To keep each in a group of similar elements' (43); distractors longer.
- Rung 3 chain 2 (isotopes and tellurium): the conclusion link could also be read first. Links 2 and 3 now refer back ('this average', 'So, although ...'): one valid order. Same order credited.
- Rung 4 mark points: the Newlands point replaced by 'Mendeleev also used atomic weights, but put elements with similar properties in the same group.' Levels unchanged.
- Numbers checked: Te 52 protons, A<sub>r</sub> 127.6; I 53, 126.9 (127.60, 126.90). Ar 18, 39.9; K 19, 39.1 (39.95, 39.10). Rung 2 Q2 key Argon (18 < 19).
- Blind key pass (all items, all routes): all keys agree.

**Old subtopic data.** spec "5.1.2.2" ✓.

**Unsure (left out until checked).** Dive deeper's eka-silicon numbers: Mendeleev's predicted relative atomic mass about 72 and density about 5.5 g/cm³; germanium (found 1886) 72.6 and 5.3 g/cm³ (5.32). Beyond the spec; Dive deeper only.

**Removed or moved.**
- Design bench 'Make Mendeleev's moves' (four-step swap/gap/test/explain stepper), the Think again panel, the Who did what sort, the video and the step-list summary: off the page; their teaching is in the cards, two new figures and Easy mistakes.
- Newlands' octaves (beyond the spec): Dive deeper. Argon and potassium: Dive deeper. Command words: Dive deeper.

**Words (approximate).** Design about 931 → lean 468 (−50%), plus 138 in Dive deeper. The Design count includes the stepper's step text, which is teaching only while the bench is on the page.
