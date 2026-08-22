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

── the SECOND reference, and why it is not an oracle ────────────────────

Design has since delivered AMENDMENTS to the class view, vendored under
`docs/ks3/design-reference/class-view-amendments/`. It is tempting to point the
oracle at the newer file and be done. That is not available, and the reason is
measured rather than assumed:

  · the amended delivery carries DIFFERENT SAMPLE DATA. Its hero reads
    `WELCOME BACK, AY … SCIENCE` where the original reads
    `WELCOME BACK, AYO … BIOLOGY`; its bench reads
    `Breathing and gas exchange / 4 questions` where the original reads
    `Cells & microscopy / Eight questions`.
  · the proof that this is DATA and not DESIGN is Design's own markup. Design
    marked the hero `data-port-region="hero"` and gave it NO
    `data-port-change` — Design stating, in the file, that the hero was not
    amended — and its text differs anyway. A region Design did not touch
    cannot have diverged for any reason except its data.

So the port's rendered text can never be compared to the amended delivery's
rendered text: the comparison would report a data difference as a defect, on
every drive, forever. The original delivery stays the oracle.

What the merge legitimately ADDS to the port is Design's new CHROME — words
like `FLASHCARDS`, `BENCH THEME`, `Practise recall` — which do not vary with
data. `AMENDED_ADDITIONS` is the register for exactly those, and it is the
EXACT MIRROR of `RULED_DIVERGENCE`:

    RULED_DIVERGENCE   strips a span out of DESIGN's text  (the port removed it)
    AMENDED_ADDITIONS  strips a span out of the PORT's text (the port gained it)

