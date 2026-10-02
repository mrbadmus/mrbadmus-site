# Examination — Gravity, Stable Orbits and Orbital Speed (gravity-stable-orbits) — AQA 8463 4.8.1.3 (physics only) (HT only)
Verdict: SOURCE OK WITH FLAGS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-18/04-checked-science-source/physics-6.8.1-gravity-stable-orbits.md`.
Spec sources read as text: `AQA-8463-spec.txt` (v1.1, 30 Sep 2019) §4.8.1.1–4.8.1.3 and 4.5.6.1.3; `AQA-8464-spec.txt` (no space physics; 6.5.4.1.3 Velocity HT read for the circular-motion line); `8463-equation-sheet-Jun26.txt` (no orbit equation). Route audit row `gravity-stable-orbits` (TH / TH, "unsettled", §3 best reading TH). Neighbours: `solar-system-gravity` (this batch), batch-17 `motion-in-a-circle`, batch-6 `stellar-evolution`.

Conventions: T1–T3 = theory chunks; q1–q2 = quiz items; "wx n" = `wrong_explanations` key n. One route (TH). No fifas, no equations, no `[NEW — to be examined]` lines.

**Route settled at TH.** 8463 4.8.1.3 has a non-HT core ("Gravity provides the force that allows planets and satellites … to maintain their circular orbits") and two "(HT only)" bullets. This page's own content — its title, `higher`, both quiz items, T1–T2 — is the HT part: changing velocity with unchanged speed, and radius must change if speed changes. The non-HT core is taught on `solar-system-gravity` (TF TH). So the page is triple-higher throughout and TH is its true route, as the route audit kept it.

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 | — | none (no space physics) | — |
| 8463 | **4.8.1.3** (HT bullets) | Orbital motion, natural and artificial satellites | physics only, HT only |
| Supporting | 8463 4.5.6.1.3 / 8464 6.5.4.1.3 Velocity — "(HT only) … motion in a circle involves constant speed but changing velocity" | | HT |
| Supporting | 8463 4.8.1.3 non-HT core (taught on `solar-system-gravity`) | | physics only |

Spec statements (verbatim, 8463 4.8.1.3): "Gravity provides the force that allows planets and satellites (both natural and artificial) to maintain their circular orbits. Students should be able to describe the similarities and distinctions between the planets, their moons, and artificial satellites. (HT only) Students should be able to explain qualitatively how: (HT only) for circular orbits, the force of gravity can lead to changing velocity but unchanged speed; (HT only) for a stable orbit, the radius must change if the speed changes."

## 2. Route table
| # | teachable point | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Gravity provides the force towards the centre for a circular orbit (T1; key_note) | triple-higher (framing of the base core) | 4.8.1.3 | TH | OK |
| R2 | Gravity weaker with distance; F = Gm₁m₂/r² "for context" (T1) | triple-higher; the formula off-spec | 4.8.1.3 | TH | OK / OFF-SPEC (F2) |
| R3 | Speed up at same radius → larger orbit; slow down → smaller orbit (T1; T2; key_note; matching) | triple-higher | 4.8.1.3 HT bullet 2 | TH | OK; "spirals" IMPRECISE (F3) |
| R4 | Lower orbit → stronger gravity → higher speed; LEO 7700 m/s / 90 min; GEO 3000 m/s / 24 h (T1) | triple-higher | 4.8.1.3 HT bullet 2 | TH | OK |
| R5 | One correct speed per radius (T2) | triple-higher | 4.8.1.3 HT bullet 2 | TH | OK |
| R6 | Drag → orbit decays → re-entry; reboost burns (T2; key_note; q1) | triple-higher | 4.8.1.3 HT bullet 2 (application) | TH | OK |
| R7 | Transfer orbits; "firing engines forward → higher, slower orbit" (T2; common_mistake) | triple-higher | 4.8.1.3 HT bullet 2 | TH | IMPRECISE (F4) |
| R8 | Geostationary: one radius, 24 h, above equator (T2; key_note; q2) | triple (context of the base core) | 4.8.1.3 | TH | OK |
| R9 | Constant speed but accelerating / changing velocity (common_mistake only) | triple-higher | 4.8.1.3 HT bullet 1; 4.5.6.1.3 | TH | GAP — only in common_mistake (F6) |
| R10 | Escape velocity, black holes, Schwarzschild radius, spacetime, lensing, tides, Kepler (T3) | none — off-spec | — | TH | OFF-SPEC (F2) |
| R11 | `higher` | triple-higher | 4.8.1.3 HT | TH | OK |
| R12 | q1 | triple-higher | 4.8.1.3 HT bullet 2 | TH | usable (F5 note) |
| R13 | q2 | triple | 4.8.1.3 | TH | usable |
| — | RP, equations, fifas | none | — | — | correct |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | T1 | gravity provides the centripetal force towards the centre | OK | — | 4.8.1.3 |
| C2 | T1 | all masses attract; force decreases with distance | OK | — | — |
| C3 | T1 | F = Gm₁m₂/r², "formula not required at GCSE" | OK, OFF-SPEC | Correctly labelled; not on the 8463 sheet. No triangle, no calculation. | 8463 sheet |
| C4 | T1 | stable orbit: gravity = centripetal force needed for that speed and radius | OK | — | 4.8.1.3 HT |
| C5 | T1; T2 | speed increases → "spirals outward to larger orbit"; decreases → falls to smaller orbit | OK, IMPRECISE word | One change of speed gives a new (elliptical) orbit, not a spiral; spiralling is for gradual change (drag). Spec: "the radius must change if the speed changes". | 4.8.1.3 HT |
| C6 | T1 | lower orbit → stronger gravity → higher speed; higher → lower speed | OK | — | 4.8.1.3 HT |
| C7 | T1 | LEO ~400 km: ~7700 m/s, ~90 min | OK | 7.66 km/s, 92 min | — |
| C8 | T1 | GEO ~36,000 km: ~3000 m/s, 24 h | OK | 3.07 km/s | — |
| C9 | T2 | only one correct speed for a stable orbit at a given radius | OK | For a circular orbit. | 4.8.1.3 HT |
| C10 | T2 | speed decreases → "gravity exceeds the centripetal force needed" → moves in | OK | — | 4.8.1.3 HT |
| C11 | T2 | drag slows satellite → orbit decays → re-enters; engines fired to compensate | OK | (As it sinks it actually speeds up; drag keeps removing energy.) | — |
| C12 | T2 | raise orbit: speed up; lower orbit: slow down | OK | — | 4.8.1.3 HT |
| C13 | T2 | "firing engines forward → end up in higher, SLOWER orbit" | IMPRECISE | Ambiguous: engines pointing forward would brake the satellite. Say: "speed the satellite up (thrust forwards) → it rises to a higher orbit, where its final speed is lower." | 4.8.1.3 HT |
| C14 | T2 | GEO: period = Earth's rotation, above equator, one altitude ~35,786 km | OK | — | — |
| C15 | T3 | escape velocity Earth ~11.2 km/s | OK, OFF-SPEC | — | — |
| C16 | T3 | black holes: escape velocity > c; form when very massive stars collapse in supernova; Schwarzschild radius | OK (simplified), OFF-SPEC | Black holes as end-points belong to `stellar-evolution` (4.8.1.2). | 4.8.1.2 |
| C17 | T3 | mass curves space-time; gravitational lensing | OK, OFF-SPEC | Lensing is used on `dark-matter-dark-energy`. | — |
| C18 | T3 | tides from Moon's differential pull; spring/neap from Sun | OK, OFF-SPEC | — | — |
| C19 | T3 | Kepler: ellipses; equal areas; T² ∝ r³ | OK, OFF-SPEC | r is the semi-major axis for an ellipse. | — |
| C20 | `higher` | HT: gravity as centripetal force; speed must change if radius changes; what happens when speed changes | OK | Spec phrases it as "radius must change if the speed changes" — same relationship. | 4.8.1.3 HT |
| C21 | common_mistake | circular motion at constant speed is accelerating; force to centre; higher orbit needs a speed-up but ends slower | OK | This is HT bullet 1 — the only place the page says it (F6). | 4.8.1.3 HT; 4.5.6.1.3 |
| C22 | key_note | lower orbit: stronger gravity, faster, shorter period; GEO; speed ↑ → out; ↓ → in; drag → re-entry | OK | Period is off-spec context. | 4.8.1.3 HT |
| C23 | q1 key | drag → orbit decays → spirals in → re-enters | OK | — | 4.8.1.3 HT |
| C24 | q1 wx1 → opt 1 "settles into a higher orbit" | slowing → lower, not higher; "…without engine thrust the satellite cannot sustain even that reduced orbit" | OK paired; second clause IMPRECISE | First clause rebuts the option correctly. The second implies the satellite fails for lack of speed; in fact it speeds up as it sinks, and continuing drag is what brings it down. Does not alter the key. | — |
| C25 | q1 wx2 → opt 2 "falls straight down" | spirals in gradually, heats up | OK, paired | — | — |
| C26 | q1 wx3 → opt 3 "accelerates due to stronger gravity" | concedes it does speed up, but drag causes re-entry | OK, paired | Option 3 is partly true (a decaying satellite speeds up); the stem's "eventually" keeps the key unique. | — |
| C27 | q2 key | period matches Earth's rotation; 24 h at ~36,000 km | OK | Also needs to be above the equator, moving the same way as Earth turns — not needed for the key. | — |
| C28 | q2 wx1 → opt 1 "so far away it barely moves" | distant objects still appear to move; GEO is about matching rotation | OK, paired | — | — |
| C29 | q2 wx2 → opt 2 "hovers on engines" | orbits continuously; gravity provides the force | OK, paired | — | — |
| C30 | q2 wx3 → opt 3 "gravity too weak" | weaker but not zero; still the centripetal force | OK, paired | — | — |
| C31 | matching (to be replaced) | four orbital scenarios | OK | "Spirals outward" — same wording point as C5. | — |

Count: **0 WRONG**. IMPRECISE: C5, C13, C24. OFF-SPEC: T3 entire, C3. All `wrong_explanations` paired to their own options (6/6, read by hand).

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| none | q1 (triple-higher) and q2 (triple) both correct on TH | Both usable on TH. |

## 5. Verdict
SOURCE OK WITH FLAGS. The HT orbit science is right and both quiz items are usable. Wording to tighten: "spirals" for a single speed change, "firing engines forward". T3 is off-spec throughout (escape velocity, black holes, tides, Kepler) and overlaps `stellar-evolution` and `dark-matter-dark-energy`. HT bullet 1 (changing velocity, unchanged speed) sits only in common_mistake and should be taught.

**For Mide:** nothing. The route is TH on the best reading of the spec, as the route audit says: this page's content is the HT part of 8463 4.8.1.3; the non-HT part lives on `solar-system-gravity`.
