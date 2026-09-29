#!/usr/bin/env python3
"""flashcards_stage_d_live.py — Stage D1's LIVE proof on TEST
(docs/mrb351/STAGE-D-PLAN.md §2.9): progress is never lost, and nothing jumps.

A throwaway pupil does a REVIEW-mode deck of ten cards on the REAL class page
(student/class.html served locally; config -> TEST; the backend run from the
backend worktree on a free port, reached through the page's localhost-only
`?api=` override) against the REAL TEST database. Nothing is stubbed.

  1  390x844 phone, profile A: 3 cards (right, wrong, right), ×, reopen →
     card 4 at "2 of 10 right" with ‹ Back. DB: 3 review rows, 1 sitting, ended.
  2  card 4 right, then Chrome is SIGKILLed (no pagehide, no beforeunload —
     a phone that died). A NEW Chrome with a fresh profile (another device),
     signed in again → card 5 at "3 of 10 right".
  3  offline (CDP network emulation): card 5 right → SAVED ON THIS PHONE;
     online; reload → the queue goes first → card 6 at "4 of 10 right".
  4  cards 6–10 with 2 wrong → Try again "7 of 10 right"; × ; reopen → the
     same screen; Try again → chips, queue of 3; one right; × ; reopen →
     chips, queue of 2, "8 of 10 right". Every rating and sitting moved back
     61 minutes (service role) → reopen → a new pass "0 of 10 right".
  5  1440x900 desktop (mobile:false): the class page, the deck's row clicked,
     the deck opened, the answer box focused — scrollY, the row, the page
     width and the six rects do not move; data-hw-typing never set.
  6  DB: one flashcard_reviews row per rating made, each review answer kept;
     the sittings counted; no assignment_submissions (nothing secured).

    MRB_SHOTS=~/tmp/ks3-gates/sharpen-D1 python3 tools/flashcards_stage_d_live.py

TEST ONLY: the service key's own `ref` claim is checked before any write.
Throwaway rows are torn down by a SNAPSHOTTED ID LIST, never a predicate.
"""
from __future__ import annotations

import argparse
import base64
import json
import os
import signal
import subprocess
import sys
import time
import urllib.request
import uuid
from datetime import datetime, timedelta, timezone

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO)
sys.path.insert(0, os.path.join(REPO, "tools"))
import mrb351_acceptance as acc  # noqa: E402
import mrb351_pupil_flow_live as pf  # noqa: E402
import ks3_browser as cdp  # noqa: E402
import flashcard_homework_drive as drv  # noqa: E402

check = drv.check
FAILS = drv.FAILS

CARDS = [
    {"question": "What is the unit of force?", "answer": "The newton (N)"},
    {"question": "What is the unit of energy?", "answer": "The joule (J)"},
    {"question": "What is the unit of power?", "answer": "The watt (W)"},
    {"question": "What is the unit of charge?", "answer": "The coulomb (C)"},
    {"question": "What is the unit of current?", "answer": "The ampere (A)"},
    {"question": "What is the unit of potential difference?", "answer": "The volt (V)"},
    {"question": "What is the unit of resistance?", "answer": "The ohm"},
    {"question": "What is the unit of frequency?", "answer": "The hertz (Hz)"},
    {"question": "What is the unit of pressure?", "answer": "The pascal (Pa)"},
    {"question": "What is the unit of mass?", "answer": "The kilogram (kg)"},
]
Q = [c["question"] for c in CARDS]
RIGHT = dict(zip(Q, ["newton", "joule", "watt", "coulomb", "ampere", "volt", "ohm", "hertz", "pascal", "kilogram"]))
TITLE = "Units, stage D"
DEFAULT_ENV = "/Users/midebadmus/Documents/GitHub/mrbadmus-backend-worktrees/sharpen/.env"
BACKEND_DIR = os.path.dirname(DEFAULT_ENV)


def free_port():
    import socket
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    p = s.getsockname()[1]
    s.close()
    return p


