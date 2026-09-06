#!/usr/bin/env python3
"""mrb327_org_drive.py — the ORGANISATION journey, end to end, on the merged tree.

    # backend worktree (b2c/hardening)
    CONSUMER_SIGNUP_ENABLED=true PORT=3161 EXTRA_CORS_ORIGINS=http://localhost:8161 node server.js
    # frontend worktree root
    python3 mrb327_org_drive.py --api http://localhost:3161 --port 8161

MRB-327 §1, lane 3. Every consumer drive before this one ran on `b2c/launch`,
BEFORE teacher dashboard v3, seating (MRB-322) and the assignments go-live
hold (MRB-324) merged into main. This drives the organisation half of the
product on the MERGED tree, through the real UI, against a real backend and
the real TEST database.

Modelled on admin_ui_drive.py: the same flag-on-for-this-browser-only setter,
the same real-session-in-localStorage trick (the Supabase SDK deletes a fake
one), the same teardown discipline.

⚠️ It drives the BUILT tree (mrbadmus_site/), which is what Cloudflare serves.

Phases, in the order a council actually experiences them:

  A  the operator makes the organisation from /consumer/admin-accounts.html
  B  the caseworker signs in at /org/sign-in.html   (and a parent is refused)
  C  pupils are added in bulk, right up to the seat cap — and the cap holds
     against every path there is
  D  a group is created, and a pupil is moved into it
  E  work is set to that group, and only to that group
  F  chat, both directions, delivered by the realtime subscription
  G  a termly report for a pupil
  H  the caseworker's Sunday digest, rendered
  I  /org/index.html and /org/sign-in.html at 390px, plus the brand and
     no-price rules

  X  the night4_laneC_drive.py org fixture is written, so its orgdash phase
     can run (`--org-session <file>`)

Exit code is the number of failures.
"""
import argparse, json, os, re, ssl, subprocess, sys, time
import urllib.request, urllib.error, urllib.parse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ks3_browser as cdp

ROOT = os.path.dirname(os.path.abspath(__file__))
SB = "https://qeppkiswvclkkwbxmlok.supabase.co"
CTX = ssl.create_default_context(cafile="/etc/ssl/cert.pem")
BACKEND = "/Users/midebadmus/Documents/GitHub/mrbadmus-worktrees/b2c/backend"

SCRATCH = ("/private/tmp/claude-501/-Users-midebadmus-Documents-GitHub-"
           "mrbadmus-worktrees-b2c-launch/06d799b1-12f9-481b-9871-424a2321715f/scratchpad")
SHOTS = os.path.join(SCRATCH, "shots", "lane3")
STATE_FILE = os.path.join(SCRATCH, "mrb327_org_fixtures.json")
ORG_SESSION_FILE = os.path.join(SCRATCH, "mrb327_org_session.json")

OPERATOR = ("hz_op@test.mrbadmus", "Night3!Op")
TAG = "l3drive"
ORG_NAME = "Havering Council %s" % TAG
STAFF_EMAIL = "l3drive-caseworker@mrbadmus-test.com"
STAFF_PW = "Passw0rd!l3drive"
PARENT_EMAIL = "l3drive-parent@mrbadmus-test.com"
SEAT_CAP = 2

FAILS = []
NOTES = []


def check(ok, label, evidence=""):
    print(("  OK  " if ok else "  XX  ") + label + (("  — " + str(evidence)[:500]) if evidence else ""))
    if not ok:
        FAILS.append(label)
    return ok


def note(msg):
    print("   ·  " + msg)
    NOTES.append(msg)


def env(name):
    for line in open(os.path.join(BACKEND, ".env")):
        if line.startswith(name + "="):
            return line.split("=", 1)[1].strip()
    return None


SERVICE = env("SUPABASE_SERVICE_ROLE_KEY")
ANON = env("SUPABASE_ANON_KEY")


def http(method, url, body=None, headers=None, timeout=120):
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
    # A route that legitimately answers 4xx (the deliberate over-cap POST)
    # makes Chrome log a "Failed to load resource" line. The page handles it
    # and says so in words; that is not a page error.
    return [e for e in p.console_errors()
            if "favicon.ico" not in e
            and not re.search(r"Failed to load resource.*(40[0-9]|409|423|429)", e)]


CLICK_BY_TEXT = """(function(sel, needle){
  var b = Array.prototype.filter.call(document.querySelectorAll(sel), function(x){
    return x.textContent.indexOf(needle) >= 0; })[0];
  if (!b) return 'no-button';
  if (b.disabled) return 'disabled';
  b.click(); return 'clicked';
})(%s, %s)"""


def click_text(p, sel, needle):
    return p.eval(CLICK_BY_TEXT % (json.dumps(sel), json.dumps(needle)))


def overflow(p):
    return p.eval("[document.documentElement.scrollWidth, document.documentElement.clientWidth, "
                  "Math.max.apply(null, Array.prototype.map.call(document.querySelectorAll('body *'),"
                  "function(e){return Math.ceil(e.getBoundingClientRect().right);}))]")


# ══════════════════════════════════════════════════════════════════════════
# state
# ══════════════════════════════════════════════════════════════════════════
IDS = {"users": [], "orgs": [], "pupils": {}, "groups": [], "org": None}


def save():
    os.makedirs(SCRATCH, exist_ok=True)
    json.dump(IDS, open(STATE_FILE, "w"), indent=1)


# ══════════════════════════════════════════════════════════════════════════
# A — the operator makes the organisation, through the real console
# ══════════════════════════════════════════════════════════════════════════
def phase_a():
    print("\n── A · operator creates the organisation ─────────────────")
    op = sign_in(*OPERATOR)
    with cdp.Browser() as b:
        p = b.attach()
        p.send("Page.addScriptToEvaluateOnNewDocument", {"source": FLAG_ON_JS})
        with_session(p, op)
        p.goto(qs("/consumer/admin-accounts.html"), settle=1.4)
        ok = wait_for(p, "!!document.getElementById('new-org-btn')")
        check(ok, "A the operator console loads and offers '+ New organisation'",
              text(p)[:140].replace("\n", " "))
        check(not errs(p), "A accounts console: no console errors", errs(p))

        p.eval("document.getElementById('new-org-btn').click()")
        check(wait_for(p, "!document.getElementById('org-veil').hidden"),
              "A the New-organisation form opens")

        p.eval("""(function(){
          document.getElementById('org-name').value = %s;
          document.getElementById('org-seats').value = '%d';
          document.getElementById('org-period-end').value = '2027-08-31';
          document.getElementById('org-contact-name').value = 'Ada Okafor';
          document.getElementById('org-contact-email').value = %s;
          document.getElementById('org-submit').click();
        })()""" % (json.dumps(ORG_NAME), SEAT_CAP, json.dumps(STAFF_EMAIL)))
        ok = wait_for(p, "/Created /.test((document.getElementById('org-msg')||{}).textContent||'')",
                      tries=40, gap=0.4)
        check(ok, "A the form reports success",
              p.eval("(document.getElementById('org-msg')||{}).textContent"))
        check(not errs(p), "A creating the organisation: no console errors", errs(p))
        p.screenshot(os.path.join(SHOTS, "A-admin-new-organisation.png"), width=1440, height=1000)

    # what actually landed
    st, rows = sb_admin("GET", "/rest/v1/schools?select=id,name,kind,code,show_on_public_leaderboard"
                               "&name=eq." + urllib.parse.quote(ORG_NAME))
    check(st < 300 and len(rows or []) == 1, "A exactly one organisation row exists", (st, rows))
    org = rows[0]
    IDS["org"] = org["id"]
    IDS["orgs"].append(org["id"])
    save()
    check(org["kind"] == "organisation", "A schools.kind is 'organisation'", org["kind"])
    check(org["show_on_public_leaderboard"] is False,
          "A the organisation is off the public leaderboard", org["show_on_public_leaderboard"])

    st, sub = sb_admin("GET", "/rest/v1/subscriptions?select=status,seat_cap,quantity,current_period_end"
                              "&org_id=eq." + org["id"])
    check(sub and sub[0]["status"] == "active" and sub[0]["seat_cap"] == SEAT_CAP and sub[0]["quantity"] == 0,
          "A subscription: active, seat_cap %d, quantity 0" % SEAT_CAP, sub)
    st, yr = sb_admin("GET", "/rest/v1/academic_years?select=name,start_date,end_date&school_id=eq." + org["id"])
    check(len(yr or []) == 1, "A one academic year was created", yr)
    st, ps = sb_admin("GET", "/rest/v1/pending_staff?select=email,profile_role,claimed_at&school_id=eq." + org["id"])
    check(ps and ps[0]["email"] == STAFF_EMAIL and ps[0]["profile_role"] == "admin",
          "A a pending_staff invitation exists for the contact, role admin", ps)
    st, state = sb_admin("POST", "/rest/v1/rpc/org_access_state", {"p_org_id": org["id"]})
    check(state == "full", "A org_access_state is 'full' straight after creation", state)
    print("  org", org["id"], org["code"])


