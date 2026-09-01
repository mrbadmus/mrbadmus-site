/**
 * shared/config.js — Environment configuration switcher
 *
 * Decides which Supabase project + Render backend the frontend talks to.
 *
 * Defaults to PRODUCTION. Switches to the TEST project + local backend when:
 *   - the URL has the query parameter ?env=test, OR
 *   - hostname is "localhost" or "127.0.0.1" AND the URL does NOT have ?env=prod
 *
 * Query string wins over hostname. ?env=prod lets a developer on localhost
 * deliberately hit production for debugging real user issues.
 *
 * Mental model: test = a complete parallel universe (test DB + test backend +
 * test JWTs all match each other). Never mix prod and test in the same flow —
 * a JWT issued by the test project cannot be validated by the prod backend
 * and vice versa.
 *
 * ── Trade-off acknowledged (MRB-19 D1) ──────────────────────────────────
 * The test anon key is hardcoded below alongside the prod one. Anyone with
 * this file's source can hit the test Supabase project. That's acceptable:
 *   - Anon keys are designed to be public — RLS still enforces row-level access
 *   - The test project contains only fake seed data (Sarah Whitfield + 7
 *     fake students attached to a fake school), no real student PII
 *   - The test project is NEVER a path to read or write production data
 *
 * ── Usage ────────────────────────────────────────────────────────────────
 * Pages load this BEFORE any Supabase or backend code:
 *   <script src="/shared/config.js"></script>
 *   <script>
 *     const { SUPABASE_URL, SUPABASE_ANON_KEY, BACKEND_URL } = window.MrBadmusConfig;
 *   </script>
 *
 * Existing pages keep their inline-hardcoded constants for now — only the
 * NEW /teacher/* pages added in Stage 2A use this config. Migrating existing
 * pages is out of scope for MRB-19.
 */

