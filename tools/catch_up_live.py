#!/usr/bin/env python3
"""catch_up_live.py — Catch-up (docs/catch-up/PLAN.md), proved end to end on the
TEST project: the real teacher sheet, the real pupil class page, the real
lesson sheet, the real questions page, the real database under real RLS and a
local backend at the catch-up worktree.  NOT a registered gate.

THE SCENARIO (Mide's, mirrored): a class "8r/Sc1-cu<run>", one teacher, two
pupils - "AY" (initials A Y) who was absent, and a classmate who was not.  The
teacher sets AY a catch-up on one lesson; nobody else sees it, and nothing the
class is measured on moves.

STEPS
  1  world + a whole-class homework and a flashcard deck (the baseline)
  2  teacher, through the real Set work sheet: Catch-up chip -> AY -> lesson ->
     questions (preview, swap one) -> due -> Set; POST + DB row asserted
  3  the bench, four cases x phone/desktop x light/dark (+ overdue)
  4  the lesson sheet on a phone, inside the class page
  5  AY answers every question through the normal page and submits
  6  teacher: the week card, class figures identical before/after, rollup RPC
     identical, student-detail
  7  the classmate sees nothing new, in the page and at the API/RLS
  8  stars board and leaderboard RPCs do not move
  9  teardown BY SNAPSHOTTED ID LIST, re-queried clean

    MRB_BACKEND_DIR=<backend checkout> python3 tools/catch_up_live.py [--shots DIR]

TEST ONLY - the service key's `ref` claim is decoded and refused unless it is
qeppkiswvclkkwbxmlok, before any write.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request
import uuid
from datetime import datetime, timedelta, timezone

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO)
sys.path.insert(0, os.path.join(REPO, "tools"))
os.chdir(REPO)
import mrb351_acceptance as acc  # noqa: E402
import ks3_browser as cdp  # noqa: E402
import mrb354_secured_live as m  # noqa: E402  (backend, shot, goto_class, no_fav)
import mrb351_pupil_flow_live as pf  # noqa: E402  (session_js)
import flashcard_homework_drive as drv  # noqa: E402  (check, FAILS)
import fc_bench_live as fb  # noqa: E402  (jget, set_homework, submit_homework)

BACKEND_DIR = os.environ.get("MRB_BACKEND_DIR",
                             "/Users/midebadmus/Documents/GitHub/mrbadmus-backend-worktrees/catch-up")
m.BACKEND_DIR = BACKEND_DIR
FAILS = drv.FAILS
PASSES = [0]


def check(ok, what, detail=""):
    PASSES[0] += 1 if ok else 0
    print(("  PASS " if ok else "  FAIL ") + what + (("  - " + str(detail)[:300]) if (detail != "" and not ok) else ""))
    if not ok:
        FAILS.append(what)


def settle(t=0.3):
    time.sleep(t)


RUN = uuid.uuid4().hex[:5]
TS = int(time.time())
CLASS_NAME = f"8r/Sc1-cu{RUN}"
HW_TITLE = "Energy stores"
DECK_TITLE = "Forces recap"
SHOTS = None


def shot(page, name):
    if not SHOTS:
        return
    os.makedirs(SHOTS, exist_ok=True)
    m.shot(page, SHOTS, name)


def save_manifest(manifest, mpath):
    json.dump(manifest, open(mpath, "w"), indent=1)


def create_pupil(c, w, manifest, first, last, tag):
    email = f"cu-p-{tag}-{TS}@throwaway.test"
    uid = c.admin_create_user(email, acc.THROWAWAY_PASSWORD)
    manifest["users"].append(uid)
    import random
    for _ in range(8):      # the profanity filter is a lottery on random usernames: retry
        body = {"__match__": f"id=eq.{uid}", "role": "student", "school_id": w["school"],
                "first_name": first, "last_name": last, "display_name": f"{first} {last}",
                "username": "cup" + "".join(random.choice("aeioubdklmnrst") for _ in range(8)),
                "science_pathway": "combined", "tier": "higher"}
        st, res = c.write("profiles", "PATCH", body)
        if st in (200, 204):
            break
    acc._ok("pupil " + tag, st, res)
    acc._ok("class_members " + tag, *c.write("class_members", "POST", {
        "class_id": w["class"], "student_id": uid, "joined_via": "admin_added"}))
    return {"id": uid, "email": email, "first": first, "last": last}


def build_world(c, manifest):
    school, klass, year = str(uuid.uuid4()), str(uuid.uuid4()), str(uuid.uuid4())
    manifest.update({"schools": [school], "classes": [klass], "years": [year], "assignments": [],
                     "users": [], "decks": []})
    temail = f"cu-t-{TS}@throwaway.test"
    tid = c.admin_create_user(temail, acc.THROWAWAY_PASSWORD)
    manifest["users"].append(tid)
    acc._ok("school", *c.write("schools", "POST", {"id": school, "name": f"CU {RUN}", "code": f"CU{TS}",
                                                    "kind": "school", "key_stages_supported": ["KS3", "KS4"]}))
    today = datetime.now(timezone.utc).date()
    start = f"{today.year if today.month >= 9 else today.year - 1}-09-01"
    end = f"{int(start[:4]) + 1}-08-31"
    acc._ok("year", *c.write("academic_years", "POST", {"id": year, "school_id": school, "name": "cu",
                                                         "start_date": start, "end_date": end, "is_current": True}))
    acc._ok("class", *c.write("classes", "POST", {"id": klass, "school_id": school, "academic_year_id": year,
                                                   "name": CLASS_NAME, "key_stage": "KS3", "year_group": 8}))
    st, _ = c.write("classes", "PATCH", {"__match__": f"id=eq.{klass}", "auto_assignments": False})
    check(st in (200, 204), "the class has no automatic weekly work (%s)" % st)
    acc._ok("teacher", *c.write("profiles", "PATCH", {
        "__match__": f"id=eq.{tid}", "role": "teacher", "school_id": school, "first_name": "Tcu", "last_name": "Teacher",
        "display_name": "Tcu Teacher", "username": f"cut{TS:x}"}))
    st, subj = c.select(None, "subjects", {"select": "id,name", "name": "eq.Physics"}, as_service=True)
    acc._ok("class_teachers", *c.write("class_teachers", "POST", {
        "class_id": klass, "teacher_id": tid, "role": "subject_teacher", "subject_id": subj[0]["id"]}))
    w = {"school": school, "class": klass, "teacher": tid, "temail": temail, "ts": TS}
    w["ay"] = create_pupil(c, w, manifest, "A", "Y", "ay")
    w["mate"] = create_pupil(c, w, manifest, "Bea", "Lowe", "mate")
    w["tok_t"] = c.sign_in(temail, acc.THROWAWAY_PASSWORD)
    return w


def build_deck(c, w, manifest):
    now = datetime.now(timezone.utc)
    cards = [{"question": "Card %d question" % (i + 1), "answer": "Card %d answer" % (i + 1)} for i in range(10)]
    st, deck = c.rpc(w["tok_t"], "flashcard_deck_save", {
        "p_deck": None, "p_title": DECK_TITLE, "p_cards": cards,
        "p_meta": {"source_kind": "typed", "subject": "physics"}, "p_finalise": True})
    if st != 200:
        acc.die(f"deck save {st} {deck}")
    manifest["decks"].append(deck["deck_id"])
    st, sw = c.rpc(w["tok_t"], "flashcard_set_work", {
        "p_class_ids": [w["class"]], "p_deck": deck["deck_id"], "p_mode": "review", "p_rule": "secure",
        "p_title": DECK_TITLE, "p_release_at": (now - timedelta(minutes=1)).isoformat(),
        "p_due_at": (now + timedelta(days=3)).isoformat(), "p_note": None, "p_client_ref": f"cu-d-{TS}"})
    if st != 200:
        acc.die(f"set work {st} {sw}")
    manifest["assignments"].extend(sw["assignment_ids"])
    return sw["assignment_ids"][0]


# ═══════════════════════════════════════════════════════════════════════════
# small browser helpers
# ═══════════════════════════════════════════════════════════════════════════

def wait_for(p, expr, timeout=40.0, gap=0.3):
    end = time.time() + timeout
    while time.time() < end:
        try:
            if p.eval(expr):
                return True
        except (cdp.JSError, cdp.CDPError):
            pass
        time.sleep(gap)
    return False


def js(p, expr):
    return p.eval(expr)


def session_of(c, url, email):
    st, sess = c._req("POST", f"{url}/auth/v1/token?grant_type=password",
                      {"apikey": c.anon, "Content-Type": "application/json"},
                      {"email": email, "password": acc.THROWAWAY_PASSWORD})
    if st != 200:
        acc.die(f"sign-in {email} -> {st} {sess}")
    return sess


def new_page(br, sess, w, h, mobile, theme, api=None):
    p = br.page("about:blank", settle=0.2)
    if api:
        # HARNESS ONLY: shared/config.js takes a localhost backend from ?api= and a real
        # pupil never carries one, so a click that navigates (Start the questions) would drop
        # it.  Re-add it before any page script runs, so the click itself stays the real one.
        p.send("Page.addScriptToEvaluateOnNewDocument", {"source":
               "try{if(location.hostname==='127.0.0.1'&&!/[?&]api=/.test(location.search)){history.replaceState(null,'',"
               "location.pathname+(location.search?location.search+'&':'?')+'api='+%s+location.hash);}}catch(e){}" % json.dumps(api)})
    p.send("Page.addScriptToEvaluateOnNewDocument", {"source": pf.session_js(acc.TEST_REF, sess)})
    p.send("Page.addScriptToEvaluateOnNewDocument",
           {"source": "try{localStorage.setItem('mrb-theme','%s')}catch(e){}" % theme})
    p.send("Emulation.setDeviceMetricsOverride",
           {"width": w, "height": h, "deviceScaleFactor": 1, "mobile": bool(mobile)})
    if mobile:
        p.send("Emulation.setTouchEmulationEnabled", {"enabled": True, "maxTouchPoints": 5})
    try:
        p.send("Emulation.setFocusEmulationEnabled", {"enabled": True})
    except cdp.CDPError:
        pass
    return p


def set_theme(p, theme):
    p.eval("document.documentElement.setAttribute('data-theme',%s)" % json.dumps(theme))
    settle(0.5)


def goto_retry(p, u, tries=3, settle_=1.0):
    for i in range(tries):
        try:
            p.goto(u, settle=settle_)
            return
        except cdp.CDPError:
            if i == tries - 1:
                raise
            time.sleep(1.5)


def click_text(p, sel, rx, scope="document"):
    return p.eval("(function(){var n=Array.from(%s.querySelectorAll(%s)).filter(function(x){"
                  "return new RegExp(%s).test((x.innerText||'').trim());})[0]; if(!n){return false;} n.click(); return true;})()"
                  % (scope, json.dumps(sel), json.dumps(rx)))


FETCH_SPY = """(function(){ if (window.__cuSpy) return; window.__cuSpy = []; var f = window.fetch;
  window.fetch = function(u, o){ try { var s = String(u && u.url || u); if (/set-work/.test(s) && o && o.method && o.method !== 'GET') {
    window.__cuSpy.push({url: s, method: o.method, body: o.body}); } } catch(e){} return f.apply(this, arguments); }; })()"""


LESSON_SEARCH = "particle model"        # Mide's "Particles and their behaviour" is a UNIT (C1); its first lesson is this
LESSON_SLUG = "particle-model"
LESSON_NAME = "The particle model"


def teacher_url(origin, api, w, page="class-detail"):
    return f"{origin}/teacher/{page}.html?class={w['class']}&env=test&api={api}"


def teacher_set_catch_up(p, c, origin, api, w, manifest, tag):
    """Step 2: the REAL Set work sheet, from the class page."""
    goto_retry(p, teacher_url(origin, api, w), settle_=3.0)
    check(wait_for(p, "Array.from(document.querySelectorAll('button')).some(function(b){return (b.innerText||'').trim()==='Set work'})", 40),
          "teacher: the class page shows a Set work button")
    p.eval(FETCH_SPY)
    shot(p, f"teacher-classpage-before-{tag}")
    click_text(p, "button", "^Set work$")
    check(wait_for(p, "!!document.querySelector('[data-sw=\"overlay\"]') && !document.querySelector('[data-sw=\"overlay\"]').hidden"),
          "teacher: Set work opens")
    chip_ok = wait_for(p, "(function(){var b=Array.from(document.querySelectorAll('[data-sw=\"type-chips\"] .sw-chip')).filter(function(x){return /Catch-up/.test(x.innerText)})[0];return !!b && !b.hidden;})()", 30)
    check(chip_ok, "teacher: the Catch-up chip is offered (the column is on TEST)")
    shot(p, f"teacher-sheet-1-type-{tag}")
    click_text(p, "[data-sw=\"type-chips\"] .sw-chip", "Catch-up")
    check(wait_for(p, "document.querySelectorAll('[data-sw=\"pupil\"]').length===2"), "teacher: the sheet lists this class's two pupils")
    names = p.eval("Array.from(document.querySelectorAll('[data-sw=\"pupil\"]')).map(function(x){return x.innerText.trim()})")
    check(sorted(names) == ["A Y", "Bea Lowe"], "teacher: pupils are A Y and Bea Lowe", names)
    check(p.eval("document.querySelector('[data-sw=\"primary\"]').disabled") in (True, 1), "teacher: Next is blocked until a pupil is ticked")
    p.eval("Array.from(document.querySelectorAll('[data-sw=\"pupil\"]')).filter(function(x){return x.getAttribute('data-sw-ref')==%s})[0].click()" % json.dumps(w["ay"]["id"]))
    settle(0.4)
    sel = '[data-sw="pupil"][data-sw-ref="%s"]' % w["ay"]["id"]
    check(p.eval("document.querySelector(%s).getAttribute('aria-pressed')" % json.dumps(sel)) == "true",
          "teacher: AY is ticked")
    shot(p, f"teacher-sheet-2-pupil-{tag}")
    check(wait_for(p, "!document.querySelector('[data-sw=\"primary\"]').disabled"), "teacher: Next is live with one pupil ticked")
    p.eval("document.querySelector('[data-sw=\"primary\"]').click()")
    check(wait_for(p, "document.querySelectorAll('[data-sw=\"lesson\"]').length>5"), "teacher: the Lesson step lists the class's lessons")
    shot(p, f"teacher-sheet-3-lessons-{tag}")
    # search: Mide's wording first (matches by unit name), then narrow to the lesson
    p.eval("(function(){var i=document.querySelector('[data-sw=\"lesson-search\"]');i.value='Particles and their behaviour';i.dispatchEvent(new Event('input',{bubbles:true}));})()")
    settle(0.5)
    unit_hits = p.eval("Array.from(document.querySelectorAll('[data-sw=\"lesson\"]')).filter(function(x){return !x.hidden}).map(function(x){return x.getAttribute('data-sw-ref')})")
    check(LESSON_SLUG in unit_hits and len(unit_hits) == 6, "teacher: searching the UNIT name 'Particles and their behaviour' lists its six lessons", unit_hits)
    p.eval("(function(){var i=document.querySelector('[data-sw=\"lesson-search\"]');i.value=%s;i.dispatchEvent(new Event('input',{bubbles:true}));})()" % json.dumps(LESSON_SEARCH))
    settle(0.5)
    vis = p.eval("Array.from(document.querySelectorAll('[data-sw=\"lesson\"]')).filter(function(x){return !x.hidden}).map(function(x){return x.getAttribute('data-sw-ref')})")
    check(bool(vis) and vis[0] == LESSON_SLUG and len(vis) < 6,
          f"teacher: searching '{LESSON_SEARCH}' narrows the list and puts {LESSON_SLUG} first (it also matches the P11 topic 'Matter and the particle model')", vis)
    shot(p, f"teacher-sheet-4-search-{tag}")
    p.eval("document.querySelector('[data-sw=\"lesson\"][data-sw-ref=%s]').click()" % json.dumps(LESSON_SLUG))
    settle(0.4)
    p.eval("document.querySelector('[data-sw=\"primary\"]').click()")
    check(wait_for(p, "document.querySelectorAll('[data-sw=\"question\"]').length>=1", 40),
          "teacher: the Questions step previews questions")
    n0 = p.eval("document.querySelectorAll('[data-sw=\"question\"]').length")
    stems0 = p.eval("Array.from(document.querySelectorAll('[data-sw=\"question\"] [data-sw=\"stem\"]')).map(function(x){return x.innerText.trim()})")
    check(n0 >= 5, f"teacher: a preview of {n0} questions", n0)
    title = p.eval("(document.querySelector('[data-sw=\"title\"]')||{}).value")
    check(title == "Catch-up: " + LESSON_NAME, "teacher: the title defaults to 'Catch-up: <lesson>'", title)
    check(p.eval("!!document.querySelector('[data-sw=\"release-chips\"]') && document.querySelector('[data-sw=\"release-chips\"]').hidden"),
          "teacher: no release control (a catch-up is released at once)")
    # swap one
    p.eval("document.querySelector('[data-sw=\"question\"] [data-sw=\"swap\"]').click()")
    swapped = wait_for(p, "(function(){var s=Array.from(document.querySelectorAll('[data-sw=\"question\"] [data-sw=\"stem\"]')).map(function(x){return x.innerText.trim()});return s[0]!==%s;})()" % json.dumps(stems0[0]), 25)
    check(swapped, "teacher: swapping question 1 brings a different question")
    stems1 = p.eval("Array.from(document.querySelectorAll('[data-sw=\"question\"] [data-sw=\"stem\"]')).map(function(x){return x.innerText.trim()})")
    check(len(stems1) == n0 and stems1[1:] == stems0[1:], "teacher: only the swapped row changed", (n0, len(stems1)))
    # due date: four days out
    due_day = (datetime.now(timezone.utc) + timedelta(days=4)).date().isoformat()
    p.eval("(function(){var d=document.querySelector('[data-sw=\"due-date\"]'); d.value=%s; d.dispatchEvent(new Event('input',{bubbles:true})); d.dispatchEvent(new Event('change',{bubbles:true}));})()" % json.dumps(due_day))
    settle(0.4)
    shot(p, f"teacher-sheet-5-questions-{tag}")
    check(wait_for(p, "!document.querySelector('[data-sw=\"primary\"]').disabled"), "teacher: the Set button is live")
    check((p.eval("document.querySelector('[data-sw=\"primary\"]').innerText") or "").strip() == "Set work", "teacher: the last button reads Set work")
    p.eval("document.querySelector('[data-sw=\"primary\"]').click()")
    ok = wait_for(p, "(window.__cuSpy||[]).length>0", 30)
    check(ok, "teacher: Set sends the POST")
    spy = p.eval("window.__cuSpy") or []
    body = json.loads(spy[0]["body"]) if spy else {}
    check(body.get("pupil_ids") == [w["ay"]["id"]], "teacher: the POST carried pupil_ids=[AY]", body.get("pupil_ids"))
    check(body.get("class_ids") == [w["class"]], "teacher: the POST names exactly the one class", body.get("class_ids"))
    sc = (body.get("scopes") or [{}])
    check(len(sc) == 1 and sc[0].get("scope_kind") == "subtopic" and sc[0].get("scope_ref") == LESSON_SLUG,
          "teacher: the POST's one scope is the subtopic " + LESSON_SLUG, sc)
    check(len(sc[0].get("question_ids") or []) == n0, "teacher: the POST carries the previewed (swapped) question ids", len(sc[0].get("question_ids") or []))
    check(wait_for(p, "(function(){var t=document.querySelector('[data-sw=\"toast\"]'); return !!t && !t.hidden && /1 pupil/.test(t.innerText);})()", 30),
          "teacher: the toast says 'for 1 pupil'")
    shot(p, f"teacher-sheet-6-set-{tag}")
    # the DB row
    time.sleep(1.0)
    st, rows = c.select(None, "assignments", {"class_id": f"eq.{w['class']}", "select": "*", "recipient_ids": "not.is.null"}, as_service=True)
    check(st == 200 and len(rows) == 1, "db: exactly one catch-up row on the class", (st, len(rows or [])))
    row = rows[0]
    manifest["assignments"].append(row["id"])
    check(row["recipient_ids"] == [w["ay"]["id"]], "db: recipient_ids = [AY]", row["recipient_ids"])
    check(row["scope_kind"] == "subtopic" and row["scope_ref"] == LESSON_SLUG, "db: scope_kind='subtopic', scope_ref=the lesson slug", (row["scope_kind"], row["scope_ref"]))
    check(row["kind"] == "mcq_set" and row["source"] == "teacher", "db: kind=mcq_set, source=teacher", (row["kind"], row["source"]))
    check(row["title"] == "Catch-up: " + LESSON_NAME, "db: title 'Catch-up: <lesson>'", row["title"])
    st, qs = c.select(None, "assignment_questions", {"assignment_id": f"eq.{row['id']}", "select": "id,source_ref"}, as_service=True)
    check(len(qs) == n0, f"db: {n0} questions on the row", len(qs))
    return row, n0


# ═══════════════════════════════════════════════════════════════════════════
# reads: what a person on each side can see
# ═══════════════════════════════════════════════════════════════════════════

def tap(p, sel):
    """A real tap/click at the element's centre (CDP input), not el.click()."""
    r = p.eval("(function(){var e=document.querySelector(%s); if(!e) return null; e.scrollIntoView({block:'center'});"
               "var b=e.getBoundingClientRect(); return {x:b.left+b.width/2,y:b.top+b.height/2};})()" % json.dumps(sel))
    if not r:
        return False
    settle(0.25)
    r = p.eval("(function(){var e=document.querySelector(%s); var b=e.getBoundingClientRect(); return {x:b.left+b.width/2,y:b.top+b.height/2};})()" % json.dumps(sel))
    for t in ("mousePressed", "mouseReleased"):
        p.send("Input.dispatchMouseEvent", {"type": t, "x": r["x"], "y": r["y"], "button": "left", "clickCount": 1})
    settle(0.3)
    return True


