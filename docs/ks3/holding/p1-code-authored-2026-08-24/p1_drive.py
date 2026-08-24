#!/usr/bin/env python3
"""p1_drive.py — press every control on every P1 page, and look at the result.

    python3 p1_drive.py                 # all eight lessons
    python3 p1_drive.py conduction      # one, by slug fragment

⚠️ A FRESH HEADLESS CHROME PER PAGE. The KS3 canvas and rAF loops keep running
after the driver moves on, and one shared browser accumulates enough of them to
drop the DevTools socket around the twelfth page (MRB-220 §6). P1 has no rAF
loop anywhere, but the rule is the harness's and not the unit's.

WHAT IT ASSERTS, per page:

  1 · EVERY CONTROL RESPONDS. Every enabled `<button>` and every `<input
      type=range>` inside the lesson body is pressed, and the section it lives
      in must CHANGE. A control that leaves its own section byte-identical is
      dead, and dead is exactly what a screenshot cannot show. Scrolling counts
      as dead.
  2 · NO CONSOLE ERRORS, at rest and after the sweep. A wire function that
      throws takes every instrument after it in the dispatch list down with it.
  3 · THE RAIL EARNS ITS TICKS. Nothing is ticked on load; after the sweep the
      count is reported against the number of stops.
  4 · STATE SURVIVES A RELOAD WHERE IT IS MEANT TO, AND ONLY THERE. `ks3.js`
      persists exactly three things per lesson — the ladder's best score, the
      free text a student typed, and the motion preference. Instrument state
      and rail ticks are deliberately NOT persisted. So the reload check is
      two-sided: the typed work must come back, and the bench must not.

Screenshots land in `--shots`, three per page (rest, driven, reloaded) plus a
targeted capture of each comparative bench in its EQUAL state, which is the
state MRB-257 §5A.1 says an authored comparative gets wrong.
"""

import json
import os
import re
import sys

import ks3_browser as cdp

HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)

DIR = "ks3/physics/energy-transfers"
PAGES = [
    "energy-stores",
    "energy-transfers-before-and-after",
    "conservation-of-energy",
    "heating-and-thermal-equilibrium",
    "conduction",
    "radiation",
    "insulation",
    "simple-machines",
]

# ── the sweep, in the page ───────────────────────────────────────────────
#
# ⚠️ `section.innerHTML` IS THE PREDICATE, not a count of anything. A count
# says "one control was pressed before and after" on a page that changed every
# word underneath it — which is the b1-03 defect, and the reason MRB-257 §5A.5
# replaced counting with this.
_JS_SWEEP = r"""
(function () {
  function sectionOf(el) {
    var s = el.closest('section');
    return s || el.parentElement;
  }
  var main = document.querySelector('main') || document.body;
  var controls = Array.prototype.slice.call(
    main.querySelectorAll('button, input[type=range]'));
  var out = [], dead = [];
  controls.forEach(function (c, i) {
    if (c.disabled) { return; }
    if (c.closest('nav') || c.closest('footer')) { return; }
    var sec = sectionOf(c);
    if (!sec) { return; }
    var before = sec.innerHTML;
    var label = (c.textContent || '').replace(/\s+/g, ' ').trim().slice(0, 46)
              || (c.getAttribute('aria-label') || c.type || 'control');
    try {
      if (c.tagName === 'INPUT') {
        var max = parseInt(c.max, 10) || 0;
        c.value = String(max);
        c.dispatchEvent(new Event('input', {bubbles: true}));
      } else {
        c.click();
      }
    } catch (e) {
      dead.push({i: i, label: label, why: 'threw: ' + e.message});
      return;
    }
    var changed = sec.innerHTML !== before;
    out.push({i: i, label: label, changed: changed,
              id: sec.id || sec.className.split(' ')[0]});
    if (!changed) { dead.push({i: i, label: label, id: sec.id || '', why: 'no change'}); }
  });
  var stages = Array.prototype.slice.call(
    document.querySelectorAll('[data-stage-done]'));
  return {
    pressed: out.length,
    dead: dead,
    ticked: stages.filter(function (s) {
      return s.getAttribute('data-stage-done') === '1'; }).length,
    stages: stages.length,
    railStops: (function () {
      var r = document.querySelector('[data-rail-stages]');
      if (!r) { return 0; }
      try { return JSON.parse(r.getAttribute('data-rail-stages')).length; }
      catch (e) { return -1; }
    })()
  };
})()
"""

