# Sharpen — Stages B and C (plan, 29 Sep 2026)

Planner: Fable 5.1. Builders: Opus. Binding unless a line says "builder's choice".
Site worktree `mrbadmus-worktrees/sharpen-bc` (= main `592fb4d55`); backend worktree
`mrbadmus-backend-worktrees/sharpen` (= backend main `ac03385`). Evidence: Mide's ten
screenshots of 29 Sep in `~/Desktop/MrBadmus AI/Issues/`. Stage A (pupil flashcard
sitting) is planned elsewhere and is NOT in this file.

## 0. Ground truth the builders must not re-derive

| fact | proof |
|---|---|
| Production carries every MRB-351 migration **including `mrb351_pupil_flow`** (`schema_migrations` 20260927220633/39/42 and 20260929103647, read 29 Sep). `assignments.kind`, the flashcard tables, `flashcard_reviews.answer/answer_check` all exist on prod. | `list_migrations` on `urklkrwevjtlfbwnipjn` |
| `assignment_submissions.status ∈ {in_progress, complete}` — there is **no "marked" state in the database**. "Marked" on every screen is derived (`score != null && max_score != null`, results are live). | prod `pg_constraint`: `assignment_submissions_status_chk`, `_complete_chk` |
| Pupil RLS on `assignment_submissions` (UPDATE, no status test) and `assignment_question_attempts` (own rows, all verbs) never locks a completed set. There are **zero non-internal triggers** on either table. | prod `pg_policies`, `pg_trigger` |
| `flashcard_pupil_detail` returns per card `mine`, `check`, `written_ms`, `secured`, `known`, `ratings[{rating,phase,at,think_ms,session_id}]` + `sessions[]`. It does **not** return the review-phase typed answer (`flashcard_reviews.answer`) nor a per-card shown-count. `flashcard_progress` returns per pupil `status/made/known/secured/sittings/active_ms/rushed/last_active/answers{match,partial,no,blank,pending}/completed_at`, plus `n` (deck size) and `assignment{mode,rule,…}`. | `origin/feat/mrb351-migrations:supabase/migrations/20260924180100_mrb351_flashcards_functions.sql:700-857` |
| Generated vs hand-written: `teacher/{classes,class-detail,student-detail,assignment,digest,insights}.html` are written by `build_teacher_port.py` — change `teacher_rulings.py` / `shared/teacher-live.js` / `shared/teacher-data.js`. `teacher/flashcards.html`, `decks.html`, `today.html`, `admin.html`, `timetable.html` are hand-written. `student/class.html` and `student/assignment.html` are written by `build_student_port.py` — change `student_rulings.py` / `shared/student-live.js`. | CLAUDE.md; `teacher/flashcards.html:17-20` |
| `papers` are newest-first; index 0 is the newest (`buildPapers`, teacher-live.js:707-710). `p.state === 'open'` = released and not yet due. | teacher-live.js:707-748 |
| Every change to a generated page is proved by `python3 build_all.py`, and the page's ported bytes are what ship. | CLAUDE.md |

## 1. File-conflict map and sequencing

| lane | files | conflicts with Stage A? |
|---|---|---|
| **T — teacher lane** (B1–B6, C1, C2, C4-teacher) | `shared/flashcard-progress.{js,css}`, `teacher/flashcards.html`, **new** `shared/flashcard-breakdown.js`, `shared/breakdown.{js,css}`, `shared/teacher-live.js`, `shared/teacher-data.js`, `teacher_rulings.py`, drives | **No.** Stage A touches none of these. Build in `sharpen-bc` now. |
| **P — pupil lane** (C3, C5-site, C4-pupil check) | `student_rulings.py`, `shared/student-live.js`, `shared/student-data.js` | **Yes.** Stage A edits `student_rulings.py` (flashcard overlay region) and may touch `student-live.js`. Rulings APPEND to shared lists (`LOGIC["class view"].append`, `PRUNE`, `WRAP`), so tail-of-list merges conflict even when regions differ. **Start lane P from main after Stage A lands**, or branch now and rebase before its first gate run; never merge both blind. |
| **K — backend lane** (C5-backend) | `server.js` (`openAttempt`, `/api/assignment/answer`, `/api/assignment/progress`), one test | No. Ships FIRST (additive flag; the live site never sends it). |

Build order: **T1** B1+B2 → **T2** B3 → **T3** B4 → **T4** B5 → **T5** B6 → **T6** C1 → **T7** C2 → **T8** C4 ‖ **K1** C5 backend → **P1** C3 → **P2** C5 site. One unit = one commit + push + live proof (md5 of the shipped asset), per the Autonomy Contract.

Migrations: **one file** on a new branch `feat/mrb352-migrations` (branch from main; it does not exist yet), `supabase/migrations/20260930090000_mrb352_flashcard_pupil_detail_answers.sql` + `supabase/rollbacks/…_rollback.sql`. TEST rehearsal later; prod is the chat's. It carries §B3's function change only. **Nothing else in this plan needs SQL** (C5 is SQL-free — see §C5).

---

## STAGE B — what the teacher sees about flashcards

### B1. Chips under the progress-page title

- **Cause.** `shared/flashcard-progress.js:333-338` (`renderHead`): `chips.appendChild(chip(MODE[a.mode]…))`, `chip(RULE[a.rule]…)`, `chip(d.n + " cards")`; strings at `:38-39` (`MODE = {make:"Pupils write the answers", review:"Ready-made cards"}`, `RULE = {secure:"Secure", quick:"Quick"}`).
- **Fix.** Delete lines 333-338 and the `.fp-chips`/`.fp-chip` CSS (`flashcard-progress.css:39…`). Keep `MODE`/`RULE` constants only if the CSV or the Edit sheet still reads them; otherwise delete. Hand-written page, no generator.
- **Proof.** `flashcard_progress_drive.py:488` asserts the chips (`"Pupils write the answers" in head and "Secure" in head`) — **invert** it: assert none of the three strings is in the header, and the header carries the title once.

### B2. The ANSWERS column — decision: **drop it from the table; the words go in the per-pupil panel**

