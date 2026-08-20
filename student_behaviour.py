#!/usr/bin/env python3
"""student_behaviour.py — the ported pages driven against Design's own.

    python3 student_behaviour.py

Exit 0 clean, 1 on any divergence.

── What this proves, and why nothing else does ──────────────────────────

`student_parity.py` establishes that the ported page renders the same DOM as
Design's at rest. That is necessary and it says nothing at all about
behaviour: a page with every handler unbound is byte-identical at rest.

RULED 20 Aug 2026: Design's logic is ported to vanilla JavaScript rather than
shipped as a React bundle. The logic class itself is Design's, extracted
verbatim — so what can break is not the computation but the RUNTIME under it:
`setState` not re-rendering, an `onClick` bound to the wrong scope inside an
`sc-for`, a ref never filled, `componentDidUpdate` called without prevProps.
Every one of those leaves a page that looks perfect and does nothing, or does
the wrong thing on the third click.

So this drives BOTH FILES THROUGH THE SAME SEQUENCE and compares what each
becomes. Design's file is the oracle; nothing is compared against a recorded
constant, because a constant is a claim about the past.

⚠️ EVERY DRIVE ENDS IN AN ASSERTION ABOUT VISIBLE TEXT, not about internal
state. A test that reads `logic.state` would pass on a page whose render is
broken, which is the failure this exists to catch.
"""

import json
import os
import sys
import time

REF = os.path.join("docs", "ks3", "design-reference", "student")
SITE = "mrbadmus_site"

PAIRS = [
    dict(name="class view",
         design="standalone/MrBadmusAI Class View.html",
         ported="student/class-ported.html"),
    dict(name="assignment",
         design="standalone/MrBadmusAI Assignment.html",
         ported="student/assignment-ported.html"),
]

VIEWPORT = (1460, 1200)

# ── the drives ────────────────────────────────────────────────────────────
#
# Each is (label, [steps]). A step is one of:
#   ("click", "Button label")      click the first control whose text matches
#   ("clickAt", "prefix", n)       the nth control whose text STARTS WITH prefix
#   ("has", "substring")           the first control CONTAINING that text
#   ("opt", n)                     the nth recall/assignment option
#   ("wait", seconds)
#
# The list is Design's §9 "Every interaction", walked. Where a drive needs a
# control that only exists after another drive, the sequence carries both —
# these are journeys, not unit tests, because the bug this is looking for is
# state that goes wrong on the third click and not on the first.
DRIVES = {
    "class view": [
        ("the account sheet opens", [("has", "AY")]),
        ("a work tab filters", [("click", "MARKED 3")]),
        ("a second work tab filters", [("click", "MARKED 3"), ("click", "TO DO 2")]),
        ("a week bar filters the spine", [("click", "03")]),
        ("SHOW ALL 12 WEEKS clears it",
         [("click", "03"), ("click", "SHOW ALL 12 WEEKS")]),
        ("the composed filters empty the list and offer Clear filters",
         [("click", "MARKED 3"), ("click", "02")]),
        ("a bench task ticks and the meter moves",
         [("click", "Answer the eight questions")]),
        ("two bench tasks tick",
         [("click", "Answer the eight questions"), ("click", "Hand it in")]),
        ("a leaderboard week chip", [("click", "W02")]),
        ("the term chip", [("click", "TERM")]),
        ("SHOW TOP 10", [("click", "SHOW TOP 10")]),
        ("a work row expands", [("clickAt", "03\nAnimal and plant cells", 0)]),
        ("recall opens", [("click", "Recall")]),
        ("recall · pick an option", [("click", "Recall"), ("opt", 0)]),
        ("recall · Check reveals the answer and the feedback",
         [("click", "Recall"), ("opt", 0), ("click", "Check")]),
        ("recall · Next question moves on",
         [("click", "Recall"), ("opt", 0), ("click", "Check"),
          ("click", "Next question")]),
        ("recall · Skip breaks the streak",
         [("click", "Recall"), ("click", "Skip")]),
        ("recall · six answers reach the round card",
         [("click", "Recall")] +
         sum([[("opt", 0), ("click", "Check"), ("click", "Next question")]
              for _ in range(6)], [])),
        ("recall · back to the class", [("click", "Recall"), ("click", "My class")]),
    ],
    "assignment": [
        ("an option is selected but not confirmed", [("opt", 0)]),
        ("Confirm answer marks it",
         [("opt", 0), ("click", "Confirm answer")]),
        ("a confirmed question is locked to a second confirm",
         [("opt", 0), ("click", "Confirm answer"), ("opt", 1)]),
        ("Back navigates", [("click", "Back")]),
        ("Next navigates", [("click", "Next")]),
        ("Back then Next returns", [("click", "Back"), ("click", "Next")]),
        ("a marker jumps to its question", [("click", "12")]),
        ("the figure enlarges in place", [("has", "TAP TO ENLARGE")]),
        ("answer, then navigate away and back, keeps the mark",
         [("opt", 0), ("click", "Confirm answer"), ("click", "Back"),
          ("click", "Next")]),
    ],
}

