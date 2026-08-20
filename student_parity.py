#!/usr/bin/env python3
"""student_parity.py — the generated student previews against Design's own file.

    python3 student_parity.py

Exit 0 clean, 1 on any parity failure or unregistered section.

`build_student.py` renders Design's standalone file and takes the DOM, so
exactness ought to be automatic. "Ought to" is the reason this exists: the
generator strips 28 base64 `@font-face` blocks, rewrites the font URLs, re-wraps
the root in its own shell and re-serves the whole thing from a different origin.
Every one of those is a chance for the copy to stop being a copy, and none of
them would announce itself — a page with no fonts, or with the design-system
CSS half-applied, still renders something that looks broadly right.

── The six layers ─────────────────────────────────────────────────────────

A. **Structural parity, measured against Design's file.** Same node count, same
   tag census, same visible text, same root box, same resolved font, ground and
   ink. Design's standalone and the generated page are driven side by side in
   the same browser at the same width; nothing is compared against a recorded
   constant, because a constant is a claim about the past.

B. **Every section registered.** The brief asks for a gate that FAILS ON ABSENT
   REGISTRATIONS. Layer A would pass a page that had quietly lost a whole
   section as long as Design's file lost it too — and it would say nothing at
   all about a section nobody had thought about. So every top-level section of
   the design root must appear in `SECTIONS` by name, and every registered
   section must be present on the page. A section arriving in a future delivery
   turns this red until somebody registers it, which is the point.

C. **The 390px gap, asserted as a KNOWN gap.** Phase 8a established that a
   snapshot cannot carry Design's ten JavaScript-computed breakpoint switches,
   so the previews scroll sideways at 390px where Design's own file does not.
   That is recorded rather than hidden — and it is ASSERTED, so that when 8c
   fixes it this gate goes red and has to be updated. A known defect that stops
   being true and leaves its note behind is how a report starts lying.

D. **The `--st-*` token contract.** `--st-ok-room` was minted on 20 Aug 2026
   under a ruling that made it GRAPHIC ONLY, and a prohibition nothing reads is
   a comment. The rule is parsed out of `3d-studio/src/styles/tokens.css` (the
   file Design's bundle exports under the path-mangled name
   `src-styles-tokens.css`) and swept on the generated pages — each of which is
   then swept a SECOND time with a deliberate violation injected, because a
   gate that cannot see and a corpus that is clean look identical from here.

   And the DELIVERY is driven, not merely read. Design's own class view paints
   the token as `color:` on the 9.5px `CORRECT` label, reachable only through
   Recall → pick the right option → Check. Registered in `ST_DELIVERY_KNOWN`
   and asserted both ways: expected in the delivery, forbidden in the port.

E. **No question count is ever a literal.** RULED 20 Aug 2026. Design's class
   view says eight questions and the assignment is fifteen, because they were
   drawn separately and Design would not edit an approved file unannounced.
   The count comes from the assignment, everywhere it appears. So no spelled-
   out or numeric count may be baked into a string the generator emits.

F. **No fabricated leaderboard split.** RULED 20 Aug 2026. Design's bar split
   is an approximation drawn for layout — `onTime = round(pts × 0.4)` capped at
   40, `recall = round(pts × 0.19)` capped at 20, score the remainder — and
   Design says do not ship it. A bar that apportions points a student did not
   earn that way is a lie told in a graph.

⚠️ E AND F BOTH PROVE THEMSELVES. Each is a source scan, and a source scan
over a corpus that does not yet contain the thing it looks for is
indistinguishable from a broken scan. So each is also run against a fixture
that DOES contain it, and goes red if the fixture comes back clean.
"""

import json
import os
import sys
import time

REF = os.path.join("docs", "ks3", "design-reference", "student")
SITE = "mrbadmus_site"

PAIRS = [
    dict(
        name="class view",
        design="standalone/MrBadmusAI Class View.html",
        generated="student/class-preview.html",
    ),
    dict(
        name="assignment",
        design="standalone/MrBadmusAI Assignment.html",
        generated="student/assignment-preview.html",
    ),
]

DESKTOP = (1460, 1200)
PHONE = (390, 844)

