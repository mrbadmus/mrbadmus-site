-- B2C parent truth, part 2 (11 Oct 2026). Additive.
-- A lesson page keeps an answer it could not deliver (expired token, dropped
-- connection) in an outbox and re-sends it later. client_event_id is the id
-- the page gave that answer, so a re-send can never record it twice.
-- Apply AFTER 20261011124719_b2c_parent_truth.sql.
-- Rollback: supabase/rollbacks/20261011131302_b2c_parent_truth_client_event_id_rollback.sql
-- (and 20261011124719's rollback drops the whole table anyway).

alter table public.child_answers add column client_event_id uuid;
create unique index child_answers_client_event_uidx on public.child_answers (child_id, client_event_id) where client_event_id is not null;
