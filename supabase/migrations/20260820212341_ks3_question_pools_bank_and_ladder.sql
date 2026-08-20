-- The two KS3 question pools, mirrored out of the Python source of truth.
--
-- WHY THESE ARE TABLES. `compose_assignment()` and the bank are Python, in the
-- site repo; the producer that has to call them lives in the Node backend, in
-- a different repo. Vendoring a JSON copy of 70 question modules into the
-- backend would be a second copy of the content that drifts. These tables are
-- a BUILD ARTEFACT: `export_ks3_questions.py` refreshes them from Python, a
-- gate asserts they match, and Python stays the only place a question is
-- written. It also lets the assignment page read question text, options and
-- per-distractor feedback directly, instead of fetching a lesson page and
-- scraping its DOM the way student/assignment.html has had to.

create table if not exists public.ks3_bank_questions (
  id            text primary key,             -- 'c1-04-h02', permanent, never reused
  unit_code     text        not null,         -- 'C1'
  lesson_slug   text        not null,         -- 'gas-pressure'
  band          text        not null check (band in ('easier', 'standard', 'harder')),
  bank_position smallint    not null,         -- order within the lesson's module
  text          text        not null,
  figure        text,                         -- id of a figure already in the lesson
  options       jsonb       not null,         -- [{text, correct, why}] — exactly four
  created_at    timestamptz default now(),
  updated_at    timestamptz default now()
);

create index if not exists ks3_bank_questions_lesson_band_idx
  on public.ks3_bank_questions (unit_code, lesson_slug, band, bank_position);

-- The lesson ladder's two MARKED rungs. `explain` and `produce` are marked by
-- the student against success criteria and are not exported here — nothing can
-- score them, and a recall round needs a right answer.
create table if not exists public.ks3_ladder_questions (
  question_ref  text primary key,             -- '<lesson_slug>#<rung>' — the only
                                              -- stable identifier a rung has
  unit_code     text        not null,
  lesson_slug   text        not null,
  rung          text        not null check (rung in ('recall', 'apply')),
  text          text        not null,
  answer_letter text        not null check (answer_letter in ('A', 'B', 'C', 'D')),
  -- [{letter, text, correct, why}]. `why` is the feedback authored against that
  -- distractor. WARNING: the CORRECT option's `why` is null — the right-answer slot is
  -- CLOSED, not filled with a generic line. A ladder authors three feedback
  -- strings, one per wrong option, and inventing a fourth is exactly what the
  -- parity gate's layer H forbids.
  options       jsonb       not null,
  created_at    timestamptz default now(),
  updated_at    timestamptz default now()
);

create index if not exists ks3_ladder_questions_lesson_idx
  on public.ks3_ladder_questions (lesson_slug, rung);

alter table public.ks3_bank_questions   enable row level security;
alter table public.ks3_ladder_questions enable row level security;

-- Reference content, the same for every student. Readable by anyone signed in;
-- only the service role (the exporter and the producer) writes.
drop policy if exists ks3_bank_questions_read on public.ks3_bank_questions;
create policy ks3_bank_questions_read on public.ks3_bank_questions
  for select to authenticated using (true);

drop policy if exists ks3_ladder_questions_read on public.ks3_ladder_questions;
create policy ks3_ladder_questions_read on public.ks3_ladder_questions
  for select to authenticated using (true);
