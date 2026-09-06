#!/usr/bin/env python3
"""mrb327_family_drive.py — MRB-327 §1 Lane 1: the family journey, end to end,
on the MERGED tree (teacher v3 + seating MRB-322 + assignments hold MRB-324).

    # backend worktree
    CONSUMER_SIGNUP_ENABLED=true PORT=3141 EXTRA_CORS_ORIGINS=http://localhost:8141 \
      STRIPE_WEBHOOK_SECRET=whsec_… node server.js
    stripe listen --api-key sk_test_… --forward-to localhost:3141/api/consumer/stripe/webhook
    python3 mrb327_family_drive.py --api http://localhost:3141 --port 8141

Modelled on admin_ui_drive.py and night3_flagon_smoke.py: same FLAG_ON_JS
setter, same real-session localStorage write, same teardown order. It drives
the BUILT tree (mrbadmus_site/), because that is what Cloudflare serves.

Phases
  A  public home /parents/index.html, flag on
  B  signup: a real parent account through the real page — account step,
     verification, two children (Y8 alongside_school, Y10 Triple/Higher
     home_education), the unit picker for each, the plan step
  C  Stripe test-mode checkout + the return page
  D  a week for BOTH children; Y10 off the KS4 scheme, Y8 off KS3
  E  child login at /go/ for each child
  F1 Today — work still to do
  G  a lesson, a practice item, a unit check → result → the practice run
  H  an exam question: write, instant mark (stub provider), send to Mr Badmus
  I  the operator marks it from /consumer/admin-queue.html at 390px
  J  the child sees the mark on Today; the parent sees it on the dashboard
  K  chat both ways, live, over the realtime subscription
  F2 Today — everything done
  F3 Today — locked / read-only, then restored

⚠️ There is no ANTHROPIC_API_KEY here, so consumer/marking.js runs its `stub`
provider by design (`PROVIDER = process.env.MARK_PROVIDER || (HAS_KEY ?
'claude' : 'stub')`). The plumbing around the marker is driven in full; live
Claude marking is NOT exercised.
"""
import argparse, json, os, re, ssl, sys, time, urllib.parse, urllib.request, urllib.error

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ks3_browser as cdp

SB = "https://qeppkiswvclkkwbxmlok.supabase.co"
CTX = ssl.create_default_context(cafile="/etc/ssl/cert.pem")
FAILS = []
NOTES = []
SCRATCH = ("/private/tmp/claude-501/-Users-midebadmus-Documents-GitHub-mrbadmus-worktrees-"
           "b2c-launch/06d799b1-12f9-481b-9871-424a2321715f/scratchpad")
SHOTS = os.path.join(SCRATCH, "shots", "lane1")
STATE_FILE = os.path.join(SCRATCH, "mrb327_lane1_fixtures.json")

OPERATOR = ("hz_op@test.mrbadmus", "Night3!Op")
TAG = "l1f"                      # every fixture name carries it
PARENT_PW = "Passw0rd!mrb327lane1"
CHILD_PW = "comet-saturn-42"


def check(ok, label, evidence=""):
    print(("  OK  " if ok else "  XX  ") + label + (("  — " + str(evidence)[:500]) if evidence else ""))
    sys.stdout.flush()
    if not ok:
        FAILS.append(label)
    return ok


def note(s):
    print("  ··  " + s)
    NOTES.append(s)


def env(name):
    for line in open("/Users/midebadmus/Documents/GitHub/mrbadmus-worktrees/b2c/backend/.env"):
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
    except Exception as e:
        return 0, str(e)


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


def text(p):
    return p.eval("(document.body && document.body.innerText) || ''") or ""


IGNORABLE = re.compile(r"Failed to load resource.*(40[0-9]|409|423|429)")


def errs(p):
    return [e for e in p.console_errors()
            if "favicon.ico" not in e and not IGNORABLE.search(e)]


def errs_hard(p):
    """Console errors that are not just a 4xx logged by fetch."""
    return [e for e in errs(p) if "Failed to load resource" not in e]


def shot(p, name, width=1200, height=1000):
    try:
        p.screenshot(os.path.join(SHOTS, name), width=width, height=height)
        print("  shot → " + name)
    except Exception as e:
        print("  shot FAILED " + name + " " + str(e))


def click(p, sel):
    return p.eval("(function(){var e=document.querySelector(%s);"
                  "if(!e) return 'no-el'; if(e.disabled) return 'disabled';"
                  "e.click(); return 'clicked';})()" % json.dumps(sel))


def setval(p, sel, val):
    return p.eval("""(function(){var e=document.querySelector(%s); if(!e) return 'no-el';
      var proto = e instanceof HTMLTextAreaElement ? HTMLTextAreaElement.prototype : HTMLInputElement.prototype;
      var d = Object.getOwnPropertyDescriptor(proto,'value');
      d.set.call(e, %s);
      e.dispatchEvent(new Event('input',{bubbles:true}));
      e.dispatchEvent(new Event('change',{bubbles:true}));
      return 'set';})()""" % (json.dumps(sel), json.dumps(val)))


def sess_from_child(cl):
    return {"access_token": cl["access_token"], "refresh_token": cl["refresh_token"],
            "expires_in": cl.get("expires_in", 3600),
            "expires_at": int(time.time()) + 3600, "token_type": "bearer",
            "user": {"id": cl["user"]["id"]}}


def save(ids):
    json.dump(ids, open(STATE_FILE, "w"), indent=1)


def iso(delta_s):
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(time.time() + delta_s))


def monday():
    lt = time.localtime()
    return time.strftime("%Y-%m-%d", time.localtime(time.time() - lt.tm_wday * 86400))


# ══════════════════════════════════════════════════════════════════════════
# A — the public front door
# ══════════════════════════════════════════════════════════════════════════
def phase_a(p):
    print("\n── A · public home, flag on ──────────────────────────────")
    p.goto(qs("/parents/index.html"), settle=1.5)
    t = text(p)
    check("Not found" not in t[:200], "A /parents/index.html renders (not the flag-off page)",
          t[:120].replace("\n", " "))
    check("Start a free week" in t, "A public home shows Design's primary CTA", t[:200].replace("\n", " "))
    check(not errs(p), "A public home: zero console errors", errs(p))
    check(p.eval("!document.querySelector('meta[name=\"robots\"]')") is True,
          "A boot() removed the noindex meta with the flag on",
          p.eval("(document.querySelector('meta[name=\"robots\"]')||{}).content"))
    shot(p, "A-public-home.png")


# ══════════════════════════════════════════════════════════════════════════
# B — signup, through the real page
# ══════════════════════════════════════════════════════════════════════════
def fill_child(p, ids, who, name, year, mode, route=None, tier=None, board="AQA"):
    """Drive the child step. Returns the username chosen."""
    ok = wait_for(p, "!!document.getElementById('c-name')", tries=40)
    check(ok, "B[%s] child step renders" % who, text(p)[:160].replace("\n", " "))
    # ⚠️ `child_username_check` refuses a mostly-numeric name ("that looks like
    # a phone number"), so a timestamp cannot be the whole of it. Letters.
    import random, string
    uname = "l1" + who + "".join(random.choice(string.ascii_lowercase) for _ in range(6))
    setval(p, "#c-name", name)
    check(click(p, '[data-year="%d"]' % year) == "clicked", "B[%s] year %d selected" % (who, year))
    time.sleep(0.4)
    if year >= 10:
        check(click(p, '[data-board="%s"]' % board) == "clicked", "B[%s] exam board %s" % (who, board))
        check(click(p, '[data-route="%s"]' % route) == "clicked", "B[%s] route %s" % (who, route))
        check(click(p, '[data-tier="%s"]' % tier) == "clicked", "B[%s] tier %s" % (who, tier))
    else:
        gone = p.eval("[!!document.querySelector('[data-route]'), !!document.querySelector('[data-tier]')]")
        check(gone == [False, False],
              "B[%s] Year %d shows no GCSE route/tier controls" % (who, year), gone)
    check(click(p, '[data-mode="%s"]' % mode) == "clicked", "B[%s] mode %s" % (who, mode))
    time.sleep(0.3)
    pressed = ("(document.querySelector('[data-mode=\"%s\"]')||{}).getAttribute"
               "&&document.querySelector('[data-mode=\"%s\"]').getAttribute('aria-pressed')" % (mode, mode))
    check(p.eval(pressed) == "true", "B[%s] the mode choice shows as chosen" % who, p.eval(pressed))
    setval(p, "#c-user", uname)
    setval(p, "#c-pass", CHILD_PW)
    click(p, "#c-check")
    ok = wait_for(p, "/free|yours|available/i.test((document.getElementById('c-user-state')||{}).textContent||'')",
                  tries=40, gap=0.4)
    check(ok, "B[%s] username '%s' checks out as free" % (who, uname),
          p.eval("(document.getElementById('c-user-state')||{}).textContent"))
    # ⚠️ THE MODE CHOICE MUST SURVIVE PRESSING 'Is it free?'. The delegated
    # click handler's closest() used to walk past #su-main to the page root
    # <div id="c-main" data-mode="ks3">, so any non-option click inside the
    # form silently overwrote the parent's answer with "ks3" — which is not
    # 'home', so the child was created alongside_school/light whatever the
    # parent chose. MRB-327 §1 finding 1.
    check(p.eval(pressed) == "true",
          "B[%s] the mode choice SURVIVES the username check" % who, p.eval(pressed))
    check(p.eval("document.getElementById('c-continue').disabled") is False,
          "B[%s] Continue is available once the child form is complete" % who)
    check(click(p, "#c-continue") == "clicked", "B[%s] Continue clicked" % who)
    return uname


