-- ROLLBACK for 20260906045015_mrb327_operator_email_setting. Apply by hand only.
--
-- Removes the ops-digest recipient. Nothing breaks: consumer/email.js reads
-- the key at send time and, finding nothing, skips the 07:00 send with
-- reason 'no_operator_email'. /api/consumer/admin/health then reports
-- operator_email_set: false, which is the truthful state.
--
-- The table comment is put back to what MRB-310/315 left it as.
delete from public.platform_settings where key = 'operator_email';

comment on table public.platform_settings is
  'MRB-310/315. Operator-editable platform values. Service role writes; operators read.';
