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

def entry(eid, cid, wd, per, name, ks, yg):
    return {"id": eid, "class_id": cid, "weekday": wd, "period": per,
            "week_cycle": None, "source": "seeded", "academic_year_id": YEAR,
            "deleted_at": None, "teacher_id": TEACHER,
            "classes": klass(cid, name, ks, yg)}

# A week shaped like a real one: Monday busy, Wednesday light, Friday empty.
ENTRIES = [
    entry("eeeeeeee-0000-4000-8000-000000000001", "cccccccc-0000-4000-8000-000000000001", 1, 1, "8r/Sc1",  "KS3", 8),
    entry("eeeeeeee-0000-4000-8000-000000000002", "cccccccc-0000-4000-8000-000000000002", 1, 2, "10h/Ph1", "KS4", 10),
    entry("eeeeeeee-0000-4000-8000-000000000003", "cccccccc-0000-4000-8000-000000000003", 1, 4, "7h/Sc5",  "KS3", 7),
    entry("eeeeeeee-0000-4000-8000-000000000004", "cccccccc-0000-4000-8000-000000000001", 3, 2, "8r/Sc1",  "KS3", 8),
    entry("eeeeeeee-0000-4000-8000-000000000005", "cccccccc-0000-4000-8000-000000000002", 3, 5, "10h/Ph1", "KS4", 10),
]

YEARS = [{"id": YEAR, "name": "2026-27", "start_date": "2026-09-01",
          "end_date": "2027-08-31", "deleted_at": None}]

TABLES = {
    "timetable_entries": ENTRIES,
    "academic_years":    YEARS,
    "classes":           [klass("cccccccc-0000-4000-8000-000000000001","8r/Sc1","KS3",8), klass("cccccccc-0000-4000-8000-000000000002","10h/Ph1","KS4",10),
                          klass("cccccccc-0000-4000-8000-000000000003","7h/Sc5","KS3",7)],
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


def run_case(b, base, name, when, tables, packs, shots, width=1280):
    """One state. A FRESH PAGE TARGET each time, because
    `Page.addScriptToEvaluateOnNewDocument` is per-target — reusing a page
    would carry the previous case's frozen clock into the next one."""
    pre = ("window.__MRB_STUB__=%s;\n" % json.dumps({"uid": TEACHER, "tables": tables, "log": []}))
    pre += STUB_JS + (FREEZE % when) + (PACKS % json.dumps(packs)) + PACK_JS

    p = b.page("about:blank", settle=0.2)
    p.send("Page.addScriptToEvaluateOnNewDocument", {"source": pre})
    p.goto(base + "/teacher/today.html", settle=3.5)
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
                  "var nav=document.querySelector('nav.top-nav');"
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
    return text or "", shot, overflow, errs, visible


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
            t, s1, ov, errs, vis = run_case(b, base, "1-weekday", "2026-09-07T09:00:00",
                                       TABLES, packs_for(), args.shots)
            print("\n--- WEEKDAY ---\n" + t[:800] + "\n")
            check("Monday" in t, "weekday: names the day")
            # ⚠️ CASE-FOLDED. `innerText` applies `text-transform`, so the
            # eyebrow written as "Period 1" reads back as "PERIOD 1".
            # Asserting the source casing tests the stylesheet, not the page.
            T = t.upper()
            check("PERIOD 1" in T and "PERIOD 2" in T and "PERIOD 4" in T,
                  "weekday: periods by NUMBER and in order")
            check(not re.search(r"\b\d{2}:\d{2}\b", t),
                  "weekday: NO clock times invented", "school_period_times is empty")
            check("8r/Sc1" in t and "10h/Ph1" in t and "7h/Sc5" in t,
                  "weekday: all three classes drawn")
            check("Science" in t and "Physics" in t,
                  "weekday: subject from the class CODE")
            check("1 of 3 in" in t, "weekday: chase count from the union predicate")
            check("nothing to chase" in t, "weekday: a class that is all in reads clear")
            check("No work set this week." in t,
                  "weekday: a class with no work says so", "and offers no action")
            check("Higher" not in t and "Foundation" not in t,
                  "weekday: no tier / pathway anywhere")
            check(vis, "weekday: the page is actually PAINTED", "not a blank screen")
            check(not errs, "weekday: no console errors", "; ".join(errs[:2]))

            # ── 2. Saturday ──────────────────────────────────────────────
            t2, s2, _, e2, vis2 = run_case(b, base, "2-weekend", "2026-09-12T09:00:00",
                                     TABLES, packs_for(), args.shots)
            print("--- WEEKEND ---\n" + t2[:500] + "\n")
            check("No lessons at the weekend" in t2, "weekend: says so plainly")
            check("NEXT: MONDAY" in t2.upper(), "weekend: shows the next teaching day, LABELLED")
            check("TODAY\u2019S LESSONS" not in t2.upper() and "TODAY'S LESSONS" not in t2.upper(),
                  "weekend: does NOT present it as today")
            check(vis2, "weekend: the page is actually PAINTED")
            check(not e2, "weekend: no console errors", "; ".join(e2[:2]))

            # ── 3. a weekday with no lessons (Friday) ────────────────────
            t3, s3, _, e3, vis3 = run_case(b, base, "3-empty-day", "2026-09-11T09:00:00",
                                     TABLES, packs_for(), args.shots)
            print("--- EMPTY WEEKDAY ---\n" + t3[:400] + "\n")
            check("No lessons today" in t3, "empty weekday: says so")
            check("NEXT:" in t3.upper(), "empty weekday: falls forward, labelled")
            check(vis3, "empty weekday: the page is actually PAINTED")

            # ── 4. no timetable at all ───────────────────────────────────
            empty = dict(TABLES); empty["timetable_entries"] = []
            t4, s4, _, e4, vis4 = run_case(b, base, "4-no-timetable", "2026-09-07T09:00:00",
                                     empty, {}, args.shots)
            print("--- NO TIMETABLE ---\n" + t4[:400] + "\n")
            check("No timetable yet" in t4, "no timetable: says so")
            check("Period" not in t4, "no timetable: invents no lessons")
            check("upload" not in t4.lower(),
                  "no timetable: promises no upload", "that screen is not built")
            check(vis4, "no timetable: the page is actually PAINTED")

            # ── 5. 390px ─────────────────────────────────────────────────
            t5, s5, ov5, e5, vis5 = run_case(b, base, "5-390px", "2026-09-07T09:00:00",
                                       TABLES, packs_for(), args.shots, width=390)
            check(not ov5, "390px: no horizontal overflow")
            check("8r/Sc1" in t5, "390px: still renders the lessons")
            check(vis5, "390px: the page is actually PAINTED")
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
