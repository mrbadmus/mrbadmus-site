-- MRB-306 Phase 2b/3 — the author of a child's feedback, by name.
--
-- ⚠️ FILENAME VERSION IS NOT COSMETIC. Applied to prod via MCP
-- `apply_migration`, which records its OWN `schema_migrations` version —
-- 20260904214520. The filename must match it or `db push` re-applies this.
-- (CLAUDE.md's migrations-toolchain rule; the trap is written up in memory as
-- `project_migration_version_drift`.)
--
-- ── the gap this closes ─────────────────────────────────────────────
-- A student has no read policy on a teacher's `profiles` row. That gap is
-- why `class_teachers_for_viewer` and `student_reminders_for_viewer` exist,
-- and `class_teachers_for_viewer` deliberately returns display names WITHOUT
-- ids — "a student surface has no use for an identifier it cannot act on".
-- So on a CO-TAUGHT class the student page could not say which of two
-- teachers wrote a comment, and signed it "your teacher". On prod that is 9
-- of 73 classes.
--
-- Taking the first name in the list would have put one teacher's words under
-- another teacher's name, in front of a child, which is worse than not
-- naming them. Hence a mapping, scoped inside the database.
--
-- ── what it is scoped to, and why that is not a widening ────────────
-- `s.student_id = auth.uid()`. The caller learns the name of a teacher who
-- has written to them personally, on this assignment, and of nobody else.
-- Passing somebody else's assignment id returns `{}`; so does calling it as
-- a teacher, as an admin, or with a uuid that names nothing.
--
-- ⚠️ AND IT DISCLOSES NOTHING THAT WAS NOT ALREADY REACHABLE, which was
-- MEASURED rather than assumed and corrects the previous unit's premise.
-- `public.display_name_for(uuid)` has been on prod all along: STABLE
-- SECURITY DEFINER, it returns the display name of any teacher who teaches
-- a class the caller is a member of. The name was therefore already
-- available to exactly this caller, one id at a time. This function is
-- STRICTLY TIGHTER than that one (feedback AUTHORS only, where
-- `display_name_for` names every teacher of the class), is one round trip
-- for N authors instead of N, and — unlike `display_name_for` — still names
-- the person who wrote to a child after they have stopped teaching the
-- class. See the MRB-306 Phase 3 report; `display_name_for`'s looser grants
-- (EXECUTE to PUBLIC and to `anon`) are recorded there as an open item.
--
-- ── proven on TEST with real signed-in sessions ─────────────────────
-- Not with the service role, which bypasses RLS and runs `auth.uid()` as
-- NULL — a service-role call to this function returns `{}` for every input
-- and proves nothing. Thirteen probes from real JWTs on a purpose-built
-- throwaway stack (two schools, a genuinely co-taught class, two students
-- with a comment each from a DIFFERENT one of the two co-teachers):
--
--   student A on the shared assignment → exactly the teacher who wrote to A
--   student B on the SAME assignment   → exactly the OTHER teacher
--   both co-teachers writing to A      → both, distinguishable by id
--   a student in another school        → {}
--   a co-teacher; a teacher of neither → {}
--   anon (no bearer)                   → 401, 42501 permission denied
--   an unknown uuid; NULL              → {}, no error
--   a soft-deleted comment             → {}, and back on restore
--   the same student reading profiles  → 0 rows for either teacher,
--                                        so `profiles` RLS is untouched
--
-- Every throwaway row destroyed afterwards, counted back to the baseline.

create or replace function public.submission_feedback_authors_for_viewer(
  p_assignment_id uuid)
returns jsonb
language plpgsql
stable
security definer
set search_path = public
as $function$
declare
  v_rows jsonb;
begin
  if p_assignment_id is null then
    return jsonb_build_object('authors', '{}'::jsonb);
  end if;

  select coalesce(jsonb_object_agg(t.teacher_id::text, t.display_name),
                  '{}'::jsonb)
    into v_rows
  from (
    select distinct
           sf.teacher_id,
           coalesce(
             nullif(btrim(p.display_name), ''),
             nullif(btrim(coalesce(p.first_name, '') || ' ' ||
                          coalesce(p.last_name, '')), ''),
             'Your teacher')                        as display_name
      from public.submission_feedback   sf
      join public.assignment_submissions s on s.id = sf.submission_id
      left join public.profiles          p on p.id = sf.teacher_id
     where s.assignment_id = p_assignment_id
       and s.student_id    = auth.uid()
       and s.deleted_at   is null
       and sf.deleted_at  is null
  ) t;

  return jsonb_build_object('authors', v_rows);
end;
$function$;

-- ⚠️ THE GRANT IS THE TIGHT ONE, matching `student_reminders_for_viewer`
-- rather than `class_teachers_for_viewer`. The latter carries EXECUTE to
-- PUBLIC and to `anon`; that is harmless there and here alike, because
-- `auth.uid()` is NULL for an anonymous caller and the scope collapses to
-- nothing — but a function should not rely on its body to refuse a caller
-- the grant could have refused first.
revoke all on function public.submission_feedback_authors_for_viewer(uuid) from public;
revoke all on function public.submission_feedback_authors_for_viewer(uuid) from anon;
grant execute on function public.submission_feedback_authors_for_viewer(uuid) to authenticated;
grant execute on function public.submission_feedback_authors_for_viewer(uuid) to service_role;

comment on function public.submission_feedback_authors_for_viewer(uuid) is
  'MRB-306 Phase 2b/3. teacher_id -> display name, for exactly the submission_feedback rows the CALLING STUDENT may already read on this assignment (their own submissions only). Not an id->name dump: a caller learns the name of a teacher who has written to them personally and of nobody else. Exists because a student has no read policy on a teacher''s profiles row, and class_teachers_for_viewer returns names WITHOUT ids, so a co-taught class could not name the author of a comment.';
