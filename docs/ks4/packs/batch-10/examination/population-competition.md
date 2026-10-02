# Examination — Population and Competition (population-competition) — AQA 8464 4.7.1.1, 4.7.2.1 / 8461 4.7.1.1, 4.7.2.1
Verdict: SOURCE OK WITH FLAGS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-10/04-checked-science-source/biology-4.7.1-population-competition.md` (the data's "4.7.1" is the site's coarse parent number; AQA's clauses are 4.7.1.1 competition and 4.7.2.1 predator–prey cycles).
Spec sources read as text: `AQA-8464-spec.txt` (v1.1) 4.7.1.1, 4.7.1.3, 4.7.2.1; `AQA-8461-spec.txt` (v1.0) 4.7.1.1, 4.7.1.3, 4.7.2.1. Searched both specs for "carrying capacity", "intraspecific", "density" — none present. No equation sheet applies. Route audit read: `ks4-routes/docs/ks4/route-audit/biology.md` row `population-competition` (OK, CF CH TF TH, 4.7.1.1, 4.7.2.1).

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n; th1–th3 = theory chunks. The CF and TF copies differ from TH only in `higher` (`null`), so `higher` is currently served on CH and TH.

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 / 8461 | **4.7.1.1** | Communities (competition, interdependence) | base |
| 8464 / 8461 | **4.7.2.1** | Levels of organisation (predators, prey, predator–prey cycles) | base |
| Supporting | 4.7.1.3 Biotic factors ("one species outcompeting another") | | base |

Spec statements (verbatim, 8464 = 8461):
4.7.1.1: "the importance of interdependence and competition in a community." "suggest the factors for which organisms are competing in a given habitat." "To survive and reproduce, organisms require a supply of materials from their surroundings and from the other living organisms there. Plants in a community or habitat often compete with each other for light and space, and for water and mineral ions from the soil. Animals often compete with each other for food, mates and territory."
4.7.2.1: "Consumers that kill and eat other animals are predators, and those eaten are prey. In a stable community the numbers of predators and prey rise and fall in cycles. Students should be able to interpret graphs used to model these cycles." (WS 1.2, MS 4a)
4.7.1.3: "one species outcompeting another so the numbers are no longer sufficient to breed."

## 2. Route table
| # | teachable point (pack location) | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Birth rate vs death rate; limits on growth: food, water, space, predation, disease (th1) | base (context) | 4.7.1.1, 4.7.1.3 | all four | OK |
| R2 | Exponential growth; carrying capacity (th1; higher; key_note; matching) | not in spec | — | all four | OFF-SPEC (PC-F2) |
| R3 | Predator–prey cycles; predator follows prey with a lag (th1; common_mistake; key_note) | base | 4.7.2.1 | all four | OK |
| R4 | Competition: resources animals and plants compete for (th2) | base | 4.7.1.1 | all four | OK; use spec lists (PC-F5) |
| R5 | Intraspecific vs interspecific competition (th2; key_note; q2) | not in spec (terms); base (idea) | 4.7.1.1, 4.7.1.3 | all four | OFF-SPEC terms (PC-F3) |
| R6 | Stronger competitor drives weaker to local extinction; grey vs red squirrels (th2) | base | 4.7.1.3 | all four | OK |
| R7 | Density-dependent / density-independent factors; human impacts (th3) | not in spec (framing); human impacts base context (4.7.3) | — | all four | OFF-SPEC (PC-F2) |
| R8 | `higher` s1: interpret predator–prey graphs, time lag, predict knock-on effects in a web | base (not HT) | 4.7.2.1; 4.7.1.1 | CH TH | **ROUTE** (PC-F1) |
| R9 | `higher` s2–s3: carrying capacity; intraspecific competition as density-dependent control | not in spec | — | CH TH | OFF-SPEC (PC-F1, PC-F2) |
| R10 | q1 — why predator peaks after prey | base | 4.7.2.1 | all four | OK |
| R11 | q2 — why intraspecific competition is more intense | not in spec (terms) | (4.7.1.1) | all four | OFF-SPEC (PC-F3) |
| — | RP, equations, FIFA, examiner_tip | none | — | — | correct |

True routes: CF CH TF TH (matches the site). No HT layer, no triple layer.

## 3. Check table
| # | item | claim (verbatim or abridged) | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | th1 | population grows when birth rate > death rate | OK | Ignores migration; fine at GCSE. Not a spec statement. | — |
| C2 | th1 | could grow exponentially; limited by food, water, space, predation, disease, waste | OK / OFF-SPEC | Exponential growth not in spec. Limiting factors consistent with 4.7.1.1, 4.7.1.3. | 4.7.1.3 |
| C3 | th1 | carrying capacity = maximum population a habitat can sustainably support | OK / OFF-SPEC | Correct definition; term not in either spec. (PC-F2) | — |
| C4 | th1 | at carrying capacity birth ≈ death rate; stabilises with fluctuations | OK / OFF-SPEC | — | — |
| C5 | th1 | predator–prey cycle sequence; predator changes follow prey with a lag | OK | Spec: "rise and fall in cycles"; interpret graphs. | 4.7.2.1 |
| C6 | th2 | competition = organisms need the same limited resource | OK | — | 4.7.1.1 |
| C7 | th2 | intraspecific most intense (identical needs); controls population size | OK / OFF-SPEC | Standard ecology; terms not in spec. (PC-F3) | — |
| C8 | th2 | robins' territories, stags fighting for mates, oaks competing for light | OK | Match spec's territory, mates, light. | 4.7.1.1 |
| C9 | th2 | stronger competitor may drive weaker to local extinction | OK | Spec: "outcompeting another so the numbers are no longer sufficient to breed". | 4.7.1.3 |
| C10 | th2 | grey squirrels outcompete reds for food and nesting sites → reds largely absent from England | OK | Accurate (reds survive mainly in the north of England, Isle of Wight, Brownsea). Greys also carry squirrelpox, which kills reds; competition remains the accepted GCSE example. | 4.7.1.3 |
| C11 | th2 | animals: food, water, territory, mates, shelter; plants: light, water, minerals, space | OK | Spec lists: plants — light, space, water, mineral ions; animals — food, mates, territory. Use "mineral ions". (PC-F5) | 4.7.1.1 |
| C12 | th3 | density-dependent: food, disease, predation, waste | OK / OFF-SPEC | A-level framing. (PC-F2) | — |
| C13 | th3 | density-independent: weather, disasters, human activity | OK / OFF-SPEC | — | — |
| C14 | th3 | human impacts: hunting/fishing, deforestation, pollution, invasive species | OK | Context; 4.7.3 covers human impacts. | 4.7.3 |
| C15 | higher s1 | interpret predator–prey graphs, time lag; predict effects in a food web | OK; ROUTE | Base skill on every route, no HT label. (PC-F1) | 4.7.2.1; 4.7.1.1 |
| C16 | higher s2–s3 | carrying capacity; intraspecific competition as primary density-dependent control | OFF-SPEC | Neither in spec. (PC-F1, PC-F2) | — |
| C17 | common_mistake | predator follows prey with a lag; rises after prey rises, falls after prey declines | OK | — | 4.7.2.1 |
| C18 | key_note | "Population limited by resources (food, water, space), predation and disease = carrying capacity." | IMPRECISE | The limiting factors are not the carrying capacity; they set it. (PC-F4) | — |
| C19 | key_note | predator–prey out of phase; intra most intense; inter between species | OK | — | 4.7.2.1 |
| C20 | matching | 5 pairs | OK | To be replaced. | — |
| C21 | q1 key | time lag — predators take time to reproduce in response to more food | OK | — | 4.7.2.1 |
| C22 | q1 wx1 | lag is about reproduction; predators eating prey reduces prey | OK, aligned | Answers option 1. | — |
| C23 | q1 wx2 | prey outnumbering predators normal; timing is reproduction lag | OK, aligned | Answers option 2. | — |
| C24 | q1 wx3 | migration can occur; lag is biological response time | OK, aligned | Answers option 3. | — |
| C25 | q2 key | same species have identical needs, compete for exactly the same resources | OK / OFF-SPEC | Correct; the question depends on two terms not in the spec. (PC-F3) | — |
| C26 | q2 wx1 | intensity is about overlap of needs, not strength | OK, aligned | Answers option 1. | — |
| C27 | q2 wx2 | interspecific can involve large numbers; intensity is about overlap | OK, aligned | Answers option 2. | — |
| C28 | q2 wx3 | different species CAN compete (squirrels); niche overlap | OK, aligned | Answers option 3. "Niche" off-spec gloss. | — |

wrong_explanations alignment: all 6 keys read in full; each explains its own option. Count: **0 WRONG**; **ROUTE**: C15 (`higher` predator–prey skill is base, not HT); **OFF-SPEC**: C2–C4, C7, C12–C13, C16, C25 (carrying capacity, density factors, intra/inter terms); **IMPRECISE**: C18. No `[NEW — to be examined]` lines in this file.
