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
#
# ⊕ 23 Aug 2026 — THE SETUP LABELS WENT STALE AND THE SWEEP DID NOT SAY SO.
#
# `class · the recall round` was reached by clicking a nav entry labelled
# `Recall`. Phase 3 RETIRED that nav entry (the round is now reached from the
# bench), so the click matched nothing, `fresh()` returned the plain bench, and
# the sweep swept the BENCH AGAIN while printing the recall round's name — a
# screen reported as covered that was never opened. The docstring above claims
# "a screen whose setup cannot be reached is reported as unreachable rather
# than silently skipped"; it was not true, and it is now (see `fresh()`).
#
# A setup step is either an exact innerText match, `~fragment` for a substring
# match, or one of the `__…__` verbs handled in `fresh()`.
SCREENS = [
    dict(name="class · the bench", url=CLASS, setup=[]),
    # ⊕ 23 Aug 2026 — `"OT"` WAS STALE AND HAD NEVER OPENED ANYTHING.
    # It is the avatar monogram, which is the student's INITIALS: `AY` on
    # Design's fixture, `TO` on the live throwaway, `OT` on nobody. With the
    # setup unchecked the click matched nothing and this screen was swept as
    # the plain BENCH under its own name — so `account menu open` has never
    # actually been swept, and neither has the work row below it. `__avatar__`
    # finds the monogram button by SHAPE instead of by a literal, so it cannot
    # go stale when the student changes.
    dict(name="class · account menu open", url=CLASS, setup=["__avatar__"]),
    # `/^\d\d\n/` never matched: a work row's innerText opens with its WEEK
    # (`W01\n…`), not a bare pair of digits.
    dict(name="class · a work row expanded", url=CLASS, setup=["__firstrow__"]),
    # ⚠️ At 390 there is NO inline Settings — node 26 is inside `if wide`, so
    # the only route on a phone is avatar → dropdown → Settings (node 30).
    # Pressing "Settings" blind reached the sheet at 1460 and nothing at 390.
    dict(name="class · the account sheet", url=CLASS,
         setup=["__avatar__", "Settings"]),
    dict(name="class · the flashcards overlay", url=CLASS,
         setup=["~FLASHCARDS"]),
    dict(name="class · the flashcards overlay, revealed", url=CLASS,
         setup=["~FLASHCARDS", "~Reveal"]),
    dict(name="class · the recall round", url=CLASS,
         setup=["~Practise recall"]),
    dict(name="class · the recall round, an option picked", url=CLASS,
         setup=["~Practise recall", "__opt0__"]),
    dict(name="class · the recall round, checked", url=CLASS,
         setup=["~Practise recall", "__opt0__", "~Check"]),
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
    # ⊕ 23 Aug 2026 — THIS USED TO READ `"Settings": "gone"`, AND IT WENT
    # STALE THE DAY THE PICKER SHIPPED.
    #
    # P7 pruned both Settings controls because they did nothing, and this line
    # asserted they stayed pruned. Phase 1b UN-pruned them and gave them the
    # job Design drew — `SET_ON` 26 and 30 both resolve `openAccount`, and the
    # bench theme picker lives behind them. P7's own registration predicted
    # this ("It returns when Design's theme picker gives it a job"), the prune
    # and the RULED_CONTROLS twin were both retired, and THIS assertion was
    # not. The sweep therefore failed six times on correct output, saying a
    # control was "still on the page and is ruled removed" about the control
    # the run had deliberately restored.
    #
    # It is now asserted the other way: Settings must OPEN something. `change`
    # rather than a `nav:` target because the sheet is an overlay, not a page.
    "Settings": "change",
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

#
# ⊕ 23 Aug 2026 — THE FIFTH THING RECORDED, AND WHY IT HAD TO BE ADDED.
#
# `docs/ks3/MERGE-2026-08-23.md` recorded this instrument's own blind spot
# rather than working around it:
#
#     "a genuinely dead option chip and a live one both read NOTHING today"
#     "…the recall options change only a background, which the instrument
#      does not watch."
#
# It was recorded for the recall unit. The recall round has now SHIPPED, so
# four of the most-pressed controls a student touches — the A/B/C/D option
# chips — were controls this sweep could not tell working from broken. Six
# theme swatches arrived with the same shape (a swatch selects by moving a
# tick and a border) and so did the flashcard pips.
#
# So the paint of every CONTROL is digested. Deliberately NOT every element:
# a digest over the whole document would pick up the flip animation, the
# progress bar and any transition still settling, and would report CHANGED
# for everything — a gate that says yes to all inputs. The control set is
# exactly the set being pressed, which is where a selection state lives.
#
# It is reported as its own verdict, REPAINTED, and NOT folded into CHANGED:
# a reader must still be able to see at a glance which controls moved real
# content and which only moved a colour.
STATE_JS = r"""(function () {
  var q = 'button, a, [role="button"], [onclick]';
  var n = document.querySelectorAll(q), paint = '', i;
  for (i = 0; i < n.length; i++) {
    var cs = getComputedStyle(n[i]);
    paint += cs.backgroundColor + '|' + cs.color + '|' + cs.borderColor + '|' +
             cs.outlineColor + '|' + cs.opacity + '|' +
             cs.boxShadow.slice(0, 40) + '|' +
             (n[i].getAttribute('data-on') || '') + '|' +
             (n[i].getAttribute('data-st') || '') + ';';
  }
  return JSON.stringify({
    url: location.pathname + location.search,
    text: (document.body.innerText || ''),
    nodes: document.querySelectorAll('*').length,
    paint: paint,
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
        return {"url": "", "text": "", "nodes": 0, "paint": "", "scroll": 0}


def verdict(before, after):
    if before["url"] != after["url"]:
        return "NAVIGATED", after["url"]
    if before["text"] != after["text"] or before["nodes"] != after["nodes"]:
        d = after["nodes"] - before["nodes"]
        return "CHANGED", ("%+d node(s)" % d) if d else "text changed"
    # ⊕ 23 Aug 2026 — a selection is a real effect. See STATE_JS above.
    if before.get("paint") != after.get("paint"):
        return "REPAINTED", "a control's paint or selection state moved"
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
        # ⊕ 23 Aug 2026 — EVERY SETUP STEP IS NOW CHECKED. A step that matches
        # nothing used to leave the sweep on whatever screen it happened to be
        # on, under the name of the screen it failed to open. See SCREENS.
        holder["setup"] = []
        for label in setup:
            if label == "__firstrow__":
                # ⚠️ THE WEEK IS NOT ALWAYS FIRST. At 1460 a row reads
                # "W01\nParticle model…"; at 390 it reads
                # "Particle model…\nW01 · DUE". Anchoring the match at the
                # START of the text therefore worked at one width and silently
                # failed at the other — which is how this verb came to be
                # measured at 1460 only. Matched anywhere in the label, and
                # required to be a ROW rather than a chip by its height.
                got = page.eval(
                    "(function(){var n=document.querySelectorAll("
                    "'[role=\"button\"],button');"
                    "for(var i=0;i<n.length;i++){"
                    "var e=n[i], r=e.getBoundingClientRect();"
                    "if(r.height<40||!r.width){continue;}"
                    "var t=(e.innerText||'');"
                    "if(/\\bW\\d\\d\\b/.test(t)){"
                    "e.click();return 'ok';}}"
                    "return 'not found';})()")
            elif label == "__avatar__":
                # The header monogram: a control in the top 120px whose whole
                # label is 1-3 capitals. Matched by shape, never by initials.
                got = page.eval(
                    "(function(){var n=document.querySelectorAll("
                    "'button,[role=\"button\"]');"
                    "for(var i=0;i<n.length;i++){"
                    "var e=n[i], r=e.getBoundingClientRect();"
                    "if(r.top>120||!r.width){continue;}"
                    "var t=(e.innerText||'').replace(/\\s+/g,' ').trim();"
                    # ⚠️ THE MONOGRAM IS ALONE ONLY AT PHONE WIDTH. At 1460
                    # the same button reads "AY Ayo" (monogram + first name),
                    # so an anchored `^[A-Z]{1,3}$` matched at 390 and failed
                    # at 1460 — the mirror image of __firstrow__'s failure.
                    # The monogram is the FIRST token either way.
                    "if(/^[A-Z]{1,3}( |$)/.test(t)){e.click();return 'ok';}}"
                    "return 'not found';})()")
            elif label == "__opt0__":
                # the recall round's first option chip — it is drawn as a
                # cursor:pointer div, not a <button>, which is why it needs a
                # verb of its own rather than a label.
                got = page.eval(
                    "(function(){var d=document.querySelector("
                    "'[data-port-region=\"recall-round\"]');"
                    "if(!d){return 'not found';}"
                    "var o=d.querySelectorAll('.opt');"
                    "if(!o.length){return 'not found';}"
                    "o[0].click();return 'ok';})()")
            elif label.startswith("~"):
                got = page.eval(
                    "(function(){var n=document.querySelectorAll("
                    "'button,a,[role=\"button\"]');"
                    "for(var i=0;i<n.length;i++){"
                    "var t=(n[i].innerText||'').replace(/\\s+/g,' ').trim();"
                    "if(t.indexOf(%s)>=0){n[i].click();return 'ok';}}"
                    "return 'not found';})()" % json.dumps(label[1:]))
            else:
                got = page.eval(
                    "(function(){var n=document.querySelectorAll("
                    "'button,a,[role=\"button\"]');"
                    "for(var i=0;i<n.length;i++){"
                    "if(((n[i].innerText||'').trim())===%s){"
                    "n[i].click();return 'ok';}}"
                    "return 'not found';})()" % json.dumps(label))
            if got != "ok":
                holder["setup"].append((label, got))
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
    holder = {"b": None, "setup": []}

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
                    # ⊕ 23 Aug 2026 — a screen that did not open is a FINDING,
                    # never a screen swept under the wrong name.
                    if holder["setup"]:
                        bad = ", ".join("%r → %s" % (a, c)
                                        for a, c in holder["setup"])
                        print("\n   %s — SETUP FAILED (%s) — NOT SWEPT"
                              % (screen["name"], bad))
                        fails.append("%s @%dpx: setup step(s) matched nothing "
                                     "(%s) — the screen was never opened, so "
                                     "it was NOT swept"
                                     % (screen["name"], width, bad))
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
                        if want == "change":
                            # scrolling alone does not count — that is the
                            # whole point of this instrument.
                            if v in ("CHANGED", "NAVIGATED", "REPAINTED"):
                                mark = "✅"
                            else:
                                mark = "❌"
                                fails.append(
                                    "%s @%dpx: %r → %s %s (must open something)"
                                    % (screen["name"], width, c["label"],
                                       v, detail))
                        elif want == "gone":
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
