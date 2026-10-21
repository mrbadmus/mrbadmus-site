/* set_work_challenge_test.js — Unit C: `openChallenge` / `attachChallenge` in
 * shared/set-work.js, against a stubbed fetch and a tiny stand-in DOM.
 *
 *   node tools/set_work_challenge_test.js
 *
 * Loads the REAL file (see set_work_time_test.js for why). What it pins:
 *   · ready=false  -> the page's side of the seam draws NOTHING
 *   · ready=true   -> a "Set as homework" control per subject
 *   · tap          -> the sheet lists the teacher's KS4 classes only
 *   · tap Set      -> POST /api/teacher/set-work/challenge, body EXACT
 *   · Undo         -> DELETE /api/teacher/set-work/<assignment id>
 *   · already_set, error words, a separate-science class for another science
 *   · the "closes" instant is the next Friday 10:15 London, BST and GMT
 *
 * Not a registered gate (lives in tools/, like set_work_time_test.js); run by
 * hand and recorded in the run report.
 */
"use strict";

const fs = require("fs");
const path = require("path");
const vm = require("vm");

const SRC = path.join(__dirname, "..", "shared", "set-work.js");

/* ── a stand-in DOM, just big enough for the sheet ───────────────────── */
function makeNode(tag) {
  const n = {
    tagName: String(tag).toUpperCase(), children: [], attrs: {}, handlers: {},
    className: "", _text: "", hidden: false, disabled: false, style: {},
    tabIndex: 0, type: "",
    appendChild(c) { this.children.push(c); c.parent = this; return c; },
    setAttribute(k, v) { this.attrs[k] = String(v); },
    getAttribute(k) { return (k in this.attrs) ? this.attrs[k] : null; },
    addEventListener(t, f) { (this.handlers[t] = this.handlers[t] || []).push(f); },
    focus() {},
    click() {
      if (this.disabled) { return; }
      (this.handlers.click || []).forEach(function (f) { f({ target: n, stopPropagation() {} }); });
    },
    all() {
      let out = [];
      this.children.forEach(function (c) { out.push(c); out = out.concat(c.all()); });
      return out;
    },
    byData(v) { return this.all().filter(function (c) { return c.attrs["data-sw"] === v; }); }
  };
  Object.defineProperty(n, "textContent", {
    get() { return this._text; },
    set(v) { this._text = String(v); if (v === "") { this.children = []; } }
  });
  return n;
}
const body = makeNode("body");
const document = {
  body, activeElement: null,
  createElement: makeNode,
  createElementNS: makeNode
};

/* ── a stubbed backend ────────────────────────────────────────────────── */
const calls = [];
let readyAnswer = true;
let nextPost = null;
let nextDelete = null;
function res(status, bodyObj) {
  return Promise.resolve({ status, ok: status >= 200 && status < 300,
                           json() { return Promise.resolve(bodyObj); } });
}
function fetchStub(url, init) {
  init = init || {};
  calls.push({ url, method: init.method || "GET", headers: init.headers || {}, body: init.body });
  if (/\/challenge\/ready$/.test(url)) { return res(200, { ready: readyAnswer }); }
  if (/\/set-work\/challenge$/.test(url) && init.method === "POST") { return nextPost(); }
  if (/\/set-work\/[^/]+$/.test(url) && init.method === "DELETE") { return nextDelete(); }
  return res(404, null);
}
const client = { auth: { getSession() {
  return Promise.resolve({ data: { session: { access_token: "tok-123" } } });
} } };

const sandbox = {
  window: { MrBadmusConfig: { BACKEND_URL: "https://api.test" } },
  document, fetch: fetchStub, console, Intl, Date, Math, JSON, Promise,
  setTimeout, clearTimeout
};
sandbox.globalThis = sandbox;
vm.createContext(sandbox);
vm.runInContext(fs.readFileSync(SRC, "utf8"), sandbox, { filename: SRC });
const SW = sandbox.window.MRBSetWork;

let failures = 0;
function check(name, got, want) {
  const ok = JSON.stringify(got) === JSON.stringify(want);
  if (!ok) { failures += 1; }
  console.log(`${ok ? "  ok  " : "  FAIL"}  ${name}${ok ? "" : `\n           got  ${JSON.stringify(got)}\n           want ${JSON.stringify(want)}`}`);
}
const tick = () => new Promise(function (r) { setImmediate(r); });
async function settle() { for (let i = 0; i < 8; i++) { await tick(); } }

