/* ───────────────────────────────────────────────────────────────────────
   shared/account.js — THE ONE MAP: who is this, and where do they go
   (front door run, Part 1, 12 Oct 2026)

   ── Why this file exists ────────────────────────────────────────────────
   On 9 Oct 2026 a parent signed in, opened mrbadmus.com, and saw "Dad" in the
   top bar. Clicking it went to /teacher-profile.html, whose guard bounced
   them to /index.html. There was no sign-out and no way to the parent
   dashboard. The chain was five places each deciding, on their own and from
   different facts, where a person goes: nav.js routed the chip by
   `role !== 'student'`, teacher-guard.js and student-guard.js bounced a wrong
   role to /index.html, auth.html's redirectAfterAuth had a parent branch
   bolted on the day before, class-entry.js had its own role test, and
   profile-setup.html had a staff branch and nothing for anybody else.

   Every one of them now asks THIS file. A route is decided here, once.

   ── The kinds ───────────────────────────────────────────────────────────
     pupil      a school pupil (role student)
     staff      school staff (role teacher / hod / admin) at a school
     parent     a family parent (role parent)
     child      a family OR organisation child (the @children.mrbadmus.internal
                address — MrBadmusConfig.isChildSession, the one test)
     org_staff  staff whose school is an organisation (schools.kind)
     operator   the platform operator: staff with NO school who the
                `auth_user_is_platform_operator()` RPC confirms

   ── Precedence — the order is the rule ──────────────────────────────────
     1. child session (email suffix)                       → child
     2. role parent                                        → parent
     3. staff role, schools.kind = 'organisation'          → org_staff
     4. staff role, a school of any other kind             → staff
        (EVEN IF the person is also an operator: Mide teaches. A teacher who
        can also operate lands on their classes, and reaches the operator
        console from the link that already exists for it.)
     5. staff role, NO school                              → the operator RPC:
        true → operator, otherwise staff
     6. role student, or no profile row yet (a new sign-up) → pupil

   ⚠️ ANY READ FAILURE FALLS BACK TO THE ROLE-ONLY ANSWER — what the site did
   before this file existed — and never to a bounce. A schools read that
   fails is "a school"; an operator RPC that fails is "not an operator"; a
   profile read that fails is `kind: null, unknown: true`, and every caller
   treats null as "do nothing", not as "send them away".

   ── What lives here, and what does not ──────────────────────────────────
   Here: the pure map (classify / describe / afterAuthTarget), resolving a
   session to an account, signing out, and the audience check the guards use.
   NOT here: the pupil's class lookup. "Which class page is mine" is
   class-entry.js's question (MRB-259, year-scoped by MRB-267) and this file
   asks it through `MRBClassEntry.pupilEntry()` instead of re-asking the
   database. Nor any menu: the drawer that shows the account is nav.js.

   ── Load order ──────────────────────────────────────────────────────────
   After config.js, before class-entry.js. It reads window.MrBadmusConfig and
   the stored session at CALL time and imports nothing at load, so it is safe
   anywhere after config.js; callers reach it as `window.MrBadmusAccount` and
   treat its absence as "legacy behaviour" rather than throwing. It is a
   static <script> everywhere (never injected on demand): /shared/* is served
   `immutable`, and only a stamped URL is safe under that — see _headers.

   ── Re-stamped 17 Oct 2026 ─────────────────────────────────────────────
   This comment exists to change the file's stamp. The front-door fixes'
   first deploy left `account.js?v=85ddd06e` cached at a Cloudflare edge
   holding the PREVIOUS file, under the year-long `immutable` rule, so no
   later deploy could reach that URL. A new stamp is the only cure from here
   (no purge API); see project memory "immutable cache trap".

   ── Test isolation ──────────────────────────────────────────────────────
   Every URL here comes from window.MrBadmusConfig. No project or backend is
   named in this file; with no config it finds no session and does nothing.
   ─────────────────────────────────────────────────────────────────────── */
