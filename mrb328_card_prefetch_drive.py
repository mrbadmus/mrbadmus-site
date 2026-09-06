#!/usr/bin/env python3
"""mrb328_card_prefetch_drive.py — MRB-328 J4(b). Does the hover actually help?

    MRB_TEST_TEACHER_PASSWORD=… python3 mrb328_card_prefetch_drive.py

⚑ WHY THIS EXISTS

`teacher/class-detail.html` is a 165 KB document served `max-age=0`, so every
press of a class card begins by downloading it. J4(b) spends the time a
pointer rests on a card: `armCardPrefetch` in `shared/teacher-live.js` puts a
`<link rel="prefetch">` in the head for the page that card would open.

⚠️ AND EVERY WAY THAT CAN GO WRONG IS SILENT. This is an affordance with no
   visible output: it draws nothing, it changes no text, and it is wrapped in
   `try/catch` so that a page is never taken down by a speculative fetch. A
   version of it that fires for nobody and a version that fires for everybody
   look identical from the outside, and BOTH are wrong. One buys nothing; the
   other prefetches a colleague's class pages off an admin's screen.

   That is not hypothetical. The first version of the scoped-list guard read
   `if (data.scope)`, which is a key `load()` has never published — `base()`
   sets it on its own cache object, `load()` publishes `scopeTeacherParam` and
   `scopePendingParam` instead. `undefined` is falsy, so the refusal was a
   no-op that read like a refusal. Nothing said so, and no other gate on this
   estate looks at the head of a signed-in classes page.

── WHAT IS CHECKED ──────────────────────────────────────────────────────

  1. NOTHING IS PREFETCHED BEFORE A HOVER. A page that speculatively fetched
     every class on mount would pass a naive "is there a link" check while
     doing the opposite of what this is for.
  2. A POINTER OVER A CARD PRODUCES EXACTLY ONE LINK, and its href is the URL
     that card's own click handler would navigate to — same file, same
     parameters, same ORDER. A prefetch of `?class=X` when the click goes to
     `?class=X&env=test` warms an entry nobody asks for and costs a teacher
     165 KB for nothing, silently.
  3. IT IS IDEMPOTENT. Hovering the same card forty more times — which is what
     crossing its descendants does — adds no second link.
  4. THE ZERO-STUDENT FORK IS HONOURED. `c.open` routes a card with no roster
     to the IMPORT screen (a standing ruling), so a prefetch of
     `class-detail.html` for such a card would be warming the wrong page.
     Checked by reading the card's own `MRB_DATA` row rather than by assuming
     the fixture has one.
  5. A SCOPED LIST PREFETCHES NOTHING. `?teacher=<profile>` draws a
     COLLEAGUE'S classes (MRB-328 J3); the head must stay empty of prefetches.
     This is the reason the file exists, and it takes THREE checks, because
     the obvious single check is the one that misleads.

     ⚠️ `?teacher=` IN THE URL IS NOT THE SAME THING AS A SCOPED PAGE, and the
     first version of this gate confused the two and went red against correct
     code. `resolveClassScope` honours the parameter only for an ADMIN; a
     plain teacher who types it is shown HER OWN classes, unheaded and
     unmarked (MRB-328 J3, and `teacher_admin_foreign_class_drive` D4 proves
     it). On that page prefetching is not a leak — it is the right behaviour,
     because the list is hers. So:

       5a. the plain teacher's `?teacher=` was NOT honoured, and the page
           therefore DOES prefetch. Asserted positively, so this gate can
           never pass by measuring a page that simply has no cards on it.
       5b. the payload publishes `scopeTeacherParam` / `scopePendingParam`
           and does NOT publish `scope`. This is the exact fact the guard
           depends on and the exact fact whose absence made the first guard a
           silent no-op — `if (data.scope)` on a key `load()` has never
           emitted. Pinning the key NAMES is what stops that recurring.
       5c. a REAL school admin, whose `?teacher=` IS honoured, prefetches
           nothing. Env-switched on $MRB_THROWAWAY_PASSWORD — the MRB-326
           throwaway admin — for the same reason `mrb328_import_picker_drive
           --section a` is: a push must not depend on a shared project being
           reachable. Reported SKIPPED, by name, when it is not set.

Signs in as the MRB-293 TEST fixture `hz_amy` — a fake account on the sandbox
project, password from $MRB_TEST_TEACHER_PASSWORD with no literal fallback, so
`prepush_gate.py` reports this SKIPPED BY NAME on a machine that has not opted
in. It READS ONLY: no row on TEST is written, updated or deleted.
"""