(async function () {
  if (!SW || typeof SW.openChallenge !== "function" || typeof SW.attachChallenge !== "function") {
    console.error("set_work_challenge_test: shared/set-work.js did not expose the challenge surface");
    process.exit(2);
  }

  /* ── the closing instant ─────────────────────────────────────────────
     Wed 21 Oct 2026 12:00Z, BST -> Fri 23 Oct 10:15 BST = 09:15Z.
     Fri 23 Oct 10:30 BST (09:30Z) is past this week's drop -> Fri 30 Oct,
     GMT by then (BST ended 25 Oct) -> 10:15Z.
     Fri 23 Oct 10:00 BST (09:00Z) is still before it -> the same day. */
  console.log("the challenge closes at the next Friday 10:15 London");
  check("Wed 21 Oct (BST)", SW.challengeClosesAt(Date.parse("2026-10-21T12:00:00Z")), "2026-10-23T09:15:00.000Z");
  check("Fri 23 Oct 10:30 BST -> next Friday, GMT", SW.challengeClosesAt(Date.parse("2026-10-23T09:30:00Z")), "2026-10-30T10:15:00.000Z");
  check("Fri 23 Oct 10:00 BST -> today", SW.challengeClosesAt(Date.parse("2026-10-23T09:00:00Z")), "2026-10-23T09:15:00.000Z");

  /* ── ready = false: nothing is drawn ─────────────────────────────── */
  console.log("\nready=false draws nothing");
  const hosts = { biology: makeNode("div"), chemistry: makeNode("div"), physics: makeNode("div") };
  readyAnswer = false;
  const drew = await SW.attachChallenge({ client, hosts, buttonClass: "sc-hw" });
  check("attachChallenge resolves false", drew, false);
  check("no control in any host", Object.keys(hosts).map(function (k) { return hosts[k].children.length; }), [0, 0, 0]);
  check("the only request was GET /ready, with the Bearer token",
    calls.map(function (c) { return c.method + " " + c.url + " " + c.headers.Authorization; }),
    ["GET https://api.test/api/teacher/set-work/challenge/ready Bearer tok-123"]);
  check("no overlay was built", body.children.length, 0);

  /* ── ready = true: a control per subject ─────────────────────────── */
  console.log("\nready=true draws a control per subject");
  readyAnswer = true;
  const classes = [
    { id: "c1", name: "10a/Sc1", key_stage: "KS4" },
    { id: "c2", name: "7h/Sc5", key_stage: "KS3" },
    { id: "c3", name: "11a/Ph1", key_stage: "KS4" },
    { id: "c4", name: "10b/Sc2", key_stage: "KS4" }
  ];
  const drew2 = await SW.attachChallenge({ client, hosts, buttonClass: "sc-hw", classes });
  check("attachChallenge resolves true", drew2, true);
  check("a button in each host, saying Set as homework",
    Object.keys(hosts).map(function (k) { return hosts[k].children[0] && hosts[k].children[0].textContent; }),
    ["Set as homework", "Set as homework", "Set as homework"]);
  check("with the page's own class", hosts.biology.children[0].className, "sc-hw");

  /* ── tap Biology ─────────────────────────────────────────────────── */
  console.log("\ntapping Set as homework on Biology");
  hosts.biology.children[0].click();
  await settle();
  const overlay = body.children[0];
  check("the overlay is open", overlay.hidden, false);
  check("heading", overlay.byData("challenge-title")[0].textContent, "Set this week\u2019s Biology challenge");
  check("due line says when it closes", /^Due when it closes, (Mon|Tue|Wed|Thu|Fri|Sat|Sun) \d{1,2} [A-Z][a-z]{2}, \d\d:\d\d$/.test(overlay.byData("challenge-due")[0].textContent), true);
  const rows = overlay.byData("challenge-class");
  check("KS4 classes only, KS3 left out", rows.map(function (r) { return r.attrs["data-sw-ref"]; }), ["c1", "c4", "c3"]);
  const rowOf = function (id) { return rows.filter(function (r) { return r.attrs["data-sw-ref"] === id; })[0]; };
  const part = function (row, v) { return row.byData(v)[0]; };
  const tagOf = function (row) { return row.all().filter(function (c) { return /sw-row-tag/.test(c.className); })[0]; };
  check("a Physics-only class is disabled for Biology, with its reason",
    [rowOf("c3").attrs["aria-disabled"], tagOf(rowOf("c3")).textContent], ["true", "Physics only"]);
  check("a combined class is enabled", rowOf("c1").attrs["aria-disabled"], "false");
  check("Undo is hidden before anything is set", part(rowOf("c1"), "challenge-undo").hidden, true);

  /* ── tap Set ─────────────────────────────────────────────────────── */
  console.log("\ntapping Set on 10a/Sc1");
  calls.length = 0;
  nextPost = function () {
    return res(200, { assignments: [{ id: "a1", class_id: "c1", class_name: "10a/Sc1",
                                      due_at: "2026-10-23T09:15:00.000Z", already_set: false }] });
  };
  part(rowOf("c1"), "challenge-set").click();
  await settle();
  check("exactly one request", calls.length, 1);
  check("POST to the challenge route", calls[0].method + " " + calls[0].url, "POST https://api.test/api/teacher/set-work/challenge");
  check("body is EXACT", calls[0].body, JSON.stringify({ class_ids: ["c1"], subject: "biology" }));
  check("Bearer token and JSON content type", [calls[0].headers.Authorization, calls[0].headers["Content-Type"]], ["Bearer tok-123", "application/json"]);
  check("the row reads Set \u00b7 Undo", [tagOf(rowOf("c1")).textContent, part(rowOf("c1"), "challenge-set").hidden, part(rowOf("c1"), "challenge-undo").hidden], ["Set", true, false]);
  check("the due line is now the server's due_at (Fri 23 Oct, 10:15)", overlay.byData("challenge-due")[0].textContent, "Due when it closes, Fri 23 Oct, 10:15");

  /* ── Undo ────────────────────────────────────────────────────────── */
  console.log("\ntapping Undo");
  calls.length = 0;
  nextDelete = function () { return res(200, { ok: true }); };
  part(rowOf("c1"), "challenge-undo").click();
  await settle();
  check("DELETE /api/teacher/set-work/a1", calls.map(function (c) { return c.method + " " + c.url; }), ["DELETE https://api.test/api/teacher/set-work/a1"]);
  check("no body on the DELETE", calls[0].body, undefined);
  check("the row is back to Set", [part(rowOf("c1"), "challenge-set").hidden, part(rowOf("c1"), "challenge-undo").hidden, tagOf(rowOf("c1")).hidden], [false, true, true]);

  /* ── already_set ─────────────────────────────────────────────────── */
  console.log("\nan idempotent second set");
  nextPost = function () {
    return res(200, { assignments: [{ id: "a1", class_id: "c1", due_at: "2026-10-23T09:15:00.000Z", already_set: true }] });
  };
  part(rowOf("c1"), "challenge-set").click();
  await settle();
  check("reads Already set \u00b7 Undo", [tagOf(rowOf("c1")).textContent, part(rowOf("c1"), "challenge-undo").hidden], ["Already set", false]);

  /* ── errors, in plain words ──────────────────────────────────────── */
  console.log("\nerrors");
  nextPost = function () { return res(403, { error: "not_authorised_for_class" }); };
  part(rowOf("c4"), "challenge-set").click();
  await settle();
  check("403 -> Not your class, and Set stays", [tagOf(rowOf("c4")).textContent, part(rowOf("c4"), "challenge-set").hidden], ["Not your class", false]);
  nextPost = function () { return res(503, { error: "not_ready" }); };
  part(rowOf("c4"), "challenge-set").click();
  await settle();
  check("503 -> Not available yet", tagOf(rowOf("c4")).textContent, "Not available yet");
  nextPost = function () { return Promise.reject(new Error("offline")); };
  part(rowOf("c4"), "challenge-set").click();
  await settle();
  check("a dropped connection -> Couldn\u2019t set it", tagOf(rowOf("c4")).textContent, "Couldn\u2019t set it. Try again.");
  nextDelete = function () { return res(500, null); };
  part(rowOf("c1"), "challenge-undo").click();
  await settle();
  check("a failed Undo keeps the row set and says so", [tagOf(rowOf("c1")).textContent, part(rowOf("c1"), "challenge-undo").hidden], ["Couldn\u2019t undo. Try again.", false]);

  /* ── a disabled row is inert ─────────────────────────────────────── */
  calls.length = 0;
  check("a disabled row has no Set button to press", part(rowOf("c3"), "challenge-set").hidden, true);

  /* ── a bad subject opens nothing ─────────────────────────────────── */
  check("an unknown subject is refused", SW.openChallenge({ subject: "maths", client, classes }), false);

  console.log(failures ? `\n${failures} FAILED` : "\nall passed");
  process.exit(failures ? 1 : 0);
})().catch(function (e) { console.error(e); process.exit(2); });
