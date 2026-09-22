-- ROLLBACK for 20260922231500_mrb348_teacher_class_rollup
--
-- Apply MANUALLY only -- the Supabase CLI never reads supabase/rollbacks/.
--
-- Returns the database to EXACTLY the state 20260922114500 left it in:
-- `teacher_class_rollup` dropped, and `teacher_class_summaries(uuid[])`
-- recreated with the body and comment that migration created. The forward
-- migration does precisely two things -- it DROPs the older function and
-- CREATEs the newer one -- so this file does those two things backwards and
-- nothing else. It touches no table, no policy and no row of pupil data.
--
-- The function body below is a byte-for-byte copy of the CREATE statement in
-- `supabase/migrations/20260922114500_mrb348_teacher_class_summaries.sql`,
-- taken from that file rather than retyped. Its own header explains the
-- first-attempt rule, the float8-then-numeric rounding and the internal gate;
-- read it there, because this is a copy and that is the original.
--
-- ⚠️ NO GRANT OR REVOKE APPEARS BELOW, AND THAT IS DELIBERATE -- it is the
-- opposite of the MRB-336 precedent, so here is why. The house rule is that a
-- function rollback must re-state privileges, because CREATE OR REPLACE
-- resets them and a rollback that opens a hole is worse than the thing it
-- undoes. That rule exists for functions whose forward migration GRANTED
-- explicitly. Neither MRB-348 migration contains a single executable GRANT or
-- REVOKE: both rely on the estate's ALTER DEFAULT PRIVILEGES, which
-- materialise EXECUTE to PUBLIC (and to anon, authenticated, service_role) on
-- a freshly created function -- the same ACL every other definer function
-- here carries, and the one 20260922114500's header names. Adding explicit
-- grants would therefore leave a DIFFERENT ACL from the one 114500 leaves,
-- which is the one thing this file must not do. Proven on TEST by comparing
-- `pg_proc.proacl` after this rollback against `proacl` after applying the
-- real 20260922114500 -- identical. See docs/mrb348/teacher-aggregate.md.
--
-- ⚠️ ROLLING BACK PUTS THE SIX TEACHER SCREENS BACK ON THE UNBOUNDED READ.
-- `loadClassMatrices()` falls back to fetching every submission of every
-- assignment of every class the viewer touches when the function is absent --
-- that fallback was proven for real on TEST (MRB-348 round three, §4b), so
-- the screens keep WORKING; they simply get slow again, and get slower every
-- week of term. Nothing is lost and no pupil sees an error. Roll back only if
-- the aggregate is implicated in an actual incident.
--
-- ⚠️ THE REGISTRY VERSION MAY NOT BE THE FILENAME'S. Observed on TEST on
-- 22 Sep 2026: the rollup was applied through the MCP connector, which stamps
-- `schema_migrations` with ITS OWN timestamp -- the row there reads
-- `20260922175719 | mrb348_teacher_class_rollup`, not `20260922231500`. The
-- delete at the end of this file therefore matches on the name as well as the
-- canonical version, so it works whichever path applied the migration. It is
-- a no-op if no row matches.

begin;

drop function if exists public.teacher_class_rollup(uuid[], timestamptz, jsonb);

CREATE OR REPLACE FUNCTION public.teacher_class_summaries(p_class_ids uuid[])
RETURNS TABLE (
  class_id              uuid,
  active_member_count   int,
  assignment_count      int,
  submissions_completed int,
  completion_pct        int,
  class_mean            int,
  last_activity_at      timestamptz
)
LANGUAGE plpgsql
STABLE SECURITY DEFINER
SET search_path TO 'public'
AS $function$
DECLARE
  v_school   uuid;
  v_operator boolean;
  v_wide     boolean;   -- school_admin OR slt
  v_hod      boolean;
  v_now      timestamptz := now();
