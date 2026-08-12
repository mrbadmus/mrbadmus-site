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

Checks 1–8 are gates: any failure exits non-zero.

  1. It renders at all. The mesh renderer mounts, the stage container reaches
     ``ready``, a <canvas> exists inside the stage.
  2. Honest occlusion. Every hotspot in ``content/heart.json`` has a dot at the
     default view; a drag that turns the specimen roughly 180° leaves NONE of
     them on screen; Reset brings them all back.
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
     deleted, must land on the flat stage: paper renderer, FLAT DIAGRAM chip,
     no quality chip, and no error/failure/apology text anywhere on the page.

  7. Isolate and layers (MRB-188). Isolate steps through every part the asset
     declares, drawing exactly one at a time and naming it from the file; one
     step past the last returns the whole specimen. Layers peels the outer
     depth level away. Both are judged by the HOTSPOT LAYER as well as by the
     part count — every stand-in anchor sits on the outer shell, so taking
     that shell off the stage must take its dots with it, which is the one
     thing a step counter cannot fake.

  8. The cross-section cuts, and the cut is CAPPED (MRB-189). The only check
     here that reads pixels rather than the DOM, because "is there a cut face
     at all" is not a question any attribute can answer. Repeated at all three
     tiers: Tier A renders through a post-processing composer whose own render
     target would silently un-cap the cut if it carried no stencil buffer.
     Whether the cap covers every last pixel of the cut is NOT settled here —
     see the limitation in the check's own docstring.

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
  * Occlusion at authored anchor positions. Every ``position3d`` in
    heart.json is still the all-zero Stage-8 sentinel, so the renderer derives
    stand-in anchors on the mesh surface. The occlusion MECHANISM is what is
    under test; the anchor coordinates arrive with the content.

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
SPECIMEN_GLB = os.path.join("assets", "_test-specimen.glb")

VIEWPORT = (1440, 900)

# A left-button drag this far across the stage turns the specimen roughly 180°
# at the desktop stage size: OrbitControls maps horizontal travel to azimuth
# against the element's height, and the stage is ~1055px tall here. Enough of
# a turn that every stand-in anchor — spread 18°–52° off the default camera
# axis — ends up behind the form. Verified by hand before it was written down.
DRAG_PX = 520
DRAG_STEPS = 30

# How still is still. The controls damp (dampingFactor 0.075), so a released
# drag or a just-switched-off auto-rotate keeps creeping for a second or more.
# Waiting a fixed sleep instead of waiting for stillness is how this check
# would become flaky, so it polls for a run of identical samples.
SETTLE_STABLE_RUNS = 5
SETTLE_INTERVAL = 0.3
SETTLE_TIMEOUT = 15.0

# How long "holds still" and "keeps moving" are given to prove themselves.
HOLD_SECONDS = 1.0

