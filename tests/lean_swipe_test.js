// Node test for shared/lean.js: where a swipe must not start. No DOM library: a few fake nodes.
// Run: node tests/lean_swipe_test.js
const fs = require("fs"), vm = require("vm"), path = require("path");
const src = fs.readFileSync(path.join(__dirname, "..", "shared", "lean.js"), "utf8");
const noop = () => {};
const ctx = {
  window: { addEventListener: noop, getComputedStyle: (el) => ({ overflowX: el.__ox || "visible" }) },
  document: { addEventListener: noop, readyState: "complete", body: null, querySelectorAll: () => [] },
  console,
};
ctx.window.window = ctx.window;
vm.createContext(ctx);
vm.runInContext(src.replace(/^\(function \(\) \{/, "(function () { var window = this.window, document = this.document;"), ctx);
const L = ctx.window.MrBadmusLean;
let fails = 0;
function node(tag, o = {}, parent = null) {
  return Object.assign({ nodeType: 1, tagName: tag, parentNode: parent, scrollWidth: 100, clientWidth: 100,
    classList: { contains: (c) => (o.cls || []).includes(c) }, hasAttribute: (a) => (o.attrs || []).includes(a) }, o);
}
const card = node("DIV", {});
function expect(name, got, want) { if (got !== want) { fails++; console.log("FAIL " + name + ": got " + got); } }
expect("plain text swipes", L.ignoresSwipe(node("P", {}, card), card), false);
expect("slider", L.ignoresSwipe(node("INPUT", {}, node("DIV", {}, card)), card), true);
expect("select", L.ignoresSwipe(node("SELECT", {}, card), card), true);
expect("textarea", L.ignoresSwipe(node("TEXTAREA", {}, card), card), true);
expect("preset button", L.ignoresSwipe(node("BUTTON", {}, node("DIV", {}, card)), card), true);
expect("card header button swipes", L.ignoresSwipe(node("SPAN", {}, node("BUTTON", { cls: ["lean-card-btn"] }, card)), card), false);
expect("data-no-swipe", L.ignoresSwipe(node("SPAN", {}, node("DIV", { attrs: ["data-no-swipe"] }, card)), card), true);
expect("sideways scroller", L.ignoresSwipe(node("SVG", {}, node("DIV", { scrollWidth: 300, __ox: "auto" }, card)), card), true);
expect("wide but not a scroller", L.ignoresSwipe(node("DIV", { scrollWidth: 300, __ox: "visible" }, card), card), false);
if (fails) { process.exit(1); }
console.log("lean_swipe_test: ok");
