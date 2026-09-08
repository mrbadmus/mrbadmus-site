-- MRB-336 review — `set search_path` on `replace_assignment_questions`.
--
-- ⊕ Follow-up to 20260908065607, and a CREATE OR REPLACE rather than an edit of
-- that file. 20260908065607 has already been recorded — on TEST, and it is
-- queued for production — and quietly changing the body of a migration a
-- database has already run is how a file in git stops describing what actually
-- ran. A third migration is explicit and ordered: `search_path` was absent, then
-- it was added, and both facts have a version.
--
-- ⚠️ NOT A VULNERABILITY, AND THE REASON IS WORTH WRITING DOWN so nobody
-- downgrades the habit. `replace_assignment_questions` is SECURITY INVOKER, so
-- it runs with the caller's own privileges and a hijacked `search_path` would
-- buy an attacker exactly the rights they already had. What makes this worth a
-- migration is CONSISTENCY: every SECURITY DEFINER function in
-- `schools_layer.sql` pins its path, and a reader who finds one function in the
-- estate without it has to work out for themselves whether that is deliberate.
-- Making them all look the same means the one that MATTERS is never the odd one
-- out — and if this function is ever promoted to SECURITY DEFINER, the pin is
-- already there rather than being the thing somebody forgot.
--
-- `pg_temp` is LAST, on purpose. It is where a caller can create objects, so
-- naming it first would let a session-temporary table shadow `public`'s — which
-- is the whole attack the pin exists to close.
--
-- The body below is byte-identical to 20260908065607's; only the `set` clause
-- is new. Re-stating the whole function is what CREATE OR REPLACE requires, and
-- it is also why the comments come with it: the next reader of this function
-- should find its reasoning in the same place as its code.
create or replace function public.replace_assignment_questions(
  p_assignment_id uuid,
  p_rows jsonb
) returns integer
language plpgsql
set search_path = public, pg_temp
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

-- ⚠️ CREATE OR REPLACE RESETS PRIVILEGES TO THE DEFAULT, so the grants from
-- 20260908065607 have to be re-stated or this function silently becomes
-- callable by `authenticated` again — which would hand any signed-in browser
-- the ability to empty any assignment whose id it could guess. This is the
-- failure mode of a REPLACE that looks like a no-op.
revoke all on function public.replace_assignment_questions(uuid, jsonb) from public;
revoke all on function public.replace_assignment_questions(uuid, jsonb) from anon;
revoke all on function public.replace_assignment_questions(uuid, jsonb) from authenticated;
grant execute on function public.replace_assignment_questions(uuid, jsonb) to service_role;
