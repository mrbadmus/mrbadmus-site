#!/usr/bin/env python3
"""teacher_behaviour.py — the ported teacher pages, driven.

    python3 teacher_behaviour.py                # all twelve fixtures
    python3 teacher_behaviour.py classes        # one page (substring match)
    python3 teacher_behaviour.py --shots DIR    # also write screenshots

⊕ MRB-287, 24 Aug 2026.

── WHY THIS EXISTS ──────────────────────────────────────────────────────

`teacher_tells.py` reads the built pages' BYTES. It can prove that Design's
invented school is not in the file; it cannot prove that anything renders,
that a button does something, or that an empty class produces an empty state
rather than a stack trace. Every check it makes would pass on a page that is
blank.

This is the gate that opens the pages. It is the teacher-side twin of
`ks3_instrument_liveness` — "the only gate that PRESSES THE BUTTONS" — and it
exists for the reason that file gives: every other gate measures the page at
rest, so a dead control passes all of them and does nothing when a teacher
touches it.

── WHAT IT DRIVES, AND WHY NOT THE LIVE PAGES ───────────────────────────

The twelve fixtures: six screens x {populated, empty}.

⚠️ IT DOES NOT DRIVE THE LIVE PAGES, and that is a real limit rather than an
oversight. A live teacher page begins with `requireTeacherRole`, so reaching
one needs a teacher account and a password. This run had neither
(`MRB_DRIVE_PASSWORD` unset), and a gate that signs in to production is a gate
that fails when Render is asleep — which is why `student_page_drive.py` and
`student_controls_drive.py` are both EXCLUDED from the registry for exactly
this reason.

What the fixtures CAN prove is everything between the data arriving and the
pixels: that every screen mounts, that every binding resolves, that every
control does something, and that the empty shapes render as states rather
than as errors. What they cannot prove is that the SEAM returns the right
rows. That is `teacher_tells` (nothing invented reaches the page) plus review,
and it is stated here rather than implied.

── THE EMPTY HALF ───────────────────────────────────────────────────────

Half the fixtures are empty on purpose, because empty states are the half of
the product that ships broken. A populated fixture exercises the path where
every array has something in it; it is the other path that throws on
`rows[0]`, divides by `length`, and renders `null%`.

The five shapes, from the port's own emission:

    no classes at all · a class with no roster · a class with students but
    no work set · a paper with nobody's submission · a grid whose paper was
    not prefetched

── THE RELOAD ───────────────────────────────────────────────────────────

Every page is driven, RELOADED, and driven again. This is not padding: a
reload is where the runtime's field-value preservation, the `?v=` stamps and
any state written at mount get a second chance to disagree with each other,
and MRB-287's own brief records that three of the worst defects of the month
surfaced on the second pass rather than the first.
"""

import json
import os
import re
import sys

REPO = os.path.dirname(os.path.abspath(__file__))
PAGE_DIR = "teacher"

# ⛔ NO `import`: it is not ported, so there is no `import-fixture.html` to
# drive. `teacher/import.html` is the hand-written wizard again — see
# IMPORT_NOT_PORTED in teacher_rulings.py. It is not covered by any gate here,
# which is exactly where it was before the port and is stated rather than
# implied.
SCREENS = ["classes", "class-detail", "student-detail", "assignment",
           "digest", "insights"]

# Every fixture, and what it is supposed to be showing. The empty ones name
# their shape so a failure says which state broke rather than just "empty".
EMPTY_SHAPE = {
    "classes": "a teacher with no classes at all",
    "class-detail": "a class with no roster, and one with no work set",
    "student-detail": "a student with no submissions",
    "assignment": "a paper nobody has submitted",
    "digest": "no live classes to digest",
    "insights": "nothing marked to chart",
}


def fixtures():
    out = []
    for s in SCREENS:
        out.append((s, "%s-fixture.html" % s, False))
        out.append((s, "%s-empty-fixture.html" % s, True))
    return out


