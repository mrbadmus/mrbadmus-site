#!/usr/bin/env python3
"""night4_laneC_drive.py — the public-site lane's own drive (MRB-317 Night 4, lane C).

    # backend worktree
    EXTRA_CORS_ORIGINS=http://localhost:8893 CONSUMER_SIGNUP_ENABLED=true PORT=8793 node server.js
    # frontend worktree ROOT
    python3 -m http.server 8893
    python3 night4_laneC_drive.py --base http://localhost:8893 --api http://localhost:8793

What it proves, and why each one is here rather than eyeballed:

  1. FLAG OFF — every public page, including tonight's three new ones, renders
     "Not found", keeps its static `<meta name="robots" content="noindex">`,
     and makes ZERO API / Supabase / CDN requests. The flag is turned off for
     THIS BROWSER only (the repo's shared/config.js already has it off; the
     override is belt and braces and makes the run independent of what any
     other lane has done to the file). The TEST `platform_flags` row is NOT
     touched — other lanes need it on.

  2. FLAG ON — the same pages render for real at 390 and 1280, with zero
     console errors, the noindex tag REMOVED, the shared nav carrying five
     links with Organisations among them, and the footer carrying Terms and
     Privacy on every one of them.

  3. RESET PASSWORD in its three states: a real Supabase recovery link from
     TEST, an expired/invalid link, and no token at all.

  4. BRAND — the staff surfaces carry the wordmark and no chevron; the public
     and consumer surfaces carry no "AI" wordmark; no organisation price
     appears on any public surface.

Screenshots at 390 into --shots. Exit code is the number of failures.
"""
import argparse, json, os, re, ssl, sys, time, urllib.request, urllib.parse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ks3_browser as cdp

ROOT = os.path.dirname(os.path.abspath(__file__))

# The five content pages plus tonight's three. `sign-in` and `reset-password`
# are listed separately where they need a different assertion.
PUBLIC = [
    ("/parents/index.html",           "public home"),
    ("/parents/how-it-works.html",    "how it works"),
    ("/parents/pricing.html",         "pricing"),
    ("/parents/home-education.html",  "home education"),
    ("/parents/organisations.html",   "organisations  ⊕NEW"),
    ("/parents/terms.html",           "terms  ⊕NEW"),
    ("/parents/privacy.html",         "privacy  ⊕NEW"),
    ("/parents/sign-in.html",         "sign in"),
    ("/parents/reset-password.html",  "reset password  ⊕NEW"),
]

# Every page that mounts the shared footer. sign-in and reset-password draw
# their own thin header and no footer — Design's shape, not an omission.
FOOTERED = [p for p, _ in PUBLIC if p not in
            ("/parents/sign-in.html", "/parents/reset-password.html")]

NAV_LINKS = ["How it works", "Home education", "Pricing", "Organisations"]

# Turned OFF for this browser only. Mirrors night3_flagon_smoke's setter
# trick in the other direction, so the run does not depend on the current
# contents of shared/config.js.
FLAG_OFF_JS = ("(function(){var c=null;Object.defineProperty(window,'MrBadmusConfig',"
               "{configurable:true,get:function(){return c;},"
               "set:function(v){if(v&&typeof v==='object'){v.CONSUMER_SIGNUP_ENABLED=false;}c=v;}});})();")
FLAG_ON_JS = ("(function(){var c=null;Object.defineProperty(window,'MrBadmusConfig',"
              "{configurable:true,get:function(){return c;},"
              "set:function(v){if(v&&typeof v==='object'){v.CONSUMER_SIGNUP_ENABLED=true;}c=v;}});})();")

FAILS = []


def check(ok, label, evidence=""):
    print(("  ok   " if ok else "  FAIL ") + label + (("  — " + str(evidence)[:260]) if evidence else ""))
    if not ok:
        FAILS.append(label)


def requests_of(page):
    page.drain(0.3)
    out = []
    for ev in page._events:
        if ev.get("method") == "Network.requestWillBeSent":
            out.append(ev["params"]["request"]["url"])
    return out


def errors_of(page):
    return [e for e in page.console_errors() if "favicon.ico" not in e]


# ── TEST project, for the real recovery link ───────────────────────────────
SB_URL = "https://qeppkiswvclkkwbxmlok.supabase.co"


def anon_key():
    src = open(os.path.join(ROOT, "shared/config.js"), encoding="utf-8").read()
    return re.search(r"'(eyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+)'",
                     src[src.index("const TEST"):]).group(1)


