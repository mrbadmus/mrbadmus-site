"""consumer_dash_fixture.py — an OFFLINE signed-in parent, for the family
dashboard (consumer/overview.html) and the account page (consumer/account.html).

B2C repair, 3 Oct 2026. Until this file existed no gate had ever loaded a
signed-in consumer page: contrast_audit.py listed consumer/signup.html and
consumer/today.html, and both rendered "Not found" on 127.0.0.1 (config.js's
TEST block has CONSUMER_SIGNUP_ENABLED false) or bounced for want of a
session. So the dashboard's dark sidebar shipped with its wordmark at 1.08:1
and nothing measured it.

`prescript(...)` returns JavaScript for `Page.addScriptToEvaluateOnNewDocument`
— it runs before the page's own scripts on every navigation and:

  * traps `window.MrBadmusConfig` as config.js assigns it, switching the
    consumer flag ON and pointing BACKEND_URL at a host that cannot resolve
    (so a request the stub does not answer fails loudly, never reaches TEST
    or production);
  * pre-installs `window.supabase` — consumer-common.js's `loadSdk()` sees it
    and never fetches the CDN — whose client hands back a parent session;
  * replaces `fetch` for `/api/consumer/*` with canned answers from the
    `family` payload built below, honouring AbortSignal exactly as fetch does
    (so a "hang" checkout times out through the page's own AbortController).

Import-only: no top-level work beyond building constants.
"""
from __future__ import annotations

import json

KIDS = [
    {
        "id": "kid-ada", "first_name": "Ada", "year_group": 8, "mode": "alongside_school",
        "username": "ada.comet", "status": "active", "intensity": "steady",
        "streak": 4, "unread": 1, "humanLeft": 2, "paused": False,
        "lastActive": "2026-10-02T18:40:00Z",
        "days": [1, 0, 1, 0, 0, 0, 0],
        # B2C unit 7 (ruling 3): the Monday-first strip the pages now read.
        "week_strip": {"from": "2026-09-28", "today": 2,
                       "dates": ["2026-09-28", "2026-09-29", "2026-09-30", "2026-10-01",
                                 "2026-10-02", "2026-10-03", "2026-10-04"],
                       "done": [1, 0, 1, 0, 0, 0, 0]},
        "work": [
            {"id": "w1", "title": "Cells and organisation", "done": True, "day": "Mon",
             "mins": 20, "source": "Mr Badmus"},
            {"id": "w2", "title": "Quick questions: cells", "done": False, "day": "Wed",
             "mins": 10, "source": "Mr Badmus"},
            # B2C unit 7 (ruling 1): a row still to open reads "Opens Fri".
            {"id": "w3", "title": "Diffusion", "done": False, "day": "Fri", "mins": 20,
             "source": "You", "byParent": True, "scheduled_for": "2030-10-11"},
        ],
        # B2C week repair (4 Oct 2026): work set for a LATER week — the backend
        # sends it as `upcoming`, its day carrying the date.
        "upcoming": [
            {"id": "w4", "title": "Photosynthesis: lesson 3", "done": False, "day": "Mon 12 Oct",
             "mins": 20, "source": "Set by You", "byParent": True, "week_start": "2026-10-12"},
        ],
        "scores": [{"pct": 58, "label": "Cells"}, {"pct": 71, "label": "Particles"}],
        "weak": "Calculating magnification",
        # ⊕ B2C polish (9 Oct 2026): Ada's topic answer was given ("chosen"),
        # with GET /family's real `position` shape — the unit names the
        # pages show (labels), and the scheme weeks they must never show.
        "position": {"cursors": {"Biology": 12, "Chemistry": 5, "Physics": 5},
                     "labels": {"Biology": "Breathing and gas exchange: lesson 1",
                                "Chemistry": "Chemical reactions: lesson 2",
                                "Physics": "Electric circuits: lesson 1"},
                     "chosen": True},
    },
    {
        "id": "kid-ben", "first_name": "Ben", "year_group": 10, "mode": "home_education",
        "exam_board": "AQA", "pathway": "combined", "tier": "higher",
        "username": "ben.saturn", "status": "never", "intensity": "light",
        "streak": 0, "unread": 0, "humanLeft": 2, "paused": False,
        "lastActive": None, "days": [0, 0, 0, 0, 0, 0, 0], "work": [], "scores": [],
        "position": {"cursors": {}},
    },
]

