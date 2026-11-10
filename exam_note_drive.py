#!/usr/bin/env python3
"""exam_note_drive.py — an exam result accounts for every scheme point ONCE.

B2C small fixes (26 Oct 2026). Since the backend's 9b96370 the examiner's
note ends with one "Point N: got it — …" / "Point N: not yet — …" line per
scheme point (consumer/point-account.js), and `/api/consumer/mark` also
returns `points: [{n, earned, text}]`. consumer/exam.html already draws a
tick list of the points, so showing the note whole said every point twice
(Mide's no-redundant-text rule). The page now shows the marker's own words
in the note and the account once, as the tick list.

On the BUILT consumer/exam.html, with `MrBadmusConsumer.boot` and `.api`
replaced by fixtures before the page's own script runs (no session, no
network: every request off 127.0.0.1 is blocked), at 390x844 and 1280x900:

  A  STORED ANSWER (?q=, a done question: scheme + hits + a stored note with
     the account and a trailing "Final answer checked" line):
       · the note shows the marker's words and the trailing line, and no
         "Point N:" line at all;
       · the tick list has one row per scheme point, in order, ticked
         exactly where `hits` says, each row's text present once on screen.
  B  FRESH MARK (write, press Mark; the fixture answers with `points`):
       · the list follows `points` (earned → ticked), in order;
       · the note has no "Point N:" line, and each point text appears once.
  C  NO SCHEME (a stored answer whose question has no scheme): no list is
     drawn, so the note keeps its account whole — the facts are not lost.

Run:  python3 exam_note_drive.py [--shots DIR]
"""

import argparse
import json
import os
import sys
import time

import ks3_browser as cdp

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "mrbadmus_site")
PAGE = "/consumer/exam.html"
SIZES = [(390, 844), (1280, 900)]
BLOCK = ["https://*", "wss://*", "http://localhost*"]
FAILS = []

P1 = "Diffusion is the net movement of particles from high to low concentration"
P2 = "Oxygen diffuses from the alveoli into the blood"
P3 = "The alveoli give a large surface area"
STORED_NOTE = ("You explained diffusion clearly; say where the oxygen goes.\n"
               "Point 1: got it — %s.\nPoint 2: not yet — %s.\nPoint 3: got it — %s.\n"
               "Final answer checked against the mark scheme." % (P1, P2, P3))
FRESH_NOTE = ("Good start. Name the blood vessel next time.\n"
              "Point 1: not yet — %s.\nPoint 2: got it — %s.\nPoint 3: not yet — %s." % (P1, P2, P3))

QUESTIONS = [
    dict(id="drv-1", subject="Biology", topic="Organisation", marks=3, text="Explain how oxygen reaches the blood.",
         scheme=[P1, P2, P3], done=True, answer="Oxygen diffuses into the blood.", aiScore="2/3",
         hits=[0, 2], feedback=STORED_NOTE, verdict="nearly there"),
    dict(id="drv-2", subject="Biology", topic="Organisation", marks=3, text="Explain gas exchange in the lungs.",
         scheme=[P1, P2, P3], done=False),
    dict(id="drv-3", subject="Biology", topic="Organisation", marks=2, text="Describe diffusion.",
         scheme=[], done=True, answer="Particles spread out.", aiScore="1/2", hits=[0],
         feedback="Close.\nPoint 1: got it — %s.\nPoint 2: not yet — %s." % (P1, P2), verdict="halfway"),
]
MARK = dict(ok=True, answer_id="a-2", score=1, max=3, hits=[1],
            points=[dict(n=1, earned=False, text=P1), dict(n=2, earned=True, text=P2),
                    dict(n=3, earned=False, text=P3)],
            feedback=FRESH_NOTE, verdict="halfway", provider="claude", quotaLeft=2, quotaTotal=2)

STUB = r"""
(function () {
  var QS = %s, MARK = %s;
  var real;
  function patch(C) {
    C.boot = function (o) { setTimeout(function () { o.run({ token: 'stub', sb: null }); }, 0); };
    C.api = function (path, opts) {
      if (path.indexOf('/api/consumer/child/exam-questions') === 0) {
        return Promise.resolve({ questions: JSON.parse(JSON.stringify(QS)), quotaLeft: 2, quotaTotal: 2,
                                 resetDate: '1 November', access: { state: 'active' } });
      }
      if (path.indexOf('/api/consumer/mark') === 0) {
        QS[1].done = true;
        return Promise.resolve(JSON.parse(JSON.stringify(MARK)));
      }
      return Promise.reject({ status: 404, message: 'stub: ' + path });
    };
    C.guard = function () { return { writable: true }; };
    return C;
  }
  Object.defineProperty(window, 'MrBadmusConsumer', {
    configurable: true,
    get: function () { return real; },
    set: function (v) { real = patch(v); }
  });
})();
""" % (json.dumps(QUESTIONS), json.dumps(MARK))

