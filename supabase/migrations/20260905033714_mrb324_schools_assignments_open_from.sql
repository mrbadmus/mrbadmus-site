-- MRB-324: the assignments go-live hold.
--
-- ⚠️ Applied with apply_migration, which records its OWN version per project,
-- so the two environments hold DIFFERENT versions for this one migration:
--     PROD (urklkrwevjtlfbwnipjn) 20260905033714  ← this filename
--     TEST (qeppkiswvclkkwbxmlok) 20260905032924
-- The filename tracks PROD, as the rest of this folder does. TEST already has
-- the column; do not re-apply there on the strength of the name not matching.
--
-- A school can delay when its classes start COMPOSING assignments. Before this
-- date the backend's composition path in GET /api/class/current-assignment
-- refuses and returns reason='assignments_not_open_yet' as an ordinary 200 —
-- students see the normal "no work set yet" empty state, nothing errors.
--
-- Already-composed assignments are served untouched regardless of this date:
-- the guard sits AFTER the "already composed?" branch, so a school that turns
-- the hold on does not retract work its students can already see.
--
-- NULL (the default, and every existing row) means no hold: compose as today.
alter table public.schools
  add column if not exists assignments_open_from date;

comment on column public.schools.assignments_open_from is
  'MRB-324 assignments go-live hold. When set and strictly in the future, the backend refuses to compose NEW assignments for this school''s classes (GET /api/class/current-assignment returns 200 with reason=assignments_not_open_yet). Already-composed assignments are unaffected. NULL means no hold.';
