/**
 * shared/teacher-data.js — Teacher dashboard data layer
 *
 * Page contract (load AFTER teacher-guard.js):
 *   <script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2/dist/umd/supabase.min.js"></script>
 *   <script src="/shared/config.js"></script>
 *   <script src="/shared/teacher-guard.js"></script>
 *   <script src="/shared/teacher-data.js"></script>
 *   <script>
 *     MrBadmusTeacherGuard.requireTeacherRole({
 *       onAllowed: async function () {
 *         const classes = await MrBadmusTeacherData.loadTeacherClasses();
 *         // render
 *       },
 *     });
 *   </script>
 *
 * Reads classes the signed-in teacher teaches and decorates each with the
 * counts and pill metadata the dashboard needs. Takes no arguments — the
 * Supabase client is fetched via MrBadmusTeacherGuard.getClient(), and RLS
 * scopes rows to the JWT's auth.uid automatically. Layer 2 of
 * defence-in-depth: this module is a UX convenience; the database's RLS
 * policies are the real boundary.
 *
 * Also exports loadClassDetail(classId) — the data layer for the MRB-38
 * class-detail page. Shape, error codes, and the locked design decisions
 * (first-attempt scoring, Logic A eligibility, departed-member handling,
 * window calculation in browser TZ) are documented in the JSDoc directly
 * above that function.
 *
 * Returned shape (one entry per unique class.id, sorted by class.name ASC
 * with natural-number ordering, so "9A" sorts before "10A"):
 *   {
 *     id, name, key_stage, year_group, tier, science_pathway,
 *     pill_label, pill_colour_var,
 *     student_count, assignment_count, submission_count,
 *     completion_pct,        // null if assignment_count === 0
 *                            //   OR if student_count === 0 (no honest %)
 *     last_activity_at,      // ISO string of max(submitted_at), or null
 *   }
 *
 * Subject pill rule (locked for MRB-20):
 *   KS3                  → 'Science'          / var(--science)
 *   KS4 + combined       → 'Combined Science' / var(--science)
 *   KS4 + triple         → derive from class_teachers row with smallest
 *                          subject_id (deterministic), look up name + colour
 *   anything else (KS5)  → null pill (card shows class name only)
 *
 * Error handling:
 *   - Driver query failure       → throw upward; page renders error state
 *   - Per-class sub-query failure → log, return zero counts, so one bad
 *                                   class doesn't blank the whole list
 */

