# Examination — Internal energy (internal-energy) — AQA 8463 4.3.2.1 / 8464 6.3.2.1
Verdict: SOURCE OK WITH FLAGS
Examiner: Opus, 1 Oct 2026. Pack examined: `docs/ks4/packs/batch-2/physics-6.3.2.1-internal-energy.md`.
Spec sources fetched from filestore.aqa.org.uk and read as text: AQA-8463-SP-2016.PDF (v1.1, 30 Sep 2019) incl. Appendix A, AQA-8464-SP-2016.PDF (v1.1, 04 Oct 2019). Mark-scheme conventions from examiner knowledge of AQA 8463/8464 papers 2018–2024.

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n. All route copies identical.

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 | **6.3.2.1** | Internal energy | base |
| 8463 | **4.3.2.1** | Internal energy | base |
| Supporting (referenced by the pack) | 8463 4.3.2.2 / 8464 6.3.2.2 Temperature changes in a system and specific heat capacity; 4.3.2.3 / 6.3.2.3 Changes of state and specific latent heat (heating/cooling graphs); 4.3.3.1 / 6.3.3.1 Particle motion in gases (temperature ↔ average KE) — all base | | |

Spec statement (verbatim, 8463 = 8464): "Energy is stored inside a system by the particles (atoms and molecules) that make up the system. This is called internal energy. Internal energy is the total kinetic energy and potential energy of all the particles (atoms and molecules) that make up a system. Heating changes the energy stored within the system by increasing the energy of the particles that make up the system. This either raises the temperature of the system or produces a change of state."
4.3.2.3: "When a change of state occurs, the energy supplied changes the energy stored (internal energy) but not the temperature. … Students should be able to interpret heating and cooling graphs that include changes of state. Students should be able to distinguish between specific heat capacity and specific latent heat."
4.3.3.1: "The temperature of the gas is related to the average kinetic energy of the molecules."

## 2. Route table
| # | teachable point | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Internal energy = total KE + PE of all particles (theory 1; key_note; matching) | base | 4.3.2.1 | all four | OK |
| R2 | Heating raises temperature **or** changes state (theory 1, 3; q1) | base | 4.3.2.1 | all four | OK |
| R3 | Temperature constant during change of state; flat sections on heating/cooling curves (theory 3; common_mistake; q1) | base | 4.3.2.3 | all four | OK |
| R4 | Temperature ↔ average KE of particles (theory 2; key_note) | base | 4.3.3.1 (stated for gases) | all four | OK — spec says "related to", stated for gases |
| R5 | Bigger mass → more internal energy at lower temperature (lake/pool vs tea) (theory 2; q2) | base | 4.3.2.1 (total of all particles) | all four | OK |
| R6 | ΔE = mcΔθ and E = mL named (theory 3) | base | 4.3.2.2, 4.3.2.3 (both **on the sheet**) | all four | OK as signposts; taught in `temperature-changes-shc` and `specific-latent-heat` (batch 3) |
| R7 | "Thermal energy" as a distinct quantity; "extensive property" (theory 2; q2 wx3) | NOT-IN-SPEC / imprecise | — | all four | Re-cut (C9) |
| — | RP, FIFA, equations field, examiner tip | none in pack | — | — | correct: no RP for 4.3.2.1 (the SHC RP is 8464 RP14 / 8463 RP1, in 6.1.1.3 / 4.1.1.3) |

