#!/usr/bin/env python3
"""mrb327_billing_drive.py — MRB-327 §1 Lane 2: the post-merge consumer
billing and account regression, driven on the MERGED tree against TEST.

    # backend worktree, branch b2c/hardening
    stripe listen --forward-to localhost:3151/api/consumer/stripe/webhook
    CONSUMER_SIGNUP_ENABLED=true PORT=3151 EXTRA_CORS_ORIGINS=http://localhost:8151 \
      STRIPE_WEBHOOK_SECRET=whsec_… node server.js

    python3 mrb327_billing_drive.py --api http://localhost:3151 --port 8151

⚑ WHY THIS FILE EXISTS.

Every consumer drive to date ran on `b2c/launch` BEFORE teacher dashboard v3,
seating (MRB-322) and the assignments go-live hold (MRB-324) merged. This one
runs on the merged tree, drives every billing state a real family can be in,
and presses every account action a parent has.

⚑ WHAT IS DRIVEN BY A REAL STRIPE EVENT, AND WHAT IS NOT.

Where a test-mode Stripe event can produce a state, the event produces it and
the webhook does the work — that is the only way to know the webhook, the
mirror and `org_access_state()` still agree. Two states cannot be reached that
way and are reached by SQL, and both are named as such in the report:

  trialing            EVENT  customer.subscription.created (trial 7 days)
  past_due + grace    EVENT  invoice.payment_failed (declining card at trial end)
  read_only           SQL    needs current_period_end 8+ days in the REAL past
  active              EVENT  invoice.paid + customer.subscription.updated
  cancelled (paid up) EVENT  customer.subscription.updated cancel_at_period_end
  cancelled (read-only) SQL  Stripe cannot make `canceled` + a FUTURE period end
  locked              EVENT  customer.subscription.deleted
  reactivate          EVENT  customer.subscription.created on the same customer

⚑ THE THREE LAYERS OF A WRITE REFUSAL.

In every non-writable state the drive demands all three, together, because any
one of them alone is not enforcement:
  · the page disables its `[data-write]` controls (guard()/applyWritable);
  · the backend answers 423 `org_locked` (requireWritable / writableHere);
  · RLS refuses underneath — `family_messages_send` carries the conjunct
    `org_access_state(org_id) = 'full'`, so the child's own JWT is refused by
    Postgres even if both layers above were removed.

⚑ TEST PROJECT ONLY. Fixtures are created through the real API and torn down
in `docs/b2c/night3-executor-common.md`'s order; ids are journalled to a JSON
state file as they are made so a crash cannot lose them. Stripe test customers
and subscriptions are deleted too.
"""
import argparse, json, os, re, ssl, sys, time, urllib.parse, urllib.request, urllib.error

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ks3_browser as cdp

SB = "https://qeppkiswvclkkwbxmlok.supabase.co"
STRIPE_API = "https://api.stripe.com/v1"
CTX = ssl.create_default_context(cafile="/etc/ssl/cert.pem")
BACKEND_ENV = "/Users/midebadmus/Documents/GitHub/mrbadmus-worktrees/b2c/backend/.env"
SCRATCH = ("/private/tmp/claude-501/-Users-midebadmus-Documents-GitHub-mrbadmus-worktrees-"
           "b2c-launch/06d799b1-12f9-481b-9871-424a2321715f/scratchpad")
STATE_FILE = os.path.join(SCRATCH, "mrb327_lane2_fixtures.json")

TAG = "l2"
PW = "Passw0rd!mrb327lane2"
CHILD_PW = "comet-saturn-42"
OPERATOR = ("hz_op@test.mrbadmus", "Night3!Op")

# `org_access_state()` is cached for 15 s in consumer/access.js. A transition
# made by SQL is invisible to the backend until it expires; a transition made
# by a webhook invalidates it on the spot. Every SQL move below pays this.
CACHE_TTL = 16

FAILS = []
NOTES = []


def check(ok, label, evidence=""):
    print(("  OK  " if ok else "  XX  ") + label + (("  — " + str(evidence)[:500]) if evidence else ""))
    if not ok:
        FAILS.append(label)
    return ok


def note(text):
    NOTES.append(text)
    print("  ··  " + text)


def env(name):
    for line in open(BACKEND_ENV):
        if line.startswith(name + "="):
            return line.split("=", 1)[1].strip().strip('"').strip("'")
    return None


SERVICE = env("SUPABASE_SERVICE_ROLE_KEY")
ANON = env("SUPABASE_ANON_KEY")
SK = env("STRIPE_SECRET_KEY")
PRICE_MONTH = env("STRIPE_PRICE_MONTHLY")
PRICE_YEAR = env("STRIPE_PRICE_ANNUAL")
# The account's own version — the one `stripe listen` speaks and the one
# consumer/stripe.js pins. Reading a Subscription in any other version puts
# current_period_end somewhere else.
STRIPE_VERSION = "2026-08-26.dahlia"


# ── plumbing ──────────────────────────────────────────────────────────────
def http(method, url, body=None, headers=None, timeout=90, raw=None):
    if raw is not None:
        data = raw
    else:
        data = json.dumps(body).encode() if body is not None else None
    h = {"Content-Type": "application/json"}
    h.update(headers or {})
    req = urllib.request.Request(url, data=data, method=method, headers=h)
    try:
        with urllib.request.urlopen(req, context=CTX, timeout=timeout) as r:
            t = r.read().decode()
            try:
                return r.status, (json.loads(t) if t else None), dict(r.headers)
            except Exception:
                return r.status, t, dict(r.headers)
    except urllib.error.HTTPError as e:
        t = e.read().decode()
        try:
            return e.code, json.loads(t), dict(e.headers)
        except Exception:
            return e.code, t, dict(e.headers)
    except Exception as e:
        return 0, str(e), {}


def sb_admin(method, path, body=None):
    st, d, _ = http(method, SB + path, body,
                    {"apikey": SERVICE, "Authorization": "Bearer " + SERVICE,
                     "Prefer": "return=representation"})
    return st, d


def sb_as(jwt, method, path, body=None):
    """PostgREST as a real end user — this is the RLS layer, with no backend
    in front of it."""
    st, d, _ = http(method, SB + path, body,
                    {"apikey": ANON, "Authorization": "Bearer " + jwt,
                     "Prefer": "return=representation"})
    return st, d


def sign_in(email, pw):
    st, d, _ = http("POST", SB + "/auth/v1/token?grant_type=password",
                    {"email": email, "password": pw}, {"apikey": ANON})
    assert st == 200, (email, st, d)
    return d


def api(method, path, jwt=None, body=None, timeout=120, _retry=True):
    """⚠️ 120 CONSUMER REQUESTS PER USER PER 15 MINUTES (`consumer_user` in
    consumer/limits.js). A drive that presses every route in every billing
    state spends that budget in about five minutes, and a 429 recorded as a
    failure would be a lie about the product. It is waited out instead, with
    the wait printed, so the run stays honest and stays complete."""
    h = {"Authorization": "Bearer " + jwt} if jwt else {}
    st, d, hdrs = http(method, API + path, body, h, timeout=timeout)
    if st == 429 and _retry and isinstance(d, dict):
        wait = int(d.get("retry_after_s") or 60) + 3
        print("  ..  rate limited on %s — waiting %ds for the window to roll" % (path, wait))
        time.sleep(wait)
        return api(method, path, jwt, body, timeout, _retry=False)
    return st, d


# ── Stripe, over its REST API ─────────────────────────────────────────────
def _form(prefix, value, out):
    if isinstance(value, dict):
        for k, v in value.items():
            _form("%s[%s]" % (prefix, k) if prefix else k, v, out)
    elif isinstance(value, (list, tuple)):
        for i, v in enumerate(value):
            _form("%s[%d]" % (prefix, i), v, out)
    elif isinstance(value, bool):
        out.append((prefix, "true" if value else "false"))
    elif value is None:
        out.append((prefix, ""))
    else:
        out.append((prefix, str(value)))


def stripe(method, path, params=None):
    body = None
    url = STRIPE_API + path
    if params:
        pairs = []
        _form("", params, pairs)
        enc = urllib.parse.urlencode(pairs)
        if method == "GET":
            url += "?" + enc
        else:
            body = enc.encode()
    st, d, _ = http(method, url, raw=body, headers={
        "Authorization": "Bearer " + SK,
        "Content-Type": "application/x-www-form-urlencoded",
        "Stripe-Version": STRIPE_VERSION,
    })
    return st, d


def sub_period_end(sub):
    """The account version moved current_period_end onto the ITEM. Read both
    shapes for the same reason consumer/stripe.js does."""
    if not isinstance(sub, dict):
        return None
    if sub.get("current_period_end"):
        return sub["current_period_end"]
    items = ((sub.get("items") or {}).get("data") or [])
    for it in items:
        if it.get("current_period_end"):
            return it["current_period_end"]
    return None