Everything outside a registered span stays under the same byte-for-byte
comparison against the original delivery it has always been under.
"""

import json
import os
import sys
import time

REF = os.path.join("docs", "ks3", "design-reference", "student")
SITE = "mrbadmus_site"

# ⚠️ THE FIXTURE PAGES, NOT THE PRODUCTION ONES, and that is not a weakening.
# Since the data seam, `*-ported.html` carries no data at all: it defines
# `window.__MRB_MOUNT__`, does not call it, and ends by loading
# `shared/student-live.js`. Driving it would drive a blank page — or, once the
# live source exists, whatever the database held that morning, which is not
# something Design's file can be compared against.
#
# `*-fixture.html` is the same bytes apart from its banner and its last two
# script tags, which load Design's own extracted values and mount. So what is
# driven here is Design's markup, Design's logic and Design's data, on our
# runtime — which is exactly what this gate was always driving. The seam moved
# the data out of the page; it did not move it out of the comparison.
#
# `amended_root` / `amended` are OPTIONAL and name Design's amended delivery for
# that page — a second reference, never an oracle (see the module docstring).
# Their ABSENCE is meaningful and is the normal case: it says this page has no
# amended delivery, and every line of the additions machinery below must treat
# it as "skip", not as "missing file". The assignment has no amendments, so it
# carries neither key and never reaches any of it.
PAIRS = [
    dict(name="class view",
         design="standalone/MrBadmusAI Class View.html",
         ported="student/class-fixture.html",
         amended_root="docs/ks3/design-reference/class-view-amendments",
         amended="standalone/ks3-class-view-bench-open.html"),
    dict(name="assignment",
         design="standalone/MrBadmusAI Assignment.html",
         ported="student/assignment-fixture.html"),
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
#
# `regions` is the third reading, and it is the one an `AMENDED_ADDITIONS` entry
# is checked against. Design's amended delivery annotates its own surfaces with
# `data-port-region`, and where it changed one, `data-port-change` says so in
# Design's words. Reading them here rather than grepping the file means an
# addition is checked against what a RENDERED region actually contains, in a
# named state, which is the only thing a student ever sees.
#
# ⚠️ AN EMPTY MAP IS THE NORMAL CASE, NOT AN ERROR, and code downstream must
# never read `{}` as a failure to measure. Counted: the ORIGINAL delivery and
# both fixtures carry ZERO `data-port-region` markers — the markers are new,
# they exist only on the amended delivery, and there they number nine visible at
# rest out of fourteen drawn (the account sheet, the flashcards overlay, the
# recall round, the done bench and the reward slot sit behind a conditional).
# So on the oracle and on the port this reads `{}` today, and will keep reading
# `{}` until the merge lands Design's markers on our markup too.
#
# Hidden nodes are dropped here for the same reason they are dropped from the
# control census: `innerText` of a `display:none` subtree is empty anyway, and a
# region that is drawn but not on screen is not a region a student has reached.
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
    controls: ctl,
    regions: (function () {
      var out = {};
      r.querySelectorAll('[data-port-region]').forEach(function (e) {
        var cs = getComputedStyle(e);
        if (cs.display === 'none' || cs.visibility === 'hidden') { return; }
        var c = [];
        e.querySelectorAll('button,a').forEach(function (x) {
          var xs = getComputedStyle(x);
          if (xs.display === 'none' || xs.visibility === 'hidden') { return; }
          c.push((x.innerText || '').replace(/\s+/g, ' ').trim());
        });
        out[e.getAttribute('data-port-region')] = {
          change: e.getAttribute('data-port-change') || '',
          text: (e.innerText || '').replace(/\s+/g, ' ').trim(),
          controls: c
        };
      });
      return out;
    })()
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


def _amended_wanted(pair):
    """Whether Design's amended delivery has to be driven for this page.

    Two independent reasons not to, and both are ordinary rather than
    exceptional:

      · the page has no amended delivery at all — the assignment carries
        neither `amended_root` nor `amended`, and never will unless Design
        amends it;
      · the page has one, and NOTHING IS REGISTERED against it. An inert
        registry must not cost a browser launch. This gate already launches
        four (two pages × oracle and port) and each costs seconds; a third per
        page, to drive a file whose findings nothing would consult, would make
        the run slower for no reading at all.

    ⚠️ The second clause is what keeps this change genuinely invisible today.
    With both registries empty the amended file is never served, never loaded
    and never measured, so the run is byte-for-byte the run it was before the
    mechanism existed — which is the only honest way to add a gate to a green
    tree.
    """
    if not pair.get("amended") or not pair.get("amended_root"):
        return False
    name = pair["name"]
    return bool(AMENDED_ADDITIONS.get(name) or AMENDED_CONTROLS.get(name))


def run(cdp):
    # The self-proof first, so a machinery that cannot see never gets as far as
    # reporting clean — the same ordering `student_parity.py` uses for its
    # count scan, and for the same reason.
    rows, problems = _prove_additions()
    for pair in PAIRS:
        name = pair["name"]
        drives = DRIVES[name]
        d = run_one(cdp, REF, pair["design"], drives)
        g = run_one(cdp, SITE, pair["ported"], drives)
        amended_states = None
        if _amended_wanted(pair):
            amended_states = run_one(cdp, pair["amended_root"],
                                     pair["amended"],
                                     AMENDED_DRIVES.get(name, []))
        seen = set()

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

            d_text, ruled = _apply_ruled(
                name, ds["text"], gs["text"], problems, seen)
            rows.extend(ruled)

            d_ctl, ctl_rows = _apply_ruled_controls(
                name, ds["controls"], gs["controls"], problems, seen)
            rows.extend(ctl_rows)

            # ⚑ THE TWO MECHANISMS COMPOSE, AND THE ORDER IS THIS WAY ROUND.
            # Design's side loses its ruled spans first; the port's side then
            # loses its registered additions. They never touch the same text —
            # one edits `d_text`, the other `g_text` — so a page that both
            # removed something Design drew AND gained something Design drew
            # later ends up with two shortened strings that are still held to
            # byte-for-byte equality everywhere else.
            #
            # ⚠️ `_apply_additions` is handed `ds["text"]`, the ORACLE's text
            # BEFORE the ruled spans came out of it, and that is deliberate: it
            # asks "was this already in Design's original?", and a span that
            # was ruled away is still something Design's original said.
            g_text, add_rows = _apply_additions(
                name, ds["text"], gs["text"], gs.get("regions") or {},
                amended_states, problems, seen)
            rows.extend(add_rows)

            g_ctl, add_ctl_rows = _apply_additions_controls(
                name, ds["controls"], gs["controls"], amended_states,
                problems, seen)
            rows.extend(add_ctl_rows)

            same_text = d_text == g_text
            same_ctl = d_ctl == g_ctl
            ok = same_text and same_ctl
            if ok:
                rows.append((name, label, "PASS",
                             "%d node(s), %d control(s), text identical"
                             % (gs["nodes"], len(g_ctl))))
            else:
                # ⚠️ THE DIFF IS TAKEN ON THE STRIPPED PAIR, not on the raw
                # readings, because the stripped pair is what was compared.
                # Reporting the raw texts here would point at the first
                # REGISTERED span as though it were the defect, and send
                # whoever reads it to re-litigate a ruling that is working.
                bits = []
                if not same_text:
                    bits.append(_first_diff(d_text, g_text))
                if not same_ctl:
                    only_d = [c for c in d_ctl if c not in g_ctl]
                    only_g = [c for c in g_ctl if c not in d_ctl]
                    bits.append("controls only in Design: %s; only in port: %s"
                                % (only_d[:3], only_g[:3]))
                problems.append("%s — %r diverges: %s"
                                % (name, label, "; ".join(bits)))
                rows.append((name, label, "FAIL", "; ".join(bits)[:110]))

        rows.extend(_ruled_seen(name, seen, problems))
        rows.extend(_additions_seen(name, seen, amended_states, problems))
    return rows, problems


# ── RULED DIVERGENCES — where the port must NOT match Design's file ───────
#
# This gate's whole premise is that the port and Design's own file produce the
# same visible text. A ruling that changes the product breaks that premise, and
# there are exactly two honest ways to handle it: change the ruling, or register
# the divergence and keep asserting it. Deleting the drive is not one of them —
# that is how a gate quietly stops covering the thing it was written for.
#
# So each entry is asserted BOTH WAYS, the same shape layer D uses for the
# delivery's `--st-ok-room` violation:
#
#   · the pattern MUST match Design's own file — if Design redraws and it stops
#     matching, this registration is stale and goes red so somebody re-reads it
#   · the pattern MUST NOT match the port — if it comes back, the ruling has
#     been reverted by accident and that goes red too
#
# Only then is the matched text removed from Design's side and the rest of the
# drive compared exactly as before. Everything outside the ruled span is still
# held to byte-for-byte parity.
RULED_DIVERGENCE = {
    "class view": [
        ("the leader's ON TIME / SCORE / RECALL figures",
         r"ON TIME \d+ SCORE \d+ RECALL \d+ "),
        ("the static 40 / 40 / 20 split legend",
         r"ON TIME · 40 SCORE · 40 RECALL · 20 "),
        # ⊕ RULED 22 Aug 2026 — P7. Settings did nothing at all: an
        # `<a href="#top">` with no handler, which scrolls to the top and is
        # read by a student as the app ignoring them. Removed from the port
        # until Design's theme picker gives it a job.
        #
        # ⚠️ THIS IS THE FIRST DIVERGENCE THAT REMOVES A WORD FROM THE HEADER
        # rather than a figure from the leaderboard, so it shows on EVERY
        # class-view drive rather than on the two that reach the board. That
        # is why it is registered rather than argued about: the gate asserts
        # it both ways — still in Design's delivery, and gone from ours — so
        # if Design ever gives Settings a purpose, the first half fails and
        # this ruling gets re-read instead of quietly outliving its reason.
        #
        # ⚠️ THE TRAILING SPACE IS PART OF THE PATTERN, exactly as it is in the
        # two entries above. `_apply_ruled` deletes the match from Design's
        # text; a pattern of `Settings` alone leaves the space that separated
        # it behind, Design's side reads "Ayo  Sign out" with two spaces
        # against the port's one, and all nineteen drives go red over
        # whitespace while reporting a defect that is not there.
        ("the dead Settings control", r"Settings "),
    ],
}

# ── the same ruling, on the CONTROL list ─────────────────────────────────
#
# ⚑ TEXT AND CONTROLS ARE COMPARED SEPARATELY, AND A RULING HAS TO REACH BOTH.
#
# `RULED_DIVERGENCE` strips the ruled span out of Design's TEXT. It does
# nothing to `ds["controls"]`, which is compared as a plain list — so removing
# a control from the port passes the text half and fails the control half, with
# a message ("controls only in Design: ['Settings']") that reads like a bug.
#
# Every divergence registered until now removed FIGURES — the leader's three
# columns, the static legend — and a figure is not a control, so the gap had
# never been reached. P7 is the first ruling that removes something a student
# can press.
#
# Asserted both ways, exactly as the text is: it must be one of Design's
# controls, and it must not be one of ours.
RULED_CONTROLS = {
    "class view": ["Settings"],
}
#
# ⊕ RULED 21 Aug 2026 (MRB-275). The bar shows the TOTAL and omits the split.
# ON TIME and SCORE are computable; RECALL is not — nothing anywhere records a
# recall round, `quiz_scores` carries neither a class nor a teaching week, and
# `quiz_question_attempts` has no question_ref to resolve an answer back to a
# rung. A bar showing two of three components is a different lie from one
# showing three fabricated ones, and it is still one.
#
# The static legend goes with it for a second reason: "ON TIME · 40 / SCORE · 40
# / RECALL · 20" is a HARD-CODED string stating an apportionment the platform
# cannot compute, and it is platform self-explanation on a student page.
# "RESETS EVERY MONDAY 00:00" is deliberately KEPT — that is a fact a student
# needs in order to read the competition, not an explanation of the machinery.


def _apply_ruled(page, d_text, g_text, problems, seen):
    """Strip ruled divergences from Design's text, asserting each both ways.

    ⚠️ THE TWO HALVES ARE ASSERTED AT DIFFERENT SCOPES, and the first draft got
    this wrong by asserting both per drive. Not every drive has the leaderboard
    on screen — the six recall drives navigate away from it entirely — so
    "present in Design" is legitimately false there, and demanding it per drive
    painted twelve healthy drives red for the crime of being on another screen.

      · FORBIDDEN IN THE PORT — per drive, every drive. The ruling holds on
        every screen, so there is no state in which it may reappear.
      · PRESENT IN DESIGN — once per page, over all drives. That is what stops
        the registration rotting: if Design redraws and the pattern stops
        matching anywhere, the page-level assertion goes red.
    """
    import re
    rows = []
    for label, pat in RULED_DIVERGENCE.get(page, ()):
        if re.search(pat, d_text):
            seen.add(label)
        if re.search(pat, g_text):
            rows.append((page, "ruled · %s" % label, "FAIL", "back on the port"))
            problems.append(
                "%s — %r is BACK on the ported page. RULED 21 Aug 2026: the "
                "bar shows the total and omits the split until recall has "
                "somewhere to write (MRB-275). A bar apportioning points a "
                "student did not earn that way is a lie told in a graph."
                % (page, label))
        d_text = re.sub(pat, "", d_text)
    return d_text, rows


def _apply_ruled_controls(page, d_controls, g_controls, problems, seen):
    """Design's control list with the ruled-away controls removed.

    Same discipline as `_apply_ruled`, and the same split of scopes: forbidden
    in the port on EVERY drive, present in Design's file ONCE PER PAGE (the
    recall drives navigate away from the header, so demanding it per drive
    would paint healthy drives red — the mistake `_apply_ruled` documents).
    """
    rows = []
    ruled = RULED_CONTROLS.get(page, ())
    if not ruled:
        return d_controls, rows
    for label in ruled:
        if label in d_controls:
            seen.add("control:" + label)
        if label in g_controls:
            rows.append((page, "ruled · the %s control" % label, "FAIL",
                         "back on the port"))
            problems.append(
                "%s — the control %r is BACK on the ported page. RULED 22 Aug "
                "2026 (P7): it did nothing at all, and a button that ignores a "
                "student teaches them not to trust the others. It returns when "
                "Design's theme picker gives it a job, not before."
                % (page, label))
    return [c for c in d_controls if c not in ruled], rows


def _ruled_seen(page, seen, problems):
    """Once per page: every registered divergence was found in Design's file."""
    rows = []
    for label, _pat in RULED_DIVERGENCE.get(page, ()):
        ok = label in seen
        rows.append((page, "ruled · %s — still in the delivery" % label,
                     "PASS" if ok else "FAIL",
                     "found in Design's own file, removed from the port" if ok
                     else "NOT found in Design's file on any drive"))
        if not ok:
            problems.append(
                "%s — the ruled divergence %r was not found in DESIGN's own "
                "file on any drive. Either Design has redrawn it or the "
                "pattern has rotted; either way this registration is a claim "
                "about the past, and the port is being credited with removing "
                "something that is no longer there. Re-read the delivery."
                % (page, label))
    for label in RULED_CONTROLS.get(page, ()):
        ok = ("control:" + label) in seen
        rows.append((page, "ruled · the %s control — still in the delivery"
                     % label, "PASS" if ok else "FAIL",
                     "a control in Design's own file, gone from the port" if ok
                     else "NOT a control in Design's file on any drive"))
        if not ok:
            problems.append(
                "%s — %r is registered as a control this port removes, and it "
                "is not a control in DESIGN's own file on any drive. The "
                "registration is a claim about the past; re-read the delivery."
                % (page, label))
    return rows


