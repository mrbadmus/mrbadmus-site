-- MRB-347 — RLS InitPlan hoist. A PERFORMANCE migration with NO semantic change.
--
-- ============================================================================
-- WHAT WAS WRONG
-- ============================================================================
-- A student reading their OWN profile by primary key cost 23.9 ms and 440
-- shared buffer hits, for ONE row. Measured on production, 21 Sep 2026:
--
--   Limit  (actual time=23.820..23.821 rows=1 loops=1)
--     Buffers: shared hit=440
--     ->  Index Scan using profiles_pkey on profiles
--           Filter: (((school_id = auth_user_school_id()) AND ... EXISTS(SubPlan 1))
--                    OR auth_user_operator_active() OR ... OR (jwt.sub = id))
--           SubPlan 1 -> Index Scan on class_members  (actual time=9.752..9.752)
--
-- Two compounding causes:
--
--   1. Every `auth.<fn>()` and every constant-per-request helper
--      (auth_user_school_id(), auth_user_has_scope('x'), auth_user_operator_active(),
--      auth_user_id(), auth_user_role(), auth_user_department(),
--      auth_user_is_platform_operator()) was called BARE in the policy qual.
--      Postgres cannot hoist a bare function call out of a row filter, and it
--      cannot INLINE these helpers either — they are SECURITY DEFINER and carry
--      SET search_path, both of which disqualify a SQL function from inlining.
--      So each one runs as a full nested query ONCE PER ROW SCANNED, per policy.
--      auth.uid() is worse than it looks: it re-parses the JWT claims JSON per row.
--
--   2. The permissive policies OR together, so a table with 5 SELECT policies
--      evaluates all five branches per row until one is true — and the CHEAPEST
--      branch ("is this your own row") was ordered LAST.
--
-- Supabase's own linter flagged cause 1 as `auth_rls_initplan`: 47 findings on
-- production across 26 tables.
--
-- ============================================================================
-- THE FIX
-- ============================================================================
-- Wrap each constant-per-request call in a scalar subquery: `f()` -> `(select f())`.
-- Postgres then evaluates it as an InitPlan — ONCE per query instead of once per
-- row. This is the transform Supabase documents for this exact lint.
--
-- It is SEMANTICALLY INERT, and that is provable rather than hopeful: every one
-- of these functions is declared STABLE, so by definition its value cannot change
-- within a single statement. Evaluating it once and reusing the value is
-- therefore identical to evaluating it per row. The boolean expression is
-- otherwise untouched.
--
-- ⚠️ Calls whose argument depends on the ROW are deliberately NOT wrapped:
--      auth_user_teaches_class(class_id), class_school_id(class_id),
--      auth_user_is_member_of_class(id), auth_user_is_hod_of_dept(department),
--      auth_user_is_hod_of_subject_dept(subject_id)
--    Hoisting those WOULD change meaning — they must vary per row. The regexes
--    below only match the zero-argument forms and the constant-literal
--    auth_user_has_scope('...'::text) form, so they cannot touch these.
--
-- ============================================================================
-- EVIDENCE (rehearsed on TEST qeppkiswvclkkwbxmlok, 21 Sep 2026)
-- ============================================================================
-- Equivalence: 9 users spanning student / teacher / HoD / SLT / school_admin,
-- x 19 tables = 171 cells. For each cell the FULL visible row-set was hashed
-- (md5 over every row cast to text, ordered) before and after.
--     mismatches: 0        row-count mismatches: 0      rows compared: 10,329
--
-- Speed, 30 iterations per query, as a teacher holding 6 classes:
--     profiles (scan)          588.5 ms -> 148.8 ms   3.96x
--     class_members            204.6 ms ->  75.0 ms   2.73x
--     class_teachers           146.6 ms ->  66.0 ms   2.22x
--     classes                  180.2 ms ->  97.4 ms   1.85x
--     assignment_submissions  1281.5 ms -> 813.7 ms   1.57x
--     assignments              369.3 ms -> 238.6 ms   1.55x
--     TOTAL                   2856   ms -> 1506   ms   1.90x
-- TEST holds 54 profiles; production holds 1,187. Per-row costs dominate the
-- larger table, so production should gain MORE than these figures, not less.
--
-- ============================================================================
-- APPLIED TO PRODUCTION 21 Sep 2026, ruled by Mide in the prompt
-- ============================================================================
-- Target named and proven from the data before the write, not from a label:
-- 153 policies / 1,193 profiles / 73 classes, which is production and is not
-- TEST (141 / 54 / 12).
--
-- Equivalence re-proved ON PRODUCTION against production data, not inferred
-- from the TEST run: 10 real users (2 school_admins, 4 teachers holding up to
-- 16 classes, 4 students in 4 classes each) x 24 tables = 240 cells, every
-- visible row hashed before and after.
--     visibility mismatches: 0    row-count mismatches: 0    errors: 0
--     rows fingerprinted: 202,922
--
-- Result: 153 policies (unchanged), 138 hoisted by this migration, +3 more by
-- the auth.role() follow-on (20260921192908) for 141 total.
--
-- The headline query — a student reading their OWN profile by primary key,
-- the same plan quoted at the top of this file:
--     execution   23.916 ms  ->  4.715 ms     (5.1x)
--     planning     5.717 ms  ->  1.709 ms
-- The filter now reads `(InitPlan 20).col1` rather than a bare call, and most
-- InitPlans report "never executed" because the OR short-circuits before it
-- reaches them.
--
-- Supabase linter, auth_rls_initplan on production: 47 -> 3 -> 0 (the 3 being
-- the auth.role() gap that the follow-on closed).
--
-- ============================================================================
-- SHAPE OF THIS MIGRATION
-- ============================================================================
-- It rewrites whatever policies it finds at apply time rather than hard-coding
-- 132 ALTER statements, because TEST and production policy sets are not
-- byte-identical (e.g. profiles_teacher_read_students carries an extra
-- `cm.deleted_at IS NULL` on production). Generating from pg_policies means each
-- environment gets its own true expression hoisted and nothing else changed.
--
-- It is IDEMPOTENT: a policy already containing a wrapped form is skipped.
-- It is REVERSIBLE: every original qual/with_check is kept in
-- public.mrb347_policy_backup. See supabase/rollbacks/ for the undo.
-- ============================================================================

