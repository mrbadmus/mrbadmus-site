/* ═══════════════════════════════════════════════════════════════════════
   consumer/consumer-common.js — the one gate, and the shared plumbing.

   MRB-308 Night 1. Every page under /consumer/ loads config.js and then
   this file, and does NOTHING else on its own. All five pages hand their
   work to `MrBadmusConsumer.boot()`, which is the single place the
   CONSUMER_SIGNUP_ENABLED check exists.

   ── WHY THE CHECK LIVES HERE AND NOWHERE ELSE ──────────────────────────
   Five copies of "if the flag is off, stop" is five chances to write the
   fourth one slightly differently — a `!==` that should have been `!`, an
   early return that leaves the nav rendered, a page that checks the flag
   after it has already fired its first fetch. A launch switch that is
   correct on four pages out of five is not a launch switch. So there is
   exactly one implementation, and a page that forgets to call `boot()`
   renders nothing at all rather than rendering unguarded — the body starts
   at `display:none` in consumer.css and only `boot()` reveals it.

   ── FAIL-CLOSED, AND WHAT "NOTHING" MEANS ──────────────────────────────
   The flag must be EXACTLY `true`. Absent, undefined, the string "false",
   a config.js that failed to load at all — every one of those is OFF.

   When it is off the page renders a plain "Not found" and stops. Not a
   redirect (a redirect tells you the address was real), not "coming soon"
   (that advertises an unlaunched product), not an error (there is no
   error). And genuinely stops: no Supabase SDK is fetched — it is injected
   by `boot()` only on the enabled path, which is why no page carries a
   CDN <script> tag of its own — no session is read, no /api/consumer/*
   call is made. The only bytes an off page pulls are its own stylesheet.

   ── WHAT THIS FILE DOES NOT DO ─────────────────────────────────────────
   It is not an auth guard. `boot({ requireSession: true })` will wait for a
   parent session and bounce to signup.html without one, but that is a
   ROUTING convenience, not a security boundary — every /api/consumer/*
   endpoint must authorise the JWT itself, exactly as the teacher endpoints
   do. Nothing a browser can be talked out of is a permission.
   ═══════════════════════════════════════════════════════════════════════ */

