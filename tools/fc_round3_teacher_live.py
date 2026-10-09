#!/usr/bin/env python3
"""fc_round3_teacher_live.py — Flashcards round 3 (teacher), the LIVE proof on TEST.

EFFORT is not UNDERSTANDING. A throwaway school, class, teacher and three
pupils; a 10-card review-mode deck set to the class. Activity is written
through the real path (`flashcard_record`, as each pupil):

  Ada   presses "I don't know" on cards 1-4 (card 4 twice), types her own
        words after each, then GOT_IT on all ten; her typed answers on cards 5
        and 6 are checked Nearly / Wrong      -> Done, 6 of 10 unsure
  Ben   GOT_IT on all ten with Right answers  -> Done, all confident
  Cal   does nothing                          -> Not started, nothing extra

The model that writes `answer_check` has no key on TEST, so the VERDICTS are
set on `flashcard_reviews.answer_check` by id (service role) after the pupils'
events are recorded — the answers, ratings and IDK events themselves are the
real path's. Then, as the TEACHER, against the real TEST database, it opens
teacher/flashcards.html at 390x844 and 1280x800, light and dark, and asserts
the per-card counts, their order, the three pupil lines and the CSV, and that
a teacher's own client really can SELECT the three tables (the RLS the page
depends on).

    MRB_THROWAWAY_PASSWORD=mrb326-throwaway \\
      python3 tools/fc_round3_teacher_live.py [--env-file PATH-TO-TEST-.env] [--shots DIR]

TEST ONLY: the service key's own `ref` claim is checked before any write.
Everything minted is torn down by a SNAPSHOTTED ID LIST, never a predicate.
Screenshots: r3-teacher-<theme>-<width>.png under gate_tmp()/fc-round3-teacher-live
(outside the repo, MRB-346 rule 5); --shots docs/experience/y-shots refreshes the
committed set on purpose.
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
IDK = "I don't know"
# ⊕ 9 Oct 2026 — this defaulted to docs/experience/y-shots, so every run
# overwrote committed reference images. MRB-346 rule 5: never into the repo by
# default. main() sets it from --shots, else gate_tmp()/fc-round3-teacher-live.
SHOTS = None


def check(ok, what, detail=""):
    print("   %s  %s%s" % ("PASS" if ok else "FAIL", what, ("  - " + str(detail)) if detail else ""))
    if not ok:
        FAILS.append(what)


CARDS = [{"question": "Card %d: what is the unit of quantity %d?" % (i + 1, i + 1),
          "answer": "Unit %d" % (i + 1)} for i in range(10)]


def build(c, manifest):
    ts = int(time.time())
    school, klass, year = str(uuid.uuid4()), str(uuid.uuid4()), str(uuid.uuid4())
    manifest.update({"schools": [school], "classes": [klass], "years": [year]})
    people = {}
    for key in ("t", "a", "b", "c"):
        email = f"r3t-{key}-{ts}@throwaway.test"
        uid = c.admin_create_user(email, acc.THROWAWAY_PASSWORD)
        manifest.setdefault("users", []).append(uid)
        people[key] = {"id": uid, "email": email}
    acc._ok("school", *c.write("schools", "POST", {"id": school, "name": f"R3T {ts}", "code": f"R3T{ts}",
                                                   "kind": "school", "key_stages_supported": ["KS3", "KS4"]}))
    today = datetime.now(timezone.utc).date()
    start = f"{today.year if today.month >= 9 else today.year - 1}-09-01"
    end = f"{int(start[:4]) + 1}-08-31"
    acc._ok("year", *c.write("academic_years", "POST", {"id": year, "school_id": school, "name": "r3t",
                                                        "start_date": start, "end_date": end, "is_current": True}))
    acc._ok("class", *c.write("classes", "POST", {"id": klass, "school_id": school, "academic_year_id": year,
                                                  "name": f"8t/Sc{ts % 10}", "key_stage": "KS3", "year_group": 8}))
    names = {"t": ("Tess", "Round3", "teacher"), "a": ("Ada", "Able", "student"),
             "b": ("Ben", "Bold", "student"), "c": ("Cal", "Cole", "student")}
    for key, (first, last, role) in names.items():
        body = {"__match__": f"id=eq.{people[key]['id']}", "role": role, "school_id": school,
                "first_name": first, "last_name": last, "display_name": f"{first} {last}",
                "username": f"r3t{key}{ts:x}"}
        if role == "student":
            body.update(science_pathway="combined", tier="higher")
        acc._ok(key, *c.write("profiles", "PATCH", body))
    st, subj = c.select(None, "subjects", {"select": "id,name", "name": "eq.Physics"}, as_service=True)
    acc._ok("class_teachers", *c.write("class_teachers", "POST", {
        "class_id": klass, "teacher_id": people["t"]["id"], "role": "subject_teacher", "subject_id": subj[0]["id"]}))
    for key in ("a", "b", "c"):
        acc._ok("class_members", *c.write("class_members", "POST", {
            "class_id": klass, "student_id": people[key]["id"], "joined_via": "admin_added"}))
    tok_t = c.sign_in(people["t"]["email"], acc.THROWAWAY_PASSWORD)
    st, deck = c.rpc(tok_t, "flashcard_deck_save", {
        "p_deck": None, "p_title": "Round 3 deck", "p_cards": CARDS,
        "p_meta": {"source_kind": "typed", "subject": "physics"}, "p_finalise": True})
    if st != 200:
        acc.die(f"deck save {st} {deck}")
    manifest["decks"] = [deck["deck_id"]]
    now = datetime.now(timezone.utc)
    st, sw = c.rpc(tok_t, "flashcard_set_work", {
        "p_class_ids": [klass], "p_deck": deck["deck_id"], "p_mode": "review", "p_rule": "secure",
        "p_title": "Round 3 units", "p_release_at": (now - timedelta(minutes=2)).isoformat(),
        "p_due_at": (now + timedelta(days=5)).isoformat(), "p_note": None, "p_client_ref": f"r3t-{ts}"})
    if st != 200:
        acc.die(f"set work {st} {sw}")
    manifest["assignments"] = list(sw["assignment_ids"])
    return {"class": klass, "people": people, "aid": sw["assignment_ids"][0], "tok_t": tok_t}


def events_for(cards, plan):
    """plan: card index -> {"idk": n_presses, "answer": text, "rating": str}."""
    t = datetime.now(timezone.utc) - timedelta(minutes=20)
    ev = []

    def add(**kw):
        nonlocal t
        kw.setdefault("visible", True)
        ev.append(dict(id=str(uuid.uuid4()), at=t.isoformat(), phase="review", **kw))
        t += timedelta(seconds=4)
    for i, cd in enumerate(cards):
        p = plan[i]
        add(type="card_shown", card=cd["id"])
        for _ in range(p.get("idk", 0)):
            add(type="answer_submitted", card=cd["id"], answer=IDK, idk=True)
        add(type="answer_submitted", card=cd["id"], answer=p["answer"])
        add(type="rated", card=cd["id"], rating=p["rating"])
    return ev


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--env-file", default="/Users/midebadmus/Documents/GitHub/mrbadmus---backend/.env")
    ap.add_argument("--keep", action="store_true")
    ap.add_argument("--shots", default=None,
                    help="screenshot dir (default: gate_tmp()/fc-round3-teacher-live, outside "
                         "the repo; pass docs/experience/y-shots to refresh the committed set)")
    a = ap.parse_args()
    global SHOTS
    SHOTS = os.path.abspath(a.shots) if a.shots else os.path.join(cdp.gate_tmp(), "fc-round3-teacher-live")
    print(f"screenshots -> {SHOTS}")
    env = acc.read_env(a.env_file)
    url, service = env["SUPABASE_URL"], env["SUPABASE_SERVICE_ROLE_KEY"]
    ref = acc.jwt_ref(service)
    if ref == acc.PROD_REF or ref != acc.TEST_REF:
        acc.die(f"refusing: service key ref {ref} is not TEST ({acc.TEST_REF})")
    print(f"credential ref, proven from the key payload: {ref} => TEST")
    c = acc.Client(url, acc.anon_key(), service)
    os.makedirs(SHOTS, exist_ok=True)
    out = os.path.join(os.path.expanduser(os.environ.get("MRB_SHOTS") or cdp.gate_tmp()), "r3-teacher-live")
    os.makedirs(out, exist_ok=True)
    manifest = {}
    mpath = os.path.join(out, "manifest.json")
    try:
        w = build(c, manifest)
        json.dump(manifest, open(mpath, "w"), indent=1)
        aid, pa, pb, pc_ = w["aid"], w["people"]["a"], w["people"]["b"], w["people"]["c"]
        st, cards = c.select(None, "assignment_flashcards",
                             {"select": "id,position,question", "assignment_id": f"eq.{aid}", "order": "position"},
                             as_service=True)
        check(st == 200 and len(cards) == 10, "the deck has ten cards", st)

        # ── Ada: 6 of 10 unsure, all ten got_it ───────────────────────
        plan_a = []
        for i in range(10):
            plan_a.append({"idk": 2 if i == 3 else (1 if i < 4 else 0),
                           "answer": "my words %d" % (i + 1), "rating": "got_it"})
        tok_a = c.sign_in(pa["email"], acc.THROWAWAY_PASSWORD)
        st, body = acc.run_events(c, tok_a, aid, events_for(cards, plan_a))
        check(st == 200, "Ada's sitting recorded by flashcard_record", "%s %s" % (st, str(body)[:200]))
        # ── Ben: all ten got_it, no IDK ───────────────────────────────
        plan_b = [{"answer": "right words %d" % (i + 1), "rating": "got_it"} for i in range(10)]
        tok_b = c.sign_in(pb["email"], acc.THROWAWAY_PASSWORD)
        st, body = acc.run_events(c, tok_b, aid, events_for(cards, plan_b))
        check(st == 200, "Ben's sitting recorded by flashcard_record", "%s %s" % (st, str(body)[:200]))

        # ── verdicts (no model key on TEST): by row id, never a predicate ──
        st, rows = c.select(None, "flashcard_reviews", {"select": "*", "assignment_id": f"eq.{aid}"}, as_service=True)
        check(st == 200 and len(rows) >= 20, "twenty review rows exist (10 per finished pupil)", len(rows or []))
        pos_of = {cd["id"]: cd["position"] for cd in cards}
        patched = 0
        for r in rows or []:
            verdict = "match"
            if r["pupil_id"] == pa["id"] and pos_of.get(r["card_id"]) == 4:
                verdict = "partial"
            if r["pupil_id"] == pa["id"] and pos_of.get(r["card_id"]) == 5:
                verdict = "no"
            s2, _ = c.write("flashcard_reviews", "PATCH", {"__match__": f"id=eq.{r['id']}", "answer_check": verdict})
            patched += 1 if s2 in (200, 204) else 0
        check(patched == len(rows or []), "every review's verdict set by its id", "%s/%s" % (patched, len(rows or [])))

        # ── the RLS the page depends on: a TEACHER's own client reads all three ──
        for table in ("flashcard_events", "flashcard_reviews", "flashcard_pupil_cards"):
            s3, got = c.select(w["tok_t"], table, {"select": "pupil_id", "assignment_id": f"eq.{aid}", "limit": "5"})
            if table == "flashcard_pupil_cards":
                check(s3 == 200, "teacher SELECT %s -> 200 (review mode: no rows expected)" % table, s3)
            else:
                check(s3 == 200 and len(got) > 0, "teacher SELECT %s -> rows (RLS lets a class teacher read)" % table,
                      "%s %s" % (s3, len(got) if isinstance(got, list) else got))
        s4, idk_rows = c.select(w["tok_t"], "flashcard_events",
                                {"select": "pupil_id,card_id", "assignment_id": f"eq.{aid}",
                                 "type": "eq.answer_submitted", "answer": f"eq.{IDK}"})
        check(s4 == 200 and len({(r['pupil_id'], r['card_id']) for r in idk_rows}) == 4
              and len(idk_rows) >= 4, "the IDK events are readable: Ada x4 cards (one pressed twice)",
              "%s rows=%s" % (s4, len(idk_rows) if isinstance(idk_rows, list) else idk_rows))

        s_t, tsess = c._req("POST", f"{url}/auth/v1/token?grant_type=password",
                            {"apikey": c.anon, "Content-Type": "application/json"},
                            {"email": w["people"]["t"]["email"], "password": acc.THROWAWAY_PASSWORD})
        if s_t != 200:
            acc.die(f"teacher sign-in {s_t}")

        server, port = cdp.serve(REPO, 0)
        base = "http://127.0.0.1:%d" % port
        try:
            with cdp.Browser() as br:
                for theme in ("light", "dark"):
                    for vw, vh in ((1280, 800), (390, 844)):
                        tag = "%s-%d" % (theme, vw)
                        p = br.page("about:blank", settle=0.2)
                        p.send("Page.addScriptToEvaluateOnNewDocument", {"source": pf.session_js(ref, tsess)})
                        p.send("Page.addScriptToEvaluateOnNewDocument",
                               {"source": "try{localStorage.setItem('mrb-theme','%s')}catch(e){}" % theme})
                        p.set_viewport(vw, vh)
                        p.goto(base + "/teacher/flashcards.html?assignment=" + aid, settle=1.0)
                        ok = wait(p, "document.querySelectorAll('#fp-table tbody tr.fp-row').length===3")
                        check(ok, "[%s] the page renders three pupils" % tag,
                              "" if ok else p.eval("document.body.innerText.slice(0,300)"))
                        if not ok:
                            continue
                        ok = wait(p, "document.getElementById('fp-body').getAttribute('data-truth')==='ok'", 40)
                        check(ok, "[%s] the understanding read settles OK on the real database" % tag)
                        und = p.eval(UND_ALL)
                        ua, ub, uc = und.get(pa["id"]) or {}, und.get(pb["id"]) or {}, und.get(pc_["id"]) or {}
                        check(ua.get("chip") == "Done" and ua.get("und") == "· 6 of 10 unsure",
                              "[%s] Ada: Done · 6 of 10 unsure" % tag, ua)
                        check(ub.get("chip") == "Done" and ub.get("und") == "· all confident",
                              "[%s] Ben: Done · all confident" % tag, ub)
                        check(uc.get("chip") == "Not started" and uc.get("und") is None,
                              "[%s] Cal: Not started, nothing extra" % tag, uc)
                        rt = p.eval(RT_ALL)
                        ids = [r["no"] for r in (rt or {}).get("rows", [])]
                        check(ids == ["1", "2", "3", "4", "5", "6"],
                              "[%s] reteach rows hardest first: cards 1-4 (don't know) then 5, 6 (Nearly/Wrong)" % tag, ids)
                        rows_ = {r["no"]: r["bits"] for r in (rt or {}).get("rows", [])}
                        check(rows_.get("1") == ["1 don't know", "1 secured anyway"]
                              and rows_.get("4") == ["1 don't know", "1 secured anyway"]
                              and rows_.get("5") == ["1 Nearly/Wrong", "1 secured anyway"]
                              and rows_.get("6") == ["1 Nearly/Wrong", "1 secured anyway"],
                              "[%s] per-card counts (card 4 counted once for two presses)" % tag, rows_)
                        pg = p.eval("document.documentElement.scrollWidth - document.documentElement.clientWidth")
                        check(pg <= 1, "[%s] no horizontal page scroll" % tag, pg)
                        shot(p, os.path.join(SHOTS, "r3-teacher-%s.png" % tag), vw, vh)
                        if theme == "light" and vw == 1280:
                            p.eval("document.getElementById('fp-csv').click(); true")
                            csv = p.eval("window.__MRB_FP_LAST_CSV__")
                            lines = csv["text"].lstrip("﻿").strip().split("\r\n") if csv else []
                            hdr = lines[0].split(",") if lines else []
                            check("Unsure" in hdr, "CSV carries an Unsure column", lines[:1])
                            if "Unsure" in hdr:
                                by = {l.split(",")[0]: l.split(",")[hdr.index("Unsure")] for l in lines[1:]}
                                check(by.get("Ada Able") == "6" and by.get("Ben Bold") == "0",
                                      "CSV: Ada 6, Ben 0", by)
        finally:
            server.shutdown()
    finally:
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
        print("\n❌ fc_round3_teacher_live: %d failure(s)" % len(FAILS))
        for f in FAILS:
            print("   · " + f)
        return 1
    print("\n✅ fc_round3_teacher_live: all checks passed")
    return 0


UND_ALL = r"""(function(){
  var out = {};
  Array.prototype.forEach.call(document.querySelectorAll('#fp-table tbody tr.fp-row'), function(r){
    var st = r.querySelector('td.fp-col-status');
    var chip = st && st.querySelector('.fp-status');
    var u = st && st.querySelector('[data-fp-und]');
    out[r.getAttribute('data-pupil')] = {chip: chip ? chip.textContent : null, und: u ? u.textContent : null};
  });
  return out;
})()"""
RT_ALL = r"""(function(){
  var card = document.getElementById('fp-reteach');
  if (!card) return null;
  return {rows: Array.prototype.map.call(card.querySelectorAll('li.fp-rt-card'), function(li){
    return {no: li.querySelector('.fp-rt-no').textContent,
            bits: Array.prototype.map.call(li.querySelectorAll('.fp-rt-bit'), function(b){return b.textContent;})};})};
})()"""


def shot(p, path, w, h):
    y = p.eval("window.scrollY") or 0
    res = p.send("Page.captureScreenshot", {"format": "png", "fromSurface": True,
                 "clip": {"x": 0, "y": y, "width": w, "height": h, "scale": 1}})
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


if __name__ == "__main__":
    sys.exit(main())
