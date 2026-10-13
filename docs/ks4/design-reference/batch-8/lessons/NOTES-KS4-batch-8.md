# KS4 batch 8: 16 lessons

Written from `docs/ks4/packs/batch-8/` (00-BRIEF.md, FLAGS.md, 04-checked-science-source/, 05-diagram-library/README.md), main, 8 Oct 2026. The V6 prompt’s updates win over the pack. No lesson text comes from old site data: these pages don’t load `ks4-source.js`; every quiz item is written into its lesson.

Batch 7 (and the batch 6 transpiration fix from V5) was already finished before this batch: `Design's Output/Batch 7/lessons/` and `Design's Output/Batch 6/lessons/ks4-biology-4.2.3.2-transpiration.dc.html`.

## Files and routes

One runnable `.dc.html` per lesson in `Batch 8/lessons/`, named `ks4-biology-<spec>-<slug>`. Where 8461 and 8464 number a point differently, the file name uses the 8461 (Biology) number and the header shows both. Order is the prompt’s.

1. Homeostasis · `ks4-biology-4.5.1-homeostasis` · CF CH TF TH · Higher layer CH TH
2. The nervous system · `ks4-biology-4.5.2.1-nervous-system` · CF CH TF TH
3. Reflex actions · `ks4-biology-4.5.2.1-reflex-actions` · CF CH TF TH
4. Reaction time · `ks4-biology-4.5.2.1-reaction-time` · CF CH TF TH · RP 6 (Combined) / RP 7 (Biology) · calculates
5. The brain · `ks4-biology-4.5.2.2-the-brain` · TF TH · Triple Higher layer TH
6. The eye · `ks4-biology-4.5.2.3-the-eye` · TF TH
7. Defects of the eye · `ks4-biology-4.5.2.3-defects-of-the-eye` · TF TH
8. Thermoregulation · `ks4-biology-4.5.2.4-thermoregulation` · TF TH · Triple Higher layer TH
9. The endocrine system · `ks4-biology-4.5.3.1-endocrine-system` · CF CH TF TH · Higher layer CH TH
10. Blood glucose and diabetes · `ks4-biology-4.5.3.2-blood-glucose-diabetes` · CF CH TF TH · Higher layer CH TH
11. Hormones in human reproduction · `ks4-biology-4.5.3.4-human-reproduction-hormones` · CF CH TF TH · Higher layer CH TH
12. Contraception and fertility · `ks4-biology-4.5.3.5-contraception-fertility` · CF CH TF TH · Higher layer CH TH (infertility, IVF)
13. Sexual and asexual reproduction · `ks4-biology-4.6.1.1-sexual-asexual-reproduction` · CF CH TF TH · Triple pointer TF TH
14. Meiosis · `ks4-biology-4.6.1.2-meiosis` · CF CH TF TH (not TF TH as the site ships, MEI-F1)
15. Advantages of sexual and asexual reproduction · `ks4-biology-4.6.1.3-advantages-sexual-asexual` · TF TH
16. DNA and the genome · `ks4-biology-4.6.1.4-dna-genome` · CF CH TF TH · Triple pointer TF TH

The three 4.5.2.1 lessons share a spec number, so the slug tells them apart (as aerobic and anaerobic did in batch 7). Triple-only pages offer the two Triple routes in the picker.

## Page order (every lesson)

Header (AQA ref, route chips, RP chip on reaction time, route picker) → Start here (`Ks4Guess`) → video slot → two teaching sections, each with a figure and one interaction, route layers as `sc-if` → on reaction time only: method block, CFIFA (`Ks4Cfifa`) and Step 1 / Step 2 (`Ks4Steps`) → Think again (`Ks4Choice`) → Sort (`Ks4Sort`) → command words → key fact → exam ladder (`Ks4Practice`) → key note → practice set (`Ks4QuizBank`) → end. No examiner tips: none approved.

## Shared blocks

Copied from the batch-7 delivery (the newest) into `lessons/` so each page runs on its own: Ks4Triangle, Ks4Guess, Ks4Steps, Ks4Practice, Ks4Chain, Ks4Write, Ks4Chrome, Ks4Cfifa, Ks4Choice, Ks4Sort, Ks4KeyNote, Ks4QuizBank, Ks4End, Ks4Video, ks4-lib.js, ks4-diagrams.js, ks4-theme.css, support.js. No `_ds` inside; pages link `../../_ds/…`.

