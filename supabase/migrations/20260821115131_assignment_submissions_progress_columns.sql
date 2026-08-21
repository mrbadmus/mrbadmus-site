-- A submission stops being a single moment and becomes a week of work.
--
-- Ruled 22 Aug 2026: every answer saves the moment it is given; progress is
-- visible all week; "Complete" marks the work finished rather than transferring
-- it; nothing is locked by the clock; late is a fact recorded at completion.
--
-- `submitted_at` is kept and kept in sync — it is the legacy completion stamp
-- and other readers still use it. `completed_at` is the one this model writes.
alter table public.assignment_submissions
  add column if not exists attempt_no   smallint,
  add column if not exists status       text,
  add column if not exists started_at   timestamptz,
  add column if not exists completed_at timestamptz,
  add column if not exists is_late      boolean;

comment on column public.assignment_submissions.attempt_no is
  'Which go this is at (assignment, student). Both attempts are kept; the best counts.';
comment on column public.assignment_submissions.status is
  'in_progress | complete. A row exists from the FIRST answer, not from completion.';
comment on column public.assignment_submissions.is_late is
  'Stamped at completion against the server clock. NULL while in progress — a student who has not finished is unfinished, not late.';