# ── B · every top-level section of each page, by the text it opens with ───
#
# Registered by a stable, human-readable landmark rather than by index or by
# class name: Design's classes are compiler-generated (`scp0`, `scp1`) and an
# index changes the moment anything is inserted above. The eyebrow text is what
# a person would use to point at the section, and it is what the handoff notes
# call it.
SECTIONS = {
    # ⚠️ REGISTERED AGAINST THE DEFAULT STATE, which is the only state a
    # snapshot has. The first draft of this list registered the work list by
    # "Question by question" — the heading the handoff notes give the marked
    # breakdown — and layer B went red twice, correctly: that text is inside
    # the EXPANDED work row, behind an interaction, so it is in neither the
    # generated page nor Design's own file at rest. Reading a README is not
    # the same as reading the page.
    "class view": [
        ("the header and brand", "MrBadmusAI"),
        ("the nav", "My class"),
        ("the account", "Sign out"),
        ("the breadcrumb", "OVERVIEW"),
        ("the term line", "AUTUMN TERM · WEEK 04 / 12"),
        ("the welcome", "WELCOME BACK, AYO"),
        ("the class facts", "28 STUDENTS"),
        ("reading · handed in", "HANDED IN"),
        ("reading · on time", "ON TIME"),
        ("reading · average score", "AVG SCORE"),
        ("reading · recall", "ANSWERED · WK 04"),
        ("the bench", "ON THE BENCH NOW"),
        ("the bench tasks", "Answer the eight questions"),
        ("the bench CTA", "Open the assignment"),
        ("the assignment docket", "THIS WEEK’S ASSIGNMENT"),
        ("the docket footer", "40 POINTS AT STAKE"),
        ("the term spine", "TERM SPINE"),
        ("the spine legend", "MISSED"),
        ("the recall card", "Start a round"),
        ("the work list", "WORK"),
        ("the work tabs", "MARKED 3"),
        ("a marked work row", "READ FEEDBACK"),
        ("a missed work row", "Lab safety check"),
        ("lessons in this topic", "LESSONS IN THIS TOPIC"),
        ("a lesson row", "Using a microscope"),
        ("shoutouts", "SHOUTOUTS"),
        ("the leaderboard", "LEADERBOARD"),
        ("the leader card", "TOP OF WEEK 04"),
        ("the pinned self row", "YOU"),
        ("the leaderboard legend", "RESETS EVERY MONDAY 00:00"),
    ],
    "assignment": [
        ("the back chevron and class", "8r/Sc1"),
        ("the assignment title", "Cells & microscopy"),
        ("the question count", "15 QUESTIONS"),
        ("the timer", "06:"),
        ("the due line", "DUE THU 18 SEP, 18:00"),
        ("the question eyebrow", "QUESTION 07 OF 15"),
        ("the question", "plant cell"),
        ("the figure", "FIGURE"),
        ("the figure hint", "TAP TO ENLARGE"),
        ("the marker row", "ALL 15 QUESTIONS"),
        ("the readout", "ANSWERED"),
        ("the action bar", "Next"),
    ],
}

# ── C · the 390px gap, per page and not in general ────────────────────────
#
# ⚠️ MEASURED PER PAGE, because the first draft asserted it of BOTH and the
# gate went red on the assignment — which is CLEAN at 390px. Phase 8a's commit
# says "the previews" scroll sideways; that was over-broad and this is the
# correction. The class view has the gap because its layout is grids the ten
# switches reshape — the twelve-column term spine alone needs 662px. The
# assignment is one question on a single column, so its eight switches frozen
# at desktop values happen to produce nothing that overflows.
#
# True/False here is an ASSERTION either way. If the class view becomes clean,
# this goes red and somebody must come and delete it; if the assignment stops
# being clean, that is a regression. A known defect that silently stops being
# true is how a report starts lying.
EXPECTED_390_GAP = {
    "class view": True,
    "assignment": False,
}