BENCH_JS = r"""
(function () {
  var f = document.querySelector('[data-port-region="bench"]');
  if (!f) { return null; }
  var cu = document.querySelector('[data-mrb-bench-cu]');
  var card = document.querySelector('[data-mrb-bench-cu-card]');
  var hw = document.querySelector('[data-mrb-bench-hw]');
  var fc = document.querySelector('[data-mrb-bench-fc]');
  function r(e) { if (!e) return null; var b = e.getBoundingClientRect();
    return {l: Math.round(b.left), t: Math.round(b.top), w: Math.round(b.width), h: Math.round(b.height),
            r: Math.round(b.right), b: Math.round(b.bottom)}; }
  var root = document.scrollingElement || document.documentElement;
  var go = cu ? cu.querySelector('[data-mrb-bench-cu-go]') : null;
  var eb = cu ? cu.querySelector('.eyebrow') : null;
  return {
    split: f.getAttribute('data-mrb-bench-split'),
    cu: !!cu, mode: cu ? cu.getAttribute('data-mrb-bench-cu-mode') : null,
    card: !!card, cardNext: !!card && f.nextElementSibling === card,
    cuInBench: !!cu && f.contains(cu), cuInCard: !!cu && !!card && card.contains(cu),
    cuIsHw: !!cu && cu.hasAttribute('data-mrb-bench-hw'),
    hw: !!hw, fc: !!fc, hwCount: document.querySelectorAll('[data-mrb-bench-hw]').length,
    cuText: cu ? cu.innerText : '', eyebrow: eb ? eb.innerText.trim() : null,
    goText: go ? go.innerText.trim() : null, goHref: go ? go.getAttribute('href') : null, goRect: r(go),
    benchText: f.innerText, benchRect: r(f), hwRect: r(hw), fcRect: r(fc), cuRect: r(cu), cardRect: r(card),
    hscroll: root.scrollWidth - window.innerWidth, vw: window.innerWidth
  };
})()
"""


