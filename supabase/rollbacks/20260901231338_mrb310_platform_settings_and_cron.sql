-- ROLLBACK for 20260901231338_mrb310_platform_settings_and_cron. Apply by hand only.
-- ⚠️ Unschedules the clock: no Sunday generation, no digests, no trial
-- reminders, no message batches. The extensions are left installed — other
-- things may come to depend on pg_cron, and dropping it is a separate
-- decision.
select cron.unschedule('consumer_weekly_utc17');
select cron.unschedule('consumer_weekly_utc18');
select cron.unschedule('consumer_daily_utc08');
select cron.unschedule('consumer_daily_utc09');
select cron.unschedule('consumer_hourly');
drop function if exists public.consumer_cron_call(text);
drop table if exists public.platform_settings;
