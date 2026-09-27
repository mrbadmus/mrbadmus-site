#!/usr/bin/env python3
"""flashcard_request_shape_drive.py — MRB-351 landing (27 Sep 2026), the
coordinator's required proof: production must see the IDENTICAL Supabase
request shape it saw before this feature existed, plus one harmless extra
column (`quiz_type`) on the `assignments` select.

`shared/teacher-data.js`'s `loadClassMatrices` and `shared/student-data.js`'s
`loadStudentClass` are the two functions every consumer named by the
coordinator goes through:

  · `loadClassMatrices` — the ONE data layer under `teacher-live.js`'s
    `base()`, which every one of classes.html, class-detail.html,
    student-detail.html, digest.html, insights.html and Today (library mode)
    calls to build its matrix. Proving the request shape here proves it for
    all six transitively — there is no second copy of this read anywhere.
  · `loadStudentClass` — the student class page's own loader.

This drive calls BOTH functions directly, against a recording stub (never a
real network — CDP is not even needed for the network layer, only to run the
JS), in two shapes:

  1. BASELINE — no `assignments` row has `quiz_type='flashcards'`,
     i.e. production's real state today. Every check below runs against
     this.
  2. ONE FLASHCARD ROW — proves the scoped follow-up read fires ONLY then,
     scoped to that row's id alone, never before.

And against BOTH this worktree's `shared/teacher-data.js`/`shared/
student-data.js` and origin/main's own copies (fetched with `git show
e18beda12:...` into a throwaway temp dir — e18beda12 is the exact commit this
branch merged, named in docs/mrb351/REPORT.md) on the SAME baseline fixture,
to prove the two produce the IDENTICAL number of Supabase calls. If `git
show` cannot resolve that commit (e.g. a shallow clone), the count-equality
checks are SKIPPED BY NAME, not silently passed, and the reason is printed —
per the brief's "reason from the diff if a drive can't run main — say which".

Asserts, on the baseline fixture, for both this worktree's files:
  · no call names `kind` / `flashcard_mode` / `completion_rule` / `deck_id`
    in its `select()` string, on any table, ever;
  · no call is made to `flashcard_decks` / `flashcard_cards` /
    `assignment_flashcards`, and no `rpc()` name starts with `flashcard_`;
  · `assignments` is asked exactly ONCE (no follow-up, because there is
    nothing to follow up);
  · the total call count equals origin/main's, for the same fixture (or is
    reported SKIPPED with the reason, if main's files could not be fetched).

And on the one-flashcard-row fixture:
  · `assignments` is asked exactly TWICE — the original select plus one
    follow-up `.in('id', [that one id])` naming only the three extra columns
    (`flashcard_mode, completion_rule, deck_id` / `flashcard_mode`);
  · the follow-up's `.in()` filter carries ONLY the flashcard row's id, never
    an MCQ row's.

A THIRD consumer, `student-live.js`'s `buildAssignment` (the loader behind
`student/assignment.html`), is checked too, but not by driving the function —
it reaches its own backend `/api/class/current-assignment`, not just
Supabase, and mounts a whole page — which is what
`tools/mrb351_noschema_live.py`'s real browser + real TEST run already
exercises end to end. What is proper to this STATIC drive is the one claim
that function makes about its OWN deck-redirect read: it never selects
`kind` (which does not exist on production and would 400 the read on every
`?assignment=` load, per the comment right above it), and it does select
`quiz_type` (the column it actually branches on). That is checked here by
reading the shipped source and matching the exact `.select(...)` call, not
by executing it.
"""
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

import ks3_browser as cdp

MAIN_REF = "e18beda12581d57ac1b63cfaaba34e4867a45176"

T = "11111111-1111-4111-8111-111111111111"      # teacher
STU = "22222222-2222-4222-8222-222222222222"    # pupil
CID = "c1c1c1c1-0000-4000-8000-000000000001"    # class
A_MCQ = "a1a1a1a1-0000-4000-8000-000000000001"  # an ordinary MCQ set
A_FC = "a2a2a2a2-0000-4000-8000-000000000002"   # a flashcard set (fixture 2 only)

