# KS4 batches 10 and 11: port report

Design's batches 10 (15 biology lessons: ecology) and 11 (16 chemistry lessons: atomic structure, quantitative
chemistry, acids and electrolysis), delivered 12 Oct 2026, ported the way batches 7–8 were
(`docs/ks4/BATCH7-8-PORT-REPORT.md`): her lessons, her blocks, her words, with every change a named ruling in
`ks4_batch_rulings.py` that fails the build if its target text is not found the expected number of times. Her files
sit verbatim in `docs/ks4/design-reference/batch-10/` and `batch-11/` (`MD5SUMS` beside each). Opus led and audited;
Sonnet built. One worktree (`mrbadmus-worktrees/ks4-batch10`), one push per batch.

How the science was checked: seven independent Opus examiners (three for batch 10, four for batch 11) read all 31
files in full against the AQA 8461/8462/8464 spec text, the batch pack (`docs/ks4/packs/batch-10|11/`: brief, FLAGS,
checked science source, examination notes) and Design's NOTES, every pupil-visible string on every route. The lead
ruled on each finding. Settled science was ruled here; nothing in this report needs Mide's examiner judgement unless
it is listed under "For Mide".

Her shared blocks (all fourteen `Ks4*` blocks, `ks4-lib.js`, `ks4-diagrams.js`, `ks4-theme.css`, `support.js`) are
byte-identical to batch 8's in both batches.

---

## Batch 10: ecology (15 lessons, 45 pages)

### Files and routes

| # | lesson (live slug) | spec | routes |
|---|---|---|---|
| 1 | ecosystems | 4.7.1.1 | CF CH TF TH |
| 2 | population-competition | 4.7.1.1 | CF CH TF TH |
| 3 | abiotic-biotic-factors | 4.7.1.2 | CF CH TF TH |
| 4 | adaptations | 4.7.1.4 | CF CH TF TH |
| 5 | food-chains-webs | 4.7.2.1 | CF CH TF TH |
| 6 | sampling-techniques | 4.7.2.1 | CF CH TF TH |
| 7 | environmental-change | 4.7.2.4 | TH |
| 8 | deforestation | 4.7.3.4 | CF CH TF TH |
| 9 | maintaining-biodiversity | 4.7.3.6 | CF CH TF TH |
| 10 | trophic-levels | 4.7.4.1 | TF TH |
| 11 | pyramids-of-biomass | 4.7.4.2 | TF TH |
| 12 | transfer-of-biomass | 4.7.4.3 | TF TH |
| 13 | farming-techniques | 4.7.5.2 | TF TH |
| 14 | sustainable-fisheries | 4.7.5.3 | TF TH |
| 15 | role-of-biotechnology | 4.7.5.4 | TF TH |

