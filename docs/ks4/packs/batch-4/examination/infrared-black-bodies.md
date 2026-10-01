# Examination — Infrared Emission, Absorption and Black Bodies (infrared-black-bodies) — AQA 8463 4.6.3.1–4.6.3.2
Verdict: SOURCE HAS ERRORS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-4/04-checked-science-source/physics-8463-4.6.3-infrared-black-bodies.md`.
Spec sources read as text: `AQA-8463-spec.txt` (v1.1) §4.6.2.1–4.6.2.4, §4.6.3.1–4.6.3.2, §8.2.10 (RP10); `AQA-8464-spec.txt` (v1.1) §6.6.2.1–6.6.2.4, §10.2.21 (RP21) — 8464 has no black-body section; `AQA-8462-spec.txt` §4.9.2 (greenhouse, for cross-reference). Route audit `physics.md` row `infrared-black-bodies` and §3. Peak wavelengths below from Wien's law (λmax ≈ 2.9 × 10⁻³ m K ÷ T) — examiner check only, not spec content.

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n; T1–T3 = theory chunks. Quiz identical on TF and TH; TF `higher` copy is null.

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8463 | **4.6.3.1** | Emission and absorption of infrared radiation | (physics only) |
| 8463 | **4.6.3.2** | Perfect black bodies and radiation | (physics only); balance and Earth statements (HT only) |
| 8464 | — | no equivalent — black body radiation is not in Combined | — |
| Supporting | 8464 6.6.2.2 / 8463 4.6.2.2 — RP21 / RP10 (IR from surfaces) | base | base |
| Supporting | 8464 6.6.2.4 / 8463 4.6.2.4 — "infrared – … infrared cameras" | base | base |

Spec statements (verbatim, 8463): 4.6.3.1 "All bodies (objects), no matter what temperature, emit and absorb infrared radiation. The hotter the body, the more infrared radiation it radiates in a given time. A perfect black body is an object that absorbs all of the radiation incident on it. A black body does not reflect or transmit any radiation. Since a good absorber is also a good emitter, a perfect black body would be the best possible emitter." 4.6.3.2 "Students should be able to explain: • that all bodies (objects) emit radiation • that the intensity and wavelength distribution of any emission depends on the temperature of the body. (HT only) A body at constant temperature is absorbing radiation at the same rate as it is emitting radiation. The temperature of a body increases when the body absorbs radiation faster than it emits radiation. (HT only) The temperature of the Earth depends on many factors including: the rates of absorption and emission of radiation, reflection of radiation into space. (HT only) Students should be able to explain how the temperature of a body is related to the balance between incoming radiation absorbed and radiation emitted, using everyday examples to illustrate this balance, and the example of the factors which determine the temperature of the Earth. (HT only) Students should be able to use information, or draw/interpret diagrams to show how radiation affects the temperature of the Earth's surface and atmosphere."
RP (8464 6.6.2.2 RP21 = 8463 4.6.2.2 RP10, base): "investigate how the amount of infrared radiation absorbed or radiated by a surface depends on the nature of that surface."

## 2. Route table
| # | teachable point | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | All objects emit and absorb IR (T1; key_note) | triple | 4.6.3.1 | TF TH | OK |
| R2 | Hotter → more radiation per second; distribution shifts to shorter λ (T1; T2 curves; common_mistake) | triple | 4.6.3.1; 4.6.3.2 | TF TH | IMPRECISE wording (C3) |
| R3 | Dark matt = better absorber and emitter; shiny = reflector (T1; key_note; T3 "selective") | **base** (RP outcome) | 8464 6.6.2.2 RP21 / 8463 4.6.2.2 RP10 | TF TH | OK science; ROUTE — Combined gets it only on `properties-em-waves-1` (IRB-F6) |
| R4 | Emission vs absorption rate → cools / heats / constant (T1 last block) | **triple-higher** | 4.6.3.2 (HT only) | TF TH, taught as base | ROUTE (IRB-F5) |
| R5 | Perfect black body: absorbs all, reflects/transmits none, best emitter (T2; common_mistake; key_note) | triple | 4.6.3.1 | TF TH | OK |
| R6 | Black body curves: peak shifts, total rises with T (T2) | triple | 4.6.3.2 ("intensity and wavelength distribution… depends on the temperature") | TF TH | OK in principle; example WRONG (C9) |
| R7 | Cavity with small hole ≈ black body (T2) | triple (context) | — | TF TH | OK |
| R8 | Star colour ↔ temperature (T3) | off-spec context | — (8463 4.8 does not require it) | TF TH | OFF-SPEC (IRB-F7) |
| R9 | Earth absorbs solar, re-emits longer-λ IR; greenhouse gases (T3; `higher`) | **triple-higher** | 4.6.3.2 (HT only); greenhouse mechanism also 8462 4.9.2.1 / 8464 5.9.2.1 base chemistry | TF TH, taught as base | ROUTE (IRB-F5) |
| R10 | Thermal cameras (T3) | base | 8464 6.6.2.4 | TF TH | OK |
| R11 | JWST/Hubble (T3) | off-spec context | — | TF TH | OFF-SPEC (IRB-F7) |
| R12 | Solar panels / water heaters dark; flask silvered (T3; q2) | base (RP outcome applied) | 8464 6.6.2.2 RP21 | TF TH | OK |
| R13 | `higher` (TH): curves; Earth balance; greenhouse; albedo | curves = triple; rest = triple-higher | 4.6.3.2 | TH | ROUTE/IMPRECISE (IRB-F5) |
| R14 | q1 — heated rod red → orange → white | triple | 4.6.3.2 | TF TH | **WRONG** (wx3; IRB-F2) |
| R15 | q2 — silvered thermos walls | base | 8464 6.6.2.2 RP21 | TF TH | OK |
| — | `rp` | absent | RP21/RP10 is base and belongs on `properties-em-waves-1` | — | IRB-F6 |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | T1 | all objects emit and absorb IR continuously | OK | — | 4.6.3.1 |
| C2 | T1 | "All objects above absolute zero emit infrared radiation" | OK | Spec: "no matter what temperature". | 4.6.3.1 |
| C3 | T1; common_mistake | "Hotter objects emit MORE radiation and at SHORTER wavelengths" | IMPRECISE | A hotter body emits more at every wavelength, and a greater share at shorter wavelengths — the peak moves to shorter λ. It does not stop emitting long wavelengths. | 4.6.3.2 |
| C4 | T1 | dark matt better absorbers and emitters; shiny light better reflectors, poorer emitters/absorbers | OK | RP21/RP10 outcome. | 6.6.2.2 |
| C5 | T1 | emission > absorption → cools; absorption > emission → heats; equal → constant | OK science | HT only (triple-higher). | 4.6.3.2 HT |
| C6 | T2 | perfect black body absorbs all, emits maximum for its temperature | OK | — | 4.6.3.1 |
| C7 | T2 | spectrum of a black body depends only on temperature | OK | True for an ideal black body; beyond spec wording. | 4.6.3.2 |
| C8 | T2 | hot iron 600 °C glows dull red | OK | Visible red glow begins ≈ 500–600 °C. Peak still ≈ 3.3 µm (IR). | — |
| C9 | T2 | "Very hot iron (1000°C): orange-white — peak moves into visible range" | **WRONG** | At 1000 °C (1273 K) the peak is ≈ 2.3 µm — still infrared. The glow brightens and more of the visible band is emitted; the peak only reaches the visible near 4000 K and above. Also 1000 °C looks orange-yellow, not white. IRB-F1. | 4.6.3.2 |
| C10 | T2 | Sun ~5500 °C, peak in visible (yellow-green) | OK | Photosphere ≈ 5800 K ≈ 5500 °C; peak ≈ 500 nm ✓. | — |
| C11 | T2 | a cavity with a small hole ≈ black body | OK | — | — |
| C12 | T3 | red stars ~3000 K peak in IR/red; Sun ~5500 K; blue-white ~30,000 K peak UV | IMPRECISE / OFF-SPEC | Peaks ✓ (≈ 970 nm; ≈ 100 nm). Sun given as "~5500 K" here but "~5500 °C" in T2 — it is ≈ 5800 K. Star colour not in spec. IRB-F4, IRB-F7. | — |
| C13 | T3 | Earth absorbs solar radiation, re-emits as longer-λ IR because cooler | OK | HT only. | 4.6.3.2 HT |
| C14 | T3 | greenhouse gases absorb Earth's IR → warming | OK | HT here; chemistry base elsewhere. | 4.6.3.2 HT; 8462 4.9.2.1 |
| C15 | T3 | thermal cameras: night vision, firefighting, medical, building inspection | OK | — | 6.6.2.4 |
| C16 | T3 | Hubble detects visible; JWST detects infrared | IMPRECISE / OFF-SPEC | Hubble also observes near-UV and near-IR. Not examinable. | — |
| C17 | T3 | solar panels dark matt; solar water heaters black tubes; flasks silvered | OK | (PV panels are dark behind glass — "dark" is the point.) | 6.6.2.2 RP outcome |
| C18 | `higher` (TH) | "Explain black body radiation curves — how peak wavelength depends on temperature" | ROUTE | Not HT — 4.6.3.2's distribution statement is unlabelled, so TF needs it too. | 4.6.3.2 |
| C19 | `higher` (TH) | Earth radiation balance; greenhouse; "albedo" | OK as triple-higher | Spec says "reflection of radiation into space" — use those words, not "albedo". | 4.6.3.2 HT |
| C20 | common_mistake | black body absorbs all, emits maximum; perfect emitter and absorber go together | OK | "Since a good absorber is also a good emitter" ✓ | 4.6.3.1 |
| C21 | key_note | as above; Earth / greenhouse | OK | Greenhouse line is HT. | — |
| C22 | q1 key | "peak emission shifts to shorter wavelengths — from infrared through red to shorter visible wavelengths approaching white" | IMPRECISE | First clause ✓ (the creditable point). Second clause implies the peak passes through red into the visible — for a furnace-heated rod it stays in the IR. | 4.6.3.2 |
| C23 | q1 wx1 | colour change is temperature, not chemistry | OK | — | — |
| C24 | q1 wx2 | pattern follows the temperature-dependent black body spectrum | OK | — | — |
| C25 | q1 wx3 | "White hot means the peak has moved to visible wavelengths with broad-spectrum emission" | **WRONG** | White-hot metal (≈ 1300–1500 °C) peaks ≈ 1.6–1.8 µm, in the IR. It looks white because it now emits all visible wavelengths strongly enough to mix. IRB-F2. | 4.6.3.2 |
| C26 | q2 key | silvered walls poor emitters and absorbers, reflect IR back | OK | — | 6.6.2.2 RP outcome |
| C27 | q2 wx1 | silver conducts well, but silvering reduces radiation | OK | — | — |
| C28 | q2 wx2 | silver forms no significant oxide layer at room temperature | OK | (Tarnish is silver sulfide; irrelevant.) | — |
| C29 | q2 wx3 | IR, not visible, reflection is the point | OK | — | — |
| C30 | matching (to be replaced) | four pairs | OK | "peak shifts towards visible/UV" ✓ as direction. | — |

Count: **2 WRONG** (C9 theory — re-cuttable; C25 q1 wx3 — frozen, q1 not usable as written). IMPRECISE: C3, C12, C16, C22. ROUTE: R3, R4, R9, C18.

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| q1 | wx3 states a false fact; key's gloss implies the peak enters the visible | **Do not use as written.** |
| q2 | correct; base content (RP outcome) | Usable on TF TH. |

## 5. For the lesson author
**Misconceptions seen in AQA marking**: "cold objects don't emit radiation"; "black bodies are black because they don't emit"; "shiny surfaces absorb more because they look brighter"; "a hotter object emits shorter wavelengths instead of longer ones" (it emits more of all); "a body at constant temperature has stopped absorbing/emitting" (HT: the rates are equal); "white-hot means the peak is in the visible".

**Command words**: Explain, Describe, Give, Suggest (everyday balance examples, HT), Use the diagram (Earth's energy balance, HT).

**Required practical**: settled — RP21 (8464 6.6.2.2) = RP10 (8463 4.6.2.2), **base, all four routes**. Its spec home is "Properties of electromagnetic waves 1", so it belongs on `properties-em-waves-1` (CF CH TF TH), agreeing with the route audit. It must not live on this page: this page is physics-only, so Combined pupils would lose a base RP. This page recalls its result (dark matt surfaces are the best emitters and absorbers) as the bridge into "the perfect absorber is the perfect emitter".

## 6. Verdict
SOURCE HAS ERRORS. Two WRONG statements about where a glowing object's emission peak lies (theory chunk 2's 1000 °C example; q1 wx3). Both make the same false point — "the peak moves into the visible" for hot metal — and it is exactly the misconception the lesson should kill. q1 not usable as written; q2 usable. HT content (absorb/emit balance; Earth's temperature) is taught as base and must become the triple-higher layer. Spec field "6.6.5 (physics only)" is wrong (8463 4.6.3; no 8464 equivalent). True routes TF TH, as the site ships.

**For Mide:** nothing on science. RP placement is settled from the spec (base RP on `properties-em-waves-1`) and goes in the route-flag PR alongside the audit's other RP fixes.
