#!/usr/bin/env python3
"""MRB-351 §5 — drive `teacher/flashcards.html`, one flashcard set's progress.

    python3 flashcard_progress_drive.py              # everything
    python3 flashcard_progress_drive.py --shots DIR  # screenshots somewhere else

It drives the REAL page (served from the repo root) with a STUBBED client:
`window.supabase` answers `flashcard_progress`, `flashcard_pupil_detail` and
`flashcard_edit_assignment` from fixtures shaped exactly like the SQL in
20260924180100_mrb351_flashcards_functions.sql, and `fetch` records the
fire-and-forget answer-check call. Nothing is written to either project.

What it proves:
  · the default sort is least progress first (Missing, Not started, In
    progress by secured, Done late, Done), and every column sorts both ways
    with `aria-sort` saying so;
  · make mode shows Made and Answers, review mode does not;
  · the drawer shows the pupil's answer beside the model answer, the check
    chip, the rating history in order (make phase marked) and the sittings;
  · polling flips a row to Done on an open tab, without a reload;
  · the CSV is the table as displayed, UTF-8 with a BOM;
  · Rushed is a small inline marker, never a block;
  · no horizontal page scroll at 360 / 390, the table scrolls in its own box
    and the pupil column is sticky;
  · no explanatory copy, no mono label under 12px, tap targets >= 44px;
  · and, separately, that teacher-live.js's `cellOf` never grades a
    flashcard set: one MCQ paper at 50% and one flashcard set at 100% give a
    class mean and pupil averages of 50 — the JS twin of
    20260924180200_mrb351_rollup_kind.sql.

Exits non-zero on any failure.
"""

import argparse, json, os, re, sys, time
from datetime import datetime, timedelta, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import ks3_browser as cdp

TEACHER = "11111111-1111-4111-8111-111111111111"
ASSIGN = "aaaaaaaa-0000-4000-8000-000000000001"
CLASS = "cccccccc-0000-4000-8000-000000000001"


def iso(dt):
    return dt.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S+00:00")


NOW = datetime.now(timezone.utc)


def pupil(pid, first, last, status, made, known, secured, sittings, active,
          think, rushed, last_ago, answers, completed=None):
    return {"pupil_id": pid, "first_name": first, "last_name": last,
            "display_name": first, "status": status, "made": made,
            "known": known, "secured": secured, "sittings": sittings,
            "active_ms": active, "median_think_ms": think,
            "median_write_ms": None, "rushed": rushed,
            "last_active": iso(NOW - last_ago) if last_ago is not None else None,
            "answers": dict(zip(["match", "partial", "no", "blank", "pending"], answers)),
            "completed_at": completed}


def progress(mode="make", rule="secure", phase=1):
    ps = [
        pupil("p-ann", "Ann", "Able", "done", 10, 10, 10, 2, 612000, 4200, False,
              timedelta(minutes=3), [8, 1, 1, 0, 0], iso(NOW)),
        pupil("p-ben", "Ben", "Brown", "in_progress", 10, 7, 5, 1, 300000, 2500, False,
              timedelta(days=1, hours=1), [5, 2, 2, 1, 0]),
        pupil("p-cat", "Cat", "Cole", "in_progress", 6, 3, 2, 1, 125000, 900, True,
              timedelta(minutes=70), [2, 1, 1, 0, 2]),
        pupil("p-dan", "Dan", "Dale", "not_started", 0, 0, 0, 0, 0, None, False,
              None, [0, 0, 0, 0, 0]),
        pupil("p-eve", "Eve", "Eyre", "done_late", 10, 10, 10, 3, 900000, 5100, False,
              timedelta(days=2), [9, 1, 0, 0, 0], iso(NOW)),
        pupil("p-fay", "Fay", "Ford", "missing", 3, 1, 0, 1, 60000, 3000, False,
              timedelta(days=3), [1, 0, 1, 1, 0]),
    ]
    if phase == 2:
        for p in ps:
            if p["pupil_id"] == "p-cat":
                p.update(status="done", made=10, known=10, secured=10, sittings=2,
                         completed_at=iso(NOW), last_active=iso(NOW))
    done = sum(1 for p in ps if p["status"] in ("done", "done_late"))
    return {
        "assignment": {"id": ASSIGN, "title": "Atomic structure", "class_id": CLASS,
                       "class_name": "8r/Sc1", "mode": mode, "rule": rule,
                       # 15:00 London (BST) on Friday 3 October 2026
                       "due_at": "2026-10-03T14:00:00+00:00",
                       "release_at": "2026-09-21T06:00:00+00:00",
                       "note": "Bring your planner", "deck_id": "dddddddd-0000-4000-8000-000000000001"},
        "n": 10, "now": iso(NOW),
        "class": {"pupils": len(ps), "done": done,
                  "completion_pct": round(done / len(ps) * 100),
                  "avg_sittings": 1.6,
                  "reteach": [
                      {"card_id": "c2", "position": 1, "question": "Name the particle with no charge",
                       "answer": "Neutron", "not_yet": 4},
                      {"card_id": "c1", "position": 0, "question": "What is the formula of carbon dioxide? CO2",
                       "answer": "CO2", "not_yet": 2}]},
        "pupils": ps,
    }


