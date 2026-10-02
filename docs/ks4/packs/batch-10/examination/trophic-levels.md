# Examination — Trophic Levels (trophic-levels) — AQA 8461 4.7.4.1 (biology only)
Verdict: SOURCE OK WITH FLAGS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-10/04-checked-science-source/biology-4.7.4.1-trophic-levels.md`.
Spec sources read as text: `AQA-8461-spec.txt` (v1.0) 4.7.4.1, 4.7.4.2, 4.7.4.3, 4.7.2.1, 4.7.5; `AQA-8464-spec.txt` (v1.1) 4.7.2.1 — confirmed 8464 has no trophic-levels section (food chains, producers and primary/secondary/tertiary consumers are in 4.7.2.1, base). No equation sheet applies. Route audit read: `ks4-routes/docs/ks4/route-audit/biology.md` row `trophic-levels` (OK, TF TH).

Conventions: q1–q2 = quiz items in file order; "opt n" = option index n (0 = credited); "wx n" = `wrong_explanations` key n; th1–th3 = theory chunks. The TF copy differs from TH only in `higher` (`null` = not shown).

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8461 Biology | **4.7.4.1** | Trophic levels | **(biology only)** (section 4.7.4 heading) |
| 8464 / 8461 | 4.7.2.1 | Levels of organisation — food chains, producer, primary/secondary/tertiary consumers, predators | base |
| 8461 | 4.7.4.3 | Transfer of biomass — ~10 %, losses | (biology only) — taught in `transfer-of-biomass` |

Spec statements (verbatim, 8461 4.7.4.1): "Students should be able to describe the differences between the trophic levels of organisms within an ecosystem." "Trophic levels can be represented by numbers, starting at level 1 with plants and algae. Further trophic levels are numbered subsequently according to how far the organism is along the food chain." "Level 1: Plants and algae make their own food and are called producers. Level 2: Herbivores eat plants/algae and are called primary consumers. Level 3: Carnivores that eat herbivores are called secondary consumers. Level 4: Carnivores that eat other carnivores are called tertiary consumers. Apex predators are carnivores with no predators." "Decomposers break down dead plant and animal matter by secreting enzymes into the environment. Small soluble food molecules then diffuse into the microorganism."

## 2. Route table
| # | teachable point | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Producer / primary / secondary / tertiary consumer (th1) | base | 8464/8461 4.7.2.1 | TF TH | OK |
| R2 | Trophic levels numbered 1–4; apex predators (th1; key_note) | triple | 8461 4.7.4.1 | TF TH | OK |
| R3 | Decomposers (th2) | triple | 8461 4.7.4.1 | TF TH | GAP — enzymes/diffusion missing (TL-F2) |
| R4 | Food chains, food webs, arrow = energy flow (th2; common_mistake; q1) | base | 8464/8461 4.7.2.1 | TF TH | OK |
| R5 | ~10 % transfer; losses; fewer levels (th3; q2) | triple | 8461 4.7.4.3 | TF TH | IMPRECISE — energy vs biomass (TL-F3) |
| R6 | `higher` — efficiency calc; human food production; food webs | triple / base — **not HT** | 8461 4.7.4.3, 4.7.5; 8464/8461 4.7.1.1 | TH only | ROUTE (TL-F1) |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | th1 | Trophic level = position in a food chain — "how far it is from the original energy source (the Sun)" | IMPRECISE (minor) | Spec: numbered "according to how far the organism is along the food chain". | 4.7.4.1 |
| C2 | th1 | Level 1 producers: plants and algae, photosynthesis; grass, oak, phytoplankton, seaweed | OK | — | 4.7.4.1 |
| C3 | th1 | Level 2 herbivores: rabbits, caterpillars, cows, zooplankton | OK | — | 4.7.4.1 |
| C4 | th1 | Level 3 carnivores eating primary consumers: fox, frog, small fish | OK | — | 4.7.4.1 |
| C5 | th1 | Level 4 carnivores eating secondary consumers: eagles, sharks, humans | OK | — | 4.7.4.1 |
| C6 | th1 | Apex predators not eaten by any other organism in that ecosystem | OK | Spec: "carnivores with no predators". | 4.7.4.1 |
| C7 | th2 | Decomposers (bacteria, fungi) break down dead organisms and waste; "digest complex organic molecules → release nutrients" | GAP | Spec mechanism missing: enzymes secreted into the environment; small soluble molecules diffuse into the microorganism. | 4.7.4.1 |
| C8 | th2 | Decomposers not usually given a numbered level | OK | — | — |
| C9 | th2 | Food chain arrow = energy transfer direction; food web = interconnected chains | OK | — | 4.7.2.1 |
| C10 | th3 | Energy lost at each level: respiration (heat), movement, excretion, undigested material; ~10 % transferred | IMPRECISE | AQA states it as biomass: "Only approximately 10 % of the biomass from each trophic level is transferred"; losses = egestion (faeces), CO₂ and water from respiration, water and urea in urine. Belongs to 4.7.4.3. | 8461 4.7.4.3 |
| C11 | th3 | 1000 → 100 → 10 → 1 kJ | OK | 10 % each step ✓ | — |
| C12 | th3 | Higher levels support fewer organisms; chains rarely > 4–5 levels | OK | — | 4.7.4.3 |
| C13 | th3 | "This pattern of decreasing energy is shown in PYRAMIDS OF BIOMASS" | IMPRECISE | Pyramids of biomass show biomass, not energy. | 8461 4.7.4.2 |
| C14 | `higher` | Efficiency calculation; sustainability of fewer levels; human food production; food webs | ROUTE | None is HT. Efficiency = 4.7.4.3 (biology only, TF TH); food production = 4.7.5 (biology only); food-web predictions = 4.7.1.1 (base). Said in energy, spec says biomass. | TL-F1 |
| C15 | common_mistake | Arrows = energy flow from prey to predator; ~10 % passes on, most lost in respiration | OK | "Most lost in respiration" is acceptable; egestion and excretion are the other losses. | 4.7.2.1; 4.7.4.3 |
| C16 | key_note | Summary | OK | — | — |
| C17 | q1 key | Arrows point prey → predator; energy flow grass → rabbit → fox | OK | — | 4.7.2.1 |
| C18 | q1 opt1 / wx1 | predator → prey | OK | wx1 explains opt1 ✓ | — |
| C19 | q1 opt2 / wx2 | both ways | OK | wx2 explains opt2 ✓ | — |
| C20 | q1 opt3 / wx3 | arrows organisational only | OK | wx3 explains opt3 ✓ | — |
| C21 | q2 key | ~10 % of energy transferred, so too little for another level | OK | "Energy" is credited alongside "biomass" in this context. | 4.7.4.3 |
| C22 | q2 opt1 / wx1 | not enough species | OK | wx1 explains opt1 ✓ | — |
| C23 | q2 opt2 / wx2 | too many organisms at high levels | OK | wx2 explains opt2 ✓ | — |
| C24 | q2 opt3 / wx3 | predators too large | OK | wx3 explains opt3 ✓ | — |
| C25 | matching (to be replaced) | oak → caterpillar → blue tit → sparrowhawk; decomposers | OK | — | — |

Count: **0 WRONG**; **IMPRECISE**: C1, C10, C13; **GAP**: C7; **ROUTE**: C14. wrong_explanations: both items aligned (key n explains option n). No CFIFA line in this file.

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| `higher` | Not HT; TF pupils lose it; its content belongs to other lessons | TL-F1. |
| q1, q2 | — | Usable on TF and TH. |

## 5. Verdict
SOURCE OK WITH FLAGS. Routes are right (8461 4.7.4.1 is biology only → TF TH). Level definitions and both quiz items are correct. The spec's decomposer mechanism (secreted enzymes, diffusion of soluble molecules) is missing; th3 speaks of energy where AQA speaks of biomass and wrongly ties energy to pyramids of biomass; the `higher` field is not HT. Nothing for Mide.
