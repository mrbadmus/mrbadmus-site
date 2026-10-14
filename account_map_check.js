/* account_map_check.js — shared/account.js under Node (front door, Part 1).

   Two halves. The PURE map (classify / describe / afterAuthTarget / nameFor)
   is a table: every kind, the precedence between them, every home, door,
   label and profile route, and every case auth.html's redirectAfterAuth
   decided before it was lifted out. The SESSION half (resolve, guardAudience,
   signOut) runs against stubbed storage, fetch and location, to pin the
   fallbacks the header promises: a read that fails is never a bounce. */
'use strict';
var assert = require('assert');
var path = require('path');

var passed = 0, failed = 0;
function t(name, fn) {
  return Promise.resolve().then(fn).then(function () { passed++; },
    function (e) { failed++; console.log('FAIL  ' + name + '\n      ' + (e && e.message)); });
}

// ── environment stubs (account.js reads globalThis at CALL time) ──────────
function store() {
  var m = {};
  return { getItem: function (k) { return k in m ? m[k] : null; },
           setItem: function (k, v) { m[k] = String(v); },
           removeItem: function (k) { delete m[k]; },
           key: function (i) { return Object.keys(m)[i] || null; },
           get length() { return Object.keys(m).length; }, _m: m };
}
var REF = 'abcdefgh';
var STORAGE_KEY = 'sb-' + REF + '-auth-token';
var calls;
function world(o) {
  o = o || {};
  calls = [];
  globalThis.localStorage = store();
  globalThis.sessionStorage = store();
  globalThis.atob = function (s) { return Buffer.from(s, 'base64').toString('binary'); };
  globalThis.location = { search: o.search || '', origin: 'https://x.test', pathname: o.pathname || '/index.html',
                          replace: function (u) { calls.push(['replace', u]); } };
  globalThis.MrBadmusConfig = {
    SUPABASE_URL: 'https://' + REF + '.supabase.co', SUPABASE_ANON_KEY: 'k', environment: 'prod',
    AUTH_STORAGE_KEY: STORAGE_KEY, CHILD_HOME: '/consumer/today.html',
    isChildSession: function (s) { var e = s && s.user && s.user.email; return !!e && /@children\.mrbadmus\.internal$/.test(e); }
  };
  var session = o.session === null ? null : {
    access_token: 'tok', expires_at: Math.floor(Date.now() / 1000) + 3600,
    user: { id: 'u1', email: o.email || 'a@b.test' } };
  if (session) globalThis.localStorage.setItem(STORAGE_KEY, JSON.stringify(session));
  delete globalThis.MRBClassEntry;
  if (o.pupilEntry !== undefined) {
    globalThis.MRBClassEntry = { pupilEntry: function () { return Promise.resolve(o.pupilEntry); },
                                 dropCaches: function () { calls.push(['dropCaches']); } };
  }
  globalThis.fetch = function (url, init) {
    calls.push(['fetch', (init && init.method) || 'GET', url.replace(/^https:\/\/[a-z]+\.supabase\.co/, '')]);
    var respond = function (status, body) { return Promise.resolve({ ok: status < 300, status: status, json: function () { return Promise.resolve(body); } }); };
    if (/\/auth\/v1\/logout/.test(url)) return o.logoutFails ? Promise.reject(new Error('offline')) : respond(204, null);
    if (/\/rest\/v1\/profiles/.test(url)) return o.profileFails ? respond(500, null) : respond(200, o.profile === undefined ? [] : [o.profile]);
    if (/\/rest\/v1\/schools/.test(url)) return o.schoolFails ? respond(500, null) : respond(200, [{ kind: o.schoolKind }]);
    if (/rpc\/auth_user_is_platform_operator/.test(url)) return o.rpcFails ? respond(500, null) : respond(200, !!o.operator);
    return respond(404, null);
  };
  return session;
}
var A = require(path.join(__dirname, 'shared', 'account.js'));