# Frame samples per tier in the frame-timing report.
FRAME_SAMPLES = 120


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

    Returns None on success, or a problem string if the press point is not
    over the canvas (a hotspot dot parked on the stage centre would swallow
    the press and the specimen would silently never turn — a harness fault
    wearing the costume of a broken renderer).
    """
    rect = page.eval("window.__rc.rect('.stage')")
    if not rect:
        return "no .stage to drag on"
    cx = rect["x"] + rect["w"] / 2.0
    cy = rect["y"] + rect["h"] / 2.0

    tag = page.eval("window.__rc.tagAt(%f, %f)" % (cx, cy))
    if tag != "canvas":
        return ("the stage centre (%.0f, %.0f) is covered by <%s>, not the "
                "canvas — the drag would never reach the controls" % (cx, cy, tag))

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


def hotspot_count():
    import json
    with open(HEART, encoding="utf-8") as fh:
        return len(json.load(fh)["hotspots"])


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


# ── checks 1–8 ───────────────────────────────────────────────────────────


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


def check_occlusion(page, report, want):
    """2. Honest occlusion."""
    problems, details = [], []

    at_default = settle(page)
    details.append("default view: %d dot(s) — %s"
                   % (len(at_default), ", ".join(at_default) or "none"))
    if len(at_default) != want:
        problems.append("expected %d dot(s) at the default view (one per "
                        "hotspot in content/heart.json), found %d"
                        % (want, len(at_default)))

    fault = drag_horizontal(page)
    if fault:
        problems.append("HARNESS: " + fault)
        report.check(2, "honest occlusion", problems, details)
        return

    turned = settle(page)
    details.append("after a %dpx drag (roughly 180°): %d dot(s)"
                   % (DRAG_PX, len(turned)))
    if turned:
        problems.append(
            "%d dot(s) survived the turn (%s) — every anchor should be on the "
            "far side of the specimen. A renderer that always reported "
            "visible:true would look exactly like this."
            % (len(turned), ", ".join(turned)))

    reset_view(page)
    back = settle(page)
    details.append("after Reset view: %d dot(s)" % len(back))
    if len(back) != want:
        problems.append("Reset brought back %d dot(s), expected %d"
                        % (len(back), want))

    report.check(2, "honest occlusion", problems, details)


def check_reset(page, report, want):
    """3. Reset is exact."""
    problems, details = [], []

    baseline = settle(page)
    if len(baseline) != want:
        problems.append("not at the default view before the test (%d dot(s), "
                        "expected %d)" % (len(baseline), want))

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


def check_parts(page, report, want):
    """7. Isolate and layers take real geometry off the stage (MRB-188).

    The failure this is written against is a control that steps a counter
    while the picture stays the same. So every assertion below is about
    something OUTSIDE the tool's own bookkeeping: how many hotspot dots the
    shell is drawing, which is downstream of the renderer's occlusion test and
    of part visibility, and never of the step number.

    On the generated test specimen every stand-in anchor sits on the outer
    shell (the raycast that places them starts outside the form and stops at
    the first surface it meets), so:

      * isolate the shell  ⇒ the dots stay, the interior goes
      * isolate anything else, or peel the outer layer ⇒ the shell is not
        drawn, so every dot on it goes with it

    That second line is the one that cannot be faked by a counter.
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
    if len(at_start) != want:
        problems.append("not at the default view before the test (%d dot(s), "
                        "expected %d)" % (len(at_start), want))

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
        problems.append(
            "the hotspot layer did not change across isolate's %d steps "
            "(%s dot(s) each time). Every stand-in anchor sits on the outer "
            "shell, so isolating anything else must take its dots with it — "
            "this is the assertion a counter cannot fake."
            % (whole, dots_per_step))
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
    if len(restored) != want:
        problems.append("the dots did not come back with the whole specimen "
                        "(%d, expected %d)" % (len(restored), want))

    if not page.eval("window.__rc.rail('Layers')"):
        problems.append("no Layers button on the rail")
        report.check(7, "isolate and layers", problems, details)
        return
    time.sleep(0.35)
    peeled_parts = page.eval("window.__rc.partsShown()")
    peeled_layer = page.eval("window.__rc.ds('layer')")
    peeled_dots = len(dots(page))
    if peeled_parts is None or peeled_parts >= whole:
        problems.append("Layers left %r of %d part(s) drawn — nothing was "
                        "peeled" % (peeled_parts, whole))
    if peeled_layer in (None, "off"):
        problems.append("Layers reports %r — the tool did not engage"
                        % peeled_layer)
    if peeled_dots >= len(restored):
        problems.append(
            "peeling the outer layer left %d dot(s), same or more than the %d "
            "before it. Every anchor sits on the outer shell, so removing that "
            "layer must remove them." % (peeled_dots, len(restored)))
    details.append("layers: %r, %s of %d part(s) drawn, %d dot(s) (was %d)"
                   % (peeled_layer, peeled_parts, whole, peeled_dots,
                      len(restored)))

    # ── reset puts the form back whole ────────────────────────────────────
    reset_view(page)
    after_reset = settle(page)
    if page.eval("window.__rc.partsShown()") != whole:
        problems.append("Reset left the specimen taken apart — a half-restored "
                        "view reads as a broken control")
    if len(after_reset) != want:
        problems.append("Reset brought back %d dot(s), expected %d"
                        % (len(after_reset), want))
    else:
        details.append("Reset restores the whole specimen and all %d dot(s)"
                       % want)

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
    return (abs(rgb[0] - VOID_RGB[0]) < 40 and rgb[1] < 60
            and abs(rgb[2] - VOID_RGB[2]) < 40)


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


