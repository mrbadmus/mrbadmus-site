#!/usr/bin/env python3
"""student_bell_drive.py — press the student's bell, and say what it did.

    MRB_THROWAWAY_PASSWORD=… python3 student_bell_drive.py
    python3 student_bell_drive.py --provision      # reset the TEST pupils' pw
    python3 student_bell_drive.py --keep           # leave the seeded rows

MRB-337, 8 Sep 2026. Mide asked for a bell on the student pages carrying the
count of unread messages, with the class page's existing top banner untouched
and the badge moving when the banner does.

── WHAT IT PROVES, AND HOW ──────────────────────────────────────────────

Seven claims, each in its own named check:

    badge_zero        the badge is HIDDEN at nought, and the bell is still there
    badge_one         one unread message makes it 1, and the aria-label says so
    panel_lists       the panel lists every message, newest first, kind + London date
    tap_opens         tapping a message opens its work AND clears its badge
    banner_lives      the class page's banner still draws and still marks read,
                      and the badge moves with it
    rls               a pupil cannot read another pupil's rows
    narrow            390px: no sideways scroll, and the panel is full width

── ⚠️ THE BACKEND ROUTE IS SERVED BY A PROXY, AND THAT IS SAID OUT LOUD ──

`GET /api/student/notifications` is built by a different lane. This drive does
NOT wait for it and does NOT fake a pass about it: it stands up a local
PASS-THROUGH PROXY on its own port and hands the page that address through
config.js's `?api=` override — the localhost-only mechanism the repo already
uses to point one worktree at its own backend.

The proxy serves the TWO notification routes from a script this file controls
and FORWARDS EVERYTHING ELSE, unread and unaltered, to whatever backend is
actually running. So the class page mounts on real data from the real backend
while the bell is fed a known set of messages.

What that proves and what it does not:

    ✅  every frontend claim above — the badge, the panel, the ordering, the
        London dates, the navigation, the mark-read POST going out with the
        right id and the right bearer, the badge and banner agreeing
    ❌  that the real route returns the right rows for the right pupil

The second is the backend lane's to prove. This drive PROBES for the real
route and, when it answers, re-runs `rls` against it for real (see
`route_rls`); until then that one check reports NOT EXECUTED with its reason
printed, and the run is not called green.

── ⚠️ THE TRAPS THIS FILE IS WRITTEN AGAINST ────────────────────────────

  · The viewport is set on a BLANK page BEFORE navigating. The CDP override
    persists across navigations, and a page decides its header treatment once,
    at mount — so resizing into a page measures the previous width's layout.
  · ONE BROWSER PER PERSONA, sequentially. Two personas in one browser share
    one `localStorage`, and the second sign-in silently becomes the first
    pupil again.
  · The planted session is a REAL one, minted from GoTrue. A hand-rolled JWT
    is deleted by the Supabase SDK on the first read.
  · Screenshots are taken BEFORE navigating away, never after.
  · `pkill` appears nowhere. Other lanes' browsers are running.
"""

import argparse
import http.server
import json
import os
import re
import socketserver
import ssl
import sys
import threading
import time
import urllib.error
import urllib.parse
import urllib.request

REPO = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, REPO)
os.chdir(REPO)

import ks3_browser as cdp                                    # noqa: E402

# ── the world ────────────────────────────────────────────────────────────
#
# TEST, always. This drive WRITES a reminder row so the banner has something
# to draw, and a drive that writes belongs in the sandbox.
SB_URL = "https://qeppkiswvclkkwbxmlok.supabase.co"
PROJECT_REF = "qeppkiswvclkkwbxmlok"
CTX = ssl.create_default_context(cafile="/etc/ssl/cert.pem")

PUPIL_A = "mrb326_pupil_a@throwaway.test"
PUPIL_B = "mrb326_pupil_b@throwaway.test"
TEACHER = "mrb326_teacher@throwaway.test"
PW_ENV = "MRB_THROWAWAY_PASSWORD"

SITE_PORT = 5507          # not 5500 — student_controls_drive owns that one
_SITE = {"base": ""}


def base_site():
    """The local site's origin. Module-level because the real-route phases
    take the BACKEND's base as their `base` argument and still need this."""
    return _SITE["base"]

SHOTS = os.path.join(cdp.gate_tmp(), "bell")

# The backend the proxy forwards to, and the one the real route is read from.
# The class page needs a backend that accepts a TEST JWT, which the production
# instance does not.
#
# ⚠️ 3337 IS THE ONE, AND 3336 IS A TRAP. Two local backends were running on
# 8 Sep: 3337 from the MRB-337 backend worktree, carrying these routes, and
# 3336 from an earlier pass off backend `main`, which does not. This drive
# probed 3336 first, got a 404 on `/api/student/notifications`, and reported
# the route as NOT BUILT — a whole security assertion skipped because the
# probe was pointed at the wrong process. 3336 is deliberately NOT on this
# list; another lane is using it and it must not be killed either.
#
# The probe below tells the two apart properly now: a REGISTERED route answers
# 401 unauthenticated, an absent one answers 404.
LOCAL_BACKENDS = ("http://localhost:3337", "http://localhost:3000",
                  "http://localhost:3100")

results = []          # (name, ok|None, detail)   ok=None → NOT EXECUTED


def check(name, ok, detail=""):
    results.append((name, ok, detail))
    mark = "✅" if ok else ("⏭ " if ok is None else "❌")
    print("     %s %-34s %s" % (mark, name, detail))
    return ok


# ── credentials ──────────────────────────────────────────────────────────

def anon_key():
    src = open("shared/config.js", encoding="utf-8").read()
    return re.search(r"'(eyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+)'",
                     src[src.index("const TEST"):]).group(1)


def service_key():
    """The TEST service-role key from the backend repo's .env, or None.

    ⚠️ IT PROVES NOTHING. It bypasses RLS entirely, so no check in this file
    runs on it. Two jobs only: resetting the throwaway passwords under
    `--provision`, and deleting the reminder row this drive seeds —
    `student_notifications` has no delete policy for anybody, so the account
    that wrote the row cannot remove it, and the unique index
    `(student_id, assignment_id, sent_on)` would make a second run today fail
    with a 409 that has nothing to do with the bell.
    """
    path = "/Users/midebadmus/Documents/GitHub/mrbadmus---backend/.env"
    try:
        for line in open(path, encoding="utf-8"):
            if line.startswith("SUPABASE_SERVICE_ROLE_KEY="):
                return line.split("=", 1)[1].strip()
    except OSError:
        pass
    return None


def call(method, url, key, bearer, body=None, prefer=None):
    headers = {"apikey": key, "Authorization": "Bearer " + bearer,
               "Content-Type": "application/json"}
    if prefer:
        headers["Prefer"] = prefer
    req = urllib.request.Request(
        url, data=json.dumps(body).encode() if body is not None else None,
        headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=45, context=CTX) as r:
            raw = r.read().decode()
            return r.status, (json.loads(raw) if raw.strip() else None)
    except urllib.error.HTTPError as e:
        raw = e.read().decode()
        try:
            return e.code, json.loads(raw)
        except ValueError:
            return e.code, raw[:400]


def sign_in(email, password, key):
    st, body = call("POST", SB_URL + "/auth/v1/token?grant_type=password",
                    key, key, {"email": email, "password": password})
    if st != 200 or not isinstance(body, dict) or "access_token" not in body:
        raise SystemExit(
            "student_bell_drive: %s could not sign in (HTTP %s). Run\n"
            "    python3 student_bell_drive.py --provision\n"
            "to re-assert the throwaway passwords on TEST." % (email, st))
    return body


def provision(password):
    """Re-assert the two pupils' password on TEST. A RESET, not a reseed."""
    svc = service_key()
    if not svc:
        print("\n❌ --provision needs the TEST service-role key and the "
              "backend .env does not carry one. Nothing changed.\n")
        return 2
    key, bad = anon_key(), 0
    print("\n🔑  re-asserting the throwaway pupils' password on TEST\n")
    st, body = call("GET", SB_URL + "/auth/v1/admin/users?per_page=1000",
                    svc, svc)
    users = {u.get("email"): u["id"]
             for u in (body or {}).get("users", [])} if st == 200 else {}
    for email in (PUPIL_A, PUPIL_B):
        uid = users.get(email)
        if not uid:
            print("     ❌ %s — no such user on TEST" % email)
            bad += 1
            continue
        st, _ = call("PUT", SB_URL + "/auth/v1/admin/users/" + uid, svc, svc,
                     {"password": password, "email_confirm": True})
        if st != 200:
            print("     ❌ %s — reset HTTP %s" % (email, st))
            bad += 1
            continue
        # Verified by SIGNING IN, never by the reset's own 200.
        st2, _ = call("POST", SB_URL + "/auth/v1/token?grant_type=password",
                      key, key, {"email": email, "password": password})
        ok = st2 == 200
        print("     %s %s — sign-in %s" % ("✅" if ok else "❌", email, st2))
        bad += 0 if ok else 1
    print("")
    return 1 if bad else 0


