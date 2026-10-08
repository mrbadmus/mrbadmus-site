#!/usr/bin/env python3
"""fc_bench_live.py — the pupil class page's bench, homework and flashcard
deck together (8 Oct 2026), proved live on the TEST project with the real
class page, the real database and a local backend at origin/main.

THE RULE UNDER TEST
  unfinished homework + unfinished deck -> the bench splits (homework left /
  top, deck right / below); only one -> it fills the card; neither -> exactly
  the bench as it was (done bench / Mixed practice).  The deck shown is the
  one due soonest.  A Done deck drops off the bench — including live, the
  same visit, through the heal.

CASES (a fresh pupil each; every case at phone 390x844 and desktop 1280x800,
light and dark)
  both       nothing done -> split, deck S (due sooner) on the right
  hw-only    both decks Done -> homework fills, no deck half
  fc-only    homework submitted -> deck S fills the card, no Mixed practice
  neither    homework submitted + both decks Done -> the empty bench as before
  started    4 of deck S secured -> "4 of 10 secured" and the started label
  s-done     deck S Done, L not -> deck L shown
  button     the deck half's button opens the flashcard overlay on that deck
  heal-empty homework submitted, deck L Done, deck S fully rated but never submitted: deck S fills the
             card, then the heal drops it and the bench is handed back as it was (Mixed practice)
  heal-live  deck S fully rated but never submitted -> the page's heal writes
             the submission and the bench moves on to deck L the same visit

TEARDOWN deletes ONLY the ids this run created (a snapshotted manifest, never
a predicate) and then proves nothing is left behind.

    MRB_BACKEND_DIR=<backend checkout at origin/main> python3 tools/fc_bench_live.py
        [--cases both,fc-only] [--configs phone-light] [--shots DIR]

TEST ONLY — the service key's `ref` claim is checked before any write.
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
import mrb354_secured_live as m  # noqa: E402  (backend, teardown, shot)
import flashcard_homework_drive as drv  # noqa: E402  (Phone, check, CONTRAST_JS)

check = drv.check
FAILS = drv.FAILS
settle = drv.settle

EVIDENCE_DIR = None        # set only by an explicit --shots DIR (evidence is never written into the tree by default)
BACKEND_DIR = os.environ.get("MRB_BACKEND_DIR",
                             "/Users/midebadmus/Documents/GitHub/mrbadmus-backend-worktrees/fc-bench")
m.BACKEND_DIR = BACKEND_DIR
SCRATCH = os.path.expanduser(os.environ.get("MRB_SHOTS") or "~/tmp/fc-bench")

CONFIGS = [  # (tag, width, height, mobile, theme)
    ("phone-light", 390, 844, True, "light"),
    ("phone-dark", 390, 844, True, "dark"),
    ("desk-light", 1280, 800, False, "light"),
    ("desk-dark", 1280, 800, False, "dark"),
    ("tab-light", 820, 1100, False, "light"),
]
CASES = ["live-finish", "both", "hw-only", "fc-only", "neither", "started", "s-done", "button", "heal-live", "heal-empty"]

# (case, config) -> evidence name
EVIDENCE = {
    ("both", "phone-light"): "both-phone-light", ("both", "desk-dark"): "both-desk-dark",
    ("fc-only", "phone-dark"): "fc-only-phone-dark", ("fc-only", "desk-light"): "fc-only-desk-light",
    ("started", "desk-light"): "started-desk-light", ("neither", "phone-light"): "neither-phone-light",
    ("hw-only", "desk-light"): "hw-only-desk-light", ("s-done", "phone-dark"): "s-done-phone-dark", ("both", "tab-light"): "both-tablet-light",
}

DECK = [("Card %d question" % (i + 1), "Card %d answer" % (i + 1)) for i in range(10)]
TITLE_S, TITLE_L = "Forces recap", "Cells recap"
HW_TITLE = "Energy stores"


def jget(url, token, method="GET", body=None, timeout=60):
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, method=method,
                                 headers={"Authorization": "Bearer " + token, "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            raw = r.read()
            return r.status, (json.loads(raw) if raw else None)
    except urllib.error.HTTPError as e:
        raw = e.read()
        try:
            return e.code, json.loads(raw)
        except Exception:
            return e.code, raw.decode(errors="replace")[:300]


def build_world(c, manifest):
    ts = int(time.time())
    school, klass, year = str(uuid.uuid4()), str(uuid.uuid4()), str(uuid.uuid4())
    manifest.update({"schools": [school], "classes": [klass], "years": [year], "assignments": [], "users": [],
                     "decks": []})
    email = f"fcb-t-{ts}@throwaway.test"
    tid = c.admin_create_user(email, acc.THROWAWAY_PASSWORD)
    manifest["users"].append(tid)
    acc._ok("school", *c.write("schools", "POST", {"id": school, "name": f"FCB {ts}", "code": f"FCB{ts}",
                                                    "kind": "school", "key_stages_supported": ["KS3", "KS4"]}))
    today = datetime.now(timezone.utc).date()
    start = f"{today.year if today.month >= 9 else today.year - 1}-09-01"
    end = f"{int(start[:4]) + 1}-08-31"
    acc._ok("year", *c.write("academic_years", "POST", {"id": year, "school_id": school, "name": "fcb",
                                                         "start_date": start, "end_date": end, "is_current": True}))
    acc._ok("class", *c.write("classes", "POST", {"id": klass, "school_id": school, "academic_year_id": year,
                                                   "name": f"8b/Sc{ts % 10}", "key_stage": "KS3", "year_group": 8}))
    st, body = c.write("classes", "PATCH", {"__match__": f"id=eq.{klass}", "auto_assignments": False})
    check(st in (200, 204), "the class has no automatic weekly work (%s)" % st)
    acc._ok("t", *c.write("profiles", "PATCH", {"__match__": f"id=eq.{tid}", "role": "teacher", "school_id": school,
                                                 "first_name": "Tfc", "last_name": "Bench", "display_name": "Tfc Bench",
                                                 "username": f"fcbt{ts:x}"}))
    st, subj = c.select(None, "subjects", {"select": "id,name", "name": "eq.Physics"}, as_service=True)
    acc._ok("class_teachers", *c.write("class_teachers", "POST", {
        "class_id": klass, "teacher_id": tid, "role": "subject_teacher", "subject_id": subj[0]["id"]}))
    tok_t = c.sign_in(email, acc.THROWAWAY_PASSWORD)
    now = datetime.now(timezone.utc)
    cards = [{"question": q, "answer": a} for q, a in DECK]
    aids = {}
    for key, title, days in (("S", TITLE_S, 2), ("L", TITLE_L, 6)):
        st, deck = c.rpc(tok_t, "flashcard_deck_save", {
            "p_deck": None, "p_title": title, "p_cards": cards,
            "p_meta": {"source_kind": "typed", "subject": "physics"}, "p_finalise": True})
        if st != 200:
            acc.die(f"deck save {st} {deck}")
        manifest["decks"].append(deck["deck_id"])
        st, sw = c.rpc(tok_t, "flashcard_set_work", {
            "p_class_ids": [klass], "p_deck": deck["deck_id"], "p_mode": "review", "p_rule": "secure",
            "p_title": title, "p_release_at": (now - timedelta(minutes=1)).isoformat(),
            "p_due_at": (now + timedelta(days=days)).isoformat(), "p_note": None,
            "p_client_ref": f"fcb-{key}-{ts}"})
        if st != 200:
            acc.die(f"set work {st} {sw}")
        manifest["assignments"].extend(sw["assignment_ids"])
        aids[key] = sw["assignment_ids"][0]
    return {"school": school, "class": klass, "teacher": tid, "tok_t": tok_t, "aids": aids, "ts": ts}


def set_homework(w, api, manifest):
    """One real teacher-set question homework through the local backend's set-work route."""
    tok = w["tok_t"]
    st, sc = jget(f"{api}/api/teacher/set-work/scope?class_id={w['class']}", tok)
    if st != 200:
        acc.die(f"scope {st} {sc}")
    tiers = sc.get("tiers") or []
    tier = None
    for t in tiers:
        tid = t.get("id") if isinstance(t, dict) else t
        if tid in ("standard", "medium", "higher"):
            tier = tid
    if tier is None and tiers:
        tier = tiers[0].get("id") if isinstance(tiers[0], dict) else tiers[0]
    chosen = None
    for topic in sc.get("tree") or []:
        for child in topic.get("children") or []:
            cnt = child.get("counts") or child.get("count") or {}
            k = cnt.get(tier) if isinstance(cnt, dict) else cnt
            if (k or 0) >= 8:
                chosen = (child["id"], topic.get("subject"))
                break
        if chosen:
            break
    if not chosen:
        acc.die("no lesson with 8+ questions")
    lesson, subject = chosen
    q = (f"{api}/api/teacher/set-work/preview?class_id={w['class']}&tier={tier}&scope_kind=subtopic"
         f"&scope_ref={lesson}&count=6" + (f"&subject={subject}" if subject else ""))
    st, pv = jget(q, tok)
    if st != 200:
        acc.die(f"preview {st} {pv}")
    ids = [x["id"] for x in (pv.get("picked") or [])][:6]
    now = datetime.now(timezone.utc)
    st, out = jget(f"{api}/api/teacher/set-work", tok, "POST", {
        "class_ids": [w["class"]], "tier": tier, "title": HW_TITLE, "release_at": None,
        "due_at": (now + timedelta(days=4)).isoformat(), "client_ref": str(uuid.uuid4()),
        "scopes": [{"scope_kind": "subtopic", "scope_ref": lesson, "subject": subject, "question_ids": ids}]})
    if st != 200:
        acc.die(f"set-work {st} {out}")
    aid = (out.get("assignment_ids") or [None])[0] or (out.get("assignments") or [{}])[0].get("id")
    manifest["assignments"].append(aid)
    return aid


