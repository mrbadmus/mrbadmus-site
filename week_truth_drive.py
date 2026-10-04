#!/usr/bin/env python3
"""week_truth_drive.py — SPEC-A's own proof requirement: walk every week of
both real-shaped classes on TEST, at fixed clocks, and write down what each
card shows.

    MRB_WEEK_TRUTH_PASSWORD=<pw> python3 week_truth_drive.py

Builds the throwaway world (`week_truth_fixture.py`), freezes Chrome's clock
with `Emulation.setFixedTime` at each of SPEC-A's four instants, signs in as
the throwaway teacher through the real `auth.html` form, opens the GENERATED
`teacher/class-detail.html` against TEST, and clicks every chip on the week
bar — reading `window.__MRB_CMP__.logic.renderVals()` directly rather than
scraping rendered text, because that object IS the exact computed `glance`/
`roster`/`cards` the page is about to paint, with every number named rather
than embedded in a sentence this script would have to re-parse.

This is NOT a gate — it has no pass/fail assertions of its own; it is the
proof artefact SPEC-A's "Deliver" section asks RESULT-A.md to be built from.
`week_scope_check.py` (the registered fast gate) is what a future change is
held against; this is one session's evidence that the live defect is fixed
on real TEST data, at the real clock it was found on.

Tears down by the snapshotted id list `week_truth_fixture.py` itself writes
and reads — never a predicate.
"""
import json
import os
import sys
import time

REPO = os.path.dirname(os.path.abspath(__file__))
os.chdir(REPO)
sys.path.insert(0, REPO)

import week_truth_fixture as FX2   # noqa: E402
import ks3_browser as cdp          # noqa: E402

SITE_PORT = 5544

# The Sun 4 Oct clock was already walked and recorded in RESULT-A.md in an
# earlier pass of this same session; these three remaining ones are what
# this run is for. Re-add the Sun entry here if a from-scratch run is ever
# wanted again.
CLOCKS = [
    # (label, y, mo, d, h, mi) — Europe/London wall-clock, BST throughout.
    ("Wed 30 Sep 2026 12:00 BST", 2026, 9, 30, 12, 0),
    ("Mon 5 Oct 2026 12:00 BST (Temperature still open)", 2026, 10, 5, 12, 0),
    ("Tue 6 Oct 2026 12:00 BST", 2026, 10, 6, 12, 0),
]


def anon_key():
    src = open("shared/config.js", encoding="utf-8").read()
    import re
    return re.search(r"'(eyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+)'",
                     src[src.index("const TEST"):]).group(1)


def sign_in(email, pw):
    import ssl
    import urllib.request
    key = anon_key()
    req = urllib.request.Request(
        "https://qeppkiswvclkkwbxmlok.supabase.co/auth/v1/token?grant_type=password",
        method="POST", headers={"apikey": key, "Content-Type": "application/json"},
        data=json.dumps({"email": email, "password": pw}).encode())
    ctx = ssl.create_default_context(cafile="/etc/ssl/cert.pem")
    with urllib.request.urlopen(req, context=ctx, timeout=30) as r:
        return json.loads(r.read().decode())


CLICK_SIGN_IN_JS = """
(function () {
  var e = document.getElementById('signin-email');
  var p = document.getElementById('signin-password');
  var b = document.getElementById('btn-signin');
  if (!e || !p || !b) { return 'no sign-in form'; }
  e.value = %s; p.value = %s;
  b.click();
  return 'clicked';
})()
"""
TOKEN_JS = ("(Object.keys(localStorage).filter(function(k){"
            "return k.indexOf('-auth-token') > -1;})[0] || '')")


FREEZE_JS = """
(function () {
  var FIXED = %r;
  var Orig = Date;
  function Fake(...args) {
    return args.length === 0 ? new Orig(FIXED) : new Orig(...args);
  }
  Fake.now = function () { return FIXED; };
  Fake.prototype = Orig.prototype;
  Object.setPrototypeOf(Fake, Orig);
  window.Date = Fake;
})();
"""


