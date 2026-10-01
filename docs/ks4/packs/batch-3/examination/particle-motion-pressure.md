# Examination — Particle Motion in Gases (particle-motion-pressure) — AQA 8463 4.3.3.1–4.3.3.3 / 8464 6.3.3.1
Verdict: SOURCE NEEDS ROUTE SURGERY — science mostly sound; one frozen item not in spec on any route; route tags wrong
Examiner: Opus, 1 Oct 2026. Pack examined: `docs/ks4/packs/batch-3/physics-6.3.3.1-particle-motion-pressure.md`.
Spec sources fetched from filestore.aqa.org.uk and read as text: AQA-8463-SP-2016.PDF (v1.1, 30 Sep 2019) incl. Appendix A; AQA-8464-SP-2016.PDF (v1.1, 04 Oct 2019) — searched in full: 6.3.3 contains **6.3.3.1 only**. Both June 2026 equation sheets (8463; 8464/8465) downloaded and read in full. I searched the whole 8463 text for "kelvin" and "absolute zero": **no occurrence**. Mark-scheme conventions from examiner knowledge of AQA 8463/8464 papers 2018–2024; not fetched.

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n. Theory, quiz and FIFA identical on all routes; the `higher` field is present on **CH and TH** and **null on CF and TF**.

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 | **6.3.3.1** | Particle motion in gases | base |
| 8463 | **4.3.3.1** | Particle motion in gases | base |
| 8463 | **4.3.3.2** | Pressure in gases | **physics only** (no HT marker) |
| 8463 | **4.3.3.3** | Increasing the pressure of a gas | **physics only, HT only** |
| 8464 | — | no equivalent of 4.3.3.2 or 4.3.3.3 | — |

The BATCH-PLAN has no separate lesson for 8463 4.3.3.2 or 4.3.3.3, so **this lesson is their only home**: it must carry 4.3.3.2 as a `triple` layer and 4.3.3.3 as a `triple-higher` layer.

Spec statements (verbatim).
6.3.3.1 / 4.3.3.1 (identical): "The molecules of a gas are in constant random motion. The temperature of the gas is related to the average kinetic energy of the molecules. Changing the temperature of a gas, held at constant volume, changes the pressure exerted by the gas. Students should be able to: • explain how the motion of the molecules in a gas is related to both its temperature and its pressure • explain qualitatively the relation between the temperature of a gas and its pressure at constant volume."
4.3.3.2 (physics only): "A gas can be compressed or expanded by pressure changes. The pressure produces a net force at right angles to the wall of the gas container (or any surface). Students should be able to use the particle model to explain how increasing the volume in which a gas is contained, at constant temperature, can lead to a decrease in pressure. For a fixed mass of gas held at a constant temperature: pressure × volume = constant, pV = constant … Students should be able to apply this equation which is given on the Physics equation sheet. … Students should be able to calculate the change in the pressure of a gas or the volume of a gas (a fixed mass held at constant temperature) when either the pressure or volume is increased or decreased."
4.3.3.3 (physics only) (HT only): "Work is the transfer of energy by a force. Doing work on a gas increases the internal energy of the gas and can cause an increase in the temperature of the gas. Students should be able to explain how, in a given situation eg a bicycle pump, doing work on an enclosed gas leads to an increase in the temperature of the gas."

## Ruling on `findings-for-mide.md` row 8
Row 8 says: "`pV = constant`, and the pressure/temperature relation — HT-only; the p/T relation is not in AQA."

| claim in row 8 | ruling | evidence |
|---|---|---|
| pV = constant is HT-only | **Does not hold.** It is **Physics-only, base tier** (Triple Foundation and Triple Higher). | 8463 4.3.3.2 heading reads "(physics only)" with no "(HT only)"; Appendix A sheet list eq 12 "For gases: pressure × volume = constant" has **no HT mark** (eqs 1, 3, 8, 10, 11 do); the June 2026 8463 sheet prints it unmarked. Absent from 8464 and from the 8464/8465 June 2026 sheet. |
| pV = constant is Physics-only | **Holds.** | 8463 4.3.3.2; not in 8464. |
| the p/T relation is not in AQA | **Half holds.** The **qualitative** relation (raise the temperature at constant volume → pressure rises, explained by faster molecules) **is** in AQA, **base, all four routes** — 8464 6.3.3.1 and 8463 4.3.3.1 both require it. The **quantitative** law (p ÷ T = constant, p ∝ T in kelvin) and the kelvin scale **are not** in AQA physics at any tier. | 6.3.3.1 "explain qualitatively the relation between the temperature of a gas and its pressure at constant volume"; whole-text search of 8463: no "kelvin", no "absolute zero". |