# ══════════════════════════════════════════════════════════════════════════
# B — the caseworker signs in through Design's form
# ══════════════════════════════════════════════════════════════════════════
def phase_b():
    print("\n── B · staff sign-in at /org/sign-in.html ────────────────")
    org = IDS["org"]

    # The invited contact makes their account. In production this is Microsoft
    # or the magic link; both land on the same claim trigger, which is what
    # actually attaches them to the organisation.
    st, users = sb_admin("GET", "/auth/v1/admin/users?per_page=1000")
    for u in (users or {}).get("users", []):
        if u["email"] == STAFF_EMAIL:
            sb_admin("DELETE", "/rest/v1/profiles?id=eq." + u["id"])
            sb_admin("DELETE", "/auth/v1/admin/users/" + u["id"])
    st, made = sb_admin("POST", "/auth/v1/admin/users",
                        {"email": STAFF_EMAIL, "password": STAFF_PW, "email_confirm": True,
                         "user_metadata": {"full_name": "Ada Okafor"}})
    check(st < 300, "B the invited contact's account is created", (st, made))
    staff_id = made["id"]
    IDS["users"].append(staff_id)
    IDS["staff"] = staff_id
    save()

    time.sleep(1.2)
    st, prof = sb_admin("GET", "/rest/v1/profiles?select=id,role,school_id,first_name,last_name&id=eq." + staff_id)
    prof = (prof or [{}])[0]
    check(prof.get("role") in ("admin", "hod", "teacher") and prof.get("school_id") == org,
          "B claim_pending_staff attached the contact to the organisation on first sign-in", prof)
    check(prof.get("first_name") == "Ada" and prof.get("last_name") == "Okafor",
          "B the provider's full_name was split into first/last", prof)
    st, ps = sb_admin("GET", "/rest/v1/pending_staff?select=claimed_at&school_id=eq." + org)
    check(ps and ps[0]["claimed_at"], "B the invitation is marked claimed", ps)

    # A parent — someone who has an account but no organisation — for the refusal.
    st, users = sb_admin("GET", "/auth/v1/admin/users?per_page=1000")
    for u in (users or {}).get("users", []):
        if u["email"] == PARENT_EMAIL:
            sb_admin("DELETE", "/rest/v1/profiles?id=eq." + u["id"])
            sb_admin("DELETE", "/auth/v1/admin/users/" + u["id"])
    st, par = sb_admin("POST", "/auth/v1/admin/users",
                       {"email": PARENT_EMAIL, "password": STAFF_PW, "email_confirm": True,
                        "user_metadata": {"first_name": "Nia"}})
    IDS["users"].append(par["id"])
    IDS["parent"] = par["id"]
    save()

    with cdp.Browser() as b:
        p = b.attach()
        p.send("Page.addScriptToEvaluateOnNewDocument", {"source": FLAG_ON_JS})
        p.set_viewport(1280, 900)
        clear_session(p)
        p.goto(qs("/org/sign-in.html"), settle=1.6)
        t = text(p)
        check("Staff sign in" in t, "B the sign-in page renders", t[:80].replace("\n", " "))
        check("MrBadmusAI" not in t, "B no 'MrBadmusAI' wordmark on a staff surface")
        chev = p.eval("document.querySelectorAll('header svg path[d^=\"M4 6l4-4\"], "
                      "header svg[stroke=\"#E4572E\"]').length")
        check(chev == 0, "B the staff sign-in header carries no chevron", chev)
        check(not re.findall(r"£\s?\d", t), "B no price on the staff sign-in page",
              re.findall(r"£\s?\d", t))

        # a wrong password, in Design's one string
        p.eval("(function(){document.getElementById('email').value=%s;"
               "document.getElementById('pass').value='definitely-wrong';"
               "document.getElementById('go').click();})()" % json.dumps(STAFF_EMAIL))
        ok = wait_for(p, "!document.getElementById('err').hidden && "
                         "document.getElementById('err').style.display!=='none'", tries=30, gap=0.4)
        msg = p.eval("document.getElementById('err').textContent")
        check(ok and "don" in msg and "match" in msg,
              "B a wrong password is refused in Design's one string", msg)

        # a real parent, with a valid session but no organisation
        p.eval("(function(){document.getElementById('email').value=%s;"
               "document.getElementById('pass').value=%s;"
               "document.getElementById('go').click();})()"
               % (json.dumps(PARENT_EMAIL), json.dumps(STAFF_PW)))
        ok = wait_for(p, "/isn.t set up for an organisation/.test(document.body.innerText)",
                      tries=40, gap=0.4)
        check(ok, "B a non-staff account is refused by name, not bounced to a broken dashboard",
              p.eval("document.getElementById('err').textContent"))
        left = p.eval("localStorage.getItem('sb-qeppkiswvclkkwbxmlok-auth-token')")
        check(not left, "B and the refused session is signed back out (no 'can't in, can't out' trap)",
              (left or "")[:60])

        # the caseworker
        p.eval("(function(){document.getElementById('email').value=%s;"
               "document.getElementById('pass').value=%s;"
               "document.getElementById('go').click();})()"
               % (json.dumps(STAFF_EMAIL), json.dumps(STAFF_PW)))
        ok = wait_for(p, "location.pathname === '/org/index.html'", tries=40, gap=0.4)
        check(ok, "B the caseworker signs in and lands on /org/index.html", p.eval("location.pathname"))
        ok = wait_for(p, "!!document.querySelector('.og-table')", tries=40, gap=0.4)
        check(ok, "B the dashboard renders its (empty) pupil list", text(p)[:160].replace("\n", " "))
        check(not errs(p), "B sign-in journey: no console errors", errs(p))
        p.screenshot(os.path.join(SHOTS, "B-org-dashboard-empty.png"), width=1280, height=900)


