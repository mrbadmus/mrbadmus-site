#!/usr/bin/env python3
"""sharpen_flashcard_panel_live.py — Sharpen B3/B4/B5/B6, the LIVE proof on TEST.

A throwaway school, class, teacher and two pupils; a make-mode deck of four
cards set to the class. Pupil A does the writing pass for every card (two
Got it, two Not yet) and then, in review, types an answer for card 3 and
rates it Nearly. Pupil B does nothing. Then, as the TEACHER, against the REAL
TEST database:

  · `flashcard_pupil_detail` carries MRB-352's keys (`cards[].shown`,
    `ratings[].answer` / `answer_check`) when the migration is applied, and
    the panel degrades when it is not (`--expect-migration` asserts which);
  · teacher/flashcards.html → the centred per-pupil panel, prev/next, the
    latest written answer from the review rating, Tries, History closed;
  · teacher/student-detail.html → the deck row reads In progress, "N/4
    secured", Breakdown opens the flashcard panel;
  · teacher/class-detail.html → the Students table's Score cell;
  · teacher/classes.html → the card's "N of M in" on the current set.

    MRB_THROWAWAY_PASSWORD=mrb326-throwaway \\
      python3 tools/sharpen_flashcard_panel_live.py --expect-migration

TEST ONLY: the service key's own `ref` claim is checked before any write.
Everything minted is torn down by a SNAPSHOTTED ID LIST, never a predicate.
Screenshots: $MRB_SHOTS/sharpen-live/.
"""
from __future__ import annotations

import argparse
import base64
import json
import os
import sys
import time
import uuid
from datetime import datetime, timedelta, timezone

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO)
sys.path.insert(0, os.path.join(REPO, "tools"))
import mrb351_acceptance as acc  # noqa: E402
import mrb351_pupil_flow_live as pf  # noqa: E402  (teardown, session_js)
import ks3_browser as cdp  # noqa: E402

FAILS = []


def check(ok, what, detail=""):
    print("   %s  %s%s" % ("PASS" if ok else "FAIL", what, ("  - " + str(detail)) if detail else ""))
    if not ok:
        FAILS.append(what)


CARDS = [
    {"question": "What is the unit of force?", "answer": "The newton (N)"},
    {"question": "What is the formula of water?", "answer": "H2O"},
    {"question": "What is weight?", "answer": "The force acting on an object due to gravity"},
    {"question": "What is the unit of energy?", "answer": "The joule (J)"},
]


