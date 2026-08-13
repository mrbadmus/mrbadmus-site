#!/usr/bin/env python3
"""3d_render_check.py — the MRB-187 browser-level check for the mesh renderer.

Stage 2 replaced the placeholder stage with a real React Three Fiber renderer
(``3d-studio/src/renderer/mesh/``). Its four load-bearing promises cannot be
tested in vitest, because jsdom has no WebGL and therefore no camera, no
raycaster against a real scene graph, and no canvas to remount or not remount:

  * honest occlusion — a dot vanishes when the specimen turns its anchor away,
    rather than a renderer that reports ``visible: true`` for everything (which
    is exactly what Stage 1's placeholder did, and which every DOM-level test
    would happily accept);
  * exact reset — the rail's Reset returns the camera to the authored default
    view to the pixel, and stays there;
  * live tier change — Ultra / High / Balanced retune the same canvas rather
    than tearing one down and building another;
  * failure is a route — a specimen mesh that will not load lands on the flat
    stage, not on a broken viewport with an apology on it.

So they are tested here, in the installed Chrome, over CDP, on the BUILT app —
the same stdlib harness (``ks3_browser.py``) and the same reporting shape as
``3d_parity.py``, which serves ``3d-studio/dist/`` the same way this does.

═══════════════════════════════════════════════════════════════════════════
WHAT THIS CHECK DOES, AND WHAT IT CANNOT DO — read before trusting it
═══════════════════════════════════════════════════════════════════════════

Checks 1–10 are gates: any failure exits non-zero.

  1. It renders at all. The mesh renderer mounts, the stage container reaches
     ``ready``, a <canvas> exists inside the stage.
  2. Honest occlusion. At the default view SOME anchors face the camera and
     some do not, so some dots are drawn and some are not; a full turn in six
     steps brings every hotspot in ``content/heart.json`` into view at some
     angle; the half-turn sample replaces most of what was visible with what
     was not; Reset returns the default view exactly.
  3. Reset is exact. Dot coordinates come back as identical strings after a
     drag, and are still identical a second later (no slow drift). Reset from
     the default view is a no-op.
  4. Auto-rotate. On ⇒ the dots move. Off ⇒ they hold still. ``aria-pressed``
     tracks both.
  5. Live tier change, no remount. Driven through the real affordance (the
     quality chip and its radio menu), the container's tier moves A→B→C while
     the SAME canvas element survives — proven by a probe attribute stamped on
     it before the journey and read back after each step.
  6. Failure is a route. A second copy of the build, with the specimen GLB
     deleted, must land on the flat renderer: FLAT DIAGRAM chip, no quality
     chip, and no error/failure/apology text anywhere on the page.

  7. Isolate and layers (MRB-188). Isolate steps through every part the asset
     declares, drawing exactly one at a time and naming it from the file; one
     step past the last returns the whole specimen. Layers peels the outer
     depth level away. Both are judged by the HOTSPOT LAYER as well as by the
     part count — occlusion is recomputed against whatever is still drawn, so
     taking geometry off the stage must change which dots are visible, which
     is the one thing a step counter cannot fake.

  8. The cross-section cuts, and the cut is CAPPED (MRB-189). The only check
     here that reads pixels rather than the DOM, because "is there a cut face
     at all" is not a question any attribute can answer. Repeated at all three
     tiers: Tier A renders through a post-processing composer whose own render
     target would silently un-cap the cut if it carried no stencil buffer.
     Whether the cap covers every last pixel of the cut is NOT settled here —
     see the limitation in the check's own docstring.

  9. A Tier D device never downloads Three.js (ruling on MRB-190). Driven in
     a browser with WebGL genuinely off, against the chunks that are FOUND to
     contain Three rather than the ones named as if they did. The same run
     confirms a capable browser does fetch it, so the split cannot pass by
     having broken both halves.

 10. The retrieval round frames its target before asking (ruling on
     MRB-191). Driven from the WORST case on purpose: a round is opened once
     to find out which structure it asks about first, the specimen is turned
     until THAT structure's marker is measurably off the stage, and only then
     is a round opened from there. The pulsing 52px marker must be on screen
     and inside the stage when the prompt appears.

Frame timing is a REPORT, never a gate, and carries no check number for that
reason — see its banner. Nothing it prints can change the exit code.

WHAT IT DOES NOT CATCH, stated plainly:

  * Whether the specimen LOOKS right. Nothing here is a pixel comparison
    against a reference image. Check 5's tier screenshots are compared by
    bytes only, which proves the tiers differ, not that either is correct.
  * Real-device performance. The frame-timing numbers come from SwiftShader
    on the CPU. See its banner.
  * Composition, colour and type — that is ``3d_parity.py``'s job, and this
    script deliberately duplicates none of it.
  * Whether an anchor sits on the RIGHT structure. heart.json now carries
    authored ``position3d`` for all fourteen hotspots (they were the all-zero
    Stage-8 sentinel while nothing had been acquired, and the renderer derived
    stand-in anchors on the mesh surface instead). Nothing here can tell an
    anchor over the aorta from one a centimetre into the pulmonary artery —
    that is the science gate's, and the manifest's. The occlusion MECHANISM is
    what is under test; where each anchor belongs arrives with the content.

HARNESS NOTES, both learned the hard way:

  * Chrome is launched with ``--enable-unsafe-swiftshader``. Without it
    headless Chrome has no WebGL at all, the capability probe lands on tier D,
    and the app correctly shows the paper stage — every check below would then
    be measuring the fallback while appearing to measure the renderer. Check 1
    reports that as a HARNESS fault, not an app fault, exactly as
    ``3d_parity.py`` does for its own probe.
  * ``page.screenshot()`` overrides device metrics and does not restore the
    viewport exactly. A screenshot taken mid-sequence silently moves the stage
    and every hotspot coordinate with it. Screenshots therefore happen only at
    the END of check 5's sequence, and the viewport is re-asserted afterwards.

One honesty note on check 3: the shell rounds dot coordinates to whole pixels
(``Math.round`` in ``useHotspotDots``), so "identical strings" means the camera
returned to within half a pixel of the default view, not to identical floats.
The floats are the renderer's business and are asserted in vitest; what this
gate owns is that nothing a student can see has moved.
"""

from __future__ import annotations

import json
import math
import os
import re
import shutil
import sys
import tempfile
import time

import ks3_browser as cdp

HERE = os.path.dirname(os.path.abspath(__file__))
APP = os.path.join(HERE, "3d-studio")
DIST = os.path.join(APP, "dist")
HEART = os.path.join(APP, "content", "heart.json")
SPECIMEN_ASSETS = os.path.join("assets")

VIEWPORT = (1440, 900)

# A left-button drag this far across the stage turns the specimen roughly 180°
# at the desktop stage size: OrbitControls maps horizontal travel to azimuth
# against the element's height, and the stage is ~1055px tall here. Verified
# by hand before it was written down.
DRAG_PX = 520
DRAG_STEPS = 30

# A full revolution, and how finely check 2 samples it. Twice the half turn
# above is 360°; six steps samples it every 60°, which is the coarsest sweep
# that can still claim to have looked all the way round. Measured on the
# acquired heart: the union closes over all fourteen hotspots by the fourth
# step, so this is not a threshold fitted to scrape a pass.
SWEEP_STEPS = 6
SWEEP_PX = 2.0 * DRAG_PX / SWEEP_STEPS

# Quarter turns, used by check 10 to hunt for a view from which the round's
# own target is not on screen. Four of them close the circle.
QUARTER_PX = DRAG_PX / 2.0
QUARTER_TURNS = 4

# Below this many hotspots, "some are visible and some are not" is not a
# question worth asking of a specimen — see check 2. The generated test
# specimen declares two.
PARTIAL_MIN_HOTSPOTS = 4

# How still is still. The controls damp (dampingFactor 0.075), so a released
# drag or a just-switched-off auto-rotate keeps creeping for a second or more.
# Waiting a fixed sleep instead of waiting for stillness is how this check
# would become flaky, so it polls for a run of identical samples.
SETTLE_STABLE_RUNS = 5
SETTLE_INTERVAL = 0.3
SETTLE_TIMEOUT = 15.0

# How long "holds still" and "keeps moving" are given to prove themselves.
HOLD_SECONDS = 1.0

# The gap check 8 leaves between a change and the capture that measures it,
# and — crucially — the same gap it leaves when measuring its own noise floor.
SETTLE_GAP = 0.6

# Frame samples per tier in the frame-timing report.
FRAME_SAMPLES = 120

# The framing move the retrieval round makes is animated on purpose (620ms,
# eased). This is how long check 10 gives it to land before it looks.
FRAME_MOVE = 1.4

# A style change has to reach the compositor before a capture can see it —
# check 8 hides the hotspot layer for its screenshots and this is the beat it
# leaves for the frame that draws the stage without it.
DOT_HIDE_SETTLE = 0.15


# ── the page-side helpers ────────────────────────────────────────────────
#
# Injected after every navigation, in the same spirit as 3d_parity's
# window.__st: the Python side stays readable, and the DOM knowledge lives in
# one place.

