# Overnight run — 22 August 2026

Follows `d875e5a0a`. Scope: the student pages only.

**Production project ref: `urklkrwevjtlfbwnipjn` — ends in N.** Stated before the first write,
as the standing contract requires. Test project `qeppkiswvclkkwbxmlok` is not in play tonight.

---

## Step 0 — Recon

Repo at `d875e5a0a`, tree clean, branch `main`.

⚠️ **The machine clock reads 21 August, not 22.** `date` returns 21 Aug, the migration
versions Supabase assigned are `202608211151xx`, and the backend's own `server_now` came back
`2026-08-21T12:01Z`. This file keeps the name the contract gave it; every timestamp in it is
the real one, so they will not agree with the title and that is deliberate rather than sloppy.

| | |
|---|---|
| assignments on production | 2 |
| `assignment_questions` | 6 |
| `assignment_submissions` | 3 (all by Mide's own account) |
| `class_members` | 134 across 15 classes |
| `8r/Sc1` | `d9740ab8…`, KS3 Y8, year 2026-27, **1 member** |

`b0308282-5429-4050-827f-4707286a88aa` is **midebolabadmus@gmail.com** — Mide's own account,
which this run is forbidden to use. Checked before writing anything so that its three
submissions could be excluded from every cleanup below by id rather than by hope.

---

## W1–W4 — an assignment becomes a week of work. BUILT, DEPLOYED, DRIVEN.

### The schema, four migrations, one at a time

Production `urklkrwevjtlfbwnipjn`. `apply_migration`, never `db push`. The MCP records its own
version and writes no local file, so all four were written to `supabase/migrations/` afterwards
under the versions Postgres actually recorded — the drift gotcha, handled rather than repeated.

| version | what |
|---|---|
| `20260821115131` | `assignment_submissions` gains `attempt_no`, `status`, `started_at`, `completed_at`, `is_late` |
| `20260821115140` | backfill — every existing row is complete; the two rows against `72a5b315` become attempts 1 and 2 rather than a constraint violation |
| `20260821115148` | NOT NULL + defaults + two CHECKs |
| `20260821115157` | unique `(assignment_id, student_id, attempt_no)`, unique `(submission_id, question_index)`, and a covering index |

Checked for duplicate `(submission_id, question_index)` **before** adding the unique index —
zero, so it could be added without touching a single existing row.

⚑ **`assignment_submissions_complete_chk` is the interesting one.** It makes a completed row
without a completion stamp, or an in-progress row carrying one, *impossible to write*:

```sql
check ( (status = 'complete'    and completed_at is not null and is_late is not null)
     or (status = 'in_progress' and completed_at is null     and is_late is null) )
```

That is the constraint that makes `'17 SEP, 20:41'` unrepresentable. There is exactly one
writer of `completed_at` and it is the server's own clock.

### The routes

`POST /api/assignment/answer` · `GET /api/assignment/progress` · `POST /api/assignment/complete`
· `GET /api/class/progress` — and `/api/assignment-submit` **rebuilt on the same machinery**
rather than left as a second way for a submission to come into existence. `/api/class/current-assignment`
gained a `progress` block so the class page's work row can say "5 of 15" without a second round trip.

The score is **derived on the server** from the rows in the table and recomputed on every
answer. The browser posts what the student chose; it never posts what it is worth.

### Deployed, and proved BEHAVIOURALLY — twice

A health check cannot prove which build Render is serving, so it was not used.

1. **Route existence.** `/api/assignment/definitely-not-a-route` → **404**, while
   `/api/assignment/progress`, `/api/assignment/complete` and `/api/class/progress` all →
   **401**. The router distinguishes them, so the new code is the code running.
2. **A field that did not exist before.** `/api/class/current-assignment` came back carrying
   `progress: {total: 4, answered: 0, percent: 0, status: "not_started", …}`. That block is new
   in this commit and no earlier build could have emitted it.

### The drive, as a real signed-in student

Every ruling exercised against production, end to end:

```
── SITTING ONE
  answer q1 (right) → answered 1/4  score 1/1
  answer q2 (wrong) → answered 2/4  score 1/2
── CHANGE AN ANSWER: q2 again, this time right
  answer q2        → answered 2/4  score 2/2      ← 2, not 3. It UPDATED the row.
── LEAVE AND RETURN — read back FROM THE SERVER
  200 answered=2/4 status=in_progress attempt=1 overdue=False
── SITTING TWO
  q3 (wrong)                → answered 3/4  score 2/3
  q4 SELF-MARKED, is_correct null, criteria 2 of 3
                            → answered 4/4  score 2/3   ← max_score 3, not 4
── COMPLETE
  200 is_late false  completed_at 2026-08-21T12:01:57.288+00:00
── COMPLETE AGAIN
  200 already:true   completed_at IDENTICAL to the first press
── ANSWER AFTER COMPLETION, no retake flag
  409 attempt_already_complete            ← not a silent second attempt
```

Read back at the database, which is the check that matters: **one** submission row, **four**
attempt rows, `q2` present once, `is_correct` NULL preserved on the self-marked rung with
`criteria_met [1,2]` of 3.

### Rulings 4 and 5, proved against a genuinely overdue piece of work

Neither live assignment is overdue, so a throwaway one two days past its due date was created,
driven, and is deleted in the housekeeping below.

```
answer on a 2-days-overdue assignment      → 200. Nothing is locked by the clock.
progress while overdue and unfinished      → status in_progress, is_late NULL
                                              ← unfinished, not late
complete after the deadline                → 200 is_late TRUE
```

### W4 — both attempts kept, best counts

```
retake answer     → attempt_no 2
attempts kept     → [(1, 1/1, complete), (2, 0/1, complete)]
BEST              → attempt 1
```

Best is decided on **raw score first**, deliberately: a retake abandoned after one lucky answer
is 1/1 = 100%, and it must not beat a finished 3/4.

### Scoping

```
/api/class/progress as a STUDENT      → 403 not_authorised   (a child may not read the class's other children)
/api/assignment/progress, unknown id  → 404 assignment_not_found
```

---

## The welded numbers, the six-question floor, and the words. BOTH GATES GREEN.

### The class view — 22 seams closed inside method bodies

Every figure the last run listed as "still welded, and left deliberately" is now data:
the docket's question count, `Using a microscope`, `Mon 15 Sep`, `Thu 18 Sep, 18:00`,
`2 days left`, `40 POINTS AT STAKE`, `58%`; the recall panel's `46` and the readings strip's
paired `46` / `77%`; `ROUNDS` `08`; `roundNote`; and `DUE THU 18:00`.

`grep -c -F` on `student/class-ported.html`, every one: **0**.

⛔ **`pad(Math.max(9, st.streak))` — the floor of nine.** A child whose best streak is three
was shown nine. It is now `Math.max(MRB_DATA('bestStreakFloor'), st.streak)`; the fixture
carries `9` as a NUMBER so Design's render is byte-identical, and the live source supplies
`0`, which makes the `Math.max` a no-op and lets the real streak through.

⛔ **Where the product does not record something, the key is EMPTY.** `docketWorth` is empty
because no column anywhere assigns an assignment a points value — `40 POINTS AT STAKE` was a
number chosen for a drawing. `recallAnswered`, `recallPct` and `recallRounds` are empty because
the recall round writes nowhere: `/api/class/recall` only reads, and no table carries a class,
a teaching week and a rung together. `roundNote` is empty because Design's sentence states an
apportionment ("Recall is worth 20 of the 100 points") the platform cannot compute — the same
fault the 21 Aug ruling took out of the split bar, and platform self-explanation besides.

`docketElapsed` is the one that COULD be made real, and the ruling requires it to be: it now
carries the student's answered percentage, which is exactly ruling 2's "the same as a percentage".

⚑ **`dueWordLong` is deliberately less specific than Design's.** Design wrote `'DUE THU 18:00'`
— one class's one deadline, printed on every open row of every class. It is now just `DUE`.
The precise deadline is already on the line directly below (`detail` reads
`DUE THU 18 SEP, 18:00`), so nothing is lost, and a class with two things open at once no
longer shows one row's time on the other's.

### The six-question floor — it was FIVE places, not three

The prompt named `roundLive: st.qi < 6`, `Math.min(st.qi, 5)` and `/ 06` and attributed them to
the assignment page. ⚠️ **They are the CLASS page's recall round.** The assignment page's floor
is a different line — `Math.max(6, …)` in `count()` — and `shared/student-live.js` had a third,
refusing to build an assignment of fewer than six at all. All were real; all are fixed. Two more
turned up that were on nobody's list: the recall room's own `qCounter`, and the index clamp
`const qi = Math.min(st.qi, 5)` two hundred lines earlier, which picks the question object
itself and would have read past the end of a short round.

Every count now derives from the array's actual length, guarded so an empty round renders `0%`
rather than `NaN%`.

⚠️ **AND THE CAP OF FIFTEEN IS NOT THE SAME BUG — the first draft removed it and went red.**
`count()` reads `Math.round(this.props.questionCount ?? 15)`, which looks inert: nothing passes
`questionCount` and the mount emits `props: {}`. But Design's own fixture array is **sixteen**
questions long and Design renders fifteen, so the 15 is a working cap that `Math.min` applies.
Removing it made the port render `16 QUESTIONS` against Design's `15` and diverged nine
behaviour drives at the same character. It is also the RIGHT cap independently:
`ASSIGNMENT_SIZE` in `assignment-compose.js` is 15, so a longer assignment cannot be composed.
Only the floor was ever wrong.

### The words — W5

"Complete" replaces "Hand it in" on the button, the chip, the end-screen heading and eyebrow,
the marked-work kicker, and the class page's work rows (`COMPLETED …`, `NOT COMPLETED`).

⚑ **Two mechanisms, and not by preference — by which one can reach the word.** The button, the
chip and one heading are TEXT NODES in Design's markup, so they go through BINDINGS, which is
the mechanism built for a template literal that differs on the real page. Their siblings
(`screenLabel`, `doneEyebrow`, `doneKicker`) are computed in `renderVals()`, where BINDINGS
cannot see them, so they go through `student_rulings`. Design's typography and placement are
untouched throughout.

### The wiring

`shared/student-live.js` gained a **sink** — `window.__MRB_SINK__`, set immediately before
mount and read lazily by the page. It is a WRITER and a resume source; everything the page
RENDERS still comes through `MRB_DATA`, so the rule that the production page has no code path
to Design's example data is intact.

- `confirm()` posts the answer **the moment it is given**.
- `loadLive()` takes the server's state outright when a sink is present; localStorage is a
  cache and an offline queue, never the truth.
- `handIn()` calls `/api/assignment/complete` and takes its stamp and its lateness from the
  reply — or shows no stamp at all. It never manufactures one.

⚑ **The sink is read lazily on every call and never captured at script-evaluation time.** The
logic script runs before `student-live.js` has loaded, so a captured reference would be null
for ever and every answer would be silently dropped — which is precisely the failure this
whole unit exists to remove, and it would have been invisible.

⊕ **Design's demo scenarios are now unreachable in production.** The page routed off the URL
hash and fell back to `Mid-way`, which pre-fills six answers with three deliberately wrong;
`#handedin` would have shown a child a completion that never happened. With a sink present
there is exactly one scenario and it is the student's own saved state. This replaces the
`#live` history rewrite `student-live.js` was doing from outside, which the last run recorded
as a workaround belonging in the page. It now is in the page.

### Both gates, green, nothing weakened

```
student_behaviour.py   30 drives, every one "text identical", RULED_DIVERGENCE UNTOUCHED
student_parity.py      layers A–H green at 360 / 390 / 820 / 1460
```

⚑ Worth saying plainly: **no divergence had to be registered for any of this.** The word
changes go through bindings (the fixture keeps Design's words), and the two ruling-introduced
constants carry Design's own values, so the fixture still renders byte-for-byte what Design
drew. `RULED_DIVERGENCE` still holds exactly the two 21 Aug entries and no more.

