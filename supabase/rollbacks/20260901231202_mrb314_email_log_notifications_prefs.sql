-- ROLLBACK for 20260901231202_mrb314_email_log_notifications_prefs. Apply by hand only.
-- ⚠️ Drops the send log — and with it the dedupe keys, so the next cron
-- re-sends every digest and reminder it has already sent.
drop function if exists public.consumer_notifications_mark_read(uuid[]);
drop table if exists public.parent_prefs;
drop table if exists public.consumer_notifications;
drop table if exists public.email_log;
