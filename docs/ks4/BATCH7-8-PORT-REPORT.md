# KS4 batches 7 and 8: port report

Design's batches 7 and 8 (32 biology lessons, delivered 8 Oct 2026), ported the way batches 4–6 were: her lessons,
her blocks, her words, with every change a named ruling in `ks4_batch_rulings.py` that fails the build if its target
text is not found the expected number of times. Her files sit verbatim in `docs/ks4/design-reference/batch-7/` and
`batch-8/` (`MD5SUMS` beside each). Opus led and audited; Sonnet built. One worktree
(`mrbadmus-worktrees/ks4-batch7`), one push per batch.

How the science was checked: four independent Opus examiners read all 32 files against the AQA 8461/8464 spec text,
the batch pack (`docs/ks4/packs/batch-7|8/`, FLAGS and examination notes) and Design's NOTES, every pupil-visible
string on every route layer. The lead ruled on each finding. Settled science was ruled here; nothing in this report
needs Mide's examiner judgement unless it is listed under "For Mide".

---

## Batch 7: infection and response, bioenergetics (16 lessons, 59 pages)

### Files and routes

| # | lesson (live slug) | topic | routes |
|---|---|---|---|
| 1 | communicable-diseases-defence | infection-response | CF CH TF TH |
| 2 | viral-diseases | infection-response | CF CH TF TH |
| 3 | bacterial-diseases | infection-response | CF CH TF TH |
| 4 | fungal-protist-diseases | infection-response | CF CH TF TH |
| 5 | vaccination | infection-response | CF CH TF TH |
| 6 | antibiotics-painkillers | infection-response | CF CH TF TH |
| 7 | drug-discovery-development | infection-response | CF CH TF TH |
| 8 | monoclonal-antibodies | infection-response | TH |
| 9 | plant-disease-detection-defence | infection-response | TF TH |
| 10 | photosynthesis | bioenergetics | CF CH TF TH |
| 11 | rate-of-photosynthesis | bioenergetics | CF CH TF TH |
| 12 | uses-of-glucose | bioenergetics | CF CH TF TH |
| 13 | aerobic-respiration | bioenergetics | CF CH TF TH |
| 14 | anaerobic-respiration | bioenergetics | CF CH TF TH |
| 15 | response-to-exercise | bioenergetics | CF CH TF TH |
| 16 | metabolism | bioenergetics | CF CH TF TH |

59 pages per tree (`combined/` + `triple/`, and the same 59 in `mrbadmus_site/`). They replace the old generated
pages at the same URLs. New files: `ks4_lessons/batch_7.py`, `batch7_ext.js` (a copy of the fixed batch-6 subscript
script: SVG tspans, added SVGs scanned, handles ₆ and ₁₂), `frozen_batch-7.json`, `ks4_batch-7_manifest.json`,
`shared/ks4-{source,lesson,ext}-batch-7.*`.

Her shared blocks: byte-identical to batch 6's except `Ks4Triangle` (two lines: `fixed` now also read from the top
item, for the 1 in relative light intensity = 1 ÷ d²). Batch 7 registers its own block set.

### Port mechanics (not science)

- **B7-<slug>-CHIP** (16): every page returns a fresh object from `common()`, so the route chip needs its words
  and menu passed through (as B4-IRB-CHIP, B5-RSBB-CHIP, B6-*-CHIP).
- **B7-ONE-ROUTE**: monoclonal antibodies has one route; her page shows a "Triple Higher only" pill and no picker.
  Plant disease's picker offers the two Triple routes.
- **B-CONNECTS / B-INLINE-LINKS**: her pages name the route helper `c`, not `R`; the batch 4–6 spelling is tried
  first and unchanged.