def freeze_clock(page, epoch_ms):
    """Chrome here has no `Emulation.setFixedTime` ('wasn't found', -32601 —
    an older Chrome than the CDP docs assume). Overriding `window.Date`
    before any page script runs is the same effect from the other side:
    every `Date.now()`/`new Date()` on the page reads the frozen instant.
    `Page.addScriptToEvaluateOnNewDocument` re-applies it on EVERY
    navigation this target makes from here on, auth.html included."""
    page.send("Page.enable")
    # `teachingWeek()` and friends read the DEVICE's local calendar day/hour
    # off whatever `new Date(iso)` gives them (an explicit-args Date still
    # constructs a REAL Date, carrying the OS timezone) — so the machine
    # this runs on has to be told it is in the UK too, not only told what
    # instant it is. `Emulation.setTimezoneOverride` IS supported here
    # (unlike `setFixedTime` above it).
    page.send("Emulation.setTimezoneOverride", {"timezoneId": "Europe/London"})
    page.send("Page.addScriptToEvaluateOnNewDocument",
               {"source": FREEZE_JS % epoch_ms})


def goto_ready(p, url, ready, settle=2.0, tries=4):
    for _ in range(tries):
        try:
            p.goto(url, settle=settle)
        except Exception:
            time.sleep(1.0)
            continue
        for _ in range(60):
            try:
                if p.eval(ready):
                    return True
            except Exception:
                pass
            time.sleep(0.3)
    return False


def sign_in_page(p, base, email, pw):
    if not goto_ready(p, "%s/auth.html?env=test" % base,
                      "!!document.getElementById('btn-signin')"):
        return "auth.html never rendered its sign-in form"
    try:
        clicked = p.eval(CLICK_SIGN_IN_JS % (json.dumps(email), json.dumps(pw)))
    except Exception as e:
        return "could not press Sign In: %s" % e
    if clicked != "clicked":
        return str(clicked)
    for _ in range(80):
        time.sleep(0.3)
        try:
            key = p.eval(TOKEN_JS)
        except Exception:
            continue
        if key:
            return "ok"
    return "no session in localStorage"


RENDER_JS = """
(async function () {
  var el = document.querySelector('[data-week="%d"]');
  if (!el) { return {error: 'no chip for wi=%d'}; }
  el.click();
  await new Promise(function (r) {
    requestAnimationFrame(function () { requestAnimationFrame(r); });
  });
  var L = window.__MRB_CMP__ && window.__MRB_CMP__.logic;
  if (!L || !L.renderVals) { return {error: 'no logic.renderVals()'}; }
  var v = L.renderVals();
  // `kWeeks`/`wScope`/`lastP` are LOCALS inside `renderVals`, not keys of
  // what it returns — re-derive the same facts from the page's own globals
  // (`MRB_PICK`, `MRB_WEEK_SCOPE`) for the walk's own record, rather than
  // guessing at them from the rendered props alone.
  var cid = '%s';
  var weeks = MRB_PICK('WEEKS', cid) || [];
  var papers = MRB_PICK('PAPERS', cid) || [];
  var wscope = MRB_WEEK_SCOPE(papers, weeks, %d);
  var wk = weeks[%d] || null;
  // Trim to what this walk records — the rest (handlers, unrelated screens'
  // props) is noise JSON.stringify would otherwise choke the terminal with.
  return {
    klass: v.klass,
    week: wk && {label: wk.label, range: wk.range, now: wk.now,
                 started: wk.started, monYmd: wk.monYmd, endMs: wk.endMs},
    scope: {started: wscope.started, weekEndMs: wscope.weekEndMs,
            lastClosed: wscope.lastClosed && {title: wscope.lastClosed.title,
                                               due_at: wscope.lastClosed.due_at,
                                               colSub: null},
            liveN: wscope.live.length, closedN: wscope.closed.length,
            scheduledN: wscope.scheduled.length},
    glance: v.glance && {
      cards: (v.glance.cards || []).map(function (c) {
        return {eyebrow: c.eyebrow, title: c.title, count: c.count,
                hasBar: c.hasBar, hasChase: c.hasChase,
                chase: (c.chase || []).map(function (x) { return x.name; }),
                remindLabel: c.remindLabel, hasMore: c.hasMore, moreLabel: c.moreLabel};
      }),
      showReteach: v.glance.showReteach,
      lastTitle: v.glance.lastTitle, lastLine: v.glance.lastLine,
      worstTwo: v.glance.worstTwo, hasBreakdown: v.glance.hasBreakdown,
      hasWatch: v.glance.hasWatch, noWatch: v.glance.noWatch,
      noWatchLine: v.glance.noWatchLine,
      watch: (v.glance.watch || []).map(function (w) {
        return {name: w.name, reason: w.reason};
      }),
      watchMore: v.glance.watchMore,
      praise: (v.glance.praise || []).map(function (w) {
        return {name: w.name, reason: w.reason};
      })
    },
    roster: (v.roster || []).slice(0, 20).map(function (r) {
      return {name: r.name, week: r.week, avg: r.avg, flag: r.flag, last: r.last};
    }),
    allFlagged: v.allFlagged
  };
})()
"""


