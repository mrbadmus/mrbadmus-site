#!/usr/bin/env python3
"""flashcards_sharpen_live.py — the Sharpen run's LIVE proof on TEST
(docs/mrb351/PUPIL-FLOW.md §13.9).

A throwaway pupil does a REVIEW-mode deck of six cards on the REAL class page
(student/class.html served locally; config -> TEST; the backend on
localhost:3000 pointed at TEST) against the REAL TEST database. Nothing is
stubbed but ONE model verdict: TEST has no ANTHROPIC_API_KEY, so its
`flashcard-answer-check` gives no verdict for a multi-word answer; for one card
`window.MRBHomework.modelCheck` is replaced in the page to answer "partial",
so a Nearly hint (which no longer caps anything — 5 Oct) can be seen on the real page against the real database.

On a 390x844 phone (`mobile: true`, a fake `visualViewport` of height 508 for
the keyboard, exactly as flashcard_homework_drive.py does):

  the first pass — Right (newton), Wrong (one wrong word), Nearly (stubbed),
                   Right (joule), I don't know → own words (no cap),
                   No answer (dunno), then the I-don't-know card again;
  its end        — "3 of 6 right", Try again, no session_finish;
  Try again      — only the leftovers, the green chips; a green chip redone
                   (re-rated Nearly); the queue finished; Try again once more
                   for the redone card; all right → Done;
  the database   — ONE flashcard_sessions row for the pass and both retries,
                   ended; flashcard_reviews holds every rating of the redone
                   card;
  a delete       — the throwaway teacher deletes the set through
                   DELETE /api/teacher/set-work/:id WITHOUT the pupil's page
                   reloading; the pupil taps the row → "Your teacher has
                   taken this work down." → "Back to my class" → the row is
                   gone.

    MRB_SHOTS=~/tmp/ks3-gates python3 tools/flashcards_sharpen_live.py

Shots: $MRB_SHOTS/flashcards-sharpen/ (fallback ks3_browser.gate_tmp()).
TEST ONLY: the service key's own `ref` claim is checked before any write.
Throwaway rows are torn down by a SNAPSHOTTED ID LIST, never a predicate.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.request
import uuid
from datetime import datetime, timedelta, timezone

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO)
sys.path.insert(0, os.path.join(REPO, "tools"))
import mrb351_acceptance as acc  # noqa: E402  (Client, env, the TEST guard)
import mrb351_pupil_flow_live as pf  # noqa: E402  (teardown, open_deck, wait_for, session_js)
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
    {"question": "What is the unit of power?", "answer": "The watt (W)"},
]
Q = [c["question"] for c in CARDS]
RIGHT = {Q[0]: "newton", Q[1]: "h2o", Q[2]: "gravity", Q[3]: "joule", Q[4]: "vector", Q[5]: "watt"}
DEFAULT_ENV = "/Users/midebadmus/Documents/GitHub/mrbadmus-backend-worktrees/sharpen/.env"
BACKEND = "http://localhost:3000"


def build(c, manifest, label):
    """pf.build's world, with a REVIEW-mode deck of six cards."""
    ts = int(time.time())
    school, klass, year = str(uuid.uuid4()), str(uuid.uuid4()), str(uuid.uuid4())
    manifest.update({"schools": [school], "classes": [klass], "years": [year]})
    people = {}
    for key in ("t", "p"):
        email = f"mrb351sh-{key}-{label}-{ts}@throwaway.test"
        uid = c.admin_create_user(email, acc.THROWAWAY_PASSWORD)
        manifest.setdefault("users", []).append(uid)
        people[key] = {"id": uid, "email": email}
    manifest["people"] = people
    acc._ok("school", *c.write("schools", "POST", {"id": school, "name": f"MRB351 Sharpen {ts}",
                                                   "code": f"MRB351SH{ts}", "kind": "school",
                                                   "key_stages_supported": ["KS3", "KS4"]}))
    today = datetime.now(timezone.utc).date()
    start = f"{today.year if today.month >= 9 else today.year - 1}-09-01"
    end = f"{int(start[:4]) + 1}-08-31"
    acc._ok("year", *c.write("academic_years", "POST", {"id": year, "school_id": school, "name": "sharpen",
                                                        "start_date": start, "end_date": end,
                                                        "is_current": True}))
    acc._ok("class", *c.write("classes", "POST", {
        "id": klass, "school_id": school, "academic_year_id": year, "name": f"8s/Sc{ts % 10}",
        "key_stage": "KS3", "year_group": 8}))
    acc._ok("t", *c.write("profiles", "PATCH", {"__match__": f"id=eq.{people['t']['id']}",
        "role": "teacher", "school_id": school, "first_name": "Tsh", "last_name": "Mrb351",
        "display_name": "Tsh Mrb351", "username": f"mrb351sht{ts:x}"}))
    acc._ok("p", *c.write("profiles", "PATCH", {"__match__": f"id=eq.{people['p']['id']}",
        "role": "student", "school_id": school, "first_name": "Psh", "last_name": "Mrb351",
        "display_name": "Psh Mrb351", "username": f"mrb351shp{ts:x}",
        "science_pathway": "combined", "tier": "higher"}))
    st, subj = c.select(None, "subjects", {"select": "id,name", "name": "eq.Physics"}, as_service=True)
    acc._ok("class_teachers", *c.write("class_teachers", "POST", {
        "class_id": klass, "teacher_id": people["t"]["id"], "role": "subject_teacher",
        "subject_id": subj[0]["id"]}))
    acc._ok("class_members", *c.write("class_members", "POST", {
        "class_id": klass, "student_id": people["p"]["id"], "joined_via": "admin_added"}))
    tok_t = c.sign_in(people["t"]["email"], acc.THROWAWAY_PASSWORD)
    st, deck = c.rpc(tok_t, "flashcard_deck_save", {
        "p_deck": None, "p_title": "Energy and forces", "p_cards": CARDS,
        "p_meta": {"source_kind": "typed", "subject": "physics"}, "p_finalise": True})
    if st != 200:
        acc.die(f"deck save {st} {deck}")
    manifest["decks"] = [deck["deck_id"]]
    now = datetime.now(timezone.utc)
    st, sw = c.rpc(tok_t, "flashcard_set_work", {
        "p_class_ids": [klass], "p_deck": deck["deck_id"], "p_mode": "review", "p_rule": "secure",
        "p_title": "Energy and forces", "p_release_at": (now - timedelta(minutes=1)).isoformat(),
        "p_due_at": (now + timedelta(days=5)).isoformat(), "p_note": None,
        "p_client_ref": f"mrb351-sh-{label}-{ts}"})
    if st != 200:
        acc.die(f"set work {st} {sw}")
    manifest["assignments"] = list(sw["assignment_ids"])
    return {"school": school, "class": klass, "people": people, "aid": sw["assignment_ids"][0],
            "tok_t": tok_t}


