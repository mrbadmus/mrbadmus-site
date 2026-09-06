# Class detail — Design's screen against the built page

**MRB-326 JOB 4.** Written before the run and updated at the end of it, so the
right-hand column is what SHIPPED rather than what was intended.

Column 1 is Design's v3 class screen in DOM order — `docs/ks3/design-reference/
teacher/source/Teacher Dashboard.dc.html`, nodes 207–328, the `sc-if isClass`
branch. Column 2 is what the built page carried BEFORE this run
(`teacher_fixtures/class-detail-fixture.html` plus the live screenshot at
`v3 targets/Screenshot 2026-09-06 at 05.23.13.png`). Column 3 is the verdict.

**The acceptance rule:** anything live that is not in column 1 and is not a
ruled addition is DELETED this run.

**Mide's governing rule, 6 Sep 2026, verbatim:** *"PLEASE STOP REDUNDANCY ON
THIS PROJECT!!!!!! SO MANY PAGES ARE TOO REDUNDANT!!!!!"* — if a number, a
label or a sentence appears anywhere else on the page, or is already implied by
the class name (MRB-263: `8r/Sc1` says Year 8 and Science), it does not appear
again.

---

## 1. Design's sections, in DOM order

| # | Design (node) | Live state before this run | Verdict |
|---|---|---|---|
| — | *(nothing above the header)* | **A banner box above the header**: "Everyone has handed this week's work in." / "N students have not handed this week's work in." + "Remind all N" / "Reminded today". Injected by `drawRemindControl` in `shared/teacher-live.js`. | **REMOVED (not Design's, and redundant)** — Mide, JOB 4c. It sat above a card whose own 34px number already read "2 of 2 in". Its behaviour moved into Design's own in-card button; see row 10. |
| 1 | `‹ Back to today` (210) | present | MATCHES |
| 2 | **Set work** (214, primary) | absent | REMOVED — `DEAD`, MRB-287: creating an assignment has no write path. |
| 3 | **Shoutouts** (215) | present | MATCHES |
| 4 | **Charts** (216) | present | MATCHES |
| — | — | **Pick a student** | RULED ADDITION — `INSERT_AT (213, 216)`, `AMENDED_ADDITIONS` marker `pick-open`, MRB-323. STAYS. |
| 5 | **Print report** (217) | present | MATCHES |
| — | — | **Seating plan** | RULED ADDITION — `INSERT_AT (213, 217)`, marker `class-seating`, MRB-322. STAYS. |
| 6 | `<h1>` class code (219) | present | MATCHES |
| 7 | eyebrow `klass.meta` (220) — "28 STUDENTS · YEAR 7 SCIENCE · NO LESSON TODAY" | "2 STUDENTS · YEAR 8 SCIENCE · NO LESSON TODAY" | **REMOVED (redundancy) in part** — "YEAR 8 SCIENCE" cut, JOB 4e. `8r/Sc1` above it already says Year 8 and Science (MRB-263). Now reads "2 STUDENTS · NO LESSON TODAY". |
| 8 | stat line `klass.statLine` (221) — "Class mean 62% · 80% on time · 4 students to keep an eye on" | same shape | **REMOVED (redundancy) in part** — the keep-an-eye segment cut, JOB 4e. Card 3 IS "Keep an eye on", names those children, and says "No one flagged" when there are none. Now reads "Class mean 42% · 100% on time". ⊕ post-review 6 Sep: **on a class with no papers the line is now BLANK**, where it said "No work set yet" — the third of three sentences saying there is no work (node 280 heads the empty state, and the Assignments caption says "None set"). A statistics strip with no statistics says nothing. |
| — | — | **the week bar** (WEEK ‹ chip ›) | RULED ADDITION — `INSERT_AT (208, 218)`, Mide 1 Sep 2026, MRB-325 ruling 7. STAYS. |
| — | — | "This week · 31/08/26 · 2 assignments set · Week mean 42%" (`weekNote`) | **REMOVED (redundancy)** — JOB 4d. All four parts are within 200px of it: the selected chip carries the date and the term label and is marked as selected; `paperLine` counts the week's assignments; the mean is in the stat line. Key and node both deleted. |
| — | — | read-only year statement | RULED ADDITION — `INSERT_AT (218, None)`, MRB-261. STAYS (past-year classes only). |
| 9 | glance grid, 3 cards, `minmax(330px,1fr)`, gap 16, padding 20 (223–276) | same geometry, **visibly shorter** | MATCHES — measured identical; see §3. |
| 10 | **card 1** — eyebrow, title, `openIn`, bar, "NOT IN YET" + chips, **Remind all N** (236) | eyebrow, title, number, bar, chips — **no Remind button** | **RESTORED** — JOB 4c. Node 236 was on `DEAD` (Design's handler toasted a send in front of no write). It is off `DEAD` and wired to `MRB_REMIND_ALL`, per paper. |
| 11 | card 1 alt — "Everyone's in — nothing to chase." (237/238) | present on an all-in class | **REMOVED (redundancy)** — JOB 5b. The card's own 34px number three lines above already reads "4 of 4 in". `glance.allIn` dropped with the node. |
| 12 | **card 2** — "RETEACH FROM THE LAST SET", title, `lastLine` ("Marked · class mean 62% · 14 submitted"), **two per-question bars** (244–251), "Open the full breakdown" | heading, title, `lastLine` as **"Marked · 14 submitted"**, bars, link | **FIXED (JOB 4b)** — the card was structurally correct and drew nothing; root cause and fix in §2. ⊕ **REMOVED (redundancy) in part**, post-review 6 Sep: "class mean X" is cut. Row 8 four inches above states the class mean, and the card's own two bars are the finer, per-question evidence the recommendation actually rests on. The submitted count STAYS — it is about this paper alone, and nothing else on the screen says it. |
| 13 | **card 3** — "KEEP AN EYE ON", watch list *or* "No one flagged…", "WORTH A SHOUTOUT", praise list, "Send a shoutout" | present | MATCHES |
| 14 | no-work empty state (277–281) + **Set work** (282) | panel present, button absent | MATCHES / button REMOVED — `DEAD`, MRB-287. ⊕ post-review 6 Sep: `klass.noWorkLine` inside it **drops its leading roster count** — "25 students are enrolled and waiting." sat directly under an eyebrow opening "25 STUDENTS", so it now reads "Everyone is enrolled and waiting. No activity yet." Design's sentence shape and her words are kept; the number is not. Node 280's own heading ("No work set for this class") is Design's and STAYS — it names the state the panel is in. |
| 15 | `<h2>` Students (284) | present | MATCHES |
| 16 | `klass.rosterLine` (285) — "28 STUDENTS · NOT SUBMITTED SHOWN FIRST" | "2 STUDENTS · NOT SUBMITTED SHOWN FIRST" | **REMOVED (redundancy) in part** — the count cut, JOB 4e. The eyebrow above the table already states it. Now reads "NOT SUBMITTED SHOWN FIRST". |
| 17 | Students table header — STUDENT / THIS WEEK / AVERAGE / LAST ACTIVE / — (287–292) | present | MATCHES |
| 18 | Students rows — avatar, name, dot + week, avg, last, "NEEDS A LOOK" (294–301) | present | MATCHES |
| 19 | `<h2>` Assignments + `klass.paperLine` (474) | present | MATCHES |
| 20 | Assignments table — Title / Status / Set / Due / Submitted / Class mean / Weakest question | present | MATCHES |
| — | — | **Shoutouts** composer + feed + delete confirm | RULED ADDITION — `INSERT_AT (208, 306)` and `(208, None)`, Mide 3 Sep 2026. STAYS. |
| — | — | four live-state panels (`#state-not-found`, `#state-not-authorised`, `#state-error`, `#compose-error`, `#shoutouts-loadmore`) | RULED ADDITION — `live_regions`, hidden until a real failure. STAYS. |

