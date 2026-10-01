# carbonates-halides-sulfates — author's notes (batch-2)

## Lesson record

```python
dict(slug="carbonates-halides-sulfates", source_file="carbonates-halides-sulfates.dc.html",
     subject="chemistry", topic_id="analysis",
     title="Tests for carbonates, halides and sulfates",
     spec="8462 4.8.3.3–4.8.3.5 (chemistry only) + RP7",
     family="Required practical", routes=["TF", "TH"],
     review_state="draft", batch="batch-2",
     block_map={"s-rack": "practical", "s-ionic": "check"}),
```

`block_map` is needed: the classifier reads `s-rack` as a bare `figure` and raises on `s-ionic`. Verified in a scratch harness against the real classifier.

## Family: REQUIRED PRACTICAL, and why

8462 Required practical 7 is "use of chemical tests to identify the ions in unknown single ionic compounds". The pupil's job is to run the anion tests in the right way, and to name a whole compound from a cation result plus an anion result: that is RP7 itself. BATCH-PLAN's provisional family kept. It differs from the adjacent `metal-hydroxides` lesson (CLASSIFY, precipitate bench). This flagship is about **choosing tests and acids and combining results on unknowns**, not about learning one reagent's colours, and it reuses nothing from that lesson's bench.

## Activities and the demand each trains

| Activity | Size | Demand |
|---|---|---|
| **The test rack** (`s-rack`) | Flagship | Five unknown salts. For each: a metal-ion result already recorded (drawn flame or drawn NaOH precipitate, or both for calcium); the pupil must **call the metal ion first** (the gate) before any anion test unlocks. Then they run any of the three anion tests on fresh samples (animated: acid drops then reagent drops, fizzing, limewater turning milky, precipitate forming; reduced motion swaps to the end state) and **name the salt** from four options. Every wrong option is a named error: the wrong anion (each reply says what that anion would have shown) or the right anion with the wrong metal. Messy observations: copper(II) sulfate's white BaSO₄ sits in blue solution, and the cream/yellow pair needs comparing. Trains combining tests to identify an unknown compound (base RP7 content, examination R8). |
| **Fair test or false positive?** (`s-acid`, `Ks4Sort`) | Mid | Six reagent pairs: which is the fair halide test, the fair sulfate test, or can give a false positive (HCl before AgNO₃, H₂SO₄ before BaCl₂, either reagent with no acid). Trains the acid choice: the misconception confronted where it is born. |
| **Strike out the spectators** (`s-ionic`, Higher) | Mid | Three full equations (AgNO₃ + NaBr, BaCl₂ + Na₂SO₄, Na₂CO₃ + 2HCl); tap the spectator ions, check, then the ionic equation is revealed. Unlocks one at a time. |
| Hook `Ks4Choice` | Micro | Five tubes all white after HCl + AgNO₃: what went wrong? |
| Spot-the-flaw `Ks4Choice` (`s-think`) | Micro | "It fizzed, so it is a carbonate", with a drawn magnesium-in-acid tube. |
| RP block (`s-rp`) | — | Drawn apparatus (delivery tube into limewater), 5-step method, 4 risks with controls. |
| Exam ladder | — | r1 verbatim q2 (Identify, 1); r2 data table P/Q/R across the three tests (Identify, 3); r3 chain: why HCl before BaCl₂, with two herrings (Explain, 3); r4 the examiner's 6-mark Plan (Na₂CO₃ / Na₂SO₄ / NaI), levels-marked (Plan, 6). |

No CFIFA: no calculation. No exam-tip slot: no `examiner_tip`.

## Misconceptions and where each is confronted

