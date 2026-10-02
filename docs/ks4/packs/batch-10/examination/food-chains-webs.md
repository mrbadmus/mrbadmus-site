# Examination — Food Chains and Food Webs (food-chains-webs) — AQA 8464 4.7.2.1 / 8461 4.7.2.1 (+ 8461 4.7.4 biology only)
Verdict: SOURCE OK WITH FLAGS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-10/04-checked-science-source/biology-4.7.1-food-chains-webs.md` (the data's "4.7.1" is the site's coarse parent number; AQA's core clause is 4.7.2.1).
Spec sources read as text: `AQA-8464-spec.txt` (v1.1) 4.7.1.1, 4.7.2.1 — searched for "trophic", "biomass", "decomposer", "apex": 8464 has none of them in ecology except "producers of biomass"; `AQA-8461-spec.txt` (v1.0) 4.7.1.1, 4.7.2.1, 4.7.4.1–4.7.4.3. No equation sheet applies. Route audit read: `ks4-routes/docs/ks4/route-audit/biology.md` row `food-chains-webs` (OK, CF CH TF TH, 4.7.2.1) — the page route is right; the audit did not tag the biology-only layer inside it.

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n; th1–th3 = theory chunks. The CF and TF copies differ from TH only in `higher` (`null`), so `higher` is currently served on CH and TH.

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 / 8461 | **4.7.2.1** | Levels of organisation (producers, food chains, consumers, predators/prey) | base |
| 8464 / 8461 | 4.7.1.1 | Communities (interdependence — species removal in a web) | base |
| 8461 | **4.7.4.1** | Trophic levels | **(biology only)** |
| 8461 | **4.7.4.2** | Pyramids of biomass | **(biology only)** |
| 8461 | **4.7.4.3** | Transfer of biomass | **(biology only)** |

Spec statements (verbatim):
8464 = 8461 4.7.2.1: "Students should understand that photosynthetic organisms are the producers of biomass for life on Earth. Feeding relationships within a community can be represented by food chains. All food chains begin with a producer which synthesises molecules. This is usually a green plant or alga which makes glucose by photosynthesis. … Producers are eaten by primary consumers, which in turn may be eaten by secondary consumers and then tertiary consumers. Consumers that kill and eat other animals are predators, and those eaten are prey."
8461 4.7.4.1 (biology only): "Trophic levels can be represented by numbers, starting at level 1 with plants and algae. … Level 4: Carnivores that eat other carnivores are called tertiary consumers. Apex predators are carnivores with no predators. Decomposers break down dead plant and animal matter by secreting enzymes into the environment. Small soluble food molecules then diffuse into the microorganism."
8461 4.7.4.3 (biology only): "Producers are mostly plants and algae which transfer about 1 % of the incident energy from light for photosynthesis. Only approximately 10 % of the biomass from each trophic level is transferred to the level above it. Losses of biomass are due to: • not all the ingested material is absorbed, some is egested as faeces • some absorbed material is lost as waste, such as carbon dioxide and water in respiration and water and urea in urine. Large amounts of glucose are used in respiration. Students should be able to calculate the efficiency of biomass transfers between trophic levels by percentages or fractions of mass. Students should be able to explain how this affects the number of organisms at each trophic level."

## 2. Route table
| # | teachable point (pack location) | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Food chain = feeding relationships; arrows point to the eater (th1; common_mistake) | base | 4.7.2.1 | all four | OK |
| R2 | Producer (photosynthesis), primary/secondary/tertiary consumer (th1; key_note) | base | 4.7.2.1 | all four | OK; algae too (FCW-F5) |
| R3 | "Each feeding level is called a TROPHIC LEVEL" (th1) | triple | 8461 4.7.4.1 (biology only) | all four | **ROUTE** (FCW-F1) |
| R4 | Energy/biomass lost at each level, ~10%, why; few organisms at top; ≤ 4–5 levels (th2; key_note) | triple | 8461 4.7.4.3 (biology only) | all four | **ROUTE** (FCW-F1); "excreted as faeces" IMPRECISE (FCW-F4) |
| R5 | Food webs; removing a predator or prey species (th3) | base | 4.7.1.1; 4.7.2.1 | all four | OK |
| R6 | Keystone species; Yellowstone wolves, sea otters (th3) | not in spec (context) | — | all four | OK as context |
| R7 | `higher`: pyramids of biomass, efficiency equation, ~10%, losses | triple (not HT) | 8461 4.7.4.2, 4.7.4.3 (biology only) | CH TH | **ROUTE** (FCW-F2); "biomass lost as heat" IMPRECISE (FCW-F3) |
| R8 | `higher`: pyramids of number | not in spec | — | CH TH | OFF-SPEC (FCW-F2) |
| R9 | Decomposers (matching) | triple | 8461 4.7.4.1 | all four | to be replaced; triple if kept |
| R10 | q1 — why ≤ 4–5 trophic levels | triple | 8461 4.7.4.3 (biology only) | all four | OK science; **ROUTE** — TF TH only (FCW-F1) |
| R11 | q2 — foxes die → rabbits up → grass down | base | 4.7.1.1; 4.7.2.1 | all four | OK; wx1 wording (FCW-F6) |
| — | RP, equations, FIFA, examiner_tip | none | — | — | correct here. (RP7/RP9 sits under 4.7.2.1 but is taught in sampling-techniques; the efficiency calculation is taught in transfer-of-biomass.) |

True routes: CF CH TF TH for the page (matches the site), with a triple layer (trophic levels, biomass/energy transfer, pyramids) that should show on TF TH only.

## 3. Check table
| # | item | claim (verbatim or abridged) | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | th1 | food chain shows feeding relationships and direction of energy flow | OK | 8464 does not mention energy here; the arrow convention is assessed on every route. | 4.7.2.1 |
| C2 | th1 | arrows show direction of energy transfer, food → eater | OK | — | — |
| C3 | th1 | producer makes own food by photosynthesis (green plants, algae); all chains start with one | OK | Spec: "usually a green plant or alga which makes glucose by photosynthesis". | 4.7.2.1 |
| C4 | th1 | primary (usually herbivore), secondary, tertiary (often top predator) | OK | "Top predator" = 8461's "apex predator" (biology only). | 4.7.2.1; 8461 4.7.4.1 |
| C5 | th1 | Grass → Rabbit → Fox → Eagle, labelled | OK | Plausible (golden eagles take foxes occasionally); fine as a model chain. | — |
| C6 | th1 | "Each feeding level is called a TROPHIC LEVEL" | OK; ROUTE | Term is biology only. (FCW-F1) | 8461 4.7.4.1 |
| C7 | th2 | energy enters as sunlight, absorbed in photosynthesis, stored in glucose | OK | Spec adds producers transfer about 1% of incident light energy (biology only). | 8461 4.7.4.3 |
| C8 | th2 | energy lost each level: respiration → heat; not all eaten; faeces | OK; ROUTE | Biology only. AQA frames this as loss of **biomass**. (FCW-F1) | 8461 4.7.4.3 |
| C9 | th2 | "SOME MATERIAL is excreted as faeces and not digested" | IMPRECISE | Faeces are **egested**; excretion is removal of metabolic waste (CO₂, urea). AQA's word: "egested as faeces". (FCW-F4) | 8461 4.7.4.3 |
| C10 | th2 | about 10% passes to the next level | OK; ROUTE | Spec: "approximately 10 % of the biomass". | 8461 4.7.4.3 |
| C11 | th2 | producers most energy and biomass; each level up less, and fewer organisms; chains rarely > 4–5 levels | OK; ROUTE | "Fewer organisms" holds for the usual case (spec: "explain how this affects the number of organisms at each trophic level"). | 8461 4.7.4.3 |
| C12 | th3 | food web = interconnected chains; organisms eat/are eaten by more than one thing | OK | — | 4.7.1.1 |
| C13 | th3 | predator removed → prey increase → their food decreases; prey removed → predators decline → other prey may increase | OK | Spec: "If one species is removed it can affect the whole community." | 4.7.1.1 |
| C14 | th3 | keystone species; Yellowstone wolves; sea otters in kelp forests | OK / OFF-SPEC | Both well-documented; "keystone" is not a spec term. | — |
| C15 | higher | pyramids of biomass show dry mass; always narrow upward | OK; ROUTE | Biology only, not HT. "Always" is how AQA treats pyramids of biomass. (FCW-F2) | 8461 4.7.4.2 |
| C16 | higher | pyramids of number can be inverted (oak tree → insects) | OFF-SPEC | Pyramids of number are not in the current spec. (FCW-F2) | — |
| C17 | higher | efficiency (%) = biomass transferred ÷ biomass available × 100; ~10% | OK; ROUTE | Biology only, not HT. Spec: "by percentages or fractions of mass". (FCW-F2) | 8461 4.7.4.3 |
| C18 | higher | "90% of biomass is lost at each level as heat (respiration), undigested material (faeces), and uneaten portions" | IMPRECISE | Biomass is not lost "as heat" — energy is. Biomass is lost as CO₂ and water in respiration, water and urea in urine, and egested faeces. (FCW-F3) | 8461 4.7.4.3 |
| C19 | common_mistake | arrows go from prey to predator (energy flow) | OK | The most-lost mark on this topic. | 4.7.2.1 |
| C20 | common_mistake | "PRODUCERS are PLANTS (photosynthetic)" | IMPRECISE (minor) | Spec: "usually a green plant or alga". (FCW-F5) | 4.7.2.1 |
| C21 | key_note | chain roles; arrows = energy flow; ~10% passes on, rest lost as heat, waste, movement; webs | OK; ROUTE | The ~10% sentence is biology only. "Movement" is energy used via respiration. | 8461 4.7.4.3 |
| C22 | matching | 5 pairs incl. decomposers | OK | To be replaced; decomposers are biology only (8461 4.7.4.1). | — |
| C23 | q1 key | energy lost at each level, too little at top to support many organisms | OK; ROUTE | Biology only — TF TH. | 8461 4.7.4.3 |
| C24 | q1 wx1 | size can increase, but the limit is energy | OK, aligned | Answers option 1 ("too large"). | — |
| C25 | q1 wx2 | food chains are not navigated; limit is energy loss, not cognitive | OK, aligned | Answers option 2 ("too complex to navigate"). | — |
| C26 | q1 wx3 | no fixed rule about producers; limit is progressive energy loss | OK, aligned | Answers option 3 ("producers cannot support > 4"). | — |
| C27 | q2 key | grass decreases — more rabbits eat more grass | OK | — | 4.7.1.1 |
| C28 | q2 wx1 | "Fox death → reduced decomposition adds some nutrients, but the dominant effect is … grass DECREASES" | OK, aligned; IMPRECISE (wording) | Answers option 1 (nutrients from dead foxes). "Reduced decomposition adds some nutrients" contradicts itself — decomposing foxes would add nutrients. Conclusion correct. (FCW-F6) | — |
| C29 | q2 wx2 | plants are part of food webs as producers | OK, aligned | Answers option 2. | 4.7.2.1 |
| C30 | q2 wx3 | rabbit–grass is herbivory, not mutualism | OK, aligned | Answers option 3. "Mutualism" not a spec term but explained. | — |

wrong_explanations alignment: all 6 keys read in full; each explains its own option. Count: **0 WRONG**; **ROUTE**: C6, C8, C10, C11, C15, C17, C21, C23 (biology-only content served to Combined; `higher` is triple, not HT); **OFF-SPEC**: C14, C16; **IMPRECISE**: C9, C18, C20, C28. No `[NEW — to be examined]` lines in this file.