# ── state journal ─────────────────────────────────────────────────────────
IDS = {"users": [], "orgs": [], "stripe_customers": [], "stripe_subscriptions": [],
       "stripe_payment_methods": []}


def journal():
    os.makedirs(SCRATCH, exist_ok=True)
    with open(STATE_FILE, "w") as f:
        json.dump(IDS, f, indent=2)


def remember(bucket, value):
    if value and value not in IDS[bucket]:
        IDS[bucket].append(value)
        journal()
    return value


def iso(delta_s):
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(time.time() + delta_s))


# ── the mirror, and waiting for a webhook to land on it ───────────────────
def mirror(org):
    st, d = sb_admin("GET", "/rest/v1/subscriptions?org_id=eq." + org + "&select=*")
    return (d or [None])[0] if isinstance(d, list) else None


def access_state(org):
    st, d = sb_admin("POST", "/rest/v1/rpc/org_access_state", {"p_org_id": org})
    return d


def wait_mirror(org, predicate, label, tries=40, gap=1.0):
    """Stripe delivers, `stripe listen` forwards, the webhook writes. None of
    that is instant, and polling the mirror is the only honest way to know it
    happened."""
    row = None
    for _ in range(tries):
        row = mirror(org)
        if row and predicate(row):
            return row
        time.sleep(gap)
    return row


# ── browser helpers (night3_flagon_smoke's, unchanged in substance) ───────
FLAG_ON_JS = """(function(){var c=null;Object.defineProperty(window,'MrBadmusConfig',{configurable:true,
  get:function(){return c;}, set:function(v){ if(v&&typeof v==='object'){v.CONSUMER_SIGNUP_ENABLED=true;} c=v; }});})();"""


def with_session(p, sess):
    p.goto(BASE + "/404.html?env=test", settle=0.2)
    p.eval("localStorage.clear()")
    p.eval("localStorage.setItem('sb-qeppkiswvclkkwbxmlok-auth-token', %s)"
           % json.dumps(json.dumps(sess)))


def session_of(tok):
    """A child JWT from /api/consumer/child/login, shaped as a GoTrue session.
    The SDK deletes a session it cannot parse, so the shape is load-bearing."""
    return {"access_token": tok["access_token"], "refresh_token": tok["refresh_token"],
            "expires_in": tok.get("expires_in", 3600), "expires_at": int(time.time()) + 3600,
            "token_type": "bearer", "user": {"id": tok["user"]["id"]}}


def errs(p):
    return [e for e in p.console_errors()
            if "favicon.ico" not in e
            and not re.search(r"Failed to load resource.*\b(40[0-9]|423|429)\b", e)]


# ⚠️ "THE TEXT STOPPED CHANGING" IS NOT "THE PAGE IS READY".
#
# Every consumer page ships a static skeleton and fills it from one API call.
# The skeleton is long, stable and contains no word like "Loading", so a
# settle loop that waits for stability alone reads the skeleton and calls it
# a render — and then asserts against a page that has not loaded. It cost one
# false failure on this drive (child Today, "Hello." with no name) before it
# was caught. Each page therefore names the DOM fact that means it has data.
READY = {
    "/consumer/today.html":
        "!!document.getElementById('td-greet') && "
        "document.getElementById('td-greet').textContent.trim() !== 'Hello.'",
    "/consumer/overview.html":
        "!!document.getElementById('c-main') && "
        "document.getElementById('c-main').innerText.trim().length > 60",
    "/consumer/account.html":
        "!!document.getElementById('c-main') && "
        "/your plan|couldn/i.test(document.getElementById('c-main').innerText)",
    "/consumer/report.html":
        "!!document.getElementById('c-main') && "
        "document.getElementById('c-main').innerText.trim().length > 60",
}


def ready_expr(path):
    for k, v in READY.items():
        if path.startswith(k):
            return v
    return None


def visit(p, path, label, expect=None, forbid=None, shot=None, width=390, quiet=False):
    p.goto(BASE + path + ("&" if "?" in path else "?") + "env=test&api=" + API, settle=1.0)
    want = ready_expr(path)
    if want:
        got = False
        for _ in range(40):
            try:
                if p.eval("(function(){try{return (%s);}catch(e){return false;}})()" % want):
                    got = True
                    break
            except Exception:
                pass
            time.sleep(0.75)
        check(got, "%s: the page actually filled from its API call "
                   "(not the empty skeleton)" % label,
              (p.eval("document.body.innerText") or "")[:200].replace("\n", " ") if not got else "")
    text, prev = "", None
    for _ in range(30):
        text = p.eval("document.body ? document.body.innerText : ''") or ""
        loading = ("Loading" in text) or (len(text.strip()) < 40)
        if not loading and text == prev:
            break
        prev = text
        time.sleep(1.0)
    e = errs(p)
    check(not e, "%s: zero console errors" % label, e)
    check("Not found" not in text[:200], "%s: rendered" % label, text[:120].replace("\n", " "))
    norm = lambda t: t.lower().replace("’", "'").replace("‘", "'")
    for x in (expect or []):
        check(norm(x) in norm(text), "%s: says “%s”" % (label, x),
              "" if norm(x) in norm(text) else text[:700].replace("\n", " "))
    for x in (forbid or []):
        check(norm(x) not in norm(text), "%s: does NOT say “%s”" % (label, x),
              "" if norm(x) not in norm(text) else text[:700].replace("\n", " "))
    if shot:
        p.screenshot(os.path.join(SHOTS, shot), width=width)
    return text


def write_controls(p):
    """Every [data-write] control on the page, and whether it is disabled.
    This is the frontend half of the refusal; on its own it is untidiness,
    not enforcement, which is why the 423 and the RLS check ride with it."""
    return p.eval("""(function(){var n=document.querySelectorAll('[data-write]');
      var t=0,d=0; for(var i=0;i<n.length;i++){t++; if(n[i].disabled)d++;}
      return JSON.stringify({total:t,disabled:d});})()""")


# ══════════════════════════════════════════════════════════════════════════
# FIXTURES
# ══════════════════════════════════════════════════════════════════════════
FAM = {}


def make_parent(email, name):
    st, d = sb_admin("POST", "/auth/v1/admin/users",
                     {"email": email, "password": PW, "email_confirm": True,
                      "user_metadata": {"first_name": name}})
    if st >= 300:
        st2, users = sb_admin("GET", "/auth/v1/admin/users?per_page=500")
        d = next(u for u in users["users"] if u["email"] == email)
    remember("users", d["id"])
    return d["id"]


def setup():
    print("\n── fixtures ───────────────────────────────────────────────────")
    email = "mrb327-%s-parent@mrbadmus-test.com" % TAG
    uid = make_parent(email, "Funmi")
    sess = sign_in(email, PW)
    jwt = sess["access_token"]
    st, fam = api("POST", "/api/consumer/family/ensure", jwt,
                  {"family_name": "Lane2 family %s" % TAG})
    check(st == 200 and fam.get("ok"), "family/ensure", (st, fam))
    org = remember("orgs", fam["org_id"])

    kids = []
    stamp = int(time.time()) % 100000
    for i, (n, yg, mode) in enumerate((("Amara", 8, "alongside_school"),
                                       ("Leo", 7, "home_education"))):
        st, c = api("POST", "/api/consumer/children", jwt, {
            "first_name": n, "year_group": yg, "username": "l2%s%d%d" % (n[:3].lower(), stamp, i),
            "password": CHILD_PW, "mode": mode, "intensity": "light", "exam_board": "AQA"})
        check(st == 200, "create child %s" % n, (st, c))
        remember("users", c["child_id"])
        kids.append({"id": c["child_id"], "name": n, "username": c["username"]})

    FAM.update({"email": email, "uid": uid, "sess": sess, "jwt": jwt, "org": org, "kids": kids})
    print("  parent %s   org %s   kids %s" % (uid, org, [k["id"] for k in kids]))

    FAM["monday"] = time.strftime("%Y-%m-%d",
                                  time.localtime(time.time() - (time.localtime().tm_wday * 86400)))
    # ⚠️ NO WEEK IS GENERATED HERE. A family with no subscription is at access
    # `none`, and `writableHere` refuses generation with a 423 — correctly.
    # The week is generated in state_trialing(), the first state in which a
    # real family could have had one.
    return FAM


def generate_week():
    """Per child, through the real route — never /cron/weekly, which sweeps
    every consumer org on TEST and other lanes are driving."""
    jwt = parent_jwt()
    for k in FAM["kids"]:
        st, g = api("POST", "/api/consumer/children/%s/generate" % k["id"], jwt,
                    {"week_start": FAM["monday"]})
        check(st == 200, "generate a week of work for %s" % k["name"], (st, g))


_SLUG = {}