# ── AMENDED ADDITIONS — where the port must NOT match Design's ORIGINAL ───
#
# ⚑ THE EXACT MIRROR OF `RULED_DIVERGENCE`, AND THE MIRROR IS THE WHOLE IDEA.
#
#   RULED_DIVERGENCE   the port REMOVED something Design drew.
#                      Strip it from DESIGN's text; assert it is still in
#                      Design's file, and gone from ours.
#   AMENDED_ADDITIONS  the port GAINED something Design drew LATER.
#                      Strip it from the PORT's text; assert it is in Design's
#                      AMENDED delivery and in the port, and that it was NOT in
#                      Design's ORIGINAL.
#
# Both leave everything outside the registered span under the same byte-for-byte
# comparison against the original delivery. Neither is a licence to stop
# comparing: a registration is a sentence about ONE span, and it is asserted
# from every side that could rot.
#
# ⚠️ WHY THIS CANNOT SIMPLY BE "COMPARE TO THE AMENDED FILE INSTEAD". Measured,
# not assumed: the amended delivery carries different SAMPLE DATA (hero
# `WELCOME BACK, AY … SCIENCE` against the original's `WELCOME BACK, AYO …
# BIOLOGY`; bench `Breathing and gas exchange / 4 questions` against
# `Cells & microscopy / Eight questions`). Design's own markup proves it is data
# and not design — the hero is marked `data-port-region="hero"` with NO
# `data-port-change`, which is Design saying in the file that the hero was not
# amended, and its text differs anyway. Repointing the oracle would therefore
# report Design's sample data as a defect on every drive, permanently, and the
# only way to keep the gate green after that is to stop comparing text. That is
# how a behaviour gate turns into a screenshot.
#
# What the merge does legitimately add is Design's new CHROME — `FLASHCARDS`,
# `BENCH THEME`, `Practise recall` — which does not vary with data, which is why
# a registered addition is a fixed pattern inside a NAMED REGION rather than a
# free-floating substring of the whole page.

