# Catch-up — report (14 Oct 2026)

Mide's brief: a teacher sets a lesson plus questions to one or two NAMED
pupils. It shows as **Catch-up** on their class page, lesson first, then the
questions. The teacher picks the lesson (Mide, 13 Oct). Build contract:
`docs/catch-up/PLAN.md`.

## What shipped

| side | where | state |
|---|---|---|
| backend | `mrbadmus---backend` 9ec3907 (server.js, test_catch_up.js) | live on Render |
| site | this branch → main (teacher side, pupil side, proof rig) | see the push commit |
| database | `feat/catch-up-migration` — `supabase/CATCH-UP-APPLY.md` | **TEST only; production waits for Mide** |

The site and the backend work **with or without** the migration. Both probe for
`assignments.recipient_ids`; when it is absent, nothing is a catch-up and the
Catch-up option is not offered. That makes today's push a no-op for every
teacher and pupil until the migration is applied and Render is restarted.

## The design, in five lines

1. One new column, `assignments.recipient_ids uuid[]`. NULL means the whole
   class, which is every existing row. A list means a catch-up for exactly
   those pupils.
2. A catch-up is an ordinary assignment (`mcq_set`, `source='teacher'`). It
   uses the same questions, submissions, `/answer`, `/complete` and marking.
   Its lesson is its scope (`scope_kind='subtopic'`, `scope_ref` = the lesson
   slug).
3. **Rule 7.** `scope_kind`/`scope_ref` were made for Set work v2 (MRB-335),
   not for catch-up. They are reused unchanged because the lesson IS a
   subtopic scope, so no lesson column was added.
4. Visibility is enforced in the database by a restrictive SELECT policy,
   `assignments_catch_up_audience`. It also hides the catch-up's
   `assignment_questions`. Three SECURITY DEFINER functions each gained one
   line, `AND a.recipient_ids IS NULL`, so a catch-up never counts in the stars
   board, the stars leaderboard or the teacher rollup.
5. Every backend read that hands work to a pupil applies the same audience
   rule. A classmate gets a 404 on the catch-up's id from every route.

## Choices I made (Mide can overturn any)

- **The lesson is embedded with a same-origin frame (v1).** The brief allowed
  this. The existing lesson page loads inside the sheet. CSS injected from the
  class page hides the lesson's own header, footer and tutor chat, so no lesson
  file was edited. On a phone it is a full-screen sheet under the pupil's own
  header; from 900px wide it is a panel.
  - Links inside the lesson stay in the frame.
  - Off-site links open a new tab.
  - Nothing navigates the pupil away from the class page.
- **Questions come from the lesson itself**, not the lesson's parent topic or
  unit. Set work's Detail step (tier, preview, swap, count) is unchanged.
- **The lesson picker** starts filtered to the class's current topic: this
  week's scheme-of-work entry, or else the topic of the most recent
  whole-class set. Search reaches every lesson the class's tree holds.
- **A catch-up releases immediately.** There is no scheduled release.
- **Up to 10 pupils** per catch-up in the app. The database allows 60.
- **A pupil's own stats on their class page include their catch-ups.** The
  brief says it "DOES show on each named pupil's own record". The class-wide
  figures, the teacher rollup, the stars and Wrapped's class totals do not
  include them.
- **Wrapped.** The Wrapped session excludes catch-ups from the class totals.
  A pupil's own Wrapped still counts their catch-up work. They will change
  that if Mide wants.
- **"Particles and their behaviour" is a KS3 unit (C1), not a lesson.**
  Searching that name lists C1's six lessons, and the proof picked the first
  one, "The particle model".

## Proof

### Classmate RLS proof (TEST, real class 8X1, everything rolled back)

```sql
do $$
declare
  v_class uuid := '2a000000-0000-0000-0000-000000000001';
  v_a uuid; v_b uuid; v_t uuid; v_tpl assignments%rowtype; v_id uuid; r text := '';
  n1 int; n2 int; n3 int;
begin
  select student_id into v_a from class_members where class_id=v_class and left_at is null and deleted_at is null order by student_id limit 1;
  select student_id into v_b from class_members where class_id=v_class and left_at is null and deleted_at is null and student_id<>v_a order by student_id limit 1;
  select teacher_id into v_t from class_teachers where class_id=v_class and ended_at is null limit 1;
  select * into v_tpl from assignments where class_id=v_class and kind='mcq_set' limit 1;
  insert into assignments(class_id, teacher_id, subject_id, school_id, key_stage, year_group, topic, title, quiz_type, kind, source, auto_generated, due_at, release_at, scope_kind, scope_ref, recipient_ids)
  values (v_class, v_t, v_tpl.subject_id, v_tpl.school_id, v_tpl.key_stage, v_tpl.year_group, 'rls-proof', 'Catch-up RLS proof', 'subtopic_quiz', 'mcq_set', 'teacher', false, now()+interval '7 days', now()-interval '1 minute', 'subtopic', 'particles-and-their-behaviour', array[v_a])
  returning id into v_id;
  insert into assignment_questions(assignment_id, position, source_ref, band) values (v_id, 1, 'rls-proof-q', 'standard');

  execute 'set local role authenticated';
  perform set_config('request.jwt.claims', json_build_object('sub', v_a, 'role','authenticated')::text, true);
  select count(*) into n1 from assignments where id=v_id; select count(*) into n2 from assignment_questions where assignment_id=v_id;
  select count(*) into n3 from assignments where class_id=v_class;
  r := r || format('RECIPIENT sees assignment=%s questions=%s classRows=%s | ', n1, n2, n3);

  perform set_config('request.jwt.claims', json_build_object('sub', v_b, 'role','authenticated')::text, true);
  select count(*) into n1 from assignments where id=v_id; select count(*) into n2 from assignment_questions where assignment_id=v_id;
  select count(*) into n3 from assignments where class_id=v_class;
  r := r || format('CLASSMATE sees assignment=%s questions=%s classRows=%s | ', n1, n2, n3);

  perform set_config('request.jwt.claims', json_build_object('sub', v_t, 'role','authenticated')::text, true);
  select count(*) into n1 from assignments where id=v_id; select count(*) into n2 from assignment_questions where assignment_id=v_id;
  r := r || format('TEACHER sees assignment=%s questions=%s', n1, n2);
  raise exception 'PROOF (rolled back): %', r;
end $$;
```