def pick_unit(p, who, skip=False):
    ok = wait_for(p, "!!document.getElementById('u-save') || !!document.getElementById('u-skip')",
                  tries=60, gap=0.5)
    check(ok, "B[%s] unit picker step renders" % who, text(p)[:200].replace("\n", " "))
    if not ok:
        return None
    n = p.eval("document.querySelectorAll('[data-unit]').length")
    check(n > 0, "B[%s] unit picker lists units from GET /children/:id/picker" % who, n)
    if skip or not n:
        check(click(p, "#u-skip") == "clicked", "B[%s] 'start from the beginning' taken" % who)
        return None
    unit = p.eval("document.querySelectorAll('[data-unit]')[%d].getAttribute('data-unit')" % min(2, n - 1))
    check(click(p, '[data-unit=%s]' % json.dumps(unit)) == "clicked", "B[%s] unit '%s' chosen" % (who, unit))
    time.sleep(0.3)
    check(click(p, "#u-save") == "clicked", "B[%s] unit saved" % who)
    return unit


def phase_b(p, ids):
    print("\n── B · signup through the real page ──────────────────────")
    # ⚠️ NOT the usual @mrbadmus-test.com fixture domain. That domain has no MX
    # record, and GoTrue's own address validation refuses it on the CLIENT
    # signup path with 'Email address "…" is invalid'. The other drives never
    # met it because they make users through the admin API, which does not
    # validate. A real parent's address has MX; this one does too.
    email = "l1-parent-%d@mailinator.com" % int(time.time())
    ids["parent_email"] = email
    save(ids)

    clear_session(p)
    p.goto(qs("/consumer/signup.html"), settle=1.8)
    check("Not found" not in text(p)[:200], "B signup.html renders with the flag on",
          text(p)[:120].replace("\n", " "))
    check(not errs(p), "B signup account step: zero console errors", errs(p))

    # ── account step ──
    check(p.eval("document.getElementById('continue').disabled") is True,
          "B Continue is disabled before the terms box is ticked")
    setval(p, "#email", email)
    setval(p, "#password", PARENT_PW)
    # ⚠️ HARNESS NOTE, not a product finding: #terms sits INSIDE <label
    # id="terms-row">, and a synthetic .click() on an input inside its own
    # label is re-dispatched by the label — it toggles twice and lands back
    # off. A real pointer click does not. Tick it the way a person does.
    check(p.eval("(function(){var b=document.getElementById('terms');b.checked=true;"
                 "b.dispatchEvent(new Event('change',{bubbles:true}));return b.checked;})()") is True,
          "B terms ticked")
    time.sleep(0.3)
    check(p.eval("document.getElementById('continue').disabled") is False,
          "B Continue enables once terms are ticked")
    shot(p, "B1-signup-account.png", width=1200, height=900)
    check(click(p, "#continue") == "clicked", "B Continue clicked — signUp fires")

    ok = wait_for(p, "/check your (email|inbox)|sent you|verify/i.test(document.body.innerText)",
                  tries=40, gap=0.5)
    at = text(p)
    shot(p, "B2-signup-verify-wait.png", width=1200, height=900)

    # who did signUp actually make?
    st, users = sb_admin("GET", "/auth/v1/admin/users?per_page=1000")
    row = next((u for u in users["users"] if u["email"] == email), None)
    if row:
        check(ok, "B the verify-your-email step is shown", at[:220].replace("\n", " "))
        check(True, "B signUp created the parent account through the page", email)
    else:
        # GoTrue refused the signup. That is a real thing to observe: the drive
        # asserts the page SAYS so in words rather than sitting there, then
        # makes the account the way an admin would and carries on, so the rest
        # of the journey is still driven.
        check(not errs_hard(p), "B a refused signUp does not throw in the console", errs(p))
        low = at.lower()
        check(("couldn" in low or "can" in low) and "try again" in low,
              "B a refused signUp is explained on screen, in words",
              at[:400].replace("\n", " "))
        # MRB-327 §1 finding 2: GoTrue's own wording must not reach the parent.
        check("rate limit" not in low and "gotrue" not in low and "400" not in at,
              "B the refusal is OUR words, not the auth server's internal string",
              at[:400].replace("\n", " "))
        note("REAL signUp refused by GoTrue — on-screen: %r" % at[at.find("Password"):][:160])
        st, made = sb_admin("POST", "/auth/v1/admin/users",
                            {"email": email, "password": PARENT_PW, "email_confirm": False,
                             "user_metadata": {"account_type": "parent"}})
        check(st < 300, "B fallback: the account was made through the admin API instead", (st, made))
        st, users = sb_admin("GET", "/auth/v1/admin/users?per_page=1000")
        row = next((u for u in users["users"] if u["email"] == email), None)
    check(row is not None, "B the parent auth user exists", email)
    if not row:
        raise SystemExit("no parent user")
    ids["parent"] = row["id"]
    ids["users"] = [row["id"]]
    save(ids)
    check(not row.get("email_confirmed_at"),
          "B the account starts UNconfirmed — verification is a real step",
          row.get("email_confirmed_at"))

    # ── verification: redeem the link GoTrue would have emailed ──
    #
    # ⚠️ DRIVE MECHANISM. The TEST project's Redirect-URL allow-list does not
    # contain this drive's static server, so GoTrue's own /verify redirect
    # lands on SITE_URL and never reaches the page under test. So the token is
    # redeemed against GoTrue directly — a REAL single-use signup token, from
    # the real generate_link — and verify.html is then entered on exactly the
    # implicit-flow fragment GoTrue would have produced. The page's own code
    # path (supabase-js detectSessionInUrl → family/ensure → hand-off) is the
    # one being driven; only the hop is synthesised.
    st, link = sb_admin("POST", "/auth/v1/admin/generate_link",
                        {"type": "signup", "email": email, "password": PARENT_PW})
    check(st < 300 and link.get("hashed_token"), "B a real verification token was issued", (st, link))
    st2, sess0 = http("POST", SB + "/auth/v1/verify",
                      {"type": "signup", "token_hash": link["hashed_token"]},
                      {"apikey": ANON})
    check(st2 == 200 and sess0.get("access_token"),
          "B redeeming the verification token returns a session", (st2, sess0))
    frag = ("#access_token=%s&refresh_token=%s&expires_in=3600&token_type=bearer&type=signup"
            % (sess0["access_token"], sess0["refresh_token"]))
    # A real parent opens the link in the SAME browser: no session yet, but the
    # signup draft (email, terms, any held children) is still in localStorage.
    # Clearing all of it here would quietly change the journey under test.
    p.eval("localStorage.removeItem('sb-qeppkiswvclkkwbxmlok-auth-token')")
    p.goto(BASE + "/consumer/verify.html?env=test&api=" + API + frag, settle=2.5)
    ok = wait_for(p, "/verified|Setting your family/i.test(document.body.innerText) || "
                     "(location.pathname.indexOf('/consumer/')===0 && location.pathname!=='/consumer/verify.html')",
                  tries=50, gap=0.5)
    vt = text(p)
    check(ok, "B verify.html accepted the link", vt[:220].replace("\n", " "))
    check("couldn't verify" not in vt.lower() and "isn't verified" not in vt.lower()
          and "refused to connect" not in vt.lower(),
          "B verify.html did NOT fall to a failure state", vt[:220].replace("\n", " "))
    check(not errs(p), "B verify.html: zero console errors", errs(p))
    shot(p, "B3-verify.png", width=1200, height=900)

    st, users = sb_admin("GET", "/auth/v1/admin/users?per_page=1000")
    row = next((u for u in users["users"] if u["email"] == email), None)
    check(bool(row.get("email_confirmed_at")), "B the account is now confirmed in the database",
          row.get("email_confirmed_at"))

    # verify.html hands off to signup step=child (draft has no children yet) or overview
    time.sleep(2.0)
    where = p.eval("location.pathname + location.search")
    note("verify.html landed on " + where)
    ids["org"] = None

    # ── children ──
    if "/consumer/signup.html" not in where:
        # settle() with a verified session and no children lands on 'child'
        # by itself; no ?step= is needed and ?step= is ignored until verified.
        p.goto(qs("/consumer/signup.html"), settle=2.5)
    ok = wait_for(p, "!!document.getElementById('c-name')", tries=50, gap=0.4)
    check(ok, "B signup resumes at the child step after verification",
          text(p)[:200].replace("\n", " "))

    u8 = fill_child(p, ids, "y8", "Amara", 8, "school")
    shot(p, "B4-child-y8.png", width=1200, height=1100)
    pick_unit(p, "y8")

    ok = wait_for(p, "!!document.getElementById('add-another')", tries=60, gap=0.5)
    check(ok, "B the children list step renders after the first child",
          text(p)[:220].replace("\n", " "))
    check(click(p, "#add-another") == "clicked", "B 'Add another child' clicked")
    u10 = fill_child(p, ids, "y10", "Tobi", 10, "home", route="Triple", tier="Higher")
    shot(p, "B5-child-y10.png", width=1200, height=1100)
    pick_unit(p, "y10")

    ok = wait_for(p, "!!document.getElementById('to-plan')", tries=60, gap=0.5)
    check(ok, "B the children list shows both children",
          text(p)[:300].replace("\n", " "))
    lt = text(p)
    check("Amara" in lt and "Tobi" in lt, "B both children are named on the list step",
          lt[:300].replace("\n", " "))
    shot(p, "B6-children-list.png", width=1200, height=1100)

    # what the API actually made
    sess = sign_in(email, PARENT_PW)
    jwt = sess["access_token"]
    st, fam = api("GET", "/api/consumer/family", jwt)
    check(st == 200, "B GET /api/consumer/family → 200", st)
    ids["org"] = (fam.get("family") or {}).get("id")
    kids = fam.get("children") or []
    check(len(kids) == 2, "B the family has exactly two children", len(kids))
    for k in kids:
        ids.setdefault("kids", []).append({"id": k["id"], "name": k.get("first_name") or k.get("name")})
        ids["users"].append(k["id"])
    save(ids)

    check((fam.get("parent") or {}).get("terms_accepted_at") is not None,
          "B ticking the terms box is RECORDED against the account",
          (fam.get("parent") or {}).get("terms_accepted_at"))

    st, prof = sb_admin("GET", "/rest/v1/profiles?select=id,first_name,year_group,key_stage,tier,"
                               "science_pathway,mode,intensity,username&created_by=eq." + ids["parent"])
    by = {r["first_name"]: r for r in (prof or [])}
    a, t10 = by.get("Amara"), by.get("Tobi")
    check(a and str(a["year_group"]) == "8" and a["key_stage"] == "KS3"
          and a["mode"] == "alongside_school",
          "B Amara: Year 8, KS3, alongside_school", a)
    check(t10 and str(t10["year_group"]) == "10" and t10["key_stage"] == "KS4"
          and t10["tier"] == "higher" and t10["science_pathway"] == "triple"
          and t10["mode"] == "home_education",
          "B Tobi: Year 10, KS4, Triple, Higher, home_education", t10)
    ids["amara"] = a["id"] if a else None
    ids["tobi"] = t10["id"] if t10 else None
    ids["amara_user"] = a["username"] if a else u8
    ids["tobi_user"] = t10["username"] if t10 else u10
    save(ids)

    # ── the plan step ──
    check(click(p, "#to-plan") == "clicked", "B 'Choose a plan' clicked")
    ok = wait_for(p, "!!document.getElementById('to-stripe')", tries=40, gap=0.4)
    check(ok, "B the plan step renders", text(p)[:250].replace("\n", " "))
    pt = text(p)
    check("£" in pt, "B the plan step shows real prices from GET /api/consumer/pricing",
          pt[:250].replace("\n", " "))
    check(not errs(p), "B plan step: zero console errors", errs(p))
    shot(p, "B7-plan.png", width=1200, height=1000)
    check(click(p, '[data-plan="month"]') == "clicked", "B monthly plan chosen")
    time.sleep(0.3)
    return jwt


