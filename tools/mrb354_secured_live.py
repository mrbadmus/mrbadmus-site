#!/usr/bin/env python3
"""mrb354_secured_live.py — MRB-354 Unit D, the live end-to-end proof on TEST
of "one word, and right first time is Secured" (RULE.md, Mide's ruling 2 Oct
2026): one got_it rating, in ANY phase, in ANY sitting, secures a card — no
pairing, no hour-gap-between-sittings, no completion_rule. "Got it" is gone
from every pupil/teacher surface; four states, Secured / Nearly / Not yet /
Not seen. New Forward › beside ‹ Back.

Built the same way as tools/mrb353_verdicts_live.py: a throwaway TEST world
(one teacher, one pupil, one class, one 3-card review-mode flashcard deck),
the REAL class page and teacher pages served locally, the local backend
(mrbadmus---backend) for the class page's boot reads, and the COMMITTED
`flashcard-answer-check` edge function run for real under Deno with ONLY the
model call swapped for a deterministic stand-in
(tools/mrb353_stub_model.ts — reused unedited: contains "half" -> partial,
"wrong" -> no, else match; that is everything this proof needs, so no new
stub file was required). The browser's real fetch() to
`<SUPABASE_URL>/functions/v1/flashcard-answer-check` is routed to the local
Deno server with CDP's `Fetch` domain; every other request goes to the real
network untouched.

TEST already has the MRB-354 SQL applied (flashcard_card_state's `secured`
column and flashcard_record's completion block both collapsed to the new
one-rule definition — see supabase/migrations/20261002120000_mrb354_one_word_
secured.sql, rehearsed and left APPLIED on TEST per that file's header). So
the teacher-side RPC reads (`known`) are already the new rule live, and this
script's OWN Python re-implementation of `secured()` (mirroring flashcard-
homework.js's `securedInfo()`) is used only to prove the pupil-visible UI
against ground truth in `flashcard_reviews`, never to second-guess the RPC.

The backend this script starts is a throwaway `git worktree` of the backend
repo's `origin/main` (not the long-lived local checkout, which was behind
and dirty) with its own `npm ci`'d node_modules, pointed at the main
checkout's already-TEST `.env`.

    MRB_SHOTS=/Users/midebadmus/tmp/mrb354/shots python3 tools/mrb354_secured_live.py

Exits 1 on any FAIL. TEST ONLY — the service key's own `ref` claim is
checked before any write and refused if it is not qeppkiswvclkkwbxmlok.
"""
from __future__ import annotations

import argparse
import base64
import json
import os
import re
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
import mrb351_pupil_flow_live as pf  # noqa: E402  (session_js only)
import flashcard_homework_drive as drv  # noqa: E402  (Phone, check, FAILS, FAKE_VV, settle)

check = drv.check
FAILS = drv.FAILS
settle = drv.settle

# ⚠️ NOT the long-lived local checkout (behind origin/main and carrying local
# changes — see memory "main backend checkout goes stale"). A throwaway
# `git worktree` of origin/main, `npm ci`'d fresh, its own .env copied from
# the long-lived checkout's (already TEST). Created once, outside this
# script, and left in place for inspection; nothing here deletes it.
BACKEND_DIR = "/Users/midebadmus/Documents/GitHub/mrbadmus-backend-worktrees/mrb354"
DENO = "/opt/homebrew/bin/deno"
DENO_PORT = 8000  # Deno.serve() in index.ts takes no options — hardcoded, not ours to change

DEFAULT_SHOTS = os.environ.get("MRB_SHOTS", "/Users/midebadmus/tmp/mrb354/shots")

CARDS = [
    {"question": "What is the unit of charge?", "answer": "The coulomb (C)"},
    {"question": "What is the unit of current?", "answer": "The ampere (A)"},
    {"question": "What is the unit of resistance?", "answer": "The ohm"},
]
Q1, Q2, Q3 = (c["question"] for c in CARDS)
A1, A2, A3 = (c["answer"] for c in CARDS)

# Card 2's learn-step answer and card 3's direct answer: multi-word (so
# quickCheck's client-side fast path returns null and the real network call
# to the Deno stand-in fires), and containing "half" so the stub's
# deterministic rule (tools/mrb353_stub_model.ts) answers "partial" -> Nearly.
A2_NEARLY = "it is roughly half of the ampere I think"
A3_NEARLY = "something like half an ohm maybe"
# "I don't know" cards come round once more, at the end of the SAME pass,
# as a plain card (no model answer shown) — PUPIL-FLOW's documented §13.1.4
# behaviour, not something this scenario can skip by using idk on card 2.
A2_NEARLY_REPLAY = "still roughly half of it I reckon"


def free_port() -> int:
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    p = s.getsockname()[1]
    s.close()
    return p


# ════════════════════════════════════════════════════════════════════════
# the Deno stand-in server (identical approach to tools/mrb353_verdicts_live.py)
# ════════════════════════════════════════════════════════════════════════