# ── the probe ────────────────────────────────────────────────────────────
#
# One evaluation per page rather than a round trip per control: the DOM is
# rebuilt wholesale on every `setState`, so a Python-side loop holding element
# handles would be holding handles to elements that no longer exist. The press
# and the before/after comparison have to happen inside one script.
#
# "Something changed" is measured as the host's own serialised text plus its
# render counter. A control that renders the same text twice has still done
# something if the counter moved (a no-op re-render is legal — Design has
# toggles that land on the state they were already in), but a control that
# moves NEITHER is dead.
_DRIVE_JS = r"""
(async function () {
  var host = document.querySelector('#mrb-teacher');
  if (!host) { return JSON.stringify({error: 'no #mrb-teacher host'}); }

  /* ⚠️ THE REDRAW IS ON A FRAME, NOT ON THE CLICK. `setState` calls the
     runtime's `schedule`, which defers the rebuild to `requestAnimationFrame`.
     The first version of this probe snapshotted synchronously after `.click()`
     and therefore read the DOM as it was BEFORE the control acted — so it
     reported all 29 controls on the classes screen as dead, including the
     filter tabs and the nav. Two frames, because the callback queue is
     drained on the frame after the one that draws. */
  function frame() {
    return new Promise(function (r) {
      requestAnimationFrame(function () { requestAnimationFrame(r); });
    });
  }

  /* Navigation is recorded, not followed. Six of Design's handlers now set
     `window.location.href` through `MRB_GO`, and letting one fire would tear
     down the page mid-sweep and take the remaining controls with it. Stubbing
     the helper keeps the press REAL — the handler still runs, still computes
     its destination, and still proves it is wired — while the browser stays
     put. A press that reaches MRB_GO is alive by definition. */
  var navs = [];
  var realGo = window.MRB_GO, realBack = window.MRB_BACK;
  window.MRB_GO = function (screen, params) {
    navs.push({screen: screen, params: params || null});
  };
  window.MRB_BACK = function () { navs.push({screen: '<back>', params: null}); };

  function snap() {
    return {
      text: host.innerText || '',
      renders: host.getAttribute('data-mrb-renders'),
      misses: host.getAttribute('data-mrb-misses'),
      nodes: host.querySelectorAll('*').length
    };
  }

  var first = snap();

  var all = host.querySelectorAll('[data-dc-tpl]');
  var controls = [];
  for (var i = 0; i < all.length; i++) {
    var el = all[i];
    var tag = el.tagName.toLowerCase();
    var clickable = tag === 'button' || tag === 'a' || tag === 'select' ||
                    tag === 'input' || tag === 'textarea' ||
                    el.getAttribute('role') === 'button' ||
                    (el.style && el.style.cursor === 'pointer');
    if (clickable) { controls.push(el); }
  }

  var dead = [], pressed = 0, errors = [];
  for (var j = 0; j < controls.length; j++) {
    var c = controls[j];
    if (!host.contains(c)) { continue; }  // an earlier press rebuilt it away

    var label = (c.innerText || c.getAttribute('aria-label') ||
                 c.getAttribute('placeholder') || c.tagName)
                .slice(0, 40).replace(/\s+/g, ' ').trim();
    var idx = c.getAttribute('data-dc-tpl');
    var before = snap();
    var navsBefore = navs.length;
    try {
      var tg = c.tagName.toLowerCase();
      if (tg === 'input' || tg === 'textarea') {
        c.focus();
        c.value = 'zz';
        c.dispatchEvent(new Event('input', {bubbles: true}));
      } else if (tg === 'select') {
        c.focus();
        if (c.options && c.options.length > 1) { c.selectedIndex = 1; }
        c.dispatchEvent(new Event('change', {bubbles: true}));
      } else {
        c.click();
      }
      pressed++;
    } catch (e) {
      errors.push(idx + ' ' + label + ': ' + e.message);
      continue;
    }
    await frame();
    var after = snap();
    var moved = after.text !== before.text ||
                after.renders !== before.renders ||
                after.nodes !== before.nodes ||
                navs.length > navsBefore;
    if (!moved) {
      dead.push({i: idx, label: label, tag: c.tagName.toLowerCase()});
    }
  }

  window.MRB_GO = realGo;
  window.MRB_BACK = realBack;

  return JSON.stringify({
    error: '',
    first: first,
    last: snap(),
    controls: controls.length,
    pressed: pressed,
    navs: navs.length,
    dead: dead,
    errors: errors
  });
})()
"""

# Strings that must never be on a rendered teacher page. These are RENDER-time
# failures the byte-level gate cannot see, because each one is produced by
# arithmetic rather than written in the source.
#
# ⚠️ `null%` AND `NaN` ARE THE POINT. The seam returns `null` for a percentage
# with nothing markable behind it — deliberately, so that "nothing to measure"
# cannot be confused with "zero". `null + '%'` renders the four characters
# `null%`, and a teacher reads that as a broken page; `0%` would be worse
# still, because they would read it as a fact.
RENDER_TELLS = ["null%", "NaN", "undefined", "-Infinity", "Infinity",
                "[object Object]", "null/", "/null", "null students"]


