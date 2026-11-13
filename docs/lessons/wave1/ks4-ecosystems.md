# ecosystems

Sources: AQA spec 4.7.1.1 Communities, read from spec-8464.txt (Combined Trilogy, CF CH) and spec-8461.txt (Biology, TF TH). The two are word for word the same here, with no HT-only or Biology-only lines. Rainford KS4 Biology Unit 7 lesson "Ecosystems, biodiversity, biotic and abiotic factors" (outcomes: use the terms ecosystem, community, competition, habitat, interdependence; explain how one species depends on others; describe a stable community and give an example). LEGACY page (batch 10): the ladder and the practice set are the Design page's own, kept verbatim except the logic_edits listed below.

| Spec statement | Where it is covered | Route | Ticked |
|---|---|---|---|
| Describe different levels of organisation in an ecosystem from individual organisms to the whole ecosystem | Reveal: Levels of organisation; Rung 1 Q1, Q2; Quiz Q1 | CF CH TF TH | ✓ |
| Describe the importance of interdependence and competition in a community | Card: Interdependence (legacy-fig:wFig); Reveal: Take one species out; Card: Competition; Key fact; Rung 2, Rung 3, Rung 4; Quiz Q2, Q5 | CF CH TF TH | ✓ |
| Suggest the factors for which organisms are competing in a given habitat | Card: Competition; Quiz Q4 (taught in full in Population and competition) | CF CH TF TH | ✓ |
| Suggest how organisms are adapted to the conditions in which they live | Taught in Adaptations (4.7.1.4), the lesson that carries it | CF CH TF TH | ✓ (other lesson) |
| An ecosystem is the interaction of a community of living organisms (biotic) with the non-living (abiotic) parts of their environment | Card: Ecosystem and habitat; Reveal; Key fact; Easy mistakes; Rung 1 Q2; Quiz Q1 | CF CH TF TH | ✓ |
| To survive and reproduce, organisms require a supply of materials from their surroundings and from the other living organisms there | Card: Ecosystem and habitat | CF CH TF TH | ✓ |
| Plants compete for light and space, and for water and mineral ions from the soil. Animals compete for food, mates and territory | Card: Competition | CF CH TF TH | ✓ |
| Each species depends on other species for food, shelter, pollination, seed dispersal etc. If one species is removed it can affect the whole community. This is called interdependence | Card: Interdependence; Reveal: Take one species out; Key fact; Easy mistakes; Start here; Rung 2 Q1 | CF CH TF TH | ✓ |
| A stable community is one where all the species and environmental factors are in balance so that population sizes remain fairly constant | Card: A stable community; Easy mistakes | CF CH TF TH | ✓ |
| MS 2c, 4a: extract and interpret information from charts, graphs and tables relating to the interaction of organisms within a community | Card: Explain a change from data; Rung 2 Q2; Rung 4; Quiz Q5 | CF CH TF TH | ✓ |
| (SOW) habitat; give an example of a stable community | Card: Ecosystem and habitat; Card: A stable community (tropical rainforests, ancient oak woodlands) | CF CH TF TH | ✓ |

**Gaps and mismatches.** The legacy page never said "to survive and reproduce, organisms require a supply of materials" and gave no example of a stable community; both are now in cards. No rung or quiz item is untaught. Quiz Q3 (farmland has lower biodiversity) is not a 4.7.1.1 statement; it is taught in the Dive deeper card "Farmland" (it belongs to 4.7.3.1 / 4.7.3.6). Its stem is kept so its ID survives; flagged for the lead to keep or retire.

**Practice set source.** The practice set is the legacy page's own `BANK` in the logic (`BANK.map((q) => K.item(q))`), the same five on every route. It does not read the subtopic `quiz` list, so every fix is a `logic_edits` pair in the record. There is no quiz-ecosystems.json. Q5's stem now states that dragonfly larvae eat tadpoles (new id, see below); the other four stems are unchanged, so their ids survive.

**Audit of the ladder and practice set.**

