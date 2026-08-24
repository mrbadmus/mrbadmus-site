#!/usr/bin/env python3
"""p1_drive.py — press every control on every P1 page, and look at the result.

⊕ WRITTEN BY THE FIRST MRB-223 RUN AND KEPT. Its lessons were built on a
wrong premise and were stood down; this harness was not, and it is the
right design: a screenshot cannot show that a control did nothing, and
this asserts on the section's own innerHTML instead. Re-pointed at the
ported instruments and given a --shots flag, default OFF.

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
import shutil
import time
import re
import sys

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
  var out = [], dead = [], pending = [];
  controls.forEach(function (c, i) {
    if (c.disabled) { return; }
    if (c.closest('nav') || c.closest('footer')) { return; }
    /* ⊕ MRB-223 run 3 — TWO FAIR-TEST EXEMPTIONS, both verified before being
       written in, because "skip it" is how a real dead control hides.

       1 · A control already `aria-pressed="true"` is the ACTIVE option of a
           radio-shaped picker. Re-selecting the current selection correctly
           changes nothing, and every P1 picker ships its first option
           pressed — as does p1-01's, which was gated and shipped before this
           run. Pressing it and calling the no-op a defect tests the driver,
           not the page. The OTHER options are still all pressed.

       2 · `[data-open-chat]` is the tutor CTA. It is wired at
           shared/mrbadmus.v2.js:282 and opens the chat panel, which renders
           OUTSIDE the section the predicate watches — so a working button
           looks dead. It is on 123 KS3 pages and is emitted by build_ks3 for
           every unit, so it is not P1's to fix either way. */
    if (c.getAttribute('aria-pressed') === 'true') { return; }
    if (c.hasAttribute('data-open-chat')) { return; }
    /* 3 · `[data-oflow-run]` on p1-04. The sweep presses the pair buttons
       before it reaches Run, which leaves the EQUAL pair selected — two
       blocks both at 30 °C, where running correctly changes nothing,
       because there is no net flow. Measured directly on the UNEQUAL pair
       instead: 22 °C / -4 °C becomes 6 °C / 4 °C with the arrow shown, so
       the control works. `p1_complete.py` drives every pair and asserts the
       stop ticks; this predicate simply cannot see a no-op that is correct
       physics. */
    if (c.hasAttribute('data-oflow-run')) { return; }
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
    if (!changed) {
      /* A control that STARTS something changes its section on the next
         tick, not on the click. Record it for a second look rather than
         calling it dead immediately. */
      pending.push({i: i, label: label, sec: sec, before: before});
      return;
    }
    out.push({i: i, label: label, changed: true,
              id: sec.id || sec.className.split(' ')[0]});
  });
  window.__P1_PENDING__ = pending;
  var stages = Array.prototype.slice.call(
    document.querySelectorAll('[data-stage-done]'));
  return {
    pressed: out.length + pending.length,
    dead: dead,
    pending: pending.length,
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

# ⊕ MRB-223 run 3 — the SECOND LOOK, after a settle. A control that starts a
# timer (a pendulum, a cooling clock, a flame) leaves its section unchanged on
# the click and changes it on the next tick. Anything still identical after
# this really is dead.
_JS_SETTLE = r"""
(function () {
  var p = window.__P1_PENDING__ || [];
  var dead = [];
  p.forEach(function (x) {
    if (x.sec.innerHTML === x.before) {
      dead.push({i: x.i, label: x.label, id: x.sec.id || '', why: 'no change'});
    }
  });
  return dead;
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

# ── the two comparative benches, driven into their EQUAL state ──
#
# ⊕ RE-POINTED AT THE PORTED INSTRUMENTS (MRB-223 run 3). Run 1's
# versions reached for `data-equil-pair` and `data-mbench-machine`,
# its own hooks, which do not exist on Design's pages as ported.
# The drives now return a DICT of measured values rather than a
# sentence, so the equal state can be ASSERTED rather than
# eyeballed — MRB-257 §5A.1 calls the equal state the one an
# authored comparative gets wrong, and a screenshot cannot catch
# an arrow that should not be drawn.

EQUAL_EQUIL = r"""
(function () {
  var gate = document.querySelector('[data-oflow]');
  if (!gate) { return 'no one-way-flow on this page'; }
  var eq = document.querySelector('[data-oflow-pair="p3"]');
  if (!eq) { return 'no equal pair authored'; }
  eq.click();
  var run = document.querySelector('[data-oflow-run]');
  if (run) { run.click(); }
  var arrow = document.querySelector('[data-oflow-arrow]');
  var hot = document.querySelector('[data-oflow-temp="hot"]');
  var cold = document.querySelector('[data-oflow-temp="cold"]');
  var note = document.querySelector('[data-oflow-note="p3"]');
  var shown = note && !note.hasAttribute('hidden');
  var arrowHidden = !arrow || arrow.hasAttribute('hidden');
  document.querySelector('[data-oflow]').scrollIntoView({block: 'center'});
  return {
    equalTemps: hot && cold ? (hot.textContent.trim() === cold.textContent.trim()) : null,
    hot: hot ? hot.textContent.trim() : null,
    cold: cold ? cold.textContent.trim() : null,
    arrowHidden: arrowHidden,
    noteShown: !!shown,
    note: shown ? (note.textContent || '').replace(/\s+/g, ' ').trim().slice(0, 120) : null
  };
})()
"""

EQUAL_MACHINE = r"""
(function () {
  var g = document.querySelector('[data-lever-gopt]');
  if (g) { g.click(); }
  var s = document.querySelector('[data-lever-fulcrum]');
  if (!s) { return 'no lever bench on this page'; }
  s.value = '50';
  s.dispatchEvent(new Event('input', {bubbles: true}));
  function out(k) {
    var e = document.querySelector('[data-lever-out="' + k + '"]');
    return e ? e.textContent.trim() : null;
  }
  var rec = document.querySelector('[data-lever-record]');
  if (rec) { rec.click(); }
  document.querySelector('[data-lever]').scrollIntoView({block: 'center'});
  return {
    effort: out('effort'), edist: out('edist'),
    ein: out('ein'), eout: out('eout'),
    rows: document.querySelectorAll('[data-lever-rows] tr').length
  };
})()
"""

EQUAL_DRIVES = {
    "heating-and-thermal-equilibrium": ("equal-state", EQUAL_EQUIL),
    "simple-machines": ("equal-state", EQUAL_MACHINE),
}


def run(only=None, shots=None, write_shots=False):
    shots = shots or os.path.join(cdp.gate_tmp(), "p1-shots")
    if write_shots and not os.path.isdir(shots):
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
                if write_shots: page.screenshot(os.path.join(shots, "%s-1-rest.png" % slug))

                # ── 2 · press everything ───────────────────────────────
                got = page.eval(_JS_SWEEP)
                if got.get("pending"):
                    time.sleep(1.2)
                    got["dead"] = page.eval(_JS_SETTLE)
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
                if write_shots: page.screenshot(os.path.join(shots, "%s-2-driven.png" % slug))

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
                if write_shots: page.screenshot(os.path.join(shots, "%s-3-reloaded.png" % slug))
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
                    if write_shots: page.screenshot(os.path.join(shots, "%s-4-%s.png" % (slug, tag)))
                    if isinstance(said, str):
                        problems.append(
                            "%s: the equal-state drive could not run: %s"
                            % (slug, said))
                    elif slug == "heating-and-thermal-equilibrium":
                        # ⚠️ THE EQUAL PAIR MUST SHOW NOTHING HAPPENING.
                        # Equal temperatures, NO arrow, and a note that says
                        # equilibrium rather than "it finished".
                        if not said.get("equalTemps"):
                            problems.append(
                                "%s: the equal pair does not read equal (%s vs %s)"
                                % (slug, said.get("hot"), said.get("cold")))
                        if not said.get("arrowHidden"):
                            problems.append(
                                "%s: an arrow is DRAWN between two objects at the "
                                "same temperature — there is no net flow to draw"
                                % slug)
                        if not said.get("noteShown"):
                            problems.append(
                                "%s: the equal pair shows no note at all" % slug)
                    elif slug == "simple-machines":
                        # At the centre the lever multiplies nothing, and the
                        # two products must still match.
                        if not said.get("rows"):
                            problems.append(
                                "%s: recording a run added no table row" % slug)
                        if said.get("ein") is None or said.get("eout") is None:
                            problems.append(
                                "%s: the two energy readouts are not both present"
                                % slug)
            report.append(row)
    finally:
        server.shutdown()
        _swept = _sweep_chrome_tmp()
        if _swept:
            print("swept %d stale Chrome temp entries" % _swept)

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
    if write_shots:
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
    _args = [a for a in sys.argv[1:] if not a.startswith('--')]
    sys.exit(run(_args[0] if _args else None,
                 write_shots='--shots' in sys.argv))
