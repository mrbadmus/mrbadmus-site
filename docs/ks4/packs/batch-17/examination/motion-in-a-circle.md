# Examination — Motion in a Circle (motion-in-a-circle) — AQA 8464 6.5.4.1.3 (HT only) / 8463 4.5.6.1.3 (HT only); Triple Higher layer 8463 4.8.1.3 (physics only, HT only)
Verdict: SOURCE HAS ERRORS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-17/04-checked-science-source/physics-6.5.6-motion-in-a-circle.md`.
Spec sources read as text: `AQA-8464-spec.txt` (v1.1, 04 Oct 2019) 6.5.4.1.3, 6.5.4.2.1; `AQA-8463-spec.txt` (v1.1, 30 Sep 2019) 4.5.6.1.3, 4.8.1.3. Neither spec contains the word "centripetal" or "geostationary". Neither June 2026 sheet prints a circular-motion equation. Route audit read: `ks4-routes/docs/ks4/route-audit/physics.md` row `motion-in-a-circle` ("MOVE WIDER → CH TH … Physics-only layer (HT): stable orbit speed and radius (4.8.1.3)") and note 4.

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n; th1–th3 = theory chunks. The data's "6.5.6" is a known-wrong ref (BATCH-PLAN "Odd things"); true refs 8464 **6.5.4.1.3** and 8463 **4.5.6.1.3**, both (HT only). Single route copy (TH); the site ships TH; the approved route PR moves the page to CH TH.

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 | **6.5.4.1.3** | Velocity | **(HT only)** sentence on circular motion |
| 8463 | **4.5.6.1.3** | Velocity | **(HT only)**, identical wording |
| 8463 | **4.8.1.3** | Orbital motion, natural and artificial satellites | (physics only); the speed/radius bullets **(HT only)** |
| Supporting | 8464 6.5.4.2.1 / 8463 4.5.6.2.1 Newton's first law; 6.5.4.2.2 / 4.5.6.2.2 resultant force → acceleration | | base |

Spec statements (verbatim):
- 8464 6.5.4.1.3 = 8463 4.5.6.1.3: "The velocity of an object is its speed in a given direction. Velocity is a vector quantity. … (HT only) Students should be able to explain qualitatively, with examples, that motion in a circle involves constant speed but changing velocity."
- 8463 4.8.1.3: "Gravity provides the force that allows planets and satellites (both natural and artificial) to maintain their circular orbits. … (HT only) Students should be able to explain qualitatively how: (HT only) for circular orbits, the force of gravity can lead to changing velocity but unchanged speed; (HT only) for a stable orbit, the radius must change if the speed changes."

## 2. Route table
| # | teachable point (pack location) | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Constant speed, changing direction → changing velocity → accelerating (th1; common_mistake; key_note; `higher` s1) | higher | 6.5.4.1.3 (HT only) | TH | OK — ROUTE: CH TH |
| R2 | Velocity tangential; acceleration and resultant force towards the centre (th1, th2) | higher (beyond spec, correct) | 6.5.4.1.3; 6.5.4.2.2 | TH | OK; "centripetal" OFF-SPEC term (F4) |
| R3 | Inward force supplied by existing forces: friction, tension, gravity (th2; `higher` s2; common_mistake) | higher | 6.5.4.1.3 with 6.5.4.2.2 | TH | OK |
| R4 | Electron orbiting nucleus; roller-coaster loop; F = mv²/r (th2) | off-spec | — | TH | OFF-SPEC (F4) |
| R5 | Force removed → straight line along the tangent, Newton's first law (th2; common_mistake; key_note) | higher | 6.5.4.1.3; 6.5.4.2.1 | TH | OK |
| R6 | Gravity provides the force for an orbit (th3; matching) | triple-higher on this page | 8463 4.8.1.3 (physics only) | TH | OK |
| R7 | Faster orbit needs smaller radius; lower satellites faster (th3; `higher` s3; key_note) | triple-higher | 8463 4.8.1.3 (HT only) | TH | OK; "spiral" IMPRECISE (F3) |
| R8 | Geostationary radius ~36,000 km (th3) | off-spec | — | TH | WRONG (F2) |
| R9 | q1 (satellite accelerating?) | higher | 6.5.4.1.3 (HT only) | TH | OK — CH TH |
| R10 | q2 (faster orbit, radius) | triple-higher | 8463 4.8.1.3 (HT only) | TH | WRONG key reason (F1) |
| — | equations, FIFA, RP | none | — | — | correct: no equation on spec |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | th1 | constant speed in a circle is still accelerating; velocity is a vector; direction changes | OK | — | 6.5.4.1.3 |
| C2 | th1 | acceleration towards the centre; "centripetal" | OK / OFF-SPEC term | direction correct; the term is not used by AQA | — |
| C3 | th1 | velocity tangential, at 90° to the radius | OK | — | — |
| C4 | th2 | net inward force; not a new type of force | OK | correct and useful | 6.5.4.2.2 |
| C5 | th2 | planet–gravity; car–friction; ball–tension | OK | — | 4.8.1.3 |
| C6 | th2 | electron orbiting nucleus–electrostatic attraction; roller-coaster loop top: contact force + gravity | OFF-SPEC | physics acceptable; cut (not assessable, and electrons in AQA are "at specific distances", 4.4.1.3 / 6.4.1.3) | — |
| C7 | th2 | F = mv²/r "not required at GCSE" | OFF-SPEC | correct statement; cut | — |
| C8 | th2 | string cut → ball moves off along the tangent, not outward; Newton's first law | OK | — | 6.5.4.2.1 |
| C9 | th3 | gravity provides the force for an orbit; stable when it exactly provides the force needed | OK | — | 4.8.1.3 |
| C10 | th3 | speed increases at same radius → gravity insufficient → "object spirals outward" | IMPRECISE | it moves away into a larger, non-circular orbit; it does not spiral. Spec: "for a stable orbit, the radius must change if the speed changes". | 4.8.1.3 |
| C11 | th3 | stable faster orbit → smaller radius; slower → larger; lower satellites faster | OK | — | 4.8.1.3 (HT) |
| C12 | th3 | geostationary: "orbital speed matches Earth's rotation period"; "Radius: ~36,000 km" | WRONG + OFF-SPEC | ~36,000 km (35,800 km) is the HEIGHT above the surface; the orbital radius from Earth's centre is ≈ 42,000 km. It is the orbital PERIOD (24 h) that matches Earth's rotation, not the speed. Geostationary orbits are not in 8463. | — |
| C13 | `higher` | explain acceleration at constant speed; what provides the inward force; orbital stability | OK | s3 is 8463 4.8.1.3 (physics only) | 6.5.4.1.3; 4.8.1.3 |
| C14 | common_mistake | not in equilibrium; net resultant; tangent not outward | OK | — | 6.5.4.1.3; 6.5.4.2.1 |
| C15 | key_note | "Faster orbit at same radius = spiral outward" | IMPRECISE | as C10 | 4.8.1.3 |
| C16 | q1 key | direction changes → velocity changes → accelerates towards Earth's centre | OK | — | 6.5.4.1.3; 4.8.1.3 |
| C17 | q1 opt 2 / wx1 | constant speed → no acceleration | OK aligned | — | — |
| C18 | q1 opt 3 / wx2 | accelerates away from Earth | OK aligned | — | — |
| C19 | q1 opt 4 / wx3 | acceleration needs a change of speed | OK aligned | — | — |
| C20 | q2 key | "The orbital radius must decrease — a smaller orbit requires less centripetal force at higher speed" | WRONG (reason) | Conclusion right, reason backwards: a faster satellite needs a BIGGER inward force; closer to Earth, gravity is stronger and can supply it. | 4.8.1.3 (HT) |
| C21 | q2 opt 2 / wx1 | radius increases | OK aligned | — | — |
| C22 | q2 opt 3 / wx2 | nothing changes | OK aligned | — | — |
| C23 | q2 opt 4 / wx3 | engines fire continuously | OK aligned | — | — |
| C24 | matching (to be replaced) | gravity; friction; tension; satellite gravity | OK | replaced anyway | — |
| C25 | header routes / spec | TH; "6.5.6 (HT only)" | ROUTE | true CH TH (8464 6.5.4.1.3 HT); data spec ref wrong (known) | 6.5.4.1.3 |

Count: **WRONG 2** (C12, C20); IMPRECISE 1 (spiral, C10/C15); OFF-SPEC: "centripetal" term, mv²/r, electron, roller coaster, geostationary; ROUTE 1 (TH → CH TH, approved, in the route PR). wrong_explanations: all 6 read and aligned. No calculations.

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| q1 | — | Usable CH TH (satellite context is everyday enough for Combined) |
| q2 | key's reason backwards (F1); orbit content is 8463 only | Do not use as written; corrected copy in F1, then TH only |

## 5. Calculations (rule 3)
None. No equation in either spec point; F = mv²/r is off-spec.

## 6. Verdict
SOURCE HAS ERRORS. The core (constant speed, changing direction, so changing velocity and an acceleration towards the centre; force removed → straight-line tangent) is correct. q2's key gives a backwards reason, and the geostationary "radius ~36,000 km" is the height above the surface. The page's true routes are CH TH, with the orbit material (gravity provides the force; faster orbit needs a smaller radius) a Triple Higher layer from 8463 4.8.1.3. Nothing for Mide.
