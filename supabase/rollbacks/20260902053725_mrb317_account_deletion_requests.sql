-- ROLLBACK for mrb317_account_deletion_requests. Apply by hand only.
-- ⚠️ Drops the deletion-request ledger. Any parent who asked for deletion
-- during the window loses the request (nothing else is lost — no sweep ever
-- executed one). The backend routes /family/delete-request and the Admin
-- accounts list read this table; roll the backend back with it.
drop policy if exists account_deletion_requests_read_own_org on public.account_deletion_requests;
drop table if exists public.account_deletion_requests;
