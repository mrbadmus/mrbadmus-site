-- Rollback for supabase/baselines/20261013_prod_lesson_mark_kind_FOR_MIDE.sql. Mide only.
-- Removes lesson-marking cost rows (they would violate the narrower CHECK), then restores it.
delete from public.ai_usage_events where kind = 'lesson_mark';
alter table public.ai_usage_events drop constraint ai_usage_events_kind_check;
alter table public.ai_usage_events add constraint ai_usage_events_kind_check check (kind = any (array[
  'tutor_turn','ai_mark','explain','flashcard_extract','flashcard_answer_check']::text[]));