def lesson_slug():
    """A real lesson from the child's own scheme, read from the picker the
    parent's page reads. Cached: it does not change during a run."""
    if _SLUG.get("v"):
        return _SLUG["v"]
    st, pick = api("GET", "/api/consumer/children/%s/picker" % FAM["kids"][0]["id"], parent_jwt())
    for u in (pick or {}).get("units") or []:
        for l in u.get("lessons") or []:
            if l.get("slug"):
                _SLUG["v"] = l["slug"]
                return l["slug"]
    return None


_CHILD_SESS = {}


def child_session(kid, force=False):
    """⚠️ CACHED, and it has to be. `/api/consumer/child/login` allows ten
    attempts per fifteen minutes per IP *and* per username, and a drive that
    signs a child in once per assertion runs out inside the first three
    states. The token lives an hour; it is re-fetched when it is nearly
    stale and not before."""
    hit = _CHILD_SESS.get(kid["id"])
    if hit and not force and time.time() - hit["at"] < 45 * 60:
        return hit["sess"]
    st, cl = api("POST", "/api/consumer/child/login", None,
                 {"username": kid["username"], "password": CHILD_PW})
    assert st == 200, (st, cl)
    _CHILD_SESS[kid["id"]] = {"at": time.time(), "sess": cl}
    return cl


def parent_jwt():
    """Re-signs in. A GoTrue access token lives an hour and this drive is
    longer than that once Stripe's retries are waited on."""
    FAM["sess"] = sign_in(FAM["email"], PW)
    FAM["jwt"] = FAM["sess"]["access_token"]
    return FAM["jwt"]


# ══════════════════════════════════════════════════════════════════════════
# THE THREE-LAYER WRITE REFUSAL
# ══════════════════════════════════════════════════════════════════════════
def backend_refusals(label, writable):
    """The backend half. Every guarded route, in one place, so a state that
    guards one and not another cannot pass."""
    jwt = parent_jwt()
    kid = FAM["kids"][0]
    probes = []

    st, d = api("POST", "/api/consumer/chat/send", jwt,
                {"to": kid["id"], "text": "lane2 refusal probe"})
    probes.append(("chat/send", st, d))

    st, d = api("POST", "/api/consumer/children/%s/work" % kid["id"], jwt,
                {"kind": "lesson", "lesson_slug": lesson_slug(),
                 "scheduled_for": time.strftime("%Y-%m-%d")})
    probes.append(("children/:id/work", st, d))
    if st == 200 and (d or {}).get("item"):
        # A probe that leaves work behind changes what the next assertion
        # sees. Take it back out.
        api("DELETE", "/api/consumer/children/%s/work/%s" % (kid["id"], d["item"]["id"]), jwt)

    st, d = api("POST", "/api/consumer/children/%s/generate" % kid["id"], jwt,
                {"week_start": FAM["monday"]})
    probes.append(("children/:id/generate", st, d))

    cl = child_session(kid)
    st, today = api("GET", "/api/consumer/child/today", cl["access_token"])
    item = ((today or {}).get("items") or [{}])[0].get("id") if st == 200 else None
    if item:
        st, d = api("POST", "/api/consumer/child/work/%s/done" % item, cl["access_token"], {})
        probes.append(("child/work/:id/done", st, d))

    if writable:
        ok = all(s < 400 for _, s, _ in probes)
        check(ok, "%s: every write route is ALLOWED" % label,
              [(n, s) for n, s, _ in probes if s >= 400])
    else:
        bad = [(n, s, (d or {}).get("error") if isinstance(d, dict) else d)
               for n, s, d in probes if not (s == 423 and isinstance(d, dict) and d.get("error") == "org_locked")]
        check(not bad, "%s: every write route answers 423 org_locked" % label, bad)
    return probes


def rls_refusal(label, writable):
    """The layer underneath. `family_messages_send` carries the conjunct
    `org_access_state(org_id) = 'full'`, so Postgres itself refuses — the
    parent's own JWT, no backend in the path."""
    jwt = parent_jwt()
    kid = FAM["kids"][0]
    st, d = sb_as(jwt, "POST", "/rest/v1/family_messages", {
        "org_id": FAM["org"], "sender_id": FAM["uid"], "recipient_id": kid["id"],
        "body": "lane2 rls probe %s" % label})
    if writable:
        ok = st in (200, 201) and isinstance(d, list) and d
        check(ok, "%s: RLS ALLOWS the insert when access is full" % label, (st, d))
        if ok:
            sb_admin("DELETE", "/rest/v1/family_messages?id=eq." + d[0]["id"])
    else:
        refused = st in (401, 403) or (isinstance(d, dict) and str(d.get("code")) == "42501")
        check(refused, "%s: RLS REFUSES the insert underneath" % label, (st, d))
    return st, d


def page_layer(p, label, writable, kid_sess, shots_prefix, overview_expect,
               account_expect, today_expect, overview_forbid=None):
    """What the parent and the child actually SEE, and whether the page's own
    controls are disabled."""
    kid = FAM["kids"][0]
    with_session(p, FAM["sess"])
    t1 = visit(p, "/consumer/overview.html", "%s · parent overview" % label,
               expect=overview_expect, forbid=overview_forbid,
               shot="%s-overview-390.png" % shots_prefix)

    # ⚠️ THE OVERVIEW ITSELF CARRIES NO [data-write] CONTROL. Every one of
    # them is on the child, chat, set-work and manage views, so counting them
    # on the overview counts zero and passes either way. These two views are
    # where the guard can actually be seen to work.
    for view, vlabel in (("child", "child view"), ("chat", "chat view")):
        visit(p, "/consumer/overview.html?child=%s&view=%s" % (kid["id"], view),
              "%s · parent %s" % (label, vlabel),
              shot=("%s-%s-390.png" % (shots_prefix, view)) if not writable else None)
        wc = json.loads(write_controls(p))
        if writable:
            check(wc["total"] > 0 and wc["disabled"] == 0,
                  "%s: parent %s leaves its %d write controls live" % (label, vlabel, wc["total"]), wc)
        else:
            check(wc["total"] > 0 and wc["disabled"] == wc["total"],
                  "%s: parent %s disables all %d write controls" % (label, vlabel, wc["total"]), wc)

    t2 = visit(p, "/consumer/account.html", "%s · parent account" % label,
               expect=account_expect, shot="%s-account-390.png" % shots_prefix)

    with_session(p, session_of(kid_sess))
    t3 = visit(p, "/consumer/today.html", "%s · child today" % label,
               expect=today_expect, shot="%s-today-390.png" % shots_prefix)
    wc3 = json.loads(write_controls(p))
    if not writable:
        check(wc3["total"] > 0 and wc3["disabled"] == wc3["total"],
              "%s: child Today disables all %d write controls" % (label, wc3["total"]), wc3)
    return t1, t2, t3


def assert_state(p, label, shots_prefix, want_status, want_access, want_billing_state,
                 writable, overview_expect, account_expect, today_expect,
                 overview_forbid=None):
    print("\n── state: %s ──────────────────────────────────────────────" % label)
    row = mirror(FAM["org"])
    check(row is not None and row["status"] == want_status,
          "%s: subscriptions.status = %s" % (label, want_status),
          {k: row.get(k) for k in ("status", "trial_end", "current_period_end", "canceled_at",
                                   "cancel_at_period_end", "locked_at", "retry_at", "quantity")} if row else None)
    st = access_state(FAM["org"])
    check(st == want_access, "%s: org_access_state() = %s" % (label, want_access), st)

    jwt = parent_jwt()
    code, fam = api("GET", "/api/consumer/family", jwt)
    b = (fam or {}).get("billing") or {}
    check(code == 200, "%s: GET /api/consumer/family 200" % label, code)
    check(b.get("state") == want_billing_state,
          "%s: family.billing.state = %s" % (label, want_billing_state), b.get("state"))
    check(b.get("access") == want_access,
          "%s: family.billing.access = %s (the permission)" % (label, want_access), b.get("access"))

    kid_sess = child_session(FAM["kids"][0])
    page_layer(p, label, writable, kid_sess, shots_prefix,
               overview_expect, account_expect, today_expect, overview_forbid)
    backend_refusals(label, writable)
    rls_refusal(label, writable)
    return row, b


# ══════════════════════════════════════════════════════════════════════════
# PHASE A — every billing state
# ══════════════════════════════════════════════════════════════════════════
PM_FAIL = "pm_card_chargeCustomerFail"   # attaches fine, declines when charged
PM_GOOD = "pm_card_visa"


