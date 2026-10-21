#!/usr/bin/env python3
"""weekly_challenge_class_drive.py -- Unit C: the weekly-challenge row on the
PUPIL class page, rendered by the real ported template.

    python3 weekly_challenge_class_drive.py [--shots DIR]

Exit 0 clean, 1 on any failure.

Drives `student/class-fixture.html` (Design's own example class, mounted by the
same runtime and the same rulings as the live page) and adds three
`weekly_challenge` rows to its `work` list in the exact shape
`weeklyChallengeRows()` in shared/student-live.js produces -- one open, one
played, one closed unplayed -- then re-renders. It asserts, on VISIBLE TEXT:

  3(a)  every number the page already drew is UNCHANGED: Handed in, On time,
        Avg score and the "N MARKED" caption; the Marked tab; the bench.
  3(b)  the rows read "Weekly challenge: Physics", say PLAYED / CLOSED / a due
        date, and never MISSED, MARKED, late, a question count or a score;
        the open row's one button reads "Play the challenge" and goes to
        /weekly-challenge.html?subject=physics.
  3(c)  no Start/answer/flashcard affordance on any of them.

The fixture is never edited: the rows are added in the page, at run time, so
`student_behaviour`'s comparison against Design's own file is untouched.
"""

import json
import os
import sys
import time

REPO = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, REPO)
os.chdir(REPO)

import ks3_browser as cdp

SITE = "mrbadmus_site"
PATH = "student/class-fixture.html"

ADD_ROWS = """(function () {
  var d = window.__MRB_DATA__;
  var base = { wc: true, brief: '', lessons: [], lessonHref: '', noClose: true, week: 4,
               assignmentHref: '/weekly-challenge.html?subject=physics' };
  d.work.push(Object.assign({}, base, { id: 'wc-open', title: 'Weekly challenge: Physics',
    status: 'open', played: false, detail: 'DUE FRI 23 OCT, 10:15' }));
  d.work.push(Object.assign({}, base, { id: 'wc-played', title: 'Weekly challenge: Biology',
    status: 'closed', played: true, detail: 'DUE FRI 23 OCT, 10:15',
    assignmentHref: '/weekly-challenge.html?subject=biology' }));
  d.work.push(Object.assign({}, base, { id: 'wc-closed', title: 'Weekly challenge: Chemistry',
    status: 'closed', played: false, detail: 'DUE FRI 23 OCT, 10:15',
    assignmentHref: '/weekly-challenge.html?subject=chemistry' }));
  return d.work.length;
})()"""

# What the page already said, before the rows exist.
READ = """(function () {
  var root = document.querySelector('.rd[data-mode="ks3"]');
  var t = root.innerText;
  var tabs = Array.prototype.map.call(root.querySelectorAll('button'), function (b) {
    return (b.innerText || '').trim();
  }).filter(function (x) { return /^(ALL|TO DO|MARKED) \\d+$/i.test(x); });
  var line = function (re) { var m = re.exec(t); return m ? m[0] : null; };
  return JSON.stringify({
    tabs: tabs,
    handed: line(/HANDED IN[\\s\\S]{0,40}/i), onTime: line(/ON TIME[\\s\\S]{0,40}/i),
    avg: line(/AVG SCORE[\\s\\S]{0,60}/i), text: t });
})()"""

CLICK_TAB = """(function (name) {
  var root = document.querySelector('.rd[data-mode="ks3"]');
  var hit = null;
  root.querySelectorAll('button').forEach(function (b) {
    if (!hit && (b.innerText || '').trim().toUpperCase().indexOf(name.toUpperCase()) === 0 && /\\d+$/.test((b.innerText || '').trim())) { hit = b; }
  });
  if (!hit) { return 'MISS'; }
  hit.click(); return 'ok';
})(%s)"""

# Open a row by its title; returns the text of its expanded body and what its
# primary button is called and where it goes.
OPEN_ROW = """(function (title) {
  var root = document.querySelector('.rd[data-mode="ks3"]');
  var hit = null;
  root.querySelectorAll('button').forEach(function (e) {
    if (!hit && (e.innerText || '').indexOf(title) > -1) { hit = e; }
  });
  if (!hit) { return 'MISS'; }
  hit.click(); return 'ok';
})(%s)"""

ROW_TEXT = """(function (title) {
  var root = document.querySelector('.rd[data-mode="ks3"]');
  var out = null;
  root.querySelectorAll('button').forEach(function (e) {
    if (out === null && (e.innerText || '').indexOf(title) > -1) {
      var box = e.parentElement;
      out = (box.innerText || '');
    }
  });
  return out;
})(%s)"""

CLICK_PRIMARY = """(function (title) {
  var root = document.querySelector('.rd[data-mode="ks3"]');
  var row = null;
  root.querySelectorAll('button').forEach(function (e) {
    if (!row && (e.innerText || '').indexOf(title) > -1) { row = e.parentElement; }
  });
  if (!row) { return 'MISS'; }
  var btns = row.querySelectorAll('button');
  var label = null;
  btns.forEach(function (b) {
    var t = (b.innerText || '').trim();
    if (label === null && /^(Play the challenge|Open the challenge)$/.test(t)) { label = t; window.__clicked = b; }
  });
  return label;
})(%s)"""


