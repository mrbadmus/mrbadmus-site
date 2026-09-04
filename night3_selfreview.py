#!/usr/bin/env python3
"""night3_selfreview.py — the commander's own pass over the BUILT site (MRB-317/318 §9).

    python3 night3_selfreview.py --site mrbadmus_site --api http://localhost:3120 [--shots DIR]

Three things the lane drives cannot prove, because each lane drives its own pages
from the repo root with the flag on:

  1. FLAG OFF ⇒ every consumer / public-consumer page is "Not found" and makes
     ZERO requests beyond itself and its stylesheets. Driven on the BUILT tree
     (mrbadmus_site/, whose shared/config.js has both flags false) with CDP's
     Network domain recording every request.
  2. RAINFORD REGRESSION on the built tree with the flag off: teacher landing,
     today, admin (consumer card absent, no /api/consumer request), the student
     class page, the leaderboard — zero console errors, and the leaderboard's
     rendered row count recorded.
  3. COLD GREPS of the built tree: "MrBadmusAI" and the chevron on staff/admin
     surfaces, leftover mock constants, any "AI" wordmark on consumer surfaces.

Screenshots go OUTSIDE the repo by default (a gate must not write into the tree
it attests). Exit code is the number of failures.
"""
import argparse, json, os, re, ssl, sys, time, urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ks3_browser as cdp

CONSUMER_PAGES = [
    "/parents/index.html", "/parents/how-it-works.html", "/parents/pricing.html",
    "/parents/home-education.html", "/parents/sign-in.html",
    # ⊕ MRB-321 Night 4. Four pages Night 3 did not have. They are listed here
    # because a flag gate that does not name a page cannot fail for it: a new
    # public page that forgot the boot()/Not-found mechanism would have shipped
    # readable with the flag off, and this harness would still have exited 0.
    "/parents/terms.html", "/parents/privacy.html",
    "/parents/organisations.html", "/parents/reset-password.html",
    "/go/index.html",
    "/consumer/signup.html", "/consumer/verify.html", "/consumer/checkout-return.html",
    "/consumer/overview.html", "/consumer/account.html", "/consumer/report.html",
    "/consumer/today.html", "/consumer/exam.html", "/consumer/unit-check.html",
    "/org/sign-in.html", "/org/index.html",
]
RAINFORD_PAGES = [
    ("teacher landing", "/teacher/classes.html", "hz_amy@test.mrbadmus"),
    ("teacher today", "/teacher/today.html", "hz_amy@test.mrbadmus"),
    ("admin (consumer card must be absent)", "/teacher/admin.html", "hz_admin@test.mrbadmus"),
    ("student class page", "/student/class.html", "hz_s1@test.mrbadmus"),
    ("leaderboard", "/leaderboard.html", "hz_s1@test.mrbadmus"),
]
STAFF_SURFACES = ["org/sign-in.html", "org/index.html", "teacher/admin.html"]
CONSUMER_TREES = ["parents", "go", "consumer", "org"]

FAILS = []
def check(ok, label, evidence=""):
    print(("  ✓ " if ok else "  ✗ ") + label + (("  — " + str(evidence)[:300]) if evidence else ""))
    if not ok:
        FAILS.append(label)

def anon_key():
    src = open("shared/config.js", encoding="utf-8").read()
    return re.search(r"'(eyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+)'", src[src.index("const TEST"):]).group(1)

SB_URL = "https://qeppkiswvclkkwbxmlok.supabase.co"
def sign_in(email, password):
    ctx = ssl.create_default_context(cafile="/etc/ssl/cert.pem")
    req = urllib.request.Request(SB_URL + "/auth/v1/token?grant_type=password",
                                 data=json.dumps({"email": email, "password": password}).encode(),
                                 headers={"apikey": anon_key(), "Content-Type": "application/json"})
    with urllib.request.urlopen(req, context=ctx, timeout=30) as r:
        return json.loads(r.read())

def requests_of(page):
    page.drain(0.3)
    out = []
    for ev in page._events:
        if ev.get("method") == "Network.requestWillBeSent":
            out.append(ev["params"]["request"]["url"])
    return out