var P = { // profile rows
  pupilGcse:  { role: 'student', first_name: 'Ayo', key_stage: 'KS4', science_pathway: 'combined', tier: 'higher' },
  pupilNoPath:{ role: 'student', first_name: 'Ayo', key_stage: 'KS4', science_pathway: null, tier: null },
  pupilKs3:   { role: 'student', first_name: 'Ayo', key_stage: 'KS3' },
  teacher:    { role: 'teacher', first_name: 'Mide', display_name: 'Mr Badmus', school_id: 's1' },
  hod:        { role: 'hod', first_name: 'Hod', school_id: 's1' },
  admin:      { role: 'admin', first_name: 'Ad', school_id: 's1' },
  noSchool:   { role: 'admin', first_name: 'Op' },
  parent:     { role: 'parent', first_name: 'Dad' }
};

var jobs = [];
function job(n, f) { jobs.push(function () { return t(n, f); }); }

// ── 1. PRECEDENCE: classify ───────────────────────────────────────────────
job('classify: every kind', function () {
  var c = A.classify;
  assert.strictEqual(c({ role: 'student' }), 'pupil');
  assert.strictEqual(c({}), 'pupil', 'no profile row yet = a new pupil');
  assert.strictEqual(c({ role: 'parent' }), 'parent');
  assert.strictEqual(c({ isChild: true, role: 'student' }), 'child');
  ['teacher', 'hod', 'admin'].forEach(function (r) {
    assert.strictEqual(c({ role: r, schoolId: 's', schoolKind: 'school' }), 'staff', r);
    assert.strictEqual(c({ role: r, schoolId: 's', schoolKind: 'organisation' }), 'org_staff', r);
    assert.strictEqual(c({ role: r, isOperator: true }), 'operator', r);
    assert.strictEqual(c({ role: r, isOperator: false }), 'staff', r);
  });
  assert.strictEqual(c({ role: 'wizard' }), null, 'an unheard-of role is unknown, not a pupil');
});
job('classify: precedence order', function () {
  var c = A.classify;
  assert.strictEqual(c({ isChild: true, role: 'parent' }), 'child', 'child beats parent');
  assert.strictEqual(c({ isChild: true, role: 'teacher', schoolId: 's', schoolKind: 'organisation' }), 'child', 'child beats org staff');
  assert.strictEqual(c({ role: 'teacher', schoolId: 's', schoolKind: 'organisation', isOperator: true }), 'org_staff', 'organisation beats operator');
  assert.strictEqual(c({ role: 'teacher', schoolId: 's', schoolKind: 'school', isOperator: true }), 'staff', 'a teacher who is also an operator is staff');
  assert.strictEqual(c({ role: 'admin', schoolId: null, isOperator: true }), 'operator', 'operator only when NO school');
  assert.strictEqual(c({ role: 'teacher', schoolId: 's', schoolKind: 'family' }), 'staff');
});
job('classify: read failures fall back to the role-only answer', function () {
  var c = A.classify;
  assert.strictEqual(c({ role: 'teacher', schoolId: 's', schoolKind: null }), 'staff', 'schools read failed');
  assert.strictEqual(c({ role: 'admin', schoolId: null, isOperator: null }), 'staff', 'operator rpc failed');
  assert.strictEqual(c({ role: 'admin', schoolId: null, isOperator: undefined }), 'staff');
});