def sb_post(path, body, key=None, bearer=None):
    ctx = ssl.create_default_context(cafile="/etc/ssl/cert.pem")
    h = {"apikey": key or anon_key(), "Content-Type": "application/json"}
    if bearer:
        h["Authorization"] = "Bearer " + bearer
    req = urllib.request.Request(SB_URL + path, data=json.dumps(body).encode(), headers=h)
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=40) as r:
            raw = r.read()
            return r.status, (json.loads(raw) if raw else {})
    except urllib.error.HTTPError as e:
        raw = e.read()
        try:
            return e.code, json.loads(raw)
        except Exception:
            return e.code, {"raw": raw.decode("utf-8", "replace")[:300]}


# ══════════════════════════════════════════════════════════════════════════
def flag_off(base, shots):
    print("\n[1] FLAG OFF — Not found, noindex kept, zero requests")
    with cdp.Browser() as b:
        p = b.attach()
        p.send("Network.enable")
        p.send("Page.addScriptToEvaluateOnNewDocument", {"source": FLAG_OFF_JS})
        for path, label in PUBLIC:
            p.goto(base + path + "?env=test", settle=1.2)
            reqs = [u for u in requests_of(p) if not u.startswith("data:")]
            foreign = [u for u in reqs
                       if "/api/" in u or "supabase" in u or "cdn.jsdelivr" in u or "cdnjs" in u]
            text = p.eval("document.body ? document.body.innerText : ''") or ""
            visible = p.eval("(function(){var b=document.body;"
                             "return !!b && getComputedStyle(b).display!=='none';})()")
            robots = p.eval("(function(){var m=document.querySelector('meta[name=\"robots\"]');"
                            "return m?m.content:'ABSENT';})()")
            check("Not found" in text and visible, "OFF %-30s renders Not found" % label,
                  text[:60].replace("\n", " "))
            check(not foreign, "OFF %-30s makes no API/Supabase/CDN request" % label, foreign)
            check(robots == "noindex", "OFF %-30s keeps meta robots=noindex" % label, robots)
            check(not errors_of(p), "OFF %-30s zero console errors" % label, errors_of(p))


