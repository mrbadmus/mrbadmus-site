-- ROLLBACK for MRB-308 Night 1, migration 8
-- (20260901220658_mrb308_fix_parent_owns_child). Apply MANUALLY only.
--
-- ⚠️⚠️⚠️ READ THIS BEFORE YOU RUN IT. ⚠️⚠️⚠️
--
-- Running this file REINTRODUCES A REAL PRIVILEGE BUG. It is not a neutral
-- undo. The definition below is the pre-fix one, and every clause in it
-- describes the PARENT or the ORG — not one of them asks what the TARGET is.
-- So it returns true in two cases it must not:
--
--   * A PARENT AGAINST THEMSELVES. parent_owns_child(p, p) is true, which
--     is how the end-to-end drive PATCHed a parent's own adult profile
--     through /children/:id and got a 200 back, stamping a grown adult's row
--     with a key stage and a year group.
--   * ONE PARENT AGAINST THE OTHER ADULT IN A TWO-PARENT FAMILY. Either
--     could then run the child-account path against the other — including
--     resetting that adult's password.
--
-- The function is granted to `authenticated` and is reachable directly over
-- PostgREST, so restoring it re-opens both holes at the source no matter what
-- the backend does. It is also wrong in the harmless direction: it names
-- kind 'family' only, so every organisation-kind pupil becomes unownable and
-- staff-managed pupils stop working.
--
-- There is almost no good reason to run this file. If you are unwinding the
-- whole MRB-308 stack, the right move is to DROP parent_owns_child (see
-- rollbacks/20260901214558_mrb308_child_accounts.sql, which does exactly
-- that) rather than to restore a broken predicate and leave it live.
--
-- It exists only so that the pair (migration, rollback) is complete and so
-- that the old body is on the record in one identifiable place.

create or replace function public.parent_owns_child(p_parent uuid, p_child uuid)
returns boolean language sql stable security definer set search_path to 'public'
as $fn$
  select exists (
    select 1
      from public.profiles parent
      join public.schools  fam   on fam.id = parent.school_id
      join public.profiles child on child.school_id = parent.school_id
     where parent.id = p_parent
       and child.id  = p_child
       and parent.role = 'parent'
       and fam.kind = 'family'
       and fam.deleted_at is null
       and child.deleted_at is null
  );
$fn$;
grant execute on function public.parent_owns_child(uuid, uuid) to authenticated;

-- Restore the pre-fix comment too, so the catalogue does not advertise a
-- guarantee this definition does not make.
comment on function public.parent_owns_child(uuid, uuid) is null;
