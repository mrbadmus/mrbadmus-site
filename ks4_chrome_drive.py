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
import re
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
    ("lesson",         "/combined/foundation/physics/energy/energy-stores-systems.html"),
]

# A phrase on one of these pages would be a progress claim with no data
# behind it. Checked against RENDERED TEXT, which is where `tells` cannot
# look: a string assembled by JS never appears in the built bytes.
PROGRESS_CLAIMS = [
    "Jump back in", "Your progress", "Your best", "Your rank", "Your tier so far",
    "Last opened", "Half finished", "Not started", "In progress", "of 7 done",
    "You are here", "Carry on",
]

# ⊕ Test isolation (5 Oct 2026) — the key of the world the page RESOLVES.
# This used to be the production project's slot: the KS4 pages loaded no
# config.js, so nav.js fell back to production and read that slot even on
# 127.0.0.1. KS4 pages now load config.js, which resolves TEST on a local
# origin, and nav.js reads TEST's slot — so the seed goes there. Read from
# config.js's TEST block rather than retyped.
def _test_session_key():
    src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "shared", "config.js"), encoding="utf-8").read()
    block = src[src.index("const TEST = {"):]
    ref = re.search(r"SUPABASE_URL:\s*'https://([a-z0-9]+)\.supabase\.co'", block).group(1)
    return "sb-%s-auth-token" % ref


SESSION_KEY = _test_session_key()

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
        # ⊕ One-mark ruling (Mide, 13 Sep 2026): the header carries the ONE
        # lockup brand.py draws — `.mrb-brand` with the kit's double chevron
        # (back chevron faded, front solid, #E4572E) and the wordmark
        # "MrBadmus" in Bricolage Grotesque 600. This used to pin Design's
        # `.nav-brand` BrandMark and the "MrBadmusAI" wordmark; every
        # property it checked is still checked, against the ruled mark, plus
        # the direction of the fade and the wordmark weight. (Byte-level
        # identity with brand.py is brand_one_mark.py's job.)
        brand = page.eval(
            "(function(){var a=document.querySelector('nav .mrb-brand');"
            "if(!a) return null;"
            "var s=a.querySelector('svg[data-mrb-mark]');"
            "var p=s?s.querySelectorAll('path'):[];"
            "return {text:a.textContent.trim(),"
            " chevrons:p.length,"
            " stroke:p.length?p[1].getAttribute('stroke'):null,"
            " backFaded:p.length?p[0].getAttribute('stroke-opacity'):null,"
            " frontFaded:p.length?p[1].getAttribute('stroke-opacity'):null,"
            " font:getComputedStyle(a).fontFamily,"
            " weight:getComputedStyle(a).fontWeight};})()")
        if not brand:
            fail("%s — no .mrb-brand lockup in the header" % label)
        else:
            if brand["text"] != "MrBadmus":
                fail("%s — brand wordmark reads %r" % (label, brand["text"]))
            if brand["chevrons"] != 2:
                fail("%s — the one mark is a DOUBLE chevron; found %d path(s)"
                     % (label, brand["chevrons"]))
            if (brand["stroke"] or "").upper() != "#E4572E":
                fail("%s — brand stroke is %r, not #E4572E" % (label, brand["stroke"]))
            if brand["backFaded"] != "0.34" or brand["frontFaded"] is not None:
                fail("%s — the back chevron must be the faded one (0.34) and the "
                     "front solid; found back=%r front=%r"
                     % (label, brand["backFaded"], brand["frontFaded"]))
            if "Bricolage" not in (brand["font"] or "") and "MrBadmus Wordmark" not in (brand["font"] or ""):
                fail("%s — brand font resolves to %r, not Bricolage Grotesque"
                     % (label, brand["font"]))
            if str(brand["weight"]) != "600":
                fail("%s — wordmark weight is %r, not 600" % (label, brand["weight"]))


def check_no_progress(page, label, signed_in):
    text = page.eval("document.body.innerText")
    for claim in PROGRESS_CLAIMS:
        if claim in text:
            fail("%s (%s) — renders the progress claim %r, and there is no "
                 "KS4 progress model behind it"
                 % (label, "signed-in" if signed_in else "signed-out", claim))


