# MRB-331 — SET WORK v1

Teachers set targeted work themselves; the automatic weekly work can be
switched off per class. Built on `feat/set-work`, to merge by PR after main's
MRB-328 and MRB-330.

---

## 1 · What this run actually is: a reversal of MRB-287

Design drew a "Set work" sheet. It has never shipped, because
`teacher_rulings.DEAD` prunes it from all six generated teacher pages, under a
ruling that was **correct when it was written**:

> Creating an assignment HAS NO WRITE PATH. Measured, not assumed: the only
> teacher-side writes that exist anywhere in the data layer are
> `insertClassShoutout` and `softDeleteClassShoutout` … So Design's three-step
> "Set work" sheet is a sheet that would collect a topic, a question count, a
> due day and a class list, press a button, show a toast saying the work had
> been set, and set nothing. That is not an unfinished feature — it is a
> control that LIES, and MRB-287 forbids it outright.

MRB-331 builds the write path. The premise stops being true, and the sheet
comes back. The manoeuvre has a precedent in the same file — MRB-326 JOB 4c
took node 236 off `DEAD` the same way — and the same discipline is followed:
the removed rows are kept verbatim in a comment saying what changed and what
re-adding them would destroy.

⚠️ **The brief says the button was "withheld in MRB-325". It was not.** MRB-325
ruling 1 (restated as MRB-326 ruling 4) is why the hand-written
`teacher/today.html` has no Set work button. `DEAD`, under MRB-287, is why the
six GENERATED pages have none. Both are reversed here; only the second is a
`teacher_rulings.py` edit. Nothing in this run turned on the difference, but a
future reader looking for the ruling under MRB-325 would not find it.

### Six nodes, five restored

| node | what | verdict |
|---|---|---|
| 581 | the Set-work sheet itself | restored |
| 165 | "Set work", classes screen primary | restored |
| 214 | "Set work", class screen primary | restored |
| 282 | "Set work", the no-work empty state | restored |
| 194 | "Set work" on a class card with students but no work | restored |
| 382 | **"Reteach and reset"**, marking screen header | **STAYS DEAD** |

Node 382 is drawn by `openSetWork` but is labelled "Reteach and reset".
Restoring it would have made a control that lies about *what it does* rather
than about *whether it does anything* — a smaller lie, still a lie.
Reteach-and-reset is a different feature and is not in this ticket. **Decision,
not oversight.**

---

## 2 · The data model as built

Two migrations, both rehearsed on TEST, neither applied to production — per the
project rule, production migrations reach prod only at merge.

### `20260906144742_mrb331_teacher_set_work_columns.sql`

| column | on | shape |
|---|---|---|
| `source` | `assignments` | `text not null default 'auto'`, CHECK in (`auto`,`teacher`) |
| `set_by` | `assignments` | `uuid references profiles(id)` |
| `release_at` | `assignments` | `timestamptz`, NULL = already released |
| `auto_assignments` | `classes` | `boolean not null default true` |

**`source` is tied to `auto_generated` by a CHECK**
(`assignments_source_agrees_with_auto_generated`), not by discipline. The older
column already answered "where did this come from", and every existing reader of
it — the API payload, the teacher tables, the consumer path — keeps working
unchanged only for as long as the two agree. The constraint makes disagreement
impossible rather than unlikely.

**`set_by` is not `teacher_id`.** On an auto row `teacher_id` is whichever
teacher `classSubjectId()` happened to find first in `class_teachers` — a filing
detail. `set_by` is the author, and is NULL on every auto row.

**The lesson ref needed no new column.** `assignments.subtopic` *is* it:
`scheme_of_work_entries.subtopic` is the lesson slug and is the whole join to
`ks3_assignment_bank.lesson_slug`, and the auto producer writes `subtopic: null`,
so there is no collision. `source_sow_entry_id` is set too — the teacher picks a
real scheme row, so the provenance is real rather than reconstructed.

**Per-class-per-week uniqueness is now auto-only** —
`assignments_class_week_uniq` gained `and source = 'auto'`.

### `20260906145023_mrb331_release_gates_student_reads.sql`

