/* shared/teacher-picker.js — MRB-323, 5 Sep 2026.

   A random name picker, per class, for the front of a classroom.

   ══ WHAT IT IS ═════════════════════════════════════════════════════════

   `window.MrBadmusPicker.open({id, code, students})` puts a full-screen
   board display over the page: a name at the display scale, a Pick button,
   a no-repeats cycle with a visible count, a pure-random alternative, and a
   session-only absent list.

   ══ WHAT IT IS NOT ═════════════════════════════════════════════════════

   ⛔ IT WRITES NOTHING. Not to the database, not to `localStorage`, not to
   `sessionStorage`, not to a cookie. There is no `fetch`, no Supabase
   client and no storage API anywhere in this file, deliberately and
   checkably: who was picked and who was away is a fact about one lesson in
   one room, and a platform that recorded it would be keeping an attendance
   register nobody asked it to keep and no teacher had a chance to correct.
   `STATE` below is a plain object in this closure. Reload the page and it
   is gone, which is the intended lifetime.

   ⛔ IT READS NO ROSTER OF ITS OWN. The caller hands it the students it has
   already loaded and already shown — `rosterFor(klass())` on the generated
   class screen, `loadClassMatrices()[cid].members` on Today. So the pool
   can never disagree with the names on the page behind it, and the picker
   adds not one query. It also means the permission question is already
   answered: a caller that could not read the class could not have a roster
   to pass, and neither surface renders at all without one.

   ══ WHERE IT MOUNTS, AND WHY THAT MATTERS ══════════════════════════════

   ⚠️ INTO `#mrb-teacher` WHEN THAT HOST EXISTS, not into `document.body`.
   The generated teacher pages are drawn by `student-runtime` into that host,
   and both of the port's drive gates scope themselves to it —
   `teacher_behaviour.py` sweeps `host.querySelectorAll('[data-dc-tpl],
   [data-mrb-added])` and `teacher_reach.py` does the same inside its
   `modalRoot()`. An overlay hung off `document.body` would be invisible to
   both: the press that opened it would be recorded as changing nothing (a
   DEAD control, which is exactly the finding those gates exist to make) and
   nothing inside it would ever be hit-tested at 390px.

   Every control here therefore carries a `data-mrb-added` marker, so both
   gates see it, press it and measure it. Only the ENTRY button is in
   `teacher_rulings.AMENDED_ADDITIONS` — that register is asserted against
   the emitted BYTES of a page, and these elements do not exist until a
   teacher presses something.

   ⚠️ THE OVERLAY IS `position:fixed;inset:0`, so being a descendant of the
   host does not constrain it: it covers the viewport either way, and
   `teacher_reach.modalRoot()` recognises it as the modal (it looks for a
   fixed element at 90%+ of the viewport, sized rather than named).

   ⚠️ AND THE HOST CAN BE WIPED UNDER IT. `student-runtime`'s `draw()` does
   `host.textContent = ''` on every `setState`, so a redraw takes the
   overlay with it. A teacher cannot cause that while the overlay is up —
   the overlay covers every control that could — but a gate's synthetic
   `.click()` can, and an in-flight toast timer could. `STATE` lives outside
   the DOM for that reason: the cycle, the mode and the absent list survive,
   and reopening resumes rather than restarts.

   ══ THE DOM ORDER IS NOT THE VISUAL ORDER, ON PURPOSE ═══════════════════

   The three panels are appended stage → footer → header and put back in
   visual order with `order`. `teacher_behaviour.py` walks controls by
   ORDINAL (`list[j]`, re-queried each iteration), so a close button first
   in the DOM is pressed first — it would shut the overlay before the sweep
   had reached the Pick button, the mode toggle, the reset or a single
   absent chip, and every one of them would ship unpressed by any gate. Last
   in the DOM, the close is the last thing pressed and everything above it
   is swept on the way. Tab order follows the DOM too, which puts the
   primary action first and the dismissal last — the right order for this
   surface anyway.
*/
(function () {
  'use strict';

  /* ── session state, in memory, for the life of this page load ──────────
     `{classId: {mode, absent:{id:1}, picked:{id:1}, last:{id,name}}}`.
     No serialisation, no persistence, no key anywhere outside this line. */
  var STATE = {};

  var live = null;      // {el, opts, pool, timer} while open, else null
  var keyHandler = null;

  /* ── Design's v3 tokens, off the pages this sits on ────────────────────
     Every colour, face and radius below is a `--st-*` custom property from
     `shared/teacher-ds.css`; nothing here invents a value. The registers are
     taken from controls Design drew on the class screen: her action-row
     buttons (nodes 214-217) for the two button weights, her `--st-mono`
     uppercase caption for the counts, her h1 (node 219) for the name. */
  var GROUND = 'var(--st-ground)';

  /* ⚠️ OPAQUE, NOT A SCRIM, and this is the one place the picker leaves
     Design's overlay idiom. Her three sheets dim the page behind them
     (`rgba(26,23,20,.45)`) because they are dialogs you look INTO. This is
     a board display projected at a wall: a name over a half-lit dashboard
     is a name read against thirty rows of other children's marks. */
  var OVERLAY = 'position:fixed;inset:0;z-index:90;background:' + GROUND +
                ';display:flex;flex-direction:column;overflow:hidden';

  var HEAD = 'order:1;flex:none;display:flex;align-items:center;' +
             'justify-content:space-between;gap:12px;padding:14px 20px;' +
             'border-bottom:1px solid var(--st-rule)';
  /* ⛔ NO `text-transform`, AND THE REST OF THE ESTATE HAS THE SAME NOTE.
     Design's mono caption register is uppercase, and every OTHER use of it
     here follows her — but those are LABELS ("Week", "Picked 3 of 28"). This
     one is a class's NAME, and MRB-263 makes a class name mixed-case on
     purpose: `8r/Sc1`, `10h/Ph1`, `11r/Sc1`. Uppercasing it prints `8R/SC1`
     on the wall, which is not what the class is called anywhere else in the
     product. `teacher/today.html` carries the identical warning over its own
     three lesson lines. */
  var HEAD_CODE = 'min-width:0;overflow:hidden;text-overflow:ellipsis;' +
                  'white-space:nowrap;font:500 14px/1.2 var(--st-mono);' +
                  'letter-spacing:.08em;color:var(--st-caption)';
  /* Design's close X (node 520) at 32px, taken to 40px: 40 is the height of
     every button in her class-screen action row, and it is this file's
     floor for anything a finger has to find. */
  var HEAD_X = 'flex:none;width:40px;height:40px;display:flex;' +
               'align-items:center;justify-content:center;' +
               'background:transparent;border:1px solid var(--st-btn-border);' +
               'border-radius:9px;cursor:pointer;color:var(--st-muted)';

  var STAGE = 'order:2;flex:1;min-height:0;overflow:auto;display:flex;' +
              'flex-direction:column;align-items:center;' +
              'justify-content:center;gap:28px;padding:24px 20px;' +
              'text-align:center';

  /* Design's own h1 face and tracking (node 219, `600 52px/1 var(--st-display)`
     with `letter-spacing:-0.035em`), scaled to the surface: 52px is the top
     of the page type scale and the FLOOR here, because the thing this has to
     survive is a projector and the back row. `9vw` reaches 132px on a
     1460px board and falls to 38px on a 390px phone, where nobody is
     projecting anything. */
  var NAME = 'max-width:100%;font:600 clamp(38px,9vw,132px)/1.02 ' +
             'var(--st-display);letter-spacing:-0.035em;color:var(--st-ink);' +
             'overflow-wrap:break-word;word-break:break-word';

  /* Design's primary action (node 214), at 40px → 60px. The only control on
     this screen a teacher presses from three metres away. */
  var PICK = 'flex:none;min-height:60px;padding:0 34px;' +
             'font:600 22px/1.2 var(--st-ui);color:var(--st-paper);' +
             'background:var(--st-accent-text);border:none;border-radius:11px;' +
             'cursor:pointer';
  var PICK_OFF = 'flex:none;min-height:60px;padding:0 34px;' +
                 'font:600 22px/1.2 var(--st-ui);color:var(--st-caption);' +
                 'background:var(--st-paper);' +
                 'border:1px solid var(--st-btn-border);border-radius:11px;' +
                 'cursor:not-allowed';

  var FOOT = 'order:3;flex:none;max-height:60vh;overflow-y:auto;' +
             'padding:14px 20px;border-top:1px solid var(--st-rule);' +
             'background:var(--st-paper)';
  var FOOT_ROW = 'display:flex;align-items:center;flex-wrap:wrap;gap:12px';
  var COUNT = 'font:500 13px/1.2 var(--st-mono);letter-spacing:.16em;' +
              'text-transform:uppercase;color:var(--st-caption)';

  /* Design's segmented trough (`--st-seg-bg`), the same idiom her day bar
     and pathway toggles use. */
  var SEG = 'display:flex;gap:3px;padding:3px;background:var(--st-seg-bg);' +
            'border-radius:10px';
  var SEG_ON = 'min-height:40px;padding:0 14px;font:600 15px/1.2 ' +
               'var(--st-ui);color:var(--st-ink);background:var(--st-paper);' +
               'border:none;border-radius:8px;cursor:pointer';
  var SEG_OFF = 'min-height:40px;padding:0 14px;font:600 15px/1.2 ' +
                'var(--st-ui);color:var(--st-caption);background:transparent;' +
                'border:none;border-radius:8px;cursor:pointer';

  /* Design's low-emphasis text button (node 213's "Back to <class>"), given
     the 40px floor a bare text button does not have. */
  var TEXT_BTN = 'flex:none;min-height:40px;padding:0 4px;' +
                 'font:600 14.5px/1.2 var(--st-ui);color:var(--st-muted);' +
                 'background:none;border:none;cursor:pointer';

  var CHIPS = 'display:flex;flex-wrap:wrap;gap:8px;margin-top:12px';
  var CHIP_IN = 'min-height:40px;padding:0 13px;font:500 15px/1.2 ' +
                'var(--st-ui);color:var(--st-ink);background:var(--st-paper);' +
                'border:1px solid var(--st-btn-border);border-radius:9px;' +
                'cursor:pointer';
  var CHIP_OUT = 'min-height:40px;padding:0 13px;font:500 15px/1.2 ' +
                 'var(--st-ui);color:var(--st-caption);' +
                 'background:var(--st-seg-bg);' +
                 'border:1px solid var(--st-rule-strong);border-radius:9px;' +
                 'cursor:pointer;text-decoration:line-through';

  // ── little DOM helpers ─────────────────────────────────────────────────

  function el(tag, style, marker) {
    var n = document.createElement(tag);
    if (style) { n.setAttribute('style', style); }
    if (marker) { n.setAttribute('data-mrb-added', marker); }
    if (tag === 'button') { n.type = 'button'; }
    return n;
  }

  function text(node, s) { node.textContent = s; return node; }

  /* ⚠️ NEVER `innerHTML` WITH A CHILD'S NAME. Every name on this surface
     arrives from `profiles.first_name` / `last_name`, which is user-entered
     text this file has no business trusting. `textContent` throughout. */

  // ── the pool ───────────────────────────────────────────────────────────

  /* Both callers' row shapes, normalised once. `rosterFor()` gives
     `{id, name, …}`; `loadClassMatrices().members` gives
     `{student_id, first_name, last_name, …}`. A row with no usable name is
     dropped rather than shown as a blank: you cannot call on a child whose
     name the picker does not know, and a blank slot in a cycle would be a
     turn that silently belongs to nobody. */
  function normalise(rows) {
    var out = [], seen = {};
    (rows || []).forEach(function (r) {
      if (!r) { return; }
      var id = r.id || r.student_id;
      var name = r.name ||
                 [r.first_name, r.last_name].filter(Boolean).join(' ');
      name = String(name || '').trim();
      if (!id || !name || seen[id]) { return; }
      seen[id] = 1;
      out.push({ id: String(id), name: name });
    });
    return out;
  }

  function sessionFor(classId) {
    if (!STATE[classId]) {
      STATE[classId] = { mode: 'cycle', absent: {}, picked: {}, last: null };
    }
    return STATE[classId];
  }

  /* The three sets every line on this screen is derived from. Recomputed on
     every draw rather than cached, because a student can be marked absent
     after being picked and the count has to stay honest when they are:
     `done` is intersected with `present`, so N can never exceed M. */
  function sets(pool, s) {
    var present = pool.filter(function (p) { return !s.absent[p.id]; });
    var done = present.filter(function (p) { return s.picked[p.id]; });
    var left = present.filter(function (p) { return !s.picked[p.id]; });
    return { present: present, done: done, left: left };
  }

  // ── the reveal ─────────────────────────────────────────────────────────

  function reduced() {
    try {
      return window.matchMedia &&
             window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    } catch (e) { return false; }
  }

  function stopReveal() {
    if (live && live.timer) { clearTimeout(live.timer); live.timer = null; }
  }

  /* ⚠️ THE WINNER IS DECIDED BEFORE THE ANIMATION, NEVER BY IT. The shuffle
     is decoration over a result that already exists, so an interrupted or
     switched-off animation cannot change who was picked — and the
     reduced-motion branch is the same pick, shown immediately, rather than
     a different code path with its own chance of disagreeing.

     ⚠️ KEPT SHORT ON PURPOSE (~700ms). `teacher_behaviour.py` decides
     whether a press did anything by comparing the host's text before and
     after, so text that keeps changing on a timer is text that could make
     some OTHER dead control look alive. Under a second, over one press in a
     twenty-minute sweep, is the smallest window this can be given while
     still reading as a draw rather than a jump. */
  /* ⚠️ `aria-busy` IS UP WHILE THE NAMES ARE STILL MOVING, AND IT IS NOT
     DECORATION. The name slot is an `aria-live` region, and a live region
     announced ten times in seven hundred milliseconds reads a class list at
     a teacher instead of a name — `aria-busy` is the attribute that says
     "not yet" and the one a screen reader waits on.

     It is ALSO the only honest way to drive this. `teacher_picker_drive.py`
     has to know which name was PICKED, and its first version polled until
     the text stopped changing: the last shuffle frames are 140ms apart and
     the poll was 60ms, so two consecutive reads landed on the same DECOY
     and the gate reported repeats a correct picker had not made. A drive
     that has to guess when an animation ended will eventually guess wrong;
     the page says so instead. */
  function reveal(nameNode, winner, pool) {
    stopReveal();
    function land() {
      text(nameNode, winner.name);
      nameNode.removeAttribute('aria-busy');
    }
    if (reduced() || pool.length < 2) { land(); return; }
    nameNode.setAttribute('aria-busy', 'true');
    var i = 0, FRAMES = 10;
    (function step() {
      if (!live || !document.contains(nameNode)) { return; }
      if (i >= FRAMES) { land(); live.timer = null; return; }
      text(nameNode, pool[Math.floor(Math.random() * pool.length)].name);
      i += 1;
      live.timer = setTimeout(step, 30 + i * i * 1.1);
    })();
  }

  // ── draw ───────────────────────────────────────────────────────────────

  function draw() {
    if (!live) { return; }
    stopReveal();
    var root = live.el, opts = live.opts, pool = live.pool;
    var s = sessionFor(opts.id);
    var g = sets(pool, s);
    var cycling = s.mode === 'cycle';

    root.textContent = '';

    // ── stage (first in the DOM, second on the screen) ─────────────────
    var stage = el('div', STAGE);
    var nameNode = el('div', NAME);
    nameNode.setAttribute('data-mrb-name', '1');
    nameNode.setAttribute('aria-live', 'polite');
    /* The resting state is named in the footer, not here: an empty slot
       above the button says nothing a teacher has to read, and a line of
       copy explaining what the button does would be the meta-text this
       surface has none of. `s.last` survives a reopen, so coming back to a
       class shows the name it was left on. */
    if (s.last) { text(nameNode, s.last.name); }
    stage.appendChild(nameNode);

    var exhausted = cycling ? g.left.length === 0 : g.present.length === 0;
    var pick = el('button', exhausted ? PICK_OFF : PICK, 'pick-go');
    /* ⚠️ A SPENT BUTTON SAYS SO. Dimming it and leaving it reading "Pick
       again" makes the reader join two things up — a greyed control here and
       a count in the footer — to work out why nothing happens. Looked at on
       a 1460px board, that is exactly how it read. The three labels are the
       three states, and "Start again" in the footer is the way on. */
    text(pick, exhausted ? (g.present.length ? 'Everyone picked' : 'Nobody here')
                         : (s.last ? 'Pick again' : 'Pick a student'));
    if (exhausted) {
      pick.setAttribute('aria-disabled', 'true');
    } else {
      pick.addEventListener('click', function () {
        var from = cycling ? g.left : g.present;
        if (!from.length) { return; }
        var winner = from[Math.floor(Math.random() * from.length)];
        if (cycling) { s.picked[winner.id] = 1; }
        s.last = winner;
        draw();
        reveal(root.querySelector('[data-mrb-name]') || nameNode,
               winner, g.present);
      });
    }
    stage.appendChild(pick);
    root.appendChild(stage);

    // ── footer ─────────────────────────────────────────────────────────
    var foot = el('div', FOOT);
    var row = el('div', FOOT_ROW);

    var count = el('div', COUNT);
    if (!g.present.length) {
      text(count, 'Nobody in the pool');
    } else if (cycling) {
      text(count, 'Picked ' + g.done.length + ' of ' + g.present.length);
    } else {
      text(count, g.present.length + ' in the pool');
    }
    row.appendChild(count);

    var seg = el('div', SEG + ';margin-left:auto');
    [['cycle', 'No repeats'], ['random', 'Random']].forEach(function (m) {
      var b = el('button', s.mode === m[0] ? SEG_ON : SEG_OFF,
                 'pick-mode-' + m[0]);
      text(b, m[1]);
      b.setAttribute('aria-pressed', s.mode === m[0] ? 'true' : 'false');
      b.addEventListener('click', function () { s.mode = m[0]; draw(); });
      seg.appendChild(b);
    });
    row.appendChild(seg);

    /* Only when there is something to reset. A control that is on the
       screen before it can do anything is a control whose first press does
       nothing — which is both a worse surface and, on this port, a gate
       failure with an accurate name for it. */
    if (cycling && g.done.length) {
      var reset = el('button', TEXT_BTN, 'pick-reset');
      text(reset, 'Start again');
      reset.addEventListener('click', function () { s.picked = {}; draw(); });
      row.appendChild(reset);
    }
    foot.appendChild(row);

    // ── absent, this lesson only ───────────────────────────────────────
    var away = pool.filter(function (p) { return s.absent[p.id]; }).length;
    var open = el('button', TEXT_BTN, 'pick-absent');
    text(open, away ? 'Absent today · ' + away : 'Absent today');
    open.setAttribute('aria-expanded', live.absentOpen ? 'true' : 'false');
    open.addEventListener('click', function () {
      live.absentOpen = !live.absentOpen;
      draw();
    });
    var openRow = el('div', 'margin-top:10px');
    openRow.appendChild(open);
    foot.appendChild(openRow);

    if (live.absentOpen) {
      var chips = el('div', CHIPS);
      pool.forEach(function (p) {
        var out = !!s.absent[p.id];
        var c = el('button', out ? CHIP_OUT : CHIP_IN, 'pick-absent-row');
        text(c, p.name);
        c.setAttribute('aria-pressed', out ? 'true' : 'false');
        c.addEventListener('click', function () {
          if (s.absent[p.id]) { delete s.absent[p.id]; }
          else { s.absent[p.id] = 1; }
          draw();
        });
        chips.appendChild(c);
      });
      foot.appendChild(chips);
    }
    root.appendChild(foot);

    // ── header (last in the DOM, first on the screen — see the note up top)
    var head = el('div', HEAD);
    var code = el('div', HEAD_CODE);
    code.setAttribute('data-mrb-code', '1');
    text(code, opts.code || 'Class');
    head.appendChild(code);
    var x = el('button', HEAD_X, 'pick-close');
    x.setAttribute('aria-label', 'Close');
    x.innerHTML = '<svg width="14" height="14" viewBox="0 0 14 14" ' +
                  'fill="none" aria-hidden="true"><path d="M2 2l10 10M12 2' +
                  'L2 12" stroke="currentColor" stroke-width="1.6" ' +
                  'stroke-linecap="round"/></svg>';
    x.addEventListener('click', close);
    head.appendChild(x);
    root.appendChild(head);
  }

  // ── open / close ───────────────────────────────────────────────────────

  function close() {
    stopReveal();
    if (keyHandler) {
      document.removeEventListener('keydown', keyHandler);
      keyHandler = null;
    }
    if (live && live.el && live.el.parentNode) {
      live.el.parentNode.removeChild(live.el);
    }
    live = null;
  }

  function open(opts) {
    opts = opts || {};
    var pool = normalise(opts.students);
    /* Nothing to pick from is not a state worth putting a board display in
       front of; both callers already hide their entry control when the
       roster is empty, and this is the belt to that brace. */
    if (!pool.length || !opts.id) { return; }

    close();

    /* ⚠️ `#mrb-teacher` FIRST — see the mount note at the top of this file.
       `document.body` is the hand-written pages' answer (Today has no
       runtime host), not a fallback that is ever taken on a generated one. */
    var host = document.querySelector('#mrb-teacher') || document.body;
    var root = el('div', OVERLAY);
    root.setAttribute('role', 'dialog');
    root.setAttribute('aria-modal', 'true');
    /* ⚠️ THE CLASS CODE IS IN THE DIALOG'S NAME, NOT ONLY IN ITS HEADER, and
       that is the answer to the one cost of the DOM order this file uses
       (see the note at the top). The header is LAST in the DOM so that the
       close button cannot shut the overlay before an ordinal sweep has
       reached anything else — which would leave the header's caption read
       last by a screen reader, after the controls it captions. Named here,
       the class is announced the moment the dialog opens, which is earlier
       and better than either DOM order would have given. */
    root.setAttribute('aria-label',
                      'Pick a student' + (opts.code ? ' · ' + opts.code : ''));
    root.setAttribute('data-mrb-picker', String(opts.id));
    host.appendChild(root);

    live = { el: root, opts: opts, pool: pool, timer: null,
             absentOpen: false };

    keyHandler = function (e) {
      if (e.key === 'Escape' || e.keyCode === 27) { close(); }
    };
    document.addEventListener('keydown', keyHandler);

    draw();
    var go = root.querySelector('[data-mrb-added="pick-go"]');
    if (go && go.focus) { try { go.focus(); } catch (e) { /* headless */ } }
  }

  window.MrBadmusPicker = { open: open, close: close, isOpen: function () {
    return !!live;
  } };
}());
