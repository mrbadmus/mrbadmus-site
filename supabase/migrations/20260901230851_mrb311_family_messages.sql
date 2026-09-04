-- MRB-311 Night 2, migration 4 of 9: parent–child chat, sealed inside the org.
--
-- The ruling: two-way parent↔child chat, sealed inside the family; council
-- staff → pupils the same; NO child↔child path anywhere, enforced at policy
-- level, not in the UI.
--
-- family_message_allowed() is the whole rule, in one place:
--   * both parties in the same family- or organisation-kind org
--   * a student may address only a non-student of that org (parent / staff)
--   * a non-student may address only a student of that org
-- so child→sibling, child→other family's child, parent→other family's child,
-- and adult→adult are all impossible at INSERT. The 0011 matrix asserts each.
--
-- Sending requires the org to be in the 'full' access state: a locked or
-- read-only org can read its history and send nothing.
--
-- Realtime: the table joins the supabase_realtime publication so both sides
-- get live delivery, filtered by the SELECT policy. REPLICA IDENTITY FULL so
-- an UPDATE (read_at) carries enough for the policy to run.

create table if not exists public.family_messages (
  id            uuid primary key default gen_random_uuid(),
  org_id        uuid not null references public.schools(id),
  sender_id     uuid not null references public.profiles(id),
  recipient_id  uuid not null references public.profiles(id),
  body          text not null,
  created_at    timestamptz not null default now(),
  read_at       timestamptz,
  deleted_at    timestamptz,
  constraint family_messages_body_len check (char_length(body) between 1 and 1000),
  constraint family_messages_not_self check (sender_id <> recipient_id)
);

create index if not exists idx_family_messages_thread
  on public.family_messages (org_id, least(sender_id, recipient_id), greatest(sender_id, recipient_id), created_at desc);
create index if not exists idx_family_messages_unread
  on public.family_messages (recipient_id) where read_at is null and deleted_at is null;

alter table public.family_messages replica identity full;
alter table public.family_messages enable row level security;

create or replace function public.family_message_allowed(p_sender uuid, p_recipient uuid)
returns boolean
language sql
stable
security definer
set search_path to 'public'
as $fn$
  select p_sender is not null
     and p_recipient is not null
     and p_sender <> p_recipient
     and exists (
       select 1
         from public.profiles s
         join public.profiles r   on r.school_id = s.school_id
         join public.schools  org on org.id = s.school_id
        where s.id = p_sender
          and r.id = p_recipient
          and s.deleted_at is null
          and r.deleted_at is null
          and org.deleted_at is null
          and org.kind in ('family', 'organisation')
          and (
                -- a child may only address an adult of their own org
                (s.role = 'student' and r.role in ('parent', 'teacher', 'hod', 'admin'))
                -- an adult may only address a child of their own org
             or (s.role in ('parent', 'teacher', 'hod', 'admin') and r.role = 'student')
          )
     );
$fn$;

comment on function public.family_message_allowed(uuid, uuid) is
  'MRB-311. The one rule for who may message whom. No child→child path exists.';

drop policy if exists family_messages_party_read on public.family_messages;
create policy family_messages_party_read on public.family_messages
  for select using (
    deleted_at is null
    and org_id = public.auth_user_school_id()
    and (sender_id = auth.uid() or recipient_id = auth.uid())
  );

drop policy if exists family_messages_operator_read on public.family_messages;
create policy family_messages_operator_read on public.family_messages
  for select using (public.auth_user_operator_active());

drop policy if exists family_messages_send on public.family_messages;
create policy family_messages_send on public.family_messages
  for insert with check (
    sender_id = auth.uid()
    and org_id = public.auth_user_school_id()
    and public.family_message_allowed(auth.uid(), recipient_id)
    and public.org_access_state(org_id) = 'full'
    and read_at is null
    and deleted_at is null
  );

-- No UPDATE or DELETE policy. Read receipts and the sender's soft delete go
-- through the two functions below, which check auth.uid() themselves.
revoke update, delete on public.family_messages from anon, authenticated;

create or replace function public.family_messages_mark_read(p_from uuid)
returns integer
language plpgsql
security definer
set search_path to 'public'
as $fn$
declare n integer;
begin
  update public.family_messages
     set read_at = now()
   where recipient_id = auth.uid()
     and sender_id = p_from
     and read_at is null
     and deleted_at is null;
  get diagnostics n = row_count;
  return n;
end
$fn$;

create or replace function public.family_message_delete(p_id uuid)
returns boolean
language plpgsql
security definer
set search_path to 'public'
as $fn$
declare n integer;
begin
  update public.family_messages
     set deleted_at = now()
   where id = p_id
     and sender_id = auth.uid()
     and deleted_at is null;
  get diagnostics n = row_count;
  return n = 1;
end
$fn$;

revoke all on function public.family_messages_mark_read(uuid) from public;
grant execute on function public.family_messages_mark_read(uuid) to authenticated;
revoke all on function public.family_message_delete(uuid) from public;
grant execute on function public.family_message_delete(uuid) to authenticated;

-- Live delivery.
do $do$
begin
  if not exists (select 1 from pg_publication where pubname = 'supabase_realtime') then
    create publication supabase_realtime;
  end if;
  if not exists (
    select 1 from pg_publication_tables
     where pubname = 'supabase_realtime' and schemaname = 'public' and tablename = 'family_messages'
  ) then
    alter publication supabase_realtime add table public.family_messages;
  end if;
end
$do$;

comment on table public.family_messages is
  'MRB-311. Parent↔child and staff↔pupil messages, sealed inside the org by family_message_allowed(). Soft delete by sender only; read receipts by recipient only; both via SECURITY DEFINER functions.';