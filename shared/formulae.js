/* ⊕ MRB-351 — chemical formulae, rendered with real subscripts, in the browser.
 *
 * The JavaScript twin of `formulae()` in ks3_art/kit.py (MRB-302, "STORE
 * FLAT, RENDER SUBSCRIPT"), for text that only exists at run time: a
 * teacher's flashcard deck. The stored string is never changed; this only
 * decides how it is DRAWN.
 *
 * The rule is the Python one, token for token, and must stay so:
 *   · a token is a run of element symbols with digits, optionally led by a
 *     coefficient (`2CO2`: the 2 in front stays full size);
 *   · every symbol must be a real element (or the placeholder X);
 *   · there must be a digit to drop, and TWO OR MORE element groups — or the
 *     token must be one of the genuinely subscripted single-element species
 *     (O2, H2, Cl2 …). `C1`, `P11`, `B2` are unit codes, not formulae;
 *   · `KS3`/`KS4` parse as K+S+digit and are denied by name.
 *
 * It builds DOM (text nodes and <sub> elements), never HTML strings, so a
 * card's text can never become markup.
 *
 *   MRBFormulae.nodes("Water is H2O")  → [Text "Water is H", <sub>2</sub>, Text "O"]
 *   MRBFormulae.fill(el, "CO2")         → replaces el's children
 *   MRBFormulae.segments("CO2")         → [{t:"CO"},{sub:"2"}]   (for templating)
 */
(function (root) {
  "use strict";

  var ELEMENTS = {};
  ("H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca Sc Ti V Cr Mn Fe Co Ni " +
   "Cu Zn Ga Ge As Se Br Kr Rb Sr Y Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I Xe " +
   "Cs Ba La Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu Hf Ta W Re Os Ir Pt Au " +
   "Hg Tl Pb Bi Po At Rn Fr Ra Ac Th Pa U Np Pu Am Cm")
    .split(" ").forEach(function (s) { ELEMENTS[s] = true; });
  var PLACEHOLDER = { X: true };
  var SINGLE_WITH_SUB = { H2: 1, O2: 1, N2: 1, F2: 1, Cl2: 1, Br2: 1, I2: 1, O3: 1, S8: 1, P4: 1 };
  var NOT_FORMULAE = { KS3: 1, KS4: 1 };

  // The Python pattern uses a lookbehind; this one captures the preceding
  // character instead, so it runs on every browser the site supports.
  var TOKEN = /(^|[^0-9A-Za-z<&\/])(\d*)((?:[A-Z][a-z]?\d*)+)(?![0-9A-Za-z;])/g;
  var GROUP = /([A-Z][a-z]?)(\d*)/g;

  function groupsOf(body) {
    var out = [], m;
    GROUP.lastIndex = 0;
    while ((m = GROUP.exec(body)) !== null) { out.push([m[1], m[2]]); }
    return out;
  }

  function isFormula(body) {
    if (NOT_FORMULAE[body]) { return false; }
    var g = groupsOf(body);
    if (!g.length) { return false; }
    for (var i = 0; i < g.length; i++) {
      if (!ELEMENTS[g[i][0]] && !PLACEHOLDER[g[i][0]]) { return false; }
    }
    if (!g.some(function (x) { return x[1]; })) { return false; }
    if (g.length < 2 && !SINGLE_WITH_SUB[body]) { return false; }
    return true;
  }

  function segments(text) {
    var s = String(text == null ? "" : text);
    var out = [], last = 0, m;
    var push = function (t) {
      if (!t) { return; }
      var prev = out[out.length - 1];
      if (prev && prev.t !== undefined) { prev.t += t; } else { out.push({ t: t }); }
    };
    TOKEN.lastIndex = 0;
    while ((m = TOKEN.exec(s)) !== null) {
      var lead = m[1], coeff = m[2], body = m[3];
      var start = m.index + lead.length;
      if (!isFormula(body)) { continue; }
      push(s.slice(last, start));
      push(coeff);
      groupsOf(body).forEach(function (g) {
        push(g[0]);
        if (g[1]) { out.push({ sub: g[1] }); }
      });
      last = start + coeff.length + body.length;
      // The token regex consumed the lead character; let the next search
      // start right after this token so adjacent formulae are all found.
      TOKEN.lastIndex = last;
    }
    push(s.slice(last));
    return out;
  }

  function nodes(text, doc) {
    doc = doc || root.document;
    return segments(text).map(function (seg) {
      if (seg.sub !== undefined) {
        var el = doc.createElement("sub");
        el.textContent = seg.sub;
        return el;
      }
      return doc.createTextNode(seg.t);
    });
  }

  function fill(el, text) {
    while (el.firstChild) { el.removeChild(el.firstChild); }
    nodes(text, el.ownerDocument).forEach(function (n) { el.appendChild(n); });
    return el;
  }

  var api = { segments: segments, nodes: nodes, fill: fill, isFormula: isFormula };
  if (typeof module !== "undefined" && module.exports) { module.exports = api; }
  root.MRBFormulae = api;
})(typeof window !== "undefined" ? window : globalThis);
