/**
 * shared/seating-data.js — MRB-322 seating plans data layer
 *
 * Page contract (load AFTER teacher-guard.js, which owns the Supabase client):
 *   <script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2/dist/umd/supabase.min.js"></script>
 *   <script src="/shared/config.js"></script>
 *   <script src="/shared/class-entry.js"></script>
 *   <script src="/shared/teacher-guard.js"></script>
 *   <script src="/shared/seating-data.js"></script>
 *
 * Two tables, and one rule about each:
 *
 *   room_layouts   the shape of a room. Readable by the school's STAFF —
 *                  teachers and admins, not pupils — and writable only by
 *                  whoever drew it (or a school admin). Desk geometry, no
 *                  children, which is why cover reads these and not plans.
 *   seating_plans  a class placed onto a layout. Readable only by that class's
 *                  own subject teachers (co-teachers included) and school
 *                  admins — never by cover, and never by a pupil. A seating
 *                  plan is a named list of children, which is why that
 *                  boundary is tighter than the layout's.
 *
 * ⚠️ Everything here is layer 2 of defence-in-depth. The RLS policies in
 * migration 20260903214546_mrb322_seating_admin_is_scope.sql (the latest of
 * five; it supersedes the admin branch of all four before it) are the real
 * boundary; this
 * module exists so the page can render the right thing rather than firing
 * requests it knows will come back empty. `canEditLayout` / `canEditPlan` in
 * particular are NOT security — they decide whether a control is drawn at all,
 * because the house rule is that a control someone cannot use is absent rather
 * than greyed out.
 *
 * Soft delete: neither table is ever hard-deleted, and — deliberately — no RLS
 * policy filters on `deleted_at`. Postgres applies a SELECT policy to a row's
 * POST-update state, so a policy that hid deleted rows would make the soft
 * delete itself fail with 42501 (CLAUDE.md, MRB-46 Phase 2). Filtering retired
 * rows out is therefore this module's job, and every read below does it.
 */

