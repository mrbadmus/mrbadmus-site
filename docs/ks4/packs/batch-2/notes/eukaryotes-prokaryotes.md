# eukaryotes-prokaryotes — author's notes (batch 2)

## Lesson record

```python
dict(slug="eukaryotes-prokaryotes",
     source_file="eukaryotes-prokaryotes.dc.html",
     subject="biology", topic_id="cell-biology",
     title="Eukaryotes and prokaryotes",
     spec="4.1.1.1", family="Contrast",
     routes=["CF", "CH", "TF", "TH"],
     review_state="draft", batch="batch-2",
     # optional: the classifier reads both of these as "figure"
     block_map={"s-build": "comparison", "s-scale": "check"})
```

Spec: 8461 and 8464 4.1.1.1 (word-for-word identical; examination §1). Supporting: 4.1.1.5 (the magnification equation), 4.1.1.2 (cellulose walls are plant and algal), 4.6.4 (fungi and protists are eukaryotic), and 8461 4.1.1.6 (biology only; the 20-minute division).

## Family, and why

**CONTRAST.** (Throughout these notes, the 20 µm reference cell is now a liver cell, per S-2.) The demand is one discriminating difference: is the genetic material enclosed in a nucleus or not? Every other structural difference hangs off it. The flagship is therefore a predict-gated A/B instrument that builds the two cells side by side. The spec's second demand, scale and order-of-magnitude calculation with prefixes and standard form, gets a mid-size estimating instrument and the CFIFA block. I chose CONTRAST over QUANTITATIVE because the calculation serves the comparison ("much smaller"), not the other way round.

Line-up (deliberately unlike `chromosomes-mitosis`): hook (scale figure + Choice) → video → explainer → **cell builder (L)** with a growing comparison table → units explainer → **"how many fit across?" (M1)** → Triple explainer → equation (Learn it) → **CFIFA** → command words → key fact → ladder → key note → bank → end. There is no chain or sort mid-lesson, but there is an equation block and CFIFA.

## Activities and the demand each trains

| activity | size | demand | how it delivers it |
|---|---|---|---|
| Hook: cheek cell and bacterium drawn to the same scale (10 µm scale bar); "Where is the bacterium's DNA?" | commit | predict the key difference | Ungraded choice; the 4 options are the 4 misconception positions (in a nucleus, loose loop, none, plasmids as nucleus) |
| **Build the two cells** (`s-build`) | **L, flagship** | classify each structure as animal-only, bacterium-only or both, and so build the comparison AQA's "compare" question rewards | 7 structures (nucleus; membrane + cytoplasm; cell wall; single DNA loop; plasmids; mitochondria; ribosomes). Tapping a bin commits the pick, then the structure animates into the drawing (`ep-in`, reduced-motion: instant) and a row is added to the Yes/No comparison table. Every wrong bin has its own corrective feedback |
| **How many fit across?** (`s-scale`) | M1 | estimate orders of magnitude, with unit conversion (µm→nm, mm→µm) | 3 predict-gated cases (10, 100, 100), drawn to scale. The small objects pop in one by one, lined up across the large one; reduced-motion shows them at once. Each wrong option names the unit slip that produces it |
| CFIFA (`s-calc`) | equation block, not counted | calculate magnification and actual size with units matched first | Worked examples: both source FIFAs verbatim with a Convert step in front ("Nothing to convert: both in mm"; "Nothing to convert before substituting", with the mm→µm conversion inside the verbatim Fine-tune step), plus a new convert-first example (12 mm → 12 000 µm). Two write-it-out questions per tier, each opening with the convert decision. **Foundation**: ×2000 with nothing to convert; mm→µm then ×5000. **Higher**: rearranged to actual size (60 µm); nm conversion with a standard-form answer (×2 × 10⁵) |
| Ladder | — | r1 Give (q1 verbatim) · r2 Calculate, 3 marks, a calc rung with a convert choice and unit (Foundation 24 mm ÷ 400 = 60 µm; Higher 18 mm ÷ 6000 = 3 µm) · r3 Estimate chain (0.1 mm vs 1 µm → 10²) with 2 red herrings (no conversion; 1 mm = 100 µm) · r4 Compare, 4 marks, 6 marking points and reject lines | |

## Misconceptions and where each is confronted