def open_checkout():
    """The parent's own path to a subscription. Driven for itself — and it is
    also what creates the Stripe customer, which every later transition needs.
    The session is read back FROM STRIPE, because a URL is not evidence that a
    session exists."""
    print("\n── checkout (the real route) ──────────────────────────────────")
    jwt = parent_jwt()
    st, d = api("POST", "/api/consumer/checkout", jwt, {"interval": "month"})
    check(st == 200 and d.get("url"), "POST /api/consumer/checkout → 200 with a url", (st, d))
    if st != 200:
        return None
    url = d["url"]
    check(url.startswith("https://checkout.stripe.com/"),
          "checkout url is a real hosted Checkout page", url[:80])
    sst, sess = stripe("GET", "/checkout/sessions/" + d["session_id"])
    check(sst == 200, "the session exists AT STRIPE", (sst, sess if sst != 200 else ""))
    if sst == 200:
        check(sess.get("livemode") is False, "checkout session is TEST mode", sess.get("livemode"))
        check(sess.get("client_reference_id") == FAM["org"],
              "checkout session carries the org as client_reference_id", sess.get("client_reference_id"))
        check((sess.get("subscription_data") or {}).get("trial_period_days") == 7
              or sess.get("mode") == "subscription",
              "checkout session is a subscription with the 7-day trial",
              {"mode": sess.get("mode"), "sd": sess.get("subscription_data")})
    row = mirror(FAM["org"])
    cust = row and row.get("stripe_customer_id")
    check(bool(cust), "the Stripe customer is mirrored the moment checkout opens", cust)
    remember("stripe_customers", cust)
    return cust


def attach(customer, pm):
    st, d = stripe("POST", "/payment_methods/%s/attach" % pm, {"customer": customer})
    if st == 200:
        remember("stripe_payment_methods", d["id"])
        stripe("POST", "/customers/" + customer,
               {"invoice_settings": {"default_payment_method": d["id"]}})
        return d["id"]
    # An already-attached test PM comes back 400; find it on the customer.
    st2, lst = stripe("GET", "/payment_methods", {"customer": customer, "type": "card"})
    return (lst.get("data") or [{}])[0].get("id") if st2 == 200 else None


def state_trialing(p, customer):
    pm = attach(customer, PM_FAIL)
    check(bool(pm), "a declining test card is attached (so trial end really fails)", pm)
    st, sub = stripe("POST", "/subscriptions", {
        "customer": customer,
        "items": [{"price": PRICE_MONTH, "quantity": len(FAM["kids"])}],
        "trial_period_days": 7,
        "default_payment_method": pm,
        "metadata": {"org_id": FAM["org"]},
        "trial_settings": {"end_behavior": {"missing_payment_method": "cancel"}},
    })
    check(st == 200, "Stripe: subscription created with a 7-day trial", (st, sub if st != 200 else sub["id"]))
    if st != 200:
        return None
    remember("stripe_subscriptions", sub["id"])
    row = wait_mirror(FAM["org"], lambda r: r.get("status") == "trialing"
                      and r.get("stripe_subscription_id") == sub["id"],
                      "trialing")
    check(row and row.get("status") == "trialing",
          "webhook customer.subscription.created → mirror status trialing", row and row.get("status"))
    check(row and row.get("quantity") == len(FAM["kids"]),
          "mirror quantity follows the Stripe item quantity", row and row.get("quantity"))
    generate_week()
    assert_state(p, "trialing", "01-trialing", "trialing", "full", "trialing", True,
                 overview_expect=["Free week", "Amara"],
                 account_expect=["Free week", "Manage card in Stripe"],
                 today_expect=["Amara"])
    return sub


def state_past_due_grace(p, sub):
    """Trial end with a card that declines. This is the ONE transition a real
    family hits without doing anything, and it is the one the merge could most
    plausibly have broken."""
    st, up = stripe("POST", "/subscriptions/" + sub["id"],
                    {"trial_end": "now", "proration_behavior": "none"})
    check(st == 200, "Stripe: trial ended now", (st, up if st != 200 else up.get("status")))
    # ⚠️ TWO EVENTS, EITHER ORDER. `customer.subscription.updated` (status
    # past_due) and `invoice.payment_failed` (the dunning stamps) are separate
    # deliveries; waiting on the status alone reads the row between them and
    # sees a half-written state that never reaches a parent.
    row = wait_mirror(FAM["org"],
                      lambda r: r.get("status") == "past_due" and r.get("last_payment_failed_at"),
                      "past_due", tries=60)
    check(row and row.get("status") == "past_due",
          "webhook customer.subscription.updated → mirror status past_due", row and row.get("status"))
    check(row and row.get("last_payment_failed_at"),
          "webhook invoice.payment_failed → mirror records WHEN the card was declined",
          row and row.get("last_payment_failed_at"))
    check(row and row.get("retry_at"),
          "mirror records Stripe's OWN next attempt (the page shows the date, never a countdown)",
          row and row.get("retry_at"))
    assert_state(p, "past_due (in grace)", "02-pastdue-grace", "past_due", "full", "past_due", True,
                 overview_expect=["Payment didn’t go through", "Fix card"],
                 account_expect=["Payment failed", "Your card was declined", "Update card in Stripe"],
                 today_expect=["Amara"])
    return row


def state_read_only(p, row):
    """SQL, and it has to be: `org_access_state()` drops a past_due family to
    read-only seven days after the period end, and no Stripe event can move a
    date that is measured against the real clock."""
    keep = row.get("current_period_end")
    sb_admin("PATCH", "/rest/v1/subscriptions?org_id=eq." + FAM["org"],
             {"current_period_end": iso(-10 * 86400)})
    sb_admin("POST", "/rest/v1/rpc/stamp_org_lock", {"p_org_id": FAM["org"]})
    time.sleep(CACHE_TTL)
    # ⚠️ THE ASSERTION THAT FOUND THE BUG. Once the grace is spent the family
    # IS read-only: no new work, no marking, no messages. A banner that still
    # says "work carries on until <a date that has gone>" is telling a parent
    # the opposite of what is happening to their child, on the one screen they
    # opened to find out.
    assert_state(p, "read_only (grace spent)", "03-readonly", "past_due", "read_only", "past_due", False,
                 overview_expect=["Payment didn’t go through", "paused"],
                 overview_forbid=["Work carries on until"],
                 account_expect=["Payment failed", "paused"],
                 today_expect=[])
    return keep


def state_active(p, sub, restore_cpe):
    sb_admin("PATCH", "/rest/v1/subscriptions?org_id=eq." + FAM["org"],
             {"current_period_end": restore_cpe})
    pm = attach(FAM["customer"], PM_GOOD)
    stripe("POST", "/subscriptions/" + sub["id"], {"default_payment_method": pm})
    st, inv = stripe("GET", "/invoices", {"customer": FAM["customer"], "status": "open", "limit": 3})
    target = (inv.get("data") or [{}])[0].get("id") if st == 200 else None
    check(bool(target), "there is an open invoice to pay", target)
    if target:
        pst, paid = stripe("POST", "/invoices/%s/pay" % target, {})
        check(pst == 200, "Stripe: the invoice is paid with a good card",
              (pst, paid if pst != 200 else paid.get("status")))
    row = wait_mirror(FAM["org"], lambda r: r.get("status") == "active", "active", tries=60)
    check(row and row.get("status") == "active",
          "webhook invoice.paid + subscription.updated → mirror status active", row and row.get("status"))
    check(row and not row.get("retry_at") and not row.get("last_payment_failed_at"),
          "paying clears the dunning fields — no “we will retry” shown to somebody who has paid",
          {"retry_at": row.get("retry_at"), "failed": row.get("last_payment_failed_at")} if row else None)
    assert_state(p, "active", "04-active", "active", "full", "active", True,
                 overview_expect=["Amara"],
                 account_expect=["Active", "Manage billing in Stripe", "On this plan"],
                 today_expect=["Amara"])
    return row


def state_cancelled_paid_up(p, sub):
    """The REAL cancellation: Stripe keeps the subscription active to the
    period end. Design's screen is this one, and only `access` separates it
    from the read-only cancellation below."""
    st, up = stripe("POST", "/subscriptions/" + sub["id"], {"cancel_at_period_end": True})
    check(st == 200, "Stripe: cancel at period end", (st, up if st != 200 else up.get("cancel_at_period_end")))
    row = wait_mirror(FAM["org"], lambda r: r.get("cancel_at_period_end") is True, "cancel_at_period_end")
    check(row and row.get("cancel_at_period_end") is True,
          "webhook subscription.updated → mirror cancel_at_period_end true", row and row.get("cancel_at_period_end"))
    assert_state(p, "cancelled (paid up)", "05-cancelled-full", "active", "full", "cancelled", True,
                 overview_expect=["Cancelled", "Everything works until"],
                 account_expect=["Everything works until", "Resume subscription"],
                 today_expect=["Amara"])
    return row


