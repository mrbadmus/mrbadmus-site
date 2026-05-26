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

  function bounceToLogin() {
    const here = window.location.pathname + window.location.search;
    window.location.replace('/auth.html?return=' + encodeURIComponent(here));
  }

  function bounceToHome() {
    window.location.replace('/index.html');
  }

  async function requireStudentRole(opts) {
    opts = opts || {};
    const onAllowed = opts.onAllowed || function () {};
    const onDenied = opts.onDenied || null;

    const sb = getClient();
    if (!sb) {
      // getClient already console.error'd what was wrong. Fail-closed bounce.
      bounceToLogin();
      return;
    }

    // 1. Session check via getUser() — round-trips to validate the JWT,
    // unlike getSession() which only reads localStorage.
    const { data: { user }, error: userError } = await sb.auth.getUser();
    if (userError || !user) {
      if (onDenied) return onDenied({ reason: 'no_session', error: userError });
      return bounceToLogin();
    }

    // 2. Role check.
    const { data: profile, error } = await sb
      .from('profiles')
      .select('first_name, last_name, role, school_id, avatar_url')
      .eq('id', user.id)
      .single();

    if (error || !profile) {
      console.error('[student-guard] profile lookup failed for session user — bouncing to home', error);
      if (onDenied) return onDenied({ reason: 'profile_lookup_failed', error });
      return bounceToHome();
    }

    if (!ALLOWED_ROLES.includes(profile.role)) {
      if (onDenied) return onDenied({ reason: 'wrong_role', role: profile.role });
      return bounceToHome();
    }

    onAllowed({ user, profile });
  }

  // Sign the student out and send them to the login page. Idempotent
  // in spirit: the redirect always happens, even if signOut errors,
  // so the student is never stranded on a protected page.
  async function signOut() {
    const sb = getClient();
    if (sb) {
      try {
        await sb.auth.signOut();
      } catch (e) {
        console.error('[student-guard] signOut error', e);
      }
    }
    window.location.replace('/auth.html');
  }

  return { requireStudentRole, signOut, getClient, ALLOWED_ROLES };
})();