# ══════════════════════════════════════════════════════════════════════════
# C — Stripe checkout, for real, in test mode
# ══════════════════════════════════════════════════════════════════════════
def stripe_form(method, path, fields):
    body = "&".join("%s=%s" % (k, urllib.parse.quote(str(v))) for k, v in fields)
    req = urllib.request.Request("https://api.stripe.com/v1" + path, data=body.encode(),
                                 method=method,
                                 headers={"Authorization": "Bearer " + env("STRIPE_SECRET_KEY"),
                                          "Content-Type": "application/x-www-form-urlencoded"})
    try:
        with urllib.request.urlopen(req, context=CTX, timeout=60) as r:
            return r.status, json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        return e.code, json.loads(e.read().decode())


def stripe_subscribe(ids, jwt):
    """Make the subscription Stripe Checkout would have made, on the customer
    the checkout call already created. Same price, same quantity, same trial,
    same org_id metadata — so the webhook path under test is the real one."""
    st, sub = sb_admin("GET", "/rest/v1/subscriptions?select=stripe_customer_id&org_id=eq." + ids["org"])
    cus = sub[0]["stripe_customer_id"] if sub else None
    if not cus:
        check(False, "C no Stripe customer to subscribe", sub)
        return False
    st, pm = stripe_form("POST", "/payment_methods", [("type", "card"), ("card[token]", "tok_visa")])
    if st >= 300:
        note("stripe payment_methods: %s %s" % (st, pm))
        return False
    st, _ = stripe_form("POST", "/payment_methods/%s/attach" % pm["id"], [("customer", cus)])
    stripe_form("POST", "/customers/" + cus,
                [("invoice_settings[default_payment_method]", pm["id"])])
    st, s = stripe_form("POST", "/subscriptions", [
        ("customer", cus), ("items[0][price]", env("STRIPE_PRICE_MONTHLY")),
        ("items[0][quantity]", 2), ("trial_period_days", 7),
        ("metadata[org_id]", ids["org"]), ("default_payment_method", pm["id"])])
    if st >= 300:
        note("stripe subscriptions: %s %s" % (st, s))
        return False
    ids["stripe_sub"] = s["id"]
    ids["stripe_customer"] = cus
    save(ids)
    print("  stripe subscription created", s["id"], s["status"])

    # ⚠️ The event is delivered to the backend HERE rather than left to
    # `stripe listen`. Six lanes share one Stripe test account tonight, and the
    # CLI multiplexes ONE endpoint across every connected listener — so an
    # event for this family is as likely to be handed to another lane's
    # backend as to this one (observed: our customer.created went to :3151).
    # A listener left running would also be eating other lanes' events. So the
    # REAL event object is fetched from Stripe and posted to the real handler
    # with a real signature over STRIPE_WEBHOOK_SECRET. The handler, the
    # signature check and the database write are all the shipped ones; only
    # the transport is ours.
    for _ in range(10):
        st, evs = stripe_form("GET", "/events?limit=40", [])
        want = [e for e in (evs.get("data") or [])
                if e["type"] in ("customer.subscription.created", "customer.subscription.updated")
                and ((e.get("data") or {}).get("object") or {}).get("id") == s["id"]]
        if want:
            for e in reversed(want):
                code = deliver_event(e)
                print("  delivered", e["type"], "->", code)
            break
        time.sleep(1.0)
    return True


def deliver_event(event):
    import hmac, hashlib
    secret = env("STRIPE_WEBHOOK_SECRET")
    payload = json.dumps(event, separators=(",", ":")).encode()
    ts = str(int(time.time()))
    sig = hmac.new(secret.encode(), (ts + ".").encode() + payload, hashlib.sha256).hexdigest()
    req = urllib.request.Request(API + "/api/consumer/stripe/webhook", data=payload,
                                 method="POST",
                                 headers={"Content-Type": "application/json",
                                          "Stripe-Signature": "t=%s,v1=%s" % (ts, sig)})
    try:
        with urllib.request.urlopen(req, timeout=40) as r:
            return r.status
    except urllib.error.HTTPError as e:
        return "%s %s" % (e.code, e.read().decode()[:160])


def phase_c(p, ids, jwt):
    print("\n── C · Stripe test-mode checkout ─────────────────────────")
    check(click(p, "#to-stripe") == "clicked", "C 'Add a card' clicked — POST /api/consumer/checkout")
    ok = wait_for(p, "location.host.indexOf('stripe.com') >= 0", tries=60, gap=0.5)
    check(ok, "C the browser reached Stripe Checkout", p.eval("location.href")[:120])
    if not ok:
        check(False, "C checkout could not start", text(p)[:300].replace("\n", " "))
        return False
    time.sleep(4.0)
    shot(p, "C1-stripe-checkout.png", width=1200, height=1100)

    # Stripe's hosted checkout renders the card fields directly on the page.
    for sel, val in (("#cardNumber", "4242424242424242"), ("#cardExpiry", "12 / 30"),
                     ("#cardCvc", "123"), ("#billingName", "Funmi Test"),
                     ("#billingPostalCode", "SW1A 1AA")):
        r = setval(p, sel, val)
        if r == "no-el":
            note("Stripe checkout: %s absent (layout varies by account)" % sel)
    time.sleep(0.6)
    r = p.eval("(function(){var b=document.querySelector('.SubmitButton')||"
               "document.querySelector('button[type=\"submit\"]');"
               "if(!b) return 'no-btn'; b.click(); return 'clicked';})()")
    check(r == "clicked", "C Stripe's pay button pressed", r)

    ok = wait_for(p, "location.host.indexOf('stripe.com') < 0", tries=60, gap=1.0)
    landed = p.eval("location.href")
    sid = None
    m = re.search(r"session_id=([^&]+)", landed or "")
    if m:
        sid = m.group(1)
    if ok:
        check(True, "C Stripe redirected back off its own domain", landed[:160])
        check(bool(sid), "C the return carries a Stripe session id", landed[:160])
    else:
        # ⚠️ NOT a product defect, and it must be said plainly. The card form
        # accepts every field (screenshot C1b) and then Stripe's own hosted
        # page answers "There was an error processing your request." — its bot
        # protection refusing an automated browser, on Stripe's side of the
        # seam. So the CARD leg cannot be completed here. Everything on OUR
        # side of it can: the subscription Checkout would have created is made
        # through the Stripe API on the same customer, with the same price,
        # quantity, trial and org_id metadata, which makes the real webhook
        # fire for real over `stripe listen`.
        err = p.eval("(function(){var e=Array.prototype.filter.call("
                     "document.querySelectorAll('*'),function(x){return x.children.length===0 && "
                     "/error processing|declined|try again/i.test(x.textContent||'');})[0];"
                     "return e?e.textContent:'';})()")
        shot(p, "C1b-stripe-refused.png", width=1200, height=1300)
        note("Stripe's hosted page refused the automated submit: %r — the card leg is "
             "NOT driven; the subscription is made through the Stripe API instead" % (err or "")[:120])
        check(stripe_subscribe(ids, jwt), "C the subscription Checkout would have made is created")
    save(ids)

    # ⚠️ DRIVE MECHANISM, not a product finding: FRONTEND_ORIGIN in the backend
    # .env is http://localhost:5500, so Stripe's success_url points there and
    # not at this drive's static server. Re-enter the SAME return page on this
    # server, with the same query, so the page under test is the built one and
    # ?api= still points at this backend.
    p.goto(qs("/consumer/checkout-return.html?state=success" + ("&session_id=" + sid if sid else "")), settle=2.0)
    ok = wait_for(p, "/first week is ready|payment went through/i.test(document.body.innerText)",
                  tries=120, gap=1.0)
    rt = text(p)
    check(ok, "C checkout-return.html settles", rt[:300].replace("\n", " "))
    check("first week is ready" in rt.lower(),
          "C the return page reaches the WELCOME state, not the still-waiting fallback",
          rt[:400].replace("\n", " "))
    check("Amara" in rt and "Tobi" in rt, "C the return page names both children",
          rt[:400].replace("\n", " "))
    check(ids["amara_user"] in rt and ids["tobi_user"] in rt,
          "C the return page hands over both usernames",
          rt[-500:].replace("\n", " "))
    check("still being set" not in rt and "couldn't read this week" not in rt,
          "C the return page shows real sessions, not the empty-week fallback",
          rt[:600].replace("\n", " "))
    check(not errs(p), "C checkout-return.html: zero console errors", errs(p))
    shot(p, "C2-checkout-return.png", width=1200, height=1400)

    st, bill = api("GET", "/api/consumer/billing", jwt)
    check(st == 200 and bill["billing"]["state"] in ("trialing", "active"),
          "C the subscription really is live in our database", bill.get("billing"))
    st, sub = sb_admin("GET", "/rest/v1/subscriptions?select=stripe_customer_id,stripe_subscription_id,"
                              "status,quantity&org_id=eq." + ids["org"])
    check(sub and sub[0].get("stripe_subscription_id"),
          "C the webhook wrote the Stripe subscription id back", sub)
    check(sub and sub[0].get("quantity") == 2, "C the seat quantity is 2, one per child", sub)
    if sub:
        ids["stripe_customer"] = sub[0].get("stripe_customer_id")
        ids["stripe_sub"] = sub[0].get("stripe_subscription_id")
        save(ids)
    return True


