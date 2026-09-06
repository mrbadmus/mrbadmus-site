# `teacher/today.html` — reconciliation against Design

MRB-326 JOB 3, 6 September 2026. Branch `mrb326/j3`.

**Column one** is Design's Today, section by section, in DOM order, from the
`isToday` block of `docs/ks3/design-reference/teacher/source/Teacher Dashboard.dc.html`
(lines 59–156) plus her `renderVals` constants (lines 1544–1868).

**Column two** is what shipped on this branch.

**Column three** is the verdict. Anything that was live before this run, is not
in column one, and is not a ruled addition, was DELETED — the deletions are
listed in their own table below.

Mide's governing message for the run: *"PLEASE STOP REDUNDANCY ON THIS
PROJECT!!!!!! SO MANY PAGES ARE TOO REDUNDANT!!!!!"* — read as: if a number, a
label or a sentence appears anywhere else on the page, or is implied by the
class name, it does not appear again. Where a section below is cut, that rule
is usually why.

---

## 1. Nav

| Design | Shipped | Verdict |
|---|---|---|
| `BrandMark` (Design's chevron) + "MrBadmusAI" | plain text "MrBadmusAI", no logo asset | **RULED DIVERGENCE** — CLAUDE.md's staff brand rule. `/teacher/*` is a staff surface and takes the plain white wordmark; the chevron is for external, KS3 and STUDENT surfaces. Ruling 9 says so explicitly. |
| `navTabs` strip — Today / My classes | same two tabs, same segmented control, Today lit | MATCHES |
| `hasCrumb` breadcrumb | not rendered | REMOVED (nothing on Today computes a crumb; Design's own default is `false`) |
| "Find a student" + `/` key chip, `margin-left:auto` | same control, same shape, in the same place — and it WORKS | MATCHES (rebuilt — see note ⓐ) |
| Charts button (`openInsights`) | not rendered | REMOVED — not in ruling 9's enumeration, and it is a second navigation this page has never had. `teacher/insights.html` stays reachable from the six generated screens. |
| teacher name | `teacherName(ctx.profile)`, between the search and Sign out | MATCHES (the page always held the string; it had nowhere to put it) |
| — | "Admin" link, when the viewer is admin-scoped | **RULED ADDITION** — MRB-303 Job 2. Injected by `shared/teacher-admin-nav.js` before the last `<button>`, which is why Sign out must stay the last button in the bar. |
| Sign out | same | MATCHES |

ⓐ The generated bar could not be borrowed. It is a compiled `__MRB_TPL__` tree
driven by `shared/teacher-live.js`, which is a self-running IIFE that exports
nothing and mounts against a `#mrb-teacher` host this hand-written page does
not have. So the search is rebuilt here, and the rule that governs every
control on this page governs it: **it reads nothing until it is pressed**, then
loads `loadAcademicYears` → `loadTeacherClasses` → `loadClassMatrices` and
filters in the browser. That is the same population Design's box claims ("all
your classes") and the same population `buildSearchPool` uses on the generated
pages. No new query, no new data helper, and zero cost to the page load that
MRB-292 shrank. Gated by nine drive checks, including one that proves the read
does **not** happen before the press.

## 2. Page head

| Design | Shipped | Verdict |
|---|---|---|
| eyebrow `todayLine` — "MONDAY 31 AUGUST · AUTUMN TERM · 2026-27", 13px mono, .18em, uppercase | same slot, same type, built from data: weekday + date from the clock **read in `Europe/London`**, the term derived from the month, the year name from `loadAcademicYears().working.name` | MATCHES (ruling 8). Each of the three parts is **dropped rather than guessed**: August falls in no term and the word is simply omitted; a failed year read costs the line "2026-27" and keeps the rest. |
| h1 `greeting` — "Good morning, Ayomide" | same, from the clock and `display_name` | MATCHES |
| `todaySummary` — "4 lessons today · 57 students to chase · 3 topics worth a reteach" | same sentence, same three facts, same order. **"N students to chase" counts the whole pool — every class, not the day's** (Design's `chaseAll.length`), and "N topics" counts the reteach rows drawn. | MATCHES (⊕ corrected 6 Sep with the panel below it) |
| "Set work" (primary, filled) | **not rendered** | **RULED** — ruling 4. `DEAD` in `teacher_rulings.py`: no backend write path composes an assignment from any teacher surface, so a working one is not a front-end job and a non-working one is what that ruling forbids. Disclosed deviation from the approved screenshot. |
| "Weekly digest" | same, → `/teacher/digest.html` | MATCHES |
| "Upload timetable" | same, → `/teacher/timetable.html` | **RULED ADDITION** kept — MRB-325 ruling 1 |

## 3. Left column — the lessons

| Design | Shipped | Verdict |
|---|---|---|
| two-column grid `1.35fr 1fr`, gap 16, `align-items:start` | same ratio at ≥1000px; one stacked column below it | MATCHES (the narrow state is the same content in reading order — `today_drive`'s "390px: no horizontal overflow" is a push gate on this page) |
| h2 "Today's lessons", 29px display | same — and it names the day ("Monday's lessons") when the day shown is not today | MATCHES + ruling 2 |
| `lessonCount` — "4 LESSONS" beside the h2 | **not rendered** | **REMOVED (redundancy)** — ruling 6. The summary sentence one line above already says "4 lessons today". Design draws it twice; Mide's rule is once, and the summary keeps it. |
| "Edit timetable" underline link | same, as a real underline link rather than the button it used to be | MATCHES |
| row grid `92px / 1fr / min-content` | same | MATCHES |
| `l.p` — "P1", 21px display | same | MATCHES (it said "Period 1"; "PERIOD 1" does not fit a 92px column at 21px) |
| `l.time` — "08:45", 13.5px mono, under the period | same, **and only when `school_period_times` has a row**. No time is ever invented. | MATCHES (MRB-325 ruling 2) |
| `l.code` — "8h/Sc2", 25px display | same | MATCHES |
| `l.meta` — "LAB 2 · 29 STUDENTS · SCIENCE" | **not rendered** | **REMOVED** — ruling 1. Every part of it is already on the row or is not ours: the SUBJECT is read off the class code beside it (MRB-263 makes `/Sc` `/Ph` `/Ch` `/Bi` the subject), the STUDENT COUNT is the denominator of the status line directly under it, and there is no `room` in this schema at all. `subjectFromCode()` was deleted with it. |
| `l.ready` + `l.readyFg`, 16.5px, coloured | same slot, same colours (rust to chase, KS3 "ok" green all-in, muted otherwise) | MATCHES — strings under §7 below |
| chevron | same | MATCHES |
| — | name-picker button (icon only, `aria-label`) | **RULED ADDITION** — MRB-323. Revealed only for a class whose roster came back. |

## 4. Right column — Students to chase

| Design | Shipped | Verdict |
|---|---|---|
| header "STUDENTS TO CHASE" (rust) + `chaseCount` | same | MATCHES |
| six rows: avatar 28px / name + code on one baseline / reason under | same | MATCHES (the code used to sit on a line of its own) |
| `c.reason` — `reasonFor` | Design's branching adopted exactly: missed+low → "6 missed this term · avg 38%"; missed → "6 missed this term"; low only → "Averaging 38%"; else → "Nothing in this week" | MATCHES. It used to append "· avg 78%" to every row, which is not a reason to chase anybody. |
| `c.open` → that child's page | `→ /teacher/student-detail.html?student=…&class=…` | MATCHES |
| the panel's POPULATION — `chaseAll` iterates `liveClasses`, i.e. every class the teacher holds | same: every class this teacher teaches this academic year | MATCHES (⊕ corrected 6 Sep — it shipped scoped to today's classes, which was wrong against Design and against ruling 5's "every chase-able student". See note ⓑ) |
| footer `chaseFoot` — "+51 MORE ACROSS YOUR CLASSES" | Design's exact words, on **an openable control**: pressing it expands the panel in place to every chase-able student, grouped by class; "Show fewer" collapses it | **RULED CHANGE** — ruling 5. See §"How the full list works" below. |
| footer "Send reminders" — underline link, 600 15.5px, accent, underline-offset 3px | same markup and same values (`.panel-link`); its "Reminded N students" state keeps the treatment | MATCHES (⊕ corrected 6 Sep — it shipped as a bordered `.btn`) |
| — | the reminder write itself | already REAL before this run — `TD.sendReminders`, the same `student_notifications` upsert the class screen's "Remind all" makes. It now covers every class in the pool, which is the list the panel is showing. |

## 5. Right column — Worth a reteach

| Design | Shipped | Verdict |
|---|---|---|
| the panel's POPULATION — `reteachRows` maps `liveClasses`, the same set `chaseAll` uses | same: every class the teacher holds | MATCHES. **Design's rule was checked in her source before this was changed**, because the two panels could honestly have had different scopes and this one had the better excuse for being narrow. She scopes neither to the day. |
| `hasReteach` — the whole card is conditional | same: the card is **created only when there is something to reteach**, never rendered empty | MATCHES. It used to print "Nothing marked yet." under a heading that says "Worth a reteach" — a card whose heading and body disagree. |
| header "WORTH A RETEACH" | same | MATCHES |
| rows: code / question / pct | same, with Design's colour rule on the number (rust under 50%, muted above) | MATCHES |
| `w.min < 55` threshold | adopted | MATCHES — and it is what makes `hasReteach` mean anything. Without it the panel listed each class's weakest question however well the class did it; 92% is not worth a reteach. |
| footer caption "Lowest-scoring question on each class's last marked set" | same | MATCHES (it used to be a "+N more" count) |

## 6. Right column — Needs setting up

| Design | Shipped | Verdict |
|---|---|---|
| `hasSetup` dashed card: rows of code / line / action ("Import", "Set work") | **not rendered** | **REMOVED (redundancy + ruling 4)**. Its two rows are "No students yet" and "N students · no work set for two weeks" — both of which the lesson row for that class already says, one inch to the left, as its status line (ruling 7 keeps those two sentences there). Of its two actions, "Set work" is DEAD platform-wide and "Import" already has its own live page. So the card would repeat two sentences to offer one door that exists and one that does not. Design's own default for it is `hasSetup: false`. |

---

## Everything live that is now DELETED

Each of these was on the page before this run and is not in column one.

| Cut | Where it was | Why |
|---|---|---|
| `"No lessons at the weekend. Showing your next teaching day."` | the sub-line under the greeting | **Ruling 2.** The eyebrow says what day it is; the h2 says whose lessons these are. The sentence was the page narrating the arithmetic between two facts it had already stated. |
| `"No lessons today. Showing your next teaching day."` | same, on an empty weekday | Ruling 2, same sentence, other branch. |
| `"Next: Monday"` as the h2 | the lessons heading | Ruling 2 — the h2 now names the day directly: **"Monday's lessons"**. One word, not a label plus a sentence. |
| the day-chip strip — `MON · 10  TUE · 7  WED · 8  THU · 7  FRI · 5` | a band under the sub-line | **Ruling 3.** Design does not draw it. `.daybar` CSS and the `DAY_SHORT` array went with it. |
| `l.meta` — "KS3 · Science" on every lesson row | the lesson row | **Ruling 1.** See §3. `subjectFromCode()` deleted. |
| `lessonCount` — "3 LESSONS" beside the h2 | the h2 row | **Ruling 6, redundancy.** Said in the summary sentence. |
| `"No assignment set yet"` on every lesson row | lesson status lines | **Ruling 6.** On the drive's own fixture the held school printed this sentence **five times on one screen**. It is now said once, in the summary. |
| `"No assignment set yet"` in the chase panel | the chase panel body | Ruling 6. The panel now shows a count of `0` and no rows. |
| `"No assignment set yet"` in the reteach panel | the reteach panel body | Ruling 6. The panel is not rendered at all (Design's `hasReteach: false`). |
| `"Send reminders"` in the held state | the chase footer | Ruling 6 — there is nobody to remind and nothing to remind them about. |
| `"Couldn't load your classes just now."` twice | both panels | Redundancy. One failure, one sentence: the chase panel says it, the reteach panel is not rendered, the summary drops its counts. |
| `"nothing to chase"` | the all-in status line | **Ruling 7.** "All 29 homeworks in — nothing to chase" → **"29/29 in"**. The absence of a chase clause does not need saying, and the summary above already counts the day's whole chase list. |
| `"· 18 still to hand in"` | the chase status line | **Ruling 7.** "11 of 29 in · 18 still to hand in" said the same subtraction twice — 29 minus 11 IS 18 — and named nobody. Design's form names two of them. |
| `"· avg 78%"` on rows with a healthy average | chase rows | Design's `reasonFor` shows the average only under 50%. A good average is not a reason to chase anybody, and it pushed the number that IS one off the end of a narrow panel. |
| `"+N more across today's classes"` as the chase caption | the chase footer | ⊕ **Reverted 6 Sep.** It was the true sentence while the pool was the day; the pool is now every class, so Design's own "+N MORE ACROSS YOUR CLASSES" is correct again. The narrower sentence survives in code for the one case where it is true: a failed wide read. |
| `"+N more across today's classes"` in the reteach panel | the reteach footer | Design's footer there is her caption. There is at most one candidate per lesson on the day, so three is the panel, not a truncation of it. |
| `"…and there isn't one on your account yet"` | the no-timetable prompt | **Ruling 6.** The summary sentence directly above it says "No timetable yet." |
| the whole `.strip` band (`.strip` / `.strip-line` / `.strip-actions`) | between the greeting and the grid | Design puts the sentence directly under the h1 and the buttons on the greeting's own row — one band fewer for the same two facts. |
| `.stats` `.stat` `.row` `.name` `.meta` `.right` `.year-heading` `.year-group` `.tag` `.classlist` `.count` `.muted` `a.classlink` `.remind-row` `.page-sub` — **~80 lines of CSS** | the stylesheet | Inherited from `admin.html` when this page was written, "so the two hand-written staff pages cannot drift apart". They diverged on purpose in Phase 2a, and **not one of those selectors has ever matched a node on Today** — measured by collecting every class token the file emits. Mide's ruling covers the stylesheet as much as the copy. |

---

## How the chase full list works (ruling 5)

The footer used to be a caption. It told a teacher that fifty-one other
children owed them work and then gave them no way to see who — a dead count
standing where a door belonged.

It is now a `<button>` wearing the caption's exact typography.

* **Pressing it** redraws the chase panel **in place**, from six rows to every
  chase-able student on the day, grouped by class in the order the classes
  appear on the timetable. Each group carries a `.chase-group` heading with the
  class code.
* **The rows inside a group drop their own class code.** The heading two lines
  above has just said it — Mide's rule applied to the thing the ruling
  introduced, rather than only to what it replaced. Gated: the drive counts
  `.chase-group ~ [data-chase-student] .panel-code` and requires zero.
* **"Show fewer"** collapses it again.
* **Nothing is fetched either way.** `chaseRows` was always the whole list;
  only six of it was ever drawn. The drive proves this by comparing the stub's
  table-read log before and after the whole open/collapse interaction: the
  delta is zero.
* **"Send reminders" survives the toggle**, label and all. Expanding rebuilds
  the footer, and a "Reminded 12 students" that reverted to "Send reminders"
  on the next press would invite a teacher to send again — harmless at the
  database (the write is an upsert against the per-day rate limit) and
  misleading on the screen, which is the part that matters. `remindState` lives
  outside `paintChase()` for exactly that.

---

## ⓑ The chase pool is every class — and what it cost

Corrected 6 September 2026. The panels shipped scoped to the day's handful.
Design's own source scopes **neither**: `chaseAll` and `reteachRows` both
iterate `liveClasses`, her footer reads "+51 MORE ACROSS YOUR CLASSES", and
ruling 5 asks for "every chase-able student". A teacher chasing homework is not
chasing only the children they see before lunch.

**What is day-scoped and what is not.** The LESSON ROWS stay day-scoped,
because a lesson row is about a lesson. The two panels and the summary
sentence's chase count are across every class the teacher holds this year.

**Order.** Today's classes first, in the order they are taught — the part of
the list the teacher can still act on this morning — then every other class by
code, naturally ordered so 9A precedes 10A. It is also the dedup order, so a
child taught twice is filed under today's class rather than under whichever
other set the alphabet reached first.

**The read is in parallel, not in series.** This is the MRB-292 lesson, and it
is why the class-list read sits at the top of `onAllowed` rather than beside
the panel that consumes it:

* `loadAcademicYears` is fired once and read by three callers.
* `loadTeacherClasses` hangs off it and overlaps `loadTimetable` completely.
* The day's `loadClassMatrices` and the rest's are issued in the **same
  microtask**; the day's is awaited first so the lesson rows never wait on the
  twelfth class. The two sets are **disjoint** — the wide read asks only for
  classes the day does not cover — so nothing is fetched twice.
* `loadPaperQuestions` takes an array and chunks internally, so a dozen
  classes' newest marked papers is a couple of round trips, not a dozen; and it
  still fires after the chase panel has painted.
* The **search sheet now costs nothing at all**: it reads the pool the chase
  panel has already built. One population, one source. Its drive check went
  from "reads nothing until opened" to the sharper "adds not one read of its
  own".

**Measured.** `teacher_perf_budget` — the gate that owns MRB-325 ruling 4's
2500ms warm load — **could not be run: `$MRB_TEST_TEACHER_PASSWORD` is unset**,
and the registry skips it by name for exactly that reason. So the numbers below
are the stubbed drive's, and they are a **bound on client-side cost only**: the
stub answers every query from an in-page array, so there is no network latency
in them at all. Measured with `performance.now()` (monotonic — the drive freezes
`Date`), from navigation to the instant the chase panel has painted; median of
seven, three repeats of the whole bench.

| | median | min | max |
|---|---|---|---|
| **before** — 3 classes, all taught today | 50 ms | 23 | 155 |
| **after** — 3 classes, all taught today | 47–55 ms | 20 | 178 |
| **after** — 4 classes, one *not* taught today | 42–50 ms | 26 | 84 |

The difference is inside the run-to-run noise, which is the expected result of
issuing the wide read in parallel rather than behind the day's: the page waits
on the slower of two concurrent reads instead of on their sum.

⚠️ **One honest caveat on the read count.** The drive stubs `loadTeacherClasses`
and `loadClassMatrices` at the *data-layer* boundary, so neither reaches the
query stub's table log — which is why that log reads 8 both before and after.
The load-shape claim above rests on the code and on the wall-clock, not on that
counter. The real round-trip count is what `teacher_perf_budget` would measure,
and it remains unmeasured on this branch.

**Degradation.** If `loadTeacherClasses` or the wide matrices read fails, it
resolves to `null` — never `[]`, which would mean "this teacher has no classes"
and would quietly narrow the panel while still captioning it "across your
classes". On `null` the panels fall back to the day's classes and the footer
reverts to "+N more across today's classes", which is then the true sentence.

---

## Gate

`today_drive.py` — **112 checks, all passing** (was 53). Every assertion that
named a deleted thing now asserts its **absence**, which is an inversion, not a
weakening: the property under test in each case is unchanged.

* weekend / empty weekday: the explainer sentence and the `NEXT:` label must be
  **gone**, the h2 must name the day, and the eyebrow must still carry *today's*
  real date.
* ruling 1: no `.lesson` row carries a meta line — measured on the DOM, not on
  the joined text.
* ruling 3: no `MON`/`TUE`/`THU` day strip.
* ruling 5: the footer expands to the full list, groups it, drops the repeated
  codes, collapses again, and reads nothing new (case 9, its own wider fixture —
  case 1's three students cannot produce an overflow against a panel of six).
* correction 1: case 9's fixture carries a fourth class, `9r/Ch2`, **taught on
  Thursday**. It is never in Monday's lesson list, and the case asserts that the
  pool is 17 rather than 14, that its three students appear under a `9r/Ch2`
  group heading, and that the headings come out `8r/Sc1, 10h/Ph1, 9r/Ch2` —
  today's two first, the off-day class after. No fixture could have caught the
  day-scoping while every class in it was on the day.
* correction 1: `run_case` built the stubbed `loadTeacherClasses` from the
  module-level `TABLES` rather than the case's own — so a case that widened the
  class list silently got the base fixture's three. Fixed; it was found by the
  new assertions failing against a correct page.
* ruling 6: in the held state `"No assignment set yet"` appears **exactly once
  in `#main`'s whole innerHTML**, no lesson row carries a status line, the chase
  count is `0` with no rows and no "Send reminders", and the reteach panel is
  not rendered (case 10).
* ruling 9: both tabs, "Find a student", the teacher's name, Sign out — and the
  search opens, loads its pool only on press, filters, routes to a real page,
  says so on a miss, and closes on Escape.
* Case 8 (Job 1's — a colleague's lesson, and a slot written twice) stays green.
  Its expected period labels moved from `PERIOD n` to `Pn`; the three slots it
  asserts and the newer-row-wins collapse are untouched.

Paired screenshots: `/tmp/mrb306-today/` (all ten cases) and
`/tmp/mrb326-shots/today-live.png` (the weekday case at Design's own 1460px).
