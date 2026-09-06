#!/usr/bin/env python3
"""mrb327_marketing_drive.py — MRB-327 §8 MARKETING SCREENSHOTS.

    cd .../b2c/backend && CONSUMER_SIGNUP_ENABLED=true PORT=3191 \
        EXTRA_CORS_ORIGINS=http://localhost:8191 node server.js
    python3 mrb327_marketing_drive.py --api http://localhost:3191 --port 8191

Builds ONE believable family on TEST through the real routes, marks one answer
through the real operator queue, shoots the six surfaces at desktop and 390px,
then deletes every row it made.

Phases:
  S  seed      — parent, two children, this week's work, chat, exam answer
  M  mark      — the operator marks the answer in /consumer/admin-queue.html
  R  report    — backfill the SUMMER 2026 term so the termly report has a term
  P  shoot     — the screenshots
  T  teardown

Modelled on admin_ui_drive.py: same FLAG_ON_JS, same with_session(), same
built-tree-only rule.
"""
import argparse, json, os, ssl, sys, time, urllib.request, urllib.error, datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ks3_browser as cdp

SB = "https://qeppkiswvclkkwbxmlok.supabase.co"
CTX = ssl.create_default_context(cafile="/etc/ssl/cert.pem")
ROOT = "/Users/midebadmus/Documents/GitHub/mrbadmus-worktrees/b2c/launch"
SCRATCH = ("/private/tmp/claude-501/-Users-midebadmus-Documents-GitHub-mrbadmus-"
           "worktrees-b2c-launch/06d799b1-12f9-481b-9871-424a2321715f/scratchpad")
STATE_FILE = os.path.join(SCRATCH, "mrb327_marketing_fixtures.json")
SHOTS = os.path.join(ROOT, "docs/b2c/marketing")

OPERATOR = ("hz_op@test.mrbadmus", "Night3!Op")
PARENT_EMAIL = "mkt327-prescott@mrbadmus-test.com"
PARENT_PW = "Passw0rd!mkt327"
CHILD_PW = "harbour-lantern-42"
FAMILY_NAME = "The Prescott family"
TAG = "mkt327"

# The question the exam-feedback shot is built on: a real seeded KS3 item,
# four marks, four scheme points, third-person mark-scheme voice.
EXAM_Q = "ks3-b1-specialised-cells-explain"

# Verified against the shipped marker BEFORE it was used: it earns scheme
# points 1-3 and misses point 4 (it never gets to what the water is FOR), so
# the instant mark on screen is 3/4 with three real ticks and one real cross.
# Nothing about the mark is arranged after the fact.
ELLIE_ANSWER = (
    "The root hair cell is pulled out into a long thin hair, so it has a much larger surface "
    "area than a round cell of the same volume would have. Water and the dissolved minerals "
    "can only enter through the surface, so more surface means a faster rate of absorption. "
    "The hair also reaches in between the soil particles, which is where the water actually "
    "is, so it can get to water that a rounder cell would never reach."
)

# Mr Badmus's own marking. Written in his voice: names what the answer did,
# names the one thing it did not, and says what to do next.
MB_FEEDBACK = (
    "This is a strong answer, Ellie. You have the surface area point and, better than that, "
    "you explained WHY surface area matters here rather than just naming it. The bit about "
    "the hair reaching between the soil particles is the detail most students miss. "
    "One thing to add next time: you mentioned staying firm, but not the minerals the plant "
    "needs to keep growing. Get both halves of \"what the water is for\" in and this is full marks."
)

# ⊕ DEVIATION, declared. The INSTANT mark on the exam screen (score 3/4 and
# the three ticks) is genuinely computed by the shipped marker and is left
# exactly as it came back. Its NOTE is not: TEST has no ANTHROPIC_API_KEY, so
# `markingSystemPrompt` never runs and the keyword-stub adapter answers
# instead. Its string ("Got 3 of 4 points. Missing: <mark scheme point cut off
# mid-word>…. Next step: …") is a fallback nobody sees in production, and a
# marketing shot of it would misdescribe the product rather than show it. So
# the note — and ONLY the note — is replaced with one sentence in the register
# the real marker writes in. Reported, not hidden.
AI_NOTE = (
    "Three of the four points, and all three are explained rather than just named. "
    "The missing one is what the water is FOR once it is inside the plant. "
    "Next step: finish the chain — enough water to stay firm, enough minerals to keep growing."
)

CHAT = [
    ("parent", "Morning love — I've put the endothermic reactions lesson on for today. "
               "Do that one before you go out, it's only twenty minutes."),
    ("child",  "ok can i do it after football"),
    ("parent", "Yes that's fine. Just not at bedtime again!"),
    ("child",  "i sent the root hair question to mr badmus btw"),
    ("parent", "Well done. He usually gets back within a couple of days."),
]

FAILS = []


def check(ok, label, evidence=""):
    print(("  OK  " if ok else "  XX  ") + label + (("  — " + str(evidence)[:300]) if evidence else ""))
    if not ok:
        FAILS.append(label)


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


