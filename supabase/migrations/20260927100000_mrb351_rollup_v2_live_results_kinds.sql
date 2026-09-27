-- ════════════════════════════════════════════════════════════════════════
-- MRB-351 landing, stream B, 27 Sep 2026 — public.teacher_class_rollup_v2
-- (uuid[], timestamptz, jsonb) — LIVE RESULTS + THE FLASHCARD KIND SPLIT
--
-- SUPERSEDES, AND MUST NOT BE APPLIED ALONGSIDE:
--   supabase/migrations/20260924180200_mrb351_rollup_kind.sql
--     (md5 c738d1b85583dc4eb557b066e28b02b4) — edited teacher_class_rollup
--     (v1) in place to add the flashcard kind carve-out described below.
--     Retired: v1 is left EXACTLY as production has it (this file never
--     touches it), and the carve-out it added is folded into v2 instead, so
--     v2 alone carries both the live-results ruling AND the kind split.
--   branch feat/rollup-live-results, commit b734f03ba,
--     supabase/migrations/20260924010000_rollup_live_results.sql
--     (md5 112d63fbb9440bd8faca02c0efffff41) — created v2 with the live-
--     results ruling but with NO flashcard awareness at all (production had
--     no `assignments.kind` column when it was written). This file is that
--     one PLUS the kind split; do not apply both, and do not use that one's
--     rollback (md5 603adc26fe27eaa98668cbee409dcef7) — this file's own
--     rollback (below) supersedes it, dropping the SAME single function.
--
-- WHY ONE FILE AND NOT TWO. TEST briefly held D's v2 (no kind awareness) and
-- v1 with an UN-MIGRATED, TEST-only kind carve-out (`docs/experience/
-- REPORT.md`'s "found while rehearsing" note) — two different rollup
-- functions disagreeing about flashcards, neither of them what will exist on
-- production the day both MRB-348 round three and MRB-351 have landed. This
-- migration is what SHOULD exist once both have: v2's live-results
-- semantics, v1 untouched, and the kind split living in v2 only.
--
-- A NEW function beside `public.teacher_class_rollup` (20260922231500),
-- unchanged from D's original design in every other respect. Same
-- signature, same shape, same security model — this migration does not
-- touch the old function at all, because production DDL could not change in
-- that run and a green build must not regress the estate onto a function
-- that does not exist yet. `shared/teacher-data.js`'s `loadClassSummaries`
-- calls `_v2` and falls back to the full submissions read for EVERY class
-- when it is absent (`PGRST202` / `42883`), so the estate is CORRECT
-- (slower) until the chat applies this migration and WRONG never, either
-- side of that moment.
--
-- ⚠️ WHY A NEW FUNCTION AND NOT AN EDIT TO THE OLD ONE, STATED ONCE. Mide's
-- 23 Sep 2026 ruling changes what "marked" MEANS on every teacher screen —
-- "results update live as pupils complete work; the deadline only decides
-- who is missing or late, never whether finished work is visible" — which
-- is a correctness change, not a tuning change, and it must ship on the JS
-- side (`shared/teacher-live.js`) the same day it ships here or the two
-- halves of one screen disagree with each other. This run cannot apply DDL
-- to production, so the JS ships behind a NEW RPC name and the old function
-- is untouched until the migration lands. See CLAUDE.md's "when a
-- migration may touch production" rule.
--
-- THE DEFINITIONS THIS FUNCTION CHANGES, AGAINST v1
-- ==================================================
--   marked   (was) a.due_at IS NOT NULL AND a.due_at <= v_now   — CLOSED.
--            (now) a.release_at IS NULL OR a.release_at <= v_now — RELEASED.
--            Kept the COLUMN NAME `marked` in `per_paper`/`cmean` for the
--            same reason `shared/teacher-live.js` keeps the KEY `when ===
--            'marked'`: it is the population every average and every
--            "released work" reader already selects on, and renaming it
--            would be a second migration for no behavioural gain. Every
--            downstream user of `marked` (the class mean, the per-pupil
--            average, `marked_n`/`marked_count`-shaped counts) INHERITS the
--            new population automatically, exactly as the JS's `markedIdx`
--            does from the one-line change to `buildPapers`.
--   closed   NEW. a.due_at IS NOT NULL AND a.due_at <= v_now — the genuine
--            deadline test v1's `marked` used to BE. `shared/teacher-
--            live.js`'s `paper.closed` / `mx.closedIdx` is its JS twin.
--   in_week  (was) due_at falls inside the caller's week window.
--            (now) (marked AND NOT closed) OR (due_at falls inside the
--            window) — an OPEN paper is "this week's homework" the instant
--            it is released, whether or not its due date happens to land
--            in the window; a CLOSED paper still counts if its due date
--            does. Mirrors `buildMatrix`'s `inWeekPaper` in
--            shared/teacher-live.js exactly (item 5 of the ruling).
--   on_time_week  NEW. bool_or, per pupil: a cell with `late = false` on an
--            in-week paper (using the SAME in-week test as `in_week`
--            above). The SQL twin of `buildMatrix`'s new `onTimeWeek`,
--            which "Select all on time this week" reads.
--   missing_marked  UNCHANGED IN MEANING, RE-EXPRESSED ON `closed`. It was
--            already "a paper whose deadline has passed, with no cell" —
--            correct by the coincidence that v1's `marked` WAS the deadline
--            test. Spelled on the new, separate `closed` column so it does
--            not silently start asking about released-but-still-open work
--            the moment `marked`'s meaning moves under it.
--   graded   NEW population rule, folded in from MRB-351 (20260924180200).
--            (was, in D's v2) fa.score/max_score present and max_score > 0.
--            (now) the same, AND asg.kind <> 'flashcards'. A flashcard
--            assignment's completion write is score = max_score = N — a
--            completion stamp, not a mark (MRB-351 §1) — so it is a CELL
--            (counted in sub/on_time/late/unknown/off_roster/
--            submissions_completed/last_activity_at/in_week/missing_marked,
--            exactly like an MCQ cell) but never GRADED (never in marked_n,
--            mean, tot/totmax, class_mean or a pupil's avg). Left graded, a
--            class with one MCQ set (mean 54%) and one finished flashcard
--            deck would read 77% — a number describing nothing a teacher
--            can act on. Requires `assignments.kind` (MRB-351 migration 1);
--            this migration must apply AFTER migrations 1 and 2. Identical
--            predicate to the JS twin, `cellOf`'s `graded = !(paper &&
--            paper.kind === "flashcards")` in shared/teacher-live.js — the
--            two must never be allowed to drift (the MRB-348 header's
--            warning, restated for the third implementation of this rule).
--
-- ⊕ 27 Sep 2026 (Opus review of this migration, before it ever shipped) —
-- TWO MORE FIXES TO THE PER-PUPIL `last_at`, FOLDED IN HERE RATHER THAN A
-- SEPARATE MIGRATION, because the first draft above had not caught up with
-- either of them yet:
--   1. `last_at` WAS `MAX(c.stamp)` — CELLS ONLY. Mide's 25 Sep 2026 ruling
--      (experience run, item 7, landed on `feat/mrb351-landing` at commit
--      `c2fde3a12`) changed `buildRoster`'s `lastIso` to read
--      `row.activity[]` instead of `row.stamp[]`: a pupil mid-way through an
--      open paper (`started_at` set, no `completed_at` yet) has NO cell
--      (`cellOf` returns null for one) and was invisible to `stamp`, so a
--      pupil who answered yesterday and had not yet pressed Finish read as
--      "No activity yet". Fixed by the new `activity` CTE below: for every
--      first attempt, activity is the cell's stamp when it IS one, or
--      `started_at` when it is not (yet) one — line for line, `activity[p]`
--      in `shared/teacher-live.js`.
--   2. A FLASHCARD SITTING WROTE NO ACTIVITY AT ALL. A deck writes no
--      `assignment_submissions` row until every card is secured (MRB-351
--      §1), so a pupil several sittings into an unfinished deck had no
--      `first_attempts` row and no activity either — worse than the MCQ
--      case above, because there is no eventual "in progress" submission
--      row to fall back to. Fixed by the new `flashcard_activity` CTE,
--      folding in `MAX(flashcard_sessions.last_seen_at)` over the class's
--      released flashcard assignments. Full rule (for the JS twin) under
--      "The last-activity rule" in `supabase/MRB351-APPLY.md`, MRB-351
--      landing.
-- Both feed `last_at` via `GREATEST()`, in `per_student` below.
--
-- Everything else — the roster count, the first-attempt rule, the tri-state
-- lateness, the departed-student column handling, the internal RLS gate,
-- the float8-then-numeric rounding, the security model — is copied from
-- 20260922231500 UNCHANGED. Read that file's header for the reasoning;
-- restating it here would be a second copy to keep in sync.
-- ════════════════════════════════════════════════════════════════════════
CREATE OR REPLACE FUNCTION public.teacher_class_rollup_v2(
  p_class_ids uuid[],
  p_now       timestamptz DEFAULT NULL,
  p_windows   jsonb       DEFAULT NULL
)
RETURNS TABLE (
  class_id uuid,
  summary  jsonb,
  papers   jsonb,
  students jsonb
)
LANGUAGE plpgsql
STABLE SECURITY DEFINER
SET search_path TO 'public'
SET "TimeZone" TO 'UTC'
AS $function$
DECLARE
  v_school   uuid;
  v_operator boolean;
  v_wide     boolean;   -- school_admin OR slt
  v_hod      boolean;
  v_now      timestamptz := COALESCE(p_now, now());
BEGIN
  IF p_class_ids IS NULL OR array_length(p_class_ids, 1) IS NULL THEN
    RETURN;
  END IF;

  v_school   := auth_user_school_id();
  v_operator := auth_user_operator_active();
  v_wide     := auth_user_has_scope('school_admin') OR auth_user_has_scope('slt');
  v_hod      := auth_user_has_scope('hod');

  RETURN QUERY
  WITH asked AS (
    SELECT DISTINCT unnest(p_class_ids) AS id
  ),
  visible AS (
    SELECT c.id,
           (v_operator
             OR (c.school_id = v_school
                 AND (v_wide OR v_hod OR auth_user_teaches_class(c.id))))  AS can_see,
           (v_operator
             OR (c.school_id = v_school
                 AND (v_wide OR auth_user_teaches_class(c.id))))           AS all_work
      FROM classes c
      JOIN asked a ON a.id = c.id
     WHERE c.deleted_at IS NULL
  ),
  cls AS (
    SELECT v.id, v.all_work,
           -- The class's own teaching-week window, as the BROWSER computed
           -- it. Absent → no pupil is "in this week", which is the same
           -- thing the page draws for a class with nothing due.
           (p_windows -> v.id::text ->> 'start')::timestamptz AS week_start,
           (p_windows -> v.id::text ->> 'end')::timestamptz   AS week_end
      FROM visible v
     WHERE v.can_see
  ),
  -- ONE ROW PER `class_members` ROW, not per pupil: `pack.members.length`
  -- on the page counts rows, and there is no unique index on
  -- (class_id, student_id). The roster size below must count the same
  -- thing the browser counts, even where that is a duplicate.
  mem_rows AS (
    SELECT cm.class_id, cm.student_id
      FROM class_members cm
      JOIN cls ON cls.id = cm.class_id
      JOIN profiles p ON p.id = cm.student_id
     WHERE cm.deleted_at IS NULL
       AND cm.left_at   IS NULL
       AND p.deleted_at IS NULL
  ),
  mem AS (
    SELECT mr.class_id, COUNT(*)::int AS n FROM mem_rows mr GROUP BY mr.class_id
  ),
  -- Who is ON THE ROLL, for "is this submission a departed pupil's".
  active AS (
    SELECT DISTINCT mr.class_id, mr.student_id FROM mem_rows mr
  ),
  asg AS (
    SELECT a.id, a.class_id, a.due_at, a.release_at, a.kind
      FROM assignments a
      JOIN cls ON cls.id = a.class_id
     WHERE a.deleted_at IS NULL
       AND (cls.all_work
            OR (v_hod AND auth_user_is_hod_of_subject_dept(a.subject_id)))
  ),
  acount AS (
    SELECT asg.class_id, COUNT(*)::int AS n FROM asg GROUP BY asg.class_id
  ),
  first_attempts AS (
    SELECT DISTINCT ON (s.assignment_id, s.student_id)
           s.assignment_id, s.student_id, s.score, s.max_score,
           s.submitted_at, s.completed_at, s.status, s.is_late, s.started_at
      FROM assignment_submissions s
      JOIN asg ON asg.id = s.assignment_id
     WHERE s.deleted_at IS NULL
     ORDER BY s.assignment_id, s.student_id,
              COALESCE(s.attempts, 2147483647) ASC,
              COALESCE(s.submitted_at, 'infinity'::timestamptz) ASC,
              s.id ASC
  ),
  -- The card's own count and stamp. `submitted_at IS NOT NULL`, over every
  -- first attempt — cells have nothing to do with it.
  handed AS (
    SELECT asg.class_id,
           COUNT(*) FILTER (WHERE fa.submitted_at IS NOT NULL)::int AS n,
           MAX(fa.submitted_at)                                     AS last_at
      FROM asg
      JOIN first_attempts fa ON fa.assignment_id = asg.id
     GROUP BY asg.class_id
  ),
  -- ── EVERY CELL, EXACTLY AS `cellOf` MAKES ONE ─────────────────────────
  cells AS (
    SELECT asg.class_id,
           asg.id   AS assignment_id,
           asg.due_at,
           fa.student_id,
           COALESCE(fa.completed_at, fa.submitted_at) AS stamp,
           fa.score, fa.max_score,
           (fa.score     IS NOT NULL
            AND fa.max_score IS NOT NULL
            AND fa.max_score > 0
            -- ⊕ MRB-351 — a finished flashcard set is handed in, on time or
            -- late, like any other work — but its "N of N" is a completion
            -- stamp, not a mark, so it never enters a mean or an average.
            -- This is the CURRENT statement of the rule this file's header
            -- describes at length; the same predicate lived briefly in
            -- teacher_class_rollup's own kind carve-out
            -- (20260924180200_mrb351_rollup_kind.sql, retired — see the
            -- header above), and lives on today in the JS twin `cellOf`'s
            -- `graded = !(paper && paper.kind === "flashcards")` in
            -- shared/teacher-live.js. The two (this file and the JS) must
            -- never be allowed to drift from each other.
            AND asg.kind <> 'flashcards')                AS graded,
           CASE
             WHEN fa.is_late IS NOT NULL THEN fa.is_late
             WHEN COALESCE(fa.completed_at, fa.submitted_at) IS NOT NULL
                  AND asg.due_at IS NOT NULL
               THEN COALESCE(fa.completed_at, fa.submitted_at) > asg.due_at
             ELSE NULL
           END                                        AS late
      FROM asg
      JOIN first_attempts fa ON fa.assignment_id = asg.id
     WHERE fa.completed_at IS NOT NULL
        OR fa.submitted_at IS NOT NULL
        OR fa.status = 'complete'
  ),
  -- ⊕ MRB-351 landing, stream B, follow-up (Opus review, 27 Sep 2026) —
  -- PER-PUPIL "LAST ACTIVE" IS WIDER THAN "LAST CELL". Mide's 25 Sep 2026
  -- ruling (experience run, item 7) made `buildRoster`'s `lastIso` read
  -- `row.activity[]`, not `row.stamp[]`: a pupil mid-way through an open
  -- paper (`started_at` set at the first answer, no `completed_at` yet) was
  -- invisible to `stamp`, because `cellOf` returns null for a row that is
  -- not yet a cell. `activity[p]` in shared/teacher-live.js is `c.stamp`
  -- when the row IS a cell, or `mine[p].started_at` when a first-attempt row
  -- exists but is NOT (yet) one — exactly the CASE below, over every first
  -- attempt rather than only the ones `cells` (above) keeps. One row per
  -- (class, pupil): pre-aggregated here, before `per_student` joins it, so
  -- the join stays one-to-one and cannot fan out the SUMs/COUNTs already
  -- computed against `cells` in that CTE.
  activity AS (
    SELECT asg.class_id,
           fa.student_id,
           MAX(
             CASE
               WHEN fa.completed_at IS NOT NULL OR fa.submitted_at IS NOT NULL
                    OR fa.status = 'complete'
                 THEN COALESCE(fa.completed_at, fa.submitted_at)
               ELSE fa.started_at
             END
           ) AS last_activity_at
      FROM asg
      JOIN first_attempts fa ON fa.assignment_id = asg.id
     GROUP BY asg.class_id, fa.student_id
  ),
  -- ⊕ MRB-351 landing, stream B, follow-up (Opus review, 27 Sep 2026) — A
  -- FLASHCARD SITTING IS ACTIVITY TOO, EVEN BEFORE THE DECK IS FINISHED. A
  -- deck writes NO `assignment_submissions` row until every card is secured
  -- (MRB-351 §1), so a pupil three sittings into a deck they have not yet
  -- finished has no `first_attempts` row at all and would otherwise read
  -- "No activity yet". `flashcard_sessions.last_seen_at` is kept current on
  -- every batch `flashcard_record` processes (including the one that ends a
  -- sitting), so it is the honest "were they here, and when" instant for a
  -- deck exactly as `started_at` is for an in-progress MCQ attempt above.
  -- Scoped to this class's own NON-DELETED, RELEASED flashcard assignments —
  -- the same population `asg`/`cells` already restrict to (a pupil's
  -- sessions on a class they have since left, or a deleted assignment,
  -- should not surface here either) — and to `kind = 'flashcards'` for
  -- clarity, though `flashcard_sessions` rows only ever exist for one.
  -- Written up in full, for the JS twin, under "The last-activity rule" in
  -- `supabase/MRB351-APPLY.md`.
  flashcard_activity AS (
    SELECT asg.class_id,
           fs.pupil_id AS student_id,
           MAX(fs.last_seen_at) AS last_activity_at
      FROM flashcard_sessions fs
      JOIN asg ON asg.id = fs.assignment_id
     WHERE asg.kind = 'flashcards'
       AND (asg.release_at IS NULL OR asg.release_at <= v_now)
     GROUP BY asg.class_id, fs.pupil_id
  ),
  -- ── ONE ROW PER ASSIGNMENT: the column ────────────────────────────────
  -- `off_roster` rather than `asked`: the page adds it to
  -- `pack.members.length`, so the roster stays defined in exactly one
  -- place (`colAsked = members + offRoster`, the 24 Aug 2026 ruling that
  -- stopped a column reading "31 of 29").
  --
  -- ⊕ 23 Sep 2026 ruling — `marked` IS RELEASED, `closed` IS THE OLD
  -- `marked`. See the file header. A NULL `release_at` is released (the
  -- MRB-336 rule, unchanged): automatic weekly work and every row written
  -- before Set work existed carry no release instant and are out, and
  -- always were.
  per_paper AS (
    SELECT a.class_id,
           a.id                                                        AS assignment_id,
           COUNT(c.student_id)::int                                    AS sub,
           COUNT(*) FILTER (WHERE c.late IS TRUE)::int                 AS late_n,
           COUNT(*) FILTER (WHERE c.late IS FALSE)::int                AS on_time,
           COUNT(*) FILTER (WHERE c.student_id IS NOT NULL
                              AND c.late IS NULL)::int                 AS unknown,
           COUNT(*) FILTER (WHERE c.graded)::int                       AS marked_n,
           COUNT(*) FILTER (WHERE c.student_id IS NOT NULL
                              AND act.student_id IS NULL)::int         AS off_roster,
           COALESCE(SUM(c.score)     FILTER (WHERE c.graded), 0)       AS tot,
           COALESCE(SUM(c.max_score) FILTER (WHERE c.graded), 0)       AS totmax,
           (a.release_at IS NULL OR a.release_at <= v_now)             AS marked,
           (a.due_at IS NOT NULL AND a.due_at <= v_now)                AS closed
      FROM asg a
      LEFT JOIN cells c   ON c.assignment_id = a.id
      LEFT JOIN active act ON act.class_id = a.class_id
                          AND act.student_id = c.student_id
     GROUP BY a.class_id, a.id, a.due_at, a.release_at
  ),
  per_paper_mean AS (
    SELECT pp.*,
           CASE WHEN pp.totmax > 0
                THEN round((((pp.tot)::float8 / (pp.totmax)::float8) * 100)::numeric)::int
                ELSE NULL
           END AS mean
      FROM per_paper pp
  ),
  -- The class mean: the mean OF THE RELEASED COLUMN MEANS (item 6 of the
  -- ruling — Design's README pins it as a mean of means, so the digest's
  -- "mean of N class means" is a mean of things that are themselves means).
  -- A column contributes only when something in it is graded. `ppm.marked`
  -- is RELEASED now, not closed — an open paper with a graded cell already
  -- counts, which is the entire point of "results are live".
  cmean AS (
    SELECT ppm.class_id,
           round(((SUM(ppm.mean))::float8 / (COUNT(*))::float8)::numeric)::int AS class_mean
      FROM per_paper_mean ppm
     WHERE ppm.marked AND ppm.mean IS NOT NULL
     GROUP BY ppm.class_id
  ),
  -- ⊕ 23 Sep 2026 ruling — RENAMED FROM `marked_count`, AND RE-BASED ON
  -- `closed`. This is `missing_marked`'s denominator, and `missing_marked`
  -- means "a CLOSED paper with no cell" (item 2) — the genuine deadline
  -- test, which moved to `closed` when `marked` stopped being it.
  closed_count AS (
    SELECT pp.class_id, COUNT(*)::int AS n
      FROM per_paper pp WHERE pp.closed GROUP BY pp.class_id
  ),
  -- ── ONE ROW PER ACTIVE PUPIL: the row ─────────────────────────────────
  per_student AS (
    SELECT act.class_id,
           act.student_id,
           -- ⚠️ `>` AND `<=`, WHERE THE PAGE READS `>=` AND `<`, AND THAT
           -- IS NOT A TYPO. `buildMatrix` tests
           -- `p.due_at >= pack.week.start_at && p.due_at < pack.week.end_at`
           -- as STRINGS: `due_at` arrives from PostgREST as
           -- `…T23:00:00+00:00` and the window from `Date.toISOString()` as
           -- `…T23:00:00.000Z`. Lexicographic order IS chronological order
           -- for those two forms everywhere EXCEPT an exact tie to the
           -- second, where `'+'` (0x2B) sorts before `'.'` (0x2E) — so a
           -- deadline landing exactly ON the window's start is EXCLUDED by
           -- the page and one landing exactly on its end is INCLUDED. A
           -- class anchored on Monday has a window that starts at local
           -- midnight, which is precisely where a round `due_at` falls, so
           -- this is a real boundary and not a theoretical one. Half-open
           -- the other way round is what reproduces the browser.
           --
           -- ⊕ 23 Sep 2026 ruling, item 5 — AN OPEN PAPER IS "IN WEEK" TOO,
           -- REGARDLESS OF WHERE ITS DUE DATE FALLS. `pmk.marked AND NOT
           -- pmk.closed` is `state === 'open'` in `shared/teacher-live.js`
           -- terms: released, not yet due. OR'd onto the existing
           -- due-date-in-window test, which is kept exactly as it was for a
           -- paper that has closed but whose due date still falls in this
           -- window. Mirrors `buildMatrix`'s `inWeekPaper` exactly.
           COALESCE(bool_or(
             c.assignment_id IS NOT NULL
             AND (
               (pmk.marked AND NOT pmk.closed)
               OR (cls.week_start IS NOT NULL
                   AND c.due_at IS NOT NULL
                   AND c.due_at >  cls.week_start
                   AND c.due_at <= cls.week_end)
             )
           ), false)                                                   AS in_week,
           -- ⊕ 23 Sep 2026 ruling, item 5 — NEW. "On time this week": a cell
           -- with `late = false` on an in-week paper, the SAME in-week test
           -- as `in_week` above. The SQL twin of `buildMatrix`'s
           -- `onTimeWeek`, which "Select all on time this week" reads.
           COALESCE(bool_or(
             c.assignment_id IS NOT NULL
             AND c.late IS FALSE
             AND (
               (pmk.marked AND NOT pmk.closed)
               OR (cls.week_start IS NOT NULL
                   AND c.due_at IS NOT NULL
                   AND c.due_at >  cls.week_start
                   AND c.due_at <= cls.week_end)
             )
           ), false)                                                   AS on_time_week,
           -- ⊕ Opus review, 27 Sep 2026 — was `MAX(c.stamp)`, cells only.
           -- `act_last`/`fc_last` are ALREADY one row per (class, pupil)
           -- (pre-aggregated above), so this join is one-to-one and cannot
           -- fan out `tot`/`totmax`/`closed_cells` below; MAX() here is
           -- belt-and-braces (GREATEST already collapses the pair), not a
           -- sign the join fans out. GREATEST ignores a NULL side; both NULL
           -- gives NULL, exactly "no activity of either kind yet".
           MAX(GREATEST(act_last.last_activity_at, fc_last.last_activity_at)) AS last_at,
           -- Item 6 — a pupil's average is sum(score)/sum(max) over cells
           -- on RELEASED papers. `pmk.marked` IS released now, so this is
           -- unchanged text with a changed population underneath it.
           COALESCE(SUM(c.score)     FILTER (WHERE c.graded AND pmk.marked), 0) AS tot,
           COALESCE(SUM(c.max_score) FILTER (WHERE c.graded AND pmk.marked), 0) AS totmax,
           -- ⊕ 23 Sep 2026 ruling — RENAMED FROM `marked_cells`, RE-BASED ON
           -- `pmk.closed`. `missing_marked` below means "a CLOSED paper
           -- with no cell" — NOT "no mark": an ungraded submission is still
           -- a cell, so this counts CELLS (any complete submission),
           -- exactly as `row.submitted[i]` does in `buildRoster`.
           COUNT(*) FILTER (WHERE c.student_id IS NOT NULL AND pmk.closed)::int AS closed_cells
      FROM active act
      JOIN cls ON cls.id = act.class_id
      LEFT JOIN cells c ON c.class_id = act.class_id
                       AND c.student_id = act.student_id
      LEFT JOIN per_paper pmk ON pmk.assignment_id = c.assignment_id
      LEFT JOIN activity act_last ON act_last.class_id = act.class_id
                                  AND act_last.student_id = act.student_id
      LEFT JOIN flashcard_activity fc_last ON fc_last.class_id = act.class_id
                                           AND fc_last.student_id = act.student_id
     GROUP BY act.class_id, act.student_id
  ),
  student_rows AS (
    SELECT ps.class_id,
           jsonb_agg(jsonb_build_object(
             'student_id',     ps.student_id,
             'in_week',        ps.in_week,
             'on_time_week',   ps.on_time_week,
             'last_at',        ps.last_at,
             'avg',            CASE WHEN ps.totmax > 0
                                    THEN round((((ps.tot)::float8
                                                 / (ps.totmax)::float8) * 100)::numeric)::int
                                    ELSE NULL END,
             -- `mx.closedIdx.some(i => !row.submitted[i])` — a CLOSED
             -- paper this pupil has no cell for. NOT "no mark": an
             -- ungraded submission is submitted.
             'missing_marked', (COALESCE(cc.n, 0) > ps.closed_cells)
           ) ORDER BY ps.student_id) AS rows
      FROM per_student ps
      LEFT JOIN closed_count cc ON cc.class_id = ps.class_id
     GROUP BY ps.class_id
  ),
  paper_rows AS (
    SELECT ppm.class_id,
           jsonb_agg(jsonb_build_object(
             'assignment_id', ppm.assignment_id,
             'sub',           ppm.sub,
             'off_roster',    ppm.off_roster,
             'on_time',       ppm.on_time,
             'late',          ppm.late_n,
             'unknown',       ppm.unknown,
             'marked_n',      ppm.marked_n,
             'mean',          ppm.mean
           ) ORDER BY ppm.assignment_id) AS rows
      FROM per_paper_mean ppm
     GROUP BY ppm.class_id
  )
  SELECT cls.id,
         jsonb_build_object(
           'active_member_count',   COALESCE(mem.n, 0),
           'assignment_count',      COALESCE(acount.n, 0),
           'submissions_completed', COALESCE(handed.n, 0),
           'completion_pct',        CASE
             WHEN COALESCE(mem.n, 0) * COALESCE(acount.n, 0) = 0 THEN NULL
             ELSE round(((COALESCE(handed.n, 0))::float8
                         / ((mem.n * acount.n))::float8 * 100)::numeric)::int
           END,
           'class_mean',            cmean.class_mean,
           'last_activity_at',      handed.last_at
         ),
         COALESCE(paper_rows.rows,   '[]'::jsonb),
         COALESCE(student_rows.rows, '[]'::jsonb)
    FROM cls
    LEFT JOIN mem          ON mem.class_id          = cls.id
    LEFT JOIN acount       ON acount.class_id       = cls.id
    LEFT JOIN handed       ON handed.class_id       = cls.id
    LEFT JOIN cmean        ON cmean.class_id        = cls.id
    LEFT JOIN paper_rows   ON paper_rows.class_id   = cls.id
    LEFT JOIN student_rows ON student_rows.class_id = cls.id;
END;
$function$;

COMMENT ON FUNCTION public.teacher_class_rollup_v2(uuid[], timestamptz, jsonb) IS
  'MRB-351 landing, stream B (27 Sep 2026), on Mide''s 23 Sep 2026 '
  '"results are live" ruling. Same shape as teacher_class_rollup (MRB-348 '
  'round three), with marked := released (not closed), a new closed '
  'column carrying the old deadline test, in_week widened to include an '
  'open paper regardless of its due date, a per-pupil on_time_week, and '
  'the MRB-351 flashcard kind split folded in (a flashcard cell counts '
  'everywhere an MCQ cell does except marked_n/mean/class_mean/avg — '
  'never graded). Per-pupil last_at (Opus review, 27 Sep 2026) is activity, '
  'not just a completed cell: an in-progress first attempt contributes its '
  'started_at, and a flashcard sitting contributes its own '
  'flashcard_sessions.last_seen_at, even before the deck is finished. '
  'Supersedes 20260924180200_mrb351_rollup_kind.sql (which edited v1) and '
  'the ungraded-of-kind 20260924010000_rollup_live_results.sql on '
  'feat/rollup-live-results. Sits beside teacher_class_rollup without '
  'replacing it; the clock and the teaching-week window are the CALLER''s, '
  'and the gate takes no parameters — unreadable class ids are dropped '
  'silently.';
