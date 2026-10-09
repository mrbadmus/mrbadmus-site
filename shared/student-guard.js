/**
 * shared/student-guard.js — Reusable role gate for /student/* pages
 *
 * Parallels shared/teacher-guard.js exactly in shape; the differences
 * are role allowlist + bounce target. Built as a separate module for
 * MRB-46 Phase 3 (the first student-side route) so the teacher path
 * stays untouched and the student-mode mental model is its own thing.
 *
 * Page contract:
 *   <script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2/dist/umd/supabase.min.js"></script>
 *   <script src="/shared/config.js"></script>
 *   <script src="/shared/student-guard.js"></script>
 *   <script>
 *     MrBadmusStudentGuard.requireStudentRole({
 *       onAllowed: ({ user, profile }) => {
 *         // page-specific render code
 *       },
 *     });
 *   </script>
 *
 *   To sign out from any /student/* page:
 *     <button onclick="MrBadmusStudentGuard.signOut()">Sign out</button>
 *
 * Behaviour:
 *   - No active session   → redirect to /auth.html?return=<current-path>
 *   - Session valid, role !== 'student' → redirect to /index.html
 *     (rationale: no "logged in but wrong role for this page" surface
 *      exists yet; landing is the safe default. A teacher who accidentally
 *      lands on a /student/* URL goes home rather than seeing an awkward
 *      error. Revisit when a dedicated wrong-role page appears.)
 *   - Session valid + role === 'student' → call onAllowed({ user, profile })
 *
 * NOT IN SCOPE here: class-membership check. That's a per-page concern
 * (the page knows which class it's rendering and calls the data layer,
 * which surfaces RLS denial as a notAuthorised state). This guard only
 * gates "is the viewer a student at all" — not "is this student in this
 * specific class."
 *
 * Reads SUPABASE_URL/SUPABASE_ANON_KEY from window.MrBadmusConfig so
 * the prod/test environment switch works the same way as teacher-guard.
 *
 * Defence in depth: this is the FRONTEND guard. It improves UX (right
 * page for the right user). The real security gates are the backend
 * (if/when a student endpoint exists) and the database (RLS policies).
 * Anyone bypassing this script still hits zero rows from RLS.
 */

