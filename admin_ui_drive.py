#!/usr/bin/env python3
"""admin_ui_drive.py — the operator console's browser self-review (MRB-317 admin-ui).

    EXTRA_CORS_ORIGINS=http://localhost:8131 CONSUMER_SIGNUP_ENABLED=true PORT=3131 node server.js
    python3 admin_ui_drive.py --api http://localhost:3131 --port 8131

Modelled directly on night3_flagon_smoke.py: same flag-on-for-this-browser-only
setter, same real-API fixtures, same teardown. It drives the BUILT tree
(mrbadmus_site/), never the source pages.

Phases:
  A  flag OFF          — both admin pages are "Not found", zero SDK/API requests
  B  flag on, no sess  — both bounce to /auth.html (NOT /consumer/signup.html)
  C  flag on, teacher  — both are "Not found"; the routes 404 for that JWT
  D  flag on, operator — consumer/admin-accounts.html
  E  flag on, operator — consumer/admin-queue.html
"""
import argparse, json, os, re, ssl, sys, time, urllib.request, urllib.error

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ks3_browser as cdp

SB = "https://qeppkiswvclkkwbxmlok.supabase.co"
CTX = ssl.create_default_context(cafile="/etc/ssl/cert.pem")
FAILS = []
SCRATCH = "/private/tmp/claude-501/-Users-midebadmus-Documents-GitHub-mrbadmus-worktrees-b2c-launch/f0d1d849-b2b5-42f6-adaa-1d3c56c76a59/scratchpad"
STATE_FILE = os.path.join(SCRATCH, "admin_fixtures.json")

OPERATOR = ("hz_op@test.mrbadmus", "Night3!Op")
TEACHER = ("hz_amy@test.mrbadmus", "mrb293-drive-only")
PW = "Passw0rd!admindrive"
TAG = "advdrive"   # every fixture name carries it, so nothing is ambiguous


def check(ok, label, evidence=""):
    print(("  OK  " if ok else "  XX  ") + label + (("  — " + str(evidence)[:400]) if evidence else ""))
    if not ok:
        FAILS.append(label)


def env(name):
    for line in open("/Users/midebadmus/Documents/GitHub/mrbadmus-worktrees/b2c/backend/.env"):
        if line.startswith(name + "="):
            return line.split("=", 1)[1].strip()
    return None


SERVICE = env("SUPABASE_SERVICE_ROLE_KEY")
ANON = env("SUPABASE_ANON_KEY")


def http(method, url, body=None, headers=None, timeout=90):
    data = json.dumps(body).encode() if body is not None else None
    h = {"Content-Type": "application/json"}
    h.update(headers or {})
    req = urllib.request.Request(url, data=data, method=method, headers=h)
    try:
        with urllib.request.urlopen(req, context=CTX, timeout=timeout) as r:
            t = r.read().decode()
            return r.status, (json.loads(t) if t else None)
    except urllib.error.HTTPError as e:
        t = e.read().decode()
        try:
            return e.code, json.loads(t)
        except Exception:
            return e.code, t


def sb_admin(method, path, body=None):
    return http(method, SB + path, body,
                {"apikey": SERVICE, "Authorization": "Bearer " + SERVICE,
                 "Prefer": "return=representation"})


def sign_in(email, pw):
    st, d = http("POST", SB + "/auth/v1/token?grant_type=password",
                 {"email": email, "password": pw}, {"apikey": ANON})
    assert st == 200, (email, st, d)
    return d


def api(method, path, jwt=None, body=None):
    h = {"Authorization": "Bearer " + jwt} if jwt else {}
    return http(method, API + path, body, h)


FLAG_ON_JS = """(function(){var c=null;Object.defineProperty(window,'MrBadmusConfig',{configurable:true,
  get:function(){return c;}, set:function(v){ if(v&&typeof v==='object'){v.CONSUMER_SIGNUP_ENABLED=true;} c=v; }});})();"""


# ── browser helpers ───────────────────────────────────────────────────────
def qs(path):
    return BASE + path + ("&" if "?" in path else "?") + "env=test&api=" + API


def with_session(p, sess):
    p.goto(BASE + "/404.html?env=test", settle=0.2)
    p.eval("localStorage.clear()")
    p.eval("localStorage.setItem('sb-qeppkiswvclkkwbxmlok-auth-token', %s)"
           % json.dumps(json.dumps(sess)))


def clear_session(p):
    p.goto(BASE + "/404.html?env=test", settle=0.2)
    p.eval("localStorage.clear()")


def requests_seen(p):
    p.drain(0.3)
    out = []
    for ev in p._events:
        if ev.get("method") == "Network.requestWillBeSent":
            out.append(((ev.get("params") or {}).get("request") or {}).get("url", ""))
    return out


def wait_for(p, expr, tries=40, gap=0.35):
    for _ in range(tries):
        try:
            if p.eval(expr):
                return True
        except Exception:
            pass
        time.sleep(gap)
    return False


def text(p, sel="document.body"):
    return p.eval("(%s && %s.innerText) || ''" % (sel, sel)) or ""


def errs(p):
    # A route that legitimately answers 4xx (resend-verification on an already
    # confirmed address) makes Chrome log a "Failed to load resource" line. The
    # page handles it and says so in words; that is not a page error.
    return [e for e in p.console_errors()
            if "favicon.ico" not in e
            and not re.search(r"Failed to load resource.*(40[0-9]|409|423|429)", e)]


# ══════════════════════════════════════════════════════════════════════════
# fixtures
# ══════════════════════════════════════════════════════════════════════════
FAMILIES = [
    ("trialing",  "Trial family %s" % TAG,     "advdrive-trial@mrbadmus-test.com",   ["Amara", "Leo"]),
    ("active",    "Active family %s" % TAG,    "advdrive-active@mrbadmus-test.com",  ["Bola"]),
    ("past_due",  "Pastdue family %s" % TAG,   "advdrive-pastdue@mrbadmus-test.com", ["Chidi"]),
    ("cancelled", "Cancelled family %s" % TAG, "advdrive-cancel@mrbadmus-test.com",  ["Dara"]),
    ("locked",    "Locked family %s" % TAG,    "advdrive-locked@mrbadmus-test.com",  ["Efe"]),
]

NOSCHEME_Q = "zz-advdrive-levels"


