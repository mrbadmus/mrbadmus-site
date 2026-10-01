# Examination — The Endocrine System (endocrine-system) — AQA 8464 4.5.3.1 (+4.5.3.6 HT) / 8461 4.5.3.1 (+4.5.3.7 HT)
Verdict: SOURCE OK WITH FLAGS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-8/04-checked-science-source/biology-4.5.3-endocrine-system.md`.
Spec sources read as text: `AQA-8464-spec.txt` (Trilogy v1.1, 4.5.1; 4.5.3.1–4.5.3.6), `AQA-8461-spec.txt` (Biology v1.0, 4.5.3.1–4.5.3.7). Route audit row `endocrine-system` (OK, CF CH TF TH; HT layer thyroxine/adrenaline).

Conventions: q1–q3 = quiz items; "wx n" = `wrong_explanations` key n (explains `opts[n]`, 0-based; key always option 0). T1–T3 = theory blocks. Route copies: `higher` null on CF and TF (served CH/TH only). No FIFA, no `[NEW — to be examined]` line. **wx alignment checked: all three items correctly paired, keys 1–3 each explain their own option; no shift.**

**Spec ref:** the file and site label "4.5.3" (the whole of hormonal coordination); true refs **8464 4.5.3.1 / 8461 4.5.3.1**, with the HT layer from **8464 4.5.3.6 / 8461 4.5.3.7**.

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 | **4.5.3.1** | Human endocrine system | base |
| 8461 | **4.5.3.1** | Human endocrine system | base |
| Layer | 8464 **4.5.3.6** / 8461 **4.5.3.7** | Feedback systems / Negative feedback | **(HT only)** — whole section |
| Layer | 8464/8461 4.5.3.2 (glucagon) | Control of blood glucose concentration | **(HT only)** statement |
| Layer | 8461 4.5.3.3 (ADH) | Maintaining water and nitrogen balance | **(biology only)** + **(HT only)** |
| Supporting | 4.5.1 (effectors are muscles or glands); 4.5.2.1 (nervous system); 8464 4.5.3.3 / 8461 4.5.3.4 (sex hormones) | | base |

Spec statements (verbatim, 8464 = 8461, 4.5.3.1): "Students should be able to describe the principles of hormonal coordination and control by the human endocrine system. The endocrine system is composed of glands which secrete chemicals called hormones directly into the bloodstream. The blood carries the hormone to a target organ where it produces an effect. Compared to the nervous system the effects are slower but act for longer. The pituitary gland in the brain is a 'master gland' which secretes several hormones into the blood in response to body conditions. These hormones in turn act on other glands to stimulate other hormones to be released to bring about effects. Students should be able to identify the position of the following on a diagram of the human body: pituitary gland, pancreas, thyroid, adrenal gland, ovary, testes."
4.5.3.6 / 4.5.3.7 (HT only): "Students should be able to explain the roles of thyroxine and adrenaline in the body. Adrenaline is produced by the adrenal glands in times of fear or stress. It increases the heart rate and boosts the delivery of oxygen and glucose to the brain and muscles, preparing the body for 'flight or fight'. Thyroxine from the thyroid gland stimulates the basal metabolic rate. It plays an important role in growth and development. Thyroxine levels are controlled by negative feedback." (WS 1.2, MS 2c: interpret and explain simple diagrams of negative feedback control.)

## 2. Route table
| # | teachable point | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Hormones secreted directly into blood, carried to target organ (T1; common_mistake; key_note) | base | 4.5.3.1 | all four | OK |
| R2 | Slower but longer-lasting than nervous (T1, T3; key_note) | base | 4.5.3.1 | all four | OK |
| R3 | Pituitary master gland acting on other glands (T2) | base | 4.5.3.1 | all four | OK |
| R4 | Six glands and where they are (T2) | base | 4.5.3.1 | all four | OK — the spec skill is locating them **on a diagram**; needs the figure |
| R5 | Insulin; oestrogen, progesterone, testosterone; FSH, LH (T2) | base | 4.5.3.2; 4.5.3.3/4.5.3.4 | all four | OK |
| R6 | Glucagon (T2; key_note) | **higher** | 4.5.3.2 (HT only) | all four | ROUTE (F1) |
| R7 | Thyroxine → metabolic rate, growth (T2; key_note) | **higher** | 4.5.3.6/4.5.3.7 | all four | ROUTE (F1) |
| R8 | Adrenaline → fight or flight (T2; T3 last paragraph; `higher`) | **higher** | 4.5.3.6/4.5.3.7 | T2/T3 all four; `higher` CH/TH | ROUTE (F1) |
| R9 | Thyroxine negative feedback | **higher** | 4.5.3.6/4.5.3.7 | **missing** | GAP (F2) |
| R10 | ADH (T2; `higher`) | **triple-higher** | 8461 4.5.3.3 | T2 all four; `higher` CH/TH | ROUTE (F3) |
| R11 | TSH, ACTH, tropic hormones, glycogenolysis (`higher`) | off-spec | — | CH/TH | OFF-SPEC (F3) |
| R12 | q1, q3 | base | 4.5.3.1 | all four | OK |
| R13 | q2 (adrenaline = fight or flight) | **higher** | 4.5.3.6/4.5.3.7 | all four | ROUTE (F1) |
| — | RP, equations, FIFA | none | — | — | correct: none in 4.5.3.1 |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | T1 | endocrine system = chemical communication using hormones | OK | — | 4.5.3.1 |
| C2 | T1 | secreted directly into the bloodstream; no ducts; exocrine glands (salivary) have ducts | OK | Duct contrast is off-spec context. | 4.5.3.1 |
| C3 | T1 | blood carries hormones to every organ; only target organs respond (receptor proteins) | OK | Receptors off-spec but correct. | 4.5.3.1 |
| C4 | T1 | slower to start, longer lasting, more widespread | OK | — | 4.5.3.1 |
| C5 | T2 | pituitary in the brain, below the hypothalamus; master gland controlling other glands | OK | — | 4.5.3.1 |
| C6 | T2 | pituitary produces FSH, LH, growth hormone, ADH | OK, ADH **triple-higher** | ADH is released by the pituitary (8461 wording). | 8461 4.5.3.3 |
| C7 | T2 | thyroid in the neck; thyroxine controls metabolic rate; growth and development | OK, **HT** | Spec verb: "stimulates the basal metabolic rate". | 4.5.3.6/4.5.3.7 |
| C8 | T2 | adrenal glands above the kidneys; adrenaline in stress, fear, excitement; ↑ heart rate, ↑ breathing, pupils dilate, blood to muscles | OK, **HT** | Spec: "fear or stress … increases the heart rate and boosts the delivery of oxygen and glucose to the brain and muscles". Breathing/pupils off-spec but true. | 4.5.3.6/4.5.3.7 |
| C9 | T2 | pancreas makes insulin and glucagon | OK | Glucagon HT. | 4.5.3.2 |
| C10 | T2 | ovaries: oestrogen and progesterone; testes: testosterone, sperm production | OK | — | 8464 4.5.3.3 / 8461 4.5.3.4 |
| C11 | T3 | nerve impulses up to 120 m/s | OK (off-spec) | Fastest myelinated neurones ≈ 120 m/s. Context only, never a question. | — |
| C12 | T3 | nervous: electrical, short-lived, specific; hormonal: chemical in blood, minutes–days, any organ with receptor | OK | — | 4.5.2.1; 4.5.3.1 |
| C13 | T3 | emergency: nervous gives immediate response, adrenaline sustains it | OK, **HT** (adrenaline) | — | 4.5.3.6/4.5.3.7 |
| C14 | `higher` | tropic hormones TSH, ACTH; ADH controls kidney water reabsorption | OK but OFF-SPEC (TSH, ACTH, "tropic") / triple-higher (ADH) | Not on 8464; ADH is 8461 biology-only HT. | 8461 4.5.3.3 |
| C15 | `higher` | adrenaline raises blood glucose via liver glycogen → glucose (glycogenolysis) | OK | True; term off-spec. Spec: "boosts the delivery of oxygen and glucose to the brain and muscles". | 4.5.3.6/4.5.3.7 |
| C16 | `higher` | — | GAP | The section's one feedback statement, "Thyroxine levels are controlled by negative feedback", is absent from every field. | 4.5.3.6/4.5.3.7 |
| C17 | common_mistake | hormones travel in blood not nerves; only target organs respond | OK | — | 4.5.3.1 |
| C18 | key_note | glands and roles; slower but longer-lasting | OK | Thyroid/adrenal/glucagon clauses HT. | 4.5.3.1; 4.5.3.6 |
| C19 | matching (to be replaced) | six gland–hormone pairs | OK | Thyroid and adrenal pairs HT. | — |
| C20 | q1 key | via bloodstream, secreted directly by endocrine glands | OK | Spec wording. | 4.5.3.1 |
| C21 | q1 wx1 | hormones travel in blood, not nerves | OK | — | 4.5.3.1 |
| C22 | q1 wx2 | exocrine glands use ducts; endocrine have none | OK | — | — |
| C23 | q1 wx3 | hormones travel long distances; "paracrine signals" | OK | "Paracrine" is off-spec jargon; harmless in an explanation. | — |
| C24 | q2 key | adrenaline, adrenal glands, stress or danger | OK, **HT** | — | 4.5.3.6/4.5.3.7 |
| C25 | q2 wx1 | insulin lowers glucose, released after eating | OK | — | 4.5.3.2 |
| C26 | q2 wx2 | thyroxine controls long-term metabolic rate | OK | — | 4.5.3.6 |
| C27 | q2 wx3 | oestrogen = menstrual cycle, not acute stress | OK | — | 4.5.3.3 |
| C28 | q3 key | nervous fast, short-lived, specific; hormonal slower, longer-lasting, via blood | OK | Spec wording. | 4.5.3.1 |
| C29 | q3 wx1 | option 1 reversed | OK | — | — |
| C30 | q3 wx2 | both use chemicals somewhere (synapse / blood) but differ | OK | — | 4.5.2.1 |
| C31 | q3 wx3 | nervous controls muscles AND glands | OK | Effectors are muscles or glands. | 4.5.1 |

Count: **0 WRONG**. ROUTE: glucagon, thyroxine, adrenaline served on all routes (F1); ADH triple-higher (F3). GAP: thyroxine negative feedback (F2). OFF-SPEC: TSH/ACTH/tropic in `higher` (F3).

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| q2 | Adrenaline's role is 4.5.3.6/4.5.3.7, the whole section HT only | **Usable on CH and TH only.** |
| q1, q3 | correct, base | Usable on all four routes. |

## 5. Verdict
SOURCE OK WITH FLAGS. No wrong science. The base core (glands into blood, target organ, slower but longer, master gland, six gland positions) is all present. Thyroxine, adrenaline and glucagon are HT and currently sit in theory on every route; the HT section's negative-feedback statement for thyroxine is missing (written into the source from the spec). ADH is biology-only HT and has no other home on the site. **For Mide:** nothing.