def _is_cut_face(rgb):
    """A pixel of exposed cut material.

    The cap is drawn in the accent family (`#A93411` outer, `#E4572E` inside
    it) — strongly saturated red-orange. The generated test specimen's own PBR
    surface is a near-neutral warm grey: measured around (192, 170, 158),
    saturation 0.18. The gap between the two is nearly fivefold, so this
    classifier does not need to be clever, and it deliberately is not: it
    checks that the pixel is saturated, red-dominant, and warmer in green than
    in blue. Magenta fails it on the last condition, which matters because the
    void backdrop is the other thing on screen.

    It DOES assume the specimen is not itself painted a saturated orange. A
    bought asset could be; the check reports its counts either way, and a
    specimen that broke the assumption would show as a large cut-face count
    with no cut engaged, which is asserted below rather than assumed.
    """
    top, bottom = max(rgb), min(rgb)
    if top < 40:
        return False
    return (top - bottom) / float(top) > 0.45 and rgb[0] == top and rgb[2] <= rgb[1]


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

      * THE CAP IS DRAWN. The cut face is painted in the accent family, which
        is nothing like the specimen's own near-neutral surface, so counting
        saturated red-orange pixels answers "is there a cut face" directly.
        Asserted in both directions: many with the cut engaged, essentially
        none without it.
      * THE CAP HAS NO HOLE IN IT. The canvas is transparent — Design's room
        is a CSS gradient behind it — so the stage background is swapped for
        magenta and any background pixel ENCLOSED by specimen pixels on its
        own scanline is counted. Enclosed, not merely present: a cut
        legitimately narrows the silhouette wherever the near half bulged
        further than the far half, and an earlier version of this check called
        that a defect. It is not one; a hole in the middle of the cut face is.
      * INTERIOR GEOMETRY BECOMES VISIBLE. Proven without naming a colour:
        with the specimen whole, isolating the outer shell draws the SAME
        picture as drawing everything, because everything else is inside it.
        Engage the cut and that stops being true — which is what "the interior
        is now visible" means, stated as something measurable.

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
        path = os.path.join(shots, name + ".png")
        page.screenshot(path, width=VIEWPORT[0], height=VIEWPORT[1], full_page=False)
        page.set_viewport(*VIEWPORT)
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
        drawn = {p for p, rgb in whole.items() if not _is_void(rgb)}
        face_before = sum(1 for rgb in whole.values() if _is_cut_face(rgb))

        # The instrument's own noise floor: the SAME state, photographed
        # twice. Tier A renders through SSAO and a continuously re-integrated
        # contact shadow, and neither settles to identical bytes — measured at
        # a few hundred pixels here, against 1 at tiers B and C. The
        # comparisons below are against this rather than against zero, so the
        # gate is calibrated to what the renderer actually does rather than to
        # what a still image would do.
        again, _ = shoot("t%s-again" % tier)
        noise = sum(1 for p in whole if _differs(whole[p], again.get(p)))
        if len(drawn) < 500:
            problems.append(
                "tier %s: only %d specimen pixel(s) on the stage before the cut "
                "— the backdrop probe or the render is broken, and everything "
                "below would be measuring nothing" % (tier, len(drawn)))
            continue

        # ── shell alone, no cut: must be the same picture ─────────────────
        page.eval("window.__rc.rail('Isolate')")
        time.sleep(0.5)
        shell, _ = shoot("t%s-shell" % tier)
        same_before = sum(1 for p in whole if _differs(whole[p], shell.get(p)))

        # ── shell alone, cut ──────────────────────────────────────────────
        page.eval("window.__rc.rail('Cross-section')")
        time.sleep(0.6)
        shell_cut, _ = shoot("t%s-shell-cut" % tier)

        # ── whole specimen, cut ───────────────────────────────────────────
        page.eval("window.__rc.rail('Isolate')")   # step off the shell…
        for _ in range(4):
            page.eval("window.__rc.rail('Isolate')")  # …round to whole again
        time.sleep(0.6)
        if page.eval("window.__rc.ds('isolate')") != "off":
            problems.append("tier %s: could not get back to the whole specimen"
                            % tier)
        cut, cut_rows = shoot("t%s-cut" % tier)

        face_after = sum(1 for rgb in cut.values() if _is_cut_face(rgb))
        holes_before = _interior_holes(whole_rows, inner)
        holes_after = _interior_holes(cut_rows, inner)
        changed = sum(1 for p in drawn if _differs(whole[p], cut.get(p)))
        same_after = sum(1 for p in cut if _differs(cut[p], shell_cut.get(p)))

        # (a) a cut face exists, and only once there is a cut
        if face_before > len(drawn) * 0.02:
            problems.append(
                "tier %s: %d cut-face pixel(s) with NO cut engaged — the "
                "specimen\'s own surface is being read as a cap, so the count "
                "below proves nothing" % (tier, face_before))
        if face_after < len(drawn) * 0.10:
            problems.append(
                "tier %s: %d of %d specimen pixel(s) are cut face — the plane "
                "clipped the geometry and left the cut open"
                % (tier, face_after, len(drawn)))

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

        # (d) the interior was hidden before, and is not after
        if same_before > max(noise * 3, len(drawn) * 0.01):
            problems.append(
                "tier %s: isolating the outer shell changed %d pixel(s) with no "
                "cut engaged, against a %d-pixel noise floor — the interior was "
                "already visible, so the line below would prove nothing"
                % (tier, same_before, noise))
        if same_after < max(noise * 3, len(drawn) * 0.02):
            problems.append(
                "tier %s: with the cut engaged, drawing the whole specimen and "
                "drawing only its outer shell are still the same picture (%d "
                "pixel(s) differ) — the cut exposed no interior geometry"
                % (tier, same_after))

        details.append(
            "tier %s: %d specimen px · noise floor %d · cut face %d → %d · "
            "enclosed background %d → %d · cut changed %d (%.0f%%) · interior "
            "hidden before (%d px differ) → visible after (%d px differ)"
            % (tier, len(drawn), noise, face_before, face_after, holes_before,
               holes_after, changed, 100.0 * changed / max(len(drawn), 1),
               same_before, same_after))

        page.eval("window.__rc.rail('Cross-section')")
        time.sleep(0.3)

    page.eval("window.__rc.restoreBackdrop()")
    reset_view(page)
    settle(page)
    details.append("cut-face pixels are counted by saturation, not by an exact "
                   "colour match: the cap is lit and tone-mapped like anything "
                   "else. The specimen\'s own surface measures 0.18 saturation "
                   "against the classifier\'s 0.45 floor, and the count with no "
                   "cut engaged is asserted above rather than assumed.")

    report.check(8, "cross-section is capped, at every tier (MRB-189)",
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
            if renderer == "placeholder-paper":
                break
            time.sleep(0.2)

        detected = page.eval(
            "document.querySelector('.app').getAttribute('data-detected-tier')")
        if detected == "D":
            problems.append(
                "HARNESS: this browser has no WebGL either, so the flat stage "
                "proves nothing about the missing-GLB route")

        if renderer != "placeholder-paper":
            problems.append("stage reports renderer=%r, expected "
                            "'placeholder-paper' — a mesh that will not load "
                            "must route to the flat stage" % renderer)
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
    copied, nothing can drift). The failure build is a real copy with the
    specimen GLB removed: the real dist/ is never touched.

    Returns (url, cleanup).
    """
    root = tempfile.mkdtemp(prefix=prefix)
    target = os.path.join(root, "3d")
    if strip_glb:
        shutil.copytree(DIST, target)
        glb = os.path.join(target, SPECIMEN_GLB)
        if not os.path.exists(glb):
            shutil.rmtree(root, ignore_errors=True)
            raise RuntimeError(
                "cannot build the failure case: %s is not in the build, so "
                "removing it would prove nothing" % SPECIMEN_GLB)
        os.remove(glb)
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


def staleness_note():
    """A built app older than its sources measures yesterday's renderer.

    A note, not a failure: this repo is worked in more than one worktree at a
    time and a stale dist is usually a forgotten build, not a defect.
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
        return ("WARNING: %s is newer than the build — run `npm run build` in "
                "3d-studio/ or this measures the previous renderer"
                % os.path.relpath(newest, HERE))
    return None


