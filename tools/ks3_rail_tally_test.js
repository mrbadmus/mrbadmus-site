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
 *   1b. The REAL `wireLadder` (exposed on the same hook) driven over a built
 *      lesson's ladder in a small fake DOM: the reopen the blind run hit
 *      (rungs 3-4 restored "rung met" from saved work, rungs 1-2 unanswered),
 *      a fresh ladder, and all four met this visit. Asserts the bar's tally
 *      (`data-rungs-met`/`data-rungs-total` through `railTally`), the
 *      ladder's own score line and the side rail's ladder stop (`doneByDom`)
 *      all tell the same story.
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
/* A localStorage the ladder reads its saved work from (1b), and timers that
   never fire: a resolved ladder ARMS a 20-second send, which would otherwise
   hold the process open (and there is no backend config, so it sends
   nothing either way). */
const store = new Map();
win.localStorage = {
  getItem: (k) => (store.has(k) ? store.get(k) : null),
  setItem: (k, v) => { store.set(k, String(v)); },
  removeItem: (k) => { store.delete(k); }
};
const sandbox = { window: win, document: doc, console, Math, JSON, Date,
                  setTimeout: () => 0, clearTimeout: noop,
                  navigator: { userAgent: "" } };
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

/* ── 1b. the real ladder over a built lesson ───────────────────────── */
const VOID = new Set(["area", "base", "br", "col", "embed", "hr", "img", "input",
  "link", "meta", "param", "source", "track", "wbr"]);
/* Just enough DOM for wireLadder and doneByDom: elements with attributes,
   classes, text, value/checked/disabled, listeners, and querySelector over
   the simple selectors the ladder uses (tag, .class, [attr], [attr="v"],
   :not([attr]), comma lists). */
