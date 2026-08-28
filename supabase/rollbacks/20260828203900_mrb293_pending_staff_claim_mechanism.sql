-- Rollback for 20260828203900_mrb293_pending_staff_claim_mechanism. Apply MANUALLY.
-- Restores handle_new_user to its pre-MRB-293 body and removes the claim mechanism.
-- ⚠️ ORDER MATTERS. Apply rollbacks/20260828204639_mrb293_hook_admits_pending_staff.sql
-- FIRST. The live hook_before_user_created references public.pending_staff, which this
-- file drops; reversing the order leaves every Microsoft sign-in raising at the gate.
--
-- NOTE: this does NOT remove class_teachers rows or staff_scopes already granted by a
-- claim. Those are ordinary live rows; end them the ordinary way if that is intended.
drop trigger if exists on_auth_user_signin_claim on auth.users;
drop function if exists public.handle_user_signin_claim();

create or replace function public.handle_new_user()
returns trigger
language plpgsql
security definer
as $fn$
BEGIN
  INSERT INTO public.profiles (id)
  VALUES (NEW.id)
  ON CONFLICT (id) DO NOTHING;
  RETURN NEW;
END;
$fn$;

drop function if exists public.claim_pending_staff(uuid);
drop table if exists public.pending_staff_classes;
drop table if exists public.pending_staff_scopes;
drop table if exists public.pending_staff;
