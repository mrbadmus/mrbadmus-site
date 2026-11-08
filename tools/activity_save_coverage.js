#!/usr/bin/env node
// activity_save_coverage.js — the KS4 half of tools/activity_save_coverage.py.
// No browser, no DOM. For each rebuilt KS4 lesson page it loads the page's
// own inline scripts (the lesson's logic, its compiled template and the
// shared blocks) in a sandbox, exactly as tools/kp_ks4_eval.js does, and
// classifies every ROOT option group (a lesson's own activity, outside the
// shared blocks) with the classifier the page itself runs: the text between
// `<ks4-root-acts>` markers in shared/mrbadmus.v2.js (or --classifier FILE).
// It also counts Ks4Write instances that are marked by LEVELS (a level pick,
// not ticked points): standalone, a ladder's rung 4, a practice write item.
//
// stdin:  one page path per line (relative to the repo)
// argv:   <repo> [classifierFile]
// stdout: {"<page>": {"slug", "groups": [{g, kind, why, id, graded, by}], "levels": n, "error"?}}
"use strict";
const fs = require("fs");
const path = require("path");
const vm = require("vm");

const repo = process.argv[2];
let RA_SRC;
if (process.argv[3]) RA_SRC = fs.readFileSync(process.argv[3], "utf8");
else {
  const js = fs.readFileSync(path.join(repo, "shared/mrbadmus.v2.js"), "utf8");
  const a = js.indexOf("/* <ks4-root-acts>"), b = js.indexOf("/* </ks4-root-acts> */");
  if (a < 0 || b < 0) { process.stderr.write("no <ks4-root-acts> block in shared/mrbadmus.v2.js; pass a classifier file\n"); process.exit(2); }
  RA_SRC = js.slice(a, b);
}
const pages = fs.readFileSync(0, "utf8").split("\n").map((s) => s.trim()).filter(Boolean);
const srcFiles = fs.readdirSync(path.join(repo, "shared")).filter((f) => /^ks4-source(-batch-[a-z0-9-]+)?\.js$/.test(f)).sort().map((f) => "shared/" + f);
const libs = srcFiles.concat(["shared/ks4-lib.js", "shared/ks4-diagrams.js"]).map((p) => fs.readFileSync(path.join(repo, p), "utf8"));

function noop() {}
function makeContext(pagePath) {
  const el = () => ({ setAttribute: noop, getAttribute: () => null, appendChild: noop, style: {}, classList: { add: noop, remove: noop, contains: () => false }, addEventListener: noop });
  const sb = {
    console: { log: noop, warn: noop, error: noop },
    setInterval: () => 0, clearInterval: noop, setTimeout: () => 0, clearTimeout: noop,
    requestAnimationFrame: () => 0, cancelAnimationFrame: noop,
    matchMedia: () => ({ matches: false, addEventListener: noop, removeEventListener: noop }),
    document: { getElementById: () => null, querySelector: () => null, querySelectorAll: () => [], createElement: el,
      documentElement: { getAttribute: () => null, classList: { add: noop, remove: noop, toggle: noop, contains: () => false } },
      addEventListener: noop, removeEventListener: noop, body: el() },
    addEventListener: noop, removeEventListener: noop, pageYOffset: 0, scrollY: 0, innerWidth: 1280,
    location: { pathname: "/" + pagePath }, localStorage: { getItem: () => null, setItem: noop },
    IntersectionObserver: function () { return { observe: noop, disconnect: noop }; },
    performance: { now: () => 0 },
  };
  sb.window = sb;
  sb.React = { createElement: () => null, Fragment: "f" };
  vm.createContext(sb);
  for (const s of libs) vm.runInContext(s, sb);
  vm.runInContext(
    "class DCLogic { constructor(p){ this.props = p || {}; this.state = {}; }" +
    " setState(o){ const v = typeof o === 'function' ? o(this.state, this.props) : o; this.state = Object.assign({}, this.state, v); }" +
    " forceUpdate(){} componentDidMount(){} componentDidUpdate(){} componentWillUnmount(){} renderVals(){ return {}; } }" +
    " window.DCLogic = DCLogic; window.MrbRef = function () { return { current: null }; };", sb);
  sb.MrBadmusKS4Runtime = { mount: (o) => { sb.__mounted = o; } };
  return sb;
}
function look(expr, scope) { let c = scope; for (const p of String(expr).split(".")) { if (c == null) return undefined; c = c[p]; } return c; }
function attrVal(v, vals) {
  if (v && v.parts && v.parts.length === 1 && typeof v.parts[0] !== "string") return look(v.parts[0].e, vals);
  return v;
}
// Ks4Write instances marked by levels, among the root template's shared blocks.
function levelWrites(tpl, vals) {
  let n = 0;
  (function walk(x) {
    if (!x || typeof x !== "object") return;
    if (Array.isArray(x)) return x.forEach(walk);
    if (x.t === "child") {
      const a = x.a || {};
      if (x.comp === "Ks4Write") { const lv = attrVal(a.levels, vals); if (Array.isArray(lv) && lv.length) n += 1; }
      if (x.comp === "Ks4Ladder") { const r = attrVal(a.rungs, vals) || {}; if (r.r4 && Array.isArray(r.r4.levels) && r.r4.levels.length) n += 1; }
      if (x.comp === "Ks4Practice") {
        const r = attrVal(a.rungs, vals) || {};
        ["r1", "r2", "r3", "r4"].forEach((k) => (r[k] || []).forEach((it) => { if (it && (it.kind || "mcq") === "write" && Array.isArray(it.levels) && it.levels.length) n += 1; }));
      }
      return;
    }
    (x.c || []).forEach(walk);
  })(tpl.roots);
  return n;
}

