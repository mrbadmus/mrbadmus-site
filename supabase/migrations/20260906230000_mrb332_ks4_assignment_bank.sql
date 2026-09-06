-- MRB-332 — the KS4 assignment question pool.
--
-- ── WHY ITS OWN TABLE ──────────────────────────────────────────────────
--
-- One pool per surface is the standing law (MRB-288). This is the KS4
-- weekly-assignment pool, and it is the ONLY thing a KS4 assignment is
-- composed from. In particular it is NOT the lesson pages' "Test yourself"
-- questions: those are baked into a page a child can open whenever they
-- like, so serving one as homework publishes the answers in advance.
--
-- It is a SEPARATE TABLE rather than a `key_stage` column on
-- `ks3_assignment_bank`, and that is the whole point of the design.
-- `ks3_assignment_bank` is joined on `lesson_slug` alone. Eight KS4 subtopic
-- slugs are byte-identical to KS3 lesson slugs —
--
--     aerobic-respiration, catalysts, changes-of-state, chromatography,
--     conservation-of-mass, distance-time-graphs, electric-fields,
--     magnetic-fields
--
-- — and each returns twelve KS3 rows to a KS4 lookup: real science, correct,
-- and three years too easy, with nothing anywhere saying so. MRB-331 held
-- that off with `bankFor(keyStage)`, a guard that works only while every
-- future call site remembers to pass the right argument. Two tables end the
-- collision structurally, which is the only way it stays ended.
--
-- ── THE CONTENT RULE (standing, ruled by Mide) ─────────────────────────
--
--     tier='foundation', triple_only=false → BASE. Every class.
--     tier='higher',     triple_only=false → Higher tier only.
--     triple_only=true                     → Triple Science only.
--
-- ⚠️ A Foundation Combined class must NEVER be served a higher or a
-- triple_only question. A Triple Higher class gets all three sets. The
-- filter lives in the composition read (`bankFor`), and the flags are set
-- here from the site's own curriculum data — see `ks4_data/__init__.py`,
-- `classify()`. Nothing hand-types a flag.
--
-- ── THIS TABLE IS A BUILD ARTEFACT ─────────────────────────────────────
--
-- `ks4_data/questions/**.py` is the source. `export_ks4_questions.py` is the
-- only writer, and it is idempotent. Nothing here may be hand-edited in the
-- database: the next export would silently revert it, which is the worst way
-- to lose a correction.

create table if not exists public.ks4_assignment_bank (
  id            text primary key,            -- 'ks4-temperature-changes-shc-e01'
  subtopic_slug text     not null,           -- the KS4 scheme key — joins to
                                             -- scheme_of_work_entries.subtopic
  subject       text     not null check (subject in ('biology', 'chemistry',
                                                     'physics')),
  band          text     not null check (band in ('easier', 'standard',
                                                  'harder')),
  -- 'foundation' means BASE — content every class may be asked, Foundation
  -- Combined included. 'higher' means higher-only. It is NOT a label for
  -- "which tier is sitting this question", which is the reading that would
  -- let a Foundation class be served a Higher one.
  tier          text     not null check (tier in ('foundation', 'higher')),
  triple_only   boolean  not null default false,
  text          text     not null,
  -- Exactly four options, as plain strings, and the answer is an INDEX into
  -- them. ⚠️ This is deliberately NOT the KS3 shape ([{text, correct, why}]).
  -- text[] rather than jsonb so the database itself can insist there are four
  -- of them and that none is null — a three-option question that renders as
  -- four is invisible until a student meets it.
  options       text[]   not null,
  correct_index smallint not null check (correct_index between 0 and 3),
  -- One line on why the CORRECT answer is correct. Unlike KS3's bank there is
  -- no per-distractor `why` here; MRB-332 specified this shape.
  why           text     not null,
  bank_position smallint not null,           -- 0..11 within the subtopic
  created_at    timestamptz default now(),
  updated_at    timestamptz default now(),

  constraint ks4_assignment_bank_four_options check (
    array_length(options, 1) = 4
    and array_position(options, null) is null
  )
);

comment on table public.ks4_assignment_bank is
  'MRB-332. The KS4 weekly-assignment question pool — the only pool a KS4 '
  'assignment is composed from. A BUILD ARTEFACT: ks4_data/questions/**.py is '
  'the source and export_ks4_questions.py is the only writer. Separate from '
  'ks3_assignment_bank on purpose: eight subtopic slugs collide across the '
  'key stages and the two tables end that structurally.';

comment on column public.ks4_assignment_bank.tier is
  'foundation = BASE content, servable to every class including Foundation '
  'Combined. higher = higher-tier only. Read with triple_only.';

comment on column public.ks4_assignment_bank.triple_only is
  'true = Triple Science only. A Combined class must never be served one.';

-- The composition read path: given a class''s subtopic slugs and a band, take
-- questions in bank order. tier and triple_only are in the index because the
-- content rule filters on them on every single read.
create index if not exists ks4_assignment_bank_serving_idx
  on public.ks4_assignment_bank
     (subtopic_slug, band, tier, triple_only, bank_position);

-- The answer-position gate and the per-subject export both sweep by subject.
create index if not exists ks4_assignment_bank_subject_idx
  on public.ks4_assignment_bank (subject, subtopic_slug, bank_position);

alter table public.ks4_assignment_bank enable row level security;

-- Reference content, identical for every student. Readable by anyone signed
-- in; only the service role — the exporter and the backend's composition —
-- writes. Mirrors ks3_assignment_bank_read exactly.
drop policy if exists ks4_assignment_bank_read on public.ks4_assignment_bank;
create policy ks4_assignment_bank_read on public.ks4_assignment_bank
  for select to authenticated using (true);
