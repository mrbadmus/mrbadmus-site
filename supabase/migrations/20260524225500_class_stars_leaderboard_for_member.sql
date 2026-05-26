-- =====================================================================
-- Migration:        20260524225500_class_stars_leaderboard_for_member.sql
-- Stage:            2C — Class shoutouts (MRB-46) — Phase 3 enabler
-- Branch:           schools/mrb-46-phase-3-student-class
-- Apply target:     TEST PROJECT ONLY (qeppkiswvclkkwbxmlok)
-- DO NOT APPLY ON:  PRODUCTION (urklkrwevjtlfbwnipjn) until MRB-35
-- Linear:           MRB-46 (Phase 3 — student class detail page)
-- Author:           Drafted with Mide on 2026-05-24
-- =====================================================================
--
-- Adds class_stars_leaderboard_for_member(p_class_id uuid) — a SECURITY
-- DEFINER function that returns the weekly Stars leaderboard for a class.
-- Required because students CANNOT see other students' submissions via
-- RLS (assignment_submissions.submissions_self_all restricts to
-- student_id = auth_user_id()), so they cannot compute the leaderboard
-- client-side the way teachers do (teachers see all submissions in their
-- classes via submissions_teacher_read).
--
-- The function:
--   1. Checks the caller is an active member of the class (else returns
--      empty + 'not_member'). This is the security boundary.
--   2. Computes the current assignment-week window using Europe/London
--      timezone (matches the JS-side computeWeekWindow behaviour for
--      UK users — the platform's intended audience).
--   3. Identifies week assignments + active members + first-attempt
--      submissions.
--   4. Applies the same two-gate eligibility as
--      teacher-data.js's calcLeaderboard:
--         - All week assignments submitted on time
--         - Total weekly score_pct >= 75%
--   5. Returns ranked top-N with first/last/avatar + score + time.
--
-- Return shape — mirrors calcLeaderboard's output exactly so the
-- existing renderStarsLeaderboard function works without modification:
--   {
--     "eligible": [
--       { student_id, first_name, last_name, avatar_url,
--         on_time_count, total_this_week, score_pct, total_time_sec }
--     ],
--     "is_empty": boolean,
--     "empty_reason": "not_member" | "class_not_found"
--                     | "no_assignments_this_week" | "no_eligibles_yet"
--                     | null
--   }
--
-- Privacy posture: reveals first_name + last_name + avatar_url + score
-- for top-N eligible members of THIS class to any active member. That's
-- exactly what the rendered podium shows; no over-exposure beyond the
-- visible UI.
--
-- Wrapped in a single transaction. CREATE OR REPLACE makes this safe
-- to re-run.
-- =====================================================================

BEGIN;

CREATE OR REPLACE FUNCTION public.class_stars_leaderboard_for_member(p_class_id uuid)
RETURNS jsonb
LANGUAGE plpgsql
STABLE
SECURITY DEFINER
SET search_path TO 'public'
AS $$
DECLARE
  v_anchor               int;
  v_local_today          timestamp;
  v_local_today_dow      int;
  v_start_at             timestamptz;
  v_end_at               timestamptz;
  v_week_assignment_count int;
  v_result               jsonb;
BEGIN
  -- 1. Membership gate — non-members get nothing.
  IF NOT auth_user_is_member_of_class(p_class_id) THEN
    RETURN jsonb_build_object(
      'eligible',     '[]'::jsonb,
      'is_empty',     true,
      'empty_reason', 'not_member'
    );
  END IF;

  -- 2. Anchor day (default Monday = 1 if class.assignment_day_of_week is NULL).
  -- Also drop out if the class is soft-deleted or doesn't exist.
  SELECT COALESCE(c.assignment_day_of_week, 1)
    INTO v_anchor
  FROM classes c
  WHERE c.id = p_class_id AND c.deleted_at IS NULL;

  IF v_anchor IS NULL THEN
    RETURN jsonb_build_object(
      'eligible',     '[]'::jsonb,
      'is_empty',     true,
      'empty_reason', 'class_not_found'
    );
  END IF;

  -- 3. Week window in Europe/London timezone — matches JS-side semantics
  -- for UK users. v_local_today is "today's local clock-day midnight"
  -- as a naive timestamp; v_start_at converts back to timestamptz so
  -- comparison against assignment.due_at (timestamptz) is correct.
  v_local_today := date_trunc('day', now() AT TIME ZONE 'Europe/London');
  v_local_today_dow := EXTRACT(dow FROM v_local_today)::int;
  v_start_at := (v_local_today
                 - (((v_local_today_dow - v_anchor + 7) % 7) * interval '1 day')
                ) AT TIME ZONE 'Europe/London';
  v_end_at := v_start_at + interval '7 days';

  -- 4. Count this week's assignments. None → empty.
  SELECT COUNT(*) INTO v_week_assignment_count
  FROM assignments a
  WHERE a.class_id = p_class_id
    AND a.deleted_at IS NULL
    AND a.due_at IS NOT NULL
    AND a.due_at >= v_start_at AND a.due_at < v_end_at;

  IF v_week_assignment_count = 0 THEN
    RETURN jsonb_build_object(
      'eligible',     '[]'::jsonb,
      'is_empty',     true,
      'empty_reason', 'no_assignments_this_week'
    );
  END IF;

  -- 5. Compute eligible. Mirrors calcLeaderboard:
  --   - For each active member × each week assignment, pick first attempt
  --     (lowest 'attempts', tiebreak earliest submitted_at; NULLs worst).
  --   - On-time = submitted >= week_start AND submitted <= due_at.
  --   - Gate 1: on_time_count = total_assignments.
  --   - Gate 2: score_pct >= 75 over on-time graded subs.
  --   - Sort score DESC, time ASC (NULL last), first_name ASC.
  WITH
    week_assignments AS (
      SELECT a.id, a.due_at
      FROM assignments a
      WHERE a.class_id = p_class_id
        AND a.deleted_at IS NULL
        AND a.due_at IS NOT NULL
        AND a.due_at >= v_start_at AND a.due_at < v_end_at
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
        CASE WHEN fa.submitted_at IS NOT NULL
              AND fa.submitted_at >= v_start_at
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
        v_week_assignment_count AS total_assignments,
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
    'empty_reason', CASE WHEN COUNT(*) = 0 THEN 'no_eligibles_yet'::text ELSE NULL END
  ) INTO v_result
  FROM eligible e;

  RETURN v_result;
END;
$$;

GRANT EXECUTE ON FUNCTION public.class_stars_leaderboard_for_member(uuid) TO authenticated;

COMMIT;