def build(c, manifest, label):
    ts = int(time.time())
    school, klass, year = str(uuid.uuid4()), str(uuid.uuid4()), str(uuid.uuid4())
    manifest.update({"schools": [school], "classes": [klass], "years": [year]})
    people = {}
    for key in ("t", "p"):
        email = f"mrb351sd-{key}-{label}-{ts}@throwaway.test"
        uid = c.admin_create_user(email, acc.THROWAWAY_PASSWORD)
        manifest.setdefault("users", []).append(uid)
        people[key] = {"id": uid, "email": email}
    manifest["people"] = people
    acc._ok("school", *c.write("schools", "POST", {"id": school, "name": f"MRB351 StageD {ts}",
                                                   "code": f"MRB351SD{ts}", "kind": "school",
                                                   "key_stages_supported": ["KS3", "KS4"]}))
    today = datetime.now(timezone.utc).date()
    start = f"{today.year if today.month >= 9 else today.year - 1}-09-01"
    end = f"{int(start[:4]) + 1}-08-31"
    acc._ok("year", *c.write("academic_years", "POST", {"id": year, "school_id": school, "name": "staged",
                                                        "start_date": start, "end_date": end, "is_current": True}))
    acc._ok("class", *c.write("classes", "POST", {
        "id": klass, "school_id": school, "academic_year_id": year, "name": f"8d/Sc{ts % 10}",
        "key_stage": "KS3", "year_group": 8}))
    acc._ok("t", *c.write("profiles", "PATCH", {"__match__": f"id=eq.{people['t']['id']}",
        "role": "teacher", "school_id": school, "first_name": "Tsd", "last_name": "Mrb351",
        "display_name": "Tsd Mrb351", "username": f"mrb351sdt{ts:x}"}))
    acc._ok("p", *c.write("profiles", "PATCH", {"__match__": f"id=eq.{people['p']['id']}",
        "role": "student", "school_id": school, "first_name": "Psd", "last_name": "Mrb351",
        "display_name": "Psd Mrb351", "username": f"mrb351sdp{ts:x}",
        "science_pathway": "combined", "tier": "higher"}))
    st, subj = c.select(None, "subjects", {"select": "id,name", "name": "eq.Physics"}, as_service=True)
    acc._ok("class_teachers", *c.write("class_teachers", "POST", {
        "class_id": klass, "teacher_id": people["t"]["id"], "role": "subject_teacher",
        "subject_id": subj[0]["id"]}))
    acc._ok("class_members", *c.write("class_members", "POST", {
        "class_id": klass, "student_id": people["p"]["id"], "joined_via": "admin_added"}))
    tok_t = c.sign_in(people["t"]["email"], acc.THROWAWAY_PASSWORD)
    st, deck = c.rpc(tok_t, "flashcard_deck_save", {
        "p_deck": None, "p_title": TITLE, "p_cards": CARDS,
        "p_meta": {"source_kind": "typed", "subject": "physics"}, "p_finalise": True})
    if st != 200:
        acc.die(f"deck save {st} {deck}")
    manifest["decks"] = [deck["deck_id"]]
    now = datetime.now(timezone.utc)
    st, sw = c.rpc(tok_t, "flashcard_set_work", {
        "p_class_ids": [klass], "p_deck": deck["deck_id"], "p_mode": "review", "p_rule": "secure",
        "p_title": TITLE, "p_release_at": (now - timedelta(minutes=1)).isoformat(),
        "p_due_at": (now + timedelta(days=5)).isoformat(), "p_note": None,
        "p_client_ref": f"mrb351-sd-{label}-{ts}"})
    if st != 200:
        acc.die(f"set work {st} {sw}")
    manifest["assignments"] = list(sw["assignment_ids"])
    return {"people": people, "aid": sw["assignment_ids"][0], "tok_t": tok_t}


