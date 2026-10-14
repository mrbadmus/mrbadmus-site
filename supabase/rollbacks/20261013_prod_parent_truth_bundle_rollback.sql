-- ROLLBACK for supabase/baselines/20261013_prod_parent_truth_bundle.sql (production).
--
-- Non-destructive: the two tables are RENAMED out of the way, with their
-- indexes, so every recorded row is kept and the bundle can be applied again
-- later. The backend probes for public.child_answers before every ledger
-- write and read; once it is renamed, the backend records nothing new and the
-- parent activity route answers 503 not_ready — school pupils are unaffected
-- (the ledger is consumer-children only).
--
-- REHEARSED on TEST (qeppkiswvclkkwbxmlok) 13 Oct 2026, in scratch schema rh,
-- as the full cycle: bundle forward (48 columns, 10 indexes, RLS on both) →
-- this rollback (table + index renames) → bundle forward again: all succeeded.
-- The DROP-based variant could not be rehearsed (the Supabase connector
-- auto-declines any DROP) and is kept separately as
-- 20261013_prod_parent_truth_bundle_PURGE_destroys_data.sql — Mide only, by hand.
--
-- Apply with apply_migration (one transaction).

alter table public.child_tutor_questions rename to child_tutor_questions_retired_20261013;
alter table public.child_answers rename to child_answers_retired_20261013;
alter index public.child_answers_pkey rename to child_answers_retired_20261013_pkey;
alter index public.child_answers_child_time_idx rename to child_answers_retired_20261013_child_time_idx;
alter index public.child_answers_child_question_idx rename to child_answers_retired_20261013_child_question_idx;
alter index public.child_answers_work_item_idx rename to child_answers_retired_20261013_work_item_idx;
alter index public.child_answers_visit_idx rename to child_answers_retired_20261013_visit_idx;
alter index public.child_answers_source_idx rename to child_answers_retired_20261013_source_idx;
alter index public.child_answers_client_event_uidx rename to child_answers_retired_20261013_client_event_uidx;
alter index public.child_answers_lesson_ai_marks_idx rename to child_answers_retired_20261013_lesson_ai_marks_idx;
alter index public.child_tutor_questions_pkey rename to child_tutor_questions_retired_20261013_pkey;
alter index public.child_tutor_questions_child_idx rename to child_tutor_questions_retired_20261013_child_idx;
