-- Undoes 20261109060000_child_answers_self_level.sql. Apply manually only.
alter table public.child_answers drop column if exists self_level;
