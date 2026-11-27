/* shared/teacher-timer.js — a classroom timer, and the SHELL that shows the
   teacher tools (this timer and the name picker, `teacher-picker.js`) in one
   place at a time.

   `window.MrBadmusTimer = {open(opts), close(), isOpen(), isShown(), …}`.
   `opts.view` is 'full' (the default) or 'dock' (not full: docked in the
   picker's board when it is open, otherwise the Mini). 'float' and 'mini'
   are accepted as old names for 'dock'.

   ══ ONE STATE, FOUR VIEWS, AND ONLY ONE VIEW AT A TIME ══════════════════

   The STATE is single-source and no view owns any of it: the timer's `S`
   below, and the picker's per-class `STATE` in `teacher-picker.js`. The views
   only draw that state, so no view change — minimise, expand, pop-out,
   pop-in, the teacher closing the pop-out window — can reset a running timer
   or lose the picked list, the absent list, weights or pick-next.

     1. BOARD — the picker's full-screen board (`teacher-picker.js`). A live
        timer (running, paused, finished or ready) is DOCKED in the board's
        own layout as a slim STRIP, the row under its header
        (`[data-mrb-tm-slot]`, which the picker draws). It is in the flow of
        the board, never a card over it: ONE row of the board's HEADER (its
        own line of the header on a phone), at most 56px tall, so the name
        and the Pick button keep their space. It holds the digits (warn
        colour in the last ten seconds, the finished state), start/pause and
        expand (to the full timer), and nothing else — reset, time adjust,
        presets and mute are the full view's. The timer is closed from the
        full view's X, or from the Mini.
     2. TIMER FULL — an opaque, full-viewport display with digits sized for
        the back of a projected room (`min(32vw, 56vh)`, tabular numerals):
        presets, a custom time, a stopwatch, start/pause/reset, and −30 s,
        +30 s, +1 min while a countdown is running or paused (removing time
        clamps at 0, and reaching 0 that way is "Time's up"). Its header:
        mute, pop-out, minimise (to the board's strip if the board is open
        underneath, otherwise to the Mini) and X (close the timer).
     3. MINI — ONE small panel, at most 320px wide, on `document.body`, fixed, on top of
        everything, DRAGGABLE by its header (pointer events, kept inside the
        viewport, the position kept in memory only). It holds whichever tools
        are live: a timer section (digits, start/pause, reset, −30 s, +30 s)
        and/or a picker section (the class, the last picked name, Pick and
        Skip, drawn by the picker) for the class the picker was last opened
        on. At rest it is three rows: the header, the timer row (digits,
        start/pause, reset, −30 s, +30 s) and the picker row (name, Pick,
        Skip). Its header: expand (back to the board, or the full timer when
        there is no board), pop-out, mute, X. X closes the Mini AND its tools:
        the timer stops and clears, the picker closes and keeps its per-class
        STATE in memory exactly as closing the board does. It starts in the
        bottom-right corner; at or under 560px wide it docks full-width at the
        bottom and drags up and down only.
     4. POP-OUT — the Mini's sections in a Document Picture-in-Picture window
        (see POP-OUT below).

   `layout()` is the only thing that decides what shows, and the rule is:
     · popped out          → everything is in the pop-out; NOTHING of the
                             tools is on the page;
     · else board open     → the board (the timer as its strip, or the full
                             timer over it if the teacher expanded it);
     · else timer full     → the full timer;
     · else anything live  → the Mini.
   So the Mini is never up with the board or the full timer, and nothing ever
   floats over the board. Close and minimise are one tap on a visible 44px
   button in every view; nothing needs a swipe or a detour via full screen.

   ══ POP-OUT (Document Picture-in-Picture), AND ITS FALLBACK ═════════════

   Offered only where `'documentPictureInPicture' in window`; anywhere else
   the pop-out buttons are not drawn at all and the Mini IS the on-top box
   (over the teacher page only — these tools are never put on lesson pages).
   The button calls `requestWindow()` inside the click (it needs the click's
   activation). If that throws or is refused, the tools quietly stay in the
   Mini and the button is not offered again in this page load; nothing is
   said about it.

   The window (about 360×300, taller with both tools) starts empty: the
   page's stylesheets are copied in (each sheet's rules into a `<style>`, a
   `<link>` when its rules cannot be read), its `<html data-theme>` mirrors
   the page's and keeps mirroring it while open (a MutationObserver), and its
   body has an explicit `--st-ground` background. The same nodes the Mini
   held are moved into it, under a header of mute and "Back to page". Its
   digits and the picked name are sized in container units of their own
   section (`cqw`/`cqh`), so they grow with the window as the teacher
   resizes it. Its title follows the brand rule (`… | MrBadmus`).
   "Back to page", or the teacher closing the window with its own X
   (`pagehide`), puts the tools back on the page as the Mini with identical
   state. So does pressing the PAGE's own "Pick a student" or "Timer" while
   popped out — the teacher is asking for that tool on the page — which then
   opens the board or the full timer as usual. While it is open the clicker listener is on the pop-out's window
   as well, the ticker and the reveal run on ITS timers (a page in a
   background tab is throttled; the pop-out in front is not), and the finish
   beep still plays from this page's Web Audio.

   ══ WHAT IT WRITES — NOTHING ═══════════════════════════════════════════

   ⛔ No storage of any kind, no cookie, no `fetch`, no Supabase, no audio
   file. The countdown's end sound is two short Web Audio oscillator beeps
   made in the page. Everything lives in this closure (`S`, and the shell's
   view flags, the Mini's position and the pop-out window), including the
   mute toggle, and goes with the page load.

   ══ WHERE IT MOUNTS, AND WHY ═══════════════════════════════════════════

   The timer is ONE element, `[data-tm="overlay"]`, MOVED to wherever its
   view is: `document.body` (full, or hidden), the board's slot (strip), the
   Mini, or the pop-out. ⚠️ Full and Mini are on `document.body`, never in
   `#mrb-teacher`: the generated teacher pages are drawn by
   `student-runtime`, whose `draw()` empties that host on every `setState`.

   ⚠️ THE STRIP IS INSIDE THE BOARD, AND SO INSIDE THE HOST, and the drive
   gates decide whether a press "did something" by comparing the host's text.
   A clock that changed that text every second would make dead controls look
   alive, so the strip's digits are CSS generated content
   (`::before{content:attr(data-tm-gen)}`) — drawn, but not in `innerText`.
   They are `aria-hidden` everywhere anyway (see SCREEN READERS).
   `teacher_behaviour.py` reads this element's view, open count and press
   count (`data-tm-view`, `data-tm-opens`, `data-tm-acts`) and the Mini's
   (`data-tools-view`, `data-tools-opens`), never the reading.

   ══ KEYBOARD ══════════════════════════════════════════════════════════

   One capture-phase keydown/keyup pair on `window` (and on the pop-out's
   window while it is open), attached while the timer exists OR the picker is
   live (see the CLICKER KEYS note by `onKey`): a presentation clicker's
   forward key picks (or, with no picker or a full-screen timer covering it,
   starts/pauses the timer), its back key starts/pauses the timer, a hold of
   about a second cheers, and B or "." shows/hides the timer without stopping
   it. Nothing is taken while focus is in an input. Escape on the page closes
   the FULL view — to the strip or the Mini if the timer has been started,
   outright if not — and is stopped in the capture phase so the same keypress
   never reaches the picker's own Escape handler beneath. Escape in the
   pop-out does nothing. F5 is never touched.

   ══ SCREEN READERS ═════════════════════════════════════════════════════

   The digits are `aria-hidden`: a live region that changed every second
   would be unusable. A separate visually-hidden `role="status"` region says
   the time on start, pause and finish, and at most once a minute in between.
*/
(function () {
  'use strict';

  var Z = 100;                       // the full timer: above the picker's board (90)
  var ZMINI = 2147483000;            // the Mini: above everything on the page
  var WARN_MS = 10000;               // the last ten seconds
  var NARROW = 560;                  // at or under: the Mini docks full-width

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
  /* ── the shell's view flags (never the tools' state) ────────────────── */
  var full = false;                  // the teacher wants the full view
  var hidden = false;                // open and running, but not shown (B)
  var view = null;                   // null | full | strip | mini | pip | hidden
  var root = null, tbody = null, liveNode = null, digitsNode = null;
  var digitsGen = false;             // strip: digits as generated content
  var ticker = null, opens = 0, acts = 0, prevFocus = null, audio = null;
  var lastSaid = null;               // the minute last announced
  var listeners = [];

  var mini = null, miniOpens = 0, miniPos = null, drag = null;
  var pipWin = null, pipObs = null, pipBroken = false, pipPending = false;

  function now() {
    return (window.performance && performance.now) ? performance.now()
                                                   : Date.now();
  }

  /* Timers run on the window the tools are SHOWN in: the pop-out's while it
     is open (a page in a background tab is throttled to a tick a second or
     worse; the window in front of the class is not), this page's otherwise.
     `later` hands back the window with the id, so `cancel` clears it on the
     right one even after the pop-out has gone. */
  function later(fn, ms) {
    var w = pipWin || window;
    try { return { w: w, id: w.setTimeout(fn, ms) }; }
    catch (e) { return { w: window, id: window.setTimeout(fn, ms) }; }
  }
  function cancel(h) {
    if (!h) { return; }
    try { h.w.clearTimeout(h.id); } catch (e) { /* the window is gone */ }
  }

  function P() {
    var p = window.MrBadmusPicker;
    return (p && p.view) ? p : null;
  }
  function pickerView() { var p = P(); return p ? p.view() : null; }

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

  function stopTick() {
    if (ticker) {
      try { ticker.w.clearInterval(ticker.id); } catch (e) { /* gone */ }
      ticker = null;
    }
  }
  /* On the window the tools are shown in — see `later`. Restarted whenever
     the pop-out opens or closes, so it always lives on the visible one. */
  function startTick() {
    stopTick();
    var w = pipWin || window;
    try { ticker = { w: w, id: w.setInterval(tick, 200) }; }
    catch (e) { ticker = { w: window, id: window.setInterval(tick, 200) }; }
  }

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

  /* Add (or, with a negative delta, REMOVE) time from a running or paused
     countdown. Clamped at 0, and a countdown taken to 0 this way has run
     out: it finishes, with its sound, exactly as if it had got there. */
  function addTime(delta) {
    if (S.mode !== 'down') { return; }
    if (S.status === 'running') { S.endAt = Math.max(now(), S.endAt + delta); }
    else if (S.status === 'paused') { S.ms = Math.max(0, S.ms + delta); }
    else { return; }
    if (cur() <= 0) { finish(); return; }
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
  /* The strip: a row of the board's own layout, under its header. */
  /* ⊕ Mide, 16 Nov 2026: "too big, it shouldn't take that much space". The
     strip is ONE row inside the board's HEADER (never the stage), at most
     56px tall at every width: the digits, start/pause and expand, nothing
     else. Reset, time adjust, presets and mute are the full view's. */
  var STRIP = 'display:flex;align-items:center;justify-content:center;' +
              'gap:8px;min-width:0;max-height:56px;color:var(--st-ink)';
  /* The Mini's timer: one row — digits, start/pause, reset, −30 s, +30 s. */
  var COMPACT = 'display:flex;align-items:center;gap:6px;padding:6px 10px;' +
                'color:var(--st-ink)';
  /* In the pop-out the section is its own size container, so the digits
     scale with whatever the teacher has made of the window. */
  var PIPSEC = 'flex:1 1 0;min-height:0;container-type:size;display:flex;' +
               'flex-direction:column;align-items:center;' +
               'justify-content:safe center;gap:8px;padding:6px 10px 10px;' +
               'color:var(--st-ink);overflow:hidden';
  var MINI_BOX = 'position:fixed;z-index:' + ZMINI + ';box-sizing:border-box;' +
                 'max-height:calc(100vh - 16px);overflow:auto;' +
                 'background:var(--st-paper);color:var(--st-ink);' +
                 'border:1px solid var(--st-edge);border-radius:14px;' +
                 'box-shadow:var(--st-shadow-frame);display:flex;' +
                 'flex-direction:column';
  var MINI_HEAD = 'flex:none;display:flex;align-items:center;gap:6px;' +
                  'padding:6px 6px 6px 8px;cursor:grab;touch-action:none;' +
                  'user-select:none;-webkit-user-select:none;' +
                  'border-bottom:1px solid var(--st-rule)';
  var GRIP = 'flex:1;min-width:0;display:flex;align-items:center;' +
             'min-height:44px;color:var(--st-caption)';
  var SR = 'position:absolute;width:1px;height:1px;margin:-1px;padding:0;' +
           'overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap;border:0';

  /* Row-REVERSED and wrapping: the buttons (minimise, X) are first in the
     row, so on a phone, where the mode switch and four buttons cannot share
     a line, the buttons keep the top right and the switch goes under them. */
  var BAR = 'flex:none;display:flex;flex-direction:row-reverse;' +
            'flex-wrap:wrap;align-items:center;gap:10px;' +
            'justify-content:space-between;padding:14px 20px;' +
            'border-bottom:1px solid var(--st-rule)';
  var ICON_BTN = 'flex:none;width:44px;height:44px;display:flex;' +
                 'align-items:center;justify-content:center;padding:0;' +
                 'background:transparent;border:1px solid var(--st-btn-border);' +
                 'border-radius:10px;cursor:pointer;color:var(--st-muted)';
  var ICON_ON = ICON_BTN.replace('background:transparent',
                                 'background:var(--st-seg-bg)')
                        .replace('color:var(--st-muted)', 'color:var(--st-ink)');
  /* Start/pause as an icon (strip, Mini): the primary action's colours. */
  var ICON_GO = ICON_BTN.replace('background:transparent',
                                 'background:var(--st-accent-text)')
                        .replace('border:1px solid var(--st-btn-border)',
                                 'border:1px solid var(--st-accent-text)')
                        .replace('color:var(--st-muted)', 'color:var(--st-paper)');
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
    var base = 'flex:none;min-height:' + h + 'px;min-width:44px;padding:0 ' +
               (big ? 34 : 14) + 'px;font:' + f + ' var(--st-ui);' +
               'display:inline-flex;align-items:center;justify-content:center;' +
               'gap:8px;border-radius:11px;cursor:pointer;box-sizing:border-box;';
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
    return 'min-height:44px;padding:0 16px;font:600 16px/1.2 var(--st-ui);' +
           'border-radius:10px;cursor:pointer;color:var(--st-ink);' +
           'background:' + (on ? 'var(--st-seg-bg)' : 'var(--st-paper)') + ';' +
           'border:1px solid ' + (on ? 'var(--st-rule-strong)'
                                     : 'var(--st-btn-border)');
  }

  /* Digits. Full: the biggest that fits a 5-character reading across the
     viewport width or its height, whichever is smaller. Longer readings (an
     hour or more) take the smaller size. Pop-out: the same idea in the
     section's own container units. Tabular numerals, so the reading never
     jitters as digits change (measured: every 4-character reading is the
     same width in Instrument Sans). Not the mono face: DM Mono's zero is
     slashed, which on a projector reads as a different character. */
  function digitStyle(len) {
    var long = len > 5, size;
    if (view === 'full') {
      size = long ? 'clamp(56px,min(22vw,42vh),460px)'
                  : 'clamp(72px,min(32vw,56vh),640px)';
    } else if (view === 'pip') {
      size = long ? 'max(28px,min(25cqw,calc(100cqh - 72px)))'
                  : 'max(32px,min(36cqw,calc(100cqh - 72px)))';
    } else if (view === 'strip') {
      size = long ? '24px' : '30px';
    } else {
      size = long ? '22px' : '30px';
    }
    return 'font:600 ' + size + '/1 var(--st-ui);' +
           'font-variant-numeric:tabular-nums;letter-spacing:-.02em;' +
           'text-align:center;white-space:nowrap;' +
           (view === 'pip' ? 'margin:0 auto' : 'flex:none');
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
    minus: svg('<path d="M3.5 8h9"/>', 14),
    on: svg('<path d="M2.5 6v4h2.6L8.6 13V3L5.1 6z"/>' +
            '<path d="M11 5.6a3.5 3.5 0 0 1 0 4.8"/>'),
    off: svg('<path d="M2.5 6v4h2.6L8.6 13V3L5.1 6z"/>' +
             '<path d="M11 6l3 4M14 6l-3 4"/>'),
    expand: svg('<path d="M2 6V2h4M14 6V2h-4M2 10v4h4M14 10v4h-4"/>'),
    /* minimise: a bar at the foot of the box — "put it down small" */
    minimise: svg('<path d="M3.5 12.5h9"/>'),
    /* pop-out: an arrow leaving a window; back to page: one coming in */
    popout: svg('<path d="M9.5 2.5h4v4M13.5 2.5L8 8"/>' +
                '<path d="M12 9.5v3a1 1 0 0 1-1 1H3.5a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3"/>'),
    popin: svg('<path d="M13.5 2.5L8 8M8 4.5V8h3.5"/>' +
               '<path d="M12 9.5v3a1 1 0 0 1-1 1H3.5a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3"/>'),
    grip: '<svg width="16" height="16" viewBox="0 0 16 16" fill="none" ' +
          'aria-hidden="true" stroke="currentColor" stroke-width="2.2" ' +
          'stroke-linecap="round"><path d="M5.5 4h.01M10.5 4h.01M5.5 8h.01' +
          'M10.5 8h.01M5.5 12h.01M10.5 12h.01"/></svg>',
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
     icon-only button) goes in aria-label. Every press of a timer control is
     counted on the element (`data-tm-acts`) — see the mount note. */
  function button(marker, style, iconName, txt, label, onClick) {
    var b = el('button', style, marker);
    if (iconName) {
      var i = el('span', 'display:inline-flex;flex:none');
      i.innerHTML = ICONS[iconName];
      b.appendChild(i);
    }
    if (txt) { b.appendChild(document.createTextNode(txt)); }
    if (label) { b.setAttribute('aria-label', label); }
    if (onClick) {
      b.addEventListener('click', function (e) {
        acts += 1;
        if (root) { root.setAttribute('data-tm-acts', String(acts)); }
        onClick(e);
      });
    }
    return b;
  }

  function disable(b) { b.setAttribute('aria-disabled', 'true'); return b; }

  /* The strip's digits are generated content (see the mount note); this
     puts the one rule that draws them into whichever document needs it. */
  function genCss(doc) {
    if (!doc || doc.querySelector('style[data-mrb-tm-css]')) { return; }
    var st = doc.createElement('style');
    st.setAttribute('data-mrb-tm-css', '1');
    st.textContent = '[data-tm-gen]::before{content:attr(data-tm-gen)}';
    (doc.head || doc.documentElement).appendChild(st);
  }

  // ── drawing the timer ──────────────────────────────────────────────────

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

  function muteBtn(marker) {
    var b = button(marker, S.muted ? ICON_ON : ICON_BTN,
                   S.muted ? 'off' : 'on', null,
                   S.muted ? 'Turn sound on' : 'Mute sound',
                   function () { S.muted = !S.muted; sync(marker); });
    b.setAttribute('aria-pressed', S.muted ? 'true' : 'false');
    return b;
  }

  function fullButtons(parent) {
    parent.appendChild(muteBtn('tm-mute'));
    if (pipOK()) {
      parent.appendChild(button('tm-popout', ICON_BTN, 'popout', null,
                                'Pop out', popOut));
    }
    parent.appendChild(button('tm-min', ICON_BTN, 'minimise', null,
                              'Minimise', function () { minimiseFull(); }));
    parent.appendChild(button('tm-close', ICON_BTN, 'close', null,
                              'Close timer', close));
  }

  function toggleLabel() {
    return S.status === 'running' ? 'Pause'
         : S.status === 'paused' ? 'Resume'
         : S.status === 'done' ? 'Again' : 'Start';
  }
  function toggleIcon() {
    return S.status === 'running' ? 'pause'
         : S.status === 'done' ? 'reset' : 'play';
  }

  /* `size`: 'full' (the 60px row, with labels), 'mini' (the Mini's and the
     pop-out's one row: icons, and the time steps as an icon plus "30"),
     'strip' (start/pause only). */
  function transport(parent, size) {
    var big = size === 'full';
    if (size === 'strip' || size === 'mini') {
      parent.appendChild(button('tm-toggle', ICON_GO, toggleIcon(), null,
                                toggleLabel(), toggle));
      if (size === 'strip') { return; }
    } else {
      parent.appendChild(button('tm-toggle', btnStyle('primary', big),
                                toggleIcon(), toggleLabel(), null, toggle));
    }

    var rs = button('tm-reset', btnStyle(atStart() ? 'off' : 'secondary', big),
                    'reset', big ? 'Reset' : null, big ? null : 'Reset',
                    atStart() ? null : function () { reset(); });
    if (atStart()) { disable(rs); }
    parent.appendChild(rs);

    if (S.mode === 'down' && (S.status === 'running' || S.status === 'paused')) {
      var m = size === 'mini';
      var steps = [[-30000, 'minus', m ? '30' : '30 s', 'tm-sub-30', 'Remove 30 seconds'],
                   [30000, 'plus', m ? '30' : '30 s', 'tm-add-30', 'Add 30 seconds']];
      if (big) { steps.push([60000, 'plus', '1 min', 'tm-add-60', 'Add 1 minute']); }
      steps.forEach(function (a) {
        parent.appendChild(button(a[3], btnStyle('secondary', big) +
                                  (m ? ';padding:0 8px;gap:3px;font-size:15px' : ''),
                                  a[1], a[2], a[4], function () { addTime(a[0]); }));
      });
    }
  }

  function presets(parent) {
    var row = el('div', ROWS);
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
    var r = fmt(cur());
    var d = el('div', digitStyle(r.length), 'tm-digits');
    d.setAttribute('aria-hidden', 'true');
    d.setAttribute('data-tm-digits', '1');
    digitsGen = view === 'strip';
    if (digitsGen) { d.setAttribute('data-tm-gen', r); }
    else { d.textContent = r; }
    digitsNode = d;
    return d;
  }

  function doneEl() {
    var d = el('div', view === 'full'
      ? 'font:600 clamp(28px,5vw,64px)/1.1 var(--st-display);' +
        'letter-spacing:-0.03em;color:var(--st-accent-text)'
      : view === 'pip'
      ? 'font:600 max(16px,min(7cqw,12cqh))/1.1 var(--st-ui);' +
        'color:var(--st-accent-text);text-align:center'
      : 'font:600 15px/1.2 var(--st-ui);color:var(--st-accent-text);' +
        'text-align:center;white-space:nowrap;flex:none', 'tm-done');
    d.textContent = "Time's up";
    return d;
  }

  function rootStyle() {
    if (view === 'full') { return FULL; }
    if (view === 'strip') { return STRIP; }
    if (view === 'pip') { return PIPSEC; }
    if (view === 'mini') { return COMPACT; }
    return 'display:none';
  }

  /* Rebuilt on a state change (start, pause, a button), never on a tick —
     a tick only repaints the digits. Focus is put back on the control that
     had it, by marker, since the node it was on is gone. */
  function render() {
    if (!root) { return; }
    var doc = root.ownerDocument;
    var act = doc.activeElement, marker = null;
    if (act && root.contains(act)) { marker = act.getAttribute('data-mrb-added'); }

    root.setAttribute('style', rootStyle());
    root.setAttribute('role', view === 'full' ? 'dialog' : 'region');
    if (view === 'full') { root.setAttribute('aria-modal', 'true'); }
    else { root.removeAttribute('aria-modal'); }
    root.setAttribute('aria-label', 'Timer');
    root.setAttribute('data-tm-view', view || '');
    root.setAttribute('data-tm-mode', S.mode);
    root.setAttribute('data-tm-muted', S.muted ? '1' : '0');
    root.setAttribute('data-tm-beeps', String(S.beeps));
    root.setAttribute('data-tm-acts', String(acts));

    tbody.textContent = '';
    digitsNode = null;
    var idle = S.status === 'idle' || S.status === 'done';

    if (view === 'full') {
      var bar = el('div', BAR);
      var right = el('div', 'display:flex;align-items:center;gap:8px;margin-left:auto');
      fullButtons(right);
      bar.appendChild(right);
      if (idle) { bar.appendChild(modeSeg()); } else { bar.appendChild(el('div')); }
      tbody.appendChild(bar);

      var mid = el('div', MID);
      mid.appendChild(digitsEl());
      if (S.status === 'done') { mid.appendChild(doneEl()); }
      var ctl = el('div', ROWS);
      transport(ctl, 'full');
      mid.appendChild(ctl);
      if (S.mode === 'down' && idle) {
        presets(mid);
        customRow(mid);
      }
      tbody.appendChild(mid);
    } else if (view === 'strip') {
      genCss(doc);
      tbody.appendChild(digitsEl());
      if (S.status === 'done') { tbody.appendChild(doneEl()); }
      transport(tbody, 'strip');
      tbody.appendChild(button('tm-expand', ICON_BTN, 'expand', null,
                               'Full-screen timer', function () { expandFull(); }));
    } else if (view === 'mini') {
      tbody.appendChild(digitsEl());
      tbody.appendChild(el('div', 'flex:1;min-width:0'));
      transport(tbody, 'mini');
    } else if (view === 'pip') {
      tbody.appendChild(digitsEl());
      if (S.status === 'done') { tbody.appendChild(doneEl()); }
      var ct = el('div', ROWS + ';gap:8px');
      transport(ct, 'mini');
      tbody.appendChild(ct);
    }
    paint();

    if (marker) {
      var again = root.querySelector('[data-mrb-added="' + marker + '"]');
      if (again && again.focus) { try { again.focus(); } catch (e) { /* ok */ } }
    }
  }

  /* The per-tick repaint: the reading, and the state it is in. */
  function paint() {
    if (!root) { return; }
    var ms = cur(), r = fmt(ms), st = stateName();
    root.setAttribute('data-tm-state', st);
    root.setAttribute('data-tm-reading', r);
    if (!digitsNode) { return; }
    var was = digitsGen ? digitsNode.getAttribute('data-tm-gen')
                        : digitsNode.textContent;
    if (was !== r) {
      if (digitsGen) { digitsNode.setAttribute('data-tm-gen', r); }
      else { digitsNode.textContent = r; }
      if (!was || was.length !== r.length) {
        digitsNode.setAttribute('style', digitStyle(r.length));
      }
    }
    var col = (st === 'warn' || st === 'done') ? 'var(--st-accent)'
            : st === 'paused' ? 'var(--st-muted)' : 'var(--st-ink)';
    digitsNode.style.color = col;
  }

  function notify() {
    listeners.slice().forEach(function (fn) { try { fn(); } catch (e) { /* ok */ } });
  }

  // ══ THE SHELL: which view shows ══════════════════════════════════════

  function narrow() { return window.innerWidth <= NARROW; }

  /* THE one place that decides what shows — the rule is in the header.
     `focusMarker`, when given, is the control to put focus on afterwards
     (the nodes are rebuilt, so focus is restored by marker). */
  function layout() {
    var pv = pickerView();
    var tv = null;
    if (root) {
      tv = hidden ? 'hidden'
         : pipWin ? 'pip'
         : full ? 'full'
         : pv === 'board' ? 'strip' : 'mini';
    }
    view = tv;
    var wantMini = !pipWin && !pipPending && pv !== 'board' && tv !== 'full' &&
                   (tv === 'mini' || pv === 'away');
    /* A pop-out with nothing left in it has nothing to show. A timer HIDDEN
       with B/"." is still in it: B hides and nothing else changes, so the
       window stays open and the next B shows the timer there again. */
    if (pipWin && !(tv === 'pip' || tv === 'hidden' || pv === 'away')) { pipBack(); return; }

    if (pipWin) { drawPip(tv, pv); }
    if (wantMini || (pipPending && (tv || pv === 'away'))) { drawMini(tv, pv); }
    else { removeMini(); }

    if (root) {
      if (tv === 'full' || tv === 'hidden') {
        if (root.parentNode !== document.body) { document.body.appendChild(root); }
      } else if (tv === 'strip') {
        var slot = P() && P().slot ? P().slot() : null;
        if (slot && root.parentNode !== slot) { slot.appendChild(root); }
        else if (!slot && !root.parentNode) { document.body.appendChild(root); }
      } else if (tv === 'mini' && !mini) {
        /* pip pending with no Mini drawn cannot happen; belt and braces */
        document.body.appendChild(root);
      }
      render();
    }
    /* Placed again now the timer row has its real height: `drawMini`
       measured it before `render()` filled it (or while it still carried the
       pop-out's sizing), which left a dragged Mini hanging off the edge. */
    if (mini) { placeMini(); }
  }

  function sync(focusMarker) {
    layout();
    syncKeys();
    notify();
    if (focusMarker) { focusOn(focusMarker); }
  }

  function focusOn(marker) {
    var places = [mini, root, pipWin && pipWin.document.body,
                  document.querySelector('[data-mrb-picker]')];
    for (var i = 0; i < places.length; i++) {
      var p = places[i];
      if (!p) { continue; }
      var n = p.querySelector('[data-mrb-added="' + marker + '"]');
      if (n && n.focus) { try { n.focus(); } catch (e) { /* ok */ } return; }
    }
  }

  // ── the Mini ───────────────────────────────────────────────────────────

  function miniHeadButtons(parent) {
    parent.appendChild(button('tools-expand', ICON_BTN, 'expand', null,
                              pickerView() === 'away' ? 'Back to the board'
                                                      : 'Full-screen timer',
                              function () { expandMini(); }));
    if (pipOK()) {
      parent.appendChild(button('tools-popout', ICON_BTN, 'popout', null,
                                'Pop out', popOut));
    }
    parent.appendChild(muteBtn('tools-mute'));
    parent.appendChild(button('tools-close', ICON_BTN, 'close', null,
                              'Close', closeAll));
  }

  function placeMini() {
    if (!mini) { return; }
    var st = mini.style;
    if (narrow()) {
      st.left = '8px'; st.right = '8px'; st.width = 'auto';
    } else {
      st.width = 'min(320px,calc(100vw - 32px))';
    }
    if (!miniPos) {
      st.top = 'auto'; st.bottom = narrow() ? '8px' : '16px';
      if (!narrow()) { st.left = 'auto'; st.right = '16px'; }
      return;
    }
    /* Remembered (memory only) and clamped, so a resize can never leave it
       off screen. */
    var w = mini.offsetWidth, h = mini.offsetHeight;
    var vw = window.innerWidth, vh = window.innerHeight;
    var x = narrow() ? 8 : Math.max(8, Math.min(miniPos.x, vw - w - 8));
    var y = Math.max(8, Math.min(miniPos.y, vh - h - 8));
    st.right = narrow() ? '8px' : 'auto'; st.bottom = 'auto';
    st.left = x + 'px'; st.top = y + 'px';
  }

  function drawMini(tv, pv) {
    var doc = document, act = doc.activeElement, marker = null;
    if (!mini) {
      mini = el('div', MINI_BOX, 'tools-mini');
      mini.setAttribute('data-mrb-tools', 'mini');
      mini.setAttribute('role', 'region');
      mini.setAttribute('aria-label', 'Classroom tools');
      miniOpens += 1;
      mini.setAttribute('data-tools-opens', String(miniOpens));
      document.body.appendChild(mini);
    } else if (act && mini.contains(act)) {
      marker = act.getAttribute('data-mrb-added');
    }
    mini.setAttribute('data-tools-view', (tv === 'mini' ? 'timer' : '') +
                      (pv === 'away' ? (tv === 'mini' ? '+' : '') + 'picker' : ''));
    mini.textContent = '';
    mini.setAttribute('style', MINI_BOX);

    var head = el('div', MINI_HEAD, 'tools-head');
    var grip = el('div', GRIP);
    grip.innerHTML = ICONS.grip;
    head.appendChild(grip);
    miniHeadButtons(head);
    head.addEventListener('pointerdown', onGripDown);
    head.addEventListener('pointermove', onGripMove);
    head.addEventListener('pointerup', onGripUp);
    head.addEventListener('pointercancel', onGripUp);
    mini.appendChild(head);

    if (root && tv === 'mini') { mini.appendChild(root); }
    if (pv === 'away') {
      var sec = P().section('mini');
      if (sec) {
        if (tv === 'mini') { sec.style.borderTop = '1px solid var(--st-rule)'; }
        mini.appendChild(sec);
      }
    }
    placeMini();
    if (marker) { focusOn(marker); }
  }

  function removeMini() {
    if (mini && mini.parentNode) { mini.parentNode.removeChild(mini); }
    mini = null; drag = null;
  }

  /* ⚠️ DRAGGED BY THE HEADER, NEVER BY ITS BUTTONS. A press that starts on
     one of the four header buttons is that button's. */
  function onGripDown(e) {
    if (!mini || (e.button !== undefined && e.button !== 0)) { return; }
    if (e.target && e.target.closest && e.target.closest('button')) { return; }
    var r = mini.getBoundingClientRect();
    drag = { id: e.pointerId, dx: e.clientX - r.left, dy: e.clientY - r.top };
    try { e.currentTarget.setPointerCapture(e.pointerId); } catch (x) { /* ok */ }
    e.currentTarget.style.cursor = 'grabbing';
    e.preventDefault();
  }
  function onGripMove(e) {
    if (!drag || !mini || e.pointerId !== drag.id) { return; }
    miniPos = { x: e.clientX - drag.dx, y: e.clientY - drag.dy };
    placeMini();
    e.preventDefault();
  }
  function onGripUp(e) {
    if (!drag || e.pointerId !== drag.id) { return; }
    drag = null;
    if (e.currentTarget && e.currentTarget.style) { e.currentTarget.style.cursor = 'grab'; }
  }
  window.addEventListener('resize', function () { placeMini(); });

  // ── view changes (never state changes) ─────────────────────────────────

  function minimiseFull() {
    full = false;
    sync(pickerView() === 'board' ? 'tm-expand' : 'tools-expand');
  }
  function expandFull() {
    if (!root) { return; }
    full = true; hidden = false;
    sync('tm-toggle');
  }
  function expandMini() {
    var p = P();
    if (p && pickerView() === 'away') { full = false; p.restore(); return; }
    expandFull();
  }
  /* The Mini's X: the Mini AND its tools. The picker closes keeping its
     per-class STATE (as closing the board does); the timer stops and clears. */
  function closeAll() {
    var p = P();
    if (p && p.isOpen()) { p.close(); }
    close();
    sync();
  }

  // ── pop-out ────────────────────────────────────────────────────────────

  function pipOK() {
    return !pipBroken && ('documentPictureInPicture' in window) &&
           !!window.documentPictureInPicture &&
           typeof window.documentPictureInPicture.requestWindow === 'function';
  }

  function popOut() {
    if (!pipOK() || pipWin || pipPending) { return; }
    var p = P(), both = !!root && !!(p && p.isOpen()), req = null;
    /* ⚠️ INSIDE THE CLICK, BEFORE ANYTHING ELSE: the request needs the
       click's activation. */
    try {
      req = window.documentPictureInPicture.requestWindow(
        { width: 360, height: both ? 440 : 300 });
    } catch (e) { req = null; pipBroken = true; }
    /* The page side goes to the Mini first, so a refusal leaves the tools
       exactly where a teacher can still use them. */
    full = false;
    pipPending = !!req;
    if (p && pickerView() === 'board') { p.minimise(); } else { sync(); }
    if (!req) { return; }
    req.then(function (w) {
      pipPending = false;
      adoptPip(w);
    }, function () {
      pipPending = false; pipBroken = true;
      sync('tools-expand');
    });
  }

  function pipTitle() {
    var t = !!root, k = pickerView() === 'away';
    var name = t && k ? 'Class tools' : t ? 'Class timer' : 'Pick a student';
    var brand = (window.MrBadmusBrand && window.MrBadmusBrand.NAME) || 'MrBadmus';
    return name + ' | ' + brand;
  }

  function copyStyles(d) {
    var base = d.createElement('base');
    base.href = document.baseURI || location.href;
    d.head.appendChild(base);
    Array.prototype.forEach.call(document.styleSheets, function (ss) {
      try {
        var css = Array.prototype.map.call(ss.cssRules, function (r) {
          return r.cssText;
        }).join('\n');
        var st = d.createElement('style');
        st.textContent = css;
        d.head.appendChild(st);
      } catch (e) {
        if (ss.href) {
          var l = d.createElement('link');
          l.rel = 'stylesheet'; l.href = ss.href;
          d.head.appendChild(l);
        }
      }
    });
  }

  function mirrorTheme() {
    if (!pipWin) { return; }
    var a = document.documentElement, b = pipWin.document.documentElement;
    ['data-theme', 'data-theme-pref'].forEach(function (n) {
      if (a.hasAttribute(n)) { b.setAttribute(n, a.getAttribute(n)); }
      else { b.removeAttribute(n); }
    });
    b.style.colorScheme = a.style.colorScheme || '';
  }

  function adoptPip(w) {
    pipWin = w;
    var d = w.document;
    try { copyStyles(d); } catch (e) { /* unstyled beats nothing */ }
    mirrorTheme();
    try {
      pipObs = new MutationObserver(mirrorTheme);
      pipObs.observe(document.documentElement, {
        attributes: true, attributeFilter: ['data-theme', 'data-theme-pref', 'style']
      });
    } catch (e) { pipObs = null; }
    d.body.setAttribute('style', 'margin:0;height:100vh;display:flex;' +
                        'flex-direction:column;overflow:hidden;' +
                        'background:var(--st-ground);color:var(--st-ink);' +
                        'font-family:var(--st-ui)');
    w.addEventListener('pagehide', pipGone);
    if (keysOn) { attachKeys(w); }
    if (S.status === 'running') { startTick(); }
    sync();
  }

  function drawPip(tv, pv) {
    var d = pipWin.document, b = d.body, act = d.activeElement, marker = null;
    if (act && b.contains(act)) { marker = act.getAttribute('data-mrb-added'); }
    d.title = pipTitle();
    b.textContent = '';
    var head = el('div', 'flex:none;display:flex;align-items:center;' +
                         'justify-content:flex-end;gap:6px;padding:6px 8px;' +
                         'border-bottom:1px solid var(--st-rule);' +
                         'background:var(--st-paper)', 'tools-head');
    /* The brand, where the page carries its lockup partial
       (`shared/brand/brand.js`) — never a copy of the mark. As a plain span:
       a link in here would navigate the pop-out itself. */
    var B = window.MrBadmusBrand;
    if (B && B.lockup) {
      var wrap = el('div', 'flex:1;min-width:0;display:flex;align-items:center');
      wrap.innerHTML = B.lockup('/');
      var a = wrap.firstChild;
      if (a && a.tagName === 'A') {
        var sp = document.createElement('span');
        sp.className = a.className;
        while (a.firstChild) { sp.appendChild(a.firstChild); }
        wrap.replaceChild(sp, a);
      }
      head.appendChild(wrap);
    }
    head.appendChild(muteBtn('tools-mute'));
    head.appendChild(button('tools-back', ICON_BTN, 'popin', null,
                            'Back to page', pipBack));
    b.appendChild(head);
    var main = el('div', 'flex:1 1 0;min-height:0;display:flex;' +
                         'flex-direction:column', 'tools-pip');
    main.setAttribute('data-mrb-tools', 'pip');
    if (root && tv === 'pip') { main.appendChild(root); }
    if (pv === 'away') {
      var sec = P().section('pip');
      if (sec) {
        if (tv === 'pip') { sec.style.borderTop = '1px solid var(--st-rule)'; }
        main.appendChild(sec);
      }
    }
    b.appendChild(main);
    if (marker) {
      var n = b.querySelector('[data-mrb-added="' + marker + '"]');
      if (n && n.focus) { try { n.focus(); } catch (e) { /* ok */ } }
    }
  }

  /* The pop-out is gone — by "Back to page", or the teacher's own X
     (`pagehide`). Everything comes back to the page as the Mini, with the
     state untouched: the nodes are moved home before the window's document
     goes, any reveal in flight is landed, and the ticker moves to this
     page's timers. */
  function pipGone() {
    if (!pipWin) { return; }
    var w = pipWin;
    pipWin = null;
    if (pipObs) { try { pipObs.disconnect(); } catch (e) { /* ok */ } pipObs = null; }
    try { w.removeEventListener('pagehide', pipGone); } catch (e) { /* ok */ }
    detachKeys(w);
    full = false;
    var p = P();
    if (p && p.settle) { p.settle(); }
    if (root && root.ownerDocument !== document) {
      try { document.adoptNode(root); } catch (e) { /* appendChild adopts */ }
    }
    if (S.status === 'running') { startTick(); }
    Object.keys(H).forEach(function (k) { clearHold(H[k]); });
    H = {};
    sync('tools-expand');
  }

  function pipBack() {
    var w = pipWin;
    pipGone();
    if (w) { try { w.close(); } catch (e) { /* ok */ } }
  }

  // ── open, close ────────────────────────────────────────────────────────

  function open(opts) {
    opts = opts || {};
    /* The page's own Timer button, pressed while popped out: the teacher is
       asking for the timer HERE, so the tools come back to the page first. */
    if (pipWin && opts.view === 'full') { pipBack(); }
    var wantFull = !(opts.view === 'dock' || opts.view === 'float' ||
                     opts.view === 'mini');
    var wasOpen = !!root;
    if (!wasOpen) {
      var a = document.activeElement;
      prevFocus = (a && a !== document.body) ? a : null;
      root = el('div', 'display:none', 'tm-root');
      root.setAttribute('data-tm', 'overlay');
      tbody = el('div', 'display:contents');
      liveNode = el('div', SR, 'tm-live');
      liveNode.setAttribute('role', 'status');
      liveNode.setAttribute('aria-live', 'polite');
      liveNode.setAttribute('aria-atomic', 'true');
      root.appendChild(tbody);
      root.appendChild(liveNode);
      document.body.appendChild(root);
    }
    hidden = false;
    opens += 1;
    root.setAttribute('data-tm-opens', String(opens));
    /* A second open never DEMOTES: asking for the dock while the full view
       is up leaves the full view up. Asking for full promotes. While popped
       out, it all goes to the pop-out. */
    full = pipWin ? false : ((wasOpen && full) ? true : wantFull);
    sync(full ? 'tm-toggle' : null);
  }

  function close() {
    if (!root) { return; }
    stopTick();
    if (root.parentNode) { root.parentNode.removeChild(root); }
    root = tbody = liveNode = digitsNode = null;
    var wasFull = view === 'full';
    view = null; hidden = false; full = false;
    /* Back to a clean idle at the same length; mute and the last preset are
       kept, in memory, for the next open. */
    S.status = 'idle';
    S.ms = S.mode === 'down' ? S.preset : 0;
    lastSaid = null;
    sync();
    if (wasFull && prevFocus && document.contains(prevFocus)) {
      try { prevFocus.focus(); } catch (e) { /* ok */ }
    }
    prevFocus = null;
  }

  // ── keyboard: the full-screen timer's own keys, and the clicker ────────

  /* ONE capture-phase keydown/keyup pair on `window` — and on the pop-out's
     window while it is open, because key events go to whichever window has
     focus — attached while the picker is live OR the timer exists (shown,
     hidden or running) and detached when neither is. Capture +
     stopPropagation on the keys it handles is what keeps one keypress from
     also reaching the picker's own Escape handler or a focused button.

     CLICKER KEYS (a presentation clicker sends keyboard keys):
       forward  PageDown, ArrowRight, Space   → pick the next name (on the
                board, in the Mini or in the pop-out); or, with no picker (or
                a full-screen timer covering it), start/pause the timer.
       back     PageUp, ArrowLeft             → start/pause the timer (opened
                docked if it is not showing). NEVER touches the pick.
       hold either for ~900 ms                → a cheer, once, and nothing else.
       blank    B or "."                      → show/hide the timer; hiding
                does not stop it.
     F5 is never looked at. Escape on the page keeps its old meaning; Escape in
     the pop-out does nothing. Nothing is taken while focus is in an input,
     textarea, select or contenteditable, nor with Ctrl/Meta/Alt held.

     ⚠️ SHORT ACTIONS HAPPEN ON RELEASE. A press can turn into a hold, and a
     hold must never also pick. Clickers repeat in two styles — real
     `e.repeat` auto-repeat, or discrete down/up pairs a few tens of ms apart
     — so a release arms a 150 ms window: a new keydown of the same key inside
     it is the same hold continuing, otherwise the short action runs once. */

  var HOLD_MS = 900, GAP_MS = 150;
  var FWD = { 'PageDown': 1, 'ArrowRight': 1, ' ': 1 };
  var BACK = { 'PageUp': 1, 'ArrowLeft': 1 };
  var picker = null;                 // {pick(): true|'busy'|'off'} while live
  var H = {};                        // key -> hold state
  var keysOn = false, keyWins = [], statusNode = null, cheers = 0,
      cheerNode = null, cheerTimer = null, noise = null;

  function typing(t) {
    var tag = t && t.tagName;
    return tag === 'INPUT' || tag === 'TEXTAREA' || tag === 'SELECT' ||
           !!(t && t.isContentEditable);
  }
  /* ⚠️ SPACE ON SOMEBODY ELSE'S BUTTON IS THAT BUTTON'S. With the picker
     closed and a timer in the Mini, the teacher is using the PAGE: a focused
     link or button on it must still activate with Space, as it does with no
     timer at all. Only Space is given back — it is the key that presses a
     focused control; the arrow and Page keys a clicker sends stay the
     clicker's. Inside the tools (the timer, the Mini, the pop-out), Space
     stays a clicker key (its keyup is swallowed, so a focused control there
     is not also pressed). */
  function pageControl(e) {
    if (picker || e.key !== ' ') { return false; }
    var t = e.target;
    if (!t || !t.closest || t.ownerDocument !== document) { return false; }
    if ((root && root.contains(t)) || (mini && mini.contains(t))) { return false; }
    return !!t.closest('button,a[href],summary,[role="button"],[role="link"],' +
                       '[role="tab"],[role="checkbox"],[role="switch"]');
  }
  function kindOf(e) {
    var k = e.key;
    if (k === 'Spacebar' || (k === undefined && e.code === 'Space')) { k = ' '; }
    if (FWD[k]) { return 'fwd'; }
    if (BACK[k]) { return 'back'; }
    if (k === 'b' || k === 'B' || k === '.') { return 'blank'; }
    return null;
  }
  function keyId(e) { return e.key === 'Spacebar' ? ' ' : e.key; }

  function attachKeys(w) {
    if (keyWins.indexOf(w) !== -1) { return; }
    try {
      w.addEventListener('keydown', onKey, true);
      w.addEventListener('keyup', onKeyUp, true);
      keyWins.push(w);
    } catch (e) { /* a window that is going */ }
  }
  function detachKeys(w) {
    var i = keyWins.indexOf(w);
    if (i === -1) { return; }
    keyWins.splice(i, 1);
    try {
      w.removeEventListener('keydown', onKey, true);
      w.removeEventListener('keyup', onKeyUp, true);
    } catch (e) { /* gone */ }
  }

  function syncKeys() {
    var want = !!(picker || root);
    if (want) {
      if (!keysOn) {
        keysOn = true;
        statusNode = el('div', SR, 'clicker-status');
        statusNode.setAttribute('role', 'status');
        statusNode.setAttribute('aria-live', 'polite');
        statusNode.setAttribute('data-cheers', String(cheers));
        document.body.appendChild(statusNode);
      }
      attachKeys(window);
      if (pipWin) { attachKeys(pipWin); }
    } else if (keysOn) {
      keysOn = false;
      keyWins.slice().forEach(detachKeys);
      Object.keys(H).forEach(function (k) { clearHold(H[k]); });
      H = {};
      if (statusNode && statusNode.parentNode) { statusNode.parentNode.removeChild(statusNode); }
      statusNode = null;
      endCheer();
    }
  }

  function clearHold(st) {
    if (st.holdTimer) { cancel(st.holdTimer); st.holdTimer = null; }
    if (st.gapTimer) { cancel(st.gapTimer); st.gapTimer = null; }
  }

  // ── the cheer: a clap in Web Audio and a CSS-only flash ────────────────

  function clap() {
    ensureAudio();
    if (!audio) { return; }
    try {
      if (!noise) {
        var n = Math.floor(audio.sampleRate * 0.12);
        noise = audio.createBuffer(1, n, audio.sampleRate);
        var d = noise.getChannelData(0);
        for (var i = 0; i < n; i++) { d[i] = Math.random() * 2 - 1; }
      }
      var t0 = audio.currentTime + 0.02;
      for (var j = 0; j < 14; j++) {
        var at = t0 + j * 0.075 + Math.random() * 0.04;
        var src = audio.createBufferSource(), f = audio.createBiquadFilter(),
            g = audio.createGain();
        src.buffer = noise;
        f.type = 'bandpass';
        f.frequency.value = 1200 + Math.random() * 1800;
        f.Q.value = 0.9;
        g.gain.setValueAtTime(0.0001, at);
        g.gain.exponentialRampToValueAtTime(0.5, at + 0.005);
        g.gain.exponentialRampToValueAtTime(0.0001, at + 0.11);
        src.connect(f); f.connect(g); g.connect(audio.destination);
        src.start(at);
      }
    } catch (e) { /* silence beats a broken clicker */ }
  }

  function endCheer() {
    if (cheerTimer) { cancel(cheerTimer); cheerTimer = null; }
    if (cheerNode && cheerNode.parentNode) { cheerNode.parentNode.removeChild(cheerNode); }
    cheerNode = null;
  }

  /* Shown where the tools are: in the pop-out while it is open. */
  function cheer() {
    cheers += 1;
    if (statusNode) {
      statusNode.setAttribute('data-cheers', String(cheers));
      statusNode.textContent = 'Well done';
    }
    if (!S.muted) { clap(); }
    endCheer();
    var still = false;
    try { still = !!(window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches); }
    catch (e) { /* motion allowed */ }
    var n = el('div', 'position:fixed;inset:0;z-index:' + (ZMINI + 1) +
               ';pointer-events:none;overflow:hidden', 'clicker-cheer');
    n.setAttribute('aria-hidden', 'true');
    n.setAttribute('data-still', still ? '1' : '0');
    if (still) {
      /* Reduced motion: one static flash, no movement. */
      n.appendChild(el('div', 'position:absolute;inset:0;opacity:.3;' +
                      'box-shadow:inset 0 0 0 14px var(--st-accent)'));
    } else {
      var st = document.createElement('style');
      st.textContent =
        '@keyframes mrbCheerRing{from{transform:translate(-50%,-50%) scale(.15);opacity:.9}' +
        'to{transform:translate(-50%,-50%) scale(1.5);opacity:0}}' +
        '@keyframes mrbCheerFall{from{transform:translateY(-12vh) rotate(0);opacity:1}' +
        'to{transform:translateY(112vh) rotate(540deg);opacity:.9}}';
      n.appendChild(st);
      for (var r = 0; r < 3; r++) {
        n.appendChild(el('div', 'position:absolute;left:50%;top:50%;' +
          'width:80vmin;height:80vmin;border-radius:50%;' +
          'border:10px solid var(--st-accent);' +
          'animation:mrbCheerRing 1.3s ease-out ' + (r * 0.22) + 's both'));
      }
      var cols = ['var(--st-accent)', 'var(--st-accent-text)', 'var(--st-ink)',
                  'var(--st-chip-tint-border)'];
      for (var c = 0; c < 20; c++) {
        n.appendChild(el('div', 'position:absolute;top:0;left:' + (3 + c * 4.8) +
          '%;width:10px;height:22px;border-radius:3px;background:' + cols[c % 4] +
          ';animation:mrbCheerFall ' + (1.1 + (c % 5) * 0.08) + 's ease-in ' +
          ((c % 7) * 0.06) + 's both'));
      }
    }
    (pipWin ? pipWin.document.body : document.body).appendChild(n);
    cheerNode = n;
    cheerTimer = later(endCheer, 1500);
  }

  // ── what a short press does ────────────────────────────────────────────

  function covering() { return !!(root && view === 'full' && !hidden); }

  function showTimer() {
    if (!root) { open({ view: 'dock' }); return; }
    if (hidden) { hidden = false; sync(); }
  }

  function toggleHidden() {
    if (!root) { open({ view: 'dock' }); return; }
    hidden = !hidden;
    say(hidden ? 'Timer hidden' : 'Timer shown');
    sync();
  }

  function shortAction(kind) {
    if (kind === 'fwd') {
      if (picker && !covering()) { picker.pick(); return; }
      if (!root) { return; }
      showTimer(); toggle(); return;
    }
    /* back: the timer, never the pick. */
    showTimer();
    toggle();
  }

  function onKey(e) {
    if (e.key === 'F5') { return; }
    var inPage = !e.view || e.view === window ||
                 (e.target && e.target.ownerDocument === document);
    if ((e.key === 'Escape' || e.keyCode === 27) && inPage && covering()) {
      /* Handled and STOPPED: the picker's own Escape handler is on
         `document`, later in the path, and must not see this keypress. */
      e.stopPropagation(); e.preventDefault();
      if (S.status === 'running' || S.status === 'paused') { minimiseFull(); }
      else { close(); }
      return;
    }
    if (e.key === 'Tab' && inPage && covering()) {
      var f = root.querySelectorAll('button:not([aria-disabled="true"]),input');
      if (!f.length) { return; }
      var first = f[0], last = f[f.length - 1], a = document.activeElement;
      if (e.shiftKey && (a === first || !root.contains(a))) {
        e.preventDefault(); last.focus();
      } else if (!e.shiftKey && (a === last || !root.contains(a))) {
        e.preventDefault(); first.focus();
      }
      return;
    }
    var kind = kindOf(e);
    if (!kind || typing(e.target) || pageControl(e) ||
        e.ctrlKey || e.metaKey || e.altKey) { return; }
    e.preventDefault(); e.stopPropagation();
    if (kind === 'blank') { if (!e.repeat) { toggleHidden(); } return; }
    var id = keyId(e), st = H[id];
    if (e.repeat) { return; }                 // confirms the hold; nothing to do
    if (st && (st.gapTimer)) {                // same key again inside the gap
      cancel(st.gapTimer); st.gapTimer = null;
      return;
    }
    if (st) { clearHold(st); }                // a stale entry: start over
    st = H[id] = { kind: kind, consumed: false, holdTimer: null, gapTimer: null };
    st.holdTimer = later(function () {
      st.holdTimer = null; st.consumed = true; cheer();
    }, HOLD_MS);
  }

  function onKeyUp(e) {
    if (e.key === 'F5') { return; }
    var kind = kindOf(e);
    if (!kind || typing(e.target) || pageControl(e) ||
        e.ctrlKey || e.metaKey || e.altKey) { return; }
    e.preventDefault(); e.stopPropagation();
    if (kind === 'blank') { return; }
    var id = keyId(e), st = H[id];
    if (!st) { return; }
    if (st.gapTimer) { cancel(st.gapTimer); }
    st.gapTimer = later(function () {
      st.gapTimer = null;
      clearHold(st);
      if (H[id] === st) { delete H[id]; }
      if (!st.consumed) { shortAction(st.kind); }
    }, GAP_MS);
  }

  window.MrBadmusTimer = {
    open: open,
    close: close,
    isOpen: function () { return !!root; },
    isShown: function () { return !!root && !hidden; },
    /* Where the timer is drawn: null | full | strip | mini | pip | hidden. */
    view: function () { return view; },
    /* The picker registers itself while it is live (board, Mini or pop-out)
       so the clicker's forward keys can pick. `p.pick()` returns true
       (picked), 'busy' (a reveal is still spinning) or 'off'. */
    setPicker: function (p) { picker = p || null; syncKeys(); },
    /* Re-run the one layout rule. The picker calls it whenever it draws its
       board (the strip docks into the board's new slot), minimises,
       restores or closes. */
    sync: function (focusMarker) { sync(focusMarker); },
    /* ONE mute for the picker's cheer and the timer's beeps. Memory only. */
    muted: function () { return S.muted; },
    setMuted: function (b) { S.muted = !!b; sync(); },
    canPopOut: pipOK,
    popOut: popOut,
    isPopped: function () { return !!pipWin; },
    /* Back to the page from the pop-out (as its "Back to page" does). */
    popIn: function () { if (pipWin) { pipBack(); } },
    /* Timers on the window the tools are shown in (see `later`). */
    later: later,
    cancel: cancel,
    icon: function (name) { return ICONS[name] || ''; },
    /* Subscribe to open / close / view / state changes; returns an
       unsubscribe function. The picker uses it to keep its Timer button
       honest. */
    onChange: function (fn) {
      listeners.push(fn);
      return function () {
        var i = listeners.indexOf(fn);
        if (i !== -1) { listeners.splice(i, 1); }
      };
    }
  };
}());
