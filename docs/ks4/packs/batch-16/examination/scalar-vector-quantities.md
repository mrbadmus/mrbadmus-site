# Examination — Scalar and Vector Quantities (scalar-vector-quantities) — AQA 8464 6.5.1.1 / 8463 4.5.1.1
Verdict: SOURCE OK WITH FLAGS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-16/04-checked-science-source/physics-6.5.1.1-scalar-vector-quantities.md`.
Spec sources read as text: `AQA-8464-spec.txt` (v1.1) §6.5.1.1, §6.5.1.4, §6.5.4.1.1–6.5.4.1.3; `AQA-8463-spec.txt` (v1.1) §4.5.1.1, §4.5.1.4, §4.5.6.1.1–4.5.6.1.3; June 2026 sheets 8463 and 8464/8465 (no resultant/Pythagoras equation on either). Route audit row `scalar-vector-quantities`.

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n. All four route copies identical.

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 / 8463 | **6.5.1.1 / 4.5.1.1** | Scalar and vector quantities | base |
| Supporting | 6.5.4.1.1 / 4.5.6.1.1 Distance and displacement | | base |
| Supporting | 6.5.4.1.3 / 4.5.6.1.3 Velocity — vector–scalar distinction; **(HT only)** circular motion | | base + HT bullet |
| Supporting | 6.5.1.4 / 4.5.1.4 Resultant forces — straight line base; **(HT only)** vector diagrams, "scale drawings only" | | base + HT |

Spec statements (6.5.1.1 = 4.5.1.1, verbatim): "Scalar quantities have magnitude only. Vector quantities have magnitude and an associated direction. A vector quantity may be represented by an arrow. The length of the arrow represents the magnitude, and the direction of the arrow the direction of the vector quantity."
6.5.4.1.3: "Students should be able to explain the vector–scalar distinction as it applies to displacement, distance, velocity and speed. (HT only) Students should be able to explain qualitatively, with examples, that motion in a circle involves constant speed but changing velocity."
6.5.1.4: "Students should be able to calculate the resultant of two forces that act in a straight line. … (HT only) Students should be able to use vector diagrams to illustrate resolution of forces, equilibrium situations and determine the resultant of two forces, to include both magnitude and direction (scale drawings only)."

## 2. Route table
| # | teachable point | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Scalar = magnitude only; vector = magnitude + direction (theory 1; key_note) | base | 6.5.1.1 | all four | OK |
| R2 | Lists of scalars and vectors (theory 1; key_note) | base | 6.5.1.1 (+ quantities across 6.5) | all four | OK |
| R3 | Arrow: length = magnitude, direction = direction (theory 1; key_note) | base | 6.5.1.1 | all four | OK |
| R4 | Distance vs displacement; speed vs velocity (theory 2; common_mistake; q1) | base | 6.5.4.1.1, 6.5.4.1.3 | all four | OK |
| R5 | Mass vs weight (theory 2) | base | 6.5.1.3 | all four | OK |
| R6 | Adding forces in a line (same direction add; opposite subtract) (theory 3; key_note; q2) | base | 6.5.1.4 | all four | OK |
| R7 | Forces at right angles → Pythagoras; scale drawings (theory 3; key_note; equations) | **higher** | 6.5.1.4 (HT only) | all four | ROUTE (F1) |
| R8 | Circle at constant speed → changing velocity (common_mistake) | **higher** | 6.5.4.1.3 (HT only) | all four | ROUTE (F1) |
| R9 | equations: "Resultant² = F₁² + F₂²" | higher; not a spec equation; on neither sheet | 6.5.1.4 (HT only; "scale drawings only") | all four | ROUTE / IMPRECISE (F2) |
| R10 | q1 (lap: distance vs displacement) | base | 6.5.4.1.1 | all four | OK |
| R11 | q2 (8 N right, 3 N left) | base | 6.5.1.4 | all four | OK |
| — | rp, fifas, `higher`, examiner_tip | none | — | — | `higher` absent although R7–R9 are HT — see F1 |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | theory 1 | definitions | OK | Spec wording. | 6.5.1.1 |
| C2 | theory 1 | scalars: distance, speed, mass, time, temperature, energy, power, pressure | OK | All scalars ✓. | — |
| C3 | theory 1 | vectors: displacement, velocity, force, acceleration, momentum, weight | OK | ✓ | — |
| C4 | theory 1 | 10 N right + 10 N left → net zero | OK | — | 6.5.1.4 |
| C5 | theory 1 | arrow length ∝ magnitude; direction = direction | OK | Spec: "length of the arrow represents the magnitude". | 6.5.1.1 |
| C6 | theory 2 | 3 m east then 3 m west: distance 6 m, displacement 0 m | OK | ✓ | 6.5.4.1.1 |
| C7 | theory 2 | speed 30 m/s; velocity 30 m/s north | OK | — | 6.5.4.1.3 |
| C8 | theory 2 | mass scalar (kg); weight vector (N, downward) | OK | — | 6.5.1.3 |
| C9 | theory 3 | 3 kg + 5 kg = 8 kg; 10 N + 5 N same way = 15 N; 10 N right + 5 N left = 5 N right | OK | ✓ ✓ ✓ | 6.5.1.4 |
| C10 | theory 3 | right angles: Resultant² = F₁² + F₂²; 3 N up + 4 N right → 5 N "(at an angle)" | IMPRECISE + ROUTE | Arithmetic ✓ (√25 = 5). HT only. Spec method is **scale drawing**; a vector answer needs its direction too (here 37° above the horizontal / 53° from the vertical), so "at an angle" is incomplete. Calculation by Pythagoras is normally credited by AQA as an alternative, but must not be presented as the method. | 6.5.1.4 (HT) |
| C11 | theory 3 | scale drawings for any angle | OK, ROUTE | HT. | 6.5.1.4 (HT) |
| C12 | common_mistake | speed scalar / velocity vector; distance / displacement; circle at constant speed → changing velocity | OK, ROUTE | Last sentence is HT. | 6.5.4.1.3 (HT) |
| C13 | key_note | "right angles = Pythagoras" | ROUTE | HT. | 6.5.1.4 |
| C14 | equations | "Resultant² = F₁² + F₂²" | ROUTE / IMPRECISE | Not a spec equation; not on the 8464 or 8463 June 2026 sheet. A maths tool (MS 4a/5a context), HT only. No "On the sheet"/"Learn it" chip. | sheets |
| C15 | q1 key | 400 m lap: distance 400 m, displacement 0 m | OK | ✓ | 6.5.4.1.1 |
| C16 | q1 opt 2 / wx1 | distance 0, displacement 400 → wx: net change 0; distance 400 | OK, aligned | — | — |
| C17 | q1 opt 3 / wx2 | both 400 → wx: equal only for straight-line one-way motion | OK, aligned | — | — |
| C18 | q1 opt 4 / wx3 | both zero → wx: distance never zero if moved | OK, aligned | — | — |
| C19 | q2 key | 8 N right, 3 N left → 5 N right | OK | 8 − 3 = 5 ✓ | 6.5.1.4 |
| C20 | q2 opt 2 / wx1 | 11 N → wx: opposite directions subtract | OK, aligned | — | — |
| C21 | q2 opt 3 / wx2 | 5 N left → wx: direction of the larger force | OK, aligned | — | — |
| C22 | q2 opt 4 / wx3 | zero → wx: cancel only when equal and opposite | OK, aligned | — | — |
| C23 | matching (to be replaced) | speed S, velocity V, distance S, displacement V, force V | OK | — | — |

Count: **0 WRONG**; IMPRECISE: C10, C14; ROUTE: C10–C14. Arithmetic: 5 checks ✓. No CFIFA Convert line in this file (no FIFA).

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| q1, q2 | correct, base | Usable on all four routes. |
| `equations` Resultant² = F₁² + F₂² | HT only; not a spec equation | Show only in the HT layer, as a maths check alongside a scale drawing. |

## 5. For the lesson author
**Misconceptions seen in AQA marking**: speed and velocity used interchangeably; "displacement = distance"; vectors added as plain numbers (8 + 3 = 11); mass listed as a vector, weight as a scalar; arrows drawn without regard to length; a resultant given without direction.

**Command words**: Define, Give (one scalar and one vector), Explain (the difference), Calculate (resultant in a line), Draw (HT: scale vector diagram).

**Typical questions** ⚑ examiner-drafted
- *Velocity is a vector quantity. What is a vector quantity? [1]* — has magnitude and direction.
- *Explain the difference between distance and displacement. [2]* — distance has magnitude only / is a scalar (1); displacement has magnitude and direction / is measured in a straight line from start to finish (1).
- *Two forces of 12 N and 7 N act on a box in opposite directions. Calculate the resultant force. [2]* — 5 N (1) in the direction of the 12 N force (1).

**Required practical**: none. **Equations**: none in the base spec.

## 6. Verdict
SOURCE OK WITH FLAGS. All base science and both quiz items correct and usable everywhere. Three HT points (right-angle resultant, Pythagoras equation, circular motion) are written into the base text and must become an HT layer; the spec method for the HT resultant is scale drawing.

**For Mide:** nothing.