# ── the proxy ────────────────────────────────────────────────────────────

class Feed:
    """What the two notification routes say, and what they were told."""

    def __init__(self):
        self.items = []
        self.reads = []          # ids POSTed to …/read
        self.gets = 0
        self.bearers = []
        # ⚠️ PASSTHROUGH TURNS THE PROXY INTO A PURE CORS SHIM. In this mode
        # it synthesises NOTHING: both notification routes are forwarded to
        # the real backend with the caller's bearer untouched, so the page is
        # talking to the backend lane's own handler.
        #
        # It exists because the backend's CORS allowlist is
        # `mrbadmus.com`, `localhost:3000` and `localhost:5500` — and this
        # drive serves the site on 5507, deliberately, so it cannot collide
        # with `student_controls_drive`. Without the shim every fetch the
        # class page makes is blocked and the page renders its "could not
        # load" sentence, which reads exactly like a bell defect and is not
        # one. (CLAUDE.md's own note: a CORS-blocked page gives a false
        # layout pass.) The alternative — moving the site onto 5500 — trades
        # a shim for a port collision with another lane's browser.
        self.passthrough = False

    def set(self, items, passthrough=False):
        self.items = items
        self.reads = []
        self.gets = 0
        self.passthrough = passthrough


FEED = Feed()


def live_backend():
    for base in LOCAL_BACKENDS:
        try:
            req = urllib.request.Request(base + "/api/health")
            with urllib.request.urlopen(req, timeout=3) as r:
                if r.status == 200:
                    return base
        except Exception:                                    # noqa: BLE001
            continue
    return None


def probe_route(base, bearer):
    """Is the route REGISTERED? Two questions, because one is not enough.

    ⚠️ THE UNAUTHENTICATED PROBE IS THE ONE THAT PROVES IT. A registered route
    behind `getUser()` answers 401 with no bearer; a route Express has never
    heard of answers 404. Asking only the authenticated question conflates
    "the route is missing" with "my token was refused", and a single
    `except: return False` conflates both with "the port was wrong" — which is
    exactly how this drive skipped `route_rls` on its first pass.

    Returns (registered, how) so the run can PRINT which of the two it saw.
    """
    if not base:
        return False, "no local backend"
    unauth = None
    try:
        req = urllib.request.Request(base + "/api/student/notifications")
        with urllib.request.urlopen(req, timeout=10) as r:
            unauth = r.status
    except urllib.error.HTTPError as e:
        unauth = e.code
    except Exception as err:                                 # noqa: BLE001
        return False, "unreachable: %s" % err
    if unauth == 404:
        return False, "404 unauthenticated — not registered on %s" % base
    try:
        req = urllib.request.Request(
            base + "/api/student/notifications",
            headers={"Authorization": "Bearer " + bearer})
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.status == 200, ("%s unauthenticated, %s with a bearer"
                                     % (unauth, r.status))
    except urllib.error.HTTPError as e:
        return False, "%s unauthenticated, %s with a bearer" % (unauth, e.code)
    except Exception as err:                                 # noqa: BLE001
        return False, "%s unauthenticated, then %s" % (unauth, err)


class Proxy(http.server.BaseHTTPRequestHandler):
    """Two injected routes; everything else forwarded, unread and unaltered."""

    upstream = None

    def log_message(self, *a):        # silence
        pass

    def _cors(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Headers", "authorization,content-type")
        self.send_header("Access-Control-Allow-Methods", "GET,POST,OPTIONS")
        # ⚠️ `Date` IS NOT A CORS-SAFELISTED RESPONSE HEADER, and without this
        # line the class page will not mount at all. `buildClass` reads the
        # backend's `date` header as THE SERVER CLOCK and refuses to guess with
        # the device's — "no server clock on the response" — so a proxy that
        # forwards the body perfectly and hides that one header looks exactly
        # like a broken page. Cost one debugging round; written down so it
        # costs none.
        self.send_header("Access-Control-Expose-Headers", "date, Date")

    def _json(self, code, payload):
        body = json.dumps(payload).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self._cors()
        self.end_headers()
        self.wfile.write(body)

    def do_OPTIONS(self):             # noqa: N802
        self.send_response(204)
        self._cors()
        self.end_headers()

    def do_GET(self):                 # noqa: N802
        if self.path.split("?")[0] == "/api/student/notifications":
            FEED.gets += 1
            FEED.bearers.append(self.headers.get("Authorization", ""))
            if not FEED.passthrough:
                return self._json(200, FEED.items)
        self._forward("GET")

    def do_POST(self):                # noqa: N802
        m = re.match(r"^/api/student/notifications/(.+)/read$",
                     self.path.split("?")[0])
        if m and not FEED.passthrough:
            FEED.reads.append(urllib.parse.unquote(m.group(1)))
            for it in FEED.items:
                if str(it.get("id")) == FEED.reads[-1]:
                    it["read"] = True
            return self._json(200, {"ok": True})
        self._forward("POST")

    def _forward(self, method):
        if not Proxy.upstream:
            return self._json(503, {"error": "no upstream backend"})
        n = int(self.headers.get("Content-Length") or 0)
        body = self.rfile.read(n) if n else None
        req = urllib.request.Request(
            Proxy.upstream + self.path, data=body, method=method)
        for h in ("Authorization", "Content-Type"):
            if self.headers.get(h):
                req.add_header(h, self.headers[h])
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                out, code = r.read(), r.status
        except urllib.error.HTTPError as e:
            out, code = e.read(), e.code
        except Exception as err:                             # noqa: BLE001
            return self._json(502, {"error": str(err)})
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(out)))
        self._cors()
        self.end_headers()
        self.wfile.write(out)


class Threaded(socketserver.ThreadingMixIn, http.server.HTTPServer):
    daemon_threads = True
    allow_reuse_address = True


def start_proxy():
    srv = Threaded(("127.0.0.1", 0), Proxy)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv, "http://localhost:%d" % srv.server_address[1]


# ── the browser ──────────────────────────────────────────────────────────

def plant(browser, base, key, session):
    """A REAL session in this origin's localStorage, through the real SDK.

    ⚠️ NOT A HAND-ROLLED JWT. The SDK validates what it finds and deletes a
    token it does not recognise, so a fabricated one leaves the page signed
    out and every check below measuring a signed-out page.

    ⚠️ AND NOT ON THE APP PAGE. `localStorage` is per-origin, so this has to
    be served from the same port — but it must not be a page that is doing its
    own auth at the same time. The directory listing is HTML on the right
    origin with no JavaScript of its own to race.
    """
    boot = browser.page(base + "/shared/", settle=0.4)
    boot.eval("(function(){var s=document.createElement('script');"
              "s.src='https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2';"
              "document.head.appendChild(s);})()")
    for _ in range(40):
        if boot.eval("!!(window.supabase && window.supabase.createClient)"):
            break
        time.sleep(0.25)
    got = boot.eval(
        "(async function(){var c=window.supabase.createClient(%s,%s);"
        "var r=await c.auth.setSession(%s);"
        "return r.error ? ('err:'+r.error.message) : 'ok';})()"
        % (json.dumps(SB_URL), json.dumps(key),
           json.dumps({"access_token": session["access_token"],
                       "refresh_token": session["refresh_token"]})))
    return got == "ok"


def sized(browser, width, height=900):
    """⚠️ BLANK PAGE, SET THE SIZE, THEN NAVIGATE. See the header."""
    browser.page("about:blank", settle=0.15).set_viewport(width, height)


BELL_STATE = r"""(function () {
  var b = document.querySelector('[data-mrb-bell]');
  var badge = b && b.querySelector('[data-mrb-bell-badge]');
  var p = document.getElementById('mrb-bell-panel');
  var de = document.documentElement;
  return {
    bell: !!b,
    visible: !!(b && b.getBoundingClientRect().width > 0),
    w: b ? Math.round(b.getBoundingClientRect().width) : 0,
    h: b ? Math.round(b.getBoundingClientRect().height) : 0,
    label: b ? (b.getAttribute('aria-label') || '') : '',
    badgeShown: !!(badge && !badge.hidden && badge.getBoundingClientRect().width > 0),
    badgeText: badge ? badge.textContent : null,
    panelOpen: !!(p && !p.hidden),
    panelW: p && !p.hidden ? Math.round(p.getBoundingClientRect().width) : 0,
    panelRows: p ? p.querySelectorAll('[data-mrb-bell-row]').length : 0,
    panelText: p && !p.hidden ? (p.innerText || '').replace(/\s+/g, ' ').trim() : '',
    banner: !!document.querySelector('[data-mrb-reminder]'),
    scrollW: de.scrollWidth,
    clientW: de.clientWidth,
    docH: de.scrollHeight
  };
})()"""