_PROBE = """(function () {
  var r = document.querySelector('.rd[data-mode="ks3"]');
  if (!r) { return JSON.stringify({error: 'no design root on the page'}); }
  var cs = getComputedStyle(r), d = document.documentElement;
  var all = r.querySelectorAll('*'), tags = {};
  for (var i = 0; i < all.length; i++) {
    tags[all[i].tagName] = (tags[all[i].tagName] || 0) + 1;
  }
  var box = r.getBoundingClientRect();
  var over = 0;
  for (var j = 0; j < all.length; j++) {
    var rc = all[j].getBoundingClientRect();
    if (rc.width === 0 && rc.height === 0) { continue; }
    if (rc.right > d.clientWidth + 0.5 || rc.left < -0.5) { over += 1; }
  }
  return JSON.stringify({
    error: '',
    nodes: all.length,
    tags: tags,
    text: (r.innerText || '').replace(/\\s+/g, ' ').trim(),
    w: Math.round(box.width), h: Math.round(box.height),
    font: cs.fontFamily, bg: cs.backgroundColor, ink: cs.color,
    docScroll: d.scrollWidth, docClient: d.clientWidth,
    overflowing: over,
    // ⚠️ `document.fonts.size` COUNTS DECLARATIONS, NOT LOADS, and
    // `document.fonts.check()` returns true even for a family that does not
    // exist because it reports "can be rendered" — with a fallback. The first
    // draft of this gate used `.size` and stayed green with every font URL
    // pointed at a directory that does not exist. STATUS is the only one of
    // the three that discriminates: measured, a good page reports
    // {loaded: 4, unloaded: 3} and a broken path reports {error: 4,
    // unloaded: 3}. `unloaded` is normal — it is a face the page has not
    // needed to paint yet.
    fontStatus: (function () {
      var o = {};
      if (!document.fonts) { return o; }
      document.fonts.forEach(function (f) { o[f.status] = (o[f.status] || 0) + 1; });
      return o;
    })()
  });
})()"""


def grab(cdp, root, path, viewport):
    server, port = cdp.serve(root)
    try:
        with cdp.Browser() as b:
            page = b.attach()
            page.set_viewport(*viewport)
            page.goto("http://127.0.0.1:%d/%s" % (port, path.replace(" ", "%20")))
            time.sleep(2.5)
            got = json.loads(page.eval(_PROBE))
            if got.get("error"):
                raise SystemExit("student_parity: %s — %s" % (path, got["error"]))
            return got
    finally:
        server.shutdown()


