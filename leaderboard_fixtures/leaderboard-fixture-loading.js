
/* GENERATED FIXTURE DATA — not checked in, not published. */
(function () {
  var D = {};
  var VIEWER = "AmberYew12";
  var START = {"tier": "Foundation", "subject": "Overall", "week": "2026-08-24"};
  var sel = {tier: START.tier, subject: START.subject, week: START.week};
  var redraw = function () {};
  var mounted = null;

  function initialsOf(n) {
    if (!n) { return ''; }
    var m = n.match(/^([A-Z])[a-z]*([A-Z])/);
    return m ? m[1] + m[2] : n.slice(0, 2).toUpperCase();
  }
  function key() { return [sel.tier, sel.subject, sel.week].join('|'); }
  function cur() { return D[key()] || null; }

  var TO_KEY = {biology: 'B', chemistry: 'C', physics: 'P'};
  function safeAvatar(u) {
    if (typeof u !== 'string' || !u) { return null; }
    if (!/^(https?:\/\/|\/)/i.test(u)) { return null; }
    if (/["'\\\s()<>;]/.test(u)) { return null; }
    return u;
  }
  function mapRow(r) {
    if (!r) { return null; }
    var p = r.per || {};
    var per = {B: p.biology == null ? null : p.biology,
               C: p.chemistry == null ? null : p.chemistry,
               P: p.physics == null ? null : p.physics};
    var done = [];
    (r.done || []).forEach(function (s) {
      var k = TO_KEY[s];
      if (k && per[k] != null && done.indexOf(k) < 0) { done.push(k); }
    });
    return {name: r.name, rank: r.rank, pct: r.pct, marks: r.marks,
            total: r.total, secs: r.secs, per: per, done: done,
            avatar_url: safeAvatar(r.avatar_url),
            move: (r.move === undefined ? null : r.move),
            was: (r.was === undefined ? null : r.was),
            streak: r.streak || 0};
  }

  var api = {
    status: function () { return "loading"; },
    payload: cur,
    stateFor: function (cmp) {
      var st = (cmp && cmp.state) || {};
      return {wk: api.weekIndex(), tier: sel.tier, subject: sel.subject,
              open: st.open == null ? null : st.open,
              flip: !!st.flip, now: st.now || Date.now()};
    },
    weeks: function () { var d = cur(); return (d && d.weeks) || []; },
    weekIndex: function () {
      var w = api.weeks();
      for (var i = 0; i < w.length; i++) {
        if (w[i].week_start === sel.week) { return i; }
      }
      return api.liveIndex();
    },
    liveIndex: function () {
      var w = api.weeks();
      for (var i = 0; i < w.length; i++) { if (w[i].is_current) { return i; } }
      return Math.max(0, w.length - 1);
    },
    topFor: function (i) {
      var w = api.weeks()[i];
      return (w && w.top_pct != null) ? {pct: w.top_pct} : null;
    },
    rows: function () {
      var d = cur();
      return (d && d.board) ? d.board.map(mapRow) : [];
    },
    me: function () { var d = cur(); return (d && d.me) ? mapRow(d.me) : null; },
    isCurrent: function () { var d = cur(); return !!(d && d.is_current); },
    now: function () { return Date.parse('2026-08-25T09:00:00Z'); },
    closesAt: function () {
      var d = cur();
      return d && d.closes_at ? Date.parse(d.closes_at) : null;
    },
    viewerName: function () { return VIEWER; },
    viewerInitials: function () { return initialsOf(VIEWER); },
    isYou: function (n) { return !!VIEWER && n === VIEWER; },
    select: function (p) {
      if (p.tier) { sel.tier = p.tier; }
      if (p.subject) { sel.subject = p.subject; }
      if ('week' in p) { sel.week = p.week; }
      /* ⚠️ THE SAME FALLBACK THE SEAM HAS. A tier or subject press keeps the
         DATE; if the new axis has no such week the index falls back to that
         axis's current week. Without this the fixture would resolve to a
         missing key and render an empty board — which would look exactly
         like the empty-week state and pass. */
      if (!D[key()]) {
        var w = api.weeks();
        for (var i = 0; i < w.length; i++) {
          if (w[i].is_current) { sel.week = w[i].week_start; break; }
        }
      }
      redraw();
    }
  };
  window.MrBadmusLeaderboardLive = api;

  var boot = window.__MRB_MOUNT__;
  window.__MRB_MOUNT__ = function () {
    mounted = boot();
    redraw = function () { if (mounted) { mounted.schedule(); } };
    return mounted;
  };
})();
