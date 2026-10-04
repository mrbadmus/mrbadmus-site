#!/usr/bin/env python3
"""MRB-354 unit B / Y UNIT 1 — phone-keyboard layout of the flashcard homework
typing screen.

Round 1 (MRB-354 unit B) fixed the dead gap between the box and Check and
added the card-priority split (`fitCard()`+`fitBox()`). Round 2 (Y Unit 1,
Mide's 4 Oct 2026 iPhone report on the real feature) found three more real
bugs round 1 never tested for:

  (a) nothing ever focuses the answer box on "I don't know" — the keyboard
      does not reliably open, and the NEXT redraw's path-based refocus can
      land on Check instead (the tap button that used to sit where the box's
      path now points disappears from the row).
  (b) the learn step's layout gave the CARD priority by raw content height,
      with no idea the model answer existed inside it — a real iPhone's
      keyboard (plus its QuickType/accessory bar, which the ORIGINAL version
      of this tool simulated as a flat 388px cut) leaves more like 380–420px
      visible, not the ~456px the old constant implied, and production cards
      (a two-line question, a two-to-three-line answer) overflowed the card
      with no scroll cue and no guarantee the answer was what overflowed
      into view.
  (c) the answer box's rest-state border was `--pg-rule-strong` on
      `--pg-card` — 2.05:1 light, 1.7:1 dark, well under the 3:1 non-text
      floor: faint cream on cream, "not obviously a box to type into."

    python3 tools/flashcard_phone_layout.py

Drives the COMPILED fixture (`student/class-fixture.html`, the real
`shared/flashcard-homework.js` + `shared/flashcard-keyboard.js`), the same way
`flashcard_homework_drive.py` does.

TWO KEYBOARD MECHANISMS, BECAUSE THE CLASS PAGE ASKS FOR TWO.

  iOS-shaped devices (390×844, 360×740) stub `window.visualViewport` (iOS
  shrinks ONLY the visual viewport on focus, never the layout viewport) and
  fire a `resize` at it via `window.__KB__(height, offsetTop)` — the same
  pattern `flashcard_homework_drive.py` already uses, because Chrome itself
  cannot reproduce that split. The shrunk heights used here (~400 at
  390×844, ~340 at 360×740) are what a real iPhone Safari reports with its
  keyboard AND its QuickType/autofill accessory bar up — measured range
  ~380–420px — not the flat "height − 388" the first pass of this tool
  guessed.

  Android-shaped devices (412×915, 360×800) get NO stub at all: the class
  page's viewport meta is `interactive-widget=resizes-content`, which makes
  Android Chrome (108+) shrink the LAYOUT viewport itself on focus, so
  `innerHeight` genuinely changes and `visualViewport.height` tracks it for
  free. This is reproduced with a SECOND real
  `Emulation.setDeviceMetricsOverride` call, to the shrunk height, issued
  AFTER the box is focused at the full height — a true resize, not a
  simulation, because Chrome can do this one natively.

OFFSETTOP (iOS devices only — Android's real resize has no separate
offsetTop signal). `window.__KB__(height, offsetTop)` also stubs a non-zero
`visualViewport.offsetTop`, simulating a page that has scrolled a little
while the keyboard is up; swept at 0 and 40, assertions only at 40 (no
screenshots — see `main()`). The "keyboard top" in every assertion is
`offsetTop + height`, never just `height`.

BEFORE / AFTER. `shared/flashcard-keyboard.js` is swapped on disk, in place,
between `origin/main`'s copy (BEFORE) and the worktree's fixed copy (AFTER)
— then restored in a `finally`, so a crash mid-run cannot leave the repo on
the wrong version.

Exit code 0 only if every assertion below passed in every AFTER case.
"""
import argparse
import base64
import json
import os
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
import ks3_browser as cdp  # noqa: E402

KEYBOARD_JS_PATH = os.path.join(ROOT, "shared", "flashcard-keyboard.js")
AID = "aaaaaaaa-0000-4000-8000-00000000f1a1"

SHORT_Q = "What is the unit of force?"
SHORT_A = "The newton (N)"

# Real production cards (given verbatim by the commander).
PROD1_Q = "Explain the effect adding a catalyst has on the rate of a reaction."
PROD1_A = ("Increases the rate of reaction by providing an alternative reaction "
           "pathway with a lower activation energy")
PROD2_Q = "Describe the test for alkenes, including the positive result."
PROD2_A = "Add bromine water, bromine water turns from orange to colourless (decolourises)"

LONG_Q = ("Explain, in as much detail as you can, how fossil fuels such as coal, "
          "oil and natural gas formed from the remains of ancient plants and "
          "animals that lived millions of years ago, and explain why this is "
          "described as a non-renewable process.")
LONG_A = ("Plankton died, were buried under layers of mud and sediment on the sea "
          "floor, and were compressed and heated over millions of years without "
          "oxygen, which slowly turned the remains into crude oil and natural "
          "gas. Coal formed the same way from dead trees and plants on land, "
          "compacted under layers of rock. It cannot be repeated on a useful "
          "timescale because the process takes millions of years.")

