#!/usr/bin/env python3
"""flashcards_complete_live.py — "finished the homework" is done, the LIVE
proof on TEST (Mide's ruling, 1 Oct 2026; docs/experience/DESIGN-PORT-REPORT.md
"Follow-up 1 Oct").

Two throwaway pupils do real flashcard homework on the REAL class page
(student/class.html, served locally; config -> TEST; the backend run from
the design-port backend worktree, pointed at TEST) against the REAL TEST
database. Nothing about the write path is stubbed: the engine's own
`onFinish` hook (`shared/flashcard-homework.js`) and the write it triggers
(`shared/student-live.js`'s `recordFinish`) run for real, against real RLS.

  (a) pupilReview finishes a REVIEW-mode set, all-Got-it, in one sitting →
      the teacher sees them "in" (`flashcard_progress` status, a live
      class-detail.html read), the pupil's own row reads "Give it another
      go" and sits outside To do. Reopening starts a FRESH pass; finishing
      it again does not move `completed_at` (idempotent).
  (b) pupilMake finishes a MAKE-mode set: the writing pass, then the review
      pass all-Got-it → done, same proof.
  (c) HEAL — reusing the EXISTING design-port throwaway world
      (docs/.../design-port/world/WORLD.md, class 8d/Sc1, F1 "Cell
      structures — flashcards"): Ben and Chidi finished before this fix (no
      submission, reproducing Mide's bug). Loading the real class page as
      each of them (which runs `wireLibrary`'s heal) writes the row; the
      teacher then sees them "in" too.
  (d) pupilReview, mid a SECOND set, is NOT done and resumes on the next
      undone card (Stage D; unchanged by this fix — asserted so a future
      change cannot quietly break it here).
  (e) a reminder on the finished set is hidden once it is done; a reminder
      on a different, unfinished set still shows.

    MRB_SHOTS=~/tmp/mrb-shots/design-port/fc-complete/shots \\
      python3 tools/flashcards_complete_live.py

TEST ONLY: the service key's own `ref` claim is checked before any write,
against qeppkiswvclkkwbxmlok. Production (urklkrwevjtlfbwnipjn) is never
touched. Throwaway rows are torn down by a SNAPSHOTTED ID LIST, never a
predicate (memory "Throwaway teardown").
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

DEFAULT_ENV = "/Users/midebadmus/Documents/GitHub/mrbadmus-backend-worktrees/design-port/.env"
BACKEND_DIR = os.path.dirname(DEFAULT_ENV)
WORLD_MANIFEST = "/Users/midebadmus/tmp/mrb-shots/design-port/world/manifest.json"

REVIEW_CARDS = pf.CARDS            # 5 physics cards, RIGHT already mapped
REVIEW_RIGHT = pf.RIGHT
MAKE_CARDS = [
    {"question": "What is the unit of charge?", "answer": "The coulomb (C)"},
    {"question": "What is the unit of current?", "answer": "The ampere (A)"},
    {"question": "What is the unit of resistance?", "answer": "The ohm"},
]
MAKE_RIGHT = {"What is the unit of charge?": "coulomb", "What is the unit of current?": "ampere",
              "What is the unit of resistance?": "ohm"}
RESUME_CARDS = [
    {"question": "What is the unit of frequency?", "answer": "The hertz (Hz)"},
    {"question": "What is the unit of pressure?", "answer": "The pascal (Pa)"},
    {"question": "What is the unit of mass?", "answer": "The kilogram (kg)"},
]
RESUME_RIGHT = {"What is the unit of frequency?": "hertz", "What is the unit of pressure?": "pascal",
                "What is the unit of mass?": "kilogram"}


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
    for key in ("t", "review", "make"):
        email = f"fccomplete-{key}-{label}-{ts}@throwaway.test"
        uid = c.admin_create_user(email, acc.THROWAWAY_PASSWORD)
        manifest.setdefault("users", []).append(uid)
        people[key] = {"id": uid, "email": email}
    manifest["people"] = people
    acc._ok("school", *c.write("schools", "POST", {"id": school, "name": f"FC Complete {ts}",
                                                    "code": f"FCCOMPLETE{ts}", "kind": "school",
                                                    "key_stages_supported": ["KS3", "KS4"]}))
    today = datetime.now(timezone.utc).date()
    start = f"{today.year if today.month >= 9 else today.year - 1}-09-01"
    end = f"{int(start[:4]) + 1}-08-31"
    acc._ok("year", *c.write("academic_years", "POST", {"id": year, "school_id": school, "name": "fc-complete",
                                                        "start_date": start, "end_date": end, "is_current": True}))
    acc._ok("class", *c.write("classes", "POST", {
        "id": klass, "school_id": school, "academic_year_id": year, "name": f"8f/Sc{ts % 10}",
        "key_stage": "KS3", "year_group": 8}))
    acc._ok("t", *c.write("profiles", "PATCH", {"__match__": f"id=eq.{people['t']['id']}",
        "role": "teacher", "school_id": school, "first_name": "Tfc", "last_name": "Complete",
        "display_name": "Tfc Complete", "username": f"fcct{ts:x}"}))
    for key, first in (("review", "Rev"), ("make", "Mak")):
        acc._ok(key, *c.write("profiles", "PATCH", {"__match__": f"id=eq.{people[key]['id']}",
            "role": "student", "school_id": school, "first_name": first, "last_name": "Complete",
            "display_name": f"{first} Complete", "username": f"fcc{key[0]}{ts:x}",
            "science_pathway": "combined", "tier": "higher"}))
    st, subj = c.select(None, "subjects", {"select": "id,name", "name": "eq.Physics"}, as_service=True)
    acc._ok("class_teachers", *c.write("class_teachers", "POST", {
        "class_id": klass, "teacher_id": people["t"]["id"], "role": "subject_teacher",
        "subject_id": subj[0]["id"]}))
    for key in ("review", "make"):
        acc._ok("class_members", *c.write("class_members", "POST", {
            "class_id": klass, "student_id": people[key]["id"], "joined_via": "admin_added"}))
    tok_t = c.sign_in(people["t"]["email"], acc.THROWAWAY_PASSWORD)
    now = datetime.now(timezone.utc)

    def set_deck(title, cards, mode, class_ref):
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
            "p_client_ref": f"fc-complete-{class_ref}-{ts}"})
        if st != 200:
            acc.die(f"set work {st} {sw}")
        manifest.setdefault("assignments", []).extend(sw["assignment_ids"])
        return sw["assignment_ids"][0]

    aid_review = set_deck("Units, review", REVIEW_CARDS, "review", "rev")
    aid_make = set_deck("Units, make", MAKE_CARDS, "make", "mak")
    aid_resume = set_deck("Units, resume", RESUME_CARDS, "review", "res")
    return {"school": school, "class": klass, "people": people, "tok_t": tok_t,
            "aid_review": aid_review, "aid_make": aid_make, "aid_resume": aid_resume}


def teardown(c, manifest):
    aids, cls, users = manifest.get("assignments", []), manifest.get("classes", []), manifest.get("users", [])
    order = [
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


PROGRESS_JS = "(function(){var e=window.MRBHomework&&window.MRBHomework.active; if(!e) return null; var v=e.view(); return {phase:v.phase,progress:v.progress,end:v.end};})()"
WORK_ROW_JS = ("(function(){var b=Array.prototype.filter.call(document.querySelectorAll('button'),"
               " function(b){return (b.innerText||'').indexOf(%s)>=0 && !b.closest('[data-port-region=\"flashcards-overlay\"]');})[0];"
               " if(!b) return null; var card=b.closest('[data-port-region]')||b.parentElement;"
               " return {label: b.innerText.trim(), context: (card?card.innerText:'').slice(0,400)};})()")
REMINDER_JS = "(function(){var b=document.querySelector('[data-mrb-reminder]'); return b ? b.innerText : null;})()"


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
    shots = os.path.join(os.environ.get("MRB_SHOTS") or cdp.gate_tmp(), "fc-complete")
    os.makedirs(shots, exist_ok=True)
    manifest = {}
    mpath = os.path.join(shots, "manifest.json")

    sport, bport = free_port(), free_port()
    origin = f"http://127.0.0.1:{sport}"
    benv = dict(os.environ, PORT=str(bport), EXTRA_CORS_ORIGINS=origin)
    backend = subprocess.Popen(["node", "server.js"], cwd=BACKEND_DIR, env=benv,
                               stdout=open(os.path.join(shots, "backend.log"), "w"),
                               stderr=subprocess.STDOUT, start_new_session=True)
    api = f"http://localhost:{bport}"
    t0 = time.time()
    while time.time() - t0 < 45:
        try:
            with urllib.request.urlopen(api + "/api/health", timeout=2) as r:
                if r.status == 200:
                    break
        except Exception:
            time.sleep(0.5)
    time.sleep(2.0)   # /api/health green does not mean every route (DB pool,
                       # current-assignment) is warm yet — seen as a "could not
                       # load your class" flake on the very first page load
    print(f"backend {api} (pid {backend.pid}), site {origin}")

    def sign_in(email, password=None):
        st, sess = c._req("POST", f"{url}/auth/v1/token?grant_type=password",
                          {"apikey": c.anon, "Content-Type": "application/json"},
                          {"email": email, "password": password or acc.THROWAWAY_PASSWORD})
        if st != 200:
            acc.die(f"sign-in {email} -> {st} {sess}")
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

    def _goto_class(P, url, tries=2):
        for i in range(tries):
            try:
                P.page.goto(url)
                return
            except cdp.CDPError:
                if i == tries - 1:
                    raise
                time.sleep(1.5)

    def open_deck(P, aid, wait=40, tries=3):
        for attempt in range(tries):
            P.page.goto("about:blank")
            _goto_class(P, f"{origin}/student/class.html?api={api}#cards={aid}")
            t = time.time()
            while time.time() - t < wait:
                s = P.st()
                if s["strip"] and (s["writing"] or s["rating"] or s["panel"]):
                    return s
                body = P.q("document.body.innerText") or ""
                if "could not load your class" in body.lower():
                    break   # a transient backend hiccup under this test's own
                             # load — not a finding; reload rather than wait it out
                time.sleep(0.5)
            if attempt < tries - 1:
                print("  [open_deck] transient load failure, retrying…")
                time.sleep(2.0)
        print("  [open_deck] not open: %r" % (P.q("document.body.innerText") or "")[:300])
        return P.st()

    def load_class(P, wait=40):
        """Just load the class page (no deck) — e.g. to run the heal."""
        P.page.goto("about:blank")
        _goto_class(P, f"{origin}/student/class.html?api={api}")
        t = time.time()
        while time.time() - t < wait and P.q("!!window.__MRB_DATA__") is not True:
            time.sleep(0.5)
        time.sleep(3.5)   # the heal fires after the mount, not awaited — several
                          # sequential reads (reviews, cards, assignments, subs,
                          # sessions) must land before the write; give it room

    def answer_all(P, right_map, upto=99):
        n = 0
        while n < upto:
            s = P.st()
            if not s["writing"]:
                break
            front = s["front"]
            P.type(right_map.get(front, "x"))
            P.click('[data-hw="check"]')
            P.click('[data-hw="got_it"]')
            time.sleep(0.35)
            n += 1
        return n

    def submission(aid, pupil):
        st, rows = c.select(None, "assignment_submissions",
                            {"assignment_id": f"eq.{aid}", "student_id": f"eq.{pupil}",
                             "select": "id,score,max_score,submitted_at,completed_at,is_late,status"},
                            as_service=True)
        return (rows or [None])[0]

    try:
        w = build(c, manifest, a.label)
        json.dump(manifest, open(mpath, "w"), indent=1)
        klass = w["class"]
        tok_t = w["tok_t"]
        pupil_r, pupil_m = w["people"]["review"], w["people"]["make"]
        aid_r, aid_m, aid_res = w["aid_review"], w["aid_make"], w["aid_resume"]
        server, port = cdp.serve(REPO, sport)
        try:
            # ══ (a) review mode, all-Got-it in one sitting ═════════════════
            brA = cdp.Browser().start()
            P = phone(brA, sign_in(pupil_r["email"]))
            s = open_deck(P, aid_r)
            check(s["progress"] == "0 of 5 right", "a: opens at '0 of 5 right' (got %r)" % s["progress"])
            answer_all(P, REVIEW_RIGHT)
            s = pf.wait_for(P, lambda x: x["end1"] is not None, "a: end screen")
            check(s["end1"] == "5 of 5 right" and s["done"] == "Done",
                  "a: all right, one sitting → Done (got %r %r)" % (s["end1"], s["done"]))
            time.sleep(2.0)   # the flush settles → Api.onFinish → recordFinish
            shot(P.page, "a-01-done")
            sub1 = submission(aid_r, pupil_r["id"])
            check(bool(sub1) and sub1["status"] == "complete" and sub1["score"] == 5 and sub1["max_score"] == 5
                  and not sub1["is_late"],
                  "a: assignment_submissions row written at Done, on time, 5/5 (got %r)" % sub1)
            st_p, body_p = c.rpc(tok_t, "flashcard_progress", {"p_assignment": aid_r})
            rows_p = {p["pupil_id"]: p for p in (body_p or {}).get("pupils", [])} if st_p == 200 else {}
            check(rows_p.get(pupil_r["id"], {}).get("status") in ("done", "done_late"),
                  "a: teacher's flashcard_progress reads the pupil DONE (got %r)"
                  % rows_p.get(pupil_r["id"], {}).get("status"))
            # TEACHER screenshot: the progress table, pupil Done.
            with cdp.Browser() as brT:
                pageT = brT.attach()
                pageT.send("Emulation.setDeviceMetricsOverride",
                           {"width": 1440, "height": 900, "deviceScaleFactor": 1, "mobile": False})
                pageT.send("Page.addScriptToEvaluateOnNewDocument",
                           {"source": pf.session_js(ref, sign_in(w["people"]["t"]["email"]))})
                pageT.goto(f"{origin}/teacher/flashcards.html?assignment={aid_r}&api={api}")
                tT = time.time()
                while time.time() - tT < 20 and not pageT.eval("document.body.innerText.indexOf('Rev Complete')>=0"):
                    time.sleep(0.5)
                time.sleep(0.5)
                shot(pageT, "a-00-teacher-progress-done")

            # the pupil's own row: status 'marked', no secured wording, no
            # redundant text — the exact fields `student_rulings.py`'s
            # primaryLabel/detailLine tuples key off (RULED 1 Oct 2026).
            P.q("location.reload()")
            t = time.time()
            while time.time() - t < 30 and P.q("!!window.__MRB_DATA__") is not True:
                time.sleep(0.5)
            time.sleep(1.0)
            work_rows = P.q(
                "(function(){var w=(window.__MRB_DATA__&&window.__MRB_DATA__.work)||[];"
                " return w.map(function(x){return {id:x.id,title:x.title,status:x.status,"
                " detail:x.detail,fc:x.fc};});})()") or []
            row_r = next((x for x in work_rows if x.get("id") == aid_r), None)
            check(bool(row_r) and row_r.get("status") == "marked" and row_r.get("fc") is True
                  and (row_r.get("detail") or "").startswith("COMPLETED ")
                  and "SECURED" not in (row_r.get("detail") or ""),
                  "a: the pupil's data layer marks the row done, no 'secured' wording (got %r)" % row_r)
            # the RENDERED row: the WORK list is filtered to one teaching
            # week at a time, and this deck's due date can land outside
            # "this week" — switch to 'All weeks' first (a real pupil would
            # too), THEN expand the row (tap its title) for the button.
            P.q("(function(){var s=document.querySelector('[data-mrb-week-select]'); if(!s) return false;"
                " s.value=''; s.dispatchEvent(new Event('change',{bubbles:true})); return true;})()")
            time.sleep(0.6)
            # ⊕ 1 Oct 2026 (review) — the row's own header IS the toggle
            # button (student_rulings.py "PROD N4": node 161, one
            # <button onClick={{r.toggle}}>, which that same ruling gives
            # aria-expanded so a screen reader has something to announce).
            # The FIRST build's selector (`button,[role="button"],div`,
            # first match) could land on an OUTER wrapper that merely
            # CONTAINS the title text and sorts earlier in document order
            # than the real button — exactly the review's diagnosis. Scope
            # to the real toggle by that attribute, not by tag soup.
            tapped = P.q(
                "(function(){var bs=Array.prototype.filter.call(document.querySelectorAll('button[aria-expanded]'),"
                " function(b){return (b.innerText||'').indexOf('Units, review')>=0;});"
                " var b=bs[0]; if(!b) return false; b.scrollIntoView({block:'center'});"
                " b.click(); return true;})()")
            time.sleep(0.6)
            row = P.q(WORK_ROW_JS % json.dumps("Give it another go"))
            if not row:
                print("  [diag] tapped=%r; could not find the expanded button; body text:" % tapped,
                      repr((P.q("document.body.innerText") or "")[:600]))
            check(bool(row), "a: the expanded row's button reads 'Give it another go' (got %r)" % row)
            shot(P.page, "a-02-give-it-another-go")

            # reopen → a FRESH pass (never un-dones the set)
            s = open_deck(P, aid_r)
            check(s["progress"] == "0 of 5 right",
                  "a: reopening a done set starts a fresh pass, '0 of 5 right' (got %r)" % s["progress"])
            sub_before_fresh = submission(aid_r, pupil_r["id"])
            check(sub_before_fresh["completed_at"] == sub1["completed_at"],
                  "a: reopening alone does not touch completed_at")

            # finishing again: still complete, completed_at UNCHANGED (idempotent)
            answer_all(P, REVIEW_RIGHT)
            pf.wait_for(P, lambda x: x["end1"] is not None, "a: second end screen")
            time.sleep(2.0)
            sub2 = submission(aid_r, pupil_r["id"])
            check(sub2["completed_at"] == sub1["completed_at"] and sub2["id"] == sub1["id"],
                  "a: finishing a SECOND time never re-stamps completed_at (idempotent) (%r vs %r)"
                  % (sub2["completed_at"], sub1["completed_at"]))
            brA.close()

            # ══ (b) make mode: writing pass + review pass → done ═══════════
            brB = cdp.Browser().start()
            P = phone(brB, sign_in(pupil_m["email"]))
            s = open_deck(P, aid_m)
            check(P.q(PROGRESS_JS)["phase"] == "make", "b: opens on the writing pass (got %r)" % P.q(PROGRESS_JS))
            answer_all(P, MAKE_RIGHT)
            s = pf.wait_for(P, lambda x: x["again"] is not None, "b: writing pass end")
            check(s["again"] == "Revise flashcards one more time", "b: writing pass end screen (got %r)" % s["again"])
            P.click('[data-hw="again"]')
            time.sleep(0.6)
            answer_all(P, MAKE_RIGHT)
            s = pf.wait_for(P, lambda x: x["end1"] is not None, "b: review end")
            check(s["end1"] == "3 of 3 right" and s["done"] == "Done",
                  "b: make mode, review pass all right → Done (got %r %r)" % (s["end1"], s["done"]))
            time.sleep(2.0)
            shot(P.page, "b-01-make-done")
            subm = submission(aid_m, pupil_m["id"])
            check(bool(subm) and subm["status"] == "complete" and subm["score"] == 3,
                  "b: make mode writes the submission too (got %r)" % subm)
            brB.close()

            # ══ (d) mid-set: NOT done, resumes on the next undone card ═════
            brD = cdp.Browser().start()
            P = phone(brD, sign_in(pupil_r["email"]))
            s = open_deck(P, aid_res)
            P.type(RESUME_RIGHT.get(s["front"], "x")); P.click('[data-hw="check"]'); P.click('[data-hw="got_it"]')
            time.sleep(0.4)
            front2 = P.st()["front"]
            P.q("(function(){var e=window.MRBHomework&&window.MRBHomework.active; if(e){e.finish();}})()")
            time.sleep(1.0)
            check(submission(aid_res, pupil_r["id"]) is None,
                  "d: one of three cards done — not a finished set, no submission")
            s = open_deck(P, aid_res)
            check(s["progress"] == "1 of 3 right" and s["front"] == front2,
                  "d: reopening a mid-set deck resumes on the next undone card (got %r %r)" % (s["progress"], s["front"]))
            shot(P.page, "d-01-resume")
            brD.close()

            # ══ (e) a reminder hides once its set is done ═══════════════════
            acc._ok("reminder done", *c.write("student_notifications", "POST", {
                "student_id": pupil_r["id"], "class_id": klass, "assignment_id": aid_r,
                "kind": "reminder", "sent_by": w["people"]["t"]["id"]}))
            acc._ok("reminder open", *c.write("student_notifications", "POST", {
                "student_id": pupil_r["id"], "class_id": klass, "assignment_id": aid_res,
                "kind": "reminder", "sent_by": w["people"]["t"]["id"]}))
            brE = cdp.Browser().start()
            P = phone(brE, sign_in(pupil_r["email"]))
            load_class(P)
            txt = P.q(REMINDER_JS)
            check(txt is not None, "e: a reminder for the UNFINISHED resume set still shows (got %r)" % txt)
            shot(P.page, "e-01-reminder-shows")
            brE.close()
            # (the done set's reminder, on its own, with no other unread one)
            st_del, _ = c.write("student_notifications", "DELETE",
                                {"__match__": f"assignment_id=eq.{aid_res}"})
            brE2 = cdp.Browser().start()
            P = phone(brE2, sign_in(pupil_r["email"]))
            load_class(P)
            txt2 = P.q(REMINDER_JS)
            check(txt2 is None, "e: the reminder on the FINISHED set is hidden (got %r)" % txt2)
            shot(P.page, "e-02-reminder-hidden")
            brE2.close()

            # ══ (c) HEAL — the existing design-port world's Ben and Chidi ══
            if os.path.exists(WORLD_MANIFEST):
                wm = json.load(open(WORLD_MANIFEST))
                f1 = wm.get("f1_assignment_id")
                dp_people = wm.get("people", {})
                if f1 and "ben" in dp_people and "chidi" in dp_people:
                    before = {k: submission(f1, dp_people[k]["id"]) for k in ("ben", "chidi")}
                    for k in ("ben", "chidi"):
                        brH = cdp.Browser().start()
                        P = phone(brH, sign_in(dp_people[k]["email"], "DesignPort-2026!"))
                        load_class(P)
                        shot(P.page, f"c-{k}-after-heal")
                        brH.close()
                    after = {k: submission(f1, dp_people[k]["id"]) for k in ("ben", "chidi")}
                    for k in ("ben", "chidi"):
                        check(after[k] is not None and after[k]["status"] == "complete",
                              "c: heal — %s (finished before the fix, no row: %s) now has a submission after "
                              "loading the class page (%s)" % (k, bool(before[k]), after[k]))
                else:
                    check(False, "c: heal — WORLD.md manifest missing f1_assignment_id or ben/chidi; skipped (deviation)")
            else:
                check(False, "c: heal — %s not found; skipped (deviation, noted in the report)" % WORLD_MANIFEST)

        finally:
            server.shutdown()
            server.server_close()
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
            teardown(c, manifest)

    print(f"\n  {len(FAILS)} failed" if FAILS else "\n  all checks passed")
    for f in FAILS:
        print("  - " + f)
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main())