- **B7-END-EMPTY-CONNECTS** (`build_ks4.py`, batch 7's own copy of `Ks4End` only): a "Connects to" list that the
  route filter leaves empty is hidden instead of showing an empty heading. Batches 2–6 are untouched (their empty
  headings are still listed for Mide in the batch 4–6 notes).
- Titles: all 59 read "… | GCSE Biology | MrBadmus" (her files said "MrBadmusAI").

### G3 links (lane ruling)

Prev/next follow the live per-topic order (`compute_prev_next`, as batches 4–6). So lesson 1 (first in
infection-response) has no Back link to Translocation (organisation), and photosynthesis (first in bioenergetics) has
no Back link to plant disease. On Combined routes drug discovery has no Next (monoclonal and plant disease are
Triple-only); plant disease TF has no Next, TH goes to monoclonal. Every earlier-batch link (Translocation, Culturing
microorganisms, Health and disease, Digestive system, Animal and plant cells, Plant tissues, Heart and blood vessels)
resolves to the live page for the pupil's route; a Triple-only target is dropped on a Combined route rather than left
broken. No `.dc.html` or `Batch N/` text survives on any page.

### Lane rulings (from Mide's prompt)

- **7.4 Thalidomide**: the sentence and verbatim q3 are dropped together (B7-DD-THAL, B7-DD-Q3). The pack's own quiz
  has only three items and Design used all three, so q3's replacement is from the KS4 bank:
  `ks4-drug-discovery-development-e08`, "State what is meant by the efficacy of a drug" (key: how well it works).
  The lead first chose e07 ("the three things a new drug is tested for") but Design's ladder rung 2 already asks that,
  so e08 replaced it. Toxicity, efficacy, dose, double-blind (q1), placebo (q2) and peer review (her new item) are all
  now tested.
- **G3**: above.
- **9.5, 11.7, 16.5**: ruled below.

### Design's "Code to check" items

- **9.5 Plant disease.** Bark "taking pathogens with them": KEEP (spec 8461 4.3.3.2 "layers of dead cells … which fall
  off"; the pathogens going with them is the credited reason). Drooping leaves: KEEP. Mimicry: CHANGED (B7-PD-MIMIC)
  to a concrete example, "leaf spots that look like butterfly eggs, so butterflies don't lay eggs there"; "looking like
  something else" gave a pupil nothing to write. The bank reply on bark reworded (B7-PD-BARK).
- **11.7 Rate of photosynthesis bank.** KEEP her composition. Every brief item is taught and tested on every route:
  rate (bank, rung 2, CFIFA), chlorophyll (bank), one-factor graph (bank on F, rung 3 on all), and on CH TH
  inverse square (bank, rung 2, CFIFA) and greenhouse (Higher interaction, rung 3).
- **16.5 Metabolism.** KEEP. "Ammonia is toxic and so it is immediately converted to urea for safe excretion" is
  8461 4.5.3.3's own wording; route placement is right (deamination HT-only in a biology-only section, so TH;
  kidney filtration biology-only, so TF TH; thyroxine and metabolic rate HT, so CH TH).

### Science rulings from the examination (batch 7)

| id | lesson | what changed, and why |
|---|---|---|
| B7-BD-RESFIG | bacterial diseases | The "resistant bacteria multiply" step redrew ten live non-resistant bacteria, as if the killed ones grew back. Now every bacterium is resistant from that step on (spec: "the population of the resistant strain rises"). |
| B7-VD-FATAL | viral diseases | "Can be fatal if complications arise" taught in the measles row; rung 2 keyed on it and only the key note (after the ladder) said it. |
| B7-VD-CHLORO | viral diseases | TMV's pale patches "have less chlorophyll"; bank q2's key relied on it. |
| B7-AB-VIRUS | antibiotics | "A virus has none of the bacterial structures that antibiotics attack": bank q1's key needed the reason taught. |
| B7-VAC-HERD | vaccination | "This is called herd immunity": bank q2 asks for the term. |
| B7-VAC-MEMORY, B7-CD-MEMORY | vaccination, communicable diseases | "Memory cells" taught in one clause; verbatim bank items test the term (FLAGS keep the idea base). |
| B7-VAC-GRID | vaccination | Grid labels matched what is drawn: 12 of 25 is 48% (was "50%"), 24 of 25 is 96% (was "95%" with 23 drawn). Outcomes 20 / 7 / 1 infected unchanged. |
| B7-FP-APHID | fungal and protist | A Think-again distractor named aphids (Triple-only) on Combined routes: now "By insects". |
| B7-FP-WX3 | fungal and protist | Wetting the leaves "could help it spread" (was "won't help"). |
| B7-MET-LIPID | metabolism | Lipid drawn as 4 beads (one glycerol + three fatty acids), not 6. |
| B7-MET-GLUCOSE | metabolism | Respiration draws glucose as one molecule, not a 6-bead polymer. |
| B7-MET-UREA | metabolism | Breakdown label "amino acids, then urea": the old figure implied protein is made of urea. |
| B7-MET-PLANTS | metabolism | "In plants, glucose and nitrate ions form amino acids." |
| B7-MET-WX2 | metabolism (TH) | A wrong-answer reply said CO₂ is not converted to urea (urea's carbon does come from CO₂); now "Urea contains nitrogen, which comes from amino acids…". |
| B7-MET-KIDNEY | metabolism (CH) | Combined Higher reply no longer leans on kidney filtration (Triple-only). |
| B7-RP-ZERO | rate of photosynthesis | The practical figure measured lamp distance from the heat shield, 60 px short of the pondweed ("10 cm" was really about 17.5 cm on its own scale). Distances now read from the pondweed; shield and its label moved. |
| B7-RP-REL | rate of photosynthesis | "relative light intensity = 1 ÷ d²" on all 7 equation lines (the spec's relationship is a proportion; the triangle already said "relative"). |
| B7-RP-KEYFACT | rate of photosynthesis | The key fact said "The factor in shortest supply limits the rate" on every route; that idea is HT-only. Now lists the four factors. |
| B7-EX-R4 | response to exercise | On CF TF rung 4 no longer asks why breathing stays fast afterwards (the oxygen-debt definition is HT-only). |
| B7-EX-CHAIN | response to exercise (CH TH) | The chain's last two links could be swapped and the liver link did not explain the breathing; now "So breathing stays fast until the lactic acid has been removed". |
| B7-PS-CHAIN | photosynthesis | The CO₂ link could fairly come first; reworded so the order is forced. |
| B7-AR-CHAIN | aerobic respiration | Links 1 and 2 could swap; link 2 now begins "So they need a high rate of aerobic respiration…". |
| B7-AR-Q5 | aerobic respiration | Distractor "They are the largest cells in the body" may be true of muscle fibres; now "They need very little energy". |
| B7-AN-ATP | anaerobic respiration | ATP numbers ("~2 vs ~36") removed from a reply, as FLAGS F1 rules; now "transfers much less energy". |
| B7-UG-WP, B7-UG-POTATO | uses of glucose | "water potential" (A level) removed from a reply; "A potato is packed with food the plant made" (it is mostly water). |
| B7-PD-MIMIC, B7-PD-BARK | plant disease | Above (9.5). |

### Checks

- **Gates (builder):** `ks4_parity.py --batch batch-7` 826 PASS 0 FAIL; `ks4_batch_check` clean for batches 2–7
  (batch 7: 59 pages); one `build_all.py`; diff against `origin/main` = the 118 batch-7 page files, the new batch-7
  files, `build_ks4.py` and `ks4_batch_rulings.py`. Batches 1–6, KS3, B2C, flashcards, Simulations,
  `shared/ks4-nav.js` and `shared/ks4-lib.js` byte-identical to main.
- **Independent pupil walk (Opus auditor, not the builder), 390 px, light theme, one headless Chrome:** all 59 pages,
  every opener option, every teaching control and range, Think again, Sort wrong-then-right, the whole ladder with
  right and wrong answers, chains, mark schemes and "Retry my misses", all five practice questions wrong then right,
  every link; plus targeted drives of the viral clue game, the antibiotics pairs, the plant-doctor game, every figure
  state and every calculation rung.
  - Hard checks clean on all 59 from the first pass: five practice questions on every route, ladder 2·2·2·1 on
    every route, no alert/confirm/prompt, no "Shape:" or stray tokens, no console errors (including after
    interactions), no horizontal scroll, every formula drawn with real subscripts (C₆H₁₂O₆ included), no HTML sub
    inside SVG, every link resolves.
  - The first pass found defects, all fixed by named `B7W-*` rulings and re-walked:
    a right answer marked wrong on the CH/TH inverse-square rung (both "convert" distractors were also correct if
    applied to both distances; now "convert only one distance", and the feedback says why); the viral clue table
    stayed blank for a disease answered wrongly (now fills on any answer); five chains that accepted only one of
    two sensible orders (fungal nets, monoclonal, antibiotics ×2, bark; reworded so the order is forced); labels
    clipped or overlapping (rate "enzymes denatured", exercise "shortfall" and "oxygen debt", HIV "immune cells
    attacked", anaerobic header, malaria box); doubled words ("Fair guess. A fair guess", "Yes. Yes:"); "Pick a
    distance." shown three times; the drug-testing gates figure redrawn as two rows of three (label text 5.7 px →
    11–13 px at 390). Three old verbatim items rebuilt on the auditor's science flags: plant cuticle key ("stops
    pathogens getting into the leaf", not "landing"), herd-immunity reply to "naturally immune", and "Root cells get
    no light and have no chloroplasts" taught before rung 2 asks it.
  - Re-walk after the fixes: every item fixed; regression sweep 59 of 59 pass.
- **Kept (auditor flags, lead's ruling):** uses-of-glucose q3 "main use … (ATP)" and metabolism q2's "catabolic" are
  old verbatim words of the same off-spec class listed after batches 4–6; the rate practical's bubble counts
  (52/30/16/9) are made-up teaching data and need not follow the inverse square law (the page teaches the law for
  light intensity, not rate).
- **Known, left as Design drew them:** most figure labels render at 5–7.5 px on a 390 px phone (as in batches 4–6);
  prev/next labels use the shared nav's older titles ("Uses of Glucose from Photosynthesis") — changing them would
  move every KS4 page; the lipid figure does not colour the glycerol bead differently.

---

- **Shipped:** pushed 13 Oct 2026 as `3650fb9ff..c9af64ea2`; `check_ks4_live.py --batch batch-7`: all 59 live pages are
  this build byte for byte, and every asset they name matches its stamp.

---

## Batch 8: homeostasis and response, inheritance (16 lessons, 54 pages)

### Files and routes

| # | lesson (live slug) | topic | routes |
|---|---|---|---|
| 1 | homeostasis | homeostasis | CF CH TF TH |
| 2 | nervous-system | homeostasis | CF CH TF TH |
| 3 | reflex-actions | homeostasis | CF CH TF TH |
| 4 | reaction-time | homeostasis | CF CH TF TH |
| 5 | the-brain | homeostasis | TF TH |
| 6 | the-eye | homeostasis | TF TH |
| 7 | defects-of-the-eye | homeostasis | TF TH |
| 8 | thermoregulation | homeostasis | TF TH |
| 9 | endocrine-system | homeostasis | CF CH TF TH |
| 10 | blood-glucose-diabetes | homeostasis | CF CH TF TH |
| 11 | human-reproduction-hormones | homeostasis | CF CH TF TH |
| 12 | contraception-fertility | homeostasis | CF CH TF TH |
| 13 | sexual-asexual-reproduction | inheritance | CF CH TF TH |
| 14 | meiosis | inheritance | CF CH TF TH |
| 15 | advantages-sexual-asexual | inheritance | TF TH |
| 16 | dna-genome | inheritance | CF CH TF TH |

54 pages per tree. Her shared blocks are byte-identical to batch 7's except `Ks4Steps` (one line: an optional
`eyebrow`, used on reaction time's table-then-mean chain).

### Port mechanics (not science)

- **The crash on six pages (B8-<lesson>-TDZ).** On the brain, thermoregulation, endocrine system, blood glucose,
  human reproduction and contraception, the progress-rail line read the route flag (`H` or `TH`) before the line
  that set it. Loading the page was fine; the moment a pupil finished the guarded step (the fourth brain patient,
  the sixth gland, the third blood-glucose mode, the fourth cycle stage, the third contraception need, both
  temperature views) the page stopped working, on every route that got that far. Design's check only loaded each
  page, so it could not see it. Each ruling computes the same flag first, exactly as the page's own route helper
  does; nothing else changes. Batch 7 has no such line (checked by script on all 32 files).
- **B8-LNK**: batch 8 writes its links through a `LNK(slug, label)` helper over a file map, not `href` objects;
  the ruling sends them through the live route-aware link helper.
- **B8-<slug>-CHIP** (16), the "Triple" pathway pill, and the empty "Connects to" hide extended to batch 8's own
  end block, as in batch 7.
- **Triple-only pointers on Combined pages** (homeostasis → Thermoregulation, reflex actions → The eye): her text
  labels them "(Triple)"; they would have been dead links on Combined routes, so they show on Triple routes only.
  Her words are unchanged.

### G3 links

Prev/next follow the live per-topic order: homeostasis (first in its topic) and sexual and asexual reproduction
(first in inheritance) have no Back link; DNA and the genome keeps the live Next. Her links into batches 6 and 7
(Metabolism, Aerobic respiration, Fungal and protist diseases) resolve to the live pages. DNA's Triple pointer to
the DNA structure lesson stays unlinked, as she built it (lane ruling 16.1; that lesson is batch 9).

### Lane rulings (from Mide's prompt)

- **4.7 reaction-time conversion table**: kept, given not derived. The examiner recomputed all nine values
  (t = √(2d ÷ 9.8), 2 dp: 5 cm 0.10 s … 45 cm 0.30 s; 15 cm is 0.1750, which rounds to 0.17). No free-fall
  equation, ½, √ or 9.8 appears anywhere.
- **11.6 progesterone "from the ovary"**: kept. Verbatim q1 and q2 both mention the corpus luteum in their
  explanations, so both are replaced from the KS4 bank on every route: q1 → `ks4-human-reproduction-hormones-e06`
  ("What does the hormone LH cause to happen?") on CF TF and `-s15` ("Explain why oestrogen levels rise before
  the LH surge") on CH TH, because CH TH already has a graph item whose answer is the LH peak; q2 → `-s04`
  (progesterone keeps the lining if an embryo implants), with one sentence added to the cycle stepper so it is
  taught first (B8-HR-IMPLANT). No "corpus luteum" remains anywhere.
- **12.5 contraception**: both lines kept. Every method's wording was checked line by line against 8461 4.5.3.5 /
  8464 4.5.3.4 and matches; two old verbatim strings were not (below).
- **16.1 DNA and the genome**: kept as she built it.
- **7.2 and 15.4**: ruled below.

### Design's "Code to check" items

- **7.2 Defects of the eye.** Hard lenses (long-lasting, less comfortable), soft lenses (comfortable, higher
  infection risk) and the replacement lens: KEEP. Laser surgery keeps "usually removes the need for glasses or
  contact lenses", plus "for myopia it is made flatter, so it refracts light less" (B8-DE-LASER: bank q2 keys on
  it). Spectacles' "risk" line loses "the eye itself is unchanged", which is not a risk (B8-DE-SPECS).
- **15.4 Advantages.** The water flea (asexual when food is plentiful, sexual when the pond dries) and the aphids on
  rung 4: KEEP. Both are accurate and given as information, which is exactly what 8461 4.6.1.3 allows.
- **4.6 Reaction time**: both typical-time statements kept; 0.2–0.3 s for a simple ruler catch sits inside the
  physics spec's 0.2–0.9 s.

### Science rulings from the examination (batch 8)

| id | lesson | what changed, and why |
|---|---|---|
| B8-DE-WRONGLENS | defects of the eye | The "wrong lens" view for long sight drew the concave lens bending rays inwards, like a converging lens, beside a note saying it spreads them further. Now drawn diverging. |
| B8-NS-RUNG2 | nervous system | The data question moved the hand ("near the face" vs "at the foot"); the nerve from the hand is the same length either way, so the keyed answer didn't follow. Now a touch on the cheek vs the foot. |
| B8-NS-NT | nervous system | "The chemical, a neurotransmitter, binds to receptors on the next neurone": a verbatim bank key uses the word. |
| B8-RT-MM | reaction time | The method block now shows "mm ÷ 10, so 120 mm = 12 cm"; the Step 1 attempt converts mm and only m → cm had been shown. |
| B8-TR-EVAP | thermoregulation | "Sweat, which evaporates from the skin": the TF bank item's key relies on evaporation, which was only in the TH layer. |
| B8-EYE-ACC | the eye | Accommodation context reworded ("You stop looking at the far side of a field and look at a book"); "look up from" read as looking away. |
| B8-BG-HOOK | blood glucose | The opener had a snack fixing low blood sugar, which backs the answer marked wrong, and raising low glucose is glucagon (HT only). Now "A big bowl of pasta": glucose rises after a meal and is back to normal two hours later with nothing else eaten. Question and bridge unchanged. |
| B8-DNA-CIRCLE | DNA and the genome | A distractor reply said a circle of DNA is "Not at GCSE"; plasmid rings are GCSE. Now "DNA's two strands twist into a double helix". |
| B8-DNA-EVERY | DNA and the genome | "Nearly every cell" (red blood cells have no nucleus). |
| B8-DNA-NONCODING | DNA and the genome | A reply mentioned non-coding DNA (Triple HT only): now "A gene is a small section of DNA that codes for a particular protein." |
| B8-CF-DIAPHRAGM | contraception | An old reply said a diaphragm stops sperm entering; it covers the cervix. Now names only the condom. |
| B8-CF-IUD | contraception | A distractor described how a condom is worn; replaced with "It stops eggs maturing" (hormonal), keeping to what each method blocks. |
| B8-HR-GRAMMAR | human reproduction | "State approximately how often an egg is released" (was "Give how often…, approximately"). |
| B8-SAR-BANK | sexual and asexual | On TF TH the bank tested advantages taught two lessons later; every route now gets the same five. |
| B8-ADV-WHEAT | advantages | "Wheat grows from seeds, not bulbs" (the reply gave the wrong reason). |

### Checks

- **Gates (builder):** `ks4_parity.py --batch batch-8` 756 PASS 0 FAIL; `ks4_batch_check` clean for batches 2–8
  (batch 8: 54 pages); one `build_all.py`; diff against main = the 108 batch-8 page files, the new batch-8 files,
  `build_ks4.py` and `ks4_batch_rulings.py`. Batches 1–7 (including batch 7's metabolism page), KS3, B2C,
  flashcards, Simulations, `shared/ks4-nav.js` and `shared/ks4-lib.js` byte-identical to main.
- **Independent pupil walk (the same Opus auditor, not the builder)**, 390 px, light theme, one headless Chrome, all
  54 pages, everything pressed as for batch 7; every 3- and 4-link chain (108) tried in every order.
  - Clean on all 54 from the first pass: no console errors or exceptions anywhere, including after every
    interaction on the six formerly crashing pages (every step completed on every route, every rail item ticks);
    five practice questions and ladder 2·2·2·1 on every route; no dialogs, "Shape:" or stray tokens; no horizontal
    scroll; no raw subscript digits, no HTML sub inside SVG, cm³ drawn on the glucose axis; every link resolves;
    the "(Triple)" pointers appear on Triple routes only; reproduction and contraception keep to hormones, the
    lining, ovulation and what each method blocks. Every reaction-time mean, conversion and table value, the
    glucose curves and the meiosis numbers recomputed correct.
  - Fixed after the first pass (named `B8W-*` rulings): three clipped labels ("cerebral cortex" off the left of
    both brain figures, the IVF "1 or 2 embryos into the uterus" stage, "focus behind the retina"), two overlaps
    (the homeostasis red X over "Coordination centre", "LH" running into "ovulation"); a CH/TH reproduction
    distractor marked wrong although the page teaches it ("maintains the uterus lining in the second half" →
    "Stimulates sperm production"); eight chains that rejected a second sensible order (brain ×3, thermoregulation
    ×2, reproduction, contraception, cuttings) reworded or merged so one order is forced; blood glucose's Type 1/2
    key put in the spec's words ("fails to produce sufficient insulin"), "tablets" removed from its reply, and
    "Insulin is a protein, so it would be digested if swallowed; it is injected instead" taught before the
    practice key relies on it.
- **Kept (old verbatim words, same class as batches 4–7):** DNA's "DNA bases" / "~3 billion base pairs" on Combined
  routes; thermoregulation's "latent heat"; blood glucose's "beta cells"/"autoimmune" (answerable by elimination).
- **Known, left as Design drew them:** tiny figure text at 390 (worst on the nervous-system pathway and the
  reaction-time table); contraception's "Sperm meets egg"/"Embryo implants" touch their box edges; "predict first"
  sits across panel borders on advantages; the reproduction hormone graph marks ovulation but not menstruation
  (pack flag HRH-F2 asked for both: a figure addition for Design, not a port fix).

- **Re-walk after the fixes:** every item fixed; regression sweep 54 of 54 pass; the six formerly crashing lessons
  re-walked in full on all 20 route pages (every step done, every rail item ticked, ladders 4/4 after retry,
  practice 5/5). Two old verbatim wrong-answer replies on blood glucose left as written: "Only TYPE 1 is
  autoimmune" (term not taught) and "about 90% of all diabetes cases" (true, not on the spec).

---

## For Mide (nothing here blocks; your call when convenient)

1. **Old verbatim quiz words that are off-spec but not wrong**: ATP (uses of glucose), "catabolic" (metabolism TH),
   "DNA bases" and "~3 billion base pairs" on Combined (DNA), "latent heat" (thermoregulation), "beta cells",
   "autoimmune" and "about 90%" (blood glucose). Same class as the list after batches 4–6.
2. **Tiny figure text on phones**: most figure labels in both batches render at 5–7.5 px on a 390 px screen. Only the
   drug-testing gates figure was redrawn (two rows; now 11–13 px). A general fix belongs in Design's diagram style.
3. **Prev/next labels** use the shared nav's older titles (e.g. "Uses of Glucose from Photosynthesis"). Changing them
   moves every KS4 page.
4. **Hormone graph** (reproduction, CH TH) marks ovulation but not menstruation; the pack asked for both. For Design.

---

## Still missing (not built)

- **Batch 6 transpiration with rate calculations.** Pending: Mide to download Design's updated Batch 6 transpiration
  file. Design made it (her batch 7 and 8 NOTES both say so, `Batch 6/lessons/ks4-biology-4.2.3.2-transpiration.dc.html`)
  but it is not in this download; the live page is still the old one.
