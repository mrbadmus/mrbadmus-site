# KS4 batch 4 port report (Prompt AA)

Branch `feat/ks4-batch4`, based on `origin/main` at `692a23f2f` (main has moved since: merge, do not assume a fast-forward). Not pushed.
13 lessons, 50 pages (CF CH TF TH, except infrared: TF TH). All `examiner-reviewed` and frozen (`ks4_lessons/frozen_batch-4.json`).
Every science decision, with its source line, is in `docs/ks4/BATCH4-SCIENCE-LOG.md`; this report summarises it and does not repeat the working.

## 1. What was built

- **Design's delivery sits verbatim** in `docs/ks4/design-reference/batch-4/` (`MD5SUMS`). Nothing in it was edited.
- **Port mechanics are named rulings** in `ks4_batch_rulings.py`: B-R1 (Route select off), B-R12 (one route chip), B-PREVNEXT and B-CONNECTS (live order), B-PRACTICE-PARSE (decimal comma in the ladder number box), the per-lesson SCIENCE table (below), and B4-TRI-TOP (triangle label).
- **Batch-level blocks**: batch-4 pages register their own block set (Ks4Triangle, Ks4Guess, Ks4Steps, Ks4Practice, five-question Ks4QuizBank, Ks4Cfifa with the triangle under Formula). The pilot and batches 2 and 3 never take this path.
- **Batch-only assets**: `shared/ks4-lesson-batch-4.css` (Design's own styles plus the phone placeholder fix), `shared/ks4-source-batch-4.js`, `shared/ks4-ext-batch-4.js` (display-time `<sub>`; source `ks4_lessons/batch4_ext.js`).
- Engine doc: `docs/ks4/batch-engine.md` section 8.

## 2. The 13 lessons

Rules: 1 = two-option "If you had to guess, …?" opener; 2 = tap-to-cover triangles (physics "On the sheet", biology no chip and "Written out"); 3 = each step taught before it is tested, chained calculations worked then attempted; 4 = ladder 2·2·2·1 and five quiz questions on every route. Every row is **checked on every route it serves**: rule 1 (two buttons), rule 4 (7 ladder questions in the source, five quiz items rendered, no "Shape:" alert after pressing every enabled control), and Prev/Next (against the live per-route order, no dead links).

| # | Slug (spec) | Routes | Rule 2 | Rule 3 | Interactives driven | Numbers recomputed | Prev / Next (live order) |
|---|---|---|---|---|---|---|---|
| 1 | heart-blood-vessels (4.2.2.2) | CF CH TF TH | 2 triangles, no chip, "Written out" | CFIFA examples then attempts before ladder | circuit walk (10 stops), sort, think, CFIFA tabs | 4.0; 84; 5.0; 72; 0.60; ladder 72, 4.5 | enzymes / blood |
| 2 | water-cycle (4.7.2.2) | all | none | none | drop walk (9 stops), sort, think | none | carbon-cycle / decomposition |
| 3 | atmospheric-pollutants (5.9.3.1) | all | none | none | 4-case predictor, sort, think | equations S + O2, N2 + O2 balanced | greenhouse-gases / none |
| 4 | efficiency (6.1.2.2) | all; Higher layer CH TH | 2 triangles, "On the sheet" on all four routes | worked Steps (0.80 x 2000) then attempt (35% of 60 kJ) before ladder | Sankey presets and slider, triangles, CFIFA, Steps | 0.35; 0.72; 24 W; 0.75; 4500 J; 1600/400 J; 21 000/39 000 J; 0.05; 2600 J; 0.15, 0.375; quiz 200 J, 89 J/s, 1700 W, 0.25 | energy-transfers-in-a-system / energy-resources |
| 5 | infrared-black-bodies (4.6.3) | TF TH; layer TH | none | none | temperature slider (7 stops), sort, think | peaks 3.0, 2.3, 1.6, 1.0, 0.77, 0.50 um | TF: lenses / none; TH: lenses / radiation-balance-temperature |
| 6 | transport-in-cells (4.1.3) | all; RP2 on CF CH, RP3 on TF TH | 3 triangles, no chip, "Written out" | SA:V three-step worked (2 cm) then attempt (3 cm) before ladder | membrane, cells, RP graph, cubes, CFIFA, Steps | -15%; +12%; 0.005; -12.5%; 0.01 g/min; +15%; SA:V 6:1, 3:1, 2:1, 1.5:1; crossing about 0.37 | stem-cells / none (CF CH), culturing-microorganisms (TF TH) |
| 7 | blood (4.2.2.3) | all | none | none | smear walk (4 cells name then job), sort, think | none | heart-blood-vessels / coronary-heart-disease |
| 8 | periodic-table (5.1.2.1) | all | none | none | atom builder (+1/-1, Z = 1-20), sort, think | 2.8.2 = P3 G2; 2.8.5 = P3 G5; neon outer 8 | electronic-structure / development-periodic-table |
| 9 | thermal-conductivity (6.1.2.1) | all; RP2 layer TF TH | none | none | wall model (predict then change), sort, think | model ratios only (stone 3x block; thick 3x thin) | energy-resources / none |
| 10 | coronary-heart-disease (4.2.2.4) | all | none | none | artery stages slider, 3-patient choice, sort, think | none | blood / health-disease |
| 11 | biodiversity (4.7.3.1) | all | none | none | two food webs, sort (three threats), think | web cascades re-derived (5 and 10 species) | population-competition / waste-management |
| 12 | development-periodic-table (5.1.2.2) | all | none | none | four Mendeleev moves, sort, think | Te 52 p 127.6, I 53 p 126.9, Ar 18 p 39.9, K 19 p 39.1 | periodic-table / metals-non-metals |
| 13 | uses-em-waves (6.6.2.4) | all; Higher layer CH TH | none | none | spectrum figure, sort, think | none | properties-em-waves-2 / none (CF), wave-front-refraction (CH TH), lenses (TF) |

Hook questions, as rendered: every one reads "If you had to guess, …?" with its own question and exactly two cards.

## 3. Science flags: ruling, change, source

Detail per flag is in the log. Summary of every change made to Design's text (all else verified and kept as drawn):

| id | lesson | ruling and change | source |
|---|---|---|---|
| B4-IRB-GLOW-1..4 | infrared | Mide: hot-metal colours. Slider adds a 700 C stop; 700 dull red, 1000 orange, 1500 yellow-white, 2500+ white; default stop 1000 C. Curves and peaks untouched. | Mide; FLAGS IRB-F1/F2 |
| B4-IRB-CHIP | infrared | route chip got no words (fresh return object); passes `routeWords` / `routeSwitchOptions`. `port_lesson` now fails if a lesson cannot feed the chip. | engine |
| B4-TC-VERDICT | thermal-conductivity | "about the same" verdict described a ninefold change, not a cancel; now "One change raises the rate threefold and the other lowers it threefold, so they cancel out." | own recompute |
| B4-PT-F1 | periodic-table | transition-metals pointer shown on TF TH only | FLAGS PERIODIC-TABLE-F1 |
| B4-DPT-F3 | development-periodic-table | "Argon and potassium, found later" implied potassium was later; now "Argon, found later, and potassium" | FLAGS DEVELOPMENT-PERIODIC-TABLE-F3 |
| B4-AP-STOVE | atmospheric-pollutants | reply said a camping stove is "not hot enough" for NOx; re-cut | own check |
| B4-AP-F2 | atmospheric-pollutants | distractor "The catalytic converter" (off-spec) became "The engine oil" | FLAGS ATMOSPHERIC-POLLUTANTS-F2/F8 |
| B4-BIO-SORT-1..3 | biodiversity | Mide 11.2: sort now covers the three threats (Waste, Deforestation, Global warming); hedgerow, breeding and field-margin cards removed | Mide; FLAGS BIODIVERSITY-F9 |
| G2 (ext asset) | blood | the one Unicode subscript shows as real CO<sub>2</sub> at display time | Mide / MRB-302 |
| B4-EFF-SANKEY | efficiency | drawing 380 -> 410 high so the wasted arrowhead stays in the box at every preset | review |
| B4-TIC-CAPTIONS-1..2 | transport-in-cells | three membrane captions split at their own middle dot onto two lines (words unchanged) | review |
| B4-TRI-TOP | all triangles | long top labels ("useful") set smaller and a little lower so the apex sides no longer cross the letters | review |
| EXTRA_CSS | batch 4 | placeholders fit the Steps / CFIFA inputs at 360 and 390 | review |

Mide's other rulings applied as drawn (no change needed): G1 biology no chip, 12.2 arsenic kept, 12.3 no Newlands table, 13.3 UV lamp reason kept, 2.2 snow runoff kept, G2 Delta and arrow left in the system fallback font like the pilot.
Pack flags (every numbered flag for these 13 lessons): each checked against Design's page; the log lists what it found for each lesson. No wrong number, unit or key remained after the changes above.

## 4. Files changed (against base `692a23f2f`)

- Engine and registry: `build_ks4.py`, `ks4_batch_rulings.py` (new), `ks4_lessons/__init__.py`, `ks4_lessons/blocks.py`, `ks4_lessons/batch_4.py` (new), `ks4_lessons/batch4_ext.js` (new), `ks4_lessons/frozen_batch-4.json` (new), `ks4_batch-4_manifest.json` (new).
- Docs: `docs/ks4/BATCH4-PORT-REPORT.md`, `docs/ks4/BATCH4-SCIENCE-LOG.md`, `docs/ks4/batch-engine.md`, `docs/ks4/design-reference/batch-4/**` (Design's files, verbatim).
- Batch-only assets: `shared/ks4-{lesson-batch-4.css,source-batch-4.js,ext-batch-4.js}` and the same three in `mrbadmus_site/shared/`.
- Pages: 50 under `combined/` and `triple/` and 50 under `mrbadmus_site/` (replacing the old-data pages at the same URLs; infrared CF CH had no page and gets none).
- Nothing else. No shared asset, no pilot file, no `all_subtopics_*.py`, no B2C file, no `robots.txt`, no sitemap.

## 5. Pilot byte-identity and other pages

Procedure, run after every change set and finally after the three review fixes: `generate_site_v5.py` (which rewrites about 400 pages with old-data output), then `build_ks4.py` for every batch (restores them), then `git status`. Final result: **104 modified files = the 100 batch-4 pages plus `build_ks4.py`, `ks4_batch_rulings.py`, `ks4_batch-4_manifest.json`, `frozen_batch-4.json`**. The pilot's 54 pages and 17 assets, batch 2 (52 pages), batch 3 (44 pages) and every other page came back byte-identical. A full `build_all.py` run (earlier, exit 0) gave the same result and left the B2C pages, `robots.txt` and the sitemap alone (unset `CONSUMER_SIGNUP_ENABLED` uses the committed value).
Gates: `ks4_pilot_check` clean (54 pages, 17 assets); `ks4_batch_check` clean for batches 2, 3 and 4 (50 pages, 21 assets); `ks4_parity --batch batch-4` 700 PASS, 0 FAIL; `ks4_science_rulings --batch batch-4` has nothing registered (batch-4 rulings live in `ks4_batch_rulings.py`).

## 6. Frozen corrections

`docs/ks4/FROZEN-CORRECTIONS.md` covers batch 2 and batch 3 items and atom economy; none of the 13 batch-4 slugs appears in it, and this branch does not touch any `all_subtopics_*.py` (`git diff 692a23f2f -- all_subtopics_*.py` is empty). The 13 replaced pages serve their own authored quizzes, not the old frozen data. Every page this run does not replace is byte-identical, so the merged 4 Oct corrections survive on all of them.

## 7. How this was verified (what was exhaustive, what was sampled)

- **Exhaustive, by me:** every lesson read in full (template and logic); every number recomputed; every flag in the pack checked; all 50 pages built with zero console errors at 1280 and 360; all 50 rendered at 1280 and 390, light and dark, with no horizontal scroll and no "Shape:" alert; every enabled control pressed once on every page; rule 1, rule 4 and Prev/Next structurally on all 50; every placeholder in every line input measured at 360 and 390 (368 inputs).
- **Exhaustive, by the independent auditor (`scratchpad/audit/`):** a scripted pupil walk at 390 px, light theme, on **all 50 pages**: both options of every opener, every think-again option, a wrong then a corrected sort, every triangle, worked Steps and attempts typed and checked, the whole ladder with a mix of right and wrong answers and "Retry my misses", all five quiz questions with retry, link check, and global render checks (overflow, clipped text, bad tokens, contrast). Result: 49 of 50 pages fully clean. One flag (`periodic-table` TH, builder): the harness saw "no text change" after pressing the +1 and -1 buttons; I re-ran it by hand and the atom line, period and group all change (Li to Be to B to Be), so it is a harness artefact. A 390 dark sweep of the global checks passed on all 50. A 1280 light sweep flagged the same "clipped text" item on all 50 pages: those are the 1-pixel visually hidden "Light / Dark / System" labels in the shared top bar, not batch-4 content.
- **Sampled:** screenshots (I viewed a sample across lessons, routes and both themes, not all 200); the deep per-lesson interactive drives (circuit, water journey, smear, atom builder, patients, food webs) were run on the Triple Higher route, with the other routes covered by the generic walk and by the shared logic being identical across routes; the dark-theme interactive walk was run in full on one page (efficiency TH) and as a global check on the rest.
- **Not done:** no real-device test; no check of the live site (nothing is pushed); the examiner-level science judgement is Mide's, not the audit's.

## 8. Known cosmetics, left as Design drew them

- Tiny SVG labels at 390 (membrane captions, mini periodic table, figure labels).
- Minor label overlaps: "energy" over dots in the active-transport panel, "concentrated" over a particle, "satellite" and the atmosphere caption crossing arrows, cycle-figure labels.
- At 500 C the infrared peak (3.7 um) is off the right edge of the 0-3 um axis (the peak text is right).
- At 320 px wide the Steps / CFIFA placeholders are still tight (fixed for 360 and above).

## 9. Not sure: for Mide

1. **EM-waves CH TH quiz keeps the ionosphere item and the UV-sterilisation item.** Both are pack-sanctioned (UEM-F3, F4) and lane-ruled as standing. UV sterilising is not on the AQA spec and conflicts with the lesson's own gamma line ("gamma rays ... sterilise medical equipment"); "radio waves reflect off the ionosphere" is true only of long, medium and short-wave radio, not FM or TV. The lesson's own explanation says "pass through the atmosphere", which is safer.
2. **Thermal conductivity RP2 "Physics only" labelling** follows pack TC-F1 (page on all four routes, RP2 as a TF TH layer). The auditor could not verify the AQA numbering independently; the pack is the only source.
3. **Pollutant predictor "CO and soot".** It treats carbon monoxide and soot as arriving together under limited oxygen; the pack says "CO and/or C". A pupil who ticks only CO sees "Here is the full set", not a wrong-idea message.
4. **The 700 C slider stop was added** (infrared) so "dull red" has a stop; Design had six stops and none at which it was true. Planck curves and peaks are untouched.
5. **Newlands is named in text only** (no octaves table), per ruling 12.3.
6. **Quiz options carry per-option working text** (a reply under every option). It is Design's and the pack's text and was not compared with the wording of earlier batches.
7. **Long header on physics pages.** The header (chip, equation-sheet link, two compact triangles) pushes "Start here" about 1,400 px down on a phone.
8. **"Steam vs cloud" wording.** Raised in the pupil walk: the water cycle's "Think again" says the white plume above a kettle is droplets, not vapour. I checked it and it is correct science (a visible cloud or plume is liquid droplets), but it is a plain-language correction of everyday "steam", so it is worth your eye.
9. Draft banner is off on all 13 and the lessons are frozen. Reverting is `review_state` in `ks4_lessons/batch_4.py` plus a re-freeze.
