-- ⚠️ FOR MIDE — NOT APPLIED. NOT ADDITIVE (drops and re-adds a CHECK on an existing table).
--
-- Production (urklkrwevjtlfbwnipjn) ai_usage_events_kind_check, read 14 Oct 2026:
--   CHECK (kind = ANY (ARRAY['tutor_turn','ai_mark','explain','flashcard_extract','flashcard_answer_check']))
-- The backend now AI-marks a family child's written lesson rungs and records that
-- cost as kind 'lesson_mark'. Until this runs, production refuses that row; the
-- backend logs one line an hour and carries on (marking is never affected), and
-- the per-child daily cap counts child_answers (marked_by='ai') instead, so the
-- cap holds either way. What is lost until then: lesson-marking cost rows in the
-- ledger Admin bills from.
--
-- TEST (qeppkiswvclkkwbxmlok) has had this since 11 Oct (migration 20261011124719).
-- Rollback: supabase/rollbacks/20261013_prod_lesson_mark_kind_FOR_MIDE_rollback.sql
-- (deletes any 'lesson_mark' rows first, then restores the five-kind CHECK).

alter table public.ai_usage_events drop constraint ai_usage_events_kind_check;
alter table public.ai_usage_events add constraint ai_usage_events_kind_check check (kind = any (array[
  'tutor_turn','ai_mark','explain','flashcard_extract','flashcard_answer_check','lesson_mark']::text[]));
