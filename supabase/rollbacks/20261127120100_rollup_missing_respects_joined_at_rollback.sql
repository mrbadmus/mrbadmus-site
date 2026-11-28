-- Rollback for 20261127120100_rollup_missing_respects_joined_at.sql
-- Puts teacher_class_rollup_v2's missing_marked back to the closed-count test.
-- Apply manually only.
do $rollback$
declare
  v_def  text;
  v_from int;
  v_to   int;
  v_head text := $h$'missing_marked', EXISTS (
               SELECT 1
                 FROM per_paper pp2$h$;
  v_tail text := $t$AND c2.student_id    = ps.student_id))$t$;
begin
  select pg_get_functiondef('public.teacher_class_rollup_v2(uuid[], timestamptz, jsonb)'::regprocedure)
    into v_def;
  v_from := position(v_head in v_def);
  v_to   := position(v_tail in v_def);
  if v_from = 0 or v_to = 0 or v_to < v_from then
    raise exception 'teacher_class_rollup_v2: joined_at expression not found; nothing to roll back';
  end if;
  execute substr(v_def, 1, v_from - 1)
       || $o$'missing_marked', (COALESCE(cc.n, 0) > ps.closed_cells)$o$
       || substr(v_def, v_to + length(v_tail));
end
$rollback$;
