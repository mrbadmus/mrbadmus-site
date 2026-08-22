-- profiles: scope what a student may write on their own row.
--
-- MRB · 22 Aug 2026. Closes a live privilege-escalation path.
--
-- ── THE HOLE ────────────────────────────────────────────────────────────
--
-- `Users can update own profile` is `UPDATE ... USING (auth.uid() = id)` with
-- no `WITH CHECK` and no column scope, and `authenticated` holds `UPDATE` on
-- all thirty columns. Row-level security is exactly that — ROW level. It says
-- which row you may write. It has never said which COLUMNS, and nothing else
-- was saying it either.
--
-- That would be survivable if `profiles.role` were dead. It is not.
-- `auth_user_has_scope()` — SECURITY DEFINER, and the function every newer
-- policy reads — still carries its M1 dual-read fallback:
--
--     or (p_scope = 'school_admin' and exists (select 1 from public.profiles p
--                                              where p.id = auth.uid()
--                                                and p.role = 'admin'));
--
-- So `role` is a live grant of scope that its holder can write. Demonstrated on
-- the test project and reverted: a roster-imported student set their own
-- `role = 'admin'`, `auth_user_has_scope('school_admin')` went false → true,
-- and the profiles they could read went from 1 to 39.
--
-- ── WHY GRANTS AND NOT A POLICY ─────────────────────────────────────────
--
-- The instinct is to write the column list into the policy. Postgres will not
-- do it: a policy's `WITH CHECK` sees only the NEW row, never the OLD one, so
-- it cannot say "role must not have changed" without reading the table back —
-- and a subquery on `profiles` inside a policy on `profiles` recurses.
--
-- Column privileges are the mechanism the database already has for this, they
-- are checked BEFORE row security, and they are declarative. So the column
-- scope is a GRANT, and the policy keeps its one honest job: the row is yours.
--
-- ── THE LIST, AND HOW IT WAS DRAWN ──────────────────────────────────────
--
-- Every column a student's browser actually writes, and nothing else. The one
-- client-side write path to this table is the fallback upsert in
-- `profile-setup.html` (the primary path is `PUT /api/profile` on the backend,
-- which holds the SERVICE ROLE key and is untouched by any of this), plus the
-- new `bench_theme`.
--
--   id             the upsert carries it; the policy's WITH CHECK below pins
--                  it to auth.uid(), so it can only ever be set to itself
--   updated_at     written by the same upsert
--   first_name, last_name, avatar_url, school_name, year_group, exam_board,
--   science_pathway, tier, target_grade, strengths, weaknesses, personal_note
--                  the profile wizard's own fields — self-declared, presentation
--   bench_theme    the student's chosen bench theme
--
-- EXCLUDED, and why:
--
--   role, school_id, department, key_stage    identity and enrolment — the
--                  four `auth_user_*` functions read these to decide scope
--   username, last_username_change_at         written only by `set_username`,
--                  a SECURITY DEFINER function that re-checks moderation, the
--                  30-day lock and availability. Definer's rights, so it does
--                  not need this grant and must not have it
--   total_xp, streak_days, last_active        server-owned counters. Nothing
--                  client-side writes them; a student who could would be
--                  marking their own homework
--   created_at, deleted_at, external_student_id, school_code, teacher_name,
--   recent_results, display_name              nothing client-side writes them
--
-- `anon` loses UPDATE outright. RLS already refused it — `auth.uid()` is null,
-- so `auth.uid() = id` is false — but a grant that is only ever saved by a
-- policy is a grant waiting for the policy to change.
--
-- `service_role` is deliberately NOT touched. It holds its own column grants,
-- and BYPASSRLS does not bypass column privileges, so the backend's writes go
-- on working exactly as they did.

revoke update on public.profiles from authenticated, anon;

grant update (
  id,
  updated_at,
  first_name,
  last_name,
  avatar_url,
  school_name,
  year_group,
  exam_board,
  science_pathway,
  tier,
  target_grade,
  strengths,
  weaknesses,
  personal_note,
  bench_theme
) on public.profiles to authenticated;

-- The policy states its `WITH CHECK` rather than inheriting it.
--
-- Postgres already uses `USING` as the `WITH CHECK` when none is given, so this
-- changes no behaviour today. It is written down so that the next person to
-- widen `USING` — to let a teacher write a student's row, say — does not widen
-- what a row may be turned INTO at the same time, silently, in one edit.
alter policy "Users can update own profile" on public.profiles
  using (auth.uid() = id)
  with check (auth.uid() = id);