One change: **Ks4Steps** takes an optional `eyebrow` prop. Its default (“Worked example · two equations · one line at a time”) is unchanged; reaction time passes “Worked example · table, then mean · one line at a time”, because its chain is a table read then a mean, not two equations. Ks4Triangle is copied but unused this batch (no equation needs one).

## Rules 1–4

- **Rule 1.** Every opener is “If you had to guess, …?” with exactly two options from everyday life, following each brief’s access note: walking in a heatwave, a hot pan handle, an oven tray, catching a dropped phone, spinning round, walking into a dark room, who wears glasses for what, a red face after a sprint, a slammed door, a skipped lunch, a period coming once a month, many contraceptive methods, a plant cutting, getting features from each parent, a crop field beside a meadow, “your mother’s nose”. Titles and scenes set up the situation without stating the answer (the heatwave scene doesn’t mention sweat; the sprint scene doesn’t mention blood vessels). The wrong option’s reply is encouraging and goes straight into the teaching.
- **Rule 2.** No formula triangles this batch. Every lesson’s “Equations that need formula triangles” line says none, and the lane ruled out reaction time’s optional t = √(2d ÷ g) (F1), so d = ½ g t² appears nowhere. The mean of repeats is shown in a method block as “mean = total of the repeats ÷ number of repeats”, labelled “Written out”, no chip, and the same line is the Formula step of every CFIFA. “Learn this one” appears nowhere.
- **Rule 3.** Reaction time only. The method block teaches random error and the mean, ms ÷ 1000 → s, and m × 100 / mm ÷ 10 → cm for the table. Then CFIFA: worked “nothing to convert” (0.20, 0.23, 0.20 s → 0.21 s) and “convert first” (240, 260, 280 ms → 0.26 s) before two attempts (0.31, 0.27, 0.29 s → 0.29 s; 180, 220, 230 ms → 0.21 s). The table-then-mean chain gets a worked Step 1 / Step 2 (0.20, 0.25, 0.30 m → 20, 25, 30 cm → 0.20, 0.23, 0.25 s → 0.23 s) and an attempt (150, 200, 250 mm → 0.17, 0.20, 0.23 s → 0.20 s), CFIFA on each step, all before the ladder. Blood glucose’s FIFA is taught as a process, not a calculation, and has no CFIFA (BLOOD-GLUCOSE-DIABETES-F5).
- **Rule 4.** Ladder 2 · 2 · 2 · 1 on every page and route; rung 4 is one 4- or 6-mark answer (6 marks on reflex, reaction time, the eye, defects, meiosis, advantages, and on the Higher/Triple Higher copies of brain, thermoregulation, endocrine, blood glucose, reproduction, contraception). Practice set: five per route, checked by loading all 52 page–route pairs (no console errors, five questions each). Where a layer swaps items, the count stays the same.

## Quiz items (practice set, five per route)

“Rebuilt” = same stem and key, with the flagged option or explanation replaced by FLAGS’ own wording. Options are shuffled by `KS4.item()`.