# B2C onboarding repair (3 Oct 2026): the child's scheme as GET
# /children/:id/picker really sends it — units with their lessons and the
# scheme's subject name — so the shared topic picker can be measured and
# driven offline. Names and slugs are the real curriculum's (the picker
# matches them against consumer/curriculum-index.json).
PICKERS = {
    "kid-ada": [
        {"unit_code": "B4", "subject": "Biology", "name": "Breathing and gas exchange",
         "lessons": [{"slug": "the-gas-exchange-system", "title": "The gas exchange system", "week": 1},
                     {"slug": "how-breathing-works", "title": "How breathing works", "week": 2}]},
        {"unit_code": "C4", "subject": "Chemistry", "name": "Chemical reactions",
         "lessons": [{"slug": "chemical-vs-physical-change", "title": "Chemical vs physical change", "week": 1}]},
        {"unit_code": "P8", "subject": "Physics", "name": "Electric circuits",
         "lessons": [{"slug": "current-and-circuits", "title": "Current and circuits", "week": 1}]},
    ],
    "kid-ben": [
        {"unit_code": None, "subject": "Biology", "name": "Cell Biology",
         "lessons": [{"slug": "eukaryotes-prokaryotes", "title": "Eukaryotes prokaryotes", "week": 1},
                     {"slug": "animal-plant-cells", "title": "Animal plant cells", "week": 2}]},
        {"unit_code": None, "subject": "Chemistry", "name": "Bonding, Structure and Properties of Matter",
         "lessons": [{"slug": "chemical-bonds", "title": "Chemical bonds", "week": 9}]},
    ],
}

PRICING = {"tiers": {"month": {"first": 999, "rest": 599},
                     "year": {"first": 9990, "rest": 5990}},
           "trial_days": 7}


def billing(state, kids):
    """The `billing` block /api/consumer/family sends, per state."""
    access = {"trialing": "full", "active": "full", "none": "none",
              "locked": "locked", "past_due": "read_only"}.get(state, "full")
    seats = [{"name": k["first_name"], "year": k["year_group"],
              "price_pence": 999 if i == 0 else 599} for i, k in enumerate(kids)]
    total_m = sum(s["price_pence"] for s in seats)
    return {
        "state": state, "access": access, "interval": "month",
        "trial_end": "2026-10-09T12:00:00Z" if state == "trialing" else None,
        "days_left": 6 if state == "trialing" else None,
        "next_payment_at": "2026-11-02T12:00:00Z" if state == "active" else None,
        "access_end": "2026-09-30T12:00:00Z" if state == "locked" else None,
        "retry_at": None, "failed_at": None,
        "seats": seats, "monthly_total_pence": total_m,
        "annual_total_pence": total_m * 10,
        "can_checkout": state in ("none", "locked"),
        "can_portal": state not in ("none",),
    }


def family(state="trialing", kids=2, deletion=None):
    k = KIDS[:kids]
    return {
        "family": {"id": "fam-1", "name": "The Fixture family"},
        "subscription": None if state == "none" else {"current_period_end": "2026-11-02T12:00:00Z"},
        "parent": {"name": "Sam", "email": "sam@example.test"},
        "billing": billing(state, k),
        "children": k,
        "prefs": {"digest": True, "marking_email": True},
        "deletion": deletion,
    }


