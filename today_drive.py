#!/usr/bin/env python3
"""MRB-306 — drive `teacher/today.html`, the teacher's day.

    python3 today_drive.py                  # everything
    python3 today_drive.py --shots DIR      # write screenshots somewhere

⚑ WHAT THIS PROVES, AND WHAT IT DOES NOT.

  It drives the REAL PAGE with a STUBBED CLIENT — the same split, and the
  same reasoning, as `admin_view_drive.py`. The page's own guard, its own
  data layer (`teacher-data.js`'s `loadTimetable`, `loadAcademicYears`,
  `loadClassMatrices`) and its own rendering all run unmodified, against
  fixture rows shaped exactly like the ones the RLS policies return.

  So it proves everything between the rows arriving and the pixels. It does
  NOT prove the RLS — `timetable_entries_own_all` and the reminder policies
  are proved separately by SQL, under real roles, and written up in the
  MRB-306 report. Neither half writes a byte to either project.

⚠️ THE STATES ARE THE POINT. A timetable page is easy to make look right on
  the one day it has lessons. The four cases below are the ones that decide
  whether it is honest:

    weekday     — a day this teacher actually teaches
    weekend     — Saturday: says so, and shows the NEXT teaching day
    empty-day   — a weekday with no lessons: same honest fallback
    no-timetable— no rows at all: the prompt, and no invented lessons

  ⚠️ The clock is FROZEN per case. `schoolWeekday()` reads the real instant,
  so a drive that did not freeze it would pass on a Tuesday and fail on a
  Saturday — the exact defect this file exists to catch.
"""

import argparse, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ks3_browser as cdp

TEACHER = "11111111-1111-1111-1111-111111111111"
YEAR    = "22222222-2222-2222-2222-222222222222"

def klass(cid, name, ks, yg):
    return {"id": cid, "name": name, "key_stage": ks, "year_group": yg,
            "academic_year_id": YEAR, "deleted_at": None, "school_id": "s1"}

def entry(eid, cid, wd, per, name, ks, yg, teacher=None,
          source="seeded", updated="2026-09-01T08:00:00+00:00"):
    """One timetable row. `teacher` and `updated` default to this fixture's own
       teacher and to the seeded import's timestamp; the MRB-326 case below is
       the only caller that passes either, and it passes both."""
    return {"id": eid, "class_id": cid, "weekday": wd, "period": per,
            "week_cycle": None, "source": source, "academic_year_id": YEAR,
            "deleted_at": None, "teacher_id": teacher or TEACHER,
            "updated_at": updated,
            "classes": klass(cid, name, ks, yg)}

# A week shaped like a real one: Monday busy, Wednesday light, Friday empty.
ENTRIES = [
    entry("eeeeeeee-0000-4000-8000-000000000001", "cccccccc-0000-4000-8000-000000000001", 1, 1, "8r/Sc1",  "KS3", 8),
    entry("eeeeeeee-0000-4000-8000-000000000002", "cccccccc-0000-4000-8000-000000000002", 1, 2, "10h/Ph1", "KS4", 10),
    entry("eeeeeeee-0000-4000-8000-000000000003", "cccccccc-0000-4000-8000-000000000003", 1, 4, "7h/Sc5",  "KS3", 7),
    entry("eeeeeeee-0000-4000-8000-000000000004", "cccccccc-0000-4000-8000-000000000001", 3, 2, "8r/Sc1",  "KS3", 8),
    entry("eeeeeeee-0000-4000-8000-000000000005", "cccccccc-0000-4000-8000-000000000002", 3, 5, "10h/Ph1", "KS4", 10),
]

# ── ⊕ MRB-326 · a colleague's lesson, and a slot written twice ───────────
#
# Two rows this fixture's teacher must never see rendered, and one they must
# see EXACTLY ONCE. Both are shapes the served table really can hold:
#
#  · A CO-TEACHER'S ROW on a class this teacher also teaches, at a period
#    this teacher is free (Monday P3). Under `timetable_entries_admin_read`
#    a school_admin's read returns it — it is a lesson of their class, taught
#    by somebody else — and the old class-scoped loader passed it straight
#    through to the page. It must not be rendered, and it must not put a
#    lesson in an empty period.
#
#  · TWO ROWS IN ONE SLOT (Monday P2): the `seeded` import's 10h/Ph1 and the
#    teacher's own later `manual` edit, 7h/Sc5. The DB's unique index cannot
#    always prevent this (a NULL week_cycle and an 'A' one coexist in its
#    key), so the loader collapses on read, newest `updated_at` winning. The
#    period must appear ONCE, showing what the teacher last saved.
#
# ⚠️ The grid the editor draws is one class per (weekday, period) cell, last
# row wins — so a slot that arrives twice is not merely a cosmetic duplicate.
# It is a cell that can be SAVED back wrong, which is how MRB-326's real
# timetable was overwritten.
CO_TEACHER = "33333333-3333-3333-3333-333333333333"

ENTRIES_MIXED = ENTRIES + [
    # a colleague's lesson of 8r/Sc1, in a period this teacher does not teach
    entry("eeeeeeee-0000-4000-8000-000000000006", "cccccccc-0000-4000-8000-000000000001",
          1, 3, "8r/Sc1", "KS3", 8, teacher=CO_TEACHER),
    # the teacher's own later edit of Monday P2 — a different class, newer stamp
    entry("eeeeeeee-0000-4000-8000-000000000007", "cccccccc-0000-4000-8000-000000000003",
          1, 2, "7h/Sc5", "KS3", 7, source="manual",
          updated="2026-09-05T17:30:00+00:00"),
]

# What Monday must look like: the teacher owns P1, P2 and P4, and P2 shows the
# class they saved last.
# ⊕ MRB-326 JOB 3 — "P1", not "PERIOD 1". Design's row stacks the period over
# its clock time in a 92px column, and "PERIOD 1" does not fit that column at
# 21px display. The SLOTS this case is about are unchanged: P1, P2, P4, with
# P2 showing the class the teacher saved last.
MIXED_EXPECTED = [("P1", "8r/Sc1"), ("P2", "7h/Sc5"), ("P4", "7h/Sc5")]

YEARS = [{"id": YEAR, "name": "2026-27", "start_date": "2026-09-01",
          "end_date": "2027-08-31", "deleted_at": None}]

# ⊕ MRB-326, 6 Sep 2026 — THIS TABLE IS NO LONGER LOAD-BEARING FOR `Today`,
# and the reason it stopped being is the whole of MRB-326. It was added on
# 5 Sep because `loadTimetable()` read `class_teachers` for the signed-in user
# and then asked `timetable_entries` for `.in('class_id', myClassIds)` — a
# filter on the CLASS, which for a school_admin (whose RLS read is school-wide)
# returns every teacher's lesson of every class they co-teach, and which the
# editor then saved back over their real timetable. The loader now filters on
# `teacher_id`, which is the only thing that can mean "mine".
#
# The rows are KEPT because `loadTeacherClasses` still reads this table for the
# editor's class picker (case 6), and because a fixture that stopped carrying
# them would stop being able to notice if the class pre-read ever came back.
CLASS_TEACHERS = [
    {"class_id": cid, "teacher_id": TEACHER, "deleted_at": None, "ended_at": None}
    for cid in ("cccccccc-0000-4000-8000-000000000001",
                "cccccccc-0000-4000-8000-000000000002",
                "cccccccc-0000-4000-8000-000000000003")
]

TABLES = {
    "timetable_entries": ENTRIES,
    "academic_years":    YEARS,
    "class_teachers":    CLASS_TEACHERS,
    "classes":           [klass("cccccccc-0000-4000-8000-000000000001","8r/Sc1","KS3",8), klass("cccccccc-0000-4000-8000-000000000002","10h/Ph1","KS4",10),
                          klass("cccccccc-0000-4000-8000-000000000003","7h/Sc5","KS3",7)],
    # ⚠️ EMPTY, and the case that needs a row puts one here. `loadSchoolHold`
    # reads this table; zero rows is "no hold known", which is the state every
    # case except the held one is in.
    "schools":           [],
    "profiles": [{"id": TEACHER, "first_name": "Ada", "last_name": "Nwosu",
                  "display_name": "Ms Nwosu", "role": "teacher", "school_id": "s1"}],
}

