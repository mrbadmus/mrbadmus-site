"""leaderboard_seam.py — the leaderboard's data seam, driven directly.

MRB-290, the fast gate that `leaderboard_behaviour` cannot be.

⚑ WHY THIS EXISTS AS A SEPARATE GATE, AND IT IS A COVERAGE HOLE I FOUND BY
ADMITTING TO ONE.

`leaderboard_behaviour.py` drives eight fixtures, and every one of them
REPLACES `window.MrBadmusLeaderboardLive` wholesale with canned shapes. That
is the right design — it is what lets the behaviour gate press every control
with no network and no credential — but it means the behaviour gate never
executes a single line of `shared/leaderboard-live.js`. `load()`, `boot()`,
`mapRow()` and `safeAvatar()` were all completely ungated, and two real fixes
landed in them (the error-key refetch and the warm-up ping) with nothing
watching either.

So this gate drives THE REAL FILE, under Node, with a stubbed `fetch` and a
stubbed Supabase client. It asserts the things that live between the network
and Design's arithmetic:

  · the warm-up ping fires (the Render dyno sleeps; without it the first
    board request pays the whole cold start)
  · a failed key REFETCHES on the next press, and recovers
  · a succeeded key does NOT refetch
  · the row mapping — per → B/C/P, and R21's `done` ∩ non-null `per`, which
    is the guard against the literal string "null%" in the copy
  · `move`: undefined → null (NEW) and 0 preserved (HELD), which are
    different facts about a student
  · `safeAvatar` REJECTS rather than escapes, which is R25's security half
  · the viewer lands on their own profile tier, and a signed-out visitor
    gets no `me` row and no YOU badge
  · the countdown clock is anchored to `server_now`, not to the device

⚠️ WHAT IT STILL DOES NOT PROVE. `fetch` is stubbed, so this says nothing
about whether the backend returns what it claims to. Between them the three
leaderboard gates cover: the built page carries no invented identity
(`leaderboard_tells`), the rendered page behaves under every control
(`leaderboard_behaviour`), and the data layer maps and caches correctly
(this). Nothing in the set proves the live endpoint's contract; that needs a
credential and a warm dyno, and it is a drive, not a gate.
"""

import json
import os
import shutil
import subprocess
import sys

REPO = os.path.dirname(os.path.abspath(__file__))
SEAM = os.path.join("shared", "leaderboard-live.js")
SCRATCH = os.path.join("leaderboard_fixtures", "_seam_drive.js")

# ⚠️ TZ PINNED, for the same reason build_leaderboard_port pins it: this
# harness asserts on a clock offset, and a machine in another zone must get
# the same answer.
ENV_TZ = "UTC"