(function () {
  // ── PRODUCTION (live site at mrbadmus.com) ─────────────────────────────
  const PROD = {
    SUPABASE_URL:      'https://urklkrwevjtlfbwnipjn.supabase.co',
    SUPABASE_ANON_KEY: 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVya2xrcndldmp0bGZid25pcGpuIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzQxOTQyNzksImV4cCI6MjA4OTc3MDI3OX0.pW9AP6TPlKC_XHDTbrEKrEGmGXglN0z5b0KGXD2oHvg',
    BACKEND_URL:       'https://mrbadmus-backend.onrender.com',
    // See the CONSUMER_SIGNUP_ENABLED note below. Off here, deliberately.
    CONSUMER_SIGNUP_ENABLED: false,
  };

  // ── TEST (local dev / Stage 2A sandbox) ────────────────────────────────
  const TEST = {
    SUPABASE_URL:      'https://qeppkiswvclkkwbxmlok.supabase.co',
    SUPABASE_ANON_KEY: 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFlcHBraXN3dmNsa2t3YnhtbG9rIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Nzc2NjMzMzMsImV4cCI6MjA5MzIzOTMzM30.WxprirdO3yIZfcOiUMwbVPFPcD6Sx5SIZrQ3pvMOKT8',
    BACKEND_URL:       'http://localhost:3000',
    // Off here TOO. See the note below — "test" is not a reason to be on.
    CONSUMER_SIGNUP_ENABLED: false,
  };

  /* ── CONSUMER_SIGNUP_ENABLED — MRB-308, the B2C launch ─────────────────
   *
   * OFF by default in BOTH environments above, and that is the point: this
   * is a launch switch, not an environment switch. A developer on localhost
   * should not silently get a half-built consumer product just because they
   * are on localhost, and neither should a tester on ?env=test.
   *
   * ⚠️ IT IS ONE OF THREE, AND ALL THREE MUST BE ON. Consumer surfaces only
   * work when every switch agrees:
   *
   *   1. this flag                    — the FRONTEND half. Decides whether
   *                                     /consumer/* renders at all. A page
   *                                     with this off renders "Not found"
   *                                     and makes no network call.
   *   2. the backend env var
   *      CONSUMER_SIGNUP_ENABLED      — decides whether /api/consumer/*
   *                                     answers or 404s.
   *   3. the `platform_flags` DB row  — decides whether the data layer will
   *                                     accept a consumer org at all.
   *
   * Turning on ONLY this one gets you a full parent signup page whose every
   * button fails against a backend that does not answer. Turning on only the
   * backend gets you an API nobody can reach. The three are deliberately
   * separate so that a launch is a decision taken three times, in three
   * places, by someone who meant it — and so that ANY ONE of them, flipped
   * back, closes the whole product instantly without a deploy of the others.
   *
   * A page must treat this as fail-closed: absent, undefined or anything
   * other than exactly `true` means OFF.
   * ─────────────────────────────────────────────────────────────────────── */

  // ── Environment detection ──────────────────────────────────────────────
  // Query string wins; hostname is the fallback. ?env=prod on localhost
  // forces production (useful for debugging a real user issue locally).
  const host = window.location.hostname;
  const queryEnv = new URLSearchParams(window.location.search).get('env');
  const isLocalHost = host === 'localhost' || host === '127.0.0.1';
  const useTest =
    queryEnv === 'test' ||
    (isLocalHost && queryEnv !== 'prod');

  const config = useTest ? TEST : PROD;
  config.environment = useTest ? 'test' : 'prod';

  /* ── ?api= — a LOCALHOST-ONLY backend override (MRB-308) ───────────────
   *
   * Two backends now run on this machine at the same time. `main`'s backend
   * owns port 3000, which is what TEST.BACKEND_URL points at and must keep
   * pointing at; the b2c worktree's backend runs on 3100 so that both can be
   * up together and neither developer has to stop the other's server to test
   * their own. Rather than editing the shared default back and forth — an
   * edit that WILL eventually be committed by accident and point every
   * tester at a port that isn't running — the worktree passes its own URL in
   * the query string:
   *
   *     http://localhost:8000/consumer/signup.html?api=http://localhost:3100
   *
   * ⚠️ GUARDED ON isLocalHost, and that guard is the whole safety argument.
   * Without it this is an open redirect for API traffic: a link with
   * `?api=https://evil.example` sent to a signed-in student would point
   * their browser's authenticated backend calls — JWT and all — at someone
   * else's server. On a real hostname the parameter is read and then
   * ignored, so no link can ever redirect a real student's browser.
   *
   * Deliberately NOT folded into the useTest decision above: this changes
   * the backend URL only. Supabase project, anon key and environment label
   * are untouched, so `?env=test&api=…` still means "the test universe, but
   * served by the backend I am currently editing".
   * ─────────────────────────────────────────────────────────────────────── */
  const apiOverride = new URLSearchParams(window.location.search).get('api');
  if (apiOverride && isLocalHost) config.BACKEND_URL = apiOverride;

  window.MrBadmusConfig = config;

  // Loud signal in DevTools so it's obvious which environment is active.
  if (useTest) {
    // eslint-disable-next-line no-console
    console.log('[MrBadmus] config: TEST environment (sandbox)');
  }

  // Same reason: an overridden backend must never be a silent condition.
  // "It works on my machine but not on the other one" is exactly what an
  // unannounced port swap looks like from the outside.
  if (apiOverride && isLocalHost) {
    // eslint-disable-next-line no-console
    console.log('[MrBadmus] config: backend overridden by ?api= → ' + config.BACKEND_URL);
  } else if (apiOverride) {
    // eslint-disable-next-line no-console
    console.warn(
      '[MrBadmus] ?api= was IGNORED: the backend override is localhost-only. ' +
      'This page is talking to ' + config.BACKEND_URL + '.'
    );
  }

  // Test mode on a non-localhost URL is suspicious — typically a stale
  // bookmark with ?env=test on the live site. Promote to a warning so it
  // shows up loudly in DevTools without breaking the page.
  if (useTest && !isLocalHost) {
    // eslint-disable-next-line no-console
    console.warn(
      '[MrBadmus] WARNING: this page is using the TEST environment ' +
      'but loaded from a non-localhost URL. If you are a student and ' +
      'see this, remove `?env=test` from the URL.'
    );
  }
})();