def add_pupil(c, manifest, w, tag):
    email = f"fcb-p-{tag}-{w['ts']}@throwaway.test"
    uid = c.admin_create_user(email, acc.THROWAWAY_PASSWORD)
    manifest["users"].append(uid)
    acc._ok("p", *c.write("profiles", "PATCH", {"__match__": f"id=eq.{uid}", "role": "student", "school_id": w["school"],
                                                 "first_name": "Pfc", "last_name": tag.title(), "display_name": f"Pfc {tag}",
                                                 "username": f"fcbp{abs(hash(tag)) % 10000}{w['ts']:x}",
                                                 "science_pathway": "combined", "tier": "higher"}))
    acc._ok("class_members", *c.write("class_members", "POST", {"class_id": w["class"], "student_id": uid,
                                                                 "joined_via": "admin_added"}))
    return {"email": email, "id": uid}


def rate(c, pupil, aid, deck_cards, n):
    """n got_it ratings through the real flashcard_record path, as the pupil."""
    tok = c.sign_in(pupil["email"], acc.THROWAWAY_PASSWORD)
    t = datetime.now(timezone.utc) - timedelta(minutes=20)
    ev = []

    def add(**kw):
        nonlocal t
        ev.append(dict(id=str(uuid.uuid4()), at=t.isoformat(), phase="review", visible=True, **kw))
        t += timedelta(seconds=4)
    for cd in deck_cards[:n]:
        add(type="card_shown", card=cd["id"])
        add(type="answer_submitted", card=cd["id"], answer="my own words")
        add(type="rated", card=cd["id"], rating="got_it")
    st, body = acc.run_events(c, tok, aid, ev)
    check(st == 200, "flashcard_record recorded %d got_it ratings (%s)" % (n, st))
    return body


