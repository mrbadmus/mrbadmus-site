#!/usr/bin/env python3
"""tools/y_runthrough_live.py — Prompt Y, Unit 2: a FINDINGS rig for the
flashcard "one word, Secured" rule (Mide, 2 Oct 2026) and the surrounding
pupil/teacher flows, run live against TEST with production-shaped decks.

Built the same way as tools/mrb354_secured_live.py: a throwaway TEST world
(one teacher, 25 pupils, one class, ten decks), the REAL class page and
teacher pages served locally, a local backend worktree for boot reads, and
the COMMITTED `flashcard-answer-check` edge function run for real under Deno
with only the model call swapped for the deterministic stand-in
(tools/mrb353_stub_model.ts, unedited: "half"->partial, "wrong"->no, else
match). The browser's fetch() to the edge function is routed to the local
Deno server with CDP's `Fetch` domain. This file ADDS, on top of mrb354's
pattern, per-answer-marker control of that routing: an answer containing
ZZZSLOW6ZZZ sleeps 6s before forwarding (the client's own timeout is 4s);
ZZZFAIL500ZZZ returns a synthetic 500 without ever reaching Deno.

This is a FINDINGS rig, not a product-fix tool: it builds, runs, and reports
faults with evidence. It does not edit product code.

    python3 tools/y_runthrough_live.py --shots ~/tmp/y-shots/unit2

TEST ONLY — the service key's own `ref` claim is checked before any write.
"""
from __future__ import annotations

import argparse
import base64
import json
import os
import random
import signal
import socket
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import uuid
from datetime import datetime, timedelta, timezone

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO)
sys.path.insert(0, os.path.join(REPO, "tools"))
os.chdir(REPO)
import mrb351_acceptance as acc  # noqa: E402
import ks3_browser as cdp  # noqa: E402
import mrb351_pupil_flow_live as pf  # noqa: E402  (session_js)
import flashcard_homework_drive as drv  # noqa: E402  (Phone, check, FAILS, settle, FAKE_VV)
import mrb354_secured_live as m354  # noqa: E402  (generic helpers, reused read-only)

check = drv.check
FAILS = drv.FAILS
settle = drv.settle

BACKEND_DIR = "/Users/midebadmus/Documents/GitHub/mrbadmus-backend-worktrees/y-flashcards"
DENO = "/opt/homebrew/bin/deno"
DENO_PORT = 8000  # Deno.serve() in index.ts takes no options — not ours to change

DEFAULT_SHOTS = os.path.expanduser(os.environ.get("MRB_SHOTS", "~/tmp/y-shots/unit2"))

MARK_SLOW = "ZZZSLOW6ZZZ"
MARK_FAIL = "ZZZFAIL500ZZZ"
# ⊕ Y2 — ONE slow reply: the first request carrying it takes 6 s (the page
# gives up on it at 4 s; the server still finishes and stores the verdict),
# any repeat is answered at normal speed — a single slow reply, not an outage.
MARK_SLOW_ONCE = "ZZZSLOWONCEZZZ"
_SLOW_ONCE_SEEN = set()

REPORT = []  # list of dicts: {path, action, result, verdict, evidence}


def record(path, action, result, verdict, evidence=""):
    REPORT.append({"path": path, "action": action, "result": result, "verdict": verdict, "evidence": evidence})
    print(f"  [{verdict}] {path}: {result}" + (f" — {evidence}" if evidence else ""))


def free_port() -> int:
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    p = s.getsockname()[1]
    s.close()
    return p


# ════════════════════════════════════════════════════════════════════════
# the Deno stand-in, with per-answer slow/fail routing done in the CDP
# Fetch handler (not the stub) — a marker in `pupil_answer` decides.
# ════════════════════════════════════════════════════════════════════════

def write_import_map(path: str) -> None:
    model_abs = os.path.join(REPO, "supabase/functions/_shared/flashcards/model.ts")
    stub_abs = os.path.join(REPO, "tools/mrb353_stub_model.ts")
    json.dump({"imports": {f"file://{model_abs}": f"file://{stub_abs}"}}, open(path, "w"), indent=1)


def start_deno(url, service, log_dir, stub_log):
    import_map = os.path.join(cdp.gate_tmp(), "y_runthrough_import_map.json")  # per run, never in the tree
    write_import_map(import_map)
    if os.path.exists(stub_log):
        os.remove(stub_log)
    env = dict(os.environ, SUPABASE_URL=url, SUPABASE_SERVICE_ROLE_KEY=service,
               ANTHROPIC_API_KEY="stub-not-a-key", MRB353_STUB_LOG=stub_log)
    logf = open(os.path.join(log_dir, "deno.log"), "w")
    p = subprocess.Popen([DENO, "run", "-A", f"--import-map={import_map}",
                          "supabase/functions/flashcard-answer-check/index.ts"],
                         cwd=REPO, env=env, stdout=logf, stderr=subprocess.STDOUT,
                         start_new_session=True)
    deadline = time.time() + 20
    while time.time() < deadline:
        if p.poll() is not None:
            logf.flush()
            raise SystemExit("deno exited on boot:\n" + open(os.path.join(log_dir, "deno.log")).read()[-2000:])
        try:
            with urllib.request.urlopen(f"http://127.0.0.1:{DENO_PORT}/", timeout=1) as r:
                break
        except urllib.error.HTTPError:
            break
        except Exception:
            time.sleep(0.3)
    else:
        raise SystemExit("deno never answered on port %d" % DENO_PORT)
    return p


def stop_deno(p):
    if p is None:
        return
    try:
        os.killpg(p.pid, signal.SIGTERM)
        p.wait(timeout=5)
    except Exception:
        try:
            os.killpg(p.pid, signal.SIGKILL)
        except Exception:
            pass


FETCH_PATTERN = "*functions/v1/flashcard-answer-check*"


def enable_fetch(page):
    page.send("Fetch.enable", {"patterns": [{"urlPattern": FETCH_PATTERN}]})


def _forward_real(method, path, headers, body):
    target = f"http://127.0.0.1:{DENO_PORT}{path}"
    req = urllib.request.Request(target, data=body or None, method=method)
    for k, v in headers.items():
        if k.lower() in ("host", "content-length", "connection"):
            continue
        try:
            req.add_header(k, v)
        except Exception:
            pass
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return r.status, dict(r.headers), r.read()
    except urllib.error.HTTPError as e:
        return e.code, dict(e.headers or {}), e.read()


def forward_marked(method, path, headers, body):
    """Marker-aware routing: a SLOW marker sleeps before forwarding for real
    (proving the client's own 4s timeout actually fires before our 6s
    reply); a FAIL marker never reaches Deno at all — a synthetic 500,
    exactly what a real outage/5xx looks like to the browser."""
    try:
        payload = json.loads(body.decode("utf-8")) if body else {}
    except Exception:
        payload = {}
    ans = str(payload.get("pupil_answer") or "")
    if MARK_FAIL in ans:
        return 500, {"Content-Type": "application/json"}, b'{"error":"synthetic_failure"}'
    if MARK_SLOW in ans:
        time.sleep(6.0)
    if MARK_SLOW_ONCE in ans and ans not in _SLOW_ONCE_SEEN:
        _SLOW_ONCE_SEEN.add(ans)
        time.sleep(6.0)
    return _forward_real(method, path, headers, body)


def pump_fetch_once(page, seen: set) -> int:
    page.drain(0.05)
    n = 0
    for ev in list(page._events):
        if ev.get("method") != "Fetch.requestPaused":
            continue
        p = ev["params"]
        rid = p.get("requestId")
        if rid in seen:
            continue
        seen.add(rid)
        req = p.get("request", {})
        method = req.get("method", "GET")
        headers = req.get("headers", {}) or {}
        if req.get("hasPostData") and "postData" not in req:
            r = page.send("Fetch.getRequestPostData", {"requestId": rid})
            body = (base64.b64decode(r["postData"]) if r.get("base64Encoded")
                    else (r.get("postData") or "").encode())
        elif "postData" in req:
            body = req["postData"].encode("utf-8")
        else:
            body = b""
        path = urllib.parse.urlsplit(req["url"]).path
        status, resp_headers, resp_body = forward_marked(method, path, headers, body)
        hdrs = [{"name": k, "value": v} for k, v in resp_headers.items()
                if k.lower() not in ("content-length", "transfer-encoding", "connection")]
        try:
            page.send("Fetch.fulfillRequest", {"requestId": rid, "responseCode": status,
                                               "responseHeaders": hdrs,
                                               "body": base64.b64encode(resp_body).decode()})
        except cdp.CDPError:
            pass
        n += 1
    return n


def wait_chip(P, page, seen, timeout=12.0):
    t0 = time.time()
    s = P.st()
    while time.time() - t0 < timeout:
        pump_fetch_once(page, seen)
        s = P.st()
        if s["chip"] != "Checking…":
            return s
        time.sleep(0.12)
    return s


# ════════════════════════════════════════════════════════════════════════
# local backend + static site server
# ════════════════════════════════════════════════════════════════════════

def start_backend(bport, origin, log_dir):
    env = acc.read_env(acc.BACKEND_ENV_DEFAULT)
    base_env = dict(os.environ)
    for k, v in env.items():
        base_env[k] = v
    base_env["PORT"] = str(bport)
    base_env["EXTRA_CORS_ORIGINS"] = origin
    logf = open(os.path.join(log_dir, "backend.log"), "w")
    p = subprocess.Popen(["node", "server.js"], cwd=BACKEND_DIR, env=base_env,
                         stdout=logf, stderr=subprocess.STDOUT, start_new_session=True)
    api = f"http://localhost:{bport}"
    deadline = time.time() + 30
    while time.time() < deadline:
        if p.poll() is not None:
            raise SystemExit("backend never came up:\n" + open(os.path.join(log_dir, "backend.log")).read()[-2000:])
        try:
            with urllib.request.urlopen(api + "/api/health", timeout=2) as r:
                if r.status == 200:
                    time.sleep(2.0)
                    return p
        except Exception:
            time.sleep(0.4)
    try:
        os.killpg(p.pid, signal.SIGTERM)
    except Exception:
        pass
    raise SystemExit("backend never came up (timeout)")


def stop_backend(p):
    if p is None:
        return
    try:
        os.killpg(p.pid, signal.SIGTERM)
        p.wait(timeout=5)
    except Exception:
        try:
            os.killpg(p.pid, signal.SIGKILL)
        except Exception:
            pass


# ════════════════════════════════════════════════════════════════════════
# generic browser-side helpers (thin wrappers / reuse of mrb354's generic
# ones, which take no mrb354-specific state)
# ════════════════════════════════════════════════════════════════════════

fetch_reviews = m354.fetch_reviews
secured_from_rows = m354.secured_from_rows
teacher_card_state = m354.teacher_card_state
open_panel = m354.open_panel
no_got_it = m354.no_got_it
ALL_STATE_WORDS = m354.ALL_STATE_WORDS
goto_class = m354.goto_class
shot = m354.shot
wait_front = m354.wait_front
wait_end = m354.wait_end


def no_fav(errs):
    return [e for e in errs if "favicon.ico" not in e]


def hint(s):
    """⊕ 5 Oct 2026 — THE PUPIL DECIDES. Nothing is pre-filled any more and all
    three ratings are always enabled; the verdict chip is only a hint. This is
    the rating a pupil who simply follows that hint would tap (None = no chip).
    It reads the verdict chip proper, never the strip's numbered chips."""
    return {"Right": "got_it", "Nearly": "nearly", "Wrong": "not_yet", "No answer": "not_yet"}.get(
        s.get("verdictChip") or s.get("chip"))


