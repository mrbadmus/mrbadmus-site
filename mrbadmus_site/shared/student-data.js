/**
 * shared/student-data.js — Student dashboard data layer
 *
 * Page contract (load AFTER student-guard.js + shoutouts.js):
 *   <script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2/dist/umd/supabase.min.js"></script>
 *   <script src="/shared/config.js"></script>
 *   <script src="/shared/student-guard.js"></script>
 *   <script src="/shared/shoutouts.js"></script>
 *   <script src="/shared/student-data.js"></script>
 *   <script>
 *     MrBadmusStudentGuard.requireStudentRole({
 *       onAllowed: async function ({ user }) {
 *         const detail = await MrBadmusStudentData.loadStudentClass(classId, user.id);
 *         // render
 *       },
 *     });
 *   </script>
 *
 * Parallel module to shared/teacher-data.js for the same architectural
 * reason that the guards are parallel: separate role-shaped data layers,
 * clear ownership, no piling on a ~1100-line file.
 *
 * Exports:
 *   loadStudentClass(classId, viewingStudentId) — bundle for the page
 *   loadStudentClassShoutouts(classId, opts)     — paginated read-only feed
 *
 * Error codes thrown by loadStudentClass (UI matches state from .code):
 *   'invalid_class_id'  — caller-provided classId isn't a UUID
 *   'not_authorised'    — viewer is not an active member of this class
 *   'class_not_found'   — class doesn't exist or is soft-deleted (and
 *                          viewer was a member, so RLS didn't hide it)
 *   (other errors propagate; UI renders generic error state)
 *
 * RLS notes (Phase 3A recon):
 *   - assignment_submissions.submissions_self_all restricts students
 *     to their own submissions — so viewer stats are computable
 *     client-side from raw rows, but the LEADERBOARD is NOT.
 *   - The leaderboard is loaded via the SECURITY DEFINER RPC
 *     class_stars_leaderboard_for_member(p_class_id) added in
 *     20260524225500_class_stars_leaderboard_for_member.sql.
 *   - The function membership-gates internally — non-members get
 *     { eligible: [], is_empty: true, empty_reason: 'not_member' }.
 *
 * Subject pill rule (student variant — simpler than teacher's):
 *   KS3                  → 'Science'          / var(--science)
 *   KS4 + combined       → 'Combined Science' / var(--science)
 *   KS4 + triple         → 'Triple Science'   / var(--science)
 *                          (teacher view picks a per-subject colour
 *                           by reading class_teachers; students can't
 *                           read that table. v1 ships neutral; if Mide
 *                           wants per-subject for Triple students later,
 *                           we add a primary_subject_id column on
 *                           classes or a SECURITY DEFINER helper.)
 *   anything else (KS5)  → null pill
 */

