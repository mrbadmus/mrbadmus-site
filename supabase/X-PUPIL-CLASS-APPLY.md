# Apply sheet — 20261004120000_x_pupil_class_board_and_practice.sql

> ## Mide ruled 4 Oct 2026: top five — the HOLD is lifted
>
> *"Leaderboard should only show top 5 in the class, that way only the best of
> the best are being shown."* `class_stars_board_for_member` now enforces that
> **on the server**:
>
> - **A pupil** gets, for each tab (W01–W04 as keys `"1"`–`"4"`, and `"term"`),
>   **at most five** entries `{id, name, mono, points, me}` and nothing about
>   anyone else. A pupil outside the five gets the five and **no rank, row or
>   score of their own**; `me` is true only on a row that is theirs. A pupil
>   with nothing handed in on time that week is never listed (points must be
>   above 0), so a quiet week returns fewer than five, or none.
> - **A teacher of the class** (an active `class_teachers` row) gets every
>   pupil, ranked, per tab. Anyone else gets `not_member` and nothing.
> - **Points** = the week's percentage (marks over marks possible across that
>   week's sets, first attempts, graded, in on time — the sibling function's
>   `score_pct`). **TERM** = the four weeks added, as the page always added
>   its four chips.
> - **Ties** — exactly five are returned however many tie at fifth. Order:
>   points high to low, then whoever **finished first**, then pupil id (so the
>   order never changes between calls). "Finished" = the pupil's *latest
>   counted hand-in* — for a week tab, the latest `COALESCE(completed_at,
>   submitted_at)` among their on-time graded hand-ins in that week's sets;
>   for TERM, the latest among those in all four weeks. The earlier latest
>   hand-in ranks higher.
> - Membership gate unchanged for pupils. The `practice_rounds` half is
>   unchanged.
>
> The response shape changed from the held draft (`roster` + `points`) to
> `{is_empty, empty_reason, mode: 'pupil'|'teacher'|'none', tabs: {"1".."4",
> "term": [entry…]}}`. The frontend on `feat/x-pupil-class` reads the new
> shape; the old frontend commit must not ship against this function.

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
3. `public.class_stars_board_for_member(uuid)` — NEW function. The class
   board: per tab (four teaching weeks keyed 1..4, oldest..newest, 4 = now,
   plus term) the top five for a pupil, everyone for a teacher. See the
   ruling at the top.
4. `public.practice_rounds` — NEW table + index + RLS (SELECT only; no
   client-writable policy).

## Before/after (TEST, qeppkiswvclkkwbxmlok)

| object | before | after |
|---|---|---|
| `class_stars_leaderboard_for_member` | `9271514c8cf9296e308a4dd5e8169bf5` (= production's current body, verified equal before this migration) | `40d975e212de315132082815b5067b88` |
| `class_stars_board_for_member` | (did not exist) | `c309e0419062699c0962e1ccf5d2e279` (top-five version; the held whole-roster draft was `348689c98335d9f87820ba7644cbc931`, never applied to production) |
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
| `supabase/migrations/20261004120000_x_pupil_class_board_and_practice.sql` | `b22aa03a4fc19676e42ad22e4061f88f` |
| `supabase/rollbacks/x_pupil_class_board_and_practice_rollback.sql` | `f88dcf3a2c8bd136769259b03a14e575` |

Production pre-check (read-only, 4 Oct 2026): `class_stars_leaderboard_for_member`
is still at md5(prosrc) `9271514c8cf9296e308a4dd5e8169bf5`, the body this
migration was built from; `class_stars_board_for_member`, `_mrb_week_number` and
`practice_rounds` do not exist yet. No Render restart is needed after applying:
`POST /api/class/practice/round` tries the insert on every call and simply stops
answering 503 once the table exists.

Independent of `X-REOPEN` — either may be applied first. Once both are on,
the leaderboard's points read `assignment_submissions.score`, which `X-REOPEN`
makes the pre-reveal counted score; that is the intended figure.

## Top-five rehearsal on TEST (4 Oct 2026, qeppkiswvclkkwbxmlok)

Seed: the 17-pupil throwaway class shaped like 10h/Ph1 (week 4 and week 5
sets, today = teaching week 5) with varied scores and a tie at fifth — week 5:
Pupil 7 100, Pupil 1 90, Pupil 4 80, then Pupils 5, 6, 2 all on 70 (handed in
09:00, 11:00, 12:00 on 3 Oct); Pupil 10 60; Pupil 3 50. Week 4: Pupil 7 100,
Pupils 1–6 on 80 (Pupil 2 handed in a day earlier than the rest), Pupil 9 60,
Pupil 10 40, Pupil 8 late (counts 0). A teacher added to `class_teachers`.

| call as | result |
|---|---|
| Pupil 17 (17th, nothing handed in) | every tab ≤ 5 rows (W01/W02 empty; W03, W04, TERM = 5), `me` true on **zero** rows, no rank/score of their own |
| Pupil 4 (3rd in W04) | W04 and TERM = 5 rows, `me:true` exactly on Pupil 4's row in each tab they are in |
| W04 tie at fifth | Pupil 5 (09:00) and Pupil 6 (11:00) kept, Pupil 2 (12:00) out — exactly five |
| TERM tie at fifth (150 each: 5, 6, 2) | latest-hand-in order 5 (09:00), 6 (11:00), 2 (12:00): 5 and 6 kept |
| W03 six-way tie on 80 | Pupil 2 first (earliest hand-in), then the rest by id; five rows |
| Teacher | `mode:"teacher"`, 17 rows on every tab, `me` false everywhere |
| A random uuid | `not_member`, empty tabs |

`md5(prosrc)` of the deployed function on TEST = `c309e0419062699c0962e1ccf5d2e279`,
equal to the body in the migration file (checked byte-for-byte).
The migration does not touch `flashcard_card_state` or `flashcard_record`
(grep of migration + rollback finds neither), so the "stays secured"
production state (`ec4834b7…`, `118ade9a…`) is unaffected by this unit.
