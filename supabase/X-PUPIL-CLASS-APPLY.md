# Apply sheet — 20261004120000_x_pupil_class_board_and_practice.sql

> ## ⛔ HOLD — DO NOT APPLY UNTIL MIDE RULES (commander, 4 Oct 2026)
>
> `class_stars_board_for_member` returns **every active pupil's weekly score
> percentage to every member of the class** — the whole roster, struggling
> pupils included. The function it sits beside, `class_stars_leaderboard_for_member`,
> only ever named pupils who cleared the bar (every set on time AND ≥ 75 %).
> Showing each child's homework score to their classmates is a safeguarding /
> product decision, not an engineering one. Design's board draws the whole
> class ranked, which is what this implements, but Mide has not ruled on it.
>
> Options for Mide: (1) apply as is — whole class, real percentages;
> (2) whole class, but a pupil sees only their OWN figure and classmates'
> names/ranks without percentages; (3) only pupils who cleared the bar that
> week are listed (the old rule, per week). The frontend that is live on main
> works with (1) as written; (2)/(3) are a change to this function only.
>
> The practice_rounds half of this migration (table + RLS) has no such
> question and could be split out and applied on its own if wanted.


Branch: `feat/x-mig-pupil-class` (site repo). PARKED — not merged to main.
Do not apply to production until the frontend branch (`feat/x-pupil-class`)
and backend branch (`feat/x-pupil-class`, backend repo) have both merged.

## What it does, in order

1. `public._mrb_week_number(date, timestamptz)` — new helper, SQL mirror of
   `assignment-compose.js`'s `weekZeroFor()`/`currentTeachingWeek()`
   (Sunday-rollover teaching weeks). Not granted to any role.
2. `public.class_stars_leaderboard_for_member(uuid)` — REDEFINED in place
   (same name/signature/return shape). Fixes the week rule: "this week" is
   now the assignment's SET week (`academic_week`, falling back to a
   teaching week computed from `release_at`/`created_at`), not a `due_at`
   window; on-time drops the `submitted_at >=` lower bound.
3. `public.class_stars_board_for_member(uuid)` — NEW function. Per-week
   points series (score_pct) for the whole active roster, last four
   teaching weeks, keyed 1..4 (oldest..newest, position 4 always "now").
4. `public.practice_rounds` — NEW table + index + RLS (SELECT only; no
   client-writable policy).

## Before/after (TEST, qeppkiswvclkkwbxmlok)

| object | before | after |
|---|---|---|
| `class_stars_leaderboard_for_member` | `9271514c8cf9296e308a4dd5e8169bf5` (= production's current body, verified equal before this migration) | `40d975e212de315132082815b5067b88` |
| `class_stars_board_for_member` | (did not exist) | `348689c98335d9f87820ba7644cbc931` |
| `_mrb_week_number` | (did not exist) | `d34a6117e625b5b321486eeacdc40558` |
| `practice_rounds` | (did not exist) | table + 1 index + RLS enabled + 1 SELECT policy |

Rehearsed in FOUR separate `apply_migration` calls (helper function, then
leaderboard redefine, then board function, then table+RLS) rather than one —
the table/RLS statements were originally written with `CREATE TEMP TABLE`
inside the board function, which Postgres refuses inside a `STABLE`
function ("CREATE TABLE AS is not allowed in a non-volatile function"). Found
by this exact rehearsal; the function was rewritten to three CTEs (no DDL)
before any of this landed in the committed migration file, which already
carries the corrected, CTE-only body.

## Verification queries run on TEST

- `to_regclass('public.practice_rounds')`, `to_regprocedure(...)` for both
  new functions — all resolve.
- `relrowsecurity` on `practice_rounds` — `true`; exactly 1 policy
  (`practice_rounds_select`).
- Impersonated a pupil (`set_config('request.jwt.claim.sub', …, true)` under
  `role authenticated`) against a throwaway 17-pupil class shaped like
  production's 10h/Ph1 (see RESULT-C.md for the exact fixture): both
  functions return correct, class-membership-gated data; a non-member gets
  `not_member` from both; a pupil reading `practice_rounds` sees only their
  own row, a different pupil in the same class sees none.
- Cross-checked `_mrb_week_number('2026-09-06', now())` against the
  backend's own `currentTeachingWeek()` (assignment-compose.js) for the same
  academic year — both return `5` for 2026-10-04. The two clocks agreeing is
  load-bearing: `practice_rounds.teaching_week` is stamped by the backend
  using its JS clock, read back by the SQL clock above.

## Rollback

`supabase/rollbacks/x_pupil_class_board_and_practice_rollback.sql` — drops
`practice_rounds` and its policy, drops `class_stars_board_for_member` and
`_mrb_week_number`, and documents (rather than duplicates) restoring
`class_stars_leaderboard_for_member`'s pre-migration body by re-running
`20260524225500_class_stars_leaderboard_for_member.sql`'s own
`CREATE OR REPLACE`.

## What is safe before this migration is applied (prod today)

- `shared/student-data.js`'s new `class_stars_board_for_member` RPC call is
  wrapped in `settle()`, same as every sibling read — a missing function
  (`42883`/`PGRST202`) resolves to `{ data: null, error }`, logged, and
  `board` is `null`. `shared/student-live.js` treats `board == null` or
  `board.is_empty` identically: `roster = []`, `weekPts = {}`, which is the
  EXACT pre-existing (safe) shape the page already shipped with.
- The backend's `POST /api/class/practice/round` answers `503
  { reason: 'not_ready' }` on a missing `practice_rounds` table (`PGRST205`/
  `42P01`), never a 500; the page's sink treats any non-2xx the same —
  no visible change, tile keeps its last value.
- `class_stars_leaderboard_for_member`'s redefinition is the one piece that
  changes behaviour the INSTANT it is applied (same function name, same
  callers) — but nothing on the pupil class page reads its answer any more
  (see `shared/student-data.js`'s comment at the old call site), so the only
  consumer affected is `shared/teacher-data.js`, which benefits from the
  same week-rule fix.

## Fingerprints (added by the commander, 4 Oct 2026)

| file | md5 (file bytes) |
|---|---|
| `supabase/migrations/20261004120000_x_pupil_class_board_and_practice.sql` | `d3b3d72ad3c7bb17435dbb4eb3774978` |
| `supabase/rollbacks/x_pupil_class_board_and_practice_rollback.sql` | `263dc663425683ec7c8e6e7044a814cf` |

Production pre-check (read-only, 4 Oct 2026): `class_stars_leaderboard_for_member`
is still at md5(prosrc) `9271514c8cf9296e308a4dd5e8169bf5`, the body this
migration was built from; `class_stars_board_for_member`, `_mrb_week_number` and
`practice_rounds` do not exist yet. No Render restart is needed after applying:
`POST /api/class/practice/round` tries the insert on every call and simply stops
answering 503 once the table exists.

Independent of `X-REOPEN` — either may be applied first. Once both are on,
the leaderboard's points read `assignment_submissions.score`, which `X-REOPEN`
makes the pre-reveal counted score; that is the intended figure.
