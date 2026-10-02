# Examination — Resolving Forces and Vector Diagrams (resolving-forces) — AQA 8464 6.5.1.4 (HT only) / 8463 4.5.1.4 (HT only)
Verdict: SOURCE HAS ERRORS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-16/04-checked-science-source/physics-6.5.1-resolving-forces.md`.
Spec sources read as text: `AQA-8464-spec.txt` (v1.1, 04 Oct 2019) 6.5.1.4; `AQA-8463-spec.txt` (v1.1, 30 Sep 2019) 4.5.1.4 (identical wording). Neither June 2026 equation sheet prints any resolving equation (none exists on the spec). Route audit read: `ks4-routes/docs/ks4/route-audit/physics.md` row `resolving-forces` and note 2.

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n; th1–th3 = theory chunks. Site's "6.5.1 (HT only)" is its internal number; true refs are 8464 **6.5.1.4** and 8463 **4.5.1.4**, both (HT only). Single route copy (TH).

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 | **6.5.1.4** | Resultant forces | **(HT only)** for resolution / vector diagrams |
| 8463 | **4.5.1.4** | Resultant forces | **(HT only)**, identical wording |
| Supporting | 8464 6.5.1.1 / 8463 4.5.1.1 vectors as arrows | | base |

Spec statements (verbatim, 8464 = 8463):
- "(HT only) A single force can be resolved into two components acting at right angles to each other. The two component forces together have the same effect as the single force."
- "(HT only) Students should be able to use vector diagrams to illustrate resolution of forces, equilibrium situations and determine the resultant of two forces, to include both magnitude and direction (scale drawings only)." — skills MS 4a, 5a, b.

There is no equation in this spec point. "Scale drawings only" excludes trigonometry (F cos θ, F sin θ), Pythagoras and arctan as required methods.

## 2. Route table
| # | teachable point (pack location) | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | A force resolves into two perpendicular components with the same effect (th1) | higher | 6.5.1.4 (HT only) | TH | OK — ROUTE: should be CH TH |
| R2 | Fx = F cos θ, Fy = F sin θ; 50 N at 37° example (th1; equations; key_note; common_mistake; variables) | off-spec | — | TH | OFF-SPEC (F1) |
| R3 | Scale drawing tip-to-tail (th2 Method 1) | higher | 6.5.1.4 (HT only) | TH | OK |
| R4 | Parallelogram of forces (th2 Method 2) | higher | 6.5.1.4 (HT only) | TH | OK (a vector diagram) |
| R5 | Component method, R = √(ΣFx² + ΣFy²), arctan (th2 Method 3; equations; FIFA) | off-spec | — | TH | OFF-SPEC (F1, F2) |
| R6 | Equilibrium: three forces form a closed triangle (th3; key_note; q2) | higher | 6.5.1.4 (HT only) "equilibrium situations" | TH | OK |
| R7 | Scale-drawing technique: ruler, protractor, state scale (th3) | higher | 6.5.1.4 (HT only); MS 5a | TH | OK |
| R8 | "component method is more precise… For GCSE, scale drawings are acceptable" (th3) | — | 6.5.1.4 | TH | WRONG emphasis (F3) |
| R9 | `higher` "using trigonometry" | off-spec | — | TH | OFF-SPEC (F1) |
| R10 | FIFA (3 N E, 4 N N → 5 N at 53°) | higher (as a scale drawing); method off-spec | 6.5.1.4 (HT only) | TH | OFF-SPEC method (F2) |
| R11 | q1 (13 N at 67.4°, sin/cos given) | off-spec | — | TH | OFF-SPEC (F4) |
| R12 | q2 (closed triangle → equilibrium) | higher | 6.5.1.4 (HT only) | TH | OK |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | th1 | a force can be resolved into two perpendicular components; reverse of finding a resultant | OK | — | 6.5.1.4 |
| C2 | th1 | Fx = F cos θ, Fy = F sin θ (θ from horizontal) | OFF-SPEC | Physics correct; AQA requires scale drawing only | 6.5.1.4 |
| C3 | th1 | 50 N at 37°: Fx = 50 × 0.799 = 40 N; Fy = 50 × 0.602 = 30 N; 40² + 30² = 50² | OFF-SPEC (arithmetic OK) | cos 37° = 0.7986, sin 37° = 0.6018 ✓; 39.9 ≈ 40, 30.1 ≈ 30 ✓; 1600 + 900 = 2500 ✓. Usable only as a scale drawing (50 mm at 37°, measure ≈ 40 mm and 30 mm). | 6.5.1.4 |
| C4 | th1 | "Essential for inclined plane problems, projectile problems" | OFF-SPEC | Projectiles are not in AQA GCSE. Slopes only qualitatively / by scale drawing. | — |
| C5 | th2 M1 | tip-to-tail scale drawing, 5 steps | OK | — | 6.5.1.4 |
| C6 | th2 M2 | parallelogram: both from one point, diagonal = resultant | OK | — | 6.5.1.4 |
| C7 | th2 M3 | component method with √ and arctan | OFF-SPEC | — | 6.5.1.4 |
| C8 | th3 | equilibrium = zero resultant; three forces tip-to-tail form a closed triangle | OK | — | 6.5.1.4 |
| C9 | th3 | applications: tension in two strings holding a weight; object at rest on a slope | OK | Both are "equilibrium situations" doable by scale drawing | 6.5.1.4 |
| C10 | th3 | "Accuracy matters — ruler and protractor; always state the scale; convert back" | OK | — | MS 5a |
| C11 | th3 | "component method is more precise. For GCSE, scale drawings are acceptable" | WRONG (for AQA) | For AQA GCSE scale drawing is the required method, not a tolerated second best. Say: "AQA asks for scale drawings. Use a sharp pencil and a large scale to reduce error." | 6.5.1.4 |
| C12 | `higher` | "resolve forces into components using trigonometry" | OFF-SPEC | replace "trigonometry" with "scale drawing" | 6.5.1.4 |
| C13 | common_mistake | cos horizontal / sin vertical; swap if from vertical; Pythagoras check | OFF-SPEC | physics correct; not usable. Replace with a scale-drawing mistake (no scale stated; resultant drawn tip-of-last to tail-of-first; angle measured from the wrong line). | 6.5.1.4 |
| C14 | key_note | Fx = F cos θ…; R = √(…); closed triangle; parallelogram | OFF-SPEC in part | keep closed triangle and parallelogram | 6.5.1.4 |
| C15 | equations | Fx = F cos θ; Fy = F sin θ; R = √(Fx² + Fy²) | OFF-SPEC | No equation on spec or on either June 2026 sheet. No formula triangles. | 6.5.1.4 |
| C16 | variables | "F — Resultant force" | IMPRECISE | In Fx = F cos θ, F is the force being resolved, not a resultant. Moot (equations off-spec). | — |
| C17 | FIFA F, I, F | R = √(9 + 16) = 5 N; θ = arctan(4/3) = 53° N of E | OFF-SPEC (arithmetic OK) | arctan(1.333) = 53.13° ✓. Answer correct; method off-spec. As a scale drawing (1 cm = 1 N): 3 cm east, 4 cm north, measure 5.0 cm and ≈ 53° → 5 N at 53° north of east. | 6.5.1.4 |
| C18 | FIFA Convert `[NEW]` | "Nothing to convert — both forces are already given in newtons (SI)." | CORRECTED | For a scale drawing the conversion is the scale. Corrected line in source. | CFIFA amendment |
| C19 | q1 key | 13 N at 67.4°: Fx = 13 × 0.385 = 5 N; Fy = 13 × 0.923 = 12 N | OFF-SPEC (arithmetic OK) | 5.005 ✓, 12.0 ✓ (5-12-13 triangle) | 6.5.1.4 |
| C20 | q1 opt 2 / wx1 | swapped sin/cos | OK aligned | — | — |
| C21 | q1 opt 3 / wx2 | both 9.2 N; equal only at 45° | OK aligned | 13/√2 = 9.19 ✓ | — |
| C22 | q1 opt 4 / wx3 | 13 N horizontal, 0 vertical | OK aligned | — | — |
| C23 | q2 key | closed triangle → equilibrium, resultant zero | OK | — | 6.5.1.4 |
| C24 | q2 wx1 | aligned to opt 1 (all equal); triangle can be scalene | OK | — | — |
| C25 | q2 wx2 | aligned to opt 2 (accelerating) | OK | — | — |
| C26 | q2 wx3 | aligned to opt 3 (parallel); parallel forces cannot form a triangle | OK | — | — |
| C27 | matching (to be replaced) | rows 1–3 are trig/Pythagoras | OFF-SPEC | replace anyway | — |
| C28 | header routes | TH only | ROUTE | true routes CH TH (Combined HT has the identical text) | 8464 6.5.1.4 (HT only) |

Count: **WRONG 1** (C11); OFF-SPEC: trigonometry/Pythagoras throughout (th1, th2 M3, equations, FIFA method, q1, common_mistake, key_note, `higher`); ROUTE 1 (TH → CH TH, approved, in the route PR). wrong_explanations: all 6 read and aligned. All 10 arithmetic results rechecked ✓.

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| q1 | Requires trigonometry; AQA says scale drawings only | Do not use as written on any route |
| FIFA | Pythagoras + arctan | Keep its numbers and answer; Design re-sets it as a scale drawing (see F2) |
| q2 | — | Usable on CH TH |

## 5. Calculations (rule 3)
No equation. The only quantitative step is a scale drawing: choose a scale (Convert: N → cm), draw, measure length and angle, convert back (cm → N). **No chained equations.** Higher only.

## 6. Verdict
SOURCE HAS ERRORS. The lesson's core method is off-spec: AQA 6.5.1.4 says "(scale drawings only)", and the page teaches trigonometry, Pythagoras and arctan as its equations, worked example, common mistake and q1. th3 calls scale drawing a second-best when it is the required method. Correct content: resolution idea, tip-to-tail, parallelogram, closed triangle, q2. True routes CH TH (approved move). Not a Mide call: the spec wording is unambiguous and both sheets agree (no equation printed).
