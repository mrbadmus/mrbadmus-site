#!/usr/bin/env python3
"""MRB-351 pupil flow — drive a pupil through flashcard homework in the class
page's flashcard overlay (Design's one flashcard component, in homework
mode), on a PHONE, with the keyboard up.

    python3 flashcard_homework_drive.py            # everything, both phones
    python3 flashcard_homework_drive.py --shots D  # screenshots into D

⚑ WHAT THIS PROVES, AND WHAT IT DOES NOT.

  It drives the COMPILED class page (`student/class-fixture.html`, Design's
  template with every ruling applied) and the REAL engine
  (`shared/flashcard-homework.js`), keyboard module
  (`shared/flashcard-keyboard.js`) and formula renderer (`shared/formulae.js`).
  Only the transport and the model check are replaced: an in-page stand-in for
  `flashcard_record()` that keeps a deck's state the way the server does, and
  a model check that answers when told to.

  THE PHONE (docs/mrb351/PUPIL-FLOW.md §9.2 + A11). Device metrics are set to
  390×844 (then 360×740) with `mobile: true` and NEVER shrunk — iOS Safari and
  Android Chrome do not shrink the layout viewport for the keyboard, and a
  drive that did would test a phone nobody owns. Instead a fake
  `window.visualViewport` is installed before the page loads, and "the
  keyboard comes up" is its height dropping to 508 (404 at 360×740) and a
  `resize` event. At every state with the keyboard up, the question text's
  and the answer box's bounding boxes must sit inside the visual viewport and
  Check must be visible (the element at its centre IS Check).

  Both modes (make: the writing pass, its end screen, the review pass; review:
  one sitting), every state (A question, keyboard up, B checking, C verdict,
  ‹ Back, I don't know, the end screens, a second sitting, secured), and the
  retired words absent from the page throughout.

  It does NOT prove the server's arithmetic — durations, sittings, the
  60-minute secure rule, completion writing the submission. Those are proved
  on TEST with the real database (tools/mrb351_pupil_flow_live.py) and in
  flashcard_engine_test.js.
"""

import argparse
import base64
import json
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ks3_browser as cdp  # noqa: E402

ROOT = os.path.dirname(os.path.abspath(__file__))
AID = "aaaaaaaa-0000-4000-8000-000000000351"

# An in-page stand-in for `flashcard_record()`: the same state shape, the
# same completion idea (secure = got it when writing AND got it in review, or
# got it in two review sittings an hour apart — `later` says the hour passed).
FAKE = r"""
(function () {
  var cards = [
    {id: "c0000000-0000-4000-8000-000000000001", position: 0, question: "What is the unit of force?", answer: "The newton (N)"},
    {id: "c0000000-0000-4000-8000-000000000002", position: 1, question: "What is the formula of water?", answer: "H2O"},
    {id: "c0000000-0000-4000-8000-000000000003", position: 2, question: "What is weight?", answer: "The force acting on an object due to gravity"},
    {id: "c0000000-0000-4000-8000-000000000004", position: 3, question: "Write the equation for the force on a spring.", answer: "Force = spring constant × extension (F = ke)"},
    {id: "c0000000-0000-4000-8000-000000000005", position: 4, question: "Is velocity a scalar or a vector?", answer: "A vector"}
  ].map(function (c) { return Object.assign({made: false, known: false, secured: false, last: null, mine: null, gm: false, gr: false}, c); });
  var S = window.__FC_FAKE__ = {events: [], calls: 0, complete: false, mode: "make", sittings: 0, open: false};
  function state() {
    var made = 0, known = 0, secured = 0;
    cards.forEach(function (c) { if (c.made) made++; if (c.known) known++; if (c.secured) secured++; });
    return JSON.parse(JSON.stringify({assignment_id: "__AID__", title: "Forces flashcards", mode: S.mode,
      rule: "secure", n: cards.length, made: made, known: known, secured: secured, complete: S.complete,
      sittings: S.sittings, session_id: null, note: "Do these on your phone", cards: cards}));
  }
  S.transport = function (id, events) {
    S.calls++;
    (events || []).forEach(function (e) {
      S.events.push(e);
      if (!S.open && e.type !== "visibility") { S.open = true; S.sittings++; }
      if (e.type === "session_finish") { S.open = false; }
      var c = cards.filter(function (k) { return k.id === e.card; })[0];
      if (!c) return;
      if (e.type === "answer_submitted" && e.phase === "make") { c.made = true; if (c.mine == null) c.mine = e.answer; }
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
    S.complete = cards.every(function (c) { return c.secured && (S.mode !== "make" || c.made); });
    return new Promise(function (r) { setTimeout(function () { r(state()); }, 5); });
  };
})();
""".replace("__AID__", AID)