DETAIL_BEN = {
    "pupil": {"id": "p-ben", "first_name": "Ben", "last_name": "Brown", "display_name": "Ben"},
    "cards": [
        {"id": "c1", "position": 0, "question": "What is the formula of carbon dioxide?",
         "answer": "CO2", "mine": "CO2 gas", "check": "match", "written_ms": 34000,
         "secured": True, "known": True,
         "ratings": [{"rating": "nearly", "phase": "make", "at": iso(NOW - timedelta(days=1, hours=2)), "think_ms": 3000, "session_id": "s1"},
                     {"rating": "got_it", "phase": "review", "at": iso(NOW - timedelta(days=1, hours=1)), "think_ms": 2000, "session_id": "s1"},
                     {"rating": "got_it", "phase": "review", "at": iso(NOW - timedelta(days=1)), "think_ms": 1800, "session_id": "s2"}]},
        {"id": "c2", "position": 1, "question": "Name the particle with no charge",
         "answer": "Neutron", "mine": "electron", "check": "no", "written_ms": 12000,
         "secured": False, "known": False,
         "ratings": [{"rating": "not_yet", "phase": "make", "at": iso(NOW - timedelta(days=1, hours=2)), "think_ms": 900, "session_id": "s1"},
                     {"rating": "not_yet", "phase": "review", "at": iso(NOW - timedelta(days=1, hours=1)), "think_ms": 700, "session_id": "s1"},
                     {"rating": "nearly", "phase": "review", "at": iso(NOW - timedelta(days=1)), "think_ms": 800, "session_id": "s2"}]},
        {"id": "c3", "position": 2, "question": "What is the charge on a proton?",
         "answer": "+1", "mine": "positive", "check": "pending", "written_ms": 8000,
         "secured": False, "known": True, "ratings": []},
    ],
    "sessions": [
        {"id": "s1", "started_at": iso(NOW - timedelta(days=1, hours=2)),
         "ended_at": iso(NOW - timedelta(days=1, hours=1)), "open": False,
         "active_ms": 240000, "cards_seen": 10, "cards_rated": 12, "cards_made": 10,
         "median_think_ms": 2500, "rushed": False},
        {"id": "s2", "started_at": iso(NOW - timedelta(days=1)),
         "ended_at": iso(NOW - timedelta(hours=23)), "open": False,
         "active_ms": 60000, "cards_seen": 10, "cards_rated": 10, "cards_made": 0,
         "median_think_ms": 700, "rushed": True},
    ],
}

STUB_JS = r"""
(function () {
  var F = window.__FP__;
  F.calls = []; F.fetches = []; F.phase = 1;
  function Q(table) {
    var api = {
      select: function () { return api; }, order: function () { return api; },
      limit: function () { return api; }, eq: function () { return api; },
      is: function () { return api; }, in: function () { return api; },
      single: function () { api._one = true; return api; },
      maybeSingle: function () { api._one = true; return api; },
      then: function (res, rej) {
        var rows = (F.tables[table] || []).slice();
        var out = api._one ? {data: rows[0] || null, error: rows.length ? null : {code: 'PGRST116'}}
                           : {data: rows, error: null};
        return Promise.resolve(out).then(res, rej);
      }
    };
    return api;
  }
  var user = {id: F.uid, aud: 'authenticated', role: 'authenticated',
              email: 'stub@drive.invalid', app_metadata: {}, user_metadata: {}};
  var client = {
    from: Q,
    rpc: function (name, args) {
      F.calls.push({name: name, args: args});
      if (name === 'flashcard_progress') {
        return Promise.resolve({data: F.phase === 2 ? F.progress2 : F.progress, error: null});
      }
      if (name === 'flashcard_pupil_detail') {
        return Promise.resolve({data: F.detail[args.p_pupil] || F.detail['*'], error: null});
      }
      if (name === 'flashcard_edit_assignment') {
        return Promise.resolve({data: {ok: true}, error: null});
      }
      return Promise.resolve({data: null, error: {message: 'unknown_rpc'}});
    },
    auth: {
      getUser: function () { return Promise.resolve({data: {user: user}, error: null}); },
      getSession: function () {
        return Promise.resolve({data: {session: {user: user, access_token: 'stub'}}, error: null});
      },
      signOut: function () { return Promise.resolve({error: null}); },
      onAuthStateChange: function () { return {data: {subscription: {unsubscribe: function () {}}}}; }
    }
  };
  var sdk = {createClient: function () { return client; }};
  Object.defineProperty(window, 'supabase', {
    configurable: true, get: function () { return sdk; }, set: function () {}
  });
  var realFetch = window.fetch;
  window.fetch = function (url, opts) {
    var u = String(url && url.url || url);
    if (/functions\/v1\//.test(u) || /onrender\.com/.test(u)) {
      F.fetches.push({url: u, method: opts && opts.method, body: opts && opts.body});
      return Promise.resolve(new Response('{"ok":true}', {status: 200,
        headers: {'Content-Type': 'application/json'}}));
    }
    return realFetch.apply(this, arguments);
  };
})();
"""


