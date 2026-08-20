#!/usr/bin/env python3
"""ks3_instrument_liveness.py — does the instrument actually DO anything?

    python3 ks3_instrument_liveness.py            # every registered unit
    python3 ks3_instrument_liveness.py C3         # one unit

── Why this exists ──────────────────────────────────────────────────────

An instrument fails in a way that looks like success. The markup renders, the
buttons are there, the colours are right, the page passes parity and passes
overflow and passes contrast — and nothing happens when a student presses the
button, because the marker attribute never reached the dispatch list in
`wireInstruments`, or the wire function threw on the way in.

Every other KS3 gate measures the page AT REST. This one presses the buttons.

The check is deliberately generic rather than per-instrument: for each marker
block on the page, find the controls inside it, click the first one that looks
like a control, and assert the block's own DOM changed. A wired instrument
responds to its own controls. A dead one is inert, and inert is exactly what
you cannot see in a screenshot.

It also fails on any console error raised during load, because a wire function
that throws takes every instrument after it in the dispatch list down with it —
which is the failure mode that hurts most and shows least.
"""

import sys

import ks3_browser as cdp

# One entry per instrument family: the marker attribute, and the unit it
# belongs to. A family that reaches the dispatch table but not this list is
# untested, so adding an instrument means adding a line here.
INSTRUMENTS = [
    # ── C3 · Mixtures and separation (MRB-272) ──
    ("C3", "data-psortblock",    "purity-sorter"),
    ("C3", "data-dlabblock",     "dissolve-lab"),
    ("C3", "data-seqblock",      "sequence-rebuild"),
    ("C3", "data-crystblock",    "crystal-bench"),
    ("C3", "data-mchoiceblock",  "method-choice"),
    ("C3", "data-stillblock",    "still-run"),
    ("C3", "data-chromablock",   "chroma-run"),
    ("C3", "data-critiqueblock", "plan-critique"),
    ("C3", "data-mpbblock",      "melting-point-bench"),
]

UNIT_DIRS = {
    "C3": "ks3/chemistry/mixtures-and-separation",
}

# Press the first thing inside the block that a student could press. Buttons
# first, then the radio/option controls the KS3 instruments use.
#
# ⚠️ SOME INSTRUMENTS ARE DELIBERATELY LOCKED, and an unlock is not a defect.
# C3's dissolving bench ships `hidden` behind `data-dlab-lock`, which names a
# PREDICT BLOCK elsewhere on the page: answer that and the bench arrives in the
# space the question was occupying (`ks3.js:17708`). A liveness check that
# cannot tell "locked" from "dead" reports every gated instrument as broken and
# is worse than no check at all — so this opens the gates first, by answering
# one option in every other activity block on the page, and only then presses
# the instrument's own controls.
PROBE = """
(function (sel) {
  function visible(c) {
    if (c.disabled) return false;
    var box = c.getBoundingClientRect();
    return !!(box.width || box.height);
  }
  var blocks = document.querySelectorAll('[' + sel + ']');
  if (!blocks.length) return { found: 0 };

  // Open any gate. An option click is what `openBench` and its siblings listen
  // for; answering a question the student would answer anyway is not cheating
  // the gate, it is reaching the instrument.
  var unlocked = 0;
  for (var b = 0; b < blocks.length; b++) {
    var blk = blocks[b];
    var box = blk.getBoundingClientRect();
    if (box.width || box.height) continue;              // already open
    var gates = document.querySelectorAll('[data-activity]');
    for (var g = 0; g < gates.length; g++) {
      if (gates[g].contains(blk) || blk.contains(gates[g])) continue;
      var opt = gates[g].querySelector('.ks3-option');
      if (opt && visible(opt)) { try { opt.click(); unlocked++; } catch (e) {} }
    }
  }

  var out = [];
  for (var b2 = 0; b2 < blocks.length; b2++) {
    var block = blocks[b2];
    var before = block.innerHTML;
    var controls = block.querySelectorAll(
      'button, [role="button"], input, select, [data-opt], .ks3-option, [tabindex]');
    var clicked = null, changed = false, tried = 0;
    for (var i = 0; i < controls.length; i++) {
      var c = controls[i];
      if (!visible(c)) continue;
      tried++;
      clicked = (c.tagName + (c.className ? '.' + String(c.className).split(' ')[0] : ''));
      try { c.click(); } catch (e) { return { error: String(e) }; }
      if (block.innerHTML !== before) { changed = true; break; }
    }
    out.push({
      controls: controls.length,
      reachable: tried,
      clicked: clicked,
      changed: changed,
      unlocked: unlocked,
      open: !!(block.getBoundingClientRect().width || block.getBoundingClientRect().height)
    });
  }
  return { found: blocks.length, blocks: out };
})(%s)
"""