`assignments_student_read` and `aq_student_read` gain
`(release_at is null or release_at <= now())`.

The hold could have lived in the backend alone. It does not, because
`student-data.js` reads `assignments` **directly through PostgREST** — the
student's work list is one of those reads — and a backend-only check would have
left next Monday's title on a child's screen today, silently, looking normal.

`release_at IS NULL` stays visible. Every assignment that exists today has a
NULL release, including the two pre-term ones on Rainford's `8r/Sc1` that
MRB-324 went out of its way not to retract.

**Proved under real RLS on a real child's JWT before any code depended on it:**
held work invisible — the assignment *and* its questions — released work
visible, and the flip happens at read time rather than being cached in the
token.

### The backfill, and the one number that made it safe

The backfill reads `auto_generated`, which is the only record of how a row was
made, and labels `false` rows `'teacher'`. On TEST that is 25 rows — hand-seeded
fixtures with no `set_by`, which will render with no author, which is true.

What mattered was whether the relabel moved any row **out of** the uniqueness
index. It did not, and that was measured rather than assumed:

```sql
select count(*) filter (where auto_generated is false and academic_week is not null)
from assignments where deleted_at is null;
```

**TEST: 0 of 34. PROD: 0 of 2.** Every such row already carried
`academic_week IS NULL` and was therefore already outside the partial index. The
query is written into the migration to be re-run before the production apply; a
non-zero answer means the migration must not go in as written.

---

## 3 · The hold, resolved once

`release_at = max(what the teacher chose, schools.assignments_open_from)`,
computed when the work is set and **stored**.

Not recomputed at read time, and the reason is a live ruling rather than a
preference. MRB-324 ruled that the hold governs CREATION and never retracts —
Rainford's two pre-term assignments keep being served, hold or no hold. A
read-time `max()` would mean a school moving its hold later retracts work a
class can already see, which is exactly what that ruling forbids. A stored
instant is a promise; it does not get renegotiated.

The date arithmetic does not use `new Date('YYYY-MM-DD')`. That is UTC midnight,
which in British Summer Time is 01:00 school-local — work held until the 14th
would release at one in the morning on the 14th. Wrong by an hour, for half the
year, in a way nobody finds. `londonMidnightInstant` asks `Intl` where midnight
actually was, the same way `dueAtFor` already asks it where 18:00 is. Proved:
the fixture's 14 September hold resolves to `2026-09-13T23:00:00Z`.

---

## 4 · The change that could have broken the live site

`/api/class/current-assignment` found the week's work with

```js
.eq('class_id', classId).eq('academic_week', week).maybeSingle()
```

The moment a class holds an auto **and** a teacher-set assignment in the same
week — the entire point of this ticket — that returns two rows and PostgREST
turns `maybeSingle()` into an error. Not for the teacher who set it: **for every
child in the class**, on the page they open to do their homework.

Three lookups gained `.eq('source', 'auto')` — `server.js:1047`, `:1175`,
`:3527` — and the uniqueness index was narrowed to match. Nothing else in the
run would have caught it: the set succeeds, the row is correct, the RLS is
correct, and the class page is simply broken. It has its own named check in the
drive.

Teacher-set work still carries a real `academic_week`, which is what puts it in
the class screen's week bar, in Today and in the digest. Dropping the week to
dodge the constraint would have left the index untouched and made the work
invisible to every week-scoped surface.

---

## 5 · Found on the way: the KS4/KS3 lesson-slug collision

**A live defect, dormant, that this ticket would have activated.**

`bankFor()` joined `ks3_assignment_bank` on `lesson_slug` alone. That table has
**no `key_stage` column** — only its name says KS3. Eight KS4 subtopic slugs in
`scheme_of_work_entries` are byte-identical to KS3 lesson slugs, twelve bank
rows each:

| slug | KS4 topic | KS3 unit |
|---|---|---|
| `aerobic-respiration` | Bioenergetics | B8 |
| `catalysts` | Rate and Extent of Chemical Change | C6 |
| `changes-of-state` | Particle Model of Matter | C1 |
| `chromatography` | Chemical Analysis | C3 |
| `conservation-of-mass` | Quantitative Chemistry | C2 |
| `distance-time-graphs` | Forces | P3 |
| `electric-fields` | Electricity | P9 |
| `magnetic-fields` | Magnetism and Electromagnetism | P10 |

