-- B2C parent truth, part 4 (11 Oct 2026). Additive.
-- Many KS3 lesson blocks only REVEAL the answer on screen; the right option
-- lives only in the authored lesson data. answer_key carries it so the
-- backend can record a consumer child's choice as right or wrong. Never sent
-- to a page. Apply AFTER 20261011154346.
-- Rollback: supabase/rollbacks/20261011170510_b2c_parent_truth_answer_key_rollback.sql

alter table public.question_knowledge_points add column answer_key text;
comment on column public.question_knowledge_points.answer_key is 'The right option''s text, from the authored lesson data, for lesson questions whose page reveals rather than marks. NULL when the question has no single right option. Used by the backend to mark a consumer child''s choice; never shown on a page.';