STUB_JS = r"""
(function () {
  var S = window.__MRB_STUB__;
  function rows(t) { return (S.tables[t] || []).slice(); }
  function ok(row, f) {
    var v = row[f.col];
    if (f.op === 'eq') { return v === f.val; }
    if (f.op === 'is') { return f.val === null ? (v === null || v === undefined) : v === f.val; }
    if (f.op === 'in') { return f.val.indexOf(v) !== -1; }
    return true;
  }
  function Q(table) {
    var fs = [], one = false;
    var api = {
      select: function () { return api; },
      order:  function () { return api; },
      limit:  function () { return api; },
      eq: function (c, v) { fs.push({op:'eq', col:c, val:v}); return api; },
      is: function (c, v) { fs.push({op:'is', col:c, val:v}); return api; },
      in: function (c, v) { fs.push({op:'in', col:c, val:v}); return api; },
      single: function () { one = true; return api; },
      maybeSingle: function () { one = true; return api; },
      then: function (res, rej) {
        var out = rows(table).filter(function (r) {
          for (var i = 0; i < fs.length; i++) { if (!ok(r, fs[i])) { return false; } }
          return true;
        });
        var payload = one
          ? {data: out[0] || null, error: out.length ? null : {code: 'PGRST116'}}
          : {data: out, error: null};
        S.log.push(table);
        return Promise.resolve(payload).then(res, rej);
      }
    };
    return api;
  }
  var user = {id: S.uid, aud: 'authenticated', role: 'authenticated',
              email: 'stub@drive.invalid', app_metadata: {}, user_metadata: {}};
  var client = {
    from: Q,
    rpc: function () { return Promise.resolve({data: null, error: null}); },
    auth: {
      getUser: function () { return Promise.resolve({data: {user: user}, error: null}); },
      getSession: function () {
        return Promise.resolve({data: {session: {user: user, access_token: 'stub'}}, error: null});
      },
      signOut: function () { return Promise.resolve({error: null}); },
      onAuthStateChange: function () {
        return {data: {subscription: {unsubscribe: function () {}}}};
      }
    }
  };
  /* ⚠️ A GETTER, NOT AN ASSIGNMENT, AND THAT IS THE WHOLE TRICK.
     This script runs at document-start, but the page then loads the real
     supabase-js UMD bundle from the CDN, and that bundle's last act is to
     assign `window.supabase`. A plain assignment here is overwritten by it a
     few milliseconds later, the guard then builds a REAL client with no
     session, `getUser()` fails and the page bounces to auth.html — which
     presents as "the drive renders nothing" with a completely silent
     console. Swallowing the CDN's write keeps the stub in place. */
  var sdk = {createClient: function () { return client; }};
  Object.defineProperty(window, 'supabase', {
    configurable: true,
    get: function () { return sdk; },
    set: function () { /* the CDN bundle's own assignment, ignored */ }
  });
})();
"""
FREEZE = r'''
/* Freeze the clock. `schoolWeekday()` formats a real Date in Europe/London,
   so the only honest way to drive a Saturday is to make it BE Saturday. */
(function () {
  var FIXED = new Date("%s");
  var RealDate = Date;
  function D(a, b, c, d, e, f, g) {
    if (!(this instanceof D)) { return FIXED.toString(); }
    /* ⚠️ ARITY MATTERS. `new Date(str, undefined, undefined…)` is NOT
       `new Date(str)` — the multi-argument form parses its first argument as
       a YEAR, so forwarding a fixed 7 arguments turns every one-argument
       construction in the page into an Invalid Date. That is what the
       weekend case's `RangeError: Invalid time value` was: a bug in this
       harness, not in the page. */
    if (arguments.length === 0) { return new RealDate(FIXED.getTime()); }
    if (arguments.length === 1) { return new RealDate(a); }
    if (arguments.length === 2) { return new RealDate(a, b); }
    if (arguments.length === 3) { return new RealDate(a, b, c); }
    return new RealDate(a, b, c, d, e, f, g);
  }
  D.now = function () { return FIXED.getTime(); };
  D.parse = RealDate.parse;
  D.UTC = RealDate.UTC;
  D.prototype = RealDate.prototype;
  window.Date = D;
})();
'''

PACKS = '''
/* `loadClassMatrices` is stubbed at the DATA-LAYER boundary rather than the
   table boundary: it fans out over several tables with chunking and joins,
   and reproducing that in the tiny query stub would be testing the stub. The
   page's own `describeClass` still runs on these packs unmodified, which is
   the logic under test. */
window.__MRB_PACKS__ = %s;
'''

CLASSES_JS = '''
window.__MRB_CLASSES__ = %s;
'''

PACK_JS = '''
/* ⚠️ A SETTER, NOT A POLL — the same trick STUB_JS uses for `window.supabase`,
   and for the same reason. A `setTimeout` poll LOST THE RACE: teacher-data.js
   assigns `window.MrBadmusTeacherData` synchronously, the page's guard chain
   then resolves against the (fast) stubbed client, and `loadClassMatrices` was
   called before the first 20ms tick ever fired. The real function ran, refused
   the fixture's classes with "not authorised", and the drive read three empty
   cells as a page bug.

   ⊕ WORTH RECORDING: the page behaved CORRECTLY under that failure. It left
   the state blank rather than printing "0 to chase" — unknown is not zero —
   which is exactly the rule it was written to follow. */
(function () {
  var held;
  function patch(v) {
    if (v && typeof v === 'object' && !v.__mrbPatched) {
      v.__mrbPatched = true;
      v.loadClassMatrices = function (ids) {
        var out = {};
        (ids || []).forEach(function (id) {
          out[id] = (window.__MRB_PACKS__ || {})[id] || null;
        });
        return Promise.resolve(out);
      };
      /* `loadTeacherClasses` reads class_teachers with a NESTED join
         (`class:class_id ( … )`) that the tiny query stub does not model, so
         unstubbed it returns zero classes and the editor correctly shows
         "No classes yet" — a true page behaviour, but not the one under test.
         Stubbed at the same data-layer boundary as the matrices, for the
         same reason: reproducing PostgREST's join semantics in the stub
         would be testing the stub. */
      v.loadTeacherClasses = function () {
        return Promise.resolve((window.__MRB_CLASSES__ || []).slice());
      };
      /* ⊕ MRB-326 post-review, 6 Sep 2026 — A QUESTION-PACK READ THAT
         FAILS, on demand. The page's reteach panel is the one place a
         `catch` decides what the SUMMARY SENTENCE says, and no fixture
         could reach that catch: the tiny query stub answers every read,
         so `loadPaperQuestions` always resolved. Overridden at the same
         data-layer boundary as the two above, for the same reason. */
      if (window.__MRB_QFAIL__) {
        v.loadPaperQuestions = function () {
          return Promise.reject(new Error('drive: question packs unavailable'));
        };
      }
      /* ⊕ MRB-326 post-review — THE REMINDER WRITE, ANSWERED AS POSTGREST
         WOULD ANSWER IT. `sendReminders` is an UPSERT and the query stub
         models reads only, so pressing the control threw and the footer
         silently reverted — which is why "Reminded N students" had never
         been measured at all. This echoes back the rows a FRESH upsert
         returns (one per student per assignment, none suppressed by the
         per-day rate limit) and records every call, so the drive can
         compare rows WRITTEN against children TOLD. It adjudicates
         nothing: whether RLS accepts the write is proved elsewhere, under
         a real JWT, by teacher_admin_real_drive.py. */
      if (window.__MRB_SENDREC__) {
        v.sendReminders = function (o) {
          o = o || {};
          var rows = (o.studentIds || []).map(function (id) {
            return {student_id: id, assignment_id: o.assignmentId,
                    class_id: o.classId, sent_by: o.teacherId,
                    sent_on: '2026-09-07'};
          });
          window.__MRB_SENDREC__.push({classId: o.classId,
                                       assignmentId: o.assignmentId,
                                       studentIds: (o.studentIds || []).slice()});
          return Promise.resolve(rows);
        };
      }
    }
    return v;
  }
  Object.defineProperty(window, 'MrBadmusTeacherData', {
    configurable: true,
    get: function () { return held; },
    set: function (v) { held = patch(v); }
  });
})();
'''



def packs_for(with_data=True):
    """Class packs. `c1` has work with two of three in; `c2` has work all in;
       `c3` has no work set at all — three different sentences on one screen."""
    if not with_data:
        return {}
    return {
        "cccccccc-0000-4000-8000-000000000001": {
            "members": [{"student_id": "s1", "first_name": "A", "last_name": "One"},
                        {"student_id": "s2", "first_name": "B", "last_name": "Two"},
                        {"student_id": "s3", "first_name": "C", "last_name": "Three"}],
            "assignments": [{"id": "a1", "title": "Particles", "due_at": "2026-09-04T16:00:00+00:00",
                             "academic_week": 1}],
            "submissions": [{"id": "x1", "assignment_id": "a1", "student_id": "s1",
                             "status": "complete", "completed_at": "2026-09-02T10:00:00+00:00",
                             "submitted_at": "2026-09-02T10:00:00+00:00", "score": 6, "max_score": 8},
                            {"id": "x2", "assignment_id": "a1", "student_id": "s2",
                             "status": "in_progress", "completed_at": None,
                             "submitted_at": None, "score": None, "max_score": None}],
        },
        "cccccccc-0000-4000-8000-000000000002": {
            "members": [{"student_id": "s4", "first_name": "D", "last_name": "Four"}],
            "assignments": [{"id": "a2", "title": "Forces", "due_at": "2026-09-04T16:00:00+00:00",
                             "academic_week": 1}],
            "submissions": [{"id": "x3", "assignment_id": "a2", "student_id": "s4",
                             "status": "complete", "completed_at": "2026-09-03T09:00:00+00:00",
                             "submitted_at": "2026-09-03T09:00:00+00:00", "score": 8, "max_score": 8}],
        },
        "cccccccc-0000-4000-8000-000000000003": {"members": [{"student_id": "s5", "first_name": "E", "last_name": "Five"}],
               "assignments": [], "submissions": []},
    }