FLAG_ON_JS = ("(function(){var c=null;Object.defineProperty(window,'MrBadmusConfig',"
              "{configurable:true,get:function(){return c;},"
              "set:function(v){ if(v&&typeof v==='object'){v.CONSUMER_SIGNUP_ENABLED=true;} c=v; }});})();")


def qs(path):
    return BASE + path + ("&" if "?" in path else "?") + "env=test&api=" + API


def with_session(p, sess):
    p.goto(BASE + "/404.html?env=test", settle=0.2)
    p.eval("localStorage.clear()")
    p.eval("localStorage.setItem('sb-qeppkiswvclkkwbxmlok-auth-token', %s)"
           % json.dumps(json.dumps(sess)))


def wait_for(p, expr, tries=50, gap=0.35):
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


def iso(dt):
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")


TODAY = datetime.date.today()
MONDAY = TODAY - datetime.timedelta(days=TODAY.weekday())


def child_session(child_id, password):
    """A REAL Supabase session for a child. The child's GoTrue address is the
    internal one made at creation; sign in on the anon client exactly as the
    browser would, so the SDK keeps the session instead of deleting it."""
    st, u = sb_admin("GET", "/auth/v1/admin/users/" + child_id)
    assert st == 200, (st, u)
    return sign_in(u["email"], password)


# ══════════════════════════════════════════════════════════════════════════
# S — seed
# ══════════════════════════════════════════════════════════════════════════
KIDS = [
    # first_name, year, username, mode, intensity
    ("Ellie", 9, "ellieprescott", "alongside_school", "steady"),
    ("Jack",  7, "jackprescott",  "alongside_school", "light"),
]


def seed():
    ids = {"users": [], "orgs": [], "answers": [], "kids": {}}
    print("\n── seed ──────────────────────────────────────────────────")

    st, d = sb_admin("POST", "/auth/v1/admin/users",
                     {"email": PARENT_EMAIL, "password": PARENT_PW, "email_confirm": True,
                      "user_metadata": {"first_name": "Hannah"}})
    if st >= 300:
        st2, users = sb_admin("GET", "/auth/v1/admin/users?per_page=1000")
        d = next(u for u in users["users"] if u["email"] == PARENT_EMAIL)
    parent = d["id"]
    ids["parent"] = parent
    ids["users"].append(parent)
    print("  parent Hannah Prescott", parent)

    sess = sign_in(PARENT_EMAIL, PARENT_PW)
    pjwt = sess["access_token"]
    st, fam = api("POST", "/api/consumer/family/ensure", pjwt, {"family_name": FAMILY_NAME})
    assert st == 200, (st, fam)
    org = fam["org_id"]
    ids["org"] = org
    ids["orgs"].append(org)
    print("  family org", org)

    # A family a term in, now a week into the autumn term: trialing is the
    # wrong billing state for that story, so it is an ordinary paid family.
    sb_admin("PATCH", "/rest/v1/subscriptions?org_id=eq." + org, {
        "status": "active", "trial_end": None, "quantity": 2,
        "billing_interval": "month",
        "current_period_end": iso(datetime.datetime.utcnow() + datetime.timedelta(days=22)),
        "stripe_customer_id": "cus_mkt327_prescott"})

    for first, year, uname, mode, intensity in KIDS:
        st, c = api("POST", "/api/consumer/children", pjwt, {
            "first_name": first, "year_group": year, "username": uname,
            "password": CHILD_PW, "mode": mode, "intensity": intensity,
            "exam_board": "AQA"})
        assert st == 200, (first, st, c)
        ids["kids"][first] = {"id": c["child_id"], "year": year, "username": uname}
        ids["users"].append(c["child_id"])
        print("  child %-6s Y%d  %s  %s" % (first, year, uname, c["child_id"]))

    # ── the family joined in the summer term; backdate so the account does
    #    not read as one day old on any surface that shows "since".
    joined = iso(datetime.datetime.utcnow() - datetime.timedelta(days=132))
    sb_admin("PATCH", "/rest/v1/schools?id=eq." + org, {"created_at": joined})
    for k in ids["kids"].values():
        sb_admin("PATCH", "/rest/v1/profiles?id=eq." + k["id"], {"created_at": joined})

    # ── this week's work, from the REAL generator ──
    for first, meta in ids["kids"].items():
        st, g = api("POST", "/api/consumer/children/%s/generate" % meta["id"], pjwt,
                    {"week_start": MONDAY.isoformat(), "force": True})
        assert st == 200, (first, st, g)
        print("  %s week %s → %d items" % (first, MONDAY, len(g.get("items_list") or [])))
        for it in (g.get("items_list") or []):
            print("      %-9s %-46s %s" % (it.get("day"), it.get("title"), it.get("mins")))

    json.dump(ids, open(STATE_FILE, "w"), indent=1)
    return ids, pjwt