A KS4 class asking for any of those gets KS3 questions. Real science, three
years too easy, and nothing anywhere says so. It is dormant today only because
production has no KS4 scheme rows and KS4 assignments are never composed.

**This run would have activated it.** The topics route would have reported
`available: 12` on exactly those eight and 0 elsewhere — which reads like a
partially-stocked KS4 bank rather than like a bug — and a teacher would have set
the twelve. It would also have made this run's own claim ("KS4 has no bank, so
the sheet refuses") quietly false on eight rows.

Sealed at the signature rather than at a call site: **`bankFor(keyStage, slugs,
band, cols)`**. No caller can reach the table without naming a key stage, and
the wrong one yields an empty map rather than the wrong questions. That closes
the thing a call-site guard cannot — a future fifth call site.

⚠️ **The write-side seal is the one that mattered.** `questions_not_in_lesson`
would have PASSED these ids: they genuinely *are* in the lesson, by slug. The
key-stage refusal is checked first, and is why a crafted request cannot store
KS3 questions on a KS4 assignment.

`pool_ownership.py` now fails if that argument ever disappears.

---

## 6 · KS4, honestly

The brief says teacher-set work draws from "KS4 quiz banks for KS4". **Those do
not exist**, and this was measured rather than assumed:

- `ks3_assignment_bank` is the only bank — 2,220 rows, units B1–P12.
- `exam_questions` holds 41 KS4 rows, `source` in (`code_seed`, `bonding_v2`),
  **zero** `unit_code`, extended-response with mark schemes.
- `assignment_questions.one_pool_per_assignment` requires `band NOT NULL`, which
  structurally refuses an exam question.
- The codebase already says so: `consumer/work.js:484`
  `return { skipped: 'no_ks4_bank' }`, and `generate_site_v5.py:773` "THERE IS
  NO KS4 PROGRESS MODEL."

What KS4 *does* have is the scheme — 865 `scheme_of_work_entries` rows across
Y10/Y11, fully scoped by tier × pathway. So the KS4 half that could be built and
proved is the **picker**: a KS4 class browses its own correctly-scoped scheme,
and the sheet **refuses to set** with a named honest state rather than creating
empty work. The backend's own stance, at `server.js:1194`: *"An assignment with
no questions is worse than none."*

Proved on a Higher Triple class against a Foundation Combined control: **49
lessons the Triple class is offered that the Combined class is not**, `has_bank:
false`, `available: 0` on every row, and zero leakage on all eight colliding
slugs.

---

## 7 · A design decision the data forced

**One lesson cannot fill ten questions.** Measured: `max(available)` across all
81 lessons offered to a class is **4**. The bank holds twelve questions per
lesson — four easier, four standard, four harder — so a single (lesson, band) is
always exactly four.

The brief asks for a default of 10, a max of 20, and a swap "for another from
the same lesson". Taken literally, all three are impossible at once: the default
could never be met, and **the swap pool would always be empty — a dead control**,
which is the exact thing MRB-287 forbade and this ticket exists to stop shipping.

**Decision.** The chosen lesson supplies everything it can in the chosen band;
the rest fills from the lessons **before** it in the scheme, nearest first. That
is not a new rule — it is `composeFromBank`, Mide's ruling of 20 August 2026,
already mirrored in Python and cross-checked test-for-test against it. Reusing
it means a teacher-set assignment and an auto one cannot disagree about what
"ten questions on gas exchange" means.

- `picked` = `composeFromBank([chosen], earlierSlugs, byLesson, band, count)`
- `pool` (the swap candidates) = everything unused from the same drawn range
- **every question carries its `lesson_slug` and lesson title**, and the sheet
  shows them

That last point is what keeps the fill honest rather than hidden: the teacher
picked one lesson and is getting a set drawn *around* it, and can see exactly
that on every row. "Same lesson" is impossible at four per band, so the honest
reading is "the same neighbourhood of the scheme", and nothing is concealed.

