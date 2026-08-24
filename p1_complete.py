#!/usr/bin/env python3
"""p1_complete.py — drive every P1 instrument to COMPLETION and prove it ticks.

`p1_drive.py` presses every control ONCE and asserts that each one changes its
own section. That catches a dead control, and it is the right first pass — but
it cannot reach completion, because completion is a SEQUENCE: three rods raced,
three runs recorded, every scenario visited, a clock run to the end. A sweep
that presses each button once leaves those stops un-ticked and cannot tell
"this stop is unreachable" from "I did not do enough".

So this drives each instrument the way a student would, and asserts:

  1 · the stop TICKS — `data-stage-done` goes to "1" on that section
  2 · it was NOT ticked before the drive, so the tick was earned
  3 · for the two comparatives, the EQUAL state is also driven and asserted,
      because MRB-257 §5A.1 says that is the state an authored comparative
      gets wrong

⚠️ A stop that cannot be ticked by any sequence is a rail stop a student can
never complete, and MRB-208's R2 gate checks only that the page DECLARES a
completion signal — not that any sequence actually fires one. That gap is why
this file exists: the eight instruments this run added shipped with no
`markStage` call at all, every gate passed, and the rail simply never moved.
"""
import os
import shutil
import sys
import time

import ks3_browser as cdp

def _sweep_chrome_tmp(older_than_min=30):
    """Remove Chrome's OWN $TMPDIR litter, which nothing else cleans up.

    ⚠️ THIS FILLED A 228 GB DISK ON THE NIGHT OF 24 AUG 2026. `ks3_browser`
    already removes the `--user-data-dir` it creates (see its `stop()`), and
    that is not what leaks. Chrome ALSO writes about a hundred
    `.com.google.Chrome.*` entries per launch straight into $TMPDIR, plus a
    `scoped_dir*` profile, and removes none of them. A night of gate runs —
    every `verify_ks3` launches dozens — left 15,304 of them and 426
    profiles, and free space went from 6.1 GB to 234 MB.

    Only entries older than `older_than_min` are touched, so a live browser
    (the user's own, or one this process has open) is never interfered with.
    """
    import glob
    import time as _t
    tmp = os.environ.get("TMPDIR") or "/tmp"
    cutoff = _t.time() - older_than_min * 60
    n = 0
    for pat in (".com.google.Chrome.*", "scoped_dir*"):
        for p in glob.glob(os.path.join(tmp, pat)):
            try:
                if os.path.getmtime(p) < cutoff:
                    if os.path.isdir(p):
                        shutil.rmtree(p, ignore_errors=True)
                    else:
                        os.remove(p)
                    n += 1
            except OSError:
                pass
    return n


HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)
DIR = "ks3/physics/energy-transfers"

# One drive per instrument: click these selectors in order, pausing where a
# timer has to run. `n` repeats a click on the same selector.
DRIVES = {
    # ⚠️ p1-01 IS RUN 2's AND IS DRIVEN HERE TOO, because a completion drive
    # that skips the one lesson it did not write proves nothing about the
    # unit. Its ledger cannot be completed by clicking every chip — a
    # SUPERSET does not balance, by design — so the drive reads the correct
    # answer off each chip's own `data-saudit-want-<scenario>` attribute,
    # which is where the payload puts it.
    "energy-stores": [
        ("store-audit", [("__ledger__", 0)], 0.3),
        ("store-pathway-sort", [("[data-spath-pick]", "all")], 0.4),
    ],
    "energy-transfers-before-and-after": [
        ("before-after-tally", [("[data-btally-gopt]", 1),
                                ("[data-btally-dev]", "all")], 0.4),
        ("waste-sort", [("[data-wsort-pick]", "all")], 0.4),
    ],
    "conservation-of-energy": [
        ("running-total", [("[data-rtotal-gopt]", 1),
                           ('[data-rtotal-ctl="hide"]', 1)], 0.4),
        ("conservation-beam", [("[data-cbeam-split]", "all")], 0.4),
    ],
    "heating-and-thermal-equilibrium": [
        ("two-quantities", [("[data-twoq-amt]", "all"), ("[data-twoq-spd]", "all")], 0.4),
        # every pair, each one RUN — the equal pair included
        ("one-way-flow", [("__pairs_run__", 0)], 0.2),
    ],
    "conduction": [
        # three rods raced, not merely selected
        ("conduction-bench", [("__rods_run__", 0)], 0.2),
        ("touch-test", [("[data-wsort-pick]", "all")], 0.4),
    ],
    "radiation": [
        ("three-routes", [("[data-troute-sc]", "all")], 0.3),
        ("radiation-word-sort", [("[data-wsort-pick]", "all")], 0.4),
    ],
    "insulation": [
        ("plan-the-trial", [("[data-wsort-pick]", "all")], 0.4),
        ("insulation-trial", [("[data-itrial-jump]", 1)], 0.4),
        ("ice-trial", [("__ice_run__", 0)], 0.2),
    ],
    "simple-machines": [
        ("lever-bench", [("[data-lever-gopt]", 1), ("[data-lever-record]", 3)], 0.4),
    ],
}

JS_CLICK = """
(function (sel, mode) {
  var els = Array.prototype.slice.call(document.querySelectorAll(sel));
  if (!els.length) { return 0; }
  if (mode === 'all') { els.forEach(function (e) { e.click(); }); return els.length; }
  var n = Math.min(mode, els.length), i;
  for (i = 0; i < mode; i++) { els[Math.min(i, els.length - 1)].click(); }
  return mode;
})(%s, %s)
"""