# ⊕ B2C unit 6 (5 Oct 2026) — THE CHILD AND THE ORGANISATION, OFFLINE.
# contrast_audit.py measured consumer/today.html and org/index.html with the
# consumer flag OFF ("Not found") and with nobody signed in, so the child's
# whole product and the organisation dashboard had never been measured. These
# payloads are the SHAPES the TEST backend answered on 5 Oct 2026 for a real
# throwaway family (GET /api/consumer/child/today, /child/exam-questions,
# /children/:id/report), with the fixture's own names, and the org dashboard
# assembled from KIDS the way GET /api/consumer/org assembles its pupils.
CHILD_TODAY = {
    "ok": True,
    "child": {"name": "Ada", "streak": 3, "best": "8/10", "bestUnit": "Cells"},
    "parent": {"id": "parent-1", "name": "Sam", "initial": "S"},
    "access": "full",
    "items": [
        {"id": "i1", "title": "Reproduction: lesson 1", "sub": "Human reproductive systems",
         "mins": "20", "done": True, "by": "mb", "byName": None,
         "href": "/ks3/biology/reproduction/human-reproductive-systems.html", "kind": "lesson",
         "scheduled_for": "2026-10-05", "day": "Mon", "tag": "Mr Badmus", "next_week": False},
        {"id": "i2", "title": "Practice: Reproduction", "sub": "10 questions", "mins": "10",
         "done": False, "by": "mb", "byName": None, "href": "/student/assignment.html?id=a1",
         "kind": "practice", "scheduled_for": "2026-10-05", "day": "Mon", "tag": "Mr Badmus",
         "next_week": False},
        {"id": "i3", "title": "Diffusion", "sub": "Lesson", "mins": "20", "done": False,
         "by": "parent", "byName": "Sam", "href": "/ks3/biology/cells/diffusion.html",
         "kind": "lesson", "scheduled_for": "2026-10-05", "day": "Mon", "tag": "Sam",
         "next_week": False},
    ],
    "later": [
        {"id": "l1", "title": "Unit check: Reproduction", "sub": "10 questions", "mins": "15",
         "done": False, "by": "mb", "byName": None, "href": "/consumer/unit-check.html?unit=B5",
         "kind": "unit_check", "scheduled_for": "2026-10-08", "day": "Thu", "tag": "Mr Badmus",
         "next_week": False},
    ],
    "messages": [
        {"who": "them", "text": "Well done on the cells check!", "created_at": "2026-10-04T17:10:00Z"},
        {"who": "you", "text": "Thanks! Diffusion next.", "created_at": "2026-10-04T17:12:00Z"},
    ],
    "unread": 1,
    "flashcards": [],
    "notifications": [
        {"title": "Marked", "body": "Your answer on cells came back: 3 out of 4.",
         "ref": {"href": "/consumer/exam.html"}},
    ],
}

CHILD_EXAM = {
    "ok": True, "access": "full", "quotaLeft": 1, "quotaTotal": 2, "resetDate": "1 November",
    "provider": "stub",
    "questions": [
        {"id": "q-cells-explain", "topic": "Cells and organisation", "subject": "Biology",
         "marks": 4, "command": "Explain",
         "text": "Down a school microscope you can see a leaf cell’s wall and nucleus but "
                 "not its mitochondria. Explain why not.",
         "stem": None, "scheme": ["Says they are still there.", "Says they are too small to resolve."],
         "done": True, "answer": "They are too small for the microscope to show.",
         "aiScore": 3, "feedback": "Good — now say what limits the microscope.",
         "practice": None, "human": None, "waiting": False, "answer_id": "ans-1"},
        {"id": "q-particles-describe", "topic": "Particles", "subject": "Chemistry",
         "marks": 3, "command": "Describe",
         "text": "Describe how the particles in a solid are arranged.",
         "stem": None, "scheme": ["Close together.", "Regular pattern.", "Vibrate in place."],
         "done": False},
    ],
}