// ── 2. HOMES, DOORS, LABELS, PROFILES ─────────────────────────────────────
job('describe: homes, labels, doors, profile routes, kind labels', function () {
  var want = {
    pupil:     ['/student/classes.html',        'My classes',   '/auth.html',             '/profile-setup.html',  'Pupil'],
    staff:     ['/teacher/today.html',          'My classes',   '/auth.html',             '/teacher-profile.html','Teacher'],
    parent:    ['/consumer/overview.html',      'My dashboard', '/parents/sign-in.html',  '/consumer/account.html','Parent'],
    child:     ['/consumer/today.html',         'Today',        '/go/',                   null,                   'Pupil'],
    org_staff: ['/org/index.html',              'My dashboard', '/org/sign-in.html',      null,                   'Organisation'],
    operator:  ['/consumer/admin-accounts.html','My dashboard', '/auth.html',             null,                   'Operator']
  };
  Object.keys(want).forEach(function (k) {
    var d = A.describe(k), w = want[k];
    assert.deepStrictEqual([d.home, d.homeLabel, d.door, d.profileUrl, d.kindLabel], w, k);
    assert.strictEqual(d.kind, k);
  });
});
job('describe: a pupil with a class goes to it; child home follows config', function () {
  var d = A.describe('pupil', { classEntry: { href: '/student/class.html?class=c1', label: 'My class', title: '10h/Sc1' } });
  assert.strictEqual(d.home, '/student/class.html?class=c1');
  assert.strictEqual(d.homeLabel, 'My class');
  assert.strictEqual(A.describe('child', { childHome: '/x/y.html' }).home, '/x/y.html');
});
job('describe: unknown kind has no home and the school door', function () {
  var d = A.describe(null);
  assert.strictEqual(d.kind, null); assert.strictEqual(d.home, null); assert.strictEqual(d.door, '/auth.html');
});
job('no school-facing kind\'s door is a family/org link (those are sign-out destinations only)', function () {
  ['pupil', 'staff', 'operator'].forEach(function (k) { assert.strictEqual(A.DOORS[k], '/auth.html', k); });
});
job('nameFor: staff by display name, others by first name', function () {
  assert.strictEqual(A.nameFor('staff', P.teacher), 'Mr Badmus');
  assert.strictEqual(A.nameFor('staff', P.hod), 'Hod');
  assert.strictEqual(A.nameFor('parent', P.parent), 'Dad');
  assert.strictEqual(A.nameFor('pupil', { first_name: ' Ayo ', display_name: 'x' }), 'Ayo');
  assert.strictEqual(A.nameFor('pupil', {}), null);
});

// ── 3. afterAuthTarget — every branch redirectAfterAuth had ───────────────
job('afterAuthTarget', function () {
  var T = A.afterAuthTarget, d = A.describe;
  function acct(kind, extra) { var a = d(kind); for (var k in extra) a[k] = extra[k]; return a; }
  assert.strictEqual(T(acct('child'), '/x.html'), '/consumer/today.html', 'child ignores return');
  assert.strictEqual(T(acct('parent'), '/x.html'), '/consumer/overview.html', '9 Oct parent fix kept; return ignored');
  assert.strictEqual(T(acct('org_staff'), '/index.html'), '/org/index.html');
  assert.strictEqual(T(acct('staff'), '/index.html'), '/teacher/today.html', 'staff default = Today');
  assert.strictEqual(T(acct('staff'), '/teacher/classes.html'), '/teacher/classes.html', 'staff honours an explicit return');
  assert.strictEqual(T(acct('operator'), '/index.html'), '/consumer/admin-accounts.html');
  assert.strictEqual(T(acct('operator'), '/x.html'), '/x.html');
  var cls = { hasClass: true, home: '/student/class.html?class=c1' };
  function pup(extra) { return acct('pupil', Object.assign({ gcseComplete: true, keyStage: 'KS4' }, extra)); }
  assert.strictEqual(T(pup({ keyStage: 'KS3', gcseComplete: false }), '/ks3/'), '/ks3/', 'KS3 never to the wizard (MRB-101), explicit return honoured');
  assert.strictEqual(T(pup({ keyStage: 'KS3', gcseComplete: false }), '/index.html'), '/index.html', 'KS3 with no class and no return');
  assert.strictEqual(T(pup(Object.assign({ keyStage: 'KS3', gcseComplete: false }, cls)), '/index.html'), cls.home, 'KS3 with a class lands on it');
  assert.strictEqual(T(pup(Object.assign({ keyStage: 'KS3', gcseComplete: false }, cls)), '/ks3/'), '/ks3/', 'KS3, explicit return beats the class');
  assert.strictEqual(T(pup({ gcseComplete: false }), '/index.html'), '/profile-setup.html', 'GCSE incomplete');
  assert.strictEqual(T(pup(Object.assign({ gcseComplete: false }, cls)), '/index.html'), '/profile-setup.html', 'GCSE incomplete beats the class');
  assert.strictEqual(T(pup({ keyStage: null, gcseComplete: false }), '/index.html'), '/profile-setup.html', 'new account, no profile row');
  assert.strictEqual(T(pup({}), '/x.html'), '/x.html', 'complete GCSE, explicit return');
  assert.strictEqual(T(pup({}), '/index.html'), '/index.html', 'complete GCSE, no class, no return');
  assert.strictEqual(T(pup(cls), '/index.html'), cls.home, 'complete GCSE with a class lands on it');
  assert.strictEqual(T(pup(cls), '/x.html'), '/x.html', 'explicit return beats the class');
  assert.strictEqual(T(pup({ hasClass: false, home: '/student/classes.html' }), '/index.html'), '/index.html', 'the picker is not a home for a classless pupil');
  assert.strictEqual(T({ kind: null, unknown: true }, '/x.html'), '/x.html', 'a failed read is not a reason for the wizard');
  assert.strictEqual(T(null, undefined), '/index.html');
  // Nobody but a GCSE pupil is ever sent to profile-setup.
  ['child', 'parent', 'org_staff', 'staff', 'operator'].forEach(function (k) {
    assert.notStrictEqual(T(acct(k, { gcseComplete: false, keyStage: 'KS4' }), '/index.html'), '/profile-setup.html', k);
  });
});