window.MrBadmusSeatingData = (function () {
  'use strict';

  // ── The room list ────────────────────────────────────────────────────
  // Fixed, and fixed in three places on purpose: here for the dropdown, in a
  // CHECK constraint on room_layouts.room_code so the database refuses
  // anything else, and in seating_tells.py so a drifted copy fails the build.
  // Nobody types a room name — not a teacher, not an admin.
  const ROOMS = ['S01', 'S02a', 'S02b', 'S02c', 'S04',
                 'S08a', 'S08b', 'S08c', 'S09a', 'S09b', 'S010'];

  const SOURCES = ['photo', 'template', 'manual'];

  function client() {
    const guard = window.MrBadmusTeacherGuard;
    const sb = guard && guard.getClient ? guard.getClient() : null;
    if (!sb) throw new Error('[seating-data] Supabase client unavailable');
    return sb;
  }

  const UUID_RE =
    /^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/i;
  function isUuid(v) { return typeof v === 'string' && UUID_RE.test(v); }

  function requireUuid(v, what) {
    if (!isUuid(v)) {
      const e = new Error('[seating-data] invalid ' + what + ': ' + v);
      e.code = 'invalid_' + what;
      throw e;
    }
    return v;
  }

  function bail(what, error) {
    const e = new Error('[seating-data] ' + what + ': ' +
                        (error && error.message ? error.message : 'unknown'));
    e.code = (error && error.code) || 'query_failed';
    throw e;
  }

  // ── Who am I ─────────────────────────────────────────────────────────
  // Cached for the life of the page: the answer cannot change without a
  // navigation, and every permission question below asks for it.
  let _me = null;
  async function me() {
    if (_me) return _me;
    const sb = client();
    const { data: auth } = await sb.auth.getUser();
    const uid = auth && auth.user ? auth.user.id : null;
    if (!uid) {
      const e = new Error('[seating-data] not signed in');
      e.code = 'not_signed_in';
      throw e;
    }
    const { data, error } = await sb
      .from('profiles')
      .select('id, first_name, last_name, role, school_id')
      .eq('id', uid)
      .single();
    if (error) bail('profile read failed', error);

    // The school_admin SCOPE, read alongside the profile.
    //
    // `staff_scopes` carries a self-read policy (`profile_id = auth.uid()`),
    // so this is one extra round trip and never a permission problem. It has
    // to happen at all because the seating policies now decide "admin" on the
    // SCOPE rather than on `profiles.role`, and a page still asking the old
    // question would hide Save from a school_admin the database is perfectly
    // willing to let write. That is the worst kind of disagreement between
    // the two layers, because it presents as a broken button rather than as a
    // refusal.
    //
    // A failed scope read is deliberately NOT fatal: it degrades to "not an
    // admin", which is the safe direction. RLS is what actually enforces
    // this; the helpers below only decide what gets drawn.
    var scopeRows = null;
    try {
      var got = await sb
        .from('staff_scopes')
        .select('scope, started_at, ended_at, deleted_at')
        .eq('profile_id', uid);
      scopeRows = got.data;
    } catch (e) { scopeRows = null; }

    var nowMs = Date.now();
    data.scopes = (scopeRows || []).filter(function (s) {
      return !s.deleted_at
        && (!s.started_at || Date.parse(s.started_at) <= nowMs)
        && (!s.ended_at   || Date.parse(s.ended_at)   >  nowMs);
    }).map(function (s) { return s.scope; });

    _me = data;
    return _me;
  }

  // ── Permission helpers (presentation only — see the header) ──────────
  // Mirrors `auth_user_has_scope('school_admin')` in the database, M1
  // dual-read fallback included: that SQL helper still answers true for
  // `profiles.role = 'admin'` while the scope migration is unfinished, so
  // this answers true for it too. When the fallback is finally removed, both
  // halves lose the same clause, on the same day.
  //
  // ⚠️ On production these are two different sets of people. `role = 'admin'`
  // names one account holding no scopes at all; the three who actually
  // administer the school are `role = 'teacher'` carrying the scope. Testing
  // only the role — which this did until the scope migration — drew a
  // read-only page for all three of them.
  function isAdmin(who) {
    if (!who) return false;
    return who.role === 'admin'
      || (who.scopes || []).indexOf('school_admin') !== -1;
  }

  function canEditLayout(layout, who) {
    if (!layout || !who) return false;
    return layout.created_by === who.id || isAdmin(who);
  }

  function canEditPlan(plan, who) {
    if (!plan || !who) return false;
    return plan.created_by === who.id || isAdmin(who);
  }

  // ── Author names ─────────────────────────────────────────────────────
  // Every layout card names the person who drew it, because two teachers will
  // have different opinions about the same room and the card is where that
  // gets settled. One batched read rather than one per row.
  async function authorsFor(rows) {
    const ids = [];
    (rows || []).forEach(function (r) {
      if (r.created_by && ids.indexOf(r.created_by) === -1) ids.push(r.created_by);
    });
    if (!ids.length) return {};
    const { data, error } = await client()
      .from('profiles')
      .select('id, first_name, last_name')
      .in('id', ids);
    if (error) {
      // A missing author name must not blank the list — the layout is still
      // usable, it just says "Unknown" on the card.
      console.warn('[seating-data] author lookup failed', error.message);
      return {};
    }
    const byId = {};
    (data || []).forEach(function (p) {
      byId[p.id] = displayName(p);
    });
    return byId;
  }

  function displayName(p) {
    if (!p) return 'Unknown';
    const first = (p.first_name || '').trim();
    const last = (p.last_name || '').trim();
    const joined = (first + ' ' + last).trim();
    return joined || 'Unknown';
  }

  // ── Seat labels ──────────────────────────────────────────────────────
  // A seat is small. "Firstname L." is what fits and what a teacher reads at a
  // glance from the front of the room. Two children with the same first name
  // and the same initial is ordinary in a class of thirty, so the label grows
  // only as far as it must to stay unambiguous: first name, then one initial,
  // then more of the surname.
  function seatLabels(students) {
    const out = {};
    const byFirst = {};
    (students || []).forEach(function (s) {
      const first = (s.first_name || '').trim() || 'Pupil';
      (byFirst[first] = byFirst[first] || []).push(s);
    });
    Object.keys(byFirst).forEach(function (first) {
      const group = byFirst[first];
      if (group.length === 1) { out[group[0].id] = first; return; }
      // Grow the surname slice until every label in this group is distinct,
      // or until we run out of surname to give.
      for (let n = 1; n <= 12; n++) {
        const seen = {};
        let clash = false;
        group.forEach(function (s) {
          const lab = first + ' ' + (s.last_name || '').trim().slice(0, n) +
                      (n < (s.last_name || '').trim().length ? '.' : '');
          if (seen[lab]) clash = true;
          seen[lab] = true;
        });
        if (!clash || n === 12) {
          group.forEach(function (s) {
            const surname = (s.last_name || '').trim();
            out[s.id] = (first + ' ' + surname.slice(0, n) +
                         (n < surname.length ? '.' : '')).trim();
          });
          return;
        }
      }
    });
    return out;
  }

  // ── Room layouts ─────────────────────────────────────────────────────

  async function listRoomLayouts() {
    const { data, error } = await client()
      .from('room_layouts')
      .select('id, school_id, room_code, name, layout, source, created_by, created_at, updated_at')
      .is('deleted_at', null)
      .order('room_code', { ascending: true })
      .order('created_at', { ascending: false });
    if (error) bail('layout list failed', error);
    const rows = data || [];
    const authors = await authorsFor(rows);
    const who = await me();
    return rows.map(function (r) {
      return decorateLayout(r, authors, who);
    });
  }

  function decorateLayout(r, authors, who) {
    const desks = (r.layout && r.layout.desks) || [];
    let seats = 0;
    desks.forEach(function (d) { seats += (Number(d.seats) || 0); });
    return {
      id: r.id,
      room_code: r.room_code,
      name: r.name || null,
      layout: r.layout,
      source: r.source,
      created_by: r.created_by,
      author_name: authors[r.created_by] || 'Unknown',
      created_at: r.created_at,
      updated_at: r.updated_at,
      desk_count: desks.length,
      seat_count: seats,
      can_edit: canEditLayout(r, who),
    };
  }

  async function loadRoomLayout(id) {
    requireUuid(id, 'layout id');
    const { data, error } = await client()
      .from('room_layouts')
      .select('id, school_id, room_code, name, layout, source, created_by, created_at, updated_at')
      .eq('id', id)
      .is('deleted_at', null)
      .maybeSingle();
    if (error) bail('layout read failed', error);
    if (!data) return null;
    const authors = await authorsFor([data]);
    return decorateLayout(data, authors, await me());
  }

  async function createRoomLayout(input) {
    const who = await me();
    const room = String((input && input.room_code) || '');
    if (ROOMS.indexOf(room) === -1) {
      const e = new Error('[seating-data] unknown room: ' + room);
      e.code = 'unknown_room';
      throw e;
    }
    const source = String((input && input.source) || 'manual');
    if (SOURCES.indexOf(source) === -1) {
      const e = new Error('[seating-data] unknown source: ' + source);
      e.code = 'unknown_source';
      throw e;
    }
    const { data, error } = await client()
      .from('room_layouts')
      .insert({
        school_id:  who.school_id,
        room_code:  room,
        name:       (input && input.name) || null,
        layout:     input.layout,
        source:     source,
        created_by: who.id,
      })
      .select('id, school_id, room_code, name, layout, source, created_by, created_at, updated_at')
      .single();
    if (error) bail('layout create failed', error);
    return decorateLayout(data, { [who.id]: displayName(who) }, who);
  }

  async function updateRoomLayout(id, patch) {
    requireUuid(id, 'layout id');
    const fields = {};
    if (patch && patch.layout !== undefined) fields.layout = patch.layout;
    if (patch && patch.name !== undefined) fields.name = patch.name;
    if (patch && patch.room_code !== undefined) {
      if (ROOMS.indexOf(patch.room_code) === -1) {
        const e = new Error('[seating-data] unknown room: ' + patch.room_code);
        e.code = 'unknown_room';
        throw e;
      }
      fields.room_code = patch.room_code;
    }
    const { data, error } = await client()
      .from('room_layouts')
      .update(fields)
      .eq('id', id)
      .is('deleted_at', null)
      .select('id, school_id, room_code, name, layout, source, created_by, created_at, updated_at')
      .maybeSingle();
    if (error) bail('layout update failed', error);
    // RLS returns zero rows rather than an error when the caller may read the
    // row but not write it. That is a permission answer, not a missing row.
    if (!data) {
      const e = new Error('[seating-data] layout not writable by you');
      e.code = 'not_permitted';
      throw e;
    }
    const authors = await authorsFor([data]);
    return decorateLayout(data, authors, await me());
  }

  async function softDeleteRoomLayout(id) {
    requireUuid(id, 'layout id');
    const { data, error } = await client()
      .from('room_layouts')
      .update({ deleted_at: new Date().toISOString() })
      .eq('id', id)
      .is('deleted_at', null)
      .select('id')
      .maybeSingle();
    if (error) bail('layout retire failed', error);
    if (!data) {
      const e = new Error('[seating-data] layout not writable by you');
      e.code = 'not_permitted';
      throw e;
    }
    return true;
  }

  // ── Seating plans ────────────────────────────────────────────────────

  async function listPlansForClass(classId) {
    requireUuid(classId, 'class id');
    const { data, error } = await client()
      .from('seating_plans')
      .select('id, class_id, room_layout_id, name, assignments, created_by, created_at, updated_at, ' +
              'room_layout:room_layout_id ( id, room_code, name, layout, created_by, deleted_at )')
      .eq('class_id', classId)
      .is('deleted_at', null)
      .order('updated_at', { ascending: false });
    if (error) bail('plan list failed', error);
    const rows = data || [];
    const authors = await authorsFor(rows);
    const who = await me();
    return rows.map(function (r) { return decoratePlan(r, authors, who); });
  }

  function decoratePlan(r, authors, who) {
    const layout = r.room_layout || null;
    return {
      id: r.id,
      class_id: r.class_id,
      room_layout_id: r.room_layout_id,
      room_code: layout ? layout.room_code : null,
      layout: layout ? layout.layout : null,
      layout_retired: !!(layout && layout.deleted_at),
      name: r.name || null,
      assignments: r.assignments || {},
      created_by: r.created_by,
      author_name: authors[r.created_by] || 'Unknown',
      created_at: r.created_at,
      updated_at: r.updated_at,
      seated_count: Object.keys(r.assignments || {}).length,
      can_edit: canEditPlan(r, who),
    };
  }

  async function loadSeatingPlan(id) {
    requireUuid(id, 'plan id');
    const { data, error } = await client()
      .from('seating_plans')
      .select('id, class_id, room_layout_id, name, assignments, created_by, created_at, updated_at, ' +
              'room_layout:room_layout_id ( id, room_code, name, layout, created_by, deleted_at )')
      .eq('id', id)
      .is('deleted_at', null)
      .maybeSingle();
    if (error) bail('plan read failed', error);
    if (!data) return null;
    const authors = await authorsFor([data]);
    return decoratePlan(data, authors, await me());
  }

  async function createSeatingPlan(input) {
    const who = await me();
    requireUuid(input && input.class_id, 'class id');
    requireUuid(input && input.room_layout_id, 'layout id');
    const { data, error } = await client()
      .from('seating_plans')
      .insert({
        class_id:       input.class_id,
        room_layout_id: input.room_layout_id,
        name:           input.name || null,
        assignments:    input.assignments || {},
        created_by:     who.id,
      })
      .select('id, class_id, room_layout_id, name, assignments, created_by, created_at, updated_at, ' +
              'room_layout:room_layout_id ( id, room_code, name, layout, created_by, deleted_at )')
      .single();
    if (error) bail('plan create failed', error);
    return decoratePlan(data, { [who.id]: displayName(who) }, who);
  }

  async function updateSeatingPlan(id, patch) {
    requireUuid(id, 'plan id');
    const fields = {};
    if (patch && patch.assignments !== undefined) fields.assignments = patch.assignments;
    if (patch && patch.name !== undefined) fields.name = patch.name;
    const { data, error } = await client()
      .from('seating_plans')
      .update(fields)
      .eq('id', id)
      .is('deleted_at', null)
      .select('id, class_id, room_layout_id, name, assignments, created_by, created_at, updated_at, ' +
              'room_layout:room_layout_id ( id, room_code, name, layout, created_by, deleted_at )')
      .maybeSingle();
    if (error) bail('plan save failed', error);
    if (!data) {
      const e = new Error('[seating-data] plan not writable by you');
      e.code = 'not_permitted';
      throw e;
    }
    const authors = await authorsFor([data]);
    return decoratePlan(data, authors, await me());
  }

  async function softDeleteSeatingPlan(id) {
    requireUuid(id, 'plan id');
    const { data, error } = await client()
      .from('seating_plans')
      .update({ deleted_at: new Date().toISOString() })
      .eq('id', id)
      .is('deleted_at', null)
      .select('id')
      .maybeSingle();
    if (error) bail('plan retire failed', error);
    if (!data) {
      const e = new Error('[seating-data] plan not writable by you');
      e.code = 'not_permitted';
      throw e;
    }
    return true;
  }

  // ── Classes and rosters ──────────────────────────────────────────────

  /**
   * Classes the signed-in teacher can place. Scoped by the working academic
   * year via MRBClassEntry.workingAcademicYear — never by
   * academic_years.is_current, which is moved by hand on 1 September and so
   * still points at last year through the whole of August (MRB-261).
   */
  async function myClasses() {
    const sb = client();
    const { data, error } = await sb
      .from('class_teachers')
      .select('class_id, role, ended_at, ' +
              'class:class_id ( id, name, key_stage, year_group, academic_year_id, deleted_at )')
      .is('deleted_at', null);
    if (error) bail('class list failed', error);

    let year = null;
    if (window.MRBClassEntry && window.MRBClassEntry.academicYears) {
      try {
        const years = await window.MRBClassEntry.academicYears();
        year = window.MRBClassEntry.workingAcademicYear(years || []);
      } catch (err) {
        console.warn('[seating-data] academic year lookup failed', err.message);
      }
    }

    const seen = {};
    const out = [];
    (data || []).forEach(function (row) {
      const c = row.class;
      if (!c || c.deleted_at) return;
      if (year && c.academic_year_id !== year.id) return;
      // An ended attachment is history, not a class you can seat today.
      if (row.ended_at && new Date(row.ended_at) <= new Date()) return;
      // Cover is outside seating entirely (ruled 3 Sep 2026), so a class you
      // are only covering must not be offered here. The policies would refuse
      // the plan anyway; listing the class would just walk a teacher into a
      // screen that cannot work, and the house rule is that a control someone
      // cannot use is absent rather than shown and then apologised for.
      if (row.role !== 'subject_teacher') return;
      if (seen[c.id]) return;
      seen[c.id] = true;
      out.push({ id: c.id, name: c.name, key_stage: c.key_stage,
                 year_group: c.year_group });
    });
    return out.sort(byNaturalName);
  }

  // "9A" must sort before "10A" — plain string order gets that backwards.
  function byNaturalName(a, b) {
    const na = parseInt((a.name || '').match(/\d+/), 10);
    const nb = parseInt((b.name || '').match(/\d+/), 10);
    if (!isNaN(na) && !isNaN(nb) && na !== nb) return na - nb;
    return String(a.name).localeCompare(String(b.name));
  }

  async function loadClass(classId) {
    requireUuid(classId, 'class id');
    const { data, error } = await client()
      .from('classes')
      .select('id, name, key_stage, year_group')
      .eq('id', classId)
      .is('deleted_at', null)
      .maybeSingle();
    if (error) bail('class read failed', error);
    return data || null;
  }

  /**
   * The class roster, read-only. Departed members (left_at set) are excluded:
   * a seating plan is about who is in the room now.
   */
  async function loadClassRoster(classId) {
    requireUuid(classId, 'class id');
    const { data, error } = await client()
      .from('class_members')
      .select('student_id, left_at, ' +
              'student:student_id ( id, first_name, last_name, deleted_at )')
      .eq('class_id', classId)
      .is('deleted_at', null)
      .is('left_at', null);
    if (error) bail('roster read failed', error);
    const students = [];
    (data || []).forEach(function (row) {
      const s = row.student;
      if (!s || s.deleted_at) return;
      students.push({ id: s.id, first_name: s.first_name, last_name: s.last_name });
    });
    students.sort(function (a, b) {
      const la = (a.last_name || '').toLowerCase();
      const lb = (b.last_name || '').toLowerCase();
      if (la !== lb) return la < lb ? -1 : 1;
      return (a.first_name || '').toLowerCase() < (b.first_name || '').toLowerCase() ? -1 : 1;
    });
    const labels = seatLabels(students);
    students.forEach(function (s) { s.label = labels[s.id]; });
    return students;
  }

  return {
    ROOMS: ROOMS.slice(),
    me,
    isAdmin,
    canEditLayout,
    canEditPlan,
    seatLabels,
    displayName,
    listRoomLayouts,
    loadRoomLayout,
    createRoomLayout,
    updateRoomLayout,
    softDeleteRoomLayout,
    listPlansForClass,
    loadSeatingPlan,
    createSeatingPlan,
    updateSeatingPlan,
    softDeleteSeatingPlan,
    myClasses,
    loadClass,
    loadClassRoster,
  };
})();
