-- ════════════════════════════════════════════════════════════════════════
-- MRB-351 — FLASHCARD HOMEWORK, PART 1 OF 3: THE TABLES AND THEIR RLS.
--
--   flashcard_decks          a teacher's authored deck (library row)
--   flashcard_cards          the cards in a deck (editable)
--   flashcard_extractions    one row per extraction job (progress + tokens)
--   assignment_flashcards    the FROZEN snapshot a flashcard assignment reads
--   flashcard_events         every raw pupil event, idempotent by client id
--   flashcard_sessions       one row per sitting
--   flashcard_pupil_cards    the answer a pupil wrote (make mode), immutable
--   flashcard_reviews        one row per rating
--
-- plus four columns on `assignments` (kind, deck_id, flashcard_mode,
-- completion_rule), a widened `quiz_type` CHECK, two new `ai_usage_events`
-- kinds, and the private `teacher-uploads` bucket.
--
-- WHY `assignments` GROWS RATHER THAN A PARALLEL TABLE
-- ====================================================
-- A flashcard homework IS an assignment: it has a class, a release, a
-- deadline, a teacher note, soft delete, a submission when it is done, and
-- it has to appear in the bell, the class list, the rollup and all six
-- teacher screens. Every one of those already reads `assignments`. A
-- parallel table would have meant teaching each of them about a second
-- kind of work; a `kind` column with a default means none of them has to
-- change to keep working, and the ones that must tell the two apart can.
--
-- `kind` DEFAULTS TO 'mcq_set', so every existing row, and every INSERT the
-- backend's automatic weekly composition makes (which names none of these
-- columns), lands exactly as it did before this migration.
--
-- `quiz_type` is NOT NULL with a CHECK. A flashcard row says so honestly —
-- 'flashcards' — rather than borrowing 'topic_quiz' and lying to any
-- reader that switches on it. The CHECK is widened, never narrowed.
--
-- THE RLS SHAPE (MRB-348)
-- =======================
-- One policy per (table, command). Cheapest branch first:
--   0  pupil_id = (select auth.uid())            -- a column and an InitPlan
--   1  request-constant scope checks, hoisted    -- evaluated once per query
--   2  EXISTS over class_teachers                -- an index probe, and
--      class_teachers' own SELECT policy opens on `teacher_id = auth.uid()`
--      first, so the probe needs no SECURITY DEFINER helper at all.
-- No policy body here calls a row-dependent SECURITY DEFINER function.
-- `school_id` and `class_id` are DENORMALISED onto every pupil table for
-- exactly that reason: the teacher branch can be answered from the row.
--
-- PUPILS NEVER WRITE THESE TABLES DIRECTLY. There is no INSERT/UPDATE/DELETE
-- policy for them on any pupil table: every pupil write goes through
-- `flashcard_record()` (part 2), which computes every duration server-side
-- from the event stream. A client that posts `think_ms: 5000` has nowhere
-- to post it.
--
-- REVERSIBLE: supabase/rollbacks/20260924180000_mrb351_flashcards_schema_rollback.sql
-- ════════════════════════════════════════════════════════════════════════

begin;

-- ── assignments: the four columns ──────────────────────────────────────
alter table public.assignments
  add column if not exists kind            text not null default 'mcq_set',
  add column if not exists deck_id         uuid,
  add column if not exists flashcard_mode  text,
  add column if not exists completion_rule text;

alter table public.assignments drop constraint if exists assignments_kind_check;
alter table public.assignments add constraint assignments_kind_check
  check (kind in ('mcq_set', 'flashcards'));

alter table public.assignments drop constraint if exists assignments_flashcard_mode_check;
alter table public.assignments add constraint assignments_flashcard_mode_check
  check (flashcard_mode is null or flashcard_mode in ('make', 'review'));

alter table public.assignments drop constraint if exists assignments_completion_rule_check;
alter table public.assignments add constraint assignments_completion_rule_check
  check (completion_rule is null or completion_rule in ('secure', 'quick'));