| Misconception (examination §5) | Where |
|---|---|
| Acidifying the halide test with HCl; the sulfate test with H₂SO₄ | Hook (the whole scenario), `s-acid` sort, r3 herring, r4 reject, key-note line 5 |
| "The acid removes sulfate" | **Never stated anywhere.** Every reason given for acidifying is "removes carbonate ions" (examination C7). |
| Fizzing proves a carbonate | `s-think` spot-the-flaw with a drawn magnesium tube (three beats) |
| Adding limewater to the solid | `s-think` reveal ("bubble it through limewater; never pour limewater onto the sample") and the drawn apparatus |
| Cream vs yellow | Rack: potassium iodide is a distractor for potassium bromide, and its reply says to compare against a white background; legal line |
| "Silver nitrate turns white" instead of "a white precipitate forms" | Every result in the rack is worded as "… precipitate" |
| Anion tests identify the metal (or NaOH the anion) | Rack gate: cation from the cation result, anion from the anion tests; "Right anion, wrong metal" replies; key-note line 6 |

## Route tags (all from the AQA spec)

Whole lesson TF/TH only: 8462 4.8.3.3–4.8.3.5 are "(chemistry only)"; 8464 has only the CO₂ gas test (5.8.2.3).

| Element | Tag | Citation |
|---|---|---|
| Carbonate, halide, sulfate tests; why acidify; which acid; combining cation + anion results; Na₂CO₃ + 2HCl equation | base (triple lesson) | 8462 4.8.3.3, 4.8.3.4, 4.8.3.5 (no HT marker); 4.8.3.1 ("identify species from the results of the tests in 4.8.3.1 to 4.8.3.5"); RP7; 4.1.1.1 balanced equations |
| `s-ionic` (ionic equations by striking spectators); key-note line 7 | `data-route="higher"` / `R.isHigher` | 8462 4.1.1.1 "(HT only) … ionic equations" |
| "Contains Higher" header pill | `sc-if isHigher` | — |

## ⚑ Net-new science-bearing items

