# Examination — Energy Transfers in Everyday Appliances (energy-transfers-appliances) — AQA 8464 6.2.4.2 / 8463 4.2.4.2
Verdict: SOURCE OK WITH FLAGS (kilowatt-hours and cost are beyond the spec, so q1 is not usable; E = QV is missing from the frozen data)
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-15/04-checked-science-source/physics-6.2.4.2-energy-transfers-appliances.md`.
Spec sources read: `AQA-8464-spec.txt` §6.2.4.2, §6.1.2.2 (efficiency); `AQA-8463-spec.txt` §4.2.4.2. Both June 2026 equation sheets. A text search of both spec files for "kilowatt" and "kWh" returns nothing; neither sheet prints a kWh equation. Route audit row `energy-transfers-appliances` (base / base).

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n (option 0 is the key on both). All four route copies identical.

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 | **6.2.4.2** | Energy transfers in everyday appliances | base |
| 8463 | **4.2.4.2** | Energy transfers in everyday appliances | base |
| Supporting | 8464 6.2.4.1 / 8463 4.2.4.1 (P = VI); 6.2.1.2 / 4.2.1.2 (Q = It) | | base |

Spec statements (verbatim, 8463 = 8464): "Everyday electrical appliances are designed to bring about energy transfers. The amount of energy an appliance transfers depends on how long the appliance is switched on for and the power of the appliance. Students should be able to describe how different domestic appliances transfer energy from batteries or ac mains to the kinetic energy of electric motors or the energy of heating devices. Work is done when charge flows in a circuit. The amount of energy transferred by electrical work can be calculated using the equation: energy transferred = power × time  E = P t; energy transferred = charge flow × potential difference  E = Q V" — "Students should be able to recall and apply both equations." Units J, W, s, C, V. "Students should be able to explain how the power of a circuit device is related to: • the potential difference across it and the current through it • the energy transferred over a given time. Students should be able to describe, with examples, the relationship between the power ratings for domestic electrical appliances and the changes in stored energy when they are in use."

Equation sheets (June 2026): E = P t and E = Q V printed on **both** sheets → "On the sheet" on all four routes. "Energy (kWh) = Power (kW) × time (h)" is on **neither** sheet and not in either spec.

## 2. Route table
| # | teachable point | true layer | spec | verdict |
|---|---|---|---|---|
| R1 | appliances transfer energy: motor → kinetic; heater → thermal; lamp, speaker, charger (theory 1; key_note) | base | 6.2.4.2 | IMPRECISE wording (ETA-F2) |
| R2 | "no appliance is 100% efficient" (theory 1) | base (6.1.2.2) | 6.1.2.2 | IMPRECISE (ETA-F3) |
| R3 | E = Pt, t in seconds; 2 kW × 3 min (theory 2; equations; common_mistake; FIFA) | base | 6.2.4.2 | OK |
| R4 | kWh, 1 kWh = 3.6 MJ, cost, kWh comparisons (theory 2–3; equations; key_note; q1) | none — beyond spec | — | OFF-SPEC (ETA-F1) |
| R5 | energy depends on power AND time; fridge vs kettle (theory 3; common_mistake; q2) | base | 6.2.4.2 | OK |
| R6 | reducing energy use (theory 3) | base context | 6.1.2.2 | OK |
| R7 | E = QV; "work is done when charge flows" | base | 6.2.4.2 | **GAP** — absent from this file (ETA-F4) |
| R8 | q1 | beyond spec | — | not usable (ETA-F1) |
| R9 | q2 | base | 6.2.4.2 | OK, usable all routes |
| — | RP, `higher` | none | — | correct |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | theory 1 | "Every electrical appliance transfers energy from the electrical store" | IMPRECISE | AQA's model has no "electrical store": energy is transferred **electrically** (work done when charge flows) from the chemical store of a battery or from the ac mains. | 6.2.4.2 |
| C2 | theory 1 | motor → kinetic + thermal; heater → thermal; lamp → light + thermal; speaker → sound; charger → chemical | OK / IMPRECISE | Destinations right for motor, heater, charger (kinetic store, thermal store, chemical store). Light and sound are ways energy is transferred (pathways), ending in the thermal store of the surroundings. | 6.2.4.2 |
| C3 | theory 1 | "All appliances dissipate some energy as thermal — no appliance is 100% efficient." | IMPRECISE | An electric heater's useful output IS the thermal store, so it is (very nearly) 100% efficient. Say "most appliances waste some energy by heating". | 6.1.2.2 |
| C4 | theory 2; equations; variables | E = P × t; J, W, s | OK | — | 6.2.4.2 |
| C5 | theory 2 | 2 kW for 3 min → 2000 × 180 = 360,000 J | OK | ✓ | — |
| C6 | theory 2 | kWh = kW × h; 1 kWh = 3,600,000 J; 3 kW × 0.5 h = 1.5 kWh | OK / OFF-SPEC | All ✓; beyond spec. | — |
| C7 | theory 3 | cost = kWh × price; 1.5 × 30p = 45p | OK / OFF-SPEC | ✓; beyond spec. | — |
| C8 | theory 3 | fridge 200 W × 24 h = 4.8 kWh; kettle 2 kW × 5 min ≈ 0.17 kWh | OK | 0.2 × 24 = 4.8 ✓; 2 × 5/60 = 0.167 ✓. The principle is spec. ("Runs continuously" is idealised; a fridge compressor cycles.) | 6.2.4.2 |
| C9 | theory 3 | LED bulbs, shorter use, insulation | OK | — | 6.1.2.2 |
| C10 | common_mistake | t in s for J; kW and h for kWh; high power briefly can use less than low power for hours | OK / OFF-SPEC | kWh half beyond spec. | 6.2.4.2 |
| C11 | key_note | E = Pt; kWh = kW × h; 1 kWh = 3.6 MJ; cost; appliance list | OK / OFF-SPEC | — | — |
| C12 | FIFA | 1.5 kW, 4 min → 1500 × 240 = 360,000 J | OK | ✓ | 6.2.4.2 |
| C13 | CFIFA Convert `[NEW]` | "TWO conversions: kW → W (1.5 kW = 1500 W) and minutes → seconds (4 min = 4 × 60 = 240 s) — both needed before E = Pt gives joules." | OK | Examined ✓. | CFIFA amendment |
| C14 | q1 key | 2 kW × 3 h = 6 kWh; 6 × 25p = £1.50 | OK / OFF-SPEC | Arithmetic ✓; the item tests kWh and cost. | — |
| C15 | q1 opt 2 / wx1 | 6000 kWh / "Must use KILOWATTS" | OK | Aligned. | — |
| C16 | q1 opt 3 / wx2 | 0.67 kWh / "Must multiply" | OK | Aligned; 2 ÷ 3 = 0.67 ✓ | — |
| C17 | q1 opt 4 / wx3 | "6 kWh and 25p" / "Cost = energy × price per unit" | OK | Aligned. | — |
| C18 | q2 key | fridge 4.8 kWh vs kettle ≈ 0.17 kWh | OK | Tests the spec principle (power and time); kWh only appears as working. | 6.2.4.2 |
| C19 | q2 opt 2 / wx1 | "kettle — higher power" / "Higher power ≠ higher energy use" | OK | Aligned. | 6.2.4.2 |
| C20 | q2 opt 3 / wx2 | "the same" / "Fridge: 4.8 kWh. Kettle: 0.17 kWh" | OK | Aligned. | — |
| C21 | q2 opt 4 / wx3 | "brands" / "Power and time are all that's needed" | OK | Aligned. | — |
| C22 | matching (to be replaced) | "Speaker — Sound — kinetic energy of vibrating air" | OK | — | — |
| C23 | coverage | E = QV; "work is done when charge flows" | GAP | Spec core of this section, recall-and-apply; only appears in `power-electricity`'s file. Added to the source file. | 6.2.4.2 |

Count: **0 WRONG**. OFF-SPEC: kWh and cost (C6, C7, C14). IMPRECISE: C1, C2, C3. GAP: C23. All arithmetic ✓ (10 calculations rechecked).

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| q1 | correct arithmetic, but tests kWh and cost — not on 8463/8464 | Not usable as a rung. |
| q2 | tests the spec principle | Usable on all four routes. |

## 5. For the lesson author
**Misconceptions seen in AQA marking:** minutes or hours left in E = Pt; kW left unconverted; "the most powerful appliance always uses the most energy"; "energy is used up" (it is transferred, then dissipated); E = Q ÷ V; mixing charge (C) and current (A).

**Typical questions** ⚑ examiner-drafted
- *Write down the equation that links energy transferred, power and time. [1]* — E = Pt.
- *A 2.5 kW kettle is on for 2 minutes. Calculate the energy transferred. [3]* — 2500 W and 120 s (1); 2500 × 120 (1); 300,000 J (1).
- *A charge of 40 C flows through a lamp with a pd of 6.0 V. Calculate the energy transferred. [2]* — 40 × 6.0 (1); 240 J (1).
- *A 12 V motor draws 2.0 A for 30 s. Calculate the energy transferred. [3]* — Step 1 Q = 2.0 × 30 = 60 C (or P = 12 × 2.0 = 24 W) (1); Step 2 E = 60 × 12 (or 24 × 30) (1); 720 J (1).

## 6. Verdict
SOURCE OK WITH FLAGS. E = Pt and every number correct. kWh and cost are beyond the spec (q1 not usable). E = QV, half the section's equations, is missing from the frozen data and has been added from the spec. Theory 1's energy language needs AQA's store/pathway wording. Nothing for Mide.
