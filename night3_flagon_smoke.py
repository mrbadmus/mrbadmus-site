#!/usr/bin/env python3
"""night3_flagon_smoke.py — the commander's flag-ON pass over the BUILT tree.

    EXTRA_CORS_ORIGINS=http://localhost:8121 CONSUMER_SIGNUP_ENABLED=true PORT=3121 node server.js   (backend worktree)
    python3 night3_flagon_smoke.py --api http://localhost:3121 --port 8121

The four lanes drove their own pages from the repo root. This drives the BUILT
mrbadmus_site/ — cache-bust stamps and all — with real sessions, one pass per
surface, and it is the only place the cancel-at-period-end branch (full access,
Design's original wording) has ever been rendered, because `billingFor` learned
that state after the dashboard lane finished.

The built config has the flag OFF (as it must). The flag is turned on for THIS
browser only, by a setter installed before any page script runs: config.js does
`window.MrBadmusConfig = config`, the setter flips CONSUMER_SIGNUP_ENABLED on the
object as it is assigned. Nothing on disk changes.

Fixtures are created through the real API and removed at the end.
"""
import argparse, json, os, re, ssl, sys, time, urllib.request, urllib.error

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ks3_browser as cdp

SB = "https://qeppkiswvclkkwbxmlok.supabase.co"
CTX = ssl.create_default_context(cafile="/etc/ssl/cert.pem")
FAILS = []
def check(ok, label, evidence=""):
    print(("  ✓ " if ok else "  ✗ ") + label + (("  — " + str(evidence)[:400]) if evidence else ""))
    if not ok: FAILS.append(label)

def env(name):
    for line in open("/Users/midebadmus/Documents/GitHub/mrbadmus-worktrees/b2c/backend/.env"):
        if line.startswith(name + "="): return line.split("=", 1)[1].strip()
    return None
SERVICE = env("SUPABASE_SERVICE_ROLE_KEY"); ANON = env("SUPABASE_ANON_KEY")

def http(method, url, body=None, headers=None, timeout=60):
    data = json.dumps(body).encode() if body is not None else None
    h = {"Content-Type": "application/json"}; h.update(headers or {})
    req = urllib.request.Request(url, data=data, method=method, headers=h)
    try:
        with urllib.request.urlopen(req, context=CTX, timeout=timeout) as r:
            t = r.read().decode(); return r.status, (json.loads(t) if t else None)
    except urllib.error.HTTPError as e:
        t = e.read().decode()
        try: return e.code, json.loads(t)
        except Exception: return e.code, t

def sb_admin(method, path, body=None):
    return http(method, SB + path, body, {"apikey": SERVICE, "Authorization": "Bearer " + SERVICE, "Prefer": "return=representation"})

def sign_in(email, pw):
    st, d = http("POST", SB + "/auth/v1/token?grant_type=password", {"email": email, "password": pw}, {"apikey": ANON})
    assert st == 200, (st, d); return d

def api(base, method, path, jwt=None, body=None):
    h = {"Authorization": "Bearer " + jwt} if jwt else {}
    return http(method, base + path, body, h)

FLAG_ON_JS = """(function(){var c=null;Object.defineProperty(window,'MrBadmusConfig',{configurable:true,
  get:function(){return c;}, set:function(v){ if(v&&typeof v==='object'){v.CONSUMER_SIGNUP_ENABLED=true;} c=v; }});})();"""

def with_session(p, sess):
    p.goto(BASE + "/404.html?env=test", settle=0.2)
    p.eval("localStorage.setItem('sb-qeppkiswvclkkwbxmlok-auth-token', %s)" % json.dumps(json.dumps(sess)))

def visit(p, path, label, shots, shot=None, expect=None, width=390):
    p.goto(BASE + path + ("&" if "?" in path else "?") + "env=test&api=" + API, settle=1.0)
    # GET /family can take 5–10 s on TEST (an open item): wait for the page to
    # settle rather than read it at a fixed instant.
    text, prev = "", None
    for _ in range(30):
        text = p.eval("document.body ? document.body.innerText : ''") or ""
        loading = ("Loading" in text) or (len(text.strip()) < 40)
        if not loading and text == prev:
            break
        prev = text; time.sleep(1.0)
    errs = [e for e in p.console_errors() if "favicon.ico" not in e]
    check(not errs, "%s: zero console errors" % label, errs)
    check("Not found" not in text[:200], "%s: rendered (not the off page)" % label, text[:100].replace("\n", " "))
    norm = lambda t: t.lower().replace("’", "'")
    for e in (expect or []):
        check(norm(e) in norm(text), "%s: shows “%s”" % (label, e), text[:600].replace("\n", " ") if norm(e) not in norm(text) else "")
    if shot: p.screenshot(os.path.join(shots, shot), width=width)
    return text