- **Cause.** `answersCell()` `flashcard-progress.js:436-455` renders `✓4 ≈3 ✗1 ○2 …n` from `p.answers{match,partial,no,blank,pending}`; column key `answers` in `COLUMNS` `:142-153` (make mode only, `:156`).
- **Why drop, not reword.** (1) It is make-mode only, so the table already changes shape by mode; removing it makes the two tables the same. (2) Made / Secured / Rushed already answer "who is getting on" at a glance; the verdict split is diagnostic — it says *what* went wrong for one child, which is the panel's job. (3) A four-part phrase per row is the "second sentence" pattern (CLAUDE.md, no redundant text) and the table already fights for width at 390 (the drive asserts no page scroll at 360/390). (4) The CSV "as displayed" loses nothing a teacher acts on from a spreadsheet.
- **Fix.** Remove the `answers` column from `COLUMNS`, `renderTable`, the sort table and the CSV. In the B3 panel, ONE line under the tiles, only in make mode and only when `answers` has any count: `"4 right · 3 nearly · 1 wrong · 2 blank"` (+ `" · 1 checking"` when `pending > 0`; omit zero buckets; singular never needed because the noun is absent). Source: `flashcard_progress.pupils[i].answers` — already loaded for the table; pass the pupil row into the panel.
- **Proof.** `flashcard_progress_drive.py:530-533` (`.fp-ans-pending` "…2") → replace with: the table has no `Answers` header in either mode; the panel line for `p-cat` reads exactly the words above; CSV header list has no `Answers`.

### B3. Per-pupil sheet → the centred wide panel with ‹ prev / next ›

