alter table public.assignment_submissions
  alter column attempt_no set default 1,
  alter column attempt_no set not null,
  alter column status     set default 'in_progress',
  alter column status     set not null,
  alter column started_at set default now(),
  alter column started_at set not null;

alter table public.assignment_submissions
  drop constraint if exists assignment_submissions_status_chk;
alter table public.assignment_submissions
  add constraint assignment_submissions_status_chk
  check (status in ('in_progress', 'complete'));

-- A completed submission must carry its completion stamp and its lateness; an
-- in-progress one must carry neither. This is what stops a hardcoded '17 SEP,
-- 20:41' ever reaching the table: there is exactly one writer of completed_at
-- and it is the server clock.
alter table public.assignment_submissions
  drop constraint if exists assignment_submissions_complete_chk;
alter table public.assignment_submissions
  add constraint assignment_submissions_complete_chk
  check (
    (status = 'complete'    and completed_at is not null and is_late is not null)
 or (status = 'in_progress' and completed_at is null     and is_late is null)
  );
