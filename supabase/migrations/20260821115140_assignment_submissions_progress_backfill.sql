-- Every row that exists today was written by the old one-shot route, so every
-- one of them is complete. `attempt_no` is assigned in creation order, which is
-- how the two rows against 72a5b315 become attempt 1 and attempt 2 rather than
-- a constraint violation.
with ranked as (
  select id,
         row_number() over (partition by assignment_id, student_id order by created_at, id) as rn
  from public.assignment_submissions
)
update public.assignment_submissions s
set attempt_no   = r.rn,
    status       = 'complete',
    started_at   = coalesce(s.created_at, s.submitted_at, now()),
    completed_at = coalesce(s.submitted_at, s.created_at, now()),
    is_late      = coalesce(
      (select coalesce(s.submitted_at, s.created_at) > a.due_at
         from public.assignments a where a.id = s.assignment_id and a.due_at is not null),
      false)
from ranked r
where r.id = s.id;
