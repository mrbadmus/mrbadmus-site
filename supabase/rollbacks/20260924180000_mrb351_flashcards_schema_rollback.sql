-- Rollback for 20260924180000_mrb351_flashcards_schema.sql (MRB-351).
-- Apply by hand, AFTER 20260924180100's rollback (its functions reference
-- these tables). The Supabase CLI never reads this folder.
--
-- ⚠️ LOSSY. Dropping these tables discards every deck, every card, every
-- pupil's written answer, rating and sitting, and the flashcard assignments
-- themselves. Check first:
--
--   select count(*) from public.assignments where kind = 'flashcards';
--   select count(*) from public.flashcard_decks;
--   select count(*) from public.flashcard_events;
--
-- ⚠️ ASSIGNMENTS FIRST. The widened CHECKs cannot be narrowed back while a
-- flashcard assignment exists, so this rollback SOFT-DELETES nothing and
-- HARD-DELETES the flashcard rows (and their submissions) before narrowing.
-- On production that is the loss of real pupils' completed homework: do not
-- run it there without Mide's explicit go-ahead for exactly that loss.

begin;

delete from public.assignment_submissions
 where assignment_id in (select id from public.assignments where kind = 'flashcards');
delete from public.student_message_reads
 where source = 'work'
   and source_id in (select id from public.assignments where kind = 'flashcards');
delete from public.student_notifications
 where assignment_id in (select id from public.assignments where kind = 'flashcards');

drop table if exists public.flashcard_reviews;
drop table if exists public.flashcard_pupil_cards;
drop table if exists public.flashcard_events;
drop table if exists public.flashcard_sessions;
drop table if exists public.assignment_flashcards;

delete from public.assignments where kind = 'flashcards';

alter table public.assignments drop constraint if exists assignments_deck_id_fkey;
drop table if exists public.flashcard_extractions;
drop table if exists public.flashcard_cards;
drop table if exists public.flashcard_decks;

drop function if exists public.mrb351_deck_card_count();
drop function if exists public.mrb351_touch_updated_at();

alter table public.assignments drop constraint if exists assignments_flashcard_shape;
alter table public.assignments drop constraint if exists assignments_kind_check;
alter table public.assignments drop constraint if exists assignments_flashcard_mode_check;
alter table public.assignments drop constraint if exists assignments_completion_rule_check;
drop index if exists public.assignments_kind_idx;
alter table public.assignments
  drop column if exists completion_rule,
  drop column if exists flashcard_mode,
  drop column if exists deck_id,
  drop column if exists kind;
alter table public.assignments drop constraint if exists assignments_quiz_type_check;
alter table public.assignments add constraint assignments_quiz_type_check
  check (quiz_type = any (array['topic_quiz', 'subtopic_quiz', 'weekly_challenge']));

delete from public.ai_usage_events where kind in ('flashcard_extract', 'flashcard_answer_check');
alter table public.ai_usage_events drop constraint if exists ai_usage_events_kind_check;
alter table public.ai_usage_events add constraint ai_usage_events_kind_check
  check (kind = any (array['tutor_turn', 'ai_mark', 'explain']));
alter table public.ai_usage_events drop column if exists deck_id, drop column if exists assignment_id;

drop policy if exists teacher_uploads_staff_read on storage.objects;
-- The bucket's objects must be emptied (Storage API or dashboard) before the
-- bucket row can go; left in place deliberately so no file is lost silently.
-- delete from storage.buckets where id = 'teacher-uploads';

commit;