Result: `RECIPIENT sees assignment=1 questions=1 classRows=7 | CLASSMATE sees
assignment=0 questions=0 classRows=6 | TEACHER sees assignment=1 questions=1`.

### End to end on TEST — `tools/catch_up_live.py`: **450 PASS, 0 FAIL**

The run builds a throwaway world: class `8r/Sc1-cu<run>`, a teacher, AY and
one classmate. The class has a homework that the classmate has handed in and
a flashcard deck. The backend runs locally from the catch-up backend worktree
against TEST. The rig refuses to write unless the service key's `ref` is
TEST's. Teardown is by a snapshotted id list, and a re-query finds nothing
left behind.

- **Teacher, real UI:** Set work → Catch-up → tick AY → search → pick the
  lesson → 10 questions, swap one → due date → Set work.
  - The POST carries `pupil_ids=[AY]`, and the row has `recipient_ids=[AY]`.
  - The class figures did not move.
- **Bench:** all four cases at phone 390 and desktop 1280, light and dark.
  - Layout mode, the "Catch-up" label (never "Homework"), touch target
    ≥44px, contrast ≥4.5, no sideways scroll, no console errors.
  - Overdue shows "Finish it" and "Was due".
- **Phone sheet:**
  - The lesson opens inside the class page under the pupil's header, and the
    lesson's own chrome is hidden.
  - "Start the questions" goes to the questions.
  - The "Lesson" button reopens the lesson over question 2; closing returns
    to question 2 with nothing lost.
- **AY answers all 10** through the normal UI. The submission is complete and
  the score is stored.
- **Teacher after:**
  - The week card reads "Catch-up · 1 pupil" with the lesson and AY's 4/10.
  - Handed-in counts, the Students and Assignments tables, the header and
    `teacher_class_rollup_v2` are identical to before.
  - AY's student screen lists the catch-up; the classmate's does not.
  - Answer Breakdown reads "Pupil 1 of 1".
- **Classmate:**
  - The page text, bench, bell and notifications are identical to before.
  - Their own token reads 0 rows of the catch-up, its questions and AY's
    submission.
  - Every assignment API returns 404 for them and 200 for AY, and the refused
    calls wrote nothing.
- **Stars board and leaderboard:** unchanged for both pupils. The board held
  real points, so this is not an empty-equals-empty pass.

Screenshots (before and after, all four bench cases, the sheet, the teacher
card): `~/tmp/catch-up-live/shots/` (46 files).

### Unit and gate results
- `test_catch_up.js` 99 passed, 0 failed.
- `test_set_work_v2.js` 209 passed, 1 skipped (unchanged).
- `set_work_unit` 169 passed.
- `week_truth` PASS.
- The gate run recorded for the push is listed in the push commit's receipts.

## Two defects the proof run found, both fixed

1. **The pupil's header could vanish under the sheet.** The header scrolls
   with the page, so a pupil who had scrolled down to the catch-up card got a
   sheet covering the whole phone. The sheet now scrolls the page to the top
   before opening, and puts the pupil back on close.
2. **Answer Breakdown walked the whole class roster** for a catch-up (found by
   reading the code; the old behaviour was not driven as a baseline). It now
   walks only the named pupils, and "Pupil 1 of 1" is asserted.

## Deviations

- **The spec file was not read.** `claude/catch-up-spec.md` lives in a
  claude.ai project. It is in neither repo, and Drive access was refused, so
  I built from the pasted brief, which carries the rules verbatim.
- **No Playwright.** It is not installed, and its browsers would take about
  500 MB on a disk with 3–4 GB free. The proof uses the repo's own
  headless-Chrome CDP rig, the same pattern as `fc_bench_live.py`, with the
  same viewports, themes and assertions.
- **The rollback was not rehearsed on TEST.** The connector declines `DROP`
  unattended, the same as MRB-353. The rollback soft-deletes catch-ups first
  so none can surface to a whole class, then restores the three functions to
  production's "before" bodies (md5s are in the apply sheet).
- **Production path not driven end to end.** Without the column the probes
  hide everything. That is today's live behaviour and it is what pages do
  now, but no throwaway world ran against a column-less database.
- **jsdelivr flake.** `cdn.jsdelivr.net` timed out on about 3 in 25 page
  loads on this machine. The rig reloads on that exact error, and no
  assertion was weakened.

## Ordering hazard (also in the apply sheet)

`feat/x-mig-pupil-class` (the stars functions) and the MRB-351 rollup v2 file
are already live on production. Re-running either after this migration would
quietly remove the catch-up line. Any future migration that redefines those
three functions must keep `AND a.recipient_ids IS NULL`.