# ══════════════════════════════════════════════════════════════════════════
# D — a week for both children, off the right scheme
# ══════════════════════════════════════════════════════════════════════════
def phase_d(ids, jwt):
    print("\n── D · a week for both children ──────────────────────────")
    wk = monday()
    for kid in ("amara", "tobi"):
        st, g = api("POST", "/api/consumer/children/%s/generate" % ids[kid], jwt, {"week_start": wk})
        check(st == 200, "D generate is idempotent for %s (already run by the return page)" % kid, (st, g))
    st, rows = sb_admin("GET", "/rest/v1/work_items?select=child_id,kind,title,ref,scheduled_for,minutes,status"
                               "&org_id=eq." + ids["org"] + "&week_start=eq." + wk + "&order=scheduled_for,position")
    check(st < 300, "D work_items read", st)
    rows = rows or []
    per = {}
    for r in rows:
        per.setdefault(r["child_id"], []).append(r)
    check(len(per.get(ids["amara"], [])) > 0, "D Amara (Y8) has work_items rows",
          len(per.get(ids["amara"], [])))
    check(len(per.get(ids["tobi"], [])) > 0, "D Tobi (Y10) has work_items rows",
          len(per.get(ids["tobi"], [])))

    def hrefs(cid):
        return [((r.get("ref") or {}).get("href") or "") for r in per.get(cid, [])
                if r["kind"] == "lesson"]

    a_h, t_h = hrefs(ids["amara"]), hrefs(ids["tobi"])
    check(bool(a_h) and all(h.startswith("/ks3/") for h in a_h),
          "D every Amara lesson comes off the KS3 scheme of work", a_h[:4])
    check(bool(t_h) and all(re.match(r"^/(combined|triple)/", h) for h in t_h),
          "D every Tobi lesson comes off the KS4 scheme of work", t_h[:4])
    check(bool(t_h) and all(h.startswith("/triple/") for h in t_h),
          "D Tobi's KS4 lessons are the TRIPLE pathway he was signed up for", t_h[:4])
    # every href a child is about to tap must actually be a page in the built
    # tree — a scheme row pointing at a file that was never generated is a
    # dead end the child meets and nobody else ever does.
    dead = []
    for h in a_h + t_h:
        try:
            with urllib.request.urlopen(BASE + h.split("#")[0], timeout=20) as r:
                if r.status != 200:
                    dead.append((h, r.status))
        except Exception as e:
            dead.append((h, str(e)))
    check(not dead, "D every generated lesson link resolves to a real page in the built tree", dead)

    kinds = {}
    for cid, rs in per.items():
        kinds[cid] = sorted(set(r["kind"] for r in rs))
    note("work kinds — Amara %s / Tobi %s" % (kinds.get(ids["amara"]), kinds.get(ids["tobi"])))
    check("practice" in (kinds.get(ids["amara"]) or []),
          "D the KS3 child gets practice items", kinds.get(ids["amara"]))
    ids["week"] = wk
    save(ids)
    return per


# ══════════════════════════════════════════════════════════════════════════
# E — child login at /go/
# ══════════════════════════════════════════════════════════════════════════
def phase_e(p, ids):
    print("\n── E · child login at /go/ ───────────────────────────────")
    out = {}
    for kid, uname in (("amara", ids["amara_user"]), ("tobi", ids["tobi_user"])):
        clear_session(p)
        p.goto(qs("/go/index.html"), settle=1.5)
        gt = text(p).replace("\u2019", "'").lower()
        check("who's this" in gt,
              "E /go/ renders the child sign-in for %s" % kid, text(p)[:140].replace("\n", " "))
        setval(p, "#gl-user", uname)
        setval(p, "#gl-pass", CHILD_PW)
        p.eval("document.querySelector('#gl-go').click()")
        ok = wait_for(p, "location.pathname === '/consumer/today.html'", tries=50, gap=0.4)
        check(ok, "E %s signs in and lands on Today" % kid,
              (p.eval("location.pathname"), p.eval("(document.getElementById('gl-error')||{}).textContent")))
        if ok:
            # bank the session the page just made, so nothing after this
            # spends another attempt against the child-login rate limiter
            raw = p.eval("localStorage.getItem('sb-qeppkiswvclkkwbxmlok-auth-token')")
            try:
                sess = json.loads(raw)
                if isinstance(sess, dict) and sess.get("access_token"):
                    ids.setdefault("sess", {})[kid] = sess
                    out[kid] = sess
            except Exception:
                pass
            save(ids)
        check(not errs(p), "E %s login: zero console errors" % kid, errs(p))
        if kid == "amara":
            shot(p, "E1-go-login.png", width=390, height=800)
    # a wrong password says the one generic thing
    clear_session(p)
    p.goto(qs("/go/index.html"), settle=1.2)
    setval(p, "#gl-user", ids["amara_user"])
    setval(p, "#gl-pass", "definitely-not-it")
    p.eval("document.querySelector('#gl-go').click()")
    ok = wait_for(p, "!document.getElementById('gl-error').hidden", tries=40, gap=0.4)
    msg = p.eval("(document.getElementById('gl-error')||{}).textContent")
    check(ok and "don" in (msg or "").lower(), "E a wrong password shows the generic refusal", msg)
    return out


# ══════════════════════════════════════════════════════════════════════════
# F1 — Today, work still to do
# ══════════════════════════════════════════════════════════════════════════
def child_session(ids, kid):
    """⚠️ REUSE, do not re-log-in. `/api/consumer/child/login` is rate limited
    at 10 attempts per IP per 15 minutes AND 10 per username — correctly, it
    is the brute-force surface of the whole product. A drive that signs a
    child in once per phase trips its own product's protection and then
    reports it as a failure. Phase E banks the session the PAGE obtained;
    everything after it reuses that."""
    cache = ids.setdefault("sess", {})
    s = cache.get(kid)
    if s and s.get("expires_at", 0) > time.time() + 120:
        return s, s["access_token"]
    st, cl = api("POST", "/api/consumer/child/login", None,
                 {"username": ids[kid + "_user"], "password": CHILD_PW})
    assert st == 200, (st, cl)
    s = sess_from_child(cl)
    cache[kid] = s
    save(ids)
    return s, s["access_token"]


def phase_f1(p, ids, sess):
    print("\n── F1 · Today — work still to do ─────────────────────────")
    with_session(p, sess)
    p.goto(qs("/consumer/today.html"), settle=2.0)
    ok = wait_for(p, "document.querySelectorAll('#td-items .td-item').length > 0", tries=50, gap=0.4)
    t = text(p)
    check(ok, "F1 Today lists this week's items", t[:300].replace("\n", " "))
    check("Amara" in t, "F1 Today greets the child by name", t[:120].replace("\n", " "))
    check("Nothing set for today" not in t and "Nothing new right now" not in t,
          "F1 Today is in the work-to-do state, not an empty one", t[:200].replace("\n", " "))
    n = p.eval("document.querySelectorAll('#td-items .td-item').length")
    dn = p.eval("document.querySelectorAll('#td-items .td-done-btn').length")
    check(dn > 0, "F1 every unfinished item offers 'Mark as done'", (n, dn))
    check(p.eval("document.querySelectorAll('#td-items .td-done-btn[disabled]').length") == 0,
          "F1 the done controls are enabled on a paid-up account")
    check(not errs(p), "F1 Today: zero console errors", errs(p))
    shot(p, "F1-today-work.png", width=390, height=1100)
    return n


