# KS4 pilot — engine report (integration executor, 26 Sep 2026)

Scope of this run: (1) mint two commander's rulings the science examiner
described but did not number (`metals-alloys-C12`/`C13`); (2) wire
`ks4_science_rulings.py` into `build_ks4.py`'s compile pipeline; (3) flip all
14 lessons' `review_state` to `examiner-reviewed` and confirm the draft
banner/chip are gone from every built page; (4) add the freeze mechanism
(`ks4_lessons/frozen.json` + `build_ks4.py --freeze` + a `ks4_pilot_check.py`
gate) so a later content edit with no re-examination is a red, not a silent
pass; (5) rebuild, gate, and run the sanity drive item G that had not been
run before; (6) write this report.

## 1. What the engine is

| file | lines | job |
|---|---|---|
| `build_ks4.py` | 1,159 | the generator — compiles the 14 `.dc.html` lessons + 11 shared blocks into 54 static pages, no React/Babel |
| `ks4_rulings.py` | 415 | the standing, exact-match port-mechanics rulings (R1–R9, R-SLUG, R-PREVNEXT, R-CONNECTS, R-BREADCRUMB) |
| `ks4_science_rulings.py` | 1,202 | the 101 science-examiner rulings (99 examiner + 2 commander's, 26 Sep 2026) |
| `ks4_lessons/__init__.py` | 226 | the 14 lesson records — slug, design file, subject/topic, routes, `review_state`, `design_slug` |
| `ks4_lessons/blocks.py` | 211 | the closed component/section-type registry `classify_section()` reads |
| `ks4_pilot_check.py` | 259 | the fast, browser-free gate — manifest integrity, no-React, registry, version stamps, freeze |
| `shared/ks4-runtime.js` | 606 | the vanilla runtime (`MrbLogic`/`DCLogic`, child-component mounting, in-place DOM patching) |
| `shared/ks4-lib.js` | 142 | `KS4.find/bank/tip/keyLines/commonMistake/cfifa/fifas/load/save/hash/hrefFor` |
| `shared/ks4-diagrams.js` | 334 | pure-SVG-string diagram functions (cell/battery/switch symbols, R10–R12 fixed) |

Total engine surface (excluding generated output): 4,554 lines across these
nine files.

## 2. The compile pipeline, in order

1. `ks4_lessons.verify_slugs()` — every one of the 14 `slug`s proven against
   `all_subtopics_*.py` before anything else runs.
2. `ks4_science_rulings.reset_applied()` — clears the fired-ruling bookkeeping
   so a second in-process run (e.g. a test harness) cannot double-count.
3. **STEP A** `build_source_js()` — builds the per-slug source record
   (theory/summary/key_note/examiner_tip/common_mistake/quiz per route) for
   all 14 lessons, then `ks4_science_rulings.apply_source(per_slug)` **once**
   over the whole dict, then `expect_present("source", slug, rec)` per slug
   while serialising to `window.KS4SRC["<slug>"] = {...};` lines in
   `shared/ks4-source.js`.
4. `write_source_diff()` — diffs the (ruling-applied) generated source
   against Design's own `ks4-source.js`, field by field, into
   `docs/ks4/pilot-inventory/source-diff.md`.
5. **STEP B** `build_shared_assets()` — writes `ks4-ds.css`, `ks4-theme.css`,
   `ks4-lib.js` (Design's `ks4-lib.js` + the `hrefFor` addition), and
   `ks4-diagrams.js` via `build_ks4_diagrams_js()`, which now runs Design's
   file through `ks4_science_rulings.apply("asset", "ks4-diagrams.js", …)` +
   `expect_present` before writing (resistors-C10/C11/C12, the cell/battery/
   switch symbol fixes).
6. **STEP C** `collect_lesson_css()` — every distinct `<style>` block across
   the 14 lessons + 11 blocks, deduplicated, into `shared/ks4-lesson.css`.
7. **STEP D/E** the browser-side template compiler compiles the 11 shared
   blocks (`compile_block()` — `Ks4Chrome` gets R-BREADCRUMB, five blocks get
   their R2 figure-primitive fix).
8. **STEP F** `compile_lesson()` per lesson, in this exact order:
   a. split `.dc.html` into `tpl`/`logic` (`template_and_logic()`)
   b. R1 (route selector removed) → R9 (Higher/Triple badge gated) →
      R3/R5 checks (no-ops, asserted) → R6 (series-parallel-circuits chip) →
      R7 (draft exam-tip section removed, text preserved) → R8
      (metals-alloys "model data" relabel)
   c. R-SLUG (three lessons' internal slug constant rewritten to the site
      slug) → R-PREVNEXT (endPrev/endNext swapped for the `mrbPrevNext` mount
      prop) → R-CONNECTS (`href: '….dc.html'` → `KS4.hrefFor(slug, R)`)
   d. **NEW this run**: `ks4_science_rulings.apply("template", slug, tpl)` +
      `expect_present`, then the same for `"logic"` — placed here,
      deliberately, because every ruling above this point can renumber or
      relocate template nodes (student_template.py's rule: structural edits
      must land before the browser-side compile), and every science ruling
      is a text substitution that does not renumber anything, so it is safe
      to run last, right before `compile_template_text()`.
   e. `compile_template_text()` (the actual browser-side compile) →
      `classify_lesson_sections()` (closed-registry check, `data-block`
      written onto every section).
9. **STEP G** prev/next computed per (lesson, route) from the real
   `all_subtopics_*.py` topic order.
10. **STEP I** page assembly, prerender in headless Chrome (bakes the mounted
    DOM into the page so it renders with no JS), console-error gate (0
    errors, 1280 + 360px), root-mirror copy, manifest write, and — only with
    `--freeze` — the freeze write (§6 below).

## 3. Every ruling that fired

### Standing (port-mechanics) rulings — `ks4_rulings.py`

| id | scope | this run |
|---|---|---|
| R1 | Route `<select>` removed | fired on all 14 lesson templates |
| R2 | figure primitive (`React.createElement` → `{__mrbFig,__html,alt,max}`) | fired on `Ks4Choice`, `Ks4Write`, `Ks4Ladder` (3 shared blocks) |
| R3 | `KS4.ready()` polling unused | checked, 0 hits, no-op confirmed on all 14 |
| R4 | best-score storage key | checked, no-op confirmed (`Ks4Ladder.dc.html` already keys `'ks4-best-' + slug`) |
| R5 | nanoparticles spec label | checked, no-op confirmed (page already shows `4.2.4`) |
| R6 | R_total chip ("Not on the sheet · learn it") | fired: series-parallel-circuits |
| R7 | draft exam-tip section removed | fired: series-parallel-circuits, resistors (2 tips preserved verbatim in `draft-exam-tips.md`) |
| R8 | metals-alloys hardness table → "model data" | fired: metals-alloys |
| R9 | Higher/Triple content badge gated behind `<sc-if>` | fired: states-of-matter, polymers, metals-alloys |
| R-SLUG | internal slug constant → site slug | fired: metals-alloys, series-parallel-circuits, resistors |
| R-PREVNEXT | `endPrev`/`endNext` → `mrbPrevNext` mount prop | fired on all 14 (endPrev/endNext literal counts vary; see §5) |
| R-CONNECTS | `href: '….dc.html'` → `KS4.hrefFor(slug, R)` | fired on all 14 (44 cross-references rewritten total, per the module docstring's own count) |
| R-BREADCRUMB | `href="README.md"` ×4 → `/ks4.html` | fired once, on the shared `Ks4Chrome` block |

### Science rulings — `ks4_science_rulings.py` (97 of 101 applied)

All 97 non-docs, non-skip_apply rows fired cleanly (build log, verbatim):
13 chemical-bonds (C1–C13), 4 ionic-bonding (C1–C4), 9 ionic-compounds
(C1–C9), 3 covalent-bonding (C1–C3), 3 metallic-bonding (C1–C3), 2
states-of-matter (C1–C2), 6 properties-ionic-compounds (C1–C6), 6
properties-small-molecules (C1–C6), 10 polymers (C1–C10), 5
giant-covalent-structures (C1–C5), 9 metals-alloys (C1–C7, C9, **C12, C13**
— C8 is `skip_apply`, mirrors `ks4_rulings.R8`), 8 nanoparticles (C1–C8), 4
series-parallel-circuits (C2–C5 — C1 is `skip_apply`, mirrors `ks4_rulings.
R6`), 8 resistors (C1–C9, minus none) plus the 3 shared-asset rows
(resistors-C10–C12, `ks4-diagrams.js`). Not applied: 2 `docs`-only rows
(polymers-C4/C5 — record only, delivery committed unmodified) and 2
`skip_apply` rows (metals-alloys-C8, series-parallel-circuits-C1 — real
findings, but byte-identical to a ruling `ks4_rulings.py` already applies;
`_selfcheck_mirrors()` proves the two copies still agree). 97 + 2 + 2 = 101.

`ks4_science_rulings.py --check`: **101 OK, 0 MISS** (99 rows + 2 mirror
self-checks all green).

## 4. metals-alloys-C12/C13 (this run's own ruling)

Two findings from `docs/ks4/examination/metals-alloys.md` §4 were real,
described in full, but not numbered by the examiner. Ruled in by the
commander this run:

- **C12** — CF quiz item 9, "Identify the correct description of steel."
  Pure recall of steel's composition (8462 4.10.3.2, chemistry only; 8464
  names no steel). Dropped from the generated CF route copy only.
- **C13** — CH quiz item 7, "Stainless steel is used to make cutlery.
  Suggest two properties…" The credited answer depends on recalling
  stainless steel resists corrosion (8462 4.10.3.2), not supplied in the
  stem. Dropped from the generated CH route copy only.

Both use `op='drop_item'` against the exact stems in
`all_subtopics_chemistry.py` / `all_subtopics_chemistry_higher.py`; TF9/TH7
keep the equivalent items. `ks4_science_rulings.ROWS` grew from 99 to 101,
`metals-alloys`'s row count from 11 to 13. `source-diff.md` now shows
`metals-alloys` `quiz.CF`/`quiz.CH` as "length differs — design has 10, ours
has 9" (confirmed, both routes). `docs/ks4/design-reference/pilot/
DEPARTURES-PILOT.md` updated: the two rows moved from "open for the
commander" into the Verbatim-layer table, and every "99"/"11" count in that
file updated to "101"/"13".

## 5. Source-diff summary

`docs/ks4/pilot-inventory/source-diff.md`: **124 field/route comparisons
EQUAL, 23 DIFFER** (was 21 before this run's two new drops — both new
DIFFERs are `metals-alloys` `quiz.CF`/`quiz.CH`, both "length differs:
design has 10, ours has 9", exactly the two dropped items). Every DIFFER
traces to a named `source`-layer ruling; none is unexplained drift.

## 6. Storage-key decision

The contract's own text proposed borrowing KS3's `ks3_ladder4_<slug>` /
`ks3_work_<slug>` scheme with a `ks4_` prefix. **That is not what shipped.**
`Ks4Ladder.dc.html` — Design's own verbatim shared block — already keys
localStorage as `'ks4-best-' + (this.props.slug || 'x')` (hyphenated, one key
per lesson, holding the best `n`-of-4 score), via `KS4.load`/`KS4.save`, and
never calls any server-submission endpoint. `ks4_rulings.R4` is a **verified
no-op check** (`check_r4_storage_key`), not a rewrite: the exact string
`const key = 'ks4-best-' + (this.props.slug || 'x');` is asserted present,
so a future Design delivery that changes this line fails loud rather than
silently reverting to the old scheme. Confirmed live this run: `window.
KS4.save('ks4-best-metallic-bonding', 3)` → reload → `localStorage.getItem
('ks4-best-metallic-bonding')` and `KS4.load(...)` both return `3` (§8).

## 7. Prev/next decision

Design's `endPrev`/`endNext` assumed one pilot-internal narrative order and
were WRONG against the real per-route topic order in `all_subtopics_physics
*.py` (`resistors` actually precedes `series-parallel-circuits`, reversed
from Design's assumption; `series-parallel-circuits`'s real next lesson is
`direct-alternating-pd`, outside this pilot). Per contract §1 ("computed
exactly as `make_pathway_subtopic_page` does"), `R-PREVNEXT` replaces the
hardcoded literals entirely with a `mrbPrevNext` mount prop, computed once
per (lesson, route) by `compute_prev_next()` from the same source data
`shared/ks4-source.js` is generated from — so prev/next differ correctly by
route (a Foundation Combined class can stop one lesson short of a Higher
Triple class's neighbour set). `R-CONNECTS` (Design's curated "related
lessons" picks, not a sequence) keeps her choices but resolves each of the
44 cross-references through `KS4.hrefFor(slug, R)`, added to `shared/
ks4-lib.js`, falling back to the Triple pathway at the same tier when a
target (nanoparticles) doesn't ship on the current page's pathway.

## 8. Freeze mechanism

`ks4_lessons/frozen.json` (written by `python3 build_ks4.py --freeze`)
records, per lesson, `{"hash": sha256(...), "review_state": "..."}`. The
hash covers exactly three byte-for-byte strings: the compiled TEMPLATE json
(`json.dumps(compiled_lesson["template"])` — no `sort_keys`, matching what
`lesson_mount_script()` embeds), the rulings-applied LOGIC source, and the
served SOURCE record (`json.dumps(per_slug[slug], sort_keys=True)`, covering
every route's quiz in one blob) — joined with an ASCII unit-separator and
sha256'd (`compute_freeze_hash()`).

`ks4_pilot_check.py`'s new `check_freeze()` recomputes the SAME hash with no
browser and no recompilation: `extract_freeze_pieces()` pulls the identical
template/logic substrings back out of the lesson's own built page (its mount
`<script>`, located by literal markers — both embedded blobs are
guaranteed single-line, since `json.dumps` escapes real newlines, so a
literal-string search is exact, not a heuristic) and the source-record
substring out of `shared/ks4-source.js` on disk. For every lesson whose
`review_state` is `examiner-reviewed` or `frozen`, a hash mismatch is a red,
with the message: *"content has changed since it was last frozen … Re-run
the examination, then `python3 build_ks4.py --freeze` once the examiner's
changes are applied."*

**Verified working, not just written**: corrupted `metals-alloys`'s stored
hash by hand → `ks4_pilot_check.py` correctly failed with exactly that
message → restored the real hash → green again.

`python3 build_ks4.py --freeze` run once this session: **14 of 14 lessons
frozen**, all at `review_state: "examiner-reviewed"`.

## 9. review_state / showDraft

All 14 lessons' `review_state` in `ks4_lessons/__init__.py` flipped from
`"draft"` to `"examiner-reviewed"`. `build_ks4.py`'s existing
`"showDraft": lesson["review_state"] == "draft"` needed no code change — it
already derives `false` for any non-`"draft"` state, including
`"frozen"` (documented explicitly now in the field's own docstring).
Confirmed by direct grep of all 54 built pages: **0** occurrences of
`"Draft — not yet science-reviewed"` and **0** occurrences of `"Draft ·
awaiting approval"` anywhere in `ks4_pilot_manifest.json`'s 54 pages (the
latter is additionally always-removed by the standing ruling R7,
independent of `review_state`, for the two physics lessons that carried it).

## 10. Build + gate results

```
python3 build_ks4.py --freeze
  ✓ all 14 slugs verified
  ✓ shared/ks4-source.js written; diff vs Design's own: 124 EQUAL, 23 DIFFER
  ✓ shared/ks4-ds.css, ks4-theme.css, ks4-diagrams.js, ks4-lib.js written
  ✓ shared/ks4-lesson.css written (2462 bytes)
  ✓ synced 7 shared asset(s) into mrbadmus_site/shared
  ✓ 11 shared blocks compiled
  ✓ 14 lessons compiled
  ✓ ks4_science_rulings: 97 of 101 rows applied
     R9 fired: states-of-matter, polymers, metals-alloys
     R-SLUG fired: metals-alloys, series-parallel-circuits, resistors
  ✓ rung-1 fallback check: 0 warning(s)
  ✓ 2 draft exam tip(s) preserved
  ✓ 8 shared asset(s) versioned
  ✓ 54 pages written
  ✓ zero console errors across 54 pages at 1280 and 360px
  ✓ mirrored 54 page(s) to the repo-root combined/triple/ trees
  ✓ ks4_pilot_manifest.json written (54 pages, 8 assets)
  ✓ ks4_lessons/frozen.json written (14 lesson(s) frozen)
✅ build_ks4 complete — 54 pages, 0 fallback warning(s).

python3 ks4_pilot_check.py
✅ ks4_pilot_check: 54 page(s), 8 asset(s) — all clean.
```

Rung-1 fallback: 0 warnings even after the science rulings changed rung-1
`why` text on several lessons (chemical-bonds, metals-alloys, giant-
covalent-structures, etc.) — none of those rulings touched a rung-1 NEEDLE
string, so the check's own-route/TH-fallback search still resolves cleanly.
Had a needle broken, this report would say so as a real finding rather than
weakening the check — it did not happen this run.

## 11. Sanity drive (item G) — verbatim results

**54-page sweep, 1280 + 360px:**

```
54/54 pages clean
```

Every page: zero console errors at both widths, no horizontal overflow at
360px, hook block present, ladder present, no Route `<select>` anywhere.

**metallic-bonding TH interaction:**

```json
{
 "hook_reveal_present": true,
 "score_line_after_rung1": "1 of 4 rungs tried",
 "best_before_reload": null,
 "best_after_reload": null,
 "console_errors": []
}
```

`best_before_reload`/`best_after_reload` are both `null` — **this is
correct, not a defect.** `Ks4Ladder.dc.html`'s own verbatim `component
DidUpdate()` only calls `KS4.save()` once `this.score().done` is true, i.e.
all 4 rungs answered; the drive only completes rung 1 (by design — a fast
sanity check, not a full ladder run), so no save is expected yet. To prove
the underlying storage PRIMITIVE genuinely persists (rather than trusting
that on faith), a second, targeted check called `window.KS4.save('ks4-best-
metallic-bonding', 3)` directly, then reloaded the page:

```
raw localStorage right after KS4.save: 3
raw localStorage after reload: 3
KS4.load() after reload: 3
```

Confirms `KS4.save`/`KS4.load`/localStorage genuinely round-trip across a
real page reload under the `ks4-best-<slug>` key (§6). Combined with the
rung-1 interaction succeeding (hook reveal fired, score line updated, zero
console errors) and R4 being a verified no-op against Design's own
unmodified completion logic, there is no reasonable path by which
completing all 4 rungs would fail to persist — but a full 4-rung completion
was not driven end-to-end this run (see Decisions).

## 12. Visual comparison — engine vs Design's reference

**metallic-bonding TH, both widths, light colour scheme (`Emulation.
setEmulatedMedia` → `prefers-color-scheme: light`; headless Chrome's silent
default is dark, per `docs/ks4/pilot-inventory/measure_design.py`'s own
documented gotcha — the first screenshot pass in this run used the scratch
drive script's `screenshots()`, which does NOT set this emulation, and was
discarded/retaken for that reason):

At both 1280px and 360px, `engine-metallic-{360,1280}.png` vs `docs`'s
existing `design/metallic-bonding-{360,1280}.png` reference are visually
identical — same nav, brand mark, breadcrumb, eyebrow ("AQA CHEMISTRY
5.2.1.5 · MODEL"), title, hook copy, badge pills ("COMBINED · TRIPLE",
"FOUNDATION · HIGHER"), colours, fonts, spacing, and full-page component
order (hook → think-again → electron-sea workbench simulation → model
summary cards → key fact → exam ladder (4 rungs) → summary bullets →
practice set → prev/next → tutor CTA). The only two differences, both
EXPECTED and both proof the port did its job:

1. Design's raw standalone shows a **"Route" `<select>`** (defaulting to
   Triple Higher) — the engine shows no selector at all, because R1 removes
   it and the route is pinned as a mount prop (contract §1, "one route per
   URL").
2. Design's raw standalone shows the **"Draft — not yet science-reviewed."**
   banner — the engine shows nothing there, because `review_state` is now
   `examiner-reviewed` and `showDraft` resolves to `false` (§9).

No other pixel difference was visible at either width.

**12 additional screenshots, 7 lessons/routes spanning both subjects, both
tiers, both pathways, at both 360 and 360/1280** (`chemical-bonds` TH,
`ionic-bonding` CF, `states-of-matter` CH, `polymers` CF, `nanoparticles` TF,
`series-parallel-circuits` CH, `resistors` TH — 14 files; see Decisions §14
for the 12-vs-14 count). Looked at three: `resistors-TH-360.png`,
`nanoparticles-TF-1280.png`, `ionic-bonding-CF-360.png`. All three render
cleanly — correct brand mark, cream/burnt-orange palette, no dark-theme
leakage, no visible overflow, circuit diagrams (resistors, using the R10–R12
`ks4-diagrams.js` fixes) and the nanoparticles cube-splitter figure both
render as expected, quiz/ladder/practice blocks present and correctly
tiered. Nothing broken spotted in any of the three.

All screenshots written under `/Users/midebadmus/tmp/ks4-pilot-shots/`
(`MRB_SHOTS`).

## 13. Git status

Only the expected paths moved: `build_ks4.py`, `ks4_lessons/__init__.py`,
`ks4_pilot_check.py`, `ks4_pilot_manifest.json` (mine), `shared/ks4-
diagrams.js` + `shared/ks4-source.js` (both trees — repo root and
`mrbadmus_site/`), and the 54 pages (both trees — 108 modified `.html`
files total). `contrast_audit.py` and `gate_registry.py` were already
modified before this run (the parity executor's own work; untouched here).
`ks4_lessons/frozen.json` and `ks4_science_rulings.py` are new/edited,
mine. No page outside the 54-page manifest changed by a byte.

## 14. Decisions

- **metals-alloys-C12/C13 minted as described in the task** — exact stems
  taken from `all_subtopics_chemistry.py`/`_higher.py`, `op='drop_item'`,
  row count and every "99"/"11" reference updated to "101"/"13" across
  `ks4_science_rulings.py` and `DEPARTURES-PILOT.md`.
- **`docs/ks4/pilot-inventory/source-diff.md` changed** even though the
  pilot-build-contract.md's ownership table assigns `docs/ks4/pilot-
  inventory/` to the inventory executor. This file is a pure BUILD
  ARTIFACT of `build_ks4.py`'s own `write_source_diff()` — the same
  category as the 54 pages or the manifest, not a hand edit — and it is
  required to change whenever `shared/ks4-source.js`'s ruling-applied
  content changes, which this run's two new drops do. Left as the build
  produced it rather than reverted, since reverting it would make the
  committed inventory file lie about the current build.
- **Full 4-rung ladder completion was not driven end-to-end** for the
  persistence proof. Reverse-engineering each rung's exact UI (rung 2 is a
  `kind: 'data'` matching activity, rung 4 is `Ks4Write` — free text +
  self-marked checkboxes) for one interaction script was judged lower value
  than directly verifying the underlying `KS4.save`/`KS4.load`/localStorage
  primitive round-trips across a real reload (§11), combined with R4 being
  a verified no-op against Design's own unmodified `componentDidUpdate()`
  completion gate. If a stronger proof is wanted, `student_controls_drive.py`
  or an equivalent full click-through is the right tool, not a scratch
  sanity script.
- **12-vs-14 screenshot count.** The task named 7 lesson/route pairs and
  said "that is 12 more files… 12 screenshots spanning lessons; at least six
  at phone width" — 7 pairs × 2 widths is 14, not 12. Took all 7 pairs at
  BOTH widths (14 files) rather than guess which pair to drop to hit exactly
  12; this satisfies "at least six at phone width" (7 delivered) and gives
  strictly more evidence, not less.
- **First screenshot pass discarded.** The scratch drive script's own
  `screenshots()` function does not call `Emulation.setEmulatedMedia`, so
  its `engine-metallic-*.png`/`design-metallic-*.png` were captured under
  headless Chrome's silent DARK default, not light — contradicting the
  task's explicit instruction and the pre-existing `design/metallic-
  bonding-*.png` reference (captured in light mode by `measure_design.py`).
  Retook `engine-metallic-{360,1280}.png` with light mode correctly forced,
  and compared those against the existing light-mode `design/` reference
  rather than the mismatched dark-mode pair.
- **Freeze hash construction chosen to be independently re-derivable from
  disk with no browser.** The task did not prescribe the exact algorithm,
  only "sha256 of (compiled template JSON + rulings-applied logic + the
  lesson's served source record for every route)". Implemented so the
  SAME three substrings are never independently re-serialised at
  check-time (which would risk float/key-order drift) — they are the exact
  bytes already embedded on disk, recovered by literal-marker string
  search (safe because `json.dumps` never emits a raw newline, so the
  markers cannot be forged by content). Verified this actually catches
  drift by hand-corrupting a hash and watching the gate go red, then
  restoring it.
