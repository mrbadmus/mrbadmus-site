# Examination — Moments, Levers and Gears (moments-levers-gears) — AQA 8463 4.5.4 (physics only); not in 8464
Verdict: SOURCE HAS ERRORS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-17/04-checked-science-source/physics-6.5.3-moments-levers-gears.md`.
Spec sources read as text: `AQA-8463-spec.txt` (v1.1, 30 Sep 2019) 4.5.4; `AQA-8464-spec.txt` (v1.1, 04 Oct 2019) — searched, no moments content; `8463-equation-sheet-Jun26.txt` (prints M = F d). Route audit read: `ks4-routes/docs/ks4/route-audit/physics.md` row `moments-levers-gears` (TF TH, OK).

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n; th1–th3 = theory chunks. Site's "6.5.3 (physics only)" is its internal number; true ref is 8463 **4.5.4**. Two route copies (TF, TH); the TF `higher` copy is `null`.

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8463 | **4.5.4** | Moments, levers and gears | **(physics only)**; no HT content |
| 8464 | — | not taught | — |
| Supporting | 8463 4.5.1.4 resultant forces / balanced; 4.5.2 work done (energy conserved in a lever) | | base |

Spec statements (verbatim, 8463 4.5.4):
- "A force or a system of forces may cause an object to rotate. Students should be able to describe examples in which forces cause rotation."
- "The turning effect of a force is called the moment of the force. The size of the moment is defined by the equation: moment of a force = force × distance, M = Fd … moment of a force, M, in newton-metres, Nm; force, F, in newtons, N; distance, d, is the perpendicular distance from the pivot to the line of action of the force, in metres, m." — "recall and apply this equation." MS 3c.
- "If an object is balanced, the total clockwise moment about a pivot equals the total anticlockwise moment about that pivot. Students should be able to calculate the size of a force, or its distance from a pivot, acting on an object that is balanced."
- "A simple lever and a simple gear system can both be used to transmit the rotational effects of forces. Students should be able to explain how levers and gears transmit the rotational effects of forces."

June 2026 8463 sheet prints "moment of a force = force × distance (normal to direction of force) M = F d" — label **On the sheet**.

## 2. Route table
| # | teachable point (pack location) | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Moment = turning effect; M = F × d; perpendicular distance; units (th1; equations; variables; common_mistake) | triple | 4.5.4 | TF TH | OK |
| R2 | Clockwise / anticlockwise; bigger moment from bigger F or d; door handle (th1) | triple | 4.5.4 | TF TH | OK |
| R3 | Principle of moments; seesaw example (th2; key_note; equations) | triple | 4.5.4 | TF TH | OK |
| R4 | Lever as force multiplier; examples (th2) | triple | 4.5.4 | TF TH | WRONG in part (F3) |
| R5 | Lever classes 1–3 (th2) | off-spec | — | TF TH | OFF-SPEC (F6) |
| R6 | Gears: opposite rotation; small→large slower with bigger turning effect (th3; key_note) | triple | 4.5.4 | TF TH | IMPRECISE (F4) |
| R7 | Gear ratio = teeth driven ÷ teeth driving (th3; key_note) | off-spec | — | TF TH | OFF-SPEC (F6) |
| R8 | Energy conserved in gears/levers (th3) | triple | 4.5.4 with 4.5.2 | TF TH | OK |
| R9 | `higher` (TH copy) — moments, principle, multiple forces | triple, **not HT** | 4.5.4 | TH | ROUTE (F5) |
| R10 | `higher` — gear ratios, output speed/force | off-spec | — | TH | OFF-SPEC (F5, F6) |
| R11 | FIFA (seesaw, 1.5 m) | triple | 4.5.4 | TF TH | OK; chains (rule 3) |
| R12 | q1 (40 N, 0.5 m) | triple | 4.5.4 | TF TH | key OK; wx1 WRONG (F1) |
| R13 | q2 (bicycle low gear) | triple | 4.5.4 | TF TH | key OK; wx1 WRONG (F2) |
| — | RP | none | — | — | correct: 4.5.4 has no required practical |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | th1 | a moment is the turning effect of a force about a pivot | OK | spec wording | 4.5.4 |
| C2 | th1; variables | M = F × d; N·m, N, m; d perpendicular from line of action to pivot | OK | spec writes "Nm" | 4.5.4 |
| C3 | th1 | 50 N at 0.4 m → 20 N·m | OK | 50 × 0.4 = 20 ✓ | — |
| C4 | th1 | bigger moment from bigger force or distance; handle at the edge | OK | — | 4.5.4 |
| C5 | th2 | equilibrium: total clockwise = total anticlockwise "about any pivot" | OK | true about any point for a balanced object; spec says "about a pivot" | 4.5.4 |
| C6 | th2 | 600 N at 1.5 m = 900 N·m; 900 ÷ 450 = 2 m | OK | ✓ | — |
| C7 | th2 | lever: small input force × long distance = large output force × short distance | OK | distances from the pivot | 4.5.4 |
| C8 | th2 | examples of levers "as FORCE MULTIPLIERS: … tweezers … fishing rod" | WRONG | Tweezers and a fishing rod (effort between pivot and load) give an output force SMALLER than the input; they multiply movement, not force. Wheelbarrow, crowbar, nutcracker, scissors are force multipliers. | 4.5.4 |
| C9 | th2 | lever classes 1–3 with examples | OFF-SPEC | physics correct; not in 8463; context only, never tested | — |
| C10 | th3 | meshed gears turn in opposite directions; teeth interlock | OK | — | 4.5.4 |
| C11 | th3 | gear ratio = teeth driven ÷ teeth driving | OFF-SPEC | a valid convention; no gear-ratio calculation in 8463 | — |
| C12 | th3 | small gear drives large: slower "but with MORE FORCE (torque)" | IMPRECISE | The teeth push on each other with equal force; on the larger gear that force acts further from its axle, so the MOMENT (turning effect) is larger. Say "bigger moment / turning effect", not "more force"; "torque" is not an AQA term. | 4.5.4 |
| C13 | th3 | low gear for acceleration; high gear at speed | OK | — | — |
| C14 | th3 | gears turn "a small force over a large rotation into a large force over a small rotation"; energy conserved | IMPRECISE / OK | same as C12 (moment, not force); energy statement OK | 4.5.4; 4.5.2 |
| C15 | th3 | bicycle gears, car gearbox, clocks, wind turbine gearbox | OK | note: bicycle sprockets are linked by a chain, not meshed, and turn the same way | — |
| C16 | `higher` | moments and principle of moments listed as HT | ROUTE | 4.5.4 has no HT label; all of it is on TF and TH | 4.5.4 |
| C17 | `higher` | calculate gear ratios, predict output speed/force | OFF-SPEC | — | 4.5.4 |
| C18 | common_mistake | perpendicular distance; principle needs equilibrium | OK | — | 4.5.4 |
| C19 | key_note | gears "more force, less speed" | IMPRECISE | as C12 | 4.5.4 |
| C20 | equations | M = F × d; Σ clockwise = Σ anticlockwise | OK | M = F d is On the sheet (8463 June 2026) | 8463 sheet |
| C21 | FIFA | 300 × 2 = 400 × d₂; d₂ = 600 ÷ 400 = 1.5 m | OK | ✓. Frozen typo "an 400 N" (should be "a"). Label "Moment Calculation" is a principle-of-moments problem. Chains: Step 1 moment of the known side (300 × 2 = 600 N m); Step 2 equal and opposite moment, d = M ÷ F. | 4.5.4 |
| C22 | Convert `[NEW]` | "Nothing to convert — both forces … newtons … metres …" | OK | marked examined ✓ | CFIFA amendment |
| C23 | q1 key | M = 40 × 0.5 = 20 N·m | OK | ✓ | 4.5.4 |
| C24 | q1 opt 2 / wx1 | 80 = 40 ÷ 0.5; wx1 "M = F ÷ d gives the force needed to produce a given moment at that distance" | WRONG (wx1) | F ÷ d is not a meaningful quantity; the force needed for a given moment is M ÷ d. Option arithmetic ✓; wx1 is aligned to option 2 but states false physics. | 4.5.4 |
| C25 | q1 opt 3 / wx2 | 40.5 = 40 + 0.5 | OK aligned | — | — |
| C26 | q1 opt 4 / wx3 | 0.0125 = 0.5 ÷ 40 | OK aligned | ✓ | — |
| C27 | q2 key | small driving → large driven: wheel turns slowly with more turning force | OK | "turning force" acceptable everyday wording for moment. Stem: on a bicycle the sprockets are chain-linked, not meshed (IMPRECISE, see F2). | 4.5.4 |
| C28 | q2 opt 2 / wx1 | wx1 "Small driving → large driven gear gives MORE SPEED not more force. Low gear = large driving sprocket (at pedals) → small sprocket (at wheel)…" | WRONG | Contradicts the key and th3: small driving large gives LESS speed and a bigger moment. Large chainring → small sprocket is a HIGH gear. | 4.5.4 |
| C29 | q2 opt 3 / wx2 | equal speeds only with identical gears | OK aligned | — | — |
| C30 | q2 opt 4 / wx3 | gears can trade either way | OK aligned | — | — |
| C31 | matching (to be replaced) | 20 N·m; principle; lever; gear "more turning force (torque)" | OK / IMPRECISE (row 4 "torque") | replaced anyway | — |
| C32 | header routes | TF TH | OK | physics only, no HT | 4.5.4 |

Count: **WRONG 3** (C8, C24, C28); IMPRECISE 3 (C12, C14, C19, one idea); OFF-SPEC 2 (lever classes, gear ratio); ROUTE 1 (`higher` labels base content HT). wrong_explanations: all 6 read — all aligned to their option index; 2 state false physics. All 6 arithmetic results rechecked ✓.

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| q1 | wx1 false (F1) | Do not use as written. Corrected wx1 in F1; then TF TH. |
| q2 | wx1 contradicts the key (F2); "meshes" on a bicycle | Do not use as written. Corrected copy in F2; then TF TH. |
| FIFA | — | Usable TF TH; it chains (rule 3) — set it out Step 1 / Step 2. |

## 5. Calculations (rule 3)
- Moment M = F d (and F = M ÷ d, d = M ÷ F): no chain. Convert cm → m.
- Balanced object, find a force or distance: **chains** — Step 1 find the known moment(s) with M = F d (add if more than one); Step 2 set equal to the unknown side and rearrange M = F d. Convert cm → m.
- Gear ratio: off-spec, none.

## 6. Verdict
SOURCE HAS ERRORS. Moment calculations and the principle of moments are correct throughout. Three WRONG items: both quiz items carry a false wrong-answer explanation (q2's contradicts its own key), and th2 lists tweezers and a fishing rod as force multipliers. The gear explanation says "more force" where AQA wants "bigger moment". No HT content exists in 4.5.4, so nothing on this page is badged Higher. No conflict between AQA sources; nothing for Mide.
