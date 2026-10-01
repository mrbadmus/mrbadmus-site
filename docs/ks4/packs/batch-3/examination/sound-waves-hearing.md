# Examination — Sound Waves and Hearing (sound-waves-hearing) — AQA 8463 4.6.1.4 (physics only, HT only) / not in 8464
Verdict: SOURCE OK WITH FLAGS — but the pack teaches the wrong spec point
Examiner: Opus, 1 Oct 2026. Pack examined: `docs/ks4/packs/batch-3/physics-8463-4.6.1.4-sound-waves-hearing.md`.
Spec sources fetched from filestore.aqa.org.uk and read as text: AQA-8463-SP-2016.PDF (v1.1, 30 Sep 2019) incl. Appendix A; AQA-8464-SP-2016.PDF (v1.1, 04 Oct 2019) — searched in full: 6.6.1 has 6.6.1.1 (transverse and longitudinal) and 6.6.1.2 (properties of waves) only; no sound-and-hearing section. Both June 2026 equation sheets read in full. Mark-scheme conventions from examiner knowledge of AQA 8463 papers 2018–2024; not fetched.

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n. One route copy (TH).

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8463 | **4.6.1.4** | Sound waves | **physics only, HT only** |
| 8464 | **not in 8464** | — | — |
| Supporting | 8463 4.6.1.2 (physics only, base tier): "show how changes in velocity, frequency and wavelength, in transmission of sound waves from one medium to another, are inter-related"; 8464 6.6.1.1 / 8463 4.6.1.1 "Sound waves travelling through air are longitudinal" | | |
| Where most of the pack belongs | 8463 **4.6.1.5** Waves for detection and exploration (physics only, HT only) — ultrasound, echo sounding (lesson `waves-detection-exploration`) | | |

**Is the whole subtopic really HT? Yes.** The 8463 heading reads verbatim "4.6.1.4 Sound waves (physics only) (HT only)". The data's `spec` field ("6.6.1.4 (HT only, physics only)") has the right labels but the **wrong number**: there is no 6.6.1.4 in 8464; the reference is 8463 4.6.1.4. The route (Triple Higher only) is correct.

Spec statement (verbatim, 8463 4.6.1.4 — the whole of it): "Sound waves can travel through solids causing vibrations in the solid. Within the ear, sound waves cause the ear drum and other parts to vibrate which causes the sensation of sound. The conversion of sound waves to vibrations of solids works over a limited frequency range. This restricts the limits of human hearing. Students should be able to: • describe, with examples, processes which convert wave disturbances between sound waves and vibrations in solids. Examples may include the effect of sound waves on the ear drum • explain why such processes only work over a limited frequency range and the relevance of this to human hearing. Students should know that the range of normal human hearing is from 20 Hz to 20 kHz."

**The pack's coverage problem.** Of the pack's three theory blocks, two (ultrasound uses, SONAR, d = vt/2) and both quiz items and the FIFA are **4.6.1.5** content. The pack never describes the conversion of sound into vibrations of a solid (ear drum, small bones), never explains *why* the conversion works only over a limited frequency range, and never gives an example other than the ear (e.g. a microphone diaphragm, a loudspeaker cone, sound making a window or table vibrate). Those are the whole of 4.6.1.4. Both lessons are TH-only, so nothing is route-wrong — but the author must write 4.6.1.4 from the spec, and the two lessons must divide the ultrasound material between them rather than both teach it.