# ══════════════════════════════════════════════════════════════════════════
# C — bulk add, right up to the seat cap
# ══════════════════════════════════════════════════════════════════════════
def phase_c():
    print("\n── C · bulk add to the seat cap ──────────────────────────")
    org = IDS["org"]
    sess = sign_in(STAFF_EMAIL, STAFF_PW)
    jwt = sess["access_token"]

    with cdp.Browser() as b:
        p = b.attach()
        p.send("Page.addScriptToEvaluateOnNewDocument", {"source": FLAG_ON_JS})
        p.set_viewport(1280, 900)
        with_session(p, sess)
        p.goto(qs("/org/index.html"), settle=2.0)
        wait_for(p, "!!document.querySelector('.og-table')")

        def open_add():
            ok = click_text(p, ".og-cta, .og-cta-sm, button", "Add pupils")
            if ok != "clicked":
                p.eval("(function(){var a=document.querySelector('[data-go=\"add\"]');if(a)a.click();})()")
            return wait_for(p, "!!document.getElementById('bulk')")

        check(open_add(), "C the Add pupils screen opens")
        free = p.eval("(function(){var e=document.querySelectorAll('.og-count span');"
                      "return e.length>1?e[1].textContent:'';})()")
        check(free == "%d seats free" % SEAT_CAP, "C the seat counter reads the real cap", free)

        def type_bulk(txt):
            p.eval("(function(){var t=document.getElementById('bulk');t.value=%s;"
                   "t.dispatchEvent(new Event('input'));})()" % json.dumps(txt))

        def press_go():
            p.eval("document.getElementById('bulk-go').click()")

        # ── one pupil, one seat left afterwards ──
        type_bulk("Amara, 9, 9X")
        press_go()
        ok = wait_for(p, "/Login slips/.test(document.body.innerText)", tries=60, gap=0.5)
        check(ok, "C the first pupil is created and the login slips are shown",
              text(p)[:140].replace("\n", " "))
        slips = p.eval("Array.prototype.map.call(document.querySelectorAll('.og-slip'),"
                       "function(s){return s.innerText.replace(/\\n/g,' | ');})")
        check(len(slips) == 1 and "mrbadmus.com/go" in slips[0],
              "C the slip carries a username, a password and where to sign in", slips)
        amara_user = p.eval("(function(){var d=document.querySelectorAll('.og-slip dd');"
                            "return d.length?d[0].textContent:'';})()")
        amara_pw = p.eval("(function(){var d=document.querySelectorAll('.og-slip dd');"
                          "return d.length>1?d[1].textContent:'';})()")
        IDS["amara_login"] = [amara_user, amara_pw]
        save()
        check(not errs(p), "C creating a pupil: no console errors", errs(p))
        p.screenshot(os.path.join(SHOTS, "C-login-slips.png"), width=1280, height=900)

        # ── two lines into one free seat: the refusal ──
        p.eval("(function(){var d=document.querySelector('[data-go=\"pupils\"]');if(d)d.click();})()")
        wait_for(p, "!!document.querySelector('.og-table')")
        check(open_add(), "C back on Add pupils with one seat left")
        free = p.eval("(function(){var e=document.querySelectorAll('.og-count span');"
                      "return e.length>1?e[1].textContent:'';})()")
        check(free == "1 seat free", "C the seat counter agrees in number with itself", free)
        type_bulk("Kwame, 9, 9X\nIfe, 8, 8B")
        press_go()
        ok = wait_for(p, "!!document.querySelector('.og-err')", tries=30, gap=0.4)
        refusal = p.eval("(function(){var e=document.querySelector('.og-err');return e?e.textContent:'';})()")
        check(ok, "C two pupils into one free seat are refused before anything is created", refusal)
        check(refusal == "Only 1 seat free. Raise the cap from Account, or remove a leaver "
                         "from their own page first.",
              "C the one-seat refusal is a sentence, in the right number", refusal)
        IDS["refusal_client"] = refusal
        st, count = sb_admin("GET", "/rest/v1/profiles?select=id&school_id=eq." + org + "&role=eq.student")
        check(len(count or []) == 1, "C nothing was created by the refused submission", len(count or []))

        # ── the last seat ──
        type_bulk("Kwame, 9, ")
        press_go()
        ok = wait_for(p, "/Login slips/.test(document.body.innerText)", tries=60, gap=0.5)
        check(ok, "C the last free seat is filled", text(p)[:120].replace("\n", " "))
        kwame_user = p.eval("(function(){var d=document.querySelectorAll('.og-slip dd');"
                            "return d.length?d[0].textContent:'';})()")
        kwame_pw = p.eval("(function(){var d=document.querySelectorAll('.og-slip dd');"
                          "return d.length>1?d[1].textContent:'';})()")
        IDS["kwame_login"] = [kwame_user, kwame_pw]
        save()

        # ── the cap, reached ──
        p.eval("(function(){var d=document.querySelector('[data-go=\"pupils\"]');if(d)d.click();})()")
        wait_for(p, "!!document.querySelector('.og-table')")
        check(open_add(), "C back on Add pupils with the cap reached")
        free = p.eval("(function(){var e=document.querySelectorAll('.og-count span');"
                      "return e.length>1?e[1].textContent:'';})()")
        check(free == "0 seats free", "C the seat counter reads zero", free)
        type_bulk("Ife, 8, 8B")
        press_go()
        ok = wait_for(p, "!!document.querySelector('.og-err')", tries=30, gap=0.4)
        full = p.eval("(function(){var e=document.querySelector('.og-err');return e?e.textContent:'';})()")
        check(ok, "C at the cap, one more pupil is refused", full)
        check(full == "No seats free. Raise the cap from Account, or remove a leaver "
                      "from their own page first.",
              "C the at-the-cap refusal names two things a caseworker can do", full)
        IDS["refusal_full"] = full
        save()
        p.screenshot(os.path.join(SHOTS, "C-seat-cap-refusal.png"), width=1280, height=900)
        check(not errs(p), "C the seat-cap refusals: no console errors", errs(p))

        # ⚠ the refusal names a control. Does that control exist?
        p.eval("(function(){var d=document.querySelector('[data-nav=\"account\"]');if(d)d.click();})()")
        wait_for(p, "/invoiced annually/.test(document.body.innerText)")
        acct = text(p)
        check("Raise the cap" in acct and "Add seats" not in acct,
              "C the Account screen offers 'Raise the cap' and no 'Add seats'",
              [w for w in ("Raise the cap", "Add seats") if w in acct])
        check("Raise the cap" in IDS["refusal_full"],
              "C the refusal points at a control the Account screen actually has",
              IDS["refusal_full"])

        # …and the OTHER thing it names: a leaver, removed from their own page.
        p.eval("(function(){var d=document.querySelector('[data-nav=\"pupils\"]');if(d)d.click();})()")
        wait_for(p, "!!document.querySelector('[data-pupil]')")
        p.eval("document.querySelector('[data-pupil]').click()")
        wait_for(p, "!!document.getElementById('move-group')")
        check(p.eval("!!document.getElementById('remove-pupil')"),
              "C the pupil page carries the remove control the refusal sends you to",
              text(p)[-160:].replace("\n", " "))

    # ── the cap holds on every OTHER path ──
    st, d = api("POST", "/api/consumer/org/pupils/bulk", jwt, {"pupils": [{"first_name": "Ife", "year_group": 8}]})
    check(st == 409 and d.get("error") == "seat_cap_reached",
          "C the bulk route itself refuses with 409 seat_cap_reached", (st, d))
    IDS["refusal_backend"] = d.get("message")
    check(isinstance(d.get("message"), str) and "seats free" in d["message"],
          "C the backend refusal is a sentence, not a status code", d.get("message"))

    st, uname = sb_admin("POST", "/rest/v1/rpc/generate_username", {})
    st, d2 = api("POST", "/api/consumer/children", jwt,
                 {"first_name": "Ife", "year_group": 8, "username": uname,
                  "password": "comet-saturn-42"})
    check(st == 409 and d2.get("error") == "seat_cap_reached",
          "C the per-child route refuses too — the cap is not a bulk-only check", (st, d2))
    check("seats" in (d2.get("message") or "").lower(),
          "C and it says so in words a caseworker can act on", d2.get("message"))

    st, count = sb_admin("GET", "/rest/v1/profiles?select=id&school_id=eq." + org + "&role=eq.student")
    check(len(count or []) == SEAT_CAP,
          "C after every attempt the organisation still holds exactly %d pupils" % SEAT_CAP,
          len(count or []))

    # and the database itself, under the service role, which bypasses RLS
    st, d3 = sb_admin("POST", "/rest/v1/rpc/attach_child_to_family", {
        "p_child_id": "00000000-0000-4000-8000-00000000dead",
        "p_parent_id": IDS["staff"], "p_first_name": "Ife", "p_year_group": 8,
        "p_username": "l3drivecap%d" % (int(time.time()) % 100000),
        "p_mode": "alongside_school", "p_intensity": "light", "p_exam_board": "AQA",
        "p_tier": None, "p_pathway": None})
    check(st >= 400 and "seat_cap_reached" in json.dumps(d3),
          "C attach_child_to_family refuses even under the service role — the cap is a DB floor",
          (st, str(d3)[:200]))

    # who is who
    st, kids = sb_admin("GET", "/rest/v1/profiles?select=id,first_name,username,created_at"
                               "&school_id=eq." + org + "&role=eq.student&order=created_at.asc")
    for k in kids or []:
        IDS["pupils"][k["first_name"]] = k["id"]
        IDS["users"].append(k["id"])
    save()
    check(sorted(IDS["pupils"]) == ["Amara", "Kwame"], "C the two pupils are Amara and Kwame",
          IDS["pupils"])
    st, sub = sb_admin("GET", "/rest/v1/subscriptions?select=quantity,seat_cap&org_id=eq." + org)
    check(sub and sub[0]["quantity"] == SEAT_CAP,
          "C subscriptions.quantity follows the pupils", sub)


