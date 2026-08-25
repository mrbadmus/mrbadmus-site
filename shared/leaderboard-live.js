/* shared/leaderboard-live.js — the KS4 Weekly Leaderboard's data seam.
   ══════════════════════════════════════════════════════════════════════════

   MRB-290. Design's delivery (docs/ks3/design-reference/leaderboard/) is a
   SAMPLE: sixty-one invented handles derived from a seeded PRNG, nine
   invented weeks, every mark hashed out of a name. None of that ships. This
   file is the ONLY way a number reaches the ported page.

   ⚑ WHAT THIS FILE OWNS, AND WHAT DESIGN STILL OWNS.

   Design's `renderVals` is ~170 lines of view-model computation over a
   ten-field record — {name, rank, pct, marks, total, secs, per, done, move,
   streak} — and every pixel of the podium, the rail, the rows and the
   expanded breakdown is derived from it. That computation is NOT
   reimplemented here. This file returns real rows in Design's own shapes and
   lets Design's arithmetic run unmodified on top. "One number, one source"
   survives; the source is now the backend.

   The endpoint is `GET /api/weekly-leaderboard/board`. It is deliberately
   NARROW: it returns the top ten plus the viewer's own row and nothing else,
   and it precomputes the header statistics over the FULL board server-side.
   The client therefore cannot see, count or rank the whole cohort — which is
   the point, and which is why `build_leaderboard_port.py` rules out every
   `board.length` in Design's aggregate block. See RULINGS R20/R21 there.

   ⚠️ THE WEEKS ARRAY CHANGES WITH THE SUBJECT, and this is measured, not
   assumed. On 25 Aug 2026 the live backend returned ten weeks for
   Higher/Overall, six for Foundation/Overall, four for Foundation/Biology and
   three for Foundation/Physics — and the Higher list has a two-month hole in
   it between 8 May and 3 July. Design addresses a week by INDEX into a fixed
   nine, so an index is not stable across a subject press: index 3 means
   17 July before the press and 24 July after it. Selection is therefore held
   HERE, as a DATE (`sel.week`, the Friday `week_start`), and the index Design
   wants is derived from it per payload. A week that does not exist in the new
   list falls back to that list's current week rather than to index 3.

   ⚠️ WEEKS RUN FRIDAY → THURSDAY. `week_start` is always a Friday (verified
   across every week the backend returns), the week ends `week_start + 6`, and
   the round closes at `closes_at` — 09:15 UTC on the following Friday, which
   is AFTER the next week has already begun. Design's `weekDates()` derives a
   Monday-based week from the device clock and is replaced wholesale.

   ⚠️ THE COUNTDOWN IS ANCHORED TO THE SERVER. `server_now` arrives with every
   payload; the offset from `Date.now()` is captured ONCE, at first load, and
   every tick is `Date.now() - skew`. A device clock that is a day fast must
   not be able to close the round early, and one that is a day slow must not
   be able to hold it open.

   Loading and error are STATES, not blanks — Design drew neither, because a
   sample never waits and never fails. See R28/R29.  */

