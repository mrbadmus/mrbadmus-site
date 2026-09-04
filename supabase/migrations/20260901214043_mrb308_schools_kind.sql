-- MRB-308 Night 1, migration 1 of 6: org kinds.
--
-- "A family is a tiny school; a council is a school without a timetable."
-- (Mide, 1 Sep 2026, locked.) One column carries that distinction; there is
-- no synthetic consumer school and no second org table.
--
-- Recon note: NOTHING here needs widening. Every school-specific column on
-- `schools` (slug, subdomain, email_domains, key_stages_supported,
-- departments, admin_user_id) is ALREADY nullable or defaulted, and there is
-- no URN / SSO-domain / tenant column at all. `code` is NOT NULL but carries
-- no unique index, so a family row can hold a generated code safely.

alter table public.schools
  add column if not exists kind text not null default 'school';

alter table public.schools
  drop constraint if exists schools_kind_check;

alter table public.schools
  add constraint schools_kind_check
  check (kind in ('school', 'family', 'organisation'));

-- The privacy property, made STRUCTURAL rather than remembered.
--
-- The leaderboard is entirely global: neither weekly_challenges nor
-- weekly_scores carries a school_id, and every endpoint scopes only on
-- (week_start, subject, pathway, tier). A family child taking a weekly
-- challenge would otherwise surface by name and avatar beside Rainford
-- students. `show_on_public_leaderboard` already existed as the seam; this
-- makes it impossible for a consumer org to be created facing outward,
-- rather than relying on every future creation path to remember.
alter table public.schools
  drop constraint if exists schools_consumer_orgs_are_private;

alter table public.schools
  add constraint schools_consumer_orgs_are_private
  check (kind = 'school' or coalesce(show_on_public_leaderboard, true) = false);

-- Consumer orgs are looked up by kind constantly (admin lists, the
-- leaderboard exclusion set). Rainford is one row among what will become
-- many families, so index the small side.
create index if not exists idx_schools_kind_consumer
  on public.schools (kind)
  where kind <> 'school' and deleted_at is null;

comment on column public.schools.kind is
  'MRB-308. school = a real school with a timetable (Rainford). family = one '
  'paying parent household, parent is staff+admin, children are members. '
  'organisation = a council//service: staff are caseworkers, no timetable. '
  'Consumer kinds are sealed from every cross-org query and must have '
  'show_on_public_leaderboard = false (enforced by '
  'schools_consumer_orgs_are_private).';