# A chemical formula in the model answer — the deck is already forced to
# "chemistry" below (`__MRB_FC_SUBJECT__`), so this exercises the SAME
# formula renderer (`shared/formulae.js`'s `fx` nodes) the real Chemistry
# homework deck uses: CO2 must render as CO with a real <sub>2</sub>, not the
# flat text an authored string stores.
CHEM_Q = "What happens when carbon dioxide is bubbled through limewater?"
CHEM_A = "CO2 turns limewater cloudy"

CONTENT = {
    "short": (SHORT_Q, SHORT_A),
    "prod1": (PROD1_Q, PROD1_A),
    "prod2": (PROD2_Q, PROD2_A),
    "long": (LONG_Q, LONG_A),
    "chem": (CHEM_Q, CHEM_A),
}
# A stable small int per content key, used only to make each card's id
# distinct (FAKE_TMPL interpolates it into a UUID's last hex digit).
CONTENT_N = {"short": "1", "prod1": "2", "prod2": "3", "long": "4", "chem": "5"}

# (name, width, height, kind, shrunk_vv) — shrunk_vv is the keyboard-up
# visual-viewport height at offsetTop 0: for "ios" it is what __KB__ is told
# to report; for "android" it is the SECOND setDeviceMetricsOverride height.
DEVICES = [
    ("ios-390x844", 390, 844, "ios", 400),
    ("ios-360x740", 360, 740, "ios", 340),
    ("android-412x915", 412, 915, "android", 560),
    ("android-360x800", 360, 800, "android", 470),
]

FAKE_TMPL = r"""
(function () {
  var cards = [
    {id: "c0000000-0000-4000-8000-00000000000%(n)s", position: 0, question: %(q)s, answer: %(a)s}
  ].map(function (c) { return Object.assign({made: false, known: false, secured: false, last: null, mine: null, gm: false, gr: false}, c); });
  var S = window.__FC_FAKE__ = {events: [], calls: 0, complete: false, mode: "make", sittings: 0, open: false,
                                rows: [], seen: {}};
  S.reviews = function () {
    if (!S.events.length) { S.rows.length = 0; S.seen = {}; }
    return JSON.parse(JSON.stringify(S.rows));
  };
  function state() {
    var made = 0, known = 0, secured = 0;
    cards.forEach(function (c) { if (c.made) made++; if (c.known) known++; if (c.secured) secured++; });
    return JSON.parse(JSON.stringify({assignment_id: "__AID__", title: "Fossil fuels flashcards", mode: S.mode,
      rule: "secure", n: cards.length, made: made, known: known, secured: secured, complete: S.complete,
      sittings: S.sittings, session_id: null, note: null, cards: cards}));
  }
  S.transport = function (id, events) {
    S.calls++;
    (events || []).forEach(function (e) {
      if (e.id && S.seen[e.id]) { return; }
      if (e.id) { S.seen[e.id] = true; }
      S.events.push(e);
      if (!S.open && e.type !== "visibility") { S.open = true; S.sittings++; }
      if (e.type === "session_finish") { S.open = false; }
      var c = cards.filter(function (k) { return k.id === e.card; })[0];
      if (!c) return;
      if (e.type === "answer_submitted" && e.phase === "make") { c.made = true; if (c.mine == null) c.mine = e.answer; }
      if (e.type === "rated") {
        c.last = e.rating;
        if (e.rating === "got_it") { c.known = true; c.gm = true; }
      }
    });
    return new Promise(function (r) { setTimeout(function () { r(state()); }, 5); });
  };
})();
""".replace("__AID__", AID)

