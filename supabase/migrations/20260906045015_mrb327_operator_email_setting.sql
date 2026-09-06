-- MRB-327 §5 (ops health): the address the 07:00 operator digest goes to.
--
-- DATA, not schema. public.platform_settings already exists (MRB-310,
-- Night 2 migration 9 of 9) and this adds exactly one row to it. It is a
-- checked-in migration rather than a hand-typed INSERT because the repo and
-- the database have to agree about it: /api/consumer/admin/health reports
-- operator_email_set, and a setting that exists on TEST and nowhere in the
-- repo is a setting that silently will not exist on production.
--
-- ⚠️ The VALUE is RESOLVED from the database rather than written literally,
-- so this file is correct in every environment it is applied to — on TEST it
-- lands on the harness operator, on production it lands on Mide. Writing an
-- address into a migration would have shipped a TEST fixture's mailbox to
-- production the day this merged.
--
-- With no active operator at all it stores 'null' — the same deliberately
-- unset shape cron_target_url and cron_secret already use — and
-- consumer/email.js skips the send with reason 'no_operator_email' rather
-- than mailing nobody.
--
-- Mide repoints it at any time, with no deploy, because email.js reads it at
-- send time:
--   update public.platform_settings
--      set value = '"someone@example.com"'::jsonb, updated_at = now()
--    where key = 'operator_email';

insert into public.platform_settings (key, value, note)
select
  'operator_email',
  coalesce(
    to_jsonb((
      select u.email
        from public.platform_operators po
        join auth.users u on u.id = po.profile_id
       where po.ended_at is null
         and po.deleted_at is null
         and u.email is not null
       order by po.started_at asc
       limit 1)),
    'null'::jsonb),
  'MRB-327. Recipient of the 07:00 ops digest, sent from /api/consumer/cron/hourly. Read at send time, so a change here takes effect the next morning with no deploy. "null" means no digest is sent.'
on conflict (key) do nothing;

comment on table public.platform_settings is
  'MRB-310/315/327. Operator-editable platform values: consumer cap defaults, the cron target and secret, and the ops-digest recipient. Service role writes; operators read.';