## 2. Route table
| # | teachable point | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Sound is longitudinal; compressions and rarefactions; needs a medium (theory 1; key_note) | base (prior knowledge) | 6.6.1.1 / 4.6.1.1 | TH | OK |
| R2 | Sound travels through solids causing vibrations in the solid | triple-higher | 4.6.1.4 | — | **Missing** |
| R3 | Ear: sound waves make the ear drum and other parts vibrate → sensation of sound | triple-higher | 4.6.1.4 | — | **Missing** |
| R4 | Examples of sound ↔ vibration conversion (ear drum, microphone, loudspeaker) | triple-higher | 4.6.1.4 | — | **Missing** |
| R5 | Conversion only works over a limited frequency range → limits of hearing | triple-higher | 4.6.1.4 | — (theory 2 states the range, never the reason) | **Missing** |
| R6 | Human hearing 20 Hz–20 kHz (theory 1, 2; key_note) | triple-higher | 4.6.1.4 | TH | OK |
| R7 | Speed of sound different in different media; f unchanged, v and λ change (theory 1) | **triple** (base tier) | 4.6.1.2 (physics only) | TH | OK on TH; the f-constant / λ-changes link is **missing**. Lives in `properties-of-waves` for TF. |
| R8 | Ultrasound > 20 kHz; partial reflection at boundaries; timing → distance; medical and industrial imaging (theory 2, 3; q1, q2; FIFA; equations) | triple-higher | **4.6.1.5** | TH | Route OK; **wrong lesson** — belongs to `waves-detection-exploration` |
| R9 | SONAR / echo sounding (theory 3; FIFA; q1) | triple-higher | **4.6.1.5** | TH | As R8 |
| R10 | Pitch ↔ frequency; loudness ↔ amplitude; decibels; infrasound; animals; echo > 0.1 s; cleaning; echocardiography | NOT-IN-SPEC (context) | — | TH | Context only |
| R11 | `higher` field ("HT only — …") | — | — | TH | Redundant — the whole page is HT; do not render a separate Higher block |
| — | RP | none | none | — | correct |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | theory 1 | sound waves are longitudinal mechanical waves; compressions and rarefactions; cannot travel through a vacuum | OK | — | 4.6.1.1 |
| C2 | theory 1 | higher frequency → higher pitch; larger amplitude → louder; decibels | OK, NOT-IN-SPEC | — | — |
| C3 | theory 1, 2 | human hearing ≈ 20 Hz to 20 kHz; infrasound < 20 Hz; ultrasound > 20 kHz | OK | Spec: "20 Hz to 20 kHz"; ultrasound "higher than the upper limit of hearing" (4.6.1.5). "Infrasound" is not an AQA term. | 4.6.1.4; 4.6.1.5 |
| C4 | theory 1 | air ~340 m/s; water ~1500 m/s; solids faster | OK | Typical values (air 330–340 m/s). | — |
| C5 | theory 1 | water faster "because particles closer together"; solids "densest medium, most efficient transmission"; "Sound travels faster in denser media (unlike EM waves …)" | **WRONG** | The ordering solid > liquid > gas is generally right, but **density is not the reason, and "denser → faster" is false as a rule**: speed depends on the stiffness of the material relative to its density. Denser materials of similar stiffness carry sound *more slowly* (lead ≈ 1200 m/s vs aluminium ≈ 6400 m/s; sound is slower in CO₂ than in air, faster in helium). Correct: "Sound usually travels fastest in solids and slowest in gases, because the particles are more strongly linked (closer together and held by stronger forces), so vibrations pass on more quickly." AQA mark schemes credit "particles closer together" for solid vs gas comparisons, never "denser so faster". | — |
| C6 | theory 1 | echo heard when reflection arrives > 0.1 s after the original | OK, NOT-IN-SPEC | Approximate psychoacoustic figure. | — |
| C7 | theory 2 | upper limit decreases with age | OK | — | — |
| C8 | theory 2 | "Most sensitive around 2–5 kHz (conversational speech frequencies)" | IMPRECISE, NOT-IN-SPEC | Peak sensitivity ~2–5 kHz is right; speech's fundamental frequencies are mostly 100–300 Hz (consonant detail extends to 2–4 kHz). Drop the bracket. | — |
| C9 | theory 2 | infrasound: earthquakes, volcanoes, ocean waves; elephants and whales communicate; humans feel very low frequencies | OK, NOT-IN-SPEC | — | — |
| C10 | theory 2 | "Animals that use ultrasound: bats (echolocation), dolphins, dogs" | IMPRECISE | Dogs **hear** ultrasound; they do not use it to echolocate. | — |
| C11 | theory 2 | medical ultrasound: partially reflected at tissue boundaries; timing → depth; d = v × t/2; builds an image; no ionising radiation; foetal, soft tissue, stones | OK | 4.6.1.5 content. "No ionising radiation" — standard AQA credit. | 4.6.1.5 |
| C12 | theory 3 | SONAR; d = (v × t)/2; industrial crack detection; cleaning; pregnancy scanning; echocardiography | OK | Crack detection = "industrial imaging" (4.6.1.5); cleaning, echocardiography NOT-IN-SPEC. | 4.6.1.5 |
| C13 | theory 3 | "divide by 2 because the pulse travels to the boundary AND back" | OK | — | 4.6.1.5 |
| C14 | `higher` | "HT only — calculate distance using d = vt/2; ultrasound vs X-rays; echolocation and SONAR quantitatively" | OK / redundant | Whole page is HT. | — |
| C15 | common_mistake | divide time by 2; "Sound travels FASTER in denser media (solid > liquid > gas) — opposite to EM waves" | **WRONG** (second sentence) | As C5. Replace with "Sound usually travels fastest in solids and slowest in gases". | — |
| C16 | key_note | longitudinal, needs medium; 20 Hz–20 kHz; speed solid > liquid > gas; ultrasound uses; d = vt/2 | OK | Missing the 4.6.1.4 core (ear drum vibrates; limited range). | 4.6.1.4 |
| C17 | equations | "d = v × t / 2 (distance to reflecting surface)" | IMPRECISE | Not an AQA equation. AQA's equation is **s = v t** (recall list eq 6; printed on both June 2026 sheets as "distance travelled = speed × time"); the halving is method. Equation card: s = v t; method chip "distance to the boundary = half the distance travelled". | App. A eq 6 |
| C18 | FIFA | echo 0.06 s, v = 1500 m/s: d = 1500 × 0.06 / 2 = 45 m | OK | 1500 × 0.06 = 90; ÷ 2 = 45 ✓. CFIFA Convert: "nothing to convert". Conversion example: echo time in **ms** (e.g. 80 ms → 0.080 s). This FIFA is 4.6.1.5 content. | 4.6.1.5 |
| C19 | q1 key | divide by 2: pulse travels to the surface and back | OK | — | 4.6.1.5 |
| C20 | q1 wx1–wx3 | speed unchanged; energy loss affects amplitude not timing; no fixed delay | OK | — | — |
| C21 | q2 key | ultrasound non-ionising; doesn't damage cells/DNA like X-rays can; safe for the baby | OK | — | 4.6.1.5; 6.6.2.3 |
| C22 | q2 wx1 | "X-rays actually produce higher resolution images — but the ionising radiation risk outweighs this" | OK | Broadly true for a radiograph; harmless. | — |
| C23 | q2 wx2 | "X-rays DO penetrate soft tissue (though not as well as bone) — but they are not used because of ionising radiation risk" | **WRONG** | Reversed. X-rays pass through soft tissue **more** easily than through bone (bone absorbs more — which is why bones show up). The bracket says the opposite. Correct: "X-rays DO pass through soft tissue — more easily than through bone — but they are not used because of the ionising radiation risk to the fetus (and soft tissue shows little contrast on an X-ray)." | 6.6.2.2 (absorption varies by material) |
| C24 | q2 wx3 | cost and speed secondary; safety primary | OK | — | — |
| C25 | matching (to be replaced) | 4 pairs | OK | — | — |

