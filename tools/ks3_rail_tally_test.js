/* ks3_rail_tally_test.js — the KS3 lesson progress bar counts RUNGS.
 *
 *   node tools/ks3_rail_tally_test.js
 *
 * ⊕ B2C polish (9 Oct 2026, R14). Mide's rule: the sticky progress bar on a
 * lesson page matches the mastery-ladder rungs. Its count and fill are rungs
 * MET out of rungs on the page wherever the reader is scrolled; START HERE and
 * every other non-rung question never move it.
 *
 * Two halves:
 *
 *   1. `railTally` from the REAL shared/ks3.js (loaded in a vm sandbox with
 *      `window.MRB_KS3_TEST_HOOK`, which is the only thing the hook exposes),
 *      driven through the cases the blind run hit.
 *
 *   2. Every built KS3 lesson under ks3/ (185 of them), read as HTML with no
 *      browser. For each, the rungs `wireLadder` will count are enumerated by
 *      the same rule it uses (a `.ks3-rung` inside a `.ks3-ladder`; self-marked
 *      when `data-mode="self"` or, with no mode, when it has `[data-ticks]`;
 *      counted when self-marked with ticks or page-marked with `.ks3-option`s).
 *      It asserts every lesson has scorable rungs — so the bar never falls
 *      back to counting stages — and that no ladder sits inside the first
 *      rail stop (START HERE), so answering it cannot reach the count.
 *
 * Not a registered gate (same reasoning as tools/set_work_time_test.js): it
 * is run by hand and its result is recorded in the run report.
 */
"use strict";

const fs = require("fs");
const path = require("path");
const vm = require("vm");

const ROOT = path.join(__dirname, "..");
const SRC = path.join(ROOT, "shared", "ks3.js");

/* ── 1. the pure tally ─────────────────────────────────────────────── */
const noop = () => {};
const doc = {
  readyState: "loading",            // keeps init() from running
  addEventListener: noop,
  querySelectorAll: () => [],
  querySelector: () => null,
  documentElement: { style: { setProperty: noop } },
  createElement: () => ({ style: {}, setAttribute: noop, appendChild: noop })
};
const win = {
  MRB_KS3_TEST_HOOK: {},
  addEventListener: noop,
  matchMedia: () => ({ matches: false, addListener: noop })
};
const sandbox = { window: win, document: doc, console, Math, JSON, Date,
                  setTimeout, clearTimeout, navigator: { userAgent: "" } };
vm.createContext(sandbox);
vm.runInContext(fs.readFileSync(SRC, "utf8"), sandbox, { filename: SRC });
const railTally = win.MRB_KS3_TEST_HOOK.railTally;
if (typeof railTally !== "function") {
  console.error("FAIL shared/ks3.js did not expose railTally on the test hook");
  process.exit(2);
}

let failures = 0;
function check(name, got, want) {
  const g = JSON.stringify(got), w = JSON.stringify(want);
  const ok = g === w;
  if (!ok) { failures += 1; }
  console.log(`${ok ? "  ok  " : "  FAIL"}  ${name}${ok ? "" : `\n           got  ${g}\n           want ${w}`}`);
}
const t = (l, d, s) => { const r = railTally(l, d, s); return `${r.shown} / ${r.of}`; };

console.log("railTally (shared/ks3.js)");
// The alveoli page: 4 stages, 4 rungs.
check("load: nothing done", t([{ met: "0", total: "4" }], 0, 4), "0 / 4");
check("START HERE answered (a stage, not a rung) does not move it",
      t([{ met: "0", total: "4" }], 1, 4), "0 / 4");
check("START HERE + both activities, no rung", t([{ met: "0", total: "4" }], 3, 4), "0 / 4");
check("rung 1 met", t([{ met: "1", total: "4" }], 1, 4), "1 / 4");
check("rungs 1-4 met", t([{ met: "4", total: "4" }], 4, 4), "4 / 4");
check("all four met, scrolled back to the top (stages done 2)",
      t([{ met: "4", total: "4" }], 2, 4), "4 / 4");
check("a wrong rung is resolved, not met", t([{ met: "2", total: "4" }], 4, 4), "2 / 4");
check("numbers as well as attribute strings", t([{ met: 3, total: 4 }], 0, 5), "3 / 4");
check("stage count never leaks in when stages > rungs", t([{ met: "1", total: "4" }], 5, 6), "1 / 4");
check("met clamped to total", t([{ met: "9", total: "4" }], 0, 4), "4 / 4");
check("garbage met reads 0", t([{ met: "x", total: "4" }], 3, 4), "0 / 4");
check("two ladders sum", t([{ met: "1", total: "4" }, { met: "2", total: "3" }], 0, 4), "3 / 7");
check("a ladder with no scorable rung is skipped", t([{ met: "0", total: "0" }, { met: "1", total: "4" }], 3, 4), "1 / 4");
check("no rungs on the page at all: stages", t([], 2, 5), "2 / 5");
check("unit says rungs", railTally([{ met: 1, total: 4 }], 0, 4).unit, "rungs");