_JS_TICKED_ON_LOAD = r"""
(function () {
  var t = Array.prototype.slice.call(
    document.querySelectorAll('[data-stage-done="1"]'));
  return t.map(function (s) { return s.id || s.className; });
})()
"""

# Type into the ladder's free-text answer and answer a marked rung, so the
# reload check has something to be about.
_JS_SEED_WORK = r"""
(function () {
  var area = document.querySelector('.ks3-rung textarea, .ks3-rung input[type=text]');
  var typed = null;
  if (area) {
    area.focus();
    area.value = 'P1 DRIVE MARKER 24 AUG';
    area.dispatchEvent(new Event('input', {bubbles: true}));
    area.dispatchEvent(new Event('change', {bubbles: true}));
    area.blur();
    typed = area.value;
  }
  var opt = document.querySelector('.ks3-rung .ks3-option');
  if (opt) { opt.click(); }
  return {typed: typed, answered: !!opt};
})()
"""

_JS_AFTER_RELOAD = r"""
(function () {
  var area = document.querySelector('.ks3-rung textarea, .ks3-rung input[type=text]');
  var marked = document.querySelector(
    '.ks3-rung .ks3-option.is-correct, .ks3-rung .ks3-option.is-wrong');
  var benchOpen = !!document.querySelector(
    '[data-instrument] [data-stage-done="1"]');
  return {
    work: area ? area.value : null,
    railTicked: document.querySelectorAll('[data-stage-done="1"]').length,
    ladderMarked: !!marked,
    benchOpen: benchOpen
  };
})()
"""

# ── the two comparative benches, driven into their EQUAL state ──────────
_JS_EQUAL_EQUIL = r"""
(function () {
  var g = document.querySelector('[data-benchgate] .ks3-option');
  if (g) { g.click(); }
  var eq = document.querySelector('[data-equil-pair="equal"]');
  if (!eq) { return 'no equal pair'; }
  eq.click();
  var on = Array.prototype.slice.call(
    document.querySelectorAll('[data-equil-state]')).filter(function (n) {
      return !n.hasAttribute('hidden'); });
  if (on.length !== 1) { return on.length + ' states visible'; }
  on[0].scrollIntoView({block: 'center'});
  return (on[0].textContent || '').replace(/\s+/g, ' ').trim();
})()
"""

_JS_EQUAL_MACHINE = r"""
(function () {
  var g = document.querySelector('[data-benchgate] .ks3-option');
  if (g) { g.click(); }
  var lever = document.querySelector('[data-mbench-machine="lever"]');
  if (!lever) { return 'no lever'; }
  lever.click();
  var eq = document.querySelector('[data-mbench-setting="lever:equal"]');
  if (!eq) { return 'no 1x setting'; }
  eq.click();
  var out = document.querySelector('[data-mbench-out="lever:equal"]');
  if (!out || out.hasAttribute('hidden')) { return 'no readout'; }
  out.scrollIntoView({block: 'center'});
  return (out.textContent || '').replace(/\s+/g, ' ').trim();
})()
"""

EQUAL_DRIVES = {
    "heating-and-thermal-equilibrium": ("equal-state", _JS_EQUAL_EQUIL),
    "simple-machines": ("equal-state", _JS_EQUAL_MACHINE),
}


