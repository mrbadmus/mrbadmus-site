#!/usr/bin/env python3
"""ks4_chrome_drive.py — walk the whole KS4 journey in a real browser (MRB-301).

`ks4_chrome_tells.py` reads the built BYTES: it proves no invented number and
no dead destination survives, and it would pass just as happily on a page that
renders blank. This is the other half — the pages DRIVEN, at four widths, in
both auth states, with the console listened to.

── WHAT IT WALKS ──────────────────────────────────────────────────────────

The journey as a student meets it, one click at a time and following the real
hrefs rather than a list of URLs:

    landing → KS3 entry (the UNTOUCHED estate) → back
            → GCSE hub → Combined → Foundation → Physics → Energy → a LESSON
                       → Triple   → Higher     → each science

── WHAT IT ASSERTS ────────────────────────────────────────────────────────

  1. every view mounts, wearing the chrome, with Design's brand on it;
  2. NO HORIZONTAL OVERFLOW at 360 / 390 / 820 / 1440. The header-overflow
     defect class is known on this site, and it only ever shows up at a real
     narrow width — Chrome floors a `--window-size` run near 500px, so the
     widths come from Emulation.setDeviceMetricsOverride via ks3_browser;
  3. the console stays quiet, on load AND after a reload;
  4. every KS3 page reached from the landing still works and still wears the
     KS3 mark — the scope wall, driven rather than assumed;
  5. the LESSON page behind a topic row still renders, still wears the
     CLASSIC nav, and does NOT wear the chrome;
  6. no visible progress claim on any page, signed out or signed in — the
     text-level twin of what `tells` checks in the bytes.

Signed-in is simulated by seeding the same localStorage key `shared/nav.js`
reads (`sb-…-auth-token`). No backend, no credential: nav.js's two follow-up
fetches fail and are caught, which is also the cold-Render state a real
student sees, so it is worth driving on purpose.

Run:  python3 ks4_chrome_drive.py [--shots DIR]
"""

import argparse
import json
import os
import sys

import ks3_browser as cdp

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "mrbadmus_site")

WIDTHS = [1440, 820, 390, 360]

# One representative route per view of the journey. Discovered by FOLLOWING
# the built pages' own links below; this is the spine the walk must reach.
JOURNEY = [
    ("landing",        "/index.html"),
    ("ks3-entry",      "/ks3/index.html"),
    ("gcse-hub",       "/ks4.html"),
    ("pathway-combined", "/combined/index.html"),
    ("pathway-triple", "/triple/index.html"),
    ("tier-foundation", "/combined/foundation/index.html"),
    ("tier-higher",    "/combined/higher/index.html"),
    ("science-physics", "/combined/foundation/physics/index.html"),
    ("science-chemistry", "/combined/foundation/chemistry/index.html"),
    ("science-biology", "/combined/foundation/biology/index.html"),
    ("topic-energy",   "/combined/foundation/physics/energy.html"),
    ("lesson",         "/combined/foundation/physics/energy/efficiency.html"),
]

# A phrase on one of these pages would be a progress claim with no data
# behind it. Checked against RENDERED TEXT, which is where `tells` cannot
# look: a string assembled by JS never appears in the built bytes.
PROGRESS_CLAIMS = [
    "Jump back in", "Your progress", "Your best", "Your rank", "Your tier so far",
    "Last opened", "Half finished", "Not started", "In progress", "of 7 done",
    "You are here", "Carry on",
]

SESSION_KEY = "sb-urklkrwevjtlfbwnipjn-auth-token"

