-- ROLLBACK for mrb321_terms_accepted_at. Apply by hand only.
-- ⚠️ Drops the record of WHEN each parent accepted the terms. Nothing else reads
-- it, so nothing breaks operationally — but the acceptance timestamps are the
-- evidence that the tick was given, and they cannot be recovered once dropped.
-- Take them off first if you may need them:
--   select id, terms_accepted_at from public.profiles where terms_accepted_at is not null;
-- Roll the backend back with it: /api/consumer/family/ensure and PATCH
-- /api/consumer/parent write this column, and GET /api/consumer/family and
-- GET /api/consumer/admin/accounts/:id read it.
alter table public.profiles
  drop column if exists terms_accepted_at;