- 1 Homeostasis: CF TF q2 verbatim + 4 new (receptor, effector, three conditions, nervous or chemical); CH TH q1 q2 q3 verbatim + 2 new (receptor, effector)
- 2 Nervous system: q1 q2 verbatim + 3 new (CNS, effector response, synapse data table); q3 not used (F2)
- 3 Reflex actions: q1 q2 q3 verbatim + 2 new (where the two synapses are, why reflexes matter)
- 4 Reaction time: q2 verbatim + 4 new (table read with units, mean, control variable, ethics); q1 not used (F1 dropped)
- 5 The brain: TF q1 verbatim + 4 new (medulla, cortex function, neurones, folded outer layer); TH q1 q2 verbatim + 3 new (medulla, cortex, MRI)
- 6 The eye: q1 q2 verbatim + 3 new (sclera, retina, optic nerve)
- 7 Defects: q1 rebuilt (wx1, F1), q2 verbatim + 3 new (reading a ray diagram, convex lens, replacement lens)
- 8 Thermoregulation: TF q1 rebuilt (wx2, F1), q2 verbatim + 3 new (too-cold responses, the centre, its receptors); TH q1 rebuilt, q2 q3 verbatim + 2 new (too cold, receptors)
- 9 Endocrine: CF TF q1 q3 verbatim + 3 new (pituitary position, master gland, target organ); CH TH q1 q2 q3 verbatim + 2 new (pituitary position, thyroxine feedback diagram)
- 10 Blood glucose: q1 q2 q3 verbatim on every route + 2 new: graph data and insulin’s first effect (CF TF), graph data and glucagon (CH TH)
- 11 Reproduction: CF TF q1 q2 verbatim + 3 new (oestrogen’s base role with no “second half” distractor, testosterone, pituitary); CH TH q1 q2 q3 verbatim + 2 new (pituitary, LH peak on a graph)
- 12 Contraception: CF TF q1 verbatim, q3 rebuilt + 3 new (patch, IUD, spermicide); CH TH q1 q2 verbatim, q3 rebuilt + 2 new (IUD, multiple births)
- 13 Sexual and asexual: CF CH q3 verbatim + 4 new (plant gametes, mitosis only, variety, clone); TF TH q1 q3 verbatim + 3 new; q2 not used (SAR-F2)
- 14 Meiosis: q1 rebuilt (wx2, MEI-F4) + 4 new (where, divisions and gametes, all different, after fertilisation); q2 not used (MEI-F5)
- 15 Advantages: q1 verbatim, q2 rebuilt (wx2, ADV-F2) + 3 new (malaria, selective breeding, a given-information item)
- 16 DNA and the genome: q2 verbatim, q3 rebuilt (wx2 and wx3 swapped, DNA-F3) + 3 new (genome, DNA, migration patterns); q1 not used (12.1 below)

## Science flags

**G · Global**
- G1. Arrows, subscripts and superscripts inside JS-built text (quiz, ladder, sort, key note) are plain characters and fall back to a system font, as in batches 5–7. My new text avoids arrows; verbatim items keep their own glyphs (“→”, “°C”).
- G2. Made-up teaching data, labelled on each page: synapse response times, ruler catches, the bar chart, the blood-glucose curves, the hormone curves, the population pictures.
- G3. Prev/next follow this batch’s order, skipping pages a route doesn’t have: on Combined, Reaction time → Endocrine system and Meiosis → DNA and the genome. Lesson 1 links back to Metabolism (batch 7). DNA and the genome has no Next: 4.6.2 onwards isn’t in batches 4–8.
- G4. Every figure is mine, in the ks4-diagrams style. `reflex_arc()`, `body_glands()`, `cycle_clock()` and `dna_schematic()` are Python and weren’t ported. FLAGS win where the diagram README disagrees: six glands, not four; no hairs in the skin figure (THERMOREGULATION-F4); no MRI/CT/PET line on TF.
- G5. Sibling overlap, pointers not re-teaching: nervous vs chemical control → Nervous system / Endocrine system; sweating and shivering → Thermoregulation; glucagon → Blood glucose; drugs and reaction time → Reaction time; pupil reflex → The eye; the pathway → Nervous system; hormones at work → Blood glucose, Reproduction; hormones in contraception → Reproduction; advantages → Advantages (Triple); halving → Meiosis; nucleotides and pairing → DNA structure (sibling).
- G6. Mide’s bar: two teaching sections per page. Off-spec detail in the sources is left out of my text throughout: positive feedback, myelin, SSRIs, one-way synapses, d = ½ g t², EEG, fovea, presbyopia, hairs, adrenaline as a warming response, ADH, tropic hormones, beta and alpha cells, metformin, corpus luteum, emergency contraception, PGD, meiosis stages, crossing over, triplet code.

**1 · Homeostasis**
- 1.1 Base teaches “responses which restore optimum levels” with no name; “negative feedback” and the loop diagram are the CH TH layer (F1). q1 and q3 are CH TH only.
- 1.2 Positive feedback not shown (F2). Higher wording is the spec’s “interpret and explain simple diagrams”.
- 1.3 Pancreas named as a coordination centre (spec list); glucagon is a pointer only (F3).
- 1.4 “Control may involve nervous responses or chemical responses”, with pointers to the next two lessons (F4).
- 1.5 “Much above 40 °C enzymes begin to denature, and this can be fatal” (F5). No osmoreceptors, no “proportional signal”.
- 1.6 The break-a-part instrument uses a temperature example with “brain” and “sweat glands” as named examples only (pack note).