45 pages per tree (16 Combined, 29 Triple; the same 45 in `mrbadmus_site/`). Each replaces the old generated page at
the same URL. New files: `ks4_lessons/batch_10.py`, `batch10_ext.js` (batch 8's subscript script),
`frozen_batch-10.json`, `ks4_batch-10_manifest.json`, `shared/ks4-{source,lesson,ext}-batch-10.*`.

### Port mechanics (not science)

- **B10-<slug>-CHIP** (15): her `common()` returns a fresh object, so the route chip's words and menu are passed
  through (as batches 4–8).
- **B10-ALL-FOUR-PILL**: she draws one "All four routes" pill and no tier pill; it is replaced by the route chip.
- **B10-ONE-ROUTE-SELECT**: environmental change (Triple Higher only) carried a one-option Route picker; removed.
- **B8-LNK widened, generically**: batch 10 calls `this.common(done, F, ready)` and her `endNext:` line also closes the
  object (`… : null };`); both spellings are now accepted, batch 8's tried first. **B10-FILE-REFS**: her in-text
  links are bound off the FILE map (`pcHref: FILE['…']`); each is now routed through the live route-aware link helper.
- **B10-<slug>-FOODSEC** (4): her `food-security` key is the live `factors-affecting-food-security` (Triple only, so
  absent on Combined routes).
- `build_ks4.py`: batch 10 added to the END-EMPTY-CONNECTS tuple (its own copy of `Ks4End` hides an empty
  "Connects to"); batches 2–6 untouched.
- No use-before-declare on any page (the batch 8 crash class): checked by the builder and all three examiners.
- `block_map`: 18 data/evaluation sections the classifier could not type are `explainer`, as batch 8.
- Titles read "… | GCSE Biology | MrBadmus".

### Links to batch 9 (lane ruling: dropped, to restore when batch 9 lands)

Batch 9 is not live. Every link to a batch 9 lesson is dropped, and every in-text pointer to one is removed, not left
dead. Prev/next follow the live per-topic order, so no batch 9 page appeared there.

| ruling | lesson | what was removed (restore this) |
|---|---|---|
| B10-ADAPTATIONS-B9-CONNECT | adaptations | "Connects to" entry `LNK('evolution-natural-selection', 'Evolution and natural selection')` |
| B10-ADAPTATIONS-B9-NSHREF-BIND, -NSLINK | adaptations | the link on "natural selection" in "…the feature becomes common: `<a href="{{ nsHref }}">natural selection</a>`." (the words stay: they are the term, not a pointer) |
| B10-ENVIRONMENTAL-CHANGE-B9-CONNECT | environmental change | "Connects to" entry `LNK('variation', 'Variation')` |
| B10-FARMING-TECHNIQUES-B9-CONNECT | farming techniques | "Connects to" entry `LNK('resistant-bacteria', 'Resistant bacteria')` |
| B10-ROLE-OF-BIOTECHNOLOGY-B9-CONNECT | role of biotechnology | "Connects to" entry `LNK('genetic-engineering', 'Genetic engineering')` |
| B10-ROLE-OF-BIOTECHNOLOGY-B9-GEHREF-BIND, -GELINK | role of biotechnology | the sentence "How the gene is moved is in `<a href="{{ geHref }}">Genetic engineering</a>`; here the chain is the point." |

Her NOTES G7 asked Code to re-point three earlier pages' forward links. Not needed and not done (those pages stay
byte-identical): batch 4 Biodiversity has no link to a batch 10 page; batch 2 Carbon cycle already links to
Maintaining biodiversity, which now resolves to the new page on all four routes; batch 9 is not live.

### Lane rulings (from Mide's prompt)

- **2.3** (population and competition): q2 and the "(competition within a species / between species)" gloss kept.
  The page never prints "intraspecific"/"interspecific"; q2's key repeats the page's own sentence and every
  distractor is wrong on its own terms, so it is answerable. The terms were not added.
