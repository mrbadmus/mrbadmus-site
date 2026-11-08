# Saved work coverage: does every lesson activity save and come back?

Mide's item 1 (25 Oct 2026): every activity a family child does on a lesson must save
to `child_answers` (question id, knowledge point, answer, right/wrong or marks, attempt,
measured time, when) and come back on any device, the way the core rungs already do.

This page is the measurement, before and after. It is produced by
`python3 tools/activity_save_coverage.py --md` over the BUILT pages (`ks3/**`,
`combined/**`, `triple/**`) and the capture code itself (`shared/mrbadmus.v2.js`).
Static: no browser, no account, no network.

## How it counts

- **KS3**: every `[data-activity]` block outside the ladder (the ladder's four rungs
  save and restore themselves through `shared/ks3.js`). An instrument kind counts as
  handled when the capture's tables name it (`KIND_A`, `KIND_B5C`, `<ks3-specs>`) or
  it is a "Your turn" calculation (`data-p<N>cfa`). Whether an unhandled kind is
  answerable at all comes from `tools/ks3_instrument_shapes.json`: each of the 172
  unhandled kinds was read in its `shared/ks3.js` wire function and its markup and
  given a shape — **G** commit-before-explore gate, **A/M** a choice judged (or
  shown) at once, **S** several placements committed together, **T** typed or
  selected inputs committed by a button, **X** exploration only (sliders, tabs,
  run buttons, toggles), **R** reading only (no controls), **D** drag/canvas.
- **KS4**: every ROOT option group on a rebuilt lesson — the lesson's own
  activity, outside the shared blocks (`Ks4Choice`, `Ks4Ladder`, …, which were
  already saved). Each group is classified by running the lesson's own code in a
  sandbox (`tools/activity_save_coverage.js`) and pressing every option against a
  COPY of its state: an option that writes one place in the state, a different value
  per option, into a slot that starts empty, is an answer; a verdict comes from the
  lesson's own flag (`bqOk`), from the words it draws ("Yes." for some options
  only), from a "N of M right" tally, or from an alert-styled verdict. Cards that
  only open, tabs that only record they were seen, and selectors that start on an
  option already chosen are explorations, not answers. The classifier is the same
  text the page runs (`<ks4-root-acts>` in `shared/mrbadmus.v2.js`).
- **KS4 level picks**: every `Ks4Write` marked by LEVELS (the child picks a level
  for their own writing) — standalone, a ladder's rung 4, or a practice write item.

## Before (origin/main c3a30aebd, 25 Oct 2026)

The "before" KS4 rows were classified with the same classifier, run from a file
(`--classifier`), because the page did not carry it yet.

### KS3 (185 lessons, 747 activity blocks outside the ladder)

| block class | answerable | saved + restored | blocks |
|---|---|---|---|
| keyed commit (Start here / keyed) | yes | yes | 187 |
| instrument shape R | no | no | 95 |
| instrument (adapter A / B5C) | yes | yes | 86 |
| instrument shape G | yes | no | 68 |
| reading (no controls) | no | no | 64 |
| instrument shape X | no | no | 63 |
| prediction (options + reveal) | yes | yes | 62 |
| worked example (reveal the next step) | no | no | 58 |
| "Your turn" calculation | yes | yes | 22 |
| instrument shape M | yes | no | 17 |
| instrument shape S | yes | no | 14 |
| instrument shape A | yes | no | 5 |
| instrument shape T | yes | no | 4 |
| commitment (options, nothing revealed) | yes | no | 2 |

KS3 answerable blocks: **467**, saved: **357**, not saved: **110**. Instrument blocks not handled (any shape): **266**.

### KS4 rebuilt lessons (148 lessons, 522 route pages)

| root option group | kind | verdict from | saved + restored | groups (all routes) |
|---|---|---|---|---|
| answer | pick | flag | no | 345 |
| answer | pick | words | no | 164 |
| answer | pick | style | no | 94 |
| answer | pick | prediction | no | 39 |
| answer | pick | key | no | 32 |
| answer | pick | tally | no | 20 |
| answer | gate | key | no | 12 |
| answer | pick | style | yes | 4 |
| answer | pick | words | yes | 4 |
| answer | multi | unjudged | no | 4 |
| answer | pick | unjudged | no | 4 |
| not an answer | explore | a selector: it starts on an option already chosen | no | 232 |
| not an answer | explore | a tab that records which ones were seen | no | 224 |
| not an answer | explore | opens a card or marks it seen | no | 212 |
| not an answer | explore | no single place the choice is kept | no | 109 |
| not an answer | explore | part of a form another button commits | no | 59 |
| not an answer | none | no option changes the lesson here | no | 32 |
| not an answer | explore | shows a result for any choice; nothing is judged | no | 28 |
| not an answer | none | no options | no | 13 |
| not an answer | explore | a list of picks (choose several) | no | 8 |