def main():
    global BASE, API
    ap = argparse.ArgumentParser()
    ap.add_argument("--site", default="mrbadmus_site"); ap.add_argument("--api", default="http://localhost:3121")
    ap.add_argument("--port", type=int, default=8121)
    ap.add_argument("--shots", default="docs/b2c/night3-screens")
    a = ap.parse_args(); API = a.api
    os.makedirs(a.shots, exist_ok=True)
    server, port = cdp.serve(os.path.abspath(a.site), a.port); BASE = "http://localhost:%d" % port
    print("serving built tree at", BASE, "backend", API)
    ids = {"users": [], "org": None}
    try:
        # ── fixtures through the real API ────────────────────────────────
        email = "n3-cmd-parent@mrbadmus-test.com"; pw = "Passw0rd!night3"
        st, d = sb_admin("POST", "/auth/v1/admin/users", {"email": email, "password": pw, "email_confirm": True, "user_metadata": {"first_name": "Funmi"}})
        if st == 422 or (isinstance(d, dict) and d.get("code") == 422):
            # left over from an interrupted run: find and reuse
            st2, users = sb_admin("GET", "/auth/v1/admin/users?per_page=200")
            d = next(u for u in users["users"] if u["email"] == email)
        uid = d["id"]; ids["users"].append(uid)
        sess = sign_in(email, pw); jwt = sess["access_token"]
        st, fam = api(API, "POST", "/api/consumer/family/ensure", jwt, {"family_name": "Commander family"})
        check(st == 200 and fam.get("ok"), "family/ensure", (st, fam)); org = fam["org_id"]; ids["org"] = org
        kids = []
        for name, yg, mode, inten, user in (("Amara", 9, "alongside_school", "light", "cmdamara%d" % (int(time.time()) % 10000)),
                                             ("Leo", 7, "home_education", "full", "cmdleo%d" % (int(time.time()) % 10000))):
            st, c = api(API, "POST", "/api/consumer/children", jwt, {"first_name": name, "year_group": yg, "username": user, "password": "comet-saturn-42", "mode": mode, "intensity": inten, "exam_board": "AQA"})
            check(st == 200, "create child %s" % name, (st, c)); kids.append({"id": c["child_id"], "username": c["username"], "name": name}); ids["users"].append(c["child_id"])
        # trialing, then generate a week
        monday = time.strftime("%Y-%m-%d", time.localtime(time.time() - ((time.localtime().tm_wday) * 86400)))
        sb_admin("PATCH", "/rest/v1/subscriptions?org_id=eq." + org, {"status": "trialing", "trial_end": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(time.time() + 6 * 86400)), "quantity": 2})
        time.sleep(16)  # access cache
        for k in kids:
            st, g = api(API, "POST", "/api/consumer/children/%s/generate" % k["id"], jwt, {"week_start": monday})
            check(st == 200, "generate week for %s" % k["name"], (st, g))
        # child login through the backend
        st, cl = api(API, "POST", "/api/consumer/child/login", None, {"username": kids[0]["username"], "password": "comet-saturn-42"})
        check(st == 200, "child login", (st, cl))
        st, bad1 = api(API, "POST", "/api/consumer/child/login", None, {"username": "nosuchchildxyz", "password": "x"})
        st2, bad2 = api(API, "POST", "/api/consumer/child/login", None, {"username": kids[0]["username"], "password": "wrong-pass"})
        check(st == 401 and st2 == 401 and bad1 == bad2, "child login: unknown username and wrong password are one identical 401", (st, bad1, st2, bad2))
        child_sess = {"access_token": cl["access_token"], "refresh_token": cl["refresh_token"], "expires_in": cl.get("expires_in", 3600), "expires_at": int(time.time()) + 3600, "token_type": "bearer", "user": {"id": cl["user"]["id"]}}

        with cdp.Browser() as b:
            p = b.attach()
            p.send("Page.addScriptToEvaluateOnNewDocument", {"source": FLAG_ON_JS})
            # public pages, flag on
            visit(p, "/parents/index.html", "public home (flag on)", a.shots, expect=["Start a free week"])
            visit(p, "/parents/pricing.html", "public pricing (flag on)", a.shots, expect=["£9.99"])
            # parent journey
            with_session(p, sess)
            visit(p, "/consumer/overview.html", "dashboard trialing", a.shots, "built-dash-trialing.png", expect=["Free week", "Amara", "Leo"])
            visit(p, "/consumer/overview.html?child=%s&view=child" % kids[0]["id"], "child detail", a.shots, expect=["Amara"])
            visit(p, "/consumer/account.html", "account trialing", a.shots, expect=["Free week"])
            visit(p, "/consumer/report.html?child=%s" % kids[0]["id"], "report", a.shots, expect=["Science progress report"])
            # cancel at period end — the branch nobody has rendered
            # ⊕ MRB-321. `stripe_customer_id` is set HERE and not before, because
            # without it `billingFor` returns can_portal=false and the account
            # page correctly renders "There is no billing account to manage yet"
            # instead of Design's "Resume subscription" CTA — a fixture that had
            # cancelled a subscription which never went through Stripe, which
            # cannot happen in production. The assertion below was right; the
            # fixture was not. The id is synthetic: can_portal only tests for
            # presence, and nothing in this pass presses the button.
            sb_admin("PATCH", "/rest/v1/subscriptions?org_id=eq." + org, {"status": "active", "trial_end": None, "cancel_at_period_end": True, "stripe_customer_id": "cus_night4smoke", "current_period_end": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(time.time() + 19 * 86400))})
            time.sleep(16)
            st, bill = api(API, "GET", "/api/consumer/billing", jwt)
            check(st == 200 and bill["billing"]["state"] == "cancelled" and bill["billing"]["access"] == "full", "billingFor: cancel_at_period_end → state cancelled, access full", bill.get("billing"))
            visit(p, "/consumer/overview.html", "dashboard cancelled (full access)", a.shots, "dash-overview-cancelled-full.png", expect=["Cancelled", "Everything works until"])
            visit(p, "/consumer/account.html", "account cancelled (full access)", a.shots, "account-cancelled-full.png", expect=["Everything works until", "Resume subscription"])
            # child journey
            p.eval("localStorage.clear()")
            with_session(p, child_sess)
            visit(p, "/consumer/today.html", "child today", a.shots, "built-child-today.png", expect=["Amara"])
            visit(p, "/consumer/exam.html", "child exam pick", a.shots, expect=["Pick a question"])
            visit(p, "/consumer/unit-check.html?unit=B1", "child unit check start", a.shots)
            p.eval("localStorage.clear()")
            visit(p, "/go/index.html", "child login page", a.shots, expect=["Who's this"])
            visit(p, "/org/sign-in.html", "org sign in", a.shots, expect=["Staff sign in"])
    finally:
        # ── cleanup ──────────────────────────────────────────────────────
        print("\ncleanup — the Night 2 drive's teardown order, over PostgREST as the service role")
        if ids["org"]:
            o = ids["org"]
            st, classes = sb_admin("GET", "/rest/v1/classes?select=id&school_id=eq." + o)
            for c in (classes or []):
                st, assigns = sb_admin("GET", "/rest/v1/assignments?select=id&class_id=eq." + c["id"])
                for a_ in (assigns or []):
                    st, subs = sb_admin("GET", "/rest/v1/assignment_submissions?select=id&assignment_id=eq." + a_["id"])
                    for s_ in (subs or []): sb_admin("DELETE", "/rest/v1/assignment_question_attempts?submission_id=eq." + s_["id"])
                    sb_admin("DELETE", "/rest/v1/assignment_submissions?assignment_id=eq." + a_["id"])
                    sb_admin("DELETE", "/rest/v1/assignment_questions?assignment_id=eq." + a_["id"])
                sb_admin("DELETE", "/rest/v1/assignments?class_id=eq." + c["id"])
                sb_admin("DELETE", "/rest/v1/class_members?class_id=eq." + c["id"])
                sb_admin("DELETE", "/rest/v1/class_teachers?class_id=eq." + c["id"])
            sb_admin("DELETE", "/rest/v1/classes?school_id=eq." + o)
            for t in ("stripe_events", "email_log", "ai_usage_events", "exam_answers", "unit_check_attempts", "work_items",
                      "child_plans", "family_messages", "consumer_notifications", "org_limits", "account_deletion_requests"):
                sb_admin("DELETE", "/rest/v1/%s?org_id=eq.%s" % (t, o))
            for t in ("pending_staff", "staff_scopes"):
                sb_admin("DELETE", "/rest/v1/%s?school_id=eq.%s" % (t, o))
            sb_admin("DELETE", "/rest/v1/audit_log?school_id=eq." + o)
            sb_admin("DELETE", "/rest/v1/subscriptions?org_id=eq." + o)
            for u in ids["users"]:
                for t, col in (("consumer_notifications", "recipient_id"), ("family_messages", "sender_id"), ("family_messages", "recipient_id"),
                               ("exam_answers", "child_id"), ("unit_check_attempts", "child_id"), ("child_flashcard_queue", "child_id"),
                               ("work_items", "child_id"), ("work_generation_runs", "child_id"), ("child_plans", "child_id"),
                               ("ai_usage_events", "profile_id"), ("email_log", "recipient_id"), ("class_members", "student_id"),
                               ("class_teachers", "teacher_id"), ("platform_operators", "profile_id"), ("staff_scopes", "profile_id"),
                               ("parent_prefs", "profile_id"), ("report_notes", "child_id"), ("audit_log", "actor_id")):
                    sb_admin("DELETE", "/rest/v1/%s?%s=eq.%s" % (t, col, u))
                sb_admin("PATCH", "/rest/v1/profiles?created_by=eq." + u, {"created_by": None})
            for u in ids["users"]:
                st, r = sb_admin("DELETE", "/rest/v1/profiles?id=eq." + u)
                st2, r2 = sb_admin("DELETE", "/auth/v1/admin/users/" + u)
                print("  user", u, "profile", st, "auth", st2, "" if st2 < 300 else r2)
            sb_admin("DELETE", "/rest/v1/academic_years?school_id=eq." + o)
            st, r = sb_admin("DELETE", "/rest/v1/schools?id=eq." + o); print("  org", o, st, "" if st < 300 else r)
        server.shutdown()
    print("\n%d failure(s)" % len(FAILS)); [print("  - " + f) for f in FAILS]
    sys.exit(min(len(FAILS), 99))

if __name__ == "__main__":
    main()
