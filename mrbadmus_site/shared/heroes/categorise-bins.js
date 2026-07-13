/* ============================================================
   MrBadmus Hero — CATEGORISE BINS  (vanilla port)
   Archetype 09 / 12. The "sort it" archetype: a pool of cards and
   2–3 labelled bins. Tap a card to select it, tap a bin to drop it
   in, tap a placed card to send it back to the pool. Check answers
   marks every card ✓ / ✕ in place and updates the score pill.

   Ported from Design's `Bonding Hero 9 - Categorise Bins.dc.html`.
   No React, no build step.

   WHY THIS REPLACES THE OLD DRAG-MATCH FOR CATEGORY SORTS:
   the old widget rendered one labelled slot per card, so slot order
   ≈ answer order and a student could drag top-to-bottom without
   reading. Bins have no per-card slots: there is one pool and a few
   bins, so position carries no answer.

   ANTI-GIVE-AWAY GUARANTEES (Mide, locked):
     · The card pool is shuffled IN THE BROWSER on every load
       (and on Reset) — never baked into the HTML. Order is
       arbitrary per visit and un-memorisable.
     · Check grades by the card→bin MAPPING, never by position, so
       display order can never leak or affect correctness.

   PUBLIC API:
     MrbHeroes.categoriseBins.init(container, config)

   CONFIG SCHEMA:
   {
     emoji, title, subtitle : string     // hero header row
     prompt                 : string     // instruction line above the tray
     trayLabel              : string     // mono label on the tray
     bins: [ 2–3 × {
       key   : string,                   // stable id used by cards' `bin`
       label : string,                   // bin heading
       emoji : string (optional),        // icon in the bin heading
       tint  : 'warm'|'cool'|'neutral'   // bin container colour (default warm/cool alternation)
     } ],
     cards: [ { id, text, bin } ],        // bin = key of the correct bin
     hint : string                        // dark mono bar text (optional)
   }
============================================================ */
(function () {
  'use strict';
  var NS = (window.MrbHeroes = window.MrbHeroes || {});
  if (NS.categoriseBins) return;

  /* ---- bin container tints (soft, distinct from the ✓/✕ marks) ----
     Green is reserved exclusively for "correct" feedback, so bins use
     warm (orange) / cool (blue) neutral tints. */
  var TINT = {
    warm:    { fill: 'linear-gradient(180deg,#FDF1E9,#FBF7EF)', border: '#E7A886', head: 'var(--accent-deep,#B5341A)', hint: '#C7A38F' },
    cool:    { fill: 'linear-gradient(180deg,#E9F1FA,#F4F7FB)', border: '#9CC0E4', head: 'var(--context-blue,#2E7DD1)', hint: '#96B4D4' },
    neutral: { fill: 'var(--surface-inset,#F7F2E8)',           border: '#D8CFBD', head: 'var(--ink,#1A1714)',        hint: '#B0A695' },
  };

  var STYLE_ID = 'mrb-hero-bins-styles';
  function ensureStyles() {
    if (document.getElementById(STYLE_ID)) return;
    var s = document.createElement('style');
    s.id = STYLE_ID;
    s.textContent = [
      '.mrb-bins,.mrb-bins *{box-sizing:border-box}',
      '.mrb-bins{font-family:var(--font-body,system-ui,sans-serif);background:var(--surface-panel,#FFFDF8);border:1px solid var(--border,#E4DCCB);border-radius:var(--r-panel,22px);box-shadow:var(--shadow-panel,0 22px 50px -35px rgba(60,30,20,.5));overflow:hidden}',
      '.mrb-bins__head{display:flex;align-items:center;gap:10px;padding:16px 24px;border-bottom:1px solid var(--surface-inset,#EFE7D8);flex-wrap:wrap}',
      '.mrb-bins__head h3{font-family:var(--font-display,sans-serif);font-weight:700;font-size: calc(18px * var(--rd-fs-scale, 1));color:var(--ink,#1A1714);margin:0}',
      '.mrb-bins__sub{font-family:var(--font-mono,monospace);font-size: calc(12px * var(--rd-fs-scale, 1));color:var(--ink-faint,#8A8074)}',
      '.mrb-bins__body{padding:22px 24px}',
      '.mrb-bins__toprow{display:flex;align-items:center;justify-content:space-between;gap:16px;flex-wrap:wrap;margin-bottom:18px}',
      '.mrb-bins__prompt{margin:0;font-size: calc(14.5px * var(--rd-fs-scale, 1));line-height:1.55;color:var(--ink-body,#3A322A);max-width:62ch}',
      '.mrb-bins__score{font-family:var(--font-mono,monospace);font-size: calc(13px * var(--rd-fs-scale, 1));font-weight:600;padding:7px 14px;border-radius:999px;white-space:nowrap}',
      '.mrb-bins__tray{background:var(--surface-inset,#F7F2E8);border:1px dashed #D8CFBD;border-radius:16px;padding:16px;margin-bottom:18px;min-height:64px}',
      '.mrb-bins__tray-lbl{font-family:var(--font-mono,monospace);font-size: calc(11px * var(--rd-fs-scale, 1));font-weight:600;letter-spacing:.1em;color:#9A9082;margin-bottom:10px}',
      '.mrb-bins__tray-empty{font-size: calc(14px * var(--rd-fs-scale, 1));color:#B0A695;padding:4px 2px}',
      '.mrb-bins__pool{display:flex;flex-wrap:wrap;gap:10px}',
      '.mrb-bins__grid{display:grid;gap:16px}',
      '.mrb-bins__bin{border-radius:16px;padding:16px;min-height:120px;transition:all .15s;cursor:pointer}',
      '.mrb-bins__bin.is-target{box-shadow:0 0 0 3px rgba(224,83,31,.28)}',
      '.mrb-bins__bin-head{display:flex;align-items:center;gap:8px;margin-bottom:12px}',
      '.mrb-bins__bin-title{font-family:var(--font-display,sans-serif);font-weight:700;font-size: calc(16px * var(--rd-fs-scale, 1))}',
      '.mrb-bins__placed{display:flex;flex-direction:column;gap:8px}',
      '.mrb-bins__bin-hint{font-size: calc(13.5px * var(--rd-fs-scale, 1))}',
      '.mrb-bins__card{font-family:var(--font-body,system-ui,sans-serif);font-size: calc(13.5px * var(--rd-fs-scale, 1));line-height:1.4;text-align:left;cursor:pointer;border-radius:10px;padding:10px 13px;transition:all .15s;border:1px solid var(--border,#E4DCCB);background:var(--surface-panel,#FFFDF8);color:var(--ink-body,#2A241E)}',
      '.mrb-bins__card.is-sel{background:#FBEAE1;border:2px solid #E0531F;box-shadow:0 6px 16px -8px rgba(224,83,31,.6)}',
      '.mrb-bins__card--placed{display:flex;justify-content:space-between;align-items:center;gap:8px;width:100%}',
      '.mrb-bins__mark{font-weight:700;margin-left:8px}',
      '.mrb-bins__actions{display:flex;gap:12px;margin-top:20px;flex-wrap:wrap}',
      '.mrb-bins__check{font-family:var(--font-display,sans-serif);font-weight:700;font-size: calc(15px * var(--rd-fs-scale, 1));color:#fff;background:var(--accent-deep,#B5341A);border:none;padding:13px 24px;border-radius:12px;cursor:pointer;box-shadow:0 8px 20px -8px rgba(181,52,26,.7)}',
      '.mrb-bins__reset{font-family:var(--font-display,sans-serif);font-weight:600;font-size: calc(15px * var(--rd-fs-scale, 1));color:#4A4238;background:var(--surface-inset,#EFE7D8);border:1px solid var(--border,#E4DCCB);padding:13px 24px;border-radius:12px;cursor:pointer}',
      '.mrb-bins__strap{padding:13px 24px;background:var(--surface-dark,#1A1714);font-family:var(--font-mono,monospace);font-size: calc(12.5px * var(--rd-fs-scale, 1));line-height:1.5;color:#EAE3D6}',
    ].join('');
    document.head.appendChild(s);
  }

  /* ---- tiny DOM helper ---- */
  function el(tag, attrs, kids) {
    var n = document.createElement(tag);
    if (attrs) {
      if (attrs.className) n.className = attrs.className;
      if (attrs.style) for (var k in attrs.style) n.style[k] = attrs.style[k];
      if (attrs.on) for (var ev in attrs.on) n.addEventListener(ev, attrs.on[ev]);
    }
    if (kids != null) {
      if (!Array.isArray(kids)) kids = [kids];
      kids.forEach(function (c) {
        if (c == null) return;
        n.appendChild(typeof c === 'string' ? document.createTextNode(c) : c);
      });
    }
    return n;
  }

  /* ---- Fisher–Yates shuffle (browser-side, per load) ---- */
  function shuffle(a) {
    var arr = a.slice();
    for (var i = arr.length - 1; i > 0; i--) {
      var j = Math.floor(Math.random() * (i + 1));
      var t = arr[i]; arr[i] = arr[j]; arr[j] = t;
    }
    return arr;
  }

  function init(container, config) {
    if (!container || !config) return;
    ensureStyles();

    var bins = config.bins || [];
    var cards = (config.cards || []).map(function (c, i) {
      return { id: c.id != null ? String(c.id) : ('c' + i), text: c.text, bin: c.bin };
    });
    // default tint = warm/cool alternation when a bin omits it
    bins.forEach(function (b, i) { if (!b.tint) b.tint = i % 2 ? 'cool' : 'warm'; });

    // state: which bin each card sits in (undefined = still in the tray)
    var placed = {};       // cardId -> binKey
    var selected = null;   // cardId currently selected in the tray
    var checked = false;   // has Check been pressed since the last change
    var order = shuffle(cards.map(function (c) { return c.id; }));  // tray display order (browser-shuffled)

    var byId = {}; cards.forEach(function (c) { byId[c.id] = c; });

    // ---- build fixed chrome once ----
    var root = el('div', { className: 'mrb-bins' });

    var head = el('div', { className: 'mrb-bins__head' }, [
      el('span', { style: { fontSize: 'calc(20px * var(--rd-fs-scale, 1))' } }, config.emoji || ''),
      el('h3', null, config.title || ''),
      config.subtitle ? el('span', { className: 'mrb-bins__sub' }, '— ' + config.subtitle) : null,
    ]);

    var scorePill = el('div', { className: 'mrb-bins__score' });
    var topRow = el('div', { className: 'mrb-bins__toprow' }, [
      el('p', { className: 'mrb-bins__prompt' }, config.prompt || ''),
      scorePill,
    ]);

    var trayLbl = el('div', { className: 'mrb-bins__tray-lbl' }, config.trayLabel || 'CARDS · tap one, then tap a bin');
    var pool = el('div', { className: 'mrb-bins__pool' });
    var trayEmpty = el('div', { className: 'mrb-bins__tray-empty' }, 'All sorted — hit Check answers below ↓');
    var tray = el('div', { className: 'mrb-bins__tray' }, [trayLbl, trayEmpty, pool]);

    var grid = el('div', { className: 'mrb-bins__grid' });
    grid.style.gridTemplateColumns = 'repeat(' + Math.min(bins.length, 3) + ', minmax(0, 1fr))';

    var checkBtn = el('button', { className: 'mrb-bins__check', on: { click: function () { checked = true; selected = null; render(); } } }, '✓ Check answers');
    var resetBtn = el('button', { className: 'mrb-bins__reset', on: { click: function () {
      placed = {}; selected = null; checked = false; order = shuffle(cards.map(function (c) { return c.id; })); render();
    } } }, '↻ Reset');
    var actions = el('div', { className: 'mrb-bins__actions' }, [checkBtn, resetBtn]);

    var body = el('div', { className: 'mrb-bins__body' }, [topRow, tray, grid, actions]);

    root.appendChild(head);
    root.appendChild(body);
    if (config.hint) root.appendChild(el('div', { className: 'mrb-bins__strap' }, config.hint));
    container.appendChild(root);

    // bin DOM built once; contents re-rendered each pass
    var binEls = bins.map(function (b) {
      var t = TINT[b.tint] || TINT.warm;
      var titleSpan = el('span', { className: 'mrb-bins__bin-title', style: { color: t.head } }, b.label || b.key);
      var headRow = el('div', { className: 'mrb-bins__bin-head' }, [
        b.emoji ? el('span', { style: { fontSize: 'calc(18px * var(--rd-fs-scale, 1))' } }, b.emoji) : null,
        titleSpan,
      ]);
      var placedWrap = el('div', { className: 'mrb-bins__placed' });
      var binBox = el('div', {
        className: 'mrb-bins__bin',
        style: { background: t.fill, border: '2px dashed ' + t.border },
        on: { click: function (e) {
          // clicking the bin background (not a placed card) drops the selected card
          if (e.target.closest('.mrb-bins__card')) return;
          if (!selected) return;
          placed[selected] = b.key; selected = null; checked = false; render();
        } },
      }, [headRow, placedWrap]);
      return { def: b, tint: t, box: binBox, placedWrap: placedWrap };
    });
    binEls.forEach(function (be) { grid.appendChild(be.box); });

    function trayCard(c) {
      return el('button', {
        className: 'mrb-bins__card' + (selected === c.id ? ' is-sel' : ''),
        on: { click: function () { selected = selected === c.id ? null : c.id; checked = false; render(); } },
      }, c.text);
    }

    function placedCard(c) {
      var style = {}, mark = '';
      if (checked) {
        var ok = placed[c.id] === c.bin;
        style.background = ok ? 'var(--ok-bg,#E7F3EA)' : 'var(--err-bg,#FBE4DE)';
        style.border = '1px solid ' + (ok ? 'var(--ok-border,#7FB98A)' : 'var(--err-border,#E0897B)');
        style.color = ok ? 'var(--ok,#2E6B3A)' : 'var(--err,#A83824)';
        mark = ok ? '✓' : '✕';
      }
      return el('button', {
        className: 'mrb-bins__card mrb-bins__card--placed',
        style: style,
        on: { click: function () { delete placed[c.id]; checked = false; selected = null; render(); } },
      }, [
        el('span', null, c.text),
        mark ? el('span', { className: 'mrb-bins__mark' }, mark) : null,
      ]);
    }

    function render() {
      // tray (browser-shuffled order, minus placed cards)
      pool.innerHTML = '';
      var inTray = order.filter(function (id) { return !(id in placed); });
      inTray.forEach(function (id) { pool.appendChild(trayCard(byId[id])); });
      trayEmpty.style.display = inTray.length ? 'none' : 'block';

      // bins
      binEls.forEach(function (be) {
        be.box.classList.toggle('is-target', !!selected);
        be.placedWrap.innerHTML = '';
        var here = cards.filter(function (c) { return placed[c.id] === be.def.key; });
        if (!here.length) {
          be.placedWrap.appendChild(el('div', { className: 'mrb-bins__bin-hint', style: { color: be.tint.hint } },
            selected ? 'Tap here to drop the selected card' : 'Tap a card above, then tap here'));
        } else {
          here.forEach(function (c) { be.placedWrap.appendChild(placedCard(c)); });
        }
      });

      // score pill
      var total = cards.length;
      var sorted = total - order.filter(function (id) { return !(id in placed); }).length;
      if (checked) {
        var correct = cards.filter(function (c) { return placed[c.id] === c.bin; }).length;
        scorePill.textContent = correct + ' / ' + total + ' correct' + (correct === total ? '  🎉' : '');
        var win = correct === total;
        scorePill.style.color = win ? 'var(--ok,#2E6B3A)' : 'var(--err,#A83824)';
        scorePill.style.background = win ? 'var(--ok-bg,#E7F3EA)' : 'var(--err-bg,#FBE4DE)';
      } else {
        scorePill.textContent = sorted === total ? 'Ready to check' : (sorted + ' / ' + total + ' sorted');
        scorePill.style.color = 'var(--ink-faint,#8A8074)';
        scorePill.style.background = 'var(--surface-inset,#EFE7D8)';
      }
    }

    render();
    return { render: render };
  }

  NS.categoriseBins = { init: init };
})();
