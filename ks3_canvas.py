#!/usr/bin/env python3
"""ks3_canvas.py — does the canvas actually REDRAW when you touch the controls?

    python3 ks3_canvas.py

Exit 0 clean, 1 if any instrument failed to redraw, 2 on a harness fault.

── Why this exists ────────────────────────────────────────────────────────

`ks3_parity.py` covers the KS3 instruments thoroughly — every colour, every
length, every state, driven through their real controls — and covers the canvas
NOT AT ALL. The one canvas row it has, `check_canvas_contrast()`, computes
contrast from `tokens.css` arithmetically. It never opens a browser. It cannot
tell a canvas that redraws from a canvas that has been painted once and then
sits there, and a canvas that has been painted once looks exactly right in a
screenshot.

That is precisely where the C1 instruments were broken: the picture was on
screen, the controls responded, the aria-pressed flipped, the readouts updated —
and the drawing did not move. Every assertion in the parity gate stayed green
through all of it, because none of them were looking at pixels.

So this reads the pixels. Per instrument: capture `toDataURL()`, drive the real
controls, capture again, and fail if the bytes are identical.

── The trap this file exists to avoid, and how it is handled ──────────────

"Compare before and after" is only evidence if the canvas would otherwise have
STAYED THE SAME. A canvas running its own animation loop differs from itself
one frame later, so a before/after diff on one of those passes whatever the
control does — including nothing. That is a gate that lies, which is the thing
this whole phase is about.

So every instrument is measured for IDLE STABILITY first, and the two kinds get
different, honestly-labelled assertions:

  STABLE (five of the six) — sampled three times at rest with no interaction,
      the bytes must be identical. Then, and only then, driving the controls
      must change them. The idle check is the control for the drive check: it
      is what makes "the bytes changed" mean "the control redrew it".

  ANIMATED (`collision-counter` on gas-pressure, a live gas simulation) — a
      pixel diff proves nothing, so it is not claimed. What IS asserted is the
      property that actually broke: the render loop is RUNNING (three idle
      samples must all differ), and driving a control moves the instrument's
      own live readout. The row says which of the two it is, so nobody reads
      more into it than it proves.

An instrument that is registered as STABLE and turns out to animate — or the
reverse — is itself a failure, not a silent switch to the other mode. That
would be the gate quietly rewriting its own claim to stay green.
"""

import hashlib
import os
import sys
import time

KS3_OUT = os.path.join("mrbadmus_site", "ks3")
C1 = "chemistry/particles-and-their-behaviour/"

STABLE = "stable"
ANIMATED = "animated"


