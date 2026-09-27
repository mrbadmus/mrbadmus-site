/* shared/theme.js — the site's ONE Light / Dark / System control (theme run,
   Mide's ruling 26 Sep 2026: "the mode should automatically be on light mode,
   and then users can toggle to dark. Allow the light, dark, system mode options
   for every page on the website.")

   How a page themes itself, end to end:
   1. The inline pre-paint snippet in <head> (THEME_HEAD in theme_head.py — the
      same bytes on every page) reads localStorage 'mrb-theme' and writes
      <html data-theme="light|dark" data-theme-pref="light|dark|system"> before
      first paint. Light is the default and the fallback for anything unreadable.
   2. Every family's stylesheet keys its dark tokens on html[data-theme="dark"].
      Because data-theme is ALWAYS written, the older prefers-color-scheme blocks
      (which stand down under data-theme="light") never fire on their own.
   3. This file mounts the control into every [data-mrb-theme] slot a generator
      emitted, persists the choice, follows the device live under System, and
      keeps other open tabs in step.

   Storage: localStorage only. profiles has no suitable column on production;
   the migration that adds one (profiles.colour_scheme) is parked — see
   docs/theme/REPORT.md. Every storage access is wrapped: a private window or
   blocked storage leaves the page in light and the control still works for the
   life of the page. */
