-- MRB-275 phase 2 — a recall/quiz attempt records WHICH QUESTION.
--
-- ⚠️ APPLIED VIA MCP `apply_migration`; this file's timestamp is the version it
-- recorded (20260820160311) so `supabase db push` will not re-run it. That
-- rename is not cosmetic — `apply_migration` writes no local file and records
-- its OWN version, so a file named anything else is a second, unapplied
-- migration as far as the CLI is concerned.
--
-- ══ WHY, and what was measured first ═══════════════════════════════════════
--
-- The sibling table got exactly this on 20 Aug (20260820140008,
-- `assignment_question_attempts`). The last run flagged that
-- `quiz_question_attempts` still had no question identity and correctly scoped
-- it out; it is in scope now, same shape, same reasoning.
--
-- Measured on production before writing:
--
--   quiz_question_attempts already has, from earlier migrations —
--       rung                   text        (20260819122539)
--       criteria_met           smallint[]  (20260819134801)
--       criteria_total         smallint    (20260819134801)
--       selected_option_letter text        (20260820091934)
--       correct_option_letter  text        (20260820091934)
--       is_correct             boolean     NULLABLE already
--
--   ...and no question_ref. That is the only gap between the two tables.
--
-- ⚖️ `rung` IS NOT IDENTITY, and this is the whole point of the column. Every
-- recall rung across a lesson carries the string 'recall', so `group by rung`
-- can never answer "which question did they get wrong" — which is the only
-- question question-grain capture exists to answer. A difficulty band is not a
-- question, in the same way a year group is not a student.
--
-- ⚖️ NO BACKFILL, deliberately. Rows written before today have no recoverable
-- question identity: the rung name cannot be resolved back to one of six
-- questions that share it. They stay NULL, which is true, rather than being
-- guessed at, which would be a fabrication that reads exactly like data.
--
-- Additive and nullable, so nothing that writes today breaks.

alter table public.quiz_question_attempts
  add column if not exists question_ref text;

comment on column public.quiz_question_attempts.question_ref is
  'Stable per-question id (bank q["id"], or unit/lesson/rung for a ladder rung). Identity, not rung. NULL on rows written before 21 Aug 2026.';