Measured live: **10 picked where the lesson itself holds 4, a swap pool of 310,
spanning 3 lessons.** Week 1 still gives its 4 with `short: true`, because there
is nothing behind week 1 to fill from.

---

## 8 · Decisions taken under my own authority

| # | Decision | Why |
|---|---|---|
| 1 | **The sheet goes through the backend**, not straight to Supabase | `pool_ownership` fails on the mere presence of `ks3_assignment_bank` in `teacher-live.js`/`teacher-data.js`. Putting the read in an unscanned file would widen a gate by naming rather than by decision. The gate's own note names the honest route; `assignments_hold_drive.py` set the precedent that a teacher write control must not become a direct DB write |
| 2 | **Node 382 stays DEAD** | It is labelled "Reteach and reset". A Set work sheet behind it would lie about what the control does |
| 3 | **`source` tied to `auto_generated` by a CHECK** | Two columns answering one question drift. The constraint makes that impossible, and every existing reader keeps working |
| 4 | **No new column for the lesson ref** | `assignments.subtopic` *is* the lesson slug, and the auto producer writes null there |
| 5 | **The hold is baked at set time, not applied at read time** | MRB-324 ruled the hold never retracts visible work. A read-time `max()` would retract |
| 6 | **Auto rows are not retro-held** | Same ruling. Auto work is already held at creation; adding a read-time hold would retract Rainford's two pre-term assignments, which MRB-324 explicitly protects |
| 7 | **Fill backwards through the scheme** (§7) | The alternative was a dead swap control and an unreachable default |
| 8 | **KS4 refuses rather than composing empty work** (§6) | There is no KS4 pool; the backend's own stance is that empty work is worse than none |
| 9 | **A partial multi-class set is refused whole** | A teacher who sees an error must not have to guess which half landed. ⚠️ See §13 — this was TRUE of the authorisation check and FALSE of everything else until a cold pass found it |
| 10 | **The bench falls back to teacher-set work when auto is off** | Otherwise a class with the switch off shows an empty bench above a full work list, which reads as broken |
| 11 | **Only *open* work rows get a link** | Marked rows already route to their lesson (ruling P3); missed ones are Design's "Ask for an extension", a different control |
| 12 | **`slt` cannot set work** | Setting work is a teaching act. The admin route accepts SLT for a date dial, which is a different kind of thing |

---

## 9 · What is v2, and deliberately not built

- **Teacher-authored free-text questions.** Named as v2 in the brief. Not built,
  and **not drawn as a dead control** — there is no greyed-out "write your own"
  anywhere on the sheet.
- **Reteach and reset** (node 382). Still `DEAD`.
- **A KS4 question pool.** §6. Until one exists, KS4 set-work is a picker and an
  honest refusal.

---

## 10 · The student side

Teacher-set work reaches a child's work list **for free**, and that was verified
rather than rebuilt: `student-data.js` reads `assignments` under RLS with no
source filter, and the work row already renders `c.title` verbatim. The release
gate is on that same read. Two things were genuinely missing:

1. **It was not openable.** `assignmentHref` was set only for the current auto
   assignment, so every teacher-set row rendered with no way in. Every open row
   now carries `?assignment=<id>`; the bench's own row keeps the bare address so
   existing bookmarks and `student_controls_drive`'s ruled expectation still
   hold.
2. **The assignment page always served the week's auto work.** It now honours
   `?assignment=<id>`, passing it through as `assignment_id`. Absent, the
   request is byte-identical to the one that went out before.

**The bench falls back.** It shows the auto assignment when there is one; when
there is not — a class with the switch off — it shows the earliest-due open
teacher-set assignment for the week. Without that, a class with automatic work
off would show an empty bench above a full work list, which reads as broken
rather than as configured.

The answer sink, the resume, the Complete model and the feedback view all key on
`assignment.id` and needed no change — confirmed by reading, not assumed. The
localStorage answer queue is already per-student **and** per-assignment
(`mrbadmusai.answerqueue.v1.<uid>.<assignment id>`), and the stored blob repeats
both ids and is discarded on a mismatch, so two assignments in one week cannot
collide.

No new render key and no new control were introduced, so the fixture payloads and
the control census are unchanged — `student_behaviour` stays at 100/100 against
Design's own files.