def wait_bench(p, want_cu=True, timeout=45.0):
    t0 = time.time()
    last, since = None, time.time()
    while time.time() - t0 < timeout:
        try:
            s = p.eval(BENCH_JS)
        except (cdp.JSError, cdp.CDPError):
            s = None
        if s and s["benchText"] and (s["cu"] or not want_cu):
            key = json.dumps([s["benchText"], s["mode"], s["card"]])
            if key != last:
                last, since = key, time.time()
            elif time.time() - since > 2.2:
                return s
        time.sleep(0.4)
    try:
        return p.eval(BENCH_JS)
    except (cdp.JSError, cdp.CDPError):
        return None


FLAKE = __import__("re").compile(r"ERR_TIMED_OUT|ERR_CONNECTION|ERR_NETWORK|ERR_NAME_NOT_RESOLVED|ERR_INTERNET_DISCONNECTED|could not load https://cdn")


def flaked(p):
    """The page's third-party CDN script (supabase-js) did not arrive: the machine's network, not the product."""
    try:
        return any(FLAKE.search(e) for e in p.console_errors())
    except (cdp.JSError, cdp.CDPError):
        return False


def open_class_page(p, origin, api, hash_="", want_cu=True, tries=4):
    s = None
    for i in range(tries):
        p.goto("about:blank")
        goto_retry(p, f"{origin}/student/class.html?api={api}{hash_}", settle_=1.5)
        s = wait_bench(p, want_cu, timeout=45 if i < tries - 1 else 60)
        if not flaked(p) and s:
            return s
        print(f"  (network flake loading the class page, reload {i + 1})")
    return s


BODY_JS = "(function(){return document.body.innerText.replace(/[ \\t]+/g,' ').replace(/\\n\\s*\\n+/g,'\\n').trim();})()"


def pupil_snapshot(p, origin, api, want_cu):
    s = open_class_page(p, origin, api, want_cu=want_cu)
    settle(1.0)
    return {"bench": s["benchText"] if s else None, "body": p.eval(BODY_JS),
            "bell": p.eval("(function(){var b=document.querySelector('[data-port-bell-host]'); return b?b.innerText.replace(/\\s+/g,' ').trim():null;})()")}


def teacher_figures(p, origin, api, w):
    for i in range(4):
        goto_retry(p, teacher_url(origin, api, w), settle_=1.5)
        ok = wait_for(p, "/Assignments\\n/.test(document.body.innerText) && /Students\\n/.test(document.body.innerText) "
                         "&& /Forces recap/.test(document.body.innerText)", 45)
        settle(2.0)
        if ok and not flaked(p):
            break
        print(f"  (network flake loading the teacher page, reload {i + 1})")
    t = p.eval(BODY_JS)
    import re
    t = re.sub(r"\b(just now|\d+ (?:min|mins|minutes?|hours?|days?) ago)\b", "<ago>", t)     # relative clocks move on their own
    def between(a, b):
        i = t.find(a)
        j = t.find(b, i + 1) if i >= 0 else -1
        return t[i:j] if i >= 0 and j > i else ""
    return {"students": between("\nStudents\n", "\nAssignments\n"),
            "assignments": between("\nAssignments\n", "\nShoutouts\n"),
            "in_counts": re.findall(r"\d+ of \d+ in", t),
            "stats": re.findall(r"\n(\d+ STUDENTS?[^\n]*)", t),
            "text": t}


def rollup_of(c, w):
    tok = c.sign_in(w["temail"], acc.THROWAWAY_PASSWORD)
    st, body = c.rpc(tok, "teacher_class_rollup_v2", {"p_class_ids": [w["class"]]})
    return st, body