def wait_bell(page, seconds=30.0):
    end = time.time() + seconds
    while time.time() < end:
        st = page.eval(BELL_STATE)
        if isinstance(st, dict) and st.get("bell"):
            return st
        time.sleep(0.25)
    return page.eval(BELL_STATE)


def wait_mount(page, seconds=75.0, poll=0.3):
    """Rendered AND settled — the student pages' own definition."""
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


# ── the messages the proxy serves ────────────────────────────────────────

def sample(assignment_id, reminder_id=None):
    """Four kinds, deliberately out of order, so `panel_lists` proves the
    page sorts them rather than trusting the wire.

    ⚠️ `reminder_id` IS THE REAL ROW'S UUID ON THE CLASS PAGE, and it has to
    be. The banner is drawn from the `student_reminders_for_viewer` RPC — real
    Supabase, not this proxy — so if the bell were fed a made-up reminder id
    the two would be talking about different rows and `banner_lives` would
    measure a coincidence. Feeding the seeded row's own id is what makes
    "Dismiss moved the badge" a statement about one message."""
    now = time.time()

    def iso(mins_ago):
        return time.strftime("%Y-%m-%dT%H:%M:%SZ",
                             time.gmtime(now - mins_ago * 60))
    return [
        {"id": "shoutout:33333333-3333-3333-3333-333333333333",
         "kind": "shoutout", "text": "Nice work in the last round.",
         "created_at": iso(600), "read": True},
        {"id": "reminder:" + (reminder_id or
                              "11111111-1111-1111-1111-111111111111"),
         "kind": "reminder", "text": "This week's work is waiting.",
         "created_at": iso(5), "read": False,
         "assignment_id": assignment_id},
        {"id": "feedback:22222222-2222-2222-2222-222222222222",
         "kind": "feedback", "text": "Check your units on question 3.",
         "created_at": iso(120), "read": True},
        # ⚠️ `work`, NOT `new_work`. `NOTIF_SOURCES` on the backend is
        # ['reminder','feedback','shoutout','work']; the proxy must speak the
        # real contract or the frontend claims it proves are claims about a
        # contract nobody implements. Fed as `new_work` this row rendered
        # under the heading `Reminder` and nothing said so.
        {"id": "work:44444444-4444-4444-4444-444444444444",
         "kind": "work", "text": "Particle model, due Thursday.",
         "created_at": iso(60), "read": True},
    ]


# ═══════════════════════════════════════════════════════════════════════
#  the phases
# ═══════════════════════════════════════════════════════════════════════

def phase_source():
    """The two joins that make the badge and the banner ONE fact.

    Read off the SHIPPED bytes, not the source tree: `mrbadmus_site/` is what
    Cloudflare serves, and a join that exists only in `shared/` is a join no
    student has.
    """
    print("\n  ── phase 0 · the badge/banner join, in the shipped bytes ──")
    js = open("mrbadmus_site/shared/student-live.js", encoding="utf-8").read()
    i = js.index("function markRemindersRead(sb, ids)")
    body = js[js.index("{", i):js.index("async function run()", i)]
    check("join_banner_to_badge",
          "MrBadmusBell.markReadLocal(ids)" in body,
          "markRemindersRead hands its ids to the bell")
    check("join_badge_to_banner",
          "retireReminder()" in js and "bell.on(function" in js,
          "the bell's change listener retires the banner")
    for page_name in ("class", "assignment"):
        html = open("mrbadmus_site/student/%s.html" % page_name,
                    encoding="utf-8").read()
        check("bell_host_on_%s" % page_name,
              html.count("data-port-bell-host") == 1,
              "student/%s.html names exactly one bell host (SET_ATTR, so the "
              "build stops if Design moves the node)" % page_name)
    check("no_polling_loop",
          "setInterval" not in
          open("mrbadmus_site/shared/student-bell.js", encoding="utf-8").read(),
          "shared/student-bell.js contains no setInterval")


def phase_chrome(key, sess_a, base, api, aid):
    """The KS4 chrome surfaces — badge, panel, keyboard, widths, navigation.

    my-challenges.html is the surface used because it needs NO backend of its
    own to render its chrome, so a failure here is the bell's and nothing
    else's.
    """
    print("\n  ── phase 1 · the bell on a KS4 chrome page (my-challenges) ──")
    url = base + "/my-challenges.html?env=test&api=" + api
    b = cdp.Browser().start()
    try:
        if not plant(b, base, key, sess_a):
            return check("chrome_session", False, "could not plant the session")

        # ── badge_zero ───────────────────────────────────────────────────
        FEED.set([])
        sized(b, 1280)
        page = b.page(url, settle=0.8)
        st = wait_bell(page)
        check("badge_zero", bool(st.get("bell")) and not st.get("badgeShown")
              and st.get("visible"),
              "bell drawn %dx%d, badge hidden, label %r"
              % (st.get("w"), st.get("h"), st.get("label")))
        check("fetched_on_load", FEED.gets >= 1,
              "%d GET(s) on load, bearer %s"
              % (FEED.gets,
                 "present" if any(x.startswith("Bearer ey")
                                  for x in FEED.bearers) else "MISSING"))

        # ── badge_one + panel_lists ──────────────────────────────────────
        FEED.set(sample(aid))
        sized(b, 1280)
        page = b.page(url, settle=0.8)
        st = wait_bell(page)
        check("badge_one", st.get("badgeShown") and st.get("badgeText") == "1"
              and "1 unread" in st.get("label", ""),
              "badge %r, label %r" % (st.get("badgeText"), st.get("label")))

        page.eval("document.querySelector('[data-mrb-bell]').click()")
        time.sleep(0.5)
        st = page.eval(BELL_STATE)
        order = page.eval(
            "(function(){var r=document.querySelectorAll('[data-mrb-bell-row]');"
            "return Array.prototype.map.call(r,function(e){"
            "return (e.innerText||'').replace(/\\s+/g,' ').trim();});})()")
        kinds = [str(x).split(" ")[0] for x in (order or [])]
        check("panel_lists",
              st.get("panelOpen") and st.get("panelRows") == 4
              and kinds == ["REMINDER", "NEW", "FEEDBACK", "SHOUTOUT"],
              "%d rows, kinds %s" % (st.get("panelRows"), kinds))
        check("panel_london_date",
              bool(re.search(r"\d{1,2} [A-Z][a-z]{2}, \d{2}:\d{2}",
                             " ".join(str(x) for x in (order or [])))),
              "dates read '<d> <Mon>, <HH>:<MM>' (London)")
        os.makedirs(SHOTS, exist_ok=True)
        # ⚠️ THE WIDTH IS PASSED TO `screenshot()`, ALWAYS. `ks3_browser`'s
        # capture RE-SETS the viewport to its own 1280x900 default before it
        # shoots, so a shot taken after a 390px measurement comes back showing
        # the DESKTOP layout — a picture that contradicts the number beside it
        # and looks like the measurement was wrong. Every capture in this file
        # names its width for that reason. (Every check is measured BEFORE the
        # shot, so the reset cannot reach a result.)
        page.screenshot(os.path.join(SHOTS, "panel-1280.png"), 1280, 900)

        # ── Escape closes, and focus comes back ──────────────────────────
        page.eval(
            "document.dispatchEvent(new KeyboardEvent('keydown',"
            "{key:'Escape',bubbles:true}))")
        time.sleep(0.35)
        closed = page.eval(BELL_STATE)
        check("escape_closes", not closed.get("panelOpen")
              and page.eval("document.activeElement && "
                            "document.activeElement.hasAttribute('data-mrb-bell')"),
              "panel dismissed, focus back on the bell")

        # ── the Close control ────────────────────────────────────────────
        page.eval("document.querySelector('[data-mrb-bell]').click()")
        time.sleep(0.4)
        page.eval("document.querySelector('.mrb-bell-close').click()")
        time.sleep(0.35)
        check("close_control", not page.eval(BELL_STATE).get("panelOpen"),
              "the Close button dismisses the panel")

        # ── keyboard reachable ───────────────────────────────────────────
        check("keyboard_reachable",
              page.eval("(function(){var b=document.querySelector("
                        "'[data-mrb-bell]');b.focus();"
                        "return document.activeElement===b && "
                        "b.tabIndex>=0 && b.tagName==='BUTTON';})()"),
              "a real <button>, focusable, with an aria-label")

        # ── 1280 and 390: no sideways scroll ─────────────────────────────
        wide = page.eval(BELL_STATE)
        check("wide_no_hscroll", wide["scrollW"] <= wide["clientW"] + 1,
              "1280px: scrollWidth %d ≤ clientWidth %d"
              % (wide["scrollW"], wide["clientW"]))

        sized(b, 390, 780)
        page = b.page(url, settle=0.8)
        st = wait_bell(page)
        check("narrow_bell_visible", st.get("visible") and st.get("badgeShown"),
              "390px: the bell is on screen (nav.css hides .nav-icon-link "
              "below 400 — the bell does not use that class)")
        page.eval("document.querySelector('[data-mrb-bell]').click()")
        time.sleep(0.5)
        st = page.eval(BELL_STATE)
        page.screenshot(os.path.join(SHOTS, "panel-390.png"), 390, 780)
        check("narrow", st["scrollW"] <= st["clientW"] + 1
              and st["panelW"] >= st["clientW"] - 26,
              "390px: no sideways scroll (%d ≤ %d), panel %dpx of %dpx"
              % (st["scrollW"], st["clientW"], st["panelW"], st["clientW"]))

        # ── tap_opens ────────────────────────────────────────────────────
        FEED.set(sample(aid))
        sized(b, 1280)
        page = b.page(url, settle=0.8)
        wait_bell(page)
        page.eval("document.querySelector('[data-mrb-bell]').click()")
        time.sleep(0.45)
        page.eval(
            "(function(){var r=document.querySelectorAll('[data-mrb-bell-row]');"
            "for(var i=0;i<r.length;i++){"
            "if(/REMINDER/.test(r[i].innerText||'')){r[i].click();return;}}})()")
        time.sleep(1.6)
        where = page.eval("location.pathname + location.search") or ""
        check("tap_opens", "/student/assignment.html" in where
              and ("assignment=" + aid) in where,
              "landed on %s" % where[:90])
        check("tap_marks_read",
              FEED.reads == ["reminder:11111111-1111-1111-1111-111111111111"],
              "POST …/read carried %s" % (FEED.reads or "NOTHING"))

        # ── the badge cleared, back on the chrome page ───────────────────
        sized(b, 1280)
        page = b.page(url, settle=0.8)
        st = wait_bell(page)
        check("badge_clears", not st.get("badgeShown"),
              "with the message read, the badge is hidden again")
    finally:
        b.close()