Count: **3 WRONG** — C5 and C15 ("denser → faster", theory and common_mistake; re-cuttable) and **C23 (frozen q2 wx2)**. **IMPRECISE**: C8, C10, C17. All arithmetic ✓.

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| TH · q2 · "Why is ultrasound used for foetal scanning rather than X-rays?" — wx2 | Keyed answer correct; wx2 states that X-rays penetrate bone better than soft tissue (C23). Wrong on its only route. Also 4.6.1.5 content, not 4.6.1.4. | **Withhold until wx2 is corrected** (DEPARTURES, text in C23). Then move to `waves-detection-exploration`'s ladder (TH) rather than this one. |
| TH · q1 · "Why must you divide the echo time by 2 in SONAR calculations?" | Correct; 4.6.1.5 content. | Keep (TH). Prefer it on `waves-detection-exploration`'s ladder; usable here only if the lesson keeps a short ultrasound bridge. |
| FIFA · SONAR distance | Correct; 4.6.1.5. Duplicates the detection lesson's q2 method. | Keep (TH); best placed in `waves-detection-exploration`, which has no FIFA of its own. |
| `equations` field · "d = v × t / 2" | Not an AQA equation (C17). | Keep as data; render s = v t on the card. |

This lesson then has **no correct, in-section frozen ladder item** for 4.6.1.4 itself — the ear/limited-range ladder rungs must all be newly written (examiner-drafted below).

