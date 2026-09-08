-- ROLLBACK for 20260908065322_mrb336_assignment_delete_and_message_reads
--
-- Apply MANUALLY only (psql or the SQL editor). The CLI never reads this folder.
--
-- ⚠️ ORDER MATTERS AND SO DOES WHAT IS *NOT* HERE. This restores the two RLS
-- policies to their pre-MRB-336 text FIRST, because those are the only part of
-- the migration that changes what a live pupil can read; the table and column
-- drops are cosmetic by comparison and can wait a minute.
--
-- ⚠️ DROPPING `deleted_by` AND `student_message_reads` DESTROYS DATA. If
-- anything has already been deleted through `DELETE /api/teacher/set-work/:id`,
-- the name against that act is gone for good and only the `assignment.deleted`
-- audit row remains — which is why the audit row carries the actor rather than
-- pointing at this column. If any pupil has ticked a message off their bell,
-- those marks are gone and the bell will re-light. Neither is recoverable.
-- Take the two lines out and leave the column and table in place if you are
-- rolling back the ROUTES only; both are additive and inert with no code
-- reading them.

begin;

-- ── 1. the two student-read policies, back to their MRB-335 text ────
--
-- Verbatim pre-images, transcribed from `pg_policies` before the migration ran.
drop policy if exists assignments_student_read on public.assignments;
create policy assignments_student_read
  on public.assignments
  for select
  using (
    (class_school_id(class_id) = auth_user_school_id())
    AND auth_user_is_member_of_class(class_id)
    AND ((release_at IS NULL) OR (release_at <= now()))
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
    )
  );

-- ── 2. the read markers (DESTRUCTIVE — see the note above) ──────────
drop table if exists public.student_message_reads;

-- ── 3. who deleted it (DESTRUCTIVE — see the note above) ────────────
alter table public.assignments drop column if exists deleted_by;

commit;

-- The CLI's ledger, so `supabase migration list` stops claiming this is applied.
delete from supabase_migrations.schema_migrations where version = '20260908065322';