def submit_homework(c, pupil, aid):
    now = datetime.now(timezone.utc)
    st, body = c.write("assignment_submissions", "POST", {
        "assignment_id": aid, "student_id": pupil["id"], "score": 5, "max_score": 6, "status": "complete",
        "submitted_at": now.isoformat(), "completed_at": now.isoformat(), "started_at": now.isoformat(),
        "is_late": False, "attempts": 1, "attempt_no": 1})
    check(st in (200, 201, 204), "homework submission row written (%s %s)" % (st, str(body)[:120]))


def ensure_submission(c, pupil, aid):
    st, rows = c.select(None, "assignment_submissions", {"assignment_id": f"eq.{aid}", "student_id": f"eq.{pupil['id']}",
                                                          "select": "id,submitted_at"}, as_service=True)
    return bool(rows and rows[0].get("submitted_at"))


# ── what the page shows ───────────────────────────────────────────────────

ROW_LABEL_JS = r"""
(function (title) {
  var bench = document.querySelector('[data-port-region="bench"]');
  var all = document.querySelectorAll('main *, body *');
  var hit = null;
  for (var i = 0; i < all.length; i++) {
    var e = all[i];
    if (bench && bench.contains(e)) { continue; }
    if (e.children.length === 0 && (e.textContent || '').trim() === title) { hit = e; break; }
  }
  if (!hit) { return {err: 'row not found'}; }
  hit.click();
  return {ok: true};
})(%s)
"""

ROW_TEXT_JS = r"""
(function (title) {
  var bench = document.querySelector('[data-port-region="bench"]');
  var out = [];
  document.querySelectorAll('a,button').forEach(function (e) {
    if (bench && bench.contains(e)) { return; }
    var t = (e.innerText || '').replace(/\s+/g, ' ').trim();
    if (/Complete homework|Continue|Open the assignment|Revise|another go/.test(t)) {
      out.push(t + ' -> ' + (e.getAttribute('href') || ''));
    }
  });
  return out;
})(%s)
"""