# ── the instruments, their canvases, and how to work their real controls ──
#
# ⚠️ THE DRIVES CLICK THE SHIPPED CONTROLS. Not a synthetic event on the
# canvas, not a call into the instrument's internals — the same buttons and
# range inputs a student touches. An instrument whose controls are wired to
# nothing has to fail here, and it can only fail if this is what is driven.
INSTRUMENTS = [
    dict(
        name="halving-bench · cutting the block redraws it",
        page=C1 + "particle-model.html",
        canvas="[data-cut-canvas]",
        kind=STABLE,
        drive="""(function () {
          var b = document.querySelector('.ks3-cut-btn[data-act="cut"]');
          if (!b) { return "no cut control on the bench"; }
          if (b.disabled) { return "the cut control is disabled at rest"; }
          b.click(); b.click(); b.click();
          return "";
        })()""",
    ),
    dict(
        name="gap-test-rig · choosing a test redraws the boxes",
        page=C1 + "particle-model.html",
        canvas="[data-gap-canvas]",
        kind=STABLE,
        # ⚠️ ITS OWN GATE, not the page's. particle-model carries ONE
        # `[data-benchgate]` and it belongs to the halving bench; the gap rig
        # is revealed by ANSWERING it, so `bench-gate-opened` leaves this
        # canvas inside `DIV.ks3-gap-rig[hidden]` and the precondition says so
        # rather than measuring a frozen picture.
        gate="gap-answered",
        drive="""(function () {
          var t = document.querySelectorAll('.ks3-gap-test');
          if (t.length < 2) { return "the rig offers " + t.length + " test(s)"; }
          t[0].click();
          return "";
        })()""",
    ),
    dict(
        name="heating-bench · scrubbing the curve redraws the flask",
        page=C1 + "changes-of-state.html",
        canvas="[data-hb-canvas]",
        kind=STABLE,
        drive="""(function () {
          var j = document.querySelectorAll('.ks3-hb-jump');
          if (!j.length) { return "the bench offers no temperature jumps"; }
          for (var i = 0; i < j.length; i++) {
            if (j[i].getAttribute('aria-pressed') !== 'true') { j[i].click(); return ""; }
          }
          return "every temperature jump was already pressed";
        })()""",
    ),
    dict(
        name="random-walk-bench · running the walk redraws the tank",
        page=C1 + "diffusion.html",
        canvas="[data-walk-canvas]",
        kind=STABLE,
        drive="""(function () {
          var r = document.querySelector('[data-walk-run]');
          if (!r) { return "the bench has no run control"; }
          r.click();
          return "";
        })()""",
    ),
    dict(
        name="state-bench · changing state redraws the particle box",
        page=C1 + "solids-liquids-and-gases.html",
        canvas="[data-sbench-canvas]",
        # ⚠️ ANIMATED, and it took the gate refusing to lie to find that out.
        # Registered STABLE at first, on a measurement taken while the bench
        # was still behind its gate and therefore frozen. Once the gate is
        # opened the particles move and the canvas differs from itself at
        # rest, so a before/after pixel diff would pass whatever the control
        # did. The check said so — "registered STABLE but the canvas differs
        # from itself at rest" — instead of quietly switching mode, which is
        # the whole reason that branch is a FAIL and not a shrug.
        kind=ANIMATED,
        readout_attr=("[data-sbench-canvas]", "aria-label"),
        drive="""(function () {
          var g = document.querySelector('[data-sbench-state="gas"]');
          if (!g) { return "the bench has no gas setting"; }
          if (g.getAttribute('aria-pressed') === 'true') { return "it opens on gas"; }
          g.click();
          return "";
        })()""",
    ),
    dict(
        name="collision-counter · the simulation is running, and the dial moves it",
        page=C1 + "gas-pressure.html",
        canvas="[data-counter-canvas]",
        kind=ANIMATED,
        # For the animated one the pixel diff proves nothing, so the drive is
        # checked against the instrument's OWN live readout instead.
        # The counter's numbers are DRAWN ON THE CANVAS, not in the DOM —
        # "Wall hits in the last second: 0. Pressure: 0.0 kPa." lives in the
        # canvas's own aria-label, which the instrument keeps up to date
        # because that label IS the readout for a screen reader. So that is
        # what the drive is checked against, and it is the right thing to
        # check: if it stops moving, a blind student's readout has frozen.
        readout_attr=("[data-counter-canvas]", "aria-label"),
        drive="""(function () {
          var b = document.querySelectorAll('.ks3-counter-btn[data-group="temp"]');
          if (b.length < 2) { return "the counter offers " + b.length + " temperature(s)"; }
          for (var i = 0; i < b.length; i++) {
            if (b[i].getAttribute('aria-pressed') !== 'true') { b[i].click(); return ""; }
          }
          return "every temperature was already pressed";
        })()""",
    ),
]

_SNAP = """(function () {
  var c = document.querySelector(%r);
  if (!c) { return "NO-CANVAS"; }
  if (!c.getContext) { return "NOT-A-CANVAS"; }
  try { return c.toDataURL(); } catch (e) { return "TAINTED:" + e.message; }
})()"""

_ATTR = """(function () {
  var e = document.querySelector(%r);
  return e ? (e.getAttribute(%r) || "").trim() : "NO-READOUT";
})()"""

IDLE_SAMPLES = 3
IDLE_GAP = 0.55

# ⚠️ THE BENCH SHIPS BEHIND A GATE, AND THIS COST TWO FALSE FINDINGS.
#
# Every C1 instrument's body ships `hidden` until the student commits to the
# question in front of it, and the render loops guard on exactly that:
#
#     if (body.hasAttribute("hidden") || document.hidden) { return; }
#
# So a canvas measured before the gate is opened NEVER REDRAWS, whatever you
# click — and the first run of this file duly reported `random-walk-bench` and
# `state-bench` as broken. They are not. The controls were live, nothing was
# disabled, no sim was locked, `document.hidden` was false and scrolling the
# canvas into view changed nothing; the bench body simply still had `hidden` on
# it. Reported as a defect, that is a gate lying in the other direction, which
# is no better than a gate that passes.
#
# So the gate is OPENED first, through `ks3_parity`'s own registered drive
# rather than a copy of it, and then the canvas is checked to have no `[hidden]`
# ancestor left. A canvas still behind a gate FAILS LOUDLY as a precondition —
# never measured and quietly reported.
_HIDDEN_ANCESTORS = """(function () {
  var n = document.querySelector(%r), out = [];
  if (!n) { return "NO-CANVAS"; }
  while (n) {
    if (n.hasAttribute && n.hasAttribute('hidden')) {
      out.push(n.tagName + '.' + String(n.className || '').split(' ')[0]);
    }
    n = n.parentElement;
  }
  return out.join(' < ');
})()"""