begin;

create table if not exists public.mrb347_policy_backup (
  schemaname text, tablename text, policyname text, cmd text,
  qual text, with_check text, taken_at timestamptz default now()
);
revoke all on public.mrb347_policy_backup from public, anon, authenticated;

insert into public.mrb347_policy_backup (schemaname, tablename, policyname, cmd, qual, with_check)
select schemaname, tablename, policyname, cmd, qual, with_check
from pg_policies
where schemaname = 'public'
  and not exists (select 1 from public.mrb347_policy_backup b
                  where b.tablename = pg_policies.tablename
                    and b.policyname = pg_policies.policyname);

create or replace function pg_temp.mrb347_hoist(expr text) returns text
language sql immutable as $fn$
  select case when expr is null then null else
    regexp_replace(
    regexp_replace(
    regexp_replace(
    regexp_replace(
    regexp_replace(
    regexp_replace(
    regexp_replace(
    regexp_replace(expr,
      '\mauth\.uid\(\)',                       '(select auth.uid())', 'g'),
      '\mauth_user_school_id\(\)',             '(select auth_user_school_id())', 'g'),
      '\mauth_user_id\(\)',                    '(select auth_user_id())', 'g'),
      '\mauth_user_role\(\)',                  '(select auth_user_role())', 'g'),
      '\mauth_user_department\(\)',            '(select auth_user_department())', 'g'),
      '\mauth_user_operator_active\(\)',       '(select auth_user_operator_active())', 'g'),
      '\mauth_user_is_platform_operator\(\)',  '(select auth_user_is_platform_operator())', 'g'),
      '\mauth_user_has_scope\((''[^'']*''::text)\)', '(select auth_user_has_scope(\1))', 'g')
  end
$fn$;

do $do$
declare
  r record; stmt text; nq text; nw text;
  n_before int; n_after int; done int := 0;
begin
  select count(*) into n_before from pg_policies where schemaname = 'public';

  for r in
    select tablename, policyname, qual, with_check
    from pg_policies
    where schemaname = 'public'
      -- idempotency: skip anything already hoisted
      and coalesce(qual, '')       !~* '\(\s*select\s+auth'
      and coalesce(with_check, '') !~* '\(\s*select\s+auth'
  loop
    nq := pg_temp.mrb347_hoist(r.qual);
    nw := pg_temp.mrb347_hoist(r.with_check);

    if (nq is distinct from r.qual) or (nw is distinct from r.with_check) then
      stmt := format('alter policy %I on public.%I', r.policyname, r.tablename);
      -- only ever set the clause that already existed: an INSERT policy has no
      -- USING, and adding one would be an error rather than a no-op.
      if r.qual       is not null then stmt := stmt || format(' using (%s)', nq);      end if;
      if r.with_check is not null then stmt := stmt || format(' with check (%s)', nw); end if;
      execute stmt;
      done := done + 1;
    end if;
  end loop;

  select count(*) into n_after from pg_policies where schemaname = 'public';

  -- ALTER POLICY can only change an expression; it cannot add or drop a policy.
  -- Assert that anyway, so a future edit to this file cannot quietly widen access.
  if n_after <> n_before then
    raise exception 'MRB-347 aborted: policy count changed % -> %', n_before, n_after;
  end if;

  raise notice 'MRB-347: hoisted % policies (% total, unchanged)', done, n_after;
end $do$;

commit;
