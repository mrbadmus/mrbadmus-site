-- Rollback for 20260924180100_mrb351_flashcards_functions.sql (MRB-351).
-- Apply by hand, BEFORE the schema rollback. Loses no data: functions only.

begin;
drop function if exists public.flashcard_pupil_detail(uuid, uuid);
drop function if exists public.flashcard_progress(uuid, timestamptz);
drop function if exists public.mrb351_teacher_gate(uuid);
drop function if exists public.flashcard_record(uuid, jsonb);
drop function if exists public.mrb351_active_between(uuid, timestamptz, timestamptz);
drop function if exists public.mrb351_session_refresh(uuid);
drop function if exists public.flashcard_card_state(uuid, uuid);
drop function if exists public.flashcard_edit_assignment(uuid, text, timestamptz, text, timestamptz);
drop function if exists public.flashcard_set_work(uuid[], uuid, text, text, text, timestamptz, timestamptz, text, text);
drop function if exists public.flashcard_deck_duplicate(uuid);
drop function if exists public.flashcard_deck_save(uuid, text, jsonb, jsonb, boolean);
drop function if exists public.flashcard_quick_check(text, text);
commit;

-- ⊕ MRB-351 landing stream J, 27 Sep 2026 — Step 3 of
-- supabase/rollbacks/README.md, matching the pattern already used by
-- 20260927100000's own rollback: the MCP connector has been observed
-- stamping `schema_migrations` with its own timestamp rather than the
-- file's, so this matches on the name as well as the canonical version and
-- is a no-op if neither matches.
delete from supabase_migrations.schema_migrations
 where version = '20260924180100'
    or name    = 'mrb351_flashcards_functions';
