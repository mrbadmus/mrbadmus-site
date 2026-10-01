# metal-hydroxides — author's notes (batch-2)

## Lesson record

```python
dict(slug="metal-hydroxides", source_file="metal-hydroxides.dc.html",
     subject="chemistry", topic_id="analysis",
     title="Metal hydroxides", spec="8462 4.8.3.2 (chemistry only) + RP7",
     family="Classify", routes=["TF", "TH"],
     review_state="draft", batch="batch-2",
     block_map={"s-bench": "practical", "s-forge": "worked-example", "s-ionic": "check"}),
```

`block_map` is needed: the classifier reads `s-bench` as a bare `figure` (it has a `{{ tubeFig }}` binding) and raises on `s-forge` and `s-ionic` (no import, no figure). Checked against the real `compile_batch_lesson` + `classify_lesson_sections` in a scratch harness: with this map every section classifies.

## Family: CLASSIFY, and why

The demand is "decide the category fast, and know why": precipitate colour → ion, then for the three white precipitates, excess → aluminium or not, then the honest limit (calcium or magnesium needs a flame test). That is CLASSIFY's decision instrument plus drills at rising stakes. BATCH-PLAN's provisional family kept. It is not REQUIRED PRACTICAL: the adjacent lesson (`carbonates-halides-sulfates`) carries RP7 as its family and its full block; this lesson carries only RP7's sodium-hydroxide part.

## Activities and the demand each trains

