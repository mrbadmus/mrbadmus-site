-- MRB-335 — only a school admin may move a class's tier, pathway or science.
--
-- ⚠️ VERSION IS LOAD-BEARING. TEST recorded 20260907235438; written as
-- 20260908000400 and renamed to match.
--
-- ── THE HOLE THIS CLOSES ───────────────────────────────────────────────
--
-- `POST /api/admin/class-tier` checks `school_admin`, refuses a non-KS4 class,
-- validates the triple for coherence and writes an `audit_log` row. All of that
-- is real, and NONE of it is a seal, because the route is not the only way in.
--
-- Two policies on `classes` allow the write, and MEASURED on TEST they are:
--
--     classes_teacher_update  FOR UPDATE  school_id = mine AND I teach the class
--     classes_hod_write       FOR ALL     school_id = mine AND I hold 'hod'
--
-- The frontend holds a Supabase client with the teacher's own JWT, so any
-- teacher of a class — or anybody who can read a teacher's session out of
-- localStorage — can PATCH `/rest/v1/classes?id=eq.<uuid>` directly and set
-- `tier`, `science_pathway` or `science_subject` to anything the CHECK
-- constraints allow. A hod can do it to any class in the school. No scope
-- check, no audit row, no trace.
--
-- ⚠️ `classes_teacher_update` HAS NO `WITH CHECK` CLAUSE AT ALL, only a
-- `USING`. Postgres then applies USING to the post-update row as well, so it
-- constrains WHICH ROW may be updated and says nothing whatever about what it
-- may be updated TO.
--
-- What that changes is not cosmetic. A class's pathway decides which questions
-- its children are served: flipping a Foundation Combined class to Higher
-- Triple silently widens its pool to the full specification, and the only
-- symptom is a Foundation child meeting questions three years above them, in
-- work that looks completely normal.
--
-- ⚠️ SO THE CHECK MOVES INTO THE DATABASE, where it applies to every writer
-- rather than to the one route that remembers. The route keeps its own checks:
-- it still refuses a non-KS4 class and an incoherent triple, which this trigger
-- has no opinion about, and it still writes the audit row.

create or replace function public.classes_guard_tier_columns()
returns trigger
language plpgsql
set search_path = public, pg_temp
as $fn$
declare
  claims text;
  claim_role text;
begin
  -- Nothing to guard unless one of the three actually moves. An UPDATE that
  -- renames a class, changes its year or flips `auto_assignments` is untouched.
  if (NEW.tier, NEW.science_pathway, NEW.science_subject)
       is not distinct from (OLD.tier, OLD.science_pathway, OLD.science_subject) then
    return NEW;
  end if;

  claims := current_setting('request.jwt.claims', true);

  -- ⚠️ NO CLAIMS AT ALL = NOT A POSTGREST REQUEST. A migration, a psql session,
  -- the SQL editor, a `supabase db push`. Refusing those would make this file
  -- unable to run its own backfills and would lock Mide out of his own
  -- database — and somebody with a direct connection is already past every
  -- policy in the schema, so there is nothing here to defend.
  if claims is null or claims = '' then
    return NEW;
  end if;

  -- The backend's service-role client. It reaches this table through exactly
  -- one route, which has already asked `auth_user_has_scope('school_admin')`
  -- under the CALLER's own JWT. ⚠️ A malformed claims string must not be read
  -- as service_role, so the cast is guarded rather than trusted.
  begin
    claim_role := nullif(claims, '')::jsonb ->> 'role';
  exception when others then
    claim_role := null;
  end;
  if claim_role = 'service_role' then
    return NEW;
  end if;

  -- Everybody else answers the same predicate the route does. It is SECURITY
  -- DEFINER and reads `auth.uid()`, so it is the caller's own standing, and it
  -- already folds in the legacy `profiles.role = 'admin'` path.
  if public.auth_user_has_scope('school_admin') then
    return NEW;
  end if;

  raise exception
    'classes.tier, classes.science_pathway and classes.science_subject may only '
    'be changed by a school admin (MRB-335). Use POST /api/admin/class-tier.'
    using errcode = '42501';
end;
$fn$;

-- ⚠️ THE NAME SORTS AFTER `classes_apply_tier_rule`, AND THAT IS DELIBERATE.
-- Postgres fires row triggers in alphabetical order, so the rule trigger runs
-- first and this one sees the values that are actually about to be stored. If
-- it ran first it would be guarding an intermediate state.
drop trigger if exists classes_guard_tier_columns on public.classes;
create trigger classes_guard_tier_columns
  before update on public.classes
  for each row execute function public.classes_guard_tier_columns();

comment on function public.classes_guard_tier_columns() is
  'MRB-335: refuses a change to tier/science_pathway/science_subject unless the writer is a direct connection, the service role, or holds school_admin. classes_teacher_update (FOR UPDATE, no WITH CHECK) and classes_hod_write (FOR ALL) let any teacher of a class, and any hod in the school, PATCH it into the Higher Triple pool through PostgREST with no audit.';
