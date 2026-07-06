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

  var SUPA_URL = 'https://urklkrwevjtlfbwnipjn.supabase.co';
  var SUPA_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVya2xrcndldmp0bGZid25pcGpuIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzQxOTQyNzksImV4cCI6MjA4OTc3MDI3OX0.pW9AP6TPlKC_XHDTbrEKrEGmGXglN0z5b0KGXD2oHvg';

  function esc(s) { var d = document.createElement('div'); d.textContent = s == null ? '' : s; return d.innerHTML; }

  // ── Drawer auth row — mirrors the signed-in / signed-out state ──────────
  function renderDrawerAuthSignedOut(slot) {
    if (!slot) return;
    slot.innerHTML =
      '<a href="/auth.html?tab=signin" class="btn-signin">Sign In</a>' +
      '<a href="/auth.html?tab=signup" class="btn-signup">Sign Up</a>';
  }
  function renderDrawerAuthSignedIn(slot, href, firstName, avatarUrl) {
    if (!slot) return;
    var inner = avatarUrl
      ? '<img src="' + esc(avatarUrl) + '" alt="" style="width:26px;height:26px;border-radius:50%;object-fit:cover;border:2px solid var(--accent);"/> ' + esc(firstName)
      : '👤 ' + esc(firstName);
    slot.innerHTML = '<a href="' + href + '" class="nav-drawer-chip" style="background:var(--accent-soft);color:var(--accent);border:1px solid var(--accent-border);">' + inner + '</a>';
  }

  // ── Auth control (nav cluster + drawer) ─────────────────────────────────
  function initAuth(drawerAuthSlot) {
    var area = document.getElementById('nav-auth-area');
    // Default (signed-out) drawer state; upgraded below if a live session exists.
    renderDrawerAuthSignedOut(drawerAuthSlot);
    if (!area) return;

    try {
      var raw = localStorage.getItem('sb-urklkrwevjtlfbwnipjn-auth-token');
      if (!raw) return;
      var session = JSON.parse(raw);
      var user = session && session.user;
      // Expired stored session → keep Sign In / Sign Up (don't render a chip
      // that would 401 on click).
      var expMs = session && session.expires_at ? session.expires_at * 1000 : 0;
      if (!user || (expMs && expMs <= Date.now())) return;

      var firstName = (user.user_metadata && user.user_metadata.first_name) ||
        (user.email && user.email.split('@')[0]) || 'You';

      // Route the chip by advisory role, cached PER USER so a previous
      // account's route can't leak onto a different signed-in user.
      var hrefKey = 'mrb-profile-href:' + user.id;
      var profileHref = '/profile-setup.html';
      try { profileHref = localStorage.getItem(hrefKey) || profileHref; } catch (err) {}

      function paintChip(avatarUrl) {
        var inner = avatarUrl
          ? '<img src="' + esc(avatarUrl) + '" style="width:28px;height:28px;border-radius:50%;object-fit:cover;border:2px solid var(--accent);" alt=""/><span style="color:var(--accent);font-weight:700;font-size:0.82rem;">' + esc(firstName) + '</span>'
          : '👤 ' + esc(firstName);
        var style = avatarUrl
          ? 'display:flex;align-items:center;gap:6px;text-decoration:none;white-space:nowrap;'
          : 'background:var(--accent-soft);color:var(--accent);border:1px solid var(--accent-border);padding:5px 12px;border-radius:999px;font-weight:700;font-size:0.82rem;text-decoration:none;white-space:nowrap;';
        area.innerHTML = '<a id="nav-profile-link" href="' + profileHref + '" style="' + style + '">' + inner + '</a>';
        renderDrawerAuthSignedIn(drawerAuthSlot, profileHref, firstName, avatarUrl);
      }

      paintChip(null);

      // Resolve role → correct profile route (staff vs student). A 401/empty
      // response must NOT overwrite the cached route with the student default.
      fetch(SUPA_URL + '/rest/v1/profiles?id=eq.' + user.id + '&select=role', {
        headers: { 'apikey': SUPA_KEY, 'Authorization': 'Bearer ' + session.access_token }
      }).then(function (r) { return r.ok ? r.json() : null; }).then(function (rows) {
        if (!rows || !rows[0]) return;
        profileHref = (rows[0].role && rows[0].role !== 'student') ? '/teacher-profile.html' : '/profile-setup.html';
        try { localStorage.setItem(hrefKey, profileHref); } catch (err) {}
        var link = document.getElementById('nav-profile-link');
        if (link) link.href = profileHref;
        var dchip = drawerAuthSlot && drawerAuthSlot.querySelector('a');
        if (dchip) dchip.href = profileHref;
      }).catch(function () {});

      // Fetch avatar (best-effort) and upgrade the chip to show it.
      fetch('https://mrbadmus-backend.onrender.com/api/profile', {
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
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    boot();
  }
})();