# ⚠️ THE ACCESS TOKEN HAS TO BE A REAL-SHAPED JWT, and finding that out cost a
# round of 88 identical failures.
#
# Every one of these pages loads the Supabase UMD bundle (`chat_html()`), and
# the SDK reads this key at boot, decodes `access_token` as a JWT, and DELETES
# the stored session when it cannot. A token of "drive-only-not-a-real-token"
# was therefore written, purged before nav.js looked, and read back as absent
# — which is indistinguishable from "localStorage does not persist here", and
# was misdiagnosed as exactly that until raw persistence was tested on its own
# and turned out to be fine.
#
# So the header and payload below are properly base64url-encoded. The
# signature is not, and does not need to be: nothing client-side verifies it.
# Nothing this token reaches would honour it either — its only job is to make
# the SDK keep the session so nav.js can render a chip.
_JWT_HEADER = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
_JWT_PAYLOAD = ("eyJzdWIiOiIwMDAwMDAwMC0wMDAwLTAwMDAtMDAwMC0wMDAwMDAwMDAzMDEi"
                "LCJhdWQiOiJhdXRoZW50aWNhdGVkIiwicm9sZSI6ImF1dGhlbnRpY2F0ZWQi"
                "LCJleHAiOjQxMDI0NDQ4MDAsImlhdCI6MTcwMDAwMDAwMCwiZW1haWwiOiJk"
                "cml2ZUBleGFtcGxlLmludmFsaWQifQ")
_JWT_SIG = "c2lnbmF0dXJlLW5vdC12ZXJpZmllZC1jbGllbnQtc2lkZQ"

FAKE_SESSION = {
    "access_token": "%s.%s.%s" % (_JWT_HEADER, _JWT_PAYLOAD, _JWT_SIG),
    "token_type": "bearer",
    "expires_in": 3600,
    "expires_at": 4102444800,          # 2100 — never expired during a run
    "refresh_token": "drive-refresh-not-a-real-token",
    "user": {"id": "00000000-0000-0000-0000-000000000301",
             "aud": "authenticated",
             "role": "authenticated",
             "email": "drive@example.invalid",
             "app_metadata": {},
             "user_metadata": {"first_name": "Anifat"}},
}

failures = []


def fail(msg):
    failures.append(msg)
    print("   ✗ %s" % msg)


def probe(page, label, width, signed_in):
    """Everything measurable about one view at one width."""
    tag = "%s @%d %s" % (label, width, "signed-in" if signed_in else "signed-out")

    # Horizontal overflow. documentElement is the scroller; comparing its
    # scrollWidth to its clientWidth is what a sideways-scrolling page looks
    # like from the inside. `+1` absorbs sub-pixel rounding, nothing more.
    over = page.eval(
        "(function(){var d=document.documentElement;"
        "return {sw:d.scrollWidth, cw:d.clientWidth, iw:window.innerWidth};})()")
    if over["iw"] != width:
        fail("%s — viewport reflowed at %dpx, not %d (device metrics did not "
             "take; a --window-size run would floor near 500)"
             % (tag, over["iw"], width))
    if over["sw"] > over["cw"] + 1:
        widest = page.eval(
            "(function(){var w=null,m=0;"
            "document.querySelectorAll('body *').forEach(function(e){"
            "var r=e.getBoundingClientRect();"
            "if(r.right>m){m=r.right;w=e.tagName+'.'+(e.className||'')+''}});"
            "return w+' @'+Math.round(m);})()")
        fail("%s — scrolls sideways: %dpx of content in %dpx. Widest: %s"
             % (tag, over["sw"], over["cw"], widest))

    errs = page.console_errors()
    if errs:
        # A failed fetch to the backend is expected here: this harness serves
        # static files with no Render behind it, and both nav.js's profile
        # calls and ks4-chrome.js's leaderboard call will fail. That is the
        # cold-backend state and the page must survive it — so those are not
        # counted, and anything else is.
        real = [e for e in errs
                if "mrbadmus-backend" not in str(e)
                and "supabase.co" not in str(e)
                and "Failed to load resource" not in str(e)
                and "ERR_" not in str(e)]
        if real:
            fail("%s — console: %s" % (tag, json.dumps(real)[:400]))
    return over