_JS = r"""
window.__rc = {
  cont: function () {
    return document.querySelector('[data-testid=renderer-container]');
  },
  ds: function (key) {
    var el = this.cont();
    if (!el) { return null; }
    var v = el.dataset[key];
    return v === undefined ? null : v;
  },
  /** identity + position of every dot currently on the stage, in DOM order */
  dots: function () {
    return Array.prototype.map.call(
      document.querySelectorAll('.hotspot'),
      function (e) {
        return (e.textContent || '').trim() + '@' + e.style.left + ',' + e.style.top;
      });
  },
  n: function (sel) { return document.querySelectorAll(sel).length; },
  text: function (sel) {
    var el = document.querySelector(sel);
    return el ? (el.textContent || '').trim() : null;
  },
  rect: function (sel) {
    var el = document.querySelector(sel);
    if (!el) { return null; }
    var r = el.getBoundingClientRect();
    return { x: r.x, y: r.y, w: r.width, h: r.height };
  },
  /** what the pointer would actually hit — a dot sitting over the drag point
   *  would swallow the press and the specimen would never turn */
  tagAt: function (x, y) {
    var el = document.elementFromPoint(x, y);
    return el ? el.tagName.toLowerCase() : null;
  },
  rail: function (label) {
    var b = Array.prototype.slice.call(document.querySelectorAll('.railbtn'))
      .find(function (x) { return x.getAttribute('aria-label') === label; });
    if (!b) { return false; }
    b.click();
    return true;
  },
  autorot: function () {
    var b = document.querySelector('.autorot');
    if (!b) { return false; }
    b.click();
    return true;
  },
  autorotPressed: function () {
    var b = document.querySelector('.autorot');
    return b ? b.getAttribute('aria-pressed') : null;
  },
  openQuality: function () {
    var c = document.querySelector('.chip');
    if (!c) { return false; }
    c.click();
    return true;
  },
  pickQuality: function (word) {
    var rows = Array.prototype.slice.call(
      document.querySelectorAll('[role=menuitemradio]'));
    var row = rows.find(function (e) {
      return (e.textContent || '').trim().indexOf(word) === 0;
    });
    if (!row) { return false; }
    row.click();
    return true;
  },
  /** enter the retrieval room through the header's own mode control */
  enterRetrieval: function () {
    var b = Array.prototype.slice.call(
      document.querySelectorAll('.modeseg button'))
      .find(function (x) { return /retrieve/i.test(x.textContent || ''); });
    if (!b) { return false; }
    b.click();
    return true;
  },
  /** and leave it by the same control. The mode segment is drawn in both
   *  rooms, so this is the room's own way out and not a back door. */
  leaveRetrieval: function () {
    var b = Array.prototype.slice.call(
      document.querySelectorAll('.modeseg button'))
      .find(function (x) { return /explore/i.test(x.textContent || ''); });
    if (!b) { return false; }
    b.click();
    return true;
  },
  /** give up on the current question, which is the only affordance that says
   *  out loud WHICH structure was being asked about */
  reveal: function () {
    var b = document.querySelector('.rreveal__link');
    if (!b) { return false; }
    b.click();
    return true;
  },
  revealedLabel: function () {
    var el = document.querySelector('.rreveal-card__title');
    return el ? (el.textContent || '').trim() : null;
  },
  /** the pulsing 52px target dot, if one is on the stage */
  target: function () {
    var t = document.querySelector('.hotspot[data-state=target]');
    if (!t) { return null; }
    var r = t.getBoundingClientRect();
    var s = document.querySelector('.stage').getBoundingClientRect();
    return {
      x: r.x + r.width / 2, y: r.y + r.height / 2,
      w: r.width, h: r.height,
      inside: r.x >= s.x && r.y >= s.y &&
              r.x + r.width <= s.x + s.width &&
              r.y + r.height <= s.y + s.height,
      ping: t.querySelectorAll('.hotspot__ping').length
    };
  },
  /** Swap Design's room for one flat screaming colour, so a hole in the
   *  specimen is a pixel value rather than a judgement call. The canvas is
   *  transparent by design, so whatever is behind it shows through any gap. */
  voidBackdrop: function () {
    var s = document.getElementById('__voidprobe') || document.createElement('style');
    s.id = '__voidprobe';
    s.textContent = '.stage--viewport{background:#FF00FF !important;}';
    document.head.appendChild(s);
    return true;
  },
  restoreBackdrop: function () {
    var s = document.getElementById('__voidprobe');
    if (s) { s.remove(); }
    return true;
  },
  /** Take the hotspot layer out of the PICTURE without taking it out of the
   *  DOM. The dots are shell elements painted in the accent, sitting over the
   *  stage; check 8 measures canvas pixels and they are not canvas. Hidden
   *  rather than removed so every dot read in that check still sees real
   *  visibility — display:none changes nothing about which dots exist, where
   *  they are, or what the renderer thinks. */
  hideDots: function () {
    var s = document.getElementById('__dotprobe') || document.createElement('style');
    s.id = '__dotprobe';
    s.textContent = '.hotspot{display:none !important;}';
    document.head.appendChild(s);
    return true;
  },
  showDots: function () {
    var s = document.getElementById('__dotprobe');
    if (s) { s.remove(); }
    return true;
  },
  /** how many of the parts the asset declares are currently drawn */
  partsShown: function () {
    var v = this.ds('partsShown');
    return v === null ? null : parseInt(v, 10);
  },
  stampCanvas: function () {
    var c = document.querySelector('canvas');
    if (!c) { return false; }
    c.dataset.probe = '1';
    return true;
  },
  canvasProbe: function () {
    var c = document.querySelector('canvas');
    return c ? (c.dataset.probe === undefined ? null : c.dataset.probe) : null;
  },
  /** n consecutive requestAnimationFrame deltas, in ms */
  frames: function (n) {
    return new Promise(function (resolve) {
      var out = [], last = performance.now(), seen = 0;
      function tick(t) {
        out.push(t - last);
        last = t;
        seen += 1;
        // the first delta spans from this call to the first frame, not
        // between two frames — dropped.
        if (seen > n) { resolve(out.slice(1)); }
        else { requestAnimationFrame(tick); }
      }
      requestAnimationFrame(tick);
    });
  }
};
true
"""


# ── driving helpers ──────────────────────────────────────────────────────


def inject(page):
    page.eval(_JS)


def wait_state(page, timeout=45.0):
    """Poll the stage container until it settles on ready or failed.

    Never a fixed sleep: one of the two renderers now loads a GLB over the
    network, and a slow decode on a busy machine is not a failure.
    """
    deadline = time.time() + timeout
    last = None
    while time.time() < deadline:
        last = page.eval("window.__rc.ds('state')")
        if last in ("ready", "failed"):
            return last
        time.sleep(0.15)
    return last


def dots(page):
    return tuple(page.eval("window.__rc.dots()") or [])


def settle(page, timeout=SETTLE_TIMEOUT):
    """Wait until the dots stop moving, and return where they stopped.

    "Stopped" means SETTLE_STABLE_RUNS identical samples in a row, which at
    the interval above is about a second and a half of genuine stillness —
    long enough for the controls' damping tail to die rather than merely to
    slow down.
    """
    deadline = time.time() + timeout
    last, runs = None, 0
    while time.time() < deadline:
        now = dots(page)
        if now == last:
            runs += 1
            if runs >= SETTLE_STABLE_RUNS:
                return now
        else:
            last, runs = now, 1
        time.sleep(SETTLE_INTERVAL)
    return last if last is not None else dots(page)


def drag_horizontal(page, px=DRAG_PX, steps=DRAG_STEPS):
    """Turn the specimen with a real left-button drag across the stage.

    Raw CDP input, not a synthetic JS event: OrbitControls listens on the
    canvas's pointer events, and only the browser's own input pipeline
    produces the sequence it expects.

    Returns None on success, or a problem string if NO press point down the
    middle of the stage is over the canvas (a hotspot dot parked on the press
    point would swallow the press and the specimen would silently never turn —
    a harness fault wearing the costume of a broken renderer).

    The candidate list is new, and it is not a softening of that guard. This
    used to press the stage centre and give up if anything covered it, which
    was safe while the fixture had two anchors and neither projected near the
    middle. A real specimen puts anchors wherever its structures are, each dot
    carries a 48px touch area (§04), and check 2 now stops at six views
    instead of two — so a covered centre is an ordinary event rather than a
    freak one. Where the press lands does not affect the turn: OrbitControls
    maps DELTA to azimuth and ignores the origin. If every candidate is
    covered this still refuses to drag.
    """
    rect = page.eval("window.__rc.rect('.stage')")
    if not rect:
        return "no .stage to drag on"
    cx = rect["x"] + rect["w"] / 2.0

    cy, covered = None, []
    for fraction in (0.5, 0.62, 0.38, 0.75, 0.25):
        y = rect["y"] + rect["h"] * fraction
        tag = page.eval("window.__rc.tagAt(%f, %f)" % (cx, y))
        if tag == "canvas":
            cy = y
            break
        covered.append("%.0f%%:<%s>" % (fraction * 100, tag))
    if cy is None:
        return ("every press point down the middle of the stage is covered by "
                "something other than the canvas (%s) — the drag would never "
                "reach the controls" % ", ".join(covered))

    page.send("Input.dispatchMouseEvent", {
        "type": "mousePressed", "x": cx, "y": cy,
        "button": "left", "buttons": 1, "clickCount": 1})
    for i in range(1, steps + 1):
        page.send("Input.dispatchMouseEvent", {
            "type": "mouseMoved", "x": cx + px * i / float(steps), "y": cy,
            "button": "left", "buttons": 1})
    page.send("Input.dispatchMouseEvent", {
        "type": "mouseReleased", "x": cx + px, "y": cy,
        "button": "left", "buttons": 0, "clickCount": 1})
    return None


def reset_view(page):
    return page.eval("window.__rc.rail('Reset view')")


def set_quality(page, word):
    """Drive the real affordance: open the quality chip, click a radio row."""
    if not page.eval("window.__rc.openQuality()"):
        return "no quality chip on the stage"
    time.sleep(0.25)
    if not page.eval("window.__rc.n('.qpanel')"):
        return "the quality chip did not open its panel"
    if not page.eval("window.__rc.pickQuality(%r)" % word):
        return "no quality option starting %r" % word
    time.sleep(0.6)
    return None


def hotspot_ids():
    """Every dot id the shell can draw for this specimen, in record order.

    A dot's id is its TEXT: the shell numbers the hotspots by their position
    in the specimen's own list ('01', '02', …), so the ids are derived from
    the record's length and never written down here. Nothing in this file may
    hardcode how many structures the heart has — that is content, and content
    changes.
    """
    import json
    with open(HEART, encoding="utf-8") as fh:
        count = len(json.load(fh)["hotspots"])
    return tuple("%02d" % (i + 1) for i in range(count))


def ids_of(sample):
    """The dot ids in a `dots()` sample, as a set — positions dropped."""
    return frozenset(entry.split("@", 1)[0] for entry in sample)


# ── the report ───────────────────────────────────────────────────────────


class Report:
    """One pass/fail line per check, plus indented detail, in 3d_parity's
    house style. Problems accumulate; check 7 adds none by construction."""

    def __init__(self):
        self.problems = []
        self.results = []  # (number, title, ok)

    def check(self, number, title, problems, details=()):
        ok = not problems
        self.results.append((number, title, ok))
        print("  %s %d. %s" % ("✓" if ok else "✗", number, title))
        for d in details:
            print("       %s" % d)
        for p in problems:
            print("       ✗ %s" % p)
            self.problems.append("%d. %s — %s" % (number, title, p))
        return ok

    def note(self, text):
        print("       %s" % text)


# ── checks 1–10 ──────────────────────────────────────────────────────────


def check_renders(page, report):
    """1. It renders at all."""
    problems, details = [], []

    t0 = time.time()
    state = wait_state(page)
    took = time.time() - t0

    detected = page.eval(
        "(document.querySelector('.app')||{getAttribute:function(){return null}})"
        ".getAttribute('data-detected-tier')")
    if detected == "D":
        problems.append(
            "capability probe landed on tier D — headless Chrome has no WebGL "
            "despite --enable-unsafe-swiftshader, so the app correctly showed "
            "the paper stage and every check below would be measuring the "
            "fallback. HARNESS FAULT, not app fault.")
        report.check(1, "it renders at all", problems, details)
        return False

    renderer = page.eval("window.__rc.ds('renderer')")
    if renderer != "mesh":
        problems.append("stage container reports renderer=%r, expected 'mesh'"
                        % renderer)
    if state != "ready":
        problems.append("stage container never reached 'ready' (state=%r after "
                        "%.1fs)" % (state, took))
    canvases = page.eval("window.__rc.n('.stage canvas')")
    if canvases != 1:
        problems.append("expected exactly 1 <canvas> inside the stage, found %d"
                        % canvases)

    source = page.eval("window.__rc.ds('specimenSource')")
    details.append("renderer=%r  state=%r (%.1fs into the readiness poll, "
                   "which starts after the load event)  detected tier=%s  "
                   "canvases=%d" % (renderer, state, took, detected, canvases))
    if source:
        details.append("specimen source: %s (the acquired heart GLB is still "
                       "Stage-8 work; the build points the renderer at the "
                       "generated test specimen)" % source)

    ok = report.check(1, "it renders at all", problems, details)
    return ok