| Activity | Size | Demand |
|---|---|---|
| **Precipitate bench** (`s-bench`) | Flagship | Round 1 (6 named solutions): commit to a precipitate colour, then watch the drops go in (animated; reduced motion swaps to the end state). White precipitates get a second commit (dissolves / stays) before excess goes in. Iron(II) has a "Leave it to stand" step showing the surface browning (RP7's messy observation). Calcium's precipitate is drawn faint. Round 2 (unknown tubes W–Z, unlocked when round 1 is done): run the test, then identify. A white-precipitate identification before excess is refused ("Hold on"); calcium-or-magnesium must be named as such. Trains classification and knowing when the evidence is not enough. |
| **Equation forge** (`s-forge`) | Mid | Worked CuSO₄ example revealed step by step, then two builds (FeCl₃, FeSO₄): pick the hydroxide formula and the balancing numbers; every wrong pick has its own correction. Trains production of balanced equations (Law 6). |
| **Ionic equation** (`s-ionic`, Higher) | Micro | Cu²⁺ + _OH⁻ → ___: count of OH⁻ and the product with its state symbol. |
| Hook `Ks4Choice` | Micro | Commit: what is the blue solid? Introduces "precipitate". |
| Spot-the-flaw `Ks4Choice` (`s-think`) | Micro | See misconceptions. |
| Exam ladder | — | r1 verbatim q1 (Identify, 1); r2 data table P/Q/R with an excess column and a flame-test column (Identify, 3); r3 chain Al vs Mg with two red herrings (Explain, 3); r4 the examiner's 6-mark Plan, levels-marked (Plan, 6). |

No CFIFA: the lesson has no calculation. No exam-tip slot: the subtopic has no `examiner_tip`.

## Misconceptions and where each is confronted

| Misconception (examination §5) | Where |
|---|---|
| Solution colour reported instead of precipitate colour | Hook (blue solution in, blue solid out), explainer line, bench verdict for copper(II) |
| Swapping iron(II) green and iron(III) brown | Bench round 1 verdicts, with a specific line when the swap is made ("the number in brackets is the charge on the ion"); forge FeCl₃ vs FeSO₄; r2 |
| Adding excess at once and missing the aluminium precipitate | `s-think` spot-the-flaw (three beats: quote → choice with corrective replies → reveal); r3 herring |
| Calling every white precipitate calcium | Bench round 2 refuses a white identification before excess, and refuses "calcium" or "magnesium" alone for tube Y |
| Wrong hydroxide formula (Fe(OH)₂ vs Fe(OH)₃, missing brackets, one OH) | Forge wrong-option replies; Higher ionic builder |
| Flame test identifies all metals / NaOH identifies the anion | r4 reject list; connects to the anion lesson |

## Route tags (all from the AQA spec)

The whole lesson ships on TF/TH only: 8462 4.8.3 is "(chemistry only)", and 8464 5.8 stops at gas tests. Inside it:

| Element | Tag | Citation |
|---|---|---|
| NaOH test, colours, excess, combining with flame test, full balanced equations | base (triple lesson) | 8462 4.8.3.2 (no HT marker; "Students should be able to write balanced equations for the reactions to produce the insoluble hydroxides"); 4.8.3.1 ("identify species from the results of the tests in 4.8.3.1 to 4.8.3.5") |
| Ionic equation card in `s-equation`; `s-ionic` builder; key-note line 6 | `data-route="higher"` / `R.isHigher` | 8462 4.1.1.1 "(HT only) write balanced half equations and ionic equations where appropriate" |
| "Contains Higher" header pill | `sc-if isHigher` (logic, not a route badge) so it is honest on TF | — |

## ⚑ Net-new science-bearing items

1. ⚑ Hook text and options (Cu²⁺ solution blue, Cu(OH)₂ pale blue precipitate). 4.8.3.2.
2. ⚑ Hook reveal's definition of a precipitate (solid formed when two solutions mix). 4.8.3.2 / th1.
3. ⚑ Bench verdicts (FACT table), including "Some books say rust-red or orange-brown; in the exam, write brown" (examination C3).
4. ⚑ Calcium precipitate faint because calcium hydroxide is slightly soluble (source th1 "sparingly soluble"; examination §5 typical results "can be faint").
5. ⚑ Iron(II) hydroxide browns at the surface on standing as air oxidises it (examination C3 and RP7 typical results).
6. ⚑ "Calcium or magnesium: a flame test decides; calcium gives an orange-red flame" (examination C12; 4.8.3.1).
7. ⚑ RP7 method (3 steps), risks, from examination §5 RP7.
8. ⚑ Forge: CuSO₄ + 2NaOH → Cu(OH)₂ + Na₂SO₄ (examination R3); FeCl₃ + 3NaOH → Fe(OH)₃ + 3NaCl (examination §5); FeSO₄ + 2NaOH → Fe(OH)₂ + Na₂SO₄ (new, same pattern); every wrong-option reply.
9. ⚑ Higher ionic builder: Cu²⁺(aq) + 2OH⁻(aq) → Cu(OH)₂(s), plus the spectator-ion sentence in the equation card.
10. ⚑ Spot-the-flaw quote, options and reveal (excess at once).
11. ⚑ Ladder r2 (data table and model answers), r3 chain and herrings, r4 levels and indicative content (examiner-drafted 6-marker, examination §5, adapted wording), r4 reject lines.
12. ⚑ Key-note lines 2–5 (line 1 and line 6 are verbatim source).
13. ⚑ Key fact card.

## Frozen items and source fields flagged, and how each is handled

- **Quiz q1, q2: clean** (examination §4). q1 is rung 1 on both routes. q2 is in the practice bank only; its key mentions "aluminate", which is true but beyond the spec; no rung asks for the aluminate equation.
- **`rp` field "RP Chemistry 4" — WRONG number** (C23). Not displayed. The RP block and pills say "Required practical 7", chemistry only; there is no Combined equivalent.
- **Aluminate equation Al(OH)₃ + OH⁻ → Al(OH)₄⁻ and "amphoteric"** — NOT-IN-SPEC (R5, C9, C16, C21). Not taught; not in any rung.
- **Ammonium test** — NOT-IN-SPEC (R6, C5, C20). Not taught; never a rung.
- **th3 copper flame-test parenthetical** — WRONG (C14). Not used.
- **`higher` "identify both cation and anion"** — WRONG (C17). Not used; combining tests is taught as base, and this lesson's tests are named as cation tests.
- **th2 ionic equations shown as base on TF** (R4). Re-tagged Higher.
- **Key note**: the source key note's sentence 1 is kept verbatim (line 1). Sentence 2 (ammonium) is cut as not in the spec. Sentence 3 ("Aluminium unique: amphoteric") is replaced by the spec's own wording, "Only aluminium hydroxide dissolves in excess sodium hydroxide solution" (C21). The frozen `equations` field "M²⁺(aq) + 2OH⁻(aq) → M(OH)₂(s)" is line 6, Higher only.
- Practice bank: `K.bank(slug, R.route)`, both items, verbatim.

## New instruments and helpers

All inside the lesson's own Component logic; no `_ext` file.
- `tube(o)`: a test-tube figure in the `ks4-diagrams.js` house style (cream plate, #1A1A1A 3px strokes, `KS4D.T` labels). It shows the solution colour, a precipitate cloud or settled layer, an optional browned surface, and a dropper with falling drops. Animation is CSS keyframes inside the SVG string, emitted only on the animated frame. Under reduced motion the end state is drawn straight away (no animation markup at all).
- `view()`, `run()`, `idReply()`: bench state machine; `run()` uses one timer per action, all cleared on unmount.
- `hookFig()`: before/after tubes.
- Precipitate/solution shades are physical colours (plates stay cream in both themes, as the pilot's do).

## Body prose

About 330 words of template prose (hook 40, explainer 72, RP block 87 including its heading, equation block 71, the rest headings and prompts), well under 700. Hook ≤ 150 words before the first commitment. Explainer + RP block ≈ 150 words before the bench's first commitment.

## Self-check done

Compiled through the real `build_ks4.compile_batch_lesson` + `apply_route_layers` + `render_page` in a scratch harness (no repo files written). Rendered on TF and TH and driven in headless Chrome, both animated and with reduced motion: zero console errors at 1280 and 390; no horizontal overflow at 390; no `undefined`/`NaN`/`{{` text; Higher sections and badges present on TH and absent on TF; rung 1 resolves from the route's own quiz; the bench completes all 6 + 4 tubes; the forge and ionic builder grade correctly. Two defects found and fixed during this check: a white unknown could be identified before excess was added, and rapid picks in the forge could be lost to a stale closure (all pick handlers now use functional `setState`).

## Review fixes

- quality-b Q-1 → Removed the `Triple`, `Foundation · Higher` and `Contains Higher` pills. Added the route chip (`ks3-route-switch`, `{{ routeWords }}` / `{{ routeSwitchOptions }}`, as in using-moles-calculations) with fallback defaults on `R`. The RP pill now reads `Required practical · identifying ions`. Eyebrow → `AQA Chemistry (8462) 4.8.3.2 · Classify`. Verified in scratch that TF shows "Triple science · Foundation tier" and TH "Triple science · Higher tier".
- quality-b A-1 (advisory, cheap) → an identified unknown's bench title now reads "Tube W · identified".
- quality-b A-2 (advisory) → not done: varying the ladder shape is a design change beyond the requested scope. The forge already trains the balanced-equation skill.
- science-chem-b A-5 → key-note line 1 `Fe³⁺ = brown/rust` → `Fe³⁺ = brown`. This edits the frozen key-note sentence, on the examiner's advice, to model the answer to write.
- No new block_map need: the classification is unchanged.