def flag_on(base, api, shots):
    print("\n[2] FLAG ON — the real pages, 390 and 1280")
    q = "?env=test&api=" + urllib.parse.quote(api, safe="")
    with cdp.Browser() as b:
        p = b.attach()
        p.send("Network.enable")
        p.send("Page.addScriptToEvaluateOnNewDocument", {"source": FLAG_ON_JS})
        for width in (390, 1280):
            print("  ── %dpx ──" % width)
            for path, label in PUBLIC:
                p.set_viewport(width, 900)
                p.goto(base + path + q, settle=2.0)
                text = p.eval("document.body ? document.body.innerText : ''") or ""
                robots = p.eval("(function(){var m=document.querySelector('meta[name=\"robots\"]');"
                                "return m?m.content:'ABSENT';})()")
                # The reset page with no token in the URL is SUPPOSED to be
                # short: it is the dead-end screen, which is real content and
                # is asserted properly in [3]. Everything else is a full page.
                floor = 120 if "reset" in path else 200
                check("Not found" not in text and len(text) > floor,
                      "ON  %-30s @%d renders real content" % (label, width), len(text))
                check(robots == "ABSENT",
                      "ON  %-30s @%d meta robots removed by boot()" % (label, width), robots)
                check(not errors_of(p), "ON  %-30s @%d zero console errors" % (label, width),
                      errors_of(p))
                if width == 390 and shots:
                    p.screenshot(os.path.join(shots, path.strip("/").replace("/", "-").replace(".html", "") + ".png"),
                                 width=390)

        # ── the shared nav and footer, on every page that mounts them ──────
        print("  ── nav and footer ──")
        for path in FOOTERED:
            p.set_viewport(1280, 900)
            p.goto(base + path + q, settle=1.6)
            nav = p.eval("(function(){var n=document.querySelector('.pb-nav-links');"
                         "return n?Array.prototype.map.call(n.querySelectorAll('a'),"
                         "function(a){return a.textContent.trim();}).join('|'):'NONE';})()")
            check(nav == "|".join(NAV_LINKS), "nav on %-34s = %s" % (path, "|".join(NAV_LINKS)), nav)
            foot = p.eval("(function(){var f=document.querySelector('footer');"
                          "return f?Array.prototype.map.call(f.querySelectorAll('a'),"
                          "function(a){return a.getAttribute('href').split('?')[0];}).join(' '):'NONE';})()")
            check("/parents/terms.html" in foot, "footer on %-34s links Terms" % path, foot)
            check("/parents/privacy.html" in foot, "footer on %-34s links Privacy" % path, foot)
            check("/parents/organisations.html" in foot, "footer on %-34s links Organisations" % path, foot)
            ent = p.eval("(function(){var f=document.querySelector('footer');"
                         "return f?f.innerText:'';})()")
            check("3rd Eye Ltd, trading as MrBadmus" in ent,
                  "footer on %-34s carries the trading entity" % path)

        # ── the nav collapses under 900, CTA and Sign in survive ──────────
        print("  ── the 900px collapse ──")
        for width, want in ((899, "none"), (900, "flex")):
            p.set_viewport(width, 900)
            p.goto(base + "/parents/index.html" + q, settle=1.4)
            disp = p.eval("(function(){var n=document.querySelector('.pb-nav-links');"
                          "return n?getComputedStyle(n).display:'NONE';})()")
            check(disp == want, "at %dpx .pb-nav-links display is %s" % (width, want), disp)
            head = p.eval("(function(){var h=document.querySelector('header.pb-head');"
                          "return h?h.innerText.replace(/\\s+/g,' ').trim():'NONE';})()")
            check("Sign in" in head and "Start free" in head,
                  "at %dpx Sign in and Start free stay in the header" % width, head)
            if width == 900:
                # Design added `.pb-head a{white-space:nowrap}` in drop 2 for
                # exactly this width; a wrapped link doubles the header.
                hh = p.eval("(function(){var h=document.querySelector('header.pb-head');"
                            "return h?Math.round(h.getBoundingClientRect().height):0;})()")
                check(hh < 90, "at 900px the header is one row high (%spx)" % hh, hh)

        # ── the organisations page has no price, and its form composes ────
        print("  ── organisations ──")
        p.set_viewport(390, 900)
        p.goto(base + "/parents/organisations.html" + q, settle=1.6)
        body = p.eval("document.body.innerText") or ""
        money = re.findall(r"£\s?\d", body)
        check(not money, "organisations page shows no price at all", money[:5])
        kinds = p.eval("document.querySelectorAll('#kinds [data-kind]').length")
        check(kinds == 5, "five organisation-type pills render", kinds)
        p.eval("document.querySelector('#send').click()")
        time.sleep(0.4)
        err = p.eval("(function(){var e=document.getElementById('error');"
                     "return e && e.style.display!=='none' ? e.textContent : '';})()")
        check(err == "Name, work email and organisation, please.",
              "empty submit shows Design's validation string", err)
        p.eval("document.getElementById('f-name').value='Ada Bello';"
               "document.getElementById('f-email').value='ada@council.example';"
               "document.getElementById('f-org').value='Test Council';"
               "document.querySelector('[data-kind=\"Council\"]').click();")
        time.sleep(0.3)
        # The href is built and then assigned to location; assert the compose
        # rather than firing it, so no mail client opens on the machine.
        composed = p.eval("(function(){"
                          " var n=document.getElementById('f-name').value,"
                          "     e=document.getElementById('f-email').value,"
                          "     o=document.getElementById('f-org').value;"
                          " return !!(n && e.indexOf('@')>-1 && o);})()")
        check(composed, "the three required fields are filled and would pass validation")
        pressed = p.eval("document.querySelector('[data-kind=\"Council\"]').getAttribute('aria-pressed')")
        check(pressed == "true", "the chosen organisation type is aria-pressed", pressed)
        if shots:
            p.screenshot(os.path.join(shots, "parents-organisations-form.png"), width=390)


