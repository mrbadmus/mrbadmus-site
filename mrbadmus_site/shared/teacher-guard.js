/**
 * shared/teacher-guard.js — Reusable role gate for /teacher/* pages
 *
 * Page contract:
 *   <script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2/dist/umd/supabase.min.js"></script>
 *   <script src="/shared/config.js"></script>
 *   <script src="/shared/teacher-guard.js"></script>
 *   <script>
 *     MrBadmusTeacherGuard.requireTeacherRole({
 *       onAllowed: ({ user, profile }) => {
 *         // page-specific render code, e.g. document.body.style.display = 'block'
 *       },
 *     });
 *   </script>
 *
 *   To sign out from any /teacher/* page:
 *     <button onclick="MrBadmusTeacherGuard.signOut()">Sign out</button>
 *
 * Behaviour:
 *   - No active session  → redirect to /auth.html?return=<current-path>
 *   - Session valid but role not in (teacher, hod, admin) → redirect to /index.html
 *   - Session valid and role allowed → call onAllowed({ user, profile })
 *
 * The guard reads SUPABASE_URL/SUPABASE_ANON_KEY from window.MrBadmusConfig
 * (set by /shared/config.js), so it follows the prod/test environment switch.
 *
 * NOTE — Defence in depth: this is the FRONTEND guard. It improves UX (right
 * page for the right user) but is NOT the security boundary. The backend
 * (server.js requireTeacherRole) and database (RLS policies) are the real
 * gates. Anyone bypassing this script in the browser still hits 401/403 from
 * the backend and zero rows from RLS.
 */

window.MrBadmusTeacherGuard = (function () {
  // Roles allowed to reach /teacher/*. Mirror this list in server.js's
  // requireTeacherRole — both must agree or the layers contradict each other.
  const ALLOWED_ROLES = ['teacher', 'hod', 'admin'];

  // Lazy-init shared client so requireTeacherRole and signOut talk to the
  // same Supabase project (whichever MrBadmusConfig pointed at). Logs a
  // loud error if config or SDK is missing; callers decide what to do
  // with the null return.
  let _client = null;
  function getClient() {
    if (_client) return _client;
    if (!window.MrBadmusConfig) {
      console.error('[teacher-guard] window.MrBadmusConfig missing');
      return null;
    }
    if (!window.supabase || !window.supabase.createClient) {
      console.error('[teacher-guard] Supabase SDK not loaded');
      return null;
    }
    const { SUPABASE_URL, SUPABASE_ANON_KEY } = window.MrBadmusConfig;
    _client = window.supabase.createClient(SUPABASE_URL, SUPABASE_ANON_KEY);
    return _client;
  }

  function bounceToLogin() {
    const here = window.location.pathname + window.location.search;
    window.location.replace('/auth.html?return=' + encodeURIComponent(here));
  }

  function bounceToHome() {
    window.location.replace('/index.html');
  }

  async function requireTeacherRole(opts) {
    opts = opts || {};
    const onAllowed = opts.onAllowed || function () {};
    const onDenied = opts.onDenied || null; // null = use default redirect logic

    const sb = getClient();
    if (!sb) {
      // getClient already console.error'd what was wrong. Fail-closed bounce.
      bounceToLogin();
      return;
    }

    // 1. Session check — getUser() actually validates the JWT with Supabase
    // (round-trip), unlike getSession() which just reads localStorage. This
    // file is layer 2 of defence-in-depth (UX gate); the real security gates
    // are the backend's requireTeacherRole and the database's RLS policies.
    const { data: { user }, error: userError } = await sb.auth.getUser();
    if (userError || !user) {
      if (onDenied) return onDenied({ reason: 'no_session', error: userError });
      return bounceToLogin();
    }

    // 2. Role check.
    const { data: profile, error } = await sb
      .from('profiles')
      .select('first_name, role, school_id')
      .eq('id', user.id)
      .single();

    if (error || !profile) {
      console.error('[teacher-guard] profile lookup failed for session user — bouncing to home', error);
      if (onDenied) return onDenied({ reason: 'profile_lookup_failed', error });
      return bounceToHome();
    }

    if (!ALLOWED_ROLES.includes(profile.role)) {
      if (onDenied) return onDenied({ reason: 'wrong_role', role: profile.role });
      return bounceToHome();
    }

    // 3. Allowed — let the page render with the data we already have.
    onAllowed({ user, profile });
  }

  // Sign the user out and send them to the login page.
  // Idempotent in spirit: even if the signOut call fails (network error,
  // missing client), the redirect always happens — so the user is never
  // stranded on a protected page.
  async function signOut() {
    const sb = getClient();
    if (sb) {
      try {
        await sb.auth.signOut();
      } catch (e) {
        console.error('[teacher-guard] signOut error', e);
      }
    }
    window.location.replace('/auth.html');
  }

  return { requireTeacherRole, signOut, ALLOWED_ROLES };
})();