BEGIN
  IF p_class_ids IS NULL OR array_length(p_class_ids, 1) IS NULL THEN
    RETURN;
  END IF;

  v_school   := auth_user_school_id();
  v_operator := auth_user_operator_active();
  v_wide     := auth_user_has_scope('school_admin') OR auth_user_has_scope('slt');
  v_hod      := auth_user_has_scope('hod');

  RETURN QUERY
  WITH asked AS (
    SELECT DISTINCT unnest(p_class_ids) AS id
  ),
  visible AS (
    SELECT c.id,
           (v_operator
             OR (c.school_id = v_school
                 AND (v_wide OR v_hod OR auth_user_teaches_class(c.id))))  AS can_see,
           (v_operator
             OR (c.school_id = v_school
                 AND (v_wide OR auth_user_teaches_class(c.id))))           AS all_work
      FROM classes c
      JOIN asked a ON a.id = c.id
     WHERE c.deleted_at IS NULL
  ),
  cls AS (
    SELECT id, all_work FROM visible WHERE can_see
  ),
  mem AS (
    SELECT cm.class_id, COUNT(*)::int AS n
      FROM class_members cm
      JOIN cls ON cls.id = cm.class_id
      JOIN profiles p ON p.id = cm.student_id
     WHERE cm.deleted_at IS NULL
       AND cm.left_at   IS NULL
       AND p.deleted_at IS NULL
     GROUP BY cm.class_id
  ),
  asg AS (
    SELECT a.id, a.class_id, a.due_at
      FROM assignments a
      JOIN cls ON cls.id = a.class_id
     WHERE a.deleted_at IS NULL
       AND (cls.all_work
            OR (v_hod AND auth_user_is_hod_of_subject_dept(a.subject_id)))
  ),
  acount AS (
    SELECT asg.class_id, COUNT(*)::int AS n FROM asg GROUP BY asg.class_id
  ),
  first_attempts AS (
    SELECT DISTINCT ON (s.assignment_id, s.student_id)
           s.assignment_id, s.student_id, s.score, s.max_score,
           s.submitted_at, s.completed_at, s.status
      FROM assignment_submissions s
      JOIN asg ON asg.id = s.assignment_id
     WHERE s.deleted_at IS NULL
     ORDER BY s.assignment_id, s.student_id,
              COALESCE(s.attempts, 2147483647) ASC,
              COALESCE(s.submitted_at, 'infinity'::timestamptz) ASC,
              s.id ASC
  ),
  handed AS (
    SELECT asg.class_id,
           COUNT(*) FILTER (WHERE fa.submitted_at IS NOT NULL)::int AS n,
           MAX(fa.submitted_at)                                     AS last_at
      FROM asg
      JOIN first_attempts fa ON fa.assignment_id = asg.id
     GROUP BY asg.class_id
  ),
  -- One row per assignment: Σscore and Σmax over every first attempt that
  -- `cellOf` would have turned into a graded cell.
  per_assignment AS (
    SELECT asg.id, asg.class_id, asg.due_at,
           COALESCE(SUM(fa.score)     FILTER (WHERE graded), 0) AS tot,
           COALESCE(SUM(fa.max_score) FILTER (WHERE graded), 0) AS totmax
      FROM asg
      LEFT JOIN LATERAL (
        SELECT f.score, f.max_score,
               ((f.completed_at IS NOT NULL
                 OR f.submitted_at IS NOT NULL
                 OR f.status = 'complete')
                AND f.score     IS NOT NULL
                AND f.max_score IS NOT NULL
                AND f.max_score > 0) AS graded
          FROM first_attempts f
         WHERE f.assignment_id = asg.id
      ) fa ON TRUE
     GROUP BY asg.id, asg.class_id, asg.due_at
  ),
  marked_means AS (
    SELECT pa.class_id,
           round((((pa.tot)::float8 / (pa.totmax)::float8) * 100)::numeric)::int AS mean
      FROM per_assignment pa
     WHERE pa.due_at IS NOT NULL
       AND pa.due_at <= v_now
       AND pa.totmax > 0
  ),
  cmean AS (
    SELECT mm.class_id,
           round(((SUM(mm.mean))::float8 / (COUNT(*))::float8)::numeric)::int AS class_mean
      FROM marked_means mm
     GROUP BY mm.class_id
  )
  SELECT cls.id,
         COALESCE(mem.n, 0),
         COALESCE(acount.n, 0),
         COALESCE(handed.n, 0),
         CASE WHEN COALESCE(mem.n, 0) * COALESCE(acount.n, 0) = 0 THEN NULL
              ELSE round(((COALESCE(handed.n, 0))::float8
                          / ((mem.n * acount.n))::float8 * 100)::numeric)::int
         END,
         cmean.class_mean,
         handed.last_at
    FROM cls
    LEFT JOIN mem    ON mem.class_id    = cls.id
    LEFT JOIN acount ON acount.class_id = cls.id
    LEFT JOIN handed ON handed.class_id = cls.id
    LEFT JOIN cmean  ON cmean.class_id  = cls.id;
END;
$function$;

COMMENT ON FUNCTION public.teacher_class_summaries(uuid[]) IS
  'MRB-348 WS-2. Per-class summary numbers for the teacher summary screens, '
  'computed in SQL under the first-attempt rule (MRB-38). Gated internally '
  'on the same reader set the classes/class_members/assignments/'
  'assignment_submissions SELECT policies grant; unreadable class ids are '
  'dropped silently.';

commit;

-- Step 3 of supabase/rollbacks/README.md. Matches the canonical filename
-- version OR the migration name, because the two have been seen to differ
-- (see the registry warning in the header). No-op when neither is present.
delete from supabase_migrations.schema_migrations
 where version = '20260922231500'
    or name    = 'mrb348_teacher_class_rollup';
