# Examination — The Haber Process (haber-process) — AQA 8462 4.10.4.1
Verdict: SOURCE OK WITH FLAGS (science correct; the explanation of the conditions is HT only, so TF has no usable frozen quiz item)
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-14/04-checked-science-source/chemistry-4.10.4.1-haber-process.md`.
Spec sources read: `AQA-8462-spec.txt` (v1.1, 04 Oct 2019) §4.10.4.1, §4.6.1.4, §4.6.2.1–4.6.2.7, §4.3.3.2. No equation sheet applies. Route audit: `ks4-routes/docs/ks4/route-audit/chemistry.md` row `haber-process` ("HT layer: interpret rate/yield graphs, compromise conditions"). Agrees.

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n (option 0 is the key on both items).

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8462 | **4.10.4.1** | The Haber process | (chemistry only); the last four "Students should be able to" bullets are **(HT only)** |
| Supporting | 8462 4.6.1.4 Catalysts (base); 4.6.2.1–4.6.2.3 reversible reactions, energy changes, equilibrium (base); 4.6.2.4–4.6.2.7 Le Chatelier, concentration, temperature, pressure (**HT only**); 4.3.3.2 Atom economy (chemistry only, base) | | |

Spec statements (verbatim, 4.10.4.1): "The Haber process is used to manufacture ammonia, which can be used to produce nitrogen-based fertilisers. The raw materials for the Haber process are nitrogen and hydrogen. Students should be able to recall a source for the nitrogen and a source for the hydrogen used in the Haber process. The purified gases are passed over a catalyst of iron at a high temperature (about 450°C) and a high pressure (about 200 atmospheres). Some of the hydrogen and nitrogen reacts to form ammonia. The reaction is reversible so some of the ammonia produced breaks down into nitrogen and hydrogen: nitrogen + hydrogen ⇌ ammonia. On cooling, the ammonia liquefies and is removed. The remaining hydrogen and nitrogen are recycled." "(HT only) Students should be able to: • interpret graphs of reaction conditions versus rate • apply the principles of dynamic equilibrium in Reversible reactions and dynamic equilibrium to the Haber process • explain the trade-off between rate of production and position of equilibrium • explain how the commercially used conditions for the Haber process are related to the availability and cost of raw materials and energy supplies, control of equilibrium position and rate." MS 1a, 1c.

## 2. Route table
| # | teachable point | true layer | spec | verdict |
|---|---|---|---|---|
| R1 | Ammonia made by Haber; used for fertilisers (theory 1; key_note) | triple | 4.10.4.1 | OK |
| R2 | Raw materials N₂ (air) and H₂ (natural gas) (theory 1; common_mistake) | triple | 4.10.4.1 | OK |
| R3 | Steam reforming equation; fractional distillation of air (theory 1) | triple (beyond spec, correct) | — | OK |
| R4 | N₂ + 3H₂ ⇌ 2NH₃; reversible (theory 1; equations) | triple | 4.10.4.1; 4.6.2.1 | OK |
| R5 | Forward reaction exothermic (theory 1) | triple | 4.6.2.2 | OK |
| R6 | Conditions: ~450 °C, ~200 atm, iron catalyst (theory 2; key_note; equations) | triple | 4.10.4.1 | OK |
| R7 | Cool → ammonia liquefies, removed; unreacted gases recycled (theory 1, 2; matching) | triple | 4.10.4.1 | OK |
| R8 | Catalyst speeds up the reaction (theory 2) | triple | 4.6.1.4; 4.10.4.1 | OK |
| R9 | Catalyst does not change equilibrium position / yield (theory 2; common_mistake; q2) | **triple-higher** | 4.10.4.1 (HT) "apply the principles of dynamic equilibrium" | ROUTE (HB-F1) |
| R10 | Temperature: lower T → more NH₃ but slower; 450 °C compromise (theory 2, 3; common_mistake; FIFA) | **triple-higher** | 4.10.4.1 (HT); 4.6.2.6 (HT) | ROUTE (HB-F1) |
| R11 | Pressure: 4 → 2 molecules; higher p → more NH₃; 200 atm cost/safety compromise (theory 2, 3; q1) | **triple-higher** | 4.10.4.1 (HT); 4.6.2.7 (HT) | ROUTE (HB-F1) |
| R12 | Economic and environmental considerations; green ammonia (theory 3) | triple-higher (the "availability and cost of raw materials and energy" bullet) | 4.10.4.1 (HT) | OK |
| R13 | Graphs of conditions vs rate / yield | triple-higher | 4.10.4.1 (HT) | **MISSING** (HB-F5) |
| R14 | Haber/Bosch history; feeds ~half the world (theory 3) | triple (context) | — | OK |
| R15 | `higher` field: Le Chatelier, compromise, sustainability, recycling | triple-higher | 4.10.4.1 (HT); 4.6.2.4 (HT) | OK. Except "Calculate atom economy", which is ROUTE (HB-F6) |
| R16 | FIFA (why 450 °C) | triple-higher | 4.10.4.1 (HT) | OK |
| R17 | q1 (why not higher pressure) | triple-higher | 4.10.4.1 (HT) | OK, TH only |
| R18 | q2 (catalyst, equilibrium unchanged) | triple-higher | 4.10.4.1 (HT) | OK, TH only (one imprecise phrase, HB-F2) |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | theory 1 | ammonia used for fertilisers, explosives, chemicals | OK | — | 4.10.4.1 |
| C2 | theory 1 | N₂ from air (78 %), by fractional distillation | OK | Spec only needs "air". | 4.10.4.1 |
| C3 | theory 1 | H₂ from natural gas by steam reforming: CH₄ + H₂O → CO + 3H₂ | OK | Balanced ✓. Beyond spec. | 4.10.4.1 |
| C4 | theory 1 | N₂(g) + 3H₂(g) ⇌ 2NH₃(g), ΔH = −92 kJ/mol, exothermic | OK | −92 kJ per mole of reaction as written (2 mol NH₃). ΔH notation is beyond spec. | 4.6.2.2 |
| C5 | theory 1 | "At equilibrium, only about 15% of reactants convert to ammonia under typical conditions." | IMPRECISE | About 15 % is the **single-pass** conversion; the gases leave before reaching equilibrium. The equilibrium yield at 450 °C and 200 atm is about 25–30 %, which is what AQA's yield-vs-pressure graphs show. Say "only about 15 % is converted on each pass through the reactor". | 4.10.4.1 |
| C6 | theory 1; matching | recycling → overall conversion ~98 % | OK | Commonly quoted figure (about 97–98 %). | 4.10.4.1 |
| C7 | theory 2 | lower T favours ammonia (exothermic); lower T slower; 450 °C compromise | OK | HT. | 4.6.2.6 |
| C8 | theory 2 | 4 mol gas → 2 mol gas; higher p favours NH₃; 200 atm (cost, danger) | OK | Spec says "molecules"; fine. HT. | 4.6.2.7 |
| C9 | theory 2 | iron catalyst with Al₂O₃/K₂O promoters; speeds rate; no change to yield; allows a lower T | OK | Promoters beyond spec ("do not need to know the names of catalysts other than those specified"). Harmless; omit on TF. | 4.6.1.4 |
| C10 | theory 2 | cooling liquefies NH₃; N₂, H₂ stay gaseous, recycled | OK | Spec wording. | 4.10.4.1 |
| C11 | theory 3 | rate/yield compromise; high pressure expensive; catalyst cheap; recycling | OK | HT. | 4.10.4.1 (HT) |
| C12 | theory 3 | methane → CO₂ footprint; green ammonia via electrolysis; ~2 % of global energy | OK | 1–2 % is the usual estimate. | — |
| C13 | theory 3 | Haber and Bosch, early 1900s; sustains about half the population | OK | Widely cited estimate (40–50 %). | — |
| C14 | `higher` | "Calculate atom economy of the Haber process" | ROUTE | Atom economy (4.3.3.2) is chemistry-only base, not HT. Here it is trivially 100 % (one product). | 4.3.3.2 |
| C15 | `higher` | remaining items (Le Chatelier on T, p, concentration; 450 °C compromise; sustainability; recycling) | OK | HT, correct. | 4.6.2.4–4.6.2.7; 4.10.4.1 |
| C16 | common_mistake | catalyst doesn't change yield; 450 °C compromise; N₂ from air, H₂ from natural gas | OK | First two sentences TH; third is TF + TH. | 4.10.4.1 |
| C17 | key_note | as above | OK | Mixed layers: split at Design time. | — |
| C18 | FIFA | four steps: rate vs yield separately; lower T → more yield, slower; too slow; 450 °C compromise | OK | HT. Not a calculation. | 4.10.4.1 (HT) |
| C19 | CFIFA Convert | "Nothing to convert — this FIFA explains a rate/yield trade-off rather than calculating from a measured quantity, so there is no unit to convert." | OK | Examined ✓. | CFIFA amendment |
| C20 | q1 key | very high pressure expensive (stronger reactors, more energy); 200 atm = yield/cost compromise | OK | Mark schemes also credit safety. | 4.10.4.1 (HT) |
| C21 | q1 opt 1 / wx1 | "higher p favours reactants" → wx1: higher p favours products (fewer moles); issue is cost | OK | Aligned. | 4.6.2.7 |
| C22 | q1 opt 2 / wx2 | "catalyst only works at 200 atm" → wx2: not so; cost decides | OK | Aligned. | — |
| C23 | q1 opt 3 / wx3 | "higher p decomposes NH₃" → wx3: "Ammonia is more stable at higher pressure (equilibrium favours it)…" | IMPRECISE | Aligned; conclusion right. "More stable" is loose: higher pressure shifts the equilibrium position towards ammonia (fewer gas molecules). Minor; usable. | 4.6.2.7 |
| C24 | q2 key | "increases the rate of both forward and reverse reactions equally — … equilibrium position is unchanged" | OK (IMPRECISE phrase) | Strictly, both rates go up by the same factor (Ea lowered by the same amount both ways), not by an equal amount. Acceptable at GCSE; AQA credits "speeds up both forward and reverse reactions". | 4.6.1.4; 4.10.4.1 (HT) |
| C25 | q2 opt 1 / wx1 | "bypassing equilibrium" → wx1: catalysts can't change where equilibrium lies | OK | Aligned. | — |
| C26 | q2 opt 2 / wx2 | "shifts equilibrium right" → wx2: lowers Ea for both directions equally | OK | Aligned (wording fits opt 2 well enough). | 4.6.1.4 |
| C27 | q2 opt 3 / wx3 | "lowers Ea only for forward" → wx3: if only forward were lowered, forward rate would rise more, but that is not how catalysts work | OK | Aligned. | 4.6.1.4 |
| C28 | matching (to be replaced) | four condition → reason pairs | OK | Rows 1–3 are HT reasoning. | — |

Count: **0 WRONG**; **IMPRECISE**: C5, C23, C24; **ROUTE**: R9–R11 (layering), C14. wrong_explanations alignment read item by item: all six aligned.

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| q1 | HT reasoning (trade-off, Le Chatelier on pressure) | TH only. Not usable on TF. |
| q2 | HT reasoning (dynamic equilibrium applied to Haber) | TH only. Not usable on TF. |
| FIFA | HT (trade-off) | TH only. |

## 5. For the lesson author
**Misconceptions seen in AQA marking:** "the catalyst increases the yield"; "high temperature increases the yield because it speeds the reaction up"; rate and yield treated as one thing; "pressure is kept low because high pressure lowers yield"; hydrogen "from water/air"; recycling described as "the ammonia is recycled".
**Typical questions** ⚑ examiner-drafted
- *Give a source of the nitrogen and of the hydrogen. [2]* — air (1); natural gas / methane (1). (TF + TH)
- *Describe how ammonia is separated from unreacted gases. [2]* — cooled, ammonia liquefies (1); unreacted N₂/H₂ recycled (1). (TF + TH)
- *(HT) Use the graph of % ammonia against pressure at 350/450/550 °C. Explain why 450 °C and 200 atm are used. [6]* — level-marked: lower T gives higher yield but slower rate; higher p gives higher yield but costly/dangerous; catalyst speeds rate, no effect on yield; compromise.

## 6. Verdict
SOURCE OK WITH FLAGS. Every fact is correct apart from one imprecise yield figure (C5). The main point is layering: all of the "why these conditions" reasoning, both quiz items and the FIFA are HT only (8462 4.10.4.1 HT bullets; 4.6.2.4–4.6.2.7). TF gets raw materials, equation, conditions as facts, liquefy-and-recycle, and catalyst = faster. The source's `higher` copy for TF is null, so as it stands TF would be served HT reasoning. CFIFA Convert line examined ✓. Nothing for Mide.
