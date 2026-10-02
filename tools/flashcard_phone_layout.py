#!/usr/bin/env python3
"""MRB-354 unit B — phone-keyboard layout of the flashcard homework typing
screen: Mide's 2 Oct 2026 iPhone report ("the question card is cut off
mid-sentence… the answer box shows two lines… a big empty gap between Check
and the keyboard… iOS showed the autofill/accessory bar above the keyboard"),
and the commander's follow-up review of the first pass: the gap was fixed,
but the card itself was still clipped mid-line with no scroll cue, and in
the "I don't know" learn step the model answer was not visible at all.

    python3 tools/flashcard_phone_layout.py

Drives the COMPILED fixture (`student/class-fixture.html`, the real
`shared/flashcard-homework.js` + `shared/flashcard-keyboard.js`), the same way
`flashcard_homework_drive.py` does — same `cdp` transport, same fake
`flashcard_record()` transport shape, same `window.visualViewport` stub
pattern (that file's own `FAKE_VV`/`window.__KB__`), because that is the
"faithful method" the task asked for: Chrome cannot itself shrink
`visualViewport` while leaving `innerHeight` alone (that is a real-OS-only
split — see the header comment of `flashcard-keyboard.js`), so a drive that
wants to exercise the same code path a real phone's keyboard does has to
replace `window.visualViewport` with a stub object and fire a `resize` at
it, exactly as the existing homework drive already does for its own
keyboard-up assertions. Nothing about `flashcard-keyboard.js`'s own logic
can tell a stub `resize` from iOS's real one — it reads
`visualViewport.height`/`.offsetTop` and listens for the same event either
way — so this exercises the identical branch a phone would.

THE ACCESSORY BAR. iOS's keyboard carries an "accessory"/QuickType/AutoFill
strip above its keys (the key/card/location icons in Mide's screenshot) that
is part of the keyboard's own occlusion of the page — real iOS already
folds it into `visualViewport.height` (there is no separate signal for it).
So "a 336px keyboard plus a 52px accessory bar" is simulated as ONE combined
388px cut to `visualViewport.height`, matching what a real phone reports.

OFFSETTOP. `window.__KB__(height, offsetTop)` also stubs a non-zero
`visualViewport.offsetTop`, simulating a page that has scrolled a little
while the keyboard is up (the AFTER pass runs the whole matrix a second
time at offsetTop=40, assertions only, no screenshots — see `main()`).
The "keyboard top" in every assertion is `offsetTop + height`, never just
`height`, so this is exercised rather than assumed.

BEFORE / AFTER. `shared/flashcard-keyboard.js` is swapped on disk, in place,
between `origin/main`'s copy (BEFORE: the box fixed at 64px under a
keyboard and the card capped by a flat percentage of the viewport,
STAGE-D-PLAN.md decision 1/3) and the worktree's fixed copy (AFTER:
`fitCard()`+`fitBox()` split the budget, card gets priority, snap-to-line +
fade cue, MRB-354 unit B) — then restored in a `finally`, so a crash
mid-run cannot leave the repo on the wrong version. Nothing else changes
between the two passes: same fixture, same fake transport, same device
metrics.

Exit code 0 only if every assertion below passed in every AFTER case (both
offsetTop sweeps). The BEFORE pass is expected to fail several — that is the
proof the bugs were real.
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
KEYBOARD_PLUS_ACCESSORY = 336 + 52  # 388, see module docstring

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
SHORT_Q = "What is the unit of force?"
SHORT_A = "The newton (N)"

# A one-card deck. `flashcard-homework.js` only needs the shape
# `flashcard_homework_drive.py`'s own FAKE already proves against the real
# engine; this is that same shape, trimmed to one card per content length.
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

# `__KB__(height, offsetTop)` — both halves of the real signal, stubbed.
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
# line boundary can be measured against. Exposed globally so MEASURE_JS and
# the scroll-reach check can both use it without re-declaring it.
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
  // Is any leaf's text straddling the face's own visible bottom edge —
  // a half-cut line? Only the bottom edge matters: scrollTop is 0 at rest,
  // so nothing can be cut at the top.
  // A leaf's OWN bounding box covers every visual line it wraps into, so a
  // leaf with more lines below the fold than above it is "below the fold"
  // as a box the instant the face scrolls at all — that is just "this
  // scrolls", not "a line is cut". The defect is a LINE straddling the
  // fold; `Range.getClientRects()` gives the real per-line boxes, matching
  // exactly what `snapToLineBoundary()` in the product code checks against.
  function anyClipped(face) {
    if (!face) { return false; }
    var fr = face.getBoundingClientRect();
    var ls = leaves(face);
    for (var i = 0; i < ls.length; i++) {
      var rg = document.createRange();
      rg.selectNodeContents(ls[i]);
      var rects = rg.getClientRects();
      for (var k = 0; k < rects.length; k++) {
        var r = rects[k];
        if (r.top < fr.bottom - 0.5 && r.bottom > fr.bottom + 0.5) { return true; }
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

MEASURE_JS = r"""
(function () {
  function rect(sel) { var e = document.querySelector(sel); if (!e) return null;
    var r = e.getBoundingClientRect(); return {top: r.top, bottom: r.bottom, left: r.left, right: r.right, h: r.height, w: r.width}; }
  var vv = window.visualViewport;
  var cardFit = document.querySelector('[data-card-fit]');
  var front = document.querySelector('[data-dc-tpl="10334"]');
  var cs = front ? getComputedStyle(front) : null;
  var box = document.querySelector('[data-hw="answer"]');
  var act = document.querySelector('[data-hw="act"]');
  var check = document.querySelector('[data-hw="check"]');
  var dlg = document.querySelector('[data-mrb-dialog="flashcards"]');
  var learnEl = document.querySelector('[data-hw="learn"]');
  var frontRect = front ? front.getBoundingClientRect() : null;
  var learnRect = learnEl ? learnEl.getBoundingClientRect() : null;
  var cueCs = cardFit ? getComputedStyle(cardFit, '::after') : null;
  return {
    vvTop: vv.offsetTop, vvHeight: vv.height, vvBottom: vv.offsetTop + vv.height,
    typing: dlg ? dlg.getAttribute('data-hw-typing') : null,
    learn: dlg ? dlg.getAttribute('data-hw-learn') : null,
    card: rect('[data-card-fit]'),
    front: front ? {scrollHeight: front.scrollHeight, clientHeight: front.clientHeight,
                    overflowY: cs.overflowY, text: front.innerText} : null,
    clipped: (front && window.__MRB_ANY_CLIPPED__) ? window.__MRB_ANY_CLIPPED__(front) : null,
    overflowAttr: cardFit ? cardFit.getAttribute('data-hw-overflow') : null,
    cueBg: cueCs ? cueCs.backgroundImage : null,
    box: rect('[data-hw="answer"]'),
    act: rect('[data-hw="act"]'),
    check: rect('[data-hw="check"]'),
    docWidth: document.documentElement.scrollWidth,
    innerWidth: window.innerWidth,
    hwBoxVar: dlg ? getComputedStyle(dlg).getPropertyValue('--hw-box-h') : null,
    learnPresent: !!learnEl,
    learnVisibleAtRest: (learnRect && frontRect)
      ? (learnRect.top >= frontRect.top - 0.5 && learnRect.bottom <= frontRect.bottom + 0.5)
      : null
  };
})()
"""

# Scroll the card's scrollable face all the way down and ask: is the model
# answer's FOOT now inside the visible box? (Its top may have scrolled past
# on a very long answer — that is fine; nothing is "unreachable" as long as
# the end of it can be brought into view.)
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


def run_case(port, width, height, content, step, offset_top, shots_dir, label):
    """One fresh browser: open the overlay, focus the box, bring the fake
    keyboard+accessory up (height − 336 − 52 [− offsetTop], at offsetTop),
    optionally go to the 'I don't know' learn step, measure, screenshot."""
    q, a = (LONG_Q, LONG_A) if content == "long" else (SHORT_Q, SHORT_A)
    fake = FAKE_TMPL % {"n": "1" if content == "long" else "2", "q": json.dumps(q), "a": json.dumps(a)}
    with cdp.Browser() as br:
        page = br.attach()
        page.send("Emulation.setDeviceMetricsOverride",
                  {"width": width, "height": height, "deviceScaleFactor": 3, "mobile": True})
        page.send("Emulation.setTouchEmulationEnabled", {"enabled": True, "maxTouchPoints": 5})
        page.send("Page.addScriptToEvaluateOnNewDocument", {"source": fake})
        page.send("Page.addScriptToEvaluateOnNewDocument", {"source": FAKE_VV})
        page.send("Page.addScriptToEvaluateOnNewDocument", {"source": LEAF_HELPERS_JS})
        page.goto("http://127.0.0.1:%d/student/class-fixture.html" % port)
        settle(0.8)
        ok = page.eval(LOAD)
        if ok is not True:
            check(False, "%s: fixture mounted (__MRB_OPEN_HW__ present)" % label)
            return None
        page.eval("window.__MRB_FC_SUBJECT__ = %s" % json.dumps({AID: "chemistry"}))
        page.eval("window.__MRB_OPEN_HW__(%s)" % json.dumps(AID))
        settle(0.6)

        if step == "learn":
            page.eval("(function(){var b=document.querySelector('[data-hw=\"idk\"]'); if(b) b.click();})()")
            settle(0.3)

        # Keyboard + accessory bar up: one combined visualViewport shrink,
        # exactly what real iOS/Android report (see module docstring). The
        # BOTTOM of the visual viewport (offsetTop + height) is pinned at
        # height − 388 regardless of offsetTop, matching a page that has
        # scrolled a little while the keyboard occupies the same physical
        # strip of the screen.
        target = height - KEYBOARD_PLUS_ACCESSORY - offset_top
        page.eval("(function(){var t=document.querySelector('[data-hw=\"answer\"]'); if(t) t.focus();})()")
        page.eval("window.__KB__(%d, %d)" % (target, offset_top))
        settle(0.5)

        m = page.eval(MEASURE_JS)
        reach = page.eval(SCROLL_REACH_JS) if step == "learn" else None

        if shots_dir:
            os.makedirs(shots_dir, exist_ok=True)
            # Cropped to the visual viewport (0…H−388 at offsetTop 0), so the
            # frame looks like the phone with the keyboard up rather than
            # showing the simulation's bare page bleeding through underneath
            # (Chrome has no real on-screen keyboard to paint there).
            vv_h = height - KEYBOARD_PLUS_ACCESSORY - offset_top
            res = page.send("Page.captureScreenshot", {
                "format": "png", "fromSurface": True,
                "clip": {"x": 0, "y": offset_top, "width": width, "height": vv_h, "scale": 1}
            })
            path = os.path.join(shots_dir, "%s.png" % label)
            with open(path, "wb") as fh:
                fh.write(base64.b64decode(res["data"]))

    # ── assertions ──────────────────────────────────────────────────────
    vv_bottom = m["vvBottom"]
    check_bottom = m["check"]["bottom"] if m["check"] else None
    box = m["box"]
    act = m["act"]
    front = m["front"]

    ok1 = check_bottom is not None and (vv_bottom - check_bottom) <= 8 and check_bottom <= vv_bottom + 0.5
    check(ok1, "%s: Check's bottom within 8px above the keyboard top (check=%.1f keyboard_top=%.1f gap=%.1f)"
          % (label, check_bottom or -1, vv_bottom, (vv_bottom - check_bottom) if check_bottom else -1))

    gap = (act["top"] - box["bottom"]) if (act and box) else None
    ok2 = gap is not None and gap <= 12
    check(ok2, "%s: answer box fills down to Check (gap=%.1fpx)" % (label, gap if gap is not None else -1))

    ok2b = bool(box) and box["h"] >= 90
    check(ok2b, "%s: answer box is at least 90px (box_h=%.1f)" % (label, box["h"] if box else -1))

    overflowing = front and front["scrollHeight"] > front["clientHeight"] + 1
    fits = front and not overflowing
    cue_on = m["overflowAttr"] == "1" and bool(m["cueBg"]) and "gradient" in (m["cueBg"] or "")

    ok_clip = not m["clipped"]
    check(ok_clip, "%s: no line clipped at the card's bottom edge (clipped=%s)" % (label, m["clipped"]))

    if overflowing:
        ok3 = front["overflowY"] == "auto" and cue_on
        check(ok3, "%s: card scrolls AND shows the fade cue (overflowY=%s overflowAttr=%s cueBg=%s)"
              % (label, front["overflowY"], m["overflowAttr"], m["cueBg"]))
    else:
        ok3 = not cue_on
        check(ok3, "%s: card fits fully, no stray cue (overflowAttr=%s)" % (label, m["overflowAttr"]))

    ok4 = m["docWidth"] <= m["innerWidth"] + 1
    check(ok4, "%s: no horizontal overflow (docWidth=%s innerWidth=%s)" % (label, m["docWidth"], m["innerWidth"]))

    if step == "learn":
        ok5 = m["learnPresent"]
        check(ok5, "%s: the model answer's block is in the DOM" % label)
        if content == "short":
            # At offsetTop=0 (the realistic case — a fixed overlay does not
            # itself need the page to have scrolled) this is a hard
            # requirement. At offsetTop=40 — an ADDITIONAL, deliberately
            # extreme stress combination (the smallest tested device, 360
            # wide, stacked with a 40px page-scroll offset on TOP of the
            # full keyboard) the visible budget can drop to ~150px for the
            # whole card+box+act row; there is no allocation that both
            # keeps Check above the keyboard AND shows a 2-part (question +
            # model answer) card with zero scroll in that little room. The
            # real invariants — never clipped, always reachable by
            # scrolling, Check still correctly placed — are still asserted
            # unconditionally below and above, and still hold here.
            if offset_top == 0:
                ok6 = bool(m["learnVisibleAtRest"])
                check(ok6, "%s: a short model answer is fully visible without scrolling" % label)
            else:
                print("    INFO  %s: short model answer visible-at-rest=%s (not required at offsetTop=%d — see comment)"
                      % (label, m["learnVisibleAtRest"], offset_top))
        if reach is not None:
            ok7 = bool(reach.get("reach"))
            check(ok7, "%s: the model answer is reachable by scrolling the card (frontBottom=%.1f learnBottom=%.1f)"
                  % (label, reach.get("frontBottom", -1), reach.get("learnBottom", -1)))

    print("    %s: card_h=%.1f box_h=%.1f gap=%.1f check_bottom=%.1f keyboard_top=%.1f "
          "typing=%s learn=%s overflowing=%s clipped=%s cue=%s"
          % (label, m["card"]["h"] if m["card"] else -1, box["h"] if box else -1,
             gap if gap is not None else -1, check_bottom or -1, vv_bottom, m["typing"], m["learn"],
             overflowing, m["clipped"], cue_on))
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


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--shots", default=None, help="base dir; before/ and after/ subfolders are made under it")
    ap.add_argument("--pass-name", choices=["before", "after", "both"], default="both")
    args = ap.parse_args()

    with open(KEYBOARD_JS_PATH, "r") as fh:
        fixed_text = fh.read()  # the worktree's current (AFTER) version
    before_text = git_show("origin/main", KEYBOARD_JS_PATH)

    devices = [(390, 844), (360, 740)]
    contents = ["long", "short"]
    steps = ["card", "learn"]

    # (pass label, file variant, offsetTop, take screenshots?)
    sweeps = [
        ("before", "before", 0, False),
        ("after", "after", 0, True),
        ("after-offset40", "after", 40, False),
    ]
    if args.pass_name == "before":
        sweeps = [s for s in sweeps if s[1] == "before"]
    elif args.pass_name == "after":
        sweeps = [s for s in sweeps if s[1] == "after"]

    results = {}
    sweep_stats = {}  # sweep name -> [cases, failed assertions] — labels alone
                      # can't be summed by prefix: "after-" is a prefix of
                      # "after-offset40-" too.
    restore_to = fixed_text
    try:
        for (sweep, variant, offset_top, want_shots) in sweeps:
            print("\n══ %s (%s, offsetTop=%d) ══" % (sweep.upper(),
                  "origin/main, unfixed" if variant == "before" else "this worktree, fitCard()+fitBox()",
                  offset_top))
            swap_in(before_text if variant == "before" else fixed_text)
            server, port = cdp.serve(ROOT)
            try:
                for (w, h) in devices:
                    for content in contents:
                        for step in steps:
                            label = "%s-%dx%d-%s-%s" % (sweep, w, h, content, step)
                            shots_dir = os.path.join(args.shots, variant) if (args.shots and want_shots) else None
                            n0 = len(FAILS)
                            # A DNS blip, a Chrome websocket hiccup, a cold
                            # start — none of these are findings about the
                            # code; retry exactly once (gate_registry's own
                            # convention) before it counts. A second failure
                            # of any shape is real and is not caught here.
                            try:
                                m = run_case(port, w, h, content, step, offset_top, shots_dir, label)
                            except (cdp.CDPError, TimeoutError, OSError) as exc:
                                print("    RETRY %s after transient error: %r" % (label, exc))
                                time.sleep(1.0)
                                del FAILS[n0:]
                                m = run_case(port, w, h, content, step, offset_top, shots_dir, label)
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
    for (sweep, variant, offset_top, want_shots) in sweeps:
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
