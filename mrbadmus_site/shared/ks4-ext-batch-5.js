/* shared/ks4-ext-batch-5.js — batch-5 pages only (source: ks4_lessons/batch5_ext.js; same code as batch 4).
   Standing ruling (MRB-302): a chemical formula renders with a real subscript. Design's
   verbatim quiz text carries Unicode subscript digits (U+2080..2089), which the house fonts
   do not have, so they fall back to a system font. This turns each run of them into a real
   <sub>2</sub> at display time. The authored text is untouched; the shared runtime is untouched.

   The runtime patches a text node IN PLACE (node.nodeValue = text), so the original node is
   kept as the first fragment and the pieces added after it are tracked: when the runtime
   writes new text into the node, the old pieces are removed and the new text is split again. */
(function () {
  var host = document.getElementById('ks4-mount');
  if (!host || !window.MutationObserver) return;
  var RE = /[₀-₉]+/;
  var RE_G = /[₀-₉]+/g;
  var made = new WeakMap();
  // ⊕ 17 Nov 2026: the runtime keeps each text node and, on every redraw, sets the element's
  // children back to [that node]. That removed the pieces split() had added after it and left
  // only the head ("CaCO₃(s) → CaO(s) + CO₂(g)" showed as "CaCO"); the runtime never rewrites
  // the node, because its own record still says the full text. So the full text is kept here,
  // and a node found holding only its head without its pieces is restored and split again.
  var orig = new WeakMap();   // text node -> { full, head }
  var owner = new WeakMap();  // added piece -> the text node it was split from
  var SVGNS = 'http://www.w3.org/2000/svg';
  var SKIP = { SCRIPT: 1, STYLE: 1, TEXTAREA: 1, INPUT: 1, SVG: 1, svg: 1 };

  function clear(n) {
    var list = made.get(n);
    if (!list) return;
    list.forEach(function (x) { if (x.parentNode) x.parentNode.removeChild(x); });
    made.delete(n);
  }
  function digits(run) {
    var s = '';
    for (var i = 0; i < run.length; i++) s += String(run.charCodeAt(i) - 0x2080);
    return s;
  }
  function intact(n) {
    var list = made.get(n);
    if (!list || !list.length) return false;
    var ref = n;
    for (var i = 0; i < list.length; i++) { if (ref.nextSibling !== list[i]) return false; ref = list[i]; }
    return true;
  }
  function split(n) {
    var o = orig.get(n);
    if (o && n.nodeValue === o.head) {
      if (intact(n)) return;
      n.nodeValue = o.full;
    }
    clear(n);
    orig.delete(n);
    var txt = n.nodeValue;
    if (!RE.test(txt)) return;
    var parent = n.parentNode;
    if (!parent || SKIP[parent.nodeName]) return;
    var parts = [], last = 0, m;
    RE_G.lastIndex = 0;
    while ((m = RE_G.exec(txt))) {
      parts.push({ t: txt.slice(last, m.index) });
      parts.push({ sub: digits(m[0]) });
      last = m.index + m[0].length;
    }
    parts.push({ t: txt.slice(last) });
    n.nodeValue = parts[0].t;
    var ref = n, added = [];
    for (var i = 1; i < parts.length; i++) {
      var p = parts[i], node;
      if (p.sub !== undefined && parent.namespaceURI === SVGNS) {
        // inside a figure label an HTML <sub> is not drawn ("CO2 in" showed as "CO in"): use an SVG tspan
        node = document.createElementNS(SVGNS, 'tspan'); node.setAttribute('baseline-shift', 'sub'); node.setAttribute('font-size', '75%'); node.textContent = p.sub;
      } else if (p.sub !== undefined) { node = document.createElement('sub'); node.textContent = p.sub; }
      else { if (!p.t) continue; node = document.createTextNode(p.t); }
      parent.insertBefore(node, ref.nextSibling);
      ref = node; added.push(node); owner.set(node, n);
    }
    made.set(n, added);
    orig.set(n, { full: txt, head: parts[0].t });
  }
  function scan(root) {
    if (root.nodeType === 3) { split(root); return; }
    // an added <svg> (a figure redrawn after a tap) is scanned too: its labels get SVG tspans
    if (root.nodeType !== 1 || (SKIP[root.nodeName] && root.nodeName !== 'svg' && root.nodeName !== 'SVG')) return;
    var w = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, null, false), list = [], x;
    while ((x = w.nextNode())) if (RE.test(x.nodeValue) || orig.has(x)) list.push(x);
    list.forEach(split);
  }
  var cfg = { childList: true, subtree: true, characterData: true };
  var obs = new MutationObserver(function (muts) {
    obs.disconnect();
    try {
      muts.forEach(function (mu) {
        if (mu.type === 'characterData') split(mu.target);
        else {
          mu.addedNodes.forEach(scan);
          // a piece taken away by a redraw: put its text node back together
          mu.removedNodes.forEach(function (r) {
            var n = owner.get(r);
            if (n && n.isConnected) split(n);
          });
        }
      });
    } finally { obs.observe(host, cfg); }
  });
  scan(host);
  obs.observe(host, cfg);
})();