# Which states of the AMENDED delivery to visit, in the shape of `DRIVES`.
#
# Several of Design's amendments sit behind a conditional and are simply not on
# screen at rest — the account sheet, the flashcards overlay, the recall round,
# the done bench — so an addition NAMES the state that reveals it, and that name
# has to be a label in here. Ships with `at rest` alone because every addition
# registered so far is visible without a click; a state lands here when the
# region that needs it is registered, and not before, because a drive nobody
# reads is a browser launch nobody needed.
AMENDED_DRIVES = {
    "class view": [("at rest", [])],
}

# ── the registry ──────────────────────────────────────────────────────────
#
# Entry shape:
#
#     label   a phrase a person would use, for the report
#     region  the `data-port-region` the addition must live inside, on BOTH
#             the amended delivery and the port
#     pat     a regex, matched against that region's text
#     state   the AMENDED_DRIVES label that reveals it (default "at rest")
#     why     a sentence. Required.
#
# ⚠️ `why` IS NOT DECORATION AND IS NOT OPTIONAL. Every entry here removes text
# from the port's side of the only comparison that can see a runtime defect, and
# in six months the only defence against somebody widening a pattern to make a
# red gate green is a sentence saying what the span is FOR. `RULED_DIVERGENCE`
# earned its reasons in comments; this one carries them in the data, because
# this registry is expected to grow with the merge and comments drift out of
# line with entries in a way a required field cannot.
#
# ⚠️ THE PATTERN'S TRAILING SPACE MATTERS, for exactly the reason spelled out on
# `RULED_DIVERGENCE`'s Settings entry: the match is DELETED from the port's
# text, so a pattern that stops short of the separating space leaves a double
# space behind, and every drive on the page goes red over whitespace while
# reporting a defect that is not there.
#
# SHIPPING EMPTY, deliberately. The mechanism lands before the merge does, so
# that the first addition is a one-line registration reviewed on its own rather
# than a gate rewritten under deadline alongside the change it is meant to
# police. An empty registry costs nothing at all — `run()` will not even launch
# a browser for the amended delivery until something is registered.
AMENDED_ADDITIONS = {
    "class view": [],
}

