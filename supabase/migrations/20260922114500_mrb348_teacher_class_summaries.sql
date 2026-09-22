-- ════════════════════════════════════════════════════════════════════════
-- MRB-348 WS-2 — public.teacher_class_summaries(uuid[])
-- One row per class: the six numbers the SUMMARY screens draw, computed
-- in SQL instead of shipped to the browser.
-- ════════════════════════════════════════════════════════════════════════
--
-- WHAT THIS REPLACES
-- ==================
-- `loadClassMatrices()` in `shared/teacher-data.js` is the universal read
-- behind all six generated teacher screens. It fetches EVERY submission of
-- EVERY assignment of EVERY class the viewer touches — no limit, no window —
-- and then computes the class-card numbers in JavaScript with
-- `pickFirstAttempts()` + `deriveClassMetrics()`. At week 2 of term that is
-- a hundred rows. By December, five classes × forty assignments × thirty
-- students is tens of thousands of rows over the wire to render a page that
-- often shows only counts.
--
-- This function answers the counting question at the database, where the
-- rows already are.
--
-- ⚠️ IT IS A SECOND IMPLEMENTATION OF A LOCKED RULE, AND THAT IS THE RISK
-- THIS HEADER EXISTS TO NAME. The first-attempt rule (MRB-38, Mide,
-- 9 May 2026) now has two implementations that must agree for ever: the
-- JavaScript `pickFirstAttempts()` and the `DISTINCT ON` below. They are
-- written to be read side by side:
--
--     JS                                     SQL
--     lower `attempts` wins                  COALESCE(attempts, 2147483647) ASC
--     tiebreak: earlier submitted_at         COALESCE(submitted_at,'infinity') ASC
--     NULL attempts is worst                 2147483647
--     NULL submitted_at is worst in a tie    'infinity'
--
-- The same shape `class_stars_leaderboard_for_member` already uses. ⚠️ Do
-- not "simplify" it to `attempt_no = 1` or `ORDER BY submitted_at` — both
-- are different rules, and both are wrong on the estate's real rows (a
-- retake with no `attempts`, an historic row with no stamp).
--
-- ⚠️ A FULL TIE IS NOT DEFINED BY EITHER SIDE. Two live rows for one
-- (assignment, student) with the SAME `attempts` and the SAME
-- `submitted_at` are separated by the JS only by PostgREST's return order,
-- which is unspecified. `s.id ASC` is added here so THIS side is at least
-- deterministic; it is a tiebreak for an anomaly, not a rule. TEST held
-- none on 22 Sep 2026.
--
-- THE SIX NUMBERS, AND WHICH JS LINE EACH MIRRORS
-- ===============================================
--   active_member_count    `loadClassMatrices` members grouping — `left_at IS
--                          NULL`, `deleted_at IS NULL`, and the embedded
--                          profile neither null nor soft-deleted (the JS does
--                          that last one in JavaScript because PostgREST
--                          cannot filter an embedded resource; here it is a
--                          join).
--   assignment_count       `deleteAt IS NULL` assignments of the class.
--   submissions_completed  `deriveClassMetrics`: first attempts with
--                          `submitted_at` NOT NULL. ⚠️ NOT the matrix's
--                          `colSub`, which counts a row `completed_at` or
--                          `status='complete'` also satisfies. The two
--                          predicates are genuinely different and the card
--                          uses this one.
--   completion_pct         `Math.round(handed / (members × assignments) ×
--                          100)`, NULL — never 0 — when the denominator is 0.
--   class_mean             `buildMatrix`'s `classMean`: the mean OF THE
--                          MARKED COLUMN MEANS, each column mean itself
--                          `round(Σscore / Σmax × 100)` over EVERYONE who sat
--                          the paper (active AND departed — the locked MRB-38
--                          rule), a column contributing only when something in
--                          it is graded. ⚠️ A mean of means, not a pooled
--                          Σ/Σ — Design's README pins it that way so the
--                          digest's "mean of N class means" is a mean of
--                          things that are themselves means.
--   last_activity_at       `max(submitted_at)` over the first attempts.
--
-- ⚠️ `marked` MEANS "THE DEADLINE HAS PASSED", nothing else — `buildPapers`'
-- `when = open ? 'upcoming' : 'marked'` with `open = !due_at || due_at >
-- now`. It is NOT "released", NOT "somebody sat it" and NOT "graded". An
-- assignment with no `due_at` never closes and is never marked.
--
-- ⚠️ float8 THEN numeric, ON PURPOSE. `round(((a::float8 / b::float8) *
-- 100)::numeric)` reproduces JavaScript's `Math.round(a / b * 100)`
-- exactly: the same IEEE double division, then half-away-from-zero rounding
-- (which equals `Math.round` for non-negative values). Rounding the float8
-- directly would use Postgres's banker's rounding and disagree on every
-- exact `.5`; doing the division in `numeric` would disagree wherever the
-- double is a hair under a `.5`.
--
-- SECURITY
-- ========
-- SECURITY DEFINER with `SET search_path TO 'public'`, gated INTERNALLY as
-- its first statement, in the shape `class_teachers_for_viewer` and
-- `class_stars_leaderboard_for_member` both use. A class id the caller may
-- not see is DROPPED SILENTLY rather than raising — a summary read is asked
-- speculatively over a remembered id list, and an error would take the whole
-- page down over one stale id.
--
-- ⚠️ THE GATE IS NOT ONE PREDICATE, BECAUSE THE FOUR TABLES' RLS IS NOT ONE
-- PREDICATE, and getting that wrong would make this function return numbers
-- no reader could have computed for themselves. The live policies (TEST,
-- post-WS-3 consolidation) grant:
--
--   classes / class_members    operator | school+(school_admin|slt) |
--                              school+hod | school+teaches
--   assignments / submissions  operator | school+(school_admin|slt) |
--                              school+HOD **OF THAT SUBJECT'S DEPARTMENT** |
--                              school+teaches
--
-- So a plain HoD sees every class in the school and every MEMBER of it, but
-- only the assignments — and therefore only the submissions — of their own
-- department. `all_work` below is exactly that distinction: when it is
-- false, the assignment set is narrowed by
-- `auth_user_is_hod_of_subject_dept(a.subject_id)` and every number derived
-- from it narrows with it, which is what that reader's browser would have
-- computed.
--
-- ⚠️ THE STUDENT ARMS ARE DELIBERATELY NOT REPRODUCED. `class_members` and
-- `assignment_submissions` both also grant `student_id = auth_user_id()`, so
-- a pupil can read their own row. This is a teacher aggregate; a pupil
-- calling it gets the class dropped by the gate and no rows back. That is a
-- NARROWING of what RLS would allow them, never a widening, and no student
-- surface calls it.
--
-- Default grants are left as the estate's other definer functions carry
-- them (EXECUTE to PUBLIC). An anon caller has no `auth.uid()` and no
-- school, so every arm of the gate is false and the function returns zero
-- rows.
--
-- WHAT IT IS NOT FOR
-- ==================
-- The full student × assignment grid. `class-detail`, `assignment` and
-- `student-detail` genuinely need every submission row of ONE class and must
-- keep reading them; this function answers only the counting question the
-- summary screens ask.
-- ════════════════════════════════════════════════════════════════════════

