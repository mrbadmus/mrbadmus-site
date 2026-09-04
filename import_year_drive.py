#!/usr/bin/env python3
"""MRB-307 — drive `teacher/import.html` and prove which SCHOOL YEAR an import lands in.

    python3 import_year_drive.py                 # both cases
    python3 import_year_drive.py --shots DIR     # write screenshots somewhere

⚑ THE DEFECT THIS EXISTS FOR.

  On 1 September 2026 a real roster import enrolled 14 real students into
  LAST YEAR's 7h/Sc5. This year's class stayed empty. Nothing on screen had
  ever named a year, so nothing on screen could have looked wrong.

  The page sent `academicYearName: null`, and the `roster-import` edge
  function fell back to `academic_years.is_current` — a flag moved BY HAND on
  1 September. On the morning it mattered it still pointed at 2025-26.

  That defect is invisible to every assertion that reads ONE year. A fixture
  with a single academic year passes whether the page resolves the year
  correctly, reads `is_current`, or sends null — all three roads lead to the
  only row there is. So the fixture below holds TWO years and points
  `is_current` at the WRONG one. The trap has to be in the data or the gate
  is decoration.

⚠️ THE CLOCK IS FROZEN, and it is load-bearing. `workingAcademicYear()` is
  date-based — the earliest year whose `end_date` is still ahead of today+30d
  — so a drive on the real clock proves a different thing every day it runs,
  and proves nothing at all after 31 Aug 2027. Frozen to 2026-09-04 the
  working year is unambiguously 2026-27, and the answer is the same forever.

⚑ WHAT IT DRIVES, AND WHERE THE STUBS SIT.

  The REAL page, the REAL `shared/class-entry.js` (which owns the one
  `workingAcademicYear` predicate, MRB-267), and the page's own rendering all
  run unmodified. Stubbed: the Supabase client, the teacher guard, and
  PapaParse. Nothing here touches either project, and nothing here touches
  the network — see NO NETWORK below.

  The central assertion is not a rendered string. It is the BODY actually
  handed to `functions.invoke('roster-import', …)`, captured by replacing
  `invoke` with a recorder. A page can name the right year in its own note
  and still send null a screen later; the note is what the teacher reads, the
  body is what enrols the children.

⚑ THE NEGATIVE CONTROL (`--case negative`, and it runs by default).

  A gate that stubs this much can go vacuously green: stub one thing too many
  and the drive ends up asserting its own fixture back to itself. So the same
  drive runs a second time with `MRBClassEntry.workingAcademicYear` FORCED to
  return the 2025-26 row, and demands the payload then say `2025-26`.

  If the negative case still yields 2026-27, the payload is not coming from
  the working-year resolution at all and every check above is measuring
  something else. That exits non-zero, exactly like a real failure — a gate
  that cannot fail is not a gate.

⚑ NO NETWORK, TWICE OVER.

  The page loads supabase-js, PapaParse and SheetJS from CDNs. Both belts are
  worn on purpose:

    1. the three CDN hosts are BLOCKED at the protocol level
       (`Network.setBlockedURLs`), so a machine with no internet, or a CDN
       having a bad day, cannot turn this gate amber; and
    2. `window.Papa` is installed as a GETTER that swallows assignment, the
       same trick `today_drive.py` uses for `window.supabase` — so even if a
       bundle did arrive it could not displace the stub.

  SheetJS is deliberately NOT stubbed: `XLSX` is only reachable through the
  .xlsx branch, and this drive feeds a .csv. A stub there would be scenery.
"""

import argparse, json, os, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ks3_browser as cdp

TEACHER = "11111111-1111-1111-1111-111111111111"
SCHOOL  = "55555555-5555-5555-5555-555555555555"