**2 · The nervous system**
- 2.1 No Higher layer on any route; `higher` not shown (F1). Drugs: one pointer line, “some drugs and alcohol slow the nervous system and increase reaction time”.
- 2.2 q3 not used; one-way transmission not taught (F2).
- 2.3 q2 used as written; no synapse timing figure (F3).
- 2.4 Data items (F4): a made-up synapse-number table in the bank, a hand-to-foot comparison on rung 2.
- 2.5 Myelin dropped (F1).

**3 · Reflex actions**
- 3.1 Both synapses are steps in the build-the-arc instrument, and in the sort, ladder and key note (F1).
- 3.2 The rule is the spec sentence; hand withdrawal goes through the spinal cord; blink and pupil reflexes go through “an unconscious part of the brain, never the conscious part” (F2).
- 3.3 “Fewer synapses” is taught as a reason, so q1 is usable as written (F3).
- 3.4 “Several times faster”, no ratio and no reflex times (F4).
- 3.5 q3 used as a Recall item in the bank; its distractors name brain regions (pack note).

**4 · Reaction time**
- 4.1 The free-fall calculation is left out, as the lane ruled (F1); q1 is not used. The conversion table is given, not derived.
- 4.2 RP chip “Required practical 6” on CF CH, “Biology required practical 7” on TF TH (F5).
- 4.3 Added (F2): IV, DV and control cards and a sort; an ethics card (informed consent, right to withdraw; for caffeine a small legal dose, exclude heart conditions or caffeine sensitivity); a table of repeats and a bar chart of means, since the factor is categorical.
- 4.4 AQA’s wording on random error and means; “reliable” not in my text (F3); q2 used as written.
- 4.5 “Caffeine is a stimulant: it speeds up the nervous system” (F4).
- 4.6 Both typical-time statements given: 0.2–0.9 s (physics spec) and about 0.2–0.3 s for a simple stimulus (pack note).
- 4.7 Conversion-table values are t = √(2d ÷ g) with g = 9.8 m/s², rounded to 2 dp (5 cm 0.10 s … 45 cm 0.30 s). Code to check the rounding.
- 4.8 The sim factor is distraction; the planning answer (rung 4) is caffeine, the usual 6-mark context.

**5 · The brain**
- 5.1 TF: regions and functions only. Mapping (damage, electrical stimulation, MRI) and the difficulties are a TH-only layer; q2 is TH only (F1).
- 5.2 Re-cut (F2): “damaged neurones are not easily repaired or replaced”; “taking a sample of brain tissue, or operating, risks damaging other parts of the brain”. q2’s key (“cannot regenerate”) kept verbatim on TH, as F2 allows.
- 5.3 “Cerebral cortex” alone, never “(cerebrum)”; no memory trick (F3).
- 5.4 Side-view brain with the three regions labelled; the page opens with “controls complex behaviour” (F4).
- 5.5 Functions as AQA lists them: cortex consciousness, intelligence, memory and language; cerebellum muscle coordination (balance added); medulla unconscious activities such as heartbeat and breathing.

**6 · The eye**
- 6.1 Sclera labelled and taught: tough, white outer layer that protects the eye and keeps its shape (F1).
- 6.2 No fovea, rods or cones (F2).
- 6.3 Pupil reflex gives both muscle sets: circular contract and radial relax in bright light, and the reverse in dim light (pack note).
- 6.4 Accommodation in the spec’s words: contract, loosen, thicker; relax, pulled tight, thin.
- 6.5 The rung-4 context (cinema to sunlight) combines the pupil reflex and accommodation; my wording.

**7 · Defects of the eye**
- 7.1 q1 used only with F1’s replacement wx1.
- 7.2 Hard and soft contact lenses and a replacement lens added; one benefit and one risk each are my wording; Code to check (F2).
- 7.3 Four ray diagrams in one instrument: myopia and hyperopia, each uncorrected and corrected, plus the wrong lens for each. A ray-diagram reading check sits on the page, and the bank has a ray-diagram item in words (F3). Ks4Practice and Ks4QuizBank are text-only, so neither can carry a drawn diagram.
- 7.4 Laser surgery “usually removes the need for glasses or contact lenses” (F4). No lens powers, no presbyopia.
- 7.5 Causes (eyeball too long or lens too curved; too short or too flat) are from the source; the spec doesn’t give causes.

