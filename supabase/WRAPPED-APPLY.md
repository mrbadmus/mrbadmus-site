# MrBadmus Wrapped — database half — apply sheet

**Nothing in here has been run against production.** Everything below was
applied to and driven on the TEST project (`qeppkiswvclkkwbxmlok`). The only
things touched on production (`urklkrwevjtlfbwnipjn`, ends in **N**) were
read-only SELECTs, listed in section 7.

**Mide rules the prod apply.** The migration is PARKED on branch
`feat/wrapped-migrations` until he says to apply it.

Evidence gathered 15 Oct 2026 (fresh, by the finishing agent; the first agent's
session died before writing this sheet).

## 1. What it adds, reads, and does not touch

File: `supabase/migrations/20261014120000_wrapped.sql`
Rollback: `supabase/rollbacks/20261014120000_wrapped_rollback.sql`

| file md5 (bytes) | |
|---|---|
| `682041683fe45721be018427a3c53db9` | migration |
| `c3792998e51185fe4ff0f7ed7fb8be5e` | rollback |

**Adds — one table, five functions:**

- `public.wrapped_settings` — the single settings row (RLS on, no policies, all
  grants revoked from public/anon/authenticated).
- `public._wrapped_gate(boolean)` — internal (execute revoked from everyone).
- `public._wrapped_week_points(uuid, uuid, boolean)` — internal.
- `public.wrapped_status(uuid, boolean)`, `public.wrapped_pupil(uuid, boolean)`,
  `public.wrapped_class(uuid, boolean)` — the three public RPCs. All SECURITY
  DEFINER, `search_path=public`; execute granted to `authenticated` only.

**Reads (existing tables/functions only):** `assignments`,
`assignment_submissions`, `classes`, `academic_years`, `class_members`,
`class_teachers`, `profiles`, `flashcard_reviews`, `quiz_scores`, plus the
functions `flashcard_card_state`, `_mrb_week_number`,
`auth_user_is_member_of_class`, `auth_user_teaches_class`. The stars rule is
copied from `class_stars_board_for_member`, not called.

**Does NOT touch:** no existing table, column, policy, trigger or function is
altered. Never names `assignments.recipient_ids` (works whether or not that
parked column exists). No pupil parameter anywhere: `wrapped_pupil` answers for
`auth.uid()` only.

## 2. Deploy-order safety

The site half is **already LIVE on mrbadmus.com** (commit `be3231df6`,
`wrapped.js?v=fbcb65d0`). On production it is **inert until this migration
lands**: boot calls `wrapped_status`, the RPC does not exist, the error is
swallowed silently, nothing renders. So site-before-migration is safe (it is the
current state).

Migration-before-release is also safe: `release_at` gates everything. Before
`2026-10-20 08:00 Europe/London` only the profile ids in
`preview_profile_ids` can see anything, and only when the caller asks for
`preview=true`. Everyone else gets `open:false`.

There is no unsafe ordering.

## 3. The prod apply step

1. Run the migration file on production. It seeds the settings row:
   - `release_at` = `2026-10-20 08:00 Europe/London` (07:00 UTC)
   - `close_at` = NULL, `window_start` = `2026-09-01 00:00 Europe/London`
   - `half_term_from/to` = 2026-10-24 / 2026-11-01
   - `christmas_on` = 2026-12-18 (**confirmed by Mide, 15 Oct 2026**: last day of
     term; card wording stays "by Christmas")
   - `show_zero_card` = true
   - `preview_profile_ids` = **AY `b0308282-5429-4050-827f-4707286a88aa` and Mide
     `74db2bf7-7c0d-47e6-9479-5cee3cda610e`** — which is already exactly what
     production should hold. The migration seeds it, so no follow-up UPDATE is
     needed. If the row is ever found holding anything else (it will on TEST,
     where the fixture ids were put in), the one-line fix is:

```sql
update public.wrapped_settings
   set preview_profile_ids = array['b0308282-5429-4050-827f-4707286a88aa','74db2bf7-7c0d-47e6-9479-5cee3cda610e']::uuid[];
```

   The insert is `on conflict (id) do nothing`, so re-running never overwrites.
2. Nothing to restart (no backend involvement).

## 4. Verification after the prod apply (all read-only)