PENDING_JS = "(function(){var e=window.MRBHomework&&window.MRBHomework.active; return e ? e.pending.length : -1;})()"
SEGS_JS = ("(function(){var e=window.MRBHomework&&window.MRBHomework.active; if(!e) return null; var v=e.view();"
           " return {segs: v.segments.map(function(s){return s.state;}), retry: v.retry, queue: e.passIds.length - e.idx,"
           " phase: v.phase};})()")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--label", default="run")
    ap.add_argument("--env-file", default=DEFAULT_ENV)
    ap.add_argument("--keep", action="store_true")
    a = ap.parse_args()

    env = acc.read_env(a.env_file)
    url, service = env["SUPABASE_URL"], env["SUPABASE_SERVICE_ROLE_KEY"]
    ref = acc.jwt_ref(service)
    if ref != acc.TEST_REF:
        acc.die(f"refusing: service key ref {ref} is not TEST ({acc.TEST_REF})")
    print(f"credential ref, proven from the key payload: {ref} => TEST")
    c = acc.Client(url, acc.anon_key(), service)
    shots = os.path.join(os.environ.get("MRB_SHOTS") or cdp.gate_tmp(), "flashcards-stage-d")
    os.makedirs(shots, exist_ok=True)
    manifest, result = {}, {"ratings": 0}
    mpath = os.path.join(shots, "manifest.json")

    sport, bport = free_port(), free_port()
    origin = f"http://127.0.0.1:{sport}"
    benv = dict(os.environ, PORT=str(bport), EXTRA_CORS_ORIGINS=origin)
    backend = subprocess.Popen(["node", "server.js"], cwd=BACKEND_DIR, env=benv,
                               stdout=open(os.path.join(shots, "backend.log"), "w"),
                               stderr=subprocess.STDOUT, start_new_session=True)
    api = f"http://localhost:{bport}"
    t0 = time.time()
    while time.time() - t0 < 30:
        try:
            with urllib.request.urlopen(api + "/api/health", timeout=2) as r:
                if r.status == 200:
                    break
        except Exception:
            time.sleep(0.5)
    print(f"backend {api} (pid {backend.pid}), site {origin}")

    def sign_in(email):
        st, sess = c._req("POST", f"{url}/auth/v1/token?grant_type=password",
                          {"apikey": c.anon, "Content-Type": "application/json"},
                          {"email": email, "password": acc.THROWAWAY_PASSWORD})
        if st != 200:
            acc.die(f"pupil sign-in {st}")
        return sess

    def shot(page, name):
        res = page.send("Page.captureScreenshot", {"format": "png", "fromSurface": True})
        with open(os.path.join(shots, name + ".png"), "wb") as fh:
            fh.write(base64.b64decode(res["data"]))

    def phone(br, sess):
        page = br.attach()
        page.send("Emulation.setDeviceMetricsOverride",
                  {"width": 390, "height": 844, "deviceScaleFactor": 2, "mobile": True})
        page.send("Emulation.setTouchEmulationEnabled", {"enabled": True, "maxTouchPoints": 5})
        try:
            page.send("Emulation.setFocusEmulationEnabled", {"enabled": True})
        except cdp.CDPError:
            pass
        page.send("Page.addScriptToEvaluateOnNewDocument", {"source": drv.FAKE_VV})
        page.send("Page.addScriptToEvaluateOnNewDocument", {"source": pf.session_js(ref, sess)})
        return drv.Phone(page, 390, 844, 508, shots)

    def open_deck(P, aid, wait=40):
        P.page.goto("about:blank")
        P.page.goto(f"{origin}/student/class.html?api={api}#cards={aid}")
        t = time.time()
        while time.time() - t < wait:
            s = P.st()
            if s["strip"] and (s["writing"] or s["rating"] or s["panel"]):
                return s
            time.sleep(0.5)
        print("  [open_deck] not open: %r" % (P.q("document.body.innerText") or "")[:300])
        return P.st()

    def settled(P, timeout=20):
        t = time.time()
        while time.time() - t < timeout:
            if P.q(PENDING_JS) == 0:
                return True
            time.sleep(0.3)
        return False

    def rate(P, right):
        f = P.st()["front"]
        P.type(RIGHT.get(f, "x") if right else "zzz")
        P.click('[data-hw="check"]')
        P.click('[data-hw="%s"]' % ("got_it" if right else "not_yet"))
        result["ratings"] += 1
        return f

    def close(P):
        P.click('[data-port-region="flashcards-overlay"] button[title="Close"]')
        time.sleep(0.8)

    def reopen(P, aid, pred=None, timeout=15):
        P.q("window.__MRB_OPEN_HW__(%s)" % json.dumps(aid))
        return pf.wait_for(P, pred or (lambda x: x["strip"]), "reopen", timeout=timeout)

    def reviews(aid, pupil):
        st, rows = c.select(None, "flashcard_reviews", {"assignment_id": f"eq.{aid}", "pupil_id": f"eq.{pupil}",
                            "select": "id,card_id,rating,phase,answer,rated_at", "order": "rated_at.asc"}, as_service=True)
        return rows or []

    def sessions(aid, pupil):
        st, rows = c.select(None, "flashcard_sessions", {"assignment_id": f"eq.{aid}", "pupil_id": f"eq.{pupil}",
                            "select": "id,started_at,last_seen_at,ended_at"}, as_service=True)
        return rows or []

    try:
        w = build(c, manifest, a.label)
        json.dump(manifest, open(mpath, "w"), indent=1)
        aid, pupil = w["aid"], w["people"]["p"]
        server, port = cdp.serve(REPO, sport)
        try:
            # ══ 1 · × mid-pass, reopen ══════════════════════════════════════
            brA = cdp.Browser().start()
            P = phone(brA, sign_in(pupil["email"]))
            s = open_deck(P, aid)
            check(s["progress"] == "0 of 10 right" and s["segs"] == 10,
                  "1: the real class page opens the ten-card deck at '0 of 10 right' (got %r)" % s["progress"])
            rate(P, True); rate(P, False); rate(P, True)
            check(P.st()["progress"] == "2 of 10 right", "1: three answered → '2 of 10 right'")
            check(settled(P), "1: the device queue is empty (everything reached the server)")
            close(P)
            shot(P.page, "01-closed")
            s = reopen(P, aid, lambda x: x["writing"])
            g = P.q(SEGS_JS)
            check(s["progress"] == "2 of 10 right" and s["front"] == Q[3] and s["back"]
                  and g["segs"][:4] == ["right", "answered", "right", "todo"],
                  "1: reopened after × → card 4 at '2 of 10 right', segments right/answered/right, ‹ Back (got %r %r %r)"
                  % (s["progress"], s["front"], g["segs"][:4]))
            shot(P.page, "02-reopen-card-4")
            rv, ss = reviews(aid, pupil["id"]), sessions(aid, pupil["id"])
            check(len(rv) == 3 and len(ss) == 1 and ss[0]["ended_at"],
                  "1: DB — 3 flashcard_reviews rows, 1 flashcard_sessions row, ended by × (%d, %s)" % (len(rv), ss))

            # ══ 2 · the phone dies; another device ══════════════════════════
            rate(P, True)
            check(settled(P), "2: card 4's rating reached the server before the phone died")
            P.type("half a thought")              # typed on the dying phone, never sent
            brA.kill()
            check(brA.proc is None, "2: Chrome SIGKILLed (no pagehide, no beforeunload)")
            brB = cdp.Browser().start()
            P = phone(brB, sign_in(pupil["email"]))
            s = open_deck(P, aid)
            check(s["progress"] == "3 of 10 right" and s["front"] == Q[4] and s["draft"] == "",
                  "2: another device, fresh profile → card 5 at '3 of 10 right' (got %r %r)" % (s["progress"], s["front"]))
            shot(P.page, "03-other-device-card-5")

            # ══ 3 · offline, then a reload ═════════════════════════════════
            P.page.send("Network.enable")
            P.page.send("Network.emulateNetworkConditions", {"offline": True, "latency": 0,
                                                             "downloadThroughput": -1, "uploadThroughput": -1})
            rate(P, True)
            s = pf.wait_for(P, lambda x: "SAVED ON THIS PHONE" in (x["text"] or "").upper(), "offline", timeout=15)
            check("SAVED ON THIS PHONE" in (s["text"] or "").upper() and P.q(PENDING_JS) > 0,
                  "3: offline → SAVED ON THIS PHONE, the rating queued on the device")
            shot(P.page, "04-offline-saved")
            queued = len(reviews(aid, pupil["id"]))
            P.page.send("Network.emulateNetworkConditions", {"offline": False, "latency": 0,
                                                             "downloadThroughput": -1, "uploadThroughput": -1})
            s = open_deck(P, aid)                 # a reload
            check(s["progress"] == "4 of 10 right" and s["front"] == Q[5],
                  "3: online and reloaded → the queue went first, card 6 at '4 of 10 right' (got %r %r)"
                  % (s["progress"], s["front"]))
            shot(P.page, "05-after-offline-reload")
            rv = reviews(aid, pupil["id"])
            check(queued == 4 and len(rv) == 5, "3: DB — 4 rows while offline, 5 after the reload (%d → %d)" % (queued, len(rv)))

            # ══ 4 · Try again across reopens, then the hour ═════════════════
            for right in (True, False, True, False, True):   # cards 6–10: 7 and 9 wrong
                rate(P, right)
            s = pf.wait_for(P, lambda x: x["end1"] is not None, "try again")
            check(s["end1"] == "7 of 10 right" and s["retryPass"] == "Try again",
                  "4: the pass ends on Try again, '7 of 10 right' (got %r)" % s["end1"])
            shot(P.page, "06-try-again")
            settled(P)
            close(P)
            s = reopen(P, aid, lambda x: x["end1"] is not None)
            check(s["end1"] == "7 of 10 right" and s["retryPass"] == "Try again",
                  "4: × and reopen → the same Try again screen (got %r %r)" % (s["end1"], s["retryPass"]))
            shot(P.page, "07-try-again-again")
            P.click('[data-hw="retry-pass"]')
            s = P.st()
            g = P.q(SEGS_JS)
            check(s["chipsShown"] and s["greens"] == 7 and g["queue"] == 3 and s["front"] == Q[1],
                  "4: Try again → chips, 7 green, a queue of 3 starting at card 2 (got %r %r %r)"
                  % (s["greens"], g["queue"], s["front"]))
            shot(P.page, "08-retry-queue")
            rate(P, True)
            check(settled(P), "4: the retry's rating reached the server")
            close(P)
            s = reopen(P, aid, lambda x: x["chipsShown"])
            g = P.q(SEGS_JS)
            check(s["chipsShown"] and g["retry"] and g["queue"] == 2 and s["progress"] == "8 of 10 right"
                  and s["front"] == Q[6],
                  "4: mid-retry reopen → chips, a queue of 2, '8 of 10 right', card 7 (got %r %r %r)"
                  % (g["queue"], s["progress"], s["front"]))
            shot(P.page, "09-mid-retry-reopen")
            close(P)
            hour = timedelta(minutes=61)

            def back(ts):
                return (datetime.fromisoformat(ts.replace("Z", "+00:00")) - hour).isoformat() if ts else ts

            def shift_hour():
                for r in reviews(aid, pupil["id"]):
                    acc._ok("shift review", *c.write("flashcard_reviews", "PATCH",
                                                     {"__match__": f"id=eq.{r['id']}", "rated_at": back(r["rated_at"])}))
                for x in sessions(aid, pupil["id"]):
                    acc._ok("shift session", *c.write("flashcard_sessions", "PATCH", {
                        "__match__": f"id=eq.{x['id']}", "started_at": back(x["started_at"]),
                        "last_seen_at": back(x["last_seen_at"]), "ended_at": back(x["ended_at"])}))
            # An unfinished round keeps its place however long the pupil is away
            # (decision 5: only a FINISHED round goes stale after an hour).
            shift_hour()
            s = reopen(P, aid, lambda x: x["chipsShown"])
            g = P.q(SEGS_JS)
            check(s["chipsShown"] and g["queue"] == 2 and s["progress"] == "8 of 10 right" and s["front"] == Q[6],
                  "4: an hour later, mid-retry → still the chips and the queue of 2 (got %r %r)" % (g["queue"], s["progress"]))
            rate(P, True); rate(P, False)
            s = pf.wait_for(P, lambda x: x["end1"] is not None, "try again 2")
            check(s["end1"] == "9 of 10 right" and s["retryPass"] == "Try again",
                  "4: the retry round ends on Try again, '9 of 10 right' (got %r)" % s["end1"])
            settled(P)
            close(P)
            shift_hour()
            s = reopen(P, aid, lambda x: x["writing"] and not x["chipsShown"])
            g = P.q(SEGS_JS)
            check(s["progress"] == "0 of 10 right" and g["segs"] == ["todo"] * 10 and not s["chipsShown"],
                  "4: every rating an hour old → a new pass, '0 of 10 right', 10 to do (got %r)" % s["progress"])
            shot(P.page, "10-new-pass-after-hour")
            close(P)
            brB.close()

            # ══ 5 · the desktop: nothing moves ══════════════════════════════
            with cdp.Browser() as brC:
                page = brC.attach()
                page.send("Emulation.setDeviceMetricsOverride",
                          {"width": 1440, "height": 900, "deviceScaleFactor": 1, "mobile": False})
                try:
                    page.send("Emulation.setFocusEmulationEnabled", {"enabled": True})
                except cdp.CDPError:
                    pass
                page.send("Page.addScriptToEvaluateOnNewDocument", {"source": pf.session_js(ref, sign_in(pupil["email"]))})
                page.goto(f"{origin}/student/class.html?api={api}")
                t = time.time()
                while time.time() - t < 40 and not page.eval(
                        "Array.prototype.some.call(document.querySelectorAll('button'),"
                        " function(b){return (b.innerText||'').indexOf(%s)>=0;})" % json.dumps(TITLE)):
                    time.sleep(0.5)
                time.sleep(1.0)
                ROW = ("(function(){var b=Array.prototype.filter.call(document.querySelectorAll('button'),"
                       " function(b){return (b.innerText||'').indexOf(%s)>=0 && !b.closest('[data-port-region=\"flashcards-overlay\"]');})[0];"
                       " if(!b) return null; var r=b.getBoundingClientRect();"
                       " return {y: window.scrollY, top: r.top, cw: document.documentElement.clientWidth,"
                       " gutter: getComputedStyle(document.documentElement).scrollbarGutter,"
                       " scrolls: (window.__SCROLLS__||[]).length};})()" % json.dumps(TITLE))
                page.eval("(function(){var b=Array.prototype.filter.call(document.querySelectorAll('button'),"
                          " function(b){return (b.innerText||'').indexOf(%s)>=0;})[0];"
                          " window.scrollTo(0, Math.max(0, b.getBoundingClientRect().top + window.scrollY - 450));})()"
                          % json.dumps(TITLE))
                time.sleep(0.5)
                r0 = page.eval(ROW)
                page.eval("window.__SCROLLS__=[]; window.addEventListener('scroll', function(){window.__SCROLLS__.push(1);}, true);")
                page.eval(pf_row_click(TITLE))
                time.sleep(0.8)
                r1 = page.eval(ROW)
                page.eval("window.__MRB_OPEN_HW__(%s)" % json.dumps(aid))
                t = time.time()
                while time.time() - t < 15 and not page.eval("!!document.querySelector('[data-hw=\"answer\"]')"):
                    time.sleep(0.3)
                time.sleep(0.8)
                r2 = page.eval(ROW)
                rects = [page.eval(drv.RECTS_JS)]
                page.eval("document.querySelector('[data-hw=\"answer\"]').focus()")
                time.sleep(0.6)
                rects.append(page.eval(drv.RECTS_JS))
                shot(page, "11-desk-no-jump")
                page.eval("(function(){var t=document.querySelector('[data-hw=\"answer\"]'); t.value='n';"
                          " t.dispatchEvent(new Event('input',{bubbles:true}));})()")
                time.sleep(0.6)
                rects.append(page.eval(drv.RECTS_JS))
                page.eval("document.querySelector('[data-port-region=\"flashcards-overlay\"] button[title=\"Close\"]').click()")
                time.sleep(1.0)
                r3 = page.eval(ROW)
                for step, x in (("the row expands", r1), ("the deck opens", r2), ("the deck closes", r3)):
                    check(x and abs(x["y"] - r0["y"]) <= 1 and abs(x["top"] - r0["top"]) <= 1 and abs(x["cw"] - r0["cw"]) <= 1,
                          "5: 1440, %s — scrollY %s→%s, row top %.1f→%.1f, width %s→%s" %
                          (step, r0["y"], x and x["y"], r0["top"], x and x["top"], r0["cw"], x and x["cw"]))
                check(r3["scrolls"] == 0, "5: 1440 — no scroll event across click, open, focus, typing, close (%d)" % r3["scrolls"])
                check(r0["gutter"] == "stable", "5: the class page keeps its scrollbar's room (%s)" % r0["gutter"])
                keys = ("header", "strip", "card", "q", "ta", "check")
                same = all(x[k] == rects[0][k] for x in rects[1:] for k in keys)
                check(same and all(x["typing"] is None for x in rects),
                      "5: 1440 — the six rects identical at rest, focused and typing; data-hw-typing absent (%s)"
                      % ([[x[k] for k in keys] for x in rects] if not same else rects[0]))

            # ══ 6 · the database ════════════════════════════════════════════
            rv, ss = reviews(aid, pupil["id"]), sessions(aid, pupil["id"])
            result["reviews"], result["sessions"] = len(rv), len(ss)
            check(len(rv) == result["ratings"], "6: one flashcard_reviews row per rating made (%d rows, %d ratings)"
                  % (len(rv), result["ratings"]))
            check(all(r["answer"] for r in rv if r["phase"] == "review"),
                  "6: every review rating kept the answer typed for it")
            check(len(ss) >= 3, "6: sittings — %d (one per × / hour boundary; the server's rule, unchanged)" % len(ss))
            st, subs = c.select(None, "assignment_submissions", {"assignment_id": f"eq.{aid}", "select": "id"},
                                as_service=True)
            check(not subs, "6: no assignment_submissions row (nothing secured under 'secure')")
        finally:
            server.shutdown()
            server.server_close()
        json.dump(result, open(os.path.join(shots, "result.json"), "w"), indent=1, default=str)
    finally:
        try:
            os.killpg(backend.pid, signal.SIGTERM)
        except OSError:
            pass
        if not a.keep and manifest.get("classes"):
            st, extra = c.select(None, "assignments", {"class_id": f"in.({','.join(manifest['classes'])})",
                                                      "select": "id"}, as_service=True)
            manifest["auto_assignments"] = [x["id"] for x in (extra or []) if x["id"] not in manifest.get("assignments", [])]
            json.dump(manifest, open(mpath, "w"), indent=1)
            pf.teardown(c, manifest)
            residue = {}
            for table, ids in (("schools", manifest.get("schools", [])), ("classes", manifest.get("classes", [])),
                               ("assignments", manifest.get("assignments", []))):
                if ids:
                    st, rows = c.select(None, table, {"id": f"in.({','.join(ids)})", "select": "id"}, as_service=True)
                    if rows:
                        residue[table] = len(rows)
            check(not residue, "teardown by snapshotted id list left nothing behind (%s)" % residue)
    print("\n  screenshots: %s" % shots)
    if FAILS:
        print("\n  FAIL — %d check(s)" % len(FAILS))
        sys.exit(1)
    print("\n  PASS — flashcards stage D1, live on TEST")


def pf_row_click(title):
    """Press the deck's row header (it expands the row)."""
    return ("(function(){var b=Array.prototype.filter.call(document.querySelectorAll('button'),"
            " function(b){return (b.innerText||'').indexOf(%s)>=0 && !b.closest('[data-port-region=\"flashcards-overlay\"]');})[0];"
            " if(b) b.click(); return !!b;})()" % json.dumps(title))


if __name__ == "__main__":
    main()