PARENT_REPORT = {
    "ok": True,
    "report": {
        "child": {"name": "Ada", "surname": "", "year": 8, "ks": 3, "mode": "school",
                  "dates": "1 September – 19 December 2026"},
        "term": "Autumn 2026", "term_key": "autumn-2026", "produced": "5 October 2026",
        "ref": "A-Y8-AUT26", "sessions": {"done": 5, "set": 8}, "minutes": 35,
        "streakBest": 4, "checksAvg": 72, "checksCount": 1,
        "units": [{"code": "B5", "name": "Reproduction", "subject": "Biology", "lessons": "3/8",
                   "check": "72%", "status": "In progress",
                   "nc": "National curriculum: Reproduction (KS3.B.REP.01, KS3.B.REP.02)"}],
        "summary": "Ada completed 5 of the 8 sessions set this term.",
        "progressNote": "One unit check so far, at 72%.",
        "strengths": ["Cell structure"], "nextSteps": ["Calculating magnification"],
        "answers": [{"q": "Explain why mitochondria do not show.", "mark": "3/4", "date": "4 Oct"}],
        "teacherNote": "",
    },
}


def org_payload():
    """GET /api/consumer/org's shape, pupils built from KIDS."""
    pupils = []
    for i, k in enumerate(KIDS):
        pupils.append({
            "id": k["id"], "name": k["first_name"], "initial": k["first_name"][0],
            "username": k["username"], "year": k["year_group"],
            "group": "Tuesday group" if i == 0 else None, "group_id": "g1" if i == 0 else None,
            "mode": k["mode"], "intensity": k["intensity"], "paused": False,
            "days": k["days"], "last": None, "streak": k["streak"],
            "lastActive": k["lastActive"], "active": i == 0, "flag": None,
            "scores": k["scores"], "weak": k.get("weak"), "humanUsed": 0,
            "humanLeft": k["humanLeft"], "unread": k["unread"], "work": k["work"],
            "position": k["position"], "status": k["status"],
        })
    return {
        "ok": True,
        "org": {"id": "org-1", "name": "Northside Learning Centre", "kind": "organisation",
                "seat_cap": 20, "seats_used": len(pupils), "period_end": "2027-07-31T00:00:00Z",
                "contact_name": "Pat Lee", "contact_email": "pat@example.test",
                "access": "full", "state": "active"},
        "staff": {"id": "staff-1", "name": "Pat Lee"},
        "staff_list": [{"id": "staff-1", "name": "Pat Lee", "role": "Admin",
                        "groups": "All groups", "pending": False},
                       {"id": "pend-1", "name": "Jo Ray", "role": "Caseworker", "groups": "",
                        "pending": True}],
        "groups": [{"id": "g1", "name": "Tuesday group", "year": 8, "unit": "Cells",
                    "intensity": "steady", "count": 1, "done": "1/3"}],
        "pupils": pupils,
    }