def iso(delta_s):
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(time.time() + delta_s))


def set_sub(org, fields):
    body = dict(fields)
    st, d = sb_admin("PATCH", "/rest/v1/subscriptions?org_id=eq." + org, body)
    if st < 300 and isinstance(d, list) and d:
        return
    body["org_id"] = org
    st, d = sb_admin("POST", "/rest/v1/subscriptions", body)
    assert st < 300, (st, d)


def setup():
    ids = {"users": [], "orgs": [], "questions": [], "answers": []}
    print("\n── fixtures ──────────────────────────────────────────────")
    for state, name, email, kids in FAMILIES:
        st, d = sb_admin("POST", "/auth/v1/admin/users",
                         {"email": email, "password": PW, "email_confirm": True,
                          "user_metadata": {"first_name": name.split()[0]}})
        if st >= 300:
            st2, users = sb_admin("GET", "/auth/v1/admin/users?per_page=500")
            d = next(u for u in users["users"] if u["email"] == email)
        uid = d["id"]
        ids["users"].append(uid)
        sess = sign_in(email, PW)
        jwt = sess["access_token"]
        st, fam = api("POST", "/api/consumer/family/ensure", jwt, {"family_name": name})
        assert st == 200, (st, fam)
        org = fam["org_id"]
        ids["orgs"].append(org)
        kid_ids = []
        for i, k in enumerate(kids):
            st, c = api("POST", "/api/consumer/children", jwt, {
                "first_name": k, "year_group": 8,
                "username": ("adv%s%d%d" % (state[:3], int(time.time()) % 100000, i)),
                "password": "comet-saturn-42", "mode": "alongside_school",
                "intensity": "light", "exam_board": "AQA"})
            assert st == 200, (st, c)
            kid_ids.append(c["child_id"])
            ids["users"].append(c["child_id"])
        if state == "trialing":
            set_sub(org, {"status": "trialing", "trial_end": iso(6 * 86400), "quantity": len(kids)})
        elif state == "active":
            set_sub(org, {"status": "active", "trial_end": None, "quantity": 1,
                          "current_period_end": iso(20 * 86400), "billing_interval": "month",
                          "stripe_customer_id": "cus_advdrive_active"})
        elif state == "past_due":
            set_sub(org, {"status": "past_due", "trial_end": None, "quantity": 1,
                          "current_period_end": iso(-2 * 86400), "retry_at": iso(3 * 86400),
                          "billing_interval": "month"})
        elif state == "cancelled":
            set_sub(org, {"status": "canceled", "trial_end": None, "quantity": 1,
                          "current_period_end": iso(10 * 86400), "canceled_at": iso(-86400),
                          "billing_interval": "month"})
        elif state == "locked":
            set_sub(org, {"status": "locked", "trial_end": None, "quantity": 1,
                          "current_period_end": iso(-40 * 86400), "locked_at": iso(-10 * 86400),
                          "billing_interval": "month"})
        ids.setdefault("fam", {})[state] = {"org": org, "parent": uid, "kids": kid_ids, "name": name}
        print("  family %-9s %s  kids=%d" % (state, org, len(kid_ids)))

    # ── an organisation at its seat cap, created through the real route ──
    op = sign_in(*OPERATOR)
    st, o = api("POST", "/api/consumer/admin/orgs", op["access_token"], {
        "name": "Seatcap Centre %s" % TAG, "seat_cap": 2,
        "period_end": time.strftime("%Y-%m-%d", time.gmtime(time.time() + 300 * 86400)),
        "contact_name": "Cap Contact", "contact_email": "advdrive-org@mrbadmus-test.com"})
    assert st == 200, (st, o)
    org_id = o["org"]["id"]
    ids["orgs"].append(org_id)
    ids["org_seatcap"] = org_id
    sb_admin("PATCH", "/rest/v1/subscriptions?org_id=eq." + org_id, {"quantity": 2})
    print("  organisation (seat cap 2, quantity 2) %s  warnings=%s" % (org_id, o["org"]["warnings"]))

    # ── a levels-marked question ──
    # ⚠️ `exam_questions_scheme_is_array` is a CHECK: scheme must be an array
    # with at least one element, so a question with NO scheme cannot exist in
    # the database at all. The page's numeric fallback is still reachable —
    # `schemePoint()` drops a point whose shape it does not recognise, and a
    # levels grid is exactly that shape — so the fixture carries a levels
    # descriptor in `scheme` rather than an empty array.
    st, q = sb_admin("POST", "/rest/v1/exam_questions", {
        "id": NOSCHEME_Q, "key_stage": "KS3", "subject": "Chemistry",
        "topic": "Extended response", "marks": 6,
        "text": "Describe and explain how the particle model accounts for the three states of matter. [6 marks]",
        "scheme": [{"level": 3, "descriptor": "Detailed and coherent — judged holistically."}],
        "levels": {"3": "Detailed, coherent", "2": "Some links", "1": "Simple statements"},
        "source": "advdrive-fixture", "active": True})
    if st < 300:
        ids["questions"].append(NOSCHEME_Q)
    print("  levels-marked question %s (%s)" % (NOSCHEME_Q, st))

    # ── three queued answers at three ages ──
    # ⚠️ `ai_hits` is smallint[] and holds the INDEXES of the scheme points the
    # instant marker awarded (marking.js: `hits.push(i)` … `hits.includes(i)`),
    # NOT one boolean per point. The fixtures are written in that real shape.
    tf = ids["fam"]["trialing"]
    rows = [
        (tf["kids"][0], "bv2-ib-1a", 6, 1, 3, [1],
         "Sodium gives its electron away and chlorine takes it."),
        (tf["kids"][1], "bv2-ib-1c", 70, 2, 3, [0, 2],
         "Metals lose electrons so they go positive. Non metals gain them."),
        (tf["kids"][0], NOSCHEME_Q, 26, 3, 6, [],
         "In a solid the particles are in a fixed pattern and vibrate. In a liquid they can slide past "
         "each other. In a gas they are far apart and move quickly in all directions."),
    ]
    for kid, qid, hours, score, mx, hits, ans in rows:
        st, a = sb_admin("POST", "/rest/v1/exam_answers", {
            "org_id": tf["org"], "child_id": kid, "question_id": qid, "answer": ans,
            "ai_score": score, "ai_max": mx, "ai_hits": hits,
            "ai_feedback": "Instant mark: name the particles and say what they do.",
            "ai_model": "advdrive", "ai_marked_at": iso(-hours * 3600),
            "status": "sent_to_mb", "sent_to_mb_at": iso(-hours * 3600)})
        assert st < 300, (st, a)
        ids["answers"].append(a[0]["id"])
        print("  queued answer %s  age=%dh  q=%s" % (a[0]["id"][:8], hours, qid))

    json.dump(ids, open(STATE_FILE, "w"), indent=1)
    return ids


