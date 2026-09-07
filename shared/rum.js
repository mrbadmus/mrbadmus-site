/**
 * shared/rum.js — MRB-328 J4(a). One row per page load, and nothing else.
 *
 * WHY THIS EXISTS
 *
 * Every number we have about how fast this site feels is a LOCAL measurement:
 * `teacher_perf_budget.py` drives headless Chrome against a TEST fixture over a
 * warm cache, on a developer laptop, on home broadband. It is a good regression
 * gate and a bad model of a Year 8 on a school Chromebook over shared wifi. So
 * "it feels slow" has only ever been answerable with a guess. This makes it
 * answerable with a measurement.
 *
 * WHAT IT DELIBERATELY DOES NOT SEND
 *
 *   · No URL, ever. A URL on this estate carries ?class=<uuid> and
 *     ?student=<uuid>; shipping one would quietly rebuild a per-child browsing
 *     log out of fields that each look harmless. `page` is a coarse screen name
 *     off a fixed list and nothing finer.
 *   · No free text. Fetch labels are TABLE NAMES pulled out of the REST path
 *     with the query string thrown away first, and each is re-checked against a
 *     slug pattern before it is sent.
 *   · No student names, in any field.
 *
 * The table enforces all of that again in Postgres, because this file is
 * JavaScript and anyone can edit it in a console and post as themselves. The
 * checks here are for correctness; the checks there are the actual guarantee.
 *
 * ⚠️ If you are verifying this file live after a deploy, read the note at the
 * top of `_headers` FIRST. Polling its stamped URL before the deploy lands
 * pins the OLD bytes to the NEW url for a year, and this file was the one it
 * happened to.
 */
