#!/usr/bin/env python3
"""test_isolation_drive.py — prove, in a real browser, that a TEST page never
even TRIES to reach production, and that the tutor is honest when it cannot
answer.

⊕ Mide's ruling, 5 Oct 2026. SLOW gate (headless Chrome). The fast half is
`test_isolation_check.py` (no shipped file names production; config.js runs
before every reader). This half watches what a page actually does.

── WHAT IT DRIVES ─────────────────────────────────────────────────────────

Four page families, each opened on `?env=test&api=http://127.0.0.1:<stub>`:
a KS3 lesson, a KS4 subtopic page, `student/class.html` and a consumer page
(with `CONSUMER_SIGNUP_ENABLED` forced on by an init script — it is off on
TEST on purpose). A fake, unexpired session is planted under BOTH the test
project's storage key and the production one, so any code still reading the
production slot would believe it was signed in and act on it.

Every request the page makes is recorded from CDP `Network.requestWillBeSent`
— NOTHING IS BLOCKED. A request to any host on the production backend's platform or to the
production Supabase host is a failure, as is a preconnect/dns-prefetch hint
for either. Blocking those hosts would hide exactly the defect this gate
exists to catch; it must observe that nothing even tries.

The tutor, on the KS3 lesson and the KS4 page, is then asked about
photosynthesis — the question that used to produce a canned "fact card" —
against a stub backend that (a) answers 500, (b) refuses with a 429 and a
readable sentence, and (c) is not running at all. (a) and (c) must show the
one honest line; (b) must show the backend's own sentence; none may show a
fact card.

Finally config.js is loaded on `?env=prod` in an empty document (no page, no
pupil traffic) and must resolve the production backend, project and session
key exactly as before.

`--backend URL` drives a real local backend instead of the stub for the
four-page sweep and one tutor question (used for the TEST proof run).
`--shots DIR` writes light/dark screenshots at 1280 and 390.
"""
import argparse
import http.server
import json
import os
import re
import sys
import threading
import time
import uuid
from urllib.parse import urlparse

import ks3_browser as kb
import config_env  # noqa: E402 — shared/config.js's worlds (B2C unit 6)

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.join(ROOT, "mrbadmus_site")

UNAVAILABLE = "The tutor's unavailable right now. Try again in a few minutes."
LIMIT_MSG = "You've used today's 20 tutor questions. They reset at midnight."


def prod_values():
    """The PROD block of shared/config.js — the one place it is written."""
    src = open(os.path.join(ROOT, "shared", "config.js"), encoding="utf-8").read()
    block = src[src.index("const PROD = {"):src.index("};", src.index("const PROD = {"))]
    url = re.search(r"SUPABASE_URL:\s*'([^']+)'", block).group(1)
    be = re.search(r"BACKEND_URL:\s*'([^']+)'", block).group(1)
    ref = re.match(r"https://([a-z0-9]+)\.supabase\.co", url).group(1)
    return {"SUPABASE_URL": url, "BACKEND_URL": be, "ref": ref,
            "AUTH_STORAGE_KEY": "sb-%s-auth-token" % ref}


def test_ref():
    src = open(os.path.join(ROOT, "shared", "config.js"), encoding="utf-8").read()
    block = src[src.index("const TEST = {"):]
    url = re.search(r"SUPABASE_URL:\s*'([^']+)'", block).group(1)
    return re.match(r"https://([a-z0-9]+)\.supabase\.co", url).group(1)