# ── the same registry, on the CONTROL list ────────────────────────────────
#
# ⚑ TEXT AND CONTROLS ARE COMPARED SEPARATELY, AND A REGISTRATION HAS TO REACH
# BOTH. This is not a new lesson; it is `RULED_CONTROLS`' lesson, read in the
# mirror. Stripping `FLASHCARDS` out of the port's TEXT does nothing to
# `gs["controls"]`, which is compared as a plain list — so an addition that a
# student can press passes the text half and fails the control half, with a
# message ("controls only in port: ['FLASHCARDS']") that reads like a bug in the
# port rather than a gap in the registration.
#
# Entry shape: `label`, `region`, `control` (the EXACT control text, as the
# census renders it — whitespace-collapsed and trimmed, not a substring),
# `state`, `why`.
AMENDED_CONTROLS = {
    "class view": [],
}

# The keys `seen` is stamped with. Named once rather than spelled inline in four
# places, because a typo in one of them is a silent PASS — the page-level
# assertion would look for a key nothing ever writes, find it missing, and
# report the registration stale when the registration is fine.
_ADD_IN_AMENDED = "added-in-amended:"
_ADD_IN_PORT = "added-in-port:"
_ADD_IN_ORIGINAL = "added-was-already-there:"
_ADD_CTL_IN_AMENDED = "added-control-in-amended:"
_ADD_CTL_IN_PORT = "added-control-in-port:"
_ADD_CTL_IN_ORIGINAL = "added-control-was-already-there:"


def _amended_region(amended_states, add):
    """The rendered `{change, text, controls}` of an addition's region, or None.

    Returns None for both ways of missing it — the named state was never driven,
    or the named region is not on screen in it — because the caller reports them
    with the same sentence: the registration does not describe the delivery any
    more.
    """
    st = (amended_states or {}).get(add.get("state", "at rest"))
    if not st:
        return None
    return (st.get("regions") or {}).get(add["region"])