READ = r"""
(function () {
  var main = document.getElementById('ex-main');
  var note = main && main.querySelector('.ex-note p:last-child');
  var rows = Array.prototype.map.call(main ? main.querySelectorAll('.ex-point') : [], function (li) {
    return { hit: li.classList.contains('is-hit'),
             text: li.querySelector('.ex-point-text').textContent };
  });
  // The marking's account, without "You wrote": the child's own words may
  // repeat a scheme point word for word (B's answer does), and that is the
  // child's answer, not a second account of the point.
  var text = main ? main.innerText : '', wrote = main && main.querySelector('.ex-wrote');
  if (wrote) { text = text.replace(wrote.innerText, ''); }
  return { note: note ? note.textContent : null, rows: rows,
           text: text, result: !!(main && main.querySelector('.ex-score')) };
})()
"""


def fail(msg):
    FAILS.append(msg)
    print("  FAIL  " + msg)


def ok(msg):
    print("  ok    " + msg)


def check(cond, msg):
    (ok if cond else fail)(msg)


def wait_result(page, timeout=8.0):
    end = time.time() + timeout
    while time.time() < end:
        r = page.eval(READ)
        if r and r["result"]:
            return r
        time.sleep(0.2)
    return page.eval(READ)


def count(hay, needle):
    return hay.count(needle)


def drive(b, base, size, shots):
    w, h = size
    tag = "%dx%d" % size
    page = b.attach()
    page.send("Network.enable")
    page.send("Network.setBlockedURLs", {"urls": BLOCK})
    page.send("Page.addScriptToEvaluateOnNewDocument", {"source": STUB})
    page.set_viewport(w, h)

    # A — stored answer
    page.goto(base + PAGE + "?q=drv-1", settle=1.5)
    r = wait_result(page)
    check(r["result"], "%s A: the result screen is drawn" % tag)
    check(r["note"] is not None and "Point " not in r["note"]
          and "You explained diffusion clearly" in r["note"] and "Final answer checked" in r["note"],
          "%s A: note keeps the marker's words and the trailing line, no Point lines: %r" % (tag, r["note"]))
    check([x["hit"] for x in r["rows"]] == [True, False, True],
          "%s A: three rows ticked where hits say: %s" % (tag, [x["hit"] for x in r["rows"]]))
    check(all(count(r["text"], p) == 1 for p in (P1, P2, P3)),
          "%s A: each point's text is on screen exactly once: %s" % (tag, [count(r["text"], p) for p in (P1, P2, P3)]))
    check([x["text"] for x in r["rows"]] == ["Got it: " + P1, "Not yet: " + P2, "Got it: " + P3],
          "%s A: each row carries its verdict for a screen reader" % tag)
    if shots:
        page.screenshot(os.path.join(shots, "exam-result-%d.png" % w), width=w, height=h, full_page=True)

    # B — a fresh mark carrying `points`
    page.goto(base + PAGE + "?q=drv-2", settle=1.5)
    page.eval("var t=document.getElementById('ex-answer'); t.value='Oxygen diffuses from the alveoli into the "
              "blood capillaries.'; t.dispatchEvent(new Event('input',{bubbles:true})); 1")
    time.sleep(0.2)
    page.eval("document.getElementById('ex-mark').click(); 1")
    r = wait_result(page)
    check(r["result"], "%s B: the result screen is drawn after Mark" % tag)
    check([x["hit"] for x in r["rows"]] == [False, True, False],
          "%s B: the list follows points[] (earned -> ticked): %s" % (tag, [x["hit"] for x in r["rows"]]))
    check(r["note"] == "Good start. Name the blood vessel next time.",
          "%s B: the note is the marker's words only: %r" % (tag, r["note"]))
    check(all(count(r["text"], p) == 1 for p in (P1, P2, P3)),
          "%s B: each point's text is on screen exactly once" % tag)

    # C — no scheme: the note's own account is the only one, so it stays
    page.goto(base + PAGE + "?q=drv-3", settle=1.5)
    r = wait_result(page)
    check(not r["rows"] and r["note"] and "Point 1: got it" in r["note"] and "Point 2: not yet" in r["note"],
          "%s C: no list, so the note keeps its account: %r" % (tag, r["note"]))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--shots", default=None)
    a = ap.parse_args()
    shots = a.shots or os.path.join(cdp.gate_tmp(), "exam_note_drive")
    os.makedirs(shots, exist_ok=True)
    if not os.path.exists(OUT + PAGE):
        print("missing built page %s — run build_all.py first" % PAGE)
        return 2
    server, port = cdp.serve(OUT)
    base = "http://127.0.0.1:%d" % port
    try:
        for size in SIZES:
            print("\nexam.html at %dx%d" % size)
            with cdp.Browser() as b:
                drive(b, base, size, shots)
    finally:
        server.shutdown()
    print("\nscreenshots: %s" % shots)
    print("FAILED: %d" % len(FAILS) if FAILS else "exam_note_drive: all checks passed")
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main())
