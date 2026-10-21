/* teacher_challenge_cards_test.js — Unit C: `buildChallenges` in
 * shared/teacher-live.js, and the week bucketing the class page's card uses.
 *
 *   node tools/teacher_challenge_cards_test.js
 *
 * Loads the REAL file, like week_scope_check.js. Pins: a challenge set this
 * week sits in the current week's chip and no other; one set last week sits in
 * last week's; the deadline reads "Fri 23 Oct"; and a pack whose only work is a
 * challenge has NO papers (so no grid column, no digest figure, no "not in").
 *
 * Not a registered gate (lives in tools/); run by hand, recorded in the run
 * report.
 */
"use strict";
process.env.TZ = "Europe/London";
const path = require("path");
global.window = { MRB_TEACHER_LIVE_NO_AUTORUN: true };
require(path.join(__dirname, "..", "shared", "teacher-live.js"));
const TL = global.window.MrBadmusTeacherLive;
if (!TL || !TL.buildChallenges) { console.log("FAIL buildChallenges is not exposed"); process.exit(1); }

let fails = 0;
function check(name, got, want) {
  const ok = JSON.stringify(got) === JSON.stringify(want);
  if (!ok) { fails += 1; }
  console.log(`${ok ? "  ok  " : "  FAIL"}  ${name}${ok ? "" : `\n           got  ${JSON.stringify(got)}\n           want ${JSON.stringify(want)}`}`);
}

const YEAR = { start_date: "2026-09-01", end_date: "2027-08-31" };
const NOW = new Date(2026, 9, 21, 12, 0, 0);            // Wed 21 Oct 2026, London
const weeks = TL.buildWeeks(YEAR, NOW);
const pack = {
  members: [], assignments: [],
  challenges: [
    { id: "c-now", title: "Weekly challenge: Physics", due_at: "2026-10-23T09:15:00Z",
      release_at: "2026-10-21T10:00:00Z", academic_week: 8 },
    { id: "c-prev", title: "Weekly challenge: Biology", due_at: "2026-10-16T09:15:00Z",
      release_at: "2026-10-12T10:00:00Z", academic_week: 6 }
  ]
};

console.log("a pack whose only work is a challenge has no papers");
check("buildPapers -> []", TL.buildPapers(pack, NOW).length, 0);

console.log("\nbuildChallenges");
const list = TL.buildChallenges(pack, weeks, YEAR, NOW);
check("both come back, titled as set", list.map(function (c) { return c.title; }),
  ["Weekly challenge: Physics", "Weekly challenge: Biology"]);
check("the deadline reads like the rest of the page", list[0].due, "Fri 23 Oct");
check("no count of who has played is invented", Object.keys(list[0]).sort(), ["due", "dueAt", "id", "title", "weekIdx"]);

console.log("\nthe week bucket (catchUpsForWeek, the week bar's rule)");
const cur = TL.catchUpsForWeek(list, weeks, 0).map(function (c) { return c.id; });
check("this week's chip holds this week's challenge", cur.indexOf("c-now") > -1, true);
check("and not last week's", cur.indexOf("c-prev") > -1, false);
const prevIdx = list[1].weekIdx;
check("last week's lands on a later (older) chip", prevIdx > 0, true);
check("and shows there", TL.catchUpsForWeek(list, weeks, prevIdx).map(function (c) { return c.id; }).indexOf("c-prev") > -1, true);

console.log("\nno challenges -> nothing");
check("empty pack", TL.buildChallenges({ members: [], assignments: [] }, weeks, YEAR, NOW), []);

console.log(fails ? `\n${fails} FAILED` : "\nall passed");
process.exit(fails ? 1 : 0);
