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
- **Gates (pre-push):** every registered gate green, no override. Slow gates selected by this branch's paths and
  recorded: verify_ks3, ks4_parity (full pilot sweep), ks4_chrome_drive, test_isolation_drive. ks4_parity first died
  three times on a Chrome websocket timeout (`timed out waiting for 2 bytes from chrome`) while another session was
  building and running headless Chrome; the lesson it stopped on passed alone (92/92), and the full sweep passed on a
  quiet machine. No gate was weakened.

**Shipped:** backend `dcbb5c8..1eef943` (knowledge points; Render serving 1eef943), then site pushed 16 Oct 2026 as
`f4e5add6b..7850ba8cc`; `check_ks4_live.py --batch batch-10`: all 45 live pages are this build byte for byte, and
every asset they name matches its stamp.

---

## Batch 11: atomic structure, quantitative chemistry, acids and electrolysis (16 lessons, 56 pages)

### Files and routes

| # | lesson (live slug) | topic | spec | routes |
|---|---|---|---|---|
| 1 | model-of-the-atom | atomic-structure | 5.1.1.3 | CF CH TF TH |
| 2 | subatomic-particles | atomic-structure | 5.1.1.4 | CF CH TF TH |
| 3 | relative-atomic-mass | atomic-structure | 5.1.1.6 | CF CH TF TH |
| 4 | electronic-structure | atomic-structure | 5.1.1.7 | CF CH TF TH |
| 5 | group-7 | atomic-structure | 5.1.2.6 | CF CH TF TH |
| 6 | transition-metals | atomic-structure | 8462 4.1.3.1 | TF TH |
| 7 | mass-changes-reactions | quantitative | 5.3.1.3 | CF CH TF TH |
| 8 | chemical-measurements | quantitative | 5.3.1.4 | CF CH TF TH |
| 9 | moles | quantitative | 5.3.2.1 | CH TH |
| 10 | amounts-in-equations | quantitative | 5.3.2.2 | CH TH |
| 11 | oxidation-reduction | chemical-changes | 5.4.1.4 (+ 5.4.1.1, 5.4.1.3) | CF CH TF TH |
| 12 | salts-neutralisation | chemical-changes | 5.4.2.2 | CF CH TF TH |
| 13 | ph-scale | chemical-changes | 5.4.2.4 | CF CH TF TH |
| 14 | strong-weak-acids | chemical-changes | 5.4.2.5 | CH TH |
| 15 | electrolysis-principles | chemical-changes | 5.4.3.1 | CF CH TF TH |
| 16 | electrolysis-molten | chemical-changes | 5.4.3.2 | CF CH TF TH |

56 pages per tree (CF 12, CH 15, TF 13, TH 16). Each replaces the old generated page at the same URL. New files:
`ks4_lessons/batch_11.py`, `batch11_ext.js`, `frozen_batch-11.json`, `ks4_batch-11_manifest.json`,
`shared/ks4-{source,lesson,ext}-batch-11.*`.

### Port mechanics (not science)

- **B11-<slug>-CHIP** (16), and B8-LNK widened again, generically: four pages call `this.common(done, F, ready, rail)`
  and electrolysis-molten names the result `cm` (its `c` is the compound picker). Tried only when the batch 8 and
  batch 10 spellings are absent.
- **B11-HIGHER-PILL** (new): moles, amounts in equations and strong and weak acids (CH TH) draw a filled "Higher only"
  pill and "Combined · Triple"; the "Higher only" pill is removed (the eyebrow already says "Higher only" and the route
  chip names the tier) and "Combined · Triple" becomes the route chip, e.g. "Combined Science · Higher tier" with a
  switch to Triple Higher.
- **B11-G3-KS4**: batch 11's pages may carry no `/ks4/` text after the link rulings (it never fired).
- 16 data sections the classifier could not type are `explainer`, as batches 8 and 10.
- No use-before-declare on any page (checked by the builder and all four examiners).
- Titles read "… | GCSE Chemistry | MrBadmus".

### G2 links (lane ruling)

