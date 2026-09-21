-- ROLLBACK for MRB-347 (RLS InitPlan hoist).
--
-- Apply MANUALLY only — the Supabase CLI never reads supabase/rollbacks/.
--
-- Restores every policy expression captured in public.mrb347_policy_backup by
-- the forward migration. Safe to run more than once: it simply re-asserts the
-- original expressions.
--
-- ⚠️ This returns the estate to the SLOW policies. The forward migration was
-- proven semantically identical (171 user x table visibility digests, zero
-- mismatches), so rolling back buys nothing but latency. Use it only if the
-- hoist is implicated in an actual incident.

begin;

do $do$
declare r record; stmt text; n int := 0;
begin
  if to_regclass('public.mrb347_policy_backup') is null then
    raise exception 'MRB-347 rollback: backup table missing, cannot restore';
  end if;

  for r in select * from public.mrb347_policy_backup loop
    -- only restore policies that still exist under the same name
    if exists (select 1 from pg_policies
               where schemaname = 'public'
                 and tablename = r.tablename
                 and policyname = r.policyname) then
      stmt := format('alter policy %I on public.%I', r.policyname, r.tablename);
      if r.qual       is not null then stmt := stmt || format(' using (%s)', r.qual);      end if;
      if r.with_check is not null then stmt := stmt || format(' with check (%s)', r.with_check); end if;
      execute stmt;
      n := n + 1;
    else
      raise warning 'MRB-347 rollback: policy %.% no longer exists, skipped', r.tablename, r.policyname;
    end if;
  end loop;

  raise notice 'MRB-347 rollback: restored % policies', n;
end $do$;

commit;

-- Optional, once you are certain you will not roll back again:
--   drop table public.mrb347_policy_backup;
