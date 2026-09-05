#!/usr/bin/env python3
"""teacher_perf_budget.py — MRB-325 ruling 4. How long a teacher waits.

    MRB_TEST_TEACHER_PASSWORD=… python3 teacher_perf_budget.py
    MRB_TEST_TEACHER_PASSWORD=… python3 teacher_perf_budget.py --budget 3000

⚑ WHY THIS EXISTS, AND WHY IT IS THE FIRST OF ITS KIND HERE.

Ruling 4 asks for a load-time budget across the four journeys a teacher
actually walks — the landing, a class, that class's marking screen, and one
student. Nothing in this repo measured a page's load time before this file: not
`teacher_behaviour` (text), not `student_parity` (pixels), not
`ks3_instrument_liveness` (does the button work). Every one of them asks
whether the page is CORRECT. None asks the only question a teacher asks at
08:40 with a class coming in: *is it up yet?*

A page can be perfectly correct and unusable. MRB-292 is the proof — the
student pages were green on every gate while taking four and a half seconds to
paint, because the reads went out in serial waves and nothing counted the
waves. That was found by hand, by Mide, on a Friday. This counts them.

── WHAT IS MEASURED ─────────────────────────────────────────────────────

Wall clock from `Page.navigate` to the moment the page's OWN content is on
screen — not `load`, not `DOMContentLoaded`, both of which fire while the
teacher is still looking at nothing. Every one of these four pages hides its
content until its data has arrived, and each does it differently, so the ready
signal is read from the page rather than assumed:

    teacher/today.html          hand-written: `body` AND `#main` both set to
                                display:block, and `#lessons` actually filled.
                                ⚠️ `body` alone is NOT the signal — `onAllowed`
                                reveals the body FIRST and then awaits
                                loadTimetable(), so a body check would stop the
                                clock before a single lesson had been read.
    the three ported screens    the runtime has drawn its own region
                                (`[data-port-region="class"|"marking"|
                                "student"]`) into `#mrb-teacher`, and the boot
                                wrapper (`[data-mrb-state]`, which carries the
                                skeleton) is gone. The runtime draws in one
                                pass — `host.textContent = ""` then rebuild —
                                so the region appearing IS the mount finishing.

A refusal panel (`data-mrb-state="unavailable"`, or Today's `#notice`) is
detected and reported as a FAILED journey, never as a fast one. A page that
gives up quickly is the cheapest way to pass a timing gate and it must not.

── THE NUMBER, AND WHY IT IS THIS NUMBER ────────────────────────────────

2500 ms, warm, per journey.

There was no existing budget in this codebase to copy — no page, student or
teacher, has ever had one — so it is chosen against what this gate actually
measures rather than asserted from taste. The first full runs on 5 Sep 2026
(TEST project, warm cache, one warm-up load discarded, median of three)
produced:

    landing · teacher/today.html                    127 / 128 ms
    Today → class detail                            286 / 347 ms
    class detail → marking                          235 / 182 ms
    class detail → student                          331 / 284 ms

⚠️ IT IS DELIBERATELY NOT 1.5× THE WORST OF THOSE. 1.5× would be about 520 ms,
   and a ceiling that tight would be red on the first bad minute of Wi-Fi and
   red for good the first time a THIRTY-student class is loaded instead of a
   six-student fixture. It would be measuring the fixture and the office
   broadband, not the product.

2500 ms is where a teacher perceives waiting — the thing ruling 4 is actually
about — and it sits roughly 7× above the worst warm median measured here.
That headroom is what makes it a gate rather than a coin toss:

  1. THE TEST FIXTURES ARE TINY. The biggest class on TEST has six students and
     the only class carrying an assignment has one. `loadClassMatrices` fans
     out over the roster and the submissions, so these medians are a FLOOR, not
     a forecast.
  2. IT IS A REAL NETWORK, warm. Genuine round trips to Supabase eu-west-1 on a
     browser that already holds the connection. A colder machine, a worse line
     or a busier project all cost real milliseconds that are nobody's
     regression.
  3. IT STILL CATCHES THE DEFECT IT EXISTS FOR. MRB-292's serial-wave load was
     four and a half seconds; an N+1 put back into `base()`, or one more
     awaited wave on the class screen, lands in seconds and not in hundreds of
     milliseconds. That is the size of regression this can see, and it is the
     size that has actually happened here.
  4. A CEILING, NOT A TARGET. A median of 2 s would be green and would still be
     something wrong. The PRINTED MEDIANS are what a human reads for that; the
     verdict only says whether a teacher is now visibly waiting.

⚠️ AND ONE HONEST WEAKNESS, recorded rather than papered over: the TEST project
   holds NO `timetable_entries` rows for either fixture teacher, so the landing
   journey traverses `today.html`'s no-timetable branch — one read, then the
   "It needs your timetable first" prompt — and never reaches the per-class
   reads that a teacher with a real timetable pays for. Its 128 ms is a true
   measurement of the wrong day. Seeding a timetable on TEST would fix it and
   is a write to a shared project, so it is left as a finding.

⚠️ NO RENDER IN THE PATH. It is worth saying plainly because the obvious
   assumption is wrong: the teacher screens talk to Supabase DIRECTLY and never
   touch the Render backend, so nothing here can be blamed on — or hidden by —
   a Render cold start. What this budget covers is auth plus the Supabase read
   waves plus the mount, which is the whole of what a teacher waits for.

── MEDIAN, NOT MEAN, AND NOT MIN ────────────────────────────────────────

Three timed runs per journey after one discarded warm-up. The median is the
honest middle: a mean lets one 6-second outlier fail a healthy page, and a min
is how a slow page passes — take enough runs and something will be fast once.
The warm-up is discarded because the first load of the session pays for the
supabase-js CDN bundle and a cold DNS lookup, which a teacher on their second
page of the morning does not.

── CREDENTIALS ──────────────────────────────────────────────────────────

Signs in as the real TEST fixtures `hz_amy` and `hz_rich` (MRB-293 set their
passwords by SQL; fake accounts on a sandbox project, no production
credential). The password is read from $MRB_TEST_TEACHER_PASSWORD and there is
NO literal fallback, so `prepush_gate.py` reports this gate SKIPPED BY NAME on
a machine that has not opted in.

⚠️ THAT IS NOT SECRECY — the same string is committed in
  `teacher_landing_drive.py` and `admin_view_drive.py`. It is the registry's
  own switch for "this gate goes over the network", and it is why this file
  earns a row in GATES where those two are EXCLUDED outright: a load-time
  ceiling has to be named in the list and re-measurable on demand, but a push
  must never depend on Supabase TEST being reachable.

⚠️ TWO TEACHERS, ON PURPOSE, and it is a property of the fixtures rather than
  a preference. `hz_amy` holds the largest roster on TEST (six students) and
  `hz_rich` holds the ONLY class with an assignment on it — so the marking
  journey is driven as Rich and the other three as Amy, because a marking
  screen with no paper on it measures an empty state rather than a load.
"""