BENCH_JS = r"""
(function () {
  var f = document.querySelector('[data-port-region="bench"]');
  if (!f) { return null; }
  var half = f.querySelector('[data-mrb-bench-fc]');
  var next = f.querySelector('[data-mrb-bench-next]');
  var held = f.querySelector('[data-mrb-held]');
  var hw = f.querySelector('[data-mrb-bench-hw]');
  var go = half ? half.querySelector('[data-mrb-bench-fc-go]') : null;
  function r(e) { if (!e) return null; var b = e.getBoundingClientRect();
    return {l: Math.round(b.left), t: Math.round(b.top), w: Math.round(b.width), h: Math.round(b.height)}; }
  var root = document.scrollingElement || document.documentElement;
  var lines = half ? half.innerText.split('\n').map(function (s) { return s.trim(); }).filter(Boolean) : null;
  var cta = null;
  var all = f.querySelectorAll('a,button');
  var ctas = [];
  all.forEach(function (e) { var t = (e.innerText || '').replace(/\s+/g, ' ').trim(); if (t) ctas.push(t); });
  return {text: f.innerText.replace(/\s+\n/g, '\n').trim(), halfLines: lines, half: !!half, next: !!next, held: !!held,
          frame: r(f), halfRect: r(half), goRect: r(go), goHref: go ? go.getAttribute('href') : null,
          goText: go ? go.innerText.trim() : null, ctas: ctas,
          hscroll: root.scrollWidth - window.innerWidth, vw: window.innerWidth};
})()
"""

# the bench's open grid / done bench are Design's own markup, so "homework is
# present" is read from the text the pupil can see.
HW_VISIBLE_JS = r"""
(function (title) {
  var f = document.querySelector('[data-port-region="bench"]');
  if (!f) { return null; }
  var t = f.innerText;
  return {hw: t.indexOf(title) >= 0};
})(%s)
"""


def goto_ready(P, page, origin, api, session, hash_=""):
    page.goto(origin + "/CLAUDE.md")
    P.q("localStorage.setItem(%s,%s)" % (json.dumps(f"sb-{acc.TEST_REF}-auth-token"), json.dumps(json.dumps(session))))
    page.goto("about:blank")
    m.goto_class(page, f"{origin}/student/class.html?api={api}{hash_}")
    t0 = time.time()
    last, since = None, time.time()
    while time.time() - t0 < 45:
        try:
            s = P.q(BENCH_JS)
        except Exception:
            s = None
        if s and s["text"]:
            key = json.dumps([s["text"], s["half"], s["next"]])
            if key != last:
                last, since = key, time.time()
            elif time.time() - since > 2.2:
                return s
        time.sleep(0.4)
    return P.q(BENCH_JS)


def set_theme(P, theme):
    P.q("document.documentElement.setAttribute('data-theme',%s)" % json.dumps(theme))
    settle(0.5)


def sess_for(c, url, email):
    st, sess = c._req("POST", f"{url}/auth/v1/token?grant_type=password",
                      {"apikey": c.anon, "Content-Type": "application/json"},
                      {"email": email, "password": acc.THROWAWAY_PASSWORD})
    if st != 200:
        acc.die(f"sign-in {email} -> {st} {sess}")
    return sess


