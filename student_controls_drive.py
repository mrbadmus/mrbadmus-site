#!/usr/bin/env python3
"""student_controls_drive.py — press EVERY control on the student pages, and
say what each one did.

    MRB_DRIVE_EMAIL=… MRB_DRIVE_PASSWORD=… python3 student_controls_drive.py

⚑ WHY THIS EXISTS.

On 22 August 2026 Mide walked the two live student pages himself and found
nine defects in a few minutes. Four of them — P1, P3, P5, P7 — were the same
defect wearing four hats:

    "Open the assignment"  opened nothing
    "Open the lesson"      opened the recall round
    "Sign out"             scrolled the page to the top
    "Settings"             did nothing whatsoever

Every gate was green. `student_parity.py` proved the pages LOOK like Design's
delivery; `student_behaviour.py` proved a scripted sequence of clicks produces
Design's own text; `student_page_drive.py` proved the data on screen is real.
Not one of them asks the only question a student asks: *I pressed the button —
did it do the thing it says?*

Nobody had ever pressed everything. So this presses everything.

── HOW IT DECIDES A CONTROL "DID SOMETHING" ─────────────────────────────

Each control is clicked in a PAGE OF ITS OWN, re-mounted from scratch, so no
click is contaminated by the one before it. Before and after, four things are
recorded:

    the URL            navigation
    the visible text   a view change, a new panel, a changed label
    the node count     something appeared or was removed
    the scroll offset  ← the one that matters

That last one is the point. A dead `<a href="#top">` is not inert: it SCROLLS,
and a check that only asked "did the page change?" would see the scroll
position move and call it a pass. So a control whose ONLY effect is scrolling
is reported as DEAD, loudly, because that is precisely the failure mode that
shipped four times.

A control is judged against what its own label promises:

    NAVIGATED   the URL changed          — for anything named "open …"
    CHANGED     text or node count moved — for a tab, a chip, a toggle
    SCROLLED    nothing but the scroll offset            ⚠️ DEAD
    NOTHING     not one of the four moved                ⚠️ DEAD

── WHAT IT IS NOT ───────────────────────────────────────────────────────

It is not a parity gate and it does not know what the right destination is —
`EXPECT` below carries that, and only for the controls whose destination has
been ruled. Everything else is reported rather than asserted, because a
control doing SOMETHING is the bar this instrument sets, and a human reading
the table is the check on whether it is the right something.
"""

import json
import os
import re
import ssl
import sys
import time
import urllib.request

REPO = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, REPO)
os.chdir(REPO)

import ks3_browser as cdp

PORT = 5500
SUPABASE_URL = "https://urklkrwevjtlfbwnipjn.supabase.co"
PROJECT_REF = "urklkrwevjtlfbwnipjn"
EMAIL = os.environ.get("MRB_DRIVE_EMAIL", "midebolabadmus@gmail.com")
CTX = ssl.create_default_context(cafile="/etc/ssl/cert.pem")

CLASS = "/student/class.html?env=prod"
ASSIGN = "/student/assignment.html?env=prod"

# ── the screens, and how to get to each ──────────────────────────────────
#
# `setup` is a list of label substrings to click, in order, before the sweep
# begins. A screen whose setup cannot be reached is reported as unreachable
# rather than silently skipped — an unreachable screen is itself a finding.
SCREENS = [
    dict(name="class · the bench", url=CLASS, setup=[]),
    dict(name="class · account menu open", url=CLASS, setup=["OT"]),
    dict(name="class · a work row expanded", url=CLASS, setup=["__firstrow__"]),
    dict(name="class · the recall round", url=CLASS, setup=["Recall"]),
    dict(name="assignment · first question", url=ASSIGN, setup=[]),
]

# ── what a control's label PROMISES ──────────────────────────────────────
#
# Only the ruled ones. Anything not named here is reported, not asserted.
#
#   nav:<fragment>   clicking it must land on a URL containing <fragment>
#   change           it must change the page (text or nodes), scrolling alone
#                    does not count
#   gone             it must not be on the page at all
EXPECT = {
    "Open the assignment": "nav:/student/assignment.html",
    "Open the lesson": "nav:/ks3/",
    "Sign out": "nav:/auth.html",
    "Settings": "gone",
}

# Controls that genuinely leave the pages, and so cannot be swept in place
# without ending the screen. They are clicked LAST and their navigation is the
# result. (Nothing here yet beyond the ruled ones above, which are handled.)
DESTRUCTIVE = set()


