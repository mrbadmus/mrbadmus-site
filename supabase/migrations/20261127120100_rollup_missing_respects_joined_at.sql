-- =====================================================================
-- teacher_class_rollup_v2: a pupil is never "missing" work that was set
-- before they joined the class.
--
-- The JS twin is `buildRoster` in shared/teacher-live.js (`setBeforeJoin`):
-- a CLOSED paper counts against a pupil only if it reached the class
-- (release_at, else created_at) at or after the pupil's joined_at in THIS
-- class. The two must never drift (teacher_rollup_equal).
--
-- One expression changes and nothing else. The function is far too long to
-- restate safely, so this edits its live definition in place and REFUSES if
-- the text it is replacing is not there exactly once — on a drifted project
-- it fails loudly instead of guessing.
--
-- Equivalence where nobody joined late: the old test was
-- `closed papers > closed cells`, i.e. "some closed paper has no cell for
-- this pupil" (first_attempts is one row per pupil per paper). The new one
-- is that EXISTS, minus papers set before the pupil joined.
-- Rollback: supabase/rollbacks/20261127120100_rollup_missing_respects_joined_at_rollback.sql
-- =====================================================================
do $migrate$
declare
  v_def  text;
  v_old  text := $o$'missing_marked', (COALESCE(cc.n, 0) > ps.closed_cells)$o$;
  v_new  text := $n$'missing_marked', EXISTS (
               SELECT 1
                 FROM per_paper pp2
                 JOIN assignments ax ON ax.id = pp2.assignment_id
                WHERE pp2.class_id = ps.class_id
                  AND pp2.closed
                  -- work set before this pupil joined is not theirs to miss
                  AND NOT EXISTS (
                        SELECT 1 FROM class_members cmj
                         WHERE cmj.class_id   = ps.class_id
                           AND cmj.student_id = ps.student_id
                           AND cmj.left_at    IS NULL
                           AND cmj.deleted_at IS NULL
                           AND cmj.joined_at  > COALESCE(ax.release_at, ax.created_at))
                  AND NOT EXISTS (
                        SELECT 1 FROM cells c2
                         WHERE c2.assignment_id = pp2.assignment_id
                           AND c2.student_id    = ps.student_id))$n$;
begin
  select pg_get_functiondef('public.teacher_class_rollup_v2(uuid[], timestamptz, jsonb)'::regprocedure)
    into v_def;
  if (length(v_def) - length(replace(v_def, v_old, ''))) / length(v_old) <> 1 then
    raise exception 'teacher_class_rollup_v2 has drifted: expected the missing_marked expression exactly once';
  end if;
  execute replace(v_def, v_old, v_new);
end
$migrate$;
