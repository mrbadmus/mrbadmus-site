# First-week fixes — five rulings from Mide's first real week with the classes

Branch `feat/first-week-fixes`, off `origin/main` at `3fb38bb62`. Run overnight,
22 Sep 2026, unattended. No ticket number was given for this run; every code
comment it adds is marked `first-week fixes (22 Sep 2026)` rather than an
invented `MRB-` number, and Mide can attach the ticket when he files one.

Backend half: `mrbadmus---backend` `d57dd7c`, pushed and live on Render before
the site (health reports `build: d57dd7c…`). Site half: one commit on this
branch, one push, receipts recorded on the tip.

A second session was working `feat/speed-round-2` in the main checkout at the
same time (student-live.js load order, teacher-data.js, RLS). Its branch had
not been pushed when this run landed, so this run landed first onto an
unchanged `origin/main`; that session rebases onto this. The student-live.js
edits here are kept inside the assignment-row model and the two existing
reads it draws on, with no code moved, so their rebase should be clean.

---

## 1 · Set work: the count is per topic (backend + site)

**What was wrong.** `MAX_QUESTIONS = 20` was read as a ceiling on the WHOLE
set, both in `shared/set-work.js` (`room = MAX_QUESTIONS - othersTotal(sc)`
greyed the chips) and in the backend's `POST /api/teacher/set-work` (refused a
combined list over twenty). Three topics of thirty-odd questions each offered
5 and 10 and nothing else; two topics still capped at ten apiece.

**The rule, as ruled.** A teacher picks the count per topic — 5, 10, 15, 20 —
limited only by that topic's own pool at the chosen tier, never by how many
topics are on the sheet.

**Site.** `othersTotal()` is deleted with all four uses. A chip is disabled only
when `n > that topic's availability`. `Add topic` is bounded by a new
`MAX_SCOPES = 10` (the number `worksheet.js` already used). `stepValid` now
asks: every filled scope has ≥1 row, none over 20, scopes ≤ 10.

**Backend** (`set-work-scope.js`, `server.js`, `worksheet.js`,
`test_set_work_v2.js`, `API-CONTRACT.md`):

- `MAX_SCOPES` (10), `MAX_QUESTIONS_PER_SCOPE` (= `MAX_QUESTIONS`, 20),
  `MAX_QUESTIONS_TOTAL` (their product, 200 — reachable only by a crafted
  body, never by the sheet). `worksheet.js` reads the first two from `SW`
  instead of holding its own copies; it keeps its own `MAX_QUESTIONS_TOTAL =
  100` because that is a fact about a PDF's length, and `test_worksheet.js`
  asserts it.
- `too_many_scopes` uses `MAX_SCOPES`; a per-scope `too_many_questions` inside
  the scopes loop; the combined check is the product for a `scopes` body and
  stays 20 for the flat legacy body (one scope by definition).
- ⚠️ **The real hazard was the history read.** `HISTORY_CHUNK × MAX_QUESTIONS <
  1000` bounded `teacherSetHistory` only while one assignment held twenty
  questions. A multi-scope set writes ONE `assignments` row per class carrying
  every scope's questions, so forty assignments could be 8,000
  `assignment_questions` rows and PostgREST would have returned the first
  1,000 in silence — already-set questions would look fresh and the preview
  would prefer them. The read now pages each chunk with `.range()` under the
  existing `(assignment_id, position)` total order. Shrinking the chunk was
  rejected: ~15 extra round trips on the critical path of `/scope` and
  `/preview`, the screen Mide already reports as slow.

**Not fixed, named for a ticket.** `PATCH /api/teacher/set-work/:id` on a
multi-scope assignment revalidates every stored id against the head scope
only, so editing tier/scope/question_ids on such a set answers
`questions_not_in_scope`. Pre-existing from MRB-342; the larger totals make it
more likely to be met.

## 2 · Set work: Next enables the moment a class is chosen (site)

`stepValid()` for step 0 was `!!(S.scope || S.scopeErr)` — it waited for
`/scope` to settle, and the stale-discard path in `loadScope()` never resynced
validity. It is now `S.classes.length > 0`; no fetch state can strand it.

The waiting moved to the Topic step, which has a real third state:
`S.scopeLoading`, a `syncScopePanel()` that stamps
`data-sw-scope-state="loading|ready|error|idle"` and renders a `Loading` /
`Unavailable` note plus a `Retry` button as siblings of the tree (the tree is
emptied on every build, which is why the old failure tag had an undefined
lifetime). Every path out of `loadScope()` — success, error, stale-discard —
resyncs; un-anchoring bumps `fetchSeq` so an in-flight answer cannot paint a
tree for a class nobody chose.