def backend_delete(aid, token):
    req = urllib.request.Request(f"{BACKEND}/api/teacher/set-work/{aid}", method="DELETE",
                                 headers={"Authorization": f"Bearer {token}"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.status, json.loads(r.read().decode() or "{}")
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode()[:300]


# The deck's row on the class page. Its header is a button carrying the
# title (it opens the row); the row's own primary button, under it, navigates
# to `#cards=<id>` (student_rulings.py `primary`). mode "find" returns the
# header's text (or null), "open" presses the header, "go" presses the first
# button after the header that is not the header.
ROW_JS = r"""
(function (title, mode) {
  var bs = Array.prototype.filter.call(document.querySelectorAll('button'), function (b) {
    return !b.closest('[data-port-region="flashcards-overlay"]');
  });
  var i = -1;
  for (var k = 0; k < bs.length; k++) { if ((bs[k].innerText || '').indexOf(title) >= 0) { i = k; break; } }
  if (i < 0) return null;
  if (mode === 'find') return bs[i].innerText.trim();
  if (mode === 'open') { bs[i].click(); return bs[i].innerText.trim(); }
  for (var j = i + 1; j < bs.length; j++) {
    var t = (bs[j].innerText || '').trim();
    if (t && t.indexOf(title) < 0) { bs[j].click(); return t; }
  }
  return null;
})(%s, %s)
"""


def answer(P, text, rating):
    P.type(text)
    P.click('[data-hw="check"]')
    s = pf.wait_for(P, lambda x: x["chip"] != "Checking…", "verdict", timeout=8)
    P.click('[data-hw="%s"]' % rating)
    return s


def enabled_is(s, want):
    return sorted(s["enabled"]) == sorted(want)


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
    shots = os.path.join(os.environ.get("MRB_SHOTS") or cdp.gate_tmp(), "flashcards-sharpen")
    os.makedirs(shots, exist_ok=True)
    manifest = {}
    mpath = os.path.join(shots, "manifest.json")
    result = {}

    class Shots(drv.Phone):
        def shot(self, name):
            import base64
            res = self.page.send("Page.captureScreenshot", {"format": "png", "fromSurface": True})
            with open(os.path.join(shots, name + ".png"), "wb") as fh:
                fh.write(base64.b64decode(res["data"]))

    try:
        w = build(c, manifest, a.label)
        json.dump(manifest, open(mpath, "w"), indent=1)
        aid, pupil = w["aid"], w["people"]["p"]
        st, sess = c._req("POST", f"{url}/auth/v1/token?grant_type=password",
                          {"apikey": c.anon, "Content-Type": "application/json"},
                          {"email": pupil["email"], "password": acc.THROWAWAY_PASSWORD})
        if st != 200:
            acc.die(f"pupil sign-in {st}")
        server, port = cdp.serve(REPO, 5612)
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
                page.send("Page.addScriptToEvaluateOnNewDocument", {"source": pf.session_js(ref, sess)})
                P = Shots(page, 390, 844, 508, shots)

                s = pf.open_deck(P, port, aid)
                check(s["strip"] and s["progress"] == "0 of 6 right" and s["writing"] and s["segs"] == 6,
                      "live: the real class page opens the review deck at '0 of 6 right' (got %r)" % s["progress"])
                order = []

                def front():
                    f = P.st()["front"]
                    order.append(f)
                    return f

                # The first pass. Review mode ranks never-rated cards by position.
                check(front() == Q[0], "card 1 first")
                s = answer(P, "newton", "got_it")
                check(s["chip"] == "Right" and enabled_is(s, ["not_yet", "nearly", "got_it"]),
                      "live: Right → all three enabled (got %r %r)" % (s["chip"], s["enabled"]))

                check(front() == Q[1], "card 2")
                P.type("oxygen")
                P.click('[data-hw="check"]')
                s = P.st()
                check(s["chip"] == "Wrong" and enabled_is(s, ["not_yet", "nearly", "got_it"]) and s["pressed"] == [],
                      "live: Wrong is only a hint → all three enabled, none filled (got %r %r)" % (s["chip"], s["enabled"]))
                P.shot("01-wrong-hint")
                P.click('[data-hw="not_yet"]')

                check(front() == Q[2], "card 3")
                P.q("window.__MC0 = window.MRBHomework.modelCheck;"
                    "window.MRBHomework.modelCheck = function () { return Promise.resolve('partial'); };")
                P.type("the pull of gravity on it")
                P.click('[data-hw="check"]')
                s = pf.wait_for(P, lambda x: x["chip"] == "Nearly", "stubbed verdict", timeout=6)
                check(s["chip"] == "Nearly" and s["pressed"] == [] and enabled_is(s, ["not_yet", "nearly", "got_it"]),
                      "live (ONE verdict stubbed in-page): Nearly → still all three enabled (got %r %r)" % (s["chip"], s["enabled"]))
                P.shot("02-nearly-stubbed-hint")
                P.q("window.MRBHomework.modelCheck = window.__MC0;")
                P.click('[data-hw="nearly"]')

                check(front() == Q[3], "card 4")
                P.type("joule")
                P.click('[data-hw="check"]')
                s = P.st()
                check(s["chip"] == "Right" and s["pressed"] == [] and enabled_is(s, ["not_yet", "nearly", "got_it"]),
                      "live: Right → nothing filled, all three enabled")
                P.shot("03-right-open")
                P.click('[data-hw="got_it"]')

                check(front() == Q[4], "card 5")
                P.click('[data-hw="idk"]')
                P.keyboard(True)
                s = P.st()
                check(s["learn"] and "A vector" in s["learn"] and s["placeholder"] == "Now write it in your own words"
                      and not s["idk"] and s["front"] == Q[4] and s["typing"] == "1",
                      "live: I don't know → the question stays, the answer under it, own-words box, keyboard up")
                P.learn_boxes(508)
                P.shot("04-idk-learn-keyboard")
                P.type("vector")
                P.click('[data-hw="check"]')
                P.keyboard(False)
                s = P.st()
                check(s["chip"] == "Right" and s["pressed"] == [] and enabled_is(s, ["not_yet", "nearly", "got_it"]),
                      "live: own words Right → no cap after I don't know, all three enabled (got %r %r %r)" % (s["chip"], s["pressed"], s["enabled"]))
                P.shot("05-idk-checked-hint")
                P.click('[data-hw="nearly"]')

                check(front() == Q[5], "card 6")
                P.type("dunno")
                P.click('[data-hw="check"]')
                s = P.st()
                check(s["chip"] == "No answer" and enabled_is(s, ["not_yet", "nearly", "got_it"]), "live: 'dunno' → No answer as a hint, all three enabled")
                P.click('[data-hw="not_yet"]')

                s = P.st()
                check(s["front"] == Q[4] and s["idk"] and not s["learn"] and s["progress"] == "2 of 6 right"
                      and s["draft"] == ""
                      and s["segs"] == 6,
                      "live: the I-don't-know card comes back as a plain card, still 6 segments (got %r %r)"
                      % (s["front"], s["progress"]))
                P.shot("06-idk-replay")
                s = answer(P, "vector", "got_it")
                check(s["chip"] == "Right" and "got_it" in s["enabled"], "live: on the replay, Got it is allowed")

                s = pf.wait_for(P, lambda x: x["end1"] is not None, "leftovers")
                check(s["end1"] == "3 of 6 right" and s["retryPass"] == "Try again" and s["end2"] is None
                      and s["done"] is None and s["again"] is None,
                      "live: leftovers — '3 of 6 right' and ONE button Try again (got %r %r)" % (s["end1"], s["retryPass"]))
                P.no_retired("leftovers")
                P.shot("07-end-try-again")

                P.click('[data-hw="retry-pass"]')
                s = P.st()
                check(s["chipsShown"] and len(s["chips"]) == 6 and s["greens"] == 3 and s["progress"] == "3 of 6 right"
                      and s["front"] == Q[1] and s["draft"] == "",
                      "live: Try again — 6 chips, 3 green, '3 of 6 right', the first leftover with an empty box")
                P.shot("08-retry-strip")
                P.click('[data-hw="chip-redo"]')          # the first green: card 1
                s = P.st()
                check(s["front"] == Q[0] and s["draft"] == "newton" and s["back"],
                      "live: a green chip → that card in state A with its earlier answer (got %r %r)" % (s["front"], s["draft"]))
                P.shot("09-redo-green")
                P.type("newton")
                P.click('[data-hw="check"]')
                P.click('[data-hw="nearly"]')              # re-rated below Got it
                s = P.st()
                check(s["front"] == Q[1] and s["progress"] == "2 of 6 right" and s["greens"] == 2,
                      "live: re-rated Nearly → chip grey, back on the queue (got %r %r)" % (s["front"], s["progress"]))
                answer(P, "h2o", "got_it")
                answer(P, "gravity", "got_it")
                answer(P, "watt", "got_it")
                s = pf.wait_for(P, lambda x: x["end1"] is not None, "second leftovers")
                check(s["end1"] == "5 of 6 right" and s["retryPass"] == "Try again", "live: card 1 left → Try again (%r)" % s["end1"])
                P.click('[data-hw="retry-pass"]')
                check(P.st()["front"] == Q[0], "live: the second Try again is only card 1")
                answer(P, "newton", "got_it")
                s = pf.wait_for(P, lambda x: x["end2"] is not None, "all right, settled", timeout=20)
                check(s["end1"] == "6 of 6 right" and s["done"] == "Done" and s["retryPass"] is None
                      and (s["end2"] or "").endswith("of 6 secured so far"),
                      "live: all right → Done, line 2 from the server (got %r %r %r)" % (s["end1"], s["end2"], s["done"]))
                result["end2"] = s["end2"]
                P.no_retired("done")
                P.shot("10-end-done")
                P.click('[data-hw="done"]')
                time.sleep(2.0)
                check(not P.st()["open"], "live: Done closes the overlay")

                # ══ the database ══════════════════════════════════════════
                st, sessions = c.select(None, "flashcard_sessions",
                                        {"assignment_id": f"eq.{aid}", "pupil_id": f"eq.{pupil['id']}",
                                         "select": "id,ended_at"}, as_service=True)
                manifest["sessions"] = [x["id"] for x in sessions or []]
                result["sessions"] = sessions
                check(st == 200 and len(sessions) == 1 and sessions[0]["ended_at"],
                      "DB: ONE flashcard_sessions row for the pass and both retries, ended (%s)" % sessions)
                st, cards = c.select(None, "assignment_flashcards",
                                     {"assignment_id": f"eq.{aid}", "select": "id,question"}, as_service=True)
                c1 = [x["id"] for x in cards or [] if x["question"] == Q[0]]
                st, rv = c.select(None, "flashcard_reviews",
                                  {"assignment_id": f"eq.{aid}", "card_id": f"eq.{c1[0] if c1 else 'x'}",
                                   "select": "rating,rated_at,session_id", "order": "rated_at.asc"}, as_service=True)
                ratings = [x["rating"] for x in rv or []]
                result["card1_ratings"] = ratings
                check(ratings == ["got_it", "nearly", "got_it"],
                      "DB: flashcard_reviews holds every rating of the re-rated card (%s)" % ratings)

                # ══ the teacher deletes it; the pupil's page is NOT reloaded ══
                st, body = backend_delete(aid, w["tok_t"])
                result["delete"] = [st, body]
                check(st == 200 and isinstance(body, dict) and body.get("ok"),
                      "DELETE /api/teacher/set-work/:id as the teacher → 200 (%s %s)" % (st, str(body)[:160]))
                title = json.dumps("Energy and forces")
                label = P.q(ROW_JS % (title, '"find"'))
                check(bool(label), "the pupil's page still lists the deck (loaded before the delete): %r" % label)
                P.q(ROW_JS % (title, '"open"'))
                time.sleep(0.6)
                pressed = P.q(ROW_JS % (title, '"go"'))
                result["row_button"] = pressed
                time.sleep(0.5)
                s = pf.wait_for(P, lambda x: x["gone"] is not None, "taken down", timeout=15)
                check(s["gone"] == "Your teacher has taken this work down." and s["goneBtn"] == "Back to my class"
                      and "Try again" not in (s["text"] or ""),
                      "live: tapping the row → 'Your teacher has taken this work down.' + 'Back to my class' (got %r)"
                      % s["gone"])
                P.shot("11-taken-down")
                P.click('[data-hw="gone"]')
                t0 = time.time()
                while time.time() - t0 < 30:
                    time.sleep(1.0)
                    try:
                        ready = P.q("!!document.querySelector('[data-port-region]') && "
                                    "document.body.innerText.indexOf('Loading') < 0")
                    except Exception:
                        ready = False
                    if ready:
                        break
                time.sleep(3.0)
                gone_row = P.q(ROW_JS % (title, '"find"')) is None
                check(gone_row and "#cards=" not in (P.q("location.href") or ""),
                      "live: Back to my class reloads the page without the fragment, and the deck's row is gone")
                check(not P.st()["open"], "live: no overlay after the reload")
                # the shot shows the work list, where the deck's row was
                P.q("(function(){var m=Array.prototype.filter.call(document.querySelectorAll('body *'),"
                    "function(x){return /TERM SPINE/i.test(x.innerText||'');});"
                    "m.sort(function(a,b){return a.innerText.length-b.innerText.length;});"
                    "if(m[0]) m[0].scrollIntoView({block:'start'});})()")
                time.sleep(0.6)
                P.shot("12-after-delete")
        finally:
            server.shutdown()
            server.server_close()
        json.dump(result, open(os.path.join(shots, "result.json"), "w"), indent=1, default=str)
    finally:
        if not a.keep:
            st, extra = c.select(None, "assignments", {"class_id": f"in.({','.join(manifest.get('classes', []))})",
                                                      "select": "id"}, as_service=True) \
                if manifest.get("classes") else (200, [])
            manifest["auto_assignments"] = [x["id"] for x in (extra or [])
                                            if x["id"] not in manifest.get("assignments", [])]
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
    print("\n  PASS — flashcards sharpen, live on TEST")


if __name__ == "__main__":
    main()