# ── ⊕ coordinator correction 1 · A CLASS THIS TEACHER TEACHES AND IS NOT
#    TEACHING TODAY ────────────────────────────────────────────────────────
#
# Design's `chaseAll` and `reteachRows` both iterate `liveClasses` — every
# class the teacher holds — and her footer says "+51 MORE ACROSS YOUR
# CLASSES". The panels shipped scoped to the day, which no fixture could
# catch while every class in the fixture was ON the day.
#
# `9r/Ch2` is taught on THURSDAY only. It never appears in the Monday lesson
# list, and every one of its students who owes work must still appear in the
# expanded chase list, under its own heading, after the day's classes.
OFF_DAY_CLASS = "cccccccc-0000-4000-8000-000000000004"

CLASSES_WIDE = TABLES["classes"] + [klass(OFF_DAY_CLASS, "9r/Ch2", "KS3", 9)]

ENTRIES_WIDE = ENTRIES + [
    entry("eeeeeeee-0000-4000-8000-000000000008", OFF_DAY_CLASS, 4, 3, "9r/Ch2", "KS3", 9),
]


def packs_wide():
    """⊕ MRB-326 JOB 3 — a day with MORE chase-able students than the panel
       shows, which is the only state in which ruling 5's expander exists.

       `packs_for()` cannot ask the question: three students owe work there
       and Design's panel shows six. Here `c1` has ten owing and `c2` four, so
       the panel shows six of fourteen and the footer has something to open —
       and the expanded list has TWO class groups to draw, which is what the
       grouping check needs.

       ⚠️ NO REAL NAMES. Initials-and-ordinals, exactly as `packs_for()` does,
       because real staff and children are live."""
    def member(i, cls):
        return {"student_id": "w%s%d" % (cls, i),
                "first_name": chr(70 + (i % 20)), "last_name": "Ten" + str(i)}

    def sub(i, cls, aid):
        return {"id": "y%s%d" % (cls, i), "assignment_id": aid,
                "student_id": "w%s%d" % (cls, i), "status": "complete",
                "completed_at": "2026-09-02T10:00:00+00:00",
                "submitted_at": "2026-09-02T10:00:00+00:00",
                "score": 4, "max_score": 8}

    return {
        # twelve on roll, two of them in: ten to chase
        "cccccccc-0000-4000-8000-000000000001": {
            "members": [member(i, "a") for i in range(12)],
            "assignments": [{"id": "a1", "title": "Particles",
                             "due_at": "2026-09-04T16:00:00+00:00", "academic_week": 1}],
            "submissions": [sub(0, "a", "a1"), sub(1, "a", "a1")],
        },
        # five on roll, one in: four to chase
        "cccccccc-0000-4000-8000-000000000002": {
            "members": [member(i, "b") for i in range(5)],
            "assignments": [{"id": "a2", "title": "Forces",
                             "due_at": "2026-09-04T16:00:00+00:00", "academic_week": 1}],
            "submissions": [sub(0, "b", "a2")],
        },
        # and one with nothing set, so the day still carries all three states
        "cccccccc-0000-4000-8000-000000000003": {
            "members": [member(0, "c")], "assignments": [], "submissions": [],
        },
        # ⊕ THE OFF-TIMETABLE CLASS. Three on roll, none in: three students the
        # day-scoped panel could not see at all.
        OFF_DAY_CLASS: {
            "members": [member(i, "d") for i in range(3)],
            "assignments": [{"id": "a4", "title": "Acids",
                             "due_at": "2026-09-04T16:00:00+00:00", "academic_week": 1}],
            "submissions": [],
        },
    }


# ── ⊕ MRB-326 post-review · ONE CHILD, TWO CLASSES ──────────────────────
#
# ⚑ THE SHAPE NO OTHER FIXTURE HAS. `packs_for` and `packs_wide` both give
# every class its own children, so `chaseRows`'s dedup (`chaseSeen`) has never
# actually deduped anything and the arithmetic downstream of it was never
# tested. A science teacher taking the same child for two subjects, or a set
# and an intervention group, is ordinary — and that child owes work in BOTH
# classes.
#
# The panel lists them ONCE. The reminder, correctly, goes out per PAPER, so
# they are TWO written rows. "Reminded 3 students" over a panel showing two
# children is the defect this fixture exists to hold shut.
#
# ⚠️ NO REAL NAMES — initials and ordinals, as every fixture in this file
# does, because real staff and children are live.
TWICE_A = "tw-shared-child"
TWICE_B = "tw-second-child"


def packs_twice():
    def paper(pid, title):
        return {"id": pid, "title": title,
                "due_at": "2026-09-04T16:00:00+00:00", "academic_week": 1}
    return {
        # 8r/Sc1 — the shared child and one other, neither of them in.
        "cccccccc-0000-4000-8000-000000000001": {
            "members": [{"student_id": TWICE_A, "first_name": "F", "last_name": "One"},
                        {"student_id": TWICE_B, "first_name": "G", "last_name": "Two"}],
            "assignments": [paper("a1", "Particles")],
            "submissions": [],
        },
        # 10h/Ph1 — the SAME child again, owing a DIFFERENT paper.
        "cccccccc-0000-4000-8000-000000000002": {
            "members": [{"student_id": TWICE_A, "first_name": "F", "last_name": "One"}],
            "assignments": [paper("a2", "Forces")],
            "submissions": [],
        },
        # and one with nothing set, so the day still carries three states.
        "cccccccc-0000-4000-8000-000000000003": {
            "members": [{"student_id": "tw-third-child",
                         "first_name": "H", "last_name": "Three"}],
            "assignments": [], "submissions": [],
        },
    }


# ── ⊕ MRB-323 · the name picker, on Today ────────────────────────────────
#
# ⚑ THE ONE THING NO OTHER GATE CAN SEE. `teacher_behaviour` and
# `teacher_reach` drive the GENERATED class screen's copy of this feature,
# and `teacher_picker_drive` drives its behaviour there. None of the three
# knows this page exists: Today is hand-written, it has no fixture, and its
# picker button is REVEALED by the same `loadClassMatrices` read that fills
# the state line — which is stubbed here and nowhere else.
#
# So the questions this asks are Today's own:
#
#   · is the button revealed at all, and only for classes with a roster;
#   · does the row still WORK as a link — it used to be one `<a>` wrapping
#     the whole card, and a `<button>` cannot live inside one, so the card
#     was restructured and "the card is still a link to the class" stopped
#     being true by construction;
#   · does pressing it open the picker HERE rather than navigating, and on
#     the names this page already holds;
#   · and does any of that touch the database. `S.log` records every table
#     the stubbed client is asked for, reads included, so a delta of zero
#     across the whole interaction is the read-only claim, measured.
PICKER_EVALS = {
    "rows": "document.querySelectorAll('.lesson').length",
    # ⊕ MRB-326 JOB 3 · RULING 1 — measured on the DOM, not on the joined
    # text. "LAB 2 · 29 STUDENTS · SCIENCE" is gone, and the claim is about
    # the ROW's shape rather than about words that could one day legitimately
    # appear somewhere else on the screen. A row is period, time, code,
    # status: so the column holding the code holds at most those two lines.
    "metas": "(function(){var n=0;"
             "document.querySelectorAll('.lesson').forEach(function(l){"
             "if(l.querySelector('.lesson-meta')){n++;return;}"
             "var c=l.querySelector('.lesson-code');"
             "if(c&&c.parentElement&&c.parentElement.children.length>2){n++;}"
             "});return n;})()",
    "links": "(function(){var a=document.querySelectorAll('.lesson-go[href]');"
             "return Array.prototype.map.call(a,function(x){"
             "return x.getAttribute('href').indexOf('/teacher/class-detail.html?class=')===0;"
             "}).filter(Boolean).length;})()",
    "pickers": "document.querySelectorAll('.lesson-pick:not([hidden])').length",
    "logBefore": "(window.__MRB_STUB__.log||[]).length",
    "opened": """(async () => {
      const b = document.querySelector('.lesson-pick:not([hidden])');
      if (!b) { return JSON.stringify({error: 'no picker button revealed'}); }
      b.click();
      await new Promise(r => requestAnimationFrame(r));
      const o = document.querySelector('[data-mrb-picker]');
      if (!o) { return JSON.stringify({error: 'the picker button opened nothing'}); }
      const host = o.parentElement;
      const go = o.querySelector('[data-mrb-added="pick-go"]');
      go.click();
      await new Promise(r => setTimeout(r, 1400));
      const n = o.querySelector('[data-mrb-name]');
      /* ⚠️ BY ITS OWN MARKER, NOT `innerText.split('\\n')[0]`. The overlay's
         header is LAST in the DOM and first on the screen (flex `order`, and
         `shared/teacher-picker.js` says why), so reading the first LINE of
         its text reads the big picked name instead of the class code. That
         is what the first version of this check did, and it failed on a
         perfectly correct page. */
      const cd = o.querySelector('[data-mrb-code]');
      const out = {
        host: host.tagName,
        code: cd ? (cd.textContent || '').trim() : '(no code node)',
        dialog: o.getAttribute('aria-label') || '',
        name: n ? (n.textContent || '').trim() : '',
        stillHere: location.pathname
      };
      o.querySelector('[data-mrb-added="pick-close"]').click();
      await new Promise(r => requestAnimationFrame(r));
      out.closed = !document.querySelector('[data-mrb-picker]');
      return JSON.stringify(out);
    })()""",
    "logAfter": "(window.__MRB_STUB__.log||[]).length",
    # ── ⊕ MRB-326 JOB 3 · ruling 9 — "FIND A STUDENT" ────────────────────
    #
    # The six GENERATED teacher screens carry this control, so ruling 9 puts
    # it here. It could not be borrowed — `teacher-live.js` exports nothing
    # and mounts against a host this hand-written page does not have — so it
    # is rebuilt, and the rule that governs every control on this page
    # governs it: a control that does nothing when pressed is worse than none.
    #
    # ⚑ AND IT IS LAZY, which this probe is the only thing that can prove.
    # `logBeforeSearch` is taken AFTER the page has settled, so a non-zero
    # delta across the OPEN is the read the sheet makes for itself — the pool
    # is every student on every class, which is a wider read than the rest of
    # this page makes and must therefore not be made on load.
    "logBeforeSearch": "(window.__MRB_STUB__.log||[]).length",
    "search": """(async () => {
      const btn = document.getElementById('search-open');
      const back = document.getElementById('search-back');
      if (!btn || !back) { return JSON.stringify({error: 'no search control in the bar'}); }
      const shutAtStart = back.hidden;
      btn.click();
      await new Promise(r => setTimeout(r, 900));
      const input = document.getElementById('search-input');
      const out = document.getElementById('search-results');
      const idle = (out.textContent || '').trim();
      input.value = 'One';
      input.dispatchEvent(new Event('input', {bubbles: true}));
      await new Promise(r => requestAnimationFrame(r));
      const hits = out.querySelectorAll('[data-go-student]');
      const first = hits.length ? (hits[0].textContent || '').trim() : '';
      const href = hits.length
        ? ('/teacher/student-detail.html?student=' + hits[0].getAttribute('data-go-student'))
        : '';
      input.value = 'zzzz-nobody';
      input.dispatchEvent(new Event('input', {bubbles: true}));
      await new Promise(r => requestAnimationFrame(r));
      const miss = (out.textContent || '').trim();
      document.dispatchEvent(new KeyboardEvent('keydown', {key: 'Escape', bubbles: true}));
      await new Promise(r => requestAnimationFrame(r));
      return JSON.stringify({
        shutAtStart, opened: true, idle, hitCount: hits.length,
        first, href, miss, shutAtEnd: back.hidden
      });
    })()""",
    "logAfterSearch": "(window.__MRB_STUB__.log||[]).length",
}