CREATE OR REPLACE FUNCTION public.teacher_class_summaries(p_class_ids uuid[])
RETURNS TABLE (
  class_id              uuid,
  active_member_count   int,
  assignment_count      int,
  submissions_completed int,
  completion_pct        int,
  class_mean            int,
  last_activity_at      timestamptz
)
LANGUAGE plpgsql
STABLE SECURITY DEFINER
SET search_path TO 'public'
AS $function$
DECLARE
  v_school   uuid;
  v_operator boolean;
  v_wide     boolean;   -- school_admin OR slt
  v_hod      boolean;
  v_now      timestamptz := now();
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
    SELECT id, all_work FROM visible WHERE can_see
  ),
  mem AS (
    SELECT cm.class_id, COUNT(*)::int AS n
      FROM class_members cm
      JOIN cls ON cls.id = cm.class_id
      JOIN profiles p ON p.id = cm.student_id
     WHERE cm.deleted_at IS NULL
       AND cm.left_at   IS NULL
       AND p.deleted_at IS NULL
     GROUP BY cm.class_id
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
           s.submitted_at, s.completed_at, s.status
      FROM assignment_submissions s
      JOIN asg ON asg.id = s.assignment_id
     WHERE s.deleted_at IS NULL
     ORDER BY s.assignment_id, s.student_id,
              COALESCE(s.attempts, 2147483647) ASC,
              COALESCE(s.submitted_at, 'infinity'::timestamptz) ASC,
              s.id ASC
  ),
  handed AS (
    SELECT asg.class_id,
           COUNT(*) FILTER (WHERE fa.submitted_at IS NOT NULL)::int AS n,
           MAX(fa.submitted_at)                                     AS last_at
      FROM asg
      JOIN first_attempts fa ON fa.assignment_id = asg.id
     GROUP BY asg.class_id
  ),
  -- One row per assignment: Σscore and Σmax over every first attempt that
  -- `cellOf` would have turned into a graded cell.
  per_assignment AS (
    SELECT asg.id, asg.class_id, asg.due_at,
           COALESCE(SUM(fa.score)     FILTER (WHERE graded), 0) AS tot,
           COALESCE(SUM(fa.max_score) FILTER (WHERE graded), 0) AS totmax
      FROM asg
      LEFT JOIN LATERAL (
        SELECT f.score, f.max_score,
               ((f.completed_at IS NOT NULL
                 OR f.submitted_at IS NOT NULL
                 OR f.status = 'complete')
                AND f.score     IS NOT NULL
                AND f.max_score IS NOT NULL
                AND f.max_score > 0) AS graded
          FROM first_attempts f
         WHERE f.assignment_id = asg.id
      ) fa ON TRUE
     GROUP BY asg.id, asg.class_id, asg.due_at
  ),
  marked_means AS (
    SELECT pa.class_id,
           round((((pa.tot)::float8 / (pa.totmax)::float8) * 100)::numeric)::int AS mean
      FROM per_assignment pa
     WHERE pa.due_at IS NOT NULL
       AND pa.due_at <= v_now
       AND pa.totmax > 0
  ),
  cmean AS (
    SELECT mm.class_id,
           round(((SUM(mm.mean))::float8 / (COUNT(*))::float8)::numeric)::int AS class_mean
      FROM marked_means mm
     GROUP BY mm.class_id
  )
  SELECT cls.id,
         COALESCE(mem.n, 0),
         COALESCE(acount.n, 0),
         COALESCE(handed.n, 0),
         CASE WHEN COALESCE(mem.n, 0) * COALESCE(acount.n, 0) = 0 THEN NULL
              ELSE round(((COALESCE(handed.n, 0))::float8
                          / ((mem.n * acount.n))::float8 * 100)::numeric)::int
         END,
         cmean.class_mean,
         handed.last_at
    FROM cls
    LEFT JOIN mem    ON mem.class_id    = cls.id
    LEFT JOIN acount ON acount.class_id = cls.id
    LEFT JOIN handed ON handed.class_id = cls.id
    LEFT JOIN cmean  ON cmean.class_id  = cls.id;
END;
$function$;

COMMENT ON FUNCTION public.teacher_class_summaries(uuid[]) IS
  'MRB-348 WS-2. Per-class summary numbers for the teacher summary screens, '
  'computed in SQL under the first-attempt rule (MRB-38). Gated internally '
  'on the same reader set the classes/class_members/assignments/'
  'assignment_submissions SELECT policies grant; unreadable class ids are '
  'dropped silently.';
