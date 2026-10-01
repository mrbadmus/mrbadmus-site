# Science review — batch 2, group bio-a

Reviewer: fresh AQA GCSE examiner (Opus), 1 Oct 2026. I wrote none of these lessons.
Lessons: `chromosomes-mitosis`, `eukaryotes-prokaryotes`, `enzymes`, `carbon-cycle`.
Specs: 8461 Biology, 8464 Combined Trilogy. The source examination files in
`docs/ks4/packs/batch-2/examination/` were the starting evidence. I re-checked them; I did not take them on trust.

## Method

- Read every lesson source in full: the template and all of the Component logic (stage tables,
  `why`/`reply` texts, figure geometry, CFIFA steps, rungs, levels, reject lines, key-note assembly, bank filter).
- Extracted the prerendered text of all 16 built pages (4 lessons × CF/CH/TF/TH) and diffed each route
  against Triple Higher. Only the route chip, the 8461/8464 eyebrow and key-note label, and the one
  Triple-tagged explainer in `eukaryotes-prokaryotes` differ.
- Drove all 16 pages in headless Chrome on :8711 with `prefers-color-scheme: light`. I captured the
  client-rendered text: ladder, CFIFA, key note and practice bank. On every route, the pages have no
  console errors apart from the expected localhost CORS block on `/api/health`.
- Checked every calculation by hand. Checked the enzymes simulation's noise table against every pH order
  a pupil can choose (see S-3).
- Checked the frozen items served from `shared/ks4-source-batch-2.js` per route, and the `withhold` list in `batch_2.py`.

No lesson teaches HT content (none of 4.1.1.1, 4.1.2.1–2, 4.2.2.1, 4.7.2.2 or 4.7.3.3–5 carries an HT
label), so the Foundation and Higher text is the same apart from the tiered calculation numbers. That matches
the spec. The only separate-science fact (8461 4.1.1.6, bacteria dividing "as often as once every 20 minutes")
is tagged `data-route="triple"`. It is absent on CF and CH and badged on TF and TH. I verified this in the built pages.

---

## 1. chromosomes-mitosis — AQA 4.1.2.1–4.1.2.2 (+4.2.2.7, 4.6.1.2)

**Route-by-route.** CF/CH/TF/TH are identical apart from the chip. That is correct: everything is base. The
pack's wrongly Higher-only `higher` field is taught to all four routes. Meiosis is described as "on both tiers"
(examination C17 fixed). The phrase "not needed for Foundation" (C9) is gone; the legal line says GCSE never
asks for the phase names. Bank: q1–q5 on all routes; nothing is withheld, and nothing needs to be.

**Verified correct.** Stage 1–3 predictions, keyed answers and every `why`/`yes` text. The 92-vs-46 box
("count the copies … 92; count the chromosomes … 46"). The meiosis box (four cells, 23 each, genetically
different: 4.6.1.2). The cell figure: replication shown as joined copies, then one copy of each chromosome
at each end with two nuclei, then two identical cells. The DNA-mass graph doubles in stage 1, stays doubled
through mitosis and halves at division. Rung 2's P–T graph and its three keyed parts (P→Q replication; R =
cytoplasm and membrane divide; Q = 46, each of two copies). Rung 3's chain and herrings. Rung 4's levels and
indicative content. The sort (bone-marrow stem cells, not red cells dividing: C12 fixed; no bacteria
example: C13). The cancer explainer and spot-the-flaw, which use spec wording ("secondary tumours";
"metastasis" and "lymph" are absent from the authored text). The key fact.

### REQUIRED

| # | lesson · routes | where | OLD → NEW | reason | citation |
|---|---|---|---|---|---|
| S-1 | chromosomes-mitosis · all | `s-order` Ks4Chain `prompt` | "This is the order the marks follow in a describe question. Leave out anything that does not happen in mitosis." → "This is the order the marks follow in a describe question. Leave out anything that does not happen in the cell cycle." | The chain is the whole cell cycle. Its first two links (growth, DNA replication) are not part of mitosis, which the spec treats as one of three stages. As written, the prompt tells the pupil to exclude links they must include, and it feeds the examined misconception "the cell cycle = mitosis only" (examination §5). | 8461/8464 4.1.2.2 ("three overall stages of the cell cycle … the mitosis stage") |

