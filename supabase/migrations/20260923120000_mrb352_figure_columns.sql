-- MRB-352 — the `figure` column, at the two surfaces that do not have one yet.
--
-- Companion to docs/diagrams/figure-contract.md, which is the spec for the
-- whole feature: a question carries a `figure` ID (never an SVG blob), and a
-- build-time manifest (`build_figures.py` → `shared/figures.js` +
-- `figures.json`) is the only thing that turns an id into markup. This
-- migration is the database half of §1 and §6 of that contract — it does not
-- draw anything and does not validate that an id exists in the manifest;
-- an unknown id is `build_figures.py`'s failure to catch, not this table's.
--
-- ── WHY TWO TABLES, AND WHY NOT A THIRD ─────────────────────────────────
--
-- `public.ks3_assignment_bank` (renamed from `ks3_bank_questions` at MRB-288)
-- already carries `figure text` — it shipped with the table on
-- 20260820212341_ks3_question_pools_bank_and_ladder.sql and this migration
-- does not touch it.
--
-- `public.ks4_assignment_bank` (MRB-332) has no such column. Set work v2 and
-- the automatic weekly producer both compose from it, and the
-- described-diagrams audit (docs/diagrams/described-diagrams-audit.md) found
-- rows in it whose stems describe a picture in words instead of showing one.
--
-- `public.ks3_ladder_questions` (the KS3 lesson ladder's `recall`/`apply`
-- rungs, same migration as the assignment bank above) also has no `figure`
-- column. The practice round on the student class page serves from this
-- table — it is the ruled, frozen exception in pool_ownership's contract
-- (MRB-288) — and three of the audit's confirmed rows are ladder rungs. A
-- rung with no way to carry a figure id is a rung the fix run cannot fix.
--
-- ── ADDITIVE, NULLABLE, READ-OPTIONAL — SAFE BEFORE AND AFTER ───────────
--
-- Both columns are `text`, nullable, no default, no CHECK, no FK, no index.
-- `add column if not exists` makes the statement safe to run twice, and
-- there is no data migration: every existing row gets NULL, which is
-- "no figure", exactly the state every row is in today.
--
-- ⚠️ THIS MIGRATION IS NOT APPLIED TO PRODUCTION BY THIS RUN (per
-- figure-contract.md §6 and the task that produced this file). It is
-- rehearsed on TEST only (qeppkiswvclkkwbxmlok) — forward, verified,
-- rolled back, verified, forward again, verified. Reaching production is a
-- later, separate, deliberate step; see docs/diagrams/fix-run-report.md §7
-- for the exact command and the migration file's md5.
--
-- Both the exporter (`export_ks4_questions.py`) and the backend's `BANK_COLS`
-- KS4 arm are written to work whether or not this column exists on whichever
-- project they are pointed at — see `_has_figure_column()` in the exporter.
-- So a site/backend deploy that lands before this migration is applied, or a
-- rollback of this migration after one, is not a breaking change either way:
-- every reader either gets a real figure id or `figure: null`, never a 400.

alter table public.ks4_assignment_bank
  add column if not exists figure text;

comment on column public.ks4_assignment_bank.figure is
  'MRB-352. An id ([a-z0-9-]+) resolved against the build_figures.py manifest (shared/figures.js on the site, figures.json on the backend) — never SVG stored here. NULL means no figure, which is every row authored before this column existed. Nullable and read-optional by design: the exporter and the backend both work whether or not this column is present on a given project (figure-contract.md §6).';

alter table public.ks3_ladder_questions
  add column if not exists figure text;

comment on column public.ks3_ladder_questions.figure is
  'MRB-352. Same shape and same manifest as ks4_assignment_bank.figure and ks3_assignment_bank.figure (which already had one — MRB-288). Added here so PRACTICE (the frozen ks3_ladder_questions serving read, pool_ownership.py MRB-288) can show a figure on a recall/apply rung. NULL means no figure.';