def walk(page, base, class_id, label, clock_label):
    url = "%s/teacher/class-detail.html?env=test&class=%s" % (base, class_id)
    ok = goto_ready(page, url, "!!document.querySelector('[data-week]')", settle=3.0)
    print("\n" + "=" * 90)
    print("%s — %s" % (label, clock_label))
    print("=" * 90)
    if not ok:
        print("  !! page never rendered a week chip (class=%s)" % class_id)
        return
    # How many chips are actually on the bar.
    n = page.eval("document.querySelectorAll('[data-week]').length")
    if not n:
        print("  !! no week chips at all")
        return
    for wi in range(n):
        try:
            v = page.eval(RENDER_JS % (wi, wi, class_id, wi, wi))
        except Exception as e:
            print("  wi=%d  !! %s" % (wi, e))
            continue
        if isinstance(v, dict) and v.get("error"):
            print("  wi=%d  !! %s" % (wi, v["error"]))
            continue
        wk = v.get("week")
        sc = v.get("scope") or {}
        print("\n  -- chip %d%s --" % (wi, (" (%s, %s)" % (wk["label"], wk["range"])) if wk else ""))
        print("     week.started=%s week.monYmd=%s | scope.started=%s "
              "lastClosed=%s live=%d closed=%d scheduled=%d"
              % (wk and wk.get("started"), wk and wk.get("monYmd"), sc.get("started"),
                 (sc.get("lastClosed") or {}).get("title"), sc.get("liveN"),
                 sc.get("closedN"), sc.get("scheduledN")))
        g = v.get("glance") or {}
        for c in g.get("cards", []):
            print("     homework card: %r  %r  count=%r hasBar=%s hasChase=%s chase=%s %s"
                  % (c.get("eyebrow"), c.get("title"), c.get("count"), c.get("hasBar"),
                     c.get("hasChase"), c.get("chase"),
                     ("+more(%s)" % c.get("moreLabel") if c.get("hasMore") else "")))
        print("     reteach: title=%r line=%r hasBreakdown=%s worstTwo=%s"
              % (g.get("lastTitle"), g.get("lastLine"), g.get("hasBreakdown"),
                 g.get("worstTwo")))
        if g.get("noWatch"):
            print("     keep an eye on: EMPTY — %r" % g.get("noWatchLine"))
        else:
            print("     keep an eye on: %s %s" % (g.get("watch"), g.get("watchMore") or ""))
        print("     worth a shoutout: %s" % g.get("praise"))
        print("     allFlagged=%s" % v.get("allFlagged"))
        for r in (v.get("roster") or [])[:6]:
            print("       roster: %-22s week=%-14r avg=%-5r flag=%-5s last=%r"
                  % (r.get("name"), r.get("week"), r.get("avg"), r.get("flag"), r.get("last")))


def main():
    pw = os.environ.get("MRB_WEEK_TRUTH_PASSWORD")
    if not pw:
        raise SystemExit("Set MRB_WEEK_TRUTH_PASSWORD (same value --seed used).")

    site, site_port = cdp.serve("mrbadmus_site", port=SITE_PORT)
    base = "http://localhost:%d" % site_port
    print("site on %s" % base)

    classes = [("10h/Ph1", FX2.C_PH1), ("8r/Sc1", FX2.C_SC1), ("9r/Sc2", FX2.C_ONE)]

    for clock_label, y, mo, d, h, mi in CLOCKS:
        with cdp.Browser() as b:
            p = b.attach()
            p.set_viewport(1280, 1400, settle=0)
            # Freeze BEFORE any navigation, so the very first paint already
            # sees it — `Date.now()` on this target returns this instant from
            # here on, exactly as `Emulation.setFixedTime`'s own contract.
            import datetime
            dt = datetime.datetime(y, mo, d, h, mi, 0,
                                    tzinfo=datetime.timezone(datetime.timedelta(hours=1)))  # BST
            epoch_ms = int(dt.timestamp() * 1000)
            freeze_clock(p, epoch_ms)

            signed = sign_in_page(p, base, FX2.TEACHER_EMAIL, pw)
            if not str(signed).startswith("ok"):
                print("!! sign-in failed at %s: %s" % (clock_label, signed))
                continue

            for label, cid in classes:
                walk(p, base, cid, label, clock_label)


if __name__ == "__main__":
    main()