# ⊕ FRONT DOOR (12 Oct 2026) — THE BAR'S CONTRACT CHANGED, AND SO DID THIS.
# It used to assert the old cluster: the signed-in name chip ("Anifat"), the
# bar's own "Sign In" only above 900px (empty at 900px and below), "Sign In /
# Sign Up" in the drawer's auth row. The public bar is now brand · theme · ONE
# home button · hamburger at EVERY width, the account lives at the top of the
# drawer, and the home button says "Sign in" signed out at every width. The
# assertions below are the new contract and each one still fails if the bar
# regresses (a chip, a Challenge pill, a search icon, a second row, a sticky
# phone bar, a small burger):
#
#   before                                    after
#   signed out, slot "" (≤900) / "Sign In"   slot "Sign in" at every width
#   signed in, slot contains the name         slot is the home label, no name
#   drawer `#nav-drawer-auth` Sign In/Up      `#nav-drawer-account` Sign in/Sign up
#                                             signed in: "<name> · <kind>", My
#                                             profile, Switch account, Sign out
#   (no assertion on what else is in the bar) NONE of .nav-text-link,
#                                             .challenge-chip, .nav-icon-link,
#                                             .nav-class-link, #nav-profile-link,
#                                             a bell; exactly brand + theme + home
#                                             + burger
#   (no assertion on the phone bar)           ≤700px: one row, ≤56px, not sticky;
#                                             burger a 40px box, ≥44px to the finger
HOME_LABELS = ("My class", "My classes", "My dashboard", "Today")
BAR_FORBIDDEN = (".nav-text-link, .challenge-chip, .nav-icon-link, .nav-class-link, "
                 "#nav-profile-link, [data-mrb-bell], .mrb-topbar__who")
BAR_PHONE_MAX = 700
# The signed-in drive has no backend, so the profile read the map makes is
# answered here: a teacher at a school. The map then resolves kind "staff",
# whose home button reads "My classes" and whose drawer reads "Anifat · Teacher".
STUB_PROFILE_JS = r"""(function(){var of=window.fetch;
function J(b){return Promise.resolve(new Response(JSON.stringify(b),{status:200,headers:{'Content-Type':'application/json'}}));}
window.fetch=function(u,i){var s=String((u&&u.url)||u);
if(/\/rest\/v1\/profiles/.test(s))return J([{role:'teacher',first_name:'Anifat',display_name:'Anifat',school_id:'s1'}]);
if(/\/rest\/v1\/schools/.test(s))return J([{kind:'school'}]);
if(/\/rest\/v1\/(academic_years|class_members|classes)/.test(s))return J([]);
return of.apply(this,arguments);};})();"""


def check_bar_contract(page, label, width):
    """Exactly brand + theme + home + burger; and, on a phone, one slim, static row."""
    m = page.eval(
        "(function(){"
        "var bar=document.querySelector('nav.nav, header.mrb-topbar');"
        "if(!bar)return {nobar:true};"
        "var forb=bar.querySelectorAll(%s).length;"
        "var vis=function(e){var r=e.getBoundingClientRect(),cs=getComputedStyle(e);"
        "return r.width>0&&r.height>0&&cs.visibility!=='hidden'&&cs.display!=='none'};"
        "var parts={brand:bar.querySelector('.mrb-brand'),theme:bar.querySelector('.mrb-theme-slot'),"
        "home:bar.querySelector('#nav-auth-area'),burger:bar.querySelector('.nav-burger')};"
        "var missing=Object.keys(parts).filter(function(k){return !parts[k]});"
        "var tops=Object.keys(parts).filter(function(k){return parts[k]&&vis(parts[k])}).map(function(k){var r=parts[k].getBoundingClientRect();return r.top+r.height/2});"
        "var bb=bar.getBoundingClientRect(),cs=getComputedStyle(bar);"
        "var bg=parts.burger&&parts.burger.getBoundingClientRect();"
        "var af=parts.burger?getComputedStyle(parts.burger,'::after'):null;"
        "var tap=bg&&af?bg.width+2*Math.abs(parseFloat(af.top)||0):0;"
        "var links=Array.prototype.filter.call(bar.querySelectorAll('a[href],button'),function(e){return vis(e)&&!e.closest('.mrb-theme-slot')&&!e.closest('#nav-auth-area')&&!e.matches('.nav-burger')&&!e.closest('.mrb-brand')&&!e.closest('.nav-crumbs')&&!e.matches('.mrb-brand,.mrb-topbar__title')}).map(function(e){return (e.className||e.tagName)+':'+(e.textContent||'').trim().slice(0,20)});"
        "return {forb:forb,missing:missing,spread:tops.length?Math.max.apply(0,tops)-Math.min.apply(0,tops):0,"
        "h:bb.height,pos:cs.position,bw:bg&&bg.width,bh:bg&&bg.height,tap:tap,links:links};})()" % json.dumps(BAR_FORBIDDEN))
    if m.get("nobar"):
        fail("%s — no public bar on the page" % label)
        return
    if m["forb"]:
        fail("%s — the bar still carries a retired control (3D Studio / Challenge / "
             "Leaderboard / Search / name chip / bell): %d found" % (label, m["forb"]))
    if m["missing"]:
        fail("%s — the bar is missing %s" % (label, ", ".join(m["missing"])))
    if m["links"]:
        fail("%s — the bar holds more than brand + theme + home + burger: %s"
             % (label, m["links"]))
    if width <= BAR_PHONE_MAX:
        if m["h"] > 56.5:
            fail("%s — the phone bar is %.0fpx tall, over the 56px ceiling" % (label, m["h"]))
        if m["spread"] > 10:
            fail("%s — the phone bar wraps: its parts sit %.0fpx apart vertically" % (label, m["spread"]))
        if m["pos"] in ("sticky", "fixed"):
            fail("%s — the phone bar is %s; it must scroll away" % (label, m["pos"]))
    elif m["pos"] != "sticky" and "mrb-topbar" not in (page.eval(
            "(document.querySelector('nav.nav, header.mrb-topbar')||{}).className") or ""):
        fail("%s — the desktop bar is %s, expected sticky (unchanged)" % (label, m["pos"]))
    if m["bw"] is not None and (abs(m["bw"] - 40) > 0.6 or abs(m["bh"] - 40) > 0.6):
        fail("%s — the burger is %.0f×%.0f, expected a 40px box" % (label, m["bw"], m["bh"]))
    if m["tap"] < 44:
        fail("%s — the burger's tap area is %.0fpx, under 44" % (label, m["tap"]))