def run(cdp):
    problems, rows = [], []

    for pair in PAIRS:
        name = pair["name"]
        d = grab(cdp, REF, pair["design"], DESKTOP)
        g = grab(cdp, SITE, pair["generated"], DESKTOP)

        # ── A · structural parity ──────────────────────────────────────
        def same(field, label, tol=0):
            a, b = d[field], g[field]
            ok = (abs(a - b) <= tol) if isinstance(a, (int, float)) else (a == b)
            rows.append((name, "A · " + label, "PASS" if ok else "FAIL",
                         "%s" % a if ok else "Design %r vs generated %r"
                         % (a, b)))
            if not ok:
                problems.append("%s — %s: Design %r, generated %r"
                                % (name, label, a, b))
            return ok

        same("nodes", "node count")
        same("tags", "tag census")
        same("text", "visible text")
        same("w", "root width")
        same("h", "root height", tol=1)
        same("font", "resolved font family")
        same("bg", "resolved ground")
        same("ink", "resolved ink")

        # The fonts are the thing the generator most plausibly breaks: it
        # rewrites 28 face declarations to a served path. A page whose faces
        # all 404 still renders, in a fallback, and looks broadly right.
        st = g.get("fontStatus") or {}
        loaded, errored = st.get("loaded", 0), st.get("error", 0)
        ok = loaded > 0 and errored == 0
        rows.append((name, "A · font faces load from /shared/fonts/",
                     "PASS" if ok else "FAIL",
                     "%d loaded, %d errored, %d not yet needed"
                     % (loaded, errored, st.get("unloaded", 0))))
        if not ok:
            problems.append(
                "%s — the @font-face rewrite to /shared/fonts/ is not "
                "resolving: %d face(s) loaded, %d in error. The page still "
                "renders, in a fallback, which is why this is measured rather "
                "than looked at" % (name, loaded, errored))

        # ── B · every section registered, and every registration present ──
        registered = SECTIONS.get(name)
        if registered is None:
            problems.append("%s has NO registration list in SECTIONS. A page "
                            "this gate does not know the sections of is a page "
                            "it is not gating." % name)
            rows.append((name, "B · page registered", "FAIL", "absent"))
        else:
            missing = [(lbl, needle) for lbl, needle in registered
                       if needle.lower() not in g["text"].lower()]
            ok = not missing
            rows.append((name, "B · %d registered section(s) present"
                         % len(registered), "PASS" if ok else "FAIL",
                         "all present" if ok else
                         "; ".join("%s (looked for %r)" % m for m in missing)))
            if missing:
                problems.append(
                    "%s — %d registered section(s) absent from the generated "
                    "page: %s" % (name, len(missing),
                                  ", ".join(m[0] for m in missing)))

            # And the other direction: text Design shows that no registration
            # accounts for cannot be detected in general, but a section count
            # can be. Design's own file is the authority.
            d_missing = [lbl for lbl, needle in registered
                         if needle.lower() not in d["text"].lower()]
            if d_missing:
                problems.append(
                    "%s — %d registration(s) name a section that is NOT in "
                    "DESIGN's file either: %s. The registry has drifted from "
                    "the delivery" % (name, len(d_missing),
                                      ", ".join(d_missing)))
                rows.append((name, "B · registry matches the delivery", "FAIL",
                             ", ".join(d_missing)))
            else:
                rows.append((name, "B · registry matches the delivery", "PASS",
                             "every registration is in Design's file too"))

        # ── C · the 390px gap, asserted as a KNOWN gap ─────────────────
        dp = grab(cdp, REF, pair["design"], PHONE)
        gp = grab(cdp, SITE, pair["generated"], PHONE)
        design_clean = dp["docScroll"] <= dp["docClient"]
        gen_clean = gp["docScroll"] <= gp["docClient"]

        if not design_clean:
            problems.append(
                "%s — DESIGN's own file scrolls sideways at 390px "
                "(scrollWidth %s vs clientWidth %s). That is a finding about "
                "the delivery, not about the generator"
                % (name, dp["docScroll"], dp["docClient"]))
            rows.append((name, "C · Design is clean at 390px", "FAIL",
                         "scrollWidth %s" % dp["docScroll"]))
        else:
            rows.append((name, "C · Design is clean at 390px", "PASS",
                         "scrollWidth %s = clientWidth" % dp["docScroll"]))

        # ⚖️ THE KNOWN GAP IS ASSERTED, NOT TOLERATED. If the generated page
        # becomes clean at 390px — because 8c reproduced Design's ten switches
        # — this goes RED and somebody has to come here and delete it. That is
        # deliberate. A known defect that silently stops being true is how a
        # parity report starts lying.
        expect_gap = EXPECTED_390_GAP.get(name)
        if expect_gap is None:
            problems.append("%s has no entry in EXPECTED_390_GAP" % name)
            rows.append((name, "C · 390px behaviour registered", "FAIL",
                         "absent"))
        elif expect_gap and gen_clean:
            problems.append(
                "%s — the generated page NO LONGER scrolls sideways at 390px. "
                "That is good news and it makes this assertion stale: phase 8a "
                "recorded the ten JS-computed breakpoint switches as "
                "unreproducible by a snapshot. If 8c has landed, set "
                "EXPECTED_390_GAP[%r] = False and delete the ⚑ block in "
                "build_student.py" % (name, name))
            rows.append((name, "C · the KNOWN 390px gap still holds", "FAIL",
                         "generated page is clean — the gap is fixed, update "
                         "this gate"))
        elif expect_gap:
            rows.append((name, "C · the KNOWN 390px gap still holds", "PASS",
                         "generated scrollWidth %s vs %s, %d element(s) "
                         "overflowing — Design's ten JS switches are frozen at "
                         "their desktop values (phase 8a)"
                         % (gp["docScroll"], gp["docClient"],
                            gp["overflowing"])))
        elif gen_clean:
            rows.append((name, "C · clean at 390px, as registered", "PASS",
                         "generated scrollWidth %s = clientWidth; its eight "
                         "switches frozen at desktop values happen to overflow "
                         "nothing" % gp["docScroll"]))
        else:
            problems.append(
                "%s — registered as CLEAN at 390px and it is not: scrollWidth "
                "%s against clientWidth %s, %d element(s) overflowing. That is "
                "a regression, not a known gap"
                % (name, gp["docScroll"], gp["docClient"], gp["overflowing"]))
            rows.append((name, "C · clean at 390px, as registered", "FAIL",
                         "scrollWidth %s, %d overflowing"
                         % (gp["docScroll"], gp["overflowing"])))

    rows_d, problems_d = run_token_contract(cdp)
    rows.extend(rows_d)
    problems.extend(problems_d)

    for fn in (run_no_literal_count, run_no_fabricated_split):
        r, pr = fn()
        rows.extend(r)
        problems.extend(pr)

    return rows, problems


