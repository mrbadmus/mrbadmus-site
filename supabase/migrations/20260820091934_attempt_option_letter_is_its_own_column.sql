-- MRB-270 phase 5 — the option LETTER stops being glued to the option TEXT.
--
-- ⚠️ APPLIED VIA MCP `apply_migration`; this file's timestamp is the version it
-- recorded (20260820091934) so `supabase db push` will not re-run it.
--
-- `selected_answer` held "ANothing at all": the letter badge and the label,
-- read off one element and concatenated. MRB-239 made that at least SPLITTABLE
-- by joining with a TAB, which authored prose cannot contain — but it recorded
-- the fix's own note that "two real columns remain the right answer and are
-- still open". This opens them.
--
-- Why it matters at the point of capture rather than at read time: per-
-- distractor analysis is the main reason the question grain was ruled in.
-- Knowing that nineteen students all chose the SAME wrong option is what turns
-- a mark into a lesson plan, and that needs the letter as a value you can
-- GROUP BY, not a prefix you have to guess the length of. An option beginning
-- with a capital is indistinguishable from a letter prefix.
--
-- Both new columns are NULLABLE and NOTHING IS BACKFILLED. The four existing
-- rows keep their tab-joined form: the history is small and honest, and a
-- backfill that guessed which side of the tab was the letter would be worse
-- than a gap. From here `selected_answer` / `correct_answer` carry the option
-- TEXT ALONE and the letter is beside it.
--
-- Free-text (self-marked) rungs carry no letter and so leave both null, which
-- is what null means here: there was no lettered option to record — not that
-- one failed to be read.
--
-- ⚑ SCOPE. This is the KS3 LADDER path only (shared/ks3.js → /api/quiz-score →
-- quiz_question_attempts). `assignment_question_attempts` has the identical
-- glued shape and is deliberately NOT changed: its writer is
-- student/assignment.html, a live page this run does not touch, so a column
-- there would only ever be null. It is the same fix and it is still open.

alter table public.quiz_question_attempts
  add column if not exists selected_option_letter text,
  add column if not exists correct_option_letter  text;

comment on column public.quiz_question_attempts.selected_option_letter is
  'The letter badge of the option the student chose (A/B/C/D). NULL on a '
  'free-text rung, which has no lettered options. MRB-270 phase 5.';

comment on column public.quiz_question_attempts.correct_option_letter is
  'The letter badge of the option that was correct (A/B/C/D). NULL on a '
  'free-text rung. MRB-270 phase 5.';

comment on column public.quiz_question_attempts.selected_answer is
  'The TEXT of the option the student chose, without the letter badge — the '
  'letter is in selected_option_letter. Rows created before MRB-270 phase 5 '
  'hold "<letter>\<tab>><text>"; nothing was backfilled.';

comment on column public.quiz_question_attempts.correct_answer is
  'The TEXT of the option that was correct, without the letter badge. On a '
  'self-marked rung this carries the success criteria, tab-separated.';