(function () {
  'use strict';

  var PAGES = {
    'teacher-classes': 1, 'teacher-class-detail': 1, 'teacher-student': 1,
    'teacher-today': 1, 'teacher-timetable': 1, 'teacher-admin': 1,
    'teacher-import': 1, 'teacher-assignment': 1, 'teacher-digest': 1,
    'teacher-insights': 1, 'teacher-seating': 1,
    'student-class': 1, 'student-assignment': 1
  };
  var SLUG = /^[a-z][a-z0-9_-]{0,39}$/;

  // A stuck reload loop must not be able to flood the table. Every load is
  // sampled otherwise: at 135 students this is a few hundred rows a day, and
  // sub-sampling that would only make the first week's numbers noisier for no
  // saving worth having.
  var SESSION_CAP = 20;
  var CAP_KEY = 'mrb-rum-count';

  function sessionCountOk() {
    try {
      var n = parseInt(sessionStorage.getItem(CAP_KEY) || '0', 10) || 0;
      if (n >= SESSION_CAP) { return false; }
      sessionStorage.setItem(CAP_KEY, String(n + 1));
      return true;
    } catch (e) {
      // Private mode, or site data blocked. Send anyway — the cap is a courtesy
      // to the table, not a correctness requirement.
      return true;
    }
  }

  function conf() {
    return (window.MrBadmusConfig || null);
  }

  // Same shape class-entry.js reads. Duplicated rather than imported because
  // this file must be able to run before, after, or without it.
  function session(ref) {
    try {
      var raw = localStorage.getItem('sb-' + ref + '-auth-token');
      if (!raw) { return null; }
      if (raw.indexOf('base64-') === 0) {
        raw = decodeURIComponent(escape(atob(raw.slice(7))));
      }
      var s = JSON.parse(raw);
      if (!s || !s.access_token || !s.user || !s.user.id) { return null; }
      var exp = s.expires_at ? s.expires_at * 1000 : 0;
      if (exp && exp <= Date.now()) { return null; }
      return s;
    } catch (e) { return null; }
  }

  // Turn resource timings into {n: <table>, ms: <total>} — names only.
  //
  // The query string is dropped BEFORE anything is read out of the URL, which
  // is the step that matters: `?student_id=eq.<uuid>` is exactly the thing that
  // must never leave the browser.
  function fetches() {
    var out = [];
    try {
      var entries = performance.getEntriesByType('resource') || [];
      var byTable = {};
      for (var i = 0; i < entries.length; i++) {
        var url = String(entries[i].name || '');
        var cut = url.indexOf('?');
        if (cut >= 0) { url = url.slice(0, cut); }   // query string gone first
        var at = url.indexOf('/rest/v1/');
        if (at < 0) { continue; }
        var table = url.slice(at + 9).split('/')[0].toLowerCase();
        if (!SLUG.test(table)) { continue; }
        byTable[table] = (byTable[table] || 0) + (entries[i].duration || 0);
      }
      for (var t in byTable) {
        if (Object.prototype.hasOwnProperty.call(byTable, t)) {
          out.push({ n: t, ms: Math.round(byTable[t]) });
        }
      }
      out.sort(function (a, b) { return b.ms - a.ms; });
      out = out.slice(0, 40);
    } catch (e) { return []; }
    return out;
  }

  function deviceClass() {
    try {
      var cores = navigator.hardwareConcurrency || 0;
      var mem = navigator.deviceMemory || 0;
      if (!cores && !mem) { return 'unknown'; }
      if (cores <= 2 || (mem && mem <= 2)) { return 'low'; }
      if (cores >= 8 && (!mem || mem >= 8)) { return 'high'; }
      return 'mid';
    } catch (e) { return 'unknown'; }
  }

  function connType() {
    try {
      var c = navigator.connection || navigator.mozConnection;
      var t = c && c.effectiveType;
      return (t === 'slow-2g' || t === '2g' || t === '3g' || t === '4g')
        ? t : 'unknown';
    } catch (e) { return 'unknown'; }
  }

  // One stamp standing for the whole build. Any shared asset's hash moves when
  // the build does, so the specific file does not matter — only that a week of
  // rows spanning three deploys does not average into a number describing no
  // version of the site.
  function build() {
    try {
      var m = window.__MRB_ASSET_V__ || {};
      var v = m['config.js'] || m['styles.css'];
      if (!v) {
        var keys = Object.keys(m).sort();
        v = keys.length ? m[keys[0]] : null;
      }
      /* ⚠️ FALLBACK: READ THE STAMP OFF THE DOCUMENT'S OWN TAGS.
         `__MRB_ASSET_V__` is published by the ported runtime, and the
         hand-written pages — today.html, timetable.html, admin.html, import
         .html — do not have it. The first live rows proved it: every ported
         screen carried a build and `teacher-today` carried NULL, which is the
         landing page, the one most worth attributing. A stamped `?v=` is on
         every page by definition, because the generator puts it there. */
      if (!v) {
        /* config.js SPECIFICALLY, not merely the first stamped tag in the
           document. Taking the first one made today.html report tokens.css's
           hash while every ported screen reported config.js's — so `build`
           was per-page and could not be grouped on. config.js is on every
           page that could ever beacon, and picking it by name makes the
           column ONE value across the estate for a given deploy. */
        var tags = document.querySelectorAll(
          'script[src*="/shared/"], link[href*="/shared/"]');
        var any = null;
        for (var i = 0; i < tags.length; i++) {
          var url = tags[i].getAttribute('src') || tags[i].getAttribute('href') || '';
          var hit = /[?&]v=([a-f0-9]{8})\b/.exec(url);
          if (!hit) { continue; }
          if (url.indexOf('/shared/config.js') >= 0) { any = hit[1]; break; }
          if (!any) { any = hit[1]; }   // keep the first as a last resort
        }
        v = any;
      }
      return (v && /^[a-f0-9]{8}$/.test(v)) ? v : null;
    } catch (e) { return null; }
  }

  function ttoi() {
    try {
      var nav = performance.getEntriesByType('navigation')[0];
      var start = nav ? 0 : (performance.timing && performance.timing.navigationStart);
      var now = nav ? performance.now()
                    : (Date.now() - start);
      var ms = Math.round(now);
      return (ms >= 0 && ms < 600000) ? ms : null;
    } catch (e) { return null; }
  }

  /**
   * Call once, at the moment the page becomes usable — where the skeleton is
   * replaced, so the number means what a person would say it means.
   *
   * `atMs` is that moment, captured by the CALLER. It matters: this file is
   * fetched asynchronously AFTER the mount so telemetry can never delay a
   * page, which means by the time report() runs, performance.now() has moved
   * on and would quietly report the beacon's own download as part of the
   * student's wait. The caller reads the clock at the right instant; the
   * fallback below is only for a caller that cannot.
   */
  function report(page, role, atMs) {
    try {
      if (!PAGES[page]) { return; }
      if (role !== 'teacher' && role !== 'student') { return; }
      var c = conf();
      if (!c || !c.SUPABASE_URL) { return; }
      var ref = c.SUPABASE_URL.split('//')[1].split('.')[0];
      var s = session(ref);
      if (!s) { return; }
      var ms = (typeof atMs === 'number' && atMs >= 0 && atMs < 600000)
        ? Math.round(atMs) : ttoi();
      if (ms === null) { return; }
      if (!sessionCountOk()) { return; }

      // No school_id: a BEFORE INSERT trigger derives it from the profile.
      // Sending it from here got it wrong twice over — it is usually absent
      // from the JWT, and a client should not be able to assert its own school.
      var row = {
        profile_id: s.user.id,
        page: page, role: role, ttoi_ms: ms,
        fetches: fetches(), conn: connType(), device: deviceClass(),
        build: build()
      };

      // keepalive, because a beacon fired as the page is being left dies
      // silently without it — the same trap the student answer-save hit.
      fetch(c.SUPABASE_URL + '/rest/v1/rum_timings', {
        method: 'POST', keepalive: true,
        headers: {
          'Content-Type': 'application/json',
          'apikey': c.SUPABASE_ANON_KEY,
          'Authorization': 'Bearer ' + s.access_token,
          'Prefer': 'return=minimal'
        },
        body: JSON.stringify(row)
      }).catch(function () { /* silent: never let telemetry break a page */ });
    } catch (e) { /* silent, always */ }
  }

  window.MrBadmusRUM = { report: report };
}());
