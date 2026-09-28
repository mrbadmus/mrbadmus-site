/* shared/teacher-topbar.js — the teacher top bar's phone menu.
 *
 * ⊕ phone-teacher run, 28 Sep 2026 (Mide's screenshot of Today on a phone:
 * the bar wrapped onto two lines — brand + tabs + search on one, the name,
 * Admin and Sign out on a second).
 *
 * At ≤560px the bar is ONE row: the brand, the Today / My classes segment,
 * and a single menu button (≡). Everything else the bar holds on a desktop —
 * the teacher's name, Admin and Flashcard decks (both injected later by
 * shared/teacher-admin-nav.js), Find a student, the theme control and Sign
 * out — is reached through that button. Above 560px nothing changes.
 *
 * ⚠️ THE MENU IS BUILT FROM THE BAR EVERY TIME IT OPENS, NOT FROM A LIST.
 * The bar is not a fixed set of items: teacher-admin-nav.js injects Admin and
 * Flashcard decks after an async capability probe, the Operator tab appears
 * only for an operator, and the name fills in after sign-in. So the phone CSS
 * (shared/teacher-topbar.css) marks what it hides with `--tb-in-menu: 1`, and
 * this file lists, at open time, every link and button the CSS has moved out
 * of sight — and nothing the PAGE itself has hidden (an inline
 * `display:none`, e.g. the Operator tab for a non-operator). Injected items
 * therefore appear in the menu with no coordination, and the injectors keep
 * landing where they always did ("before the bar's last button", Sign out).
 *
 * ⚠️ BUTTONS ARE PROXIED, NOT CLONED. "Find a student" and "Sign out" carry
 * listeners and inline handlers; the menu's entry clicks the real control, so
 * there is exactly one implementation of each.
 *
 * The theme control is the one exception: it is a radio group, not a button,
 * so the menu carries its own `[data-mrb-theme]` slot and shared/theme.js
 * mounts the same control into it (it watches for slots that arrive late).
 */