# ══════════════════════════════════════════════════════════════════════════
# G — a lesson, a practice item, a unit check
# ══════════════════════════════════════════════════════════════════════════
def phase_g(p, ids, sess, jwt):
    print("\n── G · a lesson, a practice item, a unit check ───────────")
    with_session(p, sess)
    p.goto(qs("/consumer/today.html"), settle=2.0)
    wait_for(p, "document.querySelectorAll('#td-items .td-item').length > 0", tries=50, gap=0.4)

    # ── a lesson: follow the link the row actually carries ──
    href = p.eval("""(function(){var a=document.querySelector('#td-items a.td-item-top');
        return a ? a.getAttribute('href') : null;})()""")
    check(bool(href), "G the first Today row is a real link", href)
    if href:
        p.goto(BASE + href, settle=2.0)
        lt = text(p)
        code = p.eval("document.title")
        check(len(lt.strip()) > 200 and "404" not in code,
              "G the lesson page a child taps actually opens", (href, code, lt[:120].replace("\n", " ")))
        shot(p, "G1-lesson.png", width=390, height=1200)

    # ── a practice item: mark one done and watch the count fall ──
    with_session(p, sess)
    p.goto(qs("/consumer/today.html"), settle=2.0)
    wait_for(p, "document.querySelectorAll('#td-items .td-item').length > 0", tries=50, gap=0.4)
    before = p.eval("document.querySelectorAll('#td-items .td-done-btn').length")
    idx = p.eval("""(function(){var b=document.querySelectorAll('#td-items .td-item');
        for (var i=0;i<b.length;i++){ if(b[i].innerText.indexOf('Practice')>=0) return i; } return -1;})()""")
    check(idx >= 0, "G a practice item is on Today", idx)
    p.eval("""(function(){var b=document.querySelectorAll('#td-items .td-item')[%d];
        var d=b && b.querySelector('.td-done-btn'); if(d) d.click();})()""" % max(idx, 0))
    ok = wait_for(p, "document.querySelectorAll('#td-items .td-done-btn').length === %d" % (before - 1),
                  tries=50, gap=0.5)
    check(ok, "G 'Mark as done' takes the item out of the to-do list",
          p.eval("document.querySelectorAll('#td-items .td-done-btn').length"))
    st, done = sb_admin("GET", "/rest/v1/work_items?select=id,kind,status&org_id=eq." + ids["org"]
                        + "&child_id=eq." + ids["amara"] + "&status=eq.done")
    check(bool(done), "G the done state is in the database, not just on screen", done)
    check(not errs(p), "G Today after marking done: zero console errors", errs(p))

    # ── a unit check, all the way to the practice run ──
    st, uc = api("GET", "/api/consumer/child/unit-check", None, None) if False else (0, None)
    unit = None
    st, items = sb_admin("GET", "/rest/v1/work_items?select=kind,ref,title&org_id=eq." + ids["org"]
                         + "&child_id=eq." + ids["amara"] + "&kind=eq.unit_check")
    if items:
        unit = (items[0].get("ref") or {}).get("unit_code")
    if not unit:
        st, items = sb_admin("GET", "/rest/v1/work_items?select=kind,ref&org_id=eq." + ids["org"]
                             + "&child_id=eq." + ids["amara"] + "&kind=eq.lesson")
        for r in (items or []):
            if (r.get("ref") or {}).get("unit_code"):
                unit = r["ref"]["unit_code"]
                break
    check(bool(unit), "G a unit code is available for the unit check", unit)
    if not unit:
        return
    with_session(p, sess)
    p.goto(qs("/consumer/unit-check.html?unit=" + unit), settle=2.5)
    ok = wait_for(p, "!!document.getElementById('uc-start')", tries=60, gap=0.5)
    check(ok, "G unit-check start screen renders for %s" % unit, text(p)[:250].replace("\n", " "))
    check(not errs(p), "G unit-check start: zero console errors", errs(p))
    shot(p, "G2-unitcheck-start.png", width=390, height=1000)
    if not ok:
        return
    check(click(p, "#uc-start") == "clicked", "G 'Start the clock' pressed")
    ok = wait_for(p, "document.querySelectorAll('#uc-progress [data-jump]').length > 0", tries=60, gap=0.5)
    check(ok, "G the check starts and the progress bar appears",
          text(p)[:250].replace("\n", " "))
    if not ok:
        return
    total = p.eval("document.querySelectorAll('#uc-progress [data-jump]').length")
    note("unit check %s has %d questions" % (unit, total))
    for i in range(total):
        answered = p.eval("""(function(){
            var o=document.querySelector('#uc-options .ks3-option'); if(o){o.click(); return 'opt';}
            var t=document.getElementById('uc-typed'); if(t){
              var d=Object.getOwnPropertyDescriptor(HTMLInputElement.prototype,'value');
              d.set.call(t,'42'); t.dispatchEvent(new Event('input',{bubbles:true})); return 'typed';}
            return 'none';})()""")
        time.sleep(0.35)
        if i < total - 1:
            p.eval("(document.getElementById('uc-next')||{click:function(){}}).click()")
            time.sleep(0.35)
    check(answered != "none", "G every question offered an answer control", answered)
    ok = wait_for(p, "!!document.getElementById('uc-finish')", tries=20, gap=0.3)
    check(ok, "G the last question offers 'Hand in'")
    p.eval("(document.getElementById('uc-finish')||{click:function(){}}).click()")
    ok = wait_for(p, "!!document.querySelector('.uc-pct')", tries=60, gap=0.5)
    rt = text(p)
    check(ok, "G the unit check reaches its RESULT screen", rt[:300].replace("\n", " "))
    check(bool(p.eval("(document.querySelector('.uc-score-line')||{}).textContent")),
          "G the result screen states the score in words",
          p.eval("(document.querySelector('.uc-score-line')||{}).textContent"))
    check(p.eval("document.querySelectorAll('.uc-review li').length") > 0,
          "G the result screen reviews every question",
          p.eval("document.querySelectorAll('.uc-review li').length"))
    check(not errs(p), "G unit-check result: zero console errors", errs(p))
    shot(p, "G3-unitcheck-result.png", width=390, height=1600)
    st, att = sb_admin("GET", "/rest/v1/unit_check_attempts?select=id,unit_code,score,max_score,"
                              "is_record&child_id=eq." + ids["amara"])
    check(st < 300 and isinstance(att, list) and att,
          "G the attempt is recorded in unit_check_attempts", (st, att))
    if isinstance(att, list) and att:
        onscreen = re.search(r"(\d+) of (\d+) correct",
                             p.eval("(document.querySelector('.uc-score-line')||{}).textContent") or "")
        check(onscreen and int(onscreen.group(1)) == att[0]["score"]
              and int(onscreen.group(2)) == att[0]["max_score"],
              "G the score on screen is the score in the database",
              (onscreen.groups() if onscreen else None, att[0]))

    # ── the practice run it offers ──
    check(p.eval("!!document.getElementById('uc-again')"),
          "G the result screen offers a practice run",
          rt[-300:].replace("\n", " "))
    check(click(p, "#uc-again") == "clicked", "G 'Practice again' pressed")
    ok = wait_for(p, "document.querySelectorAll('#uc-progress [data-jump]').length > 0 "
                     "|| !!document.getElementById('uc-start')", tries=60, gap=0.5)
    check(ok, "G the practice run actually starts a second attempt",
          text(p)[:250].replace("\n", " "))
    started = p.eval("document.querySelectorAll('#uc-progress [data-jump]').length > 0")
    if not started:
        # some builds return to the start screen and want a second press
        click(p, "#uc-start")
        started = wait_for(p, "document.querySelectorAll('#uc-progress [data-jump]').length > 0",
                           tries=40, gap=0.5)
    check(started, "G the practice run puts questions on screen",
          text(p)[:250].replace("\n", " "))
    check(not errs(p), "G practice run: zero console errors", errs(p))
    shot(p, "G4-practice-run.png", width=390, height=1100)


# ══════════════════════════════════════════════════════════════════════════
# H — an exam question, marked, then sent to Mr Badmus
# ══════════════════════════════════════════════════════════════════════════
ANSWER = ("In a solid the particles are packed closely in a fixed regular pattern and can only "
          "vibrate about fixed positions, so a solid keeps its shape and volume. When it is heated "
          "the particles gain energy, the forces between them are overcome and they can slide past "
          "one another, which is why a liquid takes the shape of its container but keeps its volume. "
          "Heating further gives the particles enough energy to escape completely, so in a gas they "
          "are far apart and move quickly in all directions, which is why a gas fills its container.")