import json
import os
import re
import ssl
import sys
import time
import urllib.request

REPO = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, REPO)
os.chdir(REPO)

import ks3_browser as cdp

REF = "qeppkiswvclkkwbxmlok"
URL = "https://%s.supabase.co" % REF
PORT = 5517
CTX = ssl.create_default_context(cafile="/etc/ssl/cert.pem")

AMY = "hz_amy@test.mrbadmus"
SETTLE_S = 12.0          # the classes screen mounts after two read waves
POLL_S = 0.15

fails = []


def check(label, ok, detail=""):
    print("     %s %s%s" % ("✅" if ok else "❌", label,
                            ("  — %s" % detail) if detail else ""))
    if not ok:
        fails.append(label + ((" — " + detail) if detail else ""))


def anon_key():
    src = open("shared/config.js", encoding="utf-8").read()
    return re.search(r"'(eyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+)'",
                     src[src.index("const TEST"):]).group(1)


def password():
    pw = os.environ.get("MRB_TEST_TEACHER_PASSWORD")
    if not pw:
        raise SystemExit(
            "mrb328_card_prefetch_drive: $MRB_TEST_TEACHER_PASSWORD is not "
            "set, so this gate cannot sign in. It is the MRB-293 TEST fixture "
            "password — see the module docstring.")
    return pw


THROWAWAY_ENV = "MRB_THROWAWAY_PASSWORD"
ADMIN_EMAIL = "mrb326_admin@throwaway.test"

# Cross every element in the classes region. This is what a pointer travelling
# over a card actually does — forty-odd `pointerover` events, one per
# descendant — and it is the shape that would expose a prefetch fired from a
# handler with no idempotence.
HOVER_EVERYTHING = r"""(function () {
  var region = document.querySelector('[data-port-region="classes"]');
  if (!region) { return 'no region'; }
  var all = region.querySelectorAll('*');
  for (var i = 0; i < all.length; i++) {
    all[i].dispatchEvent(new PointerEvent('pointerover',
                         {bubbles: true, cancelable: true}));
  }
  return 'ok';
})()"""


def sign_in(email, key, pw=None):
    req = urllib.request.Request(
        URL + "/auth/v1/token?grant_type=password",
        data=json.dumps({"email": email,
                         "password": pw or password()}).encode(),
        headers={"apikey": key, "Content-Type": "application/json"},
        method="POST")
    with urllib.request.urlopen(req, timeout=60, context=CTX) as r:
        return json.loads(r.read().decode())


def put_session(page, base, key, sess):
    page.goto(base + "/leaderboard.html?env=test", settle=2.0)
    return page.eval("""
      (async function () {
        var c = window.supabase.createClient(%s, %s);
        var r = await c.auth.setSession({access_token: %s, refresh_token: %s});
        return r.error ? 'error: ' + r.error.message : 'ok';
      })()
    """ % (json.dumps(URL), json.dumps(key),
           json.dumps(sess["access_token"]), json.dumps(sess["refresh_token"])))


# The mount signal: the runtime has drawn its classes region and the boot
# wrapper that carries the skeleton is gone.
MOUNTED = r"""(function () {
  var h = document.getElementById('mrb-teacher');
  if (!h) { return 'no host'; }
  if (h.querySelector('[data-mrb-state]')) { return 'booting'; }
  return h.querySelector('[data-port-region="classes"]') ? 'ready' : 'no region';
})()"""

PREFETCHES = r"""JSON.stringify(
  Array.prototype.map.call(
    document.querySelectorAll('link[rel="prefetch"]'),
    function (l) { return l.getAttribute('href'); }))"""


def wait_mounted(page, why):
    deadline = time.time() + SETTLE_S
    last = "?"
    while time.time() < deadline:
        last = page.eval(MOUNTED) or "?"
        if last == "ready":
            return True
        time.sleep(POLL_S)
    check("the classes screen mounted (%s)" % why, False, last)
    return False