⚠️ **No platform self-explanation.** A child is never told what "teacher-set"
means. The work carries the teacher's own title, and that is the whole of the
difference they see. One honesty fix: the bench's blurb drops the clause "set
from this week's lessons" on the fallback path, because that is a fact about an
auto assignment and would be untrue of work whose lesson the teacher chose.

---

## 11 · Caught in review: the Swap control was dead on most rows

Worth writing down because it would have shipped, and because of *how* it
happened.

The sheet's question preview gives every row a **Swap**. Its first
implementation took "swap for another from the same lesson" from the brief
literally, which was correct when it was written. Unit A then changed the
selection underneath it, on my instruction (§7): one lesson cannot fill ten
questions, so the set fills backwards through the scheme.

Those two halves are inconsistent, and the inconsistency is invisible from
either side. Driven against the live backend on a real class:

| count | picked | pool | rows with a swap available |
|---|---|---|---|
| 6 | 6 | 314 | **2 of 6** |
| 10 | 10 | 310 | **2 of 10** |
| 15 | 15 | 305 | **3 of 15** |
| 20 | 20 | 300 | **0 of 20** |

The fill consumes a lesson's four questions *entirely* before moving to the next
lesson back, so the pool holds nothing for any fully-consumed lesson. At count
10 the picked set is `{chosen: 4, next back: 4, next: 2}` and the pool holds
`{0, 0, 2}` for those three. Only the partially-consumed final lesson can swap.

**A control that does nothing when pressed, on eight rows in ten — and on
twenty in twenty at the maximum count.** That is precisely what MRB-287's `DEAD`
ruling forbade. Restoring the sheet while re-committing its original sin would
have been the worst possible outcome of this ticket.

Fixed by making Swap draw from the drawn range — same lesson first, then the
nearest unused, the pool already being nearest-first — and by **putting each
question's lesson on its row**, which is the half that makes the fill visible
rather than hidden:

```js
const free = (s.swPool || []).filter(x => used.indexOf(x.id) < 0);
const alt  = free.filter(x => x.lesson_slug === q.lesson_slug)[0] || free[0];
```

The pool is ~300 questions against a picked set of at most 20, so `free` is
never empty on a real class and **every row is swappable at every count** —
measured on the closure lifted verbatim out of the built page, against the same
pool model that produced the table above:

| count | picked | pool | rows with a swap available |
|---|---|---|---|
| 6 | 6 | 314 | **6 of 6** |
| 10 | 10 | 310 | **10 of 10** |
| 15 | 15 | 305 | **15 of 15** |
| 20 | 20 | 300 | **20 of 20** | The
refusal survives for the genuinely-exhausted case and now says something true —
"Nothing left in the bank to swap in" — rather than the previous "No other
question from that lesson yet", whose "yet" implied a bank that grows.

⚠️ **`teacher_behaviour` could not have caught this.** It presses each
registered marker once and asks whether anything changed; one row's swap
working is enough to satisfy it. The property here is about the other nine rows,
so the proof is a count of available alternatives, not a press.

⊕ **My own fault as much as anyone's**: I ruled the fill change and did not tell
the unit that owned the swap.

---

## 12 · Fidelity: reconciling the sheet against Design's template

Design's Set-work sheet is at lines 889–968 of
`docs/ks3/design-reference/teacher/source/Teacher Dashboard.dc.html`; its
behaviour is in her script constants at 2046–2099 and `TOPICS` at 1092.

⚠️ **The comparison is against her SCRIPT, not her markup.** Her HTML carries
`hint-placeholder-count` stubs, not content; the constants are what she actually
specified. This is the method the estate already uses.

### What ships unchanged

| Design | Ships |
|---|---|
| Three steps, `swStep` 1–3 | unchanged |
| Eyebrow `'Step ' + n + ' of 3 · ' + [...][n-1]` | the sentence is unchanged; its three words are reordered — see divergence 6 |
| Topic rows: name, `unit` caption, right-aligned `tag` | unchanged |
| Footer summary + Back/Next, labels `Cancel`/`Back` and `Next`/`Set work` | unchanged |
| Due: five weekday chips Mon–Fri | unchanged |
| Step 3: multi-select class grid with the square checkbox | unchanged |
| Modal frame, 720px, `--st-*` tokens throughout | unchanged |