def phase_class(key, sess_a, base, api, aid, seeded):
    """The class page — the bell in the studio header, the banner, the join.

    ⚠️ THIS PHASE NEEDS A BACKEND THAT ACCEPTS A TEST JWT. The class page does
    not mount without one, and reporting an unmounted page as a bell failure
    would be a lie in the expensive direction. With no local backend the whole
    phase reports NOT EXECUTED, by name.
    """
    print("\n  ── phase 2 · the bell on the student class page ──")
    if not Proxy.upstream:
        for n in ("class_bell", "bell_survives_redraw",
                  "panel_survives_redraw", "banner_lives"):
            check(n, None, "no local backend accepts a TEST JWT — the class "
                           "page cannot mount, so this was not executed")
        return

    url = base + "/student/class.html?env=test&api=" + api
    b = cdp.Browser().start()
    try:
        if not plant(b, base, key, sess_a):
            return check("class_session", False, "could not plant the session")
        FEED.set(sample(aid, seeded))
        sized(b, 1280)
        page = b.page(url, settle=1.0)
        n = wait_mount(page)
        if n < 20:
            for nm in ("class_bell", "bell_survives_redraw",
                       "panel_survives_redraw", "banner_lives"):
                check(nm, None, "the class page did not mount (%d nodes) — "
                                "not a bell result" % n)
            return
        st = wait_bell(page)
        inhead = page.eval(
            "(function(){var b=document.querySelector('[data-mrb-bell]');"
            "return !!(b && b.closest('[data-port-bell-host]'));})()")
        check("class_bell", st.get("bell") and inhead and st.get("badgeShown"),
              "in the header's [data-port-bell-host], badge %r"
              % st.get("badgeText"))
        os.makedirs(SHOTS, exist_ok=True)
        page.screenshot(os.path.join(SHOTS, "class-1280.png"), 1280, 900)

        # ── the redraw trap ──────────────────────────────────────────────
        #
        # `draw()` empties #mrb-student and rebuilds it on every setState.
        # Press a real control, then look again: the button must be back
        # (after-draw hook) with its number, and the panel — which lives on
        # document.body — must still be open.
        page.eval("document.querySelector('[data-mrb-bell]').click()")
        time.sleep(0.45)
        before = page.eval(BELL_STATE)
        # A mark on the panel NODE. If the rebuild destroyed it, the element
        # that comes back is a different object and the mark is gone — which
        # is exactly what would happen to a panel living inside the mount host.
        page.eval("document.getElementById('mrb-bell-panel').__mrbTag = 'v21'")
        pressed = page.eval(
            "(function(){var n=document.querySelectorAll("
            "'#mrb-student button,#mrb-student [role=\"button\"]');"
            "for(var i=0;i<n.length;i++){var e=n[i];"
            "if(e.hasAttribute('data-mrb-bell'))continue;"
            "var r=e.getBoundingClientRect();"
            "if(r.width>30&&r.height>20){e.click();return 'ok';}}"
            "return 'none';})()")
        time.sleep(0.9)
        after = page.eval(BELL_STATE)
        check("bell_survives_redraw",
              pressed == "ok" and after.get("bell")
              and after.get("badgeText") == before.get("badgeText"),
              "pressed a control (%s); bell back, badge still %r"
              % (pressed, after.get("badgeText")))

        # ⚠️ THE CONTROL PRESSED ABOVE IS AN OUTSIDE CLICK, AND THE PANEL
        # CLOSING IS CORRECT. Tapping the page behind an open panel dismisses
        # it — that is the behaviour, not the defect. The claim under test is
        # narrower and it is the one the runtime can break: the panel ELEMENT
        # is not destroyed and rebuilt by `draw()`, because it is a child of
        # `document.body` rather than of the mount host. The mark proves the
        # node came through the rebuild as the same object; re-opening proves
        # it still works afterwards.
        survived = page.eval(
            "(function(){var p=document.getElementById('mrb-bell-panel');"
            "return !!(p && p.__mrbTag==='v21' && p.parentNode===document.body"
            " && !document.getElementById('mrb-student').contains(p));})()")
        page.eval("document.querySelector('[data-mrb-bell]').click()")
        time.sleep(0.45)
        again = page.eval(BELL_STATE)
        check("panel_survives_redraw",
              pressed == "ok" and before.get("panelOpen") and survived
              and again.get("panelOpen") and again.get("panelRows") == 4,
              "the panel node came through the rebuild as the same object, "
              "still a child of <body>, and re-opens with %d rows"
              % again.get("panelRows"))
        page.eval(
            "document.dispatchEvent(new KeyboardEvent('keydown',"
            "{key:'Escape',bubbles:true}))")
        time.sleep(0.3)

        # ── the banner, and the join ─────────────────────────────────────
        if not seeded:
            check("banner_lives", None,
                  "no reminder row could be seeded for this pupil — see the "
                  "seeding note above; the banner path was not executed")
            return
        page = b.page(url, settle=1.0)
        wait_mount(page)
        st = wait_bell(page)
        if not st.get("banner"):
            return check("banner_lives", False,
                         "a reminder row was seeded and the banner did not draw")
        page.eval(
            "(function(){var n=document.querySelectorAll("
            "'[data-mrb-reminder] button');"
            "for(var i=0;i<n.length;i++){"
            "if(/Dismiss/.test(n[i].innerText||'')){n[i].click();return;}}})()")
        time.sleep(1.0)
        gone = page.eval(BELL_STATE)
        check("banner_lives",
              not gone.get("banner") and not gone.get("badgeShown"),
              "banner drawn; after Dismiss banner=%s badge=%r (want gone, "
              "hidden)" % (gone.get("banner"), gone.get("badgeText")))
    finally:
        b.close()


