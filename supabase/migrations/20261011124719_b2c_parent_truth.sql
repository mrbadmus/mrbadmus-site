-- B2C "parents see exactly what their child does" (Mide, 11 Oct 2026).
--
-- ADDITIVE ONLY. Four new tables and one widened CHECK. Nothing here alters,
-- rewrites or reads an existing row: quiz_scores, quiz_question_attempts,
-- assignment_question_attempts, unit_check_attempts, exam_answers and
-- chat_logs keep their columns, their rows and their meaning for every
-- school pupil. The backend probes for child_answers before writing to any of
-- these, so a backend deployed ahead of this migration records nothing new
-- and changes nothing.
--
--   knowledge_points            one row per knowledge point (what a question tests)
--   question_knowledge_points   question id -> knowledge point, for every question
--                               source (both banks, the KS3 ladder, exam_questions,
--                               KS4 lesson items). Keyed by the question's stable id,
--                               so the banks themselves are not touched.
--   child_answers               append-only ledger: one row per answer a consumer
--                               child gives, anywhere, with the marking that was
--                               actually done. Written only by the backend
--                               (service role), only for family/organisation children.
--   child_tutor_questions       what a consumer child asked the tutor, and where.
--
-- All four are service-role only (RLS on, no policies): parents read through
-- GET /api/consumer/children/:id/activity, which checks guardianship itself.
--
-- Rollback: supabase/rollbacks/20261011124719_b2c_parent_truth_rollback.sql

create table public.knowledge_points (
  id          text primary key,                       -- 'ks3.<lesson-slug>.<n>' / 'ks4.<subtopic>.<n>'
  key_stage   text not null check (key_stage in ('KS3','KS4')),
  subject     text,
  scope_kind  text not null check (scope_kind in ('lesson','subtopic')),
  scope_ref   text not null,                          -- KS3 lesson slug / KS4 subtopic slug
  position    smallint not null,
  label       text not null check (char_length(label) between 3 and 200),
  created_at  timestamptz not null default now(),
  updated_at  timestamptz not null default now(),
  unique (key_stage, scope_ref, position)
);
alter table public.knowledge_points enable row level security;

create table public.question_knowledge_points (
  question_id         text primary key,
  source              text not null check (source in
                        ('ks3_bank','ks4_bank','ks3_ladder','exam','ks4_lesson')),
  knowledge_point_id  text not null references public.knowledge_points(id) on delete cascade,
  updated_at          timestamptz not null default now()
);
create index question_knowledge_points_kp_idx on public.question_knowledge_points (knowledge_point_id);
alter table public.question_knowledge_points enable row level security;

create table public.child_answers (
  id                  uuid primary key default gen_random_uuid(),
  org_id              uuid not null references public.schools(id) on delete cascade,
  child_id            uuid not null references public.profiles(id) on delete cascade,
  work_item_id        uuid references public.work_items(id) on delete set null,
  surface             text not null check (surface in ('lesson','practice','unit_check','exam')),
  source_kind         text check (source_kind in
                        ('quiz_score','assignment_submission','unit_check_attempt','exam_answer')),
  source_id           uuid,
  visit_id            uuid,                            -- one page load of a lesson
  question_id         text not null,
  knowledge_point_id  text,                            -- copied from question_knowledge_points at write time
  key_stage           text check (key_stage in ('KS3','KS4')),
  subject             text,
  unit_code           text,
  lesson_slug         text,
  rung                text,
  answer_kind         text not null check (answer_kind in ('choice','written','numeric','order')),
  question_text       text,
  answer              text,
  correct_answer      text,
  is_correct          boolean,                         -- right/wrong for a choice/numeric/order answer
  marks_scored        smallint,
  marks_available     smallint not null check (marks_available >= 0),
  points_hit          smallint[],                      -- 1-based mark-scheme points credited
  points_total        smallint,
  marked_by           text not null check (marked_by in ('key','ai','stub','unmarked')),
  unmarked_reason     text,
  feedback            text,
  ai_model            text,
  attempt_no          smallint not null default 1 check (attempt_no >= 1),
  time_spent_seconds  integer check (time_spent_seconds is null or time_spent_seconds >= 0),
  answered_at         timestamptz not null default now(),
  created_at          timestamptz not null default now(),
  -- An answer nobody marked is never right, never wrong and never scores.
  constraint child_answers_unmarked_scores_nothing check (
    marked_by <> 'unmarked' or (is_correct is null and marks_scored is null and points_hit is null)),
  constraint child_answers_marked_has_marks check (
    marked_by = 'unmarked' or (marks_scored is not null and marks_scored between 0 and marks_available))
);
create index child_answers_child_time_idx on public.child_answers (child_id, answered_at desc);
create index child_answers_child_question_idx on public.child_answers (child_id, question_id);
create index child_answers_work_item_idx on public.child_answers (work_item_id) where work_item_id is not null;
create index child_answers_visit_idx on public.child_answers (visit_id) where visit_id is not null;
create index child_answers_source_idx on public.child_answers (source_id) where source_id is not null;
alter table public.child_answers enable row level security;

create table public.child_tutor_questions (
  id           uuid primary key default gen_random_uuid(),
  org_id       uuid not null references public.schools(id) on delete cascade,
  child_id     uuid not null references public.profiles(id) on delete cascade,
  question     text not null,
  has_image    boolean not null default false,
  page_path    text,
  page_title   text,
  key_stage    text check (key_stage in ('KS3','KS4')),
  lesson_slug  text,
  answered     boolean,                                -- did the tutor reply (false = refused/failed)
  asked_at     timestamptz not null default now()
);
create index child_tutor_questions_child_idx on public.child_tutor_questions (child_id, asked_at desc);
alter table public.child_tutor_questions enable row level security;

-- Lesson-rung marking is part of a lesson, not the family's exam-marking
-- allowance, so it gets its own kind: it is costed in the same ledger Admin
-- bills from, and ai_usage_counts (which counts only the capped kinds) does
-- not count it against ai_marks_per_month. Same five kinds on TEST and
-- production as of 11 Oct 2026, plus the new one.
alter table public.ai_usage_events drop constraint ai_usage_events_kind_check;
alter table public.ai_usage_events add constraint ai_usage_events_kind_check check (kind = any (array[
  'tutor_turn','ai_mark','explain','flashcard_extract','flashcard_answer_check','lesson_mark']::text[]));