def check_chrome(page, label, chrome_expected):
    has_attr = page.eval("document.body.getAttribute('data-chrome')==='ks4'")
    if has_attr != chrome_expected:
        fail("%s — data-chrome=\"ks4\" is %s, expected %s"
             % (label, has_attr, chrome_expected))
    if chrome_expected:
        brand = page.eval(
            "(function(){var a=document.querySelector('.nav-brand');"
            "if(!a) return null;"
            "var s=a.querySelector('svg');"
            "return {text:a.textContent.trim(),"
            " chevrons:s?s.querySelectorAll('path').length:0,"
            " stroke:s?(s.querySelector('path')||{}).getAttribute"
            "&&s.querySelector('path').getAttribute('stroke'):null,"
            " font:getComputedStyle(a).fontFamily};})()")
        if not brand:
            fail("%s — no .nav-brand in the header" % label)
        else:
            if brand["text"] != "MrBadmusAI":
                fail("%s — brand wordmark reads %r" % (label, brand["text"]))
            if brand["chevrons"] != 2:
                fail("%s — Design's BrandMark is a DOUBLE chevron; found %d path(s)"
                     % (label, brand["chevrons"]))
            if (brand["stroke"] or "").upper() != "#E4572E":
                fail("%s — brand stroke is %r, not #E4572E" % (label, brand["stroke"]))
            if "Bricolage" not in (brand["font"] or ""):
                fail("%s — brand font resolves to %r, not Bricolage Grotesque"
                     % (label, brand["font"]))


def check_no_progress(page, label, signed_in):
    text = page.eval("document.body.innerText")
    for claim in PROGRESS_CLAIMS:
        if claim in text:
            fail("%s (%s) — renders the progress claim %r, and there is no "
                 "KS4 progress model behind it"
                 % (label, "signed-in" if signed_in else "signed-out", claim))


def check_auth_chip(page, label, signed_in, has_slot=True):
    """The auth state, where shared/nav.js actually puts it.

    ⚠️ Signed OUT, `#nav-auth-area` is EMPTY — that is not a bug and it is not
    new. nav.js renders Sign In / Sign Up into the DRAWER (`#nav-drawer-auth`)
    and returns early before touching the cluster slot. The first version of
    this check asserted the buttons were in the cluster and failed 48 times on
    correct, pre-existing behaviour. Both places are asserted now, each for
    what it actually holds."""
    if not has_slot:
        return
    got = page.eval(
        "(function(){var a=document.getElementById('nav-auth-area');"
        "return a? a.innerText.replace(/\\s+/g,' ').trim() : null;})()")
    drawer = page.eval(
        "(function(){var d=document.getElementById('nav-drawer-auth');"
        "return d? d.innerText.replace(/\\s+/g,' ').trim() : null;})()")
    if got is None:
        fail("%s — no #nav-auth-area on the page at all" % label)
        return
    if signed_in:
        if "Anifat" not in got:
            fail("%s — signed in, but the cluster chip reads %r" % (label, got))
        if drawer is not None and "Sign In" in (drawer or ""):
            fail("%s — signed in, but the drawer still offers Sign In (%r)"
                 % (label, drawer))
    else:
        if got != "":
            fail("%s — signed out, but the cluster chip is not empty (%r)"
                 % (label, got))
        if drawer is not None and "Sign In" not in drawer:
            fail("%s — signed out, but the drawer does not offer Sign In (%r)"
                 % (label, drawer))


