/**
 * shared/teacher-admin-nav.js — the Admin entry, and the ONE client-side
 * answer to "is this person admin-scoped?"  (MRB-303 Job 2)
 *
 * Two jobs, deliberately in one small file:
 *
 *   1. `window.MrBadmusAdminScope.isAdmin(sb, uid)` — the scope predicate.
 *      `teacher/admin.html` imports the SAME function for its own
 *      fail-closed guard, so the link and the page can never disagree about
 *      who is an admin. Two copies of this predicate is two answers, and the
 *      one that drifts is always the page's.
 *
 *   2. On load: if the viewer is admin-scoped, put an "Admin" link in the
 *      nav. Pure DOM append after render — it does NOT touch Design's
 *      compiled `__MRB_TPL__` tree, which is why this file can ship on the
 *      five ported pages without carrying any of that edit's risk.
 *
 * ─────────────────────────────────────────────────────────────────────────
 * ⚠️ THE PREDICATE MIRRORS `auth_user_has_scope()` EXACTLY. Do not simplify
 * it. The database function (verified live on prod AND test, 30 Aug 2026) is:
 *
 *     exists (select 1 from staff_scopes
 *              where profile_id = auth.uid() and scope = p_scope
 *                and started_at <= now()
 *                and (ended_at is null or ended_at > now())
 *                and deleted_at is null)
 *     -- M1 dual-read fallback (removed at the final advisory flip)
 *     or (p_scope = 'hod'          and profiles.role = 'hod')
 *     or (p_scope = 'school_admin' and profiles.role = 'admin')
 *
 * so a live `staff_scopes` row OR the legacy `profiles.role = 'admin'` path.
 * The legacy path is deliberate and documented in
 * `supabase/migrations/20260822000056_profiles_update_column_scope.sql` —
 * it is honoured here, not "cleaned up". `hz_legacyadmin` on TEST is a
 * fixture that has ONLY that path, and it must reach the page.
 *
 * ⛔ `hod` IS NOT ADMIN. `auth_user_has_scope('hod')` exists and the RLS
 * policies this page depends on
 * (`classes_admin_read` / `class_teachers_admin_read` /
 * `class_members_admin_read` / `profiles_admin_read_school`) all read
 * `school_admin OR slt` and never `hod`. Widening the check here would put
 * an Admin link in front of a head of department who would then be handed
 * zero rows by the database — an entry that leads to an empty room. The
 * narrowness is the point.
 *
 * ⚠️ BOTH READS ARE ALLOWED TO EVERYONE, so this costs a non-admin nothing
 * but two cheap queries and reveals nothing: `staff_scopes_self_read`
 * (`profile_id = auth.uid()`) and profiles' "Users can view own profile"
 * (`auth.uid() = id`) are self-reads that need no scope at all. A viewer
 * asking whether THEY are an admin is always answerable.
 *
 * ⚠️ THIS IS NOT THE SECURITY BOUNDARY — same standing as teacher-guard.js.
 * Hiding the link hides a link. The gates are the RLS policies above, which
 * hand a non-admin zero rows however they arrive at the page.
 * ─────────────────────────────────────────────────────────────────────────
 */

