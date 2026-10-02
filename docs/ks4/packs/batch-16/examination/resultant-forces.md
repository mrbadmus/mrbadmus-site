# Examination — Resultant Forces (resultant-forces) — AQA 8464 6.5.1.4 / 8463 4.5.1.4
Verdict: SOURCE OK WITH FLAGS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-16/04-checked-science-source/physics-6.5.1.4-resultant-forces.md`.
Spec sources read as text: `AQA-8464-spec.txt` (v1.1, 04 Oct 2019) 6.5.1.4, 6.5.4.1.3, 6.5.4.1.5, 6.5.4.2.1; `AQA-8463-spec.txt` (v1.1, 30 Sep 2019) 4.5.1.4 (identical wording), 4.5.6.1.5, 4.5.6.2.1. Equation sheets: none needed (no equation in this lesson). Route audit read: `ks4-routes/docs/ks4/route-audit/physics.md` rows `resultant-forces`, `resolving-forces`, `free-body-diagrams`.

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n; th1–th3 = theory chunks. Route copies identical except `higher` (TH text on CH/TH; `null` on CF/TF).

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 | **6.5.1.4** | Resultant forces | base (first two sentences); rest **(HT only)** |
| 8463 | **4.5.1.4** | Resultant forces | same split, identical wording |
| Supporting | 8464 6.5.4.2.1 / 8463 4.5.6.2.1 Newton's First Law | | base |
| Supporting | 8464 6.5.4.1.5 / 8463 4.5.6.1.5 terminal velocity ("An object falling through a fluid initially accelerates… Eventually the resultant force will be zero and the object will move at its terminal velocity.") | | base |
| Supporting | 8464 6.5.4.1.3 / 8463 4.5.6.1.3 "(HT only) …motion in a circle involves constant speed but changing velocity" | | higher |

Spec statements (verbatim, 8464 = 8463):
- "A number of forces acting on an object may be replaced by a single force that has the same effect as all the original forces acting together. This single force is called the resultant force."
- "Students should be able to calculate the resultant of two forces that act in a straight line."
- "(HT only) Students should be able to: • describe examples of the forces acting on an isolated object or system • use free body diagrams to describe qualitatively examples where several forces lead to a resultant force on an object, including balanced forces when the resultant force is zero."
- "(HT only) A single force can be resolved into two components acting at right angles to each other…"
- "(HT only) Students should be able to use vector diagrams to illustrate resolution of forces, equilibrium situations and determine the resultant of two forces, to include both magnitude and direction (scale drawings only)."

## 2. Route table
| # | teachable point (pack location) | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Resultant = single force with the same effect (th1; key_note) | base | 6.5.1.4 | all four | OK |
| R2 | Same direction add; opposite subtract, direction of larger (th1) | base | 6.5.1.4 | all four | OK |
| R3 | Forces at right angles: Pythagoras / trigonometry / scale drawing (th1) | higher (scale drawing only); Pythagoras/trig off-spec | 6.5.1.4 (HT only) | all four | ROUTE + OFF-SPEC (F1) |
| R4 | Zero resultant → stationary or constant velocity; Newton's First Law (th1; common_mistake; key_note; q1) | base | 6.5.4.2.1 | all four | OK |
| R5 | Non-zero resultant → acceleration (change of speed or direction) (th1, th3) | base | 6.5.4.2.1 | all four | OK |
| R6 | Free body diagrams (th2; key_note) | higher | 6.5.1.4 (HT only) | all four | ROUTE (F2) |
| R7 | Resultant along / against / perpendicular to motion (th3) | base (along/against); higher (perpendicular → circle) | 6.5.4.2.1; 6.5.4.1.3 (HT only) | all four | OK; perpendicular line is HT (F2) |
| R8 | Scale drawing head-to-tail for a resultant (th3) | higher | 6.5.1.4 (HT only) | all four | ROUTE (F2) |
| R9 | Terminal velocity: air resistance = weight (th3; key_note; q2) | base | 6.5.4.1.5 | all four | OK |
| R10 | `higher`: resolve into components, vector addition at angles | higher | 6.5.1.4 (HT only) | CH TH | OK (scale drawing only — F1) |
| R11 | `higher`: forces in a circle, centripetal force towards centre; changing velocity | higher | 6.5.4.1.3 (HT only) | CH TH | IMPRECISE (F3) |
| R12 | q1 constant speed → balanced | base | 6.5.4.2.1 | all four | OK |
| R13 | q2 terminal velocity | base | 6.5.4.1.5 | all four | OK |
| — | equations, fifas, rp | none | — | — | correct: no equation and no RP in 6.5.1.4 |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | th1 | multiple forces replaced by single resultant with same effect | OK | spec wording | 6.5.1.4 |
| C2 | th1 | same direction add; opposite subtract, direction of larger | OK | — | 6.5.1.4 |
| C3 | th1 | "FORCES AT RIGHT ANGLES: use Pythagoras; direction from trigonometry or scale drawing" | OFF-SPEC / ROUTE | Resultant of two non-collinear forces is HT and "scale drawings only". Pythagoras and trigonometry are not required by AQA. Base pages: straight-line resultants only. | 6.5.1.4 |
| C4 | th1 | resultant 0 → at rest or constant velocity; "This is Newton's First Law" | OK | — | 6.5.4.2.1 |
| C5 | th1 | resultant ≠ 0 → accelerates (changes speed or direction) | OK | — | 6.5.4.2.1 |
| C6 | th2 | FBD: arrows, length ∝ magnitude, object as box/dot | OK (HT) | — | 6.5.1.4 (HT only); 6.5.1.1 |
| C7 | th2 | book: normal contact up, weight down, resultant 0 | OK | — | — |
| C8 | th2 | car accelerating: driving > friction + air resistance | OK | — | — |
| C9 | th2 | skydiver before terminal velocity: weight > air resistance, accelerates down | OK | — | 6.5.4.1.5 |
| C10 | th3 | equilibrium = zero resultant | OK | — | 6.5.1.4 |
| C11 | th3 | resultant along motion speeds up; against slows down; perpendicular changes direction | OK | perpendicular case is the HT circle idea | 6.5.4.1.3 (HT only) |
| C12 | th3 | scale drawing: head-to-tail, measure with ruler × scale, protractor | OK (HT) | — | 6.5.1.4 (HT only) |
| C13 | th3 | terminal velocity: air resistance rises with speed until = weight | OK | — | 6.5.4.1.5 |
| C14 | th3 | skydiver terminal velocity ≈ 55 m/s (120 mph) | OK | 55 m/s ≈ 123 mph; typical belly-down value 50–60 m/s | — |
| C15 | `higher` | "centripetal force is always directed towards the centre" | IMPRECISE | AQA does not use "centripetal force"; 8464/8463 require only "explain qualitatively… motion in a circle involves constant speed but changing velocity". Circle content belongs on `motion-in-a-circle`. | 6.5.4.1.3 (HT only) |
| C16 | `higher` | object in circle at constant speed has changing velocity → accelerating | OK | — | 6.5.4.1.3 (HT only) |
| C17 | `higher` | omits free body diagrams | GAP | FBD is HT in 6.5.1.4; covered by the `free-body-diagrams` page | 6.5.1.4 |
| C18 | common_mistake | zero resultant ≠ stationary; constant velocity includes stationary | OK | — | 6.5.4.2.1 |
| C19 | key_note | as th1–th3; "Free body diagrams" | OK | FBD clause is HT (F2) | — |
| C20 | q1 key | constant speed straight road → resultant 0 | OK | — | 6.5.4.2.1 ("when a vehicle travels at a steady speed the resistive forces balance the driving force") |
| C21 | q1 wx1 | aligned to opt 1 (no forces) | OK | — | — |
| C22 | q1 wx2 | aligned to opt 2 (driving > resistive) | OK | — | — |
| C23 | q1 wx3 | aligned to opt 3 (slowing down) | OK | — | — |
| C24 | q2 key | air resistance increases until = weight, resultant 0, acceleration stops | OK | — | 6.5.4.1.5 |
| C25 | q2 wx1 | aligned to opt 1 (runs out of energy) | OK | — | — |
| C26 | q2 wx2 | aligned to opt 2 (gravity decreases); "weight stays approximately constant" | OK | — | — |
| C27 | q2 wx3 | aligned to opt 3 (constant acceleration) | OK | — | — |
| C28 | matching (to be replaced) | four pairs | OK | — | — |

Count: **0 WRONG**; OFF-SPEC 1 (C3); ROUTE 1 (F2: FBD/scale-drawing/perpendicular content sits on base without an HT label); IMPRECISE 1 (C15). wrong_explanations: all 6 read and aligned.

## 4. Frozen items wrong for their route
None. q1 and q2 are base and usable on all four routes.

## 5. Calculations (rule 3)
Only "resultant of two forces in a straight line" (add / subtract). No equation, no unit conversion, **no chained calculation**. HT layer: resultant of two non-parallel forces by scale drawing (scale conversion N ↔ cm is the only "Convert").

## 6. Verdict
SOURCE OK WITH FLAGS. All base science correct; both quiz items usable on all routes. The page mixes HT content (FBDs, scale drawing, circle) into base theory without labels, and offers Pythagoras/trigonometry where AQA says "scale drawings only". No Mide call.
