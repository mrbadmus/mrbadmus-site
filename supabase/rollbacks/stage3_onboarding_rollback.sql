-- =====================================================================
-- Rollback:  Stage 3 — Schools Onboarding (SSO + CSV import + merge)
-- Reverses:  20260530140000_stage3_sso_domain_hook.sql
--            20260530140100_stage3_audit_writers.sql
--            20260530140200_stage3_account_claims_merge.sql
--            20260530140400_stage3_import_helpers.sql
-- Apply:     MANUALLY only (the Supabase CLI never reads supabase/rollbacks/).
-- =====================================================================
--
-- ⚠️ BEFORE running this, UN-REGISTER the Before-User-Created auth hook in
--    Dashboard > Authentication > Hooks (or config.toml) — dropping the
--    function while it is still registered as the active hook will block
--    ALL sign-ups. Disable the hook first, then run this.
--
-- ⚠️ This does NOT drop Stage-1 objects (public.audit_log, the
--    schools.email_domains column). Those predate Stage 3.
--
-- ⚠️ Any student accounts already created by the CSV importer, and any
--    completed account merges, are DATA — this rollback does not reverse
--    them. It only removes the Stage-3 functions/table.
-- =====================================================================

BEGIN;

-- 20260530140200_stage3_account_claims_merge.sql
DROP FUNCTION IF EXISTS public.confirm_account_claim_and_reparent(text);
DROP FUNCTION IF EXISTS public.create_account_claim(uuid, text, text, int);
DROP FUNCTION IF EXISTS public.reparent_student(uuid, uuid);
DROP POLICY  IF EXISTS account_claims_self_read ON public.account_claims;
DROP TABLE   IF EXISTS public.account_claims;

-- 20260530140400_stage3_import_helpers.sql
DROP FUNCTION IF EXISTS public.user_id_for_email(text);

-- 20260530140100_stage3_audit_writers.sql
DROP FUNCTION IF EXISTS public.log_my_event(text, jsonb);
DROP FUNCTION IF EXISTS public.write_audit_event(text, text, uuid, jsonb, uuid, uuid);

-- 20260530140000_stage3_sso_domain_hook.sql
DROP FUNCTION IF EXISTS public.hook_before_user_created(jsonb);
DROP FUNCTION IF EXISTS public.school_id_for_email_domain(text);

COMMIT;
