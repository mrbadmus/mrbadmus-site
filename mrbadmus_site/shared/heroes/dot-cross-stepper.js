/* ============================================================
   MrBadmus Hero — DOT-AND-CROSS STEPPER  (vanilla, net-new)
   Archetype 02. Two (or three) atoms drawn as electron shells; an
   ordered step sequence moves the outer electrons by TRANSFER
   (ionic) or SHARE (covalent), one caption per step, plus a final
   structure line. Optional molecule picker steps between several
   molecules in one hero (still one teaching interaction).

   Ported 1:1 from Design's `Bonding Hero 2 - Dot-and-Cross
   Stepper.dc.html`. No React, no build step. Locked-token colours;
   the focus pulse respects prefers-reduced-motion.

   PUBLIC API:
     MrbHeroes.dotCrossStepper.init(container, config)

   CONFIG SCHEMA:
   {
     emoji, title : string           // hero header
     molecules: [ {                  // 1+; a picker shows when >1
       name  : string,               // picker tab label
       mode  : 'transfer' | 'share',
       layout: 'di' | 'tri',         // di = left+right; tri = metal centre + 2 non-metals
       left  : { sym, cfgBefore, cfgAfter, charge, outer, r },
       right : { sym, cfgBefore, cfgAfter, charge, outer, r },
       steps : [ { phase:'neutral'|'focus'|'moved', title, caption } ],
       result: string                // final-structure line (dark bar, last step)
     } ]
   }
   Geometry (electronModel/buildViz) is pure and separate from the
   render/binding, exactly like the shipped heroes.
============================================================ */
(function () {
  'use strict';
  var NS = (window.MrbHeroes = window.MrbHeroes || {});
  if (NS.dotCrossStepper) return;

  var STYLE_ID = 'mrb-hero-dcs-styles';
  function ensureStyles() {
    if (document.getElementById(STYLE_ID)) return;
    var s = document.createElement('style');
    s.id = STYLE_ID;
    s.textContent = [
      '@keyframes mrbPulseDot{0%,100%{box-shadow:0 0 0 0 rgba(224,83,31,.55)}50%{box-shadow:0 0 0 9px rgba(224,83,31,0)}}',
      '.mrb-dcs,.mrb-dcs *{box-sizing:border-box}',
      '.mrb-dcs{font-family:var(--font-body,system-ui,sans-serif);background:var(--surface-panel,#FFFDF8);border:1px solid var(--border,#E4DCCB);border-radius:var(--r-panel,22px);box-shadow:var(--shadow-panel,0 22px 50px -35px rgba(60,30,20,.5));overflow:hidden}',
      '.mrb-dcs__head{display:flex;align-items:center;gap:10px;padding:16px 24px;border-bottom:1px solid var(--surface-inset,#EFE7D8);flex-wrap:wrap}',
      '.mrb-dcs__head h3{font-family:var(--font-display,sans-serif);font-weight:700;font-size: calc(18px * var(--rd-fs-scale, 1));color:var(--ink,#1A1714);margin:0;min-width:0;overflow-wrap:anywhere}',
      '.mrb-dcs__sub{font-family:var(--font-mono,monospace);font-size: calc(12px * var(--rd-fs-scale, 1));font-weight:700;color:var(--ink-muted,#6B635A)}',
      '.mrb-dcs__picker{display:flex;gap:8px;flex-wrap:wrap;padding:12px 24px 0}',
      '.mrb-dcs__tab{font-family:var(--font-display,sans-serif);font-weight:700;font-size: calc(13.5px * var(--rd-fs-scale, 1));cursor:pointer;border-radius:999px;padding:7px 15px;color:#4A4238;background:var(--surface-inset,#EFE7D8);border:1px solid var(--border,#E4DCCB)}',
      '.mrb-dcs__tab.is-active{color:#fff;background:var(--surface-dark,#1A1714);border-color:var(--surface-dark,#1A1714)}',
      '.mrb-dcs__viz{padding:8px 18px 0;overflow-x:auto}',
      '.mrb-dcs__ctrls{display:flex;align-items:center;gap:14px;padding:6px 24px 14px;flex-wrap:wrap}',
      '.mrb-dcs__nav{font-family:var(--font-display,sans-serif);font-weight:700;font-size: calc(14px * var(--rd-fs-scale, 1));border-radius:10px;padding:10px 18px;cursor:pointer;transition:all .15s}',
      '.mrb-dcs__nav--back{color:#4A4238;background:var(--surface-inset,#EFE7D8);border:1px solid var(--border,#E4DCCB)}',
      '.mrb-dcs__nav--next{color:#fff;background:var(--accent-deep,#B5341A);border:none;box-shadow:0 8px 20px -8px rgba(181,52,26,.6)}',
      '.mrb-dcs__nav:disabled{color:#B0A695;background:var(--surface-inset,#EFE7D8);border:1px solid var(--border,#E4DCCB);box-shadow:none;cursor:not-allowed}',
      '.mrb-dcs__dots{display:flex;gap:7px;align-items:center}',
      '.mrb-dcs__dot{height:10px;border-radius:999px;border:none;cursor:pointer;padding:0;transition:all .25s;background:#DCD3C2}',
      '.mrb-dcs__dot.is-done{background:var(--accent-deep,#B5341A)}',
      '.mrb-dcs__count{font-family:var(--font-mono,monospace);font-size: calc(12px * var(--rd-fs-scale, 1));font-weight:700;color:var(--ink-muted,#6B635A);margin-left:auto}',
      '.mrb-dcs__step{margin:0 24px 18px;background:var(--surface-inset,#F7F2E8);border-radius:12px;padding:14px 18px}',
      '.mrb-dcs__step-t{font-family:var(--font-display,sans-serif);font-weight:700;font-size: calc(15px * var(--rd-fs-scale, 1));color:var(--ink,#1A1714);margin-bottom:3px}',
      '.mrb-dcs__step-c{font-size: calc(14px * var(--rd-fs-scale, 1));line-height:1.55;color:#3A322A}',
      '.mrb-dcs__result{padding:13px 24px;background:var(--surface-dark,#1A1714);font-family:var(--font-mono,monospace);font-size: calc(12.5px * var(--rd-fs-scale, 1));line-height:1.5}',
    ].join('');
    document.head.appendChild(s);
  }

  /* ---- tiny DOM helper (attrs style, same shape as categorise-bins) ---- */
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

  function reduceMotion() {
    return window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  }

  function pos(cx, cy, r, deg) { var a = deg * Math.PI / 180; return { x: cx + r * Math.cos(a), y: cy + r * Math.sin(a) }; }

  /* ---- one atom: shell ring + symbol/config label + optional charge badge ---- */
  function atomEls(sym, cfg, cx, cy, r, charge, showCharge) {
    var out = [];
    out.push(el('div', { style: {
      position: 'absolute', left: (cx - r) + 'px', top: (cy - r) + 'px', width: (2 * r) + 'px', height: (2 * r) + 'px',
      borderRadius: '50%', border: '2px solid #C9BFAD', background: 'radial-gradient(circle,#FFFDF8 55%,#F3ECDD)',
      transition: 'all .75s cubic-bezier(.5,0,.2,1)',
    } }));
    out.push(el('div', { style: {
      position: 'absolute', left: (cx - r) + 'px', top: (cy - 22) + 'px', width: (2 * r) + 'px', textAlign: 'center',
      pointerEvents: 'none', transition: 'all .75s cubic-bezier(.5,0,.2,1)',
    } }, [
      el('div', { style: { fontFamily: 'var(--font-display,sans-serif)', fontWeight: '700', fontSize: 'calc(26px * var(--rd-fs-scale, 1))', color: 'var(--ink,#1A1714)', lineHeight: '1' } }, sym),
      el('div', { style: { fontFamily: 'var(--font-mono,monospace)', fontSize: 'calc(11px * var(--rd-fs-scale, 1))', fontWeight: '700', color: 'var(--ink-muted,#6B635A)', marginTop: '3px' } }, cfg),
    ]));
    if (showCharge && charge) {
      var posv = charge.indexOf('+') >= 0;
      out.push(el('div', { style: {
        position: 'absolute', left: (cx + r - 14) + 'px', top: (cy - r - 6) + 'px',
        fontFamily: 'var(--font-display,sans-serif)', fontWeight: '700', fontSize: 'calc(15px * var(--rd-fs-scale, 1))',
        color: '#fff', background: posv ? '#B5341A' : '#2E7DD1', padding: '3px 9px', borderRadius: '999px',
        boxShadow: '0 4px 10px -3px rgba(0,0,0,.3)',
      } }, charge));
    }
    return out;
  }

  /* ---- one electron: filled dot (•, from atom A) or hollow cross (×, from atom B) ---- */
  function dotEl(x, y, isDot, focus) {
    var st = {
      position: 'absolute', left: (x - 9) + 'px', top: (y - 9) + 'px', width: '18px', height: '18px',
      display: 'flex', alignItems: 'center', justifyContent: 'center', borderRadius: '50%',
      transition: 'all .75s cubic-bezier(.5,0,.2,1)',
      background: isDot ? '#B5341A' : 'transparent', color: isDot ? '#fff' : '#2E7DD1',
      fontSize: 'calc(17px * var(--rd-fs-scale, 1))', fontWeight: '700', fontFamily: 'var(--font-mono,monospace)', lineHeight: '1',
      boxShadow: isDot ? '0 2px 6px -2px rgba(181,52,26,.7)' : 'none',
    };
    if (focus && !reduceMotion()) st.animation = 'mrbPulseDot 1.3s ease-in-out infinite';
    return el('div', { style: st }, isDot ? '' : '×');
  }

  /* ---- pure geometry for the current phase ---- */
  function buildViz(m, phase) {
    var after = phase === 'moved', focus = phase === 'focus';
    var W = 640, H = 280, cy = 134;
    var els = [], L = m.left, Rt = m.right, i;

    if (m.mode === 'share') {
      var lx = after ? 280 : 170, rx = after ? 390 : 470;
      els = els.concat(atomEls(L.sym, after ? L.cfgAfter : L.cfgBefore, lx, cy, L.r, '', false));
      els = els.concat(atomEls(Rt.sym, after ? Rt.cfgAfter : Rt.cfgBefore, rx, cy, Rt.r, '', false));
      var spare = [-90, -45, 0, 45, 90, 135, -135].slice(0, Rt.outer - 1);
      spare.forEach(function (deg) { var p = pos(rx, cy, Rt.r, deg); els.push(dotEl(p.x, p.y, false, false)); });
      var pairX = 322;
      var dp = after ? { x: pairX, y: cy - 11 } : pos(lx, cy, L.r, 0);
      var xp = after ? { x: pairX, y: cy + 11 } : pos(rx, cy, Rt.r, 180);
      els.push(dotEl(dp.x, dp.y, true, focus));
      els.push(dotEl(xp.x, xp.y, false, focus));
    } else if (m.layout === 'di') {
      var mx = 150, nx = 490;
      els = els.concat(atomEls(L.sym, after ? L.cfgAfter : L.cfgBefore, mx, cy, L.r, L.charge, after));
      els = els.concat(atomEls(Rt.sym, after ? Rt.cfgAfter : Rt.cfgBefore, nx, cy, Rt.r, Rt.charge, after));
      var nonAngles, incomingSlots, metalStart;
      if (Rt.outer === 7) { nonAngles = [-90, -45, 0, 45, 90, 135, -135]; incomingSlots = [180]; metalStart = [0]; }
      else { nonAngles = [-90, -45, 0, 45, 90, -135]; incomingSlots = [135, 180]; metalStart = [-22, 22]; }
      nonAngles.forEach(function (deg) { var p = pos(nx, cy, Rt.r, deg); els.push(dotEl(p.x, p.y, false, false)); });
      metalStart.slice(0, L.outer).forEach(function (deg, k) {
        var p = after ? pos(nx, cy, Rt.r, incomingSlots[k]) : pos(mx, cy, L.r, deg);
        els.push(dotEl(p.x, p.y, true, focus));
      });
    } else {
      // tri: metal centre, a non-metal each side (e.g. MgCl₂ — two 1-electron transfers)
      var R = 58, mgx = 320, clL = 108, clR = 532;
      els = els.concat(atomEls(L.sym, after ? L.cfgAfter : L.cfgBefore, mgx, cy, R, L.charge, after));
      els = els.concat(atomEls(Rt.sym, after ? Rt.cfgAfter : Rt.cfgBefore, clL, cy, R, Rt.charge, after));
      els = els.concat(atomEls(Rt.sym, after ? Rt.cfgAfter : Rt.cfgBefore, clR, cy, R, Rt.charge, after));
      [-90, -45, 45, 90, 135, 180, -135].forEach(function (deg) { var p = pos(clL, cy, R, deg); els.push(dotEl(p.x, p.y, false, false)); });
      [-90, -45, 0, 45, 90, 135, -135].forEach(function (deg) { var p = pos(clR, cy, R, deg); els.push(dotEl(p.x, p.y, false, false)); });
      [{ from: 180, tx: clL, ta: 0 }, { from: 0, tx: clR, ta: 180 }].forEach(function (s) {
        var p = after ? pos(s.tx, cy, R, s.ta) : pos(mgx, cy, R, s.from);
        els.push(dotEl(p.x, p.y, true, focus));
      });
    }
    return el('div', { style: { position: 'relative', width: W + 'px', height: H + 'px', margin: '0 auto' } }, els);
  }

  function init(container, config) {
    if (!container || !config) return;
    ensureStyles();
    var molecules = config.molecules || [];
    if (!molecules.length) return;
    var mi = 0, step = 0;
    // Phase 1a (MRB-133): optional predict gate on reaching the reveal step
    var gate = (config.predict && window.MrbPredictWrapper)
      ? MrbPredictWrapper.create(config.predict) : null;
    function goTo(k) {
      var key = 'step:' + k;
      if (k > step && gate && !gate.allow(key)) return;
      step = k; render();
      if (gate) gate.resolveIf(key);
    }

    var root = el('div', { className: 'mrb-dcs' });
    root.appendChild(el('div', { className: 'mrb-dcs__head' }, [
      el('span', { style: { fontSize: 'calc(20px * var(--rd-fs-scale, 1))' } }, config.emoji || '⚛️'),
      el('h3', null, config.title || 'Dot-and-Cross'),
      el('span', { className: 'mrb-dcs__sub' }, '— dots (•) from one atom, crosses (×) from the other'),
    ]));

    var pickerWrap = null, tabEls = [];
    if (molecules.length > 1) {
      pickerWrap = el('div', { className: 'mrb-dcs__picker' });
      tabEls = molecules.map(function (m, k) {
        var t = el('button', { className: 'mrb-dcs__tab', attrs: { type: 'button' },
          on: { click: function () { mi = k; step = 0; render(); } } }, m.name || ('Molecule ' + (k + 1)));
        pickerWrap.appendChild(t); return t;
      });
      root.appendChild(pickerWrap);
    }

    var vizWrap = el('div', { className: 'mrb-dcs__viz' });
    var backBtn = el('button', { className: 'mrb-dcs__nav mrb-dcs__nav--back', attrs: { type: 'button' },
      on: { click: function () { step = Math.max(0, step - 1); render(); } } }, '← Back');
    var dotsWrap = el('div', { className: 'mrb-dcs__dots' });
    var nextBtn = el('button', { className: 'mrb-dcs__nav mrb-dcs__nav--next', attrs: { type: 'button' },
      on: { click: function () { var last = molecules[mi].steps.length - 1; goTo(Math.min(last, step + 1)); } } }, 'Next →');
    var count = el('span', { className: 'mrb-dcs__count' });
    var ctrls = el('div', { className: 'mrb-dcs__ctrls' }, [backBtn, dotsWrap, nextBtn, count]);

    var stepBox = el('div', { className: 'mrb-dcs__step' });
    var stepT = el('div', { className: 'mrb-dcs__step-t' });
    var stepC = el('div', { className: 'mrb-dcs__step-c' });
    stepBox.appendChild(stepT); stepBox.appendChild(stepC);

    var result = el('div', { className: 'mrb-dcs__result' });

    if (gate) root.appendChild(gate.el);   // Phase 1a: wager row above the viz
    root.appendChild(vizWrap);
    root.appendChild(ctrls);
    root.appendChild(stepBox);
    root.appendChild(result);
    container.appendChild(root);

    function render() {
      var m = molecules[mi], steps = m.steps, last = steps.length - 1;
      var stp = steps[step];
      // viz
      vizWrap.innerHTML = '';
      vizWrap.appendChild(buildViz(m, stp.phase));
      // Phase 0c (MRB-132): name the dot-and-cross diagram per molecule + step
      // so screen-reader users get the same story the animation tells.
      vizWrap.setAttribute('role', 'img');
      vizWrap.setAttribute('aria-label', 'Dot-and-cross diagram: ' + (m.name || '')
        + '. Step ' + (step + 1) + ' of ' + steps.length + ': ' + (stp.title || '')
        + '. ' + (stp.caption || ''));
      // picker active
      tabEls.forEach(function (t, k) { t.classList.toggle('is-active', k === mi); });
      // nav
      backBtn.disabled = step === 0;
      nextBtn.disabled = step === last;
      nextBtn.textContent = step === last ? '✓ Done' : 'Next →';
      // dots
      dotsWrap.innerHTML = '';
      steps.forEach(function (_, k) {
        var d = el('button', { className: 'mrb-dcs__dot' + (k <= step ? ' is-done' : ''),
          style: { width: k === step ? '26px' : '10px' }, attrs: { type: 'button', 'aria-label': 'Go to step ' + (k + 1) },
          on: { click: function () { goTo(k); } } });
        dotsWrap.appendChild(d);
      });
      count.textContent = 'STEP ' + (step + 1) + ' / ' + steps.length;
      // caption
      stepT.textContent = stp.title || '';
      stepC.textContent = stp.caption || '';
      // result bar
      if (step === last) { result.textContent = m.result || ''; result.style.color = '#9BD0A6'; }
      else { result.textContent = 'Final structure: … (step through to build it)'; result.style.color = 'var(--ink-faint,#8A8074)'; }
    }
    render();
    return { render: render };
  }

  NS.dotCrossStepper = { init: init };
})();