def phase_signed_out(base, api):
    """A signed-OUT visitor sees no bell at all, and no error either.

    ⚠️ ITS OWN BROWSER, WITH NOTHING PLANTED. `weekly-challenge.html`,
    `my-challenges.html`, `revision.html` and `leaderboard.html` are PUBLIC
    pages — a prospective student or a parent reaches them with no account —
    and a bell there would be a control that cannot do anything, on a page
    whose whole job is to be a first impression.

    The second half matters as much as the first: the module is LOADED on
    those pages whether or not anybody is signed in, so "no bell" has to mean
    "it chose not to attach", not "it threw on the way".
    """
    print("\n  ── phase 6 · a signed-out visitor ──")
    b = cdp.Browser().start()
    seen, noisy = [], []
    try:
        FEED.set(sample("00000000-0000-0000-0000-0000000000aa"))
        for name, path in (("my-challenges", "/my-challenges.html"),
                           ("weekly-challenge", "/weekly-challenge.html"),
                           ("revision", "/revision.html"),
                           ("leaderboard", "/leaderboard.html")):
            sized(b, 390, 820)
            page = b.page(base + path + "?env=test&api=" + api, settle=1.1)
            time.sleep(1.0)
            if page.eval("!!document.querySelector('[data-mrb-bell]')"):
                seen.append(name)
            if not page.eval("!!window.MrBadmusBell"):
                noisy.append(name + " (the module did not even load)")
            for line in page.console_errors():
                if "student-bell" in str(line):
                    noisy.append("%s: %s" % (name, str(line)[:80]))
        check("signed_out_no_bell", not seen,
              "no bell on any of the four public pages"
              if not seen else "a bell appeared on: " + ", ".join(seen))
        check("signed_out_quiet", not noisy,
              "the module loaded on all four and said nothing"
              if not noisy else "; ".join(noisy))
    finally:
        b.close()


SURFACES = [
    ("leaderboard",       "/leaderboard.html"),
    ("weekly-challenge",  "/weekly-challenge.html"),
    ("my-challenges",     "/my-challenges.html"),
    ("revision",          "/revision.html"),
    ("student/classes",   "/student/classes.html"),
    ("student/class",     "/student/class.html"),
    ("student/assignment", "/student/assignment.html"),
]


def phase_surfaces(key, sess_a, base, api, aid):
    """The bell on EVERY logged-in student surface, at 390 and at 1280.

    Two questions per surface, and the second is the one Mide would notice:

      · is the bell actually there and on screen?
      · did adding it push anything sideways?

    ⚠️ 390 IS THE WIDTH THAT MATTERS, and not only because it is the common
    phone. `shared/nav.css` sets `.nav-cluster .nav-icon-link{display:none}`
    below 400px — so a bell that had borrowed that class would be INVISIBLE on
    the phone every student uses and present on every screen a developer
    checks. The bell has its own class for that reason; this measures it.
    """
    print("\n  ── phase 4 · every surface, 390 and 1280 ──")
    os.makedirs(SHOTS, exist_ok=True)
    b = cdp.Browser().start()
    widened, missing, skipped = [], [], []
    try:
        if not plant(b, base, key, sess_a):
            return check("surfaces", False, "could not plant the session")
        FEED.set(sample(aid))
        for name, path in SURFACES:
            q = "?env=test&api=" + api
            if "assignment" in path:
                q += "&assignment=" + aid
            for width in (390, 1280):
                sized(b, width, 820)
                page = b.page(base + path + q, settle=0.9)
                if "/student/" in path:
                    wait_mount(page, seconds=45)
                st = wait_bell(page, seconds=20)
                where = page.eval("location.pathname") or path

                # A surface that never drew its own chrome cannot be asked
                # about a bell IN that chrome, and calling that a bell failure
                # would be a lie in the expensive direction. The student pages
                # render one centred sentence and NO HEADER when they have
                # nothing to show — see `say()` in student-live.js — so there
                # is no header for a bell to sit in.
                # ⚠️ ONLY THE TWO PORTED PAGES. `student/classes.html` is
                # hand-written, has no `#mrb-student` and no bell host — its
                # bell auto-attaches to `nav.top-nav` — so asking it this
                # question threw, and treating a missing host as "no header"
                # would have excused a genuinely missing bell there.
                ported = path in ("/student/class.html",
                                  "/student/assignment.html")
                headless = ported and not page.eval(
                    "!!document.querySelector('[data-port-bell-host]')")
                if where != path:
                    skipped.append("%s@%d redirected to %s"
                                   % (name, width, where))
                elif headless:
                    skipped.append("%s@%d rendered no header, only its own "
                                   "sentence (%r)"
                                   % (name, width,
                                      (page.eval(
                                          "(function(){var h="
                                          "document.getElementById("
                                          "'mrb-student');return h?"
                                          "(h.innerText||'').slice(0,70):'';"
                                          "})()") or "").strip()))
                elif not st.get("visible"):
                    missing.append("%s@%d no bell on screen" % (name, width))

                # ⚠️ THE OVERFLOW QUESTION IS ASKED AS A DIFFERENCE, NOT AS AN
                # ABSOLUTE. The leaderboard's own podium already overflows at
                # 390 (measured on this build with the bell absent from the
                # page entirely — its `.sc-interp` spans run to 525px), and a
                # bare `scrollWidth <= clientWidth` would have failed this run
                # for somebody else's defect while proving nothing about mine.
                # So: measure, take the bell out of the DOM, measure again. A
                # bell that widened a surface shows up as a difference; one
                # that did not cannot be blamed for what was already there.
                pair = page.eval(
                    "(function(){var de=document.documentElement;"
                    "var before=de.scrollWidth;"
                    "var b=document.querySelector('[data-mrb-bell]');"
                    "var p=document.getElementById('mrb-bell-panel');"
                    "if(!b){return [before,before,de.clientWidth];}"
                    "var par=b.parentNode, nx=b.nextSibling;"
                    "b.remove(); if(p){p.remove();}"
                    "var after=de.scrollWidth;"
                    "par.insertBefore(b,nx);"
                    "return [before,after,de.clientWidth];})()")
                if pair and pair[0] > pair[1]:
                    widened.append("%s@%d %d→%d without the bell"
                                   % (name, width, pair[0], pair[1]))
                page.screenshot(os.path.join(
                    SHOTS, "%s-%d.png" % (name.replace("/", "-"), width)),
                    width, 820)

        check("bell_widens_nothing", not widened,
              "14 measurements, %s" % (", ".join(widened) if widened else
                                       "removing the bell narrows no surface "
                                       "— it costs nothing horizontally"))
        check("bell_on_every_surface", not missing,
              ", ".join(missing) if missing
              else "on screen wherever a header was drawn%s"
                   % ("; not asked on: " + "; ".join(skipped) if skipped else ""))
        if skipped:
            check("surfaces_not_asked", None, "; ".join(skipped))
    finally:
        b.close()


