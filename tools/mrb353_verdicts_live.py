#!/usr/bin/env python3
"""mrb353_verdicts_live.py — MRB-353, the live proof that THE VERDICT THE
PUPIL SAW IS THE ONE STORED (docs/mrb353 — "Checking never goes away").

Neither TEST nor this machine has an ANTHROPIC_API_KEY, so the real Claude
call cannot run. This script runs the COMMITTED `flashcard-answer-check`
edge function (supabase/functions/flashcard-answer-check/index.ts and its
shared http.ts, UNEDITED) for real, under Deno, against the REAL TEST
database — and replaces ONLY the Claude call with a deterministic stand-in
(tools/mrb353_stub_model.ts), remapped in with a Deno `--import-map`
(tools/mrb353_import_map.json, regenerated on every run from this file's own
paths). The browser's real fetch() calls to
`<SUPABASE_URL>/functions/v1/flashcard-answer-check` are routed to the local
Deno server with Chrome DevTools Protocol's `Fetch` domain — every OTHER
request (Supabase REST/RPC/Auth, the local backend, the local site) goes to
the real network untouched.

Two real throwaway pupils' flashcard homework, on the REAL class page
(student/class.html, served locally, config -> TEST by virtue of being on
127.0.0.1) and the REAL teacher's progress page (teacher/flashcards.html),
against a throwaway TEST world this script mints and tears down by a
SNAPSHOTTED ID LIST. The local backend (mrbadmus---backend, its .env is
already TEST) is started because the class page's own boot reads
(`/api/class/current-assignment`, `/api/class/practice`) 404 without it —
proved empirically before writing this script (ERR_CONNECTION_REFUSED,
"We could not load your class").

    MRB_SHOTS=/Users/midebadmus/tmp/mrb353/shots python3 tools/mrb353_verdicts_live.py

Exits 1 on any FAIL. TEST ONLY — the service key's own `ref` claim (read out
of its JWT payload, never a label beside it) is checked before any write,
and refused if it is not qeppkiswvclkkwbxmlok. Production
(urklkrwevjtlfbwnipjn) is never touched, and no SQL DDL is ever run here —
the MRB-353 migration is already applied on TEST by a separate, already-run
apply (supabase/MRB353-APPLY.md on the feat/mrb353-migrations worktree).
"""
from __future__ import annotations

import argparse
import base64
import json
import os
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
import flashcard_homework_drive as drv  # noqa: E402  (Phone, check, FAILS, FAKE_VV)

check = drv.check
FAILS = drv.FAILS

BACKEND_DIR = "/Users/midebadmus/Documents/GitHub/mrbadmus---backend"
DENO = "/opt/homebrew/bin/deno"
DENO_PORT = 8000  # Deno.serve() in index.ts takes no options — hardcoded, not ours to change
FALLBACK_NODE_MODULES = "/Users/midebadmus/Documents/GitHub/mrbadmus-backend-worktrees/experience/node_modules"

DEFAULT_SHOTS = "/Users/midebadmus/tmp/mrb353/shots"

TABLE: list[dict] = []  # the pupil-seen vs teacher-seen verdict table for the report

# ── the four decks ─────────────────────────────────────────────────────────
# MAKE deck: the writing pass types the task's own three example answers;
# the review pass (same deck, second pass) types fresh ones so the model is
# asked again rather than reusing the stored verdict.
MAKE_CARDS = [
    {"question": "What is the unit of charge?", "answer": "The coulomb (C)"},
    {"question": "What is the unit of current?", "answer": "The ampere (A)"},
    {"question": "What is the unit of resistance?", "answer": "The ohm"},
]
MAKE_WRITE = {
    "What is the unit of charge?": ("it is the coulomb", "match", "Right"),
    "What is the unit of current?": ("about half the ampere", "partial", "Nearly"),
    "What is the unit of resistance?": ("wrong guess volts", "no", "Wrong"),
}
MAKE_REVIEW = {
    "What is the unit of charge?": ("yes it's the coulomb for sure", "match", "Right"),
    "What is the unit of current?": ("roughly half an ampere", "partial", "Nearly"),
    "What is the unit of resistance?": ("nah that's wrong, volts", "no", "Wrong"),
}

# READY-MADE (review-mode) deck: one typed pass, every card.
REVIEW_CARDS = [
    {"question": "What is the unit of frequency?", "answer": "The hertz (Hz)"},
    {"question": "What is the unit of pressure?", "answer": "The pascal (Pa)"},
    {"question": "What is the unit of mass?", "answer": "The kilogram (kg)"},
]
REVIEW_ANSWERS = {
    "What is the unit of frequency?": ("it is the hertz", "match", "Right"),
    "What is the unit of pressure?": ("about half the pascal", "partial", "Nearly"),
    "What is the unit of mass?": ("wrong guess newtons", "no", "Wrong"),
}