def shape_week(ids, pjwt):
    """Turn the generated week into a believable Sunday-morning state:
    Ellie five days done with today still open, Jack three days done."""
    print("\n── shaping the week ──────────────────────────────────────")
    plan = {
        # first: [(weekday index done, ...)]  Monday = 0
        "Ellie": [1, 2, 3, 4, 5],
        "Jack":  [3, 4, 5],
    }
    for first, meta in ids["kids"].items():
        st, rows = sb_admin(
            "GET", "/rest/v1/work_items?select=id,scheduled_for,title,kind,status"
                   "&child_id=eq.%s&week_start=eq.%s&order=scheduled_for.asc,position.asc"
            % (meta["id"], MONDAY.isoformat()))
        done_days = plan[first]
        marked = []
        for r in rows:
            d = datetime.date.fromisoformat(r["scheduled_for"])
            if d.weekday() in done_days and d <= TODAY:
                # done at a plausible after-school hour on its own day
                at = datetime.datetime(d.year, d.month, d.day, 17, 12 + (d.weekday() * 7) % 40)
                sb_admin("PATCH", "/rest/v1/work_items?id=eq." + r["id"],
                         {"status": "done", "done_at": iso(at)})
                marked.append((r["scheduled_for"], r["title"]))
        print("  %-6s done %d of %d" % (first, len(marked), len(rows)))
        for d, t in marked:
            print("      %s  %s" % (d, t))
    return ids


def seed_chat(ids, pjwt):
    print("\n── chat ──────────────────────────────────────────────────")
    ellie = ids["kids"]["Ellie"]["id"]
    cs = child_session(ellie, CHILD_PW)
    base = datetime.datetime.utcnow() - datetime.timedelta(hours=26)
    for i, (who, body) in enumerate(CHAT):
        when = base + datetime.timedelta(minutes=i * 37)
        st, r = sb_admin("POST", "/rest/v1/family_messages", {
            "org_id": ids["org"],
            "sender_id": ids["parent"] if who == "parent" else ellie,
            "recipient_id": ellie if who == "parent" else ids["parent"],
            "body": body, "created_at": iso(when),
            # everything but the last parent line has been read, so the child's
            # unread badge shows 1 rather than a wall of five.
            "read_at": None if i == len(CHAT) - 1 else iso(when + datetime.timedelta(minutes=4))})
        assert st < 300, (st, r)
    print("  %d messages seeded" % len(CHAT))
    return cs


def seed_exam(ids, cs):
    """Ellie answers the root-hair question through the REAL marking route,
    then sends it to Mr Badmus through the REAL route."""
    print("\n── exam answer ───────────────────────────────────────────")
    cjwt = cs["access_token"]
    st, m = api("POST", "/api/consumer/mark", cjwt,
                {"question_id": EXAM_Q, "answer": ELLIE_ANSWER})
    check(st == 200, "POST /api/consumer/mark → 200", (st, m))
    if st != 200:
        return ids
    aid = m.get("answer_id") or m.get("id")
    print("  instant mark %s/%s  answer %s" % (m.get("score"), m.get("max"), aid))
    ids["answers"].append(aid)
    ids["exam_answer"] = aid
    st, s = api("POST", "/api/consumer/exam-answers/%s/send-to-mb" % aid, cjwt)
    check(st == 200, "POST /send-to-mb → 200", (st, s))
    # sent yesterday, so the queue and the child's page both read as a real wait
    sb_admin("PATCH", "/rest/v1/exam_answers?id=eq." + aid,
             {"sent_to_mb_at": iso(datetime.datetime.utcnow() - datetime.timedelta(hours=30)),
              "ai_marked_at": iso(datetime.datetime.utcnow() - datetime.timedelta(hours=30, minutes=6)),
              "created_at": iso(datetime.datetime.utcnow() - datetime.timedelta(hours=30, minutes=8))})
    json.dump(ids, open(STATE_FILE, "w"), indent=1)
    return ids