def main():
    only = sys.argv[1].upper() if len(sys.argv) > 1 else None
    wanted = [i for i in INSTRUMENTS if only is None or i[0] == only]
    if not wanted:
        raise SystemExit("no instruments registered for unit %r" % only)

    print("\n🔌  ks3_instrument_liveness — pressing the buttons\n")

    server, port = cdp.serve(".")
    failures = []
    try:
        with cdp.Browser() as b:
            for unit in sorted({i[0] for i in wanted}):
                import os
                d = UNIT_DIRS[unit]
                pages = sorted(p for p in os.listdir(d)
                               if p.endswith(".html") and p != "index.html")
                # marker -> the page(s) that carry it
                where = {}
                for p in pages:
                    src = open(os.path.join(d, p), encoding="utf-8").read()
                    for u, marker, name in wanted:
                        if u == unit and marker in src:
                            where.setdefault(marker, []).append(p)

                print("     %s — %d page(s)\n" % (unit, len(pages)))
                seen_console = set()
                for u, marker, name in [i for i in wanted if i[0] == unit]:
                    hosts = where.get(marker, [])
                    if not hosts:
                        failures.append("%s/%s — marker %s appears on NO built "
                                        "page: the instrument is not emitted"
                                        % (unit, name, marker))
                        print("       ❌ %-22s marker on no page" % name)
                        continue
                    for host in hosts:
                        page = b.page("http://127.0.0.1:%d/%s/%s" % (port, d, host))
                        errs = [e for e in page.console_errors()
                                if e not in seen_console]
                        seen_console.update(errs)
                        res = page.eval(PROBE % repr(marker))
                        if errs:
                            failures.append("%s/%s on %s — console error during "
                                            "load: %s" % (unit, name, host, errs[0]))
                            print("       ❌ %-22s console error on %s"
                                  % (name, host))
                            continue
                        if res.get("error"):
                            failures.append("%s/%s on %s — clicking threw: %s"
                                            % (unit, name, host, res["error"]))
                            print("       ❌ %-22s threw on click" % name)
                            continue
                        blocks = res.get("blocks") or []
                        dead = [i for i, blk in enumerate(blocks)
                                if not blk.get("changed")]
                        if not blocks:
                            failures.append("%s/%s on %s — no block found at "
                                            "runtime" % (unit, name, host))
                            print("       ❌ %-22s no block at runtime" % name)
                        elif dead:
                            for i in dead:
                                blk = blocks[i]
                                failures.append(
                                    "%s/%s on %s — block %d is INERT: %d control(s), "
                                    "%d reachable, %d gate(s) opened, block %s, "
                                    "clicked %s, DOM unchanged. The marker renders "
                                    "and nothing responds."
                                    % (unit, name, host, i + 1, blk["controls"],
                                       blk.get("reachable", 0), blk.get("unlocked", 0),
                                       "visible" if blk.get("open") else "STILL HIDDEN",
                                       blk.get("clicked")))
                            print("       ❌ %-22s INERT on %s (%d/%d block(s))"
                                  % (name, host, len(dead), len(blocks)))
                        else:
                            print("       ✅ %-22s %s  (%d block(s) responded)"
                                  % (name, host, len(blocks)))
    finally:
        server.shutdown()

    print()
    if failures:
        print("     ❌ %d failure(s):\n" % len(failures))
        for f in failures:
            print("        · " + f)
        print()
        return 1
    print("     ✅ every registered instrument responded to its own controls.\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