```sql
-- 1. objects exist
select (select count(*) from information_schema.tables where table_name='wrapped_settings') tbl,
       (select count(*) from pg_proc where pronamespace='public'::regnamespace and proname like '%wrapped%') fns;
-- expect 1, 5

-- 2. bodies match the file (compare to section 5)
select proname, md5(prosrc) from pg_proc
 where pronamespace='public'::regnamespace and proname like '%wrapped%' order by 1;

-- 3. grants: public RPCs yes for authenticated, no for anon; internals and table no for both
select has_function_privilege('authenticated','public.wrapped_status(uuid,boolean)','execute') auth_status,  -- true
       has_function_privilege('anon','public.wrapped_status(uuid,boolean)','execute') anon_status,         -- false
       has_function_privilege('authenticated','public._wrapped_gate(boolean)','execute') auth_gate,        -- false
       has_table_privilege('authenticated','public.wrapped_settings','select') auth_tbl;                   -- false

-- 4. settings row
select release_at, close_at, christmas_on, show_zero_card, preview_profile_ids from public.wrapped_settings;
-- expect 2026-10-20 07:00:00+00, null, 2026-12-18, true, {AY, Mide}
```

## 5. md5 table (`md5(prosrc)`)

All five bodies on TEST are byte-identical to the file (re-applied to TEST on
15 Oct 2026 after the last edit, see section 6). After a prod apply from the
file, expect exactly these values.

| function | md5 on TEST = md5 of file body |
|---|---|
| `_wrapped_gate` | `57de0ebd9f4e1e0f46ede752d42820a5` |
| `_wrapped_week_points` | `490efd7a02939d558d2ccb01fceebb3e` |
| `wrapped_status` | `65b7d715ae7a843fc68f219cf76d8151` |
| `wrapped_pupil` | `32ffb4b77dad53ced5f011ae2fca4d78` |
| `wrapped_class` | `1210a0867dd53e6205809af63fbb8b2f` |



Dependency bodies, TEST vs production (`md5(prosrc)`):

| dependency | prod | TEST | |
|---|---|---|---|
| `flashcard_card_state` | `ec4834b787ec5c7e4b3408c9876457bb` | same | identical |
| `auth_user_is_member_of_class` | `471f944d66bea8ad3c2c058570b6213b` | same | identical |
| `auth_user_teaches_class` | `eeb08a9afe6d18cce7ad4c53af3718c9` | same | identical |
| `_mrb_week_number` | `76bd0667f32536e1c2764950b3a8f6c2` | `d34a6117e625b5b321486eeacdc40558` | differs: prod has two extra comment lines only |
| `class_stars_board_for_member` | `c309e0419062699c0962e1ccf5d2e279` | `45a942329c57c7c60d46e21896b75bb1` | differs: TEST has the parked catch-up line `a.recipient_ids IS NULL`; prod does not |

The `class_stars_board_for_member` difference is the parked catch-up migration.
Wrapped does not depend on that column (it checks `to_jsonb(a)->'recipient_ids'`),
so it behaves correctly on prod today and after catch-up lands.

## 6. TEST proofs (all inside `begin; … rollback;`, impersonating via `request.jwt.claims` + `set local role authenticated`)

Fixture: class A `ca110000-…-0000000000a1` (WR 8r/Sc1), class B `…a2`. Busy
pupil `…0011` (Bea), light `…0012` (Lia), zero `…0013` (Zed), non-preview pupil
`…0014`, teacher `…0001`, other teacher `…0002` (not on class A). TEST
`release_at` = 2026-10-20 07:00 UTC (future); preview ids = busy, light, zero,
teacher.

**Payloads, preview=true**

| caller | status | cards |
|---|---|---|
| busy | open, role pupil, has_activity true | opener; flashcards secured 11, decks_finished 1; homework stars 610, handed_in 7; best_topic Particle Model of Matter 100% (homework); streak 7 weeks current; top_band 10 (scope year, yg 8); forward cards now 11 projected 25 |
| light | open, has_activity true | opener; homework stars 60, handed_in 1; best_topic Particle Model of Matter 60%; forward homework now 1 projected 2 |
| zero | open, has_activity **false**, show_zero true | `zero:true`, no cards |
| teacher (`wrapped_class`) | open, role teacher | opener active 12/13; homework handed_in 22; flashcards decks 3 secured 21; most_secured "Particle model key words" 100%; revisit Forces 45%; top3 Bea 610, "Ava R." 180, "Ava S." 135 (first name, surname initial on a clash) |

