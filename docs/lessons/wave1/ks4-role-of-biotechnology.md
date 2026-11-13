# role-of-biotechnology

Sources: AQA 8461 4.7.5.4 Role of biotechnology (biology only), and the linked 4.6.2.4 Genetic engineering (concerns about GM crops; HT-only steps), read from `~/Desktop/Rainford/Curriculum/AQA/AQA-8461-SP-2016.pdf` (also checked against the SCRATCH `spec-8461.txt`, which holds this section). Rainford SOW, Biology Unit 7, "Role of Biotechnologies". Routes: TF, TH only. No HT-only lines in 4.7.5.4; the 4.6.2.4 HT steps sit in a TH-only Dive deeper card. No required practical.

Kind: LEGACY (batch 10). Ladder and practice set stay from the live page. The practice set is the hard-coded `BANK` in the legacy logic, so its fixes are `logic_edits`, not a quiz JSON.

| Spec statement | Where it is covered | Route | Ticked |
|---|---|---|---|
| Describe and explain some possible biotechnical and agricultural solutions, including genetic modification, to the demands of the growing human population | Card: Feeding a growing population; Cards: Mycoprotein, Human insulin, GM crops | TF TH | ✓ |
| Modern biotechnology techniques enable large quantities of microorganisms to be cultured for food | Card: Feeding a growing population | TF TH | ✓ |
| The fungus Fusarium is useful for producing mycoprotein, a protein-rich food suitable for vegetarians. Grown on glucose syrup, in aerobic conditions; the biomass is harvested and purified | Card: Mycoprotein (fig:mycoprotein-fermenter); Key fact | TF TH | ✓ |
| A genetically modified bacterium produces human insulin. When harvested and purified this is used to treat people with diabetes | Card: Human insulin (fig:insulin-gm-bacteria); Key fact | TF TH | ✓ |
| GM crops could provide more food or food with an improved nutritional value such as golden rice | Card: GM crops; Key fact | TF TH | ✓ |
| (4.6.2.4, linked) Concerns about GM crops: wild flowers and insects; health effects not fully explored; some people have objections | Card: Concerns about GM crops; Card: Evaluating a GM crop | TF TH | ✓ |
| (4.6.2.4, HT only) the main steps of genetic engineering: enzymes, vector (plasmid or virus) | Dive deeper: How the gene is moved | TH | ✓ |

SOW rows: "Describe how the fungus Fusarium can be grown to produce mycoprotein" ✓; "Describe what Golden rice is and how it was produced" ✓; "Make informed judgements about … genetic engineering" ✓ (Evaluating a GM crop); "Describe how microorganisms can be grown in large vats" ✓; "Explain how the conditions in the vat are monitored and controlled" is beyond 8461 4.7.5.4, so it sits in Dive deeper (Inside the fermenter). "Evaluate the use of mycoprotein as a food" is not covered beyond "protein-rich, suitable for vegetarians" (see report: left out, not certain of AQA-safe claims).

## Audit of the kept ladder and practice set

| Item | Verdict | Fix |
|---|---|---|
| Rung 1 Q1 (Name the fungus) | ok | |
| Rung 1 Q2 (State what it is grown on) | ok | |
| Rung 2 Q1 (Describe insulin production) | Credited option 71 against 32 and 39 | logic_edits: credited "A GM bacterium makes it; it is harvested and purified"; distractors lengthened |
| Rung 2 Q2 (Explain how mycoprotein could help) | Credited option 111 against 21 and 26 | logic_edits: credited "Large amounts of protein-rich food are made in fermenters"; distractors lengthened |
| Rung 3 Q1 (chain: mycoprotein) | ok; one forced order (grow on syrup → aerobic growth → harvest and purify) | |
| Rung 3 Q2 (chain: insulin) | ok; one forced order | |
| Rung 4 (6-mark evaluate, golden rice) | ok; "selective breeding cannot" insert genes from another organism is right | |
| Practice 1 "What is the source of mycoprotein (Quorn)?" | Dash tails; credited option the longest; feedback named *Fusarium venenatum*, which the lesson never teaches | Stem kept (id kept). logic_edits: options "The fungus Fusarium" / "Soya beans, a plant" / "Algae grown in ponds" / "Yeast used to make bread", new explanations |
| Practice 2 "Why are some environmentalists concerned about herbicide-resistant GM crops?" | Credited option 146 characters with dash tails; "absorb more herbicide… more toxic" is arguable (residues are a real question) | Stem kept. logic_edits: credited "The gene could spread to wild plants, making hard-to-kill weeds"; distractors "The crops cannot be eaten by people or by animals", "The crops grow so fast that they take over wild habitats", "The crops give a smaller yield than ordinary crops" |
| Practice 3 "Describe how mycoprotein is produced." | Credited option 95 against 31 to 40 | Stem kept. logic_edits: credited "Fusarium grows aerobically on glucose syrup; it is harvested and purified"; distractors lengthened |
| Practice 4 "How is the insulin used to treat diabetes produced today?" | Credited option 85 against 28 to 40 | Stem kept. logic_edits: credited "A GM bacterium makes it, then it is harvested and purified"; distractors lengthened |
| Practice 5 "What is the intended benefit of golden rice?" | Credited option 73 against 16 to 21 | Stem kept. logic_edits: credited "Improved nutritional value"; distractors lengthened |