def teardown(ids):
    print("\n── cleanup ───────────────────────────────────────────────")
    for aid in ids.get("answers", []):
        sb_admin("DELETE", "/rest/v1/exam_answers?id=eq." + aid)
    for org in ids.get("orgs", []):
        # family/ensure creates a class + academic year; both hold FKs on the school.
        st, classes = sb_admin("GET", "/rest/v1/classes?select=id&school_id=eq." + org)
        for c in (classes or []):
            st, assigns = sb_admin("GET", "/rest/v1/assignments?select=id&class_id=eq." + c["id"])
            for a_ in (assigns or []):
                st, subs = sb_admin("GET", "/rest/v1/assignment_submissions?select=id&assignment_id=eq." + a_["id"])
                for s_ in (subs or []):
                    sb_admin("DELETE", "/rest/v1/assignment_question_attempts?submission_id=eq." + s_["id"])
                sb_admin("DELETE", "/rest/v1/assignment_submissions?assignment_id=eq." + a_["id"])
                sb_admin("DELETE", "/rest/v1/assignment_questions?assignment_id=eq." + a_["id"])
            sb_admin("DELETE", "/rest/v1/assignments?class_id=eq." + c["id"])
            sb_admin("DELETE", "/rest/v1/class_members?class_id=eq." + c["id"])
            sb_admin("DELETE", "/rest/v1/class_teachers?class_id=eq." + c["id"])
        sb_admin("DELETE", "/rest/v1/classes?school_id=eq." + org)
        for t in ("stripe_events", "email_log", "ai_usage_events", "exam_answers",
                  "unit_check_attempts", "work_items", "child_plans", "family_messages",
                  "consumer_notifications", "org_limits", "account_deletion_requests"):
            sb_admin("DELETE", "/rest/v1/%s?org_id=eq.%s" % (t, org))
        for t in ("pending_staff", "staff_scopes"):
            sb_admin("DELETE", "/rest/v1/%s?school_id=eq.%s" % (t, org))
        sb_admin("DELETE", "/rest/v1/audit_log?school_id=eq." + org)
        sb_admin("DELETE", "/rest/v1/subscriptions?org_id=eq." + org)
    for u in ids.get("users", []):
        for t, col in (("consumer_notifications", "recipient_id"), ("family_messages", "sender_id"),
                       ("family_messages", "recipient_id"), ("exam_answers", "child_id"),
                       ("unit_check_attempts", "child_id"), ("child_flashcard_queue", "child_id"),
                       ("work_items", "child_id"), ("work_generation_runs", "child_id"),
                       ("child_plans", "child_id"), ("ai_usage_events", "profile_id"),
                       ("email_log", "recipient_id"), ("class_members", "student_id"),
                       ("class_teachers", "teacher_id"), ("parent_prefs", "profile_id"),
                       ("report_notes", "child_id"), ("audit_log", "actor_id")):
            sb_admin("DELETE", "/rest/v1/%s?%s=eq.%s" % (t, col, u))
        sb_admin("PATCH", "/rest/v1/profiles?created_by=eq." + u, {"created_by": None})
    for u in ids.get("users", []):
        st, _ = sb_admin("DELETE", "/rest/v1/profiles?id=eq." + u)
        st2, r2 = sb_admin("DELETE", "/auth/v1/admin/users/" + u)
        if st2 >= 300:
            print("  ! user", u, st2, r2)
    for org in ids.get("orgs", []):
        sb_admin("DELETE", "/rest/v1/academic_years?school_id=eq." + org)
        st, r = sb_admin("DELETE", "/rest/v1/schools?id=eq." + org)
        print("  org", org, st, "" if st < 300 else r)
    for q in ids.get("questions", []):
        sb_admin("DELETE", "/rest/v1/exam_questions?id=eq." + q)
    # any organisation created through the FORM during the drive
    st, extras = sb_admin("GET", "/rest/v1/schools?select=id,name&name=like.*" + TAG + "*")
    for s in (extras or []):
        st, classes = sb_admin("GET", "/rest/v1/classes?select=id&school_id=eq." + s["id"])
        for c in (classes or []):
            sb_admin("DELETE", "/rest/v1/class_members?class_id=eq." + c["id"])
            sb_admin("DELETE", "/rest/v1/class_teachers?class_id=eq." + c["id"])
        sb_admin("DELETE", "/rest/v1/classes?school_id=eq." + s["id"])
        sb_admin("DELETE", "/rest/v1/audit_log?school_id=eq." + s["id"])
        sb_admin("DELETE", "/rest/v1/pending_staff?school_id=eq." + s["id"])
        sb_admin("DELETE", "/rest/v1/subscriptions?org_id=eq." + s["id"])
        sb_admin("DELETE", "/rest/v1/academic_years?school_id=eq." + s["id"])
        st2, r = sb_admin("DELETE", "/rest/v1/schools?id=eq." + s["id"])
        print("  leftover org", s["name"], st2, "" if st2 < 300 else r)


PAGES = ["/consumer/admin-accounts.html", "/consumer/admin-queue.html"]


# ══════════════════════════════════════════════════════════════════════════
# A — flag OFF
# ══════════════════════════════════════════════════════════════════════════
def phase_a():
    print("\n── A · flag OFF ──────────────────────────────────────────")
    with cdp.Browser() as b:
        p = b.attach()
        p.send("Network.enable")
        for path in PAGES:
            p.goto(qs(path), settle=1.2)
            t = text(p)
            reqs = requests_seen(p)
            offsite = [u for u in reqs if not u.startswith(BASE) and not u.startswith("data:")]
            bad = [u for u in offsite if "jsdelivr" in u or "supabase.co" in u]
            bad += [u for u in reqs if u.startswith(API + "/") or "/api/consumer/" in u.split("?", 1)[0]]
            check("Not found" in t, "A %s: renders Not found" % path, t[:120].replace("\n", " "))
            check(len(reqs) >= 4, "A %s: the network log is actually capturing" % path, len(reqs))
            check(not bad and not offsite, "A %s: zero SDK/API/offsite requests" % path,
                  bad + offsite if (bad or offsite) else reqs)
            check(not errs(p), "A %s: no console errors" % path, errs(p))