def _digest(data):
    return hashlib.sha256(data.encode("utf-8")).hexdigest()[:16]


def _snapshot(page, sel):
    raw = page.eval(_SNAP % sel)
    if raw in ("NO-CANVAS", "NOT-A-CANVAS") or raw.startswith("TAINTED:"):
        return None, raw
    return _digest(raw), ""


def _idle_series(page, sel):
    """Sample the canvas at rest, without touching anything."""
    out = []
    for i in range(IDLE_SAMPLES):
        d, err = _snapshot(page, sel)
        if d is None:
            return None, err
        out.append(d)
        if i < IDLE_SAMPLES - 1:
            time.sleep(IDLE_GAP)
    return out, ""


def run(cdp, instruments=None, settle_js="", gate_js="", gates=None):
    """Drive each instrument. Returns (rows, problems).

    rows: (name, kind, verdict, detail)
    """
    instruments = instruments or INSTRUMENTS
    gates = gates or {}
    rows, problems = [], []
    serve_root = os.path.dirname(KS3_OUT) or "."
    prefix = "/" + os.path.basename(KS3_OUT)
    server, port = cdp.serve(serve_root)
    try:
        for inst in instruments:
            name, kind, sel = inst["name"], inst["kind"], inst["canvas"]
            url = "http://127.0.0.1:%d%s/%s" % (port, prefix, inst["page"])
            # A fresh browser per instrument: the KS3 canvas loops keep running
            # after the driver moves on, and this file is the one place that
            # cares what those loops are doing.
            with cdp.Browser() as b:
                page = b.attach()
                page.set_viewport(1280, 900)
                page.goto(url)
                if settle_js:
                    page.eval(settle_js)

                # ── PRECONDITION: open the bench gate ────────────────────
                # Through ks3_parity's OWN registered drive, not a copy, so
                # this cannot drift away from how the gate really opens.
                this_gate = gates.get(inst.get("gate", "bench-gate-opened"),
                                     gate_js)
                if this_gate:
                    gate_err = page.eval(this_gate)
                    if gate_err and "no commit gate" not in gate_err:
                        problems.append("%s — could not open the bench gate: "
                                        "%s" % (name, gate_err))
                        rows.append((name, kind, "FAIL", gate_err))
                        continue
                    time.sleep(0.25)

                # ── PRECONDITION: nothing is still `hidden` ──────────────
                # A canvas inside a hidden body never redraws, whatever you
                # click, because the render loop returns early on exactly
                # that. Measuring one would report a working instrument as
                # broken — it did, twice, before this check existed.
                hidden = page.eval(_HIDDEN_ANCESTORS % sel)
                if hidden == "NO-CANVAS":
                    problems.append("%s — no canvas at %s on %s"
                                    % (name, sel, inst["page"]))
                    rows.append((name, kind, "FAIL", "no canvas at %s" % sel))
                    continue
                if hidden:
                    d = ("the canvas is still inside a hidden element (%s) "
                         "after the gate step. Its render loop returns early "
                         "on `body.hasAttribute(\"hidden\")`, so nothing "
                         "measured here would mean anything" % hidden)
                    problems.append("%s — %s" % (name, d))
                    rows.append((name, kind, "FAIL", d))
                    continue

                idle, err = _idle_series(page, sel)
                if idle is None:
                    problems.append("%s — %s (%s on %s)"
                                    % (name, err, sel, inst["page"]))
                    rows.append((name, kind, "FAIL", err))
                    continue

                animating = len(set(idle)) > 1

                # ⚖️ The registered kind is a CLAIM, and a claim that turns out
                # false is a failure. Silently switching to the other mode is
                # how a gate rewrites itself to stay green.
                if kind == STABLE and animating:
                    d = ("registered STABLE but the canvas differs from itself "
                         "at rest (%s). A before/after diff would then pass "
                         "whatever the control does" % " ".join(idle))
                    problems.append("%s — %s" % (name, d))
                    rows.append((name, kind, "FAIL", d))
                    continue
                if kind == ANIMATED and not animating:
                    d = ("registered ANIMATED and the canvas is IDENTICAL "
                         "across %d samples at rest (%s) — the render loop has "
                         "stopped, which is the liveness this row exists to "
                         "hold" % (IDLE_SAMPLES, idle[0]))
                    problems.append("%s — %s" % (name, d))
                    rows.append((name, kind, "FAIL", d))
                    continue

                before = idle[-1]
                # ⚖️ The animated branch needs a BEFORE for its readout, and it
                # has to be taken before the drive. Reporting the readout after
                # the fact — which the first version did — is not an assertion:
                # a control wired to nothing leaves a perfectly good-looking
                # readout sitting there, and the row passes on it.
                read_before = ""
                if kind == ANIMATED:
                    r_sel, r_attr = inst["readout_attr"]
                    read_before = page.eval(_ATTR % (r_sel, r_attr))
                err = page.eval(inst["drive"])
                if err:
                    problems.append("%s — the drive could not work the real "
                                    "controls: %s" % (name, err))
                    rows.append((name, kind, "FAIL", err))
                    continue
                time.sleep(IDLE_GAP)

                if kind == STABLE:
                    after, serr = _snapshot(page, sel)
                    if after is None:
                        problems.append("%s — %s after the drive" % (name, serr))
                        rows.append((name, kind, "FAIL", serr))
                        continue
                    if after == before:
                        d = ("the canvas is BYTE-IDENTICAL after driving its "
                             "own controls (%s). The controls responded and "
                             "the drawing did not move — which is exactly what "
                             "a screenshot cannot see" % before)
                        problems.append("%s — %s" % (name, d))
                        rows.append((name, kind, "FAIL", d))
                    else:
                        rows.append((name, kind, "PASS",
                                     "stable at rest across %d samples (%s), "
                                     "and the drive redrew it (%s -> %s)"
                                     % (IDLE_SAMPLES, before, before, after)))
                else:
                    # ANIMATED: the loop is proved running by the idle series.
                    # The drive is proved by the instrument's own readout.
                    r_sel, r_attr = inst["readout_attr"]
                    got = page.eval(_ATTR % (r_sel, r_attr))
                    if got == "NO-READOUT" or read_before == "NO-READOUT":
                        d = ("no live readout at %s[%s] to check the drive "
                             "against" % (r_sel, r_attr))
                        problems.append("%s — %s" % (name, d))
                        rows.append((name, kind, "FAIL", d))
                    elif got == read_before:
                        d = ("the render loop is running, but driving the "
                             "controls did not move the live readout "
                             "%s[%s] — it still reads %r. On an animated "
                             "canvas a pixel diff proves nothing, so this "
                             "readout is the whole of the evidence that the "
                             "control did anything"
                             % (r_sel, r_attr, got[:60]))
                        problems.append("%s — %s" % (name, d))
                        rows.append((name, kind, "FAIL", d))
                    else:
                        rows.append((name, kind, "PASS",
                                     "the render loop is running (%d idle "
                                     "samples all differ: %s), and driving the "
                                     "real controls moved the live readout: "
                                     "%r -> %r. A pixel diff is NOT claimed "
                                     "here and would prove nothing"
                                     % (IDLE_SAMPLES, " ".join(idle),
                                        read_before[:46], got[:46])))
    finally:
        server.shutdown()
    return rows, problems


def main():
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import ks3_browser as cdp
    try:
        import ks3_parity
        settle = ks3_parity._JS_SETTLE
    except Exception:                                       # noqa: BLE001
        settle = ""

    try:
        gate = ks3_parity.DRIVES["bench-gate-opened"]
        gates = dict(ks3_parity.DRIVES)
    except Exception:                                       # noqa: BLE001
        gate, gates = "", {}

    print("── the canvas gate ──")
    rows, problems = run(cdp, settle_js=settle, gate_js=gate, gates=gates)
    for name, kind, verdict, detail in rows:
        print("  %-4s %-8s %s" % (verdict, kind, name))
        print("         %s" % detail)
    print()
    if problems:
        print("  %d PROBLEM(S) — a canvas that does not redraw looks correct "
              "in every screenshot ever taken of it." % len(problems))
        return 1
    n_stable = sum(1 for r in rows if r[1] == STABLE)
    print("  PASS  %d instrument(s) — %d stable (the canvas redraws when its "
          "own controls are driven) and %d animated (the render loop is "
          "running and the drive moves the live readout)."
          % (len(rows), n_stable, len(rows) - n_stable))
    return 0


if __name__ == "__main__":
    sys.exit(main())