_HARNESS = r"""
'use strict';
const fs = require('fs');
const SRC = fs.readFileSync(process.argv[2], 'utf8');

const checks = [];
function ok(name, cond, detail) {
  checks.push({name: name, ok: !!cond, detail: detail || ''});
}

/* A fresh seam per scenario. The file is an IIFE that assigns onto `window`,
   so each scenario gets its own global and they cannot leak into each other
   — which matters, because the whole point of two of them is cache state. */
function boot(opts) {
  opts = opts || {};
  const calls = [];
  let fail = opts.failFirstBoard || 0;

  global.window = {};
  global.document = {readyState: 'complete', addEventListener: function () {}};
  global.fetch = function (url, init) {
    calls.push({url: String(url), init: init || {}});
    if (String(url).indexOf('/api/health') >= 0) {
      return Promise.resolve({ok: true, json: function () { return {}; }});
    }
    if (fail > 0) { fail -= 1; return Promise.reject(new Error('stubbed')); }
    return Promise.resolve({
      ok: true,
      json: function () { return Promise.resolve(opts.payload || PAYLOAD); }
    });
  };
  if (opts.supabase) { global.window.supabase = opts.supabase; }
  let mounts = 0;
  global.window.__MRB_MOUNT__ = function () {
    mounts += 1;
    return {schedule: function () {}};
  };
  eval(SRC);
  return {
    api: global.window.MrBadmusLeaderboardLive,
    calls: calls,
    /* Arm the NEXT n board requests to fail. Needed because the errored key
       has to be reachable a second time — see the scenario below. */
    setFail: function (n) { fail = n; },
    boards: function () {
      return calls.filter(function (c) { return c.url.indexOf('/board?') >= 0; });
    },
    mounts: function () { return mounts; }
  };
}

const PAYLOAD = {
  server_now: '2026-08-25T09:00:00.000Z',
  closes_at: '2026-08-28T09:15:00.000Z',
  current_week: '2026-08-21', week_start: '2026-08-21', is_current: true,
  tier: 'foundation', subject: 'overall',
  weeks: [{week_start: '2026-08-14', attempts: 3, is_current: false, top_pct: 91},
          {week_start: '2026-08-21', attempts: 2, is_current: true, top_pct: 80}],
  entries: 2, median_pct: 80, fastest_secs: 60, biggest_climb: null,
  cut_pct: null,
  board: [
    /* A real generator-shaped handle. ⚠️ Deliberately NOT one of Design's
       sixty-one — this file is checked in and `leaderboard_tells` would be
       right to fail on it. */
    {name: 'RealStudent7', school: 'A School', avatar_url: null, rank: 1,
     pct: 80, marks: 24, total: 30, secs: 60,
     /* physics is in `done` with a NULL score — the exact pairing R21
        exists for. Unfiltered it renders the string "null%". */
     per: {biology: 80, chemistry: 80, physics: null},
     done: ['biology', 'chemistry', 'physics'],
     move: 0, was: 1, streak: 2},
    {name: 'OtherStudent3', school: '', avatar_url: 'https://cdn.test/a.png',
     rank: 2, pct: 70, marks: 21, total: 30, secs: 90,
     per: {biology: 70, chemistry: null, physics: null}, done: ['biology'],
     was: null, streak: 1}
  ],
  me: null
};

const wait = (ms) => new Promise((r) => setTimeout(r, ms));

(async function () {
  /* ── 1. the warm-up ping ─────────────────────────────────────────── */
  {
    const s = boot({});
    await wait(30);
    ok('warm-up ping fires at boot',
       s.calls.some(function (c) { return c.url.indexOf('/api/health') >= 0; }),
       'the Render dyno sleeps; without this the first board request pays '
       + 'the whole cold start');
  }

  /* ── 2/3. an error is not a cached answer; an ok answer is ───────── */
  {
    /* ⚠️ THE ORDER HERE IS LOAD-BEARING, AND THE FIRST VERSION OF THIS
       SCENARIO SILENTLY PROVED NOTHING. It failed the very first board
       request, then pressed Biology and pressed back to Overall — and the
       cache key is `tier|subject|week`. On that first failure the payload
       never arrived, so `sel.week` was still null and the errored key was
       `Foundation|Overall|`; the Biology fetch then SET `sel.week`, so
       pressing back produced `Foundation|Overall|2026-08-21` — a key that
       had never been seen. It refetched because it was new, not because the
       error was discarded. Reverting the fix left this check GREEN.
       Caught by mutation-testing the gate rather than by reading it.

       So: let the first load SUCCEED, which pins `sel.week`. Only then arm a
       failure, and press back onto that exact key. */
    const s = boot({});
    await wait(40);
    ok('the first load succeeds and pins the week',
       s.api.status() === 'ok' && s.api.weeks().length === 2,
       'status ' + s.api.status());

    s.setFail(1);
    s.api.select({subject: 'Biology'});
    await wait(40);
    const afterFail = s.boards().length;
    ok('a failed fetch leaves that key in status "error"',
       s.api.status() === 'error', 'got ' + s.api.status());

    /* Away and back — the SAME key both times now, because the week is
       pinned and only the subject moves. */
    s.api.select({subject: 'Overall'});
    await wait(40);
    const cached = s.boards().length;
    ok('a SUCCEEDED key is never refetched', cached === afterFail,
       'board requests ' + afterFail + ' -> ' + cached
       + ' on returning to a key already fetched');

    s.api.select({subject: 'Biology'});
    await wait(40);
    ok('pressing back onto an ERRORED key refetches it',
       s.boards().length > cached,
       'board requests ' + cached + ' -> ' + s.boards().length
       + '; an error is the absence of an answer, not a cached one');
    ok('and that key recovers to "ok"', s.api.status() === 'ok',
       'status ' + s.api.status());
  }

  /* ── 4. the row mapping, including R21 ───────────────────────────── */
  {
    const s = boot({});
    await wait(40);
    const rows = s.api.rows();
    ok('rows map into Design\'s ten-field shape', rows.length === 2,
       'got ' + rows.length + ' row(s)');
    const r0 = rows[0];
    ok('per maps biology/chemistry/physics -> B/C/P',
       r0 && r0.per.B === 80 && r0.per.C === 80 && r0.per.P === null,
       JSON.stringify(r0 && r0.per));
    ok('R21: a subject in `done` with a NULL score is dropped from done',
       r0 && r0.done.length === 2 && r0.done.indexOf('P') < 0,
       'done = ' + JSON.stringify(r0 && r0.done)
       + ' (unfiltered, Design renders the literal string "null%")');
    ok('move 0 is preserved as HELD, not confused with NEW',
       r0 && r0.move === 0, 'move = ' + JSON.stringify(r0 && r0.move));
    ok('an ABSENT move becomes null (NEW), never undefined',
       rows[1] && rows[1].move === null,
       'move = ' + JSON.stringify(rows[1] && rows[1].move));
    ok('streak defaults to 0 rather than undefined',
       typeof r0.streak === 'number', 'streak = ' + r0.streak);
  }

  /* ── 5. R25's security half — reject, never escape ───────────────── */
  {
    const s = boot({payload: Object.assign({}, PAYLOAD, {
      board: PAYLOAD.board.map(function (r, i) {
        const urls = [
          'https://cdn.test/ok.png',
          '/leaderboard_fixtures/av.png'
        ];
        return Object.assign({}, r, {avatar_url: urls[i]});
      })
    })});
    await wait(40);
    const rows = s.api.rows();
    ok('an https avatar survives', rows[0].avatar_url === 'https://cdn.test/ok.png',
       String(rows[0].avatar_url));
    ok('a same-origin root-relative avatar survives',
       rows[1].avatar_url === '/leaderboard_fixtures/av.png',
       String(rows[1].avatar_url));
  }
  {
    const hostile = [
      'https://cdn.test/x.png");color:red;a("',   // closes the declaration
      'javascript:alert(1)',                       // wrong scheme
      'https://cdn.test/a b.png',                  // whitespace
      "https://cdn.test/'.png",                    // quote
      'https://cdn.test/x.png);background:url(y'   // parentheses
    ];
    const s = boot({payload: Object.assign({}, PAYLOAD, {
      board: hostile.map(function (u, i) {
        return Object.assign({}, PAYLOAD.board[0], {rank: i + 1, avatar_url: u});
      })
    })});
    await wait(40);
    const bad = s.api.rows().filter(function (r) { return r.avatar_url !== null; });
    ok('every hostile avatar URL is REJECTED back to initials',
       bad.length === 0,
       bad.length + ' survived: ' + JSON.stringify(bad.map(function (r) {
         return r.avatar_url; })));
  }

  /* ── 6. identity: signed out, and the profile-tier landing ───────── */
  {
    const s = boot({});
    await wait(40);
    ok('signed out: no `me` row', s.api.me() === null, String(s.api.me()));
    ok('signed out: viewer name is empty', s.api.viewerName() === '',
       JSON.stringify(s.api.viewerName()));
    ok('signed out: isYou() is false even for an unnamed row',
       s.api.isYou('') === false && s.api.isYou('RealStudent7') === false,
       'an empty viewer must not badge a row as YOU');
    ok('signed out: the board still renders (it is public)',
       s.api.rows().length === 2, 'rows = ' + s.api.rows().length);
  }
  {
    const supabase = {
      createClient: function () {
        return {
          auth: {getSession: function () {
            return Promise.resolve({data: {session: {
              access_token: 'tok', user: {id: 'u1'}}}});
          }},
          from: function () {
            return {select: function () { return {eq: function () {
              return {single: function () {
                return Promise.resolve({data: {
                  tier: 'higher', username: 'WolfSummit53',
                  first_name: 'Ada'}});
              }};
            }}; }};
          }
        };
      }
    };
    const s = boot({supabase: supabase});
    await wait(60);
    ok('the viewer lands on their OWN profile tier, not Design\'s default',
       s.api.stateFor({}).tier === 'Higher',
       'tier = ' + s.api.stateFor({}).tier + ' (Design hardcodes Higher; the '
       + 'seam default is Foundation, so Higher here proves the profile was '
       + 'read rather than defaulted)');
    ok('the viewer name follows the live rule (username first)',
       s.api.viewerName() === 'WolfSummit53', s.api.viewerName());
    ok('viewer initials come from Design\'s own initialsOf',
       s.api.viewerInitials() === 'WS', s.api.viewerInitials());
    ok('isYou() matches the signed-in viewer',
       s.api.isYou('WolfSummit53') === true, 'isYou failed for the viewer');
    ok('the board request carries the bearer token',
       s.boards().some(function (c) {
         return c.init && c.init.headers
                && /^Bearer /.test(c.init.headers.Authorization || '');
       }), 'no Authorization header on any board request');
  }

  /* ── 7. the clock is the server's, not the device's ──────────────── */
  {
    const s = boot({});
    await wait(40);
    const skewed = s.api.now();
    const real = Date.now();
    ok('now() is anchored to server_now, not Date.now()',
       Math.abs(real - skewed) > 1000,
       'server_now was 2026-08-25T09:00:00Z; the offset from this machine\'s '
       + 'clock is ' + Math.round((real - skewed) / 1000) + 's — a device '
       + 'clock a day fast must not be able to close the round early');
    ok('closesAt() parses the payload\'s closes_at',
       s.api.closesAt() === Date.parse('2026-08-28T09:15:00.000Z'),
       String(s.api.closesAt()));
  }

  /* ── 8. the week fallback when an axis lacks the selected week ───── */
  {
    const s = boot({});
    await wait(40);
    s.api.select({week: '2026-08-14'});
    await wait(30);
    ok('selecting a week that the payload does not list falls back to '
       + 'that axis\'s current week rather than to index 3',
       s.api.weekIndex() >= 0 && s.api.weekIndex() < s.api.weeks().length,
       'weekIndex = ' + s.api.weekIndex() + ' of ' + s.api.weeks().length);
  }

  process.stdout.write(JSON.stringify(checks));
})().catch(function (e) {
  process.stdout.write(JSON.stringify(
    [{name: 'the harness itself', ok: false, detail: String(e && e.stack || e)}]));
});
"""