# ── the stub backend ─────────────────────────────────────────────────────
class Stub:
    mode = "500"
    hits = []
    probe_html = ""

    @classmethod
    def handler(cls):
        stub = cls

        class H(http.server.BaseHTTPRequestHandler):
            def log_message(self, *a):
                pass

            def _cors(self):
                self.send_header("Access-Control-Allow-Origin", self.headers.get("Origin") or "*")
                self.send_header("Access-Control-Allow-Headers", "Authorization, Content-Type")
                self.send_header("Access-Control-Allow-Methods", "GET, POST, PUT, PATCH, DELETE, OPTIONS")
                self.send_header("Vary", "Origin")

            def _json(self, code, body):
                data = json.dumps(body).encode()
                self.send_response(code)
                self._cors()
                self.send_header("Content-Type", "application/json")
                self.send_header("Content-Length", str(len(data)))
                self.end_headers()
                self.wfile.write(data)

            def do_OPTIONS(self):
                self.send_response(204)
                self._cors()
                self.end_headers()

            def do_GET(self):
                stub.hits.append(("GET", self.path))
                if self.path.startswith("/probe.html"):
                    data = stub.probe_html.encode()
                    self.send_response(200)
                    self.send_header("Content-Type", "text/html")
                    self.send_header("Content-Length", str(len(data)))
                    self.end_headers()
                    self.wfile.write(data)
                    return
                if self.path.startswith("/api/health"):
                    return self._json(200, {"ok": True})
                return self._json(404, {"error": "not_found"})

            def _any(self):
                n = int(self.headers.get("Content-Length") or 0)
                if n:
                    self.rfile.read(n)
                stub.hits.append((self.command, self.path))
                if self.path.startswith("/api/chat"):
                    if stub.mode == "429":
                        return self._json(429, {"error": "cap_reached", "message": LIMIT_MSG})
                    return self._json(500, {"error": {"message": "Server error. Please try again."}})
                return self._json(404, {"error": "not_found"})

            do_POST = _any
            do_PUT = _any
            do_PATCH = _any
            do_DELETE = _any

        return H


def closed_port():
    import socket
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    p = s.getsockname()[1]
    s.close()
    return p


# ── the browser side ─────────────────────────────────────────────────────
def init_script(prod, tref, consumer, real_session=None):
    exp = int(time.time()) + 3600
    sess = {"access_token": "test-isolation-fake-token", "token_type": "bearer",
            "expires_at": exp, "expires_in": 3600, "refresh_token": "fake",
            "user": {"id": str(uuid.UUID(int=0x7e57)), "email": "isolation@example.invalid",
                     "user_metadata": {"first_name": "Iso"}}}
    js = ["(function(){try{var s=%s;" % json.dumps(json.dumps(sess)),
          "localStorage.setItem(%s,s);" % json.dumps(prod["AUTH_STORAGE_KEY"]),
          "localStorage.setItem(%s,%s);" % (json.dumps("sb-%s-auth-token" % tref),
                                             json.dumps(json.dumps(real_session)) if real_session else "s"),
          "}catch(e){}"]
    if consumer:
        js.append("var v;Object.defineProperty(window,'MrBadmusConfig',{configurable:true,"
                  "get:function(){return v;},set:function(x){if(x&&x.environment==='test')"
                  "{x.CONSUMER_SIGNUP_ENABLED=true;}v=x;}});")
    js.append("})();")
    return "".join(js)


class Recorder:
    def __init__(self, page):
        self.page = page
        self.urls = []

    def collect(self):
        self.page.drain(0.1)
        for ev in self.page._events:
            if ev.get("method") == "Network.requestWillBeSent":
                u = ev["params"]["request"]["url"]
                if u not in self.urls:
                    self.urls.append(u)
            elif ev.get("method") == "Network.webSocketCreated":
                u = ev["params"]["url"]
                if u not in self.urls:
                    self.urls.append(u)
        return self.urls


def is_prod(url, prod):
    h = (urlparse(url).hostname or "").lower()
    return config_env.is_prod_url(url) or h == urlparse(prod["SUPABASE_URL"]).hostname


def hints(page):
    return page.eval(
        "Array.prototype.map.call(document.querySelectorAll("
        "'link[rel=preconnect],link[rel=dns-prefetch]'),function(l){return l.href;})") or []


def ask_tutor(page, question, timeout=20.0):
    page.eval("window.MrBadmus && MrBadmus.open(), true")
    time.sleep(0.3)
    n0 = page.eval("document.querySelectorAll('.chat-msg--bot').length") or 0
    page.eval("window.MrBadmus && MrBadmus.ask(%s), true" % json.dumps(question))
    deadline = time.time() + timeout
    while time.time() < deadline:
        txt = page.eval(
            "(function(){var b=document.querySelectorAll('.chat-msg--bot .chat-msg__bubble');"
            "if(b.length<=%d)return null;var t=b[b.length-1];"
            "if(t.querySelector('.typing'))return null;return t.textContent;})()" % n0)
        if txt:
            return txt.strip()
        time.sleep(0.25)
    return None