window.MrBadmusStudentData = (function () {

  // Shape-only UUID check — same idiom as teacher-data.js.
  function isUuid(s) {
    return typeof s === 'string' &&
      /^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/i.test(s);
  }

  // Student-side pill derivation. See JSDoc above.
  function deriveStudentPill(klass) {
    if (klass.key_stage === 'KS3') {
      return { pill_label: 'Science', pill_colour_var: 'var(--science)' };
    }
    if (klass.key_stage === 'KS4' && klass.science_pathway === 'combined') {
      return { pill_label: 'Combined Science', pill_colour_var: 'var(--science)' };
    }
    if (klass.key_stage === 'KS4' && klass.science_pathway === 'triple') {
      return { pill_label: 'Triple Science', pill_colour_var: 'var(--science)' };
    }
    return { pill_label: null, pill_colour_var: null };
  }

  // Subject-colour top stripe (Phase 3 visual differentiator). Currently
  // all-classes get the neutral science colour for the same RLS reason
  // (students can't read class_teachers to derive a per-subject colour
  // for Triple classes). Single-subject KS4 Triple classes — those whose
  // class.name encodes a subject like "Physics" — would deserve their
  // own colour; v2 work, not Phase 3.
  function deriveStripeColourVar(klass) {
    return 'var(--science)';
  }

  // Week window — same algorithm as teacher-data.js's computeWeekWindow.
  // Browser-LOCAL time (matches UK-AQA user expectation). Anchor day from
  // class.assignment_day_of_week, default Monday (1) when NULL.
  function computeWeekWindow(assignmentDayOfWeek) {
    const isFallback = (assignmentDayOfWeek === null || assignmentDayOfWeek === undefined);
    const anchor_day = isFallback ? 1 : assignmentDayOfWeek;
    const now = new Date();
    const today = now.getDay();
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
      anchor_source: isFallback ? 'fallback' : 'explicit',
    };
  }

  // First-attempt rule (same as teacher-data.js). Lower 'attempts' wins;
  // earlier 'submitted_at' breaks ties; NULLs treated as worst.
  function pickFirstAttempts(submissions) {
    const byKey = new Map();
    (submissions || []).forEach(function (s) {
      if (!s.assignment_id || !s.student_id) return;
      const key = s.assignment_id + ':' + s.student_id;
      const existing = byKey.get(key);
      if (!existing) { byKey.set(key, s); return; }
      const ea = existing.attempts == null ? Number.MAX_SAFE_INTEGER : existing.attempts;
      const na = s.attempts        == null ? Number.MAX_SAFE_INTEGER : s.attempts;
      if (na < ea) { byKey.set(key, s); return; }
      if (na === ea) {
        const ets = existing.submitted_at || '￿';
        const nts = s.submitted_at        || '￿';
        if (nts < ets) byKey.set(key, s);
      }
    });
    return byKey;
  }

  // Subject name → CSS var; mirrors teacher-data.js's lookup. Used for
  // assignment cards in the "Due this week" section.
  const SUBJECT_COLOUR_VARS = {
    Biology:   'var(--biology)',
    Chemistry: 'var(--chemistry)',
    Physics:   'var(--physics)',
  };
  function subjectColourVar(subjectName) {
    return SUBJECT_COLOUR_VARS[subjectName] || 'var(--science)';
  }

  /**
   * loadStudentClass(classId, viewingStudentId)
   *
   * Loads the bundle for /student/class.html. Two-step gate to
   * differentiate notAuthorised (not a member) from notFound (class
   * doesn't exist or is soft-deleted):
   *
   *   1. Check class_members.student_id = viewer + class_id = X.
   *      No row → not_authorised (the membership query is RLS-gated
   *      to the viewer's own rows; non-membership = no row).
   *   2. SELECT class. No row → class_not_found.
   *
   * Then in parallel: assignments + own submissions + RPC leaderboard.
   *
   * Returns:
   *   {
   *     class: { id, name, key_stage, year_group, tier, science_pathway,
   *              pill_label, pill_colour_var, stripe_colour_var,
   *              assignment_day_of_week },
   *     viewer: { id, first_name, last_name, avatar_url },
   *     viewerStats: { assignments_in_class_count, submissions_completed,
   *                    on_time_count, average_score_pct,
   *                    submissions_completed_pct },
   *     assignmentsDueThisWeek: [
   *       { id, title, subject_id, subject_name, subject_colour_var,
   *         due_at, is_submitted, score, max_score, on_time }
   *     ],
   *     leaderboard: { eligible, is_empty, empty_reason },
   *     viewerOnPodium: boolean,   // viewer in leaderboard.eligible
   *     week: { start_at, end_at, anchor_day, anchor_source },
   *   }
   */
  async function loadStudentClass(classId, viewingStudentId) {
    if (!isUuid(classId)) {
      const e = new Error('Invalid class id');
      e.code = 'invalid_class_id';
      throw e;
    }

    const guard = window.MrBadmusStudentGuard;
    const sb = guard && guard.getClient ? guard.getClient() : null;
    if (!sb) {
      throw new Error('[student-data] Supabase client unavailable — getClient() returned null');
    }

    // 1. Membership gate — RLS-scoped to viewer's own rows; if they're
    // not a member, the query returns zero rows. We treat that as
    // not_authorised (cleanly differentiated from class_not_found below).
    const memberRes = await sb
      .from('class_members')
      .select('id, joined_at, left_at, deleted_at')
      .eq('class_id', classId)
      .eq('student_id', viewingStudentId)
      .is('left_at', null)
      .is('deleted_at', null)
      .limit(1);
    if (memberRes.error) {
      console.error('[student-data] membership query failed', memberRes.error);
      throw memberRes.error;
    }
    if (!memberRes.data || memberRes.data.length === 0) {
      const e = new Error('Not authorised — viewer is not an active member of this class');
      e.code = 'not_authorised';
      throw e;
    }

    // 2. Class fetch — RLS allows since viewer is a member. If the row
    // is missing, the class was soft-deleted between member-join and now
    // (or never existed but the membership row leaked somehow — defensive).
    const classRes = await sb
      .from('classes')
      .select('id, name, key_stage, year_group, tier, science_pathway, assignment_day_of_week, deleted_at')
      .eq('id', classId)
      .is('deleted_at', null)
      .single();
    if (classRes.error || !classRes.data) {
      // PostgREST returns code PGRST116 when .single() finds 0 rows.
      if (classRes.error && classRes.error.code === 'PGRST116') {
        const e = new Error('Class not found or soft-deleted');
        e.code = 'class_not_found';
        throw e;
      }
      console.error('[student-data] class fetch failed', classRes.error);
      throw classRes.error || new Error('class fetch returned no row');
    }
    const klass = classRes.data;

    // 3. Viewer's profile (for "Hi, [first_name]" greeting). Could be
    // pulled from the auth/profile in the guard's onAllowed, but we
    // fetch fresh here to keep this module self-contained.
    const viewerProfileRes = await sb
      .from('profiles')
      .select('id, first_name, last_name, avatar_url')
      .eq('id', viewingStudentId)
      .single();
    const viewer = viewerProfileRes.data || {
      id: viewingStudentId, first_name: null, last_name: null, avatar_url: null,
    };

    // 4. Parallel: assignments + own submissions + RPC leaderboard.
    const week = computeWeekWindow(klass.assignment_day_of_week);

    const [assignmentsRes, mySubsRes, leaderboardRes] = await Promise.all([
      sb.from('assignments')
        .select('id, title, subject_id, due_at, deleted_at, ' +
                'subject:subject_id ( name )')
        .eq('class_id', classId)
        .is('deleted_at', null),
      sb.from('assignment_submissions')
        .select('id, assignment_id, student_id, score, max_score, ' +
                'submitted_at, attempts, total_time_seconds')
        .eq('student_id', viewingStudentId)
        .is('deleted_at', null),
      sb.rpc('class_stars_leaderboard_for_member', { p_class_id: classId }),
    ]);

    if (assignmentsRes.error) {
      console.error('[student-data] assignments fetch failed', assignmentsRes.error);
      throw assignmentsRes.error;
    }
    if (mySubsRes.error) {
      console.error('[student-data] own-submissions fetch failed', mySubsRes.error);
      throw mySubsRes.error;
    }
    if (leaderboardRes.error) {
      // Soft-fail the leaderboard — render Stars unavailable rather than
      // breaking the whole page. The function is robust internally, so a
      // failure here typically means the RPC itself errored.
      console.error('[student-data] leaderboard RPC failed', leaderboardRes.error);
    }

    // 5. Compute viewer stats.
    const assignments = assignmentsRes.data || [];
    const ownFirstAttempts = pickFirstAttempts(mySubsRes.data || []);

    let submissions_completed = 0;
    let on_time_count = 0;
    let total_score = 0;
    let total_max = 0;

    assignments.forEach(function (a) {
      const sub = ownFirstAttempts.get(a.id + ':' + viewingStudentId);
      if (!sub || !sub.submitted_at) return;
      submissions_completed += 1;
      if (a.due_at && sub.submitted_at <= a.due_at) {
        on_time_count += 1;
      }
      if (sub.score != null && sub.max_score != null && sub.max_score > 0) {
        total_score += sub.score;
        total_max += sub.max_score;
      }
    });

    const assignments_in_class_count = assignments.length;
    const viewerStats = {
      assignments_in_class_count: assignments_in_class_count,
      submissions_completed: submissions_completed,
      on_time_count: on_time_count,
      average_score_pct: total_max === 0 ? null : Math.round((total_score / total_max) * 100),
      submissions_completed_pct: assignments_in_class_count === 0
        ? null
        : Math.round((submissions_completed / assignments_in_class_count) * 100),
    };

    // 6. Bucket each assignment into dueThisWeek (actionable) or
    // pastAssignments (submitted OR past-deadline-not-submitted).
    //
    // Phase 3 v2 rewrite — v1 returned a single "Due this week" list
    // including past-and-submitted items, which produced contradictory
    // pill states (e.g. "Overdue by 3 days" + "✓ Submitted on time"
    // on the same card). The split below makes each card's status
    // unambiguous and matches the two sections the page now renders.
    //
    // Bucketing rules:
    //   dueThisWeek:
    //     - due_at IS in current week-window
    //     - AND viewer has NOT submitted yet
    //     (covers "upcoming this week" and "overdue this week but not
    //      submitted yet — still in time today/tomorrow to do it late")
    //   pastAssignments:
    //     - viewer HAS submitted (regardless of when), OR
    //     - due_at is BEFORE current week-window (i.e. last week or
    //       earlier) AND viewer did NOT submit (missed)
    //   future-not-this-week (due 2+ weeks away, not submitted):
    //     - silently dropped — not actionable yet, not past.
    //
    // Past assignments sort: newest due-date first. The page applies
    // the "last week only by default" filter + Show-all toggle in JS
    // using the week.start_at + week.prev_week_start values it
    // computes from the same window.
    const dueThisWeek    = [];
    const pastAssignments = [];

    assignments.forEach(function (a) {
      if (!a.due_at) return;  // assignments without deadlines are not surfaceable here

      const sub = ownFirstAttempts.get(a.id + ':' + viewingStudentId);
      const isSubmitted = !!(sub && sub.submitted_at);
      const inThisWeek = a.due_at >= week.start_at && a.due_at < week.end_at;

      const card = {
        id: a.id,
        title: a.title,
        subject_id: a.subject_id,
        subject_name: a.subject ? a.subject.name : null,
        subject_colour_var: subjectColourVar(a.subject ? a.subject.name : null),
        due_at: a.due_at,
        is_submitted: isSubmitted,
        score: isSubmitted ? sub.score : null,
        max_score: isSubmitted ? sub.max_score : null,
        on_time: isSubmitted && a.due_at && sub.submitted_at <= a.due_at,
        submitted_at: isSubmitted ? sub.submitted_at : null,
      };

      if (isSubmitted) {
        pastAssignments.push(card);
      } else if (inThisWeek) {
        dueThisWeek.push(card);
      } else if (a.due_at < week.start_at) {
        // Past deadline + never submitted = missed → past assignments
        pastAssignments.push(card);
      }
      // else: future-not-this-week + not-submitted → silently dropped (v1)
    });

    dueThisWeek.sort(function (a, b) { return a.due_at.localeCompare(b.due_at); });
    pastAssignments.sort(function (a, b) { return b.due_at.localeCompare(a.due_at); });

    // Compute the previous week's start_at so the page can default-filter
    // "Past assignments" to last week only without having to recompute
    // the window itself.
    const prevWeekStart = new Date(new Date(week.start_at).getTime() - 7 * 86400000).toISOString();

    // 7. Leaderboard + viewer-on-podium derivation.
    const leaderboard = leaderboardRes && leaderboardRes.data
      ? leaderboardRes.data
      : null;
    const viewerOnPodium = !!(
      leaderboard &&
      Array.isArray(leaderboard.eligible) &&
      leaderboard.eligible.some(function (e) { return e.student_id === viewingStudentId; })
    );

    const pill = deriveStudentPill(klass);
    const stripe_colour_var = deriveStripeColourVar(klass);

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
        stripe_colour_var: stripe_colour_var,
        assignment_day_of_week: klass.assignment_day_of_week,
      },
      viewer: viewer,
      viewerStats: viewerStats,
      assignmentsDueThisWeek: dueThisWeek,
      pastAssignments: pastAssignments,
      leaderboard: leaderboard,
      viewerOnPodium: viewerOnPodium,
      week: week,
      prevWeekStart: prevWeekStart,  // for "Past assignments" last-week-only default filter
    };
  }

  /**
   * loadStudentClassShoutouts(classId, opts)
   *
   * Same shape as teacher-data.js's loadClassShoutouts — but called from
   * student-guard's auth context, so RLS gates by member-of-class
   * (class_shoutouts_select policy allows members to read non-deleted).
   *
   * Returns { shoutouts: [...], hasMore: boolean }.
   * Each shoutout row carries id, template_key, message, created_at,
   * author_id, recipient_id, author { first/last/avatar }, recipient { … }.
   *
   * Pagination is cursor-based on created_at (stable across new inserts
   * from the teacher side, which can happen between pages).
   *
   * Throws on driver error. Caller renders feed's error state.
   */
  async function loadStudentClassShoutouts(classId, opts) {
    const limit           = (opts && opts.limit)           != null ? opts.limit           : 20;
    const beforeCreatedAt = (opts && opts.beforeCreatedAt) != null ? opts.beforeCreatedAt : null;

    const guard = window.MrBadmusStudentGuard;
    const sb = guard && guard.getClient ? guard.getClient() : null;
    if (!sb) {
      throw new Error('[student-data] Supabase client unavailable — getClient() returned null');
    }

    // Phase 3 v2: call the class_shoutouts_for_viewer RPC instead of a
    // direct PostgREST query with profile-FK joins. Required because
    // students have NO SELECT policy on profiles for other users — the
    // FK join returned null author + recipient, surfacing as "by — · …"
    // em-dash names on every shoutout card.
    //
    // Migration: 20260525093000_class_shoutouts_for_viewer.sql.
    // The RPC is SECURITY DEFINER + membership-gated, so the privacy
    // boundary is preserved (returns ONLY first/last/avatar to active
    // class members).
    const { data, error } = await sb.rpc('class_shoutouts_for_viewer', {
      p_class_id:          classId,
      p_limit:             limit,
      p_before_created_at: beforeCreatedAt,
    });
    if (error) {
      console.error('[student-data] loadStudentClassShoutouts (RPC) failed', error);
      throw error;
    }

    const result = data || {};
    return {
      shoutouts: Array.isArray(result.shoutouts) ? result.shoutouts : [],
      hasMore:   !!result.hasMore,
    };
  }

  return {
    loadStudentClass: loadStudentClass,
    loadStudentClassShoutouts: loadStudentClassShoutouts,
  };
})();
