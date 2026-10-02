# Examination — Nuclear Fission (nuclear-fission) — AQA 8463 4.4.4.1 (physics only); no 8464 statement
Verdict: SOURCE OK WITH FLAGS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-16/04-checked-science-source/physics-6.4.5.1-nuclear-fission.md`.
Spec sources read as text: `AQA-8463-spec.txt` (v1.1, 30 Sep 2019) §4.4.4, §4.4.4.1, §4.4.4.2, §4.1.3; `AQA-8464-spec.txt` (v1.1, 04 Oct 2019) §6.1.3 (no fission statement in 8464); June 2026 equation sheets 8463 and 8464/8465 (neither prints E = mc²). Route audit `ks4-routes/docs/ks4/route-audit/physics.md` row `nuclear-fission`. Mark-scheme conventions from examiner knowledge of AQA 8463 papers 2018–2024; not fetched.

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n. The site's spec label "6.4.5.1 (physics only)" is the site's internal numbering; the true ref is **8463 4.4.4.1**.

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8463 | **4.4.4** | Nuclear fission and fusion | **(physics only)** |
| 8463 | **4.4.4.1** | Nuclear fission | physics only (no HT label anywhere in 4.4.4) |
| 8464 | — | no fission statement | — |
| Supporting | 8464 6.1.3 / 8463 4.1.3 National and global energy resources ("nuclear fuel"; environmental impact; reliability) | | base |
| Supporting | 8463 4.4.4.2 ("some of the mass may be converted into the energy of radiation") | | physics only |

Spec statements (8463 4.4.4.1, verbatim): "Nuclear fission is the splitting of a large and unstable nucleus (eg uranium or plutonium). Spontaneous fission is rare. Usually, for fission to occur the unstable nucleus must first absorb a neutron. The nucleus undergoing fission splits into two smaller nuclei, roughly equal in size, and emits two or three neutrons plus gamma rays. Energy is released by the fission reaction. All of the fission products have kinetic energy. The neutrons may go on to start a chain reaction. The chain reaction is controlled in a nuclear reactor to control the energy released. The explosion caused by a nuclear weapon is caused by an uncontrolled chain reaction. Students should be able to draw/interpret diagrams representing nuclear fission and how a chain reaction may occur."

## 2. Route table
| # | teachable point | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Fission = large unstable nucleus splits; U-235, Pu-239 (theory 1; key_note) | triple | 8463 4.4.4.1 | TF TH | OK (term "FISSILABLE" imprecise, C1) |
| R2 | Neutron absorbed first, then split (theory 1; common_mistake) | triple | 8463 4.4.4.1 | TF TH | OK |
| R3 | Two smaller nuclei + 2–3 neutrons + energy; example equation (theory 1) | triple | 8463 4.4.4.1 (+ 4.4.2.2 balancing) | TF TH | GAP — gamma rays, "roughly equal in size", KE of all products, "spontaneous fission is rare" missing (F2) |
| R4 | Mass defect, E = mc², ~200 MeV vs few eV (theory 1; common_mistake; key_note; equations) | not in spec (beyond 4.4.4.1) | — (4.4.4.2 states mass → radiation energy for fusion only) | TF TH | OFF-SPEC (F3) |
| R5 | Chain reaction; controlled (reactor) vs uncontrolled (weapon) (theory 2; key_note) | triple | 8463 4.4.4.1 | TF TH | OK |
| R6 | Critical mass (theory 2; key_note; `higher`) | not in spec | — | TF TH | OFF-SPEC (F3) |
| R7 | Moderator slows neutrons; thermal neutrons more likely to cause fission (theory 2, 3; key_note) | not named in spec — triple context | 8463 4.4.4.1 ("chain reaction is controlled in a nuclear reactor") | TF TH | OK as context (C9) |
| R8 | Control rods absorb neutrons (theory 3; common_mistake; q1) | triple (how the chain reaction "is controlled") | 8463 4.4.4.1 | TF TH | OK |
| R9 | Fuel rods, coolant, steam generator, shielding (theory 3) | not in spec — context | — | TF TH | OK, cut-able |
| R10 | Advantages/disadvantages of nuclear power (theory 3) | base | 8464 6.1.3; 8463 4.1.3 | TF TH | OK (base cross-reference) |
| R11 | `higher` (quantitative chain reaction, critical mass, controlled vs uncontrolled, reactor components) | NOT HT — 4.4.4 has no HT label; controlled/uncontrolled is triple core; critical mass is off-spec | 8463 4.4.4.1 | TH only (TF copy null) | ROUTE (F4) |
| R12 | equations: "E = mc²" | not in spec; on neither sheet | — | TF TH | OFF-SPEC (F3) |
| R13 | q1 (control rods) | triple | 8463 4.4.4.1 | TF TH | OK |
| R14 | q2 (why energy is released — mass defect) | beyond 4.4.4.1; consistent with 4.4.4.2 | 8463 4.4.4.1–4.4.4.2 | TF TH | OFF-SPEC, stretch only (F3) |
| — | rp, fifas, examiner_tip | none | — | — | correct: no RP and no calculation in 4.4.4.1 |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | theory 1 | "FISSILABLE MATERIALS" | IMPRECISE | The word is **fissile**. | — |
| C2 | theory 1 | U-235 most common; Pu-239 in some reactors and weapons | OK | Spec: "eg uranium or plutonium". | 4.4.4.1 |
| C3 | theory 1 | slow (thermal) neutron absorbed by U-235 → U-236, splits | OK | — | 4.4.4.1 |
| C4 | theory 1 | products: two smaller nuclei + 2–3 neutrons + energy | IMPRECISE (incomplete) | Spec adds: nuclei "roughly equal in size"; emits "two or three neutrons **plus gamma rays**"; "All of the fission products have kinetic energy". Add all three. | 4.4.4.1 |
| C5 | theory 1 | ²³⁵U + n → ²³⁶U → ¹⁴¹Ba + ⁹²Kr + 3n + energy | OK | Mass: 235 + 1 = 236 = 141 + 92 + 3 ✓. Charge: Ba 56 + Kr 36 = 92 ✓. | 4.4.2.2 skills |
| C6 | theory 1 | products' mass < reactants'; missing mass → energy, E = mc² | OFF-SPEC (correct physics) | Not in 4.4.4.1, which says only "Energy is released by the fission reaction". E = mc² is on no AQA GCSE sheet or recall list. Teach "energy is released; the products move off fast (kinetic energy)". | 4.4.4.1 |
| C7 | theory 1 | ~200 MeV per fission vs a few eV chemical | OK, OFF-SPEC | Values correct; MeV is not a GCSE unit. Could survive as "millions of times more than a chemical reaction". | — |
| C8 | theory 2 | 2–3 neutrons trigger further fissions → chain reaction; controlled = reactor; uncontrolled = weapon | OK | Spec wording. | 4.4.4.1 |
| C9 | theory 2 | critical mass definition; below/above | OFF-SPEC (correct) | Not in 8463. Cut or keep as one-line context. | — |
| C10 | theory 2 | fission neutrons are fast; moderator (water/graphite) slows them by elastic collisions; slow neutrons more likely to cause fission | OK (context) | Correct. Not named in spec; AQA items on reactors supply it. | — |
| C11 | theory 3 | fuel ~3–5 % U-235, rest U-238 | OK | — | — |
| C12 | theory 3 | control rods (boron/cadmium) absorb neutrons; deeper → less fission | OK | — | 4.4.4.1 ("controlled") |
| C13 | theory 3 | coolant water or CO₂; steam → turbine → generator | OK | — | — |
| C14 | theory 3 | advantages (low CO₂ in operation, energy-dense, reliable base load); disadvantages (cost, long-lived waste, accident risk) | OK | Base content, 8464 6.1.3 / 8463 4.1.3. | 6.1.3 |
| C15 | common_mistake | neutron absorbed first; fission ≠ radioactive decay; mass defect; control rods absorb | OK / OFF-SPEC | "Fission is NOT the same as radioactive decay" is fine at GCSE (spec: "Spontaneous fission is rare"). Mass-defect sentence off-spec (C6). | 4.4.4.1 |
| C16 | key_note | as above | OK / OFF-SPEC | Critical mass and E = mc² off-spec. | — |
| C17 | equations | "E = mc²" | OFF-SPEC | Not a spec equation; on neither June 2026 sheet. No triangle, no chip. | sheets |
| C18 | `higher` | listed as HT | ROUTE | 4.4.4 has no HT content. Controlled vs uncontrolled chain reaction is core for TF and TH; critical mass and "quantitative" chain reaction are off-spec. TF copy is null, so TF loses spec core. | 4.4.4.1 |
| C19 | q1 key | control rods absorb neutrons; deeper → slows chain reaction | OK | ✓ | 4.4.4.1 |
| C20 | q1 opt 2 / wx1 | slows neutrons → wx: moderators slow, control rods absorb | OK, aligned | ✓ | — |
| C21 | q1 opt 3 / wx2 | cool the core → wx: coolant removes thermal energy | OK, aligned | ✓ | — |
| C22 | q1 opt 4 / wx3 | contain fuel → wx: fuel rods / pressure vessel contain | OK, aligned | ✓ | — |
| C23 | q2 key | mass defect → energy via E = mc² | OFF-SPEC (correct) | Beyond 4.4.4.1. Stretch only. | — |
| C24 | q2 opt 2 / wx1 | chemical bonds → wx: nuclear forces; chemical energies millions of times smaller | OK, aligned | ~200 MeV vs few eV ≈ 10⁷–10⁸ ✓. | — |
| C25 | q2 opt 3 / wx2 | gamma radiation → wx: carries some energy, not the primary source | OK, aligned | Consistent with spec (gamma emitted; products have KE). | 4.4.4.1 |
| C26 | q2 opt 4 / wx3 | electrons released → wx: KE of fragments and mass-energy conversion | OK, aligned | — | 4.4.4.1 |
| C27 | matching (to be replaced) | four reactor components | OK | — | — |
| C28 | spec skill | "draw/interpret diagrams representing nuclear fission and how a chain reaction may occur" | GAP | No diagram in the source. Must-draw figure. | 4.4.4.1 |

Count: **0 WRONG**; IMPRECISE: C1, C4; OFF-SPEC: C6, C7, C9, C16, C17, C23; ROUTE: C18; GAP: C28. One arithmetic check (C5) ✓. No CFIFA Convert line in this file (no FIFA).

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| q1 | correct; triple | Usable TF TH. |
| q2 | correct physics, beyond 4.4.4.1 | Usable TF TH as a stretch item only, not as a spec rung. |
| `equations` "E = mc²" | off-spec | Do not show as a lesson equation. |

## 5. For the lesson author
**Misconceptions seen in AQA marking**: fission confused with radioactive decay (alpha emission); "the nucleus splits by itself" (neutron absorption omitted); control rods "slow the neutrons" (moderator); "electrons are released"; "chain reaction" described as one nucleus splitting several times; gamma rays omitted from the products list.

**Command words**: Describe, Draw/complete (chain-reaction diagram), Explain (how the reactor is controlled), Compare (reactor vs weapon).

**Typical questions** ⚑ examiner-drafted
- *Describe the process of nuclear fission. [3]* — unstable nucleus absorbs a neutron (1); splits into two smaller nuclei (1); releases 2–3 neutrons / gamma rays / energy (1).
- *Explain how a chain reaction occurs. [2]* — neutrons released by one fission (1) are absorbed by other nuclei, causing further fissions (1).
- *Explain why the chain reaction in a reactor is controlled but in a weapon is not. [2]* — reactor: energy released at a steady/safe rate (1); weapon: uncontrolled chain reaction → explosion (1).

**Required practical**: none. **Equations**: none in spec.

## 6. Verdict
SOURCE OK WITH FLAGS. All science correct; no frozen item is wrong. The source omits four spec statements (gamma rays, roughly equal fragments, KE of products, spontaneous fission rare) and the chain-reaction diagram, and carries off-spec E = mc² / critical mass. The `higher` field is not HT — its spec content (controlled vs uncontrolled) is core for TF too.

**For Mide:** nothing. All route facts are settled by the spec's own labels.