### ADVISORY

| # | where | note |
|---|---|---|
| A-1 | rung 1 (frozen q1) feedback | q1 wx2 "92 is the number of chromatids DURING DNA replication" is imprecise (it should be "after"; examination C23). It is served as rung-1 feedback on all routes. It is not wrong enough to withhold: the lesson's own 92-vs-46 box gives the right timing. If the commander allows generated-copy rulings, use the examination's replacement text. |
| A-2 | explainer 2, last sentence | "The one job mitosis never does is make gametes." This is true for animals and is the AQA position (4.6.1.2). Optionally make it "In animals, mitosis never makes gametes" to avoid an over-general claim (plant gametes arise by mitosis). Not examinable either way. |
| A-3 | key note (verbatim) | "Cancer = uncontrolled mitosis caused by mutation in regulatory genes." This is acceptable. The spec phrase is "uncontrolled growth and division", which the lesson's own explainer uses. |

**Frozen items still served that should be withheld:** none.
**For Mide:** none. 8461 and 8464 are identical here.
**Verdict: SCIENCE PASS AFTER REQUIRED CHANGES** (S-1).

---

## 2. eukaryotes-prokaryotes — AQA 4.1.1.1 (+4.1.1.5 magnification)

**Route-by-route.** CF/CH have no 20-minute line. TF/TH show it, badged Triple, in spec wording (8461 4.1.1.6). That is correct.
CFIFA questions and rung 2 switch on `isHigher`. I confirmed this live: CF/TF get 40 mm ÷ 0.02 mm and 15 mm ÷ 3 µm,
and rung 2 is 24 mm at ×400. CH/TH get 36 mm at ×600, 5 mm ÷ 25 nm in standard form, and rung 2 is 18 mm at ×6000.
Bank: q1–q5 on all routes. q5 (flagellum, not in spec) stays in the bank only and is not a rung, which is correct.

**Verified correct.** The builder's seven assignments and every corrective text. The bacterium's wall sits
outside its membrane. "Cellulose = plant and algal walls" (4.1.1.2). The C15 error ("big cells need lungs") is
not carried. The prefix explainer gives micro = a millionth, which is the correct reason missing from frozen q4
wx3. The order-of-magnitude definition. The hook figure is to scale: 20 µm cell, 2 µm × 1 µm rod, 10 µm bar,
all at 15 px/µm. The builder's "drawn 10× larger" is about 10.6×, which is fine. All arithmetic checks out:
20÷2=10; 2000 nm÷20 nm=100; 2000 µm÷20 µm=100; 30÷0.003=1×10⁴; 10÷500=0.02 mm=20 µm; 12 000÷2=6000;
36÷600=0.06 mm=60 µm; 5×10⁶ nm÷25=2×10⁵; 40÷0.02=2000; 15 000÷3=5000; 18÷6000=0.003 mm=3 µm;
24÷400=0.06 mm=60 µm; 0.1 mm=100 µm, ÷1=10². Every "unconverted gives…" line is right. Rung 4's compare
points match the examiner shape, and "a list about one cell caps at 2" is in the reject list. "Learn it" on the
equation is correct: there is no biology equation sheet.

### REQUIRED

