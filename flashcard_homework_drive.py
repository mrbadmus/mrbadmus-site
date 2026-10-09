#!/usr/bin/env python3
"""MRB-351 pupil flow — drive a pupil through flashcard homework in the class
page's flashcard overlay (Design's one flashcard component, in homework
mode), on a PHONE, with the keyboard up.

    python3 flashcard_homework_drive.py            # everything, both phones
    python3 flashcard_homework_drive.py --shots D  # screenshots into D
                                                   # (default: $MRB_SHOTS/flashcard-homework,
                                                   #  outside the repo — MRB-346 rule 5)

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
  ‹ Back, Forward ›, I don't know, the end screens, secured), and the
  retired words absent from the page throughout.

  ⊕ MRB-354 (2 Oct 2026) — secured/done/finish are rewritten: one got_it
  rating, in any phase, in any sitting, secures a card (no pairing, no
  second-sitting gap); the writing pass follows the same rule as review (no
  forced review pass once every card is secured); "Got it" is "Secured"
  everywhere; Forward › sits beside ‹ Back. The engine computes this itself
  from the pupil's own rows, never from the stand-in server's own (still OLD
  two-sitting rule) `secured`/`known` counts — this file's stand-in keeps
  that old arithmetic ON PURPOSE, to prove the page never reads it.

  It does NOT prove the server's arithmetic — durations, sittings,
  completion writing the submission. Those are proved on TEST with the real
  database (tools/mrb351_pupil_flow_live.py) and in flashcard_engine_test.js.
"""

import argparse
import base64
import json
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ks3_browser as cdp  # noqa: E402

