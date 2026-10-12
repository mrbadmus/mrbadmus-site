-- B2C parent truth, round 2 (13 Oct 2026). ADDITIVE ONLY. For TEST, where
-- child_answers and child_tutor_questions already exist (20261011124719 and
-- 20261011131302). Production does NOT run this file: it gets both tables in
-- their final shape, these columns included, from
-- supabase/baselines/20261013_prod_parent_truth_bundle.sql.
--
--   child_answers.mark_level         a level-marked written answer's level, 0-3
--   child_answers.mark_next_step     one line on what lifts it to the next level
--   child_tutor_questions.reply      the tutor's reply, as the pupil's page showed it
--   child_tutor_questions.replied_at when it came
--   child_answers_lesson_ai_marks_idx  the per-child daily lesson-marking cap now
--                                    counts these ledger rows, not ai_usage_events
--
-- Nothing here touches a school pupil's data or any existing row: four
-- nullable columns, two CHECKs that every existing row already satisfies
-- (the columns are NULL), and one partial index. The backend probes each
-- column pair before writing it, so a backend deployed ahead of this file
-- records everything else exactly as before.
--
-- Mide's brief (13 Oct 2026): "Store each child question and tutor reply
-- (text, lesson, time) in a proper table" — this is the reply half of it.
--
-- Apply AFTER 20261011170510.
-- Rollback: supabase/rollbacks/20261013003836_b2c_parent_truth_r2_rollback.sql

alter table public.child_answers add column mark_level smallint;
alter table public.child_answers add column mark_next_step text;
alter table public.child_answers add constraint child_answers_mark_level_range
  check (mark_level is null or mark_level between 0 and 3);
alter table public.child_answers add constraint child_answers_mark_next_step_len
  check (mark_next_step is null or char_length(mark_next_step) between 1 and 1000);

alter table public.child_tutor_questions add column reply text;
alter table public.child_tutor_questions add column replied_at timestamptz;
-- A refused or failed exchange stores no reply.
alter table public.child_tutor_questions add constraint child_tutor_questions_reply_only_when_answered
  check (reply is null or answered is true);
alter table public.child_tutor_questions add constraint child_tutor_questions_reply_len
  check (reply is null or char_length(reply) between 1 and 20000);

create index child_answers_lesson_ai_marks_idx on public.child_answers (child_id, created_at)
  where surface = 'lesson' and marked_by = 'ai';

comment on column public.child_answers.mark_level is 'Level (0-3) a level-marked written answer reached, as the AI marker returned it. NULL when not level-marked.';
comment on column public.child_answers.mark_next_step is 'One line from the marker on what would lift the answer to the next level. NULL when not given.';
comment on column public.child_tutor_questions.reply is 'The tutor''s reply text exactly as the pupil''s page showed it (the response''s text parts joined). NULL when the tutor did not answer.';
comment on column public.child_tutor_questions.replied_at is 'When the reply was stored. NULL when there is no reply.';
