# Examination — Human Reproduction and Hormones (human-reproduction-hormones) — AQA 8464 4.5.3.3 / 8461 4.5.3.4
Verdict: SOURCE OK WITH FLAGS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-8/04-checked-science-source/biology-4.5.4-human-reproduction-hormones.md`.
Spec sources read as text: `AQA-8464-spec.txt` (Trilogy v1.1, 4.5.3.1; 4.5.3.3), `AQA-8461-spec.txt` (Biology v1.0, 4.5.3.1; 4.5.3.4). Route audit row `human-reproduction-hormones` (OK, CF CH TF TH; HT layer interactions).

Conventions: q1–q3 = quiz items; "wx n" = `wrong_explanations` key n (explains `opts[n]`, 0-based; key always option 0). T1–T3 = theory blocks. Route copies: `higher` null on CF and TF (served CH/TH only). No FIFA, no `[NEW — to be examined]` line. **wx alignment checked: all three items correctly paired; no shift.**

**Spec ref:** the file and site label "4.5.4" — wrong in both specs (8461 4.5.4 is *Plant hormones*; 8464 4.5.4 does not exist). True refs **8464 4.5.3.3 / 8461 4.5.3.4** (identical text).

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 | **4.5.3.3** | Hormones in human reproduction | base, with two **(HT only)** statements |
| 8461 | **4.5.3.4** | Hormones in human reproduction | same |
| Supporting | 4.5.3.1 (pituitary as master gland; ovary, testes positions) | | base |

Spec statements (verbatim, 8464 = 8461): "Students should be able to describe the roles of hormones in human reproduction, including the menstrual cycle. During puberty reproductive hormones cause secondary sex characteristics to develop. Oestrogen is the main female reproductive hormone produced in the ovary. At puberty eggs begin to mature and one is released approximately every 28 days. This is called ovulation. Testosterone is the main male reproductive hormone produced by the testes and it stimulates sperm production. Several hormones are involved in the menstrual cycle of a woman. • Follicle stimulating hormone (FSH) causes maturation of an egg in the ovary. • Luteinising hormone (LH) stimulates the release of the egg. • Oestrogen and progesterone are involved in maintaining the uterus lining. (HT only) Students should be able to explain the interactions of FSH, oestrogen, LH and progesterone, in the control of the menstrual cycle. (HT only) Students should be able to extract and interpret data from graphs showing hormone levels during the menstrual cycle." (MS 2c)

## 2. Route table
| # | teachable point | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Puberty, secondary sex characteristics, oestrogen and testosterone (T1) | base | 4.5.3.3/4.5.3.4 | all four | OK; one IMPRECISE (F3) |
| R2 | "pituitary releases FSH and LH → ovaries produce oestrogen" at puberty (T1) | base (link to master gland) | 4.5.3.1 | all four | OK |
| R3 | 28-day cycle; menstruation, rebuilding, ovulation day ~14, maintenance (T2) | base | 4.5.3.3/4.5.3.4 | all four | OK; day ranges IMPRECISE (F3) |
| R4 | FSH matures egg; LH releases egg; oestrogen repairs lining; progesterone maintains it (T3; common_mistake; key_note) | base | 4.5.3.3/4.5.3.4 | all four | OK |
| R5 | FSH → oestrogen; oestrogen inhibits FSH, triggers LH surge; progesterone inhibits FSH and LH (T3; `higher`) | **higher** | 4.5.3.3/4.5.3.4 (HT only) | T3 all four; `higher` CH/TH | ROUTE (F1) |
| R6 | Hormone-level graphs | **higher** | (HT only), MS 2c | **missing** | GAP (F2) |
| R7 | q1, q2 | base | 4.5.3.3/4.5.3.4 | all four | OK; q2 wx3 IMPRECISE (F4) |
| R8 | q3 | **higher** | (HT only) | all four | ROUTE (F5) |
| — | RP, equations, FIFA | none | — | — | correct |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | T1 | puberty = development preparing the body for reproduction | OK | — | 4.5.3.3 |
| C2 | T1 | females: pituitary FSH and LH → ovaries make oestrogen | OK (off-spec detail) | — | — |
| C3 | T1 | oestrogen causes breast development, pelvis widening, "Pubic and underarm hair growth", menstrual cycle onset, growth spurt | IMPRECISE | Pubic and underarm hair in girls is driven mainly by androgens (adrenal), not oestrogen. Spec only says "reproductive hormones cause secondary sex characteristics". Re-cut: list hair under "reproductive hormones", or drop. | 4.5.3.3 |
| C4 | T1 | males: pituitary LH → testes make testosterone; penis/testes enlarge, voice breaks, hair, muscle, sperm production, growth spurt | OK | Spec: testosterone "stimulates sperm production". | 4.5.3.3 |
| C5 | T2 | cycle ≈ 28 days, varies | OK | — | 4.5.3.3 |
| C6 | T2 | day 1 menstruation, lining shed | OK | — | — |
| C7 | T2 | "Days 1–13: The uterus lining rebuilds and thickens — stimulated by oestrogen." | IMPRECISE | The lining is being shed for about days 1–4/5; it rebuilds from about day 5 to ovulation. "Days 1–13" puts shedding and rebuilding at once. Say "about days 5–14". | — |
| C8 | T2 | day ~14 ovulation from one ovary | OK | — | 4.5.3.3 |
| C9 | T2 | days 14–28 lining maintained by progesterone; if fertilised, implantation, progesterone stays high; if not, progesterone falls, lining breaks down | OK | — | 4.5.3.3 |
| C10 | T3 | FSH from pituitary: egg in follicle matures; stimulates oestrogen production | OK | Second clause HT. | 4.5.3.3 (HT) |
| C11 | T3 | oestrogen from ovaries: repairs and thickens lining | OK | — | 4.5.3.3 |
| C12 | T3 | "At low levels: inhibits FSH production"; "At HIGH levels (mid-cycle): triggers a surge in LH" | OK, **HT**; minor IMPRECISE | AQA's credited line is "oestrogen inhibits FSH and stimulates LH". The "at low levels" qualifier is non-standard and invites "so high oestrogen doesn't inhibit FSH"; drop it. | 4.5.3.3 (HT only) |
| C13 | T3 | LH surge ≈ day 14 triggers ovulation | OK | — | 4.5.3.3 |
| C14 | T3 | progesterone from corpus luteum; maintains lining; inhibits FSH and LH | OK, inhibition **HT** | Corpus luteum off-spec, true. | 4.5.3.3 (HT only) |
| C15 | T3 | no pregnancy → corpus luteum breaks down → progesterone falls → menstruation | OK | — | — |
| C16 | `higher` | full interaction sequence; "positive feedback at high concentration" | OK | Positive feedback off-spec term, true. | 4.5.3.3 (HT only) |
| C17 | common_mistake | FSH matures egg, not ovulation; LH ovulation; oestrogen rebuilds; progesterone maintains; pituitary makes FSH, LH; ovaries make oestrogen, progesterone | OK | — | 4.5.3.3 |
| C18 | key_note | as above | OK | — | 4.5.3.3 |
| C19 | matching (to be replaced) | five pairs | OK | Oestrogen "triggers LH surge" clause HT. | — |
| C20 | q1 key | LH surge ≈ day 14 releases egg | OK | Spec: "LH stimulates the release of the egg". | 4.5.3.3 |
| C21 | q1 wx1 | FSH = maturation, not release | OK | — | 4.5.3.3 |
| C22 | q1 wx2 | high oestrogen → LH release → ovulation | OK | HT fact in an explanation; fine on all routes. | (HT only) |
| C23 | q1 wx3 | progesterone made after ovulation, maintains lining | OK | — | — |
| C24 | q2 key | progesterone falls → lining breaks down → menstruation | OK | Base: progesterone maintains the lining. | 4.5.3.3 |
| C25 | q2 wx1 | rising would signal pregnancy; corpus luteum degenerates | OK | — | — |
| C26 | q2 wx2 | corpus luteum degenerates after about 14 days without implantation | OK | ≈10–14 days after ovulation. | — |
| C27 | q2 wx3 | "FSH is released at the start of a new cycle as progesterone falls — but it is oestrogen and progesterone levels, not progesterone directly stimulating FSH." | IMPRECISE | Muddled. The point to make: progesterone **inhibits** FSH; FSH rises again only because progesterone falls and the inhibition is removed. Key unaffected. | 4.5.3.3 (HT only) |
| C28 | q3 key | oestrogen repairs and thickens lining; triggers LH surge at high levels | OK, **HT** | LH clause is an HT interaction. | 4.5.3.3 (HT only) |
| C29 | q3 wx1 | high oestrogen → LH → ovulation; "at LOW concentrations, oestrogen inhibits FSH" | OK (minor IMPRECISE qualifier, as C12) | — | (HT only) |
| C30 | q3 wx2 | maintaining the lining in the second half = progesterone | OK on HT; see F5 | Base spec reads "Oestrogen and progesterone are involved in maintaining the uterus lining", so on F routes option 2 is defensible from the spec's own words. | 4.5.3.3 |
| C31 | q3 wx3 | egg maturation = FSH; oestrogen is a result of FSH | OK | — | 4.5.3.3 (HT) |

Count: **0 WRONG**. IMPRECISE: C3, C7, C12/C29, C27. ROUTE: interactions in theory 3 on every route (F1); q3 HT only (F5). GAP: hormone-level graphs (F2).

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| q3 | Key's "triggers the LH surge" is an (HT only) interaction; option 2 ("maintains the uterus lining in the second half") is defensible on F routes from the base wording "oestrogen and progesterone are involved in maintaining the uterus lining" | **Usable on CH and TH only.** |
| q1, q2 | correct, base | Usable on all four routes (q2 wx3 imprecise, F4). |

## 5. Verdict
SOURCE OK WITH FLAGS. No wrong science. Base roles (FSH matures, LH releases, oestrogen and progesterone maintain the lining) are right. Hormone interactions (HT) sit in theory 3 on every route; the HT hormone-graph statement has no material. Two re-cuttable day/hair imprecisions and one muddled explanation. Ref "4.5.4" is wrong — 4.5.3.3 (8464) / 4.5.3.4 (8461). **For Mide:** nothing.
