-- ROLLBACK for MRB-308 Night 1, migration 6 of 6
-- (20260901214558_mrb308_child_accounts). Apply MANUALLY only.
--
-- ⚠️ APPLY FIRST, before any other MRB-308 rollback. These five functions read
-- schools.kind (migration 1), profiles.mode / intensity / created_by and the
-- 'parent_added' joined_via value (migration 2), and public.subscriptions
-- (migration 3). Every one of those is dropped by a rollback further down the
-- stack, and a plpgsql body is not checked until it runs — so a function left
-- standing over a dropped column fails on a live parent action, not here.
--
-- Order within this file: parent_remove_child and parent_update_child both
-- call parent_owns_child, so the callers go before the callee.
--
-- ⚠️ Dropping these does NOT remove any child. Their profiles, per-child
-- classes, class_members and class_teachers rows all stay, and so does every
-- attempt they have made. Nothing here touches student work.

drop function if exists public.parent_remove_child(uuid);

drop function if exists public.parent_update_child(uuid, text, int, text, text, text, text);

drop function if exists public.attach_child_to_family(uuid, uuid, text, int, text, text, text, text, text, text);

drop function if exists public.child_username_check(text);

drop function if exists public.parent_owns_child(uuid, uuid);