def verify(case, tag, width, P, s, expect):
    """expect: dict(half=bool, title, count, due?, progress?, label?, hw=bool, next=bool)"""
    name = f"{case}/{tag}"
    check(s is not None, f"{name}: the bench is on the page")
    if s is None:
        return
    check(s["half"] is expect["half"], f"{name}: deck half {'present' if expect['half'] else 'absent'} (got {s['half']})")
    hwv = P.q(HW_VISIBLE_JS % json.dumps(HW_TITLE))
    check(bool(hwv and hwv["hw"]) is expect["hw"], f"{name}: homework {'shown' if expect['hw'] else 'not shown'} on the bench")
    if expect["next"] is not None:
        check(s["next"] is expect["next"], f"{name}: Mixed-practice / next box {'present' if expect['next'] else 'absent'} (got {s['next']})")
    check(s["hscroll"] <= 1, f"{name}: no horizontal page scroll ({s['hscroll']})")
    if expect["half"]:
        lines = s["halfLines"] or []
        joined = " | ".join(lines)
        lj = joined.lower()
        check(expect["title"] in joined, f"{name}: deck title {expect['title']!r} ({joined})")
        if expect.get("progress"):
            check(expect["progress"] in lj, f"{name}: progress {expect['progress']!r} ({joined})")
            check("10 cards" not in lj, f"{name}: the count is said once (the progress line, not also '10 cards')")
        else:
            check(lj.count("10 cards") == 1, f"{name}: card count shown once as '10 CARDS' ({joined})")
            check("secured" not in lj, f"{name}: no progress line before the pupil has started")
        check(lj.count("flashcards") == 1 and lj.count("due") == 1, f"{name}: kicker and due day each shown once")
        check(s["goText"] == expect["label"], f"{name}: button reads {expect['label']!r} (got {s['goText']!r})")
        check(bool(s["goHref"]) and s["goHref"].startswith("#cards="), f"{name}: button is a #cards= link ({s['goHref']})")
        check(s["goRect"] and s["goRect"]["h"] >= 43.5, f"{name}: button >= 44px tall ({s['goRect']})")
        ct = P.q("(%s)('[data-mrb-bench-fc] h2')" % drv.CONTRAST_JS)
        ct2 = P.q("(%s)('[data-mrb-bench-fc] [data-mrb-bench-fc-go]')" % drv.CONTRAST_JS)
        ct3 = P.q("(%s)('[data-mrb-bench-fc] [data-mrb-bench-fc-meta]')" % drv.CONTRAST_JS)
        check(ct is not None and ct >= 4.5, f"{name}: heading contrast {ct and round(ct, 2)}")
        check(ct2 is not None and ct2 >= 4.5, f"{name}: button contrast {ct2 and round(ct2, 2)}")
        if expect.get("progress"):
            check(ct3 is not None and ct3 >= 3.0, f"{name}: progress line contrast {ct3 and round(ct3, 2)}")
        hr = P.q("(function(){var h=document.querySelector('[data-mrb-bench-hw]'); var d=document.querySelector('[data-mrb-bench-fc]');"
                 "if(!h||!d) return null; var a=h.getBoundingClientRect(), b=d.getBoundingClientRect();"
                 "return {al:a.left,at:a.top,ar:a.right,ab:a.bottom,bl:b.left,bt:b.top,br:b.right,bb:b.bottom,"
                 "ow:Math.max(h.scrollWidth-h.clientWidth,d.scrollWidth-d.clientWidth)};})()")
        if expect["hw"]:
            check(hr is not None, f"{name}: homework wrapper and deck half both present")
            if hr:
                if width >= 1024:
                    check(hr["al"] < hr["bl"] and abs(hr["at"] - hr["bt"]) < 4, f"{name}: homework left, deck right ({hr})")
                else:
                    check(hr["at"] < hr["bt"] and abs(hr["al"] - hr["bl"]) < 4, f"{name}: homework on top, deck below ({hr})")
                check(hr["ow"] <= 1, f"{name}: neither half clips horizontally ({hr['ow']})")
    else:
        pass


def snap_evidence(page, case, tag, scratch):
    nm = EVIDENCE.get((case, tag))
    os.makedirs(scratch, exist_ok=True)
    m.shot(page, scratch, f"{case}-{tag}")
    if nm and EVIDENCE_DIR:
        os.makedirs(EVIDENCE_DIR, exist_ok=True)
        m.shot(page, EVIDENCE_DIR, nm)


