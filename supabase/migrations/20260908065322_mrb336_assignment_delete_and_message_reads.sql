-- MRB-336 / MRB-337 — a teacher can delete work, and a pupil has one bell.
--
-- Three things, and deliberately only three:
--
--   1. `assignments.deleted_by` — who soft-deleted a row. `deleted_at` has
--      existed since the table was written and the whole backend already
--      filters on it; what was missing was the name against the act.
--   2. `student_message_reads` — the read marker for the two message sources
--      that have none of their own.
--   3. Two STUDENT-facing RLS policies narrowed so that a soft-deleted
--      assignment is invisible at the DATABASE, not merely at the client.
--
-- ⚠️ NO NEW INDEX, ON PURPOSE. The obvious partial index over
-- (class_id, ...) WHERE deleted_at IS NULL already exists twice:
--   assignments_class_week_uniq   UNIQUE (class_id, academic_week)
--                                 WHERE deleted_at IS NULL
--                                   AND academic_week IS NOT NULL
--                                   AND source = 'auto'
--   assignments_class_release_idx        (class_id, release_at)
--                                 WHERE deleted_at IS NULL
-- The second serves the one genuinely NEW read this ticket adds — the bell's
-- "teacher work released to my classes" scan, which is class_id IN (…) AND
-- release_at <= now() AND deleted_at IS NULL — on exactly its leading columns.
-- A third index over the same ground would cost write throughput on every
-- assignment insert and buy nothing.

-- ── 1. who deleted it ───────────────────────────────────────────────
--
-- Nullable and unconstrained against `deleted_at`: rows soft-deleted before
-- today have a `deleted_at` and no `deleted_by`, and inventing an actor for
-- them would be worse than admitting we do not know. A CHECK tying the two
-- together would refuse those existing rows on the next UPDATE that touched
-- them.
alter table public.assignments
  add column if not exists deleted_by uuid references public.profiles(id);

comment on column public.assignments.deleted_by is
  'MRB-336: the profile that soft-deleted this assignment. NULL on rows deleted before 8 Sep 2026, and on rows that are not deleted at all.';

-- ── 2. the read marker for feedback and shoutouts ───────────────────
--
-- `student_notifications` carries its own `read_at`. `submission_feedback` and
-- `class_shoutouts` do not, and cannot easily be given one: both are written BY
-- a teacher and read BY a pupil, so a `read_at` on those rows would be a column
-- the author can write and the reader must write, on a table whose UPDATE
-- policy exists to stop the reader writing anything at all.
--
-- So the marker lives on its own table, keyed by (student, source, source_id),
-- owned entirely by the pupil. `source` is CHECKed rather than free text
-- because an unrecognised source is a row that can never be matched back to a
-- message and would sit there for ever.
--
-- ⚠️ 'reminder' IS NOT IN THE CHECK, AND THAT IS THE POINT. A reminder's read
-- state lives in `student_notifications.read_at` and nowhere else; letting one
-- be recorded here as well would create two answers to one question and a
-- first-writer-wins bug the day they disagree.
--
-- 'work' is the synthesised "your teacher set you something" entry — there is
-- no row behind it, so `source_id` is the ASSIGNMENT's id.
create table if not exists public.student_message_reads (
  student_id uuid not null references public.profiles(id) on delete cascade,
  source     text not null check (source in ('feedback', 'shoutout', 'work')),
  source_id  uuid not null,
  read_at    timestamptz not null default now(),
  primary key (student_id, source, source_id)
);

comment on table public.student_message_reads is
  'MRB-337: a pupil''s own read marks for message sources that carry no read_at of their own (submission_feedback, class_shoutouts, and the synthesised new-work entry). Reminders are NOT recorded here — student_notifications.read_at is their only marker.';

alter table public.student_message_reads enable row level security;

-- One policy, ALL, on the pupil's own id — the same shape as
-- `submissions_self_all` and `attempts_self_all`. There is nobody else who
-- needs to know what a child has ticked off: a teacher reads whether the work
-- was DONE, which is a submission, not whether the bell was cleared.
drop policy if exists student_message_reads_self_all on public.student_message_reads;
create policy student_message_reads_self_all
  on public.student_message_reads
  for all
  using (student_id = auth_user_id())
  with check (student_id = auth_user_id());

grant select, insert, update, delete on public.student_message_reads to authenticated;
grant select, insert, update, delete on public.student_message_reads to service_role;

-- ── 3. a deleted assignment is deleted AT THE DATABASE ──────────────
--
-- ⚠️ BOTH POLICIES ARE RE-CREATED FROM THEIR EXACT CURRENT TEXT PLUS ONE
-- CONJUNCT. Nothing else in either predicate is touched — not the school seal,
-- not the membership test, not the release gate, not the class_members
-- filters. Read the two `create policy` bodies against `pg_policies` before and
-- after: the only difference is `deleted_at IS NULL`.
--
-- Why it is needed: before MRB-336 nothing could soft-delete an assignment
-- through the product, so `deleted_at` was only ever set by hand and the gap
-- never showed. With a DELETE route live, a soft-deleted assignment would stay
-- readable by a pupil through a direct PostgREST read — the site's own client
-- happens to filter it, but a delete that depends on the client remembering to
-- filter is not a delete.
--
-- ⚠️ ONLY THE TWO STUDENT-FACING POLICIES ARE NARROWED, and the staff ones are
-- deliberately left alone. Two reasons, and the second is a trap:
--   • a teacher or admin SHOULD still be able to read a row they deleted —
--     that is the same ruling `class_shoutouts_select` already makes, where
--     the author keeps sight of their own deleted rows;
--   • `assignments_teacher_write` is a FOR ALL policy, and Postgres applies
--     the SELECT predicate to the POST-UPDATE row. Adding `deleted_at IS NULL`
--     to `assignments_teacher_read` would make the soft-delete UPDATE itself
--     fail 42501 for any caller under RLS — the exact information-leak guard
--     written up in CLAUDE.md's "RLS soft-delete gotcha".
--
-- MEASURED BEFORE APPLYING: production holds 5 assignment rows and none has
-- `deleted_at` set, so this narrowing retracts nothing any pupil can currently
-- see. It is a no-op on today's data and a seal on tomorrow's.

drop policy if exists assignments_student_read on public.assignments;
create policy assignments_student_read
  on public.assignments
  for select
  using (
    (class_school_id(class_id) = auth_user_school_id())
    AND auth_user_is_member_of_class(class_id)
    AND ((release_at IS NULL) OR (release_at <= now()))
    AND (deleted_at IS NULL)
  );

drop policy if exists aq_student_read on public.assignment_questions;
create policy aq_student_read
  on public.assignment_questions
  for select
  using (
    EXISTS (
      SELECT 1
        FROM assignments a
        JOIN class_members cm
          ON cm.class_id = a.class_id
         AND cm.left_at IS NULL
         AND cm.deleted_at IS NULL
       WHERE a.id = assignment_questions.assignment_id
         AND cm.student_id = auth_user_id()
         AND (a.release_at IS NULL OR a.release_at <= now())
         AND a.deleted_at IS NULL
    )
  );
