-- PRODUCTION bundle — B2C parent truth (13 Oct 2026). Apply MANUALLY, once.
--
-- ⚠️ This is the WHOLE of what production needs for the parent-truth ledger,
-- in its final shape. It is NOT the TEST migration chain replayed:
--
--   * child_answers           — the answer ledger, final shape: everything
--                                20261011124719 created, plus client_event_id
--                                (20261011131302) and mark_level /
--                                mark_next_step (20261013003836).
--   * child_tutor_questions   — what a consumer child asked the tutor, final
--                                shape: plus reply / replied_at (20261013003836).
--   * their indexes, and RLS ENABLED WITH NO POLICIES (service role only:
--     parents read through GET /api/consumer/children/:id/activity, which
--     checks guardianship itself).
--
-- And, ON PURPOSE, NOT:
--   * knowledge_points / question_knowledge_points — the backend reads the
--     tags from its bundled knowledge-points.json; 42k rows are not loaded
--     into production.
--   * any change to ai_usage_events — its kind CHECK stays as it is, without
--     'lesson_mark'. The backend's lesson-marking cap counts child_answers
--     rows, and its 'lesson_mark' usage row is best effort (refused by the
--     CHECK here, logged once an hour, marking unaffected).
--
-- Additive only: two new tables nothing else reads, written only by the
-- backend's service role and only for family / organisation children. No
-- existing table, row or policy is altered. School pupils (Rainford) are
-- untouched: the backend never writes either table for them.
--
-- Depends on public.schools, public.profiles and public.work_items (all on
-- production since the B2C launch). Runs in one transaction; a re-run fails
-- on "relation already exists" rather than doing anything twice.
--
-- It does not write supabase_migrations.schema_migrations: it is a baseline,
-- not a CLI migration. If it is applied through a tool that records a version
-- (MCP apply_migration does), note the version it recorded.
--
-- Rollback: supabase/rollbacks/20261013_prod_parent_truth_bundle_rollback.sql

begin;

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
  knowledge_point_id  text,                            -- from knowledge-points.json at write time (no FK: no table)
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
  client_event_id     uuid,                            -- the page's id for this answer: a re-send is idempotent
  mark_level          smallint,                        -- level-marked written answer: 0-3
  mark_next_step      text,                            -- one line on what lifts it to the next level
  -- An answer nobody marked is never right, never wrong and never scores.
  constraint child_answers_unmarked_scores_nothing check (
    marked_by <> 'unmarked' or (is_correct is null and marks_scored is null and points_hit is null)),
  constraint child_answers_marked_has_marks check (
    marked_by = 'unmarked' or (marks_scored is not null and marks_scored between 0 and marks_available)),
  constraint child_answers_mark_level_range check (mark_level is null or mark_level between 0 and 3),
  constraint child_answers_mark_next_step_len check (
    mark_next_step is null or char_length(mark_next_step) between 1 and 1000)
);
create index child_answers_child_time_idx on public.child_answers (child_id, answered_at desc);
create index child_answers_child_question_idx on public.child_answers (child_id, question_id);
create index child_answers_work_item_idx on public.child_answers (work_item_id) where work_item_id is not null;
create index child_answers_visit_idx on public.child_answers (visit_id) where visit_id is not null;
create index child_answers_source_idx on public.child_answers (source_id) where source_id is not null;
create unique index child_answers_client_event_uidx on public.child_answers (child_id, client_event_id)
  where client_event_id is not null;
create index child_answers_lesson_ai_marks_idx on public.child_answers (child_id, created_at)
  where surface = 'lesson' and marked_by = 'ai';
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
  asked_at     timestamptz not null default now(),
  reply        text,                                   -- the reply as the pupil's page showed it
  replied_at   timestamptz,
  -- A refused or failed exchange stores no reply.
  constraint child_tutor_questions_reply_only_when_answered check (reply is null or answered is true),
  constraint child_tutor_questions_reply_len check (reply is null or char_length(reply) between 1 and 20000)
);
create index child_tutor_questions_child_idx on public.child_tutor_questions (child_id, asked_at desc);
alter table public.child_tutor_questions enable row level security;

comment on table public.child_answers is 'Parent truth: append-only ledger of every answer a consumer (family/organisation) child gives, with the marking actually done. Service role only; parents read via GET /api/consumer/children/:id/activity.';
comment on table public.child_tutor_questions is 'Parent truth: each question a consumer child put to the tutor, where, and the reply. Service role only.';

commit;