def main():
    started = time.time()
    print("3D Studio render check (MRB-187 Stage 2) — real Chrome, software WebGL")
    print("  the built app at %s, served as /3d/" % os.path.relpath(DIST, HERE))
    print("  checks 1–8 gate the exit code; frame timing is a report and never does")

    if not os.path.isdir(DIST) or not os.path.exists(os.path.join(DIST, "index.html")):
        print("FAIL: no built app at %s — run `npm run build` in 3d-studio/"
              % os.path.relpath(DIST, HERE))
        return 1

    stale = staleness_note()
    if stale:
        print("  " + stale)

    want = hotspot_count()
    print("  content/heart.json declares %d hotspot(s)\n" % want)

    report = Report()
    shots = tempfile.mkdtemp(prefix="st-render-shots-")
    shot_a = os.path.join(shots, "tier-a.png")
    shot_c = os.path.join(shots, "tier-c.png")

    url, cleanup = serve_dist_as_3d("st-render-")
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
                check_occlusion(page, report, want)
                check_reset(page, report, want)
                check_autorotate(page, report)
                check_tiers(page, report, shot_a, shot_c)
                check_parts(page, report, want)
                check_section(page, report, shots)
                timing = frame_timing(page)
            else:
                print("       (checks 2–5, 7–8 and the timing report skipped — "
                      "nothing rendered)")
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
    print("RENDER CHECK PASS — %d/%d gates hold, frame timing reported only "
          "(%.0fs)" % (passed, len(gated), time.time() - started))
    return 0


if __name__ == "__main__":
    sys.exit(main())
