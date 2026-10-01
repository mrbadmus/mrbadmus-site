# Examination — Contraception and Fertility Treatment (contraception-fertility) — AQA 8464 4.5.3.4 (+4.5.3.5 HT) / 8461 4.5.3.5 (+4.5.3.6 HT)
Verdict: SOURCE HAS ERRORS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-8/04-checked-science-source/biology-4.5.4-contraception-fertility.md`.
Spec sources read as text: `AQA-8464-spec.txt` (Trilogy v1.1, 4.5.3.3–4.5.3.6), `AQA-8461-spec.txt` (Biology v1.0, 4.5.3.4–4.5.3.7). Route audit row `contraception-fertility` (OK, CF CH TF TH; HT layer infertility/IVF, whole section HT).

Conventions: q1–q3 = quiz items; "wx n" = `wrong_explanations` key n (explains `opts[n]`, 0-based; key always option 0). T1–T3 = theory blocks. Route copies: `higher` null on CF and TF (served CH/TH only). No FIFA, no `[NEW — to be examined]` line. **wx alignment checked: all three items correctly paired; no shift.**

**Spec ref:** the file and site label "4.5.4" — wrong in both specs. True refs **8464 4.5.3.4 + 4.5.3.5 (HT only) / 8461 4.5.3.5 + 4.5.3.6 (HT only)**.

**Infertility treatment is HT — confirmed.** 8464 4.5.3.5 and 8461 4.5.3.6 are both headed "The use of hormones to treat infertility (HT only)": the fertility drug, every IVF stage and the evaluation of fertility treatment are HT on both Combined and Biology. Contraception (8464 4.5.3.4 / 8461 4.5.3.5) carries no HT or separate-science label: base. Thyroxine/adrenaline negative feedback (8464 4.5.3.6 / 8461 4.5.3.7, HT) does **not** appear in this file and is not this lesson's content; it belongs to `endocrine-system`.

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 | **4.5.3.4** | Contraception | base |
| 8461 | **4.5.3.5** | Contraception | base |
| 8464 | **4.5.3.5** | The use of hormones to treat infertility | **(HT only)** — whole section |
| 8461 | **4.5.3.6** | The use of hormones to treat infertility | **(HT only)** — whole section |
| Supporting | 8464 4.5.3.3 / 8461 4.5.3.4 (FSH, LH, oestrogen, progesterone roles) | | base (+HT interactions) |

Spec statements (verbatim, 8464 = 8461). Contraception: "Students should be able to evaluate the different hormonal and non-hormonal methods of contraception. Fertility can be controlled by a variety of hormonal and non-hormonal methods of contraception. These include: oral contraceptives that contain hormones to inhibit FSH production so that no eggs mature; injection, implant or skin patch of slow release progesterone to inhibit the maturation and release of eggs for a number of months or years; barrier methods such as condoms and diaphragms which prevent the sperm reaching an egg; intrauterine devices which prevent the implantation of an embryo or release a hormone; spermicidal agents which kill or disable sperm; abstaining from intercourse when an egg may be in the oviduct; surgical methods of male and female sterilisation." (WS 1.3: show why issues around contraception cannot be answered by science alone; WS 1.4.)
Infertility (HT only): "Students should be able to explain the use of hormones in modern reproductive technologies to treat infertility. This includes giving FSH and LH in a 'fertility drug' to a woman. She may then become pregnant in the normal way. In Vitro Fertilisation (IVF) treatment. IVF involves giving a mother FSH and LH to stimulate the maturation of several eggs. The eggs are collected from the mother and fertilised by sperm from the father in the laboratory. The fertilised eggs develop into embryos. At the stage when they are tiny balls of cells, one or two embryos are inserted into the mother's uterus (womb). Although fertility treatment gives a woman the chance to have a baby of her own: it is very emotionally and physically stressful; the success rates are not high; it can lead to multiple births which are a risk to both the babies and the mother." (WS 1.1 microscopy enabled IVF; WS 1.3 social and ethical issues; WS 1.4 evaluate from the perspective of patients and doctors.)

## 2. Route table
| # | teachable point | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Hormonal methods: combined pill, mini-pill, implant, injection, hormonal IUD (T1; key_note) | base | 4.5.3.4/4.5.3.5 | all four | OK; patch missing (F3) |
| R2 | Barrier methods; condoms also protect from STIs (T1; common_mistake; key_note; q1) | base | 4.5.3.4/4.5.3.5 | all four | OK; one IMPRECISE (F4) |
| R3 | Copper IUD (T1; key_note) | base | 4.5.3.4/4.5.3.5 | all four | GAP — implantation mechanism missing (F3) |
| R4 | Spermicides; abstinence | base | 4.5.3.4/4.5.3.5 | **missing** | GAP (F3) |
| R5 | Vasectomy, tubal ligation (T1) | base | 4.5.3.4/4.5.3.5 | all four | OK |
| R6 | Contraception ethics; religion; STIs (T3 first half) | base (WS 1.3) | 4.5.3.4/4.5.3.5 | all four | OK |
| R7 | FSH/LH fertility drug; multiple pregnancy (T2) | **higher** | 4.5.3.5/4.5.3.6 (HT only) | all four | ROUTE (F1) |
| R8 | IVF stages; success rates (T2; common_mistake; key_note; `higher`) | **higher** | 4.5.3.5/4.5.3.6 (HT only) | T2 all four; `higher` CH/TH | ROUTE (F1) |
| R9 | IVF ethics: spare embryos, PGD, cost, burden, donors (T3 second half) | **higher** (PGD off-spec) | 4.5.3.5/4.5.3.6 (HT only) | all four | ROUTE (F1) |
| R10 | q1, q3 | base | 4.5.3.4/4.5.3.5 | all four | q1 OK; **q3 WRONG** (F2) |
| R11 | q2 | **higher** | 4.5.3.5/4.5.3.6 (HT only) | all four | ROUTE (F1); wx2 IMPRECISE (F4) |
| — | RP, equations, FIFA | none | — | — | correct |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | T1 | contraception interferes with fertilisation, ovulation or implantation | OK | — | 4.5.3.4 |
| C2 | T1 | combined pill: oestrogen + progesterone; oestrogen inhibits FSH → no maturation → no ovulation | OK | Spec: "hormones to inhibit FSH production so that no eggs mature". | 4.5.3.4 |
| C3 | T1 | mini-pill thickens cervical mucus, may prevent ovulation | OK (off-spec detail) | — | — |
| C4 | T1 | implant: progesterone, up to 3 years | OK | — | 4.5.3.4 |
| C5 | T1 | injection every 8–12 weeks | OK | — | 4.5.3.4 |
| C6 | T1 | hormonal IUD releases progesterone in the uterus | OK | Spec: IUDs "release a hormone". | 4.5.3.4 |
| C7 | T1 | (skin patch) | GAP | Spec lists "skin patch". | 4.5.3.4 |
| C8 | T1 | male condom "ALSO protects against STIs — the only contraceptive that does this"; next line female condom "Also protects against STIs" | IMPRECISE | Self-contradictory: condoms (male and female) are the only methods that protect against STIs. | — |
| C9 | T1 | diaphragm over the cervix | OK | Spec: prevents sperm reaching an egg. | 4.5.3.4 |
| C10 | T1 | copper IUD: copper ions toxic to sperm; no hormones | IMPRECISE (incomplete) | True, but the spec's mechanism for IUDs is "prevent the implantation of an embryo". Teach both. | 4.5.3.4 |
| C11 | T1 | (spermicides; abstinence when an egg may be in the oviduct) | GAP | Both on the spec list. | 4.5.3.4 |
| C12 | T1 | vasectomy: vas deferens cut/tied; tubal ligation: oviducts cut/tied | OK | "Male and female sterilisation". | 4.5.3.4 |
| C13 | T2 | FSH (and LH) fertility drug → egg maturation and ovulation; risk of multiple pregnancy | OK, **HT** | — | 4.5.3.5 (HT only) |
| C14 | T2 | "in vitro" = "in glass"; fertilisation in a lab dish | OK, **HT** | — | 4.5.3.5 |
| C15 | T2 | IVF steps 1–7: FSH (and LH) → several eggs; collected; mixed with sperm; embryos 2–5 days; one or two into uterus; progesterone; implantation | OK, **HT** | Matches spec ("tiny balls of cells, one or two embryos"); progesterone support off-spec but true. | 4.5.3.5 |
| C16 | T2 | success ≈ 30–40% per cycle under 35, declining with age | OK (off-spec) | Order right; spec: "success rates are not high". Context only, never a question. | 4.5.3.5 |
| C17 | T3 | some religious groups oppose artificial contraception; emergency contraception controversial; condoms supported for STIs | OK | Stated as views. | WS 1.3 |
| C18 | T3 | spare embryos frozen/destroyed/donated; PGD; cost; physical and emotional burden; donor anonymity | OK, **HT** (PGD off-spec) | Spec adds: multiple births "a risk to both the babies and the mother" — not stated for IVF. | 4.5.3.5 |
| C19 | `higher` | combined pill: oestrogen inhibits FSH, progesterone thickens cervical mucus; IVF sequence; ethics | OK | Note: this field itself says the combined pill thickens cervical mucus — which is why q3 option 1 is true (F2). | 4.5.3.4; 4.5.3.5 |
| C20 | common_mistake | pill does not protect against STIs; combined pill prevents ovulation by inhibiting FSH; in IVF, FSH for multiple eggs, progesterone for implantation | OK | IVF sentence HT. | 4.5.3.4; 4.5.3.5 |
| C21 | key_note | "IVF: FSH → multiple eggs → fertilised in lab → embryo implanted" | IMPRECISE (minor) | Embryos are *inserted* into the uterus; implantation is what the embryo then does (or not). | 4.5.3.5 |
| C22 | matching (to be replaced) | five pairs | OK | — | — |
| C23 | q1 key | condoms prevent pregnancy and STIs | OK | — | 4.5.3.4 |
| C24 | q1 wx1 | pill: no STI protection | OK | — | — |
| C25 | q1 wx2 | copper IUD: no STI protection | OK | — | — |
| C26 | q1 wx3 | implant: no barrier | OK | — | — |
| C27 | q2 key | FSH to make the ovaries produce several eggs for collection | OK, **HT** | Spec: "FSH and LH to stimulate the maturation of several eggs". | 4.5.3.5 (HT only) |
| C28 | q2 wx1 | uterus lining = progesterone, later | OK | — | — |
| C29 | q2 wx2 | "Immune suppression is managed separately" | IMPRECISE | Implies routine IVF includes immune suppression; it does not. The point: FSH is a reproductive hormone that makes eggs mature; it has nothing to do with the immune system. | — |
| C30 | q2 wx3 | fertilisation is by sperm; FSH is a hormone | OK | — | 4.5.3.5 |
| C31 | q3 key | oestrogen inhibits FSH → no egg maturation, no ovulation | OK | Spec wording. | 4.5.3.4 |
| C32 | q3 opt 1 / wx1 | option "It thickens the cervical mucus so sperm cannot swim through" marked false; wx1 "Thickening cervical mucus = PROGESTERONE-ONLY PILL … The COMBINED pill works primarily by suppressing ovulation" | **WRONG** | The combined pill's progestogen also thickens cervical mucus — the source's own `higher` field says so ("progesterone to thicken cervical mucus"), and wx1 concedes it with "primarily". Option 1 is a true answer to "How does the combined contraceptive pill prevent pregnancy?" — two defensible keys. | — |
| C33 | q3 wx2 | barrier methods prevent sperm entering | OK | — | 4.5.3.4 |
| C34 | q3 wx3 | "The combined pill actually STABILISES the uterus lining" | IMPRECISE | The combined pill keeps the lining thin; the withdrawal bleed occurs in the pill-free days. Option 3 is still false. | — |

Count: **1 WRONG** (C32 — frozen q3). IMPRECISE: C8, C10, C21, C29, C34. ROUTE: fertility drugs, IVF and IVF ethics on every route (F1). GAP: skin patch, IUD implantation, spermicides, abstinence, multiple-birth risk (F3).

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| q3 | Two defensible keys (option 1 is true of the combined pill) | **Do not use as written** on any route (F2). |
| q2 | IVF — 8464 4.5.3.5 / 8461 4.5.3.6 (HT only) | **Usable on CH and TH only** (wx2 imprecise, F4). |
| q1 | correct, base | Usable on all four routes. |

## 5. Verdict
SOURCE HAS ERRORS. One wrong frozen quiz item (q3: the combined pill does thicken cervical mucus, so the "wrong" option is true). Fertility drugs, IVF and the IVF evaluation are HT on both specs and currently sit in theory on every route. The spec's contraception list is incomplete in the source (skin patch, spermicides, abstinence, and the IUD's implantation mechanism). Ref "4.5.4" is wrong. **For Mide:** nothing — the combined pill's mechanisms (inhibits ovulation, thickens cervical mucus) are settled pharmacology, not a marking question.