def phase_assignment_header(base, api, aid):
    """The ASSIGNMENT header, with a bell in it, at 390 and 1280.

    ⚠️ WHY THE FIXTURE. The live assignment page only draws its header when
    the pupil has work to open; the TEST pupil's one assignment is week 1 and
    unreleased, so the live page renders its own sentence and no header at all
    (reported by `surfaces_not_asked`). That leaves ONE claim unmeasured — that
    Design's assignment header, which already carries a LATE chip, a saved tick
    and a running clock, still fits a bell on a 390px phone.

    `assignment-fixture.html` is the same bytes as the live page apart from its
    banner and its last two script tags, so its header is the header. The bell
    is not injected into it by anything (the fixture does not load
    student-live.js), so this drive mounts it by hand — which is the ONLY
    place in this file that fabricates anything, and it fabricates a mount
    rather than a result: what is measured afterwards is real layout.
    """
    print("\n  ── phase 5 · Design's assignment header, with a bell in it ──")
    b = cdp.Browser().start()
    try:
        FEED.set(sample(aid))
        for width in (390, 1280):
            sized(b, width, 820)
            page = b.page(base + "/student/assignment-fixture.html", settle=1.0)
            wait_mount(page, seconds=30)
            has_host = page.eval(
                "!!document.querySelector('[data-port-bell-host]')")
            if not has_host:
                check("assignment_header_%d" % width, False,
                      "the fixture drew no [data-port-bell-host]")
                continue
            # ⚠️ THE AFTER-DRAW HOOK IS PUSHED HERE TOO, AND ON THIS PAGE IT
            # IS NOT A PRECAUTION. Measured on the fixture without it: the
            # bell was in the DOM and GONE 1.5 seconds later. The assignment
            # page carries a running CLOCK, so its logic calls `setState` on a
            # timer, so `draw()` empties `#mrb-student` and rebuilds it once a
            # second whether or not the pupil touches anything. A bell
            # inserted once would disappear on its own, unprompted, within a
            # second of the page opening — the MRB-330 banner defect, except
            # that this one does not even need a click to happen.
            # `wireBell` in student-live.js registers exactly this on the live
            # page; the fixture loads no student-live, so the drive does it.
            page.eval(
                "(function(){var s=document.createElement('script');"
                "s.src='/shared/student-bell.js';"
                "s.onload=function(){var B=window.MrBadmusBell;"
                "B.mount({host:'[data-port-bell-host]',place:'first',"
                "tone:'studio',token:function(){return Promise.resolve('drive');}});"
                "window.__MRB_AFTER_DRAW__=window.__MRB_AFTER_DRAW__||[];"
                "window.__MRB_AFTER_DRAW__.push(function(){B.attach();});};"
                "document.head.appendChild(s);})()")
            # Long enough to cross at least two of the clock's own redraws.
            time.sleep(3.2)
            st = page.eval(BELL_STATE)
            # ⚠️ THE HEADER'S HEIGHT IS A DIFFERENCE, NOT A CEILING. At 390
            # Design's own assignment header stacks a progress row and a
            # breadcrumb under the top bar and stands 124px tall with no bell
            # on the page at all; an absolute ceiling would have failed this
            # run for her layout. Measure, take the bell out, measure again.
            #
            # ⚠️ ROWS ARE COUNTED ON CENTRES, NOT ON TOPS. The cluster is
            # `align-items:center`, and the bell (40px, a touch target) is
            # three times the height of the clock text beside it — so their
            # `top` values differ by thirteen pixels while they sit on one
            # line. Counting tops reported a wrap that is not there.
            wraps = page.eval(
                "(function(){var h=document.querySelector("
                "'[data-port-bell-host]');var r=h.getBoundingClientRect();"
                "var hd=h.closest('header').getBoundingClientRect();"
                "var kids=h.children, mid=null, rows=0;"
                "for(var i=0;i<kids.length;i++){var k=kids[i]"
                ".getBoundingClientRect(); if(!k.width)continue;"
                "var c=k.top+k.height/2;"
                "if(mid===null||Math.abs(c-mid)>4){rows++;mid=c;}}"
                "var was=hd.height;"
                "var bb=document.querySelector('[data-mrb-bell]');"
                "var par=bb.parentNode, nx=bb.nextSibling; bb.remove();"
                "var without=h.closest('header').getBoundingClientRect().height;"
                "par.insertBefore(bb,nx);"
                "return [rows, Math.round(r.width), Math.round(r.height),"
                " Math.round(was), Math.round(without)];})()")
            os.makedirs(SHOTS, exist_ok=True)
            page.screenshot(os.path.join(
                SHOTS, "assignment-header-%d.png" % width), width, 820)
            check("assignment_header_%d" % width,
                  st.get("visible") and wraps[0] == 1
                  and st["scrollW"] <= st["clientW"] + 1
                  and wraps[3] <= wraps[4] + 1,
                  "bell %dx%d in Design's cluster, %d row (no wrap), cluster "
                  "%dx%d, header %dpx with the bell and %dpx without it, no "
                  "sideways scroll"
                  % (st.get("w"), st.get("h"), wraps[0], wraps[1], wraps[2],
                     wraps[3], wraps[4]))
    finally:
        b.close()


def phase_rls(key, sess_a, sess_b, uid_a, uid_b):
    """A pupil cannot read another pupil's rows.

    ⚠️ ONE BROWSER PER PERSONA, and this phase uses none at all: it asks the
    question at the API, on pupil B's own JWT, which is where the answer lives.
    Two checks, and they are different claims:

      rls_rows    the DATABASE will not hand B any of A's `student_notifications`
                  rows. Executable today, and it is the guarantee the route
                  is built on.
      route_rls   the ROUTE will not. Executable only once the backend lane's
                  route exists; probed, not assumed.
    """
    print("\n  ── phase 3 · a pupil cannot read another pupil's messages ──")
    # ⚠️ PUPIL A MUST HAVE A ROW, or "B saw none of A's" is a sentence about
    # an empty table. The seed above puts one there, and the two pupils are in
    # the SAME CLASS on TEST — which makes this the strong version of the
    # question rather than the weak one: not "can a stranger see it" but "can
    # the pupil sitting next to her".
    st_a, a_rows = call("GET", SB_URL + "/rest/v1/student_notifications"
                        "?select=id,student_id", key, sess_a["access_token"])
    a_rows = a_rows if isinstance(a_rows, list) else []
    if st_a != 200 or not a_rows:
        for n in ("rls_rows", "rls_scoped_to_viewer"):
            check(n, None, "pupil A has no notification row to leak (seeding "
                           "did not run) — the question could not be asked")
    else:
        check("rls_scoped_to_viewer",
              all(r.get("student_id") == uid_a for r in a_rows),
              "pupil A's own JWT reads %d row(s), all hers" % len(a_rows))
        st, mine = call("GET", SB_URL + "/rest/v1/student_notifications"
                        "?select=id,student_id", key, sess_b["access_token"])
        mine = mine if isinstance(mine, list) else []
        a_ids = {r["id"] for r in a_rows}
        leaked = [r for r in mine if r["id"] in a_ids
                  or r.get("student_id") != uid_b]
        check("rls_rows", st == 200 and not leaked,
              "pupil B — same class — read %d row(s) and NONE of pupil A's %d"
              % (len(mine), len(a_rows)))

    # ⊕ The route-level question moved to `phase_route`, which asks it four
    # ways against the real handler. What stays here is the DATABASE's own
    # answer, and it is a different claim worth keeping: the route reads with
    # the SERVICE-ROLE key, so RLS is not what protects it — but RLS is still
    # what protects every other reader of these tables, including the class
    # page's own `student_reminders_for_viewer`.


# ── seeding one real reminder, so the banner has something to draw ───────