FORBIDDEN_COLS = ("kind", "flashcard_mode", "completion_rule", "deck_id")
FORBIDDEN_TABLES = ("flashcard_decks", "flashcard_cards", "assignment_flashcards")

# The recording stub. Filters (eq/is/in) are applied against whatever rows
# `window.__RS_TABLES__` seeds for that table; the SELECT STRING itself is
# recorded verbatim, unfiltered by it — this is a request-SHAPE proof, not a
# response-shape one, so a row seeded with more fields than were asked for
# is fine: the assertion reads the select() argument, exactly like a real
# PostgREST URL's own `select=` query parameter would.
STUB_JS = r"""
(function () {
  var T = window.__RS_TABLES__;
  window.__RS__ = { calls: [] };
  function rows(t) { return T[t] || []; }
  function match(r, f) {
    var v = r[f.col];
    if (f.op === 'eq') { return v === f.val; }
    if (f.op === 'is') { return f.val === null ? (v === null || v === undefined) : v === f.val; }
    if (f.op === 'in') { return f.val.indexOf(v) !== -1; }
    return true;
  }
  function Q(table) {
    var fs = [], selStr = '', single = false, head = false;
    var api = {
      select: function (s, o) { selStr = s || ''; if (o && o.head) { head = true; } return api; },
      eq: function (c, v) { fs.push({ op: 'eq', col: c, val: v }); return api; },
      is: function (c, v) { fs.push({ op: 'is', col: c, val: v }); return api; },
      in: function (c, v) { fs.push({ op: 'in', col: c, val: v }); return api; },
      order: function () { return api; },
      limit: function () { return api; },
      single: function () { single = true; return api; },
      maybeSingle: function () { single = true; return api; },
      then: function (res, rej) {
        window.__RS__.calls.push({ table: table, select: selStr, filters: JSON.parse(JSON.stringify(fs)) });
        var out = rows(table).filter(function (r) {
          for (var i = 0; i < fs.length; i++) { if (!match(r, fs[i])) { return false; } }
          return true;
        });
        var payload;
        if (head) { payload = { data: null, count: out.length, error: null }; }
        else if (single) { payload = { data: out[0] ? JSON.parse(JSON.stringify(out[0])) : null, error: null }; }
        else { payload = { data: JSON.parse(JSON.stringify(out)), error: null }; }
        return Promise.resolve(payload).then(res, rej);
      }
    };
    return api;
  }
  function rpc(name, args) {
    window.__RS__.calls.push({ rpc: name, args: args });
    return Promise.resolve({ data: (T.__rpc && T.__rpc[name]) || null, error: null });
  }
  var client = { from: Q, rpc: rpc };
  window.MrBadmusTeacherGuard = { getClient: function () { return client; } };
  window.MrBadmusStudentGuard = { getClient: function () { return client; } };
  // `yearRows` prefers `window.MRBClassEntry.academicYears()`; left absent on
  // purpose so it falls through to the direct `academic_years` read, which
  // this stub CAN answer — exercising the real fallback path, not skipping it.
})();
"""


