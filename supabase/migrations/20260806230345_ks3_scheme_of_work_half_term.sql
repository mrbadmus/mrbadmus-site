-- ═══════════════════════════════════════════════════════════════════════
-- KS3 — give scheme_of_work_entries a half term to put the lesson in.
--
-- The table already answers "which year, which week". It cannot answer
-- "which half term", and that is the grain a department actually plans at:
-- nobody writes a scheme of work in years, and nobody asks "what am I
-- teaching in week 23?" — they ask what comes back after October half term.
--
-- ⚠️ This is METADATA, and architecture.md §4.5 governs it exactly as it
-- governs year_group:
--
--     "year and sequence are metadata, never structure"
--
-- Half term inherits the whole of that prohibition. It must never reach a
-- URL, a folder, a page byte or a content branch. It exists to be written
-- here and read back by a teacher. The generator side is
-- `ks3_data/half_terms.py`, whose placement is DERIVED from the default
-- sequence rather than authored, and `verify_ks3.py` proves that adding it
-- changed zero lesson-page bytes.
--
-- ── Why nullable, and why KS3 rows are NOT forced to carry one ──────────
--
-- The obvious constraint — mirroring scheme_of_work_entries_ks3_has_no_board
-- exactly, so that half_term is NOT NULL whenever key_stage = 'KS3' — would
-- fail on apply. KS3 rows already exist (the default-sequence seed), and every
-- one of them has half_term IS NULL until the seed is re-run. A migration that
-- cannot be applied to the database it is written for is not a stricter
-- migration, it is a broken one.
--
-- More importantly it would be wrong even on an empty table. A scheme-of-work
-- row is meaningful without a half term: the year and the teaching order are
-- the load-bearing facts, and half term is the refinement on top. Forcing it
-- would mean a school could not record a partial scheme, which is what a real
-- school has in September.
--
-- So the rule enforced here is the half that IS unconditionally true:
--
--     half_term is a KS3 concept. A non-KS3 row must not carry one.
--
-- That mirrors the DIRECTION of the exam_board constraint (a column that
-- belongs to one key stage is NULL in the other) without importing its
-- NOT NULL half, which the data cannot satisfy. If KS3 rows should later be
-- required to carry a half term, that is a second migration written after the
-- seed has backfilled them — and it will be a one-line CHECK at that point.
--
-- KS4 keeps its own answer to "when": academic_week against an exam board's
-- specification. It has no half-term concept and gains none here.
--
-- Safe to run against a table holding KS4 rows AND existing KS3 rows: the new
-- column is NULL on every existing row, and NULL satisfies both constraints.
-- ═══════════════════════════════════════════════════════════════════════

begin;

alter table public.scheme_of_work_entries
  add column if not exists half_term smallint;

-- Six half terms in an English school year. Not a magic number: it is the
-- number of teaching blocks between the fixed holidays, and it is the number
-- ks3_data/half_terms.py splits each discipline's year into.
alter table public.scheme_of_work_entries
  add constraint scheme_of_work_entries_half_term_range
  check (half_term is null or half_term between 1 and 6);

-- The domain rule, stated once, in the database — the same move
-- scheme_of_work_entries_ks3_has_no_board makes for exam_board, in the
-- opposite direction. KS3 owns half_term; KS4 must leave it NULL.
alter table public.scheme_of_work_entries
  add constraint scheme_of_work_entries_half_term_is_ks3_only
  check (
    key_stage = 'KS3'
    or half_term is null
  );

comment on column public.scheme_of_work_entries.half_term is
  'Which of the six half terms of the school year this lesson falls in (KS3 '
  'only; NULL on KS4 rows). Advisory metadata exactly as year_group is — '
  'architecture.md §4.5 forbids it determining any URL, page or content '
  'branch. Populated by ks3_seed_sow.py from ks3_data/half_terms.py, which '
  'derives it from the published default sequence rather than authoring it.';

comment on constraint scheme_of_work_entries_half_term_is_ks3_only
  on public.scheme_of_work_entries is
  'Deliberately one-sided: a non-KS3 row must not carry a half term, but a KS3 '
  'row is not forced to. Existing KS3 rows predate the column, and a partial '
  'scheme of work is a real thing a school has in September.';

commit;