(function () {
  'use strict';
  var BAR = '[data-port-region="topbar"]';
  var MENU_SVG = '<svg width="20" height="20" viewBox="0 0 20 20" fill="none" ' +
    'aria-hidden="true" focusable="false"><path d="M3 5.5h14M3 10h14M3 14.5h14" ' +
    'stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>';
  var panel = null, openBtn = null;

  function inMenu(el, bar) {
    // Hidden by the PAGE (inline display:none on it or an ancestor inside
    // the bar)? Then it is not ours to show.
    for (var n = el; n && n !== bar; n = n.parentNode) {
      if (n.style && n.style.display === 'none') { return false; }
      if (n.hidden) { return false; }
    }
    for (var m = el; m && m !== bar; m = m.parentNode) {
      if (m.nodeType === 1 &&
          getComputedStyle(m).getPropertyValue('--tb-in-menu').trim() === '1') {
        return true;
      }
    }
    return false;
  }

  function label(el) {
    // The accessible name first: "Find a student" carries a "/" key chip in
    // its text that means nothing in a menu.
    var a = el.getAttribute('aria-label');
    if (a) { return a; }
    return (el.textContent || '').replace(/\s+/g, ' ').trim() ||
      el.getAttribute('title') || '';
  }

  function close(focusBack) {
    if (!panel || panel.hidden) { return; }
    panel.hidden = true;
    if (openBtn) {
      openBtn.setAttribute('aria-expanded', 'false');
      if (focusBack) { openBtn.focus(); }
    }
  }

  function build(bar) {
    var box = panel.querySelector('.tb-menu-items');
    box.textContent = '';
    var name = bar.querySelector('.tb-name, .mrb-teachername');
    if (name && (name.textContent || '').trim() && inMenu(name, bar)) {
      var who = document.createElement('div');
      who.className = 'tb-menu-name';
      var nm = document.createElement('span');
      nm.className = 'tb-menu-who';
      nm.textContent = name.textContent.trim();
      who.appendChild(nm);
      box.appendChild(who);
    }
    // The environment badge (TEST / LOCAL) is a warning, not chrome: when
    // the bar shows one, the menu repeats it beside the name so a teacher on
    // a phone still sees they are not on the live school's data.
    var envs = bar.querySelectorAll(':scope > span');
    for (var e = 0; e < envs.length; e++) {
      var tx = (envs[e].textContent || '').trim();
      if (/^[A-Z]{2,8}$/.test(tx) && inMenu(envs[e], bar)) {
        var pill = document.createElement('span');
        pill.className = 'tb-menu-env';
        pill.textContent = tx;
        var host = box.querySelector('.tb-menu-name');
        if (!host) {
          host = document.createElement('div');
          host.className = 'tb-menu-name';
          box.appendChild(host);
        }
        host.appendChild(pill);
        break;
      }
    }
    var signout = null, rest = [];
    var els = bar.querySelectorAll('a, button');
    for (var i = 0; i < els.length; i++) {
      var el = els[i];
      if (el.classList.contains('tb-menu') || el.closest('.mrb-brand')) { continue; }
      if (el.closest('[data-mrb-theme]')) { continue; }
      if (!inMenu(el, bar)) { continue; }
      if (el.tagName === 'BUTTON' && /^sign out$/i.test(label(el))) { signout = el; continue; }
      rest.push(el);
    }
    rest.forEach(function (el) { if (label(el)) { box.appendChild(item(el)); } });
    var slot = bar.querySelector('[data-mrb-theme]');
    if (slot && inMenu(slot, bar)) {
      var row = document.createElement('div');
      row.className = 'tb-menu-theme';
      var lab = document.createElement('span');
      lab.textContent = 'Theme';
      row.appendChild(lab);
      var s = document.createElement('span');
      s.setAttribute('data-mrb-theme', '');
      row.appendChild(s);
      box.appendChild(row);
      if (window.MRBTheme && typeof window.MRBTheme.mount === 'function') {
        try { window.MRBTheme.mount(); } catch (e) { /* theme.js observes */ }
      }
    }
    if (signout) { box.appendChild(item(signout)); }
  }

  function item(el) {
    var it;
    if (el.tagName === 'A') {
      it = document.createElement('a');
      it.href = el.getAttribute('href') || '#';
    } else {
      it = document.createElement('button');
      it.type = 'button';
      it.addEventListener('click', function () { close(false); el.click(); });
    }
    it.className = 'tb-menu-item';
    it.textContent = label(el);
    return it;
  }

  /* The hand-written pages carry the button in their markup. The six
     generated screens are drawn by shared/student-runtime.js, whose draw()
     empties the mount host and rebuilds the whole bar on every setState — so
     the button is injected here and re-injected by the observer below after
     every redraw (teacher-admin-nav.js does the same for Admin).

     ⚠️ APPENDED AT THE END OF THE BAR, NOT AFTER THE TABS. draw() restores
     focus to the element at the same child position it had before the
     redraw; a node inserted in the MIDDLE of the bar shifts every later
     sibling by one, so closing the search overlay put focus on the wrong
     control (focus_audit's teacher_pupil_reach caught it). At the end it
     shifts nothing. On a phone every sibling between the tabs and it is
     hidden, so it still sits at the right-hand edge. teacher-admin-nav.js
     skips `.tb-menu` when it looks for "the bar's last button". */
  function inject(bar) {
    var tabs = bar.querySelector(':scope > .tb-seg, :scope > [data-tb-keep="tabs"]');
    if (!tabs) { return null; }
    var b = document.createElement('button');
    b.type = 'button';
    b.className = 'tb-menu';
    b.setAttribute('aria-label', 'Menu');
    b.setAttribute('data-tb-menu', '1');
    b.innerHTML = MENU_SVG;
    bar.appendChild(b);
    return b;
  }

  function ensure(bar) {
    var btn = bar.querySelector('.tb-menu') || inject(bar);
    if (!btn) { return; }
    openBtn = btn;
    if (!panel) {
      panel = document.createElement('div');
      panel.className = 'tb-menu-panel noprint';
      panel.id = 'tb-menu-panel';
      panel.hidden = true;
      panel.setAttribute('role', 'dialog');
      panel.setAttribute('aria-label', 'Menu');
      panel.innerHTML = '<div class="tb-menu-items"></div>';
      document.body.appendChild(panel);
      panel.addEventListener('keydown', function (e) {
        if (e.key === 'Escape') { e.stopPropagation(); close(true); }
      });
      document.addEventListener('click', function (e) {
        if (panel.hidden) { return; }
        if (panel.contains(e.target) || (openBtn && openBtn.contains(e.target))) { return; }
        close(false);
      });
      window.addEventListener('resize', function () {
        if (!panel.hidden && window.innerWidth > 560) { close(false); }
      });
    }
    if (btn.getAttribute('data-tb-wired') === '1') { return; }
    btn.setAttribute('data-tb-wired', '1');
    btn.setAttribute('aria-controls', 'tb-menu-panel');
    btn.setAttribute('aria-expanded', 'false');
    btn.addEventListener('click', function () {
      if (!panel.hidden) { close(true); return; }
      build(bar);
      var r = bar.getBoundingClientRect();
      panel.style.top = Math.round(r.bottom + 6) + 'px';
      panel.hidden = false;
      btn.setAttribute('aria-expanded', 'true');
      var first = panel.querySelector('a, button, input');
      if (first) { first.focus(); }
    });
  }

  function init() {
    var bar = document.querySelector(BAR);
    if (bar) { ensure(bar); }
    if (!window.MutationObserver || init.watching) { return; }
    init.watching = true;
    var queued = false;
    new MutationObserver(function () {
      if (queued) { return; }
      queued = true;
      (window.requestAnimationFrame || window.setTimeout)(function () {
        queued = false;
        var b = document.querySelector(BAR);
        if (!b) { return; }
        // A redraw replaced the bar under an open menu: its items now point
        // at detached controls, so close it rather than leave it stale.
        if (panel && !panel.hidden && openBtn && !b.contains(openBtn)) { close(false); }
        ensure(b);
      });
    }).observe(document.body, { childList: true, subtree: true });
  }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else { init(); }
  window.MrBadmusTopbarMenu = { close: close };
})();
