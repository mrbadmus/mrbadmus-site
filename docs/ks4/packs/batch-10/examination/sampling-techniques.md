# Examination — Sampling Techniques (sampling-techniques) — AQA 8464 4.7.2.1 (RP7) / 8461 4.7.2.1 (RP9)
Verdict: SOURCE HAS ERRORS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-10/04-checked-science-source/biology-4.7.1-sampling-techniques.md` (the data's "4.7.1" is the site's internal number; AQA's is 4.7.2.1, which is where both specs put quadrats, transects and the RP).
Spec sources read as text: `AQA-8464-spec.txt` (v1.1) 4.7.2.1, RP7 box and 10.2.7; `AQA-8461-spec.txt` (v1.0) 4.7.2.1, RP9 box and 8.2.9. Searched both specs for "capture", "mark", "Lincoln": no hits — mark-release-recapture is not in either spec. No equation sheet applies (biology). Route audit read: `ks4-routes/docs/ks4/route-audit/biology.md` row `sampling-techniques` (OK, CF CH TF TH, 4.7.2.1 RP7 / RP9).

Conventions: q1–q3 = quiz items in file order; "opt n" = option index n (0 = credited); "wx n" = `wrong_explanations` key n; th1–th3 = theory chunks. CF and TF copies differ from TH only in `higher` (`null` = not shown).

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 Combined Trilogy | **4.7.2.1** | Levels of organisation (quadrats, transects, abundance) + **Required practical activity 7** | base |
| 8461 Biology | **4.7.2.1** | Levels of organisation + **Required practical activity 9** | base |
| 8461 Biology | 8.2.9 RP9 AT 8 | "continuous sampling in an investigation" — listed for RP9 only, not in 8464 10.2.7 | triple (apparatus/technique only) |

Spec statements (verbatim, 8464 = 8461): "A range of experimental methods using transects and quadrats are used by ecologists to determine the distribution and abundance of species in an ecosystem." "In relation to abundance of organisms students should be able to: understand the terms mean, mode and median; calculate arithmetic means; plot and draw appropriate graphs selecting appropriate scales for the axes." (MS 2b, 2f, 4a, 4c)

RP (8464 RP7 = 8461 RP9): "measure the population size of a common species in a habitat. Use sampling techniques to investigate the effect of a factor on the distribution of this species." AT 1 "use appropriate apparatus to record length and area"; AT 3 "use transect lines and quadrats to measure distribution of a species"; AT 4 "safe and ethical use of organisms and response to a factor in the environment"; AT 6 "application of appropriate sampling techniques to investigate the distribution and abundance of organisms in an ecosystem via direct use in the field"; 8461 only: AT 8 "use of appropriate techniques in more complex contexts including continuous sampling in an investigation". WS 2.3 "apply a range of techniques, including the use of transects and quadrats, and the measurement of an abiotic factor." MS 1d, 3a "estimates of population size based on sampling"; MS 2d "understand principles of sampling".

## 2. Route table
| # | teachable point | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Why sample; random, representative, enough samples (th1) | base | 4.7.2.1; RP7/RP9 MS 2d | all four | OK |
| R2 | Quadrats: random placement, count, mean, scale up (th2; key_note) | base | 4.7.2.1; RP7/RP9 AT 1, 3, 6; MS 1d, 2b, 3a | all four | OK except throwing (C6) |
| R3 | Transects for distribution; belt/line (th3 first half) | base | 4.7.2.1; AT 3 | all four | OK, one imprecise (C11) |
| R4 | Continuous belt transect | triple (technique) | 8461 8.2.9 AT 8 | all four | not taught; optional TF TH layer |
| R5 | Mark-recapture method, formula, assumptions (th3 second half; equation; variables; FIFA; common_mistake; part of key_note; q2) | **OFF-SPEC** | none | all four | OFF-SPEC (SAMP-F1) |
| R6 | `higher` — mark-recapture assumptions; random number tables/coordinates | random coordinates = base (RP); mark-recapture = off-spec | RP7/RP9 | CH TH only | ROUTE (SAMP-F4) |
| R7 | `rp` "RP6 — …" | base | RP7 (8464) / RP9 (8461) | all four | WRONG number (SAMP-F2) |
| R8 | q1 quadrat scale-up | base | MS 1d, 3a | all four | OK |
| R9 | q3 why random | base | MS 2d | all four | OK |
| R10 | Mean, mode, median; graphs; effect of a factor on distribution; measuring an abiotic factor | base | 4.7.2.1; RP WS 2.1–2.3, MS 2f, 4c | — | GAP (SAMP-F5) |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | th1 | Impossible to count every individual; sample a representative section and estimate | OK | — | MS 2d |
| C2 | th1 | Random to avoid bias; representative; enough samples for a reliable mean | OK | — | MS 2d |
| C3 | th1 | Quadrats for slow/stationary; transects for change across habitat; mark-recapture for mobile | OFF-SPEC (part) | Third technique is not in either spec. | 4.7.2.1 |
| C4 | th2 | 0.5 m × 0.5 m = 0.25 m²; 1 m × 1 m | OK | ✓ | AT 1 |
| C5 | th2 | Estimated population = mean per quadrat × (habitat area ÷ quadrat area) | OK | Standard and examined (MS 1d, 3a). | RP7/RP9 |
| C6 | th2 | "use random number tables or throw the quadrat over your shoulder" | **WRONG** | Throwing is not random (the thrower chooses where to stand and aim) and is unsafe; AQA mark schemes credit random coordinates (random number generator/table) on a grid set out with two tape measures. Cut "throw". | MS 2d; AT 4 |
| C7 | th2 | Quadrats best for plants, mosses, lichens, limpets, snails, woodlice; not fast-movers | OK | — | — |
| C8 | th2 | "Count or estimate the abundance" | OK | Percentage cover is a valid alternative for plants that cannot be counted; worth a line. | AT 6 |
| C9 | th3 | Transect line; organisms recorded at regular intervals; shows change in distribution | OK | — | AT 3 |
| C10 | th3 | Line transect records which species touch the line | OK | — | — |
| C11 | th3 | "BELT TRANSECT … quadrats placed at regular intervals" | IMPRECISE | That is an interrupted belt transect; a continuous belt transect places quadrats end to end along the line (8461 AT 8 "continuous sampling"). | 8461 8.2.9 |
| C12 | th3 | Mark-recapture method, N = (n₁ × n₂) ÷ m, four assumptions | OFF-SPEC | Science is correct (Lincoln index), but it is not in 8464 or 8461 at any tier. | — |
| C13 | equation; variables | N = (n₁ × n₂) ÷ m; units "individuals" | OFF-SPEC | Correct, off-spec. | — |
| C14 | FIFA | 40 marked, 30 caught, 6 marked → N = 1200 ÷ 6 = 200 | OFF-SPEC (arithmetic OK) | 40 × 30 = 1200 ✓; ÷ 6 = 200 ✓. Do not use as the lesson's worked example. | — |
| C15 | CFIFA Convert (NEW) | "Nothing to convert — n₁, n₂ and m are already plain counts of individuals in matching units." | OK as a line | True for that example; the example itself is off-spec (SAMP-F1). The lesson's real worked examples are quadrat scale-ups; the conversion case is cm → m for a quadrat side (50 cm → 0.5 m, area 0.25 m²). | CFIFA amendment |
| C16 | rp | "RP6 — Use quadrats or transects to estimate population size or distribution …" | **WRONG** (number) / GAP (text) | Combined RP7 (8464 4.7.2.1, 10.2.7); Biology RP9 (8461 4.7.2.1, 8.2.9). RP6 is reaction time (8464) / photosynthesis (8461). Text omits "investigate the effect of a factor on the distribution" and measuring an abiotic factor. | RP7/RP9 |
| C17 | `higher` | Mark-recapture assumptions; random number tables/coordinates for random placement | ROUTE / OFF-SPEC | Random coordinates are base RP method; mark-recapture is off-spec. No HT content exists in 4.7.2.1. | RP7/RP9 |
| C18 | common_mistake | n₁, n₂, m mix-ups | OFF-SPEC | Correct, off-spec. | — |
| C19 | key_note | Quadrats; transects; mark-recapture; assumptions | OFF-SPEC (part) | Keep the first two sentences. | 4.7.2.1 |
| C20 | q1 key | 10 × 1 m² quadrats, field 500 m², mean 4 → 4 × 500 = 2000 | OK | 500 ÷ 1 = 500 quadrat areas; 4 × 500 = 2000 ✓ | MS 1d, 3a |
| C21 | q1 opt1 / wx1 | 40 = mean × number of quadrats = total counted | OK | 4 × 10 = 40 ✓; wx1 explains opt1 ✓ | — |
| C22 | q1 opt2 / wx2 | 500 = field area | OK | wx2 explains opt2 ✓ | — |
| C23 | q1 opt3 / wx3 | 50 = area ÷ number of quadrats | OK | 500 ÷ 10 = 50 ✓; wx3 explains opt3 ✓ | — |
| C24 | q2 | Mark-recapture 25, 20, 5 → 100 | OFF-SPEC | Arithmetic ✓ (500 ÷ 5 = 100). Also: opt3 "1 — N = 5 ÷ (25 × 20)" — 5 ÷ 500 = 0.01, not 1; wx1 says "not by n₂" but opt1 divides by 2, not by n₂ (20). Alignment: wx1→opt1, wx2→opt2, wx3→opt3 ✓. | — |
| C25 | q3 key | Random placement avoids sampling bias; choosing dense areas would overestimate | OK | — | MS 2d |
| C26 | q3 wx1–wx3 | size fixed by frame; disturbance not the reason; not a legal requirement | OK | Each key explains its own option ✓ | — |
| C27 | matching (to be replaced) | Quadrats/transect/mark-recapture pairs | OK (mark-recapture pair off-spec) | — | — |

Count: **2 WRONG** (C6 theory, C16 rp number); **OFF-SPEC**: mark-recapture throughout incl. equation, FIFA, q2; **IMPRECISE**: C11, C24. wrong_explanations: all three items aligned (key n explains option n).

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| q2, FIFA, equation, variables, common_mistake | Mark-recapture is in neither spec | Do not use as written on any route (SAMP-F1). Replace the worked example with a quadrat scale-up. |
| rp | Wrong RP number | Do not use the "RP6" label (SAMP-F2). |
| `higher` | Not HT; served only CH TH | Teach random coordinates on all routes (SAMP-F4). |
| q1, q3 | — | Usable on all four routes. |

## 5. Verdict
SOURCE HAS ERRORS. Quadrat and transect science is sound and q1/q3 are good; but the lesson's only equation, worked example and one of three quiz items are off-spec mark-recapture, the RP is mislabelled RP6 (it is Combined RP7 / Biology RP9), "throw the quadrat over your shoulder" is not random, and the spec's mean/mode/median, graphing and "effect of a factor on distribution" (with an abiotic measurement) are missing. Nothing for Mide: the spec is unambiguous that only quadrats and transects are named.
