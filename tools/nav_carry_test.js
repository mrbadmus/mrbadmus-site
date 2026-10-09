/* nav_carry_test.js — shared/nav.js carries ?env=&api= across every
 * same-origin link (the TEST world survives a click), and on the live site
 * (neither parameter) touches nothing.
 *
 *   node tools/nav_carry_test.js
 *
 * ⊕ B2C polish round 3 (9 Oct 2026): on / with ?env=test&api=… the KS3 and
 * GCSE cards, "Take the challenge", the footer and the class-entry "Today"
 * link all pointed at bare paths. Loads the REAL shared/nav.js in a vm with a
 * stub document; carry() is exposed only on window.MRB_NAV_TEST_HOOK.
 * Not a registered gate (see tools/set_work_time_test.js); run by hand.
 */
"use strict";
const fs = require("fs");
const path = require("path");
const vm = require("vm");

const SRC = fs.readFileSync(path.join(__dirname, "..", "shared", "nav.js"), "utf8");
const ORIGIN = "http://localhost:48442";

function load(search) {
  const listeners = [];
  let observers = 0;
  const win = {
    MRB_NAV_TEST_HOOK: {}, MrBadmusConfig: {},
    location: { search, href: ORIGIN + "/index.html" + search, origin: ORIGIN, pathname: "/index.html" },
  };
  const sandbox = {
    window: win, URL, URLSearchParams, console,
    document: { readyState: "loading", documentElement: {},
      addEventListener: (type) => listeners.push(type) },
    MutationObserver: class { constructor() { observers += 1; } observe() {} },
  };
  vm.createContext(sandbox);
  vm.runInContext(SRC, sandbox, { filename: "shared/nav.js" });
  return { carry: win.MRB_NAV_TEST_HOOK.carry, listeners, observers: () => observers };
}

let failures = 0;
function check(name, got, want) {
  const ok = got === want;
  if (!ok) failures += 1;
  console.log(`${ok ? "  ok  " : "  FAIL"}  ${name}${ok ? "" : `\n           got  ${got}\n           want ${want}`}`);
}

const API = "http://localhost:48441";
const T = load("?env=test&api=" + encodeURIComponent(API));
const Q = "env=test&api=" + encodeURIComponent(API);
const c = T.carry;

// The links the blind run found bare on /.
check("KS3 card", c("/ks3/index.html"), "/ks3/index.html?" + Q);
check("GCSE card / Combined chip", c("/ks4.html"), "/ks4.html?" + Q);
check("class-entry Today", c("/consumer/today.html"), "/consumer/today.html?" + Q);
check("Take the challenge", c("/weekly-challenge.html"), "/weekly-challenge.html?" + Q);
check("footer Leaderboard", c("/leaderboard.html"), "/leaderboard.html?" + Q);
check("Past papers", c("/past-papers.html"), "/past-papers.html?" + Q);
check("3D Studio", c("/3d/"), "/3d/?" + Q);
check("brand home", c("/"), "/?" + Q);
// The link's own query and hash survive; a key it sets itself wins.
check("own query and hash kept", c("/auth.html?tab=signin#top"), "/auth.html?tab=signin&" + Q + "#top");
check("a key the link sets is not overwritten", c("/x.html?env=prod"), "/x.html?env=prod&api=" + encodeURIComponent(API));
check("already carried: unchanged, byte for byte", c("/x.html?env=test&api=" + API), "/x.html?env=test&api=" + API);
check("carrying twice is carrying once", c(c("/ks4.html")), c("/ks4.html"));
// Page-relative and same-origin absolute links are the same journey.
check("page-relative link", c("ks4.html"), "/ks4.html?" + Q);
check("query-only link", c("?tab=signup"), "/index.html?tab=signup&" + Q);
check("same-origin absolute link", c(ORIGIN + "/ks4.html"), "/ks4.html?" + Q);
// Everything else is left exactly as written.
check("same-page hash", c("#k4-challenge"), "#k4-challenge");
check("protocol-relative", c("//example.com/x"), "//example.com/x");
check("another origin", c("https://www.aqa.org.uk/x.pdf"), "https://www.aqa.org.uk/x.pdf");
check("mailto:", c("mailto:help@example.com"), "mailto:help@example.com");
check("javascript:", c("javascript:void(0)"), "javascript:void(0)");
check("empty href", c(""), "");
check("TEST page wires click + auxclick + contextmenu", T.listeners.filter(t => t !== "DOMContentLoaded").sort().join(","),
      "auxclick,click,contextmenu");
check("TEST page watches for links drawn later", T.observers(), 1);

// Production: neither parameter on the URL, so nothing changes and nothing is wired.
const P = load("");
check("production: href untouched", P.carry("/ks4.html"), "/ks4.html");
check("production: page-relative untouched", P.carry("ks4.html"), "ks4.html");
check("production: no click handlers", P.listeners.filter(t => t !== "DOMContentLoaded").length, 0);
check("production: no observer", P.observers(), 0);
const O = load("?tab=signin");
check("unrelated query only: untouched", O.carry("/ks4.html"), "/ks4.html");

console.log(failures ? `\n${failures} FAILED` : "\nall passed");
process.exit(failures ? 1 : 0);