_JS = r"""
(function () {
  var F = __FIXTURE__;
  window.__CF__ = F;
  F.calls = [];

  /* 1. The flag, on — whatever config.js decides for 127.0.0.1. */
  var cfg = null;
  Object.defineProperty(window, 'MrBadmusConfig', {
    configurable: true,
    get: function () { return cfg; },
    set: function (v) {
      if (v && typeof v === 'object') {
        v.CONSUMER_SIGNUP_ENABLED = true;
        v.BACKEND_URL = 'https://consumer-fixture.invalid';
      }
      cfg = v;
    }
  });

  /* 1b. The signup draft (B2C onboarding repair): every load starts from
     exactly the draft the fixture names, or none — the page target is
     reused across specs and localStorage would otherwise leak between
     them. A drive that wants the page's OWN writes to survive a reload
     sets sessionStorage `__cf_keep`. */
  try {
    if (!sessionStorage.getItem('__cf_keep')) {
      if (F.draft) { localStorage.setItem('mrb.consumer.signup', JSON.stringify(F.draft)); }
      else { localStorage.removeItem('mrb.consumer.signup'); }
    }
  } catch (e) {}

  /* 2. A Supabase client that is already signed in as a parent. */
  var session = { access_token: 'fixture-token', refresh_token: 'r', token_type: 'bearer',
                  expires_at: Math.floor(Date.now() / 1000) + 3600,
                  user: { id: 'parent-1', email: F.family.parent.email,
                          email_confirmed_at: F.unconfirmed ? null : '2026-09-01T00:00:00Z' } };
  /* ⊕ B2C unit 6 — `who`: a CHILD's session carries the internal address
     the backend mints (its suffix is read from config.js when the page asks,
     so this file never spells it); org STAFF are an organisation's teacher. */
  if (F.who === 'child') {
    session.user.id = 'kid-ada';
    Object.defineProperty(session.user, 'email', { enumerable: true, get: function () {
      var c = window.MrBadmusConfig || {};
      return 'kid-ada' + (c.CHILD_EMAIL_SUFFIX || '@child.invalid');
    } });
  } else if (F.who === 'org') {
    session.user.id = 'staff-1';
    session.user.email = 'pat@example.test';
  }
  var ch = { on: function () { return ch; }, subscribe: function () { return ch; } };
  var ok = function (v) { return Promise.resolve(v); };
  window.supabase = { createClient: function () { return {
    auth: {
      getSession: function () { return ok({ data: { session: F.signedIn === false ? null : session } }); },
      signUp: function (a) {
        F.calls.push({ method: 'AUTH', path: 'signUp', body: a });
        return ok({ data: { user: { identities: F.existing ? [] : [{}] }, session: null }, error: null });
      },
      signInWithPassword: function (a) {
        F.calls.push({ method: 'AUTH', path: 'signInWithPassword', body: { email: a && a.email } });
        if (F.passwordOk) { F.signedIn = true; return ok({ data: { session: session }, error: null }); }
        return ok({ data: {}, error: { message: 'Email not confirmed' } });
      },
      resend: function () { return ok({}); },
      getUser: function () { return ok({ data: { user: session.user } }); },
      onAuthStateChange: function () { return { data: { subscription: { unsubscribe: function () {} } } }; },
      resetPasswordForEmail: function () { return ok({}); },
      updateUser: function () { return ok({ data: {} }); },
      signOut: function () { return ok({}); }
    },
    channel: function () { return ch; },
    removeChannel: function () {},
    rpc: function (name) { return ok({ data: F.who === 'operator' && name === 'auth_user_is_platform_operator' }); },
    /* A profile read under the session (auth.html's interstitial, /go's
       "signed in as"), answered from the fixture. */
    from: function () {
      var q = { select: function () { return q; }, eq: function () { return q; },
                single: function () { return ok({ data: { first_name: 'Ada', username: 'ada.comet', role: 'student' } }); },
                maybeSingle: function () { return ok({ data: { first_name: 'Ada', username: 'ada.comet' } }); } };
      return q;
    }
  }; } };

  /* 3. fetch, for /api/consumer/* only. */
  var realFetch = window.fetch.bind(window);
  function reply(status, body) {
    return Promise.resolve(new Response(body == null ? '' : JSON.stringify(body),
      { status: status, headers: { 'Content-Type': 'application/json' } }));
  }
  function hang(init) {
    return new Promise(function (_, reject) {
      var s = init && init.signal;
      if (!s) { return; }
      var die = function () { reject(new DOMException('The operation was aborted.', 'AbortError')); };
      if (s.aborted) { return die(); }
      s.addEventListener('abort', die);
    });
  }
  window.fetch = function (url, init) {
    var u = String(url);
    var i = u.indexOf('/api/consumer/');
    if (i < 0) { return realFetch(url, init); }
    var path = u.slice(i).split('?')[0];
    var method = ((init && init.method) || 'GET').toUpperCase();
    var body = null;
    try { body = init && init.body ? JSON.parse(init.body) : null; } catch (e) { body = null; }
    F.calls.push({ method: method, path: path, body: body });

    var fails = F.fail || [];
    for (var fi = 0; fi < fails.length; fi++) {
      if (new RegExp(fails[fi]).test(path)) {
        return reply(500, { error: 'fixture_fail', message: 'The fixture refused this on purpose.' });
      }
    }

    if (path === '/api/consumer/family' && method === 'GET') { return reply(200, F.family); }
    // ⊕ B2C unit 6 — the child's pages, the parent's report, the org dashboard.
    if (path === '/api/consumer/child/today') { return reply(200, F.childToday); }
    if (path === '/api/consumer/child/session') { return reply(200, { ok: true, first_name: 'Ada' }); }
    if (path === '/api/consumer/child/unit-checks') { return reply(200, { ok: true, attempts: [] }); }
    if (path === '/api/consumer/child/unit-check') {
      return reply(200, { ok: true, unit: { code: 'B5', name: 'Reproduction', subject: 'Biology', year: 8,
        count: 10, minutes: 15, lessons: 8 }, previous: null, access: 'full', org_id: 'fam-1' });
    }
    if (path === '/api/consumer/child/exam-questions') { return reply(200, F.childExam); }
    if (/\/children\/[^/]+\/report$/.test(path)) { return reply(200, F.report); }
    if (path === '/api/consumer/org' && method === 'GET') { return reply(200, F.org); }
    if (path === '/api/consumer/admin/accounts') {
      return reply(200, { ok: true,
        stats: { families: 3, in_trial: 1, children: 4, organisations: 1, pupils: 2,
                 family_mrr_pence: 1198, past_due: 1 },
        accounts: [
          { id: 'fam-1', name: 'The Fixture family', email: 'sam@example.test', kids_label: '2 children',
            billing: 'trialing', mrr_label: '—', since: '2 Oct', last_active: 'Today' },
          { id: 'fam-2', name: 'The Okafor family', email: 'ifeoma@example.test', kids_label: '1 child',
            billing: 'past_due', mrr_label: '£9.99', since: '14 Sep', last_active: '3 days ago' }] });
    }
    if (path === '/api/consumer/admin/health') {
      return reply(200, { ok: true, checked_at: '2026-10-05T08:00:00Z', figures: [] });
    }
    if (path === '/api/consumer/admin/mb-queue') { return reply(200, { ok: true, pending: [] }); }
    if (path === '/api/consumer/pricing') { return reply(200, F.pricing); }
    if (path === '/api/consumer/chat/threads') { return reply(200, { threads: [] }); }
    if (path === '/api/consumer/chat/messages') { return reply(200, { messages: F.messages || [] }); }
    if (path === '/api/consumer/chat/read') { return reply(200, { ok: true }); }
    if (/\/picker$/.test(path)) {
      var pk = Object.keys(F.pickers || {}).filter(function (id) { return path.indexOf(id) >= 0; })[0];
      return reply(200, { units: (F.pickers || {})[pk] || [] });
    }
    if (path === '/api/consumer/family/ensure') { return reply(200, { ok: true, terms_accepted_at: '2026-10-03T00:00:00Z' }); }
    if (path === '/api/consumer/username/check') {
      var u = (String(url).split('u=')[1] || '').split('&')[0];
      if ((F.taken || []).indexOf(u) >= 0) {
        return reply(200, { ok: false, reason: 'That username is taken — try another.', suggestions: [u + '7', u + 'x'] });
      }
      return reply(200, { ok: true, reason: null, suggestions: [] });
    }
    if (path === '/api/consumer/children' && method === 'POST') {
      if ((F.taken || []).indexOf(body && body.username) >= 0) {
        return reply(409, { error: 'username_unavailable', message: 'That username is taken — try another.',
                            suggestions: [body.username + '7', body.username + 'x'] });
      }
      var nid = 'kid-new' + F.family.children.length;
      F.family.children.push({ id: nid, first_name: body.first_name, year_group: body.year_group,
        username: body.username, mode: body.mode, tier: body.tier, pathway: body.pathway,
        exam_board: body.exam_board, position: { cursors: {} } });
      F.pickers[nid] = F.pickers[body.year_group >= 10 ? 'kid-ben' : 'kid-ada'];
      return reply(200, { ok: true, child_id: nid });
    }
    if (/\/answers$/.test(path)) { return reply(200, { answers: [] }); }
    if (path === '/api/consumer/checkout') {
      var mode = F.checkout || 'ok';
      if (mode === 'hang') { return hang(init); }
      if (mode === '500') { return reply(500, { error: 'stripe_down', message: 'Stripe is unavailable.' }); }
      if (mode === 'no_children') {
        return reply(409, { error: 'no_children', message: 'Add a child before starting a subscription.' });
      }
      if (mode === 'no_url') { return reply(200, {}); }
      return reply(200, { url: location.origin + '/404.html#stripe-checkout' });
    }
    if (path === '/api/consumer/portal') { return reply(200, { url: location.origin + '/404.html#stripe-portal' }); }
    if (path === '/api/consumer/family/delete-request') {
      if (method === 'POST') {
        if (!body || body.confirm !== 'DELETE') {
          return reply(400, { error: 'confirm_required', message: 'Type DELETE to confirm.' });
        }
        F.family.deletion = { execute_after: '2026-11-02T12:00:00Z' };
        return reply(200, { ok: true, execute_after: F.family.deletion.execute_after });
      }
      if (method === 'DELETE') { F.family.deletion = null; return reply(200, { ok: true }); }
    }
    if (/\/password$/.test(path)) { return reply(200, { password: 'comet-saturn-42' }); }
    if (/\/pause$/.test(path)) {
      var kid = F.family.children.filter(function (k) { return path.indexOf(k.id) >= 0; })[0];
      if (kid) { kid.paused = !!(body && body.paused); }
      return reply(200, { ok: true });
    }
    if (/\/children\/[^/]+\/work$/.test(path) || path === '/api/consumer/chat/send') {
      if (F.family.billing.access !== 'full') {
        return reply(423, { error: 'org_locked', message: 'This account is not started.' });
      }
      return reply(200, { ok: true });
    }
    return reply(200, { ok: true });
  };
})();
"""