def flag_off_sweep(base, shots):
    print("\n[1] FLAG OFF — every consumer page is Not found with zero foreign requests")
    with cdp.Browser() as b:
        p = b.attach()
        p.send("Network.enable")
        for path in CONSUMER_PAGES:
            url = base + path + "?env=test"
            p.goto(url)
            reqs = [u for u in requests_of(p) if not u.startswith("data:")]
            def own(u):
                bare = u.split("?", 1)[0]
                return (bare.startswith(base + path) or (bare.startswith(base) and (bare.endswith(".css") or bare.endswith(".js")
                        or "/shared/fonts/" in bare or bare.endswith("favicon.ico"))))
            foreign = [u for u in reqs if not own(u)]
            api = [u for u in reqs if "/api/" in u or "supabase" in u or "cdn.jsdelivr" in u or "cdnjs" in u]
            text = p.eval("document.body ? document.body.innerText : ''") or ""
            nf = "Not found" in text
            visible = p.eval("(function(){var b=document.body;return b && getComputedStyle(b).display!=='none';})()")
            check(nf and visible, "%s renders Not found" % path, text[:80].replace("\n", " "))
            check(not api, "%s makes no API/Supabase/CDN request" % path, api)
            check(not foreign, "%s loads only itself, CSS, fonts and its own scripts" % path, foreign)
            errs = [e for e in p.console_errors() if "favicon.ico" not in e]
            check(not errs, "%s has zero console errors" % path, errs)
            if shots:
                p.screenshot(os.path.join(shots, "off-" + path.strip("/").replace("/", "-") + ".png"), width=390)

def rainford(base, api, shots, passwords):
    print("\n[2] RAINFORD REGRESSION on the built tree, flag off")
    with cdp.Browser() as b:
        p = b.attach()
        p.send("Network.enable")
        for label, path, email in RAINFORD_PAGES:
            pw = passwords.get(email)
            if not pw:
                check(False, "%s — no password known for %s" % (label, email)); continue
            try:
                sess = sign_in(email, pw)
            except Exception as e:
                check(False, "%s — sign-in failed for %s" % (label, email), e); continue
            p.goto(base + "/404.html?env=test", settle=0.2)
            p.eval("localStorage.setItem('sb-qeppkiswvclkkwbxmlok-auth-token', %s)" % json.dumps(json.dumps(sess)))
            p.goto(base + path + "?env=test&api=" + api, settle=2.5)
            reqs = requests_of(p)
            consumer_reqs = [u for u in reqs if "/api/consumer/" in u]
            errs = [e for e in p.console_errors() if "favicon.ico" not in e]
            check(not errs, "%s: zero console errors" % label, errs)
            check(not consumer_reqs, "%s: no /api/consumer request" % label, consumer_reqs)
            if "admin" in path:
                card = p.eval("(function(){var c=document.getElementById('consumer-card');return c?getComputedStyle(c).display:'absent';})()")
                check(card in ("none", "absent"), "admin: consumer card hidden", card)
            if "leaderboard" in path:
                rows = p.eval("document.querySelectorAll('[data-rank], .lb-row, tbody tr').length")
                print("     leaderboard rendered rows: %s" % rows)
            if shots:
                p.screenshot(os.path.join(shots, "rainford-" + path.strip("/").replace("/", "-") + ".png"), width=390)
            p.eval("localStorage.clear()")

