-- mark_memo — the same answer always gets the same mark (Mide, 12 Nov 2026).
--
-- The backend's AI marker (consumer/marking.js, claudeMark) stores each mark
-- against a sha256 of: the marker version, the model, the question (id,
-- marks, every scheme point, its per-part caps, levels and rulings) and the
-- answer (NFKC, spaces collapsed). The same answer to the same question then
-- gets back exactly the stored mark, ticks and note, on any instance.
-- The answer itself is never stored here, only its hash.
--
-- Additive: one new table, read and written only by the service role. A
-- backend running before this table exists skips the memo and marks as before.
-- Rollback (rename, keeps the rows): supabase/rollbacks/20261112225055_mark_memo_rollback.sql

create table if not exists public.mark_memo (
  key         text primary key check (key ~ '^[0-9a-f]{64}$'),
  question_id text,
  result      jsonb not null,
  created_at  timestamptz not null default now()
);

comment on table public.mark_memo is
  'The same answer gets the same mark: one stored AI mark per (marker version, model, question, answer) hash. Service role only. No answer text is stored.';

alter table public.mark_memo enable row level security;
revoke all on public.mark_memo from anon, authenticated;