KS4 lessons with an answerable root activity: **87**; with one NOT saved: **86**.
Distinct root answer groups (per lesson, across routes): **213**, not saved: **211**.
KS4 level picks (Ks4Write marked by levels): **443** instances over all routes in **127** lessons; not saved: **443**.


### KS4: what the option-group classifier cannot see (before)

| class | outcome | lessons | controls (distinct, per lesson) |
|---|---|---|---|
| a list of picks (choose several) | NOT saved | 2 | 2 |
| a selector: it starts on an option already chosen | exploring (read, reason in the doc) | 46 | 59 |
| a tab that records which ones were seen | exploring (read, reason in the doc) | 42 | 63 |
| no option changes the lesson here | exploring (read, reason in the doc) | 1 | 1 |
| no options | exploring (read, reason in the doc) | 1 | 1 |
| no single place the choice is kept | NOT saved | 9 | 9 |
| no single place the choice is kept | exploring (read, reason in the doc) | 17 | 19 |
| opens a card or marks it seen | exploring (read, reason in the doc) | 46 | 56 |
| part of a form another button commits | NOT saved | 9 | 12 |
| part of a form another button commits | exploring (read, reason in the doc) | 1 | 1 |
| shows a result for any choice; nothing is judged | exploring (read, reason in the doc) | 4 | 4 |
| slider | exploring (a slider: nothing asks for a value) | 8 | 8 |
| typed or selected | NOT saved | 9 | 13 |

Lessons with a control here NOT saved: **25**.


### Against the numbers we were given

- **KS4 custom-layout activities, "~80 lessons"**: measured **86** lessons with a root
  answer that is not saved (87 have one; only `eukaryotes-prokaryotes` was saved, by
  its hand-written ROOT_SPECS entry, and only its two groups). Close to the claim.
- **KS3 activity blocks, "~266"**: measured exactly **266** instrument blocks the
  capture did not handle. But 158 of those have nothing to answer (95 reading-only:
  the 54 "Think again" panels, figure bands; 63 explorations), so the real gap was
  **108** answerable instrument blocks, plus **2** non-instrument "commit first"
  blocks (options with nothing revealed) — **110** answerable KS3 blocks not saved.
- **KS4 level picks**: none saved. **443** level-marked writes over all routes, in
  **127** lessons. (`tickTap` skipped any Ks4Write with levels; the pick lived on the
  page only.)

## After (fix/beta-1108, 8 Nov 2026)

`python3 tools/activity_save_coverage.py --md`, over the same built pages. The "before" table of
the unseen class above is the same tool with `--before`.

### KS3 (185 lessons, 747 activity blocks outside the ladder)

| block class | answerable | saved + restored | blocks |
|---|---|---|---|
| keyed commit (Start here / keyed) | yes | yes | 187 |
| instrument shape R | no | no | 95 |
| instrument (adapter A / B5C) | yes | yes | 86 |
| instrument shape G | yes | yes | 68 |
| reading (no controls) | no | no | 64 |
| instrument shape X | no | no | 63 |
| prediction (options + reveal) | yes | yes | 62 |
| worked example (reveal the next step) | no | no | 58 |
| "Your turn" calculation | yes | yes | 22 |
| instrument shape M | yes | yes | 17 |
| instrument shape S | yes | yes | 14 |
| instrument shape A | yes | yes | 5 |
| instrument shape T | yes | yes | 4 |
| commitment (options, nothing revealed) | yes | yes | 2 |

KS3 answerable blocks: **467**, saved: **467**, not saved: **0**. Instrument blocks not handled (any shape): **158**.

### KS4 rebuilt lessons (148 lessons, 522 route pages)

