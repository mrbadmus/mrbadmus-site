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