# ══════════════════════════════════════════════════════════════════════════
# D — a group, and a pupil moved into it
# ══════════════════════════════════════════════════════════════════════════
def phase_d():
    print("\n── D · groups ───────────────────────────────────────────")
    org = IDS["org"]
    sess = sign_in(STAFF_EMAIL, STAFF_PW)

    with cdp.Browser() as b:
        p = b.attach()
        p.send("Page.addScriptToEvaluateOnNewDocument", {"source": FLAG_ON_JS})
        p.set_viewport(1280, 900)
        with_session(p, sess)
        p.goto(qs("/org/index.html"), settle=2.0)
        wait_for(p, "!!document.querySelector('.og-table')")

        # Amara's line said group 9X, so the bulk route made it on first mention.
        p.eval("document.querySelector('[data-nav=\"groups\"]').click()")
        wait_for(p, "!!document.getElementById('new-group')")
        names = p.eval("Array.prototype.map.call(document.querySelectorAll('[data-group] h2'),"
                       "function(h){return h.textContent;})")
        check(names == ["9X"], "D the group named on a bulk line was created on first mention", names)
        counts = p.eval("Array.prototype.map.call(document.querySelectorAll('.og-group-c'),"
                        "function(e){return e.textContent;})")
        check(counts == ["1 pupil"], "D the group's member count agrees in number with itself", counts)

        # a second group, through Design's own form
        p.eval("document.getElementById('new-group').click()")
        wait_for(p, "!!document.getElementById('ng-name')")
        p.eval("(function(){document.getElementById('ng-name').value='8B';"
               "document.getElementById('ng-year').value='8';"
               "document.getElementById('ng-go').click();})()")
        ok = wait_for(p, "document.querySelectorAll('[data-group]').length === 2", tries=40, gap=0.4)
        check(ok, "D a group is created from the New group form",
              p.eval("document.querySelectorAll('[data-group]').length"))
        check(not errs(p), "D creating a group: no console errors", errs(p))

        # a duplicate name is refused in words
        p.eval("document.getElementById('new-group').click()")
        p.eval("(function(){document.getElementById('ng-name').value='8B';"
               "document.getElementById('ng-year').value='8';"
               "document.getElementById('ng-go').click();})()")
        ok = wait_for(p, "/already a group with that name/.test("
                         "(document.getElementById('ng-msg')||{}).textContent||'')", tries=30, gap=0.4)
        check(ok, "D a duplicate group name is refused in words",
              p.eval("(document.getElementById('ng-msg')||{}).textContent"))

        p.screenshot(os.path.join(SHOTS, "D-groups.png"), width=1280, height=900)

        # move Kwame into 8B from his own page, then back out
        p.eval("document.querySelector('[data-nav=\"pupils\"]').click()")
        wait_for(p, "!!document.querySelector('[data-pupil]')")
        p.eval("(function(){var r=Array.prototype.filter.call(document.querySelectorAll('[data-pupil]'),"
               "function(x){return x.innerText.indexOf('Kwame')>=0;})[0]; if(r) r.click();})()")
        ok = wait_for(p, "!!document.getElementById('move-group')")
        check(ok, "D Kwame's page opens with a Move-to-group control")
        opts = p.eval("Array.prototype.map.call(document.querySelectorAll('#move-group option'),"
                      "function(o){return o.textContent;})")
        check(opts == ["No group", "8B", "9X"], "D the move control lists every group", opts)
        p.eval("(function(){var s=document.getElementById('move-group');"
               "var o=Array.prototype.filter.call(s.options,function(x){return x.textContent==='8B';})[0];"
               "s.value=o.value;document.getElementById('move-go').click();})()")
        ok = wait_for(p, "/Moved\\./.test(document.body.innerText)", tries=40, gap=0.4)
        check(ok, "D the move reports success", p.eval("(document.getElementById('move-msg')||{}).textContent"))
        check(not errs(p), "D moving a pupil: no console errors", errs(p))

    st, groups = sb_admin("GET", "/rest/v1/classes?select=id,name,consumer_kind,year_group"
                                 "&school_id=eq." + org + "&consumer_kind=eq.group&order=name.asc")
    IDS["groups"] = [g["id"] for g in groups or []]
    save()
    check([g["name"] for g in groups or []] == ["8B", "9X"],
          "D both groups exist as classes with consumer_kind='group'", groups)
    g8 = [g for g in groups if g["name"] == "8B"][0]
    st, mem = sb_admin("GET", "/rest/v1/class_members?select=student_id,left_at&class_id=eq." + g8["id"])
    live = [m for m in mem or [] if not m["left_at"]]
    check(len(live) == 1 and live[0]["student_id"] == IDS["pupils"]["Kwame"],
          "D Kwame is a live member of 8B in the database", mem)

    # put him back where the lane-C fixture wants him: no group
    st, _ = api("POST", "/api/consumer/org/groups/%s/members" % g8["id"],
                sign_in(STAFF_EMAIL, STAFF_PW)["access_token"], {"remove": [IDS["pupils"]["Kwame"]]})
    check(st == 200, "D and he can be moved back out again", st)


# ══════════════════════════════════════════════════════════════════════════
# E — set work to a group, and only to that group
# ══════════════════════════════════════════════════════════════════════════
def phase_e():
    print("\n── E · set work to a group ──────────────────────────────")
    sess = sign_in(STAFF_EMAIL, STAFF_PW)
    amara, kwame = IDS["pupils"]["Amara"], IDS["pupils"]["Kwame"]

    st, before_a = sb_admin("GET", "/rest/v1/work_items?select=id&child_id=eq." + amara)
    st, before_k = sb_admin("GET", "/rest/v1/work_items?select=id&child_id=eq." + kwame)

    with cdp.Browser() as b:
        p = b.attach()
        p.send("Page.addScriptToEvaluateOnNewDocument", {"source": FLAG_ON_JS})
        p.set_viewport(1280, 900)
        with_session(p, sess)
        p.goto(qs("/org/index.html"), settle=2.0)
        wait_for(p, "!!document.querySelector('.og-table')")
        p.eval("document.querySelector('[data-nav=\"groups\"]').click()")
        wait_for(p, "!!document.querySelector('[data-gwork]')")
        p.eval("(function(){var c=Array.prototype.filter.call(document.querySelectorAll('[data-group]'),"
               "function(x){return x.innerText.indexOf('9X')>=0;})[0];"
               "c.querySelector('[data-gwork]').click();})()")
        ok = wait_for(p, "!!document.getElementById('work-go')")
        check(ok, "E 'Set work' on a group opens the work screen with that group chosen")
        chosen = p.eval("(function(){var b=document.querySelector('[data-target][aria-pressed=\"true\"]');"
                        "return b?b.textContent:'';})()")
        check(chosen == "9X", "E the group is the pre-selected target", chosen)

        ok = wait_for(p, "document.querySelectorAll('[data-unit]').length > 0", tries=60, gap=0.5)
        check(ok, "E the topic chips load from a real pupil's picker",
              p.eval("(document.getElementById('topic-note')||{}).textContent"))
        unit = p.eval("(function(){var u=document.querySelector('[data-unit]');"
                      "return u?[u.getAttribute('data-unit'),u.textContent]:null;})()")
        p.eval("document.querySelector('[data-unit]').click()")
        time.sleep(0.3)
        p.eval("document.querySelector('[data-due=\"Fri\"]').click()")
        time.sleep(0.3)
        p.eval("document.getElementById('work-go').click()")
        ok = wait_for(p, "!!document.querySelector('.og-done') || !!document.querySelector('.og-err')",
                      tries=60, gap=0.5)
        done = p.eval("(function(){var e=document.querySelector('.og-done');return e?e.textContent:'';})()")
        err = p.eval("(function(){var e=document.querySelector('.og-err');return e?e.textContent:'';})()")
        check(ok and done and not err, "E the work is set and reported in words", (done or err))
        check("set by Ada" in done, "E the message names who the pupil will see it from", done)
        check(not errs(p), "E setting work: no console errors", errs(p))
        p.screenshot(os.path.join(SHOTS, "E-set-work.png"), width=1280, height=900)
        print("   ·  unit chosen:", unit)

    st, after_a = sb_admin("GET", "/rest/v1/work_items?select=id,title,set_by,scheduled_for,kind"
                                  "&child_id=eq." + amara + "&order=created_at.desc")
    st, after_k = sb_admin("GET", "/rest/v1/work_items?select=id&child_id=eq." + kwame)
    check(len(after_a or []) > len(before_a or []),
          "E Amara — the group's only member — got a new work item",
          (len(before_a or []), len(after_a or [])))
    check(len(after_k or []) == len(before_k or []),
          "E Kwame, who is not in that group, got nothing",
          (len(before_k or []), len(after_k or [])))
    newest = (after_a or [{}])[0]
    check(newest.get("set_by") == IDS["staff"],
          "E the item records the caseworker as the person who set it", newest.get("set_by"))
    IDS["work_item"] = newest.get("id")
    save()

    # ── the two things the merge could have broken here, asked directly ──
    #
    # MRB-308 put a `schools.kind` seal at the top of generateWeek(): anything
    # that is not a family or an organisation is refused `not_consumer_org`.
    # An organisation is on the allowed side of that seal, and this is the
    # assertion that says so rather than assuming it.
    st, gen = api("POST", "/api/consumer/children/%s/generate" % amara,
                  sign_in(STAFF_EMAIL, STAFF_PW)["access_token"], {})
    check(st == 200 and (gen or {}).get("skipped") != "not_consumer_org",
          "E MRB-308's consumer seal lets an ORGANISATION compose", (st, str(gen)[:200]))
    check(st == 200 and (gen or {}).get("items", 0) >= 0,
          "E a week composes for an organisation's pupil", str(gen)[:200])

    # MRB-324 added `schools.assignments_open_from`, a hold on COMPOSING a
    # class assignment. A consumer organisation gets null (no hold) from the
    # Admin create route, and nothing on the consumer path reads it — but a
    # non-null value arriving by accident would stop a council's work dead,
    # so the column's value on a freshly made organisation is asserted.
    st, sch = sb_admin("GET", "/rest/v1/schools?select=assignments_open_from&id=eq." + IDS["org"])
    check(sch and sch[0]["assignments_open_from"] is None,
          "E MRB-324's go-live hold is null on a new organisation — nothing is held back", sch)


