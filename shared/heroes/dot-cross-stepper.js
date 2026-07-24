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
      /* Fix 2 (MRB-134) — consistent secondary Reset, above the dark strap. */
      '.mrb-dcs__footer{display:flex;justify-content:flex-end;padding:10px 24px 12px;border-top:1px solid var(--surface-inset,#EFE7D8)}',
      '.mrb-dcs__reset{font-family:var(--font-mono,monospace);font-size: calc(12px * var(--rd-fs-scale, 1));font-weight:600;letter-spacing:.04em;color:var(--ink-muted,#6B635A);background:transparent;border:1px solid var(--border,#E4DCCB);border-radius:8px;padding:8px 14px;cursor:pointer;transition:border-color .15s,color .15s}',
      '.mrb-dcs__reset:hover{border-color:var(--accent-strong,#C0392B);color:var(--accent-deep,#B5341A)}',
      '.mrb-dcs__reset:focus-visible{outline:2px solid var(--accent-strong,#C0392B);outline-offset:2px}',
      /* MRB-134 Law 9: reduced-motion users get the instant end-state — the
         keyed viz nodes carry an unconditional CSS transition, so kill it here
         (a !important stylesheet rule beats the inline transition). */
      '@media (prefers-reduced-motion: reduce){.mrb-dcs__viz [data-k]{transition:none!important}}',
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

  /* ---- descriptor builders (MRB-134 Law 9) ----
     Each returns a keyed descriptor for the shared reconciler instead of
     a fresh DOM node. The geometry (pos/angles/coords) is identical to
     before; only the node lifecycle changes — nodes are reused across
     steps and their left/top updated, so the .75s CSS transition already
     on the ring / label / electron actually fires and the electron is
     SEEN travelling from shell to shell (never a frame swap). ---- */

  // one atom = a shell ring + a symbol/config label (+ optional charge
  // badge), keyed by the atom's stable `tag` so it persists across steps.
  function atomDescs(tag, sym, cfg, cx, cy, r, charge, showCharge) {
    var out = [];
    out.push({
      key: 'ring-' + tag,
      create: function () {
        return el('div', { style: {
          position: 'absolute', borderRadius: '50%', border: '2px solid #C9BFAD',
          background: 'radial-gradient(circle,#FFFDF8 55%,#F3ECDD)',
          transition: 'all .75s cubic-bezier(.5,0,.2,1)',
        } });
      },
      update: function (n) {
        n.style.left = (cx - r) + 'px'; n.style.top = (cy - r) + 'px';
        n.style.width = (2 * r) + 'px'; n.style.height = (2 * r) + 'px';
      },
    });
    out.push({
      key: 'label-' + tag,
      create: function () {
        return el('div', { style: {
          position: 'absolute', textAlign: 'center', pointerEvents: 'none',
          transition: 'all .75s cubic-bezier(.5,0,.2,1)',
        } }, [
          el('div', { style: { fontFamily: 'var(--font-display,sans-serif)', fontWeight: '700', fontSize: 'calc(26px * var(--rd-fs-scale, 1))', color: 'var(--ink,#1A1714)', lineHeight: '1' } }, sym),
          el('div', { className: 'mrb-dcs__cfg', style: { fontFamily: 'var(--font-mono,monospace)', fontSize: 'calc(11px * var(--rd-fs-scale, 1))', fontWeight: '700', color: 'var(--ink-muted,#6B635A)', marginTop: '3px' } }, cfg),
        ]);
      },
      update: function (n) {
        n.style.left = (cx - r) + 'px'; n.style.top = (cy - 22) + 'px'; n.style.width = (2 * r) + 'px';
        var c = n.querySelector('.mrb-dcs__cfg');
        if (c && c.textContent !== cfg) c.textContent = cfg;
      },
    });
    if (showCharge && charge) {
      var posv = charge.indexOf('+') >= 0;
      out.push({
        key: 'charge-' + tag,
        create: function () {
          return el('div', { style: {
            position: 'absolute', fontFamily: 'var(--font-display,sans-serif)', fontWeight: '700',
            fontSize: 'calc(15px * var(--rd-fs-scale, 1))', color: '#fff',
            background: posv ? '#B5341A' : '#2E7DD1', padding: '3px 9px', borderRadius: '999px',
            boxShadow: '0 4px 10px -3px rgba(0,0,0,.3)', transition: 'opacity .4s ease',
          } }, charge);
        },
        enter: function (n) { n.style.opacity = '0'; },   // the charge only exists once the transfer completes: fade it in
        update: function (n) {
          n.style.left = (cx + r - 14) + 'px'; n.style.top = (cy - r - 6) + 'px'; n.style.opacity = '1';
          if (n.textContent !== charge) n.textContent = charge;
        },
      });
    }
    return out;
  }

  // one electron: filled dot (•, from atom A) or hollow cross (×, from atom
  // B). `enterX/enterY` = its pre-move coordinates: a NEW node spawns there
  // and animates to (curX,curY); a reused node just moves there.
  function electronDesc(key, isDot, curX, curY, focus, enterX, enterY) {
    return {
      key: key,
      create: function () {
        return el('div', { style: {
          position: 'absolute', width: '18px', height: '18px',
          display: 'flex', alignItems: 'center', justifyContent: 'center', borderRadius: '50%',
          transition: 'all .75s cubic-bezier(.5,0,.2,1)',
          background: isDot ? '#B5341A' : 'transparent', color: isDot ? '#fff' : '#2E7DD1',
          fontSize: 'calc(17px * var(--rd-fs-scale, 1))', fontWeight: '700', fontFamily: 'var(--font-mono,monospace)', lineHeight: '1',
          boxShadow: isDot ? '0 2px 6px -2px rgba(181,52,26,.7)' : 'none',
        } }, isDot ? '' : '×');
      },
      enter: (enterX != null) ? function (n) { n.style.left = (enterX - 9) + 'px'; n.style.top = (enterY - 9) + 'px'; } : null,
      update: function (n) {
        n.style.left = (curX - 9) + 'px'; n.style.top = (curY - 9) + 'px';
        n.style.animation = (focus && !reduceMotion()) ? 'mrbPulseDot 1.3s ease-in-out infinite' : 'none';
      },
    };
  }

  /* ---- pure geometry → keyed descriptor list for the current phase ---- */
  function describeViz(m, phase) {
    var after = phase === 'moved', focus = phase === 'focus';
    var cy = 134;
    var out = [], L = m.left, Rt = m.right;

    if (m.mode === 'share') {
      var lx = after ? 280 : 170, rx = after ? 390 : 470, lxPre = 170, rxPre = 470;
      out = out.concat(atomDescs('L', L.sym, after ? L.cfgAfter : L.cfgBefore, lx, cy, L.r, '', false));
      out = out.concat(atomDescs('R', Rt.sym, after ? Rt.cfgAfter : Rt.cfgBefore, rx, cy, Rt.r, '', false));
      var spare = [-90, -45, 0, 45, 90, 135, -135].slice(0, Rt.outer - 1);
      spare.forEach(function (deg, k) {
        var p = pos(rx, cy, Rt.r, deg), pre = pos(rxPre, cy, Rt.r, deg);
        out.push(electronDesc('nfix-' + k, false, p.x, p.y, false, pre.x, pre.y));
      });
      var pairX = 322;
      var dp = after ? { x: pairX, y: cy - 11 } : pos(lx, cy, L.r, 0);
      var xp = after ? { x: pairX, y: cy + 11 } : pos(rx, cy, Rt.r, 180);
      var dpPre = pos(lxPre, cy, L.r, 0), xpPre = pos(rxPre, cy, Rt.r, 180);
      out.push(electronDesc('pair-dot', true, dp.x, dp.y, focus, dpPre.x, dpPre.y));
      out.push(electronDesc('pair-cross', false, xp.x, xp.y, focus, xpPre.x, xpPre.y));
    } else if (m.layout === 'di') {
      var mx = 150, nx = 490;
      out = out.concat(atomDescs('L', L.sym, after ? L.cfgAfter : L.cfgBefore, mx, cy, L.r, L.charge, after));
      out = out.concat(atomDescs('R', Rt.sym, after ? Rt.cfgAfter : Rt.cfgBefore, nx, cy, Rt.r, Rt.charge, after));
      var nonAngles, incomingSlots, metalStart;
      if (Rt.outer === 7) { nonAngles = [-90, -45, 0, 45, 90, 135, -135]; incomingSlots = [180]; metalStart = [0]; }
      else { nonAngles = [-90, -45, 0, 45, 90, -135]; incomingSlots = [135, 180]; metalStart = [-22, 22]; }
      nonAngles.forEach(function (deg, k) { var p = pos(nx, cy, Rt.r, deg); out.push(electronDesc('nfix-' + k, false, p.x, p.y, false)); });
      metalStart.slice(0, L.outer).forEach(function (deg, k) {
        var pre = pos(mx, cy, L.r, deg);
        var p = after ? pos(nx, cy, Rt.r, incomingSlots[k]) : pre;
        out.push(electronDesc('etr-' + k, true, p.x, p.y, focus, pre.x, pre.y));
      });
    } else {
      // tri: metal centre, a non-metal each side (e.g. MgCl₂ — two 1-electron transfers)
      var R = 58, mgx = 320, clL = 108, clR = 532;
      out = out.concat(atomDescs('C', L.sym, after ? L.cfgAfter : L.cfgBefore, mgx, cy, R, L.charge, after));
      out = out.concat(atomDescs('R', Rt.sym, after ? Rt.cfgAfter : Rt.cfgBefore, clL, cy, R, Rt.charge, after));
      out = out.concat(atomDescs('R2', Rt.sym, after ? Rt.cfgAfter : Rt.cfgBefore, clR, cy, R, Rt.charge, after));
      [-90, -45, 45, 90, 135, 180, -135].forEach(function (deg, k) { var p = pos(clL, cy, R, deg); out.push(electronDesc('nfixL-' + k, false, p.x, p.y, false)); });
      [-90, -45, 0, 45, 90, 135, -135].forEach(function (deg, k) { var p = pos(clR, cy, R, deg); out.push(electronDesc('nfixR-' + k, false, p.x, p.y, false)); });
      [{ from: 180, tx: clL, ta: 0 }, { from: 0, tx: clR, ta: 180 }].forEach(function (s, k) {
        var pre = pos(mgx, cy, R, s.from);
        var p = after ? pos(s.tx, cy, R, s.ta) : pre;
        out.push(electronDesc('etr-' + k, true, p.x, p.y, focus, pre.x, pre.y));
      });
    }
    return out;
  }

  /* keyed paint with a graceful fallback if the reconciler is absent */
  function paintViz(stage, descriptors, reduce) {
    if (window.MrbKeyedRender) { MrbKeyedRender.reconcile(stage, descriptors, { reduceMotion: reduce }); return; }
    stage.innerHTML = ''; stage.__mrbKeyed = {};
    descriptors.forEach(function (d) {
      var n = d.create(); if (n && n.setAttribute) n.setAttribute('data-k', d.key);
      if (d.update) d.update(n, true); stage.appendChild(n);
    });
  }

  // Law 9 detail: the receiving shell highlights the moment the transferred
  // electron arrives — driven by the electron's own transitionend, not a timer.
  function armReceiveHighlight(stage, m) {
    var travelKey = (m.mode === 'share') ? 'pair-dot' : 'etr-0';
    var rings = (m.mode === 'share') ? ['ring-L', 'ring-R']
      : (m.layout === 'di') ? ['ring-R'] : ['ring-R', 'ring-R2'];
    var e = stage.querySelector('[data-k="' + travelKey + '"]');
    if (!e) return;
    var done = false;
    function onEnd(ev) {
      if (done || (ev.propertyName !== 'left' && ev.propertyName !== 'top')) return;
      done = true;
      e.removeEventListener('transitionend', onEnd);
      rings.forEach(function (rk) {
        var r = stage.querySelector('[data-k="' + rk + '"]');
        if (!r) return;
        var prior = r.style.boxShadow;
        r.style.boxShadow = '0 0 0 5px rgba(155,208,166,.75)';   // sage "received" glow
        setTimeout(function () { r.style.boxShadow = prior || 'none'; }, 900);
      });
    }
    e.addEventListener('transitionend', onEnd);
  }

  function init(container, config) {
    if (!container || !config) return;
    ensureStyles();
    var molecules = config.molecules || [];
    if (!molecules.length) return;
    var mi = 0, step = 0;
    var stage = null, lastMi = -1;   // persistent coordinate space for keyed render
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

    // Fix 2 (MRB-134): consistent secondary reset — back to step 1 and re-arm
    // the predict wager. Placed in a footer just above the dark result strap.
    var resetBtn = el('button', { className: 'mrb-dcs__reset', attrs: { type: 'button', 'aria-label': 'Reset this walkthrough to step 1' },
      on: { click: function () { step = 0; if (gate) gate.reset(); render(); } } }, '↺ Reset');
    var footer = el('div', { className: 'mrb-dcs__footer' }, resetBtn);

    if (gate) root.appendChild(gate.el);   // Phase 1a: wager row above the viz
    root.appendChild(vizWrap);
    root.appendChild(ctrls);
    root.appendChild(stepBox);
    root.appendChild(footer);
    root.appendChild(result);
    container.appendChild(root);

    function render() {
      var m = molecules[mi], steps = m.steps, last = steps.length - 1;
      var stp = steps[step];
      // viz — MRB-134 Law 9: reuse the coordinate stage and keyed-reconcile
      // its children so electrons visibly travel between shells rather than
      // being torn down and rebuilt (the old innerHTML='' frame swap).
      if (!stage) {
        stage = el('div', { style: { position: 'relative', width: '640px', height: '280px', margin: '0 auto' } });
        vizWrap.appendChild(stage);
      }
      if (mi !== lastMi) {   // molecule switch = a different diagram: start fresh, never morph across molecules
        stage.innerHTML = ''; stage.__mrbKeyed = {}; stage.__phase = null; lastMi = mi;
      }
      var reduce = window.MrbKeyedRender ? MrbKeyedRender.reduceMotion() : reduceMotion();
      var prevPhase = stage.__phase;
      paintViz(stage, describeViz(m, stp.phase), reduce);
      if (stp.phase === 'moved' && prevPhase && prevPhase !== 'moved' && !reduce) armReceiveHighlight(stage, m);
      stage.__phase = stp.phase;
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