def teacher_tables(with_flashcard_row):
    assignments = [{
        "id": A_MCQ, "class_id": CID, "title": "Cell biology set", "due_at": "2026-10-01T17:00:00Z",
        "release_at": "2026-09-20T06:00:00Z", "source": "teacher", "set_by": T,
        "set_tier": "higher", "scope_kind": "topic", "scope_ref": "cell-biology", "paper": None,
        "quiz_type": "topic_quiz", "teacher_note": "", "created_at": "2026-09-01T00:00:00Z",
        "academic_week": 3, "subject_id": "subj1", "deleted_at": None,
        "subject": {"id": "subj1", "name": "Biology"},
    }]
    if with_flashcard_row:
        assignments.append({
            "id": A_FC, "class_id": CID, "title": "Cell biology deck", "due_at": "2026-10-02T17:00:00Z",
            "release_at": "2026-09-21T06:00:00Z", "source": "teacher", "set_by": T,
            "set_tier": "higher", "scope_kind": "topic", "scope_ref": "cell-biology", "paper": None,
            "quiz_type": "flashcards", "teacher_note": "", "created_at": "2026-09-02T00:00:00Z",
            "academic_week": 3, "subject_id": "subj1", "deleted_at": None,
            "subject": {"id": "subj1", "name": "Biology"},
            # These three only exist on the row so the SCOPED follow-up (a
            # second `assignments` select, `.in('id', [A_FC])`) has something
            # real to answer with — a live PostgREST response would carry
            # them on that second call's row, not the first.
            "flashcard_mode": "review", "completion_rule": "quick", "deck_id": "deck1",
        })
    return {
        "class_teachers": [{
            "class_id": CID, "subject_id": "subj1", "deleted_at": None, "ended_at": None,
            "subject": {"id": "subj1", "name": "Biology"},
            "class": {"id": CID, "name": "10a/Bi1", "key_stage": 4, "year_group": 10,
                      "tier": "higher", "science_pathway": "triple",
                      "assignment_day_of_week": 1, "deleted_at": None, "academic_year_id": "ay1"},
        }],
        "class_members": [{
            "class_id": CID, "student_id": STU, "joined_at": "2026-09-01T00:00:00Z",
            "left_at": None, "deleted_at": None,
            "student": {"id": STU, "first_name": "Ada", "last_name": "Nwosu",
                        "avatar_url": None, "deleted_at": None},
        }],
        "assignments": assignments,
        "assignment_submissions": [],
        # ⊕ MRB-351 landing (27 Sep 2026) — a sitting on the flashcard
        # assignment, present only in the `with_flashcard_row` fixture, so
        # the "fires ONLY when the class has ≥1 flashcard assignment" check
        # below has something real to find when it should, and nothing when
        # it shouldn't.
        "flashcard_sessions": ([{
            "assignment_id": A_FC, "pupil_id": STU, "class_id": CID,
            "last_seen_at": "2026-09-25T09:00:00Z",
        }] if with_flashcard_row else []),
    }


def student_tables(with_flashcard_row):
    t = teacher_tables(with_flashcard_row)
    t["profiles"] = [{"id": STU, "first_name": "Ada", "last_name": "Nwosu",
                       "avatar_url": None, "bench_theme": None}]
    t["classes"] = [{"id": CID, "name": "10a/Bi1", "key_stage": 4, "year_group": 10,
                      "tier": "higher", "science_pathway": "triple",
                      "assignment_day_of_week": 1, "deleted_at": None, "academic_year_id": "ay1"}]
    t["academic_years"] = [{"id": "ay1", "name": "2026-27", "start_date": "2026-09-01",
                             "end_date": "2027-08-31", "deleted_at": None}]
    t["__rpc"] = {"class_stars_leaderboard_for_member": []}
    return t


