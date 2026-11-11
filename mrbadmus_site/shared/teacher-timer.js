/* shared/teacher-timer.js — a classroom timer, for the front of a room.

   `window.MrBadmusTimer = {open(opts), close(), isOpen(), onChange(fn)}`.
   `opts.view` is 'full' (the default) or 'float'.

   ══ WHAT IT IS ═════════════════════════════════════════════════════════

   A countdown (30 s, 1, 2, 3, 5, 10 min, or a custom minutes + seconds) and
   a stopwatch, in two views of ONE running timer:

   · FULL — an opaque, full-viewport display with digits sized for the back
     of a projected classroom (`min(32vw, 56vh)`, tabular numerals).
   · FLOAT — a small card fixed in the bottom-right corner, over the page and
     over the name picker, so a timer can run while names are being picked.

   ══ WHAT IT WRITES — NOTHING ═══════════════════════════════════════════

   ⛔ No storage of any kind, no cookie, no `fetch`, no Supabase, no audio
   file. The countdown's end sound is two short Web Audio oscillator beeps
   made in the page. Everything lives in this closure (`S`), including the
   mute toggle, and goes with the page load.

   ══ WHERE IT MOUNTS, AND WHY ═══════════════════════════════════════════

   ⚠️ ON `document.body`, NEVER INTO `#mrb-teacher`. The generated teacher
   pages are drawn by `student-runtime`, whose `draw()` empties the mount
   host on every `setState` — a timer inside it would be wiped by the very
   page the teacher is using while it runs. On `document.body` it is a
   sibling of the host (as the Set work sheet and the breakdown panel are),
   z-index 100, above the picker's 90.

   The same placement keeps a ticking display out of the host's text. The
   drive gates decide whether a press "did something" by comparing the
   host's text; a clock that changes every second inside it would make dead
   controls look alive. `teacher_behaviour.py` instead reads this module's
   `data-tm` overlay the way it reads the Set work sheet's: view and open
   count, never the reading.

   ══ KEYBOARD ═══════════════════════════════════════════════════════════

   · Space starts / pauses when the FULL view is open, or when focus is
     inside the FLOAT. It is never taken anywhere else, and never from a
     text field: the teacher may be typing or pressing a button.
   · Escape closes the FULL view — to the float if the timer has been
     started (so a running countdown is not lost), outright if it has not.
     It is handled in the window's CAPTURE phase and stopped there, so the
     same keypress never reaches the picker's own Escape handler beneath.

   ══ SCREEN READERS ═════════════════════════════════════════════════════

   The big digits are `aria-hidden`: a live region that changed every second
   would be unusable. A separate visually-hidden `role="status"` region says
   the time on start, pause and finish, and at most once a minute in between.
*/
(function () {
  'use strict';

  var Z = 100;                       // above the picker's overlay (90)
  var WARN_MS = 10000;               // the last ten seconds

  /* ── all state, in this closure ─────────────────────────────────────── */
  var S = {
    mode: 'down',                    // 'down' | 'up'
    preset: 300000,                  // the countdown's length, ms
    status: 'idle',                  // idle | running | paused | done
    ms: 300000,                      // stored reading while not running
    endAt: 0,                        // countdown: when it reaches zero
    t0: 0, base: 0,                  // stopwatch: when it started / its base
    muted: false,
    beeps: 0
  };
  var view = null;                   // null | 'full' | 'float'
  var root = null, body = null, liveNode = null, digitsNode = null;
  var ticker = null, opens = 0, prevFocus = null, audio = null;
  var lastSaid = null;               // the minute last announced
  var listeners = [];

  function now() {
    return (window.performance && performance.now) ? performance.now()
                                                   : Date.now();
  }

  // ── time ───────────────────────────────────────────────────────────────

  function cur() {
    if (S.status !== 'running') { return S.ms; }
    return S.mode === 'down' ? Math.max(0, S.endAt - now())
                             : S.base + (now() - S.t0);
  }

  /* The reading, as a person says it. A countdown rounds UP (0:10 is shown
     until the last tenth is gone, then 0:09), a stopwatch rounds down. */
  function secs(ms) {
    return S.mode === 'down' ? Math.ceil(ms / 1000) : Math.floor(ms / 1000);
  }
  function two(n) { return (n < 10 ? '0' : '') + n; }
  function fmt(ms) {
    var t = secs(ms), h = Math.floor(t / 3600), m = Math.floor((t % 3600) / 60);
    return h ? h + ':' + two(m) + ':' + two(t % 60)
             : Math.floor(t / 60) + ':' + two(t % 60);
  }
  function words(ms) {
    var t = secs(ms), m = Math.floor(t / 60), s = t % 60, out = [];
    if (m) { out.push(m + (m === 1 ? ' minute' : ' minutes')); }
    if (s || !m) { out.push(s + (s === 1 ? ' second' : ' seconds')); }
    return out.join(' ');
  }

  /* idle | running | paused | warn | done — `warn` is a countdown in its
     last ten seconds, running or paused. */
  function stateName() {
    if (S.status === 'done') { return 'done'; }
    if (S.mode === 'down' && (S.status === 'running' || S.status === 'paused') &&
        cur() <= WARN_MS) { return 'warn'; }
    return S.status;
  }

  // ── sound: two beeps in the page, no file, no network ──────────────────

  function ensureAudio() {
    try {
      if (!audio) {
        var C = window.AudioContext || window.webkitAudioContext;
        if (C) { audio = new C(); }
      }
      if (audio && audio.state === 'suspended' && audio.resume) { audio.resume(); }
    } catch (e) { audio = null; }
  }

  function beep() {
    if (S.muted) { return; }
    ensureAudio();
    if (!audio) { return; }
    S.beeps += 1;
    try {
      var t0 = audio.currentTime + 0.05;
      for (var i = 0; i < 6; i++) {
        var o = audio.createOscillator(), g = audio.createGain();
        o.type = 'sine';
        o.frequency.value = i % 2 ? 660 : 880;
        var a = t0 + i * 0.42;
        g.gain.setValueAtTime(0.0001, a);
        g.gain.exponentialRampToValueAtTime(0.35, a + 0.02);
        g.gain.exponentialRampToValueAtTime(0.0001, a + 0.34);
        o.connect(g); g.connect(audio.destination);
        o.start(a); o.stop(a + 0.36);
      }
    } catch (e) { /* no sound is better than no timer */ }
  }

  // ── announcements ──────────────────────────────────────────────────────

  function say(msg) { if (liveNode) { liveNode.textContent = msg; } }

  // ── the clock ──────────────────────────────────────────────────────────

  function stopTick() { if (ticker) { clearInterval(ticker); ticker = null; } }
  function startTick() { stopTick(); ticker = setInterval(tick, 200); }

  function tick() {
    if (S.status !== 'running') { return; }
    var ms = cur();
    if (S.mode === 'down' && ms <= 0) { finish(); return; }
    paint();
    /* At most once a minute: when the whole-minute figure changes. */
    var m = Math.floor(secs(ms) / 60);
    if (m >= 1 && lastSaid !== null && m !== lastSaid) {
      lastSaid = m;
      say(words(ms) + (S.mode === 'down' ? ' left' : ''));
    }
  }

  function finish() {
    stopTick();
    S.status = 'done'; S.ms = 0;
    say("Time's up");
    beep();
    render();
    notify();
  }

  function start() {
    if (S.status === 'running') { return; }
    if (S.status === 'done') { reset(true); }
    if (S.mode === 'down' && S.ms <= 0) { return; }
    ensureAudio();
    if (S.mode === 'down') { S.endAt = now() + S.ms; }
    else { S.t0 = now(); S.base = S.ms; }
    S.status = 'running';
    lastSaid = Math.floor(secs(S.ms) / 60);
    say((S.mode === 'down' ? 'Timer started, ' : 'Stopwatch started, ') +
        words(S.ms));
    startTick(); render(); notify();
  }

  function pause() {
    if (S.status !== 'running') { return; }
    S.ms = cur(); S.status = 'paused'; stopTick();
    say('Paused, ' + words(S.ms) + (S.mode === 'down' ? ' left' : ''));
    render(); notify();
  }

  function toggle() {
    if (S.status === 'running') { pause(); } else { start(); }
  }

  function reset(quiet) {
    stopTick();
    S.status = 'idle';
    S.ms = S.mode === 'down' ? S.preset : 0;
    lastSaid = null;
    if (!quiet) { say('Reset, ' + words(S.ms)); }
    render(); notify();
  }

  function atStart() {
    return S.status === 'idle' && S.ms === (S.mode === 'down' ? S.preset : 0);
  }

  function addTime(delta) {
    if (S.mode !== 'down') { return; }
    if (S.status === 'running') { S.endAt += delta; }
    else if (S.status === 'paused') { S.ms += delta; }
    else { return; }
    lastSaid = Math.floor(secs(cur()) / 60);
    say(words(cur()) + ' left');
    render(); notify();
  }

  function setPreset(ms) {
    S.preset = ms;
    reset(true);
    say(words(ms));
  }

  function setMode(m) {
    if (S.mode === m) { return; }
    S.mode = m;
    reset(true);
    say(m === 'down' ? 'Countdown' : 'Stopwatch');
  }

  // ── styles — `--st-*` tokens only, like the picker ─────────────────────

  var FULL = 'position:fixed;inset:0;z-index:' + Z + ';background:var(--st-ground);' +
             'display:flex;flex-direction:column;overflow:auto;' +
             'color:var(--st-ink)';
  var FLOAT = 'position:fixed;right:12px;bottom:12px;z-index:' + Z + ';' +
              'width:min(340px,calc(100vw - 24px));box-sizing:border-box;' +
              'max-height:calc(100vh - 24px);overflow:auto;padding:12px;' +
              'background:var(--st-paper);color:var(--st-ink);' +
              'border:1px solid var(--st-edge);border-radius:14px;' +
              'box-shadow:var(--st-shadow-frame);display:flex;' +
              'flex-direction:column;gap:10px';
  var SR = 'position:absolute;width:1px;height:1px;margin:-1px;padding:0;' +
           'overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap;border:0';

  var BAR = 'flex:none;display:flex;align-items:center;gap:10px;' +
            'justify-content:space-between;padding:14px 20px;' +
            'border-bottom:1px solid var(--st-rule)';
  var BAR_FLOAT = 'display:flex;align-items:center;gap:8px;' +
                  'justify-content:space-between';
  var ICON_BTN = 'flex:none;width:40px;height:40px;display:flex;' +
                 'align-items:center;justify-content:center;' +
                 'background:transparent;border:1px solid var(--st-btn-border);' +
                 'border-radius:9px;cursor:pointer;color:var(--st-muted)';
  var ICON_ON = ICON_BTN.replace('background:transparent',
                                 'background:var(--st-seg-bg)')
                        .replace('color:var(--st-muted)', 'color:var(--st-ink)');
  var SEG = 'display:flex;gap:3px;padding:3px;background:var(--st-seg-bg);' +
            'border-radius:10px';
  var SEG_ON = 'min-height:40px;padding:0 14px;font:600 15px/1.2 var(--st-ui);' +
               'color:var(--st-ink);background:var(--st-paper);border:none;' +
               'border-radius:8px;cursor:pointer';
  var SEG_OFF = 'min-height:40px;padding:0 14px;font:600 15px/1.2 var(--st-ui);' +
                'color:var(--st-caption);background:transparent;border:none;' +
                'border-radius:8px;cursor:pointer';
  var MID = 'flex:1;min-height:0;display:flex;flex-direction:column;' +
            'align-items:center;justify-content:center;gap:28px;' +
            'padding:24px 20px;text-align:center';
  var ROWS = 'display:flex;flex-wrap:wrap;align-items:center;' +
             'justify-content:center;gap:12px';

  function btnStyle(kind, big) {
    var h = big ? 60 : 44, f = big ? '600 22px/1.2' : '600 16px/1.2';
    var base = 'flex:none;min-height:' + h + 'px;padding:0 ' + (big ? 34 : 18) +
               'px;font:' + f + ' var(--st-ui);display:inline-flex;' +
               'align-items:center;justify-content:center;gap:10px;' +
               'border-radius:11px;cursor:pointer;';
    if (kind === 'primary') {
      return base + 'color:var(--st-paper);background:var(--st-accent-text);' +
             'border:none';
    }
    if (kind === 'off') {
      return base + 'color:var(--st-caption);background:var(--st-paper);' +
             'border:1px solid var(--st-btn-border);cursor:not-allowed';
    }
    return base + 'color:var(--st-ink);background:var(--st-paper);' +
           'border:1px solid var(--st-btn-border)';
  }
  function chipStyle(on) {
    var f = view === 'float';
    return 'min-height:' + (f ? 40 : 44) + 'px;padding:0 ' + (f ? 12 : 16) +
           'px;font:600 ' + (f ? 15 : 16) + 'px/1.2 var(--st-ui);' +
           'border-radius:10px;cursor:pointer;color:var(--st-ink);' +
           'background:' + (on ? 'var(--st-seg-bg)' : 'var(--st-paper)') + ';' +
           'border:1px solid ' + (on ? 'var(--st-rule-strong)'
                                     : 'var(--st-btn-border)');
  }

  /* Digits. Full: the biggest that fits a 5-character reading across the
     viewport width or its height, whichever is smaller. Longer readings (an
     hour or more) take the smaller size. Tabular numerals, so the reading
     never jitters as digits change (measured: every 4-character reading is
     the same width in Instrument Sans). Not the mono face: DM Mono's zero is
     slashed, which on a projector reads as a different character. */
  function digitStyle(len) {
    var size = view === 'full'
      ? (len > 5 ? 'clamp(56px,min(22vw,42vh),460px)'
                 : 'clamp(72px,min(32vw,56vh),640px)')
      : (len > 5 ? 'clamp(30px,9vw,40px)' : 'clamp(40px,12vw,56px)');
    return 'font:600 ' + size + '/1 var(--st-ui);' +
           'font-variant-numeric:tabular-nums;letter-spacing:-.02em;' +
           'text-align:center;white-space:nowrap;margin:0 auto';
  }

  // ── icons: the close X's recipe, aria-hidden, stroke = currentColor ────

  function svg(inner, w) {
    return '<svg width="' + (w || 18) + '" height="' + (w || 18) +
           '" viewBox="0 0 16 16" fill="none" aria-hidden="true" ' +
           'stroke="currentColor" stroke-width="1.6" stroke-linecap="round" ' +
           'stroke-linejoin="round">' + inner + '</svg>';
  }
  var ICONS = {
    play: svg('<path d="M5 3.2v9.6L13 8z"/>'),
    pause: svg('<path d="M5.5 3.5v9M10.5 3.5v9"/>'),
    reset: svg('<path d="M2.6 8a5.4 5.4 0 1 0 1.7-3.9M2.6 2.4v3.3h3.3"/>'),
    plus: svg('<path d="M3.5 8h9M8 3.5v9"/>', 14),
    on: svg('<path d="M2.5 6v4h2.6L8.6 13V3L5.1 6z"/>' +
            '<path d="M11 5.6a3.5 3.5 0 0 1 0 4.8"/>'),
    off: svg('<path d="M2.5 6v4h2.6L8.6 13V3L5.1 6z"/>' +
             '<path d="M11 6l3 4M14 6l-3 4"/>'),
    expand: svg('<path d="M2 6V2h4M14 6V2h-4M2 10v4h4M14 10v4h-4"/>'),
    shrink: svg('<path d="M6 2v4H2M10 2v4h4M6 14v-4H2M10 14v-4h4"/>'),
    close: '<svg width="14" height="14" viewBox="0 0 14 14" fill="none" ' +
           'aria-hidden="true"><path d="M2 2l10 10M12 2L2 12" ' +
           'stroke="currentColor" stroke-width="1.6" ' +
           'stroke-linecap="round"/></svg>'
  };

  // ── little DOM helpers ─────────────────────────────────────────────────

  function el(tag, style, marker) {
    var n = document.createElement(tag);
    if (style) { n.setAttribute('style', style); }
    if (marker) { n.setAttribute('data-mrb-added', marker); }
    if (tag === 'button') { n.type = 'button'; }
    return n;
  }

  /* A button with an optional icon and optional text. `label` (for an
     icon-only button) goes in aria-label. */
  function button(marker, style, iconName, txt, label, onClick) {
    var b = el('button', style, marker);
    if (iconName) {
      var i = el('span', 'display:inline-flex;flex:none');
      i.innerHTML = ICONS[iconName];
      b.appendChild(i);
    }
    if (txt) { b.appendChild(document.createTextNode(txt)); }
    if (label) { b.setAttribute('aria-label', label); }
    if (onClick) { b.addEventListener('click', onClick); }
    return b;
  }

  function disable(b) { b.setAttribute('aria-disabled', 'true'); return b; }

  // ── drawing ────────────────────────────────────────────────────────────

  var PRESETS = [[30, '30 s'], [60, '1 min'], [120, '2 min'], [180, '3 min'],
                 [300, '5 min'], [600, '10 min']];

  function modeSeg() {
    var seg = el('div', SEG);
    [['down', 'Countdown'], ['up', 'Stopwatch']].forEach(function (m) {
      var b = button('tm-mode-' + m[0], S.mode === m[0] ? SEG_ON : SEG_OFF,
                     null, m[1], null, function () { setMode(m[0]); });
      b.setAttribute('aria-pressed', S.mode === m[0] ? 'true' : 'false');
      seg.appendChild(b);
    });
    return seg;
  }

  function topButtons(parent) {
    var mute = button('tm-mute', S.muted ? ICON_ON : ICON_BTN,
                      S.muted ? 'off' : 'on', null,
                      S.muted ? 'Turn sound on' : 'Mute sound',
                      function () { S.muted = !S.muted; render(); });
    mute.setAttribute('aria-pressed', S.muted ? 'true' : 'false');
    parent.appendChild(mute);
    parent.appendChild(button('tm-view', ICON_BTN,
                              view === 'full' ? 'shrink' : 'expand', null,
                              view === 'full' ? 'Small timer' : 'Full-screen timer',
                              function () { setView(view === 'full' ? 'float' : 'full'); }));
    parent.appendChild(button('tm-close', ICON_BTN, 'close', null,
                              'Close timer', close));
  }

  function transport(parent, big) {
    var label = S.status === 'running' ? 'Pause'
              : S.status === 'paused' ? 'Resume'
              : S.status === 'done' ? 'Again' : 'Start';
    var go = button('tm-toggle', btnStyle('primary', big),
                    S.status === 'running' ? 'pause'
                    : S.status === 'done' ? 'reset' : 'play', label, null, toggle);
    parent.appendChild(go);

    var rs = button('tm-reset', btnStyle(atStart() ? 'off' : 'secondary', big),
                    'reset', 'Reset', null, atStart() ? null : function () { reset(); });
    if (atStart()) { disable(rs); }
    parent.appendChild(rs);

    if (S.mode === 'down' && (S.status === 'running' || S.status === 'paused')) {
      [[30000, '30 s', 'tm-add-30'], [60000, '1 min', 'tm-add-60']].forEach(function (a) {
        parent.appendChild(button(a[2], btnStyle('secondary', big), 'plus', a[1],
                                  'Add ' + a[1], function () { addTime(a[0]); }));
      });
    }
  }

  function presets(parent) {
    var row = el('div', ROWS + (view === 'float' ? ';gap:8px' : ''));
    PRESETS.forEach(function (p) {
      var on = S.preset === p[0] * 1000;
      var b = button('tm-preset-' + p[0], chipStyle(on), null, p[1], null,
                     function () { setPreset(p[0] * 1000); });
      b.setAttribute('aria-pressed', on ? 'true' : 'false');
      row.appendChild(b);
    });
    parent.appendChild(row);
  }

  function customRow(parent) {
    var row = el('div', ROWS);
    var FIELD = 'width:72px;min-height:44px;box-sizing:border-box;' +
                'padding:0 10px;font:600 18px/1.2 var(--st-mono);' +
                'text-align:center;color:var(--st-ink);' +
                'background:var(--st-paper);' +
                'border:1px solid var(--st-btn-border);border-radius:10px';
    var CAP = 'font:500 13px/1.2 var(--st-mono);letter-spacing:.14em;' +
              'text-transform:uppercase;color:var(--st-caption)';
    var t = Math.floor(S.preset / 1000);
    var min = el('input', FIELD, 'tm-custom-min');
    min.type = 'number'; min.min = '0'; min.max = '180';
    min.setAttribute('inputmode', 'numeric');
    min.setAttribute('aria-label', 'Custom minutes');
    min.value = String(Math.floor(t / 60));
    var sec = el('input', FIELD, 'tm-custom-sec');
    sec.type = 'number'; sec.min = '0'; sec.max = '59';
    sec.setAttribute('inputmode', 'numeric');
    sec.setAttribute('aria-label', 'Custom seconds');
    sec.value = String(t % 60);
    var lm = el('span', CAP); lm.textContent = 'min';
    var ls = el('span', CAP); ls.textContent = 'sec';
    var set = button('tm-custom-set', btnStyle('secondary', false), null, 'Set',
                     'Set custom time', function () {
      var m = Math.max(0, Math.min(180, Math.floor(Number(min.value)) || 0));
      var s = Math.max(0, Math.min(59, Math.floor(Number(sec.value)) || 0));
      var total = (m * 60 + s) * 1000;
      if (total <= 0) {
        min.setAttribute('aria-invalid', 'true');
        sec.setAttribute('aria-invalid', 'true');
        return;
      }
      setPreset(total);
    });
    [min, lm, sec, ls, set].forEach(function (n) { row.appendChild(n); });
    parent.appendChild(row);
  }

  function digitsEl() {
    var d = el('div', digitStyle(fmt(cur()).length), 'tm-digits');
    d.setAttribute('aria-hidden', 'true');
    d.setAttribute('data-tm-digits', '1');
    d.textContent = fmt(cur());
    digitsNode = d;
    return d;
  }

  function doneEl() {
    var d = el('div', view === 'full'
      ? 'font:600 clamp(28px,5vw,64px)/1.1 var(--st-display);' +
        'letter-spacing:-0.03em;color:var(--st-accent-text)'
      : 'font:600 18px/1.2 var(--st-ui);color:var(--st-accent-text);' +
        'text-align:center', 'tm-done');
    d.textContent = "Time's up";
    return d;
  }

  /* Rebuilt on a state change (start, pause, a button), never on a tick —
     a tick only repaints the digits. Focus is put back on the control that
     had it, by marker, since the node it was on is gone. */
  function render() {
    if (!root) { return; }
    var act = document.activeElement, marker = null;
    if (act && root.contains(act)) { marker = act.getAttribute('data-mrb-added'); }

    root.setAttribute('style', view === 'full' ? FULL : FLOAT);
    root.setAttribute('role', view === 'full' ? 'dialog' : 'region');
    if (view === 'full') { root.setAttribute('aria-modal', 'true'); }
    else { root.removeAttribute('aria-modal'); }
    root.setAttribute('aria-label', 'Timer');
    root.setAttribute('data-tm-view', view || '');
    root.setAttribute('data-tm-mode', S.mode);
    root.setAttribute('data-tm-muted', S.muted ? '1' : '0');
    root.setAttribute('data-tm-beeps', String(S.beeps));

    body.textContent = '';
    var idle = S.status === 'idle' || S.status === 'done';

    if (view === 'full') {
      var bar = el('div', BAR);
      if (idle) { bar.appendChild(modeSeg()); } else { bar.appendChild(el('div')); }
      var right = el('div', 'display:flex;align-items:center;gap:8px');
      topButtons(right);
      bar.appendChild(right);
      body.appendChild(bar);

      var mid = el('div', MID);
      mid.appendChild(digitsEl());
      if (S.status === 'done') { mid.appendChild(doneEl()); }
      var ctl = el('div', ROWS);
      transport(ctl, true);
      mid.appendChild(ctl);
      if (S.mode === 'down' && idle) {
        presets(mid);
        customRow(mid);
      }
      body.appendChild(mid);
    } else {
      var top = el('div', BAR_FLOAT);
      if (idle) { top.appendChild(modeSeg()); } else { top.appendChild(el('div')); }
      var rt = el('div', 'display:flex;align-items:center;gap:6px');
      topButtons(rt);
      top.appendChild(rt);
      body.appendChild(top);
      body.appendChild(digitsEl());
      if (S.status === 'done') { body.appendChild(doneEl()); }
      var ct = el('div', ROWS + ';gap:8px');
      transport(ct, false);
      body.appendChild(ct);
      if (S.mode === 'down' && idle) { presets(body); }
    }
    paint();

    if (marker) {
      var again = root.querySelector('[data-mrb-added="' + marker + '"]');
      if (again && again.focus) { try { again.focus(); } catch (e) { /* ok */ } }
    }
  }

  /* The per-tick repaint: the reading, and the state it is in. */
  function paint() {
    if (!root || !digitsNode) { return; }
    var ms = cur(), r = fmt(ms), st = stateName();
    if (digitsNode.textContent !== r) {
      digitsNode.textContent = r;
      digitsNode.setAttribute('style', digitStyle(r.length));
    }
    var col = (st === 'warn' || st === 'done') ? 'var(--st-accent)'
            : st === 'paused' ? 'var(--st-muted)' : 'var(--st-ink)';
    digitsNode.style.color = col;
    root.setAttribute('data-tm-state', st);
    root.setAttribute('data-tm-reading', r);
  }

  // ── views, open, close ─────────────────────────────────────────────────

  function notify() {
    listeners.slice().forEach(function (fn) { try { fn(); } catch (e) { /* ok */ } });
  }

  function setView(v) {
    view = v;
    render();
    var f = root.querySelector(v === 'full' ? '[data-mrb-added="tm-toggle"]'
                                            : '[data-mrb-added="tm-view"]');
    if (f && f.focus) { try { f.focus(); } catch (e) { /* ok */ } }
    notify();
  }

  function open(opts) {
    opts = opts || {};
    var want = opts.view === 'float' ? 'float' : 'full';
    var wasOpen = !!root;
    if (!wasOpen) {
      var a = document.activeElement;
      prevFocus = (a && a !== document.body) ? a : null;
      root = el('div', FULL, 'tm-root');
      root.setAttribute('data-tm', 'overlay');
      body = el('div', 'display:contents');
      liveNode = el('div', SR, 'tm-live');
      liveNode.setAttribute('role', 'status');
      liveNode.setAttribute('aria-live', 'polite');
      liveNode.setAttribute('aria-atomic', 'true');
      root.appendChild(body);
      root.appendChild(liveNode);
      document.body.appendChild(root);
      window.addEventListener('keydown', onKey, true);
      window.addEventListener('keyup', onKeyUp, true);
    }
    opens += 1;
    root.setAttribute('data-tm-opens', String(opens));
    /* A second open never DEMOTES: asking for the float while the full view
       is up leaves the full view up. Asking for full promotes. */
    view = (wasOpen && view === 'full') ? 'full' : want;
    render();
    if (view === 'full') {
      var f = root.querySelector('[data-mrb-added="tm-toggle"]');
      if (f && f.focus) { try { f.focus(); } catch (e) { /* ok */ } }
    }
    notify();
  }

  function close() {
    if (!root) { return; }
    stopTick();
    window.removeEventListener('keydown', onKey, true);
    window.removeEventListener('keyup', onKeyUp, true);
    if (root.parentNode) { root.parentNode.removeChild(root); }
    root = body = liveNode = digitsNode = null;
    var wasFull = view === 'full';
    view = null;
    /* Back to a clean idle at the same length; mute and the last preset are
       kept, in memory, for the next open. */
    S.status = 'idle';
    S.ms = S.mode === 'down' ? S.preset : 0;
    lastSaid = null;
    if (wasFull && prevFocus && document.contains(prevFocus)) {
      try { prevFocus.focus(); } catch (e) { /* ok */ }
    }
    prevFocus = null;
    notify();
  }

  // ── keyboard ───────────────────────────────────────────────────────────

  function typing(t) {
    var tag = t && t.tagName;
    return tag === 'INPUT' || tag === 'TEXTAREA' || tag === 'SELECT' ||
           !!(t && t.isContentEditable);
  }
  function isSpace(e) { return e.key === ' ' || e.code === 'Space'; }
  function spaceIsMine(e) {
    if (!root || typing(e.target)) { return false; }
    return view === 'full' || (view === 'float' && root.contains(e.target));
  }

  function onKey(e) {
    if (!root) { return; }
    if ((e.key === 'Escape' || e.keyCode === 27) && view === 'full') {
      /* Handled and STOPPED: the picker's own Escape handler is on
         `document`, later in the path, and must not see this keypress. */
      e.stopPropagation(); e.preventDefault();
      if (S.status === 'running' || S.status === 'paused') { setView('float'); }
      else { close(); }
      return;
    }
    if (isSpace(e) && spaceIsMine(e)) {
      e.preventDefault(); e.stopPropagation();
      if (!e.repeat) { toggle(); }
      return;
    }
    if (e.key === 'Tab' && view === 'full') {
      var f = root.querySelectorAll('button:not([aria-disabled="true"]),input');
      if (!f.length) { return; }
      var first = f[0], last = f[f.length - 1], a = document.activeElement;
      if (e.shiftKey && (a === first || !root.contains(a))) {
        e.preventDefault(); last.focus();
      } else if (!e.shiftKey && (a === last || !root.contains(a))) {
        e.preventDefault(); first.focus();
      }
    }
  }

  /* A focused button would otherwise ALSO activate on the Space key's
     release; the keydown already did the timer's work. */
  function onKeyUp(e) {
    if (root && isSpace(e) && spaceIsMine(e)) {
      e.preventDefault(); e.stopPropagation();
    }
  }

  window.MrBadmusTimer = {
    open: open,
    close: close,
    isOpen: function () { return !!root; },
    /* Subscribe to open / close / view / state changes; returns an
       unsubscribe function. The picker uses it to keep its Timer button's
       pressed state honest. */
    onChange: function (fn) {
      listeners.push(fn);
      return function () {
        var i = listeners.indexOf(fn);
        if (i !== -1) { listeners.splice(i, 1); }
      };
    }
  };
}());
