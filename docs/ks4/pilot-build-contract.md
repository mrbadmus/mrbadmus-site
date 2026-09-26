# KS4 pilot — build contract (25 Sep 2026)

Binding on every stream of the KS4 pilot port. Where this file and a stream's
own judgement disagree, this file wins; where this file and Design's page
disagree on what a page LOOKS like or DOES, **the page wins** and the
disagreement is noted in the inventory.

## 0. What is being built

Fourteen KS4 lessons authored by Design (`docs/ks4/design-reference/pilot/`,
committed unmodified, md5s in `MD5SUMS`) are ported to the site's own
generator and put live on their existing URLs, in all four routes. These 14
set the standard the other 250 KS4 lessons are built from.

| # | Design file (`KS4 Lessons/Pilot - Bonding and Electricity/`) | site slug | subject/topic | routes |
|---|---|---|---|---|
| L1 | `ks4-chemistry-5.2.1.1-chemical-bonds.dc.html` | `chemical-bonds` | chemistry/bonding | CF CH TF TH |
| L2 | `ks4-chemistry-5.2.1.2-ionic-bonding.dc.html` | `ionic-bonding` | chemistry/bonding | CF CH TF TH |
| L3 | `ks4-chemistry-5.2.1.3-ionic-compounds.dc.html` | `ionic-compounds` | chemistry/bonding | CF CH TF TH |
| L4 | `ks4-chemistry-5.2.1.4-covalent-bonding.dc.html` | `covalent-bonding` | chemistry/bonding | CF CH TF TH |
| L5 | `ks4-chemistry-5.2.1.5-metallic-bonding.dc.html` | `metallic-bonding` | chemistry/bonding | CF CH TF TH |
| L6 | `ks4-chemistry-5.2.2.1-states-of-matter.dc.html` | `states-of-matter` | chemistry/bonding | CF CH TF TH |
| L7 | `ks4-chemistry-5.2.2.3-properties-ionic-compounds.dc.html` | `properties-ionic-compounds` | chemistry/bonding | CF CH TF TH |
| L8 | `ks4-chemistry-5.2.2.4-properties-small-molecules.dc.html` | `properties-small-molecules` | chemistry/bonding | CF CH TF TH |
| L9 | `ks4-chemistry-5.2.2.5-polymers.dc.html` | `polymers` | chemistry/bonding | CF CH TF TH |
| L10 | `ks4-chemistry-5.2.2.6-giant-covalent-structures.dc.html` | `giant-covalent-structures` | chemistry/bonding | CF CH TF TH |
| L11 | `ks4-chemistry-5.2.2.7-metals-alloys.dc.html` | `metals-alloys` | chemistry/bonding | CF CH TF TH |
| L12 | `ks4-chemistry-5.2.3.3-nanoparticles.dc.html` | `nanoparticles` | chemistry/bonding | **TF TH only** (whole lesson is 8462 4.2.4, chemistry only) |
| L13 | `ks4-physics-6.2.2-series-parallel-circuits.dc.html` | `series-parallel-circuits` | physics/electricity | CF CH TF TH |
| L14 | `ks4-physics-6.2.1.4-resistors-iv-required-practical.dc.html` | `resistors` | physics/electricity | CF CH TF TH |

Route → URL: `/{combined|triple}/{foundation|higher}/{subject}/{topic}/{slug}.html`
(e.g. `combined/foundation/chemistry/bonding/metallic-bonding.html`). 54 pages
in total (13 × 4 + 2). Verify every slug against `all_subtopics_*.py` before
relying on it — the table above was read from the data by a scout, not proven.

## 1. Engine shape — compile, do not re-author

Design's pages run on `support.js`, which loads React, ReactDOM and Babel
from unpkg at runtime. **None of that ships.** The port is a compile:

- `build_ks4.py` parses each lesson's `.dc.html` (template inside `<x-dc>`,
  logic in `<script type="text/x-dc" data-dc-script>`, Design's props
  defaults in `data-props`) and each of the 11 block `.dc.html` files
  (`Ks4Chrome`, `Ks4Choice`, `Ks4Sort`, `Ks4Chain`, `Ks4Write`, `Ks4Cfifa`,
  `Ks4Ladder`, `Ks4KeyNote`, `Ks4QuizBank`, `Ks4End`, `Ks4Video`).
- Template directives to support: `{{ path }}`, `<sc-if value>`, `<sc-for
  list as>`, `<dc-import name … props… on-x="{{ handler }}">`, `onClick`,
  `onChange`, `onInput`, `style-hover`. Editor hints (`hint-size`,
  `hint-placeholder-*`, `$preview`) are stripped. Reuse the browser-side
  template walker in `student_template.py` (it uses Chrome's own parser, which
  matters for `<sc-for>` inside tables) — extend it for `dc-import`.
- `shared/ks4-runtime.js`: a vanilla runtime derived from
  `shared/student-runtime.js` (`MrbLogic` = `DCLogic`: `state`, `setState`,
  `renderVals`, `componentDidMount/Update/WillUnmount`), extended with
  **child components**: each `dc-import` node mounts a block instance keyed by
  (template node index, for-loop path), receives props from the parent's
  render scope with kebab→camel names (`right-word` → `rightWord`, `on-commit`
  → `onCommit`), keeps its own state across parent re-renders, and re-renders
  when its props change. Rendering must **patch the DOM in place** (tag/attr/
  text reconciliation by position), not empty the host: lessons run 90 ms
  animation ticks and inner scrollers, and a full rebuild per tick is the
  scroll-jump defect CLAUDE.md records for `set-work.js`. Focus, form values
  and `scrollTop` survive a render.
