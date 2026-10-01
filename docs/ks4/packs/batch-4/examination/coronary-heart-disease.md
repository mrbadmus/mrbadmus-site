# Examination — Coronary Heart Disease (coronary-heart-disease) — AQA 8464 4.2.2.4 / 8461 4.2.2.4
Verdict: SOURCE OK WITH FLAGS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-4/04-checked-science-source/biology-4.2.3.3-coronary-heart-disease.md`.
Spec sources read: `AQA-8464-spec.txt` 4.2.2.4, 4.2.2.6; `AQA-8461-spec.txt` 4.2.2.4, 4.2.2.6 (wording identical). Route audit: `ks4-routes/docs/ks4/route-audit/biology.md` row `coronary-heart-disease` (CF CH TF TH, OK).

Conventions: q1–q3 = quiz items; "wx n" = `wrong_explanations` key n; T1–T4 = theory chunks in order. The file's own label "4.2.3.3" is the site's numbering; AQA's is 4.2.2.4.

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 | **4.2.2.4** | Coronary heart disease: a non-communicable disease | base |
| 8461 | **4.2.2.4** | Coronary heart disease: a non-communicable disease | base |
| Supporting | 8464/8461 4.2.2.6 The effect of lifestyle on some non-communicable diseases (risk factors; "effects of diet, smoking and exercise on cardiovascular disease") | | base |

Spec statements (verbatim, 8464 = 8461):
- "Students should be able to evaluate the advantages and disadvantages of treating cardiovascular diseases by drugs, mechanical devices or transplant." (WS 1.3, 1.4: "Evaluate methods of treatment bearing in mind the benefits and risks associated with the treatment.")
- "In coronary heart disease layers of fatty material build up inside the coronary arteries, narrowing them. This reduces the flow of blood through the coronary arteries, resulting in a lack of oxygen for the heart muscle. Stents are used to keep the coronary arteries open. Statins are widely used to reduce blood cholesterol levels which slows down the rate of fatty material deposit."
- "In some people heart valves may become faulty, preventing the valve from opening fully, or the heart valve might develop a leak. Students should understand the consequences of faulty valves. Faulty heart valves can be replaced using biological or mechanical valves."
- "In the case of heart failure a donor heart, or heart and lungs can be transplanted. Artificial hearts are occasionally used to keep patients alive whilst waiting for a heart transplant, or to allow the heart to rest as an aid to recovery."
- 4.2.2.6: "Risk factors are linked to an increased rate of a disease. They can be: aspects of a person's lifestyle; substances in the person's body or environment. A causal mechanism has been proven for some risk factors, but not in others. • The effects of diet, smoking and exercise on cardiovascular disease."

No HT or biology-only label in 4.2.2.4 or 4.2.2.6. Every point is base.

## 2. Route table
| # | teachable point | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | CHD = coronary arteries narrowed; heart muscle short of oxygen (T1; key_note) | base | 4.2.2.4 | all four | OK |
| R2 | Fatty deposits build up, lumen narrows, flow falls; clot → heart attack (T2; q1) | base | 4.2.2.4 | all four | OK |
| R3 | Risk factors — lifestyle vs non-lifestyle (T3; q3) | base | 4.2.2.6 | all four | OK / IMPRECISE (C9, C10) |
| R4 | Statins (T4; q2 distractor) | base | 4.2.2.4 | all four | OK |
| R5 | Stents (T4; q2; common_mistake) | base | 4.2.2.4 | all four | OK |
| R6 | Bypass surgery (T4; common_mistake; q2 distractor) | base (context) | — not in 4.2.2.4 | all four | OFF-SPEC (accurate) |
| R7 | Heart transplant; immunosuppressants (T4) | base | 4.2.2.4 | all four | OK; "heart and lungs" missing |
| R8 | `higher`: statins, stents, bypass, transplant recap | **base** | 4.2.2.4 | CH, TH only (CF/TF copy = null) | ROUTE |
| R9 | `higher`: artificial hearts — temporary support | **base** | 4.2.2.4 | CH, TH only | ROUTE |
| R10 | `higher`: faulty valves → biological/mechanical replacement | **base** | 4.2.2.4 | CH, TH only | ROUTE |
| R11 | `higher`: evaluate risks and benefits of each treatment | **base** | 4.2.2.4 | CH, TH only | ROUTE |
| R12 | q1–q3 | base | 4.2.2.4; 4.2.2.6 | all four | all usable |
| — | Consequences of faulty valves (don't open fully / leak) | base | 4.2.2.4 | **absent** | GAP |
| — | Artificial hearts' two uses (bridge to transplant; rest for recovery) | base | 4.2.2.4 | only in hidden `higher` | GAP/ROUTE |
| — | RP, equations, FIFA, examiner_tip | none | — | — | correct: no RP or calculation in 4.2.2.4 |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | T1 | CHD = coronary arteries narrowed/blocked; they supply heart muscle with oxygen and glucose | OK | — | 4.2.2.4 |
| C2 | T1 | Heart muscle continuously respiring; needs continuous O₂ | OK | — | — |
| C3 | T1 | CHD a leading cause of death in UK and worldwide | OK | — | — |
| C4 | T2 | Fatty material (mainly cholesterol) builds up in coronary artery walls → plaques/atheromas | OK | Spec says "inside the coronary arteries"; the deposit is in the wall lining — both credited. | 4.2.2.4 |
| C5 | T2 | Plaques harden, wall less elastic; lumen narrows; flow reduced | OK | — | 4.2.2.4 |
| C6 | T2 | Plaque rupture → clot → complete blockage → heart attack; muscle starved of O₂ dies | OK | Beyond spec detail; correct. | — |
| C7 | T3 | Smoking: CO damages artery walls; nicotine raises heart rate and BP | OK | — | 4.2.2.6 |
| C8 | T3 | High cholesterol, high BP, poor diet (saturated fat, salt), lack of exercise, obesity | OK | — | 4.2.2.6 |
| C9 | T3 | "AGE — risk increases with age as arteries gradually narrow" | IMPRECISE | Contradicts q1 wx3 in the same file ("Arteries don't naturally narrow with age"). Say: risk rises with age because fatty deposits have longer to build up. | — |
| C10 | T3 | "males … younger ages than females (though risk equalises after menopause)" | IMPRECISE | Women's risk **rises** after menopause; "equalises" overstates. Off-spec detail. | — |
| C11 | T3 | Lifestyle = can change; non-lifestyle = genetics, age, sex | OK | (Spec framing: lifestyle vs substances in body/environment; and correlation ≠ proven cause — worth one line.) | 4.2.2.6 |
| C12 | T4 | Statins reduce (LDL) cholesterol; slow plaque build-up; daily; side effects e.g. muscle pain | OK | Spec says "blood cholesterol"; "LDL" is beyond spec, correct. | 4.2.2.4 |
| C13 | T4 | Stent: metal mesh tube, holds artery open, inserted by angioplasty; does not treat cause | OK | — | 4.2.2.4 |
| C14 | T4 | Bypass surgery: graft (e.g. leg vein) around blockage | OFF-SPEC | Accurate, but not in AQA 4.2.2.4. Context only; not the core contrast. | — |
| C15 | T4 | Transplant: donor heart, last resort for heart failure; rejection, waiting, lifelong immunosuppressants | OK | Add spec's "or heart and lungs". | 4.2.2.4 |
| C16 | T4 | (absent) faulty valves and their consequences | GAP | Valve not opening fully → less blood pumped; leaking valve → blood flows backwards; both → less oxygenated blood reaches the body → tiredness, breathlessness. Replaced by biological (from pigs/cows or human donors) or mechanical valves. | 4.2.2.4 |
| C17 | T4 | (absent) artificial hearts | GAP | Spec: keep patients alive while waiting for a transplant, or let the heart rest as an aid to recovery. Present only in the hidden `higher` block. | 4.2.2.4 |
| C18 | `higher` | Recap of statins, stents, bypass, transplant; artificial hearts temporary; valve replacement; evaluate | OK, **mis-tagged** | All base 4.2.2.4. | 4.2.2.4 |
| C19 | common_mistake | Stent holds artery open, does not bypass; bypass creates new route | OK | Correct; but bypass is off-spec — the spec's own contrast is stent (mechanical) vs statin (drug). | — |
| C20 | key_note | as above | OK | — | — |
| C21 | q1 key | Fatty plaques narrow coronary arteries, reducing flow to heart muscle | OK | — | 4.2.2.4 |
| C22 | q1 wx1 | Heart failure is a consequence not the cause | OK | — | — |
| C23 | q1 wx2 | Blood viscosity not the mechanism | OK | — | — |
| C24 | q1 wx3 | Arteries narrow because of plaques, not naturally with age | OK | Correct; theory T3 must be re-cut to agree (C9). | — |
| C25 | q2 key | Stent inserted, expands, holds artery open | OK | — | 4.2.2.4 |
| C26 | q2 wx1–wx3 | Not dissolving; rerouting = bypass; cholesterol = statins | OK | — | — |
| C27 | q3 key | Smoking is a changeable lifestyle risk factor | OK | — | 4.2.2.6 |
| C28 | q3 wx1–wx3 | Genetics, sex, age not changeable | OK | — | — |
| C29 | matching (to be replaced) | four pairs | OK | — | — |
| C30 | — | `[NEW — to be examined]` Convert lines | n/a | None present (no calculation). | — |

Count: **0 WRONG**. **IMPRECISE**: C9, C10. **OFF-SPEC**: C14 (bypass). **ROUTE**: C18 (whole `higher` block is base). **GAP**: C16 (faulty valves), C17 (artificial hearts), C15 (heart-and-lungs).

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| `higher` block | Base content shown only on CH/TH | Teach as base on all four routes. |
| q1, q2, q3 | Correct, base | Usable on all four routes. |

## 5. For the lesson author
**Misconceptions seen in AQA marking**
- "CHD is a blockage in the heart" / "in the blood" — it is in the coronary **arteries** that supply the heart muscle.
- "A stent removes the fat" / "statins unblock arteries" — stents hold open; statins slow further deposits.
- "Arteries just narrow with age."
- "A transplant cures it with no downside" — rejection, donor shortage, lifelong immunosuppressants.
- "The heart is short of blood" (vague) — the heart **muscle** is short of oxygen.
- "Correlation proves cause" when reading risk-factor data.

**Command words**: Describe, Explain, Evaluate (6-mark), Suggest, Give one advantage/disadvantage.

**Typical questions** ⚑ examiner-drafted
- *Explain how coronary heart disease can cause a heart attack. [3]* — fatty material builds up in coronary arteries (1); narrows them / reduces blood flow (1); heart muscle lacks oxygen (and dies) (1).
- *Describe how a stent treats coronary heart disease. [2]* — inserted into the narrowed coronary artery (1); holds it open so blood flow is restored (1).
- *Give one disadvantage of using statins. [1]* — side effects (e.g. muscle pain/liver damage); must be taken long term; do not work immediately.
- *Suggest one consequence of a leaking heart valve. [2]* — blood flows backwards (1); so less oxygenated blood reaches the body / patient tired or breathless (1).
- *Evaluate the use of drugs, stents and heart transplants to treat heart disease. [6]* — Level-marked: advantages and disadvantages of at least two methods, with a justified conclusion (e.g. statins non-surgical but long-term/side effects; stents quick recovery but surgery risk/artery may re-narrow; transplant for heart failure but rejection, donor shortage, immunosuppressants).

**Required practical**: none.

**Equations**: none.

## 6. Verdict
SOURCE OK WITH FLAGS. All science correct; all three quiz items usable on every route. The `higher` block is entirely base and hidden from Foundation pupils; faulty valves (and their consequences) and artificial hearts are spec core with no theory coverage, now added from the spec. Bypass surgery is accurate but off-spec. Two small theory imprecisions on age and sex.

**For Mide:** nothing. Every point is a settled fact.
