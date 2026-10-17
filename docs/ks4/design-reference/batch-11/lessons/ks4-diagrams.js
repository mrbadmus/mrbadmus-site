/* KS4 diagram engine — a browser port of Mide's house library
   (05-diagram-library/chem_diagrams.py + physics_diagrams.py).
   Same locked style core: cream #F3F0E7 plate, dark-sage labels #2E5E45,
   near-black strokes #1A1A1A, teal process arrows #2E8B7F, Georgia.
   Every function returns a complete <svg> string. Plates stay cream in dark mode.
   Circuit symbols follow the AQA symbol sheet via physics_diagrams.py: the diode
   and LED sit in a circle; the variable resistor's arrow runs fully through the body;
   there is no motor symbol. Loops are laid out with no wire crossings. */
window.KS4D = (function () {
  var C = { cream: '#F3F0E7', label: '#2E5E45', stroke: '#1A1A1A', e: '#2E5E45', metal: '#F2C9AE', nm: '#A9D9BE',
    arrow: '#2E8B7F', muted: '#5B6B82', red: '#C8102E', gold: '#FBBF24', blue: '#3B82F6' };
  var F = 'Georgia, \'Times New Roman\', serif';
  function esc(t) { return String(t == null ? '' : t).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;'); }
  function svg(w, h, body, alt) {
    return '<svg viewBox="0 0 ' + w + ' ' + h + '" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="' + esc(alt) +
      '" style="display:block;width:100%;height:auto"><rect x="0" y="0" width="' + w + '" height="' + h + '" rx="18" fill="' + C.cream + '"/>' + body + '</svg>';
  }
  function T(x, y, t, size, o) {
    o = o || {};
    return '<text x="' + x.toFixed(1) + '" y="' + y.toFixed(1) + '" font-family="' + F + '" font-size="' + (size || 22) + '" fill="' + (o.fill || C.label) +
      '" text-anchor="' + (o.anchor || 'middle') + '" font-weight="' + (o.weight || 'bold') + '"' + (o.style ? ' font-style="' + o.style + '"' : '') + '>' + esc(t) + '</text>';
  }
  function line(x1, y1, x2, y2, w, col, extra) {
    return '<line x1="' + x1.toFixed(1) + '" y1="' + y1.toFixed(1) + '" x2="' + x2.toFixed(1) + '" y2="' + y2.toFixed(1) + '" stroke="' + (col || C.stroke) + '" stroke-width="' + (w || 3) + '" stroke-linecap="round"' + (extra || '') + '/>';
  }
  function circ(x, y, r, fill, stroke, w, extra) {
    return '<circle cx="' + x.toFixed(1) + '" cy="' + y.toFixed(1) + '" r="' + r + '" fill="' + (fill || 'none') + '" stroke="' + (stroke || 'none') + '" stroke-width="' + (w || 0) + '"' + (extra || '') + '/>';
  }
  function dot(x, y, r) { return circ(x, y, r || 5.5, C.e); }
  function cross(x, y, s) { s = s || 6; return '<g stroke="' + C.e + '" stroke-width="2.6" stroke-linecap="round"><line x1="' + (x - s) + '" y1="' + (y - s) + '" x2="' + (x + s) + '" y2="' + (y + s) + '"/><line x1="' + (x - s) + '" y1="' + (y + s) + '" x2="' + (x + s) + '" y2="' + (y - s) + '"/></g>'; }
  function mark(kind, x, y) { return kind === 'x' ? cross(x, y) : dot(x, y); }
  function arrowPath(x1, y1, x2, y2, col, w) {
    col = col || C.arrow; w = w || 6;
    var a = Math.atan2(y2 - y1, x2 - x1), h = 16;
    return line(x1, y1, x2 - Math.cos(a) * 6, y2 - Math.sin(a) * 6, w, col) +
      '<polygon points="' + x2 + ',' + y2 + ' ' + (x2 - h * Math.cos(a - 0.45)).toFixed(1) + ',' + (y2 - h * Math.sin(a - 0.45)).toFixed(1) + ' ' + (x2 - h * Math.cos(a + 0.45)).toFixed(1) + ',' + (y2 - h * Math.sin(a + 0.45)).toFixed(1) + '" fill="' + col + '"/>';
  }
  function sup(n) { return n === 1 ? '+' : n === -1 ? '\u2212' : (Math.abs(n) + (n > 0 ? '+' : '\u2212')); }

  /* ── atoms and ions ─────────────────────────────────────────── */
  // Electrons on a shell of radius r: pairs at the four compass points (dot-and-cross convention).
  function shellMarks(cx, cy, r, n, kinds, start) {
    var out = '', base = [ -90, 0, 90, 180 ];
    for (var i = 0; i < n; i++) {
      var slot = i % 4, paired = n > 4 && (i >= 4 || i + 4 < n);
      var deg = base[slot] + (paired ? (i >= 4 ? 13 : -13) : 0);
      if (n === 2 && r < 40) deg = base[i * 2];
      var a = deg * Math.PI / 180;
      out += mark(kinds[i] || 'o', cx + r * Math.cos(a), cy + r * Math.sin(a));
    }
    return out;
  }
  // atom: shells = [2,8,1]; kinds per shell as string e.g. 'x' or explicit arrays; opt.outerOnly
  function atom(cx, cy, sym, shells, opt) {
    opt = opt || {};
    var out = '', R0 = opt.r0 || 34, step = opt.step || 24;
    var list = opt.outerOnly ? [shells[shells.length - 1]] : shells;
    var nucR = opt.outerOnly ? 26 : 22;
    out += circ(cx, cy, nucR, opt.fill || C.nm, C.stroke, 2);
    out += T(cx, cy + 8, sym, opt.outerOnly ? 24 : 20);
    list.forEach(function (n, k) {
      var r = opt.outerOnly ? (opt.r || 62) : R0 + k * step;
      out += circ(cx, cy, r, 'none', C.stroke, 2.4);
      var kinds = [];
      var spec = (opt.kinds && opt.kinds[opt.outerOnly ? 0 : k]) || opt.kind || 'o';
      for (var i = 0; i < n; i++) kinds.push(typeof spec === 'string' ? (spec.length > 1 ? spec[i] : spec) : spec[i]);
      out += shellMarks(cx, cy, r, n, kinds);
    });
    if (opt.charge) {
      var rr = opt.outerOnly ? (opt.r || 62) + 16 : R0 + (list.length - 1) * step + 16;
      out += bracket(cx, cy, rr);
      out += T(cx + rr + 18, cy - rr + 14, sup(opt.charge), 26, { anchor: 'start' });
    }
    return out;
  }
  function bracket(cx, cy, r) {
    var d = 12;
    return '<path d="M' + (cx - r + d) + ' ' + (cy - r) + ' h' + (-d) + ' v' + (2 * r) + ' h' + d + '" fill="none" stroke="' + C.stroke + '" stroke-width="2.5"/>' +
      '<path d="M' + (cx + r - d) + ' ' + (cy - r) + ' h' + d + ' v' + (2 * r) + ' h' + (-d) + '" fill="none" stroke="' + C.stroke + '" stroke-width="2.5"/>';
  }
  var CONFIG = { H: [1], He: [2], Li: [2, 1], C: [2, 4], N: [2, 5], O: [2, 6], F: [2, 7], Ne: [2, 8], Na: [2, 8, 1], Mg: [2, 8, 2], Al: [2, 8, 3], S: [2, 8, 6], Cl: [2, 8, 7], K: [2, 8, 8, 1], Ca: [2, 8, 8, 2] };

  // Ionic pair before (stage 0) / during (1) / after (2) the transfer. metal/nonmetal symbols.
  function ionicTransfer(metal, nonmetal, stage, alt) {
    var mc = CONFIG[metal], nc = CONFIG[nonmetal];
    var lose = mc[mc.length - 1], W = 900, H = 360, y = 180, x1 = 230, x2 = 650;
    var body = '';
    if (stage < 2) {
      var mk = mc.map(function () { return 'x'; });
      var mo = mc.slice();
      body += atom(x1, y, metal, mo, { fill: C.metal, kinds: mk, r0: 36, step: 26 });
      body += atom(x2, y, nonmetal, nc, { fill: C.nm, r0: 36, step: 26 });
      body += T(x1, 340, metal + ' ' + mc.join('.'), 22, { weight: 'normal' });
      body += T(x2, 340, nonmetal + ' ' + nc.join('.'), 22, { weight: 'normal' });
      if (stage === 1) body += arrowPath(x1 + 36 + (mc.length - 1) * 26 + 10, y - 30, x2 - 36 - (nc.length - 1) * 26 - 12, y - 30);
    } else {
      var mion = mc.slice(0, -1), nion = nc.slice(); nion[nion.length - 1] += lose;
      var nk = nion.map(function (n, k) { if (k < nion.length - 1) return 'o'; var s = ''; for (var i = 0; i < n; i++) s += (i >= n - lose ? 'x' : 'o'); return s; });
      body += atom(x1, y, metal, mion, { fill: C.metal, kind: 'x', r0: 36, step: 26, charge: lose });
      body += atom(x2, y, nonmetal, nion, { fill: C.nm, kinds: nk, r0: 36, step: 26, charge: -lose });
      body += T(x1, 340, metal + sup(lose) + '  ' + mion.join('.'), 22, { weight: 'normal' });
      body += T(x2, 340, nonmetal + sup(-lose) + '  ' + nion.join('.'), 22, { weight: 'normal' });
    }
    return svg(W, H, body, alt || '');
  }

  /* ── covalent dot-and-cross (outer shells only, AQA convention) ── */
  // centre atom first; others placed at an angle so the shells overlap and the shared pairs sit in the overlap.
  var MOLDEF = {
    H2: ['H', 1, [['H', 1, 0, 1]]], Cl2: ['Cl', 7, [['Cl', 7, 0, 1]]], HCl: ['H', 1, [['Cl', 7, 0, 1]]],
    O2: ['O', 6, [['O', 6, 0, 2]]], N2: ['N', 5, [['N', 5, 0, 3]]],
    H2O: ['O', 6, [['H', 1, 145, 1], ['H', 1, 35, 1]]],
    NH3: ['N', 5, [['H', 1, 180, 1], ['H', 1, 0, 1], ['H', 1, 90, 1]]],
    CH4: ['C', 4, [['H', 1, 180, 1], ['H', 1, 0, 1], ['H', 1, -90, 1], ['H', 1, 90, 1]]],
    CO2: ['C', 4, [['O', 6, 180, 2], ['O', 6, 0, 2]]]
  };
  var MOL = {};
  Object.keys(MOLDEF).forEach(function (k) {
    var d = MOLDEF[k], rC = d[0] === 'H' ? 50 : 62, atoms = [[d[0], d[1], 0, 0]], bonds = [];
    d[2].forEach(function (o, i) {
      var r = o[0] === 'H' ? 50 : 62, dist = rC + r - 36, a = o[2] * Math.PI / 180;
      atoms.push([o[0], o[1], dist * Math.cos(a), dist * Math.sin(a)]); bonds.push([0, i + 1, o[3]]);
    });
    var minX = 1e9, maxX = -1e9, minY = 1e9, maxY = -1e9;
    atoms.forEach(function (a) { var r = a[0] === 'H' ? 50 : 62; minX = Math.min(minX, a[2] - r); maxX = Math.max(maxX, a[2] + r); minY = Math.min(minY, a[3] - r); maxY = Math.max(maxY, a[3] + r); });
    var W = 800, ox = W / 2 - (minX + maxX) / 2, oy = 40 - minY;
    atoms.forEach(function (a) { a[2] += ox; a[3] += oy; });
    MOL[k] = { atoms: atoms, bonds: bonds, H: maxY - minY + 80 };
  });
  function covalent(key, opt) {
    opt = opt || {};
    var m = MOL[key]; if (!m) return '';
    var body = '', rH = 50, rX = 62;
    var used = m.atoms.map(function () { return []; });
    var bondE = m.atoms.map(function () { return 0; });
    var showPairs = opt.pairs !== false;
    m.atoms.forEach(function (a, i) {
      var r = a[0] === 'H' ? rH : rX;
      body += circ(a[2], a[3], r, 'none', C.stroke, 2.4);
    });
    m.bonds.forEach(function (b) {
      var A = m.atoms[b[0]], B = m.atoms[b[1]], order = b[2];
      var ang = Math.atan2(B[3] - A[3], B[2] - A[2]);
      used[b[0]].push(ang); used[b[1]].push(ang + Math.PI);
      bondE[b[0]] += order; bondE[b[1]] += order;
      var rA = A[0] === 'H' ? rH : rX, rB = B[0] === 'H' ? rH : rX;
      var dAB = Math.hypot(B[2] - A[2], B[3] - A[3]);
      var t = (rA + (dAB - rB)) / 2 / dAB;
      var mx = A[2] + (B[2] - A[2]) * t, my = A[3] + (B[3] - A[3]) * t;
      var px = -Math.sin(ang), py = Math.cos(ang), ux = Math.cos(ang), uy = Math.sin(ang);
      if (!showPairs) return;
      for (var k = 0; k < order; k++) {
        var off = (k - (order - 1) / 2) * 17;
        var cx = mx + px * off, cy = my + py * off;
        body += mark('o', cx - ux * 8, cy - uy * 8) + mark('x', cx + ux * 8, cy + uy * 8);
      }
    });
    m.atoms.forEach(function (a, i) {
      var r = a[0] === 'H' ? rH : rX;
      body += circ(a[2], a[3], 22, a[0] === 'H' ? C.metal : C.nm, C.stroke, 2);
      body += T(a[2], a[3] + 8, a[0], 22);
      var lone = a[1] - bondE[i];
      var kind = i === 0 || key === 'H2' || key === 'Cl2' || key === 'O2' || key === 'N2' ? (i === 0 ? 'o' : 'x') : 'x';
      if (key === 'H2' || key === 'Cl2' || key === 'O2' || key === 'N2' || key === 'HCl') kind = i === 0 ? 'o' : 'x';
      if (lone > 0 && showPairs) {
        var cands = [];
        for (var d = 0; d < 360; d += 45) cands.push(d * Math.PI / 180);
        cands.sort(function (p, q) { return minGap(q, used[i]) - minGap(p, used[i]); });
        var pairs = Math.floor(lone / 2), single = lone % 2, picks = [];
        for (var c = 0; c < cands.length && picks.length < pairs + single; c++) {
          if (picks.every(function (pk) { return angDist(pk, cands[c]) > 1.2; })) picks.push(cands[c]);
        }
        picks.forEach(function (pa, n) {
          var rx = a[2] + r * Math.cos(pa), ry = a[3] + r * Math.sin(pa);
          var tx = -Math.sin(pa) * 8, ty = Math.cos(pa) * 8;
          if (n < pairs) body += mark(kind, rx - tx, ry - ty) + mark(kind, rx + tx, ry + ty);
          else body += mark(kind, rx, ry);
        });
      }
    });
    return svg(800, m.H, body, opt.alt || (key + ' dot-and-cross diagram'));
  }
  function angDist(a, b) { var d = Math.abs(a - b) % (2 * Math.PI); return d > Math.PI ? 2 * Math.PI - d : d; }
  function minGap(a, list) { var g = 9; list.forEach(function (b) { g = Math.min(g, angDist(a, b)); }); return g; }

  /* ── structures ─────────────────────────────────────────────── */
  function lattice(cation, anion, cols, rows, opt) {
    opt = opt || {};
    var s = opt.s || 64, x0 = 60, y0 = 50, body = '';
    var W = x0 * 2 + (cols - 1) * s, H = y0 * 2 + (rows - 1) * s + (opt.caption ? 30 : 0);
    for (var r = 0; r < rows; r++) for (var c = 0; c < cols; c++) {
      var x = x0 + c * s, y = y0 + r * s;
      if (c < cols - 1) body += line(x, y, x + s, y, 2, C.muted);
      if (r < rows - 1) body += line(x, y, x, y + s, 2, C.muted);
    }
    for (var r2 = 0; r2 < rows; r2++) for (var c2 = 0; c2 < cols; c2++) {
      var pos = (r2 + c2) % 2 === 0;
      var xx = x0 + c2 * s, yy = y0 + r2 * s;
      body += circ(xx, yy, pos ? s * 0.26 : s * 0.36, pos ? C.metal : C.nm, C.stroke, 2);
      body += T(xx, yy + 6, pos ? cation : anion, pos ? 14 : 16);
    }
    if (opt.caption) body += T(W / 2, H - 14, opt.caption, 18, { weight: 'normal', fill: C.muted });
    return svg(W, H, body, opt.alt || 'Part of a giant ionic lattice');
  }
  function metallic(cols, rows, opt) {
    opt = opt || {};
    var s = 72, x0 = 60, y0 = 56, body = '', W = x0 * 2 + (cols - 1) * s, H = y0 * 2 + (rows - 1) * s;
    var seed = 7; function rnd() { seed = (seed * 9301 + 49297) % 233280; return seed / 233280; }
    var alloyAt = opt.alloy || [];
    for (var r = 0; r < rows; r++) for (var c = 0; c < cols; c++) {
      var x = x0 + c * s, y = y0 + r * s, big = alloyAt.some(function (p) { return p[0] === r && p[1] === c; });
      body += circ(x, y, big ? 34 : 24, big ? C.gold : C.metal, C.stroke, 2);
      body += T(x, y + 7, big ? '' : '+', 22);
    }
    var ne = (opt.electrons || 1) * cols * rows;
    for (var i = 0; i < ne; i++) {
      var ex = x0 - 20 + rnd() * ((cols - 1) * s + 40), ey = y0 - 20 + rnd() * ((rows - 1) * s + 40);
      var cx = Math.round((ex - x0) / s), cy = Math.round((ey - y0) / s);
      var tries = 0; while (tries < 30) { var nx = Math.round((ex - x0) / s), ny = Math.round((ey - y0) / s); if (Math.hypot(ex - (x0 + nx * s), ey - (y0 + ny * s)) >= 31) break; ex = x0 - 20 + rnd() * ((cols - 1) * s + 40); ey = y0 - 20 + rnd() * ((rows - 1) * s + 40); tries++; }
      body += circ(ex, ey, 5, C.e);
    }
    return svg(W, H, body, opt.alt || 'Metal ions in a sea of delocalised electrons');
  }
  function particles(state, opt) {
    opt = opt || {};
    var W = 280, H = 220, body = '', r = 15;
    body += '<rect x="20" y="20" width="240" height="180" rx="10" fill="none" stroke="' + C.stroke + '" stroke-width="2.5"/>';
    var seed = state === 'gas' ? 11 : 5; function rnd() { seed = (seed * 9301 + 49297) % 233280; return seed / 233280; }
    if (state === 'solid') {
      for (var i = 0; i < 6; i++) for (var j = 0; j < 5; j++) body += circ(52 + i * 35, 200 - 20 - j * 31 - r + 2, r, C.nm, C.stroke, 2);
    } else if (state === 'liquid') {
      var pts = []; for (var k = 0; k < 40 && pts.length < 17; k++) { var tries = 0, x, y, bad; do { x = 38 + rnd() * 204; y = 78 + rnd() * 104; tries++; bad = pts.some(function (p) { return Math.hypot(p[0] - x, p[1] - y) < 2 * r + 1; }); } while (bad && tries < 200); if (!bad) pts.push([x, y]); }
      pts.forEach(function (p) { body += circ(p[0], p[1], r, C.nm, C.stroke, 2); });
    } else {
      var g = [[60, 60], [150, 45], [220, 90], [95, 140], [185, 165], [55, 175], [140, 110]];
      g.forEach(function (p) { body += circ(p[0], p[1], r, C.nm, C.stroke, 2); });
    }
    if (opt.label) body += T(W / 2, H - 2, opt.label, 18);
    return svg(W, H + 14, body, opt.alt || state + ' particle diagram');
  }

  /* ── circuits (port of physics_diagrams.circuit) ────────────── */
  var SPAN = 120;
  function leads(x, y, bw) { return line(x - SPAN / 2, y, x - bw / 2, y) + line(x + bw / 2, y, x + SPAN / 2, y); }
  function lab(x, y, t, size, col) { return T(x, y, t, size || 22, { fill: col || C.label }); }
  var SYM = {
    cell: function (x, y, it) { return leads(x, y, 36) + line(x - 9, y - 26, x - 9, y + 26) + line(x + 9, y - 13, x + 9, y + 13, 7, C.stroke, ' stroke-linecap="butt"') + (it.value ? lab(x, y + 52, it.value, 22, C.red) : ''); },
    battery: function (x, y, it) { var s = leads(x, y, 70); [-22, 14].forEach(function (dx) { s += line(x + dx, y - 26, x + dx, y + 26) + line(x + dx + 16, y - 13, x + dx + 16, y + 13, 7, C.stroke, ' stroke-linecap="butt"'); }); return s + (it.value ? lab(x, y + 52, it.value, 22, C.red) : ''); },
    power: function (x, y, it) { return leads(x, y, 70) + '<rect x="' + (x - 35) + '" y="' + (y - 26) + '" width="70" height="52" rx="6" fill="none" stroke="' + C.stroke + '" stroke-width="3"/>' + lab(x, y + 7, 'd.c.', 20) + (it.value ? lab(x, y + 52, it.value, 22, C.red) : ''); },
    resistor: function (x, y, it) { return leads(x, y, 80) + '<rect x="' + (x - 40) + '" y="' + (y - 17) + '" width="80" height="34" fill="' + C.cream + '" stroke="' + C.stroke + '" stroke-width="3"/>' + (it.name ? lab(x, y - 30, it.name) : '') + (it.value ? lab(x, y + 44, it.value, 22, C.red) : ''); },
    variable_resistor: function (x, y, it) { return leads(x, y, 80) + '<rect x="' + (x - 40) + '" y="' + (y - 17) + '" width="80" height="34" fill="' + C.cream + '" stroke="' + C.stroke + '" stroke-width="3"/>' + line(x - 46, y + 30, x + 46, y - 30) + '<polygon points="' + (x + 46) + ',' + (y - 30) + ' ' + (x + 30) + ',' + (y - 26) + ' ' + (x + 38) + ',' + (y - 14) + '" fill="' + C.stroke + '"/>' + (it.name ? lab(x, y - 40, it.name) : '') + (it.value ? lab(x, y + 52, it.value, 22, C.red) : ''); },
    lamp: function (x, y, it) { var d = 26 / Math.SQRT2; return leads(x, y, 56) + circ(x, y, 26, C.cream, C.stroke, 3) + line(x - d, y - d, x + d, y + d) + line(x - d, y + d, x + d, y - d) + (it.name ? lab(x, y - 36, it.name) : '') + (it.value ? lab(x, y + 50, it.value, 22, C.red) : ''); },
    switch: function (x, y, it) { return leads(x, y, 60) + circ(x - 30, y, 5, C.stroke) + circ(x + 30, y, 5, C.stroke) + (it.closed ? line(x - 30, y, x + 30, y) : line(x - 30, y, x + 24, y - 26)) + (it.name ? lab(x, y - 40, it.name) : ''); },
    ammeter: function (x, y, it) { return leads(x, y, 52) + circ(x, y, 26, C.cream, C.stroke, 3) + lab(x, y + 8, 'A', 26) + (it.name ? lab(x, y - 36, it.name, 20) : '') + (it.value ? lab(x, y + 50, it.value, 22, C.red) : ''); },
    voltmeter: function (x, y, it) { return circ(x, y, 26, C.cream, C.stroke, 3) + lab(x, y + 8, 'V', 26) + (it.value ? lab(x, y - 38, it.value, 22, C.red) : ''); },
    thermistor: function (x, y, it) { return leads(x, y, 80) + '<rect x="' + (x - 40) + '" y="' + (y - 17) + '" width="80" height="34" fill="' + C.cream + '" stroke="' + C.stroke + '" stroke-width="3"/>' + '<polyline points="' + (x - 46) + ',' + (y + 30) + ' ' + (x - 18) + ',' + (y + 30) + ' ' + (x + 40) + ',' + (y - 26) + '" fill="none" stroke="' + C.stroke + '" stroke-width="3"/>' + (it.name ? lab(x, y - 34, it.name) : ''); },
    ldr: function (x, y, it) { var s = leads(x, y, 80) + '<rect x="' + (x - 26) + '" y="' + (y - 13) + '" width="52" height="26" fill="' + C.cream + '" stroke="' + C.stroke + '" stroke-width="3"/>' + circ(x, y, 36, 'none', C.stroke, 2); for (var k = 0; k < 2; k++) { var sx = x - 70 + k * 22, sy = y - 64, ex = sx + 30, ey = sy + 30; s += line(sx, sy, ex, ey, 2.5) + '<polygon points="' + ex + ',' + ey + ' ' + (ex - 13) + ',' + (ey - 4) + ' ' + (ex - 4) + ',' + (ey - 13) + '" fill="' + C.stroke + '"/>'; } return s + (it.name ? lab(x, y - 58, it.name) : ''); },
    diode: function (x, y, it) { return leads(x, y, 56) + circ(x, y, 28, C.cream, C.stroke, 3) + '<polygon points="' + (x - 13) + ',' + (y - 15) + ' ' + (x - 13) + ',' + (y + 15) + ' ' + (x + 13) + ',' + y + '" fill="none" stroke="' + C.stroke + '" stroke-width="3"/>' + line(x + 13, y - 15, x + 13, y + 15) + (it.name ? lab(x, y - 40, it.name) : ''); },
    led: function (x, y, it) { var s = SYM.diode(x, y, {}); for (var k = 0; k < 2; k++) { var ax = x + 6 + k * 20, ay = y - 30; s += line(ax, ay, ax + 20, ay - 20, 2.5) + '<polygon points="' + (ax + 20) + ',' + (ay - 20) + ' ' + (ax + 7) + ',' + (ay - 17) + ' ' + (ax + 16) + ',' + (ay - 7) + '" fill="' + C.stroke + '"/>'; } return s + (it.name ? lab(x - 30, y - 44, it.name) : ''); },
    fuse: function (x, y, it) { return leads(x, y, 70) + '<rect x="' + (x - 35) + '" y="' + (y - 15) + '" width="70" height="30" fill="' + C.cream + '" stroke="' + C.stroke + '" stroke-width="3"/>' + line(x - 35, y, x + 35, y, 2) + (it.name ? lab(x, y - 28, it.name) : ''); },
    gap: function (x, y) { return line(x - SPAN / 2, y, x + SPAN / 2, y); }
  };
  function rowWidth(items) { var w = 0; items.forEach(function (it) { w += it.par ? Math.max.apply(null, it.par.map(rowWidth)) + 80 : SPAN; }); return w; }
  function rowDepth(items) { var d = 0; items.forEach(function (it) { if (it.par) d = Math.max(d, it.par.length - 1); }); return d; }
  /* spec: { top: [items], bottom: [items], meters: [{across:name,value}] , alt }
     item: {t:'lamp', name, value} or {par: [[items],[items]]} */
  function circuit(spec) {
    var top = spec.top || [], bottom = spec.bottom || [{ t: 'cell' }];
    var gap = 140, padX = 70, yTop = spec.meters && spec.meters.length ? 180 : 80;
    var wTop = rowWidth(top), wBot = rowWidth(bottom);
    var inner = Math.max(wTop, wBot + 120, 360);
    var L = padX, R = padX + inner;
    var depth = rowDepth(top);
    var yBot = yTop + Math.max(1, depth) * gap + (depth ? gap * 0.85 : 150);
    var W = R + padX, H = yBot + 90;
    var body = '', pos = {};
    function drawRow(items, y, x0, x1) {
      var w = rowWidth(items), spare = (x1 - x0) - w, x = x0, gapEach = spare / (items.length + 1), out = '';
      items.forEach(function (it) {
        out += line(x, y, x + gapEach, y); x += gapEach;
        if (it.par) {
          var pw = Math.max.apply(null, it.par.map(rowWidth)) + 80, xs = x, xe = x + pw;
          it.par.forEach(function (br, k) {
            var by = y + k * gap;
            out += drawRow(br, by, xs, xe);
            if (k > 0) { out += line(xs, by - gap, xs, by) + line(xe, by - gap, xe, by); }
          });
          for (var k2 = 0; k2 < it.par.length - 1; k2++) { out += circ(xs, y + k2 * gap, 6, C.stroke) + circ(xe, y + k2 * gap, 6, C.stroke); }
          x = xe;
        } else {
          var cx = x + SPAN / 2;
          out += (SYM[it.t] || SYM.gap)(cx, y, it);
          if (it.name) pos[it.name] = { x: cx, y: y };
          if (it.id) pos[it.id] = { x: cx, y: y };
          x += SPAN;
        }
      });
      out += line(x, y, x1, y);
      return out;
    }
    body += drawRow(top, yTop, L, R);
    body += drawRow(bottom, yBot, L, R);
    body += line(L, yTop, L, yBot) + line(R, yTop, R, yBot);
    (spec.meters || []).forEach(function (m) {
      var p = pos[m.across]; if (!p) return;
      var vy = p.y - 96, xl = p.x - 60, xr = p.x + 60;
      body += line(xl, p.y, xl, vy) + line(xl, vy, p.x - 26, vy) + line(p.x + 26, vy, xr, vy) + line(xr, vy, xr, p.y);
      body += circ(xl, p.y, 6, C.stroke) + circ(xr, p.y, 6, C.stroke);
      body += SYM.voltmeter(p.x, vy, { value: m.value });
    });
    (spec.notes || []).forEach(function (n) { body += T(n.x, n.y, n.text, n.size || 20, { fill: n.col || C.label }); });
    return svg(W, H, body, spec.alt || 'Circuit diagram');
  }
  /* data table drawn as a figure, so exam data is shown, never described */
  function table(head, rows, opt) {
    opt = opt || {};
    var cw = opt.widths || head.map(function () { return 200; }), rh = 56, W = cw.reduce(function (a, b) { return a + b; }, 0) + 40, H = rh * (rows.length + 1) + 40, body = '', x0 = 20, y0 = 20;
    body += '<rect x="' + x0 + '" y="' + y0 + '" width="' + (W - 40) + '" height="' + (H - 40) + '" fill="#FFFDF8" stroke="' + C.stroke + '" stroke-width="2.5"/>';
    var x = x0;
    cw.forEach(function (w, i) {
      if (i) body += line(x, y0, x, H - 20, 2, C.stroke);
      body += T(x + w / 2, y0 + 36, head[i], 19, { fill: C.label });
      rows.forEach(function (r, k) { body += T(x + w / 2, y0 + rh * (k + 1) + 36, r[i], 21, { fill: C.stroke, weight: i === 0 ? 'bold' : 'normal' }); });
      x += w;
    });
    for (var k = 0; k <= rows.length; k++) body += line(x0, y0 + rh * (k + 1), W - 20, y0 + rh * (k + 1), k === 0 ? 3 : 1.5, C.stroke);
    return svg(W, H, body, opt.alt || 'Data table');
  }
  function symbol(t, name) { return svg(170, 150, SYM[t](85, 82, { name: name }), name || t); }

  return { C: C, F: F, svg: svg, T: T, line: line, circ: circ, dot: dot, cross: cross, arrow: arrowPath, atom: atom, bracket: bracket,
    CONFIG: CONFIG, ionicTransfer: ionicTransfer, covalent: covalent, lattice: lattice, metallic: metallic, particles: particles,
    circuit: circuit, symbol: symbol, table: table, SYM: SYM, esc: esc };
})();