def phase_h(p, ids, sess):
    print("\n── H · exam question → instant mark → Mr Badmus ──────────")
    with_session(p, sess)
    p.goto(qs("/consumer/exam.html"), settle=2.5)
    ok = wait_for(p, "document.querySelectorAll('.ex-card[data-open]').length > 0", tries=60, gap=0.5)
    t = text(p)
    check(ok, "H the exam picker lists questions", t[:250].replace("\n", " "))
    check(not errs(p), "H exam picker: zero console errors", errs(p))
    shot(p, "H1-exam-pick.png", width=390, height=1200)
    if not ok:
        return None
    qid = p.eval("document.querySelector('.ex-card[data-open]').getAttribute('data-open')")
    ids["exam_q"] = qid
    p.eval("document.querySelector('.ex-card[data-open]').click()")
    ok = wait_for(p, "!!document.getElementById('ex-answer')", tries=40, gap=0.4)
    check(ok, "H opening a question shows the write screen", text(p)[:200].replace("\n", " "))
    if not ok:
        return None
    check(p.eval("document.getElementById('ex-mark').disabled") is True,
          "H 'Mark my answer' is refused on an empty answer")
    # ⚠️ Write an answer to THE QUESTION THE PAGE OPENED, not a canned one.
    # The stub marker is keyword overlap against the scheme, so a canned
    # answer scores 0 and the whole hits → ticks → admin-checklist chain is
    # never exercised. The answer below is built from this question's own
    # scheme points, which is what a full-marks answer says.
    st, qrow = sb_admin("GET", "/rest/v1/exam_questions?select=marks,scheme&id=eq." + qid)
    pts = [(x.get("text") or "") for x in ((qrow or [{}])[0].get("scheme") or [])]
    answer = " ".join(pts) if pts else ANSWER
    ids["exam_scheme_n"] = len(pts)
    setval(p, "#ex-answer", answer)
    time.sleep(0.4)
    check(p.eval("document.getElementById('ex-mark').disabled") is False,
          "H 'Mark my answer' enables once there is an answer")
    check(click(p, "#ex-mark") == "clicked", "H answer submitted for marking")
    ok = wait_for(p, "!!document.querySelector('.ex-score')", tries=90, gap=0.5)
    rt = text(p)
    check(ok, "H the instant mark comes back", rt[:300].replace("\n", " "))
    if not ok:
        check(False, "H marking failed", p.eval("(document.getElementById('ex-error')||{}).textContent"))
        return None
    score = p.eval("document.querySelector('.ex-score').textContent")
    check(re.match(r"^\d+/\d+$", (score or "").strip()), "H the mark reads as a score out of the total", score)
    got = int((score or "0/0").split("/")[0])
    check(got > 0, "H a scheme-complete answer actually earns marks from the marker", score)
    hits = p.eval("document.querySelectorAll('.ex-point.is-hit').length")
    check(hits == got, "H the ticked scheme points are exactly the marks awarded", (hits, score))
    check(bool(p.eval("(document.querySelector('.ex-note')||{}).textContent")),
          "H the mark carries feedback in words",
          p.eval("(document.querySelector('.ex-note')||{}).textContent"))
    check(p.eval("document.querySelectorAll('.ex-point').length") > 0,
          "H the scheme points are shown", p.eval("document.querySelectorAll('.ex-point').length"))
    check("[object Object]" not in rt, "H no scheme point renders as [object Object]")
    check(not errs(p), "H instant mark: zero console errors", errs(p))
    shot(p, "H2-exam-instant-mark.png", width=390, height=1400)

    st, ans = sb_admin("GET", "/rest/v1/exam_answers?select=id,question_id,ai_score,ai_max,ai_hits,"
                              "ai_model,status&child_id=eq." + ids["amara"] + "&order=created_at.desc")
    check(bool(ans), "H the answer is stored with its AI mark", ans[:1] if ans else ans)
    aid = ans[0]["id"] if ans else None
    ids["answer"] = aid
    save(ids)
    note("marking provider on this run: ai_model=%s (no ANTHROPIC_API_KEY → stub)"
         % (ans[0].get("ai_model") if ans else "?"))

    check(p.eval("!!document.getElementById('ex-send')"), "H a 'Send to Mr Badmus' control is offered")
    check(p.eval("document.getElementById('ex-send').disabled") is False,
          "H 'Send to Mr Badmus' is enabled inside the monthly quota",
          p.eval("(document.querySelector('.ex-quota-out')||{}).textContent"))
    check(click(p, "#ex-send") == "clicked", "H 'Send to Mr Badmus' pressed")
    ok = wait_for(p, "!!document.querySelector('.ex-sent')", tries=60, gap=0.5)
    check(ok, "H the page confirms it went to Mr Badmus", text(p)[-400:].replace("\n", " "))
    check("1 of 2 left" in text(p) or "1 left" in text(p),
          "H the monthly Mr Badmus quota drops on screen", text(p)[:120].replace("\n", " "))
    ans2 = None
    for _ in range(20):
        st, ans2 = sb_admin("GET", "/rest/v1/exam_answers?select=id,status,sent_to_mb_at&id=eq." + (aid or ""))
        if ans2 and ans2[0]["status"] == "sent_to_mb":
            break
        time.sleep(0.5)
    check(ans2 and ans2[0]["status"] == "sent_to_mb" and ans2[0]["sent_to_mb_at"],
          "H the answer is queued for Mr Badmus in the database", ans2)
    check(not errs(p), "H send-to-MB: zero console errors", errs(p))
    shot(p, "H3-exam-sent.png", width=390, height=1400)
    return aid


# ══════════════════════════════════════════════════════════════════════════
# I — the operator marks it, at 390px
# ══════════════════════════════════════════════════════════════════════════
MB_NOTE = "Really clear on the three states — now say what happens to the ENERGY of the particles."


def phase_i(p, ids, aid):
    print("\n── I · the operator marks it at 390px ────────────────────")
    if not aid:
        check(False, "I no answer to mark")
        return
    op = sign_in(*OPERATOR)
    jwt = op["access_token"]
    st, q = api("GET", "/api/consumer/admin/mb-queue", jwt)
    check(st == 200, "I GET /admin/mb-queue as operator → 200", st)
    mine = [x for x in (q.get("pending") or []) if x["id"] == aid]
    check(bool(mine), "I this lane's answer is in the queue", len(q.get("pending") or []))

    with_session(p, op)
    p.set_viewport(390, 820, settle=0.4)
    p.goto(qs("/consumer/admin-queue.html"), settle=2.0)
    ok = wait_for(p, "document.querySelectorAll('.ad-item').length > 0", tries=60, gap=0.5)
    check(ok, "I the marking queue renders", text(p)[:250].replace("\n", " "))
    check(p.eval("getComputedStyle(document.getElementById('sidebar')).display") == "none",
          "I 390px: the desktop sidebar is out of the way")
    check(p.eval("getComputedStyle(document.getElementById('mlist-wrap')).display") != "none",
          "I 390px: the phone picker is in")
    over = p.eval("[document.documentElement.scrollWidth, document.documentElement.clientWidth]")
    check(over[0] <= over[1] + 1, "I 390px: no horizontal page overflow", over)
    check(not errs(p), "I marking queue: zero console errors", errs(p))

    r = p.eval("(function(){var s=document.getElementById('mobile-pick'); if(!s) return 'no-select';"
               "s.value=%s; s.dispatchEvent(new Event('change')); return s.value;})()" % json.dumps(aid))
    check(r == aid, "I 390px: the phone picker selects this lane's answer", r)
    ok = wait_for(p, "document.querySelectorAll('.ad-point').length > 0 || !!document.getElementById('num-score')",
                  tries=40, gap=0.4)
    check(ok, "I the marking pane opens on it", text(p)[:250].replace("\n", " "))
    qt = text(p)
    check("Amara" in qt, "I the operator can see whose answer it is", qt[:200].replace("\n", " "))
    shot(p, "I1-admin-queue-390.png", width=390, height=1400)

    npoints = p.eval("document.querySelectorAll('.ad-point').length")
    if npoints:
        # award one more point than the instant marker did
        p.eval("""(function(){var ps=document.querySelectorAll('.ad-point');
            for(var i=0;i<ps.length;i++){ if(!ps[i].classList.contains('is-on')){ ps[i].click(); return i; } }
            return -1;})()""")
        time.sleep(0.4)
    else:
        p.eval("(function(){var n=document.getElementById('num-score');"
               "var d=Object.getOwnPropertyDescriptor(HTMLInputElement.prototype,'value');"
               "d.set.call(n,'4'); n.dispatchEvent(new Event('input',{bubbles:true}));})()")
        time.sleep(0.3)
    score = p.eval("(document.querySelector('.ad-score')||{}).textContent")
    check(bool(score), "I the operator's score readout is live", score)
    check(p.eval("document.getElementById('send-btn').disabled") is True,
          "I Send is refused before a note is written")
    p.eval("(function(){var n=document.getElementById('note');"
           "var d=Object.getOwnPropertyDescriptor(HTMLTextAreaElement.prototype,'value');"
           "d.set.call(n,%s); n.dispatchEvent(new Event('input',{bubbles:true}));})()" % json.dumps(MB_NOTE))
    time.sleep(0.4)
    check(p.eval("document.getElementById('send-btn').disabled") is False,
          "I Send enables once the note is long enough")
    p.eval("document.getElementById('send-btn').click()")
    ok = wait_for(p, "!Array.prototype.some.call(document.querySelectorAll('.ad-item'),"
                     "function(e){return e.getAttribute('data-id')===%s;})" % json.dumps(aid),
                  tries=60, gap=0.5)
    check(ok, "I the marked answer leaves the queue",
          p.eval("(document.getElementById('send-msg')||{}).textContent"))
    st, row = sb_admin("GET", "/rest/v1/exam_answers?select=status,mb_score,mb_feedback,mb_marked_at"
                              "&id=eq." + aid)
    check(row and row[0]["status"] == "mb_marked" and row[0]["mb_feedback"] == MB_NOTE,
          "I the human mark is in the database, in the operator's own words", row)
    ids["mb_score"] = row[0]["mb_score"] if row else None
    save(ids)
    check(not errs(p), "I marking queue after sending: zero console errors", errs(p))
    p.set_viewport(1200, 1000, settle=0.3)