No HT or physics-only content.

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | theory 1 | "INTERNAL ENERGY is the total kinetic energy and potential energy of all the particles in a system" | OK | Verbatim spec definition. | 4.3.2.1 |
| C2 | theory 1 | KE "from their random motion (vibration, translation, rotation)" | OK | — | — |
| C3 | theory 1 | PE "stored in the bonds and intermolecular forces between them" | IMPRECISE | At GCSE, the particles' potential energy is energy due to the **forces between particles / their separation**. Saying it is "stored in the bonds" invites the chemistry error that melting/boiling breaks covalent bonds. Say "potential energy due to the forces between the particles". | 4.3.2.1; cf. chemistry 8464 5.2.2.4 (small molecules: intermolecular forces, not covalent bonds, are overcome) |
| C4 | theory 1 | change of state: "particles gain enough PE to overcome intermolecular forces (**bonds break/form**)" | IMPRECISE | "Bonds break/form" is ambiguous and, for molecular substances, wrong if read as covalent bonds. Also "gain PE to overcome forces" reverses cause: energy supplied does work against the forces, so PE increases. Say: "the energy supplied is used to overcome the forces between particles, so their potential energy increases". | 4.3.2.3 |
| C5 | theory 1 | "Both effects cannot happen simultaneously for a pure substance at its melting or boiling point — during a change of state, temperature stays constant" | OK | — | 4.3.2.3 |
| C6 | theory 2 | "TEMPERATURE is a measure of the AVERAGE KINETIC ENERGY of the particles" | OK (beyond-spec wording) | Spec: temperature of a gas "is related to the average kinetic energy". AQA credits "temperature depends on / is related to average KE". | 4.3.3.1 |
| C7 | theory 2 | different materials at the same temperature have different internal energies (number of particles, PE) | OK | — | 4.3.2.1 |
| C8 | theory 2 | "TEMPERATURE (°C or K)" | OK | Kelvin is not required in 8463/8464 for this section (it appears in neither spec's content for 4.3.2); harmless. | — |
| C9 | theory 2 | "THERMAL ENERGY (J) — total energy transferred — depends on temperature difference AND mass AND specific heat capacity." | **IMPRECISE (borderline WRONG)** | Conflates two things. AQA's term in ΔE = mcΔθ is "**change in** thermal energy" — the energy needed for a temperature *change*. It is not "total energy" and it is not a property alongside internal energy. As written, a pupil learns "internal energy depends on temperature × mass × c" (see q2 wx2). Replace with: "Energy transferred when the temperature changes: ΔE = m c Δθ (on the sheet)." | 4.3.2.2 |
| C10 | theory 2 | lake vs tea: tea hotter; lake far more internal energy | OK | — | 4.3.2.1 |
| C11 | theory 3 | temperature rise: KE increases; calculated by ΔE = mcΔθ | OK | On the sheet. | 4.3.2.2 |
| C12 | theory 3 | change of state: temperature constant; energy increases PE; "breaking intermolecular bonds"; E = mL | IMPRECISE | "Intermolecular bonds" — see C3/C4; say "forces". E = mL on the sheet. | 4.3.2.3 |
| C13 | theory 3 | heating curve: sloping = temperature rising; flat = change of state at melting / boiling point; cooling curve reverse | OK | — | 4.3.2.3 |
| C14 | common_mistake | constant temperature during change of state; "energy goes into potential energy (breaking bonds)" | OK / IMPRECISE ("breaking bonds") | As C4. | 4.3.2.3 |
| C15 | key_note | KE + PE; raises T or changes state; T = average KE; flat = change of state | OK | — | 4.3.2.1, 4.3.2.3 |
| C16 | matching (to be replaced) | 4 pairs; "energy increasing PE (breaking bonds)" | OK / IMPRECISE | As C4. | — |
| C17 | q1 key | constant temperature at constant power = change of state; PE increases | OK | — | 4.3.2.3 |
| C18 | q1 wx1 | "If no energy were being supplied, temperature would fall (cool to room temperature)" | OK (minor) | Only if above room temperature; fine in context. | — |
| C19 | q1 wx2 | "no maximum temperature concept for most substances" | OK | — | — |
| C20 | q1 wx3 | heat loss can cause plateaus, but "in exam context a flat section on a heating curve always indicates a change of state" | OK, honest | Option 4 describes a physically real steady state; the explanation concedes it. Keyed answer is the best answer for AQA. The stem would be cleaner with "…at 0 °C" or "…at its melting point", but the item is frozen. | 4.3.2.3 |
| C21 | q2 key | pool: lower temperature, far more particles, greater total KE + PE | OK | — | 4.3.2.1 |
| C22 | q2 wx1 | higher temperature = higher average KE, but internal energy is total | OK | — | 4.3.2.1 |
| C23 | q2 wx2 | "Internal energy depends on temperature, mass AND specific heat capacity — not temperature alone." | IMPRECISE | Specific heat capacity relates a **change** in internal energy to a change in temperature; it is not what internal energy "depends on". Correct statement: "Internal energy depends on the number of particles (the mass) and the material and state, not on temperature alone." Not route-wrong. | 4.3.2.1, 4.3.2.2 |
| C24 | q2 wx3 | "internal energy is an EXTENSIVE property — it scales with the amount of matter" | OK science, NOT-IN-SPEC term | "Extensive" is university vocabulary; the idea (more matter, more internal energy) is right. | — |

Count: **0 WRONG** in frozen items; **1 borderline WRONG** theory sentence (C9, re-cuttable); **IMPRECISE**: C3, C4, C12, C14, C16 (all one fault: "bonds" for forces between particles), C23 (frozen). No arithmetic in the pack.

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| all routes · q2 wx2 · "Internal energy depends on temperature, mass AND specific heat capacity…" | Imprecise (C23); not route-wrong. | Keep verbatim; q2 is a good rung on all four routes. The lesson body must not echo "internal energy depends on SHC". Optional generated-copy ruling: "Internal energy depends on how many particles there are (the mass) and what they are, not on temperature alone." |
| all routes · q1 · "A substance is heated at constant power. Its temperature stays constant…" | Correct; option 4 is physically possible but the explanation handles it. | Keep; usable as a rung on all routes. |
| No item is wrong for its route. | | |

## 5. For the lesson author
**Misconceptions seen in AQA marking**
- "Temperature and internal energy are the same thing" / "hotter object has more internal energy" (q2's target).
- "Heating always raises the temperature" (q1's target).
- "Particles get bigger / expand" when heated; "particles melt".
- Change of state "breaks the bonds in the molecules" (covalent bonds) — chemistry examiners reject this; physics examiners credit "forces between particles overcome" / "potential energy increases".
- Internal energy = kinetic energy only (PE omitted: the definition mark is lost without "and potential energy").
- "Total energy of the particles" without "kinetic and potential" — loses the mark.
- Plateau read as "the heater was switched off".

**Command words**: Define / What is meant by (internal energy), Describe, Explain (why temperature stays constant), Use the graph / Determine (melting point from a cooling curve), Compare.

**Typical questions** ⚑ examiner-drafted
- *What is meant by the internal energy of a system? [2]* — total kinetic energy and potential energy (1) of all the particles (atoms/molecules) in the system (1).
- *A cooling curve for stearic acid shows a flat section at 69 °C. Explain why the temperature stays constant. [3]* — the substance is changing state / freezing (1); energy is being transferred to the surroundings (1); internal energy decreases but this is a decrease in potential energy (forces between particles / bonds forming between particles), not kinetic energy, so temperature does not change (1). (Accept "latent heat released".)
- *Explain why a bath of warm water has more internal energy than a cup of hot water. [2]* — the bath has (many) more particles / greater mass (1); internal energy is the total KE + PE of all particles, so the total is greater even though the average KE is lower (1).
- 6-mark (levels of response; usually spans 4.3.2.1–4.3.2.3): *Describe what happens to the particles and the internal energy as ice at −10 °C is heated until it becomes water at 20 °C.* L3 (5–6): ice warms — particle KE (vibration) increases, temperature rises; at 0 °C temperature constant while melting, energy increases PE / overcomes forces between particles; water warms — KE increases; internal energy increases throughout; L2 (3–4): correct sequence with some particle explanation; L1 (1–2): some stages described. ⚑ examiner-drafted.

**Required practical**: none for 4.3.2.1. (Related: 8464 RP14 / 8463 RP1 specific heat capacity, lesson `temperature-changes-shc`. The latent-heat-of-fusion experiment is an AT 5 opportunity, not an RP.)

**Equations**: none to calculate in this lesson. Signposted: ΔE = m c Δθ — **on the sheet**; E = m L — **on the sheet**.

## 6. Verdict
SOURCE OK WITH FLAGS. Definitions match the spec verbatim; no wrong keyed answer. One recurring imprecision (potential energy "in the bonds" / "breaking intermolecular bonds") and one confusing "thermal energy" paragraph to fix in the re-cut; q2 wx2 is imprecise but usable.

**For Mide:** none. (8463 4.3.2.1 and 8464 6.3.2.1 are identical.)
