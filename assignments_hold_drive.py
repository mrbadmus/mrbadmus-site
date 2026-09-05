#!/usr/bin/env python3
"""
assignments_hold_drive.py — MRB-324, the assignments go-live hold, driven on
the real `teacher/admin.html`.

⚑ WHAT THIS GATE IS ACTUALLY FOR.

`schools.assignments_open_from` is Mide's dial for delaying the day a school
starts composing assignments. The backend half is gated by its own drive in
the backend repo. This gate watches the FRONTEND half, and it exists for one
reason above the others:

  ⚠️ THE CONTROL MUST NEVER BECOME A DIRECT DATABASE WRITE.

`teacher/admin.html` says of itself that it makes no direct database write —
every `sb.` call on it is a `.select()` — and that is the property that lets
it be shipped against production data on the strength of RLS alone. The hold
is the page's FIRST mutating control, and the tempting way to build it is one
line: `sb.from('schools').update({assignments_open_from: v})`. RLS would even
permit it, so it would appear to work when a school_admin tried it.

It is wrong in two ways that no manual test would show:

  · `schools_admin_update` carries NO column list, so that one line hands the
    browser "rewrite your school row" — name, code, kind, active,
    email_domains, admin_user_id — as the capability behind a date picker.

  · the policy wants `auth_user_has_scope('school_admin')`, while the gate on
    the page itself is `MrBadmusAdminScope.isAdmin` — school_admin OR slt OR
    legacy admin. An SLT user therefore SEES the control, and their direct
    write matches zero rows and comes back from PostgREST as a cheerful 200
    with an empty array. A silent no-op that looks exactly like a save. On
    the morning of a live dry run that is the worst failure available.

So the central assertion here is NOT a rendered string. The stub client
records every mutating verb reached on it, and the drive demands the count is
ZERO while the control is used four times over. A future author who "tidies"
the fetch into a Supabase call turns this gate red immediately.

⚑ WHAT ELSE IT WATCHES.

  · the three states the card can be in, which are three different sentences
    and easy to get backwards: no hold, a hold still ahead, and a date that
    has already passed (which is NOT a hold any more, and saying it is would
    be a lie about whether work is being set);
  · the body actually POSTed — `{assignments_open_from: 'YYYY-MM-DD'}` on
    Save and `{assignments_open_from: null}` on "Start now" — because the
    sentence on screen and the body on the wire are two different facts and
    only the second one changes anything;
  · that the Authorization header is a bearer token from the live session;
  · that the card repaints from the SERVER's answer rather than from what was
    typed, so a date the backend normalised or refused cannot be shown as
    saved;
  · that a refusal shows the backend's own words and does NOT repaint.

⚑ THE CLOCK IS FROZEN, and it has to be. "Is this date in the future" is the
whole logic of the card's three states; against a real clock 2026-09-14 is a
hold today, "already started" next month, and this file asserts a different
thing every day until it asserts nothing.

⚑ NO NETWORK AND NO CREDENTIALS. The CDN hosts and supabase.co are blocked at
the protocol level, the page is served from the repo root over a local port,
and `fetch` is replaced before the page's own script runs — nothing here can
reach the real backend, and a slow CDN cannot turn a push amber.

`needs` names `teacher/admin.html`: it is one of the four hand-written teacher
pages, so the repo copy is the source of truth and the built copy under
`mrbadmus_site/` is a restamped duplicate of it.
"""

import argparse, json, os, sys

import ks3_browser as cdp

# Frozen "now". Chosen so the fixture's three dates are unambiguous:
#   2026-09-14 is AHEAD  → a live hold
#   2026-08-20 is BEHIND → a date that has already passed
WHEN = "2026-09-05T09:00:00"
AHEAD = "2026-09-14"
BEHIND = "2026-08-20"

SCHOOL = "18969b5e-0412-41ae-9ee1-f5bd90624f18"
UID = "11111111-2222-3333-4444-555555555555"


