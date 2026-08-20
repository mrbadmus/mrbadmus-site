-- MRB-269's final ruling (Mide, 20 Aug 2026): difficulty is a property of the
-- QUESTION — its band — and that supersedes MRB-239's rung-based difficulty
-- model. A bank question has a band and no rung; a ladder question has a rung
-- and no band. The column was NOT NULL, so a bank question could not be stored
-- at all.
alter table public.assignment_questions
  add column if not exists band text;

alter table public.assignment_questions
  drop constraint if exists assignment_questions_band_check;
alter table public.assignment_questions
  add constraint assignment_questions_band_check
  check (band is null or band in ('easier', 'standard', 'harder'));

alter table public.assignment_questions
  alter column rung drop not null;

-- A row must say which pool it came from. Exactly one of the two.
alter table public.assignment_questions
  drop constraint if exists assignment_questions_rung_xor_band;
alter table public.assignment_questions
  add constraint assignment_questions_rung_xor_band
  check ((rung is not null) <> (band is not null));