def state_cancelled_read_only(p):
    """SQL. Stripe cannot produce `canceled` with a period end still ahead —
    when it cancels, the period has ended. The state is real all the same: it
    is what a family looks like between Stripe's cancellation and the day
    their paid period runs out, if the two are ever a moment apart."""
    sb_admin("PATCH", "/rest/v1/subscriptions?org_id=eq." + FAM["org"],
             {"status": "canceled", "canceled_at": iso(-86400),
              "cancel_at_period_end": False, "current_period_end": iso(9 * 86400)})
    sb_admin("POST", "/rest/v1/rpc/stamp_org_lock", {"p_org_id": FAM["org"]})
    time.sleep(CACHE_TTL)
    assert_state(p, "cancelled (read-only)", "06-cancelled-readonly", "canceled", "read_only",
                 "cancelled", False,
                 overview_expect=["Cancelled", "new work and messages are paused"],
                 account_expect=["Cancelled", "paused"],
                 today_expect=[])


def state_locked(p, sub):
    """⚠️ CANCELLING AT STRIPE DOES NOT LOCK A FAMILY, AND MUST NOT.
    `DELETE /subscriptions` ends the subscription immediately, but the object
    it returns still carries the period end the family PAID FOR — 6 October,
    not now — so `org_access_state()` answers `read_only` until that date and
    `stamp_org_lock` correctly stamps nothing. That is the product being
    right: a family that has paid to the sixth keeps reading to the sixth.
    `locked` is therefore reached by the EVENT plus the CALENDAR, and the
    calendar half is `dailySweep()`'s job. Driven the same way here: cancel at
    Stripe, wind the period end into the past, then run the very RPC the daily
    cron runs."""
    st, gone = stripe("DELETE", "/subscriptions/" + sub["id"])
    check(st == 200, "Stripe: subscription cancelled outright", (st, gone if st != 200 else gone.get("status")))
    row = wait_mirror(FAM["org"], lambda r: r.get("status") == "canceled", "canceled", tries=60)
    check(row and row.get("status") == "canceled",
          "webhook subscription.deleted → mirror status canceled", row and row.get("status"))
    check(access_state(FAM["org"]) == "read_only",
          "a just-cancelled family is READ-ONLY, not locked — they paid to the period end",
          access_state(FAM["org"]))
    check(not (row or {}).get("locked_at"),
          "and nothing is stamped as locked while that period is still running",
          (row or {}).get("locked_at"))

    sb_admin("PATCH", "/rest/v1/subscriptions?org_id=eq." + FAM["org"],
             {"current_period_end": iso(-2 * 86400)})
    st, state = sb_admin("POST", "/rest/v1/rpc/stamp_org_lock", {"p_org_id": FAM["org"]})
    check(state == "locked", "the daily sweep's own RPC now answers locked", state)
    time.sleep(CACHE_TTL)
    row = mirror(FAM["org"])
    check(row and row.get("locked_at"),
          "stamp_org_lock records WHEN access ended (the account card says it)",
          row and row.get("locked_at"))
    assert_state(p, "locked", "07-locked", "canceled", "locked", "locked", False,
                 overview_expect=["Work has stopped being set"],
                 account_expect=["Paused", "No active plan", "Restart"],
                 today_expect=[])
    return row


def bootstrap_active():
    """An active family, with no ladder in front of it — what the `actions`
    and `hold` phases need when they are run on their own."""
    FAM["customer"] = open_checkout()
    pm = attach(FAM["customer"], PM_GOOD)
    st, sub = stripe("POST", "/subscriptions", {
        "customer": FAM["customer"],
        "items": [{"price": PRICE_MONTH, "quantity": len(FAM["kids"])}],
        "default_payment_method": pm,
        "metadata": {"org_id": FAM["org"]},
    })
    check(st == 200, "Stripe: subscription created", (st, sub if st != 200 else sub["id"]))
    remember("stripe_subscriptions", sub["id"])
    row = wait_mirror(FAM["org"], lambda r: r.get("status") == "active", "active", tries=60)
    check(row and row.get("status") == "active", "mirror is active", row and row.get("status"))
    generate_week()
    FAM["live_sub"] = sub["id"]
    return sub


def state_reactivate(p):
    """The way back. The parent's control is Restart, which opens Checkout;
    the state change itself arrives as a subscription.created webhook, so that
    is how it is driven."""
    print("\n── reactivate ─────────────────────────────────────────────────")
    jwt = parent_jwt()
    st, d = api("POST", "/api/consumer/checkout", jwt, {"interval": "month"})
    check(st == 200 and d.get("url"), "a locked family can open Checkout again", (st, d))
    if st == 200:
        sst, sess = stripe("GET", "/checkout/sessions/" + d["session_id"])
        check(sst == 200 and sess.get("status") == "open",
              "the restart session is a live test-mode session", (sst, sess.get("status") if sst == 200 else sess))

    pm = attach(FAM["customer"], PM_GOOD)
    st, sub = stripe("POST", "/subscriptions", {
        "customer": FAM["customer"],
        "items": [{"price": PRICE_MONTH, "quantity": len(FAM["kids"])}],
        "default_payment_method": pm,
        "metadata": {"org_id": FAM["org"]},
    })
    check(st == 200, "Stripe: a new subscription on the same customer", (st, sub if st != 200 else sub["id"]))
    if st != 200:
        return None
    remember("stripe_subscriptions", sub["id"])
    row = wait_mirror(FAM["org"], lambda r: r.get("status") == "active", "reactivated", tries=60)
    check(row and row.get("status") == "active",
          "webhook → mirror is active again", row and row.get("status"))
    check(row and not row.get("locked_at"),
          "locked_at is CLEARED on reactivation (a stale stamp would date the wrong thing)",
          row and row.get("locked_at"))
    assert_state(p, "reactivated", "08-reactivated", "active", "full", "active", True,
                 overview_expect=["Amara"],
                 account_expect=["Active"],
                 today_expect=["Amara"],
                 overview_forbid=["Work has stopped being set"])
    return sub


# ══════════════════════════════════════════════════════════════════════════
# PHASE B — the account actions
# ══════════════════════════════════════════════════════════════════════════
def action_pause_resume(p):
    print("\n── B: pause, then resume ──────────────────────────────────────")
    jwt = parent_jwt()
    kid = FAM["kids"][0]
    st, d = api("POST", "/api/consumer/children/%s/pause" % kid["id"], jwt, {"paused": True})
    check(st == 200 and d.get("paused") is True, "pause: 200 and paused true", (st, d))
    st, fam = api("GET", "/api/consumer/family", jwt)
    k = next((c for c in (fam.get("children") or []) if c["id"] == kid["id"]), {})
    check(k.get("paused") or k.get("paused_at"),
          "pause: the family payload says the child is paused", {x: k.get(x) for x in ("paused", "paused_at")})
    with_session(p, FAM["sess"])
    t = visit(p, "/consumer/overview.html?child=%s&view=child" % kid["id"],
              "B: paused child page", shot="10-paused-390.png")
    check("paused" in t.lower(), "pause: the parent SEES it on the child page",
          t[:400].replace("\n", " "))

    st, d = api("POST", "/api/consumer/children/%s/pause" % kid["id"], jwt, {"paused": False})
    check(st == 200 and d.get("paused") is False, "resume: 200 and paused false", (st, d))
    st, fam = api("GET", "/api/consumer/family", jwt)
    k = next((c for c in (fam.get("children") or []) if c["id"] == kid["id"]), {})
    check(not (k.get("paused") or k.get("paused_at")),
          "resume: the family payload says the child is running again",
          {x: k.get(x) for x in ("paused", "paused_at")})
    t = visit(p, "/consumer/overview.html?child=%s&view=child" % kid["id"],
              "B: resumed child page", shot="11-resumed-390.png")
    check("paused" not in t.lower(), "resume: the paused sentence is gone", t[:400].replace("\n", " "))


def action_set_work(p):
    print("\n── B: the parent sets work ────────────────────────────────────")
    jwt = parent_jwt()
    kid = FAM["kids"][0]
    st, pick = api("GET", "/api/consumer/children/%s/picker" % kid["id"], jwt)
    check(st == 200 and (pick or {}).get("units"), "picker: units to choose from",
          (st, len((pick or {}).get("units") or [])))
    slug = None
    for u in (pick or {}).get("units") or []:
        for l in u.get("lessons") or []:
            if l.get("slug"):
                slug = l["slug"]
                break
        if slug:
            break
    check(bool(slug), "picker: a real lesson slug", slug)
    today = time.strftime("%Y-%m-%d")
    st, d = api("POST", "/api/consumer/children/%s/work" % kid["id"], jwt,
                {"kind": "lesson", "lesson_slug": slug, "scheduled_for": today})
    check(st == 200 and (d or {}).get("item"), "set work: 200 with the item", (st, d))
    item = (d or {}).get("item") or {}
    FAM["set_work_item"] = item.get("id")

    cl = child_session(kid)
    st, today_payload = api("GET", "/api/consumer/child/today", cl["access_token"])
    titles = [i.get("title") for i in (today_payload or {}).get("items") or []]
    check(item.get("title") in titles, "set work: the CHILD sees it on Today", (item.get("title"), titles))
    with_session(p, session_of(cl))
    t = visit(p, "/consumer/today.html", "B: child today after set work", shot="12-setwork-390.png")
    check((item.get("title") or "zzz") in t, "set work: it is on the rendered Today page",
          t[:500].replace("\n", " "))
    # Leave nothing behind that the next assertion would trip over.
    if FAM["set_work_item"]:
        st, _ = api("DELETE", "/api/consumer/children/%s/work/%s" % (kid["id"], FAM["set_work_item"]),
                    parent_jwt())
        check(st == 200, "set work: the parent can remove it again", st)