def stub(progress1, progress2, detail):
    fx = {"uid": TEACHER,
          "tables": {"profiles": [{"id": TEACHER, "role": "teacher", "first_name": "Tess",
                                   "last_name": "Teacher", "school_id": "s", "deleted_at": None}],
                     "staff_scopes": []},
          "progress": progress1, "progress2": progress2, "detail": detail}
    return "window.__FP__=%s;\n%s" % (json.dumps(fx), STUB_JS)


def wait_for(p, expr, timeout=8.0, step=0.1):
    end = time.time() + timeout
    while time.time() < end:
        try:
            if p.eval(expr):
                return True
        except cdp.JSError:
            pass
        time.sleep(step)
    return False


ORDER = "Array.prototype.map.call(document.querySelectorAll('#fp-table tbody tr.fp-row'),function(r){return r.getAttribute('data-pupil');})"

RANK = {"missing": 0, "not_started": 1, "in_progress": 2, "done_late": 3, "done": 4}


def value_of(p, key):
    if key == "pupil":
        return (p["last_name"] + " " + p["first_name"]).lower()
    if key == "status":
        return RANK[p["status"]]
    if key == "made":
        return p["made"]
    if key == "secured":
        return p["secured"]
    if key == "sittings":
        return p["sittings"]
    if key == "time":
        return p["active_ms"]
    if key == "percard":
        return p["median_think_ms"]
    if key == "rushed":
        return 1 if p["rushed"] else 0
    if key == "answers":
        return p["answers"]["match"]
    if key == "last":
        return p["last_active"]
    raise KeyError(key)


def monotonic(vals, desc):
    present = [v for v in vals if v is not None]
    # nulls always sink, whichever way
    if vals[:len(present)] != present:
        return False
    for a, b in zip(present, present[1:]):
        if (b > a) if desc else (b < a):
            return False
    return True


# Visible text that is NOT data: labels, counts, buttons. Anything that reads
# like a sentence of explanation fails.
COPY_JS = r"""
(function(){
  var out = [];
  var roots = [document.getElementById('fp-main'), document.getElementById('fp-drawer-back')];
  roots.forEach(function (root) {
    if (!root) return;
    var w = document.createTreeWalker(root, NodeFilter.SHOW_TEXT);
    var n;
    while ((n = w.nextNode())) {
      var t = n.nodeValue.replace(/\s+/g, ' ').trim();
      if (!t) continue;
      var e = n.parentElement;
      if (!e || e.closest('[data-fp-data],.fp-name,.fp-drawer-name,.fp-title,.fp-crumb')) continue;
      if (e.closest('[hidden]')) continue;
      var cs = getComputedStyle(e);
      if (cs.display === 'none' || cs.visibility === 'hidden') continue;
      out.push(t);
    }
  });
  return out;
})()
"""

FORBIDDEN = re.compile(r"(\bthis page\b|\bclick\b|\btap\b|\byou can\b|\bwill\b|\bhere\b|"
                       r"\bhow\b|\bshows?\b|\bwhen\b|\. [A-Z])", re.I)

A11Y_JS = r"""
(function(){
  var small = [], tiny = [];
  document.querySelectorAll('#fp-main *, #fp-drawer-back *').forEach(function (e) {
    if (e.closest('[hidden]')) return;
    var cs = getComputedStyle(e);
    if (cs.display === 'none') return;
    var hasText = Array.prototype.some.call(e.childNodes, function (c) {
      return c.nodeType === 3 && c.nodeValue.trim(); });
    if (hasText && /DM Mono/.test(cs.fontFamily) && parseFloat(cs.fontSize) < 12) {
      small.push(e.className + ' ' + cs.fontSize);
    }
  });
  document.querySelectorAll('.fp-sort, .fp-name, .fp-actions .btn, .fp-close').forEach(function (b) {
    if (b.closest('[hidden]')) return;
    var r = b.getBoundingClientRect();
    if (r.width && r.height < 43.5) tiny.push((b.className || b.tagName) + ' ' + Math.round(r.height));
  });
  return {small: small, tiny: tiny};
})()
"""


