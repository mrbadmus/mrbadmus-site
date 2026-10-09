# KS4 batch 6: 14 lessons

Written from `docs/ks4/packs/batch-6/` (00-BRIEF.md, FLAGS.md, 04-checked-science-source/, 05-diagram-library/README.md), main, 4 Oct 2026. The batch-6 prompt's three updates override the pack. No lesson text comes from old site data: these pages don't load `ks4-source.js`; every quiz item is written into its lesson.

## Files and routes

One runnable `.dc.html` per lesson in `Batch 6/lessons/`, named `ks4-<subject>-<spec>-<slug>` with the corrected AQA reference from FLAGS. Order is the prompt's.

1. Factors affecting food security · `ks4-biology-4.7.5.1-factors-affecting-food-security` · TF TH
2. Group 1 · `ks4-chemistry-5.1.2.5-group-1` · CF CH TF TH
3. Reactions of acids · `ks4-chemistry-5.4.2.1-reactions-of-acids` · CF CH TF TH · Higher layer CH TH
4. Life cycle of a star · `ks4-physics-4.8.1.2-stellar-evolution` · TF TH
5. Animal and plant cells · `ks4-biology-4.1.1.2-animal-plant-cells` · CF CH TF TH · RP1 · calculates
6. Cell specialisation · `ks4-biology-4.1.1.3-cell-specialisation` · CF CH TF TH
7. Culturing microorganisms · `ks4-biology-4.1.1.6-culturing-microorganisms` · TF TH · Biology RP2 · calculates · Higher layer TH
8. Stem cells · `ks4-biology-4.1.2.3-stem-cells` · CF CH TF TH
9. Principles of organisation · `ks4-biology-4.2.1-principles-of-organisation` · CF CH TF TH · calculates
10. Digestive system · `ks4-biology-4.2.2.1-digestive-system` · CF CH TF TH · RP3 (Combined) / RP4 (Biology)
11. Health, disease and risk factors · `ks4-biology-4.2.2.5-health-disease` · CF CH TF TH
12. Cancer · `ks4-biology-4.2.2.7-cancer` · CF CH TF TH
13. Transpiration · `ks4-biology-4.2.3.2-transpiration` · CF CH TF TH
14. Translocation · `ks4-biology-4.2.3.2-translocation` · CF CH TF TH

Transpiration and translocation share the spec point 4.2.3.2, so the slug tells them apart.

## Page order (every lesson)

Header (AQA ref, route chips, RP badge where there is one, route picker) → Start here (`Ks4Guess`) → video slot → teaching sections, each with a figure and one interaction (Higher layers as `sc-if` on `isHigher`) → equation block (`Ks4Triangle`), CFIFA (`Ks4Cfifa`) and Step 1 / Step 2 (`Ks4Steps`) where the lesson calculates → Think again (`Ks4Choice`) → Sort (`Ks4Sort`) → command words → key fact → exam ladder (`Ks4Practice`) → key note → practice set (`Ks4QuizBank`) → end. Triple-only pages offer only the two Triple routes in the picker. No examiner tips: none approved.

## Shared blocks

Copied from the batch-5 delivery (the newest), into `lessons/` so each page runs on its own: Ks4Triangle, Ks4Guess, Ks4Steps, Ks4Practice, Ks4Chain, Ks4Write, Ks4Chrome, Ks4Cfifa, Ks4Choice, Ks4Sort, Ks4KeyNote, Ks4QuizBank, Ks4End, Ks4Video, ks4-lib.js, ks4-diagrams.js, ks4-theme.css, support.js.

One change: **Ks4Triangle** accepts `fixed: true` on a bottom item. A fixed cell (π in A = π r²) is greyed and can't be picked, and reads "pi, about 3.14, a fixed number" to screen readers. It reuses the existing `half` styling path; nothing else changes, and every batch 4–5 equation renders as before.

## Design-system path

