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
        "work": [
            {"id": "w1", "title": "Cells and organisation", "done": True, "day": "Mon",
             "mins": 20, "source": "Mr Badmus"},
            {"id": "w2", "title": "Quick questions: cells", "done": False, "day": "Wed",
             "mins": 10, "source": "Mr Badmus"},
            {"id": "w3", "title": "Diffusion", "done": False, "day": "Fri", "mins": 20,
             "source": "You", "byParent": True},
        ],
        "scores": [{"pct": 58, "label": "Cells"}, {"pct": 71, "label": "Particles"}],
        "weak": "Calculating magnification",
        "position": {"cursors": {}},
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
    rpc: function () { return ok({ data: false }); }
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
              password_ok=False, unconfirmed=False):
    """`fail`: regexes over the request path that answer 500 — for proving a
    page's failure line, not for anything a gate measures.

    B2C onboarding repair: `signed_in=False` is a visitor with no session
    (the signup account / verify steps); `draft` seeds the signup draft in
    localStorage on every load; `taken` lists usernames the checker and the
    create route refuse, with two suggestions each; `existing` makes
    signUp answer as Supabase does for an address that already has an
    account (empty identities); `password_ok` makes signInWithPassword sign
    the parent in (otherwise it answers "Email not confirmed"); `unconfirmed`
    signs in a parent whose email is not verified yet."""
    fx = {"family": family(state, kids, deletion), "pricing": PRICING,
          "checkout": checkout, "messages": messages or [], "fail": fail or [],
          "pickers": json.loads(json.dumps(PICKERS)), "signedIn": signed_in,
          "draft": draft, "taken": taken or [], "existing": existing,
          "passwordOk": password_ok, "unconfirmed": unconfirmed}
    return _JS.replace("__FIXTURE__", json.dumps(fx))
