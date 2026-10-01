# chromosomes-mitosis — author's notes (batch 2)

## Lesson record

```python
dict(slug="chromosomes-mitosis",
     source_file="chromosomes-mitosis.dc.html",
     subject="biology", topic_id="cell-biology",
     title="Chromosomes, the cell cycle and mitosis",
     spec="4.1.2.1–4.1.2.2", family="Process",
     routes=["CF", "CH", "TF", "TH"],
     review_state="draft", batch="batch-2",
     # optional: the classifier reads the stepper as "figure"
     block_map={"s-cycle": "worked-example"})
```

Spec: 8461 and 8464 4.1.2.1 Chromosomes + 4.1.2.2 Mitosis and the cell cycle (identical in both specs; examination §1). Cancer is supporting 4.2.2.7 (base).

## Family, and why

**PROCESS.** The demand is a mechanism that unfolds in a fixed order: grow and replicate, then mitosis, then the cytoplasm divides. AQA marks the order ("correct order required for full marks"). The architecture names mitosis as its PROCESS example. So the shape is a worked stepper with predictions at each stage, then the pupil builds the same sequence.

Line-up: hook (figure + Choice) → video → explainer → **cell-cycle stepper (L)** → **sequence chain (M1)** → explainer → **mitosis/meiosis context sort (M2)** → explainer → cancer spot-the-flaw → command words → key fact → ladder → key note → bank → end. No equation, CFIFA or RP block: the examination confirms there is none.

## Activities and the demand each trains

| activity | size | demand | how it delivers it |
|---|---|---|---|
| Hook: model cell with 4 chromosomes, "how does each new cell get all 4?" | commit | predict the need for replication | Ungraded choice; the reveal gives the copy-then-share answer |
| **Run the cell cycle** (`s-cycle`) | **L, flagship** | sequence plus mechanism: what happens at each of AQA's three stages, and its effect on the chromosome count and the DNA mass | 3 stages, 4 predictions in all. Each stage stays locked until every prediction is made. Then the cell figure animates (grow + copy; one set of chromosomes slides to each end and two nuclei form; the two cells slide apart) and a DNA-mass graph draws its next segment. Reduced motion shows the end state at once. Every option is a real `<button>` |
| Build the sequence (`s-order`, Ks4Chain, unscored) | M1 | describe: produce the five-step order the marks follow | 5 links, 2 red herrings (halving to 23; four cells) |
| Mitosis or meiosis? (`s-where`, Ks4Sort) | M2 | spec 4.1.2.2 "recognise and describe situations in given contexts where mitosis is occurring" | 7 contexts (repair, growth ×2, replacement from bone-marrow stem cells, asexual runners, sperm, eggs), each with a corrective note. The context text never contains the words "identical", "growth" or "gamete" |
| Cancer spot-the-flaw (`s-cancer`, Ks4Choice, graded) | micro | explain what goes wrong (4.2.2.7) | 3 options, each distractor a named misconception |
| Ladder | — | r1 Give (q1 verbatim) · r2 Use, a data rung on a DNA-mass graph (3 parts, answers at positions 0/1/2) · r3 Explain chain (identical cells) with 2 red herrings · r4 Explain, 6 marks, levels of response plus 7 indicative points | |

## Misconceptions and where each is confronted

1. **"46 chromosomes become 92 chromosomes"** (examination §5). Born at replication. The stage 1 predict-trap asks "how many chromosomes does the model cell hold?" (options 8 / 4-each-two-copies / 2). The three-beat box `cyConfront92` follows the reveal. It is tested again in ladder r2(c).
2. **"Mitosis makes four cells with half the chromosomes" / confusing it with meiosis** (common_mistake, re-cut per examination C17). Born at stage 3: the predict-trap option "Four cells with 2 chromosomes each" leads into the three-beat box `cyConfrontMeiosis`. It is also a stage 1 and stage 2 distractor, a chain herring and an r3 herring. The re-cut says meiosis is required on **both tiers** (C17 correction), not "not required at Foundation".
3. **"Cells split with no DNA replication first"**: the hook and the stage 1 distractor "It splits at once…".
4. **"Mitosis makes gametes" / "mitosis causes variation"**: the M2 sort (sperm, eggs) and the stage 3 distractor "different from each other".
5. **"Cancer is caused by mitosis"; benign vs malignant**: `s-cancer`, three beats (the quote in the box, the distractor feedback, then the reveal).
6. **"Genes are in the cytoplasm"**: r3 red herring.

