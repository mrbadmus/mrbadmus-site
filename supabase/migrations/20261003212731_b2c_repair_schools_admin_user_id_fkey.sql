-- B2C repair (3 Oct 2026) — make TEST carry production's schools.admin_user_id FK.
--
-- Production has `schools_admin_user_id_fkey` (schools.admin_user_id → profiles.id);
-- TEST did not. With it, profiles and schools have TWO relationships, and an
-- unhinted PostgREST embed `profiles?select=…,schools!inner(…)` fails with
-- PGRST201 (ambiguous embed). That is how the /go/ child login broke on prod
-- while passing on TEST. Adding the FK to TEST makes TEST reproduce prod.
--
-- Definition copied from production via pg_get_constraintdef:
--   FOREIGN KEY (admin_user_id) REFERENCES profiles(id)
--   (not deferrable, validated, ON UPDATE/ON DELETE NO ACTION, MATCH SIMPLE)
--
-- IDEMPOTENT: adds the constraint only if it is missing, so on production
-- (where it already exists) this is a no-op.
DO $$
BEGIN
  IF NOT EXISTS (
    SELECT 1 FROM pg_constraint
    WHERE conname = 'schools_admin_user_id_fkey'
      AND conrelid = 'public.schools'::regclass
  ) THEN
    ALTER TABLE public.schools
      ADD CONSTRAINT schools_admin_user_id_fkey
      FOREIGN KEY (admin_user_id) REFERENCES public.profiles(id);
  END IF;
END
$$;

NOTIFY pgrst, 'reload schema';

-- TEST registry note (rehearsal 3 Oct 2026): apply_migration recorded its own
-- versions. 20261003212700 = first apply, 20261003212715 = rollback rehearsal,
-- 20261003212731 = final re-apply (this file). The connector declined the
-- DELETE of the 20261003212700 row, so all three rows remain on TEST.