# ORDER deck: never touched through the UI — direct RPC/HTTP only, for the
# DB-level ordering proof (E) and the batch path (F).
ORDER_CARDS = [
    {"question": "What is the unit of energy?", "answer": "The joule (J)"},
    {"question": "What is the SI unit of power?", "answer": "The watt (W)"},
    {"question": "What is the unit of time?", "answer": "The second (s)"},
]
E1_ANSWER = "it is the joule for definite"      # verdict BEFORE rating -> match
E2_ANSWER = "roughly half a watt"               # rating BEFORE verdict -> partial
E3_ANSWER = "wrong, that's hertz"               # batch path, no sync call -> no


def free_port() -> int:
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    p = s.getsockname()[1]
    s.close()
    return p


# ════════════════════════════════════════════════════════════════════════
# the Deno stand-in server
# ════════════════════════════════════════════════════════════════════════

def write_import_map(path: str) -> None:
    model_abs = os.path.join(REPO, "supabase/functions/_shared/flashcards/model.ts")
    stub_abs = os.path.join(REPO, "tools/mrb353_stub_model.ts")
    json.dump({"imports": {f"file://{model_abs}": f"file://{stub_abs}"}}, open(path, "w"), indent=1)


def start_deno(url: str, service: str, log_dir: str, stub_log: str):
    import_map = os.path.join(REPO, "tools", "mrb353_import_map.json")
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
            break  # any HTTP reply (even 4xx/5xx) means the server is up
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


# ════════════════════════════════════════════════════════════════════════
# CDP Fetch-domain interception: route *flashcard-answer-check* to Deno
# ════════════════════════════════════════════════════════════════════════

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
    """One non-blocking pass: service any Fetch.requestPaused events already
    buffered or waiting on the socket, by forwarding to the local Deno
    server and fulfilling with its real response. Returns the count serviced."""
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
            pass  # the request may already be gone (navigation, abort)
        n += 1
    return n


def wait_chip(P, page, seen, timeout=6.0):
    """Drive the pump while polling the pupil page's own chip state."""
    t0 = time.time()
    s = P.st()
    while time.time() - t0 < timeout:
        pump_fetch_once(page, seen)
        s = P.st()
        if s["chip"] != "Checking…":
            return s
        time.sleep(0.12)
    return s


def wait_batch(page, seen, timeout=16.0):
    t0 = time.time()
    serviced = 0
    while time.time() - t0 < timeout:
        serviced += pump_fetch_once(page, seen)
        time.sleep(0.2)
    return serviced


# ════════════════════════════════════════════════════════════════════════
# the throwaway world
# ════════════════════════════════════════════════════════════════════════