def run_case(b, base, name, when, tables, packs, shots, width=1280,
             page="/teacher/today.html", evals=None, pre_extra=""):
    """One state. A FRESH PAGE TARGET each time, because
    `Page.addScriptToEvaluateOnNewDocument` is per-target — reusing a page
    would carry the previous case's frozen clock into the next one."""
    pre = ("window.__MRB_STUB__=%s;\n" % json.dumps({"uid": TEACHER, "tables": tables, "log": []}))
    pre += STUB_JS + (FREEZE % when) + (PACKS % json.dumps(packs))
    # ⚠️ FROM THE CASE'S OWN `tables`, NOT FROM THE MODULE-LEVEL `TABLES`.
    # It was hardcoded, which meant a case that widened the class list — the
    # correction-1 case does exactly that — got the stubbed `loadTeacherClasses`
    # of the BASE fixture and silently proved nothing.
    pre += (CLASSES_JS % json.dumps(tables.get('classes', [])))
    # ⊕ MRB-326 post-review — BEFORE `PACK_JS`, not after. The flags below
    # are read inside its `patch()`, which fires the instant teacher-data.js
    # assigns `window.MrBadmusTeacherData`; setting them afterwards would set
    # them after the only moment anything looks at them.
    pre += pre_extra + PACK_JS

    p = b.page("about:blank", settle=0.2)
    p.send("Page.addScriptToEvaluateOnNewDocument", {"source": pre})
    p.goto(base + page, settle=3.5)
    # ⚠️ SCOPED TO THE RENDERED REGION, not `document.body`. `innerText` on
    # body pulled in this page's own <script> source, so the drive matched
    # the words "Period" and "upload" in its own comments and called that a
    # failure. Reading #main / #notice asserts what a teacher can actually
    # see, which is the only thing worth asserting.
    text = p.eval("(function(){"
                  "var m=document.getElementById('main');"
                  "var n=document.getElementById('notice');"
                  "var v=[];"
                  "if(m&&getComputedStyle(m).display!=='none'){v.push(m.innerText);}"
                  "if(n&&getComputedStyle(n).display!=='none'){v.push(n.innerText);}"
                  # ⊕ 2 Sep 2026 (MRB-306 Phase 2a) — BOTH selectors, because the bar
                  # changed shape. today.html and timetable.html took v3's top bar,
                  # whose region marker is `data-port-region="topbar"`; the old
                  # `nav.top-nav` is kept so this drive still reads admin.html and
                  # import.html's bar if it is ever pointed at them. Widening the
                  # selector keeps the nav's text inside every assertion below —
                  # dropping it would have made this read silently return nothing.
                  "var nav=document.querySelector('nav.top-nav,[data-port-region=\"topbar\"]');"
                  "if(nav){v.push(nav.innerText);}"
                  "return v.join('\\n');})()")
    shot = os.path.join(shots, name + ".png")
    p.screenshot(shot, width=width)
    overflow = p.eval("document.documentElement.scrollWidth > "
                      "document.documentElement.clientWidth + 1")
    # ⚠️ IS THE PAGE ACTUALLY VISIBLE? Every text assertion in this file
    # passed once against a page that rendered BLANK: `body { display: none }`
    # was never lifted, and `getComputedStyle` on a CHILD of a hidden parent
    # still reports its own `display: block`, so checking #main proved
    # nothing. Ask the BODY, and measure that something was actually painted.
    visible = p.eval("(function(){"
                     "var b=getComputedStyle(document.body);"
                     "if(b.display==='none'||b.visibility==='hidden'){return false;}"
                     "var m=document.getElementById('main');"
                     "var n=document.getElementById('notice');"
                     "function painted(e){if(!e)return false;"
                     "var r=e.getBoundingClientRect();return r.width>0&&r.height>0;}"
                     "return painted(m)||painted(n);})()")
    # The favicon 404 is the static server's, not the page's.
    errs = [e for e in p.console_errors() if 'favicon' not in e]
    # `evals` lets a case assert DOM STATE, not only rendered text — the
    # grid's selected options are not text and cannot be read any other way.
    probed = {}
    for k, expr in (evals or {}).items():
        probed[k] = p.eval(expr)
    return text or "", shot, overflow, errs, visible, probed


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--shots", default="/tmp/mrb306-today")
    args = ap.parse_args()
    os.makedirs(args.shots, exist_ok=True)

    fails = []
    def check(ok_, what, detail=""):
        print("   %s  %s%s" % ("PASS" if ok_ else "FAIL", what,
                               ("  - " + detail) if detail else ""))
        if not ok_:
            fails.append(what)

    server, port = cdp.serve("mrbadmus_site")
    base = "http://127.0.0.1:%d" % port

    try:
        with cdp.Browser() as b:
            # ── 1. a weekday this teacher teaches (Monday 7 Sep 2026) ────
            t, s1, ov, errs, vis, g1 = run_case(
                b, base, "1-weekday", "2026-09-07T09:00:00",
                TABLES, packs_for(), args.shots, evals=PICKER_EVALS)
            print("\n--- WEEKDAY ---\n" + t[:800] + "\n")
            # ⚠️ CASE-FOLDED, for the reason the block below states: the day
            # is named in the EYEBROW now, which `text-transform: uppercase`
            # renders as "MONDAY". Asserting the source casing would test the
            # stylesheet rather than the page. (It used to be matched in the
            # sub-line "Monday · 3 lessons", which ruling 2 replaced.)
            check("MONDAY" in t.upper(), "weekday: names the day")
            # ⚠️ CASE-FOLDED where a stylesheet uppercases, and NOT where it
            # does not. The eyebrow and the panel headings carry
            # `text-transform`; the lesson row carries none, so "P1" and
            # "8r/Sc1" are asserted exactly as the page writes them.
            T = t.upper()
            check("P1" in t and "P2" in t and "P4" in t,
                  "weekday: periods by NUMBER and in order",
                  "Design's row is P1 over its clock time, not 'PERIOD 1'")
            # ⊕ MRB-326 JOB 3 · RULING 1 — a row is period, time, code, status.
            check(not re.search(r"\bPERIOD \d\b", T),
                  "weekday: the old 'PERIOD n' eyebrow is GONE")
            check(not re.search(r"\b\d{2}:\d{2}\b", t),
                  "weekday: NO clock times invented", "school_period_times is empty")
            check("8r/Sc1" in t and "10h/Ph1" in t and "7h/Sc5" in t,
                  "weekday: all three classes drawn")
            # ⊕ RULING 1 — THE META LINE IS DELETED. It said "KS3 · Science",
            # which is the class code beside it spelled out. Asserting its
            # ABSENCE, on the DOM rather than on the joined text, because the
            # words could legitimately appear elsewhere one day and the claim
            # is about the ROW.
            check(g1["metas"] == 0,
                  "weekday: no lesson row carries a meta line",
                  "ruling 1 — %d row(s) still do" % g1["metas"])
            check("KS3" not in T and "KS4" not in T,
                  "weekday: the key stage is not spelled out beside the code",
                  "MRB-263 makes the code itself say it")
            check("1 of 3 in" in t, "weekday: chase count from the union predicate")
            # ⊕ RULING 7 — Design's chase form, with the names on it.
            # `shortName` is Design's: first name, then the surname's initial.
            # This fixture's students are "B Two" and "C Three", so they read
            # "B T" and "C T" — a real "Hana Popescu" reads "Hana P".
            check("chase B T, C T" in t,
                  "weekday: the chase line NAMES who to chase",
                  "Design's '11 of 29 in — chase Hana P, Idris B +16 more'")
            check("1/1 in" in t,
                  "weekday: a class that is all in reads as the numeric form",
                  "ruling 7 — 'All N homeworks in — nothing to chase' is gone")
            check("nothing to chase" not in t.lower(),
                  "weekday: 'nothing to chase' is GONE",
                  "the absence of a chase clause does not need saying")
            check("still to hand in" not in t,
                  "weekday: the row does not say the same subtraction twice",
                  "'1 of 3 in · 2 still to hand in' — 3 minus 1 IS 2")
            check("No work set this week." in t,
                  "weekday: a class with no work says so", "and offers no action")
            check("Higher" not in t and "Foundation" not in t,
                  "weekday: no tier / pathway anywhere")
            # ⊕ RULING 3 — the day-chip strip is gone. Design does not draw it.
            check(not re.search(r"\bTUE\b|\bTHU\b", T),
                  "weekday: the MON/TUE/WED day-chip strip is GONE", "ruling 3")
            # ⊕ RULING 6 — "N lessons" is said in the summary sentence and
            # NOT AGAIN beside the h2 as Design's `lessonCount`.
            check(T.count("3 LESSONS") == 1,
                  "weekday: the lesson count is said ONCE",
                  "ruling 6 — Design draws it twice; got %d" % T.count("3 LESSONS"))
            check("3 lessons today" in t,
                  "weekday: and the once is the summary sentence")
            # ⊕ RULING 8 — the eyebrow, from data. Monday 7 September 2026,
            # autumn term, and the academic year's own name.
            check("MONDAY 7 SEPTEMBER" in T,
                  "weekday: the eyebrow names the day and date from the clock")
            check("AUTUMN TERM" in T,
                  "weekday: the term is derived from the month", "ruling 8: Sep-Dec")
            check("2026-27" in t,
                  "weekday: the academic year comes from loadAcademicYears")
            # ⊕ RULING 4 — "Set work" is DEAD platform-wide and is not drawn.
            check("Set work" not in t, "weekday: no dead 'Set work' button", "ruling 4")
            check("Weekly digest" in t and "Upload timetable" in t,
                  "weekday: the two live actions are drawn", "ruling 4")
            check("Edit timetable" in t, "weekday: Design's Edit timetable link is drawn")
            # ⊕ RULING 9 — the nav carries what the generated screens carry.
            check("Today" in t and "My classes" in t, "nav: both tabs")
            check("FIND A STUDENT" in T, "nav: Find a student, as on the six generated screens")
            check("Ms Nwosu" in t, "nav: the teacher is named, as Design draws it")
            check("Sign out" in t, "nav: Sign out")
            check(vis, "weekday: the page is actually PAINTED", "not a blank screen")
            check(not errs, "weekday: no console errors", "; ".join(errs[:2]))

            check("Send reminders" in t,
                  "chase: the reminder control is present and REAL",
                  "TD.sendReminders — the same write the class screen makes")

            # ── ⊕ MRB-323 · the name picker on Today ─────────────────────
            check(g1["rows"] == 3 and g1["links"] == 3,
                  "picker: every lesson row is STILL a link to its class",
                  "%d row(s), %d working link(s) — the card stopped being one "
                  "<a> so that a second control could live on it"
                  % (g1["rows"], g1["links"]))
            check(g1["pickers"] == 3,
                  "picker: offered on every class whose roster came back",
                  "3 classes, all with members; got %d button(s)" % g1["pickers"])
            op = json.loads(g1["opened"])
            check(not op.get("error"), "picker: the button opens the picker",
                  op.get("error", ""))
            if not op.get("error"):
                check(op["host"] == "BODY",
                      "picker: mounts on THIS page",
                      "no #mrb-teacher runtime host here, so body; got " + op["host"])
                check(op["stillHere"] == "/teacher/today.html",
                      "picker: does NOT navigate away",
                      "the whole point is that it is at hand between lessons; "
                      "landed on " + op["stillHere"])
                check(op["code"] == "8r/Sc1",
                      "picker: names the class as the class is named",
                      "MRB-263 case, not upper-cased; got " + repr(op["code"]))
                check(op["dialog"] == "Pick a student · 8r/Sc1",
                      "picker: the dialog announces which class it is for",
                      "its accessible name, so the class is heard on open "
                      "rather than read last; got " + repr(op["dialog"]))
                check(op["name"] in ("A One", "B Two", "C Three"),
                      "picker: picks from THIS class's own roster",
                      "3 members stubbed; got " + repr(op["name"]))
                check(op["closed"], "picker: closes cleanly")
            # ── ⊕ MRB-326 JOB 3 · ruling 9 — the student search ──────────
            se = json.loads(g1["search"])
            check(not se.get("error"), "search: the bar carries a working control",
                  se.get("error", ""))
            if not se.get("error"):
                check(se["shutAtStart"], "search: the sheet ships CLOSED")
                # ⊕ COORDINATOR CORRECTION 1 — THIS CHECK IS INVERTED, and
                # the inversion is the correction. The search used to load its
                # own pool on first press, because it was the only thing that
                # wanted every class. The chase panel now wants the same
                # population, so the page builds it once and the sheet reads
                # it — which makes the sharper claim: opening the search costs
                # NOT ONE query, because there is one pool and one source.
                check(g1["logAfterSearch"] == g1["logBeforeSearch"],
                      "search: adds NOT ONE read of its own",
                      "it reads the pool the chase panel already built; "
                      "%s read(s) before the press, %s after"
                      % (g1["logBeforeSearch"], g1["logAfterSearch"]))
                check("5 students on your classes" in se["idle"],
                      "search: the pool is every student on EVERY class",
                      "3 classes hold 5 students between them; got " + repr(se["idle"]))
                check(se["hitCount"] == 1 and "A One" in se["first"],
                      "search: typing filters it", "got %d hit(s): %r"
                      % (se["hitCount"], se["first"]))
                check("8r/Sc1" in se["first"],
                      "search: and a hit names the class the child is in",
                      repr(se["first"]))
                check(se["href"].startswith("/teacher/student-detail.html?student="),
                      "search: a hit goes to that child's page",
                      "not a dead row; " + repr(se["href"]))
                # ⚠️ UNKNOWN IS NOT EMPTY, and NO MATCH IS NOT AN ERROR. Both
                # states get their own sentence, and neither is a blank box.
                check("Nobody on your classes matches" in se["miss"],
                      "search: a miss says so", repr(se["miss"]))
                check(se["shutAtEnd"], "search: Escape closes it")

            check(g1["logAfter"] == g1["logBefore"],
                  "picker: touches the database NOT ONCE",
                  "%d table read(s) before, %d after — it is read-only and "
                  "absences are not written down"
                  % (g1["logBefore"], g1["logAfter"]))

            # ── 2. Saturday ──────────────────────────────────────────────
            t2, s2, _, e2, vis2, _ = run_case(b, base, "2-weekend", "2026-09-12T09:00:00",
                                     TABLES, packs_for(), args.shots)
            print("--- WEEKEND ---\n" + t2[:500] + "\n")
            # ⊕ MRB-326 JOB 3 · RULING 2 — THESE TWO CHECKS ARE INVERTED, and
            # the inversion is the ruling rather than a weakening. They used
            # to assert "No lessons at the weekend. Showing your next teaching
            # day." and "NEXT: MONDAY"; both are deleted. The property under
            # test is unchanged — a Saturday must not pass Monday's lessons off
            # as today's — and it is now carried by ONE WORD in the h2 instead
            # of by two sentences of the page explaining its own arithmetic.
            check("No lessons at the weekend" not in t2,
                  "weekend: the explainer sentence is GONE", "ruling 2")
            check("Showing your next teaching day" not in t2,
                  "weekend: and so is the second half of it", "ruling 2")
            check("NEXT:" not in t2.upper(),
                  "weekend: the 'NEXT: MONDAY' label is GONE", "ruling 2")
            check("Monday\u2019s lessons" in t2 or "Monday's lessons" in t2,
                  "weekend: the h2 NAMES THE DAY instead", "ruling 2 — one word")
            check("TODAY\u2019S LESSONS" not in t2.upper() and "TODAY'S LESSONS" not in t2.upper(),
                  "weekend: does NOT present it as today")
            # The eyebrow still tells the truth about what day it actually is:
            # the h2 says whose lessons these are, the date line says the date.
            # Two facts, each said once.
            check("SATURDAY 12 SEPTEMBER" in t2.upper(),
                  "weekend: the eyebrow is still TODAY's date", "ruling 8")
            check(vis2, "weekend: the page is actually PAINTED")
            check(not e2, "weekend: no console errors", "; ".join(e2[:2]))

            # ── 3. a weekday with no lessons (Friday) ────────────────────
            t3, s3, _, e3, vis3, _ = run_case(b, base, "3-empty-day", "2026-09-11T09:00:00",
                                     TABLES, packs_for(), args.shots)
            print("--- EMPTY WEEKDAY ---\n" + t3[:400] + "\n")
            # ⊕ RULING 2 again — a weekday with no lessons falls forward the
            # same silent way a weekend does.
            check("No lessons today" not in t3,
                  "empty weekday: the explainer sentence is GONE", "ruling 2")
            check("NEXT:" not in t3.upper(),
                  "empty weekday: the 'NEXT:' label is GONE", "ruling 2")
            check("Monday\u2019s lessons" in t3 or "Monday's lessons" in t3,
                  "empty weekday: falls forward, and the h2 names the day")
            check("FRIDAY 11 SEPTEMBER" in t3.upper(),
                  "empty weekday: the eyebrow is still TODAY's date")
            check(vis3, "empty weekday: the page is actually PAINTED")

            # ── 4. no timetable at all ───────────────────────────────────
            empty = dict(TABLES); empty["timetable_entries"] = []
            t4, s4, _, e4, vis4, _ = run_case(b, base, "4-no-timetable", "2026-09-07T09:00:00",
                                     empty, {}, args.shots)
            print("--- NO TIMETABLE ---\n" + t4[:400] + "\n")
            check("No timetable yet" in t4, "no timetable: says so")
            # ⊕ RULING 6 — and says it ONCE. The prompt paragraph used to end
            # "…and there isn't one on your account yet", directly under the
            # line that had just said it.
            check("isn\u2019t one on your account" not in t4
                  and "isn't one on your account" not in t4,
                  "no timetable: and does not say it twice", "ruling 6")
            check("Period" not in t4, "no timetable: invents no lessons")
            check("upload" not in t4.lower(),
                  "no timetable: promises no upload", "that screen is not built")
            check(vis4, "no timetable: the page is actually PAINTED")

            # ── 5. 390px ─────────────────────────────────────────────────
            t5, s5, ov5, e5, vis5, _ = run_case(b, base, "5-390px", "2026-09-07T09:00:00",
                                       TABLES, packs_for(), args.shots, width=390)
            check(not ov5, "390px: no horizontal overflow")
            check("8r/Sc1" in t5, "390px: still renders the lessons")
            check(vis5, "390px: the page is actually PAINTED")

            # ── 6. the timetable EDITOR ──────────────────────────────────
            t6, s6, ov6, e6, vis6, g6 = run_case(
                b, base, "6-editor", "2026-09-07T09:00:00", TABLES,
                packs_for(), args.shots, page="/teacher/timetable.html",
                evals={
                    "cells":  "document.querySelectorAll('#grid select').length",
                    "filled": "(function(){var s=document.querySelectorAll('#grid select'),n=0;"
                              "for(var i=0;i<s.length;i++){if(s[i].value)n++;}return n;})()",
                    "options":"(function(){var s=document.querySelector('#grid select');"
                              "return s?s.options.length:0;})()",
                })
            print("--- EDITOR ---\n" + t6[:500] + "\n")
            check(vis6, "editor: the page is actually PAINTED")
            check(not e6, "editor: no console errors", "; ".join(e6[:2]))
            check("PHOTO" not in t6.upper(),
                  "editor: no photo-upload promise",
                  "Design's v3 offers one; no photo path is built, so it is not claimed")
            check("MON" in t6.upper() and "FRI" in t6.upper(),
                  "editor: the Mon-Fri grid is drawn")
            check("PERIOD 1" in t6.upper() and "PERIOD 5" in t6.upper(),
                  "editor: five periods, by NUMBER")
            check(g6["cells"] == 25, "editor: a full Mon-Fri x P1-P5 grid",
                  "25 cells, got %s" % g6["cells"])
            # The fixture's teacher has 5 timetable entries; the grid must open
            # on the timetable they ALREADY have, not empty.
            check(g6["filled"] == 5, "editor: pre-filled from the saved timetable",
                  "expected 5 selected, got %s" % g6["filled"])
            # 3 classes + the empty option. A picker offering a class the
            # teacher does not teach is the failure this asserts against.
            check(g6["options"] == 4, "editor: offers ONLY this teacher's classes",
                  "expected 3 classes + blank, got %s" % g6["options"])

            # ── 7. the CSV importer, exercised through the page's own
            #       functions. It is pure logic over text, so driving it
            #       directly asserts far more than clicking a file input:
            #       both header shapes, a quoted field, loose code matching,
            #       and every way a row can be REFUSED rather than guessed.
            csv_probe = {
                # simple shape, no header
                "simple": "JSON.stringify((function(){var r=parseCsv('Mon,1,8r/Sc1\\nWed,4,10h/Ph1');"
                          "var c=columnsOf(r);return [r.length,c.skipHeader,readDay(r[0][0]),readPeriod(r[0][1]),"
                          "!!matchClass(r[0][2])];})())",
                # MIS shape, with a header and different column order words
                "mis":    "JSON.stringify((function(){var r=parseCsv('Day,Period,Class\\nTuesday,P3,\"8R / SC1\"');"
                          "var c=columnsOf(r);return [c.skipHeader,c.day,c.period,c.cls,"
                          "readDay(r[1][c.day]),readPeriod(r[1][c.period]),"
                          "(matchClass(r[1][c.cls])||{}).name||null];})())",
                # every refusal path
                "bad":    "JSON.stringify([readDay('Sunday'),readDay('nonsense'),readPeriod('none'),"
                          "readPeriod('99'),matchClass('9z/Xx9'),matchClass('')])",
            }
            _t7, _s7, _o7, _e7, _v7, c7 = run_case(
                b, base, "7-csv", "2026-09-07T09:00:00", TABLES, packs_for(),
                args.shots, page="/teacher/timetable.html", evals=csv_probe)

            simple = json.loads(c7["simple"])
            check(simple == [2, False, 1, 1, True],
                  "csv: bare day,period,class shape", str(simple))

            mis = json.loads(c7["mis"])
            check(mis == [True, 0, 1, 2, 2, 3, "8r/Sc1"],
                  "csv: MIS export shape, quoted field, loose code match",
                  "'8R / SC1' must resolve to 8r/Sc1; got %s" % (mis,))

            bad = json.loads(c7["bad"])
            check(bad == [None, None, None, None, None, None],
                  "csv: every unreadable row is REFUSED, never guessed",
                  "Sunday, nonsense, bad periods and unknown codes all null; got %s" % (bad,))

            # ── 8. ⊕ MRB-326 · a colleague's lesson, and a slot written
            #       twice. The served table holds both — this is the shape a
            #       school_admin's school-wide RLS read really returns — and
            #       the page must render the teacher's OWN day, each period
            #       once. See ENTRIES_MIXED above for why each row is there.
            mixed = dict(TABLES); mixed["timetable_entries"] = ENTRIES_MIXED
            pairs_probe = {
                "pairs": "JSON.stringify(Array.prototype.map.call("
                         "document.querySelectorAll('.lesson'), function (l) {"
                         "var p = l.querySelector('.lesson-p');"
                         "var c = l.querySelector('.lesson-code');"
                         "return [(p ? p.textContent : '').trim(),"
                         "        (c ? c.textContent : '').trim()]; }))",
            }
            t8, s8, _o8, e8, vis8, g8 = run_case(
                b, base, "8-own-day-once", "2026-09-07T09:00:00",
                mixed, packs_for(), args.shots, evals=pairs_probe)
            print("--- OWN DAY, ONCE ---\n" + t8[:600] + "\n")
            pairs = json.loads(g8["pairs"])
            # ⚠️ CASE-FOLDED on the period label for the same reason case 1 is:
            # `innerText` applies `text-transform`, and the class CODE must NOT
            # be folded (MRB-263 names classes in mixed case, and asserting the
            # folded form would let 8R/SC1 pass for 8r/Sc1).
            got = [[p.upper(), c] for p, c in pairs]
            want = [[p, c] for p, c in MIXED_EXPECTED]
            check(len(pairs) == 3,
                  "own day: one row per slot the teacher OWNS on the day shown",
                  "Monday holds P1, P2 and P4 for this teacher; got %d row(s): %s"
                  % (len(pairs), pairs))
            check(all(p != "PERIOD 3" for p, _ in got),
                  "own day: a colleague's lesson of a shared class is NOT drawn",
                  "P3 is free for this teacher and a co-teacher's 8r/Sc1 row sits "
                  "in the served table; got %s" % (pairs,))
            check(got == want,
                  "own day: the twice-written slot collapses to the NEWER row",
                  "Monday P2 has a seeded 10h/Ph1 and a later manual 7h/Sc5; "
                  "expected %s, got %s" % (want, got))
            check("10h/Ph1" not in t8,
                  "own day: the superseded class is not shown at all",
                  "the seeded row it came from lost to a newer manual edit")
            check(vis8, "own day: the page is actually PAINTED")
            check(not e8, "own day: no console errors", "; ".join(e8[:2]))

            # ── 9. ⊕ MRB-326 JOB 3 · ruling 5 — THE CHASE FOOTER OPENS ───
            #
            # "+51 MORE ACROSS YOUR CLASSES" was a dead count: the page told a
            # teacher that fifty-one other children owed them work and then
            # gave them no way to see who. It is now the door to the full list.
            #
            # ⚠️ ITS OWN FIXTURE, because case 1's cannot ask the question:
            # three students owe work there and the panel shows six, so there
            # is no overflow and no footer to press. `packs_wide()` puts a
            # roster on two classes big enough that some of it is BELOW the
            # fold, which is the only state in which the control exists.
            wide = packs_wide()
            chase_probe = {
                "logBefore": "(window.__MRB_STUB__.log||[]).length",
                "chase": """(async () => {
                  const box = document.getElementById('chase');
                  if (!box) { return JSON.stringify({error: 'no chase panel'}); }
                  const rows = () => box.querySelectorAll('[data-chase-student]').length;
                  const before = rows();
                  const more = document.getElementById('chase-more');
                  if (!more) { return JSON.stringify({error: 'no expander — ' + before + ' row(s) shown'}); }
                  const label = (more.textContent || '').trim();
                  more.click();
                  await new Promise(r => requestAnimationFrame(r));
                  const after = rows();
                  const groups = Array.prototype.map.call(
                    box.querySelectorAll('.chase-group'),
                    g => (g.textContent || '').trim());
                  /* ⊕ CORRECTION 1 — is the OFF-TIMETABLE class's student in
                     the list, under that class's own heading? */
                  const offRows = (() => {
                    const hs = box.querySelectorAll('.chase-group');
                    for (const h of hs) {
                      if ((h.textContent || '').trim() !== '9r/Ch2') { continue; }
                      let n = 0;
                      for (let e = h.nextElementSibling;
                           e && !e.classList.contains('chase-group');
                           e = e.nextElementSibling) {
                        if (e.hasAttribute('data-chase-student')) { n++; }
                      }
                      return n;
                    }
                    return -1;
                  })();
                  /* ⊕ THE REDUNDANCY RULE, MEASURED. Once a group is headed
                     "8r/Sc1" the rows inside it drop their own class code —
                     the heading two lines up has just said it. */
                  const codesInGroups = box.querySelectorAll('.chase-group ~ [data-chase-student] .panel-code').length;
                  const back = document.getElementById('chase-more');
                  const backLabel = (back ? back.textContent : '').trim();
                  if (back) { back.click(); }
                  await new Promise(r => requestAnimationFrame(r));
                  return JSON.stringify({
                    before, after, groups, offRows, codesInGroups, label, backLabel,
                    collapsed: rows(),
                    /* ⊕ MRB-326 post-review — THE BADGE IS GONE, so the
                       pool size is read off the OPENED LIST rather than off
                       `#chase-count`. The count was printed in the panel
                       header and in the summary sentence, and the summary is
                       the one place (see the markup comment on the head).
                       `badge` is kept as an assertion so the removal cannot
                       silently come back. */
                    badge: !!document.getElementById('chase-count'),
                    remind: !!document.getElementById('remind-all')
                  });
                })()""",
                "logAfter": "(window.__MRB_STUB__.log||[]).length",
            }
            # ⊕ CORRECTION 1 — the wide fixture carries a FOURTH class taught
            # on Thursday. It is never in Monday's lesson list, and its three
            # students must still be chase-able.
            wide_tables = dict(TABLES)
            wide_tables["timetable_entries"] = ENTRIES_WIDE
            wide_tables["classes"] = CLASSES_WIDE
            wide_tables["class_teachers"] = CLASS_TEACHERS + [
                {"class_id": OFF_DAY_CLASS, "teacher_id": TEACHER,
                 "deleted_at": None, "ended_at": None}]
            t9, s9, _o9, e9, vis9, g9 = run_case(
                b, base, "9-chase-open", "2026-09-07T09:00:00",
                wide_tables, wide, args.shots, evals=chase_probe)
            print("--- CHASE, OPENED ---\n" + t9[:500] + "\n")
            ex = json.loads(g9["chase"])
            check(not ex.get("error"), "chase: the footer is a CONTROL, not a caption",
                  ex.get("error", ""))
            if not ex.get("error"):
                check(ex["before"] == 6,
                      "chase: Design shows six", "got %d" % ex["before"])
                # ⊕ CORRECTION 1 — Design's exact words. It said "across
                # today's classes" while the pool WAS the day; the pool is now
                # every class, so the caption is hers again.
                check("more across your classes" in ex["label"],
                      "chase: and the control says how many more, in Design's words",
                      repr(ex["label"]))
                check(ex["after"] > ex["before"],
                      "chase: pressing it opens the FULL list, in place",
                      "%d shown, %d after opening" % (ex["before"], ex["after"]))
                check(ex["after"] == 17,
                      "chase: the pool is EVERY class, not the day's",
                      "10 + 4 today, plus 3 on a class taught on Thursday; "
                      "got %d" % ex["after"])
                check(not ex["badge"],
                      "chase: the header count badge is GONE",
                      "the summary sentence already says '17 students to "
                      "chase'; Design's `chaseCount` beside the heading is "
                      "the same number one inch away")
                check("17 students to chase" in t9,
                      "chase: and the count is said in the summary sentence",
                      "the one place it is said")
                check(len(ex["groups"]) == 3,
                      "chase: the full list is GROUPED BY CLASS",
                      "three classes owe work; got %s" % (ex["groups"],))
                # Today's classes first, in the order they are taught; then
                # the rest by code. The teacher's next hour is the part of
                # this list they can still do something about.
                check(ex["groups"] == ["8r/Sc1", "10h/Ph1", "9r/Ch2"],
                      "chase: today's classes first, then the rest by code",
                      "got %s" % (ex["groups"],))
                check(ex["offRows"] == 3,
                      "chase: a class NOT on today's timetable is in the list",
                      "9r/Ch2 is taught on Thursday and three of its students "
                      "owe work; got %s row(s) under its heading" % ex["offRows"])
                check(ex["codesInGroups"] == 0,
                      "chase: and a grouped row does not repeat its class code",
                      "the heading above it has just said it; %d row(s) do"
                      % ex["codesInGroups"])
                check(ex["backLabel"] == "Show fewer",
                      "chase: there is a way back", repr(ex["backLabel"]))
                check(ex["collapsed"] == ex["before"],
                      "chase: and it collapses again",
                      "back to %d, was %d" % (ex["collapsed"], ex["before"]))
                check(ex["remind"], "chase: Send reminders survives the toggle")
            check(g9["logAfter"] == g9["logBefore"],
                  "chase: opening the full list reads NOTHING new",
                  "the whole list was already in hand before the press; "
                  "%s read(s) before, %s after" % (g9["logBefore"], g9["logAfter"]))
            check(not e9, "chase: no console errors", "; ".join(e9[:2]))

            # ── 10. ⊕ MRB-326 JOB 3 · ruling 6 — THE HELD SCHOOL ─────────
            #
            # `schools.assignments_open_from` in the future. MRB-325 ruled the
            # sentence "once per surface" and this page has FOUR surfaces, so
            # the drive's own fixture rendered it five times: on three lesson
            # rows, in both panels, and in the summary. Ruling 6 hardens that
            # to once, full stop.
            held = dict(TABLES)
            held["schools"] = [{"assignments_open_from": "2026-10-01"}]
            hold_probe = {
                "states": "(function(){var n=0;"
                          "document.querySelectorAll('.lesson-state').forEach(function(c){"
                          "if((c.textContent||'').trim())n++;});return n;})()",
                "chaseRows": "document.querySelectorAll('#chase [data-chase-student]').length",
                # ⊕ MRB-326 post-review — INVERTED, not deleted. This read
                # `#chase-count` and demanded "0". The badge is removed
                # (the count is the summary sentence's, and only its), so
                # the assertion becomes: the element does not exist, and
                # the zero is still said exactly once, in the summary.
                "chaseBadge": "!!document.getElementById('chase-count')",
                "chaseEmptyText": "(document.getElementById('chase').textContent||'').trim()",
                "remind": "!!document.getElementById('remind-all')",
                "reteach": "(document.getElementById('reteach-host').innerHTML||'').trim().length",
                # ⚠️ THE WHOLE DOCUMENT, not the rendered text — a sentence
                # hidden in a `title`, an `aria-label` or a skeleton would
                # still be a second copy of it waiting to surface.
                "saidTimes": "(document.getElementById('main').innerHTML"
                             ".split('No assignment set yet').length - 1)",
            }
            t10, s10, _o10, e10, vis10, g10 = run_case(
                b, base, "10-held", "2026-09-07T09:00:00",
                held, packs_for(), args.shots, evals=hold_probe)
            print("--- HELD SCHOOL ---\n" + t10[:500] + "\n")
            check(g10["saidTimes"] == 1,
                  "held: 'No assignment set yet' appears EXACTLY ONCE",
                  "ruling 6 — it was said 5 times; got %s" % g10["saidTimes"])
            check("No assignment set yet" in t10,
                  "held: and the once is where a teacher reads it")
            # And the once is in the SUMMARY SENTENCE, beside the lesson
            # count — not stranded in a panel where a teacher scanning the
            # top of the page would never meet it.
            check("3 lessons today" in t10 and
                  t10.index("No assignment set yet") - t10.index("3 lessons today") < 40,
                  "held: and it is said in the summary sentence",
                  "beside the lesson count, where the page's one-line answer is")
            check(g10["states"] == 0,
                  "held: NO lesson row carries a status line",
                  "ruling 6 — %s row(s) still do" % g10["states"])
            check(not g10["chaseBadge"],
                  "held: the chase panel carries NO count badge",
                  "removed as a redundancy — the count is the summary "
                  "sentence's and only its")
            # ⚠️ AND ON A HELD SCHOOL THE COUNT IS NOT SAID AT ALL, which is
            # the pre-existing behaviour of the branch above (`summary([
            # stripHead, HELD_TEXT])`) and is the right one: "0 students to
            # chase" under a school that has not opened yet is arithmetic
            # about a state that does not exist. The hold sentence is the
            # answer, and it is the only one.
            check("students to chase" not in t10 and "student to chase" not in t10,
                  "held: and no chase count is said anywhere",
                  "the hold sentence is the whole answer; nothing was set, so "
                  "there is no chase arithmetic to report")
            check(g10["chaseRows"] == 0, "held: and no chase rows")
            check(g10["chaseEmptyText"] == "",
                  "held: an empty chase panel says NOTHING under its heading",
                  "'Nobody owes this week’s work.' was the same count a THIRD "
                  "time, in words; got %r" % g10["chaseEmptyText"])
            check("Nobody owes" not in t10,
                  "held: and that sentence is nowhere on the page")
            check(not g10["remind"],
                  "held: and NO 'Send reminders'",
                  "there is nobody to remind and nothing to remind them about")
            check(g10["reteach"] == 0,
                  "held: the reteach panel is not rendered at all",
                  "Design's `hasReteach` false")
            check("No work set this week" not in t10,
                  "held: the per-class sentence is not shown over the school-wide one")
            check(vis10, "held: the page is actually PAINTED")
            check(not e10, "held: no console errors", "; ".join(e10[:2]))

            # ── 11. ⊕ MRB-326 post-review · UNKNOWN IS NOT ZERO, in the
            #        summary sentence ────────────────────────────────────
            #
            # `loadPaperQuestions` throws. The page caught it, left `qpacks`
            # null, and the summary sentence still ended "· 0 topics worth a
            # reteach" — a reassurance it had just failed to earn, and the
            # exact defect the `!matrices` branch two panels up is written
            # against. The segment is now DROPPED where the read failed.
            #
            # ⚠️ AND ONLY WHERE IT FAILED. A teacher with nothing marked
            # anywhere really does have nothing worth a reteach, and zero is
            # the true answer there — every other case in this file still
            # renders the segment, which is what keeps this check honest.
            qfail_probe = {
                "summary": "(document.querySelector('.summary').textContent||'')"
                           ".replace(/\\s+/g,' ').trim()",
                "reteach": "(document.getElementById('reteach-host').innerHTML||'').trim().length",
            }
            t11, s11, _o11, e11, vis11, g11 = run_case(
                b, base, "11-reteach-unavailable", "2026-09-07T09:00:00",
                TABLES, packs_for(), args.shots, evals=qfail_probe,
                pre_extra="window.__MRB_QFAIL__=true;\n")
            print("--- RETEACH READ FAILED ---\n" + g11["summary"] + "\n")
            check("worth a reteach" not in g11["summary"],
                  "reteach-fail: the summary DROPS the reteach segment",
                  "a count this page could not make is not printed; got %r"
                  % g11["summary"])
            check("0 topics" not in g11["summary"] and "0 topic" not in g11["summary"],
                  "reteach-fail: and it never says '0 topics'",
                  "unknown is not zero; got %r" % g11["summary"])
            check("students to chase" in g11["summary"],
                  "reteach-fail: the clauses it CAN make are still said",
                  "the sentence is shorter by one clause, not gone; got %r"
                  % g11["summary"])
            check(g11["reteach"] == 0,
                  "reteach-fail: and no reteach card is drawn")
            check(vis11, "reteach-fail: the page is actually PAINTED")
            check(not e11, "reteach-fail: no console errors — a WARN, not an "
                           "error, is what a failed panel costs",
                  "; ".join(e11[:2]))

            # ── 12. ⊕ MRB-326 post-review · ONE CHILD, TWO CLASSES ───────
            #
            # The chase panel dedups by student; the reminder goes out per
            # paper. So a child owing work in two of this teacher's classes
            # is ONE row in the panel and TWO rows in the database, and the
            # footer summed rows: "Reminded 3 students" over a panel showing
            # two children. It counts distinct children now, the same way
            # `MRB_REMIND_ALL` does on the class screen — one number, one
            # source.
            twice_probe = {
                "chaseRows": "document.querySelectorAll('#chase [data-chase-student]').length",
                "summary": "(document.querySelector('.summary').textContent||'')"
                           ".replace(/\\s+/g,' ').trim()",
                "remind": """(async () => {
                  const b = document.getElementById('remind-all');
                  if (!b) { return JSON.stringify({error: 'no reminder control'}); }
                  b.click();
                  for (let i = 0; i < 40 && document.getElementById('remind-all')
                       && /Sending/.test(document.getElementById('remind-all').textContent); i++) {
                    await new Promise(r => setTimeout(r, 50));
                  }
                  await new Promise(r => setTimeout(r, 200));
                  const after = document.getElementById('remind-all');
                  const calls = window.__MRB_SENDREC__ || [];
                  return JSON.stringify({
                    label: after ? (after.textContent || '').trim() : '(gone)',
                    calls: calls.length,
                    rows: calls.reduce((a, c) => a + c.studentIds.length, 0),
                    children: Object.keys(calls.reduce((a, c) => {
                      c.studentIds.forEach(id => { a[id] = 1; }); return a; }, {})).length
                  });
                })()""",
            }
            t12, s12, _o12, e12, vis12, g12 = run_case(
                b, base, "12-child-in-two-classes", "2026-09-07T09:00:00",
                TABLES, packs_twice(), args.shots, evals=twice_probe,
                pre_extra="window.__MRB_SENDREC__=[];\n")
            print("--- ONE CHILD, TWO CLASSES ---\n" + g12["summary"] + "\n")
            check(g12["chaseRows"] == 2,
                  "twice: a child in TWO classes is listed ONCE",
                  "three owing rows across two classes, two children; got %d"
                  % g12["chaseRows"])
            check("2 students to chase" in g12["summary"],
                  "twice: and the summary counts children, not rows",
                  repr(g12["summary"]))
            rm = json.loads(g12["remind"])
            check(not rm.get("error"), "twice: the reminder control is pressable",
                  rm.get("error", ""))
            if not rm.get("error"):
                check(rm["calls"] == 2 and rm["rows"] == 3,
                      "twice: the write itself is still PER PAPER",
                      "two classes, three rows — the shared child is nudged "
                      "about each paper they owe; got %d call(s), %d row(s)"
                      % (rm["calls"], rm["rows"]))
                check(rm["children"] == 2,
                      "twice: over two distinct children", "got %d" % rm["children"])
                check(rm["label"] == "Reminded 2 students",
                      "twice: and the footer counts CHILDREN, not rows",
                      "it summed rows.length and said 'Reminded 3 students' "
                      "over a panel showing two; got %r" % rm["label"])
            check(vis12, "twice: the page is actually PAINTED")
            check(not e12, "twice: no console errors", "; ".join(e12[:2]))
    finally:
        try: server.shutdown()
        except Exception: pass

    print("\n   screenshots -> %s" % args.shots)
    if fails:
        print("\n%d CHECK(S) FAILED:" % len(fails))
        for f in fails: print("   - " + f)
        return 1
    print("\nall checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