def check_occlusion(page, report, every):
    """2. Honest occlusion.

    WHAT THIS USED TO ASSERT, and why it was the fixture talking. Two things:
    that the default view drew one dot per hotspot in the record, and that a
    drag of roughly 180° left NO dot on the stage at all. Both held on the
    generated test specimen — two anchors, on a convex form, both facing the
    camera at rest and both behind it after half a turn — and both contradict
    the feature on a real specimen. Stage 2's entire point is that an anchor
    on the far side reports visible:false and the shell drops the dot; on a
    deeply concave heart with fourteen anchors spread over its surface, about
    half face the camera at any one moment and the other half do not. Seeing 7
    of 14 IS the mechanism working, and 0 after a half turn would mean the far
    side of the heart carries no structures — it carries the left atrium and
    both pulmonary vessels. The old form was demanding the defect back.

    What replaces it are three properties of the MECHANISM, which hold on any
    specimen of any shape, and which a renderer that reported visible:true for
    everything fails on every count:

      * SOME ARE DRAWN AND SOME ARE NOT at the default view. Read against the
        record's own count rather than a number written here. A specimen small
        enough that every anchor could honestly face the camera at once is not
        asked the strong form at all — the generated fixture declares two, and
        this file must still hold against it if the GLB is ever removed.
      * EVERY HOTSPOT IS REACHABLE BY ROTATION. A full turn in six steps, the
        dot ids unioned. This is the one a student's learning actually rests
        on: a structure that can never be brought into view cannot be
        labelled, learned, or asked about in a retrieval round.
      * THE TURN CHANGES WHAT IS ON THE STAGE. A clear majority of what was
        visible must be gone by the half-turn sample, and at least one dot
        that was not visible before must have arrived. Survivors are
        legitimate on a real specimen and were impossible on the fixture: a
        thin structure — the pulmonary artery, the pulmonary vein — has an
        anchor that can be genuinely visible from front and back, which is
        why this asks for a majority rather than for none.
    """
    problems, details = [], []
    total = len(every)

    at_default = settle(page)
    details.append("default view: %d of %d dot(s) — %s"
                   % (len(at_default), total, ", ".join(at_default) or "none"))

    # ── (a) some face the camera, some do not ─────────────────────────────
    if not at_default:
        problems.append(
            "not one of the %d hotspot(s) has a dot at the default view — the "
            "anchors are not reaching the screen at all" % total)
    elif total >= PARTIAL_MIN_HOTSPOTS and len(at_default) >= total:
        problems.append(
            "all %d hotspot(s) have a dot at the default view. The anchors sit "
            "over structures on every side of a solid specimen, so the far "
            "ones must report visible:false — a renderer that reported "
            "visible:true for everything looks exactly like this." % total)
    if total < PARTIAL_MIN_HOTSPOTS:
        details.append(
            "the specimen declares %d hotspot(s), too few to ask that some be "
            "hidden while others are shown — only 'at least one is visible' is "
            "asserted at the default view" % total)

    # ── (b) and (c), off one sweep ────────────────────────────────────────
    # The half-turn sample is the halfway point of the full turn, so the two
    # properties come out of the same journey rather than out of two.
    union, per_step, half_turn = set(ids_of(at_default)), [len(at_default)], None
    for step in range(SWEEP_STEPS):
        fault = drag_horizontal(page, px=SWEEP_PX)
        if fault:
            problems.append("HARNESS: " + fault)
            break
        sample = settle(page)
        union |= ids_of(sample)
        per_step.append(len(sample))
        if step + 1 == SWEEP_STEPS // 2:
            half_turn = sample
    details.append("a full turn in %d steps of %.0fpx — dots at each: %s"
                   % (SWEEP_STEPS, SWEEP_PX,
                      " → ".join(str(n) for n in per_step)))

    missing = sorted(set(every) - union)
    if missing:
        problems.append(
            "%d of %d hotspot(s) never appeared anywhere in a full turn: %s. A "
            "structure a student cannot bring into view cannot be labelled, "
            "learned, or asked about." % (len(missing), total, ", ".join(missing)))
    else:
        details.append("every one of the %d hotspot(s) appears somewhere in the "
                       "turn — none is unreachable" % total)

    if half_turn is None:
        problems.append("the sweep never reached its halfway sample, so what a "
                        "half turn does to the stage was not measured")
    else:
        before, after = ids_of(at_default), ids_of(half_turn)
        survived, fresh = sorted(before & after), sorted(after - before)
        if len(survived) * 2 > len(before):
            problems.append(
                "%d of the %d dot(s) visible at the default view were STILL "
                "visible after a half turn (%s) — the far side is not being "
                "occluded" % (len(survived), len(before), ", ".join(survived)))
        if not fresh:
            problems.append(
                "the half turn brought no new dot into view (%s) — the far "
                "side of a specimen carries structures too, and a visibility "
                "test that never changes its answer draws the same set at "
                "every angle"
                % (", ".join(sorted(after)) or "nothing on the stage"))
        details.append(
            "half turn: %d of %d survived (%s) · %d arrived (%s)"
            % (len(survived), len(before), ", ".join(survived) or "none",
               len(fresh), ", ".join(fresh) or "none"))

    reset_view(page)
    back = settle(page)
    if back != at_default:
        problems.append("Reset did not bring the default view back: %s → %s"
                        % (list(at_default), list(back)))
    else:
        details.append("Reset returns the default view exactly (%d dot(s))"
                       % len(back))

    report.check(2, "honest occlusion", problems, details)


def check_reset(page, report, default_view):
    """3. Reset is exact.

    `default_view` is a PRECONDITION and nothing more: everything this check
    asserts, it asserts against a baseline it takes itself, a line below. It
    used to read "one dot per hotspot in the record", which was the generated
    fixture's arithmetic (see check 2) and says nothing about where the camera
    is. What stands in its place is the dot set the default view actually drew
    once, right after check 1 — measured, so it stays true of whatever
    specimen is loaded, and still fails loudly if some earlier check left the
    camera somewhere else.
    """
    problems, details = [], []

    baseline = settle(page)
    if ids_of(baseline) != ids_of(default_view):
        problems.append("not at the default view before the test: dots %s, "
                        "expected %s"
                        % (sorted(ids_of(baseline)), sorted(ids_of(default_view))))

    # (a) reset from the default view changes nothing
    reset_view(page)
    noop = settle(page)
    if noop != baseline:
        problems.append("Reset from the default view MOVED the camera: %s → %s"
                        % (list(baseline), list(noop)))
    else:
        details.append("Reset with no prior drag is a no-op: %s"
                       % ", ".join(baseline))

    # (b) drag away, reset, compare as strings
    fault = drag_horizontal(page)
    if fault:
        problems.append("HARNESS: " + fault)
        report.check(3, "reset is exact", problems, details)
        return
    settle(page)  # let the damping tail die before resetting

    reset_view(page)
    after = settle(page)
    if after != baseline:
        problems.append("after drag → Reset the coordinates differ: expected "
                        "%s, got %s" % (list(baseline), list(after)))
    else:
        details.append("after drag → Reset: identical strings (%d dot(s))"
                       % len(after))

    # (c) and no slow drift a second later
    time.sleep(HOLD_SECONDS)
    later = dots(page)
    if later != after:
        problems.append("the view drifted %.1fs after Reset: %s → %s"
                        % (HOLD_SECONDS, list(after), list(later)))
    else:
        details.append("still identical %.1fs later — no slow drift"
                       % HOLD_SECONDS)

    report.check(3, "reset is exact", problems, details)


def check_autorotate(page, report):
    """4. Auto-rotate."""
    problems, details = [], []

    before = page.eval("window.__rc.autorotPressed()")
    if before != "false":
        problems.append("auto-rotate starts with aria-pressed=%r, expected "
                        "'false'" % before)

    if not page.eval("window.__rc.autorot()"):
        problems.append("no .autorot toggle on the rail")
        report.check(4, "auto-rotate", problems, details)
        return

    pressed = page.eval("window.__rc.autorotPressed()")
    if pressed != "true":
        problems.append("after switching on, aria-pressed=%r, expected 'true'"
                        % pressed)

    start = dots(page)
    time.sleep(HOLD_SECONDS)
    moved = dots(page)
    if moved == start:
        problems.append("auto-rotate is ON but the dots did not move over "
                        "%.1fs (%s)" % (HOLD_SECONDS, list(start)))
    else:
        details.append("ON: dots moved within %.1fs (%s → %s)"
                       % (HOLD_SECONDS, list(start), list(moved)))

    page.eval("window.__rc.autorot()")
    pressed = page.eval("window.__rc.autorotPressed()")
    if pressed != "false":
        problems.append("after switching off, aria-pressed=%r, expected 'false'"
                        % pressed)

    # Reset before measuring stillness, and here is why. The controls damp,
    # so switching auto-rotate off leaves a tail that decays geometrically —
    # it converges on stopped without ever arriving, and a residual well under
    # a pixel can still tip a rounded coordinate over minutes. Waiting it out
    # is a race this check would lose intermittently (it did, before this line
    # existed). Reset is the app's own way of putting the camera at rest: it
    # suspends damping and zeroes the accumulated delta outright.
    #
    # It does not soften the check. If the toggle had NOT actually stopped the
    # rotation, the controls would start driving the camera again on the very
    # next frame after the reset, and the hold below would catch it.
    reset_view(page)
    stopped = settle(page)
    time.sleep(HOLD_SECONDS)
    held = dots(page)
    if held != stopped:
        problems.append("auto-rotate is OFF but the camera kept turning over "
                        "%.1fs after a Reset: %s → %s"
                        % (HOLD_SECONDS, list(stopped), list(held)))
    else:
        details.append("OFF: dots held still for %.1fs from a reset view (%s)"
                       % (HOLD_SECONDS, ", ".join(held)))

    report.check(4, "auto-rotate", problems, details)


def check_tiers(page, report, shot_a, shot_c):
    """5. Live tier change, no remount."""
    problems, details = [], []

    if not page.eval("window.__rc.stampCanvas()"):
        problems.append("no <canvas> to stamp — cannot tell a retune from a "
                        "remount")
        report.check(5, "live tier change, no remount", problems, details)
        return

    for word, want in (("High", "B"), ("Balanced", "C"), ("Ultra", "A")):
        fault = set_quality(page, word)
        if fault:
            problems.append("%s: %s" % (word, fault))
            continue
        tier = page.eval("window.__rc.ds('tier')")
        probe = page.eval("window.__rc.canvasProbe()")
        canvases = page.eval("window.__rc.n('canvas')")
        if tier != want:
            problems.append("%s selected but the stage reports tier=%r, "
                            "expected %r" % (word, tier, want))
        if probe != "1":
            problems.append("%s remounted the canvas — the probe attribute is "
                            "%r, so this is a different element. A tier is a "
                            "retune, not a rebuild." % (word, probe))
        if canvases != 1:
            problems.append("%s left %d canvases on the page, expected 1"
                            % (word, canvases))
        details.append("%-8s → tier %s, same canvas (probe=%r), %d canvas"
                       % (word, tier, probe, canvases))

    # ── and the tiers must actually LOOK different ───────────────────────
    # Screenshots last, and only last: page.screenshot() overrides device
    # metrics and does not put the viewport back exactly, which would move
    # the stage and every coordinate above it.
    # Reset first: a camera still coasting on its damping tail would move the
    # specimen between the two captures and manufacture a byte difference out
    # of nothing, which is the one way this comparison could pass vacuously.
    # The dot coordinates either side of the pair are recorded and compared
    # below so that guard is asserted, not assumed.
    reset_view(page)
    settle(page)

    fault = set_quality(page, "Ultra")
    if fault:
        problems.append("tier A for the screenshot: %s" % fault)
    before = dots(page)
    page.screenshot(shot_a, width=VIEWPORT[0], height=VIEWPORT[1], full_page=False)
    page.set_viewport(*VIEWPORT)

    fault = set_quality(page, "Balanced")
    if fault:
        problems.append("tier C for the screenshot: %s" % fault)
    page.screenshot(shot_c, width=VIEWPORT[0], height=VIEWPORT[1], full_page=False)
    page.set_viewport(*VIEWPORT)
    after = dots(page)

    if before != after:
        problems.append("the camera moved between the two tier screenshots "
                        "(%s → %s) — any byte difference between them would "
                        "prove nothing" % (list(before), list(after)))

    with open(shot_a, "rb") as fh:
        a = fh.read()
    with open(shot_c, "rb") as fh:
        c = fh.read()
    if a == c:
        problems.append("the tier A and tier C screenshots are byte-identical "
                        "— the tier is being reported but not rendered")
    else:
        details.append("tier A (%d bytes) and tier C (%d bytes) PNGs differ, "
                       "from a camera that did not move between them (%s)"
                       % (len(a), len(c), ", ".join(after)))
    details.append("byte-difference is a WEAK check: it proves the two tiers "
                   "are not the same picture, not that either is the right "
                   "one. It is non-vacuous — a tier that only changed a data "
                   "attribute would produce identical bytes and fail here.")

    report.check(5, "live tier change, no remount", problems, details)


