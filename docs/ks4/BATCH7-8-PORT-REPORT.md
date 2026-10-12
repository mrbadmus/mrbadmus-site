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

<!-- WALK7 -->

---

## Batch 8: homeostasis and response, inheritance (16 lessons)

<!-- BATCH8 -->

---

## Still missing (not built)

- **Batch 6 transpiration with rate calculations.** Pending: Mide to download Design's updated Batch 6 transpiration
  file. Design made it (her batch 7 and 8 NOTES both say so, `Batch 6/lessons/ks4-biology-4.2.3.2-transpiration.dc.html`)
  but it is not in this download; the live page is still the old one.