# ⊕ Prompt Y — card 3 typed in full (a lone word of it now goes to the answer check).
WEIGHT_RIGHT = "the force acting on an object due to gravity"

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
  var S = window.__FC_FAKE__ = {events: [], calls: 0, complete: false, mode: "make", sittings: 0, open: false,
                                rows: [], seen: {}};
  // ⊕ Stage D — the pupil's own flashcard_reviews, oldest first: one row per
  // rating (a make rating only once the card is made). Cleared with events.
  S.reviews = function () {
    if (!S.events.length) { S.rows.length = 0; S.seen = {}; }
    return JSON.parse(JSON.stringify(S.rows));
  };
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
      if (e.id && S.seen[e.id]) { return; }             // on conflict (id) do nothing
      if (e.id) { S.seen[e.id] = true; }
      S.events.push(e);
      if (!S.open && e.type !== "visibility") { S.open = true; S.sittings++; }
      if (e.type === "session_finish") { S.open = false; }
      var c = cards.filter(function (k) { return k.id === e.card; })[0];
      if (!c) return;
      if (e.type === "answer_submitted" && e.phase === "make") { c.made = true; if (c.mine == null) c.mine = e.answer; }
      if (e.type === "rated") {
        if (e.phase !== "make" || c.made) {
          // ⊕ MRB-354 — session_id is the real grouping key the pupil-side
          // engine now secures by; S.sittings already IS this stand-in's
          // sitting id.
          S.rows.push({id: e.id, card_id: c.id, rating: e.rating, phase: e.phase, rated_at: e.at,
                       session_id: "s" + S.sittings});
        }
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
  window.MRBHomework.resumeRead = function () { return Promise.resolve(window.__FC_FAKE__.reviews()); };
  window.MRBHomework.modelCheck = function () {
    return new Promise(function (r) { window.__MODEL__ = r; });
  };
  return !!window.__MRB_OPEN_HW__;
})()
"""

MODEL_ANSWERS = {
    "What is the unit of force?": "The newton (N)",
    "What is the formula of water?": "H2O",
    "What is weight?": "The force acting on an object due to gravity",
    "Write the equation for the force on a spring.": "Force = spring constant × extension (F = ke)",
    "Is velocity a scalar or a vector?": "A vector",
}

RETIRED = ("FOR NOW", "Go again", "Made ", "later on", "Finish for now", "Compare it yourself",
           "Not quite", "Keep revising", "YOUR DECK IS READY", "DECK SECURED", "right this time",
           "Got it", "secured so far")   # ⊕ MRB-354 (2 Oct 2026)

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
    // ⊕ 5 Oct 2026 — the verdict chip proper, never one of the strip's numbered chips
    verdictChip: (function () { var els = document.querySelectorAll('[data-hw="chip"]'); for (var i = 0; i < els.length; i++) { if (!els[i].closest('[data-hw="chips"]')) { return els[i].innerText.trim(); } } return null; })(),
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


# ⊕ Stage D — the homework card's size: its height, the taller face's CONTENT
# height (measured the way flashcard-keyboard.js measures it), the strip.
CARD_JS = r"""
(function () {
  function content(f) { if (!f) return 0; var b = f.style.bottom, h = f.style.height;
    f.style.bottom = 'auto'; f.style.height = 'auto'; var n = f.offsetHeight; f.style.bottom = b; f.style.height = h; return n; }
  var card = document.querySelector('[data-card-fit]'), dlg = document.querySelector('[data-mrb-dialog="flashcards"]');
  var strip = document.querySelector('[data-hw="strip"]'), ta = document.querySelector('[data-hw="answer"]');
  var front = document.querySelector('[data-dc-tpl="10334"]');
  return {card: card ? card.getBoundingClientRect().height : null,
          content: Math.max(content(front), content(document.querySelector('[data-dc-tpl="10351"]'))),
          dialog: dlg ? dlg.getBoundingClientRect().height : null,
          strip: strip ? strip.getBoundingClientRect().height : null,
          ta: ta ? ta.getBoundingClientRect().height : null,
          frontClipped: !!front && front.scrollHeight > front.clientHeight + 1,
          vv: window.visualViewport.height,
          typing: dlg ? dlg.getAttribute('data-hw-typing') : null,
          fit: dlg ? dlg.getAttribute('data-hw-fit') : null};
})()
"""

# the six rects Mide sees move (header, strip, card, question text, box, Check)
RECTS_JS = r"""
(function () {
  function r(s) { var e = document.querySelector(s); if (!e) return null; var b = e.getBoundingClientRect();
    return [Math.round(b.top * 100) / 100, Math.round(b.height * 100) / 100]; }
  var dlg = document.querySelector('[data-mrb-dialog="flashcards"]');
  return {header: r('[data-dc-tpl="10321"]'), strip: r('[data-hw="strip"]'), card: r('[data-card-fit]'),
          q: r('[data-dc-tpl="10340"]'), ta: r('[data-hw="answer"]'), check: r('[data-hw="check"]'),
          typing: dlg ? dlg.getAttribute('data-hw-typing') : null};
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
            rest = P.q(CARD_JS)
            check(rest["fit"] == "1" and abs(rest["card"] - max(140, rest["content"])) <= 2,
                  "%d×%d keyboard down: the card is its content's height (card %.1f, content %.1f)"
                  % (width, height, rest["card"], rest["content"]))

            P.keyboard(True)
            s = P.st()
            check(s["focused"] and s["typing"] == "1", "keyboard up: the dialog goes compact (data-hw-typing=1)")
            up = P.q(CARD_JS)
            # ⊕ MRB-354 unit B commander follow-up — see `run_resizes_content`
            # for the full reasoning: the card no longer has a fixed 120px
            # floor under a keyboard, by design (a short card hands the room
            # it doesn't need straight to the box). This card's question is
            # long enough that it still lands above 120 here, which is why
            # this particular case didn't itself go red — but the assertion
            # must not claim a floor the product no longer has.
            check(40 - 0.5 <= up["card"] <= max(120, 0.34 * up["vv"]) + 0.5,
                  "%d×%d keyboard up: the card is at least 40px, at most 120px or 34%% of the visual height "
                  "(card %.1f, visual %d)" % (width, height, up["card"], up["vv"]))
            P.keyboard(False)
            down = P.q(CARD_JS)
            check(down["typing"] is None and abs(down["card"] - rest["card"]) <= 0.5 and abs(down["strip"] - rest["strip"]) <= 0.5,
                  "%d×%d keyboard down again, box still focused: not compact, card and strip back to full "
                  "(card %.1f/%.1f, strip %.1f/%.1f)" % (width, height, down["card"], rest["card"], down["strip"], rest["strip"]))
            P.keyboard(True)
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
            check(s["chip"] == "Right" and s["pressed"] == [] and s["enabled"] == ["not_yet", "nearly", "got_it"],
                  "state C: chip 'Right' as a hint, nothing filled, all three ratings enabled (got %r %r %r)"
                  % (s["chip"], s["pressed"], s["enabled"]))
            check(P.q("document.querySelector('[data-hw=\"got_it\"]').textContent.trim()") == "Secured",
                  "⊕ MRB-354 — the rating button reads 'Secured', never 'Got it'")
            check("newton" in (s["mine"] or "") and s["back_"] == "The newton (N)", "the pupil's answer under the model answer")
            check(s["typing"] is None, "keyboard gone: compact mode off")
            P.shot("C-verdict-right")
            P.click('[data-hw="got_it"]')
            s = P.st()
            check(s["progress"] == "1 of 5 right" and s["front"] == "What is the formula of water?" and s["back"],
                  "Got it → '1 of 5 right', card 2, ‹ Back now offered (got %r)" % s["progress"])
            check(not s["note"], "the note goes once the pupil has started")
            # ⊕ design-port audit, must-fix 2 — card 1 is now green (got_it)
            # and card 2 is unrevealed: exactly the state the audit caught
            # the redo hint leaking into, because `hwRetryHintOn` only
            # checked `v.chips.some(g => g.redo)` and never `!!v.retry`, so
            # a green card during the FIRST pass (not a retry) satisfied it.
            # Nothing on this bar can be tapped in the first pass — its
            # chips are plain spans, not buttons — so the hint would have
            # promised a tap that does nothing.
            check(s["hint"] is None,
                  "first pass, a green card behind it: still no redo hint "
                  "(nothing on this bar is tappable yet) (got %r)" % s["hint"])

            # state B: the model is asked, and has not answered yet
            P.keyboard(True)
            P.type("made of water")
            P.click('[data-hw="check"]')
            P.keyboard(False)
            s = P.st()
            check(s["chip"] == "Checking…" and s["rating"] and s["pressed"] == [] and s["enabled"] == ["not_yet", "nearly", "got_it"],
                  "state B: 'Checking…', ratings showing, none filled, all three ENABLED — the pupil never waits (5 Oct) (got %r %r %r)"
                  % (s["chip"], s["pressed"], s["enabled"]))
            check(s["backSubs"] == 1 and s["back_"] == "H2O", "H2O renders with a real <sub> (text unchanged)")
            P.shot("B-checking")
            P.q("window.__MODEL__('partial')")
            settle()
            s = P.st()
            check(s["chip"] == "Nearly" and s["pressed"] == [] and s["enabled"] == ["not_yet", "nearly", "got_it"],
                  "partial: chip 'Nearly' is only a hint — nothing filled, Secured still enabled (got %r %r %r)"
                  % (s["chip"], s["pressed"], s["enabled"]))
            P.shot("C-nearly-hint")
            # (a) a right-but-differently-worded answer the check called Nearly:
            # the pupil taps Secured and it is taken (key 3 does the same).
            P.click('[data-hw="got_it"]')
            check(P.st()["front"] == "What is weight?" and P.st()["progress"] == "2 of 5 right",
                  "(a) Secured on a 'Nearly' verdict is taken: card 2 is secured, on to card 3 (got %r)" % P.st()["front"])

            # card 3, then ‹ Back to card 2 from state C
            P.keyboard(True)
            # ⊕ Prompt Y — the whole answer: a single word of a longer model
            # answer ("gravity") is no longer Right on the spot.
            P.type(WEIGHT_RIGHT)
            P.click('[data-hw="check"]')
            P.keyboard(False)
            check(P.st()["chip"] == "Right", "card 3: the whole answer is Right")
            P.click('[data-hw="back"]')
            s = P.st()
            check(s["front"] == "What is the formula of water?" and s["writing"] and s["draft"] == "made of water",
                  "‹ Back: card 2 in state A with the earlier answer in the box (got %r)" % s["draft"])
            check(s["progress"] == "2 of 5 right", "the count holds until the card is re-rated")
            check(P.q("!!document.querySelector('[data-hw=\"forward\"]')"),
                  "⊕ MRB-354 — Forward › sits beside ‹ Back once a step back has been taken")
            P.click('[data-hw="forward"]')
            s = P.st()
            check(s["front"] == "What is weight?" and s["writing"] and s["draft"] == WEIGHT_RIGHT,
                  "Forward ›: back up to card 3, state A, its earlier answer intact, no rating changed (got %r)"
                  % s["draft"])
            check(not P.q("!!document.querySelector('[data-hw=\"forward\"]')"),
                  "Forward › is hidden again on the newest card (the frontier)")
            P.click('[data-hw="back"]')
            s = P.st()
            check(s["front"] == "What is the formula of water?" and s["draft"] == "made of water",
                  "‹ Back again: card 2, in state A, with its own earlier answer (got %r)" % s["draft"])
            P.shot("Back-card-2")
            P.type("the")                  # a lone function word: Wrong on the spot
            P.click('[data-hw="check"]')
            s = P.st()
            check(s["chip"] == "Wrong" and s["pressed"] == [] and s["enabled"] == ["not_yet", "nearly"],
                  "Wrong on a non-attempt ('the'): chip 'Wrong' as a hint, Nearly / Not yet enabled, Secured greyed "
                  "(8 Oct floor) (got %r %r)" % (s["chip"], s["enabled"]))
            P.no_retired("wrong hint")
            P.shot("C-wrong-hint")
            P.click('[data-hw="not_yet"]')
            s = P.st()
            check(s["front"] == "What is weight?" and s["draft"] == WEIGHT_RIGHT,
                  "card 3 again, its answer still in its box (got %r)" % s["draft"])
            P.keyboard(True)
            P.boxes("state A after ‹ Back")
            P.keyboard(False)
            P.click('[data-hw="check"]')
            P.click('[data-hw="got_it"]')

            # card 4: I don't know → the learn state → own words (no cap)
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
            check(s["chip"] == "Right" and s["pressed"] == [] and s["enabled"] == ["not_yet", "nearly", "got_it"],
                  "own words Right after I don't know: chip Right, nothing filled, all three enabled — no cap after I don't know (got %r %r %r)"
                  % (s["chip"], s["pressed"], s["enabled"]))
            P.shot("C-idk-hint")
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
            # ⊕ Mide, 4 Oct 2026 (option B) — nothing could check it, so it
            # may be Nearly or Not yet, never Secured; Nearly brings it back.
            check(s["chip"] is None and s["pressed"] == [] and sorted(s["enabled"]) == ["got_it", "nearly", "not_yet"],
                  "(c) no verdict (no model check): no chip, nothing filled, all three enabled (got %r)" % s["enabled"])
            P.click('[data-hw="nearly"]')
            settle(0.8)
            s = P.st()
            # ⊕ MRB-354 — c1 (water) was corrected to Wrong/Not yet via ‹ Back
            # earlier and never got_it since: it is the one card NOT secured.
            # The writing pass follows the SAME rule as review now: not all
            # secured → ONE button, Try again (no forced review pass).
            # ⊕ 5 Oct 2026 — card 2 was Secured (on a 'Nearly' hint) and later
            # re-answered Not yet via ‹ Back: once secured, stays secured. Only
            # the spring card (rated Nearly twice) is left.
            check(s["end1"] == "4 of 5 secured" and s["end2"] is None,
                  "writing pass end screen: '4 of 5 secured' — the spring card is left; card 2 stays secured (got %r / %r)" % (s["end1"], s["end2"]))
            check(s["retryPass"] == "Try again" and s["done"] is None and s["again"] is None
                  and s["endHint"] is None,
                  "writing pass, not all secured: ONE button Try again, no forced review pass (MRB-354)")
            # ⊕ MRB-354 — a "retry" end screen (unlike "done") carries no
            # strip title (hwEndDone-only), but the strip itself stays on
            # screen for Close and the segmented bar, exactly as the review
            # mode's own leftovers screen does further down this file — the
            # writing pass never reached this screen before MRB-354 (it only
            # ever ended on "again"), so this is new ground, not a changed
            # assertion.
            check(s["stripShown"] and not s["chipsShown"],
                  "leftovers screen: the strip stays (Close + the segmented bar), no title, no chips yet")
            ev = P.q("window.__FC_FAKE__.events")
            check(not any(e["type"] == "session_finish" for e in ev), "the leftovers screen does not end the sitting")
            idk_ev = [e for e in ev if e["type"] == "answer_submitted" and e.get("card", "").endswith("04")]
            check([bool(e.get("idk")) for e in idk_ev][:2] == [True, False] and idk_ev[1].get("own_words") is True,
                  "events: 'I don't know' (idk) then the own words (own_words)")
            P.no_retired("writing end screen")
            P.shot("End-writing")

            # Try again RETYPES the leftover (c1) — stays in the writing
            # stage, never a review of it.
            P.click('[data-hw="retry-pass"]')
            s = P.st()
            check(s["writing"] and s["front"] == "Write the equation for the force on a spring.",
                  "Try again on a writing pass retypes only the leftover (the spring card), in state A (got %r)" % s["front"])
            P.keyboard(True)
            P.type("Force = spring constant × extension (F = ke)")
            P.click('[data-hw="check"]')
            s = P.st()
            check(s["pressed"] == [] and s["enabled"] == ["not_yet", "nearly", "got_it"],
                  "checked this time: nothing filled, all three enabled (got %r %r)" % (s["pressed"], s["enabled"]))
            P.click('[data-hw="got_it"]')
            settle(0.8)
            s = P.st()
            check(s["end1"] == "5 of 5 secured" and s["end2"] is None,
                  "securing the last card from the writing pass alone finishes the deck: '5 of 5 secured'")
            check(s["done"] == "Done" and s["again"] == "Revise flashcards one more time"
                  and s["retryPass"] is None,
                  "all secured → Done, plus the quieter 'Revise flashcards one more time' secondary — together")
            # ⊕ MRB-354 — the secondary sits on the PAGE, not the card: its
            # label once inherited the card's cream ink and read blank on the
            # cream page while its text still matched above. Measure contrast
            # against the first opaque background behind it.
            ink = P.q("""(function(){
              var b=document.querySelector('[data-hw="again"]'); if(!b) return null;
              function rgb(c){var m=c.match(/[\\d.]+/g)||[];return m.map(Number);}
              function lum(c){return c.slice(0,3).map(function(v){v/=255;return v<=0.03928?v/12.92:Math.pow((v+0.055)/1.055,2.4);})
                .reduce(function(a,v,i){return a+v*[0.2126,0.7152,0.0722][i];},0);}
              var fg=rgb(getComputedStyle(b).color), el=b, bg=null;
              while(el){var c=rgb(getComputedStyle(el).backgroundColor); if(c.length>=3&&(c.length<4||c[3]>0.5)){bg=c;break;} el=el.parentElement;}
              if(!bg) bg=[255,255,255];
              var a=lum(fg),z=lum(bg); return (Math.max(a,z)+0.05)/(Math.min(a,z)+0.05);
            })()""")
            check(ink is not None and ink >= 4.5,
                  "the 'Revise flashcards one more time' label is readable on the page behind it (contrast %r ≥ 4.5)" % ink)
            ev = P.q("window.__FC_FAKE__.events")
            check(sum(1 for e in ev if e["type"] == "session_finish") == 1,
                  "securing the last card (via a retry) ends the sitting, once — no review pass was ever needed")
            check(all(e.get("via") == "tap" for e in ev if e["type"] == "rated"), "nothing is pre-filled, so every rating is a tap")
            check(not any("think_ms" in e or "active_ms" in e for e in ev), "no event carries a duration")
            ids = [e["id"] for e in ev]
            check(len(ids) == len(set(ids)), "every event has its own id (idempotent resend)")
            P.no_retired("writing-pass Done screen")
            P.shot("End-writing-done")

            # The voluntary "Revise flashcards one more time": a FULL pass of
            # the whole deck, in review stage — it never un-secures anything.
            P.click('[data-hw="again"]')
            s = P.st()
            check(s["progress"] == "0 of 5 right" and s["secured"] is None and s["hint"] is None,
                  "Revise: '0 of 5 right' and the bar only — no secured line, no helper mid-pass "
                  "(got %r %r %r)" % (s["progress"], s["secured"], s["hint"]))
            # ⊕ MRB-354 — a review-stage pass is still "type an answer, Check,
            # rate" (state A), the SAME mechanic as the writing pass; what
            # changes between the two modes is the PASS STRUCTURE (two passes
            # vs one), never "typing vs flip-and-rate". `e.stage` (not the
            # DOM) is the real signal that this is the voluntary full-deck
            # revise, not a continuation of the writing pass.
            check(P.q("window.MRBHomework.active.stage") == "review" and s["writing"],
                  "Revise: a fresh REVIEW-STAGE pass, still state A (type, Check) like any pass")
            P.keyboard(True)
            P.boxes("revise pass, state A")
            s = P.st()
            check(s["hint"] is None or P.q("document.querySelector('[data-hw=\"strip\"] [data-hw=\"hint\"]').getBoundingClientRect().height") == 0,
                  "compact: the helper line hides while typing")
            P.shot("Review-keyboard-up")
            P.keyboard(False)
            answers = {"What is the formula of water?": "h2o", "What is the unit of force?": "newton",
                       "What is weight?": WEIGHT_RIGHT, "Write the equation for the force on a spring.": "Force = spring constant × extension (F = ke)",
                       "Is velocity a scalar or a vector?": "vector"}
            for _ in range(5):
                f = P.st()["front"]
                P.type(answers.get(f, "x"))
                P.click('[data-hw="check"]')
                P.click('[data-hw="got_it"]')
            settle(0.8)
            s = P.st()
            check(s["end1"] == "5 of 5 secured" and s["end2"] is None,
                  "revise pass all right: still '5 of 5 secured' — nothing was un-secured (got %r / %r)"
                  % (s["end1"], s["end2"]))
            check(s["done"] == "Done" and s["again"] == "Revise flashcards one more time" and s["retryPass"] is None,
                  "Done + the Revise secondary, still together")
            ev = P.q("window.__FC_FAKE__.events")
            check(sum(1 for e in ev if e["type"] == "session_finish") == 2,
                  "two all-secured endings across this phone's visit so far (writing-retry, then this revise)")
            check(all(e.get("via") == "tap" for e in ev if e["type"] == "rated"), "nothing is pre-filled, so every rating is a tap")
            check(not any("think_ms" in e or "active_ms" in e for e in ev), "no event carries a duration")
            ids = [e["id"] for e in ev]
            check(len(ids) == len(set(ids)), "every event has its own id (idempotent resend)")
            P.no_retired("make all-secured end screen")
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
            wrong = {"What is the formula of water?": "the", "Write the equation for the force on a spring.": "a"}
            order = []
            for _ in range(5):
                f = P.st()["front"]
                order.append(f)
                typed = wrong.get(f) or answers.get(f, "x")
                P.type(typed)
                P.click('[data-hw="check"]')
                # ⊕ 5 Oct 2026 — the revealed answer is ALWAYS the deck's model
                # answer; what was typed is only ever "your answer" beside it.
                st = P.st()
                check(st["back_"] == MODEL_ANSWERS[f] and (st["mine"] or "").endswith(typed) and st["back_"] != typed,
                      "model answer shown for %r, the typed %r only as 'your answer' (got %r / %r)" % (f, typed, st["back_"], st["mine"]))
                P.click('[data-hw="not_yet"]' if f in wrong else '[data-hw="got_it"]')
            settle(0.8)
            s = P.st()
            check(s["end1"] == "3 of 5 secured" and s["retryPass"] == "Try again" and s["end2"] is None
                  and s["done"] is None and s["again"] is None and s["endHint"] is None,
                  "leftovers: '3 of 5 secured' and ONE button 'Try again', no secondary (got %r %r %r)"
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
            # ⊕ Design port review — a hint that promises a tap that does
            # nothing is worse than none, so it moved OFF the end screen
            # (where the same chips are plain spans) and onto an ACTIVE
            # retry pass instead, where a green chip really is `redo:true`
            # right now (line above: 3 of them, here).
            check(s["secured"] is None and s["hint"] == "Tap a green card to redo it",
                  "Try again (an active retry pass): the strip is the headline, the chips, and the redo hint")
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
            P.type("the")
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
            # ⊕ Mide, 4 Oct 2026 — "once secured, stays secured": the redo's
            # Not yet is recorded, but the card it was given to stays secured,
            # so securing the queue's two cards finishes the deck.
            check(s["end1"] == "5 of 5 secured" and s["done"] == "Done" and s["end2"] is None
                  and s["retryPass"] is None and s["again"] == "Revise flashcards one more time",
                  "the redone card stays secured: Done, plus the quieter Revise secondary (got %r %r %r)"
                  % (s["end1"], s["done"], s["again"]))
            ev = P.q("window.__FC_FAKE__.events")
            check(sum(1 for e in ev if e["type"] == "session_finish") == 1,
                  "ONE session_finish across the pass and the Try again")
            P.no_retired("all-right screen")
            P.shot("End-all-right-done")
            P.click('[data-hw="done"]')

            # ══ ⊕ Stage D: × mid-pass, reopen, reload → the same place ═════
            P.q("window.MRBHomework._reset(); localStorage.clear(); window.__FC_FAKE__.events.length = 0; "
                "window.__FC_FAKE__.rows.length = 0; window.__FC_FAKE__.seen = {};")
            P.q("window.__MRB_OPEN_HW__(%s)" % json.dumps(AID))
            settle(0.6)
            order = []
            for verdict in ("got_it", "not_yet", "got_it"):
                f = P.st()["front"]
                order.append(f)
                P.type(answers.get(f, "x") if verdict == "got_it" else "zzz")
                P.click('[data-hw="check"]')
                P.click('[data-hw="%s"]' % verdict)
            fourth = P.st()["front"]
            settle(0.5)
            P.click('[data-port-region="flashcards-overlay"] button[title="Close"]')
            settle(0.5)
            check(not P.st()["open"], "Stage D: × closes the deck after 3 of 5")
            ev = P.q("window.__FC_FAKE__.events")
            check(sum(1 for e in ev if e["type"] == "rated") == 3 and any(e["type"] == "session_finish" for e in ev),
                  "Stage D: the three ratings reached the server, and × still ended the sitting (A13)")
            P.q("window.__MRB_OPEN_HW__(%s)" % json.dumps(AID))
            settle(0.6)
            s = P.st()
            check(s["progress"] == "2 of 5 right" and s["front"] == fourth and s["back"] and not s["note"],
                  "Stage D: reopening after × lands on card 4 at '2 of 5 right' with ‹ Back, no teacher's note (got %r %r)"
                  % (s["progress"], s["front"]))
            P.no_retired("reopen after ×")
            P.shot("D-reopen-card-4")
            saved = P.q("JSON.stringify(window.__FC_FAKE__.events)")
            page.goto("http://127.0.0.1:%d/student/class-fixture.html" % port)
            settle(1.0)
            P.q(LOAD)                                  # a new page: localStorage cleared too
            P.q("window.__FC_FAKE__.mode = 'review'; window.__FC_FAKE__.transport(%s, JSON.parse(%s))"
                % (json.dumps(AID), json.dumps(saved)))
            settle(0.3)
            P.q("window.__MRB_OPEN_HW__(%s)" % json.dumps(AID))
            settle(0.6)
            s = P.st()
            check(s["progress"] == "2 of 5 right" and s["front"] == fourth and s["back"],
                  "Stage D: after a reload (a fresh page, nothing on the device) the same landing (got %r %r)"
                  % (s["progress"], s["front"]))
            P.shot("D-reload-card-4")

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


def shot(page, shots, name):
    if not shots:
        return
    res = page.send("Page.captureScreenshot", {"format": "png", "fromSurface": True})
    with open(os.path.join(shots, name + ".png"), "wb") as fh:
        fh.write(base64.b64decode(res["data"]))


def run_desktop(width, height, shots, expect_tall=True):
    """⊕ Stage D, item 1 — on a desktop, focusing the answer box moves NOTHING.

    No fake keyboard: the visual viewport is the window, as on every desktop.
    Four snapshots of the six rects — at rest, focused, after a keystroke
    that redraws the overlay, blurred — must be identical to the pixel."""
    print("\n── desktop %d×%d ──" % (width, height))
    server, port = cdp.serve(ROOT)
    try:
        with cdp.Browser() as br:
            page = br.attach()
            page.send("Emulation.setDeviceMetricsOverride",
                      {"width": width, "height": height, "deviceScaleFactor": 1, "mobile": False})
            try:
                page.send("Emulation.setFocusEmulationEnabled", {"enabled": True})
            except cdp.CDPError:
                pass
            page.send("Page.addScriptToEvaluateOnNewDocument", {"source": FAKE})
            page.goto("http://127.0.0.1:%d/student/class-fixture.html" % port)
            settle(1.0)
            check(page.eval(LOAD) is True, "desktop %d: the page mounts" % width)
            page.eval("window.__FC_FAKE__.mode = 'review'")
            page.eval("window.__MRB_OPEN_HW__(%s)" % json.dumps(AID))
            settle(0.8)
            snaps = [page.eval(RECTS_JS)]
            shot(page, shots, "D-desk-%d-rest" % width)
            page.eval("document.querySelector('[data-hw=\"answer\"]').focus()")
            settle(0.5)
            snaps.append(page.eval(RECTS_JS))
            shot(page, shots, "D-desk-%d-focus" % width)
            page.eval("(function(){var t=document.querySelector('[data-hw=\"answer\"]'); t.value='n';"
                      " t.dispatchEvent(new Event('input',{bubbles:true}));})()")
            settle(0.5)
            snaps.append(page.eval(RECTS_JS))
            focused = page.eval("document.activeElement && document.activeElement.getAttribute('data-hw')")
            page.eval("document.activeElement.blur()")
            settle(0.5)
            snaps.append(page.eval(RECTS_JS))
            keys = ("header", "strip", "card", "q", "ta", "check")
            same = all(snaps[i][k] == snaps[0][k] for i in range(1, 4) for k in keys)
            check(same and all(x[k] for x in snaps for k in keys),
                  "desktop %d×%d: header, strip, card, question, box and Check identical at rest, focused, "
                  "typing and blurred (%s)" % (width, height, [[x[k] for k in keys] for x in snaps] if not same else snaps[0]))
            check(focused == "answer", "desktop %d: the keystroke's redraw kept focus in the box" % width)
            check(all(x["typing"] is None for x in snaps), "desktop %d: data-hw-typing is never set" % width)
            c = page.eval(CARD_JS)
            tall = page.eval("document.querySelector('[data-mrb-dialog=\"flashcards\"]').getAttribute('data-hw-tall')")
            check((tall == "1") == expect_tall,
                  "desktop %d×%d: data-hw-tall %s (dialog %.0fpx; got %r)"
                  % (width, height, "present" if expect_tall else "absent", c["dialog"], tall))
            if expect_tall:
                check(96 - 0.5 <= c["ta"] <= 200 + 0.5,
                      "desktop %d: the answer box takes the room, 96–200px (%.1f)" % (width, c["ta"]))
            else:
                check(abs(c["ta"] - 64) <= 0.5, "desktop %d: a short dialog keeps the 64px box (%.1f)" % (width, c["ta"]))
            check(c["card"] <= 420 + 0.5 and c["card"] < c["dialog"] / 2,
                  "desktop %d: the card is at most 420px and under half the dialog (%.1f of %.1f)"
                  % (width, c["card"], c["dialog"]))
            check(abs(c["card"] - max(140, c["content"])) <= 2 and not c["frontClipped"],
                  "desktop %d: the card is its content's height and the question is not clipped (%.1f / %.1f)"
                  % (width, c["card"], c["content"]))
    finally:
        server.shutdown()


LIFT_JS = r"""
(function () {
  var b = document.querySelector('[aria-expanded]');
  var r = b ? b.getBoundingClientRect() : null;
  return {y: window.scrollY, top: r ? r.top : null, cw: document.documentElement.clientWidth,
          scrolls: (window.__SCROLLS__ || []).length,
          gutter: getComputedStyle(document.documentElement).scrollbarGutter};
})()
"""


def run_resizes_content(width, height, kb, shots):
    """⊕ Stage D review (Fable) — Android Chrome under this page's
    `interactive-widget=resizes-content`: the keyboard shrinks the LAYOUT
    viewport as well as the visual one, so innerHeight and
    visualViewport.height both read the room left. Compact mode must still
    engage and the box and Check must still be in view."""
    print("\n── Android resizes-content %d×%d, keyboard %d ──" % (width, height, kb))
    server, port = cdp.serve(ROOT)
    try:
        with cdp.Browser() as br:
            page = br.attach()
            page.send("Emulation.setDeviceMetricsOverride",
                      {"width": width, "height": height, "deviceScaleFactor": 1, "mobile": True})
            try:
                page.send("Emulation.setFocusEmulationEnabled", {"enabled": True})
            except cdp.CDPError:
                pass
            page.send("Page.addScriptToEvaluateOnNewDocument", {"source": FAKE + FAKE_VV})
            page.goto("http://127.0.0.1:%d/student/class-fixture.html" % port)
            settle(1.0)
            check(page.eval(LOAD) is True, "resizes-content %d: the page mounts" % width)
            page.eval("window.__FC_FAKE__.mode = 'review'")
            page.eval("window.__MRB_OPEN_HW__(%s)" % json.dumps(AID))
            settle(0.8)
            page.eval("document.querySelector('[data-hw=\"answer\"]').focus()")
            vis = height - kb
            page.send("Emulation.setDeviceMetricsOverride",
                      {"width": width, "height": vis, "deviceScaleFactor": 1, "mobile": True})
            page.eval("window.__KB__(%d)" % vis)
            settle(0.8)
            inner = page.eval("window.innerHeight")
            check(inner == vis, "resizes-content %d: the layout viewport followed the keyboard (%s)" % (width, inner))
            st = page.eval(STATE_JS)
            bx = page.eval(BOXES_JS)
            c = page.eval(CARD_JS)
            check(st["typing"] == "1" and st["focused"], "resizes-content %d: compact mode is on (%s)" % (width, st["typing"]))
            check(bx["tIn"] and bx["checkVisible"] and bx["qIn"],
                  "resizes-content %d: question, box and Check inside the %dpx left (box %s, vv %s)"
                  % (width, vis, bx["t"], bx["vv"]))
            # ⊕ MRB-354 unit B commander follow-up (2 Oct 2026) — this used to
            # read `c["card"] >= 120 - 0.5` (a FIXED floor, regardless of
            # content). That was the exact defect the follow-up fixed: a
            # 120px floor padded a short card past its own content and
            # starved the box of room it would otherwise have had, even
            # though `fitBox()` could not know to reclaim it. The card now
            # gets `min(content, available − a ~96px box floor)`, so a short
            # review card (this one, 97px) hands the extra room straight to
            # the box instead — `box {'h': 96}` just above, at its new
            # floor, is that room landing exactly where it should. The real
            # invariants are the ones already asserted around this line:
            # compact mode on, question+box+Check all inside the visible
            # 336px, the strip back once the keyboard goes down. What's left
            # to check about the card itself is only the UPPER bound and
            # that it never collapses to nothing.
            check(c["card"] >= 40 - 0.5 and c["card"] <= max(120, 0.34 * vis) + 0.5,
                  "resizes-content %d: the card is at least 40px, at most 120px or 34%% of the visual height (%.1f)"
                  % (width, c["card"]))
            shot(page, shots, "D-android-rc-%d-keyboard-up" % width)
            page.eval("document.activeElement.blur()")
            page.send("Emulation.setDeviceMetricsOverride",
                      {"width": width, "height": height, "deviceScaleFactor": 1, "mobile": True})
            page.eval("window.__KB__(null)")
            settle(0.6)
            st = page.eval(STATE_JS)
            check(st["typing"] is None and st["stripShown"], "resizes-content %d: keyboard down → the strip is back" % width)
    finally:
        server.shutdown()


def run_lift(width, height, mobile, shots):
    """⊕ Stage D, item 4 — clicking a homework row, opening the deck and
    closing it lift nothing: scrollY, the row's top and the page width hold,
    no scroll event fires, and the dialog arrives without Design's slide."""
    print("\n── item 4, %d×%d ──" % (width, height))
    server, port = cdp.serve(ROOT)
    try:
        with cdp.Browser() as br:
            page = br.attach()
            page.send("Emulation.setDeviceMetricsOverride",
                      {"width": width, "height": height, "deviceScaleFactor": 1, "mobile": mobile})
            page.send("Page.addScriptToEvaluateOnNewDocument", {"source": FAKE})
            page.goto("http://127.0.0.1:%d/student/class-fixture.html" % port)
            settle(1.0)
            page.eval(LOAD)
            page.eval("window.__FC_FAKE__.mode = 'review'")
            page.eval("(function(){var b=document.querySelector('[aria-expanded]');"
                      " window.scrollTo(0, Math.max(0, b.getBoundingClientRect().top + window.scrollY - %d));})()"
                      % (height // 2))
            settle(0.4)
            a = page.eval(LIFT_JS)
            page.eval("window.__SCROLLS__ = []; window.addEventListener('scroll', function(){"
                      " window.__SCROLLS__.push(window.scrollY); }, true);")
            page.eval("document.querySelector('[aria-expanded]').click()")
            settle(0.6)
            b = page.eval(LIFT_JS)
            shot(page, shots, "D-lift-%d-row-open" % width)
            page.eval("window.__MRB_OPEN_HW__(%s)" % json.dumps(AID))
            settle(0.05)
            anim = page.eval("(function(){var d=document.querySelector('[data-mrb-dialog=\"flashcards\"]'),"
                             " o=document.querySelector('[data-port-region=\"flashcards-overlay\"]');"
                             " return [d ? getComputedStyle(d).animationName : null, o ? getComputedStyle(o).animationName : null];})()")
            settle(0.6)
            c = page.eval(LIFT_JS)
            shot(page, shots, "D-lift-%d-deck-open" % width)
            page.eval("document.querySelector('[data-port-region=\"flashcards-overlay\"] button[title=\"Close\"]').click()")
            settle(0.6)
            d = page.eval(LIFT_JS)
            for step, x in (("the row expands", b), ("the deck opens", c), ("the deck closes", d)):
                check(abs(x["y"] - a["y"]) <= 1 and abs(x["top"] - a["top"]) <= 1 and abs(x["cw"] - a["cw"]) <= 1,
                      "%d×%d, %s: scrollY %s→%s, row top %.1f→%.1f, width %s→%s unchanged"
                      % (width, height, step, a["y"], x["y"], a["top"], x["top"], a["cw"], x["cw"]))
            check(d["scrolls"] == 0, "%d×%d: no scroll event fired across click, open and close (%d)" % (width, height, d["scrolls"]))
            check(anim == ["none", "fcIn"], "%d×%d: the dialog has no entrance slide; the scrim keeps its fade (%s)"
                  % (width, height, anim))
            check(a["gutter"] == "stable", "%d×%d: the class page keeps its scrollbar's room (%s)" % (width, height, a["gutter"]))
    finally:
        server.shutdown()


# ══ MRB-352 Stage D2 — "Your flashcards" (the library), on the fixture ═════
#
# The REAL `shared/flashcard-library.js` + `.css` on the compiled class page,
# with an in-page stand-in for the pupil's Supabase client (R3–R7 and the
# names table). `names_missing` makes the names table answer 42P01, which is
# production today: the degrade mode is proved here, never by DDL.
LIB_FAKE = r"""
(function () {
  var AID = "__AID__";
  var F = window.__LIB_FAKE__ = {namesMissing: false, names: {}, writes: [], failSets: false};
  var cards = [
    {id: "c0000000-0000-4000-8000-000000000001", position: 0, question: "What is the unit of force?", answer: "The newton (N)"},
    {id: "c0000000-0000-4000-8000-000000000002", position: 1, question: "What is the formula of water?", answer: "H2O"},
    {id: "c0000000-0000-4000-8000-000000000003", position: 2, question: "What is weight?", answer: "The force acting on an object due to gravity"},
    {id: "c0000000-0000-4000-8000-000000000004", position: 3, question: "Write the equation for the force on a spring.", answer: "Force = spring constant × extension (F = ke)"},
    {id: "c0000000-0000-4000-8000-000000000005", position: 4, question: "Is velocity a scalar or a vector?", answer: "A vector"}
  ];
  F.cards = cards;
  function answer(t, op, body, filters) {
    if (t === "assignments") {
      if (F.failSets) return {data: null, error: {code: "500", message: "down"}};
      return {data: [{id: AID, title: "Forces flashcards", class_id: "k1", subject_id: "s1",
        created_at: "2026-09-21T08:00:00Z", release_at: null, subject: {name: "Physics"}, "class": {name: "10h/Ph1"}}], error: null};
    }
    if (t === "flashcard_set_names") {
      if (F.namesMissing) return {data: null, error: {code: "42P01", message: "relation does not exist"}};
      if (op === "select") return {data: Object.keys(F.names).map(function (k) { return {assignment_id: k, name: F.names[k]}; }), error: null};
      F.writes.push({op: op, body: body});
      if (op === "upsert") { F.names[body.assignment_id] = body.name; }
      if (op === "delete") { delete F.names[filters.assignment_id]; }
      return {data: null, error: null};
    }
    if (t === "assignment_flashcards") return {data: cards.slice(), error: null};
    if (t === "flashcard_pupil_cards") return {data: [{card_id: cards[0].id, pupil_answer: "newton"}], error: null};
    if (t === "flashcard_reviews") return {data: [{card_id: cards[1].id, answer: "h2o", rated_at: "2026-09-22T10:00:00Z"}], error: null};
    return {data: [], error: null};
  }
  F.reads = [];
  F.sb = {from: function (t) {
    var op = "select", body = null, filters = {}, sel = null;
    var b = {
      select: function (x) { sel = x; return b; },
      upsert: function (x) { op = "upsert"; body = x; return b; },
      delete: function () { op = "delete"; return b; },
      eq: function (k, v) { filters[k] = v; return b; },
      "in": function () { return b; }, is: function () { return b; }, not: function () { return b; },
      order: function () { return b; }, range: function () { return b; },
      then: function (ok, bad) {
        F.reads.push({t: t, op: op, sel: sel});
        var r = answer(t, op, body, filters);
        return new Promise(function (res) { setTimeout(function () { res(r); }, 5); }).then(ok, bad);
      }
    };
    return b;
  }};
})();
""".replace("__AID__", AID)

LIB_STATE = r"""
(function () {
  var $ = function (s) { return document.querySelector(s); };
  var root = $('[data-mrb-library]');
  var vis = function (e) { return !!e && !e.closest('[hidden]') && e.getBoundingClientRect().height > 0; };
  var surface = $('[data-bench-surface="cards"]');
  var rows = Array.prototype.map.call(document.querySelectorAll('[data-lib="set-row"]'), function (r) {
    return {name: r.children[0].innerText.trim(), meta: r.children[1].innerText.trim()}; });
  var dlg = $('[data-mrb-library] .mrbl-dlg');
  return {
    buttons: document.querySelectorAll('[data-mrb-library-open]').length,
    inSurface: !!surface && !!surface.querySelector('[data-mrb-library-open]'),
    open: !!root && !root.hasAttribute('hidden'),
    hash: location.hash,
    rows: rows,
    listShown: vis($('[data-lib="list"]')),
    front: vis($('[data-lib="q"]')) ? $('[data-lib="q"]').innerText.trim() : null,
    back: $('[data-lib="a"]') ? $('[data-lib="a"]').innerText.trim() : null,
    mine: vis($('[data-lib="mine-block"]')) ? $('[data-lib="mine"]').innerText.trim() : null,
    flip: $('[data-lib="card"]') ? $('[data-lib="card"]').getAttribute('data-flip') : null,
    pos: vis($('[data-lib="pos"]')) ? $('[data-lib="pos"]').innerText.trim() : null,
    name: vis($('[data-lib="name"]')) ? $('[data-lib="name"]').innerText.trim() : null,
    input: vis($('[data-lib="name-input"]')) ? $('[data-lib="name-input"]').value : null,
    shuffle: $('[data-lib="shuffle"]') ? $('[data-lib="shuffle"]').getAttribute('aria-pressed') : null,
    err: vis($('[data-lib="err"]')) ? $('[data-lib="err"]').innerText.trim() : null,
    dlgBg: dlg ? getComputedStyle(dlg).backgroundColor : null,
    anim: dlg ? getComputedStyle(dlg).animationName : null,
    scrimAnim: root ? getComputedStyle(root).animationName : null,
    scrollY: window.scrollY,
    cw: document.documentElement.clientWidth,
    text: root && !root.hasAttribute('hidden') ? root.innerText : "",
    overflowX: document.documentElement.scrollWidth > window.innerWidth + 1
  };
})()
"""


def run_library(width, height, mobile, shots):
    print("\n── library, %d×%d%s ──" % (width, height, " mobile" if mobile else ""))
    server, port = cdp.serve(ROOT)
    tag = "%d" % width
    n = [0]

    def shot(page, name):
        n[0] += 1
        res = page.send("Page.captureScreenshot", {"format": "png", "fromSurface": True})
        path = os.path.join(shots, "lib-%s-%02d-%s.png" % (tag, n[0], name))
        with open(path, "wb") as fh:
            fh.write(base64.b64decode(res["data"]))

    try:
        with cdp.Browser() as br:
            page = br.attach()
            page.send("Emulation.setDeviceMetricsOverride",
                      {"width": width, "height": height, "deviceScaleFactor": 2 if mobile else 1,
                       "mobile": mobile})
            page.send("Page.addScriptToEvaluateOnNewDocument", {"source": LIB_FAKE})
            url = "http://127.0.0.1:%d/student/class-fixture.html" % port

            def boot(ready=True):
                page.goto(url)
                settle(1.0)
                return page.eval(r"""(async function () {
                  function add(src) { return new Promise(function (ok, bad) {
                    var s = document.createElement('script'); s.src = src; s.onload = ok; s.onerror = bad; document.head.appendChild(s); }); }
                  await add('/shared/formulae.js');
                  await add('/shared/flashcard-library.js');
                  window.__MRB_LIBRARY_READY__ = %s;
                  window.MRBFlashcardLibrary.offer(window.__LIB_FAKE__.sb, 'pupil-uid', {'%s': 5});
                  await new Promise(function (r) { setTimeout(r, 300); });
                  return !!window.MRBFlashcardLibrary;
                })()""" % (json.dumps([AID] if ready else []), AID))

            def st():
                return page.eval(LIB_STATE)

            def click(sel):
                ok = page.eval("(function(){var e=document.querySelector(%s); if(!e) return false; e.click(); return true;})()"
                               % json.dumps(sel))
                settle(0.35)
                return ok

            def key(sel, k):
                page.eval("(function(){var e=document.querySelector(%s)||document.body;"
                          "e.dispatchEvent(new KeyboardEvent('keydown',{key:%s,bubbles:true,cancelable:true}));})()"
                          % (json.dumps(sel), json.dumps(k)))
                settle(0.35)

            # ── no qualifying set: no button ────────────────────────────
            check(boot(ready=False) is True, "library script loads on the class page")
            check(st()["buttons"] == 0, "%s: no set qualifies → no 'View your flashcards' button" % tag)
            shot(page, "no-sets-no-button")

            # ── one qualifying set ──────────────────────────────────────
            boot()
            page.eval("(function(){var s=document.querySelector('[data-bench-surface=\"cards\"]');"
                      "if(s) window.scrollTo(0, Math.max(0, s.getBoundingClientRect().top + scrollY - 120));})()")
            settle(0.3)
            s = st()
            check(s["buttons"] == 1 and s["inSurface"],
                  "%s: one 'View your flashcards' button, inside the FLASHCARDS card" % tag)
            label = page.eval("document.querySelector('[data-mrb-library-open]').innerText.trim()")
            check(label == "View your flashcards", "%s: the button reads 'View your flashcards' (got %r)" % (tag, label))
            # a redraw (open and close the practice deck) keeps exactly one button
            click('[data-port-region="sidebar-flashcards"] button')
            click('[data-port-region="flashcards-overlay"] button[title="Close"]')
            s = st()
            check(s["buttons"] == 1 and s["inSurface"], "%s: the button survives a redraw, once" % tag)
            shot(page, "class-page-button")
            y0, cw0 = s["scrollY"], s["cw"]

            # ── the sets ────────────────────────────────────────────────
            click('[data-mrb-library-open]')
            settle(0.3)
            s = st()
            check(s["open"] and s["hash"] == "#sets" and len(s["rows"]) == 1,
                  "%s: tap → '#sets', the list of 1 (got %r %r)" % (tag, s["hash"], s["rows"]))
            check(s["rows"] and s["rows"][0] == {"name": "Forces flashcards", "meta": "5 CARDS"},
                  "%s: the row is the teacher's title and '5 CARDS', no class name (got %r)" % (tag, s["rows"]))
            check(s["anim"] == "none" and s["scrimAnim"] == "mrblIn", "%s: the scrim fades, the column does not slide" % tag)
            check(s["cw"] == cw0, "%s: opening changes no width behind it (%s → %s)" % (tag, cw0, s["cw"]))
            check("Your flashcards" in s["text"] and not s["overflowX"], "%s: header 'Your flashcards', no sideways scroll" % tag)
            shot(page, "L-sets")

            # ── one set: front, back, move, wrap ────────────────────────
            click('[data-lib="set-row"]')
            s = st()
            check(s["hash"] == "#set=" + AID and s["front"] == "What is the unit of force?" and s["pos"] == "1 / 5"
                  and s["name"] == "Forces flashcards" and s["flip"] == "0",
                  "%s: open → card 1's question, '1 / 5', the set's name in the header (got %r %r %r)"
                  % (tag, s["front"], s["pos"], s["name"]))
            pen = page.eval("(function(){var p=document.querySelector('[data-lib=\"name\"] svg');"
                            "return p ? [p.getAttribute('aria-hidden'), getComputedStyle(p).display] : null;})()")
            check(pen == ["true", "block"] or (pen and pen[0] == "true" and pen[1] != "none"),
                  "%s: the set's name carries a small pencil, hidden from screen readers (got %r)" % (tag, pen))
            hidden_back = page.eval("document.querySelector('[data-lib=\"back-face\"]').getAttribute('aria-hidden')")
            check(hidden_back == "true", "%s: face up, the answer side is hidden" % tag)
            shot(page, "L-card-front")
            click('[data-lib="card"]')
            settle(0.4)
            s = st()
            check(s["flip"] == "1" and s["back"] == "The newton (N)" and s["mine"] == "newton",
                  "%s: tap → the model answer, with YOUR ANSWER beneath (got %r %r)" % (tag, s["back"], s["mine"]))
            shot(page, "L-card-back")
            click('[data-lib="next"]')
            s = st()
            check(s["pos"] == "2 / 5" and s["front"] == "What is the formula of water?" and s["flip"] == "0",
                  "%s: › → card 2, face up (got %r)" % (tag, s["pos"]))
            click('[data-lib="prev"]')
            click('[data-lib="prev"]')
            s = st()
            check(s["pos"] == "5 / 5" and s["front"] == "Is velocity a scalar or a vector?",
                  "%s: ‹ from card 1 wraps to card 5 (got %r)" % (tag, s["pos"]))
            key('body', 'ArrowRight')
            check(st()["pos"] == "1 / 5", "%s: → key moves on (wraps to 1)" % tag)

            # ── shuffle ─────────────────────────────────────────────────
            click('[data-lib="shuffle"]')
            fronts = []
            for _ in range(5):
                fronts.append(st()["front"])
                click('[data-lib="next"]')
            deck = ["What is the unit of force?", "What is the formula of water?", "What is weight?",
                    "Write the equation for the force on a spring.", "Is velocity a scalar or a vector?"]
            check(st()["shuffle"] == "true" and sorted(fronts) == sorted(deck) and fronts != deck,
                  "%s: Shuffle → every card once, in a new order (got %r)" % (tag, fronts))
            shot(page, "L-shuffled")
            click('[data-lib="shuffle"]')
            check(st()["shuffle"] == "false", "%s: Shuffle again → back to the teacher's order" % tag)

            # ── rename in place ─────────────────────────────────────────
            click('[data-lib="name"]')
            s = st()
            check(s["input"] == "Forces flashcards", "%s: tap the name → a box holding the current name" % tag)
            page.eval("(function(){var i=document.querySelector('[data-lib=\"name-input\"]'); i.value='My forces set';"
                      "i.dispatchEvent(new Event('input',{bubbles:true}));})()")
            shot(page, "L-rename")
            key('[data-lib="name-input"]', 'Enter')
            settle(0.3)
            s = st()
            F = page.eval("window.__LIB_FAKE__")
            check(s["name"] == "My forces set" and F["names"].get(AID) == "My forces set"
                  and any(w["op"] == "upsert" and w["body"]["pupil_id"] == "pupil-uid" for w in F["writes"]),
                  "%s: Enter → the header says 'My forces set', upserted as the pupil (got %r %r)"
                  % (tag, s["name"], F["names"]))
            shot(page, "L-renamed")
            click('[data-lib="name"]')
            page.eval("document.querySelector('[data-lib=\"name-input\"]').value='x'")
            key('[data-lib="name-input"]', 'Escape')
            s = st()
            check(s["open"] and s["name"] == "My forces set", "%s: Escape in the box cancels, and does not close" % tag)
            click('[data-lib="name"]')
            page.eval("document.querySelector('[data-lib=\"name-input\"]').value='   '")
            key('[data-lib="name-input"]', 'Enter')
            settle(0.3)
            s = st()
            F = page.eval("window.__LIB_FAKE__")
            check(s["name"] == "Forces flashcards" and AID not in F["names"],
                  "%s: a blank name → the teacher's title again, the row deleted (got %r)" % (tag, s["name"]))

            # ── Back steps out: set → sets → the class page ─────────────
            page.eval("history.back()")
            settle(0.5)
            s = st()
            check(s["open"] and s["hash"] == "#sets" and s["listShown"], "%s: Back → the list (got %r)" % (tag, s["hash"]))
            check(s["rows"] and s["rows"][0]["name"] == "Forces flashcards", "%s: the list carries the current name" % tag)
            page.eval("history.back()")
            settle(0.5)
            s = st()
            check(not s["open"] and s["hash"] == "", "%s: Back again → closed, no fragment (got %r)" % (tag, s["hash"]))
            check(abs(s["scrollY"] - y0) <= 1 and s["cw"] == cw0,
                  "%s: the class page did not move (scrollY %s → %s)" % (tag, y0, s["scrollY"]))

            # ── × and Escape close from a set ───────────────────────────
            click('[data-mrb-library-open]')
            click('[data-lib="set-row"]')
            click('[data-lib="close"]')
            settle(0.4)
            s = st()
            check(not s["open"] and s["hash"] == "", "%s: × from a set closes, no fragment left (got %r)" % (tag, s["hash"]))
            click('[data-mrb-library-open]')
            key('body', 'Escape')
            settle(0.4)
            s = st()
            check(not s["open"] and s["hash"] == "" and abs(s["scrollY"] - y0) <= 1,
                  "%s: Escape closes; scrollY unchanged across every open/close" % tag)

            # ── a direct link opens the set ─────────────────────────────
            page.eval("location.hash = '#set=%s'" % AID)
            settle(0.5)
            s = st()
            check(s["open"] and s["front"] == "What is the unit of force?" and s["pos"] == "1 / 5",
                  "%s: a #set= link opens that set, on card 1 (got %r %r %r)" % (tag, s["open"], s["front"], s["pos"]))
            click('[data-lib="close"]')
            check(not st()["open"], "%s: × on a direct link closes" % tag)

            # ── dark ────────────────────────────────────────────────────
            page.eval("document.documentElement.setAttribute('data-theme','dark')")
            settle(0.3)
            click('[data-mrb-library-open]')
            s = st()
            check(s["dlgBg"] not in ("rgb(251, 243, 230)", None), "%s: dark theme reaches the library (bg %s)" % (tag, s["dlgBg"]))
            shot(page, "L-dark-sets")
            click('[data-lib="set-row"]')
            shot(page, "L-dark-front")
            click('[data-lib="card"]')
            settle(0.5)
            shot(page, "L-dark-back")
            click('[data-lib="close"]')
            page.eval("document.documentElement.removeAttribute('data-theme')")

            # ── the list fails to load ──────────────────────────────────
            boot()
            page.eval("window.__LIB_FAKE__.failSets = true")
            click('[data-mrb-library-open]')
            s = st()
            check(s["err"] and s["err"].startswith("Your flashcards did not load.") and "Try again" in s["err"],
                  "%s: a failed list → 'Your flashcards did not load.' + Try again (got %r)" % (tag, s["err"]))
            shot(page, "L-list-failed")
            page.eval("window.__LIB_FAKE__.failSets = false")
            click('[data-lib="retry"]')
            s = st()
            check(s["err"] is None and len(s["rows"]) == 1, "%s: Try again → the list" % tag)
            click('[data-lib="close"]')

            # ── DEGRADE: no names table (production until the migration) ─
            boot()
            page.eval("window.__LIB_FAKE__.namesMissing = true; localStorage.removeItem('mrbadmusai.fcset.v1.names')")
            click('[data-mrb-library-open]')
            click('[data-lib="set-row"]')
            click('[data-lib="name"]')
            page.eval("document.querySelector('[data-lib=\"name-input\"]').value='Revision: forces'")
            key('[data-lib="name-input"]', 'Enter')
            settle(0.3)
            s = st()
            stored = page.eval("localStorage.getItem('mrbadmusai.fcset.v1.names')")
            F = page.eval("window.__LIB_FAKE__")
            check(s["name"] == "Revision: forces" and stored and json.loads(stored).get(AID) == "Revision: forces"
                  and not F["writes"],
                  "%s: no names table → the name is kept on the device, no server write (got %r %r)"
                  % (tag, s["name"], stored))
            check(not any(w in s["text"] for w in ("device", "phone", "saved", "offline", "Saved")),
                  "%s: degrade mode says nothing about it on screen" % tag)
            shot(page, "L-degrade-renamed")
            click('[data-lib="close"]')
            # reload: the device name persists
            boot()
            page.eval("window.__LIB_FAKE__.namesMissing = true")
            click('[data-mrb-library-open]')
            s = st()
            check(s["rows"] and s["rows"][0]["name"] == "Revision: forces", "%s: device name survives a reload" % tag)
            click('[data-lib="close"]')
            # the table arrives: the device name is written up once and the key cleared
            boot()
            click('[data-mrb-library-open]')
            settle(0.4)
            s = st()
            F = page.eval("window.__LIB_FAKE__")
            stored = page.eval("localStorage.getItem('mrbadmusai.fcset.v1.names')")
            check(F["names"].get(AID) == "Revision: forces" and stored is None
                  and s["rows"] and s["rows"][0]["name"] == "Revision: forces"
                  and sum(1 for w in F["writes"] if w["op"] == "upsert") == 1,
                  "%s: the table arrives → the device name is upserted once, the local key cleared (got %r %r)"
                  % (tag, F["names"], stored))
            click('[data-lib="close"]')
            page.eval("localStorage.clear()")

            # ── reads: one serving read, no writes but a name ───────────
            reads = page.eval("window.__LIB_FAKE__.reads")
            tables = sorted(set(r["t"] for r in reads))
            check(set(tables) <= {"assignments", "flashcard_set_names", "assignment_flashcards",
                                  "flashcard_pupil_cards", "flashcard_reviews"},
                  "%s: the library reads only its five tables (got %r)" % (tag, tables))
            check(all(r["op"] == "select" for r in reads if r["t"] != "flashcard_set_names"),
                  "%s: nothing written but a name" % tag)
    finally:
        server.shutdown()



# ══ ⊕ 8 Oct 2026 — FLASHCARDS, ROUND 3 ═════════════════════════════════════
# Unit 1: Secured is greyed until the SUBMITTED answer is a real attempt.
# Unit 2: the Mr Badmus nudge on Done when 3+ cards were shaky.
# ⊕ 9 Oct 2026 — round 3 used to write its screenshots straight into
# `docs/experience/y-shots/` on EVERY run (a module constant that ignored
# `--shots`), so a gate run overwrote committed reference images and dirtied
# the tree it was attesting. MRB-346 rule 5: a drive never writes into the
# repo by default. Round 3 now writes where every other section of this drive
# does — `--shots`, else `gate_tmp()/flashcard-homework`. To refresh the
# committed set on purpose: `--round3 --shots docs/experience/y-shots`.
CRUDE_Q = "Describe how crude oil is formed."
CRUDE_A = "Plankton died, were buried under sediment and compressed via heat and pressure over millions of years"
# a model-answer word for every card (a real attempt; the floor judges effort)
R3_REAL = {"What is the unit of force?": "newton", "What is the formula of water?": "water",
           "What is weight?": "gravity", "Write the equation for the force on a spring.": "F = ke",
           CRUDE_Q: "plants died, got buried, heat and pressure"}

CONTRAST_JS = r"""
(function (sel) {
  var b = document.querySelector(sel); if (!b) return null;
  function rgb(c) { var m = c.match(/[\d.]+/g) || []; return m.map(Number); }
  function lum(c) { return c.slice(0, 3).map(function (v) { v /= 255; return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4); })
    .reduce(function (a, v, i) { return a + v * [0.2126, 0.7152, 0.0722][i]; }, 0); }
  var fg = rgb(getComputedStyle(b).color), el = b, bg = null;
  while (el) { var c = rgb(getComputedStyle(el).backgroundColor); if (c.length >= 3 && (c.length < 4 || c[3] > 0.5)) { bg = c; break; } el = el.parentElement; }
  if (!bg) bg = [255, 255, 255];
  var a = lum(fg), z = lum(bg); return (Math.max(a, z) + 0.05) / (Math.min(a, z) + 0.05);
})
"""

FIT_JS = r"""
(function () {
  var dlg = document.querySelector('[data-mrb-dialog="flashcards"]');
  function r(sel) { var e = document.querySelector(sel); if (!e) return null; var b = e.getBoundingClientRect();
    return {top: b.top, bottom: b.bottom, left: b.left, right: b.right, h: b.height}; }
  var d = dlg ? dlg.getBoundingClientRect() : null;
  var root = document.scrollingElement || document.documentElement;
  return {vh: window.innerHeight, vw: window.innerWidth,
          dlg: d ? {top: d.top, bottom: d.bottom} : null,
          dlgScroll: dlg ? dlg.scrollHeight - dlg.clientHeight : null,
          pageScroll: root.scrollHeight - window.innerHeight,
          panel: r('[data-hw="panel"]'), nudge: r('[data-hw="nudge"]'), label: r('[data-hw="nudge-label"]'),
          text: r('[data-hw="nudge-text"]'), done: r('[data-hw="done"]'), again: r('[data-hw="again"]'),
          end1: r('[data-hw="end1"]')};
})()
"""


def run_round3(width, height, mobile, theme, shots):
    print("\n── round 3: %d×%d %s, %s ──" % (width, height, "phone" if mobile else "desktop", theme))
    if shots:
        os.makedirs(shots, exist_ok=True)
    fake = (FAKE.replace('{id: "c0000000-0000-4000-8000-000000000005", position: 4, question: "Is velocity a scalar or a vector?", answer: "A vector"}',
                         '{id: "c0000000-0000-4000-8000-000000000005", position: 4, question: "%s", answer: "%s"}' % (CRUDE_Q, CRUDE_A)))
    assert CRUDE_A in fake
    server, port = cdp.serve(ROOT)
    tag = "%dx%d-%s" % (width, height, theme)

    def snap(page, name):
        if not shots:
            return
        res = page.send("Page.captureScreenshot", {"format": "png", "fromSurface": True})
        with open(os.path.join(shots, "r3-%s-%s.png" % (name, tag)), "wb") as fh:
            fh.write(base64.b64decode(res["data"]))

    try:
        with cdp.Browser() as br:
            page = br.attach()
            page.send("Emulation.setDeviceMetricsOverride",
                      {"width": width, "height": height, "deviceScaleFactor": 2 if mobile else 1, "mobile": mobile})
            if mobile:
                page.send("Emulation.setTouchEmulationEnabled", {"enabled": True, "maxTouchPoints": 5})
            try:
                page.send("Emulation.setFocusEmulationEnabled", {"enabled": True})
            except cdp.CDPError:
                pass
            page.send("Page.addScriptToEvaluateOnNewDocument", {"source": fake})
            page.goto("http://127.0.0.1:%d/student/class-fixture.html" % port)
            settle(1.0)
            P = Phone(page, width, height, 0, None)
            check(P.q(LOAD) is True, "r3 %s: the page mounts" % tag)
            if theme == "dark":
                P.q("document.documentElement.setAttribute('data-theme','dark')")
            P.q("window.__FC_FAKE__.mode = 'review'; window.MRBHomework.modelCheck = null;")

            def fresh_deck():
                P.q("window.MRBHomework._reset(); localStorage.clear(); window.__FC_FAKE__.events.length = 0; "
                    "window.__FC_FAKE__.rows.length = 0; window.__FC_FAKE__.seen = {}; window.MRBHomework.modelCheck = null;")
                P.q("window.__MRB_OPEN_HW__(%s)" % json.dumps(AID))
                settle(0.6)

            def got():
                return P.q("""(function(){var b=document.querySelector('[data-hw="got_it"]'); if(!b) return null;
                  return {disabled: b.disabled, aria: b.getAttribute('aria-disabled'),
                          opacity: parseFloat(getComputedStyle(b).opacity)};})()""")

            # ── unit 1: mash → Secured greyed; one real word → open; own words after idk → open ──
            fresh_deck()
            P.type("asdf kkkk")
            P.click('[data-hw="check"]')
            s = P.st()
            g = got()
            check(s["rating"] and s["enabled"] == ["not_yet", "nearly"]
                  and g["disabled"] is True and g["aria"] == "true" and abs(g["opacity"] - 0.4) < 0.02,
                  "r3 %s: after a mash Check, Secured is greyed (disabled, aria-disabled true, opacity .4); Nearly / Not yet open (got %r %r)"
                  % (tag, s["enabled"], g))
            front = s["front"]
            P.q("window.MRBHomework.active.rate('got_it')")        # what key 3 and swipe-right call
            settle(0.2)
            check(P.st()["front"] == front and P.st()["rating"],
                  "r3 %s: the 3 key / swipe-right (rate('got_it')) do nothing while floored" % tag)
            snap(page, "greyed-secured")
            P.click('[data-hw="not_yet"]')
            # card 2: one real word opens it
            P.type("water")
            P.click('[data-hw="check"]')
            g = got()
            check(P.st()["enabled"] == ["not_yet", "nearly", "got_it"] and g["disabled"] is False and abs(g["opacity"] - 1) < 0.02,
                  "r3 %s: one real word ('water' for H2O) opens Secured" % tag)
            P.click('[data-hw="got_it"]')
            # card 3: I don't know, mashed own words stay greyed, real own words open
            P.click('[data-hw="idk"]')
            P.type("zzzz qqqq")
            P.click('[data-hw="check"]')
            check(P.st()["enabled"] == ["not_yet", "nearly"], "r3 %s: I don't know, then mashed own words: Secured stays greyed" % tag)
            P.click('[data-hw="nearly"]')
            # card 4 (spring): just rate Nearly; card 5 crude oil own words
            P.type("zzz")
            P.click('[data-hw="check"]')
            P.click('[data-hw="not_yet"]')
            check(P.st()["front"] == CRUDE_Q, "r3 %s: reached the crude-oil card" % tag)
            P.click('[data-hw="idk"]')
            P.type("plants died, got buried, heat and pressure")
            P.click('[data-hw="check"]')
            check(P.st()["enabled"] == ["not_yet", "nearly", "got_it"],
                  "r3 %s: crude oil in the pupil's own words after I don't know opens Secured" % tag)

            # ── unit 2: the nudge ────────────────────────────────────────────
            def play(idk_fronts):
                fresh_deck()
                seen = set()
                for _ in range(20):
                    st = P.st()
                    if st["end1"]:
                        break
                    f = st["front"]
                    if f in idk_fronts and f not in seen:
                        seen.add(f)
                        P.click('[data-hw="idk"]')
                    P.type(R3_REAL[f])
                    P.click('[data-hw="check"]')
                    P.click('[data-hw="got_it"]')
                settle(0.8)
                return P.st()

            s = play({"What is the unit of force?", "What is the formula of water?", "What is weight?"})
            check(s["end1"] == "5 of 5 secured" and s["done"] == "Done" and s["again"] == "Revise flashcards one more time",
                  "r3 %s: 3 idk-then-secured: Done screen, Done primary, Revise secondary (got %r %r)" % (tag, s["end1"], s["done"]))
            nudge = P.q("!!document.querySelector('[data-hw=\"nudge\"]')")
            label = P.q("(document.querySelector('[data-hw=\"nudge-label\"]')||{}).textContent")
            body = P.q("(document.querySelector('[data-hw=\"nudge-text\"]')||{}).textContent")
            check(nudge and (label or "").strip().lower() == "a note from mr badmus"
                  and body == "Nice one for finishing. A few of these weren't quite there yet, so one more run before class would lock them in.",
                  "r3 %s: the nudge shows with 3 shaky cards, with the agreed wording (got %r / %r)" % (tag, label, body))
            check(P.q("document.querySelector('[data-hw=\"nudge\"]').getAttribute('aria-live')") == "polite",
                  "r3 %s: the nudge is an aria-live polite region" % tag)
            f = P.q(FIT_JS)
            inside = lambda r: r is not None and r["top"] >= -0.5 and r["bottom"] <= f["vh"] + 0.5 and r["left"] >= -0.5 and r["right"] <= f["vw"] + 0.5
            check(inside(f["nudge"]) and inside(f["done"]) and inside(f["again"]) and inside(f["end1"]),
                  "r3 %s: nudge, N of M, Done and Revise all inside the viewport, none clipped (nudge=%s done=%s again=%s)"
                  % (tag, f["nudge"], f["done"], f["again"]))
            # (the class page behind the overlay scrolls on its own; what matters is the dialog)
            check((f["dlgScroll"] or 0) <= 1 and f["dlg"]["top"] >= -0.5 and f["dlg"]["bottom"] <= f["vh"] + 0.5,
                  "r3 %s: the dialog neither scrolls nor overflows the screen with the nudge showing (dialog scroll %s, %s)"
                  % (tag, f["dlgScroll"], f["dlg"]))
            check(f["nudge"]["top"] >= f["end1"]["bottom"] - 0.5 and f["nudge"]["bottom"] <= f["done"]["top"] + 0.5,
                  "r3 %s: the note sits under 'N of M secured' and above Done" % tag)
            c_text = P.q("(%s)('[data-hw=\"nudge-text\"]')" % CONTRAST_JS)
            c_label = P.q("(%s)('[data-hw=\"nudge-label\"]')" % CONTRAST_JS)
            check(c_text is not None and c_text >= 4.5 and c_label is not None and c_label >= 4.5,
                  "r3 %s: nudge text contrast %.2f and label contrast %.2f, both >= 4.5" % (tag, c_text or 0, c_label or 0))
            check(not P.st()["overflowX"], "r3 %s: no sideways scroll" % tag)
            snap(page, "nudge")
            ev = P.q("window.__FC_FAKE__.events")
            check(sum(1 for e in ev if e["type"] == "session_finish") == 1, "r3 %s: the nudge changed nothing about finishing" % tag)
            P.click('[data-hw="done"]')
            check(not P.st()["open"], "r3 %s: Done still closes the overlay" % tag)

            s = play({"What is the unit of force?", "What is the formula of water?"})
            check(s["end1"] == "5 of 5 secured" and not P.q("!!document.querySelector('[data-hw=\"nudge\"]')"),
                  "r3 %s: only 2 idk-then-secured: no nudge" % tag)
            snap(page, "no-nudge")
            # Revise one more time starts a new run: 0 shaky afterwards, no nudge on the next Done
            P.click('[data-hw="again"]')
            for _ in range(20):
                st = P.st()
                if st["end1"]:
                    break
                P.type(R3_REAL[st["front"]])
                P.click('[data-hw="check"]')
                P.click('[data-hw="got_it"]')
            settle(0.6)
            check(P.st()["end1"] == "5 of 5 secured" and not P.q("!!document.querySelector('[data-hw=\"nudge\"]')"),
                  "r3 %s: a fresh run after Revise with no shaky cards shows no nudge" % tag)
    finally:
        server.shutdown()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--shots", default=None)
    ap.add_argument("--round3", action="store_true", help="only the round 3 drives (floor + nudge)")
    ap.add_argument("--library", action="store_true",
                    help="only the flashcard library section (MRB-352 Stage D2)")
    a = ap.parse_args()
    shots = a.shots or os.path.join(cdp.gate_tmp(), "flashcard-homework")
    os.makedirs(shots, exist_ok=True)
    live = open(os.path.join(ROOT, "shared", "student-live.js"), encoding="utf-8").read()
    check('"/shared/flashcard-keyboard.js"' in live and "H.modelCheck = function" in live
          and "H.resumeRead = function" in live and "H.transportKeepalive = function" in live
          and "keepalive: true" in live,
          "the live page loads the keyboard module and wires the model check and the resume read")
    check("e.flip()" not in live, "the live page no longer turns a card with Space")
    check('document.body.style.overflow = on ? "hidden"' not in live,
          "Stage D item 4: the scroll lock hides the root only (html+body hidden clamped the page to the top)")
    check('.eq("id", wanted).is("deleted_at", null)' in live and '"pageshow"' in live,
          "§13.6: the kind read skips deleted sets; a page back from the bfcache reloads")
    if a.round3:
        for w, h, mobile in ((390, 844, True), (360, 640, True), (1280, 800, False)):
            for theme in ("light", "dark"):
                run_round3(w, h, mobile, theme, shots)
    if a.round3:
        pass
    elif not a.library:
        for w, h, kb in ((390, 844, 508), (360, 740, 404)):
            run(w, h, kb, shots)
        for w, h, tall in ((1440, 900, True), (1280, 720, True), (1366, 660, False)):
            run_desktop(w, h, shots, tall)
        for w, h, kb in ((360, 740, 404), (390, 844, 336)):
            run_resizes_content(w, h, kb, shots)
        # ⊕ 8 Oct 2026 — round 3: the Secured floor and the Mr Badmus nudge
        for w, h, mobile in ((390, 844, True), (360, 640, True), (1280, 800, False)):
            for theme in ("light", "dark"):
                run_round3(w, h, mobile, theme, shots)

        for w, h, mobile in ((1440, 900, False), (390, 844, True)):
            run_lift(w, h, mobile, shots)
    # ⊕ MRB-352 Stage D2 — the library, phone and desktop
    for w, h, mobile in (() if a.round3 else ((390, 844, True), (1440, 900, False))):
        run_library(w, h, mobile, shots)
    print("\n  screenshots: %s" % shots)
    if FAILS:
        print("\n  FAIL — %d check(s) failed" % len(FAILS))
        sys.exit(1)
    print("\n  PASS — flashcard homework, pupil flow, on a phone with the keyboard up")


if __name__ == "__main__":
    main()