def build(c, manifest, label):
    ts = int(time.time())
    school, klass, year = str(uuid.uuid4()), str(uuid.uuid4()), str(uuid.uuid4())
    manifest.update({"schools": [school], "classes": [klass], "years": [year]})
    people = {}
    for key in ("t", "p"):
        email = f"mrb353-{key}-{label}-{ts}@throwaway.test"
        uid = c.admin_create_user(email, acc.THROWAWAY_PASSWORD)
        manifest.setdefault("users", []).append(uid)
        people[key] = {"id": uid, "email": email}
    manifest["people"] = people
    acc._ok("school", *c.write("schools", "POST", {"id": school, "name": f"MRB353 {ts}",
                                                     "code": f"MRB353{ts}", "kind": "school",
                                                     "key_stages_supported": ["KS3", "KS4"]}))
    today = datetime.now(timezone.utc).date()
    start = f"{today.year if today.month >= 9 else today.year - 1}-09-01"
    end = f"{int(start[:4]) + 1}-08-31"
    acc._ok("year", *c.write("academic_years", "POST", {"id": year, "school_id": school, "name": "mrb353",
                                                         "start_date": start, "end_date": end, "is_current": True}))
    acc._ok("class", *c.write("classes", "POST", {
        "id": klass, "school_id": school, "academic_year_id": year, "name": f"8v/Sc{ts % 10}",
        "key_stage": "KS3", "year_group": 8}))
    acc._ok("t", *c.write("profiles", "PATCH", {"__match__": f"id=eq.{people['t']['id']}",
        "role": "teacher", "school_id": school, "first_name": "Tvd", "last_name": "Mrb353",
        "display_name": "Tvd Mrb353", "username": f"mrb353t{ts:x}"}))
    acc._ok("p", *c.write("profiles", "PATCH", {"__match__": f"id=eq.{people['p']['id']}",
        "role": "student", "school_id": school, "first_name": "Pvd", "last_name": "Mrb353",
        "display_name": "Pvd Mrb353", "username": f"mrb353p{ts:x}",
        "science_pathway": "combined", "tier": "higher"}))
    st, subj = c.select(None, "subjects", {"select": "id,name", "name": "eq.Physics"}, as_service=True)
    acc._ok("class_teachers", *c.write("class_teachers", "POST", {
        "class_id": klass, "teacher_id": people["t"]["id"], "role": "subject_teacher",
        "subject_id": subj[0]["id"]}))
    acc._ok("class_members", *c.write("class_members", "POST", {
        "class_id": klass, "student_id": people["p"]["id"], "joined_via": "admin_added"}))
    tok_t = c.sign_in(people["t"]["email"], acc.THROWAWAY_PASSWORD)
    now = datetime.now(timezone.utc)

    def set_deck(title, cards, mode, ref):
        st, deck = c.rpc(tok_t, "flashcard_deck_save", {
            "p_deck": None, "p_title": title, "p_cards": cards,
            "p_meta": {"source_kind": "typed", "subject": "physics"}, "p_finalise": True})
        if st != 200:
            acc.die(f"deck save {st} {deck}")
        manifest.setdefault("decks", []).append(deck["deck_id"])
        st, sw = c.rpc(tok_t, "flashcard_set_work", {
            "p_class_ids": [klass], "p_deck": deck["deck_id"], "p_mode": mode, "p_rule": "secure",
            "p_title": title, "p_release_at": (now - timedelta(minutes=1)).isoformat(),
            "p_due_at": (now + timedelta(days=5)).isoformat(), "p_note": None,
            "p_client_ref": f"mrb353-{ref}-{ts}"})
        if st != 200:
            acc.die(f"set work {st} {sw}")
        manifest.setdefault("assignments", []).extend(sw["assignment_ids"])
        aid = sw["assignment_ids"][0]
        st, rows = c.select(None, "assignment_flashcards", {"assignment_id": f"eq.{aid}",
                                                             "select": "id,question,answer"}, as_service=True)
        by_q = {r["question"]: r["id"] for r in rows}
        return aid, by_q

    aid_make, cards_make = set_deck("Units, make", MAKE_CARDS, "make", "make")
    aid_review, cards_review = set_deck("Units, review", REVIEW_CARDS, "review", "review")
    aid_order, cards_order = set_deck("Units, order", ORDER_CARDS, "review", "order")
    return {"school": school, "class": klass, "people": people, "tok_t": tok_t,
            "aid_make": aid_make, "cards_make": cards_make,
            "aid_review": aid_review, "cards_review": cards_review,
            "aid_order": aid_order, "cards_order": cards_order}


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
# the local backend (the class page's boot reads need it — proved empirically)
# ════════════════════════════════════════════════════════════════════════

def start_backend(bport: int, origin: str, log_dir: str):
    env = acc.read_env(acc.BACKEND_ENV_DEFAULT)
    base_env = dict(os.environ)
    for k, v in env.items():
        base_env[k] = v
    base_env["PORT"] = str(bport)
    base_env["EXTRA_CORS_ORIGINS"] = origin

    def try_start(extra_env):
        e = dict(base_env)
        e.update(extra_env)
        logf = open(os.path.join(log_dir, "backend.log"), "w")
        p = subprocess.Popen(["node", "server.js"], cwd=BACKEND_DIR, env=e,
                             stdout=logf, stderr=subprocess.STDOUT, start_new_session=True)
        api = f"http://localhost:{bport}"
        deadline = time.time() + 30
        while time.time() < deadline:
            if p.poll() is not None:
                return None, open(os.path.join(log_dir, "backend.log")).read()[-2000:]
            try:
                with urllib.request.urlopen(api + "/api/health", timeout=2) as r:
                    if r.status == 200:
                        return p, None
            except Exception:
                time.sleep(0.4)
        try:
            os.killpg(p.pid, signal.SIGTERM)
        except Exception:
            pass
        return None, "timed out waiting for /api/health"

    p, err = try_start({})
    if p is None and os.path.isdir(FALLBACK_NODE_MODULES):
        print(f"  [backend] own node_modules failed ({err}); retrying with NODE_PATH fallback")
        p, err = try_start({"NODE_PATH": FALLBACK_NODE_MODULES})
    if p is None:
        raise SystemExit("backend never came up: " + str(err))
    time.sleep(2.0)  # /api/health green != every route's DB pool warm yet
    return p


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


