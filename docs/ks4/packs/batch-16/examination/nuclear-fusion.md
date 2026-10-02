# Examination — Nuclear Fusion (nuclear-fusion) — AQA 8463 4.4.4.2 (physics only); no 8464 statement
Verdict: SOURCE HAS ERRORS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-16/04-checked-science-source/physics-6.4.5.2-nuclear-fusion.md`.
Spec sources read as text: `AQA-8463-spec.txt` (v1.1) §4.4.4, §4.4.4.1, §4.4.4.2, §4.4.2.2, §4.8.1.2; `AQA-8464-spec.txt` (v1.1) §6.1.3 (no fusion statement in 8464); June 2026 equation sheets 8463 and 8464/8465. Route audit row `nuclear-fusion`. Mark-scheme conventions from examiner knowledge of AQA 8463 papers 2018–2024; not fetched.

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n. Site label "6.4.5.2 (physics only)" is internal; true ref **8463 4.4.4.2**.

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8463 | **4.4.4** | Nuclear fission and fusion | **(physics only)** |
| 8463 | **4.4.4.2** | Nuclear fusion | physics only (no HT label) |
| 8464 | — | no fusion statement | — |
| Supporting | 8463 4.8.1.2 Life cycle of a star (physics only) — fusion in stars | | physics only |
| Supporting | 8463 4.4.2.2 Nuclear equations — balancing mass and atomic numbers | | base |

Spec statement (8463 4.4.4.2, verbatim, the whole of it): "Nuclear fusion is the joining of two light nuclei to form a heavier nucleus. In this process some of the mass may be converted into the energy of radiation."

## 2. Route table
| # | teachable point | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Fusion = two light nuclei join → heavier nucleus + energy (theory 1; key_note) | triple | 8463 4.4.4.2 | TF TH | OK |
| R2 | Fusion vs fission contrast (theory 1, 3; key_note; matching) | triple | 8463 4.4.4.1–4.4.4.2 | TF TH | OK |
| R3 | Mass → energy (common_mistake) | triple | 8463 4.4.4.2 | TF TH | OK (E = mc² itself off-spec) |
| R4 | Stars powered by fusion; 4 protons → He-4 (theory 1) | triple | 8463 4.8.1.2 | TF TH | OK, simplified (C3) |
| R5 | D-T reaction ²H + ³H → ⁴He + n + 17.6 MeV (theory 1; equations; key_note) | triple context (balancing is base 4.4.2.2) | 8463 4.4.2.2 | TF TH | OK, MeV off-spec |
| R6 | Electrostatic repulsion, strong force, ~100 million °C, plasma (theory 2; common_mistake; `higher`; q1) | not in spec | — | TF TH (`higher` TH) | OFF-SPEC; one number WRONG (F1) |
| R7 | Magnetic / inertial confinement, JET, ITER, NIF (theory 2, 3; `higher`) | not in spec | — | TF TH | OFF-SPEC; dated facts (C11) |
| R8 | Fusion as an energy source: advantages, challenges, status (theory 3; key_note; q2) | not in spec (4.1.3 lists energy resources; fusion is not one) | — | TF TH | OFF-SPEC (F3) |
| R9 | `higher` | NOT HT — 4.4.4 has no HT label; its content is off-spec | — | TH only (TF null) | ROUTE / OFF-SPEC (F4) |
| R10 | q1 (why high temperature) | not in spec | — | TF TH | OFF-SPEC, stretch only |
| R11 | q2 (advantage over fission) | not in spec | — | TF TH | not usable as written (F2) |
| — | rp, fifas, examiner_tip | none | — | — | correct |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | theory 1 | fusion = joining of two small nuclei → larger nucleus, releasing energy | OK | Spec: "two light nuclei … heavier nucleus". | 4.4.4.2 |
| C2 | theory 1 | Sun and all stars powered by fusion | OK | Main-sequence stars; fine at GCSE. | 4.8.1.2 |
| C3 | theory 1 | "Four protons → helium-4 nucleus … + energy" | IMPRECISE | Net reaction also emits 2 positrons and 2 neutrinos. Say "hydrogen nuclei fuse, in several steps, to make helium". | 4.8.1.2 |
| C4 | theory 1; equations | ²H + ³H → ⁴He + n + 17.6 MeV | OK | Mass 2 + 3 = 4 + 1 ✓; charge 1 + 1 = 2 + 0 ✓; 17.6 MeV ✓. | 4.4.2.2 |
| C5 | theory 1 | deuterium from seawater; tritium from lithium | OK | Tritium is bred from lithium in the reactor. | — |
| C6 | theory 2 | nuclei repel; must get close enough for the strong force | OFF-SPEC (correct) | — | — |
| C7 | theory 2 | "~100 million °C (ten times hotter than the Sun's core …)" | **WRONG** | Sun's core ≈ 15 million °C, so 100 million °C is about **six to seven** times hotter. | — |
| C8 | theory 2 | plasma = fully ionised gas | OK (off-spec) | — | — |
| C9 | theory 2 | magnetic (tokamak — JET, ITER) and inertial (lasers — NIF) confinement; stars confine by gravity | OK (off-spec) | — | — |
| C10 | theory 3 | advantages: abundant fuel, no CO₂ in operation, no long-lived waste, inherently safe | OK (off-spec) | "No long-lived waste" is fair (activated walls decay over ~100 years); tritium is itself radioactive and goes unmentioned. | — |
| C11 | theory 3 | "JET … record fusion energy output 2022"; "ITER costs ~€20 billion"; "first commercial power 2040s–2050s" | IMPRECISE (dated) | JET's final record was 69 MJ (Oct 2023, announced Feb 2024) before it closed in Dec 2023; ITER cost estimates now well above €20 bn. Cut dated figures: they are off-spec and will age. | — |
| C12 | theory 3 | "net energy gain not yet achieved consistently" | OK | NIF passed target gain > 1 (Dec 2022) but not wall-plug gain. | — |
| C13 | common_mistake | product has less mass; mass converted (E = mc²); needs very high temperature, not just pressure | OK | First half is the spec statement. E = mc² off-spec. | 4.4.4.2 |
| C14 | key_note | summary incl. ~100 million °C, tokamak/ITER | OK (off-spec parts) | — | — |
| C15 | `higher` | listed as HT | ROUTE / OFF-SPEC | 4.4.4 has no HT content; this text (Coulomb repulsion, confinement, evaluation) is all beyond the spec. | 4.4.4.2 |
| C16 | q1 key | KE to overcome electrostatic repulsion; strong force | OK, OFF-SPEC | Correct physics; beyond 4.4.4.2. Stretch only. | — |
| C17 | q1 opt 2 / wx1 | "so much energy … must start at high T" → wx: energy comes from fusion; high T is the requirement | OK, aligned | — | — |
| C18 | q1 opt 3 / wx2 | "radioactive materials only become fusible …" → wx: D and T are isotopes of hydrogen, need not be radioactive | OK, aligned | (Tritium is in fact radioactive; the wx does not deny it.) | — |
| C19 | q1 opt 4 / wx3 | "plasma … only state in magnetic field" → wx: plasma needed for confinement, but the reason is repulsion | OK, aligned | — | — |
| C20 | q2 key | "virtually unlimited fuel from seawater, no long-lived waste, inherently safe" | IMPRECISE | Only deuterium comes from seawater; tritium is made from lithium. Question asks for "the main advantage" but the key lists three. | — |
| C21 | q2 opt 2 / wx1 | "already used commercially" → wx: not yet; research reactors | OK, aligned | — | — |
| C22 | q2 opt 3 / wx2 | "Fusion produces more energy per reaction than fission" → wx: "comparison isn't straightforward per reaction" | **WRONG (wx)** | The comparison is straightforward and the option is false: one fission releases ≈ 200 MeV, one D-T fusion ≈ 17.6 MeV, so **fission releases more per reaction**. (Per kilogram of fuel, fusion releases more.) The wx dodges the fact. | — |
| C23 | q2 opt 4 / wx3 | "no confinement, room temperature" → wx: needs extreme T and confinement | OK, aligned | — | — |
| C24 | matching (to be replaced) | fusion/fission/both sort | OK | — | — |

Count: **2 WRONG** (C7 theory — re-cuttable; C22 frozen wx); IMPRECISE: C3, C11, C20; OFF-SPEC: R6–R8, C15, C16. Two equation balances checked ✓. No CFIFA Convert line in this file (no FIFA).

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| q1 | correct physics; beyond 4.4.4.2 | Usable TF TH as a stretch item only, not as a spec rung. |
| q2 | wx2 is wrong; key imprecise; whole item off-spec | **Do not use as written.** |

## 5. For the lesson author
**Misconceptions seen in AQA marking**: fusion and fission swapped; "fusion splits atoms"; "fusion is used in power stations now"; energy said to come from nowhere / from "joining bonds"; "light nuclei" written as "light atoms" or "light elements" (accept at GCSE, but the spec says nuclei).

**Command words**: Describe, Compare (fusion with fission), State (where fusion happens).

**Typical questions** ⚑ examiner-drafted
- *Describe the difference between nuclear fission and nuclear fusion. [2]* — fission: a large nucleus splits into two smaller nuclei (1); fusion: two light nuclei join to form a heavier nucleus (1).
- *Where does the energy released in fusion come from? [1]* — some of the mass is converted into energy (of radiation).

**Required practical**: none. **Equations**: none in spec.

## 6. Verdict
SOURCE HAS ERRORS. The spec core (two sentences) is present and correct. One wrong number in theory ("ten times hotter than the Sun's core") and one wrong frozen wrong_explanation (q2 wx2). Most of the file is beyond the spec; dated reactor facts should be cut.

**For Mide:** nothing. Settled facts.