So: "particle-motion-pressure, flagged BASE — the whole subtopic" is right to be base; what is wrong on the live page is (a) pV = constant taught to Combined pupils and (b) the kelvin / p ∝ T law taught to everyone.

## 2. Route table
| # | teachable point | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Gas molecules in constant random motion (theory 1) | base | 6.3.3.1 | all four | OK |
| R2 | Temperature related to average KE of molecules (theory 1; `higher`) | base | 6.3.3.1 | theory: all four; `higher`: CH, TH | Route OK in theory; **the `higher` field's restatement of it is mis-tagged** (base content) |
| R3 | Pressure caused by collisions of molecules with the walls (theory 2; key_note; q1) | base | 6.3.3.1 ("motion … related to … its pressure") | all four | OK |
| R4 | Qualitative: raise T at constant V → faster molecules → more frequent and harder collisions → higher p (theory 2; matching; q1) | base | 6.3.3.1 | all four | OK |
| R5 | Pressure produces a **net force at right angles** to the wall | **triple** | 4.3.3.2 | — | **Missing** |
| R6 | Particle explanation: larger V at constant T → less frequent collisions → lower p (theory 2; matching) | **triple** | 4.3.3.2 | all four | **WRONG ROUTE** on CF, CH — withhold from Combined |
| R7 | pV = constant; p₁V₁ = p₂V₂ calculations (theory 3; equations; FIFA; `higher`) | **triple** (base tier) | 4.3.3.2 | theory/equations/FIFA: all four; `higher`: **CH, TH** | **WRONG ROUTE twice**: shown to CF and CH (not in 8464); badged Higher, yet it is Foundation-tier Triple content — the `higher` field withholds it from **TF**, who are examined on it |
| R8 | Work done on a gas raises its internal energy and temperature (bicycle pump) | **triple-higher** | 4.3.3.3 | — (theory 3 mentions the bike pump only as a pV example) | **Missing** — and the bike-pump example as written teaches the wrong idea for 4.3.3.3 (C17) |
| R9 | Kelvin scale; K = °C + 273; absolute zero (theory 1; equations; common_mistake; key_note; `higher`; variables) | **NOT-IN-SPEC** at any tier | — | all four | Remove from teaching and from the equation card |
| R10 | p ÷ T = constant; p ∝ absolute temperature (theory 2, 3; equations; q2) | **NOT-IN-SPEC** at any tier | — | all four | Remove; q2 withheld everywhere (§4) |
| R11 | Applications: tyres, syringes, aerosols, bike pump (theory 3) | triple (as pV illustrations) | 4.3.3.2 | all four | Triple layer only; bike pump → 4.3.3.3 framing (C17) |
| — | RP | none | none | — | correct |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | theory 1 | gas molecules in constant random motion, all directions, high speeds | OK | — | 6.3.3.1 |
| C2 | theory 1 | temperature related to average KE; higher T → faster → higher average KE | OK | — | 6.3.3.1 |
| C3 | theory 1 | absolute zero 0 K = −273 °C; "minimum possible energy — minimum motion"; K = °C + 273; 0 °C = 273 K; 100 °C = 373 K; "used in gas law calculations" | OK as physics, **NOT-IN-SPEC** | Correct (−273.15 °C, rounded) but nowhere in 8463/8464. AQA never asks for kelvin in GCSE physics. Remove. | — |
| C4 | theory 2 | pressure caused by collisions of molecules with the walls; each collision a tiny force; total of many collisions | OK | Triple layer adds: "a net force at right angles to the wall" (4.3.3.2). | 6.3.3.1; 4.3.3.2 |
| C5 | theory 2 | pressure in Pa or N/m²; 1 Pa = 1 N/m² | OK | (p = F/A is 6.5 / 4.5.1 forces content.) | — |
| C6 | theory 2 | "Higher temperature → molecules move FASTER → MORE FREQUENT collisions with walls → HIGHER PRESSURE → MORE FORCEFUL collisions." | IMPRECISE | Chain out of order: "more forceful collisions" is a cause, placed after the effect. Correct chain: higher T → higher average KE → molecules move faster → collide with the walls **more often** and **with more force** → greater force on the walls → higher pressure. | 6.3.3.1 |
| C7 | theory 2 | "At constant volume: pressure is proportional to absolute temperature (Kelvin)." | NOT-IN-SPEC | Spec wants the qualitative relation only. | 6.3.3.1 |
| C8 | theory 2 | smaller V → less distance between collisions → more frequent collisions → higher p; "(Boyle's Law)" | OK — triple | Correct; 4.3.3.2 content (physics only). "Boyle's law" is not an AQA term — harmless gloss, but AQA writes "pV = constant". | 4.3.3.2 |
| C9 | theory 3 | pV = constant; doubling V halves p | OK — triple | "for a fixed mass of gas at constant temperature" must be stated every time. | 4.3.3.2 |
| C10 | theory 3 | example: 100 kPa, 2 m³ → 0.5 m³: p₂ = 400 kPa | OK — triple | 100 × 2 = 200; 200 ÷ 0.5 = 400 ✓ | 4.3.3.2 |
| C11 | theory 3 | "p ÷ T = constant (T in kelvin); double absolute temperature → double pressure" | NOT-IN-SPEC | Physically correct. Remove. | — |
| C12 | theory 3 | TYRES: "pressurised air — less volume of air compressed inside → high pressure" | IMPRECISE | Garbled. A tyre is at high pressure because a large mass of air has been pumped into a fixed volume (more molecules → more collisions per second). | — |
| C13 | theory 3 | SYRINGES: smaller volume → higher pressure | OK — triple | — | 4.3.3.2 |
| C14 | theory 3 | AEROSOLS: high-pressure gas pushes liquid out | OK | Context. | — |
| C15 | equations | "p × V = constant (Boyle's Law, constant temperature)" | OK — triple | On the 8463 sheet only. | 4.3.3.2; App. A eq 12 |
| C16 | equations | "p ÷ T = constant"; "T (K) = T (°C) + 273" | NOT-IN-SPEC | The `equations` field is kept verbatim per the architecture: keep the field, but the page's equation card shows **pV = constant only, on Triple routes only**, chip "Equation sheet". Never render the other two. | — |
| C17 | theory 3 | BIKE PUMP: "compressing air into small volume → high pressure → inflates tyre" | IMPRECISE for the spec's use of the example | AQA uses the bicycle pump for **4.3.3.3** (HT, physics only): pushing the piston does **work** on the gas, increasing its internal energy, so its **temperature rises** (the pump barrel gets warm). The pack's framing (pV) is not wrong but misses the spec point; the 4.3.3.3 point is not taught anywhere in the pack. | 4.3.3.3 |
| C18 | `higher` (CH, TH) | "Use pV = constant … in calculations. Explain changes in gas pressure using kinetic theory … Absolute zero (0 K) …" | **WRONG TAG** | pV: Triple, base tier (TF + TH), never Combined. Kinetic-theory explanation: base, all routes. Absolute zero: not in spec. | 4.3.3.2; 6.3.3.1 |
| C19 | common_mistake | "Temperature in gas law calculations MUST be in KELVIN … 0 °C = 273 K" | NOT-IN-SPEC | Remove the kelvin half. Keep "Pressure is caused by COLLISIONS of molecules with the walls … the RATE and FORCE of collisions" — exactly what AQA credits. | 6.3.3.1 |
| C20 | key_note | collisions; higher T → faster, more frequent, harder collisions; smaller V → more frequent; pV = constant; kelvin; absolute zero | partly NOT-IN-SPEC | Split: base card (first three sentences); Triple add-on (pV = constant at constant T, fixed mass); delete the kelvin/absolute-zero sentences. | — |
| C21 | variables | p Pa; V m³; T kelvin K; Ek average KE J | IMPRECISE | T "kelvin" not in spec; temperature at GCSE is in °C. V m³ matches 4.3.3.2. | 4.3.3.2 |
| C22 | FIFA | 200 kPa, 3 m³ → 1 m³ at constant T: p₂ = 600 kPa | OK — **triple only** | 200 × 3 ÷ 1 = 600 ✓. CFIFA Convert: "nothing to convert — kPa can stay kPa because the same unit appears on both sides". A second worked example with a conversion is needed (e.g. volumes in cm³ and m³ mixed, or p in kPa → Pa when a force is then asked for). | 4.3.3.2; CFIFA amendment |
| C23 | q1 key | tyre pressure rises after driving: tyre hotter → faster molecules → more frequent, harder collisions | OK | Model answer for the 6.3.3.1 qualitative relation. | 6.3.3.1 |
| C24 | q1 wx1 | air does not leak in; slow leaks go out | OK | — | — |
| C25 | q1 wx2 | tyre volume approximately constant | OK | — | — |
| C26 | q1 wx3 | molecules don't change size with temperature | OK | Named KS3 misconception — strong distractor. | — |
| C27 | q2 | 27 °C, 100 kPa heated to 327 °C at constant volume → 200 kPa (via 300 K → 600 K) | **NOT-IN-SPEC** (every route) | Physics and arithmetic correct (27 + 273 = 300; 327 + 273 = 600; ratio 2 → 200 kPa ✓). But it requires the kelvin scale and p ∝ T — neither is in 8463 or 8464 at any tier. No AQA GCSE physics paper can set it. | — |
| C28 | q2 opt 2 / wx1 | "1200 kPa — used Celsius values: 327 ÷ 27 × 100" | IMPRECISE | 327 ÷ 27 × 100 = **1211** kPa, not 1200. wx1's "≈ 12" ratio is fine. | — |
| C29 | q2 wx2, wx3 | pressure increases with temperature at constant volume | OK | (These two would be in spec as a qualitative item.) | 6.3.3.1 |
| C30 | matching (to be replaced) | 4 pairs: T↑ → p↑; V↓ → p↑; T↓ → p↓; V↑ → p↓ | OK | Pairs 2 and 4 are Triple-only (4.3.3.2). | — |

