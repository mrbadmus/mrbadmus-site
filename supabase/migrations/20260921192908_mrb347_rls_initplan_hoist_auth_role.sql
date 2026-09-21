-- MRB-347 follow-on — auth.role() was missed by the first pass.
--
-- WHY THERE ARE TWO MIGRATIONS AND NOT ONE
-- The first pass (20260921192720) named auth.uid() in its substitution list but
-- not auth.role(). Supabase's linter caught the gap immediately after that
-- migration landed: 47 auth_rls_initplan findings had fallen to 3, and all
-- three were bare auth.role() calls —
--     weekly_challenges  "Authenticated users can view active challenges"
--     weekly_challenges  "Service role manages challenges"
--     weekly_scores      "Authenticated can view weekly leaderboard"
--
-- ⚠️ weekly_scores backs the LEADERBOARD, which index.html reads for Champion
-- of the Week and leaderboard.html reads for all twelve tracks. It is one of
-- the most-read tables on the site by a signed-in student, so leaving it bare
-- would have left the hoist half-done exactly where it is most felt.
--
-- This is a separate file rather than an edit to the first one because the
-- first one had already been applied to production. A migration file must
-- record what actually ran; rewriting it after the fact would make the repo
-- disagree with schema_migrations. Applied in order, the two give a fresh
-- environment the same end state.
--
-- auth.role() is STABLE and constant for the life of a request, exactly like
-- auth.uid(), so this hoist is inert for the same reason.
--
-- VERIFIED ON PRODUCTION after this ran: 153 policies (unchanged), 141 hoisted,
-- and the visibility harness re-run against the pre-change baseline showed
-- 0 mismatches across 240 user x table cells / 202,922 rows.

begin;

-- top up the rollback backup with anything not already captured
insert into public.mrb347_policy_backup (schemaname, tablename, policyname, cmd, qual, with_check)
select schemaname, tablename, policyname, cmd, qual, with_check
from pg_policies
where schemaname = 'public'
  and not exists (select 1 from public.mrb347_policy_backup b
                  where b.tablename = pg_policies.tablename
                    and b.policyname = pg_policies.policyname);

do $do$
declare r record; stmt text; nq text; nw text; n_before int; n_after int; done int := 0;
begin
  select count(*) into n_before from pg_policies where schemaname='public';

  for r in
    select tablename, policyname, qual, with_check from pg_policies
    where schemaname='public'
      and (coalesce(qual,'') ~ '\mauth\.role\(\)' or coalesce(with_check,'') ~ '\mauth\.role\(\)')
  loop
    nq := regexp_replace(r.qual,       '\mauth\.role\(\)', '(select auth.role())', 'g');
    nw := regexp_replace(r.with_check, '\mauth\.role\(\)', '(select auth.role())', 'g');
    -- already-hoisted policies rewrite to themselves, so this is idempotent:
    -- `( SELECT auth.role() AS role)` contains no BARE auth.role() for \m to match
    -- at a word boundary preceded by "select ".
    if (nq is distinct from r.qual) or (nw is distinct from r.with_check) then
      stmt := format('alter policy %I on public.%I', r.policyname, r.tablename);
      if r.qual       is not null then stmt := stmt || format(' using (%s)', nq);      end if;
      if r.with_check is not null then stmt := stmt || format(' with check (%s)', nw); end if;
      execute stmt;
      done := done + 1;
    end if;
  end loop;

  select count(*) into n_after from pg_policies where schemaname='public';
  if n_after <> n_before then
    raise exception 'MRB-347 follow-on aborted: policy count changed % -> %', n_before, n_after;
  end if;
  raise notice 'MRB-347 follow-on: hoisted % policies (% total, unchanged)', done, n_after;
end $do$;

commit;