def live_finish(c, url, manifest, mpath, w, hw, c_s, c_l, origin, api, page, P, tag, theme):
    """Finish a deck through the REAL overlay, opened from the bench button, and watch the bench in the
    SAME visit (no reload): A) deck S done -> deck L promoted; B) homework submitted and L already Done,
    S done -> the bench is handed back as it was (no deck half)."""
    m.enable_fetch(page)
    seen: set = set()

    def play_through():
        for _ in range(60):
            s = P.st()
            if s.get("end1") is not None:
                return s
            f = s["front"]
            if f is None:
                time.sleep(0.3)
                continue
            P.type(f.replace("question", "answer"))
            P.click('[data-hw="check"]')
            m.wait_chip(P, page, seen)
            P.click('[data-hw="got_it"]')
        return P.st()

    for variant in ("A", "B"):
        name = f"live-finish-{variant}/{tag}"
        p = add_pupil(c, manifest, w, f"lf{variant.lower()}{tag.replace('-', '')}")
        json.dump(manifest, open(mpath, "w"), indent=1)
        if variant == "B":
            submit_homework(c, p, hw)
            rate(c, p, w["aids"]["L"], c_l, 10)
        sess = sess_for(c, url, p["email"])
        s = goto_ready(P, page, origin, api, sess)
        set_theme(P, theme)
        P.q("window.__lf_marker = 1")
        s = P.q(BENCH_JS)
        check(bool(s and s["half"]) and TITLE_S in " ".join(s["halfLines"] or []), f"{name}: the bench starts on deck S")
        P.q("document.querySelector('[data-mrb-bench-fc-go]').click()")
        t0 = time.time()
        while time.time() - t0 < 15 and not P.st()["strip"]:
            time.sleep(0.4)
        end = play_through()
        check(end.get("end1") == "10 of 10 secured" and end.get("done") == "Done", f"{name}: finished in the overlay ({end.get('end1')!r})")
        settle(2.5)                         # the Done screen's pass settles, onFinish runs
        P.click('[data-hw="done"]')
        t0 = time.time()
        res = None
        while time.time() - t0 < 25:
            s = P.q(BENCH_JS)
            if variant == "A" and s and s["half"] and TITLE_L in " ".join(s["halfLines"] or []):
                res = s
                break
            if variant == "B" and s and not s["half"] and s["text"]:
                res = s
                break
            time.sleep(0.5)
        check(P.q("window.__lf_marker") == 1, f"{name}: same visit, the page was not reloaded")
        if variant == "A":
            check(res is not None, f"{name}: deck S left the bench and deck L took its place")
            check(res is not None and not any(TITLE_S in x for x in (res["halfLines"] or [])), f"{name}: deck S is no longer shown")
        else:
            check(res is not None and not res["half"], f"{name}: deck S left the bench and no deck half is left")
            check(bool(res and res["next"]), f"{name}: the bench is handed back as it was (Mixed practice)")
        errs = m.no_fav(page.console_errors())
        check(not errs, f"{name}: no console errors ({errs[:2]})")
        snap_evidence(page, f"live-finish-{variant}", tag, os.path.join(SCRATCH, "shots"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cases", default=",".join(CASES))
    ap.add_argument("--configs", default=",".join(c[0] for c in CONFIGS))
    ap.add_argument("--dump", action="store_true", help="print each bench's text")
    ap.add_argument("--shots", default=None, help="write the named evidence shots into DIR (default: scratch only)")
    a = ap.parse_args()
    global EVIDENCE_DIR
    if a.shots:
        EVIDENCE_DIR = os.path.abspath(a.shots)
    cases = [x for x in a.cases.split(",") if x]
    configs = [c for c in CONFIGS if c[0] in a.configs.split(",")]

    env = acc.read_env(acc.BACKEND_ENV_DEFAULT)
    url, service = env["SUPABASE_URL"], env["SUPABASE_SERVICE_ROLE_KEY"]
    ref = acc.jwt_ref(service)
    if ref != acc.TEST_REF:
        acc.die(f"refusing: service key ref {ref} is not TEST ({acc.TEST_REF})")
    print(f"credential ref, proven from the key payload: {ref} => TEST (writing to TEST only)")
    if not os.path.isdir(BACKEND_DIR):
        acc.die(f"backend checkout missing: {BACKEND_DIR}")
    c = acc.Client(url, acc.anon_key(), service)
    manifest = {}
    os.makedirs(SCRATCH, exist_ok=True)
    mpath = os.path.join(SCRATCH, "manifest.json")

    sport, bport = m.free_port(), m.free_port()
    origin = f"http://127.0.0.1:{sport}"
    api = f"http://localhost:{bport}"
    backend_proc = site_server = deno_proc = None
    try:
        w = build_world(c, manifest)
        json.dump(manifest, open(mpath, "w"), indent=1)
        backend_proc = m.start_backend(bport, origin, SCRATCH)
        site_server, _ = cdp.serve(REPO, sport)
        if "live-finish" in cases:
            deno_proc = m.start_deno(url, service, SCRATCH, os.path.join(SCRATCH, "stub.log"))
        hw = set_homework(w, api, manifest)
        json.dump(manifest, open(mpath, "w"), indent=1)
        print(f"backend {api}, site {origin}; homework {hw}, decks {w['aids']}")

        st, c_s = c.select(None, "assignment_flashcards", {"select": "id,position", "assignment_id": f"eq.{w['aids']['S']}",
                                                              "order": "position"}, as_service=True)
        st, c_l = c.select(None, "assignment_flashcards", {"select": "id,position", "assignment_id": f"eq.{w['aids']['L']}",
                                                              "order": "position"}, as_service=True)
        check(len(c_s) == 10 and len(c_l) == 10, "both decks hold ten cards")

        # ── the pupils: one fresh pupil per case, states made through real paths ──
        pupils = {}
        for case in [x for x in cases if x != "live-finish"]:
            p = add_pupil(c, manifest, w, case.replace("-", ""))
            pupils[case] = p
            json.dump(manifest, open(mpath, "w"), indent=1)
            if case == "hw-only":
                rate(c, p, w["aids"]["S"], c_s, 10)
                rate(c, p, w["aids"]["L"], c_l, 10)
            elif case == "fc-only":
                submit_homework(c, p, hw)
            elif case == "neither":
                submit_homework(c, p, hw)
                rate(c, p, w["aids"]["S"], c_s, 10)
                rate(c, p, w["aids"]["L"], c_l, 10)
            elif case == "started":
                rate(c, p, w["aids"]["S"], c_s, 4)
            elif case == "s-done":
                rate(c, p, w["aids"]["S"], c_s, 10)
            if case in ("hw-only", "neither", "s-done"):
                for key in ("S", "L"):
                    done = ensure_submission(c, p, w["aids"][key])
                    print(f"  [{case}] deck {key} submission written by the RPC: {done}")
                # a deck the RPC completed but did not submit is healed on the page's own load (heal-live);
                # for the static cases it is written here so the starting state is exact.
                for key in (("S", "L") if case != "s-done" else ("S",)):
                    if not ensure_submission(c, p, w["aids"][key]):
                        now = datetime.now(timezone.utc).isoformat()
                        c.write("assignment_submissions", "POST", {
                            "assignment_id": w["aids"][key], "student_id": p["id"], "score": 10, "max_score": 10,
                            "status": "complete", "submitted_at": now, "completed_at": now, "started_at": now,
                            "is_late": False, "attempts": 1, "attempt_no": 1})
            elif case == "heal-live":
                rate(c, p, w["aids"]["S"], c_s, 10)
                # make the starting state exact: rated all ten, NOT submitted
                st, rows = c.select(None, "assignment_submissions", {
                    "assignment_id": f"eq.{w['aids']['S']}", "student_id": f"eq.{p['id']}", "select": "id"}, as_service=True)
                for r in rows or []:
                    manifest.setdefault("submissions_removed", []).append(r["id"])
                    c.write("assignment_submissions", "DELETE", {"__match__": f"id=eq.{r['id']}"})

        s_secs = {}
        for tag, width, height, mobile, theme in configs:
            print(f"\n── {tag}: {width}x{height} {'phone' if mobile else 'desktop'}, {theme} ──")
            br = cdp.Browser().start()
            try:
                page = br.attach()
                page.send("Emulation.setDeviceMetricsOverride",
                          {"width": width, "height": height, "deviceScaleFactor": 2 if mobile else 1, "mobile": mobile})
                if mobile:
                    page.send("Emulation.setTouchEmulationEnabled", {"enabled": True, "maxTouchPoints": 5})
                try:
                    page.send("Emulation.setFocusEmulationEnabled", {"enabled": True})
                except cdp.CDPError:
                    pass
                P = drv.Phone(page, width, height, 0, None)
                for case in [x for x in cases if x != "live-finish"]:
                    p = pupils[case]
                    if case in ("heal-live", "heal-empty"):
                        # a pupil whose submission the heal writes is spent after one load: a fresh one per config
                        p = add_pupil(c, manifest, w, f"{case.replace('-', '')}{tag.replace('-', '')}")
                        json.dump(manifest, open(mpath, "w"), indent=1)
                        if case == "heal-empty":
                            submit_homework(c, p, hw)
                            rate(c, p, w["aids"]["L"], c_l, 10)
                        rate(c, p, w["aids"]["S"], c_s, 10)
                        st, rows = c.select(None, "assignment_submissions", {
                            "assignment_id": f"eq.{w['aids']['S']}", "student_id": f"eq.{p['id']}", "select": "id"},
                                            as_service=True)
                        for r in rows or []:
                            manifest.setdefault("submissions_removed", []).append(r["id"])
                            json.dump(manifest, open(mpath, "w"), indent=1)
                            c.write("assignment_submissions", "DELETE", {"__match__": f"id=eq.{r['id']}"})
                    sess = sess_for(c, url, p["email"])
                    s = goto_ready(P, page, origin, api, sess)
                    set_theme(P, theme)
                    s = P.q(BENCH_JS)
                    if a.dump and s:
                        print(f"  [{case}] bench text: {s['text']!r}")
                        open(os.path.join(SCRATCH, f"bench-{case}-{tag}.html"), "w").write(
                            P.q("document.querySelector('[data-port-region=\"bench\"]').outerHTML"))
                    base = {"title": TITLE_S, "label": "Complete homework"}
                    if case == "both":
                        verify(case, tag, width, P, s, dict(base, half=True, hw=True, next=False))
                    elif case == "hw-only":
                        verify(case, tag, width, P, s, dict(base, half=False, hw=True, next=False))
                    elif case == "fc-only":
                        verify(case, tag, width, P, s, dict(base, half=True, hw=False, next=False))
                    elif case == "neither":
                        verify(case, tag, width, P, s, dict(base, half=False, hw=False, next=None))
                    elif case == "started":
                        time.sleep(1.5)
                        s = P.q(BENCH_JS)
                        P.q(ROW_LABEL_JS % json.dumps(TITLE_S))
                        settle(0.6)
                        rowbtns = P.q(ROW_TEXT_JS % json.dumps(TITLE_S))
                        check(any(b.startswith("Complete homework") for b in rowbtns) and
                              not any(b.startswith("Continue") for b in rowbtns),
                              f"started/{tag}: the work list's own label for the started deck is 'Complete homework' ({rowbtns})")
                        P.q(ROW_LABEL_JS % json.dumps(TITLE_S))      # collapse the row again
                        settle(0.4)
                        verify(case, tag, width, P, s, dict(base, half=True, hw=True, next=False,
                                                            progress="4 of 10 secured"))
                    elif case == "s-done":
                        verify(case, tag, width, P, s, dict(base, title=TITLE_L, half=True, hw=True, next=False))
                    elif case == "button":
                        verify(case, tag, width, P, s, dict(base, half=True, hw=True, next=False))
                        P.q("document.querySelector('[data-mrb-bench-fc-go]').click()")
                        t0 = time.time()
                        opened = False
                        while time.time() - t0 < 15:
                            st_ = P.st()
                            if st_["strip"] and (st_["writing"] or st_["rating"] or st_["panel"]):
                                opened = True
                                break
                            time.sleep(0.5)
                        check(opened, f"button/{tag}: the deck half's button opens the flashcard overlay")
                        if opened:
                            ov = P.q("(document.querySelector('[data-port-region=\"flashcards-overlay\"]')||{}).innerText||''")
                            check(TITLE_S.lower() in ov.lower(), f"button/{tag}: the overlay is deck S ({ov[:80]!r})")
                    elif case == "heal-empty":
                        t0 = time.time()
                        gone = False
                        s = P.q(BENCH_JS)
                        while time.time() - t0 < 30:
                            s = P.q(BENCH_JS)
                            if s and not s["half"] and (s["next"] or s["text"]):
                                gone = True
                                break
                            time.sleep(0.5)
                        check(gone, f"heal-empty/{tag}: the heal dropped deck S and the bench was handed back (no deck half)")
                        check(bool(s and s["next"]), f"heal-empty/{tag}: Mixed practice is back ({s and s['text'][:60]!r})")
                        check(ensure_submission(c, p, w["aids"]["S"]), f"heal-empty/{tag}: deck S now has a submission")
                    elif case == "heal-live":
                        # the heal runs after paint: first the split with deck S, then deck L alone-with-homework
                        t0 = time.time()
                        moved = False
                        while time.time() - t0 < 30:
                            s = P.q(BENCH_JS)
                            if s and s["half"] and TITLE_L in (" ".join(s["halfLines"] or [])):
                                moved = True
                                break
                            time.sleep(0.5)
                        check(moved, f"heal-live/{tag}: the heal wrote deck S's submission and the bench moved to deck L the same visit")
                        verify(case, tag, width, P, s, dict(base, title=TITLE_L, half=True, hw=True, next=False))
                        check(ensure_submission(c, p, w["aids"]["S"]), f"heal-live/{tag}: deck S now has a submission")
                    errs = m.no_fav(page.console_errors())
                    check(not errs, f"{case}/{tag}: no console errors ({errs[:2]})")
                    snap_evidence(page, case, tag, os.path.join(SCRATCH, "shots"))
                if "live-finish" in cases and tag in ("desk-light", "phone-light"):
                    live_finish(c, url, manifest, mpath, w, hw, c_s, c_l, origin, api, page, P, tag, theme)
            finally:
                br.close()
    finally:
        m.stop_deno(deno_proc)
        if site_server is not None:
            site_server.shutdown()
            site_server.server_close()
        m.stop_backend(backend_proc)
        if manifest.get("classes"):
            st, extra = c.select(None, "assignments", {"class_id": f"in.({','.join(manifest['classes'])})",
                                                        "select": "id"}, as_service=True)
            manifest["auto_assignments"] = [x["id"] for x in (extra or []) if x["id"] not in manifest.get("assignments", [])]
            json.dump(manifest, open(mpath, "w"), indent=1)
            m.teardown(c, manifest)
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
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main())
