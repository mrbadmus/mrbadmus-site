# Examination — Uses and Applications of Electromagnetic Waves (uses-em-waves) — AQA 8464 6.6.2.4 / 8463 4.6.2.4
Verdict: SOURCE HAS ERRORS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-4/04-checked-science-source/physics-6.6.2.4-uses-em-waves.md`.
Spec sources read as text: `AQA-8464-spec.txt` (v1.1) §6.6.2.1–6.6.2.4; `AQA-8463-spec.txt` (v1.1) §4.6.1.5, §4.6.2.1–4.6.2.4 (grep for "total internal", "ionosphere", "optical fibre": no hits in either spec). Route audit `physics.md` row `uses-em-waves`.

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n; T1–T3 = theory chunks. Quiz identical on all four routes; CF and TF `higher` copies are null.

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 | **6.6.2.4** | Uses and applications of electromagnetic waves | base; "why suitable" (HT only) |
| 8463 | **4.6.2.4** | Uses and applications of electromagnetic waves | base; "why suitable" (HT only) |
| Supporting | 8464 6.6.2.2 (HT: absorb/transmit/refract/reflect vary with λ); 6.6.2.3 (UV/X/gamma hazards; ionising) | | base / HT |

Spec statements (verbatim, 8464 = 8463): "Electromagnetic waves have many practical applications. For example: • radio waves – television and radio • microwaves – satellite communications, cooking food • infrared – electrical heaters, cooking food, infrared cameras • visible light – fibre optic communications • ultraviolet – energy efficient lamps, sun tanning • X-rays and gamma rays – medical imaging and treatments." "(HT only) Students should be able to give brief explanations why each type of electromagnetic wave is suitable for the practical application."

## 2. Route table
| # | teachable point | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Which wave → which use (all theory lists; key_note) | base | 6.6.2.4 | all four | OK (GAP: sun tanning — UEM-F5) |
| R2 | Reasons each wave suits its use (penetration, absorption, ionosphere; theory glosses; common_mistake) | **higher** | 6.6.2.4 (HT only); 6.6.2.2 (HT only) | all four (theory) | ROUTE — CH TH layer (UEM-F3) |
| R3 | Extra uses beyond the spec list (MRI, radar, Wi-Fi, CT, tracers, irradiation, vitamin D, lasers…) | base (context) | — | all four | OK as context, not examinable |
| R4 | Microwave ovens "resonance… heats from inside" (T1) | — | 6.6.2.4 | all four | **WRONG** (UEM-F1) |
| R5 | Ionising types: hazard managed (T3 last block) | base | 6.6.2.3 | all four | OK |
| R6 | `higher` (TH/CH): why suitable; evaluate hazards/benefits; X-ray vs MRI vs ultrasound; TIR in optical fibres | higher, except: ultrasound = triple-higher (8463 4.6.1.5); TIR = off-spec | 6.6.2.4 HT | CH TH | OFF-SPEC / ROUTE (UEM-F2) |
| R7 | q1 — why microwaves for satellites | **higher** | 6.6.2.4 (HT only) | all four | OK — CH TH only |
| R8 | q2 — why UV sterilises | **higher** | 6.6.2.4 (HT only); 6.6.2.3 | all four | OK — CH TH only |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | T1 | radio: AM/FM, TV; "travel long distances, reflect off ionosphere" | IMPRECISE | Long/medium/short-wave radio (below ≈ 30 MHz) reflects off the ionosphere; FM and TV (VHF/UHF) pass through it and are line-of-sight. Ionosphere is off-spec. UEM-F4. | 6.6.2.4 |
| C2 | T1 | radio: aircraft/ship communication; radio telescopes; MRI uses radio waves + magnetic field, no ionising radiation | OK | Context beyond the spec list. | — |
| C3 | T1 | microwaves: mobile phones, Wi-Fi; satellite comms pass through atmosphere/ionosphere | OK | AQA credits "microwaves pass through the atmosphere" for satellites. | 6.6.2.4 HT |
| C4 | T1 | "microwave frequency matches water molecules' resonance → absorbed → food heats from inside" | **WRONG** | 2.45 GHz is not a resonance of water; microwaves are absorbed by water molecules in the food (dielectric heating) over the first few cm, and the centre heats by conduction. "Heats from inside" is a common myth. UEM-F1. | 6.6.2.4 |
| C5 | T1 | radar: timing reflections | OK | — | — |
| C6 | T2 | IR: heaters, grills — "absorbed by surfaces, converted to heat" | IMPRECISE (minor) | "Transfers energy to the thermal energy store of the food/surface". | 6.6.2.4 |
| C7 | T2 | IR: remote controls; IR along optical fibres; night vision; thermal imaging | OK | Telecom fibres do carry IR (≈ 1.3–1.55 µm). Spec's own example is visible light for fibre optics — teach that first. | 6.6.2.4 |
| C8 | T2 | visible: photography, fibre optics, photosynthesis (red and blue), lasers | OK | — | 6.6.2.4 |
| C9 | T2 | UV: sterilisation; fluorescence — security marks, fluorescent lamps; forged notes; vitamin D | OK | Fluorescent lamps = spec's "energy efficient lamps" ✓. Spec's "sun tanning" missing — UEM-F5. | 6.6.2.4 |
| C10 | T3 | X-rays: pass through soft tissue, absorbed by bone; CT; airport security; crack testing | OK | — | 6.6.2.4 |
| C11 | T3 | gamma: radiotherapy; "ST ERILISATION" of equipment without heat; food irradiation; tracers; thickness monitoring | OK | Typo "ST ERILISATION" — re-cut. | 6.6.2.4 |
| C12 | T3 | matching application to wave: penetration, interaction, hazard minimised | OK | HT reasoning. | 6.6.2.4 HT; 6.6.2.3 |
| C13 | `higher` | why wavelengths suit uses: penetration, absorption, reflection, refraction | OK | HT ✓. | 6.6.2.4 HT; 6.6.2.2 HT |
| C14 | `higher` | "X-rays vs MRI vs ultrasound for medical imaging" | ROUTE | Ultrasound is "Waves for detection and exploration (physics only) (HT only)" — not on Combined. MRI not in spec (context). | 8463 4.6.1.5 |
| C15 | `higher` | "Explain how optical fibres work using total internal reflection" | OFF-SPEC | TIR is in neither 8463 nor 8464. UEM-F2. | — |
| C16 | common_mistake | MRI uses radio waves, not X-rays; X-rays image bone; microwaves for satellites, radio for broadcast | OK / IMPRECISE | First two ✓. Ionosphere clause: as C1. | — |
| C17 | key_note | list of uses per wave | OK | Add sun tanning (UV) and cooking food (IR) to match the spec list. | 6.6.2.4 |
| C18 | q1 key | microwaves pass through the ionosphere; radio waves reflect off it | IMPRECISE (acceptable) | True for long/medium/short-wave radio; the creditable HT point is "microwaves pass through the atmosphere/ionosphere". Usable on CH TH. | 6.6.2.4 HT |
| C19 | q1 wx1 | power ≠ distance; all EM waves same speed | OK | "same velocity through a vacuum (space) or air" ✓. | 6.6.2.1 |
| C20 | q1 wx2 | "the ionosphere physically reflects (most) radio waves" | IMPRECISE | "(most)" overstates — only lower frequencies. Not misleading for the item's purpose. | — |
| C21 | q1 wx3 | receiver incompatibility is backwards reasoning | OK | — | — |
| C22 | q2 stem | "UV light is used to sterilise medical equipment" | IMPRECISE (minor) | UV sterilises surfaces, water and air; sealed medical equipment is usually sterilised by gamma (as T3 says). Acceptable stem. | — |
| C23 | q2 key | UV has enough energy to damage DNA in microorganisms | OK | Consistent with 6.6.2.3 (UV harms tissue). | 6.6.2.3 |
| C24 | q2 wx1–wx3 | not heating; metal surfaces usually heat/chemicals; not ozone | OK | — | — |
| C25 | matching (to be replaced) | five pairs | OK | — | — |

Count: **1 WRONG** (C4 theory — re-cuttable). OFF-SPEC: C15. ROUTE: C14, R2. IMPRECISE: C1, C6, C16, C18, C20, C22. GAP: sun tanning.

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| q1, q2 | both ask "why" a wave suits a use — HT only | Usable on **CH TH only**. CF TF: none usable. |
| `higher` (TH/CH) | TIR off-spec; ultrasound physics-only HT | Do not use the TIR and ultrasound clauses on any route; ultrasound may appear on TH only. |

## 5. For the lesson author
**Misconceptions seen in AQA marking**: MRI uses X-rays; "microwaves cook from the inside out"; infrared cameras "see heat" vs detect IR emitted by warm objects; mixing up which end of the spectrum is ionising; giving a use without the matching property at HT ("microwaves for satellites because they are fast" — all EM waves travel at the same speed); "gamma is used for imaging bones".

**Command words**: Give (a use), Name (the wave), Explain why (HT), Suggest (a wave for a new use, HT), Evaluate (risk vs benefit, from data — 6.6.2.3).

**Required practical**: none.

## 6. Verdict
SOURCE HAS ERRORS. One WRONG statement (microwave-oven "water resonance… heats from inside", theory — re-cuttable). The `higher` field carries off-spec TIR and a physics-only ultrasound comparison. Both quiz items are correct, but both are HT "why suitable" items: usable on CH TH, none on CF TF. Spec's "sun tanning" use is missing. True routes CF CH TF TH, as the site ships.

**For Mide:** nothing.
