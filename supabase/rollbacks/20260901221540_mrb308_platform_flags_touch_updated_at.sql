-- ROLLBACK for 20260901221540_mrb308_platform_flags_touch_updated_at.
-- Apply by hand only. The Supabase CLI never reads this folder.
--
-- ⚠️ What reverting COSTS you. Without the trigger, platform_flags.updated_at
-- goes back to being nothing but `default now()` on INSERT: it records when the
-- ROW WAS INSERTED, not when the flag last changed. The value can then go
-- true -> false -> true with updated_at sitting unmoved at its insert time, and
-- updated_by never filled in at all.
--
-- That is the failure mode worth naming, because it does not look like one. The
-- question this table gets asked is "when did consumer signup get switched on,
-- and by whom" — asked during an incident, in a hurry, by someone who will read
-- updated_at as the answer. A column that looks like an answer but is actually
-- the insert timestamp is worse than no column at all.

drop trigger if exists trg_platform_flags_touch on public.platform_flags;
drop function if exists public.platform_flags_touch_updated_at();