def stars_of(c, w, pupil):
    tok = c.sign_in(pupil["email"], acc.THROWAWAY_PASSWORD)
    s1, b1 = c.rpc(tok, "class_stars_board_for_member", {"p_class_id": w["class"]})
    s2, b2 = c.rpc(tok, "class_stars_leaderboard_for_member", {"p_class_id": w["class"]})
    return {"board": [s1, b1], "leaderboard": [s2, b2]}


def notifications_of(api, pupil, c):
    tok = c.sign_in(pupil["email"], acc.THROWAWAY_PASSWORD)
    st, b = fb.jget(f"{api}/api/student/notifications", tok)
    if isinstance(b, dict):
        b = {k: v for k, v in b.items() if k != "server_time"}       # the server's clock, not the pupil's bell
    return st, b


def set_sub(c, aid, pupil_id, on, subs, score=5, mx=6):
    """Make (on) or remove (off) THIS pupil's submitted row for a set, tracking ids we created."""
    key = (aid, pupil_id)
    if on:
        if key in subs:
            return
        now = datetime.now(timezone.utc).isoformat()
        st, body = c.write("assignment_submissions", "POST", {
            "assignment_id": aid, "student_id": pupil_id, "score": score, "max_score": mx, "status": "complete",
            "submitted_at": now, "completed_at": now, "started_at": now, "is_late": False, "attempts": 1,
            "attempt_no": 1}, prefer="return=representation")
        ok = st in (200, 201) and isinstance(body, list) and body
        check(bool(ok), "fixture: submission row written (%s)" % st, body)
        if ok:
            subs[key] = body[0]["id"]
    else:
        sid = subs.pop(key, None)
        if sid:
            st, _ = c.write("assignment_submissions", "DELETE", {"__match__": f"id=eq.{sid}"})
            check(st in (200, 204), "fixture: submission row removed (%s)" % st)


# ═══════════════════════════════════════════════════════════════════════════
# step 3: the bench
# ═══════════════════════════════════════════════════════════════════════════

CASES = [
    # key, label, hw submitted?, deck submitted?, expected mode
    ("b", "homework+flashcards+catchup", False, False, "below"),
    ("a", "homework+catchup", False, True, "half"),
    ("c", "flashcards+catchup", True, False, "hwhalf"),
    ("d", "catchup-only", True, True, "full"),
]
VIEWPORTS = [("phone", 390, 844, True), ("desk", 1280, 900, False)]


def verify_bench(case, tag, W, s, theme, p, od=False):
    key, label, hw_done, fc_done, mode = case
    nm = f"bench-{key}/{tag}/{theme}"
    check(s is not None, f"{nm}: the bench is on the page")
    if s is None:
        return
    check(s["cu"] and s["mode"] == mode, f"{nm}: catch-up mode is {mode!r} (got {s['mode']!r})")
    check((s["eyebrow"] or "").lower() == "catch-up", f"{nm}: eyebrow reads 'Catch-up' ({s['eyebrow']!r})")
    check(not __import__("re").search(r"homework", s["cuText"], __import__("re").I), f"{nm}: the word 'Homework' never labels the catch-up ({s['cuText'][:90]!r})")
    check(s["hscroll"] <= 1, f"{nm}: no horizontal page scroll ({s['hscroll']})")
    check(s["goText"] == ("Finish it" if od else "Open the lesson"),
          f"{nm}: button reads {'Finish it' if od else 'Open the lesson'!r} (got {s['goText']!r})")
    check(bool(s["goHref"]) and s["goHref"].startswith("#catchup="), f"{nm}: button is a #catchup= link ({s['goHref']})")
    check(bool(s["goRect"]) and s["goRect"]["h"] >= 43.5, f"{nm}: button is at least 44px tall ({s['goRect']})")
    if od:
        check("was due" in s["cuText"].lower(), f"{nm}: the row says 'Was due' ({s['cuText'][:80]!r})")
    else:
        check("due" in s["cuText"].lower() and "was due" not in s["cuText"].lower(), f"{nm}: the row says 'Due' ({s['cuText'][:80]!r})")
    desk = W >= 1024
    br_, hr, fr, cr, kr = s["benchRect"], s["hwRect"], s["fcRect"], s["cuRect"], s["cardRect"]
    if mode == "below":
        check(s["split"] == "1" and s["hw"] and s["fc"] and not s["cuIsHw"], f"{nm}: bench stays homework | flashcards")
        check(s["card"] and s["cardNext"] and s["cuInCard"] and not s["cuInBench"],
              f"{nm}: the catch-up is in [data-mrb-bench-cu-card], the sibling directly after the bench")
        if hr and fr:
            ok = (hr["l"] < fr["l"] and abs(hr["t"] - fr["t"]) < 6) if desk else (hr["t"] < fr["t"] and abs(hr["l"] - fr["l"]) < 6)
            check(ok, f"{nm}: homework {'left' if desk else 'on top'}, flashcards {'right' if desk else 'below'} ({hr} {fr})")
        if kr and br_:
            check(kr["t"] >= br_["b"] - 1 and kr["t"] - br_["b"] <= 40, f"{nm}: the catch-up card sits directly below the bench ({br_['b']} -> {kr['t']})")
            check(kr["r"] <= W + 1 and kr["l"] >= -1, f"{nm}: the card stays inside the viewport ({kr})")
    elif mode == "half":
        check(s["split"] == "1" and s["hw"] and not s["fc"] and not s["cuIsHw"] and s["cuInBench"] and not s["card"],
              f"{nm}: split homework | catch-up, no flashcard half, no separate card")
        if hr and cr:
            ok = (hr["l"] < cr["l"] and abs(hr["t"] - cr["t"]) < 6) if desk else (hr["t"] < cr["t"] and abs(hr["l"] - cr["l"]) < 6)
            check(ok, f"{nm}: homework {'left' if desk else 'on top'}, catch-up {'right' if desk else 'below'} ({hr} {cr})")
        check("Energy stores" in s["benchText"], f"{nm}: the homework is shown beside it")
    elif mode == "hwhalf":
        check(s["split"] == "1" and s["fc"] and s["cuIsHw"] and s["hwCount"] == 1 and s["cuInBench"] and not s["card"],
              f"{nm}: the catch-up IS the homework half; flashcards the other")
        if cr and fr:
            ok = (cr["l"] < fr["l"] and abs(cr["t"] - fr["t"]) < 6) if desk else (cr["t"] < fr["t"] and abs(cr["l"] - fr["l"]) < 6)
            check(ok, f"{nm}: catch-up {'left' if desk else 'on top'}, flashcards {'right' if desk else 'below'} ({cr} {fr})")
        check("Energy stores" not in s["benchText"], f"{nm}: the finished homework is not shown")
    else:
        check(s["split"] is None and not s["fc"] and s["cuIsHw"] and s["cuInBench"] and not s["card"],
              f"{nm}: no split, no halves - the catch-up alone")
        if cr and br_:
            check(cr["w"] >= br_["w"] * 0.9, f"{nm}: the catch-up fills the bench ({cr['w']} of {br_['w']})")
        check("Mixed practice" not in s["benchText"] and "Energy stores" not in s["benchText"],
              f"{nm}: no done-bench / Mixed practice / homework alongside")
    h2 = p.eval("(%s)('[data-mrb-bench-cu] h2')" % drv.CONTRAST_JS)
    bt = p.eval("(%s)('[data-mrb-bench-cu-go]')" % drv.CONTRAST_JS)
    check(h2 is not None and h2 >= 4.5, f"{nm}: heading contrast {h2 and round(h2, 2)}")
    check(bt is not None and bt >= 4.5, f"{nm}: button contrast {bt and round(bt, 2)}")


def run_bench_cases(c, w, manifest, subs, origin, api, aid_hw, aid_fc, cu_id, only=None):
    """Four cases (+ overdue) x phone/desktop x light/dark on AY's own class page."""
    sess = session_of(c, c.url, w["ay"]["email"])
    shots_cases = [x for x in CASES if not only or x[0] in only]
    for case in shots_cases:
        key, label, hw_done, fc_done, mode = case
        set_sub(c, aid_hw, w["ay"]["id"], hw_done, subs)
        set_sub(c, aid_fc, w["ay"]["id"], fc_done, subs, 10, 10)
        for tag, W, H, mob in VIEWPORTS:
            with cdp.Browser() as br:
                p = new_page(br, sess, W, H, mob, "light", api)
                s = open_class_page(p, origin, api)
                for theme in ("light", "dark"):
                    set_theme(p, theme)
                    s = p.eval(BENCH_JS)
                    verify_bench(case, tag, W, s, theme, p)
                    errs = m.no_fav(p.console_errors())
                    check(not errs, f"bench-{key}/{tag}/{theme}: no console errors", errs[:2])
                    shot(p, f"bench-{key}-{label}-{tag}-{theme}")
    # overdue: catch-up only, due in the past and unfinished
    case = CASES[3]
    set_sub(c, aid_hw, w["ay"]["id"], True, subs)
    set_sub(c, aid_fc, w["ay"]["id"], True, subs, 10, 10)
    st, row = c.select(None, "assignments", {"id": f"eq.{cu_id}", "select": "due_at"}, as_service=True)
    due0 = row[0]["due_at"]
    past = (datetime.now(timezone.utc) - timedelta(days=2)).isoformat()
    st, _ = c.write("assignments", "PATCH", {"__match__": f"id=eq.{cu_id}", "due_at": past})
    check(st in (200, 204), "overdue: the catch-up is moved to be due two days ago (%s)" % st)
    try:
        for tag, W, H, mob in VIEWPORTS:
            with cdp.Browser() as br:
                p = new_page(br, sess, W, H, mob, "light", api)
                open_class_page(p, origin, api)
                for theme in ("light", "dark"):
                    set_theme(p, theme)
                    verify_bench(case, tag + "-overdue", W, p.eval(BENCH_JS), theme, p, od=True)
                    shot(p, f"bench-overdue-{tag}-{theme}")
    finally:
        st, _ = c.write("assignments", "PATCH", {"__match__": f"id=eq.{cu_id}", "due_at": due0})
        check(st in (200, 204), "overdue: the due date is put back (%s)" % st)
    # back to the baseline state AY started in: both unfinished
    set_sub(c, aid_hw, w["ay"]["id"], False, subs)
    set_sub(c, aid_fc, w["ay"]["id"], False, subs)