window.MrBadmusAdminScope = (function () {

  /* ── the predicate ──────────────────────────────────────────────────── */

  async function isAdmin(sb, uid) {
    if (!sb || !uid) { return false; }

    /* Both reads at once. Neither needs the other's answer, and the legacy
       fallback means we need the profile row even when the scopes read comes
       back empty — so there is no short-circuit worth having. */
    var scopeRes, profRes;
    try {
      var pair = await Promise.all([
        sb.from('staff_scopes')
          .select('scope, started_at, ended_at, deleted_at')
          .eq('profile_id', uid),
        sb.from('profiles').select('role').eq('id', uid).single(),
      ]);
      scopeRes = pair[0];
      profRes = pair[1];
    } catch (e) {
      // Fail CLOSED. A network blip is not a grant.
      console.error('[teacher-admin-nav] scope check failed', e);
      return false;
    }

    var rows = (scopeRes && scopeRes.data) || [];
    /* ⚠️ COMPARED AS ISO STRINGS, not Date objects, exactly as
       teacher-profile.html's access line already does it. `started_at` and
       `ended_at` are `timestamptz` and PostgREST renders them ISO-8601 in
       UTC, so lexical order IS chronological order and there is no parse to
       get wrong. */
    var nowIso = new Date().toISOString();
    function live(name) {
      for (var i = 0; i < rows.length; i++) {
        var r = rows[i];
        if (r.scope !== name) { continue; }
        if (r.deleted_at) { continue; }
        if (!(r.started_at <= nowIso)) { continue; }
        if (r.ended_at && !(r.ended_at > nowIso)) { continue; }
        return true;
      }
      return false;
    }

    var role = (profRes && profRes.data && profRes.data.role) || null;
    return live('school_admin') || live('slt') || role === 'admin';
  }

  /* ── the link ───────────────────────────────────────────────────────── */

  var MARK = 'data-mrb-admin-nav';          // so we never inject twice
  var HREF = '/teacher/admin.html';

  /* ⊕ MRB-306 — TODAY joins the same nav, through the same two hosts and the
     same redraw observer.

     It is here rather than in a file of its own because a new file would need
     a `<script>` tag on the five PORTED pages, and those tags are written by
     `build_teacher_port.py` from Design's template — a ruling, and a node
     index, for a link. This module is already loaded on every page that needs
     it and already survives the ported pages' full-tree redraw, which is the
     hard part and the part a fresh injector gets wrong.

     ⚠️ UNLIKE ADMIN, TODAY IS NOT SCOPE-GATED. Every teacher has a day. It is
     injected unconditionally, and needs no client and no predicate — so it is
     injected at DOM-ready rather than waiting on `client()`, and a page with
     no session still shows it (the page behind it does its own guarding). */
  var TODAY_MARK = 'data-mrb-today-nav';
  var TODAY_HREF = '/teacher/today.html';

  // Keep the environment across the hop. Both page families load config.js,
  // so this is the one source that works on the hand-written pages and the
  // ported ones alike — a tester on TEST who clicks Admin must not be
  // silently dropped onto production data.
  function href() {
    var c = window.MrBadmusConfig;
    return HREF + (c && c.environment === 'test' ? '?env=test' : '');
  }

  // Never link a page to itself.
  function isHere() {
    return window.location.pathname === HREF;
  }

  function make(style, label, mark, target) {
    var a = document.createElement('a');
    a.setAttribute(mark || MARK, '1');
    a.href = target || href();
    a.textContent = label;
    a.style.cssText = style;
    return a;
  }

  /* Today's own href/here pair. Kept beside `href()`/`isHere()` rather than
     folded into them: the two links differ in that Admin carries `?env=test`
     and Today does not need to, and collapsing them would tie one link's URL
     shape to the other's. */
  function todayHref() {
    var c = window.MrBadmusConfig;
    return TODAY_HREF + (c && c.environment === 'test' ? '?env=test' : '');
  }
  function todayIsHere() {
    return window.location.pathname === TODAY_HREF;
  }

  /* Host A — the hand-written staff pages (`teacher-profile.html`,
     `teacher/import.html`, `teacher/admin.html`).

     ⚠️ ANCHORED ON THE SIGN-OUT BUTTON, NOT ON `.nav-right`. The two pages
     do not agree on the container: teacher-profile.html uses
     `<div class="nav-right">` and import.html uses a bare inline-styled
     `<div>` with no class at all. The sign-out button is on both, is the
     last child of both, and is what the link must sit before — so it is the
     anchor. Selecting `.nav-right` silently did nothing on import.html. */
  function injectTopNav() {
    var btn = document.querySelector('nav.top-nav .signout-btn');
    if (!btn || !btn.parentNode) { return false; }
    if (btn.parentNode.querySelector('[' + MARK + ']')) { return true; }
    btn.parentNode.insertBefore(
      make('color:var(--muted);font-weight:700;font-size:0.85rem;' +
           'text-decoration:none;', 'Admin'), btn);
    return true;
  }

  /* Today, host A. Same anchor and same reasoning as `injectTopNav` above —
     the sign-out button, not `.nav-right`, because the hand-written pages do
     not agree on the container. */
  function injectTodayTopNav() {
    if (todayIsHere()) { return true; }
    var btn = document.querySelector('nav.top-nav .signout-btn');
    if (!btn || !btn.parentNode) { return false; }
    if (btn.parentNode.querySelector('[' + TODAY_MARK + ']')) { return true; }
    btn.parentNode.insertBefore(
      make('color:var(--muted);font-weight:700;font-size:0.85rem;' +
           'text-decoration:none;', 'Today', TODAY_MARK, todayHref()), btn);
    return true;
  }

  /* Today, host B — the ported pages' topbar. */
  function injectTodayTopbar() {
    if (todayIsHere()) { return true; }
    var bar = document.querySelector('[data-port-region="topbar"]');
    if (!bar) { return false; }
    if (bar.querySelector('[' + TODAY_MARK + ']')) { return true; }
    var buttons = bar.querySelectorAll('button');
    var out = buttons.length ? buttons[buttons.length - 1] : null;
    var link = make(
      'flex:none;height:32px;padding:0 12px;display:inline-flex;' +
      'align-items:center;font:600 15.5px/1.2 var(--st-ui);' +
      'color:var(--st-muted);background:transparent;' +
      'border:1px solid var(--st-btn-border);border-radius:9px;' +
      'cursor:pointer;text-decoration:none;', 'Today', TODAY_MARK, todayHref());
    if (out) { bar.insertBefore(link, out); } else { bar.appendChild(link); }
    return true;
  }

  function injectToday() {
    var a = injectTodayTopNav();
    var b = injectTodayTopbar();
    return a || b;
  }

  /* Host B — the five ported pages, whose topbar is `data-port-region`
     ("ours, stable" — teacher_rulings.py's own words).

     ⚠️ RE-INJECTED ON EVERY REDRAW, and that is not belt-and-braces. The
     runtime's `draw()` does `host.textContent = ""` and rebuilds the WHOLE
     tree from the template on every state change — open the search sheet,
     switch a key-stage tab, pick a year, and the topbar is a brand-new set
     of nodes. A one-shot append survives until the teacher's first click and
     then vanishes, which is precisely the kind of defect a screenshot taken
     immediately after load reports as working. */
  function injectTopbar() {
    var bar = document.querySelector('[data-port-region="topbar"]');
    if (!bar) { return false; }
    if (bar.querySelector('[' + MARK + ']')) { return true; }
    // The sign-out button is the topbar's last child and the link belongs
    // before it, matching the hand-written pages' running order.
    var buttons = bar.querySelectorAll('button');
    var out = buttons.length ? buttons[buttons.length - 1] : null;
    var link = make(
      'flex:none;height:32px;padding:0 12px;display:inline-flex;' +
      'align-items:center;font:600 15.5px/1.2 var(--st-ui);' +
      'color:var(--st-muted);background:transparent;' +
      'border:1px solid var(--st-btn-border);border-radius:9px;' +
      'cursor:pointer;text-decoration:none;', 'Admin');
    if (out) { bar.insertBefore(link, out); } else { bar.appendChild(link); }
    return true;
  }

  function inject() {
    // A page is one family or the other, never both; try each.
    var a = injectTopNav();
    var b = injectTopbar();
    return a || b;
  }

  /* ⊕ MRB-306. Today is armed on its own, at DOM-ready, because it is not
     scope-gated and so must not wait on `client()` — a teacher with a slow
     session would otherwise watch the nav change shape seconds after the page
     settled. It rides the SAME observer as Admin (see `watch`), which is what
     keeps it alive through the ported pages' full-tree redraws. */
  function watchToday() {
    injectToday();
    var mount = document.getElementById('mrb-teacher') || document.body;
    if (!mount || !window.MutationObserver) { return; }
    var pending = false;
    new MutationObserver(function () {
      if (pending) { return; }
      pending = true;
      (window.requestAnimationFrame || window.setTimeout)(function () {
        pending = false;
        injectToday();
      }, 0);
    }).observe(mount, { childList: true, subtree: true });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', watchToday);
  } else {
    watchToday();
  }

  function watch() {
    inject();
    /* The ported pages mount asynchronously and redraw forever after, so the
       observer is the mechanism rather than a safety net. On the
       hand-written pages the nav is static, `inject()` above has already
       succeeded, and the observer simply never fires — it costs nothing to
       arm it in both cases rather than branching on which page we are. */
    var mount = document.getElementById('mrb-teacher') || document.body;
    if (!mount || !window.MutationObserver) { return; }
    var pending = false;
    new MutationObserver(function () {
      // Coalesce: a redraw is many mutations and we want one re-inject.
      if (pending) { return; }
      pending = true;
      (window.requestAnimationFrame || window.setTimeout)(function () {
        pending = false;
        inject();
      }, 0);
    }).observe(mount, { childList: true, subtree: true });
  }

  /* ── boot ───────────────────────────────────────────────────────────── */

  /* The client comes from teacher-guard.js, and on the FIVE PORTED PAGES
     that file is not on the page yet: `teacher-live.js` loads it itself,
     asynchronously, through `loadDeps()`. So this waits for it rather than
     reading it once and giving up — reading once is why an injector like
     this works on the two hand-written pages and silently does nothing on
     the five that matter most.

     Bounded, and a timeout is simply "no link": on a fixture page (no
     config.js, no SDK, no session) that is the correct and intended
     outcome, not a failure. */
  async function client(ms) {
    var deadline = Date.now() + (ms || 15000);
    for (;;) {
      var g = window.MrBadmusTeacherGuard;
      if (g && g.getClient) {
        var sb = g.getClient();
        if (sb) { return sb; }
      }
      if (Date.now() > deadline) { return null; }
      await new Promise(function (r) { setTimeout(r, 120); });
    }
  }

  async function boot() {
    /* On `admin.html` itself there is nothing to link to. The module still
       LOADS there, because the page imports `isAdmin` from it for its own
       fail-closed guard — one predicate, two callers. */
    if (isHere()) { return; }
    var sb = await client();
    if (!sb) { return; }
    /* `getSession()` is a localStorage read, not a round trip. The link is
       chrome — it does not need `getUser()`'s server-side JWT validation,
       and the page it points at re-checks everything from scratch anyway. */
    var sess;
    try { sess = await sb.auth.getSession(); } catch (e) { return; }
    var user = sess && sess.data && sess.data.session
      ? sess.data.session.user : null;
    if (!user || !user.id) { return; }
    if (!(await isAdmin(sb, user.id))) { return; }
    watch();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function () { boot(); });
  } else {
    boot();
  }

  return { isAdmin: isAdmin, inject: inject };
})();