-- A flashcard row carries all three; an MCQ row carries none. Stated once,
-- here, so no reader has to wonder what a half-filled row means.
alter table public.assignments drop constraint if exists assignments_flashcard_shape;
alter table public.assignments add constraint assignments_flashcard_shape
  check (
    (kind = 'flashcards'
       and deck_id is not null and flashcard_mode is not null
       and completion_rule is not null and quiz_type = 'flashcards')
    or
    (kind = 'mcq_set'
       and deck_id is null and flashcard_mode is null
       and completion_rule is null and quiz_type <> 'flashcards')
  );

alter table public.assignments drop constraint if exists assignments_quiz_type_check;
alter table public.assignments add constraint assignments_quiz_type_check
  check (quiz_type = any (array['topic_quiz', 'subtopic_quiz', 'weekly_challenge', 'flashcards']));

create index if not exists assignments_kind_idx
  on public.assignments (class_id) where kind = 'flashcards' and deleted_at is null;

-- ── ai_usage_events: two more kinds ───────────────────────────────────
-- The existing usage log (MRB-315). `profile_id` is the TEACHER for both
-- kinds — the one who uploaded the file, or who set the assignment whose
-- answers were checked. A pupil's id is never written here.
alter table public.ai_usage_events
  add column if not exists assignment_id uuid,
  add column if not exists deck_id       uuid;
alter table public.ai_usage_events drop constraint if exists ai_usage_events_kind_check;
alter table public.ai_usage_events add constraint ai_usage_events_kind_check
  check (kind = any (array['tutor_turn', 'ai_mark', 'explain',
                           'flashcard_extract', 'flashcard_answer_check']));

-- ── flashcard_decks ───────────────────────────────────────────────────
create table if not exists public.flashcard_decks (
  id                 uuid primary key default gen_random_uuid(),
  school_id          uuid not null references public.schools(id),
  created_by         uuid not null references public.profiles(id),
  title              text not null check (char_length(btrim(title)) between 1 and 120),
  -- Curriculum tags, optional, from the existing trees — never free text.
  -- KS4: topic id / subtopic slug; KS3: unit code / lesson slug, exactly the
  -- vocabulary `assignments.scope_ref` already uses.
  key_stage          text check (key_stage is null or key_stage in ('KS3', 'KS4')),
  subject            text check (subject is null or subject in ('biology', 'chemistry', 'physics')),
  topic_id           text check (topic_id is null or topic_id ~ '^[a-z0-9][a-z0-9._-]{0,80}$'),
  subtopic_id        text check (subtopic_id is null or subtopic_id ~ '^[a-z0-9][a-z0-9._-]{0,120}$'),
  source_kind        text not null check (source_kind in ('upload', 'paste', 'typed')),
  source_file_path   text,
  source_file_name   text check (source_file_name is null or char_length(source_file_name) <= 200),
  source_file_sha256 text check (source_file_sha256 is null or source_file_sha256 ~ '^[0-9a-f]{64}$'),
  status             text not null default 'draft' check (status in ('draft', 'ready')),
  shared_with_school boolean not null default true,
  card_count         integer not null default 0,
  duplicated_from    uuid references public.flashcard_decks(id),
  created_at         timestamptz not null default now(),
  updated_at         timestamptz not null default now(),
  deleted_at         timestamptz
);
create index if not exists flashcard_decks_school_idx
  on public.flashcard_decks (school_id, updated_at desc) where deleted_at is null;
create index if not exists flashcard_decks_author_idx
  on public.flashcard_decks (created_by, updated_at desc);
create index if not exists flashcard_decks_sha_idx
  on public.flashcard_decks (school_id, source_file_sha256) where source_file_sha256 is not null;

alter table public.assignments drop constraint if exists assignments_deck_id_fkey;
alter table public.assignments add constraint assignments_deck_id_fkey
  foreign key (deck_id) references public.flashcard_decks(id);