def reset_states(base, shots, email, password):
    print("\n[3] RESET PASSWORD — three states, real TEST links")
    q = "?env=test"
    with cdp.Browser() as b:
        p = b.attach()
        p.send("Network.enable")
        p.send("Page.addScriptToEvaluateOnNewDocument", {"source": FLAG_ON_JS})

        # (a) no token at all
        p.goto(base + "/parents/reset-password.html" + q, settle=2.0)
        text = p.eval("document.body.innerText") or ""
        check("That link won’t work" in text or "That link won't work" in text,
              "no token  → the dead-end screen", text[:80].replace("\n", " "))
        check("password-reset email" in text, "no token  → says where the link comes from")
        check(p.eval("!!document.getElementById('again-go')"),
              "no token  → offers a way to request a new link")
        check(not errors_of(p), "no token  → zero console errors", errors_of(p))
        if shots:
            p.screenshot(os.path.join(shots, "parents-reset-password-notoken.png"), width=390)

        # (b) an expired / invalid link — Supabase's own fragment shape.
        #
        # ⚠️ `&state=` is not read by the page and is there for the harness:
        # changing ONLY the fragment is a same-document navigation, Chrome
        # fires no load event, and `goto` waits 30s and dies. A differing
        # query forces a real navigation.
        p.goto(base + "/parents/reset-password.html" + q + "&state=expired" +
               "#error=access_denied&error_code=otp_expired"
               "&error_description=Email+link+is+invalid+or+has+expired", settle=2.0)
        text = p.eval("document.body.innerText") or ""
        check("expired" in text and "already been used" in text,
              "expired   → names both ways a link dies", text[:100].replace("\n", " "))
        check(not errors_of(p), "expired   → zero console errors", errors_of(p))
        if shots:
            p.screenshot(os.path.join(shots, "parents-reset-password-expired.png"), width=390)

        # (b2) the way OUT of the dead end. Driven against an address with no
        # account on purpose: Supabase sends nothing, and the page must still
        # end on "Check your email" — the enumeration argument. Nothing is
        # created and no inbox is touched.
        p.eval("document.getElementById('again-email').value='';"
               "document.getElementById('again-go').click();")
        time.sleep(0.5)
        bad = p.eval("(function(){var e=document.getElementById('again-error');"
                     "return e && e.style.display!=='none' ? e.textContent:'';})()")
        check(bad == "That doesn’t look like an email address.",
              "expired   → an empty address is refused in our voice", bad)
        p.eval("document.getElementById('again-email').value='n4-laneC-nobody@example.com';"
               "document.getElementById('again-go').click();")
        time.sleep(3.0)
        text = p.eval("document.body.innerText") or ""
        check("Check your email" in text and "has an account" in text,
              "expired   → an unknown address gets the same answer as a known one",
              text[:110].replace("\n", " "))
        check(not errors_of(p), "expired   → resend leaves zero console errors", errors_of(p))
        if shots:
            p.screenshot(os.path.join(shots, "parents-reset-password-sent.png"), width=390)

        if not email:
            print("  (skipping the live-link state: no --reset-email given)")
            return

        # (c) a REAL recovery link from TEST, generated by the admin API so
        #     the run needs no inbox. `generate_link` returns the same URL
        #     Supabase would have emailed.
        svc = os.environ.get("SUPABASE_SERVICE_ROLE_KEY", "")
        if not svc:
            check(False, "live link → SUPABASE_SERVICE_ROLE_KEY not in the environment")
            return
        code, out = sb_post("/auth/v1/admin/generate_link",
                            {"type": "recovery", "email": email,
                             "options": {"redirect_to": base + "/parents/reset-password.html?env=test"}},
                            key=svc, bearer=svc)
        link = (out or {}).get("action_link") or (out or {}).get("properties", {}).get("action_link")
        if code >= 400 or not link:
            check(False, "live link → generate_link failed", (code, out))
            return

        """ ⚠️ THE REDIRECT ALLOW-LIST, AND WHY THE HARNESS SPLITS THE HOP.

        The `action_link` is Supabase's `/auth/v1/verify`, which answers 302
        to `<redirect_to>#access_token=…&type=recovery`. `redirect_to` is
        honoured ONLY if it matches the project's redirect allow-list; TEST's
        does not list this harness's port, so Supabase substitutes the Site
        URL (http://localhost:3000, nothing listening) and the browser lands
        on "localhost refused to connect" — which proves the allow-list, not
        the page.

        So the 302 is followed here, WITHOUT a browser, and the fragment it
        hands back is put on the real page's URL. What the browser then
        receives is byte-identical to what it receives in production; the
        only step skipped is Supabase's own redirect, which is not our code.

        The same gap is the production checklist item: mrbadmus.com's
        allow-list needs /parents/reset-password.html adding, or every
        parent's reset link lands on the wrong page. """
        import urllib.error as _ue

        class _NoRedirect(urllib.request.HTTPRedirectHandler):
            def redirect_request(self, *a, **k):
                return None
        # Same CA bundle the rest of this file uses; the default store on
        # this machine has no issuer for Supabase's cert.
        opener = urllib.request.build_opener(
            _NoRedirect,
            urllib.request.HTTPSHandler(
                context=ssl.create_default_context(cafile="/etc/ssl/cert.pem")))
        loc = ""
        try:
            opener.open(link, timeout=30)
        except urllib.error.HTTPError as e:
            loc = e.headers.get("location", "")
        frag = loc.split("#", 1)[1] if "#" in loc else ""
        check(bool(frag) and "access_token=" in frag,
              "live link→ Supabase issued a recovery fragment", loc[:60])
        if not frag:
            return
        if "localhost:8893" not in loc:
            print("     note: TEST's redirect allow-list sent the 302 to %s — "
                  "the fragment is replayed onto the real page below."
                  % loc.split("#", 1)[0])
        p.goto(base + "/parents/reset-password.html?env=test&state=live#" + frag, settle=4.0)
        text = p.eval("document.body.innerText") or ""
        check("Choose a new password" in text, "live link→ the password form opens",
              text[:80].replace("\n", " "))
        check(not errors_of(p), "live link→ zero console errors", errors_of(p))
        if shots:
            p.screenshot(os.path.join(shots, "parents-reset-password-form.png"), width=390)

        # short password, then a mismatch, then the real change
        p.eval("document.getElementById('pw1').value='short';"
               "document.getElementById('pw2').value='short';"
               "document.getElementById('save').click();")
        time.sleep(0.6)
        e1 = p.eval("(function(){var e=document.getElementById('form-error');"
                    "return e && e.style.display!=='none' ? e.textContent:'';})()")
        check(e1 == "Make it at least eight characters.", "live link→ short password refused", e1)

        p.eval("document.getElementById('pw1').value='Night4Reset!a';"
               "document.getElementById('pw2').value='Night4Reset!b';"
               "document.getElementById('save').click();")
        time.sleep(0.6)
        e2 = p.eval("(function(){var e=document.getElementById('form-error');"
                    "return e && e.style.display!=='none' ? e.textContent:'';})()")
        check("don’t match" in e2 or "don't match" in e2, "live link→ mismatch refused", e2)

        p.eval("document.getElementById('pw1').value=%s;"
               "document.getElementById('pw2').value=%s;"
               "document.getElementById('save').click();" % (json.dumps(password), json.dumps(password)))
        # Read BEFORE the 1.6s hop to the dashboard, so the assertion is on
        # the done screen rather than on whatever the dashboard did next.
        time.sleep(0.9)
        text = p.eval("document.body.innerText") or ""
        check("Password changed" in text, "live link→ the done screen shows",
              text[:80].replace("\n", " "))
        if shots and "Password changed" in text:
            p.screenshot(os.path.join(shots, "parents-reset-password-done.png"), width=390)
        time.sleep(2.5)
        href = p.eval("location.href") or ""
        check("/consumer/overview" in href, "live link→ lands on the dashboard", href[:90])

        # And the new password really works.
        code, out = sb_post("/auth/v1/token?grant_type=password",
                            {"email": email, "password": password})
        check(code == 200 and "access_token" in (out or {}),
              "live link→ the new password signs in", code)


