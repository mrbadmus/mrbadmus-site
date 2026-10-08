# KS4 batch 5 port report (Prompt AB)

Branch `feat/ks4-batch5`, based on `origin/main` at `60160db07` (batch 4 live). Not pushed.
15 lessons, 58 pages (CF CH TF TH, except red-shift-big-bang: TF TH). All `examiner-reviewed`, frozen
(`ks4_lessons/frozen_batch-5.json`). Science decisions: `docs/ks4/BATCH5-SCIENCE-LOG.md`.

## 1. What was built

- **Design's delivery sits verbatim** in `docs/ks4/design-reference/batch-5/lessons/` with `MD5SUMS`. Nothing edited.
- **Her shared blocks are byte-identical to batch 4's.** Checked with `cmp` against `batch-4/lessons/`: all 14 `Ks4*.dc.html`
  blocks, `ks4-lib.js`, `ks4-diagrams.js`, `ks4-theme.css` and `support.js` are the same bytes. Her NOTES say so; confirmed.
- **`ks4_lessons/batch_5.py`**: 15 records, `port_rulings=True`, batch-4's block set read from batch 5's own copy,
  `review_state="examiner-reviewed"`, draft banner off. Slug = filename minus `ks4-<subject>-<spec>-`. Topics agree with
  `FULL_NAV` (all_subtopics): land-use, waste-management, global-warming (biology/ecology); plant-tissues (biology/organisation);
  metals-non-metals, group-0 (chemistry/atomic-structure); reactivity-series, extraction-of-metals (chemistry/chemical-changes);
  earths-resources, potable-water (chemistry/resources); energy-resources (physics/energy); structure-of-atom,
  development-atomic-model, radioactive-decay (physics/atomic-structure); red-shift-big-bang (physics/space, TF TH).
- **Batch-only assets**: `shared/ks4-lesson-batch-5.css`, `shared/ks4-source-batch-5.js`, `shared/ks4-ext-batch-5.js` (source
  `ks4_lessons/batch5_ext.js`, identical code to batch 4's: the quiz text carries `₂`-style subscript escapes, so the
  display-time `<sub>` asset is needed). `shared/ks4-nav.js` did not change a byte.
- **Section classification**: ten lessons needed `block_map` entries for sections the heuristic cannot type (`explainer`;
  `s-rp` is typed `required-practical` automatically).

## 2. Engine changes (and why)

1. `ks4_batch_rulings.py` `_HREF_RE` / `apply_connects`: also reads `href: '../KS4 Batch N/<file>.dc.html'` (six of Design's
   cross-batch connects) and resolves a file through every registered batch (and the pilot), fail-loud on an unknown file.
   Every batch-4 href matches as before.
2. `ks4_batch_rulings.py` `apply_inline_links` (B-INLINE-LINKS): the four in-text `<a href="ks4-….dc.html">` template links
   (waste-management to potable-water, land-use to global-warming, group-0 and structure-of-atom to metals-non-metals) become a
   bound `{{ mrbLink_<slug> }}` filled by `KS4.hrefFor(slug, R)`, so each is the live per-route URL. Fail-loud on an unknown file or a
   `renderVals` that does not `return Object.assign({}, R, {`. A page with no such link is untouched.
3. `build_ks4.py` `compile_batch_lesson`: passes the all-batch file-to-slug map to `port_lesson`.
4. `docs/ks4/batch-engine.md` §8: one paragraph recording 1 and 2.
5. `B5-RSBB-CHIP` (port mechanic) in `SCIENCE`: see the science log.

## 3. Links (G3)

Prev/next follow the live per-route order (B-PREVNEXT, `compute_prev_next`): checked on all 58 pages, 104 expected neighbours all
present as anchors. 468 in-page `/…` links on the 58 pages all resolve to a built file. No `.dc.html` or `KS4 Batch` text survives in
any page. Connects: every batch-5 page, on every route, shows "Connects to" with at least one link; **no batch-5 lesson passes an
empty connects list** (waste-management shows two).

## 4. Byte identity

`git diff --name-only origin/main` after `build_ks4.py --batch batch-5`, `--freeze`, and one `build_all.py` lists exactly: the 58
batch-5 pages in `combined/` + `triple/`, the same 58 in `mrbadmus_site/`, `build_ks4.py`, `ks4_batch_rulings.py` (plus the
new, untracked batch-5 files and docs). The pilot, batches 2, 3 and 4 (all their pages and manifests), `shared/ks4-nav.js`,
every other shared asset and every KS3, teacher, student and B2C file are byte-identical to `origin/main`.

## 5. Checks

- 390 px, one headless Chrome, all 58 pages, every enabled button pressed once (plus ranges): zero console errors (the
  localhost-to-backend CORS noise excluded, as `ks4_parity` does), no `window.alert`, opener "If you had to guess, …?" with two
  cards, five practice questions, ladder 2·2·2·1, no visible `undefined` / `NaN` / `{{`, no horizontal scroll. The six rulings
  visibly applied (see the science log).
- Gates run once each, foreground: `ks4_pilot_check` clean (54 pages, 17 assets); `ks4_batch_check` clean for batches 2, 3, 4, 5
  (batch 5: 58 pages, 21 assets); `ks4_parity.py --batch batch-5` 812 PASS, 0 FAIL; `ks4_science_rulings.py --check` 101 OK.
  Not run: the other slow gates (the lead runs them).

## 6. Known, left as Design drew them

Drawings are Design's schematic figures; tiny SVG labels at 390 px; Ks4Steps placeholders tight at 320 px (batch-4 fix applies at
360 and above).
