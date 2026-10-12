-- Rollback for migrations/20261012234246_b2c_parent_truth_r2.sql (TEST).
-- Drops the four r2 columns — and so every stored tutor reply and every
-- stored level / next step — plus their CHECKs and the cap's index. The rest
-- of both tables, and every other row, is untouched. The backend probes the
-- columns, so it carries on recording everything else.

drop index if exists public.child_answers_lesson_ai_marks_idx;

alter table public.child_tutor_questions drop constraint if exists child_tutor_questions_reply_len;
alter table public.child_tutor_questions drop constraint if exists child_tutor_questions_reply_only_when_answered;
alter table public.child_tutor_questions drop column if exists replied_at;
alter table public.child_tutor_questions drop column if exists reply;

alter table public.child_answers drop constraint if exists child_answers_mark_next_step_len;
alter table public.child_answers drop constraint if exists child_answers_mark_level_range;
alter table public.child_answers drop column if exists mark_next_step;
alter table public.child_answers drop column if exists mark_level;

delete from supabase_migrations.schema_migrations where version = '20261012234246';
