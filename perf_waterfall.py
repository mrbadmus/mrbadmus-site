#!/usr/bin/env python3
"""
perf_waterfall.py — MRB-348. What the page actually waits for, in order.

    MRB_TEST_TEACHER_PASSWORD=… python3 perf_waterfall.py --journey student-class
    MRB_TEST_TEACHER_PASSWORD=… python3 perf_waterfall.py --all --runs 5
    MRB_TEST_TEACHER_PASSWORD=… python3 perf_waterfall.py --all --json out.json

WHY THIS EXISTS, AND WHY IT IS NOT teacher_perf_budget.py

`teacher_perf_budget.py` answers "is the page under 2500 ms". That is the right
question for a gate and the wrong one for a diagnosis: when it goes red it says
a number and nothing about which of a page's twenty requests moved it. MRB-347
was argued from a hand-built waterfall that was never committed, so the numbers
in its report cannot be reproduced or compared against. This file is that
waterfall, kept.

WHAT IT MEASURES

Chrome's Network domain over CDP, not `performance.getEntriesByType('resource')`.
Resource timing gives a duration per URL; it does not reliably give you when the
request LEFT relative to the others, and "when it left" is the entire question
here. A page making 13 requests in one wave and a page making 13 one after the
other have the same total duration and completely different feel.

So each request is recorded with `requestWillBeSent` / `responseReceived` /
`loadingFinished` timestamps, and from those three facts the script derives:

  · WAVES — requests grouped by when they started. Two requests are in the same
    wave if the second left before the first came back. A wave is what the page
    does in parallel; the number of waves is how many times the page stopped and
    waited, and it is the number that a restructure has to move.

  · CRITICAL PATH — the longest chain of "B could not start until A finished".
    This is the floor on the page: no amount of parallelism inside a wave beats
    it. ⚠️ It is inferred from timing, not from causality Chrome tells us, so it
    is a lower bound on the true dependency depth, not proof of one. A request
    that merely happened to start late looks the same as one that had to.

  · MOUNT — the moment the page's own content replaces the skeleton, read from
    the page rather than from `load`. `load` on these pages fires long before
    the student can read anything, and long after would also be wrong.

⚠️ THIS IS A DIAGNOSTIC, NOT A GATE. It does not fail. It prints what happened
and exits 0 whether that is good or bad, because a threshold here would invite
the one thing MRB-346 was about: a number nudged to make a build pass. The gate
is `teacher_perf_budget.py` and it stays the gate.

⚠️ AND IT IS A LOCAL MEASUREMENT, with all of `shared/rum.js`'s objections to
local measurements still standing: a developer laptop, home broadband, a warm
cache, against the TEST project's small seed. It is good for SHAPE — how many
waves, what is on the critical path, did an arm move off it — and it is not a
model of a Year 8 on a school Chromebook. For that, read `rum_timings`.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import ssl
import statistics
import sys
import time
import urllib.request

REPO = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, REPO)
os.chdir(REPO)

import ks3_browser as cdp  # noqa: E402

TEST_REF = "qeppkiswvclkkwbxmlok"
PROD_REF = "urklkrwevjtlfbwnipjn"
URL = "https://%s.supabase.co" % TEST_REF
CTX = ssl.create_default_context(cafile="/etc/ssl/cert.pem")
PORT = int(os.environ.get("MRB348_PORT") or 5531)
# ⊕ MRB-348 round three — the tree to serve. `mrbadmus_site` always, unless a
# caller names another with $MRB348_SERVE_DIR.
#
# ⚠️ CHANGE $MRB348_PORT WITH IT, ALWAYS. Two trees built from the same repo
# serve the SAME asset urls, cache-bust stamp and all — `/shared/
# teacher-live.js?v=94834e17` names the path, and the stamp is a hash of the
# file the CURRENT build produced. Serve both on 127.0.0.1:5531 and Chrome
# answers the second run out of the first run's cache: the measurement is of
# the wrong code and it looks completely normal. It fired on the first attempt
# here, and the tell was `rpc:teacher_class_rollup` appearing in the critical
# path of a run that was supposed to predate it. A different port is a
# different origin and therefore a different cache.
#
# ⚠️ IT EXISTS SO A **BEFORE** CAN BE MEASURED WITHOUT DISTURBING THE REPO.
# Round two left no committed BEFORE for the teacher journeys, and the way to
# get one is to build the old files and drive them — which, done in place,
# means a stash, a full rebuild, a measurement, a restore and another rebuild,
# on a tree whose gate receipts bind to its content. Pointing this at a
# hardlinked copy of `mrbadmus_site` carrying the previous commit's
# `shared/*.js` costs nothing and cannot leave the repo half-reverted if the
# run dies in the middle.
SERVE_DIR = os.environ.get("MRB348_SERVE_DIR") or "mrbadmus_site"

# The realistic TEST world, not the hz_* smoke fixtures. See the note in
# `_mrb348_fixture_pw.py`: hz_s1's class holds no assignments and no
# submissions, so a waterfall driven from it measures a page with nothing to
# fetch — fast for the one reason that cannot be shipped.
JOURNEYS = {
    "student-class": dict(
        who="aiden.cole@test-rainford.local",
        path="/student/class.html?class=2a000000-0000-0000-0000-000000000001",
        note="KS3 8X1 — 4 assignments, 15 submissions; exercises deck + ladder",
        ready="student",
    ),
    "student-class-ks4": dict(
        who="hannah.patel@test-rainford.local",
        path="/student/class.html?class=2a000000-0000-0000-0000-000000000002",
        note="KS4 10A — 17 assignments, the longest work list on TEST",
        ready="student",
    ),
    "teacher-classes": dict(
        who="mide.badmus@test-rainford.local",
        path="/teacher/classes.html",
        note="5 classes / 26 assignments / 79 submissions — the WS-2 shape",
        ready="teacher",
    ),
    "teacher-class-detail": dict(
        who="mide.badmus@test-rainford.local",
        path="/teacher/class-detail.html?class=2a000000-0000-0000-0000-000000000002",
        note="10A, the class with the most assignments",
        ready="teacher",
    ),
    "teacher-insights": dict(
        who="mide.badmus@test-rainford.local",
        path="/teacher/insights.html",
        note="reads every live class's marked papers",
        ready="teacher",
    ),
    "teacher-digest": dict(
        who="mide.badmus@test-rainford.local",
        path="/teacher/digest.html",
        note="per-class summaries across all 5 classes",
        ready="teacher",
    ),
}

# The page has mounted when its own region is drawn and the skeleton is gone.
# Deliberately the same shape of question `teacher_perf_budget.py` asks, so the
# two instruments agree about what "the page is up" means.
READY = {
    "student": """(function(){
        var host = document.querySelector('[data-port-region], #mrb-student, main');
        if (!host) { return false; }
        if (document.querySelector('.skeleton, [data-skeleton]')) { return false; }
        return (host.textContent || '').trim().length > 80;
    })()""",
    "teacher": """(function(){
        var host = document.querySelector('[data-port-region], #mrb-teacher, main');
        if (!host) { return false; }
        if (document.querySelector('.skeleton, [data-skeleton]')) { return false; }
        return (host.textContent || '').trim().length > 80;
    })()""",
}


# ── credentials ──────────────────────────────────────────────────────────────

def anon_key() -> str:
    """The TEST anon key.

    ⚠️ SLICED FROM `const TEST`, NEVER THE FIRST KEY IN THE FILE. config.js
    carries both projects and production's key comes first, so a first-match
    read signs a TEST fixture's email into PRODUCTION and returns a 401 that
    reads exactly like a wrong password. Cost an hour once; costs nothing to
    prevent. The ref is then checked out of the key's own payload.
    """
    src = open("shared/config.js", encoding="utf-8").read()
    key = re.search(r"'(eyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+)'",
                    src[src.index("const TEST"):]).group(1)
    import base64
    pl = key.split(".")[1]
    pl += "=" * (-len(pl) % 4)
    ref = json.loads(base64.urlsafe_b64decode(pl)).get("ref")
    if ref == PROD_REF:
        raise SystemExit("perf_waterfall: refusing — that key is PRODUCTION's.")
    if ref != TEST_REF:
        raise SystemExit("perf_waterfall: anon key ref %r is not TEST's." % ref)
    return key


def password() -> str:
    pw = os.environ.get("MRB_TEST_TEACHER_PASSWORD")
    if not pw:
        raise SystemExit(
            "perf_waterfall: $MRB_TEST_TEACHER_PASSWORD is not set, so there "
            "is no session to measure. It is the TEST fixture password.")
    return pw


def sign_in(email: str, key: str, pw: str) -> dict:
    req = urllib.request.Request(
        URL + "/auth/v1/token?grant_type=password",
        data=json.dumps({"email": email, "password": pw}).encode(),
        headers={"apikey": key, "Content-Type": "application/json"},
        method="POST")
    return json.load(urllib.request.urlopen(req, timeout=30, context=CTX))


def put_session(page, base: str, key: str, sess: dict) -> None:
    """Plant the session the way the SDK stores it, then prove it took."""
    payload = json.dumps({
        "access_token": sess["access_token"],
        "refresh_token": sess.get("refresh_token", ""),
        "expires_at": int(time.time()) + int(sess.get("expires_in", 3600)),
        "expires_in": int(sess.get("expires_in", 3600)),
        "token_type": "bearer",
        "user": sess["user"],
    })
    page.goto(base + "/student/class.html", settle=0.2)
    ok = page.eval(
        "(function(){ try { localStorage.setItem(%s, %s); return true; }"
        " catch(e) { return String(e); } })()"
        % (json.dumps("sb-%s-auth-token" % TEST_REF), json.dumps(payload)))
    if ok is not True:
        raise SystemExit("perf_waterfall: could not plant the session: %r" % ok)


# ── the measurement ──────────────────────────────────────────────────────────

def collect(page, base: str, path: str, ready_expr: str, timeout: float = 40.0):
    """Navigate and return every network request with its timings, plus mount."""
    page._events.clear()
    page.send("Network.enable", {})
    page.send("Network.clearBrowserCache", {})

    t0 = time.time()
    page.send("Page.navigate", {"url": base + path})

    mount_ms = None
    deadline = t0 + timeout
    while time.time() < deadline:
        page.drain(timeout=0.05)
        try:
            if page.eval(ready_expr, timeout=5) is True:
                mount_ms = (time.time() - t0) * 1000.0
                break
        except Exception:
            pass
        time.sleep(0.05)

    # Let the tail of the wave land so late arms are visible in the picture.
    end = time.time() + 2.5
    while time.time() < end:
        page.drain(timeout=0.05)
        time.sleep(0.02)

    sent, recv, done, failed = {}, {}, {}, {}
    for ev in page._events:
        m, p = ev.get("method"), ev.get("params") or {}
        rid = p.get("requestId")
        if m == "Network.requestWillBeSent" and rid:
            sent[rid] = dict(url=p.get("request", {}).get("url", ""),
                             ts=p.get("timestamp"), typ=p.get("type"),
                             method=(p.get("request", {}).get("method") or ""))
        elif m == "Network.responseReceived" and rid:
            recv[rid] = dict(ts=p.get("timestamp"),
                             status=p.get("response", {}).get("status"))
        elif m == "Network.loadingFinished" and rid:
            done[rid] = p.get("timestamp")
        elif m == "Network.loadingFailed" and rid:
            failed[rid] = p.get("errorText")

    reqs = []
    for rid, s in sent.items():
        fin = done.get(rid) or (recv.get(rid) or {}).get("ts")
        if s["ts"] is None or fin is None:
            continue
        reqs.append(dict(
            url=s["url"], typ=s["typ"], method=s["method"],
            start=s["ts"], end=fin,
            status=(recv.get(rid) or {}).get("status"),
            error=failed.get(rid),
        ))
    if not reqs:
        return [], mount_ms
    base_ts = min(r["start"] for r in reqs)
    for r in reqs:
        r["t0"] = (r["start"] - base_ts) * 1000.0
        r["t1"] = (r["end"] - base_ts) * 1000.0
        r["ms"] = r["t1"] - r["t0"]
    reqs.sort(key=lambda r: r["t0"])
    return reqs, mount_ms


def label(url: str, method: str = "") -> str:
    """A short name. Table for REST, route for the API, filename otherwise.

    ⚠️ A CORS PREFLIGHT IS MARKED, NOT HIDDEN. Chrome issues an `OPTIONS` for
    every cross-origin request carrying `apikey`/`Authorization` headers, and
    it is a FULL round trip of its own. Folding it into the request it precedes
    would halve the apparent request count and hide the fact that the page pays
    two trips for every read.
    """
    pre = "OPTIONS " if (method or "").upper() == "OPTIONS" else ""
    u = url.split("?")[0]
    if "/rest/v1/rpc/" in u:
        return pre + "rpc:" + u.split("/rest/v1/rpc/")[1]
    if "/rest/v1/" in u:
        return pre + u.split("/rest/v1/")[1].split("/")[0]
    if "/auth/v1/" in u:
        return pre + "auth:" + u.split("/auth/v1/")[1].split("/")[0]
    if "/api/" in u:
        return pre + "api:" + u.split("/api/")[1].split("?")[0]
    return pre + (u.rsplit("/", 1)[-1][:34] or u[:34])


def is_data(r: dict) -> bool:
    """A round trip the page waits for, as against an asset it renders with."""
    u = r["url"]
    return ("/rest/v1/" in u) or ("/api/" in u) or ("/auth/v1/" in u)


def waves(reqs: list) -> list:
    """Group into waves: a new wave starts when nothing earlier is still open.

    This is the honest version of "serial round trips". Requests that overlap
    are one wave however many there are; a request that leaves only after every
    earlier one has come back opens a new one. The wave COUNT is how many times
    the page stopped and waited.
    """
    out, cur, open_until = [], [], None
    for r in sorted(reqs, key=lambda x: x["t0"]):
        if cur and open_until is not None and r["t0"] >= open_until - 1e-9:
            out.append(cur)
            cur, open_until = [r], r["t1"]
        else:
            cur.append(r)
            open_until = max(open_until or 0.0, r["t1"])
    if cur:
        out.append(cur)
    return out


def critical_path(reqs: list) -> list:
    """Longest chain where each link started only after the previous finished.

    ⚠️ INFERRED FROM TIMING, NOT FROM CAUSALITY. Chrome does not tell us that B
    needed A; this says only that B could not have overlapped A. So it is a
    lower bound on dependency depth and an upper bound on what parallelising
    could remove — useful, and not proof.
    """
    rs = sorted(reqs, key=lambda x: x["t0"])
    best, prev = [0.0] * len(rs), [-1] * len(rs)
    for i, r in enumerate(rs):
        best[i] = r["ms"]
        for j in range(i):
            if rs[j]["t1"] <= r["t0"] + 1e-9 and best[j] + r["ms"] > best[i]:
                best[i], prev[i] = best[j] + r["ms"], j
    if not best:
        return []
    i = max(range(len(rs)), key=lambda k: best[k])
    chain = []
    while i >= 0:
        chain.append(rs[i])
        i = prev[i]
    return list(reversed(chain))


SHOW_URLS = False
SHOW_ASSETS = False


def filt(url: str) -> str:
    """The query, trimmed. TEST data only — every row here is fake."""
    q = url.split("?", 1)[1] if "?" in url else ""
    q = re.sub(r"select=[^&]*", "select=…", q)
    return q[:110]


def draw(reqs: list, mount_ms, name: str, note: str, width: int = 58) -> None:
    data = [r for r in reqs if is_data(r)]
    drawn = reqs if SHOW_ASSETS else data
    span = max([r["t1"] for r in reqs] or [1.0])
    scale = width / span

    print("\n" + "=" * 92)
    print("  %s   %s" % (name, note))
    print("=" * 92)
    pre = [r for r in data if (r.get("method") or "").upper() == "OPTIONS"]
    real = [r for r in data if (r.get("method") or "").upper() != "OPTIONS"]
    print("  requests: %d total, %d data = %d real + %d CORS preflight"
          "   span %.0f ms" % (len(reqs), len(data), len(real), len(pre), span))
    if pre:
        print("  ⚠️ %d preflights costing %.0f ms of round trips"
              % (len(pre), sum(r["ms"] for r in pre)))
    if mount_ms is not None:
        print("  MOUNT (skeleton replaced): %.0f ms" % mount_ms)
    else:
        print("  MOUNT: never reached within the timeout")
    print("-" * 92)

    for r in sorted(drawn, key=lambda x: x["t0"]):
        a = int(r["t0"] * scale)
        b = max(1, int(r["ms"] * scale))
        bar = " " * a + "█" * b
        flag = ""
        if r.get("error"):
            flag = " ✗ " + str(r["error"])[:18]
        elif r.get("status") and int(r["status"]) >= 400:
            flag = " ✗ HTTP %s" % r["status"]
        late = ""
        if mount_ms is not None and r["t0"] > mount_ms:
            late = " ·after mount"
        print("  %-30s %-*s %6.0f ms%s%s"
              % (label(r["url"], r.get("method", ""))[:30], width, bar[:width], r["ms"], late, flag))
        if SHOW_URLS and (r.get("method") or "").upper() != "OPTIONS":
            f = filt(r["url"])
            if f:
                print("  %-30s   ↳ %s" % ("", f))

    ws = waves(data)
    cp = critical_path(data)
    print("-" * 92)
    print("  WAVES: %d  (a wave = requests that overlap; the count is how many"
          " times the page waited)" % len(ws))
    for i, w in enumerate(ws, 1):
        names = ", ".join(sorted({label(x["url"], x.get("method", "")) for x in w}))
        print("    %d. %5.0f–%-5.0f ms  ×%-2d  %s"
              % (i, min(x["t0"] for x in w), max(x["t1"] for x in w), len(w),
                 names[:64]))
    print("  CRITICAL PATH: %d hops, %.0f ms  (lower bound on dependency depth)"
          % (len(cp), sum(x["ms"] for x in cp)))
    print("    " + " → ".join(label(x["url"], x.get("method", "")) for x in cp))

    if mount_ms is not None:
        blocking = [r for r in data if r["t1"] <= mount_ms + 1e-9]
        after = [r for r in data if r["t0"] > mount_ms]
        print("  BEFORE MOUNT: %d requests   AFTER MOUNT: %d requests"
              % (len(blocking), len(after)))
        slow = sorted(blocking, key=lambda x: -x["ms"])[:5]
        if slow:
            print("  SLOWEST BLOCKING:")
            for r in slow:
                print("    %7.0f ms  %s" % (r["ms"], label(r["url"], r.get("method", ""))))


def run_journey(page, base, jname, j, runs, warm):
    key = READY[j["ready"]]
    results = []
    for i in range(runs + warm):
        reqs, mount = collect(page, base, j["path"], key)
        if i >= warm:
            results.append((reqs, mount))
    mounts = [m for _, m in results if m is not None]
    med = statistics.median(mounts) if mounts else None
    # Report the run whose mount is closest to the median, so the drawn
    # waterfall is a real single load rather than an average of shapes that
    # never happened.
    if med is not None:
        pick = min(results, key=lambda r: abs((r[1] or 1e9) - med))
    else:
        pick = results[0]
    draw(pick[0], pick[1], jname, j["note"])
    data = [r for r in pick[0] if is_data(r)]
    return dict(
        journey=jname, who=j["who"], path=j["path"],
        mount_ms_median=med, mount_ms_runs=mounts,
        requests_total=len(pick[0]), requests_data=len(data),
        requests_real=len([r for r in data
                           if (r.get("method") or "").upper() != "OPTIONS"]),
        requests_preflight=len([r for r in data
                                if (r.get("method") or "").upper() == "OPTIONS"]),
        waves=len(waves(data)),
        critical_path_hops=len(critical_path(data)),
        critical_path_ms=sum(x["ms"] for x in critical_path(data)),
        before_mount=len([r for r in data
                          if med is not None and r["t1"] <= med + 1e-9]),
        tables=sorted({label(r["url"], r.get("method", "")) for r in data}),
    )


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--journey", action="append",
                    help="one of: " + ", ".join(JOURNEYS))
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--runs", type=int, default=3)
    ap.add_argument("--warm", type=int, default=1,
                    help="discarded warm-up loads before the timed ones")
    ap.add_argument("--json", help="write the summary here")
    ap.add_argument("--assets", action="store_true",
                    help="draw script/style/document loads too. The data reads "
                         "cannot leave until the JS that issues them has "
                         "parsed, so a serial module graph is a serial page "
                         "however parallel its queries are.")
    ap.add_argument("--urls", action="store_true",
                    help="print each request's filter too, so two reads of the "
                         "same table are distinguishable from one read twice")
    a = ap.parse_args()

    global SHOW_URLS, SHOW_ASSETS
    SHOW_URLS = bool(a.urls)
    SHOW_ASSETS = bool(a.assets)
    names = list(JOURNEYS) if a.all else (a.journey or ["student-class"])
    for n in names:
        if n not in JOURNEYS:
            raise SystemExit("unknown journey %r" % n)

    key, pw = anon_key(), password()
    server, port = cdp.serve(SERVE_DIR, PORT)
    base = "http://127.0.0.1:%d" % port
    print("perf_waterfall — TEST (%s), serving mrbadmus_site on %s"
          % (TEST_REF, base))
    print("runs=%d (after %d warm-up), cache cleared before each load"
          % (a.runs, a.warm))

    out, who = [], None
    try:
        with cdp.Browser() as b:
            page = b.attach()
            for n in names:
                j = JOURNEYS[n]
                if j["who"] != who:
                    put_session(page, base, key, sign_in(j["who"], key, pw))
                    who = j["who"]
                out.append(run_journey(page, base, n, j, a.runs, a.warm))
    finally:
        try:
            server.shutdown()
        except Exception:
            pass

    print("\n" + "=" * 92)
    print("  SUMMARY")
    print("=" * 92)
    print("  %-22s %9s %6s %6s %6s %6s %9s"
          % ("journey", "mount ms", "real", "pre", "waves", "hops", "pre-mount"))
    for r in out:
        print("  %-22s %9s %6d %6d %6d %6d %9d"
              % (r["journey"],
                 ("%.0f" % r["mount_ms_median"]) if r["mount_ms_median"] else "—",
                 r["requests_real"], r["requests_preflight"], r["waves"],
                 r["critical_path_hops"], r["before_mount"]))

    if a.json:
        with open(a.json, "w") as fh:
            json.dump(out, fh, indent=2)
        print("\n  wrote %s" % a.json)
    return 0


if __name__ == "__main__":
    sys.exit(main())