// ── 4. AUDIENCES ──────────────────────────────────────────────────────────
job('audiences: consumer turns away only a school pupil', function () {
  var all = ['pupil', 'staff', 'parent', 'child', 'org_staff', 'operator'];
  all.forEach(function (k) {
    var allowed = A.AUDIENCES.consumer.indexOf(k) !== -1;
    assert.strictEqual(allowed, k !== 'pupil', k);
  });
  assert.deepStrictEqual(A.AUDIENCES.challenge, ['pupil', 'staff', 'operator']);
  assert.deepStrictEqual(A.AUDIENCES.staff, ['staff', 'operator']);
  assert.deepStrictEqual(A.AUDIENCES.pupil, ['pupil']);
});

// ── 5. resolve against stubbed reads ──────────────────────────────────────
function resolveWith(o, opts) { world(o); return A.resolve(Object.assign({ fresh: true }, opts || {})); }
job('resolve: signed out is null', function () {
  return resolveWith({ session: null }).then(function (a) { assert.strictEqual(a, null); });
});
job('resolve: child needs no read at all', function () {
  return resolveWith({ email: 'x@children.mrbadmus.internal' }).then(function (a) {
    assert.strictEqual(a.kind, 'child'); assert.strictEqual(a.home, '/consumer/today.html');
    assert.strictEqual(calls.filter(function (c) { return c[0] === 'fetch'; }).length, 0);
  });
});
job('resolve: parent', function () {
  return resolveWith({ profile: P.parent }).then(function (a) {
    assert.strictEqual(a.kind, 'parent'); assert.strictEqual(a.name, 'Dad'); assert.strictEqual(a.profileUrl, '/consumer/account.html');
    assert.strictEqual(a.door, '/parents/sign-in.html');
  });
});
job('resolve: the 9 Oct trap — a parent is never routed to a teacher page', function () {
  return resolveWith({ profile: P.parent }).then(function (a) {
    assert.ok(!/teacher/.test(a.profileUrl + a.home));
  });
});
job('resolve: school staff, org staff, operator, teacher-who-is-operator', function () {
  return resolveWith({ profile: P.teacher, schoolKind: 'school', operator: true }).then(function (a) {
    assert.strictEqual(a.kind, 'staff'); assert.strictEqual(a.name, 'Mr Badmus');
    assert.strictEqual(calls.some(function (c) { return /rpc/.test(c[2]); }), false, 'no operator call when there is a school');
    return resolveWith({ profile: P.teacher, schoolKind: 'organisation' });
  }).then(function (a) {
    assert.strictEqual(a.kind, 'org_staff'); assert.strictEqual(a.home, '/org/index.html');
    return resolveWith({ profile: P.noSchool, operator: true });
  }).then(function (a) {
    assert.strictEqual(a.kind, 'operator'); assert.strictEqual(a.home, '/consumer/admin-accounts.html');
    return resolveWith({ profile: P.noSchool, operator: false });
  }).then(function (a) { assert.strictEqual(a.kind, 'staff'); });
});
job('resolve: failed schools / rpc reads fall back to staff, never to unknown', function () {
  return resolveWith({ profile: P.teacher, schoolFails: true }).then(function (a) {
    assert.strictEqual(a.kind, 'staff');
    return resolveWith({ profile: P.noSchool, rpcFails: true });
  }).then(function (a) { assert.strictEqual(a.kind, 'staff'); });
});
job('resolve: a failed profile read is unknown (kind null), not "new user"', function () {
  return resolveWith({ profileFails: true }).then(function (a) {
    assert.strictEqual(a.kind, null); assert.strictEqual(a.unknown, true);
    assert.strictEqual(A.afterAuthTarget(a, '/back'), '/back');
  });
});
job('resolve: no profile row = a new pupil who needs the wizard', function () {
  return resolveWith({ profile: undefined }).then(function (a) {
    assert.strictEqual(a.kind, 'pupil'); assert.strictEqual(a.gcseComplete, false);
    assert.strictEqual(A.afterAuthTarget(a, '/index.html'), '/profile-setup.html');
  });
});
job('resolve: the one home button — by kind; a classless pupil has none', function () {
  return resolveWith({ profile: P.parent }).then(function (a) {
    assert.deepStrictEqual(a.homeButton, { href: '/consumer/overview.html', label: 'My dashboard' });
    return resolveWith({ profile: P.teacher, schoolKind: 'school' });
  }).then(function (a) {
    assert.deepStrictEqual(a.homeButton, { href: '/teacher/today.html', label: 'My classes' });
    return resolveWith({ email: 'k@children.mrbadmus.internal' });
  }).then(function (a) {
    assert.deepStrictEqual(a.homeButton, { href: '/consumer/today.html', label: 'Today' });
    return resolveWith({ profile: P.pupilGcse, pupilEntry: null });
  }).then(function (a) {
    assert.strictEqual(a.homeButton, null, 'no class, no button: /student/classes.html would loop');
    return resolveWith({ profile: P.pupilGcse, pupilEntry: { href: '/student/class.html?class=c1', label: 'My class', title: 't' } });
  }).then(function (a) {
    assert.deepStrictEqual(a.homeButton, { href: '/student/class.html?class=c1', label: 'My class' });
  });
});
job('resolve: pupil gets their class from class-entry, not from a second query', function () {
  var entry = { href: '/student/class.html?class=c9', label: 'My class', title: '9x' };
  return resolveWith({ profile: P.pupilGcse, pupilEntry: entry }).then(function (a) {
    assert.strictEqual(a.kind, 'pupil'); assert.strictEqual(a.home, entry.href); assert.strictEqual(a.hasClass, true);
    assert.strictEqual(calls.some(function (c) { return /class_members/.test(c[2]); }), false);
    return resolveWith({ profile: P.pupilGcse, pupilEntry: null });
  }).then(function (a) { assert.strictEqual(a.hasClass, false); assert.strictEqual(a.home, '/student/classes.html'); });
});
job('resolve: kind is cached per viewer and swept by the family stem', function () {
  world({ profile: P.parent });
  return A.resolve({ fresh: true }).then(function () {
    var keys = Object.keys(globalThis.sessionStorage._m);
    assert.ok(keys.length && keys.every(function (k) { return k.indexOf('mrb-account:') === 0; }), keys.join());
    calls.length = 0;
    return A.resolve({ classes: false });
  }).then(function (a) {
    assert.strictEqual(a.kind, 'parent');
    assert.strictEqual(calls.filter(function (c) { return c[0] === 'fetch'; }).length, 0, 'second answer from cache');
  });
});