def build(c, manifest):
    ts = int(time.time())
    school, klass, year = str(uuid.uuid4()), str(uuid.uuid4()), str(uuid.uuid4())
    manifest.update({"schools": [school], "classes": [klass], "years": [year]})
    people = {}
    for key in ("t", "a", "b"):
        email = f"sharpen-{key}-{ts}@throwaway.test"
        uid = c.admin_create_user(email, acc.THROWAWAY_PASSWORD)
        manifest.setdefault("users", []).append(uid)
        people[key] = {"id": uid, "email": email}
    acc._ok("school", *c.write("schools", "POST", {"id": school, "name": f"Sharpen {ts}",
                                                   "code": f"SHARPEN{ts}", "kind": "school",
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
    names = {"t": ("Tess", "Sharpen", "teacher"), "a": ("Ada", "Able", "student"),
             "b": ("Ben", "Bold", "student")}
    for key, (first, last, role) in names.items():
        body = {"__match__": f"id=eq.{people[key]['id']}", "role": role, "school_id": school,
                "first_name": first, "last_name": last, "display_name": f"{first} {last}",
                "username": f"sharpen{key}{ts:x}"}
        if role == "student":
            body.update(science_pathway="combined", tier="higher")
        acc._ok(key, *c.write("profiles", "PATCH", body))
    st, subj = c.select(None, "subjects", {"select": "id,name", "name": "eq.Physics"}, as_service=True)
    acc._ok("class_teachers", *c.write("class_teachers", "POST", {
        "class_id": klass, "teacher_id": people["t"]["id"], "role": "subject_teacher",
        "subject_id": subj[0]["id"]}))
    for key in ("a", "b"):
        acc._ok("class_members", *c.write("class_members", "POST", {
            "class_id": klass, "student_id": people[key]["id"], "joined_via": "admin_added"}))
    tok_t = c.sign_in(people["t"]["email"], acc.THROWAWAY_PASSWORD)
    st, deck = c.rpc(tok_t, "flashcard_deck_save", {
        "p_deck": None, "p_title": "Sharpen deck", "p_cards": CARDS,
        "p_meta": {"source_kind": "typed", "subject": "physics"}, "p_finalise": True})
    if st != 200:
        acc.die(f"deck save {st} {deck}")
    manifest["decks"] = [deck["deck_id"]]
    now = datetime.now(timezone.utc)
    st, sw = c.rpc(tok_t, "flashcard_set_work", {
        "p_class_ids": [klass], "p_deck": deck["deck_id"], "p_mode": "make", "p_rule": "secure",
        "p_title": "Forces flashcards", "p_release_at": (now - timedelta(minutes=2)).isoformat(),
        "p_due_at": (now + timedelta(days=5)).isoformat(), "p_note": None,
        "p_client_ref": f"sharpen-{ts}"})
    if st != 200:
        acc.die(f"set work {st} {sw}")
    manifest["assignments"] = list(sw["assignment_ids"])
    return {"class": klass, "people": people, "aid": sw["assignment_ids"][0], "tok_t": tok_t}


def pupil_sitting(c, w):
    """Pupil A: the writing pass for every card, then one review answer."""
    aid = w["aid"]
    tok = c.sign_in(w["people"]["a"]["email"], acc.THROWAWAY_PASSWORD)
    st, cards = c.select(None, "assignment_flashcards",
                         {"select": "id,position", "assignment_id": f"eq.{aid}", "order": "position"},
                         as_service=True)
    t = datetime.now(timezone.utc) - timedelta(minutes=10)
    ratings = ["got_it", "got_it", "not_yet", "not_yet"]
    ev = []

    def add(**kw):
        nonlocal t
        kw.setdefault("visible", True)
        ev.append(dict(id=str(uuid.uuid4()), at=t.isoformat(), **kw))
        t += timedelta(seconds=4)

    for i, cd in enumerate(cards):
        add(type="card_shown", phase="make", card=cd["id"])
        add(type="answer_submitted", phase="make", card=cd["id"], answer=["newton", "H2O", "mass", "watt"][i])
        add(type="rated", phase="make", card=cd["id"], rating=ratings[i])
    # review of card 3: shown, typed answer, Nearly
    add(type="card_shown", phase="review", card=cards[2]["id"])
    add(type="answer_submitted", phase="review", card=cards[2]["id"], answer="the force of gravity on it")
    add(type="rated", phase="review", card=cards[2]["id"], rating="nearly")
    st, body = acc.run_events(c, tok, aid, ev)
    check(st == 200, "pupil A's sitting recorded by flashcard_record", "%s %s" % (st, str(body)[:200]))
    return cards


def session_for(c, url, email):
    st, sess = c._req("POST", f"{url}/auth/v1/token?grant_type=password",
                      {"apikey": c.anon, "Content-Type": "application/json"},
                      {"email": email, "password": acc.THROWAWAY_PASSWORD})
    if st != 200:
        acc.die(f"sign-in {st}")
    return sess


def shot(p, out, name, w, h):
    y = p.eval("window.scrollY") or 0
    res = p.send("Page.captureScreenshot", {"format": "png", "fromSurface": True,
                 "clip": {"x": 0, "y": y, "width": w, "height": h, "scale": 1}})
    path = os.path.join(out, name)
    open(path, "wb").write(base64.b64decode(res["data"]))
    print("   shot", path)


def wait(p, expr, timeout=40.0):
    end = time.time() + timeout
    while time.time() < end:
        try:
            if p.eval(expr):
                return True
        except cdp.JSError:
            pass
        time.sleep(0.4)
    return False


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--env-file", default="/Users/midebadmus/Documents/GitHub/mrbadmus-backend-worktrees/sharpen/.env")
    ap.add_argument("--expect-migration", action="store_true",
                    help="assert MRB-352's keys ARE present (else assert the degrade)")
    ap.add_argument("--keep", action="store_true")
    a = ap.parse_args()

    env = acc.read_env(a.env_file)
    url, service = env["SUPABASE_URL"], env["SUPABASE_SERVICE_ROLE_KEY"]
    ref = acc.jwt_ref(service)
    if ref == acc.PROD_REF or ref != acc.TEST_REF:
        acc.die(f"refusing: service key ref {ref} is not TEST ({acc.TEST_REF})")
    print(f"credential ref, proven from the key payload: {ref} => TEST")
    c = acc.Client(url, acc.anon_key(), service)
    out = os.path.join(os.path.expanduser(os.environ.get("MRB_SHOTS") or cdp.gate_tmp()), "sharpen-live")
    os.makedirs(out, exist_ok=True)
    manifest = {}
    mpath = os.path.join(out, "manifest.json")
    try:
        w = build(c, manifest)
        json.dump(manifest, open(mpath, "w"), indent=1)
        aid, pa, pb = w["aid"], w["people"]["a"], w["people"]["b"]
        pupil_sitting(c, w)

        # ── the RPC, as the teacher ─────────────────────────────────────
        st, d = c.rpc(w["tok_t"], "flashcard_pupil_detail", {"p_assignment": aid, "p_pupil": pa["id"]})
        check(st == 200 and d and len(d.get("cards", [])) == 4, "flashcard_pupil_detail answers as the teacher", st)
        cards = d.get("cards", []) if isinstance(d, dict) else []
        has_shown = all("shown" in cd for cd in cards)
        rev = [r for cd in cards for r in cd.get("ratings", []) if r.get("phase") == "review"]
        if a.expect_migration:
            check(has_shown and cards[2]["shown"] == 2 and cards[0]["shown"] == 1,
                  "MRB-352: cards[].shown counts card_shown events", [cd.get("shown") for cd in cards])
            check(rev and rev[0].get("answer") == "the force of gravity on it"
                  and rev[0].get("answer_check") in ("match", "partial", "no", "pending"),
                  "MRB-352: a review rating carries its typed answer and check", rev and rev[0])
        else:
            check(not has_shown and all("answer" not in r for r in rev),
                  "pre-migration function: no MRB-352 keys (the degrade branch)")
        st, prog = c.rpc(w["tok_t"], "flashcard_progress", {"p_assignment": aid,
                                                            "p_now": datetime.now(timezone.utc).isoformat()})
        me = [p for p in (prog or {}).get("pupils", []) if p["pupil_id"] == pa["id"]]
        check(me and me[0]["status"] == "in_progress",
              "flashcard_progress: pupil A in progress", me and me[0])
        secured_a = me[0]["secured"] if me else None

        sess = session_for(c, url, w["people"]["t"]["email"])
        server, port = cdp.serve(REPO, 0)
        base = "http://127.0.0.1:%d" % port
        try:
            with cdp.Browser() as br:
                for theme in ("light", "dark"):
                    for vw, vh in ((1440, 900), (390, 844)):
                        tag = "%s-%d" % (theme, vw)
                        p = br.page("about:blank", settle=0.2)
                        p.send("Page.addScriptToEvaluateOnNewDocument", {"source": pf.session_js(ref, sess)})
                        p.send("Page.addScriptToEvaluateOnNewDocument",
                               {"source": "try{localStorage.setItem('mrb-theme','%s')}catch(e){}" % theme})
                        p.set_viewport(vw, vh)
                        # ── flashcards.html → the panel ─────────────────
                        p.goto(base + "/teacher/flashcards.html?assignment=" + aid, settle=1.0)
                        ok = wait(p, "document.querySelectorAll('#fp-table tbody tr.fp-row').length===2")
                        check(ok, "[%s] flashcards page renders the class" % tag,
                              "" if ok else p.eval("document.body.innerText.slice(0,300)"))
                        if not ok:
                            continue
                        head = p.eval("document.getElementById('fp-head').innerText")
                        check("Pupils write the answers" not in head and "Secure" not in head,
                              "[%s] no chips under the title (B1)" % tag)
                        p.eval("document.querySelector('tr[data-pupil=\"%s\"]').click();true" % pa["id"])
                        ok = wait(p, "document.querySelectorAll('[data-fb=\"overlay\"] .fb-card').length===4")
                        check(ok, "[%s] the panel opens on pupil A with four cards" % tag)
                        info = p.eval(r"""(function(){var o=document.querySelector('[data-fb="overlay"]');
                          var c3=o.querySelectorAll('.fb-card')[2];
                          return {title:o.querySelector('.bd-title').textContent,
                            chip:o.querySelector('.fb-status').textContent,
                            verdicts:(o.querySelector('[data-fb="verdicts"]')||{}).textContent||'',
                            c3ans:c3.querySelector('.fb-ans-text').textContent,
                            c3state:c3.querySelector('.fb-state').textContent,
                            c3tries:c3.querySelector('.fb-tries').textContent,
                            histOpen:!!c3.querySelector('details.fb-history[open]'),
                            sub:o.querySelector('.bd-subtitle').textContent,
                            text:o.querySelector('.bd-sheet').innerText};})()""")
                        check(info["title"] == "Ada Able" and info["chip"] == "In progress",
                              "[%s] panel header: pupil and one status chip" % tag, info["title"])
                        if a.expect_migration:
                            check(info["c3ans"] == "the force of gravity on it" and info["c3tries"] == "Tries: 2",
                                  "[%s] card 3: the typed review answer and Tries = shown" % tag,
                                  "%s / %s" % (info["c3ans"], info["c3tries"]))
                        else:
                            check(info["c3ans"] == "mass" and info["c3tries"] == "Tries: 2",
                                  "[%s] card 3 degrade: the make answer, Tries = rated passes" % tag,
                                  "%s / %s" % (info["c3ans"], info["c3tries"]))
                        check(info["c3state"] == "Nearly", "[%s] card 3 state = its latest rating" % tag)
                        check(not info["histOpen"] and "while writing" not in info["text"],
                              "[%s] History closed" % tag)
                        check(info["sub"] == "" and "Pupil 1 of" not in info["text"], "[%s] no Pupil N of M" % tag)
                        shot(p, out, "live-panel-%s.png" % tag, vw, vh)
                        # the table's default order is least progress first, so
                        # Ben (not started) sits BEFORE Ada: press whichever
                        # neighbour carries his name.
                        p.eval("(function(){var o=document.querySelector('[data-fb=\"overlay\"]');"
                               "var b=['prev','next'].map(function(k){return o.querySelector('[data-fb=\"'+k+'\"]');})"
                               ".filter(function(x){return /Ben Bold/.test(x.textContent)&&!x.disabled;})[0];"
                               "if(b)b.click();})();true")
                        wait(p, "document.querySelector('[data-fb=\"overlay\"]').getAttribute('data-fb-student')==='%s'" % pb["id"])
                        time.sleep(1.0)
                        tb = p.eval("document.querySelector('[data-fb=\"overlay\"] .bd-body').innerText")
                        check("hasn't started" in tb, "[%s] prev/next → pupil B, not started" % tag, tb[:120])
                        p.eval("document.querySelector('[data-fb=\"close\"]').click();true")

                        # ── student-detail → the deck row ──────────────
                        p.goto(base + "/teacher/student-detail.html?class=%s&student=%s" % (w["class"], pa["id"]),
                               settle=1.0)
                        ok = wait(p, "/Forces flashcards/.test(document.body.innerText)", 60)
                        check(ok, "[%s] student screen loads the deck row" % tag)
                        row = p.eval(r"""(function(){
                          var h=[...document.querySelectorAll('h2')].find(e=>/history/i.test(e.textContent));
                          if(h){h.scrollIntoView();window.scrollBy(0,-80);}
                          var t=document.body.innerText; var i=t.indexOf('Forces flashcards');
                          return t.slice(i, i+160);})()""")
                        check("In progress" in row.replace("IN PROGRESS", "In progress") and
                              ("%s/4 secured" % secured_a) in row,
                              "[%s] deck row: In progress and %s/4 secured (B4)" % (tag, secured_a), row.replace("\n", " | "))
                        check("Add feedback" not in row, "[%s] no Add feedback before the deck is complete" % tag)
                        time.sleep(0.4)
                        shot(p, out, "live-student-%s.png" % tag, vw, vh)
                        p.eval(r"""(function(){var b=[...document.querySelectorAll('[data-mrb-added="breakdown-open"]')]
                          .find(x=>x.closest('[style*="grid"]') && /Forces flashcards/.test(x.closest('[style*="grid"]').innerText));
                          if(b)b.click();})();true""")
                        ok = wait(p, "!!document.querySelector('[data-fb=\"overlay\"] .fb-card')")
                        check(ok, "[%s] Breakdown on the deck row opens the flashcard panel" % tag)
                        if ok and theme == "light":
                            shot(p, out, "live-student-panel-%s.png" % tag, vw, vh)

                        # ── class-detail → Students table ──────────────
                        p.goto(base + "/teacher/class-detail.html?class=%s" % w["class"], settle=1.0)
                        ok = wait(p, "!!document.querySelector('[data-mrb-cell=\"week-score\"]')", 60)
                        cells = p.eval("Array.prototype.map.call(document.querySelectorAll('[data-mrb-cell=\"week-score\"]'),"
                                       "function(e){return e.textContent;})") if ok else []
                        check(ok and sorted(cells) == sorted(["%s/4 secured" % secured_a, "—"]),
                              "[%s] Students table: Score cells (B5)" % tag, cells)
                        week = p.eval("document.body.innerText")
                        check("In progress" in week, "[%s] THIS WEEK says In progress for the deck pupil" % tag)
                        p.eval(r"""(function(){var h=[...document.querySelectorAll('h2')].find(e=>/^Students$/.test(e.textContent.trim()));
                          if(h){h.scrollIntoView();window.scrollBy(0,-80);}})();true""")
                        time.sleep(0.4)
                        shot(p, out, "live-class-students-%s.png" % tag, vw, vh)

                        # ── classes → the card ─────────────────────────
                        p.goto(base + "/teacher/classes.html", settle=1.0)
                        ok = wait(p, "/0 of 2 in/.test(document.body.innerText)", 60)
                        check(ok, "[%s] My classes card: 0 of 2 in on the current set (B6)" % tag,
                              "" if ok else p.eval("document.body.innerText.slice(0,400)"))
                        shot(p, out, "live-classes-%s.png" % tag, vw, vh)
        finally:
            server.shutdown()
    finally:
        # Anything the pages composed on the throwaway class (lazy weekly
        # work) is snapshotted BY ID here and deleted by that list.
        if manifest.get("classes"):
            st, rows = c.select(None, "assignments", {"select": "id",
                                "class_id": "in.(%s)" % ",".join(manifest["classes"])}, as_service=True)
            extra = [r["id"] for r in (rows or []) if r["id"] not in manifest.get("assignments", [])]
            manifest["auto_assignments"] = extra
            json.dump(manifest, open(mpath, "w"), indent=1)
        if a.keep:
            print("   --keep: manifest at", mpath)
        else:
            pf.teardown(c, manifest)
            print("   torn down by id list:", {k: len(v) for k, v in manifest.items() if isinstance(v, list)})
    if FAILS:
        print("\n❌ sharpen_flashcard_panel_live: %d failure(s)" % len(FAILS))
        for f in FAILS:
            print("   · " + f)
        return 1
    print("\n✅ sharpen_flashcard_panel_live: all checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