def _apply_additions(page, d_text, g_text, g_regions, amended_states,
                     problems, seen):
    """Strip registered additions from the PORT's text, asserting each 3 ways.

    ⚠️ THE SCOPES ARE SPLIT EXACTLY AS `_apply_ruled` SPLITS THEM, and for the
    identical reason — the mistake that function's docstring records is the
    mistake this one would otherwise repeat. Not every drive reaches every
    surface: the six recall drives navigate away from the sidebar entirely, so
    "the addition is present" is legitimately false there, and demanding it per
    drive would paint twelve healthy drives red for the crime of being on
    another screen.

      · STRIPPED FROM THE PORT — per drive, every drive. Wherever the pattern
        matches, it goes, so the remaining text meets Design's ORIGINAL under
        the byte-for-byte comparison it has always been under. This is the one
        half that must be per drive, because the text being compared is.
      · PRESENT IN THE PORT'S REGION — once per page, over all drives.
      · PRESENT IN THE AMENDED DELIVERY'S SAME REGION — once per page.
      · ABSENT FROM THE ORIGINAL DELIVERY — once per page, over all drives:
        matching it on ANY drive is fatal, because one screen where Design
        already drew it is enough to prove it was never an addition.

    The three page-level halves are RECORDED here (into `seen`) and REPORTED by
    `_additions_seen`, which is how `_apply_ruled` and `_ruled_seen` already
    divide the work.

    Returns `(g_text, rows)`. `rows` is empty by construction and the shape is
    kept anyway: `_apply_ruled` has a genuine per-drive verdict to emit — a
    ruled-away span that came BACK is wrong on the drive it came back on —
    whereas every way an addition can be wrong is a statement about the page,
    not about one drive. A row emitted here would be the same row nineteen
    times.
    """
    import re
    rows = []
    adds = AMENDED_ADDITIONS.get(page) or ()
    if not adds or amended_states is None:
        return g_text, rows
    for add in adds:
        pat = add["pat"]
        reg = _amended_region(amended_states, add)
        if reg is not None and re.search(pat, reg["text"]):
            seen.add(_ADD_IN_AMENDED + add["label"])
        port_reg = (g_regions or {}).get(add["region"])
        if port_reg is not None and re.search(pat, port_reg["text"]):
            seen.add(_ADD_IN_PORT + add["label"])
        # ⚠️ Checked against the ORACLE's text on this drive, NOT against the
        # amended delivery. If Design's original already said it, the entry is
        # not registering an addition — it is deleting a span out of the port's
        # side of a live comparison, which is the one thing this must not do.
        if re.search(pat, d_text):
            seen.add(_ADD_IN_ORIGINAL + add["label"])
        g_text = re.sub(pat, "", g_text)
    return g_text, rows


def _apply_additions_controls(page, d_controls, g_controls, amended_states,
                              problems, seen):
    """The port's control list with the registered added controls removed.

    Same discipline and the same split of scopes as `_apply_additions`: removed
    from the port's census on EVERY drive, and the three "is it really an
    addition" halves recorded once per page for `_additions_seen` to report.

    Matched on EXACT control text rather than a substring, because the census
    stores one whole label per entry and a substring rule would quietly swallow
    a second control that merely contains the first — `FLASHCARDS` would take
    `FLASHCARDS · 8r/Sc1` with it, and the port would lose a control from the
    comparison without anybody registering it.
    """
    rows = []
    adds = AMENDED_CONTROLS.get(page) or ()
    if not adds or amended_states is None:
        return g_controls, rows
    labels = set()
    for add in adds:
        ctl = add["control"]
        labels.add(ctl)
        reg = _amended_region(amended_states, add)
        if reg is not None and ctl in reg["controls"]:
            seen.add(_ADD_CTL_IN_AMENDED + add["label"])
        if ctl in (g_controls or ()):
            seen.add(_ADD_CTL_IN_PORT + add["label"])
        if ctl in (d_controls or ()):
            seen.add(_ADD_CTL_IN_ORIGINAL + add["label"])
    return [c for c in g_controls if c not in labels], rows


