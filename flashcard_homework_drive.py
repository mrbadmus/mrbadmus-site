#!/usr/bin/env python3
"""MRB-351 — drive a pupil through flashcard homework in the class page's
flashcard overlay (Design's one flashcard component, in homework mode).

    python3 flashcard_homework_drive.py            # everything, 390 and 360
    python3 flashcard_homework_drive.py --shots D  # screenshots into D

⚑ WHAT THIS PROVES, AND WHAT IT DOES NOT.

  It drives the COMPILED class page (`student/class-fixture.html`, Design's
  template with every ruling applied) and the REAL engine
  (`shared/flashcard-homework.js`) and formula renderer (`shared/formulae.js`).
  Only the transport is replaced: an in-page stand-in for
  `flashcard_record()` that keeps a deck's state the way the server does
  (made / known / secured / complete) and records every event it is sent.

  So it proves everything between the pupil's thumb and the event batch:
  the make phase (write → Check → the model answer beside theirs → rate),
  "Your deck is ready", the review queue order, Reveal, Space / 1·2·3,
  swipe, Finish for now, the secured panel, formulae as <sub>, the practice
  deck left exactly as Design drew it, and no sideways scroll at 390 or 360.

  It does NOT prove the server's arithmetic — durations, sittings, the
  60-minute secure rule, completion writing the submission. Those are proved
  in SQL on TEST under real roles (docs/mrb351/REPORT.md).
"""

import argparse
import json
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ks3_browser as cdp  # noqa: E402

ROOT = os.path.dirname(os.path.abspath(__file__))
AID = "aaaaaaaa-0000-4000-8000-000000000351"

# An in-page stand-in for `flashcard_record()`: the same state shape, the
# same completion idea (secure = got it when writing AND got it in review).
FAKE = r"""
(function () {
  var cards = [
    {id: "c0000000-0000-4000-8000-000000000001", position: 0, question: "What is the unit of force?", answer: "The newton (N)"},
    {id: "c0000000-0000-4000-8000-000000000002", position: 1, question: "What is the formula of water?", answer: "H2O"},
    {id: "c0000000-0000-4000-8000-000000000003", position: 2, question: "What is weight?", answer: "The force acting on an object due to gravity"},
    {id: "c0000000-0000-4000-8000-000000000004", position: 3, question: "Write the equation for the force on a spring.", answer: "Force = spring constant × extension (F = ke)"},
    {id: "c0000000-0000-4000-8000-000000000005", position: 4, question: "Is velocity a scalar or a vector?", answer: "A vector"}
  ].map(function (c) { return Object.assign({made: false, known: false, secured: false, last: null, mine: null, gm: false, gr: false}, c); });
  var S = window.__FC_FAKE__ = {events: [], calls: 0, complete: false};
  function state() {
    var made = 0, known = 0, secured = 0;
    cards.forEach(function (c) { if (c.made) made++; if (c.known) known++; if (c.secured) secured++; });
    return JSON.parse(JSON.stringify({assignment_id: "__AID__", title: "Forces flashcards", mode: "make",
      rule: "secure", n: cards.length, made: made, known: known, secured: secured, complete: S.complete,
      note: "Do these on your phone", cards: cards}));
  }
  S.transport = function (id, events) {
    S.calls++;
    (events || []).forEach(function (e) {
      S.events.push(e);
      var c = cards.filter(function (k) { return k.id === e.card; })[0];
      if (!c) return;
      if (e.type === "answer_submitted") { c.made = true; c.mine = e.answer; }
      if (e.type === "rated") {
        c.last = e.rating;
        if (e.rating === "got_it") {
          c.known = true;
          if (e.phase === "make") c.gm = true;
          else if (c.gr && S.later) c.gr2 = true;   // a second sitting, an hour on
          else c.gr = true;
        }
        c.secured = (c.gm && c.gr) || (c.gr && c.gr2);
      }
    });
    S.complete = cards.every(function (c) { return c.secured && c.made; });
    return new Promise(function (r) { setTimeout(function () { r(state()); }, 5); });
  };
})();
""".replace("__AID__", AID)

LOAD = r"""
(async function () {
  function add(src) { return new Promise(function (ok, bad) {
    var s = document.createElement('script'); s.src = src; s.onload = ok; s.onerror = bad; document.head.appendChild(s); }); }
  try { localStorage.clear(); } catch (e) {}
  await add('/shared/formulae.js');
  await add('/shared/flashcard-homework.js');
  window.MRBHomework.transport = window.__FC_FAKE__.transport;
  return !!window.__MRB_OPEN_HW__;
})()
"""

FAILS = []


