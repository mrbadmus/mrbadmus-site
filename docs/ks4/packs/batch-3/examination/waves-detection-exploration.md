# Examination — Waves for Detection and Exploration (waves-detection-exploration) — AQA 8463 4.6.1.5 (physics only, HT only) / not in 8464
Verdict: SOURCE OK WITH FLAGS
Examiner: Opus, 1 Oct 2026. Pack examined: `docs/ks4/packs/batch-3/physics-8463-4.6.1.5-waves-detection-exploration.md`.
Spec sources fetched from filestore.aqa.org.uk and read as text: AQA-8463-SP-2016.PDF (v1.1, 30 Sep 2019) incl. Appendix A; AQA-8464-SP-2016.PDF (v1.1, 04 Oct 2019) — searched in full: no ultrasound, seismic-wave or echo-sounding content anywhere. Both June 2026 equation sheets read in full. Mark-scheme conventions from examiner knowledge of AQA 8463 papers 2018–2024; not fetched.

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n. One route copy (TH).

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8463 | **4.6.1.5** | Waves for detection and exploration | **physics only, HT only** |
| 8464 | **not in 8464** | — | — |
| Content the pack strays into | 8463 4.6.2.2 / 8464 6.6.2.2 Properties of EM waves 1 — "(HT only) Different substances may absorb, transmit, refract or reflect electromagnetic waves in ways that vary with wavelength" (HT, both pathways; lesson `properties-em-waves-1`); 8463 4.6.1.3 Reflection of waves (physics only) | | |

**Is the whole subtopic really HT? Yes.** The 8463 heading reads verbatim "4.6.1.5 Waves for detection and exploration (physics only) (HT only)". The data's `spec` field "6.6.1.5" has the right labels but the wrong number (no 6.6.1.5 in 8464). The route (Triple Higher only) is correct.

Spec statement (verbatim, the whole of it): "Students should be able to explain in qualitative terms, how the differences in velocity, absorption and reflection between different types of wave in solids and liquids can be used both for detection and exploration of structures which are hidden from direct observation. Ultrasound waves have a frequency higher than the upper limit of hearing for humans. Ultrasound waves are partially reflected when they meet a boundary between two different media. The time taken for the reflections to reach a detector can be used to determine how far away such a boundary is. This allows ultrasound waves to be used for both medical and industrial imaging. Seismic waves are produced by earthquakes. P-waves are longitudinal, seismic waves. P-waves travel at different speeds through solids and liquids. S-waves are transverse, seismic waves. S-waves cannot travel through a liquid. P-waves and S-waves provide evidence for the structure and size of the Earth's core. Echo sounding, using high frequency sound waves is used to detect objects in deep water and measure water depth. Students should be aware that the study of seismic waves provided new evidence that led to discoveries about parts of the Earth which are not directly observable." (WS 1.1, WS 1.4.)

**Coverage note.** The pack covers seismic waves and echo sounding well but has **no ultrasound-imaging block** — the medical and industrial ultrasound material (a third of the spec point) sits in the `sound-waves-hearing` pack. Move it here; see that examination.

