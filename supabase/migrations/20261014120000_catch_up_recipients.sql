-- Catch-up work for absent pupils (14 Oct 2026, feat/catch-up).
--
-- A catch-up is an ordinary assignment (kind 'mcq_set', source 'teacher')
-- set to one or more NAMED pupils of a class rather than the whole class.
-- Its lesson is the assignment's own scope (scope_kind 'subtopic', scope_ref
-- the KS3 lesson / KS4 subtopic slug), so no lesson column is added.
--
-- 1. assignments.recipient_ids uuid[] — NULL = the whole class (every row
--    written before today); a non-empty array = a catch-up for those pupils.
-- 2. A RESTRICTIVE select policy: a pupil who is a member of the class sees a
--    catch-up only if they are named in it. Restrictive policies AND with the
--    existing permissive ones, so no existing policy body is rewritten (TEST
--    and production policy bodies differ — MRB-348). assignment_questions is
--    covered too: its pupil branch reads `assignments` inside its EXISTS, and
--    that read is itself subject to this policy.
-- 3. Three SECURITY DEFINER functions (which bypass RLS) each gain ONE line,
--    `AND a.recipient_ids IS NULL`, so a catch-up never counts in the stars
--    board, the weekly stars leaderboard, or the teacher class rollup.
--    Their bodies are PRODUCTION's, byte-for-byte (md5-proven 14 Oct 2026)
--    plus that line. ⚠️ Re-running feat/x-mig-pupil-class or
--    feat/mrb351-migrations' rollup v2 file AFTER this would drop the line.
--
-- Additive: nothing is dropped; existing rows are untouched (all NULL).
-- Rollback: supabase/rollbacks/20261014120000_catch_up_recipients_rollback.sql

ALTER TABLE public.assignments
  ADD COLUMN IF NOT EXISTS recipient_ids uuid[];

ALTER TABLE public.assignments
  DROP CONSTRAINT IF EXISTS assignments_recipient_ids_nonempty;
ALTER TABLE public.assignments
  ADD CONSTRAINT assignments_recipient_ids_nonempty
  CHECK (recipient_ids IS NULL OR cardinality(recipient_ids) BETWEEN 1 AND 60);

COMMENT ON COLUMN public.assignments.recipient_ids IS
  'Catch-up: NULL = the whole class; otherwise the only pupils (profiles.id) '
  'who may see this assignment. Enforced for pupils by the restrictive policy '
  'assignments_catch_up_audience; excluded from every class aggregate.';

DROP POLICY IF EXISTS assignments_catch_up_audience ON public.assignments;
CREATE POLICY assignments_catch_up_audience ON public.assignments
  AS RESTRICTIVE
  FOR SELECT
  TO public
  USING (
    recipient_ids IS NULL
    OR (SELECT auth.uid()) = ANY (recipient_ids)
    OR NOT auth_user_is_member_of_class(class_id)
    OR auth_user_teaches_class(class_id)
  );

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
        AND a.recipient_ids IS NULL   -- ⊕ catch-up: never a class set
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
       AND a.recipient_ids IS NULL   -- ⊕ catch-up: never a class set
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
       AND a.recipient_ids IS NULL   -- ⊕ catch-up: out of every class figure
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