-- ── flashcard_cards ───────────────────────────────────────────────────
-- A DRAFT card may have an empty answer (extraction found none) or an
-- empty question; `flashcard_deck_save(..., finalise => true)` refuses to
-- mark a deck ready while any card is empty. Formulae are stored FLAT.
create table if not exists public.flashcard_cards (
  id          uuid primary key default gen_random_uuid(),
  deck_id     uuid not null references public.flashcard_decks(id) on delete cascade,
  position    integer not null check (position >= 0),
  question    text not null default '' check (char_length(question) <= 400),
  answer      text not null default '' check (char_length(answer) <= 600),
  source_ref  text check (source_ref is null or char_length(source_ref) <= 40),
  confidence  real check (confidence is null or (confidence >= 0 and confidence <= 1)),
  flagged     boolean not null default false,
  created_at  timestamptz not null default now(),
  updated_at  timestamptz not null default now(),
  unique (deck_id, position) deferrable initially deferred
);

-- ── flashcard_extractions ─────────────────────────────────────────────
create table if not exists public.flashcard_extractions (
  id             uuid primary key default gen_random_uuid(),
  deck_id        uuid not null references public.flashcard_decks(id) on delete cascade,
  school_id      uuid not null references public.schools(id),
  created_by     uuid not null references public.profiles(id),
  status         text not null default 'queued'
                 check (status in ('queued', 'reading', 'asking', 'done', 'failed')),
  progress       smallint not null default 0 check (progress between 0 and 100),
  method         text check (method is null or method in ('table', 'lines', 'model', 'cache')),
  file_sha256    text,
  pairs_found    integer,
  needs_answer   integer,
  unpaired       jsonb,
  error          text,
  model          text,
  input_tokens   integer,
  output_tokens  integer,
  created_at     timestamptz not null default now(),
  updated_at     timestamptz not null default now()
);
create index if not exists flashcard_extractions_deck_idx
  on public.flashcard_extractions (deck_id, created_at desc);

-- ── assignment_flashcards: the frozen snapshot ────────────────────────
-- Written ONCE, when the assignment is created. Editing or deleting the deck
-- afterwards never reaches a live assignment: this is what pupils read.
create table if not exists public.assignment_flashcards (
  id             uuid primary key default gen_random_uuid(),
  assignment_id  uuid not null references public.assignments(id) on delete cascade,
  card_id        uuid references public.flashcard_cards(id) on delete set null,
  position       integer not null check (position >= 0),
  question       text not null check (char_length(btrim(question)) between 1 and 400),
  answer         text not null check (char_length(btrim(answer)) between 1 and 600),
  created_at     timestamptz not null default now(),
  unique (assignment_id, position)
);

-- ── the pupil tables ──────────────────────────────────────────────────
create table if not exists public.flashcard_sessions (
  id              uuid primary key default gen_random_uuid(),
  assignment_id   uuid not null references public.assignments(id),
  pupil_id        uuid not null references public.profiles(id),
  school_id       uuid not null references public.schools(id),
  class_id        uuid not null references public.classes(id),
  started_at      timestamptz not null default now(),   -- SERVER time
  last_seen_at    timestamptz not null default now(),   -- SERVER time
  ended_at        timestamptz,                          -- SERVER time
  active_ms       integer not null default 0,
  cards_seen      integer not null default 0,
  cards_rated     integer not null default 0,
  cards_made      integer not null default 0,
  median_think_ms integer,
  median_write_ms integer,
  rushed          boolean not null default false,
  finished        boolean not null default false        -- ended by "Finish for now"
);
create index if not exists flashcard_sessions_pupil_idx
  on public.flashcard_sessions (assignment_id, pupil_id, started_at);
create index if not exists flashcard_sessions_class_idx
  on public.flashcard_sessions (class_id);

create table if not exists public.flashcard_events (
  id             uuid primary key,                      -- CLIENT-generated: idempotency
  assignment_id  uuid not null references public.assignments(id),
  pupil_id       uuid not null references public.profiles(id),
  school_id      uuid not null references public.schools(id),
  class_id       uuid not null references public.classes(id),
  session_id     uuid not null references public.flashcard_sessions(id),
  card_id        uuid references public.assignment_flashcards(id),
  type           text not null check (type in ('card_shown', 'answer_submitted', 'revealed',
                                               'rated', 'session_finish', 'visibility')),
  client_at      timestamptz not null,
  server_at      timestamptz not null default now(),
  visible        boolean not null default true,
  phase          text check (phase is null or phase in ('make', 'review')),
  rating         text check (rating is null or rating in ('got_it', 'nearly', 'not_yet'))
);
create index if not exists flashcard_events_session_idx
  on public.flashcard_events (session_id, client_at);