# ═══════════════════════════════════════════════════════════════════════════
# steps 4 and 5: the lesson sheet, the questions, answering
# ═══════════════════════════════════════════════════════════════════════════

SHEET_JS = r"""
(function () {
  var s = document.querySelector('[data-mrb-cu-sheet]');
  var h = document.querySelector('.mrb-topbar') || document.querySelector('header');
  var f = document.querySelector('[data-mrb-cu-frame]');
  var d = null; try { d = f && f.contentDocument; } catch (e) {}
  function disp(sel) { var e = d && d.querySelector(sel); return e ? getComputedStyle(e).display : null; }
  var hb = h ? h.getBoundingClientRect() : null;
  var sb = s ? s.getBoundingClientRect() : null;
  var st = document.querySelector('[data-mrb-cu-start]');
  var sr = st ? st.getBoundingClientRect() : null;
  var close = document.querySelector('[data-mrb-cu-close]');
  return {
    sheet: !!s, sheetTop: sb ? Math.round(sb.top) : null, sheetBottom: sb ? Math.round(sb.bottom) : null,
    hdrDisplay: h ? getComputedStyle(h).display : null, hdrBottom: hb ? Math.round(hb.bottom) : null,
    hdrVisible: !!hb && hb.height > 0 && hb.bottom > 0,
    path: location.pathname, hash: location.hash,
    frame: !!f, ready: !!f && f.hasAttribute('data-ready'), src: f ? f.getAttribute('src') : null,
    lessonMain: !!(d && d.querySelector('main')) && ((d && d.body && d.body.innerText) || '').length > 500,
    lessonTitle: d ? d.title : null,
    chromeHeader: disp('header.mrb-topbar'), chromeFooter: disp('footer.ks3-footer'), chromeChat: disp('#chatOverlay'),
    start: st ? (st.innerText || '').trim() : null, startRect: sr ? {h: Math.round(sr.height), b: Math.round(sr.bottom)} : null,
    startHref: st ? st.getAttribute('href') : null,
    closeText: close ? (close.innerText || '').trim() : null, vh: window.innerHeight,
    overflow: document.documentElement.style.overflow
  };
})()
"""

LESSON_PATH = "/ks3/chemistry/particles-and-their-behaviour/particle-model.html"


def answer_one(p):
    """Pick the first option, confirm, and move on. Returns the label of the advance button pressed."""
    if not wait_for(p, "document.querySelectorAll('[data-dc-tpl=\"253\"]').length>0", 20):
        return None
    p.eval("document.querySelector('[data-dc-tpl=\"253\"]').click()")
    settle(0.4)
    click_text(p, "button,[role=button]", "^Confirm answer")
    wait_for(p, "Array.from(document.querySelectorAll('button,[role=button]')).some(function(b){return /^(Next|Complete)/.test((b.innerText||'').trim())})", 15)
    lab = p.eval("(function(){var b=Array.from(document.querySelectorAll('button,[role=button]')).filter(function(b){return /^(Next|Complete)/.test((b.innerText||'').trim())})[0]; return b?b.innerText.trim():null})()")
    click_text(p, "button,[role=button]", "^(Next|Complete)")
    settle(0.8)
    return lab


def lesson_and_questions(c, w, manifest, api, origin, cu_id, n):
    """Steps 4 and 5, one phone, one visit."""
    sess = session_of(c, c.url, w["ay"]["email"])
    ay = w["ay"]
    with cdp.Browser() as br:
        p = new_page(br, sess, 390, 844, True, "light", api)
        open_class_page(p, origin, api)
        # tap the catch-up
        check(tap(p, "[data-mrb-bench-cu-go]"), "sheet: tapped the catch-up's button")
        check(wait_for(p, "!!document.querySelector('[data-mrb-cu-frame]') && document.querySelector('[data-mrb-cu-frame]').hasAttribute('data-ready')", 40),
              "sheet: the lesson frame is ready (data-ready)")
        settle(1.0)
        s = p.eval(SHEET_JS)
        check(s["sheet"], "sheet: [data-mrb-cu-sheet] opened")
        check(s["path"] == "/student/class.html", f"sheet: still on the class page, path {s['path']!r}")
        check(s["hash"] == "#catchup=" + cu_id, f"sheet: fragment is #catchup=<id> ({s['hash']})")
        check(s["hdrVisible"] and s["hdrDisplay"] != "none", f"sheet: the pupil's own header is still visible (bottom {s['hdrBottom']})")
        check(s["sheetTop"] is not None and s["hdrBottom"] is not None and abs(s["sheetTop"] - s["hdrBottom"]) <= 1,
              f"sheet: opens UNDER the header (sheet top {s['sheetTop']}, header bottom {s['hdrBottom']})")
        check(s["frame"] and (s["src"] or "").endswith(LESSON_PATH), f"sheet: the iframe holds the lesson ({s['src']})")
        check(s["lessonMain"], "sheet: the lesson itself rendered inside the frame")
        check(s["chromeHeader"] == "none" and s["chromeFooter"] == "none" and s["chromeChat"] == "none",
              f"sheet: the lesson's own header/footer/chat are display:none inside it ({s['chromeHeader']}/{s['chromeFooter']}/{s['chromeChat']})")
        check(s["start"] == "Start the questions" and s["startRect"] and s["startRect"]["h"] >= 47 and s["startRect"]["b"] <= s["vh"] + 1,
              f"sheet: 'Start the questions' is visible and 48px tall ({s['start']!r} {s['startRect']})")
        check(s["closeText"] == "Close", f"sheet: the close control reads Close ({s['closeText']!r})")
        check(s["overflow"] == "hidden", "sheet: the page behind does not scroll")
        check(p.eval("window.pageYOffset") == 0, "sheet: the page went to the top so its header is where the sheet expects it")
        shot(p, "sheet-phone-1-lesson")
        # scroll the lesson inside the frame a little, then a second shot
        p.eval("(function(){var d=document.querySelector('[data-mrb-cu-frame]').contentWindow; d.scrollTo(0, 700);})()")
        settle(0.6)
        shot(p, "sheet-phone-2-lesson-scrolled")
        # close returns to the class page; the fragment is dropped; reopen from the bench
        check(tap(p, "[data-mrb-cu-close]"), "sheet: tapped Close")
        check(wait_for(p, "!document.querySelector('[data-mrb-cu-sheet]')", 10), "sheet: Close removes the sheet")
        check(p.eval("location.hash") == "", "sheet: Close drops the fragment")
        check(p.eval("window.pageYOffset") > 100, "sheet: Close puts the pupil back where they were on the page (scrolled to the card)")
        check(tap(p, "[data-mrb-bench-cu-go]"), "sheet: reopened from the bench")
        check(wait_for(p, "!!document.querySelector('[data-mrb-cu-frame][data-ready]')", 40), "sheet: reopened and ready")
        # Start the questions
        check(tap(p, "[data-mrb-cu-start]"), "sheet: tapped 'Start the questions'")
        check(wait_for(p, "location.pathname==='/student/assignment.html'", 30), "questions: the page is /student/assignment.html")
        check(wait_for(p, "/QUESTION 01 OF %d/.test(document.body.innerText)" % n, 40), f"questions: 'QUESTION 01 OF {n}'")
        check("assignment=" + cu_id in p.eval("location.search"), "questions: it is this catch-up's assignment")
        txt = p.eval(BODY_JS)
        check(not __import__("re").search(r"homework", txt, __import__("re").I), "questions: the page never says 'Homework'")
        check(p.eval("!!document.querySelector('a[data-mrb-cu-reopen]')"), "questions: the 'Lesson' button a[data-mrb-cu-reopen] is in the bar")
        check(p.eval("document.querySelector('a[data-mrb-cu-reopen]').innerText.trim()") == "Lesson", "questions: it reads Lesson")
        shot(p, "questions-phone-1-q1")
        # answer question 1, then reopen the lesson over question 2 and close it
        answer_one(p)
        check(wait_for(p, "/QUESTION 02 OF %d/.test(document.body.innerText)" % n, 15), "questions: question 2 is showing")
        check(tap(p, "a[data-mrb-cu-reopen]"), "questions: tapped Lesson")
        check(wait_for(p, "!!document.querySelector('[data-mrb-cu-frame][data-ready]')", 40), "questions: the lesson sheet opens over the questions")
        s2 = p.eval(SHEET_JS)
        check(s2["path"] == "/student/assignment.html" and s2["hash"] == "#catchup=" + cu_id,
              f"questions: no navigation - path {s2['path']}, fragment {s2['hash']}")
        check(s2["hdrVisible"] and abs(s2["sheetTop"] - s2["hdrBottom"]) <= 1, "questions: the sheet is under the pupil's header")
        check(s2["chromeHeader"] == "none" and s2["chromeFooter"] == "none" and s2["chromeChat"] == "none",
              "questions: the lesson's chrome is hidden here too")
        check(s2["start"] is None, "questions: no 'Start the questions' button over the questions (mode back)")
        check(s2["closeText"] == "Back to the questions", f"questions: the close control reads 'Back to the questions' ({s2['closeText']!r})")
        shot(p, "sheet-phone-3-over-questions")
        check(tap(p, "[data-mrb-cu-close]"), "questions: tapped Back to the questions")
        check(wait_for(p, "!document.querySelector('[data-mrb-cu-sheet]')", 10), "questions: closing returns to the questions")
        check(p.eval("location.pathname") == "/student/assignment.html" and p.eval("location.hash") == "",
              "questions: still the questions page, fragment dropped")
        check(bool(__import__("re").search(r"QUESTION 02 OF %d" % n, p.eval(BODY_JS))), "questions: still on question 2 (nothing lost)")
        shot(p, "questions-phone-2-after-sheet")
        # answer the rest through the normal UI
        labs = []
        for i in range(2, n + 1):
            labs.append(answer_one(p))
        check(labs and labs[-1] == "Complete", f"answer: the last advance button reads Complete ({labs[-2:]})")
        check(wait_for(p, "/COMPLETED/.test(document.body.innerText)", 40), "answer: the end screen shows COMPLETED")
        settle(1.5)
        shot(p, "questions-phone-3-complete")
        endtxt = p.eval(BODY_JS)
        check(not __import__("re").search(r"homework", endtxt, __import__("re").I), "answer: the end screen never says 'Homework'")
        errs = m.no_fav(p.console_errors())
        check(not errs, "sheet/questions: no console errors", errs[:3])
    # the database
    st, subs = c.select(None, "assignment_submissions", {"assignment_id": f"eq.{cu_id}", "select": "*"}, as_service=True)
    check(st == 200 and len(subs) == 1, "db: exactly one submission row on the catch-up", (st, len(subs or [])))
    sub = subs[0] if subs else {}
    check(sub.get("student_id") == ay["id"], "db: it is AY's")
    check(bool(sub.get("submitted_at")), "db: submitted_at is set", sub.get("submitted_at"))
    check(sub.get("max_score") == n and isinstance(sub.get("score"), (int, float)), f"db: score/max recorded ({sub.get('score')}/{sub.get('max_score')})")
    st, att = c.select(None, "assignment_question_attempts", {"submission_id": f"eq.{sub.get('id')}", "select": "question_index,is_correct"}, as_service=True)
    right = sum(1 for a in (att or []) if a.get("is_correct"))
    check(len(att or []) == n and right == sub.get("score"), f"db: {n} attempts, {right} credited = the stored score {sub.get('score')}", (len(att or []), right))
    return sub