Her seven `/ks4/<slug>` placeholders and her `../../KS4 Batch 4|5/…` links now go through the live route-aware link
helper. Re-pointed on every route: Atoms, elements and compounds; Relative formula mass; Conservation of mass; Using
moles in calculations (CH TH, which is every route of the two pages that link it); Periodic table, Group 0, Metals and
non-metals, Reactivity series, Extraction of metals, and physics Structure of the atom and Development of the atomic
model. Dropped where the route has no such page (no dead link):

| lesson | route | link | what the pupil sees |
|---|---|---|---|
| chemical measurements | CF CH | Titrations (connects) | not listed; listed on TF TH |
| salts and neutralisation | CF CH | Titrations (connects) | not listed; listed on TF TH |
| pH scale | CF CH | Titrations (connects) | not listed; listed on TF TH |
| strong and weak acids | CH | Titrations (connects) | not listed; listed on TH |
| amounts in equations | CH | Percentage yield, Atom economy (in-text, B11-AIE-NOLINKS) | the words, no link; linked on TH |
| mass changes | CF TF | Moles, Amounts in equations (connects) | not listed; listed on CH TH |
| pH scale | CF TF | Strong and weak acids (connects) | not listed; listed on CH TH |

Her NOTES say batch-2/3 "Connects to" lists already forward-link to Moles, Amounts in equations, Mass changes and
Salts: they did (conservation of mass, using moles, titrations), so those links now land on Design's pages with no
change to those pages. The two conditional rulings (B11-MCR-LINKS, B11-CM-TITLINK) were not needed: the route filter
already drops those links, proved on the built pages.

### Overlap with live lessons (lane ruling)

None of the 16 slugs was already a ported lesson (batches 2–10), so no ported page is swapped: every lesson replaces
the OLD generated page at its own slug. Neighbours checked for a shared spec point:

| batch 11 lesson (spec) | live neighbour (batch, spec) | same spec point? | ruling |
|---|---|---|---|
| model-of-the-atom (5.1.1.3) | atoms-elements-compounds (b2, 5.1.1.1) | no | both stay; hers points to it |
| relative-atomic-mass (5.1.1.6) | relative-formula-mass (b2, 5.3.1.2) | no | both stay; hers points to it |
| electronic-structure (5.1.1.7) | group-0 (b5, 5.1.2.4) | no | both stay; hers points to Group 0 |
| group-7 (5.1.2.6) | group-1 (b6, 5.1.2.5), group-0 (b5) | no | both stay |
| transition-metals (8462 4.1.3.1) | group-1 (b6) | no | both stay |
| mass-changes-reactions (5.3.1.3) | conservation-of-mass (b3, 5.3.1.1) | no | both stay; linked both ways (b3 already linked this URL) |
| moles (5.3.2.1) | using-moles-calculations (b2, 5.3.2.3–4) | no | both stay; linked both ways (b2 already linked this URL) |
| amounts-in-equations (5.3.2.2) | using-moles-calculations (b2), conservation-of-mass (b3) | no | both stay; both already linked this URL |
| oxidation-reduction (5.4.1.4, with the oxygen definitions of 5.4.1.1 and 5.4.1.3) | reactivity-series (b5, 5.4.1.1), extraction-of-metals (b5, 5.4.1.3) | partly: the oxygen definitions | both stay; hers points to both; the batch 5 pages do not point back (adding it would move non-batch pages: For Mide) |
| salts-neutralisation (5.4.2.2) | reactions-of-acids (b6, 5.4.2.1), titrations (b2, 8462 4.4.2.5) | no | both stay; titrations already linked this URL |
| ph-scale (5.4.2.4), strong-weak-acids (5.4.2.5) | reactions-of-acids (b6) | no | both stay |
| electrolysis-principles (5.4.3.1), electrolysis-molten (5.4.3.2) | extraction-of-metals (b5); the old unported half-equations page (5.4.3.5 HT) | no | both stay |

### Equations (lane ruling)