## 2. JOB 4b — why the reteach bars were empty, and the fix

**Root cause: nothing to do with `worstTwo`, `g1.stems` or the question data.
The grid was never fetched.**

`renderVals` computes `const g1 = lastP ? this.gridFor(k, lastP.idx) : null`.
`gridFor` returns **null for a grid that has not been prefetched** — its
documented contract in `METHODS` — and `load()` in `shared/teacher-live.js`
prefetched grids for **the marking screen and the insights question chart, and
for nothing else**. So on the class screen `g1` was null on every render,
`worstTwo` degraded to `[]`, and an `sc-for` over `[]` renders nothing at all.

That is why it was invisible to every gate:

* no throw, no console error, no missing `MRB_DATA` key — a *correct* render of
  an empty list;
* the three populated `class-detail` fixtures ship **twelve** grids apiece, a
  map the live page could never have, so `teacher_behaviour` drew both bars
  every time;
* `_shape_grid_absent` (`class-detail-gridmissing`) *did* hold the real
  production shape — its own comment says "`GRID: {}` … is what this screen
  ALWAYS has in production" — but it was written to reproduce the 26 Aug
  **crash**, and nobody asked what a *non*-crashing empty grid map costs.

**Fix**, in `shared/teacher-live.js` `load()`: the class screen now prefetches
**one** grid — the newest CLOSED paper somebody actually sat
(`markedIdx` narrowed by `colSub[i] > 0`), which is the same two lines
`renderVals` uses to resolve `lastP`, so the key it fetches is the key the card
asks for. A class with no such paper fetches nothing, which is also the state
in which the card correctly says "Nothing marked yet".

