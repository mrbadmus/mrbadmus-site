-- MRB-318 Night 3 — an organisation's "groups" compile as classes inside the org
-- (Mide, MRB-316). A pupil already owns exactly one class (Night 1: the per-child
-- class practice is composed on), so a group class must be tellable apart from it.
-- One nullable column: NULL for every school class (untouched), 'child' for the
-- per-child class a family or organisation pupil owns, 'group' for a caseworker's group.
alter table public.classes
  add column if not exists consumer_kind text
  check (consumer_kind is null or consumer_kind in ('child', 'group'));

comment on column public.classes.consumer_kind is
  'MRB-318: NULL = school class; child = the one class a consumer pupil owns; group = an organisation group (a class with members drawn from several per-child classes). Readers of a child''s own class must exclude ''group''.';

-- Backfill: every class that already exists inside a consumer org is a per-child
-- class (groups did not exist before tonight). Zero rows on TEST and on prod today;
-- kept so the rule holds if this ever lands on a database that has families.
update public.classes c
   set consumer_kind = 'child'
 where c.consumer_kind is null
   and c.deleted_at is null
   and exists (select 1 from public.schools s
                where s.id = c.school_id and s.kind in ('family', 'organisation'));
