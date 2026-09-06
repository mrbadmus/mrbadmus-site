-- MRB-326 — one live lesson per owner per slot, undefeatably.
--
-- WHY THIS EXISTS, GIVEN THE UNIQUE INDEXES ALREADY DO MOST OF IT
--
-- `timetable_entries_teacher_slot_unique` keys on
--   (teacher_id, academic_year_id, weekday, period, coalesce(week_cycle,''))
-- where deleted_at is null — and `timetable_entries_pending_slot_unique` does
-- the same for an unclaimed colleague's `pending_staff_id` rows. Between them
-- they already catch the duplicate that actually shipped: a `seeded` row and a
-- `manual` row in one slot. `source` is NOT part of either key, so the second
-- write fails whatever it calls itself. That half is covered, and this
-- migration does not change it.
--
-- What NEITHER index can see is the NULL cycle. `week_cycle` is NULL for
-- "every week", 'A'/'B' for a two-week timetable, and `coalesce(week_cycle,'')`
-- makes NULL just another distinct value — so a row with week_cycle = 'A' and
-- a row with week_cycle = NULL sit in the SAME slot without tripping the
-- index, because '' <> 'A'. That is not a theoretical hole: NULL means the
-- lesson runs EVERY week, which includes week A, so the pair is a genuine
-- double-booking that the index is structurally unable to notice. No school on
-- the platform uses week_cycle today, and the invariant must hold before one
-- does rather than after.
--
-- The trigger closes exactly that gap, and nothing else:
--   · a live row (deleted_at is null) already in the same
--     (owner, academic_year_id, weekday, period),
--   · where either row's week_cycle IS NULL, or the two are equal,
--   → raises 23505 (unique_violation), the same class of error the index
--     raises, so a caller that already handles the index's failure handles
--     this one unchanged.
--
-- It is deliberately NOT a check on soft-deleted rows: retiring a row and
-- writing its replacement is the normal `replace_timetable` path, and a
-- retired row occupies no slot. NEW.deleted_at IS NOT NULL therefore returns
-- immediately — that is a soft delete, or an update to an already-retired row.
--
-- ⚠️ THE SAME-STATEMENT CASE, MEASURED RATHER THAN ASSUMED. `replace_timetable`
-- writes its whole grid in ONE multi-row INSERT, and the obvious worry is that
-- a BEFORE ROW trigger cannot see rows written earlier in its own command. It
-- can: the guard's SELECT is an SPI query, which takes a fresh snapshot, so
-- row two of a statement sees row one. Rehearsed on TEST — two rows for one
-- (teacher, year, weekday 3, period 4) in a single INSERT were refused BY THIS
-- TRIGGER, naming the earlier row of the same statement. The unique index
-- backs it up for the equal-cycle case regardless.
--
-- The legitimate replace path is unaffected, and that was rehearsed too: the
-- RPC retires this teacher's live rows in one statement and inserts the new
-- grid in the next, and a retired row occupies no slot, so the replacement
-- lands in the same slots without tripping anything.
--
-- SECURITY INVOKER is sufficient, and that is a statement about the policies
-- rather than a hope: `timetable_entries_own_all` is FOR ALL with
-- `teacher_id = auth.uid()`, so a teacher writing a row can, by construction,
-- see every row it could clash with; `timetable_entries_admin_read` only
-- widens the read; and the seeded `pending_staff_id` rows are written by the
-- service role, which bypasses RLS entirely. No writer can hide a clash from
-- this check by not being allowed to see it.

create or replace function public.timetable_entries_slot_guard()
returns trigger
language plpgsql
security invoker
set search_path = public, pg_temp
as $$
declare
  v_clash uuid;
begin
  -- A retired row occupies no slot.
  if new.deleted_at is not null then
    return new;
  end if;

  select e.id
    into v_clash
    from public.timetable_entries e
   where e.deleted_at is null
     and e.id <> new.id
     and e.academic_year_id = new.academic_year_id
     and e.weekday = new.weekday
     and e.period  = new.period
     and (
           (new.teacher_id is not null and e.teacher_id = new.teacher_id)
        or (new.pending_staff_id is not null and e.pending_staff_id = new.pending_staff_id)
         )
     -- NULL means every week, so it collides with every cycle.
     and (e.week_cycle is null or new.week_cycle is null or e.week_cycle = new.week_cycle)
   limit 1;

  if v_clash is not null then
    raise exception using
      errcode = '23505',
      message = format('timetable slot already taken: weekday %s, period %s', new.weekday, new.period),
      detail  = format('a live entry (%s) already occupies this slot for this teacher in this academic year', v_clash),
      hint    = 'retire the existing entry (set deleted_at) before writing another lesson into the same slot';
  end if;

  return new;
end;
$$;

comment on function public.timetable_entries_slot_guard() is
  'MRB-326: refuses a second LIVE lesson in one (owner, year, weekday, period) '
  'where either row has week_cycle NULL — the collision the unique indexes '
  'cannot see, because coalesce(week_cycle, '''') makes NULL a distinct value.';

drop trigger if exists timetable_entries_slot_guard on public.timetable_entries;

create trigger timetable_entries_slot_guard
  before insert or update on public.timetable_entries
  for each row execute function public.timetable_entries_slot_guard();
