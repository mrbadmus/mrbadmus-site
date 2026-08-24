-- Manual rollback for 20260824214711_mrb288_one_pool_per_assignment.
-- Apply by hand only. Removes the one-pool guard on composed assignment
-- questions; the rung/band XOR constraint (20260820212322) remains.
alter table public.assignment_questions
  drop constraint if exists one_pool_per_assignment;