1. ⚑ Hook scenario (HCl then AgNO₃ gives white for every salt), options, reveal ("hydrochloric acid … contains chloride ions"). 4.8.3.4; examination C18 and §5.
2. ⚑ Explainer re-cut from th1–th3: "carbonate ions would also give a precipitate with either reagent, and the acid removes them as carbon dioxide" (examination C7, C13).
3. ⚑ RP block method and risks (examination §5 RP7, anion part).
4. ⚑ Spot-the-flaw: magnesium fizzes in dilute acid, its gas is hydrogen, which leaves limewater clear; "test the gas" (examination §5; 4.8.2.3 limewater test).
5. ⚑ The rack's five salts and every result: Na₂CO₃, KBr, CuSO₄, CaCl₂, LiI against acid + limewater, HNO₃ + AgNO₃, HCl + BaCl₂. Copper(II) sulfate gives no precipitate with nitric acid + silver nitrate at test concentrations (silver sulfate is not precipitated); a carbonate gives "fizz, then no precipitate" in the halide and sulfate tests.
6. ⚑ The rack's metal-ion clues use the spec's flame colours (4.8.3.1: lithium crimson, sodium yellow, potassium lilac, calcium orange-red, copper green) and NaOH results (4.8.3.2).
7. ⚑ Every cation and compound reply in the rack.
8. ⚑ `s-acid` sort items and reasons, including "silver nitrate on its own" (carbonate ions would also give a precipitate with silver nitrate; examination C7's credited reason).
9. ⚑ Equation card caption: "Any carbonate does the same: a salt, water and carbon dioxide."
10. ⚑ Higher spectator activity: the three full equations with state symbols and their ionic equations (examination R6, C15, §5 equations to learn); CO₃²⁻(aq) + 2H⁺(aq) → H₂O(l) + CO₂(g) with state symbols added.
11. ⚑ Ladder r2 table and model answers; r3 chain and herrings; r4 levels, indicative content and reject lines (examiner-drafted 6-marker, examination §5).
12. ⚑ Key-note lines 5–7 (lines 1–4 are the verbatim source key note, split at its full stops); key fact card.

## Frozen items flagged wrong, and how each is handled

- **Quiz q1 ("Why must solutions be acidified with nitric acid before adding silver nitrate…")** — WRONG in its key and wx1: it says nitric acid removes **sulfate** ions (examination C24, C25, §4). **Kept verbatim in the practice bank** (`K.bank`, untouched), **never a ladder rung on TF or TH**, and **never quoted or paraphrased in the body**. The correct reason ("to remove carbonate ions, which would also form a precipitate") is taught in new text: explainer, `s-acid` sort, r3.
- **Quiz q2** — clean; rung 1 on both routes.
- **th2 "acidify to remove interfering ions like CO₃²⁻ or SO₄²⁻" and "Why nitric acid first? To remove CO₃²⁻ and SO₄²⁻"** — WRONG (C7, C10). Not used.
- **th1 sulfite paragraph** — NOT-IN-SPEC and its distinguishing method WRONG (C4, C5). Cut.
- **`equations` field line 1 ("acid + CO₃²⁻ → CO₂ …")** — IMPRECISE, not a balanced equation (C20). Not used in the equation block; the block shows the balanced Na₂CO₃ + 2HCl equation from th1.
- **`rp` field "RP Chemistry 4"** — WRONG number (C22). Not displayed. Pills and RP block say "Required practical 7", chemistry only; no Combined equivalent.
- **Ionic equations shown as base on TF** (R6) — re-tagged Higher.
- **`higher` "identify an unknown compound" and "explain the need for acidification"** — base content (R7, R8): taught to both routes.
- **CO₂ + Ca(OH)₂ → CaCO₃ + H₂O** (th1) — correct but beyond the spec's demand (C3); not labelled "Learn it" and not shown.

## New instruments and helpers

All inside the lesson's own Component logic; no `_ext` file.
- `rackSvg(S, test, anim)`: the test tube (dropper, acid then reagent drops, bubbles, precipitate) and the carbonate apparatus (bung, delivery tube, limewater turning milky). CSS keyframes inside the SVG are emitted only on the animated frame. Under reduced motion the end state is drawn directly.
- `clueSvg(S)`, `flame()`, `mini()`: the drawn metal-ion results (flame colour, small precipitate tube).
- `rigSvg()`, `hookFig()`, `fizzFig()`.
- `outcome(an, test, blueSol)`: the one table of what each test shows for each anion.
- Option order in the rack's two choice sets is a stable hash shuffle (`KS4.hash`), as `KS4.item` does for quizzes, so the right answer is never always first.

## Body prose

About 400 words of template prose (hook 45, explainer 86, RP block 147 including its heading and risk cards, Higher ionic intro 50, equation card 33, the rest headings and prompts), under 700. The misconception commitment sits between the explainer and the RP block so no run of prose exceeds ~150 words before a commitment.

## Self-check done

Compiled, route-layered and rendered through the real `build_ks4` functions in a scratch harness, then driven in headless Chrome on TF and TH (animated and reduced motion): zero console errors at 1280 and 390, no horizontal overflow at 390, no `undefined`/`{{` text (the one "NaN" match is the formula NaNO₃), Higher section and badge present on TH and absent on TF, rung 1 resolves from the route's own quiz, all five salts can be named, the wrong-name replies fire, and all three spectator equations grade and reveal their ionic equations.

## Review fixes

- quality-b Q-1 → Removed the `Triple`, `Foundation · Higher` and `Contains Higher` pills. Added the route chip as in using-moles-calculations. The RP pill now reads `Required practical · identifying ions`. Eyebrow → `AQA Chemistry (8462) 4.8.3.3–4.8.3.5 · Required practical`.
- quality-b Q-2 → rung 4 question → "Plan tests that would identify each solid. Give the result each one would show." (the command stays `Plan`).
- quality-b Q-3 → the rack's results log now lists only earlier tests (`x.k !== r.last`), headed "Salt N · earlier results". The latest result shows once in the result line, plus the figure caption.
- quality-b A-1, A-2, A-3 (advisory) → not done (A-2 matches the pilot's own pattern; A-1 and A-3 would be design changes).
- science-chem-b A-8 → key-note line 4 `Always acidify first to remove interfering ions.` → `Always acidify first to remove carbonate ions.` This edits the frozen key-note sentence, on the examiner's advice.
- No new block_map need: the classification is unchanged.