def check_parts(page, report, default_view):
    """7. Isolate and layers take real geometry off the stage (MRB-188).

    The failure this is written against is a control that steps a counter
    while the picture stays the same. So every assertion below is about
    something OUTSIDE the tool's own bookkeeping: which hotspot dots the shell
    is drawing, which is downstream of the renderer's occlusion test and of
    part visibility, and never of the step number.

    Occlusion is recomputed against whatever is still drawn (project.ts
    consults isShown precisely so a part the tool switched off stops hiding
    what is behind it), so taking geometry off the stage MUST change which
    dots are visible. That is the line a counter cannot fake, and it holds
    whatever shape the specimen is — see the note at the layers assertion for
    what it replaced and why the old form belonged to the fixture.

    `default_view` is the dot set the default view drew, measured once after
    check 1. It is used here only as a precondition and as the thing the tools
    must restore; it replaces a hard "one dot per hotspot in the record",
    which was the fixture's arithmetic (see check 2).
    """
    problems, details = [], []

    whole = page.eval("window.__rc.partsShown()")
    if whole is None:
        problems.append("the stage does not report how many parts are drawn — "
                        "cannot tell a peel from a no-op")
        report.check(7, "isolate and layers", problems, details)
        return
    if whole < 2:
        problems.append(
            "the loaded specimen declares %d part(s), so neither tool has "
            "anything to work on. The generated test specimen declares five; "
            "an asset with one merged form would correctly make both tools "
            "inert, and this check would then be measuring nothing." % whole)
        report.check(7, "isolate and layers", problems, details)
        return
    details.append("the asset declares %d drawable part(s)" % whole)

    at_start = settle(page)
    if ids_of(at_start) != ids_of(default_view):
        problems.append("not at the default view before the test: dots %s, "
                        "expected %s"
                        % (sorted(ids_of(at_start)), sorted(ids_of(default_view))))

    # ── isolate: step through every declared part and back ────────────────
    seen_labels, dots_per_step, shown_per_step = [], [], []
    for step in range(whole):
        if not page.eval("window.__rc.rail('Isolate')"):
            problems.append("no Isolate button on the rail")
            report.check(7, "isolate and layers", problems, details)
            return
        time.sleep(0.35)
        seen_labels.append(page.eval("window.__rc.ds('isolate')"))
        shown_per_step.append(page.eval("window.__rc.partsShown()"))
        dots_per_step.append(len(dots(page)))

    if shown_per_step != [1] * whole:
        problems.append("isolate drew %s part(s) across its %d steps, expected "
                        "exactly one at each — a step that changes the counter "
                        "and not the picture looks like this"
                        % (shown_per_step, whole))
    if len(set(seen_labels)) != whole:
        problems.append("isolate reported %r across %d steps — each step "
                        "should name a different declared part"
                        % (seen_labels, whole))
    if any(label in (None, "off", "") for label in seen_labels):
        problems.append("isolate reported no part name at one of its steps: %r"
                        % (seen_labels,))
    if len(set(dots_per_step)) < 2:
        # The premise here used to be the fixture's: "every stand-in anchor
        # sits on the outer shell, so isolating anything else must take its
        # dots with it". True of five concentric parts with raycast anchors,
        # meaningless on twelve authored structures standing side by side.
        # The assertion did not change and did not need to — occlusion is
        # recomputed against whatever is still drawn, so drawing ONE structure
        # at a time cannot leave the hotspot layer identical at every step.
        problems.append(
            "the hotspot layer did not change across isolate's %d steps "
            "(%s dot(s) each time). Occlusion is recomputed against whatever "
            "is still drawn, so stepping through the parts one at a time must "
            "change which dots are visible — this is the assertion a counter "
            "cannot fake." % (whole, dots_per_step))
    details.append("isolate stepped through %s" % ", ".join(map(repr, seen_labels)))
    details.append("parts drawn per step: %s · dots per step: %s"
                   % (shown_per_step, dots_per_step))

    page.eval("window.__rc.rail('Isolate')")
    time.sleep(0.35)
    back = page.eval("window.__rc.partsShown()")
    if back != whole:
        problems.append("one step past the last part left %d part(s) drawn, "
                        "expected the whole specimen (%d) — isolate has no way "
                        "home" % (back, whole))
    if page.eval("window.__rc.ds('isolate')") != "off":
        problems.append("isolate still reports a part after returning to the "
                        "whole specimen")
    else:
        details.append("one step past the last part returns the whole specimen")

    # ── layers: peel the outer level ──────────────────────────────────────
    restored = settle(page)
    if ids_of(restored) != ids_of(default_view):
        problems.append("the dots did not come back with the whole specimen: "
                        "%s, expected %s"
                        % (sorted(ids_of(restored)), sorted(ids_of(default_view))))

    if not page.eval("window.__rc.rail('Layers')"):
        problems.append("no Layers button on the rail")
        report.check(7, "isolate and layers", problems, details)
        return
    time.sleep(0.35)
    peeled_parts = page.eval("window.__rc.partsShown()")
    peeled_layer = page.eval("window.__rc.ds('layer')")
    peeled_dot_set = dots(page)
    peeled_dots = len(peeled_dot_set)
    if peeled_parts is None or peeled_parts >= whole:
        problems.append("Layers left %r of %d part(s) drawn — nothing was "
                        "peeled" % (peeled_parts, whole))
    if peeled_layer in (None, "off"):
        problems.append("Layers reports %r — the tool did not engage"
                        % peeled_layer)
    # The assertion is that the HOTSPOT LAYER MOVED, not that it shrank.
    #
    # It used to demand a decrease, on the premise that "every anchor sits on
    # the outer shell, so removing that layer must remove them". That premise
    # belonged to the generated fixture — concentric shells, with stand-in
    # anchors placed by a raycast from outside that always stopped on the
    # outermost surface. The acquired heart is not concentric: nine of its
    # twelve parts are at depth 0, side by side, and its anchors are authored.
    # Peeling the outer level there UNCOVERS the right ventricle and the two
    # atrioventricular valves, so more dots become visible, not fewer — which
    # is MRB-188's stated design (project.ts consults isShown precisely so a
    # part the tool switched off stops occluding what is behind it), not a
    # regression.
    #
    # What survives fixture-independently is the thing the check exists for: a
    # control that ticks a counter while the picture stays the same. Occlusion
    # is recomputed against the reduced geometry, so the set of visible dots
    # MUST differ after a peel. That a counter cannot fake either.
    if peeled_dot_set == restored:
        problems.append(
            "peeling the outer layer left the hotspot layer identical (%d "
            "dot(s) at the same places). Occlusion is recomputed against what "
            "is still drawn, so a real peel must change which dots are "
            "visible — this is what a counter cannot fake."
            % peeled_dots)
    details.append("layers: %r, %s of %d part(s) drawn, %d dot(s) (was %d)"
                   % (peeled_layer, peeled_parts, whole, peeled_dots,
                      len(restored)))

    # ── reset puts the form back whole ────────────────────────────────────
    reset_view(page)
    after_reset = settle(page)
    if page.eval("window.__rc.partsShown()") != whole:
        problems.append("Reset left the specimen taken apart — a half-restored "
                        "view reads as a broken control")
    if ids_of(after_reset) != ids_of(default_view):
        problems.append("Reset brought back dots %s, expected the default "
                        "view's %s"
                        % (sorted(ids_of(after_reset)), sorted(ids_of(default_view))))
    else:
        details.append("Reset restores the whole specimen and the default "
                       "view's %d dot(s)" % len(after_reset))

    report.check(7, "isolate and layers (MRB-188)", problems, details)


# ── reading pixels back, for the cap ─────────────────────────────────────
#
# Checks 1–7 all read the DOM. The capped cut cannot be: whether the cut face
# is solid material or a hole through to the room is a question about PIXELS,
# and a renderer that clipped without capping would satisfy every attribute
# and every dot count in this file.
#
# So check 8 screenshots the stage and looks at it. The decoder below is
# stdlib zlib plus PNG's five filter types — Chrome returns 8-bit RGB(A) and
# nothing else, so that is all it handles, and it refuses anything it does not
# recognise rather than guessing.