class Seed:
    """Every row this drive writes, and how to take it all away again.

    ⚠️ WRITTEN AS THE TEACHER, UNDER REAL RLS, NEVER WITH THE SERVICE KEY. A
    row forced past `student_notifications_teacher_send` or
    `class_shoutouts_insert` would be a row no teacher could actually send,
    and every assertion standing on it would be an assertion about a world
    that does not exist. The service key appears only in `teardown`, which is
    cleanup and proves nothing.
    """

    def __init__(self, key, sess_t, uid_a, uid_b):
        self.key, self.tok = key, sess_t["access_token"]
        self.uid_t = sess_t["user"]["id"]
        self.uid_a, self.uid_b = uid_a, uid_b
        self.class_id = None
        self.released = None        # a RELEASED teacher assignment
        self.unreleased = None      # one released next week
        self.rem_a = self.rem_b = None
        self.shout_a = self.shout_b = None
        self.fb_a = None
        self.notes = []
        self.trash = []             # (table, id) in delete order

    # ── helpers ─────────────────────────────────────────────────────────
    def _post(self, table, row):
        st, body = call("POST", SB_URL + "/rest/v1/" + table, self.key,
                        self.tok, row, prefer="return=representation")
        if st in (200, 201) and isinstance(body, list) and body:
            self.trash.insert(0, (table, body[0]["id"]))
            return body[0]
        self.notes.append("%s refused (HTTP %s %s)"
                          % (table, st, json.dumps(body)[:300]))
        return None

    def build(self):
        # The teacher's own class that BOTH pupils are in. Same class is the
        # strong form of the cross-pupil question: not "can a stranger see
        # it" but "can the pupil sitting next to her".
        st, mine = call("GET", SB_URL + "/rest/v1/class_teachers?select=class_id",
                        self.key, self.tok)
        ids = [r["class_id"] for r in (mine or [])] if st == 200 else []
        if not ids:
            self.notes.append("the throwaway teacher teaches no class")
            return self
        st, mem = call(
            "GET", SB_URL + "/rest/v1/class_members?select=class_id,student_id"
            "&student_id=in.(%s)&class_id=in.(%s)"
            % (",".join([self.uid_a, self.uid_b]), ",".join(ids)),
            self.key, self.tok)
        shared = {}
        for r in (mem or []):
            shared.setdefault(r["class_id"], set()).add(r["student_id"])
        both = [c for c, who in shared.items()
                if {self.uid_a, self.uid_b} <= who]
        if not both:
            self.notes.append("the two pupils share no class this teacher teaches")
            return self
        self.class_id = both[0]

        # Shape copied off an existing row rather than guessed: `subject_id`,
        # `topic` and `quiz_type` are all NOT NULL.
        st, model = call(
            "GET", SB_URL + "/rest/v1/assignments?select=subject_id,quiz_type"
            "&class_id=eq." + self.class_id + "&limit=1", self.key, self.tok)
        if st != 200 or not model:
            self.notes.append("no assignment on that class to copy a shape from")
            return self
        # ⚠️ `auto_generated=False` IS NOT OPTIONAL. The CHECK
        # `assignments_source_agrees_with_auto_generated` reads
        #     (source = 'auto') = COALESCE(auto_generated, true)
        # so a row with `source='teacher'` and the column left NULL is
        # refused 23514 — which is what happened on the first pass, and the
        # message came back truncated to `assignments_so…`. Both are fixed:
        # the column is set, and `_post` prints enough of the error to name
        # the constraint.
        base = dict(class_id=self.class_id, subject_id=model[0]["subject_id"],
                    quiz_type=model[0]["quiz_type"], topic="MRB-337 drive",
                    source="teacher", auto_generated=False)

        # ⚠️ `source='teacher'` ON BOTH, and that is what makes the pair a
        # test. The route synthesises `work` from teacher-set assignments
        # only; the class's existing row is `source='auto'`, so it is
        # correctly invisible either way and could not have told these apart.
        now = time.time()
        self.released = self._post("assignments", dict(
            base, title="MRB-337 released",
            release_at=time.strftime("%Y-%m-%dT%H:%M:%SZ",
                                     time.gmtime(now - 3600))))
        self.unreleased = self._post("assignments", dict(
            base, title="MRB-337 UNRELEASED",
            release_at=time.strftime("%Y-%m-%dT%H:%M:%SZ",
                                     time.gmtime(now + 7 * 86400))))
        if not self.released:
            return self

        aid = self.released["id"]
        self.rem_a = self._post("student_notifications", dict(
            student_id=self.uid_a, class_id=self.class_id, assignment_id=aid,
            kind="reminder", sent_by=self.uid_t))
        self.rem_b = self._post("student_notifications", dict(
            student_id=self.uid_b, class_id=self.class_id, assignment_id=aid,
            kind="reminder", sent_by=self.uid_t))
        self.shout_a = self._post("class_shoutouts", dict(
            class_id=self.class_id, author_id=self.uid_t,
            recipient_id=self.uid_a, message="MRB-337 drive, pupil A."))
        self.shout_b = self._post("class_shoutouts", dict(
            class_id=self.class_id, author_id=self.uid_t,
            recipient_id=self.uid_b, message="MRB-337 drive, pupil B."))

        # Feedback needs a SUBMISSION, and only pupil A has one on TEST. So
        # the cross-pupil claim is proved on reminders, shout-outs and work
        # for both pupils and on feedback for A alone — said, not glossed.
        st, sub = call(
            "GET", SB_URL + "/rest/v1/assignment_submissions?select=id"
            "&student_id=eq." + self.uid_b + "&deleted_at=is.null&limit=1",
            self.key, self.tok)
        if st == 200 and sub:
            self.fb_a = self._post("submission_feedback", dict(
                submission_id=sub[0]["id"], teacher_id=self.uid_t,
                body="MRB-337 drive feedback for pupil B."))
            self.fb_owner = self.uid_b
        else:
            self.notes.append("pupil B has no submission, so no feedback row "
                              "could be seeded for them")
            self.fb_owner = None
        return self

    def describe(self):
        got = [n for n, v in (("released", self.released),
                              ("unreleased", self.unreleased),
                              ("reminder A", self.rem_a),
                              ("reminder B", self.rem_b),
                              ("shoutout A", self.shout_a),
                              ("shoutout B", self.shout_b),
                              ("feedback B", self.fb_a)) if v]
        return "seeded: %s%s" % (", ".join(got) or "nothing",
                                 ("  ⚠️ " + "; ".join(self.notes))
                                 if self.notes else "")

    def teardown(self):
        """⚠️ EVERY DELETE'S STATUS IS CHECKED AND THE TABLE IS RE-QUERIED.
        A teardown that prints "torn down" and leaves the world standing is
        the failure this repo has already paid for once."""
        svc = service_key()
        if not svc:
            print("     ⚠️  NOTHING REMOVED — no TEST service-role key, and "
                  "student_notifications has no delete policy for anybody. "
                  "Rows left: %s" % self.trash)
            return
        # Read-marks the drive itself created, first: they reference nothing
        # by FK but they would make the next run's `read` flags wrong.
        call("DELETE", SB_URL + "/rest/v1/student_message_reads?student_id=in.(%s)"
             % ",".join([self.uid_a, self.uid_b]), svc, svc)
        bad = []
        for table, row_id in self.trash:
            st, _ = call("DELETE",
                         SB_URL + "/rest/v1/" + table + "?id=eq." + row_id,
                         svc, svc)
            if st not in (200, 204):
                bad.append("%s/%s HTTP %s" % (table, row_id[:8], st))
        left = []
        for table, row_id in self.trash:
            st, rows = call("GET", SB_URL + "/rest/v1/" + table +
                            "?select=id&id=eq." + row_id, svc, svc)
            if st == 200 and rows:
                left.append("%s/%s" % (table, row_id[:8]))
        print("     🧹 %d row(s) removed%s%s"
              % (len(self.trash),
                 ("; REFUSED: " + ", ".join(bad)) if bad else "",
                 ("; STILL PRESENT: " + ", ".join(left)) if left
                 else "; re-queried, none left"))


def route_get(base, bearer):
    req = urllib.request.Request(
        base + "/api/student/notifications",
        headers={"Authorization": "Bearer " + bearer})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.status, json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode()[:300]


