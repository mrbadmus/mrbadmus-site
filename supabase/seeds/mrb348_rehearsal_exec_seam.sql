-- MRB-348 WS-3 — the TEST-ONLY rehearsal seam for tools/rls_consolidate.py.
--
-- ⚠️ NEVER APPLY THIS TO PRODUCTION. It lives in supabase/seeds/ precisely
-- because the Supabase CLI does not read this folder: `supabase db push` will
-- never pick it up. Apply it by hand, against TEST, and drop it afterwards.
--
-- WHY IT EXISTS
-- tools/rls_consolidate.py has to read pg_policies and run generated DDL.
-- PostgREST cannot reach pg_catalog, and this machine has no usable psql
-- credential (the Supabase CLI's token lives in the macOS Keychain, which a
-- non-interactive shell cannot unlock — see CLAUDE.md). So the tool needs one
-- arbitrary-SQL seam, and this is it.
--
-- ⚠️ THE TRAP, and it is the whole reason the grants below are not decoration:
-- a SECURITY DEFINER arbitrary-SQL function reachable by `anon` is a total
-- compromise of the database. The anon key is public by design — it ships in
-- shared/config.js and in every page on the site — so `grant execute ... to
-- anon` here would hand any visitor the ability to run any statement as the
-- function's owner. The revoke/grant pair is the only thing standing between
-- this object and that outcome. Verify it after applying:
--
--   select p.proname,
--          has_function_privilege('anon',          p.oid, 'execute') as anon_can,
--          has_function_privilege('authenticated', p.oid, 'execute') as auth_can,
--          has_function_privilege('service_role',  p.oid, 'execute') as sr_can
--   from pg_proc p join pg_namespace n on n.oid = p.pronamespace
--   where n.nspname = 'public' and p.proname like 'mrb348%';
--
-- anon_can and auth_can must both be false.
--
-- TEARDOWN, once the rehearsal is done:
--   drop function if exists public.mrb348_exec_sql(text);
--   drop function if exists public.mrb348_exec_ddl(text);

create or replace function public.mrb348_exec_sql(query text)
returns jsonb
language plpgsql
security definer
set search_path = public, pg_catalog
as $fn$
declare result jsonb;
begin
  execute 'select coalesce(jsonb_agg(t), ''[]''::jsonb) from (' || query || ') t' into result;
  return result;
end
$fn$;

revoke all on function public.mrb348_exec_sql(text) from public, anon, authenticated;
grant execute on function public.mrb348_exec_sql(text) to service_role;

-- The DDL sibling: statements that return no rows (drop policy, create policy).
create or replace function public.mrb348_exec_ddl(stmt text)
returns text
language plpgsql
security definer
set search_path = public, pg_catalog
as $fn$
begin
  execute stmt;
  return 'ok';
end
$fn$;

revoke all on function public.mrb348_exec_ddl(text) from public, anon, authenticated;
grant execute on function public.mrb348_exec_ddl(text) to service_role;
