-- MRB-308 Night 1, migration 2 of 6: the `parent` role, and the child fields.
--
-- Recon finding that shapes this: the estate does NOT branch on
-- profiles.role. Of 96 live policies exactly two mention `role`, and both
-- compare against 'student'. Authority flows through auth_user_has_scope()
-- and a staff_scopes row, ALWAYS conjoined with
-- `school_id = auth_user_school_id()`. I verified there is no policy in the
-- estate that grants a scope without that conjunct.
--
-- So adding 'parent' here grants NOTHING by itself, which is exactly what we
-- want. A parent becomes staff+admin of their own family by holding a
-- staff_scopes row scoped to that family — and is a stranger everywhere else.
-- No policy is rewritten. No helper is edited.

alter table public.profiles
  drop constraint if exists profiles_role_check;

alter table public.profiles
  add constraint profiles_role_check
  check (role in ('student', 'teacher', 'hod', 'admin', 'parent'));

-- ⚠️ NOT adding a username column. Recon found `profiles.username` already
-- live as citext NOT NULL, uniquely indexed, auto-assigned to every profile
-- by the profiles_username_guard trigger, with username_available() /
-- username_rejection_reason() already enforcing 3-20 chars, charset, and a
-- profanity + impersonation screen. Child login keys on THAT column. Adding
-- a second handle would leave two competing identities on one table.

-- How the child works, and how hard. Null for school students, who reach
-- their work through a real timetable instead.
alter table public.profiles
  add column if not exists mode text,
  add column if not exists intensity text,
  add column if not exists created_by uuid references public.profiles(id);

alter table public.profiles
  drop constraint if exists profiles_mode_check;
alter table public.profiles
  add constraint profiles_mode_check
  check (mode is null or mode in ('alongside_school', 'home_education'));

-- Three levels, defined here rather than left to the caller.
--   light  ~2 sessions/week  - the alongside-school default. Tracks the
--                              school's scheme of work, does not lead it.
--   steady ~3 sessions/week  - the middle setting, either mode.
--   full   ~5 sessions/week  - the home-education default. The platform IS
--                              the scheme of work.
alter table public.profiles
  drop constraint if exists profiles_intensity_check;
alter table public.profiles
  add constraint profiles_intensity_check
  check (intensity is null or intensity in ('light', 'steady', 'full'));

-- A child is created BY somebody: a parent, or organisation staff. This is
-- what makes "remove a child" soft-deletable and auditable, and what lets
-- Admin tell a consumer child from a school student without a join.
comment on column public.profiles.created_by is
  'MRB-308. The parent or organisation staff member who created this child '
  'account. NULL for self-signup and for CSV-imported school students.';
comment on column public.profiles.mode is
  'MRB-308. alongside_school = light, tracks the school SOW. '
  'home_education = full, the platform IS the SOW. NULL for school students.';
comment on column public.profiles.intensity is
  'MRB-308. light ~2 / steady ~3 / full ~5 sessions per week. Parent-settable.';

-- A parent-created child joins their class by neither code, CSV, SIMS nor an
-- admin. Additive: widening a CHECK cannot invalidate an existing row.
alter table public.class_members
  drop constraint if exists class_members_joined_via_check;
alter table public.class_members
  add constraint class_members_joined_via_check
  check (joined_via in ('code', 'csv_import', 'sims_sync', 'admin_added', 'parent_added'));