def drive(page, path, is_empty, cdp, port, shots=None):
    """Problems, as strings, for one fixture. Driven twice — load and reload."""
    problems = []
    with cdp.Browser() as b:
        pg = b.attach()
        pg.set_viewport(1460, 1200)
        url = "http://127.0.0.1:%d/%s/%s" % (port, PAGE_DIR, path)

        for pass_n, what in ((1, "load"), (2, "reload")):
            if pass_n == 1:
                pg.goto(url, settle=1.2)
            else:
                pg.eval("location.reload()")
                import time
                time.sleep(1.6)

            # ⚠️ THE SHOT IS TAKEN AT REST, BEFORE THE SWEEP. The first
            # version photographed after driving, which meant every review
            # screenshot showed the page in whatever state the LAST control
            # left it — the classes screen came out with the student-search
            # overlay open across the middle of it. A human reviewing these is
            # asking "what does a teacher see when they arrive", and that is
            # the frame before any button is pressed.
            if shots and pass_n == 1:
                out = os.path.join(shots, "%s%s.png"
                                   % (page, "-empty" if is_empty else ""))
                pg.screenshot(out, full_page=True)

            got = json.loads(pg.eval(_DRIVE_JS))
            if got.get("error"):
                problems.append("%s: %s" % (what, got["error"]))
                continue

            first, last = got["first"], got["last"]

            # 1. It mounted.
            if not first["renders"] or int(first["renders"]) < 1:
                problems.append(
                    "%s: never rendered — the host carries no "
                    "data-mrb-renders. The page is blank." % what)
                continue

            # 2. Every binding resolved. A miss is a `{{ }}` the runtime could
            #    not look up, which renders as nothing at all — invisible in a
            #    screenshot, because what is missing does not draw.
            if first["misses"] and int(first["misses"]) > 0:
                problems.append(
                    "%s: %s unresolved binding(s) at mount. A miss renders as "
                    "nothing, so this is invisible on screen."
                    % (what, first["misses"]))

            # 3. Something is actually on the page. An empty fixture is
            #    allowed to be sparse; it is not allowed to be blank, because
            #    a blank page is indistinguishable from a crash.
            text = (first["text"] or "").strip()
            if len(text) < 40:
                problems.append(
                    "%s: rendered only %d character(s) of text. An empty "
                    "state is a STATE — it has to say something. This is a "
                    "blank page, which reads as a crash." % (what, len(text)))

            # 4. No arithmetic leaked into the copy.
            for tell in RENDER_TELLS:
                if tell in text:
                    problems.append(
                        "%s: rendered %r. That is a computed value reaching "
                        "the screen, not a written one — the branch that "
                        "produces it has no guard." % (what, tell))

            # 5. No dead controls.
            for d in got["dead"]:
                problems.append(
                    "%s: control %s (%s %r) changed nothing — no text, no "
                    "node count, no re-render. Nothing that looks pressable "
                    "may do nothing."
                    % (what, d["i"], d["tag"], d["label"]))

            # 6. Nothing threw while being pressed.
            for e in got["errors"]:
                problems.append("%s: pressing %s threw" % (what, e))

            # 7. And the console stayed quiet. A page can render correctly and
            #    still be throwing on every state change — the throw happens
            #    after the draw, which is the shape of bug that survives a
            #    screenshot.
            for line in pg.console_errors():
                if "favicon" in line:
                    continue
                problems.append("%s: console error — %s" % (what, line[:200]))

    return problems


def main(argv):
    os.chdir(REPO)
    shots = None
    if "--shots" in argv:
        shots = argv[argv.index("--shots") + 1]
        os.makedirs(shots, exist_ok=True)
        argv = [a for a in argv if a != "--shots" and a != shots]
    only = [a for a in argv if not a.startswith("-")]

    sys.path.insert(0, REPO)
    import ks3_browser as cdp

    todo = [f for f in fixtures()
            if not only or any(o in f[1] for o in only)]
    missing = [f[1] for f in todo
               if not os.path.exists(os.path.join(PAGE_DIR, f[1]))]
    if missing:
        print("\nteacher_behaviour.py: not built — %s\n"
              "  Run `python3 build_teacher_port.py` first."
              % ", ".join(missing))
        return 1

    print("\n🖐  teacher_behaviour — the ported teacher pages, driven and "
          "pressed\n")
    print("     %d fixture(s): %d screen(s) x {populated, empty}, each driven "
          "on load\n             AND after a reload\n"
          % (len(todo), len(SCREENS)))

    server, port = cdp.serve(REPO)
    failed = 0
    try:
        for page, path, is_empty in todo:
            problems = drive(page, path, is_empty, cdp, port, shots)
            tag = "empty" if is_empty else "full "
            if problems:
                failed += 1
                print("     %-16s %s ❌ %d problem(s)"
                      % (page, tag, len(problems)))
                if is_empty:
                    print("        (%s)" % EMPTY_SHAPE.get(page, ""))
                for p in problems[:10]:
                    print("        · %s" % p)
                if len(problems) > 10:
                    print("        · … and %d more" % (len(problems) - 10))
            else:
                print("     %-16s %s ✅" % (page, tag))
    finally:
        server.shutdown()

    print()
    if failed:
        print("  FAIL  %d of %d fixture(s).\n" % (failed, len(todo)))
        return 1
    print("  PASS  %d fixture(s) mounted, every binding resolved, every "
          "control moved\n        something, no computed value reached the "
          "copy, and the console stayed\n        quiet — on load and again "
          "after a reload.\n" % len(todo))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
