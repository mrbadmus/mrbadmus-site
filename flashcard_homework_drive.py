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
           "Not quite", "Keep revising", "YOUR DECK IS READY", "DECK SECURED", "right this time")

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
  var enabled = Array.prototype.filter.call(document.querySelectorAll('[data-hw="rate"] button'),
                                            function (b) { return !b.disabled; })
                  .map(function (b) { return b.getAttribute('data-hw'); });
  var chipEls = document.querySelectorAll('[data-hw="chips"] > *');
  var chips = Array.prototype.map.call(chipEls, function (c) {
    return {num: c.innerText.trim(), redo: c.getAttribute('data-hw') === 'chip-redo',
            current: /inset/.test(c.getAttribute('style') || '')};
  });
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
    enabled: enabled,
    learn: txt('[data-hw="learn"]'),
    placeholder: ta ? ta.getAttribute('placeholder') : null,
    chips: chips,
    chipsShown: !!$('[data-hw="chips"]'),
    greens: chips.filter(function (c) { return c.redo; }).length,
    gone: txt('[data-hw="gone-text"]'),
    goneBtn: txt('[data-hw="gone"]'),
    retryPass: txt('[data-hw="retry-pass"]'),
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
  var l = box('[data-hw="learn"]');
  var cr = c ? c.getBoundingClientRect() : null;
  var hit = cr ? document.elementFromPoint(cr.left + cr.width / 2, cr.top + cr.height / 2) : null;
  return {vv: [top, bot], q: q, t: t, l: l,
          lIn: !!l && l.h > 0 && l.top >= top - 0.5 && l.bottom <= bot + 0.5,
          lFootIn: !!l && l.h > 0 && l.bottom >= top - 0.5 && l.bottom <= bot + 0.5,
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

    def keyboard(self, up, kb=None):
        if up:
            self.q("(function(){var t=document.querySelector('[data-hw=\"answer\"]'); if(t) t.focus();})()")
        self.q("window.__KB__(%s)" % ((kb or self.kb) if up else "null"))
        settle(0.45)

    def learn_boxes(self, kb):
        """§13.4 acceptance for the "I don't know" learn state."""
        b = self.q(BOXES_JS)
        if self.w >= 390:
            ok = b["qIn"] and b["lIn"] and b["tIn"] and b["checkVisible"]
            need = "question, ANSWER block and box inside, Check visible"
        else:
            ok = b["lFootIn"] and b["tIn"] and b["checkVisible"]
            need = "ANSWER block's foot and box inside, Check visible"
        check(ok, "%d×%d learn state, keyboard up (visual %d): %s (q=%s l=%s t=%s check=%s)"
              % (self.w, self.h, kb, need, b["q"], b["l"], b["t"], b["checkVisible"]))

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
            check(s["chip"] == "Checking…" and s["rating"] and s["pressed"] == [] and s["enabled"] == [],
                  "state B: 'Checking…', ratings showing, none filled, all three disabled (§13.1.2) (got %r %r %r)"
                  % (s["chip"], s["pressed"], s["enabled"]))
            check(s["backSubs"] == 1 and s["back_"] == "H2O", "H2O renders with a real <sub> (text unchanged)")
            P.shot("B-checking")
            P.q("window.__MODEL__('partial')")
            settle()
            s = P.st()
            check(s["chip"] == "Nearly" and s["pressed"] == ["nearly"] and s["enabled"] == ["not_yet", "nearly"],
                  "partial: chip 'Nearly', Nearly filled, Got it disabled (got %r %r %r)"
                  % (s["chip"], s["pressed"], s["enabled"]))
            P.shot("C-nearly-capped")
            P.click('[data-hw="got_it"]')
            check(P.st()["chip"] == "Nearly", "tapping the disabled Got it does nothing")
            P.q("document.dispatchEvent(new KeyboardEvent('keydown', {key: '3', bubbles: true}))")
            settle()
            check(P.st()["chip"] == "Nearly", "key 3 (Got it) is refused above the cap too")
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
            P.type("water")
            P.click('[data-hw="check"]')
            s = P.st()
            check(s["chip"] == "Wrong" and s["pressed"] == ["not_yet"] and s["enabled"] == ["not_yet"],
                  "Wrong: only Not yet enabled (got %r %r)" % (s["chip"], s["enabled"]))
            P.no_retired("wrong capped")
            P.shot("C-wrong-capped")
            P.click('[data-hw="not_yet"]')
            s = P.st()
            check(s["front"] == "What is weight?" and s["draft"] == "gravity",
                  "card 3 again, 'gravity' still in its box (got %r)" % s["draft"])
            P.keyboard(True)
            P.boxes("state A after ‹ Back")
            P.keyboard(False)
            P.click('[data-hw="check"]')
            P.click('[data-hw="got_it"]')

            # card 4: I don't know → the learn state → own words, capped at Nearly
            P.click('[data-hw="idk"]')
            s = P.st()
            check(s["front"] == "Write the equation for the force on a spring." and s["flipped"] != "1"
                  and s["learn"] and "F = ke" in s["learn"] and s["learn"].startswith("ANSWER"),
                  "I don't know: the card stays on its question, the model answer shows under it (got %r)" % s["learn"])
            check(s["placeholder"] == "Now write it in your own words" and not s["idk"] and s["back"] and not s["rating"],
                  "learn state: 'Now write it in your own words', no second I don't know, ‹ Back kept, no ratings")
            check(s["draft"] == "", "the own-words box opens empty")
            P.keyboard(True)
            s = P.st()
            check(s["typing"] == "1" and P.q("document.querySelector('[data-mrb-dialog=\"flashcards\"]').getAttribute('data-hw-learn')") == "1",
                  "learn state with the keyboard up: compact + data-hw-learn")
            P.learn_boxes(kb)
            P.shot("A2-learn")
            if width < 390:
                P.keyboard(True, 336)
                P.learn_boxes(336)
                P.shot("A2-learn-336")
            P.type("F = ke")
            P.q("window.MRBHomework.modelCheck = function () { return new Promise(function (r) { window.__MODEL__ = r; }); }")
            P.click('[data-hw="check"]')
            P.keyboard(False)
            P.q("window.__MODEL__('match')")
            settle()
            s = P.st()
            check(s["chip"] == "Right" and s["pressed"] == ["nearly"] and s["enabled"] == ["not_yet", "nearly"],
                  "own words Right after I don't know: chip Right, Nearly filled, Got it disabled (got %r %r %r)"
                  % (s["chip"], s["pressed"], s["enabled"]))
            P.shot("C-idk-capped")
            P.click('[data-hw="nearly"]')
            P.keyboard(True)
            P.type("vector")
            P.click('[data-hw="check"]')
            P.keyboard(False)
            P.click('[data-hw="got_it"]')
            s = P.st()
            check(s["front"] == "Write the equation for the force on a spring." and s["idk"] and not s["learn"]
                  and s["placeholder"] == "Your answer" and s["progress"] == "3 of 5 right" and s["draft"] == "",
                  "the I-don't-know card comes round again, as a plain card, before the pass ends (got %r %r)"
                  % (s["front"], s["progress"]))
            P.shot("A-idk-replay")
            P.q("window.MRBHomework.modelCheck = null")
            P.type("F = ke")
            P.click('[data-hw="check"]')
            s = P.st()
            check(s["chip"] is None and s["pressed"] == [] and len(s["enabled"]) == 3,
                  "no verdict (no model check): no chip, nothing filled, all three enabled (A3)")
            P.click('[data-hw="got_it"]')
            settle(0.8)
            s = P.st()
            check(s["end1"] == "4 of 5 right" and s["end2"] is None,
                  "writing pass end screen: '4 of 5 right', no line 2 (got %r / %r)" % (s["end1"], s["end2"]))
            check(s["again"] == "Revise flashcards one more time" and s["done"] is None and s["endHint"] is None
                  and s["retryPass"] is None,
                  "writing pass: the button is 'Revise flashcards one more time'")
            check(not s["stripShown"], "the strip steps aside on the end screen (its numbers would repeat)")
            ev = P.q("window.__FC_FAKE__.events")
            check(not any(e["type"] == "session_finish" for e in ev), "the writing pass does not end the sitting")
            idk_ev = [e for e in ev if e["type"] == "answer_submitted" and e.get("card", "").endswith("04")]
            check([bool(e.get("idk")) for e in idk_ev][:2] == [True, False] and idk_ev[1].get("own_words") is True,
                  "events: 'I don't know' (idk) then the own words (own_words)")
            P.no_retired("writing end screen")
            P.shot("End-writing")

            P.click('[data-hw="again"]')
            s = P.st()
            check(s["progress"] == "0 of 5 right" and s["secured"] is None and s["hint"] is None,
                  "review pass: '0 of 5 right' and the bar only — no secured line, no helper mid-pass "
                  "(got %r %r %r)" % (s["progress"], s["secured"], s["hint"]))
            check(s["front"] == "What is the formula of water?", "the review pass starts on the Not yet card")
            P.keyboard(True)
            P.boxes("review pass, state A")
            s = P.st()
            check(s["hint"] is None or P.q("document.querySelector('[data-hw=\"strip\"] [data-hw=\"hint\"]').getBoundingClientRect().height") == 0,
                  "compact: the helper line hides while typing")
            P.shot("Review-keyboard-up")
            P.keyboard(False)
            answers = {"What is the formula of water?": "h2o", "What is the unit of force?": "newton",
                       "What is weight?": "gravity", "Write the equation for the force on a spring.": "ke",
                       "Is velocity a scalar or a vector?": "vector"}
            for _ in range(5):
                f = P.st()["front"]
                P.type(answers.get(f, "x"))
                P.click('[data-hw="check"]')
                P.click('[data-hw="got_it"]')
            settle(0.8)
            s = P.st()
            check(s["end1"] == "5 of 5 right" and s["end2"] == "4 of 5 secured so far",
                  "make's review pass all right: '5 of 5 right' / '4 of 5 secured so far' (got %r / %r)"
                  % (s["end1"], s["end2"]))
            check(s["done"] == "Done" and s["again"] is None and s["retryPass"] is None
                  and s["endHint"] == "Revise flashcards one more time",
                  "all right, not all secured: ONE button Done, with 'Revise flashcards one more time' above it")
            ev = P.q("window.__FC_FAKE__.events")
            check(sum(1 for e in ev if e["type"] == "session_finish") == 1, "the all-right pass ended the sitting, once")
            check(all(e.get("via") in ("auto", "tap") for e in ev if e["type"] == "rated"), "every rating says auto/tap")
            check(not any("think_ms" in e or "active_ms" in e for e in ev), "no event carries a duration")
            ids = [e["id"] for e in ev]
            check(len(ids) == len(set(ids)), "every event has its own id (idempotent resend)")
            P.no_retired("make all-right end screen")
            P.shot("End-review")
            check(not s["overflowX"], "no sideways scroll at %dpx" % width)
            P.click('[data-hw="done"]')
            check(not P.st()["open"], "Done closes the overlay")

            # ══ REVIEW MODE: leftovers → Try again → a redo → Done ══════════
            P.q("window.MRBHomework._reset(); localStorage.clear(); window.__FC_FAKE__.mode = 'review'; "
                "window.__FC_FAKE__.later = false; window.MRBHomework.modelCheck = null;")
            P.q("window.__FC_FAKE__.events.length = 0")
            P.q("window.__MRB_OPEN_HW__(%s)" % json.dumps(AID))
            settle(0.6)
            s = P.st()
            check(s["writing"] and s["progress"] == "0 of 5 right" and s["segs"] == 5 and not s["chipsShown"],
                  "review mode: a first pass has the plain bar, no chips (got %r)" % s["progress"])
            P.keyboard(True)
            P.boxes("review mode, state A")
            P.keyboard(False)
            wrong = {"What is the formula of water?": "water", "Write the equation for the force on a spring.": "stretch"}
            order = []
            for _ in range(5):
                f = P.st()["front"]
                order.append(f)
                P.type(wrong.get(f) or answers.get(f, "x"))
                P.click('[data-hw="check"]')
                P.click('[data-hw="not_yet"]' if f in wrong else '[data-hw="got_it"]')
            settle(0.8)
            s = P.st()
            check(s["end1"] == "3 of 5 right" and s["retryPass"] == "Try again" and s["end2"] is None
                  and s["done"] is None and s["again"] is None and s["endHint"] is None,
                  "leftovers: '3 of 5 right' and ONE button 'Try again', no line 2 (got %r %r %r)"
                  % (s["end1"], s["retryPass"], s["end2"]))
            ev = P.q("window.__FC_FAKE__.events")
            check(not any(e["type"] == "session_finish" for e in ev), "the leftovers screen does not end the sitting")
            P.no_retired("leftovers screen")
            P.shot("End-try-again")
            P.click('[data-hw="retry-pass"]')
            s = P.st()
            check(s["chipsShown"] and s["segs"] == 0 and len(s["chips"]) == 5 and s["greens"] == 3
                  and s["progress"] == "3 of 5 right",
                  "Try again: 5 numbered chips, 3 green (tappable), headline '3 of 5 right' (got %r %r)"
                  % (s["chips"], s["progress"]))
            check([c["num"] for c in s["chips"]] == ["1", "2", "3", "4", "5"], "the chips are numbered 1…5")
            check(s["front"] == [f for f in order if f in wrong][0] and s["draft"] == "",
                  "the queue opens on the first leftover, with an empty box (got %r)" % s["draft"])
            cur = [c for c in s["chips"] if c["current"]]
            check(len(cur) == 1 and not cur[0]["redo"], "the current chip is ringed")
            check(s["secured"] is None and s["hint"] is None, "Try again: the strip is the headline and the chips only")
            P.no_retired("retry strip")
            P.shot("Retry-strip")
            # the dark theme: a chip still to come keeps an edge (Fable S-a)
            P.q("document.documentElement.setAttribute('data-theme','dark')")
            settle()
            edge = P.q("(function(){var c=[].slice.call(document.querySelectorAll('[data-hw=\"chips\"] > span'))"
                       ".filter(function(x){return !/inset/.test(x.getAttribute('style'))})[0];"
                       "return c ? getComputedStyle(c).borderTopWidth : null;})()")
            check(edge == "1px", "dark theme: a to-come chip has a 1px edge (got %r)" % edge)
            P.shot("Retry-strip-dark")
            P.q("document.documentElement.removeAttribute('data-theme')")
            settle()
            first_green = order.index([f for f in order if f not in wrong][0])
            P.click('[data-hw="chip-redo"]')
            s = P.st()
            check(s["front"] == order[first_green] and s["writing"] and s["draft"] == answers[order[first_green]]
                  and s["greens"] == 0 and s["back"],
                  "tap a green chip: that card in state A with its earlier answer, ‹ Back offered (got %r %r)"
                  % (s["front"], s["draft"]))
            P.shot("Redo")
            P.type("water" if order[first_green] == "What is the formula of water?" else "zzz")
            P.click('[data-hw="check"]')
            P.click('[data-hw="not_yet"]')
            s = P.st()
            check(s["progress"] == "2 of 5 right" and s["greens"] == 2 and s["front"] == [f for f in order if f in wrong][0],
                  "rated Not yet: the chip turns grey (2 of 5), back on the queue's card (got %r %r)"
                  % (s["progress"], s["front"]))
            P.shot("Redo-grey")
            for _ in range(2):
                f = P.st()["front"]
                P.type(answers.get(f, "x"))
                P.click('[data-hw="check"]')
                P.click('[data-hw="got_it"]')
            settle(0.6)
            s = P.st()
            check(s["end1"] == "4 of 5 right" and s["retryPass"] == "Try again", "the redone card is left: Try again (got %r)" % s["end1"])
            P.click('[data-hw="retry-pass"]')
            s = P.st()
            check(s["front"] == order[first_green] and s["greens"] == 4, "a second Try again: only the still-grey card")
            P.type(answers[order[first_green]])
            P.click('[data-hw="check"]')
            P.click('[data-hw="got_it"]')
            settle(0.8)
            s = P.st()
            check(s["end1"] == "5 of 5 right" and s["done"] == "Done" and s["end2"] == "4 of 5 secured so far"
                  and s["retryPass"] is None and s["endHint"] == "Revise flashcards one more time",
                  "all right: Done, line 2 from the server (got %r %r %r)" % (s["end1"], s["done"], s["end2"]))
            ev = P.q("window.__FC_FAKE__.events")
            check(sum(1 for e in ev if e["type"] == "session_finish") == 1,
                  "ONE session_finish across the pass and both Try agains")
            P.no_retired("all-right screen")
            P.shot("End-all-right-done")
            P.click('[data-hw="done"]')

            # ══ × after one Check ends the sitting (A13) ═════════════════════
            P.q("window.MRBHomework._reset(); localStorage.clear(); window.__FC_FAKE__.events.length = 0;")
            P.q("window.__MRB_OPEN_HW__(%s)" % json.dumps(AID))
            settle(0.6)
            P.type("newton")
            P.click('[data-hw="check"]')
            P.click('[data-port-region="flashcards-overlay"] button[title="Close"]')
            settle(0.5)
            ev = P.q("window.__FC_FAKE__.events")
            check(any(e["type"] == "session_finish" for e in ev), "A13: × after one Check in review ends the sitting")
            check(not P.st()["open"], "× closes the overlay")

            # ══ a set deleted after the page loaded (§13.6) ══════════════════
            P.q("window.MRBHomework._reset(); window.MRBHomework.transport = function () {"
                " return Promise.reject(Object.assign(new Error('not_your_homework'), {code: 'P0001'})); };")
            P.q("window.__MRB_OPEN_HW__(%s)" % json.dumps(AID))
            settle(0.6)
            s = P.st()
            check(s["gone"] == "Your teacher has taken this work down." and s["goneBtn"] == "Back to my class"
                  and "did not load" not in s["text"] and "Try again" not in s["text"],
                  "not_your_homework: 'Your teacher has taken this work down.' + 'Back to my class', no Try again (got %r)"
                  % s["gone"])
            P.no_retired("taken down")
            P.shot("Gone")
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
    check('.eq("id", wanted).is("deleted_at", null)' in live and '"pageshow"' in live,
          "§13.6: the kind read skips deleted sets; a page back from the bfcache reloads")
    for w, h, kb in ((390, 844, 508), (360, 740, 404)):
        run(w, h, kb, shots)
    print("\n  screenshots: %s" % shots)
    if FAILS:
        print("\n  FAIL — %d check(s) failed" % len(FAILS))
        sys.exit(1)
    print("\n  PASS — flashcard homework, pupil flow, on a phone with the keyboard up")


if __name__ == "__main__":
    main()