| # | lesson · routes | where | OLD → NEW | reason | citation |
|---|---|---|---|---|---|
| S-2 | eukaryotes-prokaryotes · all | every "cheek cell" used as the 20 µm reference cell: header `ks3-bigq`; `s-hook` h2 and p; `hookFig` label `'cheek cell ≈ 20 µm'` and its alt; the hookFig `K.fig` alt; `hookOptions[0]`; Foundation `cfQuestions` Q1 `head` | Replace "cheek cell" with "liver cell" throughout, keeping every number. bigq: "A bacterium and one of your cheek cells are both alive…" → "A bacterium and one of your liver cells are both alive…". h2: "A cheek cell and a bacterium, drawn to the same scale." → "A liver cell and a bacterium, drawn to the same scale." p: "The cheek cell is about 20 µm across." → "The liver cell is about 20 µm across." Fig label: `'cheek cell ≈ 20 µm'` → `'liver cell ≈ 20 µm'`. Alt: "A cheek cell about 20 micrometres…" → "A liver cell about 20 micrometres…". K.fig alt: "A cheek cell and a bacterium drawn to the same scale" → "A liver cell and a bacterium drawn to the same scale". Option: "Inside a nucleus, like the cheek cell, only smaller" → "Inside a nucleus, like the liver cell, only smaller". CFIFA Q1: "A drawing of a cheek cell is 40 mm wide. The real cell is 0.02 mm wide." → "A drawing of a liver cell is 40 mm wide. The real cell is 0.02 mm wide." | Human cheek (buccal epithelial) cells are large, flat squamous cells, typically about 50–60 µm across, not 20 µm. The page draws one "to scale" at 20 µm and says it is "a typical animal cell". The ×10 bacterium comparison, the 10 µm scale bar and the CFIFA check line all depend on 20 µm, so swap the cell, not the number. Liver cells (about 20–30 µm) fit every figure as drawn. Cheek cells are what pupils see in RP1, so a wrong size here is a size they will reuse. | 4.1.1.1 ("scale and size of cells"); 4.1.1.5 / RP1 context. Confidence: high that buccal cells are well over 20 µm; the exact typical value varies by source (about 40–80 µm). |

### ADVISORY

| # | where | note |
|---|---|---|
| A-4 | `FIT[1].why[0]` (pick ×10 on ribosomes across a bacterium) | "Did you divide 2 by 20 without converting? 2 µm is 2000 nm." Dividing 2 by 20 gives 0.1, not 10, so this diagnosis does not match the pick. Suggest: "×10 would make each ribosome 200 nm. Convert first: 2 µm = 2000 nm, and 2000 ÷ 20 = 100." |
| A-5 | builder `PARTS.loop.why` | "An animal cell's DNA is in chromosomes inside its nucleus, not one loose loop." Fine at GCSE. Mitochondrial DNA is a loop, but that is not examinable. No change needed. |
| A-6 | bank (frozen) | q4 wx3 (imprecise reasoning, C37) and q5 (flagellum, not in spec) are served in the practice bank on all routes. Neither is wrong, and neither is a rung. Leave as is. |

**Frozen items still served that should be withheld:** none.
**For Mide:** none.
**Verdict: SCIENCE PASS AFTER REQUIRED CHANGES** (S-2).

---

## 3. enzymes — AQA 4.2.2.1 + RP4 (8464) / RP5 (8461)

**Route-by-route.** The RP number follows the route: the eyebrow and key-note label say 8464 · RP4 on Combined
and 8461 · RP5 on Triple. That is correct; the frozen "RP3" is not displayed anywhere. CFIFA and rung 2 switch on
`isHigher`, which I confirmed live. Bank: 4 items (q2–q5) on all routes. q1 (80 °C, whose wx1 says the rate
increases above the optimum) is withheld by `batch_2.py` B2-W1 and also by the lesson's own filter. It is
absent on all four routes, which is correct.

**Verified correct.** Lock and key: complementary shape, enzyme unchanged and reused. Heated to 60 °C means
denatured, and cooling does not restore it. The think-again options and reveal (cold slows, it does not denature).
Sketch A rises to the optimum and then falls steeply; all four sketch replies are true. The RP method matches the
spec: iodine every 30 s, water bath, end point when the iodine stays orange-brown. Risks. Variables sort.
"rate = 1 ÷ time, s⁻¹". All CFIFA and rung arithmetic and significant figures: 1/75=0.013; 105 s → 0.0095,
and 1/1.45=0.69; 1/90=0.011; 150 s → 0.0067, with 0.4 being 60× too big; 1/0.0125=80 s; 195 s → 0.0051;
1/60=0.017; 240 s → 0.0042; 80 s → 0.0125; 1/120=0.0083. Rung 3 chain and herrings. Rung 4 levels,
points and rejects. The key fact. The authored key-note lines.