def cold_greps(site):
    print("\n[3] COLD GREPS of the built tree")
    def strip_comments(src):
        # A word in a comment is documentation, not a wordmark. Rendered
        # text is what the greps are about.
        src = re.sub(r"<!--.*?-->", "", src, flags=re.S)
        src = re.sub(r"/\*.*?\*/", "", src, flags=re.S)
        src = re.sub(r"^\s*//.*$", "", src, flags=re.M)
        return src
    def grep(pattern, files):
        hits = []
        for f in files:
            try:
                s = strip_comments(open(f, encoding="utf-8", errors="ignore").read())
            except OSError:
                continue
            for m in re.finditer(pattern, s):
                hits.append("%s: …%s…" % (os.path.relpath(f, site), s[max(0, m.start()-40):m.end()+40].replace("\n", " ")))
        return hits
    consumer_files = []
    for t in CONSUMER_TREES:
        d = os.path.join(site, t)
        if os.path.isdir(d):
            consumer_files += [os.path.join(d, f) for f in os.listdir(d) if f.endswith((".html", ".js"))]
    admin = os.path.join(site, "teacher", "admin.html")
    check(not grep(r"MrBadmusAI", consumer_files), "no 'MrBadmusAI' under parents/ go/ consumer/ org/", grep(r"MrBadmusAI", consumer_files)[:5])
    # The admin page's school nav legitimately says MrBadmusAI; the consumer card must not.
    adm = strip_comments(open(admin, encoding="utf-8").read())
    card = adm[adm.find('id="consumer-card"'):] if 'id="consumer-card"' in adm else ""
    check("MrBadmusAI" not in card, "admin consumer card carries no 'MrBadmusAI'")
    chevron = r'stroke="#E4572E"'
    for f in STAFF_SURFACES:
        path = os.path.join(site, f)
        body = open(path, encoding="utf-8").read() if os.path.exists(path) else ""
        if f == "teacher/admin.html":
            body = card
        check(chevron not in body, "no chevron on staff surface %s" % f)
    # ⊕ MRB-321. "Brookfield" stopped being proof of a leftover fixture when
    # Design's Drop 2 Organisations page shipped `placeholder="e.g. Brookfield
    # Tuition Centre"` — her own hint text on the Organisation field, which a
    # visitor is MEANT to see. The bare-name patterns are therefore matched
    # everywhere EXCEPT inside a placeholder attribute; the `const X = [`
    # mock-array patterns stay global, because a mock array is never legitimate
    # on a shipped page no matter where it sits.
    mocks = grep(r"const (ACCOUNTS|CHILDREN|QUESTIONS|ACCTS|PUPILS|MESSAGES|REPORT|EMAILS|GROUPS|ORG|QUEUE) = \[", consumer_files + [admin])
    names = grep(r"amara-rockets|Funmi|Brookfield", consumer_files + [admin])
    names = [h for h in names if not re.search(
        r'placeholder="[^"]*(amara-rockets|Funmi|Brookfield)', h)]
    mocks = mocks + names
    check(not mocks, "no leftover Design mock constants / fixture names", mocks[:8])
    ai_wordmark = grep(r"MrBadmus\s*AI\b|Mr Badmus AI\b", consumer_files)
    check(not ai_wordmark, "no 'AI' wordmark on consumer surfaces", ai_wordmark[:5])
    price_consts = grep(r"9\.99|5\.99|\b79\b.*\b49\b", consumer_files)
    price_consts = [h for h in price_consts if "pricing" not in h.lower()[:0]]
    print("     hard-coded price mentions (should be copy only, never maths): %d" % len(price_consts))
    for h in price_consts[:12]:
        print("       " + h)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--site", default="mrbadmus_site")
    ap.add_argument("--api", default="http://localhost:3120")
    ap.add_argument("--shots", default=os.path.join(os.environ.get("TMPDIR", "/tmp"), "night3-selfreview"))
    ap.add_argument("--port", type=int, default=5500, help="static port; 5500 is in the backend CORS allowlist, and the estate pages ping /api/health on the PROD backend, whose allowlist is fixed")
    ap.add_argument("--skip-rainford", action="store_true")
    a = ap.parse_args()
    os.makedirs(a.shots, exist_ok=True)
    server, port = cdp.serve(os.path.abspath(a.site), a.port)
    base = "http://localhost:%d" % port
    print("serving %s at %s" % (a.site, base))
    try:
        flag_off_sweep(base, a.shots)
        if not a.skip_rainford:
            pw = {
                "hz_amy@test.mrbadmus": os.environ.get("HZ_TEACHER_PW", "mrb293-drive-only"),
                "hz_admin@test.mrbadmus": os.environ.get("HZ_ADMIN_PW", "Night3!Admin"),
                "hz_s1@test.mrbadmus": os.environ.get("HZ_STUDENT_PW", ""),
            }
            rainford(base, a.api, a.shots, pw)
        cold_greps(os.path.abspath(a.site))
    finally:
        server.shutdown()
    print("\n%d failure(s)" % len(FAILS))
    for f in FAILS:
        print("  - " + f)
    sys.exit(min(len(FAILS), 99))

if __name__ == "__main__":
    main()