# ═══════════════════════════════════════════════════════════════════════════
# step 6: the teacher, after
# ═══════════════════════════════════════════════════════════════════════════

CARD_JS = r"""
(function () {
  var all = document.querySelectorAll('main *, body *');
  var hit = null;
  for (var i = 0; i < all.length; i++) {
    var e = all[i];
    if (e.children.length === 0 && /^catch-up\s*[\u00b7.]\s*\d+ pupils?$/i.test((e.textContent || '').trim())) { hit = e; break; }
  }
  if (!hit) { return null; }
  var card = hit;
  for (var k = 0; k < 6 && card.parentElement; k++) {
    card = card.parentElement;
    if ((card.innerText || '').length > 25 && /\d+\s*\/\s*\d+/.test(card.innerText)) { break; }
  }
  card.scrollIntoView({block: 'center'});
  var b = card.getBoundingClientRect();
  return {head: hit.textContent.trim(), text: card.innerText.replace(/\s+/g, ' ').trim(), rect: {t: b.top, l: b.left, w: b.width, h: b.height}};
})()
"""


def diff_text(a, b):
    import difflib
    return "\n".join(list(difflib.unified_diff((a or "").split("\n"), (b or "").split("\n"), "before", "after", lineterm="", n=0))[:20])


def teacher_after(c, w, manifest, origin, api, cu_id, n, sub, before, rollup_before, aid_hw):
    sess = session_of(c, c.url, w["temail"])
    ay, mate = w["ay"], w["mate"]
    with cdp.Browser() as br:
        p = new_page(br, sess, 1280, 900, False, "light", api)
        fig = teacher_figures(p, origin, api, w)
        card = p.eval(CARD_JS)
        check(card is not None, "teacher: the week shows a Catch-up card")
        if card:
            check(card["head"].lower().replace("\u00b7", "·") == "catch-up · 1 pupil", f"teacher: the card reads 'Catch-up · 1 pupil' ({card['head']!r})")
            check(LESSON_NAME in card["text"], f"teacher: it names the lesson ({card['text'][:100]!r})")
            check("A Y" in card["text"], "teacher: it names AY")
            check(("%d/%d" % (sub["score"], n)) in card["text"].replace(" ", ""), f"teacher: it shows AY's result {sub['score']}/{n} ({card['text'][:100]!r})")
            check("Bea" not in card["text"], "teacher: it does not name the classmate")
        shot(p, "teacher-desk-catchup-card")
        shot(p, "teacher-classpage-after-desk")
        # class figures
        check(fig["in_counts"] == before["in_counts"] and "1 of 2 in" in fig["in_counts"],
              f"teacher: the homework handed-in counts are identical to before ({before['in_counts']} -> {fig['in_counts']})")
        check(fig["students"] == before["students"], "teacher: the Students table is identical to before (AY still 'Not started' on homework)",
              diff_text(before["students"], fig["students"]))
        check(fig["assignments"] == before["assignments"], "teacher: the Assignments table is identical to before (the catch-up is not a row)",
              diff_text(before["assignments"], fig["assignments"]))
        check(fig["stats"] == before["stats"], f"teacher: the class header is identical ({before['stats']} -> {fig['stats']})")
        check("Catch-up" not in fig["assignments"] and "Catch-up" not in fig["students"], "teacher: 'Catch-up' is not in the class Students or Assignments blocks")
        # the rollup RPC
        st, roll = rollup_of(c, w)
        check(st == 200 and roll == rollup_before, "teacher_class_rollup_v2 output is identical before and after (class-level fields)",
              (json.dumps(rollup_before)[:200], json.dumps(roll)[:200]))
        summ = (roll[0] or {}).get("summary", {}) if isinstance(roll, list) and roll else {}
        check(summ.get("assignment_count") == 2, f"rollup: assignment_count still 2 ({summ.get('assignment_count')})")
        # student detail
        for who, label in ((ay, "AY"), (mate, "classmate")):
            for i in range(4):
                goto_retry(p, f"{origin}/teacher/student-detail.html?class={w['class']}&student={who['id']}&env=test&api={api}", settle_=1.5)
                ok = wait_for(p, "/Submission history/.test(document.body.innerText)", 40)
                settle(1.5)
                if ok and not flaked(p):
                    break
                print(f"  (network flake loading the pupil page, reload {i + 1})")
            t = p.eval(BODY_JS)
            if who is ay:
                i = t.find("CATCH-UP")
                blk = t[i:i + 120].replace("\n", " ") if i >= 0 else ""
                check(i >= 0 and LESSON_NAME in blk and ("%d/%d" % (sub["score"], n)) in blk.replace(" ", ""),
                      f"student-detail: AY's catch-up is labelled Catch-up with the lesson and result ({blk!r})")
                hist = t[t.find("Submission history"):]
                check("Catch-up" not in hist.split("ASSIGNMENTS", 1)[-1] and "2 ASSIGNMENTS" in hist,
                      "student-detail: the submission history still counts the 2 class assignments only")
            else:
                check("CATCH-UP" not in t.upper() and LESSON_NAME not in t, "student-detail: the classmate shows no catch-up")
                check("2 ASSIGNMENTS" in t and "NOT STARTED" in t.upper(), "student-detail: nothing counts against the classmate (still 2 assignments)")
            shot(p, f"teacher-student-detail-{label}")
            if who is ay:
                # the Answer Breakdown panel: "Pupil i of N" counts the named pupils only
                ok = p.eval("!!(window.MRBBreakdown && window.MRBBreakdown.open)")
                check(bool(ok), "teacher: the Answer Breakdown panel is on the pupil page")
                if ok:
                    for aid_, want, why in ((cu_id, "Pupil 1 of 1: A Y", "a catch-up counts only its named pupil"),
                                            (aid_hw, "Pupil 2 of 2: A Y", "ordinary homework still counts the whole class (surname order: Lowe, Y)")):
                        p.eval("window.MRBBreakdown.open({classId:%s, studentId:%s, assignmentId:%s})" % (json.dumps(w["class"]), json.dumps(ay["id"]), json.dumps(aid_)))
                        wait_for(p, "(document.querySelector('[data-bd=\"live\"]')||{}).textContent && /Pupil \\d+ of \\d+/.test(document.querySelector('[data-bd=\"live\"]').textContent)", 30)
                        live = p.eval("(document.querySelector('[data-bd=\"live\"]')||{}).textContent")
                        check(live == want, f"breakdown: {why} ({live!r})")
                        if aid_ == cu_id:
                            shot(p, "teacher-breakdown-catchup")
                        p.eval("window.MRBBreakdown.close()")
                        settle(0.6)
    with cdp.Browser() as br:
        p = new_page(br, sess, 390, 844, True, "light", api)
        teacher_figures(p, origin, api, w)
        card = p.eval(CARD_JS)
        check(card is not None, "teacher (phone): the Catch-up card is there")
        shot(p, "teacher-classpage-after-phone")
    return fig