# ══════════════════════════════════════════════════════════════════════════
# F — chat, both directions, live
# ══════════════════════════════════════════════════════════════════════════
def phase_f():
    print("\n── F · chat, both directions, over realtime ─────────────")
    amara = IDS["pupils"]["Amara"]
    staff_sess = sign_in(STAFF_EMAIL, STAFF_PW)

    # the pupil signs in the way a pupil does — /go, username and password
    user, pw = IDS["amara_login"]
    st, login = api("POST", "/api/consumer/child/login", None, {"username": user, "password": pw})
    check(st == 200 and login.get("access_token"), "F the pupil signs in with the slip's username", st)
    child_sess = {"access_token": login["access_token"], "refresh_token": login["refresh_token"],
                  "expires_in": login["expires_in"],
                  "expires_at": int(time.time()) + int(login["expires_in"]),
                  "token_type": "bearer", "user": {"id": login["user"]["id"]}}

    with cdp.Browser() as bs, cdp.Browser() as bc:
        ps = bs.attach()
        ps.send("Page.addScriptToEvaluateOnNewDocument", {"source": FLAG_ON_JS})
        ps.set_viewport(1280, 900)
        with_session(ps, staff_sess)
        ps.goto(qs("/org/index.html"), settle=2.0)
        wait_for(ps, "!!document.querySelector('[data-pupil]')")
        ps.eval("(function(){var r=Array.prototype.filter.call(document.querySelectorAll('[data-pupil]'),"
                "function(x){return x.innerText.indexOf('Amara')>=0;})[0]; if(r) r.click();})()")
        ok = wait_for(ps, "!!document.getElementById('chat-send')", tries=50, gap=0.4)
        check(ok, "F the caseworker's pupil page carries a chat panel")

        pc = bc.attach()
        pc.send("Page.addScriptToEvaluateOnNewDocument", {"source": FLAG_ON_JS})
        pc.set_viewport(390, 860)
        with_session(pc, child_sess)
        pc.goto(qs("/consumer/today.html"), settle=2.5)
        ok = wait_for(pc, "!!document.getElementById('td-msg-btn')", tries=50, gap=0.4)
        check(ok, "F the pupil's Today screen loads", text(pc)[:120].replace("\n", " "))
        pc.eval("document.getElementById('td-msg-btn').click()")
        ok = wait_for(pc, "!!document.getElementById('td-draft')", tries=40, gap=0.4)
        check(ok, "F the pupil's message screen opens")
        who = pc.eval("(document.getElementById('td-head-title')||{}).textContent")
        check(who == "Ada", "F the pupil's thread is headed with their caseworker's name", who)

        # ── pupil → caseworker, live ──
        stamp1 = "l3 pupil says %d" % int(time.time())
        pc.eval("(function(){var d=document.getElementById('td-draft');d.value=%s;"
                "document.getElementById('td-send').click();})()" % json.dumps(stamp1))
        ok = wait_for(ps, "document.body.innerText.indexOf(%s) >= 0" % json.dumps(stamp1),
                      tries=40, gap=0.5)
        nav = ps.eval("location.pathname")
        check(ok, "F the pupil's message reaches the caseworker's open page LIVE (no reload)",
              (nav, ps.eval("(document.getElementById('chat-log')||{}).innerText") or "")[1][-120:])
        check(nav == "/org/index.html", "F and the page never navigated to get it", nav)

        # ── caseworker → pupil, live ──
        stamp2 = "l3 caseworker says %d" % int(time.time())
        ps.eval("(function(){var i=document.getElementById('chat-text');i.value=%s;"
                "document.getElementById('chat-send').click();})()" % json.dumps(stamp2))
        ok = wait_for(pc, "document.body.innerText.indexOf(%s) >= 0" % json.dumps(stamp2),
                      tries=40, gap=0.5)
        check(ok, "F the caseworker's reply reaches the pupil's open screen LIVE (no reload)",
              (pc.eval("(document.getElementById('td-thread')||{}).innerText") or "")[-140:])

        # an empty send is refused in our voice
        # ⚠ read it straight away: the realtime repaint that follows the
        # previous send rebuilds the panel and takes the message with it.
        ps.eval("(function(){document.getElementById('chat-text').value='';"
                "document.getElementById('chat-send').click();})()")
        ok = wait_for(ps, "(document.getElementById('chat-msg')||{}).textContent === "
                          "'Write something first.'", tries=12, gap=0.15)
        check(ok, "F an empty message is refused in words",
              ps.eval("(document.getElementById('chat-msg')||{}).textContent"))

        ps.screenshot(os.path.join(SHOTS, "F-caseworker-chat.png"), width=1280, height=900)
        pc.screenshot(os.path.join(SHOTS, "F-pupil-chat-390.png"), width=390, height=860)
        check(not errs(ps), "F caseworker side: no console errors", errs(ps))
        check(not errs(pc), "F pupil side: no console errors", errs(pc))

    st, msgs = sb_admin("GET", "/rest/v1/family_messages?select=id,sender_id,recipient_id,body"
                               "&org_id=eq." + IDS["org"])
    bodies = [m["body"] for m in msgs or []]
    check(stamp1 in bodies and stamp2 in bodies, "F both messages are in the database", len(bodies))
    check(any(m["sender_id"] == amara for m in msgs) and any(m["sender_id"] == IDS["staff"] for m in msgs),
          "F one from each side")


