# Examination — Gravity (gravity) — AQA 8464 6.5.1.3 / 8463 4.5.1.3
Verdict: SOURCE OK WITH FLAGS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-16/04-checked-science-source/physics-6.5.1.3-gravity.md`.
Spec sources read as text: `AQA-8464-spec.txt` (v1.1) §6.5.1.3; `AQA-8463-spec.txt` (v1.1) §4.5.1.3, §4.8.1.3; June 2026 equation sheets 8463 (`W = m g` printed) and 8464/8465 (`W = m g` printed). Route audit row `gravity`. Mark-scheme conventions from examiner knowledge of AQA 8463/8464 papers 2018–2024; not fetched.

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n. All four route copies identical.

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 / 8463 | **6.5.1.3 / 4.5.1.3** | Gravity | base |
| Supporting | 8463 4.8.1.3 Orbital motions — gravity keeps satellites in orbit | | physics only |

Spec statements (6.5.1.3 = 4.5.1.3, verbatim): "Weight is the force acting on an object due to gravity. The force of gravity close to the Earth is due to the gravitational field around the Earth. The weight of an object depends on the gravitational field strength at the point where the object is. The weight of an object can be calculated using the equation: weight = mass × gravitational field strength W = mg [Students should be able to recall and apply this equation.] weight, W, in newtons, N; mass, m, in kilograms, kg; gravitational field strength, g, in newtons per kilogram, N/kg (In any calculation the value of the gravitational field strength (g) will be given.) The weight of an object may be considered to act at a single point referred to as the object's 'centre of mass'. The weight of an object and the mass of an object are directly proportional. [Students should recognise and be able to use the symbol for proportionality, ∝] Weight is measured using a calibrated spring-balance (a newtonmeter)." MS 3a, 3b, 3c.

Equation label: W = mg is **on the sheet** — printed on both June 2026 sheets (8464/8465 and 8463). (The spec lists it for recall; the 2026 sheet concession prints it.)

## 2. Route table
| # | teachable point | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Weight = force due to gravity; vector, downward (theory 1; key_note) | base | 6.5.1.3 | all four | OK |
| R2 | W = m × g; units N, kg, N/kg (theory 1; equations; variables; FIFA) | base | 6.5.1.3 | all four | OK |
| R3 | g = 9.8 N/kg Earth, 1.6 N/kg Moon; g = weight per kg (theory 1; key_note) | base | 6.5.1.3 ("depends on the gravitational field strength at the point") | all four | OK |
| R4 | Mass vs weight; mass constant, weight changes with location (theory 2; common_mistake; key_note; q1; q2) | base | 6.5.1.3 | all four | OK |
| R5 | Measuring: balance for mass, newtonmeter for weight (theory 2) | base | 6.5.1.3 | all four | OK / IMPRECISE (C9) |
| R6 | Gravitational field; field lines to centre; g falls with distance; ISS 8.7 N/kg (theory 3) | base (field exists) / beyond spec (field lines, g with altitude) | 6.5.1.3 | all four | OK, partly off-spec |
| R7 | Free fall in orbit; "weightlessness" (theory 3) | not in 6.5.1.3; orbit context 8463 4.8.1.3 (physics only) | 8463 4.8.1.3 | all four | OK, off-spec context |
| R8 | Centre of mass; W ∝ m and the ∝ symbol | base | 6.5.1.3 | **missing** | GAP (F2) |
| R9 | FIFA 12 kg on Earth | base | 6.5.1.3 | all four | OK |
| R10 | q1 (80 kg on the Moon) | base | 6.5.1.3 | all four | OK |
| R11 | q2 ("my weight is 60 kg") | base | 6.5.1.3 | all four | OK |
| — | rp, `higher`, examiner_tip | none | — | — | correct: 6.5.1.3 has no HT and no physics-only content |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | theory 1 | weight = force due to gravity, vector, downward | OK | — | 6.5.1.3 |
| C2 | theory 1; equations; variables | W = m × g; W in N, m in kg, g in N/kg | OK | — | 6.5.1.3 |
| C3 | theory 1 | g = 9.8 N/kg on Earth; "use 10 N/kg for estimates" | OK | Spec: g is always given in a calculation. | 6.5.1.3 |
| C4 | theory 1 | Moon g ≈ 1.6 N/kg, ~1/6 Earth's | OK | 1.62 N/kg ✓. | — |
| C5 | theory 1 | g = weight per unit mass; 1 kg → 9.8 N | OK | — | 6.5.1.3 |
| C6 | theory 2 | mass scalar kg, constant; weight vector N, changes | OK | — | 6.5.1.3 |
| C7 | theory 2 | 70 kg: Earth 686 N; Moon 112 N | OK | 70 × 9.8 = 686 ✓; 70 × 1.6 = 112 ✓ | — |
| C8 | theory 2 | "In deep space (no gravity): W = 0 N" | IMPRECISE | Gravity never falls to exactly zero. Say "far from any planet or star, g is almost zero, so W is almost zero". | 6.5.1.3 |
| C9 | theory 2 | "Mass: measured with a balance (compares gravitational force on both sides — same anywhere)" | IMPRECISE | True only of a two-pan/beam balance. A school top-pan balance measures a force and is calibrated for Earth's g; on the Moon it would read low. Say "a two-pan balance compares masses, so it reads the same anywhere". | — |
| C10 | theory 2 | weight measured with a calibrated spring balance / newtonmeter | OK | Spec wording. | 6.5.1.3 |
| C11 | theory 3 | field = region where a mass feels a force; field lines towards centre; vertical at the surface | OK | Field lines beyond spec; correct. | 6.5.1.3 |
| C12 | theory 3 | g decreases with distance; ISS (400 km) g ≈ 8.7 N/kg | OK | 9.8 × (6371/6771)² = 8.68 ✓. Beyond spec. | — |
| C13 | theory 3 | astronauts in orbit not weightless; in free fall | OK | Correct; orbit context is 8463 4.8.1.3 (physics only). Off-spec here — keep it short or cut. | 8463 4.8.1.3 |
| C14 | common_mistake | mass ≠ weight; weight in newtons not kg | OK | — | 6.5.1.3 |
| C15 | key_note | summary | OK | — | — |
| C16 | FIFA | 12 kg, g = 9.8 N/kg → W = 117.6 N | OK | 12 × 9.8 = 117.6 ✓ | 6.5.1.3 |
| C17 | CFIFA Convert `[NEW — to be examined]` | "Nothing to convert — mass is already in kg and g is already in N/kg (SI)." | OK | → examined ✓. Second worked example must convert g → kg (e.g. a 450 g apple: 0.45 kg; W = 0.45 × 9.8 = 4.41 N). | CFIFA amendment |
| C18 | q1 key | 80 kg, g_Moon 1.6 → 128 N | OK | 80 × 1.6 = 128 ✓ | — |
| C19 | q1 opt 2 / wx1 | 784 N, Earth g → wx: use the Moon's g | OK, aligned | 80 × 9.8 = 784 ✓ | — |
| C20 | q1 opt 3 / wx2 | "50 kg — mass on the Moon is 1/6 of Earth mass" → wx: mass never changes | OK, aligned; distractor IMPRECISE | wx correct. The distractor is internally inconsistent: 1/6 of 80 kg is 13.3 kg, not 50 kg. Harmless (the option is wrong anyway) but a sharp pupil will notice. | — |
| C21 | q1 opt 4 / wx3 | 0 N, weightless → wx: Moon has g = 1.6 N/kg; weightlessness is free fall in orbit | OK, aligned | — | — |
| C22 | q2 key | weight in newtons; kg measure mass; ≈ 588 N | OK | 60 × 9.8 = 588 ✓ | 6.5.1.3 |
| C23 | q2 opt 2 / wx1 | same thing → wx: different quantities | OK, aligned | — | — |
| C24 | q2 opt 3 / wx2 | grams → wx: grams measure mass | OK, aligned | — | — |
| C25 | q2 opt 4 / wx3 | correct on Moon → wx: newtons everywhere | OK, aligned | — | — |
| C26 | matching (to be replaced) | 686 N, 112 N | OK | ✓ | — |
| C27 | spec | centre of mass; W ∝ m and the ∝ symbol | GAP | Missing from the source. Both are base spec lines. | 6.5.1.3 |

Count: **0 WRONG**; IMPRECISE: C8, C9, C20 (distractor); GAP: C27. Arithmetic: 8 calculations rechecked ✓.

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| q1, q2 | correct, base | Usable on all four routes (q1 Apply, q2 Explain/Recall). |

## 5. For the lesson author
**Misconceptions seen in AQA marking**: weight given in kg; "mass changes on the Moon"; "no gravity in space" / astronauts weightless because gravity is zero; using 9.8 N/kg when another g is given; grams not converted to kg; the symbol g (field strength) confused with g (grams); weight drawn from the surface instead of from the centre of mass.

**Command words**: Write down the equation (W = mg), Calculate, Explain (why weight differs on the Moon), Name (the instrument: newtonmeter).

**Typical questions** ⚑ examiner-drafted
- *Write down the equation that links gravitational field strength, mass and weight. [1]* — W = mg (accept words).
- *A rucksack has a mass of 8.5 kg. g = 9.8 N/kg. Calculate its weight. [2]* — W = 8.5 × 9.8 (1); = 83.3 N (1).
- *A rover weighs 1800 N on Earth (g = 9.8 N/kg). Calculate its weight on Mars (g = 3.7 N/kg). [3]* — m = 1800 ÷ 9.8 = 184 kg (1); W = 184 × 3.7 (1); = 680 N (1). ← a two-equation chain; teach first (rule 3).
- *What is meant by the centre of mass of an object? [1]* — the single point at which the weight can be considered to act.

**Required practical**: none (weight–mass is commonly measured with a newtonmeter in class, not an AQA RP).

**Equations**: W = mg — On the sheet (8464 and 8463 June 2026).

## 6. Verdict
SOURCE OK WITH FLAGS. All science, all eight calculations and both quiz items correct and usable on every route. Two base spec lines are missing (centre of mass; W ∝ m with the ∝ symbol). Two imprecise theory lines (deep space "no gravity"; how a balance works). The CFIFA Convert line is correct.

**For Mide:** nothing.
