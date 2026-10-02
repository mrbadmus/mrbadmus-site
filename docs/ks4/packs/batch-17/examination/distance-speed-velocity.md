# Examination — Distance, Speed and Velocity (distance-speed-velocity) — AQA 8464 6.5.4.1.1–6.5.4.1.3 / 8463 4.5.6.1.1–4.5.6.1.3
Verdict: SOURCE HAS ERRORS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-17/04-checked-science-source/physics-6.5.4.1.1-distance-speed-velocity.md`.
Spec sources read as text: `AQA-8464-spec.txt` (v1.1, 04 Oct 2019) 6.5.4.1.1–6.5.4.1.3; `AQA-8463-spec.txt` (v1.1, 30 Sep 2019) 4.5.6.1.1–4.5.6.1.3 (identical wording); both June 2026 sheets (each prints s = v t). Route audit read: `ks4-routes/docs/ks4/route-audit/physics.md` row `distance-speed-velocity` (base, OK; "Circular motion (HT) has its own page").

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n; th1–th3 = theory chunks. Route copies: CF and TF `higher` are `null`; CH and TH carry `higher`.

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 / 8463 | **6.5.4.1.1 / 4.5.6.1.1** | Distance and displacement | base |
| 8464 / 8463 | **6.5.4.1.2 / 4.5.6.1.2** | Speed | base |
| 8464 / 8463 | **6.5.4.1.3 / 4.5.6.1.3** | Velocity | base; one **(HT only)** sentence (circular motion) |
| Supporting | 6.5.1.1 / 4.5.1.1 scalar and vector | | base |

Spec statements (verbatim, 8464 = 8463):
- "Distance is how far an object moves. Distance does not involve direction. Distance is a scalar quantity. Displacement includes both the distance an object moves, measured in a straight line from the start point to the finish point and the direction of that straight line. Displacement is a vector quantity. Students should be able to express a displacement in terms of both the magnitude and direction."
- "Speed does not involve direction. Speed is a scalar quantity. … Typical values may be taken as: walking ̴ 1.5 m/s, running ̴ 3 m/s, cycling ̴ 6 m/s. Students should be able to recall typical values of speed for a person walking, running and cycling as well as the typical values of speed for different types of transportation systems. … A typical value for the speed of sound in air is 330 m/s."
- "distance travelled = speed × time, s = v t … distance, s, in metres, m; speed, v, in metres per second, m/s; time, t, in seconds, s" — "recall and apply this equation." "Students should be able to calculate average speed for non-uniform motion."
- "The velocity of an object is its speed in a given direction. Velocity is a vector quantity. Students should be able to explain the vector–scalar distinction as it applies to displacement, distance, velocity and speed. (HT only) Students should be able to explain qualitatively, with examples, that motion in a circle involves constant speed but changing velocity."
- Section note: "use ratios and proportional reasoning to convert units and to compute rates."

## 2. Route table
| # | teachable point (pack location) | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Distance scalar; displacement vector; 3 m N + 4 m E (th1; key_note) | base | 6.5.4.1.1 | all four | OK; direction IMPRECISE (F6) |
| R2 | Distance = displacement only in one straight line (th1) | base | 6.5.4.1.1 | all four | OK |
| R3 | Speed scalar; v = d ÷ t; units (th2; equations; variables; FIFA) | base | 6.5.4.1.2 | all four | OK; symbols IMPRECISE (F5) |
| R4 | Typical speeds (th2) | base | 6.5.4.1.2 | all four | sound IMPRECISE (F4); transport GAP (F7) |
| R5 | Speed rarely constant; average speed (th2; common_mistake; key_note) | base | 6.5.4.1.2 | all four | OK |
| R6 | 1 m/s = 3.6 km/h (th2) | base | 6.5.4 section note | all four | OK |
| R7 | Velocity = speed in a direction; vector; out-and-back example (th3) | base | 6.5.4.1.3 | all four | OK |
| R8 | Velocity changes if speed or direction changes; = acceleration (th3) | base | 6.5.4.1.3; 6.5.4.1.5 | all four | OK |
| R9 | Car round a bend at constant speed has changing velocity (th3; common_mistake s3; key_note) | higher | 6.5.4.1.3 (HT only) | all four | ROUTE (F2) |
| R10 | `higher` — circle, centripetal acceleration and force | higher (centripetal off-spec) | 6.5.4.1.3 (HT only) | CH TH | OK / OFF-SPEC term (F2) |
| R11 | FIFA (450 m, 30 s) | base | 6.5.4.1.2 | all four | OK |
| R12 | q1 (cyclist out and back) | base | 6.5.4.1.1–3 | all four | key OK; opt 4 IMPRECISE (F3) |
| R13 | q2 (roundabout) | higher | 6.5.4.1.3 (HT only) | all four | WRONG (F1); ROUTE (F2) |
| — | RP | none | — | — | correct |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | th1 | distance = total path, scalar; displacement = straight line start→finish with direction, vector | OK | — | 6.5.4.1.1 |
| C2 | th1 | 3 m N then 4 m E: distance 7 m; displacement √(9 + 16) = 5 m "(north-east)" | IMPRECISE | 5 m ✓, but the direction is 53° east of north (bearing 053°), not north-east (045°). Pythagoras is beyond AQA's required maths here; a scale drawing gives magnitude and direction. | 6.5.4.1.1 |
| C3 | th1 | one direction in a straight line: distance = displacement; otherwise distance > |displacement| | OK | — | — |
| C4 | th2 | speed = rate of change of distance; scalar | OK | — | 6.5.4.1.2 |
| C5 | th2; equations; variables | v = d ÷ t; d distance, s displacement | IMPRECISE | AQA writes s = v t with s = distance; both June 2026 sheets print "distance travelled = speed × time s = v t". Using s for displacement here will clash with the sheet. | 6.5.4.1.2 |
| C6 | th2 | walking 1.5, running 3, cycling 6 m/s | OK | spec values | 6.5.4.1.2 |
| C7 | th2 | car on motorway ~30 m/s | OK | 70 mph ≈ 31 m/s | — |
| C8 | th2 | speed of sound in air ~340 m/s | IMPRECISE | spec typical value is 330 m/s | 6.5.4.1.2 |
| C9 | th2 | light 3 × 10⁸ m/s | OK | (8464 6.6.2.1 states EM waves travel at the same speed in vacuum) | — |
| C10 | th2 | equation gives average speed | OK | — | 6.5.4.1.2 |
| C11 | th2 | 1 m/s = 3.6 km/h; 30 m/s ≈ 108 km/h | OK | ✓ | section note |
| C12 | th3 | velocity = rate of change of displacement; vector; velocity = displacement ÷ time | OK | spec defines velocity as speed in a given direction; consistent | 6.5.4.1.3 |
| C13 | th3 | 100 m N in 10 s → 10 m/s N; 100 m N + 100 m S in 20 s: speed 10 m/s, velocity 0 | OK | ✓ (average velocity) | — |
| C14 | th3 | velocity changes with speed or direction; bend at constant speed; changing velocity = acceleration | OK; HT sentence | bend sentence is (HT only) | 6.5.4.1.3 |
| C15 | `higher` | constant speed, changing velocity; accelerating towards centre; "centripetal acceleration … centripetal force" | OK / OFF-SPEC term | spec asks only the qualitative constant-speed/changing-velocity statement; "centripetal" is not an AQA term | 6.5.4.1.3 (HT only) |
| C16 | common_mistake | speed scalar, velocity vector; circle; average speed = total distance ÷ total time | OK | circle sentence HT | 6.5.4.1.2–3 |
| C17 | key_note | as above | OK | circle phrase HT | — |
| C18 | FIFA | 450 ÷ 30 = 15 m/s | OK | ✓; no chain | 6.5.4.1.2 |
| C19 | Convert `[NEW]` | "Nothing to convert — distance … metres and time … seconds" | OK | marked examined ✓ | CFIFA amendment |
| C20 | q1 key | 1200 m ÷ 120 s = 10 m/s; displacement 0 → velocity 0 | OK | ✓ | 6.5.4.1.1–3 |
| C21 | q1 opt 2 / wx1 | swaps speed and velocity | OK aligned | — | — |
| C22 | q1 opt 3 / wx2 | both 10 m/s | OK aligned | — | — |
| C23 | q1 opt 4 / wx3 | "5 m/s … average of 600 m in 60 s both ways" | IMPRECISE (opt 4 text) | its own working gives 10, not 5 — a self-contradicting distractor. wx3 (1200 ÷ 120 = 10, not 5) aligned. | — |
| C24 | q2 key | direction changes, so velocity changes | OK | — | 6.5.4.1.3 (HT) |
| C25 | q2 opt 2 / wx1 | constant speed → constant velocity | OK aligned | — | — |
| C26 | q2 opt 3 / wx2 | velocity always 10 m/s | OK aligned | — | — |
| C27 | q2 opt 4 / wx3 | "No — the car is accelerating because it is going around a circle"; wx3 "Option D is actually CORRECT" | WRONG | Option 4 is a true answer to the question (velocity is not constant; the car is accelerating). Two correct options; wx3 concedes it and names "Option D". | 6.5.4.1.3 |
| C28 | matching (to be replaced) | 5 m/s; velocity 0 round a track; 7 m; circle | OK | row 4 HT | — |
| C29 | header routes | CF CH TF TH | OK | HT circle content reaches CF TF (F2) | — |

Count: **WRONG 1** (C27). ROUTE 1 (circle sentences on Foundation routes). IMPRECISE 4 (direction; symbols; 340 m/s; q1 opt 4). GAP 1 (transport speeds). wrong_explanations: all 6 read and aligned to their option index; q2 wx3 concedes its option is correct. 6 calculations rechecked ✓.

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| q1 | option 4's working contradicts its value (F3) | Do not use as written; corrected copy in F3, then all four routes |
| q2 | two correct options (F1); HT | Do not use as written; corrected copy in F1, then CH TH only |
| FIFA | — | Usable on all four routes |

## 5. Calculations (rule 3)
- s = v t and rearrangements: no chain. Convert km → m, minutes/hours → s, km/h → m/s (÷ 3.6). Base.
- Average speed for non-uniform motion (total distance ÷ total time): no chain when distances and times are given; **chains** when a leg is given as a speed and a time — Step 1 s = v t for each leg (add distances and times); Step 2 v = total s ÷ total t. Base.
- Displacement magnitude and direction: scale drawing (no equation). Base.

## 6. Verdict
SOURCE HAS ERRORS. Definitions, the out-and-back examples and all arithmetic are correct. q2 has two correct options (the source's own wx3 says so); q1's fourth option contradicts its own working. The circle sentences are (HT only) and reach Foundation routes; the full treatment lives on `motion-in-a-circle`. Use AQA's s = v t (s = distance) to match the sheet, and 330 m/s for sound. Nothing for Mide.