**Fixture**: `teacher_fixtures/class-detail-gridreteach-fixture.html`, new this
run (`_shape_grid_reteach_only`). It holds **exactly one** grid — the reteach
card's — so it is the shape production has from today, and a prefetch scoped to
the wrong paper or widened back to everything shows up here and nowhere else.
Registered in `teacher_behaviour.EMPTY_SHAPE`; it renders both bars.

## 3. JOB 4a — the card measurements

Headless Chrome, 1460px content viewport, Design's own file navigated to the
class screen (`My classes` → `7h/Sc5`) against the built fixture.

| | Design (`Teacher Dashboard v3.dc.html`) | Built fixture, BEFORE | Built fixture, AFTER |
|---|---|---|---|
| grid `gap` | 16px | 16px | 16px |
| grid `grid-template-columns` | 449.33 / 449.33 / 449.34 | identical | identical |
| card width | 449.3px | 449.3px | 449.3px |
| card height | **447.6px** | **447.6px** | **447.6px** |
| card padding | 20px | 20px | 20px |
| card radius | 12px | 12px | 12px |
| eyebrow font | 500 13px/15.6 DM Mono | identical | identical |
| title font | 600 21px/27.3 Instrument Sans | identical | identical |
| number font | 600 34px/34 Bricolage Grotesque | identical | identical |

**There is no CSS difference and no grid difference. Not one measurement
disagrees.** The cards on the LIVE page were shorter for one reason and it is
content: the reteach card drew no bars (JOB 4b), the homework card drew no
Remind button (JOB 4c), and on `8r/Sc1` the keep-an-eye card is a single
sentence. `align-items:stretch` then sizes all three to the tallest, which was
short.

**No `min-height` was added**, and that is a deliberate departure from the
brief's fallback clause — the clause is conditional ("*if* the only difference
is content-driven height, give the card grid Design's rendered height as a
min-height"), and pinning 447.6px would reserve 200px of empty paper under
"No one flagged — the class is keeping up." on every small class, which is the
opposite of what Mide asked for in the same message. Fixing the two content
defects is what actually restores Design's proportions, and it restores them
honestly.

## 4. Every cut, in one list

