-- ROLLBACK for MRB-348 WS-3 (consolidate multiple permissive RLS policies).
--
-- Apply MANUALLY only -- the Supabase CLI never reads supabase/rollbacks/.
--
-- Drops the merged policies and recreates every original from
-- public.mrb348_policy_backup, which the forward migration filled.
--
-- ⚠️ Unlike the MRB-347 rollback, this one cannot be a simple ALTER: the
-- forward migration DROPPED policies and CREATED differently-named ones, so
-- restoring means recreating objects, including their permissive flag, their
-- roles and their command. All four are stored in the backup table for
-- exactly this reason -- a rollback that restored the expressions but not the
-- GRANT set would quietly change who each policy reaches.
--
-- ⚠️ This returns the estate to the many-branch policies and to the 251
-- linter findings. The forward migration was proven semantically identical
-- (inverse-transform round-trip plus before/after visibility digests across
-- every role), so rolling back buys nothing but latency. Use it only if the
-- merge is implicated in an actual incident.
--
-- Pairs with the forward migration generated from ref qeppkiswvclkkwbxmlok at 2026-09-22 02:05 UTC.

begin;

do $rb$
declare r record; stmt text; n_drop int := 0; n_restore int := 0;
begin
  if to_regclass('public.mrb348_policy_backup') is null then
    raise exception 'MRB-348 rollback: backup table missing, cannot restore';
  end if;

  -- 1. drop the merged policies this ticket created
  for r in
    select tablename, policyname from pg_policies
    where schemaname = 'public'
      and policyname like '%\_merged'
      and not exists (select 1 from public.mrb348_policy_backup b
                      where b.tablename = pg_policies.tablename
                        and b.policyname = pg_policies.policyname)
  loop
    execute format('drop policy %I on public.%I', r.policyname, r.tablename);
    n_drop := n_drop + 1;
  end loop;

  -- 2. recreate every original that is no longer present
  for r in select * from public.mrb348_policy_backup loop
    if not exists (select 1 from pg_policies
                   where schemaname = 'public'
                     and tablename = r.tablename
                     and policyname = r.policyname) then
      stmt := format('create policy %I on public.%I as %s for %s to %s',
                     r.policyname, r.tablename,
                     case when r.permissive = 'PERMISSIVE' then 'permissive'
                          else 'restrictive' end,
                     r.cmd,
                     -- roles came out of pg_policies as a {a,b} array literal
                     array_to_string(
                       (select array_agg(quote_ident(x))
                        from unnest(string_to_array(trim(both '{}' from r.roles), ','))
                             as x), ', '));
      if r.qual is not null then
        stmt := stmt || format(' using (%s)', r.qual);
      end if;
      if r.with_check is not null then
        stmt := stmt || format(' with check (%s)', r.with_check);
      end if;
      execute stmt;
      n_restore := n_restore + 1;
    end if;
  end loop;

  raise notice 'MRB-348 rollback: dropped % merged, restored % original',
               n_drop, n_restore;
end $rb$;

commit;

-- Optional, once you are certain you will not roll back again:
--   drop table public.mrb348_policy_backup;
