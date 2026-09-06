#!/usr/bin/env python3
"""mrb327_safari_drive.py — fixtures + teardown for the MRB-327 SAFARI lane (§2).

The browser work itself is mrb327_safari_drive.js (Playwright: WebKit + Chromium).
This script only makes the family the drive needs, and deletes it afterwards.

    python3 mrb327_safari_drive.py setup     # writes the state file
    python3 mrb327_safari_drive.py teardown  # deletes everything in it

Fixture helpers are lifted from admin_ui_drive.py so the teardown order (which is
load-bearing: profiles FK onto auth.users with no cascade) is the proven one.
"""
import json, os, ssl, sys, time, urllib.request, urllib.error

SB = "https://qeppkiswvclkkwbxmlok.supabase.co"
API = os.environ.get("MRB_API", "http://localhost:3100")
CTX = ssl.create_default_context(cafile="/etc/ssl/cert.pem")
SCRATCH = ("/private/tmp/claude-501/-Users-midebadmus-Documents-GitHub-mrbadmus-worktrees-"
           "b2c-launch/06d799b1-12f9-481b-9871-424a2321715f/scratchpad")
STATE_FILE = os.path.join(SCRATCH, "safari_fixtures.json")

TAG = "sfdrive"
PW = "Passw0rd!safaridrive"
PARENT_EMAIL = "sfdrive-parent@mrbadmus-test.com"
CHILD_PW = "comet-saturn-42"


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
    ids = {"users": [], "orgs": []}
    print("── fixtures ──────────────────────────────────────────")

    st, d = sb_admin("POST", "/auth/v1/admin/users",
                     {"email": PARENT_EMAIL, "password": PW, "email_confirm": True,
                      "user_metadata": {"first_name": "Safari"}})
    if st >= 300:
        st2, users = sb_admin("GET", "/auth/v1/admin/users?per_page=500")
        d = next(u for u in users["users"] if u["email"] == PARENT_EMAIL)
    parent = d["id"]
    ids["users"].append(parent)
    ids["parent"] = parent
    ids["parent_email"] = PARENT_EMAIL
    ids["parent_password"] = PW

    sess = sign_in(PARENT_EMAIL, PW)
    jwt = sess["access_token"]
    ids["parent_session"] = sess

    st, fam = api("POST", "/api/consumer/family/ensure", jwt,
                  {"family_name": "Safari family %s" % TAG})
    assert st == 200, (st, fam)
    org = fam["org_id"]
    ids["orgs"].append(org)
    ids["org"] = org

    username = "sf%d" % (int(time.time()) % 1000000)
    st, c = api("POST", "/api/consumer/children", jwt, {
        "first_name": "Amara", "year_group": 8, "username": username,
        "password": CHILD_PW, "mode": "alongside_school",
        "intensity": "light", "exam_board": "AQA"})
    assert st == 200, (st, c)
    child = c["child_id"]
    ids["users"].append(child)
    ids["child"] = child
    ids["child_username"] = username
    ids["child_password"] = CHILD_PW

    # Trialing: the state checkout-return.html treats as SETTLED, and the state
    # guard() lets the child surfaces through on.
    set_sub(org, {"status": "trialing", "trial_end": iso(6 * 86400), "quantity": 1})

    # A week of work, through the real generator, so today.html has something.
    st, g = api("POST", "/api/consumer/children/%s/generate" % child, jwt, {})
    print("  generate:", st, (json.dumps(g)[:200] if g else ""))

    st, ch = api("POST", "/api/consumer/child/login", None,
                 {"username": username, "password": CHILD_PW})
    assert st == 200, (st, ch)
    ids["child_session"] = ch

    print("  parent %s  org %s" % (parent, org))
    print("  child  %s  username %s" % (child, username))
    json.dump(ids, open(STATE_FILE, "w"), indent=1)
    print("  state → " + STATE_FILE)
    return ids


def teardown(ids=None):
    if ids is None:
        if not os.path.exists(STATE_FILE):
            print("no state file — nothing to tear down")
            return
        ids = json.load(open(STATE_FILE))
    print("── cleanup ───────────────────────────────────────────")
    for org in ids.get("orgs", []):
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
                  "unit_check_attempts", "work_items", "work_generation_runs",
                  "child_plans", "family_messages", "consumer_notifications",
                  "org_limits", "account_deletion_requests"):
            sb_admin("DELETE", "/rest/v1/%s?org_id=eq.%s" % (t, org))
        for t in ("pending_staff", "staff_scopes"):
            sb_admin("DELETE", "/rest/v1/%s?school_id=eq.%s" % (t, org))
        sb_admin("DELETE", "/rest/v1/audit_log?school_id=eq." + org)
        sb_admin("DELETE", "/rest/v1/subscriptions?org_id=eq." + org)
        # ⚠️ `family/ensure` creates an ACADEMIC YEAR as well as a class, and
        # academic_years.school_id is an FK on schools. admin_ui_drive.py's
        # teardown — which this one is copied from — deletes the class and not
        # the year, so the final `DELETE /schools` comes back 409 and the org
        # row survives as residue. Delete the year before the school.
        sb_admin("DELETE", "/rest/v1/academic_years?school_id=eq." + org)
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
        sb_admin("DELETE", "/rest/v1/profiles?id=eq." + u)
        st2, r2 = sb_admin("DELETE", "/auth/v1/admin/users/" + u)
        print("  user %s deleted (%s)" % (u, st2))
    for org in ids.get("orgs", []):
        st, r = sb_admin("DELETE", "/rest/v1/schools?id=eq." + org)
        print("  org  %s deleted (%s)" % (org, st))
    print("  done")


def verify_gone(ids=None):
    if ids is None:
        ids = json.load(open(STATE_FILE))
    print("── residue check ─────────────────────────────────────")
    for u in ids.get("users", []):
        st, d = sb_admin("GET", "/auth/v1/admin/users/" + u)
        st2, p = sb_admin("GET", "/rest/v1/profiles?select=id&id=eq." + u)
        print("  user %s  auth=%s  profiles=%s" % (u, st, (p if p else [])))
    for org in ids.get("orgs", []):
        st, s = sb_admin("GET", "/rest/v1/schools?select=id&id=eq." + org)
        st2, sub = sb_admin("GET", "/rest/v1/subscriptions?select=org_id&org_id=eq." + org)
        print("  org  %s  schools=%s  subscriptions=%s" % (org, s, sub))


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "setup"
    if cmd == "setup":
        setup()
    elif cmd == "teardown":
        teardown()
    elif cmd == "verify":
        verify_gone()