## 2. Route table
| # | teachable point | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Ultrasound: f above 20 kHz; partial reflection at boundaries; timing → distance; medical and industrial imaging | triple-higher | 4.6.1.5 | — (in `sound-waves-hearing` pack) | **Missing here** — move in |
| R2 | Seismic waves from earthquakes; P longitudinal, solids and liquids, different speeds; S transverse, not through liquids (theory 1; key_note; matching) | triple-higher | 4.6.1.5 | TH | OK |
| R3 | P/S evidence for structure and size of the core; S-wave shadow → liquid outer core; refraction → curved paths (theory 1; common_mistake; q1) | triple-higher | 4.6.1.5 | TH | OK |
| R4 | Seismic study gave new evidence about parts of the Earth not directly observable | triple-higher | 4.6.1.5 (WS 1.1) | — | **Missing** — one sentence and a ladder item |
| R5 | Echo sounding with high-frequency sound: depth, objects in deep water (theory 2; q2; equations) | triple-higher | 4.6.1.5 | TH | OK |
| R6 | Seismic surveying for oil; glacier radar; fish/submarine detection (theory 2) | NOT-IN-SPEC (context) | — | TH | Context only (fish/submarines are "objects in deep water" — in spec) |
| R7 | Absorb / transmit / refract / reflect varying with wavelength; EM examples (theory 3) | **higher** (EM, both pathways) | 6.6.2.2 / 4.6.2.2 (HT only) | TH | Route OK here (TH ⊂ higher) but owned by `properties-em-waves-1`; keep only the mechanical-wave examples (sound, seismic) as 4.6.1.5's "velocity, absorption and reflection" |
| R8 | `higher` field ("HT only — …") | — | — | TH | Redundant — the whole page is HT |
| — | RP | none | none | — | correct |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | theory 1 | seismic waves produced by earthquakes (or explosions), travel through the Earth | OK | — | 4.6.1.5 |
| C2 | theory 1 | P-waves: longitudinal; solids and liquids; faster; arrive first | OK | Spec: "travel at different speeds through solids and liquids". | 4.6.1.5 |
| C3 | theory 1 | S-waves: transverse; solids only; slower | OK | — | 4.6.1.5 |
| C4 | theory 1 | S-waves do not pass through the outer core → outer core liquid | OK | — | 4.6.1.5 |
| C5 | theory 1 | "P-waves are refracted (change speed) at the core boundary → core is DENSER than mantle" | IMPRECISE | Refraction shows a sudden change of **speed** (a different material / a boundary), which is what lets the core's **size** be worked out. It does not on its own show the core is denser. Correct: "P-waves change speed and refract sharply at the core boundary → evidence of a boundary between different materials, and of the size of the core". | 4.6.1.5 |
| C6 | theory 1 | seismographs detect arrival times → map interior | OK | — | 4.6.1.5 |
| C7 | theory 1 | "SHADOW ZONES: Regions on Earth's surface that receive neither P nor S waves after a distant earthquake." | IMPRECISE | That is only the **P-wave** shadow zone (a band roughly 104°–140° from the epicentre, where neither arrives). The S-wave shadow zone is the whole region beyond about 104°, which **does** receive P-waves. Define each separately. | 4.6.1.5 |
| C8 | theory 1 | "S-wave shadow zone: region directly opposite the earthquake (S-waves blocked by liquid core)" | IMPRECISE | Much larger than "directly opposite" — the whole far side beyond ~104°. Mechanism correct. | 4.6.1.5 |
| C9 | theory 1 | P-wave shadow zone: P-waves refracted by core → gaps | OK | — | 4.6.1.5 |
| C10 | theory 2 | echo sounding uses reflected sound/ultrasound pulses; d = v × t / 2 | OK | Spec: "high frequency sound waves". | 4.6.1.5 |
| C11 | theory 2 | ocean-floor mapping; fish shoals; submarines | OK | "detect objects in deep water and measure water depth". | 4.6.1.5 |
| C12 | theory 2 | glacier thickness by radar (EM) | OK, NOT-IN-SPEC | — | — |
| C13 | theory 2 | seismic surveying for oil: explosions, reflections from rock layers, timing gives depth | OK, NOT-IN-SPEC | Good illustration of "exploration of structures hidden from direct observation". | 4.6.1.5 (spirit) |
| C14 | theory 3 | substances absorb, transmit, refract or reflect waves in ways that vary with wavelength | OK — but this is 4.6.2.2 (EM, HT) wording | Fine on TH. For 4.6.1.5, the spec's own phrase is "differences in velocity, absorption and reflection between different types of wave in solids and liquids". | 4.6.2.2; 4.6.1.5 |
| C15 | theory 3 | refraction: waves change speed between media → change direction; P-waves curve; light in lens/prism; sound between air layers at different temperatures | OK | — | — |
| C16 | theory 3 | reflection: echoes, sonar, radar from aircraft | OK | — | 4.6.1.3 |
| C17 | theory 3 | absorption: IR by greenhouse gases; UV by ozone; X-rays by bone more than soft tissue | OK | — | — |
| C18 | theory 3 | transmission: light through glass; P-waves through liquid outer core | OK | — | — |
| C19 | `higher` | infer structure; P vs S; why S not through outer core; echo depths | OK / redundant | Whole page HT. | — |
| C20 | common_mistake | S not through liquids → outer core liquid; P through both; curved paths because speed changes gradually with depth (refraction) | OK | Matches AQA mark-scheme language ("density/speed changes gradually, so the waves refract gradually"). | 4.6.1.5 |
| C21 | key_note | P/S properties; S blocked → liquid outer core; d = vt/2; oil surveying; refraction | OK | Add an ultrasound-imaging line once R1 moves in. | 4.6.1.5 |
| C22 | equations | "d = v × t / 2 (echo sounding depth calculation)" | IMPRECISE | Not an AQA equation; AQA's is **s = v t** (recall list eq 6; on both June 2026 sheets). Render s = v t; halving as a method step. | App. A eq 6 |
| C23 | q1 key | S-waves not detected opposite → liquid outer core | OK | — | 4.6.1.5 |
| C24 | q1 wx1 | S-waves lose energy but are detected if the path is clear; shadow zones indicate a liquid barrier | OK | — | — |
| C25 | q1 wx2 | "S-waves do attenuate, but the pattern of shadow zones is specifically consistent with a liquid outer core" | OK | Distractor ("absorbed by the mantle") is plausible; feedback correct. | — |
| C26 | q1 wx3 | P-waves are detected on the opposite side, so "too far" fails | OK | Good evidence-based reasoning. | — |
| C27 | q2 key | echo 0.4 s, v 1500 m/s → 300 m | OK | 1500 × 0.4 = 600; ÷ 2 = 300 ✓ | 4.6.1.5 |
| C28 | q2 opts 2–4 / wx1–wx3 | 600 m (no halving); 3750 m (1500 ÷ 0.4); 150 m (÷ 4) | OK | 600 ✓; 3750 ✓; 150 ✓. wx2 "speed ÷ time gives a rate of change of speed" — dimensionally m/s², fair. | — |
| C29 | matching (to be replaced) | 4 pairs | OK | — | — |

