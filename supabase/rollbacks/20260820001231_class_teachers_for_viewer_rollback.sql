-- Rollback for 20260820001231_class_teachers_for_viewer.
-- Apply MANUALLY. The CLI never reads this folder.
--
-- Nothing depended on this function before it existed, so dropping it is safe;
-- the class view's teacher chip falls back to its empty state.

DROP FUNCTION IF EXISTS public.class_teachers_for_viewer(uuid);
