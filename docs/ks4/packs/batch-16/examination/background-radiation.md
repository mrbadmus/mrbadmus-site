# Examination — Background Radiation (background-radiation) — AQA 8463 4.4.3.1 (physics only)
Verdict: SOURCE HAS ERRORS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-16/04-checked-science-source/physics-6.4.3-background-radiation.md`.
Spec sources read as text: `AQA-8463-spec.txt` (v1.1) §4.4.2.1–4.4.3.3; `AQA-8464-spec.txt` (v1.1) §6.4.2 (to confirm Combined has no background-radiation section — it has none). Equation sheets: none apply. Route audit row `background-radiation` (TF TH / TF TH, OK — "4.4.3 … (physics only)"). Data check: UK average dose and source shares against the UKHSA/PHE review of UK population exposure (≈ 2.7 mSv a year; radon ≈ 48 %, medical ≈ 15 %, ground and buildings ≈ 13 %, cosmic ≈ 12 %, food and drink ≈ 10 %, all other man-made < 1 %).

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n; T1–T3 = theory chunks. The source's `spec` field reads "6.4.3 (physics only)" — the true reference is **8463 4.4.3.1**; there is no 8464 equivalent.

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8463 | **4.4.3.1** | Background radiation | physics only (heading 4.4.3 "(physics only)") |
| 8464 | — | none | — |
| Supporting | 8463 4.4.2.1 (count-rate vs activity); 4.4.2.3 (half-life) | | base |

Spec statements (verbatim, 8463 4.4.3.1): "Background radiation is around us all of the time. It comes from: • natural sources such as rocks and cosmic rays from space • man-made sources such as the fallout from nuclear weapons testing and nuclear accidents. The level of background radiation and radiation dose may be affected by occupation and/or location. Radiation dose is measured in sieverts (Sv). 1000 millisieverts (mSv) = 1 sievert (Sv). Students will not need to recall the unit of radiation dose." (WS 4.4)
8463 4.4.2.1: "Activity is the rate at which a source of unstable nuclei decays. … Count-rate is the number of decays recorded each second by a detector (eg Geiger-Muller tube)."

## 2. Route table
| # | teachable point | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Background is always present; natural and man-made sources; UK shares (T1; key_note; matching) | triple | 8463 4.4.3.1 | TF TH | OK; nuclear accidents missing (F3) |
| R2 | Correcting for background: measure without source, subtract (T2; equation; common_mistake; q1, q2) | triple | 8463 4.4.3.1 + 4.4.2.1 (WS) | TF TH | OK; q1 stem WRONG (F1) |
| R3 | Background varies with place and time; measure over a long time and average (T2) | triple | 8463 4.4.3.1 | TF TH | OK |
| R4 | Dose in Sv / mSv; 1000 mSv = 1 Sv; UK ≈ 2.7 mSv/yr (T3; key_note) | triple | 8463 4.4.3.1 | TF TH | OK; 1000 mSv = 1 Sv missing (F3) |
| R5 | Dose affected by location and occupation (T3) | triple | 8463 4.4.3.1 | TF TH | OK |
| R6 | Radon in lungs → α → lung cancer; ventilation (T3) | triple | 8463 4.4.3.1; 4.4.2.4 | TF TH | OK |
| R7 | `higher` field: corrected count rate; occupations; radon | **triple (not HT)** — 4.4.3.1 has no HT statement | 8463 4.4.3.1 | TH only (TF copy null) | ROUTE (F2) |
| R8 | q1 (320 − 20) | triple | 8463 4.4.3.1 | TF TH | **WRONG stem** (F1) — not usable as written |
| R9 | q2 (why measure background first) | triple | 8463 4.4.3.1 | TF TH | OK — usable (F4 minor) |
| — | rp, fifas, examiner_tip | none | — | — | correct |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | T1 | background = low-level ionising radiation everywhere, natural and artificial | OK | Spec says "man-made". | 4.4.3.1 |
| C2 | T1 | natural ~85 %; radon ~50 %; ground/buildings ~15 %; cosmic ~10 %; food ~10 % | OK | Within rounding of UKHSA figures (48/13/12/10 %). | — |
| C3 | T1 | radon from uranium in rocks; granite areas, Cornwall | OK | — | — |
| C4 | T1 | cosmic rays more at altitude; pilots | OK | — | 4.4.3.1 |
| C5 | T1 | food: ¹⁴C, ⁴⁰K | OK | — | — |
| C6 | T1 | artificial ~15 %: medical, nuclear industry, weapons-testing fallout | OK / GAP | Medical is almost all of the ~15 %. The spec's other named man-made source, **nuclear accidents** (Chernobyl, Fukushima), is missing. | 4.4.3.1 |
| C7 | T2 | uncorrected readings overstate the source | OK | — | — |
| C8 | T2 | method: background without source, reading with source, subtract | OK | — | — |
| C9 | T2 | 175 − 25 = 150 counts per minute | OK | ✓ | — |
| C10 | T2 | background varies with place and slightly with time; measure over a long time and average | OK | Averaging because decay is random. | 4.4.3.1; 4.4.2.3 |
| C11 | T3 | dose in Sv or mSv; accounts for amount and biological effect | OK | 1000 mSv = 1 Sv (spec) is missing. Spec: unit need not be recalled — do not test recall of "sievert". | 4.4.3.1 |
| C12 | T3 | UK average ≈ 2.7 mSv a year; majority radon + medical | OK | ✓ (≈ 63 %). | — |
| C13 | T3 | location, occupation, medical procedures, altitude | OK | — | 4.4.3.1 |
| C14 | T3 | radon decays in lungs → α → lung cancer; ventilation; test kits | OK | — | — |
| C15 | T3 | benefit vs risk; regulated limits | OK | — | — |
| C16 | `higher` | corrected count rate; occupations; radon | ROUTE | Not HT — 4.4.3.1 has no HT label, so all of it belongs on TF as well as TH. | 4.4.3.1 |
| C17 | common_mistake | uncorrected count rate gives a half-life that looks longer | OK | Right: a constant background added to a falling count flattens the curve, so halving takes longer. | 4.4.2.3 |
| C18 | key_note | as above | OK | — | — |
| C19 | equation | corrected count rate = measured − background | OK | Not a spec equation, not on the 8463 sheet: "Learn it" as a method. | — |
| C20 | matching (to be replaced) | radon ~50 %; cosmic ~10 %; medical ~15 %; correction | OK | — | — |
| C21 | q1 stem | "…What is the corrected **activity** of the source?" (answer in counts/min) | **WRONG** | A detector reading is **count-rate**, not activity; the spec defines them separately, and a detector catches only a fraction of the decays. Must read "corrected count rate". | 4.4.2.1 |
| C22 | q1 key | 320 − 20 = 300 counts/min | OK | ✓ as a count rate. | — |
| C23 | q1 opt 2 / wx1 | 340 — added; "would overestimate the source activity" | OK / IMPRECISE | Aligned; "activity" → "count rate". | — |
| C24 | q1 opt 3 / wx2 | 320 — always correct for background | OK | Aligned. | — |
| C25 | q1 opt 4 / wx3 | 16 — dividing is meaningless | OK | Aligned; 320 ÷ 20 = 16 ✓. | — |
| C26 | q2 key | baseline subtracted → "true activity of the source alone" | IMPRECISE | "the count rate due to the source alone". Usable. | 4.4.2.1 |
| C27 | q2 opt 2 / wx1 | checking the counter is good practice, not the reason | OK | Aligned. | — |
| C28 | q2 opt 3 / wx2 | "Geiger counters don't need resetting to zero — they count ionisation events regardless." | IMPRECISE | A counter **is** reset to zero before each count. The real point: measuring background is not calibration. Usable. | — |
| C29 | q2 opt 4 / wx3 | background has no measurable half-life — many continuously replenished sources | OK | Aligned; fair at GCSE. | — |

Count: **1 WRONG** (C21, q1 stem). IMPRECISE: C23, C26, C28. GAP: C6, C11 (1000 mSv = 1 Sv). ROUTE: C16.

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| q1 | stem calls a detector count rate the source's "activity" | Do not use as written (BACKGROUND-RADIATION-F1). Usable once "corrected activity" → "corrected count rate" (and wx1 "activity" → "count rate"). |
| q2 | key says "activity" for count rate; wx2 says counters are not reset | Usable; prefer the wording fix (F4). |

## 5. Verdict
SOURCE HAS ERRORS — one, and a one-word fix: q1 calls a count rate an activity, the same error batch 5 found in `radioactive-decay` q2. Otherwise the science and the UK figures are right. The spec's "nuclear accidents" and "1000 mSv = 1 Sv" are missing. The `higher` field is not HT and must reach TF.

**For Mide:** nothing — all settled from the spec.
