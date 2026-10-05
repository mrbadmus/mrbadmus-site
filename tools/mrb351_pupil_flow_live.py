#!/usr/bin/env python3
"""mrb351_pupil_flow_live.py — MRB-351 pupil flow, the LIVE proof on TEST
(docs/mrb351/PUPIL-FLOW.md §9.3).

A throwaway pupil does real flashcard homework on the REAL class page
(student/class.html, served locally, config -> TEST, backend on
localhost:3000 pointed at TEST) against the REAL TEST database — no stub for
`flashcard_record`, no stub for the model check (TEST's deployed
`flashcard-answer-check` answers, and with no ANTHROPIC_API_KEY on TEST it
answers "no verdict": the page's fallback is what is exercised).

On a 390x844 phone (`mobile: true`), with the keyboard up (a fake
`visualViewport` of height 508, exactly as flashcard_homework_drive.py does):

  sitting 1 — the writing pass (Right, a model check with no verdict,
              ‹ Back twice, I don't know REPLACING a Got it, …), its end
              screen, the review pass, its end screen;
  then       — every sitting of this pupil moved back 61 minutes (service
              role PATCH of flashcard_sessions, as tools/mrb351_acceptance.py
              does) and the device's own end stamp with it;
  sitting 2 — a reload part-way through (resume), then the rest: every card
              secured, the end screen reads right, the submission row exists,
              and the teacher's flashcard_progress shows the pupil Done.

    python3 tools/mrb351_pupil_flow_live.py --label prod-state
    python3 tools/mrb351_pupil_flow_live.py --label migrated --expect-migration

Screenshots go to $MRB_SHOTS/pupil-flow/<label>/ (default
~/tmp/ks3-gates/pupil-flow/<label>/). TEST ONLY: the service key's own `ref`
claim is checked before any write. Throwaway accounts are minted here and
torn down by a SNAPSHOTTED ID LIST, never a predicate.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
import uuid
from datetime import datetime, timedelta, timezone

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO)
sys.path.insert(0, os.path.join(REPO, "tools"))
import mrb351_acceptance as acc  # noqa: E402  (Client, env, the TEST guard)
import ks3_browser as cdp  # noqa: E402
import flashcard_homework_drive as drv  # noqa: E402  (the phone, the checks)

check = drv.check
FAILS = drv.FAILS

CARDS = [
    {"question": "What is the unit of force?", "answer": "The newton (N)"},
    {"question": "What is the formula of water?", "answer": "H2O"},
    {"question": "What is weight?", "answer": "The force acting on an object due to gravity"},
    {"question": "What is the unit of energy?", "answer": "The joule (J)"},
    {"question": "Is velocity a scalar or a vector?", "answer": "A vector"},
]
RIGHT = {"What is the unit of force?": "newton", "What is the formula of water?": "h2o",
         "What is weight?": "gravity", "What is the unit of energy?": "joule",
         "Is velocity a scalar or a vector?": "vector"}


def working_year(end_dates):
    horizon = (datetime.now() + timedelta(days=30)).date().isoformat()
    live = [d for d in end_dates if d >= horizon]
    return min(live) if live else max(end_dates)


def build(c, manifest, label):
    ts = int(time.time())
    school, klass, year = str(uuid.uuid4()), str(uuid.uuid4()), str(uuid.uuid4())
    manifest.update({"schools": [school], "classes": [klass], "years": [year]})
    people = {}
    for key in ("t", "p"):
        email = f"mrb351pf-{key}-{label}-{ts}@throwaway.test"
        uid = c.admin_create_user(email, acc.THROWAWAY_PASSWORD)
        manifest.setdefault("users", []).append(uid)
        people[key] = {"id": uid, "email": email}
    manifest["people"] = people
    acc._ok("school", *c.write("schools", "POST", {"id": school, "name": f"MRB351 Pupil Flow {ts}",
                                                   "code": f"MRB351PF{ts}", "kind": "school",
                                                   "key_stages_supported": ["KS3", "KS4"]}))
    today = datetime.now(timezone.utc).date()
    start = f"{today.year if today.month >= 9 else today.year - 1}-09-01"
    end = f"{int(start[:4]) + 1}-08-31"
    acc._ok("year", *c.write("academic_years", "POST", {"id": year, "school_id": school, "name": "pupil-flow",
                                                        "start_date": start, "end_date": end,
                                                        "is_current": True}))
    acc._ok("class", *c.write("classes", "POST", {
        "id": klass, "school_id": school, "academic_year_id": year, "name": f"8p/Sc{ts % 10}",
        "key_stage": "KS3", "year_group": 8}))
    acc._ok("t", *c.write("profiles", "PATCH", {"__match__": f"id=eq.{people['t']['id']}",
        "role": "teacher", "school_id": school, "first_name": "Tpf", "last_name": "Mrb351",
        "display_name": "Tpf Mrb351", "username": f"mrb351pft{ts:x}"}))
    acc._ok("p", *c.write("profiles", "PATCH", {"__match__": f"id=eq.{people['p']['id']}",
        "role": "student", "school_id": school, "first_name": "Ppf", "last_name": "Mrb351",
        "display_name": "Ppf Mrb351", "username": f"mrb351pfp{ts:x}",
        "science_pathway": "combined", "tier": "higher"}))
    st, subj = c.select(None, "subjects", {"select": "id,name", "name": "eq.Physics"}, as_service=True)
    acc._ok("class_teachers", *c.write("class_teachers", "POST", {
        "class_id": klass, "teacher_id": people["t"]["id"], "role": "subject_teacher",
        "subject_id": subj[0]["id"]}))
    acc._ok("class_members", *c.write("class_members", "POST", {
        "class_id": klass, "student_id": people["p"]["id"], "joined_via": "admin_added"}))
    tok_t = c.sign_in(people["t"]["email"], acc.THROWAWAY_PASSWORD)
    st, deck = c.rpc(tok_t, "flashcard_deck_save", {
        "p_deck": None, "p_title": "Forces flashcards", "p_cards": CARDS,
        "p_meta": {"source_kind": "typed", "subject": "physics"}, "p_finalise": True})
    if st != 200:
        acc.die(f"deck save {st} {deck}")
    manifest["decks"] = [deck["deck_id"]]
    now = datetime.now(timezone.utc)
    st, sw = c.rpc(tok_t, "flashcard_set_work", {
        "p_class_ids": [klass], "p_deck": deck["deck_id"], "p_mode": "make", "p_rule": "secure",
        "p_title": "Forces flashcards", "p_release_at": (now - timedelta(minutes=1)).isoformat(),
        "p_due_at": (now + timedelta(days=5)).isoformat(), "p_note": "Do these on your phone",
        "p_client_ref": f"mrb351-pf-{label}-{ts}"})
    if st != 200:
        acc.die(f"set work {st} {sw}")
    manifest["assignments"] = list(sw["assignment_ids"])
    return {"school": school, "class": klass, "people": people, "aid": sw["assignment_ids"][0],
            "tok_t": tok_t}


def teardown(c, manifest):
    """Children first, every delete by an id list captured when it was made."""
    aids, cls, users = manifest.get("assignments", []), manifest.get("classes", []), manifest.get("users", [])
    order = [
        ("flashcard_reviews", "assignment_id", aids), ("flashcard_pupil_cards", "assignment_id", aids),
        ("flashcard_events", "assignment_id", aids), ("flashcard_sessions", "assignment_id", aids),
        ("assignment_submissions", "assignment_id", aids), ("assignment_flashcards", "assignment_id", aids),
        ("assignments", "id", aids),
        # the class's own lazily auto-composed weekly work, if the page made one
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


def session_js(ref, session):
    key = f"sb-{ref}-auth-token"
    return ("(function(){try{if(location.hostname==='127.0.0.1'){localStorage.setItem(%s,%s);}}catch(e){}})();"
            % (json.dumps(key), json.dumps(json.dumps(session))))


def open_deck(P, port, aid, wait=30):
    # a fresh document every time (a hash-only change fires no load event)
    P.page.goto("about:blank")
    P.page.goto(f"http://127.0.0.1:{port}/student/class.html#cards={aid}")
    t0 = time.time()
    while time.time() - t0 < wait:
        s = P.st()
        if s["strip"] and (s["writing"] or s["rating"] or s["panel"]):
            return s
        time.sleep(0.5)
    print("  [open_deck] not open after %ds: url=%s text=%r errors=%s" % (
        wait, P.q("location.href"), (P.q("document.body.innerText") or "")[:400], P.page.console_errors()[:5]))
    return P.st()


def answer_all(P, rating="got_it", upto=99):
    n = 0
    while n < upto:
        s = P.st()
        if not s["writing"]:
            break
        P.type(RIGHT.get(s["front"], "x"))
        P.click('[data-hw="check"]')
        P.click('[data-hw="%s"]' % rating)
        settle_flush(P)
        n += 1
    return n


def settle_flush(P, t=0.4):
    time.sleep(t)


def wait_for(P, pred, what, timeout=15):
    t0 = time.time()
    s = P.st()
    while time.time() - t0 < timeout:
        s = P.st()
        if pred(s):
            return s
        time.sleep(0.4)
    return s


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--label", required=True)
    ap.add_argument("--expect-migration", action="store_true")
    ap.add_argument("--env-file", default="/Users/midebadmus/Documents/GitHub/mrbadmus-worktrees/"
                                          "pupil-flow-backend/.env")
    ap.add_argument("--keep", action="store_true")
    a = ap.parse_args()

    env = acc.read_env(a.env_file)
    url, service = env["SUPABASE_URL"], env["SUPABASE_SERVICE_ROLE_KEY"]
    ref = acc.jwt_ref(service)
    if ref != acc.TEST_REF:
        acc.die(f"refusing: service key ref {ref} is not TEST ({acc.TEST_REF})")
    print(f"credential ref, proven from the key payload: {ref} => TEST")
    c = acc.Client(url, acc.anon_key(), service)
    shots = os.path.join(os.environ.get("MRB_SHOTS") or cdp.gate_tmp(), "pupil-flow", a.label)
    os.makedirs(shots, exist_ok=True)
    manifest = {}
    mpath = os.path.join(shots, "manifest.json")
    result = {}
    try:
        w = build(c, manifest, a.label)
        json.dump(manifest, open(mpath, "w"), indent=1)
        aid, pupil = w["aid"], w["people"]["p"]
        st, sess = c._req("POST", f"{url}/auth/v1/token?grant_type=password",
                          {"apikey": c.anon, "Content-Type": "application/json"},
                          {"email": pupil["email"], "password": acc.THROWAWAY_PASSWORD})
        if st != 200:
            acc.die(f"pupil sign-in {st}")
        server, port = cdp.serve(REPO, 5611)
        try:
            with cdp.Browser() as br:
                page = br.attach()
                page.send("Emulation.setDeviceMetricsOverride",
                          {"width": 390, "height": 844, "deviceScaleFactor": 2, "mobile": True})
                page.send("Emulation.setTouchEmulationEnabled", {"enabled": True, "maxTouchPoints": 5})
                try:
                    page.send("Emulation.setFocusEmulationEnabled", {"enabled": True})
                except cdp.CDPError:
                    pass
                page.send("Page.addScriptToEvaluateOnNewDocument", {"source": drv.FAKE_VV})
                page.send("Page.addScriptToEvaluateOnNewDocument", {"source": session_js(ref, sess)})
                P = drv.Phone(page, 390, 844, 508, shots)

                # ══ SITTING 1 — the writing pass ═══════════════════════════
                s = open_deck(P, port, aid)
                check(s["strip"] and s["progress"] == "0 of 5 right" and s["writing"],
                      "live: the real class page opens the deck at '0 of 5 right' (got %r)" % s["progress"])
                check(s["note"] and s["stackPos"] == "" and not s["pips"], "live: teacher's note; no header counter; no pips")
                P.shot("s1-A-question")
                P.keyboard(True)
                P.boxes("live, state A")
                P.shot("s1-A-keyboard-up")
                P.type("newton")
                P.boxes("live, typed")
                P.click('[data-hw="check"]')
                P.keyboard(False)
                s = P.st()
                check(s["chip"] == "Right" and s["pressed"] == [], "live: 'newton' → Right as a hint, nothing filled")
                P.shot("s1-C-verdict")
                P.click('[data-hw="got_it"]')
                P.keyboard(True)
                P.type("hydrogen and oxygen")
                P.click('[data-hw="check"]')
                P.keyboard(False)
                s = P.st()
                check(s["chip"] in ("Checking…", None), "live: an undecided answer asks the model (%r)" % s["chip"])
                P.shot("s1-B-checking")
                s = wait_for(P, lambda x: x["chip"] is None, "no verdict", timeout=8)
                check(s["chip"] is None and s["pressed"] == [] and s["rating"],
                      "live: TEST's edge function gives no verdict (no key) → no chip, nothing filled")
                P.shot("s1-C-no-verdict")
                P.click('[data-hw="got_it"]')
                # ‹ Back twice, then I don't know REPLACES card 1's Got it
                P.click('[data-hw="back"]')
                s = P.st()
                check(s["front"] == "What is the formula of water?" and s["draft"] == "hydrogen and oxygen",
                      "live: ‹ Back → card 2 with its answer in the box")
                P.shot("s1-Back")
                P.click('[data-hw="back"]')
                check(P.st()["draft"] == "newton", "live: ‹ Back again → card 1 with 'newton'")
                P.click('[data-hw="idk"]')
                s = P.st()
                check(s["chip"] == "No answer" and s["pressed"] == [], "live: I don't know → No answer as a hint, nothing filled")
                P.shot("s1-idk")
                P.click('[data-hw="not_yet"]')
                s = P.st()
                check(s["progress"] == "1 of 5 right", "live: card 1 re-rated Not yet → '1 of 5 right' (got %r)" % s["progress"])
                P.click('[data-hw="check"]')        # card 2, its text still in the box
                wait_for(P, lambda x: x["chip"] is None, "no verdict", timeout=8)
                P.click('[data-hw="got_it"]')
                P.type("gravity"); P.click('[data-hw="check"]'); P.click('[data-hw="got_it"]')
                P.click('[data-hw="idk"]'); P.click('[data-hw="not_yet"]')          # card 4
                P.type("vector"); P.click('[data-hw="check"]'); P.click('[data-hw="got_it"]')
                s = wait_for(P, lambda x: x["end2"] is not None, "writing end")
                check(s["end1"] == "3 of 5 right this time" and s["end2"] == "0 of 5 secured so far"
                      and s["again"] == "Revise flashcards one more time",
                      "live: writing pass end — %r / %r / %r" % (s["end1"], s["end2"], s["again"]))
                P.shot("s1-End-writing")

                # ── the review pass, same sitting ────────────────────────
                P.click('[data-hw="again"]')
                s = P.st()
                check(s["progress"] == "0 of 5 right" and s["secured"] == "0 secured"
                      and s["hint"] == "Revise flashcards one more time",
                      "live: review pass opens '0 of 5 right' / '0 secured' / helper (got %r %r %r)"
                      % (s["progress"], s["secured"], s["hint"]))
                P.keyboard(True)
                P.boxes("live, review pass")
                P.shot("s1-Review-keyboard-up")
                P.keyboard(False)
                answer_all(P)
                s = wait_for(P, lambda x: x["end2"] is not None, "review end")
                secured1 = int((s["end2"] or "0").split(" ")[0] or 0)
                result["secured_after_sitting_1"] = secured1
                want1 = 3 if a.expect_migration else 4
                check(s["end1"] == "5 of 5 right this time" and secured1 == want1,
                      "live: sitting 1 review end — %r / %r (want %d secured: %s)"
                      % (s["end1"], s["end2"], want1,
                         "the replaced Got it no longer counts" if a.expect_migration
                         else "production counts card 1's replaced Got it"))
                P.shot("s1-End-review")
                P.click('[data-port-region="flashcards-overlay"] button[title="Close"]')
                time.sleep(1.0)

        finally:
            server.shutdown()
            server.server_close()

        # ══ an hour passes ═════════════════════════════════════════════════
        st, sessions = c.select(None, "flashcard_sessions",
                                {"assignment_id": f"eq.{aid}", "pupil_id": f"eq.{pupil['id']}",
                                 "select": "id,started_at,ended_at,last_seen_at"}, as_service=True)
        manifest["sessions"] = [x["id"] for x in sessions]
        check(len(sessions) == 1 and sessions[0]["ended_at"], "sitting 1 is ONE ended sitting on the server (%d)" % len(sessions))
        for x in sessions:
            upd = {"__match__": f"id=eq.{x['id']}"}
            for k in ("started_at", "ended_at", "last_seen_at"):
                if x[k]:
                    upd[k] = (datetime.fromisoformat(x[k]) - timedelta(minutes=61)).isoformat()
            acc._ok("shift", *c.write("flashcard_sessions", "PATCH", upd))
        print("  shifted %d sitting(s) back 61 minutes (service role PATCH, by id)" % len(sessions))

        server, port = cdp.serve(REPO, 5611)
        try:
            with cdp.Browser() as br:
                page = br.attach()
                page.send("Emulation.setDeviceMetricsOverride",
                          {"width": 390, "height": 844, "deviceScaleFactor": 2, "mobile": True})
                page.send("Page.addScriptToEvaluateOnNewDocument", {"source": drv.FAKE_VV})
                page.send("Page.addScriptToEvaluateOnNewDocument", {"source": session_js(ref, sess)})
                P = drv.Phone(page, 390, 844, 508, shots)
                P.n = 20
                # the device's own end stamp moves with the server's clock
                page.goto(f"http://127.0.0.1:{port}/student/class.html")
                page.eval("localStorage.setItem('mrbadmusai.fchw.v1.end.%s', String(Date.now() - 61*60*1000))" % aid)

                # ══ SITTING 2 — a reload part-way, then the rest ═══════════
                s = open_deck(P, port, aid)
                check(s["progress"] == "0 of 5 right" and s["secured"] == "%d secured" % secured1,
                      "live: sitting 2 opens at '0 of 5 right', '%d secured' carried over (got %r %r)"
                      % (secured1, s["progress"], s["secured"]))
                P.shot("s2-A-question")
                answer_all(P, upto=2)
                time.sleep(1.5)
                page.eval("window.MRBHomework.flushAll()")
                time.sleep(2.0)
                s = open_deck(P, port, aid)
                check(s["progress"] == "2 of 5 right" and s["back"],
                      "live: reload mid-sitting resumes — '2 of 5 right', ‹ Back offered (got %r)" % s["progress"])
                P.shot("s2-resumed")
                answer_all(P)
                s = wait_for(P, lambda x: x["end2"] is not None, "sitting 2 end")
                check(s["end2"] == "5 of 5 secured so far" and s["done"] == "Done" and s["endHint"] is None,
                      "live: every card secured — %r / %r / %r" % (s["end1"], s["end2"], s["done"]))
                drv.RETIRED and check(not [x for x in drv.RETIRED if x in (s["text"] or "")], "live: no retired words")
                P.shot("s2-Secured")
                P.click('[data-hw="done"]')
                check(not P.st()["open"], "live: Done closes the overlay")
        finally:
            server.shutdown()
            server.server_close()

        # ══ what the server and the teacher see ═══════════════════════════
        st, subs = c.select(None, "assignment_submissions",
                            {"assignment_id": f"eq.{aid}", "student_id": f"eq.{pupil['id']}",
                             "select": "id,score,max_score,status,is_late,submitted_at"}, as_service=True)
        check(len(subs) == 1 and subs[0]["status"] == "complete" and subs[0]["score"] == 5,
              "the ordinary submission row is written (%s)" % subs)
        st, prog = c.rpc(w["tok_t"], "flashcard_progress", {"p_assignment": aid, "p_now": None})
        rows = (prog or {}).get("pupils") or (prog or {}).get("rows") or []
        me = [r for r in rows if r.get("pupil_id") == pupil["id"] or r.get("id") == pupil["id"]]
        result["teacher_progress"] = me[0] if me else prog
        check(st == 200 and me and me[0].get("status") in ("done", "Done", "complete") and me[0].get("secured") == 5,
              "the teacher's flashcard_progress shows the pupil Done, 5 secured (%s)" % (json.dumps(me[0])[:300] if me else str(prog)[:300]))
        st, sess_rows = c.select(None, "flashcard_sessions", {"assignment_id": f"eq.{aid}", "select": "id,ended_at,finished"},
                                 as_service=True)
        result["sittings"] = len(sess_rows)
        check(len(sess_rows) == 2, "two sittings on the server (%d)" % len(sess_rows))
        if a.expect_migration:
            st, rv = c.select(None, "flashcard_reviews", {"assignment_id": f"eq.{aid}", "phase": "eq.review",
                                                         "select": "answer,answer_check"}, as_service=True)
            with_text = [r for r in rv if r.get("answer")]
            result["review_answers"] = rv
            check(st == 200 and len(with_text) == len(rv) and all(r["answer_check"] == "match" for r in with_text),
                  "migrated: every review rating keeps the typed answer and its check (%d rows)" % len(rv))
        json.dump(result, open(os.path.join(shots, "result.json"), "w"), indent=1, default=str)
    finally:
        if not a.keep:
            # the class page may have lazily composed this class's weekly work
            st, extra = c.select(None, "assignments", {"class_id": f"in.({','.join(manifest.get('classes', []))})",
                                                      "select": "id"}, as_service=True) \
                if manifest.get("classes") else (200, [])
            manifest["auto_assignments"] = [x["id"] for x in (extra or [])
                                            if x["id"] not in manifest.get("assignments", [])]
            json.dump(manifest, open(mpath, "w"), indent=1)
            teardown(c, manifest)
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
    print("\n  PASS — pupil flow, live on TEST (%s)" % a.label)


if __name__ == "__main__":
    main()
