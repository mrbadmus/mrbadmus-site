-- Saved work, follow-up (16 Oct 2026). ADDITIVE ONLY. TEST first; production
-- at merge time only (CLAUDE.md, "When a migration may touch PRODUCTION").
--
--   child_answers.self_ticks   the lines / marking points a child ticked
--                              THEMSELVES on a self-marked answer ("I had
--                              this", a written rung's criteria), 1-based,
--                              on that answer's own ledger row.
--
-- Mide's brief: "every answer the child gave … right/wrong and marks, where
-- they got to" — a child who ticked 5 of 5 lines on one device saw 0 of 5 on
-- another, because the ticks were never sent anywhere.
--
-- Why a column of its own and not points_hit / a row of its own: a self-tick
-- is NOT a mark. points_hit is the marker's credit and feeds nothing a parent
-- totals only by luck; a separate row would be counted by every per-row
-- tally (answered, unmarked, untimed). Nothing that totals the ledger for a
-- parent selects this column, so it cannot move a parent's numbers.
--
-- The backend probes the column before reading or writing it: a backend
-- deployed ahead of this file records and restores everything else as before.
--
-- Rollback: alter table public.child_answers drop column if exists self_ticks;

alter table public.child_answers add column if not exists self_ticks smallint[];
alter table public.child_answers drop constraint if exists child_answers_self_ticks_range;
alter table public.child_answers add constraint child_answers_self_ticks_range
  check (self_ticks is null or (cardinality(self_ticks) <= 20 and 1 <= all(self_ticks) and 20 >= all(self_ticks)));
comment on column public.child_answers.self_ticks is
  'The child''s OWN ticks on a self-marked answer, 1-based. Never a mark: no parent total reads it.';