# `__KB__(height, offsetTop)` — both halves of the real iOS signal, stubbed.
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
  window.__KB__ = function (height, offsetTop) {
    h = height; top = offsetTop || 0;
    (ls.resize || []).forEach(function (f) { try { f({type: "resize"}); } catch (e) {} });
  };
})();
"""

# A leaf is an element with no element children but real text — the unit a
# line boundary can be measured against.
LEAF_HELPERS_JS = r"""
(function () {
  function leaves(el) {
    var out = [];
    (function walk(n) {
      if (!n || n.nodeType !== 1) { return; }
      var kids = [];
      for (var i = 0; i < n.childNodes.length; i++) {
        if (n.childNodes[i].nodeType === 1) { kids.push(n.childNodes[i]); }
      }
      if (!kids.length) {
        if (n.textContent && n.textContent.trim()) { out.push(n); }
        return;
      }
      kids.forEach(walk);
    })(el);
    return out;
  }
  // Is any leaf's text straddling EITHER of the face's own visible edges —
  // a half-cut line? (⊕ Y Unit 1: checks the TOP edge too, via scrollTop —
  // the learn step can legitimately start scrolled down.)
  function anyClipped(face) {
    if (!face) { return false; }
    var fr = face.getBoundingClientRect();
    var top = fr.top, bottom = fr.bottom;
    var ls = leaves(face);
    for (var i = 0; i < ls.length; i++) {
      var rg = document.createRange();
      rg.selectNodeContents(ls[i]);
      var rects = rg.getClientRects();
      for (var k = 0; k < rects.length; k++) {
        var r = rects[k];
        if (r.top < bottom - 0.5 && r.bottom > bottom + 0.5) { return true; }
        if (face.scrollTop > 1 && r.top < top - 0.5 && r.bottom > top + 0.5) { return true; }
      }
    }
    return false;
  }
  window.__MRB_LEAVES__ = leaves;
  window.__MRB_ANY_CLIPPED__ = anyClipped;
})();
"""

LOAD = r"""
(async function () {
  function add(src) { return new Promise(function (ok, bad) {
    var s = document.createElement('script'); s.src = src + '?t=' + Date.now();
    s.onload = ok; s.onerror = bad; document.head.appendChild(s); }); }
  try { localStorage.clear(); } catch (e) {}
  await add('/shared/formulae.js');
  await add('/shared/flashcard-homework.js');
  await add('/shared/flashcard-keyboard.js');
  window.MRBHomework.transport = window.__FC_FAKE__.transport;
  window.MRBHomework.resumeRead = function () { return Promise.resolve(window.__FC_FAKE__.reviews()); };
  window.MRBHomework.modelCheck = function () { return new Promise(function () {}); };
  return !!window.__MRB_OPEN_HW__;
})()
"""

# Reads the box's rest-state (unfocused) border + its own fill, before the
# case's own flow ever focuses it.
UNFOCUSED_BOX_JS = r"""
(function () {
  var box = document.querySelector('[data-hw="answer"]');
  if (!box) { return null; }
  var cs = getComputedStyle(box);
  return {borderColor: cs.borderTopColor, bg: cs.backgroundColor, boxShadow: cs.boxShadow};
})()
"""

MEASURE_JS = r"""
(function () {
  function rect(sel) { var e = document.querySelector(sel); if (!e) return null;
    var r = e.getBoundingClientRect(); return {top: r.top, bottom: r.bottom, left: r.left, right: r.right, h: r.height, w: r.width}; }
  var vv = window.visualViewport;
  var cardFit = document.querySelector('[data-card-fit]');
  var front = document.querySelector('[data-dc-tpl="10334"]');
  var cs = front ? getComputedStyle(front) : null;
  var box = document.querySelector('[data-hw="answer"]');
  var boxCs = box ? getComputedStyle(box) : null;
  var act = document.querySelector('[data-hw="act"]');
  var check = document.querySelector('[data-hw="check"]');
  var dlg = document.querySelector('[data-mrb-dialog="flashcards"]');
  var learnEl = document.querySelector('[data-hw="learn"]');
  var frontRect = front ? front.getBoundingClientRect() : null;
  var learnRect = learnEl ? learnEl.getBoundingClientRect() : null;
  // ⊕ Y review — the model answer's own TEXT (the block's last child): it is
  // what must be visible; the rule and "ANSWER" label above it may give way.
  var ansEl = learnEl ? learnEl.lastElementChild : null;
  var ansRect = ansEl ? ansEl.getBoundingClientRect() : null;
  var cueCs = cardFit ? getComputedStyle(cardFit, '::after') : null;
  var cueTopCs = cardFit ? getComputedStyle(cardFit, '::before') : null;
  var sub = learnEl ? learnEl.querySelector('sub') : null;
  // ⊕ Y review — the question's own ink against the card it sits on.
  var qEl = front ? front.querySelector('[data-dc-tpl="10340"]') : null;
  var qInk = qEl ? getComputedStyle(qEl).color : null;
  var qOn = front ? getComputedStyle(front).backgroundColor : null;
  return {
    vvTop: vv.offsetTop, vvHeight: vv.height, vvBottom: vv.offsetTop + vv.height,
    innerHeight: window.innerHeight,
    typing: dlg ? dlg.getAttribute('data-hw-typing') : null,
    learn: dlg ? dlg.getAttribute('data-hw-learn') : null,
    card: rect('[data-card-fit]'),
    front: front ? {scrollHeight: front.scrollHeight, clientHeight: front.clientHeight,
                    scrollTop: front.scrollTop, overflowY: cs.overflowY, text: front.innerText,
                    padT: parseFloat(cs.paddingTop) || 0, padB: parseFloat(cs.paddingBottom) || 0,
                    textBelow: (function(){var fr=front.getBoundingClientRect(),mx=-1e9,mn=1e9;
                      var w=document.createTreeWalker(front,NodeFilter.SHOW_TEXT);var n;
                      while((n=w.nextNode())){if(!n.textContent.trim())continue;var el=n.parentElement;
                        if(el&&getComputedStyle(el).display==='none')continue;var r=document.createRange();r.selectNodeContents(n);
                        var rs=r.getClientRects();for(var i=0;i<rs.length;i++){if(!rs[i].height)continue;mx=Math.max(mx,rs[i].bottom);mn=Math.min(mn,rs[i].top);}}
                      return {below: mx-fr.bottom, above: fr.top-mn};})()} : null,
    clipped: (front && window.__MRB_ANY_CLIPPED__) ? window.__MRB_ANY_CLIPPED__(front) : null,
    overflowAttr: cardFit ? cardFit.getAttribute('data-hw-overflow') : null,
    overflowTopAttr: cardFit ? cardFit.getAttribute('data-hw-overflow-top') : null,
    cueBg: cueCs ? cueCs.backgroundImage : null,
    cueTopBg: cueTopCs ? cueTopCs.backgroundImage : null,
    box: rect('[data-hw="answer"]'),
    boxFocused: document.activeElement === box,
    boxStyle: boxCs ? {borderColor: boxCs.borderTopColor, bg: boxCs.backgroundColor, boxShadow: boxCs.boxShadow} : null,
    act: rect('[data-hw="act"]'),
    check: rect('[data-hw="check"]'),
    docWidth: document.documentElement.scrollWidth,
    innerWidth: window.innerWidth,
    hwBoxVar: dlg ? getComputedStyle(dlg).getPropertyValue('--hw-box-h') : null,
    learnPresent: !!learnEl,
    learnVisibleAtRest: (ansRect && frontRect)
      ? (ansRect.top >= frontRect.top - 0.5 && ansRect.bottom <= frontRect.bottom + 0.5)
      : null,
    learnTopGap: (ansRect && frontRect) ? (ansRect.top - frontRect.top) : null,
    qInk: qInk, qOn: qOn,
    subText: sub ? sub.textContent : null,
    learnText: learnEl ? learnEl.textContent : null
  };
})()
"""

# Scroll the card's scrollable face all the way down and ask: is the model
# answer's FOOT now inside the visible box?
SCROLL_REACH_JS = r"""
(function () {
  var front = document.querySelector('[data-dc-tpl="10334"]');
  var learnEl = document.querySelector('[data-hw="learn"]');
  if (!front || !learnEl) { return {scrolled: false, reach: null}; }
  front.scrollTop = front.scrollHeight;
  var fr = front.getBoundingClientRect(), lr = learnEl.getBoundingClientRect();
  return {scrolled: true, reach: (lr.bottom <= fr.bottom + 0.5 && lr.bottom >= fr.top - 0.5),
          frontBottom: fr.bottom, learnBottom: lr.bottom, scrollTop: front.scrollTop};
})()
"""

FAILS = []


def check(ok, what):
    print(("    PASS " if ok else "    FAIL ") + what)
    if not ok:
        FAILS.append(what)


def settle(t=0.3):
    time.sleep(t)


def _parse_rgb(s):
    if not s:
        return None
    s = s.strip()
    if s.startswith("rgba"):
        parts = s[s.index("(") + 1:s.rindex(")")].split(",")
        r, g, b, a = [float(x) for x in parts]
        if a <= 0.01:
            return None  # fully transparent: not a real paint
        return (r, g, b)
    if s.startswith("rgb"):
        parts = s[s.index("(") + 1:s.rindex(")")].split(",")
        r, g, b = [float(x) for x in parts[:3]]
        return (r, g, b)
    return None


def _lin(c):
    c = c / 255.0
    return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4


def _lum(rgb):
    r, g, b = rgb
    return 0.2126 * _lin(r) + 0.7152 * _lin(g) + 0.0722 * _lin(b)


def contrast_ratio(rgb1, rgb2):
    if not rgb1 or not rgb2:
        return None
    l1, l2 = _lum(rgb1), _lum(rgb2)
    l1, l2 = max(l1, l2), min(l1, l2)
    return (l1 + 0.05) / (l2 + 0.05)


def run_case(port, device, content_key, step, offset_top, theme, shots_dir, label):
    """One fresh browser: open the overlay, measure the box unfocused, bring
    the fake/real keyboard up (focusing the box inside the SAME call that
    triggers it — proving the focus fix independently of the keyboard sizing
    fix), optionally go to the 'I don't know' learn step, measure, screenshot."""
    name, width, height, kind, shrunk_vv = device
    q, a = CONTENT[content_key]
    fake = FAKE_TMPL % {"n": CONTENT_N[content_key], "q": json.dumps(q), "a": json.dumps(a)}
    with cdp.Browser() as br:
        page = br.attach()
        page.send("Emulation.setDeviceMetricsOverride",
                  {"width": width, "height": height, "deviceScaleFactor": 3, "mobile": True})
        page.send("Emulation.setTouchEmulationEnabled", {"enabled": True, "maxTouchPoints": 5})
        # Headless Chrome does not consider an automated page "focused" at
        # the OS/window level by default, so `:focus` never matches even
        # after a real `element.focus()` call (confirmed: `activeElement`
        # was the box, `matches(':focus')` was false) — `flashcard_homework_
        # drive.py` already carries this same call for the same reason.
        try:
            page.send("Emulation.setFocusEmulationEnabled", {"enabled": True})
        except cdp.CDPError:
            pass
        page.send("Page.addScriptToEvaluateOnNewDocument", {"source": fake})
        if kind == "ios":
            page.send("Page.addScriptToEvaluateOnNewDocument", {"source": FAKE_VV})
        page.send("Page.addScriptToEvaluateOnNewDocument", {"source": LEAF_HELPERS_JS})
        page.goto("http://127.0.0.1:%d/student/class-fixture.html" % port)
        settle(0.8)
        page.eval("document.documentElement.setAttribute('data-theme', %s)" % json.dumps(theme))
        ok = page.eval(LOAD)
        if ok is not True:
            check(False, "%s: fixture mounted (__MRB_OPEN_HW__ present)" % label)
            return None
        page.eval("window.__MRB_FC_SUBJECT__ = %s" % json.dumps({AID: "chemistry"}))
        page.eval("window.__MRB_OPEN_HW__(%s)" % json.dumps(AID))
        settle(0.6)

        # The TRUE rest-state baseline, captured before anything — including
        # "I don't know" itself, which (⊕ Y Unit 1's own fix) focuses the box
        # SYNCHRONOUSLY inside that same tap. Capturing this after the idk
        # click would compare "focused" against "focused" and could never
        # show a difference — that was this tool's own bug, not a product
        # one (confirmed via a standalone CDP probe: the fix genuinely moves
        # border-color and box-shadow once a real focus lands).
        unfocused = page.eval(UNFOCUSED_BOX_JS)

        idk_sync = idk_after = None
        if step == "learn":
            # ⊕ Y review — read focus INSIDE the same call as the tap (what
            # iOS needs to raise the keyboard) and again after the redraw,
            # BEFORE this tool focuses anything itself.
            idk_sync = page.eval("(function(){var b=document.querySelector('[data-hw=\"idk\"]'); if(b) b.click();"
                                 "var a=document.activeElement;return a&&a.getAttribute?a.getAttribute('data-hw'):null;})()")
            settle(0.3)
            idk_after = page.eval("(function(){var a=document.activeElement;return a&&a.getAttribute?a.getAttribute('data-hw'):null;})()")

        # ⊕ Y Unit 1 — the box is focused INSIDE the same tap as "I don't
        # know" in the real component (student_rulings.py's hwIdk) — this
        # second focus() call is a no-op there (already the activeElement)
        # and is what gives the box a real focus at all on the "card" step,
        # which never taps anything.
        page.eval("(function(){var t=document.querySelector('[data-hw=\"answer\"]'); if(t) t.focus({preventScroll:true});})()")
        settle(0.2)

        if kind == "ios":
            vv_height = shrunk_vv - offset_top
            page.eval("window.__KB__(%d, %d)" % (vv_height, offset_top))
        else:
            # Android: a REAL second resize, after the box is already
            # focused at the full height — exactly the order a real phone's
            # `interactive-widget=resizes-content` layout-viewport shrink
            # happens in.
            page.send("Emulation.setDeviceMetricsOverride",
                      {"width": width, "height": shrunk_vv, "deviceScaleFactor": 3, "mobile": True})
            page.eval("window.dispatchEvent(new Event('resize'))")
        settle(0.5)

        m = page.eval(MEASURE_JS)

        if shots_dir:
            os.makedirs(shots_dir, exist_ok=True)
            vv_h = m["vvHeight"] if m else (shrunk_vv - offset_top)
            vv_t = m["vvTop"] if m else offset_top
            res = page.send("Page.captureScreenshot", {
                "format": "png", "fromSurface": True,
                "clip": {"x": 0, "y": vv_t, "width": width, "height": vv_h, "scale": 1}
            })
            path = os.path.join(shots_dir, "%s.png" % label)
            with open(path, "wb") as fh:
                fh.write(base64.b64decode(res["data"]))

        # ⊕ Y review — a pupil who scrolls the learn card UP to re-read the
        # question keeps that position while the keyboard keeps firing
        # visualViewport events (iOS does, constantly, while they type) and
        # across the redraw their first keystroke causes.
        if step == "learn" and kind == "ios":
            F = "document.querySelector('[data-mrb-dialog=\\\"flashcards\\\"] [data-dc-tpl=\\\"10334\\\"]')"
            st0 = page.eval("(function(){var f=%s;return f?f.scrollTop:-1;})()" % F)
            if st0 and st0 > 0:
                page.eval("(function(){var f=%s;f.scrollTop=0;})()" % F)
                settle(0.2)
                page.eval("window.__KB__(%d, %d)" % (shrunk_vv - offset_top, offset_top))
                settle(0.3)
                page.eval("(function(){var t=document.querySelector('[data-hw=\\\"answer\\\"]');"
                          "t.value='a';t.dispatchEvent(new Event('input',{bubbles:true}));})()")
                settle(0.4)
                page.eval("window.__KB__(%d, %d)" % (shrunk_vv - offset_top, offset_top))
                settle(0.3)
                st1 = page.eval("(function(){var f=%s;return f?f.scrollTop:-1;})()" % F)
                check(st1 is not None and st1 <= 1,
                      "%s: the pupil's own scroll up survives keyboard events and a keystroke redraw (was %.1f, now %r)"
                      % (label, st0, st1))

        # Last: it scrolls the card itself (Y review — it used to run BEFORE
        # the screenshot, so every picture showed a card the tool had scrolled).
        reach = page.eval(SCROLL_REACH_JS) if step == "learn" else None

    if m is None:
        check(False, "%s: measured" % label)
        return None

    # ── assertions ──────────────────────────────────────────────────────
    vv_bottom = m["vvBottom"]
    check_bottom = m["check"]["bottom"] if m["check"] else None
    box = m["box"]
    act = m["act"]
    front = m["front"]

    if step == "learn":
        check(idk_sync == "answer", "%s: the cursor is in the box INSIDE the 'I don't know' tap (activeElement=%r)" % (label, idk_sync))
        check(idk_after == "answer", "%s: the cursor is still in the box after the redraw (activeElement=%r)" % (label, idk_after))
    ok0 = bool(m["boxFocused"])
    check(ok0, "%s: the box is document.activeElement with the keyboard up" % label)

    ok1 = check_bottom is not None and (vv_bottom - check_bottom) <= 8 and check_bottom <= vv_bottom + 0.5
    check(ok1, "%s: Check's bottom within 8px above the keyboard top (check=%.1f keyboard_top=%.1f gap=%.1f)"
          % (label, check_bottom or -1, vv_bottom, (vv_bottom - check_bottom) if check_bottom else -1))

    gap = (act["top"] - box["bottom"]) if (act and box) else None
    ok2 = gap is not None and gap <= 12
    check(ok2, "%s: answer box fills down to Check (gap=%.1fpx)" % (label, gap if gap is not None else -1))

    floor = 72 if step == "learn" else 90
    ok2b = bool(box) and box["h"] >= floor
    check(ok2b, "%s: answer box is at least %dpx (box_h=%.1f)" % (label, floor, box["h"] if box else -1))

    overflowing = front and front["scrollHeight"] > front["clientHeight"] + 1
    cue_on = m["overflowAttr"] == "1" and bool(m["cueBg"]) and "gradient" in (m["cueBg"] or "")
    cue_top_on = m["overflowTopAttr"] == "1" and bool(m["cueTopBg"]) and "gradient" in (m["cueTopBg"] or "")

    ok_clip = not m["clipped"]
    check(ok_clip, "%s: no line clipped at either of the card's visible edges (clipped=%s)" % (label, m["clipped"]))

    # TEXT hidden, not just the face's own padding (Y review: a fade over
    # the answer's last line with nothing under it is a false "more").
    hidden_below = overflowing and (front["scrollTop"] + front["clientHeight"] < front["scrollHeight"] - front["padB"] - 1)
    hidden_above = overflowing and front["scrollTop"] > front["padT"] + 1
    if hidden_below:
        ok3 = front["overflowY"] == "auto" and cue_on
        check(ok3, "%s: hidden content below shows the bottom cue (overflowY=%s cue=%s)" % (label, front["overflowY"], cue_on))
    else:
        check(not cue_on, "%s: no stray bottom cue (overflowAttr=%s)" % (label, m["overflowAttr"]))
    if hidden_above:
        ok3b = cue_top_on
        check(ok3b, "%s: hidden content above shows the top cue (cue_top=%s scrollTop=%.1f)" % (label, cue_top_on, front["scrollTop"]))
    else:
        check(not cue_top_on, "%s: no stray top cue (overflowTopAttr=%s)" % (label, m["overflowTopAttr"]))

    ok4 = m["docWidth"] <= m["innerWidth"] + 1
    check(ok4, "%s: no horizontal overflow (docWidth=%s innerWidth=%s)" % (label, m["docWidth"], m["innerWidth"]))

    # ── box contrast + focus treatment ──────────────────────────────────
    if m["boxStyle"]:
        border_rgb = _parse_rgb(m["boxStyle"]["borderColor"])
        bg_rgb = _parse_rgb(m["boxStyle"]["bg"])
        ratio = contrast_ratio(border_rgb, bg_rgb)
        ok5 = ratio is not None and ratio >= 3.0
        check(ok5, "%s: box border contrast >= 3:1 against its own surface (%.2f, theme=%s)"
              % (label, ratio if ratio is not None else -1, theme))
        if unfocused:
            differs = (m["boxStyle"]["borderColor"] != unfocused["borderColor"] or
                       m["boxStyle"]["boxShadow"] != unfocused["boxShadow"])
            check(differs, "%s: focused box has a visible focus treatment (border/shadow differs from unfocused)" % label)

    if step == "learn":
        ok6 = m["learnPresent"]
        check(ok6, "%s: the model answer's block is in the DOM" % label)
        if content_key in ("short", "prod1", "prod2"):
            # ⊕ Y Unit 1 review — 360×740 (vv ~340) is the single tightest
            # cell in the whole matrix: narrower AND shorter than every
            # other device tested, including the real `360×740 → ~340`
            # figure the brief itself gives as the realistic iPhone SE-class
            # floor. Measured: `prod1`'s own content (its two-line question,
            # stepped down, plus its own four-line answer) genuinely cannot
            # fit even with the box shrunk to its 72px floor — box lands at
            # 82px, both cues fire, nothing is clipped, Check still sits
            # correctly. That is the priority order doing exactly what it
            # says ("answer fully visible > box ≥ 96 > ... if the answer
            # can't be fully visible with a 96px box, the box may shrink to
            # a floor of ~72px BEFORE THE ANSWER IS CUT") working as
            # intended on genuinely too little room, not a defect — the same
            # tolerance already given to `long` applies here on this one
            # device, instead of a blanket "always fits" that the room does
            # not support.
            # ⊕ Y review — no 360px exemption: the answer text must be fully
            # visible at rest on every device (the old `tight` carve-out let
            # the 360px phone show the label and lose the answer's last line).
            tight = False
            if offset_top == 0 and not tight:
                ok7 = bool(m["learnVisibleAtRest"])
                check(ok7, "%s: the model answer is fully visible without scrolling (content=%s)" % (label, content_key))
            elif tight:
                gap = m["learnTopGap"]
                ok7 = bool(m["learnVisibleAtRest"]) or (gap is not None and abs(gap) < 4)
                check(ok7, "%s: the model answer is fully visible, or (too tight even at the box floor) its first "
                      "line is at the card's visible top (visible=%s learnTopGap=%s)"
                      % (label, m["learnVisibleAtRest"], gap))
            else:
                print("    INFO  %s: model answer visible-at-rest=%s (not required at offsetTop=%d)"
                      % (label, m["learnVisibleAtRest"], offset_top))
        elif content_key == "long":
            # Too long to be fully visible: the learn block's own TOP (the
            # rule + "ANSWER" label right above its first text line) must
            # be at the card's visible top — not scrollTop==0 (there is a
            # whole question above it in the content; scrolling to the
            # learn block's own top offset is what shows its first line).
            gap = m["learnTopGap"]
            ok7 = gap is not None and -0.5 <= gap < 6
            check(ok7, "%s: the very long answer's first line is at the card's visible top (learnTopGap=%.1f)"
                  % (label, gap if gap is not None else -999))
        # ⊕ Y review — the question stays readable on the learn step: it
        # was drawn in the PAGE's muted ink on the dark card (1.8:1).
        if m.get("qInk") and m.get("qOn"):
            qcr = contrast_ratio(_parse_rgb(m["qInk"]), _parse_rgb(m["qOn"]))
            check(qcr >= 4.5, "%s: the question reads on its card (%.2f:1, theme=%s)" % (label, qcr, theme))
        if content_key == "chem":
            ok8 = bool(m["subText"]) and m["subText"] == "2"
            check(ok8, "%s: CO2 renders with a real <sub>2</sub> (subText=%r)" % (label, m["subText"]))
            lt = (m["learnText"] or "").replace("\n", " ")
            ok9 = "CO" in lt and "turns limewater cloudy" in lt
            check(ok9, "%s: the formula-rendered answer keeps its other words (learnText=%r)" % (label, lt))
        if reach is not None:
            ok10 = bool(reach.get("reach"))
            check(ok10, "%s: the model answer is reachable by scrolling the card (frontBottom=%.1f learnBottom=%.1f)"
                  % (label, reach.get("frontBottom", -1), reach.get("learnBottom", -1)))

    print("    %s: card_h=%.1f box_h=%.1f gap=%.1f check_bottom=%.1f keyboard_top=%.1f "
          "typing=%s learn=%s overflowing=%s clipped=%s cue=%s/%s focused=%s"
          % (label, m["card"]["h"] if m["card"] else -1, box["h"] if box else -1,
             gap if gap is not None else -1, check_bottom or -1, vv_bottom, m["typing"], m["learn"],
             overflowing, m["clipped"], cue_on, cue_top_on, m["boxFocused"]))
    return m