## 5. For the lesson author
**Misconceptions seen in AQA marking**
- "The ear drum hears the sound" — the sensation is produced when vibrations are passed on (small bones → cochlea → nerve impulses); the ear drum is where sound waves become vibrations of a solid.
- Why a limited range: answers say "the ear is too small" or "the brain can't process it". AQA wants: the ear drum (and the parts behind it) can only vibrate in response to — be made to vibrate by — sound waves in a certain frequency range; outside it, they do not vibrate (enough) to produce the sensation.
- "Sound travels faster in denser materials" (C5) and "sound travels fastest in a vacuum".
- Physics-only 4.6.1.2: "frequency changes when sound enters water" — the **frequency stays the same**, the speed changes, so the wavelength changes in proportion.
- Units: kHz not converted (20 kHz = 20 000 Hz).
- Air particles "travel from the source to the ear" — the particles vibrate about fixed positions; the energy travels.

**Command words**: Describe (with examples), Explain, State (the range of human hearing), Give, Calculate (v = fλ across a medium change).

**Typical questions** ⚑ examiner-drafted
- *State the range of normal human hearing. [1]* — 20 Hz to 20 kHz (both limits needed).
- *Describe how a sound wave in the air causes a sensation of sound. [3]* — sound waves (compressions/rarefactions) reach the ear drum (1); cause the ear drum to vibrate (1); the vibrations are passed through the other parts of the ear (small bones/cochlea) causing the sensation of sound (1).
- *Explain why humans cannot hear a sound of frequency 40 kHz. [2]* — the conversion of sound waves to vibrations of the ear drum (solids in the ear) only works over a limited range of frequencies (1); 40 kHz is above the upper limit of 20 kHz, so the ear drum does not vibrate (enough) to cause the sensation of sound (1).
- *Give one example, other than the ear, where sound waves are converted into vibrations of a solid. [1]* — e.g. a microphone diaphragm; a window rattling from a passing lorry; a cup on a speaker.
- *(Physics-only, 4.6.1.2 link.) A sound wave of frequency 500 Hz passes from air (330 m/s) into water (1500 m/s). Calculate its wavelength in water and state what happens to its frequency. [3]* — frequency stays 500 Hz (1); λ = 1500 ÷ 500 (1); = 3.0 m (1).
- *Explain why sound travels faster in a solid than in a gas. [2]* — particles in a solid are closer together / strongly bonded (1); so vibrations are passed from particle to particle more quickly (1). (Do **not** credit "because it is denser".)
- 6-markers are rare on 4.6.1.4; the HT ultrasound/seismic 6-marker belongs to 4.6.1.5.

**Required practical**: none. (RP8 Triple / RP20 Combined, waves in a ripple tank and a solid, sits at 4.6.1.2 / 6.6.1.2.)

**Equations**: none in 4.6.1.4. Supporting: v = f λ — **learn it** per the spec recall list (eq 16), **printed on both June 2026 sheets**; s = v t (for echo questions, 4.6.1.5) — recall list eq 6, printed on both June 2026 sheets. "d = v t / 2" is not an AQA equation.

## 6. Verdict
SOURCE OK WITH FLAGS — but the source does not cover its own spec point. The route is right (8463 4.6.1.4 is genuinely Physics-only **and** HT-only, so Triple Higher only; not in 8464). The data's `spec` number "6.6.1.4" is wrong — 8463 4.6.1.4. Almost all of the pack (ultrasound, SONAR, both quiz items, the FIFA) is 4.6.1.5 content and duplicates `waves-detection-exploration`; the 4.6.1.4 core — sound becoming vibrations in solids, the ear drum, why the conversion only works over a limited range — is absent and must be written from the spec. Two wrong statements: "sound travels faster in denser media" (theory and common_mistake) and frozen q2 wx2 (X-rays said to penetrate bone better than soft tissue — withhold until corrected).

**For Mide:** none. (The spec is unambiguous; 8464 has no counterpart.)