# ══════════════════════════════════════════════════════════════════════════
# B — flag on, signed out
# ══════════════════════════════════════════════════════════════════════════
def phase_b():
    print("\n── B · flag on, signed out ───────────────────────────────")
    with cdp.Browser() as b:
        p = b.attach()
        p.send("Page.addScriptToEvaluateOnNewDocument", {"source": FLAG_ON_JS})
        for path in PAGES:
            clear_session(p)
            p.goto(qs(path), settle=1.5)
            wait_for(p, "location.pathname !== '%s'" % path, tries=12, gap=0.3)
            url = p.eval("location.pathname")
            check(url == "/auth.html", "B %s: bounces to /auth.html (not signup)" % path, url)


# ══════════════════════════════════════════════════════════════════════════
# C — flag on, signed in as a NON-operator
# ══════════════════════════════════════════════════════════════════════════
def phase_c():
    print("\n── C · flag on, non-operator teacher ─────────────────────")
    sess = sign_in(*TEACHER)
    jwt = sess["access_token"]
    with cdp.Browser() as b:
        p = b.attach()
        p.send("Page.addScriptToEvaluateOnNewDocument", {"source": FLAG_ON_JS})
        for path in PAGES:
            with_session(p, sess)
            p.goto(qs(path), settle=1.5)
            wait_for(p, "/Not found/.test(document.body.innerText)", tries=20, gap=0.3)
            t = text(p)
            html = p.eval("document.body.innerHTML")
            check("Not found" in t and "isn" in t, "C %s: renders the Not found state" % path,
                  t[:140].replace("\n", " "))
            check("ac-room" not in html and "ad-room" not in html and "Queue" not in html,
                  "C %s: console markup is gone from the DOM" % path, html[:200])
    for route in ("/api/consumer/admin/accounts", "/api/consumer/admin/mb-queue"):
        st, d = api("GET", route, jwt)
        check(st == 404, "C %s with a teacher JWT → 404" % route, (st, d))
    st, d = api("POST", "/api/consumer/admin/orgs", jwt,
                {"name": "nope", "seat_cap": 1, "period_end": "2027-08-31",
                 "contact_email": "x@y.com"})
    check(st == 404, "C POST /api/consumer/admin/orgs with a teacher JWT → 404", (st, d))


CLICK_BY_TEXT = """(function(sel, needle){
  var b = Array.prototype.filter.call(document.querySelectorAll(sel), function(x){
    return x.textContent.indexOf(needle) >= 0; })[0];
  if (!b) return 'no-button';
  if (b.disabled) return 'disabled';
  b.click(); return 'clicked';
})(%s, %s)"""


def click_text(p, sel, needle):
    return p.eval(CLICK_BY_TEXT % (json.dumps(sel), json.dumps(needle)))


def last_msg(p):
    return p.eval("(function(){var m=document.querySelectorAll('.ac-act-msg:not([hidden])');"
                  "return m.length ? m[m.length-1].textContent : '';})()")


