-- ════════════════════════════════════════════════════════════════════════
-- MRB-351 — FLASHCARD HOMEWORK, PART 3 OF 3: teacher_class_rollup LEARNS `kind`.
--
-- ONE CHANGE to the MRB-348 round-three function, and nothing else: a cell of
-- a `kind = 'flashcards'` assignment is never GRADED. Everything else about
-- it is exactly an MCQ cell's — it is a cell, it counts in `sub`, `on_time`,
-- `late`, `unknown`, `off_roster`, `submissions_completed`, `last_activity_at`,
-- `in_week` and `missing_marked` — because a finished flashcard set IS handed
-- in and a missing one IS missing.
--
-- WHY. `flashcard_record()` writes the existing submission record when the
-- completion rule is met, with score = cards secured / total, which is N/N by
-- construction (MRB-351 §1). Left graded, every finished deck would add a 100%
-- to the class mean, the column mean and every pupil's average: a class that
-- set one quiz (mean 54%) and one deck would read 77%. That number describes
-- nothing a teacher can act on. So `marked_n`, `mean`, `tot`/`totmax`,
-- `class_mean` and `avg` leave flashcards out; the JavaScript twin
-- (`cellOf` in shared/teacher-live.js) changes in the same commit, so the two
-- implementations of the rule still agree (the MRB-348 header's warning).
--
-- The rest of this body is byte-for-byte 20260922231500's.
--
-- REVERSIBLE: supabase/rollbacks/20260924180200_mrb351_rollup_kind_rollback.sql
--   re-creates the 20260922231500 body.
-- ════════════════════════════════════════════════════════════════════════

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
    SELECT a.id, a.class_id, a.due_at, a.kind
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
            AND fa.max_score > 0
            -- ⊕ MRB-351: a finished flashcard set is handed in, on time or
            -- late, like any other work — but its "N of N" is a completion
            -- stamp, not a mark, so it never enters a mean or an average.
            AND asg.kind <> 'flashcards')             AS graded,
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