# The phone keyboard, as the browser reports it: only `visualViewport` moves.
FAKE_VV = r"""
(function () {
  var h = null, top = 0, ls = {};
  var fake = {
    get width() { return window.innerWidth; },
    get height() { return h == null ? window.innerHeight : h; },
    get offsetTop() { return top; },
    offsetLeft: 0, pageLeft: 0, get pageTop() { return window.scrollY + top; }, scale: 1,
    addEventListener: function (t, f) { (ls[t] = ls[t] || []).push(f); },
    removeEventListener: function (t, f) { ls[t] = (ls[t] || []).filter(function (g) { return g !== f; }); },
    dispatchEvent: function () { return true; }
  };
  Object.defineProperty(window, "visualViewport", {configurable: true, get: function () { return fake; }});
  window.__KB__ = function (height) {
    h = height; top = 0;
    (ls.resize || []).forEach(function (f) { try { f({type: "resize"}); } catch (e) {} });
  };
})();
"""

LOAD = r"""
(async function () {
  function add(src) { return new Promise(function (ok, bad) {
    var s = document.createElement('script'); s.src = src; s.onload = ok; s.onerror = bad; document.head.appendChild(s); }); }
  try { localStorage.clear(); } catch (e) {}
  await add('/shared/formulae.js');
  await add('/shared/flashcard-homework.js');
  await add('/shared/flashcard-keyboard.js');
  window.MRBHomework.transport = window.__FC_FAKE__.transport;
  window.MRBHomework.modelCheck = function () {
    return new Promise(function (r) { window.__MODEL__ = r; });
  };
  return !!window.__MRB_OPEN_HW__;
})()
"""

RETIRED = ("FOR NOW", "Go again", "Made ", "later on", "Finish for now", "Compare it yourself",
           "Not quite", "Keep revising", "YOUR DECK IS READY", "DECK SECURED")

FAILS = []


def check(ok, what):
    print(("  PASS " if ok else "  FAIL ") + what)
    if not ok:
        FAILS.append(what)


def settle(t=0.3):
    time.sleep(t)


STATE_JS = r"""
(function () {
  var $ = function (s) { return document.querySelector(s); };
  var ov = $('[data-port-region="flashcards-overlay"]');
  var txt = function (s) { var e = $(s); return e ? e.innerText.trim() : null; };
  var flip = $('[data-dc-tpl="10333"]');
  var check = $('[data-hw="check"]');
  var ta = $('[data-hw="answer"]');
  var strip = $('[data-hw="strip"]');
  var dlg = $('[data-mrb-dialog="flashcards"]');
  var pressed = Array.prototype.map.call(document.querySelectorAll('[data-hw="rate"] button[aria-pressed="true"]'),
                                         function (b) { return b.getAttribute('data-hw'); });
  return {
    open: !!ov,
    strip: !!strip,
    stripShown: !!strip && strip.getBoundingClientRect().height > 0,
    progress: txt('[data-hw="progress"]'),
    segs: document.querySelectorAll('[data-hw="seg"]').length,
    secured: txt('[data-hw="secured"]'),
    hint: txt('[data-hw="strip"] [data-hw="hint"]'),
    note: !!$('[data-hw="note"]'),
    writing: !!ta,
    draft: ta ? ta.value : null,
    focused: !!ta && document.activeElement === ta,
    typing: dlg ? dlg.getAttribute('data-hw-typing') : null,
    checkDisabled: check ? check.disabled : null,
    back: !!$('[data-hw="back"]'),
    idk: !!$('[data-hw="idk"]'),
    rating: !!$('[data-hw="rate"]'),
    chip: txt('[data-hw="chip"]'),
    pressed: pressed,
    panel: txt('[data-hw="panel"]'),
    end1: txt('[data-hw="end1"]'),
    end2: txt('[data-hw="end2"]'),
    endHint: txt('[data-hw="panel"] [data-hw="hint"]'),
    again: txt('[data-hw="again"]'),
    done: txt('[data-hw="done"]'),
    flipped: flip ? flip.getAttribute('data-flip') : null,
    tag: txt('[data-dc-tpl="10336"]'),
    front: txt('[data-dc-tpl="10340"]'),
    back_: txt('[data-dc-tpl="10353"]'),
    backSubs: $('[data-dc-tpl="10353"]') ? $('[data-dc-tpl="10353"]').querySelectorAll('sub').length : 0,
    mine: txt('[data-hw="mine"]'),
    pips: !!$('[data-pip-row]'),
    practiceRow: !!$('[data-dc-tpl="10362"]'),
    stackPos: txt('[data-dc-tpl="10324"]'),
    text: ov ? ov.innerText : '',
    overflowX: document.documentElement.scrollWidth > window.innerWidth + 1
  };
})()
"""

