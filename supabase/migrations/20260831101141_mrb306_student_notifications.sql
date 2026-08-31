-- MRB-306 WS-3 — in-platform student reminders.
--
-- A teacher presses one button; the students who have not completed this
-- week's assignment get told ON MRBADMUSAI. Nothing leaves the platform:
-- no email, no Resend, no push.
--
-- Applied to prod 31 Aug 2026 via MCP apply_migration after rehearsal on TEST,
-- where the rate limit was proven in all four directions (same-day duplicate
-- refused, CO-TEACHER same-day duplicate refused, previous day accepted,
-- kind='nag' rejected). This filename's version matches the version the MCP
-- recorded in schema_migrations, so `db push` will not re-apply it.

create table if not exists public.student_notifications (
  id            uuid primary key default gen_random_uuid(),
  student_id    uuid not null references public.profiles(id),
  class_id      uuid not null references public.classes(id),
  assignment_id uuid not null references public.assignments(id),
  -- FIXED TEMPLATE ONLY. There is deliberately no `message` column: a
  -- teacher-to-minor free-text channel is a safeguarding decision, not an
  -- engineering one, and it is parked for Mide. The wording is composed on
  -- read from the class, the assignment and the sender's display name.
  kind          text not null default 'reminder' check (kind in ('reminder')),
  sent_by       uuid not null references public.profiles(id),
  -- The rate limit's calendar day, stamped SERVER-side in the school's own
  -- timezone. Never the device clock, and never UTC — a 23:30 reminder in
  -- London must not read as tomorrow.
  sent_on       date not null default (now() at time zone 'Europe/London')::date,
  created_at    timestamptz not null default now(),
  read_at       timestamptz
);

-- THE RATE LIMIT, held by the database rather than by the UI: one reminder per
-- student per assignment per calendar day. Deliberately NOT scoped by sender —
-- a co-taught class must not be able to nudge the same child twice in a day.
create unique index if not exists student_notifications_one_per_day
  on public.student_notifications (student_id, assignment_id, sent_on);

create index if not exists student_notifications_student_unread_idx
  on public.student_notifications (student_id, read_at);
create index if not exists student_notifications_class_idx
  on public.student_notifications (class_id, assignment_id, created_at desc);

comment on table public.student_notifications is
  'MRB-306: in-platform reminders. Fixed template only, no free text; one per student per assignment per calendar day (Europe/London), enforced by student_notifications_one_per_day.';

alter table public.student_notifications enable row level security;

-- A student sees their own, and may only ever mark one read. The column-level
-- grant is what stops a student rewriting sent_by or assignment_id; RLS alone
-- cannot restrict columns.
drop policy if exists student_notifications_student_read on public.student_notifications;
create policy student_notifications_student_read on public.student_notifications for select
  using (student_id = auth.uid());

drop policy if exists student_notifications_student_mark_read on public.student_notifications;
create policy student_notifications_student_mark_read on public.student_notifications for update
  using      (student_id = auth.uid())
  with check (student_id = auth.uid());

-- A teacher may send only as themselves, and only into a class they teach.
drop policy if exists student_notifications_teacher_send on public.student_notifications;
create policy student_notifications_teacher_send on public.student_notifications for insert
  with check (sent_by = auth.uid() and public.auth_user_teaches_class(class_id));

-- A teacher reads every reminder on a class they teach, not only their own.
-- This is a CORRECTNESS requirement, not a convenience: the rate limit above
-- is cross-teacher, so a co-teacher who could not see a colleague's reminder
-- would be shown an enabled button that then failed on the unique index.
drop policy if exists student_notifications_teacher_read on public.student_notifications;
create policy student_notifications_teacher_read on public.student_notifications for select
  using (public.auth_user_teaches_class(class_id));

drop policy if exists student_notifications_admin_read on public.student_notifications;
create policy student_notifications_admin_read on public.student_notifications for select
  using (public.class_school_id(class_id) = public.auth_user_school_id()
         and public.auth_user_has_scope('school_admin'));

revoke update on public.student_notifications from authenticated;
grant  update (read_at) on public.student_notifications to authenticated;