def main():
    key = anon_key()
    print("\n🖱   MRB-328 J4(b) — hover a class card, start fetching its page\n")

    server, port = cdp.serve("mrbadmus_site", port=PORT)
    base = "http://localhost:%d" % port

    try:
        with cdp.Browser() as b:
            page = b.attach()
            page.set_viewport(1280, 1000)

            sess = sign_in(AMY, key)
            got = put_session(page, base, key, sess)
            if got != "ok":
                raise SystemExit("could not sign in as %s: %s" % (AMY, got))

            # ── the viewer's own list ───────────────────────────────────
            print("  ── hz_amy's own classes ──────────────────────────────")
            page.goto(base + "/teacher/classes.html?env=test", settle=1.0)
            if not wait_mounted(page, "own list"):
                raise SystemExit(1)

            before = json.loads(page.eval(PREFETCHES) or "[]")
            check("1. nothing is prefetched before a hover", before == [],
                  json.dumps(before)[:70])

            # The first card, and the URL its own handler would navigate to —
            # read out of the page's own data rather than assumed, so the
            # zero-student fork is honoured by the EXPECTATION too.
            expected = page.eval(r"""(function () {
              var d = window.__MRB_DATA__ || {};
              var k = (d.CLASSES || [])[0];
              if (!k) { return JSON.stringify({err: 'no classes'}); }
              var env = (typeof MRB_ENV === 'function') ? MRB_ENV() : '';
              var q = ['class=' + encodeURIComponent(k.id)];
              if (d.yearParam) { q.push('year=' + encodeURIComponent(d.yearParam)); }
              if (env) { q.push('env=' + env); }
              return JSON.stringify({
                code: k.code, n: k.n,
                href: '/teacher/' + (k.n > 0 ? 'class-detail.html' : 'import.html')
                      + '?' + q.join('&')
              });
            })()""")
            exp = json.loads(expected or "{}")
            if exp.get("err"):
                check("hz_amy has at least one class to hover", False, exp["err"])
                raise SystemExit(1)

            # Hover the card by dispatching the event the code listens for,
            # on the deepest element showing the class code — i.e. the thing a
            # real pointer would actually land on, not the card's own root.
            hovered = page.eval(r"""(function () {
              var region = document.querySelector('[data-port-region="classes"]');
              var code = %s;
              var hit = null;
              var all = region.querySelectorAll('*');
              for (var i = 0; i < all.length; i++) {
                if (!all[i].children.length &&
                    (all[i].textContent || '').trim() === code) { hit = all[i]; break; }
              }
              if (!hit) { return 'no element showing ' + code; }
              hit.dispatchEvent(new PointerEvent('pointerover',
                                {bubbles: true, cancelable: true}));
              return 'hovered';
            })()""" % json.dumps(exp["code"]))
            check("a card showing %s was hovered" % exp["code"],
                  hovered == "hovered", hovered)

            after = json.loads(page.eval(PREFETCHES) or "[]")
            check("2. the hover produced exactly one prefetch",
                  len(after) == 1, json.dumps(after)[:90])
            check("2. …for the URL that card's own handler would open",
                  after[:1] == [exp["href"]],
                  "got %s / want %s" % (json.dumps(after[:1]), exp["href"]))

            # 4. The fork, stated against the card actually driven.
            want_file = "class-detail.html" if exp["n"] > 0 else "import.html"
            check("4. the %s-student fork is honoured (%s)"
                  % ("zero" if exp["n"] == 0 else "non-zero", want_file),
                  bool(after) and want_file in after[0],
                  "n=%s href=%s" % (exp["n"], after[0] if after else "-"))

            # 3. Idempotence — forty more crossings of the same card.
            page.eval(r"""(function () {
              var region = document.querySelector('[data-port-region="classes"]');
              var all = region.querySelectorAll('*');
              for (var pass = 0; pass < 40; pass++) {
                for (var i = 0; i < all.length && i < 60; i++) {
                  all[i].dispatchEvent(new PointerEvent('pointerover',
                                       {bubbles: true, cancelable: true}));
                }
              }
              return 'ok';
            })()""")
            again = json.loads(page.eval(PREFETCHES) or "[]")
            check("3. crossing the card's descendants 40x adds no duplicate",
                  len(again) == len(set(again)),
                  "%d link(s), %d unique" % (len(again), len(set(again))))
            check("3. …and never more than one link per class card",
                  len(again) <= len(json.loads(page.eval(
                      "JSON.stringify((window.__MRB_DATA__||{}).CLASSES||[])")
                      or "[]")),
                  "%d link(s)" % len(again))

            # ── `?teacher=`, refused: still her own list ────────────────
            print("\n  ── `?teacher=` typed by a plain teacher ──────────────")
            viewer = json.loads(page.eval(
                "JSON.stringify((window.__MRB_DATA__||{}).ME || '')") or '""')
            page.goto(base + "/teacher/classes.html?env=test&teacher=" + viewer,
                      settle=1.0)
            if wait_mounted(page, "refused-scope list"):
                shape = json.loads(page.eval(r"""(function () {
                  var d = window.__MRB_DATA__ || {};
                  return JSON.stringify({
                    hasScopeTeacher: ('scopeTeacherParam' in d),
                    hasScopePending: ('scopePendingParam' in d),
                    hasBareScope: ('scope' in d),
                    scopeTeacher: d.scopeTeacherParam,
                    classes: (d.CLASSES || []).length
                  });
                })()""") or "{}")

                # 5b — the key names the guard is written against.
                check("5b. the payload publishes `scopeTeacherParam`",
                      shape.get("hasScopeTeacher") is True, json.dumps(shape))
                check("5b. …and `scopePendingParam`",
                      shape.get("hasScopePending") is True)
                check("5b. …and does NOT publish a bare `scope` — the key the "
                      "first guard read, which is why it never fired",
                      shape.get("hasBareScope") is False)

                # 5a — she is on HER OWN list, so the prefetch is correct here.
                check("5a. a plain teacher's `?teacher=` is NOT honoured",
                      shape.get("scopeTeacher") == "",
                      "scopeTeacherParam=%r" % shape.get("scopeTeacher"))
                page.eval(HOVER_EVERYTHING)
                own = json.loads(page.eval(PREFETCHES) or "[]")
                check("5a. …so she sees her own classes and they DO prefetch",
                      len(own) >= 1 and shape.get("classes", 0) >= 1,
                      "%d link(s) over %d card(s)"
                      % (len(own), shape.get("classes", 0)))

            # ── 5c. a real admin, whose scope IS honoured ───────────────
            print("\n  ── `?teacher=` honoured, for a real school admin ─────")
            admin_pw = os.environ.get(THROWAWAY_ENV)
            if not admin_pw:
                print("     ⏭  SKIPPED — $%s is not set, so the honoured-scope\n"
                      "        half cannot sign in. 5a/5b above still prove the\n"
                      "        guard reads keys that exist." % THROWAWAY_ENV)
            else:
                asess = sign_in(ADMIN_EMAIL, key, admin_pw)
                if put_session(page, base, key, asess) != "ok":
                    check("5c. the throwaway admin signed in", False)
                else:
                    target = page.eval(r"""(async function () {
                      var c = window.supabase.createClient(%s, %s);
                      var r = await c.from('class_teachers')
                        .select('teacher_id').is('deleted_at', null)
                        .is('ended_at', null).limit(40);
                      var me = (await c.auth.getUser()).data.user.id;
                      var rows = r.data || [];
                      for (var i = 0; i < rows.length; i++) {
                        if (rows[i].teacher_id && rows[i].teacher_id !== me) {
                          return rows[i].teacher_id;
                        }
                      }
                      return '';
                    })()""" % (json.dumps(URL), json.dumps(key))) or ""
                    check("5c. a colleague with classes was found to scope to",
                          bool(target), target[:40] or "none")
                    if target:
                        page.goto(base + "/teacher/classes.html?env=test&teacher="
                                  + target, settle=1.0)
                        if wait_mounted(page, "honoured-scope list"):
                            sh = json.loads(page.eval(
                                "JSON.stringify({s:(window.__MRB_DATA__||{})"
                                ".scopeTeacherParam,n:((window.__MRB_DATA__||{})"
                                ".CLASSES||[]).length})") or "{}")
                            check("5c. the scope WAS honoured — this is a "
                                  "colleague's list", bool(sh.get("s")),
                                  json.dumps(sh))
                            check("5c. …with cards on it to hover",
                                  sh.get("n", 0) >= 1, json.dumps(sh))
                            page.eval(HOVER_EVERYTHING)
                            scoped = json.loads(page.eval(PREFETCHES) or "[]")
                            check("5c. …and NOTHING was prefetched",
                                  scoped == [], json.dumps(scoped)[:90])
    finally:
        server.shutdown()

    print("\n" + "─" * 68)
    if fails:
        print("❌ mrb328_card_prefetch_drive: %d check(s) failed" % len(fails))
        for f in fails:
            print("   · " + f)
        return 1
    print("✅ mrb328_card_prefetch_drive: the hover fires, once, for the right "
          "URL — and never on a colleague's list")
    return 0


if __name__ == "__main__":
    sys.exit(main())
