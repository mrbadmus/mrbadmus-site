# Examination — Properties of Waves (properties-of-waves) — AQA 8464 6.6.1.2 / 8463 4.6.1.2
Verdict: SOURCE OK WITH FLAGS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-17/04-checked-science-source/physics-6.6.1.2-properties-of-waves.md`.
Spec sources read as text: `AQA-8464-spec.txt` (v1.1) §6.6.1.2, §10.2.20 (RP20); `AQA-8463-spec.txt` (v1.1) §4.6.1.2, §8.2.8 (RP8); `8464-equation-sheet.txt` and `8463-equation-sheet-Jun26.txt` (June 2026), both read in full. Route audit `physics.md` row `properties-of-waves`.

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n; T1–T3 = theory chunks. All four route copies identical; no `higher` field.

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 | **6.6.1.2** | Properties of waves | base |
| 8463 | **4.6.1.2** | Properties of waves | base; one line (physics only) |
| RP | 8464 RP20 = 8463 RP8 | waves in a ripple tank and in a solid | base, all four routes |

Spec statements (verbatim, 8464 = 8463 except where marked): "Students should be able to describe wave motion in terms of their amplitude, wavelength, frequency and period. The amplitude of a wave is the maximum displacement of a point on a wave away from its undisturbed position. The wavelength of a wave is the distance from a point on one wave to the equivalent point on the adjacent wave. The frequency of a wave is the number of waves passing a point each second." "period = 1 / frequency, T = 1/f … Students should be able to apply this equation which is given on the Physics equation sheet." "The wave speed is the speed at which the energy is transferred (or the wave moves) through the medium. All waves obey the wave equation: wave speed = frequency × wavelength, v = f λ … Students should be able to recall and apply this equation." "Students should be able to: • identify amplitude and wavelength from given diagrams • describe a method to measure the speed of sound waves in air • describe a method to measure the speed of ripples on a water surface." 8463 only: "(Physics only) Students should be able to show how changes in velocity, frequency and wavelength, in transmission of sound waves from one medium to another, are inter-related."
RP (8464 RP20 = 8463 RP8): "make observations to identify the suitability of apparatus to measure the frequency, wavelength and speed of waves in a ripple tank and waves in a solid and take appropriate measurements."
Equation sheets, June 2026: **both** print T = 1/f and v = f λ.

## 2. Route table
| # | teachable point | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Amplitude, wavelength, frequency, period definitions; units (T1; key_note; common_mistake; variables) | base | 6.6.1.2 | all four | OK |
| R2 | T = 1/f (T1; equations; q1) | base | 6.6.1.2 | all four | OK — On the sheet |
| R3 | v = f λ and rearrangements; examples (T2; equations; FIFA; q2) | base | 6.6.1.2 | all four | OK — On the sheet (June 2026), recall in spec |
| R4 | EM waves 3 × 10⁸ m/s in vacuum; sound ~340 m/s (T2; key_note) | base | 6.6.2.1; context | all four | OK |
| R5 | Ripple tank method (T3; rp) | base (RP) | 6.6.1.2; RP20 / RP8 | all four | OK; RP label WRONG (F1) |
| R6 | Waves in a solid (RP's second half) | base (RP) | RP20 / RP8 | absent | GAP (F2) |
| R7 | Speed of sound in air method (T3 Method 2; rp) | base | 6.6.1.2 | all four | IMPRECISE (F3) |
| R8 | Oscilloscope trace reading (T3 exam skill) | base (MS 1c, 3b, c) | 6.6.1.2 | all four | OK |
| R9 | Sound crossing into another medium: f fixed, v and λ change | **triple** | 8463 4.6.1.2 (physics only) | absent | GAP (F4) |
| R10 | Wave speed = speed of energy transfer (definition) | base | 6.6.1.2 | absent (matching only: "distance travelled per second") | GAP, minor (F2) |
| R11 | q1 — period from frequency | base | 6.6.1.2 | all four | OK (opt 4 working incoherent, F5) |
| R12 | q2 — frequency of a radio wave | base | 6.6.1.2 | all four | OK |
| R13 | FIFA — λ = v ÷ f | base | 6.6.1.2 | all four | OK |
| — | `higher` | none | — | — | correct: 6.6.1.2 has no HT line |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | T1 | amplitude = max displacement of a particle from equilibrium (undisturbed) position; m | OK | Spec says "of a point on a wave". | 6.6.1.2 |
| C2 | T1 | "Relates to energy — larger amplitude = more energy" | OK | True; not a spec statement. Context. | — |
| C3 | T1 | wavelength: point to equivalent point on next wave; crest–crest, trough–trough, compression–compression; m | OK | — | 6.6.1.2 |
| C4 | T1 | frequency = waves passing a point per second; Hz; 1 Hz = 1 wave/s | OK | — | 6.6.1.2 |
| C5 | T1 | period = time for one complete wave to pass a point; s; T = 1/f | OK | — | 6.6.1.2 |
| C6 | T2 | v = f × λ; f = v ÷ λ; λ = v ÷ f; units | OK | — | 6.6.1.2 |
| C7 | T2 | Ex 1: 440 Hz, 340 m/s → λ = 0.77 m | OK | 340 ÷ 440 = 0.7727 ✓ | — |
| C8 | T2 | Ex 2: λ = 0.1 m → f = 3 × 10⁹ Hz = 3 GHz, microwave | OK | 3×10⁸ ÷ 0.1 = 3×10⁹ ✓; microwave band ✓ | 6.6.2.1 |
| C9 | T2 | all EM waves same speed in vacuum, 3 × 10⁸ m/s; sound in air ~340 m/s | OK | Spec says "vacuum (space) or air". | 6.6.2.1 |
| C10 | T3 heading; key_note; rp | "REQUIRED PRACTICAL (RP19)", "RP19: measure wave speed in ripple tank" | WRONG | 8464 **RP20**; 8463 **RP8**. 8464 RP19 is force and acceleration. | 8464 6.6.1.2; 8463 4.6.1.2 (F1) |
| C11 | T3 Method 1 | stroboscope to freeze; wavelength from still image; frequency from vibrating-bar setting; v = fλ | OK | Standard method. Add the measurement technique: measure across several (e.g. 10) wavelengths on the shadow pattern and divide; count waves passing a point in a timed interval (e.g. 10 s) for f. | RP20 / RP8 |
| C12 | T3 | (absent) waves in a solid | GAP | RP covers "waves in a solid": vibration generator drives a string/elastic cord over a pulley; adjust f for a stationary pattern; measure the length of several half-wavelengths to find λ; f from the signal generator; v = fλ. | RP20 / RP8 (F2) |
| C13 | T3 Method 2 | microphone + oscilloscope: measure T, f = 1/T; "Using two microphones and measuring time delay to find speed" | IMPRECISE | Measuring T gives f, not speed. Speed needs a distance: either (a) two microphones a measured distance apart, time delay from the trace, v = distance ÷ time; or (b) move one microphone until the two traces line up again — that distance is one λ, v = fλ. A simpler accepted method: an observer a measured distance (e.g. 100 m+) away times from seeing two blocks clapped to hearing the clap, v = s ÷ t. | 6.6.1.2 "describe a method to measure the speed of sound waves in air" (F3) |
| C14 | T3 | time/div → T → f = 1/T; volts/div → amplitude | OK | — | MS 1c, 3b, c |
| C15 | common_mistake | amplitude = centre to crest, not crest to trough; f and T reciprocals | OK | — | 6.6.1.2 |
| C16 | key_note | definitions; v = fλ; c; ~340 m/s; "RP19" | OK except RP number | See C10. | — |
| C17 | equations | v = f × λ; T = 1 ÷ f | OK | Both On the sheet (8464 and 8463, June 2026). | sheets |
| C18 | FIFA | 500 Hz, 340 m/s → λ = 340 ÷ 500 = 0.68 m | OK | ✓ | — |
| C19 | FIFA Convert `[NEW]` | "Nothing to convert — speed is already in m/s and frequency already in Hz, so λ = v ÷ f gives an answer directly in metres with no unit change." | OK | Examined ✓. CFIFA's second worked example needs a conversion: kHz → Hz, or cm → m. | CFIFA amendment |
| C20 | variables | v m/s; f Hz; λ m; T s; A m | OK | — | 6.6.1.2 |
| C21 | q1 key | 200 Hz → T = 1/200 = 0.005 s | OK | ✓ | — |
| C22 | q1 opt 2 / wx1 | 200 s — T is not f; reciprocals | OK | Aligned. | — |
| C23 | q1 opt 3 / wx2 | 20 s — T = f ÷ 10; "T = 1/f not f/10" | OK | 200 ÷ 10 = 20 ✓. Aligned. | — |
| C24 | q1 opt 4 / wx3 | "0.1 s — T = 1/10 of the frequency" | IMPRECISE | The option's working does not give its number (1/10 of 200 = 20, not 0.1). The value is still wrong, so the item stands; wx3 is aligned. | (F5) |
| C25 | q2 key | λ = 3 m → f = 3×10⁸ ÷ 3 = 1×10⁸ Hz | OK | ✓ (100 MHz, FM radio) | — |
| C26 | q2 opt 2 / wx1 | 9×10⁸ — multiplied | OK | 3×10⁸ × 3 = 9×10⁸ ✓. Aligned. | — |
| C27 | q2 opt 3 / wx2 | 1×10⁻⁸ — inverted | OK | 3 ÷ 3×10⁸ = 1×10⁻⁸ ✓. Aligned. | — |
| C28 | q2 opt 4 / wx3 | f ≠ v | OK | Aligned. | — |
| C29 | matching (to be replaced) | five pairs | OK | "Distance from one crest to the next" ✓. | — |

Count: **1 WRONG** (RP number, F1, in theory 3, key_note and `rp`); **IMPRECISE**: C13, C24; **GAP**: C12, physics-only sound inter-relation, wave-speed definition. All 8 calculations rechecked ✓.

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| `rp` field | RP number wrong; ripple tank only, no "waves in a solid" | Show as Combined RP20 / Physics RP8; add the solid (F1, F2). |
| q1, q2 | none wrong | Usable on all four routes. |

## 5. For the lesson author
**Misconceptions seen in AQA marking**
- Amplitude measured crest to trough.
- Wavelength measured crest to trough (half a wavelength), or across the whole diagram.
- T = 1/f inverted or f confused with T.
- kHz / MHz / cm not converted.
- In the ripple-tank RP: measuring one wavelength rather than several and dividing; not saying how f was found.
- "Higher frequency makes the wave faster" (in a given medium v is fixed; λ falls).

**Command words**: Define, Calculate, Write down the equation (v = fλ — recall list), Describe a method, Identify (from a diagram), Explain (an improvement to the method).

**Typical questions** ⚑ examiner-drafted
- *Write down the equation that links frequency, wavelength and wave speed. [1]* — v = f λ.
- *A wave has a frequency of 2.5 kHz and a wavelength of 0.14 m. Calculate its speed. [3]* — 2500 Hz (1); v = 2500 × 0.14 (1); = 350 m/s (1).
- *Describe a method to measure the speed of ripples on a water surface. [6]* — ripple tank, stroboscope/photo; measure across 10 wavelengths with ruler and ÷ 10; count waves passing a point in 10 s for f; v = fλ; repeat and average.
- *Describe a method to measure the speed of sound in air. [4]* — measure a large distance; time from seeing to hearing a clap; repeat and average; v = distance ÷ time.

**Required practical**: Combined RP20 / Physics RP8 (8464 6.6.1.2; 8463 4.6.1.2), all four routes. Ripple tank **and** waves in a solid.

**Equations**: v = f λ — **On the sheet** (both June 2026 sheets; the spec's recall list still has it — "Write down the equation" questions are worth training). T = 1/f — **On the sheet**. Supporting s = v t for the speed-of-sound method — On the sheet (both).

## 6. Verdict
SOURCE OK WITH FLAGS. All science and arithmetic correct; both quiz items usable on all routes. The RP is wrongly numbered "RP19" in three places (true: Combined RP20 / Physics RP8); the RP's waves-in-a-solid half is missing; the sound-speed method is muddled; the physics-only sound-between-media point is missing.

**For Mide:** none.