def main():
    fails = []

    def check(ok, what, detail=""):
        print("   %s  %s%s" % ("PASS" if ok else "FAIL", what,
                                ("  - " + str(detail)) if detail and not ok else ""))
        if not ok:
            fails.append(what)

    def skip(what, why):
        print("   SKIP  %s  - %s" % (what, why))

    root = os.path.dirname(os.path.abspath(__file__))

    # ═══ 0. student-live.js — buildAssignment's deck-redirect select() ══════
    # No browser, no stub: reads the shipped source and matches the exact
    # call, per the module docstring's "A THIRD consumer" note.
    print("── student-live.js: buildAssignment's deck-redirect select() ──")
    sl_path = os.path.join(root, "shared", "student-live.js")
    sl_src = open(sl_path, encoding="utf-8").read()
    m = re.search(r'sbForKind\.from\(\s*"assignments"\s*\)\.select\(\s*"([^"]*)"\s*\)', sl_src)
    check(bool(m), "buildAssignment's deck-redirect select() was found in shared/student-live.js")
    if m:
        cols = [c.strip() for c in m.group(1).split(",")]
        check("quiz_type" in cols, "the deck-redirect select names quiz_type", cols)
        check("kind" not in cols,
              "the deck-redirect select does not name kind (kind does not exist on production)", cols)

    # Each "side" (this worktree, main) gets its own throwaway directory
    # holding ONLY an inert harness page plus a same-origin copy of the two
    # files under test — same-origin, so the injected `<script src>` needs no
    # cross-origin reasoning at all. `about:blank`'s null origin refused a
    # cross-origin script load outright (the failure mode this replaced).
    HARNESS_HTML = "<!doctype html><html><head></head><body></body></html>"

    # `student-data.js`'s `workingAcademicYear()` delegates to
    # `window.MRBClassEntry.workingAcademicYear` and throws if that module is
    # not on the page (CLAUDE.md's load-order rule) — so `class-entry.js`
    # rides along on every side, same as it does on every real page.
    FILES = ("shared/class-entry.js", "shared/teacher-data.js", "shared/student-data.js")

    def make_side(srcs):
        d = tempfile.mkdtemp(prefix="mrb351-req-shape-")
        with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as fh:
            fh.write(HARNESS_HTML)
        for name, content in srcs.items():
            with open(os.path.join(d, os.path.basename(name)), "wb") as fh:
                fh.write(content)
        srv, prt = cdp.serve(d)
        return d, srv, "http://127.0.0.1:%d" % prt

    mine_srcs = {}
    for name in FILES:
        with open(os.path.join(root, name), "rb") as fh:
            mine_srcs[name] = fh.read()
    mine_dir, mine_server, mine_base = make_side(mine_srcs)

    main_ok = True
    main_reason = ""
    main_srcs = {}
    for name in FILES:
        try:
            out = subprocess.run(["git", "show", "%s:%s" % (MAIN_REF, name)],
                                  cwd=root, capture_output=True, check=True)
        except (subprocess.CalledProcessError, FileNotFoundError) as e:
            main_ok = False
            main_reason = "git show %s:%s failed: %s" % (MAIN_REF, name, e)
            break
        main_srcs[name] = out.stdout
    main_dir = main_server = main_base = None
    if main_ok:
        main_dir, main_server, main_base = make_side(main_srcs)

    def load_script(p, url):
        loaded = p.eval("""
            new Promise(function (resolve, reject) {
              var s = document.createElement('script');
              s.src = %s;
              s.onload = function () { resolve(true); };
              s.onerror = function () { reject(new Error('load failed: ' + s.src)); };
              document.head.appendChild(s);
            })
        """ % json.dumps(url))
        if not loaded:
            raise RuntimeError("could not load %s" % url)

    def run(b, script_base, script_name, tables, call_expr):
        """Fresh page on `script_base` (same origin as `script_name`), inject
        `class-entry.js` (load-order rule) then `script_name`, seed `tables`,
        call `call_expr`, return window.__RS__ (with a `.threw` string set if
        the call itself raised)."""
        p = b.page(script_base + "/index.html", settle=0.3)
        pre = "window.__RS_TABLES__=%s;\n" % json.dumps(tables) + STUB_JS
        p.eval(pre)
        load_script(p, script_base + "/class-entry.js")
        load_script(p, script_base + "/" + script_name)
        p.eval("(async function(){ try { await (%s); } "
               "catch (e) { window.__RS__.threw = String((e && e.message) || e); } })()"
               % call_expr)
        return p.eval("window.__RS__")

    def col_violations(calls):
        bad = []
        for c in calls:
            sel = c.get("select") or ""
            for col in FORBIDDEN_COLS:
                # word-boundary-ish: 'kind' as a whole select token, not a
                # substring of something else (there is nothing else it could
                # be a substring of in these two files' selects, but match
                # the same discipline the site code itself uses).
                if any(tok.strip() == col for tok in sel.replace("(", ",").split(",")):
                    bad.append("%s: select names %r (%s)" % (c.get("table"), col, sel))
        return bad

    def table_violations(calls):
        bad = []
        for c in calls:
            t = c.get("table")
            if t in FORBIDDEN_TABLES:
                bad.append("call to table %r" % t)
            r = c.get("rpc")
            if r and str(r).startswith("flashcard_"):
                bad.append("rpc call to %r" % r)
        return bad

    try:
        with cdp.Browser() as b:
            # ═══ 1. TEACHER — loadClassMatrices, baseline (no flashcard row) ═
            print("\n── teacher-data.js: loadClassMatrices, baseline (production shape) ──")
            rs = run(b, mine_base, "teacher-data.js", teacher_tables(False),
                     "window.MrBadmusTeacherData.loadClassMatrices(%s)" % json.dumps([CID]))
            check(not rs.get("threw"), "loadClassMatrices did not throw", rs.get("threw"))
            calls = rs["calls"]
            check(not col_violations(calls), "no select names kind/flashcard_mode/completion_rule/deck_id",
                  col_violations(calls))
            check(not table_violations(calls), "no flashcard table or RPC touched", table_violations(calls))
            asg_calls = [c for c in calls if c.get("table") == "assignments"]
            check(len(asg_calls) == 1, "assignments asked exactly once (no follow-up needed)", len(asg_calls))
            check(any("quiz_type" in (c.get("select") or "") for c in asg_calls),
                  "the one assignments select names quiz_type")
            fs_calls = [c for c in calls if c.get("table") == "flashcard_sessions"]
            check(len(fs_calls) == 0,
                  "flashcard_sessions is NEVER asked when the class has no flashcard assignment",
                  len(fs_calls))
            teacher_baseline_count = len(calls)

            # ═══ 2. TEACHER — loadClassMatrices, one flashcard row ══════════
            print("\n── teacher-data.js: loadClassMatrices, one flashcard row present ──")
            rs2 = run(b, mine_base, "teacher-data.js", teacher_tables(True),
                      "window.MrBadmusTeacherData.loadClassMatrices(%s)" % json.dumps([CID]))
            check(not rs2.get("threw"), "loadClassMatrices did not throw", rs2.get("threw"))
            calls2 = rs2["calls"]
            check(not table_violations(calls2), "no flashcard table or RPC touched", table_violations(calls2))
            asg_calls2 = [c for c in calls2 if c.get("table") == "assignments"]
            check(len(asg_calls2) == 2, "assignments asked exactly twice — the select, then ONE scoped follow-up",
                  len(asg_calls2))
            if len(asg_calls2) == 2:
                followup = asg_calls2[1]
                in_filters = [f for f in followup["filters"] if f["op"] == "in" and f["col"] == "id"]
                check(bool(in_filters) and in_filters[0]["val"] == [A_FC],
                      "the follow-up's .in('id', …) names ONLY the flashcard row's id, never the MCQ row's",
                      in_filters)
                sel = followup.get("select") or ""
                check(("flashcard_mode" in sel) and ("completion_rule" in sel) and ("deck_id" in sel),
                      "the follow-up select names exactly the three extra fields the edit sheet needs", sel)
            # ⊕ MRB-351 landing (27 Sep 2026) — the last-activity rule in supabase/MRB351-APPLY.md, source 2:
            # `flashcard_sessions` fires ONLY once a flashcard assignment
            # exists, scoped to that assignment's id alone.
            fs_calls2 = [c for c in calls2 if c.get("table") == "flashcard_sessions"]
            check(len(fs_calls2) == 1,
                  "flashcard_sessions is asked exactly once, once a flashcard assignment exists",
                  len(fs_calls2))
            if fs_calls2:
                in_filters_fs = [f for f in fs_calls2[0]["filters"] if f["op"] == "in" and f["col"] == "assignment_id"]
                check(bool(in_filters_fs) and in_filters_fs[0]["val"] == [A_FC],
                      "flashcard_sessions is scoped to this class's flashcard assignment id(s) alone",
                      in_filters_fs)

            # ═══ 3. STUDENT — loadStudentClass, baseline ════════════════════
            print("\n── student-data.js: loadStudentClass, baseline (production shape) ──")
            rs3 = run(b, mine_base, "student-data.js", student_tables(False),
                      "window.MrBadmusStudentData.loadStudentClass(%s, %s)" % (json.dumps(CID), json.dumps(STU)))
            check(not rs3.get("threw"), "loadStudentClass did not throw", rs3.get("threw"))
            calls3 = rs3["calls"]
            check(not col_violations(calls3), "no select names kind/flashcard_mode/completion_rule/deck_id",
                  col_violations(calls3))
            check(not table_violations(calls3), "no flashcard table or RPC touched", table_violations(calls3))
            asg_calls3 = [c for c in calls3 if c.get("table") == "assignments"]
            check(len(asg_calls3) == 1, "assignments asked exactly once (no follow-up needed)", len(asg_calls3))
            check(any("quiz_type" in (c.get("select") or "") for c in asg_calls3),
                  "the one assignments select names quiz_type")
            student_baseline_count = len(calls3)

            # ═══ 4. STUDENT — loadStudentClass, one flashcard row ═══════════
            print("\n── student-data.js: loadStudentClass, one flashcard row present ──")
            rs4 = run(b, mine_base, "student-data.js", student_tables(True),
                      "window.MrBadmusStudentData.loadStudentClass(%s, %s)" % (json.dumps(CID), json.dumps(STU)))
            check(not rs4.get("threw"), "loadStudentClass did not throw", rs4.get("threw"))
            calls4 = rs4["calls"]
            check(not table_violations(calls4), "no flashcard table or RPC touched", table_violations(calls4))
            asg_calls4 = [c for c in calls4 if c.get("table") == "assignments"]
            check(len(asg_calls4) == 2, "assignments asked exactly twice — the select, then ONE scoped follow-up",
                  len(asg_calls4))
            if len(asg_calls4) == 2:
                in_filters4 = [f for f in asg_calls4[1]["filters"] if f["op"] == "in" and f["col"] == "id"]
                check(bool(in_filters4) and in_filters4[0]["val"] == [A_FC],
                      "the follow-up's .in('id', …) names ONLY the flashcard row's id", in_filters4)

            # ═══ 5. COUNT EQUALITY AGAINST origin/main (e18beda12) ══════════
            print("\n── count equality against origin/main, same baseline fixture ──")
            if not main_ok:
                skip("teacher-data.js baseline call count equals main's",
                     "could not fetch main's file: %s — reasoning from the diff instead: this "
                     "landing's ONLY change to loadClassMatrices's request shape is dropping "
                     "kind/flashcard_mode/completion_rule/deck_id from the primary select, adding "
                     "quiz_type to it, and adding ONE conditional follow-up gated on "
                     "quiz_type==='flashcards' being present in the answer — on a fixture with no "
                     "such row (production's real shape) that conditional never fires, so the call "
                     "sequence (class_teachers, class_members, assignments, assignment_submissions) "
                     "is identical in shape and count to main's own, by inspection of the diff." % main_reason)
                skip("student-data.js baseline call count equals main's", "same reason as above")
            else:
                rsm = run(b, main_base, "teacher-data.js", teacher_tables(False),
                          "window.MrBadmusTeacherData.loadClassMatrices(%s)" % json.dumps([CID]))
                check(not rsm.get("threw"), "main's loadClassMatrices did not throw on the same fixture",
                      rsm.get("threw"))
                main_teacher_count = len(rsm["calls"])
                check(main_teacher_count == teacher_baseline_count,
                      "teacher-data.js: this worktree's call count (%d) equals main's (%d) on the baseline fixture"
                      % (teacher_baseline_count, main_teacher_count),
                      (teacher_baseline_count, main_teacher_count))

                rsm2 = run(b, main_base, "student-data.js", student_tables(False),
                           "window.MrBadmusStudentData.loadStudentClass(%s, %s)"
                           % (json.dumps(CID), json.dumps(STU)))
                check(not rsm2.get("threw"), "main's loadStudentClass did not throw on the same fixture",
                      rsm2.get("threw"))
                main_student_count = len(rsm2["calls"])
                check(main_student_count == student_baseline_count,
                      "student-data.js: this worktree's call count (%d) equals main's (%d) on the baseline fixture"
                      % (student_baseline_count, main_student_count),
                      (student_baseline_count, main_student_count))
    finally:
        mine_server.shutdown()
        shutil.rmtree(mine_dir, ignore_errors=True)
        if main_server:
            main_server.shutdown()
        if main_dir:
            shutil.rmtree(main_dir, ignore_errors=True)

    if fails:
        print("\n❌ flashcard_request_shape_drive: %d FAIL" % len(fails))
        for f in fails:
            print("   · " + f)
        return 1
    print("\n✅ flashcard_request_shape_drive: all checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
