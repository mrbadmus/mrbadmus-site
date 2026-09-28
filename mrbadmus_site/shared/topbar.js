/* shared/topbar.js — the right-hand group of the ONE pupil top bar.

   Stage B of the phone run (28 Sep 2026). The bar's markup comes from
   topbar.py; this file fills its "who" slot — the part that depends on who
   is looking:

     signed out   → "Sign in"  (not on kind="student": the page's guard owns
                                signed-out there and will redirect)
     signed in    → the bell (pupils only), then the avatar and its menu:
                    My class · Settings · Sign out

   Load AFTER config.js, class-entry.js, student-bell.js and theme.js. All
   four are optional in the sense that a missing one degrades to less, never
   to a broken bar.

   THE SLOT CONTRACT (so the class and assignment pages can adopt the bar):

     <span class="mrb-topbar__who" data-mrb-topbar-who="…"></span>
        ""  or "all"  → bell + avatar (or Sign in)
        "avatar"      → avatar only; the page mounts its own bell
     No slot at all   → this file does nothing on that bar. The class page,
                        whose end group already carries Design's bell host and
                        avatar, simply has no slot.

   Generated runtimes (the KS4 pilot, the student pages) can redraw the bar
   after load; the slot is re-filled from a cached answer on every redraw
   (MutationObserver, plus `MRBTopbar.hydrate()` for __MRB_AFTER_DRAW__). */
