/* admin_class_tier_test.js — the shape teacher/admin.html reads a saved
 * class tier back out of.
 *
 *   node tools/admin_class_tier_test.js
 *
 * MRB-335 item 7. `POST /api/admin/class-tier` answers
 *
 *     { ok: true,
 *       class: { id, name, tier, pathway, subject, tier_pathway_source },
 *       previous, rule }
 *
 * and the page read `body.tier` / `body.pathway` / `body.subject` — all
 * `undefined`, on the SUCCESS path only. So both selectors blanked at the
 * moment the write worked: the value was in the database and gone from the
 * screen, which reads as "it did not take" and invites a second save.
 *
 * ⚠️ IT DRIVES THE BUILT PAGE'S OWN SOURCE, not a copy of the expression.
 * The reader is lifted out of `mrbadmus_site/teacher/admin.html` by its
 * anchors and evaluated; retyping it here would test this file against
 * itself, which is the drift a copy exists to hide.
 *
 * ⚠️ NOT A REGISTERED GATE. `gate_registry.py`'s `coverage()` scans the repo
 * ROOT for `.py`/`.sh`; this is neither and lives in `tools/`. Run by hand,
 * result recorded in the run report — the same standing as
 * `set_work_time_test.js` beside it.
 */
"use strict";

const fs = require("fs");
const path = require("path");
const vm = require("vm");

const PAGE = path.join(__dirname, "..", "mrbadmus_site", "teacher", "admin.html");
if (!fs.existsSync(PAGE)) {
  console.error("admin_class_tier_test: no built page at " + PAGE +
                " — run `python3 build_all.py` first");
  process.exit(2);
}
const html = fs.readFileSync(PAGE, "utf8");

/* The two fragments this asserts on, by anchor. A rename that loses either is
 * a failure rather than a silent skip: a test that quietly stops testing is
 * the thing the gate registry exists to prevent. */
function lift(startMark, endMark, label) {
  const i = html.indexOf(startMark);
  if (i < 0) { fail("could not find " + label + " in the built page"); }
  const j = html.indexOf(endMark, i);
  if (j < 0) { fail("could not find the end of " + label); }
  return html.slice(i, j + endMark.length);
}

let failures = 0;
function fail(msg) { console.error("  FAIL  " + msg); failures += 1; }
function check(label, got, want) {
  const ok = JSON.stringify(got) === JSON.stringify(want);
  if (!ok) { failures += 1; }
  console.log(`${ok ? "  ok  " : "  FAIL"}  ${label}` +
    (ok ? "" : `\n           got  ${JSON.stringify(got)}\n           want ${JSON.stringify(want)}`));
}

const reader = lift("var got = (body", "subject: got.subject || '',\n    };",
                    "the response reader");
const pathValue = lift("function pathValue(tp)", "\n}", "pathValue");

const sandbox = { console };
vm.createContext(sandbox);
vm.runInContext(pathValue, sandbox);
vm.runInContext("function read(body){ " + reader + " return next; }", sandbox);

/* ── the shape the route actually returns (server.js, the class-tier
 *    handler's `res.json`) ───────────────────────────────────────────────── */
const ROUTE = {
  ok: true,
  class: { id: "c1", name: "10a/Bi1", tier: "higher", pathway: "triple",
           subject: "biology", tier_pathway_source: "admin" },
  previous: { tier: null, pathway: null, subject: null },
  rule: { tier: "higher", pathway: "triple", subject: "biology" },
};
check("reads tier/pathway/subject out of `class`", sandbox.read(ROUTE),
      { tier: "higher", pathway: "triple", subject: "biology" });
check("…and the pathway selector value is the joined pair",
      sandbox.pathValue(sandbox.read(ROUTE)), "triple:biology");

/* Combined: a real pathway and NO subject. The selector must not invent one. */
const COMBINED = { ok: true, class: { id: "c2", name: "10b/Sc5",
  tier: "foundation", pathway: "combined", subject: null } };
check("combined keeps an empty subject", sandbox.read(COMBINED),
      { tier: "foundation", pathway: "combined", subject: "" });
check("…and selects plain `combined`",
      sandbox.pathValue(sandbox.read(COMBINED)), "combined");

/* A class the rule could not read: every field null, both selectors empty. */
const NULLED = { ok: true, class: { id: "c3", name: "10X/Zz9",
  tier: null, pathway: null, subject: null } };
check("all-null renders as two empty selectors", sandbox.read(NULLED),
      { tier: "", pathway: "", subject: "" });
check("…and pathValue stays empty", sandbox.pathValue(sandbox.read(NULLED)), "");

/* ⚠️ THE FLAT SHAPE IS ACCEPTED TOO, and that is deliberate rather than
 * defensive clutter: this page and that route deploy separately (Cloudflare
 * and Render), so for the length of one deploy window a browser can hold one
 * version of the page and talk to the other version of the route. Reading
 * `(body.class || body)` costs one expression and removes an ordering
 * constraint from the merge. */
const FLAT = { ok: true, tier: "higher", pathway: "triple", subject: "physics" };
check("a flat body still reads", sandbox.read(FLAT),
      { tier: "higher", pathway: "triple", subject: "physics" });
check("…and still joins", sandbox.pathValue(sandbox.read(FLAT)), "triple:physics");

/* The regression itself, stated as an assertion rather than as a comment:
 * reading the top level of the REAL payload yields nothing. */
check("the old top-level read would have blanked both",
      [ROUTE.tier, ROUTE.pathway, ROUTE.subject],
      [undefined, undefined, undefined]);

console.log(failures ? `\n${failures} FAILED` : "\nall checks passed");
process.exit(failures ? 1 : 0);
