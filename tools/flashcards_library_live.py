#!/usr/bin/env python3
"""flashcards_library_live.py — "Your flashcards" (the library), the LIVE
proof on TEST (docs/mrb351/STAGE-D-PLAN.md §3.6, MRB-352 Stage D2).

A throwaway pupil goes all the way through a REVIEW-mode deck of ten cards on
the REAL class page (student/class.html served locally, config -> TEST, a
local backend pointed at TEST) against the REAL TEST database, and then:

  00  before any card is rated there is no "View your flashcards" button;
  12  after the first pass (every card rated once, two of them wrong) a reload
      shows ONE "View your flashcards" button under the FLASHCARDS card;
  13  the list: one set, the teacher's title, "10 CARDS";
  14  a card, flipped: the model answer and YOUR ANSWER from the pupil's real
      flashcard_reviews.answer;
      rename to "My forces set" → a flashcard_set_names row as the pupil →
  15  reload: the name persists;
      DEGRADE on the real page — every request to flashcard_set_names answers
      exactly as PostgREST does for a table that is not there (404 PGRST205,
      production today): a rename is kept on the device, nothing is written,
      nothing on screen says so; then the table "arrives" (the answer is no
      longer faked) and the device name is written up ONCE and the local
      copy cleared;
  16  the teacher deletes the set (DELETE /api/teacher/set-work/:id) → reload
      → no button; a `#sets` link opens nothing.

  1440×900 shots of 13 and 14 (and dark-theme ones at both sizes).

    MRB_BACKEND_URL=http://localhost:5642 python3 tools/flashcards_library_live.py

Shots: $MRB_SHOTS/flashcards-library/ (fallback ks3_browser.gate_tmp()).
TEST ONLY: the service key's own `ref` claim is checked before any write.
Throwaway rows are torn down by a SNAPSHOTTED ID LIST, never a predicate.
"""
from __future__ import annotations

import argparse
import base64
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
import mrb351_pupil_flow_live as pf  # noqa: E402  (teardown, session_js, wait_for)
import ks3_browser as cdp  # noqa: E402
import flashcard_homework_drive as drv  # noqa: E402  (the phone, the checks, LIB_STATE)

check = drv.check
FAILS = drv.FAILS

TITLE = "Forces flashcards"
CARDS = [
    {"question": "What is the unit of force?", "answer": "The newton (N)"},
    {"question": "What is the formula of water?", "answer": "H2O"},
    {"question": "What is weight?", "answer": "The force acting on an object due to gravity"},
    {"question": "What is the unit of energy?", "answer": "The joule (J)"},
    {"question": "Is velocity a scalar or a vector?", "answer": "A vector"},
    {"question": "What is the unit of power?", "answer": "The watt (W)"},
    {"question": "What is the unit of charge?", "answer": "The coulomb (C)"},
    {"question": "What is the unit of current?", "answer": "The ampere (A)"},
    {"question": "What is the unit of frequency?", "answer": "The hertz (Hz)"},
    {"question": "What is the unit of pressure?", "answer": "The pascal (Pa)"},
]
Q = [c["question"] for c in CARDS]
RIGHT = {Q[0]: "newton", Q[1]: "h2o", Q[2]: "gravity", Q[3]: "joule", Q[4]: "vector", Q[5]: "watt",
         Q[6]: "coulomb", Q[7]: "ampere", Q[8]: "hertz", Q[9]: "pascal"}
WRONG = {Q[3]: "volt", Q[7]: "ohm"}
DEFAULT_ENV = "/Users/midebadmus/Documents/GitHub/mrbadmus-backend-worktrees/sharpen/.env"
NAMES_KEY = "mrbadmusai.fcset.v1.names"

# The names table "is not there": the exact reply PostgREST gives for a
# relation missing from its schema cache. Installed before the SDK loads, so
# the pupil's Supabase client captures the wrapped fetch.
NO_TABLE_JS = r"""
(function () {
  if (!window.__MRB_NO_NAMES_TABLE__) { return; }
  var real = window.fetch;
  window.__NAMES_HITS__ = 0;
  window.fetch = function (input, init) {
    var u = typeof input === "string" ? input : (input && input.url) || "";
    if (u.indexOf("/rest/v1/flashcard_set_names") >= 0) {
      window.__NAMES_HITS__++;
      return Promise.resolve(new Response(JSON.stringify({code: "PGRST205", details: null, hint: null,
        message: "Could not find the table 'public.flashcard_set_names' in the schema cache"}),
        {status: 404, headers: {"Content-Type": "application/json"}}));
    }
    return real.apply(this, arguments);
  };
})();
"""