### REQUIRED

| # | lesson · routes | where | OLD → NEW | reason | citation |
|---|---|---|---|---|---|
| S-3 | enzymes · all | logic constant `TRUE_T` (simulated practical) | `const TRUE_T = { 4: 900, 5: 165, 6: 75, 7: 105, 8: 255 };` → `const TRUE_T = { 4: 900, 5: 165, 6: 60, 7: 105, 8: 255 };` | **The simulated data can put the optimum at pH 7 while the verdict says pH 6.** The state starts at `ph: 6` and `runN: 0`, so a pupil who mixes at the default pH 6 first gets `NOISE[0]=+18`: 93 s rounds up to 120 s. If pH 7 is next, `NOISE[1]=−22` gives 83 s, which rounds up to 90 s. The means become pH 6 = (120+90)/2 = **105 s** and pH 7 = (90+120+90)/3 = **100 s**. The plotted rate is then higher at pH 7 (0.0100 vs 0.0095 s⁻¹), but `shapeTexts` tells the pupil "the rate is fastest near pH 6", and the graph's alt text says "highest at pH 6". With 60 s at pH 6, every noise value gives 60 or 90 s, so the pH 6 mean is 75 or 90 s. The pH 7 mean is never below 100 s, so the peak is always pH 6. The anomaly (Group C, 240 s) stays obvious, and the mean task is unchanged. An alternative is to derive the shape text from the computed means. | Internal consistency of a verdict. 4.2.2.1 (optimum pH) |

### ADVISORY

| # | where | note |
|---|---|---|
| A-7 | `plot()` | pH 4 ("not digested in 10 min") is plotted at rate 0, and the best-fit curve runs into it. The true rate there is below 1/600 s⁻¹, not zero. Consider a hollow marker at the axis labelled "< 0.0017" with the curve stopping at pH 5, or keep it and say so in `legal`. |
| A-8 | spotting-tile `wells` style | Unsampled wells are drawn white, but method step 1 loads every well with iodine (orange-brown). Drawing unsampled wells pale orange-brown would match the method. The `rig()` figure already does this. |
| A-9 | rung 1 (frozen q5) feedback | wx3, "Active sites … reform automatically because the enzyme is unchanged", is self-contradictory (examination C33), but it is not wrong in its conclusion. Keep it, or apply a generated-copy ruling if the commander allows. |
| A-10 | bank (frozen q3 wx1) | "Amylase is produced in the mouth AND pancreas": AQA credits salivary glands, pancreas and small intestine. This is imprecise, not wrong. Keep. |
| A-11 | explainer 1 | "the active site is the lock, the substrate is the key". This is acceptable. AQA mark schemes usually say "enzyme = lock". Either is credited. |

**Frozen items still served that should be withheld:** none. q1 is already withheld (B2-W1); confirmed absent live on all four routes.
**For Mide:** none on AQA sources. B2-W1 (q1 wx1) is already on Mide's list via DEPARTURES.
**Verdict: SCIENCE PASS AFTER REQUIRED CHANGES** (S-3).

---

## 4. carbon-cycle — AQA 4.7.2.2 (+4.7.3.3–4.7.3.5)

**Route-by-route.** All four routes are identical apart from the 8461/8464 label. That is correct: the pack's Higher-only human-impact
field is taught as base, and the not-in-spec "short-term vs geological cycle" sentence is not taught. Bank: q1–q2 on all
routes; nothing needs withholding.