def write_import_map(path: str) -> None:
    model_abs = os.path.join(REPO, "supabase/functions/_shared/flashcards/model.ts")
    stub_abs = os.path.join(REPO, "tools/mrb353_stub_model.ts")
    json.dump({"imports": {f"file://{model_abs}": f"file://{stub_abs}"}}, open(path, "w"), indent=1)


def start_deno(url: str, service: str, log_dir: str, stub_log: str):
    import_map = os.path.join(REPO, "tools", "mrb354_import_map.json")
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


def stop_deno(p) -> None:
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


def enable_fetch(page) -> None:
    page.send("Fetch.enable", {"patterns": [{"urlPattern": FETCH_PATTERN}]})


def forward_to_deno(method: str, path: str, headers: dict, body: bytes):
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
        with urllib.request.urlopen(req, timeout=10) as r:
            return r.status, dict(r.headers), r.read()
    except urllib.error.HTTPError as e:
        return e.code, dict(e.headers or {}), e.read()


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
        status, resp_headers, resp_body = forward_to_deno(method, path, headers, body)
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


def wait_chip(P, page, seen, timeout=8.0):
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
# the throwaway world
# ════════════════════════════════════════════════════════════════════════

def build(c, manifest):
    ts = int(time.time())
    school, klass, year = str(uuid.uuid4()), str(uuid.uuid4()), str(uuid.uuid4())
    manifest.update({"schools": [school], "classes": [klass], "years": [year]})
    people = {}
    for key in ("t", "p"):
        email = f"mrb354-{key}-{ts}@throwaway.test"
        uid = c.admin_create_user(email, acc.THROWAWAY_PASSWORD)
        manifest.setdefault("users", []).append(uid)
        people[key] = {"id": uid, "email": email}
    manifest["people"] = people
    acc._ok("school", *c.write("schools", "POST", {"id": school, "name": f"MRB354 {ts}",
                                                     "code": f"MRB354{ts}", "kind": "school",
                                                     "key_stages_supported": ["KS3", "KS4"]}))
    today = datetime.now(timezone.utc).date()
    start = f"{today.year if today.month >= 9 else today.year - 1}-09-01"
    end = f"{int(start[:4]) + 1}-08-31"
    acc._ok("year", *c.write("academic_years", "POST", {"id": year, "school_id": school, "name": "mrb354",
                                                         "start_date": start, "end_date": end, "is_current": True}))
    acc._ok("class", *c.write("classes", "POST", {
        "id": klass, "school_id": school, "academic_year_id": year, "name": f"8v/Sc{ts % 10}",
        "key_stage": "KS3", "year_group": 8}))
    acc._ok("t", *c.write("profiles", "PATCH", {"__match__": f"id=eq.{people['t']['id']}",
        "role": "teacher", "school_id": school, "first_name": "Tvd", "last_name": "Mrb354",
        "display_name": "Tvd Mrb354", "username": f"mrb354t{ts:x}"}))
    acc._ok("p", *c.write("profiles", "PATCH", {"__match__": f"id=eq.{people['p']['id']}",
        "role": "student", "school_id": school, "first_name": "Pvd", "last_name": "Mrb354",
        "display_name": "Pvd Mrb354", "username": f"mrb354p{ts:x}",
        "science_pathway": "combined", "tier": "higher"}))
    st, subj = c.select(None, "subjects", {"select": "id,name", "name": "eq.Physics"}, as_service=True)
    acc._ok("class_teachers", *c.write("class_teachers", "POST", {
        "class_id": klass, "teacher_id": people["t"]["id"], "role": "subject_teacher",
        "subject_id": subj[0]["id"]}))
    acc._ok("class_members", *c.write("class_members", "POST", {
        "class_id": klass, "student_id": people["p"]["id"], "joined_via": "admin_added"}))
    tok_t = c.sign_in(people["t"]["email"], acc.THROWAWAY_PASSWORD)
    now = datetime.now(timezone.utc)

    st, deck = c.rpc(tok_t, "flashcard_deck_save", {
        "p_deck": None, "p_title": "Units, secured", "p_cards": CARDS,
        "p_meta": {"source_kind": "typed", "subject": "physics"}, "p_finalise": True})
    if st != 200:
        acc.die(f"deck save {st} {deck}")
    manifest.setdefault("decks", []).append(deck["deck_id"])
    st, sw = c.rpc(tok_t, "flashcard_set_work", {
        "p_class_ids": [klass], "p_deck": deck["deck_id"], "p_mode": "review", "p_rule": "secure",
        "p_title": "Units, secured", "p_release_at": (now - timedelta(minutes=1)).isoformat(),
        "p_due_at": (now + timedelta(days=5)).isoformat(), "p_note": None,
        "p_client_ref": f"mrb354-{ts}"})
    if st != 200:
        acc.die(f"set work {st} {sw}")
    manifest.setdefault("assignments", []).extend(sw["assignment_ids"])
    aid = sw["assignment_ids"][0]
    st, rows = c.select(None, "assignment_flashcards", {"assignment_id": f"eq.{aid}",
                                                         "select": "id,question,answer"}, as_service=True)
    by_q = {r["question"]: r["id"] for r in rows}
    return {"school": school, "class": klass, "people": people, "tok_t": tok_t, "aid": aid, "cards": by_q}


