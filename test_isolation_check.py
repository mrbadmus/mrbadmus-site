#!/usr/bin/env python3
"""test_isolation_check.py — a TEST run must never be able to call production.

⊕ Mide's ruling, 5 Oct 2026. FAST gate (no browser).

── WHY ────────────────────────────────────────────────────────────────────

On 4 Oct 2026 a blind driver opened a lesson page on `?env=test&api=…` and
watched the AI tutor send `/api/health` and `/api/chat` to the PRODUCTION
backend. `shared/config.js` already decided test-vs-prod correctly; the tutor
engine simply did not ask it. It named the live backend and the live Supabase
project outright, and so did a dozen `cfg.BACKEND_URL || '<production>'`
fallbacks, five hand-written pages and the preconnect hints in two
generators' heads. Every one of those is a way for a test run to write into
the live site.

The rule this gate holds: `shared/config.js` is the ONLY shipped file that
names the production backend host or the production Supabase project. Every
other page and script reads `window.MrBadmusConfig`, and fails CLOSED (makes
no call) when it is absent.

── WHAT IT CHECKS ─────────────────────────────────────────────────────────

1. NAMES. No shipped file — the published tree `mrbadmus_site/`, the source
   pages and scripts it is copied from, and the teacher fixture harness pages
   — contains the production backend host, any `onrender.com` host, the
   production project ref, or a JWT whose payload names the production ref
   (the anon key carries the ref base64-encoded, so a plain substring search
   would miss it). `shared/config.js` is the one exemption.

2. LOAD ORDER. A consumer that cannot find config fails closed, so on the
   live site a page that forgot to load config.js would lose its backend.
   Every published page that loads a script which reads
   `window.MrBadmusConfig` must therefore load `/shared/config.js` so that it
   EXECUTES FIRST: the browser runs parser-blocking scripts in document order
   and then deferred ones in document order, and config.js must come before
   every consumer in that sequence. `async` config is refused (no order).
   The student and teacher dashboards load config.js themselves, as the
   first dependency of `shared/student-live.js` / `shared/teacher-live.js`;
   that is checked directly (DEPS[0]), and on those pages the other readers
   must be lazy. The teacher FIXTURE pages carry no config on purpose (they
   are offline harness pages): they are held to rule 1 only, and with no
   config every reader on them now fails closed.

Exit 0 = clean. Exit 1 = a finding, each printed with file and line.
"""
import base64
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.join(ROOT, "mrbadmus_site")

PROD_REF = "urk" + "lkrwevjtlfbwnipjn"          # split so this file is not a hit
PROD_HOST = "mrbadmus-backend." + "onrender.com"
HOST_RE = re.compile(r"[a-z0-9.-]*onrender\.com", re.I)
JWT_RE = re.compile(r"eyJ[A-Za-z0-9_-]{8,}\.(eyJ[A-Za-z0-9_-]{8,})\.[A-Za-z0-9_-]+")

EXEMPT = {os.path.join("shared", "config.js"),
          os.path.join("mrbadmus_site", "shared", "config.js")}

TEXT_EXT = {".html", ".htm", ".js", ".mjs", ".json", ".css", ".xml", ".txt",
            ".webmanifest", ".svg", ".md"}

# Source trees that are COPIED into mrbadmus_site, plus the fixture harness.
SOURCE_DIRS = ["shared", "teacher", "student", "consumer", "parents", "go",
               "org", "teacher_fixtures"]


def rel(p):
    return os.path.relpath(p, ROOT)


def walk(base):
    for dp, dns, fns in os.walk(base):
        dns[:] = [d for d in dns if d not in ("node_modules", ".git")]
        for fn in fns:
            if os.path.splitext(fn)[1].lower() in TEXT_EXT:
                yield os.path.join(dp, fn)


def shipped_files():
    seen = set()
    roots = [SITE] + [os.path.join(ROOT, d) for d in SOURCE_DIRS]
    for r in roots:
        if os.path.isdir(r):
            for p in walk(r):
                seen.add(p)
    for fn in os.listdir(ROOT):
        if fn.endswith(".html"):
            seen.add(os.path.join(ROOT, fn))
    return sorted(seen)


def jwt_ref(payload_b64):
    try:
        pad = "=" * (-len(payload_b64) % 4)
        return json.loads(base64.urlsafe_b64decode(payload_b64 + pad)).get("ref")
    except Exception:
        return None


def check_names(findings):
    n = 0
    for p in shipped_files():
        r = rel(p)
        if r in EXEMPT:
            continue
        n += 1
        try:
            text = open(p, encoding="utf-8", errors="replace").read()
        except OSError:
            continue
        for i, line in enumerate(text.split("\n"), 1):
            hits = []
            if PROD_REF in line:
                hits.append("the production Supabase ref")
            for m in HOST_RE.finditer(line):
                hits.append("the backend host %s" % m.group(0))
            for m in JWT_RE.finditer(line):
                if jwt_ref(m.group(1)) == PROD_REF:
                    hits.append("a JWT for the production project (anon key)")
            for h in hits:
                findings.append("%s:%d names %s" % (r, i, h))
    return n


SCRIPT_RE = re.compile(r"<script\b([^>]*)>(.*?)</script>", re.S | re.I)
SRC_RE = re.compile(r"""\bsrc\s*=\s*["']([^"']+)["']""", re.I)


