-- ════════════════════════════════════════════════════════════════════════
-- MRB-348 ROUND THREE — public.teacher_class_rollup(uuid[], timestamptz, jsonb)
--
-- Everything the six teacher screens draw about a class they are not
-- FOCUSED on, computed in SQL: the six summary numbers, one row per
-- ASSIGNMENT, and one row per ACTIVE MEMBER.
--
-- It supersedes `public.teacher_class_summaries(uuid[])`
-- (20260922114500), which this migration DROPS. See "WHY THE OLDER
-- FUNCTION IS DROPPED RATHER THAN KEPT" below.
-- ════════════════════════════════════════════════════════════════════════
--
-- WHAT THIS REPLACES
-- ==================
-- `loadClassMatrices()` in `shared/teacher-data.js` is the universal read
-- behind all six generated teacher screens. Stage B of it fetches EVERY
-- submission of EVERY assignment of EVERY class the viewer touches — no
-- limit, no window — and `buildMatrix()` in `shared/teacher-live.js` then
-- counts them in the browser. On the realistic TEST teacher that is 79
-- submission rows; five classes x forty assignments x thirty pupils is
-- about six thousand, on every screen, to draw a card that says
-- "4 of 6 in · last activity 2 days ago · mean 73%".
--
-- The cost is a PRODUCT: members x assignments. What the screens actually
-- read off it is two SUMS: a number per assignment (the column) and a
-- number per pupil (the row). This function returns the two sums.
--
-- ⚠️ WHY THE ROUND-TWO FUNCTION WAS NOT ENOUGH, which is the whole reason
-- this one exists. `teacher_class_summaries` covered six values —
-- roster size, assignment count, submissions handed in, completion %,
-- class mean, last activity. All six teacher screens share ONE compiled
-- `renderVals` that also computes, unconditionally and for EVERY class:
--
--     week[0] / week[1]   this teaching week's submitted-of-roster, drawn
--                         on every class card
--     colSub / colAsked / colMean / colOnTime / colLate / colLateUnknown
--                         the per-paper columns, which the digest sums
--                         into dgMarkedSub / dgOnTime / dgLate / dgUnknown
--                         and the class report reads paper by paper
--     roster[].avg        every pupil's average — the search pool across
--                         all classes reads it on every screen
--     roster[].inWeek     who has handed this week's work in (the card's
--                         "Chase Amy, Ben +3 more")
--     roster[].flag       Design's "needs a look" rule, which the digest
--                         counts per class
--     roster[].lastIso    the card's "Last activity 2 days ago"
--
-- Ship the six alone and every one of those degrades silently to
-- 0 / null / "No activity yet". So the aggregate had to grow to the shape
-- the RENDER needs, not the shape a card's headline numbers need.
--
-- WHY THE OLDER FUNCTION IS DROPPED RATHER THAN KEPT
-- ==================================================
-- Its six numbers are reproduced here verbatim — the same first-attempt
-- pick, the same predicates, the same rounding — so keeping it would mean
-- TWO SQL implementations of one locked rule that must agree for ever, on
-- top of the JavaScript they must both agree with. That is exactly the
-- drift its own header warns about. It was rehearsed on TEST and has never
-- been applied to production, and nothing in the repo calls it: dropping
-- it costs nothing and removes a second answer.
--
-- ⚠️ BOTH MIGRATIONS MUST BE APPLIED TO PRODUCTION, IN ORDER. This one
-- does not recreate the older function; it drops it. Applying this file
-- alone against a database that never took 20260922114500 is harmless
-- (`DROP ... IF EXISTS`).
--
-- ⚠️ IT IS A SECOND IMPLEMENTATION OF A LOCKED RULE, AND THAT IS THE RISK
-- THIS HEADER EXISTS TO NAME. The first-attempt rule (MRB-38, Mide,
-- 9 May 2026) has two implementations that must agree for ever: the
-- JavaScript `pickFirstAttempts()` and the `DISTINCT ON` below. They are
-- written to be read side by side:
--
--     JS                                     SQL
--     lower `attempts` wins                  COALESCE(attempts, 2147483647) ASC
--     tiebreak: earlier submitted_at         COALESCE(submitted_at,'infinity') ASC
--     NULL attempts is worst                 2147483647
--     NULL submitted_at is worst in a tie    'infinity'
--
-- ⚠️ A FULL TIE IS NOT DEFINED BY EITHER SIDE. Two live rows for one
-- (assignment, student) with the SAME `attempts` and the SAME
-- `submitted_at` are separated by the JS only by PostgREST's return order,
-- which is unspecified. `s.id ASC` is added here so THIS side is at least
-- deterministic; it is a tiebreak for an anomaly, not a rule.
--
-- THE THREE PREDICATES THAT ARE EASY TO CONFLATE, AND ARE NOT THE SAME
-- ===================================================================
--   1. `submissions_completed` (the class card's count, from
--      `deriveClassMetrics`) is `submitted_at IS NOT NULL`. Nothing else.
--   2. A CELL — what every column and every pupil row is built from,
--      `cellOf()` in teacher-live.js — exists when
--      `completed_at IS NOT NULL OR submitted_at IS NOT NULL OR
--       status = 'complete'`. It is GRADED, and so counts toward a mean,
--      only when `score IS NOT NULL AND max_score IS NOT NULL AND
--      max_score > 0`. A row with `completed_at` and no `submitted_at` is
--      a cell and is NOT in (1). A submitted-but-ungraded row is in (1)
--      and is a cell but is not in any mean.
--   3. `marked` means ONLY "the deadline has passed" — `buildPapers`'
--      `open = !due_at || due_at > now`. Not released, not sat, not
--      graded. An assignment with no `due_at` never closes and is never
--      marked.
--
-- LATENESS IS A TRI-STATE, AND THE THIRD STATE IS THE POINT
-- ========================================================
-- `cellOf`: the stamp first (`is_late` as written at completion), the
-- comparison second (`stamp > due_at`, where the stamp is
-- `COALESCE(completed_at, submitted_at)`), and UNKNOWN third. `is_late`
-- was added on 22 Aug 2026 and nothing was backfilled, so every older row
-- carries NULL; a submission with no stamp, or an assignment with no
-- deadline, cannot be judged either way. `on_time`, `late` and `unknown`
-- are returned as three separate counts so the caller cannot quietly
-- absorb the third into either of the other two — which is what
-- `MRB_ONTIME_SUB` on the page is about.
--
-- WHAT IS DELIBERATELY *NOT* RETURNED
-- ===================================
-- The cells themselves. A pupil's mark on a particular paper, the stamp
-- on it, and the submission id written feedback binds to are read ONLY on
-- the class, marking and student screens, and only for the ONE class in
-- focus — which keeps its full submission read (`opts.submissionsFor` in
-- `loadClassMatrices`). This function answers the counting question the
-- OTHER classes ask, and nothing more. It cannot be used to draw a grid,
-- and it must not be extended into one: at that point it is the product
-- again, and the product is what was wrong.
--
-- THE CLOCK AND THE WEEK WINDOW ARE THE CALLER'S, ON PURPOSE
-- =========================================================
-- `p_now` and `p_windows` exist because the page's own definitions of
-- "now" and "this teaching week" are the BROWSER's, and this function's
-- job is to reproduce what that browser would have computed.
--
--   · `p_now` — `buildPapers` decides `marked` against `Date.now()` taken
--     once in `base()`. A server `now()` a few hundred milliseconds later
--     can flip an assignment whose deadline falls inside that window, and
--     the two halves of one screen would then disagree. NULL falls back to
--     `now()`.
--   · `p_windows` — `computeWeekWindow()` in teacher-data.js is the ONE
--     definition of the teaching week on this side of the wire, and it is
--     computed in BROWSER-LOCAL time from the CLASS's own anchor day, with
--     MRB-330's Sunday rule (Sunday belongs to the week that is coming).
--     Four implementations of that rule already have to agree (CLAUDE.md);
--     a fifth, in SQL, would be the fifth. So the window is PASSED IN:
--     `{"<class id>": {"start": "…", "end": "…"}}`. A class with no window
--     supplied gets `in_week = false` for every pupil, which is what the
--     page draws for a class with no work due this week anyway.
--
-- ⚠️ NEITHER PARAMETER IS A TRUST BOUNDARY. Both only ever re-bucket rows
-- the caller's own RLS already grants them: a caller who lies about the
-- clock changes their own arithmetic and sees nothing new. The gate below
-- is what decides WHICH rows, and it takes no parameters at all.
--
-- ⚠️ float8 THEN numeric, ON PURPOSE. `round(((a::float8 / b::float8) *
-- 100)::numeric)` reproduces JavaScript's `Math.round(a / b * 100)`
-- exactly: the same IEEE double division, then half-away-from-zero
-- rounding (which equals `Math.round` for non-negative values). Rounding
-- the float8 directly would use Postgres's banker's rounding and disagree
-- on every exact `.5`; doing the division in `numeric` would disagree
-- wherever the double lands a hair under a `.5`.
--
-- SECURITY
-- ========
-- SECURITY DEFINER with `SET search_path TO 'public'`, gated INTERNALLY as
-- its first statement, in the shape `class_teachers_for_viewer` and
-- `class_stars_leaderboard_for_member` both use. A class id the caller may
-- not see is DROPPED SILENTLY rather than raising — a rollup is asked
-- speculatively over a remembered id list, and an error would take the
-- whole page down over one stale id. (`loadClassMatrices` still THROWS,
-- deliberately: it is a page's authorisation check.)
--
-- ⚠️ THE GATE IS NOT ONE PREDICATE, BECAUSE THE FOUR TABLES' RLS IS NOT
-- ONE PREDICATE, and getting that wrong would make this function return
-- numbers no reader could have computed for themselves:
--
--   classes / class_members    operator | school+(school_admin|slt) |
--                              school+hod | school+teaches
--   assignments / submissions  operator | school+(school_admin|slt) |
--                              school+HOD **OF THAT SUBJECT'S DEPARTMENT** |
--                              school+teaches
--
-- So a plain HoD sees every class in the school and every MEMBER of it,
-- but only the assignments — and therefore only the submissions — of their
-- own department. `all_work` below is exactly that distinction.
--
-- ⚠️ THE STUDENT ARMS ARE DELIBERATELY NOT REPRODUCED. `class_members` and
-- `assignment_submissions` both also grant `student_id = auth_user_id()`.
-- This is a teacher aggregate; a pupil calling it gets the class dropped
-- by the gate and no rows back. That is a NARROWING of what RLS would
-- allow them, never a widening, and no student surface calls it.
-- ════════════════════════════════════════════════════════════════════════

DROP FUNCTION IF EXISTS public.teacher_class_summaries(uuid[]);

CREATE OR REPLACE FUNCTION public.teacher_class_rollup(
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
    SELECT a.id, a.class_id, a.due_at
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
           s.submitted_at, s.completed_at, s.status, s.is_late
      FROM assignment_submissions s
      JOIN asg ON asg.id = s.assignment_id
     WHERE s.deleted_at IS NULL
     ORDER BY s.assignment_id, s.student_id,
              COALESCE(s.attempts, 2147483647) ASC,
              COALESCE(s.submitted_at, 'infinity'::timestamptz) ASC,
              s.id ASC
  ),
  -- The card's own count and stamp. `submitted_at IS NOT NULL`, over every
  -- first attempt — cells have nothing to do with it (predicate 1 above).
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
            AND fa.max_score > 0)                     AS graded,
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
  -- ── ONE ROW PER ASSIGNMENT: the column ────────────────────────────────
  -- `off_roster` rather than `asked`: the page adds it to
  -- `pack.members.length`, so the roster stays defined in exactly one
  -- place (`colAsked = members + offRoster`, the 24 Aug 2026 ruling that
  -- stopped a column reading "31 of 29").
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
           (a.due_at IS NOT NULL AND a.due_at <= v_now)                AS marked
      FROM asg a
      LEFT JOIN cells c   ON c.assignment_id = a.id
      LEFT JOIN active act ON act.class_id = a.class_id
                          AND act.student_id = c.student_id
     GROUP BY a.class_id, a.id, a.due_at
  ),
  per_paper_mean AS (
    SELECT pp.*,
           CASE WHEN pp.totmax > 0
                THEN round((((pp.tot)::float8 / (pp.totmax)::float8) * 100)::numeric)::int
                ELSE NULL
           END AS mean
      FROM per_paper pp
  ),
  -- The class mean: the mean OF THE MARKED COLUMN MEANS (Design's README
  -- pins it that way, so the digest's "mean of N class means" is a mean of
  -- things that are themselves means). A column contributes only when
  -- something in it is graded.
  cmean AS (
    SELECT ppm.class_id,
           round(((SUM(ppm.mean))::float8 / (COUNT(*))::float8)::numeric)::int AS class_mean
      FROM per_paper_mean ppm
     WHERE ppm.marked AND ppm.mean IS NOT NULL
     GROUP BY ppm.class_id
  ),
  marked_count AS (
    SELECT pp.class_id, COUNT(*)::int AS n
      FROM per_paper pp WHERE pp.marked GROUP BY pp.class_id
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
           COALESCE(bool_or(c.assignment_id IS NOT NULL
                            AND cls.week_start IS NOT NULL
                            AND c.due_at IS NOT NULL
                            AND c.due_at >  cls.week_start
                            AND c.due_at <= cls.week_end), false)      AS in_week,
           MAX(c.stamp)                                                AS last_at,
           COALESCE(SUM(c.score)     FILTER (WHERE c.graded AND pmk.marked), 0) AS tot,
           COALESCE(SUM(c.max_score) FILTER (WHERE c.graded AND pmk.marked), 0) AS totmax,
           COUNT(*) FILTER (WHERE c.student_id IS NOT NULL AND pmk.marked)::int AS marked_cells
      FROM active act
      JOIN cls ON cls.id = act.class_id
      LEFT JOIN cells c ON c.class_id = act.class_id
                       AND c.student_id = act.student_id
      LEFT JOIN per_paper pmk ON pmk.assignment_id = c.assignment_id
     GROUP BY act.class_id, act.student_id
  ),
  student_rows AS (
    SELECT ps.class_id,
           jsonb_agg(jsonb_build_object(
             'student_id',     ps.student_id,
             'in_week',        ps.in_week,
             'last_at',        ps.last_at,
             'avg',            CASE WHEN ps.totmax > 0
                                    THEN round((((ps.tot)::float8
                                                 / (ps.totmax)::float8) * 100)::numeric)::int
                                    ELSE NULL END,
             -- `mx.markedIdx.some(i => !row.submitted[i])` — a marked paper
             -- this pupil has no cell for. NOT "no mark": an ungraded
             -- submission is submitted.
             'missing_marked', (COALESCE(mc.n, 0) > ps.marked_cells)
           ) ORDER BY ps.student_id) AS rows
      FROM per_student ps
      LEFT JOIN marked_count mc ON mc.class_id = ps.class_id
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

COMMENT ON FUNCTION public.teacher_class_rollup(uuid[], timestamptz, jsonb) IS
  'MRB-348 round three. Per-class summary, per-assignment columns and '
  'per-pupil rows for the teacher screens, computed in SQL under the '
  'first-attempt rule (MRB-38) so the browser stops fetching every '
  'submission of every assignment of every class. Supersedes '
  'teacher_class_summaries. The clock and the teaching-week window are the '
  'CALLER''s, because the page''s are the browser''s; the gate takes no '
  'parameters and unreadable class ids are dropped silently.';