# ══════════════════════════════════════════════════════════════════════════
# M — the operator marks it, in the real console
# ══════════════════════════════════════════════════════════════════════════
def phase_mark(ids):
    print("\n── operator marks the answer ─────────────────────────────")
    op = sign_in(*OPERATOR)
    aid = ids["exam_answer"]
    with cdp.Browser() as b:
        p = b.attach()
        p.send("Page.addScriptToEvaluateOnNewDocument", {"source": FLAG_ON_JS})
        with_session(p, op)
        p.goto(qs("/consumer/admin-queue.html"), settle=1.4)
        ok = wait_for(p, "document.querySelectorAll('.ad-item').length > 0")
        check(ok, "queue renders", text(p)[:160].replace("\n", " "))
        mine = p.eval("!!document.querySelector('.ad-item[data-id=\"%s\"]')" % aid)
        check(mine, "our answer is in the operator queue", aid)
        if not mine:
            return
        p.eval("document.querySelector('.ad-item[data-id=\"%s\"]').click()" % aid)
        ok = wait_for(p, "document.querySelectorAll('.ad-point').length > 0")
        check(ok, "the scheme checklist renders")
        pts = p.eval("document.querySelectorAll('.ad-point').length")
        on = p.eval("Array.prototype.map.call(document.querySelectorAll('.ad-point'),"
                    "function(e){return e.classList.contains('is-on');})")
        print("  scheme points %d, instant ticks %s" % (pts, on))
        # Mr Badmus's own mark: the answer earns points 1, 2 and 3 and misses
        # the fourth (it never mentions minerals). Set the checklist to exactly
        # that, whatever the instant marker thought.
        want = [True, True, True, False][:pts]
        for i, w in enumerate(want):
            if on[i] != w:
                p.eval("document.querySelectorAll('.ad-point')[%d].click()" % i)
                time.sleep(0.25)
        score = p.eval("document.querySelector('.ad-score').textContent")
        check(score.startswith("3"), "operator's score reads 3 of %d" % pts, score)
        p.eval("(function(t){var n=document.getElementById('note');n.value=t;"
               "n.dispatchEvent(new Event('input'));})(%s)" % json.dumps(MB_FEEDBACK))
        time.sleep(0.3)
        check(p.eval("document.getElementById('send-btn').disabled") is False, "Send is enabled")
        p.eval("document.getElementById('send-btn').click()")
        wait_for(p, "!document.querySelector('.ad-item[data-id=\"%s\"]')" % aid, tries=40, gap=0.5)
    st, row = sb_admin("GET", "/rest/v1/exam_answers?select=status,mb_score,mb_feedback,mb_marked_at"
                              "&id=eq." + aid)
    r = (row or [{}])[0]
    check(r.get("status") == "mb_marked", "the answer is mb_marked in the database", r.get("status"))
    check(r.get("mb_feedback") == MB_FEEDBACK, "his words landed verbatim")
    print("  mb_score %s  marked %s" % (r.get("mb_score"), r.get("mb_marked_at")))
    # marked this morning, so the child's page reads "Marked ..." recently
    sb_admin("PATCH", "/rest/v1/exam_answers?id=eq." + aid,
             {"mb_marked_at": iso(datetime.datetime.utcnow() - datetime.timedelta(hours=5)),
              # see AI_NOTE above — the stub's note, not the product's, is the
              # only field in the whole set that a real marker did not produce
              "ai_feedback": AI_NOTE})



# ══════════════════════════════════════════════════════════════════════════
# W — the work Hannah set herself, through the real route
# ══════════════════════════════════════════════════════════════════════════
# An engaged parent tops the week up. That is the product's own flow
# (POST /children/:id/work), it is what the chat thread refers to, and it is
# what makes a five-day streak reachable for a child on two generated
# sessions a week.
PARENT_WORK = {
    "Ellie": [
        # days back from today, kind, args, done?
        (4, "lesson",   {"lesson_slug": "exothermic-reactions"},   True),
        (2, "lesson",   {"lesson_slug": "alcohol-and-smoking"},    True),
        (0, "lesson",   {"lesson_slug": "endothermic-reactions"},  False),
    ],
    "Jack": [
        (2, "lesson",   {"lesson_slug": "distance-time-graphs"},   True),
        # ⚠️ Saturday was meant to be a practice item. A parent cannot set one:
        # `assignments_class_week_uniq` is UNIQUE (class_id, academic_week) and
        # the generator has already used this class's slot for the week, so
        # every parent-set practice in a generated week dies on the insert and
        # the parent is told "There are no banked questions for that yet."
        # Reported, not worked around in the product — only in this fixture.
        (1, "lesson",   {"lesson_slug": "particle-model"},         True),
        (0, "lesson",   {"lesson_slug": "relative-motion"},        False),
    ],
}

# Which of the GENERATED items each child finished. Weekday index, Monday = 0.
GENERATED_DONE = {"Ellie": [1, 3, 5], "Jack": [1, 3]}


def phase_work(ids, pjwt):
    print("\n── the week ──────────────────────────────────────────────")
    for first, meta in ids["kids"].items():
        # re-runnable: drop anything Hannah set on a previous pass
        sb_admin("DELETE", "/rest/v1/work_items?child_id=eq.%s&week_start=eq.%s&set_by=eq.%s"
                 % (meta["id"], MONDAY.isoformat(), ids["parent"]))
        # 1. the generated items
        st, rows = sb_admin(
            "GET", "/rest/v1/work_items?select=id,scheduled_for,title,status"
                   "&child_id=eq.%s&week_start=eq.%s&order=scheduled_for.asc,position.asc"
            % (meta["id"], MONDAY.isoformat()))
        for r in (rows or []):
            d = datetime.date.fromisoformat(r["scheduled_for"])
            want = d.weekday() in GENERATED_DONE[first] and d <= TODAY
            sb_admin("PATCH", "/rest/v1/work_items?id=eq." + r["id"],
                     ({"status": "done", "done_at": iso(datetime.datetime(d.year, d.month, d.day, 17, 40))}
                      if want else {"status": "set", "done_at": None}))
        # 2. what Hannah set
        for back, kind, args, done in PARENT_WORK[first]:
            day = TODAY - datetime.timedelta(days=back)
            body = dict(args); body["kind"] = kind; body["scheduled_for"] = day.isoformat()
            st, out = api("POST", "/api/consumer/children/%s/work" % meta["id"], pjwt, body)
            check(st == 200, "%s: Hannah sets %s for %s" % (first, kind, day), (st, out))
            if st != 200:
                continue
            if done:
                sb_admin("PATCH", "/rest/v1/work_items?id=eq." + out["item"]["id"],
                         {"status": "done",
                          "done_at": iso(datetime.datetime(day.year, day.month, day.day, 18, 20))})
        # 3. what the week now says
        st, rows = sb_admin(
            "GET", "/rest/v1/work_items?select=scheduled_for,title,status,set_by"
                   "&child_id=eq.%s&week_start=eq.%s&status=neq.removed"
                   "&order=scheduled_for.asc" % (meta["id"], MONDAY.isoformat()))
        days = sorted(set(r["scheduled_for"] for r in rows if r["status"] == "done"))
        print("  %-6s %d items, %d done on %d days" %
              (first, len(rows), sum(1 for r in rows if r["status"] == "done"), len(days)))
        for r in rows:
            print("      %s  %-9s %-46s %s" % (r["scheduled_for"],
                  datetime.date.fromisoformat(r["scheduled_for"]).strftime("%a"),
                  r["title"][:46], r["status"]))


