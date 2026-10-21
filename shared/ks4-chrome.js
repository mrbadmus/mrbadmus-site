/* ═══════════════════════════════════════════════════════════════════════
   ks4-chrome.js — the two live surfaces on the KS4 chrome (MRB-301)

   Claude Design drew leaderboard data into two of her seven screens: a
   "This week's challenge" strip on the landing, and a "Top stars" rail on
   the GCSE hub. Both were filled with invented students — CoralTrail56 at
   80%, SlateHarrier9 at 76%, "14th of 212" — and none of it may ship.

   This file is where those two surfaces get REAL rows, from the endpoint
   the GCSE landing has been using since MRB-137:

       GET /api/weekly-leaderboard/landing
         → { champion, foundation_top3, higher_top3, week_start }

   ── ONE CALL, DELIBERATELY ─────────────────────────────────────────────

   Both surfaces are fed by that single unauthenticated GET, and there is
   no second wave behind it. MRB-292's finding was that the student pages
   were slow because independent reads ran in series on first paint; the
   front door is the last place to reintroduce that. So:

     · no Supabase SDK, no session read, no profile read;
     · nothing here needs the visitor to be signed in;
     · a signed-out visitor and a signed-in one see the same rows, which
       is also why neither can be shown invented progress.

   Design's "Your best 68%", "Your rank 14th of 212" and the "14 You" row
   in her rail are therefore NOT rendered. They need an authenticated
   /api/weekly-leaderboard/board read with the viewer's tier, and the tier
   lives in the profile — two more round trips on the front door for a
   number that already has a home on /leaderboard.html.

   ── EVERY EMPTY STATE IS A STATE ───────────────────────────────────────

   No challenge yet this week, nobody in a tier, a cold Render dyno, a
   failed fetch: each of those renders as ABSENCE, never as a zero and
   never as a placeholder name. A cell with no data is removed from the
   DOM, which is why the strip is an auto-fit grid — it closes up.
   ═══════════════════════════════════════════════════════════════════════ */

