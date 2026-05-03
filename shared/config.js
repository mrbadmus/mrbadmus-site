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
  };

  // ── TEST (local dev / Stage 2A sandbox) ────────────────────────────────
  const TEST = {
    SUPABASE_URL:      'https://qeppkiswvclkkwbxmlok.supabase.co',
    SUPABASE_ANON_KEY: 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFlcHBraXN3dmNsa2t3YnhtbG9rIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Nzc2NjMzMzMsImV4cCI6MjA5MzIzOTMzM30.WxprirdO3yIZfcOiUMwbVPFPcD6Sx5SIZrQ3pvMOKT8',
    BACKEND_URL:       'http://localhost:3000',
  };

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

  window.MrBadmusConfig = config;

  // Loud signal in DevTools so it's obvious which environment is active.
  if (useTest) {
    // eslint-disable-next-line no-console
    console.log('[MrBadmus] config: TEST environment (sandbox)');
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