import json
import os
import re
import ssl
import statistics
import sys
import time
import urllib.request

REPO = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, REPO)
os.chdir(REPO)

import ks3_browser as cdp

REF = "qeppkiswvclkkwbxmlok"
URL = "https://%s.supabase.co" % REF
PORT = 5509
CTX = ssl.create_default_context(cafile="/etc/ssl/cert.pem")

BUDGET_MS = 2500          # see the docstring; --budget overrides for a probe
RUNS = 3                  # timed loads per journey, median taken
WARMUPS = 1               # discarded loads per journey, before the timed ones
TIMEOUT_S = 30.0          # a journey that has not painted by here has failed
POLL_S = 0.05

# The TEST fixtures. Real accounts, real RLS, real round trips.
AMY = "hz_amy@test.mrbadmus"
RICH = "hz_rich@test.mrbadmus"

CLASS_AMY = "ee000000-0000-0000-0000-000000000401"   # HZ 10A Science — 6 students
CLASS_RICH = "ee000000-0000-0000-0000-000000000402"  # HZ 10B Physics — 1 assignment
STUDENT_AMY = "29000000-0000-0000-0000-000000000002"  # Lily Edwards, in 10A


# ── the ready signals, read from the pages themselves ────────────────────

def ported_ready(region, expect):
    """Has the runtime drawn `region` into #mrb-teacher, WITH real content?

    ⚠️ `expect` is not decoration. Without it the clock stops the instant the
    region element exists, and the cheapest way for a slow screen to pass a
    timing gate is to render its empty state fast. `expect` is a string only
    the real fixture data can produce — a student's name, an assignment's
    title — so the stopwatch cannot stop on a shell.
    """
    return r"""(function () {
      var host = document.getElementById('mrb-teacher');
      if (!host) { return JSON.stringify({ready:false, refused:false, why:'no host yet'}); }
      var st = host.querySelector('[data-mrb-state]');
      if (st && st.getAttribute('data-mrb-state') === 'unavailable') {
        return JSON.stringify({ready:false, refused:true,
                               why:(st.innerText||'').replace(/\s+/g,' ').trim()});
      }
      var r = host.querySelector('[data-port-region=%s]');
      if (!r) { return JSON.stringify({ready:false, refused:false, why:'region not drawn'}); }
      if (st) { return JSON.stringify({ready:false, refused:false, why:'still booting'}); }
      var txt = (r.innerText || '').replace(/\s+/g, ' ');
      if (txt.indexOf(%s) < 0) {
        return JSON.stringify({ready:false, refused:false,
                               why:'drawn, but %s is not on it yet'});
      }
      return JSON.stringify({ready:true, refused:false, why:txt.slice(0, 70)});
    })()""" % (json.dumps(region), json.dumps(expect), expect.replace("'", ""))