def consumers():
    """Shared scripts that read window.MrBadmusConfig (config.js aside)."""
    out = set()
    d = os.path.join(SITE, "shared")
    if not os.path.isdir(d):
        d = os.path.join(ROOT, "shared")
    for fn in os.listdir(d):
        if fn.endswith(".js") and fn != "config.js":
            try:
                if "MrBadmusConfig" in open(os.path.join(d, fn), encoding="utf-8").read():
                    out.add(fn)
            except OSError:
                pass
    return out


SELF_LOADING = ("student-live.js", "teacher-live.js")


def check_self_loading(findings):
    for fn in SELF_LOADING:
        p = os.path.join(ROOT, "shared", fn)
        if not os.path.exists(p):
            continue
        s = open(p, encoding="utf-8").read()
        m = re.search(r"var DEPS = \[\s*(?:/\*.*?\*/\s*)?\"([^\"]+)\"", s, re.S)
        if not m or m.group(1) != "/shared/config.js":
            findings.append("shared/%s: DEPS[0] is not /shared/config.js — the page "
                            "would read its backend before config." % fn)


_READS = {}


def reads_config(page, src, shared_cons):
    """Does the script at `src` (as written on `page`) read MrBadmusConfig?"""
    if src.startswith(("http:", "https:", "//")):
        return False
    if src.startswith("/shared/") and src.count("/") == 2:
        return os.path.basename(src) in shared_cons
    path = (os.path.join(SITE, src.lstrip("/")) if src.startswith("/")
            else os.path.join(os.path.dirname(page), src))
    path = os.path.normpath(path)
    if path not in _READS:
        try:
            _READS[path] = "MrBadmusConfig" in open(path, encoding="utf-8").read()
        except OSError:
            _READS[path] = False
    return _READS[path] and os.path.basename(path) != "config.js"


def check_order(findings):
    cons = consumers()
    selfl = set(SELF_LOADING)
    # Read config only inside functions called after the page is up — never
    # at evaluation. Checked by hand, 5 Oct 2026: topbar.js reads it in
    # sign-out; leaderboard-live.js wraps every read in a function for
    # exactly this reason (its own comment, "THE READ CANNOT HAPPEN AT PARSE
    # TIME").
    LAZY = {"topbar.js", "leaderboard-live.js", "set-work.js", "teacher-admin-nav.js"}
    pages = [p for p in walk(SITE) if p.endswith(".html")]
    checked = 0
    for p in sorted(pages):
        html = open(p, encoding="utf-8", errors="replace").read()
        seq = []    # (phase, index, name, is_config, line)
        for idx, m in enumerate(SCRIPT_RE.finditer(html)):
            attrs, body = m.group(1), m.group(2)
            line = html.count("\n", 0, m.start()) + 1
            src = SRC_RE.search(attrs)
            a = attrs.lower()
            if src:
                name = src.group(1).split("?")[0]
                base = os.path.basename(name)
                is_mod = 'type="module"' in a or "type='module'" in a
                phase = "async" if re.search(r"\basync\b", a) else (
                    1 if (re.search(r"\bdefer\b", a) or is_mod) else 0)
                if name.endswith("/shared/config.js"):
                    seq.append((phase, idx, "config.js", True, line))
                elif reads_config(p, name, cons):
                    seq.append((phase, idx, base, False, line))
            else:
                if 'type="application/json"' in a or 'type="application/ld+json"' in a:
                    continue
                if "MrBadmusConfig" in body:
                    seq.append((0, idx, "inline script", False, line))
        users = [s for s in seq if not s[3]]
        if not users:
            continue
        checked += 1
        r = rel(p)
        cfgs = [s for s in seq if s[3]]
        names = {u[2] for u in users}
        if not cfgs:
            if names <= LAZY:
                continue
            if names & selfl and names <= (selfl | LAZY | {"inline script"}):
                continue
            findings.append("%s: loads %s but never loads /shared/config.js"
                            % (r, ", ".join(sorted(names))))
            continue
        c = cfgs[0]
        if c[0] == "async":
            findings.append("%s:%d config.js is async — no execution order" % (r, c[4]))
            continue
        for u in users:
            if u[0] == "async" or u[2] in LAZY or u[2] in selfl:
                continue
            if (u[0], u[1]) < (c[0], c[1]):
                findings.append("%s:%d %s executes before config.js (line %d)"
                                % (r, u[4], u[2], c[4]))
    return checked


def main():
    findings = []
    if not os.path.isdir(SITE):
        print("test_isolation_check: no mrbadmus_site/ — run python3 build_all.py")
        return 1
    n = check_names(findings)
    k = check_order(findings)
    check_self_loading(findings)
    if findings:
        print("test_isolation_check: FAIL — %d finding(s)" % len(findings))
        for f in findings:
            print("  " + f)
        print("\nOnly shared/config.js may name production. Read window.MrBadmusConfig "
              "and fail closed without it; load config.js before every consumer.")
        return 1
    print("test_isolation_check: OK — %d shipped files name no production host or "
          "project; %d pages load config.js before every consumer" % (n, k))
    return 0


if __name__ == "__main__":
    sys.exit(main())