(function () {
  'use strict';
  if (window.MRBTheme) return;

  var KEY = 'mrb-theme';
  var PREFS = ['light', 'dark', 'system'];
  var root = document.documentElement;
  var mq = window.matchMedia ? window.matchMedia('(prefers-color-scheme: dark)') : null;
  var memory = null;           // the choice when storage is unavailable
  var listeners = [];

  function clean(p) { return PREFS.indexOf(p) >= 0 ? p : 'light'; }

  function read() {
    try { var v = window.localStorage.getItem(KEY); if (v) return clean(v); } catch (e) {}
    return memory ? memory : 'light';
  }

  function write(p) {
    memory = p;
    try { window.localStorage.setItem(KEY, p); } catch (e) {}
  }

  function resolve(p) {
    if (p === 'dark') return 'dark';
    if (p === 'system') return mq && mq.matches ? 'dark' : 'light';
    return 'light';
  }

  function apply(p) {
    var mode = resolve(p);
    root.setAttribute('data-theme', mode);
    root.setAttribute('data-theme-pref', p);
    root.style.colorScheme = mode;
    syncControls(p);
    for (var i = 0; i < listeners.length; i++) {
      try { listeners[i](mode, p); } catch (e) {}
    }
  }

  /* ── the control ───────────────────────────────────────────────────────
     A radio group of three, so the keyboard contract is the browser's own:
     Tab lands on the chosen option, the arrow keys move and choose, and a
     screen reader announces "Colour theme, Light, radio button, 1 of 3".
     Icons carry the visible meaning; each option's text is visually hidden
     but read out, and repeated in the title for pointer users. */
  var ICONS = {
    light: '<svg viewBox="0 0 20 20" width="16" height="16" aria-hidden="true" focusable="false"><circle cx="10" cy="10" r="3.6" fill="none" stroke="currentColor" stroke-width="1.8"/><g stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M10 1.8v2.1M10 16.1v2.1M1.8 10h2.1M16.1 10h2.1M4.2 4.2l1.5 1.5M14.3 14.3l1.5 1.5M4.2 15.8l1.5-1.5M14.3 5.7l1.5-1.5"/></g></svg>',
    dark: '<svg viewBox="0 0 20 20" width="16" height="16" aria-hidden="true" focusable="false"><path d="M15.8 12.6A6.6 6.6 0 0 1 7.4 4.2a6.6 6.6 0 1 0 8.4 8.4z" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg>',
    system: '<svg viewBox="0 0 20 20" width="16" height="16" aria-hidden="true" focusable="false"><rect x="2.4" y="3.4" width="15.2" height="10.2" rx="1.6" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M7 17h6M10 13.8V17" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>'
  };
  var LABELS = { light: 'Light', dark: 'Dark', system: 'System' };
  var TITLES = { light: 'Light theme', dark: 'Dark theme', system: 'Match this device' };
  var uid = 0;

  /* Scoped to the control's own class, and every colour is currentColor or a
     translucent mix of it, so the control sits in a light header, a dark
     header, a cream band or a teacher bar without per-family styling. The
     focus ring is the page's own if it has one (--mrb-focus), else the
     accent orange at a width that clears 3:1 on both grounds. */
  var CSS = [
    '.mrb-theme{display:inline-flex;align-items:center;flex:none;margin:0;padding:2px;border:1px solid color-mix(in srgb,currentColor 28%,transparent);border-radius:999px;min-width:0;line-height:1;vertical-align:middle;font:inherit}',
    '.mrb-theme legend{position:absolute;width:1px;height:1px;margin:-1px;padding:0;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap;border:0}',
    '.mrb-theme label{position:relative;display:inline-flex;align-items:center;justify-content:center;width:30px;height:28px;border-radius:999px;cursor:pointer;color:inherit;opacity:.72;transition:background-color .15s,opacity .15s}',
    '.mrb-theme label:hover{opacity:1;background:color-mix(in srgb,currentColor 10%,transparent)}',
    '.mrb-theme input{position:absolute;inset:0;width:100%;height:100%;margin:0;opacity:0;cursor:pointer}',
    '.mrb-theme input:checked+svg{opacity:1}',
    '.mrb-theme label:has(input:checked){opacity:1;background:color-mix(in srgb,currentColor 16%,transparent)}',
    '.mrb-theme label:has(input:focus-visible){outline:3px solid var(--mrb-focus,#E4572E);outline-offset:1px}',
    '.mrb-theme .mrb-theme-sr{position:absolute;width:1px;height:1px;margin:-1px;padding:0;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap;border:0}',
    '.mrb-theme svg{display:block;pointer-events:none}',
    '@media (forced-colors:active){.mrb-theme label:has(input:checked){outline:2px solid CanvasText}}',
    '@media print{.mrb-theme{display:none!important}}'
  ].join('');

  function injectCss() {
    if (document.getElementById('mrb-theme-css')) return;
    var s = document.createElement('style');
    s.id = 'mrb-theme-css';
    s.textContent = CSS;
    (document.head || root).appendChild(s);
  }

  function build(slot) {
    /* A renderer that patches in place can empty the slot but keep the
       element (and this flag) — the KS4 pilot runtime did. Trust the control
       being present, not the flag. */
    if (slot.getAttribute('data-mrb-theme-ready') === '1' && slot.querySelector('.mrb-theme')) return;
    slot.setAttribute('data-mrb-theme-ready', '1');
    var name = 'mrb-theme-' + (++uid);
    var fs = document.createElement('fieldset');
    fs.className = 'mrb-theme';
    var html = '<legend>Colour theme</legend>';
    for (var i = 0; i < PREFS.length; i++) {
      var p = PREFS[i];
      html += '<label title="' + TITLES[p] + '"><input type="radio" name="' + name +
        '" value="' + p + '">' + ICONS[p] + '<span class="mrb-theme-sr">' + LABELS[p] + '</span></label>';
    }
    fs.innerHTML = html;
    fs.addEventListener('change', function (e) {
      var t = e.target;
      if (t && t.name === name) set(t.value);
    });
    slot.appendChild(fs);
  }

  function syncControls(p) {
    var inputs = document.querySelectorAll('.mrb-theme input');
    for (var i = 0; i < inputs.length; i++) inputs[i].checked = inputs[i].value === p;
  }

  function mountAll() {
    var slots = document.querySelectorAll('[data-mrb-theme]');
    if (slots.length) injectCss();
    for (var i = 0; i < slots.length; i++) build(slots[i]);
    syncControls(read());
  }

  function set(p) {
    p = clean(p);
    write(p);
    apply(p);
  }

  /* System follows the device live; the other two ignore it. */
  if (mq) {
    var onDevice = function () { if (read() === 'system') apply('system'); };
    if (mq.addEventListener) mq.addEventListener('change', onDevice);
    else if (mq.addListener) mq.addListener(onDevice);
  }

  /* Another tab changed the choice: follow it. */
  window.addEventListener('storage', function (e) {
    if (e.key === KEY) apply(read());
  });

  /* A page restored from the back/forward cache kept its old attributes. */
  window.addEventListener('pageshow', function (e) {
    if (e.persisted) apply(read());
  });

  window.MRBTheme = {
    get: read,
    mode: function () { return resolve(read()); },
    set: set,
    mount: mountAll,
    onChange: function (fn) { if (typeof fn === 'function') listeners.push(fn); }
  };

  /* The head snippet already painted the right theme; re-apply once so a page
     that lacks the snippet (or ran it before storage was readable) converges. */
  apply(read());
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', mountAll);
  else mountAll();
  /* Generated runtimes (student, teacher, KS4 pilot) redraw their header after
     load; watch for a slot that arrives later. */
  if (window.MutationObserver) {
    var queued = false;
    var check = function () {
      queued = false;
      var slots = document.querySelectorAll('[data-mrb-theme]');
      for (var i = 0; i < slots.length; i++) {
        if (!slots[i].querySelector('.mrb-theme')) { mountAll(); return; }
      }
    };
    new MutationObserver(function () {
      if (queued) return;
      queued = true;
      (window.requestAnimationFrame || setTimeout)(check);
    }).observe(root, { childList: true, subtree: true });
  }
})();
