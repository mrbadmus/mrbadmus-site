# Examination — Forces and Elasticity (forces-elasticity) — AQA 8464 6.5.3 / 8463 4.5.3
Verdict: SOURCE HAS ERRORS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-16/04-checked-science-source/physics-6.5.3-forces-elasticity.md`.
Spec sources read as text: `AQA-8464-spec.txt` (v1.1, 04 Oct 2019) 6.5.3, 6.1.1.2, 10.2.18 (RP18); `AQA-8463-spec.txt` (v1.1, 30 Sep 2019) 4.5.3 (identical wording except RP number), 8.2.6 (RP6). Equation sheets read: `8464-equation-sheet.txt` and `8463-equation-sheet-Jun26.txt` (both June 2026) — both print F = ke, Ee = ½ke², W = mg. Route audit read: `ks4-routes/docs/ks4/route-audit/physics.md` row `forces-elasticity` ("Ee = ½ke² is base. Spring RP (8464 RP18 / 8463 RP6).").

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n; th1–th3 = theory chunks. All four route copies identical (no `higher`).

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 | **6.5.3** | Forces and elasticity | base; **Required practical activity 18** |
| 8463 | **4.5.3** | Forces and elasticity | base; **Required practical activity 6** |
| Supporting | 8464 6.1.1.2 / 8463 4.1.1.2 Ee = ½ke² "(assuming the limit of proportionality has not been exceeded)" | | base (Mide's ruling: Ee is base) |
| Supporting | 8464 6.5.1.3 / 8463 4.5.1.3 W = mg (masses hung in the RP) | | base |

Spec statements (verbatim, 8464 = 8463):
- "Students should be able to: • give examples of the forces involved in stretching, bending or compressing an object • explain why, to change the shape of an object (by stretching, bending or compressing), more than one force has to be applied – this is limited to stationary objects only • describe the difference between elastic deformation and inelastic deformation caused by stretching forces."
- "The extension of an elastic object, such as a spring, is directly proportional to the force applied, provided that the limit of proportionality is not exceeded."
- "force = spring constant × extension  F = k e" — "recall and apply this equation." F in N, k in N/m, e in m.
- "This relationship also applies to the compression of an elastic object, where 'e' would be the compression of the object."
- "A force that stretches (or compresses) a spring does work and elastic potential energy is stored in the spring. Provided the spring is not inelastically deformed, the work done on the spring and the elastic potential energy stored are equal."
- "Students should be able to: • describe the difference between a linear and non-linear relationship between force and extension • calculate a spring constant in linear cases • interpret data from an investigation of the relationship between force and extension • calculate work done in stretching (or compressing) a spring (up to the limit of proportionality) using the equation: elastic potential energy = 0.5 × spring constant × extension²  Ee = ½ k e²" — "apply this equation which is given on the Physics equation sheet."
- "Students should be able to calculate relevant values of stored energy and energy transfers."
- "Required practical activity 18 [8463: 6]: investigate the relationship between force and extension for a spring."

## 2. Route table
| # | teachable point (pack location) | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Force stretches/compresses a spring (th1) | base | 6.5.3 | all four | OK |
| R2 | Proportionality "within the ELASTIC LIMIT" (th1; th2; key_note) | base (as limit of proportionality) | 6.5.3 | all four | WRONG term (F1) |
| R3 | F = ke; k = stiffness; e = increase in length; rearrangements (th1; equations; variables; FIFA; common_mistake; q1) | base | 6.5.3 | all four | OK |
| R4 | Force–extension graph; linear section; gradient = k; curve beyond (th2; key_note) | base | 6.5.3 | all four | OK (term F1) |
| R5 | Elastic vs inelastic deformation; elastic limit defined (th2; key_note) | base | 6.5.3 | all four | OK |
| R6 | RP: masses on a spring, F–e graph, k from gradient (th2; rp; key_note) | base (RP) | 8464 RP18 / 8463 RP6 | all four | OK; RP label wrong (F2) |
| R7 | More than one force to change shape; single force → acceleration (th3; q2) | base | 6.5.3 | all four | OK; q2 WRONG (F3) |
| R8 | Ee = ½ke²; work done = Ee if not inelastically deformed; applications (th3) | base | 6.5.3; 6.1.1.2 | all four | OK; missing from `equations` (F4) |
| R9 | Compression: e = compression | base | 6.5.3 | — | GAP (F4) |
| R10 | Linear vs non-linear; "limit of proportionality" | base | 6.5.3 | — | GAP (F1, spec-core section added) |
| — | `higher` | none | — | — | correct: 6.5.3 has no HT or physics-only content |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | th1 | "Within the ELASTIC LIMIT, extension is DIRECTLY PROPORTIONAL to the applied force" | WRONG | "provided that the limit of proportionality is not exceeded". The elastic limit is a different point (can lie beyond it). | 6.5.3 |
| C2 | th1 | F = ke; units; k = stiffness; stiffer → larger k | OK | — | 6.5.3 |
| C3 | th1 | e = increase in length from natural length | OK | — | 6.5.3 |
| C4 | th1 | k = 50, e = 0.2 → F = 10 N; e = F/k; k = F/e | OK | ✓ | — |
| C5 | th2 | axes: extension x, force y; linear section, gradient = k | OK | gradient of F (y) vs e (x) = k ✓. (If e is on y, gradient = 1/k — worth a misconception line.) | 6.5.3 |
| C6 | th2 | "BEYOND THE ELASTIC LIMIT: Graph curves" | WRONG | "beyond the limit of proportionality" | 6.5.3 |
| C7 | th2 | "Larger extension per unit force" beyond | OK | typical spring | — |
| C8 | th2 | elastic: returns to length; inelastic: does not; elastic limit = point beyond which deformation becomes inelastic | OK | (term not in AQA spec, physics correct) | 6.5.3 |
| C9 | th2 | "REQUIRED PRACTICAL (RP18)" | IMPRECISE | RP18 is the Combined number; Physics 8463 = RP6 | 8464 6.5.3; 8463 4.5.3 |
| C10 | th2 | RP method: add masses, measure extension, plot F vs e, k from gradient, find where it breaks down | OK | force = weight of masses, W = mg (g given) — needed and not stated | 10.2.18; 8.2.6 |
| C11 | th3 | more than one force to change shape; one force → accelerates | OK | spec limits this to stationary objects | 6.5.3 |
| C12 | th3 | "Two equal and opposite forces are needed to stretch, compress or bend an object" | IMPRECISE | "more than one force"; bending a supported ruler takes three. Two equal and opposite for stretch/compress is fine. | 6.5.3 |
| C13 | th3 | rubber band: pull both ends; spring: push both ends | OK | — | 6.5.3 |
| C14 | th3 | Ee = ½ × k × e² | OK | base (Mide's ruling); applies up to limit of proportionality | 6.5.3; 6.1.1.2 |
| C15 | th3 | all work done (within elastic limit) stored as Ee | OK | spec: "Provided the spring is not inelastically deformed…" ✓ | 6.5.3 |
| C16 | th3 | "When released, this converts to kinetic energy" | IMPRECISE (minor) | "transferred to the kinetic store" (energy is transferred between stores) | 6.1.1.1 |
| C17 | th3 | applications | OK | — | — |
| C18 | common_mistake | 10 cm → 14 cm: e = 4 cm = 0.04 m | OK | ✓ | 6.5.3 |
| C19 | key_note | "Elastic limit: beyond this, Hooke's Law breaks down — graph curves" | WRONG | limit of proportionality | 6.5.3 |
| C20 | key_note | "RP18" | IMPRECISE | RP18 (Combined) / RP6 (Physics) | — |
| C21 | equations | only F = ke | GAP | Ee = ½ke² (base, On the sheet) taught in th3 but absent from `equations`/`variables` | 6.5.3 |
| C22 | FIFA | 80 × 0.15 = 12 N | OK | ✓ | 6.5.3 |
| C23 | FIFA Convert `[NEW]` | "Nothing to convert — k is already in N/m and e is already in metres (SI)." | OK | ✓. Second CFIFA example needs cm → m (q1's numbers or common_mistake's 10 → 14 cm are ready-made). | CFIFA amendment |
| C24 | rp | "RP18 (Physics) — …" | IMPRECISE | "RP18 (Combined 8464) / RP6 (Physics 8463)". Frozen; flag only. | — |
| C25 | q1 key | e = 6 cm = 0.06 m; k = 3/0.06 = 50 N/m | OK | ✓ | 6.5.3 |
| C26 | q1 opt 2 / wx1 | 3/0.16 = 18.75 (total length) | OK aligned | ✓ | — |
| C27 | q1 opt 3 / wx2 | 0.06/3 = 0.02 (inverted; m/N) | OK aligned | ✓ | — |
| C28 | q1 opt 4 / wx3 | 3/0.01 = 300 | OK aligned | ✓. Weak distractor (no clear route to 1 cm), still valid. | — |
| C29 | q2 key | one force → accelerate; two equal opposite forces to deform without moving | OK | — | 6.5.3 |
| C30 | q2 opt 4 (index 3) | "The rubber band needs forces from both sides to stay in equilibrium while stretching" — marked false | WRONG | This is a correct statement of the spec reason (stationary object → resultant zero → more than one force). wx3 itself says "Equilibrium… IS the right idea here". Two defensible answers. | 6.5.3 |
| C31 | q2 wx1 | "…The reason is Newton's First Law — a single force would cause acceleration" | IMPRECISE | an unbalanced force causing acceleration is Newton's Second Law (First Law is the zero-resultant case) | 6.5.4.2.1–2 |
| C32 | q2 wx2 | "A single force CAN stretch an elastic material if one end is fixed — but then the fixed end provides the second force via Newton's Third Law" | IMPRECISE | contradicts the spec's "more than one force" in its first clause; the support's pull on the band is the second force on the band — not a Third-Law pair (Third-Law pairs act on different objects) | 6.5.3; 6.5.4.2.3 |
| C33 | matching (to be replaced) | 10 N; 0.05 m; "elastic limit exceeded → graph curves" | WRONG (row 3) | limit of proportionality. Replace anyway. | 6.5.3 |

Count: **WRONG 4** (C1, C6, C19 — one error, "elastic limit" for "limit of proportionality", in three places; C30 — q2 has two correct answers). IMPRECISE: C9/C20/C24 (RP numbering), C12, C16, C31, C32. GAP: C21, compression, linear/non-linear. wrong_explanations: all 6 read; all aligned to their indices; q2's wx1–wx3 have the defects above. All 9 arithmetic results ✓.

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| q1 | — | Usable on all four routes |
| q2 | option 4 is also correct (F3) | Do not use as written |
| rp | "RP18 (Physics)" — RP18 is the Combined number | Data usable; label RP18 (8464) / RP6 (8463) |

## 5. Calculations (rule 3)
- F = ke (and k = F/e, e = F/k). Not chained. Convert: cm → m, mm → m; extension = stretched length − natural length (a step before Insert). Base.
- Spring constant from data / RP: **chained** — Step 1 weight of hung masses W = mg (Convert g → kg); Step 2 k = F/e (Convert cm → m), or k = gradient of the F–e graph. Base.
- Ee = ½ke². Not chained when k and e are given. Convert: cm → m (then square). Base.
- Ee from F and e: **chained** — Step 1 k = F/e; Step 2 Ee = ½ke². Base.
- Ee → speed (energy transfer to kinetic store): **chained** — Step 1 Ee = ½ke²; Step 2 Ek = ½mv² → v. Base. ("calculate relevant values of stored energy and energy transfers")

## 6. Verdict
SOURCE HAS ERRORS. Numbers, F = ke work, q1 and the RP method are correct. The source uses "elastic limit" where AQA requires "limit of proportionality" (th1, th2, key_note) — a mark-losing term confusion. q2 has two defensible answers and imprecise explanations; do not use. RP numbering wrong for Physics (RP6). Ee = ½ke² is base and On the sheet but missing from the equations list. True routes CF CH TF TH. No Mide call.
