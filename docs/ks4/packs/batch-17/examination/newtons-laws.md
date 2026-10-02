# Examination — Newton's Laws of Motion (newtons-laws) — AQA 8464 6.5.4.2.1–6.5.4.2.3 / 8463 4.5.6.2.1–4.5.6.2.3
Verdict: SOURCE HAS ERRORS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-17/04-checked-science-source/physics-6.5.4.2.1-newtons-laws.md`.
Spec sources read as text: `AQA-8464-spec.txt` (v1.1, 04 Oct 2019) 6.5.4.2.1–6.5.4.2.3 and §10.2.19 (RP19); `AQA-8463-spec.txt` (v1.1, 30 Sep 2019) 4.5.6.2.1–4.5.6.2.3 (identical wording; RP7). Equation sheets: `8464-equation-sheet.txt`, `8463-equation-sheet-Jun26.txt` (June 2026) — both print F = m a. Route audit row `newtons-laws` (base; HT = inertia, inertial mass; RP 8464 RP19 / 8463 RP7).

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n; th1–th3 = theory chunks. Route copies identical except `higher` (TH text on CH/TH; `null` on CF/TF).

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 | **6.5.4.2.1** | Newton's First Law | base; inertia sentence **(HT only)** |
| 8464 | **6.5.4.2.2** | Newton's Second Law | base; inertial mass **(HT only)**; **Required practical activity 19** |
| 8464 | **6.5.4.2.3** | Newton's Third Law | base |
| 8463 | **4.5.6.2.1–4.5.6.2.3** | same three | same labels, identical wording; **Required practical activity 7** |

Spec statements (verbatim, 8464 = 8463): N1 — "If the resultant force acting on an object is zero and: the object is stationary, the object remains stationary; the object is moving, the object continues to move at the same speed and in the same direction. So the object continues to move at the same velocity. So, when a vehicle travels at a steady speed the resistive forces balance the driving force. So, the velocity (speed and/or direction) of an object will only change if a resultant force is acting on the object." "(HT only) The tendency of objects to continue in their state of rest or of uniform motion is called inertia." N2 — "The acceleration of an object is proportional to the resultant force acting on the object, and inversely proportional to the mass of the object." "resultant force = mass × acceleration, F = ma … recall and apply this equation." "Students should recognise and be able to use the symbol for proportionality, ∝." "(HT only) Students should be able to explain that: inertial mass is a measure of how difficult it is to change the velocity of an object; inertial mass is defined as the ratio of force over acceleration." "Students should be able to estimate the speed, accelerations and forces involved in large accelerations for everyday road transport. Students should recognise and be able to use the symbol that indicates an approximate value or approximate answer, ~". RP: "investigate the effect of varying the force on the acceleration of an object of constant mass, and the effect of varying the mass of an object on the acceleration produced by a constant force." N3 — "Whenever two objects interact, the forces they exert on each other are equal and opposite. Students should be able to apply Newton's Third Law to examples of equilibrium situations."

## 2. Route table
| # | teachable point | true layer | spec | verdict |
|---|---|---|---|---|
| R1 | N1 statement; zero resultant → rest or constant velocity (th1, key_note) | base | 6.5.4.2.1 | OK |
| R2 | N1 examples incl. car at constant speed: driving force = resistive forces (th1; matching) | base | 6.5.4.2.1 | OK |
| R3 | Inertia (th1) | **higher** | 6.5.4.2.1 (HT only) | ROUTE — in a base field |
| R4 | N2: a ∝ F, a ∝ 1/m (th2, key_note) | base | 6.5.4.2.2 | OK |
| R5 | F = ma, rearrangements, 1000 kg / 3000 N example (th2, equations, variables) | base | 6.5.4.2.2 | OK |
| R6 | Inertial mass = F/a, measure of difficulty of changing velocity (`higher`) | **higher** | 6.5.4.2.2 (HT only) | OK |
| R7 | F = ma on slopes; inertial vs gravitational mass (`higher`) | none | — | **OFF-SPEC** |
| R8 | N3 statement and features (th3, common_mistake, key_note) | base | 6.5.4.2.3 | OK (C11) |
| R9 | FIFA 900 kg, 2700 N | base | 6.5.4.2.2 | OK |
| R10 | q1 F = 1500 × 2 | base | 6.5.4.2.2 | OK |
| R11 | q2 book on table N3 pair | base | 6.5.4.2.3 | **WRONG item** |
| R12 | RP19 (8464) / RP7 (8463) force & mass vs acceleration | base, all four routes | 6.5.4.2.2 | **GAP** — no `rp` section in the frozen data |
| R13 | Estimates of large road-transport accelerations; ~ and ∝ symbols | base | 6.5.4.2.2 | **GAP** |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | th1 | N1: rest or constant velocity unless a resultant force acts | OK | — | 6.5.4.2.1 |
| C2 | th1 | resultant force needed to start, stop or change direction | OK | — | 6.5.4.2.1 |
| C3 | th1 | book: weight balanced by normal force; puck on frictionless ice; car: driving force = friction + air resistance | OK | Puck is idealised — fine. | 6.5.4.2.1 |
| C4 | th1 | "INERTIA: the tendency of an object to resist changes in its motion" | OK (HT) | HT only. | 6.5.4.2.1 (HT only) |
| C5 | th1 | "Heavier (more massive) objects have more inertia" | IMPRECISE | Use "more mass", not "heavier": inertia depends on mass, not weight (an object has the same inertia in space). | 6.5.4.2.2 (HT only) |
| C6 | th2 | N2 proportionality statement | OK | spec wording | 6.5.4.2.2 |
| C7 | th2 | F = ma; a = F ÷ m; m = F ÷ a; 3000 ÷ 1000 = 3 m/s² | OK | ✓ | 6.5.4.2.2 |
| C8 | `higher` | "multi-step problems including objects on slopes" | OFF-SPEC | AQA GCSE never sets F = ma on a slope (resolving forces is HT vector-diagram work at 6.5.1.4, not combined with N2). Cut. | 6.5.1.4; 6.5.4.2.2 |
| C9 | `higher` | inertial mass = F/a; measure of how hard to change velocity | OK | spec wording | 6.5.4.2.2 (HT only) |
| C10 | `higher` | "Distinguish inertial mass from gravitational mass" | OFF-SPEC | Not on the spec. Cut. | 6.5.4.2.2 |
| C11 | th3 | N3 statement; equal, opposite, different objects, same type | OK | — | 6.5.4.2.3 |
| C12 | th3 | "Book on table: book pushes down on table (gravity transfers) → table pushes up on book (normal force)" | IMPRECISE | The book's push on the table is a **contact force**, not gravity "transferring". Say: "book pushes down on table (contact force) ↔ table pushes up on book (contact force)". Weight's partner is the book pulling the Earth up. | 6.5.4.2.3 |
| C13 | th3 | rocket/exhaust; swimmer/water; Earth/you | OK | — | 6.5.4.2.3 |
| C14 | common_mistake | horse–cart pair acts on different objects, cannot cancel | OK | — | 6.5.4.2.3 |
| C15 | key_note | as above | OK | — | — |
| C16 | FIFA | a = 2700 ÷ 900 = 3 m/s² | OK | ✓ | — |
| C17 | q1 key | 1500 × 2 = 3000 N | OK | ✓ | — |
| C18 | q1 opt1 / wx1 | 750 N, F = m ÷ a | OK | aligned ✓ | — |
| C19 | q1 opt2 / wx2 | 1502 N, m + a | OK | aligned ✓ | — |
| C20 | q1 opt3 / wx3 | 300 N, ÷10 "confuses g" | OK | aligned ✓ (motive speculative, harmless) | — |
| C21 | q2 stem | "The book pushes down on the table with force 10 N (its weight)" | **WRONG** | The force on the table is a contact force; the book's weight acts on the book, from the Earth. Equal in size here, not the same force. Calling it "its weight" teaches the classic N3 misconception. | 6.5.4.2.3 |
| C22 | q2 key | "The table pushes UP on the book with 10 N — equal, opposite, on the table (reacting on the book)" | **WRONG** | The partner force acts **on the book**; "on the table" is wrong. | 6.5.4.2.3 |
| C23 | q2 opt1 / wx1 | opt1: "The normal contact force from the table pushing up on the book — this balances the weight"; wx1: "…Option B describes it correctly but incorrectly labels it as 'balancing' — N3 pairs don't balance" | **WRONG** | Option 1 names exactly the right force (table on book), and "this balances the weight" is **true** — normal force and weight both act on the book and balance (N1). So the item has two correct options, and wx1 makes a false claim. | 6.5.4.2.1; 6.5.4.2.3 |
| C24 | q2 opt2 / wx2 | Earth's gravity as reaction to normal force | OK | aligned ✓ | — |
| C25 | q2 opt3 / wx3 | book pushes on Earth via table | OK | aligned ✓ | — |
| C26 | matching (to be replaced) | N1 car; N2 heavier trolley; N3 swimmer; N2 1200/600 = 2 | OK | ✓ | — |
| C27 | CFIFA Convert | "Nothing to convert — mass … kilograms and force … newtons" | OK | → `[NEW — examined ✓]` | CFIFA amendment |
| C28 | rp | (absent) | GAP | RP19 / RP7 sits in this spec point; method, variables and data processing needed. Verified: 8464 "Required practical activity 19", 8463 "Required practical activity 7", same wording. | 6.5.4.2.2 |

Count: **1 WRONG item** (q2: stem, key and a second correct option — 3 defects); **OFF-SPEC**: C8, C10; **ROUTE**: inertia in base theory; **IMPRECISE**: C5, C12. **GAP**: the required practical; road-transport estimates; ∝ and ~. All arithmetic ✓ (4 calculations).

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| q1 | — | Usable on all four routes. |
| q2 | Stem calls the contact force "its weight"; key says the force acts "on the table"; option 1 is also correct; wx1 false | **Do not use as written** (any route). |

## 5. Verdict
SOURCE HAS ERRORS. The physics of N1/N2/N3 and every calculation are right, but frozen quiz q2 is wrong three ways (stem, key, a second correct option) and must not be used. The `higher` field adds two off-spec items (slopes; gravitational mass). The required practical (8464 RP19 / 8463 RP7) belongs on this page and is entirely missing from the frozen data — written from the spec in the source file.