window.MrBadmusStudentGuard = (function () {
  // Only students see student pages. Teachers/HoDs/admins have their own
  // /teacher/* views (and would get confusing data shapes here anyway —
  // a teacher's "stats in this class" doesn't make sense).
  const ALLOWED_ROLES = ['student'];

  // Lazy-init shared client. Mirrors teacher-guard's pattern so a student
  // page calling MrBadmusStudentGuard.getClient() gets a Supabase client
  // configured for the same env as window.MrBadmusConfig.
  let _client = null;
  function getClient() {
    if (_client) return _client;
    if (!window.MrBadmusConfig) {
      console.error('[student-guard] window.MrBadmusConfig missing');
      return null;
    }
    if (!window.supabase || !window.supabase.createClient) {
      console.error('[student-guard] Supabase SDK not loaded');
      return null;
    }
    const { SUPABASE_URL, SUPABASE_ANON_KEY } = window.MrBadmusConfig;
    _client = window.supabase.createClient(SUPABASE_URL, SUPABASE_ANON_KEY);
    return _client;
  }

  /* ⊕ B2C polish (9 Oct 2026) — the sign-in page opens in the SAME world.
     `env`/`api` used to travel only inside `?return=`, so auth.html itself
     loaded on production config from a TEST page. Carried onto the
     auth.html URL too; on the live site the URL has neither and this is
     exactly the old redirect. */
  function carryEnvQuery() {
    const here = new URLSearchParams(window.location.search);
    let out = '';
    ['env', 'api'].forEach(function (k) {
      const v = here.get(k);
      if (v) out += '&' + k + '=' + encodeURIComponent(v);
    });
    return out;
  }

  function bounceToLogin() {
    const here = window.location.pathname + window.location.search;
    window.location.replace('/auth.html?return=' + encodeURIComponent(here) + carryEnvQuery());
  }

  function bounceToHome() {
    window.location.replace('/index.html');
  }

  /* ── the resolved session, remembered ────────────────────────────────
     ⊕ MRB-348 round 4 — THE STUDENT PAGE GETS WHAT THE TEACHER PAGES HAVE.

     `sb.auth.getUser()` below is a real round trip — it validates the JWT with
     Supabase, unlike `getSession()`, which only reads localStorage. Everything
     the class page does waits behind it.

     `teacher-guard.js` stopped waiting for it in MRB-328 J4(b): on a cache hit
     it hands the page its context immediately and lets the round trip become a
     correction rather than a wait. The student guard never got the same
     treatment, and production RUM for the five days to 23 Sep 2026 shows what
     that costs — `student-class` p50 2,337 ms against `teacher-classes` 814 ms,
     on pages doing comparable work.

     This is that change, copied deliberately rather than reinvented, and every
     safety property `teacher-guard.js` argues for its own cache holds here
     unchanged:

       1. THIS IS NOT THE SECURITY BOUNDARY. It is layer 2, a UX gate. Every
          row the page then reads is read under the viewer's own JWT and
          filtered by RLS, so a cached `role: 'student'` buys a non-student
          nothing — the reads still come back empty.
       2. THE KEY CARRIES THE VIEWER'S ID AND THE ENVIRONMENT, via
          `MRBClassEntry.cacheKey`, so a second child signing into the same tab
          gets a different key and therefore a miss.
       3. THE STORED TOKEN'S EXPIRY IS CHECKED BEFORE THE CACHE IS CONSULTED.
          Without it a tab left open over lunch would draw a class page off a
          two-minute-old cache against a token Supabase has stopped accepting —
          a page that looks signed in and whose every read returns 401, which
          is strictly worse than the login bounce it replaced.
       4. IT IS `sessionStorage`, so it dies with the tab — and a classroom
          machine is precisely where that matters.
       5. SIGN-OUT DROPS IT — `mrb-student-session:` is in `CACHE_FAMILIES`,
          and `signOut()` below already calls `dropCaches()` before anything
          that can fail.

     ⚠️ AND THE REVALIDATION IS NOT OPTIONAL. If it were skipped on a hit, a
     child whose account was disabled would keep a working-looking class page
     for the life of the tab. It runs on EVERY cached load, and every denial
     below is unguarded on purpose so a correction fires whether or not the
     page has already drawn. */
  const SESSION_PREFIX = 'mrb-student-session:';
  /* ⊕ MRB-348 round 5 — THIRTY MINUTES, NOT THE TEACHER GUARD'S TWO, measured.
     Production RUM: p50 page time is 522 ms when the site was idle under 10 s
     and 3,864 ms after 5–30 minutes idle. A two-minute cache has expired by
     then, so it only ever helped the loads that were already fast. The TTL is
     not what keeps this safe — the revalidation on every load, RLS on every
     row, and the token-expiry test above are — so lengthening it moves no
     safety line; it only lets the cache reach the loads that are slow. */
  const SESSION_TTL_MS = 30 * 60 * 1000;

  function sessionCacheKey() {
    const ce = window.MRBClassEntry;
    if (!ce || !ce.cacheKey) { return null; }   // module absent → no cache
    try { return ce.cacheKey(SESSION_PREFIX); } catch (e) { return null; }
  }

  function cachedResolution() {
    const ce = window.MRBClassEntry;
    const key = sessionCacheKey();
    if (!key || !ce || !ce.cacheGet) { return null; }
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
      /* The id and the profile columns `onAllowed` is handed, and nothing
         else. `user` from the SDK carries the whole identity payload — no
         caller reads it, so none of it is stored. */
      ce.cacheSet(key, {
        user: { id: user.id, email: user.email || null },
        profile: {
          first_name: profile.first_name || null,
          last_name: profile.last_name || null,
          role: profile.role,
          school_id: profile.school_id || null,
          avatar_url: profile.avatar_url || null
        }
      });
    } catch (e) {}
  }

  /* ⊕ B2C unit 6 (5 Oct 2026) — A FAMILY CHILD NEVER LANDS ON THE SCHOOL
     CLASS PAGE. A family (or organisation) child is a member of a class —
     the one their weekly work hangs off, named after the parent — so
     student/class.html drew it for them: a parent-named class, a due date
     their Today page contradicts, a school leaderboard. Their home is Today.
     The top bar already sends them there (class-entry.js); this covers the
     URL opened directly, a bookmark, or the class page's own links.
     Decided from the stored session's own address (MrBadmusConfig.
     isChildSession, the one test), synchronously, before anything is read
     or drawn. A school pupil's address never matches, so for them this is a
     no-op. Assignment pages are NOT on the list: a family child practises
     there. */
  /* Compared without `.html`: Cloudflare Pages serves /student/class.html
     at /student/class too. */
  const SCHOOL_ONLY = ['/student/class', '/student/classes'];

  function childAwayFromSchoolPage(session) {
    const c = window.MrBadmusConfig;
    if (!c || typeof c.isChildSession !== 'function') { return false; }
    if (SCHOOL_ONLY.indexOf(window.location.pathname.replace(/\.html$/, '')) < 0) { return false; }
    if (!c.isChildSession(session)) { return false; }
    const here = new URLSearchParams(window.location.search);
    const keep = new URLSearchParams();
    ['env', 'api'].forEach(function (k) { if (here.get(k)) { keep.set(k, here.get(k)); } });
    const q = keep.toString();
    window.location.replace((c.CHILD_HOME || '/consumer/today.html') + (q ? '?' + q : ''));
    return true;
  }

  function storedSessionSync() {
    try {
      const c = window.MrBadmusConfig;
      const raw = c && c.AUTH_STORAGE_KEY ? localStorage.getItem(c.AUTH_STORAGE_KEY) : null;
      if (!raw) { return null; }
      const txt = raw.indexOf('base64-') === 0
        ? decodeURIComponent(escape(atob(raw.slice(7)))) : raw;
      return JSON.parse(txt);
    } catch (e) { return null; }
  }

  async function requireStudentRole(opts) {
    opts = opts || {};
    const onAllowed = opts.onAllowed || function () {};
    const onDenied = opts.onDenied || null;

    if (childAwayFromSchoolPage(storedSessionSync())) { return; }

    const sb = getClient();
    if (!sb) {
      // getClient already console.error'd what was wrong. Fail-closed bounce.
      bounceToLogin();
      return;
    }

    /* ⊕ 27 Aug 2026 — THE TWO READS GO TOGETHER. Identical change to the one
       in shared/teacher-guard.js, made for the same measurement and carrying
       the same rule; the full reasoning lives there.

       In short: the profile read never needed `getUser()`'s ANSWER, only a
       user id and the client's persisted token, so it is started against the
       stored session's id in parallel. If `getUser()` then reports no session
       we bounce as before, and if it reports a DIFFERENT user the prefetched
       row is discarded unread and the real query runs. The row still comes
       back through RLS under the viewer's own token — what moved is when the
       request leaves, not who may read what. */
    let prefetchId = null;
    let prefetched = null;
    let storedSession = null;
    try {
      const stored = await sb.auth.getSession();
      storedSession = stored && stored.data ? stored.data.session : null;
      const storedUser = storedSession ? storedSession.user : null;
      if (storedUser && storedUser.id) {
        prefetchId = storedUser.id;
        // `.then()` forces the lazy PostgREST builder to fire NOW rather than
        // at the await below, which is the whole point.
        prefetched = sb
          .from('profiles')
          .select('first_name, last_name, role, school_id, avatar_url')
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

    /* ⊕ MRB-348 round 4 — THE OPTIMISTIC RENDER, and then the real check.

       Everything below still runs, in the order it always ran and with the
       same effect. What changes is only that on a cache hit the page is handed
       its context NOW rather than one round trip from now. See the note above
       `SESSION_PREFIX` for why that is safe, and §3 of the expiry argument for
       why the token test below is not decoration. */
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
          /* A throw out of the page's own render must not take the
             revalidation below down with it — the check still has to happen. */
          console.error('[student-guard] onAllowed threw on the cached path', e);
        }
      }
    }

    // 1. Session check via getUser() — round-trips to validate the JWT,
    // unlike getSession() which only reads localStorage.
    const { data: { user }, error: userError } = await sb.auth.getUser();
    if (userError || !user) {
      if (onDenied) return onDenied({ reason: 'no_session', error: userError });
      return bounceToLogin();
    }
    // The validated user, in case the stored copy was unreadable above.
    if (childAwayFromSchoolPage({ user: user })) { return; }

    // 2. Role check — the row already in flight, but only if it was asked for
    // about this same person.
    const { data: profile, error } = (prefetched && prefetchId === user.id)
      ? await prefetched
      : await sb
          .from('profiles')
          .select('first_name, last_name, role, school_id, avatar_url')
          .eq('id', user.id)
          .single();

    if (error && error.code !== 'PGRST116') {
      // A real query failure (network blip, RLS timeout) is NOT a denial —
      // don't dump a signed-in student on the login page as if they'd never
      // signed in. Bounce to login so a re-auth returns them here (return path
      // preserved). PGRST116 is Supabase's "no rows" code, handled below.
      console.error('[student-guard] profile lookup errored — bouncing to login', error);
      if (onDenied) return onDenied({ reason: 'profile_lookup_failed', error });
      return bounceToLogin();
    }
    if (!profile) {
      console.error('[student-guard] no profile row for session user — bouncing to home', error);
      if (onDenied) return onDenied({ reason: 'no_profile', error });
      return bounceToHome();
    }

    if (!ALLOWED_ROLES.includes(profile.role)) {
      if (onDenied) return onDenied({ reason: 'wrong_role', role: profile.role });
      return bounceToHome();
    }

    /* ⊕ MRB-348 round 4 — …unless the page already drew. On a cached load
       this whole function has BEEN the revalidation, and reaching here means
       it agreed: refresh the stamp so the next navigation is cheap too, and
       stop. Calling `onAllowed` a second time would boot the student runtime
       over its own mounted DOM. Every denial above is unguarded on purpose. */
    rememberResolution(user, profile);
    if (served) { return; }

    onAllowed({ user, profile });
  }

  // Sign the student out and send them to the login page. Idempotent
  // in spirit: the redirect always happens, even if signOut errors,
  // so the student is never stranded on a protected page.
  async function signOut() {
    /* ⊕ MRB-328 J4(b) — the shared session caches, dropped BEFORE the network
       call and before the redirect. A student surface caches only the class
       entry and the academic years, not a session (the optimistic-render path
       is staff-side), but the entry is per-viewer and a shared classroom
       machine is exactly where it must not survive one child signing out and
       the next signing in. Same call, same reasoning, same ordering argument
       as `teacher-guard.signOut` — see the longer note there. */
    try {
      const ce = window.MRBClassEntry;
      if (ce && ce.dropCaches) { ce.dropCaches(); }
    } catch (e) { /* a cache that will not clear must not strand a sign-out */ }

    const sb = getClient();
    if (sb) {
      try {
        await sb.auth.signOut();
      } catch (e) {
        console.error('[student-guard] signOut error', e);
      }
    }
    // Preserve the test environment across sign-out so a tester doesn't get
    // silently dropped onto the production auth page.
    const isTest = window.MrBadmusConfig && window.MrBadmusConfig.environment === 'test';
    // ⊕ B2C polish — and `api` with it, when the page has one.
    const apiQ = new URLSearchParams(window.location.search).get('api');
    window.location.replace('/auth.html' + (isTest ? '?env=test' + (apiQ ? '&api=' + encodeURIComponent(apiQ) : '') : ''));
  }

  return { requireStudentRole, signOut, getClient, ALLOWED_ROLES };
})();