# ══════════════════════════════════════════════════════════════════════════
# J — the child and the parent both see the mark
# ══════════════════════════════════════════════════════════════════════════
def phase_j(p, ids, sess, jwt):
    print("\n── J · the mark reaches the child and the parent ─────────")
    st, notifs = sb_admin("GET", "/rest/v1/consumer_notifications?select=recipient_id,kind,title,body"
                                 "&org_id=eq." + ids["org"] + "&kind=eq.mb_marked")
    rec = set(n["recipient_id"] for n in (notifs or []))
    check(ids["amara"] in rec, "J the child was notified", sorted(rec))
    check(ids["parent"] in rec, "J the parent was notified", sorted(rec))

    with_session(p, sess)
    p.goto(qs("/consumer/today.html"), settle=2.5)
    ok = wait_for(p, "document.querySelectorAll('#td-flags .td-dark-card').length > 0", tries=50, gap=0.5)
    t = text(p)
    check(ok, "J the child sees the mark on Today", t[:350].replace("\n", " "))
    check("Mr Badmus" in t, "J Today names Mr Badmus as the marker", t[:350].replace("\n", " "))
    check(not errs(p), "J child Today with a mark: zero console errors", errs(p))
    shot(p, "J1-today-marked.png", width=390, height=1200)

    st, answers = api("GET", "/api/consumer/children/%s/answers" % ids["amara"], jwt)
    check(st == 200, "J GET /children/:id/answers as the parent → 200", st)
    got = [a for a in (answers.get("answers") or []) if a.get("id") == ids.get("answer")]
    check(bool(got), "J the parent's answers feed carries the marked answer",
          len(answers.get("answers") or []))
    if got:
        a = got[0]
        check(a.get("mb") or a.get("human") or a.get("mb_score") is not None,
              "J the parent's copy carries the HUMAN mark, not only the instant one", a)

    parent_sess = sign_in(ids["parent_email"], PARENT_PW)
    with_session(p, parent_sess)
    p.goto(qs("/consumer/overview.html?child=%s&view=answers" % ids["amara"]), settle=3.0)
    for _ in range(25):
        t = text(p)
        if "Loading" not in t and len(t.strip()) > 120:
            break
        time.sleep(1.0)
    t = text(p)
    check("Not found" not in t[:200], "J the parent dashboard answers view renders",
          t[:200].replace("\n", " "))
    check("Mr Badmus" in t, "J the parent sees that Mr Badmus marked it", t[:500].replace("\n", " "))
    check(not errs(p), "J parent answers view: zero console errors", errs(p))
    shot(p, "J2-parent-answers.png", width=1200, height=1400)


# ══════════════════════════════════════════════════════════════════════════
# K — chat both ways, live
# ══════════════════════════════════════════════════════════════════════════
def phase_k(ids, jwt, child_tok):
    print("\n── K · chat both ways, live ──────────────────────────────")
    with cdp.Browser() as b1, cdp.Browser() as b2:
        pc = b1.attach()
        pp = b2.attach()
        for pg in (pc, pp):
            pg.send("Page.addScriptToEvaluateOnNewDocument", {"source": FLAG_ON_JS})

        # child on Today, in the chat screen
        sess, _ = child_session(ids, "amara")
        with_session(pc, sess)
        pc.goto(qs("/consumer/today.html"), settle=2.5)
        wait_for(pc, "!!document.getElementById('td-msg-btn')", tries=50, gap=0.4)
        pc.eval("document.getElementById('td-msg-btn').click()")
        ok = wait_for(pc, "!document.getElementById('td-chat').hidden", tries=30, gap=0.3)
        check(ok, "K the child can open the chat screen")
        check(not errs(pc), "K child chat: zero console errors", errs(pc))

        # parent on the chat view
        psess = sign_in(ids["parent_email"], PARENT_PW)
        with_session(pp, psess)
        pp.goto(qs("/consumer/overview.html?child=%s&view=chat" % ids["amara"]), settle=3.0)
        for _ in range(25):
            if "Loading" not in text(pp) and len(text(pp).strip()) > 120:
                break
            time.sleep(1.0)
        check("Not found" not in text(pp)[:200], "K the parent chat view renders",
              text(pp)[:200].replace("\n", " "))
        shot(pp, "K1-parent-chat.png", width=1200, height=1200)

        # ── parent → child, live ──
        msg_p = "Well done on the unit check, Amara. %d" % int(time.time() % 100000)
        st, d = api("POST", "/api/consumer/chat/send", jwt, {"to": ids["amara"], "text": msg_p})
        check(st == 200, "K the parent sends a message", (st, d))
        live = wait_for(pc, "document.body.innerText.indexOf(%s) >= 0" % json.dumps(msg_p),
                        tries=40, gap=0.5)
        check(live, "K the child's open page receives it LIVE, with no reload",
              text(pc)[-400:].replace("\n", " "))
        shot(pc, "K2-child-chat-live.png", width=390, height=1000)

        # ── child → parent, live ──
        msg_c = "Thanks! The gases one was hard. %d" % int(time.time() % 100000)
        setval(pc, "#td-draft", msg_c)
        pc.eval("document.getElementById('td-send').click()")
        ok = wait_for(pc, "document.querySelectorAll('#td-thread .td-bubble-wrap.mine').length > 0",
                      tries=50, gap=0.5)
        check(ok, "K the child's message posts", text(pc)[-300:].replace("\n", " "))
        live2 = wait_for(pp, "document.body.innerText.indexOf(%s) >= 0" % json.dumps(msg_c),
                         tries=40, gap=0.5)
        check(live2, "K the parent's open page receives it LIVE, with no reload",
              text(pp)[-500:].replace("\n", " "))
        shot(pp, "K3-parent-chat-live.png", width=1200, height=1200)
        check(not errs(pc), "K child chat after the exchange: zero console errors", errs(pc))
        check(not errs(pp), "K parent chat after the exchange: zero console errors", errs(pp))

        st, msgs = sb_admin("GET", "/rest/v1/family_messages?select=sender_id,recipient_id,body,text"
                                   "&org_id=eq." + ids["org"])
        check(len(msgs or []) >= 2, "K both messages are stored", len(msgs or []))


# ══════════════════════════════════════════════════════════════════════════
# F2 / F3 — Today's other two states
# ══════════════════════════════════════════════════════════════════════════
def phase_f2(p, ids, sess):
    print("\n── F2 · Today — everything done ──────────────────────────")
    with_session(p, sess)
    p.goto(qs("/consumer/today.html"), settle=2.0)
    wait_for(p, "document.querySelectorAll('#td-items .td-item').length >= 0", tries=30, gap=0.3)
    for _ in range(12):
        n = p.eval("document.querySelectorAll('#td-items .td-done-btn').length")
        if not n:
            break
        p.eval("document.querySelector('#td-items .td-done-btn').click()")
        wait_for(p, "document.querySelectorAll('#td-items .td-done-btn').length < %d" % n,
                 tries=40, gap=0.5)
    left = p.eval("document.querySelectorAll('#td-items .td-done-btn').length")
    check(left == 0, "F2 every item on Today can be marked done", left)
    t = text(p)
    n_items = p.eval("document.querySelectorAll('#td-items .td-item').length")
    n_done = p.eval("document.querySelectorAll('#td-items .td-item.is-done').length")
    check(n_items > 0 and n_done == n_items,
          "F2 every row shows as finished once it is done", (n_done, n_items))
    check("Nothing new right now" not in t,
          "F2 a finished day is NOT dressed as a locked account", t[:300].replace("\n", " "))
    check("day streak" in t and re.search(r"\b1\b[\s\S]{0,30}day streak", t) is not None,
          "F2 finishing the work moves the streak to 1", t[:200].replace("\n", " "))
    check(not errs(p), "F2 Today all-done: zero console errors", errs(p))
    shot(p, "F2-today-alldone.png", width=390, height=1200)
    # ⊕ OBSERVATION, not a failure. `items` on /child/today is everything
    # scheduled_for <= today, done or not — so "everything done" is NOT the
    # empty state. Design drew exactly two empty panels (nothing-today,
    # no-new-work) and no finished-for-the-day one. Recorded so nobody reads
    # the missing panel as a regression.
    note("Today has no separate 'all done' panel — the ticks and the streak are the "
         "acknowledgement; Design drew only nothing-today and no-new-work")

    # ── the genuine 'nothing set' day ──
    # Today is the last day of this week, so no item can be moved LATER inside
    # it. Park the fixture's own rows on next week instead — which is the real
    # state of a family whose week has not started — then put them back.
    wk = ids["week"]
    nxt = time.strftime("%Y-%m-%d", time.localtime(
        time.mktime(time.strptime(wk, "%Y-%m-%d")) + 7 * 86400))
    st, _ = sb_admin("PATCH", "/rest/v1/work_items?org_id=eq." + ids["org"]
                     + "&child_id=eq." + ids["amara"],
                     {"week_start": nxt, "scheduled_for": nxt})
    check(st < 300, "F2b the fixture's week is moved forward", st)
    p.goto(qs("/consumer/today.html"), settle=2.0)
    ok = wait_for(p, "/Nothing set for today/.test(document.body.innerText)", tries=40, gap=0.4)
    t2 = text(p)
    check(ok, "F2b a day with nothing due shows Design's empty-day panel",
          t2[:300].replace("\n", " "))
    check("Fancy an exam question anyway" in t2,
          "F2b the empty day still offers something to do", t2[:300].replace("\n", " "))
    check(p.eval("document.querySelectorAll('#td-items .td-item').length") == 0,
          "F2b and the item list really is empty")
    check(not errs(p), "F2b empty day: zero console errors", errs(p))
    shot(p, "F2b-today-nothing-set.png", width=390, height=1100)
    sb_admin("PATCH", "/rest/v1/work_items?org_id=eq." + ids["org"]
             + "&child_id=eq." + ids["amara"] + "&week_start=eq." + nxt,
             {"week_start": wk, "scheduled_for": wk})