### Ruled divergences

| # | Design drew | Ships as | Why |
|---|---|---|---|
| 1 | question chips `[6, 10, 15]` | `[6, 10, 15, 20]`, default 10 | The brief sets the max at 20. One chip added to her row; her `flex:1` layout absorbs it at 720px and at 390px |
| 2 | a count, and **no questions** | the count, then the auto-selected questions with a **Swap** on each, and each question's lesson | *"Six, ten or fifteen questions, chosen by nobody the teacher can see, set to thirty children. That is acceptable in a sheet that sets nothing and is not acceptable in one that does."* The lesson caption is what makes the backward fill (§7) visible rather than hidden |
| 3 | release chips `Release now` / `Release next lesson` | `Release now` / `Release later` + a date | "Next lesson" cannot be resolved: the timetable is per-teacher (MRB-326), and a multi-class set has no single next lesson. A date can be resolved and is what the brief asks for |
| 4 | *(nothing)* | one line naming the school's go-live date, shown only when a hold is set and ahead | Without it a teacher sets work for Tuesday and cannot tell why the class does not have it. One sentence, in the footer, said once |
| 5 | *(nothing)* | the due chips resolve to a real date, shown beneath them | Her chips are weekdays; the brief's default is "next week, same weekday". The resolved date is the only way to tell which Wednesday |
| 6 | step order `['Topic','Detail','Classes']` | `['Classes','Topic','Detail']` | **Forced by real data, not chosen.** Design's topic list is a five-row constant, so it can be drawn before anything is known. A real one is *this class's* scheme of work — and the sheet also opens from `classes.html` (node 165), where no class is in the URL. Her step 1 cannot be drawn there at all. No panel is redrawn and no control moves; only which step number makes each `<if>` true |

### Withheld

**Node 382, "Reteach and reset"** — drawn by `openSetWork`, so restoring the sheet
would have restored it too. It stays `DEAD`: a Set-work sheet behind a button
labelled "Reteach and reset" lies about what the control does, which is a smaller
lie than MRB-287's but still one.

**Teacher-authored free-text questions** — v2 in the brief, and **not drawn as a
disabled control**. There is no greyed-out "write your own" anywhere on the sheet.

---

## 13 · The cold pass, and what it found

The diff was read end to end by a reviewer with none of this run's context,
instructed to be adversarial about authorisation, provenance, the release logic
and crashes. It found six real defects. Two are worth reading in full because of
what they say about the rest of this report.

### The one that falsified a claim I had already written

**`POST /api/teacher/set-work` was not all-or-nothing.** The route's own header
said *"IT REFUSES THE WHOLE REQUEST OR IT WRITES ALL OF IT."* Only
**authorisation** was pre-flighted. The hold resolution, the
`due_at > release_at` check and both inserts all happened **inside** the write
loop, with no transaction and no rollback of classes already written.

A deterministic scenario, needing no transient failure: a teacher who teaches in
two schools — B with no hold, A with a go-live date — posts both with a due date
of tomorrow. Class B is inserted and released. Class A returns
`400 bad_due_at`, naming class A. The teacher sees an error about a class they
did not think they were setting, retries with a later due date, and **class B
receives a second assignment** — because this very ticket narrowed
`assignments_class_week_uniq` to `source = 'auto'`, so nothing dedupes teacher
rows. The child's week then lists the same homework twice.

⚠️ **I had already written decision 9 — "a partial multi-class set is refused
whole" — on the strength of that header.** My drive tested the *authorisation*
refusal and proved it, which is why it read as covered. It was not. The claim was
false when I made it; the fix makes it true.

### The one whose reasoning was right and whose premise was wrong

`?assignment_id=` was placed ahead of the consumer branch, on the stated grounds
that it was "behaviourally identical today since no consumer flow passes it."
The consumer branch carries the only guard stopping a family child opening work
generated a week ahead (`consumer/work.js:1733`). The premise was wrong: the
**child** can pass it. `assignments_student_read` permits `release_at is null`,
consumer practice is written with a null release, and the student page already
holds direct PostgREST reads of `assignments` — so the child's own client
returns the row and its id.

