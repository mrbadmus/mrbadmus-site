-- Undo 20261112225055_mark_memo.sql: switch the memo off, keeping its rows.
-- The backend reads and writes `public.mark_memo` only; once it is renamed the
-- memo is skipped and every answer is marked afresh (temperature 0). Rehearsed
-- on TEST 12 Nov 2026 (rename away, a mark still made, rename back).
alter table if exists public.mark_memo rename to mark_memo_retired_20261112;
-- To remove it for good afterwards (Mide, by hand):
--   drop table if exists public.mark_memo_retired_20261112;
