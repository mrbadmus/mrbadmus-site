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
        # ── ⊕ 23 Aug 2026 — PHASE 3. THE SEVEN `Recall` DRIVES ARE RETIRED ──
        #
        # They read:
        #
        #     ("recall opens",                      [click Recall])
        #     ("recall · pick an option",           [click Recall, opt 0])
        #     ("recall · Check reveals the answer and the feedback", …)
        #     ("recall · Next question moves on",   …)
        #     ("recall · Skip breaks the streak",   [click Recall, click Skip])
        #     ("recall · six answers reach the round card", …)
        #     ("recall · back to the class",        [click Recall, click My class])
        #
        # Quoted rather than deleted, because seven drives leaving a gate is
        # exactly the change that must not happen quietly.
        #
        # ⚠️ THEY CANNOT BE REWRITTEN, AND THAT IS THE POINT. Design's C2b
        # replaces the recall round wholesale: the ORIGINAL is a `view` painted
        # in page-chrome dark, the AMENDED one is a themed overlay with a round
        # number, a progress bar, a verdict and an Another-round exit. The port
        # takes Design's amended round and prunes Design's original (see PHASE
        # 3 in student_rulings.py).
        #
        # `run()` requires every step of a drive to be performable on DESIGN'S
        # ORIGINAL FILE — that is what makes the original the ORACLE — and the
        # step that opens a round therefore opens the OLD round on Design's side
        # and the NEW one on ours. The two screens share almost no text: the
        # comparison would be a whole-screen divergence, and the only way to
        # keep it green would be to register the entire old round in
        # `RULED_DIVERGENCE` and the entire new one in `AMENDED_ADDITIONS`.
        # That is not what those registries are for — "a registration is a
        # sentence about ONE span" — and a gate that deletes both sides of a
        # screen before comparing them has stopped comparing it.
        #
        # ⚑ SO THE ROUND JOINS THE FLASHCARDS OVERLAY IN THE PLACE THIS GATE
        # CANNOT REACH, and that is stated here rather than left to be
        # discovered. `student_themes.py` is extended to cover it instead: it
        # drives the PORT ALONE, needs no oracle because a colour is checked
        # against Design's stated palette, and it can therefore press a control
        # this port gained. It opens the round, walks it, and sweeps its text
        # on all six themes. It is the only gate that watches this surface.
        # ⊕ 23 Aug 2026 — PHASE 1b. Two states of Design's account sheet, and
        # they are the only drives on this page that reach the theme picker.
        #
        # `Settings` is pressed rather than the avatar, deliberately: the
        # avatar toggles the header dropdown on our page (Design's amended
        # header has no dropdown, so Design wires the avatar to the sheet
        # instead), and the control that opens the sheet on BOTH files is this
        # one. A drive has to work on Design's file or it is reported as this
        # file's bug — see `run()`.
        # ⊕ 23 Aug 2026 — THE STEP THAT OPENS THE MENU IS NEW, AND IT IS NOT
        # A CONVENIENCE. This drive used to read `[("click", "Settings")]`,
        # which worked because BOTH files drew `Settings` inline in the header.
        # The port no longer does: the wide header's inline `Settings` /
        # `Sign out` pair is pruned (student_rulings.py — "the header said
        # everything twice"), so on the port the only `Settings` is the one
        # inside the account menu, and the menu has to be opened to reach it.
        #
        # ⚠️ THE TWO FILES PRESS DIFFERENT ELEMENTS, DELIBERATELY, AND END IN
        # THE SAME STATE. `_CLICK` takes the first match in document order — on
        # Design's file that is the inline link (dead there, as it always was),
        # on the port it is the menu item wired to `openAccount`. Both files
        # therefore finish with the account menu OPEN, which is why
        # `openAccount` stops clearing `menu` in the same commit; a port that
        # closed the menu here would diverge from the oracle by two controls
        # that no registry can describe per drive.
        ("Settings opens the account sheet",
         [("has", "AY"), ("click", "Settings")]),
        #
        # ⚠️ AND THERE IS NO DRIVE HERE THAT PRESSES A SWATCH, WHICH IS A
        # LIMIT OF THIS GATE RATHER THAN AN OMISSION. It was written, run, and
        # taken back out:
        #
        #     ("a theme swatch is picked",
        #      [("click", "Settings"), ("click", "CHALK")]),
        #
        # `run()` requires every step to be performable on DESIGN'S ORIGINAL
        # file — a step that only works on the port is reported as this file's
        # bug, deliberately, because otherwise a typo in a label reads as a
        # behavioural divergence. Design's original has no picker, so it has no
        # `CHALK`, and the drive failed exactly as designed with "the drive
        # does not work on Design's file".
        #
        # That generalises: **no control this port GAINS from the amendments
        # can ever be pressed by this gate**, only observed. `Settings` can be
        # pressed because Design's original has one too (dead there, live
        # here). The six swatches are asserted to EXIST as controls, in
        # `AMENDED_CONTROLS`; what happens when one is pressed is measured by
        # `student_themes.py`, which drives the port alone and needs no oracle
        # because a colour is checked against Design's stated palette rather
        # than against Design's file.
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
    # ⊕ 23 Aug 2026 — omissions count too, and for the same reason additions
    # do: an omission that is never checked against Design's amended delivery
    # is a claim about a file nobody opened.
    return bool(AMENDED_ADDITIONS.get(name) or AMENDED_CONTROLS.get(name)
                or AMENDED_OMISSIONS.get(name))


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

            # ⊕ 23 Aug 2026. LAST of the three census steps, and it is the only
            # one that edits BOTH lists. It is applied after the other two
            # rather than between them because it counts occurrences, and
            # counting a label that a registry above is about to remove would
            # make the arithmetic depend on the order two independent
            # registries happen to be written in. Nothing it names appears in
            # either of the others — checked, not assumed.
            d_ctl, g_ctl, edit_rows = _apply_ruled_control_edits(
                name, d_ctl, g_ctl, problems, seen)
            rows.extend(edit_rows)

            # ⊕ 23 Aug 2026 — PHASE 1c. Strips nothing from either side; it
            # only records what the registered omissions look like on this
            # drive. `gs["text"]` and not `g_text`: an omission asks whether
            # the span is on the PAGE, and reading the already-stripped copy
            # would ask whether it survived a strip that never targets it.
            _apply_omissions(name, ds["text"], gs["text"],
                             gs.get("regions") or {}, amended_states,
                             problems, seen)

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
        rows.extend(_omissions_seen(name, seen, amended_states, problems))
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
        # ⊕ RULED 22 Aug 2026 — P7, and ⊕ RETIRED 23 Aug 2026 — PHASE 1b.
        # The entry that stood here read:
        #
        #     ("the dead Settings control", r"Settings "),
        #
        # It is quoted rather than deleted because its own note said what
        # would end it: *"if Design ever gives Settings a purpose, the first
        # half fails and this ruling gets re-read instead of quietly
        # outliving its reason."* Design's amended delivery gives it one —
        # donor node 22 is the same word as a `<button>` carrying
        # `onClick={{ openAccount }}` — so the port wires it to the account
        # sheet and renders it again, exactly as Design's ORIGINAL delivery
        # does. There is no divergence left to declare.
        #
        # ⚠️ AND IT COULD NOT HAVE BEEN LEFT IN "just in case". This registry
        # strips the match out of DESIGN's text, so a stale entry would have
        # taken `Settings ` off Design's side while the port had it, and all
        # nineteen class-view drives would have gone red naming a defect that
        # is the ruling being satisfied. Its twin in `RULED_CONTROLS` goes in
        # the same commit for the same reason.
        #
        # ⚑ THE SHEET IT NOW OPENS IS NOT REGISTERED HERE. It is not something
        # the port REMOVED from Design's original; it is something the port
        # GAINED from Design's amendments, which is the mirror registry —
        # `AMENDED_ADDITIONS`, below.
        #
        # ── ⊕ 23 Aug 2026 — PHASE 2. THE DARK RECALL CARD ────────────────
        #
        # Design's own donor node says what happened to it, in Design's words:
        # `data-port-change="C2 replaces the dark RECALL card"`. So the whole
        # card leaves the port — its eyebrow, its answered count, its blurb and
        # its button — and Design's flashcards card arrives in its place. The
        # arrival is registered in `AMENDED_ADDITIONS`; this is the departure.
        #
        # ⚠️ THE PATTERN STARTS `Recall 46` AND NOT `Recall`, and that is not
        # tidiness. `Recall` on its own also matches the NAV item three lines
        # into the page, and stripping that from Design's side would take a
        # control label out of the comparison on every drive while reporting
        # nothing. The count that follows it is Design's own `retrievalCount`,
        # which is a fixture value and therefore fixed.
        #
        # ⚑ NOTHING A STUDENT COULD DO IS LOST WITH IT. `Start a round` was one
        # of THREE routes into the recall round — `Practise recall` (node 77)
        # and `Start recall` (node 88) are both on the bench, and the nav has
        # `Recall` — and all three still work. Counted before the graft was
        # written, not assumed afterwards.
        # ⚠️ `RECALL` UPPER-CASE, AND THE FIRST DRAFT HAD IT SENTENCE-CASE.
        # Design's eyebrow is typed `Recall` in the markup and upper-cased by
        # `.eyebrow`'s CSS, so the SOURCE says one thing and `innerText` — which
        # is what this gate reads — says another. The same trap the bench blurb
        # and the docket lead both sprang on the seam: a pattern written against
        # the file cannot be matched against the render. Corrected by reading
        # the render, not by reading harder.
        #
        # `RECALL 46 ANSWERED` also opens the READINGS strip six hundred
        # characters earlier, and the two are told apart by what follows: this
        # one continues `THIS WEEK Questions from…`, the strip continues
        # `· WK 04`. Checked before the pattern was narrowed.
        ("the dark sidebar RECALL card, which C2 replaces",
         r"RECALL 46 ANSWERED THIS WEEK Questions from the lessons this class "
         r"has covered\. Six a round, unlimited rounds\. Start a round "),
        # ── ⊕ 23 Aug 2026 — PHASE 3. THE NAV'S `Recall` TAB ───────────────
        #
        # The header nav is a VIEW SWITCH — two tabs, `on: onClass` and
        # `on: !onClass`, an underline saying which view you are in. Design's
        # C2b makes the round a fixed overlay opened from the bench, so there
        # is no second view for a tab to switch to, and a tab wired to an
        # overlay could never look selected. It is removed; `Practise recall`
        # on the bench is the route, in both bench states, which is where
        # Design's own amended delivery puts it (donor 76 and donor 116).
        #
        # ⚠️ THE LOOKBEHIND IS LOAD-BEARING, AND A BARE `Recall ` WOULD HAVE
        # BEEN WRONG TWICE. It is the same trap the entry above documents from
        # the other side: that one had to start `RECALL 46` so it would NOT
        # catch this nav item, and this one has to be anchored so it does not
        # catch anything else that says the word. `_apply_ruled` runs these in
        # LIST ORDER and each `re.sub` edits the text the next one sees, so an
        # unanchored pattern here would also eat into the card above it
        # depending on which ran first. `My class` immediately precedes it in
        # the nav, on every drive, on both files.
        ("the nav's Recall tab, which C2b replaces with the bench route",
         r"(?<=My class )Recall "),
        # ── ⊕ RULED 23 Aug 2026 — THE HEADER SAID EVERYTHING TWICE ────────
        #
        # Design's wide header draws the student's first name beside the
        # avatar disc and an inline `Settings` / `Sign out` pair beside that —
        # and pressing the avatar drops a menu carrying `Settings` and
        # `Sign out` AGAIN. The port keeps the MENU (it is the only route at
        # phone width) and prunes the name and the inline pair.
        #
        # ⚠️ ONE PATTERN FOR THREE REMOVALS, AND THE ANCHOR IS WHAT MAKES IT
        # SAFE. `Settings ` on its own, or `Sign out ` on its own, would also
        # match the MENU's copies — which the port still has — and every drive
        # that opens the menu would report the ruling as "back on the port".
        # Anchored behind the monogram, the pattern can only match the run the
        # inline pair makes: monogram, name, Settings, Sign out. The port never
        # has a name after the monogram, so it never matches there, in any
        # state. Checked in all three: menu closed, menu open, and menu open
        # with the account sheet over it.
        ("the header's duplicated name and its inline Settings / Sign out",
         r"(?<=AY )Ayo Settings Sign out "),
        # ── ⊕ RULED 23 Aug 2026 — THE WORK ROW'S HINT WORD ────────────────
        #
        # One word at the right-hand end of each work row's summary line,
        # reading as a button and not being one — the whole line is a single
        # `<button>` that expands the row, which is what pressing the word
        # does. Design already drops all four below 720px, where the handoff
        # note says the caret carries the affordance alone; the port drops them
        # at every width (`showHint: false`, student_rulings.py).
        #
        # ⚠️ FOUR ENTRIES AND NOT ONE, because the fixture's six work rows
        # exercise all four statuses — open, marked, pending, missed — and a
        # single pattern would let three of them come back silently under the
        # fourth one's registration. Each is its own sentence about its own
        # word.
        #
        # ⚠️ AND EACH IS BARE RATHER THAN ANCHORED, which is the opposite
        # choice from the header entry above and is made for the opposite
        # reason: measured against the delivery, each of these four strings
        # occurs at exactly ONE place in Design's whole class view — the
        # `hintText` ternary — so there is nothing else on either file for a
        # bare pattern to reach. The bench's own `Open it` task is sentence
        # case and carries no `text-transform`, so it renders `Open it` and not
        # `OPEN IT`; checked in the render, not in the file.
        ("the work row's READ FEEDBACK hint", r"READ FEEDBACK "),
        ("the work row's OPEN IT hint", r"OPEN IT "),
        ("the work row's SEE IT hint", r"SEE IT "),
        ("the work row's OPTIONS hint", r"OPTIONS "),
    ],
    # ── ⊕ RULED 23 Aug 2026 — THE FIRST DIVERGENCES ON THE ASSIGNMENT ─────
    #
    # This key did not exist. Every ruling this page has carried until now
    # either changed a VALUE Design's fixture makes identical (the hand-in
    # stamp, the week label, the topic) or closed a slot Design's own example
    # data fills (the right answer's feedback line), so the rendered text was
    # unmoved and there was nothing to declare. These two remove chrome.
    "assignment": [
        # The topic and the deadline, stacked above the question eyebrow. Both
        # are already on the screen: the topic in the crumb bar and in the
        # marker sheet's lead, the deadline in the crumb bar and on the bench
        # of the page the student came from. `PRUNE` 107 takes the whole row.
        #
        # ⚠️ THE LATE CHIP BESIDE IT IS NOT REGISTERED, AND THAT IS NOT AN
        # OVERSIGHT. `dueFlag` is `st.late ? … : ''` and the `<sc-if>` around
        # it is therefore closed in every state these nine drives reach — none
        # of them hands the work in, and the fixture's scenario is not a late
        # one. A registration for it would be a claim about text that is not in
        # DESIGN's file on any drive either, and `_ruled_seen` would correctly
        # go red for it. It leaves the page with its parent row and is covered
        # by that row's prune, not by a pattern.
        ("the question screen's topic-and-deadline line",
         r"CELLS & MICROSCOPY · DUE THU 18 SEP, 18:00 "),
        # And the topic AGAIN, tacked onto the question counter — the third
        # time on one screen, in the smallest type on it.
        #
        # ⚠️ THE FOUR TOPICS ARE SPELLED OUT RATHER THAN WILDCARDED. Design's
        # sixteen questions carry exactly four distinct `q.t` values and the
        # drives visit three different questions, so an alternation covers
        # every state this gate reaches without a single `.*` — and a `.*` here
        # would eat into the question text beside it, which is the one thing
        # on this screen that must stay under byte-for-byte comparison.
        #
        # The values are already upper case in Design's data AND the span
        # carries `.eyebrow`, which upper-cases again; the pattern is written
        # against the RENDER, which is what `innerText` gives this gate.
        #
        # ⚠️ NO TRAILING SPACE, WHICH IS THE OPPOSITE OF EVERY OTHER PATTERN
        # HERE AND IS RIGHT FOR THE OPPOSITE REASON. The registrations above
        # remove a span that is FOLLOWED by more of the same line, so the
        # joining space has to come out with it or a double space is left
        # behind. This span is the END of its element: `innerText` puts one
        # space between the eyebrow and the `<h1>` below it, and that space
        # belongs to the counter, which survives. Taking it welded
        # `QUESTION 07 OF 15` to `The diagram shows…` and failed all nine
        # drives at the same character — measured, then corrected.
        ("the question eyebrow's topic suffix",
         r"(?<=QUESTION \d\d OF \d\d) · (?:USING A MICROSCOPE"
         r"|ANIMAL AND PLANT CELLS|LIFE PROCESSES AND CELLS"
         r"|SPECIALISED CELLS)"),
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
# ⊕ RETIRED 23 Aug 2026 — PHASE 1b. This read `{"class view": ["Settings"]}`
# and its comment said *"It returns when Design's theme picker gives it a job,
# not before."* The picker gives it one, so `Settings` is a control on both
# sides again and there is nothing to declare. Kept as an empty map rather
# than deleted: the mechanism is sound and the next ruling that removes a
# pressable control needs it.
# ⊕ 23 Aug 2026 — PHASE 2. AND THE MECHANISM IS NEEDED AGAIN ONE UNIT LATER,
# which is why it was kept. `Start a round` is the dark RECALL card's button,
# and the card is replaced wholesale by Design's C2. Registered here as well as
# in `RULED_DIVERGENCE` because the two comparisons are separate: stripping the
# card's TEXT does nothing to the control census, and the census would report
# "controls only in Design: ['Start a round']" as though the port had broken a
# button rather than adopted an amendment.
# ⊕ 23 Aug 2026 — PHASE 3. AND A THIRD TIME, one unit later again. `Recall`
# is the nav tab, and it is a `<button>` — so it is in the census as well as in
# the text, and a ruling that reached only the text would report "controls only
# in Design: ['Recall']" on all nineteen drives and read like a broken port.
RULED_CONTROLS = {
    "class view": ["Start a round", "Recall"],
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


# ── RULED CONTROL EDITS — a control the port RELABELS, or removes ONE OF ──
#
# ⊕ 23 Aug 2026 — THE THIRD SHAPE `RULED_CONTROLS` CANNOT SAY.
#
# `RULED_CONTROLS` is label-based and all-or-nothing: it takes EVERY entry
# with that text out of Design's census, and it fails the port on every drive
# where the label is present at all. That is exactly right for a control the
# port removes outright — `Recall`, `Start a round` — and it cannot express
# either half of the 23 Aug header ruling:
#
#   · THE PORT REMOVES ONE OF TWO IDENTICAL CONTROLS. Design draws `Settings`
#     and `Sign out` twice over — inline in the wide header, and again inside
#     the account menu. The port prunes the inline pair and KEEPS the menu, so
#     `Settings` is still a control on the port and registering it in
#     `RULED_CONTROLS` would report the surviving one as a reverted ruling on
#     every drive that opens the menu.
#   · THE PORT RELABELS A CONTROL. The avatar's label is the monogram AND the
#     name (`AY Ayo`) on Design's file and the monogram alone (`AY`) on the
#     port. `RULED_CONTROLS` can delete Design's label; nothing could then
#     account for the port's, and the two lists would differ by one entry with
#     no registry able to say why.
#
# ⚑ IT IS STILL ASSERTED BOTH WAYS, WHICH IS WHAT KEEPS IT A GATE.
#
#   · `design` must be a control in DESIGN's own file — once per page, over
#     all drives. A registration that stops matching is a claim about the
#     past and goes red, exactly as `RULED_DIVERGENCE`'s does.
#   · `port`, when there is one, must be a control on the PORT — once per
#     page. A relabel with no new label is a removal wearing the wrong shape.
#   · PER DRIVE, EVERY DRIVE: the port may not carry MORE copies of `design`
#     than `n` fewer than Design carries. That is the "back on the port" half:
#     if the pruned pair returns, the count goes back up and this goes red on
#     the drive it returned on.
#
# Everything outside the registered delta stays under the byte-for-byte list
# comparison it has always been under: this removes `n` entries from each
# side, in document order, and nothing else.
#
# TWO ENTRY SHAPES, and the second one arrived one ruling later:
#
#   `label`, `design`, `port` (or None), `n`, `why`
#       exact labels. Removes `n` copies of `design` from Design's census and,
#       when `port` is given, `n` copies of `port` from the port's — a relabel.
#
#   `label`, `suffix`, `why`
#       a TAIL the port drops from a control whose label is otherwise
#       untouched. Every Design control ENDING in `suffix` loses it; no port
#       control may end in it. This is the shape a ruling takes when the text
#       it removes is INSIDE a longer label rather than being the whole of one.
#
# ⚠️ THE SECOND SHAPE EXISTS BECAUSE THE FIRST COULD NOT SAY THE WORK ROWS.
# Each work row is ONE `<button>` whose label is the whole summary line —
# `W03 Digestion 6 questions · enzymes and the gut 82% READ FEEDBACK` — so the
# hint word this port drops is six characters at the end of a label that also
# carries a week, a title, a brief and a score, and every one of the six rows
# has a different one. Registering them as exact labels would mean twelve
# hand-typed strings carrying a student's marks, going stale the moment any
# one of them changed for a reason nothing to do with this ruling.
RULED_CONTROL_EDITS = {
    "class view": [
        dict(label="the avatar drops the duplicated name",
             design="AY Ayo", port="AY", n=1,
             why="RULED 23 Aug 2026 — the student's first name was on the "
                 "header beside the monogram, again inside the account sheet "
                 "that header opens, and again in the hero's 'Good week, …'. "
                 "The avatar keeps the monogram, which is what a monogram is "
                 "for. It is one control on both files and its LABEL moves, "
                 "so both sides lose exactly one entry."),
        dict(label="the header's inline Settings, duplicated by the menu",
             design="Settings", port=None, n=1,
             why="RULED 23 Aug 2026 — Design draws Settings twice at 1460: "
                 "inline in the header and again in the account menu the "
                 "avatar drops. The port keeps the MENU copy, because that is "
                 "the only one a phone can reach (the inline pair is inside "
                 "`if wide`), and prunes the inline one. n=1: Design's second "
                 "copy is still expected, on every drive that opens the menu."),
        dict(label="the header's inline Sign out, duplicated by the menu",
             design="Sign out", port=None, n=1,
             why="The other half of the same pair, and it is registered "
                 "separately rather than folded in because the two are "
                 "different destinations and a single entry would let one of "
                 "them come back under the other's justification."),
    ] + [
        # The four work-row hint words, on the census side. Their twins in
        # `RULED_DIVERGENCE` cover the page text; these cover the row buttons,
        # because the hint sits INSIDE the button that carries the whole row
        # and stripping the text does nothing to the control list.
        #
        # One per status, for the reason the text side gives: a single entry
        # would let three of the four come back under the fourth's ruling.
        dict(label="the work row's %s hint, on the row button" % word.lower(),
             suffix=" " + word,
             why="RULED 23 Aug 2026 — the hint word reads as a button and is "
                 "not one: the whole summary line is a single control, and "
                 "pressing the word expands the row rather than doing what it "
                 "says. Design already drops all four below 720px, where the "
                 "handoff note says the caret carries the affordance alone; "
                 "the port drops them at every width. Nothing is lost — a "
                 "marked row's expanded panel carries the real `Open the "
                 "lesson` button, wired by ruling P3.")
        for word in ("READ FEEDBACK", "OPEN IT", "SEE IT", "OPTIONS")
    ],
}


def _take(seq, label, n):
    """Return `seq` with the first `n` entries equal to `label` removed."""
    out, left = [], n
    for c in seq:
        if left and c == label:
            left -= 1
            continue
        out.append(c)
    return out


_EDIT_IN_DESIGN = "edit-in-design:"
_EDIT_IN_PORT = "edit-in-port:"


def _apply_ruled_control_edits(page, d_controls, g_controls, problems, seen):
    """Remove the registered delta from each census. See the note above."""
    rows = []
    edits = RULED_CONTROL_EDITS.get(page) or ()
    if not edits:
        return d_controls, g_controls, rows
    for e in edits:
        label = e["label"]
        if "suffix" in e:
            suf = e["suffix"]
            if any(c.endswith(suf) for c in d_controls):
                seen.add(_EDIT_IN_DESIGN + label)
            back = [c for c in g_controls if c.endswith(suf)]
            if back:
                rows.append((page, "ruled · %s" % label, "FAIL",
                             "back on the port"))
                problems.append(
                    "%s — %r: %d control(s) on the ported page still END in "
                    "%r, e.g. %r. RULED 23 Aug 2026: the hint word reads as a "
                    "button and is not one — the whole row is a single control "
                    "and pressing the word expands the row. Design itself "
                    "drops all four below 720px."
                    % (page, label, len(back), suf, back[0]))
            d_controls = [c[:-len(suf)] if c.endswith(suf) else c
                          for c in d_controls]
            continue
        design, port, n = e["design"], e.get("port"), e["n"]
        d_has = d_controls.count(design)
        g_has = g_controls.count(design)
        if d_has:
            seen.add(_EDIT_IN_DESIGN + label)
        if port is not None and port in g_controls:
            seen.add(_EDIT_IN_PORT + label)
        # ⚠️ Only checked where Design HAS the control on this drive. Not every
        # drive reaches every screen, and demanding the arithmetic on a screen
        # neither file draws the control on is the mistake `_apply_ruled`'s
        # docstring records — it paints healthy drives red for being elsewhere.
        if d_has and g_has > d_has - n:
            rows.append((page, "ruled · %s" % label, "FAIL",
                         "the port carries %d, Design %d" % (g_has, d_has)))
            problems.append(
                "%s — %r: Design's own file carries %d %r control(s) and the "
                "port carries %d, where the ruling removes %d. The pruned "
                "control is BACK on the ported page, or the prune has moved to "
                "the wrong node. RULED 23 Aug 2026: the header drew the name, "
                "Settings and Sign out, and the account menu under the avatar "
                "drew Settings and Sign out again; the menu is the copy that "
                "survives, because it is the only one a phone can reach."
                % (page, label, d_has, design, g_has, n))
        d_controls = _take(d_controls, design, n)
        if port is not None:
            g_controls = _take(g_controls, port, n)
    return d_controls, g_controls, rows


def _ruled_seen(page, seen, problems):
    """Once per page: every registered divergence was found in Design's file."""
    rows = []
    for e in RULED_CONTROL_EDITS.get(page, ()):
        label = e["label"]
        what = e.get("suffix", e.get("design"))
        ok = (_EDIT_IN_DESIGN + label) in seen
        rows.append((page, "ruled · %s — still in the delivery" % label,
                     "PASS" if ok else "FAIL",
                     "%r is on a control in Design's own file" % what if ok
                     else "%r is on NO control in Design's file on any drive"
                     % what))
        if not ok:
            problems.append(
                "%s — the control edit %r names %r as something this port "
                "removes from or relabels on a control, and no control in "
                "DESIGN's own file carries it on any drive. The registration "
                "is a claim about the past; re-read the delivery."
                % (page, label, what))
        if "suffix" in e or e.get("port") is None:
            continue
        ok = (_EDIT_IN_PORT + label) in seen
        rows.append((page, "ruled · %s — the new label is on the port" % label,
                     "PASS" if ok else "FAIL",
                     "%r is a control on the ported page" % e["port"] if ok
                     else "%r is NOT a control on the port on any drive"
                     % e["port"]))
        if not ok:
            problems.append(
                "%s — the control edit %r relabels a control to %r, and no "
                "control on the ported page carries that label on any drive. "
                "A relabel with no new label is a removal, and it is "
                "registered as the wrong thing."
                % (page, label, e["port"]))
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
    "class view": [
        ("at rest", []),
        # ⊕ 23 Aug 2026 — PHASE 3. Design's amended recall round is
        # `if recallOpen`, so it is not on screen at rest either, and the
        # OMISSION registered against it has to be checked inside a region that
        # is actually rendered. `Practise recall` is Design's own way in: donor
        # node 76 is a `<button>` carrying `onClick={{ openRecall }}` and
        # `data-port-action="recall-round"`, which is Design saying in the file
        # which control opens it.
        #
        # ⚠️ THIS DRIVES DESIGN'S AMENDED DELIVERY ONLY, and that is the
        # difference between it and a `DRIVES` entry. `AMENDED_DRIVES` never
        # touches the port and never touches the original, so it cannot put the
        # two files on different screens — which is precisely why the seven
        # retired `Recall` drives could not be rewritten to do this.
        ("the recall round", [("click", "Practise recall")]),
        # ⊕ 23 Aug 2026 — PHASE 1b. The account sheet is `if accountOpen` in
        # Design's amended delivery too, so it is not on screen at rest and a
        # registration against it would be checked against a region that is
        # never rendered. `Settings` is Design's own way in: donor node 22 is
        # a `<button>` carrying `onClick={{ openAccount }}`.
        ("the account sheet", [("click", "Settings")]),
    ],
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
# ── ⊕ 23 Aug 2026 — PHASE 1b + 1c. THE FIRST FIVE ENTRIES ────────────────
#
# All five live inside `account-sheet`, Design's own region marker, and all
# five are reached by the drive named `the account sheet` — the sheet is
# `if accountOpen` on BOTH deliveries and is not on screen at rest.
#
# ⚠️ THE PATTERNS TILE THE SHEET EXACTLY, WITH ONE SEPARATOR EACH, and that
# is arithmetic rather than taste. `_apply_additions` deletes each match from
# the port's WHOLE text, which reads
#
#     …<the page> <ACCOUNT …> <TEACHER …> <TERM …> <BENCH THEME …> <CLAY …>
#
# so what has to come out is the sheet PLUS the single space that joins it to
# the page before it. Entries 1–4 each take their own trailing space, entry 5
# takes none (it is the end of the string), and entry 1 takes the joining
# space in front — which is why it alone begins ` ?`. The space is optional
# because the same pattern is also searched inside the REGION's own text,
# where the sheet starts at `ACCOUNT` with nothing before it. Get this wrong
# in either direction and every drive on the page goes red over one space
# while reporting a defect that is not there.
#
# ⚠️ THE NAME IS `\S+` AND EVERYTHING ELSE IS LITERAL. Design's amended sample
# student is called `AY`, so its sheet reads `AY AY` — a monogram and a name
# that happen to match. The port binds the monogram to `studentInitials` and
# the name to `studentFirstName` (see `BINDINGS_AT` in build_student_port.py),
# and the fixture's student is `Ayo`, so the port reads `AY Ayo`. That is the
# two deliveries' different SAMPLE DATA, which is the thing this whole
# mechanism exists to tolerate and the reason it cannot simply compare the two
# files. One wildcard, on the one value that is data; nothing else is loosened.
AMENDED_ADDITIONS = {
    "class view": [
        dict(label="the account sheet's heading and identity block",
             region="account-sheet", state="the account sheet",
             pat=r" ?ACCOUNT AY \S+ 8r/Sc1 · SCIENCE ",
             why="Design's C1 puts the bench theme control in an account "
                 "sheet the original delivery has no counterpart for at all. "
                 "This is its header row and the monogram / name / class line "
                 "beneath it."),
        dict(label="the account sheet's TEACHER row",
             region="account-sheet", state="the account sheet",
             pat=r"TEACHER Mr Badmus ",
             why="One of the sheet's two surviving fact rows. The value is "
                 "bound to `teacherName`, which the live page fills with "
                 "'Your teacher' because a student has no read policy on a "
                 "teacher's profile; the fixture shows Design's own value, so "
                 "the pattern is Design's own bytes."),
        dict(label="the account sheet's TERM row",
             region="account-sheet", state="the account sheet",
             pat=r"TERM Summer · Week 01 / 39 ",
             why="The sheet's second fact row. Bound to `accountTerm`, "
                 "composed in student-live.js from the term this page already "
                 "computes and the teaching week the server reports, so it is "
                 "not a second opinion about either."),
        dict(label="the BENCH THEME heading and its note",
             region="account-sheet", state="the account sheet",
             pat=r"BENCH THEME Sets the bench, the week spine and the "
                 r"leaderboard card\. ",
             why="Design's own words for what the picker does, and the two "
                 "sentences C1 is named after. Pure chrome — it does not vary "
                 "with any data."),
        dict(label="the six theme swatch labels",
             region="account-sheet", state="the account sheet",
             pat=r"CLAY CHALK MOSS HARBOUR DAMSON GRAPHITE",
             why="The six themes, in Design's own order. This is the picker "
                 "itself: the six bench themes shipped on 23 Aug with no way "
                 "to choose between them, and these six words are the way."),
        # ── ⊕ 23 Aug 2026 — PHASE 2. THE FLASHCARDS CARD ─────────────────
        #
        # Design's C2 puts this where the dark RECALL card was, and unlike the
        # account sheet it is on screen AT REST on both deliveries — so it
        # needs no new `AMENDED_DRIVES` state.
        #
        # ⚠️ THE WHOLE CARD IS ONE PATTERN, because on the amended delivery it
        # is one CONTROL and the census stores one whole label per control. The
        # three values in it are Design's own: `06` is `pad(deck.length)` over
        # Design's six sample cards, `Define diffusion.` is card one's front,
        # and `01 / 06` is `stackPos` at rest. The port renders the identical
        # three because the fixture's deck IS Design's — lifted out of the
        # amended delivery's own `deck()` by `DONOR_LIFTS` in
        # build_student_port.py rather than retyped.
        #
        # ⚠️ THE TRAILING SPACE IS OPTIONAL, FOR THE REASON ENTRY 1 ABOVE
        # DOCUMENTS IN THE MIRROR. In the page's WHOLE text the card is
        # followed by `WORK`, so the joining space has to come out with it or
        # every drive goes red over a double space. In the REGION's own text
        # the card IS the whole string and there is no trailing space to take.
        # `re.sub` is greedy, so one pattern serves both.
        #
        # ⚑ AND THE OVERLAY IS NOT REGISTERED, WHICH IS A LIMIT OF THIS GATE
        # AND NOT AN OMISSION. Design's flashcards overlay is `if cardsOpen`,
        # and the only control that opens it is the card above — a control the
        # port GAINED. `run()` requires every step of a drive to be performable
        # on Design's ORIGINAL file, which has no flashcards card at all, so
        # the port can never be driven into the overlay here. That is the same
        # limit the missing swatch drive records: no control this port gains
        # from the amendments can ever be PRESSED by this gate, only observed.
        # The overlay is verified by hand-driving the live page, and by nothing
        # in the gate set.
        dict(label="the flashcards card that replaces the RECALL card",
             region="sidebar-flashcards", state="at rest",
             pat=r"FLASHCARDS 06 Define diffusion\. 01 / 06 ?",
             why="Design's C2, at rest: the deck's size, the top card's front "
                 "and the stack position. It is the deck's front door and its "
                 "resume marker — reopening mid-deck returns to this card — "
                 "and it replaces the dark RECALL card registered as leaving "
                 "in RULED_DIVERGENCE."),
    ],
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
    "class view": [
        # ⚠️ AN EMPTY LABEL IS A REAL CONTROL AND HAS TO BE REGISTERED LIKE
        # ANY OTHER. Design's close button is a 44×44 icon button carrying an
        # SVG and a `title="Close"`, so the census — which stores `innerText`
        # — records it as the empty string. Measured before it was trusted:
        # Design's ORIGINAL delivery has 44 controls and ZERO empty labels, so
        # removing "" from the port's census on every drive can only remove
        # this one. If the original ever gains an icon button, the
        # not-in-the-original assertion below goes red and says so.
        dict(label="the account sheet's close button",
             region="account-sheet", state="the account sheet", control="",
             why="Design's 44x44 icon close on the sheet. It is the only way "
                 "out of the sheet that Design drew, and it is a control a "
                 "student presses, so the census has to know it is ours by "
                 "way of Design's amendment rather than a stray."),
    ] + [
        # The six swatches. One entry each rather than a loop with a shared
        # label, because every failure message names the entry and "one of the
        # six swatches is missing" is not a sentence anybody can act on.
        dict(label="the %s swatch" % name.lower(),
             region="account-sheet", state="the account sheet", control=name,
             why="One of Design's six bench-theme swatches. It is pressable, "
                 "so it is in the control census as well as in the text, and "
                 "a registration that reached only the text would report "
                 "'controls only in port' and read like a bug in the port.")
        for name in ("CLAY", "CHALK", "MOSS", "HARBOUR", "DAMSON", "GRAPHITE")
    ] + [
        # ⊕ 23 Aug 2026 — PHASE 2. The flashcards card is a `<button>`, so it
        # is in the census as well as in the text, and its label is the whole
        # card — Design's own three values, rendered from Design's own deck on
        # both sides. Matched on EXACT text, like every entry here: a substring
        # rule would swallow anything that merely contains it.
        dict(label="the flashcards card", region="sidebar-flashcards",
             state="at rest", control="FLASHCARDS 06 Define diffusion. 01 / 06",
             why="Design's C2 card is pressable — it is what opens the "
                 "flashcards overlay — so a registration that reached only the "
                 "text would report 'controls only in port' and read like a "
                 "bug in the port rather than an amendment being adopted."),
    ],
}

# ── AMENDED OMISSIONS — where the port must NOT match Design's AMENDED file ─
#
# ⊕ 23 Aug 2026 — PHASE 1c, and it is the third corner of a square that had
# only two.
#
#   RULED_DIVERGENCE   in Design's ORIGINAL, ruled OUT of the port.
#   AMENDED_ADDITIONS  in Design's AMENDED delivery, merged INTO the port.
#   AMENDED_OMISSIONS  in Design's AMENDED delivery, and ruled out of the port
#                      on its way in.
#
# The account sheet is the first merged region that needed the third: Design
# draws an EMAIL row in it, and the ruling is that no student surface shows an
# email address. A class page is opened on shared classroom machines and on a
# projector; a school email is a real identifier and a real contact route, and
# it would be on screen for whoever is standing behind the student.
#
# ⚠️ NEITHER OF THE OTHER TWO COULD CARRY IT, and that is why this exists
# rather than being folded in. `RULED_DIVERGENCE` asserts the span is PRESENT
# in Design's original — the original has no account sheet at all, so that
# assertion is false and the entry would go red on a healthy page.
# `AMENDED_ADDITIONS` asserts the span is PRESENT IN THE PORT, which is the
# exact opposite of what is wanted. Registering an omission as either would
# have meant writing a pattern that lies about what it is for.
#
# ⚠️ AND LEAVING IT UNREGISTERED IS NOT NEUTRAL. Nothing strips it, nothing
# needs it, and every gate stays green — which is precisely the failure this
# repo keeps naming: the removal would be unwatched, and the day somebody
# widened the graft or dropped `omit` from the entry, a hundred and thirty-five
# children's email addresses would ship with a green build.
#
# STRIPS NOTHING. It is assertions only: the span is in Design's amended
# delivery (so a stale registration goes red when Design redraws), and it is
# not on the port (so a reverted ruling goes red on every drive).
#
# Entry shape: `label`, `region`, `pat`, `state`, `why` — the same as
# `AMENDED_ADDITIONS`, deliberately, so the two read as one mechanism.
AMENDED_OMISSIONS = {
    "class view": [
        dict(label="the account sheet's EMAIL row",
             region="account-sheet", state="the account sheet",
             pat=r"EMAIL ay@school\.uk ",
             why="RULED 23 Aug 2026 — no student surface shows an email "
                 "address. Nothing else on the student side does, and the "
                 "class page is read on shared classroom machines and "
                 "projectors. Removed at BUILD time by `omit` on the graft "
                 "(student_rulings.py), which is asserted from the other end: "
                 "the build stops if donor node 263 is no longer there to "
                 "remove."),
        # ── ⊕ 23 Aug 2026 — PHASE 3. THE ROUND'S `THIS WEEK` PANEL ────────
        #
        # Design draws a sidebar beside the round's question panel with three
        # figures, one sentence and a button. The whole panel — donor node 425
        # — is omitted by the graft, and the three registrations below are what
        # watch that it stays omitted. Split into three rather than one,
        # because the three are ruled out for three DIFFERENT reasons and a
        # single pattern would let two of them be reinstated silently under the
        # third one's justification.
        dict(label="the recall round's THIS WEEK figures",
             region="recall-round", state="the recall round",
             pat=r"THIS WEEK ANSWERED \d+ BEST STREAK \d+ ROUNDS \d+ ",
             why="RULED — nothing anywhere records a recall round. "
                 "`/api/class/practice` only reads, and no table carries a "
                 "class, a teaching week and a rung together, so ANSWERED and "
                 "ROUNDS are unrecorded; student-live.js has emitted "
                 "`practiceAnswered` and `recallRounds` as empty since the day "
                 "Design's 46 was found to be a drawing. BEST STREAK is real "
                 "inside one sitting and false the next morning, when a "
                 "student who answered thirty yesterday is shown 00 under a "
                 "heading that says THIS WEEK. The round shows the streak "
                 "where it is honest — `streakLabel`, live, inside the round."),
        dict(label="the recall round's 20-of-100 sentence",
             region="recall-round", state="the recall round",
             pat=r"Recall counts for 20 of the 100 points on the "
                 r"leaderboard\. Rounds are unlimited and do not need handing "
                 r"in\. ?",
             why="RULED 21 Aug 2026, and this is the THIRD place the same "
                 "apportionment has been drawn: the leaderboard's split bar, "
                 "its static ON TIME 40 / SCORE 40 / RECALL 20 legend, and now "
                 "here. The platform cannot compute it — nothing records a "
                 "recall round at all — so the sentence states a rule the "
                 "product does not implement. It is also platform "
                 "self-explanation on a student page (KS3 copy rule §8.10). "
                 "The half that IS true, that rounds are unlimited and hand "
                 "nothing in, is said twice over by the round itself: "
                 "`UNLIMITED ROUNDS` in the band, and Design's own "
                 "round-done line 'Go again as many times as you like. "
                 "Nothing here is handed in.'"),
        dict(label="the recall round's 'Open the assignment instead' button",
             region="recall-round", state="the recall round",
             pat=r"Open the assignment instead ?",
             why="It does not open the assignment. Design wires it to "
                 "`closeRecall`, so it closes the round and leaves the student "
                 "on their class page — which is what the two other controls "
                 "in the round already do and say so (`8r/Sc1` in the band, "
                 "`Back to my class` on the round-done card, both counted "
                 "before this was written). A control whose label names a "
                 "destination it does not go to is ruling P3's defect, and P1's "
                 "and P7's; the port has taken three of them out already."),
    ],
}

_OMIT_IN_AMENDED = "omitted-in-amended:"
_OMIT_IN_PORT = "omitted-still-in-port:"
_OMIT_IN_ORIGINAL = "omitted-was-in-original:"


def _apply_omissions(page, d_text, g_text, g_regions, amended_states,
                     problems, seen):
    """Record, per drive, what a registered omission looks like right now.

    Strips NOTHING from either side, and returns nothing — every verdict is a
    statement about the page rather than about one drive, so they are recorded
    here and reported once by `_omissions_seen`. The scopes split exactly as
    `_apply_additions` splits them, with one deliberate inversion:

      · PRESENT IN THE AMENDED DELIVERY'S REGION — once per page. Stale
        registration if it stops matching.
      · STILL ON THE PORT — recorded on ANY drive, and any one is fatal. This
        is the inversion: for an ADDITION, finding it once is the pass; for an
        omission, finding it once is the failure, because the ruling holds on
        every screen and there is no state in which it may come back.
      · IN DESIGN'S ORIGINAL — once per page. If it is, this is the wrong
        register and the entry belongs in `RULED_DIVERGENCE`.
    """
    import re
    adds = AMENDED_OMISSIONS.get(page) or ()
    if not adds or amended_states is None:
        return
    for add in adds:
        pat = add["pat"]
        reg = _amended_region(amended_states, add)
        if reg is not None and re.search(pat, reg["text"]):
            seen.add(_OMIT_IN_AMENDED + add["label"])
        # ⚠️ THE WHOLE PORT, NOT JUST ITS REGION. A ruling that says "this is
        # not on a student's screen" is not satisfied by the span moving to
        # another part of the same screen, and the region is exactly where a
        # careless fix would move it FROM.
        if re.search(pat, g_text):
            seen.add(_OMIT_IN_PORT + add["label"])
        port_reg = (g_regions or {}).get(add["region"])
        if port_reg is not None and re.search(pat, port_reg["text"]):
            seen.add(_OMIT_IN_PORT + add["label"])
        if re.search(pat, d_text):
            seen.add(_OMIT_IN_ORIGINAL + add["label"])


def _omissions_seen(page, seen, amended_states, problems):
    """Once per page: every registered omission is really an omission."""
    rows = []
    adds = list(AMENDED_OMISSIONS.get(page) or ())
    if not adds:
        return rows

    if amended_states is None:
        rows.append((page, "omissions · the amended delivery was driven",
                     "FAIL", "%d registration(s) with no amended reference"
                     % len(adds)))
        problems.append(
            "%s — %d omission(s) are registered and Design's AMENDED delivery "
            "was never driven, so nothing checked that Design still draws the "
            "thing this port is removing. Give the page `amended_root` / "
            "`amended` in PAIRS, or take the registrations out."
            % (page, len(adds)))
        return rows

    known_states = {lbl for lbl, _steps in AMENDED_DRIVES.get(page, ())}
    for add in adds:
        label, state = add["label"], add.get("state", "at rest")

        if state not in known_states:
            rows.append((page, "omissions · %s — the state is driven" % label,
                         "FAIL", "no AMENDED_DRIVES entry named %r" % state))
            problems.append(
                "%s — the omission %r names the state %r and AMENDED_DRIVES "
                "has no drive by that name, so the region it lives in is never "
                "reached and the entry cannot be checked against Design at "
                "all. Add the drive, or correct the state name."
                % (page, label, state))
            continue

        ok = (_OMIT_IN_AMENDED + label) in seen
        rows.append((page, "omissions · %s — in Design's amended delivery"
                     % label, "PASS" if ok else "FAIL",
                     "found in the %r region, %r" % (add["region"], state)
                     if ok else "NOT in the %r region of the amended delivery"
                     % add["region"]))
        if not ok:
            problems.append(
                "%s — the omission %r was NOT found in the %r region of "
                "Design's AMENDED delivery in the %r state. The registration "
                "is stale: Design has redrawn or removed it. If Design has "
                "removed it, this entry has nothing left to be about and the "
                "`omit` on the graft has nothing left to remove — check the "
                "build, which asserts the same thing from the other end, "
                "before deleting either." % (page, label, add["region"], state))

        bad = (_OMIT_IN_PORT + label) in seen
        rows.append((page, "omissions · %s — gone from the port" % label,
                     "FAIL" if bad else "PASS",
                     "STILL ON THE PORT" if bad
                     else "absent from the port on every drive, as the ruling "
                          "requires"))
        if bad:
            problems.append(
                "%s — the omission %r is BACK ON THE PORTED PAGE. This is a "
                "ruling about what a student's screen may show, and it has "
                "been reverted: either `omit` has been dropped from the graft "
                "in student_rulings.py, or the graft now copies a different "
                "subtree. Nothing here is cosmetic — put it back."
                % (page, label))

        bad = (_OMIT_IN_ORIGINAL + label) in seen
        rows.append((page, "omissions · %s — not in Design's original" % label,
                     "FAIL" if bad else "PASS",
                     "ALSO in the original delivery" if bad
                     else "absent from the original delivery, so this really "
                          "is about the amendment"))
        if bad:
            problems.append(
                "%s — the omission %r ALSO matches Design's ORIGINAL "
                "delivery. Then the port is not declining something Design "
                "added; it is removing something Design always drew, which is "
                "a RULED_DIVERGENCE with a ruling behind it. Move the entry."
                % (page, label))
    return rows


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

    # ── ⊕ 23 Aug 2026 — the OMISSIONS half of the same proof ─────────────
    #
    # ⚑ AND IT NEEDS ITS OWN, BECAUSE IT FAILS THE OTHER WAY ROUND. An
    # additions entry passes by FINDING its span on the port; an omission
    # passes by NOT finding it. A mechanism that recorded nothing at all —
    # a typo in a `seen` key, a registry read from the wrong page — would
    # look identical to a healthy omission and would report a clean page
    # forever. So the proof drives BOTH directions: a span that is absent
    # must pass, and the SAME span put back must fail.
    ofaults = []
    oentry = dict(label="a synthetic omission",
                  region="r",
                  pat=r"SECRET ",
                  state="at rest",
                  why="synthetic — exists only for the length of this proof")
    AMENDED_OMISSIONS[page] = [oentry]
    AMENDED_DRIVES[page] = [("at rest", [])]
    try:
        # (a) Design's amended file draws it; the port does not. That is the
        #     whole ruling, and it must report clean.
        oregion = {"change": "synthetic",
                   "text": "ALPHA SECRET BETA", "controls": []}
        oamended = {"at rest": {"regions": {"r": oregion}}}
        seen3, sink3 = set(), []
        _apply_omissions(page, d_text, "ALPHA BETA GAMMA",
                         {"r": {"change": "", "text": "ALPHA BETA",
                                "controls": []}},
                         oamended, sink3, seen3)
        rows3 = _omissions_seen(page, seen3, oamended, sink3)
        if sink3:
            ofaults.append(
                "a healthy omission — drawn by Design, absent from the port — "
                "was reported as a problem: %s" % sink3[0][:90])
        if not any(v == "PASS" for _p, _l, v, _d in rows3):
            ofaults.append("a healthy omission produced no PASS row at all, "
                           "so nothing was actually checked")

        # (b) the span COMES BACK on the port. The ruling has been reverted,
        #     and the gate must say so.
        seen4, sink4 = set(), []
        _apply_omissions(page, d_text, "ALPHA SECRET BETA GAMMA",
                         {"r": {"change": "", "text": "ALPHA SECRET BETA",
                                "controls": []}},
                         oamended, sink4, seen4)
        rows4 = _omissions_seen(page, seen4, oamended, sink4)
        if not sink4:
            ofaults.append(
                "the omitted span was put BACK on the port and the machinery "
                "reported nothing. An omission that cannot see its own ruling "
                "being reverted is a registration, not a gate")
        if not any(v == "FAIL" for _p, _l, v, _d in rows4):
            ofaults.append("the reverted omission produced no FAIL row")

        # (c) it is in Design's ORIGINAL as well — wrong register, and the
        #     machinery has to name the right one rather than pass.
        seen5, sink5 = set(), []
        _apply_omissions(page, "ALPHA SECRET BETA GAMMA", "ALPHA BETA GAMMA",
                         {}, oamended, sink5, seen5)
        rows5 = _omissions_seen(page, seen5, oamended, sink5)
        if not any("RULED_DIVERGENCE" in pr for pr in sink5):
            ofaults.append(
                "a span present in Design's ORIGINAL was accepted as an "
                "amended-delivery omission, so the two registers can be "
                "confused without the gate noticing")
    finally:
        AMENDED_OMISSIONS.pop(page, None)
        AMENDED_DRIVES.pop(page, None)

    rows, problems = [], []
    if ofaults:
        rows.append((disp, "the omissions machinery sees a ruling reverted",
                     "FAIL", "; ".join(ofaults)[:110]))
        problems.append(
            "the omissions self-proof FAILED: %s. Until this passes, every "
            "AMENDED_OMISSIONS entry is an unchecked promise — and the one "
            "registered today is the promise that no child's email address "
            "ships on a classroom projector." % "; ".join(ofaults))
    else:
        rows.append((disp, "the omissions machinery sees a ruling reverted",
                     "PASS",
                     "absent passes; the same span put back fails; a span "
                     "Design's original had is sent to RULED_DIVERGENCE"))
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