### The rest

| # | Defect |
|---|---|
| 3 | The release gate was on one student-facing route out of five. The other four go through `studentAssignment()`, which runs on the **service-role** client, so neither the backend check nor the new RLS policies applied. Not currently reachable for teacher-set work — but "not reachable" is a statement about today, and defect 2 shows ids already leak for the null-release case |
| 4 | Five `callerClient()` call sites left unwrapped, against the commit's own instruction. Verified empirically on this repo's express 4.22.1 / node 24: an async handler that throws produces no response, no error middleware is registered anywhere, and the process terminates |
| 5 | The write accepted a scheme row the preview refuses (null `subtopic`), storing work that the "last set" logic then never reports as set |
| 6 | Both audit writes were wrapped in a `try/catch` that can never fire — `supabase…insert()` resolves with `{ error }`, it does not reject, so an audit failure was discarded with no row and no log line |
| 7 | A dead filter that reads as a guard (`q.band !== band`, always false — `bankFor` already filters by band) |

### What it could not break

Authorisation — `setWorkAccess` sound, every id re-derived server-side,
`sowMatchesClass` applied to **every** class rather than the first. Question
provenance — the key-stage seal held at all four call sites. The DST arithmetic.
And the `source = 'auto'` sweep: every week-scoped lookup in the estate
enumerated, none missed.

**The lesson worth keeping:** the drive proved the properties it was written to
prove, and each of those proofs is sound. Six defects sat in the space between
them, and four were in code paths the drive never entered. A green gate is
evidence about what it watches, and nothing at all about what it does not.

---

## 14 · Gates

| Gate | Result |
|---|---|
| `set_work_drive.py` (new) | **54 checks, 0 failed**, three consecutive runs, real JWTs under real RLS |
| `teacher_behaviour.py` (dead-control) | **PASS** — 24 fixtures, 880 controls pressed; `setwork-swap`, `setwork-release-date` and `auto-assignments` pressed by name |
| `teacher_reach.py` (390px + 360px) | **PASS** — 24 fixtures × 2 widths, 3,436 controls hit-tested at their own centre, 1,894 presses, nothing out of reach, no sideways scroll |
| `teacher_tells.py` | **PASS** — none of Design's five invented topics reaches a built page |
| `student_behaviour.py` | **PASS** — 100/100 against Design's own files |
| `pool_ownership.py` | **PASS** — extended, and all three new checks mutation-tested red first |
| `gate_registry.py --check` | **PASS** — 39 gates over 39 scripts |
| backend `test_assignment_compose.js` | **51 passed** |
| backend `test_generate_week_guard.js` | **16 passed** |

⚠️ **`teacher_behaviour` presses each registered control once.** That is what it
is for, and it is why §11's dead-Swap defect was invisible to it: one row's swap
working satisfies the press. The property there was about the *other nine rows*,
and the proof was a count of available alternatives, not a press. A gate is
evidence about what it watches.

### The dead-control gate had to be taught to reach the sheet

Its `OPENERS` map held one template index per marker — enough for a control one
press behind one of Design's nodes. The sheet's controls sit **three panels
deep**, behind open-then-Next-then-Next, on two screens that open it from two
different nodes. `OPENERS` now takes a *chain*, pressed in order, re-querying the
DOM at every step — because the page is rebuilt wholesale on every `setState`, so
a handle taken before the first press is stale by the second.

### All six fixed, and how

Committed as `2bd513d`, *"a partial set is refused whole, and unreleased work is
404 everywhere"*.

1. **The multi-class write is genuinely all-or-nothing.** Split into a
   **decision pre-flight** — hold, `release_at`, `academic_week` and the due-date
   check, per class, into `plans[]` — and a **write loop that can only insert**.
   Every refusal now sits at or before `plans.push`; the only returns after the
   loop opens are two 500s, each preceded by a `rollbackAll()` that deletes
   *every* assignment the request has created, not just the current one, and
   logs loudly if a rollback delete itself fails.
