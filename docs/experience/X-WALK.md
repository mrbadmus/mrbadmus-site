# RESULT-A — the teacher class page tells the truth about every week

Branch `feat/x-week-truth` (not pushed). Final version, rewritten from the
executor's own transcript after a Mac reboot wiped the original scratchpad
copy. Nothing was re-run to write it: every number below was observed in the
session that produced it (the TEST walk, the SQL cross-check, the gates).

## Later events (recorded by the commander after this unit left the executor)

- (a) The commander changed the closed homework card's chase heading to
  "Missed it" (`RETEXT_AT[231]`, bound to `g.chaseHead`). The executor's walk
  tables below therefore predate that wording: they were captured when a
  closed card's chase chips sat under the old "Not in yet" heading. The chips
  themselves (who is named) are unchanged.
- (b) The commander added EXCLUDED rows to `gate_registry.py` for
  `week_truth_fixture.py` and `week_truth_drive.py` (they seed and drive TEST;
  they are tools, not gates).
- (c) The commander tore the TEST fixture down and verified zero rows remain
  (id prefix `f3530000-`).
- (d) `teacher_behaviour.py` then PASSED on the stacked tip. During the
  executor's session it could not complete: two runs each aborted on a raw CDP
  WebSocket timeout under machine-wide memory pressure (10 Chrome processes
  from other lanes, ~64 MB free pages, swap 7.5 of 8 GB), no assertion failed
  in either run. That is now closed.

## The single function

`weekScope(papers, weeks, wi, now)` in `shared/teacher-live.js`, beside
`buildWeeks`. Pure: no DOM, no fetch. Returns

```
{ week, started, startsOn, weekEndMs, papers, released, live, closed,
  scheduled, lastClosed }
```

- `papers` is the selected chip's own bucket, by the rule `wPapers` always
  used: chip 0 takes `weekIdx <= 0 or null`; the oldest chip takes
  `weekIdx >= wi`; every other chip takes `weekIdx === wi`.
- `released` / `live` / `closed` / `scheduled` are filters of that bucket on
  `state` / `closed`.
- `started` is `now >= the week's own Monday 00:00 (London)`. It is false only
  on a Sunday, when MRB-330 rolls chip 0 forward onto the week that starts
  tomorrow.
- `lastClosed` scans EVERY paper the class has (not only the bucket), newest
  `due_at` first, for the first that is released, genuinely closed
  (`p.closed`), not a flashcard set, and due at or before the cutoff. Cutoff =
  the selected week's end (the following Monday 00:00 London, LITERAL, no
  grace) capped at `now`. For chip 0 and any week not yet ended the cutoff is
  simply `now`, which is the unscoped search chip 0 used to run by hand,
  reached here with no `wi === 0` branch anywhere.
- It does not filter on submissions, so "the most recent closed set even if
  nobody sat it" falls out of the shape. A caller wanting "closed and sat"
  (the breakdown link) tests `colSub[lastClosed.idx]` itself.
- `buildWeeks` gained `started` and `endMs` (following Monday 00:00 London,
  epoch ms) per week. Old fixtures lack both; a missing `started` reads as
  `true` and a missing `endMs` as unbounded (cutoff = `now`), so existing
  fixtures behave as before.

Emitted wrappers in `build_teacher_port.py`: `MRB_WEEK_SCOPE(papers, weeks,
wi)` delegating to `window.MrBadmusTeacherLive.weekScope(..., Date.now())`
(the `MRB_WEEK_SCORE` / `MRB_NEWEST_MARKED` pattern), and
`MRB_OPENS_LABEL(releaseIso, monYmd)` giving the not-started-week card its
"Opens Mon 5 Oct" / "starts Mon 5 Oct" date via `teacher-live.js`'s
`dowDayMonthLdn`.

## Files changed, by function

**`shared/teacher-live.js`**
- `buildWeeks(year, now)`: `started` / `endMs` per week.
- `weekScope(...)`: new.
- `load(screen, params)`, class-screen grid prefetch: now
  `weekScope(cPapers, c.WEEKS[classId], 0, now).lastClosed` for chip 0 (the
  page always opens on chip 0), replacing a separate "newest released paper
  with a submission" search. Stepping to another chip is covered by the lazy
  `MRB_ENSURE_GRID` below.
