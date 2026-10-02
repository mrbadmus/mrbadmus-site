# Batch 18 — diagram library audit

Method: grepped `figlib/physics.py`, `figlib/ks4phys.py`, `figlib/ks4elec.py`,
`figlib/charts.py`, `shared/ks4-diagrams.js`, `ks3_art/p*.py` and
`ks4_lessons/authored/batch-2/` + `batch-3/*.dc.html` for function names and
docstrings naming each lesson's subject matter, then read the matching
function's docstring (and signature, where relevant) to confirm a real match
rather than a substring collision. `ks3_art/p*.py` entries are KS3
INTERACTIVE BENCHES (sliders, drag-and-drop, scored instruments), not drawn
figures, so they are cited only as "Reusable, contingent" pedagogical
precedent, never a direct hit. RP numbers quoted anywhere below are verbatim
from each lesson's own `rp` field only — none has been checked against AQA's
own practical-activity numbering, so every one is **(frozen label,
unverified)**. No authored batch-2/batch-3 lesson links forward to any slug
in this batch (see `_extract-notes.md` note 10) — a clean contrast with
batch 17.

| # | Lesson | Existing drawing code that already covers it |
|---|---|---|
| 1 | poles-of-a-magnet | **Direct match:** `figlib/physics.py` `two_magnets()` — "Two-magnet interaction - attraction (S face N) on left, repulsion (N face N) on right" — exactly the like/opposite-poles half of this lesson. **Nothing found** for permanent-vs-induced magnetism or magnetic domains. **Direct match (KS3 precedent):** `ks3_art/p10.py` `r_track_pair` (p10-01, "put two things end to end... the NOTHING branch is 102 of the 150 states and it is the lesson" — a combine-two-objects-and-see-if-they-attract bench, two-thirds of whose states do nothing at all because one object is non-magnetic or wrongly paired — the same permanent/induced/non-magnetic classification this lesson teaches). |
| 2 | magnetic-fields | **Direct match, two of them:** `figlib/physics.py` `bar_magnet_field()` — "Single bar magnet with field lines looping N -> S" — and `figlib/ks4phys.py` `magnet_compasses(magnet, compasses, ...)` — "A bar magnet... two halves lettered N and S, and plotting compasses drawn as EMPTY circles" at given points — the second is an exact match for this lesson's own RP21 compass-plotting method. **Direct match (KS3 precedent, two of them):** `ks3_art/p10.py` `r_compass_plot` (p10-02, "put the compass down and read it" — the KS3 unit's own compass-plotting bench, matching this lesson's RP text) and `r_dip_circle` (p10-03, "take the same compass somewhere else" — Earth's magnetic field / dip angle, matching this lesson's Earth's-field section). |
| 3 | electromagnetism | **Direct match, three of them:** `figlib/physics.py` `current_wire_field()` — "Field circles around a wire carrying current out of the page" — and `solenoid_field()` — "Solenoid with field lines like a bar magnet" — one per half of this lesson (wire, then solenoid/electromagnet); `figlib/ks4phys.py` `solenoid(turns, pitch, radius, ..., current=...)` draws the coil's physical winding (front/back strokes per turn) as a complement to `solenoid_field()`'s field-line version. **Direct match (KS3 precedent):** `ks3_art/p10.py` `r_solenoid_bench` (p10-04, "build one and see what it lifts... turns and current are two separate controls because they are two separate reasons" — the KS3 unit's own electromagnet-strength bench, exactly this lesson's "more turns/more current = stronger field" content). |
| 4 | flemings-left-hand-rule | **Direct, exact-name match:** `figlib/physics.py` `motor_effect()` — "Wire carrying current in a magnetic field: Fleming's left-hand rule (force, field, current as perpendicular axes)" — exactly this lesson's content. **No KS3 precedent** — the motor effect and Fleming's rule are KS4-only; `ks3_art/p10.py`'s `r_motor_coil` (cited under #5) teaches the coil-rotation CONSEQUENCE of the motor effect, not the rule itself. |
| 5 | electric-motors | **Direct match:** `figlib/physics.py` `motor_coil_forces(W, field_lines)` — "A motor coil seen END-ON between N (left) and S (right): the left side carries current into the page..., the right side out of it" — the coil-in-a-field half of a DC motor, exactly this lesson's mechanism. **Nothing found** for the split-ring commutator itself as a drawn figure. **Direct match (KS3 precedent):** `ks3_art/p10.py` `r_motor_coil` (p10-05, "reverse one thing at a time... the coil is frozen horizontal" — the KS3 unit's own motor-effect bench, reversing current/field to flip force direction, the same mechanism this lesson scales into a continuously-rotating motor). |
| 6 | loudspeakers-headphones | **Nothing found anywhere searched** for a loudspeaker cone/voice-coil figure. **No KS3 precedent** — no KS3 unit teaches loudspeakers as a motor-effect application; `ks3_art/p10.py`'s Magnetism unit stops at the motor itself (#5). |
| 7 | induced-potential | **Nothing found anywhere searched** for a generator-effect/induced-EMF figure (moving conductor or magnet inducing a current). **No KS3 precedent** — KS3's `p10` unit stops at the motor effect (#4–#5) and never reaches the generator effect. |
| 8 | uses-generator-effect | **Nothing found anywhere searched** for an alternator/dynamo or slip-rings-vs-commutator comparison figure. **No KS3 precedent**, for the same reason as #7. |
| 9 | microphones | **Nothing found anywhere searched** for a dynamic-microphone figure (diaphragm, coil, generator effect). **No KS3 precedent**, for the same reason as #7. |
| 10 | transformers | **Nothing found anywhere searched** for a primary/secondary-coil-on-an-iron-core transformer figure. **No KS3 precedent** — transformers sit outside `ks3_art/p10`'s five-lesson scope. |
| 11 | solar-system-gravity | **Direct match (structure half):** `figlib/physics.py` `solar_system()` — "Sun + 8 planets in order, labelled, not to scale" — exactly the Solar-System-structure half of this lesson; draws no orbital-speed-vs-distance relationship. **Reusable, contingent (KS3 precedent):** `ks3_art/p12.py`'s shared `space-bench` component (`r_space_bench`, one shell for six P12 pages) — two of the six models (`p12-01`, `p12-02`) use a W=m×g triangle for a weight-on-different-planets contrast, relevant background for this lesson's gravity content, and `p12-06` uses d=c×t for light-year/AU scale (this lesson's own scale section); none of the six models the orbital-speed-vs-orbital-radius relationship this lesson needs. |
| 12 | gravity-stable-orbits | **Nothing found anywhere searched** for an orbital-speed-vs-radius or gravity-as-centripetal-force figure — the same gap `figlib` has for batch-17's `motion-in-a-circle`. **No KS3 precedent** — P12's `space-bench` (cited under #11) stops at W=mg and distance scale, never orbital mechanics. |
| 13 | dark-matter-dark-energy | **Nothing found anywhere searched.** No figure anywhere draws galaxy rotation curves, gravitational lensing or a matter/dark-matter/dark-energy composition chart. **No KS3 precedent** — `ks3_art/p12.py`'s `r_space_think` (the shell `p12-03`–`05` put on the rail) is P12's own closest approach to content this abstract, and its module docstring states it "draws NOTHING, deliberately." |

## Figures still needed

1. **poles-of-a-magnet** — a permanent-vs-induced magnetism figure (hard vs soft material, domain alignment) — genuinely missing; `two_magnets()` already covers the attract/repel half directly.
2. **magnetic-fields** — none needed; `bar_magnet_field()` and `magnet_compasses()` already cover it directly.
3. **electromagnetism** — none needed; `current_wire_field()`, `solenoid_field()` and `solenoid()` already cover it directly.
4. **flemings-left-hand-rule** — none needed; `motor_effect()` already covers it directly.
5. **electric-motors** — a split-ring commutator figure (showing the swap every half-turn) — genuinely missing; `motor_coil_forces()` already covers the coil-in-a-field half directly.
6. **loudspeakers-headphones** — a loudspeaker cross-section figure (permanent magnet, voice coil, cone, AC in/sound out) — genuinely missing.
7. **induced-potential** — a generator-effect figure (magnet moving into/out of a coil, induced current direction by Fleming's right-hand rule) — genuinely missing.
8. **uses-generator-effect** — an alternator-vs-dynamo comparison figure (slip rings → AC vs split-ring commutator → pulsing DC) — genuinely missing.
9. **microphones** — a dynamic-microphone cross-section figure, ideally paired visually with the loudspeaker figure above to show the reversed energy flow — genuinely missing.
10. **transformers** — a primary/secondary-coil-on-an-iron-core figure with the turns ratio labelled — genuinely missing.
11. **solar-system-gravity** — an orbital-speed-vs-distance figure (closer orbit = faster speed) — genuinely missing; `solar_system()` already covers the structure half directly.
12. **gravity-stable-orbits** — an orbital-speed-vs-radius or gravity-as-centripetal-force figure — genuinely missing, the same gap as batch-17's `motion-in-a-circle`.
13. **dark-matter-dark-energy** — a galaxy-rotation-curve figure (observed flat curve vs the curve visible matter alone predicts) and/or a universe-composition chart (ordinary matter/dark matter/dark energy by proportion) — both genuinely missing.

## False near-hits

- **microphones** — grepped "microphone" across `figlib` and `ks3_art`; the only hits are `ks3_art/p6.py`'s `r_medium_range` ("a striker and a microphone across a gap" — a sound-detection prop in a KS3 medium/range experiment) and a matching comment in `ks3_art/p8.py` — neither is a figure about the electromagnetic-induction operating principle this lesson's dynamic microphone actually uses; both ruled out.
- **loudspeakers-headphones** — grepped "loudspeaker" across the same files; the only hit is a passing remark in `ks3_art/p10.py` ("which is why a compass is used away from loudspeakers and steel railings" — a magnetic-interference caution inside the compass-plotting bench, not a figure about loudspeakers themselves) — ruled out.
- **transformers** — grepped "transformer" and "gear" (batch-17's moments-levers-gears already found nothing for the latter); neither term appears anywhere in `figlib` or `ks3_art` — confirmed clean "nothing found" rather than a near-hit requiring a ruling.