## Route tags

None. Every point is base: 4.1.2.1, 4.1.2.2 and 4.2.2.7 carry no HT label and no "biology only" label (examination §2: "No HT content anywhere"). The pack's `higher` field, which the examination ruled **wrong route** (base content withheld from CF/TF), is taught as base on all four routes: the three stages, cancer, and "two identical diploid cells" (without the word "diploid"). The header shows only the build's route chip (the R12 shape), which is true on every route.

## ⚑ Net-new science-bearing items

- ⚑ The model cell (4 chromosomes, 2 pairs, red and blue = one of each pair from each parent): a simplification, declared in `legal`.
- ⚑ Stage prediction options, their corrective `why` texts and `yes` texts (all from 4.1.2.2 wording, 4.6.1.2 for meiosis).
- ⚑ The DNA-mass graph: doubles at replication, stays doubled through mitosis, halves when the cytoplasm divides. This is the examination's typical-question shape.
- ⚑ The two three-beat misconception boxes (92 vs 46; mitosis vs meiosis: four cells, 23 each, genetically different, per 4.6.1.2).
- ⚑ Sequence chain links and herrings (4.1.2.2 sentences).
- ⚑ The M2 contexts. Bone-marrow stem cells replacing blood cells follows examination C12 (red cells themselves do not divide). Strawberry runners count as asexual reproduction, "only mitosis is involved" (4.6.1.1). The runner context is used for recognition only. No bacteria example, per C13: binary fission is not mitosis.
- ⚑ The cancer explainer and the spot-the-flaw options (4.2.2.7 wording: "changes in cells that lead to uncontrolled growth and division", benign "contained in one area, usually within a membrane", malignant "spread … in the blood … secondary tumours"). The spec terms "secondary tumours" are used; "metastasis" and "lymph" are not (C15).
- ⚑ Ladder r2 (graph, 3 parts and model answers), r3 chain, r4 question, levels descriptor and indicative content (from examination §5 typical questions, with cancer left out because it is the `cancer` lesson's).
- ⚑ Key fact line.

## Frozen items flagged wrong, and how they are handled

- **q1 wx2** ("92 is the number of chromatids DURING DNA replication"): IMPRECISE (C23). Kept verbatim in the bank and in r1's feedback, because the examination says it is usable as a rung. The lesson's own 92-vs-46 box gives the correct timing ("after the DNA is copied").
- **q3 and q5** (cancer, 4.2.2.7): correct on all routes and kept in the bank. Not used as rungs: r1 is q1, which tests this lesson's own spec point.
- Non-frozen fields the examination marked wrong are **not carried**: theory 3 "not needed for Foundation GCSE" (C9; the legal line says GCSE never asks for the phase names); common_mistake "not required at Foundation" (C17; re-cut as "on both tiers"); and the not-in-spec G1/S/G2 detail, histones, diploid/haploid terms and cancer treatments (C7, C16, R3, R9). The red-blood-cell line was re-cut per C12.
- The matching activity is replaced by the chain plus the sort.
- No examiner tip exists for this subtopic, so the tip slot is omitted.

## New instrument or helper

The cell-cycle stepper is new and lives in this lesson's own template and logic. Figure helpers `cellFig`, `dnaGraph` and `ladderGraph` (plus `chrom`, `chromSet`, `organelles`, `oneCell`) are built from `KS4D.svg/T/line/circ` and the `KS4D.C` palette, so they match the house plate. The CSS keyframes `cm-grow`, `cm-in`, `cm-slide` and `cm-draw` are in the helmet, `cm-` prefixed so they cannot collide in the batch CSS, and turned off under `prefers-reduced-motion`. No `_ext` file.

## Body prose

About 330 words of explainer and hook prose: hook 45, explainer 1 95, uses 80, cancer 75, plus the two misconception boxes at about 55 each. That is under the 700 cap, and no block exceeds 150 before a commitment.

## Checks run

Rendered in Design's own runtime (pilot `support.js`, with `shared/ks4-lib.js` and `shared/ks4-diagrams.js` and this lesson's `KS4SRC` record generated by `build_ks4.build_source_js`) at 390 and 1280 px. Zero console errors and no `undefined`, `NaN` or `[object Object]` text. All three stages were driven by click, including a wrong prediction that showed its correction, and each stage's figure was checked visually. The build itself was not run; the commander builds the batch.