- Export list: added `weekScope`, `buildWeeks`, `assignPaperWeeks`,
  `dowDayMonthLdn`, `asDate`.

**`build_teacher_port.py`**: `MRB_WEEK_SCOPE`, `MRB_OPENS_LABEL`.

**`teacher_rulings.py`** (all in the class screen's `renderVals`)
- `const openP` anchor: introduces `const wScope = MRB_WEEK_SCOPE(kPapers,
  kWeeks, wi)`; `wPapers` / `wReleased` read off it; `wOldest` retired.
- `const lastP = kPapers[1] || null;` anchor: now `const lastP =
  wScope.lastClosed;`. The MRB-353 `wi === 0` / `wPapers.filter(p.closed &&
  colSub>0)` branches are gone.
- NAV `glance.openMarking`: opens `lastP.idx` directly (no second
  `MRB_NEWEST_MARKED` call).
- `g1` / `worstTwo`: added `if (lastP && !g1) MRB_ENSURE_GRID(k.id,
  lastP.idx);`, the lazy fetch the Assignments table's cells already use.
- MRB-336 §4.1 homework-card block: `wDone` is `wScope.closed` sorted (the
  `(wi === 0) ? [] : ...` guard removed); `let wCards`; a new `if
  (!wScope.started && !wCards.length)` branch builds the not-started card from
  `wScope.scheduled` (first by `release_at`, eyebrow "Opens ...", no count / bar
  / chips / Remind, "+N more") or "Nothing set yet . starts <Monday>". The
  generic empty card for a STARTED week with nothing is untouched, as are
  `cardOf` / `closedCardOf` (their Sharpen C6 text anchors still match once).
- Watch / praise: Design's class-wide `flagged` / `reasonFor` / "Top average"
  block AND the withdrawn MRB-353 `if (wi !== 0)` block replaced by one
  computation for every STARTED week: `wClosedIdxs` (the week's own closed
  released papers), `wWatchPct`, `wWatchMissed`, `flagged`, `watch`,
  `best`/`imp`, `praise`, `noWatchLine`. A pupil is watched for missing a
  CLOSED set (reasons "Missed it" if all closed sets missed, "Missed N of M"
  if some) or averaging under 50% on the week's submitted sets ("N% on it").
  Missing a still-open set never flags anyone (the homework card's chase chips
  already name them). A week that has not started flags nobody and praises
  nobody. The old block's reason read `t.closed`, a field `wTally` never
  carried, so every out pupil read "Not in yet"; that is gone with it.
- `rosterWeight`, `allFlagged`, the roster row's `flag:` read membership of
  `flagged` instead of the class-wide `r.flag` (which is untouched in
  `teacher-live.js`; other screens still read it).
- `glance` literal gained `noWatchLine` and `hasBreakdown: !!(lastP &&
  (kMx.colSub[lastP.idx] || 0) > 0)`.
- `RETEXT_AT[266]`: the "No one flagged . the class is keeping up." literal
  rebound to `glance.noWatchLine` (not started or an open set: "Nothing to
  flag yet."; closed sets only: "No one flagged . the class is keeping up.";
  no released set: "Nothing to flag.").
- `WRAP["class-detail.html"][253] = "glance.hasBreakdown"`: hides "Open the
  full breakdown" when there is no `lastP` or nobody sat it.

**`gate_registry.py`**: registered `week_scope_check` (fast; watches its own
script, the .js and `shared/teacher-live.js`).

**New**: `week_scope_check.js` / `.py` (the fast gate), `week_truth_fixture.py`
(throwaway TEST world: seed / teardown / show), `week_truth_drive.py` (the
Chrome walk). `.gitignore` gained the fixture's local id manifest.

## The deviation, made and corrected mid-session

The executor first read the bug report's "week 4 reteach showed week 4's own
set" as a fact to preserve and added a one-calendar-day grace to the cutoff
so Changes of State (due Mon 28 Sep 09:00 BST, hours after week 4's end at
28 Sep 00:00) would still count as closed "by" week 4. That was backwards:
that line IS item 1 of the defect. Week 4's own chip must read "Nothing to
reteach yet", because nothing had closed by its end (the two Energy rows are
deleted and invisible). The commander caught it from the relayed transcript
before it shipped; the grace was removed, `week_scope_check.js`'s week-4
assertion was corrected from expecting Changes of State to expecting `null`,
and a rebuild followed. The corrected behaviour is what every table below
shows, independently on three assignments in two classes (Changes of State,
Teacher set C, the 5 Oct MCQ): a set due after the Monday that ends its own
week does not count as closed by that week.

