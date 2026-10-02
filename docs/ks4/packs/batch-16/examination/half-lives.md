# Examination — Half-Lives and Radioactive Decay (half-lives) — AQA 8464 6.4.2.3 / 8463 4.4.2.3 (+ 8463 4.4.3.1–4.4.3.3 physics-only layer)
Verdict: SOURCE OK WITH FLAGS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-16/04-checked-science-source/physics-6.4.2.3-half-lives.md`.
Spec sources read as text: `AQA-8464-spec.txt` (v1.1) §6.4.2.1–6.4.2.4; `AQA-8463-spec.txt` (v1.1) §4.4.2.1–4.4.3.3. Equation sheets (8463 Jun26, 8464): no half-life relationship is printed on either. Route audit row `half-lives` (base / base, OK — "HT layer: net decline as a ratio. Physics-only layer: comparing isotopes by half-life (4.4.3.2)"). Neighbours: batch 5 `radioactive-decay` (activity, Bq, count-rate defined there); this batch's `background-radiation` and `uses-of-nuclear-radiation` (TF TH).

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n; T1–T3 = theory chunks. The CF and TF `higher` copies are `null` (no route difference in wording).

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 | **6.4.2.3** | Half-lives and the random nature of radioactive decay | base, with one **(HT only)** statement |
| 8463 | **4.4.2.3** | same | same |
| Layer | 8463 **4.4.3.2** Different half-lives of radioactive isotopes | | physics only |
| Layer | 8463 **4.4.3.1** Background radiation; **4.4.3.3** Uses of nuclear radiation | | physics only |

Spec statements (verbatim, 8463 = 8464): "Radioactive decay is random. The half-life of a radioactive isotope is the time it takes for the number of nuclei of the isotope in a sample to halve, or the time it takes for the count rate (or activity) from a sample containing the isotope to fall to half its initial level." "Students should be able to explain the concept of half-life and how it is related to the random nature of radioactive decay." "Students should be able to determine the half-life of a radioactive isotope from given information." (MS 4a) "**(HT only)** Students should be able to calculate the net decline, expressed as a ratio, in a radioactive emission after a given number of half-lives." (HT only MS 1c, 3d)
8463 4.4.3.2 (physics only): "Radioactive isotopes have a very wide range of half-life values. Students should be able to explain why the hazards associated with radioactive material differ according to the half-life involved." (MS 1b: data in standard form.)

## 2. Route table
| # | teachable point | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Decay is random; unpredictable for one nucleus, predictable for a large sample; coin analogy (T1; key_note) | base | 6.4.2.3 | all four | OK |
| R2 | Half-life definition: nuclei halve / count rate or activity halves (T2; key_note) | base | 6.4.2.3 | all four | OK |
| R3 | Half-life constant for an isotope; not affected by temperature, pressure, chemistry (T1, T2; q2) | base | 6.4.2.3 | all four | OK |
| R4 | Example half-lives (C-14, I-131, U-238, Rn-222) (T2) | base context; the "wide range" point is **triple** | 8463 4.4.3.2 | all four | OK (I-131 reason — F3) |
| R5 | Remaining after 1, 2, 3 half-lives by repeated halving; 800 → 100 Bq (T2; common_mistake; q1) | base | 6.4.2.3 ("determine … from given information") | all four | OK |
| R6 | Fraction remaining = (½)ⁿ; N = N₀ × (½)ⁿ (T2; equation; key_note; FIFA F/F steps) | **higher** | 6.4.2.3 (HT only) "net decline, expressed as a ratio" | all four | ROUTE (F1) |
| R7 | Read half-life off a decay curve (T3) | base | 6.4.2.3 (MS 4a) | all four | OK |
| R8 | Choosing isotopes by half-life: tracers, cancer treatment, waste (T3; `higher`; key_note) | **triple** | 8463 4.4.3.2; 4.4.3.3 | all four | ROUTE (F2) |
| R9 | Carbon dating (T3; key_note; matching) | not in spec (context) | — | all four | OK as context only |
| R10 | Background radiation; subtract it (T3; common_mistake; key_note) | **triple** | 8463 4.4.3.1 | all four | ROUTE (F2) |
| R11 | `higher` field: remaining after n half-lives / half-life unchangeable / compare isotopes | mixed: first clause HT (as a ratio); second base; third **triple** (not HT) | 6.4.2.3; 8463 4.4.3.2 | TH (CF/TF copies null) | ROUTE (F2) |
| R12 | FIFA: n = 12 ÷ 3 = 4, 960 × (½)⁴ = 60 Bq | base result by halving; the (½)ⁿ step is **higher** | 6.4.2.3 | all four | OK — chains two steps (F4) |
| R13 | q1 (640 Bq, T½ 4 h, 12 h → 80 Bq) | base | 6.4.2.3 | all four | OK — usable (wx3 imprecise, F5) |
| R14 | q2 (why half-life is constant) | base | 6.4.2.3 | all four | OK — usable |
| — | rp, examiner_tip | none | — | — | correct |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | T1 | cannot predict when / which nucleus decays | OK | — | 6.4.2.3 |
| C2 | T1 | decay not triggered by temperature, pressure or chemical state | OK | True; beyond spec wording, useful for q2. | — |
| C3 | T1 | large sample → predictable proportion; coin analogy | OK | — | 6.4.2.3 |
| C4 | T1 | activity falls as unstable nuclei fall | OK | — | 6.4.2.1 |
| C5 | T2 | definition (nuclei halve, or activity/count rate halves) | OK | Matches spec. | 6.4.2.3 |
| C6 | T2 | half-life constant for a given isotope | OK | — | — |
| C7 | T2 | C-14 ~5730 y; I-131 ~8 days; U-238 ~4.5 billion y; Rn-222 ~3.8 days | OK | All ✓ (I-131 8.0 d; U-238 4.47 × 10⁹ y; Rn-222 3.82 d). | — |
| C8 | T2 | I-131 "short enough to leave the body" | IMPRECISE | A short half-life means the activity falls quickly; leaving the body is biological excretion, a different thing. Say "short, so the activity soon falls to a low level". | 8463 4.4.3.2 |
| C9 | T2 | ½, ¼, ⅛, (½)ⁿ remaining | OK | Ratio form is the HT statement (R6). | 6.4.2.3 HT |
| C10 | T2 | 800 Bq, T½ 2 h, 6 h → 3 half-lives → 100 Bq | OK | ✓ | — |
| C11 | T3 | decay curve falls exponentially; half-life from graph, check next halving | OK | "Exponentially" is not spec wording; fine. | 6.4.2.3 MS 4a |
| C12 | T3 | Tc-99m 6 h, tracer needs short half-life | OK | Triple layer. | 8463 4.4.3.2–4.4.3.3 |
| C13 | T3 | carbon dating compares ¹⁴C/¹²C | OK | Off-spec context. | — |
| C14 | T3 | long-half-life waste is the biggest storage problem | OK | Triple layer (the 4.4.3.2 point exactly). | 8463 4.4.3.2 |
| C15 | T3 | background from rocks, cosmic rays, radon, food; subtract it | OK | Triple layer. | 8463 4.4.3.1 |
| C16 | `higher` | as R11 | ROUTE | None of it is an HT statement except the ratio. "Compare isotopes" is physics-only, and belongs on TF too. | 6.4.2.3; 8463 4.4.3.2 |
| C17 | common_mistake | halve from the current value; 1000 → 500 → 250 → 125 | OK | ✓. Background clause = triple. | — |
| C18 | key_note | as above | OK | Medical tracer / background clauses = triple. | — |
| C19 | equation | After n half-lives: fraction remaining = (½)ⁿ | OK | HT. Not on either sheet; not a recall-list equation → "Learn it". | 6.4.2.3 HT |
| C20 | FIFA F | n = total time ÷ half-life; remaining = initial × (½)ⁿ | OK | Two relationships stated in one step — this is a chain (rule 3). | — |
| C21 | FIFA I | n = 12 ÷ 3 = 4 | OK | ✓ | — |
| C22 | FIFA F/A | 960 × (½)⁴ = 960 ÷ 16 = 60 Bq | OK | ✓ (960 → 480 → 240 → 120 → 60). | — |
| C23 | CFIFA Convert | "…the hours cancel before any seconds conversion would be needed." | IMPRECISE | Not wrong, but implies seconds might otherwise be needed. n = t ÷ T½ only needs both times in the **same** unit; SI is never needed. Corrected line written into the source. | CFIFA amendment |
| C24 | matching (to be replaced) | 1600 → 400; 1000 → 125; longer/shorter half-life uses | OK | Use rows = triple. | — |
| C25 | q1 key | 12 ÷ 4 = 3; 640 → 320 → 160 → 80 Bq | OK | ✓ | 6.4.2.3 |
| C26 | q1 opt 2 / wx1 | 160 — only 2 half-lives | OK | Aligned. | — |
| C27 | q1 opt 3 / wx2 | 320 — only 1 half-life | OK | Aligned. | — |
| C28 | q1 opt 4 / wx3 | "Radioactive sources never fully reach zero — … never reaches exactly zero (exponential decay)." | IMPRECISE | A real sample has a finite number of nuclei and does eventually all decay; "never zero" is the smooth-curve idealisation. The real point: after 3 half-lives ⅛ remains. Usable; a cleaner wx3 is better. | 6.4.2.3 |
| C29 | q2 key | same time to halve regardless of temperature, pressure or how much has decayed | OK | — | 6.4.2.3 |
| C30 | q2 opt 2 / wx1 | number of atoms does change; proportion decaying per unit time fixed | OK | Aligned. | — |
| C31 | q2 opt 3 / wx2 | rate does not increase to compensate | OK | Aligned. | — |
| C32 | q2 opt 4 / wx3 | half-life independent of temperature | OK | Aligned. | — |

Count: **0 WRONG**. IMPRECISE: C8, C23, C28. ROUTE: R6, R8, R10, R11. Six calculations rechecked.

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| none | q1 and q2 correct and base | Both usable on all four routes (q1 Apply, q2 Explain). q1 wx3 is imprecise (F5), not wrong. |

## 5. Verdict
SOURCE OK WITH FLAGS. All arithmetic right. The route tagging needs care: the base page is random decay, the definition, finding a half-life from a graph or data, and halving step by step; the **HT** layer is the decline as a ratio, (½)ⁿ; the **triple** layer is "hazard differs with half-life" (4.4.3.2), uses, and background subtraction — the source's `higher` field holds triple content, not HT. The FIFA chains n = t ÷ T½ then N = N₀(½)ⁿ: it needs a Step 1 / Step 2 worked example, and on Foundation routes Step 2 is repeated halving rather than (½)ⁿ.

**For Mide:** one reading to confirm (HALF-LIVES-F6): "net decline, expressed as a ratio" — whether AQA wants the fraction **remaining** (1/8) or the fraction **decayed** (7/8). Best reading: teach both and word every question to name which.
