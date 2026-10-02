# Examination — Energy Changes in Systems (energy-changes-in-systems) — AQA 8463 4.1.1.3 / 8464 6.1.1.3
Verdict: SOURCE OK WITH FLAGS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-15/04-checked-science-source/physics-6.1.1.3-energy-changes-in-systems.md`.
Spec sources read as text: `AQA-8464-spec.txt` 6.1.1.3 (incl. RP14), 6.3.2.2, §10.2.14; `AQA-8463-spec.txt` 4.1.1.3 (incl. RP1), §8.2.1; both June 2026 equation sheets. Cross-read: `batch-3/examination/temperature-changes-shc.md` (sibling lesson, same equation).

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n (= opts index n). One route copy.

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 | **6.1.1.3** | Energy changes in systems | base |
| 8463 | **4.1.1.3** | Energy changes in systems | base |
| RP | **8464 RP14 = 8463 RP1** — printed at this section (the spec's home for it) | Specific heat capacity | base |
| Supporting | 8464 6.3.2.2 / 8463 4.3.2.2 (same equation, particle-model framing — sibling lesson temperature-changes-shc); 8464 6.2.4.2 / 8463 4.2.4.2 (E = Pt) | | base |

Spec statements (verbatim, 8463 = 8464): "The amount of energy stored in or released from a system as its temperature changes can be calculated using the equation: change in thermal energy = mass × specific heat capacity × temperature change ∆E = m c ∆θ" — "Students should be able to apply this equation which is given on the Physics equation sheet." Units: J, kg, J/kg °C, °C. "The specific heat capacity of a substance is the amount of energy required to raise the temperature of one kilogram of the substance by one degree Celsius." "Required practical activity 14 [8463: 1]: an investigation to determine the specific heat capacity of one or more materials. The investigation will involve linking the decrease of one energy store (or work done) to the increase in temperature and subsequent increase in thermal energy stored." AT 1 and 5.

Sheet status: ΔE = m c Δθ printed on both June 2026 sheets ("On the sheet"). E = P t printed on both ("On the sheet").

## 2. Route table
| # | teachable point | true layer | spec | verdict |
|---|---|---|---|---|
| R1 | SHC definition, ΔE = mcΔθ, units, typical values (theory 1; equations; variables; key_note) | base | 6.1.1.3 | OK |
| R2 | Rearrangements; Examples 1–2 (theory 2) | base | 6.1.1.3; MS 3b | OK |
| R3 | Δθ = final − initial; g → kg (common_mistake) | base | MS 3c | OK |
| R4 | FIFA (0.5 kg water) | base | 6.1.1.3 | OK; Convert line corrected (C16) |
| R5 | Water's high SHC: radiators, car cooling, oceans (theory 3; q2) | base (context) | 6.1.1.3 | OK |
| R6 | RP: heater of known power, E = Pt, rearrange for c, sources of error, lagging (theory 3; rp) | base — RP14 / RP1 | 6.1.1.3 / 4.1.1.3 | OK science; **numbering ROUTE** (C10, C17) |
| R7 | q1 iron block cooling | base | 6.1.1.3 | OK — usable all routes |
| R8 | q2 water in central heating | base | 6.1.1.3 | OK with imprecisions — usable all routes |
| — | `higher` | none | — | correct: no HT, no physics-only content |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | theory 1 | SHC definition (1 kg by 1 °C) | OK | Spec wording. | 6.1.1.3 |
| C2 | theory 1 | ΔE = m × c × Δθ; J, kg, J/kg°C, °C | OK | — | 6.1.1.3 |
| C3 | theory 1 | water 4200; aluminium 900; iron/steel 450; copper 385 J/kg°C | OK | Data-book values (steel 420–490). | — |
| C4 | theory 1 | water's high SHC → good for carrying/storing thermal energy | OK | — | — |
| C5 | theory 2 | Δθ = ΔE ÷ (m × c); m = ΔE ÷ (c × Δθ); c = ΔE ÷ (m × Δθ) | OK | — | MS 3b |
| C6 | theory 2 Ex 1 | 2 kg water 20→100 °C: 2 × 4200 × 80 = 672,000 J = 672 kJ | OK | ✓ | — |
| C7 | theory 2 Ex 2 | 27,000 J, 3 kg Al: Δθ = 27,000 ÷ 2700 = 10 °C | OK | ✓ | — |
| C8 | theory 2 | same equation for cooling (energy released) | OK | Spec: "stored in or released from". | 6.1.1.3 |
| C9 | theory 3 | radiators, car cooling, coastal climate | OK | Context only. | — |
| C10 | theory 3 | "RP14 — Determine the SHC of a material" | ROUTE | RP14 is the **Combined (8464)** number; Physics (8463) is **RP1**. Route-aware badge. | 8464 6.1.1.3; 8463 4.1.1.3 |
| C11 | theory 3 | method: heater of known power; record Δθ over time; E = P × t; compare with ΔE = mcΔθ → c | OK | This is a **two-equation chain** (E = Pt, then c = ΔE ÷ mΔθ). Rule 3 needs its own Step 1 / Step 2 worked example. The source has none (GAP, flag F2). | 6.1.1.3 RP |
| C12 | theory 3 | heat loss → measured c higher than true; incomplete transfer → same direction; lag to reduce | OK | Energy supplied is overcounted, Δθ is smaller, so c = E/(mΔθ) is too big. ✓ | 8463 §8.2.1 (WS 3.7) |
| C13 | common_mistake | Δθ = final − initial; g ÷ 1000 → kg | OK | — | MS 3c |
| C14 | key_note | summary | OK | "RP14" numbering as C10. | — |
| C15 | FIFA | 0.5 × 4200 × 60 = 0.5 × 252,000 = 126,000 J | OK | ✓ | — |
| C16 | FIFA Convert `[NEW]` | "…a °C difference equals the same-sized K difference…" | IMPRECISE → corrected | Kelvin is not in 6.1.1.3 and only confuses. Corrected line written into the source: "Nothing to convert — mass is already in kg and c is already in J/kg°C. Working out Δθ = 85 − 25 = 60°C is part of Insert, not a unit conversion." | CFIFA amendment |
| C17 | rp | "RP14 (Physics) — … electric heater, thermometer and balance. E = Pt gives energy input; rearrange ΔE = mcΔθ to find c." | ROUTE | Science OK (also needs a timer, or a joulemeter instead of P and t). Label "(Physics)" is wrong: 14 is the Combined number; Physics is RP1. Frozen; badge route-aware. | 8464 RP14 / 8463 RP1 |
| C18 | variables | ΔE, m, c, Δθ with units | OK | — | — |
| C19 | q1 key | 2 kg iron 150→30 °C: 2 × 450 × 120 = 108,000 J | OK | ✓ | — |
| C20 | q1 opt 1 / wx1 | 27,000 J = 2 × 450 × 30 (final temperature used) | OK, aligned | ✓ | — |
| C21 | q1 opt 2 / wx2 | 135,000 J = 2 × 450 × 150 (initial temperature used) | OK, aligned | ✓ | — |
| C22 | q1 opt 3 / wx3 | "1350 J — divided instead of multiplied" / "requires multiplication — 108,000 J" | IMPRECISE (minor) | No natural division of the given numbers gives 1350. The distractor is untraceable but harmless, and wx3 is true. Usable. | — |
| C23 | q2 stem | "…rather than a cheaper liquid?" | IMPRECISE (minor) | Water is about the cheapest liquid there is, so the premise is odd. Same finding as batch-3 temperature-changes-shc C22. Key reasoning right. | — |
| C24 | q2 key | high SHC → large energy per kg per °C → less water needed | OK | — | — |
| C25 | q2 opt 1 / wx1 | low SHC would lose heat quickly and carry less | OK, aligned | — | — |
| C26 | q2 opt 2 / wx2 | option "denser than most liquids"; wx "Water is less dense than many metals — density is not the primary reason" | IMPRECISE (minor) | The wx compares with metals while the option compares with liquids. Its conclusion (density is not the reason) is right. Usable. | — |
| C27 | q2 opt 3 / wx3 | SHC does not become zero; roughly constant | OK, aligned | — | — |
| C28 | matching (to be replaced) | four pairs | OK | — | — |

Count: **0 WRONG**. **ROUTE**: C10/C14/C17 (RP number). **IMPRECISE**: C16 (corrected), C22, C23, C26. **GAP**: the chained RP calculation has no worked example, and there is no conversion example (g → kg) for CFIFA.

## 4. Frozen items wrong for their route
None. q1 and q2 are both usable verbatim on all four routes.

## 5. For the lesson author
**Duplication risk.** The frozen data is almost a copy of batch-3 `temperature-changes-shc` (same three theory headings, same iron-block and water-coolant quiz shapes). The spec gives each lesson a different job. 6.1.1.3 (this one) is the **energy** framing and the **RP's home**: energy stored in or released from a system, and the RP linking "the decrease of one energy store (or work done) to the increase in temperature". 6.3.2.2 is the **particle-model** framing: the temperature rise depends on the mass, the material and the energy input. Build this lesson around the RP and the E = Pt → c chain.

**Misconceptions seen in AQA marking**: final temperature used as Δθ; grams left as grams; time in minutes in E = Pt; thinking heat losses make c too low; "high SHC heats up quickly".

**Typical questions** ⚑ examiner-drafted
- *A 1.0 kg aluminium block is heated by a 50 W heater for 10 minutes. Its temperature rises from 20 °C to 52 °C. Calculate the specific heat capacity of aluminium. [4]* — t = 600 s, E = 50 × 600 = 30,000 J (1); Δθ = 32 °C (1); c = 30,000 ÷ (1.0 × 32) (1) = 937.5 ≈ 940 J/kg °C (1).
- *Explain why the value obtained is higher than the true value. [2]* — energy lost to the surroundings (1); so less energy reaches the block than was supplied / the temperature rise is smaller than it should be (1).

## 6. Verdict
SOURCE OK WITH FLAGS. All 6 calculations check. Both quiz items are usable on all routes. The RP is mislabelled "(Physics)": it is Combined RP14 / Physics RP1. The Convert line has been corrected. The two-step RP calculation needs its own worked example (rule 3).

**For Mide:** nothing science-related. One build note (not science): the live batch-3 `temperature-changes-shc` already carries the full SHC RP block. When Design rebuilds batch 3, that block should become a link to this lesson, the RP's spec home.
