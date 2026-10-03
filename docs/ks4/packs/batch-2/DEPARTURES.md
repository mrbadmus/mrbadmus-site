# DEPARTURES — KS4 Batch 2 (16 Code-authored lessons)

Batch 2 has no Design original: Code wrote every lesson from the AQA spec, the
examination files and the review rounds, so there is no Design-vs-built diff
to register. A "departure" here is instead any of three things: (1) a frozen
quiz item (verbatim source data) withheld from the page because the
examination found it wrong, ambiguous or wrong for its route; (2) a frozen
source field — an `rp` practical number, a key-note line, a theory
paragraph — that is not shown on the page because it is wrong, imprecise or
out of its spec; (3) a change the two review rounds (science examiner +
quality reviewer, both fresh Opus readers, 1 Oct 2026) required to what was
first authored, plus the handful of advisories the commander or the author
applied anyway because they touched what a pupil is told. The frozen Python
data itself (`ks4_lessons/batch_2.py`, `shared/ks4-source-batch-2.js`) is
never edited for any of this — withholding happens at the serving layer
(`K.bank`/`K.find` plus `batch_2.py`'s `withhold` list), and every
pupil-facing fix is a change to the lesson's own authored template or logic,
not to the frozen record.

Sources: `ks4_lessons/batch_2.py`; `docs/ks4/packs/batch-2/review/science-*.md`
and `quality-*.md` (both rounds); `docs/ks4/packs/batch-2/notes/<slug>.md`
("Review fixes" tables); `docs/ks4/packs/batch-2/examination/<slug>.md`.

---

## 1. Withheld frozen quiz items — 10 rows

⊕ 2 Oct 2026: Mide approved correcting these items in the frozen `all_subtopics_*.py` data itself — a logged exception to the frozen window, for these rows only. Every row below is now **corrected in frozen data, feat/ks4-frozen-corrections, served again**; the `withhold` entries are gone from `ks4_lessons/batch_2.py`. Before/after text, routes and spec references: `docs/ks4/FROZEN-CORRECTIONS.md`.

Every row is a `withhold` entry in `ks4_lessons/batch_2.py` (dep ids
B2-W1…B2-W10). The item stays verbatim in the practice bank's source data on
every route it would otherwise serve; `K.bank`/`K.find` never return it as a
rung, in the body, or (where "routes" is given) on the named routes at all.

| id | lesson | routes | the question | why | citation | status |
|---|---|---|---|---|---|---|
| B2-W1 | enzymes | all | "An enzyme is heated to 80°C" | wx1 claims the rate *increases* above the optimum temperature — false | 4.2.2.1 | corrected in frozen data, feat/ks4-frozen-corrections, served again |
| B2-W2 | atoms-elements-compounds | all | "A student heats a mixture of iron filings" | wx3 states sulfur stays solid when heated with iron — false (sulfur melts ~115 °C) | C25; 4.1.1.1 | corrected in frozen data, feat/ks4-frozen-corrections, served again |
| B2-W3 | atoms-elements-compounds | all | "Which equation is correctly balanced?" | has two correct answers (H₂+O₂→H₂O₂ also balances); AQA would credit both | C26; 4.3.1.1 | corrected in frozen data, feat/ks4-frozen-corrections, served again |
| B2-W4 | using-moles-calculations | CH only | "What is the concentration of a solution made by dissolving 0.3 mol" | mol/dm³ is 8462 4.3.4, chemistry-only + HT; never taught or examined on Combined Higher | C18; 4.3.4 | corrected in frozen data, feat/ks4-frozen-corrections, served again |
| B2-W5 | concentration-of-solutions | all | "A solution has a concentration of 80 g/dm³" | distractor 3's own working gives 2000 not 320; wx2 teaches a false relationship ("dividing gives volume") | C25, C26; 4.3.2.5 | corrected in frozen data, feat/ks4-frozen-corrections, served again |
| B2-W6 | decomposition | CF, CH | "Why does food last longer in a refrigerator" | tests 8461 4.7.2.3 (biology only); not examinable on Combined | C21; 4.7.2.3 | corrected in frozen data, feat/ks4-frozen-corrections, served again |
| B2-W7 | relative-formula-mass | all | "What is the Mr of Mg(NO₃)₂?" | wx1 contradicts itself on screen ("1 N, NOT 2 — wait:") | C23; 4.3.1.2 | corrected in frozen data, feat/ks4-frozen-corrections, served again |
| B2-W8 | percentage-yield | TF, TH | "A reaction has a theoretical yield of 20 g" | distractor 1, "43% — (14÷20)×3=42%", contradicts its own working | C21; 4.3.3.1 | corrected in frozen data, feat/ks4-frozen-corrections, served again |
| B2-W9 | carbonates-halides-sulfates | TF, TH | "Why must solutions be acidified with nitric acid" | keyed answer and wx1 both say nitric acid removes **sulfate** ions — false; the real reason is carbonate | C24, C25; 4.8.3.4 | corrected in frozen data, feat/ks4-frozen-corrections, served again |
| B2-W10 | changes-in-energy | all | "An 800 kg car travels at 20 m/s" | the "16,000 J" distractor's label/wx3 misdiagnose the error as "used speed not squared"; wx1 reads as an instruction | C21, C23, C24; 6.1.1.2 | corrected in frozen data, feat/ks4-frozen-corrections, served again |

---

## 2. Frozen source text not shown on the page — 32 rows

Wrong `rp` practical numbers, key-note lines replaced or dropped, and theory
paragraphs the examination marked WRONG or route-wrong that are deliberately
not displayed (ordinary not-in-spec scope cuts — e.g. peptidoglycan, the
aluminate equation, molecular formula as a term — are not listed here; this
table is content that could mislead if it had been shown, not ordinary
scoping).

| lesson | field | what | why |
|---|---|---|---|
| chromosomes-mitosis | theory 3 | "not needed for Foundation GCSE" (phase names) | NOT-IN-SPEC; legal line says GCSE never asks for the phase names |
| chromosomes-mitosis | common_mistake | "…not required at Foundation" | WRONG (C17); meiosis is re-cut as "on both tiers" |
| enzymes | `rp` | "RP3 (Physics) — …" | WRONG number; RP block written fresh (RP4 Combined / RP5 Biology) |
| enzymes | theory 4 | charges/hydrogen-bonds paragraph | NOT-IN-SPEC (C9); cut |
| carbon-cycle | `higher` | human-impact content tagged Higher-only | WRONG ROUTE; taught as base to all four routes instead |
| using-moles-calculations | th3 heading | "Using Moles to Balance Equations" over empirical/molecular formula | WRONG (C7); 4.3.2.3 taught fresh via worked examples instead |
| using-moles-calculations | `higher`/th1 | molecular formula; the titration mol/dm³ calculation | NOT-IN-SPEC (R6) / wrong home (R1/R2); cut / left to `titrations` |
| concentration-of-solutions | th1 | g/cm³ unit; "at Foundation level" | NOT-IN-SPEC (R7/C2); not taught |
| concentration-of-solutions | th3, key_note | c₁V₁=c₂V₂; serial dilution | NOT-IN-SPEC (R5/R6); cut from both the key note and the body |
| concentration-of-solutions | `higher` | "mol/dm³ is the standard unit in Higher-level calculations" | WRONG for CH (C12); not shown |
| metal-hydroxides | `rp` | "RP Chemistry 4" | WRONG number (C23); "Required practical 7" shown instead |
| metal-hydroxides | th3 | copper flame-test parenthetical | WRONG (C14); not used |
| metal-hydroxides | `higher` | "identify both cation and anion" | WRONG (C17); not used — combining tests taught as base instead |
| metal-hydroxides | key_note | sentence 2 (ammonium); sentence 3 ("Aluminium unique: amphoteric") | NOT-IN-SPEC, cut / WRONG, replaced with spec wording (C21) |
| changes-in-energy | theory 3 | "Only valid within the ELASTIC LIMIT" | WRONG (C10); page says "limit of proportionality" |
| changes-in-energy | theory 2 | "heavier objects store more GPE" | WRONG (C7); page says "mass" |
| internal-energy | theory 2 | "THERMAL ENERGY" paragraph | borderline WRONG (C9); not displayed |
| internal-energy | theory 1/3 | "bonds" wording for forces between particles | WRONG family (C3/C4/C12); re-cut as "forces between particles" throughout |
| lenses | `equations[1]` | "image distance ÷ object distance" as a second equality | NOT-IN-SPEC; kept in the frozen data, never displayed |
| lenses | `variables` | focal length given in metres | imprecise (C13); page uses cm throughout, as AQA questions do |
| lenses | `higher` | "magnification from image and object distances" | WRONG TAG (R3/C20); ray diagrams taught at base Triple instead, this line never taught |
| eukaryotes-prokaryotes | theory | "Larger eukaryotic cells… need… lungs" | WRONG (C15); belongs to 4.1.3.1 diffusion, not taught here |
| decomposition | `rp` | "RP7 — bread… mould… respirometers" | WRONG number, method and route (C21); RP10 (milk/lipase/pH) written fresh |
| decomposition | key_note lines 3–5 | detritivores; "higher temperature… neutral pH"; uses | NOT-IN-SPEC/IMPRECISE (C17); authored lines used instead |
| relative-formula-mass | `higher` | empirical and molecular formula | NOT-IN-SPEC (R6/R7); empirical belongs to `using-moles-calculations` |
| relative-formula-mass | `higher` | carbon-12 as the relative-mass standard | NOT-IN-SPEC (R8); not taught |
| percentage-yield | th3 | "catalyst" advice (implies a catalyst raises yield) | WRONG (C11); the page teaches the opposite at three points |
| percentage-yield | th2 | "100%… impossible in practice" | WRONG framing (C8); page says a pure, dry product can never be *more* than 100% |
| percentage-yield | key_note | "Always less than 100%" / "impurities" | re-cut to "Usually less than 100%" / dropped; flagged for examiner confirmation (see §5) |
| titrations | th1 / th2 | "at Foundation level"; "reliability" | WRONG framing (C2/C12); neither reproduced |
| carbonates-halides-sulfates | th1 | sulfite paragraph and its distinguishing method | NOT-IN-SPEC / WRONG (C4/C5); cut |
| carbonates-halides-sulfates | `rp`, `equations[0]` | "RP Chemistry 4"; "acid + CO₃²⁻ → CO₂…" | WRONG number (C22) / IMPRECISE, not balanced (C20); "Required practical 7" shown; balanced Na₂CO₃+2HCl shown instead |

---

## 3. Changed after review, by lesson

Required rows from both review rounds (`S-n` = science examiner, `Q-n`/`A-n`
= quality reviewer; `Q2-n`/`A2-n`/`R2-n` = round 2), plus applied advisories
that changed science or pupil-facing wording. Pure layout/cosmetic advisories
are omitted. "Old → new" is short; full text is in the review files and the
lesson's notes file.

### chromosomes-mitosis
| id | where | old → new | reason |
|---|---|---|---|
| S-1 | `s-order` chain prompt | "…does not happen in **mitosis**." → "…does not happen in **the cell cycle**." | the chain is the whole cell cycle, not just mitosis |
| Q-CM1 | `cancerReveal` | full benign/malignant sentence (repeats the explainer) → "Mitosis is normal; losing control of it is the disease." | third telling on one screen |
| Q-CM2 | stage-1 Q2 options | `'8 chromosomes'` / `'4…, each now two copies'` / `'2 chromosomes'` → all three state "each … copy/copies" | key was the only long option (length-parity tell) |
| Q-CM3 | `cellFig` stages 1–3 | in-figure title line → deleted, figcaption kept | state captioned twice plus the verdict text |
| A-2 | explainer 2 | "mitosis never makes gametes" → "**In animals**, mitosis never makes gametes" | avoids an over-general claim (plant gametes) |
| A-CM2 | meiosis box | "You meet it in Inheritance, on both tiers." → cut | told the pupil nothing they needed now |

### eukaryotes-prokaryotes
| id | where | old → new | reason |
|---|---|---|---|
| S-2 | every "cheek cell" reference (bigq, hook, figure label/alt, hook option, Foundation CFIFA Q1) | "cheek cell" → "liver cell", every number unchanged | real cheek cells are 50–80 µm, not 20 µm; liver cells fit the 20 µm figure |
| Q-EP1 | `hookReveal` + first explainer | gave the nucleus/DNA-loop/plasmid answers away → trimmed to the one-line scenario | builder items 1, 4, 5 were answered before the builder asked |
| Q-EP2 | `hookOptions[0,1].reply` | "Hold that thought…" → `''` | the reveal answers it immediately after |
| Q-EP3 | hook paragraph | kept both cell sizes in prose → cut to one sentence | sizes are already in the figure below |
| Q-EP4 | `fitFig` k=1,2 | illegible at 390 px → rebuilt on a 640 plate, labels 26–28 px, magnified 5-unit inset | figures unreadable on a phone |
| Q-EP5 | `fText` comparison 1 | "convert, then divide" (false for case 1) → "×10: both already in µm, so just divide." | nothing to convert in comparison 1 |
| Q-EP6 | `#s-scale` eyebrow | "Estimate · how many fit across? · {{fName}}" → "Estimate · {{fName}}" | repeats the commit prompt below |
| Q2-EP1 | `FIT[1].why[0]` | gave the working ("2000÷20=100") → trimmed, working line below already shows it | third telling |
| Q2-EP2 | `fitFig` k=0 caption | "10 bacteria fit across" → deleted | verdict and working already say "×10"/"=10" |
| A-EP3 | Triple explainer | "every 20 minutes" fact → deleted from this lesson | belongs to `culturing-microorganisms` (8461 4.1.1.6) |

### enzymes
| id | where | old → new | reason |
|---|---|---|---|
| S-3 | logic `TRUE_T[6]` | `75` → `60` | the simulated data could put the apparent optimum at pH 7, contradicting the page's own "fastest near pH 6" verdict |
| Q-EN1 | `thinkReveal` last sentence | cold-slows-not-denatures sentence → deleted | third telling (bench reply + curve text already say it) |
| Q-EN2 | `keyLines` appended line | active-site-shape sentence → deleted | repeats the source key-note line directly above |
| Q-EN3 | `hookOptions[0].reply` | "Hold that…" → `''` | reveal names amylase immediately below |
| A-EN2 | `plot()` curve | joined pH 4 (unmeasured, rate 0) → curve now joins only measured means, pH 4 a hollow marker | an examiner would not join an unmeasured point |

### carbon-cycle
| id | where | old → new | reason |
|---|---|---|---|
| S-4 | `s-sort` done-note | "Only photosynthesis takes CO₂ out of the air…" → "**Of these processes**, only photosynthesis…" | false as a general claim (oceans also absorb CO₂); contradicts the page's own key note |
| Q-C1 (Q-X1) | header | static "Combined·Triple"/"Foundation·Higher" pills → route-chip disclosure | one-route URL showing all four routes is uninformative |
| Q-C2 | `tReplyText` | shown on every commit → shown only on a wrong pick | right answer repeated the reveal back to back |
| Q-C3 | rung-2 Y options | `'Photosynthesis'`/`'Respiration…'`/`'Combustion'`/`'Fossilisation'` → each lengthened to match | key was the only three-word option |
| Q-C4 | `keyLines` | source key note (decomposition/ocean/volcano lines) → 5 authored lines | re-taught the exact error the lesson confronts; contradicted the lesson's own scope note |

### decomposition
| id | where | old → new | reason |
|---|---|---|---|
| Q-D1 (Q-X2) | hook (h2, paragraph, options, reveal) | same phenomenon/question as carbon-cycle's hook, and pre-answered stepper step 1 → new hook, a compost heap over 50 °C on a frosty morning, reveal states only respiration-releases-heat | two lessons taught back to back with an identical hook; the carbon answer told three times |
| Q-D2 | — | Combined routes had one instrument (stepper) and no mid-size activity → added base `s-return` sort, "Air, soil, or locked away?" | instrument budget requires at least one mid-size activity |
| Q-D3 | `rateLabel` | gave the Insert line in the label → "Calculate the rate at 40 °C from your time." | value then shown three times (label, rateText, table) |
| Q-D4 | `rateText` (wrong) | "…about 0.007" → "…the unit is s⁻¹." | "about 0.007" is the answer for most pupils' actual time |
| Q-D5 | `s-sim` caption | "Your times for the pink to go, in seconds." → deleted | table header already says this |
| A2-D1 | `s-return` prompt/cards | "Each one comes from something that died" (false of the living fungus) → "Each one starts in a living thing."; added a second "locked away" carbon card | kept the sort from being solved by a carbon→air shortcut |
| (commander, post-R2) | hook reply | "Frozen ground is colder…" → "The ground under the heap is colder than its middle…" | R2-A1: the stem only said the air was below 0 °C, not the ground |
| (commander, post-R2) | explainer after the hook | "every atom in the leaf… Follow one leaf" → "every atom in a dead leaf… Follow one fallen leaf" | R2-A2: the hook no longer opens on a leaf, so "the leaf" had nothing to refer to |

### changes-in-energy
| id | where | old → new | reason |
|---|---|---|---|
| S-1 | `batch_2.py` | frozen q1 served, undetected error → withheld (B2-W10) | mislabelled distractor/wx (see §1) |
| S-2 | `rungs.r4.points[5]` | "…by air resistance, **so** the total stays the same." → "…by air resistance. The total energy stays the same." | false causal link; energy is conserved regardless of dissipation |
| Q-CE1 (Q-X1) | header | static pills → route chip | as carbon-cycle Q-C1 |
| Q-CE2 | first explainer | stated which quantity is squared → deleted | bench rounds 2–3 ask exactly this; answered in advance |
| Q-CE4 | `ROUNDS[0,1].ask` | "The height/extension doubles. What happens to…" → "What happens to the energy in the … store?" | h2 above already says "twice as high/far" |
| A-3 | r4 point 4 | "The cord slows her down…" → "Once the cord pulls up harder than her weight, she slows down…" | more precise sequence |
| A-CE3 | Foundation convert example | Insert line listed values → `Ee = ½ × 40 × 0.15²` | lists instead of substitutes |

Q-CE3 ("Equation sheet" → "Learn it" on Ek/Ep) was **withdrawn by commander
ruling** after round 1 — see §5.

### internal-energy
| id | where | old → new | reason |
|---|---|---|---|
| S-3 / Q-IE3 | `thinkOptions[0].text` (keyed) | "average energy of one particle…every particle's…energy" → "average **kinetic** energy of the particles…kinetic **and potential** energy of every particle" | blurred temperature (average KE) with internal energy (total KE+PE); also fixed a length-parity tell |
| S-4 | `rungs.r4.reject[0]` | "…it does not break them." → "Melting overcomes the forces between the molecules; the molecules themselves do not break." | for ice→water specifically, molecules move closer, not apart, on melting |
| S-5 | `STAGES`/`HEAT_PTS`/notes | ice warmed 4× shallower than water (wrong way round) → ice line redrawn twice as steep as water's (2:1, matching c_water≈2c_ice) | gradient-vs-SHC is standard Higher content; the curve was backwards |
| Q-IE2 | second explainer | "a large object at low temperature can hold more internal energy…" → deleted | the very next block asks the pupil to spot this exact flaw |
| A-IE2 | hook reveal | fully answered bench stage 4 (boiling) → trimmed to "It stays at 100 °C…" | pre-answered the bench |
| A-7 / A-IE1 | header | no equation-sheet link → added | explainer cites two sheet equations |

### lenses
| id | where | old → new | reason |
|---|---|---|---|
| S-6 | Higher CFIFA convert note | "…a diminished image, which a magnifying glass never makes." → "…but the wing looks bigger through the glass, not smaller." | false: a convex lens does form diminished images (the hook and the 30 cm bench set-up both show it) |
| Q-L1 (Q-X1) | header | static "Triple·physics only"/"Foundation·Higher" pills → route chip | as carbon-cycle Q-C1 |
| Q-L2 / Q2-L1 / Q2-L2 | `#s-build` | 4-option text MCQ (recognition) → tap targets on the diagram itself; targets reordered by position with purely positional labels; rings shrunk/unfilled below 480 px | "Complete the ray diagram" must be production, not recognition; the fix's own key-was-always-first and overlapping-rings defects then fixed in round 2 |
| Q-L3 | `WHY` lines | repeated real/virtual, upright/inverted, magnified/diminished → trimmed | verdict lines above already state them |
| Q-L4 | `posLabel` | "Object N cm from the lens · F is 10 cm" → "Object distance · F is 10 cm" (full text kept in `aria-valuetext`) | h2 already states the distance |
| A-L1 | verdict style | unasked verdicts rendered in alert style → neutral style | a "No image" prediction still showed Size/Way-up as if wrong |
| A-8, A-9 | explainer 1; eye distractor reply | loosely worded → tightened to name the convex-bends-through-F mechanism and the ciliary-muscle mechanism | precision |

### atoms-elements-compounds
| id | where | old → new | reason |
|---|---|---|---|
| S-1 | key fact | "one kind of particle = element…" (false for giant structures) → "an element has only one type of atom…a compound has atoms of two or more elements chemically combined…a mixture has two or more substances not chemically combined" | the page's own FeS/MgO/NaCl boxes are compounds with two kinds of atom, contradicting the old rule |
| S-2 (R2) | `#s-sort` done-note | "...anything not chemically combined is a mixture" → "...two or more substances not chemically combined with each other is a mixture" | a single element (Cu, graphite, O₂ — all in this sort) is not chemically combined with anything and is not a mixture |
| Q-1 | `#s-zoom` eyebrow | "Zoom in · {{zoomStep}}" → "Zoom in" | box number shown three times on one screen |
| Q-2 | `#s-balance` | `balLine` paragraph → deleted | reprints the stepper row above |
| Q-3 | `#s-sort` items | every mixture card was the only one with no formula → "Salt water, NaCl in H₂O" / "Graphite" / "Rust (iron oxide)" cards added, mixing formula and no-formula cards in every bin | sort solvable by label shape, not science |
| Q-4 | rung 1 | `K.find(…'key difference between a compound and a mixture')` → `K.find(…'Which of these is a mixture')`, same fallback | correct option was 1.4× the longest distractor (length-parity fail) |
| Q-5 | `#s-sort` done-note | shouty verbatim `common_mistake` → authored house-style text | capitals, and it re-explains electrolysis, which this lesson never teaches |
| Q-6 | header | no route chip at all → route chip + `specCode` (8462/8464) in the eyebrow | every other pilot/batch page shows its route |
| (commander, post-R2) | eyebrow | "AQA Chemistry (8464)" on Combined → "AQA Combined Science (8464)" | A-12/R2-A1: 8464 is a Combined Science spec, not a Chemistry one |

### relative-formula-mass
| id | where | old → new | reason |
|---|---|---|---|
| Q-1 | `#s-unpack`/`#s-pans` eyebrows | "…· {{upStep}}"/"…· {{panStep}}" → counters deleted | repeated the progress line beside them |
| Q-2 | confront panel | verbatim `common_mistake` 4th paragraph → deleted | panel's three beats already cover it; the verbatim text restated it in capitals |
| Q-3 | key fact | repeated the equation card and the MgO worked example → "A number after a bracket multiplies everything inside it: Mg(OH)₂ is one Mg, two O and two H, Mᵣ = 58. Mᵣ has no units." | the lesson's own misconception (brackets) appeared nowhere in a summary block |
| Q-4 | header | no route chip → added, with `specCode` | route honesty |
| (commander, post-R2) | eyebrow | "AQA Chemistry (8464)" on Combined → "AQA Combined Science (8464)" | same as atoms-elements-compounds |

### using-moles-calculations
| id | where | old → new | reason |
|---|---|---|---|
| Q-1 | `<title>`/`<h1>`/chrome/key-note titles | Title Case → sentence case | pilot and the lesson record both use sentence case |
| Q-2 | `#s-bench` `loadLine` | repeated both stepper values on "Your mix" → `''` | steppers already show both amounts |
| science A-7 | CH eyebrow | "AQA Chemistry (8464)" → "AQA Combined Science (8464)" | 8464 is Combined Science, not Chemistry |
| science A-8 | r1 command | "State" → "Give" | "State" is not an AQA command word |

### concentration-of-solutions
| id | where | old → new | reason |
|---|---|---|---|
| Q-1 | titles | Title Case → sentence case | as using-moles Q-1 |
| Q-2 | `#s-bench` `madeLines` | current solution shown in both the verdict and the log → log excludes the solution just made | same result shown twice |
| Q-3 | Higher r3 | 2-mark chip on a 3-link chain, easier than Foundation's → 3 marks, "6.0 g/150 cm³ vs 10 g/250 cm³, both 40 g/dm³" | tariff/demand mismatch, and Higher was easier than Foundation |
| science A-9 | CF/CH eyebrow | "AQA Chemistry (8464)" → "AQA Combined Science (8464)" | as above |
| science A-10 | r4 marking points | "volumetric flask" required outright → "…(or another container where the volume can be measured)" | the point as written withheld a mark a Combined pupil could otherwise earn |
| science A-11 | r1 command | "State" → "Give" | as using-moles |

### percentage-yield
| id | where | old → new | reason |
|---|---|---|---|
| S-1 | `rungs.r4.points[2,3]` | reasons fixed to specific marks → "First reason, any one of: …" / "Second reason: a different one of those three." | AQA credits any two of the three spec reasons; the original tied each mark to one fixed reason |
| Q-1 | `#s-bench` `benchDone` | 6.2 g repeated a 4th time → "Theoretical yield 8.0 g · actual yield 6.2 g. Nothing was destroyed." | redundant |
| Q-2 | `keyBase` | "Chemistry-only spec point." → deleted | route chip/eyebrow/key-note spec line already say it |
| Q-3 | rung 1 | frozen `K.find` item (20 vs 11 words) → authored "Give" MCQ at parity | length-parity fail |
| Q-4 | `cfQuestions` | identical TF/TH write-it-out questions → TH gets rearrangement questions (72% of 45 g; 85% of 2.40 kg) | same examples on F and H is a defect |
| Q-5 | header | hard-coded "Triple"/"Foundation·Higher" pills → route chip | one-route URL |
| A-1 | sort done-note | "…never how much." → "…never the maximum mass of product." | a faster rate can raise actual yield if a reaction is stopped early |
| A-2 | Higher worked answer | "83.3%" → "83.3% (83%)" | data are 2 s.f. |

### titrations
| id | where | old → new | reason |
|---|---|---|---|
| S-1 / Q-1 | `#s-bench` `judge()`/`onRecord` (logic bug) | an overshot rough-run-derived accurate run could be accepted as "Concordant" → rows flagged `over`, `judge()` refuses any choice containing one, "Repeat the rough run" added | rewarded a wrong mean as concordant, teaching the opposite of the RP's point |
| Q-2 | rung 1 | frozen `K.find` item (17 vs 10 words) → authored "Give" MCQ at parity | length-parity fail |
| Q-3 | `cfQuestions` | identical TF/TH questions → TH gets a rough-run-plus-anomaly set to 2 d.p. | same examples on F and H |
| Q-4 | after `#s-bench` | no mid-size activity → added `#s-errors` sort, "Titre too large, too small, or no effect?" (7 cards) | instrument budget requires one |
| Q-5 | header | pills → route chip, RP pill "Required practical · titration" | route/RP-label redundancy |
| (commander, post-R2) | `#s-errors` card why | "the top reads lower" (ambiguous) → "the top of the meniscus sits at a smaller number" | chem-b A-9: could be read as "lower down the tube", the opposite of what's meant |

### metal-hydroxides
| id | where | old → new | reason |
|---|---|---|---|
| Q-1 | header | "Triple"/"Foundation·Higher"/"Contains Higher" pills → route chip + "Required practical · identifying ions" | redundant with the Higher inline badges already on each block |
| science A-5 | key-note line 1 | "Fe³⁺ = brown/rust" → "Fe³⁺ = brown" | models the exam answer; the page's own FACT table already says "in the exam, write brown" |

### carbonates-halides-sulfates
| id | where | old → new | reason |
|---|---|---|---|
| Q-1 | header | pills → route chip + "Required practical · identifying ions" | as metal-hydroxides |
| Q-2 | rung 4 | command "Plan", question worded "Describe" → question reworded "Plan tests that would identify each solid. Give the result each one would show." | command chip and question text disagreed |
| Q-3 | `#s-rack` log | last test's result shown 3×  → log shows only earlier results | redundant |
| science A-8 | key-note line 4 | "…remove interfering ions." → "…remove carbonate ions." | names the specific, creditworthy reason |

---

## 3a. Shared-block engine fixes (Mide's approval, 2 Oct 2026)

Every page of this batch (16 lessons, all routes) changes because two shared blocks compiled into every KS4 page were fixed — see `ks4_rulings.py` R16/R17 and `docs/ks4/design-reference/pilot/DEPARTURES-PILOT.md` ("Shared blocks — ladder number parse and sort completion"). Science content, lesson logic and freeze hashes are unchanged.

- **R16 (Ks4Ladder Apply rung):** a typed number with space or comma thousands separators ("63 000", "63,000") is now read as 63000, not 63; a single decimal comma ("6,3") still reads 6.3.
- **R17 (Ks4Sort):** the block now reports completion when the sort is checked, so the lesson's rail stop ticks. Lessons in this batch that use Ks4Sort: chromosomes-mitosis, enzymes, carbon-cycle, atoms-elements-compounds, using-moles-calculations, concentration-of-solutions, changes-in-energy, internal-energy, lenses, decomposition, percentage-yield, titrations, carbonates-halides-sulfates.

---

## 4. Considered, not changed

**Q-CE3 (changes-in-energy), overruled by the commander.** The quality
reviewer's round-1 row asked for Ek/Ep's "Equation sheet" chip to read
"Learn it", since AQA's Appendix A lists them as recall equations. The
commander overruled this after both June 2026 equation sheets were checked
and found to print Ek, Ep *and* Ee unmarked, under the same precedent as the
pilot's `resistors-C9` (V = I R, also a recall equation, carries the chip
because the 2026 sheet prints it). The chip stays on all three cards; the
CFIFA "as on the equation sheet" placeholder stays too; `KS4.EQ_YEAR` is the
switch for when AQA stops publishing the full sheet.

