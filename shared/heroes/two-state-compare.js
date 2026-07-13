/* ============================================================
   MrBadmus Hero — TWO-STATE COMPARE  (vanilla port)
   Archetype 03 / 10. An A/B flip between two states of the same
   structure. Each state carries its own structural diagram + a
   plainly-stated property consequence with the reason.

   Ported from Design's `.dc.html` specs (Hero 03 Two-State Compare
   and Hero 10 Diamond vs Graphite). No React, no build step.

   LOCKED CALLOUT RULE (Mide, explicit): the key explanatory
   caption for each state sits on a SOFT TINT OF THAT STATE'S OWN
   ACCENT COLOUR — never plain cream, never buried in the dark
   footer strap. Each state's `tone` picks the tint.

   PUBLIC API:
     MrbHeroes.twoStateCompare.init(container, config)

   CONFIG SCHEMA:
   {
     emoji, title, subtitle : string        // hero header row
     strap                  : string        // constant dark-bar framing line
     states: [ exactly 2 × {
       key        : string,
       label      : string,                 // toggle button label
       emoji      : string,                 // icon shown in the callout
       tone       : 'neutral'|'good'|'bad'|'accent'|'blue',  // callout tint
       effectTitle: string,                 // bold consequence headline (callout)
       caption    : string,                 // the reason / explanation (callout)
       legend     : string,                 // mono one-liner under the diagram
       props      : [ { k, v, tone } ],     // property chips (tone colours value)
       visual     : { type, ...params }     // named renderer + params
     } ]
   }
   Renderers are pure functions of their params — add types to the
   RENDERERS registry without touching the state machine.
============================================================ */
(function () {
  'use strict';
  var NS = (window.MrbHeroes = window.MrbHeroes || {});
  if (NS.twoStateCompare) return;

  /* ---- callout / chip tone → Locked Tokens ----
     Each tone is a soft tint of that state's accent (callout rule). */
  var TONE = {
    neutral: { color: 'var(--ink)',          bg: 'var(--surface-inset)',   spine: 'var(--ink-faint)',      dot: '#B0A695', chip: '#4A4238' },
    good:    { color: 'var(--context-sage)', bg: 'var(--ok-bg)',           spine: 'var(--context-sage)',   dot: 'var(--context-sage)', chip: 'var(--context-sage)' },
    bad:     { color: 'var(--accent-deep)',  bg: 'var(--err-bg)',          spine: 'var(--accent-deep)',    dot: 'var(--accent-deep)',  chip: 'var(--accent-deep)' },
    accent:  { color: 'var(--accent-deep)',  bg: 'var(--accent-wash)',     spine: 'var(--accent-strong)',  dot: 'var(--accent-strong)', chip: 'var(--accent-deep)' },
    blue:    { color: 'var(--context-blue)', bg: '#E8F1FB',                spine: 'var(--context-blue)',   dot: 'var(--context-blue)', chip: 'var(--context-blue)' },
  };

  var STYLE_ID = 'mrb-hero-tsc-styles';
  function ensureStyles() {
    if (document.getElementById(STYLE_ID)) return;
    var s = document.createElement('style');
    s.id = STYLE_ID;
    s.textContent = [
      '@keyframes mrbEDrift{0%,100%{transform:translate(0,0)}25%{transform:translate(22px,4px)}50%{transform:translate(44px,-3px)}75%{transform:translate(18px,6px)}}',
      '.mrb-tsc,.mrb-tsc *{box-sizing:border-box}',
      '.mrb-tsc{font-family:var(--font-body,system-ui,sans-serif);background:var(--surface-panel,#FFFDF8);border:1px solid var(--border,#E4DCCB);border-radius:var(--r-panel,22px);box-shadow:var(--shadow-panel,0 22px 50px -35px rgba(60,30,20,.5));overflow:hidden}',
      '.mrb-tsc__head{display:flex;align-items:center;gap:10px;padding:16px 24px;border-bottom:1px solid var(--surface-inset,#EFE7D8);flex-wrap:wrap}',
      '.mrb-tsc__head h3{font-family:var(--font-display,sans-serif);font-weight:700;font-size: calc(18px * var(--rd-fs-scale, 1));color:var(--ink,#1A1714);margin:0}',
      '.mrb-tsc__sub{font-family:var(--font-mono,monospace);font-size: calc(12px * var(--rd-fs-scale, 1));color:var(--ink-faint,#8A8074)}',
      '.mrb-tsc__callout{display:flex;gap:14px;align-items:flex-start;padding:18px 24px;border-bottom:1px solid var(--surface-inset,#EFE7D8);border-left:5px solid transparent;transition:background .25s ease,border-color .25s ease}',
      '.mrb-tsc__callout-emoji{font-size: calc(22px * var(--rd-fs-scale, 1));line-height:1.2;flex:none}',
      '.mrb-tsc__effect{font-family:var(--font-display,sans-serif);font-weight:700;font-size: calc(17px * var(--rd-fs-scale, 1));line-height:1.25;margin-bottom:4px}',
      '.mrb-tsc__caption{font-size: calc(14px * var(--rd-fs-scale, 1));line-height:1.6;color:var(--ink-body,#3A322A)}',
      '.mrb-tsc__grid{display:grid;grid-template-columns:1.5fr .9fr}',
      '.mrb-tsc__viz{padding:20px 18px;background:linear-gradient(180deg,var(--surface-panel,#FFFDF8),#FBF4EF);border-right:1px solid var(--surface-inset,#EFE7D8);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:14px;overflow-x:auto}',
      '.mrb-tsc__legend{font-family:var(--font-mono,monospace);font-size: calc(11.5px * var(--rd-fs-scale, 1));letter-spacing:.03em;color:var(--ink-faint,#8A8074);text-align:center;max-width:36ch;line-height:1.5}',
      '.mrb-tsc__side{padding:20px 22px;display:flex;flex-direction:column;gap:10px}',
      '.mrb-tsc__lbl{font-family:var(--font-mono,monospace);font-size: calc(11px * var(--rd-fs-scale, 1));font-weight:600;letter-spacing:.1em;color:#9A9082}',
      '.mrb-tsc__btn{font-family:var(--font-display,sans-serif);font-weight:700;font-size: calc(14px * var(--rd-fs-scale, 1));text-align:left;cursor:pointer;border-radius:10px;padding:11px 14px;transition:all .15s;color:#4A4238;background:var(--surface-inset,#EFE7D8);border:1px solid var(--border,#E4DCCB)}',
      '.mrb-tsc__btn:hover{border-color:var(--accent-strong,#C0392B)}',
      '.mrb-tsc__btn.is-active{color:#fff;background:var(--surface-dark,#1A1714);border-color:var(--surface-dark,#1A1714)}',
      '.mrb-tsc__rule{height:1px;background:var(--surface-inset,#EFE7D8);margin:6px 0}',
      '.mrb-tsc__prop{display:flex;align-items:center;justify-content:space-between;gap:10px;padding:9px 12px;background:var(--surface-inset,#F7F2E8);border-radius:10px}',
      '.mrb-tsc__prop-k{font-family:var(--font-mono,monospace);font-size: calc(11.5px * var(--rd-fs-scale, 1));letter-spacing:.02em;color:var(--ink-faint,#8A8074)}',
      '.mrb-tsc__prop-v{display:flex;align-items:center;gap:7px;font-family:var(--font-display,sans-serif);font-weight:700;font-size: calc(13.5px * var(--rd-fs-scale, 1))}',
      '.mrb-tsc__dot{width:8px;height:8px;border-radius:50%;flex:none}',
      '.mrb-tsc__strap{padding:13px 24px;background:var(--surface-dark,#1A1714);font-family:var(--font-mono,monospace);font-size: calc(12.5px * var(--rd-fs-scale, 1));color:#EAE3D6}',
      '@media (max-width:640px){.mrb-tsc__grid{grid-template-columns:1fr}.mrb-tsc__viz{border-right:none;border-bottom:1px solid var(--surface-inset,#EFE7D8)}}',
    ].join('');
    document.head.appendChild(s);
  }

  /* ---- tiny DOM helper ---- */
  function el(tag, style, kids) {
    var n = document.createElement(tag);
    if (style) for (var k in style) n.style[k] = style[k];
    if (kids != null) {
      if (!Array.isArray(kids)) kids = [kids];
      kids.forEach(function (c) {
        if (c == null) return;
        n.appendChild(typeof c === 'string' ? document.createTextNode(c) : c);
      });
    }
    return n;
  }

  /* ============ structural diagram primitives ============ */
  function atom(x, y, size, opacity) {
    return el('div', {
      position: 'absolute', left: (x - size / 2) + 'px', top: (y - size / 2) + 'px',
      width: size + 'px', height: size + 'px', borderRadius: '50%',
      background: 'radial-gradient(circle at 34% 28%, #5A5148, #241F1A)',
      boxShadow: '0 3px 7px -2px rgba(0,0,0,.4), inset 0 0 0 1px rgba(255,255,255,.06)',
      opacity: opacity == null ? 1 : opacity,
    });
  }
  function bond(a, b, color, thick, opacity) {
    var dx = b[0] - a[0], dy = b[1] - a[1];
    var len = Math.hypot(dx, dy), ang = Math.atan2(dy, dx) * 180 / Math.PI;
    return el('div', {
      position: 'absolute', left: a[0] + 'px', top: (a[1] - thick / 2) + 'px',
      width: len + 'px', height: thick + 'px', background: color, opacity: opacity == null ? 1 : opacity,
      transformOrigin: '0 50%', transform: 'rotate(' + ang + 'deg)', borderRadius: '2px',
    });
  }

  /* ---- DIAMOND: rigid 3-D tetrahedral network, 4 bonds / C ---- */
  function drawTetrahedral() {
    var pad = 30, S = 52, rowH = 44, cols = 4, rows = 4;
    var pts = [];
    for (var r = 0; r < rows; r++) for (var c = 0; c < cols; c++) {
      pts.push([pad + c * S + (r % 2) * (S / 2), pad + r * rowH]);
    }
    var back = pts.map(function (p) { return [p[0] + 20, p[1] - 24]; });
    var kids = [], i, j, d;
    for (i = 0; i < pts.length; i++) for (j = i + 1; j < pts.length; j++) {
      d = Math.hypot(back[i][0] - back[j][0], back[i][1] - back[j][1]);
      if (d < S * 0.95) kids.push(bond(back[i], back[j], '#C9BBA6', 5, 0.5));
    }
    back.forEach(function (p) { kids.push(atom(p[0], p[1], 16, 0.5)); });
    for (i = 0; i < pts.length; i++) kids.push(bond(pts[i], back[i], '#B7A88F', 4, 0.45));
    for (i = 0; i < pts.length; i++) for (j = i + 1; j < pts.length; j++) {
      d = Math.hypot(pts[i][0] - pts[j][0], pts[i][1] - pts[j][1]);
      if (d < S * 0.95) kids.push(bond(pts[i], pts[j], '#8A7A66', 6));
    }
    pts.forEach(function (p) { kids.push(atom(p[0], p[1], 22)); });
    var W = pad * 2 + (cols - 1) * S + S / 2 + 26, H = pad * 2 + (rows - 1) * rowH + 8;
    return el('div', { position: 'relative', width: W + 'px', height: H + 'px' }, kids);
  }

  /* ---- honeycomb vertex/bond set for a flat graphite sheet ---- */
  function honeycomb(R) {
    var cols = 3, rows = 2, hexW = 1.5 * R, hexH = Math.sqrt(3) * R;
    var A = {}, B = {};
    var key = function (x, y) { return Math.round(x) + ',' + Math.round(y); };
    for (var cc = 0; cc < cols; cc++) for (var rr = 0; rr < rows; rr++) {
      var cx = cc * hexW, cy = rr * hexH + (cc % 2 ? hexH / 2 : 0), v = [];
      for (var a = 0; a < 6; a++) { var t = Math.PI / 180 * (60 * a); v.push([cx + R * Math.cos(t), cy + R * Math.sin(t)]); }
      for (a = 0; a < 6; a++) {
        A[key(v[a][0], v[a][1])] = v[a];
        var b = v[(a + 1) % 6], kk = [key(v[a][0], v[a][1]), key(b[0], b[1])].sort().join('|');
        B[kk] = [v[a], b];
      }
    }
    var minX = 1e9, minY = 1e9, p;
    for (var ka in A) { p = A[ka]; minX = Math.min(minX, p[0]); minY = Math.min(minY, p[1]); }
    var atoms = Object.keys(A).map(function (k2) { return [A[k2][0] - minX, A[k2][1] - minY]; });
    var bonds = Object.keys(B).map(function (k2) { var s = B[k2]; return [[s[0][0] - minX, s[0][1] - minY], [s[1][0] - minX, s[1][1] - minY]]; });
    var maxX = 0, maxY = 0;
    atoms.forEach(function (q) { maxX = Math.max(maxX, q[0]); maxY = Math.max(maxY, q[1]); });
    return { atoms: atoms, bonds: bonds, w: maxX, h: maxY };
  }

  /* ---- GRAPHITE: stacked hexagonal layers ± delocalised electrons ---- */
  function drawHexLayers(v) {
    var R = 24, hc = honeycomb(R);
    var layers = 3, dx = 30, dy = 34, pad = 20;
    var kids = [];
    var layerH = function (li) { return layers - 1 - li; };
    var ox = function (li) { return pad + layerH(li) * dx; };
    var oy = function (li) { return pad + (layers - 1) * dy - layerH(li) * dy + (v.slide ? layerH(li) * 12 : 0); };
    for (var li = layers - 1; li >= 0; li--) {
      var front = li === 0, op = front ? 1 : 0.42;
      var bx = ox(li), by = oy(li);
      hc.bonds.forEach(function (s) { kids.push(bond([s[0][0] + bx, s[0][1] + by], [s[1][0] + bx, s[1][1] + by], '#8A7A66', front ? 5 : 4, op)); });
      hc.atoms.forEach(function (p) { kids.push(atom(p[0] + bx, p[1] + by, front ? 18 : 14, op)); });
    }
    var gaps = layers - 1;
    for (var g = 0; g < gaps; g++) {
      var gli = g;
      var gx = ox(gli) + (ox(gli + 1) - ox(gli)) / 2;
      var gy = oy(gli) + (oy(gli + 1) - oy(gli)) / 2 + 6;
      for (var e = 0; e < 4; e++) {
        var ex = gx + e * 34 + 4, ey = gy + (e % 2) * 12;
        var st = {
          position: 'absolute', left: ex + 'px', top: ey + 'px', width: '12px', height: '12px', borderRadius: '50%',
          background: 'var(--context-blue,#2E7DD1)', boxShadow: '0 0 7px rgba(46,125,209,.67)', transition: 'all .7s cubic-bezier(.4,0,.2,1)',
        };
        if (v.delocalised) { st.animation = 'mrbEDrift ' + (2.2 + (e % 3) * 0.5) + 's ease-in-out ' + (e * -0.4) + 's infinite'; }
        else { st.background = '#9AA6B2'; st.boxShadow = 'none'; }
        kids.push(el('div', st));
      }
    }
    var W = pad * 2 + hc.w + (layers - 1) * dx + 24;
    var H = pad * 2 + hc.h + (layers - 1) * dy + (v.slide ? (layers - 1) * 12 : 0) + 8;
    return el('div', { position: 'relative', width: W + 'px', height: H + 'px' }, kids);
  }

  var RENDERERS = { tetrahedral: drawTetrahedral, hexLayers: drawHexLayers };
  function buildViz(visual) { return (RENDERERS[visual.type] || drawTetrahedral)(visual); }

  /* ============ instance ============ */
  function init(container, config) {
    if (!container) return;
    ensureStyles();
    var sel = 0;

    var root = el('div', null); root.className = 'mrb-tsc';

    // header
    var head = el('div', null, [
      el('span', { fontSize: 'calc(20px * var(--rd-fs-scale, 1))' }, config.emoji || ''),
      (function () { var h = el('h3', null, config.title || ''); return h; })(),
      el('span', null, '— ' + (config.subtitle || '')),
    ]);
    head.className = 'mrb-tsc__head';
    head.childNodes[2].className = 'mrb-tsc__sub';

    // callout (tinted by current state's tone — the locked callout rule)
    var callout = el('div', null); callout.className = 'mrb-tsc__callout';
    var calloutEmoji = el('span', null, ''); calloutEmoji.className = 'mrb-tsc__callout-emoji';
    var effect = el('div', null, ''); effect.className = 'mrb-tsc__effect';
    var caption = el('div', null, ''); caption.className = 'mrb-tsc__caption';
    callout.appendChild(calloutEmoji);
    callout.appendChild(el('div', null, [effect, caption]));

    // grid: viz + legend | controls
    var vizWrap = el('div', null); vizWrap.className = 'mrb-tsc__viz';
    var vizSlot = el('div', null); var legend = el('div', null, ''); legend.className = 'mrb-tsc__legend';
    vizWrap.appendChild(vizSlot); vizWrap.appendChild(legend);

    var side = el('div', null); side.className = 'mrb-tsc__side';
    var cmpLbl = el('div', null, 'COMPARE'); cmpLbl.className = 'mrb-tsc__lbl';
    side.appendChild(cmpLbl);
    var btns = config.states.map(function (s, i) {
      var b = el('button', null, s.label); b.className = 'mrb-tsc__btn';
      b.type = 'button';
      b.addEventListener('click', function () { sel = i; render(); });
      side.appendChild(b);
      return b;
    });
    side.appendChild((function () { var r = el('div', null); r.className = 'mrb-tsc__rule'; return r; })());
    var propLbl = el('div', null, 'PROPERTIES'); propLbl.className = 'mrb-tsc__lbl';
    side.appendChild(propLbl);
    var propSlot = el('div', null, ''); side.style.gap = '10px';
    side.appendChild(propSlot);

    var grid = el('div', null, [vizWrap, side]); grid.className = 'mrb-tsc__grid';

    var strap = el('div', null, config.strap || ''); strap.className = 'mrb-tsc__strap';

    root.appendChild(head);
    root.appendChild(callout);
    root.appendChild(grid);
    root.appendChild(strap);
    container.appendChild(root);

    function render() {
      var stt = config.states[sel];
      var tone = TONE[stt.tone] || TONE.neutral;
      // callout tint
      callout.style.background = tone.bg;
      callout.style.borderLeftColor = tone.spine;
      calloutEmoji.textContent = stt.emoji || '';
      effect.style.color = tone.color;
      effect.textContent = stt.effectTitle || '';
      caption.textContent = stt.caption || '';
      // viz + legend
      vizSlot.innerHTML = '';
      vizSlot.appendChild(buildViz(stt.visual));
      legend.textContent = stt.legend || '';
      // buttons
      btns.forEach(function (b, i) { b.classList.toggle('is-active', i === sel); });
      // property chips
      propSlot.innerHTML = '';
      (stt.props || []).forEach(function (p) {
        var t = TONE[p.tone] || TONE.neutral;
        var dot = el('span', { background: t.dot }); dot.className = 'mrb-tsc__dot';
        var val = el('span', { color: t.chip }, [dot, document.createTextNode(p.v)]);
        val.className = 'mrb-tsc__prop-v';
        var k = el('span', null, p.k); k.className = 'mrb-tsc__prop-k';
        var row = el('div', null, [k, val]); row.className = 'mrb-tsc__prop';
        propSlot.appendChild(row);
      });
    }
    render();
    return { render: render };
  }

  NS.twoStateCompare = { init: init, RENDERERS: RENDERERS };
})();
