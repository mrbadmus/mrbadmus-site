-- ROLLBACK for 20260901230851_mrb311_family_messages. Apply by hand only.
-- ⚠️ Drops every parent–child message. Leaves the supabase_realtime
-- publication in place (it predates this migration on production).
alter publication supabase_realtime drop table public.family_messages;
drop function if exists public.family_message_delete(uuid);
drop function if exists public.family_messages_mark_read(uuid);
drop table if exists public.family_messages;
drop function if exists public.family_message_allowed(uuid, uuid);
