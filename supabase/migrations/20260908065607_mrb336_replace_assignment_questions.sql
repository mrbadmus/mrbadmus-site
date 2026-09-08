-- MRB-336 — replacing an unreleased assignment's questions, atomically.
--
-- ⚠️ THIS EXISTS BECAUSE POSTGREST HAS NO TRANSACTION. `PATCH
-- /api/teacher/set-work/:id` replaces the whole question set when a teacher
-- edits work before it is released, and "delete the twelve, insert the new
-- fifteen" through two supabase-js calls is two transactions with a window
-- between them. If the insert fails in that window the assignment is live with
-- NO questions on it — a piece of homework a class can open and cannot answer.
--
-- The compensating-rollback pattern the POST uses (`rollbackAll`) is the right
-- answer when the thing being undone is a row that did not exist before. It is
-- the wrong answer here, because the thing being undone is rows that DID exist
-- and whose contents we would have to have saved and be able to put back — a
-- second write that can itself fail. A plpgsql function body is one
-- transaction, which is the guarantee the ticket actually asked for.
--
-- ⚠️ POSITIONS ARE 1-BASED. Every other writer of this table numbers from 1 —
-- `POST /api/teacher/set-work` and the automatic composer both insert
-- `position: i + 1` — and `assignment_questions_assignment_id_position_key` is
-- UNIQUE (assignment_id, position). An edited assignment numbered from 0 would
-- be the only 0-based assignment in the school and would sort correctly by
-- accident while disagreeing with every sibling row. The caller supplies the
-- positions; this function does not invent them.
--
-- `rung` is written NULL unconditionally rather than taken from the caller:
-- `one_pool_per_assignment` and `assignment_questions_rung_xor_band` together
-- require exactly (band NOT NULL, rung NULL) for a bank-composed set, and a
-- parameter the caller can get wrong is a parameter that will be got wrong.
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

-- ⚠️ THE BACKEND ONLY. This function rewrites an assignment's contents with no
-- authorisation of its own — the route has already resolved `setWorkAccess`,
-- the release regime and the pool seal before it is reached. Exposing it to
-- `authenticated` would hand any signed-in browser the ability to empty any
-- assignment whose id it could guess.
revoke all on function public.replace_assignment_questions(uuid, jsonb) from public;
revoke all on function public.replace_assignment_questions(uuid, jsonb) from anon;
revoke all on function public.replace_assignment_questions(uuid, jsonb) from authenticated;
grant execute on function public.replace_assignment_questions(uuid, jsonb) to service_role;