# ── The two-year fixture. `is_current` points at the WRONG year on purpose ──
#
# ⚠️ DO NOT "TIDY" THIS TO ONE YEAR, and do not move `is_current` onto
# 2026-27. Both edits make every check below pass against a page that reads
# is_current, which is the page that enrolled 14 students into last year.
#
# `school_id` and `deleted_at` are plumbing, not fixture: the page's fallback
# read filters on both, so rows without them would never come back and the
# drive would be measuring an empty list.
YEARS = [
    {"id": "ay-2025", "name": "2025-26", "start_date": "2025-09-01",
     "end_date": "2026-08-31", "is_current": True,          # ← THE TRAP
     "school_id": SCHOOL, "deleted_at": None},
    {"id": "ay-2026", "name": "2026-27", "start_date": "2026-09-01",
     "end_date": "2027-08-31", "is_current": False,         # ← THE ANSWER
     "school_id": SCHOOL, "deleted_at": None},
]

WORKING = "2026-27"
STALE   = "2025-26"

# Frozen so `lookaheadDate()` lands on 2026-10-04: 2025-26 has already ended,
# 2026-27 has not, and the working year cannot be argued about.
WHEN = "2026-09-04T09:00:00"

CLASS_NAME = "7h/Sc5"   # Year 7 → KS3, so no pathway/tier is required

# ── The class TWINS. Same name, one per year, and both are needed ──────────
#
# The success screen links straight to the class the import just filled. When
# roster-import returns no class ids (every deployment before the MRB-307
# backend change) the page looks the id up itself, scoped to school + WORKING
# YEAR + name. That lookup is the same defect one surface later: with only one
# `7h/Sc5` in the table it resolves correctly whatever it filters on.
#
# ⚠️ SO THERE ARE TWO, AND THE CHECK IS WHICH ONE IT PICKS. Drop the
# `academic_year_id` filter and the lookup matches two rows, refuses to guess,
# and falls back to the class list — a visible failure. Filter on the WRONG
# year and it opens last year's empty twin, which is the original defect
# wearing a different coat. The negative control drives exactly that.
CLASSES = [
    {"id": "cls-2026", "name": CLASS_NAME, "academic_year_id": "ay-2026",
     "school_id": SCHOOL, "deleted_at": None},
    {"id": "cls-2025", "name": CLASS_NAME, "academic_year_id": "ay-2025",
     "school_id": SCHOOL, "deleted_at": None},
]

TABLES = {
    "academic_years": YEARS,
    "classes": CLASSES,
    "profiles": [{"id": TEACHER, "first_name": "Ada", "last_name": "Nwosu",
                  "display_name": "Ms Nwosu", "role": "teacher",
                  "school_id": SCHOOL}],
    "subjects": [{"id": "subj-science", "name": "Science", "active": True}],
    # teacher-admin-nav.js asks for these on boot. An empty list is the
    # honest answer for a plain teacher and keeps the Admin link off.
    "staff_scopes": [],
}

# ⚠️ NEVER A REAL STUDENT. This file is checked in, read by people, and the
# defect it commemorates is about real children being put in the wrong class.
# `example.invalid` is reserved by RFC 2606 and can never route anywhere.
CSV = ("email,first_name,last_name,class\n"
       "test.student@example.invalid,Test,Student,7h/Sc5\n")