Other spec departures, stated plainly:
- The spec asked for class-detail fixture(s) shaped like 10h/Ph1 at Sun 4 Oct
  01:00 so `teacher_behaviour` drives them. None was added; the TEST walk
  (production-shaped, real data, frozen clock) and the Node gate are the
  substitute. Named as a gap, not silently dropped.
- No existing fixture expectation changed (none encoded the bug), so there is
  nothing to list under "expectations changed and why".
- `mrb348_teacher_equiv.py` is a two-tree `--capture` / `--compare` drive,
  excluded from the registry; it was not run as an old-vs-new capture.
  `weekScope` reads only `papers` and never the matrix, so it cannot move the
  matrix-vs-rollup equivalence that gate tests (checked by reading).

## Gates

On the REBUILT tree (`python3 build_all.py` clean after the grace revert):
- `week_scope_check.py`: 20 passed, 0 failed (also via `node
  week_scope_check.js`, TZ pinned Europe/London).
- `teacher_tells.py`: PASS (6 live pages, no sample value, no literal count).
- `gate_watches_check.py`: PASS (74 gates).
- `teacher_behaviour.py`: before the grace revert, PASS (25 fixtures, 1028/961
  controls). After the rebuild, two executor runs aborted on CDP timeouts
  under memory pressure with no assertion failing; deferred to the stack-tip
  run, where it PASSED (see "Later events", d).
- Chrome hygiene: no Chrome the executor started was left running; the
  orphan-looking groups seen were other lanes' (`ks4_chrome_drive.py`,
  `verify_ks3.py`) and were left alone. Zero processes killed by this lane.

`week_scope_check.js` asserts, under Node against the real
`buildPapers` / `assignPaperWeeks` / `buildWeeks` / `weekScope`: `started` is
false only at the Sun clock; chip 0 `lastClosed` is Changes of State at Sun /
Wed / Mon and Temperature at Tue; week 5's chip before Temperature closes
surfaces Changes of State; week 4's own chip is `null`; before either set is
released it is `null`; 8r/Sc1's flashcard set never shadows the MCQ due the
same day; the pre-term-start set lands in the oldest chip's bucket; flashcards
still appear in `closed`; a week object without `started` / `endMs` behaves as
before.

## The TEST walk

World: `week_truth_fixture.py`, TEST project `qeppkiswvclkkwbxmlok`, every id
prefixed `f3530000-`, one school, academic year pinned to 2026-09-01 ..
2027-08-31 (literal dates, not "today", so weeks sit at fixed positions),
one throwaway teacher, three classes (all with automatic weekly work off):

- **10h/Ph1** (17 pupils; class_tier_rule gave higher / triple / physics).
  "Particle Model of Matter . Changes of State": teacher, `academic_week` 4,
  released Sun 20 Sep, due Mon 28 Sep 08:00Z (09:00 BST), 8 of 17 complete.
  "... Temperature Changes and Specific Heat Capacity": `academic_week` 5,
  released Mon 28 Sep 14:45Z, due Mon 5 Oct 17:00Z (18:00 BST), 3 of 17
  complete. Two soft-deleted "Energy" rows (weeks 2 and 3).
- **8r/Sc1** (2 pupils). Week-1 auto set (due Thu 3 Sep, both done); Teacher
  sets A / B / C released Tue 8 Sep 18:42Z (A, B due Tue 15 Sep 17:00Z, C due
  Wed 16 Sep 06:00Z; pupil 1 did A + C, pupil 2 did B); flashcards "fc1" due
  Mon 5 Oct 00:00Z; MCQ due Mon 5 Oct 17:00Z (both done); flashcards due
  Fri 9 / Sat 10 Oct; an old set due 25 Aug (before term start; no
  submissions).
- **9r/Sc2** (3 pupils). Exactly one set ever, `academic_week` 3, due Tue
  22 Sep 17:00Z; nobody has submitted it.