create index if not exists flashcard_events_pupil_idx
  on public.flashcard_events (assignment_id, pupil_id, client_at);
create index if not exists flashcard_events_class_idx
  on public.flashcard_events (class_id);

create table if not exists public.flashcard_pupil_cards (
  id             uuid primary key default gen_random_uuid(),
  assignment_id  uuid not null references public.assignments(id),
  pupil_id       uuid not null references public.profiles(id),
  school_id      uuid not null references public.schools(id),
  class_id       uuid not null references public.classes(id),
  card_id        uuid not null references public.assignment_flashcards(id),
  session_id     uuid not null references public.flashcard_sessions(id),
  event_id       uuid not null references public.flashcard_events(id),
  pupil_answer   text not null check (char_length(pupil_answer) <= 500),
  written_ms     integer not null check (written_ms >= 0),
  answer_check   text not null default 'pending'
                 check (answer_check in ('match', 'partial', 'no', 'blank', 'pending')),
  check_claimed_at timestamptz,
  checked_at     timestamptz,
  created_at     timestamptz not null default now(),
  unique (assignment_id, pupil_id, card_id)
);
create index if not exists flashcard_pupil_cards_class_idx
  on public.flashcard_pupil_cards (class_id);
create index if not exists flashcard_pupil_cards_pending_idx
  on public.flashcard_pupil_cards (assignment_id, session_id) where answer_check = 'pending';

create table if not exists public.flashcard_reviews (
  id             uuid primary key default gen_random_uuid(),
  session_id     uuid not null references public.flashcard_sessions(id),
  assignment_id  uuid not null references public.assignments(id),
  pupil_id       uuid not null references public.profiles(id),
  school_id      uuid not null references public.schools(id),
  class_id       uuid not null references public.classes(id),
  card_id        uuid not null references public.assignment_flashcards(id),
  event_id       uuid not null unique references public.flashcard_events(id),
  rating         text not null check (rating in ('got_it', 'nearly', 'not_yet')),
  phase          text not null check (phase in ('make', 'review')),
  shown_at       timestamptz,
  revealed_at    timestamptz,
  rated_at       timestamptz not null,
  think_ms       integer check (think_ms is null or (think_ms between 0 and 180000))
);
create index if not exists flashcard_reviews_pupil_idx
  on public.flashcard_reviews (assignment_id, pupil_id, card_id);
create index if not exists flashcard_reviews_class_idx
  on public.flashcard_reviews (class_id);

-- ── updated_at + card_count bookkeeping ───────────────────────────────
create or replace function public.mrb351_touch_updated_at()
returns trigger language plpgsql set search_path to 'public' as $$
begin
  new.updated_at := now();
  return new;
end $$;

drop trigger if exists flashcard_decks_touch on public.flashcard_decks;
create trigger flashcard_decks_touch before update on public.flashcard_decks
  for each row execute function public.mrb351_touch_updated_at();
drop trigger if exists flashcard_cards_touch on public.flashcard_cards;
create trigger flashcard_cards_touch before update on public.flashcard_cards
  for each row execute function public.mrb351_touch_updated_at();
drop trigger if exists flashcard_extractions_touch on public.flashcard_extractions;
create trigger flashcard_extractions_touch before update on public.flashcard_extractions
  for each row execute function public.mrb351_touch_updated_at();

create or replace function public.mrb351_deck_card_count()
returns trigger language plpgsql security definer set search_path to 'public' as $$
declare v_deck uuid := coalesce(new.deck_id, old.deck_id);
begin
  update public.flashcard_decks d
     set card_count = (select count(*) from public.flashcard_cards c where c.deck_id = v_deck)
   where d.id = v_deck;
  return null;
end $$;
revoke all on function public.mrb351_deck_card_count() from public, anon, authenticated;

drop trigger if exists flashcard_cards_count on public.flashcard_cards;
create trigger flashcard_cards_count after insert or delete on public.flashcard_cards
  for each row execute function public.mrb351_deck_card_count();