# ⚠️ `.skel-row` IS SHIPPED IN THE STATIC HTML. `#lessons` opens with three
# skeleton rows baked into the file, so `children.length > 0` is true before a
# single request has been made — the first version of this check read exactly
# that and would have stopped the clock at the first paint. The skeletons are
# replaced wholesale (`innerHTML = …`) once the timetable read returns, so
# their ABSENCE is what says the data arrived.
TODAY_READY = r"""(function () {
  var notice = document.getElementById('notice');
  if (notice && notice.style.display === 'block') {
    return JSON.stringify({ready:false, refused:true,
      why:((document.getElementById('notice-title')||{}).textContent||'').trim()});
  }
  var main = document.getElementById('main');
  var lessons = document.getElementById('lessons');
  var skel = lessons ? lessons.querySelectorAll('.skel-row, .skel').length : 1;
  var ok = document.body.style.display === 'block'
        && main && main.style.display === 'block'
        && lessons && lessons.children.length > 0 && skel === 0;
  return JSON.stringify({ready:!!ok, refused:false,
    why: ok ? (lessons.innerText||'').replace(/\s+/g,' ').slice(0, 70)
            : 'body=' + document.body.style.display +
              ' main=' + (main ? main.style.display : '-') +
              ' skeletons=' + skel});
})()"""


JOURNEYS = [
    dict(name="landing · teacher/today.html",
         who=AMY,
         url="/teacher/today.html?env=test",
         ready=TODAY_READY),
    dict(name="Today → class detail",
         who=AMY,
         url="/teacher/class-detail.html?env=test&class=" + CLASS_AMY,
         ready=ported_ready("class", "Lily Edwards")),
    dict(name="class detail → marking",
         who=RICH,
         url="/teacher/assignment.html?env=test&class=" + CLASS_RICH,
         ready=ported_ready("marking", "HZ Physics HW")),
    dict(name="class detail → student",
         who=AMY,
         url=("/teacher/student-detail.html?env=test&class=" + CLASS_AMY +
              "&student=" + STUDENT_AMY),
         ready=ported_ready("student", "Lily Edwards")),
]


# ── sign-in, exactly the wire format teacher_landing_drive uses ──────────

def anon_key():
    src = open("shared/config.js", encoding="utf-8").read()
    return re.search(r"'(eyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+)'",
                     src[src.index("const TEST"):]).group(1)


def password():
    pw = os.environ.get("MRB_TEST_TEACHER_PASSWORD")
    if not pw:
        raise SystemExit(
            "teacher_perf_budget: $MRB_TEST_TEACHER_PASSWORD is not set, so "
            "this gate cannot sign in and would measure nothing. It is the "
            "MRB-293 TEST fixture password — see the module docstring.")
    return pw


def sign_in(email, key):
    req = urllib.request.Request(
        URL + "/auth/v1/token?grant_type=password",
        data=json.dumps({"email": email, "password": password()}).encode(),
        headers={"apikey": key, "Content-Type": "application/json"},
        method="POST")
    with urllib.request.urlopen(req, timeout=60, context=CTX) as r:
        return json.loads(r.read().decode())


def put_session(page, base, key, sess):
    """Same-origin sign-in, so the teacher pages find a real stored session."""
    page.goto(base + "/leaderboard.html?env=test", settle=2.0)
    return page.eval("""
      (async function () {
        var c = window.supabase.createClient(%s, %s);
        var r = await c.auth.setSession({access_token: %s, refresh_token: %s});
        return r.error ? 'error: ' + r.error.message : 'ok';
      })()
    """ % (json.dumps(URL), json.dumps(key),
           json.dumps(sess["access_token"]), json.dumps(sess["refresh_token"])))


