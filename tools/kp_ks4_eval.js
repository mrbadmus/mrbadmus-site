#!/usr/bin/env node
// kp_ks4_eval.js — evaluate KS4 rebuilt-lesson logic per route, for the
// knowledge-point tagger (tools/kp_classify.py). No browser, no DOM.
//
// stdin:  {"repo": "<repo root>", "lessons": [{"slug", "logic", "routes": ["cf",...],
//          "imports": [{"name": "Ks4Choice", "attrs": {"prompt": "...", "options": "{{ x }}"}}]}]}
// stdout: {"<slug>": {"<route>": [{"name", "n", "props": {...}} | {"name", "n", "error"}]} ,
//          "<slug>__error": "..."}
//
// The lesson's own logic class (after the build's rulings, applied by the
// caller) is instantiated with props.route set to the route's label and
// libReady true, and renderVals() is called — exactly what the page does on
// mount, minus the DOM. Each answer block's attributes are then resolved
// against those values: a whole-attribute `{{ expr }}` is evaluated, a mixed
// string is interpolated, a plain string stays a string.
"use strict";
const fs = require("fs");
const path = require("path");
const vm = require("vm");

const ROUTE_LABEL = { cf: "Combined Foundation", ch: "Combined Higher",
                      tf: "Triple Foundation", th: "Triple Higher" };

const input = JSON.parse(fs.readFileSync(0, "utf8"));
// Every ks4-source*.js the pages load: the pilot's, then one per batch
// (each batch page loads ks4-source.js AND its own ks4-source-batch-N.js,
// all writing into window.KS4SRC).
const srcFiles = fs.readdirSync(path.join(input.repo, "shared"))
  .filter((f) => /^ks4-source(-batch-[a-z0-9-]+)?\.js$/.test(f)).sort()
  .map((f) => "shared/" + f);
const libs = srcFiles.concat(["shared/ks4-lib.js", "shared/ks4-diagrams.js"])
  .map((p) => fs.readFileSync(path.join(input.repo, p), "utf8"));

function noop() {}
function makeContext() {
  const sb = {
    console: { log: noop, warn: noop, error: noop },
    setInterval: () => 0, clearInterval: noop, setTimeout: () => 0, clearTimeout: noop,
    requestAnimationFrame: () => 0, cancelAnimationFrame: noop,
    matchMedia: () => ({ matches: false, addEventListener: noop, removeEventListener: noop }),
    document: { getElementById: () => null, querySelector: () => null, querySelectorAll: () => [],
                documentElement: { getAttribute: () => null }, addEventListener: noop },
    localStorage: { getItem: () => null, setItem: noop },
    IntersectionObserver: function () { return { observe: noop, disconnect: noop }; },
    performance: { now: () => 0 },
  };
  sb.window = sb;
  sb.React = { createElement: () => null, Fragment: "f" };
  vm.createContext(sb);
  for (const src of libs) vm.runInContext(src, sb);
  vm.runInContext(
    "class DCLogic { constructor(props) { this.props = props || {}; }" +
    " setState(o) { const v = typeof o === 'function' ? o(this.state, this.props) : o;" +
    " this.state = Object.assign({}, this.state, v); } forceUpdate() {} }", sb);
  return sb;
}

function plain(v, depth) {
  if (depth > 8) return null;
  if (v === null || v === undefined) return null;
  if (typeof v === "function") return undefined;
  if (typeof v !== "object") return v;
  if (Array.isArray(v)) return v.map((x) => plain(x, depth + 1)).filter((x) => x !== undefined);
  if (v.__mrbFig) return { figure: true, alt: v.alt || "" };
  const o = {};
  for (const k of Object.keys(v)) {
    const p = plain(v[k], depth + 1);
    if (p !== undefined) o[k] = p;
  }
  return o;
}

const out = {};
for (const L of input.lessons) {
  out[L.slug] = {};
  let sb;
  try {
    sb = makeContext();
    vm.runInContext(L.logic + "\n;globalThis.__C = Component;", sb);
  } catch (e) {
    out[L.slug + "__error"] = "logic did not load: " + e.message;
    continue;
  }
  for (const r of L.routes) {
    const res = [];
    let vals;
    try {
      const C = sb.__C;
      const c = new C({ route: ROUTE_LABEL[r], showDraft: false, theme: "light",
                        mrbPrevNext: { prev: null, next: null }, mrbRouteSwitch: {}, mrbSpecNote: {} });
      // what the page does on mount (sims and observers build objects some
      // lessons' `ready` waits on); timers are stubs, so nothing runs later
      try { if (c.componentDidMount) c.componentDidMount(); } catch (e) { /* DOM-only work */ }
      c.state = Object.assign({}, c.state || {}, { libReady: true });
      vals = c.renderVals();
    } catch (e) {
      out[L.slug][r] = [{ error: "renderVals failed: " + e.message }];
      continue;
    }
    sb.__vals = vals;
    const counts = {};
    for (const imp of L.imports) {
      counts[imp.name] = (counts[imp.name] || 0) + 1;
      const item = { name: imp.name, n: counts[imp.name], props: {} };
      try {
        for (const [k, raw] of Object.entries(imp.attrs)) {
          const whole = /^\s*\{\{([\s\S]*?)\}\}\s*$/.exec(raw);
          let v;
          if (whole) {
            sb.__expr = whole[1];
            v = vm.runInContext("(function(){ with (__vals) { return eval(__expr); } })()", sb);
          } else if (raw.indexOf("{{") >= 0) {
            v = raw.replace(/\{\{([\s\S]*?)\}\}/g, (_m, ex) => {
              sb.__expr = ex;
              const x = vm.runInContext("(function(){ with (__vals) { return eval(__expr); } })()", sb);
              return x === undefined || x === null ? "" : String(x);
            });
          } else {
            v = raw;
          }
          const p = plain(v, 0);
          if (p !== undefined) item.props[k] = p;
        }
      } catch (e) {
        item.error = e.message;
      }
      res.push(item);
    }
    out[L.slug][r] = res;
  }
}
process.stdout.write(JSON.stringify(out));