def cellof_check(b, base, check):
    """teacher-live.js's `cellOf`, run for real: its `run()` is switched off
    and `buildPapers` / `buildMatrix` are called on a fixture pack."""
    src = open(os.path.join(HERE, "shared", "teacher-live.js"), encoding="utf-8").read()
    anchor = "  run().catch(function (err) {"
    if src.count(anchor) != 1:
        check(False, "cellOf: teacher-live.js's run() call found exactly once")
        return
    src = src.replace(anchor, "  (function () { return Promise.resolve(); })().catch(function (err) {")
    p = b.page("about:blank", settle=0.2)
    p.send("Page.addScriptToEvaluateOnNewDocument",
           {"source": "window.fetch=function(){return Promise.reject(new Error('offline'));};"})
    p.goto(base + "/teacher/flashcards.html?drive=cellof", settle=0.3)
    p.eval(src + "\n;true")
    probe = r"""
    (function (asFlash) {
      var L = window.MrBadmusTeacherLive;
      var pack = {
        members: [{student_id: 's1', first_name: 'A', last_name: 'One', joined_at: '2026-09-01T00:00:00+00:00'},
                  {student_id: 's2', first_name: 'B', last_name: 'Two', joined_at: '2026-09-01T00:00:00+00:00'}],
        assignments: [
          {id: 'm1', title: 'Quiz', due_at: '2026-09-10T14:00:00+00:00', kind: 'mcq_set'},
          {id: 'f1', title: 'Deck', due_at: '2026-09-12T14:00:00+00:00', kind: asFlash ? 'flashcards' : 'mcq_set'}],
        submissions: [
          {id: 'x1', assignment_id: 'm1', student_id: 's1', score: 4, max_score: 8, status: 'complete',
           completed_at: '2026-09-09T10:00:00+00:00', submitted_at: '2026-09-09T10:00:00+00:00', is_late: false},
          {id: 'x2', assignment_id: 'm1', student_id: 's2', score: 4, max_score: 8, status: 'complete',
           completed_at: '2026-09-09T11:00:00+00:00', submitted_at: '2026-09-09T11:00:00+00:00', is_late: false},
          {id: 'x3', assignment_id: 'f1', student_id: 's1', score: 10, max_score: 10, status: 'complete',
           completed_at: '2026-09-11T10:00:00+00:00', submitted_at: '2026-09-11T10:00:00+00:00', is_late: false},
          {id: 'x4', assignment_id: 'f1', student_id: 's2', score: 10, max_score: 10, status: 'complete',
           completed_at: '2026-09-13T10:00:00+00:00', submitted_at: '2026-09-13T10:00:00+00:00', is_late: true}],
        week: {start_at: '2026-09-07T00:00:00.000Z', end_at: '2026-09-14T00:00:00.000Z'}
      };
      var now = Date.parse('2026-09-20T12:00:00Z');
      var papers = L.buildPapers(pack, now);
      var mx = L.buildMatrix(pack, papers, now);
      var fi = papers.filter(function (p) { return p.id === 'f1'; })[0].idx;
      return {classMean: mx.classMean, s1: mx.studentAvg.s1, s2: mx.studentAvg.s2,
              flashMean: mx.colMean[fi], flashSub: mx.colSub[fi], flashLate: mx.colLate[fi],
              flashKind: papers[fi].kind, submitted: mx.rows.map(function (r) { return r.submitted[fi]; }),
              newest: L.newestMarkedIdx(papers), mcqIdx: papers.filter(function (p) { return p.id === 'm1'; })[0].idx};
    })(%s)
    """
    got = p.eval(probe % "true")
    ctl = p.eval(probe % "false")
    print("   cellOf probe:", json.dumps(got), " control:", json.dumps(ctl))
    check(got and got["classMean"] == 50, "cellOf: class mean 50 with one MCQ at 50% and one flashcard set at 100%",
          str(got and got["classMean"]))
    check(got and got["s1"] == 50 and got["s2"] == 50, "cellOf: every pupil average 50")
    check(got and got["flashMean"] is None, "cellOf: the flashcard column has no mean")
    check(got and got["flashSub"] == 2 and got["submitted"] == [True, True],
          "cellOf: a finished flashcard set IS handed in (2 of 2)")
    check(got and got["flashLate"] == 1, "cellOf: lateness still counts on a flashcard set")
    check(got and got["newest"] == got["mcqIdx"], "newestMarkedIdx skips the flashcard set")
    check(ctl and ctl["classMean"] == 75, "cellOf control: the same pack as two MCQ sets reads 75",
          "proves the probe can see a difference")