STUB_JS = r"""
(function () {
  var S = window.__MRB_STUB__;
  window.__MRB_INVOKES__ = [];

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
    /* ⚑ THE CENTRAL SEAM. Everything else in this file exists to get one
       honest call to land here. The body is deep-copied at capture time
       because the page reuses `lastPayload`, and a live reference would let
       a later mutation rewrite what we think we saw. */
    functions: {
      invoke: function (name, opts) {
        var body = (opts && opts.body) || null;
        window.__MRB_INVOKES__.push({
          name: name,
          body: body ? JSON.parse(JSON.stringify(body)) : null
        });
        var data = {
          ok: true,
          counts: {classesCreated: 1, classesFound: 0, studentsAttached: 1,
                   studentsCreated: 1, profilesUpdated: 0, studentsSkipped: 0},
          issues: []
        };
        /* TWO RESPONSE SHAPES, because two are deployed.
           `S.newBackend` false is the OLD roster-import: counts and nothing
           else. That is what is live right now, and it is the shape the
           success screen's deep link must work against WITHOUT a backend
           release — the page looks the class id up itself.
           `S.newBackend` true adds `academicYear` and `classes:[{name,id}]`,
           the answer the updated function will send. The link has to land in
           the same place either way, or the teacher's experience depends on
           which deployment happened to answer. */
        if (S.newBackend) {
          data.academicYear = S.landedYear;
          data.classes = S.landedClasses;
        }
        return Promise.resolve({data: data, error: null});
      }
    },
    auth: {
      getUser: function () { return Promise.resolve({data: {user: user}, error: null}); },
      /* `sessionState()` re-checks this immediately before BOTH posts and
         refuses to send if the id moved. A stub that returned no session
         would make the drive green by never reaching the seam at all. */
      getSession: function () {
        return Promise.resolve({data: {session: {user: user, access_token: 'stub'}}, error: null});
      },
      signOut: function () { return Promise.resolve({error: null}); },
      onAuthStateChange: function () {
        return {data: {subscription: {unsubscribe: function () {}}}};
      }
    }
  };

  /* ⚠️ GETTERS, NOT ASSIGNMENTS — the `today_drive.py` trick, and needed here
     for a second reason on top of the CDN one. `teacher-guard.js` is loaded
     WITHOUT defer and assigns `window.MrBadmusTeacherGuard` before the page's
     own inline IIFE runs, so a plain assignment from this document-start
     script is overwritten a few milliseconds later by the real guard — which
     would then try to validate a JWT that does not exist and bounce the drive
     to auth.html. Swallowing the write keeps the stub in place. */
  function hold(name, value) {
    Object.defineProperty(window, name, {
      configurable: true,
      get: function () { return value; },
      set: function () { /* the real file's own assignment, ignored */ }
    });
  }

  hold('supabase', {createClient: function () { return client; }});

  /* The guard's contract, read off shared/teacher-guard.js: `onAllowed` is
     called with { user, profile } and the page reads `profile.school_id`,
     `profile.first_name` and `user.id` out of it; `getClient()` hands back
     the same client the guard validated against (teacher-admin-nav.js asks
     for it too). Deferred one turn so the page sees the same asynchronous
     shape the real guard has. */
  hold('MrBadmusTeacherGuard', {
    requireTeacherRole: function (opts) {
      var onAllowed = (opts && opts.onAllowed) || function () {};
      return Promise.resolve().then(function () {
        return onAllowed({
          user: {id: S.uid},
          profile: {first_name: 'Ada', last_name: 'Nwosu',
                    display_name: 'Ms Nwosu', role: 'teacher',
                    school_id: S.school}
        });
      });
    },
    getClient: function () { return client; },
    signOut: function () {},
    ALLOWED_ROLES: ['teacher', 'hod', 'admin']
  });

  /* PapaParse, small enough for the one synthetic file this drive feeds and
     no larger. The page hands `Papa.parse` a File and reads back
     `results.meta.fields` + `results.data` as header-keyed objects, so that
     is exactly what this returns. Quoted fields are handled because a real
     MIS export has them and a parser that silently mangles one would make a
     future author distrust the gate rather than the file. */
  function splitLine(line) {
    var out = [], cur = '', q = false;
    for (var i = 0; i < line.length; i++) {
      var ch = line[i];
      if (q) {
        if (ch === '"' && line[i + 1] === '"') { cur += '"'; i++; }
        else if (ch === '"') { q = false; }
        else { cur += ch; }
      } else if (ch === '"') { q = true; }
      else if (ch === ',') { out.push(cur.trim()); cur = ''; }
      else { cur += ch; }
    }
    out.push(cur.trim());
    return out;
  }
  hold('Papa', {
    parse: function (file, opts) {
      opts = opts || {};
      var reader = new FileReader();
      reader.onload = function () {
        try {
          var lines = String(reader.result || '').split(/\r?\n/)
            .filter(function (l) { return l.trim() !== ''; });
          var fields = splitLine(lines[0] || '');
          var data = lines.slice(1).map(function (l) {
            var cells = splitLine(l), o = {};
            fields.forEach(function (h, i) { o[h] = cells[i] == null ? '' : cells[i]; });
            return o;
          });
          opts.complete({meta: {fields: fields}, data: data});
        } catch (e) {
          if (opts.error) { opts.error(e); }
        }
      };
      reader.onerror = function () { if (opts.error) { opts.error(new Error('read failed')); } };
      reader.readAsText(file);
    }
  });
})();
"""