**Privacy and access**

| check | result |
|---|---|
| busy calls `wrapped_status(classB)` (not a member) | `open:false, role:null` |
| busy calls `wrapped_pupil(classB)` | `{"state":"not_member"}` |
| busy (pupil) calls `wrapped_class(classA)` | `{"state":"not_teacher"}` |
| other teacher `…0002` calls `wrapped_class(classA)` | `{"state":"not_teacher"}` |
| `anon` calls each of the three | `ERROR 42501: permission denied for function wrapped_status / wrapped_pupil / wrapped_class` |
| `authenticated` `select * from wrapped_settings` | `ERROR 42501: permission denied for table wrapped_settings` |
| non-preview pupil `…0014`, preview=true, before release | status `open:false, preview:false`; `wrapped_pupil` → `{"state":"closed"}` |

No function takes a pupil id, so there is no parameter through which one pupil
could ask for another's numbers. Other pupils' data never leaves the database;
the top-band card carries a band only (1/5/10 %, or "top 3"), never a rank,
name or score.

**Active but nothing countable (added 15 Oct, commander's review).** A pupil
whose only activity is one lesson quiz in one week would have got the opener
and an empty summary (a share image of nothing). `wrapped_pupil` now returns
`zero:true` whenever no card beyond the opener survives. Proof, in one rolled-back
transaction: one `quiz_scores` row inserted for the zero pupil `…0013`, then as
that pupil `wrapped_status` → `open:true, has_activity:true`, and
`wrapped_pupil` → `zero:true, show_zero:true`, no cards. After rollback the
pupil has 0 quiz rows; the busy pupil's cards are unchanged (opener,
flashcards, homework, best_topic, streak, top_band, forward). Both
`wrapped_pupil` and `wrapped_class` were re-applied to TEST from the file with
`create or replace` (not `apply_migration`, so no second registry row); grants
unchanged.

**Gate flip.** In one transaction: `update wrapped_settings set release_at =
now() - interval '1 minute'`, then as non-preview pupil `…0014`, preview=false:
`wrapped_status` → `open:true, role:pupil, preview:false, has_activity:true`;
`wrapped_pupil.state` → `open`. Rolled back; afterwards `release_at` =
`2026-10-20 07:00:00+00`, unchanged. (The first attempt returned an MCP
`Invalid or expired requestState` error before executing anything; retried once,
passed.)

**Timing** (`explain analyze`, TEST, the fixture world only): `wrapped_pupil`
(busy) 399 ms cold, **26 ms** on rerun; `wrapped_class` (teacher) 45 ms. TEST
data is tiny, so these say nothing about production load; the production
replay in section 7 is the better guide to shape, not speed.

## 7. Production read-only pre-check (15 Oct 2026)

- No `wrapped_settings` table; **0** `wrapped_*` functions; **0** wrapped rows in
  `schema_migrations`. Nothing applied yet.
- Dependencies `flashcard_card_state`, `_mrb_week_number`,
  `auth_user_is_member_of_class`, `auth_user_teaches_class`,
  `class_stars_board_for_member` all exist (md5s in section 5).
- AY profile `b0308282-…` exists (`AY student`); Mide `74db2bf7-…` exists.
- Pupils currently in 2026-27 Rainford classes (academic year
  `6e7cb115-2071-4f1f-9d05-2cc6199cfc18`, not left, not deleted): **1,338**.
  With any activity since 2026-09-01 (a homework hand-in, a flashcard review or
  session, or a quiz_scores row): **45 active, 1,293 with none.** So on
  release day most pupils would see the zero card, which is what
  `show_zero_card` controls (section 9).
  (A second 2026-27 academic year row with 2 pupils belongs to another school
  and is excluded.)

**AY replay** (SELECT-only SQL mirroring the function logic; numbers only):

| card | AY's numbers |
|---|---|
| homework | 4 handed in, 138 stars |
| flashcards | 35 cards secured, 4 decks reviewed, 3 fully secured |
| best topic | best homework topic is Chemical reactions at 60% (under the 70 bar) |
| streak | active in teaching weeks 2 to 7, longest run 6, current week is 7, so "6 weeks, current" |