def swap_in(src_text):
    with open(KEYBOARD_JS_PATH, "r") as fh:
        current = fh.read()
    with open(KEYBOARD_JS_PATH, "w") as fh:
        fh.write(src_text)
    return current


def git_show(ref, path):
    rel = os.path.relpath(path, ROOT)
    out = subprocess.run(["git", "show", "%s:%s" % (ref, rel)], cwd=ROOT,
                          capture_output=True, text=True, check=True)
    return out.stdout


def build_matrix():
    """Returns a list of (content_key, step, offset_top, theme, want_shots)
    cases run against EVERY device, plus a separate list of (device_name,
    content_key, step, offset_top, theme, want_shots) cases run against ONE
    named device only (the iOS offsetTop=40 sweep, and the one dark-theme
    pair)."""
    per_device = [
        ("short", "learn", 0, "light", False),
        ("prod1", "learn", 0, "light", True),   # the screenshot case
        ("long", "learn", 0, "light", False),
        ("short", "card", 0, "light", False),
        ("long", "card", 0, "light", False),
    ]
    one_off = [
        # chemistry formula — one representative device is enough; the
        # renderer itself is device-independent.
        ("ios-390x844", "chem", "learn", 0, "light", False),
        # one dark-theme pair per device family, per the brief's "light AND
        # dark theme" (contrast is asserted on EVERY case already; this adds
        # the dark SCREENSHOT + a second device family for belt-and-braces).
        ("ios-390x844", "prod1", "learn", 0, "dark", True),
        ("android-412x915", "prod1", "learn", 0, "dark", False),
        # the offsetTop=40 stress sweep — iOS only (Android's real resize has
        # no separate offsetTop signal) — assertions only.
        ("ios-390x844", "short", "learn", 40, "light", False),
        ("ios-390x844", "long", "learn", 40, "light", False),
        ("ios-360x740", "short", "learn", 40, "light", False),
        ("ios-360x740", "long", "learn", 40, "light", False),
    ]
    return per_device, one_off


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--shots", default=None, help="base dir; before/ and after/ subfolders are made under it")
    ap.add_argument("--pass-name", choices=["before", "after", "both"], default="both")
    ap.add_argument("--device", default=None, help="run only this device (e.g. ios-390x844)")
    ap.add_argument("--only", default=None, help="run only cases whose label contains this text")
    args = ap.parse_args()

    with open(KEYBOARD_JS_PATH, "r") as fh:
        fixed_text = fh.read()  # the worktree's current (AFTER) version
    before_text = git_show("origin/main", KEYBOARD_JS_PATH)

    per_device, one_off = build_matrix()

    def all_cases():
        for device in DEVICES:
            for (content_key, step, offset_top, theme, want_shots) in per_device:
                yield (device, content_key, step, offset_top, theme, want_shots)
        by_name = dict((d[0], d) for d in DEVICES)
        for (dev_name, content_key, step, offset_top, theme, want_shots) in one_off:
            yield (by_name[dev_name], content_key, step, offset_top, theme, want_shots)

    sweeps = [("before", "before"), ("after", "after")]
    if args.pass_name == "before":
        sweeps = [s for s in sweeps if s[1] == "before"]
    elif args.pass_name == "after":
        sweeps = [s for s in sweeps if s[1] == "after"]

    results = {}
    sweep_stats = {}
    restore_to = fixed_text
    try:
        for (sweep, variant) in sweeps:
            print("\n══ %s (%s) ══" % (sweep.upper(),
                  "origin/main, unfixed" if variant == "before" else "this worktree, Y Unit 1"))
            swap_in(before_text if variant == "before" else fixed_text)
            server, port = cdp.serve(ROOT)
            try:
                for (device, content_key, step, offset_top, theme, want_shots) in all_cases():
                    # BEFORE only needs the screenshot-proof cases — the full
                    # assertion sweep on BEFORE is not interesting (it is
                    # EXPECTED to fail; the point is the AFTER sweep is
                    # clean), and running it in full would double the
                    # machine time on a box already in swap.
                    if variant == "before" and not want_shots:
                        continue
                    label = "%s-%s-%s-%s-off%d-%s" % (sweep, device[0], content_key, step, offset_top, theme)
                    if args.device and device[0] != args.device:
                        continue
                    if args.only and args.only not in label:
                        continue
                    shots_dir = os.path.join(args.shots, variant) if (args.shots and want_shots) else None
                    n0 = len(FAILS)
                    try:
                        m = run_case(port, device, content_key, step, offset_top, theme, shots_dir, label)
                    except (cdp.CDPError, TimeoutError, OSError) as exc:
                        print("    RETRY %s after transient error: %r" % (label, exc))
                        time.sleep(1.0)
                        del FAILS[n0:]
                        m = run_case(port, device, content_key, step, offset_top, theme, shots_dir, label)
                    case_fails = FAILS[n0:]
                    results[label] = (m, case_fails, variant)
                    s = sweep_stats.setdefault(sweep, [0, 0])
                    s[0] += 1
                    s[1] += len(case_fails)
                    if variant == "before":
                        del FAILS[n0:]  # BEFORE's failures are expected; don't gate on them
            finally:
                server.shutdown()
    finally:
        swap_in(restore_to)
        with open(KEYBOARD_JS_PATH, "r") as fh:
            final = fh.read()
        if final != fixed_text:
            print("!!!! shared/flashcard-keyboard.js did not restore cleanly !!!!")
            sys.exit(2)

    print("\n── summary ──")
    for (sweep, variant) in sweeps:
        n, bad = sweep_stats.get(sweep, [0, 0])
        print("  %s: %d cases, %d failed assertions" % (sweep, n, bad))

    after_fails = [k for k, (m, fails, v) in results.items() if v == "after" and fails]
    if after_fails:
        print("\nAFTER regressions (must be empty): %s" % after_fails)
        for k in after_fails:
            print("  %s: %s" % (k, results[k][1]))
        sys.exit(1)
    print("\nOK")
    sys.exit(0)


if __name__ == "__main__":
    main()
