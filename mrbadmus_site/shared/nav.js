/* ───────────────────────────────────────────────────────────────────────
   shared/nav.js — behaviour for the canonical public top-nav (MRB-109)

   ⊕ Front door (12 Oct 2026) — the ONE public bar and its ONE drawer, for
   every public system (classic nav, KS4 chrome, the KS3 / KS4-pilot /
   leaderboard bars, simulations, 3D Studio). Two jobs:

   1. THE HOME BUTTON. Paints `#nav-auth-area`: "Sign in" when signed out;
      when signed in, the one button for this kind of person (shared/
      account.js decides which — nothing here routes).

   2. THE DRAWER. Opened by any `.nav-burger` on the page: the account
      section at the top (name · kind, My profile, Switch account, Sign out —
      or Sign in / Sign up), then the site links. Accessible: aria-expanded,
      Escape, outside-click, focus into the drawer on open and back to the
      button on close, focus trapped while open. Its CSS is shared/drawer.css.

   Loaded with `defer` on every public page, after shared/account.js. Degrades
   gracefully: without account.js the signed-in bar shows no button and the
   drawer still offers a plain Sign out.
   ─────────────────────────────────────────────────────────────────────── */
(function () {
  'use strict';

  /* ⊕ MRB-336, 8 Sep 2026 — THROUGH shared/config.js, AND THE SESSION KEY
     WITH IT. These named production outright, and one line below they picked
     the localStorage slot a session is read from — `sb-<project ref>-auth-
     token`. So on any world but the live one this nav could not find the
     signed-in student at ALL: it fell through to its own signed-out branch and
     drew `Sign In / Sign Up` over the head of a pupil who was signed in, on
     every page that loads it. Measured on four of them in this sweep.

     The production literals stay as the fallback, so a page that somehow loses
     config.js behaves exactly as it does today, and on mrbadmus.com config.js
     resolves to these same two values. `shared/student-bell.js` derives its
     ref from the configured URL the same way; this is the same derivation, not
     a second rule. */
  /* ⊕ Test isolation (5 Oct 2026) — and NO production fallback. The
     paragraph above kept "the production literals as the fallback, so a page
     that somehow loses config.js behaves exactly as it does today". On a test
     page that is the failure: it reads the live project. Without config this
     nav now stays signed-out and makes no call; on mrbadmus.com config.js is
     on every page that loads this file, ahead of it. */
  var NAVCFG = window.MrBadmusConfig || {};
  var SUPA_URL = NAVCFG.SUPABASE_URL || '';
  var SUPA_KEY = NAVCFG.SUPABASE_ANON_KEY || '';
  var SESSION_KEY = NAVCFG.AUTH_STORAGE_KEY || '';

  function esc(s) { var d = document.createElement('div'); d.textContent = s == null ? '' : s; return d.innerHTML; }

  /* ⊕ B2C polish (9 Oct 2026) — THE TEST WORLD SURVIVES A NAV CLICK.
     A page opened on `?env=test&api=…` lost both on "Sign In" (and on every
     other nav link), so the next page — auth.html, the app — resolved
     shared/config.js to PRODUCTION. This carries `env` and `api` across
     every root-relative link in the nav bar and the drawer, and every link
     into /auth.html anywhere on the page, exactly as consumer-common.js's
     `href()` does across the consumer links: the link's own query and hash
     are kept, a key it already sets is not overwritten. On the live site the
     URL carries neither, CARRY is empty, and every href is left untouched. */
  var CARRY = (function () {
    var out = [];
    try {
      var here = new URLSearchParams(window.location.search);
      ['env', 'api'].forEach(function (k) { var v = here.get(k); if (v) { out.push([k, v]); } });
    } catch (e) {}
    return out;
  })();

  function carry(href) {
    if (!CARRY.length || typeof href !== 'string' || href === '') { return href; }
    if (href.charAt(0) === '#') { return href; }                            // same page
    var asWritten = href;
    if (href.charAt(0) !== '/' || href.charAt(1) === '/') {
      /* ⊕ Round 3 — a page-relative ("ks4.html", "?tab=x") or same-origin
         absolute link is the same journey: resolve it, and carry it as the
         root-relative path it names. Another origin, mailto:, javascript:,
         blob: and the like are left exactly as written. */
      var u;
      try { u = new URL(href, window.location.href); } catch (e) { return href; }
      if (u.origin !== window.location.origin || !/^https?:$/.test(u.protocol)) { return href; }
      href = u.pathname + u.search + u.hash;
    }
    var hash = '', h = href.indexOf('#');
    if (h >= 0) { hash = href.slice(h); href = href.slice(0, h); }
    var own = '', i = href.indexOf('?');
    if (i >= 0) { own = href.slice(i + 1); href = href.slice(0, i); }
    var q = new URLSearchParams(own);
    var missing = CARRY.filter(function (kv) { return !q.has(kv[0]); });
    if (!missing.length) { return asWritten; }                            // already carried
    missing.forEach(function (kv) { q.set(kv[0], kv[1]); });
    var str = q.toString();
    return href + (str ? '?' + str : '') + hash;
  }

  /* ⊕ Round 3 (9 Oct 2026) — EVERY LINK ON THE PAGE, not only the nav's.
     A blind run on / with ?env=test&api=… found the KS3 and GCSE cards,
     "Take the challenge", the footer, and the "Today" entry class-entry.js
     draws into the bar and the drawer all pointing at bare paths: the
     next page resolved config.js to PRODUCTION. So: one pass over every
     <a href> at boot, a MutationObserver that carries any link drawn or
     re-pointed later (the class entry, the chip, a page's own script), and
     the click-time rewrite as the last word. On the live site CARRY is
     empty, none of this runs, and every href is exactly as written. */
  function carryOne(a) {
    var h = a.getAttribute('href');
    if (h == null) { return; }
    var n = carry(h);
    if (n !== h) { a.setAttribute('href', n); }
  }

  function carryLinks(root) {
    if (!CARRY.length) { return; }
    try {
      root = root || document;
      if (root.nodeType === 1 && root.matches('a[href]')) { carryOne(root); }
      if (root.querySelectorAll) { root.querySelectorAll('a[href]').forEach(carryOne); }
    } catch (e) {}
  }

  if (CARRY.length) {
    var onFollow = function (e) {
      var a = e.target && e.target.closest ? e.target.closest('a[href]') : null;
      if (a) { carryOne(a); }
    };
    document.addEventListener('click', onFollow, true);
    document.addEventListener('auxclick', onFollow, true);       // middle-click: a new tab
    document.addEventListener('contextmenu', onFollow, true);    // "Open in new tab" / "Copy link"
    try {
      new MutationObserver(function (records) {
        records.forEach(function (r) {
          if (r.type === 'attributes') { if (r.target.nodeType === 1 && r.target.matches('a[href]')) { carryOne(r.target); } return; }
          r.addedNodes.forEach(function (n) { if (n.nodeType === 1) { carryLinks(n); } });
        });
      }).observe(document.documentElement, { childList: true, subtree: true, attributes: true, attributeFilter: ['href'] });
    } catch (e) {}
  }

  if (window.MRB_NAV_TEST_HOOK) { window.MRB_NAV_TEST_HOOK.carry = carry; }

  /* ⊕ D15d (13 Oct 2026) — THE PASTE HINT IS ONLY FOR A KEYBOARD.
     The tutor's box used to say "(paste screenshots with Ctrl+V)" on every
     device, phones included, where there is no Ctrl and no V. The page now
     ships the neutral "Ask MrBadmus anything..." (generate_site_v5.py
     chat_html, index.html, ks4.html, each marked `data-paste-hint`) and the
     hint is added here only where a mouse or trackpad says a keyboard is
     there too — ⌘V on a Mac, Ctrl+V elsewhere. */
  function pasteHint() {
    try {
      if (!window.matchMedia || !window.matchMedia('(hover: hover) and (pointer: fine)').matches) { return; }
      var mac = /Mac|iPhone|iPad|iPod/.test(navigator.platform || navigator.userAgent || '');
      var tail = ' (paste a screenshot with ' + (mac ? '\u2318V' : 'Ctrl+V') + ')';
      document.querySelectorAll('input[data-paste-hint]').forEach(function (i) {
        if (i.getAttribute('data-paste-hint') === 'done') { return; }
        i.setAttribute('data-paste-hint', 'done');
        i.setAttribute('placeholder', (i.getAttribute('placeholder') || '') + tail);
      });
    } catch (e) {}
  }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', pasteHint);
  } else {
    pasteHint();
  }

  /* ═══════════════════════════════════════════════════════════════════════
     ⊕ FRONT DOOR (12 Oct 2026) — THE ONE PUBLIC BAR, AND ITS ONE DRAWER

     Everything below this line used to be a name chip, a Challenge pill, a
     Sign Up button and a drawer whose first row was a profile link. A parent
     who tapped "Dad" was sent to a teacher page; there was no Sign out
     anywhere on a public page but the pupil avatar menu.

     The bar now holds: brand · theme · ONE home button · hamburger. This
     file paints the home button into `#nav-auth-area` and builds the drawer,
     and it is the only drawer in the estate — the classic nav, the KS4
     chrome, the KS3 and KS4-pilot bars, the leaderboard, the simulations and
     the 3D Studio all load THIS file and the same shared/drawer.css.

     WHO the person is and WHERE their home is come from shared/account.js
     (the one map). Nothing here decides a route.

     ── The home button ─────────────────────────────────────────────────────
     Signed out        "Sign in" → /auth.html?tab=signin
     Signed in         the kind's home button: pupil "My class" / "My classes",
                       staff "My classes", parent and organisation staff and
                       the operator "My dashboard", a family child "Today".
     Signed-in pupil with NO class: NO button. The only page a classless pupil
       could be sent to is /student/classes.html, whose empty state says
       "Back to homepage" — a loop. There is no join-by-code path on the site
       (classes come from the teacher's roster), so the honest answer is
       nothing in the bar and "My profile" in the drawer.

     It is painted in the same task as the session check, so a signed-in
     person never sees "Sign in" flash: with a session the slot is filled from
     the last answer for this person (localStorage, per user id, dropped by
     sign-out) or left empty until the map answers. The slot is re-painted if
     a page's runtime redraws the bar.
     ═══════════════════════════════════════════════════════════════════════ */
  var HOME_PREFIX = 'mrb-home:v1:';
  var HIDE_FOR = { parent: 1, child: 1, org_staff: 1, operator: 1 };
  var HIDE_HREFS = ['/weekly-challenge.html', '/leaderboard.html', '/my-challenges.html'];

  var state = { mode: null, home: undefined, acct: null };   // mode: 'out' | 'in'

  function storedUser() {
    try {
      if (!SESSION_KEY) return null;
      var raw = localStorage.getItem(SESSION_KEY);
      if (!raw) return null;
      if (raw.indexOf('base64-') === 0) raw = decodeURIComponent(escape(atob(raw.slice(7))));
      var s = JSON.parse(raw);
      var expMs = s && s.expires_at ? s.expires_at * 1000 : 0;
      if (!s || !s.user || !s.user.id || (expMs && expMs <= Date.now())) return null;
      return s.user;
    } catch (e) { return null; }
  }

  function homeArea() { return document.getElementById('nav-auth-area'); }

  function paintBar() {
    var area = homeArea();
    if (!area) return;
    if (state.mode === 'out') {
      area.innerHTML = '<a href="' + esc(carry('/auth.html?tab=signin')) + '" class="mrb-homebtn">Sign in</a>';
    } else if (state.mode === 'in' && state.home) {
      area.innerHTML = '<a href="' + esc(carry(state.home.href)) + '" class="mrb-homebtn">' + esc(state.home.label) + '</a>';
    } else {
      area.innerHTML = '';
    }
    carryLinks(area);
  }

  // ── Drawer (full menu) ──────────────────────────────────────────────────
  var MENU = [
    { ico: '🏠', label: 'Home', href: '/index.html' },
    { ico: '📘', label: 'KS3', href: '/ks3/' },
    { ico: '🎯', label: 'GCSE', href: '/ks4.html' },
    { ico: '🧪', label: 'Simulations', href: '/simulations/' },
    // A microscope rather than the anatomical heart this link used to be: the
    // studio holds eight specimens, and only one of them is a heart.
    { ico: '🔬', label: '3D Studio', href: '/3d/' },
    { ico: '⚡', label: 'Challenge', href: '/weekly-challenge.html' },
    { ico: '🏆', label: 'Leaderboard', href: '/leaderboard.html' },
    { ico: '📄', label: 'Past papers', href: '/past-papers.html' },
    { ico: '📚', label: 'Revision', href: '/revision.html' },
    { ico: '📊', label: 'My Challenges', href: '/my-challenges.html' },
    { ico: '🔍', label: 'Search', search: true }
  ];

  var drawerEl = null;

  /* Search opens the site-wide overlay. Pages that carry it (the classic nav,
     the KS4 chrome) already have shared/search.js; the others (KS3, the KS4
     pilot lessons, the leaderboard) name the two files in
     `window.MRB_SEARCH_SRC` — written as quoted /shared/ paths in the page,
     so the build's cache-bust pass stamps them like any <script src> — and
     they are fetched the first time Search is pressed, not on every page
     load (search-index.js is 88KB). Never an unstamped URL: /shared/* is
     served `immutable`. A page with neither simply has no Search row. */
  function openSearch() {
    if (window.MRBSearch) { window.MRBSearch.open(); return; }
    var src = window.MRB_SEARCH_SRC;
    if (!src || !src.length) return;
    var i = 0;
    (function next() {
      if (i >= src.length) { if (window.MRBSearch) window.MRBSearch.open(); return; }
      var el = document.createElement('script');
      el.src = src[i++];
      el.onload = next;
      el.onerror = function () { /* no search is better than a broken bar */ };
      document.head.appendChild(el);
    })();
  }

  function buildDrawer() {
    var overlay = document.createElement('div');
    overlay.className = 'nav-overlay';
    overlay.id = 'nav-overlay';

    var drawer = document.createElement('aside');
    drawer.className = 'nav-drawer';
    drawer.id = 'nav-drawer';
    drawer.setAttribute('role', 'dialog');
    drawer.setAttribute('aria-modal', 'true');
    drawer.setAttribute('aria-label', 'Main menu');
    /* ⊕ D12 (theme-run audit, 27 Sep 2026) — CLOSED by default, here at
       creation: `inert` pulls every link out of the TAB ORDER (aria-hidden
       alone would still let a sighted keyboard user Tab into an invisible
       off-canvas control). open()/close() toggle both. */
    drawer.inert = true;
    drawer.setAttribute('aria-hidden', 'true');

    var menuItems = MENU.map(function (m) {
      if (m.search) {
        return '<button type="button" class="nav-drawer-link" data-search="1" hidden>' +
          '<span class="nav-drawer-ico">' + m.ico + '</span>' + m.label + '</button>';
      }
      return '<a href="' + m.href + '"><span class="nav-drawer-ico">' + m.ico + '</span>' + m.label + '</a>';
    }).join('');

    /* No theme row: the bar carries the theme control at every width now. */
    drawer.innerHTML =
      '<div class="nav-drawer-head">' +
        '<span class="nav-drawer-title">Menu</span>' +
        '<button type="button" class="nav-drawer-close" aria-label="Close menu">&times;</button>' +
      '</div>' +
      '<div class="nav-drawer-account" id="nav-drawer-account"></div>' +
      '<nav class="nav-drawer-menu" aria-label="Full site menu">' + menuItems + '</nav>';

    document.body.appendChild(overlay);
    document.body.appendChild(drawer);
    return { overlay: overlay, drawer: drawer };
  }

  function paintAccount() {
    var box = document.getElementById('nav-drawer-account');
    if (!box) return;
    var a = state.acct;
    var html = '';
    if (state.mode === 'out') {
      html = '<div class="nav-account-actions">' +
        '<a href="/auth.html?tab=signin" class="nav-account-btn nav-account-btn--primary">Sign in</a>' +
        '<a href="/auth.html?tab=signup" class="nav-account-btn">Sign up</a></div>';
    } else if (state.mode === 'in') {
      var id = a && a.kindLabel
        ? (a.name ? '<strong>' + esc(a.name) + '</strong> · ' + esc(a.kindLabel) : '<strong>' + esc(a.kindLabel) + '</strong>')
        : '<strong>Signed in</strong>';
      html = '<p class="nav-account-id">' + id + '</p><div class="nav-account-actions">' +
        (a && a.profileUrl ? '<a href="' + esc(a.profileUrl) + '" class="nav-account-btn">My profile</a>' : '') +
        /* A family or organisation child has one door, /go/; an adult's
           sign-in page is not theirs (front door, 16 Oct 2026). */
        (a && a.kind === 'child' ? '' : '<button type="button" class="nav-account-btn" data-act="switch">Switch account</button>') +
        '<button type="button" class="nav-account-btn" data-act="signout">Sign out</button></div>';
    }
    box.innerHTML = html;
    carryLinks(box);
  }

  function paintMenuForKind() {
    var drawer = drawerEl;
    if (!drawer) return;
    var hide = !!(state.acct && HIDE_FOR[state.acct.kind]);
    /* Matched on the PATH, not the attribute: on a test page `carry()` has
       appended ?env=…&api=… to every href, and an exact [href="…"] selector
       would then find nothing and hide nothing. */
    Array.prototype.forEach.call(drawer.querySelectorAll('.nav-drawer-menu a[href]'), function (a) {
      if (HIDE_HREFS.indexOf(String(a.getAttribute('href')).split('?')[0]) !== -1) a.hidden = hide;
    });
  }

  /* The fallback when shared/account.js is not on the page: clear the stored
     token and go to the school door. The real sign-out (the map's) also
     revokes at the server, drops the caches and lands on the front page. */
  function fallbackSignOut(to) {
    try { if (SESSION_KEY) localStorage.removeItem(SESSION_KEY); } catch (e) {}
    window.location.replace(carry(to || '/'));
  }

  function initDrawer() {
    var built = buildDrawer();
    var overlay = built.overlay;
    var drawer = built.drawer;
    drawerEl = drawer;
    var closeBtn = drawer.querySelector('.nav-drawer-close');
    var lastFocused = null;
    var activeBurger = null;

    function burgers() { return document.querySelectorAll('.nav-burger'); }
    function setExpanded(v) {
      burgers().forEach(function (b) { b.setAttribute('aria-expanded', v ? 'true' : 'false'); });
    }
    function focusables() {
      return Array.prototype.slice.call(
        drawer.querySelectorAll('a[href], button:not([disabled]), input, [tabindex]:not([tabindex="-1"])')
      ).filter(function (el) { return el.offsetParent !== null; });
    }

    function open(from) {
      lastFocused = from || document.activeElement;
      activeBurger = from || null;
      // Search is offered only where the page has the overlay to open.
      var sb = drawer.querySelector('[data-search]');
      if (sb) sb.hidden = !(window.MRBSearch || window.MRB_SEARCH_SRC);
      // ⊕ D12 — remove BEFORE the drawer needs to take focus: an inert
      // subtree cannot receive it.
      drawer.inert = false;
      drawer.removeAttribute('aria-hidden');
      overlay.classList.add('open');
      drawer.classList.add('open');
      setExpanded(true);
      document.body.style.overflow = 'hidden';
      var f = focusables();
      (f[0] || drawer).focus();
    }
    function close() {
      overlay.classList.remove('open');
      drawer.classList.remove('open');
      drawer.inert = true;
      drawer.setAttribute('aria-hidden', 'true');
      setExpanded(false);
      document.body.style.overflow = '';
      // Return focus to the button that opened the drawer (spec requirement).
      var back = (activeBurger && activeBurger.isConnected) ? activeBurger : document.querySelector('.nav-burger');
      if (back && back.focus) back.focus();
      else if (lastFocused && lastFocused.focus) lastFocused.focus();
    }
    function isOpen() { return drawer.classList.contains('open'); }

    /* Delegated, not bound: a page's runtime may redraw its bar (the KS4
       pilot lessons do), and a listener on the old node would be lost. */
    document.addEventListener('click', function (e) {
      var b = e.target && e.target.closest ? e.target.closest('.nav-burger') : null;
      if (!b) return;
      e.preventDefault();
      if (isOpen()) close(); else open(b);
    });
    closeBtn.addEventListener('click', close);
    overlay.addEventListener('click', close);

    drawer.addEventListener('click', function (e) {
      var t = e.target && e.target.closest ? e.target.closest('a, button') : null;
      if (!t) return;
      if (t.hasAttribute('data-search')) {
        close();
        openSearch();
        return;
      }
      var act = t.getAttribute('data-act');
      if (act) {
        var A = window.MrBadmusAccount;
        if (act === 'signout') { if (A) A.signOut(); else fallbackSignOut('/'); }
        else if (act === 'switch') { if (A) A.switchAccount(); else fallbackSignOut('/auth.html'); }
        return;
      }
      if (t.tagName === 'A') close();   // so the drawer doesn't linger over the new page
    });

    // Escape + focus trap.
    document.addEventListener('keydown', function (e) {
      if (!isOpen()) return;
      if (e.key === 'Escape') { e.preventDefault(); close(); return; }
      if (e.key === 'Tab') {
        var f = focusables();
        if (!f.length) return;
        var first = f[0], last = f[f.length - 1];
        if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
        else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
      }
    });
  }

  function applyAccount(acct) {
    state.acct = acct;
    if (!acct) {
      // The stored session no longer resolves to anyone (expired or removed).
      state.mode = 'out'; state.home = undefined;
    } else {
      state.mode = 'in';
      if (acct.kind) {
        state.home = acct.homeButton || null;
        var user = storedUser();
        try {
          if (user) localStorage.setItem(HOME_PREFIX + user.id, JSON.stringify(state.home || { none: 1 }));
        } catch (e) {}
      }
    }
    paintBar();
    paintAccount();
    paintMenuForKind();
  }

  function initBar() {
    var user = storedUser();
    if (!user) {
      state.mode = 'out';
      paintBar();
      paintAccount();
      return;
    }
    // Signed in: never "Sign in". The last answer for THIS person fills the
    // slot instantly; with none, it stays empty until the map answers.
    state.mode = 'in';
    /* ⊕ Front door (16 Oct 2026) — a hint is only a stand-in for the map's
       answer, so it is used only on a page that HAS the map. Without
       account.js nothing would ever confirm it or withdraw it, and a pupil
       who has since left their class would keep a button to a dead end. */
    var A = window.MrBadmusAccount;
    try {
      var hint = JSON.parse(localStorage.getItem(HOME_PREFIX + user.id) || 'null');
      state.home = A && hint && hint.href ? hint : null;
    } catch (e) { state.home = null; }
    paintBar();
    paintAccount();
    if (!A) return;
    A.resolve().then(applyAccount, function () {});
  }

  /* A runtime that redraws the bar (the KS4 pilot lessons) empties the slot;
     refill it from the last answer rather than leaving the page without one. */
  function watchBar() {
    if (!window.MutationObserver) return;
    var queued = false;
    new MutationObserver(function () {
      if (queued) return;
      queued = true;
      (window.requestAnimationFrame || setTimeout)(function () {
        queued = false;
        var area = homeArea();
        if (area && state.mode && !area.firstElementChild && (state.mode === 'out' || state.home)) paintBar();
      });
    }).observe(document.documentElement, { childList: true, subtree: true });
  }

  function boot() {
    initDrawer();
    initBar();
    watchBar();
    carryLinks();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    boot();
  }
})();