FREEZE = r'''
/* Freeze the clock. `workingAcademicYear()` compares `end_date` against a
   real `new Date()` plus 30 days, so an unfrozen drive asserts a different
   fact every day and stops asserting anything at all in Sep 2027. */
(function () {
  var FIXED = new Date("%s");
  var RealDate = Date;
  function D(a, b, c, d, e, f, g) {
    if (!(this instanceof D)) { return FIXED.toString(); }
    /* ⚠️ ARITY MATTERS — `new Date(str, undefined)` parses its first argument
       as a YEAR, so forwarding a fixed argument count turns every
       one-argument construction in the page into an Invalid Date. */
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

FORCE_YEAR_JS = r'''
/* THE NEGATIVE CONTROL. Forces the ONE predicate (shared/class-entry.js's
   `workingAcademicYear`, MRB-267) to answer with the stale year, so the drive
   can check that the payload FOLLOWS it. If the payload still says the right
   thing here, the payload is not reading the predicate and every positive
   check in this file is measuring something other than what it claims.

   A setter, not a poll: class-entry.js is `defer`red but the page's own
   guard chain can reach `loadWorkingYear()` before any timer fires, and a
   poll that lost that race would patch nothing and report a false green —
   which is the exact failure mode this control exists to detect. */
(function () {
  var want = "%s";
  var held;
  function patch(v) {
    if (v && typeof v === 'object' && !v.__mrbForced) {
      v.__mrbForced = true;
      v.workingAcademicYear = function (rows) {
        return (rows || []).filter(function (y) { return y && y.name === want; })[0] || null;
      };
    }
    return v;
  }
  Object.defineProperty(window, 'MRBClassEntry', {
    configurable: true,
    get: function () { return held; },
    set: function (v) { held = patch(v); }
  });
})();
'''

FEED_JS = r"""
(function () {
  var input = document.getElementById('file-input');
  if (!input) { return 'no #file-input'; }
  /* The page reads `input.files[0]` on the change event, so the drive has to
     put a real File into a real FileList. `DataTransfer` is the only way to
     build one from script — CDP's DOM.setFileInputFiles wants a path on disk
     and would make this gate depend on a temp file it has to clean up. */
  var f = new File([window.__MRB_CSV__], 'roster.csv', {type: 'text/csv'});
  var dt = new DataTransfer();
  dt.items.add(f);
  input.files = dt.files;
  input.dispatchEvent(new Event('change', {bubbles: true}));
  return 'ok';
})()
"""

# The subject select only exists because a teacher is auto-assigned, and
# `classIsComplete()` refuses a class that has a teacher and no subject — so
# screen 2 cannot be left without picking one. This is the teacher's click.
PICK_SUBJECT_JS = r"""
(function () {
  var sel = document.querySelector('#class-settings-list select[data-subject]');
  if (!sel) { return 'no subject select'; }
  for (var i = 0; i < sel.options.length; i++) {
    if (sel.options[i].value) {
      sel.value = sel.options[i].value;
      sel.dispatchEvent(new Event('change', {bubbles: true}));
      return sel.value;
    }
  }
  return 'no subject options';
})()
"""

CLICK_JS = ("(function(){var e=document.getElementById('%s');"
            "if(!e){return 'missing';} if(e.disabled){return 'disabled';}"
            "e.click(); return 'ok';})()")


def wait_for(p, expr, what, timeout=15.0, poll=0.1):
    """Poll a JS predicate. Raises with the failing expression named, because
    a drive that times out silently and then fails eight checks sends the
    reader hunting for a page bug that is really a harness bug."""
    deadline = time.time() + timeout
    while time.time() < deadline:
        try:
            if p.eval(expr):
                return True
        except cdp.JSError:
            pass
        time.sleep(poll)
    raise RuntimeError("timed out after %.0fs waiting for %s  [%s]" % (timeout, what, expr))


def wait_soft(p, expr, timeout=6.0, poll=0.1):
    """Poll, but REPORT rather than raise on timeout.

    `setSuccessLink()` sets the fallback href synchronously and only then
    awaits the class lookup, so "not resolved yet" and "resolved to the
    fallback" look identical from outside. A hard wait would turn a real
    fallback — a genuine failure of the deep link — into a harness timeout,
    which reads like a broken gate rather than a broken page. This waits for
    the good state, gives up quietly, and lets the CHECK do the failing."""
    deadline = time.time() + timeout
    while time.time() < deadline:
        try:
            if p.eval(expr):
                return True
        except cdp.JSError:
            pass
        time.sleep(poll)
    return False


def run_case(b, base, force_year, shots, name, new_backend=False):
    """One pass through the whole import, start to enrolment.

    A FRESH PAGE TARGET each time: `Page.addScriptToEvaluateOnNewDocument` is
    per-target, so reusing one would carry the positive case's un-forced
    predicate into the negative case and make the control vacuous."""
    pre = "window.__MRB_STUB__=%s;\n" % json.dumps(
        {"uid": TEACHER, "school": SCHOOL, "tables": TABLES,
         "newBackend": bool(new_backend),
         "landedYear": WORKING,
         "landedClasses": [{"name": CLASS_NAME, "id": "cls-2026"}]})
    pre += "window.__MRB_CSV__=%s;\n" % json.dumps(CSV)
    pre += STUB_JS + (FREEZE % WHEN)
    if force_year:
        pre += FORCE_YEAR_JS % force_year

    p = b.page("about:blank", settle=0.2)
    p.send("Page.addScriptToEvaluateOnNewDocument", {"source": pre})

    # Belt 1 of the no-network rule (belt 2 is the `Papa` getter in STUB_JS).
    # A push gate must not be able to go amber because a CDN is slow.
    p.send("Network.enable")
    p.send("Network.setBlockedURLs", {"urls": [
        "*cdn.jsdelivr.net*", "*cdnjs.cloudflare.com*", "*supabase.co*",
    ]})

    p.goto(base + "/teacher/import.html", settle=0.6)

    out = {}

    # ── screen 1: the page admits which year it is about to import into ──
    wait_for(p, "document.body.style.display === 'block'", "the guard to reveal the page")
    wait_for(p,
             "(function(){var n=document.getElementById('working-year-note');"
             "return !!n && n.style.display !== 'none' &&"
             " n.textContent.indexOf('Checking') === -1;})()",
             "the working year to resolve")
    out["note"] = p.eval("document.getElementById('working-year-note').textContent")

    # ── feed the CSV the way a teacher does ──
    out["feed"] = p.eval(FEED_JS)
    wait_for(p, "!document.getElementById('to-screen-2').disabled",
             "the file to parse and unlock screen 2")
    out["to2"] = p.eval(CLICK_JS % "to-screen-2")

    # ── screen 2: the year is beside every class name ──
    wait_for(p, "document.getElementById('screen-2').classList.contains('show')",
             "screen 2 to show")
    wait_for(p,
             "document.querySelectorAll('#class-settings-list .class-setting[data-class]').length > 0",
             "the class rows to render")
    out["years_beside_classes"] = p.eval(
        "JSON.stringify(Array.prototype.map.call("
        "document.querySelectorAll('#class-settings-list .class-setting-year'),"
        "function(e){return e.textContent.trim();}))")
    out["class_rows"] = p.eval(
        "document.querySelectorAll('#class-settings-list .class-setting[data-class]').length")
    out["screen2_text"] = p.eval("document.getElementById('screen-2').innerText")
    p.screenshot(os.path.join(shots, name + "-screen2.png"), width=1280)

    out["subject"] = p.eval(PICK_SUBJECT_JS)

    # ── screen 3: the dry run, which is the first thing to leave the page ──
    wait_for(p, "!document.getElementById('to-screen-3').disabled",
             "the year AND the staff/subject lists to unblock review")
    out["to3"] = p.eval(CLICK_JS % "to-screen-3")
    wait_for(p, "window.__MRB_INVOKES__.length >= 1", "the dry-run invoke")

    # ── the real write ──
    wait_for(p, "!document.getElementById('confirm-import').disabled",
             "a clean dry run to enable Confirm")
    out["confirm"] = p.eval(CLICK_JS % "confirm-import")
    wait_for(p, "window.__MRB_INVOKES__.length >= 2", "the confirmed import invoke")

    out["invokes"] = json.loads(p.eval("JSON.stringify(window.__MRB_INVOKES__)"))

    # ── the success screen, and the class it sends the teacher to ──
    wait_for(p, "document.getElementById('success-panel').classList.contains('show')",
             "the success panel")
    # The link is rewritten ASYNCHRONOUSLY — `setSuccessLink()` paints the
    # class-list fallback first and only then awaits the lookup — so reading
    # it the instant the panel appears would photograph the fallback and
    # call the deep link broken on every run.
    out["link_settled"] = wait_soft(
        p, "document.getElementById('success-back-link')"
           ".getAttribute('href').indexOf('class-detail.html') !== -1")
    out["success_href"] = p.eval(
        "document.getElementById('success-back-link').getAttribute('href')")
    out["success_link_text"] = p.eval(
        "document.getElementById('success-back-link').textContent.trim()")
    out["success_summary"] = p.eval(
        "document.getElementById('success-summary').textContent"
        ".replace(/[\\s\\u00a0]+/g, ' ').trim()")
    p.screenshot(os.path.join(shots, name + "-screen3.png"), width=1280)

    # The favicon 404 is the static server's. ERR_BLOCKED_BY_CLIENT is this
    # drive's own CDN block, deliberate and reported by Chrome as an error.
    out["errors"] = [e for e in p.console_errors()
                     if "favicon" not in e and "ERR_BLOCKED_BY_CLIENT" not in e
                     and "net::ERR_" not in e]
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--shots", default="/tmp/mrb307-import")
    args = ap.parse_args()
    os.makedirs(args.shots, exist_ok=True)

    fails = []
    def check(ok_, what, detail=""):
        print("   %s  %s%s" % ("PASS" if ok_ else "FAIL", what,
                               ("  - " + detail) if detail else ""))
        if not ok_:
            fails.append(what)

    # The REPO ROOT, not mrbadmus_site/. `teacher/import.html` is one of the
    # four hand-written teacher pages (CLAUDE.md), so the repo copy is the
    # source of truth and the built copy is a stamp-restamped duplicate of it.
    # Serving the root also resolves /shared/*.js from the same tree.
    root = os.path.dirname(os.path.abspath(__file__))
    server, port = cdp.serve(root)
    base = "http://127.0.0.1:%d" % port

    try:
        with cdp.Browser() as b:
            # ══ CASE 1 — the page as it ships ══════════════════════════════
            print("\n--- POSITIVE: two years, is_current on the WRONG one ---")
            r = run_case(b, base, None, args.shots, "positive")

            print("   note: %r" % r["note"])
            print("   class-year chips: %s" % r["years_beside_classes"])

            check(WORKING in r["note"], "screen 1: the note NAMES the working year",
                  "expected %s in %r" % (WORKING, r["note"]))
            check(STALE not in r["note"],
                  "screen 1: the note never names the stale year",
                  "is_current points at %s; the note must not repeat it" % STALE)

            chips = json.loads(r["years_beside_classes"])
            check(r["class_rows"] == 1, "screen 2: the one class rendered",
                  "got %s rows" % r["class_rows"])
            check(chips == ["· " + WORKING],
                  "screen 2: the year sits beside the class name",
                  "expected ['· %s'], got %s" % (WORKING, chips))
            check(STALE not in r["screen2_text"],
                  "screen 2: nothing on the screen mentions the stale year")

            inv = r["invokes"]
            check(len(inv) == 2, "two invokes: a dry run and the real one",
                  "got %d" % len(inv))
            check(all(i["name"] == "roster-import" for i in inv),
                  "both invokes go to roster-import",
                  str([i["name"] for i in inv]))

            dry, real = (inv + [{}, {}])[0], (inv + [{}, {}])[1]
            dryb  = dry.get("body") or {}
            realb = real.get("body") or {}

            # ⚑ THE CENTRAL ASSERTION. Everything above is what the teacher
            # reads; this is what enrols the children.
            check(realb.get("academicYearName") == WORKING,
                  "THE PAYLOAD: the confirmed import names the working year",
                  "academicYearName = %r, expected %r — this is the MRB-307 "
                  "defect exactly" % (realb.get("academicYearName"), WORKING))
            check(dryb.get("academicYearName") == WORKING,
                  "the dry run names the same year it will write",
                  "a preview of a different year than the write is a lie: %r"
                  % (dryb.get("academicYearName"),))
            check(realb.get("academicYearName") is not None,
                  "the payload never leaves the year for the backend to GUESS",
                  "null is what fell through to is_current on 1 Sep 2026")
            check(dryb.get("dryRun") is True and realb.get("dryRun") is False,
                  "the two invokes are a dry run then a write, in that order",
                  "%r then %r" % (dryb.get("dryRun"), realb.get("dryRun")))

            klasses = realb.get("classes") or []
            check(len(klasses) == 1 and klasses[0].get("name") == CLASS_NAME
                  and klasses[0].get("keyStage") == "KS3",
                  "the payload carries the KS3 class as named", str(klasses))
            studs = realb.get("students") or []
            check(len(studs) == 1 and studs[0].get("className") == CLASS_NAME,
                  "the student is attached to that class", str(studs))

            print("   success link: %r -> %r" % (r["success_link_text"], r["success_href"]))
            print("   success summary: %r" % r["success_summary"])

            # ⚑ THE DEEP LINK, RESOLVED WITHOUT THE NEW BACKEND. The stubbed
            # invoke returns counts only — the shape live today — so the page
            # has to find the class id itself, and it has to find the right
            # one of two rows that differ ONLY by year.
            check(r["link_settled"] and "class=cls-2026" in r["success_href"],
                  "success: the button deep-links to THIS YEAR's class",
                  "href = %r; the old roster-import sends no class ids, so "
                  "this is the page's own year-scoped lookup"
                  % (r["success_href"],))
            check("cls-2025" not in r["success_href"],
                  "success: it never resolves last year's TWIN",
                  "two classes are named %s, one per year; href = %r"
                  % (CLASS_NAME, r["success_href"]))
            check(r["success_link_text"] == "Go to " + CLASS_NAME,
                  "success: the button names the class, not the list",
                  "read %r, expected 'Go to %s'"
                  % (r["success_link_text"], CLASS_NAME))
            check(WORKING in r["success_summary"] and STALE not in r["success_summary"],
                  "success: the summary names the working year and only it",
                  r["success_summary"])

            check(not r["errors"], "no console errors", "; ".join(r["errors"][:3]))

            # ══ CASE 2 — the new roster-import response ════════════════════
            # The updated edge function answers with `academicYear` and
            # `classes:[{name,id}]`, so no lookup is needed. The teacher must
            # land in the SAME place either way — a deep link that works only
            # on one of two live deployments is a deep link nobody can trust.
            print("\n--- NEW BACKEND: response carries academicYear + class ids ---")
            nb = run_case(b, base, None, args.shots, "new-backend", new_backend=True)
            print("   success link: %r -> %r" % (nb["success_link_text"], nb["success_href"]))
            print("   success summary: %r" % nb["success_summary"])

            check(nb["link_settled"] and "class=cls-2026" in nb["success_href"],
                  "new backend: the button deep-links to the same class",
                  "href = %r" % (nb["success_href"],))
            check("cls-2025" not in nb["success_href"],
                  "new backend: still never last year's twin",
                  nb["success_href"])
            check(nb["success_link_text"] == "Go to " + CLASS_NAME,
                  "new backend: the button names the class",
                  nb["success_link_text"])
            check("Everyone went into %s in the %s school year."
                  % (CLASS_NAME, WORKING) in nb["success_summary"],
                  "new backend: the summary names the class AND the year",
                  "read %r" % (nb["success_summary"],))
            nbreal = ((nb["invokes"] + [{}, {}])[1].get("body")) or {}
            check(nbreal.get("academicYearName") == WORKING,
                  "new backend: the payload still names the working year",
                  repr(nbreal.get("academicYearName")))
            check(not nb["errors"], "new backend: no console errors",
                  "; ".join(nb["errors"][:3]))

            # ══ CASE 3 — the negative control ══════════════════════════════
            print("\n--- NEGATIVE CONTROL: predicate forced to the stale year ---")
            n = run_case(b, base, STALE, args.shots, "negative")
            ninv = n["invokes"]
            nreal = ((ninv + [{}, {}])[1].get("body")) or {}
            print("   note: %r" % n["note"])
            print("   payload academicYearName: %r" % nreal.get("academicYearName"))

            # ⚠️ THIS CASE EXPECTS THE WRONG ANSWER. Read the check names
            # before "fixing" one: green here means the page FOLLOWS the
            # predicate, which is what makes the positive case meaningful.
            check(nreal.get("academicYearName") == STALE,
                  "control: the payload FOLLOWS the predicate",
                  "forced %s, payload said %r — if this says %s the payload "
                  "is not reading workingAcademicYear() at all and every "
                  "check above is vacuous"
                  % (STALE, nreal.get("academicYearName"), WORKING))
            check(STALE in n["note"],
                  "control: the note follows the predicate too",
                  "note said %r — the screen and the payload must never "
                  "disagree about the year" % (n["note"],))
            nchips = json.loads(n["years_beside_classes"])
            check(nchips == ["· " + STALE],
                  "control: the class chip follows it as well", str(nchips))

            # ⚑ THIS IS WHAT MAKES THE TWINS MEAN SOMETHING. Forced onto the
            # stale year, the lookup must open the STALE twin — proving the
            # `academic_year_id` filter is what chooses between two rows with
            # the same name, and not the row order in the fixture. (Drop the
            # filter entirely and neither case resolves: two rows match, the
            # page refuses to guess, and both fall back to the class list.)
            print("   success link: %r -> %r" % (n["success_link_text"], n["success_href"]))
            check("class=cls-2025" in n["success_href"],
                  "control: the deep link follows the year filter",
                  "forced %s, href = %r — if this still says cls-2026 the "
                  "lookup is not year-scoped and the positive case above is "
                  "picking the right twin by accident"
                  % (STALE, n["success_href"]))
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