# Pairs: select each, run it, wait for it to settle.
JS_PAIRS_RUN = """
(function () {
  var picks = Array.prototype.slice.call(
    document.querySelectorAll('[data-oflow-pair]'));
  var run = document.querySelector('[data-oflow-run]');
  window.__i = 0;
  window.__step = function () {
    if (window.__i >= picks.length) { return 'done'; }
    picks[window.__i].click();
    if (run) { run.click(); }
    window.__i += 1;
    return window.__i;
  };
  return picks.length;
})()
"""

JS_RODS_RUN = """
(function () {
  var picks = Array.prototype.slice.call(
    document.querySelectorAll('[data-cbench-mat]'));
  var run = document.querySelector('[data-cbench-run]');
  window.__i = 0;
  window.__step = function () {
    if (window.__i >= picks.length) { return 'done'; }
    picks[window.__i].click();
    if (run) { run.click(); }
    window.__i += 1;
    return window.__i;
  };
  return picks.length;
})()
"""

JS_ICE_RUN = """
(function () {
  var r = document.querySelector('[data-itrial2-run]');
  if (r) { r.click(); }
  return !!r;
})()
"""

# The ledger, balanced honestly. Each chip carries `data-saudit-want-<sc>`
# valued "before" or "after" for the scenarios it belongs to, so the correct
# set for a scenario is readable off the DOM rather than duplicated here.
JS_LEDGER = """
(function () {
  var scs = Array.prototype.slice.call(
    document.querySelectorAll('[data-saudit-sc]'));
  window.__i = 0;
  window.__step = function () {
    if (window.__i >= scs.length) { return 'done'; }
    var sc = scs[window.__i];
    var id = sc.getAttribute('data-saudit-sc');
    sc.click();
    var clear = document.querySelector('[data-saudit-clear]');
    if (clear) { clear.click(); }
    sc.click();
    Array.prototype.slice.call(
      document.querySelectorAll('[data-saudit-chip]')).forEach(function (c) {
        var side = (c.getAttribute('data-saudit-chip') || '').split(':')[0];
        var want = c.getAttribute('data-saudit-want-' + id);
        var on = c.getAttribute('aria-pressed') === 'true';
        var should = (want === side);
        if (should !== on) { c.click(); }
      });
    var chk = document.querySelector('[data-saudit-check]');
    if (chk) { chk.click(); }
    window.__i += 1;
    return window.__i;
  };
  return scs.length;
})()
"""

JS_STEP = "window.__step()"

JS_STAGES = """
(function () {
  return Array.prototype.slice.call(
    document.querySelectorAll('[data-instrument]')).map(function (s) {
      return {id: s.id || (s.className || '').split(' ')[0],
              done: s.getAttribute('data-stage-done')};
    });
})()
"""


def main(only=None):
    server, port = cdp.serve(HERE)
    problems, rows = [], []
    try:
        for slug, drives in DRIVES.items():
            if only and only not in slug:
                continue
            url = "http://127.0.0.1:%d/%s/%s.html" % (port, DIR, slug)
            with cdp.Browser().start() as b:
                page = b.page(url)
                before = page.eval(JS_STAGES)
                if any(s["done"] == "1" for s in before):
                    problems.append("%s: a stage was ticked BEFORE the drive" % slug)

                for name, steps, pause in drives:
                    for sel, mode in steps:
                        if sel == "__ledger__":
                            n = page.eval(JS_LEDGER)
                            for _ in range(int(n)):
                                page.eval(JS_STEP)
                                time.sleep(0.35)
                        elif sel == "__pairs_run__":
                            n = page.eval(JS_PAIRS_RUN)
                            for _ in range(int(n)):
                                page.eval(JS_STEP)
                                time.sleep(1.4)
                        elif sel == "__rods_run__":
                            n = page.eval(JS_RODS_RUN)
                            for _ in range(int(n)):
                                page.eval(JS_STEP)
                                time.sleep(1.4)
                        elif sel == "__ice_run__":
                            page.eval(JS_ICE_RUN)
                            time.sleep(3.0)
                        else:
                            page.eval(JS_CLICK % (repr(sel), repr(mode)))
                            time.sleep(pause)

                time.sleep(0.6)
                after = page.eval(JS_STAGES)
                ticked = sum(1 for s in after if s["done"] == "1")
                rows.append((slug, ticked, len(after)))
                for s in after:
                    if s["done"] != "1":
                        problems.append(
                            "%s: instrument %r never reached done — the rail "
                            "stop it carries can be shown but not earned"
                            % (slug, s["id"]))
                # ⚠️ ENVIRONMENTAL, NOT A PAGE DEFECT. `mrbadmus.v2.js` pings
                # the production backend for a health check; from a local
                # server that is a cross-origin request the backend does not
                # allow, so it fails on EVERY KS3 page under this harness and
                # would fail identically on an unmodified checkout. Filtered
                # by signature rather than by silencing the check.
                errs = [e for e in page.console_errors()
                        if "api/health" not in str(e)
                        and "CORS" not in str(e)]
                if errs:
                    problems.append("%s: console error(s): %s" % (slug, errs[:2]))
    finally:
        server.shutdown()
        _swept = _sweep_chrome_tmp()
        if _swept:
            print("swept %d stale Chrome temp entries" % _swept)

    print("\n" + "=" * 70)
    for slug, t, n in rows:
        print("  %-36s %d/%d instrument(s) reached done" % (slug, t, n))
    print("=" * 70)
    if problems:
        print("\n%d PROBLEM(S):" % len(problems))
        for p in problems:
            print("  - %s" % p)
        return 1
    print("\n✅ every P1 instrument reached done under a student-shaped "
          "sequence, and none was ticked before the drive.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else None))
