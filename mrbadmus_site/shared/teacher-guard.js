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

    /* ⊕ 27 Aug 2026 — THE TWO READS NOW GO TOGETHER, and the gate is not
       weakened by it.

       They used to be strictly serial: validate the JWT, THEN ask for the
       profile. Two round trips one after the other, and on a cold Supabase
       connection the first of them was the one the whole page queued behind —
       measured at 2.9 seconds on the teacher landing, with the queries
       themselves taking 3–17ms.

       The second read never needed the FIRST READ'S ANSWER. It needs a user
       id, and it needs the client's token — and the token is the persisted
       session, which is attached to every PostgREST request by the client
       itself whether or not `getUser()` has come back. So the profile read is
       started against the STORED session's user id, in parallel, and then:

         · if `getUser()` says no session, we bounce exactly as before and the
           prefetched row is dropped unread;
         · if `getUser()` returns a DIFFERENT user than the one the prefetch
           was keyed on — a session swapped mid-flight, a refresh landing on
           another account — the prefetch is discarded and the real query runs.
           Never reconciled, never trusted: a profile fetched for the wrong id
           is thrown away.

       ⚠️ THIS IS NOT THE SECURITY GATE AND MUST NOT BE MISREAD AS ONE. The
       row comes back through RLS under the viewer's own token, so a viewer
       cannot prefetch somebody else's profile in the first place; the real
       gates are the backend and the database's policies, as the header says.
       What changes here is only WHEN the request leaves, never who may read
       what.

       `getSession()` is a localStorage read, not a round trip (it refreshes
       only an expired token, which the request after it would have had to wait
       for anyway). */
    let prefetchId = null;
    let prefetched = null;
    try {
      const stored = await sb.auth.getSession();
      const storedUser = stored && stored.data && stored.data.session
        ? stored.data.session.user : null;
      if (storedUser && storedUser.id) {
        prefetchId = storedUser.id;
        // `.then()` FORCES IT TO LEAVE NOW. A PostgREST builder is lazy — it
        // is a thenable that fires on await — so holding the builder in a
        // local would run it serially after `getUser()` and change nothing.
        /* ⊕ MRB-306 — `display_name` and `last_name` join the select.
           Today greets a teacher by the name STUDENTS see, and the guard's
           profile read is the one this page already waits on — a second
           read for one column would be a serial wave for nothing.
           ⚠️ THE TWO SELECTS IN THIS FILE MUST STAY IDENTICAL. They are the
           prefetch and its fallback for the same row; a column present in
           one and absent from the other would make a page's greeting depend
           on whether a stored session happened to be warm. */
        prefetched = sb
          .from('profiles')
          .select('first_name, last_name, display_name, role, school_id')
          .eq('id', prefetchId)
          .single()
          .then(function (r) { return r; },
                function (e) { return { data: null, error: e }; });
      }
    } catch (e) {
      prefetchId = null;
      prefetched = null;
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

    // 2. Role check — the row we already asked for, but ONLY if it was asked
    // for about this same person. Otherwise ask again, properly.
    const { data: profile, error } = (prefetched && prefetchId === user.id)
      ? await prefetched
      : await sb
          .from('profiles')
          .select('first_name, last_name, display_name, role, school_id')
          .eq('id', user.id)
          .single();

    if (error && error.code !== 'PGRST116') {
      // A real query failure (network blip, RLS timeout) is NOT a denial —
      // don't treat a legitimate teacher as "not a teacher". Bounce to login so
      // a re-auth lands them back here (return path preserved). PGRST116 is
      // Supabase's "no rows" code, handled as a genuine no-profile below.
      console.error('[teacher-guard] profile lookup errored — bouncing to login', error);
      if (onDenied) return onDenied({ reason: 'profile_lookup_failed', error });
      return bounceToLogin();
    }
    if (!profile) {
      console.error('[teacher-guard] no profile row for session user — bouncing to home', error);
      if (onDenied) return onDenied({ reason: 'no_profile', error });
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
    // Preserve the test environment across sign-out so a tester doesn't get
    // silently dropped onto the production auth page.
    const isTest = window.MrBadmusConfig && window.MrBadmusConfig.environment === 'test';
    window.location.replace('/auth.html' + (isTest ? '?env=test' : ''));
  }

  return { requireTeacherRole, signOut, getClient, ALLOWED_ROLES };
})();