(function () {
  'use strict';

  var CFG = window.MrBadmusConfig || {};

  // Exactly `true`. See the fail-closed note above.
  var ENABLED = CFG.CONSUMER_SIGNUP_ENABLED === true;

  var SDK_URL = 'https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2/dist/umd/supabase.min.js';

  /* ── The consumer brand ─────────────────────────────────────────────────
     Claude Design's double chevron, copied verbatim from the BrandMark that
     student/class.html carries, plus the wordmark — and the wordmark reads
     "MrBadmus", with NO "AI".

     ⚠️ THAT IS A RULING, NOT A TYPO, AND IT IS THE ONLY PLACE ON THE ESTATE
     WHERE THE WORDMARK IS SHORT. On school surfaces the product is sold to
     teachers who are buying an AI tutor, so the identity says so. On
     consumer surfaces the buyer is a parent, and to a parent "AI" is a
     feature of the thing ("an AI tutor that knows the mark scheme"), never
     the thing itself. Do not "fix" this to MrBadmusAI for consistency with
     the other four brand presentations — the inconsistency is the decision.

     Not the gold-to-rust chevron (that is the KS4 lesson + root mark) and
     not the plain white staff wordmark (that is /teacher, /admin, /hod). */
  var BRANDMARK =
    '<svg width="20" height="20" viewBox="0 0 22 22" aria-hidden="true">' +
    '<path d="M3.5 3.5 L11 11 L3.5 18.5" stroke="#E4572E" stroke-width="3.4" ' +
    'fill="none" stroke-linecap="round" stroke-linejoin="round"></path>' +
    '<path d="M12 3.5 L19.5 11 L12 18.5" stroke="#E4572E" stroke-opacity="0.34" ' +
    'stroke-width="3.4" fill="none" stroke-linecap="round" stroke-linejoin="round"></path>' +
    '</svg>';

  function escapeHtml(s) {
    return String(s == null ? '' : s).replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }

  /* Carry the environment AND the backend override across every internal
     hop. Same reason admin.html's `envQ()` exists: a tester on TEST who
     clicks "Add a child" must not be silently dropped onto production, and
     a developer pointed at port 3100 must not have the next page talk to
     3000. Both parameters are read by config.js on the page we land on, so
     losing them mid-flow changes universes halfway through a signup. */
  function carryQuery() {
    var here = new URLSearchParams(window.location.search);
    var out = new URLSearchParams();
    if (here.get('env')) { out.set('env', here.get('env')); }
    if (here.get('api')) { out.set('api', here.get('api')); }
    return out;
  }
  function href(path, extra) {
    var q = carryQuery();
    if (extra) {
      Object.keys(extra).forEach(function (k) {
        if (extra[k] != null && extra[k] !== '') { q.set(k, extra[k]); }
      });
    }
    var s = q.toString();
    return path + (s ? ('?' + s) : '');
  }
  function go(path, extra) { window.location.href = href(path, extra); }

  /* ── The nav ────────────────────────────────────────────────────────────
     Deliberately thin. Night 3 replaces every one of these screens with
     Design's, so this is a brand-correct placeholder and not a design. */
  function navHtml(rightHtml) {
    return '<nav class="c-nav">' +
      '<a class="c-brand" href="' + escapeHtml(href('/consumer/overview.html')) + '">' +
      BRANDMARK + '<span>MrBadmus</span></a>' +
      '<div class="c-nav-right">' + (rightHtml || '') + '</div>' +
      '</nav>';
  }

  /* The off state, and the only thing an off page ever renders. Replaces
     the document rather than hiding parts of it, so there is no nav, no
     heading and no half-page left behind in the DOM for anyone to read. */
  function notFound() {
    document.title = 'Not found';
    document.body.innerHTML =
      '<div class="c-notice"><h1>Not found</h1>' +
      '<p>This page isn’t available.</p></div>';
    document.body.style.display = 'block';
  }

  /* Every failure a human can read. Never a status code, never a stack,
     never a blank panel — admin.html's `notice()` sets the voice and this
     keeps it. `hint` is for the one thing the reader could usefully do. */
  function fail(el, message, hint) {
    if (!el) { return; }
    el.innerHTML = '<div class="c-fail"><p>' + escapeHtml(message) + '</p>' +
      (hint ? '<p class="c-fail-hint">' + escapeHtml(hint) + '</p>' : '') + '</div>';
  }

  function setMsg(el, message, kind) {
    if (!el) { return; }
    if (!message) { el.style.display = 'none'; el.textContent = ''; return; }
    el.className = 'c-msg' + (kind ? (' c-msg-' + kind) : '');
    el.textContent = message;
    el.style.display = 'block';
  }

  function setBusy(btn, busy, busyLabel) {
    if (!btn) { return; }
    if (busy) {
      btn.dataset.label = btn.dataset.label || btn.textContent;
      btn.textContent = busyLabel || 'Working…';
      btn.disabled = true;
    } else {
      if (btn.dataset.label) { btn.textContent = btn.dataset.label; }
      btn.disabled = false;
    }
  }

  /* ── The backend seam ───────────────────────────────────────────────────
     Always `window.MrBadmusConfig.BACKEND_URL`, never a literal. The whole
     point of the ?api= override in config.js is that this file has no
     opinion about which backend is answering.

     Everything that can go wrong comes back as an Error carrying a sentence
     a parent could read. A raw `fetch` rejection says "Failed to fetch",
     which on a consumer surface is indistinguishable from "your card was
     declined" — so the network case is translated here, once. */
  function api(path, opts) {
    opts = opts || {};
    var base = (window.MrBadmusConfig && window.MrBadmusConfig.BACKEND_URL) || '';
    var init = { method: opts.method || 'GET', headers: {} };
    if (opts.token) { init.headers['Authorization'] = 'Bearer ' + opts.token; }
    if (opts.body != null) {
      init.headers['Content-Type'] = 'application/json';
      init.body = JSON.stringify(opts.body);
    }
    return fetch(base + path, init).then(function (res) {
      return res.text().then(function (text) {
        var data = null;
        try { data = text ? JSON.parse(text) : null; } catch (e) { data = null; }
        if (res.ok) { return data; }

        /* A 404 on /api/consumer/* is the SECOND switch being off, and it is
           worth naming: with the frontend flag on and the backend one off,
           every button on every page fails identically and looks like a
           bug. Saying so here has saved the next person an evening. */
        if (res.status === 404 && path.indexOf('/api/consumer/') === 0) {
          throw new Error(
            'The consumer service isn’t switched on for this environment yet.'
          );
        }
        if (res.status === 401 || res.status === 403) {
          throw new Error('You’re not signed in, or your session has expired.');
        }
        var msg = (data && (data.error || data.message)) || '';
        throw new Error(msg || 'Something went wrong. Please try again in a moment.');
      });
    }, function () {
      throw new Error(
        'We couldn’t reach MrBadmus. Check your connection and try again.'
      );
    });
  }

  /* Load the Supabase SDK on demand. A <script> tag in each page's head
     would be a network call made BEFORE the flag is read, which is exactly
     what "no network calls when off" forbids. */
  var sdkPromise = null;
  function loadSdk() {
    if (sdkPromise) { return sdkPromise; }
    sdkPromise = new Promise(function (resolve, reject) {
      if (window.supabase && window.supabase.createClient) { return resolve(); }
      var el = document.createElement('script');
      el.src = SDK_URL;
      el.onload = function () { resolve(); };
      el.onerror = function () { reject(new Error('sdk')); };
      document.head.appendChild(el);
    });
    return sdkPromise;
  }

  var client = null;
  function getClient() { return client; }

  /* ── boot ───────────────────────────────────────────────────────────────
     opts.requireSession  — bounce to signup.html when there is no parent
                            session. Routing only; see the header note.
     opts.anonymous       — true for child-login.html, which must NOT read
                            or care about any existing parent session.
     opts.run(ctx)        — the page. ctx = { sb, session, token, api, ... }

     Errors thrown by `run` are caught and shown as a sentence. A consumer
     page that throws must still be a page. */
  function boot(opts) {
    opts = opts || {};

    function start() {
      if (!ENABLED) { return notFound(); }

      loadSdk().then(function () {
        client = window.supabase.createClient(CFG.SUPABASE_URL, CFG.SUPABASE_ANON_KEY);
        if (opts.anonymous) { return { session: null }; }
        return client.auth.getSession().then(function (r) {
          return { session: (r && r.data && r.data.session) || null };
        });
      }).then(function (state) {
        if (opts.requireSession && !state.session) {
          go('/consumer/signup.html');
          return;
        }
        document.body.style.display = 'block';
        var session = state.session;
        return opts.run({
          sb: client,
          session: session,
          token: session ? session.access_token : null,
          api: api,
          href: href,
          go: go
        });
      }).catch(function (e) {
        console.error('[consumer]', e);
        document.body.style.display = 'block';
        var host = document.getElementById('c-main') || document.body;
        fail(host,
          'We couldn’t load this page right now.',
          'Please refresh in a moment. If it keeps happening, email hello@mrbadmus.com.');
      });
    }

    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', start);
    } else {
      start();
    }
  }

  window.MrBadmusConsumer = {
    ENABLED: ENABLED,
    BRANDMARK: BRANDMARK,
    boot: boot,
    api: api,
    navHtml: navHtml,
    href: href,
    go: go,
    escapeHtml: escapeHtml,
    fail: fail,
    setMsg: setMsg,
    setBusy: setBusy,
    getClient: getClient,
    notFound: notFound
  };
})();
