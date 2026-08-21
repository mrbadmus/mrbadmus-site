-- W4, ruled 22 Aug 2026: a student may answer again, BOTH attempts are kept,
-- and the BEST counts. That needs a constraint, not a convention — without one
-- the old route wrote a brand new row on every press and nothing merged them.
create unique index if not exists assignment_submissions_attempt_uniq
  on public.assignment_submissions (assignment_id, student_id, attempt_no)
  where deleted_at is null;

-- W1: each answer appends its OWN row and changing an answer UPDATES that row
-- rather than adding a second. `question_index` is NOT NULL on this table and
-- is stable within an assignment, so it is the key an upsert can rely on.
create unique index if not exists assignment_question_attempts_question_uniq
  on public.assignment_question_attempts (submission_id, question_index);

-- Reading "this student's current go" and "this class's progress" are the two
-- hot paths of the new model.
create index if not exists assignment_submissions_student_status_idx
  on public.assignment_submissions (assignment_id, student_id, status)
  where deleted_at is null;
