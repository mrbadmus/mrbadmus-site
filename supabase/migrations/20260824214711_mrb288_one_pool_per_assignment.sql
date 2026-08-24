-- MRB-288 (Mide's ruling, 24 Aug 2026): one bank per surface. A weekly
-- assignment is composed from the assignment pool and nothing else, so a
-- NEWLY composed assignment_questions row must carry a band (the assignment
-- pool's difficulty axis) and no rung (the lesson ladder's).
--
-- NOT VALID is deliberate: the 18 Aug hand-seeded demo assignment
-- (282f2277-77ae-4931-93c0-356a5dee891e) holds two rung-sourced rows that are
-- historical test data, kept until the pending demo-assignment cleanup. The
-- constraint still enforces on every NEW row; VALIDATE CONSTRAINT runs after
-- that cleanup deletes them.
--
-- This CONSTRAINS COMPOSITION ONLY. assignment_question_attempts.rung is a
-- record of what a student answered and is deliberately not constrained.
--
-- Applied to production 24 Aug 2026 via MCP apply_migration (which records
-- its own version — this filename matches schema_migrations, the MRB-84
-- drift gotcha handled). Rehearsed on test (qeppkiswvclkkwbxmlok) first:
-- rung row rejected, band row accepted, both observed.
alter table public.assignment_questions
  add constraint one_pool_per_assignment
  check (band is not null and rung is null) not valid;
