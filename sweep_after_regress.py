#!/usr/bin/env python3
"""sweep_after_regress.py — MRB-336/337 §8, the four regression questions.

    python3 sweep_after_regress.py <phase>

Each phase is one world state, driven as the pupil `student1@test-rainford.local`
on 10X1 Biology, and prints what the page, the bell and the banner all say. The
world is moved between phases by the caller (the product's own teacher routes
for the assignments, SQL only for the school's hold and for a row's stamped
week, neither of which has a product surface a pupil-side sweep can reach).

Phases

    hold        the school hold is in the future — released teacher work must
                still reach the pupil, and the automatic slot must be empty
    carried     the released row's `academic_week` is NOT the current week —
                it must STILL be on the bench (MRB-336's bench fix)
    scheduled   the scheduled row must be absent from the page AND unreachable
                by its own id
    deleted     the deleted row must be gone from the page, the bell and the
                banner
    baseline    nothing moved — what the pupil sees normally
"""
import json
import os
import sys
import time

import ks3_browser as cdp

SITE_PORT = 5508
API = os.environ.get("MRB_API", "http://localhost:3338")
SB = "https://qeppkiswvclkkwbxmlok.supabase.co"
KEY = ("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFlcHBraXN3"
       "dmNsa2t3YnhtbG9rIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Nzc2NjMzMzMsImV4cCI6MjA5MzIzOTMzM30"
       ".WxprirdO3yIZfcOiUMwbVPFPcD6Sx5SIZrQ3pvMOKT8")
PUPIL = "student1@test-rainford.local"

STATE = r"""(function () {
  var de = document.documentElement;
  var t = (document.body.innerText || '').replace(/\s+/g, ' ').trim();
  var bell = document.querySelector('[data-mrb-bell]');
  var badge = bell && bell.querySelector('[data-mrb-bell-badge]');
  var panel = document.getElementById('mrb-bell-panel');
  var banner = document.querySelector('[data-mrb-reminder]');
  return {
    text: t,
    scrollW: de.scrollWidth, clientW: de.clientWidth,
    bench: (t.match(/ON THE BENCH NOW[^]{0,120}/) || [''])[0],
    heldLine: t.indexOf("isn't live yet") >= 0,
    bellLabel: bell ? (bell.getAttribute('aria-label') || '') : '(no bell)',
    badgeText: badge && !badge.hidden ? (badge.textContent || '').trim() : '',
    bannerText: banner ? (banner.innerText || '').replace(/\s+/g, ' ').trim() : ''
  };
})()"""

PANEL = r"""(function () {
  var b = document.querySelector('[data-mrb-bell]');
  if (b) { b.click(); }
  return null;
})()"""

PANEL_READ = r"""(function () {
  var p = document.getElementById('mrb-bell-panel');
  if (!p || p.hidden) { return {open: false, rows: -1, text: ''}; }
  return {open: true, rows: p.querySelectorAll('[data-mrb-bell-row]').length,
          text: (p.innerText || '').replace(/\s+/g, ' ').trim()};
})()"""


def sign_in(br, base, email):
    boot = br.page(base + "/shared/", settle=0.4)
    boot.eval("(function(){var s=document.createElement('script');"
              "s.src='https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2';"
              "document.head.appendChild(s);})()")
    for _ in range(60):
        if boot.eval("!!(window.supabase && window.supabase.createClient)"):
            break
        time.sleep(0.25)
    return boot.eval(
        "(async function(){var c=window.supabase.createClient(%s,%s);"
        "var r=await c.auth.signInWithPassword({email:%s,password:'TestPass!2026'});"
        "return r.error?('err:'+r.error.message):'ok';})()"
        % (json.dumps(SB), json.dumps(KEY), json.dumps(email)))


def load(br, base, path, width=390):
    br.page("about:blank", settle=0.15).set_viewport(width, 900)
    pg = br.page(base + path + ("&" if "?" in path else "?") + "api=" + API,
                 settle=3.0)
    for _ in range(50):
        if pg.eval("document.body.innerText.trim().length > 30"):
            break
        time.sleep(0.3)
    time.sleep(1.6)
    return pg


def main():
    phase = sys.argv[1] if len(sys.argv) > 1 else "baseline"
    made = json.load(open(os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "..", "made.json"))) \
        if False else None
    site, port = cdp.serve("mrbadmus_site", port=SITE_PORT)
    base = "http://localhost:%d" % port
    out = {"phase": phase}
    try:
        with cdp.Browser() as br:
            print("sign-in", sign_in(br, base, PUPIL))
            pg = load(br, base, "/student/class.html")
            st = pg.eval(STATE)
            pg.eval(PANEL)
            time.sleep(0.8)
            st["panel"] = pg.eval(PANEL_READ)
            out["class"] = st
            print("\n── class page ──")
            print("  bench      : %s" % (st["bench"] or "(none)"))
            print("  held line  : %s" % st["heldLine"])
            print("  bell label : %s" % st["bellLabel"])
            print("  badge      : %r" % st["badgeText"])
            print("  banner     : %s" % (st["bannerText"][:120] or "(none)"))
            print("  panel      : open=%s rows=%s" % (st["panel"]["open"],
                                                      st["panel"]["rows"]))
            print("  panel text : %s" % st["panel"]["text"][:220])
            print("  scrollW/clientW : %d/%d" % (st["scrollW"], st["clientW"]))
            print("  titles seen: %s"
                  % [w for w in ("Cell Biology check-in", "Cell Biology later",
                                 "Atomic Structure")
                     if w in st["text"]])

            # the scheduled row, reached by its own id
            sched = os.environ.get("MRB_SCHED_ID", "")
            if sched:
                pg2 = load(br, base, "/student/assignment.html?assignment=" + sched)
                t2 = pg2.eval("(document.body.innerText||'').replace(/\\s+/g,' ').trim()")
                out["scheduled_by_id"] = t2
                print("\n── scheduled by id (%s) ──\n  %s" % (sched[:8], t2[:260]))

            dead = os.environ.get("MRB_DELETED_ID", "")
            if dead:
                pg3 = load(br, base, "/student/assignment.html?assignment=" + dead)
                t3 = pg3.eval("(document.body.innerText||'').replace(/\\s+/g,' ').trim()")
                out["deleted_by_id"] = t3
                print("\n── deleted by id (%s) ──\n  %s" % (dead[:8], t3[:260]))
    finally:
        site.shutdown()

    p = os.path.join("docs", "mrb336", "regress-%s.json" % phase)
    with open(p, "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=1)
    print("\nwrote %s" % p)


if __name__ == "__main__":
    main()