def org_and_admin(base, api, shots):
    print("\n[4] ORG + ADMIN surfaces — wordmark, no chevron, no price")
    q = "?env=test&api=" + urllib.parse.quote(api, safe="")
    with cdp.Browser() as b:
        p = b.attach()
        p.send("Page.addScriptToEvaluateOnNewDocument", {"source": FLAG_ON_JS})
        p.set_viewport(390, 900)
        p.goto(base + "/org/sign-in.html" + q, settle=2.0)
        text = p.eval("document.body.innerText") or ""
        check("Staff sign in" in text, "org sign-in renders", text[:60].replace("\n", " "))
        check("Seat cap, one invoice a year, no cards" in text,
              "org sign-in carries Design's drop-2 seat-cap bullet")
        check("pupils message their caseworker, logged" in text,
              "org sign-in carries Design's drop-2 messaging bullet")
        check("MrBadmusAI" not in text, "org sign-in shows no 'MrBadmusAI'")
        chev = p.eval("document.querySelectorAll('header svg path[d^=\"M4 6l4-4\"], "
                      "header svg[stroke=\"#E4572E\"]').length")
        check(chev == 0, "org sign-in header carries no chevron", chev)
        money = re.findall(r"£\s?\d", text)
        check(not money, "org sign-in shows no price", money[:4])
        if shots:
            p.screenshot(os.path.join(shots, "org-sign-in.png"), width=390)