- React is used in exactly four places (`KS4.fig`, `Ks4Choice`/`Ks4Write`
  `figure`, `Ks4Ladder.svg`) — all `createElement('div', {role:'img',
  'aria-label', style:{maxWidth}, dangerouslySetInnerHTML})`. The runtime
  provides one primitive for that (an `{__html, alt, max}` marker mounted as
  that div) and the ported `shared/ks4-lib.js` uses it. Everything else in
  `ks4-lib.js`, `ks4-diagrams.js` (pure SVG-string functions) ships as-is
  under `shared/`, with `KS4.ready()`'s polling replaced by synchronous load
  order.
- Design's per-lesson `Component` class ships **verbatim** as that page's
  script (the port is of her state machine, not a re-reading of her HTML).
  Any change to her constants or template goes through `ks4_rulings.py`
  (the `student_rulings.py` pattern: exact-match substitutions, each carrying
  a DEPARTURES id, and the build fails if a ruling no longer matches).
- **One route per URL.** The route is pinned as a prop at mount; the Route
  `<select>` and its label are removed at compile time (a ruling, not a hand
  edit). The theme prop stays `auto` (OS dark mode); the `showDraft` prop is
  set per lesson from the lesson record (`review_state`).
- **Static first.** After compiling, `build_ks4.py` prerenders each page's
  mounted DOM in headless Chrome (`cdp.py`) and bakes it into the HTML host, so
  the page carries its text without JS; the runtime then mounts over it.
- **Verbatim text comes from the repo.** `shared/ks4-source.js` is
  GENERATED from `all_subtopics_chemistry*.py` / `all_subtopics_physics*.py`
  (quiz per route CF/CH/TF/TH, `examiner_tip`, `key_note`, `common_mistake`,
  `fifas`, `equations`, `rp`), never from Design's `ks4-source.js`. A build
  check compares the two field by field and prints every difference; the
  expected result is byte equality except where a ruling says otherwise.
- **Registry.** A closed vocabulary: the 14 KS3 block types (`hook`,
  `explainer`, `figure`, `worked-example`, `check`, `keyword`, `practical`,
  `misconception`, `summary`, `quiz`, `key-fact`, `rule`, `formula`,
  `comparison`) + the four KS4 types (`required-practical`, `equation`,
  `extended-response`, `exam-tip`) + the 11 components. Every `<section>` in
  a lesson template is classified to one type (by its id/class/eyebrow, from
  a per-lesson map in the lesson record if it cannot be inferred), and every
  `dc-import` must name a registered component. **Unregistered → the build
  raises.** The classification is written into the page as `data-block`.
- **Video.** `Ks4Video` keeps its empty state. `KS4.VIDEOS` is generated from
  `ks4_lessons/videos.py` keyed by site slug (empty today), so a future
  `lesson_videos` table feeds it with no page change.
- **Scores.** Best score and retry-my-misses use KS3's scheme
  (`shared/ks3.js`: `ks3_ladder4_<slug>` / `ks3_work_<slug>`) with a `ks4_`
  prefix — `ks4_ladder4_<slug>`, `ks4_work_<slug>` — and the same
  server submission only if `API-CONTRACT.md` already lets the endpoint
  distinguish key stages (eight slugs are identical across KS3 and KS4; a
  submission that cannot say which key stage it is must NOT be sent).
- **Chat.** "Ask Mr Badmus AI" opens the site tutor via `MrBadmus.init`,
  the way `build_ks3.py`'s overlay does, with the route's tier and pathway.

## 2. Files and ownership

| path | owner |
|---|---|
| `build_ks4.py`, `shared/ks4-runtime.js`, `shared/ks4-lib.js`, `shared/ks4-diagrams.js`, `shared/ks4-theme.css`, `shared/ks4-lesson.css` (Design's per-page `<style>` blocks, de-duplicated), `shared/ks4-source.js` (generated), `ks4_lessons/`, `ks4_rulings.py`, `build_all.py` (one new step, 1b) | engine executor |
| `docs/ks4/pilot-inventory/` | inventory executor |
| `docs/ks4/examination/` | science examiners |
| `docs/ks4/design-reference/pilot/DEPARTURES-PILOT.md`, `docs/ks4/pilot-port-report.md` | commander |
| `ks4_parity.py`, `gate_registry.py` rows | parity executor (after engine + inventory) |

`ks4_data/` is the QUESTION-POOL package (`classify()`, `questions/`). It is
a hard line: **nothing under `ks4_data/` changes**. Lesson records live in the
new `ks4_lessons/` package.

Nobody commits except the commander. Executors leave their files in the
worktree `/Users/midebadmus/Documents/GitHub/mrbadmus-worktrees/ks4-pilot`.

## 3. Hard lines (from the run brief)

- No DDL on production, no `supabase db push`.
- Question banks, their frozen windows and `scheme_of_work` untouched.
  Lesson-page questions stay on lesson pages.
- The other 250 KS4 lesson pages do not change by a byte. That means: no
  edit to `shared/styles.css`, `shared/nav.css`, `shared/tokens.css`,
  `shared/mrbadmus.v2.js` or anything else the old pages load (their `?v=`
  stamps would move). New assets only.
- Never set `MRB_DRIVE_PASSWORD` or `MRB_TEST_STUDENT_PASSWORD`.
- Kill processes by captured PID. Clean up scratch output.

## 4. Measurement widths

1280, 1340 (side rail appears), 820, 390, 360 — always by CDP device-metrics
override (`cdp.py`), never a shrunk container.