# ══════════════════════════════════════════════════════════════════════════
# G — a termly report for a pupil
# ══════════════════════════════════════════════════════════════════════════
def phase_g():
    print("\n── G · a termly report ──────────────────────────────────")
    sess = sign_in(STAFF_EMAIL, STAFF_PW)
    amara = IDS["pupils"]["Amara"]
    st, d = api("GET", "/api/consumer/children/%s/report" % amara, sess["access_token"])
    check(st == 200, "G the caseworker may read a pupil's report (guardian_of_child covers org staff)",
          (st, str(d)[:200]))

    with cdp.Browser() as b:
        p = b.attach()
        p.send("Page.addScriptToEvaluateOnNewDocument", {"source": FLAG_ON_JS})
        p.set_viewport(1280, 1000)
        with_session(p, sess)
        # the link the pupil page offers, followed as written
        p.goto(qs("/org/index.html"), settle=2.0)
        wait_for(p, "!!document.querySelector('[data-pupil]')")
        p.eval("(function(){var r=Array.prototype.filter.call(document.querySelectorAll('[data-pupil]'),"
               "function(x){return x.innerText.indexOf('Amara')>=0;})[0]; if(r) r.click();})()")
        wait_for(p, "!!document.querySelector('a[href*=\"/consumer/report.html\"]')")
        href = p.eval("(document.querySelector('a[href*=\"/consumer/report.html\"]')||{}).getAttribute('href')")
        check(href and amara in href, "G the pupil page links to that pupil's own report", href)
        p.eval("document.querySelector('a[href*=\"/consumer/report.html\"]').click()")
        ok = wait_for(p, "location.pathname === '/consumer/report.html'", tries=30, gap=0.4)
        check(ok, "G the link opens the report page", p.eval("location.pathname"))
        ok = wait_for(p, "document.body.innerText.length > 300", tries=50, gap=0.5)
        t = text(p)
        check(ok and "Amara" in t, "G the report renders for that pupil, with real content",
              t[:200].replace("\n", " "))
        check("undefined" not in t and "[object Object]" not in t and "NaN" not in t,
              "G nothing on the report is a leaked internal value",
              [w for w in ("undefined", "[object Object]", "NaN") if w in t])
        check(not errs(p), "G the report: no console errors", errs(p))
        p.screenshot(os.path.join(SHOTS, "G-report.png"), width=1280, height=1400)


# ══════════════════════════════════════════════════════════════════════════
# H — the caseworker's Sunday digest
# ══════════════════════════════════════════════════════════════════════════
def phase_h():
    print("\n── H · the caseworker's digest ──────────────────────────")
    # Scoped to THIS organisation. `sendDigests()` sweeps every consumer org
    # on the project and five other lanes are driving right now, so the
    # script below reproduces its body for one org using email.js's own
    # exported childWeek/send. See scripts/mrb327-org-digest.js.
    r = subprocess.run(["node", "scripts/mrb327-org-digest.js", IDS["org"]],
                       cwd=BACKEND, capture_output=True, text=True, timeout=180)
    if r.returncode != 0:
        check(False, "H the digest ran", r.stderr[-400:])
        return
    out = json.loads(r.stdout)
    check(out["children"] == 2 and out["adults"] == 1,
          "H the digest is built for one staff member over both pupils", (out["children"], out["adults"]))
    res = out["results"][0]
    check(res["status"] == "dry_run",
          "H no RESEND_API_KEY, so the mailer logs a dry_run rather than sending", res["status"])
    IDS["digest_subject"] = res["subject"]
    IDS["digest_text"] = res["text"]
    save()
    open(os.path.join(SHOTS, "H-digest.txt"), "w").write(
        "SUBJECT: %s\n\n%s" % (res["subject"], res["text"]))
    open(os.path.join(SHOTS, "H-digest.html"), "w").write(res["html"])
    print("\n----- digest subject -----\n" + res["subject"])
    print("\n----- digest text -----\n" + res["text"] + "\n-----------------------\n")

    check("Amara" in res["text"] and "Kwame" in res["text"],
          "H both pupils appear in the caseworker's one email")
    check(res["subject"].startswith("This week:"),
          "H the subject already answers the question", res["subject"])

    st, rows = sb_admin("GET", "/rest/v1/email_log?select=id,type,status,subject,recipient_id,recipient_email"
                               "&org_id=eq." + IDS["org"] + "&type=eq.digest")
    check(len(rows or []) == 1 and rows[0]["status"] == "dry_run",
          "H exactly one digest row was logged, for the staff member", rows)
    check(rows and rows[0]["recipient_id"] == IDS["staff"] and rows[0]["recipient_email"] == STAFF_EMAIL,
          "H it went to the caseworker, not to a pupil", rows and rows[0])
    check(rows and rows[0]["subject"] == res["subject"],
          "H the logged subject is the rendered one")

    # ⚠ WHERE THE TWO LINKS IN IT GO. A digest to a caseworker carries the
    # same CTA and the same "email settings" link as a digest to a parent,
    # and both are parent-only pages.
    cta = re.search(r"See the week in full: (\S+)", res["text"])
    settings = re.search(r"Email settings: (\S+)", res["text"])
    check(cta and "/consumer/overview.html" not in cta.group(1),
          "H ⚠ the caseworker's CTA goes to a page a caseworker can open",
          cta and cta.group(1))
    check(settings and "/consumer/account.html" not in settings.group(1),
          "H ⚠ the caseworker's 'email settings' link goes somewhere they can use",
          settings and settings.group(1))
    jwt = sign_in(STAFF_EMAIL, STAFF_PW)["access_token"]
    st_f, d_f = api("GET", "/api/consumer/family", jwt)
    st_p, d_p = api("POST", "/api/consumer/prefs", jwt, {"digest": False})
    note("proof: GET /api/consumer/family → %s %s · POST /api/consumer/prefs → %s %s"
         % (st_f, (d_f or {}).get("message"), st_p, (d_p or {}).get("message")))
    check(st_p == 200, "H ⚠ a caseworker can switch the Sunday email off", (st_p, d_p))

    foot = [l for l in res["text"].split("\n") if "getting this because" in l]
    named = [n for n in ("Amara", "Kwame") if any(n in l for l in foot)]
    check(not named,
          "H ⚠ the footer does not name every pupil as the reason a caseworker is emailed "
          "(a caseload of two hundred is two hundred names in one sentence)", foot)

    # ⚠ what the log does NOT keep
    st, cols = sb_admin("GET", "/rest/v1/email_log?select=*&limit=1")
    keys = sorted((cols or [{}])[0].keys())
    check("html" in keys or "body" in keys or "text" in keys,
          "H ⚠ a dry_run row keeps the rendered body, so what would have been sent can be read back",
          keys)

    # the ORGANISATION shape
    check("your family" not in res["text"].lower(),
          "H ⚠ an organisation digest does not call the caseworker's caseload a family",
          [l for l in res["text"].split("\n") if "family" in l.lower()][:3])
    # a second run must be a no-op
    r2 = subprocess.run(["node", "scripts/mrb327-org-digest.js", IDS["org"]],
                        cwd=BACKEND, capture_output=True, text=True, timeout=180)
    out2 = json.loads(r2.stdout)
    check(out2["results"][0]["status"] == "skipped" and out2["results"][0]["reason"] == "duplicate",
          "H a re-run is deduped, not a second email", out2["results"][0])


