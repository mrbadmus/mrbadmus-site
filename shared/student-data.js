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
 *   loadStudentClasses(viewingStudentId)         — the viewer's classes (picker)
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
 * Subject pill rule — ⊕ MRB-265 (Mide, 19 Aug 2026). READ FROM
 * `class_teachers.subject_id`, exactly as the teacher view reads it:
 * filter the links that carry a subject, take the lowest subject_id for a
 * deterministic tie-break, use that subject's name and colour. No links
 * visible → no pill.
 *
 * ⊕ This SUPERSEDES the rule MRB-263 left here that morning, and the note
 * that came with it. That rule parsed the subject out of `classes.name`
 * (`/Sc` → Combined Science, `/Ph` → Physics, …) because a student could
 * not read `class_teachers` — there was no policy for it, which this file
 * had recorded since v1 — and it named the fix as one policy. The policy
 * now exists (migration 20260819154015), so the second derivation is gone
 * and `classes.name` stops being load-bearing on the student side. That
 * was the real cost: the roster importer already find-or-creates a class
 * by exact name match, so a rename could change what a student's card
 * claimed the class was.
 *
 * ⚠️ THE POLICY GRANTS THE LINK, NOT THE TEACHER'S NAME. A student can now
 * read `class_teachers` for their own classes and join `subjects` through
 * it, but `profiles` has no student-read policy for a TEACHER's row, so the
 * teacher's name is still unreadable from here. Mide's 19 Aug ruling — that
 * students should see who teaches them — is therefore only half delivered;
 * the other half needs a second policy on `profiles`. See MRB-265.
 */

