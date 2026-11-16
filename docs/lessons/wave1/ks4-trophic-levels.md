# trophic-levels (LEGACY, batch 10)

Sources: AQA 8461 4.7.4.1 "Trophic levels" (in 4.7.4, "biology only"), read from the spec PDF. 8464 has no trophic levels section; the page exists only on TF and TH, so no route gating is needed. Nothing in 4.7.4.1 is HT only. Rainford SOW lesson "Trophic levels in an ecosystem, transfer of biomass" (identify the trophic levels on food chains). The 10% card is 8461 4.7.4.3, also Triple, on both routes.

| Spec statement | Where it is covered | Route | Ticked |
|---|---|---|---|
| Describe the differences between the trophic levels of organisms within an ecosystem | Reveal: The four levels; Card: One animal, two levels; Key fact; Rung 2; Rung 4 | TF TH | ✓ |
| Trophic levels can be represented by numbers, starting at level 1 with plants and algae; further levels are numbered according to how far the organism is along the food chain | Card: Numbering the levels (legacy-fig:lvFig); Start here; Rung 1 Q1; Practice 3 | TF TH | ✓ |
| Level 1 producers; level 2 herbivores, primary consumers; level 3 carnivores that eat herbivores, secondary consumers; level 4 carnivores that eat other carnivores, tertiary consumers | Reveal: The four levels; Key fact; Rung 2 Q1; Rung 4 | TF TH | ✓ |
| Apex predators are carnivores with no predators | Card: Apex predators; Key fact; Rung 1 Q2; Practice 5 | TF TH | ✓ |
| Decomposers break down dead plant and animal matter by secreting enzymes into the environment; small soluble food molecules then diffuse into the microorganism | Card: Decomposers (fig:decomposer-feeding); Easy mistakes; Rung 3 Q1; Rung 4; Practice 4 | TF TH | ✓ |
| (4.7.4.3) Only approximately 10% of the biomass from each trophic level is transferred to the level above it | Card: Why food chains are short; Rung 3 Q2; Practice 2 | TF TH | ✓ |

**Practice set source.** The practice set is the `BANK` array written in the legacy logic (five items, the same on TF and TH). It does not read the subtopic `quiz` list, so every fix is a `logic_edits` pair and there is no quiz-trophic-levels.json. Items 1 and 2 of BANK are the old subtopic quiz questions.

**Audit of every legacy rung and practice item.**

| Item | Verdict | Fix |
|---|---|---|
| Rung 1 Q1 (level 1 organisms) | ok | none |
| Rung 1 Q2 (apex predator) | ok | none |
| Rung 2 Q1 (blue tit level) | ok | none |
| Rung 2 Q2 (fox, rabbits and blackberries) | Credited option visibly the longest (47 against 17 and 18 characters) | logic_edits: two same-shape distractors ("Level 2 with rabbits, level 3 with blackberries"; "Level 3 in both, because a fox is a carnivore") with new replies. Position and prompt unchanged |
| Rung 3 Q1 (chain: decomposer feeding) | ok, one forced order | none |
| Rung 3 Q2 (chain: why chains are short) | ok, one forced order | none |
| Rung 4 (describe levels and decomposers) | ok | none |
| Practice 1 (arrows, grass → rabbit → fox) | Credited option 108 characters against at most 85, every option has a dash tail, and it calls grass "prey" | logic_edits: question text kept (ID kept); options now "From food to eater: the way biomass is transferred" ✓ and three same-length distractors; feedback rewritten |
| Practice 2 (why 4 or 5 levels) | Credited option 141 characters with a dash tail; says "energy" where the spec says biomass | logic_edits: question text kept; options rewritten around "Only about 10% of the biomass passes to each next level" |
| Practice 3 (stickleback level) | ok | none |
| Practice 4 (how decomposers digest) | Credited option 105 characters against at most 36 | logic_edits: question text kept; "They secrete enzymes onto it, then small soluble molecules diffuse in" ✓ and three longer distractors |
| Practice 5 (apex predator) | ok | none |
| Figure lvFig | Correct (arrows from food to eater, levels 1 to 4), but the red "apex predator" label sat between the blue tit and the sparrowhawk | logic_edits: label centred under the sparrowhawk (x 535 → 600). Checked by rendering it |
| Figure dFig | Not used: it is a stepper figure (state 0 shows only a leaf and a bacterium) and its final state is cluttered, with labels floating away from what they name | fig:decomposer-feeding requested instead |

**Gaps and mismatches.** None in the legacy page's spec coverage. The legacy teaching of the arrows said "the direction in which energy and biomass are transferred"; the record keeps that idea as "from the organism that is eaten to the organism that eats it".

**Removed or moved.** Removed with the legacy body: the hook, the six-organism level picker, the apex-predator pick, the decomposer stepper, the "Think again" and the sort. Their teaching is carried by the cards: numbering (lvFig), the reveal table, Apex predators, One animal, two levels (the fox), Decomposers, Easy mistakes. The Command words box moved to Dive deeper.
- Key changes (13 Nov fixes): these options were reworded with no `{stored}` text, so their answers get new keys, which the knowledge-point top-up re-places. Practice Q1 arrows (quiz-TF-1, TF TH): three distractors; Practice Q4 decomposers (quiz-TF-4, TF TH): credited option.
- New id (stem changed): None.

**Fixes after the examiner and blind checks (13 Nov).** One line per finding (EX = examiner item number in EXAMINER.md, BLIND = blind/notes.md). Where this list and an audit row above disagree, this list is current.

- EX1 MUST practice Q4 (trophic-levels#quiz-TF-4): credited option now "They secrete enzymes; small soluble molecules diffuse in" (edit #5 new text). KEY CHANGE.
- EX2 SHOULD practice Q1 (quiz-TF-1): distractors now "From eater to food: what each animal has eaten", "Both ways: biomass flows in both directions at once", "No direction: they only join the names together" (edit #3 new text). KEY CHANGE (distractors).
- EX3 NOTE lvFig, EX4 NOTE decomposer-feeding: no change.
