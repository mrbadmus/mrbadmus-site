# MrBadmus Wrapped — open counts — apply sheet

**Nothing here has been run against production.** Applied to and driven on the
TEST project (`qeppkiswvclkkwbxmlok`) only; the TEST ref was proven from the
service-role key's JWT `ref` claim before any write. **Platform chat applies
this to PRODUCTION** (`urklkrwevjtlfbwnipjn`) once Mide says yes. It depends on
the Wrapped migration (`20261014120000_wrapped.sql`), which is already live on
prod: it uses `_wrapped_gate`, `auth_user_is_member_of_class`,
`auth_user_teaches_class`.

The site code (`shared/wrapped.js`, on main) calls `wrapped_mark` fire-and-forget
and swallows every failure, so it is safe before and after this apply.

## 1. What it does

File: `supabase/migrations/20261021120000_wrapped_opens.sql`
Rollback: `supabase/rollbacks/20261021120000_wrapped_opens_rollback.sql`

| file md5 | |
|---|---|
| `2e271a0dee93a467a1f1ddb15146dbb9` | migration |
| `cdeec0311ddc817016fdfea90ca97c98` | rollback |

- `public.wrapped_opens (profile_id, class_id, role, first_opened_at, last_opened_at, opens, reached_end, shared)`,
  PK `(profile_id, class_id)`, FKs to `profiles` / `classes` `on delete cascade`.
  RLS on, **no policies**, all privileges revoked from public/anon/authenticated.
- `public.wrapped_mark(p_class_id uuid, p_event text) returns void` — SECURITY
  DEFINER, `search_path=public`, EXECUTE for `authenticated` only. Records for
  `auth.uid()` only (no profile parameter). Silently does nothing if: not signed
  in, event not `open`/`end`/`share`, `_wrapped_gate(false) <> 'open'` (so
  preview opens before release, or after close, are ignored), or the caller is
  neither a member nor a teacher of the class. Role = `pupil` if member, else
  `teacher` (same order as `wrapped_status`).
- `public.wrapped_open_stats() returns jsonb` — totals (pupils opened, teachers
  opened, reached end, shared) plus `by_class` (class name + counts, no names).
  EXECUTE revoked from public/anon/authenticated: service role only.

Touches no existing table, function or policy.

## 2. md5 table (`md5(prosrc)`), identical on TEST and in the file

| function | md5 |
|---|---|
| `wrapped_mark` | `5646cb63c2b6d3547e53539458c067a3` |
| `wrapped_open_stats` | `b46f3a60cc3e96308bb0a7fed6b74491` |

## 3. Post-checks (read-only)

```sql
select proname, md5(prosrc) from pg_proc
 where pronamespace='public'::regnamespace and proname in ('wrapped_mark','wrapped_open_stats') order by 1;
-- compare to section 2

select has_function_privilege('authenticated','public.wrapped_mark(uuid,text)','execute')  auth_mark,   -- true
       has_function_privilege('anon','public.wrapped_mark(uuid,text)','execute')           anon_mark,   -- false
       has_function_privilege('authenticated','public.wrapped_open_stats()','execute')     auth_stats,  -- false
       has_function_privilege('anon','public.wrapped_open_stats()','execute')              anon_stats,  -- false
       has_function_privilege('service_role','public.wrapped_open_stats()','execute')      svc_stats,   -- true
       has_table_privilege('authenticated','public.wrapped_opens','select')                auth_tbl,    -- false
       has_table_privilege('anon','public.wrapped_opens','select')                         anon_tbl,    -- false
       (select relrowsecurity from pg_class where relname='wrapped_opens')                 rls,         -- true
       (select count(*) from pg_policies where tablename='wrapped_opens')                  policies;    -- 0
```

Reading the numbers later (service role / SQL editor only):

```sql
select public.wrapped_open_stats();
```

## 4. TEST proofs (21 Oct 2026, real fixture accounts over PostgREST, plus one rolled-back transaction)

- Pupil marks only self: open x2 + end + share by Bea gave one row
  `(Bea, class A) opens=2 reached_end=true shared=true`; Lia open gave her own
  row; the class-A teacher got `role=teacher`. A pupil of class B marking class
  A wrote nothing. Every new row's `profile_id` was a caller; an extra
  `p_profile_id` argument is rejected by PostgREST (404, no such signature).
- A classmate SELECT / INSERT / UPDATE on `wrapped_opens` → 403.
- anon: table select 401, `wrapped_mark` 401, `wrapped_open_stats` 401;
  authenticated `wrapped_open_stats` 403.
- Service role `wrapped_open_stats()` → `{pupils_opened:2, teachers_opened:1, reached_end:1, shared:1, by_class:[{class_name:"WR 8r/Sc1", opens:5, ...}]}`.
- Release gate: inside a transaction that was rolled back, with `release_at`
  one day ahead, a pupil's `open` wrote 0 rows; with it in the past, 1 row.
  `wrapped_settings.release_at` confirmed unchanged afterwards.
- Unknown event → 204, nothing written. Teardown by snapshotted key list; table
  empty afterwards.

## 5. Rollback

`supabase/rollbacks/20261021120000_wrapped_opens_rollback.sql` drops
`wrapped_open_stats()`, `wrapped_mark(uuid,text)`, then the table (counts are
lost). Safe with the site live. Registry caveat as in WRAPPED-APPLY.md:
`apply_migration` mints its own version — delete by name
(`select version from supabase_migrations.schema_migrations where name = 'wrapped_opens';`).