window.MrBadmusStudentData = (function () {

  // Shape-only UUID check — same idiom as teacher-data.js.
  function isUuid(s) {
    return typeof s === 'string' &&
      /^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/i.test(s);
  }

  /* ── The working academic year (MRB-261) ────────────────────────────────
     Which year's classes are the ones that matter right now.

     NOT `academic_years.is_current`: that flag is moved by hand on 1
     September (MRB-237), so through late August it still points at the year
     that finished in July — scoping on it would show a Year 11 their Year 10
     class and hide the one they start in a fortnight.

     NOT a plain `end_date >= today` either: 2025-26 runs to 31 Aug 2026, so
     on 19 Aug BOTH years are unfinished and the student is offered two
     classes. That is the bug itself.

     The rule: a year has effectively finished once it has less than
     YEAR_LOOKAHEAD_DAYS left to run, and the working year is the EARLIEST
     year still running past that horizon — "the year we will be in a month
     from now". The horizon only crosses a boundary inside the last month of
     a year, i.e. during the summer holiday, which is the one stretch where
     "this year" is genuinely ambiguous and forward-looking is what a school
     means.

     Full worked table of dates lives in shared/class-entry.js. Keep the three
     copies (here, class-entry.js, teacher-data.js) in sync by hand — there is
     no build step and class-entry.js must stay dependency-free.
     ───────────────────────────────────────────────────────────────────── */
  const YEAR_LOOKAHEAD_DAYS = 30;

  function pad2(n) { return (n < 10 ? '0' : '') + n; }

  function lookaheadDate() {
    const d = new Date();
    d.setDate(d.getDate() + YEAR_LOOKAHEAD_DAYS);
    return d.getFullYear() + '-' + pad2(d.getMonth() + 1) + '-' + pad2(d.getDate());
  }

  // Dates are ISO YYYY-MM-DD from Postgres `date` columns, so string
  // comparison IS date comparison.
  function workingAcademicYear(years) {
    const rows = (years || []).filter(function (y) { return y && y.end_date; });
    if (!rows.length) return null;
    const horizon = lookaheadDate();
    const live = rows.filter(function (y) { return y.end_date >= horizon; });
    if (live.length) {
      return live.reduce(function (best, y) {
        return (!best || y.end_date < best.end_date) ? y : best;
      }, null);
    }
    return rows.reduce(function (best, y) {
      return (!best || y.end_date > best.end_date) ? y : best;
    }, null);
  }

  /* Student-side pill derivation.

     ⊕ MRB-265 (Mide, 19 Aug 2026) — THE NAME-PARSE IS GONE. This used to
     read the subject out of `classes.name`, pulling `Sc` / `Ph` / `Ch` /
     `Bi` from `8r/Sc1` with a regex, because a student could not read
     `class_teachers` and the ruled source lives there. The comment that
     stood here said so and named the fix: one policy. That policy now
     exists — `class_teachers_member_read`, migration 20260819154015 — so
     the subject is read from `class_teachers.subject_id` on both sides of
     the app and `classes.name` stops being load-bearing here.

     That matters beyond tidiness. The parse made the class NAME carry
     meaning in a second place, and the roster importer already
     find-or-creates a class by exact name match (CLAUDE.md), so a rename
     could quietly change what subject a student's card claimed. One fact,
     one derivation, and it is now the same derivation `derivePill` uses in
     teacher-data.js — same filter, same lowest-subject_id tie-break, same
     colour lookup — so a class cannot show one subject to its teacher and
     a different one to the students in it.

     ⚠️ NO ROWS MEANS NO PILL, not a guessed one. A student who cannot see
     any link for the class — the class has no teacher assigned yet, or the
     membership lapsed — gets a card with no pill, which is what the parse
     did for an off-convention name and the same safe direction. */
  function deriveStudentPill(klass, teacherRowsForClass) {
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
    return { pill_label: name, pill_colour_var: subjectColourVar(name) };
  }

  /* The links for one or many classes, keyed by class_id.

     ⚠️ A FAILURE HERE IS NOT FATAL. The pill is a label on a card; the
     assignments under it are the page. If the query fails the classes still
     render, without pills, exactly as they do for a class with no teacher
     assigned — logged, never thrown. */
  async function loadClassTeacherLinks(sb, classIds) {
    const byClass = {};
    if (!classIds || classIds.length === 0) return byClass;
    const res = await sb
      .from('class_teachers')
      .select('class_id, subject_id, subject:subject_id ( name )')
      .in('class_id', classIds);
    if (res.error) {
      console.error('[student-data] class_teachers query failed', res.error);
      return byClass;
    }
    (res.data || []).forEach(function (row) {
      if (!byClass[row.class_id]) byClass[row.class_id] = [];
      byClass[row.class_id].push(row);
    });
    return byClass;
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
   *     // ⊕ MRB-238 (19 Aug 2026) — three buckets, nothing dropped.
   *     // Was `assignmentsDueThisWeek` + `pastAssignments`, and anything
   *     // that was neither in-window, submitted nor past fell through a
   *     // silent `else`. Cards share one shape across all three.
   *     assignmentsDueNow: [       // open, owed now; most overdue first
   *       { id, title, subject_id, subject_name, subject_colour_var,
   *         due_at, is_submitted, score, max_score, on_time }
   *     ],
   *     assignmentsComingUp: [],   // set, not yet due; undated last
   *     assignmentsDone: [],       // submitted; newest first
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
      .select('id, name, key_stage, year_group, tier, science_pathway, assignment_day_of_week, deleted_at, academic_year_id')
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

    /* 2b. Year-scope the SINGLE class, the same way the listing does.
       ⊕ MRB-261, finished (Mide, 19 Aug 2026). The listing was scoped and
       this was not, so the class a student left in July vanished from
       their list and stayed reachable at its own URL — a bookmark, a
       browser autocomplete, a link in a message from a friend. It then
       rendered as CURRENT WORK: a live leaderboard, a "due this week"
       section, a shout-out box, all belonging to a class that finished.

       Membership is not the question here and is checked above; MRB-237
       rolled students forward by creating NEW rows and leaving 2025-26
       intact on purpose, so both memberships are legitimately live. The
       question is which year is being worked in, and the answer is
       `workingAcademicYear` — never `is_current`, which is moved by hand
       on 1 September and through late August still names the year that
       finished in July.

       A past class is UNAVAILABLE, not missing and not forbidden: the
       student was in it, and saying "you're not in this class" would be a
       lie. Its own code, so the page can say the true thing. */
    const yearRes = await sb
      .from('academic_years')
      .select('id, name, start_date, end_date')
      .is('deleted_at', null);
    if (yearRes.error) {
      console.error('[student-data] academic years query failed', yearRes.error);
      throw yearRes.error;
    }
    const workingYear = workingAcademicYear(yearRes.data);
    // No readable years at all (a self-serve visitor with no school) — show
    // the class rather than hiding it, matching the listing's own fallback.
    if (workingYear && klass.academic_year_id &&
        klass.academic_year_id !== workingYear.id) {
      const e = new Error('Class belongs to a past academic year');
      e.code = 'class_not_current';
      throw e;
    }

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

    /* 6. Bucket every assignment. THREE buckets, and nothing is dropped.
       ⊕ MRB-238 (Mide, 19 Aug 2026) — VISIBILITY IS DRIVEN BY THE
       ASSIGNMENT'S OWN DATES, NEVER BY THE CURRENT CALENDAR WEEK.

       What stood here dropped, in silence, any assignment that was
       neither in this week's window, nor submitted, nor past. Mide set a
       demo assignment due 25 August; the window ran 17–24; and it existed
       on nobody's screen, with nothing anywhere saying that something
       existed. A student who wanted to work ahead could not see there was
       anything to work ahead ON.

       Silent dropping is the defect. The window boundaries are fine — it
       is the `else: drop` that was wrong. A row that exists and belongs to
       this class now appears somewhere, always.

         DUE NOW   — open and not yet submitted, deadline inside this week
                     or already past. Overdue items sort first (due_at
                     ascending puts the most overdue at the top) and STAY
                     HERE UNTIL SUBMITTED. They no longer vanish at a week
                     boundary, which is what used to move a missed piece of
                     work into "past" where it read as finished.
         COMING UP — set but not yet due, beyond this week. Present and
                     visible, clearly not required yet: a student who wants
                     to get ahead can, and one who does not is not nagged.
                     Undated assignments live here too — they exist, and
                     no date makes them due.
         DONE      — submitted, as before.

       ⚠️ MISSED WORK IS "DUE NOW", NOT "DONE". It used to be filed with
       the finished work and captioned "✗ Not submitted", which put the one
       thing a student still owes at the bottom of the screen under a
       heading that says the opposite. It is outstanding, so it sits with
       the outstanding work, and the card stays actionable.

       Done sorts newest-first; the page applies its own "last week only by
       default" filter and Show-all toggle on top of that. */
    const dueNow   = [];
    const comingUp = [];
    const done     = [];

    assignments.forEach(function (a) {
      const sub = ownFirstAttempts.get(a.id + ':' + viewingStudentId);
      const isSubmitted = !!(sub && sub.submitted_at);

      const card = {
        id: a.id,
        title: a.title,
        subject_id: a.subject_id,
        subject_name: a.subject ? a.subject.name : null,
        subject_colour_var: subjectColourVar(a.subject ? a.subject.name : null),
        due_at: a.due_at || null,
        is_submitted: isSubmitted,
        score: isSubmitted ? sub.score : null,
        max_score: isSubmitted ? sub.max_score : null,
        on_time: isSubmitted && a.due_at && sub.submitted_at <= a.due_at,
        submitted_at: isSubmitted ? sub.submitted_at : null,
      };

      if (isSubmitted) {
        done.push(card);
      } else if (a.due_at && a.due_at < week.end_at) {
        // Overdue, or due before this week is out. Either way: owed now.
        dueNow.push(card);
      } else {
        // Beyond this week, or never dated. Visible, not yet required.
        comingUp.push(card);
      }
    });

    // Most overdue first, then the rest of this week in order.
    dueNow.sort(function (a, b) { return a.due_at.localeCompare(b.due_at); });
    // Soonest first; the undated sit at the bottom, since nothing is due.
    comingUp.sort(function (a, b) {
      if (!a.due_at && !b.due_at) return (a.title || '').localeCompare(b.title || '');
      if (!a.due_at) return 1;
      if (!b.due_at) return -1;
      return a.due_at.localeCompare(b.due_at);
    });
    done.sort(function (a, b) {
      return (b.due_at || '').localeCompare(a.due_at || '');
    });

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

    // ⊕ MRB-265 — the subject comes from the link table now, not the name.
    const teacherLinks = await loadClassTeacherLinks(sb, [klass.id]);
    const pill = deriveStudentPill(klass, teacherLinks[klass.id]);
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
      assignmentsDueNow: dueNow,
      assignmentsComingUp: comingUp,
      assignmentsDone: done,
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


  /**
   * loadStudentClasses(viewingStudentId) — MRB-259.
   *
   * Every class the viewer is an active member of, for the picker at
   * /student/classes.html. Deliberately thin: the picker's job is to ROUTE,
   * not to summarise, and a student who holds several classes is one click
   * from the full page for any of them. Adding per-class assignment counts
   * here would mean a fan-out of queries to render a screen most students
   * never see (the single-class case skips it entirely — shared/class-entry.js
   * links straight past it).
   *
   * Two hops rather than a PostgREST embed, matching loadStudentClass's
   * membership-then-class shape: `class_members` is RLS-scoped to the
   * viewer's own rows, and `classes` is readable because they are a member.
   * Soft-deleted classes are filtered on the second hop, so a membership row
   * left pointing at a deleted class simply yields nothing.
   */
  async function loadStudentClasses(viewingStudentId) {
    if (!isUuid(viewingStudentId)) {
      const e = new Error('Invalid student id');
      e.code = 'invalid_student_id';
      throw e;
    }

    const guard = window.MrBadmusStudentGuard;
    const sb = guard && guard.getClient ? guard.getClient() : null;
    if (!sb) {
      throw new Error('[student-data] Supabase client unavailable — getClient() returned null');
    }

    const memberRes = await sb
      .from('class_members')
      .select('class_id')
      .eq('student_id', viewingStudentId)
      .is('left_at', null)
      .is('deleted_at', null);
    if (memberRes.error) {
      console.error('[student-data] memberships query failed', memberRes.error);
      throw memberRes.error;
    }

    const ids = (memberRes.data || [])
      .map(function (r) { return r.class_id; })
      .filter(Boolean);
    if (!ids.length) return [];

    // Year-scope (MRB-261). MRB-237 rolled students forward by creating NEW
    // rows and deliberately leaving 2025-26 intact, so the record of what a
    // Year 11 was taught in Year 10 survives. Both memberships are therefore
    // live and both were being listed — a student was offered this year's
    // class and the one they left in July. The data is right; the view was
    // not. Filtering here, not on `is_current` — see workingAcademicYear.
    const yearRes = await sb
      .from('academic_years')
      .select('id, name, start_date, end_date')
      .is('deleted_at', null);
    if (yearRes.error) {
      console.error('[student-data] academic years query failed', yearRes.error);
      throw yearRes.error;
    }
    const workingYear = workingAcademicYear(yearRes.data);

    let classQuery = sb
      .from('classes')
      .select('id, name, key_stage, year_group, tier, science_pathway, academic_year_id')
      .in('id', ids)
      .is('deleted_at', null);
    // No readable years at all (a self-serve visitor with no school) — don't
    // hide anything rather than showing an empty picker.
    if (workingYear) classQuery = classQuery.eq('academic_year_id', workingYear.id);
    const classRes = await classQuery.order('name', { ascending: true });
    if (classRes.error) {
      console.error('[student-data] classes query failed', classRes.error);
      throw classRes.error;
    }

    // ⊕ MRB-265 — one query for every class on the picker, not one each.
    const teacherLinks = await loadClassTeacherLinks(
      sb, (classRes.data || []).map(function (k) { return k.id; }));

    return (classRes.data || []).map(function (k) {
      const pill = deriveStudentPill(k, teacherLinks[k.id]);
      return {
        id: k.id,
        name: k.name,
        key_stage: k.key_stage,
        year_group: k.year_group,
        tier: k.tier,
        science_pathway: k.science_pathway,
        pill_label: pill.pill_label,
        pill_colour_var: pill.pill_colour_var,
      };
    });
  }

  return {
    loadStudentClass: loadStudentClass,
    loadStudentClasses: loadStudentClasses,
    loadStudentClassShoutouts: loadStudentClassShoutouts,
  };
})();