STUB_JS = r"""
(function () {
  var S = window.__MRB_STUB__;
  window.__MRB_POSTS__ = [];
  /* ⚑ THE CENTRAL SEAM. Every mutating verb reached on the Supabase client is
     recorded here, and the drive demands this stays empty. See the header. */
  window.__MRB_WRITES__ = [];

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
    function writeVerb(verb) {
      return function (payload) {
        window.__MRB_WRITES__.push({
          table: table, verb: verb,
          payload: payload ? JSON.parse(JSON.stringify(payload)) : null
        });
        return api;
      };
    }
    var api = {
      select: function () { return api; },
      order:  function () { return api; },
      limit:  function () { return api; },
      eq: function (c, v) { fs.push({op:'eq', col:c, val:v}); return api; },
      is: function (c, v) { fs.push({op:'is', col:c, val:v}); return api; },
      in: function (c, v) { fs.push({op:'in', col:c, val:v}); return api; },
      single: function () { one = true; return api; },
      maybeSingle: function () { one = true; return api; },
      /* Present and recorded rather than absent: a page that called one of
         these against a client that did not have it would throw, and a throw
         is a different failure with a different diagnosis. Recording lets the
         drive name the exact verb and table that broke the invariant. */
      update: writeVerb('update'),
      insert: writeVerb('insert'),
      upsert: writeVerb('upsert'),
      delete: writeVerb('delete'),
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
    auth: {
      getUser: function () { return Promise.resolve({data: {user: user}, error: null}); },
      getSession: function () {
        return Promise.resolve({data: {session: {user: user, access_token: S.token}}, error: null});
      },
      signOut: function () { return Promise.resolve({error: null}); },
      onAuthStateChange: function () {
        return {data: {subscription: {unsubscribe: function () {}}}};
      }
    }
  };

  /* GETTERS, NOT ASSIGNMENTS — teacher-guard.js and teacher-admin-nav.js are
     loaded without defer and assign these globals before the page's own
     inline script runs, so a plain assignment from this document-start hook
     is overwritten a few milliseconds later by the real file. */
  function hold(name, value) {
    Object.defineProperty(window, name, {
      configurable: true,
      get: function () { return value; },
      set: function () { /* the real file's own assignment, ignored */ }
    });
  }

  hold('supabase', {createClient: function () { return client; }});
  hold('MrBadmusConfig', {environment: 'test', BACKEND_URL: 'https://backend.invalid'});

  hold('MrBadmusTeacherGuard', {
    requireTeacherRole: function (opts) {
      var onAllowed = (opts && opts.onAllowed) || function () {};
      return Promise.resolve().then(function () {
        return onAllowed({
          user: {id: S.uid},
          profile: {first_name: 'Ada', last_name: 'Nwosu', role: 'admin', school_id: S.school}
        });
      });
    },
    getClient: function () { return client; },
    signOut: function () {},
    ALLOWED_ROLES: ['teacher', 'hod', 'admin']
  });

  /* Admin-scoped, so the page renders rather than showing its refusal. The
     REAL predicate is exercised by the teacher gates; here it would only add
     a second copy of staff_scopes fixture data to keep in step. */
  hold('MrBadmusAdminScope', {
    isAdmin: function () { return Promise.resolve(true); },
    mount: function () {}
  });

  hold('MrBadmusTeacherData', {
    loadAcademicYears: function () {
      return Promise.resolve({
        working: {id: 'year-2627', name: '2026-27',
                  start_date: '2026-09-01', end_date: '2027-08-31'},
        years: []
      });
    },
    loadClassMatrices: function () { return Promise.resolve({}); }
  });

  /* fetch, replaced wholesale. Records the call and answers with whatever the
     case asked for. Anything the page fetches that is NOT the hold endpoint
     is refused loudly rather than silently allowed to reach the network. */
  window.fetch = function (url, opts) {
    opts = opts || {};
    var body = null;
    try { body = opts.body ? JSON.parse(opts.body) : null; } catch (e) { body = String(opts.body); }
    window.__MRB_POSTS__.push({
      url: String(url),
      method: opts.method || 'GET',
      auth: (opts.headers && (opts.headers.Authorization || opts.headers.authorization)) || null,
      body: body
    });
    var r = S.response;
    return Promise.resolve({
      ok: r.status >= 200 && r.status < 300,
      status: r.status,
      json: function () { return Promise.resolve(r.body); }
    });
  };
})();
"""


