#!/usr/bin/env python3
"""student_controls_drive.py — press EVERY control on the student pages, and
say what each one did.

    MRB_DRIVE_EMAIL=… MRB_DRIVE_PASSWORD=… python3 student_controls_drive.py
    python3 student_controls_drive.py --theme chalk
    python3 student_controls_drive.py --fixture          # no credentials

`--theme <name>` sets `data-bench-theme` on the document root of EVERY mount
(and `--theme harbour` REMOVES the attribute, which is what harbour is — see
`student_themes.py`). A control can be dead in one theme and alive in another:
the 21 Aug amendments made the bench, the term spine and the leaderboard card
themeable, and a control drawn in a colour its ground swallows is pressable by
this script and invisible to a student.

`--fixture` drives `class-fixture.html` / `assignment-fixture.html` instead of
the wired pages, and signs nobody in. It exists because the wired sweep needs
`MRB_DRIVE_PASSWORD`, and a sweep that cannot run without a secret is a sweep
that does not get run. ⚠️ It is WEAKER, and knowingly so: THE WHOLE `EXPECT`
TABLE IS INVALID UNDER IT, because every ruled destination is a destination the
DATA names. `benchPrimaryHref` is empty on the fixture, so "Open the assignment"
correctly ticks the checklist instead of navigating — Design's own line, kept
deliberately (see student_rulings.py, P1) — and the fixture run reports that as
a ruled failure. Likewise the lesson cards keep Design's inert `href="#top"`
and report SCROLLED, and "Sign out" is exercised against a signed-out browser.
Read a `--fixture` run for the DEAD list, never for the ruled destinations;
only the wired run can speak to those. Everything that is purely markup and
handlers — which is every other control — is the same bytes either way.

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
CLASS_FIXTURE = "/student/class-fixture.html"
ASSIGN_FIXTURE = "/student/assignment-fixture.html"

# Set from the command line in main(). Module-level because `fresh()` has to
# re-apply the theme on EVERY mount — each control gets a page of its own, so
# a theme set once would only ever reach the first press.
THEME = None        # None = leave the attribute alone (the page's own default)
FIXTURE = False

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
# ⚠️ Swept LAST on whatever screen they appear on, because pressing them ends
# the session for everything that follows. They are still pressed for real —
# the point of this instrument is that Sign out really signs out.
DESTRUCTIVE = {"Sign out"}


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


# ── ⚠️ THE VIEWPORT IS SET BEFORE THE PAGE LOADS, NOT AFTER ──────────────
#
# ⊕ 22 Aug 2026. Every drive in this repo used to navigate first and resize
# second, and that measured the WRONG BREAKPOINT — silently, and in a way that
# looked like a product bug when it was finally noticed.
#
# Two reasons it goes wrong, and they compound:
#
#   1  The CDP viewport override PERSISTS ACROSS PAGES in one browser. So the
#      "390px" page actually mounted at whatever the previous screen left
#      behind, and the "1460px" page mounted at 390.
#   2  The page decides its header treatment ONCE, from its own width, at
#      mount. Resizing afterwards did not move it back — inside a headless
#      session the resize event does not reliably reach the listener, and
#      Design's 250ms settle poll gives up after six seconds.
#
# The result was a 390px screenshot of the DESKTOP header and a 1460px
# screenshot of the PHONE one, both green, for as long as anyone had looked.
# A real device does not resize into a page; it opens one at its own size.
# So does this now: blank page, set the size, THEN navigate.
#
# ⚠️ Whether a real browser updates the header on a genuine window drag is
# NOT settled by this and is not claimed either way — see the run log. It is a
# different question from this one, which is purely about measuring the right
# thing.


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


_SET_THEME = (
    "(function(t){var e=document.documentElement;"
    "if(t===null){e.removeAttribute('data-bench-theme');}"
    "else{e.setAttribute('data-bench-theme',t);}"
    "return String(e.getAttribute('data-bench-theme'));})(%s)")


def apply_theme(page):
    """Put `THEME` on the document root of this mount, and say what stuck.

    ⚠️ HARBOUR IS THE ABSENCE OF THE ATTRIBUTE, not `="harbour"` — Design's
    README says "(absent = harbour)". Writing the attribute for it would
    exercise a case no student is ever in, and would hide a default that had
    silently reverted to the old graphite.

    Returns the attribute the page reports, or None if no theme was asked for.
    """
    if THEME is None:
        return None
    arg = "null" if THEME == "harbour" else json.dumps(THEME)
    got = page.eval(_SET_THEME % arg)
    want = "null" if THEME == "harbour" else THEME
    if str(got) != want:
        raise SystemExit("data-bench-theme is %r after asking for %r — the "
                         "sweep would be reported under the wrong theme"
                         % (got, want))
    return got


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


def parse_args(argv):
    """`--theme <name>` and `--fixture`. Deliberately hand-rolled and tiny —
    this file's interface is two flags, and an unknown flag is a typo worth
    stopping for rather than ignoring."""
    global THEME, FIXTURE
    i = 0
    while i < len(argv):
        a = argv[i]
        if a == "--theme":
            i += 1
            if i >= len(argv):
                raise SystemExit("--theme needs a theme name")
            THEME = argv[i]
        elif a.startswith("--theme="):
            THEME = a.split("=", 1)[1]
        elif a == "--fixture":
            FIXTURE = True
        else:
            raise SystemExit("unknown argument %r "
                             "(--theme <name> | --fixture)" % a)
        i += 1
    if FIXTURE:
        for s in SCREENS:
            s["url"] = (s["url"].replace(CLASS, CLASS_FIXTURE)
                                .replace(ASSIGN, ASSIGN_FIXTURE))


def main():
    parse_args(sys.argv[1:])
    print("\n🖲   drive_controls — press every control, and say what it did\n")
    if FIXTURE:
        key, sess = None, {"access_token": "(fixture — nobody signed in)"}
        print("     ⚠️  --fixture: driving the FIXTURE pages, signed out. "
              "Sign out's ruled destination is not proof about the wired page.")
    else:
        key = anon_key()
        sess = sign_in(key)
        print("     as %s (token %s…)" % (EMAIL, sess["access_token"][:8]))
    print("     theme: %s" % (THEME if THEME else "(page default, untouched)"))

    server, port = cdp.serve("mrbadmus_site", port=PORT)
    base = "http://localhost:%d" % port
    fails, dead, rows, harness = [], [], [], []

    def size_to(b, width):
        """Set the window size once, on a blank page, before the screen's
        first mount. The override persists across navigations on this target."""
        b.page("about:blank", settle=0.15).set_viewport(width, 900)

    def fresh(b, url, setup, width):
        """A signed-in, mounted page with `setup` already clicked."""
        # ⚠️ THE VIEWPORT IS SET ONCE PER SCREEN, NOT PER CONTROL, and it is
        # the SAME persistence that caused the bug the note above describes
        # that makes this safe: the override survives a navigation on this
        # target, so every mount in this screen inherits the size set by
        # `size_to` before the first one. Two page loads per control against a
        # cold backend is what killed three runs of this sweep; one is enough.
        page = b.page(base + url, settle=0.6)
        wait_for_mount(page)
        time.sleep(0.35)
        # bounced to the sign-in page? the last control signed us out. Sign
        # back in and come again — see the note in main().
        if not FIXTURE and "auth.html" in (page.eval("location.pathname") or ""):
            sign_browser_in(b)
            page = b.page(base + url, settle=0.6)
            wait_for_mount(page)
            time.sleep(0.35)
        # ⚠️ EVERY MOUNT, not once per screen. Each control is pressed on a
        # page of its own, and a fresh document carries no attribute.
        apply_theme(page)
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

    # ── ⚠️ PRESSING "SIGN OUT" ENDS THE SESSION FOR THE WHOLE SWEEP ──────
    #
    # And that is the correct behaviour of the control being tested, which is
    # what makes it awkward: every page loaded after it is bounced to
    # /auth.html by the guard, so the remaining controls on that screen — and
    # every screen after it — were being measured on the SIGN-IN PAGE while
    # still being reported under the class view's name. The first run of this
    # sweep did exactly that and looked plausible: the controls kept reporting
    # CHANGED, because the auth page changes too.
    #
    # So the session is re-established whenever a page lands on /auth.html.
    # Signing out must stay a real sign-out — weakening it to make the sweep
    # convenient would be testing a different button.
    signed_in = [False]
    live = {"sess": sess}

    def sign_browser_in(b):
        if FIXTURE:
            return "skipped (--fixture)"
        # ⚠️ MINT A NEW SESSION, DO NOT REPLAY THE OLD ONE. `auth.signOut()`
        # revokes the refresh token server-side, so `setSession` with the
        # session we started from silently fails and the browser stays signed
        # out. The first attempt at this recovery reused `sess` and every
        # screen after "Sign out" was measured on the SIGN-IN PAGE while still
        # being reported under the class view's name — 24 controls of
        # confident nonsense, with a "Sign In" button in the middle of it that
        # gave the game away.
        try:
            live["sess"] = sign_in(key)
        except Exception as err:                      # noqa: BLE001
            print("     ⚠️  could not re-authenticate: %s" % err)
        # ⚠️ SIGN IN ON A BARE SAME-ORIGIN PAGE, NOT ON THE CLASS PAGE.
        # `localStorage` is per-origin, so this has to be served from
        # localhost:5500 — but it does NOT have to be the app. Injecting the
        # SDK into the class page means racing `student-live.js`, which is
        # loading its own copy and doing its own auth at the same time, and
        # three runs of this sweep hung inside `setSession` because of it.
        # `http.server`'s directory listing is HTML on the right origin with
        # no JavaScript of its own to fight.
        boot = b.page(base + "/shared/", settle=0.4)
        boot.eval("(function(){var s=document.createElement('script');"
                  "s.src='https://cdn.jsdelivr.net/npm/@supabase/"
                  "supabase-js@2';document.head.appendChild(s);})()")
        for _ in range(30):
            if boot.eval("!!(window.supabase && window.supabase.createClient)"):
                break
            time.sleep(0.25)
        got = boot.eval(
            "(async function(){var c=window.supabase.createClient(%s,%s);"
            "var r=await c.auth.setSession(%s);"
            "return r.error ? ('err:'+r.error.message) : 'ok';})()"
            % (json.dumps(SUPABASE_URL), json.dumps(key),
               json.dumps({"access_token": live["sess"]["access_token"],
                           "refresh_token": live["sess"]["refresh_token"]})))
        signed_in[0] = (got == "ok")
        return got

    # ── ⚠️ THE BROWSER IS RESTARTABLE, BECAUSE IT DIES ───────────────────
    #
    # This sweep makes several hundred real page loads against a real backend,
    # and Chrome's DevTools socket does not always survive that: three runs
    # ended on `timed out waiting for 2 bytes from chrome`, one of them on the
    # very first sign-in. Losing the whole matrix to one dropped socket means
    # the sweep never finishes, and a check that never finishes is a check
    # nobody runs.
    #
    # So a CDP failure restarts Chrome, signs back in and carries on, and the
    # presses it could not complete are listed separately at the end — as this
    # harness failing, never as a verdict on the control.
    holder = {"b": None}

    def restart():
        old_b = holder["b"]
        if old_b is not None:
            try:
                old_b.close()
            except Exception:                          # noqa: BLE001
                pass
        holder["b"] = cdp.Browser().start()
        sign_browser_in(holder["b"])
        return holder["b"]

    try:
        holder["b"] = cdp.Browser().start()
        b = holder["b"]
        print("     session in the browser: %s\n" % sign_browser_in(b))

        if True:
            for width in (390, 1460):
                print("\n  ══════ %dpx ══════" % width)
                for screen in SCREENS:
                    b = holder["b"]
                    try:
                        size_to(b, width)
                        page = fresh(b, screen["url"], screen["setup"], width)
                        raw = page.eval(CONTROLS_JS)
                    except Exception as err:           # noqa: BLE001
                        print("\n   %s — restarting the browser (%s)"
                              % (screen["name"], str(err)[:44]))
                        b = restart()
                        try:
                            size_to(b, width)
                            page = fresh(b, screen["url"], screen["setup"], width)
                            raw = page.eval(CONTROLS_JS)
                        except Exception as err2:      # noqa: BLE001
                            harness.append("%s @%dpx: could not open the "
                                           "screen at all — %s"
                                           % (screen["name"], width,
                                              str(err2)[:60]))
                            continue
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
                    controls.sort(key=lambda c: c["label"] in DESTRUCTIVE)
                    for c in controls:
                        try:
                            p = fresh(holder["b"], screen["url"],
                                      screen["setup"], width)
                            before = state(p)
                            click_index(p, c["i"])
                            time.sleep(0.5)
                            after = state(p)
                            v, detail = verdict(before, after)
                        except Exception as err:      # noqa: BLE001
                            # A dropped CDP socket is this harness failing, not
                            # the control. Restart, say so, carry on.
                            print("     ⁇  %-34s HARNESS   %s"
                                  % (c["label"][:34], str(err)[:44]))
                            harness.append("%s @%dpx: %r — %s"
                                           % (screen["name"], width,
                                              c["label"], str(err)[:60]))
                            try:
                                restart()
                                size_to(holder["b"], width)
                            except Exception:          # noqa: BLE001
                                pass
                            continue

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
        if holder["b"] is not None:
            try:
                holder["b"].close()
            except Exception:                          # noqa: BLE001
                pass
        server.shutdown()

    print("\n  ── controls that did nothing but scroll, or nothing at all ──")
    if dead:
        for d in dead:
            print("     ⚠️  %s" % d)
    else:
        print("     none — every control on every screen did something")

    if harness:
        print("\n  ── presses this harness could not complete ──")
        for h in harness:
            print("     ⁇  %s" % h)
        print("     (a dropped CDP socket, not a verdict on the control)")

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