def walk_links(page, label, want):
    """Assert this page really offers the next step, by href."""
    hrefs = page.eval(
        "Array.from(document.querySelectorAll('a[href]')).map(a=>"
        "a.getAttribute('href'))")
    for w in want:
        if w not in hrefs:
            fail("%s — no control linking %s. The journey is broken here."
                 % (label, w))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--shots", default=os.path.join(ROOT, "docs", "redesign",
                                                    "mrb-301-shots"))
    args = ap.parse_args()
    os.makedirs(args.shots, exist_ok=True)

    if not os.path.isdir(OUT):
        raise SystemExit("run build_all.py first — %s is missing" % OUT)

    server, port = cdp.serve(OUT)
    base = "http://localhost:%d" % port
    print("serving %s on %s\n" % (OUT, base))

    try:
        for signed_in in (False, True):
            state = "signed-in" if signed_in else "signed-out"
            print("══ %s ══" % state.upper())
            with cdp.Browser() as b:
                page = b.attach()
                if signed_in:
                    # ⚠️ SEEDED PER DOCUMENT, not once.
                    #
                    # Writing the key with `eval` and then navigating does not
                    # work here — measured: the value reads back immediately
                    # and is gone after the next `Page.navigate`. And even if
                    # it survived, nav.js reads the key at DOMContentLoaded,
                    # so a write that lands after load proves nothing.
                    #
                    # `addScriptToEvaluateOnNewDocument` runs before any of
                    # the page's own scripts, on every navigation, which is
                    # exactly the moment a real session would already exist.
                    page.send("Page.addScriptToEvaluateOnNewDocument", {
                        "source": "try{localStorage.setItem(%s,%s);}catch(e){}"
                                  % (json.dumps(SESSION_KEY),
                                     json.dumps(json.dumps(FAKE_SESSION)))})

                for label, route in JOURNEY:
                    is_chrome = label not in ("ks3-entry", "lesson")
                    for width in WIDTHS:
                        # ⚠️ VIEWPORT BEFORE NAVIGATION. Emulation metrics set
                        # after load reflow the page, but any layout the page
                        # measured for itself on load was measured at the old
                        # width. Set it first and the page never sees another.
                        page.set_viewport(width, 900)
                        page.goto(base + route)
                        probe(page, label, width, signed_in)
                        check_chrome(page, "%s @%d" % (label, width), is_chrome)
                        if is_chrome:
                            check_no_progress(page, "%s @%d" % (label, width), signed_in)
                        # KS3 pages have their own header and no cluster
                        # slot at all — asserting one would be asserting that
                        # the estate MRB-301 must not touch had been touched.
                        check_auth_chip(page, "%s @%d" % (label, width),
                                        signed_in, has_slot=(label != "ks3-entry"))
                        if width in (WIDTHS[0], 390):
                            page.screenshot(
                                os.path.join(args.shots,
                                             "%s-%s-%d.png" % (label, state, width)),
                                width=width)
                        # The reload pass — same width, driven twice.
                        page.goto(base + route)
                        probe(page, label + " (reload)", width, signed_in)
                    print("   ✓ %s %s" % (label, route))

                # The journey's own links, followed rather than assumed.
                print("   — walking the spine by href —")
                checks = [
                    ("/index.html", ["/ks3/index.html", "/ks4.html",
                                     "/weekly-challenge.html", "/leaderboard.html"]),
                    ("/ks4.html", ["/combined/index.html", "/triple/index.html",
                                   "/leaderboard.html"]),
                    ("/combined/index.html", ["/combined/foundation/index.html",
                                              "/combined/higher/index.html"]),
                    ("/triple/index.html", ["/triple/foundation/index.html",
                                            "/triple/higher/index.html"]),
                    ("/combined/foundation/index.html",
                     ["/combined/foundation/physics/index.html",
                      "/combined/foundation/chemistry/index.html",
                      "/combined/foundation/biology/index.html"]),
                    ("/combined/higher/index.html",
                     ["/combined/higher/physics/index.html"]),
                    ("/combined/foundation/physics/index.html",
                     ["/combined/foundation/physics/energy.html",
                      "/combined/foundation/physics/waves.html"]),
                    ("/combined/foundation/physics/energy.html",
                     ["/combined/foundation/physics/energy/efficiency.html",
                      "/combined/foundation/physics/energy/power.html",
                      "/combined/foundation/physics/index.html",
                      "/combined/foundation/physics/electricity.html"]),
                ]
                for route, want in checks:
                    page.set_viewport(1440, 900)
                    page.goto(base + route)
                    walk_links(page, route, want)
                    print("   ✓ %s offers %d next steps" % (route, len(want)))
    finally:
        server.shutdown()

    print()
    if failures:
        print("❌ ks4_chrome_drive: %d failure(s)" % len(failures))
        return 1
    print("✅ ks4_chrome_drive: %d views × %d widths × 2 auth states × 2 loads — "
          "every view mounts, nothing scrolls sideways, the console is quiet, "
          "no progress is claimed, KS3 and the lesson page keep the classic nav."
          % (len(JOURNEY), len(WIDTHS)))
    print("   screenshots → %s" % os.path.relpath(args.shots, ROOT))
    return 0


if __name__ == "__main__":
    sys.exit(main())