# ══════════════════════════════════════════════════════════════════════════
# D — operator · admin-accounts.html
# ══════════════════════════════════════════════════════════════════════════
def phase_d(ids, shots):
    print("\n── D · operator · admin-accounts ─────────────────────────")
    op = sign_in(*OPERATOR)
    jwt = op["access_token"]
    st, api_all = api("GET", "/api/consumer/admin/accounts", jwt)
    check(st == 200, "D GET /admin/accounts as operator → 200", st)
    stats = api_all["stats"]

    with cdp.Browser() as b:
        p = b.attach()
        p.send("Page.addScriptToEvaluateOnNewDocument", {"source": FLAG_ON_JS})
        with_session(p, op)
        p.goto(qs("/consumer/admin-accounts.html"), settle=1.2)
        ok = wait_for(p, "document.querySelectorAll('#rows .ac-row').length > 0")
        check(ok, "D accounts: the list renders", text(p)[:160].replace("\n", " "))
        check(p.eval("(function(){var m=document.getElementById('c-main');"
                     "return m ? getComputedStyle(m).display : 'missing';})()") != "none",
              "D accounts: the console is actually visible (#c-main not display:none)")
        check(not errs(p), "D accounts: no console errors", errs(p))
        check(p.eval("document.getElementById('who').textContent") == OPERATOR[0],
              "D accounts: header shows the operator's email")

        # ── stats strip ──
        tiles = p.eval("Array.prototype.map.call(document.querySelectorAll('.ac-stat'),"
                       "function(t){return [t.querySelector('.l').textContent, t.querySelector('.n').textContent];})")
        got = dict((k, v) for k, v in tiles)
        check(got.get("Families") == str(stats["families"]) and got.get("In trial") == str(stats["in_trial"])
              and got.get("Children") == str(stats["children"]) and got.get("Organisations") == str(stats["organisations"])
              and got.get("Past due") == str(stats["past_due"]),
              "D stats strip matches the API's stats", (got, stats))
        check(stats["in_trial"] == 1 and stats["past_due"] == 1 and stats["children"] == 6
              and stats["organisations"] >= 1,
              "D stats match what was seeded (1 trial, 1 past_due, 6 children)", stats)

        # ── filter pills ──
        for key in ("all", "trialing", "active", "past_due", "cancelled", "locked", "orgs"):
            st, d = api("GET", "/api/consumer/admin/accounts?filter=" + key, jwt)
            want = len(d["accounts"])
            p.eval("document.querySelector('[data-filter=\"%s\"]').click()" % key)
            ok = wait_for(p, "document.querySelectorAll('#rows .ac-row').length === %d "
                             "|| !document.getElementById('empty').hidden" % want, tries=20, gap=0.3)
            n = p.eval("document.querySelectorAll('#rows .ac-row').length")
            check(n == want, "D filter '%s' shows %d rows" % (key, want), n)
            if key == "trialing":
                check(p.eval("document.querySelector('#rows .ac-row .ac-name').textContent")
                      == ids["fam"]["trialing"]["name"], "D filter 'trialing' is the trial family")

        # ── search (server-side) ──
        p.eval("document.querySelector('[data-filter=\"all\"]').click()")
        wait_for(p, "document.querySelectorAll('#rows .ac-row').length > 1")
        p.eval("(function(){var q=document.getElementById('q');q.value='Pastdue family advdrive';"
               "q.dispatchEvent(new Event('input'));})()")
        ok = wait_for(p, "document.querySelectorAll('#rows .ac-row').length === 1", tries=50, gap=0.5)
        name = p.eval("(document.querySelector('#rows .ac-name')||{}).textContent")
        check(ok and name == ids["fam"]["past_due"]["name"], "D search narrows to one account",
              (ok, name, p.eval("document.querySelectorAll('#rows .ac-row').length")))
        p.eval("(function(){var q=document.getElementById('q');q.value='advdrive-locked@mrbadmus-test.com';"
               "q.dispatchEvent(new Event('input'));})()")
        ok = wait_for(p, "document.querySelectorAll('#rows .ac-row').length === 1 && "
                         "document.querySelector('#rows .ac-name').textContent.indexOf('Locked') >= 0",
                      tries=50, gap=0.5)
        check(ok, "D search also matches on email",
              p.eval("(document.querySelector('#rows .ac-name')||{}).textContent"))
        p.eval("(function(){var q=document.getElementById('q');q.value='';"
               "q.dispatchEvent(new Event('input'));})()")
        wait_for(p, "document.querySelectorAll('#rows .ac-row').length > 1")

        # ── screenshot, desktop — taken BEFORE any support action, so the
        #    list still shows all five billing states side by side ──
        p.screenshot(os.path.join(shots, "admin-accounts-desktop.png"), width=1440, height=1000)
        print("  shot → admin-accounts-desktop.png")

        # ── detail: the trialing family ──
        def open_detail(org):
            p.eval("document.querySelector('#rows .ac-row[data-id=\"%s\"]').click()" % org)
            return wait_for(p, "document.querySelectorAll('#detail-view .ac-act').length > 0")

        tf = ids["fam"]["trialing"]
        check(open_detail(tf["org"]), "D detail opens for the trial family")
        dis = p.eval("(function(){var o={};Array.prototype.forEach.call("
                     "document.querySelectorAll('.ac-act button'),function(b){o[b.textContent.trim()]=b.disabled;});return o;})()")
        check(dis.get("Extend trial 7 days") is False and dis.get("Unlock for 14 days") is True,
              "D trialing: Extend enabled, Unlock disabled", dis)

        st, before = sb_admin("GET", "/rest/v1/subscriptions?select=trial_end,status,comped_until&org_id=eq." + tf["org"])
        check(click_text(p, ".ac-act button", "Extend trial") == "clicked", "D click Extend trial 7 days")
        ok = wait_for(p, "/Extended to/.test(document.body.innerText)", tries=25, gap=0.4)
        check(ok, "D extend trial: success message shown", last_msg(p))
        st, after = sb_admin("GET", "/rest/v1/subscriptions?select=trial_end,status,comped_until&org_id=eq." + tf["org"])
        moved = (after[0]["comped_until"] or "") > (before[0]["trial_end"] or "")
        check(moved, "D extend trial: the account's end date actually moved forward in the DB",
              (before[0], after[0]))

        # ── reset password, on a family with TWO children ──
        nkids = p.eval("document.querySelectorAll('.kid-pwd-btn').length")
        check(nkids == 2, "D trial family shows both children", nkids)
        for i in range(nkids):
            p.eval("document.querySelectorAll('.kid-pwd-btn')[%d].click()" % i)
            ok = wait_for(p, "document.querySelectorAll('.ac-pwd').length === %d" % (i + 1), tries=25, gap=0.4)
            check(ok, "D reset password on child %d shows a password once" % (i + 1),
                  p.eval("(document.querySelectorAll('.ac-pwd')[%d]||{}).textContent" % i))
        pwds = p.eval("Array.prototype.map.call(document.querySelectorAll('.ac-pwd'),function(e){return e.textContent;})")
        check(len(pwds) == 2 and pwds[0] != pwds[1] and all(len(x or "") > 6 for x in pwds),
              "D two children each get their own password, neither button broke the other", pwds)

        # ── resend verification ──
        check(click_text(p, ".ac-act button", "Resend verification") == "clicked", "D click Resend verification")
        ok = wait_for(p, "/already confirmed|Sent\\./.test(document.body.innerText)", tries=25, gap=0.4)
        check(ok, "D resend verification: a sensible message either way", last_msg(p))

        # ── goodwill marks ──
        check(click_text(p, ".ac-act button", "Add 2 human marks") == "clicked", "D click Add 2 human marks")
        ok = wait_for(p, "/monthly Mr Badmus cap is now/.test(document.body.innerText)", tries=25, gap=0.4)
        check(ok, "D human marks: success text", last_msg(p))

        # ── the other billing states' button enablement ──
        p.eval("document.getElementById('back-btn').click()")
        wait_for(p, "document.querySelectorAll('#rows .ac-row').length > 1")
        for state in ("active", "past_due", "cancelled"):
            org = ids["fam"][state]["org"]
            check(open_detail(org), "D detail opens for the %s family" % state)
            dis = p.eval("(function(){var o={};Array.prototype.forEach.call("
                         "document.querySelectorAll('.ac-act button'),function(b){o[b.textContent.trim()]=b.disabled;});return o;})()")
            check(dis.get("Extend trial 7 days") is True and dis.get("Unlock for 14 days") is True,
                  "D %s: both Extend and Unlock are disabled" % state, dis)
            p.eval("document.getElementById('back-btn').click()")
            wait_for(p, "document.querySelectorAll('#rows .ac-row').length > 1")

        # ── unlock the locked family ──
        lf = ids["fam"]["locked"]
        check(open_detail(lf["org"]), "D detail opens for the locked family")
        dis = p.eval("(function(){var o={};Array.prototype.forEach.call("
                     "document.querySelectorAll('.ac-act button'),function(b){o[b.textContent.trim()]=b.disabled;});return o;})()")
        check(dis.get("Unlock for 14 days") is False and dis.get("Extend trial 7 days") is True,
              "D locked: Unlock enabled, Extend disabled", dis)
        check(click_text(p, ".ac-act button", "Unlock for 14 days") == "clicked", "D click Unlock for 14 days")
        ok = wait_for(p, "/Unlocked until/.test(document.body.innerText)", tries=25, gap=0.4)
        check(ok, "D unlock: success message", last_msg(p))
        st, sub = sb_admin("GET", "/rest/v1/subscriptions?select=status,comped_until&org_id=eq." + lf["org"])
        check(sub[0]["status"] == "comped" and sub[0]["comped_until"] > iso(0),
              "D unlock: the DB row is comped into the future", sub[0])
        p.eval("document.getElementById('back-btn').click()")
        wait_for(p, "document.querySelectorAll('#rows .ac-row').length > 1")

        # ── the New organisation form ──
        new_name = "Formmade Centre %s" % TAG
        p.eval("document.getElementById('new-org-btn').click()")
        wait_for(p, "!document.getElementById('org-veil').hidden")
        p.eval("""(function(){
          document.getElementById('org-name').value = %s;
          document.getElementById('org-seats').value = '40';
          document.getElementById('org-period-end').value = '2027-08-31';
          document.getElementById('org-contact-name').value = 'Ada Contact';
          document.getElementById('org-contact-email').value = 'advdrive-form@mrbadmus-test.com';
          document.getElementById('org-submit').click();
        })()""" % json.dumps(new_name))
        ok = wait_for(p, "/Created /.test((document.getElementById('org-msg')||{}).textContent||'')",
                      tries=30, gap=0.4)
        check(ok, "D new organisation: form reports success",
              p.eval("(document.getElementById('org-msg')||{}).textContent"))
        time.sleep(2.0)   # the modal closes itself 1.6s after a successful create
        p.eval("document.querySelector('[data-filter=\"orgs\"]').click()")
        has_row = ("Array.prototype.some.call(document.querySelectorAll('#rows .ac-row'),"
                   "function(x){return x.textContent.indexOf(%s)>=0;})" % json.dumps(new_name))
        ok = wait_for(p, has_row, tries=50, gap=0.5)
        check(ok, "D new organisation appears in the list",
              p.eval("document.querySelectorAll('#rows .ac-row').length"))
        check(p.eval("document.getElementById('org-veil').hidden") is True,
              "D the New-organisation modal closes itself after a successful create")
        row = p.eval("(function(){var r=Array.prototype.filter.call(document.querySelectorAll('#rows .ac-row'),"
                     "function(x){return x.textContent.indexOf(%s)>=0;})[0];return r?r.textContent:'';})()"
                     % json.dumps(new_name))
        check("Invoiced" in row, "D new organisation row reads Invoiced", row)
        p.eval("(function(){var r=Array.prototype.filter.call(document.querySelectorAll('#rows .ac-row'),"
               "function(x){return x.textContent.indexOf(%s)>=0;})[0]; if(r) r.click();})()" % json.dumps(new_name))
        wait_for(p, "document.querySelectorAll('#detail-view .ac-kv').length > 0", tries=50, gap=0.5)
        seats = p.eval("(function(){var out='';Array.prototype.forEach.call(document.querySelectorAll('.ac-kv'),"
                       "function(k){if(k.textContent.indexOf('Seats')>=0) out=k.textContent;});return out;})()")
        check("40" in (seats or ""), "D new organisation detail shows the seat cap it was given", seats)
        p.eval("document.getElementById('back-btn').click()")

        # ── the seat-cap organisation fixture ──
        p.eval("document.querySelector('[data-filter=\"orgs\"]').click()")
        wait_for(p, "document.querySelectorAll('#rows .ac-row').length >= 2")
        p.eval("document.querySelector('#rows .ac-row[data-id=\"%s\"]').click()" % ids["org_seatcap"])
        wait_for(p, "document.querySelectorAll('#detail-view .ac-kv').length > 0")
        seats = p.eval("(function(){var out='';Array.prototype.forEach.call(document.querySelectorAll('.ac-kv'),"
                       "function(k){if(k.textContent.indexOf('Seats')>=0) out=k.textContent;});return out;})()")
        cyc = p.eval("(function(){var out='';Array.prototype.forEach.call(document.querySelectorAll('.ac-kv'),"
                     "function(k){if(k.textContent.indexOf('Cycle')>=0) out=k.textContent;});return out;})()")
        check("/ 2" in (seats or ""), "D seat-cap org detail shows seats used / cap", seats)
        check("cap 2 seats" in (cyc or ""), "D seat-cap org cycle reads the cap", cyc)
        p.eval("document.getElementById('back-btn').click()")
        wait_for(p, "document.querySelectorAll('#rows .ac-row').length > 0")

        # ── 390px ──
        p.eval("document.querySelector('[data-filter=\"all\"]').click()")
        wait_for(p, "document.querySelectorAll('#rows .ac-row').length > 3")
        p.set_viewport(390, 800, settle=0.4)
        over = p.eval("[document.documentElement.scrollWidth, document.documentElement.clientWidth, "
                      "Math.max.apply(null, Array.prototype.map.call(document.querySelectorAll('body *'),"
                      "function(e){return Math.ceil(e.getBoundingClientRect().right);}))]")
        check(over[0] <= over[1] + 1, "D 390px: no horizontal page overflow", over)
        check(over[2] <= 392, "D 390px: nothing sticks out past the viewport", over)
        rows_ok = p.eval("(function(){var r=document.querySelector('.ac-row');"
                         "return r ? getComputedStyle(r).gridTemplateColumns.split(' ').length : 0;})()")
        check(rows_ok == 1, "D 390px: the list is the single-column stacked layout", rows_ok)
        check(not errs(p), "D accounts: still no console errors at the end", errs(p))