| root option group | kind | verdict from | saved + restored | groups (all routes) |
|---|---|---|---|---|
| answer | pick | flag | yes | 345 |
| answer | pick | words | yes | 168 |
| answer | pick | style | yes | 98 |
| answer | gate | key | yes | 40 |
| answer | pick | prediction | yes | 39 |
| answer | pick | tally | yes | 20 |
| answer | pick | key | yes | 4 |
| answer | multi | unjudged | yes | 4 |
| answer | pick | unjudged | yes | 4 |

KS4 lessons with an answerable root activity: **87**; with one NOT saved: **0**.
Distinct root answer groups (per lesson, across routes): **213**, not saved: **0**.
KS4 level picks (Ks4Write marked by levels): **443** instances over all routes in **127** lessons; not saved: **0**.

### KS4: what the option-group classifier cannot see

| class | outcome | lessons | controls (distinct, per lesson) |
|---|---|---|---|
| a list of picks (choose several) | saved + restored | 2 | 2 |
| a selector: it starts on an option already chosen | exploring (read, reason in the doc) | 46 | 59 |
| a selector: it starts on an option already chosen | saved + restored | 2 | 3 |
| a tab that records which ones were seen | exploring (read, reason in the doc) | 42 | 63 |
| a tab that records which ones were seen | saved + restored | 3 | 3 |
| no option changes the lesson here | exploring (read, reason in the doc) | 1 | 1 |
| no option changes the lesson here | saved + restored | 6 | 7 |
| no options | exploring (read, reason in the doc) | 1 | 1 |
| no options | saved + restored | 4 | 4 |
| no single place the choice is kept | exploring (read, reason in the doc) | 17 | 19 |
| no single place the choice is kept | saved + restored | 9 | 9 |
| opens a card or marks it seen | exploring (read, reason in the doc) | 46 | 56 |
| opens a card or marks it seen | saved + restored | 6 | 6 |
| part of a form another button commits | exploring (read, reason in the doc) | 1 | 1 |
| part of a form another button commits | saved + restored | 9 | 12 |
| shows a result for any choice; nothing is judged | exploring (read, reason in the doc) | 4 | 4 |
| shows a result for any choice; nothing is judged | saved + restored | 4 | 4 |
| slider | exploring (a slider: nothing asks for a value) | 8 | 8 |
| typed or selected | saved + restored | 9 | 13 |

Lessons with a control here NOT saved: **0**.

Root groups read in their lesson (saved, or a named exploration): **275**. Not read: **0**.

### What was read

Every root group the classifier files as not-an-answer has now been read in its lesson code: its
handler, and the words the lesson shows above it. **All of them: 0 not read** (the tool's count is
in the table above, and it reaches zero only when each group is named in `ROOT_FORMS` or
`tools/ks4_root_explorations.json`). "Read" here is one reading of the handler line and prompt per
group, not a walk through the page. The explorations file names the reason for each of its 204
entries; it is the list, and it is not repeated here.

Reading found real answers the classifier had filed as not-an-answer, and they are now saved and
driven: filing headlines under threats (`factors-affecting-food-security`), naming the level
(`principles-of-organisation`), the extraction method (`extraction-of-metals`), the disease from a
clue (`viral-diseases`), the prediction gates (`meiosis`), the objective gates (`microscopy`),
placing cards on the grid (`energy-resources`), the data-logger questions (`specific-latent-heat`),
which tones are heard (`sound-waves-hearing`), and the seven in the earlier run (ranking molecules,
ordering the spectrum, the bond predictor, the wall predictor, naming blood cells, the rough-titre
call, the atoms-lost call).

### What these numbers do and do not prove

- **The tables are static:** they say the capture code names a control, not that it was pressed.
- **KS4, driven:** `activity_save_drive.py`: a press on device A, the row through the backend's own
  `validateAnswerBody`, a fresh device B, and nothing posted while restoring. It passes
  **424 of 425 at 1280px** on the final code. The one red is the pupil comparison on
  `changes-in-energy`: the render counter differed (32 and 33) because the lesson's animation frame
  count depends on timing. A control ran the OLD code three times and it differs from itself the
  same way (32, 33, 32), and with the counter ignored old and new are identical. The red is left
  standing: the case was not loosened. **The drive at 390px has NOT been re-run on the final code**
  (it last passed 345 of 345 before the titration, reveal and read cases). Pupil pages compared: 7. Only the Triple Higher route of each lesson is driven. Most
  cases call the lesson's own handler, and several set a bench's earlier results straight into its
  state, rather than pressing every DOM button; cases whose capture reads the pressed words press
  the real control.