// ── 6. guardAudience ──────────────────────────────────────────────────────
function guard(aud, o, opts) { world(o); return A.guardAudience(aud, Object.assign({}, opts || {})); }
job('guardAudience: org staff on a teacher page go to /org/index.html', function () {
  return guard('staff', { profile: P.teacher, schoolKind: 'organisation', pathname: '/teacher/today.html' }, { profile: P.teacher })
    .then(function (ok) { assert.strictEqual(ok, false); assert.deepStrictEqual(calls.filter(function (c) { return c[0] === 'replace'; }), [['replace', '/org/index.html']]); });
});
job('guardAudience: school staff and the operator stay on a teacher page', function () {
  return guard('staff', { profile: P.teacher, schoolKind: 'school' }, { profile: P.teacher }).then(function (ok) {
    assert.strictEqual(ok, true);
    return guard('staff', { profile: P.noSchool, operator: true }, { profile: P.noSchool });
  }).then(function (ok) { assert.strictEqual(ok, true); });
});
job('guardAudience: a parent on a pupil page goes to the family dashboard (never /index.html)', function () {
  return guard('pupil', { profile: P.parent, pathname: '/student/class.html' }, { profile: P.parent }).then(function (ok) {
    assert.strictEqual(ok, false);
    assert.deepStrictEqual(calls.filter(function (c) { return c[0] === 'replace'; }), [['replace', '/consumer/overview.html']]);
  });
});
job('guardAudience: consumer turns away a pupil to their class, lets a parent, child and operator stay', function () {
  var entry = { href: '/student/class.html?class=c1', label: 'My class', title: 't' };
  return guard('consumer', { profile: P.pupilGcse, pupilEntry: entry, pathname: '/consumer/overview.html' }, { profile: P.pupilGcse }).then(function (ok) {
    assert.strictEqual(ok, false);
    assert.deepStrictEqual(calls.filter(function (c) { return c[0] === 'replace'; }), [['replace', entry.href]]);
    return guard('consumer', { profile: P.parent }, { profile: P.parent });
  }).then(function (ok) {
    assert.strictEqual(ok, true);
    return guard('consumer', { email: 'k@children.mrbadmus.internal' }, {});
  }).then(function (ok) {
    assert.strictEqual(ok, true);
    return guard('consumer', { profile: P.noSchool, operator: true }, { profile: P.noSchool });
  }).then(function (ok) { assert.strictEqual(ok, true); });
});
job('guardAudience: fail-open (signed out, failed read, unknown audience, already home)', function () {
  return guard('pupil', { session: null }, {}).then(function (ok) {
    assert.strictEqual(ok, true);
    return guard('pupil', { profileFails: true }, {});
  }).then(function (ok) {
    assert.strictEqual(ok, true); assert.strictEqual(calls.filter(function (c) { return c[0] === 'replace'; }).length, 0);
    return guard('nonsense', { profile: P.parent }, { profile: P.parent });
  }).then(function (ok) {
    assert.strictEqual(ok, true);
    return guard('pupil', { profile: P.parent, pathname: '/consumer/overview.html' }, { profile: P.parent });
  }).then(function (ok) { assert.strictEqual(ok, true, 'never redirect to the page you are on'); });
});
job('guardAudience: ?env / ?api survive the bounce', function () {
  return guard('pupil', { profile: P.parent, search: '?env=test&api=http://localhost:3100', pathname: '/student/class.html' }, { profile: P.parent })
    .then(function () {
      var r = calls.filter(function (c) { return c[0] === 'replace'; })[0][1];
      assert.ok(/env=test/.test(r) && /api=http/.test(r), r);
    });
});