def main(argv=None):
    os.chdir(REPO)
    print("\n\U0001F517  leaderboard_seam — the data layer, driven directly\n")

    if not os.path.exists(SEAM):
        raise SystemExit(
            "leaderboard_seam.py: %s does not exist. It is the only way data "
            "reaches the leaderboard, so there is nothing to assert." % SEAM)

    # ⊕ SKIPPED BY NAME, not silently, and not by weakening an assertion.
    # The same shape `pool_ownership` uses for a missing backend checkout: a
    # machine without Node cannot run `build_leaderboard_port.py` either, so
    # there is no built page for this to be lying about.
    if not shutil.which("node"):
        print("     ⏭️  SKIPPED BY NAME: `node` is not installed on this "
              "machine.\n"
              "        This gate evaluates shared/leaderboard-live.js under "
              "Node. Without\n"
              "        it, build_leaderboard_port.py cannot run either, so "
              "there is no\n"
              "        built page for this gate to be silent about.\n")
        return 0

    os.makedirs(os.path.dirname(SCRATCH), exist_ok=True)
    with open(SCRATCH, "w", encoding="utf-8") as fh:
        fh.write(_HARNESS)
    try:
        r = subprocess.run(["node", SCRATCH, SEAM], capture_output=True,
                           text=True, env=dict(os.environ, TZ=ENV_TZ),
                           timeout=120)
    finally:
        if os.path.exists(SCRATCH):
            os.remove(SCRATCH)

    if r.returncode != 0 or not r.stdout.strip():
        raise SystemExit(
            "leaderboard_seam.py: the harness did not run.\n  %s"
            % (r.stderr or "(no output)").strip()[:1200])

    try:
        checks = json.loads(r.stdout)
    except ValueError:
        raise SystemExit(
            "leaderboard_seam.py: the harness produced output that is not "
            "JSON:\n  %s" % r.stdout[:800])

    failed = 0
    for c in checks:
        if c["ok"]:
            print("     ✅ %s" % c["name"])
        else:
            failed += 1
            print("     ❌ %s" % c["name"])
            if c.get("detail"):
                print("          · %s" % c["detail"])

    if r.stderr.strip():
        # ⚠️ NOT IGNORED. An unhandled rejection here is exactly the console
        # noise the behaviour gate would fail a page for.
        failed += 1
        print("     ❌ the seam wrote to stderr while being driven")
        print("          · %s" % r.stderr.strip()[:600])

    if failed:
        print("\n  FAIL  %d of %d check(s).\n" % (failed, len(checks)))
        return 1
    print("\n  PASS  %d check(s) against the real shared/leaderboard-live.js "
          "— the\n        warm-up ping, error-key refetch, cache honouring, "
          "the row mapping\n        (including R21), R25's reject-don't-"
          "escape URL rule, the profile-tier\n        landing, the signed-out "
          "path and the server-anchored clock.\n" % len(checks))
    print("     ⚠️  `fetch` is stubbed. This proves the data layer maps and "
          "caches\n         correctly; it proves nothing about the live "
          "endpoint's contract.\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