# ── E · no question count is ever a literal ───────────────────────────────
#
# The files the student pages are BUILT from. Design's delivery is deliberately
# not in this list: `docs/ks3/design-reference/` is a frozen reference and the
# literal "eight" is in it, correctly — Design drew the two screens separately
# and said so rather than editing an approved file unannounced. What must not
# happen is that literal surviving into something we emit.
COUNT_SOURCES = [
    "build_student.py",
    "shared/student.js",
    "shared/student-assignment.js",
]

# Spelled out, and as digits where the digits are a COUNT rather than an index.
# "QUESTION 07 OF 15" is two numbers and neither is a literal count — the 15 is
# the total and must come from the data, the 07 is a position. So the scan
# looks for the count in the shapes it actually takes in copy.
_COUNT_WORDS = ("one", "two", "three", "four", "five", "six", "seven",
                "eight", "nine", "ten", "eleven", "twelve", "thirteen",
                "fourteen", "fifteen", "sixteen", "twenty")

_COUNT_PATTERNS = [
    # "Answer the eight questions", "all fifteen questions"
    r"\b(?:%s)\s+questions?\b" % "|".join(_COUNT_WORDS),
    # "8 questions", "15 QUESTIONS", "All 15 questions"
    r"\b\d{1,3}\s+questions?\b",
    # "QUESTIONS 8" — the docket's label/value pair
    r"\bquestions?\s+\d{1,3}\b",
    # A hard-coded TOTAL at the tail of a string: `" OF 15"`, `" / 15"`.
    # ⚠️ ANCHORED ON THE QUOTE, NOT ON END-OF-LINE. The first draft anchored on
    # `$` and matched nothing even in the fixture written to trip it — a count
    # literal lives INSIDE a string, so the character after it is a quote or a
    # backtick, essentially never a newline. The proof caught that, which is
    # the entire reason the proof runs before the scan is allowed to report.
    r"(?:\bof|/)\s*(?:%s|\d{1,3})\s*[\"\'`]" % "|".join(_COUNT_WORDS),
]

# The fixture that proves the scan can see. Every pattern above must fire on
# it; if any does not, that pattern is decoration.
_COUNT_FIXTURE = """
    a = "Answer the eight questions"
    b = "WEEK 04 \u00b7 15 QUESTIONS"
    c = "QUESTIONS 8"
    d = "Look through all fifteen"
    e = "QUESTION 07 OF 15"
    f = "ANSWERED 06 / 15"
"""


def _scan_counts(text):
    import re
    hits = []
    for pat in _COUNT_PATTERNS:
        for m in re.finditer(pat, text, re.I | re.M):
            hits.append((pat, m.group(0).strip()))
    return hits


def run_no_literal_count():
    rows, problems = [], []

    # The proof first, so a scan that cannot see never gets to report clean.
    proved = {pat for pat, _ in _scan_counts(_COUNT_FIXTURE)}
    missing = [p for p in _COUNT_PATTERNS if p not in proved]
    ok = not missing
    rows.append(("question count",
                 "E · the scan sees a deliberate literal count",
                 "PASS" if ok else "FAIL",
                 "all %d pattern(s) fire on the fixture" % len(_COUNT_PATTERNS)
                 if ok else "%d pattern(s) matched nothing: %s"
                 % (len(missing), missing)))
    if missing:
        problems.append(
            "E — %d of the question-count patterns matched nothing even in the "
            "fixture written to trip them. A pattern that cannot fire is "
            "decoration, and a scan carrying one reports clean for the wrong "
            "reason." % len(missing))
        return rows, problems

    scanned = 0
    for rel in COUNT_SOURCES:
        if not os.path.exists(rel):
            continue                       # not built yet — E waits for it
        scanned += 1
        hits = _scan_counts(open(rel, encoding="utf-8").read())
        for _pat, got in hits:
            problems.append(
                "E — %s carries the literal question count %r. RULED 20 Aug "
                "2026: the count comes from the assignment, everywhere it "
                "appears — the docket row, the bench task, the blurb and every "
                "count on the assignment page. Design's file says eight and "
                "the assignment is fifteen, which is exactly what a literal "
                "buys you." % (rel, got))
    ok = not problems
    rows.append(("question count",
                 "E · %d built source(s) carry no literal count" % scanned,
                 "PASS" if ok else "FAIL",
                 "clean" if ok else "%d literal(s)" % len(problems)))
    return rows, problems


