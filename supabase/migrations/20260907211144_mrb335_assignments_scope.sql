-- MRB-335 — SET WORK v2. What an assignment must carry once a teacher chooses
-- a TOPIC rather than a scheme-of-work row.
--
-- ⚠️ VERSION IS LOAD-BEARING. Applied to TEST through MCP `apply_migration`,
-- which records its OWN `schema_migrations` version rather than reading a
-- filename. TEST recorded 20260907211144, so this file carries it. It was
-- WRITTEN as 20260908000100 and renamed to match what TEST actually recorded —
-- renaming it back makes `supabase db push` re-apply the whole thing.
--
-- v1 (MRB-331) filed a teacher-set assignment against `source_sow_entry_id`:
-- the teacher picked a scheme row, and the row carried that scheme row's
-- `topic` and `subtopic` strings. v2 deletes that contract. A teacher now picks
-- a node of the CURRICULUM TREE — a KS4 topic or subtopic, a KS3 unit or
-- lesson — and a tier chosen per set rather than inherited from the class.
-- None of that has anywhere to live on `assignments` today, and inferring it
-- back out of `topic`/`subtopic` after the fact is exactly the guess this
-- ticket exists to stop.
--
-- ⚠️ EVERY COLUMN HERE IS NULLABLE, AND THAT IS NOT LAZINESS. Auto rows carry
-- none of them — 34 on TEST, 2 on production — and a NOT NULL would have to be
-- paid for with a backfilled lie about how those rows were made.

-- ── 1. `set_tier` — the tier THIS SET was drawn at ─────────────────────
--
-- Not `classes.tier`, and the difference is the ticket. The automatic producer
-- draws at the class's tier because it has nobody to ask; a teacher setting
-- Foundation revision inside a Higher class is asking for something the class
-- row cannot express. So the tier travels on the assignment, and the class row
-- keeps governing auto composition alone.
--
-- Five values, because the two key stages name difficulty differently and
-- always have: KS4 sets a TIER (the AQA one, a real entry decision), KS3 sets a
-- DIFFICULTY (easy/medium/hard, which maps onto the bank's
-- easier/standard/harder bands). Collapsing them into three shared values would
-- make a KS4 'medium' expressible, and there is no such thing.
alter table public.assignments
  add column if not exists set_tier text;

alter table public.assignments
  drop constraint if exists assignments_set_tier_check;
alter table public.assignments
  add constraint assignments_set_tier_check
  check (set_tier is null
         or set_tier in ('foundation', 'higher', 'easy', 'medium', 'hard'));

-- ── 2. `scope_kind` + `scope_ref` — WHAT was set, as the tree names it ─
--
-- `scope_kind` is 'topic' or 'subtopic' at BOTH key stages, deliberately: a KS3
-- unit is a topic and a KS3 lesson is a subtopic, and giving KS3 its own two
-- words would make every reader downstream branch on key stage to ask one
-- question.
--
-- `scope_ref` is the tree node's own id — a KS4 topic id (`energy-changes`), a
-- KS4 subtopic slug (`exothermic-and-endothermic`), a KS3 unit code (`B4`) or a
-- KS3 lesson slug (`the-gas-exchange-system`).
--
-- ⚠️ NOT A FOREIGN KEY, AND THERE IS NOTHING FOR IT TO REFERENCE. The
-- curriculum tree lives in the site repo's Python — `PATHWAY_TOPIC_MAP`,
-- `ks4_data.classify()`, `ks3_data` — and is mirrored to the backend as a JSON
-- file, not as tables. A text ref is honest about that. What keeps it from
-- rotting is that `scope_ref` is re-validated against the class's own tree at
-- write time, every time, and that slugs are permanent — by KS3's §8.4 and by
-- `classify()`'s uniqueness assertion at KS4.
alter table public.assignments
  add column if not exists scope_kind text;

alter table public.assignments
  drop constraint if exists assignments_scope_kind_check;
alter table public.assignments
  add constraint assignments_scope_kind_check
  check (scope_kind is null or scope_kind in ('topic', 'subtopic'));