const ENT = { amp: "&", quot: '"', lt: "<", gt: ">", apos: "'", "#39": "'", "#x27": "'" };
const decode = (t) => t.replace(/&(#?\w+);/g, (m, k) => (k in ENT ? ENT[k] : m));
class Node_ {
  constructor(tag, attrs) {
    this.tagName = tag ? tag.toUpperCase() : "";
    this.nodeType = tag ? 1 : 3;
    this.attrs = attrs || {};
    this.childNodes = [];
    this.parentNode = null;
    this.data = "";
    this.style = {};
    this.listeners = {};
    this.value = "";
    this.checked = "checked" in this.attrs;
    this.disabled = "disabled" in this.attrs;
    const self = this;
    this.classList = {
      contains: (c) => self.classes().includes(c),
      add: (...cs) => { const k = self.classes(); cs.forEach((c) => { if (!k.includes(c)) { k.push(c); } }); self.attrs.class = k.join(" "); },
      remove: (...cs) => { self.attrs.class = self.classes().filter((c) => !cs.includes(c)).join(" "); },
      toggle: (c, on) => { const has = self.classList.contains(c); const want = on === undefined ? !has : !!on;
        if (want && !has) { self.classList.add(c); } else if (!want && has) { self.classList.remove(c); } return want; }
    };
  }
  classes() { return (this.attrs.class || "").split(/\s+/).filter(Boolean); }
  get className() { return this.attrs.class || ""; }
  set className(v) { this.attrs.class = v; }
  get id() { return this.attrs.id || ""; }
  getAttribute(k) { return k in this.attrs ? this.attrs[k] : null; }
  setAttribute(k, v) { this.attrs[k] = String(v); }
  removeAttribute(k) { delete this.attrs[k]; }
  hasAttribute(k) { return k in this.attrs; }
  get children() { return this.childNodes.filter((n) => n.nodeType === 1); }
  get nextElementSibling() {
    if (!this.parentNode) { return null; }
    const sib = this.parentNode.children; return sib[sib.indexOf(this) + 1] || null;
  }
  appendChild(n) { if (n.parentNode) { n.parentNode.removeChild(n); } n.parentNode = this; this.childNodes.push(n); return n; }
  removeChild(n) { this.childNodes = this.childNodes.filter((c) => c !== n); n.parentNode = null; return n; }
  get textContent() { return this.nodeType === 3 ? this.data : this.childNodes.map((c) => c.textContent).join(""); }
  set textContent(v) { this.childNodes = []; const t = new Node_(); t.data = String(v); this.appendChild(t); }
  set innerHTML(v) { this.textContent = String(v).replace(/<[^>]*>/g, ""); }
  get innerHTML() { return this.textContent; }
  insertAdjacentHTML() {}
  cloneNode() {
    const c = new Node_(this.tagName.toLowerCase(), Object.assign({}, this.attrs));
    c.data = this.data; c.nodeType = this.nodeType;
    this.childNodes.forEach((k) => c.appendChild(k.cloneNode()));
    return c;
  }
  focus() {}
  addEventListener(t, fn) { (this.listeners[t] = this.listeners[t] || []).push(fn); }
  fire(t) { (this.listeners[t] || []).forEach((fn) => fn({ type: t, target: this })); }
  closest(sel) { let n = this; while (n && n.nodeType === 1) { if (matches(n, sel)) { return n; } n = n.parentNode; } return null; }
  querySelectorAll(sel) {
    const out = [];
    const walkEl = (n) => n.children.forEach((k) => { if (matches(k, sel)) { out.push(k); } walkEl(k); });
    walkEl(this); return out;
  }
  querySelector(sel) { return this.querySelectorAll(sel)[0] || null; }
}
function matchOne(el, sel) {
  const re = /([a-z][a-z0-9]*)|\.([\w-]+)|\[([\w-]+)(?:="([^"]*)")?\]|:not\(\[([\w-]+)\]\)/giy;
  sel = sel.trim();
  re.lastIndex = 0;
  while (re.lastIndex < sel.length) {
    const m = re.exec(sel);
    if (!m) { throw new Error("selector not supported: " + sel); }
    if (m[1] && el.tagName !== m[1].toUpperCase()) { return false; }
    if (m[2] && !el.classList.contains(m[2])) { return false; }
    if (m[3] && (!(m[3] in el.attrs) || (m[4] !== undefined && el.attrs[m[3]] !== m[4]))) { return false; }
    if (m[5] && m[5] in el.attrs) { return false; }
  }
  return true;
}
const matches = (el, sel) => sel.split(",").some((s1) => matchOne(el, s1));
function buildDom(html) {
  html = html.replace(/<!--[\s\S]*?-->/g, "")
             .replace(/<(script|style)\b[^>]*>[\s\S]*?<\/\1>/gi, "");
  const rootEl = new Node_("div", {});
  const stack = [rootEl];
  const re = /<(\/?)([a-zA-Z][a-zA-Z0-9-]*)((?:[^>"']|"[^"]*"|'[^']*')*)>|([^<]+)/g;
  let m;
  while ((m = re.exec(html))) {
    if (m[4] !== undefined) {
      const t = new Node_(); t.data = decode(m[4]); stack[stack.length - 1].appendChild(t); continue;
    }
    const close = m[1] === "/", tag = m[2].toLowerCase(), rest = m[3];
    if (close) {
      for (let i = stack.length - 1; i > 0; i--) { if (stack[i].tagName === tag.toUpperCase()) { stack.length = i; break; } }
      continue;
    }
    const attrs = {};
    const ar = /([^\s=/]+)(?:\s*=\s*("[^"]*"|'[^']*'|[^\s>]+))?/g;
    let a;
    while ((a = ar.exec(rest))) {
      let v = a[2] === undefined ? "" : a[2];
      if (/^["']/.test(v)) { v = v.slice(1, -1); }
      attrs[a[1].toLowerCase()] = decode(v);
    }
    const el = new Node_(tag, attrs);
    stack[stack.length - 1].appendChild(el);
    if (!VOID.has(tag) && !/\/\s*$/.test(rest)) { stack.push(el); }
  }
  return rootEl;
}
doc.createElement = (tag) => new Node_(tag, {});
doc.createTextNode = (t) => { const n = new Node_(); n.data = String(t); return n; };

const LESSON = path.join(ROOT, "ks3", "chemistry", "the-periodic-table", "group-7-the-halogens.html");
const LADDER_HTML = (() => {
  const h = fs.readFileSync(LESSON, "utf8");
  const i = h.indexOf('<section class="ks3-block ks3-ladder"');
  return h.slice(i, h.indexOf("</section>", i) + "</section>".length);
})();
const { wireLadder, doneByDom } = win.MRB_KS3_TEST_HOOK;

// One sitting: a fresh copy of the built ladder, wired by the real engine
// over whatever is in `store` (the pupil's saved work from earlier visits).
function sitting() {
  const lad = buildDom(LADDER_HTML).querySelector(".ks3-ladder");
  wireLadder(lad);
  const rungs = lad.querySelectorAll(".ks3-rung");
  return {
    lad, rungs,
    bar: () => t([{ met: lad.getAttribute("data-rungs-met"), total: lad.getAttribute("data-rungs-total") }], 0, 4),
    score: () => lad.querySelector("[data-score]").textContent,
    stop: () => doneByDom(lad),
    pick: (n, right) => {
      const opt = rungs[n - 1].querySelectorAll(".ks3-option")
        .find((b) => (b.getAttribute("data-correct") === "1") === right);
      opt.fire("click");
    },
    selfMark: (n) => {
      const r = rungs[n - 1];
      r.querySelector("[data-answer]").value = "A written answer that is comfortably over forty characters long.";
      r.querySelector("[data-answer]").fire("input");
      r.querySelector("[data-check]").fire("click");
      r.querySelectorAll("[data-crit]").forEach((b) => { b.checked = true; b.fire("change"); });
    },
    fold: (n) => rungs[n - 1].querySelector("[data-check]").fire("click")
  };
}

console.log("\nwireLadder over a built lesson (" + path.relative(ROOT, LESSON) + ")");
{
  // A first visit: nothing saved.
  store.clear();
  const s = sitting();
  check("fresh: bar", s.bar(), "0 / 4");
  check("fresh: score line", s.score(), "Not started yet.");
  check("fresh: ladder stop not ticked", s.stop(), false);

  // All four met this visit.
  s.pick(1, true); s.pick(2, true);
  check("rungs 1-2 right: bar", s.bar(), "2 / 4");
  check("rungs 1-2 right: score line", s.score(), "2 of 4 rungs met so far.");
  s.selfMark(3); s.selfMark(4);
  check("all four met: bar", s.bar(), "4 / 4");
  check("all four met: score line", s.score(), "You got 4 of 4.");
  check("all four met: ladder stop ticked", s.stop(), true);
  s.fold(4);
  check("criteria list folded away: stop stays ticked", s.stop(), true);
  check("criteria list folded away: bar unchanged", s.bar(), "4 / 4");

  // The reopen the blind run hit. The saved work from that sitting is what
  // the engine itself wrote to localStorage; MCQ answers are not saved.
  const r = sitting();
  check("reopen: rungs 3-4 restored as met, 1-2 unanswered: bar", r.bar(), "2 / 4");
  check("reopen: score line agrees with the bar", r.score(), "2 of 4 rungs met so far.");
  check("reopen: rungs 3-4 read rung met",
        [3, 4].map((n) => r.rungs[n - 1].querySelector("[data-tally]").textContent),
        ["All 5 ticked — rung met.", "All " + r.rungs[3].querySelectorAll("[data-crit]").length + " ticked — rung met."]);
  check("reopen: ladder stop not ticked (rungs 1-2 open)", r.stop(), false);
  r.pick(1, false);
  check("reopen, rung 1 wrong: bar", r.bar(), "2 / 4");
  check("reopen, rung 1 wrong: score line", r.score(), "2 of 4 rungs met so far.");
  r.pick(2, true);
  check("reopen, rung 2 right: bar", r.bar(), "3 / 4");
  check("reopen, rung 2 right: finished line", r.score(), "You got 3 of 4.");
  check("reopen, all resolved: ladder stop ticked", r.stop(), true);
  store.clear();
}

/* ── 2. every built KS3 lesson ─────────────────────────────────────── */

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
