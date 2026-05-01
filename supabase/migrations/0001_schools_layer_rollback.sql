-- =====================================================================
-- Rollback:    0001_schools_layer_rollback.sql
-- For:         0001_schools_layer.sql
-- Purpose:     Undo the entire schools layer migration cleanly.
--              Use ONLY if applied to production and a problem appears.
--              Branch failures don't need this — just drop the branch.
--
-- Safety:      Wrapped in a transaction. All-or-nothing.
-- Data loss:   Drops all NEW tables and their data.
--              Restores `profiles` to its pre-migration shape.
--              Existing 33 profile rows are NOT deleted, only un-extended.
-- =====================================================================

BEGIN;

-- 1. Drop new RLS policies on profiles (preserve original three)
DROP POLICY IF EXISTS profiles_teacher_read_students ON public.profiles;
DROP POLICY IF EXISTS profiles_hod_read_dept         ON public.profiles;
DROP POLICY IF EXISTS profiles_admin_read_school     ON public.profiles;

-- 2. Drop CHECK constraints we added to profiles
ALTER TABLE public.profiles DROP CONSTRAINT IF EXISTS profiles_role_check;
ALTER TABLE public.profiles DROP CONSTRAINT IF EXISTS profiles_key_stage_check;
ALTER TABLE public.profiles DROP CONSTRAINT IF EXISTS profiles_tier_only_ks4_check;
ALTER TABLE public.profiles DROP CONSTRAINT IF EXISTS profiles_hod_needs_department_check;
ALTER TABLE public.profiles DROP CONSTRAINT IF EXISTS profiles_staff_needs_school_check;

-- 3. Drop columns we added to profiles
ALTER TABLE public.profiles DROP COLUMN IF EXISTS school_id;
ALTER TABLE public.profiles DROP COLUMN IF EXISTS role;
ALTER TABLE public.profiles DROP COLUMN IF EXISTS department;
ALTER TABLE public.profiles DROP COLUMN IF EXISTS key_stage;
ALTER TABLE public.profiles DROP COLUMN IF EXISTS deleted_at;

-- 4. Restore exam_board default (was 'AQA' before migration)
ALTER TABLE public.profiles ALTER COLUMN exam_board SET DEFAULT 'AQA'::text;

-- 5. Drop columns we added to schools
ALTER TABLE public.schools DROP COLUMN IF EXISTS slug;
ALTER TABLE public.schools DROP COLUMN IF EXISTS email_domains;
ALTER TABLE public.schools DROP COLUMN IF EXISTS subdomain;
ALTER TABLE public.schools DROP COLUMN IF EXISTS show_on_public_leaderboard;
ALTER TABLE public.schools DROP COLUMN IF EXISTS key_stages_supported;
ALTER TABLE public.schools DROP COLUMN IF EXISTS departments;
ALTER TABLE public.schools DROP COLUMN IF EXISTS updated_at;
ALTER TABLE public.schools DROP COLUMN IF EXISTS deleted_at;

-- 6. Drop tables in reverse dependency order
DROP TABLE IF EXISTS public.audit_log                      CASCADE;
DROP TABLE IF EXISTS public.school_invitations             CASCADE;
DROP TABLE IF EXISTS public.assignment_question_attempts   CASCADE;
DROP TABLE IF EXISTS public.assignment_submissions         CASCADE;
DROP TABLE IF EXISTS public.assignments                    CASCADE;
DROP TABLE IF EXISTS public.class_teachers                 CASCADE;
DROP TABLE IF EXISTS public.class_members                  CASCADE;
DROP TABLE IF EXISTS public.classes                        CASCADE;
DROP TABLE IF EXISTS public.scheme_of_work_overrides       CASCADE;
DROP TABLE IF EXISTS public.scheme_of_work_entries         CASCADE;
DROP TABLE IF EXISTS public.school_subject_settings        CASCADE;
DROP TABLE IF EXISTS public.academic_years                 CASCADE;
DROP TABLE IF EXISTS public.subjects                       CASCADE;

-- 7. Drop helper functions
DROP FUNCTION IF EXISTS public.auth_user_school_id();
DROP FUNCTION IF EXISTS public.auth_user_role();
DROP FUNCTION IF EXISTS public.auth_user_department();
DROP FUNCTION IF EXISTS public.auth_user_id();
DROP FUNCTION IF EXISTS public.class_school_id(uuid);
DROP FUNCTION IF EXISTS public.auth_user_teaches_class(uuid);
DROP FUNCTION IF EXISTS public.auth_user_is_member_of_class(uuid);
DROP FUNCTION IF EXISTS public.auth_user_is_hod_of_subject_dept(uuid);

-- 8. Reset the 33 backfilled key_stage values? NO — they're already gone
--    because we dropped the column above. No-op.

COMMIT;

-- =====================================================================
-- After rollback: schema is back to pre-migration state.
-- profiles: 33 rows intact, original 21 columns, original 3 RLS policies.
-- schools: empty as before, original 6 columns, RLS enabled, no policies.
-- All other new tables: gone.
-- =====================================================================