**decomposition q1 (detritivores), kept in the bank.** Both reviewers flagged
it (quality A-D2/A-12): it is the only CF/CH bank item, it is correct
science, and detritivores appear in neither spec. The batch's own precedent
(enzymes q4: correct-but-not-a-named-factor, kept) argues for keeping it; the
commander ruled to keep it rather than withhold it, closing the question for
this run.

**using-moles-calculations q2, "0.1 mol Na with 0.05 mol Cl₂ → Neither",
kept in the bank.** The science reviewer flagged this as advisory (A-5): the
stoichiometric "neither is limiting" case sits in tension with the page's own
"completely used up" definition, and the reviewer recommended withholding it
on CH/TH. The commander ruled to keep it in the bank (not a rung on either
route) rather than mint a new withhold row.

**using-moles-calculations and concentration-of-solutions sharing a block
line-up, accepted.** Quality A-2 (both lessons) noted the two lessons share
nearly the same shape (hook → explainer → predict-then-animate bench →
Ks4Sort → think → route-tagged Choice → equation → CFIFA → authored r1 MCQ).
The commander accepted this rather than requiring a different mid-size
activity in either lesson — the content differs even though the shape does
not, and varying the shape is a design change outside the review's scope.

**Required rows an author declined, left for a later pass (not re-opened by
round 2):**
- *percentage-yield A-1/A-3 (binary bench commit; moving `#s-which` after the
  worked example)* — both are structural changes to the flagship's flow, not
  cheap text fixes.
- *metal-hydroxides A-2 / carbonates-halides-sulfates A-3* — the two
  "analysis" lessons' r2/r4 ladder rungs are near-clones of each other
  (same shape, different salts); varying one is a design change, not a
  required fix.
- *concentration-of-solutions A-1 (fold "Give the unit" into "Calculate")* —
  cosmetic, left as advisory.

---

Row counts: §1 (withheld quiz items) **10**; §2 (frozen source text not
shown) **32**; §3 (changed after review) **16 lessons**, 83 rows in all
(S-/Q-/A- ids, both rounds, plus 4 commander edits applied after round 2);
§4 (considered, not changed) **6** items.
