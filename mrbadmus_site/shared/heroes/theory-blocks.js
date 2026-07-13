/* ============================================================
   MrBadmus Theory Blocks — INTERACTIVE members of the canonical
   Bonding Theory Block Library (MRB-113 Phase B).

   The seven STATIC blocks (lead, feature-cards, compare-cards,
   step-sequence, example-callout, aside-callout, key-note) are
   emitted as plain HTML by the generator (bonding_redesign.py) —
   they need no JS. This module carries only the TWO interactive
   blocks, ported 1:1 from the React renderers in
   `docs/redesign/Bonding Theory Block Library.dc.html`:

     · mistakeCheck  — spot the error, then reveal the correction
     · compareReveal — tap a property to reveal its structural cause

   Data-separate, like the heroes: content lives in the per-page
   config the generator passes to init(); this file holds only the
   Locked-token shell + interaction logic. Colours are the block
   library's exact (signed-off) values; fonts resolve through the
   Locked tokens on `.rd` pages (Space Grotesk / IBM Plex).
============================================================ */
(function () {
  'use strict';
  var NS = (window.MrbTheoryBlocks = window.MrbTheoryBlocks || {});
  if (NS.__init) return;
  NS.__init = true;

  var STYLE_ID = 'mrb-theory-blocks-styles';
  function ensureStyles() {
    if (document.getElementById(STYLE_ID)) return;
    var s = document.createElement('style');
    s.id = STYLE_ID;
    s.textContent = [
      '.mrb-tb,.mrb-tb *{box-sizing:border-box}',
      /* ---- mistake-check ---- */
      '.mrb-tb-mistake{background:linear-gradient(180deg,#FBE7E2,#F8E0DA);border:1px solid #EBBCB1;border-left:5px solid var(--accent-strong,#C0392B);border-radius:var(--r-callout,18px);padding:22px 26px}',
      '.mrb-tb-mistake__hd{display:flex;align-items:center;gap:10px;margin-bottom:14px}',
      '.mrb-tb-mistake__hd b{font-family:var(--font-display,sans-serif);font-weight:700;font-size: calc(17px * var(--rd-fs-scale, 1));color:var(--accent-deep,#B5341A)}',
      '.mrb-tb-mistake__tag{font-family:var(--font-mono,monospace);font-size: calc(12px * var(--rd-fs-scale, 1));font-weight:700;letter-spacing:.1em;color:#865D54;margin-left:auto}',
      '.mrb-tb-mistake__claim{background:var(--surface-panel,#FFFDF8);border:1px solid #EBBCB1;border-radius:12px;padding:16px 20px;margin-bottom:14px}',
      '.mrb-tb-mistake__claim-lbl{font-family:var(--font-mono,monospace);font-size: calc(12px * var(--rd-fs-scale, 1));font-weight:700;letter-spacing:.1em;color:#716A60;margin-bottom:6px}',
      '.mrb-tb-mistake__claim-txt{font-family:var(--font-display,sans-serif);font-weight:700;font-size: calc(16px * var(--rd-fs-scale, 1));line-height:1.4;color:#7A241A}',
      '.mrb-tb-mistake__prompt{font-size: calc(14px * var(--rd-fs-scale, 1));font-weight:600;color:#3A2A26;margin-bottom:10px}',
      '.mrb-tb-mistake__opts{display:flex;flex-direction:column;gap:9px}',
      '.mrb-tb-mistake__opt{font-family:var(--font-body,system-ui,sans-serif);font-size: calc(14px * var(--rd-fs-scale, 1));line-height:1.5;text-align:left;width:100%;cursor:pointer;background:var(--surface-panel,#FFFDF8);border:1.5px solid #EBBCB1;color:#3A2A26;border-radius:11px;padding:13px 16px;transition:all .15s}',
      '.mrb-tb-mistake.is-answered .mrb-tb-mistake__opt{cursor:default}',
      '.mrb-tb-mistake__opt.is-correct{background:var(--ok-bg,#E7F3EA);border-color:var(--ok-border,#7FB98A);color:var(--ok,#2E6B3A)}',
      '.mrb-tb-mistake__opt.is-wrong{background:var(--err-bg,#FBE4DE);border-color:var(--err-border,#E0897B);color:var(--err,#A83824)}',
      '.mrb-tb-mistake__opt.is-dim{color:#9A9082}',
      '.mrb-tb-mistake__fix{margin-top:14px;background:var(--accent-wash,#FBEEE9);border-left:4px solid var(--accent-strong,#C0392B);border-radius:12px;padding:16px 20px}',
      '.mrb-tb-mistake__fix-hd{display:flex;align-items:center;gap:8px;margin-bottom:6px}',
      '.mrb-tb-mistake__fix-hd b{font-family:var(--font-display,sans-serif);font-weight:700;font-size: calc(15px * var(--rd-fs-scale, 1));color:var(--accent-deep,#B5341A)}',
      '.mrb-tb-mistake__fix p{margin:0;font-size: calc(14.5px * var(--rd-fs-scale, 1));line-height:1.65;color:#3A2A26}',
      /* ---- compare-reveal ---- */
      '.mrb-tb-reveal__title{font-family:var(--font-mono,monospace);font-size: calc(13px * var(--rd-fs-scale, 1));font-weight:600;color:#675F56;margin-bottom:10px}',
      '.mrb-tb-reveal__rows{display:flex;flex-direction:column;gap:9px}',
      '.mrb-tb-reveal__row{border:1px solid var(--border,#E4DCCB);border-radius:12px;overflow:hidden;background:var(--surface-panel,#FFFDF8)}',
      '.mrb-tb-reveal__btn{display:flex;align-items:center;justify-content:space-between;gap:12px;width:100%;text-align:left;cursor:pointer;border:none;background:var(--surface-panel,#FFFDF8);padding:13px 16px;font-family:var(--font-display,sans-serif);font-weight:700;font-size: calc(14.5px * var(--rd-fs-scale, 1));color:var(--ink,#1A1714);transition:all .15s}',
      '.mrb-tb-reveal__row.is-open .mrb-tb-reveal__btn{background:var(--surface-inset,#F7F2E8)}',
      '.mrb-tb-reveal__why{font-family:var(--font-mono,monospace);font-size: calc(12px * var(--rd-fs-scale, 1));font-weight:600;color:var(--accent-deep,#B5341A);flex:none}',
      '.mrb-tb-reveal__cause{padding:4px 16px 14px;font-size: calc(14px * var(--rd-fs-scale, 1));line-height:1.55;color:#3A2A26}',
    ].join('');
    document.head.appendChild(s);
  }

  /* ---- tiny DOM helper (same shape as the heroes') ---- */
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

  /* ================= mistake-check ================= */
  /* One state var: selected index (set once). Click → reveal fix. */
  function initMistakeCheck(container, config) {
    if (!container || !config) return;
    ensureStyles();
    var options = config.options || [];
    var selected = null;

    var root = el('div', { className: 'mrb-tb mrb-tb-mistake' });

    function render() {
      root.innerHTML = '';
      var answered = selected !== null;
      if (answered) root.classList.add('is-answered');

      root.appendChild(el('div', { className: 'mrb-tb-mistake__hd' }, [
        el('span', { style: { fontSize: 'calc(20px * var(--rd-fs-scale, 1))' } }, '⚠️'),
        el('b', null, 'Common Mistake'),
        el('span', { className: 'mrb-tb-mistake__tag' }, 'SPOT THE ERROR'),
      ]));

      root.appendChild(el('div', { className: 'mrb-tb-mistake__claim' }, [
        el('div', { className: 'mrb-tb-mistake__claim-lbl' }, 'A STUDENT WROTE:'),
        el('div', { className: 'mrb-tb-mistake__claim-txt' }, config.claim || ''),
      ]));

      root.appendChild(el('div', { className: 'mrb-tb-mistake__prompt' },
        config.prompt || 'What is the flaw in this reasoning?'));

      var opts = options.map(function (o, idx) {
        var cls = 'mrb-tb-mistake__opt';
        if (answered) {
          if (o.correct) cls += ' is-correct';
          else if (idx === selected) cls += ' is-wrong';
          else cls += ' is-dim';
        }
        return el('button', {
          className: cls,
          on: { click: function () { if (selected === null) { selected = idx; render(); } } },
        }, o.text);
      });
      root.appendChild(el('div', { className: 'mrb-tb-mistake__opts' }, opts));

      if (answered) {
        root.appendChild(el('div', { className: 'mrb-tb-mistake__fix' }, [
          el('div', { className: 'mrb-tb-mistake__fix-hd' }, [
            el('span', { style: { fontSize: 'calc(16px * var(--rd-fs-scale, 1))' } }, '✅'),
            el('b', null, 'The correction'),
          ]),
          el('p', null, config.fix || ''),
        ]));
      }
    }

    render();
    container.appendChild(root);
  }

  /* ================= compare-reveal ================= */
  /* open/closed flag per item (click to toggle). */
  function initCompareReveal(container, config) {
    if (!container || !config) return;
    ensureStyles();
    var items = config.items || [];
    var open = {};

    var root = el('div', { className: 'mrb-tb mrb-tb-reveal' });

    function render() {
      root.innerHTML = '';
      if (config.title) root.appendChild(el('div', { className: 'mrb-tb-reveal__title' }, config.title));
      var rows = items.map(function (it, idx) {
        var isOpen = !!open[idx];
        var row = el('div', { className: 'mrb-tb-reveal__row' + (isOpen ? ' is-open' : '') });
        row.appendChild(el('button', {
          className: 'mrb-tb-reveal__btn',
          on: { click: function () { open[idx] = !open[idx]; render(); } },
        }, [
          el('span', null, it.property),
          el('span', { className: 'mrb-tb-reveal__why' }, isOpen ? 'why ▲' : 'why ▼'),
        ]));
        if (isOpen) row.appendChild(el('div', { className: 'mrb-tb-reveal__cause' }, it.cause));
        return row;
      });
      root.appendChild(el('div', { className: 'mrb-tb-reveal__rows' }, rows));
    }

    render();
    container.appendChild(root);
  }

  NS.mistakeCheck = { init: initMistakeCheck };
  NS.compareReveal = { init: initCompareReveal };
})();
