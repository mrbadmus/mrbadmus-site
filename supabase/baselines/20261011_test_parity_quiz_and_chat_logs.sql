-- TEST ONLY (qeppkiswvclkkwbxmlok). Never apply to production — production
-- already has all three tables, and this file is a copy of them.
--
-- TEST never had quiz_scores, quiz_question_attempts or chat_logs, so on TEST
-- every KS3 lesson score and every tutor token log failed silently (the
-- backend logs and moves on). The parent-truth proof (11 Oct 2026) has to
-- drive those paths, so TEST gets production's definitions, read from
-- production's catalogue on 11 Oct 2026: columns, defaults, keys, indexes,
-- RLS and policies, byte for byte.

create table if not exists public.quiz_scores (
  id uuid primary key default gen_random_uuid(),
  created_at timestamptz default now(),
  user_id uuid not null references public.profiles(id) on delete cascade,
  subject text not null,
  topic text not null,
  subtopic text not null,
  pathway text,
  tier text,
  score smallint not null,
  max_score smallint not null,
  percentage smallint not null
);
alter table public.quiz_scores enable row level security;
create policy "Users can insert own scores" on public.quiz_scores for insert
  with check ((select auth.uid() as uid) = user_id);
create policy quiz_scores_select_merged on public.quiz_scores for select
  using (((select auth.uid() as uid) = user_id) or (exists (select 1 from public.class_members cm
    where cm.student_id = quiz_scores.user_id and cm.left_at is null and cm.deleted_at is null
      and public.auth_user_teaches_class(cm.class_id))));

create table if not exists public.quiz_question_attempts (
  id uuid primary key default gen_random_uuid(),
  quiz_score_id uuid not null references public.quiz_scores(id) on delete cascade,
  question_index smallint not null,
  question_text text,
  selected_answer text,
  correct_answer text,
  is_correct boolean,
  time_spent_seconds integer,
  attempt_number smallint default 1,
  created_at timestamptz default now(),
  rung text,
  criteria_met smallint[],
  criteria_total smallint,
  selected_option_letter text,
  correct_option_letter text,
  question_ref text
);
create index if not exists quiz_question_attempts_quiz_score_id_idx on public.quiz_question_attempts (quiz_score_id);
alter table public.quiz_question_attempts enable row level security;
create policy quiz_question_attempts_delete_merged on public.quiz_question_attempts for delete
  using (exists (select 1 from public.quiz_scores qs where qs.id = quiz_question_attempts.quiz_score_id
    and qs.user_id = (select public.auth_user_id() as auth_user_id)));
create policy quiz_question_attempts_insert_merged on public.quiz_question_attempts for insert
  with check (exists (select 1 from public.quiz_scores qs where qs.id = quiz_question_attempts.quiz_score_id
    and qs.user_id = (select public.auth_user_id() as auth_user_id)));
create policy quiz_question_attempts_select_merged on public.quiz_question_attempts for select
  using ((exists (select 1 from public.quiz_scores qs where qs.id = quiz_question_attempts.quiz_score_id
      and qs.user_id = (select public.auth_user_id() as auth_user_id)))
    or (exists (select 1 from public.quiz_scores qs
      join public.class_members cm on cm.student_id = qs.user_id and cm.left_at is null and cm.deleted_at is null
      where qs.id = quiz_question_attempts.quiz_score_id and public.auth_user_teaches_class(cm.class_id))));
create policy quiz_question_attempts_update_merged on public.quiz_question_attempts for update
  using (exists (select 1 from public.quiz_scores qs where qs.id = quiz_question_attempts.quiz_score_id
    and qs.user_id = (select public.auth_user_id() as auth_user_id)))
  with check (exists (select 1 from public.quiz_scores qs where qs.id = quiz_question_attempts.quiz_score_id
    and qs.user_id = (select public.auth_user_id() as auth_user_id)));

create table if not exists public.chat_logs (
  id uuid primary key default gen_random_uuid(),
  created_at timestamptz default now(),
  user_id uuid references public.profiles(id) on delete set null,
  input_tokens integer,
  output_tokens integer
);
alter table public.chat_logs enable row level security;
create policy "Service role only for chat_logs" on public.chat_logs using (false);