| Cut | Where it lived | Why |
|---|---|---|
| "Everyone has handed this week's work in." banner + "Remind all N" / "Reminded today" | `drawRemindControl`, `shared/teacher-live.js` (~120 lines, deleted) | Not Design's; sat above a card already showing the same count. JOB 4c. |
| "This week · 31/08/26 · 2 assignments set · Week mean 42%" | `weekNote`, `teacher_rulings.LOGIC` + the week-bar `INSERT_AT` node | Every part restated within 200px. JOB 4d. |
| "YEAR 8 SCIENCE" | `klass.meta` | The class code above it says both (MRB-263). JOB 4e. |
| "· 0 students to keep an eye on" | `klass.statLine` | Card 3 is that card. JOB 4e. |
| "No work set yet" (the whole line, on a class with no papers) | `klass.statLine`, no-work arm | Node 280 heads the empty state with it and the Assignments caption says "None set". Post-review, 6 Sep. |
| "25 students are enrolled and waiting." → "Everyone is enrolled and waiting." | `klass.noWorkLine` | The eyebrow one line above opens with the count. Post-review, 6 Sep. |
| "class mean 62% · " on the reteach card | `lastLine` | The header stat line says the class mean; the card's two bars carry the per-question detail. Post-review, 6 Sep. |
| "2 STUDENTS · " on the Students caption | `klass.rosterLine` | The eyebrow above the table states it. JOB 4e. |
| "Everyone's in — nothing to chase." | node 237/238 + `glance.allIn` | The card's 34px number says "4 of 4 in". JOB 5b. |
| "14 STUDENTS · SCIENCE" card eyebrow | node 182 + `cards.meta` + `BIND_ATTR[182]` | The chip below repeats the count; the code above repeats the subject. JOB 5a. |
| "Everyone in — nothing to chase" on the card | `cards.weekSub`, all-in arm only | `weekLabel` on the row above reads "2 of 2 in". JOB 5b. |
| `todayInSchoolTz()` | `shared/teacher-live.js` | Its only caller was the deleted banner. |

## 5. Where the reminder lives now

`teacher_rulings.DEAD` no longer prunes node 236. Design's dark "Remind all N"
button, under the Not-in-yet chips in the homework card, is the only reminder
control on the page.

* **the write** — `MRB_REMIND_ALL(classId, groups)`, new, beside
  `MRB_REMIND_STUDENT` in `build_teacher_port.py`. It calls the same
  `MrBadmusTeacherData.sendReminders` the deleted banner used and reimplements
  none of it.
* **who is chased** — `const kRemind` in `renderVals`: **one group per paper**
  in the selected teaching week, each holding only the children missing THAT
  paper. A week carrying two assignments therefore cannot nudge a child about
  the one they handed in. The union of the groups is exactly `kChase`, so
  "Remind all N" counts the same children the chips name.
* **"Reminded today"** — `glance.remindLabel`, after a press, keyed on class
  and week (`s.remindDone`), so stepping the week bar restores "Remind all N".
* **the honest count** — `sendReminders` upserts with `ignoreDuplicates` and
  returns the rows ACTUALLY WRITTEN. `ok` counts CHILDREN, not rows. The toast
  says one of: "Reminder sent to N students in 8r/Sc1" / "Reminded M of N — the
  rest were already reminded today" / "They have all already been reminded
  about this today" / `MRB_REMIND_WHY(error)`.
* **the rate limit** is the database's, unchanged: a unique index on
  `(student_id, assignment_id, sent_on)`, cross-teacher.

**One behaviour is not carried over, and it is named rather than hidden.** The
banner read `remindersForClass` *before* making itself pressable, so it could
show "Reminded today · 2" and disable itself, and it REMOVED ITSELF when that
read failed. Design's node has no state to remove itself with — and does not
need one, because it asserts nothing about the past. It says "Remind all 4";
the database decides what happens; the toast reports what was written. That is
the same honesty, bought with a press instead of a fetch, and it costs the
class screen one Supabase round trip less on every load.