(function () {
  'use strict';

  /* ⊕ Test isolation (5 Oct 2026) — from shared/config.js, read when the
     fetch is made, never a production literal. No config, no fetch: the
     strip and the stars render as the absence they already render on a
     failed fetch. */
  function backend() {
    var c = window.MrBadmusConfig;
    if (!c || !c.BACKEND_URL) { throw new Error('config.js is not on this page: no backend'); }
    return c.BACKEND_URL;
  }

  function esc(s) {
    var d = document.createElement('div');
    d.textContent = s == null ? '' : String(s);
    return d.innerHTML;
  }

  /* The leaderboard payload carries either a percentage or a score/max
     pair depending on the row; MRB-137's landing rail resolved that the
     same way and this keeps the two identical rather than inventing a
     second rule. Returns null — not 0 — when neither is present, so a
     missing value can be tested for instead of rendering as "0%". */
  function pct(e) {
    if (!e) return null;
    if (typeof e.percentage === 'number') return Math.round(e.percentage);
    if (e.max_score) return Math.round(100 * e.score / e.max_score);
    return null;
  }

  /* Display seam (MRB-138): every public name renders through here, so a
     handle appears the moment the backend puts `username` on the payload. */
  function displayName(u) {
    return (u && (u.username || u.name || u.first_name)) || 'Student';
  }

  // ── The landing's "This week's challenge" strip ───────────────────────
  //
  // Three cells and a call to action. Cell one is TRUE COPY, not data:
  // the week turns over on Friday at 10:15 UK time (server getWeekStart),
  // so "New questions every Friday" is a statement about the product, not
  // a metric. ⚠️ Design's drawn caption read "10 questions · closes
  // Sunday" — the close day is wrong and the count was invented, so
  // neither survives.
  //
  // Cells two and three are the two tier leaders, and each is deleted
  // outright if its tier has no entrant this week.
  function mountChallengeStrip(data) {
    var strip = document.getElementById('k4-challenge');
    if (!strip) return;
    var cell = document.getElementById('k4-lead');
    if (!cell) return;
    // No payload (cold backend, failed fetch): the cell is removed, and the
    // heading and the call to action still render.
    if (!data || !data.tier) { cell.parentNode.removeChild(cell); return; }

    var period = data.period === 'half' || data.period === 'all' ? data.period : 'week';
    var tab = period === 'half' ? 'This half term' : period === 'all' ? 'All time' : 'This week';
    var tier = data.tier === 'higher' ? 'Higher' : 'Foundation';
    cell.querySelector('[data-k4-kicker]').textContent = tab + ' \u00B7 ' + tier;

    var rows = (data.board || []).slice(0, 3);
    var list = cell.querySelector('[data-k4-rows]');
    var empty = cell.querySelector('[data-k4-empty]');
    var more = cell.querySelector('[data-k4-more]');
    var tgt = cell.querySelector('[data-k4-target]');

    if (!rows.length) {
      // The existing "Take the challenge" button is the Play button.
      list.hidden = true;
      more.hidden = true;
      empty.textContent = period === 'half' ? 'Be the first on the board this half term'
                        : period === 'all' ? 'Be the first on the board'
                        : 'Be the first on the board this week';
      empty.hidden = false;
    } else {
      var html = '';
      for (var i = 0; i < rows.length; i++) {
        var r = rows[i];
        var val = period === 'week' ? (typeof r.pct === 'number' ? Math.round(r.pct) : null) : r.marks;
        if (val === null || val === undefined) continue;
        html += '<li class="k4-lead-row">' +
                  '<span class="k4-lead-rank">' + String(i + 1).padStart(2, '0') + '</span>' +
                  '<span class="k4-lead-who">' + esc(displayName(r)) +
                    (r.staff === true ? '<span class="k4-lead-teacher">Teacher</span>' : '') +
                  '</span>' +
                  '<span class="k4-lead-val">' + (period === 'week' ? val + '%' : val + (val === 1 ? ' mark' : ' marks')) + '</span>' +
                '</li>';
      }
      list.innerHTML = html;
    }

    var t = data.target;
    var closed = period === 'week' && data.is_current === false;
    if (t && typeof t.score === 'number' && typeof t.max_score === 'number' && !closed) {
      tgt.textContent = (period === 'week' ? '' : 'This week, ') + (t.name || 'Mr Badmus') +
        ' scored ' + t.score + '/' + t.max_score + '. ' +
        (t.score >= t.max_score ? 'Can you match him?' : 'Can you beat him?');
      tgt.hidden = false;
    }
    cell.hidden = false;
  }

  // The tier the leaderboard itself opens on for this visitor: the signed-in
  // pupil's own profile tier, else Foundation (shared/leaderboard-live.js's
  // signed-out default). The session is read from the same localStorage slot
  // account.js reads, and the profile with one REST call; any failure is a
  // signed-out visitor, which is Foundation.
  function leaderboardTier() {
    return new Promise(function (resolve) {
      var done = false;
      function fin(t) { if (!done) { done = true; resolve(t); } }
      try {
        var c = window.MrBadmusConfig || {};
        var raw = c.AUTH_STORAGE_KEY && window.localStorage.getItem(c.AUTH_STORAGE_KEY);
        if (!raw || !c.SUPABASE_URL || !c.SUPABASE_ANON_KEY) return fin('foundation');
        if (raw.indexOf('base64-') === 0) raw = decodeURIComponent(escape(window.atob(raw.slice(7))));
        var s = JSON.parse(raw);
        if (!s || !s.access_token || !s.user || !s.user.id) return fin('foundation');
        setTimeout(function () { fin('foundation'); }, 2500);
        fetch(c.SUPABASE_URL + '/rest/v1/profiles?id=eq.' + encodeURIComponent(s.user.id) + '&select=tier', {
          headers: { apikey: c.SUPABASE_ANON_KEY, Authorization: 'Bearer ' + s.access_token, Accept: 'application/json' }
        }).then(function (r) { return r.ok ? r.json() : null; })
          .then(function (rows) { fin(rows && rows[0] && rows[0].tier === 'higher' ? 'higher' : 'foundation'); })
          .catch(function () { fin('foundation'); });
      } catch (e) { fin('foundation'); }
    });
  }

  function bootStrip() {
    leaderboardTier().then(function (tier) {
      return fetch(backend() + '/api/weekly-leaderboard/board?tier=' + tier + '&period=auto');
    }).then(function (r) { return r.ok ? r.json() : null; })
      .then(function (d) { mountChallengeStrip(d); })
      .catch(function () { mountChallengeStrip(null); });
  }

  // ── The GCSE hub's "Top stars" rail ──────────────────────────────────
  //
  // Design drew one tier. The live rail has crossfaded Foundation and
  // Higher since MRB-137, and dropping a tier to match a drawing would
  // remove half the students from the only place they appear on this
  // page — so the crossfade survives, in Design's clothes.
  function mountStars(data) {
    var rail = document.getElementById('k4-stars');
    if (!rail) return;

    var champ = data && data.champion;
    var champPct = pct(champ);
    if (champ && champPct !== null) {
      rail.querySelector('[data-k4-champ-name]').textContent = displayName(champ);
      rail.querySelector('[data-k4-champ-pct]').textContent = champPct + '%';
      document.getElementById('k4-champ').hidden = false;
    }

    var order = [];
    ['foundation', 'higher'].forEach(function (tier) {
      var rows = (data && data[tier + '_top3']) || [];
      var host = rail.querySelector('[data-k4-rows="' + tier + '"]');
      if (!host) return;
      var html = '';
      for (var i = 0; i < rows.length; i++) {
        var p = pct(rows[i]);
        if (p === null) continue;
        html += '<div class="k4-star-row">' +
                  '<span class="k4-star-who">' +
                    '<span class="k4-star-rank">' + String(i + 1).padStart(2, '0') + '</span>' +
                    esc(displayName(rows[i])) +
                  '</span>' +
                  '<span class="k4-star-pct">' + p + '%</span>' +
                '</div>';
      }
      if (html) { host.innerHTML = html; order.push(tier); }
    });

    if (!order.length) {
      // Nobody has sat it yet. Say so, rather than showing an empty box
      // that reads as a page that failed to load.
      var slides = document.getElementById('k4-stars-slides');
      if (slides) slides.innerHTML = '<p class="k4-stars-empty">No stars yet — be the first.</p>';
      return;
    }

    var dots = rail.querySelectorAll('.k4-stars-dot');
    function show(tier) {
      // Iterate BOTH tiers, not just the ones in `order`: a tier that is
      // empty this week is not in `order`, and iterating `order` alone
      // would leave its slide wearing the `k4-on` class from the initial
      // markup — two slides stacked in one grid cell. MRB-137 fixed this
      // exact bug on the old rail; the port keeps the fix.
      ['foundation', 'higher'].forEach(function (t) {
        var el = rail.querySelector('[data-k4-slide="' + t + '"]');
        if (!el) return;
        var on = t === tier;
        el.classList.toggle('k4-on', on);
        el.setAttribute('aria-hidden', on ? 'false' : 'true');
      });
      dots.forEach(function (d) {
        var on = d.getAttribute('data-tier') === tier;
        d.classList.toggle('k4-on', on);
        d.setAttribute('aria-selected', on ? 'true' : 'false');
      });
    }

    show(order[0]);

    if (order.length < 2) return;
    var foot = document.getElementById('k4-stars-dots');
    if (foot) foot.hidden = false;

    var idx = 0, paused = false;
    var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    dots.forEach(function (d) {
      d.addEventListener('click', function () { show(d.getAttribute('data-tier')); });
    });
    rail.addEventListener('mouseenter', function () { paused = true; });
    rail.addEventListener('mouseleave', function () { paused = false; });
    rail.addEventListener('focusin', function () { paused = true; });
    rail.addEventListener('focusout', function () { paused = false; });
    if (reduce) return;
    setInterval(function () {
      if (paused) return;
      idx = (idx + 1) % order.length;
      show(order[idx]);
    }, 6000);
  }

  function boot() {
    if (document.getElementById('k4-challenge')) bootStrip();
    if (!document.getElementById('k4-stars')) return;
    Promise.resolve().then(function () { return fetch(backend() + '/api/weekly-leaderboard/landing'); })
      .then(function (r) { return r.ok ? r.json() : null; })
      .then(function (data) {
        if (!data) throw new Error('no data');
        mountStars(data);
      })
      .catch(function () {
        // A failed or cold fetch leaves the rail in its server-rendered
        // state: it says nobody is on it yet, and shows no number.
        mountStars(null);
      });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    boot();
  }
})();
