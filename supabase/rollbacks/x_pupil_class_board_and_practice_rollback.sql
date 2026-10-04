-- Rollback for 20261004120000_x_pupil_class_board_and_practice.sql
-- (Prompt X / SPEC-C). Apply by hand. The Supabase CLI never reads this
-- folder.
--
-- ⚠️ LOSSY IF ANY PRACTICE ROUND HAS BEEN RECORDED. Dropping the table
-- discards every row. Check first:
--
--   select count(*) from public.practice_rounds;
--
-- A non-zero answer means real pupils have completed real rounds and
-- those counts will be lost permanently. Confirm that is really wanted
-- before running this against any project pupils are using.
--
-- `class_stars_leaderboard_for_member` is restored to the body it had in
-- supabase/migrations/20260524225500_class_stars_leaderboard_for_member.sql
-- — the PRE-this-migration week rule (due_at window, on-time required a
-- lower bound). Re-run that migration's CREATE OR REPLACE to go back to
-- it; it is not repeated here to avoid two copies of the same function
-- body drifting apart.

BEGIN;

DROP POLICY IF EXISTS practice_rounds_select ON public.practice_rounds;
DROP TABLE IF EXISTS public.practice_rounds;

-- The top-five board (Mide, 4 Oct 2026). Same signature before and after the
-- rework, so one DROP undoes either version; nothing else depends on it.
-- The page soft-fails to its empty board the moment the function is gone.
DROP FUNCTION IF EXISTS public.class_stars_board_for_member(uuid);

-- class_stars_leaderboard_for_member is NOT dropped here — re-apply
-- 20260524225500_class_stars_leaderboard_for_member.sql's CREATE OR
-- REPLACE to restore its pre-migration body.

DROP FUNCTION IF EXISTS public._mrb_week_number(date, timestamptz);

COMMIT;

-- After running the above, also re-run (manually, via the SQL editor)
-- the CREATE OR REPLACE FUNCTION block from
-- supabase/migrations/20260524225500_class_stars_leaderboard_for_member.sql
-- to put class_stars_leaderboard_for_member back to its original body.
-- Then delete the forward migration's row from the registry:
--
--   DELETE FROM supabase_migrations.schema_migrations
--     WHERE version = '20261004120000';