def check(ok, what):
    print(("  PASS " if ok else "  FAIL ") + what)
    if not ok:
        FAILS.append(what)


def q(page, js):
    return page.eval(js)


def settle(t=0.35):
    time.sleep(t)


STATE_JS = r"""
(function () {
  var $ = function (s) { return document.querySelector(s); };
  var ov = $('[data-port-region="flashcards-overlay"]');
  var txt = function (s) { var e = $(s); return e ? e.innerText.trim() : null; };
  var flip = $('[data-dc-tpl="10333"]');
  var check = $('[data-hw="check"]');
  return {
    open: !!ov,
    strip: !!$('[data-hw="strip"]'),
    progress: txt('[data-hw="progress"]'),
    hint: txt('[data-hw="hint"]'),
    fresh: !!$('[data-hw="fresh"]'),
    note: !!$('[data-hw="note"]'),
    writing: !!$('[data-hw="answer"]'),
    checkDisabled: check ? check.disabled : null,
    rating: !!$('[data-hw="rate"]'),
    reveal: !!$('[data-hw="reveal"]'),
    finish: !!$('[data-hw="finish"]'),
    panel: txt('[data-hw="panel"]'),
    flipped: flip ? flip.getAttribute('data-flip') : null,
    tag: txt('[data-dc-tpl="10336"]'),
    front: txt('[data-dc-tpl="10340"]'),
    back: txt('[data-dc-tpl="10353"]'),
    backSubs: $('[data-dc-tpl="10353"]') ? $('[data-dc-tpl="10353"]').querySelectorAll('sub').length : 0,
    mine: txt('[data-hw="mine"]'),
    practiceRow: !!$('[data-dc-tpl="10362"]'),
    stackPos: txt('[data-dc-tpl="10324"]'),
    overflowX: document.documentElement.scrollWidth > window.innerWidth + 1
  };
})()
"""


def st(page):
    return q(page, STATE_JS)


def click(page, sel):
    return q(page, "(function(){var e=document.querySelector(%s); if(!e) return false; e.click(); return true;})()"
             % json.dumps(sel))


def type_answer(page, text):
    return q(page, """(function(){var t=document.querySelector('[data-hw="answer"]'); if(!t) return false;
      t.focus(); t.value=%s; t.dispatchEvent(new Event('input',{bubbles:true})); return true;})()""" % json.dumps(text))


def key(page, k):
    q(page, "document.dispatchEvent(new KeyboardEvent('keydown',{key:%s,bubbles:true}))" % json.dumps(k))


def swipe(page, dx):
    return q(page, """(function(){var c=document.querySelector('[data-dc-tpl="10333"]'); if(!c) return false;
      var r=c.getBoundingClientRect(), x=r.left+r.width/2, y=r.top+r.height/2;
      c.dispatchEvent(new PointerEvent('pointerdown',{clientX:x,clientY:y,bubbles:true}));
      c.dispatchEvent(new PointerEvent('pointerup',{clientX:x+%d,clientY:y+4,bubbles:true}));
      return true;})()""" % dx)


# The live page's after-draw hook (swipe, keyboard, fit) lives in
# student-live.js, which the fixture never loads; this is the same code
# path, registered here so the drive exercises it on the compiled template.
HOOKS = r"""
(function () {
  var H = window.MRBHomework;
  document.addEventListener("keydown", function (ev) {
    var e = H.active; if (!e || !document.querySelector('[data-hw="strip"]')) return;
    var tag = (ev.target && ev.target.tagName) || "";
    if (tag === "TEXTAREA" || tag === "INPUT") return;
    var v = e.view();
    if ((ev.key === " " || ev.key === "Enter") && v.phase === "review" && !v.revealed) { e.flip(); return; }
    if (v.revealed && v.card) { var r = {"1":"not_yet","2":"nearly","3":"got_it"}[ev.key]; if (r) e.rate(r); }
  });
  var overlayWasOpen = false;
  window.__MRB_AFTER_DRAW__ = window.__MRB_AFTER_DRAW__ || [];
  window.__MRB_AFTER_DRAW__.push(function (host) {
    var ov = host.querySelector('[data-port-region="flashcards-overlay"]');
    if (ov && overlayWasOpen) {
      ov.style.animation = "none";
      if (ov.firstElementChild) { ov.firstElementChild.style.animation = "none"; }
    }
    overlayWasOpen = !!ov;
  });
  window.__MRB_AFTER_DRAW__.push(function (host) {
    var card = host.querySelector('[data-dc-tpl="10333"]'), e = H.active;
    if (card && e && e.view().revealed) {
      var x0 = null, y0 = null;
      card.addEventListener("pointerdown", function (ev) { x0 = ev.clientX; y0 = ev.clientY; });
      card.addEventListener("pointerup", function (ev) {
        if (x0 === null) return; var dx = ev.clientX - x0, dy = ev.clientY - y0; x0 = null;
        if (Math.abs(dx) > 70 && Math.abs(dx) > 1.5 * Math.abs(dy)) { var g = H.active; if (g) g.rate(dx > 0 ? "got_it" : "not_yet"); }
      });
    }
  });
})();
"""