def prescript(state="trialing", kids=2, checkout="ok", deletion=None, messages=None,
              fail=None, signed_in=True, draft=None, taken=None, existing=False,
              password_ok=False, unconfirmed=False, who="parent"):
    """`fail`: regexes over the request path that answer 500 — for proving a
    page's failure line, not for anything a gate measures.

    B2C onboarding repair: `signed_in=False` is a visitor with no session
    (the signup account / verify steps); `draft` seeds the signup draft in
    localStorage on every load; `taken` lists usernames the checker and the
    create route refuse, with two suggestions each; `existing` makes
    signUp answer as Supabase does for an address that already has an
    account (empty identities); `password_ok` makes signInWithPassword sign
    the parent in (otherwise it answers "Email not confirmed"); `unconfirmed`
    signs in a parent whose email is not verified yet.

    ⊕ B2C unit 6: `who` is "parent" (default), "child" (a family child's
    session — the child pages and Today), "org" (organisation staff) or
    "operator" (the platform operator's admin pages). `signed_in=False`
    with any `who` is a visitor on a public page, flag on."""
    fx = {"family": family(state, kids, deletion), "pricing": PRICING,
          "checkout": checkout, "messages": messages or [], "fail": fail or [],
          "pickers": json.loads(json.dumps(PICKERS)), "signedIn": signed_in,
          "draft": draft, "taken": taken or [], "existing": existing,
          "passwordOk": password_ok, "unconfirmed": unconfirmed, "who": who,
          "childToday": CHILD_TODAY, "childExam": CHILD_EXAM, "report": PARENT_REPORT,
          "org": org_payload()}
    return _JS.replace("__FIXTURE__", json.dumps(fx))