- **KS3 kinds, driven:** `activity_save_drive.py --sweep` opens one page per kind in `<ks3-specs>`,
  presses the block's first control as a child, checks a valid body, and compares the block's
  pressed states and values on a cleared browser. **At 390px on the final code: 96 of 96 kinds pass.** At 1280px it last passed 96 of 96 before the last KS4-only
  edits and was not re-run. It
  reuses one Chrome with cleared storage, not a separate profile per kind, and it proves the first
  control of the first page carrying each kind, not every instance.

### `numeric` does not imply a number

A typed answer the lesson judges is sent as `numeric`, because the server sends `written` to the
marker and discards the page's verdict. The answer need not be a number: `ks4:ionic-compounds:th#dxval-1`
carries a typed formula such as `NaCl`, and `relative-formula-mass` and `specific-latent-heat` carry
lines of text. Checked: `answers.js` treats `numeric` as "not written" and keeps the page's verdict
(`marked_by: key`), `outcomeOf` reads only `is_correct` for it, the `answer` column is text,
`consumer/parent-side.js` shows the answer as escaped text, and nothing in either repo parses it as a
number. The existing Ks4Ladder `text` rung already sends typed text as `numeric`. No code changed.

### Showing a verdict the child had not asked for

Four lessons draw their verdict behind a Reveal or Check press that is not itself an answer:
`conservation-of-mass`, `series-parallel-circuits`, `waves-detection-exploration`,
`sound-waves-hearing`. Their picks are saved and nothing is sent for the press, so on restore the
page presses it wherever the lesson's own handler accepts the saved picks (`ROOT_REVEALS`). A child
who had picked and not yet pressed Reveal therefore sees the verdict on the next load. That is the
price of not writing a row for a press.

### The restore race this run found

Four failures looked like missing restores and were not: the rows were on the server and the
page reported `done`. The replay ran before the page was ready, and whether it did depended on how
fast the read came back, so the same case passed and failed between runs.

- **KS3:** `mrbadmus.v2.js` is `defer`, so it runs with `readyState` already `interactive` but
  BEFORE `ks3.js`. The replay pressed buttons nothing was listening to.
- **KS4:** every one of the 522 rebuilt pages mounts with `libReady: false` and no blocks; a 40ms
  timer flips the flag and the next draw creates them. The replay found nothing to fill (5 restores
  in 6 failed on the level-pick case).

The replay now waits for `DOMContentLoaded` and, on a rebuilt lesson, for the draw after
`libReady`. Case `ks3-slow-script` holds `ks3.js` back on device B and fails on the old code.

### Cannot be captured, and why

Nothing here is an answer: no choice is committed and no single value could be put back.

- **KS3 reading only (95 instrument blocks, 64 other blocks):** 54 "Think again" panels, figure
  bands, no controls.
- **KS3 worked examples (58):** "reveal the next step" only. How far the child revealed is not kept.
- **KS3 explorations (63 instrument blocks):** sliders, tabs, run buttons, toggles.
- **KS4 sliders (8 lessons):** `coronary-heart-disease`, `efficiency`, `global-warming`,
  `infrared-black-bodies`, `lenses`, `metals-alloys`, `properties-small-molecules`, `resistors`.
  Each moves a model. Nothing asks for a value.
- **KS4 explorations:** 204 controls, each with its reason, in `tools/ks4_root_explorations.json`.
- **Drag and canvas:** no KS3 kind was classified D, so none is left out for this reason.
  Simulations on `<canvas>` are explorations and save nothing.

### Still NOT saved (named gaps)

- **KS3 balancer part-way:** an equation not yet balanced is not saved.
- **KS3 melting-point bench dials (`ks3-mpb-block`):** the verdict comes back, against the default
  rate and repeats, not the settings the child had chosen.
- **Bench settings generally:** a restored reading shows its result, not the animation. Which tab,
  temperature or run was on screen is not kept beyond what a form names, and a titration restored
  mid-run lands on its last recorded row.
- **Readings beyond the named benches:** a reading a lesson only draws (the reaction-time ruler,
  for instance) is not an answer here and is listed as exploring.
- **Wording:** question text on a form row is the lesson's own where the lesson has a fixed line;
  a few are short descriptions written for this table (`rate`, `mean`, `draw`, `rows`, `concord`),
  and they have not had Mide's eye.