(function (root) {
  'use strict';

  var STAFF_ROLES = ['teacher', 'hod', 'admin'];

  /* ── The pure map ───────────────────────────────────────────────────────
     Everything from here to `afterAuthTarget` is a function of its arguments
     alone — no DOM, no network, no storage — which is what lets
     account_map_check run it under Node and pin the precedence. */

  var DOORS = {
    // Where a person SIGNS IN. Pupils, staff and the operator share the
    // school door; the family and organisation sides have their own. Nothing
    // on a school-facing page links to the family/organisation doors (Mide,
    // 12 Oct 2026) — they are only ever reached by signing out of that side.
    pupil: '/auth.html', staff: '/auth.html', operator: '/auth.html',
    parent: '/parents/sign-in.html',
    child: '/go/',
    org_staff: '/org/sign-in.html'
  };

  /* Where SIGN OUT lands (front door, 16 Oct 2026). It used to be the kind's
     own door above, which put a signed-out teacher on /auth.html, a parent on
     the family sign-in and a pupil's sign-out on a form — Mide: "when I sign
     out I should land on the front page, signed out". Everybody now lands on
     the front page, where the bar says Sign in. The ONE exception is a family
     or organisation child: /go/ is their only door and no school-facing page
     links to it, so the front page would strand them. Switch account is a
     different act and keeps DOORS.pupil (the one door every adult can use). */
  var SIGN_OUT_TO = { adult: '/', child: DOORS.child };

  var HOMES = {
    // pupil's real home is their class page — see describe(), which takes it
    // from class-entry. This is the picker, used until/unless that is known.
    pupil:     { href: '/student/classes.html',        label: 'My classes',   title: 'Your classes' },
    staff:     { href: '/teacher/today.html',          label: 'My classes',   title: 'Your classes' },
    parent:    { href: '/consumer/overview.html',      label: 'My dashboard', title: 'Your family dashboard' },
    child:     { href: '/consumer/today.html',         label: 'Today',        title: 'Your Today page' },
    org_staff: { href: '/org/index.html',              label: 'My dashboard', title: 'Your organisation' },
    operator:  { href: '/consumer/admin-accounts.html', label: 'My dashboard', title: 'Operator console' }
  };

  var KIND_LABELS = {
    pupil: 'Pupil', staff: 'Teacher', parent: 'Parent',
    child: 'Pupil', org_staff: 'Organisation', operator: 'Operator'
  };

  // "My profile" — only where a page of that kind exists. A child, an
  // organisation and the operator have none, so the drawer shows no row.
  var PROFILES = {
    pupil: '/profile-setup.html',
    staff: '/teacher-profile.html',
    parent: '/consumer/account.html'
  };

  // Which kinds may stand on which surface. `consumer` lets everyone through
  // except a school pupil: operators (who may also hold a school) and
  // organisation staff use those pages, and a wrong guess there would lock
  // out the one person who administers the product.
  var AUDIENCES = {
    pupil:    ['pupil'],
    staff:    ['staff', 'operator'],
    parent:   ['parent'],
    child:    ['child'],
    consumer: ['parent', 'child', 'org_staff', 'operator', 'staff'],
    // The weekly challenge and the challenge history are a school pupil's (and
    // a teacher may look). A parent, a family child or organisation staff who
    // opens one by URL goes to their own home instead of an API error or the
    // GCSE wizard — front door Part 5.
    challenge: ['pupil', 'staff', 'operator'],
    // The /parents/ marketing pages and sign-in (front door, 16 Oct 2026). A
    // pupil or a family child who opens one by URL goes to their own home;
    // staff are let through for the same reason `consumer` lets them through
    // (the operator, and Mide, who also holds a family login).
    parents_public: ['parent', 'org_staff', 'operator', 'staff'],
    // /org/ is organisation staff and the operator.
    org: ['org_staff', 'operator']
  };

  function isStaffRole(role) { return STAFF_ROLES.indexOf(role) !== -1; }

  /* facts → kind. `facts` = { isChild, role, schoolId, schoolKind, isOperator }.
     schoolKind / isOperator may be null or undefined meaning "could not be
     read"; see the fallbacks in the header. Returns null only for a role this
     file has never heard of — a caller does nothing with null. */
  function classify(facts) {
    var f = facts || {};
    if (f.isChild) return 'child';
    if (f.role === 'parent') return 'parent';
    if (isStaffRole(f.role)) {
      if (f.schoolKind === 'organisation') return 'org_staff';
      if (f.schoolId) return 'staff';                   // any other / unknown kind
      return f.isOperator === true ? 'operator' : 'staff';
    }
    if (f.role === 'student' || !f.role) return 'pupil';
    return null;
  }

  /* kind → everything the UI needs to know about it. `ctx.classEntry` is
     class-entry's { href, label, title } for a pupil who has exactly one
     class (or several); without it a pupil's home is the picker. */
  function describe(kind, ctx) {
    ctx = ctx || {};
    if (!kind || !HOMES[kind]) {
      return { kind: null, kindLabel: null, home: null, homeLabel: null,
               homeTitle: null, door: DOORS.pupil, profileUrl: null };
    }
    var h = HOMES[kind];
    if (kind === 'pupil' && ctx.classEntry && ctx.classEntry.href) h = ctx.classEntry;
    if (kind === 'child' && ctx.childHome) h = { href: ctx.childHome, label: h.label, title: h.title };
    return {
      kind: kind,
      kindLabel: KIND_LABELS[kind],
      home: h.href,
      homeLabel: h.label,
      homeTitle: h.title || h.label,
      door: DOORS[kind],
      profileUrl: PROFILES[kind] || null
    };
  }

  /* Staff are greeted by the name pupils see (display_name), as Today
     already does; everyone else by first_name. */
  function nameFor(kind, p) {
    p = p || {};
    var s = (kind === 'staff' || kind === 'org_staff' || kind === 'operator')
      ? (p.display_name || p.displayName || p.first_name || p.firstName)
      : (p.first_name || p.firstName);
    s = s == null ? '' : String(s).trim();
    return s || null;
  }

  /* After a successful sign-in: where to. `acct` is a resolved account (or
     null/unknown); `returnUrl` is ?return= or '/index.html' when absent.
     This is auth.html's redirectAfterAuth with the decisions lifted out:

       child      → their Today page, whatever ?return= says
       parent     → the family dashboard (overview forwards an unfinished
                    signup to signup.html at the step it left — 9 Oct fix)
       org_staff  → /org/index.html
       staff / operator → ?return= if the visitor came for a page, else their home
       pupil      → GCSE with no pathway or no tier, or a brand-new account
                    with no profile row: /profile-setup.html (never a KS3
                    pupil — the MRB-101 loop); else ?return= if the visitor
                    came for a page; else their class page if they have one;
                    else ?return= (/index.html)
       unknown    → ?return= (a read that failed is not a reason to trap
                    someone in a wizard)

     Nobody but a GCSE pupil is ever sent to profile-setup. */
  function afterAuthTarget(acct, returnUrl) {
    var back = returnUrl || '/index.html';
    var explicit = back !== '/index.html';
    if (!acct || !acct.kind) return back;
    switch (acct.kind) {
      case 'child':     return acct.home;
      case 'parent':    return acct.home;
      case 'org_staff': return acct.home;
      case 'staff':
      case 'operator':  return explicit ? back : acct.home;
      case 'pupil':
        /* A pupil's home is their class page (the brief; the bar's own "My
           class" button), so signing in with nothing in particular in mind
           lands them there. An explicit ?return= still wins, a KS3 pupil is
           never sent to the GCSE wizard (MRB-101), and a GCSE pupil with no
           pathway or tier — or a brand-new account — still finishes setup
           first. No class (or a class lookup that could not run): ?return=. */
        if (acct.keyStage !== 'KS3' && acct.gcseComplete === false) return '/profile-setup.html';
        if (explicit) return back;
        return acct.hasClass && acct.home ? acct.home : back;
      default:          return back;
    }
  }

  /* ── Environment, session, REST ─────────────────────────────────────────
     Same rules as class-entry.js (which cannot be imported — it loads on
     pages this file must not depend on, and the reverse): the project ref
     comes out of the configured URL, and the session may be wrapped in a
     `base64-` envelope. */
  function cfg() {
    var c = root.MrBadmusConfig;
    if (c && c.SUPABASE_URL && c.SUPABASE_ANON_KEY) {
      return { url: c.SUPABASE_URL, key: c.SUPABASE_ANON_KEY,
               env: c.environment || 'prod', storage: c.AUTH_STORAGE_KEY || '' };
    }
    return { url: '', key: '', env: 'none', storage: '' };
  }

  function readSession(conf) {
    try {
      if (!conf.storage) return null;
      var raw = root.localStorage.getItem(conf.storage);
      if (!raw) return null;
      if (raw.indexOf('base64-') === 0) raw = decodeURIComponent(escape(root.atob(raw.slice(7))));
      var s = JSON.parse(raw);
      if (!s || !s.access_token || !s.user || !s.user.id) return null;
      var expMs = s.expires_at ? s.expires_at * 1000 : 0;
      if (expMs && expMs <= Date.now()) return null;
      return s;
    } catch (e) { return null; }
  }

  function rest(conf, session, path, init) {
    init = init || {};
    var headers = { 'apikey': conf.key, 'Authorization': 'Bearer ' + session.access_token,
                    'Accept': 'application/json' };
    if (init.body) headers['Content-Type'] = 'application/json';
    return root.fetch(conf.url + '/rest/v1/' + path, {
      method: init.method || 'GET', headers: headers, body: init.body
    }).then(function (r) { return r.ok ? r.json() : null; })
      .catch(function () { return null; });
  }

  // `env` / `api` ride along every redirect this file makes, so a tester on
  // ?env=test lands on a door that is still pointed at TEST (B2C polish,
  // 9 Oct 2026 — the same rule as nav.js `carry`).
  function withEnv(path) {
    try {
      var here = new URLSearchParams(root.location.search);
      var u = new URL(path, root.location.origin);
      ['env', 'api'].forEach(function (k) {
        var v = here.get(k);
        if (v && !u.searchParams.has(k)) u.searchParams.set(k, v);
      });
      return u.pathname + u.search + u.hash;
    } catch (e) { return path; }
  }

  // Shared with class-entry's `dropCaches`: this stem is in its CACHE_FAMILIES,
  // so a sign-out through any path sweeps the previous viewer's kind.
  var CACHE_FAMILY = 'mrb-account:';
  var FACTS_TTL_MS = 5 * 60 * 1000;
  var SCHOOL_TTL_MS = 30 * 60 * 1000;

  function cacheGet(key, ttl) {
    try {
      var box = JSON.parse(root.sessionStorage.getItem(key) || 'null');
      if (!box || typeof box.t !== 'number' || Date.now() - box.t > ttl) return null;
      return box.v;
    } catch (e) { return null; }
  }
  function cacheSet(key, v) {
    try { root.sessionStorage.setItem(key, JSON.stringify({ t: Date.now(), v: v })); } catch (e) {}
  }
  function factsKey(conf, uid) { return CACHE_FAMILY + 'v1:' + conf.env + ':' + uid; }
  function schoolKey(conf, uid, sid) { return CACHE_FAMILY + 'school:v1:' + conf.env + ':' + uid + ':' + sid; }

  function timed(p, ms, fallback) {
    return new Promise(function (resolve) {
      var done = false;
      var t = setTimeout(function () { if (!done) { done = true; resolve(fallback); } }, ms);
      p.then(function (v) { if (!done) { done = true; clearTimeout(t); resolve(v); } },
             function () { if (!done) { done = true; clearTimeout(t); resolve(fallback); } });
    });
  }

  var PROFILE_SELECT = 'first_name,last_name,display_name,role,school_id,key_stage,science_pathway,tier';

  /* The school half of the facts: schools.kind (readable by members under
     RLS) and, for staff with NO school, the operator RPC. Cached per viewer
     and school, because it changes about never. A failed read is NOT cached
     and answers with the fallback in the header. */
  function schoolFacts(conf, session, p) {
    var out = { schoolKind: null, isOperator: null };
    if (!isStaffRole(p.role)) return Promise.resolve(out);
    if (p.school_id) {
      var key = schoolKey(conf, session.user.id, p.school_id);
      var hit = cacheGet(key, SCHOOL_TTL_MS);
      if (hit) return Promise.resolve(hit);
      return rest(conf, session, 'schools?id=eq.' + encodeURIComponent(p.school_id) + '&select=kind')
        .then(function (rows) {
          if (rows && rows[0] && rows[0].kind) {
            out.schoolKind = rows[0].kind;
            cacheSet(key, out);
          }
          return out;
        });
    }
    var okey = schoolKey(conf, session.user.id, 'none');
    var ohit = cacheGet(okey, SCHOOL_TTL_MS);
    if (ohit) return Promise.resolve(ohit);
    return rest(conf, session, 'rpc/auth_user_is_platform_operator', { method: 'POST', body: '{}' })
      .then(function (v) {
        if (v === true || v === false) { out.isOperator = v; cacheSet(okey, out); }
        return out;
      });
  }

  function accountFrom(session, profile, school, isChild) {
    var p = profile || {};
    var kind = classify({
      isChild: isChild, role: p.role, schoolId: p.school_id,
      schoolKind: school && school.schoolKind, isOperator: school && school.isOperator
    });
    var acct = describe(kind, { childHome: root.MrBadmusConfig && root.MrBadmusConfig.CHILD_HOME });
    acct.userId = session.user.id;
    acct.role = p.role || null;
    acct.schoolKind = (school && school.schoolKind) || null;
    acct.name = nameFor(kind, p);
    acct.firstName = nameFor('pupil', p);
    acct.keyStage = p.key_stage || null;
    // Only meaningful for a pupil; `false` also covers "no profile row yet".
    acct.gcseComplete = !!(p.science_pathway && p.tier);
    acct.unknown = !kind;
    acct.hasClass = false;
    /* The ONE button the public bar shows for this person: their home, by the
       home's own label. A pupil's is set once their class is known (run()). */
    acct.homeButton = (kind && kind !== 'pupil') ? { href: acct.home, label: acct.homeLabel } : null;
    return acct;
  }

  /* ── resolve ────────────────────────────────────────────────────────────
     Session → account, or null when signed out. Options:
       session   use this session instead of reading the stored one
       profile   a profiles row the caller already has (the guards do);
                 spares the read, and is never cached (it may carry fewer
                 columns than the full select)
       fresh     skip the cache READ (auth.html: a profile finished a second
                 ago must not be answered from a five-minute-old row)
       classes   false → do not look up the pupil's class (auth.html, the
                 consumer guard); default true
       force     the pupil's class even on a staff surface (a pupil bounced
                 off a /teacher/ page still needs their way home)
     Memoised per page for the plain call, which is what nav, the bar and the
     drawer all make. */
  var _memo = null;

  function resolve(opts) {
    opts = opts || {};
    var plain = !opts.session && !opts.profile && !opts.fresh && opts.classes !== false && !opts.force;
    if (plain && _memo) return _memo;
    var p = run(opts);
    if (plain) _memo = p;
    return p;
  }

  function run(opts) {
    var conf = cfg();
    var session = opts.session || readSession(conf);
    if (!session || !session.user || !session.user.id || !conf.url) return Promise.resolve(null);

    var Cfg = root.MrBadmusConfig;
    var isChild = !!(Cfg && typeof Cfg.isChildSession === 'function' && Cfg.isChildSession(session));

    // A child's account needs no read at all: the address says it all, and
    // their name is not worth a round trip on a lesson page.
    if (isChild) {
      var childAcct = accountFrom(session, { role: 'student' }, null, true);
      return Promise.resolve(childAcct);
    }

    return classEntryReady(opts.classes !== false).then(function (ce) {
      return runWith(opts, conf, session, ce);
    });
  }

  /* class-entry.js is a deferred tag that runs AFTER nav.js and account.js, and
     nav.js asks for the account the moment it boots — so on a pupil's page the
     first answer would be given before the one module that knows their class
     had loaded, and read "no class". If the page HAS the tag, wait for it
     (bounded: 4s); if it has none, there is nothing to wait for. */
  function classEntryReady(want) {
    if (!want) return Promise.resolve(null);
    if (root.MRBClassEntry) return Promise.resolve(root.MRBClassEntry);
    var d = root.document;
    if (!d || !d.querySelector || !d.querySelector('script[src*="class-entry.js"]')) return Promise.resolve(null);
    return new Promise(function (resolve) {
      var tries = 0;
      (function poll() {
        if (root.MRBClassEntry) return resolve(root.MRBClassEntry);
        if (++tries > 80) return resolve(null);
        setTimeout(poll, 50);
      })();
    });
  }

  function runWith(opts, conf, session, ce) {
    var wantClass = opts.classes !== false && ce && typeof ce.pupilEntry === 'function';
    var key = factsKey(conf, session.user.id);

    var cached = (!opts.profile && !opts.fresh) ? cacheGet(key, FACTS_TTL_MS) : null;
    var pupilP = null;
    function pupilEntry() {
      if (!pupilP) pupilP = wantClass ? ce.pupilEntry({ force: !!opts.force }) : Promise.resolve(null);
      return pupilP;
    }

    var factsP;
    if (cached) {
      factsP = Promise.resolve({ profile: cached.profile, school: cached.school });
    } else {
      // Start the pupil's class read NOW, alongside the profile read. For a
      // pupil it is the answer; for anybody else it is the same wasted
      // membership query the site has always made on a non-staff page, and it
      // is thrown away. Doing it second would put one more round trip in
      // front of every pupil's class link.
      if (wantClass) pupilEntry();
      var profP = opts.profile
        ? Promise.resolve({ ok: true, row: opts.profile })
        : rest(conf, session, 'profiles?id=eq.' + encodeURIComponent(session.user.id) +
                              '&select=' + PROFILE_SELECT)
            .then(function (rows) { return rows ? { ok: true, row: rows[0] || null } : { ok: false }; });
      factsP = profP.then(function (r) {
        if (!r.ok) return null;                              // unknown, not "no profile"
        var prof = r.row || {};                              // {} = a new account, no row yet
        return schoolFacts(conf, session, prof).then(function (school) {
          // A new account (no row yet) is never cached: the row appears minutes later.
          if (!opts.profile && r.row) cacheSet(key, { profile: prof, school: school });
          return { profile: prof, school: school };
        });
      });
    }

    return factsP.then(function (facts) {
      if (!facts) {                       // kind null, unknown true: callers do nothing
        var u = describe(null);
        u.userId = session.user.id; u.role = null; u.schoolKind = null; u.name = null;
        u.firstName = null; u.keyStage = null; u.gcseComplete = null; u.unknown = true; u.hasClass = false; u.homeButton = null;
        return u;
      }
      var acct = accountFrom(session, facts.profile, facts.school, false);
      if (acct.kind !== 'pupil') return acct;
      if (!wantClass) { acct.homeButton = null; return acct; }   // class not looked up: no claim
      return pupilEntry().then(function (entry) {
        if (entry) {
          var d = describe('pupil', { classEntry: entry });
          acct.home = d.home; acct.homeLabel = d.homeLabel; acct.homeTitle = d.homeTitle;
          acct.hasClass = true;
          acct.homeButton = { href: d.home, label: d.homeLabel };
        }
        // else: a pupil with NO class has no home button (see nav.js — the
        // only page to send them to says "Back to homepage"); null, not a guess.
        return acct;
      });
    });
  }

  /* ── guardAudience ──────────────────────────────────────────────────────
     "Is this person on a page that is for them?" → Promise<boolean>.
     true = stay; false = a redirect to their own home has been started.
     FAIL-OPEN: a signed-out visitor, a read that failed, an unknown role,
     a target equal to the current page — all answer true. The page's own
     guard and the backend are the security boundary; this only stops a
     parent being shown a pupil's page and an error. */
  function guardAudience(audience, opts) {
    opts = opts || {};
    var allowed = AUDIENCES[audience];
    if (!allowed) return Promise.resolve(true);
    var ro = { profile: opts.profile, session: opts.session, classes: false };
    return resolve(ro).then(function (acct) {
      if (!acct || !acct.kind) return true;
      if (allowed.indexOf(acct.kind) !== -1) return true;
      return homeNow(acct).then(function (home) {
        if (!home) return true;
        var here = root.location.pathname.replace(/\.html$/, '');
        if (home.split('?')[0].replace(/\.html$/, '') === here) return true;
        root.location.replace(withEnv(home));
        return false;
      });
    }).catch(function () { return true; });
  }

  /* A pupil's home needs their class, which the cheap resolve above skipped. */
  function homeNow(acct) {
    var ce = root.MRBClassEntry;
    if (acct.kind === 'pupil' && ce && typeof ce.pupilEntry === 'function') {
      return ce.pupilEntry({ force: true }).then(function (entry) {
        return entry && entry.href ? entry.href : acct.home;
      }, function () { return acct.home; });
    }
    return Promise.resolve(acct.home);
  }

  /* ── signOut / switchAccount ────────────────────────────────────────────
     One sign-out for every page, with the consumer pages' belt and braces
     (consumer-common.js signOut): the local stores are cleared WHETHER OR NOT
     the network call worked, because a person on a shared device who pressed
     Sign out and is still signed in has not been signed out.

     Order is the whole of it:
       1. work out the door NOW, while the session still exists to ask;
       2. drop the caches (kind, class entry, staff session…);
       3. revoke the session at the server — raced against a timeout, so a
          dead network cannot hold the person on the page;
       4. clear every sign-in token this browser holds, for both projects,
          and the per-person name/route the nav remembered;
       5. leave, to the front page `/` — signed out, the bar says Sign in —
          or, for a family/organisation child alone, /go/ (their only door).
          (Until 16 Oct 2026 this was each kind's own door; see SIGN_OUT_TO.)
     `switchAccount()` is the same but lands on the school door whatever the kind:
     signing in as somebody else always starts at the one door every kind of
     person can use. No school page gains a link to the family side. */
  function clearLocalState(conf) {
    var ref = (/^https:\/\/([a-z0-9]+)\.supabase\.co/i.exec(conf.url) || [])[1] || '';
    [root.localStorage, root.sessionStorage].forEach(function (store) {
      var kill = [];
      try {
        for (var i = 0; i < store.length; i++) {
          var k = store.key(i);
          if (k == null) continue;
          if (/^sb-.*-auth-token/.test(k) || (ref && k.indexOf('sb-' + ref + '-') === 0) ||
              k.indexOf('mrb-profile-') === 0 || k.indexOf('mrb-home:') === 0 || k.indexOf('mrb-account:') === 0 ||
              // the consumer app's own state (a signup draft…): consumer-common's
              // clearLocalState sweeps `mrb.`, and a parent's family state must not
              // outlive Sign out on a shared device. Preferences (`mrb-theme`) are
              // `mrb-`, not `mrb.`, and stay.
              k.indexOf('mrb.') === 0) kill.push(k);
        }
      } catch (e) { return; }
      kill.forEach(function (k) { try { store.removeItem(k); } catch (e) {} });
    });
  }

  function signOut(opts) {
    opts = opts || {};
    var conf = cfg();
    var session = readSession(conf);
    var Cfg = root.MrBadmusConfig;

    /* Nothing to ask: whether this is a child is written on the session
       itself, so the destination is known before anything is torn down. */
    var door;
    if (opts.to) door = opts.to;
    else if (session && Cfg && typeof Cfg.isChildSession === 'function' && Cfg.isChildSession(session)) door = SIGN_OUT_TO.child;
    else door = SIGN_OUT_TO.adult;
    var doorP = Promise.resolve(door);

    return doorP.then(function (door) {
      try { var ce = root.MRBClassEntry; if (ce && ce.dropCaches) ce.dropCaches(); } catch (e) {}
      _memo = null;
      var revoke = Promise.resolve();
      try {
        if (opts.sb && opts.sb.auth && typeof opts.sb.auth.signOut === 'function') {
          revoke = Promise.resolve(opts.sb.auth.signOut());
        } else if (session && conf.url) {
          revoke = root.fetch(conf.url + '/auth/v1/logout', {
            method: 'POST', keepalive: true,
            headers: { 'apikey': conf.key, 'Authorization': 'Bearer ' + session.access_token }
          });
        }
      } catch (e) { revoke = Promise.resolve(); }
      return timed(revoke, 2500, null).then(function () {
        clearLocalState(conf);
        root.location.replace(withEnv(door));
      });
    });
  }

  function switchAccount(opts) {
    var o = {};
    for (var k in (opts || {})) o[k] = opts[k];
    o.to = DOORS.pupil;
    return signOut(o);
  }

  var api = {
    STAFF_ROLES: STAFF_ROLES,
    AUDIENCES: AUDIENCES,
    DOORS: DOORS,
    SIGN_OUT_TO: SIGN_OUT_TO,
    HOMES: HOMES,
    KIND_LABELS: KIND_LABELS,
    // pure
    classify: classify,
    describe: describe,
    nameFor: nameFor,
    afterAuthTarget: afterAuthTarget,
    // session-aware
    resolve: resolve,
    guardAudience: guardAudience,
    signOut: signOut,
    switchAccount: switchAccount
  };

  root.MrBadmusAccount = api;
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
})(typeof window !== 'undefined' ? window : globalThis);
