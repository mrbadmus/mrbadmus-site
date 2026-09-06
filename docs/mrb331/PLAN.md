# MRB-331 SET WORK v1 — the build, as decided

## The reversal this run performs

Design drew the Set work sheet. `teacher_rulings.DEAD` prunes it from all six
generated teacher pages, under **MRB-287**:

> Creating an assignment HAS NO WRITE PATH ... So Design's three-step "Set
> work" sheet is a sheet that would collect a topic, a question count, a due
> day and a class list, press a button, show a toast saying the work had been
> set, and set nothing. That is not an unfinished feature — it is a control
> that LIES, and MRB-287 forbids it outright.

MRB-331 builds the write path, so the ruling's premise stops being true and the
sheet comes back. The manoeuvre has a precedent in the same file: MRB-326 JOB 4c
took node 236 off `DEAD` the same way, and kept the superseded row as a comment
so re-adding it could not silently delete a working control.

⚠️ The brief says the button was "withheld in MRB-325". It was not. MRB-325
ruling 1 (restated as MRB-326 ruling 4) is why `teacher/today.html` has no Set
work button; `DEAD` under MRB-287 is why the six generated pages have none.
Both are reversed here; only the second is a `teacher_rulings.py` edit.

## Six nodes, five restored

| node | what | verdict |
|---|---|---|
| 581 | the Set-work sheet itself | RESTORE |
| 165 | "Set work", classes screen primary | RESTORE |
| 214 | "Set work", class screen primary | RESTORE |
| 282 | "Set work", the no-work empty state | RESTORE |
| 194 | "Set work" on a class card with students but no work | RESTORE |
| 382 | **"Reteach and reset"**, marking screen header | **STAYS DEAD** |

382 is drawn by `openSetWork` but is LABELLED "Reteach and reset". Opening a
Set work sheet from it would still lie — about what the control does rather
than about whether it does anything. Reteach-and-reset is a different feature
and is not in this ticket. Recorded as a decision, not an oversight.

## Where the sheet's data comes from — the backend, and why

`pool_ownership.check_other_surfaces()` fails on the mere PRESENCE of the
string `ks3_assignment_bank` in `shared/teacher-live.js` or
`shared/teacher-data.js`, comment or not. Three ways out were available:

1. put the read in a new `shared/*.js` the gate does not scan — rejected. That
   is widening a gate by naming rather than by decision, and it is exactly the
   shape of "how gates stop watching".
2. widen the gate's `others` list deliberately — rejected. It would let a
   teacher surface select `text`/`options` client-side, which is the thing the
   student-side half of the same gate exists to forbid.
3. **route it through the backend** — chosen. The gate's own closing note says
   so: *"If the new surface actually SERVES bank questions to a user, the
   honest move is to route it through backend composition (the ruled owner
   path)."*

It is also the shape MRB-324 already established for a teacher write control:
`assignments_hold_drive.py`'s primary assertion is that the hold control must
never become a direct database write, because `schools_admin_update` carries no
column list and an SLT user's direct write matches zero rows and returns a
cheerful 200. `assignments_teacher_write` has the same shape — `FOR ALL`, USING
only. Handing the browser an assignment INSERT would hand it every column.

So: the bank stays behind `bankFor()`, the hold stays resolved server-side next
to the `schools` read that already exists, and `pool_ownership.py` is EXTENDED
to name the new backend reads rather than left to not-notice them.

## Data model as built

`assignments` gains — migration `20260906144742`:
- `source text not null default 'auto'`, CHECK in ('auto','teacher'), tied to
  `auto_generated` by `assignments_source_agrees_with_auto_generated` so the
  two can never drift.
- `set_by uuid references profiles(id)` — the author. NOT `teacher_id`, which
  on an auto row is whichever teacher `classSubjectId()` happened to find.
- `release_at timestamptz` — NULL means already released, which every existing
  row is.
- `assignments_class_week_uniq` narrowed with `and source = 'auto'`.
- `classes.auto_assignments boolean not null default true`.

The **lesson ref** needs no new column: `assignments.subtopic` is exactly it.
`scheme_of_work_entries.subtopic` IS the lesson slug and is the whole join to
`ks3_assignment_bank.lesson_slug`; the auto producer writes `subtopic: null`,
so there is no collision. `source_sow_entry_id` is also set — the teacher picks
a real scheme row, so the provenance is real.

Migration `20260906145023` puts the release in RLS on `assignments_student_read`
and `aq_student_read`.

## The hold, resolved once at set time

`release_at = greatest(what the teacher chose, schools.assignments_open_from)`,
computed when the work is SET and stored.

Not computed at read time, deliberately. MRB-324 ruled that the hold governs
CREATION and never retracts: Rainford's two pre-term assignments keep being
served, hold or no hold. A read-time `greatest()` would mean moving the hold
later retracts work a class can already see — the exact behaviour that ruling
forbids. Baking it keeps "a hold moved later never retracts" true for
teacher-set work too.

Auto work needs nothing new here: it is already held at creation by the branch
at `server.js:1077`.

