# Examination — Dark Matter and Dark Energy (dark-matter-dark-energy) — AQA 8463 4.8.2 (physics only)
Verdict: SOURCE OK WITH FLAGS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-18/04-checked-science-source/physics-6.8.4-dark-matter-dark-energy.md`.
Spec sources read as text: `AQA-8463-spec.txt` (v1.1, 30 Sep 2019) §4.8 intro, 4.8.1, 4.8.2; `AQA-8464-spec.txt` (no space physics); `8463-equation-sheet-Jun26.txt` (no space equation). Route audit row `dark-matter-dark-energy` (TH → **TF TH**, "MOVE WIDER"; §2 item 6). Neighbour read: batch-5 `examination/red-shift-big-bang.md` and its flags (F4 CMBR off-spec; F5 1998 supernova statement).

Conventions: T1–T3 = theory chunks; q1–q2 = quiz items; "wx n" = `wrong_explanations` key n. One route copy (TH). No fifas, no equations, no `[NEW — to be examined]` lines.

**Spec ref and route settled.** The frozen "6.8.4 (HT only, physics only)" names a section that does not exist and an HT label the spec does not give. The content is **8463 4.8.2 Red-shift (physics only)**, which carries no "(HT only)" statement anywhere. True routes: **TF TH**. Site currently ships TH; moving to TF TH under the approved route-flag PR. The frozen `higher` text opens "HT only —"; that label is wrong.

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 | — | none (no space physics) | — |
| 8463 | **4.8.2** | Red-shift | physics only (no HT) |
| Context | 8463 4.8 intro (not a content statement) | Space physics | physics only |

Spec statements (verbatim):
- 4.8.2: "Since 1998 onwards, observations of supernovae suggest that distant galaxies are receding ever faster." "Students should be able to explain: … • how scientists are able to use observations to arrive at theories such as the Big Bang theory • that there is still much about the universe that is not understood, for example dark mass and dark energy."
- 4.8 intro: "'Dark matter', which bends light and holds galaxies together but does not emit electromagnetic radiation, is everywhere – what is it? And what is causing the universe to expand ever faster?"

## 2. Route table
| # | teachable point | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Dark matter: no EM emission/absorption/reflection; detected by gravity (T1; common_mistake; key_note) | triple | 4.8 intro; 4.8.2 | TH | OK (common_mistake IMPRECISE, F4) |
| R2 | Rotation curves: outer stars not slower than expected → unseen mass (T1; q1; matching) | triple (context: "holds galaxies together") | 4.8 intro | TH | OK; "same speed" IMPRECISE (F3) |
| R3 | Gravitational lensing stronger than visible mass predicts (T1; matching) | triple (context: "bends light") | 4.8 intro | TH | OK |
| R4 | CMB fluctuations → ~27%; WIMPs, axions, sterile neutrinos (T1) | none — off-spec | — | TH | OFF-SPEC (F2) |
| R5 | Dark energy: unknown cause of accelerating expansion (T2; key_note) | triple | 4.8 intro; 4.8.2 | TH | OK |
| R6 | 1998 distant supernovae → receding ever faster (T2; q2; key_note) | triple | 4.8.2 | TH | OK |
| R7 | Type Ia standard candles; "further than expected"; cosmological constant / "biggest blunder" (T2) | triple (context) | 4.8.2 | TH | OK / IMPRECISE (F5) |
| R8 | 5% / 27% / 68%; ~85% of matter dark (T1; T2; T3; key_note; matching) | none — enrichment | — | TH | OFF-SPEC (F2) |
| R9 | Fate of the universe; Euclid, DES, LHC, Fermi (T3) | none — enrichment | — | TH | OFF-SPEC (F2) |
| R10 | Much not understood — great unsolved problem (T3; common_mistake; key_note) | triple | 4.8.2 | TH | OK |
| R11 | `higher` "HT only — …" | triple (not HT) | 4.8.2 | TH | ROUTE (F1) |
| R12 | q1 | triple (context) | 4.8 intro | TH | usable TF TH |
| R13 | q2 | triple | 4.8.2 | TH | usable TF TH |
| — | RP, equations, fifas | none | — | — | correct |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | T1 | dark matter does not emit, absorb or reflect EM radiation; invisible to all telescopes | OK | Spec: "does not emit electromagnetic radiation". | 4.8 intro |
| C2 | T1 | outer stars "orbit at the same speed as those near the centre" | IMPRECISE | Observed: beyond the inner region, orbital speed stays roughly constant instead of falling. Say "about the same speed — they do not slow down as expected". | — |
| C3 | T1 | gravity predicts outer stars slower, like solar-system planets | OK | — | — |
| C4 | T1 | ~85% of matter invisible | OK (enrichment) | 27 / (27 + 5) ≈ 84% ✓ consistent with T3. | — |
| C5 | T1 | lensing greater than visible matter accounts for | OK | Spec: "bends light". | 4.8 intro |
| C6 | T1 | CMB fluctuations consistent with ~27% dark matter | OK, OFF-SPEC | CMB is not in 8463 (see batch-5 RED-SHIFT-BIG-BANG-F4). | — |
| C7 | T1 | candidates WIMPs, axions, sterile neutrinos; not directly detected | OK, OFF-SPEC | — | — |
| C8 | T2 | dark energy: unknown energy causing accelerating expansion | OK | Spec: "what is causing the universe to expand ever faster?" | 4.8 intro |
| C9 | T2 | 1998 distant supernovae showed expansion faster than expected; expected to slow under gravity | OK | Spec: "Since 1998 … receding ever faster". | 4.8.2 |
| C10 | T2 | Type Ia supernovae as standard candles; known luminosity → distance; further than expected | OK (context) | Strictly: fainter than expected for their red-shift, so further away. Fine at GCSE. | — |
| C11 | T2 | "repulsive" energy required | OK | Qualitative. | — |
| C12 | T2 | possibly property of space (cosmological constant, "Einstein's 'biggest blunder'") | IMPRECISE | The "biggest blunder" quote is reported second-hand (Gamow), not from Einstein's writings. Drop the quote. | — |
| C13 | T2 | ~68% | OK (enrichment) | Planck 2018: 68.3%. | — |
| C14 | T3 | ordinary ~5%, dark matter ~27%, dark energy ~68% | OK (enrichment) | Planck 2018: 4.9 / 26.8 / 68.3. Frozen typo "DARM MATTER" (theory, re-cuttable). | — |
| C15 | T3 | fate: Big Rip / expand forever / Big Crunch depending on dark energy | OK (speculative, enrichment) | — | — |
| C16 | T3 | Euclid, Dark Energy Survey, LHC, Fermi searches | OK (enrichment) | Euclid launched 2023. | — |
| C17 | T3 | ~95% unknown; great unsolved problem | OK | Spec: "still much about the universe that is not understood". | 4.8.2 |
| C18 | `higher` | "HT only — describe the evidence … State the approximate proportions" | ROUTE | 4.8.2 has no HT label. The content is the page's TF TH content; the label must not be shown. Proportions are enrichment, not a "state" demand. | 4.8.2 |
| C19 | common_mistake | DM has mass, interacts gravitationally, "doesn't interact with light"; DE causes accelerating expansion; ~95% together; neither detected | IMPRECISE | "Doesn't interact with light" contradicts lensing on the same page. Say: does not emit, absorb or reflect light — but its gravity bends light. Rest OK. | 4.8 intro |
| C20 | key_note | 27% / 68% / 5%; rotation, lensing; 1998 supernovae; unknowns | OK | Numbers are enrichment. Spec's own phrase is "dark mass"; accept either. | 4.8.2 |
| C21 | q1 key | outer stars orbit at similar speeds to inner stars; extra hidden mass | OK | "Similar speeds" — correctly hedged. | 4.8 intro |
| C22 | q1 wx1 → opt 1 "lubricant" | no lubricating effect; purely gravitational | OK, paired | The option's first half ("rotate faster than expected") is true; the lubricant is what is wrong, and wx1 rebuts that. | — |
| C23 | q1 wx2 → opt 2 "dark region visible" | DM emits/absorbs no EM; dark region likely dust lane or black hole | OK, paired | — | — |
| C24 | q1 wx3 → opt 3 "appears darker optically" | invisible to all EM, not just optical | OK, paired | — | — |
| C25 | q2 key | 1998 Type Ia supernovae further than expected → expanding faster now than in the past | OK | Matches 4.8.2. | 4.8.2 |
| C26 | q2 wx1 → opt 1 "Einstein predicted it" | cosmological constant introduced then abandoned; 1998 discovery observational | OK, paired | — | — |
| C27 | q2 wx2 → opt 2 "CMB high-energy regions" | CMB consistent with DE; discovery from supernovae | OK, paired | — | — |
| C28 | q2 wx3 → opt 3 "particle accelerators" | not produced or detected; may not be particles | OK, paired | — | — |
| C29 | matching (to be replaced) | rotation → DM; supernovae → DE; lensing → DM; composition | OK | — | — |
| C30 | header / spec field | "6.8.4 (HT only, physics only)" | ROUTE | No such section; no HT. True: 8463 4.8.2 (physics only). | 4.8.2 |

Count: **0 WRONG**. IMPRECISE: C2, C12, C14 (typo), C19. ROUTE: C18, C30. All `wrong_explanations` paired to their own options (6/6, read by hand).

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| none | q1 and q2 are both correct and not HT | Both usable on TF and TH once the page moves. |

## 5. Verdict
SOURCE OK WITH FLAGS. The science is right and both quiz items are usable. The route label is wrong: this is 8463 4.8.2 (physics only), not HT, so the page belongs on TF TH (moving under the route-flag PR) and the `higher` "HT only" label must not be shown. The spec asks only for the 1998 supernova observation and the fact that dark mass and dark energy are not understood; rotation curves and lensing explain the spec's own intro ("bends light and holds galaxies together"); the percentages, CMB, candidates and fate of the universe are enrichment.

**For Mide:** nothing — settled from the 8463 text.
