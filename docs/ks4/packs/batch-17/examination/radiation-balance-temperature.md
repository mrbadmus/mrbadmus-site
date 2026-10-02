# Examination — Radiation Balance and Earth's Temperature (radiation-balance-temperature) — AQA 8463 4.6.3.2 (HT)
Verdict: SOURCE OK WITH FLAGS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-17/04-checked-science-source/physics-6.6.5.4-radiation-balance-temperature.md`.
Spec sources read as text: `AQA-8463-spec.txt` (v1.1) §4.6.3.1–4.6.3.2; `AQA-8464-spec.txt` (v1.1) §6.6 (no black-body section) and §5.9.2 (greenhouse, chemistry); `AQA-8462-spec.txt` §4.9.2.1–4.9.2.3. Route audit `physics.md` row `radiation-balance-temperature`. Batch-4 examination `infrared-black-bodies.md` (IRB-F5), for the boundary.

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n; T1–T3 = theory chunks. One route copy (TH).

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8463 | **4.6.3.2** | Perfect black bodies and radiation — HT lines | (physics only) (HT only) |
| 8463 | 4.6.3.1 / 4.6.3.2 base lines (all bodies emit; distribution depends on T) | | (physics only) |
| 8464 | — | no equivalent in Combined physics | — |
| Related | 8462 4.9.2.1 / 8464 5.9.2.1 greenhouse gases; 8462 4.9.2.2–4.9.2.3 human activity, climate change | | base chemistry |

The data's spec "6.6.5.4" does not exist in 8464 (6.6 ends at 6.6.4). The true ref is 8463 4.6.3.2 (HT only), in a "(physics only)" section — triple-higher.

Spec statements (verbatim, 8463 4.6.3.2): "(HT only) A body at constant temperature is absorbing radiation at the same rate as it is emitting radiation. The temperature of a body increases when the body absorbs radiation faster than it emits radiation. (HT only) The temperature of the Earth depends on many factors including: the rates of absorption and emission of radiation, reflection of radiation into space. (HT only) Students should be able to explain how the temperature of a body is related to the balance between incoming radiation absorbed and radiation emitted, using everyday examples to illustrate this balance, and the example of the factors which determine the temperature of the Earth. (HT only) Students should be able to use information, or draw/interpret diagrams to show how radiation affects the temperature of the Earth's surface and atmosphere."
8462 4.9.2.1: "Students should be able to describe the greenhouse effect in terms of the interaction of short and long wavelength radiation with matter."

## 2. Route table
| # | teachable point | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Constant T ⇔ absorb rate = emit rate; absorb > emit → rises (T1; key_note; matching) | triple-higher | 4.6.3.2 (HT) | TH | OK |
| R2 | Everyday examples of the balance | triple-higher | 4.6.3.2 (HT) | absent | GAP (F2) |
| R3 | Earth absorbs solar, emits IR; equilibrium sets ~15 °C (T1) | triple-higher | 4.6.3.2 (HT) | TH | IMPRECISE (F1) |
| R4 | Greenhouse effect: short λ in, long λ IR out, absorbed and re-emitted (T2; common_mistake; key_note; q1) | triple-higher here (base in chemistry) | 4.6.3.2 (HT); 8462 4.9.2.1 | TH | OK |
| R5 | Without greenhouse effect ~ −18 °C (T2; q2) | context | — | TH | OK |
| R6 | Enhanced greenhouse effect; human sources; climate effects (T2) | base chemistry (context here) | 8462 4.9.2.2–4.9.2.3 | TH | OK |
| R7 | Factors: solar intensity, albedo, GHG, volcanoes (T3; key_note) | triple-higher | 4.6.3.2 (HT) "reflection of radiation into space" | TH | OK; use spec wording (F3) |
| R8 | Mercury, Venus, Mars (T3) | off-spec context | — | TH | IMPRECISE (F4) |
| R9 | Hotter body → peak at shorter λ; Sun visible, Earth IR (T3) | triple | 4.6.3.2 ("intensity and wavelength distribution … depends on the temperature") | TH | OK |
| R10 | q1 — why GHGs absorb IR not visible | triple-higher | 4.6.3.2 (HT); 8462 4.9.2.1 | TH | OK; explanation beyond spec (F5) |
| R11 | q2 — temperature without greenhouse effect | context | — | TH | OK |
| — | Page as a whole | **triple-higher (TH)** | 8463 4.6.3.2 (physics only)(HT only) | TH | OK — matches |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | T1 | temperature set by balance of incoming and outgoing radiation; constant when absorbed rate = emitted rate; absorbed > emitted → rises; emitted > absorbed → falls | OK | Spec wording. | 4.6.3.2 (HT) |
| C2 | T1 | "INPUT: solar radiation (mostly visible light and UV from the Sun)" | IMPRECISE | Sunlight is roughly half infrared, ~40–45 % visible and under 10 % UV. Say "mostly visible light and infrared, with a little ultraviolet — short wavelengths compared with what Earth emits". | (F1) |
| C3 | T1 | Earth absorbs → warms → emits IR (longer λ, cooler than Sun) | OK | — | 4.6.3.2 |
| C4 | T1 | "At equilibrium: incoming solar power = outgoing infrared power" | IMPRECISE (minor) | Absorbed solar power = emitted IR power; part of the incoming radiation is reflected into space (a spec factor). | 4.6.3.2 (F1) |
| C5 | T1 | Earth average ~15 °C | OK | — | — |
| C6 | T2 | GHGs CO₂, H₂O, CH₄ absorb outgoing IR | OK | Spec names these three. | 8462 4.9.2.1 |
| C7 | T2 | visible passes through atmosphere "(not absorbed)" → absorbed by surface → IR → partly absorbed by GHGs → re-emitted in all directions | OK | "Mostly not absorbed" is more exact. | 8462 4.9.2.1 |
| C8 | T2 | without greenhouse effect ~ −18 °C | OK | ~255 K ✓ | — |
| C9 | T2 | enhanced effect: fossil fuels → CO₂, livestock → CH₄ | OK | — | 8462 4.9.2.2 |
| C10 | T2 | melting ice → sea level rise; extreme weather; shifting ecosystems | OK | Context (chemistry 4.9.2.3). | 8462 4.9.2.3 |
| C11 | T3 | factors: solar intensity; albedo; GHG concentration; volcanic CO₂ and SO₂ (aerosol cooling) | OK | Spec phrase is "reflection of radiation into space" — use it alongside or instead of "albedo". | 4.6.3.2 (F3) |
| C12 | T3 | Mercury: no atmosphere, extreme swings | OK | Context. | — |
| C13 | T3 | Venus "similar distance to Earth but thick CO₂ atmosphere → 465 °C" | IMPRECISE | Venus is about 0.7 × Earth's distance and gets nearly twice the solar intensity. The point stands better as: Venus is hotter than Mercury, which is closer to the Sun. 465 °C ✓. | (F4) |
| C14 | T3 | Mars thin atmosphere → −60 °C | OK / IMPRECISE (minor) | ≈ −60 °C ✓; also further from the Sun. Context. | (F4) |
| C15 | T3 | hotter → peak at shorter λ; Sun ~5500 °C → visible; Earth ~15 °C → IR | OK | ✓ | 4.6.3.2 |
| C16 | T3 | GHGs absorb IR but not visible — key to climate | OK | — | 8462 4.9.2.1 |
| C17 | `higher` | HT only — balance; greenhouse mechanism; evaluate effects of rising GHGs | OK | — | 4.6.3.2 (HT) |
| C18 | common_mistake | Earth emits IR; GHGs absorb outgoing IR not incoming visible; natural effect beneficial, enhanced is the problem | OK | — | 8462 4.9.2.1 |
| C19 | key_note | as above; "albedo" | OK | See C11. | — |
| C20 | q1 key | GHGs transparent to visible, absorb IR — molecular vibrations of CO₂ and H₂O match IR wavelengths | OK (beyond spec) | True; the vibrational-mode reason is A-level. The GCSE answer is "they transmit short-wavelength radiation and absorb long-wavelength radiation". | 8462 4.9.2.1 (F5) |
| C21 | q1 opt 2 / wx1 | GHGs transmit visible, don't reflect it | OK | Aligned. | — |
| C22 | q1 opt 3 / wx2 | GHGs throughout the lower atmosphere; absorb IR by vibration modes | OK | Aligned. | — |
| C23 | q1 opt 4 / wx3 | absorption depends on resonance with vibrational frequencies, not energy alone | OK (beyond spec) | Correct physics; A-level reasoning. Aligned. | (F5) |
| C24 | q2 key | ~ −18 °C; Earth would radiate more to space and settle colder | OK | "heat … insulation" loose; fine. | — |
| C25 | q2 opt 2 / wx1 | effect raises T by ~33 °C (−18 → +15) | OK | 15 − (−18) = 33 ✓. Aligned. | — |
| C26 | q2 opt 3 / wx2 | GHGs warm by absorbing outgoing IR, not cool by reflecting | OK | Aligned. | — |
| C27 | q2 opt 4 / wx3 | 0 °C not physically derived; −18 °C from solar input and albedo | OK | Aligned. | — |
| C28 | matching (to be replaced) | four pairs | OK | — | — |

Count: **0 WRONG**. **IMPRECISE**: C2, C4, C13, C14. **GAP**: everyday examples (spec-required). One arithmetic check (33 °C) ✓.

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| None wrong. | q1's reason is beyond GCSE but true. | Both usable on TH; teach the spec-level reason alongside q1 (F5). |

## 5. For the lesson author
**Misconceptions seen in AQA marking**
- "Greenhouse gases trap heat / sunlight" — the mark is for absorbing outgoing infrared (long wavelength) and re-emitting it.
- "The greenhouse effect is caused by the hole in the ozone layer."
- "Constant temperature means no radiation is being absorbed or emitted." — both continue at equal rates.
- "Earth emits the same radiation it receives." — it emits longer-wavelength IR because it is much cooler.
- "All the Sun's radiation reaches the ground and is absorbed." — some is reflected into space (clouds, ice).

**Command words**: Explain (the balance), Use the diagram / information, Describe (the greenhouse effect), Evaluate (effect of increasing CO₂), Give an everyday example.

**Typical questions** ⚑ examiner-drafted
- *(HT) A cup of tea on a table stays at room temperature. Explain why, in terms of radiation. [2]* — it absorbs radiation at the same rate (1) as it emits radiation (1).
- *(HT) Explain how an increase in carbon dioxide in the atmosphere could increase the Earth's temperature. [4]* — short-wavelength radiation from the Sun passes through (1); Earth's surface emits long-wavelength infrared (1); more CO₂ absorbs more of it and re-emits some back towards Earth (1); Earth absorbs radiation faster than it emits it until a new, higher equilibrium temperature (1).
- *(HT) Give two factors that affect the temperature of the Earth. [2]* — rate of absorption of radiation; rate of emission; reflection of radiation into space.

**Required practical**: none.

**Equations**: none.

**Boundaries**: `infrared-black-bodies` (TF TH) teaches all bodies emit IR and the black-body curves, and touches the HT balance in a TH layer (IRB-F5) — this page is the full treatment of the 4.6.3.2 HT lines; IRB should link here, not repeat it. Chemistry `greenhouse-gases` is the base home of the greenhouse effect; this page recalls it and adds the physics balance.

## 6. Verdict
SOURCE OK WITH FLAGS. Science sound; both quiz items usable on TH. Spec number in the data is wrong (true: 8463 4.6.3.2 (HT only), physics only). The spec-required everyday examples of the balance are missing. Four imprecisions in context lines (solar spectrum "mostly visible and UV", reflected share omitted from the balance, Venus "similar distance", Mars). Routes correct: TH only.

**For Mide:** none.
