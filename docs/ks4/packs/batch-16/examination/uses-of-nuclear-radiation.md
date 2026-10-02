# Examination — Uses of Nuclear Radiation (uses-of-nuclear-radiation) — AQA 8463 4.4.3.3 (physics only) (+ 4.4.3.2)
Verdict: SOURCE OK WITH FLAGS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-16/04-checked-science-source/physics-6.4.4-uses-of-nuclear-radiation.md`.
Spec sources read as text: `AQA-8463-spec.txt` (v1.1) §4.4.2.1–4.4.3.3; `AQA-8464-spec.txt` (v1.1) §6.4.2.1 (base "apply knowledge to the uses of radiation"). Equation sheets: none apply. Route audit row `uses-of-nuclear-radiation` (TF TH / TF TH, OK — "The spec names medical uses only. Industrial uses (smoke alarms, gauges) go beyond it."). Neighbour: batch 5 `radioactive-decay` already teaches smoke detectors and thickness gauges as base applications of 6.4.2.1.

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n; T1–T3 = theory chunks. The source's `spec` field reads "6.4.4 (physics only)" — the true reference is **8463 4.4.3.3** (with 4.4.3.2 for half-life choice); there is no 8464 equivalent.

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8463 | **4.4.3.3** | Uses of nuclear radiation | physics only |
| 8463 | **4.4.3.2** | Different half-lives of radioactive isotopes | physics only |
| Supporting | 8464 6.4.2.1 / 8463 4.4.2.1 — "apply their knowledge to the uses of radiation and evaluate the best sources of radiation to use in a given situation" | | base |

Spec statements (verbatim, 8463 4.4.3.3): "Nuclear radiations are used in medicine for the: • exploration of internal organs • control or destruction of unwanted tissue. Students should be able to: • describe and evaluate the uses of nuclear radiations for exploration of internal organs, and for control or destruction of unwanted tissue • evaluate the perceived risks of using nuclear radiations in relation to given data and consequences." (WS 1.4, 1.5)
8463 4.4.3.2: "Radioactive isotopes have a very wide range of half-life values. Students should be able to explain why the hazards associated with radioactive material differ according to the half-life involved."

## 2. Route table
| # | teachable point | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Radiotherapy: Co-60 γ, crossing beams (T1; key_note; matching) | triple | 8463 4.4.3.3 (destruction of unwanted tissue) | TF TH | OK; internal sources missing (F3) |
| R2 | Tracers: γ emitter, gamma camera, Tc-99m, I-123 (T1; common_mistake; key_note; q2) | triple | 8463 4.4.3.3 (exploration of internal organs) | TF TH | OK |
| R3 | Sterilising equipment and food with γ (T1) | base application | 6.4.2.1; 6.4.2.4 | TF TH | OK |
| R4 | Thickness monitoring with β (T2; common_mistake; key_note) | base application (already in batch 5) | 6.4.2.1 | TF TH | OK; "proportional" imprecise (F4) |
| R5 | Smoke detectors with α (T2; q1) | base application (already in batch 5) | 6.4.2.1 | TF TH | OK |
| R6 | Pipeline fault detection with γ (T2) | base application | 6.4.2.1 | TF TH | IMPRECISE mechanism (F4) |
| R7 | Carbon dating (T2) | not in spec (context) | — | TF TH | OK as context only |
| R8 | Choosing type: ionisation, penetration (T3) | base | 6.4.2.1 | TF TH | OK; β wording (F4) |
| R9 | Choosing half-life: tracers short, industrial long, dating comparable (T3; key_note) | triple | 8463 4.4.3.2 | TF TH | OK |
| R10 | Evaluate perceived risks against given data and consequences | triple | 8463 4.4.3.3 | — | **GAP — missing** (F2) |
| R11 | `higher` field: evaluate choice; activity remaining; why half-lives chosen | **triple (not HT)**; "activity remaining" is the half-lives lesson (base; ratio HT) | 8463 4.4.3.2–4.4.3.3; 6.4.2.3 | TH only (TF copy null) | ROUTE (F1) |
| R12 | q1 (Am-241 α in smoke detectors) | base application | 6.4.2.1 | TF TH | OK — usable |
| R13 | q2 (tracer: γ + short half-life) | triple | 8463 4.4.3.2–4.4.3.3 | TF TH | OK — usable |
| — | rp, equations, fifas, examiner_tip | none | — | — | correct |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | T1 | Co-60 γ beams from several directions cross at the tumour; healthy tissue spared | OK | — | 4.4.3.3 |
| C2 | T1 | kills cancer cells by damaging DNA; γ reaches internal tumours | OK | — | — |
| C3 | T1 | only external γ beams given for "control or destruction of unwanted tissue" | GAP | Internal sources are the other standard AQA context: an implanted β/γ source, or I-131 taken up by the thyroid to destroy overactive or cancerous tissue. | 4.4.3.3 |
| C4 | T1 | tracer: γ emitter injected; gamma camera; shows function | OK | — | 4.4.3.3 |
| C5 | T1 | Tc-99m ~6 h; I-123 → thyroid | OK | Tc-99m 6.0 h ✓; I-123 is a γ emitter, 13 h ✓. | — |
| C6 | T1 | α/β would not leave the body | OK | Also: α inside the body would do most damage. | — |
| C7 | T1 | γ sterilisation of sealed equipment; no heat; food | OK | Irradiated items do not become radioactive (6.4.2.4). | 6.4.2.4 |
| C8 | T2 | β thickness gauge: more absorbed → thicker; feedback to rollers | OK | — | 6.4.2.1 |
| C9 | T2 | "Beta chosen: absorbed by the sheet but not by surrounding air" | IMPRECISE | β is **partly** absorbed by the sheet, and the amount changes with thickness; β is also absorbed by air over about a metre. | 6.4.2.1 |
| C10 | T2 | α too weak to penetrate; γ too penetrating to show changes | OK | — | 6.4.2.1 |
| C11 | T2 | Am-241 α ionises air, current; smoke absorbs α → current drops → alarm | OK | GCSE-standard account. | 6.4.2.1 |
| C12 | T2 | α short range — stays in casing; ionises air well | OK | — | — |
| C13 | T2 | "Gamma source moved through underground pipe … Crack or fault → more gamma escapes" | IMPRECISE | Not the standard method. Leaks are found by adding a short-half-life γ-emitting **tracer** to the fluid; where it leaks it collects in the soil and the surface detector reads higher. γ passes through the pipe wall anyway, so a crack barely changes what escapes. | 6.4.2.1 |
| C14 | T2 | carbon dating, ¹⁴C/¹²C, 5730 y | OK | Off-spec context. | — |
| C15 | T3 | α: high ionisation, short range | OK | — | 6.4.2.1 |
| C16 | T3 | "BETA: Moderate penetration — can pass through a few mm of material. Absorbed by aluminium" | IMPRECISE | Read together, these contradict each other. β passes through paper and is stopped by a few mm of aluminium. | 6.4.2.1 |
| C17 | T3 | γ: high penetration; least ionising; imaging, radiotherapy, sterilisation, pipelines; lead/concrete | OK | Lead/concrete **reduce** γ; nothing stops all of it. | 6.4.2.1 |
| C18 | T3 | half-life: tracers short, industrial long, dating comparable | OK | The 4.4.3.2 point. | 4.4.3.2 |
| C19 | `higher` | as R11 | ROUTE | No HT statement exists in 4.4.3.2–4.4.3.3. Evaluating choices must be on TF as well. | 4.4.3.3 |
| C20 | — | no perceived-risk evaluation against given data | GAP | Spec bullet 2. | 4.4.3.3 |
| C21 | common_mistake | β thickness, α smoke, γ imaging/radiotherapy, short half-life tracers | OK | — | — |
| C22 | key_note / matching | "absorbed proportional to thickness" | IMPRECISE | Absorption **increases** with thickness; it is not proportional. | — |
| C23 | q1 key | α ionises air well and has short range | OK | — | 6.4.2.1 |
| C24 | q1 opt 2 / wx1 | "less dangerous" is not precise enough | OK | Aligned. | — |
| C25 | q1 opt 3 / wx2 | γ can ionise air; α more strongly | OK | Aligned. | — |
| C26 | q1 opt 4 / wx3 | Am-241 half-life ~432 y; not the main reason | OK | Aligned; 432 y ✓. | — |
| C27 | q2 key | γ reaches an external detector; short half-life → low dose | OK | — | 4.4.3.2–4.4.3.3 |
| C28 | q2 opt 2 / wx1 | γ is least ionising | OK | Aligned. | 6.4.2.1 |
| C29 | q2 opt 3 / wx2 | "safest" oversimplifies | OK | Aligned. | — |
| C30 | q2 opt 4 / wx3 | short half-life = decays quickly | OK | Aligned. | — |

Count: **0 WRONG**. IMPRECISE: C9, C13, C16, C22. GAP: C3, C20. ROUTE: C19.

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| none | q1 (base application) and q2 (triple) correct | Both usable on TF and TH. q1 repeats batch 5's `radioactive-decay` smoke-detector content — fine as recall, not the page's centre. |

## 5. Verdict
SOURCE OK WITH FLAGS. The science is sound; the shape is off-centre. The spec for this page is **medical** — exploring internal organs and destroying unwanted tissue, and evaluating perceived risk from data — while half the source is industrial uses that batch 5's `radioactive-decay` already teaches. Design should lead with medicine, add internal treatment (I-131 / implants) and a risk-evaluation task, and keep industrial uses as quick review. The `higher` field is not HT and belongs on TF too.

**For Mide:** nothing — all settled from the spec.