TEACHER_CARD_JS = r"""
(function (qText) {
  var lis = document.querySelectorAll('.fb-card');
  for (var i = 0; i < lis.length; i++) {
    var li = lis[i];
    var q = li.querySelector('[data-fb-data="question"]');
    if (q && q.textContent.trim() === qText) {
      var v = li.querySelector('.fb-verdict');
      var ans = li.querySelector('[data-fb-data="mine"]');
      var phases = li.querySelectorAll('.fb-phase');
      return {
        verdict: v ? v.textContent.trim() : null,
        check: v ? v.getAttribute('data-check') : null,
        answerText: ans ? ans.textContent.trim() : null,
        phaseLabels: Array.prototype.map.call(phases, function (p) { return p.textContent.trim(); })
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


def open_history(page):
    page.eval("Array.prototype.forEach.call(document.querySelectorAll('.fb-history'), "
              "function(d){ d.open = true; })")


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


def answer_card(P, page, seen, answer, timeout=6.0):
    """Type an answer, Check, service the real network call to the local
    Deno stand-in, and wait for the chip. Returns the drive state at the
    moment the chip resolved (or timed out)."""
    P.type(answer)
    P.click('[data-hw="check"]')
    s = wait_chip(P, page, seen, timeout=timeout)
    return s


def rate_shown(P):
    # ⊕ 5 Oct 2026 — the pupil decides: nothing is pre-filled and all three
    # ratings are always enabled. This pupil simply follows the hint chip.
    s = P.st()
    # ⊕ 8 Oct 2026 — Nearly and Not yet are always open; Secured needs a real
    # attempt (a guess that shares no word with the model answer greys it).
    check({"nearly", "not_yet"} <= set(s["enabled"]) and not s["pressed"],
          "the verdict is only a hint: Nearly and Not yet enabled, none filled (got %r %r)" % (s["enabled"], s["pressed"]))
    rating = {"Right": "got_it", "Nearly": "nearly"}.get(s["chip"], "not_yet")
    P.click('[data-hw="%s"]' % rating)
    time.sleep(0.3)


def drive_pass(P, page, seen, answer_map, tag, on_first=None, upto=10):
    """Drive every card of the pass currently on screen, keyed by the
    question actually shown (never an assumed authoring order — the deck's
    own card order is not this script's to assume)."""
    n = 0
    while n < upto:
        s = P.st()
        if not s["writing"]:
            break
        front = s["front"]
        if front not in answer_map:
            check(False, "%s: unexpected card on screen (%r)" % (tag, front))
            break
        answer, _want_verdict, want_chip = answer_map[front]
        s2 = answer_card(P, page, seen, answer)
        check(s2["chip"] == want_chip,
              "B: %s card %r (%r) -> chip %r (got %r)" % (tag, front, answer, want_chip, s2["chip"]))
        TABLE.append({"deck": tag, "card": front, "answer": answer, "pupil_chip": s2["chip"], "want": want_chip})
        if n == 0 and on_first:
            on_first()
        rate_shown(P)
        n += 1
    return n


def no_fav(errs):
    return [e for e in errs if "favicon.ico" not in e]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--shots", default=os.environ.get("MRB_SHOTS", DEFAULT_SHOTS))
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
    c = acc.Client(url, acc.anon_key(), service)
    manifest = {}

    sport, bport = free_port(), free_port()
    origin = f"http://127.0.0.1:{sport}"
    api = f"http://localhost:{bport}"

    subprocess.run(["pkill", "-f", f"deno run.*{DENO_PORT}.*mrb353"], stderr=subprocess.DEVNULL)

    backend_proc = None
    deno_proc = None
    site_server = None
    all_console_errors: list[str] = []

    try:
        w = build(c, manifest, "run")
        json.dump(manifest, open(mpath, "w"), indent=1)
        klass = w["class"]
        tok_t = w["tok_t"]
        pupil = w["people"]["p"]
        teacher = w["people"]["t"]
        aid_make, cards_make = w["aid_make"], w["cards_make"]
        aid_review, cards_review = w["aid_review"], w["cards_review"]
        aid_order, cards_order = w["aid_order"], w["cards_order"]

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

        # ══ A/B/C/D — MAKE deck ════════════════════════════════════════════
        br1 = cdp.Browser().start()
        page1, P1 = make_phone(br1, full_session(pupil["email"]))
        seen1: set = set()
        s = open_deck(P1, page1, origin, api, aid_make)
        check(s["strip"] and s["writing"], "A: the MAKE deck opens on the writing pass")

        order_q = [c["question"] for c in MAKE_CARDS]

        # writing pass — all three cards, the task's own example answers,
        # each forcing the model path (no local quick-check decision)
        n1 = drive_pass(P1, page1, seen1, MAKE_WRITE, "make/writing")
        check(n1 == 3, "B: writing pass answered all 3 cards (got %d)" % n1)
        shot(page1, shots, "pupil-make-writing-01")
        t0 = time.time()
        while time.time() - t0 < 10 and P1.st()["again"] is None:
            time.sleep(0.3)
        s = P1.st()
        check(s["again"] is not None, "writing pass reached its end screen (got %r)" % s["again"])
        P1.click('[data-hw="again"]')
        time.sleep(0.6)

        # review pass — same three cards, fresh ambiguous answers
        def shot_both_viewports():
            shot(page1, shots, "pupil-verdict-chip-390x844")
            page1.send("Emulation.setDeviceMetricsOverride",
                      {"width": 1440, "height": 900, "deviceScaleFactor": 1, "mobile": False})
            time.sleep(0.3)
            shot(page1, shots, "pupil-verdict-chip-1440x900")
            page1.send("Emulation.setDeviceMetricsOverride",
                      {"width": 390, "height": 844, "deviceScaleFactor": 2, "mobile": True})
            time.sleep(0.3)

        n2 = drive_pass(P1, page1, seen1, MAKE_REVIEW, "make/review", on_first=shot_both_viewports)
        check(n2 == 3, "B: review pass answered all 3 cards (got %d)" % n2)
        t0 = time.time()
        while time.time() - t0 < 10 and P1.st()["done"] is None:
            time.sleep(0.3)
        s = P1.st()
        # This pupil follows the hint, so Wrong/Nearly cards are rated below
        # Secured and the pass does not end on Done — by the pupil's choice,
        # not because anything stopped them (the buttons were all enabled).
        check(s["done"] != "Done", "make deck: a pupil who rates Wrong/Nearly cards lower does NOT end on Done "
              "(got %r)" % s["done"])

        all_console_errors += no_fav(page1.console_errors())
        br1.close()

        # ══ A/B — READY-MADE (review) deck ══════════════════════════════════
        br2 = cdp.Browser().start()
        page2, P2 = make_phone(br2, full_session(pupil["email"]))
        seen2: set = set()
        s = open_deck(P2, page2, origin, api, aid_review)
        check(s["strip"] and s["writing"], "A: the READY-MADE deck opens with a typed pass (review mode)")
        n3 = drive_pass(P2, page2, seen2, REVIEW_ANSWERS, "ready-made")
        check(n3 == 3, "B: ready-made deck answered all 3 cards (got %d)" % n3)
        t0 = time.time()
        while time.time() - t0 < 10 and P2.st()["done"] is None:
            time.sleep(0.3)
        s = P2.st()
        check(s["done"] != "Done", "ready-made deck: a pupil who rates Wrong/Nearly cards lower does NOT end on Done "
              "(got %r)" % s["done"])
        shot(page2, shots, "pupil-ready-made-done")
        all_console_errors += no_fav(page2.console_errors())
        br2.close()

        # ══ C — the teacher sees the SAME verdict, within seconds ══════════
        # ⚠️ Fetch interception is enabled ONLY for the ORDER deck's teacher
        # page below (check F) — that is the one page whose automatic
        # kickAnswerCheck() batch call this proof needs serviced. The MAKE
        # and READY-MADE teacher pages below also fire that same call once on
        # load, but by then every review row of theirs already has a verdict
        # (the sync path resolved it during the UI drive above), so it hits
        # the REAL TEST edge function harmlessly (no pending rows; and TEST
        # has no ANTHROPIC_API_KEY of its own either). Enabling interception
        # there too with nothing ever servicing it would leave that one
        # paused request hanging for the life of the page — avoided by simply
        # not enabling the domain where this proof does not need it.
        def teacher_browser(width, height, mobile, fetch=False):
            br = cdp.Browser().start()
            page = br.attach()
            page.send("Emulation.setDeviceMetricsOverride",
                      {"width": width, "height": height, "deviceScaleFactor": 1, "mobile": mobile})
            if fetch:
                enable_fetch(page)
            page.send("Page.addScriptToEvaluateOnNewDocument",
                      {"source": pf.session_js(ref, full_session(teacher["email"]))})
            return br, page

        brT1, pageT1 = teacher_browser(1440, 900, False)
        goto_class(pageT1, f"{origin}/teacher/flashcards.html?assignment={aid_make}&api={api}")
        t0 = time.time()
        while time.time() - t0 < 20 and pageT1.eval("!!window.MRBFlashcardBreakdown") is not True:
            time.sleep(0.3)
        ok = open_panel(pageT1, aid_make, pupil["id"])
        check(ok, "C: teacher's panel opens for the MAKE deck's pupil")
        for qtext in order_q:
            want_chip = MAKE_REVIEW[qtext][2]
            t0 = time.time()
            st_card = teacher_card_state(pageT1, qtext)
            saw_checking = bool(st_card) and st_card.get("verdict") == "Checking"
            while time.time() - t0 < 10 and (not st_card or st_card.get("verdict") in (None, "Checking")):
                time.sleep(0.8)
                open_panel(pageT1, aid_make, pupil["id"])
                st_card = teacher_card_state(pageT1, qtext)
                saw_checking = saw_checking or (bool(st_card) and st_card.get("verdict") == "Checking")
            check(not saw_checking, "C: the teacher never saw 'Checking' on %r" % qtext)
            check(bool(st_card) and st_card.get("verdict") == want_chip,
                  "C: teacher sees %r on the MAKE deck card %r (pupil saw %r)"
                  % (st_card.get("verdict") if st_card else None, qtext, want_chip))
            for row in TABLE:
                if row["deck"] == "make/review" and row["card"] == qtext:
                    row["teacher_chip"] = st_card.get("verdict") if st_card else None
            st_r, rows_r = c.select(None, "flashcard_reviews",
                                    {"assignment_id": f"eq.{aid_make}", "card_id": f"eq.{cards_make[qtext]}",
                                     "pupil_id": f"eq.{pupil['id']}", "phase": "eq.review",
                                     "select": "answer,answer_check", "order": "rated_at.desc", "limit": "1"},
                                    as_service=True)
            db_verdict = rows_r[0]["answer_check"] if rows_r else None
            check(st_r == 200 and rows_r and rows_r[0]["answer_check"] == {"Right": "match", "Nearly": "partial",
                                                                            "Wrong": "no"}[want_chip],
                  "C(db): flashcard_reviews.answer_check for %r is %r (got %r)"
                  % (qtext, {"Right": "match", "Nearly": "partial", "Wrong": "no"}[want_chip], db_verdict))
            for row in TABLE:
                if row["deck"] == "make/review" and row["card"] == qtext:
                    row["db_verdict"] = db_verdict
            st_v, rows_v = c.select(None, "flashcard_answer_verdicts",
                                    {"assignment_id": f"eq.{aid_make}", "card_id": f"eq.{cards_make[qtext]}",
                                     "pupil_id": f"eq.{pupil['id']}", "answer": f"eq.{MAKE_REVIEW[qtext][0]}"},
                                    as_service=True)
            check(st_v == 200 and bool(rows_v), "C(db): flashcard_answer_verdicts has the row for %r" % qtext)

        # D — History labels on the MAKE deck's first card
        open_history(pageT1)
        shot(pageT1, shots, "teacher-make-history-1440x900")
        d1 = teacher_card_state(pageT1, order_q[0])
        check(bool(d1) and d1.get("phaseLabels") == ["First try", "Later tries"],
              "D: make deck card 1 History shows 'First try' / 'Later tries' (got %r)"
              % (d1.get("phaseLabels") if d1 else None))
        pageT1.send("Emulation.setDeviceMetricsOverride",
                   {"width": 390, "height": 844, "deviceScaleFactor": 2, "mobile": True})
        time.sleep(0.3)
        shot(pageT1, shots, "teacher-make-history-390x844")
        all_console_errors += no_fav(pageT1.console_errors())
        brT1.close()

        brT2, pageT2 = teacher_browser(1440, 900, False)
        goto_class(pageT2, f"{origin}/teacher/flashcards.html?assignment={aid_review}&api={api}")
        t0 = time.time()
        while time.time() - t0 < 20 and pageT2.eval("!!window.MRBFlashcardBreakdown") is not True:
            time.sleep(0.3)
        ok = open_panel(pageT2, aid_review, pupil["id"])
        check(ok, "C: teacher's panel opens for the READY-MADE deck's pupil")
        qtext0 = REVIEW_CARDS[0]["question"]
        for qq in [cd["question"] for cd in REVIEW_CARDS]:
            want = REVIEW_ANSWERS[qq][2]
            t0 = time.time()
            st_card = teacher_card_state(pageT2, qq)
            saw_checking = bool(st_card) and st_card.get("verdict") == "Checking"
            while time.time() - t0 < 10 and (not st_card or st_card.get("verdict") in (None, "Checking")):
                time.sleep(0.8)
                open_panel(pageT2, aid_review, pupil["id"])
                st_card = teacher_card_state(pageT2, qq)
                saw_checking = saw_checking or (bool(st_card) and st_card.get("verdict") == "Checking")
            check(not saw_checking, "C: the teacher never saw 'Checking' on %r" % qq)
            check(bool(st_card) and st_card.get("verdict") == want,
                  "C: teacher sees %r on the READY-MADE deck card %r (pupil saw %r)"
                  % (st_card.get("verdict") if st_card else None, qq, want))
            for row in TABLE:
                if row["deck"] == "ready-made" and row["card"] == qq:
                    row["teacher_chip"] = st_card.get("verdict") if st_card else None
            st_r, rows_r = c.select(None, "flashcard_reviews",
                                    {"assignment_id": f"eq.{aid_review}", "pupil_id": f"eq.{pupil['id']}",
                                     "answer": f"eq.{REVIEW_ANSWERS[qq][0]}",
                                     "select": "answer,answer_check", "limit": "1"}, as_service=True)
            want_db = {"Right": "match", "Nearly": "partial", "Wrong": "no"}[want]
            got_db = rows_r[0]["answer_check"] if (st_r == 200 and rows_r) else None
            check(got_db == want_db, "C(db): ready-made flashcard_reviews.answer_check for %r is %r (got %r)"
                  % (qq, want_db, got_db))
            for row in TABLE:
                if row["deck"] == "ready-made" and row["card"] == qq:
                    row["db_verdict"] = got_db

        open_history(pageT2)
        shot(pageT2, shots, "teacher-ready-made-1440x900")
        d2 = teacher_card_state(pageT2, qtext0)
        check(bool(d2) and d2.get("phaseLabels") == [],
              "D: ready-made deck card has NO .fb-phase label (got %r)" % (d2.get("phaseLabels") if d2 else None))
        pageT2.send("Emulation.setDeviceMetricsOverride",
                   {"width": 390, "height": 844, "deviceScaleFactor": 2, "mobile": True})
        time.sleep(0.3)
        shot(pageT2, shots, "teacher-ready-made-390x844")
        all_console_errors += no_fav(pageT2.console_errors())
        brT2.close()

        # ══ E — ordering, at the DB level, no UI ════════════════════════════
        tok_p = c.sign_in(pupil["email"], acc.THROWAWAY_PASSWORD)
        anon = c.anon

        def sync_call(card_id, answer):
            body = json.dumps({"assignment_id": aid_order, "card_id": card_id, "pupil_answer": answer}).encode()
            req = urllib.request.Request(f"http://127.0.0.1:{DENO_PORT}/", data=body, method="POST",
                                         headers={"Content-Type": "application/json",
                                                  "Authorization": f"Bearer {tok_p}", "apikey": anon})
            with urllib.request.urlopen(req, timeout=10) as r:
                return r.status, json.loads(r.read())

        def record_review(card_id, answer, rating="got_it"):
            t0 = datetime.now(timezone.utc)
            events = [
                {"id": str(uuid.uuid4()), "type": "card_shown", "at": t0.isoformat(), "card": card_id, "phase": "review"},
                {"id": str(uuid.uuid4()), "type": "answer_submitted",
                 "at": (t0 + timedelta(seconds=1)).isoformat(), "card": card_id, "phase": "review", "answer": answer},
                {"id": str(uuid.uuid4()), "type": "revealed",
                 "at": (t0 + timedelta(seconds=2)).isoformat(), "card": card_id, "phase": "review"},
                {"id": str(uuid.uuid4()), "type": "rated",
                 "at": (t0 + timedelta(seconds=3)).isoformat(), "card": card_id, "phase": "review", "rating": rating},
            ]
            return c.rpc(tok_p, "flashcard_record", {"p_assignment": aid_order, "p_events": events})

        def review_row(card_id):
            st, rows = c.select(None, "flashcard_reviews",
                                {"assignment_id": f"eq.{aid_order}", "card_id": f"eq.{card_id}",
                                 "pupil_id": f"eq.{pupil['id']}", "phase": "eq.review",
                                 "select": "answer,answer_check", "order": "rated_at.desc", "limit": "1"},
                                as_service=True)
            return rows[0] if (st == 200 and rows) else None

        q_e1, q_e2, q_e3 = (c["question"] for c in ORDER_CARDS)
        card_e1, card_e2, card_e3 = cards_order[q_e1], cards_order[q_e2], cards_order[q_e3]

        # (i) verdict BEFORE rating
        st_sync, body_sync = sync_call(card_e1, E1_ANSWER)
        check(st_sync == 200 and body_sync.get("verdict") == "match",
              "E(i): direct sync call for %r -> match (got %r)" % (E1_ANSWER, body_sync))
        st_rec, body_rec = record_review(card_e1, E1_ANSWER, "got_it")
        check(st_rec == 200, "E(i): flashcard_record (events only) for the same answer -> 200 (got %r %r)"
              % (st_rec, body_rec))
        row = review_row(card_e1)
        check(bool(row) and row["answer_check"] == "match" and row["answer"] == E1_ANSWER,
              "E(i): the review row is BORN with the verdict, never pending (got %r)" % row)

        # (ii) rating BEFORE verdict
        st_rec2, body_rec2 = record_review(card_e2, E2_ANSWER, "nearly")
        check(st_rec2 == 200, "E(ii): flashcard_record (events only) for %r -> 200" % E2_ANSWER)
        row2a = review_row(card_e2)
        check(bool(row2a) and row2a["answer_check"] == "pending",
              "E(ii): the review row is PENDING before the sync call (got %r)" % row2a)
        st_sync2, body_sync2 = sync_call(card_e2, E2_ANSWER)
        check(st_sync2 == 200 and body_sync2.get("verdict") == "partial",
              "E(ii): direct sync call for %r -> partial (got %r)" % (E2_ANSWER, body_sync2))
        row2b = review_row(card_e2)
        check(bool(row2b) and row2b["answer_check"] == "partial",
              "E(ii): the review row FLIPS from pending to the verdict (got %r)" % row2b)

        # ══ F — the batch path (the backfill route) ═════════════════════════
        st_rec3, body_rec3 = record_review(card_e3, E3_ANSWER, "not_yet")
        check(st_rec3 == 200, "F: flashcard_record (events only) for %r -> 200" % E3_ANSWER)
        row3a = review_row(card_e3)
        check(bool(row3a) and row3a["answer_check"] == "pending",
              "F: the review row is PENDING before any check (got %r)" % row3a)

        brT3, pageT3 = teacher_browser(1440, 900, False, fetch=True)
        goto_class(pageT3, f"{origin}/teacher/flashcards.html?assignment={aid_order}&api={api}")
        seen3: set = set()
        t0 = time.time()
        serviced = 0
        row3b = row3a
        while time.time() - t0 < 16 and (not row3b or row3b["answer_check"] == "pending"):
            serviced += pump_fetch_once(pageT3, seen3)
            time.sleep(0.3)
            row3b = review_row(card_e3)
        check(bool(row3b) and row3b["answer_check"] == "no",
              "F: within ~15s of the teacher's progress page loading, the batch call checks it -> no (got %r)" % row3b)
        check(serviced >= 1, "F: the batch call to flashcard-answer-check was intercepted and served (%d)" % serviced)
        all_console_errors += no_fav(pageT3.console_errors())
        brT3.close()

        if os.path.exists(stub_log):
            lines = [json.loads(l) for l in open(stub_log) if l.strip()]
            asked_e3 = [l for l in lines if l.get("pupil_answer") == E3_ANSWER]
            check(len(asked_e3) == 1,
                  "F: the stub model log shows %r asked exactly once (got %d)" % (E3_ANSWER, len(asked_e3)))
        else:
            check(False, "F: stub log file missing — cannot prove the model step ran")

        # ══ G — nothing else regressed visibly ══════════════════════════════
        check(not all_console_errors,
              "G: no console errors from our files across the whole pupil/teacher flow (got %r)"
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

    print("\n── pupil-seen vs teacher-seen ──")
    for row in TABLE:
        print("  %-14s %-45s %-30s pupil=%-6s teacher=%-6s db=%s"
              % (row["deck"], row["card"][:45], row["answer"][:30], row.get("pupil_chip"),
                 row.get("teacher_chip", "-"), row.get("db_verdict", "-")))

    print(f"\n  {len(FAILS)} failed" if FAILS else "\n  all checks passed")
    for f in FAILS:
        print("  - " + f)
    print(f"\n  screenshots: {shots}")
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main())