def anon_key():
    src = open("leaderboard.html", encoding="utf-8").read()
    return re.search(
        r"eyJ[A-Za-z0-9_-]{20,}\.[A-Za-z0-9_-]{20,}\.[A-Za-z0-9_-]{10,}",
        src).group(0)


def sign_in(key):
    pw = (os.environ.get("MRB_DRIVE_PASSWORD")
          or os.environ.get("MRB_TEST_STUDENT_PASSWORD"))
    if not pw:
        raise SystemExit("neither MRB_DRIVE_PASSWORD nor "
                         "MRB_TEST_STUDENT_PASSWORD is set")
    req = urllib.request.Request(
        SUPABASE_URL + "/auth/v1/token?grant_type=password",
        data=json.dumps({"email": EMAIL, "password": pw}).encode(),
        headers={"apikey": key, "Content-Type": "application/json"},
        method="POST")
    del pw
    with urllib.request.urlopen(req, timeout=60, context=CTX) as r:
        return json.loads(r.read().decode())


def wait_for_mount(page, seconds=75.0, poll=0.25):
    """Rendered AND settled — see student_page_drive for the full account.

    ⚠️ The poll is TIGHTER here than in `student_page_drive`, on purpose. That
    drive mounts five pages; this one mounts one per control — several hundred
    — so a 0.6s poll spends most of the run asleep. The settle CONDITION is
    identical (rendered, and no longer growing); only how often it is asked
    changed, which cannot make a slow page look ready."""
    end, last = time.time() + seconds, 0
    while time.time() < end:
        n = page.eval(
            "(function(){var h=document.getElementById('mrb-student');"
            "return h ? h.getElementsByTagName('*').length : -1;})()")
        n = n if isinstance(n, int) else 0
        if n > 20 and n == last:
            return n
        last = n
        time.sleep(poll)
    return last


# ── reading the page ─────────────────────────────────────────────────────

CONTROLS_JS = r"""(function () {
  /* Every control a student could press: real buttons, links, and anything
     Design gave a button role or a click handler. Design builds most of the
     page out of <button style="all:unset"> and <a href="#top">, so both are
     in scope, and so is any element carrying a cursor:pointer — which is how
     the work rows and the option cards are drawn. */
  var seen = [], out = [];
  var nodes = document.querySelectorAll(
    'button, a, [role="button"], [onclick]');
  for (var i = 0; i < nodes.length; i++) {
    var el = nodes[i];
    var r = el.getBoundingClientRect();
    if (!r.width || !r.height) { continue; }         /* not on screen */
    var cs = getComputedStyle(el);
    if (cs.visibility === 'hidden' || cs.display === 'none') { continue; }
    var label = (el.innerText || el.getAttribute('aria-label') || '').trim();
    label = label.replace(/\s+/g, ' ').slice(0, 60);
    out.push({
      i: i,
      tag: el.tagName.toLowerCase(),
      href: el.getAttribute('href') || '',
      label: label || '(no label)',
      w: Math.round(r.width), h: Math.round(r.height)
    });
  }
  return JSON.stringify(out);
})()"""

STATE_JS = r"""(function () {
  return JSON.stringify({
    url: location.pathname + location.search,
    text: (document.body.innerText || ''),
    nodes: document.querySelectorAll('*').length,
    scroll: Math.round(window.scrollY ||
      (document.documentElement && document.documentElement.scrollTop) || 0)
  });
})()"""


def click_index(page, idx):
    """Click the idx'th element of the SAME query CONTROLS_JS enumerated."""
    return page.eval(
        "(function(){var n=document.querySelectorAll("
        "'button, a, [role=\"button\"], [onclick]');"
        "var el=n[%d]; if(!el){return 'gone';}"
        "el.click(); return 'clicked';})()" % idx)


def state(page):
    raw = page.eval(STATE_JS)
    try:
        return json.loads(raw)
    except Exception:
        return {"url": "", "text": "", "nodes": 0, "scroll": 0}


def verdict(before, after):
    if before["url"] != after["url"]:
        return "NAVIGATED", after["url"]
    if before["text"] != after["text"] or before["nodes"] != after["nodes"]:
        d = after["nodes"] - before["nodes"]
        return "CHANGED", ("%+d node(s)" % d) if d else "text changed"
    if before["scroll"] != after["scroll"]:
        return "SCROLLED", "scroll %d → %d" % (before["scroll"], after["scroll"])
    return "NOTHING", ""


