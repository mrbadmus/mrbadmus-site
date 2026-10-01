# Examination — Thermal Conductivity and Reducing Unwanted Energy Transfers (thermal-conductivity) — AQA 8464 6.1.2.1 / 8463 4.1.2.1
Verdict: SOURCE HAS ERRORS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-4/04-checked-science-source/physics-6.1.2.1-thermal-conductivity.md`.
Spec sources read as text: `AQA-8464-spec.txt` (v1.1) §6.1.2.1 and the Combined RP list (RP14–21); `AQA-8463-spec.txt` (v1.1) §4.1.2.1, §8.2.2 (RP2); `AQA-8462-spec.txt` §4.2.2.8 (metals conduct thermal energy — delocalised electrons). Route audit `physics.md` row `thermal-conductivity` and §2 item 1 (approved move to base).

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n; T1–T3 = theory chunks. Quiz identical on TF and TH; TF `higher` copy is null.

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 | **6.1.2.1** | Energy transfers in a system | base |
| 8463 | **4.1.2.1** | Energy transfers in a system | base; RP2 (physics only) |
| 8463 | 8.2.2 | Required practical activity 2 (physics only) | triple |
| — | 8464/8463 "6.1.3"/"4.1.3" | National and global energy resources | the spec field's section — **wrong lesson** |

Spec statements (verbatim, 8464 = 8463): "Students should be able to explain ways of reducing unwanted energy transfers, for example through lubrication and the use of thermal insulation. The higher the thermal conductivity of a material the higher the rate of energy transfer by conduction across the material. Students should be able to describe how the rate of cooling of a building is affected by the thickness and thermal conductivity of its walls. Students do not need to know the definition of thermal conductivity." Suggested activity (both): "Investigate thermal conductivity using rods of different materials." 8463 only: "Required practical activity 2 (physics only): investigate the effectiveness of different materials as thermal insulators and the factors that may affect the thermal insulation properties of a material." No HT statement in either section. Combined's physics RPs (RP14–21) contain no insulation practical.

## 2. Route table
| # | teachable point | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Higher thermal conductivity → higher rate of conduction (T1; key_note) | base | 6.1.2.1 | TF TH | ROUTE — base, page must widen to CF CH (TC-F1) |
| R2 | Metals conduct well (free electrons); insulators: air, wood, fibreglass, wool (T1) | base | 6.1.2.1; 8462 4.2.2.8 | TF TH | OK (IMPRECISE wording, C3) |
| R3 | Unit W/m·K and numerical values (T1) | off-spec context | "do not need to know the definition" | TF TH | OFF-SPEC (C4) |
| R4 | Dissipation to surroundings; reducing unwanted transfers — insulation, lubrication, streamlining (T2; key_note; common_mistake) | base | 6.1.2.1 | TF TH | OK (C7 imprecise) |
| R5 | "Electromagnetic shielding" (T2 item 4) | none | — | TF TH | **WRONG** (TC-F2) |
| R6 | Thicker walls / lower conductivity → slower cooling (T2) | base | 6.1.2.1 ("rate of cooling of a building…") | TF TH | OK |
| R7 | k × A × ΔT ÷ thickness (T2) | off-spec | — | TF TH | OFF-SPEC (C10) |
| R8 | RP2 thermal insulators: method, variables, conclusion (T3; `rp`; q2) | **triple** | 8463 4.1.2.1 RP2 (physics only) | TF TH | OK as triple layer; GAP (C14) |
| R9 | Applications: buildings, fridges, cryogenics (T3) | base (context) | 6.1.2.1 | TF TH | OK |
| R10 | `higher` (TH) — rate calculation, U-values, wider double-glazing gaps | none — 6.1.2.1 has no HT content | — | TH | **WRONG / OFF-SPEC** (TC-F3) |
| R11 | q1 — trapped air vs glass | base | 6.1.2.1 | TF TH | OK |
| R12 | q2 — best measurement in the insulation RP | triple | RP2 | TF TH | **WRONG** (wx1; TC-F4) |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | T1 | thermal conductivity measures how well a material transfers energy by conduction | OK | Description, not a definition — fine (definition not required). | 6.1.2.1 |
| C2 | T1 | metals good conductors; free electrons carry energy | OK | (Chemistry calls them delocalised electrons.) | 8462 4.2.2.8 |
| C3 | T1 | insulators: "energy transferred only by vibration between tightly packed or sparse particles" | IMPRECISE | Solids: vibrations passed between neighbouring particles. Gases (air): particles far apart, energy passed only by occasional collisions — that is why air conducts so poorly. "Vibration… sparse particles" muddles the two. | 6.1.2.1; 6.3 particle model |
| C4 | T1 | unit W/m·K; copper ~400, glass ~1, air ~0.025 | OK values; OFF-SPEC | Values ✓ (Cu 401; glass 0.8–1; air 0.026). Not examinable — spec: "do not need to know the definition". | 6.1.2.1 |
| C5 | T1 | higher conductivity → faster transfer for same ΔT and thickness | OK | — | 6.1.2.1 |
| C6 | T2 | unwanted dissipation to the thermal store of the surroundings | OK | — | 6.1.2.1 |
| C7 | T2 | "Cavity wall insulation… reduces conduction through walls"; "Double-glazing — air gap… reduces conduction" | IMPRECISE | Cavity foam/fibreglass traps air in small pockets, so it also stops convection currents in the cavity; double glazing's gas gap is a poor conductor (and thin enough to limit convection). AQA mark schemes credit both "trapped air is a poor conductor" and "reduces convection". | 6.1.2.1 |
| C8 | T2 | lubrication, streamlining | OK | Lubrication is the spec's own example. | 6.1.2.1 |
| C9 | T2 | "ELECTROMAGNETIC SHIELDING: Reduces energy loss from electrical components." | **WRONG** | Shielding blocks electromagnetic interference; it is not a way to reduce wasted energy and is on no GCSE spec. Drop. TC-F2. | — |
| C10 | T2 | thicker / lower conductivity → less energy per second; "∝ thermal conductivity × area × ΔT ÷ thickness" | OK / OFF-SPEC | Qualitative statements ✓ (spec). The proportionality is correct physics but off-spec: no equation, not examinable. | 6.1.2.1 |
| C11 | T3 | RP2 method: wrap beakers, measure T at intervals, T–t graphs, steeper = worse insulator | OK | AQA's method: temperature every 3 min for ≈ 20 min, same starting temperature and volume. | 8463 8.2.2 |
| C12 | T3 | IV material; DV rate of cooling; controls initial T, volume, thickness, surface area | OK | — | RP2 |
| C13 | T3 | lowest conductivity → slowest cooling → best insulator; trapped air | OK | — | — |
| C14 | T3; `rp` | RP2 covers material type only | GAP | RP2's second half: "the factors that may affect the thermal insulation properties of a material" — e.g. thickness (number of layers) as IV with material fixed. TC-F5. | 8463 4.1.2.1 RP2 |
| C15 | T3 | applications: buildings, refrigeration, cryogenics | OK | — | — |
| C16 | `higher` | "Calculate rate of energy transfer through a material", "U-values" | OFF-SPEC | No equation for conduction in the spec; U-values not in spec. | 6.1.2.1 |
| C17 | `higher` | "Explain why double-glazing is more effective with wider gaps" | **WRONG** | Only up to ≈ 15–20 mm; wider gaps let convection currents form and insulation gets worse. Off-spec as well. TC-F3. | — |
| C18 | common_mistake | insulators slow, not stop; trapped air — poor conductor, convection reduced | OK | — | 6.1.2.1 |
| C19 | key_note | "Thermal conductivity: rate of energy transfer by conduction." | IMPRECISE | It is a property of the material; a higher conductivity gives a higher rate. Rest ✓. | 6.1.2.1 |
| C20 | q1 key | air has much lower thermal conductivity than glass | OK | — | 6.1.2.1 |
| C21 | q1 wx1 | "Density affects heat capacity but not thermal conductivity directly" | IMPRECISE (minor) | Loose but not false; the key point (low conductivity) is right. Usable. | — |
| C22 | q1 wx2 | transparency unrelated to conductivity | OK | — | — |
| C23 | q1 wx3 | moving air would convect; trapped air cannot, so only slow conduction | OK | — | — |
| C24 | q2 key | rate of temperature decrease; steeper = less effective | OK | — | RP2 |
| C25 | q2 wx1 | "Final temperature alone doesn't account for starting conditions or time — rate of cooling (gradient) is a fairer comparison." | **WRONG** | With the same starting temperature and the same time (both controlled in RP2), the temperature after 10 min is a fair comparison — AQA's own RP2 write-ups compare temperature drop over a fixed time. What is actually wrong with option 2 is its reasoning: a higher final temperature means a better **insulator**, not "a better conductor". The feedback teaches a false method rule and misses the real error. TC-F4. | RP2 |
| C26 | q2 wx2 | mass not the variable; thickness and type matter | OK | — | — |
| C27 | q2 wx3 | colour affects radiation, not the main factor in this test | OK | — | — |
| C28 | matching (to be replaced) | four pairs | OK | — | — |

Count: **3 WRONG** (C9 theory — re-cuttable; C17 `higher` — do not use; C25 q2 wx1 — frozen, q2 not usable as written). IMPRECISE: C3, C7, C19, C21. OFF-SPEC: C4, C10, C16. GAP: C14. ROUTE: R1 (page), spec field.

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| q1 | correct; base | Usable on all four routes once the page widens. |
| q2 | wx1 gives a false reason and misses option 2's real error | **Do not use as written.** If replaced, it is TF TH only (RP2). |
| `higher` (TH) | no HT content exists for 6.1.2.1; contains a false claim | Do not use. No higher layer on this page. |

## 5. For the lesson author
**Misconceptions seen in AQA marking**: "insulators stop heat" / "keep the cold out"; "metals feel cold because they are cold" (they conduct energy away from the hand faster); "air is a good conductor because it moves"; "thicker walls make the house warmer" without the rate idea; confusing conduction with convection in cavity walls; RP2 — not controlling starting temperature or volume, comparing final temperatures from different starts.

**Command words**: Explain (ways of reducing unwanted energy transfers), Describe (how rate of cooling of a building depends on wall thickness and conductivity), Compare; RP2 (TF TH): Plan, Identify the variable, Suggest an improvement, Use the graph.

**Required practical**: RP2 (8463 4.1.2.1, physics only) — TF TH only; Combined has no insulation RP. Base routes get the spec's suggested activity (rods of different materials) only as an optional demonstration.

## 6. Verdict
SOURCE HAS ERRORS. Three WRONG items: "electromagnetic shielding" as an energy-saving method (theory, re-cuttable), "wider double-glazing gaps are better" (`higher`, do not use) and q2's wrong-answer feedback (frozen; q2 not usable as written). q1 usable on every route. Page routes: the core is base (8464 6.1.2.1) and the page moves to CF CH TF TH under the approved route-flag PR, with RP2 as the triple layer. The spec field "6.1.3 (physics only)" is wrong — 6.1.3 is "National and global energy resources".

**For Mide:** nothing.