def run(only=None, shots=None):
    shots = shots or os.path.join(cdp.gate_tmp(), "p1-shots")
    if not os.path.isdir(shots):
        os.makedirs(shots)
    server, port = cdp.serve(HERE)
    problems, report = [], []
    pages = [p for p in PAGES if not only or only in p]
    if not pages:
        print("no page matches %r; slugs are:\n  %s" % (only, "\n  ".join(PAGES)))
        return 2
    try:
        for slug in pages:
            rel = "%s/%s.html" % (DIR, slug)
            url = "http://127.0.0.1:%d/%s" % (port, rel)
            row = {"slug": slug}

            # ── 1 · resting ────────────────────────────────────────────
            with cdp.Browser().start() as b:
                page = b.page(url)
                ticked = page.eval(_JS_TICKED_ON_LOAD)
                if ticked:
                    problems.append("%s: %d stage(s) TICKED ON LOAD: %s"
                                    % (slug, len(ticked), ticked))
                errs = page.console_errors()
                if errs:
                    problems.append("%s: %d console error(s) at rest: %s"
                                    % (slug, len(errs), errs[:2]))
                page.screenshot(os.path.join(shots, "%s-1-rest.png" % slug))

                # ── 2 · press everything ───────────────────────────────
                got = page.eval(_JS_SWEEP)
                row.update(got)
                if got["dead"]:
                    problems.append(
                        "%s: %d DEAD control(s): %s"
                        % (slug, len(got["dead"]),
                           "; ".join("%s (%s)" % (d["label"], d["why"])
                                     for d in got["dead"][:4])))
                errs = page.console_errors()
                if errs:
                    problems.append("%s: %d console error(s) after the sweep: %s"
                                    % (slug, len(errs), errs[:2]))
                page.screenshot(os.path.join(shots, "%s-2-driven.png" % slug))

                # ── 3 · seed the persisted state, then reload ──────────
                seeded = page.eval(_JS_SEED_WORK)
                page.goto(url)
                after = page.eval(_JS_AFTER_RELOAD)
                row["reload"] = after
                if seeded.get("typed") and after.get("work") != seeded["typed"]:
                    problems.append(
                        "%s: the free text a student typed did NOT survive a "
                        "reload (%r came back as %r)"
                        % (slug, seeded["typed"], after.get("work")))
                if after.get("railTicked"):
                    problems.append(
                        "%s: %d rail stage(s) came back TICKED after a reload. "
                        "Instrument progress is deliberately not persisted, so "
                        "a tick that survives is one nobody earned."
                        % (slug, after["railTicked"]))
                page.screenshot(os.path.join(shots, "%s-3-reloaded.png" % slug))
                errs = page.console_errors()
                if errs:
                    problems.append("%s: %d console error(s) after reload: %s"
                                    % (slug, len(errs), errs[:2]))

            # ── 4 · the comparative benches, in their EQUAL state ──────
            if slug in EQUAL_DRIVES:
                tag, js = EQUAL_DRIVES[slug]
                with cdp.Browser().start() as b:
                    page = b.page(url)
                    said = page.eval(js)
                    row["equal_state"] = said
                    page.screenshot(os.path.join(shots, "%s-4-%s.png" % (slug, tag)))
                    if not isinstance(said, str) or len(said) < 20:
                        problems.append(
                            "%s: the equal-state drive returned %r" % (slug, said))
            report.append(row)
    finally:
        server.shutdown()

    print("\n" + "=" * 74)
    for r in report:
        print("%-34s pressed %2d  dead %d  ticked %d/%d  rail %d"
              % (r["slug"], r.get("pressed", 0), len(r.get("dead") or []),
                 r.get("ticked", 0), r.get("stages", 0), r.get("railStops", 0)))
        if r.get("equal_state"):
            print("      EQUAL STATE: %s" % str(r["equal_state"])[:200])
        rl = r.get("reload") or {}
        print("      after reload: work=%r ladderMarked=%s railTicked=%s"
              % ((rl.get("work") or "")[:26], rl.get("ladderMarked"),
                 rl.get("railTicked")))
    print("=" * 74)
    print("screenshots: %s" % shots)
    if problems:
        print("\n%d PROBLEM(S):" % len(problems))
        for p in problems:
            print("  - %s" % p)
        return 1
    print("\n✅ every control on all %d P1 page(s) responded to its own press, "
          "no console errors, nothing ticked on load, and the persisted state "
          "survived a reload while the instrument state correctly did not."
          % len(report))
    return 0


if __name__ == "__main__":
    sys.exit(run(sys.argv[1] if len(sys.argv) > 1 else None))
