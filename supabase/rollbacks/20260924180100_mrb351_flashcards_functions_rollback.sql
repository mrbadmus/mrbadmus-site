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