1. **"Bacteria have a nucleus (just smaller)" / "bacterial DNA is in the nucleus"** (common_mistake; examination §5). Born at the hook, which offers it as option A. Confronted after the nucleus structure reveal in the three-beat box `bConfrontNucleus`. Also a reject line in r4.
2. **"Bacteria have a cellulose cell wall"** (common_mistake; C8). Confronted after the cell-wall reveal in the three-beat box `bConfrontWall`. Also a reject line in r4. Peptidoglycan is not named, because it is not in the spec; the box teaches "not cellulose", per C8.
3. **"Plasmids are the nucleus" / plasmids in animal cells**: hook option D, plus the plasmids structure feedback.
4. **"Bacteria have mitochondria"**: mitochondria structure feedback.
5. **Unit slips (µm↔mm by 100, not converting)**: every wrong option in M1, both r3 herrings, the CFIFA `close` lines and the r2 feedback.
6. **Order of magnitude answered as a ratio**: each M1 case's working line ends "= 10ⁿ · n orders of magnitude", and r3's final link.

## Route tags

None after review (see A-EP3 below). Everything taught is base: 4.1.1.1 carries no HT and no "biology only" label (examination: "No HT content anywhere"). The calculation tiers differ by `R.isHigher` only in the CFIFA questions and r2 numbers (content standards §2), not in what is taught. The header shows only the route chip (the R12 shape), which is true on every route. The 8461 4.1.1.6 "every 20 minutes" fact (examination C14, WRONG ROUTE in the pack) is no longer carried here; it belongs to `culturing-microorganisms`.

## ⚑ Net-new science-bearing items

- ⚑ Hook figure drawn to scale (cheek cell 20 µm, bacterium 2 µm, 10 µm scale bar; nucleus about 5 µm).
- ⚑ The cell builder: 7 structure assignments with their corrective texts. Ribosomes in bacteria are base per examination R4 (inferred). Membrane, cytoplasm, wall, loop and plasmids follow 4.1.1.1; no mitochondria follows C7; "cellulose = plant and algal walls" follows 4.1.1.2.
- ⚑ The two three-beat boxes (nucleus; cellulose).
- ⚑ The prefix explainer: milli, micro, nano and centi (4.1.1.1 skills column), and the definition of an order of magnitude. This is also the correct reason missing from frozen q4 wx3 (C37).
- ⚑ M1's three cases and working: 20 µm ÷ 2 µm = 10; 2000 nm ÷ 20 nm = 100; 2000 µm ÷ 20 µm = 100. Sizes are the pack's typical values (theory 5).
- ⚑ Equation-card helper lines (the rearranged actual-size form; "same unit, magnification has no unit").
- ⚑ CFIFA: the new convert-first example, the four tiered questions and their check lines, and the Answer note "×1 × 10⁴" on source FIFA 1 (as the examination suggested at C21).
- ⚑ Ladder r2 (both tiers), the r3 chain and herrings, and the r4 marking points and reject lines (from examination §5 typical questions, with "list about one cell caps at 2").
- ⚑ The Triple line uses the spec's own wording (8461 4.1.1.6).
- ⚑ Key fact line.

## Frozen items flagged wrong, and how they are handled

- **q5 "What is a flagellum…"**: NOT-IN-SPEC (examination R13). Kept verbatim in the practice bank on all routes and **never used as a rung**. The flagellum and capsule are not drawn in the builder.
- **q4 wx3** ("milli means one thousandth, so 1 mm = 1000 µm"): IMPRECISE (C37). Kept verbatim in the bank and not used as a rung. The units explainer gives the correct reason (micro = a millionth).
- Non-frozen theory **not carried**: "Larger eukaryotic cells … need … lungs" (C15, WRONG). The SA:V idea is not taught here because it belongs to 4.1.3.1 diffusion. Also not carried: "two of the largest groupings of life" (C3, imprecise), ER, Golgi, cytoskeleton, nucleoid, peptidoglycan, and the smaller prokaryotic ribosomes (not in spec). The 20-minute fact is carried only behind the Triple tag (C14).
- Source FIFA 1's third step ("F · Both values already in mm — no conversion needed") stays verbatim per the brief. The new C step states the same decision up front, as examination C21 directs.
- The matching activity is replaced by the builder.
- No examiner tip exists for this subtopic, so the tip slot is omitted.

## New instrument or helper

