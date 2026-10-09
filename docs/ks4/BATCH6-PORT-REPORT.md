# KS4 batch 6 port report (Prompt AB)

Branch `feat/ks4-batch6`, based on `origin/main` at `b9a9f5488` (batches 4 and 5 live). Not pushed.
14 lessons, 50 pages (CF CH TF TH, except factors-affecting-food-security, stellar-evolution and
culturing-microorganisms: TF TH). All `examiner-reviewed`, frozen (`ks4_lessons/frozen_batch-6.json`). Science decisions:
`docs/ks4/BATCH6-SCIENCE-LOG.md`.

## 1. What was built

- **Design's delivery sits verbatim** in `docs/ks4/design-reference/batch-6/lessons/` with `MD5SUMS`. Nothing edited.
- **Her shared blocks vs batch 5's (`cmp`):** every `Ks4*.dc.html` block except one, `ks4-lib.js`, `ks4-diagrams.js`,
  `ks4-theme.css` and `support.js` are the same bytes. The only block that differs is **`Ks4Triangle.dc.html`**
  (two lines: `fixed = !!(item && (item.half || item.fixed))` and the aria text for a fixed cell, "pi, about 3.14, a
  fixed number"). `NOTES-KS4-batch-6.md` and `README.txt` differ too (they are batch 6's own). Her NOTES say only
  Ks4Triangle changed; confirmed.
- **`ks4_lessons/batch_6.py`**: 14 records, `port_rulings=True`, its OWN block set read from batch 6's own copy,
  `review_state="examiner-reviewed"`, draft banner off. Slug = filename minus `ks4-<subject>-<spec>-`
  (`transpiration` and `translocation` share spec 4.2.3.2). Routes and topics agree with `FULL_NAV`:
  factors-affecting-food-security (biology/ecology, TF TH), group-1 (chemistry/atomic-structure),
  reactions-of-acids (chemistry/chemical-changes), stellar-evolution (physics/space, TF TH), animal-plant-cells,
  cell-specialisation, stem-cells (biology/cell-biology), culturing-microorganisms (biology/cell-biology, TF TH),
  principles-of-organisation, digestive-system, health-disease, cancer, transpiration, translocation
  (biology/organisation).
- **Batch-only assets**: `shared/ks4-lesson-batch-6.css`, `shared/ks4-source-batch-6.js`, `shared/ks4-ext-batch-6.js`
  (source `ks4_lessons/batch6_ext.js`, a copy of `batch5_ext.js` AS IT NOW IS: SVG `<tspan baseline-shift="sub">`
  inside figure labels, added `<svg>` nodes scanned). Needed: the quiz text carries `₂`-style subscripts
  (group-1 22, acids 106, transpiration 7, translocation 1). `shared/ks4-nav.js` and `shared/ks4-lib.js` did not
  change a byte.
- **Section classification**: eleven lessons needed `block_map` entries (all `explainer`).

## 2. Engine changes (and why)

1. `ks4_batch_rulings.py` `_HREF_RE` and `_TPL_HREF_RE` share one prefix pattern `_XB`: any run of `../`, optional
   `KS4 `, `Batch N/`, optional `lessons/`. Batch 6 writes `../../Batch 5/lessons/<file>.dc.html` (logic and
   template); batches 4 and 5 wrote `../KS4 Batch N/<file>` and still match. A file in no registered batch (or the
   pilot) is still a `RulingError`.
2. `port_lesson` ends with a fail-loud guard: any `<file>.dc.html` or `Batch N/lessons/` left in the template or logic
   raises. (Batches 4 and 5 pass it; their builds are unchanged.)
3. Fresh-`renderVals` lessons: culturing-microorganisms, factors-affecting-food-security, stellar-evolution return a
   fresh object, so B-R12 raised. Three named one-line rulings pass `routeWords` / `routeSwitchOptions`
   (B6-CM-CHIP, B6-FS-CHIP, B6-SE-CHIP), as B4-IRB-CHIP and B5-RSBB-CHIP did. B-R12 still fails loud without them.
4. `tripleOptions` route picker: B-R1 matched it as it did for batch 5's red-shift (the select is dropped); the chip
   on all three offers only the other Triple route (checked in the DOM: Triple Foundation page lists Triple Higher
   only, and the reverse).
5. Two text pointers Design left as plain words ("Code to wire") became links by named rulings that wrap her exact
   words and add no new ones: B6-PTR-MICRO-1/2 (animal-plant-cells, "Microscopy lesson") and B6-PTR-ENZ-1/2
   (digestive-system, "Enzymes lesson"), each via `window.KS4.hrefFor(slug, R)` (`ks4-nav.js` covers both targets
   on all four routes).
6. `docs/ks4/batch-engine.md` §8: one paragraph recording 1 to 3.
7. B-INLINE-LINKS needed no change for the fresh-object lessons: none of the three has an in-text link.
   (It still raises if one ever does.)

## 3. Links (G3)

Prev/next follow the live per-route order (`compute_prev_next`): 90 expected neighbours across the 50 pages, all
present. Every in-page `/…` link on all 50 pages resolves to a built file (checked in the DOM after pressing every
control). No `.dc.html` or `Batch N/lessons/` text survives anywhere in a built page. Connects: **no batch-6 lesson
shows an empty "Connects to" list** on any route. Counts: group-1 2, cancer 2, cell-specialisation 3, every other
lesson 1.

## 4. Transpiration

Design's file has no rate calculations; ported as it is, nothing written. **Transpiration rate calculations pending
from Design.**

## 5. Byte identity

After `build_ks4.py --batch batch-6`, `--freeze` and one `build_all.py`, `git diff --name-only origin/main` lists
exactly: the 50 batch-6 pages in `combined/` + `triple/`, the same 50 in `mrbadmus_site/`, and `ks4_batch_rulings.py`
(plus untracked new batch-6 files and these docs). The 100 batch-4 page paths and 116 batch-5 page paths
(both trees) are byte-identical to `origin/main` (`git diff --quiet` per path), as are the pilot manifest, the
batch 2, 3, 4 and 5 manifests, `shared/ks4-nav.js`, `shared/ks4-lib.js`, `shared/ks4-ext-batch-4.js` and
`shared/ks4-ext-batch-5.js`. Nothing else in the tree moved.

## 6. Checks

- 390 px, one headless Chrome, all 50 pages, every enabled button pressed (up to six passes) plus every range at
  min, middle and max: zero console errors (localhost-to-backend CORS noise excluded), no `window.alert` / confirm /
  prompt, opener "If you had to guess, …?" with two cards on every page, practice set exactly five, ladder 2·2·2·1,
  no visible `undefined` / `NaN` / `{{`, no horizontal scroll (scrollWidth 390), no page navigation, every link
  resolves. 50 of 50 pass. The pi cell in the culturing triangle is a disabled button with the "pi, about 3.14, a fixed
  number" label and cannot raise an alert.
- Figure subscripts: for fifteen representative pages, each button pressed one at a time with the figures re-read
  after each press (about 1,000 states): no SVG `<text>` holds an HTML `<sub>`/`<sup>` or a raw Unicode
  subscript or superscript digit. No batch-6 figure label carries a subscript (zero SVG tspans were needed); HTML
  subscripts are written by the ext asset (group-1 16, acids 52, transpiration 6 `<sub>`; no raw `₂` left).
- Rulings visibly applied: see the science log.
- Gates, once each, foreground: `ks4_pilot_check` clean (54 pages, 17 assets); `ks4_batch_check` clean for batches
  2, 3, 4, 5 and 6 (batch 6: 50 pages, 21 assets); `ks4_parity.py --batch batch-6` 700 PASS, 0 FAIL;
  `ks4_science_rulings.py --check` 101 OK, 0 MISS. Not run: the other slow gates (the lead runs them).
  `ks4_chrome_drive` was left alone (it samples `energy-stores-systems`, which no batch ports).

## 7. Known, left as Design drew them

- Superscripts in JS-built text (Mg²⁺, 10ⁿ, mm²) are plain Unicode characters in the system font fallback, as in
  batch 5 (Design's G1). Only subscripts are rewritten, by the ext asset.
- Translocation's hook ("A sack of potatoes") and its reply still say the sugar is stored "in the potato or carrot";
  only the sink note was ruled (B6-TL-SINK).
- The first `build_all.py` run died at step 2 on a Chrome websocket timeout (memory pressure from other sessions);
  the second run completed clean with no change to the tree.
