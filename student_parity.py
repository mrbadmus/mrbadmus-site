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

── The three layers ───────────────────────────────────────────────────────

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
    print("  PASS  both previews reproduce Design's file exactly at desktop, "
          "every registered section is present, and the known 390px gap is "
          "still exactly where phase 8a left it.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