# ══════════════════════════════════════════════════════════════════════════
# I — 390px, the brand, and no price
# ══════════════════════════════════════════════════════════════════════════
def phase_i():
    print("\n── I · 390px, brand, no price ───────────────────────────")
    sess = sign_in(STAFF_EMAIL, STAFF_PW)
    with cdp.Browser() as b:
        p = b.attach()
        p.send("Page.addScriptToEvaluateOnNewDocument", {"source": FLAG_ON_JS})

        # ── the sign-in page ──
        p.set_viewport(390, 844, settle=0.4)
        clear_session(p)
        p.goto(qs("/org/sign-in.html"), settle=2.0)
        o = overflow(p)
        check(o[0] <= o[1] + 1, "I 390 sign-in: no horizontal page overflow", o)
        check(o[2] <= 392, "I 390 sign-in: nothing sticks out past the viewport", o)
        for cid in ("email", "pass", "go", "ms"):
            h = p.eval("(function(){var e=document.getElementById('%s');"
                       "return e?Math.round(e.getBoundingClientRect().height):0;})()" % cid)
            check(h >= 44, "I 390 sign-in: #%s is a thumb-sized target" % cid, h)
        check(not errs(p), "I 390 sign-in: no console errors", errs(p))
        p.screenshot(os.path.join(SHOTS, "I-org-signin-390.png"), width=390, height=844)

        # ── the dashboard, every screen ──
        with_session(p, sess)
        p.set_viewport(390, 844, settle=0.4)
        p.goto(qs("/org/index.html"), settle=2.5)
        wait_for(p, "!!document.querySelector('.og-table')")
        check(p.eval("getComputedStyle(document.querySelector('.og-side')).display") == "none",
              "I 390 dashboard: the desktop sidebar is out")
        check(p.eval("getComputedStyle(document.querySelector('.og-mhead')).display") != "none",
              "I 390 dashboard: the mobile header is in")
        sel = p.eval("Array.prototype.map.call(document.querySelectorAll('#mnav option'),"
                     "function(o){return o.textContent;}).join('|')")
        check(sel == "Pupils|Groups|Set work|Messages|Account",
              "I 390 dashboard: the mobile picker carries every screen", sel)

        for screen, label in (("pupils", "Pupils"), ("groups", "Groups"), ("work", "Set work"),
                              ("messages", "Messages"), ("account", "Account")):
            p.eval("(function(){var s=document.getElementById('mnav');s.value='%s';"
                   "s.dispatchEvent(new Event('change'));})()" % screen)
            wait_for(p, "document.getElementById('screens').innerHTML.length > 200", tries=30, gap=0.4)
            time.sleep(1.2)
            o = overflow(p)
            check(o[0] <= o[1] + 1, "I 390 %s: no horizontal page overflow" % label, o)
            check(o[2] <= 392, "I 390 %s: nothing sticks out past the viewport" % label, o)
            p.screenshot(os.path.join(SHOTS, "I-org-%s-390.png" % screen), width=390, height=900)

        t = text(p)
        check("MrBadmusAI" not in t, "I no 'MrBadmusAI' anywhere on the dashboard")
        chev = p.eval("document.querySelectorAll('.og-mhead svg, .og-side svg').length")
        check(chev == 0, "I the dashboard wordmark carries no chevron", chev)
        check(not errs(p), "I 390 dashboard: no console errors across every screen", errs(p))

    # ── the source, cold ──
    def strip(src):
        src = re.sub(r"<!--.*?-->", "", src, flags=re.S)
        src = re.sub(r"/\*.*?\*/", "", src, flags=re.S)
        return re.sub(r"^\s*//.*$", "", src, flags=re.M)

    money = []
    ai = []
    for f in ("org/index.html", "org/sign-in.html", "org/org.css"):
        s = strip(open(os.path.join(ROOT, f)).read())
        money += [(f, m) for m in re.findall(r"£\s?\d[\d.,]*", s)]
        money += [(f, m) for m in re.findall(r"per\s+(?:seat|pupil|child)", s, re.I)]
        ai += [(f, m) for m in re.findall(r"MrBadmusAI", s)]
    check(not money, "I no price and no per-seat framing in the org/ source", money[:5])
    check(not ai, "I no 'MrBadmusAI' in the org/ source", ai[:5])


