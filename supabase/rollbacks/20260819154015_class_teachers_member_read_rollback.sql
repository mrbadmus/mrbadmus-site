-- Undo for 20260819154015_class_teachers_member_read.sql (MRB-265).
--
-- ⚠️ APPLY MANUALLY ONLY. The Supabase CLI never reads this folder.
--
-- Dropping this policy makes `class_teachers` unreadable to students again,
-- which will blank the teacher pill and the teacher chip on the student class
-- page. It does NOT restore the class-name parse that used to stand in for it —
-- that was deleted in the same unit, so a rollback here needs the frontend
-- reverted alongside it or the teacher's name simply disappears.

drop policy if exists class_teachers_member_read on public.class_teachers;