_CLICK = """(function (label) {
  var r = document.querySelector('.rd[data-mode="ks3"]');
  var hit = null;
  r.querySelectorAll('button,a').forEach(function (e) {
    if (!hit && (e.innerText || '').replace(/\\s+/g, ' ').trim() === label) {
      hit = e;
    }
  });
  if (!hit) { return 'MISS'; }
  hit.click(); return 'ok';
})(%s)"""

_CLICK_AT = """(function (prefix, n) {
  var r = document.querySelector('.rd[data-mode="ks3"]');
  var found = [];
  r.querySelectorAll('button,a').forEach(function (e) {
    if ((e.innerText || '').indexOf(prefix) === 0) { found.push(e); }
  });
  if (found.length <= n) { return 'MISS'; }
  found[n].click(); return 'ok';
})(%s, %d)"""

# ⚠️ THE FIGURE IS NOT AN OPTION, and it looked exactly like one. Six of the
# assignment's questions carry a figure with A–D label discs drawn on it, so
# the figure button's `innerText` BEGINS `A\nB\nC\nD\nFIGURE · …` and matched a
# naive `/^[ABCD]\n/`. It sorts first in document order, so every assignment
# drive clicked the figure and then asserted that nothing had happened —
# against a Design file where nothing had happened either. Five drives reported
# "cannot be performed on Design's own file", which was true and was this
# selector's fault.
#
# The line count is what separates them: an option is a letter chip and its
# text, so two lines; the figure is six. Checked both ways, because "does not
# contain FIGURE" alone would break on a question about figures.
_OPT = """(function (n) {
  var r = document.querySelector('.rd[data-mode="ks3"]');
  var opts = [].slice.call(r.querySelectorAll('button')).filter(function (e) {
    var t = (e.innerText || '').trim();
    if (!/^[ABCD]\\n/.test(t)) { return false; }
    return t.split('\\n').length <= 3 && t.indexOf('TAP TO ENLARGE') === -1;
  });
  if (opts.length <= n) { return 'MISS'; }
  opts[n].click(); return 'ok';
})(%d)"""

# A control identified by a substring of its text rather than the whole of it —
# for the avatar, whose label is `AY\nAyo` at desktop and `AY` below, and for
# the figure, whose caption row is a span inside the button.
_CLICK_CONTAINS = """(function (needle) {
  var r = document.querySelector('.rd[data-mode="ks3"]');
  var hit = null;
  r.querySelectorAll('button,a').forEach(function (e) {
    if (!hit && (e.innerText || '').indexOf(needle) > -1) { hit = e; }
  });
  if (!hit) { return 'MISS'; }
  hit.click(); return 'ok';
})(%s)"""

# What is compared after every drive. Visible text and the control census —
# text catches a wrong value, the census catches a control that appeared or
# vanished when it should not have.
_STATE = r"""(function () {
  var r = document.querySelector('.rd[data-mode="ks3"]');
  if (!r) { return JSON.stringify({error: 'no design root'}); }
  var ctl = [];
  r.querySelectorAll('button,a').forEach(function (e) {
    var cs = getComputedStyle(e);
    if (cs.display === 'none' || cs.visibility === 'hidden') { return; }
    ctl.push((e.innerText || '').replace(/\s+/g, ' ').trim());
  });
  return JSON.stringify({
    error: '',
    text: (r.innerText || '').replace(/\s+/g, ' ').trim(),
    nodes: r.querySelectorAll('*').length,
    controls: ctl
  });
})()"""