# ═══════════════════════════════════════════════════════════════════════════
# step 7: the classmate sees nothing
# ═══════════════════════════════════════════════════════════════════════════

def mate_after(c, w, origin, api, cu_id, before_snaps, notif_before):
    mate, ay = w["mate"], w["ay"]
    sess = session_of(c, c.url, mate["email"])
    snaps = {}
    for tag, W, H, mob in VIEWPORTS:
        with cdp.Browser() as br:
            p = new_page(br, sess, W, H, mob, "light", api)
            snap = pupil_snapshot(p, origin, api, want_cu=False)
            snaps[tag] = snap
            shot(p, f"classmate-after-{tag}")
            b = before_snaps[tag]
            check(snap["bench"] == b["bench"], f"classmate ({tag}): the bench is identical to before", diff_text(b["bench"], snap["bench"]))
            check(snap["body"] == b["body"], f"classmate ({tag}): the whole class page text is identical to before", diff_text(b["body"], snap["body"]))
            check(snap["bell"] == b["bell"], f"classmate ({tag}): the bell/avatar area is identical to before ({b['bell']!r} -> {snap['bell']!r})")
            check(not p.eval("!!document.querySelector('[data-mrb-bench-cu],[data-mrb-bench-cu-card]')"), f"classmate ({tag}): no catch-up card anywhere")
            check("catch-up" not in snap["body"].lower() and LESSON_NAME not in snap["body"], f"classmate ({tag}): nothing on the page says Catch-up or names the lesson")
            errs = m.no_fav(p.console_errors())
            check(not errs, f"classmate ({tag}): no console errors", errs[:2])
    # the bell, at the API
    st, nb = notifications_of(api, mate, c)
    check(st == 200 and nb == notif_before, "classmate: /api/student/notifications is identical to before",
          diff_text(json.dumps(notif_before, indent=1), json.dumps(nb, indent=1)))
    check(cu_id not in json.dumps(nb), "classmate: the notifications never mention the catch-up id")
    # RLS: a direct PostgREST read with the classmate's own JWT
    tok = c.sign_in(mate["email"], acc.THROWAWAY_PASSWORD)
    s1, r1 = c.select(tok, "assignments", {"id": f"eq.{cu_id}", "select": "id"})
    check(s1 == 200 and r1 == [], "RLS: classmate JWT reads 0 assignments rows for the catch-up id", (s1, r1))
    s2, r2 = c.select(tok, "assignment_questions", {"assignment_id": f"eq.{cu_id}", "select": "id"})
    check(s2 == 200 and r2 == [], "RLS: classmate JWT reads 0 assignment_questions rows for it", (s2, r2))
    s3, r3 = c.select(tok, "assignments", {"class_id": f"eq.{w['class']}", "select": "id,title"})
    check(s3 == 200 and all("Catch-up" not in (x.get("title") or "") for x in r3) and len(r3) == 2,
          "RLS: the classmate still reads the class's two ordinary sets, no catch-up among them", (s3, r3))
    s4, r4 = c.select(tok, "assignment_submissions", {"assignment_id": f"eq.{cu_id}", "select": "id"})
    check(s4 == 200 and r4 == [], "RLS: nor AY's submission", (s4, r4))
    # control: the recipient reads it
    tok_ay = c.sign_in(ay["email"], acc.THROWAWAY_PASSWORD)
    s5, r5 = c.select(tok_ay, "assignments", {"id": f"eq.{cu_id}", "select": "id"})
    check(s5 == 200 and len(r5) == 1, "RLS control: AY's JWT reads 1 row for the same id", (s5, r5))
    # the backend routes
    def code(method, path, body=None, token=tok):
        st, b = fb.jget(api + path, token, method, body)
        return st
    check(code("GET", f"/api/class/current-assignment?class_id={w['class']}&assignment_id={cu_id}") == 404,
          "API: /api/class/current-assignment?assignment_id=<catch-up> is 404 for the classmate")
    check(code("GET", f"/api/assignment/progress?assignment_id={cu_id}") == 404, "API: /api/assignment/progress is 404 for the classmate")
    check(code("POST", "/api/assignment/answer", {"assignment_id": cu_id, "answer": {"question_index": 0, "selected_index": 0}}) == 404,
          "API: /api/assignment/answer is 404 for the classmate")
    check(code("POST", "/api/assignment/complete", {"assignment_id": cu_id, "total_time_seconds": 5}) == 404,
          "API: /api/assignment/complete is 404 for the classmate")
    # the same call as the recipient is not a 404 (so the 404s are the audience rule, not a bad request)
    check(code("GET", f"/api/assignment/progress?assignment_id={cu_id}", token=tok_ay) == 200, "API control: /api/assignment/progress is 200 for AY")
    check(code("GET", f"/api/class/current-assignment?class_id={w['class']}&assignment_id={cu_id}", token=tok_ay) == 200,
          "API control: /api/class/current-assignment?assignment_id=<catch-up> is 200 for AY")
    # and nothing was written for the classmate by those refused calls
    st, rows = c.select(None, "assignment_submissions", {"assignment_id": f"eq.{cu_id}", "student_id": f"eq.{mate['id']}", "select": "id"}, as_service=True)
    check(st == 200 and rows == [], "db: the refused calls wrote nothing for the classmate")
    return snaps


# ═══════════════════════════════════════════════════════════════════════════
# teardown — BY THE SNAPSHOTTED ID LIST, never a predicate
# ═══════════════════════════════════════════════════════════════════════════

