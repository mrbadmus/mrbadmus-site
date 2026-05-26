-- =====================================================================
-- Migration:        0007_add_assignment_day_of_week.sql
-- Stage:            2B — Class detail page (MRB-38)
-- Branch:           schools/mrb-38-class-detail
-- Apply target:     Test project first → production after verification
-- Author:           Drafted 9 May 2026
-- =====================================================================
--
-- Adds classes.assignment_day_of_week — the weekday on which a class's
-- assignment week starts (0 = Sunday … 6 = Saturday, matching postgres
-- EXTRACT(dow FROM ...)).
--
-- Used by the MRB-38 class-detail page to compute the current
-- assignment-week window for the weekly Stars leaderboard.
--
-- Nullable on purpose: existing classes stay NULL after this migration
-- and the UI falls back to Monday (1). Future work may derive this
-- from class_teachers timetable data; the column would then be either
-- retired or kept as an explicit override.
--
-- Additive only — no DROPs, no UPDATEs to existing rows.
-- Wrapped in a single transaction.
-- =====================================================================

BEGIN;

ALTER TABLE classes
  ADD COLUMN assignment_day_of_week smallint NULL;

ALTER TABLE classes
  ADD CONSTRAINT classes_assignment_day_of_week_chk
  CHECK (assignment_day_of_week BETWEEN 0 AND 6);

COMMIT;