(function () {
  'use strict';
  if (window.MRBTopbar) { return; }

  var SLOT = '[data-mrb-topbar-who]';
  var OWN = 'data-mrb-topbar-own';
  var answer = null;      // {entry, who} once resolved
  var asking = null;
  var uid = 0;

  function q(name) {
    try { return new URLSearchParams(window.location.search).get(name); }
    catch (e) { return null; }
  }

  /* `env` and `api` travel, so a tester on TEST stays on TEST. */
  function carry(href) {
    var keep = [];
    ['env', 'api'].forEach(function (k) {
      var v = q(k);
      if (v && href.indexOf(k + '=') < 0) { keep.push(k + '=' + encodeURIComponent(v)); }
    });
    if (!keep.length) { return href; }
    return href + (href.indexOf('?') < 0 ? '?' : '&') + keep.join('&');
  }

  function here(href) {
    return window.location.pathname === String(href).split('?')[0];
  }

  function bar(slot) { return slot.closest('[data-mrb-topbar]'); }

  function ask() {
    if (answer) { return Promise.resolve(answer); }
    if (asking) { return asking; }
    var ce = window.MRBClassEntry;
    if (!ce || !ce.viewer) { answer = { entry: null, who: null }; return Promise.resolve(answer); }
    asking = Promise.all([ce.viewer(), ce.resolve()]).then(function (r) {
      answer = { who: r[0], entry: r[0] ? r[1] : null };
      return answer;
    }).catch(function () {
      answer = { entry: null, who: null };
      return answer;
    });
    return asking;
  }

  function signOut() {
    var g = window.MrBadmusStudentGuard;
    if (g && typeof g.signOut === 'function') { g.signOut(); return; }
    try { if (window.MRBClassEntry) { window.MRBClassEntry.dropCaches(); } } catch (e) {}
    try {
      var c = window.MrBadmusConfig || {};
      var m = /^https?:\/\/([^.]+)\./.exec(c.SUPABASE_URL || 'https://urklkrwevjtlfbwnipjn.supabase.co');
      if (m) { localStorage.removeItem('sb-' + m[1] + '-auth-token'); }
    } catch (e) {}
    window.location.replace(carry('/auth.html'));
  }

  function el(tag, cls, text) {
    var n = document.createElement(tag);
    if (cls) { n.className = cls; }
    if (text != null) { n.textContent = text; }
    n.setAttribute(OWN, '1');
    return n;
  }

  function closeAll(except) {
    var open = document.querySelectorAll('.mrb-topbar__avatar[aria-expanded="true"]');
    for (var i = 0; i < open.length; i++) {
      if (open[i] === except) { continue; }
      open[i].setAttribute('aria-expanded', 'false');
      var m = document.getElementById(open[i].getAttribute('aria-controls'));
      if (m) { m.hidden = true; }
    }
  }

  function avatar(slot, a) {
    var id = 'mrb-topbar-menu-' + (++uid);
    var btn = el('button', 'mrb-topbar__avatar');
    btn.type = 'button';
    btn.setAttribute('aria-expanded', 'false');
    btn.setAttribute('aria-controls', id);
    btn.setAttribute('aria-label', 'Account menu');
    btn.appendChild(el('span', 'mrb-topbar__initials', a.who.initials || '?'))
       .setAttribute('aria-hidden', 'true');

    var menu = el('div', 'mrb-topbar__menu');
    menu.id = id;
    menu.hidden = true;
    var entry = a.entry;
    if (entry && !here(entry.href)) {
      var go = el('a', '', entry.label);
      go.href = carry(entry.href);
      menu.appendChild(go);
    }
    var pupil = entry && entry.href.indexOf('/student/') === 0;
    if (pupil && !here('/student/settings.html')) {
      var st = el('a', '', 'Settings');
      st.href = carry('/student/settings.html');
      menu.appendChild(st);
    }
    var out = el('button', '', 'Sign out');
    out.type = 'button';
    out.setAttribute('data-mrb-topbar-signout', '1');
    out.addEventListener('click', signOut);
    menu.appendChild(out);

    btn.addEventListener('click', function (ev) {
      ev.stopPropagation();
      var open = btn.getAttribute('aria-expanded') !== 'true';
      closeAll(btn);
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
      menu.hidden = !open;
      if (open) {
        var first = menu.querySelector('a,button');
        if (first) { first.focus(); }
      }
    });
    menu.addEventListener('keydown', function (ev) {
      if (ev.key === 'Escape') {
        btn.setAttribute('aria-expanded', 'false');
        menu.hidden = true;
        btn.focus();
        ev.stopPropagation();
      }
    });
    slot.appendChild(btn);
    slot.appendChild(menu);
  }

  function fill(slot, a) {
    var mode = slot.getAttribute('data-mrb-topbar-who') || 'all';
    var b = bar(slot);
    var kind = (b && b.getAttribute('data-mrb-topbar')) || '';
    if (!a.who) {
      if (kind === 'student') { return; }
      var s = el('a', 'mrb-topbar__signin', 'Sign in');
      s.href = carry('/auth.html?tab=signin&return=' +
                     encodeURIComponent(window.location.pathname + window.location.search));
      slot.appendChild(s);
      return;
    }
    var pupil = a.entry && a.entry.href.indexOf('/student/') === 0;
    if (mode === 'all' && pupil && window.MrBadmusBell) {
      var tone = (b && b.getAttribute('data-mrb-bell-tone')) || 'chrome';
      if (!slot.__mrbBell) {
        slot.__mrbBell = true;
        window.MrBadmusBell.mount({
          host: function () { return document.querySelector(SLOT + ':not([data-mrb-topbar-who="avatar"])'); },
          place: 'first',
          tone: tone
        });
      } else {
        window.MrBadmusBell.attach();
      }
    }
    avatar(slot, a);
  }

  function filled(slot) {
    for (var i = 0; i < slot.children.length; i++) {
      if (slot.children[i].hasAttribute(OWN)) { return true; }
    }
    return false;
  }

  function hydrate() {
    var slots = document.querySelectorAll(SLOT);
    if (!slots.length) { return; }
    ask().then(function (a) {
      for (var i = 0; i < slots.length; i++) {
        if (!slots[i].isConnected) { continue; }
        if (filled(slots[i])) {
          if (slots[i].__mrbBell && window.MrBadmusBell) { window.MrBadmusBell.attach(); }
          continue;
        }
        fill(slots[i], a);
      }
    });
  }

  document.addEventListener('click', function (ev) {
    var t = ev.target;
    if (t && t.closest && t.closest('.mrb-topbar__menu')) { return; }
    closeAll(null);
  });

  window.MRBTopbar = { hydrate: hydrate, signOut: signOut };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', hydrate);
  } else {
    hydrate();
  }
  /* A runtime that redraws the bar after load gets its slot re-filled. */
  if (window.MutationObserver) {
    var queued = false;
    new MutationObserver(function () {
      if (queued) { return; }
      queued = true;
      (window.requestAnimationFrame || setTimeout)(function () {
        queued = false;
        var slots = document.querySelectorAll(SLOT);
        for (var i = 0; i < slots.length; i++) {
          if (!filled(slots[i]) || (slots[i].__mrbBell && !slots[i].querySelector('[data-mrb-bell]'))) {
            hydrate();
            return;
          }
        }
      });
    }).observe(document.documentElement, { childList: true, subtree: true });
  }
})();
