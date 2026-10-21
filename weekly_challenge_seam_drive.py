#!/usr/bin/env python3
"""weekly_challenge_seam_drive.py -- Unit C: the data layers' handling of a
teacher-set weekly challenge row, against a recording stub (no network).

    python3 weekly_challenge_seam_drive.py

Exit 0 clean, 1 on any failure.

A teacher-set weekly challenge is an `assignments` row with `quiz_type =
'weekly_challenge'`, no questions and no submissions. This calls the same two
loaders `flashcard_request_shape_drive.py` calls -- `loadClassMatrices` and
`loadStudentClass` -- plus `loadTeacherClasses` (what Today and My classes draw
their counts from), over a class that has one ordinary set AND one challenge
row, and asserts:

  TEACHER  the challenge is in NONE of the lists any figure is derived from:
             pack.assignments holds only the ordinary set; pack.challenges
             holds the challenge (a title and a deadline); the per-class
             `assignment_count` is 1, not 2; and the request count is
             unchanged by it (no follow-up read for a challenge).
  STUDENT  the challenge arrives as a card with kind 'weekly_challenge'
             (shared/student-live.js takes it out of every question-set sum),
             the ordinary set stays kind 'mcq_set', and no extra read fires.
"""

import json
import os
import sys
import tempfile

REPO = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, REPO)
os.chdir(REPO)

import ks3_browser as cdp
import flashcard_request_shape_drive as F

A_CH = "a3a3a3a3-0000-4000-8000-000000000003"
# The shared stub has no `.not()`, which `loadClassMetrics` chains; without it
# that function throws and degrades to zero counts, hiding the thing asserted.
STUB = F.STUB_JS.replace("order: function () { return api; },",
                         "order: function () { return api; }, not: function () { return api; },", 1)
assert "not: function" in STUB


def with_challenge(tables):
    t = json.loads(json.dumps(tables))
    for ct in t["class_teachers"]:
        ct.setdefault("teacher_id", F.T)
    t["assignments"].append({
        "id": A_CH, "class_id": F.CID, "title": "Weekly challenge: Physics",
        "due_at": "2026-10-23T09:15:00Z", "release_at": "2026-10-21T10:00:00Z",
        "source": "teacher", "set_by": F.T, "set_tier": None, "scope_kind": None,
        "scope_ref": None, "paper": None, "quiz_type": "weekly_challenge",
        "teacher_note": "", "created_at": "2026-10-21T10:00:00Z", "academic_week": 8,
        "subject_id": "subj1", "deleted_at": None, "set_subject": "physics",
        "subject": {"id": "subj1", "name": "Physics"},
    })
    return t