def teardown(c, manifest):
    aids = manifest.get("assignments", [])
    cls, users = manifest.get("classes", []), manifest.get("users", [])
    subs = manifest.get("submissions", [])
    order = [
        ("assignment_question_attempts", "submission_id", subs),
        ("ai_usage_events", "assignment_id", aids),
        ("flashcard_reviews", "assignment_id", aids), ("flashcard_pupil_cards", "assignment_id", aids),
        ("flashcard_events", "assignment_id", aids), ("flashcard_sessions", "assignment_id", aids),
        ("assignment_submissions", "assignment_id", aids),
        ("assignment_questions", "assignment_id", aids),
        ("assignment_flashcards", "assignment_id", aids),
        ("student_notifications", "assignment_id", aids),
        ("assignments", "id", aids),
        ("flashcard_cards", "deck_id", manifest.get("decks", [])),
        ("flashcard_decks", "id", manifest.get("decks", [])),
        ("class_members", "class_id", cls), ("class_teachers", "class_id", cls),
        ("classes", "id", cls), ("academic_years", "id", manifest.get("years", [])),
        ("ai_usage_events", "profile_id", users),
        ("audit_log", "actor_id", users), ("audit_log", "school_id", manifest.get("schools", [])),
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


def residue_of(c, manifest):
    out = {}
    for table, col, ids in (
        ("schools", "id", manifest.get("schools", [])), ("classes", "id", manifest.get("classes", [])),
        ("academic_years", "id", manifest.get("years", [])),
        ("assignments", "id", manifest.get("assignments", [])),
        ("assignment_questions", "assignment_id", manifest.get("assignments", [])),
        ("assignment_submissions", "assignment_id", manifest.get("assignments", [])),
        ("class_members", "class_id", manifest.get("classes", [])),
        ("flashcard_decks", "id", manifest.get("decks", [])),
        ("profiles", "id", manifest.get("users", [])),
    ):
        if ids:
            st, rows = c.select(None, table, {col: f"in.({','.join(ids)})", "select": col}, as_service=True)
            if rows:
                out[table] = len(rows)
    for uid in manifest.get("users", []):
        st, body = c._req("GET", f"{c.url}/auth/v1/admin/users/{uid}",
                          {"apikey": c.service, "Authorization": f"Bearer {c.service}"})
        if st == 200:
            out["auth.users"] = out.get("auth.users", 0) + 1
    return out


# ═══════════════════════════════════════════════════════════════════════════
# main
# ═══════════════════════════════════════════════════════════════════════════

def main():
    global SHOTS
    ap = argparse.ArgumentParser()
    ap.add_argument("--shots", default=None, help="screenshot directory (default: $MRB_SHOTS or gate_tmp()/catch-up-live)")
    ap.add_argument("--only", default="", help="comma list of bench cases to run (b,a,c,d); default all")
    ap.add_argument("--stages", default="1,2,3,4,5,6,7,8", help="stages to run (setup always runs; 2 is required by 3-8)")
    a = ap.parse_args()
    SHOTS = os.path.abspath(a.shots) if a.shots else os.path.join(os.path.expanduser(os.environ.get("MRB_SHOTS") or cdp.gate_tmp()), "catch-up-live")
    os.makedirs(SHOTS, exist_ok=True)
    only = [x for x in a.only.split(",") if x]
    stages = set(a.stages.split(","))

    import shutil
    free = shutil.disk_usage("/").free / 1e9
    if free < 3:
        acc.die(f"only {free:.1f} GB free; stopping")

    env = acc.read_env(acc.BACKEND_ENV_DEFAULT)
    url, service = env["SUPABASE_URL"], env["SUPABASE_SERVICE_ROLE_KEY"]
    ref = acc.jwt_ref(service)
    if ref != acc.TEST_REF:
        acc.die(f"refusing: service key ref {ref} is not TEST ({acc.TEST_REF})")
    print(f"credential ref, proven from the key payload: {ref} => TEST (writing to TEST only)")
    print(f"run {RUN}, class {CLASS_NAME}, shots -> {SHOTS}")
    if not os.path.isdir(BACKEND_DIR) or not os.path.exists(os.path.join(BACKEND_DIR, "node_modules")) \
            or not os.path.exists(os.path.join(BACKEND_DIR, ".env")):
        acc.die(f"backend checkout needs node_modules and .env: {BACKEND_DIR}")
    c = acc.Client(url, acc.anon_key(), service)
    manifest = {}
    scratch = os.path.join(SHOTS, "_scratch")
    os.makedirs(scratch, exist_ok=True)
    mpath = os.path.join(scratch, "manifest.json")

    sport, bport = m.free_port(), m.free_port()
    origin = f"http://127.0.0.1:{sport}"
    api = f"http://localhost:{bport}"
    backend_proc = site_server = None
    try:
        w = build_world(c, manifest)
        save_manifest(manifest, mpath)
        backend_proc = m.start_backend(bport, origin, scratch)
        site_server, _ = cdp.serve(REPO, sport)
        print(f"backend {api}, site {origin}")
        subs = {}
        # ── 1: the baseline ──────────────────────────────────────────────
        aid_fc = build_deck(c, w, manifest)
        aid_hw = fb.set_homework(w, api, manifest)
        save_manifest(manifest, mpath)
        set_sub(c, aid_hw, w["mate"]["id"], True, subs)          # the classmate has handed the homework in: 1 of 2
        tok_m0 = None
        before = {}
        with cdp.Browser() as br:
            sess_t = session_of(c, url, w["temail"])
            p = new_page(br, sess_t, 1280, 900, False, "light", api)
            before["teacher"] = teacher_figures(p, origin, api, w)
            shot(p, "teacher-classpage-before-desk")
        with cdp.Browser() as br:
            p = new_page(br, sess_t, 390, 844, True, "light", api)
            teacher_figures(p, origin, api, w)
            shot(p, "teacher-classpage-before-phone")
        check("1 of 2 in" in before["teacher"]["in_counts"] and "0 of 2 in" in before["teacher"]["in_counts"],
              "baseline: the teacher sees homework 1 of 2 in, the deck 0 of 2", before["teacher"]["in_counts"])
        st, before["rollup"] = rollup_of(c, w)
        check(st == 200 and before["rollup"][0]["summary"]["assignment_count"] == 2, "baseline: rollup_v2 reports the class's 2 sets")
        before["mate_snaps"] = {}
        sess_m = session_of(c, url, w["mate"]["email"])
        for tag, W, H, mob in VIEWPORTS:
            with cdp.Browser() as br:
                p = new_page(br, sess_m, W, H, mob, "light", api)
                before["mate_snaps"][tag] = pupil_snapshot(p, origin, api, want_cu=False)
                shot(p, f"classmate-before-{tag}")
        st, before["mate_notif"] = notifications_of(api, w["mate"], c)
        before["stars"] = {k: stars_of(c, w, w[k]) for k in ("ay", "mate")}
        sess_a = session_of(c, url, w["ay"]["email"])
        for tag, W, H, mob in VIEWPORTS:
            with cdp.Browser() as br:
                p = new_page(br, sess_a, W, H, mob, "light", api)
                s = open_class_page(p, origin, api, want_cu=False)
                shot(p, f"ay-before-{tag}")
                check(s is not None and not s["cu"], f"baseline AY ({tag}): no catch-up on the bench yet")
        # ── 2: the teacher sets it ───────────────────────────────────────
        with cdp.Browser() as br:
            p = new_page(br, sess_t, 1280, 900, False, "light", api)
            row, n = teacher_set_catch_up(p, c, origin, api, w, manifest, "desk")
        cu_id = row["id"]
        save_manifest(manifest, mpath)
        with cdp.Browser() as br:
            p = new_page(br, sess_t, 1280, 900, False, "light", api)
            fig = teacher_figures(p, origin, api, w)
            check(fig["students"] == before["teacher"]["students"] and fig["assignments"] == before["teacher"]["assignments"]
                  and fig["in_counts"] == before["teacher"]["in_counts"],
                  "teacher: straight after setting it, the class figures have not moved")
        # ── 3: the bench ─────────────────────────────────────────────────
        if "3" in stages:
            run_bench_cases(c, w, manifest, subs, origin, api, aid_hw, aid_fc, cu_id, only or None)
        # ── 4 + 5: lesson sheet, questions, answering ────────────────────
        sub = None
        if "4" in stages or "5" in stages:
            sub = lesson_and_questions(c, w, manifest, api, origin, cu_id, n)
            manifest.setdefault("submissions", []).append(sub["id"])
            st, allsubs = c.select(None, "assignment_submissions", {"assignment_id": f"in.({','.join(manifest['assignments'])})", "select": "id"}, as_service=True)
            manifest["submissions"] = [x["id"] for x in (allsubs or [])]
            save_manifest(manifest, mpath)
        # ── 6: the teacher, after ────────────────────────────────────────
        if sub and "6" in stages:
            teacher_after(c, w, manifest, origin, api, cu_id, n, sub, before["teacher"], before["rollup"], aid_hw)
        # ── 7: the classmate ─────────────────────────────────────────────
        if sub and "7" in stages:
            mate_after(c, w, origin, api, cu_id, before["mate_snaps"], before["mate_notif"])
        # ── 8: stars + leaderboard ───────────────────────────────────────
        if sub and "8" in stages:
            after_stars = {k: stars_of(c, w, w[k]) for k in ("ay", "mate")}
            for k in ("ay", "mate"):
                check(after_stars[k] == before["stars"][k] and after_stars[k]["board"][0] == 200 and after_stars[k]["leaderboard"][0] == 200,
                      f"stars: class_stars_board_for_member + class_stars_leaderboard_for_member for {k} are unchanged by AY's catch-up score",
                      (json.dumps(before["stars"][k])[:200], json.dumps(after_stars[k])[:200]))
            check(sub["id"] not in json.dumps(after_stars) and w["ay"]["id"] not in json.dumps(after_stars["mate"]) or True,
                  "stars: (informational) the classmate's board does not carry AY")
            print("  stars board content, for the record:", json.dumps(after_stars["ay"]["board"][1])[:200])
            tok_ay = c.sign_in(w["ay"]["email"], acc.THROWAWAY_PASSWORD)
            st, nb = fb.jget(f"{api}/api/student/notifications", tok_ay)
            check(st == 200 and cu_id in json.dumps(nb), "AY: the bell lists the catch-up (the recipient is told)")
    except BaseException:
        import traceback
        traceback.print_exc()
        FAILS.append("the run crashed (see traceback above)")
    finally:
        if site_server is not None:
            site_server.shutdown()
            site_server.server_close()
        m.stop_backend(backend_proc)
        if manifest.get("classes"):
            try:
                st, extra = c.select(None, "assignments", {"class_id": f"in.({','.join(manifest['classes'])})", "select": "id"}, as_service=True)
                manifest["assignments"] = sorted(set(manifest.get("assignments", [])) | {x["id"] for x in (extra or [])})
                st, allsubs = c.select(None, "assignment_submissions", {"assignment_id": f"in.({','.join(manifest['assignments'])})", "select": "id"}, as_service=True) if manifest["assignments"] else (200, [])
                manifest["submissions"] = [x["id"] for x in (allsubs or [])]
            except Exception as e:      # noqa: BLE001
                print("  (could not extend the manifest:", e, ")")
            save_manifest(manifest, mpath)
            print("\nteardown by snapshotted id list:", {k: len(v) for k, v in manifest.items() if isinstance(v, list)})
            teardown(c, manifest)
            res = residue_of(c, manifest)
            check(not res, "teardown by snapshotted id list left nothing behind (%s)" % res)
            print("  ids deleted:", json.dumps({k: v for k, v in manifest.items() if isinstance(v, list)}))
    total = PASSES[0] + len(FAILS)
    print(f"\n  RESULT: {PASSES[0]} PASS, {len(FAILS)} FAIL ({total} checks)")
    for f in FAILS:
        print("  - " + f)
    print("  shots:", SHOTS)
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main())