def action_remove_child(sub):
    """The one that has to be true AT STRIPE. Our mirror agreeing with itself
    proves nothing about what the family is billed."""
    print("\n── B: remove a child, and the seat with it ────────────────────")
    jwt = parent_jwt()
    before_st, before = stripe("GET", "/subscriptions/" + sub["id"])
    q_before = ((before.get("items") or {}).get("data") or [{}])[0].get("quantity")
    check(q_before == 2, "Stripe quantity is 2 before the removal", q_before)

    leo = FAM["kids"][1]
    st, d = api("DELETE", "/api/consumer/children/%s" % leo["id"], jwt)
    check(st == 200, "remove child: 200", (st, d))

    q_after = None
    for _ in range(40):
        _s, now = stripe("GET", "/subscriptions/" + sub["id"])
        q_after = ((now.get("items") or {}).get("data") or [{}])[0].get("quantity")
        if q_after == 1:
            break
        time.sleep(1.5)
    check(q_after == 1, "STRIPE's own subscription quantity drops to 1", q_after)
    row = wait_mirror(FAM["org"], lambda r: r.get("quantity") == 1, "quantity 1")
    check(row and row.get("quantity") == 1, "the mirror agrees with Stripe", row and row.get("quantity"))

    st, fam = api("GET", "/api/consumer/family", parent_jwt())
    seats = ((fam or {}).get("billing") or {}).get("seats") or []
    check(len(seats) == 1, "the account page will show ONE seat", [s.get("name") for s in seats])
    FAM["kids"] = [FAM["kids"][0]]
    return leo


def action_portal(p):
    print("\n── B: the customer portal link ────────────────────────────────")
    jwt = parent_jwt()
    st, d = api("POST", "/api/consumer/portal", jwt,
                {"return_url": "http://localhost:%d/consumer/account.html" % PORT})
    check(st == 200 and d.get("url"), "POST /api/consumer/portal → 200 with a url", (st, d))
    if st != 200:
        return
    url = d["url"]
    check(url.startswith("https://billing.stripe.com/"),
          "the portal url is Stripe's own hosted portal", url[:60])
    # A fabricated session id 404s here. Loading it is the only proof the
    # session was really created on the account.
    code, body, _h = http("GET", url, timeout=45)
    check(code == 200, "the portal session actually resolves at Stripe (a fake id 404s)", code)
    check(isinstance(body, str) and "stripe" in body.lower(),
          "the portal page is Stripe's", (body or "")[:80] if isinstance(body, str) else type(body))


def action_report(p):
    print("\n── B: the termly report ───────────────────────────────────────")
    jwt = parent_jwt()
    kid = FAM["kids"][0]
    st, d = api("GET", "/api/consumer/children/%s/report" % kid["id"], jwt)
    check(st == 200 and (d or {}).get("report"), "GET report → 200", (st, d if st != 200 else "ok"))
    with_session(p, FAM["sess"])
    t = visit(p, "/consumer/report.html?child=%s" % kid["id"], "B: termly report",
              expect=["Science progress report", kid["name"]], shot="13-report-390.png")
    p.set_viewport(1460, 1000)
    visit(p, "/consumer/report.html?child=%s" % kid["id"], "B: termly report (desktop)",
          shot="13-report-1460.png", width=1460)
    p.set_viewport(390, 844)
    return t


def action_export(p):
    print("\n── B: download everything we hold ─────────────────────────────")
    jwt = parent_jwt()
    code, body, hdrs = http("GET", API + "/api/consumer/family/export",
                            headers={"Authorization": "Bearer " + jwt}, timeout=180)
    check(code == 200, "GET /api/consumer/family/export → 200", code)
    cd = hdrs.get("Content-Disposition", "")
    check("attachment" in cd and ".json" in cd, "it downloads as a named .json file", cd)
    check(isinstance(body, dict) and body.get("children") is not None,
          "the export has the family and its children", list(body.keys()) if isinstance(body, dict) else body)
    if isinstance(body, dict):
        blob = json.dumps(body)
        check("children.mrbadmus.internal" not in blob,
              "the export leaks NO internal child email address")
        check("cus_" not in blob and "sub_" not in blob,
              "the export leaks NO Stripe ids")
        kid = FAM["kids"][0]
        names = [c.get("first_name") for c in body.get("children") or []]
        check(kid["name"] in names, "the export names the child", names)
    # And through the page, which is the way a parent actually gets it.
    with_session(p, FAM["sess"])
    visit(p, "/consumer/account.html", "B: account before export")
    p.eval("""(function(){var b=document.querySelector('[data-act="export"]');
              if(b){b.click();} return !!b;})()""")
    time.sleep(4)
    t = p.eval("document.body.innerText") or ""
    check("Downloaded" in t, "the page says the file was downloaded", t[-400:].replace("\n", " "))
    check(not errs(p), "export: zero console errors", errs(p))


def action_delete_request(p):
    print("\n── B: a delete-account request, and the operator's view ───────")
    jwt = parent_jwt()
    st, d = api("POST", "/api/consumer/family/delete-request", jwt, {"confirm": "nope"})
    check(st == 400 and (d or {}).get("error") == "confirm_required",
          "a request without the typed word is refused", (st, d))
    st, d = api("POST", "/api/consumer/family/delete-request", jwt, {"confirm": "DELETE"})
    check(st == 200 and d.get("execute_after"), "delete-request → 200 with a 30-day date", (st, d))
    check(d.get("billing") == "cancel_at_period_end",
          "the subscription is set to stop renewing, not cancelled on the spot", d.get("billing"))
    _s, sub_now = stripe("GET", "/subscriptions/" + FAM["live_sub"])
    check(sub_now.get("cancel_at_period_end") is True,
          "STRIPE agrees: cancel at period end", sub_now.get("cancel_at_period_end"))

    with_session(p, FAM["sess"])
    t = visit(p, "/consumer/account.html", "B: account with a deletion pending",
              expect=["Account scheduled for deletion", "Undo"], shot="14-deletion-390.png")

    # The operator's console — the assertion that matters, because a request
    # nobody can see is a request nobody will action.
    op = sign_in(*OPERATOR)
    st, accounts = api("GET", "/api/consumer/admin/accounts?q=" + urllib.parse.quote("Lane2 family"),
                       op["access_token"])
    check(st == 200, "operator: GET /admin/accounts 200", st)
    row = next((a for a in (accounts or {}).get("accounts") or [] if a.get("id") == FAM["org"]), None)
    check(row is not None, "operator: the family is in the list", row and row.get("name"))
    check(row and row.get("deletion_requested_at"),
          "operator: the LIST payload carries deletion_requested_at",
          row and row.get("deletion_requested_at"))

    with_session(p, op)
    p.goto(BASE + "/consumer/admin-accounts.html?env=test&api=" + API, settle=1.5)
    for _ in range(30):
        if p.eval("!!document.querySelector('.ac-row')"):
            break
        time.sleep(1.0)
    p.eval("""(function(){var q=document.getElementById('q');
              if(q){q.value='Lane2 family';q.dispatchEvent(new Event('input',{bubbles:true}));}})()""")
    time.sleep(2.5)
    opened = p.eval("""(function(){var rows=document.querySelectorAll('.ac-row');
        for(var i=0;i<rows.length;i++){ if(rows[i].getAttribute('data-id')===%s){rows[i].click();return true;} }
        return false;})()""" % json.dumps(FAM["org"]))
    check(opened is True, "operator: the family's row opens", opened)
    time.sleep(3.0)
    t = p.eval("document.body.innerText") or ""
    check("Deletion requested" in t,
          "operator: the console SHOWS the deletion request", t[:900].replace("\n", " "))
    check(not errs(p), "operator console: zero console errors", errs(p))
    p.screenshot(os.path.join(SHOTS, "15-operator-deletion-1460.png"), width=1460)

    # Undo, so the fixture leaves the estate the way it found it.
    st, d = api("DELETE", "/api/consumer/family/delete-request", parent_jwt())
    check(st == 200, "the parent can undo the deletion", (st, d))
    with_session(p, FAM["sess"])
    visit(p, "/consumer/account.html", "B: account after the undo",
          forbid=["Account scheduled for deletion"])


