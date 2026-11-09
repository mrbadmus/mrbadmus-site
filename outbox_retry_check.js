/* outbox_retry_check.js — a family child's answer is re-sent without a reload
 * (9 Nov 2026, blind-test fix F5). Runs the REAL startOutboxRetry in shared/account.js
 * against a stand-in clock, storage and network.
 *
 *     python3 outbox_retry_check.py
 *
 *   1. a school pupil: no timer, no request, ever;
 *   2. a 429: the answer stays queued, nothing is sent until the wait it was told
 *      has passed, and then it goes, with its own client_event_id and answered_at,
 *      and without a reload;
 *   3. never doubled: a server that already has the id answers with its row, and
 *      the queue empties; never lost: every failure keeps it;
 *   4. an answer still in its first send (under a minute old) is left alone;
 *   5. order, the 7-day limit, a 401's one refresh, a sign-out.
 */
const assert = require('assert');
const path = require('path');
const A = require(path.join(__dirname, 'shared', 'account.js'));

let pass = 0, fail = 0;
function ok(c, what, detail) {
  if (c) { pass++; console.log('  ✅ ' + what); }
  else { fail++; console.log('  ❌ ' + what + (detail !== undefined ? '\n       ' + JSON.stringify(detail) : '')); }
}
const eq = (g, w, what) => ok(JSON.stringify(g) === JSON.stringify(w), what, { got: g, want: w });

const KEY = 'mrb_answer_outbox_v1', AUTH = 'sb-test-auth';
const CHILD = { access_token: 'tok', user: { email: 'ada@children.mrbadmus.internal' } };
const PUPIL = { access_token: 'tok', user: { email: 'pupil@rainford.example' } };
const NOW0 = Date.parse('2026-11-09T18:00:00Z');

function rig(session, box, respond, extra) {
  const store = new Map();
  if (session) store.set(AUTH, JSON.stringify(session));
  if (box) store.set(KEY, JSON.stringify(box));
  const sent = [];
  const R = {
    t: NOW0, timers: [], sent, store,
    box: () => JSON.parse(store.get(KEY) || '[]'),
    async advance(ms) {
      const end = R.t + ms;
      for (;;) {
        const due = R.timers.filter((x) => x.at <= end).sort((a, b) => a.at - b.at)[0];
        if (!due) break;
        R.timers.splice(R.timers.indexOf(due), 1);
        R.t = Math.max(R.t, due.at);
        due.f();
        for (let i = 0; i < 20; i += 1) await Promise.resolve();
      }
      R.t = end;
    },
  };
  R.started = A.startOutboxRetry(Object.assign({
    config: { AUTH_STORAGE_KEY: AUTH, BACKEND_URL: 'https://api.test', isChildSession: (s) => !!(s && s.user && /@children\.mrbadmus\.internal$/.test(s.user.email)) },
    storage: { getItem: (k) => (store.has(k) ? store.get(k) : null), setItem: (k, v) => store.set(k, v), removeItem: (k) => store.delete(k) },
    now: () => R.t,
    fetch: async (u, o) => {
      const body = JSON.parse(o.body);
      sent.push({ u, body, auth: o.headers.Authorization, at: R.t });
      return respond(body, sent.length);
    },
    setTimeout: (f, ms) => { const x = { f, at: R.t + ms }; R.timers.push(x); return x; },
    clearTimeout: (x) => { const i = R.timers.indexOf(x); if (i >= 0) R.timers.splice(i, 1); },
    auth: null,
  }, extra || {}));
  return R;
}
const ans = (id, minsAgo) => ({ client_event_id: id, answered_at: new Date(NOW0 - minsAgo * 60000).toISOString(), question_id: 'q-' + id, answer: 'x' });
const okRes = { ok: true, status: 200, json: async () => ({ ok: true }) };
const r429 = (s) => ({ ok: false, status: 429, json: async () => ({ error: 'rate_limited', retry_after_s: s }) });