# ══════════════════════════════════════════════════════════════════════════
# E — operator · admin-queue.html
# ══════════════════════════════════════════════════════════════════════════
def phase_e(ids, shots):
    print("\n── E · operator · admin-queue ────────────────────────────")
    op = sign_in(*OPERATOR)
    jwt = op["access_token"]
    st, q = api("GET", "/api/consumer/admin/mb-queue", jwt)
    check(st == 200 and len(q["pending"]) == 3, "E GET /admin/mb-queue → the three fixtures", st)
    by_age = {}
    for it in q["pending"]:
        hrs = round((time.time() - time.mktime(time.strptime(it["sent_at"][:19], "%Y-%m-%dT%H:%M:%S"))
                     - time.timezone) / 3600)
        by_age[hrs] = it["id"]
    old_id = by_age[max(by_age)]      # ~70h
    mid_id = sorted(by_age.items())[1][1]   # ~26h (the levels-marked one)
    new_id = by_age[min(by_age)]      # ~6h
    print("  ages", sorted(by_age))

    with cdp.Browser() as b:
        p = b.attach()
        p.send("Page.addScriptToEvaluateOnNewDocument", {"source": FLAG_ON_JS})
        with_session(p, op)
        p.goto(qs("/consumer/admin-queue.html"), settle=1.2)
        ok = wait_for(p, "document.querySelectorAll('.ad-item').length === 3")
        check(ok, "E queue: the sidebar lists all three", text(p)[:160].replace("\n", " "))
        check(p.eval("(function(){var m=document.getElementById('c-main');"
                     "return m ? getComputedStyle(m).display : 'missing';})()") != "none",
              "E queue: the console is actually visible (#c-main not display:none)")
        check(not errs(p), "E queue: no console errors", errs(p))

        order = lambda: p.eval("Array.prototype.map.call(document.querySelectorAll('.ad-item'),"
                               "function(e){return e.getAttribute('data-id');})")
        check(order() == [old_id, mid_id, new_id], "E sort 'oldest' puts the 70h item first", order())
        foot = p.eval("document.getElementById('list-foot').textContent")
        check("Oldest: 2d" in (foot or ""), "E the footer reports the OLDEST item's age", foot)
        p.eval("document.querySelector('[data-sort=\"newest\"]').click()")
        time.sleep(0.4)
        check(order() == [new_id, mid_id, old_id], "E sort 'newest' reverses it", order())
        p.eval("document.querySelector('[data-sort=\"org\"]').click()")
        time.sleep(0.4)
        check(order() == [old_id, mid_id, new_id],
              "E sort 'organisations' — no orgs queued, so oldest-first within the family group", order())
        p.eval("document.querySelector('[data-sort=\"oldest\"]').click()")
        time.sleep(0.4)

        # ── the 48h line ──
        colours = p.eval("Array.prototype.map.call(document.querySelectorAll('.ad-item'),function(e){"
                         "var s=e.querySelector('.row1 span:last-child');"
                         "return [e.getAttribute('data-id'), getComputedStyle(s).color, s.textContent,"
                         " getComputedStyle(e).borderLeftColor];})")
        ember = p.eval("getComputedStyle(document.querySelector('.ad-room')).getPropertyValue('--st-ember').trim()")
        cmap = dict((c[0], c) for c in colours)
        check(cmap[old_id][1] == "rgb(244, 184, 96)",
              "E the >48h item's age text is ember", cmap[old_id][:3])
        check(cmap[new_id][1] != "rgb(244, 184, 96)" and cmap[mid_id][1] != "rgb(244, 184, 96)",
              "E the <48h items' age text is not ember", [cmap[new_id][1], cmap[mid_id][1]])
        check(cmap[old_id][2].startswith("2d"), "E the >48h age label reads in days", cmap[old_id][2])
        # the oldest is the CURRENT item, so its accent is ember by selection;
        # select another and the >48h accent must still be the warm accent.
        p.eval("document.querySelector('.ad-item[data-id=\"%s\"]').click()" % new_id)
        time.sleep(0.5)
        accents = p.eval("(function(){var o={};Array.prototype.forEach.call(document.querySelectorAll('.ad-item'),"
                         "function(e){o[e.getAttribute('data-id')]=getComputedStyle(e).borderLeftColor;});return o;})()")
        check(accents[old_id] not in ("rgba(0, 0, 0, 0)", "transparent"),
              "E the >48h item keeps a coloured left accent when not selected", accents[old_id])
        check(accents[mid_id] in ("rgba(0, 0, 0, 0)", "transparent"),
              "E a <48h unselected item has no accent", accents[mid_id])

        # ── checklist mode ──
        p.eval("document.querySelector('.ad-item[data-id=\"%s\"]').click()" % old_id)
        ok = wait_for(p, "document.querySelectorAll('.ad-point').length === 3")
        check(ok, "E scheme checklist renders three points from question.scheme",
              p.eval("document.querySelectorAll('.ad-point').length"))
        check("[object Object]" not in text(p), "E scheme points are text, not [object Object]")
        # the fixture's instant mark is ai_score 2, ai_hits [0, 2] — points 1
        # and 3 awarded, point 2 missed.
        ticks = p.eval("Array.prototype.map.call(document.querySelectorAll('.ad-point'),"
                       "function(e){return e.classList.contains('is-on');})")
        check(ticks == [True, False, True],
              "E the instant mark's ticks land on the points it actually awarded (ai_hits is an INDEX list)", ticks)
        score0 = p.eval("document.querySelector('.ad-score').textContent")
        label0 = p.eval("document.getElementById('send-btn').textContent")
        check(score0 == "2/3" and "2/3" in label0,
              "E score readout starts from the instant mark (2/3)", (score0, label0))
        check(p.eval("document.querySelectorAll('.ad-diff').length") == 0,
              "E no point is flagged as a divergence before the operator touches anything",
              p.eval("(document.querySelector('.ad-diff')||{}).textContent"))
        p.eval("document.querySelectorAll('.ad-point')[1].click()")
        time.sleep(0.4)
        s1 = p.eval("document.querySelector('.ad-score').textContent")
        l1 = p.eval("document.getElementById('send-btn').textContent")
        check(s1 == "3/3" and "3/3" in l1, "E toggling a point moves score AND button label together", (s1, l1))
        p.eval("document.querySelectorAll('.ad-point')[0].click()")
        time.sleep(0.4)
        s2 = p.eval("document.querySelector('.ad-score').textContent")
        l2 = p.eval("document.getElementById('send-btn').textContent")
        check(s2 == "2/3" and "2/3" in l2, "E a second toggle too", (s2, l2))
        p.eval("document.querySelectorAll('.ad-point')[0].click()")
        time.sleep(0.3)

        # ── the note gate ──
        setnote = ("(function(t){var n=document.getElementById('note');n.value=t;"
                   "n.dispatchEvent(new Event('input'));return document.getElementById('send-btn').disabled;})(%s)")
        check(p.eval(setnote % json.dumps("short")) is True, "E note < 10 chars → Send disabled")
        check(p.eval(setnote % json.dumps("Good start — now name the ions.")) is False,
              "E note >= 10 chars → Send enabled")
        check(p.eval(setnote % json.dumps("")) is True, "E emptying the note disables Send again")

        # ── levels-marked question: the numeric fallback ──
        p.eval("document.querySelector('.ad-item[data-id=\"%s\"]').click()" % mid_id)
        ok = wait_for(p, "!!document.getElementById('num-score')")
        check(ok, "E a question with no scheme falls back to a numeric input")
        check(p.eval("document.querySelectorAll('.ad-point').length") == 0,
              "E and draws no fabricated checklist")

        # ── 390px: sidebar out, dropdown in ──
        p.set_viewport(390, 820, settle=0.5)
        check(p.eval("getComputedStyle(document.getElementById('sidebar')).display") == "none",
              "E 390px: the sidebar is hidden")
        check(p.eval("getComputedStyle(document.getElementById('mlist-wrap')).display") != "none",
              "E 390px: the mobile picker is shown")
        over = p.eval("[document.documentElement.scrollWidth, document.documentElement.clientWidth]")
        check(over[0] <= over[1] + 1, "E 390px: no horizontal page overflow", over)

        # pick a DIFFERENT queued item through the <select>
        p.eval("(function(){var s=document.getElementById('mobile-pick');s.value='%s';"
               "s.dispatchEvent(new Event('change'));})()" % mid_id)
        ok = wait_for(p, "!!document.getElementById('num-score')")
        check(ok, "E 390px: the mobile <select> switches the marking pane")
        p.eval("(function(){var n=document.getElementById('num-score');n.value='5';"
               "n.dispatchEvent(new Event('input'));})()")
        time.sleep(0.3)
        check(p.eval("document.querySelector('.ad-score').textContent") == "5/6",
              "E 390px: typing a score updates the readout")
        note = "Well sequenced — now say WHY the gas particles spread out."
        p.eval(setnote % json.dumps(note))
        p.screenshot(os.path.join(shots, "admin-queue-mobile-390.png"), width=390, height=820)
        print("  shot → admin-queue-mobile-390.png")

        check(p.eval("document.getElementById('send-btn').disabled") is False, "E 390px: Send is enabled")
        p.eval("document.getElementById('send-btn').click()")
        ok = wait_for(p, "document.querySelectorAll('.ad-item').length === 2 "
                         "|| /didn/.test((document.getElementById('send-msg')||{}).textContent||'')",
                      tries=30, gap=0.4)
        sendmsg = p.eval("(document.getElementById('send-msg')||{}).textContent")
        check(p.eval("document.querySelectorAll('.ad-item').length") == 2,
              "E 390px: the marked item leaves the queue", sendmsg)
        cur = p.eval("(function(){var s=document.getElementById('mobile-pick');return s.value;})()")
        check(cur in (old_id, new_id), "E 390px: the pane advances to another queued item", cur)
        check(not errs(p), "E queue: no console errors after sending", errs(p))

        # ── what actually landed in the database ──
        st, row = sb_admin("GET", "/rest/v1/exam_answers?select=id,status,mb_score,mb_feedback,mb_marked_by,child_id"
                                  "&id=eq." + mid_id)
        r = row[0]
        check(r["status"] == "mb_marked" and r["mb_feedback"] == note,
              "E the answer is mb_marked with the operator's own words", r)
        check(r["mb_score"] == 5,
              "E the score SENT is the score the operator typed (not the instant mark)", r["mb_score"])
        st, notifs = sb_admin("GET", "/rest/v1/consumer_notifications?select=recipient_id,kind,title"
                                     "&org_id=eq." + ids["fam"]["trialing"]["org"] + "&kind=eq.mb_marked")
        rec = set(n["recipient_id"] for n in (notifs or []))
        check(r["child_id"] in rec, "E the child was notified", len(notifs or []))
        check(ids["fam"]["trialing"]["parent"] in rec, "E the parent was notified too", sorted(rec))
        st, mails = sb_admin("GET", "/rest/v1/email_log?select=type,status,recipient_id&org_id=eq."
                             + ids["fam"]["trialing"]["org"] + "&type=eq.mb_marked")
        check(bool(mails), "E an E4 mb_marked email was logged for the parent", mails)