def ready_click(P, sel, wait=5.0):
    """Click `sel` once it is drawn and enabled — the way a pupil's tap always
    lands after the redraw that offers it, never inside the same frame."""
    t = time.time()
    js = "(function(){var b=document.querySelector(%s);return !!b&&!b.disabled;})()" % json.dumps(sel)
    while time.time() - t < wait and not P.q(js):
        time.sleep(0.1)
    P.click(sel)


def open_deck(P, page, origin, api, aid, wait=40, tries=3):
    for attempt in range(tries):
        P.page.goto("about:blank")
        goto_class(page, f"{origin}/student/class.html?api={api}#cards={aid}")
        t = time.time()
        while time.time() - t < wait:
            s = P.st()
            if s["strip"] and (s["writing"] or s["rating"] or s["panel"]):
                return s
            body = P.q("document.body.innerText") or ""
            if "could not load your class" in body.lower():
                break
            time.sleep(0.5)
        if attempt < tries - 1:
            time.sleep(2.0)
    return P.st()


def new_tab(browser):
    """A second tab in the SAME Chrome process (one Chrome at a time)."""
    req = urllib.request.Request("http://127.0.0.1:%d/json/new?about:blank" % browser.port, method="PUT")
    with urllib.request.urlopen(req, timeout=5.0) as r:
        tgt = json.loads(r.read().decode("utf-8"))
    ws_url = tgt.get("webSocketDebuggerUrl")
    if not ws_url:
        raise cdp.CDPError("no webSocketDebuggerUrl for new tab")
    ws = cdp.WSClient(ws_url)
    return cdp.Page(ws, settle=browser.settle)


def got_it_scan(page, where, bucket):
    t = page.eval("document.body.innerText") or ""
    attrs = page.eval(
        "Array.prototype.map.call(document.querySelectorAll('[aria-label],[title],[placeholder]'),"
        "function(e){return [e.getAttribute('aria-label'),e.getAttribute('title'),"
        "e.getAttribute('placeholder')].join('|');}).join(' ')") or ""
    hay = (t + " " + attrs).lower()
    bad = "got it" in hay
    bucket.append((where, bad))
    if bad:
        print(f"  [SCAN-FAULT] 'got it' found at {where}")


def teardown(c, manifest):
    """Delete every row this run created, by the SNAPSHOTTED id lists in
    `manifest`, child tables first. ai_usage_events before profiles, per the
    brief. Best-effort: a missing table/id is tolerated so a partial run's
    teardown still removes everything it can."""
    aids = manifest.get("assignments", []) + manifest.get("auto_assignments", [])
    cls = manifest.get("classes", [])
    users = manifest.get("users", [])
    order = [
        ("ai_usage_events", "assignment_id", aids),
        ("flashcard_answer_verdicts", "assignment_id", aids),
        ("flashcard_reviews", "assignment_id", aids),
        ("flashcard_pupil_cards", "assignment_id", aids),
        ("flashcard_events", "assignment_id", aids),
        ("flashcard_sessions", "assignment_id", aids),
        ("assignment_submissions", "assignment_id", aids),
        ("assignment_flashcards", "assignment_id", aids),
        ("student_notifications", "assignment_id", aids),
        ("assignments", "id", aids),
        ("assignments", "class_id", cls),   # catch-all: any lazy auto-composed row
        ("flashcard_cards", "deck_id", manifest.get("decks", [])),
        ("flashcard_decks", "id", manifest.get("decks", [])),
        ("class_members", "class_id", cls),
        ("class_teachers", "class_id", cls),
        ("classes", "id", cls),
        ("academic_years", "id", manifest.get("years", [])),
        ("ai_usage_events", "profile_id", users),
        ("audit_log", "actor_id", users),
        ("profiles", "id", users),
        ("schools", "id", manifest.get("schools", [])),
    ]
    for table, col, ids in order:
        if not ids:
            continue
        st, body = c.write(table, "DELETE", {"__match__": f"{col}=in.({','.join(ids)})"})
        if st not in (200, 204):
            print(f"  teardown: {table} by {col} -> {st} {str(body)[:200]}")
    for uid in users:
        st, body = c.admin_delete_user(uid)
        if st not in (200, 204):
            print(f"  teardown: admin_delete_user {uid} -> {st} {str(body)[:160]}")


