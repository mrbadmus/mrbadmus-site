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

  return { loadTeacherClasses };
})();
