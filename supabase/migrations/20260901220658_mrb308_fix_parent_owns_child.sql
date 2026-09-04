-- MRB-308 Night 1, migration 8: parent_owns_child() never asked what the
-- CHILD was. Fixing a defect I shipped four migrations ago.
--
-- The original predicate was: the parent and the target share a school_id,
-- the parent's role is 'parent', and the org kind is 'family'. Every clause
-- describes the PARENT or the ORG. Nothing describes the target. So it
-- returned true for:
--
--   * the parent against THEMSELVES — the end-to-end drive PATCHed a
--     parent's own profile through /children/:id and got 200, stamping an
--     adult's row with a key stage and a year group; and
--   * one parent against the OTHER parent in a two-parent family, which
--     would have let either reset the other's password.
--
-- It was also wrong in the opposite direction: it names kind 'family' only,
-- so it was false for every organisation-kind org, where staff manage pupils
-- through the same code path.
--
-- The backend now checks the target is a live student before calling this,
-- so the hole is already closed at the app layer. This closes it at the
-- source too — the function is granted to `authenticated` and can be called
-- directly over PostgREST, so an app-layer guard alone is not enough.

create or replace function public.parent_owns_child(p_parent uuid, p_child uuid)
returns boolean language sql stable security definer set search_path to 'public'
as $fn$
  select p_parent is not null
     and p_child  is not null
     -- A parent is not their own child. Cheap, and it is the exact case the
     -- drive caught.
     and p_parent <> p_child
     and exists (
    select 1
      from public.profiles parent
      join public.schools  org   on org.id = parent.school_id
      join public.profiles child on child.school_id = parent.school_id
     where parent.id = p_parent
       and child.id  = p_child
       and parent.role = 'parent'
       -- THE CLAUSE THAT WAS MISSING. The target must be a child: a live
       -- student in the org, not the other adult in it.
       and child.role = 'student'
       and child.deleted_at is null
       -- Organisation-kind orgs manage pupils through this same path, so
       -- they belong here too. Naming only 'family' made every council
       -- pupil unownable.
       and org.kind in ('family', 'organisation')
       and org.deleted_at is null
       and parent.deleted_at is null
  );
$fn$;

comment on function public.parent_owns_child(uuid, uuid) is
  'MRB-308. True when p_child is a LIVE STUDENT in the same family- or '
  'organisation-kind org that p_parent is a parent of. Explicitly false for '
  'p_parent = p_child, and for a second adult in the same org — both of which '
  'the pre-fix version allowed.';