// ── 7. signOut ────────────────────────────────────────────────────────────
function signOutWith(o, fn) {
  world(o);
  var p = A.signOut(fn || {});
  return p.then(function () {
    return { to: (calls.filter(function (c) { return c[0] === 'replace'; })[0] || [])[1],
             token: globalThis.localStorage.getItem(STORAGE_KEY) };
  });
}
job('signOut: each kind lands on its own door, and the token is gone', function () {
  return signOutWith({ profile: P.parent }).then(function (r) {
    assert.strictEqual(r.to, '/parents/sign-in.html'); assert.strictEqual(r.token, null);
    return signOutWith({ email: 'k@children.mrbadmus.internal' });
  }).then(function (r) {
    assert.strictEqual(r.to, '/go/');
    return signOutWith({ profile: P.teacher, schoolKind: 'school' });
  }).then(function (r) {
    assert.strictEqual(r.to, '/auth.html');
    return signOutWith({ profile: P.teacher, schoolKind: 'organisation' });
  }).then(function (r) { assert.strictEqual(r.to, '/org/sign-in.html'); });
});
job('signOut: still signs out when the network is down', function () {
  return signOutWith({ profile: P.parent, logoutFails: true }).then(function (r) {
    assert.strictEqual(r.token, null, 'local token cleared regardless'); assert.strictEqual(r.to, '/parents/sign-in.html');
  });
});
job('signOut: unknown kind (failed read) → the school door; switchAccount → school door whatever the kind', function () {
  return signOutWith({ profileFails: true }).then(function (r) {
    assert.strictEqual(r.to, '/auth.html');
    world({ profile: P.parent });
    return A.switchAccount();
  }).then(function () {
    assert.strictEqual(calls.filter(function (c) { return c[0] === 'replace'; })[0][1], '/auth.html');
  });
});
job('signOut: sweeps the remembered name/route and the kind cache; drops class-entry caches', function () {
  world({ profile: P.parent, pupilEntry: null });
  globalThis.localStorage.setItem('mrb-profile-name:u1', 'Dad');
  globalThis.localStorage.setItem('mrb-profile-href:v2:u1', '/consumer/account.html');
  globalThis.localStorage.setItem('mrb-theme', 'dark');
  return A.signOut({}).then(function () {
    assert.strictEqual(globalThis.localStorage.getItem('mrb-profile-name:u1'), null);
    assert.strictEqual(globalThis.localStorage.getItem('mrb-profile-href:v2:u1'), null);
    assert.strictEqual(globalThis.localStorage.getItem('mrb-theme'), 'dark', 'the theme preference is not the person\'s');
    assert.ok(calls.some(function (c) { return c[0] === 'dropCaches'; }));
    assert.strictEqual(Object.keys(globalThis.sessionStorage._m).filter(function (k) { return k.indexOf('mrb-account:') === 0; }).length, 0);
  });
});
job('signOut: clears the consumer app\'s mrb.* state but keeps preferences', function () {
  world({ profile: P.parent });
  globalThis.localStorage.setItem('mrb.signup.draft', '{}');
  globalThis.sessionStorage.setItem('mrb.other', '1');
  globalThis.localStorage.setItem('mrb-theme', 'dark');
  globalThis.localStorage.setItem('mrb-pref-x', '1');
  return A.signOut({}).then(function () {
    assert.strictEqual(globalThis.localStorage.getItem('mrb.signup.draft'), null);
    assert.strictEqual(globalThis.sessionStorage.getItem('mrb.other'), null);
    assert.strictEqual(globalThis.localStorage.getItem('mrb-theme'), 'dark');
    assert.strictEqual(globalThis.localStorage.getItem('mrb-pref-x'), '1');
  });
});
job('signOut via a guard\'s delegation: the guard\'s sb is revoked and class-entry caches dropped', function () {
  world({ profile: P.teacher, schoolKind: 'school', pupilEntry: null });
  var revoked = 0;
  return A.signOut({ sb: { auth: { signOut: function () { revoked++; return Promise.resolve(); } } } }).then(function () {
    assert.strictEqual(revoked, 1);
    assert.ok(calls.some(function (c) { return c[0] === 'dropCaches'; }));
    assert.ok(!calls.some(function (c) { return c[0] === 'fetch' && /logout/.test(c[2]); }), 'no second revoke');
  });
});
job('signOut: env carried onto the door', function () {
  return signOutWith({ profile: P.parent, search: '?env=test' }).then(function (r) { assert.ok(/env=test/.test(r.to), r.to); });
});

// ── 8. isolation: this file names no project or backend ───────────────────
job('account.js spells out no Supabase project or backend host', function () {
  var src = require('fs').readFileSync(path.join(__dirname, 'shared', 'account.js'), 'utf8');
  assert.ok(!/onrender\.com/.test(src)); assert.ok(!/https?:\/\/[a-z0-9]{20}\.supabase\.co/.test(src), 'a literal Supabase project URL');
});

// run strictly in order — they share globals
jobs.reduce(function (p, j) { return p.then(j); }, Promise.resolve()).then(function () {
  console.log('account_map_check: ' + passed + ' passed, ' + failed + ' failed');
  process.exit(failed ? 1 : 0);
});