## The change that can break a live read

`/api/class/current-assignment` finds the week's work with
`.eq('class_id').eq('academic_week').maybeSingle()`. The moment a class holds
an auto AND a teacher-set assignment in one week — the point of the ticket —
that returns two rows and errors for every student in the class.

Three lookups gain `.eq('source','auto')`: `server.js:1047`, `:1175`, `:3527`.

## KS4 — what is actually possible

There is no KS4 question pool. Measured:
- `ks3_assignment_bank` is the only bank (2,220 rows, units B1–P12).
- `exam_questions` holds 41 KS4 rows, `source` in ('code_seed','bonding_v2'),
  zero `unit_code`, extended-response with mark schemes.
- `assignment_questions.one_pool_per_assignment` CHECK requires `band NOT NULL`,
  which structurally refuses an exam question.
- `consumer/work.js:484` already says it: `return { skipped: 'no_ks4_bank' }`.
- `generate_site_v5.py:773` says it: "THERE IS NO KS4 PROGRESS MODEL."

What KS4 DOES have is the scheme: 865 `scheme_of_work_entries` rows across
Y10/Y11, fully scoped by tier × pathway (Foundation Combined 83, Higher Triple
132 — the difference IS the triple-only content).

So the KS4 half of this build is: the picker works and is correctly scoped, and
the sheet REFUSES to set with a named honest state rather than creating empty
work. The backend's own stance, at `server.js:1194`: *"An assignment with no
questions is worse than none: the page would show an empty piece of work that
can be handed in."*

The KS4 gate proves the scoping and the refusal, not a KS4 composition.

## Units

- **A — backend + migrations.** The three `source='auto'` filters, the
  auto-assignments skip, four new routes, the by-id assignment read.
- **B — the teacher port.** `DEAD` −5, `DROP_KEYS` restored, the sheet's new
  steps, `teacher-live.js` supplying `TOPICS` and the rest.
- **C — the student side.** Teacher-set work is already listed by title (the
  work row reads `assignments.title` and RLS now gates release); what is
  missing is that only the current auto assignment is OPENABLE.
- **D — gates.** New drive, `pool_ownership` extension, the dead-control gate
  extended to the sheet, 390px.

## ⚠️ Found while seeding: the KS4/KS3 lesson-slug collision

`bankFor()` joins `ks3_assignment_bank` on `lesson_slug` alone. That table has
no `key_stage` column — only its NAME says KS3. Eight KS4 subtopic slugs in
`scheme_of_work_entries` are byte-identical to KS3 lesson slugs, 12 bank rows
each:

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
years too easy, and nothing says so.

**It is dormant today** only because production has no KS4 scheme rows and KS4
assignments are never composed. **MRB-331 would have activated it**: the topics
route would report `available: 12` on those eight, and the preview and the write
would have served and stored them — which would ALSO have made this run's "KS4
has no bank, so the sheet refuses" claim quietly false on exactly eight rows.

Fixed here rather than filed: key stage becomes a precondition of touching the
bank at all, mirroring `consumer/work.js:484`'s existing
`if (child.key_stage !== 'KS3') return { skipped: 'no_ks4_bank' }`. The seal
that matters is on the WRITE — `questions_not_in_lesson` alone would have
passed these, because the ids genuinely ARE in the lesson by slug.

## ⚠️ OPEN ON MIDE — `SUPABASE_ANON_KEY` may be unset on Render

Found because MRB-331's routes reuse the estate's standing-check pattern.

`callerClient(req)` (`server.js:4980`) builds a Supabase client from
`process.env.SUPABASE_ANON_KEY` and runs the caller's own JWT through
`auth_user_has_scope(...)`, so the database's predicate — not a re-implementation
of it — decides who is a school admin. That is the right design and it is the
one MRB-324 already shipped: `/api/admin/school/assignments-open-from` uses it
identically at `server.js:3013`.

**The variable is not in the backend repo's `.env`.** It holds only `PORT`,
`STRIPE_SECRET_KEY`, `SUPABASE_SERVICE_ROLE_KEY` and `SUPABASE_URL`. The
codebase already knows the variable can be missing — `server.js:5603` logs
*"SUPABASE_ANON_KEY is not set — child login cannot work"* — but `callerClient`
does not check: `createClient` throws "supabaseKey is required" synchronously,
inside an async route handler, with nothing catching it, and **node exits**.

So if it is also unset on Render, then today, before any of this ticket:

- a school admin pressing Save on the assignments start date takes the whole
  backend down for every user, rather than seeing an error;
- MRB-324's hold control has never worked in production.

MRB-331 does not introduce this and does not depend on the answer — it fixes
the crash (a missing configuration value degrades a REQUEST, never the server)
and widens the pattern to four more routes. But whether the variable is set is
a question only the Render dashboard can answer.

**The check:** Render → the backend service → Environment. If
`SUPABASE_ANON_KEY` is absent, add it (the TEST/production publishable key —
anon keys are designed to be public and one is already hardcoded in
`shared/config.js`). It is not a secret; it is a missing setting.