const out = {};
for (const p of pages) {
  const res = { slug: path.basename(p, ".html"), groups: [], levels: 0 };
  out[p] = res;
  let html;
  try { html = fs.readFileSync(path.join(repo, p), "utf8"); } catch (e) { res.error = "unreadable"; continue; }
  if (html.indexOf("ks4-mount") < 0) { res.error = "not a rebuilt page"; continue; }
  const sb = makeContext(p);
  const re = /<script>([\s\S]*?)<\/script>/g; let m;
  try {
    while ((m = re.exec(html))) { if (/MrBadmusKS4Runtime\.mount|KS4_BLOCKS/.test(m[1])) vm.runInContext(m[1], sb); }
    vm.runInContext(RA_SRC + "\n;globalThis.__RA = KS4RootActs;", sb);
  } catch (e) { res.error = "load: " + e.message; continue; }
  const M = sb.__mounted, RA = sb.__RA;
  if (!M) { res.error = "no mount"; continue; }
  let L;
  try {
    L = new M.Component(M.props);
    try { if (L.componentDidMount) L.componentDidMount(); } catch (e) { /* DOM-only work */ }
    L.state = Object.assign({}, L.state, { libReady: true });
  } catch (e) { res.error = "construct: " + e.message; continue; }
  const init = RA.clone(L.state);
  let vals;
  try { vals = RA.valsAt(L, init); } catch (e) { res.error = "render: " + e.message; continue; }
  res.levels = levelWrites(M.template, vals);
  // ⊕ 8 Nov 2026: a lesson's own typed or selected answers. The option-group
  // classifier never sees these; they are listed so that they get counted.
  res.fields = [];
  (function walk(x) {
    if (!x || typeof x !== "object") return;
    if (Array.isArray(x)) return x.forEach(walk);
    if (x.t === "child") return;
    if ((x.t === "input" || x.t === "select" || x.t === "textarea") && x.onch) {
      res.fields.push({ on: x.onch, tag: x.t, type: (x.a && typeof x.a.type === "string") ? x.a.type : (x.t === "input" ? "text" : x.t) });
    }
    (x.c || []).forEach(walk);
  })(M.template.roots);
  const scal = Object.keys(init).filter((k) => typeof init[k] === "number" && k !== "active");
  for (const g of RA.groupsOf(M.template)) {
    const ois = g.inner ? [...new Set(RA.itemsOf(g, vals).map((x) => x.oi))] : [null];
    for (const oi of (ois.length ? ois : [null])) {
      let r;
      try { r = RA.analyse(L, g, init, init, oi); } catch (e) { r = { kind: "error", why: e.message }; }
      // A group that does nothing yet (an answered-only-later step) is asked
      // again on the steps the lesson can reach: each small number the state
      // holds, set to 0..5.
      if (r.kind === "none") {
        outer: for (const k of scal) for (let v = 0; v < 6; v += 1) {
          if (v === init[k]) continue;
          const st = Object.assign(RA.clone(init), { [k]: v });
          let r2; try { r2 = RA.analyse(L, g, st, init, oi); } catch (e) { continue; }
          if (r2.kind !== "none") { r = r2; break outer; }
        }
      }
      const answer = r.kind === "pick" || r.kind === "gate" || r.kind === "multi";
      res.groups.push({ g: g.e + (g.inner ? "[" + oi + "]." + g.inner : ""), e: g.e, kind: r.kind, why: r.why || null,
        id: answer ? RA.slotId(r, oi) : null, graded: !!r.graded,
        labels: answer ? (r.options || []).filter((o) => o.k !== r.check).map((o) => o.label) : [],
        right: answer && r.right ? (r.options || []).filter((o) => r.right.indexOf(o.k) >= 0).map((o) => o.label) : [],
        by: r.byFlag ? "flag" : r.byWords ? "words" : r.byTally ? "tally" : r.byAlert ? "style" : r.prediction ? "prediction" : (r.graded ? "key" : null) });
    }
  }
}
process.stdout.write(JSON.stringify(out));
