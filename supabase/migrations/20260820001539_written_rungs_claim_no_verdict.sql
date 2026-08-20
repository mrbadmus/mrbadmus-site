-- MRB-269 phase 4a — a self-marked rung stops claiming correctness.
--
-- ⚠️ APPLIED VIA MCP `apply_migration`; this file's timestamp is the version it
-- recorded (20260820001539) so `supabase db push` will not re-run it.
--
-- RULED (Mide, 20 Aug 2026). Rungs 3 and 4 of a KS3 mastery ladder are
-- SELF-marked: the student writes prose, the page reveals success criteria,
-- and the student ticks the ones they believe they met. The platform never
-- reads the prose. It cannot know whether the answer is right.
--
-- It said so anyway. `shared/ks3.js` sent `is_correct: !!r.met`, where `r.met`
-- on a self rung means only "the student ticked every box", and the column was
-- NOT NULL so there was nowhere else for it to land. The evidence is in the
-- data: of the four rows from the test attempt on b1-01,
--
--   index 2, rung `explain`, is_correct=true, criteria_met={1,2,3,4}
--   index 3, rung `produce`, is_correct=true, criteria_met={1,2,3,4}
--             selected_answer = 'test tsgd test tesb,da,hsc czlg test tsgd …'
--
-- — gibberish, recorded as correct. Nothing in the system could have known
-- otherwise, and nothing should have said otherwise.
--
-- So `is_correct` becomes NULLABLE and null is what a self-marked rung writes.
-- `criteria_met` / `criteria_total` stay exactly as they are: they are the
-- record of what the student CLAIMED, which is real data honestly labelled.
--
--   is_correct = true/false  → the platform marked it (recall, apply)
--   is_correct = null        → self-marked; see criteria_met for the claim
--
-- ⚠️ ORDER. This widening lands BEFORE the backend and the page start sending
-- null, or the insert fails. It is safe on its own: existing code sends a
-- boolean and continues to work unchanged. Full sequence was
--   this migration → backend `server.js` map → `shared/ks3.js` payload.
--
-- ⚑ NOT CHANGED, and deliberately: the quiz_scores summary row for that
-- attempt still reads 4/4. R8 scores all four rungs on the student's own
-- screen and the ladder already discloses "You marked rungs 3 and 4 yourself".
-- The ruling was about the CLAIM stored per question, not about restating a
-- student's score after the fact.

ALTER TABLE public.quiz_question_attempts
  ALTER COLUMN is_correct DROP NOT NULL;

COMMENT ON COLUMN public.quiz_question_attempts.is_correct IS
  'Whether the platform marked this attempt right. NULL on a self-marked rung '
  '(explain, produce): the student marks their own written answer and the '
  'platform cannot know. Read criteria_met / criteria_total for what the '
  'student claimed. MRB-269 phase 4a.';

-- The two written rungs from the existing test attempt. The table must not
-- hold a claim it cannot back, including retrospectively. The two MARKED rungs
-- (recall, apply) are genuine and are left alone.
UPDATE public.quiz_question_attempts
   SET is_correct = NULL
 WHERE rung IN ('explain', 'produce');