Pages link `../../_ds/…`, as the prompt asks. In this project the design system sat at the project root, one level above `Design's Output`, so from `Batch 6/lessons/` that path didn't resolve. I copied the same `_ds` folder (17 files, unchanged) to `Design's Output/_ds` so the links work as written. Batch 4 and 5 still resolve to the root copy. Code: keep one of the two.

## Rules 1–4

- **Rule 1.** Every opener is "If you had to guess, …?" with exactly two options from everyday life (bread shelf, oil jar, tablet in vinegar, bonfires, lettuce and carrots, kitchen tools, bread mould, plant cutting, bricks and rooms, toast, a cold and a sunburn, a wart, washing on a line, potatoes). Titles and scenes set up the situation without giving the answer. Where both options are true (food security: more people, or less grown), both are marked right and the reply says so.
- **Rule 2.** Four triangles, all `source: 'none'` with no chip, reading "Written out": magnification (I over M × A); A = π r² with π fixed and the square-root extra line on r; number of divisions = time ÷ mean division time. Each appears in an equation block and under every CFIFA and Steps Formula line that uses it. Bacteria = starting number × 2ⁿ has no triangle and is taught as doubling. The size comparison in Principles of organisation ("bigger ÷ smaller") is a division with no triangle (see 9.2). "Learn this one" appears nowhere.
- **Rule 3.** Magnification: mm ↔ µm taught in the equation block and as the C line of both worked examples before either attempt. Culturing: "r = diameter ÷ 2" taught as its own line; worked examples with nothing to convert, then with a conversion; then attempts. Bacteria chain: Divide button (one doubling per line) → triangle → worked `Ks4Steps` → attempt `Ks4Steps` → ladder. Organisation: unit conversions → two worked → two attempts → ladder. Every calculation is CFIFA.
- **Rule 4.** Ladder 2 · 2 · 2 · 1 on every page and route; rung 4 is one 4- or 6-mark answer. Practice set: five questions per route. Where a Higher layer swaps an item (acids CH TH, culturing TH), the count stays the same.

## Quiz items (practice set, five per route)

- 1 Food security: q1 verbatim; q2 rebuilt (F1); 3 new
- 2 Group 1: q1 q2 verbatim; 3 new (chlorine, oxygen, predict caesium)
- 3 Acids: q1 q2 verbatim; base 3 new (formula, fizz, H₂ test); CH TH swap the H₂ test for a redox item
- 4 Star: q1 (wx1 rebuilt, F3), q2 verbatim; 3 new
- 5 Cells: q1–q5 verbatim
- 6 Specialisation: q1 q3 verbatim; q2 q4 with explanations rebuilt (F1, F2); 1 new
- 7 Culturing: q1–q3 verbatim; 1 new bacteria-count item; TF tape item / TH standard-form item
- 8 Stem cells: q2 verbatim; q3 wx2 rebuilt (F2); 3 new (q1, q4 left out, see 8.3)
- 9 Organisation: q1–q4 verbatim (q3 wx1 re-voiced, F1); 1 new size item
- 10 Digestive: q1 q3 q4 q5 verbatim; q2 with wx1 replaced (F2)
- 11 Health: q1–q3 verbatim; 2 new (scatter, sampling)
- 12 Cancer: q1 q2 verbatim; 3 new (q3 off-spec, F2)
- 13 Transpiration: q1–q3 verbatim; 2 new
- 14 Translocation: q1–q3 verbatim; 2 new

Options are shuffled by `KS4.item()`, as before.

## Science flags

**G · Global**
- G1. Arrows, subscripts and superscripts inside JS-built text (quiz, ladder, sort, key note) are plain characters and fall back to a system font, as in batch 5. In template markup, arrows are inline SVG and sub/superscripts use `<sub>`/`<sup>`. Verbatim items keep their own glyphs.
- G2. Teaching numbers are round and labelled on the page: food-production index, plate zones, bubble distances, smoking table, typical sizes.
- G3. Prev/next follow subject order inside this batch (biology: cells → organisation → plant transport → food security; chemistry: Group 1 → acids). Combined-route pupils on cell specialisation and stem cells meet a Triple-only neighbour (culturing). Links to earlier batches use `../../Batch 5/lessons/…` and `../../Batch 4/lessons/…` as the prompt specifies; in this project those folders are named `KS4 Batch 5/` and `KS4 Batch 4/` without a `lessons/` level, so they resolve only in Code's layout. Code to rewire.
- G4. Drawings are mine in the ks4-diagrams style; the figlib functions the diagram README names (`star_life_cycle`, `plant_cell`, `_leaf_section`) are Python and weren't ported. Where the README's figure briefs disagree with FLAGS (totipotent stem cells, cancer treatments, phloem "needs energy"), FLAGS win.
- G5. Sibling overlap: where content belongs to another lesson it is a one-line pointer (osmosis → Transport in cells; stomata distribution → Plant tissues; enzymes → Enzymes; viruses and cancer → Health and disease; xylem pull → Transpiration).

**1 · Food security**
- 1.1 TF TH only; route picker offers the two Triple routes. Data task (population vs food production) on both Triple routes, no HT label (F2). Rest of the old `higher` text not used.
- 1.2 All six spec threats count, including cost of inputs and conflict (F1). Transport point for changing diets taught (F3). Failed-rains example and the closing sustainability line (F4).
- 1.3 q2 rebuilt per F1: same key, distractors that are not threats. Data graph is a made-up country (index 2000 = 100), labelled on the page.
- 1.4 Meat inefficiency is a one-line pointer to 4.7.4.3 (biomass lost between trophic levels); not taught here. No sibling link: that lesson isn't in batches 4–6.
- 1.5 Rung 4 is a 6-mark Evaluate.

**2 · Group 1**
- 2.1 No Higher badge; the trend explanation and prediction are base on all four routes, never "ionisation energy" (F2). Oxygen and chlorine reactions with all six balanced equations, every route (F1).
- 2.2 T1 re-cut: "react with water", vigour rising down the group (F4); "sodium melts into a ball" added.
- 2.3 Predict-from-trend activity uses the pack's melting points (F3); the reveal gives Rb's real value, 39 °C. Rung 2's boiling points (Li 1342, Na 883, K 759, Rb 688 °C) are standard data, not in the pack: Code to check.
- 2.4 Universal indicator "purple" for the hydroxide solution is from the source.

**3 · Reactions of acids**
- 3.1 Higher layer (CH TH) is redox for acid + metal: Mg + 2H⁺ → Mg²⁺ + H₂, half equations, spectator ions named, Zn and Fe the same (F1, F2). No precipitation, and the old `higher` text is not shown. On CH TH, bank q5 and rung 3's second chain swap to redox items; counts stay 5 and 2·2·2·1.
- 3.2 Oxide, hydroxide and carbonate reactions are all labelled neutralisation (F3). Charge-balancing method taught with three tasks and one bank item and one rung-2 item (F4).
- 3.3 Colour shown only for CuO + H₂SO₄ → blue CuSO₄ (F5). Metals limited to Mg, Zn (Fe in the sort) with HCl and H₂SO₄; metal buttons are disabled for nitric acid. Copper is the no-reaction case.
- 3.4 The carbonate in the simulator is sodium carbonate, to avoid the insoluble calcium sulfate layer with sulfuric acid. The soluble-salt RP is left to `salts-neutralisation` (one line in the end note).
- 3.5 Hook: indigestion tablets contain a carbonate (typical, e.g. calcium carbonate); vinegar's acid is ethanoic, not one of the three on the page.

**4 · Life cycle of a star**
- 4.1 Badge 8463 4.8.1.2, no 8464 ref (F1). TF TH only; no Higher badge; force balance and element formation for TF and TH alike (F2). No remnant mass thresholds: "about the mass of the Sun" / "much more massive than the Sun" only.
- 4.2 Bank q1 keeps the verbatim stem, options and key with wx1 rebuilt per F3. q2 verbatim (F4); my text uses the spec sentence without "only" and never cites iron as heavier than iron.
- 4.3 Supernova: no "outshines a galaxy" line; the Sun ends as a white dwarf (F5). Planetary nebula isn't drawn or named (context only per brief); "outer layers drift away" in the white dwarf note.
- 4.4 Hook: "more massive stars burn faster and have shorter lives" is from source T3, not a spec statement. Code to check it's acceptable as the reveal.
- 4.5 Force wording: "outward pressure from fusion energy"; verbatim q1 keeps "radiation pressure".

**5 · Animal and plant cells**
- 5.1 RP1 badged on all four routes; the page observes and labels, and points to the Microscopy lesson (batch 3) for the method and drawing rules (F4). No link: batch 3 isn't in this project; Code to wire `microscopy`.
- 5.2 Stains corrected: iodine on onion, nucleus yellow-brown; methylene blue on cheek, nucleus blue (F1). "Respiration releases energy", no ATP in my text (F2); verbatim q5 keeps ATP as F2 allows. No chloroplast count (F3).
- 5.3 Estimation task (F5): what fraction of the onion cell the vacuole fills, judged by eye, no arithmetic.
- 5.4 Magnification triangle (I over M × A), `source: 'none'`, "Written out". Convert (mm × 1000 = µm) is taught in the equation block and is the C line of every CFIFA example before any question uses it. Worked: 20 mm / 50 µm → ×400; ×100, 15 mm → 150 µm. Attempts: ×500; 10 µm. Ladder: ×2000; 40 µm. Magnification answers take the unit "no unit".
- 5.5 Ribosomes drawn as dots in both cells; the figure is schematic.

**6 · Cell specialisation**
- 6.1 Six spec cells in the design-a-cell activity (sperm, nerve, muscle, root hair, xylem, phloem); red blood cell appears only in bank q2; palisade left out.
- 6.2 Nerve: "spinal cord to the foot", synapse line (F3). Root hair: osmosis vs active transport, many mitochondria; no "water potential" (F4, F5a). Mature animals divide for repair and replacement (F5b). Phloem: spec structure only, no companion cells or loading (F6). Sperm: "release energy", "enzymes to digest a way into the egg", "half the number of chromosomes"; no ATP, acrosome or haploid in my text (F7). Verbatim q1 keeps ATP, as F7 allows.
- 6.3 Bank q2 and q4 keep stem, options and key with the explanations rebuilt from F1 and F2.
- 6.4 Muscle "protein fibres that contract" is my wording for the spec's adaptation. Rung 2's small-intestine "Suggest" item gives the folds as information; "microvilli" is not named.
- 6.5 Pointers, not teaching: osmosis to Transport in cells (batch 4), xylem pull to Transpiration, sugar movement to Translocation, stem cells to Stem cells.

**7 · Culturing microorganisms**
- 7.1 Badge 8461 4.1.1.6 (F2); "Biology required practical 2", never RP6, no Combined number (F1). TF TH only. Standard form is a Higher layer, TH only: a taught box after the worked chain, the attempt's answer line, one bank item and the ladder model line.
- 7.2 Loops flamed red hot; dishes, media and glassware autoclaved (F4). Tape: two to four strips, oxygen in, no anaerobic pathogens; stored upside down for condensation (F5). 25 °C in school. Bread/yeast not raised (F6). Fair-test variables in the method; "resistant" for antibiotic C; antiseptic wording in the note (F7).
- 7.3 Binary fission "as often as once every 20 minutes", broth or agar, uncontaminated cultures (F3), taught with a Divide button that writes one doubling per line.
- 7.4 A = π r² triangle with π as a fixed cell (new `fixed` flag in Ks4Triangle) and the square-root extra line on r. "r = diameter ÷ 2" is its own taught line in the equation block. CFIFA example 1 is the frozen FIFA verbatim with the pack's Convert line; the halving sits in that step's note because the four FIFA lines are frozen. Example 2 converts (2.4 cm → 24 mm → r 12 → ≈ 452 mm²). Attempts: 14 mm → ≈ 154 mm²; 1.6 cm → ≈ 201 mm². Ladder: 2.0 cm → ≈ 314 mm².
- 7.5 Bacteria chain: Step 1 divisions = time ÷ mean division time (triangle, hours → minutes first); Step 2 doubling with no triangle, the doublings written as one arrow chain on the Fine-tune line (Ks4Steps has one line per CFIFA letter). Worked: 1, 20 min, 3 h → 9 → 512 (TH 5.12 × 10²), the examiner's example. Attempt: 50, 30 min, 2 h → 4 → 800. Ladder rung 2: 10, 20 min, 2 h → 6 → 640.
- 7.6 Plate figures (18 mm, 28 mm, none, control) are round teaching numbers. No sibling links: batch 4–6 has no other microbiology page.

**8 · Stem cells**
- 8.1 "Totipotent" and "multipotent" appear nowhere in my text (F1, F3). Embryonic "most types of human cell"; bone marrow "a limited range, including blood cells"; meristem "any type of plant cell" (F1, F6). Embryo "about 5 days old" (F5). "Fewer ethical objections" wording is not needed: adult cells' ethics aren't compared.
- 8.2 Therapeutic cloning, non-rejection and viral-infection risk are base, all four routes (F4). No nucleus-into-egg method.
- 8.3 Bank: q2 verbatim; q3 with wx2 rebuilt (F2); q1 not used (F3). q4 left out too: it is usable per F3 but leans on "totipotent/multipotent", which the page doesn't teach; replaced with a spec-worded meristem item. Code may restore q4.
- 8.4 Leukaemia/bone marrow transplant is from the source and brief, not the 4.1.2.3 spec text. Code to check it is wanted as the adult-cell use.
- 8.5 The cell types lit in the comparator are examples, labelled as such.

**9 · Principles of organisation**
- 9.1 Tissue in the spec's words, "a group of cells with a similar structure and function" (F1); q3's wx1 re-voiced as F1 allows. Stomach is the worked organ (muscle, glandular, epithelial), taught as the Sort (F2). No gene-switching line (F4).
- 9.2 Size and scale (F3): conversions (µm → mm → cm → m) taught first, then CFIFA with no triangle: "times bigger = bigger ÷ smaller" is a comparison by division, not an AQA equation (same call as batch 5's 8.4). Worked: 5 cm vs 50 µm → 1000; 1.5 m vs 12 cm → 12.5. Attempts: 100; 8. Ladder: 200; 50. Bank item: 100. If Mide wants a triangle here, it is a small change.
- 9.3 Typical sizes (cell ~50 µm, tissue ~1 mm, organ a few cm, human ~1.5 m) are round teaching figures from F3, labelled.

**10 · Digestive system**
- 10.1 No Higher layer; bile and villi taught on every route; "microvilli" not named (F1).
- 10.2 Sites of production as the three-row table: amylase (salivary glands, pancreas, small intestine), protease (stomach, pancreas, small intestine), lipase (pancreas, small intestine) (F2). Bank q2 with wx1 replaced by F2's wording.
- 10.3 RP labelled by route: "Required practical 3" on CF CH, "Biology required practical 4" on TF TH, never RP4 on Combined (F3). Benedict's heated in a water bath, blue → green/yellow/orange/brick-red; iodine orange-brown → blue-black; Biuret blue → purple; ethanol cloudy white emulsion; eye protection, no flame near ethanol (F4).
- 10.4 "Carbohydrase", the three word equations and what the products are used for, every route (F5). Enzyme action is a one-line pointer to the Enzymes lesson (F6); no link: it isn't in batches 4–6.
- 10.5 Stomach acid is described as giving the conditions the stomach protease works best in; "kills bacteria" is left to verbatim q1's explanation. Verbatim q5 keeps "maltose"; my text says "sugars".

**11 · Health, disease and risk factors**
- 11.1 Badge 4.2.2.5–4.2.2.6 (F7). Health in the spec's words; the WHO definition is not used (F1). No Higher layer; correlation, causation and sampling on every route (F4).
- 11.2 All four spec interactions, plus "diet, stress and life situations" (F2). Unborn babies, carcinogens including ionising radiation, interacting factors, and human and financial costs at each level (F3). Diet → obesity → type 2 diabetes (F6).
- 11.3 Data (F5): a five-row made-up table plotted point by point onto a scatter graph, then a correlation-or-cause choice and a sampling choice. Bank adds a scatter item and a sampling item. Rung 4 is a 6-mark Discuss on costs.
- 11.4 No percentage-change calculation: the brief offers one, but this batch's prompt says no calculations outside the three lessons named.
- 11.5 Cancer's benign/malignant content is left to Cancer (a link); CHD is a connects link to batch 4.

**12 · Cancer**
- 12.1 Badge 4.2.2.7 (F5). No Higher layer (F1). "Secondary tumours" is the term taught; "metastasis" appears only in verbatim q1 (F3). Treatments are not on the page at all, and q3 is not used (F2). No asbestos line (F4).
- 12.2 Benign: "contained in one area, usually within a membrane", spec words. Lifestyle risk examples (smoking, UV, alcohol) and the genetic example (inherited genes, e.g. some breast cancers) are my wording; viruses as triggers are a pointer to Health and disease.
- 12.3 Verbatim q1's wx3 mentions surgery and chemotherapy; kept because the brief rules q1 usable as written. Code may prefer to re-voice it.

**13 · Transpiration**
- 13.1 Badge 4.2.3.2 (F7). No Higher layer; the potometer investigation is base, every route (F1). Never badged as an RP (F6). No cohesion/adhesion (F2).
- 13.2 Stomata and guard cells taught with an open/closed toggle; most stomata on the lower surface and root hair osmosis are one-line pointers to Plant tissues (batch 5) and Cell specialisation (F4).
- 13.3 **Rate calculations left out.** The pack's brief and F3 ask for rate = distance ÷ time, the volume (π r² × distance) then rate chain, and means. This batch's prompt names only three calculating lessons and says "every other lesson has no calculations: don't add any", so the potometer reads "mm in 1 minute" as a comparison only, with no division. This needs Mide's call: if transpiration should calculate, it needs triangles, CFIFA and a worked Step 1 / Step 2 (rules 2 and 3), which is a substantial addition.
- 13.4 Bubble distances are made-up round figures that show direction only, labelled. Bank avoids partly-true distractors in the new items (F5); verbatim q3 kept as ruled.

**14 · Translocation**
- 14.1 Badge 4.2.3.2 (F5). No mechanism, companion cells, ATP or pressure on any route; no Higher layer (F1, F2). The contrast table has no "driving force" or "energy" rows.
- 14.2 Spec structure taught as half the contrast: phloem tubes of elongated living cells with end-wall pores; xylem hollow tubes strengthened by lignin (F4).
- 14.3 "Source" and "sink" are taught as labels in the flow section and key note, so verbatim q3 is used (F3).
- 14.4 The diagram README's figure brief (amino acids in phloem, "needs energy") is overruled by F1; not drawn. Rung 2's ring-barking "Suggest" item is mine.

## Not done / for Code

- Transpiration rate calculations (13.3): left out on the prompt's instruction; needs a decision.
- Videos: `KS4.VIDEOS` is empty, so the slot stays hidden.
- No examiner tips: none approved.
- Links to Microscopy (5.1) and Enzymes (10.4) are text only: those pages aren't in batches 4–6.
- Dark mode uses the existing remap; SVG plates stay cream.
