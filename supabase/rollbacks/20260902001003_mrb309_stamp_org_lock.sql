-- ROLLBACK for mrb309_stamp_org_lock. Apply by hand only.
-- ⚠️ The backend's consumer/stripe.js stampLock() calls this function on
-- every webhook event and from the daily sweep; without it every event logs
-- "stamp_org_lock failed" and locked_at is never maintained. Access is
-- unaffected (org_access_state never reads locked_at) — the account card's
-- "access ended" date is what you lose. Roll the backend back with it.
drop function if exists public.stamp_org_lock(uuid);
