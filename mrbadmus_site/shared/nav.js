/* ───────────────────────────────────────────────────────────────────────
   shared/nav.js — behaviour for the canonical public top-nav (MRB-109)

   Two jobs, both centralised here so every public page behaves identically:

   1. AUTH CONTROL. Renders #nav-auth-area: Sign In / Sign Up when signed
      out, the profile chip (with role-based routing + avatar) when signed in.
      Ported verbatim from the previous per-page inline script — the chip's
      accent-soft/accent/accent-border colour pair is the audited ~5.5:1
      contrast fix; do not weaken it. Role routing (staff → teacher-profile,
      students → profile-setup) is UX only; RLS guards the data. Does not
      touch redirectAfterAuth() — MRB-101 sign-in routing is unaffected.

   2. DRAWER. Injects an accessible full-menu drawer opened by the .nav-burger
      button: aria-expanded, Escape to close, outside-click to close, focus
      moves into the drawer on open and back to the button on close, focus is
      trapped while open, fully keyboard operable. The drawer's auth row
      mirrors the state rendered into #nav-auth-area.

   Loaded with `defer` on every public page. Degrades gracefully: if it fails
   to load, the persistent cluster (Challenge / Leaderboard / Search) and the
   default Sign In / Sign Up links remain usable from the HTML.
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

  // ── Drawer auth row — mirrors the signed-in / signed-out state ──────────
  function renderDrawerAuthSignedOut(slot) {
    if (!slot) return;
    slot.innerHTML =
      '<a href="/auth.html?tab=signin" class="btn-signin">Sign In</a>' +
      '<a href="/auth.html?tab=signup" class="btn-signup">Sign Up</a>';
  }
  function renderDrawerAuthSignedIn(slot, href, firstName, avatarUrl) {
    if (!slot) return;
    var inner = (avatarUrl
      ? '<img src="' + esc(avatarUrl) + '" alt="" style="width:26px;height:26px;border-radius:50%;object-fit:cover;border:2px solid var(--accent);"/> '
      : '👤 ') + '<span class="nav-chip-name">' + esc(firstName) + '</span>';
    slot.innerHTML = '<a href="' + href + '" class="nav-drawer-chip" style="background:var(--accent-soft);color:var(--accent);border:1px solid var(--accent-border);">' + inner + '</a>';
  }

  /* ⊕ B2C polish (9 Oct 2026) — SIGN IN IS IN THE BAR ON A DESKTOP.
     65b8cbf3a (MRB-109 follow-up, July) emptied #nav-auth-area for a
     signed-out visitor and left Sign In only inside the hamburger drawer, so
     at 1280px a visitor looking for it had to open a menu to find it. The
     bar's own copy is back, Sign In only (Sign Up stays in the drawer), and
     it is drawn here rather than in each page's HTML so every page that
     loads this file gets it from one place. At 900px and below nav.css and
     ks4-chrome.css hide it, so the phone bar is exactly what it was and the
     drawer is still the way in there. It is painted in the same task as the
     session check below, so a signed-in pupil never sees it flash. */
  function renderBarSignedOut(area) {
    if (!area) return;
    area.innerHTML = '<a href="' + carry('/auth.html?tab=signin') + '" class="btn-signin nav-bar-signin">Sign In</a>';
  }

  // ── Auth control (nav cluster + drawer) ─────────────────────────────────
  function initAuth(drawerAuthSlot) {
    var area = document.getElementById('nav-auth-area');
    // Default (signed-out) drawer state; upgraded below if a live session exists.
    renderDrawerAuthSignedOut(drawerAuthSlot);
    if (!area) return;
    // Default (signed-out) bar state; paintChip() replaces it when signed in.
    renderBarSignedOut(area);
    if (!SUPA_URL || !SUPA_KEY || !SESSION_KEY) return;

    try {
      var raw = localStorage.getItem(SESSION_KEY);
      if (!raw) return;
      var session = JSON.parse(raw);
      var user = session && session.user;
      // Expired stored session → keep Sign In / Sign Up (don't render a chip
      // that would 401 on click).
      var expMs = session && session.expires_at ? session.expires_at * 1000 : 0;
      if (!user || (expMs && expMs <= Date.now())) return;

      /* ⊕ MRB-337/N5, 8 Sep 2026 — THE EMAIL LOCAL PART IS NOT A NAME.
         This used to read `... || (user.email && user.email.split('@')[0])`,
         so a pupil whose sign-up carried no `first_name` in `user_metadata`
         — which is most of a rostered school, because the roster import
         writes names to `profiles`, not to the auth metadata — wore their
         own email address in the top bar: `👤 aiden.cole`.

         Two things were wrong with that, and only one of them is layout.
         It is a name a shared classroom screen should not be showing at all;
         and it is unbounded, so on a 390px phone the cluster reached 395.3px
         and the bar scrolled sideways. `profiles.first_name` is the real
         name and was already being fetched ONE LINE BELOW for the role
         route — the same request, the same round trip, one more column.

         So: metadata if the sign-up carried one, else the cached profile
         name, else the profile fetch when it lands, else a short generic
         word. The email is not in that ladder at any rung. The cap in
         `shared/nav.css` (`.nav-chip-name`) is the other half: a fix that
         depends on names being short is not a fix. */
      var nameKey = 'mrb-profile-name:' + user.id;
      var firstName = (user.user_metadata && user.user_metadata.first_name) || '';
      if (!firstName) {
        try { firstName = localStorage.getItem(nameKey) || ''; } catch (err) {}
      }
      if (!firstName) { firstName = 'You'; }

      // Route the chip by advisory role, cached PER USER so a previous
      // account's route can't leak onto a different signed-in user.
      var hrefKey = 'mrb-profile-href:' + user.id;
      var profileHref = '/profile-setup.html';
      try { profileHref = localStorage.getItem(hrefKey) || profileHref; } catch (err) {}

      // The avatar the chip is currently wearing, so a NAME change can
      // repaint without knowing whether an avatar has landed yet.
      var shownAvatar = null;

      function paintChip(avatarUrl) {
        shownAvatar = avatarUrl || null;
        var inner = avatarUrl
          ? '<img src="' + esc(avatarUrl) + '" style="width:28px;height:28px;border-radius:50%;object-fit:cover;border:2px solid var(--accent);" alt=""/><span class="nav-chip-name" style="color:var(--accent);font-weight:700;font-size:0.82rem;">' + esc(firstName) + '</span>'
          : '👤 <span class="nav-chip-name">' + esc(firstName) + '</span>';
        var style = avatarUrl
          ? 'display:flex;align-items:center;gap:6px;text-decoration:none;white-space:nowrap;'
          : 'background:var(--accent-soft);color:var(--accent);border:1px solid var(--accent-border);padding:5px 12px;border-radius:999px;font-weight:700;font-size:0.82rem;text-decoration:none;white-space:nowrap;';
        area.innerHTML = '<a id="nav-profile-link" href="' + profileHref + '" style="' + style + '">' + inner + '</a>';
        renderDrawerAuthSignedIn(drawerAuthSlot, profileHref, firstName, avatarUrl);
        carryLinks();
      }

      paintChip(null);

      // Resolve role → correct profile route (staff vs student). A 401/empty
      // response must NOT overwrite the cached route with the student default.
      fetch(SUPA_URL + '/rest/v1/profiles?id=eq.' + user.id + '&select=role,first_name', {
        headers: { 'apikey': SUPA_KEY, 'Authorization': 'Bearer ' + session.access_token }
      }).then(function (r) { return r.ok ? r.json() : null; }).then(function (rows) {
        if (!rows || !rows[0]) return;
        profileHref = (rows[0].role && rows[0].role !== 'student') ? '/teacher-profile.html' : '/profile-setup.html';
        try { localStorage.setItem(hrefKey, profileHref); } catch (err) {}
        // The real name, cached per user like the route above it, so the next
        // page does not have to open on 'You' and then correct itself.
        var real = rows[0].first_name;
        if (real && real !== firstName) {
          firstName = real;
          try { localStorage.setItem(nameKey, real); } catch (err) {}
          paintChip(shownAvatar);   // repaints the drawer chip too
        }
        var link = document.getElementById('nav-profile-link');
        if (link) link.setAttribute('href', carry(profileHref));
        var dchip = drawerAuthSlot && drawerAuthSlot.querySelector('a');
        if (dchip) dchip.setAttribute('href', carry(profileHref));
      }).catch(function () {});

      /* Fetch avatar (best-effort) and upgrade the chip to show it.

         ⊕ MRB-336, 8 Sep 2026 — THROUGH config.js, like the two constants at
         the top of this file. It named production outright, and it is only
         reached once a session has been FOUND — so while the session lookup
         above was also pinned to production this line could never run outside
         the live site, and fixing the lookup is what exposed it. In any other
         world it is a cross-origin call to a backend that has never heard of
         the origin: a red CORS line on every page that carries this nav, for a
         request whose answer is a best-effort avatar. */
      if (NAVCFG.BACKEND_URL) fetch(NAVCFG.BACKEND_URL + '/api/profile', {
        headers: { 'Authorization': 'Bearer ' + session.access_token }
      }).then(function (r) { return r.ok ? r.json() : null; }).then(function (profile) {
        if (profile && profile.avatar_url) paintChip(profile.avatar_url);
      }).catch(function () {});
    } catch (e) {}
  }

  // ── Drawer (full menu) ──────────────────────────────────────────────────
  var MENU = [
    { ico: '🏠', label: 'Home', href: '/index.html' },
    { ico: '⚡', label: 'Challenge', href: '/weekly-challenge.html' },
    { ico: '🏆', label: 'Leaderboard', href: '/leaderboard.html' },
    // A microscope rather than the anatomical heart this link used to be: the
    // studio holds eight specimens, and only one of them is a heart. The drawer
    // row is labelled either way — the glyph is company for the word, never a
    // substitute for it.
    { ico: '🔬', label: '3D Studio', href: '/3d/' },
    { ico: '🧪', label: 'Simulations', href: '/simulations/' },
    { ico: '📄', label: 'Past Papers', href: '/past-papers.html' },
    { ico: '📚', label: 'Revision', href: '/revision.html' },
    { ico: '📊', label: 'My Challenges', href: '/my-challenges.html' },
    { ico: '🔍', label: 'Search', search: true }
  ];

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
       creation, not only inside close(): the drawer is built once and
       starts life off-canvas (`transform: translateX(100%)`, no `.open`
       class yet), and `inert` on this attribute right now, not toggled
       later, means there is never a frame where a freshly-built, closed
       drawer is reachable. `open()`/`close()` below toggle both away and
       back. `inert` (not just `aria-hidden`) is what actually pulls its
       twelve links/buttons — and, since the theme run, the Light/Dark/
       System radios — out of the TAB ORDER; `aria-hidden` alone hides it
       from a screen reader's tree but a sighted keyboard user would still
       Tab into an invisible off-canvas control. `.nav-overlay`, the scrim,
       needs no such treatment — it is `visibility: hidden` while closed,
       which already removes it from both the accessibility tree and the
       tab order on its own. */
    drawer.inert = true;
    drawer.setAttribute('aria-hidden', 'true');

    var menuItems = MENU.map(function (m) {
      if (m.search) {
        return '<button type="button" class="nav-drawer-link" data-search="1">' +
          '<span class="nav-drawer-ico">' + m.ico + '</span>' + m.label + '</button>';
      }
      return '<a href="' + m.href + '"><span class="nav-drawer-ico">' + m.ico + '</span>' + m.label + '</a>';
    }).join('');

    drawer.innerHTML =
      '<div class="nav-drawer-head">' +
        '<span class="nav-drawer-title">Menu</span>' +
        '<button type="button" class="nav-drawer-close" aria-label="Close menu">&times;</button>' +
      '</div>' +
      '<nav class="nav-drawer-menu" aria-label="Full site menu">' + menuItems + '</nav>' +
      // Theme run (27 Sep 2026): the Light / Dark / System control lives here
      // on every width, and is the ONLY copy below 900px, where nav.css hides
      // the bar's own slot — the bar's measured phone ladder (MRB-259/337) has
      // no 96px to spare once a pupil is signed in and the bell is up.
      // shared/theme.js mounts into it and keeps both copies in step.
      '<div class="nav-drawer-theme"><span class="nav-drawer-theme-label">Theme</span>' +
        '<span class="mrb-theme-slot" data-mrb-theme></span></div>' +
      '<div class="nav-drawer-auth" id="nav-drawer-auth"></div>';

    document.body.appendChild(overlay);
    document.body.appendChild(drawer);
    return { overlay: overlay, drawer: drawer };
  }

  function initDrawer() {
    var burger = document.querySelector('.nav-burger');
    if (!burger) return null;

    var built = buildDrawer();
    var overlay = built.overlay;
    var drawer = built.drawer;
    var closeBtn = drawer.querySelector('.nav-drawer-close');
    var lastFocused = null;

    function focusables() {
      return Array.prototype.slice.call(
        drawer.querySelectorAll('a[href], button:not([disabled]), input, [tabindex]:not([tabindex="-1"])')
      ).filter(function (el) { return el.offsetParent !== null; });
    }

    function open() {
      lastFocused = document.activeElement;
      // ⊕ D12 — remove BEFORE the drawer needs to take focus: an inert
      // subtree cannot receive it, so this must run before the
      // focusables()/.focus() call three lines down, not after.
      drawer.inert = false;
      drawer.removeAttribute('aria-hidden');
      overlay.classList.add('open');
      drawer.classList.add('open');
      burger.setAttribute('aria-expanded', 'true');
      document.body.style.overflow = 'hidden';
      var f = focusables();
      (f[0] || drawer).focus();
    }
    function close() {
      overlay.classList.remove('open');
      drawer.classList.remove('open');
      // ⊕ D12 — restored once the drawer is closing. `close()` moves focus
      // back to the burger a few lines down, off the drawer entirely, so
      // setting `inert` here never strands focus inside a now-inert node.
      drawer.inert = true;
      drawer.setAttribute('aria-hidden', 'true');
      burger.setAttribute('aria-expanded', 'false');
      document.body.style.overflow = '';
      // Return focus to the button that opened the drawer (spec requirement).
      // Fall back to whatever was focused before, if the burger is gone.
      if (burger && burger.focus) burger.focus();
      else if (lastFocused && lastFocused.focus) lastFocused.focus();
    }
    function isOpen() { return drawer.classList.contains('open'); }

    burger.addEventListener('click', function () { isOpen() ? close() : open(); });
    closeBtn.addEventListener('click', close);
    overlay.addEventListener('click', close);

    // Search item opens the site-wide overlay (same wiring as the nav icon).
    var searchBtn = drawer.querySelector('[data-search]');
    if (searchBtn) {
      searchBtn.addEventListener('click', function () {
        close();
        if (window.MRBSearch) window.MRBSearch.open();
      });
    }

    // Close on link click (so the drawer doesn't linger over the new page nav).
    drawer.querySelectorAll('.nav-drawer-menu a').forEach(function (a) {
      a.addEventListener('click', function () { close(); });
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

    return drawer.querySelector('#nav-drawer-auth');
  }

  function boot() {
    var drawerAuthSlot = initDrawer();      // null if no .nav-burger on the page
    initAuth(drawerAuthSlot);
    carryLinks();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    boot();
  }
})();