`apiGet` gained a 30 s `AbortController` (`READ_TIMEOUT_MS`), so a hung read
becomes a failure rather than a forever. That also un-strands two other stale
flags found on the way: a hung `/preview` left `sc.busy` set (Detail's primary
grey for good) and a hung `/swap` left one row's Swap disabled.
`apiPost`/`apiPatch` deliberately have no timeout — an aborted set may already
have been written.

## 3 · The student assignment card (site, generated)

All through the rulings layer; nothing hand-edited. Mechanisms:
`student_rulings.LOGIC` (F1–F4), `INSERT_AT`, two NEW mechanisms
`STYLE_EDIT` and `TYPE_SCALE` applied by `build_student_port._restyle()`, and
one emitted rule each for `.eyebrow` type and the Done colour.

| ruling | where |
|---|---|
| "Ask for an extension" gone (it opened the practice round) | `LOGIC` F1 — no label, handler, state or node remains; grep-clean across both trees |
| open AND missed → "Complete homework", opens the assignment | `LOGIC` F1; `shared/student-live.js` no longer blanks `assignmentHref` for missed rows |
| "MARKS ARE FINAL UNLESS A RETAKE IS OPEN" gone | `LOGIC` F1 (`footNote`); open row's "COUNTS TOWARDS WEEK n" kept |
| completion bar + labelled percentage | `INSERT_AT` (bar in the collapsed row, `CORRECT` under the number, `N OF M ANSWERED` in the expanded panel); `LOGIC` F3; `student-live.js` tallies `qtotal` inside the existing `assignment_questions` read and `answered` off the existing submissions + attempts reads (latest `attempt_no`); both fields or neither, so a failed read draws no bar rather than a false `0 OF 8` |
| Done is bright | `--pg-ok` #12A150 dot (3.06:1, over the 3:1 non-text floor), `--pg-ok-text` #0A6B36 word (6.02:1, AA); `_ROW_DONE` emitted rule; `student_themes.py` GATES the dot at 3.0:1 on all seven cases |
| type up | `TYPE_SCALE`: 66 runs on the class view, 65 on the assignment; `.eyebrow` 10.5→12px on both pages; the build REFUSES any `--st-mono` run under 12px or `--st-ui` run under 15px anywhere on either page, `clamp()` floors included |

**The late path, audited read-only (no backend change needed).** The
assignment page's logic checks no due date ("nothing is locked by it, ruling
5"); `saveAnswer`/`complete` never test `due_at`; `POST /api/assignment/answer`
and `/complete` accept unconditionally and store `is_late`. Note there is no
`on_time` column — `card.on_time` is derived client-side.

**The bar has no text in the collapsed row on purpose.** The row is one
`<button>`, so a caption would put a progress-dependent number into the
control census. The tap that expands the row is the phone's route to the
breakdown; hover does not exist on a phone.

## 4 · Phone order (site, generated)

`STYLE_EDIT`: the flashcards card gets `order:2`, Work goes `order:2 → 1`.
⚠️ The trap: Design's original RECALL card (node 136, `order:1`) was replaced
wholesale by the 23 Aug graft — the live card is node **10204**, which carried
no `order` at all (default 0, hence above Work). Measured at 390: Work →
Flashcards → Lessons → Shoutouts → Leaderboard. Desktop unchanged (explicit
grid placement; verified at 1460).

## 5 · Timetable builder flipped (site, hand-written)

