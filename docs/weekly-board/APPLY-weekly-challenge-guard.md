# APPLY: weekly-challenge homework guard

Status: rehearsed on TEST (qeppkiswvclkkwbxmlok). NOT applied to production.
Production (urklkrwevjtlfbwnipjn) is for the platform chat to apply.

## What it does
1. Re-creates `public.teacher_class_rollup_v2(uuid[],timestamptz,jsonb)` identical to the deployed body plus ONE line in the `asg` CTE, so assignments with `quiz_type = 'weekly_challenge'` are out of every class figure.
2. Adds `public.weekly_challenge_homework_ready()` (returns true; execute granted to authenticated, service_role). The backend shows "Set as homework" only when it exists.

## Why
A weekly-challenge homework row has no assignment_questions and never any assignment_submissions (pupils play it on /weekly-challenge). Once its deadline passed, the rollup would count it as a closed paper with no cell, so every pupil would show as missing work on the class card.

## Files
- `supabase/migrations/20261020232701_weekly_challenge_homework_guard.sql`
- `supabase/rollbacks/20261020232701_weekly_challenge_homework_guard_rollback.sql`

## The one-line diff (function body)
```diff
        AND a.recipient_ids IS NULL   -- ⊕ catch-up: out of every class figure
+       AND a.quiz_type IS DISTINCT FROM 'weekly_challenge'  -- ⊕ weekly challenge homework: played on /weekly-challenge, never submitted here
        AND (cls.all_work
```
Proof: the migration's body minus that line has md5 `250f89ed0247c8ade3efdc1874695fe3` (the deployed prosrc). The body with the line has md5 `c1daba7878fa7d6850597ffb8d8a2916`, which is what TEST reports after apply.

## Pre-check (production, read-only)
```sql
select md5(prosrc) from pg_proc
 where oid = 'public.teacher_class_rollup_v2(uuid[],timestamptz,jsonb)'::regprocedure;
```
Must be `250f89ed0247c8ade3efdc1874695fe3`. If not, STOP and regenerate the migration from the then-current body.

## Apply
`supabase db push` against production, or MCP `apply_migration` (name `weekly_challenge_homework_guard`) with the file's contents, naming project `urklkrwevjtlfbwnipjn`.

## Post-checks
- `md5(prosrc)` is now `c1daba7878fa7d6850597ffb8d8a2916`.
- `select public.weekly_challenge_homework_ready();` returns true.
- Grants on the rollup unchanged: `=X, anon=X, authenticated=X, postgres=X, service_role=X` (CREATE OR REPLACE keeps them); `prosecdef` true; `proconfig` = `search_path=public`, `TimeZone=UTC`.

## Rollback
Apply `supabase/rollbacks/20261020232701_weekly_challenge_homework_guard_rollback.sql`: drops `weekly_challenge_homework_ready()` first, then restores the previous definition (md5 back to `250f89...`).

## TEST rehearsal evidence (20 Oct 2026)
- md5 after apply = `c1daba78...`; grants identical before/after; ready() = true.
- Class `ee000000-0000-0000-0000-000000000401` (6 pupils), caller teacher `...1002`, rollup called with `now()`.
  - Baseline: assignment_count 0, missing_marked pupils 0, papers 0.
  - With a past-due, past-release `weekly_challenge` row (source teacher, auto_generated false): identical to baseline.
  - Control, same row retyped `topic_quiz`: assignment_count 1, completion_pct 0, 6 pupils missing, papers 1. So the guard is what holds the figures steady.
- Leftover on TEST: assignment `ee000000-0000-0000-0000-00000000f001` ("GUARD TEST", quiz_type weekly_challenge). Its delete was declined by the permission system; remove by id: `delete from assignments where id = 'ee000000-0000-0000-0000-00000000f001';`
