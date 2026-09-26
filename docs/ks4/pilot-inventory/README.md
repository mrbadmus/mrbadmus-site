# KS4 pilot inventory — what the port is proven against

Measured 25–26 Sep 2026. **This is a specification, not a build.** Nothing
under `ks4_lessons/`, `build_ks4.py` or `shared/ks4-*` is written from this
folder — those belong to the engine executor
(`pilot-build-contract.md` §2). This folder is the exhaustive, component-by-
component reading of all 14 approved pages that the port (and
`ks4_parity.py`, once it exists) is checked against, following the same
pattern `docs/ks3/b1-inventory/` set for KS3's B1.

## Source of truth

`docs/ks4/design-reference/pilot/KS4 Lessons/Pilot - Bonding and
Electricity/*.dc.html` — Design's delivery, committed unmodified (md5s in
`docs/ks4/design-reference/pilot/MD5SUMS`). Every measurement in these files
was taken from those 14 pages, in a real headless-Chrome browser, driven by
`measure_design.py` in this folder.

## How to reproduce

```bash
cd /Users/midebadmus/Documents/GitHub/mrbadmus-worktrees/ks4-pilot
python3 docs/ks4/pilot-inventory/measure_design.py
```

This serves the delivery over a local HTTP server (Design's pages load
React/Babel from unpkg at runtime, so Chrome needs network), drives all 14
lessons through `ks3_browser.py` (the repo's CDP harness — its own docstring
calls itself `cdp.py`; imported everywhere in this repo as
`import ks3_browser as cdp`), and:

