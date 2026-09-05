/* ───────────────────────────────────────────────────────────────────────────
   shared/seating-canvas.js — the seating-plan canvas engine

   A teacher photographs, or hand-builds, the desk arrangement of their ACTUAL
   classroom. Real rooms are not grids. They have a horseshoe with one arm
   short because of the fire door, a bank of clusters angled at the board, two
   desks pushed together under the window because that is where the sockets
   are. An editor that snaps to a tidy grid cannot draw any of those, and a
   seating plan that does not look like the room is a seating plan the teacher
   will not use on cover day. So: FREE PLACEMENT, FREE ROTATION, free size.
   Nothing here snaps unless the user asks for it (Shift on a rotate).

   ── Why SVG and not <canvas> ───────────────────────────────────────────────
   Three reasons, and all three are about not rebuilding the browser:
     1. Hit-testing is free. `event.target.closest('[data-seat-id]')` IS the
        hit test. On <canvas> we would be writing our own point-in-rotated-rect
        pass over 60 desks on every pointermove.
     2. Accessibility is free. A seat is a real focusable element with a real
        `aria-label` and a real `<title>`. On <canvas> the whole plan is one
        opaque bitmap to a screen reader, and a seating plan is exactly the
        artefact a SENCO needs to read.
     3. It prints. Every teacher prints this and puts it on the desk. SVG
        prints at the printer's resolution; a canvas prints at 96dpi mush.

   ── The coordinate model (FIXED — see the plan; do not change it here) ─────
   The room is a unit rectangle. Everything stored is NORMALISED to 0..1, so
   one saved layout renders identically on a laptop, on an iPad and on A4.
   Nothing in the stored model is in pixels.

       { v: 1,
         front: 'top' | 'right' | 'bottom' | 'left',
         teacher_desk: {x, y, w, h, rotation} | null,
         desks: [ {id, shape:'rect'|'round', x, y, w, h, rotation, seats:1..6} ] }

   `x, y` are the desk's CENTRE. `w, h` are normalised to the room's width and
   height RESPECTIVELY. `rotation` is degrees clockwise.

   A seat id is DERIVED and never stored: `deskId + ':' + index`, index from 0.
   That is deliberate — it means reducing a desk from 4 seats to 2 cannot leave
   a stored seat behind to rot, and it means the id is stable under a move.
   ⚠️ Because ':' is the separator, a desk id may never contain one; `validate`
   rejects it rather than letting a colon silently split a seat id in half.

   ── The one place the model is NOT the truth: aspect ───────────────────────
   Normalising w against room width and h against room height means a desk
   stored as w=0.1,h=0.1 is NOT square on screen — it is square only in a
   square room. That is the right storage model (it keeps a layout resolution-
   independent) but it means the maths cannot be done in normalised space:
   rotating 30 degrees in normalised space is a shear, not a rotation, and a
   desk rotated 90 degrees would change size. So ALL geometry in this file is
   computed in SVG user space, where the room's real proportions hold, and
   normalised coordinates are treated as nothing more than a storage encoding
   at the two boundaries (read in, write out).

   ── Deviations from the brief, and why ─────────────────────────────────────
   1. viewBox height is `1000 / aspect`, not `1000 * aspect`. The brief said
      "aspect (default 1.35 = a wide classroom)" and also `viewBox="0 0 1000
      1000*aspect"`, and those two cannot both hold: 1000*1.35 = 1350 is a room
      HALF AS DEEP AGAIN as it is wide, i.e. a corridor, not a wide classroom.
      Read `aspect` as width÷height, which is what "1.35 is wide" means.
   2. `validate` WRAPS an out-of-range rotation instead of clamping it. 350
      degrees means -10 degrees; clamping it to 180 would take a desk that is
      almost straight and lay it sideways, silently, on a DB read. Wrapping is
      the same operation the brief wanted (get it into range without rejecting)
      and it is the one that preserves the desk. Recorded in `warnings`.
   3. `overlapReport(layout, aspect)` takes an optional second argument. Desk
      overlap is a question about the real room, and rotation only means
      anything once the room's proportions are known. Defaults to 1.35, so the
      one-argument call in the brief still works.
   4. Seat drops accept a native HTML5 `drop` as well as an internal pointer
      drag. "Seats are drop targets" only pays for itself if a student can be
      dragged in from a class list living outside this canvas, and that list is
      an ordinary `<li draggable>`, not a pointer gesture we own.
   All four are called out again in the report; none of them changes the stored
   model, so a layout written by any of them is readable by all of them.
   ─────────────────────────────────────────────────────────────────────────── */
