# HOD rollup visibility: apply sheet (parked, not applied to production)

## What it does, in plain English
The teacher class rollup (`teacher_class_rollup_v2`) runs with the database's own rights, so for a head of department it counted flashcard sittings that the head's own account is not allowed to read. That made a pupil's "last active" later than what the browser can show. This change makes the flashcard part follow the exact same rule as the `flashcard_sessions` read policy: the pupil's own sittings, school admin/SLT of the same school, or a teacher actively on that class. Nothing else changes. Applied and proven on TEST on 17 Oct 2026 (gate `teacher_rollup_equal`: 1329 values, 0 mismatches, was 1).

## Pre-check (run on PRODUCTION, refuse to apply otherwise)
```sql
select md5(prosrc) from pg_proc where proname='teacher_class_rollup_v2' and pronamespace='public'::regnamespace;
-- must equal 2d776cb168442801d3761b57b9b9bb50
```

## Apply
Paste `supabase/migrations/20261017120000_rollup_v2_flashcard_visibility.sql` into the SQL editor (project urklkrwevjtlfbwnipjn) and run. `CREATE OR REPLACE` keeps the existing grants.

## Post-checks
```sql
select md5(prosrc)=('250f89ed0247c8ade3efdc1874695fe3') md5_ok,
       prosecdef, provolatile='s' stable, proconfig,
       prosrc like '%recipient_ids IS NULL%' catchup_line,
       prosrc like '%THEMSELVES%' new_clause
  from pg_proc where proname='teacher_class_rollup_v2' and pronamespace='public'::regnamespace;
-- expect: true, true, true, {search_path=public,TimeZone=UTC}, true, true
select grantee, privilege_type from information_schema.routine_privileges
 where routine_name='teacher_class_rollup_v2' order by 1,2;
-- expect PUBLIC, anon, authenticated, postgres, service_role (all EXECUTE)
```

## Rollback
`supabase/rollbacks/20261017120000_rollup_v2_flashcard_visibility_rollback.sql` restores the previous definition verbatim (md5 2d776cb1...).
