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
SWITCHES = "student_switches.json"

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

# ── C · every band, asserted straight ─────────────────────────────────────
#
# ⊕ PHASE 2, 20 Aug 2026. This used to be `EXPECTED_390_GAP`, a registry
# recording that the class view scrolled sideways at 390px and asserting that
# it still did, so that fixing it would turn this gate red and force somebody
# to come here. That is exactly what happened, and this is the update it was
# asking for.
#
# THE GAP IS CLOSED FOR LAYOUT. Both pages are now clean at 360, 390, 820 and
# 1460 — no document overflow and no element crossing the root's edges. The
# assertion is therefore no longer "a known defect still holds"; it is the
# plain thing a student page has to do.
#
# ⚑ AND A DIFFERENT GAP IS REGISTERED IN ITS PLACE, because the first one was
# not the whole story and a report that swapped a true note for a silence would
# be worse than the note. Design switches discretely THREE ways: by inline
# style (19 declarations — reapplied), by text (1 string — swapped), and by
# PRESENCE. Presence has two halves. Nodes Design renders at desktop and not
# below can be hidden, and are: 95 of them. Nodes Design renders BELOW desktop
# and not at it cannot be conjured into a desktop snapshot, and there are 52:
#
#     class view   6   the work rows' mono meta line, `W04 · DUE THU 18:00`
#     assignment  46   the marker strip (15 cells) and the readout row
#
# Those are asserted BY COUNT below. A number that moves means Design's
# delivery moved or the extraction did, and either way somebody should look.
UNCREATABLE = {
    "class view": 6,
    "assignment": 46,
}

# Every band the pages are asserted at. 360 and 390 are the primary targets;
# 820 and 1460 are the tablet and desktop bands. Measured across the 19
# switched declarations, 360 and 390 differ in none of them — which is Design's
# "same layout as 390 throughout, no further breakpoint", confirmed rather than
# taken on trust.
ASSERT_BANDS = [360, 390, 820, 1460]

# ── G · touch targets ─────────────────────────────────────────────────────
#
# Design's §6: "40px minimum, everywhere, at every width" — nav items, avatar,
# bench tasks, week bars, work rows, work tabs, leaderboard week chips, the
# top-5/10 toggle, recall options, every button — and "the account sheet's rows
# are 44px".
#
# ⚠️ MEASURED ON THE HIT BOX, NOT ON THE FONT. A 21px marker inside a 44px row
# is compliant and a naive per-element check would call it a failure; Design
# says so explicitly ("the touch minimum is met by the row, not by the
# marker"). So an element is compliant if IT or an ancestor that is itself a
# control reaches the floor.
TOUCH_FLOOR = 40
TOUCH_EXEMPT_NOTE = ("a control inside a control — the outer one carries the "
                     "hit box, which is Design's own rule for the marker strip")

