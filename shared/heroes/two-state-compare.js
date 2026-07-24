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
      '.mrb-tsc__head h3{font-family:var(--font-display,sans-serif);font-weight:700;font-size: calc(18px * var(--rd-fs-scale, 1));color:var(--ink,#1A1714);margin:0;min-width:0;overflow-wrap:anywhere}',
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
      '.mrb-tsc__force{font-family:var(--font-display,sans-serif);font-weight:700;font-size: calc(14px * var(--rd-fs-scale, 1));text-align:center;cursor:pointer;border-radius:10px;padding:11px 14px;margin-top:2px;color:#fff;background:var(--accent-deep,#B5341A);border:none;box-shadow:0 8px 20px -8px rgba(181,52,26,.7)}',
      '.mrb-tsc__force.is-pressed{color:var(--accent-deep,#B5341A);background:#FBE0D6;border:1px solid #F0BBA9;box-shadow:none}',
      '.mrb-tsc__rule{height:1px;background:var(--surface-inset,#EFE7D8);margin:6px 0}',
      '.mrb-tsc__prop{display:flex;align-items:center;justify-content:space-between;gap:10px;padding:9px 12px;background:var(--surface-inset,#F7F2E8);border-radius:10px}',
      '.mrb-tsc__prop-k{font-family:var(--font-mono,monospace);font-size: calc(11.5px * var(--rd-fs-scale, 1));letter-spacing:.02em;color:var(--ink-faint,#8A8074)}',
      '.mrb-tsc__prop-v{display:flex;align-items:center;gap:7px;font-family:var(--font-display,sans-serif);font-weight:700;font-size: calc(13.5px * var(--rd-fs-scale, 1))}',
      '.mrb-tsc__dot{width:8px;height:8px;border-radius:50%;flex:none}',
      '.mrb-tsc__strap{padding:13px 24px;background:var(--surface-dark,#1A1714);font-family:var(--font-mono,monospace);font-size: calc(12.5px * var(--rd-fs-scale, 1));color:#EAE3D6}',
      /* Fix 6 (MRB-134) — persistent VIEWING:<state> indicator in the head. */
      '.mrb-tsc__viewing{margin-left:auto;font-family:var(--font-mono,monospace);font-size: calc(11px * var(--rd-fs-scale, 1));font-weight:700;letter-spacing:.07em;text-transform:uppercase;color:var(--accent-deep,#B5341A);background:var(--surface-inset,#EFE7D8);border:1px solid var(--border,#E4DCCB);border-radius:999px;padding:5px 12px;white-space:nowrap;transition:color .2s ease,background .2s ease}',
      /* Fix 2 (MRB-134) — consistent secondary Reset, above the dark strap. */
      '.mrb-tsc__footer{display:flex;justify-content:flex-end;padding:10px 24px 12px;border-top:1px solid var(--surface-inset,#EFE7D8)}',
      '.mrb-tsc__reset{font-family:var(--font-mono,monospace);font-size: calc(12px * var(--rd-fs-scale, 1));font-weight:600;letter-spacing:.04em;color:var(--ink-muted,#6B635A);background:transparent;border:1px solid var(--border,#E4DCCB);border-radius:8px;padding:8px 14px;cursor:pointer;transition:border-color .15s,color .15s}',
      '.mrb-tsc__reset:hover{border-color:var(--accent-strong,#C0392B);color:var(--accent-deep,#B5341A)}',
      '.mrb-tsc__reset:focus-visible{outline:2px solid var(--accent-strong,#C0392B);outline-offset:2px}',
      '@media (prefers-reduced-motion: reduce){.mrb-tsc__viewing{transition:none}}',
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
        /* Phase 0c (MRB-132): mrbEDrift was the one looping animation with no
           reduced-motion gate (council §8 item 8). Static electrons are the
           fallback — position and glow still read as delocalised. */
        if (v.delocalised && !reduceMotion()) { st.animation = 'mrbEDrift ' + (2.2 + (e % 3) * 0.5) + 's ease-in-out ' + (e * -0.4) + 's infinite'; }
        else if (!v.delocalised) { st.background = '#9AA6B2'; st.boxShadow = 'none'; }
        kids.push(el('div', st));
      }
    }
    var W = pad * 2 + hc.w + (layers - 1) * dx + 24;
    var H = pad * 2 + hc.h + (layers - 1) * dy + (v.slide ? (layers - 1) * 12 : 0) + 8;
    return el('div', { position: 'relative', width: W + 'px', height: H + 'px' }, kids);
  }

  /* ---- reduced-motion guard (looping animations only) ---- */
  function reduceMotion() {
    return window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  }

  /* ---- positive metal ion (reddish, optional '+' glyph) ---- */
  function ion(x, y, size, glyph, foreign) {
    var n = el('div', {
      position: 'absolute', left: (x - size / 2) + 'px', top: (y - size / 2) + 'px',
      width: size + 'px', height: size + 'px', borderRadius: '50%',
      display: 'flex', alignItems: 'center', justifyContent: 'center',
      fontFamily: 'var(--font-display,sans-serif)', fontWeight: '700',
      fontSize: 'calc(15px * var(--rd-fs-scale, 1))', color: '#fff',
      background: foreign
        ? 'radial-gradient(circle at 35% 30%,#8A6B4E,#5A4432)'
        : 'radial-gradient(circle at 35% 30%,#E0745F,#C0392B)',
      boxShadow: '0 4px 10px -3px rgba(0,0,0,.35)',
      transition: 'all .7s cubic-bezier(.4,0,.2,1)',
    }, glyph || '');
    return n;
  }

  /* ---- METAL LAYERS: rows of ions; pure metal shears under force
     (layers slide → bends), alloy's foreign atoms lock the layers ---- */
  function drawMetalLayers(v) {
    var COLS = 8, ROWS = 4, S = 44, ION = 34, padL = 26, padT = 40;
    var alloySpots = { 5: 1, 10: 1, 13: 1, 19: 1 };
    var slide = v.forced && !v.alloy;      // only the pure metal shears
    var shearMax = (ROWS - 1) * 22;
    var kids = [];
    for (var r = 0; r < ROWS; r++) for (var c = 0; c < COLS; c++) {
      var i = r * COLS + c;
      var foreign = v.alloy && alloySpots[i];
      var size = foreign ? 44 : ION;
      var shift = slide ? (ROWS - 1 - r) * 22 : 0;   // top rows travel furthest
      var x = padL + c * S + (ION - size) / 2 + shift + size / 2;
      var y = padT + r * S + (ION - size) / 2 + size / 2;
      kids.push(ion(x, y, size, '', foreign));
    }
    var W = padL * 2 + (COLS - 1) * S + ION + shearMax + 6;
    var H = padT + (ROWS - 1) * S + ION + 42;
    // applied-force arrow (faint until forced)
    var arrow = el('div', {
      position: 'absolute', left: padL + 'px', top: '8px', display: 'flex', alignItems: 'center', gap: '7px',
      fontFamily: 'var(--font-mono,monospace)', fontWeight: '700', fontSize: 'calc(12px * var(--rd-fs-scale, 1))',
      letterSpacing: '.06em', color: 'var(--accent-deep,#B5341A)', opacity: v.forced ? '1' : '0.3', transition: 'opacity .4s',
    }, [document.createTextNode('FORCE'),
        el('div', { width: '54px', height: '2px', background: 'var(--accent-deep,#B5341A)', position: 'relative' },
           el('div', { position: 'absolute', right: '-1px', top: '-3px', width: '0', height: '0',
             borderTop: '4px solid transparent', borderBottom: '4px solid transparent', borderLeft: '7px solid var(--accent-deep,#B5341A)' }))]);
    kids.push(arrow);
    if (v.forced) {
      var good = !v.alloy;
      kids.push(el('div', {
        position: 'absolute', left: padL + 'px', top: (H - 24) + 'px',
        fontFamily: 'var(--font-display,sans-serif)', fontWeight: '700', fontSize: 'calc(12.5px * var(--rd-fs-scale, 1))',
        color: good ? '#3E6B47' : '#B5341A', background: good ? '#E7F3EA' : '#FBE0D6',
        border: '1px solid ' + (good ? '#7FB98A' : '#F0BBA9'), padding: '3px 11px', borderRadius: '999px',
      }, good ? 'layers slide → bends' : 'layers locked → resists'));
    }
    return el('div', { position: 'relative', width: W + 'px', height: H + 'px' }, kids);
  }

  /* ---- ELECTRON SEA: lattice of + ions + one electron each; free →
     delocalised drift (conducts), pinned → stuck to atoms (no conduction) ---- */
  function drawElectronSea(v) {
    var COLS = 7, ROWS = 3, S = 56, ION = 38, padL = 24, padT = 26;
    var noMotion = reduceMotion();
    var kids = [];
    for (var r = 0; r < ROWS; r++) for (var c = 0; c < COLS; c++) {
      var i = r * COLS + c;
      kids.push(ion(padL + c * S + ION / 2, padT + r * S + ION / 2, ION, '+', false));
      var ex = padL + c * S + (v.free ? -8 : 30), ey = padT + r * S + (v.free ? 44 : 30);
      var st = {
        position: 'absolute', left: ex + 'px', top: ey + 'px', width: '11px', height: '11px', borderRadius: '50%',
        transition: 'all .8s cubic-bezier(.4,0,.2,1)',
      };
      if (v.free) {
        st.background = 'var(--context-blue,#2E7DD1)';
        st.boxShadow = '0 0 6px rgba(46,125,209,.6)';
        if (!noMotion) st.animation = 'mrbEDrift ' + (2 + (i % 5) * 0.4) + 's ease-in-out ' + (i * -0.3) + 's infinite';
      } else {
        st.background = '#9AA6B2'; st.boxShadow = 'none';
      }
      kids.push(el('div', st));
    }
    var W = padL * 2 + (COLS - 1) * S + ION + 20, H = padT * 2 + (ROWS - 1) * S + ION + 18;
    return el('div', { position: 'relative', width: W + 'px', height: H + 'px' }, kids);
  }

  var RENDERERS = {
    tetrahedral: drawTetrahedral, hexLayers: drawHexLayers,
    metalLayers: drawMetalLayers, electronSea: drawElectronSea, delocalised: drawElectronSea,
  };
  function buildViz(visual, forced) {
    var v = visual;
    if (forced != null) { v = {}; for (var k in visual) v[k] = visual[k]; v.forced = forced; }
    return (RENDERERS[v.type] || drawTetrahedral)(v);
  }

  /* ============ instance ============ */
  function init(container, config) {
    if (!container) return;
    ensureStyles();
    var sel = 0;
    var forced = false;   // optional "apply force" demo state (config.force)
    // Phase 1a (MRB-133): optional predict-before-reveal gate (Law 4)
    var gate = (config.predict && window.MrbPredictWrapper)
      ? MrbPredictWrapper.create(config.predict) : null;

    var root = el('div', null); root.className = 'mrb-tsc';

    // header
    var head = el('div', null, [
      el('span', { fontSize: 'calc(20px * var(--rd-fs-scale, 1))' }, config.emoji || ''),
      (function () { var h = el('h3', null, config.title || ''); return h; })(),
      el('span', null, '— ' + (config.subtitle || '')),
    ]);
    head.className = 'mrb-tsc__head';
    head.childNodes[2].className = 'mrb-tsc__sub';
    // Fix 6 (MRB-134): persistent VIEWING:<state> indicator, updated in render().
    var viewing = el('span', null, ''); viewing.className = 'mrb-tsc__viewing';
    viewing.setAttribute('aria-live', 'polite');
    head.appendChild(viewing);

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
      b.addEventListener('click', function () {
        var key = 'state:' + s.key;
        if (gate && !gate.allow(key)) return;
        sel = i; forced = false; render();
        if (gate) gate.resolveIf(key);
      });
      side.appendChild(b);
      return b;
    });
    side.appendChild((function () { var r = el('div', null); r.className = 'mrb-tsc__rule'; return r; })());
    var propLbl = el('div', null, 'PROPERTIES'); propLbl.className = 'mrb-tsc__lbl';
    side.appendChild(propLbl);
    var propSlot = el('div', null, ''); side.style.gap = '10px';
    side.appendChild(propSlot);

    // optional force button (only states carrying a `forced` override react)
    var forceBtn = null;
    if (config.force) {
      forceBtn = el('button', null, ''); forceBtn.className = 'mrb-tsc__force'; forceBtn.type = 'button';
      forceBtn.addEventListener('click', function () {
        if (gate && !forced && !gate.allow('force')) return;
        forced = !forced; render();
        if (gate && forced) gate.resolveIf('force');
      });
      side.appendChild(forceBtn);
    }

    var grid = el('div', null, [vizWrap, side]); grid.className = 'mrb-tsc__grid';

    var strap = el('div', null, config.strap || ''); strap.className = 'mrb-tsc__strap';

    // Fix 2 (MRB-134): consistent secondary reset — first state, force off, wager re-armed.
    var resetBtn = el('button', null, '↺ Reset'); resetBtn.className = 'mrb-tsc__reset'; resetBtn.type = 'button';
    resetBtn.setAttribute('aria-label', 'Reset the comparison to the first state');
    resetBtn.addEventListener('click', function () { sel = 0; forced = false; if (gate) gate.reset(); render(); });
    var footer = el('div', null, resetBtn); footer.className = 'mrb-tsc__footer';

    root.appendChild(head);
    if (gate) root.appendChild(gate.el);   // Phase 1a: wager row above the callout
    root.appendChild(callout);
    root.appendChild(grid);
    root.appendChild(footer);
    root.appendChild(strap);
    container.appendChild(root);

    function render() {
      var stt = config.states[sel];
      // when forced and this state carries a post-force override, swap to it
      var applyForce = forced && !!config.force;
      var view = (applyForce && stt.forced) ? stt.forced : stt;
      var tone = TONE[(view.tone != null ? view.tone : stt.tone)] || TONE.neutral;
      // Fix 6 (MRB-134): keep the VIEWING indicator in sync with the toggle.
      viewing.textContent = 'Viewing: ' + (stt.label || stt.key || '') + (applyForce ? ' · force applied' : '');
      // callout tint
      callout.style.background = tone.bg;
      callout.style.borderLeftColor = tone.spine;
      calloutEmoji.textContent = stt.emoji || '';
      effect.style.color = tone.color;
      effect.textContent = view.effectTitle || '';
      caption.textContent = view.caption || '';
      // viz + legend (pass the force flag to the renderer)
      vizSlot.innerHTML = '';
      vizSlot.appendChild(buildViz(stt.visual, config.force ? forced : null));
      legend.textContent = (view.legend != null ? view.legend : stt.legend) || '';
      // Phase 0c (MRB-132): the drawn structure is silent to screen readers —
      // name it per state so the diagram carries the same message as the visuals.
      vizSlot.setAttribute('role', 'img');
      vizSlot.setAttribute('aria-label', 'Diagram: ' + (stt.label || '') + '. '
        + (view.effectTitle || '') + '. '
        + ((view.legend != null ? view.legend : stt.legend) || ''));
      // buttons
      btns.forEach(function (b, i) { b.classList.toggle('is-active', i === sel); });
      // force button label + pressed style
      if (forceBtn) {
        forceBtn.textContent = forced ? config.force.undoLabel : config.force.label;
        forceBtn.classList.toggle('is-pressed', forced);
      }
      // property chips
      propSlot.innerHTML = '';
      ((view.props != null ? view.props : stt.props) || []).forEach(function (p) {
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