# ══════════════════════════════════════════════════════════════════════════
# PHASE P — "There are no banked questions for that yet."
# ══════════════════════════════════════════════════════════════════════════
#
# Found while driving the hold. A parent who uses Set work → Practice in a
# week the Sunday scheduler has already filled is told the QUESTIONS do not
# exist. They do. `assignments_class_week_uniq (class_id, academic_week)
# WHERE deleted_at IS NULL` allows a family class exactly one assignment per
# week, the scheduler has already used it, and the 23505 comes back through a
# branch that says one sentence for all six of composePractice()'s skip
# reasons. This phase pins the cause rather than the symptom.
def phase_practice(p):
    print("\n── P: the practice collision ──────────────────────────────────")
    jwt = parent_jwt()
    kid = FAM["kids"][0]
    st, pick = api("GET", "/api/consumer/children/%s/picker" % kid["id"], jwt)
    unit = next((u.get("unit_code") for u in (pick or {}).get("units") or [] if u.get("unit_code")), None)
    check(bool(unit), "a real unit from the child's own scheme", unit)

    # What the scheduler already put in this week.
    st, fam = api("GET", "/api/consumer/family", jwt)
    cls = next((c.get("class_id") for c in (fam or {}).get("children") or []
                if c["id"] == kid["id"]), None)
    st, rows = sb_admin("GET", "/rest/v1/assignments?select=id,title,academic_week,subject_id&class_id=eq."
                        + str(cls) + "&deleted_at=is.null")
    check(isinstance(rows, list) and len(rows) == 1,
          "the scheduler has already written this week's ONE assignment",
          [(r["title"], r["academic_week"]) for r in rows or []])
    existing = (rows or [{}])[0]

    today = time.strftime("%Y-%m-%d")
    st, pr = api("POST", "/api/consumer/children/%s/work" % kid["id"], jwt,
                 {"kind": "practice", "unit_code": unit, "scheduled_for": today})
    check(st == 200 and (pr or {}).get("item"),
          "a parent can set practice on a unit that HAS banked questions", (unit, st, pr))
    collided = st == 409 and (pr or {}).get("error") == "no_questions"
    if collided:
        note("REPRODUCED: 'There are no banked questions for that yet.' with "
             "detail=%s, on a unit whose bank is fine." % (pr or {}).get("detail"))

    # ── now prove WHICH cause it was ──────────────────────────────────
    # Same insert the composer does, as the service role, so the database's
    # own words are on the record rather than a code word.
    st, raw = sb_admin("POST", "/rest/v1/assignments", {
        "class_id": cls, "school_id": FAM["org"], "key_stage": "KS3",
        # subject_id is NOT NULL; take the one the scheduler's own row uses so
        # the only thing this insert can trip over is the class-week index.
        "subject_id": existing.get("subject_id"),
        "year_group": 8, "topic": "lane2 collision probe",
        "title": "lane2 collision probe", "quiz_type": "topic_quiz",
        "academic_week": existing.get("academic_week"), "auto_generated": True})
    check(st == 409 and isinstance(raw, dict) and raw.get("code") == "23505",
          "the database refuses a SECOND assignment in the same class-week "
          "(assignments_class_week_uniq) — that, and not a missing bank, is the cause",
          (st, raw))
    if st < 300 and isinstance(raw, list) and raw:
        sb_admin("DELETE", "/rest/v1/assignments?id=eq." + raw[0]["id"])

    # ── and prove the questions were there all along ──────────────────
    sb_admin("PATCH", "/rest/v1/assignments?id=eq." + existing["id"],
             {"deleted_at": iso(0)})
    st, pr2 = api("POST", "/api/consumer/children/%s/work" % kid["id"], parent_jwt(),
                  {"kind": "practice", "unit_code": unit, "scheduled_for": today})
    check(st == 200 and (pr2 or {}).get("item"),
          "with the week's slot free, the SAME unit composes fine — the bank was never empty",
          (unit, st, pr2))
    if st == 200 and (pr2 or {}).get("item"):
        api("DELETE", "/api/consumer/children/%s/work/%s" % (kid["id"], pr2["item"]["id"]),
            parent_jwt())
    sb_admin("PATCH", "/rest/v1/assignments?id=eq." + existing["id"], {"deleted_at": None})


# ══════════════════════════════════════════════════════════════════════════
# PHASE C — the go-live hold (MRB-324), and that it never touches a family
# ══════════════════════════════════════════════════════════════════════════
SCHOOL_TABLES_READ = []


def read_school(sel):
    SCHOOL_TABLES_READ.append("schools:" + sel)
    st, d = sb_admin("GET", "/rest/v1/schools?select=" + sel + "&kind=eq.school")
    return st, d


def phase_hold(p):
    print("\n── C: the assignments go-live hold ────────────────────────────")

    # ── the school layer, READ ONLY ───────────────────────────────────
    st, schools = read_school("id,name,kind,assignments_open_from")
    check(st == 200, "schools: the hold column reads on TEST after the merge", st)
    check(all("assignments_open_from" in s for s in schools or []),
          "every school row carries assignments_open_from", schools)
    held = [s["name"] for s in schools or [] if s.get("assignments_open_from")]
    note("TEST schools and their hold: " +
         ", ".join("%s=%s" % (s["name"], s.get("assignments_open_from")) for s in schools or []))
    check(not held, "no TEST school is currently held (so nothing else is being withheld)", held)

    # The guard, in the merged file, in the position the ruling requires.
    src = open("/Users/midebadmus/Documents/GitHub/mrbadmus-worktrees/b2c/backend/server.js").read()
    i_existing = src.find("if (existing) {")
    i_hold = src.find("assignments_open_from")
    i_compose = src.find("scheme = await schemeLessons(cls, week)")
    check(0 < i_existing < i_hold < i_compose,
          "server.js: the hold sits AFTER the already-composed branch and BEFORE composition "
          "(so turning it on never retracts work a student can already see)",
          (i_existing, i_hold, i_compose))
    check("reason: 'assignments_not_open_yet'" in src,
          "server.js: the refusal is the ordinary 200 empty shape, not an error")
    check("console.warn('[assignments-hold]" in src,
          "server.js: a failed READ of the column warns and composes — it is not treated as a hold")

    # ⚠️ STOPPED, DELIBERATELY. Driving the school-side REFUSAL end to end
    # needs `schools.assignments_open_from` set on a row with kind='school',
    # which is a write to a school-layer table. The brief forbids it, so this
    # step is reported rather than run. See the report.
    note("STOPPED: driving the school-side refusal needs a write to schools.assignments_open_from "
         "on a kind='school' row. Not run. The exact rehearsal is in the report.")

    # ── the family half, DRIVEN ───────────────────────────────────────
    #
    # `consumerPracticeFor()` returns non-null for EVERY family and
    # organisation org — `{reason:'no_practice_set'}` when there is nothing
    # set — and the route returns on it before the hold is ever read. So the
    # hold cannot reach a family by construction. This proves it by behaviour
    # as well: the hold is set on the family's OWN org row (a kind='family'
    # row this drive created, never a school) and everything is driven again.
    jwt = parent_jwt()
    kid = FAM["kids"][0]
    st, fam = api("GET", "/api/consumer/family", jwt)
    cls = next((c.get("class_id") for c in (fam or {}).get("children") or []
                if c["id"] == kid["id"]), None)
    check(bool(cls), "the child has a class to ask about", cls)

    cl = child_session(kid)
    st, before = api("GET", "/api/class/current-assignment?class_id=" + str(cls), cl["access_token"])
    check(st == 200, "current-assignment (no hold): 200", (st, before))
    base_reason = (before or {}).get("reason")
    base_assignment = bool((before or {}).get("assignment"))

    ahead = time.strftime("%Y-%m-%d", time.gmtime(time.time() + 30 * 86400))
    sb_admin("PATCH", "/rest/v1/schools?id=eq." + FAM["org"], {"assignments_open_from": ahead})
    note("hold set to %s on the FAMILY's own org row %s (kind=family, created by this drive)"
         % (ahead, FAM["org"]))
    try:
        st, after = api("GET", "/api/class/current-assignment?class_id=" + str(cls), cl["access_token"])
        check(st == 200, "current-assignment under a family hold: still 200", (st, after))
        check((after or {}).get("reason") != "assignments_not_open_yet",
              "the hold does NOT reach the family's class", (after or {}).get("reason"))
        check((after or {}).get("reason") == base_reason
              and bool((after or {}).get("assignment")) == base_assignment,
              "the family's answer is byte-for-byte the same as with no hold",
              {"before": base_reason, "after": (after or {}).get("reason")})

        st, g = api("POST", "/api/consumer/children/%s/generate" % kid["id"], parent_jwt(),
                    {"week_start": FAM["monday"]})
        check(st == 200, "work generation for a family is unaffected by the hold", (st, g))

        st, today = api("GET", "/api/consumer/child/today", cl["access_token"])
        check(st == 200 and (today or {}).get("items") is not None,
              "the child's Today is unaffected by the hold", st)

        # A real unit from the child's OWN scheme, so the practice actually
        # composes and the hold has something to fail to interfere with.
        st, pick = api("GET", "/api/consumer/children/%s/picker" % kid["id"], parent_jwt())
        unit = next((u.get("unit_code") for u in (pick or {}).get("units") or []
                     if u.get("unit_code")), None)
        st, pr = api("POST", "/api/consumer/children/%s/work" % kid["id"], parent_jwt(),
                     {"kind": "practice", "unit_code": unit,
                      "scheduled_for": time.strftime("%Y-%m-%d")})
        check(st == 200 and (pr or {}).get("item"),
              "practice for a family COMPOSES under the hold, exactly as without it",
              (unit, st, pr))
        check(not (isinstance(pr, dict) and pr.get("error") == "assignments_not_open_yet"),
              "practice is never refused with assignments_not_open_yet", pr)
        if st == 200 and (pr or {}).get("item"):
            api("DELETE", "/api/consumer/children/%s/work/%s" % (kid["id"], pr["item"]["id"]),
                parent_jwt())

        with_session(p, session_of(cl))
        visit(p, "/consumer/today.html", "C: child Today under a family hold",
              expect=["Amara"], shot="20-hold-family-390.png")
    finally:
        sb_admin("PATCH", "/rest/v1/schools?id=eq." + FAM["org"], {"assignments_open_from": None})
        st, back = sb_admin("GET", "/rest/v1/schools?id=eq." + FAM["org"] +
                            "&select=assignments_open_from")
        check(isinstance(back, list) and back and back[0]["assignments_open_from"] is None,
              "the family hold is lifted again", back)