# ⚑ THE DELIVERY DOES NOT MEET ITS OWN STATED FLOOR, and this is the count.
# Measured on Design's standalone files, not on ours, with the control-strip
# rule above applied — so the marker row and the work tabs and the week chips
# are already excused on Design's own reasoning, and what is left is what is
# left. The ASSIGNMENT is clean at every band. The class view is not:
#
#   at 390px, four:
#     MrBadmusAI    125x20   the brand
#     8r/Sc1         48x12   the breadcrumb crumb
#     Recall         38x40   a nav item  — Design's §6 list names "nav items"
#     AY             30x40   the avatar  — Design's §6 list names "avatar"
#
#   at 1460px, three: the brand at 143x20, `Settings` at 57x15, the crumb.
#
# Two of the four at phone width are on Design's OWN list of what the 40px
# floor covers, and the avatar at 30px is the one a student reaches for most —
# it is the whole account menu below 720px. This is not a boundary case.
#
# The generated page reproduces all four exactly, which is the correct
# behaviour for a reproduction and is why the assertion above is "no worse than
# Design" rather than "meets the floor". Closing it means changing sizes Design
# drew, and that is Design's call or Mide's, never a generator's.
DELIVERY_TOUCH_SHORTFALL = {
    "class view": {360: 4, 390: 4, 820: 4, 1460: 3},
    "assignment": {360: 0, 390: 0, 820: 0, 1460: 0},
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
    // ── the shim's own report ───────────────────────────────────────
    band: r.getAttribute('data-mrb-band'),
    applied: r.getAttribute('data-mrb-applied'),
    textSwaps: r.getAttribute('data-mrb-text'),
    hidden: r.getAttribute('data-mrb-hidden'),
    absent: r.getAttribute('data-mrb-absent'),
    mismatch: r.getAttribute('data-mrb-mismatch'),

    // ── every switched declaration, keyed the way the table keys them ──
    //
    // Read as the RESOLVED value on the element, not as the inline string, so
    // Design's file and the generated page are compared on what the browser
    // actually laid out with. An inline `grid-template-columns: 1fr` and a
    // computed `minmax(0px, 1fr)` are the same layout and different strings.
    switches: (function () {
      var out = {}, seen = {}, want = window.__MRB_PARITY_SWITCHES__ || null;
      var els = r.querySelectorAll('[data-dc-tpl]');
      for (var i = 0; i < els.length; i++) {
        var el = els[i], d = el.getAttribute('data-dc-tpl');
        seen[d] = (seen[d] || 0) + 1;
        if (want && !want[d]) { continue; }
        var props = want ? want[d] : null;
        if (!props) { continue; }
        var cs = getComputedStyle(el);
        for (var q = 0; q < props.length; q++) {
          out[d + '#' + seen[d] + '/' + props[q]] =
            cs.getPropertyValue(props[q]).trim();
        }
      }
      return out;
    })(),

    // ── touch targets ──────────────────────────────────────────────────
    //
    // Design's floor is 40px at every width. Measured on the HIT BOX: an
    // element is compliant if it, or an ancestor that is itself a control,
    // reaches the floor. Design's own rule for the marker strip is that "the
    // touch minimum is met by the row, not by the marker", so a 21px marker
    // inside a 44px row is compliant and a naive per-element check would call
    // it a failure.
    controls: 0, smallest: null, smallTargets: (function () {
      var out = [], sm = null, n = 0;
      var els = r.querySelectorAll('button, a[href], [role="button"], input, select');
      for (var i = 0; i < els.length; i++) {
        var el = els[i], cs = getComputedStyle(el);
        if (cs.display === 'none' || cs.visibility === 'hidden') { continue; }
        var b = el.getBoundingClientRect();
        if (b.width === 0 && b.height === 0) { continue; }
        n += 1;
        var hit = Math.min(b.width, b.height);

        // (a) A CONTROL NESTED IN A CONTROL: the outer one carries the hit
        //     box, so the inner one's size is not what a thumb aims at. This
        //     one does walk up, because nesting can be several deep.
        var e = el.parentElement;
        while (hit < 40 && e && e !== r) {
          if (e.matches('button, a[href], [role="button"], label')) {
            var pb = e.getBoundingClientRect();
            hit = Math.max(hit, Math.min(pb.width, pb.height));
          }
          e = e.parentElement;
        }

        // (b) A UNIFORM CONTROL STRIP. Design's §3, in as many words: the
        //     marker row "is 15 buttons, but every one of them opens the same
        //     thing: a grid sheet under the chrome. So the touch minimum is
        //     met by the row, not by the marker — there is no 21px tap target
        //     anywhere."
        //
        //     ⚠️ THE IMMEDIATE PARENT ONLY, AND EVERY CHILD A CONTROL. The
        //     first draft of this walked all ancestors and asked only for two
        //     controls somewhere inside — which exempted almost everything,
        //     because somewhere up every chain there is a big container with
        //     two buttons in it. It took the class view's under-floor count
        //     from eleven to one and would have gone on reporting one however
        //     small anything got. A gate that stops checking is worse than no
        //     gate, because it also reports PASS.
        //
        //     So: the strip is the DIRECT parent, every element child of it is
        //     a control, there are at least three of them, the strip itself
        //     meets the floor, and the cell already spans the floor in one
        //     direction (the markers are 21x44 — a thumb has 44px of travel).
        //     Design's header, where Settings sits beside Sign out, fails the
        //     "every child a control" test and stays counted.
        if (hit < 40 && el.parentElement && el.parentElement !== r) {
          var par = el.parentElement, kids = par.children;
          var allCtl = kids.length >= 3;
          for (var c = 0; c < kids.length && allCtl; c++) {
            if (!kids[c].matches('button, a[href], [role="button"]')) {
              allCtl = false;
            }
          }
          var prb = par.getBoundingClientRect();
          if (allCtl && Math.max(b.width, b.height) >= 40 &&
              Math.min(prb.width, prb.height) >= 40) {
            hit = Math.max(hit, Math.min(Math.max(b.width, b.height),
                                         Math.min(prb.width, prb.height)));
          }
        }

        if (sm === null || hit < sm) { sm = hit; }
        if (hit < 40) {
          out.push({tag: el.tagName.toLowerCase(),
                    w: Math.round(b.width), h: Math.round(b.height),
                    text: (el.innerText || el.getAttribute('aria-label') || '')
                          .replace(/\\s+/g, ' ').trim().slice(0, 28)});
        }
      }
      window.__MRB_CTL__ = {n: n, sm: sm};
      return out;
    })(),
    fontStatus: (function () {
      var o = {};
      if (!document.fonts) { return o; }
      document.fonts.forEach(function (f) { o[f.status] = (o[f.status] || 0) + 1; });
      return o;
    })()
  }, function (k, v) {
    return v;
  }).replace('"controls":0', '"controls":' + (window.__MRB_CTL__ || {}).n)
    .replace('"smallest":null',
             '"smallest":' + JSON.stringify(
               (window.__MRB_CTL__ || {}).sm === null ||
               (window.__MRB_CTL__ || {}).sm === undefined
                 ? null : Math.round((window.__MRB_CTL__ || {}).sm)));
})()"""


def switch_props(page_name):
    """{tpl: [property, ...]} for one page, out of the MEASURED table.

    The parity probe reads these off both files and compares. Taken from
    `student_switches.json` rather than listed here, so the set this gate
    checks is the set the shim applies — one list, and no way for a switch to
    be applied and unchecked or checked and unapplied.
    """
    if not os.path.exists(SWITCHES):
        return {}
    table = json.load(open(SWITCHES, encoding="utf-8"))
    styles = (table.get(page_name) or {}).get("styles") or {}
    return {tpl: sorted(props) for tpl, props in styles.items()}


def grab(cdp, root, path, viewport, want_switches=None):
    server, port = cdp.serve(root)
    try:
        with cdp.Browser() as b:
            page = b.attach()
            page.set_viewport(*viewport)
            page.goto("http://127.0.0.1:%d/%s" % (port, path.replace(" ", "%20")))
            time.sleep(2.5)
            page.eval("window.__MRB_PARITY_SWITCHES__ = %s; 1"
                      % json.dumps(want_switches or {}))
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

        # ── C · clean at every band, asserted straight ─────────────────
        #
        # Both directions. Design's own file is measured too, because a page
        # that matches a broken reference is not a page that works, and
        # "Design's file overflows" is a finding about the delivery rather than
        # about the generator.
        for band in ASSERT_BANDS:
            vp = (band, 900)
            sw = switch_props(name)
            d_b = grab(cdp, REF, pair["design"], vp, sw)
            g_b = grab(cdp, SITE, pair["generated"], vp, sw)

            d_ok = (d_b["docScroll"] <= d_b["docClient"]
                    and d_b["overflowing"] == 0)
            rows.append((name, "C · Design is clean at %dpx" % band,
                         "PASS" if d_ok else "FAIL",
                         "scrollWidth %s = clientWidth, 0 overflowing"
                         % d_b["docScroll"] if d_ok else
                         "scrollWidth %s vs %s, %d element(s) overflowing"
                         % (d_b["docScroll"], d_b["docClient"],
                            d_b["overflowing"])))
            if not d_ok:
                problems.append(
                    "%s — DESIGN's own file is not clean at %dpx (scrollWidth "
                    "%s vs clientWidth %s, %d overflowing). That is a finding "
                    "about the delivery, not about the generator."
                    % (name, band, d_b["docScroll"], d_b["docClient"],
                       d_b["overflowing"]))

            g_ok = (g_b["docScroll"] <= g_b["docClient"]
                    and g_b["overflowing"] == 0)
            rows.append((name, "C · the generated page is clean at %dpx" % band,
                         "PASS" if g_ok else "FAIL",
                         "scrollWidth %s = clientWidth, 0 overflowing; band "
                         "%s, %s styled, %s text, %s hidden"
                         % (g_b["docScroll"], g_b.get("band"),
                            g_b.get("applied"), g_b.get("textSwaps"),
                            g_b.get("hidden")) if g_ok else
                         "scrollWidth %s vs %s, %d element(s) overflowing"
                         % (g_b["docScroll"], g_b["docClient"],
                            g_b["overflowing"])))
            if not g_ok:
                problems.append(
                    "%s — the generated page scrolls sideways at %dpx: "
                    "scrollWidth %s against clientWidth %s, %d element(s) "
                    "crossing the root's edges. 390px is the primary target "
                    "and this is the first thing that has to work."
                    % (name, band, g_b["docScroll"], g_b["docClient"],
                       g_b["overflowing"]))

            # The shim has to have RUN, and have aimed correctly. A page where
            # it silently did nothing is clean at 1460 and wrong everywhere
            # else, and "clean at 1460" is most of this gate's assertions.
            if int(g_b.get("mismatch") or 0):
                problems.append(
                    "%s — at %dpx the breakpoint shim reports %s switch row(s) "
                    "aimed at an element whose current value is not the "
                    "desktop value the table recorded. The table is pointed at "
                    "the wrong node and those rows were skipped rather than "
                    "written." % (name, band, g_b["mismatch"]))
                rows.append((name, "C · the shim aims true at %dpx" % band,
                             "FAIL", "%s mismatched row(s)" % g_b["mismatch"]))

            # ── C · the switch VALUES, against Design's own, per band ───
            #
            # Clean-and-not-overflowing is necessary and nowhere near
            # sufficient: a page with every grid collapsed to one column
            # overflows nothing and is not Design's design. This asserts the
            # value itself, element by element, against the same element in
            # Design's file at the same width.
            diffs = []
            for key, want in sorted((d_b.get("switches") or {}).items()):
                got = (g_b.get("switches") or {}).get(key)
                if got != want:
                    diffs.append("%s: Design %r, generated %r"
                                 % (key, want, got))
            sw_ok = not diffs
            rows.append((name, "C · %d switched value(s) match Design at %dpx"
                         % (len(d_b.get("switches") or {}), band),
                         "PASS" if sw_ok else "FAIL",
                         "every one" if sw_ok else "; ".join(diffs[:3])))
            if diffs:
                problems.append(
                    "%s — at %dpx %d switched declaration(s) do not match "
                    "Design's own file: %s"
                    % (name, band, len(diffs), "; ".join(diffs[:4])))

            # ── G · touch targets, ASSERTED AGAINST DESIGN'S OWN ───────
            #
            # ⚖️ TWO-SIDED, for the same reason layer C is. Design's §6 states
            # a 40px floor "everywhere, at every width", and Design's own file
            # does not meet it — measured, 11 controls at 390px and 6 at 1460.
            # The generated page has exactly the same 11 and the same 6, to the
            # pixel, because it is Design's DOM.
            #
            # A one-sided gate here would report those as a defect in the
            # generator, which is false and would invite somebody to "fix" it
            # by inventing sizes Design did not draw — the one thing the brief
            # forbids. So the assertion is: the generated page is NO WORSE than
            # the delivery, and the delivery's own shortfall is registered by
            # count so it cannot be quietly absorbed.
            d_small = {(s["tag"], s["text"]) for s in (d_b.get("smallTargets")
                                                       or [])}
            g_small = {(s["tag"], s["text"]) for s in (g_b.get("smallTargets")
                                                       or [])}
            worse = sorted(g_small - d_small)
            g_ok = not worse
            rows.append((name, "G · no control smaller than Design's at %dpx"
                         % band,
                         "PASS" if g_ok else "FAIL",
                         "%d control(s) measured; %d under %dpx in BOTH files, "
                         "0 that Design does not also have"
                         % (g_b.get("controls", 0), len(g_small), TOUCH_FLOOR)
                         if g_ok else
                         "%d control(s) under %dpx here and not in Design's "
                         "file: %s" % (len(worse), TOUCH_FLOOR, worse[:3])))
            if worse:
                problems.append(
                    "%s — at %dpx %d control(s) are under the %dpx touch floor "
                    "HERE AND NOT in Design's own file: %s. That is a "
                    "regression in the generator, not a property of the "
                    "delivery. (%s)"
                    % (name, band, len(worse), TOUCH_FLOOR, worse[:4],
                       TOUCH_EXEMPT_NOTE))

            want_d = DELIVERY_TOUCH_SHORTFALL.get(name, {}).get(band)
            if want_d is None:
                problems.append(
                    "%s at %dpx has no entry in DELIVERY_TOUCH_SHORTFALL. A "
                    "band this gate does not know the delivery's own shortfall "
                    "at is a band where a real regression would hide inside "
                    "it." % (name, band))
                rows.append((name, "G · the delivery's shortfall is registered "
                             "at %dpx" % band, "FAIL", "absent"))
            elif len(d_small) == want_d:
                rows.append((name, "G · Design's own %dpx shortfall is still "
                             "%d control(s)" % (band, want_d), "PASS",
                             "the delivery meets its own %dpx floor here"
                             % TOUCH_FLOOR if not want_d else
                             "Design's §6 asks for a %dpx floor everywhere and "
                             "the delivery does not meet it in %d place(s) "
                             "here; recorded, not approximated"
                             % (TOUCH_FLOOR, want_d)))
            else:
                problems.append(
                    "%s — DESIGN's own file has %d control(s) under %dpx at "
                    "%dpx and this gate registers %d. The delivery moved. Read "
                    "the diff and update DELIVERY_TOUCH_SHORTFALL "
                    "deliberately." % (name, len(d_small), TOUCH_FLOOR, band,
                                       want_d))
                rows.append((name, "G · Design's own %dpx shortfall holds"
                             % band, "FAIL",
                             "%d measured against %d registered"
                             % (len(d_small), want_d)))

        # ── C · the UNCREATABLE half of the presence gap, by count ─────
        #
        # ASSERTED, in the shape the 390px gap was. Design renders nodes below
        # desktop that a desktop snapshot does not contain; they cannot be
        # conjured and they are not approximated. If the number moves, Design's
        # delivery moved or the extraction did.
        phone = grab(cdp, SITE, pair["generated"], (390, 900))
        want = UNCREATABLE.get(name)
        got = int(phone.get("absent") or 0)
        if want is None:
            problems.append("%s has no entry in UNCREATABLE" % name)
            rows.append((name, "C · the uncreatable gap is registered",
                         "FAIL", "absent"))
        elif got == want:
            rows.append((name, "C · the KNOWN uncreatable gap is exactly %d "
                         "node(s)" % want, "PASS",
                         "Design renders these below desktop and a desktop "
                         "snapshot has no DOM for them; they close when the "
                         "behaviour is ported"))
        else:
            problems.append(
                "%s — the uncreatable presence gap is %d node(s) at 390px and "
                "UNCREATABLE registers %d. Either Design's delivery changed or "
                "student_switches.py extracted differently. Re-run "
                "`python3 student_switches.py`, read the diff, and update the "
                "number deliberately." % (name, got, want))
            rows.append((name, "C · the KNOWN uncreatable gap holds", "FAIL",
                         "%d measured against %d registered" % (got, want)))

    rows_d, problems_d = run_token_contract(cdp)
    rows.extend(rows_d)
    problems.extend(problems_d)

    for fn in (run_no_literal_count, run_no_fabricated_split,
               run_feedback_strings):
        r, pr = fn()
        rows.extend(r)
        problems.extend(pr)

    return rows, problems


# ── H · the four feedback strings Design's design rests on ────────────────
#
# ⚑ FOUND IN PHASE 4, AND IT IS THE LARGEST OPEN ITEM ON EITHER PAGE.
#
# Design's assignment note, §15 "Do not ship", item 1: *"The API needs to serve
# rungs 1–2 from the class's scheme of work with the per-distractor feedback
# strings — four per question, one per option, no generic fallbacks. A question
# without all four is not shippable: the whole design rests on them."*
#
# And §2 says what the fourth one is FOR: *"Every wrong option has its own
# line… The right answer's line is shown too, so the pair reads why not that /
# why this."*
#
# MEASURED ACROSS THE WHOLE CORPUS, both places a question can come from:
#
#     lesson ladder, recall + apply    140 rungs, every one 4 options and
#                                      exactly 3 feedback strings
#     ks3_data question bank           840 questions, every one 4 options and
#                                      exactly 3 `why` strings
#
# In all 980, the three are the DISTRACTORS and the missing one is the CORRECT
# option. So "why not that" is authored everywhere and "why this" is authored
# nowhere. It is not a gap in coverage — it is a field that was never part of
# the authoring shape.
#
# ⚖️ NOT FILLABLE FROM HERE. A generated "why this" line is exactly the generic
# fallback Design rules out, and it is science prose on a student page, which
# is Mide's gate and nobody else's. So this REGISTERS the number and asserts it
# both ways: it goes red if the shortfall grows, and it goes red when somebody
# authors them, at which point this block is deleted rather than edited.
FEEDBACK_SHORTFALL = {
    "lesson ladder rungs (recall + apply)": 140,
    "question bank": 840,
}


def _ladder_feedback_gap():
    """Recall/apply rungs whose CORRECT option has no feedback line."""
    import importlib
    import pkgutil
    import ks3_data
    root = os.path.dirname(ks3_data.__file__)
    units = sorted(d for d in os.listdir(root)
                   if os.path.isdir(os.path.join(root, d))
                   and not d.startswith("_"))
    total = missing = 0
    for unit in units:
        here = os.path.join(root, unit)
        for mod in sorted(m.name for m in pkgutil.iter_modules([here])):
            if not mod.startswith("lesson_"):
                continue
            m = importlib.import_module("ks3_data.%s.%s" % (unit, mod))
            lesson = getattr(m, "LESSON", None)
            if not isinstance(lesson, dict):
                continue
            ladder = lesson.get("ladder") or {}
            for rung in ("recall", "apply"):
                r = ladder.get(rung)
                if not isinstance(r, dict) or "options" not in r:
                    continue
                total += 1
                fb = r.get("feedback") or {}
                ans = r.get("answer")
                if not str(fb.get(ans) or "").strip():
                    missing += 1
    return total, missing


def _bank_feedback_gap():
    """Bank questions whose CORRECT option has no `why`."""
    from ks3_data import question_bank as qb
    total = missing = 0
    for rec in qb.load_bank():
        for q in rec["questions"]:
            total += 1
            for opt in q.get("options") or []:
                if opt.get("correct") and not str(opt.get("why") or "").strip():
                    missing += 1
                    break
    return total, missing


def run_feedback_strings():
    rows, problems = [], []
    measured = {}

    lad_total, lad_missing = _ladder_feedback_gap()
    measured["lesson ladder rungs (recall + apply)"] = lad_missing
    rows.append(("feedback strings",
                 "H · lesson ladder: %d of %d recall/apply rung(s) carry the "
                 "right answer's line" % (lad_total - lad_missing, lad_total),
                 "PASS" if lad_missing == FEEDBACK_SHORTFALL[
                     "lesson ladder rungs (recall + apply)"] else "FAIL",
                 "%d still missing it" % lad_missing))

    bank_total, bank_missing = _bank_feedback_gap()
    measured["question bank"] = bank_missing
    rows.append(("feedback strings",
                 "H · question bank: %d of %d question(s) carry the right "
                 "answer's line" % (bank_total - bank_missing, bank_total),
                 "PASS" if bank_missing == FEEDBACK_SHORTFALL["question bank"]
                 else "FAIL",
                 "%d still missing it" % bank_missing))

    for label, want in sorted(FEEDBACK_SHORTFALL.items()):
        got = measured.get(label)
        if got == want:
            continue
        if got is not None and got < want:
            problems.append(
                "H — %s: the missing-feedback count has FALLEN from %d to %d. "
                "That is somebody authoring them, which is the point. Update "
                "FEEDBACK_SHORTFALL, and when it reaches zero delete this "
                "layer rather than setting it to 0 — a gate that asserts "
                "nothing is missing is a gate with nothing to say."
                % (label, want, got))
        else:
            problems.append(
                "H — %s: %d question(s) lack the right answer's feedback line "
                "and %d were registered. Design: 'A question without all four "
                "is not shippable: the whole design rests on them.'"
                % (label, got, want))

    rows.append(("feedback strings",
                 "H · the registered shortfall is exactly where it was",
                 "PASS" if not problems else "FAIL",
                 "%d rung(s) + %d bank question(s) still need the "
                 "'why this' line — Mide's gate, it is science prose"
                 % (lad_missing, bank_missing) if not problems
                 else "the count moved"))
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


def _emitted_only(path, text):
    """`text` with comments and docstrings removed.

    ⚠️ THIS EXISTS BECAUSE THE GATE FIRED ON ITS OWN EXPLANATION. Phase 2 added
    a paragraph to `build_student.py` describing the breadcrumb note — "reads
    `AUTUMN TERM · WEEK 04 / 12` at desktop" — and layer E dutifully reported a
    literal question count. It is not one; it is prose about one, in a
    docstring, and a docstring cannot reach a student.

    The distinction the rule actually draws is between what a file SAYS and
    what it EMITS, so that is the distinction this draws. Python is tokenised
    rather than regexed — a `#` inside a string literal is not a comment and a
    regex would take it for one, which would silently blind the scan to
    anything after it on that line.
    """
    if path.endswith(".py"):
        import io
        import tokenize
        out, prev_type = [], None
        try:
            toks = list(tokenize.generate_tokens(io.StringIO(text).readline))
        except (tokenize.TokenError, IndentationError):
            return text                      # unparseable — scan it whole
        for tok in toks:
            if tok.type == tokenize.COMMENT:
                continue
            if (tok.type == tokenize.STRING and prev_type in
                    (tokenize.INDENT, tokenize.NEWLINE, tokenize.NL, None)):
                continue                     # a docstring, not a value
            out.append(tok.string)
            if tok.type not in (tokenize.NL, tokenize.NEWLINE):
                prev_type = tok.type
            else:
                prev_type = tok.type
        return "\n".join(out)
    if path.endswith(".js"):
        import re
        # Block and line comments. A `//` inside a string is possible (a URL),
        # so only strip a line comment that starts a line or follows whitespace
        # and is not preceded by a quote on that line.
        text = re.sub(r"/\*.*?\*/", "", text, flags=re.S)
        keep = []
        for line in text.split("\n"):
            i = line.find("//")
            if i > -1 and line.count('"', 0, i) % 2 == 0 \
                      and line.count("'", 0, i) % 2 == 0:
                line = line[:i]
            keep.append(line)
        return "\n".join(keep)
    return text


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
        hits = _scan_counts(
            _emitted_only(rel, open(rel, encoding="utf-8").read()))
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
        for got in _scan_split(
                _emitted_only(rel, open(rel, encoding="utf-8").read())):
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
          "every registered section is present; BOTH ARE CLEAN AT 360, 390, "
          "820 AND 1460 with every switched value matching Design's own file "
          "at each; no control is smaller than Design's; the uncreatable "
          "presence gap is exactly where the measurement put it; "
          "`--st-ok-room` is graphic-only and the sweep proved it can see; and "
          "no built source carries a literal question count or Design's drawn "
          "leaderboard split.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