(function () {
  "use strict";

  var RENDER_URL = "https://mrbadmus-backend.onrender.com";
  var SUPABASE_URL = "https://urklkrwevjtlfbwnipjn.supabase.co";
  /* Anon keys are designed to be public; this is the same key every other
     page on the site carries inline. See CLAUDE.md. */
  var SUPABASE_ANON_KEY =
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVya2xrcndldmp0bGZid25pcGpuIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzQxOTQyNzksImV4cCI6MjA4OTc3MDI3OX0.pW9AP6TPlKC_XHDTbrEKrEGmGXglN0z5b0KGXD2oHvg";

  /* Design's subject words ↔ the endpoint's. Design types 'Overall',
     'Biology', 'Chemistry', 'Physics' and keys its `PAPERS` table on 'B',
     'C', 'P'; the endpoint speaks lowercase full names. Three vocabularies,
     one table, so no call site has to know two of them. */
  var TO_QUERY = {Overall: "", Biology: "biology",
                  Chemistry: "chemistry", Physics: "physics"};
  var TO_KEY = {biology: "B", chemistry: "C", physics: "P"};

  var store = {
    /* Design's words, because Design's `renderVals` compares against them
       (`s.tier === t`, `SUBJ_KEY[s.subject]`). Translated at the fetch. */
    sel: {tier: "Foundation", subject: "Overall", week: null},
    cache: {},
    skew: 0,
    skewSet: false,
    viewer: {name: "", initials: ""},
    signedIn: false,
    redraw: function () {}
  };

  function key(sel) {
    return sel.tier + "|" + sel.subject + "|" + (sel.week || "");
  }

  /* ── identity ────────────────────────────────────────────────────────
     ⚑ FROZEN, AND IT IS THE LIVE PAGE'S RULE, NOT A NEW ONE.
     `username || first_name || 'Student'` is what the retired
     leaderboard.html computed in `displayName()`, and it is what the new
     endpoint already applies server-side before it sends `name`. So there is
     no client-side identity logic at all here beyond the viewer's own — one
     rule, applied once, on the server. */
  function initialsOf(n) {
    if (!n) { return ""; }
    var m = n.match(/^([A-Z])[a-z]*([A-Z])/);
    return m ? m[1] + m[2] : n.slice(0, 2).toUpperCase();
  }

  /* ⊕ MRB-290 R25. An avatar URL is interpolated into a CSS `background`
     shorthand on Design's disc, so it is sanitised at the seam rather than
     at the six places it is drawn. Anything that is not a plain http(s) URL
     with no quote, backslash, whitespace, parenthesis or semicolon in it is
     discarded and the row falls back to Design's initials monogram.

     ⚠️ REJECT, NOT ESCAPE. Escaping would need to be right for the CSS
     tokeniser, the `url()` grammar and the HTML attribute all at once, and a
     mistake in any of the three is a script-injection vector on a page 135+
     students load. A missing face is a cosmetic loss; this trade is not
     close. */
  function safeAvatar(u) {
    if (typeof u !== "string" || !u) { return null; }
    if (!/^(https?:\/\/|\/)/i.test(u)) { return null; }
    if (/["'\\\s()<>;]/.test(u)) { return null; }
    return u;
  }

  /* ── the row mapper ──────────────────────────────────────────────────
     Into Design's ten-field record, and nothing else is added. */
  function mapRow(r) {
    if (!r) { return null; }
    var p = r.per || {};
    var per = {B: p.biology == null ? null : p.biology,
               C: p.chemistry == null ? null : p.chemistry,
               P: p.physics == null ? null : p.physics};
    /* ⚠️ R30 — A PAPER IS "DONE" ONLY IF IT HAS A PERCENTAGE.
       Design's `breakdown` renders `x.per[k] + '%'` for every key in `done`
       and has no null branch, so a subject listed as done with a null score
       renders the string "null%" straight into the copy. The endpoint can
       return exactly that pairing, so the intersection is taken here rather
       than guarded in nine places downstream. */
    var done = [];
    (r.done || []).forEach(function (s) {
      var k = TO_KEY[s];
      if (k && per[k] != null && done.indexOf(k) < 0) { done.push(k); }
    });
    return {
      name: r.name, rank: r.rank, pct: r.pct, marks: r.marks,
      total: r.total, secs: r.secs, per: per, done: done,
      /* ⊕ MRB-290 R25 — identity is FROZEN, and the avatar is half of it.
         The live leaderboard renders a student's avatar image today, so the
         port renders it too: inside Design's own disc, as a background, with
         her initials monogram as the fallback when there is none. See the
         ruling in build_leaderboard_port.RULINGS — identity-frozen outranks
         pixel fidelity on this one point, and only this one.

         ⚠️ SANITISED HERE, NOT AT THE DISC. This value is interpolated into
         a CSS `background` shorthand, so a URL containing a quote or a
         `;` would close the declaration and let arbitrary CSS in. Anything
         that is not a plain http(s) URL is discarded and the row falls back
         to initials — a missing face is a cosmetic loss, a CSS injection on
         a page 135+ students load is not. */
      avatar_url: safeAvatar(r.avatar_url),
      /* `move` is null for a NEW entry and 0 for HELD, and those are
         different facts. `undefined` is neither, so it is normalised to
         null — Design's `x.move === null` test would otherwise read an
         absent key as HELD. */
      move: (r.move === undefined ? null : r.move),
      was: (r.was === undefined ? null : r.was),
      streak: r.streak || 0
    };
  }

  /* ── the fetch ───────────────────────────────────────────────────────── */
  function urlFor(sel) {
    var q = "?tier=" + encodeURIComponent(sel.tier.toLowerCase());
    var s = TO_QUERY[sel.subject];
    if (s) { q += "&subject=" + s; }
    if (sel.week) { q += "&week_start=" + encodeURIComponent(sel.week); }
    return RENDER_URL + "/api/weekly-leaderboard/board" + q;
  }

  var token = null;

  function load(sel) {
    var k = key(sel);
    /* ⚠️ AN ERROR IS NOT A CACHED ANSWER. `loading` and `ok` early-return —
       one request in flight per key, and a fetched view is never refetched.
       An `error` entry is neither: it is the absence of an answer, and the
       first version kept it for the life of the page. One network blip on a
       (tier, subject, week) key meant every later press landing on that key
       showed COULD NOT LOAD until a full reload, with no control on the page
       able to recover it.

       Refetching on error is also why the error state needs no retry button:
       every tier, subject and week press becomes an honest retry, so the
       controls the page already has ARE the retry. */
    var have = store.cache[k];
    if (have && (have.status === "loading" || have.status === "ok")) {
      return;
    }
    store.cache[k] = {status: "loading", payload: null};
    var opts = token ? {headers: {Authorization: "Bearer " + token}} : {};
    fetch(urlFor(sel), opts).then(function (r) {
      if (!r.ok) { throw new Error("HTTP " + r.status); }
      return r.json();
    }).then(function (d) {
      /* ⚠️ CAPTURED ONCE. Re-anchoring the skew on every payload would let a
         slow response walk the countdown backwards mid-tick. */
      if (!store.skewSet) {
        var srv = Date.parse(d.server_now);
        if (!isNaN(srv)) { store.skew = Date.now() - srv; store.skewSet = true; }
      }
      store.cache[k] = {status: "ok", payload: d};
      /* The backend is the authority on which week this is. Asking for
         nothing and being given `current_week` is the normal first load. */
      if (!sel.week && d.week_start) {
        sel.week = d.week_start;
        store.cache[key(sel)] = store.cache[k];
      }
      store.redraw();
    }).catch(function (e) {
      store.cache[k] = {status: "error", payload: null,
                        message: (e && e.message) || "network"};
      store.redraw();
    });
  }

  function entry() {
    return store.cache[key(store.sel)] || {status: "loading", payload: null};
  }

  /* ── the API the ported logic calls ──────────────────────────────────
     Every one of these is read from Design's own code through the seam
     functions `build_leaderboard_port.py` injects. Nothing else on the page
     may reach `store`. */
  var api = {
    status: function () { return entry().status; },
    payload: function () { return entry().payload; },

    /* Design's `s`, with the selection taken from here rather than from the
       component. See R19: an index into the weeks array is not stable across
       a subject change, so the DATE is the state and the index is derived. */
    stateFor: function (cmp) {
      var d = entry().payload;
      var st = (cmp && cmp.state) || {};
      return {
        wk: api.weekIndex(),
        tier: store.sel.tier,
        subject: store.sel.subject,
        open: st.open == null ? null : st.open,
        flip: !!st.flip,
        now: st.now || Date.now()
      };
    },

    weeks: function () {
      var d = entry().payload;
      return (d && d.weeks) || [];
    },

    weekIndex: function () {
      var w = api.weeks(), i;
      for (i = 0; i < w.length; i++) {
        if (w[i].week_start === store.sel.week) { return i; }
      }
      return api.liveIndex();
    },

    liveIndex: function () {
      var w = api.weeks(), i;
      for (i = 0; i < w.length; i++) { if (w[i].is_current) { return i; } }
      return Math.max(0, w.length - 1);
    },

    /* The strip's mini-bar. ⚠️ NOT a board read: only the SELECTED week's
       board is ever fetched, and Design's `this.raw(i)[0]` would need all
       ten. `top_pct` arrives on every week of every payload for exactly this
       purpose, and is null on a week nobody has sat. */
    topFor: function (i) {
      var w = api.weeks()[i];
      return (w && w.top_pct != null) ? {pct: w.top_pct} : null;
    },

    rows: function () {
      var d = entry().payload;
      if (!d || !d.board) { return []; }
      return d.board.map(mapRow);
    },

    me: function () {
      var d = entry().payload;
      return (d && d.me) ? mapRow(d.me) : null;
    },

    isCurrent: function () {
      var d = entry().payload;
      return !!(d && d.is_current);
    },

    /* Server-anchored. Never `Date.now()` on its own. */
    now: function () { return Date.now() - store.skew; },

    closesAt: function () {
      var d = entry().payload;
      var t = d && d.closes_at ? Date.parse(d.closes_at) : NaN;
      return isNaN(t) ? null : t;
    },

    viewerName: function () { return store.viewer.name || ""; },
    viewerInitials: function () { return store.viewer.initials || ""; },
    /* ⚠️ GUARDED ON TRUTHINESS. Signed out, the viewer name is the empty
       string, and `'' === x.name` would mark any unnamed row as YOU. */
    isYou: function (n) {
      return !!store.viewer.name && n === store.viewer.name;
    },

    /* The only way selection changes. Fetches if it must, redraws either
       way, so a press is never a dead control even while the new view is
       still in flight. */
    select: function (patch) {
      if (patch.tier) { store.sel.tier = patch.tier; }
      if (patch.subject) { store.sel.subject = patch.subject; }
      if ("week" in patch) { store.sel.week = patch.week; }
      /* ⚠️ A tier or subject press keeps the DATE and lets the index move.
         If the new axis has no such week, `weekIndex()` falls back to that
         axis's current week — which is why the week is not cleared here. */
      load(store.sel);
      store.redraw();
    },

    /* For the countdown interval to know whether to keep ticking. */
    store: store
  };

  window.MrBadmusLeaderboardLive = api;

  /* ── boot ────────────────────────────────────────────────────────────
     Tier comes from the signed-in student's own profile — the behaviour the
     retired leaderboard.html had, and it beats Design's hardcoded 'Higher'
     default. A signed-out visitor lands on Foundation, which is also what
     the retired page did. */
  function boot() {
    /* ⚑ THE WARM-UP PING, restored from the retired leaderboard.html — live
       behaviour parity, not new design. The backend is on Render's free
       tier and SLEEPS; a cold dyno takes tens of seconds to wake, and the
       board request would spend all of it waiting. Fired here, before the
       session lookup, the wake starts while the student is still reading the
       heading. Fire-and-forget with a swallowed rejection, exactly as the
       retired page had it: nothing on this page depends on the result, and
       an unhandled rejection would be console noise the behaviour gate would
       correctly report. */
    fetch(RENDER_URL + "/api/health").catch(function () {});

    var mounted = null;
    store.redraw = function () {
      if (mounted) { mounted.schedule(); }
    };

    function go() {
      load(store.sel);
      mounted = window.__MRB_MOUNT__();
    }

    if (!window.supabase || !window.supabase.createClient) { go(); return; }
    var sb;
    try {
      sb = window.supabase.createClient(SUPABASE_URL, SUPABASE_ANON_KEY);
    } catch (e) { go(); return; }

    sb.auth.getSession().then(function (res) {
      var sess = res && res.data && res.data.session;
      if (!sess) { return null; }
      token = sess.access_token;
      store.signedIn = true;
      return sb.from("profiles")
        .select("tier, username, first_name")
        .eq("id", sess.user.id).single();
    }).then(function (p) {
      if (p && p.data) {
        if (p.data.tier === "foundation") { store.sel.tier = "Foundation"; }
        if (p.data.tier === "higher") { store.sel.tier = "Higher"; }
        /* The same rule the endpoint applies to everybody else's row, so the
           viewer's own name in the standing card matches the name in the
           board. */
        var n = p.data.username || p.data.first_name || "Student";
        store.viewer = {name: n, initials: initialsOf(n)};
      }
    }).catch(function () {
      /* A signed-out visitor, or a profile that cannot be read, is a normal
         state and not an error: the board is public. */
    }).then(go, go);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
})();