An Opus examiner listed and checked every chemical equation, ionic equation and half equation on all 16 pages (template,
logic, quiz, figures, chains, sorts) for atoms, charge and state symbols. All balance except two distractors that
printed H₂ + O₂ → H₂O and called it hydrogen burning (now 2H₂ + O₂ → 2H₂O on pH scale and salts: B11-PH-H2O2,
B11-SN-H2O). State symbols: the spec prints H⁺(aq) + OH⁻(aq) → H₂O(l) (5.4.2.4), so it now carries them everywhere
it is taught (B11-PH-KF-SS, B11-PH-CH-SS, B11-SN-STATE); the spec prints its half equations and ionisation equations
without them (5.4.3.5), so those stay as she wrote them. The lead bromide cell drew three Pb²⁺ to three Br⁻ (charges
not balancing); now two to four (B11-EP-IONS).

### Design's flags, ruled

KEEP: 1.1–1.4; 2.1, 2.3, 2.4; 3.1–3.3; 4.1, 4.2; 5.1, 5.2; 6.1–6.3; 7.1–7.4; 8.1–8.3; 9.1, 9.2; 10.1–10.3; 11.2, 11.3;
12.1, 12.3, 12.4; 13.2–13.4; 14.1–14.3; 15.2, 15.3; 16.1, 16.3, 16.4. CHANGE: 2.2, 5.3, 11.1, 13.1, 15.1, 16.2 (each
Higher layer was hidden, but its key-note line, command-word card or rung text still reached CF and TF); 12.2 (the
Triple titration key-note line reached Combined); 3.4 (±0.15 is right for rubidium, but on the silver item it also
accepted the simple average: B11-RAM-AG).

### Science rulings from the examination (batch 11)

