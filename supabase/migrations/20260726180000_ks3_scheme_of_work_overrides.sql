-- ═══════════════════════════════════════════════════════════════════════
-- KS3 — fix scheme_of_work_overrides so it can hold a school's KS3 scheme.
--
-- The companion to 20260726120000_ks3_scheme_of_work_entries.sql. That one
-- fixed the GLOBAL table, which holds the platform's published default
-- sequence (architecture.md §7, ruled 2026-07-26). This one fixes the
-- PER-SCHOOL table, which holds what a school actually teaches.
--
-- Both tables are load-bearing for the same invariant. §4.5:
--
--     "Reordering a school's entire KS3 curriculum must require zero content
--      changes and zero regeneration — it is a data change in that school's
--      scheme of work."
--
-- The "school's scheme of work" in that sentence IS this table. Fixing only
-- the global table would have left the default sound and every override
-- unsound, which is the half that schools actually write to.
--
-- ── Why the defect list is two long, not three ─────────────────────────
--
-- §8.7 names three problems on scheme_of_work_entries. **Defect 1
-- (exam_board NOT NULL with a CHECK restricted to real boards) DOES NOT APPLY
-- HERE: scheme_of_work_overrides has no exam_board column at all.** Nothing to
-- relax and nothing to constrain — a school-level override is already scoped
-- by school_id, and the board is a property of the school's KS4 settings, not
-- of a scheme row. So this migration is deliberately shorter than its
-- companion, and that asymmetry is real rather than an omission.
--
-- Defect 2: the unique constraint is ineffective for KS3. It spans
--           (school_id, key_stage, year_group, tier, pathway, subject_id,
--            academic_week), and tier and pathway are NULL on every KS3 row.
--           Postgres treats NULLs as DISTINCT in a unique index, so duplicate
--           KS3 override rows are currently allowed — the same school could
--           hold two different lessons in Year 8 Chemistry week 12 and the
--           database would not object.
--
-- Defect 3: nothing forces tier and pathway to be NULL at KS3, so a KS3
--           override row can quietly acquire a tier. §2 anti-goal: KS3 has
--           neither tier nor pathway and must never grow one.
--
-- Plus the free-text problem §8.7 raises alongside them: subtopic is free
-- text, so KS3 lesson slugs will drift.
--
-- Safe to run against a table that already holds KS4 rows: no KS4 row changes,
-- every constraint added is scoped to key_stage = 'KS3', and the existing
-- UNIQUE is left exactly as it is.
-- ═══════════════════════════════════════════════════════════════════════

begin;

-- ── Defect 3 ───────────────────────────────────────────────────────────
-- KS3 has neither tier nor pathway (§2 anti-goal: it must never grow one).
-- Mirrors scheme_of_work_entries_ks3_no_tier_or_pathway, and classes'
-- classes_tier_only_ks4_check before that. Stated once, in the database, so
-- it does not depend on every writer remembering.
--
-- This is also the precondition for the index below: the partial unique index
-- ignores tier and pathway entirely, which is only sound because they are
-- provably NULL.

alter table public.scheme_of_work_overrides
  add constraint scheme_of_work_overrides_ks3_no_tier_or_pathway
  check (
    key_stage <> 'KS3'
    or (tier is null and pathway is null)
  );

-- ── Defect 2 ───────────────────────────────────────────────────────────
-- A partial unique index scoped to KS3. Chosen over NULLS NOT DISTINCT so the
-- migration does not depend on PG15+, and so the KS4 uniqueness rule is left
-- exactly as it is. For KS3 the meaningful key is
-- (school_id, year_group, subject_id, academic_week) — tier and pathway are
-- always NULL and carry no information. school_id is what makes this the
-- per-school table, so unlike its global counterpart it leads the key.

create unique index if not exists scheme_of_work_overrides_ks3_unique
  on public.scheme_of_work_overrides
     (school_id, year_group, subject_id, academic_week)
  where key_stage = 'KS3';

-- ── Lesson slug, not free text ─────────────────────────────────────────
-- §8.7: "topic / subtopic are free text. KS3 rows should carry the lesson slug
-- in subtopic, and ideally gain a real foreign key once a lesson registry table
-- exists. Free text will drift."
--
-- No lesson registry table exists yet (lessons live in ks3_data/, and Phase 5
-- is where server-side content lands), so a FK is not available. What IS
-- available is a shape constraint: KS3 slugs are kebab-case, which at least
-- catches "Particle Model" and "particle_model" before they drift apart.
--
-- Drift matters more here than on the global table, not less: an override row
-- whose subtopic no longer matches any lesson slug is a school pointing at a
-- lesson that does not exist, and it will fail silently rather than loudly.

alter table public.scheme_of_work_overrides
  add constraint scheme_of_work_overrides_ks3_subtopic_is_slug
  check (
    key_stage <> 'KS3'
    or subtopic is null
    or subtopic ~ '^[a-z0-9]+(-[a-z0-9]+)*$'
  );

comment on constraint scheme_of_work_overrides_ks3_subtopic_is_slug
  on public.scheme_of_work_overrides is
  'KS3 rows carry the permanent lesson slug in subtopic (architecture.md §8.4). '
  'Replace with a real FK when a lesson registry table exists (§8.7).';

comment on constraint scheme_of_work_overrides_ks3_no_tier_or_pathway
  on public.scheme_of_work_overrides is
  'KS3 has no tier and no pathway (architecture.md §2 anti-goal). Also the '
  'precondition for scheme_of_work_overrides_ks3_unique, which ignores both '
  'columns.';

comment on index public.scheme_of_work_overrides_ks3_unique is
  'KS3 has no tier or pathway, so the base unique constraint is ineffective '
  'for it — Postgres treats NULLs as distinct. architecture.md §8.7 defect 2, '
  'applied to the per-school table. Note there is no exam_board column here, '
  'so §8.7 defect 1 does not apply to this table.';

commit;
