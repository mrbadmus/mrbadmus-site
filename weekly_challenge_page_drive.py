#!/usr/bin/env python3
"""weekly_challenge_page_drive.py -- Unit C: weekly-challenge.html and the
teacher's "Set this week's challenge" sheet, in a real browser, against a
STUBBED world (no network, no database).

    python3 weekly_challenge_page_drive.py [--shots DIR]

Exit 0 clean, 1 on any failure.

The page is the built copy (`mrbadmus_site/weekly-challenge.html`) served
locally. Before any page script runs, a script injected with
`Page.addScriptToEvaluateOnNewDocument` replaces the Supabase SDK with a
recording stub (the same table stub flashcard_request_shape_drive.py uses) and
`fetch` with a canned backend, so the page, shared/teacher-guard.js,
shared/teacher-data.js and shared/set-work.js are all the REAL files.

Asserts:
  PRESELECT  ?subject=physics selects Physics exactly as a tap does (button
             reads "Start Physics"); a finished subject still reads "Already
             completed"; ?subject=maths and no query select nothing.
  INVISIBLE  /ready false -> a teacher sees no "Set as homework", and the
             teacher stack (teacher-ds.css, set-work.js ...) is never
             downloaded; /ready true but the viewer is a pupil -> the same.
  CONTROL    /ready true + teacher -> one "Set as homework" per subject; Physics
             opens the sheet listing the teacher's KS4 classes (KS3 left out);
             Set sends the exact POST body; the row reads Set + Undo; Undo
             sends DELETE; a Biology-only class is disabled on Physics.
"""

import json
import os
import sys
import time

REPO = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, REPO)
os.chdir(REPO)

import ks3_browser as cdp
import flashcard_request_shape_drive as F

SITE = "mrbadmus_site"
STUB = F.STUB_JS.replace("order: function () { return api; },",
                         "order: function () { return api; }, not: function () { return api; },", 1)


def tables(role):
    t = F.teacher_tables(False)
    def klass(i, name, ks="KS4"):
        return {"class_id": "c%d" % i, "subject_id": "subj1", "deleted_at": None, "ended_at": None,
                "teacher_id": F.T, "subject": {"id": "subj1", "name": "Science"},
                "class": {"id": "c%d" % i, "name": name, "key_stage": ks, "year_group": 10,
                          "tier": "higher", "science_pathway": "combined",
                          "assignment_day_of_week": 1, "deleted_at": None, "academic_year_id": "ay1"}}
    t["class_teachers"] = [klass(1, "10a/Sc1"), klass(2, "10b/Sc2"), klass(3, "11a/Bi1"),
                           klass(4, "7h/Sc5", "KS3")]
    t["academic_years"] = [{"id": "ay1", "name": "2026-27", "start_date": "2026-09-01",
                            "end_date": "2027-08-31", "deleted_at": None}]
    t["profiles"] = [{"id": F.T, "science_pathway": "combined", "tier": "higher",
                      "key_stage": "KS4", "role": role}]
    return t


def bootstrap(role, ready, theme, attempted):
    status = {}
    if attempted:
        status["chemistry_combined_higher"] = {"attempted": True, "score": 11, "max_score": 15}
    return """
(function () {
  try { localStorage.setItem('mrb-theme', %(theme)s); } catch (e) {}
  window.__RS_TABLES__ = %(tables)s;
  %(stub)s
  var client = window.MrBadmusTeacherGuard.getClient();
  var tok = 'tok-stub';
  client.auth = {
    getSession: function () { return Promise.resolve({ data: { session: {
      access_token: tok, user: { id: %(uid)s } } } }); },
    onAuthStateChange: function () { return { data: { subscription: { unsubscribe: function () {} } } }; },
    getUser: function () { return Promise.resolve({ data: { user: { id: %(uid)s } } }); }
  };
  var sdk = { createClient: function () { return client; } };
  // The CDN <script> would overwrite the stub; make the assignment a no-op.
  Object.defineProperty(window, 'supabase', { get: function () { return sdk; }, set: function () {}, configurable: false });
  window.__reqs = [];
  window.__assetLoads = [];
  var json = function (o, s) { return Promise.resolve({ ok: (s || 200) < 400, status: s || 200,
                                json: function () { return Promise.resolve(o); } }); };
  window.fetch = function (u, init) {
    u = String(u); var m = (init && init.method) || 'GET';
    window.__reqs.push({ url: u, method: m, body: init && init.body });
    if (/challenge\\/ready$/.test(u)) return json({ ready: %(ready)s });
    if (/weekly-challenge\\/status/.test(u)) return json({ status: %(status)s });
    if (/set-work\\/challenge$/.test(u) && m === 'POST') {
      var b = JSON.parse(init.body);
      return json({ assignments: b.class_ids.map(function (c) {
        return { id: 'asg-' + c, class_id: c, class_name: c, due_at: '2026-10-23T09:15:00Z', already_set: false }; }) });
    }
    if (/set-work\\/[^/]+$/.test(u) && m === 'DELETE') return json({ ok: true });
    return json({});
  };
  new PerformanceObserver(function (l) { l.getEntries().forEach(function (e) {
    window.__assetLoads.push(e.name); }); }).observe({ type: 'resource', buffered: true });
})();
""" % {"theme": json.dumps(theme), "tables": json.dumps(tables(role)), "stub": STUB,
       "uid": json.dumps(F.T), "ready": "true" if ready else "false",
       "status": json.dumps(status)}