| id | lesson | what changed, and why |
|---|---|---|
| B11-PH-CURVE | pH scale | The pH curve rose only to 7.4 with its steep part at pH 4.4, while the page, its labels, a practice key and rung 4 say "steep through 7, then high". Now 1.4 → 7.0 at the midpoint → 12.6. |
| B11-RAM-21 | relative atomic mass | A wrong option "21" had the reply "That is the simple average of 10 and 11" (21 is the sum). Now 10.5. |
| B11-RAM-AG | relative atomic mass | Silver 13 : 12 gives 107.96, and the ±0.15 tolerance also accepted 108, the simple average this lesson exists to stop. Now thallium-203/205 in 3 : 7 → 204.4 (the simple average 204 is rejected). |
| B11-G7-NOCHANGE | group 7 | Every "no reaction" cell showed a colourless swatch; bromine water stays orange and iodine solution brown. The swatch is now the added halogen's colour. |
| B11-G7-ORANGE | group 7 | Distractor "The solution turns orange" (bromine water + KCl) is defensibly true: the bromine water is orange. Now "turns brown". |
| B11-MCR-H2 | mass changes | Three hydrogen-loss sums claimed 13 g, 4 g and 2 g of H₂ from containers weighing 500, 200 and 300 g (chemically impossible). Now carbon dioxide from marble chips; every number and answer unchanged. |
| B11-CM-MENISCUS | chemical measurements | The meniscus close-up painted its curve over with a rectangle (a flat top under "read the bottom of the meniscus"). Now drawn curved. |
| B11-EP-IONS | electrolysis principles | Lead bromide drawn 3 Pb²⁺ : 3 Br⁻; now 2 : 4. |
| ROUTE (17) | subatomic, group 7, mass changes, oxidation and reduction, salts, pH scale, electrolysis ×2 | B11-SUB-KEYHT, -G7-KEYHT, -G7-ELECTRONS, -MCR-KEYHT, -OXR-KEYFACT, -OXR-KEYNOTE, -OXR-CMDWRITE, -OXR-ELECDIST, -SN-KEYTRIPLE, -PH-KF-HT, -PH-KN-HT, -PH-BIGQ, -EP-KN-HT, -EM-KN-HT/-R4-P/-R4-PTS/-CMD: Higher (or Triple) content outside its gated section now shows only on its routes (the batch 7 B7-RP-KEYFACT class). |
| Taught before tested (5) | relative atomic mass, moles, amounts, oxidation and reduction | One sentence each, before the test: isotopes react the same because reactions involve electrons (B11-RAM-ISOCHEM); a mole of water is 3 × 6.02 × 10²³ atoms (B11-MOL-ATOMS); wanted ÷ given coefficient before the ratio pick (B11-AIE-RATIO); "a reaction in which both happen is called a redox reaction" (B11-OXR-REDOX); standard form stated where the pick relies on it (B11-MOL-SFPICK). |
| CHAIN (14) | 12 lessons | Each chain had a second sensible order that would be marked wrong; linking words force one order (B11-MOA-, -SUB-, -RAM-, -ES-, -G7-CHAIN1/2, -TM-, -MOL-CH1/2, -AIE-CH2, -OXR-ZNCHAIN, -SN-CH2, -SWA-CHAIN1/2). |
| Clarity (the rest) | all | e.g. "Which model first said this?" (Bohr's model is also mostly empty space); Thomson and Rutherford named on the timeline; "even in an ion" on the atomic-number sort item; "Ar has no unit" in the answer box; 2,8,2,1 fallback options for Mg and Ca; O₂ written 1 × 32 not 2 × 16 (the error the page warns against); Mg + 2HCl read in moles as the spec's key-note line; "usually a gas" (the spec's word, not "always"); 10 mol/dm³ sulfuric acid for "concentrated" (2 mol/dm³ is school dilute); "every molecule" for a strong acid (not "nearly every"); a pupil-visible "The pack's example" and "Verbatim" tab renamed; an encouraging wrong reply on the strong/weak opener ("Please not." removed); 18.5 neutrons as the real misconception herring; spectator-ion reply on NaCl. |

### Checks

- **Gates (builder):** `ks4_parity.py --batch batch-11` 784 PASS 0 FAIL; `ks4_batch_check --batch batch-11` clean (56
  pages, 27 assets, freeze); zero console errors at 1280 and 360 px; no `/ks4/`, `.dc.html`, `Batch N` or `href="#"`
  on any page; every href resolves on its route. Diff against main: the 112 batch-11 page files, the new batch-11
  files, `build_ks4.py` (one tuple entry), `ks4_batch_rulings.py` and `knowledge_points/ks4.json`. The inline
  `<sc-if>` inside a sentence (first used here) was proved on the built pages: present on CH TH, absent on CF TF,
  no broken text around it.
- **Independent pupil walk (the same Opus auditor)**, 390 px, light theme, one headless Chrome, all 56 page routes,
  224 loads, everything pressed.
  - Clean on all 56 from the first pass: no console errors, dialogs, sideways scroll, stray tokens or `/ks4/` text;
    no broken link and no link to a page the route lacks; five practice questions and ladder 2·2·2·1 everywhere;
    every rail item ticks; all 32 chains force one order; real subscripts and superscripts throughout, readable
    stacked nuclear symbols, drawn arrows (including ⇌), no lost digits or charges; H⁺(aq) + OH⁻(aq) → H₂O(l) with its
    state symbols on every route; every figure the examination touched holds (pH curve shape, 2 Pb²⁺ : 4 Br⁻, curved
    meniscus, halogen-coloured "no reaction" swatches, the Mg/Ca shell options); Higher and Triple layering right
    apart from the items below; every calculation correct, right answers accepted in sensible forms and the modelled
    mistakes rejected.
  - Fixed after the first pass (`B11W-*`): labels clipped or overrunning (relative atomic mass, subatomic scale,
    transition-metal bench, mass-change readouts, apparatus captions, cathode/anode labels cut by the wires); the pH
    curve's two labels struck through by the new curve, and a "pH" axis title added; a missing space after a
    superscript ("2e⁻loses", "Cl⁻strong", "H⁺weak") on three Higher pages; two tabs and a heading carrying authoring
    words ("Verbatim (bracket corrected)", "Worked (verbatim)"); a doubled "Fair guess."; Higher clauses still on CF and
    TF in two big questions, two command cards and a closing note; "±0.10" rejected on a calculation rung; "How many
    electrons?" asked twice; two replies repeating the bridge after them; practice steps lettered A–E with options
    lettered A–E; a group 7 chain that accepted only one of two sensible orders; "10³" rejected where "1000" was
    wanted (the rungs now ask for a whole number); hyphens for minus signs on the boiling-point chart.
  - Kept: the ion builder draws every electron (it is the teaching figure); nuclear symbols built in script sit side
    by side, not stacked (readable); "Nₐ" in script text (Unicode has no subscript capital A); "n = m ÷ Ar" in the
    mass-changes CFIFA (right for an element); the "(+ 5.4.x.x Higher)" spec reference in four eyebrows; old verbatim
    wording in replies; prev/next by the live order (group 7 CF CH and transition metals TF TH have no Next).

- **Re-walk after the fixes** (same auditor, all 56 page-routes again): 17 of the 18 fixes confirmed in their states
  (D10: "0.10", "± 0.10", "±0.10", "+0.10", "0.1" accepted, "0.2" and "±0.20" rejected; D13 key 2, 3, 1, 4, 5 with each
  distractor still matching its reply; the bars drawn at the true 15× and 8×), and a regression sweep of 56 of 56: no
  console errors, dialogs, sideways scroll or stray tokens; no broken link or link to a page the route lacks; 5/5 after
  retry; ladder 2·2·2·1; 32 of 32 chains one order only; every rail item ticks, including the re-driven CFIFA, Steps and
  triangles on all 18 calculation page-routes.
  - Still to fix then: "atomic number" still clipped (D1, labels moved further); three figure faults the first pass had
    missed (an arrow through "about 1 × 10⁻¹⁰ m"; the "−" of the supply hidden on the wire in both electrolysis cells;
    the wires through "cathode (−)" and "anode (+)" on electrolysis principles, as D16 had been on the molten lesson).
  - **A lead's error, caught by the re-walk.** The group 7 chain was re-ruled by the lead so its three links run
    reason → reactivity → displacement and only one order reads (confirmed: the other five orders are rejected and
    none reads sensibly). In the same pass the lead replaced what it took for a true decoy card, "Reactivity falls down
    the group.", with a false statement; but each decoy is a pair (card, note), and that string was the true NOTE shown
    when a pupil places the decoy "Bromine is more reactive than chlorine." The pupil would have been told something
    false. The ruling was removed, so Design's note stands; nothing shipped with it.

- **Targeted re-checks** (all routes, 390 px): D1 and the three missed figure faults all pass, with Design's true
  decoy note restored. Re-check 3 found one more (the product labels on the molten-electrolysis crucible touched its
  walls, then their subscripts sat on its floor); moved inward and up (`B11W-EM-PRODUCTS`), clear of walls, floor and
  electrodes by the auditor's measurements. Console clean on every re-checked page.
- **Knowledge points:** 979 new question ids tagged by the top-up (15 new points, 0 untagged), and the one item the
  walk fixes changed (salts practice Q4) re-placed; backend `knowledge-points.json` re-exported and pushed before the
  site.

---

## For Mide (nothing here blocks; your call when convenient)

1. **Arctic fox (your ruling 4.3).** The pack gives no functional adaptation that is true of an Arctic fox, so the
   fox's fourth feature is now a structural one the pack supports (thick fur on the soles of its paws); the
   functional type is still classified on the same activity through the fennec fox's concentrated urine. If you would
   rather the fox keep a functional feature, the one Design wrote (reduced blood flow to the paws) is true biology but
   is not in the pack: say so and it goes back.
2. **Old-bank options that give themselves away** (batch 11, about 14 pages; the same class is in earlier batches):
   in Design's verbatim practice items the right option often carries its working and distractors name their own
   mistake, e.g. moles "0.5 g — confusing moles with grams". Stripping the "— …" tails across the bank is a one-rule
   change per page if you want it.
3. **Ks4Guess never shuffles** its two opener options, and the right one is listed first on every page (shared block,
   all batches since 4).
4. **Oxidation and reduction ↔ batch 5.** The new page points to Reactivity series and Extraction of metals; those
   batch 5 pages do not point back. Adding the link would change two pages outside these batches.
5. **Batch 9 links to restore** when batch 9 goes live: the six listed under batch 10 ("Links to batch 9").
6. As after earlier batches: small figure text (down to 6 px at 390 px) and old off-spec words in verbatim replies
   (keystone, niche, aposematism, parasites; capitals for emphasis).