alter table public.assignments
  add column if not exists scope_ref text;

-- ── 3. `subject` — the science, in the pool's own vocabulary ───────────
--
-- `subject_id` already exists and is NOT NULL, so this looks redundant and is
-- not. `subject_id` points at `public.subjects`, whose rows are a SCHOOL's
-- timetable subjects — 'Science', 'Biology', 'Combined Science' — and a KS3
-- assignment is filed under whatever the class is taught as. The pools speak a
-- different, fixed vocabulary: `ks4_assignment_bank.subject` and every KS3 unit
-- carry exactly 'biology' | 'chemistry' | 'physics'.
--
-- The sheet filters by that vocabulary, so the row has to carry it. Deriving it
-- from `subject_id` at read time would mean a school that names its subject
-- 'Combined Science' has assignments that belong to no science at all.
alter table public.assignments
  add column if not exists subject text;

alter table public.assignments
  drop constraint if exists assignments_subject_check;
alter table public.assignments
  add constraint assignments_subject_check
  check (subject is null or subject in ('biology', 'chemistry', 'physics'));

-- ── 4. `paper` — AQA paper 1 or 2, KS4 only ───────────────────────────
--
-- A KS4 topic sits on exactly one of the two papers, and "which paper is this
-- on" is the second question a Year 11 teacher asks after "which topic". The
-- map is a backend constant (`KS4_PAPER` in `set-work-scope.js`, from RISKS C8)
-- rather than a table, for the same reason `scope_ref` is not a foreign key:
-- the curriculum is authored in Python and mirrored, not stored.
--
-- NULL at KS3 always — KS3 has no papers — and NULL on every auto row.
alter table public.assignments
  add column if not exists paper smallint;

alter table public.assignments
  drop constraint if exists assignments_paper_check;
alter table public.assignments
  add constraint assignments_paper_check
  check (paper is null or paper in (1, 2));

comment on column public.assignments.set_tier is
  'The tier/difficulty THIS set was drawn at (MRB-335). KS4: foundation|higher. KS3: easy|medium|hard. NULL on every auto row — auto draws at classes.tier and records nothing.';
comment on column public.assignments.scope_kind is
  'topic | subtopic — which level of the curriculum tree the teacher chose. A KS3 unit is a topic; a KS3 lesson is a subtopic.';
comment on column public.assignments.scope_ref is
  'The chosen tree node: KS4 topic id or subtopic slug, KS3 unit code or lesson slug. Not a foreign key — the tree is authored in the site repo and mirrored as JSON. Re-validated against the class tree on every write.';
comment on column public.assignments.subject is
  'biology|chemistry|physics — the POOL''s vocabulary, not the school''s. subject_id points at the school timetable subject (''Science'', ''Combined Science''), which cannot answer which science this is.';
comment on column public.assignments.paper is
  'AQA paper 1 or 2 for a KS4 topic. NULL at KS3 and on every auto row.';

-- ── 5. Backfill: a NO-OP, and it is in the file for honesty ────────────
--
-- Measured before it was written (RISKS D6). Production holds ONE teacher-set
-- assignment — the 8r/Sc1 fixture of 18 August — and its `source_sow_entry_id`
-- is NULL, so there is no scheme row to derive a scope from. TEST holds seeded
-- teacher rows with no questions and the same NULL.
--
-- So there is nothing to migrate, and the honest statement of that is a guarded
-- UPDATE that touches zero rows rather than an absent section that leaves a
-- reader wondering whether backfill was considered. If it ever reports a
-- non-zero count, a v1 row with a real scheme row appeared after the
-- measurement and the derivation below needs looking at rather than trusting:
-- it copies the scheme row's `subtopic` in as a SUBTOPIC scope, which is right
-- for KS3 (where a scheme row is a lesson) and would need checking at KS4.
update public.assignments a
   set scope_kind = 'subtopic',
       scope_ref  = s.subtopic
  from public.scheme_of_work_entries s
 where a.source_sow_entry_id is not null
   and a.source_sow_entry_id = s.id
   and s.subtopic is not null
   and a.source = 'teacher'
   and a.scope_ref is null;