def static_checks(check):
    """The generated screens carry the kind split (they are regenerated only
    by build_teacher_port.py; this reads what it wrote)."""
    def read(rel):
        return open(os.path.join(HERE, rel), encoding="utf-8").read()
    cd = read("teacher/class-detail.html")
    check("p.kind === 'flashcards' ? MRB_GO('flashcards', { assignment: p.id })" in cd,
          "class screen: a flashcard row opens the flashcards page")
    check("showDl: p.kind !== 'flashcards'" in cd, "class screen: no Download on a flashcard row")
    check("kind: p.kind, deckId: p.deck_id" in cd, "class screen: Edit carries the kind to MRBSetWork.edit")
    asg = read("teacher/assignment.html")
    check("showDl: pp.kind !== 'flashcards'" in asg, "marking screen: no Download on a flashcard set")
    sd = read("teacher/student-detail.html")
    check("stRow.submitted[i] === true ? '' : null" in sd, "student screen: an ungraded set reads handed in")
    check("stGraded" in sd, "student screen: the average is over graded rows only")
    check("flashcards:'flashcards.html'" in cd, "MRB_PAGE names flashcards.html")
    tl = read("shared/teacher-live.js")
    check('window.location.replace(flashcardsUrl(fcHit.id))' in tl,
          "marking screen: a flashcard set redirects to its progress page")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--shots", default=os.path.join(cdp.gate_tmp(), "flashcard-progress"))
    args = ap.parse_args()
    os.makedirs(args.shots, exist_ok=True)

    fails = []

    def check(ok, what, detail=""):
        print("   %s  %s%s" % ("PASS" if ok else "FAIL", what, ("  - " + detail) if detail else ""))
        if not ok:
            fails.append(what)

    static_checks(check)

    server, port = cdp.serve(HERE)
    base = "http://127.0.0.1:%d" % port
    url = base + "/teacher/flashcards.html?assignment=" + ASSIGN
    try:
        with cdp.Browser() as b:
            # ── make mode, desktop ─────────────────────────────────────────
            p = b.page("about:blank", settle=0.2)
            p.send("Page.addScriptToEvaluateOnNewDocument",
                   {"source": stub(progress(), progress(phase=2),
                                   {"p-ben": DETAIL_BEN, "*": DETAIL_BEN})})
            p.set_viewport(1280, 800)
            p.goto(url, settle=0.5)
            ok = wait_for(p, "document.querySelectorAll('#fp-table tbody tr.fp-row').length===6")
            check(ok, "page renders six pupil rows")
            if not ok:
                print(p.eval("document.body.innerText.slice(0,500)"))
                raise SystemExit(1)
            p.eval("window.__fp_marker = 1; true")

            head = p.eval("document.getElementById('fp-head').innerText")
            check("Atomic structure" in head and "8r/Sc1" in head, "header: title and class")
            check("Due Sat 3 Oct, 15:00" in head, "header: due in London time", head.replace("\n", " | "))
            check("Pupils write the answers" in head and "Secure" in head, "header: mode and rule chips")
            check("Open" in head, "header: Scheduled/Open/Closed chip")
            check("Bring your planner" in head, "header: the teacher's note")
            check(p.eval("!!document.getElementById('fp-edit') && !!document.getElementById('fp-csv')"),
                  "header: Edit and Export CSV")
            strip = p.eval("document.getElementById('fp-strip').innerText")
            check("2/6" in strip and "33%" in strip and "1.6" in strip, "strip: done, % and average sittings",
                  strip.replace("\n", " | "))
            check("Name the particle with no charge" in strip, "strip: reteach list")
            check(p.eval("!!document.querySelector('#fp-reteach sub')"), "strip: formulae render with <sub>")

            p.screenshot(os.path.join(args.shots, "fp-desktop.png"), width=1280, height=800, full_page=True)
            fx = progress()["pupils"]
            order = p.eval(ORDER)
            check(order == ["p-fay", "p-dan", "p-cat", "p-ben", "p-eve", "p-ann"],
                  "default sort: least progress first", str(order))

            cols = p.eval("Array.prototype.map.call(document.querySelectorAll('#fp-table thead .fp-sort'),"
                          "function(b){return b.getAttribute('data-sort');})")
            check(cols == ["pupil", "status", "made", "secured", "sittings", "time", "percard",
                           "rushed", "answers", "last"], "make mode: every column, Made and Answers included",
                  str(cols))
            byid = {x["pupil_id"]: x for x in fx}
            for key in cols:
                for want in ("ascending", "descending"):
                    p.eval("document.querySelector('.fp-sort[data-sort=\"%s\"]').click(); true" % key)
                    time.sleep(0.05)
                    aria = p.eval("document.querySelector('.fp-sort[data-sort=\"%s\"]').parentElement"
                                  ".getAttribute('aria-sort')" % key)
                    o = p.eval(ORDER)
                    vals = [value_of(byid[i], key) for i in o]
                    check(aria == want and monotonic(vals, want == "descending"),
                          "sort %s %s" % (key, want), "%s %s" % (aria, vals))

            # Rushed: an inline marker in Cat's row, never a block.
            r = p.eval("(function(){var e=document.querySelector('tr[data-pupil=\"p-cat\"] .fp-rushed');"
                       "if(!e)return null;var r=e.getBoundingClientRect();"
                       "return {t:e.textContent,h:r.height,d:getComputedStyle(e).display};})()")
            check(bool(r) and r["t"] == "Rushed" and r["h"] < 30 and r["d"] != "block",
                  "Rushed: a small inline marker", str(r))
            check(p.eval("document.querySelectorAll('tr.fp-row .fp-rushed').length") == 1,
                  "Rushed: only on the rushed pupil")
            check(p.eval("document.querySelector('tr[data-pupil=\"p-cat\"] .fp-ans-pending').textContent") == "…2",
                  "Answers: pending shown as …")
            check(p.eval("document.querySelector('tr[data-pupil=\"p-ben\"] .fp-sec').getAttribute('data-known')") == "7",
                  "Secured: known-once carried for the secure rule")

            # the answer-check edge function was fired, with the assignment id
            f = p.eval("window.__FP__.fetches")
            hit = [x for x in f if "flashcard-answer-check" in x["url"]]
            check(bool(hit) and hit[0]["method"] == "POST" and
                  json.loads(hit[0]["body"]) == {"assignment_id": ASSIGN},
                  "answer check: POSTed once on open with {assignment_id}", str(hit))
            pc = [c for c in p.eval("window.__FP__.calls") if c["name"] == "flashcard_progress"]
            check(bool(pc) and pc[0]["args"]["p_assignment"] == ASSIGN and
                  re.match(r"^\d{4}-\d\d-\d\dT", pc[0]["args"]["p_now"] or ""),
                  "progress rpc: p_assignment and an ISO p_now")


            # ── the drawer ─────────────────────────────────────────────────
            p.eval("document.querySelector('.fp-sort[data-sort=\"pupil\"]').click(); true")
            p.eval("document.querySelector('tr[data-pupil=\"p-ben\"]').click(); true")
            ok = wait_for(p, "document.querySelectorAll('#fp-drawer-body .fp-card').length===3")
            check(ok, "drawer: opens on a row with every card")
            d = p.eval(r"""(function(){
              var c=document.querySelector('#fp-drawer-body .fp-card[data-card="c2"]');
              var pair=c.querySelector('.fp-pair');
              return {name:document.getElementById('fp-drawer-name').textContent,
                mine:pair.querySelector('.fp-mine .fp-side-text').textContent,
                model:pair.querySelector('.fp-model .fp-side-text').textContent,
                side: (function(){var a=pair.querySelector('.fp-mine').getBoundingClientRect(),
                        b=pair.querySelector('.fp-model').getBoundingClientRect();
                        return Math.abs(a.top-b.top)<2 && b.left>a.left;})(),
                check:c.querySelector('.fp-check').getAttribute('data-check'),
                rates:Array.prototype.map.call(c.querySelectorAll('.fp-rate'),function(r){
                  return r.getAttribute('data-rating')+'/'+r.getAttribute('data-phase');}),
                sub:!!document.querySelector('#fp-drawer-body .fp-card[data-card="c1"] .fp-model sub'),
                secured:!!document.querySelector('#fp-drawer-body .fp-card[data-card="c1"] .fp-secured'),
                sessions:document.querySelectorAll('#fp-drawer-body .fp-session').length,
                sesRushed:document.querySelectorAll('#fp-drawer-body .fp-session .fp-rushed').length,
                pending:document.querySelector('#fp-drawer-body .fp-card[data-card="c3"] .fp-check').textContent,
                right:(function(){var r=document.querySelector('.fp-drawer').getBoundingClientRect();
                        return r.right>=window.innerWidth-1 && r.width<window.innerWidth;})()};
            })()""")
            check(d["name"] == "Ben Brown", "drawer: pupil name")
            check(d["mine"] == "electron" and d["model"] == "Neutron" and d["side"],
                  "drawer: pupil answer BESIDE the model answer", str(d))
            check(d["check"] == "no", "drawer: answer-check chip")
            check(d["rates"] == ["not_yet/make", "not_yet/review", "nearly/review"],
                  "drawer: rating history in order, make phase marked", str(d["rates"]))
            check(d["sub"], "drawer: formulae render with <sub>")
            check(d["secured"], "drawer: secured tick")
            check(d["sessions"] == 2 and d["sesRushed"] == 1, "drawer: sittings timeline with rushed marker")
            check(d["pending"] == "Checking", "drawer: pending answer check")
            check(d["right"], "drawer: a right-hand panel on desktop")
            p.screenshot(os.path.join(args.shots, "fp-drawer-desktop.png"), width=1280, height=800, full_page=False)
            copy_drawer = p.eval(COPY_JS)
            a11y_drawer = p.eval(A11Y_JS)
            p.eval("document.getElementById('fp-drawer-close').click(); true")
            check(p.eval("document.getElementById('fp-drawer-back').hidden"), "drawer: closes")

            # ── CSV ────────────────────────────────────────────────────────
            p.eval("document.querySelector('.fp-sort[data-sort=\"pupil\"]').click(); true")  # pupil desc
            p.eval("document.getElementById('fp-csv').click(); true")
            csv = p.eval("window.__MRB_FP_LAST_CSV__")
            lines = csv["text"].lstrip("﻿").strip().split("\r\n") if csv else []
            check(bool(csv) and csv["text"].startswith("﻿"), "CSV: UTF-8 BOM")
            check(bool(csv) and csv["name"] == "8r-Sc1-Atomic-structure.csv", "CSV: filename from class + title",
                  csv and csv["name"])
            check(lines and lines[0] == "Pupil,Status,Made,Secured,Known once,Sittings,Time,Per card,Rushed,Answers,Last active",
                  "CSV: the displayed columns", lines and lines[0])
            check(len(lines) == 7, "CSV: one row per pupil")
            disp = p.eval("Array.prototype.map.call(document.querySelectorAll('#fp-table tbody tr.fp-row .fp-name'),"
                          "function(b){return b.textContent;})")
            check([l.split(",")[0] for l in lines[1:]] == disp, "CSV: in the order displayed", str(disp))
            cat = [l for l in lines if l.startswith("Cat Cole")]
            check(bool(cat) and cat[0].startswith("Cat Cole,In progress,6/10,2/10,3/10,1,2:05,0.9,Yes,")
                  and "2 pending" in cat[0] and re.search(r",20\d\d-(0[1-9]|1[0-2])-\d\d \d\d:\d\d$", cat[0]),
                  "CSV: a row's values", cat and cat[0])

            # ── polling flips a row to Done without a reload ───────────────
            p.eval("window.__FP__.phase = 2; true")
            t0 = time.time()
            ok = wait_for(p, "document.querySelector('tr[data-pupil=\"p-cat\"]').getAttribute('data-status')==='done'",
                          timeout=13.0, step=0.25)
            check(ok, "live: Cat flips to Done by polling", "%.1fs" % (time.time() - t0))
            check(p.eval("window.__fp_marker === 1"), "live: no reload")
            check("3/6" in p.eval("document.getElementById('fp-strip').innerText"), "live: the strip recounts")

            # copy + a11y on the main page
            copy = p.eval(COPY_JS) + copy_drawer
            bad = sorted(set(t for t in copy if len(t) > 48 or FORBIDDEN.search(t)))
            check(not bad, "no explanatory copy", str(bad))
            a = p.eval(A11Y_JS)
            check(not a["small"] and not a11y_drawer["small"], "no mono label under 12px",
                  str(a["small"] + a11y_drawer["small"]))
            check(not a["tiny"], "tap targets >= 44px", str(a["tiny"]))
            errs = [e for e in p.console_errors() if "favicon" not in e and "supabase" not in e.lower()]
            check(not errs, "no console errors", str(errs[:3]))

            # ── Edit ───────────────────────────────────────────────────────
            p.eval("document.getElementById('fp-edit').click(); true")
            ed = p.eval("({open:!document.getElementById('fp-edit-back').hidden,"
                        "d:document.getElementById('fp-ed-due-date').value,"
                        "t:document.getElementById('fp-ed-due-time').value,"
                        "rel:document.getElementById('fp-ed-rel-wrap').hidden})")
            check(ed["open"] and ed["d"] == "2026-10-03" and ed["t"] == "15:00" and ed["rel"],
                  "Edit: opens on the London due time; release locked once released", str(ed))
            p.eval("document.getElementById('fp-ed-title').value='Atoms';"
                   "document.getElementById('fp-ed-due-time').value='16:30';"
                   "document.getElementById('fp-ed-save').click(); true")
            wait_for(p, "document.getElementById('fp-edit-back').hidden")
            ec = [c for c in p.eval("window.__FP__.calls") if c["name"] == "flashcard_edit_assignment"]
            check(bool(ec) and ec[0]["args"] == {"p_id": ASSIGN, "p_title": "Atoms",
                                                 "p_due_at": "2026-10-03T15:30:00.000Z",
                                                 "p_note": "Bring your planner", "p_release_at": None},
                  "Edit: rpc flashcard_edit_assignment with the UTC instant", str(ec and ec[0]["args"]))

            # ── phones: 360 and 390 ────────────────────────────────────────
            for w in (360, 390):
                p.set_viewport(w, 844, settle=0.3)
                m = p.eval("({page: document.documentElement.scrollWidth - document.documentElement.clientWidth,"
                           "box: (function(){var s=document.getElementById('fp-scroll');"
                           "return s.scrollWidth > s.clientWidth;})(),"
                           "sticky: getComputedStyle(document.querySelector('tbody .fp-col-pupil')).position})")
                check(m["page"] <= 1, "%dpx: no horizontal page scroll" % w, str(m))
                check(m["box"], "%dpx: the table scrolls in its own box" % w)
                check(m["sticky"] == "sticky", "%dpx: the pupil column is sticky" % w)
                if w == 390:
                    p.screenshot(os.path.join(args.shots, "fp-phone-390.png"), width=390, height=844, full_page=True)
                    p.eval("document.getElementById('fp-scroll').scrollLeft = 400; true")
                    time.sleep(0.2)
                    left = p.eval("(function(){var a=document.querySelector('tbody .fp-col-pupil').getBoundingClientRect();"
                                  "var s=document.getElementById('fp-scroll').getBoundingClientRect();"
                                  "return Math.abs(a.left-s.left)<2;})()")
                    check(left, "390px: pupil column stays put while the table scrolls")
                    p.eval("document.getElementById('fp-scroll').scrollLeft = 0; true")
                    p.eval("document.querySelector('tr[data-pupil=\"p-ben\"]').click(); true")
                    wait_for(p, "document.querySelectorAll('#fp-drawer-body .fp-card').length===3")
                    full = p.eval("(function(){var r=document.querySelector('.fp-drawer').getBoundingClientRect();"
                                  "return r.left<=1 && r.width>=window.innerWidth-1;})()")
                    check(full, "390px: the drawer is a full-screen sheet")
                    ov = p.eval("document.documentElement.scrollWidth - document.documentElement.clientWidth")
                    check(ov <= 1, "390px: no horizontal scroll with the drawer open")
                    p.screenshot(os.path.join(args.shots, "fp-drawer-390.png"), width=390, height=844, full_page=False)
                    p.eval("document.getElementById('fp-drawer-close').click(); true")

            # ── review mode ───────────────────────────────────────────────
            p2 = b.page("about:blank", settle=0.2)
            rv = progress(mode="review", rule="quick")
            p2.send("Page.addScriptToEvaluateOnNewDocument",
                    {"source": stub(rv, rv, {"*": DETAIL_BEN})})
            p2.set_viewport(1280, 800)
            p2.goto(url, settle=0.5)
            wait_for(p2, "document.querySelectorAll('#fp-table tbody tr.fp-row').length===6")
            cols2 = p2.eval("Array.prototype.map.call(document.querySelectorAll('#fp-table thead .fp-sort'),"
                            "function(b){return b.getAttribute('data-sort');})")
            check("made" not in cols2 and "answers" not in cols2 and len(cols2) == 8,
                  "review mode: no Made, no Answers", str(cols2))
            h2 = p2.eval("document.getElementById('fp-head').innerText")
            check("Ready-made cards" in h2 and "Quick" in h2, "review mode: mode and rule chips")
            check(p2.eval("document.querySelector('tr[data-pupil=\"p-ben\"] .fp-sec').getAttribute('data-known')") is None,
                  "review/quick: no known-once layer")
            p2.eval("document.querySelector('tr[data-pupil=\"p-ben\"]').click(); true")
            wait_for(p2, "document.querySelectorAll('#fp-drawer-body .fp-card').length===3")
            check(p2.eval("document.querySelectorAll('#fp-drawer-body .fp-mine').length") == 0 and
                  p2.eval("document.querySelectorAll('#fp-drawer-body .fp-model').length") == 3,
                  "review mode drawer: the answer only, no pupil answer")
            p2.eval("document.getElementById('fp-drawer-close').click(); true")
            p2.eval("document.getElementById('fp-csv').click(); true")
            csv2 = p2.eval("window.__MRB_FP_LAST_CSV__")
            check(csv2["text"].lstrip("﻿").split("\r\n")[0] ==
                  "Pupil,Status,Secured,Sittings,Time,Per card,Rushed,Last active",
                  "review CSV: the displayed columns")
            p2.screenshot(os.path.join(args.shots, "fp-review-desktop.png"), width=1280, height=800, full_page=True)

            # ── not found ─────────────────────────────────────────────────
            p3 = b.page("about:blank", settle=0.2)
            p3.send("Page.addScriptToEvaluateOnNewDocument", {"source": stub(None, None, {})
                     .replace("return Promise.resolve({data: F.phase === 2 ? F.progress2 : F.progress, error: null});",
                              "return Promise.resolve({data: null, error: {message: 'not_found'}});")})
            p3.goto(url, settle=0.8)
            wait_for(p3, "!document.getElementById('fp-notice').hidden")
            check(p3.eval("document.getElementById('fp-notice-title').textContent") == "Flashcard set not found",
                  "not found: a short label")

            # ── cellOf ────────────────────────────────────────────────────
            cellof_check(b, base, check)
    finally:
        server.shutdown()

    print("\n   screenshots: %s" % args.shots)
    if fails:
        print("\n❌ flashcard_progress_drive: %d failure(s)" % len(fails))
        for f_ in fails:
            print("   · " + f_)
        return 1
    print("\n✅ flashcard_progress_drive: all checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