Method: Chrome headless via `ks3_browser.py`; clock frozen by overriding
`window.Date` before any page script (`Page.addScriptToEvaluateOnNewDocument`)
because this Chrome has no `Emulation.setFixedTime`, plus
`Emulation.setTimezoneOverride` to Europe/London; signed in as the teacher
through `auth.html`; opened the generated `teacher/class-detail.html?env=test`;
clicked every `[data-week]` chip and read
`window.__MRB_CMP__.logic.renderVals()` directly. Gotchas recorded: TEST's
GoTrue admin LIST endpoint answered 500 every time (single create / get-by-id
and PostgREST worked), so the fixture never lists, writes each created id to a
gitignored manifest, and tears down from that snapshotted list. A few
(clock, class) walks failed to render a chip on the first pass (the first class
in a session always rendered; later ones sometimes did) and were re-run with a
fresh browser each; all data below is from successful renders.

Reading the tables: "week 5 (28/09)" means the chip labelled Week 5 whose
Monday is 28/09. A week's end is the following Monday 00:00 BST. Table-row
flag = "NEEDS A LOOK" membership; blank week / score cells are shown as blank.
Pupil names in the fixture are `Pupil wt_...`; chip names are truncated by the
page's own `shortName`. Per the commander's later change (a), closed cards now
head their chase list "Missed it"; chase membership is as listed.

### 10h/Ph1 . Sun 4 Oct 2026 01:04 BST (the live defect's own clock)

Six chips; chip 0 = week 6 (05/10), NOT started (its Monday is tomorrow).

| chip | started | homework card | reteach | keep an eye on | shoutout |
|---|---|---|---|---|---|
| 0 (wk6, 05/10) | no | "This week's homework" / "Nothing set yet . starts Mon 5 Oct", no count, bar, chips or Remind | Changes of State, 8/17 submitted, bars Q7 25% and Q4 38%, breakdown link live | empty, "Nothing to flag yet." | none |
| 1 (wk5, 28/09) | yes | live card: Temperature, due Mon 5 Oct, 3 of 17 in, chases 14 | Changes of State, 8/17, same bars | empty, "Nothing to flag yet." | Pupil 03 "Top score . 88%" |
| 2 (wk4, 21/09) | yes | closed card: Changes of State, "Closed . due Mon 28 Sep", 8 of 17 in, chases 9 | "Nothing to reteach yet", no bars, no breakdown link | 4 shown + "5 more": "Missed it" (pupils 09-17) | Pupil 07 "Top score . 100%" |
| 3 (wk3, 14/09) | yes | "No work set in this week" | "Nothing to reteach yet" | empty, "Nothing to flag." | none |
| 4 (wk2, 07/09) | yes | "No work set in this week" | "Nothing to reteach yet" | empty, "Nothing to flag." | none |
| 5 (wk1, 31/08) | yes | "No work set in this week" | "Nothing to reteach yet" | empty, "Nothing to flag." | none |

Table cells: chip 0 flags nobody, week and score cells blank, "Last active"
shows real times ("2 days ago", "yesterday", "24 Sep", ...), never "No
activity yet" for a pupil who has been active. Chip 1: rows read "Not
started" for the 14 who have not begun the open set; no flags (open set).
Chip 2: pupils 09-17 read "Missing" with the NEEDS A LOOK flag, sorted to the
top; the 8 who submitted are unflagged. Chips 3-5: blank week cells, no flags.