- writes `docs/ks4/pilot-inventory/reference.json` (the machine-readable
  baseline `ks4_parity.py` should compare the port against — see §"reference.json
  schema" below)
- writes screenshots (Triple Higher, light mode, 1280 and 360) to
  `$MRB_SHOTS/design/<slug>-{1280,360}.png` — **not into the repo tree**,
  per the brief's "screenshots outside the repo" rule
  (`MRB_SHOTS=/Users/midebadmus/tmp/ks4-pilot-shots` for this run)
- kills its own `http.server` and Chrome processes on exit (normal or
  interrupted), by the PIDs it printed as it started them

The whole run takes roughly 5–6 minutes for all 14 lessons on this machine.
`MRB_SMOKE=<n>` limits the run to the first `n` lessons, for a fast
smoke-test of the script itself.

The 14 per-lesson `.md` files and `payload-map.md` in this folder were then
generated from `reference.json` plus hand-curated per-lesson metadata (family,
flagship description, the relevant lines of `NOTES-KS4-pilot.md` §7/§8/§9)
by a throwaway script that was **not** committed (it lived in this session's
scratch directory and is not needed again — `reference.json` and the .md
files it produced are the durable artefacts). If `reference.json` is
regenerated with a materially different shape, the 14 lesson files and
`payload-map.md` should be regenerated from it by hand or by a fresh
equivalent script — they are a rendering of `reference.json`, not an
independent source.

## Method notes that matter for reading the numbers

1. **⚠️ Headless Chrome's own default `prefers-color-scheme` is DARK, not
   light or "no preference".** Verified directly: on a completely fresh page
   with no `Emulation.setEmulatedMedia` call at all,
   `matchMedia('(prefers-color-scheme: dark)').matches` is `true` and `.rd`'s
   background is `rgb(22, 18, 14)` (the dark ground token), not the cream
   `#FBF3E6`. Every "light mode" measurement in `reference.json` (the default
   route's width sweep, the styles pass, screenshots, interactions, keyboard)
   explicitly forces `prefers-color-scheme: light` before measuring — nothing
   was measured under Chrome's silent default. This is exactly the kind of
   thing that silently inverts a light/dark finding if missed; it is
   `set_media()`'s own docstring in `measure_design.py`, not just noted here.
2. **The top progress bar is NOT width-driven.** `Ks4Chrome.dc.html`'s
   `state.scrolled` (set by a `window.scrollY > 140` scroll listener) gates
   the top bar's visibility, and the side rail is separately CSS-hidden below
   1340px. So **at the top of a narrow page (scrollY 0), neither rail
   renders** — confirmed on all 14 lessons. `reference.json` records both
   `rail` (at scrollY 0) and `rail_after_scroll` (after `scrollTo(0,300)`,
   only captured for widths < 1340) at every width.
3. **The Question bank paginates behind its own `.ks3-reveal-btn` ("Show N
   more"), starting at 4 of however many exist.** That class name collides
   with `#s-sort`'s "Show what settles each one" button, which sits earlier
   in the DOM and is `disabled` until the sort is complete. A naive
   `document.querySelector('.ks3-reveal-btn')` finds the SORT's button first
   and looks exhausted after zero clicks — this is exactly what this script's
   first draft did, undercounting every chemistry lesson's bank at a flat 4
   regardless of its real size. Fixed by scoping every click to the bank's
   own root, found via its "Practice set" eyebrow text. The corrected counts
   are in `payload-map.md` §4 and each lesson's §2.
4. **`Ks4Choice`'s reveal panel carries no distinguishing class** — only the
   shared `[data-arrive]` wrapper attribute (used for the arrival animation).
   KS3's inventory pattern of selecting `.ks3-reveal` does not port; this
   script selects `[data-arrive]` instead, and also captures a before/after
   textContent diff on the enclosing section as a fallback for anything that
   doesn't use that wrapper.
5. **Reduced motion was proven directly, not asserted.** `[data-arrive]` is
   also the mechanism `@media (prefers-reduced-motion: reduce) { [data-arrive]
   { animation: none !important; } }` targets (`Ks4Choice.dc.html`). Every
   lesson's hook is committed twice — once under normal motion, once under
   forced `prefers-reduced-motion: reduce` — and the computed
   `animation-name` is read both times. All 14 lessons: `ks4-arrive` under
   normal motion, `none` under reduced motion → swaps instantly, proven, not
   assumed. This is the one universal animated instrument every lesson
   shares; the lesson-specific instruments (electron-sea drift, the heating
   curve, the alloy mixer's push) were **not** individually proven this way —
   see the Limitations section below.
6. **All measurements use `Emulation.setDeviceMetricsOverride`, never a
   shrunk container** — the same rule KS3's inventory established, inherited
   via `ks3_browser.py`'s `set_viewport()`.

## What was NOT measured to full B1 depth, and why

`docs/ks3/b1-inventory`'s six lesson files run 700–850 lines each, written by
hand against one lesson at a time over a full session per lesson. Doing that
for 14 KS4 lessons in one run — at the same prose depth, state-by-state,
citing exact pixel geometry for every one of 60+ tokens per lesson — was not
achievable inside this run's budget without materially degrading either
accuracy (hand-transcribing numbers from a live browser without automation)
or coverage (fewer than 14 lessons measured). The choice made: **automate the
measurement so every one of the 14 lessons gets the same real-browser pass**
(sections, route matrix, rail, ladder, question bank, key note, computed
styles light/dark, interactions with real captured verdict text, reduced-
motion proof, keyboard audit, screenshots), write the full machine-readable
result to `reference.json`, and render each lesson's `.md` file from that —
rather than writing exhaustive hand prose for a handful of lessons and
leaving the rest unmeasured. `reference.json` is the deep artefact;
`ks4_parity.py` should read it directly rather than trying to re-derive
numbers from the `.md` prose. Recorded as a Decision in the executor's final
report, not hidden here.

## Known measurement limitations

- **The Write rung's min-words unlock is not reliably measured.** By the time
  the script reaches it, ladder rung 1 is already answered+disabled from an
  earlier step, so the generic click target (`#s-ladder button`, first
  enabled match) can land on rung 2 or 3's own controls instead of rung 4's
  *Check my answer*. Every lesson's `ladder_write_ticks_present` is `false`
  in `reference.json` — this is **not** evidence that the unlock is broken,
  it is evidence the click landed on the wrong control. A real test of this
  needs a selector scoped to the rung whose `id` matches `r4`, not a bare
  `#s-ladder button`.
- **`flagship_new_text` is empty on all 14 lessons.** The before/after
  textContent diff this script uses for the hook and misconception blocks
  assumes new content is *appended* as prose. The flagship instruments more
  often change existing DOM (attribute/class swaps, a chamber redrawing,
  chips reordering) rather than appending a new paragraph, so the diff finds
  nothing even where real state changed. `flagship_option_clicked: true`
  confirms the click landed; the screenshots are the fallback evidence for
  what actually changed on screen.
- **Dark-mode computed styles cover only the fixed, always-present component
  set** (h1, eyebrow, commit prompt, resting option, misconception panel,
  key-fact card, badge pill, ladder rung header, check button, key-note
  card, end prev/next). State-dependent nodes (the reveal panel, a chosen
  option) were captured in light mode only, inside the interactions pass,
  which runs after the dedicated dark-mode pass has already reset back to
  light.
- **Per-instrument reduced-motion proof is universal, not per-instrument.**
  Only the shared `[data-arrive]` hook mechanism was driven twice (normal
  vs reduced motion) and its computed `animation-name` compared. NOTES §2's
  broader claim ("all animation reads `prefers-reduced-motion` once on mount
  and swaps to the end state") was not individually verified for the
  electron-sea workbench, the heating-curve simulation, the alloy mixer, or
  any other lesson-specific animated instrument. The 1280/360 TH-light
  screenshots exist for a manual spot-check; no automated per-instrument
  assertion was scripted.
- **Other-route passes (CF/CH/TF) are 1280-only**, per the brief's own
  design (deep sweep on the default route, lighter pass on the other three)
  — narrow-width route-specific overflow was not separately checked.

## `reference.json` schema

Top level:

```
{
  "measured": "2026-09-25",
  "method": "...",
  "widths": [1280, 1340, 820, 390, 360],
  "routes": ["Triple Higher", "Combined Foundation", "Combined Higher", "Triple Foundation"],
  "default_route": "Triple Higher",
  "lessons": { "<site-slug>": { ... } }
}
```

Per lesson (`lessons.<slug>`):

| Key | Shape | Notes |
|---|---|---|
| `file` | string | the `.dc.html` filename in the pilot delivery folder |
| `routes.<route>.widths.<width>` | object | see below — measured for ALL 5 widths on the default route (`Triple Higher`), and for **1280 only** on the other 3 routes |
| `console_errors_default_route` | string[] | `[Console]`/`[exception]`/`[Log]` entries, favicon 404s filtered, accumulated across the default route's 5-width sweep |
| `styles_light` / `styles_dark` | object keyed by component name (`h1`, `eyebrow`, `commit`, `option_resting`, `misconception_panel`, `key_fact_card`, `badge_pill`, `ladder_rung_header`, `check_button`, `key_note_card`, `end_prev_next`) | each value: `font-family, font-size, font-weight, color, background-color, border, border-radius, padding, box-shadow, __box{x,y,w,h}` — light explicitly forces `prefers-color-scheme: light`, dark forces `dark` |
| `reduced_motion` | object | `hook_reveal_animation_name_normal_motion`, `hook_reveal_animation_name_reduced_motion`, `swaps_instantly` (bool) |
| `interactions` | object | see the 20 keys in any lesson's §5 table — hook/misconception/flagship/sort/ladder/write/keynote, each with a `_clicked` bool and, where captured, the real text observed |
| `keyboard_1280` | `{count, negativeTabindex}` | focusable-control audit at 1280, fresh navigation |
| `key_note` | `{lineCount, lines[]}` | `#s-keynote`'s `<ol><li>` count and text |
| `question_bank` | `{itemCount, verdictWords[], loadMoreClicks}` | Triple Higher only, fully expanded — see method note 3 above |

Per width (`routes.<route>.widths.<width>`):

| Key | Shape | Notes |
|---|---|---|
| `sections` | array | every direct child of `.ks3-lesson`: `index, tag, id, class, eyebrow, text (first 4000 chars), words, box{x,y,w,h}, dcImports[], badgeLike` |
| `overflow` | `{scrollWidth, innerWidth, overflow, offender}` | `offender` is a CSS-selector-ish string for the worst-overflowing element, or `null` |
| `rail` | `{sideVisible, topVisible, sideNodeCount, sideNodes[], sideBox, topText}` | measured at scrollY 0 |
| `rail_after_scroll` | same shape, or `null` | only measured for `width < 1340`; measured after `scrollTo(0,300)`, then scrolled back to 0 |
| `ladder` | `{words, scoreLine, scoreNote, rungCount, hasCommandWords}` | `null` if `#s-ladder` is absent (never happens in this pilot) |
| `focusables` | `{count, negativeTabindex}` or `null` | only measured at the "deep" width, 1280 |

## Files in this folder

| File | What |
|---|---|
| `README.md` | this file |
| `measure_design.py` | the re-runnable measuring script |
| `reference.json` | the machine-readable baseline — 14 lessons × 4 routes × 5 (or 1) widths |
| `payload-map.md` | whole-pilot block vocabulary, component prop shapes, family table, route-tag inventory, shared assets, state spaces |
| `chemical-bonds.md` … `resistors.md` (14 files) | one per lesson — blocks in order, route matrix, rail/overflow per width, computed styles light/dark, interactions with observed text, findings |
| `source-diff.md`, `draft-exam-tips.md`, `engine-report.md` | **owned by a different executor** — not written or read by this pass beyond confirming they exist; do not attribute their content to this README |

## Site slugs, for cross-reference

Per `pilot-build-contract.md` §0 (verify against `all_subtopics_*.py` before
relying on it for the actual build — that table itself says it was read from
the data by a scout, not proven):

| Site slug | Lesson | Routes |
|---|---|---|
| `chemical-bonds` | L1 Chemical bonds | CF CH TF TH |
| `ionic-bonding` | L2 Ionic bonding | CF CH TF TH |
| `ionic-compounds` | L3 Ionic compounds | CF CH TF TH |
| `covalent-bonding` | L4 Covalent bonding | CF CH TF TH |
| `metallic-bonding` | L5 Metallic bonding | CF CH TF TH |
| `states-of-matter` | L6 States of matter | CF CH TF TH |
| `properties-ionic-compounds` | L7 Properties of ionic compounds | CF CH TF TH |
| `properties-small-molecules` | L8 Properties of small molecules | CF CH TF TH |
| `polymers` | L9 Polymers | CF CH TF TH |
| `giant-covalent-structures` | L10 Giant covalent structures | CF CH TF TH |
| `metals-alloys` | L11 Metals and alloys | CF CH TF TH |
| `nanoparticles` | L12 Nanoparticles | **TF TH only** |
| `series-parallel-circuits` | L13 Series and parallel circuits | CF CH TF TH |
| `resistors` | L14 Resistors and I–V (required practical) | CF CH TF TH |

## Standing law these files are written under

Same as `docs/ks3/b1-inventory/README.md`'s, restated for KS4 per
`pilot-build-contract.md`'s own opening line: **where this inventory and
Design's page disagree on what a page looks like or does, the page wins**,
and the disagreement is a finding, not a thing to silently reconcile. This
inventory does not resolve any of the numbered flags in
`NOTES-KS4-pilot.md` §9 (science accuracy) — those are named per lesson,
verbatim, and left for the science examiners named in
`pilot-build-contract.md` §2.