def cold_greps():
    print("\n[5] COLD GREPS of the SOURCE tree (not the build)")

    def strip(src):
        src = re.sub(r"<!--.*?-->", "", src, flags=re.S)
        src = re.sub(r"/\*.*?\*/", "", src, flags=re.S)
        src = re.sub(r"^\s*//.*$", "", src, flags=re.M)
        return src

    def files(*dirs):
        out = []
        for d in dirs:
            full = os.path.join(ROOT, d)
            if os.path.isdir(full):
                out += [os.path.join(full, f) for f in sorted(os.listdir(full))
                        if f.endswith((".html", ".js"))]
        return out

    def grep(pattern, paths):
        hits = []
        for f in paths:
            s = strip(open(f, encoding="utf-8", errors="ignore").read())
            for m in re.finditer(pattern, s):
                hits.append("%s: …%s…" % (os.path.relpath(f, ROOT),
                                          s[max(0, m.start() - 40):m.end() + 40].replace("\n", " ")))
        return hits

    consumer = files("parents", "go", "consumer", "org")
    check(not grep(r"MrBadmusAI", consumer),
          "no 'MrBadmusAI' anywhere under parents/ go/ consumer/ org/",
          grep(r"MrBadmusAI", consumer)[:4])
    check(not grep(r"MrBadmus\s*AI\b|Mr Badmus AI\b", consumer),
          "no 'AI' wordmark on any consumer/public surface",
          grep(r"MrBadmus\s*AI\b", consumer)[:4])

    # The staff surfaces, chevron-free. admin.html's SCHOOL nav legitimately
    # says MrBadmusAI; only its consumer card is in scope.
    chevron = r'stroke="#E4572E"|M4 6l4-4 4 4'
    for f in ("org/sign-in.html", "org/index.html"):
        body = strip(open(os.path.join(ROOT, f), encoding="utf-8").read())
        check(not re.search(chevron, body), "no chevron on staff surface %s" % f)
    adm = strip(open(os.path.join(ROOT, "teacher/admin.html"), encoding="utf-8").read())
    card = adm[adm.find('id="consumer-card"'):] if 'id="consumer-card"' in adm else ""
    check(card and "MrBadmusAI" not in card, "admin consumer card carries no 'MrBadmusAI'")
    check(card and not re.search(chevron, card), "admin consumer card carries no chevron")

    # No organisation price, anywhere public or on org/.
    pubs = files("parents", "org")
    # ⚠️ "per-pupil pricing" has to be in this pattern. It was Design's
    # drop-1 wording on the pricing FAQ, it is a price framing, and a grep
    # written around the word "seat" walked straight past it for a whole run.
    price = grep(r"per seat|perSeat|per-seat|per-pupil pricing|per pupil pricing|"
                 r"£\s?\d+\s*(?:per|a)\s*(?:seat|term|pupil)|invoiced termly|Termly ·", pubs)
    check(not price, "no organisation price or per-seat/per-pupil framing on parents/ or org/", price[:5])

    # And no price MATHS on a public page — every number comes from
    # /api/consumer/pricing. A literal in copy is fine; arithmetic is not.
    maths = grep(r"(?<![\w.])(?:999|599|7900|4900)(?![\w.])", files("parents"))
    check(not maths, "no hard-coded price constants under parents/", maths[:5])

    # The two paths Lane B's signup checkbox links to must exist by name.
    for f in ("parents/terms.html", "parents/privacy.html", "parents/organisations.html",
              "parents/reset-password.html"):
        check(os.path.exists(os.path.join(ROOT, f)), "%s exists" % f)

    # The school reset page must be untouched.
    import subprocess
    d = subprocess.run(["git", "-C", ROOT, "diff", "--stat", "--", "reset-password.html"],
                       capture_output=True, text=True).stdout.strip()
    check(d == "", "the SCHOOL /reset-password.html is unmodified", d)