def shoot(page, shots, name, w, h, title):
    """The work list around the row, light then dark: a full-page capture
    (the page scrolls inside the document), cropped to the list."""
    from PIL import Image
    for theme in ("light", "dark"):
        page.eval("document.documentElement.setAttribute('data-theme', %s), 'ok'" % json.dumps(theme))
        time.sleep(0.4)
        y = page.eval("""(function (t) {
          var r = document.querySelector('.rd[data-mode="ks3"]'), hit = null;
          r.querySelectorAll('button').forEach(function (b) {
            if (!hit && (b.innerText || '').indexOf(t) > -1) { hit = b; }
          });
          return hit ? Math.round(hit.getBoundingClientRect().top + window.scrollY) : 0;
        })(%s)""" % json.dumps(title))
        out = os.path.join(shots, "%s-%d-%s.png" % (name, w, theme))
        page.screenshot(out, width=w, height=h, full_page=True)
        im = Image.open(out)
        top = max(0, y - 260)
        im.crop((0, top, im.width, min(im.height, top + 760))).save(out)


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

    server, port = cdp.serve(SITE)
    url = "http://127.0.0.1:%d/%s" % (port, PATH)
    try:
        with cdp.Browser() as b:
            page = b.attach()
            for (w, h) in ((390, 844), (1280, 900)):
                print("\nviewport %dx%d" % (w, h))
                page.set_viewport(w, h)
                page.goto(url)
                time.sleep(2.6)
                before = json.loads(page.eval(READ))
                page.eval(ADD_ROWS)
                page.eval(CLICK_TAB % json.dumps("All"))
                time.sleep(0.6)
                after = json.loads(page.eval(READ))

                check("3(a) Handed in tile unchanged", before["handed"] == after["handed"],
                      "%r -> %r" % (before["handed"], after["handed"]))
                check("3(a) On time tile unchanged", before["onTime"] == after["onTime"],
                      "%r -> %r" % (before["onTime"], after["onTime"]))
                check("3(a) Avg score tile + MARKED caption unchanged", before["avg"] == after["avg"],
                      "%r -> %r" % (before["avg"], after["avg"]))
                bt = {t.split(" ")[0] + (" do" if t.startswith("To") else ""): t for t in before["tabs"]}
                nums = lambda tabs: [int(t.rsplit(" ", 1)[1]) for t in tabs]
                bn, an = nums(before["tabs"]), nums(after["tabs"])
                check("tabs: All +3, To do +1, Marked +0",
                      len(bn) == 3 and an == [bn[0] + 3, bn[1] + 1, bn[2]],
                      "%r -> %r" % (before["tabs"], after["tabs"]))

                txt = after["text"]
                for title, word in (("Weekly challenge: Physics", None),
                                    ("Weekly challenge: Biology", "PLAYED"),
                                    ("Weekly challenge: Chemistry", "CLOSED")):
                    check("3(b) row present: %s" % title, title in txt)
                    if word:
                        seg = txt[txt.index(title):txt.index(title) + 160] if title in txt else ""
                        check("3(b) %s reads %s" % (title.split(": ")[1], word),
                              word in seg, seg)
                # The three rows' own text may not carry marking vocabulary.
                rows = [page.eval(ROW_TEXT % json.dumps(t)) for t in
                        ("Weekly challenge: Physics", "Weekly challenge: Biology",
                         "Weekly challenge: Chemistry")]
                joined = "\n".join(r or "" for r in rows)
                bad = [w_ for w_ in ("MISSED", "MARKED", "LATE", "late", "questions", "OF 0 ANSWERED",
                                     "NaN", "undefined", "Start", "Handed in")
                       if w_ in joined]
                check("3(b) no MISSED / MARKED / late / questions / score on any of them",
                      not bad, "found %r in %r" % (bad, joined[:300]))

                # open the Physics row, read its one button, press it.
                check("open row expands", page.eval(OPEN_ROW % json.dumps("Weekly challenge: Physics")) == "ok")
                time.sleep(0.4)
                lab = page.eval(CLICK_PRIMARY % json.dumps("Weekly challenge: Physics"))
                check("3(b) open row's button reads 'Play the challenge'", lab == "Play the challenge", repr(lab))
                if shots:
                    shoot(page, shots, "pupil-challenge-open", w, h, "Weekly challenge: Physics")
                page.eval("window.__clicked && window.__clicked.click(), 'x'")
                time.sleep(0.6)
                loc = page.eval("location.pathname + location.search")
                check("3(b) it goes to /weekly-challenge.html?subject=physics",
                      loc == "/weekly-challenge.html?subject=physics", repr(loc))

                page.goto(url)
                time.sleep(2.6)
                page.eval(ADD_ROWS)
                page.eval(CLICK_TAB % json.dumps("All"))
                time.sleep(0.6)
                page.eval(OPEN_ROW % json.dumps("Weekly challenge: Biology"))
                time.sleep(0.4)
                lab = page.eval(CLICK_PRIMARY % json.dumps("Weekly challenge: Biology"))
                check("a played row's button reads 'Open the challenge'", lab == "Open the challenge", repr(lab))
                if shots:
                    shoot(page, shots, "pupil-challenge-done", w, h, "Weekly challenge: Biology")
    finally:
        server.shutdown()

    print("\n%s" % ("FAILED: %d" % len(fails) if fails else "all passed"))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