-- ── RLS ────────────────────────────────────────────────────────────────
alter table public.flashcard_decks       enable row level security;
alter table public.flashcard_cards       enable row level security;
alter table public.flashcard_extractions enable row level security;
alter table public.assignment_flashcards enable row level security;
alter table public.flashcard_sessions    enable row level security;
alter table public.flashcard_events      enable row level security;
alter table public.flashcard_pupil_cards enable row level security;
alter table public.flashcard_reviews     enable row level security;

-- decks. The author sees their own (including soft-deleted ones, so the
-- library can grey a deleted deck that is still in use); a colleague sees a
-- live deck shared with the school; a school admin sees every live deck in
-- the school. Pupils see none — they read the snapshot, never the deck.
drop policy if exists flashcard_decks_select on public.flashcard_decks;
create policy flashcard_decks_select on public.flashcard_decks for select using (
  created_by = (select auth.uid())
  or (deleted_at is null
      and school_id = (select public.auth_user_school_id())
      and (shared_with_school or (select public.auth_user_has_scope('school_admin'))))
);
drop policy if exists flashcard_decks_insert on public.flashcard_decks;
create policy flashcard_decks_insert on public.flashcard_decks for insert with check (
  created_by = (select auth.uid())
  and school_id = (select public.auth_user_school_id())
  and (select public.auth_user_role()) is distinct from 'student'
);
drop policy if exists flashcard_decks_update on public.flashcard_decks;
create policy flashcard_decks_update on public.flashcard_decks for update using (
  created_by = (select auth.uid())
  or (school_id = (select public.auth_user_school_id())
      and (select public.auth_user_has_scope('school_admin')))
) with check (
  created_by = (select auth.uid())
  or (school_id = (select public.auth_user_school_id())
      and (select public.auth_user_has_scope('school_admin')))
);
-- No DELETE policy: decks are soft-deleted (`deleted_at`), never removed.

-- cards follow their deck. The EXISTS reads flashcard_decks under ITS OWN
-- policy, so "can see the card" is exactly "can see the deck".
drop policy if exists flashcard_cards_select on public.flashcard_cards;
create policy flashcard_cards_select on public.flashcard_cards for select using (
  exists (select 1 from public.flashcard_decks d where d.id = flashcard_cards.deck_id)
);
drop policy if exists flashcard_cards_insert on public.flashcard_cards;
create policy flashcard_cards_insert on public.flashcard_cards for insert with check (
  exists (select 1 from public.flashcard_decks d
           where d.id = flashcard_cards.deck_id and d.created_by = (select auth.uid()))
);
drop policy if exists flashcard_cards_update on public.flashcard_cards;
create policy flashcard_cards_update on public.flashcard_cards for update using (
  exists (select 1 from public.flashcard_decks d
           where d.id = flashcard_cards.deck_id and d.created_by = (select auth.uid()))
) with check (
  exists (select 1 from public.flashcard_decks d
           where d.id = flashcard_cards.deck_id and d.created_by = (select auth.uid()))
);
drop policy if exists flashcard_cards_delete on public.flashcard_cards;
create policy flashcard_cards_delete on public.flashcard_cards for delete using (
  exists (select 1 from public.flashcard_decks d
           where d.id = flashcard_cards.deck_id and d.created_by = (select auth.uid()))
);

-- extraction jobs: the teacher who started one polls it. Written by the
-- edge function under the service role only.
drop policy if exists flashcard_extractions_select on public.flashcard_extractions;
create policy flashcard_extractions_select on public.flashcard_extractions for select using (
  created_by = (select auth.uid())
);

-- the snapshot: visible exactly when its assignment is. `assignments`' own
-- policy already says who that is — a released, live assignment to a pupil
-- of the class; any assignment to its teachers; the school's admin and SLT —
-- so repeating it here would be a second copy of one rule.
drop policy if exists assignment_flashcards_select on public.assignment_flashcards;
create policy assignment_flashcards_select on public.assignment_flashcards for select using (
  exists (select 1 from public.assignments a where a.id = assignment_flashcards.assignment_id)
);