`teacher/timetable.html` only. Header = blank corner + Mon…Fri; one row per
period with `periodHeader(p)`. The `<select data-wd data-p>` cell is
byte-identical, so `readGrid()` and the `replace_timetable` payload keep the
same `{classId, weekday, period}` shape (row ORDER is now period-major, which
nothing reads — the RPC is delete-then-bulk-insert). Period head is
`position:sticky; left:0` with a background and a 1px box-shadow (a collapsed
table stops repainting a sticky cell's own borders). `min-width` 640→600; at
≤560px the head wraps to 92px so class names read in full inside the selects
(a table cell treats `width` as a minimum — 104px `nowrap` rendered 152px and
clipped every class name). Page body does not scroll sideways at 390; only
`.grid-wrap` does.

---

## 6 · Design-parity references — updated for exactly these rulings

Each marked `⊕ RULED by Mide 22 Sep 2026 — first-week fixes`:

- `student_behaviour.RULED_DIVERGENCE['class view']`: the marked row's
  MARKS-ARE-FINAL footnote.
- **New registry `student_behaviour.RULED_ADDITIONS`** — the exact mirror of
  `RULED_DIVERGENCE`: a span the PORT adds that no Design delivery contains,
  stripped from the port per drive, forbidden in Design's file, required
  present on the port. `AMENDED_ADDITIONS` could not hold these: it requires
  the span to exist in Design's amended delivery. Entries: `(?<=% )CORRECT ?`,
  `\d+ OF \d+ ANSWERED `. With a four-direction self-proof.
- **New shape `port_suffix` in `RULED_CONTROL_EDITS`** (`" CORRECT"` — the
  word sits inside the row button, so text stripping cannot reach the census).
- **New drive `a marked work row expands`** — see finding 1.
- `student_themes.py`: `PAGE_OK` / `PAGE_OK_MARKS` gated at `NONTEXT_AA`.
- `student_parity.py`: nothing — the preview pair is byte-identical.

## 7 · Findings left standing (real, not papered over)

1. **No drive on the class page had ever opened an expanded work row.** The
   existing drive `"a work row expands"` clicks `03 Animal and plant cells`, a
   LESSON card. The detail line, notes, question chips, primary button and
   footnote were measured on neither file until tonight's new drive. The
   misnamed drive is kept (it is the only press on that control).
2. **The `Open the assignment → Complete homework` relabel is not gate-covered**
   on an open/missed row: `RULED_CONTROL_EDITS`' exact-label arithmetic cannot
   express it because `Open the assignment` is also the bench's button. Would
   need a fifth entry shape. Verified by screenshot and live DOM at 390/1460.
3. A marked row with an open retake would read `0 OF n ANSWERED` (answered is
   taken at the latest `attempt_no`; a fresh retake has none). Unreachable
   today — no live row carries `retake`. Needs a ruling before retakes ship.
4. **Done is now two colours on one page**: green in the work row (tonight's
   ruling) and espresso in the term-spine legend and week tiles (Mide's 23 Aug
   ruling). Not folded in; Mide's call.
5. `student_controls_drive.py` exits 1 rather than skipping cleanly when the
   credential is absent.
6. `set_work_drive.py`: three checks (`a small KS3 lesson exists to drain`, `a
   scope of 5–9 questions exists`, `a scope of 10–14 questions exists`) search
   for a node with a SMALL pool and find none now the banks are fully stocked.
   Inherited (identical on a pristine tree), and a gate that has stopped
   watching what it names. Overridden on the tip commit, not weakened.
6b. `row_download_lands` (the class table row's Download) saved Chrome's own
   33 MB `downloads.html` instead of the PDF, on the pristine tree and on
   three of four runs tonight, while every other worksheet/PDF check in the
   same drive (route, content type, sheet download, multi-scope, row read)
   is green. A headless-Chrome download artefact on that one press, not the
   worksheet route. Overridden with the three above; worth a look at how the
   row's `<a download>` is armed.
6c. `classes_screen_anchors_on_first_tap` went red in the receipt round and
   that one WAS caused here: it waited for "any new `/scope` entry", and with
   Next no longer waiting on `/scope`, the previous check's late answer (for
   another class) arrived first. The drive now waits for the picked class's
   own entry; the assertion is unchanged.
7. `mrbadmus---backend/CLAUDE.md` line ~229 still says "Never `git push` in
   Terminal". Stale since MRB-228, not corrected tonight (a docs commit would
   redeploy Render for nothing); worth one line when the backend is next touched.
8. `check_row_download` in `set_work_drive.py` recorded a correct red for a
   non-PDF download and then parsed the bytes as a PDF anyway, crashing past
   `FX.teardown()` and leaving the throwaway world standing on TEST. Fixed
   (returns after the red; no assertion weakened).

## 8 · Deviations

- Deviation: the executor labelled the change `MRB-350`, a number nobody
  issued → replaced with `first-week fixes (22 Sep 2026)` in both repos → a
  made-up ticket in `git log` is worse than none.
- Deviation: worksheet's total stays 100, not the new 200 → kept, with only
  the two per-scope constants shared → `test_worksheet.js` asserts 10×20
  overflows a worksheet; a PDF's length is a different fact from a set's size.