FREEZE = r'''
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


def tables(open_from):
    return {
        "schools": [{"id": SCHOOL, "name": "Rainford High School",
                     "assignments_open_from": open_from}],
        "classes": [],
        "class_teachers": [],
        "profiles": [],
        "staff_scopes": [],
        "pending_staff": [],
    }


def open_page(b, base, open_from, response, shots, name):
    stub = {
        "uid": UID, "school": SCHOOL, "token": "stub-jwt-token",
        "tables": tables(open_from),
        "response": response,
    }
    pre = "window.__MRB_STUB__=%s;\n" % json.dumps(stub)
    pre += STUB_JS + (FREEZE % WHEN)

    p = b.page("about:blank", settle=0.2)
    p.send("Page.addScriptToEvaluateOnNewDocument", {"source": pre})
    p.send("Network.enable")
    p.send("Network.setBlockedURLs", {"urls": [
        "*cdn.jsdelivr.net*", "*cdnjs.cloudflare.com*", "*supabase.co*",
    ]})
    p.goto(base + "/teacher/admin.html", settle=1.2)
    try:
        p.send("Page.captureScreenshot", {})
    except Exception:
        pass
    return p


def state_of(p):
    return p.eval("""(function(){
      var c = document.getElementById('hold-card');
      var s = document.getElementById('hold-state');
      var i = document.getElementById('hold-date');
      var m = document.getElementById('hold-msg');
      return JSON.stringify({
        visible: !!c && c.style.display !== 'none',
        text: s ? s.textContent.replace(/\\s+/g,' ').trim() : null,
        input: i ? i.value : null,
        msg: m ? m.textContent.trim() : null
      });
    })()""")


def click_and_settle(p, sel, settle=0.6):
    p.eval("document.getElementById('%s').click()" % sel)
    # The handler is async (getSession → fetch → repaint). Poll rather than
    # sleeping a fixed time, so a slow machine does not go red.
    import time
    deadline = time.time() + 8.0
    while time.time() < deadline:
        n = p.eval("window.__MRB_POSTS__.length")
        if n and int(n) > 0:
            break
        time.sleep(0.05)
    time.sleep(settle)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--shots", default="/tmp/mrb324-hold")
    args = ap.parse_args()
    os.makedirs(args.shots, exist_ok=True)

    fails = []

    def check(ok_, what, detail=""):
        print("   %s  %s%s" % ("PASS" if ok_ else "FAIL", what,
                               ("  - " + detail) if detail else ""))
        if not ok_:
            fails.append(what)

    root = os.path.dirname(os.path.abspath(__file__))
    server, port = cdp.serve(root)
    base = "http://127.0.0.1:%d" % port

    OK_AHEAD = {"status": 200, "body": {"ok": True, "school_id": SCHOOL,
                                        "assignments_open_from": AHEAD, "previous": None}}
    OK_NULL = {"status": 200, "body": {"ok": True, "school_id": SCHOOL,
                                       "assignments_open_from": None, "previous": AHEAD}}

    try:
        with cdp.Browser() as b:

            # ══ 1. no hold ════════════════════════════════════════════════
            print("\n--- state: no hold set (null) ---")
            p = open_page(b, base, None, OK_AHEAD, args.shots, "null")
            s = json.loads(state_of(p))
            print("   state: %r" % s["text"])
            check(s["visible"], "the card renders")
            check("running normally" in (s["text"] or ""),
                  "null: says assignments are running normally", repr(s["text"]))
            check("on hold" not in (s["text"] or ""),
                  "null: does NOT say on hold", repr(s["text"]))
            check(s["input"] == "", "null: the date field is empty", repr(s["input"]))

            # ══ 2. a hold still ahead ═════════════════════════════════════
            print("\n--- state: a hold still ahead (%s, today %s) ---" % (AHEAD, WHEN[:10]))
            p = open_page(b, base, AHEAD, OK_AHEAD, args.shots, "ahead")
            s = json.loads(state_of(p))
            print("   state: %r" % s["text"])
            check("on hold" in (s["text"] or ""),
                  "ahead: says assignments are ON HOLD", repr(s["text"]))
            check("14 Sep 2026" in (s["text"] or ""),
                  "ahead: names the date in words", repr(s["text"]))
            check(s["input"] == AHEAD,
                  "ahead: the picker is PRE-FILLED with the date that is set",
                  repr(s["input"]))

            # ── the Save seam ─────────────────────────────────────────────
            p.eval("document.getElementById('hold-date').value = '2026-09-21'")
            click_and_settle(p, "hold-save")
            posts = json.loads(p.eval("JSON.stringify(window.__MRB_POSTS__)"))
            writes = json.loads(p.eval("JSON.stringify(window.__MRB_WRITES__)"))
            check(len(posts) == 1, "Save: exactly one request went out",
                  "got %d" % len(posts))
            if posts:
                q = posts[0]
                check(q["method"] == "POST", "Save: it is a POST", q["method"])
                check(q["url"].endswith("/api/admin/school/assignments-open-from"),
                      "Save: to the hold endpoint", q["url"])
                check(q["auth"] == "Bearer stub-jwt-token",
                      "Save: carries the session's bearer token", repr(q["auth"]))
                check(q["body"] == {"assignments_open_from": "2026-09-21"},
                      "Save: the BODY carries the typed date", json.dumps(q["body"]))
            check(writes == [],
                  "⚠️ Save made NO direct database write",
                  json.dumps(writes))

            # It repaints from the SERVER's answer, not from what was typed.
            # The stub answered 2026-09-14 while 2026-09-21 was typed.
            s = json.loads(state_of(p))
            check("14 Sep 2026" in (s["text"] or "") and "21 Sep" not in (s["text"] or ""),
                  "Save: the card repaints from the SERVER's value, not the typed one",
                  repr(s["text"]))
            check(s["msg"] == "Saved.", "Save: says it saved", repr(s["msg"]))

            # ══ 3. Start now ══════════════════════════════════════════════
            print("\n--- Start now lifts the hold ---")
            p = open_page(b, base, AHEAD, OK_NULL, args.shots, "open")
            click_and_settle(p, "hold-open")
            posts = json.loads(p.eval("JSON.stringify(window.__MRB_POSTS__)"))
            writes = json.loads(p.eval("JSON.stringify(window.__MRB_WRITES__)"))
            check(len(posts) == 1 and posts[0]["body"] == {"assignments_open_from": None},
                  "Start now: POSTs null, not today's date",
                  json.dumps(posts[0]["body"]) if posts else "no request")
            check(writes == [], "⚠️ Start now made NO direct database write",
                  json.dumps(writes))
            s = json.loads(state_of(p))
            check("running normally" in (s["text"] or "") and "on hold" not in (s["text"] or ""),
                  "Start now: the card returns to running normally", repr(s["text"]))

            # ══ 4. a date that has already passed ═════════════════════════
            print("\n--- state: a date already passed (%s) ---" % BEHIND)
            p = open_page(b, base, BEHIND, OK_AHEAD, args.shots, "behind")
            s = json.loads(state_of(p))
            print("   state: %r" % s["text"])
            check("on hold" not in (s["text"] or ""),
                  "passed: a date behind us is NOT reported as a hold", repr(s["text"]))
            check("running normally" in (s["text"] or ""),
                  "passed: says assignments are running", repr(s["text"]))
            check(s["input"] == BEHIND,
                  "passed: the picker still shows the stored date", repr(s["input"]))

            # ══ 5. a refusal ══════════════════════════════════════════════
            print("\n--- the backend refuses ---")
            refuse = {"status": 403, "body": {
                "error": "admin_required",
                "message": "Only a school admin can change the assignments start date."}}
            p = open_page(b, base, AHEAD, refuse, args.shots, "refused")
            p.eval("document.getElementById('hold-date').value = '2026-09-21'")
            click_and_settle(p, "hold-save")
            s = json.loads(state_of(p))
            check("Only a school admin" in (s["msg"] or ""),
                  "refused: the backend's OWN sentence is shown", repr(s["msg"]))
            check("14 Sep 2026" in (s["text"] or ""),
                  "refused: the card does NOT repaint to the rejected date",
                  repr(s["text"]))
            check(json.loads(p.eval("JSON.stringify(window.__MRB_WRITES__)")) == [],
                  "⚠️ refused: still no direct database write")

            # ══ 6. NEGATIVE CONTROL ═══════════════════════════════════════
            # A drive that stubs this much can go vacuously green. Prove the
            # seam can actually SEE a write by making one deliberately on the
            # same stub client the page was handed, and demanding the recorder
            # notices. If this passes silently, every "no direct write" check
            # above is worthless.
            print("\n--- negative control: can the recorder see a write at all? ---")
            p.eval("""(function(){
              var c = MrBadmusTeacherGuard.getClient();
              c.from('schools').update({assignments_open_from: '2026-01-01'});
            })()""")
            seen = json.loads(p.eval("JSON.stringify(window.__MRB_WRITES__)"))
            check(len(seen) == 1 and seen[0]["verb"] == "update"
                  and seen[0]["table"] == "schools",
                  "negative control: a deliberate direct write IS recorded",
                  json.dumps(seen))

    finally:
        try:
            server.shutdown()
        except Exception:
            pass

    print("\n" + ("=" * 60))
    if fails:
        print("FAILED %d check(s):" % len(fails))
        for f in fails:
            print("  · " + f)
        return 1
    print("assignments_hold_drive: all checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
