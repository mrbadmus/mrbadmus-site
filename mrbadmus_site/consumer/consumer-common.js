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
        /* ⊕ MRB-309/315, Night 2. The contract gives every consumer error
           BOTH a machine `error` code and a human `message`, and this used to
           read `error || message` — so a 429 cap arrived on screen as the
           word "cap_reached" and a 423 as "org_locked". A parent reading
           "cap_reached" has been told nothing. `message` wins; the code is
           still carried, on the Error, for the two pages that branch on it
           (exam.html on quota_reached, every page on org_locked). */
        var code = (data && data.error) || '';
        var msg  = (data && data.message) || '';

        /* A 404 on /api/consumer/* with nothing in it is the SECOND switch
           being off, and it is worth naming: with the frontend flag on and
           the backend one off, every button on every page fails identically
           and looks like a bug. Saying so here has saved the next person an
           evening. A 404 that DID carry words keeps its own words — that is
           a real missing thing, not a switch. */
        if (!msg && res.status === 404 && path.indexOf('/api/consumer/') === 0) {
          msg = 'This part of MrBadmus isn’t switched on for this environment yet.';
        }
        if (!msg && (res.status === 401 || res.status === 403)) {
          msg = 'You’re not signed in, or your session has expired.';
        }
        var err = new Error(msg || code ||
          'Something went wrong. Please try again in a moment.');
        err.status = res.status;
        err.code = code;
        err.data = data;
        throw err;
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

  /* ══ NIGHT 2 HELPERS (MRB-309…315) ════════════════════════════

     Nine consumer pages now share four questions: what time is it, how much
     is it, may this person write, and did a message just arrive. Each one
     is answered once, here, for the same reason the flag check is: four
     copies of "is this account writable" is four chances to write the
     fourth one with the sense inverted, and the one that gets it wrong
     lets a locked family submit work.
     ═════════════════════════════════════════════════════════════ */

  var MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];

  /* Both of these refuse to invent. An unparseable date is not "today" and
     is not the epoch — it is the fallback word, visibly. overview.html's
     `dash()` policy, applied to time. */
  function fmtDate(iso, fallback) {
    if (iso == null || iso === '') { return fallback == null ? 'Not set' : fallback; }
    var d = new Date(iso);
    if (isNaN(d.getTime())) { return fallback == null ? 'Not set' : fallback; }
    return d.getDate() + ' ' + MONTHS[d.getMonth()] + ' ' + d.getFullYear();
  }

  /* 12-hour with a lowercase suffix, because the chat panel it was written
     for is read by nine-year-olds. "16:05" is a timetable; "4:05pm" is a
     time somebody said something. */
  function fmtTime(iso, fallback) {
    if (iso == null || iso === '') { return fallback == null ? '' : fallback; }
    var d = new Date(iso);
    if (isNaN(d.getTime())) { return fallback == null ? '' : fallback; }
    var h = d.getHours(), m = d.getMinutes();
    var suffix = h < 12 ? 'am' : 'pm';
    h = h % 12; if (h === 0) { h = 12; }
    return h + ':' + (m < 10 ? '0' : '') + m + suffix;
  }

  /* Pence in, pounds out, always with both decimals. Never `toFixed` on a
     float that came from a division — the backend sends whole pence and
     this does integer arithmetic on them. */
  function money(pence) {
    if (pence == null || isNaN(Number(pence))) { return '—'; }
    var n = Math.round(Number(pence));
    var sign = n < 0 ? '-' : '';
    n = Math.abs(n);
    return sign + '£' + Math.floor(n / 100) + '.' + (n % 100 < 10 ? '0' : '') + (n % 100);
  }

  /* A mark-scheme point, whatever shape it arrived in.

     ⊕ FOUND BY DRIVING IT, 2 Sep 2026. The contract says `scheme: [strings]`,
     and `/child/exam-questions` sends strings — but `/admin/mb-queue` sends
     the same field as an array of objects, and the admin queue's first render
     printed four lines of `[object Object]` where the mark scheme should have
     been. If two endpoints already disagree about this field, a third will,
     so both shapes are read here rather than bet on in each renderer. An
     unrecognised shape renders as nothing, which is at least honest. */
  function schemePoint(pt) {
    if (pt == null) { return ''; }
    if (typeof pt === 'string') { return pt; }
    return String(pt.text || pt.point || pt.criterion || pt.description || '');
  }

  /* ── guard ─────────────────────────────────────────────────────
     The ACCESS state — `billing.access` for a parent, `access` on the child
     endpoints — is the authority, and it is a different value from the
     BILLING state: a family whose card failed yesterday is `past_due`
     (billing) and still `full` (access), because there is a seven-day
     grace period. Reading the billing word and disabling the submit button
     on it would lock a paying family out five days early.

     So: an access word is used as itself. A billing word handed in by
     mistake is mapped CONSERVATIVELY and the mapping is lossy on purpose —
     `past_due` becomes read_only here, which is stricter than the truth,
     because the safe direction for a guess about permission is "no".

     ⚠️ This is not a security boundary. It greys a button and writes a
     sentence; every write is re-authorised by the backend, which is where
     `requireWritable` lives. A page that disables nothing is untidy, not
     unsafe; a page that trusts this INSTEAD of the 423 is neither. */
  var ACCESS_FROM_BILLING = {
    active: 'full', trialing: 'full', comped: 'full',
    none: 'none', locked: 'locked',
    past_due: 'read_only', cancelled: 'read_only', canceled: 'read_only'
  };

  var GUARD_COPY = {
    read_only: {
      title: 'Read only just now',
      parent: 'You can see everything, but new work, marking and messages ' +
              'are paused until the subscription is sorted out.',
      child: 'You can read your lessons and look back at your work, but you ' +
             'can’t send or hand anything in at the moment. Your grown-up ' +
             'will know why.'
    },
    locked: {
      title: 'Paused',
      parent: 'This account is paused. Start it again from the account page ' +
              'and everything comes back exactly as it was.',
      child: 'Your account is paused, so you can read but not hand work in. ' +
             'Ask your grown-up to start it again.'
    },
    none: {
      title: 'Not started yet',
      parent: 'Start a subscription to switch on weekly work, marking and ' +
              'messages. Nothing you have set up is lost in the meantime.',
      child: 'Your account isn’t switched on yet, so you can look around ' +
             'but not hand work in. Ask your grown-up.'
    }
  };

  function guard(access, who) {
    var state = access;
    if (access && typeof access === 'object') {
      // `access` first: on the family response BOTH keys exist and only one
      // of them is the permission. See the note above.
      state = access.access != null ? access.access
            : (access.state != null ? access.state : null);
    }
    state = String(state == null ? '' : state).toLowerCase();
    if (ACCESS_FROM_BILLING[state]) { state = ACCESS_FROM_BILLING[state]; }
    if (state !== 'full' && state !== 'read_only' && state !== 'locked' && state !== 'none') {
      /* An access word nobody has seen before. Refuse rather than admit —
         and say so as itself rather than as "unknown", so it is findable. */
      return { state: state || 'unknown', writable: false,
               title: 'Not available',
               message: 'This account isn’t able to send or hand work in ' +
                        'right now. Please refresh, or email hello@mrbadmus.com.' };
    }
    if (state === 'full') {
      return { state: 'full', writable: true, title: '', message: '' };
    }
    var copy = GUARD_COPY[state];
    return {
      state: state,
      writable: false,
      title: copy.title,
      message: who === 'child' ? copy.child : copy.parent
    };
  }

  /* Renders guard()'s sentence at the top of a page, and hides itself when
     access is full. Returns the guard object so a caller can do both in one
     line: `var g = C.lockedBanner(el, data.access, 'child');`. */
  function lockedBanner(el, access, who) {
    var g = guard(access, who);
    if (!el) { return g; }
    if (g.writable) { el.innerHTML = ''; el.style.display = 'none'; return g; }
    el.className = 'c-locked';
    el.innerHTML = '<strong>' + escapeHtml(g.title) + '</strong>' +
                   '<span>' + escapeHtml(g.message) + '</span>';
    el.style.display = 'block';
    return g;
  }

  /* Disable (or re-enable) every write control on a page in one call. The
     controls name themselves with `data-write`, so adding a new button to a
     page cannot forget to be guarded — the attribute IS the registration. */
  function applyWritable(root, writable) {
    var nodes = (root || document).querySelectorAll('[data-write]');
    Array.prototype.forEach.call(nodes, function (n) { n.disabled = !writable; });
  }

  /* ── section ──────────────────────────────────────────────────
     One panel, one promise, and NEVER a rejection. Night 2's pages each read
     from five or six endpoints that are being written by four other people
     at the same time, so on any given evening some of them 404. A page whose
     chat panel takes the work list down with it teaches nothing about either.

     So every panel gets its own catch, and the failure lands inside the
     panel, in the words the backend used, with a hint. The page around it
     stays a page. */
  function section(el, promise, render, hint) {
    return Promise.resolve(promise).then(function (data) {
      try {
        render(data);
      } catch (e) {
        console.error('[consumer/section]', e);
        fail(el, 'We couldn’t show this part of the page.',
             'Refresh in a moment. If it keeps happening, email hello@mrbadmus.com.');
      }
    }, function (e) {
      console.error('[consumer/section]', e);
      fail(el, (e && e.message) || 'We couldn’t load this part of the page.',
           hint || 'This part of MrBadmus may not be switched on yet.');
    });
  }

  /* ── subscribeMessages ─────────────────────────────────────────
     Live chat, with the child's or parent's OWN JWT — which is the whole
     security argument: Supabase Realtime applies the same RLS policy to a
     `postgres_changes` stream that it applies to a select, so this
     subscribes to the entire `family_messages` table and receives only the
     rows the signed-in person was already allowed to read. There is no
     filter here to get wrong, and adding one would be a second, weaker copy
     of a policy that already exists.

     INSERT and UPDATE both, because a read receipt is an UPDATE and the
     unread dot has to clear on the other person's screen too.

     ⚠️ AS ONE `event: '*'` BINDING, NOT TWO. Registering INSERT and UPDATE
     as two separate `.on('postgres_changes', …)` calls on a single channel
     subscribes cleanly — `subscribe()` reports SUBSCRIBED, no error is
     raised anywhere — and then delivers NOTHING AT ALL. It is the worst
     shape a bug can have: every signal says it is working. Found by the
     chat executor on the night this was written, 2 Sep 2026. One binding,
     and the callback branches on `payload.eventType`.

     Failure is silent and non-fatal: realtime is an enhancement over the
     poll-on-send the pages already do. A websocket that will not open must
     never stop a child reading their messages. */
  function subscribeMessages(sb, onRow) {
    var noop = { unsubscribe: function () {} };
    if (!sb || typeof sb.channel !== 'function') { return noop; }
    try {
      var name = 'family-messages-' + Math.random().toString(36).slice(2);
      var ch = sb.channel(name)
        .on('postgres_changes',
            { event: '*', schema: 'public', table: 'family_messages' },
            function (p) {
              // See the two-bindings warning above: ONE binding, branch here.
              var kind = p && p.eventType;
              if (kind !== 'INSERT' && kind !== 'UPDATE') { return; }
              try { onRow(p.new, kind); } catch (e) { console.error('[consumer/rt]', e); }
            })
        .subscribe();
      return {
        channel: ch,
        unsubscribe: function () { try { sb.removeChannel(ch); } catch (e) { /* already gone */ } }
      };
    } catch (e) {
      console.error('[consumer/rt]', e);
      return noop;
    }
  }

  /* The Monday of the week a date falls in, as YYYY-MM-DD. Every work read
     is keyed on it, and a week that starts on Sunday in one place and Monday
     in another is a week of work that vanishes. Local time, deliberately:
     the parent and the child are in the same house and the same timezone,
     and a UTC Monday is Sunday evening to half of them. */
  function weekStart(d) {
    var x = d ? new Date(d) : new Date();
    if (isNaN(x.getTime())) { x = new Date(); }
    x.setHours(12, 0, 0, 0);                 // midday: immune to DST shifts
    var dow = x.getDay();                    // 0 Sun … 6 Sat
    x.setDate(x.getDate() - ((dow + 6) % 7));
    return x.getFullYear() + '-' +
           ('0' + (x.getMonth() + 1)).slice(-2) + '-' +
           ('0' + x.getDate()).slice(-2);
  }
  function shiftWeek(iso, weeks) {
    var d = new Date(iso + 'T12:00:00');
    if (isNaN(d.getTime())) { return weekStart(); }
    d.setDate(d.getDate() + (weeks * 7));
    return weekStart(d);
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
    notFound: notFound,

    // Night 2 (MRB-309…315)
    schemePoint: schemePoint,
    fmtDate: fmtDate,
    fmtTime: fmtTime,
    money: money,
    guard: guard,
    lockedBanner: lockedBanner,
    applyWritable: applyWritable,
    section: section,
    subscribeMessages: subscribeMessages,
    weekStart: weekStart,
    shiftWeek: shiftWeek
  };
})();