-- The four pupil tables share one SELECT shape: the pupil's own rows; the
-- school's admin/SLT; a teacher of the row's class.
drop policy if exists flashcard_sessions_select on public.flashcard_sessions;
create policy flashcard_sessions_select on public.flashcard_sessions for select using (
  pupil_id = (select auth.uid())
  or (school_id = (select public.auth_user_school_id())
      and ((select public.auth_user_has_scope('school_admin'))
           or (select public.auth_user_has_scope('slt'))))
  or exists (select 1 from public.class_teachers ct
              where ct.class_id = flashcard_sessions.class_id
                and ct.teacher_id = (select auth.uid())
                and ct.ended_at is null and ct.deleted_at is null)
);
drop policy if exists flashcard_events_select on public.flashcard_events;
create policy flashcard_events_select on public.flashcard_events for select using (
  pupil_id = (select auth.uid())
  or (school_id = (select public.auth_user_school_id())
      and ((select public.auth_user_has_scope('school_admin'))
           or (select public.auth_user_has_scope('slt'))))
  or exists (select 1 from public.class_teachers ct
              where ct.class_id = flashcard_events.class_id
                and ct.teacher_id = (select auth.uid())
                and ct.ended_at is null and ct.deleted_at is null)
);
drop policy if exists flashcard_pupil_cards_select on public.flashcard_pupil_cards;
create policy flashcard_pupil_cards_select on public.flashcard_pupil_cards for select using (
  pupil_id = (select auth.uid())
  or (school_id = (select public.auth_user_school_id())
      and ((select public.auth_user_has_scope('school_admin'))
           or (select public.auth_user_has_scope('slt'))))
  or exists (select 1 from public.class_teachers ct
              where ct.class_id = flashcard_pupil_cards.class_id
                and ct.teacher_id = (select auth.uid())
                and ct.ended_at is null and ct.deleted_at is null)
);
drop policy if exists flashcard_reviews_select on public.flashcard_reviews;
create policy flashcard_reviews_select on public.flashcard_reviews for select using (
  pupil_id = (select auth.uid())
  or (school_id = (select public.auth_user_school_id())
      and ((select public.auth_user_has_scope('school_admin'))
           or (select public.auth_user_has_scope('slt'))))
  or exists (select 1 from public.class_teachers ct
              where ct.class_id = flashcard_reviews.class_id
                and ct.teacher_id = (select auth.uid())
                and ct.ended_at is null and ct.deleted_at is null)
);

-- anon reads nothing: every policy above needs auth.uid() or a school, and
-- anon has neither. Belt and braces:
revoke all on public.flashcard_decks, public.flashcard_cards, public.flashcard_extractions,
              public.assignment_flashcards, public.flashcard_sessions, public.flashcard_events,
              public.flashcard_pupil_cards, public.flashcard_reviews
  from anon;
-- Pupil tables are written ONLY by flashcard_record() (SECURITY DEFINER).
revoke insert, update, delete on public.flashcard_sessions, public.flashcard_events,
              public.flashcard_pupil_cards, public.flashcard_reviews,
              public.assignment_flashcards, public.flashcard_extractions
  from authenticated;

-- ── storage: the private upload bucket ────────────────────────────────
-- 25 MB, private, written by the edge function under the service role and
-- read back by the uploading school's staff (to re-run extraction). Never
-- readable by a pupil. Path: school/<school_id>/flashcards/<deck_id>/<sha256>.<ext>
insert into storage.buckets (id, name, public, file_size_limit, allowed_mime_types)
values ('teacher-uploads', 'teacher-uploads', false, 26214400, array[
  'application/vnd.openxmlformats-officedocument.presentationml.presentation',
  'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
  'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
  'application/pdf', 'text/csv', 'text/plain', 'text/markdown',
  'image/png', 'image/jpeg', 'image/heic', 'image/webp'])
on conflict (id) do update set public = false, file_size_limit = excluded.file_size_limit,
  allowed_mime_types = excluded.allowed_mime_types;

drop policy if exists teacher_uploads_staff_read on storage.objects;
create policy teacher_uploads_staff_read on storage.objects for select to authenticated using (
  bucket_id = 'teacher-uploads'
  and (storage.foldername(name))[1] = 'school'
  and (storage.foldername(name))[2] = (select public.auth_user_school_id())::text
  and (select public.auth_user_role()) is distinct from 'student'
);

commit;
