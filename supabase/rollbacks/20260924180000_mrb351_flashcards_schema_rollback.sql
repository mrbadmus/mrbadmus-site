-- Rollback for 20260924180000_mrb351_flashcards_schema.sql (MRB-351).
-- Apply by hand, AFTER 20260924180100's rollback (its functions reference
-- these tables). The Supabase CLI never reads this folder.
--
-- ⚠️ LOSSY. Dropping these tables discards every deck, every card, every
-- pupil's written answer, rating and sitting, and the flashcard assignments
-- themselves. EVERYTHING this file deletes or drops, in the order it does
-- it (⊕ MRB-351 landing stream J, 27 Sep 2026 — listed explicitly, not just
-- named in the queries below, after this header was found to name only
-- three of the real casualties):
--   · submission_feedback rows on a flashcard submission (a teacher's
--     "well done" under a finished deck)
--   · assignment_question_attempts rows on a flashcard submission
--   · assignment_submissions rows for every flashcard assignment (every
--     pupil's completed deck, on time or late)
--   · assignment_questions rows for a flashcard assignment, via its own
--     ON DELETE CASCADE (confirmed empty in practice — flashcard question
--     data lives in flashcard_cards/flashcard_pupil_cards, never in
--     assignment_questions — but the FK exists on both TEST and production
--     and would cascade a real row if one ever existed)
--   · student_message_reads rows whose source is a flashcard assignment
--   · student_notifications rows for a flashcard assignment
--   · every flashcard_reviews / flashcard_pupil_cards / flashcard_events /
--     flashcard_sessions / assignment_flashcards row (their tables are
--     DROPPED, not filtered — everything in them, for every assignment)
--   · every flashcard assignment row itself (public.assignments where
--     kind = 'flashcards')
--   · every flashcard_extractions / flashcard_cards / flashcard_decks row
--     (their tables are DROPPED — every deck and every extraction, whether
--     or not it was ever assigned)
--   · ai_usage_events rows with kind in ('flashcard_extract',
--     'flashcard_answer_check') — the AI-marking usage log for flashcards
--
-- Check first:
--
--   select count(*) from public.assignments where kind = 'flashcards';
--   select count(*) from public.flashcard_decks;
--   select count(*) from public.flashcard_events;
--   select count(*) from public.ai_usage_events
--    where kind in ('flashcard_extract', 'flashcard_answer_check');
--
-- ⚠️ ASSIGNMENTS FIRST. The widened CHECKs cannot be narrowed back while a
-- flashcard assignment exists, so this rollback SOFT-DELETES nothing and
-- HARD-DELETES the flashcard rows (and their submissions) before narrowing.
-- On production that is the loss of real pupils' completed homework: do not
-- run it there without Mide's explicit go-ahead for exactly that loss.
--
-- ⊕ MRB-351 landing, stream B, follow-up (Opus review, 27 Sep 2026) —
-- EVERY FOREIGN KEY INTO `assignment_submissions`/`assignments` MUST BE
-- CLEARED FIRST, NOT JUST THE TWO THIS FILE ALREADY KNEW ABOUT.
-- `submission_feedback.submission_id -> assignment_submissions(id) ON DELETE
-- RESTRICT` and `assignment_question_attempts.submission_id ->
-- assignment_submissions(id)` (no ON DELETE clause, so it defaults to
-- RESTRICT too) both hard-fail the DELETE below the moment a single feedback
-- row or attempt row references a flashcard submission — a teacher who wrote
-- "well done" under a finished deck, or (defensively) any question-attempt
-- row that somehow got attached to one, would turn this rollback into a
-- 23503 instead of a clean revert. Checked against `pg_constraint` on TEST
-- (`SELECT conrelid::regclass, conname, pg_get_constraintdef(oid) FROM
-- pg_constraint WHERE contype='f' AND confrelid IN
-- ('assignment_submissions'::regclass, 'assignments'::regclass)`): those are
-- the only two FKs into `assignment_submissions` besides this file's own
-- `assignment_submissions.assignment_id -> assignments(id)`, which the
-- ordering below already satisfies by deleting submissions before
-- assignments. `flashcard_events`/`flashcard_pupil_cards`/
-- `flashcard_reviews`/`flashcard_sessions`.assignment_id and
-- `assignment_flashcards`.assignment_id all reference `assignments(id)` too,
-- but their own tables are DROPPED below before `assignments` rows are
-- deleted, which removes the constraint along with the table — no separate
-- delete needed for those four.
--
-- ⊕ MRB-351 landing stream J, 27 Sep 2026 — RE-SWEPT AGAINST BOTH DATABASES,
-- READ-ONLY, PRODUCTION INCLUDED. The query above was only ever run on TEST;
-- production has never had this migration applied, so its FK set was never
-- checked against what this rollback actually needs to survive there once
-- it has been. Same query, `confrelid` widened to also include
-- `ai_usage_events` (this file deletes rows from it too):
--
--   production (urklkrwevjtlfbwnipjn) — assignment_question_attempts,
--   submission_feedback (both as above), PLUS one this file never named:
--   `assignment_questions.assignment_id -> assignments(id) ON DELETE
--   CASCADE`. Harmless in practice — a flashcard assignment has no rows in
--   `assignment_questions` (that table is the MCQ/ladder question-bank
--   link; flashcard content lives in `flashcard_cards`/
--   `flashcard_pupil_cards`), so the cascade fires on zero rows — but it IS
--   a real FK on production and belongs in this account rather than being
--   silently relied on. No explicit DELETE is added for it: CASCADE means
--   Postgres does it for free, in any order, and adding one would only
--   create a second thing to keep in sync with a table this rollback does
--   not otherwise touch.
--
--   TEST (qeppkiswvclkkwbxmlok) — the same set PLUS `assignment_questions`
--   again, plus the four flashcard-table FKs this comment already named
--   (`flashcard_events`/`flashcard_pupil_cards`/`flashcard_reviews`/
--   `flashcard_sessions`.assignment_id) and `assignment_flashcards`, all
--   already handled by dropping their tables before `assignments` rows are
--   deleted. Production has none of those five tables at all, so this is
--   the complete list of what production adds beyond the two already
--   handled by name: exactly the one CASCADE, and nothing this rollback's
--   existing order fails to survive.

begin;

delete from public.submission_feedback
 where submission_id in (
   select id from public.assignment_submissions
    where assignment_id in (select id from public.assignments where kind = 'flashcards')
 );
delete from public.assignment_question_attempts
 where submission_id in (
   select id from public.assignment_submissions
    where assignment_id in (select id from public.assignments where kind = 'flashcards')
 );
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

-- ⊕ MRB-351 landing stream J, 27 Sep 2026 — Step 3 of
-- supabase/rollbacks/README.md, matching the pattern already used by
-- 20260927100000's and 20260924180100's own rollbacks: the MCP connector
-- has been observed stamping `schema_migrations` with its own timestamp
-- rather than the file's, so this matches on the name as well as the
-- canonical version and is a no-op if neither matches.
delete from supabase_migrations.schema_migrations
 where version = '20260924180000'
    or name    = 'mrb351_flashcards_schema';