def check_residue(c, manifest):
    residue = {}
    for table, ids in [("schools", manifest.get("schools", [])), ("classes", manifest.get("classes", [])),
                       ("assignments", manifest.get("assignments", []) + manifest.get("auto_assignments", [])),
                       ("profiles", manifest.get("users", []))]:
        if not ids:
            continue
        st, rows = c.select(None, table, {"id": f"in.({','.join(ids)})", "select": "id"}, as_service=True)
        if rows:
            residue[table] = len(rows)
    return residue


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--shots", default=DEFAULT_SHOTS)
    ap.add_argument("--keep", action="store_true")
    ap.add_argument("--phases", default="all")
    a = ap.parse_args()
    phases = set(a.phases.split(",")) if a.phases != "all" else None

    def want(name):
        return phases is None or name in phases

    shots = a.shots
    os.makedirs(shots, exist_ok=True)
    mpath = os.path.join(shots, "manifest.json")
    stub_log = os.path.join(shots, "stub.log")
    scan_bucket = []

    env = acc.read_env(acc.BACKEND_ENV_DEFAULT)
    url, service = env["SUPABASE_URL"], env["SUPABASE_SERVICE_ROLE_KEY"]
    ref = acc.jwt_ref(service)
    if ref != acc.TEST_REF:
        acc.die(f"refusing: service key ref {ref} is not TEST ({acc.TEST_REF})")
    print(f"credential ref, proven from the key payload: {ref} => TEST")
    if not os.path.isdir(BACKEND_DIR):
        acc.die(f"backend worktree missing: {BACKEND_DIR}")

    c = acc.Client(url, acc.anon_key(), service)
    manifest = {"schools": [], "classes": [], "years": [], "users": [], "people": {},
                "decks": [], "assignments": []}

    sport, bport = free_port(), free_port()
    origin = f"http://127.0.0.1:{sport}"
    api = f"http://localhost:{bport}"
    subprocess.run(["pkill", "-f", "y_runthrough_import_map"], stderr=subprocess.DEVNULL)

    backend_proc = deno_proc = site_server = None
    all_console_errors = []

    def full_session(email):
        st, body = c._req("POST", f"{url}/auth/v1/token?grant_type=password",
                          {"apikey": c.anon, "Content-Type": "application/json"},
                          {"email": email, "password": acc.THROWAWAY_PASSWORD})
        if st != 200:
            acc.die(f"sign-in {email} -> {st} {body}")
        return body

    def make_phone(br, sess, width=390, height=844, kb=508):
        page = br.attach()
        page.send("Emulation.setDeviceMetricsOverride",
                  {"width": width, "height": height, "deviceScaleFactor": 2, "mobile": width < 900})
        if width < 900:
            page.send("Emulation.setTouchEmulationEnabled", {"enabled": True, "maxTouchPoints": 5})
            try:
                page.send("Emulation.setFocusEmulationEnabled", {"enabled": True})
            except cdp.CDPError:
                pass
        enable_fetch(page)
        page.send("Page.addScriptToEvaluateOnNewDocument", {"source": drv.FAKE_VV})
        page.send("Page.addScriptToEvaluateOnNewDocument", {"source": pf.session_js(ref, sess)})
        P = drv.Phone(page, width, height, kb, shots)
        return page, P

    def make_deck(tok_t, title, cards, subject, mode, klass, rule="secure"):
        st, deck = c.rpc(tok_t, "flashcard_deck_save", {
            "p_deck": None, "p_title": title, "p_cards": cards,
            "p_meta": {"source_kind": "typed", "subject": subject}, "p_finalise": True})
        if st != 200:
            acc.die(f"deck save ({title}) {st} {deck}")
        manifest["decks"].append(deck["deck_id"])
        now = datetime.now(timezone.utc)
        st, sw = c.rpc(tok_t, "flashcard_set_work", {
            "p_class_ids": [klass], "p_deck": deck["deck_id"], "p_mode": mode, "p_rule": rule,
            "p_title": title, "p_release_at": (now - timedelta(minutes=1)).isoformat(),
            "p_due_at": (now + timedelta(days=5)).isoformat(), "p_note": None,
            "p_client_ref": f"y2-{uuid.uuid4().hex[:12]}"})
        if st != 200:
            acc.die(f"set work ({title}) {st} {sw}")
        aid = sw["assignment_ids"][0]
        manifest["assignments"].append(aid)
        st, rows = c.select(None, "assignment_flashcards", {"assignment_id": f"eq.{aid}",
                                                             "select": "id,question,answer"}, as_service=True)
        by_q = {r["question"]: r["id"] for r in rows}
        return deck["deck_id"], aid, by_q, rows

    try:
        site_server, _ = cdp.serve(REPO, sport)
        backend_proc = start_backend(bport, origin, shots)
        print(f"backend {api} (pid {backend_proc.pid}), site {origin}")
        deno_proc = start_deno(url, service, shots, stub_log)
        print(f"deno stand-in on :{DENO_PORT} (pid {deno_proc.pid})")

        # ════════════════════════════════════════════════════════════
        # WORLD BUILD
        # ════════════════════════════════════════════════════════════
        ts = int(time.time())
        school, year, klass = str(uuid.uuid4()), str(uuid.uuid4()), str(uuid.uuid4())
        manifest["schools"].append(school)
        manifest["years"].append(year)
        manifest["classes"].append(klass)

        teacher_email = f"y2-t-{ts}@throwaway.test"
        teacher_id = c.admin_create_user(teacher_email, acc.THROWAWAY_PASSWORD)
        manifest["users"].append(teacher_id)

        PUPIL_CODES = (["pA", "pB", "pC", "pD", "pE", "pF", "pG", "pH", "pI", "pK"]
                       + [f"p{n:02d}" for n in range(1, 16)])
        pupils = {}
        for code in PUPIL_CODES:
            email = f"y2-{code}-{ts}@throwaway.test"
            uid = c.admin_create_user(email, acc.THROWAWAY_PASSWORD)
            manifest["users"].append(uid)
            pupils[code] = {"id": uid, "email": email}
        manifest["people"] = {"teacher": {"id": teacher_id, "email": teacher_email}, "pupils": pupils}

        acc._ok("school", *c.write("schools", "POST", {"id": school, "name": f"Y2 Flashcards {ts}",
                                    "code": f"Y2FC{ts}", "kind": "school",
                                    "key_stages_supported": ["KS4"]}))
        today = datetime.now(timezone.utc).date()
        start = f"{today.year if today.month >= 9 else today.year - 1}-09-01"
        end = f"{int(start[:4]) + 1}-08-31"
        acc._ok("year", *c.write("academic_years", "POST", {"id": year, "school_id": school, "name": "y2",
                                  "start_date": start, "end_date": end, "is_current": True}))
        acc._ok("class", *c.write("classes", "POST", {
            "id": klass, "school_id": school, "academic_year_id": year, "name": f"10y/Sc{ts % 10}",
            "key_stage": "KS4", "year_group": 10}))
        acc._ok("teacher_profile", *c.write("profiles", "PATCH", {
            "__match__": f"id=eq.{teacher_id}", "role": "teacher", "school_id": school,
            "first_name": "Tvd", "last_name": "Y2", "display_name": "Tvd Y2",
            "username": f"y2t{ts:x}"}))
        st, subj = c.select(None, "subjects", {"select": "id,name", "name": "eq.Physics"}, as_service=True)
        acc._ok("class_teachers", *c.write("class_teachers", "POST", {
            "class_id": klass, "teacher_id": teacher_id, "role": "subject_teacher", "subject_id": subj[0]["id"]}))
        for code, p in pupils.items():
            acc._ok(f"profile:{code}", *c.write("profiles", "PATCH", {
                "__match__": f"id=eq.{p['id']}", "role": "student", "school_id": school,
                "first_name": code, "last_name": "Y2", "display_name": f"{code} Y2",
                "username": f"y2{code}{ts:x}", "science_pathway": "combined", "tier": "higher"}))
        acc._ok("class_members", *c.write("class_members", "POST", [
            {"class_id": klass, "student_id": p["id"], "joined_via": "admin_added"} for p in pupils.values()]))
        tok_t = c.sign_in(teacher_email, acc.THROWAWAY_PASSWORD)
        json.dump(manifest, open(mpath, "w"), indent=1)
        print(f"world built: school={school} class={klass} 1 teacher + {len(pupils)} pupils")

        # ── decks + set work ────────────────────────────────────────
        D1_CARDS = [
            {"question": "How can the mean rate of a reaction be calculated from a graph?",
             "answer": "Calculate the gradient (change in y/change in x)"},
            {"question": "How can the rate of a reaction at a specific time be calculated from a graph?",
             "answer": "Draw a tangent to the curve at that time and calculate the gradient of tangent"},
            {"question": "Define activation energy.",
             "answer": "The minimum amount of energy needed for particles to react"},
            {"question": "Explain how increasing concentration affects the rate of a reaction.",
             "answer": "Increases the number of particles in the same volume, increases frequency of "
                       "collisions, increases rate of reaction"},
            {"question": "What is a catalyst?",
             "answer": "A substance that increases the rate of a reaction but is not used up during "
                       "the reaction."},
            {"question": "Explain the effect adding a catalyst has on the rate of a reaction.",
             "answer": "Increases the rate of reaction by providing an alternative reaction pathway "
                       "with a lower activation energy"},
            {"question": "Name a piece of equipment needed to measure a volume of gas.",
             "answer": "Inverted measuring cylinder (in water), gas syringe"},
            {"question": "What is a closed system?",
             "answer": "When the equipment used for an experiment stops any of the reactants or "
                       "products from escaping"},
            {"question": "When does a reversible reaction reach equilibrium?",
             "answer": "When the forward and reverse reactions occur at the same rate in a closed system"},
            {"question": "What affect will increasing the temperature have on a reversible reaction?",
             "answer": "Position of equilibrium will shift in the endothermic direction"},
        ]
        D2_CARDS = [
            {"question": "What is kinetic energy?", "answer": "Energy that is stored in moving objects"},
            {"question": "What unit is energy measured in?", "answer": "Joules (J)"},
            {"question": "Define power.",
             "answer": "The rate of energy transfer OR the amount of work done in a given period of time"},
            {"question": "What is the gravitational field strength on Earth?", "answer": "9.8 N/kg"},
            {"question": "What is gravitational potential energy?",
             "answer": "Energy stored in an object because of its height above the ground"},
            {"question": "What equation links force, mass and acceleration?",
             "answer": "Newton's second law (N2): force = mass times acceleration"},
            {"question": "What is the principle of conservation of energy?",
             "answer": "Energy cannot be created or destroyed, only transferred from one store to another"},
            {"question": "What is efficiency?",
             "answer": "The proportion of energy transferred usefully, given as a percentage or decimal"},
            {"question": "What is elastic potential energy?",
             "answer": "Energy stored in a stretched or squashed object such as a spring"},
            {"question": "What is thermal energy (internal energy)?",
             "answer": "The total kinetic and potential energy of all the particles in a system"},
        ]
        D3_CARDS = [{"question": "What is the unit of force?", "answer": "The newton (N)"}]
        D4_CARDS = [{"question": f"What is term {i}?",
                     "answer": f"This is the definition of term {i}, written to a realistic revision "
                               f"length for timing purposes."} for i in range(1, 41)]
        D5_CARDS = [
            {"question": "Explain, in as much detail as you can, why the rate of a chemical reaction "
                        "between a metal and an acid increases when the acid's concentration is "
                        "increased, referring to particle collisions and the frequency with which "
                        "they occur in the same volume of solution over the same period of time.",
             "answer": "When the concentration of the acid is increased, there are more acid particles "
                       "in the same volume of solution. This means the particles are closer together "
                       "on average, so they collide with the metal's surface particles more "
                       "frequently. A greater frequency of collisions means a greater frequency of "
                       "collisions with enough energy to exceed the activation energy, so more "
                       "successful collisions happen per second, and the rate of reaction increases."},
            {"question": "Describe, step by step, how you would carry out an experiment to measure the "
                        "rate of a reaction between marble chips and dilute hydrochloric acid by "
                        "measuring the mass of the flask over time, including the apparatus you would "
                        "use and how you would use your results to find the rate.",
             "answer": "Place a known mass of marble chips into a conical flask on a balance, plug the "
                       "flask with cotton wool to let gas escape but stop acid spray, add a measured "
                       "volume of dilute hydrochloric acid, start a timer immediately, and record the "
                       "mass shown on the balance at regular time intervals, for example every ten "
                       "seconds, until the mass stops changing. Plot a graph of mass lost against time "
                       "and calculate the gradient at any point to find the rate of reaction at that time."},
            {"question": "Explain why a reaction between magnesium ribbon and hydrochloric acid happens "
                        "faster when the magnesium is cut into smaller pieces, in terms of surface "
                        "area to volume ratio and particle collisions, compared with a single larger "
                        "piece of the same total mass.",
             "answer": "Cutting the magnesium into smaller pieces increases its total surface area "
                       "without changing its total volume or mass, so more magnesium particles are "
                       "exposed on the surface and available to collide with acid particles at any "
                       "one time. This increases the frequency of collisions between acid particles "
                       "and magnesium particles, so more successful collisions happen per second, "
                       "and the rate of reaction increases compared with the single larger piece."},
            {"question": "Explain what is meant by a reversible reaction reaching dynamic equilibrium "
                        "in a closed system, describing what is happening to the forward and reverse "
                        "reactions and to the concentrations of reactants and products at that point.",
             "answer": "A reversible reaction reaches dynamic equilibrium when the forward reaction "
                       "and the reverse reaction are both still happening, but they are happening at "
                       "exactly the same rate as each other in a closed system, so there is no overall "
                       "change in the amounts of reactants and products present. The concentrations of "
                       "reactants and products stay constant over time, even though both reactions "
                       "are continuing, because reactants are being used up at the same rate as they "
                       "are being reformed from the products."},
            {"question": "Describe, with reference to collision theory, why increasing the temperature "
                        "of a reaction mixture increases the rate of reaction, including what happens "
                        "to the particles' energy and the proportion of collisions that succeed.",
             "answer": "Increasing the temperature gives the reacting particles more kinetic energy, so "
                       "they move around faster. This means they collide with each other more "
                       "frequently, but more importantly, a greater proportion of those collisions now "
                       "have enough energy to exceed the activation energy of the reaction. Because a "
                       "larger fraction of collisions are successful, the rate of reaction increases "
                       "even though the total number of particles has not changed."},
            {"question": "Explain how a catalyst increases the rate of a reaction without being used up "
                        "itself, in terms of the activation energy and the reaction pathway, and state "
                        "one industrial reaction where a catalyst is commonly used.",
             "answer": "A catalyst works by providing an alternative reaction pathway for the reactants "
                       "that has a lower activation energy than the uncatalysed pathway. This means a "
                       "greater proportion of collisions between particles now have enough energy to "
                       "react successfully, so the rate of reaction increases. The catalyst itself "
                       "takes part in the reaction but is regenerated at the end, so its own mass "
                       "stays the same overall. An iron catalyst is commonly used in the Haber process "
                       "to manufacture ammonia from nitrogen and hydrogen."},
        ]
        D6_CARDS = [
            {"question": "What is the formula of carbon dioxide?", "answer": "Carbon dioxide (CO2)"},
            {"question": "What is the formula of sulfuric acid?", "answer": "Sulfuric acid (H2SO4)"},
            {"question": "What is the formula of methane?", "answer": "Methane (CH4)"},
            {"question": "What is the formula of sodium carbonate?", "answer": "Sodium carbonate (Na2CO3)"},
            {"question": "What apparatus is used to measure a volume of gas given off?",
             "answer": "A gas syringe or an inverted measuring cylinder in water"},
        ]
        D7_CARDS = [
            {"question": "What is the test for chlorine gas?", "answer": "It bleaches damp blue litmus paper white"},
            {"question": "What is the test for oxygen gas?", "answer": "A glowing splint relights"},
            {"question": "What is the test for hydrogen gas?", "answer": "A lit splint makes a squeaky pop"},
        ]
        D8_CARDS = [
            {"question": "What is the unit of current?", "answer": "The ampere (A)"},
            {"question": "What is the unit of potential difference?", "answer": "The volt (V)"},
            {"question": "What is the unit of power?", "answer": "The watt (W)"},
        ]
        D9_CARDS = [
            {"question": "What is the unit of energy?", "answer": "The joule (J)"},
            {"question": "What is the unit of time?", "answer": "The second (s)"},
            {"question": "What is the unit of mass?", "answer": "The kilogram (kg)"},
            {"question": "What is the unit of length?", "answer": "The metre (m)"},
        ]
        D10_CARDS = [
            {"question": "What is speed?", "answer": "Distance travelled per unit time"},
            {"question": "What is acceleration?", "answer": "The rate of change of velocity"},
            {"question": "What is momentum?", "answer": "Mass multiplied by velocity"},
            {"question": "What is a vector quantity?", "answer": "A quantity with both magnitude and direction"},
            {"question": "What is a scalar quantity?", "answer": "A quantity with magnitude only, no direction"},
        ]

        _, aid1, by_q1, rows1 = make_deck(tok_t, "Rate of Reaction", D1_CARDS, "chemistry", "make", klass)
        _, aid2, by_q2, rows2 = make_deck(tok_t, "Energy", D2_CARDS, "physics", "review", klass)
        _, aid3, by_q3, rows3 = make_deck(tok_t, "One card", D3_CARDS, "physics", "review", klass)
        _, aid4, by_q4, rows4 = make_deck(tok_t, "Forty cards", D4_CARDS, "chemistry", "make", klass)
        _, aid5, by_q5, rows5 = make_deck(tok_t, "Long answers", D5_CARDS, "chemistry", "review", klass)
        _, aid6, by_q6, rows6 = make_deck(tok_t, "Formulae", D6_CARDS, "chemistry", "review", klass)
        _, aid7, by_q7, rows7 = make_deck(tok_t, "Gas tests", D7_CARDS, "chemistry", "make", klass)
        _, aid8, by_q8, rows8 = make_deck(tok_t, "Two tabs", D8_CARDS, "physics", "make", klass)
        _, aid9, by_q9, rows9 = make_deck(tok_t, "Double tap", D9_CARDS, "physics", "make", klass)
        _, aid10, by_q10, rows10 = make_deck(tok_t, "Kill tab", D10_CARDS, "physics", "make", klass)
        json.dump(manifest, open(mpath, "w"), indent=1)
        print("all 10 decks set to the class")

        # ── seed ~6 background pupils into mixed states on D1, via real
        # RPC as those pupils (never through the browser) — the rest (9)
        # stay completely untouched, so the teacher pages look like a real
        # class: some done, some mid-way, some missing. ──────────────────
        bg_cards = rows1
        bg_plan = {
            "p01": lambda i: "got_it",                              # fully done
            "p02": lambda i: "got_it" if i < 7 else "not_yet",       # mostly done
            "p03": lambda i: "got_it" if i < 3 else None,            # in progress
            "p04": lambda i: ("nearly" if i % 2 == 0 else "got_it") if i < 5 else None,
            "p05": lambda i: "got_it" if i < 10 else None,           # fully done, 2nd pupil
            "p06": lambda i: "not_yet" if i < 2 else None,           # barely started
        }
        for code, rating_fn in bg_plan.items():
            tok_p = c.sign_in(pupils[code]["email"], acc.THROWAWAY_PASSWORD)
            t0 = datetime.now(timezone.utc) - timedelta(minutes=random.randint(5, 180))
            evs = acc.make_events(bg_cards, "make", rating_fn, "bg answer", t0, step_ms=350, mode="make")
            st, r = acc.run_events(c, tok_p, aid1, evs)
            check(st == 200, f"background seed {code} on Rate of Reaction wrote cleanly (got {st} {r})")
        print("background pupils seeded (p01-p06 mixed, p07-p15 untouched)")

        if not want("world"):
            pass  # world is always needed by every other phase; never actually skip it

        # ════════════════════════════════════════════════════════════
        # SESSION 1 — Pupil A, phone 390×844, light theme: Rate of
        # Reaction (make mode). The core rule end to end.
        # ════════════════════════════════════════════════════════════
        if want("rule"):
            # ⊕ Y review — the same session at any size and theme:
            # Y_VIEW=phone-light (default) | phone-dark | phone360-dark |
            # desktop-light | desktop-dark.
            view = os.environ.get("Y_VIEW", "phone-light")
            vw, vh, vkb = {"phone": (390, 844, 508), "phone360": (360, 740, 404),
                           "desktop": (1280, 800, 0)}[view.split("-")[0]]
            vtheme = view.split("-")[1]
            br1 = cdp.Browser().start()
            page1, P1 = make_phone(br1, full_session(pupils["pA"]["email"]), width=vw, height=vh, kb=vkb)
            seen1 = set()
            s = open_deck(P1, page1, origin, api, aid1)
            P1.q("document.documentElement.setAttribute('data-theme', %s)" % json.dumps(vtheme))
            settle(0.3)
            path = "P1-P9 (Rate of Reaction, make, %s)" % view
            check(s["strip"] and s["writing"], "pupil deck opens")
            no_got_it(page1, "deck open")
            Q = [c0["question"] for c0 in D1_CARDS]

            # card 1 — typed right first time -> Secured (P1)
            P1.type(D1_CARDS[0]["answer"])
            P1.click('[data-hw="check"]')
            s = wait_chip(P1, page1, seen1)
            ok1 = s["chip"] == "Right" and not s["pressed"] and "got_it" in s["enabled"]
            record(path, "card1: typed the exact model answer", f"chip={s['chip']!r} pressed={s['pressed']!r}",
                   "PASS" if ok1 else "FAULT")
            P1.shot("c1-right")
            P1.click('[data-hw="got_it"]')
            settle(0.5)

            # card 2 — I don't know -> learn -> Nearly hint (no cap) -> replay -> right -> Secured (P2)
            s = P1.st()
            check(s["front"] == Q[1] and s["idk"], "card 2 up, idk offered")
            P1.click('[data-hw="idk"]')
            s = P1.st()
            learn_ok = bool(s["learn"]) and s["writing"]
            record(path, "card2: I don't know", f"learn={s['learn']!r}", "PASS" if learn_ok else "FAULT")
            P1.type("draw a tangent to about half the curve roughly and find its gradient")
            P1.click('[data-hw="check"]')
            s = wait_chip(P1, page1, seen1)
            nearly_ok = s["chip"] == "Nearly" and sorted(s["enabled"]) == ["got_it", "nearly", "not_yet"]
            record(path, "card2 learn-step answer (contains 'half')",
                   f"chip={s['chip']!r} enabled={s['enabled']!r}", "PASS" if nearly_ok else "FAULT")
            P1.shot("c2-nearly-hint")
            P1.click('[data-hw="nearly"]')

            # card 3 — the ONE-WORD finding (coordinator's note): "energy"
            # for "Define activation energy." Record chip, cap, stored rows.
            s = P1.st()
            check(s["front"] == Q[2], "card 3 up")
            P1.type("energy")
            P1.click('[data-hw="check"]')
            s = wait_chip(P1, page1, seen1)
            record("FINDING: one-word answer 'energy'", "typed the single word 'energy' for "
                   "'Define activation energy.' (multi-word model answer)",
                   f"chip={s['chip']!r} pressed={s['pressed']!r} enabled={s['enabled']!r}", "FINDING")
            P1.click('[data-hw="%s"]' % (hint(s) or "not_yet"))
            settle(1.0)
            card3_id = by_q1[D1_CARDS[2]["question"]]
            st_pc, pc_rows = c.select(None, "flashcard_pupil_cards",
                                      {"assignment_id": f"eq.{aid1}", "pupil_id": f"eq.{pupils['pA']['id']}",
                                       "card_id": f"eq.{card3_id}", "select": "answer_check,answer"},
                                      as_service=True)
            rv_rows = fetch_reviews(c, aid1, pupils["pA"]["id"])
            card3_ratings = [r["rating"] for r in rv_rows if r["card_id"] == card3_id]
            record("FINDING: one-word answer 'energy' — stored rows", "after rating it as suggested",
                   f"flashcard_pupil_cards.answer_check={pc_rows!r}; flashcard_reviews ratings={card3_ratings!r}",
                   "FINDING")

            # card 4 — Nearly via a typed partial; BACK/FORWARD dance while
            # still in state A (P3 + P7); then rate Nearly.
            s = P1.st()
            check(s["front"] == Q[3], "card 4 up")
            rows_before = fetch_reviews(c, aid1, pupils["pA"]["id"])
            start_front = s["front"]
            P1.click('[data-hw="back"]')
            P1.click('[data-hw="back"]')
            check(bool(P1.q("!!document.querySelector('[data-hw=\"forward\"]')")), "Forward offered after Back")
            P1.click('[data-hw="forward"]')
            P1.click('[data-hw="forward"]')
            s = P1.st()
            rows_after = fetch_reviews(c, aid1, pupils["pA"]["id"])
            bf_ok = s["front"] == start_front and len(rows_after) == len(rows_before)
            record(path, "card4: Back x2, Forward x2 (P7)",
                   f"front {start_front!r}->{s['front']!r}, rows {len(rows_before)}->{len(rows_after)}",
                   "PASS" if bf_ok else "FAULT")
            P1.type("increases collisions by about half I think honestly")
            P1.click('[data-hw="check"]')
            s = wait_chip(P1, page1, seen1)
            check(s["chip"] == "Nearly", "card4 typed-partial -> Nearly (P3)")
            check(s["flipped"] == "1" and s["back_"] == D1_CARDS[3]["answer"], "model answer shown under the verdict")
            P1.shot("c4-nearly")
            P1.click('[data-hw="nearly"]')

            # card 5 — Wrong via a typed answer containing 'wrong' (P4)
            s = P1.st()
            check(s["front"] == Q[4], "card 5 up")
            P1.type("something wrong I don't really know sorry")
            P1.click('[data-hw="check"]')
            s = wait_chip(P1, page1, seen1)
            wrong_ok = s["chip"] == "Wrong" and sorted(s["enabled"]) == ["got_it", "nearly", "not_yet"]
            record(path, "card5: typed answer containing 'wrong'", f"chip={s['chip']!r} enabled={s['enabled']!r}",
                   "PASS" if wrong_ok else "FAULT")
            P1.click('[data-hw="not_yet"]')

            # card 6 — literal "idk" -> blank/Not yet only (P5)
            s = P1.st()
            check(s["front"] == Q[5], "card 6 up")
            P1.type("idk")
            P1.click('[data-hw="check"]')
            s = P1.st()
            blank_ok = s["chip"] == "No answer" and sorted(s["enabled"]) == ["got_it", "nearly", "not_yet"]
            record(path, "card6: typed literal 'idk' (blank)", f"chip={s['chip']!r} enabled={s['enabled']!r}",
                   "PASS" if blank_ok else "FAULT")
            P1.click('[data-hw="not_yet"]')

            # cards 7-10 — typed right first time
            for i in (6, 7, 8, 9):
                s = P1.st()
                check(s["front"] == Q[i], f"card {i+1} up")
                P1.type(D1_CARDS[i]["answer"])
                P1.click('[data-hw="check"]')
                s = wait_chip(P1, page1, seen1)
                check(hint(s) == "got_it" and not s["pressed"] and "got_it" in s["enabled"], f"card {i+1} right first time")
                P1.click('[data-hw="got_it"]')

            # §13.1.4 replay of the idk card (card 2), once more, plain
            s = P1.st()
            t0 = time.time()
            while time.time() - t0 < 6 and s.get("end1") is None and s.get("front") != Q[1]:
                time.sleep(0.2)
                s = P1.st()
            if s.get("end1") is None:
                replay_ok = s["front"] == Q[1] and not s["learn"]
                record(path, "card2 idk replay (once more, same pass, §13.1.4)",
                       f"front={s['front']!r} learn={s['learn']!r}", "PASS" if replay_ok else "FAULT")
                P1.type(D1_CARDS[1]["answer"])
                P1.click('[data-hw="check"]')
                s = wait_chip(P1, page1, seen1)
                check(hint(s) == "got_it" and not s["pressed"] and "got_it" in s["enabled"], "replay answered right -> Secured (P2 end)")
                P1.click('[data-hw="got_it"]')
            s = wait_end(P1)

            # end screen — leftovers (P6)
            record(path, "end screen with leftovers (card4 nearly, card5 wrong, card6 blank)",
                   f"end1={s['end1']!r} retryPass={s['retryPass']!r} done={s['done']!r} again={s['again']!r}",
                   "PASS" if (s["end1"] == "7 of 10 secured" and s["retryPass"] == "Try again"
                             and s["done"] is None and s["again"] is None) else "FAULT")
            no_got_it(page1, "end screen (leftovers)")
            P1.shot("end-leftovers")

            # Try again -> secure the leftovers
            P1.click('[data-hw="retry-pass"]')
            for want_q, ans in [(Q[3], D1_CARDS[3]["answer"]), (Q[4], D1_CARDS[4]["answer"]),
                                (Q[5], D1_CARDS[5]["answer"])]:
                s = P1.st()
                check(s["front"] == want_q, f"try-again lands on {want_q!r}")
                P1.type(ans)
                P1.click('[data-hw="check"]')
                s = wait_chip(P1, page1, seen1)
                check(hint(s) == "got_it" and not s["pressed"] and "got_it" in s["enabled"], "retyped correctly -> Secured suggested")
                P1.click('[data-hw="got_it"]')
            settle(0.6)
            s = wait_end(P1)
            record(path, "all secured after Try again",
                   f"end1={s['end1']!r} done={s['done']!r} again={s['again']!r} retryPass={s['retryPass']!r}",
                   "PASS" if (s["end1"] == "10 of 10 secured" and s["done"] == "Done"
                             and s["again"] == "Revise flashcards one more time"
                             and s["retryPass"] is None) else "FAULT")
            no_got_it(page1, "end screen (all secured)")
            P1.shot("end-done")
            got_it_scan(page1, "pupil deck, done screen", scan_bucket)

            # P9a — the voluntary Revise: a fresh full pass, never un-secures
            P1.click('[data-hw="again"]')
            settle(0.6)
            for i in range(10):
                s = P1.st()
                f = s["front"]
                ans = next(cc["answer"] for cc in D1_CARDS if cc["question"] == f)
                P1.type(ans)
                P1.click('[data-hw="check"]')
                P1.click('[data-hw="got_it"]')
            settle(0.8)
            s = P1.st()
            check(s["end1"] == "10 of 10 secured" and s["done"] == "Done", "revise pass: still all secured")
            P1.click('[data-hw="done"]')
            settle(0.5)

            # P9b — reopen the FINISHED homework from a fresh navigation
            # (not the in-page Revise button), confirm it reopens cleanly.
            s = open_deck(P1, page1, origin, api, aid1)
            reopen_ok = bool(s["strip"]) and (s["panel"] or s["again"] or s["writing"])
            record(path, "P9: reopen the finished homework via a fresh navigation",
                   f"strip={s['strip']!r} panel={s['panel']!r} again={s.get('again')!r} writing={s['writing']!r}",
                   "PASS" if reopen_ok else "FAULT")
            P1.shot("reopen-finished")
            if s.get("again"):
                P1.click('[data-hw="again"]')
                settle(0.6)
                for i in range(10):
                    st_ = P1.st()
                    if not st_["writing"]:
                        break
                    f = st_["front"]
                    ans = next(cc["answer"] for cc in D1_CARDS if cc["question"] == f)
                    P1.type(ans)
                    P1.click('[data-hw="check"]')
                    P1.click('[data-hw="got_it"]')
                settle(0.8)
                s = wait_end(P1)
                record(path, "P9: a second revise pass after reopening via a fresh navigation",
                       f"end1={s.get('end1')!r} done={s.get('done')!r}",
                       "PASS" if s.get("end1") == "10 of 10 secured" and s.get("done") == "Done" else "FAULT")
                P1.shot("revised-again")

            all_console_errors += no_fav(page1.console_errors())
            br1.close()
            json.dump(manifest, open(mpath, "w"), indent=1)
            print("session 1 (rule walkthrough) done")

        # ════════════════════════════════════════════════════════════
        # SESSION 2 — Pupil B, desktop 1280×800, light: Energy (review
        # mode) + the N2 formula-render check (gated by subject).
        # Also: double-click on Check/rating/Back/Forward -> no double-advance.
        # ════════════════════════════════════════════════════════════
        if want("review"):
            br2 = cdp.Browser().start()
            page2, P2 = make_phone(br2, full_session(pupils["pB"]["email"]), width=1280, height=800, kb=0)
            seen2 = set()
            s = open_deck(P2, page2, origin, api, aid2)
            path = "review mode (Energy, desktop, light) + N2 formula gate"
            check(s["strip"] and s["writing"], "pupil deck opens (review mode)")

            # double-click Check on card 1 — must not double-advance
            P2.type(D2_CARDS[0]["answer"])
            rows_b = fetch_reviews(c, aid2, pupils["pB"]["id"])
            P2.q("(function(){var e=document.querySelector('[data-hw=\"check\"]'); e.click(); e.click();})()")
            settle(0.4)
            s = wait_chip(P2, page2, seen2)
            rows_a = fetch_reviews(c, aid2, pupils["pB"]["id"])
            dbl_ok = s["chip"] == "Right"
            record(path, "double-click Check on card1", f"chip={s['chip']!r} rows {len(rows_b)}->{len(rows_a)}",
                   "PASS" if dbl_ok else "FAULT")
            P2.q("(function(){var e=document.querySelector('[data-hw=\"got_it\"]'); if(e){e.click(); e.click();}})()")
            settle(0.4)
            s2 = P2.st()
            rows_a2 = fetch_reviews(c, aid2, pupils["pB"]["id"])
            adv_ok = s2["front"] == D2_CARDS[1]["question"]  # exactly ONE card forward, not two
            record(path, "double-click Secured (got_it) on card1",
                   f"landed on {s2['front']!r} (want card2), rows now {len(rows_a2)}",
                   "PASS" if adv_ok else "FAULT")

            # card 2 — right
            P2.type(D2_CARDS[1]["answer"])
            P2.click('[data-hw="check"]')
            P2.click('[data-hw="got_it"]')
            # cards 3,4,5 right, card 6 is the N2 card
            for i in (2, 3, 4):
                s = P2.st()
                check(s["front"] == D2_CARDS[i]["question"], f"card{i+1} up")
                P2.type(D2_CARDS[i]["answer"])
                P2.click('[data-hw="check"]')
                P2.click('[data-hw="got_it"]')
            s = P2.st()
            check(s["front"] == D2_CARDS[5]["question"], "N2 card up")
            P2.type(D2_CARDS[5]["answer"])
            P2.click('[data-hw="check"]')
            s = wait_chip(P2, page2, seen2)
            subs = P2.q("document.querySelector('[data-dc-tpl=\"10353\"]') ? "
                       "document.querySelector('[data-dc-tpl=\"10353\"]').querySelectorAll('sub').length : null")
            back_text = s["back_"]
            n2_ok_no_sub = subs == 0
            record(path, "physics deck ('N2' in the answer) — formula gate should be subject-off",
                   f"model-answer face text={back_text!r} <sub> count={subs!r}",
                   "PASS (no subscript, as the subject gate intends)" if n2_ok_no_sub
                   else "FAULT (a physics deck's 'N2' got subscripted like a chemical formula)")
            P2.shot("n2-card")
            P2.click('[data-hw="got_it"]')
            for i in (6, 7, 8, 9):
                s = P2.st()
                check(s["front"] == D2_CARDS[i]["question"], f"card{i+1} up")
                P2.type(D2_CARDS[i]["answer"])
                P2.click('[data-hw="check"]')
                P2.click('[data-hw="got_it"]')
            settle(0.6)
            s = wait_end(P2)
            check(s["end1"] == "10 of 10 secured" and s["done"] == "Done", "review-mode deck finishes cleanly")
            got_it_scan(page2, "pupil review-mode done screen", scan_bucket)
            P2.shot("review-done-desktop")
            all_console_errors += no_fav(page2.console_errors())
            br2.close()
            print("session 2 (review mode + N2 + double-tap spot-check) done")

        # ════════════════════════════════════════════════════════════
        # SESSION 3 — Pupil F, phone 390×844, DARK theme: Formulae deck.
        # ════════════════════════════════════════════════════════════
        if want("formulae"):
            br3 = cdp.Browser().start()
            page3, P3 = make_phone(br3, full_session(pupils["pF"]["email"]))
            P3.q("document.documentElement.setAttribute('data-theme','dark')")
            seen3 = set()
            s = open_deck(P3, page3, origin, api, aid6)
            path = "formulae deck (chemistry, phone, dark)"
            check(s["strip"] and s["writing"], "formulae deck opens, dark theme")
            for i, cd in enumerate(D6_CARDS):
                s = P3.st()
                check(s["front"] == cd["question"], f"formula card{i+1} up")
                if i == 0:
                    P3.click('[data-hw="idk"]')
                    s = P3.st()
                    learn_text = s["learn"]
                    record(path, "card1 (CO2) learn step: shown-answer text",
                           f"learn={learn_text!r}", "PASS" if learn_text and "CO2" in learn_text else "FAULT")
                P3.type(cd["answer"])
                P3.click('[data-hw="check"]')
                s = wait_chip(P3, page3, seen3)
                mine_subs = P3.q("document.querySelector('[data-hw=\"mine\"]') ? "
                                "document.querySelector('[data-hw=\"mine\"]').querySelectorAll('sub').length : null")
                back_subs = s["backSubs"]
                record(path, f"card{i+1} ({cd['answer']}) — formula rendering",
                       f"chip={s['chip']!r} back_text={s['back_']!r} back <sub> count={back_subs!r} "
                       f"mine <sub> count={mine_subs!r}",
                       "PASS" if (i < 4 and back_subs and back_subs > 0) or (i == 4 and (back_subs or 0) == 0)
                       else "FAULT")
                if i == 0:
                    record(path, "card1: typed the exact model answer via the 'I don't know' learn step",
                           f"chip={s['chip']!r} pressed={s['pressed']!r} enabled={s['enabled']!r}",
                           "PASS (no cap after I don't know: Secured is enabled — the pupil decides, 5 Oct)"
                           if "got_it" in (s.get("enabled") or []) else
                           "FAULT (Secured was refused after I don't know)")
                P3.shot(f"formula-card{i+1}-dark")
                P3.click('[data-hw="%s"]' % (hint(s) or "got_it"))
            settle(0.6)
            s = P3.st()
            t0 = time.time()
            while time.time() - t0 < 6 and s.get("end1") is None and s.get("front") != D6_CARDS[0]["question"]:
                time.sleep(0.2)
                s = P3.st()
            if s.get("end1") is None and s.get("front") == D6_CARDS[0]["question"] and not s.get("learn"):
                # §13.1.4: the idk-marked card1 replays once more, plain,
                # before the pass can end — answer it from memory.
                P3.type(D6_CARDS[0]["answer"])
                P3.click('[data-hw="check"]')
                s = wait_chip(P3, page3, seen3)
                P3.click('[data-hw="got_it"]' if hint(s) == "got_it" else '[data-hw="not_yet"]')
            settle(0.6)
            s = wait_end(P3)
            if s.get("retryPass"):
                P3.click('[data-hw="retry-pass"]')
                settle(0.6)
                s = P3.st()
                if s["writing"]:
                    P3.type(D6_CARDS[0]["answer"])
                    P3.click('[data-hw="check"]')
                    s = wait_chip(P3, page3, seen3)
                    P3.click('[data-hw="got_it"]' if hint(s) == "got_it" else '[data-hw="not_yet"]')
                settle(0.8)
                s = wait_end(P3, timeout=10)
            check(s["done"] == "Done", f"formulae deck finishes (end1={s.get('end1')!r})")
            got_it_scan(page3, "formulae deck done screen (dark)", scan_bucket)
            P3.shot("formulae-done-dark")
            all_console_errors += no_fav(page3.console_errors())
            br3.close()
            print("session 3 (formulae, dark theme) done")

        # ════════════════════════════════════════════════════════════
        # SESSION 4 — edges: one-card, forty-card (timing), long-answer
        # (phone readability). All phone, light.
        # ════════════════════════════════════════════════════════════
        if want("edges"):
            br4 = cdp.Browser().start()
            page4, P4 = make_phone(br4, full_session(pupils["pC"]["email"]))
            path = "one-card deck (edge)"
            t_open0 = time.time()
            s = open_deck(P4, page4, origin, api, aid3)
            t_open1 = time.time()
            check(s["strip"] and s["writing"], "one-card deck opens")
            P4.type(D3_CARDS[0]["answer"])
            P4.click('[data-hw="check"]')
            s = wait_chip(P4, page4, set())
            check(hint(s) == "got_it" and not s["pressed"] and "got_it" in s["enabled"], "one-card: typed right -> Secured suggested")
            P4.click('[data-hw="got_it"]')
            settle(0.6)
            s = wait_end(P4)
            record(path, "a 1-card deck: open -> answer -> immediate finish",
                   f"open took {t_open1-t_open0:.2f}s, end1={s['end1']!r} done={s['done']!r}",
                   "PASS" if s["end1"] == "1 of 1 secured" and s["done"] == "Done" else "FAULT")
            P4.shot("onecard-done")
            br4.close()

            br5 = cdp.Browser().start()
            page5, P5 = make_phone(br5, full_session(pupils["pD"]["email"]))
            path = "40-card deck (performance)"
            t0 = time.time()
            s = open_deck(P5, page5, origin, api, aid4, wait=60)
            t_open = time.time() - t0
            check(s["strip"] and s["writing"], "40-card deck opens")
            per_card = []
            for i in range(40):
                tc0 = time.time()
                st_ = P5.st()
                if not st_["writing"]:
                    break
                f = st_["front"]
                ans = next(cc["answer"] for cc in D4_CARDS if cc["question"] == f)
                P5.type(ans)
                P5.click('[data-hw="check"]')
                st_ = P5.st()
                P5.click('[data-hw="got_it"]' if hint(st_) == "got_it" else '[data-hw="not_yet"]')
                per_card.append(time.time() - tc0)
            settle(0.8)
            s = wait_end(P5, timeout=10)
            avg_card = sum(per_card) / len(per_card) if per_card else None
            record(path, "opened + drove all 40 cards",
                   f"open={t_open:.2f}s, cards driven={len(per_card)}, avg/card={avg_card:.2f}s "
                   f"(includes {drv.settle.__defaults__[0] if False else 0.3+0.25}s of fixed settle sleeps), "
                   f"end1={s.get('end1')!r}",
                   "PASS" if s.get("end1") and "40" in s["end1"] else "FAULT")
            P5.shot("forty-done")
            br5.close()

            br6 = cdp.Browser().start()
            page6, P6 = make_phone(br6, full_session(pupils["pE"]["email"]))
            path = "very-long-answer deck (phone readability)"
            s = open_deck(P6, page6, origin, api, aid5, wait=30)
            check(s["strip"] and s["writing"], "long-answer deck opens")
            for i, cd in enumerate(D5_CARDS):
                s = P6.st()
                P6.keyboard(True)
                rest = P6.q(drv.CARD_JS)
                b = P6.q(drv.BOXES_JS)
                clipped = rest.get("frontClipped")
                check_visible = b.get("checkVisible")
                record(path, f"long card{i+1}: question {len(cd['question'])}ch, answer {len(cd['answer'])}ch",
                       f"frontClipped={clipped!r} checkVisible={check_visible!r} q-box={b.get('q')!r} "
                       f"t-box={b.get('t')!r}",
                       "PASS" if (not clipped and check_visible) else "FAULT")
                P6.shot(f"longanswer-card{i+1}")
                P6.keyboard(False)
                P6.type(cd["answer"])
                P6.click('[data-hw="check"]')
                s = wait_chip(P6, page6, set())
                P6.click('[data-hw="got_it"]' if hint(s) == "got_it" else '[data-hw="not_yet"]')
            settle(0.6)
            s = wait_end(P6, timeout=10)
            check(bool(s.get("done")) or bool(s.get("retryPass")), "long-answer deck reaches an end screen")
            P6.shot("longanswer-end")
            br6.close()
            print("session 4 (edges) done")

        # ════════════════════════════════════════════════════════════
        # SESSION 5 — slow (6s) / failed (500) model check.
        # ════════════════════════════════════════════════════════════
        if want("slowfail"):
            br7 = cdp.Browser().start()
            page7, P7 = make_phone(br7, full_session(pupils["pH"]["email"]))
            enable_fetch(page7)
            seen7 = set()
            s = open_deck(P7, page7, origin, api, aid7)
            path = "slow (6s) / failed (500) model check"
            check(s["strip"] and s["writing"], "slowfail deck opens")

            # ⊕ Mide, 4 Oct 2026 (option B) — one quiet retry, then never
            # Secured on an answer nothing checked.
            # card 1 — SLOW: the stand-in replies at 6 s; the page's first wait
            # ends at 4 s and a quiet retry starts, so the 6 s reply lands
            # inside the retry's wait and the answer IS checked.
            t0 = time.time()
            P7.type(f"it bleaches damp litmus paper white {MARK_SLOW_ONCE}")
            # The page notes its own chip 4.6 s after Check (the rig is busy
            # serving the slow reply then, so it cannot look itself).
            P7.q("(function(){setTimeout(function(){var c=document.querySelector('[data-hw=\"rate\"]') ? null : 1;"
                 "var el=document.querySelector('[data-mrb-dialog=\"flashcards\"] [data-hw=\"chip\"]');"
                 "window.__CHIP46__=el?el.textContent.trim():null;},4600);return 1;})()")
            ready_click(P7, '[data-hw="check"]')
            s_final = wait_chip(P7, page7, seen7, timeout=12.0)
            chip46 = P7.q("window.__CHIP46__ || null")
            record(path, "card1: ONE slow reply (6 s; the page waits 4 s, then retries once, quietly)",
                   f"at 4.6 s chip={chip46!r}; by {time.time()-t0:.1f}s chip={s_final['chip']!r} "
                   f"enabled={s_final['enabled']!r}",
                   "PASS" if chip46 == "Checking…" and s_final["chip"] == "Right" else "FAULT")
            ready_click(P7, '[data-hw="got_it"]' if "got_it" in (s_final.get("enabled") or []) else '[data-hw="not_yet"]')

            # card 2 — FAIL: a 500 on both attempts. No chip; all three ratings still allowed.
            s = P7.st()
            check(s["front"] == D7_CARDS[1]["question"], "card2 up")
            t0 = time.time()
            P7.type(f"a glowing splint relights {MARK_FAIL}")
            ready_click(P7, '[data-hw="check"]')
            s2 = wait_chip(P7, page7, seen7, timeout=12.0)
            ok2 = s2["chip"] is None and sorted(s2.get("enabled") or []) == ["got_it", "nearly", "not_yet"]
            record(path, "card2: a FAILED check (500 on the attempt and the retry)",
                   f"by {time.time()-t0:.1f}s chip={s2['chip']!r} enabled={s2['enabled']!r}",
                   "PASS" if ok2 else "FAULT (a failed check must not stop any rating)")
            ready_click(P7, '[data-hw="nearly"]')

            # card 3 — normal.
            s = P7.st()
            check(s["front"] == D7_CARDS[2]["question"], "card3 up")
            P7.type(D7_CARDS[2]["answer"])
            ready_click(P7, '[data-hw="check"]')
            s = wait_chip(P7, page7, seen7)
            ready_click(P7, '[data-hw="got_it"]' if hint(s) == "got_it" else '[data-hw="not_yet"]')
            settle(1.0)
            s = P7.st()
            ok3 = s.get("retryPass") == "Try again" and (s.get("end1") or "").startswith("2 of 3")
            record(path, "end of the pass: the unchecked card is left", f"end1={s.get('end1')!r} retry={s.get('retryPass')!r}",
                   "PASS" if ok3 else "FAULT")
            # Try again: card 2 comes back and gets a REAL check this time.
            ready_click(P7, '[data-hw="retry-pass"]')
            s = P7.st()
            back2 = s["front"] == D7_CARDS[1]["question"]
            P7.type("a glowing splint relights")
            ready_click(P7, '[data-hw="check"]')
            s = wait_chip(P7, page7, seen7)
            # (during Try again the strip's numbered chips share the verdict
            # chip's hook, so read the filled-in rating, not `chip`)
            ok4 = back2 and hint(s) == "got_it" and not s.get("pressed") and "got_it" in (s.get("enabled") or [])
            record(path, "card2 comes back and is really checked this time",
                   f"front was card2: {back2}; filled={s.get('pressed')!r} enabled={s['enabled']!r}",
                   "PASS" if ok4 else "FAULT")
            ready_click(P7, '[data-hw="got_it"]')
            settle(1.0)
            s = P7.st()
            record(path, "then the deck finishes", f"end1={s.get('end1')!r} done={s.get('done')!r}",
                   "PASS" if s.get("end1") == "3 of 3 secured" and s.get("done") == "Done" else "FAULT")
            P7.shot("slowfail-end")
            br7.close()
            print("session 5 (slow/fail) done")

        # ════════════════════════════════════════════════════════════
        # SESSION 6 — kill the tab mid-deck; once with a half-typed draft.
        # ════════════════════════════════════════════════════════════
        if want("killtab"):
            path = "kill tab mid-deck (resume + draft)"
            br8 = cdp.Browser().start()
            page8, P8 = make_phone(br8, full_session(pupils["pG"]["email"]))
            s = open_deck(P8, page8, origin, api, aid10)
            check(s["strip"] and s["writing"], "kill-tab deck opens")
            for i in range(4):
                s = P8.st()
                ans = next(cc["answer"] for cc in D10_CARDS if cc["question"] == s["front"])
                P8.type(ans)
                P8.click('[data-hw="check"]')
                s = wait_chip(P8, page8, set())
                P8.click('[data-hw="got_it"]' if hint(s) == "got_it" else '[data-hw="not_yet"]')
            s = P8.st()
            fifth_q = s["front"]
            br8.kill()  # hard kill: no pagehide, no beforeunload
            br9 = cdp.Browser().start()
            page9, P9b = make_phone(br9, full_session(pupils["pG"]["email"]))
            s = open_deck(P9b, page9, origin, api, aid10)
            resumed_right = s["front"] == fifth_q
            record(path, "kill after 4 full ratings, reopen",
                   f"expected card {fifth_q!r}, got {s['front']!r}, draft={s['draft']!r}",
                   "PASS" if resumed_right else "FAULT")
            P9b.shot("killtab-resume-after-4")
            br9.close()

            # second kill: mid-typing, a half-typed draft never Checked.
            br10 = cdp.Browser().start()
            page10, P10 = make_phone(br10, full_session(pupils["pG"]["email"]))
            s = open_deck(P10, page10, origin, api, aid10)
            half_draft = "mass multiplied by vel"
            P10.type(half_draft)
            settle(0.5)
            br10.kill()
            br11 = cdp.Browser().start()
            page11, P11 = make_phone(br11, full_session(pupils["pG"]["email"]))
            s = open_deck(P11, page11, origin, api, aid10)
            # A NEW Chrome profile is another device: half-typed words live on
            # the device by design (Stage D), so not carrying them is right.
            record(path, "kill mid-typing, reopen on ANOTHER device (fresh profile)",
                   f"draft after reopen={s.get('draft')!r} front={s['front']!r}",
                   "INFO (by design: drafts stay on the device that typed them)")
            br11.close()

            # ⊕ Y review — the faithful "kill the tab": the renderer dies (what
            # iOS does to a background tab), the browser and its storage live.
            br12k = cdp.Browser().start()
            page12k, P12k = make_phone(br12k, full_session(pupils["pG"]["email"]))
            s = open_deck(P12k, page12k, origin, api, aid10)
            q_before = s["front"]
            P12k.type(half_draft)
            settle(0.8)
            try:
                page12k.send("Page.crash", timeout=3)
            except Exception:
                pass
            settle(1.0)
            s = open_deck(P12k, page12k, origin, api, aid10)
            kept = s.get("draft") == half_draft and s["front"] == q_before
            record(path, "tab killed mid-typing (renderer crash, same phone), reopen",
                   f"front {q_before!r} -> {s['front']!r}; draft after reopen={s.get('draft')!r} (typed: {half_draft!r})",
                   "PASS" if kept else "FAULT (half-typed answer lost when the tab is killed)")
            P12k.shot("killtab-resume-draft")
            br12k.close()
            print("session 6 (kill tab) done")

        # ════════════════════════════════════════════════════════════
        # SESSION 7 — double-tap on every control named in the brief.
        # ════════════════════════════════════════════════════════════
        if want("doubletap"):
            path = "double-tap (two synchronous clicks) on every control"
            br12 = cdp.Browser().start()
            page12, P12 = make_phone(br12, full_session(pupils["pI"]["email"]))
            seen12 = set()

            def dbl(sel):
                return P12.q("(function(){var e=document.querySelector(%s); if(!e) return false; "
                            "e.click(); e.click(); return true;})()" % json.dumps(sel))

            s = open_deck(P12, page12, origin, api, aid9)
            check(s["strip"] and s["writing"], "doubletap deck opens")
            rows0 = fetch_reviews(c, aid9, pupils["pI"]["id"])
            P12.type(D9_CARDS[0]["answer"])
            dbl('[data-hw="check"]')
            settle(0.3)
            s = wait_chip(P12, page12, seen12)
            dbl('[data-hw="got_it"]')
            settle(0.4)
            s = P12.st()
            rows1_ = fetch_reviews(c, aid9, pupils["pI"]["id"])
            record(path, "double-click Check then double-click Secured, card1",
                   f"landed on {s['front']!r} (want card2), rows {len(rows0)}->{len(rows1_)}",
                   "PASS" if s["front"] == D9_CARDS[1]["question"] and len(rows1_) - len(rows0) == 1 else "FAULT")

            # card2 -> idk via double-click
            dbl('[data-hw="idk"]')
            s = P12.st()
            check(bool(s["learn"]), "double-click I don't know -> learn state entered once")
            P12.type("it is about half of a second maybe")
            dbl('[data-hw="check"]')
            s = wait_chip(P12, page12, seen12)
            dbl('[data-hw="nearly"]')
            settle(0.4)
            s = P12.st()
            record(path, "double-click idk, then Check, then Nearly, card2",
                   f"front after={s['front']!r}", "PASS" if s["front"] != D9_CARDS[1]["question"] else "FAULT")

            # card3 -> Wrong via double-click, then double-click Back/Forward
            P12.type("this is wrong I think")
            dbl('[data-hw="check"]')
            s = wait_chip(P12, page12, seen12)
            dbl('[data-hw="not_yet"]')
            settle(0.4)
            s = P12.st()
            front_before_bf = s["front"]
            dbl('[data-hw="back"]')
            settle(0.4)   # a real second tap comes after the redraw, never inside the same frame
            s = P12.st()
            record(path, "double-click Back moves ONE card",
                   f"before={front_before_bf!r} after={s['front']!r}",
                   "PASS" if s["front"] != front_before_bf and P12.q("!!document.querySelector('[data-hw=\"forward\"]')") else "FAULT")
            dbl('[data-hw="forward"]') if P12.q("!!document.querySelector('[data-hw=\"forward\"]')") else None
            settle(0.4)
            s = P12.st()
            record(path, "double-click Back then double-click Forward",
                   f"before={front_before_bf!r} after={s['front']!r}",
                   "PASS" if s["front"] == front_before_bf else
                   "FAULT (a double-click on Back/Forward did not land back where it started)")

            # recover robustly (not assuming a specific landing card) by
            # just answering whatever is fronted, repeatedly, until an end
            # screen appears — the double-tap finding above is recorded
            # already; this only avoids cascading unrelated failures.
            for _ in range(6):
                s = P12.st()
                if s.get("end1") is not None or not s["writing"]:
                    break
                ans_i = next((cc["answer"] for cc in D9_CARDS if cc["question"] == s["front"]), "x")
                P12.type(ans_i)
                P12.click('[data-hw="check"]')
                s = wait_chip(P12, page12, seen12)
                P12.click('[data-hw="got_it"]' if hint(s) == "got_it" else
                         ('[data-hw="nearly"]' if hint(s) == "nearly" else '[data-hw="not_yet"]'))
                settle(0.4)
            s = wait_end(P12)
            check(bool(s.get("retryPass")), "doubletap deck: leftovers end screen reached")
            dbl('[data-hw="retry-pass"]')
            settle(0.5)
            s = P12.st()
            retry_advanced_once = s["writing"]  # should land in state A on the first leftover, not skip it
            record(path, "double-click 'Try again'", f"state after={('writing' if retry_advanced_once else s)!r}",
                   "PASS" if retry_advanced_once else "FAULT")
            for _ in range(4):
                st_ = P12.st()
                if not st_["writing"]:
                    break
                f = st_["front"]
                ans = next((cc["answer"] for cc in D9_CARDS if cc["question"] == f), None)
                if ans is None:
                    break
                P12.type(ans)
                P12.click('[data-hw="check"]')
                s = wait_chip(P12, page12, seen12)
                P12.click('[data-hw="got_it"]' if hint(s) == "got_it" else
                         ('[data-hw="nearly"]' if hint(s) == "nearly" else '[data-hw="not_yet"]'))
            settle(0.8)
            s = wait_end(P12)
            if s.get("done"):
                dbl('[data-hw="done"]')
                settle(0.5)
                closed_once = not P12.st()["open"]
                record(path, "double-click 'Done'", f"overlay open after={not closed_once}",
                       "PASS" if closed_once else "FAULT")
            all_console_errors += no_fav(page12.console_errors())
            br12.close()
            print("session 7 (double-tap) done")

        # ════════════════════════════════════════════════════════════
        # SESSION 8 — two tabs on the same homework at once.
        # ════════════════════════════════════════════════════════════
        if want("twotabs"):
            path = "two tabs, same homework, same pupil"
            sess_k = full_session(pupils["pK"]["email"])
            br13 = cdp.Browser().start()
            try:
                pageA, PA = make_phone(br13, sess_k)
                tabB = new_tab(br13)
                tabB.send("Page.addScriptToEvaluateOnNewDocument", {"source": drv.FAKE_VV})
                tabB.send("Page.addScriptToEvaluateOnNewDocument", {"source": pf.session_js(ref, sess_k)})
                enable_fetch(tabB)
                PB = drv.Phone(tabB, 390, 844, 508, shots)

                sA = open_deck(PA, pageA, origin, api, aid8)
                goto_class(tabB, f"{origin}/student/class.html?api={api}#cards={aid8}")
                t0 = time.time()
                sB = PB.st()
                while time.time() - t0 < 20 and not (sB["strip"] and sB["writing"]):
                    time.sleep(0.4)
                    sB = PB.st()
                check(sA["strip"] and sA["writing"], "tab A opens the homework")
                check(sB["strip"] and sB["writing"], "tab B opens the same homework")

                # ⊕ Y review — the pupil is IN tab A (opening tab B put B in
                # front, and a hidden tab never redraws: no animation frames).
                pageA.send("Page.bringToFront")
                PA.q("(function(){window.dispatchEvent(new Event('focus'));"
                     "document.dispatchEvent(new Event('visibilitychange'));return 1;})()")
                settle(0.8)
                # tab A rates card1 right -> advances locally to card2.
                PA.type(D8_CARDS[0]["answer"])
                ready_click(PA, '[data-hw="check"]')
                sA = wait_chip(PA, pageA, set())
                ready_click(PA, '[data-hw="got_it"]')
                settle(0.5)
                c1q = by_q8[D8_CARDS[0]["question"]]
                t1 = time.time()
                while time.time() - t1 < 10 and not any(r["card_id"] == c1q and r["rating"] == "got_it"
                                                         for r in fetch_reviews(c, aid8, pupils["pK"]["id"])):
                    time.sleep(0.5)
                record(path, "tab A's Secured reaches the server before the pupil switches tabs",
                       f"after {time.time() - t1:.1f}s", "INFO")

                # ⊕ Y review — the pupil SWITCHES to tab B, as a phone does: it
                # comes to the front (visibilitychange + focus). The old version
                # typed into a tab that never came forward, which no pupil can do.
                tabB.send("Page.bringToFront")
                PB.q("(function(){window.dispatchEvent(new Event('focus'));"
                     "document.dispatchEvent(new Event('visibilitychange'));return 1;})()")
                sB = wait_front(PB, D8_CARDS[1]["question"], timeout=12)
                record(path, "secure card1 in tab A, then switch to tab B (opened earlier, on card1)",
                       f"tab B front={sB['front']!r} (card2={D8_CARDS[1]['question']!r})",
                       "PASS" if sB["front"] == D8_CARDS[1]["question"] else
                       "FAULT (the stale tab offers card1 again)")
                # tab B carries on: card2 typed wrong -> Not yet. Check is
                # enabled by the redraw that typing causes; a pupil's tap always
                # comes after it, so wait for it as a pupil would.
                PB.type("the")
                t2 = time.time()
                while time.time() - t2 < 5 and not PB.q("(function(){var b=document.querySelector('[data-hw=\"check\"]');return !!b&&!b.disabled;})()"):
                    time.sleep(0.1)
                PB.click('[data-hw="check"]')
                wait_chip(PB, tabB, set())
                ready_click(PB, '[data-hw="not_yet"]')
                settle(0.6)
                # back to tab A: it must catch up (card3, not card2 again).
                pageA.send("Page.bringToFront")
                PA.q("(function(){window.dispatchEvent(new Event('focus'));"
                     "document.dispatchEvent(new Event('visibilitychange'));return 1;})()")
                sA2 = wait_front(PA, D8_CARDS[2]["question"], timeout=12)
                rowsK = fetch_reviews(c, aid8, pupils["pK"]["id"])
                sBx = PB.st()
                record(path, "back to tab A after answering card2 in tab B",
                       f"tab A front={sA2['front']!r} (card3={D8_CARDS[2]['question']!r}); "
                       f"server rows={[r['rating'] for r in rowsK]}; tab B {sBx.get('progress')!r} draft={sBx.get('draft')!r}",
                       "PASS" if sA2["front"] == D8_CARDS[2]["question"] else
                       "FAULT (tab A is stale after tab B moved on)")
                # Server truth, as the teacher reads it.
                card1_id = by_q8[D8_CARDS[0]["question"]]
                stD, det = c.rpc(tok_t, "flashcard_pupil_detail", {"p_assignment": aid8, "p_pupil": pupils["pK"]["id"]})
                cards = (det or {}).get("cards", []) if isinstance(det, dict) else []
                c1 = next((x for x in cards if x.get("card_id") == card1_id or x.get("id") == card1_id), None)
                ok1 = bool(c1) and bool(c1.get("secured") or c1.get("known"))
                record(path, "server (teacher's pupil detail): card1 still secured after both tabs",
                       f"status={stD} card1={ {k: c1.get(k) for k in ('secured', 'known', 'last_rating')} if c1 else None }",
                       "PASS" if ok1 else "FAULT")
                PA.shot("twotabs-A-reload")
                PB.shot("twotabs-B-reload")
            finally:
                br13.close()
            print("session 8 (two tabs) done")

        # ════════════════════════════════════════════════════════════
        # TEACHER PAGES — cross-check classes.html / class-detail.html /
        # teacher/flashcards.html (progress + breakdown + CSV) against
        # each other and against DB truth, for pupil A's finished deck.
        # ════════════════════════════════════════════════════════════
        # ⊕ Y review — ‹ Back and Forward › on EVERY card of a 10-card deck,
        # then ‹ Back onto a secured card and a wrong answer there.
        if want("backwalk"):
            path = "Back and Forward on every card (10 cards)"
            brW = cdp.Browser().start()
            try:
                pageW, PW = make_phone(brW, full_session(pupils["pB"]["email"]))
                s = open_deck(PW, pageW, origin, api, aid1)
                order = []
                for i in range(9):
                    s = PW.st()
                    order.append(s["front"])
                    ans = next(cc["answer"] for cc in D1_CARDS if cc["question"] == s["front"])
                    PW.type(ans)
                    PW.click('[data-hw="check"]')
                    wait_chip(PW, pageW, set())
                    PW.click('[data-hw="got_it"]')
                    settle(0.4)
                s = PW.st()
                order.append(s["front"])
                prog0 = s["progress"]
                rows0 = fetch_reviews(c, aid1, pupils["pB"]["id"])
                back_ok, walked = True, []
                for i in range(9, 0, -1):
                    PW.click('[data-hw="back"]')
                    settle(0.4)
                    s = PW.st()
                    walked.append(s["front"])
                    if s["front"] != order[i - 1] or not s["writing"]:
                        back_ok = False
                record(path, "‹ Back from card 10 to card 1, one card a press",
                       f"{len(walked)} presses, each landed on the card before: {back_ok}; at card 1 ‹ Back offered: {s['back']}",
                       "PASS" if back_ok and not s["back"] else "FAULT")
                fwd_ok = True
                for i in range(1, 10):
                    PW.click('[data-hw="forward"]')
                    settle(0.4)
                    s = PW.st()
                    if s["front"] != order[i]:
                        fwd_ok = False
                rows1 = fetch_reviews(c, aid1, pupils["pB"]["id"])
                fwd_hidden = not PW.q("!!document.querySelector('[data-hw=\"forward\"]')")
                record(path, "Forward › from card 1 back up to card 10",
                       f"each landed on the next card: {fwd_ok}; hidden at card 10: {fwd_hidden}; "
                       f"ratings {len(rows0)}->{len(rows1)}; strip {prog0!r}->{s['progress']!r}",
                       "PASS" if fwd_ok and fwd_hidden and len(rows1) == len(rows0) and s["progress"] == prog0 else "FAULT")
                PW.shot("backwalk-at-frontier")
                # ‹ Back onto card 9 (secured) and answer it wrong.
                PW.click('[data-hw="back"]')
                settle(0.4)
                PW.type("the")
                PW.click('[data-hw="check"]')
                s = wait_chip(PW, pageW, set())
                enabled = s.get("enabled")
                PW.click('[data-hw="not_yet"]')
                settle(0.6)
                s = PW.st()
                # finish the deck: card 10, typed right.
                ans10 = next(cc["answer"] for cc in D1_CARDS if cc["question"] == order[9])
                if s["front"] == order[9]:
                    PW.type(ans10)
                    ready_click(PW, '[data-hw="check"]')
                    wait_chip(PW, pageW, set())
                    ready_click(PW, '[data-hw="got_it"]')
                    settle(1.0)
                s = PW.st()
                stD, det = c.rpc(tok_t, "flashcard_pupil_detail", {"p_assignment": aid1, "p_pupil": pupils["pB"]["id"]})
                cards = (det or {}).get("cards", []) if isinstance(det, dict) else []
                c9id = by_q1[order[8]]
                c9 = next((x for x in cards if x.get("card_id") == c9id or x.get("id") == c9id), None)
                hist = [r.get("rating") for r in (c9 or {}).get("ratings", [])]
                ok = (sorted(enabled or []) == ["got_it", "nearly", "not_yet"] and s.get("end1") == "10 of 10 secured" and s.get("done") == "Done"
                      and bool(c9) and bool(c9.get("secured")) and hist == ["got_it", "not_yet"])
                record(path, "‹ Back to a SECURED card, answered wrong (Mide 4 Oct: once secured, stays secured)",
                       f"ratings offered={enabled}; pupil end={s.get('end1')!r} {s.get('done')!r}; "
                       f"teacher card9 secured={c9.get('secured') if c9 else None}, history={hist}",
                       "PASS" if ok else "FAULT")
                PW.shot("backwalk-rerated")
            finally:
                brW.close()
            print("session backwalk done")

        if want("teacher"):
            path = "teacher pages cross-check (classes / class-detail / progress / breakdown / CSV)"
            brT = cdp.Browser().start()
            pageT, _ = make_phone(brT, full_session(teacher_email), width=1440, height=900, kb=0)

            # DB truth first.
            rows_pa = fetch_reviews(c, aid1, pupils["pA"]["id"])
            card_ids1 = list(by_q1.values())
            sec_truth = secured_from_rows(rows_pa, card_ids1)
            db_secured_n = sum(1 for v in sec_truth.values() if v)
            st_rpc, prog = c.rpc(tok_t, "flashcard_progress", {"p_assignment": aid1, "p_now": None})
            rpc_row = next((p for p in (prog.get("pupils") or []) if p["pupil_id"] == pupils["pA"]["id"]), None) \
                if st_rpc == 200 else None

            goto_class(pageT, f"{origin}/teacher/classes.html?api={api}")
            t0 = time.time()
            txt = ""
            while time.time() - t0 < 20 and "Rate of Reaction" not in txt:
                txt = pageT.eval("document.body.innerText") or ""
                time.sleep(0.5)
            got_it_scan(pageT, "teacher classes.html", scan_bucket)
            shot(pageT, shots, "teacher-classes")

            goto_class(pageT, f"{origin}/teacher/class-detail.html?class={klass}&api={api}")
            t0 = time.time()
            txt = ""
            while time.time() - t0 < 20 and "Rate of Reaction" not in txt:
                txt = pageT.eval("document.body.innerText") or ""
                time.sleep(0.5)
            got_it_scan(pageT, "teacher class-detail.html", scan_bucket)
            shot(pageT, shots, "teacher-class-detail")

            goto_class(pageT, f"{origin}/teacher/flashcards.html?assignment={aid1}&api={api}")
            t0 = time.time()
            while time.time() - t0 < 20 and pageT.eval("document.querySelectorAll('tr[data-pupil]').length") == 0:
                time.sleep(0.4)
            row = pageT.eval("(function(){var tr=document.querySelector('tr[data-pupil=\"%s\"]'); "
                            "if(!tr) return null; var n=tr.querySelector('.fp-sec-n'); "
                            "return {status: tr.getAttribute('data-status'), "
                            "secured: n ? n.childNodes[0].textContent.trim() : null};})()" % pupils["pA"]["id"])
            progress_ok = bool(row) and row.get("secured") == "10" and row.get("status") == "done"
            record(path, "progress-page row for pupil A vs DB truth",
                   f"row={row!r}; DB secured count={db_secured_n}/10; RPC row={rpc_row!r}",
                   "PASS" if progress_ok and db_secured_n == 10 else "FAULT")
            shot(pageT, shots, "teacher-progress-row")

            ok = open_panel(pageT, aid1, pupils["pA"]["id"])
            check(ok, "breakdown panel opens for pupil A")
            states = pageT.eval("Array.prototype.map.call(document.querySelectorAll('.fb-state'), "
                               "function(s){return s.textContent.trim();})")
            panel_all_secured = bool(states) and all(w == "Secured" for w in states)
            record(path, "breakdown panel per-card states vs DB truth",
                   f"panel states={states!r}", "PASS" if panel_all_secured and all(w in ALL_STATE_WORDS
                   for w in states) else "FAULT")
            phase_labels = pageT.eval("Array.prototype.map.call(document.querySelectorAll('[data-fb-phase-label]'), "
                                     "function(e){return e.textContent.trim();})")
            record(path, "breakdown panel First-try/Later-tries labels (make-mode deck)",
                   f"labels seen={set(phase_labels)!r}", "FINDING")
            got_it_scan(pageT, "teacher breakdown panel", scan_bucket)
            shot(pageT, shots, "teacher-breakdown-panel")

            csv = pageT.eval("window.__MRB_FP_LAST_CSV__ || null")
            if not csv:
                pageT.eval("var b=document.getElementById('fp-csv'); if(b) b.click();")
                settle(0.6)
                csv = pageT.eval("window.__MRB_FP_LAST_CSV__ || null")
            csv_ok = bool(csv) and "got it" not in (csv.get("text") or "").lower()
            record(path, "CSV export text", f"name={csv.get('name') if csv else None} "
                   f"len={len(csv['text']) if csv else None}", "PASS" if csv_ok else "FAULT")

            # "revised after marking" / reopen: have pupil A re-rate one
            # card via a second Revise pass (already done in session 1,
            # P9b) and see if ANYTHING on these pages reflects it.
            # ⊕ Y review — "revised after marking" lives on the teacher's PUPIL
            # screen (submission history, `[data-mrb-revised]`), not on the
            # deck's progress page. Pupil A finished the deck, then ran a
            # Revise pass (session 1): that is a revision after marking.
            _st, subs = c.select(None, "assignment_submissions",
                                 {"assignment_id": f"eq.{aid1}", "student_id": f"eq.{pupils['pA']['id']}",
                                  "select": "completed_at,updated_at"}, as_service=True)
            goto_class(pageT, f"{origin}/teacher/student-detail.html?class={klass}&student={pupils['pA']['id']}&api={api}")
            t0 = time.time()
            revised_n = 0
            while time.time() - t0 < 20:
                revised_n = pageT.eval("document.querySelectorAll('[data-mrb-revised]').length") or 0
                if revised_n:
                    break
                time.sleep(0.5)
            record(path, "teacher's pupil screen after pupil A finished the deck, then revised it",
                   f"'revised after marking' marks={revised_n}; submission={subs}",
                   "PASS" if revised_n else "FAULT (a revised deck never says so to the teacher)")
            shot(pageT, shots, "teacher-student-detail-revised")

            all_console_errors += no_fav(pageT.console_errors())
            # ⊕ Y review — the same four teacher views at phone size and in
            # dark: screenshots, no sideways scroll, no "got it".
            views = [(390, 844, "light"), (390, 844, "dark"), (1440, 900, "dark")]
            urls = [("classes", f"{origin}/teacher/classes.html?api={api}"),
                    ("class-detail", f"{origin}/teacher/class-detail.html?class={klass}&api={api}"),
                    ("progress", f"{origin}/teacher/flashcards.html?assignment={aid1}&api={api}"),
                    ("student-detail", f"{origin}/teacher/student-detail.html?class={klass}&student={pupils['pA']['id']}&api={api}")]
            for (vw, vh, vth) in views:
                pageT.send("Emulation.setDeviceMetricsOverride",
                           {"width": vw, "height": vh, "deviceScaleFactor": 2, "mobile": vw < 900})
                for (nm, u) in urls:
                    goto_class(pageT, u)
                    settle(3.0)
                    pageT.eval("document.documentElement.setAttribute('data-theme', %s)" % json.dumps(vth))
                    settle(0.5)
                    over = pageT.eval("document.documentElement.scrollWidth - window.innerWidth") or 0
                    body = (pageT.eval("document.body.innerText") or "").lower()
                    record(path, f"teacher {nm} at {vw}px {vth}",
                           f"sideways overflow={over}px; 'got it' present={'got it' in body and 'class got it' not in body}",
                           "PASS" if over <= 1 and not ('got it' in body and 'class got it' not in body) else "FAULT")
                    shot(pageT, shots, f"teacher-{nm}-{vw}-{vth}")
            brT.close()
            print("teacher pages cross-check done")

        check(not all_console_errors, "no console errors (our files) across every visited page "
              f"(got {all_console_errors[:10]!r})")
        bad_scan = [w for w, bad in scan_bucket if bad]
        check(not bad_scan, f"global scan: 'got it' never found (checked {len(scan_bucket)} pages; "
              f"bad={bad_scan!r})")

    finally:
        if site_server is not None:
            site_server.shutdown()
            site_server.server_close()
        stop_deno(deno_proc)
        stop_backend(backend_proc)
        if manifest.get("classes"):
            st, extra = c.select(None, "assignments", {"class_id": f"in.({','.join(manifest['classes'])})",
                                                        "select": "id"}, as_service=True)
            manifest["auto_assignments"] = [x["id"] for x in (extra or [])
                                            if x["id"] not in manifest.get("assignments", [])]
        json.dump(manifest, open(mpath, "w"), indent=1)
        if not a.keep:
            teardown(c, manifest)
            residue = check_residue(c, manifest)
            print("\nTEARDOWN residue check:", residue if residue else "0 rows left behind")
        else:
            print(f"\n--keep set; manifest saved to {mpath}, nothing torn down")

    print(f"\n{len(FAILS)} FAIL" if FAILS else "\nall PASS")
    for f in FAILS:
        print("  - " + f)
    print(f"\nscreenshots + manifest: {shots}")
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main())
