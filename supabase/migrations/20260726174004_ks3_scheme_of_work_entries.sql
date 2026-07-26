-- ═══════════════════════════════════════════════════════════════════════
-- KS3 — fix scheme_of_work_entries so it can hold a KS3 scheme at all.
--
-- architecture.md §8.7 names two defects and calls them build-blocking for
-- KS3, and §10.1 puts this migration in Phase 1: "without it, §4.5 cannot be
-- honoured."
--
-- §4.5 is the invariant that year and sequence are metadata, never structure —
-- a school reorders KS3 by changing data, and nothing rebuilds. That promise
-- lives or dies in this table.
--
-- Defect 1: exam_board is NOT NULL with a CHECK restricted to real boards.
--           KS3 has no exam board, so every KS3 row would have to lie.
--           A 'None' sentinel is the WRONG fix — it pollutes the domain and
--           every consumer then has to special-case it. Allow NULL instead,
--           and require it to be NULL exactly when key_stage = 'KS3'.
--
-- Defect 2: the unique constraint is ineffective for KS3. It spans
--           (key_stage, year_group, tier, pathway, subject_id, exam_board,
--            academic_week), and tier/pathway/exam_board are all NULL on every
--           KS3 row. Postgres treats NULLs as DISTINCT in a unique index, so
--           duplicate KS3 scheme rows are currently allowed.
--
-- Safe to run against a table that already holds KS4 rows: no KS4 row changes,
-- and every constraint added is satisfied by existing KS4 data.
-- ═══════════════════════════════════════════════════════════════════════

begin;

-- ── Defect 1 ───────────────────────────────────────────────────────────

alter table public.scheme_of_work_entries
  alter column exam_board drop not null;

-- Replace the board CHECK so it tolerates NULL. The original constraint name
-- is looked up rather than assumed, because it may have been auto-generated.
--
-- The board list below must stay identical to the one in
-- 20260501212106_schools_layer.sql (both scheme_of_work_entries and
-- school_subject_settings): eight boards, not five. Tolerating NULL is the
-- ONLY change this constraint makes — narrowing the domain would silently
-- lock out any school on Eduqas, CIE or SQA.
do $$
declare
  c record;
begin
  for c in
    select con.conname
      from pg_constraint con
      join pg_class rel on rel.oid = con.conrelid
      join pg_namespace ns on ns.oid = rel.relnamespace
     where ns.nspname = 'public'
       and rel.relname = 'scheme_of_work_entries'
       and con.contype = 'c'
       and pg_get_constraintdef(con.oid) ilike '%exam_board%'
  loop
    execute format('alter table public.scheme_of_work_entries drop constraint %I',
                   c.conname);
  end loop;
end $$;

alter table public.scheme_of_work_entries
  add constraint scheme_of_work_entries_exam_board_check
  check (exam_board is null or exam_board in (
    'AQA', 'Edexcel', 'OCR', 'WJEC', 'CCEA', 'Eduqas', 'CIE', 'SQA'
  ));

-- The domain rule, stated once, in the database: KS3 has no board; KS4 must
-- have one. This is what stops a KS3 row quietly acquiring 'AQA' later.
alter table public.scheme_of_work_entries
  add constraint scheme_of_work_entries_ks3_has_no_board
  check (
    (key_stage = 'KS3' and exam_board is null)
    or (key_stage <> 'KS3' and exam_board is not null)
  );

-- KS3 has neither tier nor pathway (§2 anti-goal: it must never grow one).
-- Enforce that here too, mirroring profiles_tier_only_ks4_check.
alter table public.scheme_of_work_entries
  add constraint scheme_of_work_entries_ks3_no_tier_or_pathway
  check (
    key_stage <> 'KS3'
    or (tier is null and pathway is null)
  );

-- ── Defect 2 ───────────────────────────────────────────────────────────
-- A partial unique index scoped to KS3. Chosen over NULLS NOT DISTINCT so the
-- migration does not depend on PG15+, and so the KS4 uniqueness rule is left
-- exactly as it is. For KS3 the meaningful key is simply
-- (year_group, subject_id, academic_week) — tier, pathway and exam_board are
-- always NULL and carry no information.

create unique index if not exists scheme_of_work_entries_ks3_unique
  on public.scheme_of_work_entries (year_group, subject_id, academic_week)
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

alter table public.scheme_of_work_entries
  add constraint scheme_of_work_entries_ks3_subtopic_is_slug
  check (
    key_stage <> 'KS3'
    or subtopic is null
    or subtopic ~ '^[a-z0-9]+(-[a-z0-9]+)*$'
  );

comment on constraint scheme_of_work_entries_ks3_subtopic_is_slug
  on public.scheme_of_work_entries is
  'KS3 rows carry the permanent lesson slug in subtopic (architecture.md §8.4). '
  'Replace with a real FK when a lesson registry table exists (§8.7).';

comment on index public.scheme_of_work_entries_ks3_unique is
  'KS3 has no tier, pathway or exam board, so the base unique constraint is '
  'ineffective for it — Postgres treats NULLs as distinct. architecture.md §8.7 '
  'defect 2.';

commit;