# The live hook must match this one — assert it, so the two cannot drift.
LIVE_MARKERS = ('"1": "not_yet", "2": "nearly", "3": "got_it"', 'Math.abs(dx) > 70 && Math.abs(dx) > 1.5 * Math.abs(dy)',
                'if (ov && overlayWasOpen) {')


def run(width, height, shots):
    print("\n── %d×%d ──" % (width, height))
    server, port = cdp.serve(ROOT)
    try:
        with cdp.Browser() as br:
            page = br.attach()
            page.set_viewport(width, height)
            page.send("Page.addScriptToEvaluateOnNewDocument", {"source": FAKE})
            page.goto("http://127.0.0.1:%d/student/class-fixture.html" % port)
            settle(1.0)
            check(q(page, LOAD) is True, "the page exposes window.__MRB_OPEN_HW__ once mounted")
            q(page, HOOKS)

            # ── the practice deck is Design's, untouched ────────────────
            click(page, '[data-port-region="sidebar-flashcards"] button')
            settle()
            s = st(page)
            check(s["open"] and s["practiceRow"] and not s["strip"],
                  "practice deck: Design's Reveal/Next row, no homework strip")
            click(page, '[data-port-region="flashcards-overlay"] button[title="Close"]')
            settle()

            # ── open the homework ────────────────────────────────────────
            q(page, "window.__MRB_OPEN_HW__(%s)" % json.dumps(AID))
            settle(0.6)
            s = st(page)
            check(s["open"] and s["strip"], "homework opens in the SAME overlay")
            check(s["progress"] == "Made 0 / 5", "strip reads 'Made 0 / 5' (got %r)" % s["progress"])
            check(s["tag"] == "HOMEWORK" and s["front"] == "What is the unit of force?", "card 1 question on Design's card")
            check(not s["practiceRow"], "Design's Reveal/Next row is hidden in homework mode")
            check(s["writing"] and s["checkDisabled"] is True, "answer box shown, Check disabled while empty")
            check(s["note"], "the teacher's note shows before the first rating")
            if shots:
                page.screenshot(os.path.join(shots, "hw-%d-1-write.png" % width), width=width, height=height, full_page=False)

            type_answer(page, "   ")
            settle()
            check(st(page)["checkDisabled"] is True, "Check stays disabled for spaces only")
            type_answer(page, "newton")
            settle()
            check(st(page)["checkDisabled"] is False, "Check enables after one non-space character")
            click(page, '[data-hw="check"]')
            settle()
            s = st(page)
            check(s["flipped"] == "1" and s["rating"] and not s["writing"],
                  "Check turns the card to the model answer and offers the three ratings")
            check("newton" in (s["mine"] or "") and s["back"] == "The newton (N)",
                  "the pupil's answer sits under the model answer")
            if shots:
                page.screenshot(os.path.join(shots, "hw-%d-2-checked.png" % width), width=width, height=height, full_page=False)
            click(page, '[data-hw="got_it"]')
            settle()
            s = st(page)
            check(s["progress"] == "Made 1 / 5" and s["front"] == "What is the formula of water?",
                  "Got it moves to card 2; strip reads Made 1 / 5")
            check(not s["note"], "the note goes once the pupil has started")

            type_answer(page, "idk")
            settle(0.2)
            click(page, '[data-hw="check"]')
            settle()
            s = st(page)
            check(s["backSubs"] == 1 and s["back"] == "H2O", "H2O renders with a real <sub> (text unchanged)")
            click(page, '[data-hw="not_yet"]')
            settle()
            for ans, r in (("gravity", "nearly"), ("F = ke", "got_it"), ("vector", "got_it")):
                type_answer(page, ans)
                settle(0.2)
                click(page, '[data-hw="check"]')
                settle(0.2)
                click(page, '[data-hw="%s"]' % r)
                settle(0.3)
            s = st(page)
            check(s["fresh"], "'YOUR DECK IS READY' when the last card is made")
            check(s["reveal"] and s["finish"] and not s["writing"], "review phase: Reveal and Finish for now")
            check(s["front"] == "What is the formula of water?",
                  "review queue starts with the Not yet card (got %r)" % s["front"])
            check((s["progress"] or "").endswith("of 5 secured"), "strip counts cards secured (got %r)" % s["progress"])
            if shots:
                page.screenshot(os.path.join(shots, "hw-%d-3-review.png" % width), width=width, height=height, full_page=False)

            key(page, " ")
            settle()
            check(st(page)["flipped"] == "1" and st(page)["rating"], "Space reveals the answer")
            key(page, "3")
            settle()
            s = st(page)
            check(s["front"] == "What is weight?", "3 = Got it, next is the Nearly card (got %r)" % s["front"])
            click(page, '[data-hw="reveal"]')
            settle()
            check(swipe(page, 120), "swipe dispatched")
            settle()
            s = st(page)
            check(s["front"] == "What is the unit of force?", "swipe right = Got it (got %r)" % s["front"])
            for _ in range(3):
                click(page, '[data-hw="reveal"]')
                settle(0.2)
                click(page, '[data-hw="got_it"]')
                settle(0.3)
            q(page, "window.MRBHomework.active.flush()")
            settle(0.6)
            s = st(page)
            check(s["panel"] is not None and "FOR NOW" in s["panel"] and "03 / 05" in s["panel"]
                  and s["hint"] == "Get every card right once more, later on" and "Go again" in s["panel"]
                  and "later on" not in s["panel"],
                  "queue empty, 2 cards not yet got right twice → FOR NOW 03 / 05 + the one hint + Go again (got %r)"
                  % s["panel"])
            if shots:
                page.screenshot(os.path.join(shots, "hw-%d-4-pause.png" % width), width=width, height=height, full_page=False)
            # An hour later: the next sitting's Got it secures the rest.
            q(page, "window.__FC_FAKE__.later = true")
            click(page, '[data-hw="again"]')
            settle()
            s = st(page)
            check(s["reveal"] and s["front"] == "What is the formula of water?",
                  "Go again starts a pass at the weakest card (got %r)" % s["front"])
            for _ in range(5):
                if not st(page)["reveal"]:
                    break
                click(page, '[data-hw="reveal"]')
                settle(0.2)
                click(page, '[data-hw="got_it"]')
                settle(0.3)
            q(page, "window.MRBHomework.active.flush()")
            settle(0.6)
            s = st(page)
            check(s["panel"] is not None and "DECK SECURED" in s["panel"] and "05 / 05" in s["panel"],
                  "every card secured → the themed panel: DECK SECURED 05 / 05 (got %r)" % s["panel"])
            check("Keep revising" in (s["panel"] or ""), "'Keep revising' stays available")
            if shots:
                page.screenshot(os.path.join(shots, "hw-%d-5-secured.png" % width), width=width, height=height, full_page=False)
            check(not s["overflowX"], "no sideways scroll at %dpx" % width)

            ev = q(page, "window.__FC_FAKE__.events")
            ids = [e["id"] for e in ev]
            types = [e["type"] for e in ev]
            check(len(ids) == len(set(ids)), "every event has its own id (idempotent resend)")
            check(types.count("answer_submitted") == 5 and types.count("session_finish") >= 1,
                  "5 answers written, and the pass ended with session_finish")
            check(all(isinstance(e.get("at"), (int, float)) and "visible" in e for e in ev),
                  "every event carries the device clock and visibility")
            check(not any("think_ms" in e or "active_ms" in e for e in ev),
                  "no event carries a duration — the server computes them")

            click(page, '[data-hw="keep"]')
            settle()
            s = st(page)
            check(s["reveal"] and not s["panel"], "Keep revising starts another pass")
            click(page, '[data-port-region="flashcards-overlay"] button[title="Close"]')
            settle()
            check(not st(page)["open"], "Close ends the sitting and closes the overlay")
    finally:
        server.shutdown()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--shots", default=None)
    a = ap.parse_args()
    shots = a.shots or cdp.gate_tmp()
    os.makedirs(shots, exist_ok=True)
    live = open(os.path.join(ROOT, "shared", "student-live.js"), encoding="utf-8").read()
    check(all(m in live for m in LIVE_MARKERS), "the live page's swipe/keyboard hook is the one driven here")
    for w, h in ((390, 844), (360, 780)):
        run(w, h, shots)
    print("\n  screenshots: %s" % shots)
    if FAILS:
        print("\n  FAIL — %d check(s) failed" % len(FAILS))
        sys.exit(1)
    print("\n  PASS — flashcard homework, in Design's one flashcard component")


if __name__ == "__main__":
    main()
