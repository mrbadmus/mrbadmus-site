# Examination — Microphones (microphones) — AQA 8463 4.7.3.3
Verdict: SOURCE HAS ERRORS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-18/04-checked-science-source/physics-6.7.3.3-microphones.md`.
Spec sources read as text: `AQA-8463-spec.txt` (v1.1, 30 Sep 2019) §4.7.2.4, 4.7.3, 4.7.3.1, 4.7.3.3; `AQA-8464-spec.txt` (v1.1, 04 Oct 2019) §6.7 (no microphone content); both June 2026 equation sheets. Route audit `ks4-routes/docs/ks4/route-audit/physics.md` row 88.

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n. One route copy (TH).

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8463 | **4.7.3.3** | Microphones | **(HT only)**, under 4.7.3 "(physics only) (HT only)" |
| 8464 | — | not in Combined | — |
| Supporting | 8463 4.7.3.1 (generator effect); 8463 4.7.2.4 Loudspeakers (physics only)(HT only) — the reverse device | | |

Spec statements (verbatim, 8463 4.7.3.3): "Microphones use the generator effect to convert the pressure variations in sound waves into variations in current in electrical circuits." "Students should be able to explain how a moving-coil microphone works."

## 2. Route table
| # | teachable point | true layer | spec | verdict |
|---|---|---|---|---|
| R1 | Moving-coil (dynamic) microphone: sound → diaphragm vibrates → coil moves in magnet's field → generator effect → varying current at the sound's frequency (theory 1; common_mistake; key_note; `higher`; q1; q2) | triple-higher | 4.7.3.3 | OK |
| R2 | Microphone is the reverse of a loudspeaker (theory 1; q1) | triple-higher | 4.7.3.3; 4.7.2.4 | OK |
| R3 | Condenser, ribbon, electret microphones; quality factors (theory 2; key_note "Condenser") | not in spec | — | OFF-SPEC (F3) |
| R4 | Preamp, ADC, CD sampling, signal chain (theory 3) | not in spec | — | OFF-SPEC (F3) |
| R5 | "electromagnetic induction works in both directions … Einstein's principle of symmetry" (theory 3) | — | — | **WRONG** (F1) |
| R6 | q1 | triple-higher | 4.7.3.3 | usable |
| R7 | q2 | triple-higher | 4.7.3.3 | **not usable as written** (F2) |
| — | equations, FIFA, RP, examiner_tip | none | — | correct: none in 4.7.3.3 |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | theory 1 | microphone converts sound energy into electrical energy by electromagnetic induction; reverse of a loudspeaker | IMPRECISE (minor) | Spec wording: "pressure variations in sound waves into variations in current". "Sound energy"/"electrical energy" are not AQA stores. | F4; 4.7.3.3 |
| C2 | theory 1 steps 1–5 | sound hits diaphragm → vibrates → attached coil moves in permanent magnet's field → generator effect → induced current alternates at the sound's frequency | OK | Matches AQA mark schemes. "emf" → say "potential difference". | 4.7.3.3; 4.7.3.1 |
| C3 | theory 1 | loudspeaker: AC in → motor effect → sound; microphone: sound → generator effect → AC out | OK | — | 4.7.2.4; 4.7.3.3 |
| C4 | theory 2 | condenser (capacitance change, phantom power), ribbon (induction), electret; frequency response, sensitivity, noise floor, polar patterns | OFF-SPEC | True in outline; omit. | F3 |
| C5 | theory 3 | output millivolts; needs preamp; ADC; 44,100 samples/s for CD | OFF-SPEC | All true (CD = 44.1 kHz ✓); omit. | F3 |
| C6 | theory 3 | "Microphones demonstrate that electromagnetic induction works in both directions: Current in magnetic field → motion (motor effect)…" | **WRONG** | The motor effect is not electromagnetic induction. Correct: the same coil-and-magnet arrangement works both ways — current in a field gives a force (motor effect, loudspeaker); movement in a field induces a pd (generator effect, microphone). | F1; 4.7.2.2; 4.7.3.1 |
| C7 | theory 3 | "Einstein's principle of symmetry — if one works, the reverse also works." | **WRONG** | No such principle; a false attribution. Delete. | F1 |
| C8 | `higher` | describe dynamic mic; compare with loudspeaker; same frequency | OK | — | 4.7.3.3 |
| C9 | common_mistake | microphone = generator effect, loudspeaker = motor effect; exact reverses; frequency of induced AC = sound frequency | OK | — | 4.7.3.3 |
| C10 | key_note | as theory; "Condenser: capacitance change method" | OK / OFF-SPEC (condenser) | — | F3 |
| C11 | q1 key | microphone: sound moves coil → generator effect → AC; loudspeaker: AC → motor effect → sound | OK | — | 4.7.3.3; 4.7.2.4 |
| C12 | q1 opt 1 / wx1 | coil size not the principle | OK | Aligned. | — |
| C13 | q1 opt 2 / wx2 | both deal with AC | OK | Aligned. | — |
| C14 | q1 opt 3 / wx3 | microphone uses generator, not motor effect | OK | Aligned. | — |
| C15 | q2 key | 440 Hz sung → 440 Hz output | OK | — | 4.7.3.3 |
| C16 | q2 opt 1 / wx1 | "Frequency doesn't double — …" | OK | Aligned. | — |
| C17 | q2 opt 2 / wx2 | "Frequency halves — the coil vibrates at the same rate as the sound, inducing AC at the same frequency." | **WRONG** (frozen text) | Opens by asserting the distractor as fact, then contradicts it. Should read: "Frequency doesn't halve — the coil vibrates at the same rate as the sound, inducing AC at the same frequency." | F2 |
| C18 | q2 opt 3 / wx3 | output ≠ 50 Hz mains; matches sound | OK | Aligned. | — |
| C19 | matching (to be replaced) | four pairs incl. condenser | OK / OFF-SPEC (condenser) | — | — |

Count: **3 WRONG** (C6, C7 — theory, re-cuttable; C17 — frozen wrong_explanation). IMPRECISE: C1. OFF-SPEC: C4, C5, C10.

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| q2 | wx2 states "Frequency halves" as fact | **Do not use as written.** Corrected wx2 in F2. |
q1 usable on TH.

## 5. Verdict
SOURCE HAS ERRORS. The microphone physics is right, but theory 3 calls the motor effect induction and invents an "Einstein's principle of symmetry", and q2's wx2 asserts the wrong answer. Theory 2–3 are mostly off-spec context.

**For Mide:** nothing — all settled facts.
