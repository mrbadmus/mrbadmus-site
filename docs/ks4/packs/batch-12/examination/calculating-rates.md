# Examination — Rate of Reaction and Calculations (calculating-rates) — AQA 8464 5.6.1.1 / 8462 4.6.1.1
Verdict: SOURCE HAS ERRORS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-12/04-checked-science-source/chemistry-5.6.1.1-calculating-rates.md`.
Spec sources read as text: `AQA-8464-spec.txt` 5.6.1.1–5.6.1.3; `AQA-8462-spec.txt` 4.6.1.1–4.6.1.3 (identical wording, except the RP number). No equation sheet applies (chemistry). Route audit read: `chemistry.md` row `calculating-rates` (OK, base, CF CH TF TH; HT layer: mol/s, tangent gradient).

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n; th1–th3 = theory chunks. TH and CH copies carry a `higher` field; CF and TF copies' `higher` is null.

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 | **5.6.1.1** | Calculating rates of reactions | base; one sentence and one bullet (HT only) |
| 8462 | **4.6.1.1** | Calculating rates of reactions | as above |
| Supporting | 8464 5.6.1.2 / 8462 4.6.1.2 — the rate required practical: **Combined RP 11, Chemistry RP 5** | | base |
| Supporting | 8464 5.3.2.1 / 8462 4.3.2.1 moles (HT) — for rates in mol/s | | higher |

Spec statement (verbatim, 8464 = 8462): "The rate of a chemical reaction can be found by measuring the quantity of a reactant used or the quantity of product formed over time: mean rate of reaction = quantity of reactant used / time taken; mean rate of reaction = quantity of product formed / time taken. The quantity of reactant or product can be measured by the mass in grams or by a volume in cm³. The units of rate of reaction may be given as g/s or cm³/s. For the Higher Tier, students are also required to use quantity of reactants in terms of moles and units for rate of reaction in mol/s. Students should be able to: • calculate the mean rate of a reaction from given information about the quantity of a reactant used or the quantity of a product formed and the time taken • draw, and interpret, graphs showing the quantity of product formed or quantity of reactant used up against time • draw tangents to the curves on these graphs and use the slope of the tangent as a measure of the rate of reaction • (HT only) calculate the gradient of a tangent to the curve on these graphs as a measure of rate of reaction at a specific time." (MS 1a, 1c, 1d, 4a–4e)

RP (verbatim, 8464 5.6.1.2): "Required practical activity 11: investigate how changes in concentration affect the rates of reactions by a method involving measuring the volume of a gas produced and a method involving a change in colour or turbidity. This should be an investigation involving developing a hypothesis." 8462 4.6.1.2: identical text as "Required practical 5".

## 2. Route table
| # | teachable point | true layer | spec | verdict |
|---|---|---|---|---|
| R1 | Rate = how fast reactants used / products formed; fast and slow examples (th1) | base | 5.6.1.1 | OK |
| R2 | Ways to follow a reaction: mass, gas volume, colour/turbidity (th1; th3) | base | 5.6.1.1; 5.6.1.2 RP | OK |
| R3 | Mean rate = quantity ÷ time; units g/s, cm³/s (th2; equations 1; key_note; variables; FIFA; q1) | base | 5.6.1.1 | OK |
| R4 | Rate in mol/s using moles | **higher** | 5.6.1.1 "For the Higher Tier…" | **GAP** — missing from the source |
| R5 | "mol/dm³/s" (th2; key_note) | off-spec | — | OFF-SPEC (CR-F3) |
| R6 | Quantity–time graphs; steeper = faster; curve flattens as a reactant runs out (th2; common_mistake; q2) | base | 5.6.1.1 | OK (C9 imprecise) |
| R7 | Draw a tangent; its slope is a measure of rate (th2 "instantaneous rate"; equation 2; `higher` sentence 1–2) | **base** | 5.6.1.1 bullet 3 | ROUTE: `higher` carries it CH/TH only; th2 carries it on all routes |
| R8 | Calculate the gradient of a tangent at a specific time | **higher** | 5.6.1.1 bullet 4 (HT only) | OK in principle; no worked example in source (GAP) |
| R9 | Rate–concentration graphs, proportionality (`higher` sentence 3) | base (5.6.1.3 proportionality, MS 1c) | 5.6.1.3 | ROUTE — not HT; and its home is collision-theory |
| R10 | RP: gas collection, mass loss, thiosulfate cross (th3; rp) | base | 5.6.1.2 (RP's home) | rp field WRONG number and method (CR-F1) |
| R11 | q1, q2 | base | 5.6.1.1 | OK |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | th1 | fast: explosions, burning, acid + reactive metal; slow: rusting, paint drying, decay | OK | ✓ | — |
| C2 | th1 | follow mass, volume, concentration, gas, colour/turbidity | OK | ✓ | 5.6.1.1 |
| C3 | th2 | Rate = quantity ÷ time | IMPRECISE (minor) | Spec name is "mean rate of reaction"; the FIFA question uses it. Say "mean rate" in the formula. | 5.6.1.1 |
| C4 | th2 | units cm³/s or cm³/min; g/s or g/min | OK | Spec gives g/s and cm³/s; per minute is fine if asked. | 5.6.1.1 |
| C5 | th2; key_note | "If measuring CONCENTRATION: rate = mol/dm³/s" | OFF-SPEC | Not a GCSE unit. The HT unit is **mol/s** (moles of reactant used / product formed per second) — and it is missing. | 5.6.1.1 |
| C6 | th2 | gradient of quantity–time graph = rate; steep = fast; flat = slow/finished; gradient decreases over time | OK | ✓ | 5.6.1.1 |
| C7 | th2 | 60 cm³ in 120 s → 0.5 cm³/s | OK | ✓ | — |
| C8 | th2 | mean rate = total ÷ total time; instantaneous rate = gradient of tangent at a point | OK | Drawing the tangent and using its slope = base; calculating its gradient = HT. | 5.6.1.1 |
| C9 | common_mistake | "fewer reactant particles mean fewer collisions… flattens out when the reaction is complete (all reactants used)" | IMPRECISE | Lower concentration → fewer collisions **per second**; the curve flattens when **one** reactant (the limiting one) is used up, not all. "Closed system" is not needed (gas collection is open). | 5.6.1.3 |
| C10 | key_note | as th2; "mol/dm³/s" | OFF-SPEC | As C5. | — |
| C11 | equations | "Rate = quantity of product formed (or reactant used) ÷ time"; "Rate = gradient of graph of quantity vs time" | OK | Frozen; teach as "mean rate" (C3); gradient-of-tangent is the measure at an instant. | 5.6.1.1 |
| C12 | th3 | gas over water in inverted measuring cylinder or gas syringe; Mg + 2HCl → MgCl₂ + H₂ | OK | ✓ balanced | 5.6.1.2 RP |
| C13 | th3 | mass loss on a balance; CaCO₃ + 2HCl → CaCl₂ + H₂O + CO₂ | OK | ✓ balanced. Not one of the RP's two named methods (C18). | — |
| C14 | th3 | colorimeter; thiosulfate + HCl → sulfur clouds; cross disappears; time "inversely proportional to rate" | OK | ✓ (rate ∝ 1/time is the AQA measure). | 5.6.1.2 RP |
| C15 | `higher` | tangents for instantaneous rate; compare initial gradients | ROUTE | Drawing and using tangents is base (bullet 3); only calculating the gradient is HT (bullet 4). | 5.6.1.1 |
| C16 | `higher` | "rate-concentration graphs — linear relationship indicates rate directly proportional to concentration" | ROUTE | Proportionality is base 5.6.1.3 (MS 1c); not HT. | 5.6.1.3 |
| C17 | rp | "RP6 (Chemistry)" | **WRONG** | Chemistry is **RP 5** (8462 4.6.1.2); Combined is **RP 11** (8464 5.6.1.2). There is no RP6 for rates on either spec (8462 RP6 is chromatography). | 8462 4.6.1.2; 8464 5.6.1.2 |
| C18 | rp | "…sodium thiosulfate… (cross disappears). Alternatively: … marble chips and HCl by mass loss or gas collection." | **WRONG** | The RP requires **both** a gas-volume method **and** a colour/turbidity method, as one investigation with a hypothesis, varying **concentration**. "Alternatively" is wrong, and mass loss is not one of the two named methods. | 8464 5.6.1.2; 8462 4.6.1.2 |
| C19 | variables | rate, "cm³/s or g/s" | OK (base) | HT adds mol/s. | 5.6.1.1 |
| C20 | FIFA | 84 cm³ in 60 s → 1.4 cm³/s | OK | ✓ | — |
| C21 | Convert (NEW) | "Nothing to convert — the volume (cm³) and time (already in seconds) match the cm³/s answer unit directly (contrast this lesson's own quiz q1…)" | OK | ✓ examined. q1 is the ready-made wrong-unit example (minutes → s). | CFIFA amendment |
| C22 | q1 key | 120 cm³ in 4 min → 120 ÷ 240 = 0.5 cm³/s | OK | ✓ | 5.6.1.1 |
| C23 | q1 opt1 / wx1 | "30 cm³/s — 120 ÷ 4" / not converted to seconds | OK | Aligned ✓ (30 is cm³/min) | — |
| C24 | q1 opt2 / wx2 | "480 — 120 × 4" / multiplies | OK | Aligned ✓ | — |
| C25 | q1 opt3 / wx3 | "2 cm³/s — 120 ÷ 60" / divided by 60 not 240 | OK | Aligned ✓ | — |
| C26 | q2 key | steeper gradient = faster rate | OK | ✓ | 5.6.1.1 |
| C27 | q2 opt1–3 / wx1–3 | slower / complete / more reactant added | OK | All aligned ✓ | — |
| C28 | matching (to be replaced) | five pairs | OK | ✓ | — |

Count: **2 WRONG** (C17, C18 — both in the frozen `rp` field). OFF-SPEC: C5/C10. IMPRECISE: C3, C9. ROUTE: C15, C16. GAP: HT mol/s (R4); no worked tangent-gradient example (R8). 5 calculations rechecked, all ✓.

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| q1 | correct; base | Usable on CF CH TF TH. It is the Convert (min → s) item. |
| q2 | correct; base | Usable on all four routes. |
| FIFA | correct | Keep; it is the "nothing to convert" example. |
| rp | wrong RP number; wrong "alternatively" method | **Do not use as written** (CR-F1). Use the spec's RP text above. |

## 5. Calculations and chains (rule 3)
- Mean rate = quantity ÷ time (g/s, cm³/s) — one step. Convert: minutes → s (q1: 4 min = 240 s). Base.
- Mean rate in mol/s (HT) — **chain**: Step 1 n = m ÷ Mr (or given moles); Step 2 mean rate = n ÷ t. Convert min → s may sit in front. Not in the source.
- Gradient of a tangent (HT) — read two points on the drawn tangent; gradient = change in quantity ÷ change in time; unit cm³/s or g/s. Not a chain of equations, but needs its own worked example before a pupil does one (rule 3). Not in the source.
- Rate from the RP cross method: relative rate = 1 ÷ time (s⁻¹). Base; one step.

## 6. Verdict
SOURCE HAS ERRORS — both errors are in the frozen `rp` field (wrong RP number; wrong "alternatively" method). The science and arithmetic elsewhere are right, both quiz items are correct and usable on all four routes, and the FIFA and its Convert line are fine. The HT content the spec names (mol/s; calculating a tangent's gradient) is missing or unexemplified, "mol/dm³/s" is off-spec, and drawing tangents is base though the `higher` field reserves it for Higher. Nothing for Mide.