**Verified correct.** Every arrow in the 9-arrow diagram has the right direction (A air→plants, B plants→air,
C plants→animals, D animals→air, E/F to dead matter, G dead→air, H dead→fossil, I fossil→air). The
label `accept` lists are right ("Decay by microorganisms" or "Respiration" for G). All six trace steps, their
distractor replies and reveals are correct. Feeding is taught as carbon compounds, not CO₂, which fixes examination R3. The
feeding and decomposers-respire confront boxes. The plants-in-the-dark predict (CO₂ rises). The sort bins.
Rung 2 pond diagram (X feeding, Y decomposer respiration). Rung 3 chain. Rung 4 levels and points. The key fact.

### REQUIRED

| # | lesson · routes | where | OLD → NEW | reason | citation |
|---|---|---|---|---|---|
| S-4 | carbon-cycle · all | `s-sort` Ks4Sort `done-note` | "Only photosynthesis takes carbon dioxide out of the air. Respiration, by plants, animals and decomposers, and combustion put it back. Feeding and fossilisation move carbon between other stores." → "Of these processes, only photosynthesis takes carbon dioxide out of the air. Respiration, by plants, animals and decomposers, and combustion put it back. Feeding and fossilisation move carbon between other stores." | As a general statement this is false: carbon dioxide also dissolves in the oceans. That is base chemistry on every route (8464 5.9.1.2 / 5.9.1.4). It also contradicts the verbatim key note on the same page, line 01: "CO₂ removed by: photosynthesis, dissolution in oceans." Scoping it to the sorted processes makes it true. The diagram-scoped "Only arrow A…" status line is already correct and stays. | 8464 5.9.1.2, 5.9.1.4; frozen key_note |

### ADVISORY

| # | where | note |
|---|---|---|
| A-12 | explainer 2, first sentence | "For most of history, carbon dioxide was taken out of the air about as fast as it was put back." Over Earth's history, atmospheric CO₂ fell greatly (chemistry 5.9.1.4, "How carbon dioxide decreased"). The sentence is only true of the pre-industrial millennia. Suggest: "For thousands of years before people burned fossil fuels on a large scale, carbon dioxide was taken out of the air about as fast as it was put back." |
| A-13 | explainer 2, second sentence | "Humans are now adding it faster than photosynthesis can remove it." This is acceptable at GCSE. "faster than natural processes can remove it" would sit better beside the key note's ocean line. |
| A-14 | trace step 5 (author's ⚑) | "sinks into the mud, which buries it before decomposers can break it down": a fair GCSE simplification of fossilisation (waterlogged, low-oxygen conditions slow decay). No change needed. |
| A-15 | trace step 1 / feed box | "only photosynthesis can [build CO₂ into a living thing]": chemosynthesis is ignored. This is the right level for GCSE. No change. |

**Frozen items still served that should be withheld:** none. q1 and q2 are correct on all routes.
**For Mide:** none. 8461 and 8464 4.7.2.2 are identical.
**Verdict: SCIENCE PASS AFTER REQUIRED CHANGES** (S-4).

---

## Summary

| lesson | REQUIRED | verdict |
|---|---|---|
| chromosomes-mitosis | S-1 (chain prompt says "mitosis" for the cell cycle) | SCIENCE PASS AFTER REQUIRED CHANGES |
| eukaryotes-prokaryotes | S-2 (a 20 µm "cheek cell" is not a cheek cell; rename it liver cell) | SCIENCE PASS AFTER REQUIRED CHANGES |
| enzymes | S-3 (simulated data can peak at pH 7 while the verdict says pH 6; set `TRUE_T[6]` to 60) | SCIENCE PASS AFTER REQUIRED CHANGES |
| carbon-cycle | S-4 ("only photosynthesis takes CO₂ out of the air" contradicts the page's own key note) | SCIENCE PASS AFTER REQUIRED CHANGES |

No frozen item needs to be newly withheld in this group. No HT or separate-science content leaks onto the wrong route.
Nothing here needs Mide's ruling on conflicting AQA sources.