def main():
    fails = []

    def check(ok, what, detail=""):
        print("   %s  %s%s" % ("PASS" if ok else "FAIL", what,
                               ("  - " + str(detail)) if detail and not ok else ""))
        if not ok:
            fails.append(what)

    d = tempfile.mkdtemp(prefix="wc-seam-")
    with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as fh:
        fh.write("<!doctype html><html><head></head><body></body></html>")
    for name in ("shared/class-entry.js", "shared/teacher-data.js", "shared/student-data.js"):
        with open(os.path.join(REPO, name), "rb") as src, \
                open(os.path.join(d, os.path.basename(name)), "wb") as dst:
            dst.write(src.read())
    srv, prt = cdp.serve(d)
    base = "http://127.0.0.1:%d" % prt

    def load_script(p, url):
        p.eval("""new Promise(function (resolve, reject) {
              var s = document.createElement('script'); s.src = %s;
              s.onload = function () { resolve(true); };
              s.onerror = function () { reject(new Error('load failed')); };
              document.head.appendChild(s); })""" % json.dumps(url))

    def run(b, script, tables, expr):
        p = b.page(base + "/index.html", settle=0.3)
        p.eval("window.__RS_TABLES__=%s;\n" % json.dumps(tables) + STUB)
        p.eval("window.MrBadmusTeacherGuard.getClient().auth = {getSession: function () {"
               "return Promise.resolve({data: {session: {user: {id: %s}}}}); }}, 'ok'" % json.dumps(F.T))
        load_script(p, base + "/class-entry.js")
        load_script(p, base + "/" + script)
        p.eval("(async function(){ try { window.__OUT__ = await (%s); } "
               "catch (e) { window.__RS__.threw = String((e && e.message) || e); } })()" % expr)
        return p.eval("JSON.stringify({rs: window.__RS__, out: window.__OUT__})")

    try:
        with cdp.Browser() as b:
            print("── teacher-data.js: loadClassMatrices ──")
            base_calls = json.loads(run(b, "teacher-data.js", F.teacher_tables(False),
                "window.MrBadmusTeacherData.loadClassMatrices(%s)" % json.dumps([F.CID])))
            r = json.loads(run(b, "teacher-data.js", with_challenge(F.teacher_tables(False)),
                "window.MrBadmusTeacherData.loadClassMatrices(%s)" % json.dumps([F.CID])))
            check(not r["rs"].get("threw"), "loadClassMatrices did not throw", r["rs"].get("threw"))
            pack = (r["out"] or {}).get(F.CID) or {}
            check([a["id"] for a in pack.get("assignments", [])] == [F.A_MCQ],
                  "pack.assignments holds only the ordinary set", [a["id"] for a in pack.get("assignments", [])])
            check([c["id"] for c in pack.get("challenges", [])] == [A_CH],
                  "pack.challenges holds the challenge", pack.get("challenges"))
            ch = (pack.get("challenges") or [{}])[0]
            check(ch.get("title") == "Weekly challenge: Physics" and ch.get("due_at") == "2026-10-23T09:15:00Z",
                  "with its title and its deadline", ch)
            check(pack.get("catch_ups") == [], "it is not a catch-up either", pack.get("catch_ups"))
            check(len(r["rs"]["calls"]) == len(base_calls["rs"]["calls"]),
                  "the request count is unchanged by a challenge row (no follow-up read)",
                  (len(r["rs"]["calls"]), len(base_calls["rs"]["calls"])))
            subs_q = [c for c in r["rs"]["calls"] if c.get("table") == "assignment_submissions"]
            leaked = [c for c in subs_q for f in c.get("filters", []) if f.get("op") == "in" and A_CH in (f.get("val") or [])]
            check(not leaked, "no submissions read is scoped to the challenge's id", leaked)

            print("\n── teacher-data.js: loadTeacherClasses (Today / My classes counts) ──")
            r = json.loads(run(b, "teacher-data.js", with_challenge(F.teacher_tables(False)),
                "window.MrBadmusTeacherData.loadTeacherClasses('ay1')"))
            check(not r["rs"].get("threw"), "loadTeacherClasses did not throw", r["rs"].get("threw"))
            outv = r.get("out")
            row = outv[0] if isinstance(outv, list) and outv else {}
            check(row.get("assignment_count") == 1, "assignment_count counts the ordinary set only (1, not 2)",
                  row.get("assignment_count"))

            print("\n── student-data.js: loadStudentClass ──")
            base_s = json.loads(run(b, "student-data.js", F.student_tables(False),
                "window.MrBadmusStudentData.loadStudentClass(%s, %s)" % (json.dumps(F.CID), json.dumps(F.STU))))
            r = json.loads(run(b, "student-data.js", with_challenge(F.student_tables(False)),
                "window.MrBadmusStudentData.loadStudentClass(%s, %s)" % (json.dumps(F.CID), json.dumps(F.STU))))
            check(not r["rs"].get("threw"), "loadStudentClass did not throw", r["rs"].get("threw"))
            out = r["out"] or {}
            cards = (out.get("assignmentsDueNow") or []) + (out.get("assignmentsComingUp") or []) + (out.get("assignmentsDone") or [])
            kinds = {c["id"]: c.get("kind") for c in cards}
            check(kinds.get(A_CH) == "weekly_challenge", "the challenge card has kind 'weekly_challenge'", kinds)
            check(kinds.get(F.A_MCQ) == "mcq_set", "the ordinary set is still 'mcq_set'", kinds)
            check(len(r["rs"]["calls"]) == len(base_s["rs"]["calls"]),
                  "the request count is unchanged by a challenge row",
                  (len(r["rs"]["calls"]), len(base_s["rs"]["calls"])))
    finally:
        srv.shutdown()

    print("\n%s" % ("FAILED: %d" % len(fails) if fails else "all passed"))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
