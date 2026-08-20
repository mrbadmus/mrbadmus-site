-- One assignment per class per teaching week.
-- The on-demand producer composes a week's assignment the first time anybody
-- asks for it. Two simultaneous first-openers would otherwise each write one.
-- Composition is deterministic, so the loser of the race can simply re-read.
-- Partial: only auto-produced rows carry an academic_week, and a soft-deleted
-- row must not block a fresh one.
create unique index if not exists assignments_class_week_uniq
  on public.assignments (class_id, academic_week)
  where deleted_at is null and academic_week is not null;