**8 · Thermoregulation**
- 8.1 q1 used only with F1’s replacement wx2.
- 8.2 TF: the responses plus “both transfer energy from the skin to the environment”. The step-by-step explanations in context (runner, swimmer) are the TH layer, and so are q3, rung 3’s shivering chain and rung 4’s 6-marker (F2).
- 8.3 “Above about 40 °C enzymes start to denature”; “below about 35 °C is hypothermia” (F3).
- 8.4 No hairs, no adrenaline (F4).
- 8.5 TH layer leads with “explain in a given context”, and doesn’t ask for negative feedback (F5).
- 8.6 “Thermoregulatory centre in the brain (the hypothalamus)”: the spec’s term, with the other name once (pack note).

**9 · The endocrine system**
- 9.1 On CF TF the thyroid and adrenal notes give position only; what thyroxine and adrenaline do, and glucagon, appear only in the CH TH notes and layer (F1). q2 is CH TH only.
- 9.2 CH TH layer: a thyroxine negative-feedback loop you push both ways, with a bank item that reads it (F2). TSH is named on the diagram as the pituitary’s hormone, as exam diagrams name it; the spec doesn’t.
- 9.3 ADH dropped; the tropic-hormone list not used (F3).
- 9.4 Six glands on female and male outlines (README correction). The pituitary’s FSH and LH are named on the base copy (4.5.3.3/4.5.3.4 base).
- 9.5 Race graph: the nerve effect is a fast spike; the hormone effect starts later and lasts longer. Schematic, no numbers.

**10 · Blood glucose and diabetes**
- 10.1 CF TF: one arm (insulin) ending “back to normal”. Glucagon, the two-arm cycle and “negative feedback” are the CH TH layer (F1).
- 10.2 Graph block on every route: no diabetes vs Type 1 after a glucose drink, plus an insulin injection at 3 h; bank and rung-2 items read it (F2). Values made up, in mg per 100 cm³; the person without diabetes is back to normal by 2 h. The obesity line (WS 1.3) is one sentence; there is no data item for it.
- 10.3 Insulin taught as two steps: glucose moves from the blood into cells; in liver and muscle cells excess glucose becomes glycogen (F3). Verbatim q1’s key covers only the second step; it is not the only statement of it.
- 10.4 Type 2: “a carbohydrate-controlled diet and an exercise regime”; no metformin, no gluconeogenesis (F4).
- 10.5 FIFA taught as the instrument’s process steps; no CFIFA (F5).
- 10.6 Verbatim q1 and q3 keep “beta cells”, “autoimmune” and “lifestyle-related”; my text uses none of them.

**11 · Hormones in human reproduction**
- 11.1 CF TF: each hormone’s role and source; the interactions are the CH TH layer (F1).
- 11.2 CH TH: four schematic hormone curves over 28 days with ovulation marked, a pick-a-hormone reading, and a bank item on the LH peak (F2).
- 11.3 Re-cut (F3): hair goes under “reproductive hormones cause secondary sex characteristics”, not under oestrogen; days 1–4 shed, 5–13 rebuilt, 14 ovulation, 15–28 maintained; “oestrogen inhibits FSH and stimulates LH”, unqualified.
- 11.4 q2 kept verbatim (F4).
- 11.5 q3 CH TH only; CF TF get a new oestrogen item without the “second half” distractor (F5).
- 11.6 Progesterone’s source is given as “the ovary”; the corpus luteum is off-spec and not in my text (verbatim q1 and q2 mention it). Code to check.
- 11.7 Age-appropriate: hormones, the lining and ovulation only; nothing about intercourse.