Count: **0 WRONG**; **IMPRECISE**: C5, C7, C8 (theory, re-cuttable), C22. All arithmetic ✓ (5 calculations rechecked).

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| No item is wrong for its route. q1 (S-wave shadow → liquid outer core) and q2 (echo depth, 300 m) are correct and 4.6.1.5. | | **Keep both; usable as rungs on TH** (q1 Recall/Explain, q2 Apply). Also take `sound-waves-hearing` q1 and FIFA here (and its q2 once wx2 is corrected). |
| `equations` field · "d = v × t / 2" | Not an AQA equation (C22). | Keep as data; render s = v t on the card. |

## 5. For the lesson author
**Misconceptions seen in AQA marking**
- "S-waves can't pass through the core" — they cannot pass through the **liquid outer** core; P-waves do pass through it.
- P/S properties swapped (P transverse / S longitudinal), or "P-waves cannot travel through liquids".
- "Seismic waves travel in straight lines through the Earth" — they curve because speed changes gradually with depth.
- Echo sounding: forgetting to halve; time in ms not converted; using 330 m/s (air) for water.
- "Ultrasound is completely reflected" — it is **partially** reflected at each boundary; the rest is transmitted to deeper boundaries, which is what builds the image.
- "Ultrasound is a different kind of wave from sound" — it is sound above 20 kHz.

**Command words**: Explain (dominant — qualitative, per the spec), Describe, Suggest, Calculate (depth/distance), Use the information (from a seismograph trace or shadow-zone diagram).

**Typical questions** ⚑ examiner-drafted
- *Give one difference between P-waves and S-waves. [1]* — P longitudinal, S transverse / P travel through liquids, S do not / P faster.
- *An ultrasound pulse is sent into the body. A reflection from a boundary is detected 0.13 ms later. The speed of ultrasound in soft tissue is 1540 m/s. Calculate the depth of the boundary. [4]* — t = 0.13 × 10⁻³ s (1); distance travelled = 1540 × 0.000 13 = 0.2002 m (1); depth = half of this (1); = 0.10 m (10 cm) (1).
- *Explain how ultrasound is used to produce an image of a fetus. [4]* — ultrasound (above 20 kHz) is sent into the body (1); partially reflected at boundaries between different tissues/media (1); time for the reflections to return is measured (1); used to calculate how far away each boundary is, building up an image (1).
- *Explain how seismic waves provide evidence about the structure of the Earth. [6]* — Levels: **L3 (5–6)** S-waves transverse and cannot travel through liquids → S-wave shadow zone over the far side → outer core is liquid; P-waves longitudinal, travel through solids and liquids but change speed → refract at boundaries → P-wave shadow zone; the size of the shadow zones gives the size of the core; curved paths due to gradual change of speed with depth. **L2 (3–4)** S-wave evidence for a liquid outer core explained, with some P-wave reference. **L1 (1–2)** properties of P and S waves stated without linking to structure. ⚑
- *Suggest why the study of seismic waves was important in learning about the Earth's core. [2]* — the core cannot be observed directly / drilled to (1); seismic waves provided new evidence of its structure and size (1). (WS 1.1.)
- *Explain why ultrasound rather than X-rays is used for pre-natal scanning. [2]* — X-rays are ionising and could damage cells/cause mutations in the fetus (1); ultrasound is not ionising (1).

**Required practical**: none.

**Equations**: none stated in 4.6.1.5. Supporting: s = v t — **learn it** per the recall list (8463 Appendix A eq 6), **printed on both June 2026 sheets**. The halving is method, not an equation. CFIFA: the detection lesson has no FIFA in its data; take the SONAR FIFA from `sound-waves-hearing` as the "nothing to convert" example and author a second with **ms → s** (as in the ultrasound question above).

## 6. Verdict
SOURCE OK WITH FLAGS. Route is correct: 8463 4.6.1.5 is genuinely Physics-only **and** HT-only — Triple Higher only; not in 8464. The data's `spec` number "6.6.1.5" is wrong (8463 4.6.1.5). Science is sound; both frozen quiz items usable. Imprecise: the shadow-zone definitions and "refraction shows the core is denser". Missing: the ultrasound-imaging third of the spec point (currently in `sound-waves-hearing` — move it here) and the WS 1.1 point that seismic waves gave new evidence about the unobservable interior. Theory 3's general absorb/transmit/refract/reflect block is 4.6.2.2 (EM, HT) wording; trim to the mechanical-wave examples.

**For Mide:** none.