Both instruments are new and lesson-local: the **cell builder** (`buildFig`, the `PARTS` table) and **"how many fit across?"** (`fitFig`, the `FIT` table). Also `hookFig`, `rod`, and `withNote` (which adds a note to one verbatim CFIFA step without editing its text). All are built from `KS4D.svg/T/line/circ` and the `KS4D.C` palette. The CSS keyframe `ep-in` is in the helmet (`ep-` prefixed) and turned off under reduced motion. No `_ext` file.

## Body prose

About 290 words of hook, explainer and misconception prose (66 + 77 + 23 + 27 + 52 + 46). That is under the 700 cap, and no block exceeds 150 before a commitment.

## Checks run

Rendered in Design's runtime harness with `shared/ks4-lib.js`, `shared/ks4-diagrams.js` and this lesson's generated `KS4SRC` record, at 390 and 1280 px. Zero console errors and no `undefined`, `NaN` or `[object Object]` text. The whole builder (including wrong picks and both confront boxes), all three M1 cases and the CFIFA stepper were driven by click. Figures were checked visually at 390 px. The template was compiled with `build_ks4.compile_template_text` and `apply_route_layers` in a scratch run; nothing was written to the repo.

## Review fixes (science-bio-a.md, quality-a.md)

- **S-2** → done. "Cheek cell" → "liver cell" everywhere (bigq, hook h2, figure label and alt, K.fig alt, hook option A, Foundation CFIFA Q1), with every number unchanged. Also renamed in the M1 comparison titles and the fit-figure labels, which had said "animal cell" at 20 µm.
- **Q-EP1** → done. `hookReveal` replaced with the reviewer's text. The explainer sentence "They are much smaller, and their genetic material is not enclosed in a nucleus." is deleted. The builder's answers are no longer given before it asks.
- **Q-EP2** → done. Option A and B replies are now empty.
- **Q-EP3** → done. The hook paragraph is cut to its first sentence; the sizes live in the figure.
- **Q-EP4** → done. `fitFig` is rebuilt on a 640×400 plate. All labels are 26–28 px in plate units. Case 1 adds a "10 bacteria fit across" caption. Cases 2 and 3 add a dashed inset that magnifies the first 5 of the 100 units ("the first 5 of 100 … magnified"), animated in, with an instant swap under reduced motion. Checked at 390 px.
- **Q-EP5** → done. Comparison 1's correct feedback reads "×10: both already in µm, so just divide."
- **Q-EP6** → done. The eyebrow is now "Estimate · {{ fName }}".
- **Q-EP3/Q-CM3 (duplicate captions), Q-X1 (route chip)** → Q-X1 needed nothing: this lesson already had the route chip.
- **A-4** → done. `FIT[1].why[0]` now reads "×10 would make each ribosome 200 nm. Convert first: 2 µm = 2000 nm, and 2000 ÷ 20 = 100."
- **A-EP1** → done. The ribosome corrections are now just the correction ("Bacteria have ribosomes too." / "Animal cells have ribosomes too."), so the verdict no longer repeats itself.
- **A-EP2** → partly done. The DNA loop is redrawn smaller so its label sits clear of the line, and the mitochondrion and its label are moved off the cell outline. The animal cell's ribosomes stay unlabelled: the one "ribosomes" label names the identical marks in both panels, and a second label would crowd the plate at 390 px.
- **A-EP3** → done. The Triple-tagged "every 20 minutes" explainer is deleted from this lesson; 8461 4.1.1.6 is `culturing-microorganisms`' content. The lesson now has no route-tagged elements.
- **A-5, A-6** → no change (the reviewer's own verdict).
- Revalidated in a scratch harness at 390 and 1280 px: 0 console errors, no undefined/NaN. Recompiled with `compile_template_text` and `apply_route_layers`. **No new `block_map` need**; the optional mapping above still applies (`s-build`, `s-scale` classify as "figure").

## Review fixes round 2 (quality-a.md "Round 2")

- **Q2-EP1** → done. `FIT[1].why[0]` now reads "×10 would make each ribosome 200 nm. Convert 2 µm to nm first."; the working line below already prints the division.
- **Q2-EP2** → done. The "10 bacteria fit across" caption is deleted from `fitFig` k=0.
- Same defect, not a numbered row → done. `FIT[2].why[2]` repeated "2000 ÷ 20 = 100" above that same working line; it is trimmed to "Check the conversion: 2 mm = 2000 µm."
- Revalidated in a scratch harness at 390 px with all three comparisons driven: 0 console errors, no undefined/NaN. Recompiled with `compile_template_text` and `apply_route_layers`. No `block_map` change.