| Item | Verdict |
|---|---|
| Rung 1 Q1 Define population | Fault: credited option visibly longest (+26). Fix: distractors lengthened ("All the organisms of every species living in one area"; "An area with all its living and non-living parts"), same replies. |
| Rung 1 Q2 Ecosystem includes | Fault: credited option visibly longest (+31). Fix: "The plants that live in the area"; "The fungi and bacteria living in it" (reply now "These are living, so they are in the community."). |
| Rung 2 Q1 Bees die out | Fault: credited option visibly longest (+20). Fix: "The flowers had no bees to feed on, so they starved" (reply "Plants make their own food. They do not feed on bees."). |
| Rung 2 Q2 Foxes, rabbits, grass | ok |
| Rung 3 chain 1 Wolves removed | ok. One forced order (each link causes the next). |
| Rung 3 chain 2 Earthworms disappear | ok. One forced order. |
| Rung 4 Wolves data, 4 marks | ok |
| Quiz Q1 Community vs ecosystem | Fault: credited option visibly longest, dash tails, capitals. Fix: four new same-length options and plain feedback; stem kept. |
| Quiz Q2 Wolves removed | Fault: "Other predators increase in number to compensate" was arguable (its own feedback said it may happen); credited option a four-dash chain. Fix: options "Deer numbers rise and more plants are eaten" / "Every species in the wood dies out" / "Deer numbers fall and plants grow more" / "Nothing in the wood changes", new feedback; stem kept. |
| Quiz Q3 Farmland biodiversity | ok for accuracy (see Gaps: taught in Dive deeper). |
| Quiz Q4 Rock pool, crabs and fish | ok |
| Quiz Q5 Dragonfly larvae data | Fault: credited option visibly longest (+40). Fix: "More tadpoles survived and ate more pondweed"; stem kept. |

**Removed or moved.**
- Removed: the levels stepper (lvFig) and its gate questions; the inline checks "What does an ecosystem include…", "Which describes a stable community?", "Why did the ground-nesting birds fall?"; the Think again choice (community or ecosystem); the Sort (population / community / ecosystem / habitat); the Command words grid; the Key note; the video. Their teaching is now the reveal table, the cards and Easy mistakes.
- Kept: the woodland food web figure (`legacy-fig:wFig`, drawn at its first state, "Remove nothing"). Checked against its drawer: arrows leaf litter to earthworms to shrews, grass and shrubs to deer, flowering plants to deer, deer to wolves, flowering plants to bees, and a dashed green arrow from bees to flowering plants labelled "pollinates". Correct. Its "remove one" states are now the reveal table "Take one species out of the wood".
- The made-up wolves, deer, shrubs and birds data are no longer taught, because Rung 4 uses exactly that data. The data card uses a new example (sea otters, urchins, kelp).
- Moved to Dive deeper: artificial ecosystems / farmland (not 4.7.1.1).
- Builder note for the lead: see the report (RAIL regex).
- Key changes (13 Nov fixes): these options were reworded with no `{stored}` text, so their answers get new keys, which the knowledge-point top-up re-places. Rung 1 Q2 (ecosystems#r1-2): credited option; Rung 2 Q2 (ecosystems#r2-2): credited option and one distractor.
- New id (stem changed): Practice Q5, dragonfly larvae (ecosystems#quiz-CF-5, all routes): stem now opens "Information: dragonfly larvae eat tadpoles.".
- Rung prompts reworded, position kept (id kept): Rung 4 (ecosystems#r4-1): prompt says the birds nest under the shrubs.

**Fixes after the examiner and blind checks (13 Nov).** One line per finding (EX = examiner item number in EXAMINER.md, BLIND = blind/notes.md). Where this list and an audit row above disagree, this list is current.

- EX1 MUST r1.1 (ecosystems#r1-2): credited option trimmed to "The non-living (abiotic) parts". KEY CHANGE.
- EX2 MUST r2.1 (ecosystems#r2-2): credited option "More rabbits survived and ate more grass"; arguable fertilise distractor replaced by "Fewer rabbits ate the grass, so it fell". KEY CHANGE.
- EX3 MUST r4.0 (ecosystems#r4-1): prompt now says the birds nest under the shrubs (id kept, position kept).
- EX4 SHOULD practice Q3 (ecosystems#quiz-CF-3): explanations rewritten plainly; stem and options unchanged (id and keys kept).
- EX5 NOTE stable community card: "An undisturbed tropical rainforest and an ancient oak woodland are examples of stable communities."
- BLIND MED ecosystems#quiz-CF-5: stem now opens "Information: dragonfly larvae eat tadpoles." NEW ID.
- EX6/EX7 NOTE wFig, r1.0/Q1/Q2 lengths: no change (within tolerance; builder renders wFig state 0).
