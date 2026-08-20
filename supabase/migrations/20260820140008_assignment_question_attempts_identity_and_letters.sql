-- MRB-270 phase 4 — an assignment attempt records WHICH QUESTION, and the
-- option letter is its own value.
--
-- ⚠️ APPLIED VIA MCP `apply_migration`; this file's timestamp is the version it
-- recorded (20260820140008) so `supabase db push` will not re-run it.
--
-- RULED 20 Aug 2026: "Attempt capture uses the columns Phase 5 of the last run
-- established: question identity not rung name, option letter and option text
-- as separate values."
--
-- ══ WHAT WAS ACTUALLY THERE, measured before writing this ══════════════════
--
-- The brief said this table "still has the old glued shape". The migration
-- that opened the letter columns on the OTHER table said the same thing —
-- 20260820091934 records that `assignment_question_attempts` "has the
-- identical glued shape". Both are wrong, and in a way that matters, because
-- the fix for a glued value is a split and the fix for a missing one is a
-- write.
--
--   assignment_question_attempts (2 rows, 19 Aug 19:38)
--       selected_answer = 'Nothing at all'      (14 chars, no tab)
--       correct_answer  = 'Nothing at all'
--       There is NO LETTER, glued or otherwise. It was never captured.
--
--   quiz_question_attempts (4 rows, 19 Aug 19:27)
--       selected_answer = 'B' || chr(9) || 'It is made of one or more cells'
--       That IS the glued shape — tab at position 2 — and 20260820091934
--       split it correctly.
--
-- ⊕ CORRECTION TO THE COMMENT THIS MIGRATION WAS APPLIED WITH. The applied SQL
-- says of quiz_question_attempts: "The columns were added and the writer was
-- not moved." THAT IS WRONG and is corrected here rather than quietly dropped.
-- The writer WAS moved — `shared/ks3.js:144` sends
-- `selected_option_letter: r.selectedLetter || null`. The four null rows all
-- predate the migration (19 Aug 19:27 against 20 Aug 09:19) and are exactly
-- the deliberate no-backfill that migration documents in as many words. The
-- letter columns on quiz are working; nothing has been written since.
--
-- What IS still true of both tables: neither records question IDENTITY.
-- quiz has `rung`, which the ruling explicitly says is not identity — six
-- questions in one lesson share "recall". `assignment_questions.source_ref`
-- is a lesson path ('chemistry/particles-and-their-behaviour/particle-model')
-- plus a rung, not the bank's stable per-question id, which
-- `compose_assignment` already carries as q["id"]. That is what question_ref
-- below is for, and quiz_question_attempts still wants the same column.

alter table public.assignment_question_attempts
  -- Question IDENTITY: the bank's own per-question id. A rung name is a
  -- difficulty, not a question, so it can never answer "which question did
  -- they get wrong" — the question the whole question-grain capture exists for.
  add column if not exists question_ref text,

  -- The letter and the text, separate. Together, neither is usable: you cannot
  -- GROUP BY the letter without parsing, and you cannot compare the text
  -- without stripping. Apart, both are ordinary columns. Knowing that nineteen
  -- students all chose the SAME wrong option is what turns a mark into a
  -- lesson plan.
  add column if not exists selected_option_letter text,
  add column if not exists correct_option_letter  text,

  -- Parity with quiz_question_attempts for the rungs that are not multiple
  -- choice, so one reader can read both tables.
  add column if not exists rung           text,
  add column if not exists criteria_met   smallint[],
  add column if not exists criteria_total smallint;

-- ⚖️ A SELF-MARKED OR WRITTEN RESPONSE RECORDS NO CORRECTNESS CLAIM. The
-- platform cannot know: a student can tick every criterion on gibberish. NULL,
-- never false — false is a claim that they got it WRONG, which is a different
-- and unevidenced statement. quiz_question_attempts already allows this and
-- uses it (two of its four rows are null); this table's NOT NULL made an
-- honest row impossible to write.
alter table public.assignment_question_attempts
  alter column is_correct drop not null;

comment on column public.assignment_question_attempts.question_ref is
  'Bank question id (compose_assignment q["id"]). Identity, not rung.';
comment on column public.assignment_question_attempts.is_correct is
  'NULL for self-marked or written responses: the platform cannot know. Never false in that case.';
