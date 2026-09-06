#!/usr/bin/env python3
"""verify_week_truth.py — one week, agreed on by every surface that names it.

    python3 verify_week_truth.py

⊕ MRB-330, 6 Sep 2026. Ruled by Mide: the teaching week rolls on SUNDAY 00:00 UK.

This gate exists because the product had TWO definitions of "this week" and
neither knew about the other. The backend composed and served work by one; the
teacher's week bar and the digest drew the other. On Sunday 6 September 2026
they disagreed by exactly one week, and the disagreement reached a child as
"LATE · 3 DAYS LATE" on the first thing she had ever opened (MRB-329 F1/F2/F6).

Fixing the arithmetic in three files does not stop it happening again — the
three implementations are still three. So this gate holds them against each
other, every day of a whole academic year, for every weekday a year could open
on. It fails if they EVER disagree.

The three, and where each is read from rather than retyped:
  · backend   assignment-compose.js  currentTeachingWeek()   — serves the work
  · frontend  teacher-live.js        teachingWeek()          — the week bar
  · frontend  teacher-data.js        computeWeekWindow()     — "this week"

The backend lives in a separate repo. If it is not on this machine the gate
SKIPS LOUDLY and exits 0 — a missing sibling repo is not a red gate, but it must
never look like a green one either.
"""
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

# The backend checkout to hold the frontend against. It defaults to the sibling
# repo, which is what a normal machine has; pass a path (or set MRB_BACKEND) to
# name a worktree instead. ⚠️ Point it at the backend that is actually DEPLOYED:
# holding the frontend against a feature branch nobody has shipped proves
# nothing about what a child is being served.
BACKEND_CANDIDATES = [
    p for p in [
        (sys.argv[1] if len(sys.argv) > 1 else None),
        os.environ.get("MRB_BACKEND"),
        os.path.join(HERE, "..", "mrbadmus---backend", "assignment-compose.js"),
    ] if p
]


def extract(path, name):
    """Lift one named function's source out of a file, brace-balanced."""
    src = open(path, encoding="utf-8").read()
    m = re.search(r"^[ \t]*function %s\s*\(" % re.escape(name), src, re.M)
    if not m:
        sys.exit("verify_week_truth: %s not found in %s" % (name, path))
    i = src.index("{", m.end() - 1)
    depth, j = 0, i
    while j < len(src):
        if src[j] == "{":
            depth += 1
        elif src[j] == "}":
            depth -= 1
            if depth == 0:
                break
        j += 1
    return src[m.start():j + 1]


def main():
    def resolve(p):
        p = os.path.normpath(p)
        if os.path.isdir(p):
            p = os.path.join(p, "assignment-compose.js")
        return p if os.path.exists(p) else None

    backend = next((r for r in (resolve(p) for p in BACKEND_CANDIDATES) if r), None)
    if backend is None:
        print("⚠️  SKIPPED — the backend repo is not on this machine, so the")
        print("   frontend's week could not be held against the backend's.")
        print("   Looked in:")
        for p in BACKEND_CANDIDATES:
            print("     " + os.path.normpath(p))
        return 0

    teaching_week = extract(os.path.join(HERE, "shared", "teacher-live.js"), "teachingWeek")
    week_window = extract(os.path.join(HERE, "shared", "teacher-data.js"), "computeWeekWindow")

    # `academicWeekOf` is what the week bar actually prints; it is rebuilt here
    # from the real `teachingWeek` above rather than copied, so a change to the
    # frontend rule reaches this gate whether or not anybody remembers it.
    driver = r"""
const { currentTeachingWeek } = require(%(backend)s);
%(teachingWeek)s
%(weekWindow)s

function academicWeekOf(now, year) {
  const startMon = teachingWeek(new Date(year.start_date + 'T00:00:00')).mon;
  const thisMon  = teachingWeek(new Date(now)).mon;
  return Math.floor((thisMon - startMon) / (7 * 86400000)) + 1;
}

const STARTS = ['2026-08-31','2026-09-01','2026-09-02','2026-09-03','2026-09-04','2026-09-06'];
const bad = [];
let checked = 0, sundays = 0;

for (const sd of STARTS) {
  const year = { start_date: sd, end_date: '2027-07-31' };
  for (let d = 0; d < 330; d++) {
    // Midday LOCAL on each day, so the comparison is about the DAY, not about
    // a clock-change hour. The rollover instant itself is proved in the
    // backend's own test_assignment_compose.js.
    const day = new Date(sd + 'T12:00:00');
    day.setDate(day.getDate() + d);
    const back = currentTeachingWeek(year, day);
    if (back === null) continue;             // past the 39-week ceiling
    const front = academicWeekOf(day, year);
    checked++;
    if (day.getDay() === 0) sundays++;
    if (back !== front) {
      bad.push({ start: sd, day: day.toDateString(), backend: back, frontend: front });
    }
  }
}

// The window that answers "this week" must contain the week bar's own Monday.
// A Monday-anchored class is the fallback and what every real class uses.
const windowBad = [];
for (let d = 0; d < 21; d++) {
  const now = new Date('2026-09-01T12:00:00');
  now.setDate(now.getDate() + d);
  const realNow = Date.now;
  Date.now = () => now.getTime();
  const OrigDate = Date;
  global.Date = class extends OrigDate {
    constructor(...a) { return a.length ? new OrigDate(...a) : new OrigDate(now); }
    static now() { return now.getTime(); }
  };
  const w = computeWeekWindow(null);
  const mon = teachingWeek(new Date(now)).mon;
  global.Date = OrigDate; Date.now = realNow;
  if (new OrigDate(w.start_at).getTime() !== mon.getTime()) {
    windowBad.push({ day: now.toDateString(), window: w.start_at, weekBar: mon.toISOString() });
  }
}

console.log(JSON.stringify({ checked, sundays, bad, windowBad }));
""" % {
        "backend": json.dumps(backend),
        "teachingWeek": teaching_week,
        "weekWindow": week_window,
    }

    try:
        out = subprocess.run(["node", "-e", driver], capture_output=True, text=True, timeout=120)
    except FileNotFoundError:
        print("⚠️  SKIPPED — node is not on PATH.")
        return 0
    if out.returncode != 0:
        print("verify_week_truth: the driver failed to run\n" + (out.stderr or "")[-2000:])
        return 1

    r = json.loads(out.stdout.strip().splitlines()[-1])
    print("verify_week_truth — one week, agreed on by every surface that names it")
    print("  backend read from : %s" % backend)
    print("  day-weeks compared: %d across %d year-start weekdays (%d of them Sundays)"
          % (r["checked"], 6, r["sundays"]))

    ok = True
    if r["bad"]:
        ok = False
        print("\n  ❌ the backend and the week bar disagree on %d day(s):" % len(r["bad"]))
        for b in r["bad"][:12]:
            print("       year opens %s · %s · backend week %s · week bar week %s"
                  % (b["start"], b["day"], b["backend"], b["frontend"]))
        if len(r["bad"]) > 12:
            print("       … and %d more" % (len(r["bad"]) - 12))
    else:
        print("  ✅ the backend's week and the teacher's week bar agree on every day")

    if r["windowBad"]:
        ok = False
        print("\n  ❌ \"this week\"'s window does not open on the week bar's Monday, %d day(s):"
              % len(r["windowBad"]))
        for b in r["windowBad"][:12]:
            print("       %s · window opens %s · week bar Monday %s"
                  % (b["day"], b["window"], b["weekBar"]))
    else:
        print("  ✅ \"this week\"'s window opens on the week bar's own Monday")

    print("\n%s" % ("✅ PASS" if ok else "❌ FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
