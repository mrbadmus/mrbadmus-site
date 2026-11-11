/* shared/teacher-picker.js — MRB-323, 5 Sep 2026.

   A random name picker, per class, for the front of a classroom.

   ══ WHAT IT IS ═════════════════════════════════════════════════════════

   `window.MrBadmusPicker.open({id, code, students})` puts a full-screen
   board display over the page: a name at the display scale, a Pick button,
   a no-repeats cycle with a visible count, a pure-random alternative, and a
   session-only absent list.

   A small cog in the header opens a settings panel: one row per pupil with a
   TICKET count (the weighting: `−` / `+`, minimum 1, no maximum), a tap on a
   pupil's name to make them the NEXT pick, a Reset, and a "Save for this
   class" switch. A clock button beside the cog opens `MrBadmusTimer`
   (`shared/teacher-timer.js`) as a floating timer, so the names stay in view.

   ══ WHAT IT KEEPS, WHERE, AND FOR HOW LONG — AND NOTHING ELSE ═══════════

   ⛔ NO DATABASE, NO NETWORK, NO COOKIE, NO `sessionStorage`. There is no
   `fetch`, no Supabase client and no cookie anywhere in this file,
   deliberately and checkably: who was picked and who was away is a fact
   about one lesson in one room, and a platform that recorded it would be
   keeping an attendance register nobody asked it to keep and no teacher had
   a chance to correct.

   Everything is in `STATE` below, a plain object in this closure, and
   `STATE` dies with the page load. That covers the mode, the cycle's
   picked-counts, the absent list, the last name shown and the pick-next
   mark. Reload the page and all of it is gone, which is the intended
   lifetime.

   THE ONE EXCEPTION, AND IT IS THE TEACHER'S OWN SWITCH: ticket WEIGHTS.
   - "Save for this class" is OFF by default. While it is off, weights live
     in `STATE` only and go back to 1 when the picker is closed (or the page
     reloads).
   - While it is ON, this class's weights are written to this browser's
     `localStorage`, under ONE key per class —
     `mrb.picker.weights.v1.<classId>` — as `{"weights":{"<pupilId>":n}}`,
     holding only the pupils whose weight is above 1 and only pupils who are
     on the roster being shown. It is rewritten on every weight change and on
     Reset (Reset leaves `{"weights":{}}` in place rather than deleting the
     key, because the key's presence IS the switch's state and a Reset must
     not silently turn saving off). Opening the picker for a class whose key
     exists shows the switch ON and loads the weights from it. Turning the
     switch OFF deletes the key.
   - It is per device and per browser. Nothing leaves it.
   - NOTHING ELSE is ever stored: not the pick-next mark, not the absent
     list, not who was picked, not the mode. Every storage call is inside a
     try/catch; with storage blocked the picker works as if the switch were
     off and says so on the panel.

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
     `{classId: {mode, absent:{id:1}, picked:{id:n}, last:{id,name},
                 weights:{id:n}, next:id|null, save:bool}}`.
     `picked` is a COUNT per pupil (tickets drawn), not a 0/1 flag; `weights`
     holds only ids above 1. The only part of this that is ever written
     anywhere is `weights`, and only while `save` is true — see the header
     and `store*()` below. */
  var STATE = {};

  /* The one storage key family. One key per class; nothing else is stored. */
  var KEY = 'mrb.picker.weights.v1.';

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

  /* The header's two quiet icon buttons (timer, settings): the close X's
     40px box with no border, in the caption colour, so they are findable and
     never compete with the name. Pressed/expanded = the seg trough. */
  var ICON_BTN = 'flex:none;width:40px;height:40px;display:flex;' +
                 'align-items:center;justify-content:center;' +
                 'background:transparent;border:1px solid transparent;' +
                 'border-radius:9px;cursor:pointer;color:var(--st-caption)';
  var ICON_BTN_ON = 'flex:none;width:40px;height:40px;display:flex;' +
                    'align-items:center;justify-content:center;' +
                    'background:var(--st-seg-bg);' +
                    'border:1px solid var(--st-rule-strong);' +
                    'border-radius:9px;cursor:pointer;color:var(--st-ink)';
  var HEAD_RIGHT = 'flex:none;display:flex;align-items:center;gap:6px';

  /* The settings panel takes the stage's place while it is open. */
  var PANEL = 'order:2;flex:1;min-height:0;overflow:auto;padding:16px 20px 28px';
  var PANEL_IN = 'width:100%;max-width:640px;margin:0 auto;display:flex;' +
                 'flex-direction:column;gap:14px';
  var SW_ROW = 'display:flex;align-items:center;gap:14px;width:100%;' +
               'min-height:52px;padding:0 4px;background:none;border:none;' +
               'cursor:pointer;text-align:left;color:var(--st-ink);' +
               'font:600 16px/1.2 var(--st-ui)';
  var SW_TRACK_OFF = 'flex:none;position:relative;width:46px;height:28px;' +
                     'border-radius:14px;background:var(--st-seg-bg);' +
                     'border:1px solid var(--st-rule-strong)';
  var SW_TRACK_ON = 'flex:none;position:relative;width:46px;height:28px;' +
                    'border-radius:14px;background:var(--st-accent-text);' +
                    'border:1px solid var(--st-accent-text)';
  var SW_KNOB_OFF = 'position:absolute;top:2px;left:2px;width:22px;' +
                    'height:22px;border-radius:50%;background:var(--st-paper);' +
                    'border:1px solid var(--st-rule-strong)';
  var SW_KNOB_ON = 'position:absolute;top:2px;left:20px;width:22px;' +
                   'height:22px;border-radius:50%;background:var(--st-paper)';
  var RESET_BTN = 'flex:none;min-height:44px;padding:0 20px;' +
                  'font:600 16px/1.2 var(--st-ui);color:var(--st-ink);' +
                  'background:var(--st-paper);' +
                  'border:1px solid var(--st-btn-border);border-radius:10px;' +
                  'cursor:pointer';
  var RESET_OFF = 'flex:none;min-height:44px;padding:0 20px;' +
                  'font:600 16px/1.2 var(--st-ui);color:var(--st-caption);' +
                  'background:var(--st-paper);' +
                  'border:1px solid var(--st-btn-border);border-radius:10px;' +
                  'cursor:not-allowed';
  var HELP = 'font:500 14px/1.4 var(--st-ui);color:var(--st-caption)';
  var LIST_HEAD = 'display:flex;justify-content:space-between;gap:12px;' +
                  'font:500 12px/1.2 var(--st-mono);letter-spacing:.14em;' +
                  'text-transform:uppercase;color:var(--st-caption);' +
                  'margin-top:6px';
  var ROW = 'display:flex;align-items:center;gap:8px;min-height:52px;' +
            'border-top:1px solid var(--st-rule-soft)';
  var ROW_NAME = 'flex:1;min-width:0;min-height:48px;display:flex;' +
                 'align-items:center;gap:10px;padding:0 6px;background:none;' +
                 'border:none;border-radius:9px;cursor:pointer;' +
                 'text-align:left;font:500 17px/1.2 var(--st-ui);' +
                 'color:var(--st-ink)';
  var ROW_NAME_NEXT = ROW_NAME + ';background:var(--st-chip-tint);' +
                      'box-shadow:inset 0 0 0 1px var(--st-chip-tint-border)';
  var ROW_NAME_OUT = ROW_NAME + ';color:var(--st-caption);' +
                     'text-decoration:line-through;cursor:not-allowed';
  var STEP_BTN = 'flex:none;width:40px;height:40px;display:flex;' +
                 'align-items:center;justify-content:center;' +
                 'background:var(--st-paper);' +
                 'border:1px solid var(--st-btn-border);border-radius:9px;' +
                 'cursor:pointer;color:var(--st-ink)';
  var STEP_BTN_OFF = 'flex:none;width:40px;height:40px;display:flex;' +
                     'align-items:center;justify-content:center;' +
                     'background:transparent;' +
                     'border:1px solid var(--st-rule);border-radius:9px;' +
                     'cursor:not-allowed;color:var(--st-ghost)';
  var STEP_N = 'flex:none;min-width:34px;text-align:center;' +
               'font:600 18px/1 var(--st-mono);color:var(--st-ink)';
  var NEXT_TAG = 'flex:none;display:inline-flex;align-items:center;gap:5px;' +
                 'font:500 12px/1.2 var(--st-mono);letter-spacing:.12em;' +
                 'text-transform:uppercase;color:var(--st-accent-text)';

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

  /* House-style icons: the close X's recipe — stroke is currentColor, round
     caps, ~1.6 wide, aria-hidden. No glyph characters stand in for any of
     them. `innerHTML` here is a constant string, never a name. */
  var ICONS = {
    cog: '<svg width="19" height="19" viewBox="0 0 24 24" fill="none" ' +
         'aria-hidden="true" stroke="currentColor" stroke-width="1.6" ' +
         'stroke-linecap="round" stroke-linejoin="round"><circle cx="12" ' +
         'cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 ' +
         '2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 ' +
         '1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 ' +
         '1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 ' +
         '0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 ' +
         '0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 ' +
         '9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 ' +
         '2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 ' +
         '2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 ' +
         '0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 ' +
         '1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 ' +
         '0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"/></svg>',
    clock: '<svg width="19" height="19" viewBox="0 0 18 18" fill="none" ' +
           'aria-hidden="true" stroke="currentColor" stroke-width="1.6" ' +
           'stroke-linecap="round" stroke-linejoin="round"><circle cx="9" ' +
           'cy="10.2" r="6"/><path d="M9 10.2V7M7 1.8h4"/></svg>',
    minus: '<svg width="14" height="14" viewBox="0 0 14 14" fill="none" ' +
           'aria-hidden="true"><path d="M3 7h8" stroke="currentColor" ' +
           'stroke-width="1.6" stroke-linecap="round"/></svg>',
    plus: '<svg width="14" height="14" viewBox="0 0 14 14" fill="none" ' +
          'aria-hidden="true"><path d="M3 7h8M7 3v8" stroke="currentColor" ' +
          'stroke-width="1.6" stroke-linecap="round"/></svg>',
    next: '<svg width="12" height="12" viewBox="0 0 12 12" fill="none" ' +
          'aria-hidden="true"><path d="M4 2l4 4-4 4" stroke="currentColor" ' +
          'stroke-width="1.6" stroke-linecap="round" ' +
          'stroke-linejoin="round"/></svg>'
  };
  function icon(node, name) { node.innerHTML = ICONS[name]; return node; }

  // ── the one opt-in store: ticket weights, per class ────────────────────

  /* ⚠️ EVERY ACCESS IS INSIDE try/catch. `localStorage` throws in a private
     window, with site data blocked, and in some embedded previews; the
     picker has to work, switch off, without it. */
  function storeRead(classId) {
    try {
      var raw = window.localStorage.getItem(KEY + classId);
      if (raw === null || raw === undefined) { return null; }
      var out = {};
      try {
        var w = (JSON.parse(raw) || {}).weights || {};
        Object.keys(w).forEach(function (id) {
          var n = Math.floor(Number(w[id]));
          if (n > 1) { out[id] = Math.min(n, 999); }
        });
      } catch (e) { /* a corrupt value is still "saved, with nothing in it" */ }
      return out;
    } catch (e) { return null; }
  }

  function storeWrite(classId, weights) {
    try {
      window.localStorage.setItem(KEY + classId,
                                  JSON.stringify({ weights: weights }));
      return true;
    } catch (e) { return false; }
  }

  function storeRemove(classId) {
    try { window.localStorage.removeItem(KEY + classId); } catch (e) { /* ok */ }
  }

  /* Written weights: above 1 only, and only for pupils on THIS roster, so a
     key never holds an id the roster no longer shows. */
  function persist(s) {
    if (!live || !s.save) { return; }
    var out = {};
    live.pool.forEach(function (p) {
      if ((s.weights[p.id] || 1) > 1) { out[p.id] = s.weights[p.id]; }
    });
    s.saveFailed = !storeWrite(live.opts.id, out);
  }

  function wOf(s, id) { return s.weights[id] || 1; }

  function setWeight(s, id, n) {
    n = Math.max(1, Math.floor(n) || 1);
    if (n === 1) { delete s.weights[id]; } else { s.weights[id] = n; }
    persist(s);
  }

  function anyWeight(s) {
    return Object.keys(s.weights).some(function (k) { return s.weights[k] > 1; });
  }

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
      STATE[classId] = { mode: 'cycle', absent: {}, picked: {}, last: null,
                         weights: {}, next: null, save: false,
                         saveFailed: false };
    }
    return STATE[classId];
  }

  /* The sets every line on this screen is derived from. Recomputed on every
     draw rather than cached, because a student can be marked absent after
     being picked, and a weight can change mid-cycle, and the count has to
     stay honest when either happens.

     TICKETS: a pupil of weight w holds w tickets. `total` (M) is the tickets
     held by present pupils; `doneN` (N) is the tickets already drawn,
     `min(picked, w)` per present pupil — the `min` is what keeps N from ever
     exceeding M when a weight is lowered after a draw. `left` is the present
     pupils with a ticket still in the hat, and `leftN` the tickets. With
     every weight 1 this is the old 0/1 arithmetic exactly. */
  function sets(pool, s) {
    var present = pool.filter(function (p) { return !s.absent[p.id]; });
    var total = 0, doneN = 0, leftN = 0, left = [];
    present.forEach(function (p) {
      var w = wOf(s, p.id), d = Math.min(s.picked[p.id] || 0, w);
      total += w; doneN += d; leftN += w - d;
      if (d < w) { left.push(p); }
    });
    return { present: present, left: left, total: total, doneN: doneN,
             leftN: leftN };
  }

  /* Draw one ticket. `ticketsOf(p)` is how many a pupil holds in this draw. */
  function drawTicket(list, ticketsOf) {
    var sum = 0;
    list.forEach(function (p) { sum += ticketsOf(p); });
    var r = Math.random() * sum;
    for (var i = 0; i < list.length; i++) {
      r -= ticketsOf(list[i]);
      if (r < 0) { return list[i]; }
    }
    return list[list.length - 1];
  }

  /* ⚠️ THE WINNER IS DECIDED HERE, BEFORE ANY ANIMATION. Pick-next is a
     one-off: it is consumed by the press that lands it. In the cycle it spends
     one of the pupil's tickets if one is left, and is still honoured if none
     is — the teacher's choice wins — without pushing `picked` above the
     weight. */
  function chooseWinner(s, g, cycling) {
    var nx = null;
    if (s.next) {
      g.present.forEach(function (p) { if (p.id === s.next) { nx = p; } });
      s.next = null;
    }
    if (nx) {
      if (cycling && (s.picked[nx.id] || 0) < wOf(s, nx.id)) {
        s.picked[nx.id] = (s.picked[nx.id] || 0) + 1;
      }
      return nx;
    }
    if (cycling) {
      var w = drawTicket(g.left, function (p) {
        return wOf(s, p.id) - Math.min(s.picked[p.id] || 0, wOf(s, p.id));
      });
      s.picked[w.id] = (s.picked[w.id] || 0) + 1;
      return w;
    }
    return drawTicket(g.present, function (p) { return wOf(s, p.id); });
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
    var settings = !!live.settingsOpen;
    /* While the settings panel is up the board is not shown, and not merely
       covered: a hidden stage cannot be read by a screen reader or reached
       by Tab behind the panel. */
    var hideBoard = settings ? ';display:none' : '';

    root.textContent = '';

    // ── stage (first in the DOM, second on the screen) ─────────────────
    var stage = el('div', STAGE + hideBoard);
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

    /* A pick-next mark that points at nobody present is no mark. */
    var nextOk = !!(s.next && g.present.some(function (p) { return p.id === s.next; }));
    var exhausted = (cycling ? g.leftN === 0 : g.present.length === 0) && !nextOk;
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
        if (!g.present.length) { return; }
        var winner = chooseWinner(s, g, cycling);
        s.last = winner;
        draw();
        reveal(root.querySelector('[data-mrb-name]') || nameNode,
               winner, g.present);
      });
    }
    stage.appendChild(pick);
    root.appendChild(stage);

    // ── footer ─────────────────────────────────────────────────────────
    var foot = el('div', FOOT + hideBoard);
    var row = el('div', FOOT_ROW);

    var count = el('div', COUNT);
    if (!g.present.length) {
      text(count, 'Nobody in the pool');
    } else if (cycling) {
      text(count, 'Picked ' + g.doneN + ' of ' + g.total);
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
    if (cycling && g.doneN) {
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
          else {
            s.absent[p.id] = 1;
            /* Absent pupils cannot be the next pick. */
            if (s.next === p.id) { s.next = null; }
          }
          draw();
        });
        chips.appendChild(c);
      });
      foot.appendChild(chips);
    }
    root.appendChild(foot);

    // ── settings panel (after the footer, before the header) ───────────
    if (settings) { root.appendChild(buildPanel(s, pool)); }

    // ── header (last in the DOM, first on the screen — see the note up top)
    var head = el('div', HEAD);
    var code = el('div', HEAD_CODE);
    code.setAttribute('data-mrb-code', '1');
    text(code, opts.code || 'Class');
    head.appendChild(code);

    var right = el('div', HEAD_RIGHT);
    var T = window.MrBadmusTimer;
    if (T) {
      var tOpen = T.isOpen();
      var tb = el('button', tOpen ? ICON_BTN_ON : ICON_BTN, 'pick-timer');
      tb.setAttribute('aria-label', 'Timer');
      tb.setAttribute('aria-pressed', tOpen ? 'true' : 'false');
      icon(tb, 'clock');
      /* Closed: open it FLOATING, so the names stay in view. Already open:
         bring it to the full-screen view — closing a running timer from
         here would be a way to lose it by accident. It is closed from its
         own X. */
      tb.addEventListener('click', function () {
        T.open({ view: T.isOpen() ? 'full' : 'float' });
        syncTimerBtn();
      });
      live.timerBtn = tb;
      right.appendChild(tb);
    }
    var cog = el('button', settings ? ICON_BTN_ON : ICON_BTN, 'pick-settings');
    cog.setAttribute('aria-label', 'Settings');
    cog.setAttribute('aria-expanded', settings ? 'true' : 'false');
    icon(cog, 'cog');
    cog.addEventListener('click', function () {
      live.settingsOpen = !live.settingsOpen;
      draw();
      var again = root.querySelector('[data-mrb-added="pick-settings"]');
      if (again && again.focus) { try { again.focus(); } catch (e) { /* ok */ } }
    });
    right.appendChild(cog);

    var x = el('button', HEAD_X, 'pick-close');
    x.setAttribute('aria-label', 'Close');
    x.innerHTML = '<svg width="14" height="14" viewBox="0 0 14 14" ' +
                  'fill="none" aria-hidden="true"><path d="M2 2l10 10M12 2' +
                  'L2 12" stroke="currentColor" stroke-width="1.6" ' +
                  'stroke-linecap="round"/></svg>';
    x.addEventListener('click', close);
    right.appendChild(x);
    head.appendChild(right);
    root.appendChild(head);
  }

  /* The timer button reflects whether the timer is showing — in place, never
     by a redraw, because a redraw would cut a reveal short. */
  function syncTimerBtn() {
    var T = window.MrBadmusTimer;
    if (!live || !live.timerBtn || !T) { return; }
    var on = T.isOpen();
    live.timerBtn.setAttribute('aria-pressed', on ? 'true' : 'false');
    live.timerBtn.setAttribute('style', on ? ICON_BTN_ON : ICON_BTN);
    padPanel();
  }

  /* ⚠️ THE FLOATING TIMER IS A CARD IN THE BOTTOM-RIGHT CORNER, and what
     is in that corner is the picker's own footer — the mode toggle and
     "Start again" on the board, the `+` buttons of the last rows in the
     settings panel. `teacher_reach` found the second at 390px, and the
     first is the same defect with a bigger target. So while the float is
     showing, the overlay reserves room for it at the bottom (bottom
     padding = the float's measured height), and everything the picker draws
     sits above it instead of under it. Not showing, or full-screen (which
     covers the page by design), it reserves nothing. */
  function padPanel() {
    if (!live) { return; }
    var t = document.querySelector('[data-tm="overlay"]'), pad = '';
    if (t && t.getAttribute('data-tm-view') === 'float') {
      pad = (Math.ceil(t.getBoundingClientRect().height) + 12) + 'px';
    }
    live.el.style.paddingBottom = pad;
    live.el.style.boxSizing = 'border-box';
  }

  // ── the settings panel ─────────────────────────────────────────────────

  function buildPanel(s, pool) {
    var panel = el('div', PANEL, 'pick-set-panel');
    var inner = el('div', PANEL_IN);

    /* Reset, TOP of the panel. Rendered always, and dead-looking
       (`aria-disabled`, not-allowed) when there is nothing to reset — see the
       note on `PICK_OFF`: a control that does nothing must say so. */
    var nothing = !anyWeight(s) && !s.next;
    var rs = el('button', (nothing ? RESET_OFF : RESET_BTN) +
                ';align-self:flex-start', 'pick-set-reset');
    text(rs, 'Reset');
    if (nothing) {
      rs.setAttribute('aria-disabled', 'true');
    } else {
      rs.addEventListener('click', function () {
        s.weights = {};
        s.next = null;
        persist(s);
        draw();
      });
    }
    inner.appendChild(rs);

    // Save for this class — a switch, off by default.
    var sw = el('button', SW_ROW, 'pick-set-save');
    sw.setAttribute('role', 'switch');
    sw.setAttribute('aria-checked', s.save ? 'true' : 'false');
    var lab = el('span', 'flex:1;min-width:0');
    text(lab, 'Save for this class');
    var track = el('span', s.save ? SW_TRACK_ON : SW_TRACK_OFF);
    track.appendChild(el('span', s.save ? SW_KNOB_ON : SW_KNOB_OFF));
    sw.appendChild(lab);
    sw.appendChild(track);
    sw.addEventListener('click', function () {
      if (s.save) {
        s.save = false;
        storeRemove(live.opts.id);
      } else {
        s.save = true;
        persist(s);
        if (s.saveFailed) { s.save = false; }
      }
      draw();
    });
    inner.appendChild(sw);
    var help = el('div', HELP);
    help.setAttribute('data-mrb-added', 'pick-set-help');
    text(help, s.saveFailed ? 'This browser would not save. Weights reset when you close.'
               : s.save ? 'Weights are kept on this device for this class.'
                        : 'Weights reset when you close the picker.');
    inner.appendChild(help);

    // The list: name (tap = next pick) and tickets.
    var lh = el('div', LIST_HEAD);
    lh.appendChild(text(el('span'), 'Tap a name to pick them next'));
    lh.appendChild(text(el('span'), 'Tickets'));
    inner.appendChild(lh);

    pool.forEach(function (p) {
      var w = wOf(s, p.id);
      var out = !!s.absent[p.id];
      var isNext = s.next === p.id && !out;
      var row = el('div', ROW, 'pick-set-row');

      var nb = el('button', out ? ROW_NAME_OUT : (isNext ? ROW_NAME_NEXT : ROW_NAME),
                  'pick-set-name');
      nb.appendChild(text(el('span', 'min-width:0;overflow:hidden;' +
                                     'text-overflow:ellipsis;white-space:nowrap'),
                          p.name));
      if (isNext) {
        var tag = el('span', NEXT_TAG, 'pick-set-next');
        tag.appendChild(el('span', 'display:inline-flex')).innerHTML = ICONS.next;
        tag.appendChild(text(el('span'), 'Next'));
        nb.appendChild(tag);
      }
      nb.setAttribute('aria-pressed', isNext ? 'true' : 'false');
      if (out) {
        nb.setAttribute('aria-disabled', 'true');
      } else {
        nb.addEventListener('click', function () {
          s.next = isNext ? null : p.id;
          draw();
        });
      }
      row.appendChild(nb);

      var minus = el('button', w > 1 ? STEP_BTN : STEP_BTN_OFF, 'pick-set-minus');
      minus.setAttribute('aria-label', 'Fewer tickets for ' + p.name);
      icon(minus, 'minus');
      if (w > 1) {
        minus.addEventListener('click', function () {
          setWeight(s, p.id, w - 1); draw();
        });
      } else {
        minus.setAttribute('aria-disabled', 'true');
      }
      row.appendChild(minus);

      var n = el('div', STEP_N, 'pick-set-count');
      text(n, String(w));
      row.appendChild(n);

      var plus = el('button', STEP_BTN, 'pick-set-plus');
      plus.setAttribute('aria-label', 'More tickets for ' + p.name);
      icon(plus, 'plus');
      plus.addEventListener('click', function () {
        setWeight(s, p.id, w + 1); draw();
      });
      row.appendChild(plus);

      inner.appendChild(row);
    });

    panel.appendChild(inner);
    return panel;
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
    /* Weights live only as long as the picker is open unless the teacher
       turned "Save for this class" on. (Pick-next, the cycle and the absent
       list stay in `STATE` for the page load, as they always did.) */
    if (live) {
      var s = STATE[live.opts.id];
      if (s && !s.save) { s.weights = {}; }
    }
    if (live && live.unTimer) { live.unTimer(); }
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
             absentOpen: false, settingsOpen: false, timerBtn: null,
             unTimer: null };

    /* The saved weights, if this class has a key: the switch reads ON and the
       weights load from it. No key means OFF. */
    var s = sessionFor(opts.id);
    var saved = storeRead(opts.id);
    if (saved) { s.save = true; s.weights = saved; }
    else { s.save = false; }
    s.saveFailed = false;

    /* The timer button follows the timer's own open/close. */
    if (window.MrBadmusTimer && window.MrBadmusTimer.onChange) {
      live.unTimer = window.MrBadmusTimer.onChange(syncTimerBtn);
    }

    keyHandler = function (e) {
      if (e.key === 'Escape' || e.keyCode === 27) { close(); }
    };
    document.addEventListener('keydown', keyHandler);

    draw();
    padPanel();
    var go = root.querySelector('[data-mrb-added="pick-go"]');
    if (go && go.focus) { try { go.focus(); } catch (e) { /* headless */ } }
  }

  window.MrBadmusPicker = { open: open, close: close, isOpen: function () {
    return !!live;
  } };
}());
