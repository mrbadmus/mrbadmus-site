/* ============================================================
   MrBadmus Hero — STATE TOGGLE LAB  (vanilla, net-new)
   Archetype 01. A giant ionic lattice with a state toggle: each
   state rearranges the ions and updates a "does it conduct?"
   verdict. An optional force button tests brittleness (the
   lattice shears → like charges repel → it shatters).

   Ported 1:1 from Design's `Bonding Hero 1 - State Toggle Lab
   .dc.html`. No React, no build step. Locked-token colours; the
   jiggle and bulb-glow animations respect prefers-reduced-motion.

   PUBLIC API:
     MrbHeroes.stateToggleLab.init(container, config)

   CONFIG SCHEMA:
   {
     emoji, title, subtitle : string
     ions : { pos:{glyph}, neg:{glyph} }     // text inside + / − ions
     grid : { cols, rows }
     states : [ {
       key, label, inToggle?,                // inToggle:false = force-only state
       arrangement : 'lattice'|'jiggle'|'dissolved'|'sheared',
       verdict : { glow:bool, title, sub },  // bulb panel
       hint : string                         // dark mono bar text
     } ],
     force : null | { from, to, label, undoLabel }
   }
============================================================ */
(function () {
  'use strict';
  var NS = (window.MrbHeroes = window.MrbHeroes || {});
  if (NS.stateToggleLab) return;

  var STEP = 54, ION = 40;

  var STYLE_ID = 'mrb-hero-stl-styles';
  function ensureStyles() {
    if (document.getElementById(STYLE_ID)) return;
    var s = document.createElement('style');
    s.id = STYLE_ID;
    s.textContent = [
      '@keyframes mrbIonJiggle{0%,100%{transform:translate(0,0)}25%{transform:translate(3px,-2px)}50%{transform:translate(-2px,3px)}75%{transform:translate(2px,2px)}}',
      '@keyframes mrbBulbGlow{0%,100%{filter:drop-shadow(0 0 6px #F4B74088)}50%{filter:drop-shadow(0 0 16px #F4B740cc)}}',
      '.mrb-stl,.mrb-stl *{box-sizing:border-box}',
      '.mrb-stl{font-family:var(--font-body,system-ui,sans-serif);background:var(--surface-panel,#FFFDF8);border:1px solid var(--border,#E4DCCB);border-radius:var(--r-panel,22px);box-shadow:var(--shadow-panel,0 22px 50px -35px rgba(60,30,20,.5));overflow:hidden}',
      '.mrb-stl__head{display:flex;align-items:center;gap:10px;padding:16px 24px;border-bottom:1px solid var(--surface-inset,#EFE7D8);flex-wrap:wrap}',
      '.mrb-stl__head h3{font-family:var(--font-display,sans-serif);font-weight:700;font-size: calc(18px * var(--rd-fs-scale, 1));color:var(--ink,#1A1714);margin:0;min-width:0;overflow-wrap:anywhere}',
      '.mrb-stl__sub{font-family:var(--font-mono,monospace);font-size: calc(12px * var(--rd-fs-scale, 1));font-weight:700;color:var(--ink-muted,#6B635A)}',
      '.mrb-stl__grid{display:grid;grid-template-columns:1.5fr .9fr}',
      '.mrb-stl__viz{padding:16px 18px;background:linear-gradient(180deg,var(--surface-panel,#FFFDF8),#FBF4EF);overflow-x:auto;border-right:1px solid var(--surface-inset,#EFE7D8)}',
      '.mrb-stl__side{padding:20px 22px;display:flex;flex-direction:column;gap:10px}',
      '.mrb-stl__lbl{font-family:var(--font-mono,monospace);font-size: calc(11px * var(--rd-fs-scale, 1));font-weight:700;letter-spacing:.1em;color:var(--ink-muted,#6B635A)}',
      '.mrb-stl__btn{font-family:var(--font-display,sans-serif);font-weight:700;font-size: calc(14px * var(--rd-fs-scale, 1));text-align:left;cursor:pointer;border-radius:10px;padding:11px 14px;transition:all .15s;color:#4A4238;background:var(--surface-inset,#EFE7D8);border:1px solid var(--border,#E4DCCB)}',
      '.mrb-stl__btn.is-active{color:#fff;background:var(--surface-dark,#1A1714);border-color:var(--surface-dark,#1A1714)}',
      '.mrb-stl__rule{height:1px;background:var(--surface-inset,#EFE7D8);margin:6px 0}',
      '.mrb-stl__verdict{display:flex;align-items:center;gap:12px;background:var(--surface-inset,#F7F2E8);border-radius:12px;padding:12px 14px}',
      '.mrb-stl__bulb{font-size: calc(30px * var(--rd-fs-scale, 1));line-height:1}',
      '.mrb-stl__vt{font-family:var(--font-display,sans-serif);font-weight:700;font-size: calc(15px * var(--rd-fs-scale, 1))}',
      '.mrb-stl__vs{font-size: calc(12.5px * var(--rd-fs-scale, 1));color:var(--ink-muted,#6B635A);line-height:1.35}',
      '.mrb-stl__force{font-family:var(--font-display,sans-serif);font-weight:700;font-size: calc(14px * var(--rd-fs-scale, 1));text-align:center;cursor:pointer;border-radius:10px;padding:11px 14px;color:#fff;background:var(--accent-deep,#B5341A);border:none;box-shadow:0 8px 20px -8px rgba(181,52,26,.6)}',
      '.mrb-stl__force.is-pressed{color:var(--accent-deep,#B5341A);background:#FBE0D6;border:1px solid #F0BBA9;box-shadow:none}',
      '.mrb-stl__force:disabled{color:#B0A695;background:var(--surface-inset,#EFE7D8);border:1px solid var(--border,#E4DCCB);box-shadow:none;cursor:not-allowed}',
      '.mrb-stl__strap{padding:13px 24px;background:var(--surface-dark,#1A1714);font-family:var(--font-mono,monospace);font-size: calc(12.5px * var(--rd-fs-scale, 1));line-height:1.5;color:#EAE3D6}',
      /* Fix 2 (MRB-134) — consistent secondary Reset, above the dark strap. */
      '.mrb-stl__footer{display:flex;justify-content:flex-end;padding:10px 24px 12px;border-top:1px solid var(--surface-inset,#EFE7D8)}',
      '.mrb-stl__reset{font-family:var(--font-mono,monospace);font-size: calc(12px * var(--rd-fs-scale, 1));font-weight:600;letter-spacing:.04em;color:var(--ink-muted,#6B635A);background:transparent;border:1px solid var(--border,#E4DCCB);border-radius:8px;padding:8px 14px;cursor:pointer;transition:border-color .15s,color .15s}',
      '.mrb-stl__reset:hover{border-color:var(--accent-strong,#C0392B);color:var(--accent-deep,#B5341A)}',
      '.mrb-stl__reset:focus-visible{outline:2px solid var(--accent-strong,#C0392B);outline-offset:2px}',
      '@media (max-width:640px){.mrb-stl__grid{grid-template-columns:1fr}.mrb-stl__viz{border-right:none;border-bottom:1px solid var(--surface-inset,#EFE7D8)}}',
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

  function reduceMotion() {
    return window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  }

  /* stable per-instance jitter (seeded LCG, matches the spec) */
  function makeJitter(n) {
    var jit = [], seed = 7;
    function rnd() { seed = (seed * 9301 + 49297) % 233280; return seed / 233280; }
    for (var i = 0; i < n; i++) jit.push({ dx: (rnd() - 0.5) * 16, dy: (rnd() - 0.5) * 16, dur: 1 + rnd() * 0.8, del: rnd() * -2 });
    return jit;
  }

  /* pure model: where each ion sits for a given arrangement */
  function latticeModel(config, arrangement, jit) {
    var S = STEP, C = config.grid.cols, R = config.grid.rows, padL = 30, padT = 22;
    var spread = arrangement === 'dissolved' ? 1.18 : 1;
    var ions = [];
    for (var r = 0; r < R; r++) for (var cc = 0; cc < C; cc++) {
      var i = r * C + cc, x = padL + cc * S * spread, y = padT + r * S * spread, anim = false, j = jit[i];
      if (arrangement === 'jiggle' || arrangement === 'dissolved') { x += j.dx; y += j.dy; anim = true; }
      if (arrangement === 'sheared' && r >= Math.floor(R * 0.6)) { x += S; y += 14; }
      ions.push({ i: i, pos: (r + cc) % 2 === 0, x: x, y: y, anim: anim, j: j });
    }
    var W = padL * 2 + (C - 1) * S * 1.18 + ION;
    var H = padT * 2 + (R - 1) * S * 1.18 + ION + (arrangement === 'sheared' ? 14 : 0);
    return { ions: ions, W: W, H: H, shearY: padT + Math.floor(R * 0.6) * S - 8 };
  }

  function buildViz(config, stateDef, jit) {
    var m = latticeModel(config, stateDef.arrangement, jit);
    var noMotion = reduceMotion();
    var small = config.ions.pos.glyph.length > 1 || config.ions.neg.glyph.length > 1;
    var kids = m.ions.map(function (io) {
      var st = {
        position: 'absolute', left: io.x + 'px', top: io.y + 'px', width: ION + 'px', height: ION + 'px',
        borderRadius: '50%', display: 'flex', alignItems: 'center', justifyContent: 'center',
        fontFamily: 'var(--font-display,sans-serif)', fontWeight: '700', fontSize: small ? 'calc(12px * var(--rd-fs-scale, 1))' : 'calc(17px * var(--rd-fs-scale, 1))',
        color: '#fff', background: io.pos ? 'radial-gradient(circle at 35% 30%,#E0745F,#C0392B)' : 'radial-gradient(circle at 35% 30%,#6B96C9,#2E7DD1)',
        boxShadow: '0 4px 10px -3px rgba(0,0,0,.35)', transition: 'all .6s cubic-bezier(.4,0,.2,1)',
      };
      if (io.anim && !noMotion) st.animation = 'mrbIonJiggle ' + io.j.dur + 's ease-in-out ' + io.j.del + 's infinite';
      return el('div', { style: st }, io.pos ? config.ions.pos.glyph : config.ions.neg.glyph);
    });
    if (stateDef.arrangement === 'dissolved') {
      [[70, 40], [200, 30], [340, 60], [120, 150], [280, 190], [400, 120], [40, 210], [360, 220]].forEach(function (w, k) {
        var st = { position: 'absolute', left: w[0] + 'px', top: w[1] + 'px', width: '15px', height: '15px', borderRadius: '50%',
          background: 'rgba(120,170,220,.5)', border: '1px solid rgba(90,140,200,.6)' };
        if (!noMotion) st.animation = 'mrbIonJiggle ' + (1.2 + k * 0.1) + 's ease-in-out infinite';
        kids.push(el('div', { style: st }));
      });
    }
    if (stateDef.arrangement === 'sheared') {
      kids.push(el('div', { style: { position: 'absolute', left: '0', top: m.shearY + 'px', width: m.W + 'px', height: '3px',
        background: 'repeating-linear-gradient(90deg,#B5341A 0 10px,transparent 10px 18px)', opacity: '.8' } }));
      kids.push(el('div', { style: { position: 'absolute', left: (m.W / 2 - 40) + 'px', top: (m.shearY - 24) + 'px',
        fontFamily: 'var(--font-display,sans-serif)', fontWeight: '700', fontSize: 'calc(13px * var(--rd-fs-scale, 1))', color: '#B5341A',
        background: '#FBE0D6', padding: '3px 10px', borderRadius: '999px', border: '1px solid #F0BBA9' } }, '⚡ repel!'));
    }
    return el('div', { style: { position: 'relative', width: m.W + 'px', height: m.H + 'px', margin: '0 auto' } }, kids);
  }

  function init(container, config) {
    if (!container || !config) return;
    ensureStyles();
    var jit = makeJitter(config.grid.cols * config.grid.rows);
    var modeKey = config.states[0].key;
    // Phase 1a (MRB-133): optional predict-before-reveal gate (Law 4)
    var gate = (config.predict && window.MrbPredictWrapper)
      ? MrbPredictWrapper.create(config.predict) : null;

    var root = el('div', { className: 'mrb-stl' });
    root.appendChild(el('div', { className: 'mrb-stl__head' }, [
      el('span', { style: { fontSize: 'calc(20px * var(--rd-fs-scale, 1))' } }, config.emoji || '🔬'),
      el('h3', null, config.title || ''),
      config.subtitle ? el('span', { className: 'mrb-stl__sub' }, '— ' + config.subtitle) : null,
    ]));

    var vizWrap = el('div', { className: 'mrb-stl__viz' });
    var side = el('div', { className: 'mrb-stl__side' });
    side.appendChild(el('div', { className: 'mrb-stl__lbl' }, 'STATE'));

    var btnEls = config.states.filter(function (s) { return s.inToggle !== false; }).map(function (s) {
      var b = el('button', { className: 'mrb-stl__btn', attrs: { type: 'button' },
        on: { click: function () {
          var key = 'state:' + s.key;
          if (gate && !gate.allow(key)) return;
          modeKey = s.key; render();
          if (gate) gate.resolveIf(key);
        } } }, s.label);
      b._key = s.key; side.appendChild(b); return b;
    });
    side.appendChild(el('div', { className: 'mrb-stl__rule' }));

    var bulb = el('span', { className: 'mrb-stl__bulb' }, '💡');
    var vt = el('div', { className: 'mrb-stl__vt' });
    var vs = el('div', { className: 'mrb-stl__vs' });
    var verdict = el('div', { className: 'mrb-stl__verdict' }, [bulb, el('div', null, [vt, vs])]);
    side.appendChild(verdict);

    var forceBtn = null;
    if (config.force) {
      forceBtn = el('button', { className: 'mrb-stl__force', attrs: { type: 'button' }, on: { click: function () {
        if (modeKey === config.force.to) { modeKey = config.force.from; render(); return; }
        if (modeKey === config.force.from) {
          if (gate && !gate.allow('force')) return;
          modeKey = config.force.to;
          render();
          if (gate) gate.resolveIf('force');
        }
      } } });
      side.appendChild(forceBtn);
    }

    var grid = el('div', { className: 'mrb-stl__grid' }, [vizWrap, side]);
    var strap = el('div', { className: 'mrb-stl__strap' });
    // Fix 2 (MRB-134): consistent secondary reset — first state, wager re-armed.
    var resetBtn = el('button', { className: 'mrb-stl__reset', attrs: { type: 'button', 'aria-label': 'Reset the lab to its first state' },
      on: { click: function () { modeKey = config.states[0].key; if (gate) gate.reset(); render(); } } }, '↺ Reset');
    var footer = el('div', { className: 'mrb-stl__footer' }, resetBtn);
    if (gate) root.appendChild(gate.el);   // Phase 1a: wager row above the lab
    root.appendChild(grid);
    root.appendChild(footer);
    root.appendChild(strap);
    container.appendChild(root);

    function render() {
      var stateDef = null, i;
      for (i = 0; i < config.states.length; i++) if (config.states[i].key === modeKey) stateDef = config.states[i];
      if (!stateDef) stateDef = config.states[0];
      vizWrap.innerHTML = '';
      vizWrap.appendChild(buildViz(config, stateDef, jit));
      // Phase 0c (MRB-132): name the lattice diagram per state for screen readers.
      vizWrap.setAttribute('role', 'img');
      vizWrap.setAttribute('aria-label', 'Diagram: ' + (stateDef.label || stateDef.key) + '. '
        + (stateDef.verdict ? stateDef.verdict.title + ' — ' + stateDef.verdict.sub : ''));
      btnEls.forEach(function (b) {
        var on = b._key === modeKey || (config.force && modeKey === config.force.to && b._key === config.force.from);
        b.classList.toggle('is-active', on);
      });
      var glow = stateDef.verdict.glow;
      bulb.style.animation = (glow && !reduceMotion()) ? 'mrbBulbGlow 1.6s ease-in-out infinite' : 'none';
      vt.style.color = glow ? '#3E6B47' : '#B5341A';
      vt.textContent = stateDef.verdict.title;
      vs.textContent = stateDef.verdict.sub;
      if (forceBtn) {
        var sheared = modeKey === config.force.to;
        var canForce = sheared || modeKey === config.force.from;
        forceBtn.textContent = sheared ? config.force.undoLabel : config.force.label;
        forceBtn.classList.toggle('is-pressed', sheared);
        forceBtn.disabled = !canForce;
      }
      strap.textContent = stateDef.hint || '';
    }
    render();
    return { render: render };
  }

  NS.stateToggleLab = { init: init };
})();