Chains: both have one forced order; no `orders` needed.

**Gaps and mismatches.** The old generator page left out human insulin almost entirely (one line). It added traditional biotechnology, micropropagation, Bt crops, drought-tolerant crops, patents and seed companies, allergenicity and antibiotic-resistance markers. None of these is in 8461 4.7.5.4 or 4.6.2.4; they are not carried over. The live page's two figures (mFig, iFig) are not kept: each is drawn from a step-through stepper, so outside its section each would show only its first step. Two static drawings are asked for instead (see the report).

**Removed or moved.** Removed from the live page: the hook (replaced by Start here), video, the two steppers and their figures (their steps are now the points in the Mycoprotein and Human insulin cards), the insulin pick, the GM evaluation pick (its shape is the Evaluating a GM crop card), the Ks4Choice "Quorn is made from soya" (now an Easy mistakes line), the Ks4Sort, the Key note, and the Command words block (moved to Dive deeper). The mycoprotein-versus-cattle line moved to Dive deeper.
- Key changes (13 Nov fixes): these options were reworded with no `{stored}` text, so their answers get new keys, which the knowledge-point top-up re-places. Rung 1 Q2 (role-of-biotechnology#r1-2): two distractors; Rung 2 Q2 (role-of-biotechnology#r2-2): two distractors; Practice Q2 GM concern (quiz-TF-2, TF TH): credited option and two distractors; Practice Q3 mycoprotein (quiz-TF-3, TF TH): three distractors.
- New id (stem changed): None.

**Fixes after the examiner and blind checks (13 Nov).** One line per finding (EX = examiner item number in EXAMINER.md, BLIND = blind/notes.md). Where this list and an audit row above disagree, this list is current.

- EX1 MUST r1.1 (role-of-biotechnology#r1-2): distractors now "Waste meat", "Garden soil" (reply "It grows in a fermenter, not in soil."). KEY CHANGE (distractors).
- EX2 MUST r2.1 (role-of-biotechnology#r2-2): distractors now "It means that no crops will ever need to be grown again", "It is made cheaply from the waste meat left over on farms" (edits #5–#6). KEY CHANGE (distractors).
- EX3 MUST practice Q3 (quiz-TF-3): distractors now "Soya beans are crushed, heated and pressed into shaped meat-free pieces", "Fusarium is grown on meat without any oxygen, then it is dried and cut up", "Bacteria are grown in a fermenter on meat, then harvested and purified" (edits #22–#24). KEY CHANGE (distractors).
- BLIND MED quiz-TF-2: key now AQA's concern wording "They could affect populations of wild flowers and insects" (was gene flow to make hard-to-kill weeds); "The crops grow so fast that they take over wild habitats" (close to that concern) replaced by "The crops give people extra vitamin A in their daily diet"; "…by any animals"; replies rewritten. Stem kept (id kept). KEY CHANGE.
- EX4 NOTE r4.0 point 5: "a large benefit against uncertain risks" ("certain" removed).
- EX5 NOTE Q2 length: resolved by the TF-2 rewrite (57 against 53).