# ── one measured load ────────────────────────────────────────────────────

def timed_load(page, url, ready_js):
    """Navigate and stopwatch until the page's own content is on screen.

    Returns (milliseconds, note). `milliseconds` is None when the page never
    got there — refused, or still not painted at TIMEOUT_S.
    """
    # A clean slate every time: this must be a real navigation, never a state
    # change on a page that is already mounted.
    page.goto("about:blank", settle=0.05)

    t0 = time.monotonic()
    page.send("Page.navigate", {"url": url})
    deadline = t0 + TIMEOUT_S
    last = "no answer yet"
    while time.monotonic() < deadline:
        try:
            got = json.loads(page.eval(ready_js) or "{}")
        except Exception as err:                        # noqa: BLE001
            last = "harness: %s" % str(err)[:60]
            time.sleep(POLL_S)
            continue
        if got.get("refused"):
            return None, "REFUSED — %s" % (got.get("why") or "")[:70]
        if got.get("ready"):
            return (time.monotonic() - t0) * 1000.0, (got.get("why") or "")
        last = got.get("why") or last
        time.sleep(POLL_S)
    return None, "never painted in %.0fs — last state: %s" % (TIMEOUT_S, last)


def main():
    budget = BUDGET_MS
    argv = sys.argv[1:]
    if argv:
        if argv[0] == "--budget" and len(argv) == 2:
            budget = float(argv[1])
        else:
            raise SystemExit("usage: teacher_perf_budget.py [--budget MS]")

    key = anon_key()
    print("\n⏱   MRB-325 ruling 4 — the four teacher journeys, timed\n")
    print("     budget %.0f ms, median of %d timed load(s) after %d warm-up\n"
          % (budget, RUNS, WARMUPS))

    server, port = cdp.serve("mrbadmus_site", port=PORT)
    base = "http://localhost:%d" % port
    rows, fails = [], []

    try:
        with cdp.Browser() as b:
            page = b.attach()
            page.set_viewport(1280, 1000)
            signed_as = None

            for j in JOURNEYS:
                if signed_as != j["who"]:
                    sess = sign_in(j["who"], key)
                    got = put_session(page, base, key, sess)
                    if got != "ok":
                        fails.append("%s: could not sign in as %s (%s)"
                                     % (j["name"], j["who"], got))
                        print("  ❌ %-34s could not sign in — %s"
                              % (j["name"][:34], got))
                        continue
                    signed_as = j["who"]

                for _ in range(WARMUPS):
                    timed_load(page, base + j["url"], j["ready"])

                samples, note = [], ""
                for _ in range(RUNS):
                    ms, why = timed_load(page, base + j["url"], j["ready"])
                    if ms is None:
                        note = why
                        break
                    samples.append(ms)
                    note = why

                if len(samples) < RUNS:
                    fails.append("%s: %s" % (j["name"], note))
                    print("  ❌ %-34s   %s" % (j["name"][:34], note))
                    rows.append((j["name"], None))
                    continue

                med = statistics.median(samples)
                ok = med <= budget
                if not ok:
                    fails.append("%s: median %.0f ms over the %.0f ms budget"
                                 % (j["name"], med, budget))
                print("  %s %-34s median %6.0f ms   budget %.0f ms   "
                      "(runs %s)"
                      % ("✅" if ok else "❌", j["name"][:34], med, budget,
                         ", ".join("%.0f" % s for s in samples)))
                print("       as %-22s %s" % (j["who"], note[:60]))
                rows.append((j["name"], med))
    finally:
        server.shutdown()

    print("\n" + "─" * 68)
    for name, med in rows:
        print("     %-38s %s" % (name,
                                 ("%.0f ms" % med) if med is not None
                                 else "did not paint"))
    print("─" * 68)
    if fails:
        print("❌ teacher_perf_budget: %d journey/journeys over budget or "
              "unreachable" % len(fails))
        for f in fails:
            print("   · " + f)
        return 1
    print("✅ teacher_perf_budget: all %d journeys inside the %.0f ms warm-load "
          "budget" % (len(JOURNEYS), budget))
    return 0


if __name__ == "__main__":
    sys.exit(main())
