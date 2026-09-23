-- ROLLBACK for MRB-342.2 — `assignments.teacher_note`.
--
-- Apply MANUALLY only. The Supabase CLI never reads `supabase/rollbacks/`.
--
-- ⚠️ THIS DESTROYS EVERY NOTE A TEACHER HAS TYPED. Dropping the column drops
-- the data in it, and there is no other copy — the note is not in the audit
-- log (MRB-342.2 audits `note_present`, a boolean, precisely because a note may
-- carry a personal line). If any set has been written since the forward
-- migration went on, take a copy first:
--
--   create table if not exists public.assignments_teacher_note_backup as
--     select id, teacher_note from public.assignments where teacher_note is not null;
--
-- The backend is written to work in BOTH states — it probes for the column and
-- the sheet hides the field when it is absent — so dropping this column does
-- not break setting work, does not break the pupil's assignment page, and does
-- not need a code deploy to accompany it. That is the whole reason it was built
-- that way, and it is what makes this rollback safe to reach for.

alter table public.assignments
  drop constraint if exists assignments_teacher_note_check;

alter table public.assignments
  drop column if exists teacher_note;
