-- Rollback for 20261127120000_class_membership_rpcs.sql
-- Drops the membership functions. class_members rows and audit_log rows they
-- wrote are left exactly as they are (history is never deleted).
-- Apply manually only, and roll back the roster-import edge function to the
-- previous version first — it calls class_membership_batch.
drop function if exists public.class_past_members(uuid);
drop function if exists public.pupil_current_classes(uuid);
drop function if exists public.membership_targets(uuid);
drop function if exists public.membership_pupil_search(uuid, text);
drop function if exists public.can_manage_class_membership(uuid);
drop function if exists public.undo_membership_change(uuid[], uuid);
drop function if exists public.move_pupil(uuid, uuid, uuid, uuid);
drop function if exists public.remove_pupil_from_class(uuid, uuid, uuid);
drop function if exists public.add_pupil_to_class(uuid, uuid, uuid);
drop function if exists public.class_membership_batch(jsonb, uuid, text);
drop function if exists public._membership_apply(uuid, jsonb, uuid, text);
drop function if exists public._membership_name(public.profiles);
drop function if exists public._membership_leave(uuid, uuid, timestamptz);
drop function if exists public._membership_join(uuid, uuid, text, timestamptz);
drop function if exists public._membership_pupil(uuid, uuid);
drop function if exists public._membership_class(uuid, uuid);
drop function if exists public.working_academic_year_id(uuid);
drop function if exists public._membership_is_admin(uuid, uuid);
drop function if exists public._membership_actor(uuid);
