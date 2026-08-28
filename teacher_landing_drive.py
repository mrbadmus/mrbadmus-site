#!/usr/bin/env python3
"""MRB-293 — drive the real teacher landing as three real signed-in teachers.

Proves, in a real browser against the real TEST project under real RLS:
  · Rich (hod scope, teaches ONE class) sees exactly his own — the leak persona
  · Amy and Ben CO-TEACH `HZ 10A Science`, and it shows for BOTH

The old shape and the new shape are measured in the SAME page, SAME session,
SAME RLS — so the contrast is the filter and nothing else.
"""
import json, os, re, ssl, sys, urllib.request

REPO = "/Users/midebadmus/Documents/GitHub/mrbadmus-site"
sys.path.insert(0, REPO); os.chdir(REPO)
import ks3_browser as cdp

REF  = "qeppkiswvclkkwbxmlok"
URL  = "https://%s.supabase.co" % REF
YEAR = "2f560a43-73b9-422a-8fc7-ec46524a288a"      # TEST 2025-26, holds the fixtures
PORT = 5500
CTX  = ssl.create_default_context(cafile="/etc/ssl/cert.pem")

TEACHERS = [
    ("Rich (hod scope — the leak persona)", "hz_rich@test.mrbadmus",
     "ee000000-0000-0000-0000-000000001001", ["HZ 10B Physics"]),
    ("Amy (co-teacher A)",                  "hz_amy@test.mrbadmus",
     "ee000000-0000-0000-0000-000000001002", ["HZ 10A Science"]),
    ("Ben (co-teacher B)",                  "hz_ben@test.mrbadmus",
     "ee000000-0000-0000-0000-000000001003", ["HZ 10A Science"]),
]

def anon_key():
    src = open("shared/config.js", encoding="utf-8").read()
    return re.search(r"'(eyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+)'",
                     src[src.index("const TEST"):]).group(1)

def service_key():
    for line in open("/Users/midebadmus/Documents/GitHub/mrbadmus---backend/.env"):
        if line.startswith("SUPABASE_SERVICE_ROLE_KEY="):
            return line.split("=", 1)[1].strip()
    raise SystemExit("no service key")

def post(url, body, key, method="POST", bearer=None):
    req = urllib.request.Request(
        url, data=json.dumps(body).encode(),
        headers={"apikey": key, "Authorization": "Bearer " + (bearer or key),
                 "Content-Type": "application/json"}, method=method)
    with urllib.request.urlopen(req, timeout=60, context=CTX) as r:
        return json.loads(r.read().decode())

def main():
    anon, svc = anon_key(), service_key()
    pw = "mrb293-drive-only"   # set on the three TEST fixtures by SQL; fake accounts
    print("\n🔐  MRB-293 — the teacher landing, driven as three real teachers (TEST)\n")

    fails = []
    def check(ok, what, detail=""):
        print("     %s %s%s" % ("✅" if ok else "❌", what,
                                ("  — " + detail) if detail else ""))
        if not ok: fails.append(what)

    server, port = cdp.serve("mrbadmus_site", port=PORT)
    try:
        with cdp.Browser() as b:
            for label, email, uid, expected in TEACHERS:
                sess = post("%s/auth/v1/token?grant_type=password" % URL,
                            {"email": email, "password": pw}, anon)

                p = b.page("http://localhost:%d/leaderboard.html?env=test" % port,
                           settle=2.0)
                signed = p.eval("""
                  (async function () {
                    var c = window.supabase.createClient(%s, %s);
                    var r = await c.auth.setSession({access_token: %s, refresh_token: %s});
                    return r.error ? 'error: ' + r.error.message : 'ok';
                  })()
                """ % (json.dumps(URL), json.dumps(anon),
                       json.dumps(sess["access_token"]),
                       json.dumps(sess["refresh_token"])))

                print("\n  ── %s ─────────────────────────────" % label)
                check(signed == "ok", "signed in", str(signed))

                p = b.page("http://localhost:%d/teacher/classes.html?env=test" % port,
                           settle=1.0)
                p.set_viewport(1280, 1400)
                p.goto("http://localhost:%d/teacher/classes.html?env=test" % port,
                       settle=6.0)

                res = p.eval("""
                  (async function () {
                    var sb = window.MrBadmusTeacherGuard.getClient();
                    var sel = 'class_id, subject_id, subject:subject_id ( name ), ' +
                      'class:class_id ( id, name, deleted_at, academic_year_id )';
                    var self = (await sb.auth.getSession()).data.session.user.id;
                    function names(rows) {
                      var s = {};
                      (rows||[]).forEach(function (r) {
                        if (r.class && !r.class.deleted_at &&
                            r.class.academic_year_id === %s) s[r.class.name] = 1;
                      });
                      return Object.keys(s).sort();
                    }
                    // OLD shape — permissions only, exactly what shipped
                    var oldq = await sb.from('class_teachers').select(sel)
                      .is('deleted_at', null).is('ended_at', null);
                    // NEW shape — the same query, self-filtered
                    var newq = await sb.from('class_teachers').select(sel)
                      .eq('teacher_id', self)
                      .is('deleted_at', null).is('ended_at', null);
                    // and the REAL function the page actually calls
                    var real = await window.MrBadmusTeacherData
                      .loadTeacherClasses(%s, { metrics: false });
                    return { old: names(oldq.data), new: names(newq.data),
                             real: real.map(function (c) { return c.name; }).sort(),
                             onScreen: Array.prototype.map.call(
                               document.querySelectorAll('[data-class-name]'),
                               function (n) { return n.textContent.trim(); }).sort() };
                  })()
                """ % (json.dumps(YEAR), json.dumps(YEAR)))

                print("       old shape (no self filter) : %s" % res["old"])
                print("       new shape (self filtered)  : %s" % res["new"])
                print("       loadTeacherClasses() returns: %s" % res["real"])
                check(sorted(res["real"]) == sorted(expected),
                      "the real function returns exactly this teacher's classes",
                      "expected %s" % expected)
                check(sorted(res["new"]) == sorted(expected),
                      "new shape matches")
                if label.startswith("Rich"):
                    check(len(res["old"]) > len(res["new"]),
                          "old shape LEAKED other teachers' classes",
                          "%d vs %d" % (len(res["old"]), len(res["new"])))
                if "co-teacher" in label:
                    check("HZ 10A Science" in res["real"],
                          "co-taught class STILL VISIBLE to this teacher")

                shot = "/private/tmp/claude-501/-Users-midebadmus-Documents-GitHub-mrbadmus-site/7e808475-0806-48c9-b300-74c5f9cda6a6/scratchpad/mrb293-%s.png" % email.split("@")[0]
                p.screenshot(shot, full_page=True)
                print("       screenshot: %s" % shot)
    finally:
        server.shutdown()

    print("\n" + ("  ❌ FAIL: " + "; ".join(fails) if fails else
                  "  ✅ PASS — self-filter scopes to the signed-in teacher, and\n"
                  "     the co-taught class still shows for BOTH its teachers."))
    return 1 if fails else 0

sys.exit(main())