def read_png(path):
    """(width, height, rows) where each row is a bytes of RGB triples."""
    import struct
    import zlib

    with open(path, "rb") as fh:
        data = fh.read()
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("not a PNG")

    pos, width, height, depth, colour = 8, 0, 0, 0, 0
    idat = bytearray()
    while pos < len(data):
        (length,) = struct.unpack(">I", data[pos:pos + 4])
        kind = data[pos + 4:pos + 8]
        body = data[pos + 8:pos + 8 + length]
        pos += 12 + length
        if kind == b"IHDR":
            width, height, depth, colour = struct.unpack(">IIBB", body[:10])
        elif kind == b"IDAT":
            idat += body
        elif kind == b"IEND":
            break

    if depth != 8 or colour not in (2, 6):
        raise ValueError("unsupported PNG: depth=%d colour=%d" % (depth, colour))
    channels = 3 if colour == 2 else 4

    raw = zlib.decompress(bytes(idat))
    stride = width * channels
    rows, previous = [], bytearray(stride)
    at = 0
    for _ in range(height):
        filt = raw[at]
        line = bytearray(raw[at + 1:at + 1 + stride])
        at += 1 + stride
        for i in range(stride):
            a = line[i - channels] if i >= channels else 0
            b = previous[i]
            c = previous[i - channels] if i >= channels else 0
            if filt == 0:
                pass
            elif filt == 1:
                line[i] = (line[i] + a) & 0xFF
            elif filt == 2:
                line[i] = (line[i] + b) & 0xFF
            elif filt == 3:
                line[i] = (line[i] + (a + b) // 2) & 0xFF
            elif filt == 4:
                p = a + b - c
                pa, pb, pc = abs(p - a), abs(p - b), abs(p - c)
                pred = a if (pa <= pb and pa <= pc) else (b if pb <= pc else c)
                line[i] = (line[i] + pred) & 0xFF
            else:
                raise ValueError("unknown PNG filter %d" % filt)
        previous = line
        if channels == 3:
            rows.append(bytes(line))
        else:
            rows.append(bytes(b for i in range(0, stride, 4) for b in line[i:i + 3]))
    return width, height, rows


# The colour injected behind the transparent canvas. Nothing in the palette is
# within a hundred of it on any channel, so "did the room show through" is a
# question with an exact answer rather than a threshold.
VOID_RGB = (255, 0, 255)


def _pixels(rows, rect, step=2):
    """Sample RGB triples inside a rect, as a dict of (x, y) → (r, g, b)."""
    out = {}
    x0, y0 = int(rect["x"]), int(rect["y"])
    x1 = min(int(rect["x"] + rect["w"]), len(rows[0]) // 3)
    y1 = min(int(rect["y"] + rect["h"]), len(rows))
    for y in range(max(y0, 0), y1, step):
        row = rows[y]
        for x in range(max(x0, 0), x1, step):
            out[(x, y)] = (row[3 * x], row[3 * x + 1], row[3 * x + 2])
    return out


def _is_void(rgb):
    """The magenta backdrop, recognised by its HUE rather than its exact value.

    This used to ask for each channel within 40 levels of `VOID_RGB`, which is
    a fine test of a colour that arrives unmodified and a poor one of a colour
    that does not. Tier A renders through a post-processing composer and lands
    the backdrop at (215, 0, 215) — forty levels off on red and blue, exactly
    at the old test's boundary, so roughly half of tier A's backdrop counted as
    SPECIMEN. Nothing in the old check read it as a cap (magenta fails a
    red-dominant test on its blue channel), so it inflated the pixel counts the
    thresholds are taken as fractions of and never showed as a failure. It
    would have poisoned a luminance classifier outright, which is how it was
    found.

    Magenta is the one thing on the stage where red and blue are high, close to
    each other, and green is a fraction of both. Tissue (192, 170, 158) fails on
    red-against-blue; the cut wall and the cavity fail on green.
    """
    r, g, b = rgb
    return r > 90 and b > 90 and abs(r - b) < 26 and g < 0.45 * min(r, b)


# How far apart two renders of the same geometry may sit and still count as
# the same picture. Tier A composites a continuously re-integrated contact
# shadow, which lands a channel or two apart between captures — measured at
# ±1 on a handful of shadow pixels. Every difference this check cares about is
# a change of material: cap orange against neutral surface, or surface against
# backdrop, both of which are tens of levels apart on every channel. Comparing
# exactly would be measuring the shadow's dither, not the geometry.
SAME_TOLERANCE = 8


def _differs(a, b):
    if a is None or b is None:
        return True
    return any(abs(a[i] - b[i]) > SAME_TOLERANCE for i in range(3))


# ── the cut-face classifier ──────────────────────────────────────────────────
#
# THE OLD ONE'S PREMISE EXPIRED, AND THIS IS THE REPLACEMENT (MRB-189, Aug 13).
#
# Until Design authored the cross-section treatment, the cap was drawn in the
# accent family — `#A93411` outer, `#E4572E` inside it — so a cut-face pixel
# could be found by asking whether it was saturated, red-dominant and warmer in
# green than in blue, with an HSV saturation floor of 0.45 against a specimen
# surface measuring 0.18. That was a sound classifier for an orange cap.
#
# The cap is no longer orange. §08 takes the accent off the tissue entirely:
# the cut wall is `#F0E9DC` and the cavity `#141109`, the extremes of the frame.
# Measured, the wall is 0.08 saturation — it would not have been counted as cut
# face AT ALL — and the cavity is 0.55, which passes the old floor but only
# incidentally, because a near-black warm value is arithmetically "saturated"
# rather than because saturation means anything about it. The old gate would
# have failed on correct output. That is a premise expiring, not a defect in
# the design or in the gate.
#
# WHAT IT CLASSIFIES ON NOW: the two properties Design named as load-bearing.
#
#   FLAT. "The cut face is flat and unshaded while the exterior keeps its
#   gradient. That alone says cut before any colour is read, and it holds in
#   greyscale." A flat unshaded fill puts thousands of pixels on exactly one
#   value; a shaded surface cannot, because shading is what a gradient is. So a
#   cut-face colour is one held by a large share of the frame at once.
#
#   EXTREME. "The two values are the extremes of the frame, not neighbours in a
#   family: lightest thing on the stage against darkest." So a cut-face colour
#   also has to sit a long way in luminance from the specimen's own mid-tone,
#   which is measured in the same frame rather than assumed.
#
# BOTH conditions are needed, and the reason is Tier A. Tier A alone renders
# with an environment map through a composer, and its specular highlights on
# the specimen's own surface reach luminance 0.91 — BRIGHTER than the cut wall's
# 0.82. A luminance test on its own would count tier A's highlights as cut face
# with no cut engaged, and fail the baseline assertion below on a correct
# render. Flatness is what separates them there: the wall holds 6.2k pixels on
# one exact value, and the busiest single value anywhere on the lit surface
# holds 148. The gap is fortyfold, which is why this classifier, like the one it
# replaces, does not need to be clever.
#
# Deliberately NOT an exact match against `#F0E9DC` and `#141109`, even though
# both now arrive on the glass unmodified (`toneMapped: false`, and measured
# identical at all three tiers). An exact match would assert the colour rather
# than the cut, would break on any future compositing pass, and would make this
# check the third place the palette is pinned. The values themselves are
# asserted in `tests/gates/section.test.ts` and in `3d_parity.py`; this check
# asserts that a flat face at a luminance extreme exists where a cut is, and
# does not where one is not.

#: A flat population is an exact colour held by at least this share of the
#: sampled specimen pixels. Measured on the heart at all three tiers: the cut
#: wall lands 6239–6332 of ~8.8k (71%), the busiest value on the lit surface
#: lands 148 (1.7%). 3% sits an order of magnitude clear of both.
CUT_FLAT_SHARE = 0.03

#: How far from the specimen's own median luminance a flat population must sit
#: before it counts as an extreme. Measured: median 0.50–0.58 across tiers, cut
#: wall 0.8197 at every tier (Δ 0.24–0.32), cavity 0.0052 (Δ 0.50–0.57).
CUT_SEPARATION = 0.20


def _luma(rgb):
    """Relative luminance, WCAG 2.x — the same arithmetic `contrast.test.ts`
    uses, so "light" and "dark" mean here what they mean there."""
    channels = []
    for value in rgb:
        v = value / 255.0
        channels.append(v / 12.92 if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4)
    return 0.2126 * channels[0] + 0.7152 * channels[1] + 0.0722 * channels[2]


def _median_luma(pixels, keys):
    values = sorted(_luma(pixels[p]) for p in keys)
    return values[len(values) // 2] if values else 0.0


def _flat_faces(pixels, keys, mid):
    """The flat populations at a luminance extreme, as {rgb: count}.

    A flat population is one exact colour held by CUT_FLAT_SHARE of the sampled
    specimen; an extreme one sits CUT_SEPARATION or further from `mid`. Returns
    every flat population it found either way — the ones that are not extreme
    are reported, because a flat mid-tone population is the shape a broken
    premise would take.
    """
    counts = {}
    for point in keys:
        rgb = pixels[point]
        counts[rgb] = counts.get(rgb, 0) + 1
    floor = max(int(len(keys) * CUT_FLAT_SHARE), 1)
    flat = {rgb: n for rgb, n in counts.items() if n >= floor}
    extreme = {rgb: n for rgb, n in flat.items()
               if abs(_luma(rgb) - mid) >= CUT_SEPARATION}
    return flat, extreme


def _describe_pops(pops, mid):
    """Flat populations as `#RRGGBB×N L=0.82 (Δ0.24)`, biggest first.

    Reported at every tier whether or not anything failed. The old check
    reported a saturation figure it had measured once and written down; this
    reports what it actually found this run, so the number a future premise
    expires against is on the screen rather than in a comment.
    """
    return " ".join(
        "#%02X%02X%02X×%d L=%.3f (Δ%.2f)"
        % (rgb[0], rgb[1], rgb[2], n, _luma(rgb), abs(_luma(rgb) - mid))
        for rgb, n in sorted(pops.items(), key=lambda kv: -kv[1]))


def _interior_holes(rows, rect, step=2):
    """Background pixels enclosed by drawn pixels on the same scanline.

    A cap that is torn, too small, or z-fighting shows the room in the MIDDLE
    of the specimen. A cut that legitimately narrows the silhouette — the near
    half bulged further than the far half, which a lumpy specimen does all the
    time — shows it at the EDGES. Only the first is a defect, so only the first
    is counted.
    """
    holes = 0
    x0 = max(int(rect["x"]), 0)
    x1 = min(int(rect["x"] + rect["w"]), len(rows[0]) // 3)
    y0 = max(int(rect["y"]), 0)
    y1 = min(int(rect["y"] + rect["h"]), len(rows))
    for y in range(y0, y1, step):
        row = rows[y]
        drawn = [x for x in range(x0, x1, step)
                 if not _is_void((row[3 * x], row[3 * x + 1], row[3 * x + 2]))]
        if len(drawn) < 2:
            continue
        for x in range(drawn[0], drawn[-1], step):
            if _is_void((row[3 * x], row[3 * x + 1], row[3 * x + 2])):
                holes += 1
    return holes


def check_section(page, report, shots):
    """8. The cross-section cuts, and the cut is capped (MRB-189).

    Three claims, none of which can be read off an attribute the renderer
    wrote about itself:

      * THE CAP IS DRAWN. The cut face is flat and unshaded where the exterior
        is shaded, and its two values sit at the extremes of the frame — so
        counting pixels that belong to a large flat population at a luminance
        extreme from the specimen's own mid-tone answers "is there a cut face"
        directly. See the classifier above for why it is both of those and not
        either alone, and for the saturation-shaped premise it replaced.
        Asserted in both directions: many with the cut engaged, essentially
        none without it — and the mid-tone the extremes are measured against is
        measured in the same frame, never assumed. The hotspot dots are not
        part of the render and are hidden for every capture here — see `shoot`,
        which is where that was got wrong and put right.
      * THE CAP HAS NO HOLE IN IT. The canvas is transparent — Design's room
        is a CSS gradient behind it — so the stage background is swapped for
        magenta and any background pixel ENCLOSED by specimen pixels on its
        own scanline is counted. Enclosed, not merely present: a cut
        legitimately narrows the silhouette wherever the near half bulged
        further than the far half, and an earlier version of this check called
        that a defect. It is not one; a hole in the middle of the cut face is.
      * INTERIOR GEOMETRY BECOMES VISIBLE. Occlusion consults the clipping
        plane (project.ts), so geometry the cut took away stops hiding what
        was behind it — and engaging the cut must therefore change WHICH
        hotspot dots are visible. That holds whatever shape the specimen is.
        It replaces an earlier version which isolated the outermost part and
        argued it must draw the same picture as the whole specimen "because
        everything else is inside it": true of the generated fixture, false
        of the acquired heart, whose nine depth-0 parts sit side by side.
        See claim (d) below for the full note.

    All three are repeated at every tier, because the Tier A path renders
    through a post-processing composer with a render target of its own, and a
    target without a stencil buffer would silently un-cap the cut on the most
    capable hardware in the fleet.

    WHAT THIS CANNOT SETTLE, tried and stated rather than assumed: whether the
    cap covers EVERY pixel of the cut. Shrinking the cap quad to a quarter of
    its size was measured here and still passes — a large cut face remains,
    and where the cap is missing you see the inside of the far wall rather
    than the backdrop, so no pixel count separates the two without a threshold
    fitted to this one specimen. Coverage is arithmetic over two functions and
    eight box corners, so it is asserted in `tests/gates/section.test.ts`
    instead, where the same mutation fails three assertions outright.
    """
    problems, details = [], []

    rect = page.eval("window.__rc.rect('.stage')")
    if not rect:
        problems.append("no .stage to measure")
        report.check(8, "cross-section is capped", problems, details)
        return
    # Sample the specimen's half of the stage only. The left column is the
    # rail and the bottom strip is the hint line, the section slider and the
    # quality chip — all of which legitimately change when a tool is pressed,
    # and all of which would then show up as "the picture changed" in a
    # comparison that is supposed to be about geometry.
    inner = {"x": rect["x"] + 96, "y": rect["y"] + 8,
             "w": rect["w"] - 108, "h": rect["h"] - 78}

    page.eval("window.__rc.voidBackdrop()")

    def shoot(name):
        """Capture the STAGE, which means the canvas and not the shell on top
        of it.

        The hotspot layer is hidden for the capture and restored the instant
        it is taken. It is not part of the render, and every question this
        check asks is about canvas pixels — but the dots are DOM elements
        filled with `#E4572E`, which is the accent family the cap is drawn in,
        so `_is_cut_face` counted them as cut face. On the two-hotspot fixture
        that was noise beneath every threshold. The acquired heart's fourteen
        measured 593 cut-face pixels with NO cut engaged, IDENTICALLY at all
        three tiers while the render itself differed — the tell that the count
        was never coming from the canvas at all. The thresholds are not the
        problem and are untouched: a real cut still lands 6255–6267 against
        them. The instrument was reading the wrong surface.

        Hidden, not removed: the elements stay in the DOM at their real
        positions, so `dots()` either side of this call still sees exactly
        which hotspots the renderer holds visible — which claim (d) depends on.
        """
        path = os.path.join(shots, name + ".png")
        page.eval("window.__rc.hideDots()")
        time.sleep(DOT_HIDE_SETTLE)
        page.screenshot(path, width=VIEWPORT[0], height=VIEWPORT[1], full_page=False)
        page.set_viewport(*VIEWPORT)
        page.eval("window.__rc.showDots()")
        rows = read_png(path)[2]
        return _pixels(rows, inner), rows

    for word, tier in (("Ultra", "A"), ("High", "B"), ("Balanced", "C")):
        fault = set_quality(page, word)
        if fault:
            problems.append("tier %s: %s" % (tier, fault))
            continue

        # ── whole specimen, no cut ────────────────────────────────────────
        reset_view(page)
        settle(page)
        whole, whole_rows = shoot("t%s-whole" % tier)
        whole_dots = dots(page)
        drawn = {p for p, rgb in whole.items() if not _is_void(rgb)}
        # The specimen's OWN mid-tone, measured in this frame at this tier with
        # no cut engaged. Everything the classifier calls extreme is extreme
        # relative to this, not to a number written down in this file — which
        # is what makes the same thresholds right on a tier that renders the
        # surface half a stop brighter, and what makes a specimen the premise
        # does not hold for fail loudly instead of quietly.
        mid = _median_luma(whole, drawn)
        flat_before, extreme_before = _flat_faces(whole, drawn, mid)
        face_before = sum(extreme_before.values())

        # The instrument's own noise floor: the SAME state, photographed
        # twice, WITH THE SAME GAP between captures that every comparison
        # below has.
        #
        # The gap is the load-bearing part. Tier A composites a contact shadow
        # that re-integrates every frame, and page.screenshot() overrides
        # device metrics — so the shadow is still converging for a moment
        # afterwards, and a floor measured back-to-back reads 0 while the real
        # variation between two captures a beat apart reached 432 across the
        # runs of this build. A gate calibrated against the back-to-back
        # number would have been green tonight and red next week for no
        # change in the code, which is worse than no gate.
        time.sleep(SETTLE_GAP)
        again, _ = shoot("t%s-again" % tier)
        noise = sum(1 for p in whole if _differs(whole[p], again.get(p)))
        if len(drawn) < 500:
            problems.append(
                "tier %s: only %d specimen pixel(s) on the stage before the cut "
                "— the backdrop probe or the render is broken, and everything "
                "below would be measuring nothing" % (tier, len(drawn)))
            continue

        # ── shell alone, no cut ───────────────────────────────────────────
        whole_parts = page.eval("window.__rc.partsShown()") or 1
        page.eval("window.__rc.rail('Isolate')")
        time.sleep(SETTLE_GAP)
        shell, _ = shoot("t%s-shell" % tier)
        same_before = sum(1 for p in whole if _differs(whole[p], shell.get(p)))

        # ── shell alone, cut ──────────────────────────────────────────────
        page.eval("window.__rc.rail('Cross-section')")
        time.sleep(0.6)
        shell_cut, _ = shoot("t%s-shell-cut" % tier)

        # ── whole specimen, cut ───────────────────────────────────────────
        #
        # Step round until isolate reports 'off' rather than clicking a fixed
        # five times. Five was the generated fixture's part count; the heart
        # declares twelve, so the fixed count stopped three parts short of
        # home and every measurement after it was taken of a single isolated
        # structure. Bounded by the part count the stage itself reports, plus
        # one for the step back to whole, so a control that never returns
        # fails here instead of spinning.
        for _ in range(whole_parts + 1):
            page.eval("window.__rc.rail('Isolate')")
            if page.eval("window.__rc.ds('isolate')") == "off":
                break
        time.sleep(0.6)
        if page.eval("window.__rc.ds('isolate')") != "off":
            problems.append("tier %s: could not get back to the whole specimen"
                            % tier)
        cut, cut_rows = shoot("t%s-cut" % tier)
        cut_dots = dots(page)

        cut_drawn = {p for p, rgb in cut.items() if not _is_void(rgb)}
        flat_after, extreme_after = _flat_faces(cut, cut_drawn, mid)
        face_after = sum(extreme_after.values())
        wall = {rgb: n for rgb, n in extreme_after.items() if _luma(rgb) > mid}
        cavity = {rgb: n for rgb, n in extreme_after.items() if _luma(rgb) < mid}
        holes_before = _interior_holes(whole_rows, inner)
        holes_after = _interior_holes(cut_rows, inner)
        changed = sum(1 for p in drawn if _differs(whole[p], cut.get(p)))
        same_after = sum(1 for p in cut if _differs(cut[p], shell_cut.get(p)))

        # (a) a cut face exists, and only once there is a cut
        if face_before > len(drawn) * 0.02:
            problems.append(
                "tier %s: %d cut-face pixel(s) with NO cut engaged (%s) — the "
                "specimen\'s own surface is producing a flat population at a "
                "luminance extreme, so the count below proves nothing"
                % (tier, face_before, _describe_pops(extreme_before, mid)))
        if face_after < len(drawn) * 0.10:
            problems.append(
                "tier %s: %d of %d specimen pixel(s) are cut face — the plane "
                "clipped the geometry and left the cut open, or the cap is "
                "being shaded rather than drawn flat"
                % (tier, face_after, len(drawn)))
        # The cut WALL specifically. A plane through solid material must
        # produce the light extreme; the dark one only appears where the plane
        # also crossed a cavity, which is a property of where the student left
        # the slider and of the specimen, not of the renderer. So the wall is
        # asserted and the cavity is reported — its value and its contrast
        # against the wall are pinned in `tests/gates/section.test.ts`, where
        # they can be asserted without depending on the geometry a plane at
        # 50% happens to meet.
        if not wall:
            problems.append(
                "tier %s: no flat cut-face population above the specimen\'s own "
                "mid-tone (%.3f) — a plane through solid material draws a cut "
                "WALL, and the light extreme is the one value that cannot be "
                "absent from a capped cut" % (tier, mid))

        # (b) and no hole in it
        if holes_after > max(holes_before * 2, len(drawn) * 0.005):
            problems.append(
                "tier %s: %d background pixel(s) enclosed by the specimen after "
                "the cut (%d before) — the cap is torn, too small, or losing a "
                "depth fight" % (tier, holes_after, holes_before))

        # (c) the cut has to change the picture at all
        if changed < len(drawn) * 0.10:
            problems.append(
                "tier %s: engaging the cut changed %d of %d specimen pixel(s) "
                "— the plane is not cutting anything"
                % (tier, changed, len(drawn)))

        # (d) the cut exposed geometry that was hidden before it
        #
        # This claim used to be made by isolating the outermost part and
        # arguing that on a whole specimen that must draw the SAME picture as
        # drawing everything, "because everything else is inside it". That was
        # true of the generated fixture — one shell around three chambers and
        # a torus — and it is false of the acquired heart, where nine of the
        # twelve parts sit at depth 0 side by side. Isolating the first there
        # draws a right atrium alone, which legitimately differs from the
        # whole heart by thousands of pixels, so the old pair failed on a
        # correct renderer and a correct asset.
        #
        # The claim itself is still worth making; it needed a measurement that
        # assumes no nesting. project.ts consults the clipping plane when it
        # decides occlusion, precisely so geometry the cut took away stops
        # hiding what was behind it. So engaging the cut MUST change which
        # hotspot dots are visible, on any specimen of any shape. A cut that
        # drew a plane and reached nothing leaves that set exactly alone —
        # which is the same class of defect the old pair was written against,
        # caught without a premise about the asset.
        #
        # same_before / same_after are kept in the details line below as a
        # REPORT. They are informative on any specimen and assert nothing.
        if cut_dots == whole_dots:
            problems.append(
                "tier %s: the cut left the hotspot layer identical (%d dot(s) "
                "at the same places) — occlusion is recomputed against the "
                "clipping plane, so a cut that reaches real geometry must "
                "change which dots are visible" % (tier, len(cut_dots)))

        details.append(
            "tier %s: %d specimen px · own mid-tone %.3f · noise floor %d · "
            "cut face %d → %d · enclosed background %d → %d · cut changed %d "
            "(%.0f%%) · interior hidden before (%d px differ) → visible after "
            "(%d px differ)"
            % (tier, len(drawn), mid, noise, face_before, face_after,
               holes_before, holes_after, changed,
               100.0 * changed / max(len(drawn), 1), same_before, same_after))
        details.append(
            "        wall %s · cavity %s · flat populations before the cut: %s"
            % (_describe_pops(wall, mid) or "none",
               _describe_pops(cavity, mid) or "none (the plane met no cavity)",
               _describe_pops(flat_before, mid) or "none"))

        page.eval("window.__rc.rail('Cross-section')")
        time.sleep(0.3)

    page.eval("window.__rc.restoreBackdrop()")
    reset_view(page)
    settle(page)
    details.append("cut-face pixels are counted as flat populations (one exact "
                   "colour held by %.0f%%+ of the specimen, which a shaded "
                   "surface cannot produce) at a luminance extreme (%.2f or "
                   "further from the specimen's own median, measured in the "
                   "same frame). Not an exact colour match — the values are "
                   "pinned in section.test.ts and 3d_parity.py, and this check "
                   "asserts the cut rather than the palette. The count with no "
                   "cut engaged is asserted above rather than assumed."
                   % (CUT_FLAT_SHARE * 100, CUT_SEPARATION))

    report.check(8, "cross-section is capped, at every tier (MRB-189)",
                 problems, details)


TITLE_10 = "the round frames its target before asking (MRB-191)"


def structure_numerals():
    """{'01': 'Right atrium', …} — the glyph a dot wears, to what it is called.

    Stage.tsx numbers a dot `String(index + 1).padStart(2, '0')` over the
    specimen's OWN hotspot order, and pushes only the visible ones, so the
    glyph is a stable global index into content/heart.json rather than a
    position in whatever subset is on screen. Read here so the driver can name
    a structure it can see without clicking on it.
    """
    path = os.path.join(HERE, "3d-studio", "content", "heart.json")
    try:
        with open(path, encoding="utf-8") as fh:
            record = json.load(fh)
    except (OSError, ValueError):
        return {}
    return {str(i + 1).zfill(2): h.get("label")
            for i, h in enumerate(record.get("hotspots", []))}


def check_framing(page, report):
    """10. The round frames its target before asking (ruling on MRB-191).

    Stage 2 made occlusion honest, which is what makes the identify mode an
    assessment rather than a picture — and which creates this stage's problem.
    A target on the far side of the specimen is "highlighted" with NOTHING on
    screen: not a hard question, an unanswerable one, and indistinguishable
    from the app being broken.

    So this drives the worst case deliberately, and the worst case has to be
    ESTABLISHED rather than hoped for. A round opened from a view where the
    target already happened to be on screen proves nothing at all.

    TWO EARLIER FORMS OF THAT PRECONDITION, and why both are gone:

    The first turned the specimen roughly 180° and required that NO dot at all
    was left on the stage, on the strength of check 2's old claim that a half
    turn hides everything. True of the generated fixture, whose two anchors
    were both on the near side; false of the acquired heart, whose far side
    carries the left atrium and both pulmonary vessels.

    The second opened a round to learn which structure gets asked first, turned
    until THAT marker was off the stage, opened a SECOND round from there, and
    asserted the two rounds agreed on their first question — which they did,
    because a round was the whole eligible set in record order. MRB-191 then
    ruled a round to be six, SAMPLED, preferring structures not yet seen this
    session, so two consecutive rounds now deliberately do not agree. That form
    refused to run, and it refused correctly: it was reading a property of the
    old round-building, not a property of framing.

    WHAT IS MEASURED NOW uses one round and no cross-round assumption:

      1. In explore mode, at whatever view we are at, read the numeral on every
         dot on the stage. A numeral is an index into the specimen's own
         hotspot list (see structure_numerals), so this is a set of STRUCTURE
         NAMES — what the student can see from here, by name, without touching
         anything.
      2. Open a round. The retrieval room draws one dot, the target, wearing
         '?' rather than its numeral — deliberately, since what it is called is
         the question. Measure the marker: on the stage, inside it, 52px,
         pulsing.
      3. Give up on that question. Revealing is the one affordance that says
         out loud which structure was being asked about, and it happens AFTER
         the measurement, so it cannot influence it.
      4. The claim holds only if the revealed structure was not in the set from
         step 1: the round framed something that was not on screen when it
         opened.

    Identity is not carried across a mode switch, and deliberately so — the
    stage is a different width in the two rooms (`main--retrieve` gives 404px
    to the panel), so the same anchor projects to a different pixel and dots
    cannot be matched by position between them.

    If the sampler hands us a target that was already on screen, nothing is
    asserted: the specimen is turned a quarter and another round is drawn. Same
    shape as the old turn-until-hidden loop, but it now searches for an adverse
    ROUND rather than an adverse view of a fixed one.
    """
    problems, details = [], []
    names = structure_numerals()
    if not names:
        report.check(10, TITLE_10, ["HARNESS: could not read content/heart.json, "
                                    "so a dot's numeral cannot be turned into a "
                                    "structure name"], details)
        return

    def visible_structures():
        """The names of the structures whose dots are on the stage right now."""
        seen = set()
        for entry in dots(page):
            glyph = entry.split("@", 1)[0]
            if glyph in names:
                seen.add(names[glyph])
        return seen

    def leave():
        page.eval("window.__rc.leaveRetrieval()")
        time.sleep(0.3)

    def open_round(where):
        if not page.eval("window.__rc.enterRetrieval()"):
            problems.append("no Retrieve control in the header (%s)" % where)
            return False
        time.sleep(FRAME_MOVE)  # the framing move is animated: 620ms, eased
        settle(page)
        return True

    reset_view(page)
    settle(page)

    established = False
    for attempt in range(QUARTER_TURNS + 1):
        where = "attempt %d" % (attempt + 1)
        before = visible_structures()

        if not open_round(where):
            report.check(10, TITLE_10, problems, details)
            return

        marker = page.eval("window.__rc.target()")

        # Read the answer only after the marker has been measured.
        if not page.eval("window.__rc.reveal()"):
            problems.append(
                "no reveal control in the retrieval panel (%s) — the target's "
                "identity cannot be read, and without it the precondition "
                "cannot be established" % where)
            break
        time.sleep(0.4)
        asked = page.eval("window.__rc.revealedLabel()")
        leave()

        if not marker:
            problems.append(
                "the round opened with NO target dot on the stage%s. The "
                "student is being asked to name a structure that is not on "
                "screen — spec §6 says a structure is highlighted, and an "
                "invisible highlight is not a highlight."
                % (" (%r)" % asked if asked else ""))
            break

        if not asked:
            problems.append(
                "the round revealed no structure name, so there is nothing to "
                "establish a precondition about")
            break

        if asked in before:
            details.append(
                "%s: the round asked about %r, which was already on screen "
                "before it opened — nothing asserted, turning" % (where, asked))
            fault = drag_horizontal(page, px=QUARTER_PX)
            if fault:
                problems.append("HARNESS: " + fault)
                break
            settle(page)
            continue

        # ── adversity established: this round asked about something that was
        #    not on the stage a moment ago. NOW the claim is worth asserting.
        established = True
        details.append(
            "%s: %r was NOT on the stage before the round opened — %d other "
            "structure(s) were (%s) — and the round brought it into view. The "
            "precondition and the claim are about the same structure, in the "
            "same round." % (where, asked, len(before),
                             ", ".join(sorted(before)) or "none"))

        if not marker["inside"]:
            problems.append(
                "the target dot is outside the stage (%.0f, %.0f) — framed "
                "off the edge is the same as not framed"
                % (marker["x"], marker["y"]))
        if round(marker["w"]) != 52:
            problems.append("the target dot is %.0fpx, expected the 52px "
                            "marker §07 specifies" % marker["w"])
        if not marker["ping"]:
            problems.append("the target dot has no ring pulse (§02)")
        details.append("target: %.0fpx at (%.0f, %.0f), inside the stage=%s, "
                       "ping=%d"
                       % (marker["w"], marker["x"], marker["y"],
                          marker["inside"], marker["ping"]))
        break

    if not established and not problems:
        problems.append(
            "HARNESS: %d rounds were drawn and every one of them asked about a "
            "structure that was already on screen, so the framing move was "
            "never asked to do anything. Nothing is asserted."
            % (QUARTER_TURNS + 1))

    # Back out of the room so the checks after this one start where they expect.
    leave()
    page.eval("window.__rc.rail('Reset view')")
    time.sleep(0.5)

    report.check(10, TITLE_10, problems, details)


def three_chunks():
    """Every built JS chunk that actually contains Three.js.

    Found by reading the build rather than by trusting the chunk name, so a
    rollup config change that scattered three across three files could not
    quietly make check 9 vacuous.
    """
    assets = os.path.join(DIST, "assets")
    if not os.path.isdir(assets):
        return []
    marks = ("WebGLRenderer", "BufferGeometry")
    found = []
    for name in sorted(os.listdir(assets)):
        if not name.endswith(".js"):
            continue
        with open(os.path.join(assets, name), "r", encoding="utf-8",
                  errors="replace") as fh:
            text = fh.read()
        if all(mark in text for mark in marks):
            found.append(name)
    return found


def check_split(url, report):
    """9. A Tier D device never downloads Three.js (ruling on MRB-190).

    Stage 2 took the bundle to 1.15MB, nearly all of it Three, and every byte
    of it went to a device with no WebGL to render a flat diagram — the
    students on the worst hardware paying the largest download for code that
    cannot execute on their machine, usually on the worst connection too.

    Stage 5 put the mesh renderer behind a dynamic import. This is the claim
    that makes that worth doing, and it is asserted rather than assumed: a
    browser launched with WebGL genuinely off lands on Tier D, mounts the flat
    renderer, and its resource timeline must contain NO chunk carrying Three.

    The same run also checks the other half — that the split did not cost the
    capable devices anything — by confirming a WebGL browser DOES fetch it.
    """
    problems, details = [], []

    chunks = three_chunks()
    if not chunks:
        problems.append(
            "no built chunk contains Three.js at all — either the build is "
            "broken or this check is looking in the wrong place, and either "
            "way it would pass vacuously")
        report.check(9, "tier D never downloads Three", problems, details)
        return
    details.append("three lives in: %s" % ", ".join(chunks))

    def requested(extra_args):
        with cdp.Browser(extra_args=extra_args) as b:
            page = b.attach()
            page.set_viewport(*VIEWPORT)
            page.goto(url)
            inject(page)
            wait_state(page)
            # The prefetch is fired before React renders, but the response
            # still has to arrive before it shows in the timeline.
            time.sleep(2.5)
            tier = page.eval(
                "document.querySelector('.app').getAttribute('data-detected-tier')")
            renderer = page.eval("window.__rc.ds('renderer')")
            urls = page.eval(
                "performance.getEntriesByType('resource').map(function (e) "
                "{ return e.name })") or []
            return tier, renderer, [u for u in urls
                                    if any(c in u for c in chunks)]

    tier, renderer, got = requested(["--disable-webgl", "--disable-webgl2"])
    if tier != "D":
        problems.append(
            "HARNESS: WebGL was not actually disabled — the probe landed on "
            "tier %r, so this proves nothing about the Tier D route" % tier)
    if renderer != "flat":
        problems.append("tier D mounted renderer=%r, expected 'flat'" % renderer)
    if got:
        problems.append(
            "a Tier D load requested %d Three chunk(s): %s. The device cannot "
            "run a line of it." % (len(got), ", ".join(got)))
    details.append("tier D: renderer=%r, %d Three chunk request(s)"
                   % (renderer, len(got)))

    tier, renderer, got = requested(["--enable-unsafe-swiftshader"])
    if tier == "D":
        problems.append("HARNESS: the WebGL browser also landed on tier D")
    elif not got:
        problems.append(
            "a Tier %s load requested NO Three chunk — the mesh renderer "
            "cannot be running, so the split has broken the capable path "
            "rather than only the flat one" % tier)
    details.append("tier %s: renderer=%r, %d Three chunk request(s) — the "
                   "prefetch fires before React renders, so the split costs a "
                   "capable device no round-trip"
                   % (tier, renderer, len(got)))

    report.check(9, "a tier D load requests no Three chunk (MRB-190)",
                 problems, details)


def check_failure_route(url, report):
    """6. Failure is a route — driven against a build with the GLB removed."""
    problems, details = [], []

    with cdp.Browser(extra_args=["--enable-unsafe-swiftshader"]) as b:
        page = b.attach()
        page.set_viewport(*VIEWPORT)
        page.goto(url)
        inject(page)

        state = wait_state(page)
        # the shell swaps renderers in response to the failure, so the paper
        # stage's own mount/load follows the mesh renderer's rejection
        deadline = time.time() + 15.0
        renderer = None
        while time.time() < deadline:
            renderer = page.eval("window.__rc.ds('renderer')")
            if renderer == "flat":
                break
            time.sleep(0.2)

        detected = page.eval(
            "document.querySelector('.app').getAttribute('data-detected-tier')")
        if detected == "D":
            problems.append(
                "HARNESS: this browser has no WebGL either, so the flat stage "
                "proves nothing about the missing-GLB route")

        # Stage 5 (MRB-190) replaced the paper PLACEHOLDER with the real flat
        # renderer, so the name this asserts changed with it. The claim is the
        # same one: a mesh that will not load lands on the flat stage.
        if renderer != "flat":
            problems.append("stage reports renderer=%r, expected 'flat' — a "
                            "mesh that will not load must route to the flat "
                            "stage" % renderer)
        word = page.eval("window.__rc.text('.flatchip__word')")
        if (word or "").lower() != "flat diagram":
            problems.append("flat chip says %r, expected 'FLAT DIAGRAM'" % word)
        chips = page.eval("window.__rc.n('.chip')")
        if chips:
            problems.append("%d quality chip(s) on a stage with no renderer to "
                            "tune" % chips)

        body = page.eval("document.body.innerText") or ""
        shouted = [line.strip() for line in body.splitlines()
                   if re.search(r"error|failed|sorry", line, re.I)]
        if shouted:
            problems.append("the page apologises to the student: %r" % shouted)

        # Nothing may be THROWN on the way, either. The 404 for the absent
        # specimen is the point of the exercise and is expected; anything else
        # means the swap itself is faulting. This caught a real one: with the
        # React root mounted straight into the shell's container instead of
        # into a host of its own, the mesh renderer's teardown raced the flat
        # renderer's drawing and the page threw an uncaught NotFoundError from
        # removeChild — on the one code path whose entire job is to fail
        # gracefully. Silent to jsdom, loud here.
        expected_404 = re.compile(r"404|not found", re.I)
        thrown = [e for e in page.console_errors()
                  if "favicon" not in e.lower() and not expected_404.search(e)]
        if thrown:
            problems.append("the swap threw: %s"
                            % "; ".join(e.splitlines()[0][:160] for e in thrown))
        details.append("console: %d expected 404 line(s) for the absent "
                       "specimen, %d other entries"
                       % (len(page.console_errors()) - len(thrown), len(thrown)))

        # Observations, not claims: these lines print whether the check passed
        # or failed, so they say what was seen rather than what was wanted.
        details.append("settled on renderer=%r, state=%r — the mesh "
                       "renderer's rejection is observed as the SWAP, not as "
                       "a lingering failed state (the paper renderer that "
                       "replaces it reaches ready of its own accord)"
                       % (renderer, state))
        details.append("detected tier=%s — tier D here would mean the flat "
                       "stage proved nothing about the missing GLB" % detected)
        details.append("flat chip word=%r, quality chips=%d, apology lines=%d"
                       % (word, chips, len(shouted)))

    report.check(6, "failure is a route (missing GLB)", problems, details)


# ── frame timing, report only (deliberately unnumbered) ──────────────────


def _stats(samples):
    s = sorted(samples)
    n = len(s)
    p95 = s[min(n - 1, int(math.ceil(0.95 * n)) - 1)]
    return {
        "min": s[0],
        "median": s[n // 2] if n % 2 else (s[n // 2 - 1] + s[n // 2]) / 2.0,
        "p95": p95,
        "max": s[-1],
    }


def frame_timing(page):
    """Sample frame times at each tier with the scene genuinely animating.

    Auto-rotate is switched on first: an idle R3F scene renders on demand, so
    sampling a still stage would measure how fast Chrome does nothing.
    """
    rows = []
    if page.eval("window.__rc.autorotPressed()") != "true":
        page.eval("window.__rc.autorot()")
    for word, tier in (("Ultra", "A"), ("High", "B"), ("Balanced", "C")):
        fault = set_quality(page, word)
        if fault:
            rows.append((tier, None, fault))
            continue
        time.sleep(0.5)
        samples = page.eval("window.__rc.frames(%d)" % FRAME_SAMPLES, timeout=300)
        rows.append((tier, _stats(samples), None))
    page.eval("window.__rc.autorot()")
    return rows


def print_frame_timing(rows):
    bar = "  " + "─" * 70
    print()
    print(bar)
    print("  FRAME TIMING — REPORT ONLY. This can never fail the script.")
    print(bar)
    print("  These numbers come from SOFTWARE-RENDERED headless Chrome:")
    print("  SwiftShader on the CPU (--enable-unsafe-swiftshader), no GPU")
    print("  anywhere in the pipeline, on a machine no student owns.")
    print()
    print("  They are NOT evidence for or against spec §5's 60fps target at")
    print("  Tier A or its 30fps floor at Tier C. Do not quote them as such.")
    print("  Their only use is as a RELATIVE baseline: tier-to-tier ordering")
    print("  on one machine, and a before/after number for Stage 10's real-")
    print("  device test, which is where the spec's targets are actually")
    print("  answered.")
    print()
    print("    tier   samples      min    median       p95       max    fps*")
    for tier, st, fault in rows:
        if st is None:
            print("    %-6s not sampled — %s" % (tier, fault))
            continue
        fps = 1000.0 / st["median"] if st["median"] > 0 else float("inf")
        print("    %-6s %7d %8.1f  %8.1f  %8.1f  %8.1f  %6.1f"
              % (tier, FRAME_SAMPLES, st["min"], st["median"], st["p95"],
                 st["max"], fps))
    print("    (all times in ms; *fps implied by the median, software render)")
    print("    max is expected to dwarf p95: the first frames after a tier")
    print("    switch compile shaders and, at Tier A, generate the IBL.")
    print(bar)


# ── the driver ───────────────────────────────────────────────────────────


def serve_dist_as_3d(prefix, strip_glb=False):
    """Serve the built app under /3d/ so its absolute asset URLs resolve.

    The healthy build is symlinked (3d_parity.py's approach — nothing is
    copied, nothing can drift). The failure build is a real copy with EVERY
    .glb removed: the real dist/ is never touched.

    Every, not one named file. This used to delete `assets/_test-specimen.glb`
    by name, which was the only mesh in the build while nothing had been
    acquired. The heart's real mesh landing (MRB-187) broke that silently and
    in the worst possible way: `_test-specimen.glb` is still copied out of
    public/, so the guard below still found it and the deletion still
    "worked" — but the app had stopped asking for it and loaded heart.glb
    perfectly well, so the check that proves a missing mesh routes to the flat
    stage was quietly proving nothing at all. Removing whatever GLBs are there
    is the only version that cannot rot as specimens are acquired.

    Returns (url, cleanup).
    """
    root = tempfile.mkdtemp(prefix=prefix)
    target = os.path.join(root, "3d")
    if strip_glb:
        shutil.copytree(DIST, target)
        assets = os.path.join(target, SPECIMEN_ASSETS)
        removed = []
        for name in sorted(os.listdir(assets)) if os.path.isdir(assets) else []:
            if name.endswith(".glb"):
                os.remove(os.path.join(assets, name))
                removed.append(name)
        if not removed:
            shutil.rmtree(root, ignore_errors=True)
            raise RuntimeError(
                "cannot build the failure case: the build contains no .glb at "
                "all, so removing one would prove nothing")
    else:
        os.symlink(DIST, target)

    server, port = cdp.serve(root)

    def cleanup():
        server.shutdown()
        # unlink the symlink by hand before rmtree — the real dist/ is on the
        # other end of it and must not be within reach of a recursive delete
        if not strip_glb and os.path.islink(target):
            os.unlink(target)
        shutil.rmtree(root, ignore_errors=True)

    return "http://127.0.0.1:%d/3d/" % port, cleanup


def dist_staleness():
    """The newest file under src/ or content/, when it is newer than the build.

    Returns (path, seconds_ahead) or None.

    THIS IS NOW FATAL, and it used to be a note — ruled on MRB-191.

    The old reasoning was that this repo is worked in more than one worktree
    at a time, so a stale dist is usually a forgotten build rather than a
    defect. True, and beside the point. `npm run build` is `tsc && vite
    build`: a type error aborts BEFORE Vite writes, leaving dist/ on the
    previous build. Checks 1–10 then drive yesterday's renderer and print
    RENDER CHECK PASS about code that is not running.

    A gate that can report green on stale output is worse than no gate,
    because it turns a build failure into a false pass — and the pass is
    believed, twice over, since it is exactly the moment nobody re-reads the
    warnings. It cost the overnight session an hour as a warning printed
    twice. So it refuses.
    """
    index = os.path.join(DIST, "index.html")
    if not os.path.exists(index):
        return None
    built = os.path.getmtime(index)
    newest, newest_at = None, 0.0
    for root in (os.path.join(APP, "src"), os.path.join(APP, "content")):
        for dirpath, _dirs, files in os.walk(root):
            for f in files:
                p = os.path.join(dirpath, f)
                try:
                    m = os.path.getmtime(p)
                except OSError:
                    continue
                if m > newest_at:
                    newest, newest_at = p, m
    if newest and newest_at > built:
        return newest, newest_at - built
    return None


def main():
    started = time.time()
    print("3D Studio render check (MRB-187 Stage 2) — real Chrome, software WebGL")
    print("  the built app at %s, served as /3d/" % os.path.relpath(DIST, HERE))
    print("  checks 1–10 gate the exit code; frame timing is a report and never does")

    if not os.path.isdir(DIST) or not os.path.exists(os.path.join(DIST, "index.html")):
        print("FAIL: no built app at %s — run `npm run build` in 3d-studio/"
              % os.path.relpath(DIST, HERE))
        print("NO RESULTS — nothing was measured.")
        return 1

    # Refuse before a single browser starts. A refusal that still ran the
    # cheap checks would print a column of ticks above the failure, and the
    # ticks are what gets read.
    stale = dist_staleness()
    if stale:
        newest, behind = stale
        print("FAIL: the built app is STALE. %s is %.0fs newer than dist/."
              % (os.path.relpath(newest, HERE), behind))
        print("      `npm run build` is `tsc && vite build` — a type error "
              "aborts before Vite writes, so dist/ keeps the previous build "
              "and checks 1–10 would measure code that is not running.")
        print("      The render check refuses rather than report green about "
              "it (MRB-191).")
        print("      Run `npm run build` in 3d-studio/ and re-run. If the "
              "build fails, THAT is the defect this was hiding.")
        print("NO RESULTS — nothing was measured.")
        return 1

    every = hotspot_ids()
    print("  content/heart.json declares %d hotspot(s)\n" % len(every))

    report = Report()
    shots = tempfile.mkdtemp(prefix="st-render-shots-")
    shot_a = os.path.join(shots, "tier-a.png")
    shot_c = os.path.join(shots, "tier-c.png")

    url, cleanup = serve_dist_as_3d("st-render-")
    url_for_split = url
    timing = []
    try:
        # --enable-unsafe-swiftshader: without it headless Chrome has no WebGL
        # at all and the app routes, correctly, to the paper stage — see the
        # harness notes in this module's docstring.
        with cdp.Browser(extra_args=["--enable-unsafe-swiftshader"]) as b:
            page = b.attach()
            page.set_viewport(*VIEWPORT)
            page.goto(url)
            inject(page)

            if check_renders(page, report):
                # The default view's own dot set, measured once, before
                # anything has touched the camera. Checks 3 and 7 need a "we
                # are where the camera starts" precondition and used to get it
                # from a count off the record — which was the generated
                # fixture's arithmetic, not a fact about the camera (check 2
                # carries the full note). Measured, it stays true of whatever
                # specimen is loaded.
                default_view = settle(page)
                check_occlusion(page, report, every)
                check_reset(page, report, default_view)
                check_autorotate(page, report)
                check_tiers(page, report, shot_a, shot_c)
                check_parts(page, report, default_view)
                check_section(page, report, shots)
                check_framing(page, report)
                timing = frame_timing(page)
            else:
                print("       (checks 2–5, 7–8 and the timing report skipped — "
                      "nothing rendered)")

        # Its own browsers, off the same server: one with WebGL genuinely
        # disabled and one without.
        check_split(url_for_split, report)
    finally:
        cleanup()

    broken_url, broken_cleanup = serve_dist_as_3d(
        "st-render-noglb-", strip_glb=True)
    try:
        check_failure_route(broken_url, report)
    finally:
        broken_cleanup()

    shutil.rmtree(shots, ignore_errors=True)

    if timing:
        print_frame_timing(timing)

    gated = report.results
    passed = sum(1 for _n, _t, ok in gated if ok)
    print()
    if report.problems:
        print("%d problem(s):" % len(report.problems))
        for p in report.problems:
            print("  ✗ " + p)
        print("RENDER CHECK FAIL — %d/%d gates hold (%.0fs)"
              % (passed, len(gated), time.time() - started))
        return 1
    # Nothing about staleness is printed down here any more, and that is the
    # improvement: it cannot be reached with a stale dist. The warning used to
    # be repeated at the top and the bottom precisely because a note is easy to
    # scroll past — the fix for a warning nobody reads is not a third warning.
    print("RENDER CHECK PASS — %d/%d gates hold, frame timing reported only "
          "(%.0fs)" % (passed, len(gated), time.time() - started))
    return 0


if __name__ == "__main__":
    sys.exit(main())