window.MrBadmusTeacherData = (function () {
  // Subject name → CSS variable. Mirrors the :root tokens declared on
  // teacher pages; pill_colour_var is emitted as a string so the page can
  // drop it straight into a style attribute (no DOM lookup at render time).
  const SUBJECT_COLOUR_VARS = {
    Biology:   'var(--biology)',
    Chemistry: 'var(--chemistry)',
    Physics:   'var(--physics)',
  };

  // Decide the subject pill for a class given the (possibly multiple)
  // class_teachers rows that link THIS teacher to it. KS3 + KS4 Combined
  // ignore the rows entirely (pill is derived from the class itself).
  // KS4 Triple picks the row with the smallest subject_id for determinism.
  function derivePill(klass, teacherRowsForClass) {
    if (klass.key_stage === 'KS3') {
      return { pill_label: 'Science', pill_colour_var: 'var(--science)' };
    }
    if (klass.key_stage === 'KS4' && klass.science_pathway === 'combined') {
      return { pill_label: 'Combined Science', pill_colour_var: 'var(--science)' };
    }
    if (klass.key_stage === 'KS4' && klass.science_pathway === 'triple') {
      const sorted = teacherRowsForClass
        .filter(function (r) { return r.subject_id && r.subject && r.subject.name; })
        .slice()
        .sort(function (a, b) {
          if (a.subject_id < b.subject_id) return -1;
          if (a.subject_id > b.subject_id) return 1;
          return 0;
        });
      if (sorted.length === 0) return { pill_label: null, pill_colour_var: null };
      const name = sorted[0].subject.name;
      return { pill_label: name, pill_colour_var: SUBJECT_COLOUR_VARS[name] || null };
    }
    return { pill_label: null, pill_colour_var: null };
  }

  // Shape-only UUID check. Caller-provided classIds in URLs etc. should be
  // validated before any query — Supabase's UUID column would reject the
  // request, but a clear local error is friendlier and saves a round-trip.
  function isUuid(s) {
    return typeof s === 'string' &&
      /^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/i.test(s);
  }

  // Compute the current assignment-week window for a class, given the
  // class's assignment_day_of_week (postgres dow: 0=Sun … 6=Sat). NULL
  // means "not configured" — fall back to Monday (1).
  //
  // Window starts at 00:00 in the BROWSER'S local timezone on the most
  // recent occurrence of anchor_day, on or before today (inclusive when
  // today is the anchor). Ends 7 days later (exclusive).
  //
  // Browser-TZ is a v1 simplification: this platform is UK-AQA-only, so
  // a UK teacher's "Monday" is the local Monday and the start_at lands on
  // local-Monday-midnight. Multi-TZ schools would need school-TZ awareness;
  // not relevant for the current rollout.
  function computeWeekWindow(assignmentDayOfWeek) {
    // Window boundaries use BROWSER-LOCAL time (setHours/getDay).
    // For UK users in BST, this is +1 hour offset from UTC.
    // Intentional per MRB-38 Phase 3a — tied to the user's perception
    // of "Monday" not server time. Revisit if platform expands beyond
    // UK schools.
    const isFallback = (assignmentDayOfWeek === null || assignmentDayOfWeek === undefined);
    const anchor_day = isFallback ? 1 : assignmentDayOfWeek;
    const anchor_source = isFallback ? 'fallback' : 'explicit';

    const now = new Date();
    const today = now.getDay();                       // 0..6, Sun..Sat (matches postgres dow)
    const daysSinceAnchor = (today - anchor_day + 7) % 7;

    const start = new Date(now);
    start.setDate(start.getDate() - daysSinceAnchor);
    start.setHours(0, 0, 0, 0);
    const end = new Date(start);
    end.setDate(end.getDate() + 7);

    return {
      start_at: start.toISOString(),
      end_at: end.toISOString(),
      anchor_day: anchor_day,
      anchor_source: anchor_source,
    };
  }

  // First-attempt-only rule (locked for MRB-38 — Mide, 9 May 2026):
  // For each (assignment_id, student_id) pair, the FIRST attempt's row is
  // the canonical one. All other rows (retakes — 'attempts' > 1) are
  // ignored throughout the data layer: per-student stats, per-assignment
  // stats, leaderboard scoring. Stage 4 will introduce a 'try again'
  // affordance with question rephrasing, but the first-attempt score
  // remains the official one for class means and leaderboards.
  //
  // Picking rule:
  //   1. Lower 'attempts' wins.
  //   2. Tiebreak (same attempts): earlier submitted_at wins.
  //   3. NULL 'attempts' is treated as worst (we have nothing better to
  //      compare on); NULL 'submitted_at' is treated as worst within
  //      tied attempts (a stamped row beats an unstamped one).
  //
  // Returns a Map keyed by `${assignment_id}:${student_id}`.
  function pickFirstAttempts(submissions) {
    const byKey = new Map();
    (submissions || []).forEach(function (s) {
      if (!s.assignment_id || !s.student_id) return;
      const key = s.assignment_id + ':' + s.student_id;
      const existing = byKey.get(key);
      if (!existing) {
        byKey.set(key, s);
        return;
      }
      const existingAttempts = existing.attempts == null ? Number.MAX_SAFE_INTEGER : existing.attempts;
      const newAttempts      = s.attempts        == null ? Number.MAX_SAFE_INTEGER : s.attempts;
      if (newAttempts < existingAttempts) {
        byKey.set(key, s);
        return;
      }
      if (newAttempts === existingAttempts) {
        // NOTE: This compares submitted_at as ISO 8601 strings
        // (lexicographic = chronological). Safe as long as values come
        // from PostgREST as raw timestamptz strings. If anyone later
        // parses them to JS Date objects or strips timezones, this
        // comparison breaks silently and picks the wrong "first attempt."
        // Keep these as strings throughout.
        const existingTs = existing.submitted_at || '￿';
        const newTs      = s.submitted_at        || '￿';
        if (newTs < existingTs) byKey.set(key, s);
      }
    });
    return byKey;
  }

  // Per-class enrichment: student count, assignment count, submission count,
  // last activity. Keeps queries small (HEAD-count for totals, LIMIT 1 for
  // the max). A failure here degrades to zero counts so the rest of the
  // dashboard still renders.
  async function loadClassMetrics(sb, classId) {
    const zero = {
      student_count: 0,
      assignment_count: 0,
      submission_count: 0,
      completion_pct: null,
      last_activity_at: null,
    };

    try {
      // Stage A — student count + assignment ids. Independent, parallel.
      const [studentsRes, assignmentsRes] = await Promise.all([
        sb.from('class_members')
          .select('*', { count: 'exact', head: true })
          .eq('class_id', classId)
          .is('left_at', null)
          .is('deleted_at', null),
        sb.from('assignments')
          .select('id')
          .eq('class_id', classId)
          .is('deleted_at', null),
      ]);

      if (studentsRes.error) throw studentsRes.error;
      if (assignmentsRes.error) throw assignmentsRes.error;

      const student_count = studentsRes.count || 0;
      const assignmentIds = (assignmentsRes.data || []).map(function (r) { return r.id; });
      const assignment_count = assignmentIds.length;

      // No assignments → no submissions to fetch, no completion to compute.
      if (assignment_count === 0) {
        return Object.assign({}, zero, { student_count: student_count });
      }

      // Stage B — submission count + most-recent submitted_at. Both
      // filtered on the same id list; runs in parallel.
      const [subCountRes, subMaxRes] = await Promise.all([
        sb.from('assignment_submissions')
          .select('*', { count: 'exact', head: true })
          .in('assignment_id', assignmentIds)
          .not('submitted_at', 'is', null)
          .is('deleted_at', null),
        sb.from('assignment_submissions')
          .select('submitted_at')
          .in('assignment_id', assignmentIds)
          .not('submitted_at', 'is', null)
          .is('deleted_at', null)
          .order('submitted_at', { ascending: false })
          .limit(1),
      ]);

      if (subCountRes.error) throw subCountRes.error;
      if (subMaxRes.error) throw subMaxRes.error;

      const submission_count = subCountRes.count || 0;
      const last_activity_at =
        (subMaxRes.data && subMaxRes.data[0] && subMaxRes.data[0].submitted_at) || null;

      // Completion: submissions / (students × assignments) × 100, rounded.
      // Denominator is 0 when a class has assignments but no enrolled
      // students — return null so the UI can render an honest dash instead
      // of NaN or a misleading 0%.
      const denom = student_count * assignment_count;
      const completion_pct =
        denom === 0 ? null : Math.round((submission_count / denom) * 100);

      return {
        student_count: student_count,
        assignment_count: assignment_count,
        submission_count: submission_count,
        completion_pct: completion_pct,
        last_activity_at: last_activity_at,
      };
    } catch (e) {
      console.error('[teacher-data] metrics failed for class', classId, e);
      return zero;
    }
  }

  // Per-student stats for the roster section. Produces BOTH all-time
  // and this-week aggregates in a single function call (Phase 4b.5,
  // Mide 12 May 2026). Walks every assignment for all-time stats AND
  // weekAssignments (pre-filtered by loadClassDetail) for the week
  // stats. ACTIVE members only — departed members are excluded from
  // the roster upstream.
  //
  // Soft-NULL handling:
  //   - sub missing OR submitted_at NULL → student didn't submit this one
  //   - on-time means submitted_at <= due_at AND due_at not null
  //   - late_count counts subs where due_at is non-null AND submitted_at > due_at
  //     (subs against undated assignments contribute to submissions_completed
  //     but to neither on_time_count nor late_count)
  //   - score/max_score NULL → submitted-but-ungraded; counts toward
  //     submissions_completed but NOT toward average_score_pct
  //   - average_score_pct is NULL when total_max == 0 (no graded subs)
  //   - week_completion_pct is NULL when week_total_count === 0
  function calcStudentStats(student, assignments, weekAssignments, week, firstAttemptByKey) {
    // ── All-time loop ───────────────────────────────────────────────
    let submissions_completed = 0;
    let on_time_count = 0;
    let late_count = 0;
    let total_score = 0;
    let total_max = 0;
    let last_submitted_at = null;

    assignments.forEach(function (a) {
      const sub = firstAttemptByKey.get(a.id + ':' + student.id);
      if (!sub || !sub.submitted_at) return;
      submissions_completed += 1;
      if (a.due_at && sub.submitted_at <= a.due_at) {
        on_time_count += 1;
      } else if (a.due_at && sub.submitted_at > a.due_at) {
        late_count += 1;
      }
      if (sub.score != null && sub.max_score != null && sub.max_score > 0) {
        total_score += sub.score;
        total_max += sub.max_score;
      }
      if (last_submitted_at == null || sub.submitted_at > last_submitted_at) {
        last_submitted_at = sub.submitted_at;
      }
    });

    // ── This-week loop (Phase 4b.5) ────────────────────────────────
    // Submissions outside the current week window (submitted_at <
    // week.start_at) are uncategorised — neither on-time nor late.
    // Matches calcLeaderboard semantics. In practice this case is
    // rare (assignments don't open before they're set), but the
    // rule is here for production data correctness.
    let week_on_time_count = 0;
    let week_late_count = 0;
    const week_total_count = weekAssignments.length;

    weekAssignments.forEach(function (a) {
      const sub = firstAttemptByKey.get(a.id + ':' + student.id);
      if (!sub || !sub.submitted_at) return;
      if (sub.submitted_at < week.start_at) return;
      if (sub.submitted_at <= a.due_at) {
        week_on_time_count += 1;
      } else {
        week_late_count += 1;
      }
    });
    const week_completion_pct = week_total_count === 0
      ? null
      : Math.round(((week_on_time_count + week_late_count) / week_total_count) * 100);

    return {
      id: student.id,
      first_name: student.first_name,
      last_name: student.last_name,
      avatar_url: student.avatar_url,
      submissions_completed: submissions_completed,
      total_assignments: assignments.length,
      on_time_count: on_time_count,
      late_count: late_count,
      average_score_pct: total_max === 0 ? null : Math.round((total_score / total_max) * 100),
      last_active_at: last_submitted_at,
      week_on_time_count: week_on_time_count,
      week_late_count: week_late_count,
      week_total_count: week_total_count,
      week_completion_pct: week_completion_pct,
    };
  }

  // Per-assignment stats for the assignments section. INCLUDES departed
  // students' submissions (Mide, 9 May 2026): an assignment's historical
  // class mean shouldn't change just because a student left the class
  // afterwards. The roster (active members only) is computed elsewhere.
  function calcAssignmentStats(assignment, totalMemberCount, firstAttemptByKey) {
    let submissions_count = 0;
    let total_score = 0;
    let total_max = 0;

    // Iterate the full first-attempt index. Cost is O(rows × assignments)
    // but classes are small (<100 students × <50 assignments) so this is
    // fine and avoids building yet another bucketed map.
    firstAttemptByKey.forEach(function (sub, key) {
      if (key.indexOf(assignment.id + ':') !== 0) return;
      if (!sub.submitted_at) return;
      submissions_count += 1;
      if (sub.score != null && sub.max_score != null && sub.max_score > 0) {
        total_score += sub.score;
        total_max += sub.max_score;
      }
    });

    return {
      id: assignment.id,
      title: assignment.title,
      subject_id: assignment.subject_id,
      subject_name: assignment.subject ? assignment.subject.name : null,
      due_at: assignment.due_at,
      submissions_count: submissions_count,
      total_students: totalMemberCount,
      class_mean_pct: total_max === 0 ? null : Math.round((total_score / total_max) * 100),
    };
  }

  // Parse a "Wk N" tag out of an assignment title for sort purposes
  // (Phase 4c, 15 May 2026). Tagged titles sort by ascending week within
  // their subject; untagged titles fall through to MAX_SAFE_INTEGER so
  // they sort AFTER any tagged ones in the same subject — at which point
  // the final tiebreak (title.localeCompare) takes over. This is a
  // graceful degradation: real teacher-authored titles that don't follow
  // the "(Wk N)" pattern still produce a stable, predictable order.
  function parseWeekNumber(title) {
    const m = (title || '').match(/\(Wk (\d+)\)/i);
    return m ? parseInt(m[1], 10) : Number.MAX_SAFE_INTEGER;
  }

  // Compute the weekly Stars leaderboard. WEEKLY — resets each week
  // against the current window. ACTIVE members only; departed students
  // are excluded from the eligibility pool entirely.
  //
  // Stars locked model (Mide, 16 May 2026 — supersedes prior
  // "Logic A" naming). A student is eligible iff ALL of:
  //   1. Every this-week assignment submitted on time. On-time means
  //      submitted_at IS NOT NULL, submitted_at >= window.start_at,
  //      AND submitted_at <= assignment.due_at. Enforced via
  //      week_on_time_count === week_total_count.
  //   2. Overall this-week score_pct >= 75. Score is summed across
  //      this week's on-time first-attempt graded submissions
  //      (sum(score) / sum(max_score), rounded).
  //
  // Rank among eligible:
  //   1. score_pct DESC      (NULLs treated as -1 — defensive only;
  //                           the 75% gate guarantees a number)
  //   2. total_time_sec ASC  (NULLs treated as +∞ → sort last)
  //   3. first_name ASC
  //
  // INTERIM — assignment grain (Phase 4d, 16 May 2026): completion is
  // counted per assignment, not per question. The locked model targets
  // question grain (all 15 KS3 / 45 KS4 Combined / 15 KS4 Triple
  // questions) but assignment_question_attempts is empty and there's
  // no question_count column on assignments. Deferred to MRB-56 / Stage 4
  // (MRB-8). This is a decided, ticketed interim — see MRB-56 comment
  // (16 May 2026) — not an oversight.
  //
  // Returns the FULL ranked list of eligibles. Caller does .slice(0, 3)
  // for the top-3 podium — keeps the data layer dumb and lets the UI
  // re-rank or paginate without another query. Entry shape unchanged
  // from prior versions (on_time_count and total_this_week remain as
  // informational fields; the UI may ignore them).
  function calcLeaderboard(weekAssignments, students, week, firstAttemptByKey) {
    if (weekAssignments.length === 0) {
      return { eligible: [], is_empty: true, empty_reason: 'no_assignments_this_week' };
    }

    // Two-gate eligibility (Phase 4d locked model):
    //   (1) week_on_time_count === week_total_count — cheap upfront,
    //       short-circuits non-completers before the score walk.
    //   (2) score_pct >= 75 — applied after walking weekAssignments
    //       to accumulate this week's graded sum/max.
    // Score + total_time aggregates aren't on the roster output and
    // aren't needed elsewhere, so they stay local to this function.
    const eligible = [];
    students.forEach(function (s) {
      if (s.week_on_time_count !== s.week_total_count) return;

      let total_score = 0;
      let total_max = 0;
      let total_time_sec = 0;
      let any_time_present = false;

      weekAssignments.forEach(function (a) {
        const sub = firstAttemptByKey.get(a.id + ':' + s.id);
        if (!sub || !sub.submitted_at) return;
        if (sub.submitted_at < week.start_at) return;   // before window
        if (sub.submitted_at > a.due_at)      return;   // late — not on-time
        if (sub.score != null && sub.max_score != null && sub.max_score > 0) {
          total_score += sub.score;
          total_max += sub.max_score;
        }
        if (sub.total_time_seconds != null) {
          total_time_sec += sub.total_time_seconds;
          any_time_present = true;
        }
      });

      // Score gate (Stars locked model, Phase 4d). Compute once and reuse
      // in the entry below so the gate and the stored score_pct can never
      // disagree due to rounding.
      if (total_max === 0) return;                       // no graded subs
      const score_pct = Math.round((total_score / total_max) * 100);
      if (score_pct < 75) return;                        // 75% entry gate

      eligible.push({
        student_id: s.id,
        first_name: s.first_name,
        last_name: s.last_name,
        avatar_url: s.avatar_url,
        on_time_count: s.week_on_time_count,
        total_this_week: s.week_total_count,
        score_pct: score_pct,
        total_time_sec: any_time_present ? total_time_sec : null,
      });
    });

    if (eligible.length === 0) {
      return { eligible: [], is_empty: true, empty_reason: 'no_eligibles_yet' };
    }

    eligible.sort(function (a, b) {
      const aPct = a.score_pct == null ? -1 : a.score_pct;
      const bPct = b.score_pct == null ? -1 : b.score_pct;
      if (aPct !== bPct) return bPct - aPct;
      const aTime = a.total_time_sec == null ? Number.MAX_SAFE_INTEGER : a.total_time_sec;
      const bTime = b.total_time_sec == null ? Number.MAX_SAFE_INTEGER : b.total_time_sec;
      if (aTime !== bTime) return aTime - bTime;
      return (a.first_name || '').localeCompare(b.first_name || '');
    });

    return { eligible: eligible, is_empty: false, empty_reason: null };
  }

  async function loadTeacherClasses() {
    const guard = window.MrBadmusTeacherGuard;
    const sb = guard && guard.getClient ? guard.getClient() : null;
    if (!sb) {
      throw new Error('[teacher-data] Supabase client unavailable — getClient() returned null');
    }

    // Driver query: every (teacher, class, subject) link this teacher still
    // holds, with the class + subject embedded by FK. RLS filters to the
    // current teacher automatically. The .is('deleted_at', null) below is
    // the LINK row's own soft-delete column — i.e. we drop links that have
    // been retired. The class's own deleted_at is filtered in JS below
    // (PostgREST can't filter on embedded resources cleanly).
    const { data: links, error } = await sb
      .from('class_teachers')
      .select(
        'class_id, subject_id, ' +
        'subject:subject_id ( name ), ' +
        'class:class_id ( id, name, key_stage, year_group, tier, science_pathway, deleted_at )'
      )
      .is('deleted_at', null)
      .is('ended_at', null);

    if (error) {
      console.error('[teacher-data] driver query failed', error);
      throw error;
    }

    // Group by class_id, drop soft-deleted classes and orphans.
    const byClassId = new Map();
    (links || []).forEach(function (row) {
      if (!row.class) return;
      if (row.class.deleted_at) return;
      const id = row.class.id;
      if (!byClassId.has(id)) {
        byClassId.set(id, { klass: row.class, rows: [] });
      }
      byClassId.get(id).rows.push(row);
    });

    // For each unique class: derive pill, fetch metrics in parallel.
    const classIds = Array.from(byClassId.keys());
    const enriched = await Promise.all(classIds.map(async function (id) {
      const entry = byClassId.get(id);
      const klass = entry.klass;
      const pill = derivePill(klass, entry.rows);
      const metrics = await loadClassMetrics(sb, id);
      return {
        id: klass.id,
        name: klass.name,
        key_stage: klass.key_stage,
        year_group: klass.year_group,
        tier: klass.tier,
        science_pathway: klass.science_pathway,
        pill_label: pill.pill_label,
        pill_colour_var: pill.pill_colour_var,
        student_count: metrics.student_count,
        assignment_count: metrics.assignment_count,
        submission_count: metrics.submission_count,
        completion_pct: metrics.completion_pct,
        last_activity_at: metrics.last_activity_at,
      };
    }));

    // Sort by class.name ASC with natural-number ordering so "9A" comes
    // before "10A" (lexicographic alone would put "10A" first).
    enriched.sort(function (a, b) {
      return a.name.localeCompare(b.name, undefined, { numeric: true });
    });
    return enriched;
  }

  /**
   * loadClassDetail(classId) — data for the MRB-38 class-detail page.
   *
   * Single arg: classId (uuid string). Returns ONE object with the
   * shape below; never returns null. Throws an Error with a `.code`
   * property on every failure path; UI inspects code and renders the
   * matching state.
   *
   * Returned shape (snake_case to match loadTeacherClasses):
   *
   *   {
   *     class: {
   *       id, name, key_stage, year_group, tier, science_pathway,
   *       pill_label, pill_colour_var,                    // same rule as MRB-20
   *       student_count,                                  // active members
   *       assignment_count                                // active assignments
   *     },
   *     week: {
   *       start_at, end_at,                               // ISO, browser-local TZ
   *       anchor_day,                                     // 0..6 (postgres dow)
   *       anchor_source                                   // 'explicit' | 'fallback'
   *     },
   *     students: [                                       // ACTIVE members only
   *       {
   *         id, first_name, last_name, avatar_url,
   *         submissions_completed, total_assignments,    // ALL-TIME
   *         on_time_count,                                // ALL-TIME; due_at non-null AND submitted_at <= due_at
   *         late_count,                                   // ALL-TIME; due_at non-null AND submitted_at > due_at
   *         average_score_pct,                            // ALL-TIME; null if 0 graded subs
   *         last_active_at,                               // ALL-TIME; null if no submissions
   *         // THIS-WEEK (added Phase 4b.5, 12 May 2026) — drives the
   *         // "This Week" roster column AND leaderboard eligibility.
   *         // Early subs (submitted_at < week.start_at) are uncategorised:
   *         // neither on-time nor late.
   *         week_on_time_count, week_late_count,
   *         week_total_count,                             // == weekAssignments.length
   *         week_completion_pct                           // ((on_time+late)/total)*100 rounded; null if total===0
   *       }
   *     ],
   *     leaderboard: {
   *       eligible: [                                     // FULL ranked list
   *         {
   *           student_id, first_name, last_name, avatar_url,
   *           on_time_count, total_this_week,
   *           score_pct,                                  // null if 0 graded subs
   *           total_time_sec                              // null if all subs are time-null
   *         }
   *       ],
   *       is_empty: boolean,
   *       empty_reason:                                   // null when populated
   *         'no_assignments_this_week' | 'no_eligibles_yet' | null
   *     },
   *     assignments: [                                    // sort applied: due_at DESC NULLS LAST
   *       {
   *         id, title,
   *         subject_id, subject_name,                     // useful for KS4 Combined
   *         due_at,                                       // nullable
   *         submissions_count,                            // ALL-TIME, includes departed
   *         total_students,                               // ALL-TIME members count
   *         class_mean_pct                                // null if 0 graded subs
   *       }
   *     ]
   *   }
   *
   * Locked decisions (Mide, 9 May 2026 — see in-code comments at the
   * relevant helpers for full rationale):
   *   - First-attempt scoring: ignore retakes throughout (pickFirstAttempts)
   *   - Logic A eligibility: must complete ALL this-week assignments on-time
   *   - Departed students: count toward assignment stats, NOT roster
   *   - Window: browser local TZ (UK-only platform, v1 simplification)
   *
   * Error codes (thrown via Error.code):
   *   - invalid_class_id              — classId failed UUID shape check
   *   - not_authorised                — Q1 returned 0 rows (RLS or non-existent)
   *   - query_failed_class_teachers   — Q1 driver query errored
   *   - query_failed_class_members    — Q2 errored
   *   - query_failed_assignments      — Q3 errored
   *   - query_failed_submissions      — Q4 errored
   *
   * The shared/teacher-guard.js getClient() singleton must already exist
   * (the page contract loads guard before data); requireTeacherRole has
   * normally already validated the JWT before this function is called.
   */
  async function loadClassDetail(classId) {
    if (!isUuid(classId)) {
      const e = new Error('[teacher-data] invalid class id: ' + classId);
      e.code = 'invalid_class_id';
      throw e;
    }

    const guard = window.MrBadmusTeacherGuard;
    const sb = guard && guard.getClient ? guard.getClient() : null;
    if (!sb) {
      throw new Error('[teacher-data] Supabase client unavailable — getClient() returned null');
    }

    // ── Stage A — three parallel queries ─────────────────────────────
    // Q1: class_teachers (driver) — RLS scopes to the current teacher;
    //     0 rows => not a teacher of this class. Embeds the class itself
    //     and each row's subject for pill derivation.
    // Q2: class_members (ALL-TIME — no left_at filter) — splits into
    //     active vs departed in JS. Active drives the roster; all-time
    //     drives assignment stats.
    // Q3: assignments — used directly for the assignments list AND
    //     (after extracting ids) as the IN-filter for Q4.
    const [q1, q2, q3] = await Promise.all([
      sb.from('class_teachers')
        .select(
          'subject_id, ' +
          'subject:subject_id ( id, name ), ' +
          'class:class_id ( id, name, key_stage, year_group, tier, science_pathway, assignment_day_of_week, deleted_at )'
        )
        .eq('class_id', classId)
        .is('deleted_at', null)
        .is('ended_at', null),
      sb.from('class_members')
        .select(
          'id, student_id, left_at, ' +
          'student:student_id ( id, first_name, last_name, avatar_url, deleted_at )'
        )
        .eq('class_id', classId)
        .is('deleted_at', null),
      sb.from('assignments')
        .select(
          'id, title, due_at, subject_id, ' +
          'subject:subject_id ( id, name )'
        )
        .eq('class_id', classId)
        .is('deleted_at', null),
    ]);

    if (q1.error) {
      const e = new Error('[teacher-data] class_teachers query failed: ' + q1.error.message);
      e.code = 'query_failed_class_teachers';
      e.cause = q1.error;
      throw e;
    }
    // Filter out rows whose embedded class is null or soft-deleted (PostgREST
    // can't filter on the embedded resource). 0 rows => unauthorised.
    const teacherRows = (q1.data || []).filter(function (r) {
      return r.class && !r.class.deleted_at;
    });
    if (teacherRows.length === 0) {
      const e = new Error('[teacher-data] not authorised for class ' + classId);
      e.code = 'not_authorised';
      throw e;
    }

    if (q2.error) {
      const e = new Error('[teacher-data] class_members query failed: ' + q2.error.message);
      e.code = 'query_failed_class_members';
      e.cause = q2.error;
      throw e;
    }
    if (q3.error) {
      const e = new Error('[teacher-data] assignments query failed: ' + q3.error.message);
      e.code = 'query_failed_assignments';
      e.cause = q3.error;
      throw e;
    }

    const klass = teacherRows[0].class;

    // All members (active + departed); skip rows whose embedded student
    // profile is null/deleted (defensive — covers the soft-deleted-profile
    // race that PostgREST embed filtering can't catch).
    const allMembers = (q2.data || []).filter(function (m) {
      return m.student && !m.student.deleted_at;
    });
    const activeMembers = allMembers.filter(function (m) {
      return m.left_at == null;
    });

    const assignments = (q3.data || []);
    const assignmentIds = assignments.map(function (a) { return a.id; });

    // ── Stage B — Q4: submissions (only if there are assignments) ────
    // Skip the network round-trip entirely when assignmentIds is empty
    // (e.g. 9Y1's empty-state-B class). Keeps the function fast for the
    // empty case AND avoids sending PostgREST an empty `.in([])` filter.
    let submissions = [];
    if (assignmentIds.length > 0) {
      const q4 = await sb.from('assignment_submissions')
        .select('id, assignment_id, student_id, score, max_score, total_time_seconds, submitted_at, attempts')
        .in('assignment_id', assignmentIds)
        .is('deleted_at', null);

      if (q4.error) {
        const e = new Error('[teacher-data] assignment_submissions query failed: ' + q4.error.message);
        e.code = 'query_failed_submissions';
        e.cause = q4.error;
        throw e;
      }
      submissions = q4.data || [];
    }

    // ── Aggregate ─────────────────────────────────────────────────────
    const firstAttemptByKey = pickFirstAttempts(submissions);
    const pill = derivePill(klass, teacherRows);
    const week = computeWeekWindow(klass.assignment_day_of_week);
    // Filter once, share between calcStudentStats (per-student week
    // tally for the roster) and calcLeaderboard (eligibility + score
    // aggregates). due_at must be non-null AND within the half-open
    // window [start_at, end_at).
    const weekAssignments = assignments.filter(function (a) {
      return a.due_at && a.due_at >= week.start_at && a.due_at < week.end_at;
    });

    const students = activeMembers.map(function (m) {
      return calcStudentStats(m.student, assignments, weekAssignments, week, firstAttemptByKey);
    });

    const assignmentStats = assignments.map(function (a) {
      return calcAssignmentStats(a, allMembers.length, firstAttemptByKey);
    });

    // Sort assignments due_at DESC NULLS LAST (most-recent first; undated
    // ones at the bottom). Within a due_at group (or both-NULL), tiebreak
    // chain is: subject_name ASC → parseWeekNumber(title) ASC →
    // title.localeCompare ASC (Phase 4c, 15 May 2026). The subject sort
    // groups KS4 Combined's 12-row table by subject; the week sort orders
    // each subject Wk 1 → Wk N. Untagged titles fall through to the
    // title compare via MAX_SAFE_INTEGER (see parseWeekNumber).
    assignmentStats.sort(function (a, b) {
      // Primary: due_at DESC NULLS LAST
      if (a.due_at == null && b.due_at != null) return 1;
      if (b.due_at == null && a.due_at != null) return -1;
      if (a.due_at !== b.due_at) return a.due_at < b.due_at ? 1 : -1;
      // Tiebreak chain (same due_at, or both NULL):
      const sa = a.subject_name || '';
      const sb = b.subject_name || '';
      const subjectCmp = sa.localeCompare(sb);
      if (subjectCmp !== 0) return subjectCmp;
      const wa = parseWeekNumber(a.title);
      const wb = parseWeekNumber(b.title);
      if (wa !== wb) return wa - wb;
      return (a.title || '').localeCompare(b.title || '');
    });

    const leaderboard = calcLeaderboard(weekAssignments, students, week, firstAttemptByKey);

    return {
      class: {
        id: klass.id,
        name: klass.name,
        key_stage: klass.key_stage,
        year_group: klass.year_group,
        tier: klass.tier,
        science_pathway: klass.science_pathway,
        pill_label: pill.pill_label,
        pill_colour_var: pill.pill_colour_var,
        student_count: activeMembers.length,
        assignment_count: assignments.length,
      },
      week: week,
      students: students,
      leaderboard: leaderboard,
      assignments: assignmentStats,
    };
  }

  /**
   * loadStudentDetail(studentId, classId) — data for the MRB-34 Stage 2B
   * per-student detail page. Scoped to the (student, class) pair the URL
   * provides; reuses pickFirstAttempts + derivePill so first-attempt and
   * pill rules can't drift from loadClassDetail.
   *
   * Two args, both required. Both shape-validated; bad input throws an
   * invalid_* error code → page renders the notFound state.
   *
   * Returned shape:
   *   {
   *     class: {
   *       id, name, key_stage, year_group, tier, science_pathway,
   *       pill_label, pill_colour_var                  // MRB-20 rule
   *     },
   *     student: {
   *       id, first_name, last_name, avatar_url,
   *       science_pathway, tier, year_group            // for header meta
   *     },
   *     stats: {
   *       submissions_completed,                       // ALL-TIME, first-attempt, in-this-class
   *       on_time_count,                               // ALL-TIME on-time in-this-class
   *       average_score_pct,                           // null if 0 graded subs
   *       last_active_at                               // ISO; null if no subs
   *     },
   *     submission_history: [                          // first-attempt rows, submitted_at NOT NULL
   *       {
   *         id, assignment_id, title,
   *         subject_id, subject_name,
   *         due_at, submitted_at,
   *         score, max_score, score_pct,
   *         on_time                                    // bool; null when due_at null (uncategorised)
   *       }
   *     ],                                             // sort: submitted_at DESC
   *     class_has_multiple_subjects                    // drives subject-pill column visibility
   *   }
   *
   * Auth model — two checks, both must pass; the UI never differentiates
   * the two failure modes ("class you don't teach" vs "student not in
   * this class"), to avoid leaking class-membership info:
   *   (1) class_teachers — RLS scopes to the teacher; 0 rows → not_authorised
   *   (2) class_members — student must be a current member of THIS class
   *       (left_at IS NULL); 0 rows → not_authorised
   *   (3) profile fetch — RLS profiles_teacher_read_students enforces
   *       the same boundary at the DB layer; missing profile after both
   *       checks above is treated as not_authorised too (defensive — the
   *       UI never sees it under normal conditions).
   *
   * Error codes:
   *   - invalid_student_id           — studentId failed UUID shape check
   *   - invalid_class_id             — classId failed UUID shape check
   *   - not_authorised               — any auth check failed
   *   - query_failed_class_teachers  — Q1 errored
   *   - query_failed_class_members   — Q2 errored
   *   - query_failed_assignments     — Q3 errored
   *   - query_failed_student_profile — Q4 errored
   *   - query_failed_submissions     — Q5 errored
   */
  async function loadStudentDetail(studentId, classId) {
    if (!isUuid(studentId)) {
      const e = new Error('[teacher-data] invalid student id: ' + studentId);
      e.code = 'invalid_student_id';
      throw e;
    }
    if (!isUuid(classId)) {
      const e = new Error('[teacher-data] invalid class id: ' + classId);
      e.code = 'invalid_class_id';
      throw e;
    }

    const guard = window.MrBadmusTeacherGuard;
    const sb = guard && guard.getClient ? guard.getClient() : null;
    if (!sb) {
      throw new Error('[teacher-data] Supabase client unavailable — getClient() returned null');
    }

    // ── Stage A — four parallel queries ──────────────────────────────
    // Q1: class_teachers (driver). Same shape as loadClassDetail; gives
    //     us the class + teacher-subject rows for derivePill.
    // Q2: class_members. Filters to the (student, class) pair AND
    //     left_at IS NULL. 0 rows = student isn't currently in this class.
    // Q3: assignments — for this class; feeds submission stitching.
    // Q4: profile — RLS already scopes; we still .eq('id', studentId).
    const [q1, q2, q3, q4] = await Promise.all([
      sb.from('class_teachers')
        .select(
          'subject_id, ' +
          'subject:subject_id ( id, name ), ' +
          'class:class_id ( id, name, key_stage, year_group, tier, science_pathway, deleted_at )'
        )
        .eq('class_id', classId)
        .is('deleted_at', null)
        .is('ended_at', null),
      sb.from('class_members')
        .select('id, student_id, left_at')
        .eq('class_id', classId)
        .eq('student_id', studentId)
        .is('left_at', null)
        .is('deleted_at', null),
      sb.from('assignments')
        .select(
          'id, title, due_at, subject_id, ' +
          'subject:subject_id ( id, name )'
        )
        .eq('class_id', classId)
        .is('deleted_at', null),
      sb.from('profiles')
        .select('id, first_name, last_name, avatar_url, science_pathway, tier, year_group, deleted_at')
        .eq('id', studentId)
        .limit(1),
    ]);

    if (q1.error) {
      const e = new Error('[teacher-data] class_teachers query failed: ' + q1.error.message);
      e.code = 'query_failed_class_teachers';
      e.cause = q1.error;
      throw e;
    }
    const teacherRows = (q1.data || []).filter(function (r) {
      return r.class && !r.class.deleted_at;
    });
    if (teacherRows.length === 0) {
      const e = new Error('[teacher-data] not a teacher of class ' + classId);
      e.code = 'not_authorised';
      throw e;
    }

    if (q2.error) {
      const e = new Error('[teacher-data] class_members query failed: ' + q2.error.message);
      e.code = 'query_failed_class_members';
      e.cause = q2.error;
      throw e;
    }
    if ((q2.data || []).length === 0) {
      // Student isn't a current member of this class. Same error as the
      // "not your class" path so we don't leak membership info.
      const e = new Error('[teacher-data] student ' + studentId + ' not in class ' + classId);
      e.code = 'not_authorised';
      throw e;
    }

    if (q3.error) {
      const e = new Error('[teacher-data] assignments query failed: ' + q3.error.message);
      e.code = 'query_failed_assignments';
      e.cause = q3.error;
      throw e;
    }

    if (q4.error) {
      const e = new Error('[teacher-data] profile query failed: ' + q4.error.message);
      e.code = 'query_failed_student_profile';
      e.cause = q4.error;
      throw e;
    }
    const studentRow = (q4.data || []).find(function (p) { return !p.deleted_at; });
    if (!studentRow) {
      // RLS withheld the profile OR it's soft-deleted. After Q1+Q2 passed
      // this is very unlikely, but treat as not_authorised (undifferentiated)
      // rather than surface a confusing error state.
      const e = new Error('[teacher-data] profile unavailable for student ' + studentId);
      e.code = 'not_authorised';
      throw e;
    }

    const klass = teacherRows[0].class;
    const assignments = q3.data || [];
    const assignmentIds = assignments.map(function (a) { return a.id; });

    // ── Stage B — Q5: this student's submissions (skip round-trip if
    // the class has no assignments — same pattern as loadClassDetail).
    let submissions = [];
    if (assignmentIds.length > 0) {
      const q5 = await sb.from('assignment_submissions')
        .select('id, assignment_id, student_id, score, max_score, total_time_seconds, submitted_at, attempts')
        .in('assignment_id', assignmentIds)
        .eq('student_id', studentId)
        .is('deleted_at', null);

      if (q5.error) {
        const e = new Error('[teacher-data] assignment_submissions query failed: ' + q5.error.message);
        e.code = 'query_failed_submissions';
        e.cause = q5.error;
        throw e;
      }
      submissions = q5.data || [];
    }

    // ── Aggregate ─────────────────────────────────────────────────────
    const firstAttemptByKey = pickFirstAttempts(submissions);
    const pill = derivePill(klass, teacherRows);
    const assignmentById = {};
    assignments.forEach(function (a) { assignmentById[a.id] = a; });

    // Build submission_history. Filter to submitted_at NOT NULL — a row
    // with no submitted_at is "in progress, not yet submitted" and has
    // no Submitted/Score/On-time semantics to render.
    const submission_history = [];
    firstAttemptByKey.forEach(function (sub) {
      if (!sub.submitted_at) return;
      const a = assignmentById[sub.assignment_id];
      if (!a) return;
      const pct = (sub.score != null && sub.max_score != null && sub.max_score > 0)
        ? Math.round((sub.score / sub.max_score) * 100)
        : null;
      // on_time tri-state: true | false (when due_at present) | null (no due_at → uncategorised)
      let on_time = null;
      if (a.due_at) on_time = sub.submitted_at <= a.due_at;
      submission_history.push({
        id: sub.id,
        assignment_id: a.id,
        title: a.title,
        subject_id: a.subject_id,
        subject_name: a.subject ? a.subject.name : null,
        due_at: a.due_at,
        submitted_at: sub.submitted_at,
        score: sub.score,
        max_score: sub.max_score,
        score_pct: pct,
        on_time: on_time,
      });
    });
    // Sort submitted_at DESC. (No NULLS LAST tier: nulls already filtered above.)
    submission_history.sort(function (a, b) {
      if (a.submitted_at !== b.submitted_at) return a.submitted_at < b.submitted_at ? 1 : -1;
      return (a.title || '').localeCompare(b.title || '');
    });

    // At-a-glance stats — derived from submission_history so the page
    // and the stats can never disagree about what counts as a submission.
    let submissions_completed = 0;
    let on_time_count = 0;
    let total_score = 0;
    let total_max = 0;
    let last_active_at = null;
    submission_history.forEach(function (r) {
      submissions_completed += 1;
      if (r.on_time === true) on_time_count += 1;
      if (r.score != null && r.max_score != null && r.max_score > 0) {
        total_score += r.score;
        total_max += r.max_score;
      }
      if (last_active_at == null || r.submitted_at > last_active_at) {
        last_active_at = r.submitted_at;
      }
    });

    // Subject-pill column only when the class has >1 distinct subject
    // across its assignments. Mirrors class-detail.html's logic.
    const distinctSubjects = new Set(
      assignments.map(function (a) { return a.subject_id; }).filter(Boolean)
    );

    return {
      class: {
        id: klass.id,
        name: klass.name,
        key_stage: klass.key_stage,
        year_group: klass.year_group,
        tier: klass.tier,
        science_pathway: klass.science_pathway,
        pill_label: pill.pill_label,
        pill_colour_var: pill.pill_colour_var,
      },
      student: {
        id: studentRow.id,
        first_name: studentRow.first_name,
        last_name: studentRow.last_name,
        avatar_url: studentRow.avatar_url,
        science_pathway: studentRow.science_pathway,
        tier: studentRow.tier,
        year_group: studentRow.year_group,
      },
      stats: {
        submissions_completed: submissions_completed,
        on_time_count: on_time_count,
        average_score_pct: total_max === 0 ? null : Math.round((total_score / total_max) * 100),
        last_active_at: last_active_at,
      },
      submission_history: submission_history,
      class_has_multiple_subjects: distinctSubjects.size > 1,
    };
  }

  // ────────────────────────────────────────────────────────────────────
  // CLASS SHOUTOUTS (MRB-46 Phase 2)
  // ────────────────────────────────────────────────────────────────────
  // Three thin wrappers over Supabase JS for the teacher-side compose UI
  // (and the Phase 3 student-side read-only view, when it ships).
  //
  // RLS is the security boundary on all three calls — these just shape
  // the queries. See supabase/migrations/0009_class_shoutouts.sql for
  // the policy definitions (or post-MRB-84:
  // 20260524104500_class_shoutouts.sql).
  //
  // Profile joins disambiguate the two FKs on profiles via the explicit
  // constraint-name syntax: `profiles!<fk_name>(cols)`.

  /**
   * loadClassShoutouts(classId, opts)
   *
   * Page through shoutouts for a class, newest first, excluding soft-
   * deleted. Cursor-based on `created_at` so pagination is stable across
   * inserts (a new shoutout posted after the first page-fetch doesn't
   * shift the "next 20" window).
   *
   * Returns { shoutouts: [...], hasMore: boolean }.
   *
   * Each shoutout row carries:
   *   id, template_key, message, created_at, author_id, recipient_id,
   *   author:  { first_name, last_name, avatar_url } | null,
   *   recipient: { first_name, last_name, avatar_url } | null
   *
   * RLS gates the SELECT — teachers see only classes they teach;
   * students see only classes they're a member of. Soft-deleted rows
   * are also gated by the policy, but we add `.is('deleted_at', null)`
   * defensively so the client never relies on policy-only filtering.
   *
   * Throws on driver error. Caller renders the feed's error state.
   */
  async function loadClassShoutouts(classId, opts) {
    const limit            = (opts && opts.limit)            != null ? opts.limit            : 20;
    const beforeCreatedAt  = (opts && opts.beforeCreatedAt)  != null ? opts.beforeCreatedAt  : null;

    const guard = window.MrBadmusTeacherGuard;
    const sb = guard && guard.getClient ? guard.getClient() : null;
    if (!sb) {
      throw new Error('[teacher-data] Supabase client unavailable — getClient() returned null');
    }

    let q = sb
      .from('class_shoutouts')
      .select(
        'id, template_key, message, created_at, author_id, recipient_id, ' +
        'author:profiles!class_shoutouts_author_id_fkey ( first_name, last_name, avatar_url ), ' +
        'recipient:profiles!class_shoutouts_recipient_id_fkey ( first_name, last_name, avatar_url )'
      )
      .eq('class_id', classId)
      .is('deleted_at', null)
      .order('created_at', { ascending: false })
      .limit(limit);

    if (beforeCreatedAt) {
      q = q.lt('created_at', beforeCreatedAt);
    }

    const { data, error } = await q;
    if (error) {
      console.error('[teacher-data] loadClassShoutouts failed', error);
      throw error;
    }

    const shoutouts = data || [];
    return {
      shoutouts: shoutouts,
      hasMore: shoutouts.length === limit,
    };
  }

  /**
   * insertClassShoutout({ classId, authorId, recipientId, templateKey, message })
   *
   * Single INSERT. RLS enforces:
   *   - caller must teach this class
   *   - author_id must equal auth.uid()  (caller passes ctx.user.id)
   *   - recipient must be an active member of this class
   *   - school-scoped (defence-in-depth)
   *
   * Caller validates UI-side that at least one of templateKey/message is
   * non-null; the DB CHECK is the belt.
   *
   * Returns the inserted row (single object), with the same shape as a
   * loadClassShoutouts row (profile joins included), so the caller can
   * prepend it to the feed without a re-fetch if desired. We currently
   * re-fetch the feed on success — keeps the flow simple and avoids
   * cursor drift.
   *
   * Throws on driver/RLS error. Caller surfaces an inline error message.
   */
  async function insertClassShoutout(args) {
    const guard = window.MrBadmusTeacherGuard;
    const sb = guard && guard.getClient ? guard.getClient() : null;
    if (!sb) {
      throw new Error('[teacher-data] Supabase client unavailable — getClient() returned null');
    }

    const row = {
      class_id:     args.classId,
      author_id:    args.authorId,
      recipient_id: args.recipientId,
      template_key: args.templateKey || null,
      message:      args.message || null,
    };

    const { data, error } = await sb
      .from('class_shoutouts')
      .insert(row)
      .select(
        'id, template_key, message, created_at, author_id, recipient_id, ' +
        'author:profiles!class_shoutouts_author_id_fkey ( first_name, last_name, avatar_url ), ' +
        'recipient:profiles!class_shoutouts_recipient_id_fkey ( first_name, last_name, avatar_url )'
      )
      .single();

    if (error) {
      console.error('[teacher-data] insertClassShoutout failed', error);
      throw error;
    }
    return data;
  }

  /**
   * softDeleteClassShoutout(shoutoutId)
   *
   * Sets `deleted_at` on the row. RLS gates: only the author (and only
   * while they still teach the class) can UPDATE — see the
   * class_shoutouts_update policy.
   *
   * `deleted_at` is set client-side as an ISO timestamp. The actual
   * value isn't load-bearing — the SELECT policy and the partial index
   * both only check `IS NULL`. Server-side now() would be marginally
   * preferable but would require an RPC; not worth the indirection here.
   *
   * Throws on driver/RLS error.
   */
  async function softDeleteClassShoutout(shoutoutId) {
    const guard = window.MrBadmusTeacherGuard;
    const sb = guard && guard.getClient ? guard.getClient() : null;
    if (!sb) {
      throw new Error('[teacher-data] Supabase client unavailable — getClient() returned null');
    }

    // `.select('id')` forces RETURNING so we can detect silent RLS-USING
    // blocks. Without it, an UPDATE matched by USING=false returns
    // { data: null, error: null } — no error — and the caller has no
    // way to know the row didn't actually persist. Phase 2 discovery
    // (MRB-46): the soft-delete UPDATE could no-op without surfacing
    // anything to the user. Frontend would optimistically remove the
    // card and the teacher would only notice on refresh.
    //
    // Post-RETURNING, the author CAN see their own soft-deleted row
    // (per the 20260524195500_fix_class_shoutouts_soft_delete migration
    // — author-only visibility on deleted rows), so RETURNING works
    // for the legitimate caller and 0 rows reliably means a real block.
    const { data, error } = await sb
      .from('class_shoutouts')
      .update({ deleted_at: new Date().toISOString() })
      .eq('id', shoutoutId)
      .select('id');

    if (error) {
      console.error('[teacher-data] softDeleteClassShoutout failed', error);
      throw error;
    }
    if (!data || data.length === 0) {
      const e = new Error('No rows updated — RLS blocked the soft-delete (caller may not be the author, or no longer teaches this class).');
      e.code = 'no_rows_affected';
      console.error('[teacher-data] softDeleteClassShoutout silent no-op', { shoutoutId });
      throw e;
    }
  }

  return {
    loadTeacherClasses,
    loadClassDetail,
    loadStudentDetail,
    loadClassShoutouts,
    insertClassShoutout,
    softDeleteClassShoutout,
  };
})();