Note on best topic: the rule is homework >= 70, else a fully secured deck, else
homework >= 50. AY's best homework topic is 60%, and 3 decks are fully
secured, so the real card will be the largest fully secured deck (source
`deck`), not the 60% homework topic. The replay did not name the deck; the
function does. Top-band was not replayed (it needs other pupils' scores); the
real function will compute it.

## 8. Rollback

`supabase/rollbacks/20261014120000_wrapped_rollback.sql`.

**Rehearsal: the MCP declined the unattended DROP, so the rollback is proved by
inspection.** It drops, in order:

1. `function public.wrapped_class(uuid, boolean)`
2. `function public.wrapped_pupil(uuid, boolean)`
3. `function public.wrapped_status(uuid, boolean)`
4. `function public._wrapped_week_points(uuid, uuid, boolean)`
5. `function public._wrapped_gate(boolean)`
6. `table public.wrapped_settings`
7. deletes the registry row `version = '20261014120000'`

The migration creates exactly: `wrapped_settings`, `_wrapped_gate(boolean)`,
`_wrapped_week_points(uuid,uuid,boolean)`, `wrapped_status(uuid,boolean)`,
`wrapped_pupil(uuid,boolean)`, `wrapped_class(uuid,boolean)`. The drop set
equals the create set; signatures match. Functions are dropped before the table
and nothing else depends on any of them. Safe with the site live (the site does
nothing when the RPC is missing).

**Registry version caveat.** The file's version is `20261014120000`, but
`apply_migration` mints its own: on TEST it registered as
`20261013235612`. If prod is applied through the MCP the same will happen, and
the rollback's last line deletes nothing. Delete by name instead:
`select version from supabase_migrations.schema_migrations where name = 'wrapped';`.
With `supabase db push` the version is the file's own.

## 9. Switches Mide can flip later (one UPDATE each)

```sql
update public.wrapped_settings set show_zero_card = false;            -- hide "starts now" card for pupils with no activity
update public.wrapped_settings set release_at = '2026-10-21 08:00 Europe/London';   -- move the opening
update public.wrapped_settings set close_at   = '2026-11-02 08:00 Europe/London';   -- close the button (NULL = stays)
update public.wrapped_settings set christmas_on = '2026-12-18';        -- confirmed; change only if term dates move
```

## 10. TEST residue (left on purpose, for the frontend walk)

- The wrapped objects (table + 5 functions) remain on TEST, registered as
  version `20261013235612`.
- The fixture world, id namespace `ca11…`: 19 auth users and profiles
  (`ca110000-…0001/0002/0011–001d/0021–0024`), 2 classes (`…a1`, `…a2`), 17
  class_members (`ca11b000-…`), 2 class_teachers (`ca11b100-…`), 3 decks
  (`ca11d000-…`), 12 assignments (`ca11a000-…`), 19 assignment_flashcards
  (`ca11f000-…`), 29 submissions (`ca115000-…`), 5 flashcard_sessions
  (`ca11e100-…`), 29 events (`ca11e000-…`), 29 reviews (`ca11c000-…`).
- TEST `wrapped_settings.preview_profile_ids` holds the fixture busy / light /
  zero / teacher ids, and `release_at` is 2026-10-20 07:00 UTC.
- Teardown: `fixture/teardown.sql` (deletes by the snapshotted id list in
  `fixture/ids.json`, never by predicate, and resets preview ids to the two
  prod ids). Fixture account passwords are in `fixture/accounts.env`, not here.

## 11. Uncertainties

- Timing was measured on the tiny TEST fixture only. `wrapped_pupil` is a heavy
  function (it calls `flashcard_card_state` per deck and scans year-wide
  scores for the top band). With 1,338 pupils and release-morning load it is
  untested at production scale. Worth a look at the first `rum_timings` after
  release.
- Top-band (year scope) on production was not replayed, so how often a pupil
  gets a band card is unknown until live.
- With `show_zero_card` switched OFF, a pupil who has activity but nothing
  countable (e.g. one lesson quiz) still sees the button (`has_activity` is
  true) and gets the single "starts now" card. Two pupils on production have
  any quiz_scores rows at all, so this is a corner, not a cohort.
- The MCP's single-result behaviour means every proof returns one result per
  call; none of them shares a transaction with another.
