-- MRB-239 Phase 2c — assignment provenance is the tuple
-- (school_id, key_stage, year_group, subject_id, academic_week), not a
-- foreign key to a scheme-of-work row. assignments_source_sow_entry_id_fkey
-- only points at scheme_of_work_entries (global default), which cannot
-- express a school that has diverged (scheme_of_work_overrides) and dangles
-- on every ks3_seed_sow.py reseed. assignments holds zero rows, so there is
-- no data to migrate.
ALTER TABLE public.assignments
  ADD COLUMN school_id uuid REFERENCES public.schools(id),
  ADD COLUMN key_stage text,
  ADD COLUMN year_group smallint,
  ADD COLUMN academic_week smallint;

COMMENT ON COLUMN public.assignments.source_sow_entry_id IS
  'Superseded by the (school_id, key_stage, year_group, subject_id, academic_week) provenance tuple, MRB-239 (16 Aug 2026) — a scheme_of_work_entries FK cannot express a school that has diverged (scheme_of_work_overrides) and dangles on every ks3_seed_sow.py reseed. Left in place, unused, rather than dropped.';