# ── F · no fabricated leaderboard split ───────────────────────────────────
#
# Design's own words: *"the split shown in the bars is an approximation for
# drawing only (onTime = round(pts × 0.4) capped at 40, recall = round(pts ×
# 0.19) capped at 20, score is the remainder). Real per-component values come
# from the API. Do not ship the approximation."*
#
# The scan looks for the CONSTANTS, because that is what would actually be
# copied across. 0.4 and 0.19 together in a file that also mentions the
# leaderboard is the signature; either alone is an ordinary number.
_SPLIT_MARKERS = ("0.19", ".19")


def run_no_fabricated_split():
    import re
    rows, problems = [], []

    fixture = "wOnTime: Math.round(pts * 0.4), wRecall: Math.round(pts * 0.19)"
    ok = bool(_scan_split(fixture))
    rows.append(("leaderboard split",
                 "F · the scan sees the drawn approximation",
                 "PASS" if ok else "FAIL",
                 "the fixture trips it" if ok else "the fixture came back "
                 "clean, so this scan is blind"))
    if not ok:
        problems.append(
            "F — the leaderboard-split scan did not fire on a fixture "
            "containing Design's own approximation. It is blind, so its "
            "silence on the real sources means nothing.")
        return rows, problems

    scanned = 0
    for rel in COUNT_SOURCES:
        if not os.path.exists(rel):
            continue
        scanned += 1
        for got in _scan_split(open(rel, encoding="utf-8").read()):
            problems.append(
                "F — %s carries Design's drawn leaderboard approximation "
                "(%r). RULED 20 Aug 2026: derive the real per-component "
                "values, and where a component cannot be computed yet show "
                "the TOTAL and omit the split. A bar that apportions points a "
                "student did not earn that way is a lie told in a graph."
                % (rel, got))
    ok = not problems
    rows.append(("leaderboard split",
                 "F · %d built source(s) carry no fabricated split" % scanned,
                 "PASS" if ok else "FAIL",
                 "clean" if ok else "%d site(s)" % len(problems)))
    return rows, problems


def _scan_split(text):
    """The 0.4 / 0.19 pair, which is Design's approximation and nothing else."""
    import re
    hits = []
    for m in re.finditer(r"\*\s*0?\.19\b|round\([^)]*0?\.4\b[^)]*\)"
                         r"|0?\.19\s*\)", text):
        hits.append(m.group(0).strip())
    return hits


# ── D · the --st-* token contract ─────────────────────────────────────────
_CLICK = """(function (label) {
  var hit = null;
  document.querySelectorAll('button,a').forEach(function (e) {
    if (!hit && (e.innerText || '').trim() === label) { hit = e; }
  });
  if (!hit) { return 'MISS:' + label; }
  hit.click(); return 'ok';
})(%s)"""

_PICK = """(function (n) {
  var r = document.querySelector('.rd[data-mode="ks3"]');
  var opts = [].slice.call(r.querySelectorAll('button')).filter(function (e) {
    return /^[ABCD]\\n/.test((e.innerText || '').trim());
  });
  if (opts.length <= n) { return 'no option ' + n; }
  opts[n].click(); return 'ok';
})(%d)"""


def _drive_recall_correct(page, url):
    """Design's recall round, driven to the CORRECT-feedback state.

    Returns True once the panel reads CORRECT.

    ⚠️ THE RIGHT OPTION IS FOUND BY TRYING, NOT BY READING `q.a` OUT OF THE
    LOGIC CLASS. The answer index is Design's data and this gate has no
    business knowing it; a question whose answer moved would then silently
    stop being driven and the gate would report on a state it never reached.

    ⚠️ AND EACH ATTEMPT RELOADS. `Check` is terminal for the question — the
    round is locked and the only way on is `Next question`, which is a
    DIFFERENT question with a different answer. Trying option 1 after option 0
    without reloading therefore tests nothing. The first draft of this did
    exactly that and would have given up after one wrong guess.
    """
    for n in range(4):
        page.goto(url)
        time.sleep(2.2)
        page.eval(_CLICK % json.dumps("Recall"))
        time.sleep(0.7)
        if str(page.eval(_PICK % n)).startswith("no option"):
            return False
        time.sleep(0.35)
        page.eval(_CLICK % json.dumps("Check"))
        time.sleep(0.8)
        hit = page.eval("(function(){var r=document.querySelector("
                        "'.rd[data-mode=\"ks3\"]'); return (r.innerText||'')"
                        ".indexOf('CORRECT') > -1 ? 'y' : 'n';})()")
        if hit == "y":
            return True
    return False