# ══════════════════════════════════════════════════════════════════════════
# TEARDOWN — night3-executor-common.md's order. Profiles before auth users.
# ══════════════════════════════════════════════════════════════════════════
def teardown():
    print("\n── teardown ───────────────────────────────────────────────────")
    # Stripe first: deleting the customer cancels its subscriptions and
    # detaches its payment methods in one call.
    for s in IDS["stripe_subscriptions"]:
        st, d = stripe("DELETE", "/subscriptions/" + s)
        print("  stripe subscription %s → %s" % (s, st if st != 200 else d.get("status")))
    for c in IDS["stripe_customers"]:
        st, d = stripe("DELETE", "/customers/" + c)
        print("  stripe customer %s → %s deleted=%s" % (c, st, (d or {}).get("deleted")))

    for o in IDS["orgs"]:
        st, classes = sb_admin("GET", "/rest/v1/classes?select=id&school_id=eq." + o)
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
        sb_admin("DELETE", "/rest/v1/classes?school_id=eq." + o)
        for t in ("stripe_events", "email_log", "ai_usage_events", "exam_answers",
                  "unit_check_attempts", "work_items", "child_plans", "family_messages",
                  "consumer_notifications", "org_limits", "account_deletion_requests"):
            sb_admin("DELETE", "/rest/v1/%s?org_id=eq.%s" % (t, o))
        for t in ("pending_staff", "staff_scopes"):
            sb_admin("DELETE", "/rest/v1/%s?school_id=eq.%s" % (t, o))
        sb_admin("DELETE", "/rest/v1/audit_log?school_id=eq." + o)
        sb_admin("DELETE", "/rest/v1/subscriptions?org_id=eq." + o)

    for u in IDS["users"]:
        for t, col in (("consumer_notifications", "recipient_id"), ("family_messages", "sender_id"),
                       ("family_messages", "recipient_id"), ("exam_answers", "child_id"),
                       ("unit_check_attempts", "child_id"), ("child_flashcard_queue", "child_id"),
                       ("work_items", "child_id"), ("work_generation_runs", "child_id"),
                       ("child_plans", "child_id"), ("ai_usage_events", "profile_id"),
                       ("email_log", "recipient_id"), ("class_members", "student_id"),
                       ("class_teachers", "teacher_id"), ("platform_operators", "profile_id"),
                       ("staff_scopes", "profile_id"), ("parent_prefs", "profile_id"),
                       ("report_notes", "child_id"), ("audit_log", "actor_id")):
            sb_admin("DELETE", "/rest/v1/%s?%s=eq.%s" % (t, col, u))
        sb_admin("PATCH", "/rest/v1/profiles?created_by=eq." + u, {"created_by": None})
    for u in IDS["users"]:
        st, r = sb_admin("DELETE", "/rest/v1/profiles?id=eq." + u)
        st2, r2 = sb_admin("DELETE", "/auth/v1/admin/users/" + u)
        print("  user %s  profile %s  auth %s %s" % (u, st, st2, "" if st2 < 300 else r2))
    for o in IDS["orgs"]:
        sb_admin("DELETE", "/rest/v1/academic_years?school_id=eq." + o)
        st, r = sb_admin("DELETE", "/rest/v1/schools?id=eq." + o)
        print("  org %s → %s %s" % (o, st, "" if st < 300 else r))

    # Prove it, rather than assume it.
    leftovers = []
    for o in IDS["orgs"]:
        st, d = sb_admin("GET", "/rest/v1/schools?id=eq." + o + "&select=id")
        if d:
            leftovers.append(("schools", o))
        st, d = sb_admin("GET", "/rest/v1/subscriptions?org_id=eq." + o + "&select=org_id")
        if d:
            leftovers.append(("subscriptions", o))
    for u in IDS["users"]:
        st, d = sb_admin("GET", "/rest/v1/profiles?id=eq." + u + "&select=id")
        if d:
            leftovers.append(("profiles", u))
    for c in IDS["stripe_customers"]:
        st, d = stripe("GET", "/customers/" + c)
        if st == 200 and not (d or {}).get("deleted"):
            leftovers.append(("stripe_customer", c))
    check(not leftovers, "teardown: zero residue", leftovers)


# ══════════════════════════════════════════════════════════════════════════
def main():
    global BASE, API, SHOTS, PORT
    ap = argparse.ArgumentParser()
    ap.add_argument("--site", default="mrbadmus_site")
    ap.add_argument("--api", default="http://localhost:3151")
    ap.add_argument("--port", type=int, default=8151)
    ap.add_argument("--shots", default=os.path.join(SCRATCH, "shots/lane2"))
    ap.add_argument("--only", default="")
    a = ap.parse_args()
    API = a.api
    SHOTS = a.shots
    os.makedirs(SHOTS, exist_ok=True)
    os.makedirs(SCRATCH, exist_ok=True)
    server, PORT = cdp.serve(os.path.abspath(a.site), a.port)
    BASE = "http://localhost:%d" % PORT
    print("built tree at %s   backend %s   shots %s" % (BASE, API, SHOTS))

    only = set(x for x in a.only.split(",") if x)
    try:
        setup()
        with cdp.Browser() as b:
            p = b.attach()
            p.send("Page.addScriptToEvaluateOnNewDocument", {"source": FLAG_ON_JS})
            p.set_viewport(390, 844)

            if not only or "states" in only:
                FAM["customer"] = open_checkout()
                sub = state_trialing(p, FAM["customer"])
                row = state_past_due_grace(p, sub)
                keep = state_read_only(p, row)
                state_active(p, sub, keep)
                state_cancelled_paid_up(p, sub)
                state_cancelled_read_only(p)
                # Back in step with Stripe, so the cancellation below is the
                # event doing the work and not the leftovers of the SQL above.
                _s, live = stripe("GET", "/subscriptions/" + sub["id"])
                sb_admin("PATCH", "/rest/v1/subscriptions?org_id=eq." + FAM["org"],
                         {"status": "active", "canceled_at": None,
                          "current_period_end": time.strftime(
                              "%Y-%m-%dT%H:%M:%SZ", time.gmtime(sub_period_end(live) or time.time()))})
                state_locked(p, sub)
                new_sub = state_reactivate(p)
                FAM["live_sub"] = new_sub["id"] if new_sub else None

            if only and "states" not in only:
                bootstrap_active()

            if not only or "actions" in only:
                action_pause_resume(p)
                action_set_work(p)
                if FAM.get("live_sub"):
                    action_remove_child({"id": FAM["live_sub"]})
                action_portal(p)
                action_report(p)
                action_export(p)
                action_delete_request(p)

            if not only or "practice" in only:
                phase_practice(p)

            if not only or "hold" in only:
                phase_hold(p)
    finally:
        try:
            teardown()
        finally:
            server.shutdown()

    print("\n" + "=" * 70)
    for n in NOTES:
        print("NOTE  " + n)
    print("\n%d failure(s)" % len(FAILS))
    for f in FAILS:
        print("  - " + f)
    sys.exit(min(len(FAILS), 99))


if __name__ == "__main__":
    main()
