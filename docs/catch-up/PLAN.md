# Catch-up — build contract (14 Oct 2026, feat/catch-up)

Mide, 9 Oct: "we can set work for a specific student or one or two specific
students in class … if they have access to the lesson already that's directed
for them, then they will know what to do … embedding would be better."
Mide, 13 Oct: **the TEACHER picks the lesson.**

A catch-up is a lesson plus questions set to one or more NAMED pupils of a
class. It is an ordinary `assignments` row — same pipeline as homework
(assignment_questions, assignment_submissions, /api/assignment/answer and
/complete) — distinguished by ONE new column.

## 1. Data (migration parked on `feat/catch-up-migration`, applied to TEST)

- `assignments.recipient_ids uuid[]` — **NULL = whole class** (every existing
  row). Non-empty array = a catch-up for exactly those pupils (profiles.id).
  CHECK 1..60 entries.
- A catch-up row is `kind='mcq_set'`, `source='teacher'`, `quiz_type='subtopic_quiz'`,
  `scope_kind='subtopic'`, `scope_ref` = **the lesson** (KS3 lesson slug /
  KS4 subtopic slug). The lesson IS the scope: no lesson column exists.
  `scope_kind`/`scope_ref` were made for Set work v2 (MRB-335), not for this;
  a catch-up simply uses them as a subtopic-scoped set.
- RLS: restrictive SELECT policy `assignments_catch_up_audience` — a pupil who
  is a member of the class sees a catch-up only if named. Proven on TEST by
  impersonation: recipient 1/1, classmate 0/0 (assignment and its questions),
  teacher 1/1.
- SECURITY DEFINER functions now skip catch-ups: `class_stars_board_for_member`,
  `class_stars_leaderboard_for_member`, `teacher_class_rollup_v2`
  (`AND a.recipient_ids IS NULL`).
- ⚠️ **The column is NOT on production until Mide says yes.** Every reader
  must PROBE for it (copy `assignmentNoteSupported` server.js / the
  `submissionRevealColsSupported` pattern in shared/breakdown.js: `select
  recipient_ids limit 0`; cache `false` ONLY on 42703/PGRST204; re-probe on
  anything else). Absent column ⇒ nothing is a catch-up, the Catch-up chip is
  hidden, and every page behaves exactly as today. Never name the column in a
  query the probe has not cleared.

The audience rule, everywhere (one helper per codebase):
`applies(row, pupilId) = !row.recipient_ids || row.recipient_ids.includes(pupilId)`
and `isCatchUp(row) = Array.isArray(row.recipient_ids) && row.recipient_ids.length > 0`.

## 2. Backend (mrbadmus---backend, branch feat/catch-up)

1. `catchUpSupported()` probe.
2. `GET /api/teacher/set-work/scope` adds `catch_up: { supported, pupils:[{id,
   first_name, last_name}], current_topic: {kind, ref, name} | null }`.
   `pupils` = the class's active roster. `current_topic` = the most truthful
   "what is this class on now": the scheme-of-work entry for the current
   academic week if the class has one, else the topic of the most recent
   whole-class set, else null.
3. `POST /api/teacher/set-work` accepts optional `pupil_ids` (1..10 uuids).
   With it: column must be supported (else 409 `catch_up_unavailable`),
   exactly one class, exactly one scope with `scope_kind='subtopic'`, every
   pupil an active member (else 400 `pupils_not_in_class`); writes
   `recipient_ids`. Everything else (pool check, due/release, academic week,
   audit, replay guard) unchanged. Audit payload gains `pupil_ids`.
4. Every service-role read that hands work to a PUPIL applies the audience
   rule: `weekWorkFor`, `/api/class/current-assignment` (`?assignment_id=` →
   404 for a non-recipient), `studentAssignment` (progress / answer /
   complete / assignment-submit → 404), `/api/student/notifications`,
   `/api/class/progress` (a catch-up lists only its recipients). Payloads
   given to a recipient carry `recipient_ids` (so the page can label it).
5. Class freshness (`teacherSetHistory`, `classSetHistory` and anything
   feeding `last_set_*` tags or "not set to this class this year") ignores
   catch-ups — one absent pupil's catch-up is not "the class did this topic".
6. PATCH / edit never drops `recipient_ids`.

## 3. Teacher site

- `shared/set-work.js`: a third type chip **Catch-up**, shown only when
  `/scope.catch_up.supported`. Steps: **Pupils** (tick one or more of this
  class; class is fixed) → **Lesson** (search box over every lesson the
  class's tree holds — KS3 units→lessons, KS4 topics→subtopics; the list
  starts filtered to `current_topic`, search reaches all) → **Questions**
  (exactly Set work's Detail: tier chips, preview, swap, count) + due date.
  Release is immediate. Title `Catch-up: <lesson name>`. POST as §2.3.
- Class page: catch-ups are split OUT of every class aggregate (completion,
  mean, matrix, roster, grid, digest, insights) — the JS twin of the rollup
  must agree with the SQL. In the week a catch-up was set, the week card
  shows **"Catch-up · N pupils"** ("1 pupil") with the lesson and each named
  pupil's result.
- `teacher/student-detail.html`: a pupil's own catch-ups show, labelled
  Catch-up; a catch-up for someone else never counts against them.
- Generated pages: `teacher/class-detail.html` etc. come from
  `build_teacher_port.py` + `teacher_rulings.py` — never hand-edit them.

## 4. Pupil site

- Labelled **Catch-up**, never Homework, everywhere it appears.
- Bench (the big card at the top), extending the live homework|flashcards split:
  | homework | flashcards | catch-up | bench |
  |---|---|---|---|
  | ✓ | – | ✓ | split: homework · catch-up |
  | ✓ | ✓ | ✓ | homework · flashcards; catch-up its own card directly below |
  | – | ✓ | ✓ | catch-up takes the homework half: catch-up · flashcards |
  | – | – | ✓ | catch-up fills the bench |
  Overdue unfinished catch-up behaves as overdue homework does.
- Opening a catch-up shows the lesson INSIDE the class page: a full-screen
  sheet under the pupil's own header on phones, a panel on desktop. v1 is a
  same-origin `<iframe>` of the existing lesson page with the lesson page's
  own chrome hidden by CSS injected from the parent (no lesson file is
  edited). A clear **Start the questions** goes to the questions
  (`student/assignment.html`, the normal pipeline); from the questions the
  pupil can reopen the lesson. Never a bare link out to the main site.
- Generated pages: `student/class.html`, `student/assignment.html` come from
  `build_student_port.py` + `student_rulings.py` + `shared/student-live.js`.

## 5. Out of bounds

Wrapped files (the Wrapped session excludes `recipient_ids IS NOT NULL` from
class totals itself), flashcard logic, lesson content, B2C. No production
writes. One build and one Chrome at a time.
