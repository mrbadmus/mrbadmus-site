# sustainable-fisheries

Sources: AQA 8461 4.7.5.3 Sustainable fisheries (biology only), read from `~/Desktop/Rainford/Curriculum/AQA/AQA-8461-SP-2016.pdf` (also checked against the SCRATCH `spec-8461.txt`, which holds this section). Rainford SOW, Biology Unit 7, "Food production, farming techniques, sustainable fisheries". Routes: TF, TH only. No HT-only lines. No required practical.

Kind: LEGACY (batch 10). Ladder and practice set stay from the live page. The practice set is the hard-coded `BANK` in the legacy logic, so its fixes are `logic_edits`, not a quiz JSON.

| Spec statement | Where it is covered | Route | Ticked |
|---|---|---|---|
| Fish stocks in the oceans are declining | Card: Declining stocks | TF TH | ✓ |
| It is important to maintain fish stocks at a level where breeding continues or certain species may disappear altogether in some areas | Card: Why it matters; Key fact | TF TH | ✓ |
| Control of net size and the introduction of fishing quotas play important roles in conservation of fish stocks at a sustainable level | Card: Fishing quotas; Card: Net size; Key fact | TF TH | ✓ |
| WS 1.4: understand how application of different fishing techniques promotes recovery of fish stocks | Card: Net size; Card: Using stock data (fig:cod-stock-recovery) | TF TH | ✓ |

SOW rows: "Explain why some fish stocks are declining and why this is a problem" ✓ (Declining stocks, Why it matters); "Describe ways that fish stocks can be conserved" ✓; "Give an example of sustainable food production" ✓ (Dive deeper: Sustainable food).

## Audit of the kept ladder and practice set

| Item | Verdict | Fix |
|---|---|---|
| Rung 1 Q1 (State: sustainable level) | Credited option 53 characters against 13 and 33 | logic_edits: credited "Keeping enough fish so that breeding continues"; distractors lengthened |
| Rung 1 Q2 (Name the two methods) | Prompt said "the spec gives", a reply said "Not the spec’s methods"; "Fish farming" is arguable (it does take pressure off wild stocks) | logic_edits: prompt "Name two methods used to conserve fish stocks at a sustainable level."; distractors "Smaller nets and longer fishing seasons", "Bigger boats and better sonar" |
| Rung 2 Q1 (Explain a quota) | Credited option 54 against 22 and 26 | logic_edits: distractors lengthened |
| Rung 2 Q2 (trend after 2001) | "Use the data" is not a command word; the why line claimed "slowly at first", which two values cannot show; credited option visibly longest | logic_edits: command "Describe"; why "After 2001 the stock rose from 60 000 to 160 000 tonnes."; distractors "It kept falling, to below 60 000 tonnes", "It rose to 160 000 tonnes in 2002" |
| Rung 3 Q1 (chain: mesh size) | ok; one forced order | |
| Rung 3 Q2 (chain: overfishing) | Science ok; a herring reply said "The spec’s mechanism…" | logic_edits: "They are caught faster than they can breed, so too few are left." |
| Rung 4 (6-mark, cod data) | ok; values checked (250 000 → 60 000 by 2000; 70 000, 110 000, 160 000 in 2005, 2010, 2015) | |
| Practice 1 "Why are minimum mesh size rules important…" | Dash tails; credited option the longest; "water flows through more easily, reducing fuel costs" is partly true | Stem kept (id kept). logic_edits: all four options and three explanations |
| Practice 2 "What is a fishing quota?" | Credited option 93 against 13 to 34 | Stem kept. logic_edits: credited "A limit on how many fish may be caught each year"; distractors lengthened |
| Practice 3 (made-up stock data, which conclusion fits) | Credited option 71 against 15 to 31 | Stem kept. logic_edits: credited "Enough fish were left to breed, so the stock rose"; distractors lengthened. 50 000 → 120 000 "more than doubled" ✓ |
| Practice 4 "Why can a fish stock collapse?" | Credited option 76 against 16 to 38; "The sea is too big to fish out" is a claim, not a cause; "Quotas kill fish" is odd | Stem kept. logic_edits: credited "Fish are caught faster than they can breed"; distractors "Larger nets let the young fish escape", "Too few boats fish in the area" |
| Practice 5 "Why does it take years for a collapsed stock to recover…" | Credited option 76 against 24 to 31 | Stem kept. logic_edits: credited "The fish left must grow to breeding age first"; distractors lengthened |

Chains: both have one forced order; no `orders` needed.

**Gaps and mismatches.** None in the spec. The old generator page added exclusion zones, closed seasons, Marine Protected Areas, the Common Fisheries Policy and a whole fish-farming (aquaculture) section. None is in 8461 4.7.5.3; they are not carried over. The live page's stock graph (gFig) is not kept: it is drawn from two toggle buttons and a made-up model, so outside its section it would show one fixed line. A static drawing of the cod data used in Rung 4 is asked for instead (fig:cod-stock-recovery, see the report).

**Removed or moved.** Removed from the live page: the hook (replaced by Start here), video, the quota and mesh toggles with their graph, the "Why does a larger mesh help?" pick, the two data picks (their data is the same as Rung 4 and the new figure), the Ks4Choice "back in a year?" (now an Easy mistakes line), the Ks4Sort, the Key note and the Command words block (moved to Dive deeper).
- Key changes (13 Nov fixes): these options were reworded with no `{stored}` text, so their answers get new keys, which the knowledge-point top-up re-places. Rung 2 Q1 (sustainable-fisheries#r2-1): two distractors; Practice Q1 mesh (quiz-TF-1, TF TH): three distractors; Practice Q3 quota data (quiz-TF-3, TF TH): all four options; Practice Q5 recovery (quiz-TF-5, TF TH): three distractors.
- New id (stem changed): None.

**Fixes after the examiner and blind checks (13 Nov).** One line per finding (EX = examiner item number in EXAMINER.md, BLIND = blind/notes.md). Where this list and an audit row above disagree, this list is current.

- EX1 MUST r2.0 (sustainable-fisheries#r2-1): distractors now "It makes the fish breed much faster than they did before", "It lets the boats catch more fish each year than before" (edits #7–#8). KEY CHANGE (distractors).
- EX2 MUST practice Q1 (quiz-TF-1): distractors now "Larger holes catch more of the big adult fish in each trawl", "Small fish are not safe for people to eat, so are left alone", "It lets the boats catch more fish in a shorter time" (edits #15–#17). KEY CHANGE (distractors).
- EX3 SHOULD practice Q3 + BLIND MED quiz-TF-3: key now "The stock rose after the quota, so the quota may have helped" (the data show a rise after the quota, not breeding); distractors "The quota made the stock fall even further than before", "The stock recovered fully within a single year of the quota", "The stock stayed the same in the years after the quota". Stem kept. KEY CHANGE.
- EX4 SHOULD practice Q5 (quiz-TF-5): distractors now "Fish only live for about one year, so none are left", "The water has to warm up again before fish can breed", "It does not: one year without fishing is always enough". KEY CHANGE (distractors).
- EX5 NOTE fig:cod-stock-recovery / r4 data twice: no change.