Count: **0 WRONG physics**; **1 WRONG TAG** (C18: the `higher` field); **NOT-IN-SPEC on every route**: kelvin / absolute zero / p ∝ T (C3, C7, C11, C16, C19, C21) and the whole of frozen **q2** (C27); **IMPRECISE**: C6, C12, C17, C28. **Route errors**: pV = constant and the volume explanation shown to Combined (R6, R7); pV withheld from Triple Foundation (R7). All arithmetic ✓ (5 calculations rechecked).

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| all routes · q2 · "A gas is at 27°C and 100 kPa. It is heated to 327°C at constant volume. What is the new pressure?" | Requires kelvin and p ∝ T — not in AQA 8463 or 8464 at any tier (C27). Correct physics, but no route is examined on it. | **Withhold on all four routes.** Do not put it on the ladder. (If Mide wants a stretch "beyond GCSE" box, it could live there, unscored — but the architecture has no such block, so withhold.) |
| FIFA · "A gas at 200 kPa occupies 3 m³ … compressed to 1 m³ …" | pV = constant is Physics-only (4.3.3.2). Correct for TF and TH; not in 8464. | **Withhold on CF and CH; show on TF and TH** (badge **Triple**, not Higher). |
| `higher` field (CH, TH copies) | Mis-tagged (C18). Kept verbatim as data, but it must not drive rendering. | Do not render the `higher` field as a Higher block. Its pV sentence → Triple layer (TF + TH); its kinetic-theory sentence → base; its absolute-zero sentence → drop. |
| `equations` field | Two of three equations not in spec (C16). | Keep the field; render only "pV = constant" with chip **Equation sheet**, on TF and TH only. |
| all routes · q1 · tyre pressure | Correct; base 6.3.3.1. | **Keep; usable as a rung on all four routes.** |

