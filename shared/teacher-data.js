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
 * (first-attempt scoring, departed-member handling,
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

  /* ── The working academic year (MRB-261) ────────────────────────────────
     ⊕ MRB-267, 19 Aug 2026 — THE COPY THAT LIVED HERE IS DELETED. There were
     three hand-synced implementations of this predicate (here, class-entry.js,
     teacher-data.js) and they had already drifted apart — identical logic,
     different `var`/`const`. A date rule that decides which year a student's
     classes belong to should have one answer, and hand-syncing three copies
     of it is a bug waiting for the 1st of September.

     `shared/class-entry.js` owns it and carries the full reasoning: never
     `is_current` (moved by hand on 1 Sep, so through late August it still
     points at the year that finished in July), and never a bare
     `end_date >= today` (academic years run to 31 August, so through the
     summer two are unfinished at once).

     ⚠️ RESOLVED AT CALL TIME, NOT AT LOAD TIME, and that is deliberate:
     class-entry.js is `defer`red on the pages that load it and this file is
     not, so it executes AFTER this one. Every call site here is behind an
     `await` on a Supabase query, by which point it is long since present.
     If it is genuinely absent the throw is loud — a missing module must not
     degrade into a silently wrong academic year, which would show a student
     last year's classes and look like data loss. */
  function workingAcademicYear(years) {
    const mod = window.MRBClassEntry;
    if (!mod || !mod.workingAcademicYear) {
      throw new Error(
        '[teacher-data] shared/class-entry.js is not loaded, and it owns ' +
        'workingAcademicYear(). Add it to this page BEFORE this file.');
    }
    return mod.workingAcademicYear(years);
  }

  /**
   * loadAcademicYears() — MRB-261.
   *
   * Every academic year the school has, newest first, each tagged with how it
   * stands relative to the working year. The teacher grid uses this twice: to
   * decide what to land on (always the working year, every load) and to build
   * the quiet "previous years" control at the foot of the grid.
   *
   * Returns { years: [{ id, name, start_date, end_date, is_working, is_past,
   *                     is_future }], working: <that row or null> }
   *
   * A year later than the working one is FUTURE, not past — a school that has
   * created 2027-28 early must not have it offered under "previous years".
   */
  async function loadAcademicYears() {
    const guard = window.MrBadmusTeacherGuard;
    const sb = guard && guard.getClient ? guard.getClient() : null;
    if (!sb) {
      throw new Error('[teacher-data] Supabase client unavailable — getClient() returned null');
    }

    const { data, error } = await sb
      .from('academic_years')
      .select('id, name, start_date, end_date')
      .is('deleted_at', null)
      .order('start_date', { ascending: false });
    if (error) {
      console.error('[teacher-data] academic years query failed', error);
      throw error;
    }

    const rows = data || [];
    const working = workingAcademicYear(rows);
    const years = rows.map(function (y) {
      return {
        id: y.id,
        name: y.name,
        start_date: y.start_date,
        end_date: y.end_date,
        is_working: !!working && y.id === working.id,
        is_past:    !!working && y.end_date < working.end_date,
        is_future:  !!working && y.end_date > working.end_date,
      };
    });
    return { years: years, working: working };
  }

  /* Decide the subject pill for a class, from the class's OWN subject.
     ⊕ MRB-263 (Mide, 19 Aug 2026) — IT USED TO READ `science_pathway`.

     The old rule branched on `klass.science_pathway`, and consulted the
     `class_teachers` rows only for KS4 Triple. `science_pathway` is
     nullable and is null on real classes — `10h/Sc2` and `11h/Sc5` in
     production carry no pathway at all — so those two cards rendered with
     NO PILL while the cards either side of them had one. Same screen, same
     kind of class, different treatment, for a reason invisible to whoever
     was reading it.

     The subject is now read from `class_teachers.subject_id`, which is the
     field that actually means "what this class is". It is populated and
     correct for all 15 production classes, needs no new data, and matches
     the naming convention exactly: KS3 → Science, `/Sc` → Combined
     Science, `/Ph` → Physics. Every card gets a pill, and no card differs
     from its neighbour except where the classes genuinely differ.

     The driver query in `loadTeacherClasses` already embeds `subject:
     subject_id ( name )` on every link row, so this costs no extra
     request — the data was arriving and being thrown away for three of
     the four branches.

     Multiple links to one class (a teacher who teaches it for two
     subjects) still resolve deterministically by lowest subject_id, which
     is the tie-break the Triple branch already used. */
  function derivePill(klass, teacherRowsForClass) {
    const sorted = (teacherRowsForClass || [])
      .filter(function (r) { return r.subject_id && r.subject && r.subject.name; })
      .slice()
      .sort(function (a, b) {
        if (a.subject_id < b.subject_id) return -1;
        if (a.subject_id > b.subject_id) return 1;
        return 0;
      });
    if (sorted.length === 0) return { pill_label: null, pill_colour_var: null };
    const name = sorted[0].subject.name;
    // Single-science subjects carry their own identity colour; Science and
    // Combined Science stay on the neutral `--science`, exactly as before.
    return { pill_label: name, pill_colour_var: SUBJECT_COLOUR_VARS[name] || 'var(--science)' };
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
      // Flag the failure so callers can render "—" / "couldn't load stats"
      // instead of presenting these zeros as if the class were genuinely empty.
      return Object.assign({}, zero, { metrics_failed: true });
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
    // In practice this case is rare (assignments don't open before
    // they're set), but the rule is here for production data
    // correctness. (It used to read "matches calcLeaderboard
    // semantics"; that function went under MRB-287.)
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

  /* Which of the four groups an assignment belongs in, for the teacher.
     ⊕ MRB-238 (Mide, 19 Aug 2026) — A TEACHER SEES EVERYTHING, ALWAYS.

     No assignment for a teacher's class is ever hidden from them by a date
     rule; knowing what is outstanding is the whole job of that screen. The
     table already listed every row — that part was already right — but it
     listed them as one undifferentiated run sorted by date, so "three
     people still owe me last Tuesday's work" and "this is set for
     September" sat in the same block looking the same.

       overdue   — the deadline has passed and somebody has still not
                   submitted. The only group that is a to-do list.
       this_week — deadline inside the current window and not yet passed.
       upcoming  — deadline beyond this week, or no deadline at all.
       past      — deadline passed and every student has submitted.
                   Finished, and out of the way.

     A class with no students has nothing outstanding by definition, so its
     past-deadline work is `past` rather than permanently `overdue`. */
  function assignmentDueGroup(a, week, nowIso) {
    if (!a.due_at) return 'upcoming';
    if (a.due_at >= week.end_at) return 'upcoming';
    if (a.due_at > nowIso) return 'this_week';
    const everyoneIn = a.total_students === 0 ||
                       a.submissions_count >= a.total_students;
    return everyoneIn ? 'past' : 'overdue';
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

  // ⊕ `calcLeaderboard` WAS HERE, AND WAS REMOVED — 24 Aug 2026, MRB-287.
  // Mide ruled that the Stars leaderboard is a STUDENT feature and is never
  // a teacher one. This function computed weekly Stars eligibility and rank
  // a SECOND time, in JavaScript, onto a payload key nothing ever read.
  //
  // The Stars rule now has exactly ONE implementation: the Supabase RPC
  // `class_stars_leaderboard_for_member`, read by `shared/student-data.js`.
  // So this deletes a DUPLICATED rule rather than creating a gap — there was
  // no part of the rule held here that the RPC does not also hold, and two
  // copies of an eligibility rule is precisely how the two drift apart.

  async function loadTeacherClasses(academicYearId) {
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
    // Which year's classes (MRB-261). Caller may name one — the grid does,
    // when a teacher has opened a past year — otherwise the working year.
    // The grid ALWAYS lands on the working year: nothing here is persisted,
    // so a teacher who looked at 2025-26 on Friday lands on 2026-27 on
    // Monday. Persisting it would silently hand someone a historical
    // dashboard they believed was current.
    let yearId = academicYearId || null;
    if (!yearId) {
      const y = await loadAcademicYears();
      yearId = y.working ? y.working.id : null;
    }

    const { data: links, error } = await sb
      .from('class_teachers')
      .select(
        'class_id, subject_id, ' +
        'subject:subject_id ( name ), ' +
        'class:class_id ( id, name, key_stage, year_group, tier, science_pathway, deleted_at, ' +
                         'academic_year_id, academic_year:academic_year_id ( id, name ) )'
      )
      .is('deleted_at', null)
      .is('ended_at', null);

    if (error) {
      console.error('[teacher-data] driver query failed', error);
      throw error;
    }

    // Group by class_id, drop soft-deleted classes, orphans, and — the point
    // of MRB-261 — anything outside the year being viewed. 10H/Ph1 (2025-26)
    // and 11h/Ph1 (2026-27) are the same 17 students a year apart, and with
    // both in one undifferentiated list they read as a duplicate.
    const byClassId = new Map();
    (links || []).forEach(function (row) {
      if (!row.class) return;
      if (row.class.deleted_at) return;
      if (yearId && row.class.academic_year_id !== yearId) return;
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
        academic_year_id: klass.academic_year_id,
        academic_year_name: (klass.academic_year && klass.academic_year.name) || null,
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
   *         // "This Week" roster column. (It also fed leaderboard
   *         // eligibility until MRB-287 removed calcLeaderboard.)
   *         // Early subs (submitted_at < week.start_at) are uncategorised:
   *         // neither on-time nor late.
   *         week_on_time_count, week_late_count,
   *         week_total_count,                             // == weekAssignments.length
   *         week_completion_pct                           // ((on_time+late)/total)*100 rounded; null if total===0
   *       }
   *     ],
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
          'class:class_id ( id, name, key_stage, year_group, tier, science_pathway, assignment_day_of_week, deleted_at, ' +
                          'academic_year_id, academic_year:academic_year_id ( id, name, end_date ) )'
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
    // The per-student week tally for the roster (calcStudentStats).
    // due_at must be non-null AND within the half-open window
    // [start_at, end_at). This filter used to be shared with
    // calcLeaderboard; that function went under MRB-287.
    const weekAssignments = assignments.filter(function (a) {
      return a.due_at && a.due_at >= week.start_at && a.due_at < week.end_at;
    });

    const students = activeMembers.map(function (m) {
      return calcStudentStats(m.student, assignments, weekAssignments, week, firstAttemptByKey);
    });

    const nowIso = new Date().toISOString();
    const assignmentStats = assignments.map(function (a) {
      const stat = calcAssignmentStats(a, allMembers.length, firstAttemptByKey);
      stat.due_group = assignmentDueGroup(stat, week, nowIso);
      return stat;
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

    // MRB-261 — is this class history? Same definition as loadAcademicYears'
    // is_past: its year ends before the working year does. A school with only
    // one year has that year as the working one, so nothing is ever falsely
    // read-only. A failed years read leaves the page writable (fail-open on a
    // presentation rule; the DB is the actual gate).
    //
    // ⊕ MRB-291, 26 Aug 2026 — READ BY NOTHING, AND THAT IS THE SETTLED
    // ANSWER, NOT AN OVERSIGHT. MRB-287's report already listed this under
    // "found and NOT fixed, deliberately"; MRB-291 re-checked every caller
    // and confirms it. The generated teacher pages do not read it. They take
    // the YEARS-LIST path: shared/teacher-live.js derives `viewingIsPast`
    // from the viewed year's own `is_past` and exports `canWrite` and
    // `readOnlyLine` from that one derivation, and every read-only ruling on
    // those pages (the WRAP that lifts the composer, the header's read-only
    // line, the shoutout `canDelete`) reads THOSE keys. That is the live
    // path.
    // ⚠️ DO NOT "FIX" THIS BY WIRING IT IN. A second derivation of "is this
    // year history" is how one page ends up with two answers — the drift
    // MRB-267 removed from `workingAcademicYear`. Kept rather than deleted
    // because `loadClassDetail` is a shared read that hand-written teacher
    // surfaces also call, and because deleting a field is how the reasoning
    // gets lost and the field comes back.
    let isPastYear = false;
    try {
      const y = await loadAcademicYears();
      const end = klass.academic_year && klass.academic_year.end_date;
      isPastYear = !!(y.working && end && end < y.working.end_date);
    } catch (e) {
      console.error('[teacher-data] academic years read failed; treating class as current', e);
    }

    return {
      class: {
        id: klass.id,
        name: klass.name,
        key_stage: klass.key_stage,
        year_group: klass.year_group,
        tier: klass.tier,
        science_pathway: klass.science_pathway,
        academic_year_id: klass.academic_year_id,
        academic_year_name: (klass.academic_year && klass.academic_year.name) || null,
        // MRB-261 — a past year is read-only. Computed here rather than on the
        // page so both the grid and the detail screen agree on what "past"
        // means, and so the answer travels with the class it describes.
        // ⊕ MRB-291 — no current reader. The generated pages use
        // teacher-live's `canWrite` / `readOnlyLine` instead; see the long
        // note at `isPastYear` above before wiring this to anything.
        is_past_year: isPastYear,
        pill_label: pill.pill_label,
        pill_colour_var: pill.pill_colour_var,
        student_count: activeMembers.length,
        assignment_count: assignments.length,
      },
      week: week,
      students: students,
      // Every assignment for the class, none withheld, each stamped with a
      // `due_group` of overdue | this_week | upcoming | past (MRB-238).
      assignments: assignmentStats,
    };
  }

  /**
   * loadClassProgress(classId) — how far into THIS week's assignment each
   * student actually is, live, from the backend.
   *
   * Single arg: classId (uuid string). Returns the parsed payload, or null.
   *
   *   {
   *     assignment: { id, class_id, title, topic, due_at, academic_week } | null,
   *     total,                                        // students in the class
   *     students: [
   *       {
   *         student_id, first_name, last_name,
   *         state,                                    // 'not_started' | 'in_progress' | 'complete'
   *         answered, total, percent,                 // QUESTIONS, not assignments
   *         attempts, completed_at, is_late,
   *         score, max_score
   *       }
   *     ],
   *     not_started, in_progress, complete
   *   }
   *
   * A week with no assignment set is a NORMAL, QUIET state, not a failure:
   * the route answers `{ assignment: null, total: 0, students: [],
   *                      reason: 'no_assignment_this_week' }`
   * with a 200, and it is returned as-is. The caller renders nothing extra.
   *
   * ⚠️ THIS IS THE FIRST CALL ON THIS PAGE THAT LEAVES SUPABASE. Everything
   * else in this file goes to PostgREST through the guard's client, where RLS
   * is the boundary; this one goes to the Render backend, so the session's
   * raw JWT has to be lifted out and sent as a Bearer token by hand. The route
   * is teacher-only and answers 403 to a student — the backend re-checks, this
   * is not a client-side gate.
   *
   * ⚠️ AND IT RETURNS null ON EVERY FAILURE PATH, DELIBERATELY — no throw, no
   * error code, unlike every other function here. The roster and the
   * assignments table both render from Supabase and both worked before
   * this route existed; a cold Render dyno, an expired token or a 500 must
   * cost the teacher one extra line of detail, never the page. The console
   * carries the reason for whoever is debugging it.
   */
  async function loadClassProgress(classId) {
    if (!isUuid(classId)) {
      console.error('[teacher-data] loadClassProgress: invalid class id', classId);
      return null;
    }

    const guard = window.MrBadmusTeacherGuard;
    const sb = guard && guard.getClient ? guard.getClient() : null;
    if (!sb) {
      console.error('[teacher-data] loadClassProgress: Supabase client unavailable — getClient() returned null');
      return null;
    }

    try {
      // getSession() reads the persisted session and refreshes it if it is
      // about to expire, so the token handed over is one the backend will
      // still accept. requireTeacherRole has normally already validated it.
      const { data, error } = await sb.auth.getSession();
      if (error) throw error;
      const token = data && data.session && data.session.access_token;
      if (!token) throw new Error('no access token on the current session');

      const cfg = window.MrBadmusConfig || {};
      const base = cfg.BACKEND_URL || 'https://mrbadmus-backend.onrender.com';
      const res = await fetch(
        base + '/api/class/progress?class_id=' + encodeURIComponent(classId),
        { headers: { Authorization: 'Bearer ' + token } }
      );
      if (!res.ok) {
        throw new Error('backend ' + res.status + ' on /api/class/progress');
      }
      return await res.json();
    } catch (e) {
      console.error('[teacher-data] loadClassProgress failed for class', classId, e);
      return null;
    }
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

    // Phase 3 v2: call the class_shoutouts_for_viewer RPC instead of a
    // direct PostgREST query with profile-FK joins. The RPC is SECURITY
    // DEFINER so it can resolve author + recipient first_name/last_name/
    // avatar_url across the RLS gap (teachers couldn't read OTHER
    // teachers' profiles via the FK join, which surfaced as em-dash
    // names on shoutouts authored by another teacher).
    //
    // Migration: 20260525093000_class_shoutouts_for_viewer.sql.
    // The RPC's membership/teaches gate matches the class_shoutouts
    // SELECT policy — same audience, no over-exposure.
    const { data, error } = await sb.rpc('class_shoutouts_for_viewer', {
      p_class_id:          classId,
      p_limit:             limit,
      p_before_created_at: beforeCreatedAt,
    });
    if (error) {
      console.error('[teacher-data] loadClassShoutouts (RPC) failed', error);
      throw error;
    }

    // RPC returns { shoutouts: [...], hasMore: boolean } directly as jsonb.
    const result = data || {};
    return {
      shoutouts: Array.isArray(result.shoutouts) ? result.shoutouts : [],
      hasMore:   !!result.hasMore,
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

  /* ══════════════════════════════════════════════════════════════════════
     MRB-287 — THE READS THE REDESIGNED TEACHER DASHBOARD NEEDS
     ══════════════════════════════════════════════════════════════════════

     Two functions, appended rather than folded into the ones above, because
     everything above answers ONE class at a time and the redesign's first
     screen is TWELVE classes at once. `loadClassDetail` × 12 is 48 round
     trips; `loadClassMatrices` over the same twelve is four (plus chunking).
     Nothing above changes — the class-detail page still calls what it always
     called, and if these two disagree with it that is a bug in these two.

     Neither of them aggregates. They hand back rows, first-attempt-filtered
     and authorisation-checked, and `shared/teacher-live.js` does the deriving.
     That split is deliberate: the redesign derives things this file has no
     opinion about (a mean of column means, a question grid, a teaching-week
     range), and burying those here would make this file the second place a
     number can be computed.                                                */

  /* PostgREST puts `.in()` lists in the QUERY STRING, and a query string has a
     length limit that is not ours to set — Supabase's edge sits behind a proxy
     that rejects long request lines with a 414 and no useful body. A uuid is
     37 characters with its comma, so 144 assignment ids is already ~5.3 KB of
     URL. This chunks the list, runs the chunks in parallel, and concatenates.

     100 is not a tuned number: it is ~3.7 KB of ids, comfortably under every
     limit in the chain, and small enough that a class list twice the size of
     anything real still only costs one extra round trip. */
  const IN_CHUNK = 100;

  async function inChunks(ids, run) {
    const list = (ids || []).filter(Boolean);
    if (list.length === 0) return [];
    const chunks = [];
    for (let i = 0; i < list.length; i += IN_CHUNK) {
      chunks.push(list.slice(i, i + IN_CHUNK));
    }
    const results = await Promise.all(chunks.map(run));
    let out = [];
    results.forEach(function (r) { out = out.concat(r); });
    return out;
  }

  /**
   * loadClassMatrices(classIds) — MRB-287.
   *
   * The raw material for the redesigned dashboard's student × assignment
   * grid, for MANY classes in one go. Every screen in the redesign derives
   * from this one read: the class cards' "submitted this week", the class
   * detail's week bar and roster, the digest's by-class table, and every
   * chart. One read means no two screens can disagree.
   *
   * Single arg: an array of class uuids. Returns an object keyed by class id:
   *
   *   {
   *     [classId]: {
   *       class: { id, name, key_stage, year_group, tier, science_pathway,
   *                assignment_day_of_week, academic_year_id,
   *                pill_label, pill_colour_var },   // MRB-20 rule, via derivePill
   *       week:  { start_at, end_at, anchor_day, anchor_source },
   *       members: [ { student_id, first_name, last_name, avatar_url,
   *                    joined_at } ],               // ACTIVE members only
   *       departed_count,                           // members with left_at set
   *       assignments: [ { id, title, due_at, created_at, academic_week,
   *                        subject_id, subject_name } ],
   *       submissions: [ { id, assignment_id, student_id, score, max_score,
   *                        submitted_at, completed_at, status, is_late,
   *                        attempts, attempt_no, total_time_seconds } ]
   *     }
   *   }
   *
   * `submissions` is ALREADY first-attempt-filtered through pickFirstAttempts,
   * so callers cannot forget the rule. It carries at most one row per
   * (assignment, student).
   *
   * ⚠️ THE ROSTER IS ACTIVE MEMBERS; THE SUBMISSIONS ARE EVERYONE'S. Same
   * split loadClassDetail makes, and for the same reason (Mide, 9 May 2026):
   * an assignment's historical mean must not move because a student left the
   * class in February. A caller building a per-student row should walk
   * `members`; a caller building a per-assignment column should walk
   * `submissions`. A submission whose student_id is not in `members` is a
   * departed student's and is not a bug.
   *
   * ⚠️ pickFirstAttempts TIEBREAKS ON `attempts`, NOT `attempt_no`. Both
   * columns are selected and both are returned. The per-answer writer added
   * on 22 Aug 2026 sets `attempt_no` and leaves `attempts` at its default, so
   * for rows written by that path every candidate ties on `attempts` and the
   * pick falls through to submitted_at — where an in-progress row's NULL is
   * treated as worst, so a COMPLETED first attempt still wins over an
   * in-progress retake. That is the right answer, but it is the right answer
   * by accident of the tiebreak rather than by design, and it is written down
   * here so the next person to touch the picker knows both columns are live.
   *
   * Authorisation: the class_teachers driver query is RLS-scoped to the
   * caller. A class id that comes back with no row is one the caller does not
   * teach, and the whole call fails rather than quietly omitting it — a
   * dashboard that silently drops a class looks identical to a teacher who
   * has been taken off it.
   *
   * Error codes (thrown via Error.code):
   *   - invalid_class_id             — an id failed the UUID shape check
   *   - not_authorised               — a requested class returned no driver row
   *   - query_failed_class_teachers  — driver query errored
   *   - query_failed_class_members   — members query errored
   *   - query_failed_assignments     — assignments query errored
   *   - query_failed_submissions     — submissions query errored
   */
  async function loadClassMatrices(classIds) {
    const ids = Array.from(new Set((classIds || []).filter(Boolean)));
    ids.forEach(function (id) {
      if (!isUuid(id)) {
        const e = new Error('[teacher-data] invalid class id: ' + id);
        e.code = 'invalid_class_id';
        throw e;
      }
    });
    if (ids.length === 0) return {};

    const guard = window.MrBadmusTeacherGuard;
    const sb = guard && guard.getClient ? guard.getClient() : null;
    if (!sb) {
      throw new Error('[teacher-data] Supabase client unavailable — getClient() returned null');
    }

    // ── Stage A — three parallel reads, each chunked over the id list ──
    let links, memberRows, assignmentRows;
    try {
      const [a, b, c] = await Promise.all([
        inChunks(ids, async function (chunk) {
          const r = await sb.from('class_teachers')
            .select(
              'class_id, subject_id, ' +
              'subject:subject_id ( id, name ), ' +
              'class:class_id ( id, name, key_stage, year_group, tier, science_pathway, ' +
                              'assignment_day_of_week, deleted_at, academic_year_id )'
            )
            .in('class_id', chunk)
            .is('deleted_at', null)
            .is('ended_at', null);
          if (r.error) { r.error.__stage = 'class_teachers'; throw r.error; }
          return r.data || [];
        }),
        inChunks(ids, async function (chunk) {
          const r = await sb.from('class_members')
            .select(
              'class_id, student_id, joined_at, left_at, ' +
              'student:student_id ( id, first_name, last_name, avatar_url, deleted_at )'
            )
            .in('class_id', chunk)
            .is('deleted_at', null);
          if (r.error) { r.error.__stage = 'class_members'; throw r.error; }
          return r.data || [];
        }),
        inChunks(ids, async function (chunk) {
          const r = await sb.from('assignments')
            .select(
              'id, class_id, title, due_at, created_at, academic_week, subject_id, ' +
              'subject:subject_id ( id, name )'
            )
            .in('class_id', chunk)
            .is('deleted_at', null);
          if (r.error) { r.error.__stage = 'assignments'; throw r.error; }
          return r.data || [];
        }),
      ]);
      links = a; memberRows = b; assignmentRows = c;
    } catch (err) {
      const stage = err && err.__stage ? err.__stage : 'class_teachers';
      const e = new Error('[teacher-data] ' + stage + ' query failed: ' + (err && err.message));
      e.code = 'query_failed_' + stage;
      e.cause = err;
      throw e;
    }

    // Group the driver rows, dropping soft-deleted classes (PostgREST cannot
    // filter an embedded resource, so it is done here — same as everywhere
    // else in this file).
    const byClassId = new Map();
    links.forEach(function (row) {
      if (!row.class || row.class.deleted_at) return;
      const id = row.class.id;
      if (!byClassId.has(id)) byClassId.set(id, { klass: row.class, rows: [] });
      byClassId.get(id).rows.push(row);
    });

    const missing = ids.filter(function (id) { return !byClassId.has(id); });
    if (missing.length) {
      const e = new Error('[teacher-data] not authorised for class(es): ' + missing.join(', '));
      e.code = 'not_authorised';
      e.classIds = missing;
      throw e;
    }

    // ── Stage B — submissions for every assignment across every class ──
    const assignmentIds = assignmentRows.map(function (a) { return a.id; });
    let submissionRows = [];
    if (assignmentIds.length > 0) {
      try {
        submissionRows = await inChunks(assignmentIds, async function (chunk) {
          const r = await sb.from('assignment_submissions')
            .select('id, assignment_id, student_id, score, max_score, total_time_seconds, ' +
                    'submitted_at, completed_at, status, is_late, attempts, attempt_no')
            .in('assignment_id', chunk)
            .is('deleted_at', null);
          if (r.error) throw r.error;
          return r.data || [];
        });
      } catch (err) {
        const e = new Error('[teacher-data] assignment_submissions query failed: ' + (err && err.message));
        e.code = 'query_failed_submissions';
        e.cause = err;
        throw e;
      }
    }

    // ── Assemble, per class ────────────────────────────────────────────
    const membersByClass = new Map();
    const departedByClass = new Map();
    memberRows.forEach(function (m) {
      // Defensive: skip rows whose embedded profile is null or soft-deleted.
      // Covers the soft-deleted-profile race PostgREST embed filtering can't.
      if (!m.student || m.student.deleted_at) return;
      if (m.left_at != null) {
        departedByClass.set(m.class_id, (departedByClass.get(m.class_id) || 0) + 1);
        return;
      }
      if (!membersByClass.has(m.class_id)) membersByClass.set(m.class_id, []);
      membersByClass.get(m.class_id).push({
        student_id: m.student.id,
        first_name: m.student.first_name,
        last_name: m.student.last_name,
        avatar_url: m.student.avatar_url,
        joined_at: m.joined_at,
      });
    });

    const assignmentsByClass = new Map();
    const classOfAssignment = new Map();
    assignmentRows.forEach(function (a) {
      classOfAssignment.set(a.id, a.class_id);
      if (!assignmentsByClass.has(a.class_id)) assignmentsByClass.set(a.class_id, []);
      assignmentsByClass.get(a.class_id).push({
        id: a.id,
        title: a.title,
        due_at: a.due_at,
        created_at: a.created_at,
        academic_week: a.academic_week,
        subject_id: a.subject_id,
        subject_name: a.subject ? a.subject.name : null,
      });
    });

    // ONE first-attempt pass over every class's submissions at once. The key
    // is (assignment, student) and an assignment belongs to exactly one class,
    // so classes cannot collide in the map.
    const firstAttemptByKey = pickFirstAttempts(submissionRows);
    const submissionsByClass = new Map();
    firstAttemptByKey.forEach(function (sub) {
      const cid = classOfAssignment.get(sub.assignment_id);
      if (!cid) return;
      if (!submissionsByClass.has(cid)) submissionsByClass.set(cid, []);
      submissionsByClass.get(cid).push(sub);
    });

    const out = {};
    byClassId.forEach(function (entry, id) {
      const klass = entry.klass;
      const pill = derivePill(klass, entry.rows);
      out[id] = {
        class: {
          id: klass.id,
          name: klass.name,
          key_stage: klass.key_stage,
          year_group: klass.year_group,
          tier: klass.tier,
          science_pathway: klass.science_pathway,
          assignment_day_of_week: klass.assignment_day_of_week,
          academic_year_id: klass.academic_year_id,
          pill_label: pill.pill_label,
          pill_colour_var: pill.pill_colour_var,
        },
        week: computeWeekWindow(klass.assignment_day_of_week),
        members: membersByClass.get(id) || [],
        departed_count: departedByClass.get(id) || 0,
        assignments: assignmentsByClass.get(id) || [],
        submissions: submissionsByClass.get(id) || [],
      };
    });
    return out;
  }

  /**
   * loadPaperQuestions(assignmentIds) — MRB-287.
   *
   * What each student answered, question by question, for a set of
   * assignments. This is the read behind the marking screen's class ×
   * question grid and its question breakdown, and there was no path to it
   * before: everything above this line stops at the submission's total.
   *
   * Single arg: an array of assignment uuids. Returns an object keyed by
   * assignment id:
   *
   *   {
   *     [assignmentId]: {
   *       questions: [ { position, source_ref, rung } ],   // position ASC
   *       submissions: [ { id, student_id, score, max_score, status,
   *                        submitted_at, completed_at, is_late } ],
   *       attempts: [ { submission_id, question_index, question_ref,
   *                     question_text, rung, selected_answer, correct_answer,
   *                     selected_option_letter, correct_option_letter,
   *                     is_correct } ]
   *     }
   *   }
   *
   * `submissions` is first-attempt-filtered, and `attempts` is filtered to
   * those submissions — an abandoned retake's answers must not appear in a
   * grid whose marks come from the first attempt.
   *
   * ⚖️ `is_correct` IS NULLABLE AND NULL IS NOT FALSE. Self-marked and
   * written responses record no correctness claim: the platform cannot know,
   * because a student can tick every criterion on gibberish. The column's own
   * comment says so, and the NOT NULL was dropped on 20 Aug 2026 precisely so
   * an honest row could be written. A caller that renders NULL as a cross, or
   * counts it as a zero, is asserting something the database deliberately
   * refuses to assert. Returned as-is; the caller must give it its own state.
   *
   * ⚠️ THERE IS NO CLEAN JOIN FROM AN ATTEMPT TO ITS `assignment_questions`
   * ROW, and pretending otherwise is the trap here. `assignment_questions`
   * carries `source_ref` — a LESSON path plus a rung — while an attempt
   * carries `question_ref`, the bank's per-question id. They are different
   * namespaces on purpose (see 20260820140008's comment: "a rung name is a
   * difficulty, not a question"). The only thing that lines the two up is
   * ORDER: `question_index` is the 0-based index into the questions as the
   * student was served them, and the server serves them `position` ASC. So
   * `questions` comes back sorted and the caller joins by ordinal. It is
   * returned unjoined rather than joined-here because the fallback when the
   * ordinals do not line up is a display decision, not a data one.
   *
   * ⚠️ `rung` IS RETURNED AND MUST NOT BE AGGREGATED ON. It is here because
   * it is the only descriptor a question row carries, and a caller may want
   * to label one question with it. Grouping by it — a recall-versus-apply
   * split, a per-rung mean, a breakdown of any kind — is out, ruled: the
   * recall round records nothing yet, so any such split would be drawn from
   * one corpus and read as if it covered both.
   *
   * Authorisation is RLS's, through `attempts_teacher_read`, which follows
   * the submission to its assignment to `auth_user_teaches_class`. Unlike
   * loadClassMatrices there is no separate driver check: an assignment the
   * caller does not teach simply returns nothing at every stage, and the
   * caller reached this function through a class it had already been
   * authorised for.
   *
   * Error codes:
   *   - invalid_assignment_id          — an id failed the UUID shape check
   *   - query_failed_assignment_questions
   *   - query_failed_submissions
   *   - query_failed_question_attempts
   */
  async function loadPaperQuestions(assignmentIds) {
    const ids = Array.from(new Set((assignmentIds || []).filter(Boolean)));
    ids.forEach(function (id) {
      if (!isUuid(id)) {
        const e = new Error('[teacher-data] invalid assignment id: ' + id);
        e.code = 'invalid_assignment_id';
        throw e;
      }
    });
    if (ids.length === 0) return {};

    const guard = window.MrBadmusTeacherGuard;
    const sb = guard && guard.getClient ? guard.getClient() : null;
    if (!sb) {
      throw new Error('[teacher-data] Supabase client unavailable — getClient() returned null');
    }

    let questionRows, submissionRows;
    try {
      const [a, b] = await Promise.all([
        inChunks(ids, async function (chunk) {
          const r = await sb.from('assignment_questions')
            .select('assignment_id, position, source_ref, rung')
            .in('assignment_id', chunk)
            .order('position', { ascending: true });
          if (r.error) { r.error.__stage = 'assignment_questions'; throw r.error; }
          return r.data || [];
        }),
        inChunks(ids, async function (chunk) {
          const r = await sb.from('assignment_submissions')
            .select('id, assignment_id, student_id, score, max_score, ' +
                    'submitted_at, completed_at, status, is_late, attempts, attempt_no')
            .in('assignment_id', chunk)
            .is('deleted_at', null);
          if (r.error) { r.error.__stage = 'submissions'; throw r.error; }
          return r.data || [];
        }),
      ]);
      questionRows = a; submissionRows = b;
    } catch (err) {
      const stage = err && err.__stage ? err.__stage : 'assignment_questions';
      const e = new Error('[teacher-data] ' + stage + ' query failed: ' + (err && err.message));
      e.code = 'query_failed_' + stage;
      e.cause = err;
      throw e;
    }

    // First attempts only, and the attempt rows are fetched for THOSE
    // submission ids alone. Fetching all of them and filtering afterwards
    // would pull an abandoned retake's answers over the wire to throw away.
    const firstAttemptByKey = pickFirstAttempts(submissionRows);
    const keptSubs = [];
    firstAttemptByKey.forEach(function (s) { keptSubs.push(s); });
    const keptIds = keptSubs.map(function (s) { return s.id; });

    let attemptRows = [];
    if (keptIds.length > 0) {
      try {
        attemptRows = await inChunks(keptIds, async function (chunk) {
          const r = await sb.from('assignment_question_attempts')
            .select('submission_id, question_index, question_ref, question_text, rung, ' +
                    'selected_answer, correct_answer, selected_option_letter, ' +
                    'correct_option_letter, is_correct')
            .in('submission_id', chunk)
            .order('question_index', { ascending: true });
          if (r.error) throw r.error;
          return r.data || [];
        });
      } catch (err) {
        const e = new Error('[teacher-data] assignment_question_attempts query failed: ' + (err && err.message));
        e.code = 'query_failed_question_attempts';
        e.cause = err;
        throw e;
      }
    }

    const subById = new Map();
    keptSubs.forEach(function (s) { subById.set(s.id, s); });

    const out = {};
    ids.forEach(function (id) { out[id] = { questions: [], submissions: [], attempts: [] }; });

    questionRows.forEach(function (q) {
      if (!out[q.assignment_id]) return;
      out[q.assignment_id].questions.push({
        position: q.position,
        source_ref: q.source_ref,
        rung: q.rung,
      });
    });
    // `.order()` is applied per chunk, so re-sort once the chunks are merged.
    ids.forEach(function (id) {
      out[id].questions.sort(function (a, b) { return a.position - b.position; });
    });

    keptSubs.forEach(function (s) {
      if (!out[s.assignment_id]) return;
      out[s.assignment_id].submissions.push({
        id: s.id,
        student_id: s.student_id,
        score: s.score,
        max_score: s.max_score,
        status: s.status,
        submitted_at: s.submitted_at,
        completed_at: s.completed_at,
        is_late: s.is_late,
      });
    });

    attemptRows.forEach(function (a) {
      const sub = subById.get(a.submission_id);
      if (!sub || !out[sub.assignment_id]) return;
      out[sub.assignment_id].attempts.push(a);
    });

    return out;
  }

  return {
    loadAcademicYears,
    loadTeacherClasses,
    loadClassDetail,
    loadClassProgress,
    loadStudentDetail,
    loadClassShoutouts,
    insertClassShoutout,
    softDeleteClassShoutout,
    // MRB-287 — the redesigned dashboard's two reads. Additive: nothing
    // above changed, and no existing caller sees a difference.
    loadClassMatrices,
    loadPaperQuestions,
  };
})();