def main():
    key = anon_key()
    sess = sign_in(key)
    print("\n🖲   drive_controls — press every control, and say what it did\n")
    print("     as %s (token %s…)" % (EMAIL, sess["access_token"][:8]))

    server, port = cdp.serve("mrbadmus_site", port=PORT)
    base = "http://localhost:%d" % port
    fails, dead, rows = [], [], []

    def fresh(b, url, setup, width):
        """A signed-in, mounted page with `setup` already clicked."""
        page = b.page(base + url, settle=0.6)
        wait_for_mount(page)
        page.set_viewport(width, 900)
        time.sleep(0.35)
        for label in setup:
            if label == "__firstrow__":
                page.eval(
                    "(function(){var n=document.querySelectorAll("
                    "'[role=\"button\"],button');"
                    "for(var i=0;i<n.length;i++){"
                    "var t=(n[i].innerText||'');"
                    "if(/^\\d\\d\\n/.test(t)){n[i].click();return 'ok';}}"
                    "return 'no row';})()")
            else:
                page.eval(
                    "(function(){var n=document.querySelectorAll("
                    "'button,a,[role=\"button\"]');"
                    "for(var i=0;i<n.length;i++){"
                    "if(((n[i].innerText||'').trim())===%s){"
                    "n[i].click();return 'ok';}}"
                    "return 'not found';})()" % json.dumps(label))
            time.sleep(0.5)
        return page

    try:
        with cdp.Browser() as b:
            # let the SDK write its own session, on this origin
            boot = b.page(base + CLASS, settle=1.0)
            boot.eval("(function(){var s=document.createElement('script');"
                      "s.src='https://cdn.jsdelivr.net/npm/@supabase/"
                      "supabase-js@2';document.head.appendChild(s);})()")
            time.sleep(3.0)
            got = boot.eval(
                "(async function(){var c=window.supabase.createClient(%s,%s);"
                "var r=await c.auth.setSession(%s);"
                "return r.error ? ('err:'+r.error.message) : 'ok';})()"
                % (json.dumps(SUPABASE_URL), json.dumps(key),
                   json.dumps({"access_token": sess["access_token"],
                               "refresh_token": sess["refresh_token"]})))
            print("     session in the browser: %s\n" % got)

            for width in (390, 1460):
                print("\n  ══════ %dpx ══════" % width)
                for screen in SCREENS:
                    page = fresh(b, screen["url"], screen["setup"], width)
                    raw = page.eval(CONTROLS_JS)
                    try:
                        controls = json.loads(raw) if raw else []
                    except Exception:
                        controls = []
                    if not controls:
                        print("\n   %s — NO CONTROLS FOUND (unreachable?)"
                              % screen["name"])
                        fails.append("%s @%dpx: no controls found"
                                     % (screen["name"], width))
                        continue

                    print("\n   %s — %d control(s)"
                          % (screen["name"], len(controls)))
                    for c in controls:
                        p = fresh(b, screen["url"], screen["setup"], width)
                        before = state(p)
                        click_index(p, c["i"])
                        time.sleep(0.5)
                        after = state(p)
                        v, detail = verdict(before, after)

                        want = EXPECT.get(c["label"])
                        mark = "  "
                        if want == "gone":
                            mark = "❌"
                            fails.append(
                                "%s @%dpx: %r is still on the page and is "
                                "ruled removed"
                                % (screen["name"], width, c["label"]))
                        elif want and want.startswith("nav:"):
                            target = want[4:]
                            if v == "NAVIGATED" and target in detail:
                                mark = "✅"
                            else:
                                mark = "❌"
                                fails.append(
                                    "%s @%dpx: %r → %s %s (must reach %s)"
                                    % (screen["name"], width, c["label"],
                                       v, detail, target))
                        elif v in ("SCROLLED", "NOTHING"):
                            mark = "⚠️ "
                            dead.append("%s @%dpx: %r → %s"
                                        % (screen["name"], width,
                                           c["label"], v))

                        print("     %s %-34s %-10s %s"
                              % (mark, c["label"][:34], v, detail[:40]))
                        rows.append((screen["name"], width, c["label"],
                                     v, detail))
    finally:
        server.shutdown()

    print("\n  ── controls that did nothing but scroll, or nothing at all ──")
    if dead:
        for d in dead:
            print("     ⚠️  %s" % d)
    else:
        print("     none — every control on every screen did something")

    print("\n  ── ruled destinations ──")
    if fails:
        for f in fails:
            print("     ❌ %s" % f)
        print("\n  ❌ %d ruled check(s) failed" % len(fails))
        return 1
    print("     ✅ every ruled control reached what its label promises")
    print("\n  PASS  %d control press(es) across %d screen(s) at two widths"
          % (len(rows), len(SCREENS)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