def run_token_contract(cdp):
    """Layer D: the `--st-*` rules, on the port and on the delivery."""
    import ks3_parity as P

    rows, problems = [], []

    probs, n_rules, n_pages, n_proofs = P.check_st_token_contract(SITE, cdp)
    ok = not probs
    rows.append(("token contract",
                 "D · %d `--st-*` rule(s) enforced on %d generated page(s)"
                 % (n_rules, n_pages),
                 "PASS" if ok else "FAIL",
                 "no violation" if ok else "; ".join(probs)[:140]))
    problems.extend(probs)

    # The proof. A sweep that finds nothing has said nothing until it has been
    # shown finding something.
    want = n_pages * sum(1 for r in P.parse_st_token_rules(".").values()
                         if r[0] == "no-text")
    ok = n_proofs == want and want > 0
    rows.append(("token contract",
                 "D · the sweep catches a DELIBERATE violation",
                 "PASS" if ok else "FAIL",
                 "%d of %d injected violation(s) caught" % (n_proofs, want)))
    if not ok:
        problems.append(
            "the `--st-*` sweep caught %d of %d deliberately injected "
            "violations. Until it catches all of them, its silence on the real "
            "pages proves nothing." % (n_proofs, want))

    # ── the delivery, driven ───────────────────────────────────────────
    spec = [{"name": n, "rule": r, "hex": v.upper()}
            for n, (r, v) in sorted(P.parse_st_token_rules(".").items())
            if v.startswith("#")]
    js = P._TOKEN_SWEEP_JS % (json.dumps(spec), json.dumps(P.ST_SWEEP_ROOT))

    for name, known in sorted(P.ST_DELIVERY_KNOWN.items()):
        server, port = cdp.serve(REF)
        found = []
        try:
            with cdp.Browser() as b:
                page = b.attach()
                page.set_viewport(*DESKTOP)
                url = ("http://127.0.0.1:%d/%s"
                       % (port, known["page"].replace(" ", "%20")))
                reached = _drive_recall_correct(page, url)
                if not reached:
                    problems.append(
                        "%s — the delivery could not be driven to %r, so the "
                        "registered violation was neither confirmed nor "
                        "cleared. A state this gate cannot reach is a state it "
                        "is not gating." % (name, known["state"]))
                    rows.append(('token contract',
                                 "D · the delivery driven to %s" % known["state"],
                                 "FAIL", "could not reach the state"))
                    continue
                found = [x for x in (page.eval(js) or [])
                         if x.get("text") == known["text"]
                         and x.get("token") == known["token"]]
        finally:
            server.shutdown()

        if found:
            rows.append(("token contract",
                         "D · the KNOWN delivery violation still holds",
                         "PASS",
                         "Design paints `%s` on %r at %s — the port must use "
                         "`%s` instead"
                         % (known["token"], known["text"], known["state"],
                            known["fix_in_port"])))
        else:
            problems.append(
                "%s — the registered violation is GONE from the delivery: "
                "Design no longer paints `%s` on %r. Good news, and it makes "
                "this registration stale — delete the `%s` entry in "
                "ks3_parity.ST_DELIVERY_KNOWN. A known defect that silently "
                "stops being true is how a report starts lying."
                % (name, known["token"], known["text"], name))
            rows.append(("token contract",
                         "D · the KNOWN delivery violation still holds",
                         "FAIL", "it is fixed — deregister it"))

    return rows, problems


def main():
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import ks3_browser as cdp

    if not os.path.isdir(REF):
        raise SystemExit("student_parity: no design reference at %s" % REF)

    print("── the student preview parity gate ──")
    rows, problems = run(cdp)
    last = None
    for page, label, verdict, detail in rows:
        if page != last:
            print("\n  %s" % page)
            last = page
        print("    %-4s %-46s %s" % (verdict, label, detail[:96]))

    print()
    if problems:
        print("  %d PROBLEM(S):" % len(problems))
        for p in problems:
            print("    · %s" % p)
        return 1
    print("  PASS  both previews reproduce Design's file exactly at desktop; "
          "every registered section is present; the known 390px gap is still "
          "exactly where phase 8a left it; `--st-ok-room` is graphic-only on "
          "both pages and the sweep proved it can see; and no built source "
          "carries a literal question count or Design's drawn leaderboard "
          "split.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