def shoot(page, shots, name):
    if not shots:
        return []
    out = []
    for theme in ("light", "dark"):
        page.eval("document.documentElement.setAttribute('data-theme',%s);true" % json.dumps(theme))
        for w in (1280, 390):
            p = os.path.join(shots, "%s-%s-%d.png" % (name, theme, w))
            page.screenshot(p, width=w, height=900 if w == 1280 else 844, full_page=False)
            out.append(p)
    page.set_viewport(1280, 900)
    return out


PAGES = [
    ("ks3-lesson", "/ks3/biology/cells-and-organisation/animal-and-plant-cells.html", True),
    ("ks4-page", "/combined/higher/chemistry/rates-equilibrium.html", True),
    ("student-class", "/student/class.html", False),
    ("consumer", "/consumer/signup.html", False),
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--static-port", type=int, default=0)
    ap.add_argument("--chrome-port", type=int, default=0)
    ap.add_argument("--backend", default="", help="a real local backend instead of the stub")
    ap.add_argument("--shots", default="")
    ap.add_argument("--log", default="", help="write every observed request URL here (JSON)")
    ap.add_argument("--session-file", default="",
                    help="a real TEST session (JSON) to plant under the TEST key")
    a = ap.parse_args()

    if not os.path.isdir(SITE):
        print("test_isolation_drive: no mrbadmus_site/ — run python3 build_all.py")
        return 1
    for name, path, _ in PAGES:
        if not os.path.exists(os.path.join(SITE, path.lstrip("/"))):
            print("test_isolation_drive: FAIL — %s is missing from the build (%s)" % (path, name))
            return 1
    if a.chrome_port:
        kb.Browser._free_port = staticmethod(lambda: a.chrome_port)
    if a.shots:
        os.makedirs(a.shots, exist_ok=True)

    prod = prod_values()
    tref = test_ref()
    real = json.load(open(a.session_file)) if a.session_file else None
    fails, log = [], {}

    server, sport = kb.serve(SITE, a.static_port)
    origin = "http://127.0.0.1:%d" % sport
    stub_srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), Stub.handler())
    stub_srv.daemon_threads = True
    threading.Thread(target=stub_srv.serve_forever, daemon=True).start()
    stub = "http://127.0.0.1:%d" % stub_srv.server_address[1]
    api = a.backend.rstrip("/") if a.backend else stub
    print("static %s · api %s" % (origin, api))

    br = kb.Browser()
    try:
        page = br.attach()
        page._enable_domains()
        page.send("Network.enable")
        page.set_viewport(1280, 900)
        rec = Recorder(page)

        for name, path, tutor in PAGES:
            consumer = name == "consumer"
            sid = page.send("Page.addScriptToEvaluateOnNewDocument",
                            {"source": init_script(prod, tref, consumer, real)})["identifier"]
            url = "%s%s?env=test&api=%s" % (origin, path, api)
            page.goto(url, settle=3.0)          # > the tutor's 2s warm-up timer
            rec.urls = []
            seen = rec.collect()
            env = page.eval("(window.MrBadmusConfig||{}).environment||null")
            be = page.eval("(window.MrBadmusConfig||{}).BACKEND_URL||null")
            bad = [u for u in seen if is_prod(u, prod)]
            badh = [h for h in hints(page) if is_prod(h, prod)]
            here = page.eval("location.pathname+location.search")
            line = "%-13s env=%s backend=%s requests=%d prod=%d at=%s" % (name, env, be, len(seen), len(bad), here)
            print("  " + line)
            if env != "test":
                fails.append("%s: config resolved %r, not test" % (name, env))
            if bad:
                fails.append("%s: requests to production: %s" % (name, bad))
            if badh:
                fails.append("%s: connection hints to production: %s" % (name, badh))
            entry = {"url": url, "landed": here, "env": env, "backend": be, "requests": seen}
            if tutor:
                answers = {}
                modes = [("500", api)] if not a.backend else [("real", api)]
                if not a.backend:
                    modes.append(("429", api))
                for mode, _ in modes:
                    Stub.mode = mode
                    answers[mode] = ask_tutor(page, "What is photosynthesis? limiting factors")
                answers_all = dict(answers)
                for mode, txt in answers.items():
                    print("    tutor[%s] → %r" % (mode, txt))
                    if txt is None:
                        fails.append("%s tutor[%s]: no reply drawn" % (name, mode))
                    elif "6CO" in txt or "Limiting factors" in txt or "trouble thinking" in txt:
                        fails.append("%s tutor[%s]: canned fallback shown: %r" % (name, mode, txt))
                    elif mode == "500" and txt != UNAVAILABLE:
                        fails.append("%s tutor[500]: %r is not the honest line" % (name, txt))
                    elif mode == "429" and txt != LIMIT_MSG:
                        fails.append("%s tutor[429]: %r is not the backend's sentence" % (name, txt))
                entry["shots"] = shoot(page, a.shots, name + "-tutor")
                entry["tutor"] = answers_all
                more = [u for u in rec.collect() if is_prod(u, prod)]
                if more:
                    fails.append("%s: requests to production after asking: %s" % (name, more))
                entry["requests"] = list(rec.urls)
            else:
                entry["shots"] = shoot(page, a.shots, name)
            log[name] = entry
            page.send("Page.removeScriptToEvaluateOnNewDocument", {"identifier": sid})

        # (c) the backend not running at all.
        down = "http://127.0.0.1:%d" % closed_port()
        sid = page.send("Page.addScriptToEvaluateOnNewDocument",
                        {"source": init_script(prod, tref, False)})["identifier"]
        page.goto("%s%s?env=test&api=%s" % (origin, PAGES[0][1], down), settle=1.0)
        rec.urls = []
        txt = ask_tutor(page, "What is photosynthesis?")
        print("    tutor[backend down] → %r" % txt)
        if txt != UNAVAILABLE:
            fails.append("tutor with the backend down: %r is not the honest line" % txt)
        bad = [u for u in rec.collect() if is_prod(u, prod)]
        if bad:
            fails.append("backend-down page: requests to production: %s" % bad)
        log["backend-down"] = {"tutor": txt, "requests": list(rec.urls),
                               "shots": shoot(page, a.shots, "ks3-tutor-backend-down")}
        page.send("Page.removeScriptToEvaluateOnNewDocument", {"identifier": sid})

        # Production resolution, in an EMPTY document — no page, no pupil traffic.
        Stub.probe_html = ('<!doctype html><meta charset=utf-8><title>probe</title>'
                           '<script src="%s/shared/config.js"></script>' % origin)
        page.goto("%s/probe.html?env=prod" % stub, settle=0.3)
        got = page.eval("(function(c){return c&&{e:c.environment,b:c.BACKEND_URL,"
                        "s:c.SUPABASE_URL,k:c.AUTH_STORAGE_KEY,a:c.SUPABASE_ANON_KEY.split('.')[1]};})"
                        "(window.MrBadmusConfig)")
        want = {"e": "prod", "b": prod["BACKEND_URL"], "s": prod["SUPABASE_URL"],
                "k": prod["AUTH_STORAGE_KEY"]}
        ok = bool(got) and all(got.get(k) == v for k, v in want.items())
        print("  prod-config  env=%s backend-same=%s supabase-same=%s key-same=%s"
              % (got and got.get("e"), got and got.get("b") == want["b"],
                 got and got.get("s") == want["s"], got and got.get("k") == want["k"]))
        if not ok:
            fails.append("?env=prod did not resolve the production config: %r" % got)
        log["prod-config"] = {"same": ok}
    finally:
        try:
            br.close()
        finally:
            server.shutdown()
            stub_srv.shutdown()

    if a.log:
        with open(a.log, "w") as f:
            json.dump(log, f, indent=1)
    if fails:
        print("test_isolation_drive: FAIL — %d" % len(fails))
        for f in fails:
            print("  " + f)
        return 1
    print("test_isolation_drive: OK — 4 page families on ?env=test made no request to "
          "production; the tutor is honest when it cannot answer; ?env=prod resolves "
          "production unchanged")
    return 0


if __name__ == "__main__":
    sys.exit(main())
