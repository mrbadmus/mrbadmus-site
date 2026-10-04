# KS4 Physics: route audit against AQA 8464 and 8463

Audited 1 Oct 2026. Sources: `site-routes.tsv` (82 physics rows), AQA 8464 Combined Science: Trilogy v1.1 (physics is section 6), AQA 8463 Physics v1.1 (section 4), both equation sheets, and `all_subtopics_physics_*.py` (route files hold 50 / 53 / 64 / 82 pages, matching CF / CH / TF / TH).

Route key: **base** = CF CH TF TH. **CH TH** = Higher only. **TF TH** = Physics only. **TH** = Physics only and Higher only.

Rule applied: a page goes on every route where AQA teaches any of its core content. If only part of a page is HT or physics-only, that part is a **layer** inside the page and does not change the page's route.

## 1. Every physics subtopic

| slug | site routes | true route | 8464 ref | 8463 ref | verdict | note (layers) |
|---|---|---|---|---|---|---|
| energy-stores-systems | base | base | 6.1.1.1 | 4.1.1.1 | OK | |
| changes-in-energy | base | base | 6.1.1.2 | 4.1.1.2 | OK | Ee = ½ke² is base (Mide's ruling). Ek, Ep and Ee are all on both 2026 sheets. |
| energy-changes-in-systems | base | base | 6.1.1.3 | 4.1.1.3 | OK | SHC required practical (8464 RP14 / 8463 RP1) |
| power | base | base | 6.1.1.4 | 4.1.1.4 | OK | |
| energy-transfers-in-a-system | base | base | 6.1.2.1 | 4.1.2.1 | OK | |
| efficiency | base | base | 6.1.2.2 | 4.1.2.2 | OK | HT layer: "describe ways to increase the efficiency" |
| energy-resources | base | base | 6.1.3 | 4.1.3 | OK | |
| **thermal-conductivity** | TF TH | **base** | **6.1.2.1** | 4.1.2.1 | **MOVE WIDER → base** | Physics-only layer: RP2, thermal insulators. The page's `spec` field says "6.1.3 (physics only)", which is wrong. |
| circuit-symbols | base | base | 6.2.1.1 | 4.2.1.1 | OK | |
| electrical-charge-current | base | base | 6.2.1.2 | 4.2.1.2 | OK | |
| current-resistance-pd | base | base | 6.2.1.3 | 4.2.1.3 | OK | Resistance RP |
| resistors | base | base | 6.2.1.4 | 4.2.1.4 | OK | I–V RP |
| series-parallel-circuits | base | base | 6.2.2 | 4.2.2 | OK | |
| direct-alternating-pd | base | base | 6.2.3.1 | 4.2.3.1 | OK | |
| mains-electricity | base | base | 6.2.3.2 | 4.2.3.2 | OK | |
| power-electricity | base | base | 6.2.4.1 | 4.2.4.1 | OK | |
| energy-transfers-appliances | base | base | 6.2.4.2 | 4.2.4.2 | OK | |
| national-grid | base | base | 6.2.4.3 | 4.2.4.3 | OK | The transformer equation (4.7.3.4, HT, physics only) sits on `transformers`, not here |
| static-charge | TF TH | TF TH | — | 4.2.5.1 | OK | "4.2.5 Static electricity (physics only)" |
| electric-fields | TF TH | TF TH | — | 4.2.5.2 | OK | |
| density-of-materials | base | base | 6.3.1.1 | 4.3.1.1 | OK | Density RP |
| changes-of-state | base | base | 6.3.1.2 | 4.3.1.2 | OK | |
| internal-energy | base | base | 6.3.2.1 | 4.3.2.1 | OK | |
| temperature-changes-shc | base | base | 6.3.2.2 | 4.3.2.2 | OK | |
| specific-latent-heat | base | base | 6.3.2.3 | 4.3.2.3 | OK | |
| particle-motion-pressure | base | base | 6.3.3.1 | 4.3.3.1 | OK | Physics-only layer: pV = constant / Boyle (4.3.3.2), which the page currently shows on every route. 4.3.3.3 (HT, physics only) has no page, see §3. |
| structure-of-atom | base | base | 6.4.1.1 | 4.4.1.1 | OK | |
| mass-number-isotopes | base | base | 6.4.1.2 | 4.4.1.2 | OK | |
| development-atomic-model | base | base | 6.4.1.3 | 4.4.1.3 | OK | |
| radioactive-decay | base | base | 6.4.2.1 | 4.4.2.1 | OK | |
| nuclear-equations | base | base | 6.4.2.2 | 4.4.2.2 | OK | |
| half-lives | base | base | 6.4.2.3 | 4.4.2.3 | OK | HT layer: net decline as a ratio. Physics-only layer: comparing isotopes by half-life (4.4.3.2). |
| radioactive-contamination | base | base | 6.4.2.4 | 4.4.2.4 | OK | |
| background-radiation | TF TH | TF TH | — | 4.4.3.1 | OK | "4.4.3 … (physics only)" |
| uses-of-nuclear-radiation | TF TH | TF TH | — | 4.4.3.3 | OK | The spec names medical uses only. Industrial uses (smoke alarms, gauges) go beyond it. |
| nuclear-fission | TF TH | TF TH | — | 4.4.4.1 | OK | "4.4.4 Nuclear fission and fusion (physics only)" |
| nuclear-fusion | TF TH | TF TH | — | 4.4.4.2 | OK | |
| scalar-vector-quantities | base | base | 6.5.1.1 | 4.5.1.1 | OK | |
| contact-noncontact-forces | base | base | 6.5.1.2 | 4.5.1.2 | OK | |
| gravity | base | base | 6.5.1.3 | 4.5.1.3 | OK | |
| resultant-forces | base | base | 6.5.1.4 | 4.5.1.4 | OK | The HT parts of 6.5.1.4 have their own pages (next two rows) |
| **resolving-forces** | TH | **CH TH** | **6.5.1.4 (HT only)** | 4.5.1.4 (HT only) | **MOVE WIDER → CH TH** | |
| **free-body-diagrams** | TH | **CH TH** | **6.5.1.4 (HT only)** | 4.5.1.4 (HT only) | **MOVE WIDER → CH TH** | |
| work-done-energy-transfer | base | base | 6.5.2 | 4.5.2 | OK | |
| forces-elasticity | base | base | 6.5.3 | 4.5.3 | OK | Ee = ½ke² is base. Spring RP (8464 RP18 / 8463 RP6). |
| moments-levers-gears | TF TH | TF TH | — | 4.5.4 | OK | "4.5.4 Moments, levers and gears (physics only)" |
| pressure-in-a-fluid | TF TH | TF TH | — | 4.5.5.1.1, 4.5.5.2 | OK | HT layer: p = hρg and upthrust (4.5.5.1.2 HT). The key note currently shows both to TF. |
| upthrust-floating | TH | TH | — | 4.5.5.1.2 (HT only) | OK | |
| distance-speed-velocity | base | base | 6.5.4.1.1–3 | 4.5.6.1.1–3 | OK | Circular motion (HT) has its own page |
| distance-time-graphs | base | base | 6.5.4.1.4 | 4.5.6.1.4 | OK | HT layer: tangent to find speed |
| acceleration | base | base | 6.5.4.1.5 | 4.5.6.1.5 | OK | HT layer: distance from the area under a v–t graph |
| newtons-laws | base | base | 6.5.4.2.1–3 | 4.5.6.2.1–3 | OK | HT layers: inertia and inertial mass. Acceleration RP (8464 RP19 / 8463 RP7). |
| stopping-distance-braking | base | base | 6.5.4.3 | 4.5.6.3 | OK | |
| **motion-in-a-circle** | TH | **CH TH** | **6.5.4.1.3 (HT only line)** | 4.5.6.1.3 (HT only line) | **MOVE WIDER → CH TH** | Physics-only layer (HT): stable orbit speed and radius (4.8.1.3) |
| momentum | CH TH | CH TH | 6.5.5 (HT only) | 4.5.7 (HT only) | OK | Physics-only layer: F = mΔv/Δt and safety features (4.5.7.3). The key note currently shows it on CH. |
| transverse-longitudinal-waves | base | base | 6.6.1.1 | 4.6.1.1 | OK | |
| sound-waves-hearing | TH | TH | — | 4.6.1.4 (physics only)(HT only) | OK | |
| waves-detection-exploration | TH | TH | — | 4.6.1.5 (physics only)(HT only) | OK | |
| properties-of-waves | base | base | 6.6.1.2 | 4.6.1.2 | OK | Waves RP (8464 RP20 / 8463 RP8) |
| types-of-em-waves | base | base | 6.6.2.1 | 4.6.2.1 | OK | |
| properties-em-waves-1 | base | base | 6.6.2.2 | 4.6.2.2 | OK | HT layer: absorb/transmit/refract varies with wavelength. **RP is mislabelled**, see §3. TIR and critical angle go beyond the spec. |
| properties-em-waves-2 | base | base | 6.6.2.3 | 4.6.2.3 | OK | HT layer: radio waves and oscillating circuits |
| uses-em-waves | base | base | 6.6.2.4 | 4.6.2.4 | OK | HT layer: why each wave suits its use |
| **wave-front-refraction** | TH | **CH TH** | **6.6.2.2 (HT only)** (+6.6.2.3 HT) | 4.6.2.2 (HT only) | **MOVE WIDER → CH TH** | |
| lenses | TF TH | TF TH | — | 4.6.2.5 (physics only) | OK | |
| infrared-black-bodies | TF TH | TF TH | — | 4.6.3.1–4.6.3.2 | OK | "4.6.3 Black body radiation (physics only)". The base IR RP is not on this page, see §3. |
| radiation-balance-temperature | TH | TH | — | 4.6.3.2 (HT only lines) | OK | |
| poles-of-a-magnet | base | base | 6.7.1.1 | 4.7.1.1 | OK | |
| magnetic-fields | base | base | 6.7.1.2 | 4.7.1.2 | OK | |
| electromagnetism | base | base | 6.7.2.1 | 4.7.2.1 | OK | |
| flemings-left-hand-rule | CH TH | CH TH | 6.7.2.2 (HT only) | 4.7.2.2 (HT only) | OK | |
| electric-motors | CH TH | CH TH | 6.7.2.3 (HT only) | 4.7.2.3 (HT only) | OK | |
| loudspeakers-headphones | TH | TH | — | 4.7.2.4 (physics only)(HT only) | OK | |
| induced-potential | TH | TH | — | 4.7.3.1 | OK | "4.7.3 … (physics only) (HT only)" |
| uses-generator-effect | TH | TH | — | 4.7.3.2 | OK | |
| microphones | TH | TH | — | 4.7.3.3 | OK | |
| transformers | TH | TH | — | 4.7.3.4 | OK | |
| solar-system-gravity | TF TH | TF TH | — | 4.8.1.1 (+4.8.1.3 non-HT) | OK | HT layer: orbit speed and radius |
| gravity-stable-orbits | TH | TH (unsettled) | — | 4.8.1.3 | OK (see §3) | |
| stellar-evolution | TF TH | TF TH | — | 4.8.1.2 | OK | |
| red-shift-big-bang | TF TH | TF TH | — | 4.8.2 | OK | Hubble's law v = H₀d and CMBR go beyond the spec |
| **dark-matter-dark-energy** | TH | **TF TH** | — | **4.8.2 (physics only, not HT)** | **MOVE WIDER → TF TH** | The percentages, rotation curves and lensing go beyond the spec |

## 2. Changes (non-OK rows only)

1. **thermal-conductivity: TF TH → base (CF CH TF TH).**
   8464 has this content in the Combined course, under "6.1.2.1 Energy transfers in a system": *"Students should be able to explain ways of reducing unwanted energy transfers, for example through lubrication and the use of thermal insulation. The higher the thermal conductivity of a material the higher the rate of energy transfer by conduction across the material. Students should be able to describe how the rate of cooling of a building is affected by the thickness and thermal conductivity of its walls."* 8463 4.1.2.1 has the same text with no physics-only label. Only the practical is separate-only: *"Required practical activity 2 (physics only): investigate the effectiveness of different thermal insulators…"*. That makes RP2 a TF TH layer. Also correct the page's `spec` field from "6.1.3 (physics only)" to 6.1.2.1.
2. **resolving-forces: TH → CH TH.**
   8464 "6.5.1.4 Resultant forces": *"(HT only) A single force can be resolved into two components acting at right angles to each other… (HT only) Students should be able to use vector diagrams to illustrate resolution of forces, equilibrium situations and determine the resultant of two forces… (scale drawings only)."* This is Combined Higher content. Note: the page uses trigonometry (F cosθ, F sinθ), but the spec says "scale drawings only". That is a content point for Mide.
3. **free-body-diagrams: TH → CH TH.**
   8464 "6.5.1.4 Resultant forces": *"(HT only) Students should be able to: … use free body diagrams to describe qualitatively examples where several forces lead to a resultant force on an object, including balanced forces when the resultant force is zero."* The same trigonometry point applies.
4. **motion-in-a-circle: TH → CH TH.**
   8464 "6.5.4.1.3 Velocity": *"(HT only) Students should be able to explain qualitatively, with examples, that motion in a circle involves constant speed but changing velocity."* The same line is in 8463 4.5.6.1.3. The page's orbit material (stable orbit, radius changes if speed changes) is 8463 4.8.1.3 (HT, physics only) and should become a TH layer.
5. **wave-front-refraction: TH → CH TH.**
   8464 "6.6.2.2 Properties of electromagnetic waves 1": *"(HT only) Students should be able to use wave front diagrams to explain refraction in terms of the change of speed that happens when a wave travels from one medium to a different medium."* The page's radio-wave paragraph is 8464 6.6.2.3 *"(HT only) Radio waves can be produced by oscillations in electrical circuits."* That is also Combined Higher.
6. **dark-matter-dark-energy: TH → TF TH.**
   8463 "4.8.2 Red-shift (physics only)" has no HT label anywhere in the section: *"Since 1998 onwards, observations of supernovae suggest that distant galaxies are receding ever faster. Students should be able to explain: … that there is still much about the universe that is not understood, for example dark mass and dark energy."* There is no "6.8.4" and no HT marking for this content. The site's `spec` field "6.8.4 (HT only, physics only)" is wrong.

Effect on page counts: CF 50 → 51, CH 53 → 58, TF 64 → 66, TH stays 82.

## 3. Unsettled, and findings outside route scope

- **gravity-stable-orbits (kept at TH, best reading).** 8463 4.8.1.3 has a non-HT core: *"Gravity provides the force that allows planets and satellites (both natural and artificial) to maintain their circular orbits. Students should be able to describe the similarities and distinctions between the planets, their moons, and artificial satellites."* It also has HT-only bullets: *"(HT only) for circular orbits, the force of gravity can lead to changing velocity but unchanged speed; (HT only) for a stable orbit, the radius must change if the speed changes."* This page's own content (title "Stable Orbits and Orbital Speed", what happens when speed changes) is the HT bullets. The non-HT core is already the main content of `solar-system-gravity` (TF TH). So TH is the better reading. The alternative is TF TH with the stable-orbit material as an HT layer, if Mide treats "gravity keeps satellites in orbit" as this page's core. Either way, `solar-system-gravity` carries HT material ("closer orbit = faster speed") that should be an HT layer.
- **The base infrared required practical is on no page (content accuracy, for Mide).** 8464 6.6.2.2 / 8463 4.6.2.2: *"Required practical activity 21 [8463: 10]: investigate how the amount of infrared radiation absorbed or radiated by a surface depends on the nature of that surface."* It is base, not physics-only. `properties-em-waves-1` lists instead *"RP20 (Physics): Investigate refraction of light through glass or perspex blocks"*. Refraction of light is half of 8463 *"Required practical activity 9 (physics only)"* (4.6.1.3), so a physics-only practical is shown to Combined students under a wrong number. `infrared-black-bodies` (TF TH) has no RP. Recommendation: put the IR RP on `properties-em-waves-1` (base) and make RP9 a TF TH layer. The site's RP numbers are wrong in several other places too: "RP21" is attached to magnetic-field plotting and electromagnet strength, which are not AQA required practicals, and the 8464 numbers run 14–21.
- **Layers currently shown on the wrong routes** (route files carry the same text on every route, so these content items need gating):
  - pV = constant on `particle-motion-pressure` (physics-only, should be TF TH).
  - F = mΔv/Δt and safety features on `momentum` (physics-only, should be TH on a CH TH page).
  - p = hρg and upthrust on `pressure-in-a-fluid` (HT, should be TH on a TF TH page).
  - Orbit material on `motion-in-a-circle` (should be TH once the page moves to CH TH).
- **8463 content with no page:** 4.3.3.3 "Increasing the pressure of a gas (physics only) (HT only)" (bicycle pump), 4.6.1.3 "Reflection of waves (physics only)" with RP9, and 4.6.2.6 "Visible light (physics only)" (specular/diffuse reflection, colour filters). A grep for "specular", "colour filter" and "bicycle pump" finds nothing in the route files. These are coverage gaps, not route errors.
- **Spec version:** both spec texts are v1.1 (2019). The 2026 equation sheets agree on Ek, Ep and Ee. No route verdict above depends on a 2024+ spec change.
