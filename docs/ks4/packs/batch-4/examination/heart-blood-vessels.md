# Examination — The Heart and Blood Vessels (heart-blood-vessels) — AQA 8464 4.2.2.2 / 8461 4.2.2.2
Verdict: SOURCE HAS ERRORS (one WRONG frozen wrong_explanation; three spec-core gaps; `higher` block mis-tagged)
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-4/04-checked-science-source/biology-4.2.3-heart-blood-vessels.md`.
Spec sources read: `AQA-8464-spec.txt` 4.2.2.2–4.2.2.4; `AQA-8461-spec.txt` 4.2.2.2–4.2.2.4 (wording identical); 8464 4.3.1.6 (white blood cells) for cross-reference. Route audit: `ks4-routes/docs/ks4/route-audit/biology.md` row `heart-blood-vessels` (CF CH TF TH, OK). No equation sheet applies (biology).

Conventions: q1–q4 = quiz items; "wx n" = `wrong_explanations` key n; T1–T5 = theory chunks in order. The file's own spec label "4.2.3" is the site's numbering; AQA's is 4.2.2.2 in both 8461 and 8464.

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 | **4.2.2.2** | The heart and blood vessels | base |
| 8461 | **4.2.2.2** | The heart and blood vessels | base |
| Supporting | 8464/8461 4.2.2.4 (valves, artificial hearts, evaluation — the `higher` block's content) | | base |

Spec statements (verbatim, 8464 = 8461):
- "Students should know the structure and functioning of the human heart and lungs, including how lungs are adapted for gaseous exchange."
- "The heart is an organ that pumps blood around the body in a double circulatory system. The right ventricle pumps blood to the lungs where gas exchange takes place. The left ventricle pumps blood around the rest of the body."
- "Knowledge of the blood vessels associated with the heart is limited to the aorta, vena cava, pulmonary artery, pulmonary vein and coronary arteries. Knowledge of the names of the heart valves is not required."
- "Knowledge of the lungs is restricted to the trachea, bronchi, alveoli and the capillary network surrounding the alveoli."
- "The natural resting heart rate is controlled by a group of cells located in the right atrium that act as a pacemaker. Artificial pacemakers are electrical devices used to correct irregularities in the heart rate."
- "The body contains three different types of blood vessel: arteries, veins, capillaries. Students should be able to explain how the structure of these vessels relates to their functions."
- "Students should be able to use simple compound measures such as rate and carry out rate calculations for blood flow." (MS 1a, 1c)

No "(HT only)" and no "(biology only)" label anywhere in 4.2.2.2. Every point is base.

## 2. Route table
| # | teachable point | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Double circulatory system; pulmonary and systemic circuits (T1) | base | 4.2.2.2 | all four | OK |
| R2 | Four chambers; aorta, vena cava, pulmonary artery, pulmonary vein (T2) | base | 4.2.2.2 | all four | OK |
| R3 | Left ventricle thicker wall (T2; key_note; q1) | base | 4.2.2.2 | all four | OK |
| R4 | Valves prevent backflow (T2) | base | 4.2.2.2 | all four | OK; valve NAMES off-spec (C6) |
| R5 | Cardiac muscle; coronary arteries supply heart muscle (T2) | base | 4.2.2.2 | all four | OK / IMPRECISE (C7) |
| R6 | Arteries — structure ↔ function (T3; q3) | base | 4.2.2.2 | all four | OK / IMPRECISE (C10) |
| R7 | Veins — structure ↔ function, valves (T4; q3) | base | 4.2.2.2 | all four | OK |
| R8 | Capillaries — one cell thick, exchange by diffusion (T5; q4) | base | 4.2.2.2 | all four | OK; q4 wx1 WRONG |
| R9 | common_mistake — pulmonary artery/vein exceptions; A = away | base | 4.2.2.2 | all four | OK |
| R10 | key_note | base | 4.2.2.2 | all four | OK |
| R11 | `higher`: artificial pacemakers | **base** | 4.2.2.2 | CH, TH only (CF/TF copy = null) | ROUTE — mis-tagged; base |
| R12 | `higher`: faulty valves replaced by biological/mechanical valves | **base** | 4.2.2.4 | CH, TH only | ROUTE — base; belongs to CHD lesson |
| R13 | `higher`: artificial hearts | **base** | 4.2.2.4 | CH, TH only | ROUTE — base; belongs to CHD lesson |
| R14 | `higher`: evaluate drugs vs mechanical devices vs transplant | **base** | 4.2.2.4 | CH, TH only | ROUTE — base; belongs to CHD lesson |
| R15 | q1–q4 | base | 4.2.2.2 | all four | q1–q3 OK; q4 not usable as written |
| — | Lungs: trachea, bronchi, alveoli, capillary network; adaptation for gas exchange | base | 4.2.2.2 | **absent** | GAP |
| — | Natural pacemaker cells in the right atrium | base | 4.2.2.2 | **absent** | GAP |
| — | Rate calculations for blood flow | base | 4.2.2.2 (MS 1a, 1c) | **absent** | GAP |
| — | RP, equations, FIFA, examiner_tip | none in source | — | — | correct: no RP in 4.2.2.2 |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | T1 | Blood passes through the heart twice per complete circuit; pulmonary R→lungs→L; systemic L→body→R | OK | — | 4.2.2.2 |
| C2 | T1 | Two circuits keep oxygenated and deoxygenated blood separate; left side pumps to body at high pressure | OK | — | 4.2.2.2 |
| C3 | T2 | RA ← vena cava; RV → pulmonary artery; LA ← pulmonary vein; LV → aorta | OK | — | 4.2.2.2 |
| C4 | T2 | LV wall thicker — pumps to whole body, needs higher pressure than RV (lungs only) | OK | — | 4.2.2.2 |
| C5 | T2 | Valves open with pressure difference and close to prevent backflow; closing makes 'lub-dub' | OK | Sound from valve closure ✓ (context, not examinable). | — |
| C6 | T2 | "Atrioventricular (AV) valves … Semilunar valves" | OFF-SPEC | Correct biology, but "Knowledge of the names of the heart valves is not required." Do not test names; label simply "valve". | 4.2.2.2 |
| C7 | T2 | Cardiac muscle "contracts and relaxes rhythmically, never getting tired" | IMPRECISE | Cardiac muscle is highly resistant to fatigue; "never" overstates. Say "does not fatigue like skeletal muscle". Off-spec detail anyway. | — |
| C8 | T2 | Coronary arteries supply heart muscle with oxygenated blood; blockage → heart attack | OK | — | 4.2.2.2; 4.2.2.4 |
| C9 | T3 | Arteries: away from heart; thick muscular walls; elastic fibres stretch and recoil | OK | Matches AQA mark-scheme language. | 4.2.2.2 |
| C10 | T3 | "NO valves" in arteries, vs T2 "Semilunar valves — in the pulmonary artery and aorta" | IMPRECISE | Internal contradiction. The semilunar valves sit at the exits of the ventricles, where the aorta and pulmonary artery leave the heart; arteries have no valves along their length. Re-cut both lines to say so. | — |
| C11 | T3 | Narrow lumen helps maintain high pressure | OK | GCSE-creditworthy. | — |
| C12 | T3 | Pulmonary artery carries deoxygenated blood | OK | — | 4.2.2.2 |
| C13 | T4 | Veins: towards heart; thinner walls; lower pressure; wider lumen; valves prevent backflow | OK | (Wide lumen reduces resistance to the low-pressure flow.) | 4.2.2.2 |
| C14 | T4 | Pulmonary vein carries oxygenated blood to the left atrium | OK | — | 4.2.2.2 |
| C15 | T5 | Capillaries one cell thick → short diffusion distance; narrow, RBCs in single file; dense network, large surface area | OK | "shortest possible" is loose; "short" is the creditworthy word. | 4.2.2.2 |
| C16 | T5 | O₂ and glucose diffuse out; CO₂ and wastes diffuse in; down concentration gradients; no energy | OK | — | 4.1.3.1 |
| C17 | common_mistake | Pulmonary artery deoxygenated; pulmonary vein oxygenated; direction not oxygen defines A/V | OK | — | 4.2.2.2 |
| C18 | key_note | as above | OK | — | — |
| C19 | `higher` | Artificial pacemakers correct irregular rhythms | OK, **mis-tagged** | Base, 4.2.2.2. Also the natural pacemaker (right atrium) is base and missing (F4). | 4.2.2.2 |
| C20 | `higher` | Valves replaced with biological (pig/cow) or mechanical valves; artificial hearts; evaluation | OK, **mis-tagged** | Base, 4.2.2.4 — CHD lesson's spec. | 4.2.2.4 |
| C21 | q1 key | LV pumps to whole body — higher pressure than RV | OK | — | 4.2.2.2 |
| C22 | q1 wx1 | Both ventricles receive same volume per beat | OK | Stroke volumes equal ✓. | — |
| C23 | q1 wx2, wx3 | body-side size irrelevant; oxygenated/deoxygenated blood same density | OK | — | — |
| C24 | q2 key | Pulmonary artery carries deoxygenated blood | OK | — | 4.2.2.2 |
| C25 | q2 wx1–wx3 | arteries = away not oxygen; no mixing in a healthy heart; all blood has RBCs | OK | — | — |
| C26 | q3 key | Vein pressure low — valves prevent backflow; arterial pressure keeps flow one way | OK | — | 4.2.2.2 |
| C27 | q3 wx1, wx2 | wall thickness ≠ backflow; oxygen content irrelevant | OK | — | — |
| C28 | q3 wx3 | "Valves in veins do slightly slow flow, but that's acceptable…" | IMPRECISE | Answers the wrong vessel: option 4 is about arteries. The point to make: arteries need no valves because high pressure keeps blood moving one way. Not false — item usable. | — |
| C29 | q4 key | One cell thick — short diffusion distance; dense network — large surface area | OK | — | 4.2.2.2 |
| C30 | q4 wx1 | "Capillaries have the LOWEST blood pressure — that is why they can be one cell thick without bursting." | **WRONG** | Pressure falls continuously round the circuit: arteries > capillaries > veins. The **veins** (vena cava) have the lowest pressure. Capillary pressure is lower than arterial, not lowest. **q4 not usable as written.** Correct wx1: "Arteries have the highest blood pressure. Pressure has already dropped a lot by the time blood reaches the capillaries." | 4.2.2.2 (vein low pressure, T4 of this file) |
| C31 | q4 wx2 | "carry either oxygenated or deoxygenated blood depending on location — not both at once" | IMPRECISE | In a body capillary, blood enters oxygenated and leaves deoxygenated — oxygen content changes along it. Better: "Which blood a capillary carries is not what makes it good at exchange — thin walls and large surface area are." | — |
| C32 | q4 wx3 | No valves; diffusion down concentration gradients | OK | — | — |
| C33 | matching (to be replaced) | six pairs | OK | All correct. | — |
| C34 | — | `[NEW — to be examined]` Convert lines | n/a | None present in this file (no calculation in the source). | — |

Count: **1 WRONG** (C30, q4 wx1). **IMPRECISE**: C7, C10, C28, C31. **OFF-SPEC**: C6. **ROUTE**: C19, C20 (whole `higher` block is base). **GAP**: lungs; natural pacemaker; blood-flow rate calculations.

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| q4 | wx1 states a false fact (capillaries lowest pressure) | Do not use as written. Stem, options and key are correct; Design may re-author with the corrected wx1 (C30) and wx2 (C31) as a new item. |
| `higher` block | Base content (4.2.2.2, 4.2.2.4) shown only on CH/TH | Teach pacemakers (artificial AND natural) as base on all four routes; move valves/artificial hearts/evaluation to the CHD lesson as base. |
| q1, q2, q3 | Correct, base | Usable on all four routes. |

## 5. For the lesson author
**Misconceptions seen in AQA marking**
- "Arteries carry oxygenated blood, veins carry deoxygenated" (the pulmonary exceptions).
- "Left ventricle is thicker because it holds more blood."
- "Blood goes round once" / single-loop circulation; right and left sides swapped (diagram viewed as the patient's left, not the reader's).
- "Capillaries have thin walls so blood flows fast" — the thin wall is for diffusion distance.
- "The heart gets its oxygen from the blood inside its chambers" — it is supplied by the coronary arteries.
- "Valves are in all vessels" — in veins (and the heart), not along arteries.

**Command words**: Name, Label, Describe, Explain (structure → function), Calculate (rate of blood flow, heart rate), Compare (artery vs vein).

**Typical questions** ⚑ examiner-drafted
- *Name the blood vessel that carries blood from the lungs to the heart. [1]* — pulmonary vein.
- *Explain why the wall of the left ventricle is thicker than the wall of the right ventricle. [2]* — more muscle / contracts more strongly (1); to pump blood (at higher pressure) all round the body, not just to the lungs (1).
- *Explain how the structure of a capillary is adapted to its function. [2]* — wall one cell thick (1); short diffusion distance for exchange of substances (1).
- *Explain why veins have valves. [2]* — blood at low pressure (1); valves stop backflow (1).
- *Where is the natural pacemaker of the heart found? [1]* — right atrium.
- *A heart pumps 4900 cm³ of blood in 70 beats. Calculate the volume pumped per beat. [2]* — 4900 ÷ 70 (1) = 70 cm³ (1).
- *Blood flows through an artery at 0.5 dm³ in 6 s. Calculate the rate of blood flow in dm³ per minute. [2]* — 0.5 ÷ 6 = 0.083 dm³/s (1); × 60 = 5 dm³/min (1).

**Required practical**: none.

**Equations**: rate of blood flow = volume of blood ÷ time — Learn it (no biology equation sheet; spec MS 1a, 1c). Heart rate (beats per minute) = number of beats ÷ time in minutes — Learn it.

## 6. Verdict
SOURCE HAS ERRORS. All theory science is correct bar small imprecisions, and q1–q3 are usable on every route. One frozen wrong_explanation (q4 wx1) is false and makes q4 unusable as written. The `higher` block is entirely base content, hidden from Foundation pupils. Three spec-core statements are missing from the frozen data — the lungs, the natural pacemaker and blood-flow rate calculations — and are now added to the source file from the spec.

**For Mide:** nothing. Every point is a settled fact.