def phase_f3(p, ids, sess):
    print("\n── F3 · Today — locked / read-only ───────────────────────")
    st, _ = sb_admin("PATCH", "/rest/v1/subscriptions?org_id=eq." + ids["org"],
                     {"status": "locked", "locked_at": iso(-86400), "trial_end": None,
                      "current_period_end": iso(-40 * 86400)})
    check(st < 300, "F3 the family is put into the locked state", st)
    time.sleep(17)   # the access cache
    with_session(p, sess)
    p.goto(qs("/consumer/today.html"), settle=2.5)
    ok = wait_for(p, "/Nothing new right now/.test(document.body.innerText)", tries=50, gap=0.5)
    t = text(p)
    check(ok, "F3 a locked account shows Design's read-only panel", t[:350].replace("\n", " "))
    check("subscription" not in t.lower() and "grown-ups" not in t.lower(),
          "F3 the child is NOT shown the commercial copy", t[:400].replace("\n", " "))
    check(p.eval("document.querySelectorAll('#td-items .td-done-btn:not([disabled])').length") == 0,
          "F3 no write control is live on a locked account",
          p.eval("document.querySelectorAll('#td-items .td-done-btn:not([disabled])').length"))
    check(p.eval("document.getElementById('td-draft').disabled") is True,
          "F3 the chat composer is disabled too")
    check(p.eval("document.querySelectorAll('#td-items .td-item').length") > 0,
          "F3 the finished work really is still there, as the copy promises")
    check(not errs(p), "F3 locked Today: zero console errors", errs(p))
    shot(p, "F3-today-locked.png", width=390, height=1200)
    # restore
    sb_admin("PATCH", "/rest/v1/subscriptions?org_id=eq." + ids["org"],
             {"status": "trialing", "locked_at": None, "trial_end": iso(6 * 86400)})


# ══════════════════════════════════════════════════════════════════════════
# L — the SECOND child's Today, and the parent's own front page
# ══════════════════════════════════════════════════════════════════════════
def phase_l(p, ids):
    print("\n── L · the Year 10 child, and the parent's dashboard ──────")
    tsess, _ = child_session(ids, "tobi")
    with_session(p, tsess)
    p.set_viewport(390, 900, settle=0.3)
    p.goto(qs("/consumer/today.html"), settle=2.5)
    ok = wait_for(p, "document.querySelectorAll('#td-items .td-item').length > 0", tries=50, gap=0.4)
    t = text(p)
    check(ok, "L the Year 10 child's Today renders their own week", t[:300].replace("\n", " "))
    check("Tobi" in t, "L it greets Tobi, not the other child", t[:120].replace("\n", " "))
    hrefs = p.eval("Array.prototype.map.call(document.querySelectorAll('#td-items a.td-item-top'),"
                   "function(a){return a.getAttribute('href');})")
    lessons = [h for h in (hrefs or []) if not h.startswith("/consumer/")]
    check(lessons and all("/triple/higher/" in h for h in lessons),
          "L every LESSON link on the Y10 home-ed child's Today is a Triple Higher KS4 page", lessons)
    check(any(h.startswith("/consumer/exam.html") for h in (hrefs or [])),
          "L the home-education week also carries an exam question", hrefs)
    check(not errs(p), "L Y10 Today: zero console errors", errs(p))
    shot(p, "L1-today-year10.png", width=390, height=1200)

    psess = sign_in(ids["parent_email"], PARENT_PW)
    with_session(p, psess)
    p.set_viewport(1200, 1000, settle=0.3)
    p.goto(qs("/consumer/overview.html"), settle=3.0)
    for _ in range(25):
        if "Loading" not in text(p) and len(text(p).strip()) > 200:
            break
        time.sleep(1.0)
    t = text(p)
    check("Not found" not in t[:200], "L the parent dashboard renders", t[:200].replace("\n", " "))
    check("Amara" in t and "Tobi" in t, "L the dashboard shows both children",
          t[:400].replace("\n", " "))
    check("Free week" in t or "free week" in t.lower(),
          "L the dashboard states the billing state", t[:400].replace("\n", " "))
    check(not errs(p), "L parent dashboard: zero console errors", errs(p))
    shot(p, "L2-parent-dashboard.png", width=1200, height=1400)
    p.set_viewport(390, 900, settle=0.3)
    over = p.eval("[document.documentElement.scrollWidth, document.documentElement.clientWidth]")
    check(over[0] <= over[1] + 1, "L the parent dashboard does not overflow at 390px", over)
    shot(p, "L3-parent-dashboard-390.png", width=390, height=1400)
    p.set_viewport(1200, 1000, settle=0.3)


# ══════════════════════════════════════════════════════════════════════════
# teardown
# ══════════════════════════════════════════════════════════════════════════
def teardown(ids):
    print("\n── cleanup ───────────────────────────────────────────────")
    # Stripe first: the test-mode subscription and customer this drive made.
    sk = env("STRIPE_SECRET_KEY")
    for sub in ([ids["stripe_sub"]] if ids.get("stripe_sub") else []):
        st, d = http("DELETE", "https://api.stripe.com/v1/subscriptions/" + sub, None,
                     {"Authorization": "Bearer " + sk,
                      "Content-Type": "application/x-www-form-urlencoded"})
        print("  stripe subscription", sub, st)
    for cus in ([ids["stripe_customer"]] if ids.get("stripe_customer") else []):
        st, d = http("DELETE", "https://api.stripe.com/v1/customers/" + cus, None,
                     {"Authorization": "Bearer " + sk,
                      "Content-Type": "application/x-www-form-urlencoded"})
        print("  stripe customer", cus, st)

    org = ids.get("org")
    if org:
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
                  "unit_check_attempts", "work_items", "work_generation_runs", "child_plans",
                  "family_messages", "consumer_notifications", "org_limits",
                  "account_deletion_requests"):
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
        print("  user", u, "profile", st, "auth", st2, "" if st2 < 300 else r2)
    if org:
        sb_admin("DELETE", "/rest/v1/academic_years?school_id=eq." + org)
        st, r = sb_admin("DELETE", "/rest/v1/schools?id=eq." + org)
        print("  org", org, st, "" if st < 300 else r)

    # prove it
    left = {}
    if org:
        for t in ("work_items", "exam_answers", "family_messages", "consumer_notifications",
                  "unit_check_attempts", "subscriptions", "child_plans", "work_generation_runs",
                  "email_log", "stripe_events", "ai_usage_events"):
            st, rows = sb_admin("GET", "/rest/v1/%s?select=org_id&org_id=eq.%s" % (t, org))
            left[t] = len(rows or []) if isinstance(rows, list) else rows
        st, rows = sb_admin("GET", "/rest/v1/schools?select=id&id=eq." + org)
        left["schools"] = len(rows or []) if isinstance(rows, list) else rows
    st, users = sb_admin("GET", "/auth/v1/admin/users?per_page=1000")
    ghosts = [u["id"] for u in (users.get("users") or []) if u["id"] in set(ids.get("users", []))]
    left["auth_users"] = len(ghosts)
    print("  residue:", json.dumps(left))
    return left


# ══════════════════════════════════════════════════════════════════════════
def main():
    global BASE, API
    ap = argparse.ArgumentParser()
    ap.add_argument("--site", default="mrbadmus_site")
    ap.add_argument("--api", default="http://localhost:3141")
    ap.add_argument("--port", type=int, default=8141)
    ap.add_argument("--phases", default="ABCDEFGHIJKL")
    ap.add_argument("--keep", action="store_true")
    ap.add_argument("--reuse", action="store_true")
    ap.add_argument("--teardown-only", action="store_true")
    a = ap.parse_args()
    API = a.api
    os.makedirs(SHOTS, exist_ok=True)

    if a.teardown_only:
        teardown(json.load(open(STATE_FILE)))
        return 0

    server, port = cdp.serve(os.path.abspath(a.site), a.port)
    BASE = "http://localhost:%d" % port
    print("serving BUILT tree at", BASE, "· backend", API)

    ids = json.load(open(STATE_FILE)) if a.reuse else {"users": []}
    try:
        with cdp.Browser() as b:
            p = b.attach()
            p.send("Page.addScriptToEvaluateOnNewDocument", {"source": FLAG_ON_JS})

            if "A" in a.phases:
                phase_a(p)
            jwt = None
            if "B" in a.phases:
                jwt = phase_b(p, ids)
            if jwt is None and ids.get("parent_email"):
                jwt = sign_in(ids["parent_email"], PARENT_PW)["access_token"]
            if "C" in a.phases:
                phase_c(p, ids, jwt)
            if "D" in a.phases:
                phase_d(ids, jwt)
            if "E" in a.phases:
                phase_e(p, ids)
            sess = ctok = None
            if set("FGHJK") & set(a.phases):
                sess, ctok = child_session(ids, "amara")
            if "F" in a.phases:
                phase_f1(p, ids, sess)
            if "G" in a.phases:
                phase_g(p, ids, sess, jwt)
            aid = ids.get("answer")
            if "H" in a.phases:
                aid = phase_h(p, ids, sess)
            if "I" in a.phases:
                phase_i(p, ids, aid)
            if "J" in a.phases:
                phase_j(p, ids, sess, jwt)
            if "L" in a.phases:
                phase_l(p, ids)
        if "K" in a.phases:
            phase_k(ids, jwt, ctok)
        with cdp.Browser() as b:
            p = b.attach()
            p.send("Page.addScriptToEvaluateOnNewDocument", {"source": FLAG_ON_JS})
            if "F" in a.phases:
                phase_f2(p, ids, sess)
                phase_f3(p, ids, sess)
    finally:
        save(ids)
        if not a.keep:
            try:
                teardown(ids)
            except Exception as e:
                print("  teardown blew up:", e)
        server.shutdown()

    print("\n%d failure(s)" % len(FAILS))
    for f in FAILS:
        print("  - " + f)
    return min(len(FAILS), 99)


if __name__ == "__main__":
    sys.exit(main())