def _additions_seen(page, seen, amended_states, problems):
    """Once per page: every registered addition is really an addition.

    Three assertions per entry, and each of them fails a DIFFERENT way of being
    wrong. They are separate rows on purpose — collapsing them into one "the
    registration is bad" verdict would tell whoever reads the output that
    something is wrong without telling them which of three quite different
    things to go and do.
    """
    rows = []
    adds = list(AMENDED_ADDITIONS.get(page) or ())
    ctls = list(AMENDED_CONTROLS.get(page) or ())
    if not adds and not ctls:
        return rows

    if amended_states is None:
        # Registered additions with no amended delivery driven. Either the page
        # has no `amended` entry in PAIRS, or `run()` skipped the drive — both
        # mean the entries below were applied to the port's text without
        # anything ever checking them against Design. Fatal, and reported once.
        rows.append((page, "additions · the amended delivery was driven", "FAIL",
                     "%d registration(s) with no amended reference"
                     % (len(adds) + len(ctls))))
        problems.append(
            "%s — %d addition(s) are registered and Design's AMENDED delivery "
            "was never driven, so every one of them was stripped out of the "
            "port's text on trust. Give the page `amended_root` / `amended` in "
            "PAIRS, or take the registrations out; a registry that nothing "
            "checks is a licence to delete text from a comparison."
            % (page, len(adds) + len(ctls)))
        return rows

    known_states = {lbl for lbl, _steps in AMENDED_DRIVES.get(page, ())}
    for add in adds:
        label, state = add["label"], add.get("state", "at rest")

        if state not in known_states:
            rows.append((page, "additions · %s — the state is driven" % label,
                         "FAIL", "no AMENDED_DRIVES entry named %r" % state))
            problems.append(
                "%s — the addition %r names the state %r, and AMENDED_DRIVES "
                "for this page has no drive by that name. The region it lives "
                "in is therefore never reached and the entry cannot be checked "
                "against Design at all. Add the drive that reveals it, or "
                "correct the state name." % (page, label, state))
            continue

        ok = (_ADD_IN_AMENDED + label) in seen
        rows.append((page, "additions · %s — in Design's amended delivery"
                     % label, "PASS" if ok else "FAIL",
                     "found in the %r region, %r" % (add["region"], state) if ok
                     else "NOT in the %r region of the amended delivery"
                     % add["region"]))
        if not ok:
            problems.append(
                "%s — the addition %r was NOT found in the %r region of "
                "Design's AMENDED delivery in the %r state. This registration "
                "is stale: Design has redrawn the amendment, or the region was "
                "renamed, or the state that reveals it is no longer %r. "
                "Re-read the amended delivery and re-register it. Do NOT widen "
                "the pattern until it matches something — a pattern loosened "
                "to go green deletes more of the port's text than anybody "
                "agreed to." % (page, label, add["region"], state, state))

        ok = (_ADD_IN_PORT + label) in seen
        rows.append((page, "additions · %s — on the ported page" % label,
                     "PASS" if ok else "FAIL",
                     "found in the port's own %r region" % add["region"] if ok
                     else "NOT in the port's %r region on any drive"
                     % add["region"]))
        if not ok:
            problems.append(
                "%s — the addition %r is registered as chrome this port GAINS "
                "from Design's amendments, and it is not in the port's own %r "
                "region on any drive. Either the merge has not landed that "
                "region yet, or the port's markup carries no "
                "`data-port-region=\"%s\"` for this to be found inside, or the "
                "pattern has rotted. An addition the port does not have is not "
                "an addition — it is a registration written ahead of the work, "
                "and while it stands the pattern is being stripped out of a "
                "comparison it never appears in. Land the merge, or take the "
                "entry out until you do."
                % (page, label, add["region"], add["region"]))

        bad = (_ADD_IN_ORIGINAL + label) in seen
        rows.append((page, "additions · %s — not in Design's original" % label,
                     "FAIL" if bad else "PASS",
                     "ALSO matches the original delivery" if bad
                     else "absent from the original delivery, as an addition "
                          "must be"))
        if bad:
            problems.append(
                "%s — the addition %r ALSO matches DESIGN's ORIGINAL delivery, "
                "which is the oracle. Then it is not an addition, and this "
                "entry is claiming credit for work Design had already drawn "
                "while quietly deleting that span from the port's side of the "
                "comparison — the one thing this mechanism must never do. "
                "Remove the entry. If the port genuinely diverges from the "
                "original here, that is a RULED_DIVERGENCE with a ruling "
                "behind it, not an addition." % (page, label))

    for add in ctls:
        label, state = add["label"], add.get("state", "at rest")

        if state not in known_states:
            rows.append((page, "additions · the %s control — the state is "
                         "driven" % add["control"], "FAIL",
                         "no AMENDED_DRIVES entry named %r" % state))
            problems.append(
                "%s — the added control %r names the state %r, and there is no "
                "AMENDED_DRIVES entry by that name, so nothing ever reaches "
                "the screen it lives on. Add the drive, or correct the state."
                % (page, add["control"], state))
            continue

        ok = (_ADD_CTL_IN_AMENDED + label) in seen
        rows.append((page, "additions · the %s control — in Design's amended "
                     "delivery" % add["control"], "PASS" if ok else "FAIL",
                     "a control in the %r region" % add["region"] if ok
                     else "NOT a control in the amended delivery's %r region"
                     % add["region"]))
        if not ok:
            problems.append(
                "%s — %r is registered as a control this port gains, and it is "
                "not a control in the %r region of Design's AMENDED delivery "
                "in the %r state. The census stores whole labels, so a near "
                "miss reads as a total miss: check the text character for "
                "character before assuming Design removed it."
                % (page, add["control"], add["region"], state))

        ok = (_ADD_CTL_IN_PORT + label) in seen
        rows.append((page, "additions · the %s control — on the ported page"
                     % add["control"], "PASS" if ok else "FAIL",
                     "a control on the port too" if ok
                     else "NOT a control on the port on any drive"))
        if not ok:
            problems.append(
                "%s — %r is registered as a control this port gains, and it is "
                "not a control on the ported page on any drive — while being "
                "removed from the port's census on every one of them. Land the "
                "merge, or take the entry out." % (page, add["control"]))

        bad = (_ADD_CTL_IN_ORIGINAL + label) in seen
        rows.append((page, "additions · the %s control — not in Design's "
                     "original" % add["control"], "FAIL" if bad else "PASS",
                     "ALSO a control in the original delivery" if bad
                     else "absent from the original delivery, as an addition "
                          "must be"))
        if bad:
            problems.append(
                "%s — %r is ALSO a control in Design's ORIGINAL delivery, so "
                "it is not something the port gained; it is something both "
                "sides always had, being deleted from one side of the "
                "comparison. Remove the entry." % (page, add["control"]))
    return rows


