#!/usr/bin/env python3
"""
mrb348_student_equiv.py — the student class page renders the SAME PAGE after
the load-order change as before it.

    MRB_TEST_TEACHER_PASSWORD=… python3 mrb348_student_equiv.py --capture new
    MRB_TEST_TEACHER_PASSWORD=… python3 mrb348_student_equiv.py --capture old
    python3 mrb348_student_equiv.py --compare

WHY A DRIVE AND NOT `student_behaviour`

`student_behaviour.py` is green on this change and cannot have been anything
else: it drives `student/class-fixture.html`, whose data is BAKED IN by
`build_student_port.py`. MRB-348 changes when the page's reads leave and which
class it speculates on — neither of which a fixture with no network exercises.
A gate that passes without looking is not evidence, and CLAUDE.md's own note
about `student_parity` not watching the ported page is the same lesson.

So this signs in as real students on TEST, loads the real page, and compares
the rendered TEXT and the CONTROL set, which is the same bar
`student_behaviour` holds the fixture to.

THE THREE CASES, and the third is the one that matters

  1. KS3, own class named in `?class=`      — the ordinary journey
  2. KS4, own class named in `?class=`      — the longest work list on TEST
  3. KS3 student, ANOTHER student's class id in `?class=` — the RULED path
     (23 Aug 2026): the student is shown THEIR OWN class, silently, with the
     parameter dropped from the address. No banner, no message. This is the
     behaviour the speculative build could plausibly break, because it is the
     one case where the speculation must be thrown away unused — so it is
     asserted explicitly, including the final URL.

⊕ MRB-348 ROUND THREE — A FOURTH CASE: PRACTICE FORCED TO FAIL

    MRB_TEST_TEACHER_PASSWORD=… python3 mrb348_student_equiv.py --capture down-old
    MRB_TEST_TEACHER_PASSWORD=… python3 mrb348_student_equiv.py --capture down-new
    python3 mrb348_student_equiv.py --compare-down

`/api/class/practice` used to be one unguarded arm of `buildClass`'s opening
`Promise.all`, so its failure was the whole page — a child saw "We could not
load your class just now" instead of their homework, to protect a panel below
the fold behind a toggle.

⚠️ THE FAILURE IS REAL, NOT SIMULATED. Nothing in the page's own code is
edited and no flag is set. A one-file reverse proxy stands in front of the
local backend on :3100, answers `503` to `/api/class/practice` and ONLY to
that path, and proxies every other route through untouched; the page is
pointed at it with `?api=`, the localhost-only override `shared/config.js`
already carries. So the route genuinely fails at the network, exactly as a
Render blip makes it fail.

`--compare-down` asserts the two halves of the fix:

  · `down-old`  — the page NEVER MOUNTS. This is the defect, reproduced.
  · `down-new`  — the page mounts, and its WORK is byte-identical to the
                  healthy `new` capture's. Only the practice-fed surfaces may
                  differ, and what differs is printed rather than asserted
                  away, so a reader can see the size of the degradation.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import ssl
import sys
import time
import urllib.error
import urllib.request

REPO = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, REPO)
os.chdir(REPO)

import ks3_browser as cdp  # noqa: E402

TEST_REF = "qeppkiswvclkkwbxmlok"
URL = "https://%s.supabase.co" % TEST_REF
CTX = ssl.create_default_context(cafile="/etc/ssl/cert.pem")
PORT = 5537
OUT = os.environ.get("MRB_SHOTS") or os.path.expanduser("~/tmp/ks3-gates")

KS3_CLASS = "2a000000-0000-0000-0000-000000000001"   # 8X1, Aiden's
KS4_CLASS = "2a000000-0000-0000-0000-000000000002"   # 10A, Hannah's

CASES = [
    dict(key="ks3-own", who="aiden.cole@test-rainford.local",
         q="?class=" + KS3_CLASS,
         expect_param=KS3_CLASS,
         note="KS3 8X1, the student's own class"),
    dict(key="ks4-own", who="hannah.patel@test-rainford.local",
         q="?class=" + KS4_CLASS,
         expect_param=KS4_CLASS,
         note="KS4 10A, the student's own class"),
    dict(key="ks3-foreign", who="aiden.cole@test-rainford.local",
         q="?class=" + KS4_CLASS,
         expect_param=None,
         note="RULED: a class that is NOT this student's — own class, "
              "parameter dropped, nothing said"),
]


# ── the forced failure: a proxy that breaks ONE route ───────────────────
#
# ⚠️ IT BREAKS EXACTLY ONE PATH. Everything else — the current assignment, the
# submissions, the notifications — is proxied through to the real local
# backend byte for byte, because a proof that the page survives "the backend
# is down" would prove nothing about the arm this ticket is about.
BACKEND = "http://127.0.0.1:3000"
PROXY_PORT = 3100
BROKEN = "/api/class/practice"
# ⊕ the SLOW mode's stall, in seconds. Long enough that a page which mounts
# before it cannot have waited for it, short enough to keep the probe quick.
SLOW_SECONDS = 3.0


def start_broken_proxy(mode="fail"):
    """mode="fail" → 503 on BROKEN. mode="slow" → answer it, SLOW_SECONDS late."""
    import http.server
    import socketserver

    class H(http.server.BaseHTTPRequestHandler):
        protocol_version = "HTTP/1.1"

        def log_message(self, *a):        # quiet
            pass

        def _cors(self):
            self.send_header("Access-Control-Allow-Origin", "*")
            self.send_header("Access-Control-Allow-Headers", "*")
            self.send_header("Access-Control-Allow-Methods",
                             "GET,POST,PATCH,PUT,DELETE,OPTIONS")
            # ⚠️ `Date` MUST BE EXPOSED, and the backend's own CORS config
            # exposes it (`exposedHeaders: ['Date', 'Content-Disposition']`)
            # for a load-bearing reason: `api()` reads `res.headers.get('date')`
            # to set `serverNow`, and `buildClass` throws "no server clock on
            # the response" without it. `Date` is NOT a CORS-safelisted
            # response header, so a proxy that forgets this line kills the page
            # — which is a second way for this harness to report a false red.
            self.send_header("Access-Control-Expose-Headers",
                             "Date, Content-Disposition")

        def _broken(self):
            return self.path.split("?")[0] == BROKEN

        def _serve(self):
            if self._broken() and mode == "slow" and self.command != "OPTIONS":
                time.sleep(SLOW_SECONDS)          # answered, just late
            if self._broken() and mode == "fail":
                if self.command == "OPTIONS":
                    self.send_response(204)
                    self._cors()
                    self.send_header("Content-Length", "0")
                    self.end_headers()
                    return
                body = b'{"error":"forced failure (MRB-348 round three)"}'
                self.send_response(503)
                self._cors()
                self.send_header("Content-Type", "application/json")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)
                return
            n = int(self.headers.get("Content-Length") or 0)
            payload = self.rfile.read(n) if n else None
            req = urllib.request.Request(
                BACKEND + self.path, data=payload, method=self.command)
            for k, v in self.headers.items():
                if k.lower() in ("host", "content-length", "connection"):
                    continue
                req.add_header(k, v)
            try:
                with urllib.request.urlopen(req, timeout=60) as up:
                    data, code, hdrs = up.read(), up.status, up.headers
            except urllib.error.HTTPError as e:
                data, code, hdrs = e.read(), e.code, e.headers
            except Exception as e:                      # backend not running
                data = json.dumps({"error": str(e)}).encode()
                code, hdrs = 502, {}
            # ⚠️ `Date` IS NOT COPIED, AND THAT IS NOT A DETAIL.
            # `BaseHTTPRequestHandler.send_response` emits its own `Date`, so
            # copying the backend's too gives the response TWO — and
            # `res.headers.get('date')` then returns them comma-joined,
            # `Date.parse` returns NaN, `serverNow` is never set, and
            # `buildClass` throws "no server clock on the response". The page
            # dies for a reason that has nothing to do with what is being
            # tested, and the harness reports the fix as broken. It did.
            # ⚠️ THE CORS HEADERS ARE THIS PROXY'S OWN, NOT THE BACKEND'S,
            # and copying them was a harness defect that cost a false red.
            # Forwarding only `Access-Control-Allow-Origin` and dropping
            # `-Allow-Headers` made Chrome refuse the PREFLIGHT for
            # `current-assignment` ("request header field authorization is not
            # allowed"), so the CRITICAL arm failed and the page died — which
            # looks exactly like the fix not working. One permissive set,
            # emitted here, for every response: the page authenticates with a
            # bearer header and no cookie, so `*` costs nothing.
            self.send_response(code)
            v = hdrs.get("Content-Type") if hasattr(hdrs, "get") else None
            if v:
                self.send_header("Content-Type", v)
            self._cors()
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)

        do_GET = do_POST = do_PATCH = do_PUT = do_DELETE = do_OPTIONS = _serve

    class S(socketserver.ThreadingTCPServer):
        allow_reuse_address = True
        daemon_threads = True

    import threading
    srv = S(("127.0.0.1", PROXY_PORT), H)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv


def anon_key():
    src = open("shared/config.js", encoding="utf-8").read()
    return re.search(r"'(eyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+)'",
                     src[src.index("const TEST"):]).group(1)


def sign_in(email, key, pw):
    req = urllib.request.Request(
        URL + "/auth/v1/token?grant_type=password",
        data=json.dumps({"email": email, "password": pw}).encode(),
        headers={"apikey": key, "Content-Type": "application/json"},
        method="POST")
    return json.load(urllib.request.urlopen(req, timeout=30, context=CTX))


def put_session(page, base, sess):
    payload = json.dumps({
        "access_token": sess["access_token"],
        "refresh_token": sess.get("refresh_token", ""),
        "expires_at": int(time.time()) + int(sess.get("expires_in", 3600)),
        "expires_in": int(sess.get("expires_in", 3600)),
        "token_type": "bearer", "user": sess["user"],
    })
    page.goto(base + "/student/class.html", settle=0.2)
    page.eval("localStorage.setItem(%s, %s)"
              % (json.dumps("sb-%s-auth-token" % TEST_REF), json.dumps(payload)))


READY = """(function(){
    var h = document.querySelector('[data-port-region], #mrb-student, main');
    if (!h) { return false; }
    if (document.querySelector('.skeleton, [data-skeleton]')) { return false; }
    return (h.textContent||'').trim().length > 80;
})()"""

# Visible text and the control set — the same two things `student_behaviour`
# compares, so a difference here means the same kind of difference it would
# have caught had it been able to see this page.
SNAP = """(function(){
    var h = document.querySelector('[data-port-region], #mrb-student, main')
            || document.body;
    var txt = (h.innerText || h.textContent || '')
              .replace(/\\s+/g, ' ').trim();
    var ctl = [];
    var nodes = h.querySelectorAll(
        'button, a, input, select, textarea, [role=button], [tabindex]');
    for (var i = 0; i < nodes.length; i++) {
        var n = nodes[i];
        ctl.push((n.tagName || '') + '|' +
                 ((n.innerText || n.value || n.getAttribute('aria-label') || '')
                   .replace(/\\s+/g,' ').trim().slice(0, 60)));
    }
    return { text: txt, controls: ctl, nodes: h.querySelectorAll('*').length,
             url: window.location.search };
})()"""


def capture(tag, pw):
    """
    ⚠️ A WARM-UP LOAD PER CASE, AND IT IS NOT OPTIONAL.

    Auto-composition is LAZY: the weekly assignment is composed by the backend
    on the FIRST class-page read of the week, not by a cron. So the first load
    of a class CREATES a piece of work that every later load then sees.

    Run without this, the two captures are not comparable and the difference
    is spectacular and entirely false: whichever side ran FIRST composed the
    assignment, and the side that ran SECOND reported one extra piece of work,
    a different `COMPLETED n/m`, and an extra filter button. It read exactly
    like a real regression in the load path — `COMPLETED 4/5` against
    `COMPLETED 4/4`, a whole `TO DO 1` gone — and it was the harness.

    One discarded load per case first, then the measured one. Both sides then
    observe the same composed world.
    """
    key = anon_key()
    server, port = cdp.serve("mrbadmus_site", PORT)
    base = "http://127.0.0.1:%d" % port
    snaps, who = {}, None
    try:
        with cdp.Browser() as b:
            page = b.attach()
            for c in CASES:
                if c["who"] != who:
                    put_session(page, base, sign_in(c["who"], key, pw))
                    who = c["who"]
                # The discarded warm-up. See the note above: it is what makes
                # the two captures describe the same world.
                page.goto(base + "/student/class.html" + c["q"], settle=0.3)
                warm = time.time() + 40
                while time.time() < warm:
                    try:
                        if page.eval(READY, timeout=5) is True:
                            break
                    except Exception:
                        pass
                    time.sleep(0.08)

                page.goto(base + "/student/class.html" + c["q"], settle=0.3)
                end = time.time() + 40
                ok = False
                while time.time() < end:
                    try:
                        if page.eval(READY, timeout=5) is True:
                            ok = True
                            break
                    except Exception:
                        pass
                    time.sleep(0.08)
                if not ok:
                    snaps[c["key"]] = {"error": "never mounted"}
                    print("  ❌ %-13s never mounted" % c["key"])
                    continue
                time.sleep(0.6)          # let any post-mount work settle
                s = page.eval(SNAP, timeout=15)
                snaps[c["key"]] = s
                print("  ✅ %-13s %6d chars, %3d controls, %4d nodes, url=%r"
                      % (c["key"], len(s["text"]), len(s["controls"]),
                         s["nodes"], s["url"]))
    finally:
        try:
            server.shutdown()
        except Exception:
            pass
    os.makedirs(OUT, exist_ok=True)
    path = os.path.join(OUT, "mrb348_student_%s.json" % tag)
    with open(path, "w") as fh:
        json.dump(snaps, fh, indent=2)
    print("  wrote %s" % path)
    return snaps


# ── the forced-failure capture ──────────────────────────────────────────
#
# `MOUNTED` is not `READY`. `READY` counts characters, and the failure card —
# "We could not load your class just now" plus its back link — is comfortably
# over eighty of them, so READY passes on the very page this case exists to
# catch (the trap `docs/mrb348/REPORT.md` §0 records). `data-mrb-renders` is
# written by `student-runtime.js` `draw()` and by nothing else, so it is the
# one signal that says THE RUNTIME DREW rather than THE HOST HAS TEXT IN IT.
MOUNTED = """(function(){
    var h = document.querySelector('#mrb-student[data-mrb-renders]');
    return !!h && (h.textContent||'').trim().length > 80;
})()"""

DEAD = """(function(){
    var h = document.querySelector('#mrb-student') || document.body;
    return /could not load|try again|check again/i.test(h.textContent||'');
})()"""


def capture_down(tag, pw):
    """One case, one class, one broken route — see the module docstring."""
    key = anon_key()
    proxy = start_broken_proxy()
    server, port = cdp.serve("mrbadmus_site", PORT)
    base = "http://127.0.0.1:%d" % port
    c = CASES[0]                       # KS3, the student's own class
    q = c["q"] + "&api=http://127.0.0.1:%d" % PROXY_PORT
    out = {}
    try:
        with cdp.Browser() as b:
            page = b.attach()
            put_session(page, base, sign_in(c["who"], key, pw))
            # The same discarded warm-up the three healthy cases take, and for
            # the same reason: auto-composition is lazy. It is driven through
            # the HEALTHY backend so the world both sides observe is the world
            # the healthy capture composed.
            page.goto(base + "/student/class.html" + c["q"], settle=0.3)
            warm = time.time() + 40
            while time.time() < warm:
                try:
                    if page.eval(READY, timeout=5) is True:
                        break
                except Exception:
                    pass
                time.sleep(0.08)

            page.goto(base + "/student/class.html" + q, settle=0.3)
            end, mounted = time.time() + 90, False
            while time.time() < end:
                try:
                    if page.eval(MOUNTED, timeout=5) is True:
                        mounted = True
                        break
                except Exception:
                    pass
                time.sleep(0.1)
            time.sleep(1.5)            # let the fold-in land, or not
            try:
                dead = page.eval(DEAD, timeout=15) is True
            except Exception:
                dead = False
            snap = {"mounted": mounted, "dead": dead}
            if mounted:
                snap.update(page.eval(SNAP, timeout=15))
            out["ks3-practice-down"] = snap
            print("  %s ks3-practice-down  mounted=%s  failure-card=%s"
                  % ("✅" if mounted else "❌", mounted, dead))
            if mounted:
                print("     %6d chars, %3d controls, %4d nodes"
                      % (len(snap.get("text", "")),
                         len(snap.get("controls", [])), snap.get("nodes", 0)))
    finally:
        for stop in (lambda: server.shutdown(), lambda: proxy.shutdown()):
            try:
                stop()
            except Exception:
                pass
    os.makedirs(OUT, exist_ok=True)
    path = os.path.join(OUT, "mrb348_student_%s.json" % tag)
    with open(path, "w") as fh:
        json.dump(out, fh, indent=2)
    print("  wrote %s" % path)
    return out


# The surfaces `/api/class/practice` feeds, and the ONLY ones allowed to
# differ when it is down. Everything else on the page — the work, the docket,
# the bench, the lessons, the reminder, the leaderboard, the shout-outs — must
# be identical to the healthy page, because none of it has ever come from that
# endpoint.
#
# ⚠️ THE FLASHCARD DECK IS PRACTICE-FED AND IT IS NOT A SMALL ONE. Its lessons
# are the UNION of (a) every lesson behind every assignment the class has been
# set and (b) every lesson the endpoint says the scheme has taught, and on 8X1
# today (b) contributes far more than (a): the deck is 55 cards with practice
# answering and 16 without it. The button's own label carries that count, so it
# is filtered here BY NAME rather than asserted equal — and the gap is printed
# below rather than hidden, because 55 → 16 is the honest price of the
# degradation and a reader should see it.
PRACTICE_CONTROLS = ("Practice", "FLASHCARDS")


# ── the fold-in, watched in slow motion ─────────────────────────────────
#
# The forced-failure case proves the page SURVIVES practice failing. This
# proves the other half — that the page does not WAIT for it, and that the
# answer is folded in when it arrives.
#
# The same proxy stalls `/api/class/practice` by SLOW_SECONDS and answers it
# normally afterwards. The probe then watches two things on a 100 ms tick:
# whether the runtime has drawn (`data-mrb-renders`), and the flashcard
# button's own label, which carries the deck size. A page that mounts before
# the stall ends cannot have waited for the endpoint; a deck that grows after
# it ends can only have been folded in.
DECK = """(function(){
    var h = document.querySelector('#mrb-student[data-mrb-renders]');
    if (!h) { return null; }
    var b = h.querySelectorAll('button'), i, t;
    for (i = 0; i < b.length; i++) {
        t = (b[i].innerText || '').replace(/\\s+/g, ' ').trim();
        if (t.indexOf('FLASHCARDS') === 0) {
            return { renders: h.getAttribute('data-mrb-renders'), label: t };
        }
    }
    return { renders: h.getAttribute('data-mrb-renders'), label: '' };
})()"""


def slow_fold(pw):
    key = anon_key()
    proxy = start_broken_proxy("slow")
    server, port = cdp.serve("mrbadmus_site", PORT)
    base = "http://127.0.0.1:%d" % port
    c = CASES[0]
    q = c["q"] + "&api=http://127.0.0.1:%d" % PROXY_PORT
    rows, fails = [], []
    try:
        with cdp.Browser() as b:
            page = b.attach()
            put_session(page, base, sign_in(c["who"], key, pw))
            page.goto(base + "/student/class.html" + c["q"], settle=0.3)   # warm-up
            warm = time.time() + 40
            while time.time() < warm:
                try:
                    if page.eval(READY, timeout=5) is True:
                        break
                except Exception:
                    pass
                time.sleep(0.08)

            t0 = time.time()
            page.goto(base + "/student/class.html" + q, settle=0.0)
            end = t0 + SLOW_SECONDS + 12
            last = None
            while time.time() < end:
                try:
                    d = page.eval(DECK, timeout=5)
                except Exception:
                    d = None
                if d and d != last:
                    rows.append((round(time.time() - t0, 2), d))
                    last = d
                time.sleep(0.1)
    finally:
        for stop in (lambda: server.shutdown(), lambda: proxy.shutdown()):
            try:
                stop()
            except Exception:
                pass

    print("\n  /api/class/practice stalled by %.1fs — the page does not wait "
          "for it, and folds it in when it lands\n" % SLOW_SECONDS)
    for t, d in rows:
        print("     t=%5.2fs  renders=%-3s  %s" % (t, d["renders"], d["label"]))
    if not rows:
        fails.append("the page never drew at all")
    else:
        first = rows[0][0]
        if first >= SLOW_SECONDS:
            fails.append("first paint at %.2fs is not before the %.1fs stall — "
                         "the page is still waiting for practice" % (first, SLOW_SECONDS))
        else:
            print("\n     \u2705 first paint at %.2fs, before the %.1fs stall ended"
                  % (first, SLOW_SECONDS))
        if len(rows) < 2:
            fails.append("the deck never changed after the first paint — the "
                         "fold-in did not land")
        else:
            print("     \u2705 the deck changed at t=%.2fs, after the stall — "
                  "that is the fold-in" % rows[-1][0])
    if fails:
        print("\n  \u274c %d problem(s):" % len(fails))
        for f in fails:
            print("     \u00b7 %s" % f)
        return 1
    return 0


def compare_down():
    fails = []
    old = json.load(open(os.path.join(OUT, "mrb348_student_down-old.json")))
    new = json.load(open(os.path.join(OUT, "mrb348_student_down-new.json")))
    healthy = json.load(open(os.path.join(OUT, "mrb348_student_new.json")))
    o = old.get("ks3-practice-down", {})
    n = new.get("ks3-practice-down", {})
    h = healthy.get("ks3-own", {})

    print("\n  /api/class/practice forced to 503 — the defect, and the fix\n")

    print("  BEFORE (the defect reproduced)")
    if o.get("mounted"):
        fails.append("down-old: the page mounted — the defect did not "
                     "reproduce, so the 'after' proves nothing")
        print("     ❌ the page MOUNTED. Expected it to die; nothing is proven.")
    else:
        print("     ✅ the page never mounted%s"
              % (" — the failure card is up" if o.get("dead") else ""))

    print("\n  AFTER (this change)")
    if not n.get("mounted"):
        fails.append("down-new: the page still does not mount")
        print("     ❌ the page still does not mount.")
    else:
        print("     ✅ the page mounted with the practice route answering 503")
        if n.get("dead"):
            fails.append("down-new: the failure sentence is on the page")
            print("     ❌ …but the failure sentence is on it.")
        else:
            print("     ✅ no failure sentence anywhere on it")

        # The work is the page. Everything but the practice-fed controls has
        # to match the healthy capture exactly.
        hc = [x for x in h.get("controls", [])
              if not any(p in x for p in PRACTICE_CONTROLS)]
        nc = [x for x in n.get("controls", [])
              if not any(p in x for p in PRACTICE_CONTROLS)]
        if hc == nc:
            print("     ✅ every control that is not practice-fed is identical "
                  "to the healthy page (%d of them)" % len(nc))
        else:
            fails.append("down-new: a non-practice control differs from the "
                         "healthy page")
            print("     ❌ a non-practice control differs:")
            for x in sorted(set(hc) - set(nc))[:8]:
                print("        only HEALTHY: %s" % x)
            for x in sorted(set(nc) - set(hc))[:8]:
                print("        only DEGRADED: %s" % x)

        # And what a student actually loses, printed rather than asserted.
        ht, nt = h.get("text", ""), n.get("text", "")
        print("\n     what the degradation costs, stated rather than hidden:")
        print("       healthy page  %6d chars, %3d controls, %4d nodes"
              % (len(ht), len(h.get("controls", [])), h.get("nodes", 0)))
        print("       practice down %6d chars, %3d controls, %4d nodes"
              % (len(nt), len(n.get("controls", [])), n.get("nodes", 0)))
        lost = sorted(set(h.get("controls", [])) - set(n.get("controls", [])))
        print("       controls lost: %s" % (lost or "none"))

    if fails:
        print("\n  ❌ %d problem(s):" % len(fails))
        for f in fails:
            print("     · %s" % f)
        return 1
    print("\n  ✅ practice can fail and the child still gets their work.")
    return 0


def compare():
    fails = []
    a = json.load(open(os.path.join(OUT, "mrb348_student_old.json")))
    b = json.load(open(os.path.join(OUT, "mrb348_student_new.json")))
    print("\n  comparing OLD (before MRB-348) with NEW (after)\n")
    for c in CASES:
        k = c["key"]
        oldc, newc = a.get(k, {}), b.get(k, {})
        print("  %s — %s" % (k, c["note"]))
        if oldc.get("error") or newc.get("error"):
            fails.append("%s: %s / %s" % (k, oldc.get("error"), newc.get("error")))
            print("     ❌ %s / %s" % (oldc.get("error"), newc.get("error")))
            continue
        same_text = oldc.get("text") == newc.get("text")
        same_ctl = oldc.get("controls") == newc.get("controls")
        print("     %s visible text   (%d vs %d chars)"
              % ("✅" if same_text else "❌",
                 len(oldc.get("text", "")), len(newc.get("text", ""))))
        print("     %s control set    (%d vs %d)"
              % ("✅" if same_ctl else "❌",
                 len(oldc.get("controls", [])), len(newc.get("controls", []))))
        if not same_text:
            fails.append(k + ": visible text differs")
            ot, nt = oldc.get("text", ""), newc.get("text", "")
            for i in range(min(len(ot), len(nt))):
                if ot[i] != nt[i]:
                    print("        first difference at char %d:" % i)
                    print("        old …%s…" % ot[max(0, i-60):i+60])
                    print("        new …%s…" % nt[max(0, i-60):i+60])
                    break
            else:
                print("        one is a prefix of the other")
        if not same_ctl:
            fails.append(k + ": control set differs")
            so, sn = set(oldc.get("controls", [])), set(newc.get("controls", []))
            for x in sorted(so - sn)[:6]:
                print("        only OLD: %s" % x)
            for x in sorted(sn - so)[:6]:
                print("        only NEW: %s" % x)

        # The ruled address behaviour, asserted on its own rather than folded
        # into the text comparison — a wrong URL is invisible in innerText and
        # is exactly what the 23 Aug ruling is about.
        want = c["expect_param"]
        got_old, got_new = oldc.get("url", ""), newc.get("url", "")
        def has(u):
            return (re.search(r"class=([0-9a-f-]{36})", u or "") or [None, None])[1] \
                if re.search(r"class=([0-9a-f-]{36})", u or "") else None
        po, pn = has(got_old), has(got_new)
        ok_old, ok_new = (po == want), (pn == want)
        print("     %s address        old=%r new=%r (ruled: %s)"
              % ("✅" if (ok_old and ok_new) else "❌", got_old, got_new,
                 want or "no class parameter"))
        if not (ok_old and ok_new):
            fails.append(k + ": address parameter wrong")
        print()

    if fails:
        print("  ❌ %d difference(s):" % len(fails))
        for f in fails:
            print("     · %s" % f)
        return 1
    print("  ✅ every case renders the same visible text, the same controls, "
          "and the same address.")
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--capture", choices=["old", "new", "down-old", "down-new"])
    ap.add_argument("--compare", action="store_true")
    ap.add_argument("--compare-down", action="store_true")
    ap.add_argument("--slow-fold", action="store_true")
    a = ap.parse_args()
    if a.capture:
        pw = os.environ.get("MRB_TEST_TEACHER_PASSWORD")
        if not pw:
            raise SystemExit("$MRB_TEST_TEACHER_PASSWORD is not set.")
        print("capturing %s" % a.capture.upper())
        if a.capture.startswith("down-"):
            capture_down(a.capture, pw)
        else:
            capture(a.capture, pw)
        return 0
    if a.compare:
        return compare()
    if a.compare_down:
        return compare_down()
    if a.slow_fold:
        pw = os.environ.get("MRB_TEST_TEACHER_PASSWORD")
        if not pw:
            raise SystemExit("$MRB_TEST_TEACHER_PASSWORD is not set.")
        return slow_fold(pw)
    ap.print_help()
    return 2


if __name__ == "__main__":
    sys.exit(main())