def teardown(c, manifest):
    aids, cls, users = manifest.get("assignments", []), manifest.get("classes", []), manifest.get("users", [])
    order = [
        ("ai_usage_events", "assignment_id", aids),
        ("flashcard_answer_verdicts", "assignment_id", aids),
        ("flashcard_reviews", "assignment_id", aids), ("flashcard_pupil_cards", "assignment_id", aids),
        ("flashcard_events", "assignment_id", aids), ("flashcard_sessions", "assignment_id", aids),
        ("assignment_submissions", "assignment_id", aids), ("assignment_flashcards", "assignment_id", aids),
        ("student_notifications", "assignment_id", aids),
        ("assignments", "id", aids),
        ("assignment_questions", "assignment_id", manifest.get("auto_assignments", [])),
        ("assignment_submissions", "assignment_id", manifest.get("auto_assignments", [])),
        ("assignments", "id", manifest.get("auto_assignments", [])),
        ("flashcard_cards", "deck_id", manifest.get("decks", [])),
        ("flashcard_decks", "id", manifest.get("decks", [])),
        ("class_members", "class_id", cls), ("class_teachers", "class_id", cls),
        ("classes", "id", cls), ("academic_years", "id", manifest.get("years", [])),
        ("ai_usage_events", "profile_id", users),
        ("audit_log", "actor_id", users), ("profiles", "id", users),
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


# ════════════════════════════════════════════════════════════════════════
# the local backend
# ════════════════════════════════════════════════════════════════════════

def start_backend(bport: int, origin: str, log_dir: str):
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
                    time.sleep(2.0)  # /api/health green != every route's DB pool warm yet
                    return p
        except Exception:
            time.sleep(0.4)
    try:
        os.killpg(p.pid, signal.SIGTERM)
    except Exception:
        pass
    raise SystemExit("backend never came up (timeout)")


def stop_backend(p) -> None:
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
# small browser-side helpers
# ════════════════════════════════════════════════════════════════════════

def shot(page, shots_dir, name):
    res = page.send("Page.captureScreenshot", {"format": "png", "fromSurface": True})
    with open(os.path.join(shots_dir, name + ".png"), "wb") as fh:
        fh.write(base64.b64decode(res["data"]))


def goto_class(page, url, tries=3):
    for i in range(tries):
        try:
            page.goto(url)
            return
        except cdp.CDPError:
            if i == tries - 1:
                raise
            time.sleep(1.5)


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
            print("  [open_deck] transient load failure, retrying…")
            time.sleep(2.0)
    print("  [open_deck] not open: %r" % (P.q("document.body.innerText") or "")[:300])
    return P.st()


def no_fav(errs):
    return [e for e in errs if "favicon.ico" not in e]


def wait_front(P, want, timeout=6.0):
    t0 = time.time()
    s = P.st()
    while time.time() - t0 < timeout and s.get("front") != want:
        time.sleep(0.2)
        s = P.st()
    return s


def wait_end(P, timeout=6.0):
    t0 = time.time()
    s = P.st()
    while time.time() - t0 < timeout and s.get("end1") is None:
        time.sleep(0.2)
        s = P.st()
    return s


def no_got_it(page, where):
    t = page.eval("document.body.innerText") or ""
    check("got it" not in t.lower(), "no 'Got it' anywhere on screen at %s" % where)


# ── teacher-side JS probes ──────────────────────────────────────────────

TEACHER_CARD_JS = r"""
(function (qText) {
  var lis = document.querySelectorAll('.fb-card');
  for (var i = 0; i < lis.length; i++) {
    var li = lis[i];
    var q = li.querySelector('[data-fb-data="question"]');
    if (q && q.textContent.trim() === qText) {
      var v = li.querySelector('.fb-verdict');
      var st = li.querySelector('.fb-state');
      var ans = li.querySelector('[data-fb-data="mine"]');
      return {
        verdict: v ? v.textContent.trim() : null,
        state: st ? st.textContent.trim() : null,
        answerText: ans ? ans.textContent.trim() : null
      };
    }
  }
  return null;
})(%s)
"""


def teacher_card_state(page, question):
    return page.eval(TEACHER_CARD_JS % json.dumps(question))


def open_panel(page, aid, pupil_id, timeout=10.0):
    page.eval("window.MRBFlashcardBreakdown.open({assignmentId: %s, studentId: %s})"
              ".then(function(){return true;}).catch(function(){return false;})"
              % (json.dumps(aid), json.dumps(pupil_id)))
    t0 = time.time()
    while time.time() - t0 < timeout:
        n = page.eval("document.querySelectorAll('.fb-card').length")
        if n:
            return True
        time.sleep(0.3)
    return False


ALL_STATE_WORDS = {"Secured", "Nearly", "Not yet", "Not seen"}


# ════════════════════════════════════════════════════════════════════════
# the pupil-side secured() reimplementation — mirrors flashcard-homework.js
# securedInfo() exactly, over the pupil's real flashcard_reviews rows, for
# asserting ground truth independent of the server RPC.
# ════════════════════════════════════════════════════════════════════════

def secured_from_rows(rows, card_ids):
    """rows: oldest-first dicts with card_id, rating, phase, session_id,
    rated_at. Returns {card_id: True/False} — any got_it, latest per
    (card_id, session_id, phase), any sitting, any phase."""
    groups = {}
    for r in rows:
        if r["card_id"] not in card_ids:
            continue
        phase = r["phase"] if r["phase"] in ("make", "review") else "review"
        key = (r.get("session_id"), phase)
        groups.setdefault(r["card_id"], {})[key] = r  # oldest-first: last write wins
    secured = {}
    for cid in card_ids:
        g = groups.get(cid, {})
        secured[cid] = any(r["rating"] == "got_it" for r in g.values())
    return secured


def fetch_reviews(c, aid, pupil_id):
    st, rows = c.select(None, "flashcard_reviews",
                        {"assignment_id": f"eq.{aid}", "pupil_id": f"eq.{pupil_id}",
                         "select": "card_id,rating,phase,session_id,rated_at,id",
                         "order": "rated_at.asc,id.asc"}, as_service=True)
    if st != 200:
        acc.die(f"fetch_reviews {st} {rows}")
    return rows


def latest_ratings(rows):
    """card_id -> (rating, rated_at) of the single latest row overall — used
    only to prove the Back/Forward dance changed nothing."""
    out = {}
    for r in rows:
        out[r["card_id"]] = (r["rating"], r["rated_at"])
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--shots", default=DEFAULT_SHOTS)
    ap.add_argument("--keep", action="store_true")
    a = ap.parse_args()

    shots = a.shots
    os.makedirs(shots, exist_ok=True)
    mpath = os.path.join(shots, "manifest.json")
    stub_log = os.path.join(shots, "stub.log")

    env = acc.read_env(acc.BACKEND_ENV_DEFAULT)
    url, service = env["SUPABASE_URL"], env["SUPABASE_SERVICE_ROLE_KEY"]
    ref = acc.jwt_ref(service)
    if ref != acc.TEST_REF:
        acc.die(f"refusing: service key ref {ref} is not TEST ({acc.TEST_REF})")
    print(f"credential ref, proven from the key payload: {ref} => TEST")
    if not os.path.isdir(BACKEND_DIR):
        acc.die(f"backend worktree missing: {BACKEND_DIR} — see the report for how it was created")
    c = acc.Client(url, acc.anon_key(), service)
    manifest = {}

    sport, bport = free_port(), free_port()
    origin = f"http://127.0.0.1:{sport}"
    api = f"http://localhost:{bport}"

    subprocess.run(["pkill", "-f", f"deno run.*{DENO_PORT}.*mrb354"], stderr=subprocess.DEVNULL)

    backend_proc = None
    deno_proc = None
    site_server = None
    all_console_errors: list[str] = []

    try:
        w = build(c, manifest)
        json.dump(manifest, open(mpath, "w"), indent=1)
        klass = w["class"]
        pupil, teacher = w["people"]["p"], w["people"]["t"]
        aid = w["aid"]
        cards = w["cards"]
        card1, card2, card3 = cards[Q1], cards[Q2], cards[Q3]

        backend_proc = start_backend(bport, origin, shots)
        print(f"backend {api} (pid {backend_proc.pid}), site {origin}")
        deno_proc = start_deno(url, service, shots, stub_log)
        print(f"deno stand-in on :{DENO_PORT} (pid {deno_proc.pid})")
        site_server, _ = cdp.serve(REPO, sport)

        def full_session(email):
            st, body = c._req("POST", f"{url}/auth/v1/token?grant_type=password",
                              {"apikey": c.anon, "Content-Type": "application/json"},
                              {"email": email, "password": acc.THROWAWAY_PASSWORD})
            if st != 200:
                acc.die(f"sign-in {email} -> {st} {body}")
            return body

        def make_phone(br, sess):
            page = br.attach()
            page.send("Emulation.setDeviceMetricsOverride",
                      {"width": 390, "height": 844, "deviceScaleFactor": 2, "mobile": True})
            page.send("Emulation.setTouchEmulationEnabled", {"enabled": True, "maxTouchPoints": 5})
            try:
                page.send("Emulation.setFocusEmulationEnabled", {"enabled": True})
            except cdp.CDPError:
                pass
            enable_fetch(page)
            page.send("Page.addScriptToEvaluateOnNewDocument", {"source": drv.FAKE_VV})
            page.send("Page.addScriptToEvaluateOnNewDocument", {"source": pf.session_js(ref, sess)})
            return page, drv.Phone(page, 390, 844, 508, shots)

        # ══════════════════════════════════════════════════════════════
        # PUPIL — card 1: Right first time (exact model answer) → Secured
        # ══════════════════════════════════════════════════════════════
        br1 = cdp.Browser().start()
        page1, P1 = make_phone(br1, full_session(pupil["email"]))
        seen1: set = set()
        s = open_deck(P1, page1, origin, api, aid)
        check(s["strip"] and s["writing"] and s["front"] == Q1,
              "pupil deck opens on card 1, state A (got %r)" % s["front"])
        no_got_it(page1, "pupil deck open")

        P1.type(A1)
        P1.click('[data-hw="check"]')
        s = wait_chip(P1, page1, seen1)
        check(s["chip"] == "Right" and s["pressed"] == ["got_it"],
              "card 1: exact model answer -> chip Right, the got_it button suggested (got %r %r)"
              % (s["chip"], s["pressed"]))
        btn_word = P1.q('document.querySelector(\'[data-hw="got_it"]\').textContent.trim()')
        check(btn_word == "Secured", "the top rating button reads 'Secured', never 'Got it' (got %r)" % btn_word)
        P1.shot("card1-right-secured")
        P1.click('[data-hw="got_it"]')
        settle(0.6)

        # proof: secured the instant one rating lands, in the SAME open
        # sitting — never a second sitting. Ground truth straight from
        # flashcard_reviews, using the exact MRB-354 rule (any got_it, any
        # phase, any sitting).
        rows_now = fetch_reviews(c, aid, pupil["id"])
        sec_now = secured_from_rows(rows_now, [card1, card2, card3])
        check(sec_now.get(card1) is True and not sec_now.get(card2) and not sec_now.get(card3),
              "card 1 secured() is True immediately after its ONE rating, in this still-open sitting "
              "(no second sitting) — got %r" % sec_now)

        # and the teacher sees it live, mid-sitting, no reload gymnastics.
        brT = cdp.Browser().start()
        pageT = brT.attach()
        pageT.send("Emulation.setDeviceMetricsOverride",
                  {"width": 1440, "height": 900, "deviceScaleFactor": 1, "mobile": False})
        pageT.send("Page.addScriptToEvaluateOnNewDocument",
                  {"source": pf.session_js(ref, full_session(teacher["email"]))})
        goto_class(pageT, f"{origin}/teacher/flashcards.html?assignment={aid}&api={api}")
        t0 = time.time()
        while time.time() - t0 < 20 and pageT.eval("!!window.MRBFlashcardBreakdown") is not True:
            time.sleep(0.3)
        ok = open_panel(pageT, aid, pupil["id"])
        check(ok, "teacher's panel opens for this pupil mid-sitting")
        st1 = teacher_card_state(pageT, Q1)
        check(bool(st1) and st1.get("state") == "Secured",
              "teacher's per-card chip for card 1 reads 'Secured' mid-sitting (got %r)" % st1)
        no_got_it(pageT, "teacher panel mid-sitting")
        brT.close()

        # ══════════════════════════════════════════════════════════════
        # PUPIL — card 2: "I don't know" → learn step → Nearly, capped
        # ══════════════════════════════════════════════════════════════
        s = P1.st()
        check(s["front"] == Q2 and s["writing"], "card 2 up, state A (got %r)" % s["front"])
        check(s["idk"], "the 'I don't know' link is offered")
        P1.click('[data-hw="idk"]')
        s = P1.st()
        check(bool(s["learn"]) and s["writing"], "'I don't know' -> the learn step: model answer shown, "
              "box open for the pupil's own words (got learn=%r)" % s["learn"])
        P1.shot("card2-learn")
        P1.type(A2_NEARLY)
        P1.click('[data-hw="check"]')
        s = wait_chip(P1, page1, seen1)
        check(s["chip"] == "Nearly" and s["pressed"] == ["nearly"],
              "card 2 learn-step answer -> chip Nearly, nearly suggested (got %r %r)" % (s["chip"], s["pressed"]))
        check("got_it" not in s["enabled"],
              "the Secured (got_it) button is DISABLED — the verdict caps the rating (enabled=%r)" % s["enabled"])
        P1.shot("card2-nearly-capped")
        P1.click('[data-hw="nearly"]')
        settle(0.6)

        # ══════════════════════════════════════════════════════════════
        # PUPIL — card 3: partial answer → Nearly; model answer shown;
        # BACK ×2 / FORWARD ×2 before rating; then rate Nearly.
        # ══════════════════════════════════════════════════════════════
        s = P1.st()
        check(s["front"] == Q3 and s["writing"], "card 3 up, state A (got %r)" % s["front"])

        # ⊕ BACK/FORWARD dance — done here, while card 3 is still in state A
        # (nothing typed, nothing rated yet): `show()` always re-opens a
        # card in state A regardless of whether it had been revealed before
        # (the documented ‹ Back behaviour — "re-opens the previous card in
        # state A"), so doing this once a verdict is showing would lose that
        # verdict's display without changing any underlying rating. Proving
        # "no rating changed" and "lands back on the same card" is exactly
        # as strong done here, since no rating exists yet either way.
        rows_before = fetch_reviews(c, aid, pupil["id"])
        latest_before = latest_ratings(rows_before)
        start_front = s["front"]

        check(P1.q("!!document.querySelector('[data-hw=\"back\"]')"), "‹ Back is offered on card 3")
        P1.click('[data-hw="back"]')
        P1.click('[data-hw="back"]')
        s = P1.st()
        check(P1.q("!!document.querySelector('[data-hw=\"forward\"]')"),
              "Forward › appears once a step back has been taken")
        P1.click('[data-hw="forward"]')
        P1.click('[data-hw="forward"]')
        s = P1.st()
        check(s["front"] == start_front and s["writing"],
              "‹ Back ×2 then Forward › ×2 lands back on the card it started on, state A (%r, got %r)"
              % (start_front, s["front"]))
        check(not P1.q("!!document.querySelector('[data-hw=\"forward\"]')"),
              "Forward › is hidden again on the newest card")

        rows_after = fetch_reviews(c, aid, pupil["id"])
        latest_after = latest_ratings(rows_after)
        check(len(rows_after) == len(rows_before) and latest_after == latest_before,
              "the Back/Forward dance changed no rating (rows %d->%d, ratings %r -> %r)"
              % (len(rows_before), len(rows_after), latest_before, latest_after))
        P1.shot("card3-back-forward-settled")

        P1.type(A3_NEARLY)
        P1.click('[data-hw="check"]')
        s = wait_chip(P1, page1, seen1)
        check(s["chip"] == "Nearly" and s["pressed"] == ["nearly"],
              "card 3 partial answer -> chip Nearly (got %r %r)" % (s["chip"], s["pressed"]))
        check(s["flipped"] == "1" and s["back_"] == A3, "the model answer is shown under the verdict (got %r)" % s["back_"])
        check("got_it" not in s["enabled"], "Secured disabled on card 3 too (enabled=%r)" % s["enabled"])
        P1.click('[data-hw="nearly"]')

        # ⊕ PUPIL-FLOW §13.1.4 — a card met with "I don't know" (card 2)
        # comes round ONCE MORE at the end of this SAME pass, as a plain
        # card (question + box, no model answer shown — it is answered from
        # memory). Only then does the pass actually end. Keep it Nearly, so
        # the end screen's "not all secured" narrative holds.
        s = P1.st()
        t0 = time.time()
        while time.time() - t0 < 6 and s.get("end1") is None and s.get("front") != Q2:
            time.sleep(0.2)
            s = P1.st()
        if s.get("end1") is None:
            check(s["front"] == Q2 and s["writing"] and not s["learn"],
                  "card 2's 'I don't know' replay: comes round once more, plain (no model answer) "
                  "(got front=%r learn=%r)" % (s["front"], s["learn"]))
            P1.type(A2_NEARLY_REPLAY)
            P1.click('[data-hw="check"]')
            s = wait_chip(P1, page1, seen1)
            check(s["chip"] == "Nearly" and s["pressed"] == ["nearly"],
                  "card 2 replay answer -> chip Nearly again (got %r %r)" % (s["chip"], s["pressed"]))
            P1.click('[data-hw="nearly"]')
        s = wait_end(P1)

        # ══════════════════════════════════════════════════════════════
        # END SCREEN — not all secured: "1 of 3 secured", ONE button
        # ══════════════════════════════════════════════════════════════
        check(s["end1"] == "1 of 3 secured", "end screen: '1 of 3 secured' (got %r)" % s["end1"])
        check(s["retryPass"] == "Try again" and s["done"] is None and s["again"] is None,
              "exactly one button, 'Try again' — no Done (retryPass=%r done=%r again=%r)"
              % (s["retryPass"], s["done"], s["again"]))
        no_got_it(page1, "end screen (1 of 3 secured)")
        P1.shot("end-1of3-try-again")

        # ══════════════════════════════════════════════════════════════
        # TRY AGAIN — only cards 2 & 3 come back; type each right -> Secured
        # ══════════════════════════════════════════════════════════════
        P1.click('[data-hw="retry-pass"]')
        s = P1.st()
        check(s["writing"] and s["front"] == Q2 and (s["draft"] in (None, "")),
              "Try again: card 2 comes back FRESH, state A, empty box (got front=%r draft=%r)"
              % (s["front"], s["draft"]))
        # ⚠️ `[data-hw="chip"]` is ambiguous during an ACTIVE retry pass: the
        # strip's own numbered to-come chips (§13.1.10) share that same
        # attribute with the verdict chip, and querySelector returns the
        # strip's (DOM order) — documented already in
        # flashcard_homework_drive.py. The suggested rating
        # (`[data-hw="rate"] button[aria-pressed]`) is unambiguous; read that.
        P1.type(A2)
        P1.click('[data-hw="check"]')
        s = wait_chip(P1, page1, seen1)
        check(s["pressed"] == ["got_it"],
              "retyped card 2 exactly right -> Secured suggested (got %r)" % s["pressed"])
        P1.click('[data-hw="got_it"]')
        s = wait_front(P1, Q3)

        check(s["writing"] and s["front"] == Q3,
              "Try again continues to card 3, state A (got %r)" % s["front"])
        P1.type(A3)
        P1.click('[data-hw="check"]')
        s = wait_chip(P1, page1, seen1)
        check(s["pressed"] == ["got_it"],
              "retyped card 3 exactly right -> Secured suggested (got %r)" % s["pressed"])
        P1.click('[data-hw="got_it"]')
        s = wait_end(P1)

        # ══════════════════════════════════════════════════════════════
        # END SCREEN — all secured: "3 of 3 secured", Done + secondary
        # ══════════════════════════════════════════════════════════════
        check(s["end1"] == "3 of 3 secured", "end screen: '3 of 3 secured' (got %r)" % s["end1"])
        check(s["done"] == "Done" and s["again"] == "Revise flashcards one more time" and s["retryPass"] is None,
              "Done (primary) + the quieter 'Revise flashcards one more time' secondary, no Try again "
              "(done=%r again=%r retryPass=%r)" % (s["done"], s["again"], s["retryPass"]))
        no_got_it(page1, "end screen (3 of 3 secured)")
        P1.shot("end-3of3-done")
        P1.click('[data-hw="done"]')
        settle(1.0)

        all_console_errors += no_fav(page1.console_errors())
        br1.close()

        # Visiting the class page lazily auto-composes this week's ordinary
        # MCQ assignment for the class (unrelated to this proof, and not
        # something MRB-354 touches) — it competes with our flashcard set
        # for "the current set" on the My classes card. Clean it up so the
        # teacher-side checks below are unambiguous about which deck they
        # are reading, scoped to this one throwaway class only.
        st_extra, extra_rows = c.select(None, "assignments", {"class_id": f"eq.{klass}", "select": "id"},
                                        as_service=True)
        auto_ids = [r["id"] for r in (extra_rows or []) if r["id"] != aid]
        if auto_ids:
            manifest.setdefault("auto_assignments", []).extend(auto_ids)
            for table, col in [("assignment_questions", "assignment_id"),
                               ("assignment_submissions", "assignment_id"),
                               ("assignments", "id")]:
                c.write(table, "DELETE", {"__match__": f"{col}=in.({','.join(auto_ids)})"})

        # ══════════════════════════════════════════════════════════════
        # DB asserts (the last flush()/submission write may trail the UI by
        # a beat, so poll briefly rather than asserting on the first read)
        # ══════════════════════════════════════════════════════════════
        t0 = time.time()
        sec_final = {}
        while time.time() - t0 < 8:
            rows_final = fetch_reviews(c, aid, pupil["id"])
            sec_final = secured_from_rows(rows_final, [card1, card2, card3])
            if all(sec_final.values()):
                break
            time.sleep(0.5)
        check(all(sec_final.values()) and set(sec_final) == {card1, card2, card3},
              "flashcard_card_state's rule over flashcard_reviews: all 3 cards secured (got %r)" % sec_final)

        t0 = time.time()
        subs = []
        while time.time() - t0 < 8:
            st_sub, subs = c.select(None, "assignment_submissions",
                                    {"assignment_id": f"eq.{aid}", "student_id": f"eq.{pupil['id']}",
                                     "select": "id,submitted_at,score,max_score"}, as_service=True)
            if st_sub == 200 and subs and subs[0].get("submitted_at"):
                break
            time.sleep(0.5)
        check(bool(subs) and subs[0].get("submitted_at"),
              "assignment_submissions row exists with submitted_at set (got %r)" % subs)

        # ══════════════════════════════════════════════════════════════
        # TEACHER — real pages, logged in as the throwaway teacher
        # ══════════════════════════════════════════════════════════════
        brT2 = cdp.Browser().start()
        pageT2 = brT2.attach()
        pageT2.send("Emulation.setDeviceMetricsOverride",
                   {"width": 390, "height": 844, "deviceScaleFactor": 2, "mobile": True})
        pageT2.send("Page.addScriptToEvaluateOnNewDocument",
                   {"source": pf.session_js(ref, full_session(teacher["email"]))})

        # My classes
        goto_class(pageT2, f"{origin}/teacher/classes.html?api={api}")
        t0 = time.time()
        txt = ""
        while time.time() - t0 < 20 and "Units, secured" not in txt:
            txt = pageT2.eval("document.body.innerText") or ""
            time.sleep(0.5)
        # `cardSecured` is filled by a SEPARATE async batch after the class
        # cards first render (loadFlashcardSecuredCounts) — give it its own
        # window rather than assuming it is already in by the time the
        # card's own title text landed.
        m = None
        t0 = time.time()
        while time.time() - t0 < 15:
            txt = pageT2.eval("document.body.innerText") or ""
            m = re.search(r"(\d+)\s+secured", txt, re.I)
            if m:
                break
            time.sleep(0.5)
        if not m:
            print("  [debug] classes.html body text:\n" + txt[:3000])
        check(bool(m) and m.group(1) == "1",
              "My classes card shows 'N secured' for the deck, N=1 (one pupil fully secured it) — got %r"
              % (m.group(0) if m else None))
        no_got_it(pageT2, "teacher My classes")
        shot(pageT2, shots, "teacher-classes-secured")

        # Class detail — the homework row shows the pupil in
        goto_class(pageT2, f"{origin}/teacher/class-detail.html?class={klass}&api={api}")
        t0 = time.time()
        txt = ""
        while time.time() - t0 < 20:
            txt = pageT2.eval("document.body.innerText") or ""
            if "Units, secured" in txt:
                break
            time.sleep(0.5)
        if "Units, secured" not in txt:
            print("  [debug] class-detail.html body text:\n" + txt[:2000])
            print("  [debug] console errors: %r" % pageT2.console_errors()[:10])
        check("Units, secured" in txt, "class-detail shows the deck's homework row (got text len %d)" % len(txt))
        no_got_it(pageT2, "teacher class-detail")
        shot(pageT2, shots, "teacher-class-detail")
        brT2.close()

        # Progress page — Done, 3/3 secured, four-state chips + legend
        brT3 = cdp.Browser().start()
        pageT3 = brT3.attach()
        pageT3.send("Emulation.setDeviceMetricsOverride",
                   {"width": 1440, "height": 900, "deviceScaleFactor": 1, "mobile": False})
        pageT3.send("Page.addScriptToEvaluateOnNewDocument",
                   {"source": pf.session_js(ref, full_session(teacher["email"]))})
        goto_class(pageT3, f"{origin}/teacher/flashcards.html?assignment={aid}&api={api}")
        t0 = time.time()
        while time.time() - t0 < 20 and pageT3.eval("document.querySelectorAll('tr[data-pupil]').length") == 0:
            time.sleep(0.4)

        legend = pageT3.eval("Array.prototype.map.call(document.querySelectorAll('.legend span'), "
                             "function(s){return s.textContent.trim();})")
        check(legend == ["Secured", "Nearly", "Not yet", "Not seen"],
              "the legend has exactly four states, in order (got %r)" % legend)

        row = pageT3.eval("(function(){var tr=document.querySelector('tr[data-pupil=\"%s\"]'); "
                          "if(!tr) return null; "
                          "var n=tr.querySelector('.fp-sec-n'); "
                          "return {status: tr.getAttribute('data-status'), "
                          "secured: n ? n.childNodes[0].textContent.trim() : null, "
                          "total: (tr.querySelector('.fp-sec-n small')||{}).textContent || null};})()"
                          % pupil["id"])
        check(bool(row) and row.get("status") == "done",
              "the pupil's row shows status Done (got %r)" % row)
        check(bool(row) and row.get("secured") == "3" and row.get("total") == "/3",
              "the pupil's Secured cell shows 3/3 (got %r)" % row)
        shot(pageT3, shots, "teacher-progress-row")

        ok = open_panel(pageT3, aid, pupil["id"])
        check(ok, "the per-pupil breakdown panel opens")
        states = pageT3.eval("Array.prototype.map.call(document.querySelectorAll('.fb-state'), "
                             "function(s){return s.textContent.trim();})")
        check(bool(states) and all(w in ALL_STATE_WORDS for w in states),
              "every per-card chip in the panel is one of the four states, never 'Got it' (got %r)" % states)
        check(all(st3 == "Secured" for st3 in states),
              "with the deck fully secured, every card's chip reads Secured (got %r)" % states)
        shot(pageT3, shots, "teacher-progress-panel")
        no_got_it(pageT3, "teacher progress page + panel")
        all_console_errors += no_fav(pageT3.console_errors())
        brT3.close()

        check(not all_console_errors,
              "no console errors from our files across the whole pupil/teacher flow (got %r)"
              % all_console_errors[:10])

    finally:
        if site_server is not None:
            site_server.shutdown()
            site_server.server_close()
        stop_deno(deno_proc)
        stop_backend(backend_proc)
        if not a.keep and manifest.get("classes"):
            st, extra = c.select(None, "assignments", {"class_id": f"in.({','.join(manifest['classes'])})",
                                                        "select": "id"}, as_service=True)
            manifest["auto_assignments"] = [x["id"] for x in (extra or []) if x["id"] not in manifest.get("assignments", [])]
            json.dump(manifest, open(mpath, "w"), indent=1)
            teardown(c, manifest)
            residue = {}
            for table, ids in (("schools", manifest.get("schools", [])), ("classes", manifest.get("classes", [])),
                               ("assignments", manifest.get("assignments", []) + manifest.get("auto_assignments", [])),
                               ("profiles", manifest.get("users", []))):
                if ids:
                    st, rows = c.select(None, table, {"id": f"in.({','.join(ids)})", "select": "id"}, as_service=True)
                    if rows:
                        residue[table] = len(rows)
            check(not residue, "teardown by snapshotted id list left nothing behind (%s)" % residue)

    print(f"\n  {len(FAILS)} failed" if FAILS else "\n  all checks passed")
    for f in FAILS:
        print("  - " + f)
    print(f"\n  screenshots: {shots}")
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main())
