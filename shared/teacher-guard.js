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

  /* ── ⊕ MRB-328 J4(b) · THE SESSION, RESOLVED ONCE PER BURST ────────────

     `getUser()` below is a genuine round trip to Supabase auth, and it sits in
     front of EVERYTHING: no page on this surface reads a row, draws a header
     or starts a skeleton until it has come back. A teacher walking Today →
     class → marking → a student pays it four times in ninety seconds, for four
     identical answers about an identity that did not change.

     So the resolved answer — the user and the profile row, which is to say the
     ROLE — is held in `sessionStorage` for two minutes and, on a hit, the page
     is allowed to render IMMEDIATELY while the real check runs behind the
     paint. If the background check disagrees, the page bounces exactly as it
     would have done, one paint later.

     ── Why two minutes, and not thirty like the class entry ───────────────
     The class entry caches "which class page to link to", which changes when a
     teacher enrols somebody. This caches WHETHER YOU MAY BE HERE. The two are
     not comparable and the second wants the shortest TTL that still spans a
     burst of navigation — which is what a teacher does between lessons, and
     what the four measured journeys are. Two minutes covers the burst and
     expires long before anybody could sit on a revoked role.

     ── Why this is not a hole ─────────────────────────────────────────────
     ⚠️ IT NEVER WIDENS WHAT MAY BE READ, only when the page starts drawing.

       1. THIS FILE HAS NEVER BEEN THE SECURITY GATE and says so twice in its
          own header: "layer 2 of defence-in-depth (UX gate); the real security
          gates are the backend's requireTeacherRole and the database's RLS
          policies." Every row the page then fetches is fetched under the
          viewer's own JWT and filtered by RLS. A cached `role: 'teacher'`
          buys a non-teacher nothing at all — the reads still come back empty.
       2. THE CACHED ANSWER IS KEYED ON THE VIEWER'S OWN ID, via
          `MRBClassEntry.cacheKey`, and on the environment. A second person
          signing into the same tab gets a different key and therefore a miss.
       3. THE STORED TOKEN IS STILL CHECKED FOR EXPIRY before the cache is
          consulted at all. An expired session takes the full path, so the
          bounce-to-login a teacher would have got is the bounce they get.
       4. IT IS `sessionStorage`, so it dies with the tab. A shared staffroom
          machine cannot carry it into the next person's browsing session even
          for the two minutes.
       5. SIGN-OUT DROPS IT — see `signOut()` below.

     ⚠️ AND THE REVALIDATION IS NOT OPTIONAL. If it were skipped on a hit, a
     teacher whose role was removed would keep a working-looking dashboard for
     the life of the tab. It runs on EVERY cached load, and its denial path is
     the same `onDenied`/bounce the cold path uses. */
  const SESSION_PREFIX = 'mrb-staff-session:';
  const SESSION_TTL_MS = 2 * 60 * 1000;

  function sessionCacheKey() {
    const ce = window.MRBClassEntry;
    if (!ce || !ce.cacheKey) { return null; }   // module absent → no cache
    try { return ce.cacheKey(SESSION_PREFIX); } catch (e) { return null; }
  }

  function cachedResolution() {
    const ce = window.MRBClassEntry;
    const key = sessionCacheKey();
    if (!key || !ce.cacheGet) { return null; }
    try {
      const hit = ce.cacheGet(key, SESSION_TTL_MS);
      if (!hit || !hit.user || !hit.user.id || !hit.profile) { return null; }
      if (!ALLOWED_ROLES.includes(hit.profile.role)) { return null; }
      return hit;
    } catch (e) { return null; }
  }

  function rememberResolution(user, profile) {
    const ce = window.MRBClassEntry;
    const key = sessionCacheKey();
    if (!key || !ce || !ce.cacheSet) { return; }
    try {
      // The id and the profile columns, and nothing else. `user` from the SDK
      // carries the whole identity payload — app_metadata, the provider token
      // envelope, every recovery timestamp — and none of it is read by any
      // caller of `onAllowed`, so none of it is stored.
      ce.cacheSet(key, {
        user: { id: user.id, email: user.email || null },
        profile: {
          first_name: profile.first_name || null,
          last_name: profile.last_name || null,
          display_name: profile.display_name || null,
          role: profile.role,
          school_id: profile.school_id || null
        }
      });
    } catch (e) {}
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
    let storedSession = null;
    try {
      const stored = await sb.auth.getSession();
      storedSession = stored && stored.data ? stored.data.session : null;
      const storedUser = storedSession ? storedSession.user : null;
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
      storedSession = null;
    }

    /* ⊕ MRB-328 J4(b) — THE OPTIMISTIC RENDER, and then the real check.

       Everything below this block still runs, in the order it always ran and
       with the same effect. What changes is only that on a cache hit the page
       is handed its context NOW rather than one round trip from now, and the
       round trip becomes a correction rather than a wait.

       ⚠️ THE EXPIRY TEST IS NOT DECORATION. Without it a tab left open over
       lunch would render its dashboard off a two-minute-old cache against a
       token Supabase has already stopped accepting — a page that looks signed
       in and whose every read comes back 401, which is strictly worse than
       the login bounce it replaced. An expired or missing token takes the
       cold path, which is where that bounce lives. */
    let served = false;
    const expMs = storedSession && storedSession.expires_at
      ? storedSession.expires_at * 1000 : 0;
    if (storedSession && prefetchId && (!expMs || expMs > Date.now())) {
      const hit = cachedResolution();
      if (hit && hit.user.id === prefetchId) {
        served = true;
        try {
          onAllowed({ user: hit.user, profile: hit.profile });
        } catch (e) {
          // A throw out of the page's own render must not take the
          // revalidation below down with it — the check still has to happen.
          console.error('[teacher-guard] onAllowed threw on the cached path', e);
        }
      }
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

    /* 3. Allowed — let the page render with the data we already have.

       ⊕ MRB-328 J4(b) — …unless it already did. On a cached load this whole
       function has been the REVALIDATION, and reaching here means it agreed:
       the page is drawn, the answer is unchanged, and there is nothing to do
       but refresh the stamp so the next navigation is cheap too. Calling
       `onAllowed` a second time would boot the runtime twice over its own
       mounted DOM. Every DENIAL above is unguarded on purpose — a correction
       must fire whether or not the page has already drawn. */
    rememberResolution(user, profile);
    if (served) { return; }
    onAllowed({ user, profile });
  }

  // Sign the user out and send them to the login page.
  // Idempotent in spirit: even if the signOut call fails (network error,
  // missing client), the redirect always happens — so the user is never
  // stranded on a protected page.
  async function signOut() {
    /* ⊕ MRB-328 J4(b) — THE CACHES GO FIRST, before the network call that may
       fail and before the redirect that ends this script.

       Order is the whole of it. Dropped after `sb.auth.signOut()`, a network
       failure there would skip the drop and leave the previous teacher's
       session, role and class list in `sessionStorage` — where the next
       person to sign in on that tab would find them still inside their TTL.
       Dropped after the redirect, it would never run at all.

       `dropCaches` sweeps by FAMILY rather than by exact key, because by the
       time this is called the id those keys are built from may already be
       gone. See `shared/class-entry.js`. */
    try {
      const ce = window.MRBClassEntry;
      if (ce && ce.dropCaches) { ce.dropCaches(); }
    } catch (e) { /* a cache that will not clear must not strand a sign-out */ }

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
