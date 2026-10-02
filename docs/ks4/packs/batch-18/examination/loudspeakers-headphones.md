# Examination — Loudspeakers and Headphones (loudspeakers-headphones) — AQA 8463 4.7.2.4
Verdict: SOURCE OK WITH FLAGS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-18/04-checked-science-source/physics-6.7.2.4-loudspeakers-headphones.md`.
Spec sources read as text: `AQA-8463-spec.txt` (v1.1, 30 Sep 2019) §4.7.2.1–4.7.2.4; `AQA-8464-spec.txt` (v1.1, 04 Oct 2019) §6.7 (no loudspeaker content); both June 2026 equation sheets. Route audit `ks4-routes/docs/ks4/route-audit/physics.md` row 85.

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n; option indices 0–3 as stored. One route copy (TH).

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8463 | **4.7.2.4** | Loudspeakers | **(physics only) (HT only)** |
| 8464 | — | not in Combined | — |
| Supporting | 8463 4.7.2.2 / 8464 6.7.2.2 Fleming's left-hand rule, F = BIl (HT only); 8463 4.7.2.1 "(Physics only) interpret diagrams of electromagnetic devices"; 8463 4.6.1.4 Sound waves (physics only)(HT only) — sound ↔ vibrations of solids. Pitch ↔ frequency and loudness ↔ amplitude are KS3 prior knowledge (not restated in 8463), used by q2 | | |

Spec statements (verbatim, 8463 4.7.2.4): "Loudspeakers and headphones use the motor effect to convert variations in current in electrical circuits to the pressure variations in sound waves." "Students should be able to explain how a moving-coil loudspeaker and headphones work."

## 2. Route table
| # | teachable point | true layer | spec | verdict |
|---|---|---|---|---|
| R1 | Loudspeaker uses the motor effect; magnet + coil + cone; AC → force reverses → cone vibrates → compressions/rarefactions (theory 1; common_mistake; key_note; `higher`) | triple-higher | 8463 4.7.2.4 | OK |
| R2 | Sound frequency = AC frequency; larger current → louder (theory 1; q2) | triple-higher | 8463 4.7.2.4 | OK (C4 imprecise) |
| R3 | Why AC, not DC (q1; `higher`) | triple-higher | 8463 4.7.2.4 | OK |
| R4 | Moving-coil headphones: same principle, smaller (theory 2 first half) | triple-higher | 8463 4.7.2.4 | OK |
| R5 | Electrostatic and balanced-armature headphones; impedance (theory 2) | not in spec | — | OFF-SPEC (F2) |
| R6 | Energy transfers, efficiency 1–5 %, woofer/tweeter, frequency response (theory 3) | not in spec (context) | — | OFF-SPEC / IMPRECISE (F1, F2) |
| R7 | q1 | triple-higher | 4.7.2.4 | usable |
| R8 | q2 | triple-higher (pitch/loudness links are KS3 prior knowledge) | 4.7.2.4 | usable (extraction flag cleared, F4) |
| — | equations, FIFA, RP, examiner_tip | none | — | correct: 4.7.2.4 has none |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | theory 1 | loudspeaker converts electrical energy (AC) into sound using the motor effect | OK | Spec wording is "variations in current … to pressure variations in sound waves". | 4.7.2.4 |
| C2 | theory 1 | permanent magnet, voice coil, cone | OK | — | 4.7.2.4 |
| C3 | theory 1 steps 1–5 | AC in coil in magnet's field → force; AC reverses → force reverses → coil and cone move back and forth → compressions and rarefactions | OK | Matches AQA mark schemes (current in coil, in magnetic field, force on coil, current alternates so force changes direction, cone vibrates, pressure variations). | 4.7.2.4; 4.7.2.2 |
| C4 | theory 1 | "AMPLITUDE (loudness) ∝ amplitude of current" | IMPRECISE | Proportionality is not claimed by the spec and is not true across a real speaker's range. Say: larger current → larger force → larger vibrations → louder. | F3 |
| C5 | theory 1 | frequency of sound = frequency of AC | OK | — | 4.7.2.4 |
| C6 | theory 2 | headphones: same principle, miniaturised; smaller diaphragm | OK | — | 4.7.2.4 |
| C7 | theory 2 | electrostatic headphones; balanced armature; impedance matching | OFF-SPEC | True in outline, not examinable; spec names moving-coil only. Omit. | F2 |
| C8 | theory 3 | electrical → kinetic → sound energy; some thermal | IMPRECISE | AQA does not use "sound energy" or "electrical energy" as stores. Say: energy transferred electrically to the kinetic store of the coil and cone, then transferred by sound waves; some dissipated to the thermal store of the coil. | 8463 4.1.1.1 |
| C9 | theory 3 | typical efficiency 1–5 % | IMPRECISE / OFF-SPEC | Most domestic speakers are nearer 0.5–2 %; not examinable. Omit. | F2 |
| C10 | theory 3 | woofer large cone for bass; tweeter small for treble; subwoofer < 200 Hz | OFF-SPEC | True; context only. | F2 |
| C11 | common_mistake | motor effect drives the cone; AC reverses force; sound frequency = AC frequency | OK | — | 4.7.2.4 |
| C12 | key_note | as theory | OK (C8 wording) | — | — |
| C13 | `higher` | "HT only" | OK | True label is (physics only)(HT only); page is TH-only so it is a statement of the whole page. | 4.7.2.4 |
| C14 | q1 key | DC → constant force, cone deflects once and stops; AC reverses force → vibration | OK | — | 4.7.2.4 |
| C15 | q1 wx1 | AC and DC can provide the same power; reason is direction | OK | — | — |
| C16 | q1 wx2 | DC heating a concern, but fundamental reason is unidirectional force | OK | — | — |
| C17 | q1 wx3 | resonance only at specific frequencies; speaker responds to all | OK | Aligned with option 3. | — |
| C18 | q2 key | loud, low-pitched → low frequency, large amplitude | OK | — | 4.7.2.4; pitch ↔ frequency, loudness ↔ amplitude is KS3 prior knowledge |
| C19 | q2 opt 1 / wx1 | "High frequency (low pitch) and large amplitude (loud)"; wx1 "Low pitch = LOW frequency AC — high frequency would produce a high-pitched sound" | OK — extraction flag cleared | The parenthetical is the misconception being tested (pupil believes high frequency gives low pitch); wx1 corrects exactly that. Options 2 and 3 are built the same way (opt 2 pairs "small amplitude" with "loud"; opt 3 swaps the two links). Every option repeats the stem's words "low pitch" and "loud", so the pupil must judge the quantities, not match words. Coherent item. | F4 |
| C20 | q2 opt 2 / wx2 | small amplitude → quiet | OK | Aligned. | — |
| C21 | q2 opt 3 / wx3 | loudness from amplitude; frequency → pitch | OK | Aligned (swapped links). | — |
| C22 | matching (to be replaced) | four pairs | OK | All correct. | — |

Count: **0 WRONG**; IMPRECISE: C4, C8, C9; OFF-SPEC: C7, C9, C10. No calculation in the lesson.

## 4. Frozen items wrong for their route
None. q1 and q2 are both correct and triple-higher; **both usable on TH**.

## 5. Gaps
The spec asks for headphones as well as loudspeakers; the source covers moving-coil headphones in two lines (enough). The spec phrase "pressure variations in sound waves" should be the lesson's own wording for the output (C1).

## 6. Verdict
SOURCE OK WITH FLAGS. Core physics right; both quiz items usable. Theory 2 (headphone types) and most of theory 3 are off-spec context to cut; energy wording to be put in AQA stores language. The extraction's q2 flag is not a defect (C19).

**For Mide:** nothing.