## 5. For the lesson author
**Misconceptions seen in AQA marking**
- "The particles get bigger / expand when heated" (q1 wx3) — the commonest KS3 carry-over.
- "Pressure rises because the particles collide with **each other** more" — AQA credits collisions **with the walls (of the container)** only.
- "More collisions" without "**per second** / more frequent" — AQA often requires the rate.
- "The particles move faster" without linking to temperature → kinetic energy, or kinetic energy → speed.
- "Particles vibrate" (for a gas — they move randomly, travelling between collisions).
- Triple: rearranging p₁V₁ = p₂V₂ upside down; forgetting "fixed mass, constant temperature".
- Triple HT: bike pump warms "because of friction" only — AQA wants "work is done on the gas, increasing its internal energy, so its temperature rises".

**Command words**: Explain (the particle model — the dominant command for this subtopic), Describe (the motion of the molecules), Calculate (Triple: pV), Suggest, Give a reason.

**Typical questions** ⚑ examiner-drafted
- *Base. Describe the motion of the molecules in a gas. [2]* — random (1); constant / continuous / in all directions at a range of speeds (1).
- *Base. A sealed container of gas is heated. The volume of the container does not change. Explain why the pressure of the gas increases. [4]* — temperature increases so the (average) kinetic energy of the molecules increases (1); molecules move faster (1); collide with the walls more often / more collisions per second (1); with more force — greater force on the walls, so pressure increases (1).
- *Triple. A fixed mass of gas at constant temperature has a volume of 0.060 m³ at 100 kPa. It is compressed to 0.024 m³. Calculate the new pressure. [3]* — 100 × 0.060 = p × 0.024 (1); p = 6.0 ÷ 0.024 (1); = 250 kPa (1).
- *Triple. Explain, in terms of particles, why increasing the volume of a gas at constant temperature decreases its pressure. [3]* — molecules travel further between collisions with the walls / spread over a larger wall area (1); collide with the walls less often / fewer collisions per second (1); the average force on the walls (per unit area) is less, so pressure decreases (1). (Temperature constant, so molecules' speed/KE unchanged — accept as part of a full answer.)
- *Triple HT. A cyclist pumps up a tyre. The pump gets warm. Explain why. [3]* — the cyclist does work on the gas / energy is transferred by the force on the piston (1); the internal energy of the gas increases (1); so the temperature of the gas increases (and energy is transferred to the pump) (1).
- *6-marker (Triple HT)* — rare for this subtopic. If set: "Explain how the pressure of the air in a bicycle pump changes as the piston is pushed in and the outlet is blocked." **L3 (5–6)**: volume decreases at constant mass; molecules collide with walls more frequently → higher pressure; work done on gas increases internal energy → temperature rises → faster molecules → harder and more frequent collisions → pressure rises further. **L2 (3–4)**: one mechanism explained fully, or both partly. **L1 (1–2)**: isolated statements. ⚑

**Required practical**: none.

**Equations**: pV = constant — **on the sheet**, **Triple only** (8463 Appendix A sheet list eq 12, no HT mark; on the June 2026 8463 sheet, unmarked; **absent** from the 8464/8465 sheet). Not on any recall list. No equation is examined for Combined in this subtopic. p ÷ T = constant and T(K) = T(°C) + 273 — **not in spec**.

## 6. Verdict
SOURCE NEEDS ROUTE SURGERY. The base particle explanation (q1, theory 1–2) is correct and is the heart of the lesson for all four routes. But the pack teaches (a) pV = constant to Combined pupils and badges it Higher while withholding it from Triple Foundation, who are examined on it; (b) the kelvin scale and p ∝ T to everyone, which AQA does not examine at any tier — and frozen q2 depends on it, so q2 must be withheld on every route; (c) nothing of 4.3.3.2's "net force at right angles" or 4.3.3.3's work-done-on-a-gas (Triple HT), although this lesson is their only home.

**For Mide:** none needing a ruling — the spec text settles all of it. For information: `findings-for-mide.md` row 8 is half right. pV = constant is Physics-only but **not HT** (base-tier Triple); the qualitative p–T relation **is** AQA base content on all four routes; only the quantitative p/T law and kelvin are outside AQA. Suggest annotating row 8 as row 3 was annotated.