- Deviation: the `.eyebrow` rule was first typed into `shared/student-ds.css`
  and the build wiped it silently → moved to an emitted rule in
  `build_student_port.py` → that CSS is generated from Design's six sheets;
  caught by a clean `git status` after a green build.
- Deviation: two `student-live.js` edits sit outside the assignment-row block
  (the `assignment_questions` tally, the attempts read's select) → made, ~10
  added lines each inside existing loops, nothing moved → the alternative was
  a bar reading `0 of 8` at a child who had answered 7.
- Deviation: `student_behaviour.py` gained a registry, a control-edit shape,
  a self-proof and a drive → the minimum that states the rulings honestly →
  `AMENDED_ADDITIONS` structurally cannot hold a change no delivery contains.
- Deviation: backend pushed from the terminal despite the backend CLAUDE.md's
  stale line → done under the site's standing authorisation (MRB-228), and the
  order the contract requires (backend live first, then site) → see finding 7.

## 9 · Verification

Per-fix drives (executor runs, before the receipt round):

| check | result |
|---|---|
| `node test_set_work_v2.js` (backend) | 188 passed, 0 failed, 1 skipped (177 before) |
| `node test_worksheet.js` (backend) | 98 passed, 0 failed, 1 skipped |
| `teacher_behaviour.py` | PASS, 24 fixtures |
| `teacher_reach.py` | PASS, 24 fixtures × 2 widths |
| `teacher_picker_drive.py` | PASS |
| `set_work_drive.py` against the new backend | 398 checks, 3 red — the inherited small-pool searches (finding 6); identical on a pristine tree. New checks `check_three_topics_at_twenty` (7 assertions) and `check_next_is_immediate` (4, `/scope` held 3 s) green |
| `student_behaviour.py` | PASS, 20 class-view drives (incl. the new one) + 9 assignment drives |
| `student_themes.py` | PASS, seven cases, Done dot gated at 3.0:1 |
| `student_parity.py` | PASS, previews byte-identical |
| `student_controls_drive.py` | refused — no student credential in this environment |
| `today_drive.py` | all checks passed |
| `build_all.py` | exit 0; teacher pages/fixtures changed by `?v=` stamp only |
| Render | `/api/health` → `build: d57dd7c…`, `db: ok` |

Screenshots (scratch, not in the tree): Set work three topics at 390/1280;
class page marked/open/missed at 390 and 1460, phone order at 390, assignment
at 390; timetable at 390, 390-scrolled and 1280. `scrollWidth == innerWidth`
read at 390 on every student and timetable capture.

Receipt round and live check: see §10, filled after the round.

## 10 · Receipt round and live

`prepush_gate.py --record-all` on the tip (`MRB_BACKEND`, `MRB_SET_WORK_PASSWORD`,
`MRB_THROWAWAY_PASSWORD`, `MRB_TEST_TEACHER_PASSWORD` set; no student
credential in this environment). Two rounds: the first found the anchoring
race (§7 finding 6c), the second, on the amended tip:

| gate | result |
|---|---|
| verify_ks3, student_behaviour, student_themes, today_drive, teacher_behaviour, teacher_reach, teacher_picker_drive, ks4_chrome_drive, consumer_flag_off, teacher_perf_budget, teacher_admin_real, mrb328_card_prefetch, student_bell_drive | PASS, receipt written |
| set_work | FAIL — 391 checks, 4 red: the three small-pool searches + `row_download_lands` (§7 findings 6 and 6b). Overridden on the tip. `check_three_topics_at_twenty`, `check_next_is_immediate`, `classes_screen_anchors_on_first_tap` all green |
| teacher_admin_foreign_class | FAIL — C7 REMINDERS × 3, inherited since MRB-335. Overridden on the tip |
| student_parity, import_year_drive, leaderboard_behaviour, ks4_pool_drive, ks3_instrument_liveness, student_switches, seating_drive, assignments_hold_drive, class_csv_upload, mrb328_import_picker(_real) | SKIPPED BY RULE — no path this branch changed is in their `watches` |
| student_controls_drive | SKIP — no student credential |
| 3d_parity, 3d_render_check | SKIP — no `3d-studio/dist` |

Live check: a docs-only follow-up commit records the `check_ks4_live.sh`
result for `student/class.html`, `teacher/classes.html`,
`teacher/class-detail.html` and `teacher/timetable.html` after Cloudflare
reported the deploy.
