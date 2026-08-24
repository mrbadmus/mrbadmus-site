-- Manual rollback for 20260824214940_mrb288_rename_bank_to_assignment_bank.
-- Apply by hand only. Restores the pre-MRB-288 table name and object names,
-- and re-points the ingest RPC's bank branch back at it. If this is ever
-- applied, the code in BOTH repos must be reverted with it — the backend and
-- shared/student-live.js read the table by name.
alter table public.ks3_assignment_bank rename to ks3_bank_questions;
alter table public.ks3_bank_questions
  rename constraint ks3_assignment_bank_pkey to ks3_bank_questions_pkey;
alter table public.ks3_bank_questions
  rename constraint ks3_assignment_bank_band_check to ks3_bank_questions_band_check;
alter index public.ks3_assignment_bank_lesson_band_idx
  rename to ks3_bank_questions_lesson_band_idx;
alter policy ks3_assignment_bank_read on public.ks3_bank_questions
  rename to ks3_bank_questions_read;
-- Then re-apply the function body from 20260822101051_ks3_cards.sql verbatim
-- (its bank branch inserts into ks3_bank_questions).
