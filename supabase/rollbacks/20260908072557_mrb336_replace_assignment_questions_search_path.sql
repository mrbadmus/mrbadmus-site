-- ROLLBACK for 20260908072557_mrb336_replace_assignment_questions_search_path
--
-- Apply MANUALLY only. Non-destructive: it puts the function body back exactly
-- as 20260908065607 wrote it, without the `set search_path` clause.
--
-- ⚠️ THERE IS ALMOST NEVER A REASON TO RUN THIS. Rolling this back makes the
-- function LESS like the rest of the estate and fixes nothing; if you are
-- undoing MRB-336 entirely, run 20260908065607's rollback instead, which drops
-- the function outright and is the honest undo. This exists so that every
-- forward migration has a matching one, which is the repo's rule.
--
-- ⚠️ THE REVOKES AND THE GRANT ARE RE-STATED. CREATE OR REPLACE resets a
-- function's privileges to the default, so omitting them here would leave the
-- function callable by `authenticated` — handing any signed-in browser the
-- ability to empty any assignment whose id it could guess. A rollback that
-- opens a hole is worse than the thing it is rolling back.

create or replace function public.replace_assignment_questions(
  p_assignment_id uuid,
  p_rows jsonb
) returns integer
language plpgsql
as $$
declare
  v_count integer;
begin
  if p_assignment_id is null then
    raise exception 'assignment_id is required';
  end if;
  if jsonb_typeof(p_rows) <> 'array' or jsonb_array_length(p_rows) = 0 then
    raise exception 'p_rows must be a non-empty array';
  end if;

  delete from public.assignment_questions where assignment_id = p_assignment_id;

  insert into public.assignment_questions (assignment_id, position, source_ref, rung, band)
  select p_assignment_id,
         (r->>'position')::int,
         r->>'source_ref',
         null,
         r->>'band'
    from jsonb_array_elements(p_rows) as r;

  get diagnostics v_count = row_count;
  return v_count;
end;
$$;

revoke all on function public.replace_assignment_questions(uuid, jsonb) from public;
revoke all on function public.replace_assignment_questions(uuid, jsonb) from anon;
revoke all on function public.replace_assignment_questions(uuid, jsonb) from authenticated;
grant execute on function public.replace_assignment_questions(uuid, jsonb) to service_role;

delete from supabase_migrations.schema_migrations where version = '20260908072557';
