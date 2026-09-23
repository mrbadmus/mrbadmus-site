-- MRB-342.2 — a teacher can put a short note on a set, and the pupil reads it.
--
-- A teacher setting work wants to say one line to the class: who set it, that
-- they are on cover this week, "do the first ten in class and the rest at home".
-- Today there is nowhere to put that. The title is the topic and the pupil's
-- assignment page has no teacher voice on it at all.
--
-- ⚠️ ONE COLUMN, and deliberately not a reuse. `assignments.instructions`
-- already exists and is text and is nullable and would have fit. It is READ by
-- `readAssignmentWithQuestions()` (server.js line 1133) and WRITTEN by nothing
-- — in the whole backend there is not one insert or update that sets it. A
-- column that is read-but-never-written is not a free home: the next person to
-- find it has to work out which of the two meanings a row carries, and there is
-- no way to tell a note the teacher typed from an instruction some earlier
-- producer left behind. A named column says what it is.
--
-- ⚠️ NO RLS CHANGE IS NEEDED, AND THAT IS WORTH STATING RATHER THAN ASSUMING.
-- `assignments_select_merged` already lets a class member read an assignment
-- when `release_at is null or release_at <= now()` and `deleted_at is null`.
-- A new column on the row inherits that, so:
--   · the note is visible to the pupils of that class and to nobody else's;
--   · a note on an UNRELEASED set is not readable early — the release gate is
--     the same gate that hides the questions;
--   · there are no column-level grants on this table, so the new column
--     inherits the table's grants rather than needing its own.
-- If any of those three stops being true, this column leaks.

-- ── the column ────────────────────────────────────────────────────────
alter table public.assignments
  add column if not exists teacher_note text;

-- ⚠️ The bound is 300 characters, and it lives HERE as well as in the backend
-- on purpose. The backend normalises whitespace and then refuses anything
-- longer; normalisation can only shorten, so a value the backend accepts can
-- never fail this check. The constraint is not there to catch the backend — it
-- is there to catch the NEXT writer, which on past form is a script someone
-- runs once at half past eleven.
--
-- ⚠️ `char_length` counts CHARACTERS, not bytes and not UTF-16 code units, so
-- 300 emoji pass. JavaScript's `.length` counts code units and would call the
-- same string 600. The backend therefore counts CODE POINTS, so that the two
-- bounds mean the same thing and a teacher's character counter is not lying to
-- them. The direction of any residual disagreement is deliberately safe: JS
-- over-counting refuses early rather than producing a row the database rejects.
--
-- `teacher_note <> ''` is the other half of the same thought: "no note" has one
-- spelling, and it is NULL. An empty string would read as a note that renders
-- as a blank line above a child's homework.
alter table public.assignments
  drop constraint if exists assignments_teacher_note_check;
alter table public.assignments
  add constraint assignments_teacher_note_check
  check (teacher_note is null
         or (teacher_note <> '' and char_length(teacher_note) <= 300));

comment on column public.assignments.teacher_note is
  'MRB-342.2 · a teacher''s short plain-text note on this set, shown to the '
  'pupil at the top of the assignment. Plain text, never markup: escaped at '
  'every surface it renders on. At most 300 characters after whitespace '
  'normalisation. NULL means no note; '''' is refused by '
  'assignments_teacher_note_check.';