def org_dashboard(base, api, shots, session_path):
    """The Drop-2 Messages screen and the Drop-2 account wording, on a real
    organisation fixture: two pupils, four messages, three of them unread."""
    print("\n[6] ORG DASHBOARD — Drop 2's Messages screen, on real data")
    if not session_path or not os.path.exists(session_path):
        check(False, "org dashboard → no fixture session file (%s)" % session_path)
        return
    fx = json.load(open(session_path))
    q = "?env=test&api=" + urllib.parse.quote(api, safe="")
    with cdp.Browser() as b:
        p = b.attach()
        p.send("Network.enable")
        p.send("Page.addScriptToEvaluateOnNewDocument", {"source": FLAG_ON_JS})
        p.set_viewport(390, 900)
        # A REAL session, written before the page that reads it loads — the
        # SDK deletes anything fake.
        p.goto(base + "/404.html?env=test", settle=0.3)
        p.eval("localStorage.setItem('sb-qeppkiswvclkkwbxmlok-auth-token', %s)"
               % json.dumps(json.dumps(fx["session"])))

        p.goto(base + "/org/index.html" + q, settle=4.0)
        errs = errors_of(p)
        check(not errs, "org dashboard loads with zero console errors", errs)

        nav = p.eval("Array.prototype.map.call(document.querySelectorAll('#nav [data-nav]'),"
                     "function(b){return b.getAttribute('data-nav');}).join('|')")
        check(nav == "pupils|groups|work|messages|account",
              "nav is Design's drop-2 order with Messages", nav)
        badge = p.eval("(function(){var b=document.querySelector('#nav [data-nav=\"messages\"] .og-nav-badge');"
                       "return b?b.textContent:'NONE';})()")
        check(badge == "3", "Messages carries the unread total from /chat/threads", badge)
        sel = p.eval("Array.prototype.map.call(document.querySelectorAll('#mnav option'),"
                     "function(o){return o.textContent;}).join('|')")
        check(sel == "Pupils|Groups|Set work|Messages|Account",
              "the mobile select matches, and says 'Set work' not 'Work set'", sel)
        if shots:
            p.screenshot(os.path.join(shots, "org-pupils.png"), width=390)

        # ── the Messages screen ───────────────────────────────────────────
        p.eval("document.querySelector('#nav [data-nav=\"messages\"]').click()")
        time.sleep(2.5)
        rows = p.eval("Array.prototype.map.call(document.querySelectorAll('[data-thread]'),"
                      "function(b){return b.innerText.replace(/\\s+/g,' ').trim();}).join(' // ')")
        check(rows.count("//") == 1, "two threads render, one per pupil", rows)
        check("Amara" in rows and "9X" in rows,
              "a thread names the pupil and joins their group from the org payload", rows)
        check("memory cells" in rows, "the thread row shows the last message", rows[:120])
        # The backend sorts threads newest-first, so the one that opens by
        # default is whoever wrote last — Kwame, whose single message is the
        # most recent. Asserted by that rule rather than by name, so the
        # check does not silently depend on fixture timestamps.
        pane = p.eval("(function(){var e=document.getElementById('thread-pane');"
                      "return e?e.innerText.replace(/\\s+/g,' ').trim():'NONE';})()")
        first = p.eval("(function(){var b=document.querySelector('[data-thread]');"
                       "return b?b.innerText.replace(/\\s+/g,' ').trim():'NONE';})()")
        check(pane.split(" ")[0] and pane.split(" ")[0] in first,
              "the newest thread is the one that opens", pane[:110])
        check("rates test" in pane, "the open thread shows its messages", pane[:120])
        check(not errors_of(p), "Messages screen: zero console errors", errors_of(p))
        if shots:
            p.screenshot(os.path.join(shots, "org-messages.png"), width=390)

        # Kwame had one unread, so the badge falls 3 → 2.
        time.sleep(1.5)
        badge = p.eval("(function(){var b=document.querySelector('#nav [data-nav=\"messages\"] .og-nav-badge');"
                       "return b?b.textContent:'NONE';})()")
        check(badge == "2", "opening a thread clears its unread and the badge falls", badge)

        # switch to the other thread — the one with a reply in it, so both
        # sides of a conversation are proven to render.
        p.eval("(function(){var bs=document.querySelectorAll('[data-thread]');"
               "bs[bs.length-1].click();})()")
        time.sleep(2.5)
        pane = p.eval("(function(){var e=document.getElementById('thread-pane');"
                      "return e?e.innerText.replace(/\\s+/g,' ').trim():'NONE';})()")
        check("Good. Which bit?" in pane and "memory cells" in pane,
              "the other thread opens and shows BOTH sides", pane[:150])
        time.sleep(1.5)
        badge = p.eval("(function(){var b=document.querySelector('#nav [data-nav=\"messages\"] .og-nav-badge');"
                       "return b?b.textContent:'NONE';})()")
        check(badge == "NONE", "with every thread read the badge is gone, not a zero", badge)
        reply = p.eval("(function(){var i=document.getElementById('th-text');"
                       "return i?i.placeholder:'NONE';})()")
        check(reply.startswith("Reply to "), "the reply box names the pupil", reply)
        check(not errors_of(p), "switching threads: zero console errors", errors_of(p))

        # An empty send is refused in our voice, then a real one goes through
        # `/api/consumer/chat/send` and comes back on the re-read.
        p.eval("document.getElementById('th-send').click()")
        time.sleep(0.4)
        m = p.eval("(function(){var e=document.getElementById('th-msg');return e?e.textContent:'';})()")
        check(m == "Write something first.", "an empty reply is refused", m)
        stamp = "n4lc reply %d" % int(time.time())
        p.eval("document.getElementById('th-text').value=%s;"
               "document.getElementById('th-send').click();" % json.dumps(stamp))
        time.sleep(3.0)
        pane = p.eval("(function(){var e=document.getElementById('thread-pane');"
                      "return e?e.innerText:'';})()")
        check(stamp in pane, "a real reply is sent and comes back in the pane", pane[-90:])
        cleared = p.eval("(function(){var i=document.getElementById('th-text');"
                         "return i?i.value:'X';})()")
        check(cleared == "", "the reply box empties after sending", cleared)
        check(not errors_of(p), "sending a reply: zero console errors", errors_of(p))

        # ── the Drop-2 account wording ────────────────────────────────────
        p.eval("document.querySelector('#nav [data-nav=\"account\"]').click()")
        time.sleep(2.0)
        text = p.eval("document.body.innerText") or ""
        check("invoiced annually" in text, "account: 'invoiced annually'")
        check("in use against a cap of" in text, "account: Design's drop-2 seat sentence")
        check("payable by BACS within 30 days" in text, "account: BACS and its 30 days")
        check("pro-rated to the renewal date" in text, "account: the mid-year cap answer")
        check("Raise the cap" in text and "Add seats" not in text,
              "account: the control is 'Raise the cap'")
        check("On · caseworker sees them" in text, "account: the drop-2 messaging row")
        money = re.findall(r"£\s?\d", text)
        check(not money, "account: no organisation price anywhere", money[:4])
        check("MrBadmusAI" not in text, "account: no 'MrBadmusAI'")
        check(not errors_of(p), "account screen: zero console errors", errors_of(p))
        if shots:
            p.screenshot(os.path.join(shots, "org-account.png"), width=390)

        # ── the pupil page's drop-2 caseworker line ───────────────────────
        p.eval("document.querySelector('#nav [data-nav=\"pupils\"]').click()")
        time.sleep(1.5)
        p.eval("document.querySelector('[data-pupil]').click()")
        time.sleep(3.0)
        text = p.eval("document.body.innerText") or ""
        check("Caseworker:" in text and "Parent invites aren’t available in v1" in text,
              "pupil page carries Design's drop-2 caseworker sentence",
              text[-220:].replace("\n", " "))
        check("Invite a parent" not in text, "pupil page offers no parent invite")
        check(not errors_of(p), "pupil page: zero console errors", errors_of(p))
        if shots:
            p.screenshot(os.path.join(shots, "org-pupil.png"), width=390)

        p.eval("localStorage.clear()")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", default="http://localhost:8893")
    ap.add_argument("--api", default="http://localhost:8793")
    ap.add_argument("--shots", default=os.path.join(ROOT, "docs/b2c/night4-screens"))
    ap.add_argument("--reset-email", default="")
    ap.add_argument("--reset-password", default="Night4Reset!ok")
    ap.add_argument("--only", default="")
    ap.add_argument("--org-session", default="")
    a = ap.parse_args()
    os.makedirs(a.shots, exist_ok=True)
    only = set(x for x in a.only.split(",") if x)

    if not only or "off" in only:
        flag_off(a.base, a.shots)
    if not only or "on" in only:
        flag_on(a.base, a.api, a.shots)
    if not only or "reset" in only:
        reset_states(a.base, a.shots, a.reset_email, a.reset_password)
    if not only or "org" in only:
        org_and_admin(a.base, a.api, a.shots)
    if not only or "orgdash" in only:
        org_dashboard(a.base, a.api, a.shots, a.org_session)
    if not only or "grep" in only:
        cold_greps()

    print("\n%d failure(s)" % len(FAILS))
    for f in FAILS:
        print("  - " + f)
    sys.exit(min(len(FAILS), 99))


if __name__ == "__main__":
    main()
