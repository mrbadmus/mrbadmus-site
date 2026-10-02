# Examination — Wave Front Diagrams and Refraction (wave-front-refraction) — AQA 8464 6.6.2.2 (HT) / 8463 4.6.2.2 (HT)
Verdict: SOURCE OK WITH FLAGS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-17/04-checked-science-source/physics-6.6.2-wave-front-refraction.md`.
Spec sources read as text: `AQA-8464-spec.txt` (v1.1) §6.6.1.2, §6.6.2.2–6.6.2.4; `AQA-8463-spec.txt` (v1.1) §4.6.1.2, §4.6.1.5, §4.6.2.2–4.6.2.4. Route audit `physics.md` row `wave-front-refraction` and move list item 5. Batch-3 `waves-detection-exploration` (seismic), for boundaries.

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n; T1–T3 = theory chunks. One route copy (TH).

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 | **6.6.2.2** | Properties of electromagnetic waves 1 — wave-front line | (HT only) |
| 8463 | **4.6.2.2** | Properties of electromagnetic waves 1 — wave-front line | (HT only) |
| Also used | 8464 6.6.2.3 / 8463 4.6.2.3 radio production and absorption | | (HT only) — home is `properties-em-waves-2` |
| Also used | 8463 4.6.1.5 seismic P-waves | | (physics only)(HT only) — home is `waves-detection-exploration` |
| Also used | 8463 4.6.1.2 inter-relation of v, f, λ between media (sound) | | (physics only) |

The data's spec "6.6.2 (HT only)" is not a real section number; the true refs are 8464 6.6.2.2 (HT only) and 8463 4.6.2.2 (HT only). Neither line is physics-only.

Spec statements (verbatim, 8464 = 8463): "(HT only) Students should be able to use wave front diagrams to explain refraction in terms of the change of speed that happens when a wave travels from one medium to a different medium." "(HT only) Some effects, for example refraction, are due to the difference in velocity of the waves in different substances." 6.6.2.3: "(HT only) Radio waves can be produced by oscillations in electrical circuits. (HT only) When radio waves are absorbed they may create an alternating current with the same frequency as the radio wave itself, so radio waves can themselves induce oscillations in an electrical circuit."

## 2. Route table
| # | teachable point | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Wave front: line joining points in step (crests); ⊥ direction of travel; plane and circular (T1; key_note; common_mistake) | higher | 6.6.2.2 (HT only) | TH | OK; one imprecise line (F3) |
| R2 | Refraction by wave fronts: one part enters first and slows → front pivots (T1, T2; key_note; `higher`) | higher | 6.6.2.2 (HT only) | TH | OK |
| R3 | f constant; v and λ change; v = fλ (T2; common_mistake; equations; q1) | higher | 6.6.2.2 (HT only); 6.6.1.2 | TH | OK |
| R4 | Seismic P-wave paths curve (T2) | triple-higher | 8463 4.6.1.5 (physics only)(HT only) | TH | IMPRECISE + ROUTE after the move (F2) |
| R5 | Radio waves from oscillating circuits; absorbed → AC same frequency (T3; key_note; `higher`; q2) | higher | 6.6.2.3 (HT only) | TH | OK; duplicates `properties-em-waves-2` (F4) |
| R6 | Ionosphere refraction of radio waves (T3) | off-spec context | — | TH | OK as context (F5) |
| R7 | q1 — wavelength and frequency entering glass | higher | 6.6.2.2 (HT only) | TH | OK |
| R8 | q2 — how radio waves are produced | higher | 6.6.2.3 (HT only) | TH | OK |
| — | Page as a whole | **higher (CH TH)**, not triple-higher | 6.6.2.2 (HT only) — no "(physics only)" label | site ships TH | ROUTE (F1) — moving under the route-flag PR |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | T1 | wave front = line joining points at the same phase (e.g. crests) | OK | "phase" not a spec word: say "points that are in step, e.g. all the crests". | — |
| C2 | T1 | wave fronts ⊥ direction of travel | OK | — | — |
| C3 | T1 | plane waves: parallel lines; circular: concentric circles | OK | — | — |
| C4 | T1 | "Frequency and wavelength shown by spacing between lines" | IMPRECISE | Spacing shows wavelength only; a still diagram cannot show frequency. | (F3) |
| C5 | T1 | closer fronts = shorter λ / bunching as wave slows; further apart = longer λ | OK | — | 6.6.2.2 (HT) |
| C6 | T1 | part of front enters first → slows first → front pivots → direction changes | OK | The spec's mechanism. | 6.6.2.2 (HT) |
| C7 | T2 | slows: fronts bunch, towards normal; speeds up: spread, away | OK | — | 6.6.2.2 (HT) |
| C8 | T2 | frequency doesn't change; v = fλ → λ decreases | OK | — | 6.6.1.2; 6.6.2.2 |
| C9 | T2 | light entering glass: slower, towards normal, λ shortens, f unchanged, "eye perceives the same colour" | OK | — | — |
| C10 | T2 | "P-waves travel faster in denser rock. As P-waves descend through Earth, density increases → speed increases → waves curve upward." | IMPRECISE | P-wave speed does increase with depth through the mantle, so paths curve (concave upward) — correct. The cause is rock stiffness/incompressibility rising with depth, not density (higher density alone would slow the wave). Say "P-waves speed up as they go deeper, so their paths curve". Triple-higher content. | 8463 4.6.1.5 (F2) |
| C11 | T3 | radio produced by oscillating current in an aerial; f(radio) = f(oscillation) | OK | — | 6.6.2.3 (HT) |
| C12 | T3 | absorbed radio wave drives electrons → AC at the same frequency; basis of receivers | OK | — | 6.6.2.3 (HT) |
| C13 | T3 | radio refracts in the ionosphere, bent back to Earth; frequency-dependent | OK | Correct physics; not on the spec. | (F5) |
| C14 | `higher` | wave-front diagrams; change of speed; radio production/induction | OK | — | 6.6.2.2; 6.6.2.3 (HT) |
| C15 | common_mistake | f constant; λ ∝ v at fixed f; fronts ⊥ travel; closer = shorter λ, "not higher frequency" | OK | — | — |
| C16 | key_note | as above | OK | — | — |
| C17 | equations | v = f × λ (f unchanged in refraction) | OK | On the sheet (8464 and 8463, June 2026). | sheets |
| C18 | q1 key | λ decreases, f same; v = fλ | OK | — | 6.6.2.2 (HT) |
| C19 | q1 opt 2 / wx1 | waves arriving per second = waves leaving; f set by source | OK | Aligned. | — |
| C20 | q1 opt 3 / wx2 | "loses some energy (absorbed) but the frequency … remains unchanged" | OK | Aligned (addresses the frequency half; the λ half of the option is right). | — |
| C21 | q1 opt 4 / wx3 | direction and λ change; only f preserved | OK | Aligned. | — |
| C22 | q2 key | oscillating currents in an aerial; f(oscillation) = f(wave) | OK | — | 6.6.2.3 (HT) |
| C23 | q2 opt 2 / wx1 | hot metals emit IR and visible, not radio | OK | Fine at GCSE (thermal radio emission is negligible). Aligned. | — |
| C24 | q2 opt 3 / wx2 | nuclear decay gives alpha, beta, gamma, not radio | OK | Aligned. | 6.6.2.3 (gamma from nucleus) |
| C25 | q2 opt 4 / wx3 | spinning magnets → AC; the current in an aerial produces the waves | OK | Aligned. | — |
| C26 | matching (to be replaced) | four pairs | OK | — | — |

Count: **0 WRONG**. **IMPRECISE**: C4, C10. **ROUTE**: page should be CH TH (F1); seismic content TH-only after the move (F2). No calculations required by the spec line.

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| None wrong. | q1 and q2 are HT, not physics-only. | Both usable on CH and TH once the page moves. |

## 5. For the lesson author
**Misconceptions seen in AQA marking**
- Wave fronts drawn parallel to the direction of travel (they are at right angles to it).
- "Wave fronts closer together = higher frequency."
- Explanation that names only "density" — the mark is for the change of speed, and for one part of the wave front slowing first.
- "The wave bends at the boundary because it hits it at an angle" — no mechanism.
- Frequency changing in the new medium.

**Command words**: Use a wave front diagram to explain, Draw (wave fronts in the second medium), Explain.

**Typical questions** ⚑ examiner-drafted
- *(HT) Use a wave front diagram to explain why light changes direction when it enters glass at an angle. [3]* — one end of the wave front reaches the glass first (1); that end slows down while the rest keeps going faster (1); so the wave front turns/changes direction, towards the normal (1).
- *(HT) Complete the diagram to show the wave fronts in the glass. [2]* — fronts closer together (1); turned towards the normal, continuous at the boundary (1).

**Required practical**: none.

**Equations**: v = f λ — On the sheet; used qualitatively (f fixed, so λ ∝ v).

**Boundaries**: radio production/induction has its home on `properties-em-waves-2` (HT layer); seismic paths on `waves-detection-exploration` (TH).

## 6. Verdict
SOURCE OK WITH FLAGS. All science correct; both quiz items usable. The page's own point is HT only, not physics only, so the true routes are CH TH (the approved route PR moves it from TH). After the move the seismic paragraph (physics only, HT) must be a TH-only aside, and its "denser rock" cause should be re-cut. One imprecise line (spacing shows frequency).

**For Mide:** none.