(function () {
  'use strict';

  /* ── Constants ───────────────────────────────────────────────────────── */

  var VB_W = 1000;              // SVG user units across the room, always
  var DEFAULT_ASPECT = 1.35;    // width ÷ height. A wide classroom.

  var MAX_DESKS = 60;           // a hard cap: a security boundary, see validate
  var SEAT_MIN = 1;
  var SEAT_MAX = 6;

  /* Editor limits. Deliberately NARROWER than what `validate` accepts: a
     hand-drag should not be able to make a desk that fills the room, but a
     layout that arrives from elsewhere with a 0.9-wide desk is legal data and
     must not be rejected on read. */
  var EDIT_MIN_DIM = 0.03;
  var EDIT_MAX_DIM = 0.60;

  var UNDO_CAP = 50;

  var HANDLE_HIT_PX = 44;       // ≥40 CSS px of hit target, at ANY zoom
  var ROTATE_SNAP_DEG = 15;     // with Shift held
  var NUDGE = 0.004;            // arrow key, in normalised room units
  var NUDGE_BIG = 5;            // Shift multiplier

  /* ⚠️ ARRAYS, not object maps, and `indexOf`, not a property lookup.
     `SHAPES["toString"]` is truthy on an object literal, so a desk arriving
     from the vision model with shape "constructor" walked straight through
     validation, was rebuilt into the output layout, drew as a rectangle and
     PERSISTED — the database CHECK constrains `front` but not per-desk shape.
     `validate()` is a security boundary for model-generated JSON, so its
     membership tests must not be inherited-property lookups. */
  var FRONTS = ['top', 'right', 'bottom', 'left'];
  var SHAPES = ['rect', 'round'];
  function isOneOf(list, v) {
    return typeof v === 'string' && list.indexOf(v) !== -1;
  }

  /* A desk id ends up inside a CSS attribute selector and inside a seat id, so
     it is whitelisted rather than escaped. ':' is banned outright — it is the
     seat separator. */
  var ID_RE = /^[A-Za-z0-9_-]{1,64}$/;

  var PI = Math.PI;

  /* ── Small numeric helpers ───────────────────────────────────────────── */

  /* Coerce to a finite number, or return null. Accepts a numeric STRING
     because this function is on the path of model-generated JSON, where "0.42"
     is a completely ordinary thing to be handed. Rejects '', ' ', true, null,
     [], NaN, Infinity — `Number('')` is 0 and `Number(true)` is 1, and both of
     those turning into a real coordinate is exactly the silent corruption this
     is here to stop. */
  function num(v) {
    if (typeof v === 'number') { return isFinite(v) ? v : null; }
    if (typeof v === 'string') {
      var t = v.trim();
      if (t === '') return null;
      var n = Number(t);
      return isFinite(n) ? n : null;
    }
    return null;
  }

  function clamp(v, lo, hi) { return v < lo ? lo : (v > hi ? hi : v); }

  /* Into (-180, 180]. 190 -> -170, 360 -> 0, -540 -> 180. */
  function wrapDeg(d) {
    var x = d % 360;
    if (x > 180) x -= 360;
    if (x <= -180) x += 360;
    return x === 0 ? 0 : x;      // kill the -0 that % can produce
  }

  function clone(o) { return JSON.parse(JSON.stringify(o)); }

  /* Rotate an offset clockwise-as-seen, in SVG's y-down space. This is exactly
     the matrix SVG's own `transform="rotate(a)"` applies, so anything computed
     here lines up with anything rendered with that attribute. */
  function rotOff(dx, dy, deg) {
    var r = deg * PI / 180, c = Math.cos(r), s = Math.sin(r);
    return { x: dx * c - dy * s, y: dx * s + dy * c };
  }

  function metricsFor(aspect) {
    var a = num(aspect);
    if (a === null || a <= 0) a = DEFAULT_ASPECT;
    return { w: VB_W, h: VB_W / a, aspect: a };
  }

  /* The unit vector pointing AWAY from the front wall, in SVG space. This is
     the direction a student's back faces: they sit on the far side of the desk
     and look back towards the board. */
  function awayVec(front) {
    if (front === 'bottom') return { x: 0, y: -1 };
    if (front === 'left')   return { x: 1, y: 0 };
    if (front === 'right')  return { x: -1, y: 0 };
    return { x: 0, y: 1 };                            // 'top'
  }

  /* ── Desk geometry in SVG space ──────────────────────────────────────── */

  /* A desk's box in SVG user units.

     ⚠️ ROUND DESKS ARE TRUE CIRCLES. The stored model keeps h === w for a
     round desk (the contract, enforced by `validate`), but a value normalised
     against room width and the same value normalised against room height are
     two DIFFERENT lengths in a non-square room — so rendering rx from one and
     ry from the other would draw a 1.35:1 oval and call it a round table. A
     round table in a real room is round. Both radii come from `w`. */
  function deskBox(desk, M) {
    var wSvg = desk.w * M.w;
    var hSvg = (desk.shape === 'round') ? wSvg : desk.h * M.h;
    return {
      cx: desk.x * M.w, cy: desk.y * M.h,
      w: wSvg, h: hSvg,
      rot: desk.rotation || 0,
      round: desk.shape === 'round'
    };
  }

  /* Half-extents of the AXIS-ALIGNED box that contains a rotated desk. Used
     for clamping to the room and for the coarse pass of the overlap report. */
  function halfExtents(box) {
    if (box.round) { return { hx: box.w / 2, hy: box.w / 2 }; }
    var r = box.rot * PI / 180;
    var c = Math.abs(Math.cos(r)), s = Math.abs(Math.sin(r));
    return { hx: (box.w * c + box.h * s) / 2, hy: (box.w * s + box.h * c) / 2 };
  }

  /* ── Seat geometry — the bit that makes it read as a real classroom ──────
     Students face the front. So a seat sits on the desk edge FARTHER FROM THE
     FRONT WALL: the student is behind the desk, looking past it at the board.
     Put the seats on the near edge instead and every plan in the school reads
     back-to-front.

     Which edge is "farther from the front" is decided AFTER rotation, in room
     space, not from the desk's local frame — so rotating a desk 180 degrees
     leaves its students where they were (the desk turned round, the room did
     not) instead of teleporting them to the board side.

     THE TIE-BREAK IS LOAD-BEARING. A desk rotated 90 degrees has both its long
     edges at the same distance from a top or bottom front wall, and the dot
     product is 0. Left to a bare `>= 0` that would put every side desk's
     students on the same arbitrary side, which is what turns a horseshoe into
     a mess: on the left arm of a U the students belong on the LEFT of the
     desk, on the right arm they belong on the RIGHT — i.e. on the side away
     from the middle of the room, facing in. So the tie-break is "farther from
     the room centre", and a U-shape comes out right for free.

     1..3 seats: all along the far long edge.
     4..6 seats: split BOTH long edges, ceil(n/2) far, the rest near. That is
     what a cluster of six actually is — two facing rows of three — and it is
     the only arrangement in which six chairs fit round one table. */

  /* How far a chair sits OUT from the desk edge, as a fraction of its own
     radius. 0 puts the seat's CENTRE on the edge, so half the chair is buried
     in the desk — which draws every table as a car with wheels and, on the
     printed plan, lays each name half on the desk fill. 1 would push the chair
     clear of the desk entirely, which is not what a classroom looks like
     either. 0.62 leaves it mostly outside and slightly tucked, the way a chair
     actually stands at a table. */
  var SEAT_TUCK = 0.62;

  function seatPlacement(box, seats, front, M) {
    var away = awayVec(front);
    var out = [];
    var i;

    if (box.round) {
      var r = box.w / 2;
      /* First seat at the far-from-front point when the desk is unrotated;
         rotation then turns the whole ring, which is the only way rotation can
         show on a circle. */
      var base = Math.atan2(away.y, away.x) * 180 / PI + box.rot;
      var step = 360 / seats;
      var ringR = 2 * PI * r / seats;
      var sr = clamp(Math.min(ringR * 0.42, r * 0.44), 7, 26);
      for (i = 0; i < seats; i++) {
        var a = (base + i * step) * PI / 180;
        var rr = r + sr * SEAT_TUCK;
        out.push({ x: box.cx + Math.cos(a) * rr, y: box.cy + Math.sin(a) * rr, r: sr });
      }
      return out;
    }

    /* Rect. The seat rail runs along the LONGER local dimension; the seats sit
       off the shorter one. A desk deeper than it is wide (a bench turned end
       on) therefore seats along its length, which is what a bench is for. */
    var alongX = box.w >= box.h;
    var L = alongX ? box.w : box.h;      // rail length
    var S = alongX ? box.h : box.w;      // depth: how far out the seats sit

    var pLocal = alongX ? { x: 0, y: 1 } : { x: 1, y: 0 };
    var pWorld = rotOff(pLocal.x, pLocal.y, box.rot);
    var dot = pWorld.x * away.x + pWorld.y * away.y;
    var sign;
    if (Math.abs(dot) > 1e-6) {
      sign = dot > 0 ? 1 : -1;
    } else {
      var toC = { x: M.w / 2 - box.cx, y: M.h / 2 - box.cy };
      sign = (pWorld.x * toC.x + pWorld.y * toC.y) <= 0 ? 1 : -1;   // away from centre
    }

    var far = seats <= 3 ? seats : Math.ceil(seats / 2);
    var near = seats - far;
    var maxRow = Math.max(far, near);
    var sr2 = clamp(Math.min((L / maxRow) * 0.42, S * 0.40), 7, 26);

    function row(count, side, startIndex) {
      for (var k = 0; k < count; k++) {
        var t = ((k + 0.5) / count - 0.5) * L;             // evenly spaced
        var b = side * (S / 2 + sr2 * SEAT_TUCK);
        var loc = alongX ? { x: t, y: b } : { x: b, y: t };
        var wv = rotOff(loc.x, loc.y, box.rot);
        out[startIndex + k] = { x: box.cx + wv.x, y: box.cy + wv.y, r: sr2 };
      }
    }
    row(far, sign, 0);
    if (near > 0) row(near, -sign, far);
    return out;
  }

  /* ── Seat ids, in reading order ──────────────────────────────────────────
     Sorting desks by y alone is not reading order: two desks in the same row
     whose centres differ by a thousandth interleave, and the teacher's tab
     order (and the printed register) zig-zags across the room. So the desks
     are BANDED into rows first — anything within half a desk-depth of the band
     leader is in that row — and sorted left-to-right inside the band. Ties
     inside a band break on desk id, so the order is stable and deterministic
     for a given layout rather than dependent on array order. */
  function orderedDesks(desks) {
    var list = desks.slice();
    if (!list.length) return list;

    var hs = list.map(function (d) { return d.h; }).sort(function (a, b) { return a - b; });
    var medianH = hs[Math.floor(hs.length / 2)] || 0.06;
    var band = Math.max(medianH * 0.5, 0.03);

    list.sort(function (a, b) {
      if (a.y !== b.y) return a.y - b.y;
      if (a.x !== b.x) return a.x - b.x;
      return a.id < b.id ? -1 : 1;
    });

    var rows = [], cur = [list[0]], top = list[0].y;
    for (var i = 1; i < list.length; i++) {
      if (list[i].y - top <= band) { cur.push(list[i]); }
      else { rows.push(cur); cur = [list[i]]; top = list[i].y; }
    }
    rows.push(cur);

    var out = [];
    rows.forEach(function (r) {
      r.sort(function (a, b) {
        if (a.x !== b.x) return a.x - b.x;
        return a.id < b.id ? -1 : 1;
      });
      out = out.concat(r);
    });
    return out;
  }

  function seatIdsOf(layout) {
    var l = (layout && layout.desks) ? layout : { desks: [] };
    var ids = [];
    orderedDesks(l.desks || []).forEach(function (d) {
      var n = d.seats || 0;
      for (var i = 0; i < n; i++) { ids.push(d.id + ':' + i); }
    });
    return ids;
  }

  /* ── validate() — a SECURITY BOUNDARY, not a convenience ─────────────────
     This runs on two inputs and both of them are hostile by default:
       · a row read back out of the database, which may predate any given
         schema change and may have been written by an older build;
       · the JSON a model returns when it is asked to look at a PHOTOGRAPH of a
         classroom and describe the desks. That output is prose-shaped, will
         occasionally hand back "0.4" as a string, 400 desks, a rotation of
         1440, a NaN, or a desk id with a quote in it.

     The split between REJECT and NORMALISE is the whole design:
       normalise when the author's intent is unambiguous and recoverable —
         a numeric string, a rotation that has gone round the clock, a round
         desk whose h drifted off its w, a missing id;
       reject when it is not — NaN, a coordinate outside the room, a
         zero-width desk, seven seats, sixty-one desks, a duplicate id.
     Guessing on the second group would put a desk somewhere the teacher did
     not ask for and give them no way to know. An error tells them.

     Returns {ok:true, layout, warnings:[…]} or {ok:false, errors:[…]}.
     The returned layout is REBUILT from whitelisted keys — anything else the
     input carried is dropped rather than passed through, so a stray field
     cannot ride into storage. */
  function validate(input) {
    var errors = [], warnings = [];

    if (!input || typeof input !== 'object' || Array.isArray(input)) {
      return { ok: false, errors: ['layout must be an object'] };
    }

    /* Version. Unknown future versions are refused rather than best-guessed:
       a v2 with a different unit convention read as v1 draws a wrong room. */
    var v = num(input.v);
    if (v === null) { warnings.push('v missing; assumed 1'); v = 1; }
    else if (v !== 1) { errors.push('unsupported layout version: ' + input.v); }

    var front = input.front;
    if (front === undefined || front === null) {
      warnings.push("front missing; assumed 'top'");
      front = 'top';
    } else if (!isOneOf(FRONTS, front)) {
      errors.push('unknown front: ' + JSON.stringify(input.front));
      front = 'top';
    }

    /* One rect-ish body, shared by desks and the teacher desk. `where` is only
       for the error text — an error that does not say WHICH desk is an error a
       teacher cannot act on. */
    function body(o, where, opts) {
      var out = {}, bad = false;
      ['x', 'y', 'w', 'h'].forEach(function (k) {
        var n = num(o[k]);
        if (n === null) { errors.push(where + ': ' + k + ' is not a finite number'); bad = true; return; }
        if (typeof o[k] === 'string') { warnings.push(where + ': ' + k + ' coerced from string'); }
        if (k === 'w' || k === 'h') {
          if (n <= 0) { errors.push(where + ': ' + k + ' must be greater than 0'); bad = true; return; }
        }
        if (n < 0 || n > 1) { errors.push(where + ': ' + k + ' = ' + n + ' is outside 0..1'); bad = true; return; }
        out[k] = n;
      });

      var r = num(o.rotation);
      if (o.rotation === undefined || o.rotation === null) { r = 0; }
      else if (r === null) { errors.push(where + ': rotation is not a finite number'); bad = true; r = 0; }
      else if (r < -180 || r > 180) {
        var w2 = wrapDeg(r);
        warnings.push(where + ': rotation ' + r + ' wrapped to ' + w2);
        r = w2;
      }
      out.rotation = r;

      if (opts && opts.round && !bad) {
        /* A round desk's h is not free: it is the same measurement as w. If it
           has drifted, w wins — w is the diameter by contract and the renderer
           reads it. */
        if (out.h !== out.w) {
          warnings.push(where + ': round desk h (' + out.h + ') squared up to w (' + out.w + ')');
          out.h = out.w;
        }
      }
      return bad ? null : out;
    }

    var desks = input.desks;
    var outDesks = [];
    if (desks === undefined || desks === null) {
      warnings.push('desks missing; assumed empty');
      desks = [];
    }
    if (!Array.isArray(desks)) {
      errors.push('desks must be an array');
      desks = [];
    }
    if (desks.length > MAX_DESKS) {
      /* NOT truncated. A photo scan that returns 400 desks has misread the
         room, and quietly keeping the first 60 would hand back a plausible-
         looking plan built from a failure. */
      errors.push('too many desks: ' + desks.length + ' (max ' + MAX_DESKS + ')');
    }

    var seen = Object.create(null);
    desks.forEach(function (d, i) {
      var where = 'desk[' + i + ']';
      if (!d || typeof d !== 'object' || Array.isArray(d)) {
        errors.push(where + ' is not an object'); return;
      }

      var id = d.id;
      if (id === undefined || id === null || id === '') {
        id = 'd' + (i + 1);
        warnings.push(where + ': id missing; assigned ' + id);
      } else if (typeof id !== 'string' || !ID_RE.test(id)) {
        errors.push(where + ': id ' + JSON.stringify(d.id) +
                    ' is not [A-Za-z0-9_-]{1,64} (a colon would split the seat id)');
        return;
      }
      if (seen[id]) { errors.push(where + ': duplicate desk id ' + id); return; }
      seen[id] = 1;
      where = 'desk ' + id;

      var shape = d.shape === undefined || d.shape === null ? 'rect' : d.shape;
      if (!isOneOf(SHAPES, shape)) {
        errors.push(where + ': unknown shape ' + JSON.stringify(d.shape)); return;
      }

      var s = num(d.seats);
      if (s === null) { errors.push(where + ': seats is not a finite number'); return; }
      if (s !== Math.floor(s)) { errors.push(where + ': seats must be a whole number, got ' + s); return; }
      if (s < SEAT_MIN || s > SEAT_MAX) {
        errors.push(where + ': seats = ' + s + ' is outside ' + SEAT_MIN + '..' + SEAT_MAX); return;
      }

      var b = body(d, where, { round: shape === 'round' });
      if (!b) return;

      outDesks.push({
        id: id, shape: shape,
        x: b.x, y: b.y, w: b.w, h: b.h,
        rotation: b.rotation, seats: s
      });
    });

    var td = null;
    if (input.teacher_desk !== undefined && input.teacher_desk !== null) {
      if (typeof input.teacher_desk !== 'object' || Array.isArray(input.teacher_desk)) {
        errors.push('teacher_desk must be an object or null');
      } else {
        var tb = body(input.teacher_desk, 'teacher_desk', null);
        if (tb) td = { x: tb.x, y: tb.y, w: tb.w, h: tb.h, rotation: tb.rotation };
      }
    }

    if (errors.length) return { ok: false, errors: errors };
    return {
      ok: true,
      warnings: warnings,
      // `seq` rides along so the monotonic desk-id counter survives a
      // save/reload; absent on older rows, derived from the desks then.
      layout: { v: 1, seq: num(input.seq) || 0, front: front,
                teacher_desk: td, desks: outDesks }
    };
  }

  function emptyLayout() {
    return { v: 1, front: 'top', teacher_desk: null, desks: [] };
  }

  /* ── overlapReport() ─────────────────────────────────────────────────────
     NOT used by the editor. Real rooms have desks pushed together, and an
     editor that refused to let two desks touch would be an editor that cannot
     draw a cluster. This exists to sanity-check the output of a PHOTO SCAN,
     where two desks on top of each other means the scan saw one desk twice.

     Exact convex-polygon intersection area (Sutherland–Hodgman clip, then the
     shoelace formula) rather than an AABB test, because rotation is the whole
     point of this canvas and two desks at 45 degrees have wildly overlapping
     bounding boxes while not touching at all. Round desks are approximated as
     a 24-gon: the error is under 1% of area and this is a threshold test.

     `area` comes back as a fraction of the ROOM's area — a unit the caller can
     reason about without knowing the aspect. */
  function polyOf(box) {
    if (box.round) {
      var p = [], r = box.w / 2, n = 24;
      for (var i = 0; i < n; i++) {
        var a = (i / n) * 2 * PI;
        p.push({ x: box.cx + Math.cos(a) * r, y: box.cy + Math.sin(a) * r });
      }
      return p;
    }
    var hw = box.w / 2, hh = box.h / 2, out = [];
    [[-hw, -hh], [hw, -hh], [hw, hh], [-hw, hh]].forEach(function (c) {
      var v = rotOff(c[0], c[1], box.rot);
      out.push({ x: box.cx + v.x, y: box.cy + v.y });
    });
    return out;
  }

  function shoelace(p) {
    var a = 0;
    for (var i = 0, n = p.length; i < n; i++) {
      var j = (i + 1) % n;
      a += p[i].x * p[j].y - p[j].x * p[i].y;
    }
    return Math.abs(a) / 2;
  }

  /* Clip subject by the (convex, counter-clockwise-or-clockwise consistent)
     clip polygon. Both of ours are convex and wound the same way by
     construction, which is what makes the single-pass clip valid. */
  function clipPoly(subject, clip) {
    var out = subject;
    for (var i = 0, n = clip.length; i < n && out.length; i++) {
      var a = clip[i], b = clip[(i + 1) % n];
      var input = out; out = [];
      var ex = b.x - a.x, ey = b.y - a.y;
      function side(p) { return ex * (p.y - a.y) - ey * (p.x - a.x); }
      var refSign = 0;
      for (var r = 0; r < clip.length; r++) {
        var s = side(clip[r]);
        if (Math.abs(s) > 1e-9) { refSign = s > 0 ? 1 : -1; break; }
      }
      for (var k = 0, m = input.length; k < m; k++) {
        var cur = input[k], prv = input[(k + m - 1) % m];
        var sc = side(cur) * refSign, sp = side(prv) * refSign;
        if (sc >= 0) {
          if (sp < 0) {
            var t = sp / (sp - sc);
            out.push({ x: prv.x + (cur.x - prv.x) * t, y: prv.y + (cur.y - prv.y) * t });
          }
          out.push(cur);
        } else if (sp >= 0) {
          var t2 = sp / (sp - sc);
          out.push({ x: prv.x + (cur.x - prv.x) * t2, y: prv.y + (cur.y - prv.y) * t2 });
        }
      }
    }
    return out;
  }

  function overlapReport(layout, aspect) {
    var res = validate(layout);
    var l = res.ok ? res.layout : (layout && layout.desks ? layout : emptyLayout());
    var M = metricsFor(aspect);
    var roomArea = M.w * M.h;
    var boxes = (l.desks || []).map(function (d) {
      return { id: d.id, box: deskBox(d, M), poly: polyOf(deskBox(d, M)) };
    });
    var out = [];
    for (var i = 0; i < boxes.length; i++) {
      for (var j = i + 1; j < boxes.length; j++) {
        var A = boxes[i], B = boxes[j];
        // Coarse AABB reject first — most pairs die here and never see the clip.
        var ea = halfExtents(A.box), eb = halfExtents(B.box);
        if (Math.abs(A.box.cx - B.box.cx) > ea.hx + eb.hx) continue;
        if (Math.abs(A.box.cy - B.box.cy) > ea.hy + eb.hy) continue;
        var inter = clipPoly(A.poly, B.poly);
        if (inter.length < 3) continue;
        var area = shoelace(inter);
        /* Tolerance: 2% of the smaller desk. Two desks pushed together share an
           edge, and floating point makes a shared edge overlap by a sliver. A
           sliver is a butt joint; a fifth of a desk is a scan error. */
        var tol = 0.02 * Math.min(shoelace(A.poly), shoelace(B.poly));
        if (area <= tol) continue;
        out.push({ a: A.id, b: B.id, area: area / roomArea });
      }
    }
    return out;
  }

  /* ── Starting templates ──────────────────────────────────────────────────
     Every one of these is a STARTING POINT that the teacher then drags into
     the shape of their actual room, so what matters is that it lands close
     enough to be worth editing rather than close enough to be perfect.

     They are laid out the way a room is laid out, not the way a spreadsheet
     is: a gap at the front for the teacher and the board, real aisles wide
     enough to walk down, outer columns TOED IN towards the board (a desk at
     the far left of a room does not face straight up the room, it faces the
     whiteboard), and rows that drift a little from side to side the way rows
     actually drift by Thursday.

     ⚠️ ENTIRELY DETERMINISTIC. Every offset and angle below is a function of
     the desk's index. No Math.random anywhere — the same seat count must give
     the same room every time, or a teacher who clicks the template twice gets
     two different rooms and stops trusting the button.

     Each takes an approximate SEAT count (not a desk count) and returns a
     complete, valid layout. */

  function defaultTeacherDesk(front) {
    if (front === 'bottom') return { x: 0.16, y: 0.915, w: 0.17, h: 0.055, rotation: 0 };
    if (front === 'left')   return { x: 0.085, y: 0.16, w: 0.055, h: 0.17, rotation: 0 };
    if (front === 'right')  return { x: 0.915, y: 0.16, w: 0.055, h: 0.17, rotation: 0 };
    return { x: 0.16, y: 0.085, w: 0.17, h: 0.055, rotation: 0 };
  }

  function wantSeats(n, dflt, lo, hi) {
    var v = num(n);
    if (v === null) v = dflt;
    return clamp(Math.round(v), lo, hi);
  }

  function finish(desks, front) {
    return { v: 1, front: front || 'top', teacher_desk: defaultTeacherDesk(front || 'top'), desks: desks };
  }

  /* Rows of single desks, six across with a central aisle. The default UK
     "exam-ish" arrangement, and the one a cover teacher can read at a glance. */
  function tplRows(seats) {
    var n = wantSeats(seats, 30, 1, MAX_DESKS);
    var COLS = 6, W = 0.095, H = 0.062, GAP = 0.030, AISLE = 0.090;
    var span = COLS * W + (COLS - 2) * GAP + AISLE;
    var x0 = (1 - span) / 2 + W / 2;
    var desks = [], i;
    for (i = 0; i < n; i++) {
      var col = i % COLS, row = Math.floor(i / COLS);
      var x = x0 + col * (W + GAP) + (col >= COLS / 2 ? (AISLE - GAP) : 0);
      // Rows drift. Alternating, small, deterministic — it stops the eye
      // reading a grid without making anything hard to find.
      x += (row % 2) ? 0.010 : -0.006;
      var y = 0.22 + row * 0.145;
      desks.push({
        id: 'd' + (i + 1), shape: 'rect',
        x: clamp(x, 0.06, 0.94), y: clamp(y, 0.06, 0.94), w: W, h: H,
        // Toed in towards the board, and more so further back.
        rotation: wrapDeg((((COLS - 1) / 2) - col) * (1.6 + row * 0.5)),
        seats: 1
      });
    }
    return finish(desks, 'top');
  }

  /* Paired desks, three pairs across, two aisles. The everyday arrangement:
     talk partners, but still all facing the board. */
  function tplPairedRows(seats) {
    var n = wantSeats(seats, 30, 2, MAX_DESKS * 2);
    var pairs = Math.ceil(n / 2);
    var COLS = 3, W = 0.20, H = 0.065, AISLE = 0.09;
    var span = COLS * W + (COLS - 1) * AISLE;
    var x0 = (1 - span) / 2 + W / 2;
    var desks = [], left = n;
    for (var i = 0; i < pairs; i++) {
      var col = i % COLS, row = Math.floor(i / COLS);
      var x = x0 + col * (W + AISLE) + ((row % 2) ? 0.008 : -0.005);
      desks.push({
        id: 'd' + (i + 1), shape: 'rect',
        x: clamp(x, 0.11, 0.89), y: clamp(0.22 + row * 0.145, 0.06, 0.94),
        w: W, h: H,
        rotation: wrapDeg((((COLS - 1) / 2) - col) * (2.4 + row * 0.4)),
        seats: Math.min(2, left)
      });
      left -= 2;
    }
    return finish(desks, 'top');
  }

  /* Horseshoe. Two long benches down each side wall, three across the back,
     and — only if the class is bigger than the horseshoe holds — island desks
     in the middle, which is what a real room does when the U runs out.

     The side benches are rotated 90 degrees, which is precisely the case the
     seat tie-break exists for: their two long edges are the same distance from
     a front wall at the top, and the students belong on the OUTSIDE, facing
     in. See seatPlacement. */
  function tplUShape(seats) {
    var n = wantSeats(seats, 24, 3, 37);
    var desks = [];
    var slots = [
      { id: 'L1', x: 0.10, y: 0.42, w: 0.17, h: 0.055, rotation: 90 },
      { id: 'L2', x: 0.10, y: 0.68, w: 0.17, h: 0.055, rotation: 90 },
      { id: 'R1', x: 0.90, y: 0.42, w: 0.17, h: 0.055, rotation: 90 },
      { id: 'R2', x: 0.90, y: 0.68, w: 0.17, h: 0.055, rotation: 90 },
      { id: 'B1', x: 0.30, y: 0.86, w: 0.20, h: 0.055, rotation: 3 },
      { id: 'B2', x: 0.51, y: 0.87, w: 0.20, h: 0.055, rotation: 0 },
      { id: 'B3', x: 0.72, y: 0.86, w: 0.20, h: 0.055, rotation: -3 }
    ];
    /* The U caps at 3 seats a bench. A 4-seat bench splits its seats across
       BOTH long edges, which on a horseshoe would seat half the class facing
       out of the room at a wall. */
    var left = n, i;
    var per = [];
    for (i = 0; i < slots.length; i++) per.push(0);
    while (left > 0) {
      var placed = false;
      for (i = 0; i < slots.length && left > 0; i++) {
        if (per[i] < 3) { per[i]++; left--; placed = true; }
      }
      if (!placed) break;
    }
    slots.forEach(function (s, k) {
      if (per[k] <= 0) return;
      desks.push({ id: s.id, shape: 'rect', x: s.x, y: s.y, w: s.w, h: s.h,
                   rotation: s.rotation, seats: per[k] });
    });

    // Islands in the middle of the U, in fixed order, up to 4 seats each.
    var inner = [
      { id: 'M1', x: 0.37, y: 0.50 }, { id: 'M2', x: 0.63, y: 0.50 },
      { id: 'M3', x: 0.37, y: 0.68 }, { id: 'M4', x: 0.63, y: 0.68 }
    ];
    var m = 0;
    while (left > 0 && m < inner.length) {
      var take = Math.min(4, left);
      desks.push({ id: inner[m].id, shape: 'rect', x: inner[m].x, y: inner[m].y,
                   w: 0.17, h: 0.065, rotation: (m % 2 ? -4 : 4), seats: take });
      left -= take; m++;
    }
    return finish(desks, 'top');
  }

  /* Group tables. Six-seat clusters — three one side, three the other — set at
     small angles and staggered, because a room full of clusters is never
     square to the walls once the class has been in it. */
  function tplClusters(seats) {
    var n = wantSeats(seats, 30, 2, 36);
    var slots = [
      { x: 0.20, y: 0.34, rot: -8 }, { x: 0.51, y: 0.31, rot: 5 },
      { x: 0.81, y: 0.34, rot: -4 }, { x: 0.20, y: 0.68, rot: 7 },
      { x: 0.51, y: 0.71, rot: -6 }, { x: 0.81, y: 0.68, rot: 3 }
    ];
    var tables = clamp(Math.ceil(n / 6), 1, slots.length);
    var base = Math.floor(n / tables), extra = n % tables;
    var desks = [];
    for (var i = 0; i < tables; i++) {
      var count = clamp(base + (i < extra ? 1 : 0), 1, SEAT_MAX);
      desks.push({
        id: 'g' + (i + 1), shape: 'rect',
        x: slots[i].x, y: slots[i].y, w: 0.19, h: 0.115,
        rotation: slots[i].rot, seats: count
      });
    }
    return finish(desks, 'top');
  }

  /* ── Styles ──────────────────────────────────────────────────────────────
     Injected once per document, scoped entirely under `.sc-root`.

     NO COLOUR IS HARD-CODED as a decision. Every value is a studio design-
     system token from shared/teacher-ds.css with a literal fallback, so the
     canvas takes the surface's palette wherever it is mounted and still draws
     correctly on a page that has not loaded the token sheet at all (the print
     view, a fixture, this file's own harness).

     ⚠️ The cursor and outline rules are keyed on the MODE class, not on a
     disabled attribute. In `view` there is no grab cursor, no focus ring, no
     drop outline and — see renderHandles — no handle element in the DOM at
     all. A control a user cannot use must be ABSENT, not present and greyed:
     greying it out still says "there is a thing here for you", which on a
     read-only plan shared with a cover teacher is a lie. */
  var STYLE_ID = 'sc-canvas-styles-v1';
  var CSS = [
    '.sc-root{position:relative;width:100%;',
      "font-family:var(--st-ui,'Instrument Sans',system-ui,sans-serif);",
      'color:var(--st-ink,#1A1714);}',
    '.sc-svg{display:block;width:100%;height:auto;touch-action:none;',
      '-webkit-user-select:none;user-select:none;',
      'background:var(--st-paper,#FFFDF8);',
      'border:1px solid var(--st-rule,#E0D2B9);',
      'border-radius:var(--st-r-card,11px);}',
    '.sc-room{fill:var(--st-paper,#FFFDF8);}',
    '.sc-front-bar{fill:var(--st-ink,#1A1714);}',
    ".sc-front-label{fill:var(--st-cream,#FBF3E6);font-family:var(--st-mono,ui-monospace,monospace);",
      'font-size:15px;letter-spacing:0.26em;text-anchor:middle;dominant-baseline:central;}',
    /* --st-num-well, not --st-ground: a desk filled with the page's own
       ground colour is a 2%-contrast rectangle, and on a PRINTED plan (which
       is where this drawing spends most of its life) it disappears entirely
       behind the chairs. The well tint is the darkest neutral in the set that
       is still clearly furniture rather than ink. */
    '.sc-desk-shape{fill:var(--st-num-well,#F2E8D6);stroke:var(--st-rule-strong,#D6C6A8);stroke-width:2;}',
    '.sc-desk[data-selected="1"] .sc-desk-shape{stroke:var(--st-accent,#E4572E);stroke-width:3.5;}',
    '.sc-teacher-shape{fill:var(--st-note-bg,#F5EAD6);stroke:var(--st-accent,#E4572E);',
      'stroke-width:2;stroke-dasharray:7 4;}',
    '.sc-teacher-label{fill:var(--st-accent-text,#A93411);font-size:15px;font-weight:600;',
      'text-anchor:middle;dominant-baseline:central;}',
    '.sc-seat-dot{fill:var(--st-paper,#FFFDF8);stroke:var(--st-rule-strong,#D6C6A8);stroke-width:1.6;}',
    '.sc-seat[data-filled="1"] .sc-seat-dot{fill:var(--st-chip-tint,#FCEFE9);',
      'stroke:var(--st-accent,#E4572E);stroke-width:2;}',
    '.sc-seat-label{fill:var(--st-ink,#1A1714);text-anchor:middle;dominant-baseline:central;',
      'font-weight:600;pointer-events:none;}',
    '.sc-handle-hit{fill:transparent;stroke:none;}',
    '.sc-handle-dot{fill:var(--st-paper,#FFFDF8);stroke:var(--st-accent,#E4572E);stroke-width:2.5;}',
    '.sc-handle-stem{stroke:var(--st-accent,#E4572E);stroke-width:1.5;stroke-dasharray:4 3;}',
    '.sc-ghost{pointer-events:none;}',
    '.sc-ghost-dot{fill:var(--st-chip-tint,#FCEFE9);stroke:var(--st-accent,#E4572E);stroke-width:2;}',
    /* mode-scoped affordances — none of these selectors can match in view */
    '.sc-mode-edit .sc-desk{cursor:grab;}',
    '.sc-mode-edit .sc-desk[data-selected="1"]{cursor:grabbing;}',
    '.sc-mode-edit .sc-handle[data-handle="rotate"]{cursor:grab;}',
    '.sc-mode-edit .sc-handle[data-handle="resize"]{cursor:nwse-resize;}',
    '.sc-mode-plan .sc-seat{cursor:pointer;}',
    '.sc-mode-edit .sc-desk:focus-visible .sc-desk-shape,',
    '.sc-mode-plan .sc-seat:focus-visible .sc-seat-dot{stroke:var(--st-accent-text,#A93411);stroke-width:4;}',
    '.sc-mode-edit .sc-desk:focus,.sc-mode-plan .sc-seat:focus{outline:none;}',
    '.sc-seat[data-drop="1"] .sc-seat-dot{stroke:var(--st-accent,#E4572E);stroke-width:3.5;',
      'stroke-dasharray:5 3;}'
  ].join('');

  /* Put the sheet somewhere it can actually reach the drawing.

     The obvious `doc.head.appendChild` is wrong here, and it was wrong in the
     way that showed up as blank thumbnails on the Rooms and Plans lists. Every
     card on those lists is built by seating.html's `el()` helper, which fills a
     <template> and hands back `content.firstElementChild` — so at the moment
     create() runs, the mount is still inside the template's INERT contents
     document, which has neither a <head> nor a documentElement.
     `(doc.head || doc.documentElement)` was therefore null, appendChild threw a
     TypeError, and the throw was swallowed by the catch around each card's
     create call. Every canvas silently drew nothing.

     Do NOT "fix" this by appending the sheet to the fragment root instead. The
     card loops append only the card element to the grid, so a <style> sitting
     beside it inside the fragment is left behind and dropped on the floor — the
     thumbnails would come back unstyled rather than blank, which is a quieter
     failure and a harder one to spot. The fragment is on its way into the live
     page, so the LIVE document's head is the right host: one shared sheet there
     styles every card that lands. Appending to the mount itself is the last
     resort, for a mount that belongs to no real document at all — the sheet
     then travels with the element wherever it goes.

     This function never throws. A missing stylesheet is a cosmetic problem; a
     throw from here is a blank canvas. */
  function injectStyles(doc, mount) {
    var host = doc && (doc.head || doc.documentElement);
    if (host) {
      if (doc.getElementById && doc.getElementById(STYLE_ID)) return;
    } else if (typeof document !== 'undefined' &&
               (document.head || document.documentElement)) {
      if (document.getElementById(STYLE_ID)) return;
      host = document.head || document.documentElement;
      doc = document;
    } else if (mount && mount.appendChild && mount.querySelector) {
      if (mount.querySelector('#' + STYLE_ID)) return;
      host = mount;
      doc = mount.ownerDocument || doc;
    }
    if (!host || !doc || !doc.createElement) return;
    var s = doc.createElement('style');
    s.id = STYLE_ID;
    s.textContent = CSS;
    host.appendChild(s);
  }

  /* ── DOM helpers ─────────────────────────────────────────────────────── */

  var NS = 'http://www.w3.org/2000/svg';

  function svgEl(tag, attrs) {
    var e = document.createElementNS(NS, tag);
    if (attrs) { for (var k in attrs) { if (attrs[k] !== null && attrs[k] !== undefined) e.setAttribute(k, attrs[k]); } }
    return e;
  }

  function r2(n) { return Math.round(n * 100) / 100; }

  /* Fit a name into a seat circle.

     A seat is small and a name is not, so this degrades in three steps rather
     than one: whole name if it fits, truncated with an ellipsis if there is
     room for at least three characters, and INITIALS below that — "SP" reads
     as a person, "S…" reads as nothing. The full name always goes on a
     <title>, so hover and every screen reader get the real thing whatever the
     circle shows. */
  function fitLabel(label, maxChars) {
    var s = String(label == null ? '' : label).trim();
    if (!s) return '';
    if (maxChars >= s.length) return s;
    if (maxChars >= 3) return s.slice(0, maxChars - 1) + '…';
    var parts = s.split(/\s+/).filter(Boolean);
    var ini = parts.map(function (p) { return p.charAt(0).toUpperCase(); }).join('');
    return ini.slice(0, Math.max(1, maxChars));
  }

  /* ── The instance ────────────────────────────────────────────────────── */

  function create(opts) {
    opts = opts || {};
    var mount = typeof opts.mount === 'string'
      ? document.querySelector(opts.mount) : opts.mount;
    if (!mount || !mount.appendChild) {
      throw new Error('SeatingCanvas.create: opts.mount must be an element or a selector that matches one');
    }

    var mode = (opts.mode === 'plan' || opts.mode === 'view') ? opts.mode : 'edit';
    var M = metricsFor(opts.aspect);
    var layout;
    var assignments = {};
    var selected = null;
    var undoStack = [], redoStack = [];
    var gesture = null;
    var nudgeMark = 0;              // undo coalescing for held arrow keys
    var destroyed = false;

    var cb = {
      change: typeof opts.onChange === 'function' ? opts.onChange : null,
      select: typeof opts.onSelect === 'function' ? opts.onSelect : null,
      seat: typeof opts.onSeatActivate === 'function' ? opts.onSeatActivate : null,
      assign: typeof opts.onAssign === 'function' ? opts.onAssign : null
    };

    // -- initial layout ---------------------------------------------------
    (function () {
      var src = opts.layout || emptyLayout();
      var res = validate(src);
      if (!res.ok) {
        throw new Error('SeatingCanvas.create: invalid layout — ' + res.errors.join('; '));
      }
      layout = res.layout;
    })();

    injectStyles(mount.ownerDocument || document, mount);

    // -- DOM --------------------------------------------------------------
    var root = document.createElement('div');
    root.className = 'sc-root sc-mode-' + mode;
    var svg = svgEl('svg', {
      'class': 'sc-svg',
      viewBox: '0 0 ' + r2(M.w) + ' ' + r2(M.h),
      preserveAspectRatio: 'xMidYMid meet',
      role: 'group'
    });
    var lRoom = svgEl('g', { 'class': 'sc-layer-room' });
    var lFront = svgEl('g', { 'class': 'sc-layer-front' });
    var lTeacher = svgEl('g', { 'class': 'sc-layer-teacher' });
    var lDesks = svgEl('g', { 'class': 'sc-layer-desks' });
    var lHandles = svgEl('g', { 'class': 'sc-layer-handles' });
    var lGhost = svgEl('g', { 'class': 'sc-layer-ghost' });
    svg.appendChild(lRoom); svg.appendChild(lFront); svg.appendChild(lTeacher);
    svg.appendChild(lDesks); svg.appendChild(lHandles); svg.appendChild(lGhost);
    root.appendChild(svg);
    mount.appendChild(root);

    lRoom.appendChild(svgEl('rect', { 'class': 'sc-room', x: 0, y: 0, width: r2(M.w), height: r2(M.h) }));

    /* ── screen-space measurement ────────────────────────────────────────
       Handles are drawn in SVG user units but must be GRABBABLE in CSS pixels:
       the brief's 40px minimum is a finger, and a finger does not get smaller
       when the plan is scaled down to fit an iPad in portrait. getScreenCTM().a
       is CSS px per user unit, so its reciprocal converts a px budget into the
       user units the hit circle has to be drawn at. Recomputed on every resize
       and before every handle render, because the SVG is width:100% and the
       scale changes whenever the column does. */
    function unitsPerPx() {
      var m = null;
      try { m = svg.getScreenCTM(); } catch (e) { m = null; }
      if (!m || !m.a) return 1;
      return 1 / m.a;
    }

    function toSvgPoint(clientX, clientY) {
      var m = null;
      try { m = svg.getScreenCTM(); } catch (e) { m = null; }
      if (!m) return { x: 0, y: 0 };
      var p = svg.createSVGPoint();
      p.x = clientX; p.y = clientY;
      var q = p.matrixTransform(m.inverse());
      return { x: q.x, y: q.y };
    }

    // -- model helpers ----------------------------------------------------

    function deskById(id) {
      for (var i = 0; i < layout.desks.length; i++) {
        if (layout.desks[i].id === id) return layout.desks[i];
      }
      return null;
    }

    function nextDeskId() {
      var n = 1, used = {};
      layout.desks.forEach(function (d) { used[d.id] = 1; });
      while (used['d' + n]) n++;
      return 'd' + n;
    }

    function emitChange() { if (cb.change) cb.change(clone(layout)); }

    function pushUndo(before) {
      undoStack.push(before);
      if (undoStack.length > UNDO_CAP) undoStack.shift();
      redoStack.length = 0;
    }

    /* One gesture = one undo entry. `snapshot()` is taken at pointerdown and
       banked at pointerup ONLY if something actually changed — otherwise a
       click that selects a desk without moving it would fill the stack with
       no-ops and the teacher's first Ctrl-Z would appear to do nothing. */
    function snapshot() { return clone(layout); }

    function bank(before) {
      if (JSON.stringify(before) === JSON.stringify(layout)) return false;
      pushUndo(before);
      emitChange();
      return true;
    }

    // -- rendering --------------------------------------------------------

    function renderFront() {
      while (lFront.firstChild) lFront.removeChild(lFront.firstChild);
      var T = 26, f = layout.front, bar, tx, ty, rot = 0;
      if (f === 'top')        { bar = { x: 0, y: 0, width: M.w, height: T }; tx = M.w / 2; ty = T / 2; }
      else if (f === 'bottom'){ bar = { x: 0, y: M.h - T, width: M.w, height: T }; tx = M.w / 2; ty = M.h - T / 2; }
      else if (f === 'left')  { bar = { x: 0, y: 0, width: T, height: M.h }; tx = T / 2; ty = M.h / 2; rot = -90; }
      else                    { bar = { x: M.w - T, y: 0, width: T, height: M.h }; tx = M.w - T / 2; ty = M.h / 2; rot = 90; }
      bar['class'] = 'sc-front-bar';
      bar.x = r2(bar.x); bar.y = r2(bar.y); bar.width = r2(bar.width); bar.height = r2(bar.height);
      lFront.appendChild(svgEl('rect', bar));
      var t = svgEl('text', { 'class': 'sc-front-label', x: r2(tx), y: r2(ty),
                              transform: rot ? 'rotate(' + rot + ' ' + r2(tx) + ' ' + r2(ty) + ')' : null });
      t.textContent = 'FRONT';
      lFront.appendChild(t);
      // The board wall is a landmark, not a control — it is announced, never focused.
      lFront.setAttribute('aria-label', 'Front of the room, ' + f + ' wall');
    }

    function renderTeacher() {
      while (lTeacher.firstChild) lTeacher.removeChild(lTeacher.firstChild);
      var td = layout.teacher_desk;
      if (!td) return;
      var cx = td.x * M.w, cy = td.y * M.h, w = td.w * M.w, h = td.h * M.h;
      var g = svgEl('g', { 'class': 'sc-teacher', transform: 'translate(' + r2(cx) + ',' + r2(cy) + ')' });
      g.appendChild(svgEl('rect', {
        'class': 'sc-teacher-shape', x: r2(-w / 2), y: r2(-h / 2),
        width: r2(w), height: r2(h), rx: 5,
        transform: 'rotate(' + r2(td.rotation || 0) + ')'
      }));
      var t = svgEl('text', { 'class': 'sc-teacher-label', x: 0, y: 0 });
      t.textContent = h >= 34 ? 'Teacher' : 'T';
      g.appendChild(t);
      var ttl = svgEl('title'); ttl.textContent = 'Teacher desk';
      g.appendChild(ttl);
      lTeacher.appendChild(g);
    }

    function renderDesks() {
      while (lDesks.firstChild) lDesks.removeChild(lDesks.firstChild);
      /* Rendered in READING ORDER, not array order. That is what makes Tab
         walk the room the way a person reads it — DOM order IS tab order, so
         the accessible order comes free rather than from a tabindex ladder
         that would have to be renumbered on every drag. */
      var ordered = orderedDesks(layout.desks);
      ordered.forEach(function (d, idx) {
        lDesks.appendChild(renderDesk(d, idx, ordered.length));
      });
    }

    function renderDesk(d, idx, total) {
      var box = deskBox(d, M);
      var g = svgEl('g', {
        'class': 'sc-desk',
        'data-desk-id': d.id,
        transform: 'translate(' + r2(box.cx) + ',' + r2(box.cy) + ')'
      });
      if (selected === d.id) g.setAttribute('data-selected', '1');

      /* Focusable ONLY where focus can do something. In plan the seats are the
         controls and the desks are furniture; in view nothing is a control. */
      if (mode === 'edit') {
        g.setAttribute('tabindex', '0');
        g.setAttribute('role', 'button');
        g.setAttribute('aria-label',
          'Desk ' + (idx + 1) + ' of ' + total + ', ' + (d.shape === 'round' ? 'round' : 'rectangular') +
          ', ' + d.seats + (d.seats === 1 ? ' seat' : ' seats') +
          (d.rotation ? ', rotated ' + Math.round(d.rotation) + ' degrees' : ''));
      }

      if (box.round) {
        g.appendChild(svgEl('circle', { 'class': 'sc-desk-shape', cx: 0, cy: 0, r: r2(box.w / 2) }));
      } else {
        g.appendChild(svgEl('rect', {
          'class': 'sc-desk-shape', x: r2(-box.w / 2), y: r2(-box.h / 2),
          width: r2(box.w), height: r2(box.h), rx: 5,
          transform: 'rotate(' + r2(box.rot) + ')'
        }));
      }

      var seats = seatPlacement(box, d.seats, layout.front, M);
      seats.forEach(function (s, i) {
        var seatId = d.id + ':' + i;
        var a = assignments[seatId];
        /* The seat group is TRANSLATED, never rotated: a rotated desk moves
           its chairs round with it, but the name written on a chair stays the
           right way up. A plan you have to tilt your head to read is a plan
           nobody reads. */
        var sg = svgEl('g', {
          'class': 'sc-seat',
          'data-seat-id': seatId,
          'data-filled': a ? '1' : '0',
          transform: 'translate(' + r2(s.x - box.cx) + ',' + r2(s.y - box.cy) + ')'
        });
        if (mode === 'plan') {
          sg.setAttribute('tabindex', '0');
          sg.setAttribute('role', 'button');
        }
        sg.setAttribute('aria-label', 'Seat ' + (i + 1) + ' on desk ' + (idx + 1) +
                        ', ' + (a ? String(a.label || a.id) : 'empty'));
        sg.appendChild(svgEl('circle', { 'class': 'sc-seat-dot', cx: 0, cy: 0, r: r2(s.r) }));
        if (a) {
          /* Shrink the type to fit the WHOLE name before truncating any of it.
             The label is allowed to run wider than its own chair — up to about
             the gap to the next chair along the rail — because the alternative
             is what this used to do: cap the text at the circle and print
             "ZZ Te…" on every seat. A teacher reads this sheet from the front
             of the room, and a small whole name beats half a large one. Only
             when even the floor size will not fit does it fall back to the
             ellipsis, and the full name is always on the <title>. */
          var full = String(a.label || a.id);
          var maxW = s.r * 2.6;
          var fs = clamp(Math.min(s.r * 0.62, maxW / (Math.max(1, full.length) * 0.56)), 7, 13);
          var maxChars = Math.max(1, Math.floor(maxW / (fs * 0.56)));
          var t = svgEl('text', { 'class': 'sc-seat-label', x: 0, y: 0, 'font-size': r2(fs) });
          t.textContent = fitLabel(full, maxChars);
          sg.appendChild(t);
        }
        var ttl = svgEl('title');
        ttl.textContent = a ? String(a.label || a.id) : ('Seat ' + (i + 1) + ' — empty');
        sg.appendChild(ttl);
        g.appendChild(sg);
      });
      return g;
    }

    /* Handles exist ONLY in edit mode, ONLY for the selected desk, and are
       genuinely absent otherwise — this function's first line is the house
       rule about absent-not-disabled, expressed as code. */
    function renderHandles() {
      while (lHandles.firstChild) lHandles.removeChild(lHandles.firstChild);
      if (mode !== 'edit' || !selected) return;
      var d = deskById(selected);
      if (!d) return;
      var box = deskBox(d, M);
      var hitR = (HANDLE_HIT_PX / 2) * unitsPerPx();

      var halfH = box.round ? box.w / 2 : box.h / 2;
      var halfW = box.round ? box.w / 2 : box.w / 2;
      var stem = 42;
      var rotLocal = { x: 0, y: -(halfH + stem) };
      var resLocal = { x: halfW, y: halfH };
      var rw = rotOff(rotLocal.x, rotLocal.y, box.rot);
      var ew = rotOff(resLocal.x, resLocal.y, box.rot);
      var edgeW = rotOff(0, -halfH, box.rot);

      var line = svgEl('line', {
        'class': 'sc-handle-stem',
        x1: r2(box.cx + edgeW.x), y1: r2(box.cy + edgeW.y),
        x2: r2(box.cx + rw.x), y2: r2(box.cy + rw.y)
      });
      lHandles.appendChild(line);

      [['rotate', rw, 'Rotate desk'], ['resize', ew, 'Resize desk']].forEach(function (h) {
        var g = svgEl('g', {
          'class': 'sc-handle', 'data-handle': h[0],
          transform: 'translate(' + r2(box.cx + h[1].x) + ',' + r2(box.cy + h[1].y) + ')'
        });
        // The invisible circle is the target; the visible dot is only the sign.
        g.appendChild(svgEl('circle', { 'class': 'sc-handle-hit', cx: 0, cy: 0, r: r2(hitR) }));
        g.appendChild(svgEl('circle', { 'class': 'sc-handle-dot', cx: 0, cy: 0, r: 7 }));
        var ttl = svgEl('title'); ttl.textContent = h[2];
        g.appendChild(ttl);
        lHandles.appendChild(g);
      });
    }

    function render() {
      if (destroyed) return;
      root.className = 'sc-root sc-mode-' + mode;
      renderFront();
      renderTeacher();
      renderDesks();
      renderHandles();
    }

    // -- clamping ---------------------------------------------------------

    /* Keep the desk inside the room. Done on the ROTATED bounding box rather
       than on w/h, so turning a long bench 90 degrees next to a wall pushes it
       back in instead of letting it hang out of the room. */
    function clampDesk(d) {
      var box = deskBox(d, M);
      var e = halfExtents(box);
      var cx = clamp(box.cx, e.hx, M.w - e.hx);
      var cy = clamp(box.cy, e.hy, M.h - e.hy);
      // A desk wider than the room cannot be clamped into it; centre it.
      if (e.hx * 2 > M.w) cx = M.w / 2;
      if (e.hy * 2 > M.h) cy = M.h / 2;
      d.x = cx / M.w;
      d.y = cy / M.h;
    }

    // -- interaction ------------------------------------------------------

    function setSelected(id) {
      if (selected === id) return;
      selected = id;
      renderDesks();
      renderHandles();
      if (cb.select) cb.select(selected);
    }

    function seatUnderClient(cx, cy) {
      var el = document.elementFromPoint(cx, cy);
      if (!el || !el.closest) return null;
      var s = el.closest('[data-seat-id]');
      if (!s || !root.contains(s)) return null;
      return s.getAttribute('data-seat-id');
    }

    function clearDropHint() {
      var marked = lDesks.querySelectorAll('[data-drop="1"]');
      for (var i = 0; i < marked.length; i++) marked[i].removeAttribute('data-drop');
    }

    function showGhost(label, pt) {
      while (lGhost.firstChild) lGhost.removeChild(lGhost.firstChild);
      var g = svgEl('g', { 'class': 'sc-ghost', transform: 'translate(' + r2(pt.x) + ',' + r2(pt.y) + ')' });
      g.appendChild(svgEl('circle', { 'class': 'sc-ghost-dot', cx: 0, cy: 0, r: 18 }));
      var t = svgEl('text', { 'class': 'sc-seat-label', x: 0, y: 0, 'font-size': 11 });
      t.textContent = fitLabel(label, 5);
      g.appendChild(t);
      lGhost.appendChild(g);
    }

    function moveGhost(pt) {
      if (lGhost.firstChild) lGhost.firstChild.setAttribute('transform', 'translate(' + r2(pt.x) + ',' + r2(pt.y) + ')');
    }

    function clearGhost() { while (lGhost.firstChild) lGhost.removeChild(lGhost.firstChild); }

    function onPointerDown(e) {
      /* view mode has no gestures at all — and nothing to hit, since neither a
         handle nor a tabindex exists to hit. The guard is belt and braces. */
      if (mode === 'view' || destroyed) return;
      if (e.pointerType === 'mouse' && e.button !== 0) return;
      var t = e.target;
      if (!t || !t.closest) return;

      if (mode === 'edit') {
        var handle = t.closest('[data-handle]');
        if (handle && selected) {
          var dsel = deskById(selected);
          if (!dsel) return;
          var kind = handle.getAttribute('data-handle');
          var pt = toSvgPoint(e.clientX, e.clientY);
          var box = deskBox(dsel, M);
          gesture = {
            kind: kind, deskId: selected, before: snapshot(),
            start: pt, box: box,
            grab: (kind === 'rotate')
              ? (dsel.rotation || 0) - Math.atan2(pt.y - box.cy, pt.x - box.cx) * 180 / PI
              : 0
          };
          capture(e);
          e.preventDefault();
          return;
        }

        var deskEl = t.closest('[data-desk-id]');
        if (deskEl) {
          var id = deskEl.getAttribute('data-desk-id');
          setSelected(id);
          var d = deskById(id);
          var p0 = toSvgPoint(e.clientX, e.clientY);
          gesture = {
            kind: 'move', deskId: id, before: snapshot(),
            start: p0, origin: { x: d.x * M.w, y: d.y * M.h }
          };
          capture(e);
          e.preventDefault();
          return;
        }

        setSelected(null);
        return;
      }

      if (mode === 'plan') {
        var seatEl = t.closest('[data-seat-id]');
        if (!seatEl) return;
        var seatId = seatEl.getAttribute('data-seat-id');
        gesture = {
          kind: 'assign', from: seatId, before: snapshot(),
          start: toSvgPoint(e.clientX, e.clientY), moved: false,
          payload: assignments[seatId] || null
        };
        capture(e);
        e.preventDefault();
      }
    }

    function capture(e) {
      try { svg.setPointerCapture(e.pointerId); } catch (err) { /* stylus quirks */ }
    }

    function onPointerMove(e) {
      if (!gesture || destroyed) return;
      var pt = toSvgPoint(e.clientX, e.clientY);

      if (gesture.kind === 'assign') {
        var far = Math.abs(pt.x - gesture.start.x) + Math.abs(pt.y - gesture.start.y);
        if (!gesture.moved && far > 6) {
          gesture.moved = true;
          if (gesture.payload) showGhost(gesture.payload.label || gesture.payload.id, pt);
        }
        if (gesture.moved) {
          moveGhost(pt);
          clearDropHint();
          var over = seatUnderClient(e.clientX, e.clientY);
          if (over && over !== gesture.from) {
            var el = lDesks.querySelector('[data-seat-id="' + over + '"]');
            if (el) el.setAttribute('data-drop', '1');
          }
        }
        return;
      }

      var d = deskById(gesture.deskId);
      if (!d) return;

      if (gesture.kind === 'move') {
        d.x = (gesture.origin.x + (pt.x - gesture.start.x)) / M.w;
        d.y = (gesture.origin.y + (pt.y - gesture.start.y)) / M.h;
        clampDesk(d);
        /* Fast path: a move changes the group's translate and nothing else, so
           the desk's own subtree is left alone. Rebuilding 60 desks' worth of
           nodes on every pointermove is what makes a canvas feel like treacle
           on an iPad. */
        var g = lDesks.querySelector('[data-desk-id="' + d.id + '"]');
        if (g) g.setAttribute('transform', 'translate(' + r2(d.x * M.w) + ',' + r2(d.y * M.h) + ')');
        renderHandles();
        return;
      }

      if (gesture.kind === 'rotate') {
        var a = Math.atan2(pt.y - gesture.box.cy, pt.x - gesture.box.cx) * 180 / PI + gesture.grab;
        // Free by default; Shift snaps. Free is the default because a real
        // room's desks are not at multiples of 15 degrees.
        if (e.shiftKey) a = Math.round(a / ROTATE_SNAP_DEG) * ROTATE_SNAP_DEG;
        d.rotation = wrapDeg(a);
        clampDesk(d);
        redrawDesk(d);
        renderHandles();
        return;
      }

      if (gesture.kind === 'resize') {
        // Into the desk's own frame, so a rotated desk resizes along its own
        // edges rather than along the room's.
        var lp = rotOff(pt.x - gesture.box.cx, pt.y - gesture.box.cy, -gesture.box.rot);
        if (d.shape === 'round') {
          var r = Math.max(Math.abs(lp.x), Math.abs(lp.y));
          var wN = clamp((r * 2) / M.w, EDIT_MIN_DIM, EDIT_MAX_DIM);
          d.w = wN; d.h = wN;                     // round stays round
        } else {
          d.w = clamp(Math.abs(lp.x) * 2 / M.w, EDIT_MIN_DIM, EDIT_MAX_DIM);
          d.h = clamp(Math.abs(lp.y) * 2 / M.h, EDIT_MIN_DIM, EDIT_MAX_DIM);
        }
        clampDesk(d);
        redrawDesk(d);
        renderHandles();
      }
    }

    function redrawDesk(d) {
      var old = lDesks.querySelector('[data-desk-id="' + d.id + '"]');
      if (!old) { renderDesks(); return; }
      var ordered = orderedDesks(layout.desks);
      var idx = 0;
      for (var i = 0; i < ordered.length; i++) { if (ordered[i].id === d.id) { idx = i; break; } }
      var fresh = renderDesk(d, idx, ordered.length);
      old.parentNode.replaceChild(fresh, old);
    }

    function onPointerUp(e) {
      if (!gesture || destroyed) return;
      var g = gesture;
      gesture = null;
      try { svg.releasePointerCapture(e.pointerId); } catch (err) {}

      if (g.kind === 'assign') {
        clearGhost();
        clearDropHint();
        var target = seatUnderClient(e.clientX, e.clientY);
        if (!g.moved) {
          // A tap, not a drag: hand it to the page, which owns the "pick a
          // student from the list" half of the interaction.
          if (cb.seat) cb.seat(g.from);
          return;
        }
        if (target && target !== g.from && g.payload) {
          doAssign(target, g.payload, g.from);
        }
        return;
      }

      // One gesture, one undo entry — banked here and nowhere in the move path.
      bank(g.before);
      render();
    }

    function onPointerCancel(e) {
      if (!gesture) return;
      var g = gesture;
      gesture = null;
      clearGhost(); clearDropHint();
      // A cancelled gesture is an abandoned one: put the layout back rather
      // than leaving a desk wherever the pointer died.
      if (g.kind !== 'assign') { layout = g.before; render(); }
    }

    // -- assignment -------------------------------------------------------

    /* assign() swaps.

       If the student being seated is already sitting somewhere on this plan,
       the two students trade places — that is what a teacher means when they
       drag Ana onto Ben's chair, and losing Ben would be a bug they would only
       notice at the door.

       If the student is NOT already on the plan (dragged in from the class
       list), the seat's current occupant is DISPLACED off the plan rather than
       overwritten in silence: they come back in `getAssignments()`'s absence
       and in whatever unseated list the page renders, which is where a teacher
       will look for them. */
    function doAssign(seatId, payload, fromSeat) {
      var before = snapshot();
      var beforeAssign = clone(assignments);
      var existing = assignments[seatId] || null;

      var source = fromSeat || null;
      if (!source && payload && payload.id != null) {
        for (var k in assignments) {
          if (assignments[k] && assignments[k].id === payload.id) { source = k; break; }
        }
      }

      assignments[seatId] = { id: payload.id, label: payload.label };
      if (source && source !== seatId) {
        if (existing) assignments[source] = existing;
        else delete assignments[source];
      }

      renderDesks();
      renderHandles();
      if (cb.assign) cb.assign(seatId, { id: payload.id, label: payload.label });
      // Assignment does not change the LAYOUT, so it banks nothing on the
      // layout undo stack — undo is about the room, and a teacher who undoes
      // after moving a desk must not have the whole class shuffle.
      void before; void beforeAssign;
    }

    /* Native HTML5 drop, so a `<li draggable>` in the class list beside the
       canvas can be dropped straight onto a chair. The internal pointer drag
       above covers seat-to-seat; this covers list-to-seat, which is the other
       half and cannot be a pointer gesture we own because the drag starts in
       somebody else's DOM. */
    function onDragOver(e) {
      if (mode !== 'plan') return;
      var s = e.target && e.target.closest ? e.target.closest('[data-seat-id]') : null;
      if (!s) { clearDropHint(); return; }
      e.preventDefault();
      clearDropHint();
      s.setAttribute('data-drop', '1');
    }

    function onDrop(e) {
      if (mode !== 'plan') return;
      var s = e.target && e.target.closest ? e.target.closest('[data-seat-id]') : null;
      clearDropHint();
      if (!s) return;
      e.preventDefault();
      var raw = '';
      try { raw = e.dataTransfer.getData('application/json') || e.dataTransfer.getData('text/plain') || ''; }
      catch (err) { raw = ''; }
      if (!raw) return;
      var payload = null;
      try { payload = JSON.parse(raw); } catch (err) { payload = { id: raw, label: raw }; }
      if (!payload || payload.id == null) return;
      doAssign(s.getAttribute('data-seat-id'), payload, null);
    }

    // -- keyboard ---------------------------------------------------------

    function onKeyDown(e) {
      if (mode === 'view' || destroyed) return;
      var t = e.target;
      if (!t || !t.closest) return;

      if (mode === 'plan') {
        var seat = t.closest('[data-seat-id]');
        if (seat && (e.key === 'Enter' || e.key === ' ')) {
          e.preventDefault();
          if (cb.seat) cb.seat(seat.getAttribute('data-seat-id'));
        }
        return;
      }

      var deskEl = t.closest('[data-desk-id]');
      if (deskEl) {
        var id = deskEl.getAttribute('data-desk-id');
        if (selected !== id && (e.key === 'Enter' || e.key === ' ')) {
          e.preventDefault(); setSelected(id); return;
        }
        if (selected !== id) setSelected(id);
      }
      if (!selected) return;
      var d = deskById(selected);
      if (!d) return;

      var dx = 0, dy = 0;
      if (e.key === 'ArrowLeft') dx = -1;
      else if (e.key === 'ArrowRight') dx = 1;
      else if (e.key === 'ArrowUp') dy = -1;
      else if (e.key === 'ArrowDown') dy = 1;

      if (dx || dy) {
        e.preventDefault();
        var step = NUDGE * (e.shiftKey ? NUDGE_BIG : 1);
        var before = snapshot();
        d.x += dx * step;
        d.y += dy * step;
        clampDesk(d);
        /* A held arrow key fires every ~30ms. Banking each one would blow the
           50-entry stack in a second and a half and leave the teacher unable
           to undo back past a single nudge, so a run of nudges inside 700ms
           coalesces into the one entry the run started with. */
        var now = Date.now();
        if (now - nudgeMark > 700) { pushUndo(before); }
        nudgeMark = now;
        redrawDesk(d);
        renderHandles();
        emitChange();
        return;
      }

      if (e.key === 'Delete' || e.key === 'Backspace') {
        e.preventDefault();
        api.deleteSelected();
      }
    }

    // -- resize watching --------------------------------------------------

    /* The handle hit area is sized in CSS px, so it has to be recomputed
       whenever the SVG's on-screen scale changes — a window resize, a sidebar
       opening, an iPad rotating. */
    var ro = null;
    function watchResize() {
      if (typeof ResizeObserver === 'function') {
        ro = new ResizeObserver(function () { renderHandles(); });
        ro.observe(root);
      } else {
        window.addEventListener('resize', renderHandles);
      }
    }

    // -- wiring -----------------------------------------------------------

    svg.addEventListener('pointerdown', onPointerDown);
    svg.addEventListener('pointermove', onPointerMove);
    svg.addEventListener('pointerup', onPointerUp);
    svg.addEventListener('pointercancel', onPointerCancel);
    root.addEventListener('keydown', onKeyDown);
    root.addEventListener('dragover', onDragOver);
    root.addEventListener('drop', onDrop);
    watchResize();

    /* Find somewhere to put a new desk. Front-to-back, left-to-right — the
       order a teacher fills a room — taking the first slot where the new desk
       clears every existing one with a real gap round it (a desk dropped
       touching another is a desk the teacher immediately has to drag).
       Falls back to the middle of the room if the room is genuinely full,
       because refusing to add the desk would be worse than overlapping one:
       overlap is legal here and the teacher can see it and move it. */
    function freeSpot(wN, hN) {
      var pad = 14;                                   // SVG units of clearance
      var others = layout.desks.map(function (d) { return polyOf(deskBox(d, M)); });
      var hw = (wN * M.w) / 2 + pad, hh = (hN * M.h) / 2 + pad;
      for (var y = 0.20; y <= 0.92; y += 0.04) {
        for (var x = 0.08; x <= 0.94; x += 0.04) {
          var cx = x * M.w, cy = y * M.h;
          if (cx - hw < 0 || cx + hw > M.w || cy - hh < 0 || cy + hh > M.h) continue;
          var cand = [
            { x: cx - hw, y: cy - hh }, { x: cx + hw, y: cy - hh },
            { x: cx + hw, y: cy + hh }, { x: cx - hw, y: cy + hh }
          ];
          var clash = false;
          for (var i = 0; i < others.length; i++) {
            if (clipPoly(cand, others[i]).length >= 3) { clash = true; break; }
          }
          if (!clash) return { x: x, y: y };
        }
      }
      return { x: 0.5, y: 0.5 };
    }

    var api = {

      // -- layout ---------------------------------------------------------

      setLayout: function (l) {
        var res = validate(l);
        if (!res.ok) throw new Error('setLayout: invalid layout — ' + res.errors.join('; '));
        var before = snapshot();
        layout = res.layout;
        if (selected && !deskById(selected)) { selected = null; if (cb.select) cb.select(null); }
        render();
        bank(before);
        return api;
      },

      getLayout: function () { return clone(layout); },

      setMode: function (m) {
        if (m !== 'edit' && m !== 'plan' && m !== 'view') {
          throw new Error("setMode: mode must be 'edit', 'plan' or 'view'");
        }
        if (m === mode) return api;
        mode = m;
        // Selection is an EDIT concept. Leaving a desk selected on the way into
        // plan or view would leave a highlighted desk with nothing to do.
        if (mode !== 'edit' && selected) { selected = null; if (cb.select) cb.select(null); }
        gesture = null;
        clearGhost(); clearDropHint();
        render();
        return api;
      },

      getMode: function () { return mode; },

      // -- desks ----------------------------------------------------------

      addDesk: function (spec) {
        spec = spec || {};
        var shape = spec.shape === 'round' ? 'round' : 'rect';
        var seats = clamp(Math.round(num(spec.seats) === null ? 2 : num(spec.seats)), SEAT_MIN, SEAT_MAX);
        if (layout.desks.length >= MAX_DESKS) {
          throw new Error('addDesk: this room already holds the maximum of ' + MAX_DESKS + ' desks');
        }
        var wN, hN;
        if (shape === 'round') { wN = 0.13; hN = 0.13; }
        else if (seats >= 4)   { wN = 0.19; hN = 0.115; }
        else                   { wN = 0.14; hN = 0.070; }

        var before = snapshot();
        var spot = freeSpot(wN, hN);
        var d = {
          id: nextDeskId(), shape: shape,
          x: spot.x, y: spot.y, w: wN, h: hN, rotation: 0, seats: seats
        };
        layout.desks.push(d);
        clampDesk(d);
        selected = d.id;
        render();
        if (cb.select) cb.select(selected);
        bank(before);
        return d.id;
      },

      deleteSelected: function () {
        if (!selected) return api;
        var before = snapshot();
        layout.desks = layout.desks.filter(function (d) { return d.id !== selected; });
        selected = null;
        render();
        if (cb.select) cb.select(null);
        bank(before);
        /* The deleted desk's students stay in the assignment map, orphaned.
           They are NOT discarded here: a delete is undoable, and a teacher who
           undoes must get the class back, not an empty room. See
           orphanedAssignments(). */
        return api;
      },

      selectDesk: function (id) {
        if (id === null || id === undefined) { setSelected(null); return api; }
        if (!deskById(id)) throw new Error('selectDesk: no desk with id ' + id);
        if (mode !== 'edit') return api;      // nothing to select onto
        setSelected(id);
        return api;
      },

      getSelected: function () { return selected; },

      setSeatsForSelected: function (n) {
        if (!selected) return api;
        var v = num(n);
        if (v === null) throw new Error('setSeatsForSelected: seats must be a number');
        v = clamp(Math.round(v), SEAT_MIN, SEAT_MAX);
        var d = deskById(selected);
        if (!d || d.seats === v) return api;
        var before = snapshot();
        d.seats = v;
        render();
        bank(before);
        return api;
      },

      setShapeForSelected: function (shape) {
        if (!selected) return api;
        if (!isOneOf(SHAPES, shape)) throw new Error('setShapeForSelected: unknown shape ' + shape);
        var d = deskById(selected);
        if (!d || d.shape === shape) return api;
        var before = snapshot();
        d.shape = shape;
        // The contract says a round desk's h equals its w. Enforced here as
        // well as in validate, so an in-memory layout is never briefly illegal.
        if (shape === 'round') { d.h = d.w; }
        clampDesk(d);
        render();
        bank(before);
        return api;
      },

      /* Moving the board moves every student: seats are placed relative to the
         front wall, so the whole room re-seats itself. The desks do not move —
         the furniture is where it is; it is the board that has changed wall. */
      setFront: function (edge) {
        if (!isOneOf(FRONTS, edge)) throw new Error('setFront: unknown edge ' + edge);
        if (layout.front === edge) return api;
        var before = snapshot();
        layout.front = edge;
        if (layout.teacher_desk) layout.teacher_desk = defaultTeacherDesk(edge);
        render();
        bank(before);
        return api;
      },

      toggleTeacherDesk: function () {
        var before = snapshot();
        layout.teacher_desk = layout.teacher_desk ? null : defaultTeacherDesk(layout.front);
        render();
        bank(before);
        return api;
      },

      // -- undo -----------------------------------------------------------

      undo: function () {
        if (!undoStack.length) return api;
        redoStack.push(snapshot());
        layout = undoStack.pop();
        if (selected && !deskById(selected)) { selected = null; if (cb.select) cb.select(null); }
        nudgeMark = 0;                     // a run of nudges ends at an undo
        render();
        emitChange();
        return api;
      },

      redo: function () {
        if (!redoStack.length) return api;
        undoStack.push(snapshot());
        layout = redoStack.pop();
        if (selected && !deskById(selected)) { selected = null; if (cb.select) cb.select(null); }
        nudgeMark = 0;
        render();
        emitChange();
        return api;
      },

      canUndo: function () { return undoStack.length > 0; },
      canRedo: function () { return redoStack.length > 0; },

      // -- assignments ----------------------------------------------------

      setAssignments: function (map) {
        var next = {};
        if (map && typeof map === 'object') {
          for (var k in map) {
            var v = map[k];
            if (!v || typeof v !== 'object') continue;
            if (v.id == null) continue;
            next[k] = { id: v.id, label: v.label == null ? String(v.id) : String(v.label) };
          }
        }
        assignments = next;
        render();
        return api;
      },

      getAssignments: function () { return clone(assignments); },

      assign: function (seatId, payload) {
        if (typeof seatId !== 'string') throw new Error('assign: seatId must be a string');
        if (!payload || payload.id == null) throw new Error('assign: payload must be {id, label}');
        doAssign(seatId, { id: payload.id, label: payload.label == null ? String(payload.id) : String(payload.label) }, null);
        return api;
      },

      unassign: function (seatId) {
        if (!assignments[seatId]) return api;
        delete assignments[seatId];
        renderDesks();
        renderHandles();
        return api;
      },

      // -- seats ----------------------------------------------------------

      seatIds: function () { return seatIdsOf(layout); },

      seatCentre: function (seatId) {
        if (typeof seatId !== 'string') return null;
        var cut = seatId.lastIndexOf(':');
        if (cut < 1) return null;
        var d = deskById(seatId.slice(0, cut));
        if (!d) return null;
        var i = parseInt(seatId.slice(cut + 1), 10);
        if (!(i >= 0) || i >= d.seats) return null;
        var pts = seatPlacement(deskBox(d, M), d.seats, layout.front, M);
        var p = pts[i];
        if (!p) return null;
        // Back out to normalised room space — the caller's world, not the SVG's.
        return { x: p.x / M.w, y: p.y / M.h };
      },

      /* Assignments whose seat has gone: the desk was deleted, or its seat
         count was cut from 4 to 2 and seats 2 and 3 stopped existing. They are
         RETAINED in the map rather than pruned, because both of those actions
         are undoable and pruning would make the undo lossy. The page shows
         them back in the unseated list and the teacher re-seats them (or
         undoes); nothing here decides for them. */
      orphanedAssignments: function () {
        var live = {}, out = [];
        seatIdsOf(layout).forEach(function (id) { live[id] = 1; });
        for (var k in assignments) {
          if (!live[k]) out.push({ seatId: k, payload: clone(assignments[k]) });
        }
        return out;
      },

      // -- teardown -------------------------------------------------------

      destroy: function () {
        if (destroyed) return;
        destroyed = true;
        svg.removeEventListener('pointerdown', onPointerDown);
        svg.removeEventListener('pointermove', onPointerMove);
        svg.removeEventListener('pointerup', onPointerUp);
        svg.removeEventListener('pointercancel', onPointerCancel);
        root.removeEventListener('keydown', onKeyDown);
        root.removeEventListener('dragover', onDragOver);
        root.removeEventListener('drop', onDrop);
        if (ro) { try { ro.disconnect(); } catch (e) {} }
        else { window.removeEventListener('resize', renderHandles); }
        if (root.parentNode) root.parentNode.removeChild(root);
      },

      // Escape hatches for a host page that needs to decorate or print.
      element: root,
      svg: svg
    };

    if (opts.assignments) api.setAssignments(opts.assignments);
    render();
    return api;
  }

  /* ── Export ──────────────────────────────────────────────────────────────
     One global, matching every other shared module on this site: no modules,
     no bundler, no build step — a <script src> and a name on window. */
  window.SeatingCanvas = {
    create: create,
    templates: {
      rows: tplRows,
      pairedRows: tplPairedRows,
      uShape: tplUShape,
      clusters: tplClusters
    },
    emptyLayout: emptyLayout,
    validate: validate,
    seatIdsOf: seatIdsOf,
    overlapReport: overlapReport
  };
})();