# ── the self-proof ────────────────────────────────────────────────────────
#
# ⚑ A SWEEP THAT FINDS NOTHING HAS SAID NOTHING UNTIL IT HAS BEEN SHOWN FINDING
# SOMETHING. This is layer E/F/H's rule in `student_parity.py`, and it applies
# here with more force than it does there, because this registry SHIPS EMPTY:
# on the day it lands, every line of it runs against nothing and reports
# nothing, which is indistinguishable from every line of it being broken.
#
# So before the real comparison, the machinery is driven on synthetic strings —
# no browser, no files, no network — and made to prove BOTH directions:
#
#   (a) a REGISTERED addition present in the port is stripped, and the stripped
#       port text then equals Design's original exactly → the drive PASSES.
#       This is the half that lets the mechanism say yes.
#   (b) an UNREGISTERED extra span, in an untouched region, is NOT stripped, and
#       the comparison still FAILS. This is the half that stops it from being a
#       blanket amnesty — a bug that made `_apply_additions` strip broadly, or
#       return Design's text instead of the port's, would pass (a) happily and
#       turn the whole gate into a formality.
#
# ⚠️ THE PROOF USES THE REAL FUNCTIONS, not a copy of their logic. A proof that
# reimplements what it is proving tests the copy.
def _prove_additions():
    """Prove the additions machinery can both strip and refuse to strip."""
    page = "__additions self-proof__"
    disp = "the additions self-proof"
    entry = dict(label="a synthetic addition",
                 region="r",
                 pat=r"NEWCHROME ",
                 state="at rest",
                 why="synthetic — exists only for the length of this proof")
    # Design's ORIGINAL: what the port must still equal once the addition is
    # taken back out.
    d_text = "ALPHA BETA GAMMA"
    # Design's AMENDED delivery, and the port, both carrying the new chrome
    # inside the region the entry names.
    region = {"change": "synthetic", "text": "ALPHA NEWCHROME BETA",
              "controls": []}
    amended = {"at rest": {"regions": {"r": region}}}
    port_regions = {"r": dict(region, change="")}

    faults = []
    AMENDED_ADDITIONS[page] = [entry]
    AMENDED_DRIVES[page] = [("at rest", [])]
    try:
        # (a) the registered span is stripped, and what is left IS the oracle.
        seen, sink = set(), []
        got, _rows = _apply_additions(
            page, d_text, "ALPHA NEWCHROME BETA GAMMA", port_regions,
            amended, sink, seen)
        if got != d_text:
            faults.append(
                "a registered addition was not stripped out of the port's "
                "text: %r was left as %r, which does not equal Design's %r"
                % ("ALPHA NEWCHROME BETA GAMMA", got, d_text))
        if (_ADD_IN_AMENDED + entry["label"]) not in seen:
            faults.append("the amended delivery's own region was not "
                          "recognised as containing the addition")
        if (_ADD_IN_PORT + entry["label"]) not in seen:
            faults.append("the port's own region was not recognised as "
                          "containing the addition")
        if (_ADD_IN_ORIGINAL + entry["label"]) in seen:
            faults.append("the addition was reported as ALREADY PRESENT in "
                          "Design's original, which does not contain it — the "
                          "staleness check fires on healthy entries")

        # (b) an UNREGISTERED span survives, and the comparison still fails.
        seen2, sink2 = set(), []
        got2, _rows2 = _apply_additions(
            page, d_text, "ALPHA NEWCHROME BETA UNREGISTERED GAMMA",
            port_regions, amended, sink2, seen2)
        if got2 == d_text:
            faults.append(
                "an UNREGISTERED extra span was swallowed: the port read %r "
                "and still compared equal to Design's %r, so the machinery is "
                "stripping more than it was told to and no unregistered "
                "divergence on the real page could ever be seen"
                % ("ALPHA NEWCHROME BETA UNREGISTERED GAMMA", d_text))
        if "UNREGISTERED" not in got2:
            faults.append("the unregistered span %r did not survive the strip"
                          % "UNREGISTERED")
    finally:
        AMENDED_ADDITIONS.pop(page, None)
        AMENDED_DRIVES.pop(page, None)

    rows, problems = [], []
    if faults:
        rows.append((disp, "the additions machinery strips, and only what it "
                     "was told to", "FAIL", "; ".join(faults)[:110]))
        problems.append(
            "the additions self-proof FAILED: %s. Until this passes, the "
            "additions machinery is blind, and its silence on the real page "
            "proves nothing whatever — an empty problem list would mean only "
            "that a broken mechanism found nothing, which is what a broken "
            "mechanism always does." % "; ".join(faults))
    else:
        rows.append((disp, "the additions machinery strips, and only what it "
                     "was told to", "PASS",
                     "registered span removed and the text then matches; "
                     "unregistered span survives and it does not"))
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