/* ── 2. every built KS3 lesson ─────────────────────────────────────── */
const VOID = new Set(["area", "base", "br", "col", "embed", "hr", "img", "input",
  "link", "meta", "param", "source", "track", "wbr"]);

function parse(html) {
  html = html.replace(/<!--[\s\S]*?-->/g, "")
             .replace(/<(script|style)\b[^>]*>[\s\S]*?<\/\1>/gi, "");
  const rootEl = { tag: "#root", attrs: {}, kids: [] };
  const stack = [rootEl];
  const re = /<(\/?)([a-zA-Z][a-zA-Z0-9-]*)((?:[^>"']|"[^"]*"|'[^']*')*)>/g;
  let m;
  while ((m = re.exec(html))) {
    const close = m[1] === "/", tag = m[2].toLowerCase(), rest = m[3];
    if (close) {
      for (let i = stack.length - 1; i > 0; i--) {
        if (stack[i].tag === tag) { stack.length = i; break; }
      }
      continue;
    }
    const attrs = {};
    const ar = /([^\s=/]+)(?:\s*=\s*("[^"]*"|'[^']*'|[^\s>]+))?/g;
    let a;
    while ((a = ar.exec(rest))) {
      let v = a[2] === undefined ? "" : a[2];
      if (/^["']/.test(v)) { v = v.slice(1, -1); }
      attrs[a[1].toLowerCase()] = v;
    }
    const el = { tag, attrs, kids: [] };
    stack[stack.length - 1].kids.push(el);
    if (!VOID.has(tag) && !/\/\s*$/.test(rest)) { stack.push(el); }
  }
  return rootEl;
}
const hasClass = (el, c) => (" " + (el.attrs.class || "") + " ").includes(" " + c + " ");
function find(el, pred, out = []) {
  for (const k of el.kids) { if (pred(k)) { out.push(k); } find(k, pred, out); }
  return out;
}
const some = (el, pred) => find(el, pred).length > 0;

function walk(dir, out = []) {
  for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
    const p = path.join(dir, e.name);
    if (e.isDirectory()) { walk(p, out); }
    else if (e.name.endsWith(".html")) { out.push(p); }
  }
  return out;
}

console.log("\nEvery built KS3 lesson (ks3/**)");
let lessons = 0, noRungs = [], ladderInFirst = [], rungDist = {}, stagesDiffer = 0;
for (const file of walk(path.join(ROOT, "ks3"))) {
  const html = fs.readFileSync(file, "utf8");
  if (!/data-ks3-lesson="[a-z0-9]/.test(html) || !html.includes("data-rail-stages")) { continue; }
  lessons += 1;
  const dom = parse(html);
  const rel = path.relative(ROOT, file);
  let rungs = 0;
  for (const lad of find(dom, (e) => hasClass(e, "ks3-ladder"))) {
    for (const r of find(lad, (e) => hasClass(e, "ks3-rung"))) {
      const mode = r.attrs["data-mode"];
      const ticks = some(r, (e) => "data-ticks" in e.attrs);
      const opts = some(r, (e) => hasClass(e, "ks3-option"));
      const self = mode === "self" || (!mode && ticks);
      if ((self && ticks) || (!self && opts)) { rungs += 1; }
    }
  }
  rungDist[rungs] = (rungDist[rungs] || 0) + 1;
  if (!rungs) { noRungs.push(rel); }
  const rails = find(dom, (e) => "data-rail-stages" in e.attrs)[0];
  const stages = JSON.parse(rails.attrs["data-rail-stages"]
    .replace(/&quot;/g, '"').replace(/&#x27;/g, "'").replace(/&#39;/g, "'")
    .replace(/&lt;/g, "<").replace(/&gt;/g, ">").replace(/&amp;/g, "&"));
  if (stages.length !== rungs) { stagesDiffer += 1; }
  const first = find(dom, (e) => e.attrs.id === stages[0].anchor)[0];
  if (first && some(first, (e) => hasClass(e, "ks3-ladder"))) { ladderInFirst.push(rel); }
}
check("185 lessons read", lessons, 185);
check("every lesson has scorable rungs (bar never counts stages)", noRungs, []);
check("no ladder inside the first rail stop (START HERE)", ladderInFirst, []);
console.log(`        rungs per lesson: ${JSON.stringify(rungDist)}; ` +
            `lessons whose stage count differs from their rung count: ${stagesDiffer}`);

console.log(failures ? `\n${failures} FAILED` : "\nall passed");
process.exit(failures ? 1 : 0);
