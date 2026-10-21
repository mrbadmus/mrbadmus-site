#!/usr/bin/env python3
"""weekly_challenge_teacher_drive.py -- Unit C: the weekly challenge on the
TEACHER class page, rendered by the real generated template.

    python3 weekly_challenge_teacher_drive.py [--shots DIR]

Exit 0 clean, 1 on any failure.

Drives `teacher_fixtures/class-detail-fixture.html` (the populated class page,
mounted by the same runtime and rulings as `teacher/class-detail.html`) and
adds `CHALLENGES` -- the separate list teacher-live.js `buildChallenges` writes
from `pack.challenges` -- then re-renders (the week bucketing itself is pinned by
tools/teacher_challenge_cards_test.js, against the real file). Asserts, on VISIBLE TEXT:

  4(a)  the page's own figures are UNCHANGED by a challenge being set:
        "11 of 16 in", the class mean line, the students table, the
        assignments table (a challenge is never a column or a "not handed in")
  4(b)  the card reads "Weekly challenge: Physics", when it closes, and has no
        Remind / Edit / Worksheet / Set again / count of anyone
  4(c)  Remove arms on the first press and sends DELETE
        /api/teacher/set-work/<id> on the second

The fixture is never edited; the list is added in the page at run time.
"""

import json
import os
import sys
import time

REPO = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, REPO)
os.chdir(REPO)

import ks3_browser as cdp

PATH = "teacher_fixtures/class-detail-fixture.html"


ADD = """(function () {
  var d = window.__MRB_DATA__;
  d.CHALLENGES = {};
  d.CLASSES.forEach(function (c) {
    d.CHALLENGES[c.id] = [{ id: 'chal-1', title: 'Weekly challenge: Physics', weekIdx: 0,
                            dueAt: '2026-10-23T09:15:00Z', due: 'Fri 23 Oct' }];
  });
  // The fixtures carry no teacher-live.js, and defining MrBadmusTeacherLive would flip
  // other branches of the page; the week bucketing is pinned by
  // tools/teacher_challenge_cards_test.js against the real file. Here the list is
  // handed straight to the card, which is what this drive is about.
  window.MRB_CHALLENGES = function (id) { return d.CHALLENGES[id] || []; };
  window.__reqs = [];
  window.fetch = function (u, init) {
    window.__reqs.push({ url: String(u), method: (init && init.method) || 'GET' });
    return Promise.resolve({ ok: true, status: 200, json: function () { return Promise.resolve({ ok: true }); } });
  };
  window.MRB_TOKEN = function () { return Promise.resolve('t'); };
  window.MRB_API = function () { return 'https://api.test'; };
  return 'ok';
})()"""

TEXT = "document.body.innerText"

CLICK_TEXT = """(function (needle) {
  var hit = null;
  document.querySelectorAll('button').forEach(function (b) {
    if (!hit && (b.innerText || '').trim().toUpperCase().indexOf(needle.toUpperCase()) === 0) { hit = b; }
  });
  if (!hit) { return 'MISS'; }
  hit.click(); return 'ok';
})(%s)"""


def main():
    shots = None
    if "--shots" in sys.argv:
        shots = sys.argv[sys.argv.index("--shots") + 1]
        os.makedirs(shots, exist_ok=True)
    fails = []

    def check(name, ok, detail=""):
        print("  %s  %s%s" % ("ok  " if ok else "FAIL", name, ("" if ok else "\n         " + detail)))
        if not ok:
            fails.append(name)

    server, port = cdp.serve(REPO)
    url = "http://127.0.0.1:%d/%s" % (port, PATH)
    try:
        with cdp.Browser() as b:
            page = b.attach()
            for (w, h) in ((390, 844), (1280, 900)):
                print("\nviewport %dx%d" % (w, h))
                page.set_viewport(w, h)
                page.goto(url)
                time.sleep(3)
                before = page.eval(TEXT)
                check("baseline has no challenge card", "Weekly challenge" not in before)
                page.eval(ADD)
                # re-render: pick this week's chip again
                page.eval("window.__MRB_CMP__.logic.forceUpdate(), 'ok'")
                time.sleep(0.8)
                after = page.eval(TEXT)

                check("4(b) the card reads 'Weekly challenge: Physics'", "Weekly challenge: Physics" in after)
                check("4(b) and when it closes", "CLOSES FRI 23 OCT" in after.upper(), after[:200])
                i = after.index("Weekly challenge: Physics") if "Weekly challenge: Physics" in after else 0
                card = after[i - 40:i + 140]
                bad = [t for t in ("Remind", "Edit", "Worksheet", "Set again", "played", " of ", "NOT IN YET")
                       if t in card]
                check("4(b) no Remind / Edit / Worksheet / Set again / count on it", not bad,
                      "%r in %r" % (bad, card))
                check("4(b) it has Remove", "Remove" in card, card)

                # the page's own figures
                strip = lambda t: t.replace("Weekly challenge: Physics", "").replace("CLOSES FRI 23 OCT", "")
                for needle in ("11 of 16 in", "Class mean 64% · 86% on time", "NOT SUBMITTED SHOWN FIRST",
                               "Particle model — recall and apply"):
                    check("4(a) unchanged: %s" % needle, (needle in before) == (needle in after) and needle in after)
                # nothing else on the page moved: the text minus the card is identical
                b2 = [ln for ln in before.split("\n") if ln.strip()]
                a_lines = [ln for ln in after.split("\n") if ln.strip()]
                a2 = []
                taken = {"Weekly challenge: Physics": 1, "CLOSES FRI 23 OCT": 1, "Remove": 1}
                for ln in a_lines:
                    if taken.get(ln.strip(), 0) > 0:
                        taken[ln.strip()] -= 1
                        continue
                    a2.append(ln)
                check("4(a) every other line of the page is identical", b2 == a2,
                      "added %r, lost %r, order-equal %r" % ([x for x in a2 if x not in b2][:5], [x for x in b2 if x not in a2][:5], sorted(a2) == sorted(b2)))

                if shots:
                    from PIL import Image
                    for theme in ("light", "dark"):
                        page.eval("document.documentElement.setAttribute('data-theme', %s), 'ok'" % json.dumps(theme))
                        time.sleep(0.4)
                        y = page.eval("(function(){var e=document.querySelector('[data-mrb-added=\"challenge-card\"]');"
                                      "return e ? Math.round(e.getBoundingClientRect().top + window.scrollY) : 0})()")
                        out = os.path.join(shots, "teacher-challenge-card-%d-%s.png" % (w, theme))
                        page.screenshot(out, width=w, height=h, full_page=True)
                        im = Image.open(out)
                        top = max(0, y - 300)
                        im.crop((0, top, im.width, min(im.height, top + 760))).save(out)

                page.eval(CLICK_TEXT % json.dumps("Remove"))
                time.sleep(0.4)
                armed = page.eval(TEXT)
                check("4(c) first press arms", "Remove? Press again" in armed)
                check("4(c) and sends nothing", json.loads(page.eval("JSON.stringify(window.__reqs)")) == [])
                page.eval(CLICK_TEXT % json.dumps("Remove? Press again"))
                time.sleep(0.6)
                reqs = json.loads(page.eval("JSON.stringify(window.__reqs)"))
                check("4(c) second press sends DELETE /api/teacher/set-work/chal-1",
                      reqs == [{"url": "https://api.test/api/teacher/set-work/chal-1", "method": "DELETE"}],
                      repr(reqs))
    finally:
        server.shutdown()

    print("\n%s" % ("FAILED: %d" % len(fails) if fails else "all passed"))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