Why: chip 0 has not started and holds nothing, so the card is honest about
that, while the reteach cutoff is `now` and the newest closed set is Changes
of State. Chip 1: Temperature is still open so it cannot be the reteach and
nobody is flagged for an open set; Changes of State (due 28 Sep, inside week
5's cutoff 5 Oct 00:00) is the answer. Chip 2: Changes of State is week 4's
own card, but its deadline (28 Sep 09:00 BST) is after week 4's end
(28 Sep 00:00), so nothing had closed by then. Chips 3-5: no released set; the
two deleted Energy rows never appear.

### 8r/Sc1 . Sun 4 Oct 2026 01:04 BST

Six chips. T1 / T2 / T3 have no `academic_week` (deliberately, to exercise the
due_at minus 7 fallback) and all bucket into chip 4. Chip 5 is the oldest
chip and holds BOTH the week-1 auto set and the pre-term-start "old" set
(both clamp to week 1; `weekIdx` equal, oldest chip takes `>=`).

| chip | started | homework card(s) | reteach | keep an eye on |
|---|---|---|---|---|
| 0 (05/10) | no | "Nothing set yet . starts Mon 5 Oct" | Teacher set C, 1/2 submitted, breakdown live | empty, "Nothing to flag yet." |
| 1 (28/09) | yes | MCQ due Mon 5 Oct (2 of 2 in); Flashcards due Sat 10 Oct (0 of 2, chases both) + "+2 more" | Teacher set C, 1/2 | empty, "Nothing to flag yet." |
| 2 | yes | "No work set in this week" | Teacher set C, 1/2 | empty, "Nothing to flag." |
| 3 | yes | "No work set in this week" | Teacher set C, 1/2 | empty, "Nothing to flag." |
| 4 (07/09, A/B/C) | yes | closed card: Teacher set C, "due Wed 16 Sep", 1 of 2 in, chases 1, "+2 more" | Week 1 auto set, 2/2 | pupil 1 "Missed 1 of 3", pupil 2 "Missed 2 of 3" |
| 5 (31/08, oldest) | yes | closed card: Week 1 auto set, "due Thu 3 Sep", 2 of 2 in, "+1 more" | Week 1 auto set, 2/2 | pupil 1 and pupil 2 "Missed 1 of 2" |

Why: chip 0 / 1: the newest closed set class-wide is Teacher set C (due
16 Sep); the Oct sets are open or not yet closed; flashcards are never
reteach sources. Chip 4: A / B / C are all due after their own week's end
(14 Sep 00:00), the same Monday-morning shape as Changes of State, so reteach
falls back to the week-1 auto set (due Thursday, inside its own week); pupil 1
did A and C (missed B), pupil 2 did only B (missed A and C), denominator = the
3 closed sets of the week. Chip 5: the "+1 more" and the denominator 2 are the
"old" set, which neither pupil submitted. Pupil 1 and 2 each missed only that.

### 9r/Sc2 . Sun 4 Oct 2026 01:04 BST

Six chips; the one set sits in chip 3 (`academic_week` 3), nobody has done it.
Chips 0 and 3 were read straight from the render; chips 1, 2 and 5 are
confirmed by an exact `weekScope` reproduction under Node (chip 1 / 2 reteach
= the set, chip 5 = null) and consistent with the Wed / Mon / Tue renders
below.

| chip | homework card | reteach | keep an eye on |
|---|---|---|---|
| 0 (05/10, not started) | "Nothing set yet . starts Mon 5 Oct" | "The only set this class has ever had", 0/3 submitted, no bars, NO breakdown link | empty, "Nothing to flag yet." |
| 1, 2 | "No work set in this week" | the same set, 0/3, no breakdown link | empty, "Nothing to flag." |
| 3 (14/09, the set's own week) | closed card: "due Tue 22 Sep", 0 of 3 in, chases 3 | "Nothing to reteach yet" | 3 pupils "Missed it" |
| 4, 5 | "No work set in this week" | "Nothing to reteach yet" | empty, "Nothing to flag." |

Why: Mide's rule is literal, so a closed set nobody sat is still the reteach
(title and 0/3), but with no bars and no link. The set is due Tue 22 Sep,
after week 3's end (21 Sep 00:00), so its own week cannot reach it; week 4
onward can.

### 10h/Ph1 . Wed 30 Sep 2026 12:00 BST

Five chips (the year is a week younger; chip 0 = week 5 = Temperature's week).
Temperature is released and open.

| chip | started | homework card | reteach | keep an eye on | shoutout |
|---|---|---|---|---|---|
| 0 (wk5, 28/09) | yes | live card: Temperature, due Mon 5 Oct, 3 of 17 in, chases 14 | Changes of State, 8/17, bars Q7 25% / Q4 38%, breakdown live | empty, "Nothing to flag yet." | Pupil 03 "Top score . 88%" |
| 1 (wk4, 21/09) | yes | closed card: Changes of State, 8 of 17 in, chases 9 | "Nothing to reteach yet" | 4 + "5 more": "Missed it" | Pupil 07 "Top score . 100%" |
| 2 (wk3, 14/09) | yes | "No work set in this week" | "Nothing to reteach yet" | empty, "Nothing to flag." | none |
| 3 (wk2, 07/09) | yes | "No work set in this week" | "Nothing to reteach yet" | empty, "Nothing to flag." | none |
| 4 (wk1, 31/08) | yes | "No work set in this week" | "Nothing to reteach yet" | empty, "Nothing to flag." | none |

Why: the current week's own closed set count is zero, so nobody is flagged
(the 14 not yet in on Temperature are named by the card's chips); cutoff is
`now` so Changes of State is the reteach. Everything else is as on the Sun
clock. Chip 0 rows read "Not started" for non-submitters, no flags.

### 8r/Sc1 . Wed 30 Sep 2026 12:00 BST

Five chips. T-sets closed; the four Oct sets (fc1, mcq1, fc2, fc3) released
and open.

| chip | homework card(s) | reteach | keep an eye on |
|---|---|---|---|
| 0 (wk5, 28/09) | MCQ due Mon 5 Oct (2 of 2 in); Flashcards due Sat 10 Oct (0 of 2, chases both) + "+2 more" | Teacher set C, 1/2 | empty, "Nothing to flag yet." (rows read "1 of 4 in") |
| 1 (wk4) | "No work set in this week" | Teacher set C, 1/2 | empty, "Nothing to flag." |
| 2 (wk3) | "No work set in this week" | Teacher set C, 1/2 | empty, "Nothing to flag." |
| 3 (wk2, A/B/C) | closed card: Teacher set C, 1 of 2 in, "+2 more" | Week 1 auto set, 2/2 | "Missed 1 of 3" / "Missed 2 of 3" |
| 4 (wk1, oldest) | closed card: Week 1 auto set, 2 of 2 in, "+1 more" | Week 1 auto set, 2/2 | "Missed 1 of 2" each |

Why: identical reasoning to the Sun table, with the bar one chip shorter.
All four Oct sets are open, so nobody is flagged on chip 0.

### 9r/Sc2 . Wed 30 Sep 2026 12:00 BST

Five chips.

| chip | homework card | reteach | keep an eye on |
|---|---|---|---|
| 0 (wk5) | "No work set in this week" | the only set, 0/3, no breakdown link | empty, "Nothing to flag." |
| 1 (wk4) | "No work set in this week" | the only set, 0/3, no breakdown link | empty, "Nothing to flag." |
| 2 (wk3, its own week) | closed card, "due Tue 22 Sep", 0 of 3 in, chases 3 | "Nothing to reteach yet" | 3 pupils "Missed it" |
| 3 (wk2) | "No work set in this week" | "Nothing to reteach yet" | empty, "Nothing to flag." |
| 4 (wk1) | "No work set in this week" | "Nothing to reteach yet" | empty, "Nothing to flag." |

### 10h/Ph1 . Mon 5 Oct 2026 12:00 BST (Temperature still open, due 18:00 BST)

Six chips; chip 0 = week 6, started (it is Monday).

| chip | homework card | reteach | keep an eye on | shoutout |
|---|---|---|---|---|
| 0 (wk6, 05/10) | "No work set in this week" | Changes of State, 8/17, bars Q7 25% / Q4 38%, breakdown live | empty, "Nothing to flag." | none |
| 1 (wk5, 28/09) | live card: Temperature, 3 of 17 in, chases 14 | Changes of State, 8/17, bars as above | empty, "Nothing to flag yet." | Pupil 03 "Top score . 88%" |
| 2 (wk4, 21/09) | closed card: Changes of State, 8 of 17, chases 9 | "Nothing to reteach yet" | 4 + "5 more": "Missed it" | Pupil 07 "Top score . 100%" |
| 3 (wk3) | "No work set in this week" | "Nothing to reteach yet" | empty, "Nothing to flag." | none |
| 4 (wk2) | "No work set in this week" | "Nothing to reteach yet" | empty, "Nothing to flag." | none |
| 5 (wk1) | "No work set in this week" | "Nothing to reteach yet" | empty, "Nothing to flag." | none |

Why: Temperature is due at 18:00 BST, six hours after this clock, so it is
not closed and cannot be `lastClosed` anywhere yet. Chip 0 (week 6) has no
released set of its own ("Nothing to flag.", not "yet"), and its rows are
unflagged with blank week cells.

### 8r/Sc1 . Mon 5 Oct 2026 12:00 BST

Six chips; fc1 (flashcards due Mon 5 Oct 01:00 BST) has closed at this clock,
the MCQ (18:00 BST) has not.

| chip | homework card(s) | reteach | keep an eye on |
|---|---|---|---|
| 0 (wk6) | "No work set in this week" | Teacher set C, 1/2 | empty, "Nothing to flag." |
| 1 (wk5, 28/09) | MCQ due Mon 5 Oct (2 of 2 in); Flashcards due Sat 10 Oct (0 of 2, chases both) + "+1 more" | Teacher set C, 1/2 | both pupils "Missed it" |
| 2 (wk4) | "No work set in this week" | Teacher set C, 1/2 | empty, "Nothing to flag." |
| 3 (wk3) | "No work set in this week" | Teacher set C, 1/2 | empty, "Nothing to flag." |
| 4 (wk2, A/B/C) | closed card: Teacher set C, 1 of 2 in, "+2 more" | Week 1 auto set, 2/2 | "Missed 1 of 3" / "Missed 2 of 3" |
| 5 (wk1, oldest) | closed card: Week 1 auto set, 2 of 2 in, "+1 more" | Week 1 auto set, 2/2 | "Missed 1 of 2" each |

Why: chip 1's bucket holds one closed paper (the flashcard set fc1, closed at
01:00) and three open ones; neither pupil has finished the deck, so both
"Missed it" (the only closed set of the week). The MCQ, still open, flags
nobody. fc1 being closed does not make it the reteach (flashcards are
excluded), so Teacher set C stays.

### 9r/Sc2 . Mon 5 Oct 2026 12:00 BST

Six chips.

| chip | homework card | reteach | keep an eye on |
|---|---|---|---|
| 0 (wk6) | "No work set in this week" | the only set, 0/3, no breakdown link | empty, "Nothing to flag." |
| 1 (wk5), 2 (wk4) | "No work set in this week" | the only set, 0/3, no breakdown link | empty, "Nothing to flag." |
| 3 (wk3, its own week) | closed card, "due Tue 22 Sep", 0 of 3 in, chases 3 | "Nothing to reteach yet" | 3 pupils "Missed it" |
| 4 (wk2), 5 (wk1) | "No work set in this week" | "Nothing to reteach yet" | empty, "Nothing to flag." |

### 10h/Ph1 . Tue 6 Oct 2026 12:00 BST (Temperature now closed)

The other half of the defect's regression: the answer for the current week
must flip to Temperature, while Temperature's OWN week must not.

| chip | homework card | reteach | keep an eye on | shoutout |
|---|---|---|---|---|
| 0 (wk6, 05/10) | "No work set in this week" | Temperature, 3/17 submitted, breakdown live (no bars: the fixture holds no per-question attempts for Temperature) | empty, "Nothing to flag." | none |
| 1 (wk5, 28/09) | closed card: Temperature, "Closed . due Mon 5 Oct", 3 of 17 in, chases 14 | Changes of State, 8/17, bars Q7 25% / Q4 38% | 4 + "10 more": "Missed it" (the 14 who never submitted Temperature, the week's one closed set) | Pupil 03 "Top score . 88%" |
| 2 (wk4, 21/09) | closed card: Changes of State, 8 of 17, chases 9 | "Nothing to reteach yet" | 4 + "5 more": "Missed it" | Pupil 07 "Top score . 100%" |
| 3 (wk3) | "No work set in this week" | "Nothing to reteach yet" | empty, "Nothing to flag." | none |
| 4 (wk2) | "No work set in this week" | "Nothing to reteach yet" | empty, "Nothing to flag." | none |
| 5 (wk1) | "No work set in this week" | "Nothing to reteach yet" | empty, "Nothing to flag." | none |

Why: Temperature closed 18 hours ago, so chip 0's cutoff (`now`) reaches it.
Chip 1 asks the permanently different question "closed by the end of week 5
(5 Oct 00:00)"; Temperature's own deadline (5 Oct 18:00) is after that, so
Changes of State is still the answer and always was. Chip 1's table: the 14
non-submitters read "Missing" with the flag; chip 1's watch list is the same
14. Chip 2 is unchanged by Temperature closing.

### 8r/Sc1 . Tue 6 Oct 2026 12:00 BST

Six chips; the MCQ (due 5 Oct 18:00 BST) and fc1 are closed.

| chip | homework card(s) | reteach | keep an eye on |
|---|---|---|---|
| 0 (wk6) | "No work set in this week" | MCQ - due Mon 5 Oct, 2/2 submitted, breakdown live | empty, "Nothing to flag." |
| 1 (wk5, 28/09) | Flashcards due Sat 10 Oct (0 of 2, chases both); Flashcards due Fri 9 Oct (0 of 2, chases both) | Teacher set C, 1/2 | both pupils "Missed 1 of 2" |
| 2 (wk4) | "No work set in this week" | Teacher set C, 1/2 | empty, "Nothing to flag." |
| 3 (wk3) | "No work set in this week" | Teacher set C, 1/2 | empty, "Nothing to flag." |
| 4 (wk2, A/B/C) | closed card: Teacher set C, 1 of 2 in, "+2 more" | Week 1 auto set, 2/2 | "Missed 1 of 3" / "Missed 2 of 3" |
| 5 (wk1, oldest) | closed card: Week 1 auto set, 2 of 2 in, "+1 more" | Week 1 auto set, 2/2 | "Missed 1 of 2" each |

Why: chip 0 now reaches the MCQ (the newest closed non-flashcard); fc1, closed
at the same instant, is excluded by kind. Chip 1 asks "closed by 5 Oct 00:00",
which the MCQ (18:00 BST) misses: third independent confirmation of the
Monday-morning shape. Chip 1's week holds two closed papers (fc1, mcq1); each
pupil submitted the MCQ but not fc1, hence "Missed 1 of 2". The two live decks
are the cards.

### 9r/Sc2 . Tue 6 Oct 2026 12:00 BST

Six chips. Identical to the Mon table: chips 0-2 reteach the only set (0/3, no
bars, no breakdown link, "Nothing to flag." / no work), chip 3 is its own
closed card (0 of 3 in, 3 pupils "Missed it") with "Nothing to reteach yet",
chips 4-5 empty. Nothing about "today" can move this class's answer.

## Per-question percentages, recomputed from TEST rows (SPEC-A section 57)

```sql
select a.question_index,
  count(*) filter (where a.is_correct is not null) as marked,
  count(*) filter (where a.is_correct) as correct,
  round(100.0 * count(*) filter (where a.is_correct)
        / count(*) filter (where a.is_correct is not null)) as pct
from assignment_question_attempts a
join assignment_submissions s on s.id = a.submission_id
where s.assignment_id = 'f3530000-0000-0000-0000-000000000041'  -- Changes of State
group by a.question_index order by a.question_index;
```

| question_index | correct/marked | pct |
|---|---|---|
| 0, 1, 2, 4, 5, 7 | 8/8 | 100 |
| 3 | 3/8 | 38 |
| 6 | 2/8 | 25 |

The card's two bars are "Q7 . 25%" and "Q4 . 38%" (label = index + 1), an exact
match. Can `grid(classId, idx)` mix papers? No: it is fetched and cached per
`(classId, paperIdx)`, `paperIdx` is the index of one specific assignment,
and `buildGrid` joins `assignment_question_attempts` to that assignment's
submissions only. Changes of State and Temperature are different
`assignment_id`s. The old failure Mide described ("questions from that week,
numbers from the newer week") came from the reteach card resolving a different
paper than the one it named, not from the grid; with `lastP` now the single
source for title, count, bars (via `MRB_ENSURE_GRID(k.id, lastP.idx)`) and
breakdown link they cannot diverge.

## Unresolved / for the record

- No class-detail fixture shaped like 10h/Ph1 was added (see deviations).
- `mrb348_teacher_equiv.py` not run as a capture / compare.
- The tables for 9r/Sc2 at the Sun clock (chips 1, 2, 5) and the one-line
  summary for 9r/Sc2 at Tue rely on the Node reproduction plus the identical
  Mon renders rather than a separate full read-out.
