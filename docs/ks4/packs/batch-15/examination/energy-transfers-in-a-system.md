# Examination — Energy Transfers in a System (energy-transfers-in-a-system) — AQA 8463 4.1.2.1 / 8464 6.1.2.1
Verdict: SOURCE OK WITH FLAGS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-15/04-checked-science-source/physics-6.1.2.1-energy-transfers-in-a-system.md`.
Spec sources read as text: `AQA-8464-spec.txt` 6.1.2.1–6.1.2.2; `AQA-8463-spec.txt` 4.1.2.1 (incl. RP2, physics only); route audit `ks4-routes/docs/ks4/route-audit/physics.md` (thermal-conductivity → base); batch-4 `physics-6.1.2.1-thermal-conductivity.md` (sibling lesson, same spec point).

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n (= opts index n). One route copy.

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 | **6.1.2.1** | Energy transfers in a system | base |
| 8463 | **4.1.2.1** | Energy transfers in a system | base; RP2 (physics only) |
| Supporting | 8464 6.1.2.2 / 8463 4.1.2.2 Efficiency (separate lesson) | | base |

Spec statements (verbatim, 8463 = 8464): "Energy can be transferred usefully, stored or dissipated, but cannot be created or destroyed. Students should be able to describe with examples where there are energy transfers in a closed system, that there is no net change to the total energy. Students should be able to describe, with examples, how in all system changes energy is dissipated, so that it is stored in less useful ways. This energy is often described as being 'wasted'. Students should be able to explain ways of reducing unwanted energy transfers, for example through lubrication and the use of thermal insulation. The higher the thermal conductivity of a material the higher the rate of energy transfer by conduction across the material. Students should be able to describe how the rate of cooling of a building is affected by the thickness and thermal conductivity of its walls. Students do not need to know the definition of thermal conductivity." 8463 only: "Required practical activity 2 (physics only): investigate the effectiveness of different materials as thermal insulators and the factors that may affect the thermal insulation properties of a material."

**Split with the sibling lesson.** The same spec point is shared with `thermal-conductivity` (batch 4; route move to base approved). That lesson owns thermal conductivity, the wall-thickness statement and RP2 (TF TH). This lesson owns conservation, dissipation and the reduction of unwanted transfers in general (lubrication, streamlining, and insulation as one example).

## 2. Route table
| # | teachable point | true layer | spec | verdict |
|---|---|---|---|---|
| R1 | Conservation; closed system (theory 1; common_mistake; key_note) | base | 6.1.2.1 | OK |
| R2 | Examples: pendulum, bouncing ball, torch (theory 1) | base | 6.1.2.1 | OK, one imprecision (C3) |
| R3 | Dissipation, "wasted", causes, examples (theory 2) | base | 6.1.2.1 | OK, one imprecision (C6) |
| R4 | Reducing: lubrication, streamlining, insulation, better conductors (theory 3) | base | 6.1.2.1 | OK |
| R5 | Superconductors (theory 3) | — | — | OFF-SPEC (C9) |
| R6 | Wasted = input − useful (key_note) | base | 6.1.2.1 | OK |
| R7 | q1 pendulum stops | base | 6.1.2.1 | OK — usable all routes |
| R8 | q2 loft insulation | base | 6.1.2.1 ("use of thermal insulation") | OK with imprecisions — usable all routes |
| — | thermal conductivity / wall thickness / RP2 | base / triple | 6.1.2.1; 8463 RP2 | Not here, correctly; owned by thermal-conductivity |
| — | RP, `higher` | none | — | correct |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | theory 1 | cannot be created or destroyed; transferred or dissipated; closed system total constant | OK | — | 6.1.2.1 |
| C2 | theory 1 | pendulum KE ⇌ GPE (ignoring air resistance); bouncing ball lower each time | OK | — | — |
| C3 | theory 1 | "torch: chemical → electrical → light + thermal" | IMPRECISE | "Electrical" is a pathway, not a store, which contradicts energy-stores-systems' own rule. Say: chemical store → (electrically) → thermal store of the bulb and surroundings, some carried away by light. | 6.1.1.1 |
| C4 | theory 1 | energy becomes less useful as it spreads into the surroundings | OK | Spec: "stored in less useful ways". | 6.1.2.1 |
| C5 | theory 2 | dissipation = to less useful stores, usually thermal of surroundings; "wasted" | OK | — | 6.1.2.1 |
| C6 | theory 2 | causes: friction, air resistance, electrical resistance "→ heat", sound; phone charging "electrical → chemical store + thermal" | IMPRECISE (minor) | "Heat" and "electrical" again used as if they were stores. Say "→ thermal store", "electrically → chemical store". | 6.1.1.1 |
| C7 | theory 2 | filament bulb: 10 % light, 90 % thermal | OK | Order of magnitude right (≈5–10 %). | — |
| C8 | theory 3 | lubrication, streamlining, insulation (walls, double glazing, loft, cavity), lower-resistance wires | OK | Lubrication and insulation are the spec's own examples. | 6.1.2.1 |
| C9 | theory 3 | "SUPERCONDUCTORS — zero resistance at very low temperatures" | OFF-SPEC | True, but not on any AQA GCSE spec. Leave it out. | — |
| C10 | theory 3 | practical/cost limit to improvements | OK | — | — |
| C11 | common_mistake | never destroyed; "lost" energy is in the thermal store of the surroundings | OK | — | 6.1.2.1 |
| C12 | key_note | summary; wasted = total input − useful output | OK | — | 6.1.2.1 |
| C13 | q1 key | dissipated to thermal stores of air and pivot by air resistance and friction | OK | — | 6.1.2.1 |
| C14 | q1 opt 1 / wx1 | "destroyed" violates conservation | OK, aligned | — | — |
| C15 | q1 opt 2 / wx2 | no elastic PE in a pendulum at rest | OK, aligned | — | — |
| C16 | q1 opt 3 / wx3 | sound also ends as thermal energy of the air | OK, aligned | — | — |
| C17 | q2 key | slows rate of thermal transfer house → surroundings | OK | — | 6.1.2.1 |
| C18 | q2 opt 1 / wx1 | option "generates heat from solar radiation"; wx "works by reducing CONDUCTION… fibres trap air" | IMPRECISE (minor) | wx1 states the true mechanism but never says insulation does not generate energy. Acceptable. | — |
| C19 | q2 opt 2 / wx2 | option "stores thermal energy by day, releases at night"; wx "While insulation has thermal mass, this is not its primary mechanism" | IMPRECISE (minor) | Loft insulation stores very little energy, so "has thermal mass" over-concedes. The conclusion (it reduces the rate) is right. Usable. | — |
| C20 | q2 opt 3 / wx3 | reduces some convection, primarily conduction | OK, aligned | AQA mark schemes credit "trapped air reduces conduction (and convection)". | — |
| C21 | matching (to be replaced) | four cause → solution pairs | OK | — | — |
| C22 | Convert lines | none (no FIFA) | — | — | — |

Count: **0 WRONG**. **OFF-SPEC**: C9. **IMPRECISE**: C3, C6, C18, C19.

## 4. Frozen items wrong for their route
None. q1 and q2 are usable verbatim on all four routes. q2 sits on the boundary with thermal-conductivity, but "use of thermal insulation" is this spec point's own example.

## 5. For the lesson author
**Misconceptions seen in AQA marking**: "energy is lost/used up/destroyed"; "insulation keeps the cold out"; "insulation produces heat"; naming the wasted store as "heat energy" instead of the thermal store of the surroundings; "lubrication removes friction" instead of reduces it.

**Command words**: Describe (with examples), Explain (ways of reducing unwanted transfers), Give.

**Typical question** ⚑ examiner-drafted: *A cyclist freewheels down a hill and stops at the bottom without braking. Describe the energy transfers. [4]* — GPE store decreases (1), kinetic store increases (1), work done against friction and air resistance (1), energy dissipated to the thermal store of the surroundings (1).

## 6. Verdict
SOURCE OK WITH FLAGS. No arithmetic. Both quiz items usable on all routes. One off-spec aside (superconductors). Three wordings use "electrical" or "heat" as if they were stores. Thermal conductivity and RP2 correctly live in the sibling lesson.

**For Mide:** nothing.
