# Examination — Induced Potential and the Generator Effect (induced-potential) — AQA 8463 4.7.3.1
Verdict: SOURCE OK WITH FLAGS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-18/04-checked-science-source/physics-6.7.3.1-induced-potential.md`.
Spec sources read as text: `AQA-8463-spec.txt` (v1.1, 30 Sep 2019) §4.7.3, 4.7.3.1–4.7.3.2; `AQA-8464-spec.txt` (v1.1, 04 Oct 2019) §6.7 (no generator-effect content); both June 2026 equation sheets. Route audit `ks4-routes/docs/ks4/route-audit/physics.md` row 86.

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n. One route copy (TH).

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8463 | **4.7.3.1** | Induced potential | **(HT only)**, under 4.7.3 "Induced potential, transformers and the National Grid **(physics only) (HT only)**" |
| 8464 | — | not in Combined | — |
| Supporting | 8463 4.7.3.2 Uses of the generator effect (same labels) — theory 2–3 and q2 overlap it | | |

Spec statements (verbatim, 8463 4.7.3.1): "If an electrical conductor moves relative to a magnetic field or if there is a change in the magnetic field around a conductor, a potential difference is induced across the ends of the conductor. If the conductor is part of a complete circuit, a current is induced in the conductor. This is called the generator effect." "An induced current generates a magnetic field that opposes the original change, either the movement of the conductor or the change in magnetic field." "Students should be able to recall the factors that affect the size of the induced potential difference/induced current." "Students should be able to recall the factors that affect the direction of the induced potential difference/induced current." "Students should be able to apply the principles of the generator effect in a given context."

## 2. Route table
| # | teachable point | true layer | spec | verdict |
|---|---|---|---|---|
| R1 | Generator effect: relative movement / changing field → induced pd (theory 1; common_mistake; key_note; `higher`) | triple-higher | 4.7.3.1 | OK (wording F1) |
| R2 | Induced current's field opposes the change ("Lenz") (theory 1; common_mistake) | triple-higher | 4.7.3.1 | OK |
| R3 | Size factors: speed, field strength, turns (theory 1, 3; key_note; q1) | triple-higher | 4.7.3.1 | OK; "area" is extra (F5) |
| R4 | Direction factors | triple-higher | 4.7.3.1 | **GAP** — only via Fleming's right-hand rule (F2, F3) |
| R5 | pd across ends vs current only in a complete circuit | triple-higher | 4.7.3.1 | GAP — not stated (F3) |
| R6 | Simple AC generator, slip rings, split-ring commutator, AC/DC output (theory 2–3; q2) | triple-higher | **4.7.3.2** | OK, belongs to `uses-generator-effect` (F6) |
| R7 | Back-emf; motor/generator reversibility (theory 3) | not in spec | — | OFF-SPEC (F5) |
| R8 | q1 | triple-higher | 4.7.3.1 | usable |
| R9 | q2 | triple-higher | 4.7.3.2 | usable (overlaps lesson 8) |
| — | equations, FIFA, RP, examiner_tip | none | — | correct: none in 4.7.3.1 |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | theory 1 | pd induced when there is a "CHANGE IN MAGNETIC FLUX" | IMPRECISE | AQA GCSE never uses "magnetic flux" (only "magnetic flux density" in F = BIl). Spec wording: conductor moves relative to a magnetic field, or the field around it changes. | F1; 4.7.3.1 |
| C2 | theory 1 | "Faraday's Law: induced pd ∝ rate of change of flux" | OFF-SPEC (true) | Name and proportionality not required; the examinable form is "faster movement → larger pd". | F1 |
| C3 | theory 1 | "Lenz's Law: induced current produces a field that OPPOSES the change"; "why generators require work" | OK | Content is spec; the name is not required. | 4.7.3.1 |
| C4 | theory 1 | stronger magnet, faster movement, more turns → larger pd | OK | AQA recall list. | 4.7.3.1 |
| C5 | theory 1 | "CROSS-SECTIONAL AREA: larger coil area → more flux → larger pd" | OFF-SPEC (true for a rotating coil) | Not in AQA's usual list; omit or keep as extension. | F5 |
| C6 | theory 1 | Fleming's right-hand rule for induced current direction | OFF-SPEC | Not in 8463. The spec's direction factors are the direction of movement and the direction (polarity) of the field: reverse either and the induced pd/current reverses. A second hand rule beside the (HT) left-hand rule invites confusion. | F2 |
| C7 | theory 2 | generator converts kinetic → electrical | IMPRECISE (minor) | Stores language: energy transferred from the kinetic store, electrically. | 8463 4.1.1.1 |
| C8 | theory 2 | coil rotating in field cuts field lines → emf → current | OK | "emf" is not an AQA GCSE term — say "potential difference". | F1 |
| C9 | theory 2 | "At 0° to field: cutting rate maximum → maximum emf. At 90° to field: parallel to field, cutting rate zero → zero emf." | IMPRECISE | Self-contradictory as written ("90° to field: parallel to field"). Correct: coil plane **parallel** to the field → sides cut field lines fastest → maximum pd; coil plane **perpendicular** to the field → sides move along the field lines → pd zero. | F4 |
| C10 | theory 2 | sinusoidal AC; frequency = rotation frequency; slip rings rotate with coil; carbon brushes stationary | OK | 4.7.3.2 content. | 4.7.3.2 |
| C11 | theory 3 | faster, stronger, more turns, larger coil → larger pd | OK (area F5) | — | 4.7.3.1 |
| C12 | theory 3 | split-ring commutator swaps connections each half-turn → pulsing DC; used in DC generators and motors | OK | 4.7.3.2 / 4.7.2.3. | 4.7.3.2 |
| C13 | theory 3 | same device can be motor or generator | OK (context) | — | — |
| C14 | theory 3 | back-emf limits motor speed | OFF-SPEC | True; not in 8463. | F5 |
| C15 | `higher` | "Apply Fleming's right-hand rule" | OFF-SPEC | As C6. | F2 |
| C16 | common_mistake | pd induced only when field CHANGES (relative motion); stationary conductor in steady field → no pd; faster change → larger pd; induced current opposes change | OK | Wording "flux" → F1. | 4.7.3.1 |
| C17 | key_note | as theory | OK (F1 wording; area F5) | — | — |
| C18 | q1 key | changing field as magnet moves induces current; push faster, stronger magnet, more turns | OK | Exactly AQA's three factors. | 4.7.3.1 |
| C19 | q1 opt 1 / wx1 | static field induces nothing | OK | Aligned. | 4.7.3.1 |
| C20 | q1 opt 2 / wx2 | friction irrelevant | OK | Aligned. | — |
| C21 | q1 opt 3 / wx3 | stationary magnet close to coil induces nothing | OK | Aligned. | 4.7.3.1 |
| C22 | q2 key | rate of cutting varies; emf and current reverse every half-turn | OK | 4.7.3.2. | 4.7.3.2 |
| C23 | q2 opt 1 / wx1 | magnets permanent, don't switch polarity | OK | Aligned. | — |
| C24 | q2 opt 2 / wx2 | slip rings keep a continuous connection; split-ring commutator swaps | OK | Aligned; correct. | 4.7.3.2 |
| C25 | q2 opt 3 / wx3 | DC can come from rotation via a commutator | OK | Aligned. | 4.7.3.2 |
| C26 | matching (to be replaced) | four pairs | OK | All correct. | — |

Count: **0 WRONG**; IMPRECISE: C1, C7, C8, C9; OFF-SPEC: C2, C5, C6, C14, C15. No calculation.

## 4. Frozen items wrong for their route
None. q1 and q2 correct and triple-higher; **both usable on TH**. q2 tests 4.7.3.2 content, so if Design keeps it here, `uses-generator-effect` should not reuse it.

## 5. Gaps (spec core added to the source file)
The direction factors and the pd-vs-current distinction are missing from the frozen data except via the off-spec right-hand rule. Added to the source file as "Spec core missing from the frozen data".

## 6. Verdict
SOURCE OK WITH FLAGS. Physics correct; terminology (flux, emf, Faraday/Lenz, right-hand rule) goes beyond and around AQA's wording; the direction factors need teaching in AQA's terms; theory 2's angle description must be rewritten.

**For Mide:** nothing.