# §6 acceptance: inside [offsetTop, offsetTop + height] of the VISUAL viewport.
BOXES_JS = r"""
(function () {
  var vv = window.visualViewport, top = vv.offsetTop, bot = vv.offsetTop + vv.height;
  function box(sel) {
    var e = document.querySelector(sel); if (!e) return null;
    var r = e.getBoundingClientRect(); return {top: r.top, bottom: r.bottom, h: r.height};
  }
  var q = box('[data-dc-tpl="10340"]'), t = box('[data-hw="answer"]'), c = document.querySelector('[data-hw="check"]');
  var cr = c ? c.getBoundingClientRect() : null;
  var hit = cr ? document.elementFromPoint(cr.left + cr.width / 2, cr.top + cr.height / 2) : null;
  return {vv: [top, bot], q: q, t: t,
          qIn: !!q && q.h > 0 && q.top >= top - 0.5 && q.bottom <= bot + 0.5,
          tIn: !!t && t.h > 0 && t.top >= top - 0.5 && t.bottom <= bot + 0.5,
          checkVisible: !!cr && cr.top >= top - 0.5 && cr.bottom <= bot + 0.5 && !!hit && (hit === c || c.contains(hit))};
})()
"""


class Phone:
    def __init__(self, page, width, height, kb, shots):
        self.page, self.w, self.h, self.kb, self.shots = page, width, height, kb, shots
        self.n = 0

    def q(self, js):
        return self.page.eval(js)

    def st(self):
        return self.q(STATE_JS)

    def click(self, sel):
        ok = self.q("(function(){var e=document.querySelector(%s); if(!e) return false; e.click(); return true;})()"
                    % json.dumps(sel))
        settle()
        return ok

    def type(self, text):
        ok = self.q("""(function(){var t=document.querySelector('[data-hw="answer"]'); if(!t) return false;
          t.focus(); t.value=%s; t.dispatchEvent(new Event('input',{bubbles:true})); return true;})()""" % json.dumps(text))
        settle(0.25)
        return ok

    def keyboard(self, up):
        if up:
            self.q("(function(){var t=document.querySelector('[data-hw=\"answer\"]'); if(t) t.focus();})()")
        self.q("window.__KB__(%s)" % (self.kb if up else "null"))
        settle(0.45)

    def shot(self, name):
        if not self.shots:
            return
        self.n += 1
        res = self.page.send("Page.captureScreenshot", {"format": "png", "fromSurface": True})
        path = os.path.join(self.shots, "hw-%d-%02d-%s.png" % (self.w, self.n, name))
        with open(path, "wb") as fh:
            fh.write(base64.b64decode(res["data"]))

    def boxes(self, what):
        b = self.q(BOXES_JS)
        check(b["qIn"] and b["tIn"] and b["checkVisible"],
              "%d×%d keyboard up (visual %d) at %s: question text and answer box inside the visual "
              "viewport, Check visible (q=%s t=%s check=%s)"
              % (self.w, self.h, self.kb, what, b["q"], b["t"], b["checkVisible"]))

    def no_retired(self, where):
        t = self.st()["text"]
        bad = [w for w in RETIRED if w in t]
        check(not bad, "no retired words on screen at %s (%s)" % (where, bad))


