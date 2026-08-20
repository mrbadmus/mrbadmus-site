-- Rollback for 20260820001539_written_rungs_claim_no_verdict.
-- Apply MANUALLY. The CLI never reads this folder.
--
-- ⚠️ THIS RE-INSTATES A FALSE CLAIM, and it cannot do so honestly. Restoring
-- NOT NULL requires a value for every self-marked rung, and there is no true
-- value — that is the entire finding. The UPDATE below writes `true`, which is
-- what the old code wrote and what the ruling calls wrong.
--
-- Roll back ONLY to unblock a deploy that must run the pre-4a backend and page,
-- and roll forward again as soon as it is unblocked.

UPDATE public.quiz_question_attempts
   SET is_correct = true
 WHERE is_correct IS NULL;

ALTER TABLE public.quiz_question_attempts
  ALTER COLUMN is_correct SET NOT NULL;

COMMENT ON COLUMN public.quiz_question_attempts.is_correct IS NULL;