def build(c, manifest, label):
    """A throwaway world: school, year, KS3 class, teacher, pupil, a
    ten-card REVIEW-mode flashcard homework set by the teacher."""
    ts = int(time.time())
    school, klass, year = str(uuid.uuid4()), str(uuid.uuid4()), str(uuid.uuid4())
    manifest.update({"schools": [school], "classes": [klass], "years": [year]})
    people = {}
    for key in ("t", "p"):
        email = f"mrb352lib-{key}-{label}-{ts}@throwaway.test"
        uid = c.admin_create_user(email, acc.THROWAWAY_PASSWORD)
        manifest.setdefault("users", []).append(uid)
        people[key] = {"id": uid, "email": email}
    manifest["people"] = people
    acc._ok("school", *c.write("schools", "POST", {"id": school, "name": f"MRB352 Library {ts}",
                                                   "code": f"MRB352LB{ts}", "kind": "school",
                                                   "key_stages_supported": ["KS3", "KS4"]}))
    today = datetime.now(timezone.utc).date()
    start = f"{today.year if today.month >= 9 else today.year - 1}-09-01"
    end = f"{int(start[:4]) + 1}-08-31"
    acc._ok("year", *c.write("academic_years", "POST", {"id": year, "school_id": school, "name": "library",
                                                        "start_date": start, "end_date": end,
                                                        "is_current": True}))
    acc._ok("class", *c.write("classes", "POST", {
        "id": klass, "school_id": school, "academic_year_id": year, "name": f"8l/Sc{ts % 10}",
        "key_stage": "KS3", "year_group": 8}))
    acc._ok("t", *c.write("profiles", "PATCH", {"__match__": f"id=eq.{people['t']['id']}",
        "role": "teacher", "school_id": school, "first_name": "Tlb", "last_name": "Mrb352",
        "display_name": "Tlb Mrb352", "username": f"mrb352lbt{ts:x}"}))
    acc._ok("p", *c.write("profiles", "PATCH", {"__match__": f"id=eq.{people['p']['id']}",
        "role": "student", "school_id": school, "first_name": "Plb", "last_name": "Mrb352",
        "display_name": "Plb Mrb352", "username": f"mrb352lbp{ts:x}",
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
        "p_client_ref": f"mrb352-lib-{label}-{ts}"})
    if st != 200:
        acc.die(f"set work {st} {sw}")
    manifest["assignments"] = list(sw["assignment_ids"])
    return {"class": klass, "people": people, "aid": sw["assignment_ids"][0], "tok_t": tok_t}


def backend_delete(backend, aid, token):
    req = urllib.request.Request(f"{backend}/api/teacher/set-work/{aid}", method="DELETE",
                                 headers={"Authorization": f"Bearer {token}"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.status, json.loads(r.read().decode() or "{}")
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode()[:300]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--label", default="run")
    ap.add_argument("--env-file", default=DEFAULT_ENV)
    ap.add_argument("--backend", default=os.environ.get("MRB_BACKEND_URL", "http://localhost:5642"))
    ap.add_argument("--port", type=int, default=5613)
    ap.add_argument("--keep", action="store_true")
    a = ap.parse_args()

    env = acc.read_env(a.env_file)
    url, service = env["SUPABASE_URL"], env["SUPABASE_SERVICE_ROLE_KEY"]
    ref = acc.jwt_ref(service)
    if ref != acc.TEST_REF:
        acc.die(f"refusing: service key ref {ref} is not TEST ({acc.TEST_REF})")
    print(f"credential ref, proven from the key payload: {ref} => TEST")
    c = acc.Client(url, acc.anon_key(), service)
    shots = os.path.join(os.environ.get("MRB_SHOTS") or cdp.gate_tmp(), "flashcards-library")
    os.makedirs(shots, exist_ok=True)
    manifest, result = {}, {}
    mpath = os.path.join(shots, "manifest.json")

    def shot(page, name):
        res = page.send("Page.captureScreenshot", {"format": "png", "fromSurface": True})
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
        base = f"http://127.0.0.1:{a.port}/student/class.html?api={a.backend}"
        server, port = cdp.serve(REPO, a.port)

        def names_rows():
            st, rows = c.select(None, "flashcard_set_names",
                                {"pupil_id": f"eq.{pupil['id']}", "select": "assignment_id,name"},
                                as_service=True)
            return rows if st == 200 else None

        try:
            def open_browser(br, width, height, mobile, no_table=False):
                page = br.attach()
                page.send("Emulation.setDeviceMetricsOverride",
                          {"width": width, "height": height, "deviceScaleFactor": 2 if mobile else 1,
                           "mobile": mobile})
                if mobile:
                    page.send("Page.addScriptToEvaluateOnNewDocument", {"source": drv.FAKE_VV})
                page.send("Page.addScriptToEvaluateOnNewDocument", {"source": pf.session_js(ref, sess)})
                if no_table:
                    page.send("Page.addScriptToEvaluateOnNewDocument",
                              {"source": "window.__MRB_NO_NAMES_TABLE__ = true;" + NO_TABLE_JS})
                return page

            def load(page, hash_="", wait_button=None, timeout=40):
                page.goto("about:blank")
                page.goto(base + hash_)
                t0 = time.time()
                while time.time() - t0 < timeout:
                    time.sleep(0.6)
                    try:
                        mounted = page.eval("!!document.querySelector('[data-bench-surface=\"cards\"]')")
                        lib = page.eval("Array.isArray(window.__MRB_LIBRARY_READY__)")
                    except Exception:
                        continue
                    if mounted and (lib or wait_button is False and time.time() - t0 > 8):
                        break
                time.sleep(1.0)
                return page.eval(drv.LIB_STATE)

            def click(page, sel, t=0.5):
                ok = page.eval("(function(){var e=document.querySelector(%s); if(!e) return false; e.click(); return true;})()"
                               % json.dumps(sel))
                time.sleep(t)
                return ok

            def to_button(page):
                page.eval("(function(){var b=document.querySelector('[data-mrb-library-open]')||"
                          "document.querySelector('[data-bench-surface=\"cards\"]');"
                          "if(b) window.scrollTo(0, Math.max(0, b.getBoundingClientRect().top + scrollY - 260));})()")
                time.sleep(0.4)

            # ══ phone, 390×844 ═══════════════════════════════════════════
            with cdp.Browser() as br:
                page = open_browser(br, 390, 844, True)
                s = load(page, wait_button=False)
                check(s["buttons"] == 0 and page.eval("window.__MRB_LIBRARY_READY__ || []") == [],
                      "live 00: before any card is rated there is no 'View your flashcards' button (got %r)"
                      % s["buttons"])
                to_button(page)
                shot(page, "00-no-button-yet")

                # the first pass through the real homework overlay
                P = drv.Phone(page, 390, 844, 508, None)
                page.goto("about:blank")
                page.goto(base + "#cards=" + aid)
                s0 = pf.wait_for(P, lambda x: x["strip"] and x["writing"], "deck open", timeout=40)
                if not (s0["strip"] and s0["writing"]):
                    print("  [deck] not open: url=%s text=%r errors=%s" % (
                        page.eval("location.href"), (page.eval("document.body.innerText") or "")[:300],
                        page.console_errors()[:5]))
                done = 0
                for _ in range(12):
                    f = P.st()
                    if not f["writing"]:
                        break
                    q = f["front"]
                    P.type(WRONG.get(q) or RIGHT.get(q, "x"))
                    P.click('[data-hw="check"]')
                    pf.wait_for(P, lambda x: x["chip"] not in (None, "Checking…"), "verdict", timeout=8)
                    P.click('[data-hw="not_yet"]' if q in WRONG else '[data-hw="got_it"]')
                    done += 1
                s = pf.wait_for(P, lambda x: x["end1"] is not None, "end of pass", timeout=20)
                check(done == 10 and s["end1"] == "8 of 10 right",
                      "live: the first pass — 10 cards rated, 2 wrong → '8 of 10 right' (got %r after %d)"
                      % (s["end1"], done))
                t0 = time.time()
                while time.time() - t0 < 20:
                    if page.eval("(function(){var e=window.MRBHomework&&window.MRBHomework.active;"
                                 "return !e || !e.pending.length;})()"):
                        break
                    time.sleep(0.5)
                P.click('[data-port-region="flashcards-overlay"] button[title="Close"]')
                time.sleep(1.5)
                st, rv = c.select(None, "flashcard_reviews",
                                  {"assignment_id": f"eq.{aid}", "pupil_id": f"eq.{pupil['id']}",
                                   "select": "card_id,answer,rating"}, as_service=True)
                result["reviews"] = len(rv or [])
                check(st == 200 and len({x["card_id"] for x in rv or []}) == 10,
                      "DB: flashcard_reviews holds a rating for every one of the 10 cards (%d rows)" % len(rv or []))

                # 12 — the button
                s = load(page)
                check(s["buttons"] == 1 and s["inSurface"],
                      "live 12: after the pass, ONE 'View your flashcards' button under the FLASHCARDS card (got %r)"
                      % s["buttons"])
                to_button(page)
                shot(page, "12-library-button")
                y0 = page.eval("scrollY")

                # 13 — the list
                click(page, "[data-mrb-library-open]", 1.5)
                s = page.eval(drv.LIB_STATE)
                check(s["open"] and s["hash"] == "#sets" and s["rows"] == [{"name": TITLE, "meta": "10 CARDS"}],
                      "live 13: one set, the teacher's title, '10 CARDS' (got %r)" % s["rows"])
                shot(page, "13-sets")

                # 14 — a card, flipped, with the pupil's own words from the DB
                click(page, '[data-lib="set-row"]', 1.5)
                s = page.eval(drv.LIB_STATE)
                check(s["front"] == Q[0] and s["pos"] == "1 / 10", "live: the set opens on card 1 of 10 (got %r %r)"
                      % (s["front"], s["pos"]))
                shot(page, "14a-card-front")
                click(page, '[data-lib="card"]', 0.8)
                s = page.eval(drv.LIB_STATE)
                db_ans = [x["answer"] for x in rv or [] if x.get("answer")]
                check(s["back"] == CARDS[0]["answer"] and s["mine"] == "newton" and "newton" in db_ans,
                      "live 14: the model answer, and YOUR ANSWER 'newton' from flashcard_reviews.answer (got %r %r)"
                      % (s["back"], s["mine"]))
                shot(page, "14-card-back")
                for _ in range(3):
                    click(page, '[data-lib="next"]', 0.3)
                click(page, '[data-lib="card"]', 0.8)
                s = page.eval(drv.LIB_STATE)
                check(s["pos"] == "4 / 10" and s["mine"] == "volt" and s["back"] == CARDS[3]["answer"],
                      "live: a card answered wrong shows the model answer with the pupil's own 'volt' beneath (got %r)"
                      % s["mine"])
                shot(page, "14b-wrong-card-back")
                click(page, '[data-lib="shuffle"]', 0.5)
                s = page.eval(drv.LIB_STATE)
                check(s["shuffle"] == "true" and s["pos"] == "1 / 10", "live: Shuffle → pressed, from 1 / 10")
                shot(page, "14c-shuffled")
                click(page, '[data-lib="shuffle"]', 0.5)

                # rename
                click(page, '[data-lib="name"]', 0.4)
                page.eval("document.querySelector('[data-lib=\"name-input\"]').value='My forces set'")
                shot(page, "15a-renaming")
                page.eval("document.querySelector('[data-lib=\"name-input\"]').dispatchEvent("
                          "new KeyboardEvent('keydown',{key:'Enter',bubbles:true}))")
                time.sleep(2.0)
                rows = names_rows()
                result["names_after_rename"] = rows
                check(rows == [{"assignment_id": aid, "name": "My forces set"}],
                      "DB: flashcard_set_names holds the pupil's own name (%s)" % rows)
                s = load(page)
                click(page, "[data-mrb-library-open]", 1.5)
                s = page.eval(drv.LIB_STATE)
                check(s["rows"] and s["rows"][0]["name"] == "My forces set",
                      "live 15: after a reload the name persists (got %r)" % s["rows"])
                shot(page, "15-renamed")
                click(page, '[data-lib="close"]', 0.8)

                # dark
                page.eval("document.documentElement.setAttribute('data-theme','dark')")
                click(page, "[data-mrb-library-open]", 1.2)
                shot(page, "13-dark-sets")
                click(page, '[data-lib="set-row"]', 1.2)
                click(page, '[data-lib="card"]', 0.8)
                shot(page, "14-dark-card-back")
                click(page, '[data-lib="close"]', 0.6)
                page.eval("document.documentElement.removeAttribute('data-theme')")

            # ══ desktop, 1440×900 ════════════════════════════════════════
            with cdp.Browser() as br:
                page = open_browser(br, 1440, 900, False)
                s = load(page)
                check(s["buttons"] == 1, "live 1440: the button is there on a desktop")
                to_button(page)
                y0, cw0 = page.eval("scrollY"), page.eval("document.documentElement.clientWidth")
                shot(page, "12-1440-library-button")
                click(page, "[data-mrb-library-open]", 1.5)
                s = page.eval(drv.LIB_STATE)
                check(s["rows"] and s["rows"][0] == {"name": "My forces set", "meta": "10 CARDS"} and s["cw"] == cw0,
                      "live 1440: the list, the renamed set, nothing behind it changed width (got %r)" % s["rows"])
                shot(page, "13-1440-sets")
                click(page, '[data-lib="set-row"]', 1.5)
                click(page, '[data-lib="card"]', 0.8)
                shot(page, "14-1440-card-back")
                page.eval("document.documentElement.setAttribute('data-theme','dark')")
                time.sleep(0.4)
                shot(page, "14-1440-dark-card-back")
                page.eval("document.documentElement.removeAttribute('data-theme')")
                page.eval("document.dispatchEvent(new KeyboardEvent('keydown',{key:'Escape',bubbles:true}))")
                time.sleep(0.8)
                s = page.eval(drv.LIB_STATE)
                check(not s["open"] and s["hash"] == "" and abs(s["scrollY"] - y0) <= 1,
                      "live 1440: Escape closes, no fragment, the page did not move (scrollY %s → %s)"
                      % (y0, s["scrollY"]))

            # ══ DEGRADE on the real page: the names table is not there ═════
            # first clear the server name, so the device name has somewhere to go
            acc._ok("clear name", *c.write("flashcard_set_names", "DELETE",
                                           {"__match__": f"assignment_id=in.({aid})"}))
            with cdp.Browser() as br:
                page = open_browser(br, 390, 844, True, no_table=True)
                s = load(page)
                click(page, "[data-mrb-library-open]", 1.5)
                s = page.eval(drv.LIB_STATE)
                check(s["rows"] and s["rows"][0]["name"] == TITLE and page.eval("window.__NAMES_HITS__") >= 1,
                      "degrade: the probe hit the absent table and the list shows the teacher's title (got %r)"
                      % s["rows"])
                click(page, '[data-lib="set-row"]', 1.5)
                click(page, '[data-lib="name"]', 0.4)
                page.eval("document.querySelector('[data-lib=\"name-input\"]').value='Forces on my phone'")
                page.eval("document.querySelector('[data-lib=\"name-input\"]').dispatchEvent("
                          "new KeyboardEvent('keydown',{key:'Enter',bubbles:true}))")
                time.sleep(1.5)
                s = page.eval(drv.LIB_STATE)
                stored = page.eval("localStorage.getItem(%s)" % json.dumps(NAMES_KEY))
                rows = names_rows()
                check(s["name"] == "Forces on my phone" and stored and json.loads(stored).get(aid) == "Forces on my phone"
                      and rows == [],
                      "degrade: the rename is kept on the device, nothing reaches the database (%r, %s)" % (stored, rows))
                check(not any(w in s["text"] for w in ("device", "phone,", "saved", "Saved", "offline")),
                      "degrade: nothing on screen says so")
                shot(page, "17-degrade-renamed")
                s = load(page)
                click(page, "[data-mrb-library-open]", 1.5)
                s = page.eval(drv.LIB_STATE)
                check(s["rows"] and s["rows"][0]["name"] == "Forces on my phone",
                      "degrade: the device name survives a reload")
                shot(page, "18-degrade-after-reload")
            with cdp.Browser() as br:
                # the table "arrives" (nothing faked any more). A fresh browser
                # profile has no localStorage, so the device name is carried
                # across exactly as the phone above left it.
                page = open_browser(br, 390, 844, True)
                page.send("Page.addScriptToEvaluateOnNewDocument", {"source":
                          "try{if(location.hostname==='127.0.0.1'&&!sessionStorage.getItem('seeded')){"
                          "localStorage.setItem(%s,%s);sessionStorage.setItem('seeded','1');}}catch(e){}"
                          % (json.dumps(NAMES_KEY), json.dumps(json.dumps({aid: "Forces on my phone"})))})
                s = load(page)
                click(page, "[data-mrb-library-open]", 2.5)
                s = page.eval(drv.LIB_STATE)
                stored = page.eval("localStorage.getItem(%s)" % json.dumps(NAMES_KEY))
                rows = names_rows()
                check(rows == [{"assignment_id": aid, "name": "Forces on my phone"}] and stored is None
                      and s["rows"] and s["rows"][0]["name"] == "Forces on my phone",
                      "the table arrives: the device name is written up once, the local copy cleared (%s, %r)"
                      % (rows, stored))
                shot(page, "19-table-arrived")
                click(page, '[data-lib="close"]', 0.5)

                # ══ 16 — the teacher deletes the set ══════════════════════
                st, body = backend_delete(a.backend, aid, w["tok_t"])
                result["delete"] = [st, str(body)[:200]]
                check(st == 200, "DELETE /api/teacher/set-work/:id as the teacher → 200 (%s)" % st)
                s = load(page, wait_button=False)
                check(s["buttons"] == 0 and page.eval("window.__MRB_LIBRARY_READY__") == [],
                      "live 16: after the delete, a reload shows no 'View your flashcards' button (got %r)"
                      % s["buttons"])
                to_button(page)
                shot(page, "16-after-delete")
                page.eval("location.hash = '#sets'")
                time.sleep(1.5)
                s = page.eval(drv.LIB_STATE)
                check(not s["open"], "live: a '#sets' link after the delete opens nothing")
        finally:
            server.shutdown()
            server.server_close()
        json.dump(result, open(os.path.join(shots, "result.json"), "w"), indent=1, default=str)
    finally:
        if not a.keep:
            if manifest.get("assignments"):
                c.write("flashcard_set_names", "DELETE",
                        {"__match__": f"assignment_id=in.({','.join(manifest['assignments'])})"})
            st, extra = c.select(None, "assignments", {"class_id": f"in.({','.join(manifest.get('classes', []))})",
                                                      "select": "id"}, as_service=True) \
                if manifest.get("classes") else (200, [])
            manifest["auto_assignments"] = [x["id"] for x in (extra or [])
                                            if x["id"] not in manifest.get("assignments", [])]
            json.dump(manifest, open(mpath, "w"), indent=1)
            pf.teardown(c, manifest)
            residue = {}
            for table, col, ids in (("schools", "id", manifest.get("schools", [])),
                                    ("classes", "id", manifest.get("classes", [])),
                                    ("assignments", "id", manifest.get("assignments", [])),
                                    ("flashcard_set_names", "assignment_id", manifest.get("assignments", []))):
                if ids:
                    st, rows = c.select(None, table, {col: f"in.({','.join(ids)})", "select": col},
                                        as_service=True)
                    if rows:
                        residue[table] = len(rows)
            check(not residue, "teardown by snapshotted id list left nothing behind (%s)" % residue)
    print("\n  screenshots: %s" % shots)
    if FAILS:
        print("\n  FAIL — %d check(s)" % len(FAILS))
        sys.exit(1)
    print("\n  PASS — the flashcard library, live on TEST")


if __name__ == "__main__":
    main()