# ══════════════════════════════════════════════════════════════════════════
# U — real unit checks, sat through the real routes
# ══════════════════════════════════════════════════════════════════════════
# The server shuffles a question's options with a deterministic PRNG seeded on
# (attempt_id, question_id) and never tells the client which option is right.
# Replicating that here is the only way to sit a check at a CHOSEN accuracy
# instead of guessing at 25%. Same FNV-1a, same mulberry32, same Fisher-Yates.
def _hash32(s):
    h = 2166136261
    for ch in s:
        h ^= ord(ch)
        h = (h * 16777619) & 0xFFFFFFFF
    return h


def _mulberry32(seed):
    a = [seed & 0xFFFFFFFF]

    def nxt():
        a[0] = (a[0] + 0x6D2B79F5) & 0xFFFFFFFF
        t = (a[0] ^ (a[0] >> 15)) * (1 | a[0]) & 0xFFFFFFFF
        t = ((t + ((t ^ (t >> 7)) * (61 | t) & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ t
        return ((t ^ (t >> 14)) & 0xFFFFFFFF) / 4294967296.0
    return nxt


def _option_order(attempt_id, question_id, n):
    rng = _mulberry32(_hash32("%s:%s" % (attempt_id, question_id)))
    out = list(range(n))
    for i in range(len(out) - 1, 0, -1):
        j = int(rng() * (i + 1))
        out[i], out[j] = out[j], out[i]
    return out


def sit_check(child_id, cjwt, unit_code, wrong_n, when):
    """Sit one unit check for real, deliberately dropping `wrong_n` marks."""
    st, s = api("POST", "/api/consumer/child/unit-check/start", cjwt, {"unit_code": unit_code})
    if st != 200:
        check(False, "unit-check/start %s" % unit_code, (st, s))
        return None
    attempt = s["attempt_id"]
    st, rows = sb_admin("GET", "/rest/v1/unit_check_attempts?select=question_ids&id=eq." + attempt)
    qids = rows[0]["question_ids"]
    st, bank = sb_admin("GET", "/rest/v1/ks3_assignment_bank?select=id,options&id=in.(%s)"
                        % ",".join('"%s"' % q for q in qids))
    by = {r["id"]: r["options"] for r in bank}
    answers = []
    dropped = 0
    for qid in qids:
        opts = by[qid]
        order = _option_order(attempt, qid, len(opts))
        right = next(i for i, orig in enumerate(order) if opts[orig].get("correct") is True)
        if dropped < wrong_n:
            answers.append({"id": qid, "chosen": (right + 1) % len(opts)})
            dropped += 1
        else:
            answers.append({"id": qid, "chosen": right})
    st, r = api("POST", "/api/consumer/child/unit-check/submit", cjwt,
                {"attempt_id": attempt, "answers": answers})
    if st != 200:
        check(False, "unit-check/submit %s" % unit_code, (st, r))
        return None
    # backdate the sitting so it reads as part of the term's history
    sb_admin("PATCH", "/rest/v1/unit_check_attempts?id=eq." + attempt,
             {"started_at": iso(when), "completed_at": iso(when + datetime.timedelta(minutes=11))})
    print("  %s  %s  %s/%s (%s%%)" % (unit_code, when.date(), r.get("score"), r.get("max"), r.get("pct")))
    return attempt


# A term of sittings. Two children, real units from their own schemes, scores
# that go up but not in a straight line — which is what a real term looks like.
CHECKS = {
    "Ellie": [("B6", 132, 4), ("C7", 104, 3), ("B6", 76, 2), ("C7", 47, 3), ("C9", 19, 1)],
    "Jack":  [("P3", 118, 5), ("C1", 90, 4), ("P3", 61, 3), ("C1", 26, 4)],
}


def phase_checks(ids):
    print("\n── unit checks ───────────────────────────────────────────")
    ids.setdefault("attempts", [])
    for first, meta in ids["kids"].items():
        cs = child_session(meta["id"], CHILD_PW)
        print("  %s" % first)
        for unit, back, wrong in CHECKS[first]:
            when = datetime.datetime.utcnow() - datetime.timedelta(days=back)
            a = sit_check(meta["id"], cs["access_token"], unit, wrong, when)
            if a:
                ids["attempts"].append(a)
    json.dump(ids, open(STATE_FILE, "w"), indent=1)


# ══════════════════════════════════════════════════════════════════════════
# P — the screenshots
# ══════════════════════════════════════════════════════════════════════════
# Every tell that would give the shot away as a test artefact. Checked against
# the RENDERED TEXT of each page, not against the PNG.
TELLS = ["TEST", "test.mrbadmus", "sandbox", "Sandbox", "localhost", "127.0.0.1",
         "lorem", "Lorem", "4242", "MrBadmusAI", "undefined", "null", "NaN",
         "[object Object]", "Loading…", "env=test", "mrbadmus-test.com",
         "Not found", "placeholder", "TODO", "FIXME", "stub"]

SHOT_TEXT = {}


def tell_check(name, body):
    hits = [t for t in TELLS if t in body]
    SHOT_TEXT[name] = body
    check(not hits, "%s: no marketing tell in the rendered text" % name, hits)
    return hits


def shoot(p, name, url, width, height, ready, after=None, settle=1.6, tall=False):
    """Set the viewport BEFORE navigating — otherwise a desktop layout is
    captured and scaled, which is not a 390px layout at all."""
    p.set_viewport(width, height, settle=0.25)
    p.goto(url, settle=settle)
    ok = wait_for(p, ready, tries=60, gap=0.4)
    check(ok, "%s: rendered" % name, text(p)[:200].replace("\n", " "))
    if after:
        after(p)
        time.sleep(1.0)
    body = text(p)
    tell_check(name, body)
    path = os.path.join(SHOTS, name + ".png")
    if tall:
        # ⚠️ `report.html` ends in a `position: fixed` action bar. A full-page
        # capture paints it where the VIEWPORT is, i.e. across the middle of a
        # long page, hiding two rows of the units table. Growing the viewport
        # to the whole document instead puts it back at the foot where a reader
        # sees it. The page is untouched; only the camera moves.
        full = p.eval("Math.ceil(document.documentElement.scrollHeight)")
        p.set_viewport(width, min(int(full) + 8, 8000), settle=0.5)
        p.screenshot(path, width=width, height=min(int(full) + 8, 8000), full_page=False)
    else:
        p.screenshot(path, width=width, height=height)
    w, h = cdp.png_size(path)
    print("  shot → %-38s %dx%d" % (name + ".png", w, h))
    return path


READY_DASH = ("!!document.getElementById('c-main') && "
              "document.getElementById('c-main').textContent.indexOf('Loading') < 0 && "
              "document.getElementById('c-main').textContent.trim().length > 40")
READY_TODAY = "document.querySelectorAll('.td-item').length > 0"
READY_EXAM = "!!document.querySelector('.ex-human-fb')"
READY_REPORT = ("!!document.querySelector('.rpt-sheet') && "
                "document.getElementById('c-main').textContent.indexOf('Loading') < 0")


def open_child_chat(p):
    p.eval("document.getElementById('td-msg-btn').click()")


VIEWS = [("desktop", 1280, 900), ("mobile-390", 390, 844)]


def unread_again(ids):
    st, rows = sb_admin("GET", "/rest/v1/family_messages?select=id,created_at&org_id=eq.%s"
                               "&sender_id=eq.%s&order=created_at.desc&limit=1"
                        % (ids["org"], ids["parent"]))
    if rows:
        sb_admin("PATCH", "/rest/v1/family_messages?id=eq." + rows[0]["id"], {"read_at": None})


def phase_shoot(ids):
    print("\n── screenshots ───────────────────────────────────────────")
    ellie = ids["kids"]["Ellie"]["id"]
    parent_sess = sign_in(PARENT_EMAIL, PARENT_PW)
    child_sess = child_session(ellie, CHILD_PW)

    for label, w, h in VIEWS:
        # ── parent surfaces ──
        with cdp.Browser() as b:
            p = b.attach()
            p.send("Page.addScriptToEvaluateOnNewDocument", {"source": FLAG_ON_JS})
            with_session(p, parent_sess)
            # tall: the phone layout ends in a position:fixed tab bar, which a
            # full-page capture paints across the middle of the page.
            shoot(p, "01-parent-overview-" + label,
                  qs("/consumer/overview.html"), w, h, READY_DASH, tall=True)
            shoot(p, "02-child-detail-" + label,
                  qs("/consumer/overview.html?child=%s&view=child" % ellie), w, h, READY_DASH,
                  tall=True)
            shoot(p, "06a-parent-chat-" + label,
                  qs("/consumer/overview.html?child=%s&view=chat" % ellie), w, h,
                  "document.querySelectorAll('#dk-chatlist > div').length > 2")
            shoot(p, "05-termly-report-" + label,
                  qs("/consumer/report.html?child=%s&term=summer-2026" % ellie), w, h, READY_REPORT,
                  tall=True)

        # ── child surfaces ──
        # Opening the chat marks the thread read, so the SECOND pass would
        # otherwise lose the unread badge and the "Hannah wrote" card that the
        # Today screen is partly about. Put the last message back unread.
        unread_again(ids)
        with cdp.Browser() as b:
            p = b.attach()
            p.send("Page.addScriptToEvaluateOnNewDocument", {"source": FLAG_ON_JS})
            with_session(p, child_sess)
            shoot(p, "03-child-today-" + label,
                  qs("/consumer/today.html"), w, h, READY_TODAY)
            shoot(p, "06b-child-chat-" + label,
                  qs("/consumer/today.html"), w, h, READY_TODAY, after=open_child_chat)
            shoot(p, "04-exam-feedback-" + label,
                  qs("/consumer/exam.html?q=%s" % EXAM_Q), w, h, READY_EXAM)

    with open(os.path.join(SCRATCH, "mrb327_shot_text.json"), "w") as fh:
        json.dump(SHOT_TEXT, fh, indent=1)
    print("\n  rendered text of every shot saved for the tell-check")


# ══════════════════════════════════════════════════════════════════════════
# R — the summer term behind the termly report
# ══════════════════════════════════════════════════════════════════════════
# ⚠️ WHY THIS EXISTS. A termly report is a document about a TERM. The autumn
# term is six days old today, so a report drawn on it is a page of dashes —
# true, and useless as a picture of the product. So the fixture family joined
# in the summer term (their org and profiles are backdated to match) and the
# report shot is the SUMMER 2026 one: the completed term, the artefact a
# parent actually receives. The unit checks in it were sat for real through
# the real routes; the lessons behind them are seeded rows in exactly the
# shape `generateWeek` writes, because re-running the generator over sixteen
# past weeks would drag the child's scheme cursor forward and change the
# current week that every other shot is of.
def slugify(name):
    out = "".join(c.lower() if c.isalnum() else "-" for c in name)
    while "--" in out:
        out = out.replace("--", "-")
    return out.strip("-")


# (unit_code, subject, unit name, [lesson slugs], [lesson titles])
TERM_UNITS = [
    ("B6",  "Biology",   "Health and drugs",
     ["what-drugs-do-to-the-body", "alcohol-and-smoking", "substance-misuse-and-decisions"]),
    ("C7",  "Chemistry", "Energy changes in reactions",
     ["energy-and-changes-of-state", "exothermic-reactions", "endothermic-reactions",
      "measuring-a-temperature-change"]),
    ("P9",  "Physics",   "Static electricity",
     ["charging-by-rubbing", "forces-between-charges", "electric-fields"]),
    ("C9",  "Chemistry", "Metals and materials",
     ["the-reactivity-series", "predicting-displacement", "getting-metals-out-of-rocks",
      "ceramics-polymers-and-composites"]),
    ("B9",  "Biology",   "Ecosystems and interdependence",
     ["food-chains-and-food-webs", "predator-and-prey", "disturbing-a-food-web",
      "pollinators-and-food-security", "toxic-build-up-in-a-food-chain", "sampling-an-ecosystem"]),
    ("C10", "Chemistry", "The Earth and its atmosphere",
     ["inside-the-earth", "three-ways-to-make-a-rock", "the-rock-cycle"]),
]

# The two sessions she did not do. A term with nothing outstanding is not a
# term anybody recognises: one lesson skipped before a check she sat anyway,
# and the last one of the year, which the summer holidays ate.
TERM_SKIPPED = {"2026-06-27", "2026-07-21"}

# Two evenings a week — Tuesday and Saturday — which is what "steady,
# alongside school" means in daysFor(). Dates are real 2026 Tuesdays/Saturdays.
TERM_DAYS = [
    "2026-04-14", "2026-04-18", "2026-04-21",                                # B6
    "2026-04-28", "2026-05-02", "2026-05-05", "2026-05-09",                  # C7
    "2026-05-19", "2026-05-23", "2026-05-26",                                # P9
    "2026-06-02", "2026-06-06", "2026-06-09", "2026-06-13",                  # C9
    "2026-06-23", "2026-06-27", "2026-06-30",
    "2026-07-01", "2026-07-02", "2026-07-07",                                # B9 — the
    #   30 June / 1 July / 2 July run is the revision push before the check
    "2026-07-14", "2026-07-18", "2026-07-21",                                # C10
]

# One check per unit, on a Saturday after the unit's last lesson. Wrong answers
# out of ten, so the trend is 60 → 70 → 70 → 90: real progress, not a clean sweep.
TERM_CHECKS = [("B6", "2026-04-25", 4), ("C7", "2026-05-16", 3), ("P9", "2026-05-30", 3),
               ("C9", "2026-06-20", 2), ("B9", "2026-07-11", 1)]

TITLE_OF = {}


def phase_term(ids):
    print("\n── the summer term (for the report) ──────────────────────")
    ellie = ids["kids"]["Ellie"]
    ids.setdefault("attempts", [])

    # re-runnable
    sb_admin("DELETE", "/rest/v1/work_items?child_id=eq.%s&scheduled_for=lt.2026-08-01" % ellie["id"])
    st, old = sb_admin("GET", "/rest/v1/unit_check_attempts?select=id&child_id=eq." + ellie["id"])
    for r in (old or []):
        sb_admin("DELETE", "/rest/v1/unit_check_attempts?id=eq." + r["id"])
        if r["id"] in ids["attempts"]:
            ids["attempts"].remove(r["id"])

    # ── titles come from the child's OWN scheme, read through the product's
    #    own picker route, so a lesson is never named by this script ──
    pjwt = sign_in(PARENT_EMAIL, PARENT_PW)["access_token"]
    st, pick = api("GET", "/api/consumer/children/%s/picker" % ellie["id"], pjwt)
    check(st == 200, "picker read for lesson titles", st)
    for u in (pick or {}).get("units", []):
        for l in u["lessons"]:
            TITLE_OF[l["slug"]] = l["title"]

    flat = []
    for code, subject, name, slugs in TERM_UNITS:
        for i, slug in enumerate(slugs):
            flat.append((code, subject, name, slug, i + 1))
    assert len(flat) == len(TERM_DAYS), (len(flat), len(TERM_DAYS))

    rows = []
    for (code, subject, name, slug, n), day in zip(flat, TERM_DAYS):
        d = datetime.date.fromisoformat(day)
        title = TITLE_OF.get(slug) or slug.replace("-", " ").capitalize()
        done = day not in TERM_SKIPPED
        rows.append({
            "org_id": ids["org"], "child_id": ellie["id"],
            "week_start": (d - datetime.timedelta(days=d.weekday())).isoformat(),
            "scheduled_for": day, "position": 1, "kind": "lesson",
            "title": "%s: lesson %d" % (name, n), "sub": title, "minutes": 20,
            "ref": {"href": "/ks3/%s/%s/%s.html" % (subject.lower(), slugify(name), slug),
                    "topic": name, "subject": subject, "unit_code": code, "lesson_slug": slug},
            "set_by": "mrbadmus",
            "status": "done" if done else "set",
            "done_at": iso(datetime.datetime(d.year, d.month, d.day, 18, 5)) if done else None,
            "created_at": iso(datetime.datetime(d.year, d.month, d.day, 7, 0)),
        })
    st, r = sb_admin("POST", "/rest/v1/work_items", rows)
    check(st < 300, "summer-term work items written", (st, str(r)[:200]))
    print("  %d lessons across %s → %s, %d done"
          % (len(rows), TERM_DAYS[0], TERM_DAYS[-1], sum(1 for x in rows if x["status"] == "done")))

    cs = child_session(ellie["id"], CHILD_PW)
    for unit, day, wrong in TERM_CHECKS:
        d = datetime.date.fromisoformat(day)
        a = sit_check(ellie["id"], cs["access_token"], unit, wrong,
                      datetime.datetime(d.year, d.month, d.day, 11, 5))
        if a:
            ids["attempts"].append(a)
    json.dump(ids, open(STATE_FILE, "w"), indent=1)


# ══════════════════════════════════════════════════════════════════════════
def main():
    global BASE, API
    ap = argparse.ArgumentParser()
    ap.add_argument("--site", default=os.path.join(ROOT, "mrbadmus_site"))
    ap.add_argument("--api", default="http://localhost:3191")
    ap.add_argument("--port", type=int, default=8191)
    ap.add_argument("--phases", default="SMRP")
    ap.add_argument("--keep", action="store_true")
    ap.add_argument("--reuse", action="store_true")
    ap.add_argument("--teardown-only", action="store_true")
    a = ap.parse_args()
    API = a.api
    os.makedirs(SHOTS, exist_ok=True)

    if a.teardown_only:
        import mrb327_marketing_teardown as td
        td.run(json.load(open(STATE_FILE)))
        return 0

    server, port = cdp.serve(os.path.abspath(a.site), a.port)
    BASE = "http://localhost:%d" % port
    print("serving built tree at", BASE, "· backend", API)
    print("today", TODAY, TODAY.strftime("%A"), "· week Monday", MONDAY)

    ids = None
    try:
        if a.reuse:
            ids = json.load(open(STATE_FILE))
            sess = sign_in(PARENT_EMAIL, PARENT_PW)
            pjwt = sess["access_token"]
        if "S" in a.phases:
            ids, pjwt = seed()
            shape_week(ids, pjwt)
            cs = seed_chat(ids, pjwt)
            seed_exam(ids, cs)
        if "W" in a.phases:
            phase_work(ids, pjwt)
        if "U" in a.phases:
            phase_checks(ids)
        if "R" in a.phases:
            phase_term(ids)
        if "M" in a.phases:
            phase_mark(ids)
        if "P" in a.phases:
            phase_shoot(ids)
    finally:
        json.dump(ids, open(STATE_FILE, "w"), indent=1) if ids else None
        server.shutdown()

    print("\n%d failure(s)" % len(FAILS))
    for f in FAILS:
        print("  - " + f)
    return min(len(FAILS), 99)


if __name__ == "__main__":
    sys.exit(main())
