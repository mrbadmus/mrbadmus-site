-- ═══════════════════════════════════════════════════════════════════════
-- ROLLBACK for 20260906054837_mrb326_admin_write_authority.sql
-- ═══════════════════════════════════════════════════════════════════════
--
-- Apply MANUALLY only. The Supabase CLI never reads `supabase/rollbacks/`,
-- so this file cannot be picked up by `db push` — that is the whole point of
-- the folder.
--
-- Drops all seven policies the migration creates and NOTHING ELSE. Every
-- teacher-facing policy on these four tables is untouched, because the
-- migration never modified one: it added siblings. So running this returns
-- the estate to exactly the pre-MRB-326 position — an admin can still open a
-- foreign class (that is MRB-325's frontend change and needs no policy) and
-- is once again refused on every write in it.
--
-- ⚠️ `class_shoutouts_admin_read` is dropped along with the rest. If the
-- ad-hoc widening of `class_shoutouts_select` seen on TEST is ever applied
-- to production, an admin keeps read there through THAT policy — this file
-- is not the thing standing between an admin and a shoutout list, and
-- should not be edited to become it.
-- ═══════════════════════════════════════════════════════════════════════

drop policy if exists submissions_admin_write            on public.assignment_submissions;
drop policy if exists class_shoutouts_admin_read         on public.class_shoutouts;
drop policy if exists class_shoutouts_admin_insert       on public.class_shoutouts;
drop policy if exists class_shoutouts_admin_update       on public.class_shoutouts;
drop policy if exists submission_feedback_admin_insert   on public.submission_feedback;
drop policy if exists submission_feedback_admin_update   on public.submission_feedback;
drop policy if exists student_notifications_admin_send   on public.student_notifications;
