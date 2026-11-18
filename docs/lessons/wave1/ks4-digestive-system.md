# digestive-system

Sources: AQA 8464 4.2.2.1 (CF, CH) and 8461 4.2.2.1 (TF, TH), word for word the same, no HT-only or "(biology only)" lines. Required practical: **8464 RP 3 / 8461 RP 4** "use qualitative reagents to test for a range of carbohydrates, lipids and proteins. To include: Benedict's test for sugars; iodine test for starch; and Biuret reagent for protein" (AT 2 on 8464; AT 2 and 8 on 8461). Same spec point is shared with the Enzymes lesson (enzyme action, pH and temperature, amylase RP). Rainford SOW Unit 2 "Human digestive system and how it works" (functions; positions of the organs on a diagram; small soluble molecules absorbed; small intestine adaptations; key words chemical/mechanical digestion, villi, microvilli), "Chemistry of Food" / food tests RP (key words lipid, Benedict, Biuret), "Factors affecting enzyme action" (three enzymes with substrates, products and sites), "Bile" (how bile helps fat digestion). No AQA equation.

Old page: Design batch-6 (`ks4-biology-4.2.2.1-digestive-system.dc.html`), family Model, routes CF CH TF TH; RP label routed correctly in the logic (`R.isTriple ? 'Biology required practical 4' : 'Required practical 3'`). Practice set = hard-coded `bankSrc` (5 items).

| Spec statement | Where it is covered (lean record) | Route | Ticked |
|---|---|---|---|
| (assumes KS3 digestive system) The digestive system is an organ system in which several organs work together to digest and absorb food | Card 'The digestive system' (gutFig) | CF CH TF TH | ✓ |
| Recall the sites of production and the action of amylase, proteases and lipases | Reveal 'Three kinds of enzyme'; card 'Where the enzymes are made'; practice Q5 | CF CH TF TH | ✓ |
| Understand simple word equations, no chemical symbol equations | Card 'Word equations' | CF CH TF TH | ✓ |
| Digestive enzymes convert food into small soluble molecules that can be absorbed into the bloodstream | Card 'The digestive system'; Key fact; Rung 3 chain 2 | CF CH TF TH | ✓ |
| Carbohydrases break down carbohydrates to simple sugars. Amylase is a carbohydrase which breaks down starch | Reveal 'Three kinds of enzyme'; card 'Word equations' | CF CH TF TH | ✓ |
| Proteases break down proteins to amino acids | Reveal; card 'Word equations'; Easy mistakes | CF CH TF TH | ✓ |
| Lipases break down lipids (fats) to glycerol and fatty acids | Reveal; card 'Word equations'; Rung 1 Q1 | CF CH TF TH | ✓ |
| The products of digestion are used to build new carbohydrates, lipids and proteins. Some glucose is used in respiration | Card 'Word equations' | CF CH TF TH | ✓ |
| Bile: made in the liver, stored in the gall bladder; alkaline to neutralise hydrochloric acid from the stomach; emulsifies fat to small droplets, increasing surface area; alkaline conditions and large surface area increase the rate of fat breakdown by lipase | Card 'Bile'; Easy mistakes; Rung 1 Q2; Rung 3 chain 1; practice Q1 | CF CH TF TH | ✓ |
| RP 3 / RP 4: food tests (Benedict's, iodine, Biuret; lipids) | Card 'Required practical 3: food tests' (CF CH) / 'Required practical 4: food tests' (TF TH); Rung 2; Rung 4. Lipids: Sudan III (red-stained oily layer on top), with the ethanol emulsion test as a one-line alternative (supervising ruling, 18 Nov) | CF CH TF TH | ✓ |
| Enzyme nature, temperature and pH; lock and key; rate calculations; amylase pH RP | Enzymes lesson; Dive deeper 'How enzymes work' links to it | CF CH TF TH | ✓ (other lesson) |

**Gaps and mismatches.**
- None in the spec lines. The two lessons split 4.2.2.1: this one = organs, enzymes' sites and products, bile, food tests; Enzymes = enzyme action, temperature, pH, the amylase RP.
- The RP lists "lipids" in its title but names only three reagents. Ruled 18 Nov: the page teaches Sudan III (AQA's required practical handbook) as the main lipid test and the ethanol emulsion test as a one-line alternative, because exam questions use either.
- Rainford's "microvilli" and "mechanical digestion": not in 4.2.2.1. Villi are in 4.1.3.1 (exchange surfaces). Leave microvilli out.

**Practice set source.** Hard-coded `bankSrc`, five items, identical on every route. Fixes are `logic_edits`.

**Audit of the ladder and practice set (faults found).**
- Quiz "What is the role of bile in digestion?": credited visibly longest (+37), dash tails, capitals in replies ("LIPASE", "ALKALINE").
- Quiz "Why does the small intestine have villi?": credited visibly longest (+28).
- Quiz "Where are proteins first chemically digested?": credited "The stomach — by the enzyme pepsin in the presence of HCl" (+24, dash tail). Pepsin is not in the spec (it says "proteases"); a reply names "pancreatic proteases".
- Quiz "What does the large intestine absorb?": dash tails; reply mentions "lacteals (lymph vessels in villi)", beyond GCSE.
- Quiz "Which enzyme is produced by the salivary glands?": credited "Amylase — breaks down starch into maltose" (+12, dash tail); the spec says "simple sugars" (maltose is not named); distractor "Pepsin" not spec.
- Rung 1 "Name the products of lipid digestion.": credited visibly longest (+13).
- Gut figure stomach stop: "hydrochloric acid, which gives the acid conditions the stomach protease works best in" — true, fine.

**Old subtopic data.** spec "4.2.2.1" ✓. rp "RP4 — Food tests…" on all four routes: wrong on CF CH (8464 RP 3). CH and TH carry a "higher" block (bile, villi and microvilli): 4.2 has no HT content, so it is mislabelled. The page does not read either field.

**Unsure (left out until checked).**
- Sudan III and the ethanol emulsion test for lipids (the spec names neither; Sudan III is the handbook's method).
- Benedict's colour range "green, yellow or orange means less sugar": standard, not spec wording.
- Sites of amylase production "salivary glands, pancreas, small intestine" and protease "stomach, pancreas, small intestine": AQA's mark schemes accept these; keep.

**Removed or moved.**
- Design benches (follow the meal, food tests bench), Think again: off the page.
- Lipid test: left out in the first draft, restored as ethanol emulsion, then ruled (18 Nov) Sudan III first with ethanol as the alternative.
- Pepsin, maltose, lacteals, microvilli, mechanical digestion: gone from options and replies (not in the spec).
- Old subtopic data: CH/TH 'higher' block (bile, villi, microvilli) is not Higher content; RP number wrong on CF CH. Not rendered; the builder takes the RP numbers from the record.
- Practice set: options and replies rewritten (Q1 to Q5). Stems kept, so ids kept.
- Examiner/blind (18 Nov): **lipid test restored** (the live page's ethanol emulsion test, word for word; reagent then ruled: Sudan III first, see above); Rung 2's 'A cloudy white emulsion' option kept.
- Benedict's list now includes orange; 'They are absorbed in the small intestine' (not 'This happens…'); gut figure label 'small intestine' (no '(coiled)', it ran off the edge).