# ══════════════════════════════════════════════════════════════════════════
def main():
    global BASE, API
    ap = argparse.ArgumentParser()
    ap.add_argument("--site", default="mrbadmus_site")
    ap.add_argument("--api", default="http://localhost:3131")
    ap.add_argument("--port", type=int, default=8131)
    ap.add_argument("--shots", default=SCRATCH)
    ap.add_argument("--phases", default="ABCDE")
    ap.add_argument("--keep", action="store_true", help="leave fixtures in place")
    ap.add_argument("--reuse", action="store_true", help="reuse the fixtures from the state file")
    ap.add_argument("--teardown-only", action="store_true")
    a = ap.parse_args()
    API = a.api
    os.makedirs(a.shots, exist_ok=True)

    if a.teardown_only:
        teardown(json.load(open(STATE_FILE)))
        return 0

    server, port = cdp.serve(os.path.abspath(a.site), a.port)
    BASE = "http://localhost:%d" % port
    print("serving built tree at", BASE, "· backend", API)

    ids = None
    try:
        if "A" in a.phases:
            phase_a()
        if "B" in a.phases:
            phase_b()
        if "C" in a.phases:
            phase_c()
        if "D" in a.phases or "E" in a.phases:
            ids = json.load(open(STATE_FILE)) if a.reuse else setup()
            if "D" in a.phases:
                phase_d(ids, a.shots)
            if "E" in a.phases:
                phase_e(ids, a.shots)
    finally:
        if ids and not a.keep:
            teardown(ids)
        server.shutdown()

    print("\n%d failure(s)" % len(FAILS))
    for f in FAILS:
        print("  - " + f)
    return min(len(FAILS), 99)


if __name__ == "__main__":
    sys.exit(main())