- **Cause.** `openDrawer()`/`renderDetail()` `flashcard-progress.js:603-722` render into the right-hand `<aside class="fp-drawer">` (`teacher/flashcards.html:109-120`; CSS `flashcard-progress.css:197-284`, 560px, `z-index 70`). No pupil navigation. Per card it draws "Their answer"/"Model answer" side by side, a Match/… chip + `written_ms`, then rating chips grouped `while writing` / `in review` (`:676-700`), then a "Sittings" list.
- **Fix — new `shared/flashcard-breakdown.js` + reuse `shared/breakdown.css`.** Same shell markup and classes as `shared/breakdown.js` (`.bd-overlay` fixed on `<body>`, `.bd-sheet` 880px, `.bd-head` with eyebrow/title/subtitle/prev/next/close, focus at open only, `documentElement.overflow=hidden` while open, session counter for stale loads — copy `buildShell()` `breakdown.js:~460-520` structurally; do not import breakdown.js's MCQ loaders). Surface: `window.MRBFlashcardBreakdown.open({assignmentId, studentId, classId, progress?})`.
  - Roster and order: `flashcard_progress(assignmentId)` → `pupils[]` (surname order, same as the table). Per pupil: `flashcard_pupil_detail(assignmentId, pupilId)`; cache per session; prefetch neighbours (builder's choice).
  - Header: eyebrow = deck title; title = pupil name; **subtitle empty** (C2 rule: no "Pupil N of M", no due line); ‹ prev name / next name › as breakdown.js draws them (`.bd-nav-word`). The status chip (Done · on time / Done · late / In progress / Not started / Missing) sits at the right of the title row, once.
  - Three tiles (mirrors 09.27.01 so Design can redesign both together): **SECURED** `6 / 10` with small line `made 8 / 10` in make mode only; **TIME** total active (`sum sessions.active_ms`, `clock()`), small line `3 sittings` (+ ` · rushed` when `p.rushed`); **HANDED IN** `On time` / `Late` / `Not yet`, small line `Handed in 28 Sep 2026 at 20:45` when `completed_at`.
  - B2's verdict line under the tiles (make mode only).
  - Filter: `All 10` · `Not secured 4` (the `.bd-filter` twin of All/Wrong).
  - **Per card**, one `<li>`: line 1 = `Q3` + question (formulae via `sci()`), and **one** state chip at the right of the question line: `Secured` / `Got it` / `Nearly` / `Not yet` / `Not seen`. State = `secured ? Secured : lastRating(got_it→Got it, nearly→Nearly, not_yet→Not yet) : Not seen` where `lastRating` is the latest `ratings[]` entry by `at`. Line 2 = **their latest written answer** with its verdict chip (`Right` / `Nearly` / `Wrong` / `Blank` / `Checking` — reuse `CHECK` map words, verdict CSS from `.fp-check-*`). Line 3 = model answer (label "Model answer"). Line 4 = `Tries: 3`. Then `History ▸` disclosure (`<details>`, closed by default) holding what the drawer showed today: phase-grouped rating chips with times (`while writing` / `in review`, `:676-700` logic moved verbatim) and, once per panel, the Sittings list (move it into a page-level `History` details under the cards, not per card). **No label text that repeats a chip**: no "THEIR ANSWER" caption when the verdict chip is beside the text — use a muted `You wrote` prefix? No: the answer sits in a bordered box with the verdict chip; the model answer box carries the one label.
  - **Latest written answer — data.** Make mode: `c.mine` / `c.check` (the writing pass; `flashcard_pupil_cards` is immutable on first write, so it IS the only written answer). Review mode: the typed answer lives on `flashcard_reviews.answer/answer_check` (prod has `pupil_flow`) but the RPC does not return it. **The one migration** (`feat/mrb352-migrations`): `create or replace function public.flashcard_pupil_detail` identical to today's body except each `ratings[]` entry also carries `'answer', rv.answer, 'answer_check', rv.answer_check`, and each card carries `'shown', (select count(*) from flashcard_events e where e.assignment_id=p_assignment and e.pupil_id=p_pupil and e.card_id=af.id and e.type='card_shown')::int`. Rollback = today's body verbatim (copy from `20260924180100…:814-857`). Additive keys only; nothing else reads them.
  - **Degrade (binding).** `latest = last ratings[] entry with a non-null answer` → text + `answer_check`; else `c.mine`/`c.check`; else the box reads `No written answer` (one line, muted). `Tries` = `c.shown` when the key is present, else `ratings.length`. State in the code comment that Tries counts rated passes until the migration lands.
  - `teacher/flashcards.html`: drop the drawer markup (`:109-120`) and its CSS; include `/shared/breakdown.css` and `/shared/flashcard-breakdown.js` (after `formulae.js`); row click → `MRBFlashcardBreakdown.open`. The 10-second poll must not repaint an open panel.
  - Phone (≤560): breakdown.css already stacks; verify at 390/360 like `teacher_reach` does (this page has no fixture — extend `flashcard_progress_drive` with the 390 pass it already runs).
- **Proof.** `flashcard_progress_drive.py:550-596` (drawer assertions incl. `d["rateRow"] == ["[while writing]", …]` `:588`, sittings `:595`) → rewrite against the panel: opens as `[data-bd="overlay"]`-style shell, prev/next walk the roster in table order and disable at the ends, per card {question, latest answer, verdict, model answer, `Tries: N`, exactly one state chip}, `History` closed by default and its rating chips present when opened, verdict words line (B2), no `Pupil N of M`, no `while writing` text visible while History is closed. Fixture (`:110-138`): add `answer`/`answer_check` on one review rating and `shown` on one card, and a second fixture pupil WITHOUT them, so both degrade branches are driven. `theme_wiring_check` / `contrast_audit` cover the new CSS (breakdown.css is already themed).

### B4. Student-detail: flashcard rows say Not started while the pupil has 8 sittings

- **Cause.** The history rows read the MCQ matrix only: `stRow.status[i]` / `sc` / `hasRow` in the status ruling `teacher_rulings.py:9571-9583` (`Complete · late / Complete / In progress / Scheduled / Missing / Not started`), and `cellOf()` `teacher-live.js:1115-1160` only ever sees `assignment_submissions`. A deck writes **no submission row until it is complete** (LANDING §1), so every sitting is invisible: `hasRow` false → `Not started`. The only flashcard read on the page is `pack.flashcardLastActive[sid]` (`teacher-data.js:2491-2500`), a per-pupil MAX, not per deck.
- **Fix — one RPC per deck paper, on the two screens that show per-pupil cells.** In `teacher-data.js` `loadClassMatrices` (the class-in-focus branch, where `pack.submissions` is loaded ~`:1119`): for every assignment with `kind === 'flashcards'` (present in `pack.assignments`; derive from `quiz_type==='flashcards'` exactly as the estate does) call `sb.rpc('flashcard_progress', {p_assignment: id})` in parallel (`Promise.all`, tolerate per-call failure → `null`). Store `pack.flashcards = { [assignmentId]: { n, pupils: {[pupilId]: {status, secured, sittings, made}} } }`. In `buildMatrix` (`teacher-live.js:1058`) add per-row arrays `fcStatus[p]`, `fcSecured[p]`, `fcN[p]` filled from `pack.flashcards`, and let a deck with `status in (in_progress)` set `startedInWeek` when the paper is in-week (so B5's THIS WEEK chip says In progress, not Not started). `matrixFromRollup` (classes/digest/insights) unchanged — it draws no per-paper cells.
  - Status ruling (`teacher_rulings.py:9571-9583`): for a deck paper (`p.kind === 'flashcards'`): `Complete` / `Complete · late` from the submission cell exactly as now; else `fcStatus === 'in_progress'` → `In progress`; else deadline passed → `Missing`; else `Not started`. (Mide's three: Not started → In progress → Complete; Missing kept because MCQ rows already use it for a closed paper with nothing in.)
  - Score cell: deck → `fcSecured + "/" + fcN + " secured"` when `sittings > 0` (e.g. `6/10 secured`), `—` otherwise. Never a percent.
  - Links: **Breakdown** on every deck row with `sittings > 0` → `openBreakdown` branches on kind: `window.MRBFlashcardBreakdown.open({assignmentId: p.id, studentId: st.id, classId: k.id})` (ruling at `teacher_rulings.py:9250-9266`; add `flashcard-breakdown.js` + `breakdown.css` to the student-detail and class-detail script lists in `build_teacher_port.py`, same guard shape as `MRBBreakdown`). **Add feedback**: feedback binds to `assignment_submissions.id` (`fbSub`, `:9224-9229`); a deck has one only once complete → the control appears on Complete rows exactly as for MCQ, and is absent before. No fake row.
- **Data cost.** One `flashcard_progress` call per deck of the class in focus (runs `flashcard_card_state` per pupil — fine for a class of 30 and a handful of decks). Not on Today / classes / digest / insights.
- **Proof.** `flashcard_progress_drive` already runs `buildPapers/buildMatrix/buildRoster` with a stubbed client (`gate_registry.py:454-487`): add a deck paper with a sitting-only pupil and a done pupil → assert `fcStatus`, the row words `In progress` / `Complete`, score `6/10 secured`, Breakdown present, Add feedback absent until complete. `teacher_fixtures/student-detail-fixture*.html` (drives `teacher_behaviour`, `teacher_reach`): add one deck row so the new keys render; `teacher_tells` stays green (no invented counts).

### B5. Class page Students table: THIS WEEK SCORE column

- **Cause.** THIS WEEK is a per-pupil tally over the in-week papers (`week:` ruling `teacher_rulings.py:6832-6848` / `7144-7160`: `Nothing set / Not started / In progress / Missing / N of M in / In · on time|late`); AVERAGE is `mx.studentAvg` = sum(score)/sum(max) over released graded cells (`teacher-live.js:1326-1352`). Nothing shows what the pupil scored on this week's set.
- **Fix.** New column **THIS WEEK SCORE** between THIS WEEK and AVERAGE (Design's grid `1.7fr 1.3fr 110px 160px 160px`, header node at Design `Teacher Dashboard.dc.html:443`, row `:451`; find the compiled node ids the way 311/320 were found and `BIND_ATTR` both — see C1 for the final track list). Cell = one line per **in-week paper** (`mx.inWeekPaper`, newest first, at most 2): MCQ `7/10` (from `scores[p]/max[p]`), deck `6/10 secured` (B4's `fcSecured/fcN`, only when `sittings > 0`), `—` when nothing is in for that paper. One in-week paper → one line. Header string `THIS WEEK SCORE`. THIS WEEK keeps its chip as-is (`1 of 2 in` is the status; Mide: keep it in the chip, no second sentence).
  - Ruling mechanism: a `RULED_ADDITIONS`-style header cell + row cell inserted with `INSERT_AT` after the THIS WEEK cells (precedent `teacher_rulings.py:380-399` shoutout surface; column widening precedent `:1932-1939`), value from a new roster key `weekScore` in the `roster` builder (`teacher-live.js:1377-1472`, add `weekScores: [{label}]`).
  - Phone: the `≤420px` rule stacks every grid to one column (`build_teacher_port.py` `[data-port-region] [style*=grid-template-columns]`); the new cell must carry its own small header word like the others do at that width — copy whatever the AVERAGE cell does.
- **Proof.** `flashcard_progress_drive`'s roster probe: pupil with a 7/10 MCQ and a 6/10 deck this week → `weekScores` = `["7/10","6/10 secured"]`; not-started pupil → `["—"]`. `teacher_fixtures/class-detail-fixture*.html`: add the column so `teacher_behaviour`/`teacher_reach` see it at 1460/390/360; `teacher_picker_drive` unaffected.

### B6. My classes cards count LAST week's set

- **Cause (grounded).** The card's `week: [inWeekN, n]` (`buildClassEntry`, `teacher-live.js:2399-2415`) counts pupils with `inWeek`, and `inWeek` is "a complete cell on ANY in-week paper" where in-week = `state==='open' OR due_at in the week window` (`buildMatrix:1082-1087`; SQL twin `teacher_class_rollup_v2` `in_week`, rollup_v2.sql:418-432). On Tuesday 29 Sep the Monday-anchored window is Mon 28 Sep → Mon 5 Oct (`computeWeekWindow`, `teacher-data.js:236-278`), so a paper due **Mon 28 Sep 09:00** (Changes of State) is in-week by due date alongside the open 5 Oct paper, and 7 pupils who did last week's set count as "in". (The class page's roster used the same rule; its "Not started" rows come from the class's own `assignment_day_of_week` anchor shifting the window — the two pages' windows differ per class, which is a second reason the card and the table disagree.)
- **Fix — define the CURRENT SET once and use it on both pages.** `teacher-live.js`: `function currentSet(papers) { return papers.find(p => p.state === 'open') || null; }` (papers are newest-first, so the first open one is the newest open). Card (`buildClassEntry`): `week = cur ? [mx.colSub[cur.idx], mx.colAsked[cur.idx]] : null` — the same numerator/denominator the Assignments table's SUBMITTED cell uses (`decoratePapers`, `:1368`), so the card and the table always agree. Chase names: pupils on the roster with no complete cell on `cur` — on the class-in-focus path from `byId[sid].submitted[cur.idx]`; on the rollup path (classes page) from **one** extra read in `teacher-data.js` `loadClassMatrices`' rollup branch: `assignment_submissions?select=assignment_id,student_id&assignment_id=in.(<current set ids of all classes>)&status=eq.complete&deleted_at=is.null` (single request, chunked like the rollup), degrade → names omitted, count from `colSub`. No open set → the card's homework line reads `no work open` (state `nowork` visuals + Set work link) and LAST ACTIVITY stays. Label stays `HOMEWORK THIS WEEK`.
  - The class page's glance `openIn` (`kMx.colSub[0] + ' of ' + k.n + ' in'`, ruling around `teacher_rulings.py:6998`) → use `currentSet` too, so "1 of 17" is the same number on the card and the class header.
  - `roster[].inWeek`, `onTimeWeek`, the Today chase list and the SQL rollup are **untouched** (Mide's 23 Sep ruling still governs "this week's homework" for those).
- **Proof.** `flashcard_progress_drive`'s `buildClassEntry`/`buildMatrix` run: two papers, one due Mon 09:00 with 7 complete cells, one open with 1 → card `week == [1, 17]`, chase list has 16 names, glance `openIn == "1 of 17 in"`; no open paper → `week == null`. `teacher_rollup_equal` is unaffected (it compares the rollup's own fields, not the card). Live proof after push: 10h/Ph1's card and header both say the same number.

---

## STAGE C

### C1. Teacher tables: one baseline, no drift

- **Cause.** Every teacher table is a CSS grid **per row** (no `<table>`), header and rows each their own grid with identical `grid-template-columns` (Assignments `2fr 100px 1fr 1fr 1fr 1fr 1.2fr auto` — the `auto` eighth track added by `BIND_ATTR` 311/320, `teacher_rulings.py:1848-1864`; Students `1.7fr 1.3fr 110px 160px 160px`, Design `:443/:451`; Submission history `2.3fr 1fr 1.1fr 100px 1.05fr`, Design `:538/:546`). A bare `1fr` is `minmax(auto,1fr)` and `auto` sizes to its own row's content, so a row with three action buttons (Edit · Download · Delete) or a long weakest-question cell gets different track widths from its neighbour and every cell slides (11.18.33: the two OPEN pills are 30px apart; the SCORE cell wraps `5/10 ·` / `50%` at 100px in 12.21.19). The Students table has no `auto` track and short cells, which is why it reads aligned.
- **Rule (binding, all teacher tables).** Every track is either a fixed `px` or `minmax(0, Nfr)`; never `auto`, never bare `fr`. Only the title cell may wrap (`min-width:0`); every other cell `white-space:nowrap; overflow:hidden; text-overflow:ellipsis`. Header and row tracks are byte-identical (assert with `BIND_ATTR`, as 311/320 do).
  - Assignments (class-detail; also the same table on assignment/digest if drawn): `minmax(0,2fr) 96px minmax(0,1fr) minmax(0,1fr) 88px 96px minmax(0,1.2fr) 200px` — the last track fits `Edit Download Delete` at Design's button size (builder measures; fixed, right-aligned).
  - Students (class-detail): `minmax(0,1.7fr) minmax(0,1.3fr) 120px 110px 160px 160px` (B5's column is the 120px).
  - Submission history (student-detail): `minmax(0,2.3fr) minmax(0,1fr) minmax(0,1.1fr) 120px minmax(0,1.05fr)` (SCORE no longer wraps).
  - Marking grid on `teacher/assignment.html` and any other row-grid Design drew: same treatment where a bare `fr`/`auto` exists (builder greps the compiled template for `grid-template-columns` and lists what it changed).
  - `teacher/flashcards.html` `<table class="fp-table">` and `teacher/decks.html`: `table-layout: fixed` + a `<colgroup>`; text cells nowrap/ellipsis; title column wraps. Hand-written — edit directly.
- **Proof.** New fast gate assertion in `teacher_tells.py` (it reads the built bytes): every `grid-template-columns` inside a `[data-port-region]` table on the six pages contains no `auto` and no bare `fr` token; header/row pairs identical. `teacher_behaviour`/`teacher_reach` re-run (fixtures); `flashcard_progress_drive` asserts `table-layout: fixed` on `.fp-table`. Screenshot pair 1440 before/after into `$MRB_SHOTS/sharpen/`.

### C2. Pupil breakdown panel: drop "Pupil N of M · Due …"

- **Cause.** `shared/breakdown.js:1039-1044` `renderHeader`: `posLabel = "Pupil " + (S.idx+1) + " of " + S.roster.length; els.subtitle.textContent = posLabel + " · " + (due ? "Due " + fmtDateTime(due) : "No due date set")`.
- **Fix.** `els.subtitle.textContent = ""` and hide the subtitle element (keep the node so the shell shape is stable for Design's redesign). Keep `announcePupil` (`:1053`, aria-live, not visible). Nothing else in the panel changes.
- **Proof.** No gate asserts the subtitle (grep'd); add one line to `teacher_behaviour.py`'s breakdown snapshot (`:439-451`): `.bd-subtitle` text is empty after open.

### C3. Pupil class page: term spine → one week `<select>`

- **Cause.** Design's spine is node 107 (`data-port-region="term-spine"`, `student_rulings.py:3483`), Design `Class View.dc.html:170-215`: legend + 12 week buttons (`weeks` built in `renderVals` `:777-790`, `pickWeek(n)` toggles `state.week` `:723`, list filter `if (st.week != null) list = list.filter(w => w.week === st.week)` `:806`). It draws 12 fixed weeks (`for n = 1..12`) although `w.week` is `academic_week` (1–39, `student-live.js:2480-2481`, `:2649`) — from week 13 the spine cannot show a pupil's work at all. "TAP A WEEK TO FILTER" (node 114) is already pruned (`student_rulings.py:6405`).
- **Fix (port only; Design's file untouched).**
  - `PRUNE["class view"].append(107)` (whole spine section). Remove the now-dead node-114 prune (`:6405`) and the spine theme entries in `student_themes.py:24,161,173` that point at nodes 118/129/133.
  - `INSERT_AT["class view"]` a compact control into the work-list header row beside the All / To do / Marked tabs (the row Design draws at the top of the work list): `<select aria-label="Week" onChange="{{ pickWeekSelect }}">` with options from a new render key `weekOptions` = `[{value:'', label:'All weeks'}, …{value:n, label:'Week ' + n + suffix, selected}]` where the set of `n` is the distinct `w.week` values in `all` ∪ `currentWeek`, ascending; suffix = `' · this week'` for `currentWeek`, `' · missed'` if that week holds a missed item, else nothing (this is the spine's stack state, now words). LOGIC: `pickWeekSelect = (e) => this.setState({ week: e.target.value === '' ? null : Number(e.target.value) })` (precedent: teacher recipient `<select>`, `teacher_rulings.py:~1866`). Initial state: `week: (MRB_DATA('currentWeek') != null && all.some(w => w.week === MRB_DATA('currentWeek'))) ? MRB_DATA('currentWeek') : null` — **default this week when this week has work, else All weeks** (a pupil with only last week's marked set must not open onto an empty list). `SHOW ALL 12 WEEKS` / `clearWeek` go with the spine. Filter line `:806` unchanged.
  - Style: reuse the tabs' chip look (font `var(--st-mono)` 10px uppercase like the tab labels, `border:1px solid var(--st-rule)`, `border-radius:var(--st-r-chip)`, `min-height:40px`, bench-theme aware via existing tokens); no new colour. Phone: the select sits after the tabs in the same flex row and wraps under them at 360.
  - Do NOT touch the KS3 lesson pages or anything under `docs/ks3/design-reference/`.
- **Proof.** `student_behaviour.py:122` ("a week bar filters the spine", click "03") → re-aim: choose option `3` in the select → the list holds only week-3 rows; choose `All weeks` → full list; default option on load equals `this week` when the fixture has work in it. `student_page_drive.py:419-429` (NOW-dot probe via `currentWeek`) → assert the selected option is `currentWeek`. `student_behaviour.py:649` (TAP A WEEK absent) stays. **`student_parity.py:155-156` is NOT touched** — it drives the PREVIEW of Design's own file, not the port (CLAUDE.md), so the spine expectation there stays true. `student_themes` re-run (the ring/dot colour checks are removed with the nodes). Fixture `shared/student-fixture-class.js` gains `currentWeek` if it lacks one.

### C4. Top bar never repeats the h1

- **Cause.** Design's teacher bar crumb is node 17 (`.mrb-crumb`, `teacher_rulings.py:1622-1630`), bound to `{{ crumb }}` (Design `Teacher Dashboard.dc.html:44`, `text-transform:uppercase` mono) with `crumb: k.code` (`:1844`) — the class code — so on class-detail the bar says `10H/PH1` over an h1 `10h/Ph1`. On `classes.html` it reads `My classes` (ruling comment `:4204-4211`) over the same h1.
- **Fix (rule: the bar carries the PARENT as a `‹` link; nothing when the page has no parent or the h1 says it).** Per screen, by ruling on the `crumb`/node 17 binding (make the node an `<a>` with `href` when it is a link; keep `.mrb-crumb` so the phone-bar rules still apply):
  - classes → **empty** (h1 is My classes); class-detail → `‹ My classes` → `/teacher/classes.html`; student-detail → `‹ <class code>` → class-detail; assignment (teacher) → `‹ <class code>` → class-detail; digest, insights → `‹ My classes`; today/admin/timetable/decks/flashcards/seating (hand-written, `<!--mrb:topbar…-->`/their own bar): decks → `‹ My classes`, flashcards (one deck's progress) → `‹ <class code>` → class-detail, today/admin/timetable → empty. The uppercase transform stays for codes (`10H/PH1` is Design's crumb style; the h1 no longer sits under the same text so it is not a repeat — builder's choice to drop `text-transform` for the `‹ My classes` case).
  - Pupil pages (check only, from CUTS.md "The header" table and `topbar.py:14-21`): class page has no bar (Design header); assignment bar = `‹ <class>` (parent, h1 is the set title) ✓; leaderboard/classes/settings/claim-confirm carry no title ✓; KS3 lesson = `‹ unit` ✓. Nothing to change; the builder screenshots each once at 390 to confirm.
- **Proof.** `teacher_tells.py`: on each built teacher page the bar's crumb text ≠ the page's h1 text (case-insensitive), and on classes/today/admin/timetable it is empty. `today_drive` 5b (one-row bar) re-run; `teacher_reach` for the new anchor's reachability.

### C5. Pupils can always reopen their homework — architecture

**Where the lock is (grounded).** Exactly one place: `openAttempt()` `server.js:8167-8193` — `if (latest && !retake) return { closed: true }` when the latest attempt is `complete`; `/api/assignment/answer` `:8304-8312` turns that into `409 attempt_already_complete`. Not RLS (§0), not a constraint (§0), not a trigger (§0), not the page (it simply stops sending: `student-live.js:1976-1977`, and `locked = pick != null || handed` in Design's option logic `Assignment - standalone source.dc.html:956`). Score is `rescore()` `:8230-8244` = markable correct / markable answered, written to `assignment_submissions.score/max_score` **in place** with `updated_at = now`. Late is decided once at `/complete` `:8409-8420`. The teacher reads the same row (`buildMatrix` cellOf; rollup SQL; breakdown.js `loadSubmissions` `:294`).

**Decision: revise the SAME attempt in place. No new attempt, no status change, no SQL.**

- **K1 — backend** (`server.js`, ship first):
  1. `openAttempt(assignmentId, studentId, retake, revise)`: when `latest.status === 'complete'` and `revise` is true, `return { submission: latest, revised: true }`. `retake` semantics unchanged (a new attempt); `revise` wins if both are sent. Without either flag the 409 stays — old clients see no change.
  2. `/api/assignment/answer` reads `revise` from the body, passes it through, upserts the attempt row as now, `rescore()` as now (this is what makes the teacher's score "the latest": it is the same row). Response adds `status: sub.status` (`'complete'` on a revision) and `revised: !!opened.revised`. **Never** touch `completed_at`, `submitted_at`, `is_late`, `attempt_no`, `total_time_seconds`.
  3. `/api/assignment/progress` adds `revised: !!(current && current.status === 'complete' && current.updated_at > (current.completed_at || current.submitted_at))` — add `updated_at` to `SUBMISSION_COLS` `:8133`.
  4. `/api/assignment/complete` unchanged (idempotent; a revised set is already complete).
  5. Test: `test_assignment_revise.js` in the style of the existing pure tests is not possible (the routes hit Supabase) — instead extend the TEST drive `student_api_drive.py` (site repo): answer → complete → answer with `revise:true` → 200, same `attempt_no`, `status:'complete'`, score changed, `completed_at`/`is_late` unchanged, `progress.revised === true`; answer without the flag → still 409. Also the legacy `/api/assignment-submit` `:659-720` is left alone (its drive `student_submit_drive.py:132-137` still expects the 409 → `retake`).
- **The "revised after marking" marker — SQL-free and honest.** `revised = status==='complete' && updated_at > (completed_at || submitted_at)`. Why honest: the only writers of `assignment_submissions` are `server.js:711` (legacy complete, `updated_at = now = completed_at`), `:8175` (insert), `:8240` (`rescore`, the only post-completion writer, and only via a revision), `:8423` (complete, same `now` for both stamps); no site script writes the table as a teacher (grep'd `teacher-data.js`, `teacher-live.js`, `breakdown.js`, `set-work.js`); zero triggers on prod; feedback lives on `submission_feedback`. **Builder pre-flight (read-only, prod):** `select count(*) from assignment_submissions where status='complete' and updated_at > coalesce(completed_at, submitted_at) + interval '2 seconds' and deleted_at is null` — expected 0; if not 0, report the count and the rows' dates before shipping (a non-zero count means history would wrongly read "revised", and the fallback is the parked-migration column `revised_at`, NOT shipping the predicate).
- **P2 — pupil site** (`student_rulings.py` assignment LOGIC + `student-live.js`; after Stage A lands):
  1. Sending: `saveAnswer`'s payload (`student-live.js:~2004` `post("/api/assignment/answer"…)`) carries `revise: true` whenever the page state is `handed`. On the response, update `answers[idx]`, `score`/`max_score` in state so the results header re-renders; keep `view` as it was.
  2. Options: Design's `locked = pick != null || handed` (`:956`) → `locked = pick != null && st.revising !== idx`. A handed set no longer locks; a picked question shows right/wrong/answer marking as now and unlocks only via **one** button on the question card, label `Change my answer` (shown when `handed && pick != null && st.revising !== idx`), which sets `revising: idx`. Confirm sends, then `revising: null`. Unanswered questions on a handed set are simply answerable (`pick == null`). `showNextQuiet`/`showNext` rules keep the Stage-B fix (no unsaved skip while a pick is pending).
  3. Done view: `wrongList` (`:1061-1066`, node list at `:482`) → every question, in order, each row: number, stem, one mark (✓ / ✗ / `—` not answered), link `Look at it ›` (answered) or `Answer it ›` (unanswered) → `go(i)`. `wrongCount` line becomes `N of M right` only if it is not already the header's fraction (it is — the results header shows the score; so drop the count line: no redundant text). `noneWrong` copy stays for a full score.
  4. `revised` from `/progress`: the results header gets one small mono line `REVISED AFTER MARKING` (pupil side; keeps the pupil honest about what the teacher sees). Builder's choice to omit if the header already carries a second fact — but the teacher-side note (below) is not optional.
  5. Bench + work rows (class page, `student_rulings.py:2141` `primaryLabel` and the done-bench primary in `student-live.js:4480-4544`): for a completed set the one button is `Finish it` when `answered < total`, else `See your answers`; both → `assignmentHrefFor(id)` (`:881`). `Open the lesson`, `Read the feedback`, `Revisit this week's lessons` and `Close` leave these two places (the results page shows the feedback, `student-live.js:5087-5113`; lessons stay in the Lessons panel). `Retake it` (`w.retake`) is untouched. **Data for `answered < total`:** `shared/student-data.js` card build (`:450-457`, `:710`): add `assignment_questions(count)` to the `assignments` select (pupils may read it — prod policy `assignment_questions_select_merged` admits class members once released) and one read `assignment_question_attempts?select=submission_id&submission_id=in.(<own complete ids>)`; degrade on any error → `See your answers`. Practice rounds and decks (`kind==='flashcards'`, redirected to the class page) untouched.
  6. `RULED_DIVERGENCE` entries for the new labels (precedent: `Complete homework`), so `student_behaviour`'s fixture keeps Design's words.
- **Teacher side** (`teacher-data.js` q4 select `:1119` + `breakdown.js` `loadSubmissions` `:294`: add `updated_at`): student-detail history row → a small second line in the SCORE cell, exactly `revised after marking`, when the predicate holds (`teacher_rulings.py:9224-9299` row keys, add `revised`); breakdown panel → the HANDED IN tile's small line becomes `Handed in 28 Sep 2026 at 20:45 · revised 29 Sep at 21:10` (`updated_at` formatted by `fmtDateTime`). The class mean, `pickFirstAttempts` and the rollup need nothing: same row, same score column.
- **Proof.** `student_api_drive.py` (above); `student_behaviour` (done view lists every question; `Change my answer` appears once per answered card on a handed set; bench labels via divergence entries); `student_controls_drive` presses `Change my answer` and `Answer it ›` (credentialed, skipped by name here; note it); `flashcard_progress_drive`'s `buildMatrix` run gets a revised row (`updated_at > completed_at`) → `revised` true, and an untouched row → false; `teacher_behaviour` fixture with one revised row. Deploy: backend → Render `/api/health` build = new sha → site.

### C6. Tighten candidates seen while reading (for the Fable auditor; not built here)

1. `teacher/assignment.html`: `‹ Back to 8r/Sc1` under the bar AND (after C4) the bar's `‹ 8r/Sc1` — one goes. The crumb line `8R/SC1 · OPEN · SET MON 28 SEP 18:21 · DUE MON 5 OCT` repeats the h1's class, the status pill and the two tiles below.
2. Assignments table: `Flashcards · 10 cards` under a deck title + an empty CLASS MEAN `—` + an empty WEAKEST QUESTION cell — three cells saying "this is not a quiz".
3. Class-detail tile `SUBMITTED 2/2 · Still open` and the Assignments row `2/2 · OPEN` for the same set.
4. Breakdown panel (09.27.01): the `Temperature changes shc` group heading + `5 of 5 right` repeats the SCORE tile when a set has one subtopic.
5. My classes card: `LAST ACTIVITY JUST NOW` on a card that also says `2 of 2 in` — fine; but `NO ACTIVITY YET` + `no work set` on the same card is two ways of saying empty.
6. Student-detail SCORE `5/10 · 50%` — the percent is the fraction again (Mide cut the same pair on the pupil results page).
7. Pupil class page: `Recall` rail card's `Questions from the lessons this class has covered. Six a round, unlimited rounds.` — platform self-explanation (KS3 copy rule §8.10).

## For Mide (not science; product)

- **Tries** counts rated passes until the parked migration lands; after it, exact shown-count. Say if "Tries" should mean something else.
- C5: `Open the lesson` / `Read the feedback` leave the done bench and the marked work row in favour of the one button. Veto if you want the lesson link back on the row.
- B6: a class with work set but nothing open now reads `no work open` on its card.
- C3: default week = this week only when this week has work, else All weeks.

No science or content question arises in B or C.

---

## As built — lane T (teacher), 29 Sep 2026

Builder: Opus 5.5, worktree `sharpen-bc`. Stage B is one commit (B1–B6), Stage C
teacher one commit on top (C1, C2, C4).

### Stage B

- **B1** chips gone (state chip too — "Opens …" in the meta line and the due date
  already say it); `MODE`/`RULE`/`CHECK`/`RATING` and `.fp-chip*` deleted.
- **B2** Answers column gone from table, sort and CSV; the verdict words are one
  line under the panel's tiles (make mode, only when any count > 0).
- **B3** `shared/flashcard-breakdown.js` (+ `.fb-*` section in `breakdown.css`);
  drawer markup and CSS deleted from `teacher/flashcards.html` /
  `flashcard-progress.css`. Migration on `feat/mrb352-migrations` (see below).
- **B4** `pack.flashcards` (one `flashcard_progress` per released deck, focused
  class only, `opts.flashcardProgress`), `fcStatus/fcSecured/fcN/fcSittings` on
  every matrix row, three `LOGIC` rulings + the Breakdown gate `h.bdCan`, a new
  `student-detail-deck` fixture.
- **B5** `INSERT_AT[(287,289)]`/`[(294,298)]`, `BIND_ATTR[287]`/`[294]`,
  `weekScoreLines` / `MRB_WEEK_SCORE`.
- **B6** `currentSet()`, `entry.cardWeek` / `cardChase` / `currentSetId`,
  `TD.loadCompleteFor` (the one extra read on the rolled-up path), five `LOGIC`
  rulings on the card.

### Migration (B3) — parked branch `feat/mrb352-migrations`

- `supabase/migrations/20260930090000_mrb352_flashcard_pupil_detail_answers.sql`
  (file md5 `fadcd122b82d37940857cf5120429b45`, function prosrc md5
  `ad73dae2421adff5cdc85eb08646f295`)
- `supabase/rollbacks/20260930090000_mrb352_flashcard_pupil_detail_answers_rollback.sql`
  (file md5 `488b6a36685f9ed82fbab1cfbbcc9fef`, restores prosrc md5
  `167c4c0e36f0e504c3da6bc32dd11f6b`)
- Before: TEST and production `flashcard_pupil_detail` identical
  (`pg_get_functiondef` md5 `b3b67d61b644ce5b74d851c5e8eae1fd`, read-only on prod).
- TEST rehearsal: apply → `ad73dae2…` · rollback → `167c4c0e…` and def md5 back to
  `b3b67d61…` · apply → `ad73dae2…`, left applied. ACL unchanged throughout.
  Applied with `execute_sql` (not `apply_migration`), so TEST records no
  `schema_migrations` row for it.

### Deviations

- Deviation: B1 said delete `:333-338`, which includes the Scheduled/Open/Closed chip, while the proof named only the three content chips → removed all four → the due line and the "Opens …" meta already carry the state, and a lone state chip would be the only chip left.
- Deviation: B3 status chip words `Done · on time` / `Done · late` → the chip says `Done` and the HANDED IN tile says On time / Late → the plan's two strings would say "on time" twice in one header (no-redundant-text rule).
- Deviation: B3 prev/next "surname order, same as the table" — the table is least-progress-first by default → on flashcards.html the panel walks the table's CURRENT sort order (passed as `order`); from the student screen it walks the RPC's surname order.
- Deviation: B3 success-green tints use `color-mix(in srgb, var(--success) 14%, transparent)` (fallback `--st-num-well`) instead of `--success-soft` → `--success-soft` resolves to a pale light-mode tint under dark and put bright dark-mode green on a pale chip (seen in the dark screenshot).
- Deviation: B4 "add flashcard-breakdown.js to the student-detail AND class-detail script lists" → added to student-detail only (the page with the `breakdown` flag), with `formulae.js` → nothing on class-detail opens the panel (a deck row there navigates to flashcards.html).
- Deviation: B4 read is gated by an explicit `opts.flashcardProgress` (set in `base()` when `submissionsFor` is a non-empty list, and in `mergeForeignClass`) rather than inferred inside `loadClassMatrices` → the rollup fallback also narrows `submissionsFor` and must not fire it on My classes.
- Deviation: B4 fixture — a new `student-detail-deck` fixture variant (`_shape_deck`) rather than editing the populated fixture → the populated fixture's rows feed every other student-screen assertion; `teacher_behaviour` snapshot now also watches `[data-fb="overlay"]`.
- Deviation: B5 cell follows `wIdxs` (the week the week bar has in view — the same papers THIS WEEK's chip tallies), not `mx.inWeekPaper` → the class screen's THIS WEEK column has been week-bar-scoped since 1 Sep; reading `inWeekPaper` would put a different week's score beside the chip.
- Deviation: B5 header `THIS WEEK SCORE` → `Score` → it truncated in its column and repeated "This week" from the header beside it; on a past week that header shows the dates, so "Score" stays true.
- Deviation: B5 track 120px → 140px → `10/10 secured` needs ~132px at the cell's type size. (C1 keeps it fixed.)
- Deviation: (review SHOULD-4) submission-history SCORE track asked as 140px → 170px → measured: `10/10 secured` is 133px in that cell's 17px DM Mono plus 32px padding; 140px still wrapped.
- Deviation: B5 "the ≤420px rule stacks every grid to one column" → no such rule exists in `build_teacher_port.py` (only print, 560px flex-wrap and auto-fit rules) → nothing to copy; the column behaves like its neighbours at 390, and `teacher_reach` is green at 390/360.
- Deviation: B6 `entry.week` NOT redefined → new `entry.cardWeek` / `cardChase` read only by the card → `week` has five other readers (charts, class report tiles, card sort, digest row) that the plan says stay on the in-week rule. The class page's `openIn` no longer exists (MRB-336 made it one homework card per open set, already `colSub of colAsked`) → no class-page change was needed for the two to agree.
- Deviation: the flashcards page `document.title` said "— Mr Badmus AI" → "— MrBadmus" (small adjacent brand fix).

### Fable review of Stage B (29 Sep) — taken into the B commit

- MUST: the answer box is omitted on a card that has ratings but no answer in the payload (the old function never returns a review answer, so it cannot know); "No written answer" only on a card with no ratings and no make answer; a blank make answer (`""` + `blank`) keeps its Blank verdict. Proved in review mode in `flashcard_progress_drive` (`DETAIL_REVIEW`).
- Tries = `max(ratings.length, answer ? 1 : 0)` when `shown` is absent — never "Tries: 0" beside an answer.
- The panel-level disclosure is "History" (the sittings list inside).
- B6: nothing open but a set scheduled → the card's homework line says `opens Thu 09:00` (London; `opens Mon 12 Oct` beyond a week) with no bar, no chase and no Set work button.
- Accepted by the commander: the "Score" header, B1 also dropping the Open/Scheduled/Closed chip, the panel status chip "Done".

### Proof (Stage B)

- `flashcard_progress_drive` — all checks pass (panel, both degrade branches, B4/B5/B6 probe on teacher-live.js, static checks on the built pages).
- `tools/sharpen_flashcard_panel_live.py --expect-migration` on TEST — all pass: RPC carries `shown`/`answer`; the panel, the student-screen deck row (`In progress`, `0/4 secured`, Breakdown opens the panel, no Add feedback), the class Score cells, the My classes card (`0 of 2 in`, chase names). Throwaway world torn down by id list; residue query = 0.
- `teacher_behaviour` (25 fixtures), `teacher_reach` (25 × 390/360), `teacher_tells`, `theme_wiring_check`, `contrast_audit --quick --gate`, `brand_one_mark` — pass.

### Stage C (teacher) — C1, C2, C4

- **C1** Every teacher row-grid now uses only fixed px or `minmax(0,Nfr)` tracks, header and row identical, asserted by `BIND_ATTR` and by a new `teacher_tells` check (it went red on the Stage B build and is green on this one). Tracks as built:
  - Students `minmax(0,1.7fr) minmax(0,1.3fr) 140px 110px 160px 160px`
  - Assignments `minmax(0,1.6fr) 150px minmax(0,1fr) minmax(0,1fr) 120px 130px minmax(0,1.7fr) 220px`
  - Submission history `minmax(0,2.3fr) minmax(0,1fr) minmax(0,1.1fr) 170px minmax(0,1.05fr)`
  - Digest `minmax(0,1.5fr) minmax(0,1fr) 115px 115px minmax(0,1.5fr)`
  - chart rows `220px minmax(0,1fr) 96px|165px`
  - question-breakdown row `56px minmax(0,1fr) 180px <labelCol>`
  - marking grid `225px repeat(N,minmax(0,1fr)) 92px`

  A port stylesheet rule gives every row-grid cell `min-width:0` and keeps every cell but the title on one line with an ellipsis. Cells that hold a control are left unclipped, so focus rings survive. The Assignments actions sit right-aligned in a fixed 220px track and never wrap. `teacher/flashcards.html`'s table is `table-layout: fixed` with a `<colgroup>`, and `flashcard_progress_drive` asserts the layout, one col per column, every cell under its header, and nothing spilling. Measured on the fixtures at 1440: 0 misaligned cells, 0 clipped headers, 0 clipped body cells on all four tables.
- **C2** `shared/breakdown.js`: subtitle emptied in `renderHeader` and hidden from `buildShell` on (loading/error states never reach `renderHeader`; the new check caught that), node kept; `announcePupil` still says the position. `teacher_behaviour` asserts it (source check + the opened panel's `.bd-subtitle`).
- **C4** Node 17 (the top-bar crumb) is now a link to the parent: on the student and marking screens it reads `‹ 8R/SC1` and goes to the class screen via `SET_ON[17]` → `goCrumb` (it has `role=link` and `tabindex=0`). It no longer appears on the class screen. `teacher_tells` asserts both.
- Deviation: C1 widths differ from the plan. Measured on the fixtures: Assignments STATUS 96→150px ("Scheduled" pill), SUBMITTED 88→120px and CLASS MEAN 96→130px (their headers), title 2fr→1.6fr and weakest 1.2fr→1.7fr (its header clipped). The history SCORE column stays at Stage B's 170px, and the Students Score column at 140px.
- Deviation: C1 on a phone. With no `auto` minimum left, `minmax(0,…)` tracks collapse at 390 and cells overlapped (seen in the first 390 screenshot). Each table now carries a fixed `min-width` (Students 920, Assignments 1080, history 760, digest 680) and its card scrolls sideways (`overflow-x:auto`, was `overflow:hidden`, which cut the last columns off unreachably), the flashcards table's pattern. The ≤560px "wrap every nowrap caption" rule no longer applies inside a table row, and the chart-row phone rule was re-keyed to the new track string.
- Deviation: C1 "decks" — `teacher/decks.html` is a flex list (title left, actions right), not a table, so it has no columns to drift. Nothing changed there; the flashcard progress table was treated as the deck table.
- Deviation: C4 class-detail / digest / insights crumb `‹ My classes` → no crumb, because the "My classes" tab is lit right beside where it would sit, so it would repeat the tab (the no-redundant-text rule). flashcards.html → no bar crumb added: its eyebrow link (`8r/Sc1 · Flashcards`) directly under the bar already is the parent link. decks/today/admin/timetable: no crumb, unchanged.
- Adjacent fix: Stage B's `.fb-*` chips were 14px, under `breakdown.css`'s own 15px floor (caught by `breakdown_shots.py`), so they are raised to 15px here, since B is already live.
- Noted, not fixed: `breakdown_shots.py` stops at MUST-5 because its canned set was due 28 Sep 09:00, so from 29 Sep its pupil reads "Missing" rather than "hasn't started". The harness depends on the date; it is not a registered gate and this was not caused by this change.
- Pupil pages (C4 check): not re-shot here. The teacher phone bar is one row (brand, tabs, menu), so the crumb is not drawn at ≤560px on any teacher page.
