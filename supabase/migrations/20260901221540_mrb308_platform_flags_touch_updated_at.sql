-- MRB-308 Night 1, migration 9: make platform_flags.updated_at tell the truth.
--
-- The column was created with `default now()` and then never maintained, so
-- it recorded when the ROW was inserted and not when the FLAG last changed.
-- Measured during the night-1 drive: the value went true -> false -> true
-- while updated_at sat unchanged at its insert time.
--
-- That is a small trap with a bad moment to spring. The one question anyone
-- will ask this table is "when did consumer signup get switched on, and by
-- whom" — most likely during an incident, when a column that looks like an
-- answer but is actually the insert timestamp is worse than no column at all.
--
-- `subscriptions` already has exactly this trigger, so this is the same
-- pattern applied to the table that was missed rather than a new idea.

create or replace function public.platform_flags_touch_updated_at()
returns trigger language plpgsql as $fn$
begin
  new.updated_at := now();
  -- Records WHO, when a session is behind the write. A service-role or
  -- migration write has no auth.uid(), so this stays null there rather than
  -- inventing an actor.
  new.updated_by := coalesce(auth.uid(), new.updated_by);
  return new;
end $fn$;

drop trigger if exists trg_platform_flags_touch on public.platform_flags;
create trigger trg_platform_flags_touch
  before update on public.platform_flags
  for each row execute function public.platform_flags_touch_updated_at();