def scenario(base, query, role="teacher", ready=True, theme="light", attempted=False,
             w=390, h=844):
    """A fresh Chrome for each scenario: one page, one stubbed world, one
    bootstrap. Yields (page) inside a `with`."""
    class _S:
        def __enter__(self_):
            self_.b = cdp.Browser().__enter__()
            page = self_.b.attach()
            page._enable_domains()
            page.set_viewport(w, h)
            page.send("Page.addScriptToEvaluateOnNewDocument",
                      {"source": bootstrap(role, ready, theme, attempted)})
            page.goto(base + query, settle=0.5)
            for _ in range(80):          # init() awaits profile + status
                if page.eval("document.getElementById('picker').style.display") == "block":
                    break
                time.sleep(0.1)
            time.sleep(1.5)               # /ready, then the staff stack
            return page
        def __exit__(self_, *a):
            return self_.b.__exit__(*a)
    return _S()


def main():
    shots = None
    if "--shots" in sys.argv:
        shots = sys.argv[sys.argv.index("--shots") + 1]
        os.makedirs(shots, exist_ok=True)
    fails = []

    def check(name, ok, detail=""):
        print("  %s  %s%s" % ("ok  " if ok else "FAIL", name, ("" if ok else "\n         " + str(detail))))
        if not ok:
            fails.append(name)

    server, port = cdp.serve(SITE)
    base = "http://127.0.0.1:%d/weekly-challenge.html" % port
    try:
        print("PRESELECT")
        with scenario(base, "?subject=physics", role="student") as page:
            check("?subject=physics selects Physics",
                  page.eval("document.getElementById('sc-physics').classList.contains('selected')"))
            txt = page.eval("document.getElementById('btn-start').textContent")
            check("and the button reads Start Physics", txt.startswith("Start Physics"), txt)
            check("and it is enabled", page.eval("document.getElementById('btn-start').disabled") is False)
        with scenario(base, "?subject=chemistry", role="student", attempted=True) as page:
            txt = page.eval("document.getElementById('btn-start').textContent")
            check("a finished subject still reads Already completed", txt.startswith("Already completed"), txt)
            check("and is disabled", page.eval("document.getElementById('btn-start').disabled") is True)
        with scenario(base, "?subject=maths", role="student") as page:
            check("an unknown subject selects nothing",
                  page.eval("document.querySelectorAll('.subject-card.selected').length") == 0)
        with scenario(base, "", role="student") as page:
            check("no query selects nothing",
                  page.eval("document.querySelectorAll('.subject-card.selected').length") == 0)

        print("\nINVISIBLE")
        with scenario(base, "", role="teacher", ready=False) as page:
            check("ready=false: a teacher sees no Set as homework",
                  page.eval("document.querySelectorAll('.sc-hw').length") == 0)
            loads = page.eval("JSON.stringify(window.__assetLoads)")
            check("and set-work.js / teacher-ds.css / teacher-data.js are never downloaded",
                  "set-work" not in loads and "teacher-ds" not in loads and "teacher-data" not in loads, loads)
            check("no overlay exists", page.eval("document.querySelectorAll('[data-sw]').length") == 0)
            reqs = json.loads(page.eval("JSON.stringify(window.__reqs)"))
            check("the only staff request was GET /ready",
                  [r["url"].split("/api/")[-1] for r in reqs if "set-work" in r["url"]]
                  == ["teacher/set-work/challenge/ready"], reqs)
        with scenario(base, "", role="student", ready=True) as page:
            check("a pupil never sees it, even when ready",
                  page.eval("document.querySelectorAll('.sc-hw').length") == 0)
            reqs = json.loads(page.eval("JSON.stringify(window.__reqs)"))
            check("and never even asks /ready", not [r for r in reqs if "set-work" in r["url"]], reqs)

        print("\nCONTROL")
        for (w, h) in ((390, 844), (1280, 900)):
            for theme in ("light", "dark"):
                with scenario(base, "?subject=physics", role="teacher", ready=True, theme=theme,
                              w=w, h=h) as page:
                    tag = "%d %s" % (w, theme)
                    n = page.eval("document.querySelectorAll('.sc-hw').length")
                    check("[%s] one Set as homework per subject" % tag, n == 3, n)
                    if shots:
                        page.screenshot(os.path.join(shots, "weekly-challenge-page-%d-%s.png" % (w, theme)),
                                        width=w, height=h, full_page=False)
                    page.eval("document.querySelector('#sc-physics .sc-hw').click(), 'ok'")
                    time.sleep(1.2)
                    check("[%s] Physics opens the sheet" % tag,
                          page.eval("!document.querySelector('[data-sw=\"challenge-overlay\"]').hidden"))
                    check("[%s] the page's picker did not also change" % tag,
                          page.eval("document.getElementById('sc-physics').classList.contains('selected')"))
                    head = page.eval("document.querySelector('[data-sw=\"challenge-title\"]').textContent")
                    check("[%s] heading" % tag, head == "Set this week\u2019s Physics challenge", head)
                    names = page.eval("JSON.stringify([].map.call(document.querySelectorAll("
                                      "'[data-sw=\"challenge-class\"] .sw-row-name'), function(e){return e.textContent}))")
                    check("[%s] the teacher's KS4 classes, KS3 left out" % tag,
                          json.loads(names) == ["10a/Sc1", "10b/Sc2", "11a/Bi1"], names)
                    dis = page.eval("document.querySelector('[data-sw-ref=\"c3\"]').getAttribute('aria-disabled')")
                    check("[%s] a Biology-only class is disabled for Physics" % tag, dis == "true", dis)
                    if shots:
                        page.screenshot(os.path.join(shots, "teacher-sheet-%d-%s.png" % (w, theme)),
                                        width=w, height=h, full_page=False)
                    page.eval("document.querySelector('[data-sw-ref=\"c1\"] [data-sw=\"challenge-set\"]').click(), 'ok'")
                    time.sleep(0.6)
                    reqs = json.loads(page.eval("JSON.stringify(window.__reqs)"))
                    posts = [r for r in reqs if r["method"] == "POST"]
                    check("[%s] Set sends the exact POST body" % tag,
                          len(posts) == 1 and posts[0]["body"] == json.dumps({"class_ids": ["c1"], "subject": "physics"},
                                                                              separators=(",", ":")),
                          posts)
                    row = page.eval("document.querySelector('[data-sw-ref=\"c1\"]').innerText")
                    check("[%s] the row reads Set + Undo" % tag, "SET" in row.upper() and "UNDO" in row.upper(), repr(row))
                    due = page.eval("document.querySelector('[data-sw=\"challenge-due\"]').textContent")
                    check("[%s] due line is the server's" % tag, due == "Due when it closes, Fri 23 Oct, 10:15", due)
                    if shots:
                        page.screenshot(os.path.join(shots, "teacher-sheet-set-%d-%s.png" % (w, theme)),
                                        width=w, height=h, full_page=False)
                    if (w, theme) == (390, "light"):
                        page.eval("document.querySelector('[data-sw-ref=\"c1\"] [data-sw=\"challenge-undo\"]').click(), 'ok'")
                        time.sleep(0.6)
                        reqs = json.loads(page.eval("JSON.stringify(window.__reqs)"))
                        dels = [r for r in reqs if r["method"] == "DELETE"]
                        check("[%s] Undo sends DELETE /api/teacher/set-work/asg-c1" % tag,
                              len(dels) == 1 and dels[0]["url"].endswith("/api/teacher/set-work/asg-c1"), dels)
                        row = page.eval("document.querySelector('[data-sw-ref=\"c1\"]').innerText")
                        check("[%s] and the row is back to Set" % tag, "UNDO" not in row.upper() and "SET" in row.upper(), repr(row))
                        # close
                        page.eval("document.querySelector('[data-sw=\"challenge-close\"]').click(), 'ok'")
                        check("[%s] Close closes the sheet" % tag,
                              page.eval("document.querySelector('[data-sw=\"challenge-overlay\"]').hidden"))
    finally:
        server.shutdown()

    print("\n%s" % ("FAILED: %d" % len(fails) if fails else "all passed"))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