def run(width, height, kb, shots):
    print("\n── %d×%d, keyboard %d ──" % (width, height, kb))
    server, port = cdp.serve(ROOT)
    try:
        with cdp.Browser() as br:
            page = br.attach()
            page.send("Emulation.setDeviceMetricsOverride",
                      {"width": width, "height": height, "deviceScaleFactor": 2, "mobile": True})
            page.send("Emulation.setTouchEmulationEnabled", {"enabled": True, "maxTouchPoints": 5})
            try:
                page.send("Emulation.setFocusEmulationEnabled", {"enabled": True})
            except cdp.CDPError:
                pass
            page.send("Page.addScriptToEvaluateOnNewDocument", {"source": FAKE})
            page.send("Page.addScriptToEvaluateOnNewDocument", {"source": FAKE_VV})
            page.goto("http://127.0.0.1:%d/student/class-fixture.html" % port)
            settle(1.0)
            P = Phone(page, width, height, kb, shots)
            check(P.q(LOAD) is True, "the page exposes window.__MRB_OPEN_HW__ once mounted")
            check(P.q("window.innerHeight") == height and P.q("window.visualViewport.height") == height,
                  "layout viewport %d, keyboard down" % height)

            # ── the practice deck is Design's, untouched ────────────────
            P.click('[data-port-region="sidebar-flashcards"] button')
            s = P.st()
            check(s["open"] and s["practiceRow"] and not s["strip"] and s["pips"],
                  "practice deck: Design's Reveal/Next row and pip row, no homework strip")
            P.click('[data-port-region="flashcards-overlay"] button[title="Close"]')

            # ══ MAKE MODE ══════════════════════════════════════════════════
            P.q("window.__MRB_FC_SUBJECT__ = %s" % json.dumps({AID: "chemistry"}))
            P.q("window.__MRB_OPEN_HW__(%s)" % json.dumps(AID))
            settle(0.6)
            s = P.st()
            check(s["open"] and s["strip"], "homework opens in the SAME overlay")
            check(s["progress"] == "0 of 5 right" and s["segs"] == 5,
                  "strip: '0 of 5 right' and five bar segments (got %r, %d)" % (s["progress"], s["segs"]))
            check(s["stackPos"] == "" and not s["pips"], "A5: header position blank, no pip row")
            check(s["secured"] is None and s["hint"] is None, "writing pass: no secured line, no helper")
            check(s["tag"] == "HOMEWORK" and s["front"] == "What is the unit of force?", "card 1 question on Design's card")
            check(not s["practiceRow"], "Design's Reveal/Next row is hidden in homework mode")
            check(s["writing"] and s["checkDisabled"] is True and s["idk"] and not s["back"],
                  "state A: answer box, Check disabled while empty, I don't know, no ‹ Back on card 1")
            check(s["note"], "the teacher's note shows before the first answer")
            P.no_retired("state A")
            P.shot("A-question")

            P.keyboard(True)
            s = P.st()
            check(s["focused"] and s["typing"] == "1", "keyboard up: the dialog goes compact (data-hw-typing=1)")
            check(not s["note"] or P.q("document.querySelector('[data-hw=\"note\"]').getBoundingClientRect().height") == 0,
                  "compact: the note is hidden while typing")
            P.boxes("state A, empty")
            P.shot("A-keyboard-up")
            P.type("   ")
            check(P.st()["checkDisabled"] is True, "Check stays disabled for spaces only")
            P.type("newton")
            s = P.st()
            check(s["checkDisabled"] is False, "Check enables after one non-space character")
            check(s["focused"] and s["typing"] == "1", "the redraw that enabled Check kept focus and compact mode (A10)")
            P.boxes("state A, typed")
            P.shot("A-typed")
            P.click('[data-hw="check"]')
            P.keyboard(False)
            s = P.st()
            check(s["flipped"] == "1" and s["rating"] and not s["writing"],
                  "Check turns the card to the model answer and shows the three ratings")
            check(s["chip"] == "Right" and s["pressed"] == ["got_it"],
                  "state C: chip 'Right', Got it filled (got %r %r)" % (s["chip"], s["pressed"]))
            check("newton" in (s["mine"] or "") and s["back_"] == "The newton (N)", "the pupil's answer under the model answer")
            check(s["typing"] is None, "keyboard gone: compact mode off")
            P.shot("C-verdict-right")
            P.click('[data-hw="got_it"]')
            s = P.st()
            check(s["progress"] == "1 of 5 right" and s["front"] == "What is the formula of water?" and s["back"],
                  "Got it → '1 of 5 right', card 2, ‹ Back now offered (got %r)" % s["progress"])
            check(not s["note"], "the note goes once the pupil has started")

            # state B: the model is asked, and has not answered yet
            P.keyboard(True)
            P.type("made of hydrogen and oxygen")
            P.click('[data-hw="check"]')
            P.keyboard(False)
            s = P.st()
            check(s["chip"] == "Checking…" and s["rating"] and s["pressed"] == [],
                  "state B: 'Checking…', ratings showing, none filled (A2) (got %r %r)" % (s["chip"], s["pressed"]))
            check(s["backSubs"] == 1 and s["back_"] == "H2O", "H2O renders with a real <sub> (text unchanged)")
            P.shot("B-checking")
            P.q("window.__MODEL__('partial')")
            settle()
            s = P.st()
            check(s["chip"] == "Nearly" and s["pressed"] == ["nearly"], "the model's verdict: chip 'Nearly', Nearly filled (got %r %r %r)" % (s["chip"], s["pressed"], P.q("[typeof window.__MODEL__, window.MRBHomework.active.verdict]")))
            P.shot("C-verdict-nearly")
            P.click('[data-hw="nearly"]')

            # card 3, then ‹ Back to card 2 from state C
            P.keyboard(True)
            P.type("gravity")
            P.click('[data-hw="check"]')
            P.keyboard(False)
            check(P.st()["chip"] == "Right", "card 3: 'gravity' is Right")
            P.click('[data-hw="back"]')
            s = P.st()
            check(s["front"] == "What is the formula of water?" and s["writing"] and s["draft"] == "made of hydrogen and oxygen",
                  "‹ Back: card 2 in state A with the earlier answer in the box (got %r)" % s["draft"])
            check(s["progress"] == "1 of 5 right", "the count holds until the card is re-rated")
            P.shot("Back-card-2")
            P.click('[data-hw="idk"]')
            s = P.st()
            check(s["chip"] == "No answer" and s["pressed"] == ["not_yet"] and s["flipped"] == "1",
                  "I don't know: the model answer, chip 'No answer', Not yet filled (A4)")
            P.shot("C-idk")
            P.click('[data-hw="not_yet"]')
            s = P.st()
            check(s["front"] == "What is weight?" and s["draft"] == "gravity",
                  "card 3 again, 'gravity' still in its box (got %r)" % s["draft"])
            P.keyboard(True)
            P.boxes("state A after ‹ Back")
            P.keyboard(False)
            P.q("window.MRBHomework.modelCheck = null")
            P.click('[data-hw="check"]')
            P.click('[data-hw="got_it"]')
            P.keyboard(True)
            P.type("F = ke")
            P.click('[data-hw="check"]')
            P.keyboard(False)
            s = P.st()
            check(s["chip"] is None and s["pressed"] == [], "no verdict (no model check): no chip, nothing filled (A3)")
            P.click('[data-hw="got_it"]')
            P.keyboard(True)
            P.type("vector")
            P.click('[data-hw="check"]')
            P.keyboard(False)
            P.click('[data-hw="got_it"]')
            settle(0.8)
            s = P.st()
            check(s["end1"] == "4 of 5 right this time" and s["end2"] == "0 of 5 secured so far",
                  "writing pass end screen: '4 of 5 right this time' / '0 of 5 secured so far' (got %r / %r)"
                  % (s["end1"], s["end2"]))
            check(s["again"] == "Revise flashcards one more time" and s["done"] is None and s["endHint"] is None,
                  "writing pass: the button is 'Revise flashcards one more time'")
            check(not s["stripShown"], "the strip steps aside on the end screen (its numbers would repeat)")
            ev = P.q("window.__FC_FAKE__.events")
            check(not any(e["type"] == "session_finish" for e in ev), "the writing pass does not end the sitting")
            P.no_retired("writing end screen")
            P.shot("End-writing")

            P.click('[data-hw="again"]')
            s = P.st()
            check(s["progress"] == "0 of 5 right" and s["secured"] == "0 secured"
                  and s["hint"] == "Revise flashcards one more time",
                  "review pass: '0 of 5 right', '0 secured', the helper line (got %r %r %r)"
                  % (s["progress"], s["secured"], s["hint"]))
            check(s["front"] == "What is the formula of water?", "the review pass starts on the Not yet card")
            P.keyboard(True)
            P.boxes("review pass, state A")
            s = P.st()
            check(s["hint"] is None or P.q("document.querySelector('[data-hw=\"strip\"] [data-hw=\"hint\"]').getBoundingClientRect().height") == 0,
                  "compact: the helper line hides while typing")
            P.shot("Review-keyboard-up")
            P.keyboard(False)
            answers = {"What is the formula of water?": "idk", "What is the unit of force?": "newton",
                       "What is weight?": "gravity", "Write the equation for the force on a spring.": "ke",
                       "Is velocity a scalar or a vector?": "vector"}
            for _ in range(5):
                f = P.st()["front"]
                P.type(answers.get(f, "x"))
                P.click('[data-hw="check"]')
                P.click('[data-hw="got_it"]')
            settle(0.8)
            s = P.st()
            check(s["end1"] == "5 of 5 right this time" and s["end2"] == "4 of 5 secured so far",
                  "make's review pass: '5 of 5 right this time' / '4 of 5 secured so far' (got %r / %r)"
                  % (s["end1"], s["end2"]))
            check(s["again"] == "Revise flashcards one more time" and s["endHint"] is None,
                  "make's own review pass is never 'too soon': Revise is the button")
            P.shot("End-review")

            # A second sitting, an hour later: the last card secures.
            P.q("window.__FC_FAKE__.later = true")
            P.click('[data-hw="again"]')
            s = P.st()
            check(s["progress"] == "0 of 5 right", "a new sitting opens at '0 of 5 right'")
            P.shot("Sitting-2")
            for _ in range(5):
                f = P.st()["front"]
                P.type(answers.get(f, "x"))
                P.click('[data-hw="check"]')
                P.click('[data-hw="got_it"]')
            settle(0.8)
            s = P.st()
            check(s["end2"] == "5 of 5 secured so far" and s["done"] == "Done" and s["again"] is None
                  and s["endHint"] is None,
                  "every card secured → '5 of 5 secured so far' and Done (got %r %r)" % (s["end2"], s["done"]))
            P.no_retired("secured end screen")
            P.shot("Secured")
            check(not s["overflowX"], "no sideways scroll at %dpx" % width)
            ev = P.q("window.__FC_FAKE__.events")
            ids = [e["id"] for e in ev]
            check(len(ids) == len(set(ids)), "every event has its own id (idempotent resend)")
            check(sum(1 for e in ev if e["type"] == "session_finish") == 2, "two sittings ended with session_finish")
            check(all(e.get("via") in ("auto", "tap") for e in ev if e["type"] == "rated"), "every rating says auto/tap")
            check(not any("think_ms" in e or "active_ms" in e for e in ev), "no event carries a duration")
            P.click('[data-hw="done"]')
            check(not P.st()["open"], "Done closes the overlay")

            # ══ REVIEW MODE, one sitting, × part-way and back ═════════════
            P.q("window.MRBHomework._reset(); localStorage.clear(); window.__FC_FAKE__.mode = 'review'; "
                "window.__FC_FAKE__.later = false;")
            P.q("window.__FC_FAKE__.events.length = 0")
            P.q("window.__MRB_OPEN_HW__(%s)" % json.dumps(AID))
            settle(0.6)
            s = P.st()
            check(s["writing"] and s["progress"] == "0 of 5 right" and s["secured"] == "5 secured",
                  "review mode: typing in review too; '5 secured' carried over (got %r)" % s["secured"])
            P.keyboard(True)
            P.boxes("review mode, state A")
            P.keyboard(False)
            P.type("newton")
            P.click('[data-hw="check"]')
            P.click('[data-port-region="flashcards-overlay"] button[title="Close"]')
            settle(0.5)
            ev = P.q("window.__FC_FAKE__.events")
            check(any(e["type"] == "session_finish" for e in ev), "A13: × after one Check in review ends the sitting")
            check(not P.st()["open"], "× closes the overlay")
    finally:
        server.shutdown()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--shots", default=None)
    a = ap.parse_args()
    shots = a.shots or os.path.join(cdp.gate_tmp(), "flashcard-homework")
    os.makedirs(shots, exist_ok=True)
    live = open(os.path.join(ROOT, "shared", "student-live.js"), encoding="utf-8").read()
    check('"/shared/flashcard-keyboard.js"' in live and "H.modelCheck = function" in live
          and "H.resumeRead = function" in live,
          "the live page loads the keyboard module and wires the model check and the resume read")
    check("e.flip()" not in live, "the live page no longer turns a card with Space")
    for w, h, kb in ((390, 844, 508), (360, 740, 404)):
        run(w, h, kb, shots)
    print("\n  screenshots: %s" % shots)
    if FAILS:
        print("\n  FAIL — %d check(s) failed" % len(FAILS))
        sys.exit(1)
    print("\n  PASS — flashcard homework, pupil flow, on a phone with the keyboard up")


if __name__ == "__main__":
    main()