**12 · Contraception and fertility**
- 12.1 CF TF are contraception only; the whole infertility half (FSH and LH drug, IVF, its drawbacks) is the CH TH layer; q2 is CH TH only (F1).
- 12.2 q3 rebuilt (F2): option 1 is now “It forms a barrier over the cervix” with a new wx1; wx3 replaced as well, as F2 calls it loose (“the pill doesn’t make the lining shed more often”).
- 12.3 All seven spec categories in the instrument, in spec words: skin patch, IUDs preventing implantation or releasing a hormone, spermicidal agents, abstaining “when an egg may be in the oviduct” (F3). Multiple births “a risk to both the babies and the mother”.
- 12.4 “Condoms (male and female) are the only contraceptives that also protect against STIs”; “one or two embryos inserted into the uterus” (F4).
- 12.5 Not sure, so Code to check: the “easy to stop using” filter line (an implant or IUD is removed by a doctor; sterilisation is usually permanent) and rung 4’s “hormonal methods may have side effects” are mine, not spec text. The ethics line is the spec’s WS 1.3 framing only.
- 12.6 Age-appropriate: each method is named and described by what it blocks, in AQA’s words. Nothing on how a method is used beyond that. No emergency contraception, PGD, success figures or injection intervals.

**13 · Sexual and asexual reproduction**
- 13.1 Advantages and disadvantages are left to Advantages; TF TH see one tagged pointer line; q1 TF TH only (SAR-F1).
- 13.2 q2 not used (SAR-F2); halving is a pointer to Meiosis.
- 13.3 Meiosis stages, crossing over and the `higher` field cut (SAR-F3, F4).
- 13.4 Pollen and egg cells (SAR-F5). “Plants and fungi reproduce asexually by mitosis; bacteria multiply by simple cell division (binary fission)” (SAR-F6).
- 13.5 The predict-then-reveal figure is a model: coloured bars stand for genetic information.

**14 · Meiosis**
- 14.1 One page for all four routes; no “not in Combined” note (MEI-F1).
- 14.2 The spec’s sequence only, no stage names; the model shows 2 pairs of chromosomes (WS 1.2) (MEI-F2).
- 14.3 “Each chromosome is copied”; never strands (MEI-F3).
- 14.4 q1 used with MEI-F4’s replacement wx2; q2 not used (MEI-F5).
- 14.5 “Pollen and egg cells” wherever plants come up (MEI-F6). Fertilisation, mitosis, more cells and differentiation are the stepper’s last three steps (MEI-F7).
- 14.6 The four model gametes are drawn with small colour tips to show they all differ. No mechanism is named. Rung 2 uses the dog’s 78 chromosomes (78 ÷ 2 = 39).

**15 · Advantages of sexual and asexual reproduction**
- 15.1 Malarial parasites, fungal spores, strawberry runners, daffodil bulb division and selective breeding all taught, in spec words (ADV-F1).
- 15.2 q2 used with ADV-F2’s replacement wx2.
- 15.3 No Higher layer; `higher` cut (ADV-F3).
- 15.4 Aphids (rung 4) and a water flea (bank) appear only as given-information contexts, never as recall (ADV-F4). The water-flea pattern (asexual when food is plentiful, sexual when the pond dries) is my context; Code to check.
- 15.5 “Bacteria split in two by binary fission” in the bacteria item (ADV-F5). The spec lists advantages only, so the page frames each kind by its advantages and the conditions that favour it.

**16 · DNA and the genome**
- 16.1 Nucleotides and complementary pairing are left to the sibling `dna-structure` (TF TH): one tagged Triple pointer line, with no link because that page isn’t in batches 4–8 (DNA-F1). So q1 (pairing, TH) is not used, and the bank is the same on every route. If Code would rather teach pairing on TH here, q1 can swap in for the DNA-description item.
- 16.2 Nothing on CH from `higher`; triplet code and non-coding DNA not taught here (DNA-F2).
- 16.3 q3 used with wx2 and wx3 swapped (DNA-F3).
- 16.4 The spec’s three importance points, including human migration patterns, with a bank item on it (DNA-F4). No forensic, personalised-medicine or base-pair figures in my text; verbatim q3 keeps “~3 billion base pairs”.
- 16.5 Zoom levels: cell, nucleus, chromosome, DNA (double helix), gene, protein. Schematic.

## Not done / for Code

- Videos: `KS4.VIDEOS` is empty, so the slot stays hidden.
- No examiner tips: none approved.
- Links to batches 6 and 7 use `../../Batch 6|7/lessons/…`.
- Dark mode uses the existing remap; SVG plates stay cream.
