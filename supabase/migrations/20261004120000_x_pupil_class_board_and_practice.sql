-- =====================================================================
-- Migration:        20261004120000_x_pupil_class_board_and_practice.sql
-- Stage:            Prompt X, unit C — pupil class page
-- Branch:           feat/x-mig-pupil-class (PARKED — not merged to main)
-- Apply target:     TEST PROJECT ONLY (qeppkiswvclkkwbxmlok) until Mide
--                    merges the frontend/backend branches that read it.
-- DO NOT APPLY ON:  PRODUCTION (urklkrwevjtlfbwnipjn) until the merge.
-- Linear:           Prompt X / SPEC-C
-- =====================================================================
--
-- THREE CHANGES, ALL ADDITIVE OR A REDEFINE-IN-PLACE OF AN EXISTING
-- SECURITY DEFINER FUNCTION. Nothing here drops a column or a table.
--
-- 1. `class_stars_leaderboard_for_member(p_class_id uuid)` is REDEFINED.
--    Same name, same signature, same return shape
--    ({ eligible[], is_empty, empty_reason }) — every existing caller
--    (shared/student-data.js:463) keeps working unchanged. What moves is
--    the WEEK RULE:
--
--      BEFORE: "this week" = assignments whose due_at falls in
--      [Mon 00:00 London anchor, next Mon). On-time required
--      submitted_at >= that window's start AND <= due_at.
--
--      AFTER: "this week" = assignments whose SET week (academic_week,
--      falling back to the teaching week computed from
--      COALESCE(release_at, created_at) when academic_week is null) is
--      the class's CURRENT teaching week, by the same Sunday-rollover
--      clock assignment-compose.js's currentTeachingWeek() and
--      teacher-live.js's teachingWeek() already use. On-time drops the
--      lower bound: submitted_at <= due_at is enough. Teachers routinely
--      set work one week with a due date the next, so the old window
--      never held the work it was meant to hold and no class could ever
--      produce an eligible student — verified empty on every live class
--      before this migration.
--
-- 2. `class_stars_board_for_member(p_class_id uuid)` is a NEW function,
--    same SECURITY DEFINER / search_path posture. It answers what #1
--    cannot: a PER-WEEK RANKING for the class's board (the page's four
--    W01-W04 chips, oldest..newest with 4 = now, plus TERM). Mide's
--    ruling of 4 Oct 2026: a pupil sees only the TOP FIVE of the class,
--    with their scores, and nothing about anyone else, enforced here. A
--    teacher of the class gets the full ranking. Points are the week's
--    percentage (the number #1 calls score_pct). See section 2 below for
--    the exact rules, including how ties are broken.
--
-- 3. `practice_rounds` is a NEW table. One row per completed practice
--    round (never a half-finished one — the backend route this feeds
--    only ever inserts on the LAST question of a round). RLS on, no
--    insert/update/delete policy (server-only, via the service role
--    key, from POST /api/class/practice/round) — SELECT modelled on
--    `flashcard_sessions_select`'s three arms (pupil's own rows; the
--    class's own teacher; school admin/SLT).
-- =====================================================================

BEGIN;

-- ── a week-number helper, shared by both functions below ──────────────
-- The SQL mirror of assignment-compose.js's weekZeroFor()/currentTeachingWeek():
-- week 1 begins on the Sunday on or before the academic year's start_date;
-- the week number of any later instant is how many whole Sunday-to-Sunday
-- spans separate its own Sunday from that one, plus one. Floored at 1 so an
-- instant before the year opened (or a null year) never produces a
-- non-positive or wrapping week number — matching currentTeachingWeek()'s
-- own "before the year opens, the week is 1" ruling.
CREATE OR REPLACE FUNCTION public._mrb_week_number(p_year_start date, p_instant timestamptz)
RETURNS int
LANGUAGE plpgsql
STABLE
AS $$
DECLARE
  v_today      date;
  v_sunday0    date;
  v_sunday_now date;
BEGIN
  IF p_year_start IS NULL OR p_instant IS NULL THEN
    RETURN NULL;
  END IF;
  v_today      := (p_instant AT TIME ZONE 'Europe/London')::date;
  -- EXTRACT(dow FROM date): Sunday = 0 … Saturday = 6, the same numbering
  -- assignment-compose.js's getUTCDay() uses.
  v_sunday0    := p_year_start - EXTRACT(DOW FROM p_year_start)::int;
  v_sunday_now := v_today      - EXTRACT(DOW FROM v_today)::int;
  RETURN GREATEST(1, ((v_sunday_now - v_sunday0) / 7)::int + 1);
END;
$$;

COMMENT ON FUNCTION public._mrb_week_number(date, timestamptz) IS
  'Internal helper for class_stars_leaderboard_for_member and '
  'class_stars_board_for_member. Mirrors assignment-compose.js '
  'weekZeroFor()/currentTeachingWeek() — Sunday-rollover teaching weeks, '
  'floored at week 1. Not granted to any role; called only from the two '
  'SECURITY DEFINER functions below, which run as their owner.';

-- ── 1. class_stars_leaderboard_for_member — REDEFINED ──────────────────
CREATE OR REPLACE FUNCTION public.class_stars_leaderboard_for_member(p_class_id uuid)
RETURNS jsonb
LANGUAGE plpgsql
STABLE
SECURITY DEFINER
SET search_path TO 'public'
AS $$
DECLARE
  v_year_start   date;
  v_year_end     date;
  v_current_week int;
  v_result       jsonb;
BEGIN
  -- 1. Membership gate — non-members get nothing.
  IF NOT auth_user_is_member_of_class(p_class_id) THEN
    RETURN jsonb_build_object(
      'eligible',     '[]'::jsonb,
      'is_empty',     true,
      'empty_reason', 'not_member'
    );
  END IF;

  -- 2. The class's academic year, for the week clock. Also the
  -- class-not-found / soft-deleted check the original function made via
  -- assignment_day_of_week.
  SELECT ay.start_date, ay.end_date
    INTO v_year_start, v_year_end
  FROM classes c
  JOIN academic_years ay ON ay.id = c.academic_year_id
  WHERE c.id = p_class_id AND c.deleted_at IS NULL;

  IF v_year_start IS NULL THEN
    RETURN jsonb_build_object(
      'eligible',     '[]'::jsonb,
      'is_empty',     true,
      'empty_reason', 'class_not_found'
    );
  END IF;

  v_current_week := public._mrb_week_number(v_year_start, now());

  -- 3. This week's assignments — SET in the current teaching week, by
  -- academic_week where the backend stamped one, else by the teaching
  -- week the class's own composer/teacher-live.js clock would assign to
  -- COALESCE(release_at, created_at). A set belongs to the week it was
  -- SET in, not the week it falls due in — teachers routinely set one
  -- week due the next.
  WITH
    week_assignments AS (
      SELECT a.id, a.due_at
      FROM assignments a
      WHERE a.class_id = p_class_id
        AND a.deleted_at IS NULL
        AND a.due_at IS NOT NULL
        AND COALESCE(a.academic_week,
              public._mrb_week_number(v_year_start,
                COALESCE(a.release_at, a.created_at))) = v_current_week
    ),
    active_members AS (
      SELECT cm.student_id, p.first_name, p.last_name, p.avatar_url
      FROM class_members cm
      JOIN profiles p ON p.id = cm.student_id
      WHERE cm.class_id = p_class_id
        AND cm.left_at IS NULL
        AND cm.deleted_at IS NULL
        AND p.deleted_at IS NULL
    ),
    first_attempts AS (
      SELECT DISTINCT ON (sub.assignment_id, sub.student_id)
        sub.assignment_id, sub.student_id,
        sub.score, sub.max_score,
        sub.submitted_at, sub.total_time_seconds
      FROM assignment_submissions sub
      WHERE sub.assignment_id IN (SELECT id FROM week_assignments)
        AND sub.student_id    IN (SELECT student_id FROM active_members)
        AND sub.deleted_at IS NULL
      ORDER BY
        sub.assignment_id,
        sub.student_id,
        COALESCE(sub.attempts, 2147483647) ASC,
        COALESCE(sub.submitted_at, 'infinity'::timestamptz) ASC
    ),
    student_x_assignment AS (
      SELECT
        am.student_id, am.first_name, am.last_name, am.avatar_url,
        wa.id        AS assignment_id,
        wa.due_at,
        fa.score, fa.max_score, fa.submitted_at, fa.total_time_seconds,
        -- ⊕ on-time drops the lower bound: a submission before the week
        -- even opened (an early hand-in) is still on time. Only the
        -- deadline itself still matters.
        CASE WHEN fa.submitted_at IS NOT NULL
              AND fa.submitted_at <= wa.due_at
             THEN 1 ELSE 0 END AS is_on_time
      FROM active_members am
      CROSS JOIN week_assignments wa
      LEFT JOIN first_attempts fa
        ON fa.assignment_id = wa.id AND fa.student_id = am.student_id
    ),
    student_aggregates AS (
      SELECT
        sx.student_id, sx.first_name, sx.last_name, sx.avatar_url,
        SUM(sx.is_on_time) AS on_time_count,
        (SELECT COUNT(*) FROM week_assignments) AS total_assignments,
        SUM(CASE WHEN sx.is_on_time = 1
                  AND sx.score IS NOT NULL
                  AND sx.max_score IS NOT NULL
                  AND sx.max_score > 0
                 THEN sx.score ELSE 0 END) AS total_score,
        SUM(CASE WHEN sx.is_on_time = 1
                  AND sx.score IS NOT NULL
                  AND sx.max_score IS NOT NULL
                  AND sx.max_score > 0
                 THEN sx.max_score ELSE 0 END) AS total_max,
        SUM(CASE WHEN sx.is_on_time = 1
                  AND sx.total_time_seconds IS NOT NULL
                 THEN sx.total_time_seconds ELSE 0 END) AS total_time_sec,
        bool_or(sx.is_on_time = 1 AND sx.total_time_seconds IS NOT NULL) AS any_time_present
      FROM student_x_assignment sx
      GROUP BY sx.student_id, sx.first_name, sx.last_name, sx.avatar_url
    ),
    eligible AS (
      SELECT
        sa.student_id, sa.first_name, sa.last_name, sa.avatar_url,
        sa.on_time_count, sa.total_assignments,
        sa.total_score, sa.total_max, sa.total_time_sec, sa.any_time_present,
        ROUND((sa.total_score::numeric / sa.total_max::numeric) * 100)::int AS score_pct
      FROM student_aggregates sa
      WHERE sa.on_time_count = sa.total_assignments      -- gate 1: all on-time
        AND sa.total_max > 0                              -- has graded subs
        AND ROUND((sa.total_score::numeric / sa.total_max::numeric) * 100) >= 75  -- gate 2
    )
  SELECT jsonb_build_object(
    'eligible', COALESCE(
      jsonb_agg(
        jsonb_build_object(
          'student_id',      e.student_id,
          'first_name',      e.first_name,
          'last_name',       e.last_name,
          'avatar_url',      e.avatar_url,
          'on_time_count',   e.on_time_count,
          'total_this_week', e.total_assignments,
          'score_pct',       e.score_pct,
          'total_time_sec',  CASE WHEN e.any_time_present THEN e.total_time_sec ELSE NULL END
        )
        ORDER BY
          e.score_pct DESC,
          CASE WHEN e.any_time_present THEN e.total_time_sec ELSE 2147483647 END ASC,
          e.first_name ASC
      ),
      '[]'::jsonb
    ),
    'is_empty',     CASE WHEN COUNT(*) = 0 THEN true ELSE false END,
    'empty_reason', CASE WHEN COUNT(*) = 0 THEN
                       (CASE WHEN (SELECT COUNT(*) FROM week_assignments) = 0
                             THEN 'no_assignments_this_week'
                             ELSE 'no_eligibles_yet' END)::text
                     ELSE NULL END
  ) INTO v_result
  FROM eligible e;

  RETURN v_result;
END;
$$;

GRANT EXECUTE ON FUNCTION public.class_stars_leaderboard_for_member(uuid) TO authenticated;

-- ── 2. class_stars_board_for_member — NEW (Mide's ruling, 4 Oct 2026) ──
-- "Leaderboard should only show top 5 in the class, that way only the best
-- of the best are being shown."
--
-- ENFORCED HERE, NOT IN THE PAGE. For a PUPIL caller the function returns,
-- per tab (the four week chips "1".."4", oldest..newest with 4 = now, and
-- "term"), AT MOST FIVE entries {id, name, mono, points, me} — and nothing
-- about anyone else. A pupil outside the five gets the five and no row,
-- rank or score of their own; `me` is true only on a row that is theirs.
-- A pupil with nothing handed in on time that week is never listed (points
-- must be above 0), so a quiet week returns fewer than five, or none.
-- A TEACHER of the class (class_teachers, active) gets every pupil, ranked.
-- Anyone else (not a member, not a teacher) gets not_member and nothing.
--
-- points = the week's percentage: marks over marks possible across the
-- week's sets, first attempts, graded, handed in on time (the number the
-- sibling function calls score_pct). TERM = the four weeks added, as the
-- page's template always added its four chips.
--
-- TIES: points high to low; then whoever FINISHED FIRST, defined as the
-- earlier "latest counted hand-in" — for a week tab, the latest
-- COALESCE(completed_at, submitted_at) among the pupil's counted hand-ins in
-- that week's sets; for TERM, the latest among their counted hand-ins in
-- all four weeks (the moment they finished the scope's work); then the
-- pupil id, so the order is the same on every call. Exactly five are
-- returned however many tie at fifth.
--
-- ⚠️ CTEs, never CREATE TEMP TABLE (a STABLE function cannot run DDL; the
-- first draft's temp tables were refused on the first TEST call).
CREATE OR REPLACE FUNCTION public.class_stars_board_for_member(p_class_id uuid)
RETURNS jsonb
LANGUAGE plpgsql
STABLE
SECURITY DEFINER
SET search_path TO 'public'
AS $$
DECLARE
  v_year_start   date;
  v_current_week int;
  v_viewer       uuid := auth.uid();
  v_is_member    boolean;
  v_is_teacher   boolean := false;
  v_roster_count int;
  v_result       jsonb;
BEGIN
  -- Membership gate, unchanged for a pupil. A teacher of the class is the
  -- one other caller let through (full ranking); anyone else gets nothing.
  v_is_member := auth_user_is_member_of_class(p_class_id);
  IF NOT v_is_member THEN
    SELECT EXISTS (
      SELECT 1 FROM class_teachers ct
      WHERE ct.class_id = p_class_id
        AND ct.teacher_id = v_viewer
        AND ct.ended_at IS NULL AND ct.deleted_at IS NULL
    ) INTO v_is_teacher;
    IF NOT v_is_teacher THEN
      RETURN jsonb_build_object(
        'is_empty', true, 'empty_reason', 'not_member',
        'mode', 'none', 'tabs', '{}'::jsonb
      );
    END IF;
  END IF;

  SELECT ay.start_date
    INTO v_year_start
  FROM classes c
  JOIN academic_years ay ON ay.id = c.academic_year_id
  WHERE c.id = p_class_id AND c.deleted_at IS NULL;

  IF v_year_start IS NULL THEN
    RETURN jsonb_build_object(
      'is_empty', true, 'empty_reason', 'class_not_found',
      'mode', 'none', 'tabs', '{}'::jsonb
    );
  END IF;

  SELECT COUNT(*) INTO v_roster_count
  FROM class_members cm
  JOIN profiles p ON p.id = cm.student_id
  WHERE cm.class_id = p_class_id
    AND cm.left_at IS NULL AND cm.deleted_at IS NULL AND p.deleted_at IS NULL;

  IF v_roster_count = 0 THEN
    RETURN jsonb_build_object(
      'is_empty', true, 'empty_reason', 'no_members',
      'mode', 'none', 'tabs', '{}'::jsonb
    );
  END IF;

  v_current_week := public._mrb_week_number(v_year_start, now());

  WITH
    roster AS (
      SELECT cm.student_id, p.first_name, p.last_name
      FROM class_members cm
      JOIN profiles p ON p.id = cm.student_id
      WHERE cm.class_id = p_class_id
        AND cm.left_at IS NULL AND cm.deleted_at IS NULL AND p.deleted_at IS NULL
    ),
    positions AS (
      SELECT pos, (v_current_week - (4 - pos)) AS real_week
      FROM generate_series(1, 4) AS pos
    ),
    -- Every COUNTED hand-in: first attempt, graded, in on time. One row per
    -- (position, pupil, set). `done_at` is when the pupil finished it.
    counted AS (
      SELECT pos.pos, r.student_id, fa.score, fa.max_score,
             COALESCE(fa.completed_at, fa.submitted_at) AS done_at
      FROM positions pos
      CROSS JOIN roster r
      JOIN assignments a
        ON a.class_id = p_class_id
       AND a.deleted_at IS NULL
       AND a.due_at IS NOT NULL
       AND COALESCE(a.academic_week,
             public._mrb_week_number(v_year_start,
               COALESCE(a.release_at, a.created_at))) = pos.real_week
      JOIN LATERAL (
        SELECT sub.score, sub.max_score, sub.submitted_at, sub.completed_at
        FROM assignment_submissions sub
        WHERE sub.assignment_id = a.id
          AND sub.student_id = r.student_id
          AND sub.deleted_at IS NULL
        ORDER BY COALESCE(sub.attempts, 2147483647) ASC,
                 COALESCE(sub.submitted_at, 'infinity'::timestamptz) ASC
        LIMIT 1
      ) fa ON true
      WHERE fa.submitted_at IS NOT NULL
        AND fa.submitted_at <= a.due_at
        AND fa.score IS NOT NULL AND fa.max_score IS NOT NULL
        AND fa.max_score > 0
    ),
    -- One row per (position, pupil): the week's percentage (the same number
    -- the sibling function calls score_pct) and when the pupil's LATEST
    -- counted hand-in that week was finished.
    per_week AS (
      SELECT r.student_id, pos.pos,
             COALESCE(ROUND(SUM(c.score)::numeric / NULLIF(SUM(c.max_score), 0) * 100)::int, 0) AS pts,
             MAX(c.done_at) AS tie_at
      FROM roster r
      CROSS JOIN positions pos
      LEFT JOIN counted c ON c.student_id = r.student_id AND c.pos = pos.pos
      GROUP BY r.student_id, pos.pos
    ),
    -- TERM = the four weeks added, exactly as the page's template adds its
    -- four chips; its tie-break is the LATEST hand-in anywhere in the four.
    term AS (
      SELECT student_id, SUM(pts)::int AS pts, MAX(tie_at) AS tie_at
      FROM per_week GROUP BY student_id
    ),
    tabbed AS (
      SELECT pos::text AS tab, student_id, pts, tie_at FROM per_week
      UNION ALL
      SELECT 'term', student_id, pts, tie_at FROM term
    ),
    -- Rank inside each tab: points high to low, then whoever finished
    -- first, then the pupil id so the order can never wobble.
    ranked AS (
      SELECT t.tab, t.student_id, t.pts,
             row_number() OVER (
               PARTITION BY t.tab
               ORDER BY t.pts DESC, t.tie_at ASC NULLS LAST, t.student_id
             ) AS rn
      FROM tabbed t
    ),
    -- The ONLY place the five-row rule lives. A pupil gets rows 1..5 with
    -- marks on the board; a teacher gets everyone.
    visible AS (
      SELECT rk.tab, rk.rn, rk.pts, r.student_id, r.first_name, r.last_name
      FROM ranked rk
      JOIN roster r ON r.student_id = rk.student_id
      WHERE v_is_teacher OR (rk.rn <= 5 AND rk.pts > 0)
    )
  SELECT jsonb_build_object(
    'is_empty', false,
    'empty_reason', NULL,
    'mode', CASE WHEN v_is_teacher THEN 'teacher' ELSE 'pupil' END,
    'tabs', (
      SELECT jsonb_object_agg(k.tab, COALESCE((
        SELECT jsonb_agg(
          jsonb_build_object(
            'id', v.student_id,
            'name', trim(both ' ' from
                      coalesce(v.first_name, '') || ' ' || coalesce(v.last_name, '')),
            'mono', upper(
                      coalesce(substring(v.first_name from 1 for 1), '') ||
                      coalesce(substring(v.last_name  from 1 for 1), '')),
            'points', v.pts,
            'me', v.student_id = v_viewer
          ) ORDER BY v.rn)
        FROM visible v WHERE v.tab = k.tab
      ), '[]'::jsonb))
      FROM (VALUES ('1'), ('2'), ('3'), ('4'), ('term')) AS k(tab)
    )
  ) INTO v_result;

  RETURN v_result;
END;
$$;

GRANT EXECUTE ON FUNCTION public.class_stars_board_for_member(uuid) TO authenticated;

-- ── 3. practice_rounds — NEW table ──────────────────────────────────────
CREATE TABLE IF NOT EXISTS public.practice_rounds (
  id                uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  pupil_id          uuid NOT NULL REFERENCES public.profiles(id),
  class_id          uuid NOT NULL REFERENCES public.classes(id),
  school_id         uuid REFERENCES public.schools(id),
  academic_year_id  uuid REFERENCES public.academic_years(id),
  teaching_week     smallint NOT NULL,
  questions         smallint NOT NULL CHECK (questions BETWEEN 1 AND 6),
  correct           smallint NOT NULL CHECK (correct BETWEEN 0 AND questions),
  completed_at      timestamptz NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS practice_rounds_pupil_class_week_idx
  ON public.practice_rounds (pupil_id, class_id, teaching_week);

ALTER TABLE public.practice_rounds ENABLE ROW LEVEL SECURITY;

-- SELECT only — modelled on flashcard_sessions_select. No insert/update/
-- delete policy at all: every write goes through the backend's service
-- role key (POST /api/class/practice/round), never the browser.
CREATE POLICY practice_rounds_select ON public.practice_rounds
  FOR SELECT
  USING (
    pupil_id = (SELECT auth.uid())
    OR (
      school_id = (SELECT auth_user_school_id())
      AND (
        (SELECT auth_user_has_scope('school_admin'))
        OR (SELECT auth_user_has_scope('slt'))
      )
    )
    OR EXISTS (
      SELECT 1 FROM class_teachers ct
      WHERE ct.class_id = practice_rounds.class_id
        AND ct.teacher_id = (SELECT auth.uid())
        AND ct.ended_at IS NULL
        AND ct.deleted_at IS NULL
    )
  );

COMMENT ON TABLE public.practice_rounds IS
  'One row per COMPLETED practice round on the pupil class page (never a '
  'half-finished one). Written only by the backend service role, from '
  'POST /api/class/practice/round. Prompt X / SPEC-C.';

COMMIT;
