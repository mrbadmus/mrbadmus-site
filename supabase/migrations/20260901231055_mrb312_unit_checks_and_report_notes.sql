-- MRB-312 Night 2, migration 5 of 9: unit checks, the termly report's note,
-- and the flashcard queue a wrong answer feeds.
--
-- unit_check_attempts — one row per sitting. Design's ruling: the FIRST
--   completed attempt is the record (is_record = true); later attempts are
--   practice. Timed, scored, with a per-lesson breakdown and a weakest area.
-- report_notes — the teacher's note on a child's termly report, written by
--   Mide from Admin. One per (child, term).
-- child_flashcard_queue — lessons whose cards the child should see next,
--   seeded from wrong answers (unit checks tonight; practice later). The
--   student page's deck reads ks3_cards by lesson slug, so a queue of slugs
--   is exactly what the existing flow consumes.

create table if not exists public.unit_check_attempts (
  id             uuid primary key default gen_random_uuid(),
  org_id         uuid not null references public.schools(id),
  child_id       uuid not null references public.profiles(id),
  unit_code      text not null,
  key_stage      text not null,
  subject        text,
  unit_name      text,
  question_ids   text[] not null,
  count          smallint not null,
  time_limit_s   integer not null,
  started_at     timestamptz not null default now(),
  completed_at   timestamptz,
  elapsed_s      integer,
  answers        jsonb,                 -- [{"id": ..., "chosen": 2, "correct": true}]
  score          smallint,
  max_score      smallint,
  breakdown      jsonb,                 -- [{"topic": "...", "lesson_slug": "...", "got": 3, "of": 4}]
  weakest        text,
  is_record      boolean not null default false,
  work_item_id   uuid references public.work_items(id),
  created_at     timestamptz not null default now(),
  constraint unit_check_attempts_key_stage_check check (key_stage in ('KS3', 'KS4')),
  constraint unit_check_attempts_count_check check (count between 5 and 30)
);

create index if not exists idx_unit_check_attempts_child on public.unit_check_attempts (child_id, unit_code, started_at desc);
create index if not exists idx_unit_check_attempts_org on public.unit_check_attempts (org_id, completed_at desc);
-- Exactly one record per (child, unit).
create unique index if not exists uq_unit_check_record on public.unit_check_attempts (child_id, unit_code) where is_record;

create table if not exists public.report_notes (
  child_id     uuid not null references public.profiles(id),
  term         text not null,             -- e.g. 'autumn-2026'
  note         text not null,
  written_by   uuid references public.profiles(id),
  updated_at   timestamptz not null default now(),
  primary key (child_id, term),
  constraint report_notes_len check (char_length(note) between 1 and 2000)
);

create table if not exists public.child_flashcard_queue (
  id           uuid primary key default gen_random_uuid(),
  org_id       uuid not null references public.schools(id),
  child_id     uuid not null references public.profiles(id),
  lesson_slug  text not null,
  source       text not null,             -- 'unit_check' | 'practice'
  source_id    uuid,
  created_at   timestamptz not null default now(),
  cleared_at   timestamptz
);

create index if not exists idx_child_flashcard_queue_child on public.child_flashcard_queue (child_id) where cleared_at is null;

alter table public.unit_check_attempts   enable row level security;
alter table public.report_notes          enable row level security;
alter table public.child_flashcard_queue enable row level security;

drop policy if exists unit_check_attempts_read on public.unit_check_attempts;
create policy unit_check_attempts_read on public.unit_check_attempts
  for select using (
    child_id = auth.uid()
    or public.guardian_of_child(auth.uid(), child_id)
    or public.auth_user_operator_active()
  );

drop policy if exists report_notes_read on public.report_notes;
create policy report_notes_read on public.report_notes
  for select using (
    public.guardian_of_child(auth.uid(), child_id)
    or public.auth_user_operator_active()
  );

drop policy if exists child_flashcard_queue_read on public.child_flashcard_queue;
create policy child_flashcard_queue_read on public.child_flashcard_queue
  for select using (
    child_id = auth.uid()
    or public.guardian_of_child(auth.uid(), child_id)
    or public.auth_user_operator_active()
  );

revoke insert, update, delete on public.unit_check_attempts   from anon, authenticated;
revoke insert, update, delete on public.report_notes          from anon, authenticated;
revoke insert, update, delete on public.child_flashcard_queue from anon, authenticated;

comment on table public.unit_check_attempts is
  'MRB-312. One row per unit-check sitting. First completed attempt per (child, unit) is the record; later ones are practice.';
comment on table public.report_notes is
  'MRB-312. The teacher''s note on a termly report, written from Admin.';
comment on table public.child_flashcard_queue is
  'MRB-312. Lesson slugs whose flashcards a child should see next, seeded from wrong answers.';