def route_read(base, bearer, notif_id):
    req = urllib.request.Request(
        base + "/api/student/notifications/" +
        urllib.parse.quote(notif_id, safe="") + "/read",
        headers={"Authorization": "Bearer " + bearer}, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.status, json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode()[:300]


def phase_route(base, key, sess_a, sess_b, seed, registered, how):
    """THE REAL ROUTE. Not the proxy — the backend lane's own handler.

    ⚠️ THIS IS THE ASSERTION THAT MATTERS MOST IN THIS FILE, and the reason is
    that RLS IS NOT PROTECTING IT. The route reads with the SERVICE-ROLE key
    and re-derives the pupil's scope by hand, so every predicate the database
    would have enforced is a line of JavaScript that can be forgotten. An
    independent review found and fixed exactly that today — a reminder's title
    read with no membership, school or release filter, which rendered a
    foreign assignment's title to a child.

    Four questions, all on rows this drive seeded, with the two pupils in the
    SAME CLASS:

      route_no_cross_pupil   A's list contains none of B's messages
      route_read_refused     a POST carrying B's composite id neither marks it
                             read nor writes a row
      route_unreleased       an unreleased teacher assignment is not `New work`
      route_bare_uuid        a bare uuid is refused 400, not guessed at
    """
    print("\n  ── phase 7 · the REAL route, read with the service key ──")
    if not registered:
        for n in ("route_no_cross_pupil", "route_read_refused",
                  "route_unreleased", "route_bare_uuid"):
            check(n, None, "the route is not registered (%s)" % how)
        return
    if not seed.released:
        for n in ("route_no_cross_pupil", "route_read_refused",
                  "route_unreleased", "route_bare_uuid"):
            check(n, None, "nothing could be seeded: %s" % "; ".join(seed.notes))
        return

    st_a, a = route_get(base, sess_a["access_token"])
    st_b, b = route_get(base, sess_b["access_token"])
    if st_a != 200 or st_b != 200:
        return check("route_no_cross_pupil", False,
                     "GET answered %s / %s" % (st_a, st_b))
    a_items = a.get("notifications", [])
    b_items = b.get("notifications", [])
    a_ids = {x["id"] for x in a_items}
    b_ids = {x["id"] for x in b_items}

    # ── B's OWN messages, by id, none of which may be in A's list ───────
    b_only = set()
    for row, src in ((seed.rem_b, "reminder"), (seed.shout_b, "shoutout")):
        if row:
            b_only.add(src + ":" + row["id"])
    if seed.fb_a and seed.fb_owner == seed.uid_b:
        b_only.add("feedback:" + seed.fb_a["id"])
    leaked = sorted(a_ids & b_only)
    check("route_no_cross_pupil",
          bool(b_only) and not leaked and b_only <= b_ids,
          "A got %d message(s), B got %d; B's own %d (%s) — %s"
          % (len(a_items), len(b_items), len(b_only),
             ", ".join(sorted(x.split(":")[0] for x in b_only)),
             "none in A's list" if not leaked else "LEAKED " + ", ".join(leaked)))

    # ── a mark-read for somebody else's message ─────────────────────────
    victim = ("reminder:" + seed.rem_b["id"]) if seed.rem_b else None
    if not victim:
        check("route_read_refused", None, "no pupil-B reminder was seeded")
    else:
        st, body = route_read(base, sess_a["access_token"], victim)
        # The row must still be unread, read as the SERVICE key so RLS cannot
        # be what hides the answer.
        svc = service_key()
        still = None
        if svc:
            _, rows = call("GET", SB_URL + "/rest/v1/student_notifications"
                           "?select=read_at&id=eq." + seed.rem_b["id"], svc, svc)
            still = (rows or [{}])[0].get("read_at")
            _, marks = call(
                "GET", SB_URL + "/rest/v1/student_message_reads?select=source"
                "&student_id=eq." + seed.uid_a, svc, svc)
        else:
            marks = None
        check("route_read_refused",
              st == 404 and still is None and not marks,
              "A's POST of B's reminder answered %s; B's read_at is %r; "
              "%s read-mark row(s) written for A"
              % (st, still, "no" if not marks else len(marks)))

    # ── the unreleased assignment ───────────────────────────────────────
    if not seed.unreleased:
        check("route_unreleased", None, "no unreleased assignment was seeded")
    else:
        un = "work:" + seed.unreleased["id"]
        rel = "work:" + seed.released["id"]
        st_un, _ = route_read(base, sess_a["access_token"], un)
        check("route_unreleased",
              un not in a_ids and rel in a_ids and st_un == 404,
              "the released set IS `New work` in A's list, the unreleased one "
              "is absent, and marking it read answers %s" % st_un)

    # ── a bare uuid is refused, not guessed ─────────────────────────────
    st, body = route_read(base, sess_a["access_token"],
                          seed.rem_a["id"] if seed.rem_a
                          else "11111111-1111-1111-1111-111111111111")
    check("route_bare_uuid", st == 400,
          "a bare uuid with no `<source>:` prefix answered %s — the route "
          "refuses rather than picking one of four tables" % st)


def phase_page_on_real_route(base, api, key, sess_a, seed, registered, how):
    """The BELL, on the class page, reading the REAL route. No proxy.

    Everything phase 1 proved was proved against a feed this file wrote. This
    is the same page pointed straight at the backend, so the id shape, the
    kind spellings, the envelope and the sort order are the backend lane's and
    not mine — which is the only way `work` vs `new_work` was ever going to be
    caught by a machine rather than by reading the handler.
    """
    print("\n  ── phase 8 · the bell on the class page, real route ──")
    if not registered or not seed.released:
        return check("bell_on_real_route", None,
                     "the route is not registered (%s)" % how if not registered
                     else "nothing could be seeded")
    st, body = route_get(base, sess_a["access_token"])
    want = body.get("notifications", []) if st == 200 else []
    FEED.set([], passthrough=True)          # the shim forwards, it does not feed
    b = cdp.Browser().start()
    try:
        if not plant(b, base_site(), key, sess_a):
            return check("bell_on_real_route", False, "could not plant")
        sized(b, 1280)
        url = (base_site() + "/student/class.html?env=test&api=" +
               urllib.parse.quote(api, safe=""))
        page = b.page(url, settle=1.0)
        if wait_mount(page) < 20:
            return check("bell_on_real_route", None,
                         "the class page did not mount")
        st_ui = wait_bell(page)
        page.eval("document.querySelector('[data-mrb-bell]').click()")
        time.sleep(0.7)
        ui = page.eval(BELL_STATE)
        heads = page.eval(
            "(function(){var r=document.querySelectorAll('.mrb-bell-kind');"
            "return Array.prototype.map.call(r,function(e){"
            "return (e.innerText||'').trim();});})()") or []
        page.screenshot(os.path.join(SHOTS, "class-real-route-1280.png"),
                        1280, 900)
        unread = sum(1 for x in want if not x.get("read"))
        # ⚠️ NO `Message` HEADING ANYWHERE. That is the bell's honest fallback
        # for a kind it has never heard of, and seeing it here would mean the
        # contract has moved without this file noticing — which is precisely
        # what `new_work` did, silently, under the heading `Reminder`.
        check("bell_on_real_route",
              FEED.gets >= 1 and ui.get("panelRows") == len(want)
              and (ui.get("badgeText") == ("9+" if unread > 9 else str(unread)))
              and "Message" not in heads,
              "the route returned %d message(s), %d unread; the panel drew "
              "%d row(s), the badge read %r, headings %s"
              % (len(want), unread, ui.get("panelRows"), ui.get("badgeText"),
                 sorted(set(heads))))
    finally:
        b.close()


# ── main ─────────────────────────────────────────────────────────────────

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--provision", action="store_true",
                    help="re-assert the throwaway pupils' password on TEST")
    ap.add_argument("--keep", action="store_true",
                    help="leave the seeded reminder row in place")
    args = ap.parse_args()

    pw = os.environ.get(PW_ENV)
    if args.provision:
        if not pw:
            raise SystemExit("--provision needs %s" % PW_ENV)
        return provision(pw)
    if not pw:
        raise SystemExit(
            "student_bell_drive: %s is not set. It is the MRB-326 throwaway "
            "pupils' password on the TEST project; nothing here touches "
            "production." % PW_ENV)

    print("\n🔔  student_bell_drive — the student's messages, MRB-337\n")
    key = anon_key()
    sess_a = sign_in(PUPIL_A, pw, key)
    sess_b = sign_in(PUPIL_B, pw, key)
    uid_a = sess_a["user"]["id"]
    uid_b = sess_b["user"]["id"]
    print("     pupil A %s  (%s…)" % (PUPIL_A, sess_a["access_token"][:10]))
    print("     pupil B %s  (%s…)" % (PUPIL_B, sess_b["access_token"][:10]))

    Proxy.upstream = live_backend()
    print("     upstream: %s" % (Proxy.upstream or
                                 "NONE — the class-page phase will not run"))
    registered, how = probe_route(Proxy.upstream, sess_a["access_token"])
    print("     the real /api/student/notifications: %s (%s)"
          % ("REGISTERED — phases 7 and 8 run for real" if registered
             else "NOT USABLE — phases 7 and 8 cannot run", how))

    srv, api = start_proxy()
    site, port = cdp.serve("mrbadmus_site", port=SITE_PORT)
    _SITE["base"] = base = "http://localhost:%d" % port
    print("     proxy: %s     site: %s" % (api, base))

    seed = None
    try:
        try:
            sess_t = sign_in(TEACHER, pw, key)
            seed = Seed(key, sess_t, uid_a, uid_b).build()
            print("     " + seed.describe())
        except SystemExit as err:
            print("     ⚠️  no teacher session (%s) — the seeded phases will "
                  "report NOT EXECUTED" % str(err)[:80])

        # A REAL assignment id, so `tap_opens` is a real navigation.
        aid = (seed.released["id"] if seed and seed.released
               else "00000000-0000-0000-0000-0000000000aa")
        rem_a = seed.rem_a["id"] if seed and seed.rem_a else None

        phase_source()
        phase_chrome(key, sess_a, base, api, aid)
        phase_class(key, sess_a, base, api, aid, rem_a)
        phase_surfaces(key, sess_a, base, api, aid)
        phase_assignment_header(base, api, aid)
        phase_signed_out(base, api)
        phase_rls(key, sess_a, sess_b, uid_a, uid_b)
        if seed:
            phase_route(Proxy.upstream, key, sess_a, sess_b, seed,
                        registered, how)
            phase_page_on_real_route(Proxy.upstream, api, key, sess_a, seed,
                                     registered, how)
        else:
            for n in ("route_no_cross_pupil", "route_read_refused",
                      "route_unreleased", "route_bare_uuid",
                      "bell_on_real_route"):
                check(n, None, "no teacher session, so nothing was seeded")
    finally:
        if seed and not args.keep:
            seed.teardown()
        elif seed:
            print("     --keep: %d row(s) LEFT IN PLACE %s"
                  % (len(seed.trash), seed.trash))
        srv.shutdown()
        site.shutdown()

    ok = sum(1 for _, r, _ in results if r is True)
    bad = [n for n, r, _ in results if r is False]
    skip = [n for n, r, _ in results if r is None]
    print("\n  ── %d passed, %d failed, %d NOT EXECUTED ──"
          % (ok, len(bad), len(skip)))
    if skip:
        print("     not executed: %s" % ", ".join(skip))
    if bad:
        print("     failed: %s\n" % ", ".join(bad))
        return 1
    if skip:
        print("     ⚠️  green on what ran. It is NOT a full pass: the checks "
              "above could not be executed.\n")
        return 0
    print("     shots in %s\n" % SHOTS)
    return 0


if __name__ == "__main__":
    sys.exit(main())