def check_auth_chip(page, label, signed_in, has_slot=True, width=None):
    """The home button and the drawer's account section, where shared/nav.js puts them."""
    if not has_slot:
        return
    got = page.eval(
        "(function(){var a=document.getElementById('nav-auth-area');"
        "return a? a.innerText.replace(/\\s+/g,' ').trim() : null;})()")
    # the drawer is built once nav.js boots; give the map's answer a moment
    page.eval("new Promise(function(r){setTimeout(r,400)})")
    acct = page.eval(
        "(function(){var d=document.getElementById('nav-drawer-account');"
        "return d? d.innerText.replace(/\\s+/g,' ').trim() : null;})()")
    if got is None:
        fail("%s — no #nav-auth-area on the page at all" % label)
        return
    if signed_in:
        for _ in range(10):
            if got in HOME_LABELS:
                break
            page.eval("new Promise(function(r){setTimeout(r,300)})")
            got = page.eval("(document.getElementById('nav-auth-area')||{}).innerText||''").strip()
        if got != "My classes":
            fail("%s — signed in as a teacher, the home button reads %r, expected 'My classes'"
                 % (label, got))
        acct = page.eval(
            "(document.getElementById('nav-drawer-account')||{}).innerText||''")
        acct = " ".join(acct.split())
        for want in ("Anifat · Teacher", "My profile", "Switch account", "Sign out"):
            if want not in acct:
                fail("%s — signed in, the drawer's account section lacks %r (%r)"
                     % (label, want, acct))
        if "Sign in" in acct or "Sign up" in acct:
            fail("%s — signed in, the drawer still offers Sign in/up (%r)" % (label, acct))
    else:
        if got != "Sign in":
            fail("%s — signed out, the bar's home button reads %r, expected 'Sign in' "
                 "at every width" % (label, got))
        if acct is None or "Sign in" not in acct or "Sign up" not in acct:
            fail("%s — signed out, the drawer's account section is not Sign in / Sign up (%r)"
                 % (label, acct))
    if width is not None:
        check_bar_contract(page, label, width)


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
    # ⚠️ DEFAULTS OUTSIDE THE REPO, and that is not tidiness.
    #
    # This wrote into `docs/redesign/mrb-301-shots/` at first. Those PNGs are
    # committed, and a screenshot is not byte-deterministic — font rasterising
    # and layout timing move a few bytes between runs. So recording this
    # gate's own receipt DIRTIED THE TREE, and prepush_gate correctly refused
    # to record the eight gates behind it: "a receipt attests a gate against a
    # TREE; with the tree moving under it, it would attest nothing."
    #
    # A gate must not modify what it is attesting. The reviewed screenshots
    # stay committed under docs/; a plain run writes to scratch and leaves the
    # tree exactly as it found it. Pass --shots to refresh the committed set
    # deliberately.
    ap.add_argument("--shots", default=os.path.join(
        os.environ.get("KS3_GATE_TMP") or "/tmp", "mrb-301-shots"))
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
                    page.send("Page.addScriptToEvaluateOnNewDocument", {"source": STUB_PROFILE_JS})
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
                                        signed_in, has_slot=True,
                                        width=width)
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
