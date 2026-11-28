# Class membership — what to apply to production, in order

Rehearsed on TEST (`qeppkiswvclkkwbxmlok`) on 27 Nov 2026. Nothing here has
touched production (`urklkrwevjtlfbwnipjn`). Production's live `class_members`
policies, `teacher_class_rollup_v2` and the helper functions were read
(read-only) first; TEST and production agree on everything these files touch.

## 1. Migration — the functions

`supabase/migrations/20261127120000_class_membership_rpcs.sql`

Adds only functions. No table, column, index or policy changes.
Rollback: `supabase/rollbacks/20261127120000_class_membership_rpcs_rollback.sql`.

## 2. Migration — "missing" respects the join date

`supabase/migrations/20261127120100_rollup_missing_respects_joined_at.sql`

Edits one expression inside `teacher_class_rollup_v2` in place, and refuses
(raises, changes nothing) if production's function text has drifted.
Rollback: `supabase/rollbacks/20261127120100_rollup_missing_respects_joined_at_rollback.sql`.

## 3. Edge function — roster-import

Deploy `supabase/functions/roster-import/index.ts` (verify_jwt stays `true`).
It calls `class_membership_batch`, so deploy it **after** step 1. Until it is
deployed, the old function keeps working exactly as before.

## 4. Push the frontend

Only after 1–3. The new buttons ask the database whether to appear
(`can_manage_class_membership`); before step 1 that call fails and the
buttons simply do not show, so a frontend that lands early is harmless.

## Proof

- `tools/membership_rpc_check.sql` — 27 checks, rolls itself back. On TEST:
  ALL PASS (anon, a pupil and a teacher refused with nothing changed; move,
  move back with no duplicate, batch all-or-nothing, audit rows, undo once).
- `tools/class_membership_drive.js` — the walk in a real browser, with
  `supabase/seeds/class_membership_drive_seed.sql` /
  `class_membership_drive_teardown.sql`.
