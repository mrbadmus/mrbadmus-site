-- MRB-352 Stage D — a pupil's own name for a completed flashcard set (the library).
-- Pupil-owned rows only. Nothing else reads it. REVERSIBLE: rollbacks/20261001090000_mrb352_flashcard_set_names_rollback.sql
begin;

create table if not exists public.flashcard_set_names (
  pupil_id       uuid not null references public.profiles(id) on delete cascade,
  assignment_id  uuid not null references public.assignments(id) on delete cascade,
  name           text not null check (char_length(btrim(name)) between 1 and 60),
  updated_at     timestamptz not null default now(),
  primary key (pupil_id, assignment_id)
);

drop trigger if exists flashcard_set_names_touch on public.flashcard_set_names;
create trigger flashcard_set_names_touch before update on public.flashcard_set_names
  for each row execute function public.mrb351_touch_updated_at();

alter table public.flashcard_set_names enable row level security;

-- The pupil's own rows, and only for a set they can see (the assignments policy
-- decides that: released, live, a class they are in).
drop policy if exists flashcard_set_names_select on public.flashcard_set_names;
create policy flashcard_set_names_select on public.flashcard_set_names for select using (
  pupil_id = (select auth.uid())
);
drop policy if exists flashcard_set_names_insert on public.flashcard_set_names;
create policy flashcard_set_names_insert on public.flashcard_set_names for insert with check (
  pupil_id = (select auth.uid())
  and exists (select 1 from public.assignments a where a.id = flashcard_set_names.assignment_id)
);
drop policy if exists flashcard_set_names_update on public.flashcard_set_names;
create policy flashcard_set_names_update on public.flashcard_set_names for update
  using (pupil_id = (select auth.uid()))
  with check (
    pupil_id = (select auth.uid())
    and exists (select 1 from public.assignments a where a.id = flashcard_set_names.assignment_id)
  );
drop policy if exists flashcard_set_names_delete on public.flashcard_set_names;
create policy flashcard_set_names_delete on public.flashcard_set_names for delete using (
  pupil_id = (select auth.uid())
);

revoke all on public.flashcard_set_names from anon;
grant select, insert, update, delete on public.flashcard_set_names to authenticated;
revoke truncate, references, trigger on public.flashcard_set_names from authenticated;

commit;