def drive(page, steps):
    """Run one drive. Returns a list of steps that could not be performed."""
    missed = []
    for step in steps:
        kind = step[0]
        if kind == "click":
            got = page.eval(_CLICK % json.dumps(step[1]))
        elif kind == "clickAt":
            got = page.eval(_CLICK_AT % (json.dumps(step[1]), step[2]))
        elif kind == "has":
            got = page.eval(_CLICK_CONTAINS % json.dumps(step[1]))
        elif kind == "opt":
            got = page.eval(_OPT % step[1])
        elif kind == "wait":
            time.sleep(step[1])
            continue
        else:
            raise SystemExit("student_behaviour: unknown step %r" % (step,))
        if got == "MISS":
            missed.append(step)
        time.sleep(0.35)
    return missed


def run_one(cdp, root, path, drives):
    """Every drive, each from a fresh load. Returns {label: state}."""
    out = {}
    server, port = cdp.serve(root)
    url = "http://127.0.0.1:%d/%s" % (port, path.replace(" ", "%20"))
    try:
        with cdp.Browser() as b:
            page = b.attach()
            page.set_viewport(*VIEWPORT)
            for label, steps in drives:
                # ⚠️ A FRESH LOAD PER DRIVE. Running them in sequence would
                # make every assertion depend on every drive before it, and the
                # first divergence would then paint all the rest red without
                # any of them being wrong.
                page.goto(url)
                time.sleep(2.6)
                missed = drive(page, steps)
                time.sleep(0.5)
                st = json.loads(page.eval(_STATE))
                st["missed"] = [list(m) for m in missed]
                out[label] = st
    finally:
        server.shutdown()
    return out


def run(cdp):
    rows, problems = [], []
    for pair in PAIRS:
        name = pair["name"]
        drives = DRIVES[name]
        d = run_one(cdp, REF, pair["design"], drives)
        g = run_one(cdp, SITE, pair["ported"], drives)

        for label, _steps in drives:
            ds, gs = d[label], g[label]

            # A drive that could not be performed on DESIGN's file is a broken
            # drive, not a broken port, and it is reported as such — otherwise
            # a typo in a button label reads as a behavioural divergence.
            if ds["missed"]:
                problems.append(
                    "%s — the drive %r could not be performed on DESIGN's own "
                    "file: %s. That is this file's bug, not the port's; fix "
                    "the step." % (name, label, ds["missed"]))
                rows.append((name, label, "FAIL",
                             "the drive does not work on Design's file"))
                continue

            if gs["missed"]:
                problems.append(
                    "%s — %r: %d step(s) that work on Design's file cannot be "
                    "performed on the ported page: %s. A control that is on "
                    "the page and does not respond is the exact failure a "
                    "rendering-only parity gate cannot see."
                    % (name, label, len(gs["missed"]), gs["missed"]))
                rows.append((name, label, "FAIL",
                             "%d step(s) found no control" % len(gs["missed"])))
                continue

            same_text = ds["text"] == gs["text"]
            same_ctl = ds["controls"] == gs["controls"]
            ok = same_text and same_ctl
            if ok:
                rows.append((name, label, "PASS",
                             "%d node(s), %d control(s), text identical"
                             % (gs["nodes"], len(gs["controls"]))))
            else:
                bits = []
                if not same_text:
                    bits.append(_first_diff(ds["text"], gs["text"]))
                if not same_ctl:
                    only_d = [c for c in ds["controls"] if c not in gs["controls"]]
                    only_g = [c for c in gs["controls"] if c not in ds["controls"]]
                    bits.append("controls only in Design: %s; only in port: %s"
                                % (only_d[:3], only_g[:3]))
                problems.append("%s — %r diverges: %s"
                                % (name, label, "; ".join(bits)))
                rows.append((name, label, "FAIL", "; ".join(bits)[:110]))
    return rows, problems


def _first_diff(a, b):
    n = min(len(a), len(b))
    for i in range(n):
        if a[i] != b[i]:
            lo = max(0, i - 30)
            return ("text diverges at char %d — Design %r, port %r"
                    % (i, a[lo:i + 40], b[lo:i + 40]))
    return "text lengths differ: Design %d, port %d" % (len(a), len(b))


def main():
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import ks3_browser as cdp

    print("── the ported pages, driven against Design's own ──")
    rows, problems = run(cdp)
    last = None
    for page, label, verdict, detail in rows:
        if page != last:
            print("\n  %s" % page)
            last = page
        print("    %-4s %-58s %s" % (verdict, label[:58], detail[:80]))

    print()
    if problems:
        print("  %d PROBLEM(S):" % len(problems))
        for p in problems:
            print("    · %s" % p)
        return 1
    print("  PASS  every drive produces the same visible text and the same "
          "controls on the ported page as on Design's own.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