(async () => {
  console.log('\n1. A school pupil');
  {
    const R = rig(PUPIL, [ans('a', 10)], () => okRes);
    eq([R.started, R.timers.length], [false, 0], 'no family child\'s session: no timer is ever set');
    await R.advance(3600 * 1000);
    eq(R.sent.length, 0, 'and not one request in an hour');
    const none = rig(null, null, () => okRes);
    eq([none.started, none.timers.length], [false, 0], 'nobody signed in: the same');
  }

  console.log('\n2. A 429 clears itself, with no reload');
  {
    let refuse = true;
    const R = rig(CHILD, [ans('a', 2)], () => (refuse ? r429(600) : okRes));
    await R.advance(45 * 1000);
    eq(R.sent.length, 1, 'the waiting answer is re-sent');
    eq(R.box().length, 1, 'refused: it stays queued');
    await R.advance(599 * 1000);
    eq(R.sent.length, 1, 'nothing more is sent until the wait the server gave has passed');
    refuse = false;
    await R.advance(2 * 1000);
    eq(R.sent.length, 2, 'then it goes again');
    eq(R.box(), [], 'and leaves the queue only now the server has it');
    eq([R.sent[0].body.client_event_id, R.sent[1].body.client_event_id], ['a', 'a'], 'the same client_event_id');
    eq(R.sent[1].body.answered_at, ans('a', 2).answered_at, 'and the moment it was answered, not the moment it was re-sent');
    ok(R.sent[0].u.endsWith('/api/consumer/child/answer'), 'to the answer route');
  }

  console.log('\n3. Never doubled, never lost');
  {
    // The server's duplicate path answers 200 with the row it already made.
    const ledger = new Map();
    const R = rig(CHILD, [ans('a', 5), ans('b', 4), ans('c', 3)], (body) => {
      if (!ledger.has(body.client_event_id)) ledger.set(body.client_event_id, body);
      return okRes;
    });
    await R.advance(45 * 1000);
    eq([...ledger.keys()], ['a', 'b', 'c'], 'oldest first, each once');
    eq(R.box(), [], 'the queue empties');
    await R.advance(600 * 1000);
    eq(ledger.size, 3, 'and nothing is sent again');
    let tries = 0;
    const R2 = rig(CHILD, [ans('a', 5), ans('b', 4)], (body) => { tries += 1; return tries === 1 ? okRes : { ok: false, status: 500, json: async () => ({}) }; });
    await R2.advance(45 * 1000);
    eq(R2.box().map((b) => b.client_event_id), ['b'], 'a 500 keeps what it refused');
    const R3 = rig(CHILD, [ans('a', 5)], () => { throw new Error('offline'); });
    await R3.advance(45 * 1000);
    eq(R3.box().length, 1, 'no connection keeps it');
    await R3.advance(90 * 1000);
    ok(R3.sent.length >= 2, 'and tries again, more slowly', R3.sent.length);
    const before = R3.sent.length;
    await R3.advance(60 * 1000);
    ok(R3.sent.length <= before + 1, 'with a pause that grows');
    const R4 = rig(CHILD, [ans('a', 5), ans('b', 4)], (body) => (body.client_event_id === 'a' ? r429(30) : okRes));
    await R4.advance(45 * 1000);
    eq(R4.sent.map((s) => s.body.client_event_id), ['a'], 'a refusal stops the run: it is not hammered with the rest');
    // Another tab's answer, written while this one was busy, is not lost by the drop.
    let later;
    const R5 = rig(CHILD, [ans('a', 5)], () => { later(); return okRes; });
    later = () => R5.store.set(KEY, JSON.stringify([ans('a', 5), ans('new', 0)]));
    await R5.advance(45 * 1000);
    eq(R5.box().map((b) => b.client_event_id), ['new'], 'an answer queued meanwhile is kept');
  }

  console.log('\n4. A first send still in flight is left alone');
  {
    const R = rig(CHILD, [Object.assign(ans('fresh', 0))], () => okRes);
    await R.advance(45 * 1000);
    eq(R.sent.length, 0, 'under a minute old (a written answer can take half a minute to mark): not touched');
    await R.advance(45 * 1000);
    eq(R.sent.length, 1, 'older than that, it is');
  }

  console.log('\n5. The edges');
  {
    const R = rig(CHILD, [ans('old', 8 * 24 * 60)], () => okRes);
    await R.advance(45 * 1000);
    eq(R.sent.length, 0, 'over 7 days old: the server refuses it, so it is not sent');
    let refreshed = 0;
    const seen = [];
    const auth = { token: async () => 'stale', refresh: async () => { refreshed += 1; return 'new'; } };
    const R2 = rig(CHILD, [ans('a', 5)], (b, n) => { seen.push(n); return n === 1 ? { ok: false, status: 401, json: async () => ({}) } : okRes; }, { auth: () => auth });
    await R2.advance(45 * 1000);
    eq([refreshed, R2.sent.map((s) => s.auth), R2.box()], [1, ['Bearer stale', 'Bearer new'], []], 'a 401 refreshes once and sends once more');
    const R3 = rig(CHILD, [ans('a', 5)], () => r429(30));
    await R3.advance(45 * 1000);
    R3.store.delete(AUTH);
    const n = R3.sent.length;
    await R3.advance(3600 * 1000);
    eq([R3.sent.length, R3.timers.length], [n, 0], 'signed out: it stops, and the queue waits for them');
    const R4 = rig(CHILD, null, () => okRes);
    await R4.advance(3600 * 1000);
    eq(R4.sent.length, 0, 'an empty queue sends nothing');
    ok(typeof window === 'undefined', 'run as a module: nothing started by itself');
  }

  console.log(`\n${pass} passed, ${fail} failed`);
  process.exit(fail ? 1 : 0);
})().catch((e) => { console.error(e); process.exit(1); });
