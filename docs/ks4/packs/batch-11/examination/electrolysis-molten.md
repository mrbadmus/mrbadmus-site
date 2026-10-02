# Examination — Electrolysis of Molten Ionic Compounds (electrolysis-molten) — AQA 8464 5.4.3.2 / 8462 4.4.3.2 (+ HT 8464 5.4.3.1, 5.4.3.5 / 8462 4.4.3.1, 4.4.3.5)
Verdict: SOURCE HAS ERRORS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-11/04-checked-science-source/chemistry-5.4.3.2-electrolysis-molten.md`.
Spec sources read as text: `AQA-8464-spec.txt` (v1.1) 5.4.3.1–5.4.3.5 and RP9 (the only Trilogy electrolysis RP); `AQA-8462-spec.txt` (v1.1) 4.4.3.1–4.4.3.5, §8.2.3 (RP3) and §8.2.4 (RP4 = temperature changes). No AQA required practical uses a molten electrolyte. No equation sheet applies. Route audit read: `ks4-routes/docs/ks4/route-audit/chemistry.md` row `electrolysis-molten` (CF CH TF TH, base, OK); the audit did not tag the half equations in theory/equations as HT, nor the RP label.

Conventions: q1–q2 quiz items; wx n = `wrong_explanations` key n; th1–th3 theory chunks. CF and TF copies differ only in `higher` (`null`), so `higher` is served on CH TH.

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 / 8462 | **5.4.3.2 / 4.4.3.2** | Electrolysis of molten ionic compounds | base |
| 8464 / 8462 | 5.4.3.1 / 4.4.3.1 | The process of electrolysis (HT para: half equations) | base / **HT only** para |
| 8464 / 8462 | 5.4.3.5 / 4.4.3.5 | Half equations at electrodes | **(HT only)** |
| 8464 / 8462 | 5.4.3.3 / 4.4.3.3 | Using electrolysis to extract metals | base |
| 8464 RP9 / 8462 RP3 | 5.4.3.4 / 4.4.3.4 | Electrolysis of **aqueous** solutions — the electrolysis RP | base |

Spec statement (verbatim, 8464 = 8462) 5.4.3.2: "When a simple ionic compound (eg lead bromide) is electrolysed in the molten state using inert electrodes, the metal (lead) is produced at the cathode and the non-metal (bromine) is produced at the anode. Students should be able to predict the products of the electrolysis of binary ionic compounds in the molten state." Skills column: "A safer alternative for practical work is anhydrous zinc chloride."
RP (8464 RP9 = 8462 RP3): "investigate what happens when aqueous solutions are electrolysed using inert electrodes. This should be an investigation involving developing a hypothesis."

## 2. Route table
| # | teachable point (pack location) | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Molten: only the compound's ions; metal at cathode, non-metal at anode (th1; common_mistake; key_note) | base | 5.4.3.2 | all four | OK |
| R2 | Molten NaCl → Na + Cl₂; PbBr₂ → Pb + Br₂ (th1; key_note; equations 1–2) | base | 5.4.3.2 | all four | OK |
| R3 | Half equations Na⁺ + e⁻ → Na, 2Cl⁻ → Cl₂ + 2e⁻, Pb²⁺ + 2e⁻ → Pb, 2Br⁻ → Br₂ + 2e⁻ (th1; equations 3–4) | higher | 5.4.3.1 (HT para); 5.4.3.5 | all four | ROUTE (EM-F2) |
| R4 | "This is reduction — metal ions GAIN electrons … oxidation — non-metal ions LOSE electrons" (common_mistake; key_note "lose electrons") | higher | 5.4.3.5 (HT only) | all four | ROUTE (EM-F2) |
| R5 | Solid vs molten: ions fixed vs free (th2; th3; key_note) | base | 5.4.3.1 | all four | OK |
| R6 | High melting points, energy cost; Al₂O₃ in cryolite (th2) | base | 5.4.3.3 | all four | OK (belongs to electrolysis-extraction) |
| R7 | PbBr₂ demonstration observations (th3) | base (context) | 5.4.3.2 | all four | OK |
| R8 | `rp` — "RP4 (Chemistry) … electrolysis of lead(II) bromide" | none — not an AQA RP | — | all four | WRONG (EM-F1) |
| R9 | `higher` — balanced half equations, combine to overall | higher | 5.4.3.1 (HT para) | CH TH | OK |
| R10 | `higher` — product prediction from ion identity | base (not HT) | 5.4.3.2 | CH TH | ROUTE (EM-F3) |
| R11 | `higher` — why metals above carbon need electrolysis | base (not HT) | 5.4.3.3 | CH TH | ROUTE (EM-F3) |
| R12 | quiz q1 (CaCl₂, cathode) | base (key's "reduced" is HT wording) | 5.4.3.2 | all four | OK |
| R13 | quiz q2 (why melt PbBr₂) | base | 5.4.3.1–5.4.3.2 | all four | OK, wx3 imprecise (EM-F4) |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | th1 | molten compound: only its own ions present | OK | — | 5.4.3.2 |
| C2 | th1 | metal ion discharged at cathode; non-metal at anode | OK | — | 5.4.3.2 |
| C3 | th1 | NaCl: Na⁺ + e⁻ → Na (liquid); 2Cl⁻ → Cl₂ + 2e⁻ (yellow-green, toxic) | OK | Balanced, charge ✓. Na (mp 98 °C, bp 883 °C) is liquid at 801 °C ✓. | 5.4.3.5 |
| C4 | th1 | PbBr₂: Pb²⁺ + 2e⁻ → Pb; 2Br⁻ → Br₂ + 2e⁻; brown | OK | ✓ | 5.4.3.5 |
| C5 | th2 | solid fixed / molten free ions | OK | — | 5.4.3.1 |
| C6 | th2 | NaCl melts at 801 °C; high energy | OK | ✓ | 5.4.3.3 |
| C7 | th2 | Al₂O₃ dissolved in molten cryolite lowers ~2050 °C → ~950 °C | OK | Al₂O₃ mp ≈ 2072 °C; cell ≈ 950–970 °C ✓. Spec: "explain why a mixture is used". | 5.4.3.3 |
| C8 | th3 | before melting no conductivity; after, circuit completes | OK | — | — |
| C9 | th3 | "Grey metallic liquid appears at the negative electrode … Lead forms as liquid" | OK (minor) | PbBr₂ mp 373 °C > Pb mp 327 °C, so liquid ✓. Molten lead looks silvery and collects under the cathode. | — |
| C10 | th3 | reddish-brown bromine vapour at anode | OK | — | 5.4.3.2 |
| C11 | th3; equation 2 | PbBr₂(l) → Pb(l) + Br₂(g) | OK | ✓ | — |
| C12 | equation 1 | 2NaCl(l) → 2Na(l) + Cl₂(g) | OK | ✓ | — |
| C13 | rp | "RP4 (Chemistry) — Carry out electrolysis of lead(II) bromide. Observe products at each electrode. Safety: work in fume cupboard — bromine is toxic." | WRONG | Not an AQA required practical on any route. Chemistry RP4 is temperature changes in reacting solutions. The electrolysis RP is **aqueous** (Combined RP9, Chemistry RP3 — `electrolysis-aqueous`). Molten PbBr₂ is a teacher demonstration in a fume cupboard; the spec names anhydrous zinc chloride as the safer alternative for practical work. Safety sentence is correct. | 8464 5.4.3.4; 8462 §8.2.3–8.2.4 (EM-F1) |
| C14 | higher | balanced half equations; combine to overall | OK | HT ✓. | 5.4.3.1 |
| C15 | higher | "Explain product prediction from ion identity" | OK science; not HT | Base skill. | 5.4.3.2 (EM-F3) |
| C16 | higher | "reactive metals above carbon cannot be extracted by carbon reduction — electrolysis of molten compound is the only option" | OK science; not HT | Base, and belongs to `electrolysis-extraction`. Spec also: "or if the metal reacts with carbon". | 5.4.3.3 (EM-F3) |
| C17 | common_mistake | metal always at cathode; non-metal always at anode (for molten binary compounds) | OK | Reduction/electron clauses HT. | 5.4.3.2; 5.4.3.5 |
| C18 | key_note | as above | OK | — | — |
| C19 | q1 key | calcium metal; Ca²⁺ reduced at the negative cathode | OK | Answerable at base; the word "reduced" is HT framing (Foundation meets reduction only as loss of oxygen, 5.4.1.3). | 5.4.3.2 |
| C20 | q1 opt 1 / wx1 | chlorine at cathode / Cl⁻ goes to anode | OK | Aligned. | — |
| C21 | q1 opt 2 / wx2 | no decomposition / electrolysis does decompose | OK | Aligned. | — |
| C22 | q1 opt 3 / wx3 | CaO / "Electrolysis is done in an enclosed container — calcium doesn't react with air at this stage." | IMPRECISE (minor) | Not a reliable fact; the point is that the cathode product comes from the electrolyte's own ions. Aligned; usable. | EM-F5 |
| C23 | q2 key | ions fixed in solid; melting frees them | OK | — | 5.4.3.1 |
| C24 | q2 opt 1 / wx1 | formula changes / PbBr₂ either way | OK | Aligned. | — |
| C25 | q2 opt 2 / wx2 | electrodes cannot penetrate / solid still won't conduct | OK | Aligned. | — |
| C26 | q2 opt 3 / wx3 | no ions in solid / "Lead bromide is ionic in BOTH … — Na⁺ and Cl⁻ (or Pb²⁺ and Br⁻) ions exist in the solid too." | IMPRECISE | Names sodium chloride's ions first in a lead bromide item (copied from the NaCl item). Not false, but confusing. Aligned; usable. | EM-F4 |
| C27 | matching (to be replaced) | NaCl and PbBr₂ electrode products | OK | — | — |

Count: **1 WRONG** (C13, the RP label). IMPRECISE: C22, C26. No calculations (balancing half equations is HT, not a calculation).

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| q1 | correct; base answer | Usable on all four routes. |
| q2 | correct; wx3 names NaCl ions (C26) | Usable on all four routes. |
| equations 3–4 (half equations) | HT | Show on CH TH only. |
| rp | not an AQA RP | Do not render as a required practical on any route. |

## 5. For the lesson author
**Misconceptions seen in AQA marking**: "sodium is produced at the anode"; writing "chloride" (the ion) for the product "chlorine"; "Br" instead of Br₂ / "Cl" instead of Cl₂; "the ions are made when it melts"; at HT, unbalanced electrons (Pb²⁺ + e⁻ → Pb) or electrons on the wrong side at the anode.
**Command words**: Predict the products; Explain why the compound must be molten; (HT) Complete and balance the half equation.

## 6. Verdict
SOURCE HAS ERRORS. All chemistry correct; the `rp` field invents a required practical (molten PbBr₂ is a demonstration; the electrolysis RP is aqueous, RP9/RP3); the half equations and the electron-gain/loss language are HT but served on all four routes; two `higher` sentences are base. Nothing for Mide.
