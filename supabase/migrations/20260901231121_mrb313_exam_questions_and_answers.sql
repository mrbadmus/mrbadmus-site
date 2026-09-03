-- MRB-313 Night 2, migration 6 of 9: exam questions with mark schemes, and
-- the answers a child writes against them.
--
-- exam_questions — extended-response items (2–6 marks) with a STRUCTURED
--   scheme: marking points, and for 6-markers a set of level descriptors and
--   indicative content. `source` says where each came from, because recon
--   found only one pool in the estate that carries a real mark scheme (the
--   Bonding v2 WriteThenMark items, KS4 chemistry). Everything else tonight is
--   seeded by Code and marked 'code_seed' so Mide can review and replace.
--   Readable by any signed-in user, like the assignment bank. Service role
--   writes.
-- exam_answers — one row per attempt. AI-marked first (status ai_marked);
--   the child may send it to Mr Badmus (sent_to_mb), who marks from Admin
--   (mb_marked). The monthly quota counts sent_to_mb_at in the London month.

create table if not exists public.exam_questions (
  id           text primary key,
  key_stage    text not null,
  subject      text not null,
  topic        text not null,
  unit_code    text,
  marks        smallint not null,
  command      text,
  text         text not null,
  stem         text,
  scheme       jsonb not null,         -- [{"text": "...", "essential": false}]
  levels       jsonb,                  -- [{"level": 3, "marks": "5-6", "descriptor": "..."}]
  indicative   jsonb,                  -- ["...", "..."]
  source       text not null,
  tier         text,
  pathway      text,
  active       boolean not null default true,
  created_at   timestamptz not null default now(),
  updated_at   timestamptz not null default now(),
  constraint exam_questions_key_stage_check check (key_stage in ('KS3', 'KS4')),
  constraint exam_questions_marks_check check (marks between 2 and 6),
  constraint exam_questions_subject_check check (subject in ('Biology', 'Chemistry', 'Physics')),
  constraint exam_questions_scheme_is_array check (jsonb_typeof(scheme) = 'array' and jsonb_array_length(scheme) >= 1)
);

create index if not exists idx_exam_questions_pick on public.exam_questions (key_stage, subject, marks) where active;

create table if not exists public.exam_answers (
  id             uuid primary key default gen_random_uuid(),
  org_id         uuid not null references public.schools(id),
  child_id       uuid not null references public.profiles(id),
  question_id    text not null references public.exam_questions(id),
  answer         text not null,
  ai_score       smallint,
  ai_max         smallint,
  ai_hits        smallint[],
  ai_feedback    text,
  ai_model       text,
  ai_marked_at   timestamptz,
  status         text not null default 'ai_marked',
  sent_to_mb_at  timestamptz,
  mb_score       smallint,
  mb_feedback    text,
  mb_marked_at   timestamptz,
  mb_marked_by   uuid references public.profiles(id),
  work_item_id   uuid references public.work_items(id),
  created_at     timestamptz not null default now(),
  updated_at     timestamptz not null default now(),
  constraint exam_answers_len check (char_length(answer) between 1 and 4000),
  constraint exam_answers_status_check check (status in ('ai_marked', 'sent_to_mb', 'mb_marked')),
  constraint exam_answers_sent_has_time check (status = 'ai_marked' or sent_to_mb_at is not null),
  constraint exam_answers_mb_marked_complete check (status <> 'mb_marked' or (mb_score is not null and mb_marked_at is not null))
);

create index if not exists idx_exam_answers_child on public.exam_answers (child_id, created_at desc);
create index if not exists idx_exam_answers_queue on public.exam_answers (sent_to_mb_at) where status = 'sent_to_mb';
create index if not exists idx_exam_answers_org on public.exam_answers (org_id, created_at desc);

-- How many of this child's answers went to Mr Badmus this calendar month
-- (London). The cap itself lives in platform_settings / org_limits.
create or replace function public.mb_quota_used(p_child uuid)
returns integer
language sql
stable
security definer
set search_path to 'public'
as $fn$
  select count(*)::int
    from public.exam_answers a
   where a.child_id = p_child
     and a.sent_to_mb_at is not null
     and (a.sent_to_mb_at at time zone 'Europe/London') >= date_trunc('month', now() at time zone 'Europe/London');
$fn$;

alter table public.exam_questions enable row level security;
alter table public.exam_answers   enable row level security;

drop policy if exists exam_questions_read on public.exam_questions;
create policy exam_questions_read on public.exam_questions
  for select using (auth.uid() is not null and active);

drop policy if exists exam_answers_read on public.exam_answers;
create policy exam_answers_read on public.exam_answers
  for select using (
    child_id = auth.uid()
    or public.guardian_of_child(auth.uid(), child_id)
    or public.auth_user_operator_active()
  );

revoke insert, update, delete on public.exam_questions from anon, authenticated;
revoke insert, update, delete on public.exam_answers   from anon, authenticated;

drop trigger if exists trg_exam_answers_touch on public.exam_answers;
create trigger trg_exam_answers_touch before update on public.exam_answers
  for each row execute function public.consumer_touch_updated_at();

comment on table public.exam_questions is
  'MRB-313. Extended-response items with structured mark schemes. source = code_seed | bonding_v2 | ks3_ladder. Service role writes.';
comment on table public.exam_answers is
  'MRB-313. A child''s written answer: AI mark first, optionally sent to Mr Badmus, marked from Admin.';