# ══════════════════════════════════════════════════════════════════════════
# X — the fixture night4_laneC_drive.py's org phase wants
# ══════════════════════════════════════════════════════════════════════════
def phase_x(run_lane_c):
    print("\n── X · the lane-C org fixture ───────────────────────────")
    org = IDS["org"]
    amara, kwame = IDS["pupils"]["Amara"], IDS["pupils"]["Kwame"]
    staff = IDS["staff"]

    # laneC's org_dashboard() asserts a precise state: two pupils, four
    # messages, three of them unread, Amara in 9X with "memory cells" as her
    # last word and a caseworker reply above it, Kwame newest with "rates
    # test". Built here rather than in laneC, which has no fixture-maker of
    # its own — which is exactly why its org phase has never run.
    sb_admin("DELETE", "/rest/v1/family_messages?org_id=eq." + org)
    now = time.time()

    def msg(sender, recipient, body, ago, read):
        row = {"org_id": org, "sender_id": sender, "recipient_id": recipient, "body": body,
               "created_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(now - ago))}
        if read:
            row["read_at"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(now - ago + 60))
        st, d = sb_admin("POST", "/rest/v1/family_messages", row)
        assert st < 300, (st, d)

    msg(amara, staff, "I got stuck on the immune system question about memory cells", 3600, False)
    msg(staff, amara, "Good. Which bit?", 3000, True)
    msg(amara, staff, "the bit where memory cells are made", 2400, False)
    msg(kwame, staff, "is the rates test on Friday", 600, False)

    st, rows = sb_admin("GET", "/rest/v1/family_messages?select=id,read_at&org_id=eq." + org)
    check(len(rows or []) == 4 and len([r for r in rows if not r["read_at"]]) == 3,
          "X four messages, three of them unread", len(rows or []))

    # Amara in 9X, Kwame in none — laneC reads the group off the org payload.
    st, groups = sb_admin("GET", "/rest/v1/classes?select=id,name&school_id=eq." + org
                                 + "&consumer_kind=eq.group")
    g9 = [g for g in groups if g["name"] == "9X"][0]
    jwt = sign_in(STAFF_EMAIL, STAFF_PW)["access_token"]
    api("POST", "/api/consumer/org/groups/%s/members" % g9["id"], jwt, {"add": [amara]})
    st, d = api("GET", "/api/consumer/org", jwt)
    by = dict((p["name"], p.get("group")) for p in d["pupils"])
    check(by.get("Amara") == "9X" and not by.get("Kwame"),
          "X Amara is in 9X and Kwame is in no group", by)

    sess = sign_in(STAFF_EMAIL, STAFF_PW)
    fixture = {
        "org_id": org, "staff_id": staff, "staff_email": STAFF_EMAIL,
        "pupils": {"Amara": amara, "Kwame": kwame},
        "session": sess,
    }
    json.dump(fixture, open(ORG_SESSION_FILE, "w"), indent=1)
    check(os.path.exists(ORG_SESSION_FILE), "X the org-session fixture file is written", ORG_SESSION_FILE)
    print("   ·  --org-session %s" % ORG_SESSION_FILE)

    if not run_lane_c:
        return
    print("\n   ·  running night4_laneC_drive.py --only orgdash")
    r = subprocess.run(
        [sys.executable, "night4_laneC_drive.py", "--base", BASE, "--api", API,
         "--only", "orgdash", "--org-session", ORG_SESSION_FILE,
         "--shots", os.path.join(SHOTS, "lanec")],
        cwd=ROOT, capture_output=True, text=True, timeout=900)
    print(r.stdout[-4000:])
    if r.stderr.strip():
        print("   stderr:", r.stderr[-800:])
    m = re.search(r"(\d+) failure\(s\)", r.stdout)
    n = int(m.group(1)) if m else -1
    check(n == 0, "X night4_laneC_drive.py's org-dashboard phase runs green", n)
    IDS["lane_c_failures"] = n
    save()


# ══════════════════════════════════════════════════════════════════════════
# L — the one thing the seat-cap refusal tells a caseworker to do
# ══════════════════════════════════════════════════════════════════════════
def phase_l():
    print("\n── L · removing a leaver frees the seat ─────────────────")
    org = IDS["org"]
    sess = sign_in(STAFF_EMAIL, STAFF_PW)
    jwt = sess["access_token"]
    kwame = IDS["pupils"]["Kwame"]

    # The route a PARENT uses. `parent_remove_child` authorises on
    # parent_owns_child(), which requires role='parent' — so this is the
    # question of whether an organisation can use the family path at all.
    st, d = api("DELETE", "/api/consumer/children/" + kwame, jwt)
    note("the FAMILY route DELETE /api/consumer/children/:id answers %s %s — "
         "parent_remove_child() authorises on parent_owns_child(), which requires "
         "role='parent'. Reported with a proposed migration; not this lane's file."
         % (st, json.dumps(d)[:120]))
    st, live = sb_admin("GET", "/rest/v1/profiles?select=id&school_id=eq." + org
                               + "&role=eq.student&deleted_at=is.null")
    check(len(live or []) == SEAT_CAP,
          "L ⚠ and it removed nobody, so the organisation is still at its cap", len(live or []))

    st2, d2 = api("DELETE", "/api/consumer/org/pupils/" + kwame, jwt)
    check(st2 == 200 and (d2 or {}).get("ok"),
          "L the organisation's own remove-a-leaver route works", (st2, d2))
    st, live = sb_admin("GET", "/rest/v1/profiles?select=id&school_id=eq." + org
                               + "&role=eq.student&deleted_at=is.null")
    check(len(live or []) == SEAT_CAP - 1, "L the pupil is gone and a seat is free", len(live or []))

    st, kept = sb_admin("GET", "/rest/v1/work_items?select=id&child_id=eq." + kwame)
    note("the removal is soft: %d work_items kept for the removed pupil" % len(kept or []))
    st3, again = api("DELETE", "/api/consumer/org/pupils/" + kwame, jwt)
    check(st3 == 404, "L removing the same pupil twice is a clean 404, not a second seat", st3)
    st4, stranger = api("DELETE", "/api/consumer/org/pupils/" + IDS["staff"], jwt)
    check(st4 == 404, "L the route refuses anything that is not a pupil of this organisation", st4)

    st, sub = sb_admin("GET", "/rest/v1/subscriptions?select=quantity&org_id=eq." + org)
    check(sub and sub[0]["quantity"] == SEAT_CAP - 1,
          "L subscriptions.quantity followed the removal down", sub)

    st, made = api("POST", "/api/consumer/org/pupils/bulk", jwt,
                   {"pupils": [{"first_name": "Ife", "year_group": 8}]})
    check(st == 200 and len(made.get("created") or []) == 1,
          "L the freed seat is immediately usable", (st, str(made)[:200]))
    for c in (made or {}).get("created", []):
        IDS["users"].append(c["child_id"])
    save()

    # and the control a caseworker presses to get here
    with cdp.Browser() as b:
        p = b.attach()
        p.send("Page.addScriptToEvaluateOnNewDocument", {"source": FLAG_ON_JS})
        p.set_viewport(1280, 900)
        with_session(p, sess)
        p.goto(qs("/org/index.html"), settle=2.0)
        wait_for(p, "!!document.querySelector('[data-pupil]')")
        p.eval("document.querySelector('[data-pupil]').click()")
        wait_for(p, "!!document.getElementById('move-group')")
        has = p.eval("!!document.getElementById('remove-pupil')")
        check(has, "L the pupil page carries the remove control the Account screen promises",
              text(p)[-200:].replace("\n", " "))
        # one press arms, it does NOT remove
        p.eval("document.getElementById('remove-pupil').click()")
        time.sleep(0.4)
        label = p.eval("document.getElementById('remove-pupil').textContent")
        msg = p.eval("(document.getElementById('remove-msg')||{}).textContent")
        check(label.startswith("Yes — remove ") and "Press again" in msg,
              "L one press arms and says the pupil's name back; it does not remove", (label, msg))
        st, still = sb_admin("GET", "/rest/v1/profiles?select=id&school_id=eq." + org
                                    + "&role=eq.student&deleted_at=is.null")
        before_n = len(still or [])
        p.eval("document.getElementById('remove-pupil').click()")
        ok = wait_for(p, "!!document.querySelector('.og-table')", tries=50, gap=0.4)
        check(ok, "L the second press removes and returns to the pupil list")
        st, after = sb_admin("GET", "/rest/v1/profiles?select=id&school_id=eq." + org
                                    + "&role=eq.student&deleted_at=is.null")
        check(len(after or []) == before_n - 1, "L the control really removed one pupil",
              (before_n, len(after or [])))
        seats = p.eval("(document.getElementById('seats-line')||{}).textContent")
        check(seats and str(len(after or [])) in seats,
              "L the seat line on screen agrees with the database", seats)
        check(not errs(p), "L pupil page with the remove control: no console errors", errs(p))


# ══════════════════════════════════════════════════════════════════════════
def teardown():
    print("\n── cleanup ───────────────────────────────────────────────")
    ids = IDS
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
                  "unit_check_attempts", "work_items", "child_plans", "family_messages",
                  "consumer_notifications", "org_limits", "account_deletion_requests",
                  "work_generation_runs"):
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
        sb_admin("DELETE", "/rest/v1/profiles?id=eq." + u)
        st, r = sb_admin("DELETE", "/auth/v1/admin/users/" + u)
        print("  user %s %s%s" % (u, st, "" if st < 300 else " " + str(r)[:120]))
    for org in ids.get("orgs", []):
        sb_admin("DELETE", "/rest/v1/academic_years?school_id=eq." + org)
        st, r = sb_admin("DELETE", "/rest/v1/schools?id=eq." + org)
        print("  org %s %s%s" % (org, st, "" if st < 300 else " " + str(r)[:200]))

    # anything the FORM made that the state file lost
    st, extras = sb_admin("GET", "/rest/v1/schools?select=id,name&name=like.*" + TAG + "*")
    for s in (extras or []):
        print("  leftover org", s["name"], s["id"])
    for e in (STAFF_EMAIL, PARENT_EMAIL):
        st, users = sb_admin("GET", "/auth/v1/admin/users?per_page=1000")
        for u in (users or {}).get("users", []):
            if u["email"] == e:
                sb_admin("DELETE", "/rest/v1/profiles?id=eq." + u["id"])
                st2, r = sb_admin("DELETE", "/auth/v1/admin/users/" + u["id"])
                print("  leftover user", e, st2)

    # the proof
    st, left_org = sb_admin("GET", "/rest/v1/schools?select=id&name=like.*" + TAG + "*")
    st, left_kids = sb_admin("GET", "/rest/v1/profiles?select=id&id=in.(%s)"
                             % ",".join(ids.get("users", []) or ["00000000-0000-0000-0000-000000000000"]))
    print("  residue: schools=%d profiles=%d" % (len(left_org or []), len(left_kids or [])))
    if left_org or left_kids:
        FAILS.append("teardown left residue")


def main():
    global BASE, API
    ap = argparse.ArgumentParser()
    ap.add_argument("--site", default="mrbadmus_site")
    ap.add_argument("--api", default="http://localhost:3161")
    ap.add_argument("--port", type=int, default=8161)
    ap.add_argument("--phases", default="ABCDEFGHIXL")
    ap.add_argument("--keep", action="store_true")
    ap.add_argument("--reuse", action="store_true")
    ap.add_argument("--lane-c", action="store_true", help="also run night4_laneC_drive.py --only orgdash")
    ap.add_argument("--teardown-only", action="store_true")
    a = ap.parse_args()
    API = a.api
    os.makedirs(SHOTS, exist_ok=True)

    if a.teardown_only:
        IDS.update(json.load(open(STATE_FILE)))
        teardown()
        return 0

    if a.reuse and os.path.exists(STATE_FILE):
        IDS.update(json.load(open(STATE_FILE)))

    server, port = cdp.serve(os.path.abspath(a.site), a.port)
    BASE = "http://localhost:%d" % port
    print("serving the BUILT tree at", BASE, "· backend", API)

    try:
        if "A" in a.phases: phase_a()
        if "B" in a.phases: phase_b()
        if "C" in a.phases: phase_c()
        if "D" in a.phases: phase_d()
        if "E" in a.phases: phase_e()
        if "F" in a.phases: phase_f()
        if "G" in a.phases: phase_g()
        if "H" in a.phases: phase_h()
        if "I" in a.phases: phase_i()
        if "X" in a.phases: phase_x(a.lane_c)
        if "L" in a.phases: phase_l()
    finally:
        save()
        if not a.keep:
            teardown()
        server.shutdown()

    print("\n%d failure(s)" % len(FAILS))
    for f in FAILS:
        print("  - " + f)
    return min(len(FAILS), 99)


if __name__ == "__main__":
    sys.exit(main())
