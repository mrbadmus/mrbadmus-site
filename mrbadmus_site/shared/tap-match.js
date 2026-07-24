/* ============================================================
   MrBadmus — TAP MATCH  (Bonding v2 Phase 0a · MRB-132)
   Replacement for the old HTML5 drag-and-drop matching widget,
   which is dead on iOS/Android touch (drag events never fire)
   and keyboard-inaccessible. TapMatch uses the categorise-bins
   input model instead: tap a card to select it, tap a term to
   place it, tap a placed card to send it back. Every control is
   a real <button>, so Enter/Space work natively and the tab
   order is the visual order.

   ANTI-GIVE-AWAY GUARANTEES (same contract as categorise-bins):
     · BOTH columns — the terms AND the definition cards — are
       shuffled IN THE BROWSER on every load and on Reset, never
       baked into the HTML. Order is un-memorisable.
     · Check grades by the card→term GROUP MAPPING, never by
       position, so display order cannot leak or affect marks.

   PUBLIC API:
     MrbTapMatch.init(container, config)

   CONFIG SCHEMA:
   {
     stId        : string,   // storage key suffix (lab_best_<stId>)
     title       : string,   // panel heading
     instruction : string,   // line above the columns
     successTip  : string?,  // examiner-tip text shown on full marks
     pairs: [ { t: term, d: definition, g: groupId } ]
   }
   Rows sharing a term share a group id (category sorts), so a
   correctly-categorised card in a same-term sibling slot marks ✓.
============================================================ */
(function () {
  'use strict';
  if (window.MrbTapMatch) return;

  var STYLE_ID = 'mrb-tap-match-styles';
  function ensureStyles() {
    if (document.getElementById(STYLE_ID)) return;
    var s = document.createElement('style');
    s.id = STYLE_ID;
    s.textContent = [
      '.mrb-tm,.mrb-tm *{box-sizing:border-box}',
      '.mrb-tm{font-family:var(--font-body,system-ui,sans-serif);background:var(--surface-panel,#FFFDF8);border:1px solid var(--border,#E4DCCB);border-radius:var(--r-panel,22px);box-shadow:var(--shadow-panel,0 22px 50px -35px rgba(60,30,20,.5));overflow:hidden}',
      '.mrb-tm__head{display:flex;align-items:center;gap:10px;padding:16px 24px;border-bottom:1px solid var(--surface-inset,#EFE7D8);flex-wrap:wrap}',
      '.mrb-tm__head h3{font-family:var(--font-display,sans-serif);font-weight:700;font-size:calc(18px * var(--rd-fs-scale,1));color:var(--ink,#1A1714);margin:0;min-width:0;overflow-wrap:anywhere}',
      '.mrb-tm__score{font-family:var(--font-mono,monospace);font-size:calc(13px * var(--rd-fs-scale,1));font-weight:600;padding:7px 14px;border-radius:999px;white-space:nowrap;margin-left:auto}',
      '.mrb-tm__body{padding:22px 24px}',
      '.mrb-tm__prompt{margin:0 0 16px;font-size:calc(14.5px * var(--rd-fs-scale,1));line-height:1.55;color:var(--ink-body,#3A322A);max-width:70ch}',
      '.mrb-tm__cols{display:grid;grid-template-columns:1fr 1fr;gap:18px}',
      '@media (max-width:640px){.mrb-tm__cols{grid-template-columns:1fr}}',
      /* #716A60 = 4.79:1 on the cream inset (AA); the paler #9A9082 hint tint fails for instruction text */
      '.mrb-tm__col-lbl{font-family:var(--font-mono,monospace);font-size:calc(11px * var(--rd-fs-scale,1));font-weight:600;letter-spacing:.1em;color:#716A60;margin-bottom:10px;text-transform:uppercase}',
      '.mrb-tm__targets{display:flex;flex-direction:column;gap:10px}',
      '.mrb-tm__target{border:2px dashed #D8CFBD;border-radius:14px;padding:10px 12px;background:var(--surface-inset,#F7F2E8);transition:box-shadow .15s}',
      '.mrb-tm__target.is-open{box-shadow:0 0 0 3px rgba(224,83,31,.28)}',
      '.mrb-tm__term{display:block;width:100%;text-align:left;font-family:var(--font-display,sans-serif);font-weight:700;font-size:calc(14.5px * var(--rd-fs-scale,1));color:var(--ink,#1A1714);background:transparent;border:none;padding:4px 2px;cursor:pointer;border-radius:8px}',
      '.mrb-tm__term:focus-visible{outline:2px solid var(--accent-strong,#C0392B);outline-offset:2px}',
      '.mrb-tm__slot{margin-top:6px;min-height:26px;font-size:calc(12.5px * var(--rd-fs-scale,1));color:#716A60}',
      '.mrb-tm__pool{display:flex;flex-direction:column;gap:10px}',
      '.mrb-tm__card{font-family:var(--font-body,system-ui,sans-serif);font-size:calc(13.5px * var(--rd-fs-scale,1));line-height:1.45;text-align:left;cursor:pointer;border-radius:10px;padding:10px 13px;transition:all .15s;border:1px solid var(--border,#E4DCCB);background:var(--surface-panel,#FFFDF8);color:var(--ink-body,#2A241E)}',
      '.mrb-tm__card:focus-visible{outline:2px solid var(--accent-strong,#C0392B);outline-offset:2px}',
      '.mrb-tm__card.is-sel{background:#FBEAE1;border:2px solid #E0531F;box-shadow:0 6px 16px -8px rgba(224,83,31,.6)}',
      '.mrb-tm__card--placed{display:flex;justify-content:space-between;align-items:flex-start;gap:8px;width:100%}',
      '.mrb-tm__mark{font-weight:700;margin-left:6px;flex:none}',
      '.mrb-tm__pool-empty{font-size:calc(13.5px * var(--rd-fs-scale,1));color:#B0A695;padding:4px 2px}',
      '.mrb-tm__actions{display:flex;gap:12px;margin-top:20px;flex-wrap:wrap}',
      '.mrb-tm__check{font-family:var(--font-display,sans-serif);font-weight:700;font-size:calc(15px * var(--rd-fs-scale,1));color:#fff;background:var(--accent-deep,#B5341A);border:none;padding:13px 24px;border-radius:12px;cursor:pointer;box-shadow:0 8px 20px -8px rgba(181,52,26,.7)}',
      '.mrb-tm__check:focus-visible,.mrb-tm__reset:focus-visible{outline:2px solid var(--accent-strong,#C0392B);outline-offset:2px}',
      '.mrb-tm__reset{font-family:var(--font-display,sans-serif);font-weight:600;font-size:calc(15px * var(--rd-fs-scale,1));color:#4A4238;background:var(--surface-inset,#EFE7D8);border:1px solid var(--border,#E4DCCB);padding:13px 24px;border-radius:12px;cursor:pointer}',
      '.mrb-tm__result{margin-top:14px;font-family:var(--font-display,sans-serif);font-weight:700;font-size:calc(14.5px * var(--rd-fs-scale,1))}',
      '.mrb-tm__tip{margin-top:14px;background:#FEF6E0;border-left:4px solid #E0A21A;border-radius:12px;padding:14px 18px;font-size:calc(14px * var(--rd-fs-scale,1));line-height:1.55;color:#4A3A12}',
      '.mrb-tm__tip b{font-family:var(--font-display,sans-serif);color:#8A5E0A}',
      '.mrb-tm__sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}',
    ].join('');
    document.head.appendChild(s);
  }

  function el(tag, attrs, kids) {
    var n = document.createElement(tag);
    if (attrs) {
      if (attrs.className) n.className = attrs.className;
      if (attrs.style) for (var k in attrs.style) n.style[k] = attrs.style[k];
      if (attrs.on) for (var ev in attrs.on) n.addEventListener(ev, attrs.on[ev]);
      if (attrs.attrs) for (var a in attrs.attrs) n.setAttribute(a, attrs.attrs[a]);
    }
    if (kids != null) {
      if (!Array.isArray(kids)) kids = [kids];
      kids.forEach(function (c) { if (c != null) n.appendChild(typeof c === 'string' ? document.createTextNode(c) : c); });
    }
    return n;
  }

  function shuffle(a) {
    var arr = a.slice();
    for (var i = arr.length - 1; i > 0; i--) {
      var j = Math.floor(Math.random() * (i + 1));
      var t = arr[i]; arr[i] = arr[j]; arr[j] = t;
    }
    return arr;
  }

  function bestKey(stId) { return 'lab_best_' + stId; }
  function readBest(stId) {
    try { var v = parseInt(localStorage.getItem(bestKey(stId)), 10); return isNaN(v) ? null : v; } catch (e) { return null; }
  }
  function writeBest(stId, v) {
    try {
      var prev = readBest(stId);
      if (prev == null || v > prev) localStorage.setItem(bestKey(stId), String(v));
    } catch (e) {}
  }

  function init(container, config) {
    if (!container || !config || !config.pairs || !config.pairs.length) return;
    ensureStyles();

    // model: targets = one slot per pair row (its term + group);
    // cards = one card per pair row (its definition + group).
    var rows = config.pairs.map(function (p, i) {
      return { id: 'r' + i, term: p.t, def: p.d, g: p.g };
    });

    var placed = {};        // cardId -> targetId
    var selected = null;    // cardId selected in the pool
    var checked = false;
    var targetOrder = shuffle(rows.map(function (r) { return r.id; }));
    var poolOrder = shuffle(rows.map(function (r) { return r.id; }));
    var byId = {}; rows.forEach(function (r) { byId[r.id] = r; });

    var root = el('div', { className: 'mrb-tm' });
    var scorePill = el('div', { className: 'mrb-tm__score' });
    root.appendChild(el('div', { className: 'mrb-tm__head' }, [
      el('h3', null, config.title || 'Matching'),
      scorePill,
    ]));

    var live = el('div', { className: 'mrb-tm__sr', attrs: { 'aria-live': 'polite' } });

    var targetsWrap = el('div', { className: 'mrb-tm__targets' });
    var poolWrap = el('div', { className: 'mrb-tm__pool' });
    var poolEmpty = el('div', { className: 'mrb-tm__pool-empty' }, 'All placed — check your answers below.');

    var cols = el('div', { className: 'mrb-tm__cols' }, [
      el('div', null, [el('div', { className: 'mrb-tm__col-lbl' }, 'Terms · tap to place the selected card'), targetsWrap]),
      el('div', null, [el('div', { className: 'mrb-tm__col-lbl' }, 'Cards · tap one to select it'), poolEmpty, poolWrap]),
    ]);

    var result = el('div', { className: 'mrb-tm__result', attrs: { 'aria-live': 'polite' } });
    var tipSlot = el('div', null);

    var checkBtn = el('button', { className: 'mrb-tm__check', attrs: { type: 'button' }, on: { click: function () {
      checked = true; selected = null;
      writeBest(config.stId, countCorrect());
      render();
    } } }, '✓ Check answers');
    var resetBtn = el('button', { className: 'mrb-tm__reset', attrs: { type: 'button' }, on: { click: function () {
      placed = {}; selected = null; checked = false;
      targetOrder = shuffle(rows.map(function (r) { return r.id; }));
      poolOrder = shuffle(rows.map(function (r) { return r.id; }));
      render();
    } } }, '↻ Reset');

    var body = el('div', { className: 'mrb-tm__body' }, [
      el('p', { className: 'mrb-tm__prompt' }, (config.instruction || '') + ' Tap a card, then tap the term it belongs to. Tap a placed card to send it back.'),
      cols,
      el('div', { className: 'mrb-tm__actions' }, [checkBtn, resetBtn]),
      result, tipSlot, live,
    ]);
    root.appendChild(body);
    container.appendChild(root);

    // target id = 't-' + row id; group of a target
    function targetGroup(tid) { var r = byId[tid.replace('t-', '')]; return r ? r.g : null; }
    // grade by mapping: a card is correct when its target's group matches its own
    function countCorrect() {
      return rows.filter(function (r) { return placed[r.id] != null && targetGroup(placed[r.id]) === r.g; }).length;
    }
    function say(msg) { live.textContent = msg; }

    function placedCardBtn(card, ok) {
      var style = {}, mark = '';
      if (checked) {
        style.background = ok ? 'var(--ok-bg,#E7F3EA)' : 'var(--err-bg,#FBE4DE)';
        style.border = '1px solid ' + (ok ? 'var(--ok-border,#7FB98A)' : 'var(--err-border,#E0897B)');
        style.color = ok ? 'var(--ok,#2E6B3A)' : 'var(--err,#A83824)';
        mark = ok ? '✓' : '✕';
      }
      return el('button', {
        className: 'mrb-tm__card mrb-tm__card--placed', style: style,
        attrs: { type: 'button', 'aria-label': 'Return card to the pool: ' + card.def },
        on: { click: function () { delete placed[card.id]; checked = false; selected = null; render(); say('Card returned to the pool.'); } },
      }, [
        el('span', null, card.def),
        mark ? el('span', { className: 'mrb-tm__mark', attrs: { 'aria-hidden': 'true' } }, mark) : null,
      ]);
    }

    function render() {
      // terms column (browser-shuffled)
      targetsWrap.innerHTML = '';
      targetOrder.forEach(function (rid) {
        var r = byId[rid], tid = 't-' + rid;
        var box = el('div', { className: 'mrb-tm__target' + (selected ? ' is-open' : '') });
        var termBtn = el('button', {
          className: 'mrb-tm__term',
          attrs: { type: 'button', 'aria-pressed': 'false' },
          on: { click: function () {
            if (!selected) { say('Select a card first, then tap a term.'); return; }
            // occupied slot: send the occupant back
            for (var cid in placed) { if (placed[cid] === tid) delete placed[cid]; }
            placed[selected] = tid; selected = null; checked = false; render();
            var left = rows.length - Object.keys(placed).length;
            say('Placed in “' + r.term + '”. ' + (left ? left + ' card' + (left === 1 ? '' : 's') + ' left.' : 'All placed — check your answers.'));
          } },
        }, r.term);
        box.appendChild(termBtn);
        var slot = el('div', { className: 'mrb-tm__slot' });
        var occupant = null;
        for (var cid in placed) { if (placed[cid] === tid) occupant = byId[cid]; }
        if (occupant) {
          slot.innerHTML = '';
          slot.appendChild(placedCardBtn(occupant, targetGroup(tid) === occupant.g));
        } else {
          slot.textContent = selected ? 'Tap the term above to place the selected card' : '—';
        }
        box.appendChild(slot);
        targetsWrap.appendChild(box);
      });

      // pool column (browser-shuffled, minus placed)
      poolWrap.innerHTML = '';
      var inPool = poolOrder.filter(function (rid) { return !(rid in placed); });
      inPool.forEach(function (rid) {
        var r = byId[rid];
        poolWrap.appendChild(el('button', {
          className: 'mrb-tm__card' + (selected === rid ? ' is-sel' : ''),
          attrs: { type: 'button', 'aria-pressed': selected === rid ? 'true' : 'false' },
          on: { click: function () { selected = selected === rid ? null : rid; checked = false; render(); say(selected ? 'Card selected. Now tap the matching term.' : 'Card deselected.'); } },
        }, r.def));
      });
      poolEmpty.style.display = inPool.length ? 'none' : 'block';

      // score pill / result
      var total = rows.length;
      var done = Object.keys(placed).length;
      var best = readBest(config.stId);
      if (checked) {
        var correct = countCorrect();
        scorePill.textContent = correct + ' / ' + total + (best != null ? ' · best ' + best : '');
        var win = correct === total;
        scorePill.style.color = win ? 'var(--ok,#2E6B3A)' : 'var(--err,#A83824)';
        scorePill.style.background = win ? 'var(--ok-bg,#E7F3EA)' : 'var(--err-bg,#FBE4DE)';
        result.style.color = win ? 'var(--ok,#2E6B3A)' : 'var(--err,#A83824)';
        result.textContent = win ? total + '/' + total + ' — all matched.' : correct + '/' + total + ' — return the marked cards and try again.';
        tipSlot.innerHTML = '';
        if (win && config.successTip) {
          var tip = el('div', { className: 'mrb-tm__tip' });
          tip.appendChild(el('b', null, 'Examiner Tip · '));
          tip.appendChild(document.createTextNode(config.successTip));
          tipSlot.appendChild(tip);
        }
      } else {
        scorePill.textContent = (done === total ? 'Ready to check' : done + ' / ' + total + ' placed') + (best != null ? ' · best ' + best : '');
        scorePill.style.color = 'var(--ink-faint,#8A8074)';
        scorePill.style.background = 'var(--surface-inset,#EFE7D8)';
        result.textContent = '';
        tipSlot.innerHTML = '';
      }
    }

    render();
    return { render: render };
  }

  window.MrbTapMatch = { init: init };
})();