- **4.3** (Arctic fox): **changed, and not as the ruling's letter asked.** The pack does not support "blood flow to
  its paws is reduced in the cold", and no functional example the pack gives is true of an Arctic fox (its functional
  examples are antifreeze proteins in Arctic fish, the camel's tolerance of water loss, and the kangaroo rat's
  concentrated urine), so attaching one to the fox would be false. B10-AD-FOX makes the fox's fourth feature "Thick
  fur on the soles of its paws" (structural: the pack's "thick fur insulates"). The functional type is still
  classified in the same activity, on the fennec fox (very concentrated urine, the pack's functional example).
- **6.6** (sampling): her two-line form kept.

### Design's flags, ruled

1.1–1.3, 1.5 KEEP; 1.4 CHANGE (B10-ECO-COMP). 2.1–2.4 KEEP; 2.5 CHANGE (B10-PC-YR, -NQ, -LAG). 3.1–3.4 KEEP.
4.1, 4.2, 4.4 KEEP; 4.3 above. 5.2–5.5 KEEP; 5.1 CHANGE (B10-FCW-LVL). 6.1–6.6 KEEP. 7.1–7.5 KEEP; 7.6 CHANGE (the
hedge brown is a real butterfly, the gatekeeper; only its records are made up: B10-ENV-MAP). 8.1–8.3, 9.1–9.3,
10.1–10.4, 11.1–11.4, 12.1–12.5, 14.1–14.5, 15.1, 15.2, 15.4, 15.5 KEEP. 13.4 CHANGE ("battery" chickens: B10-FT-BATTERY);
15.3 CHANGE in part (B10-RB-HERB, -FLOW).

### Science rulings from the examination (batch 10)

| id | lesson | what changed, and why |
|---|---|---|
| B10-DEF-ARROW | deforestation | The photosynthesis arrow ran from the forest UP into the atmosphere (the arrowhead is drawn at the second point), the same way as the burning and decay arrows: the figure showed photosynthesis releasing carbon dioxide. Now points down, atmosphere into forest, in both states. |
| B10-FT-SPLIT | farming techniques | The figure split feed into body mass vs "respiration: movement and heat", i.e. heat as where mass goes and no faeces or urine (4.7.4.3). Now "respiration, faeces, urine". |
| B10-RB-HERB | biotechnology | A reply said herbicide-tolerant crops "don't absorb more into edible tissue" (overstated, FLAGS RB-F4). Now: residues are a separate, regulated question; the concern is gene flow. |
| B10-RB-FLOW | biotechnology | Practice q2's key (herbicide-resistance genes spreading in pollen to wild relatives) was never taught: one sentence added to the GM concerns card. |
| B10-ECO-COMP | ecosystems | Practice q4 asked what animals compete for; the page only linked to competition. The spec's two lists added. |
| B10-ECO-ART | ecosystems | Practice q3 (farmland has fewer species) taught only in the key note: one sentence added earlier. |
| B10-ECO-WEB | ecosystems | "Remove the wolves" said deer overgraze flowering plants, but the web had no flowering plants → deer arrow. Arrow added; the text names flowering plants. |
| B10-ABF-PATH | abiotic and biotic | Practice q5 (a new fungus is a pathogen): "such as a bacterium or a fungus" added where pathogens are defined. |
| B10-ENV-MISMATCH | environmental change | Practice item keyed "a timing mismatch" relied on an idea only in the opener's wrong-answer reply. One sentence added to the temperature card. |
| B10-TL-ARROWS | trophic levels | Practice q1 tests what food-chain arrows mean; the page never said. One sentence added. |
| B10-TOB-FARM | transfer of biomass | Practice q1 (why farms restrict movement) never taught on the page. One sentence added. |
| B10-FCW-LVL | food chains | The chain figure printed "level 1 … level 4" on every route; numbering trophic levels is Triple only (FCW-F1). Labels now on Triple routes only. |
| B10-PC-YR, -NQ, -LAG | population and competition | The lynx curve peaks at year 3.5, but the notes called year 4 the peak and a question said hares were "falling fast" at year 5, their minimum. Year notes and the question now match the curve; the graph scale changed so the lag arrow no longer sits on the hare peak. |
| B10-PYR-TENTH | pyramids | The mark scheme said "each bar is about a tenth of the one below" against its own data (a fifth, then a tenth). |
| B10-SF-STEADY | fisheries | "Rose steadily" (three places, one a key) for data that rise slowly then faster. |
| B10-SF-GRAPH | fisheries | "Use the graph" where the page gives the cod data as text: now "Use the data". |
| B10-ENV-MAP | environmental change | The hedge brown is a real species; "a made-up butterfly" → the records are made up. "10 km squares" (which the map does not draw) → "grid squares". |
| B10-ENV-EVOL | environmental change | "Forty years is too short for evolution" (for an insect breeding every year) → a range shift is moving, not evolving. |
| B10-AD-HUMP | adaptations | The page defines structural as "a body part", then called fat in the camel's hump functional. The card now uses the pack's clean camel example (surviving the loss of a lot of body water). |
| B10-AD-JERB | adaptations | "Getting all its water from its food" keyed functional is fairly read as behavioural; now very concentrated urine. |
| B10-AD-PROD | adaptations | Distractor "Producers" for vent bacteria is defensibly true; now "Herbivores". |
| B10-AD-NS | adaptations | The natural-selection model answer now includes passing the feature on to offspring. |
| B10-AD-FOX | adaptations | Lane ruling 4.3, above. |
| B10-FT-BATTERY (2) | farming techniques | "Battery chickens/farming" (banned in the UK since 2012, never taught on the page) → "intensively farmed". |
| B10-RB-MADEUP | biotechnology | The golden-rice box was headed "made-up data" over real facts. |
| B10-RB-RESP | biotechnology | "No animal respiring most of it away" read as if the fungus does not respire. |
| B10-ABF-POND, -OXY | abiotic and biotic | A reply claimed timing the data do not give; "polluted water holds less oxygen" (pollution uses it up). |
| B10-TOB-FOX, -UNIT | transfer of biomass | A reply implied uneaten parts are never a loss; triangle unit "g/m² or kg" → same unit for both. |
| B10-FT-JUDGE, -WARM | farming techniques | The evaluation pick's correct option had no judgement; "no need to keep warm" → "less need". |
| B10-SAMP-STILL, -YES | sampling | "Daisies do not stay still" (they do, which is why quadrats suit them); a "No" answer whose reply opened "Yes." |
| B10-ECO-HOOK, B10-MB-LABEL, B10-DEF-RAIL, B10-PYR-META | various | A garbled reply ("Nothing eats a flower's bees"); the "hedgerow" label drawn in paper colour on the cream plate (invisible); rail "CO2" without a subscript; a platform self-explanation removed (no redundant text). |
| Chains (8) | ecosystems, abiotic, adaptations, deforestation, maintaining biodiversity, pyramids, transfer, biotechnology | B10-ECO-CHAIN, -ABF-CHAIN, -AD-CACT, -DEF-CHAIN, -MB-CHAIN, -PYR-CHAIN, -TOB-CHAIN, -RB-CHAIN: each chain had a second sensible order that would be marked wrong; linking words ("So", "Then", "As well as that") force one order. |

### Checks

- **Gates (builder):** `ks4_parity.py --batch batch-10` 630 PASS 0 FAIL; `ks4_batch_check --batch batch-10` clean
  (45 pages, 27 assets, freeze); zero console errors across the 45 pages at 1280 and 360 px; all 643 hrefs on the 45
  pages exist on their route. Diff against `origin/main`: the 90 batch-10 page files, the new batch-10 files,
  `build_ks4.py` (one tuple entry) and `ks4_batch_rulings.py`. Every other page, KS3, B2C, flashcards, Simulations,
  `shared/ks4-nav.js` and `shared/ks4-lib.js` byte-identical to main.
- **Independent pupil walk (Opus auditor, not the builder)**, 390 px, light theme, one headless Chrome, all 45 page
  routes, 180 loads, everything pressed: every opener option, every teaching control and figure state, Think again,
  Sort wrong-then-right, every ladder rung right and wrong (every chain tried in every order), all five practice
  questions wrong then right, every link.
  - Clean on all 45 from the first pass: no console errors (including after every interaction), dialogs, sideways
    scroll or stray tokens; five practice questions and ladder 2·2·2·1 on every route; every link resolves on its
    route; no batch 9 slug anywhere; Triple-only blocks absent on Combined; the rail ticks every section; real
    subscripts (CO₂, B₂, B₁); all 30 chains force one order; every calculation recomputes and accepts sensible
    right forms. Every figure the examination rulings touched was checked in its state and holds (the photosynthesis
    arrows point down; the lag arrow runs hare peak to lynx peak; level labels only on Triple; the hedgerow label is
    legible; the new web arrow draws).
  - Fixed after the first pass (`B10W-*`): an untrue reply ("water is stored in fat (camels)", contradicting the
    page's own rung 4); the deforestation decay arrow drawn through its own label; the oak drawn over the levels
    labels; three labels overrunning their boxes or the leaf (trophic levels ×2, abiotic); "3, 7 8, 2 5, 4" run
    together; "1 daisies"; a tab labelled "Verbatim"; pyramid labels pushed off the figure by a wrong width; both
    biotechnology "Predict" questions answered by the sentence before them; "Rabbits double" stopping a step short
    (owls, which eat only shrews, now fall); nested double quotes; "two arrows" over three; a reply praising the
    wrong answer ("But the cascade of effects described is accurate"); the sand cat panel headed "made-up data"
    over real facts.
  - Kept: two old pack lines on evolution timescales ("Twenty years is far too short" for a fish; birds shifting
    "too rapidly (within 50 years)"), cleared by the pack examiner; a hare dot hidden where the curves cross;
    map squares a little outside the coastline (counts right); rails that tick an item with nothing to do on load
    (pyramids "Scale", transfer "Equation"); classifier ticks that clear if a pupil changes an answer; old off-spec
    words in verbatim replies (keystone, niche, aposematism, parasites); small figure text (as small as 6 px at 390).

- **Re-walk after the fixes** (same auditor, all 45 page-routes again): every fix confirmed in its state (the oak
  measured clear of both box borders at 390 px; every label inside its box; owls fall when rabbits double), and a
  regression sweep of 45 of 45: no console errors or dialogs, five practice questions, ladder 2·2·2·1, 4/4 after
  "Retry my misses", 860 links all resolving, no batch 9 slug, repo-root copies identical to `mrbadmus_site/`, no
  clipped or overlapping figure text. Two items it raised, then fixed by the lead: the mycoprotein figure drew
  "air in (aerobic)" before the pupil predicts why air is bubbled through (B10W-MY-AIRFIG: it now appears with the
  reason); "soil, water, temperature" ran across a box border (B10W-ECO-ABIOTIC-LBL). Kept: the first mycoprotein
  Predict ("what is the fungus fed on?") is a recall check of the section's own opening sentence.
- **Knowledge points (parent view):** the 769 new question ids (ladder, choice, sort and practice items on the 45
  pages) were tagged by `tools/kp_classify.py --top-up` onto the existing points (12 new points across eight lessons,
  0 left untagged), and the backend's `knowledge-points.json` re-exported (additive only) and pushed before the site.

---

<!-- BATCH11 -->