2. **`?assignment_id=` moved below the consumer branch** — consumer, then
   `assignment_id`, then compose, with the ordering's load-bearingness written
   down, and the original reasoning corrected: it was about our pages, not the
   child's client.
3. **The release gate moved into `studentAssignment()`**, so all four callers
   inherit it. A detail worth keeping: no teacher path reaches that helper at
   all — every caller requires class *membership* — so teachers read unreleased
   work through `?assignment_id=`, which permits it explicitly.
4. **`callerRpc(req, fn, args)`** — the shape-over-instruction option: it
   *cannot* throw and returns `{data, error}`, which every one of the seven
   sites already handled. Six `.rpc` sites plus `callerStanding` converted; the
   one `.from()` chain catches around itself. Plus a process-level
   `unhandledRejection` net, after empirically confirming on this repo's own
   express/node that an async handler throw produces no response and terminates
   the process.
5–7. The write mirrors the preview's `!sow.subtopic` refusal; both audit writes
   read `{ error }`; the dead band filter is gone.

Verified by a **94-check** drive on TEST covering each finding, including the
positive control for #1 — the *same* two-class request succeeds on both classes
once the hold is lifted, proving the refusal was the hold and not the shape.

⚠️ **A note on the earlier drive failures.** Six checks failed in an
intermediate run for a reason that was not the product: the throwaway school was
deleted mid-run by a concurrent session, and the classes it fell back to sit in
the **2025-26** academic year, which ended 31 August 2026 — so
`currentTeachingWeek()` returns null and every week-scoped assertion collapses
into `no_current_week`. Both drives now build and remove their own worlds. It is
the same trap §2 of the plan named for Rainford, met a second time from the
other direction.

---

## 15 · The sheet, paired

Captured from `teacher_fixtures/class-detail-fixture.html` — the driven twin of
the live `teacher/class-detail.html`, so this is the shipped markup and the
shipped logic, on the fixture's data rather than a school's.

Each step at 1460 and at 390, which is the width `teacher_reach` hit-tests.

| | desktop | phone |
|---|---|---|
| The class screen's action row, with **Set work** restored and the toggle beside it | [`class-detail-actions-desk.png`](shots/class-detail-actions-desk.png) | |
| **Step 1 · Classes** — multi-select, Design's checkbox grid | [`sheet-1-classes-desk.png`](shots/sheet-1-classes-desk.png) | [`sheet-1-classes-phone.png`](shots/sheet-1-classes-phone.png) |
| **Step 2 · Topic** — this class's own scheme | [`sheet-2-topic-desk.png`](shots/sheet-2-topic-desk.png) | [`sheet-2-topic-phone.png`](shots/sheet-2-topic-phone.png) |
| **Step 3 · Detail** — count, question preview, due, release | [`sheet-3-detail-desk.png`](shots/sheet-3-detail-desk.png) | [`sheet-3-detail-phone.png`](shots/sheet-3-detail-phone.png) |

**Step 3 is where every ruled divergence is visible at once**: the fourth
question chip (`20 Q`) that Design did not draw, `10 Q` selected as the default,
the question preview underneath it with each question's **lesson** in the caption
face and a **Swap** on every row, and the due-day chips below. Design's step 2
showed a count and no questions at all.

At 390 the chips wrap rather than overflow, the question stems truncate to one
line, and every Swap stays hit-testable — which is `teacher_reach`'s 3,436-control
pass, seen rather than asserted.

⚠️ **These are ours, not a Design-vs-ours pair.** Design's teacher delivery is a
`.dc.html` that needs her own compiler and runtime to render, so a side-by-side
photograph is not available the way it is for the student pages. The fidelity
comparison in §12 is made against her SCRIPT CONSTANTS instead — her `swCounts`,
her `swRelease`, her eyebrow expression — which is the stricter comparison
anyway, and the one this estate already uses.

⊕ Worth recording, because it nearly produced three misleading screenshots: the
capture's first pass searched for a control whose label *contained* "Set work",
and step 3's confirm button is also labelled "Set work" — so every "advance"
re-opened the sheet at step 1, and all three files showed the same panel. The
capture now matches labels EXACTLY and takes the last match.
