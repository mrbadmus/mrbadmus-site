#!/usr/bin/env python3
"""focus_audit.py — keyboard focus VISIBILITY audit.

    python3 focus_audit.py                  # every registered page
    python3 focus_audit.py student teacher   # only pages whose key contains a token
    python3 focus_audit.py --shots DIR       # also saves a handful of named
                                              # screenshots into DIR (1280 + 390)

Defect this exists to catch (found on production, 24 Sep 2026): a keyboard
user can Tab to a control on the student class page and see NOTHING change —
no outline, no box-shadow, no background, no border — because most controls
on the ported student/teacher pages are `<button style="all:unset;...">`
(Design's compiled markup keeps `all:unset` byte-identical, see
`build_student_port.py`'s module docstring) and an inline style beats any
stylesheet selector regardless of specificity, `:focus-visible` included.

── METHOD ──────────────────────────────────────────────────────────────

For every target page:

  1. Load it, let it settle, and — for anything with a SPA mount id — poll
     until the mount has actually rendered (`wait_for_mount`).
  2. In the browser, tag every element that is a plausible Tab stop (the
     same selector `shared/set-work.js`'s own focus trap uses, PLUS
     `[role="button"]`/`[role="tab"]`/`[role="menuitem"]`/`[contenteditable]`)
     with a `data-mrb-fa` index, and record its BASELINE computed style
     (outline, box-shadow, background-color, border) while nothing has
     been focused yet.
  3. Press a REAL Tab key, N times, through `Input.dispatchKeyEvent`
     (`rawKeyDown` + `keyUp` — Tab has no `char` event). A JS-dispatched
     `KeyboardEvent` would not move focus at all (untrusted events run no
     default action), so this has to be a genuine input-layer press, the
     same reasoning `set_work_drive.py`'s `press_space` uses for Space.
  4. After every press, read `document.activeElement`'s `data-mrb-fa`
     index and its CURRENT computed style. Compare against the baseline
     for that same index. Any of outline/box-shadow/background/border
     differing counts as a visible change; all four unchanged is the
     defect this reports.
  5. Also record which tagged indices were never reached by Tab at all
     (an order/trap problem, not a visibility one) and separately scan for
     elements that look interactive (`onclick`, `cursor:pointer`) but
     carry no `tabindex` and aren't naturally focusable — a keyboard user
     cannot reach these AT ALL, regardless of ring.

A "composer"/overlay page (the Set work sheet) is opened first via its own
public JS seam (`MRB_SET_WORK_OPEN('')`, the same function the page's own
"Set work" buttons call) so the audit measures the sheet's real controls,
not the page behind it.

Exit code is 1 if any page has an unreached-by-order problem or a
no-visible-change control; 0 otherwise. `--shots` never affects the exit
code — it is a reporting side effect for the run's screenshots.
"""

import json
import os
import sys
import time

REPO = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, REPO)
import ks3_browser as cdp  # noqa: E402

MAX_TABS = 200  # a generous cap; the busiest fixture here has ~80 stops


# ── the tagging + baseline-capture script ──────────────────────────────
#
# ⚠️ ONE SELECTOR, deliberately the same shape `shared/set-work.js`'s own
# `FOCUSABLE` constant uses (`button,[href],input,select,textarea,
# [tabindex]`), widened with the ARIA-role and contenteditable cases a
# custom control can carry instead of a native tag. Anything hidden,
# zero-sized, or `disabled`/`tabindex="-1"` is excluded — Tab could never
# reach it either.
TAG_AND_BASELINE_JS = r"""
(function () {
  var sel = 'button,[href],input,select,textarea,[tabindex],' +
            '[role="button"],[role="tab"],[role="menuitem"],' +
            '[role="link"],[contenteditable="true"]';
  var scope = %(scope)s;
  var root = scope ? document.querySelector(scope) : document;
  if (!root) { return JSON.stringify({error: 'scope not found: ' + scope}); }
  var nodes = Array.prototype.slice.call(root.querySelectorAll(sel));
  var out = [];
  function styleOf(el) {
    var cs = getComputedStyle(el);
    return {
      outline: [cs.outlineWidth, cs.outlineStyle, cs.outlineColor].join(' '),
      boxShadow: cs.boxShadow,
      background: cs.backgroundColor,
      border: [cs.borderTopWidth, cs.borderTopStyle,
               cs.borderTopColor].join(' '),
      color: cs.color,
      textDecoration: cs.textDecorationLine
    };
  }
  var idx = 0;
  nodes.forEach(function (el) {
    var r = el.getBoundingClientRect();
    if (!r.width || !r.height) { return; }
    var cs = getComputedStyle(el);
    if (cs.visibility === 'hidden' || cs.display === 'none') { return; }
    if (el.disabled) { return; }
    var ti = el.getAttribute('tabindex');
    if (ti !== null && parseInt(ti, 10) < 0) { return; }
    el.setAttribute('data-mrb-fa', String(idx));
    var label = (el.innerText || el.getAttribute('aria-label') ||
                 el.getAttribute('title') || el.getAttribute('placeholder') ||
                 '').trim().replace(/\s+/g, ' ').slice(0, 60);
    out.push({
      i: idx, tag: el.tagName.toLowerCase(),
      cls: (el.getAttribute('class') || '').slice(0, 60),
      label: label || '(no label)',
      style: styleOf(el)
    });
    idx += 1;
  });
  /* Reachability check: things that LOOK clickable but are not in `sel`
     at all — no native focusability, no tabindex, no button/link role. */
  var suspects = [];
  var all = root.querySelectorAll('*');
  for (var j = 0; j < all.length && suspects.length < 200; j++) {
    var e = all[j];
    if (e.closest(sel)) { continue; }  // it or an ancestor is already a
                                        // real Tab stop — a decorative
                                        // icon/label inside a button is
                                        // not a separate defect
    var hasClick = !!e.getAttribute('onclick');
    var cur = getComputedStyle(e).cursor === 'pointer';
    if (!hasClick && !cur) { continue; }
    var rr = e.getBoundingClientRect();
    if (!rr.width || !rr.height) { continue; }
    // Only the OUTERMOST clickable-looking element counts. A `cursor:
    // pointer` card commonly wraps a name, an avatar and a stat line, each
    // of which also computes `pointer` by inheritance — reporting all of
    // them for one real click target is noise, not N defects.
    var dup = false, anc = e.parentElement;
    while (anc && anc !== root.parentElement) {
      if (getComputedStyle(anc).cursor === 'pointer' ||
          anc.getAttribute('onclick')) { dup = true; break; }
      anc = anc.parentElement;
    }
    if (dup) { continue; }
    suspects.push({
      tag: e.tagName.toLowerCase(),
      cls: (e.getAttribute('class') || '').slice(0, 60),
      label: (e.innerText || '').trim().replace(/\s+/g, ' ').slice(0, 40)
    });
  }
  return JSON.stringify({count: out.length, baseline: out,
                          unreachable_candidates: suspects});
})()
"""

READ_ACTIVE_JS = r"""
(function () {
  var el = document.activeElement;
  if (!el || el === document.body) { return JSON.stringify({i: -1}); }
  var idxAttr = el.getAttribute('data-mrb-fa');
  var cs = getComputedStyle(el);
  return JSON.stringify({
    i: idxAttr === null ? null : parseInt(idxAttr, 10),
    tag: el.tagName.toLowerCase(),
    style: {
      outline: [cs.outlineWidth, cs.outlineStyle, cs.outlineColor].join(' '),
      boxShadow: cs.boxShadow,
      background: cs.backgroundColor,
      border: [cs.borderTopWidth, cs.borderTopStyle,
               cs.borderTopColor].join(' '),
      color: cs.color,
      textDecoration: cs.textDecorationLine
    }
  });
})()
"""


def press_tab(p, shift=False):
    """A REAL Tab key through CDP — see press_space() in set_work_drive.py
    for why a JS-dispatched KeyboardEvent cannot stand in for this: an
    untrusted event runs no default action, so focus would never move."""
    mods = 8 if shift else 0  # CDP modifier bit: Shift = 8
    common = {"key": "Tab", "code": "Tab", "windowsVirtualKeyCode": 9,
              "nativeVirtualKeyCode": 9, "modifiers": mods}
    p.send("Input.dispatchKeyEvent", dict(common, type="rawKeyDown"))
    p.send("Input.dispatchKeyEvent", dict(common, type="keyUp"))
    time.sleep(0.06)


def styles_differ(a, b):
    for k in ("outline", "boxShadow", "background", "border", "color",
              "textDecoration"):
        if a.get(k) != b.get(k):
            return True
    return False


def wait_for_mount(page, mount_id, seconds=40.0, poll=0.25):
    """Poll until an SPA mount has actually rendered children. Same shape as
    student_controls_drive.wait_for_mount; duplicated rather than imported
    because that module drives a different fixture set with its own CLI."""
    end, last = time.time() + seconds, 0
    expr = ("(function(){var h=document.getElementById(%r);"
            "return h?h.getElementsByTagName('*').length:-1;})()" % mount_id)
    while time.time() < end:
        n = page.eval(expr)
        n = n if isinstance(n, int) else 0
        if n > 20 and n == last:
            return n
        last = n
        time.sleep(poll)
    return last


# ── the page list ───────────────────────────────────────────────────────
#
# `pre_js`, when given, is evaluated once after the page (and its mount, if
# any) has settled, and BEFORE tagging/baseline capture — this is how the
# Set work sheet gets opened before it is measured.

PAGES = [
    dict(key="student_class", url="/student/class-fixture.html",
         mount="mrb-student"),
    dict(key="student_assignment", url="/student/assignment-fixture.html",
         mount="mrb-student"),

    dict(key="teacher_classes", url="/teacher_fixtures/classes-fixture.html",
         mount="mrb-teacher"),
    dict(key="teacher_class_detail",
         url="/teacher_fixtures/class-detail-fixture.html",
         mount="mrb-teacher"),
    dict(key="teacher_student_detail",
         url="/teacher_fixtures/student-detail-fixture.html",
         mount="mrb-teacher"),
    dict(key="teacher_assignment",
         url="/teacher_fixtures/assignment-fixture.html",
         mount="mrb-teacher"),
    dict(key="teacher_digest", url="/teacher_fixtures/digest-fixture.html",
         mount="mrb-teacher"),
    dict(key="teacher_insights",
         url="/teacher_fixtures/insights-fixture.html",
         mount="mrb-teacher"),

    # The Set work sheet: same fixture, opened via its own public seam.
    # `MRB_SET_WORK_OPEN` is the function the page's own "Set work" buttons
    # call (see teacher_fixtures/class-detail-fixture.html) — an empty
    # classId is a real, ruled state (MRB-335: the sheet opens with no
    # class preselected) rather than a synthetic shortcut.
    dict(key="set_work_sheet", url="/teacher_fixtures/class-detail-fixture.html",
         mount="mrb-teacher", pre_js="MRB_SET_WORK_OPEN('');",
         wait_js="!!(document.querySelector('.sw-overlay') && "
                 "document.querySelector('.sw-overlay').offsetParent)",
         scope=".sw-overlay"),

    # Hand-written teacher pages.
    dict(key="teacher_today", url="/teacher/today.html"),
    dict(key="teacher_timetable", url="/teacher/timetable.html"),
    dict(key="teacher_admin", url="/teacher/admin.html"),
    dict(key="teacher_import", url="/teacher/import.html"),

    # Root / public pages.
    dict(key="root_auth", url="/auth.html"),
    dict(key="root_leaderboard", url="/leaderboard.html"),
    dict(key="root_index", url="/index.html"),

    # One representative KS3 lesson page (built output).
    dict(key="ks3_lesson",
         url="/mrbadmus_site/ks3/chemistry/the-periodic-table/mendeleev.html"),
]


def wait_js_condition(page, expr, seconds=10.0, poll=0.15):
    end = time.time() + seconds
    while time.time() < end:
        if page.eval(expr):
            return True
        time.sleep(poll)
    return False


def capture_stable_baseline(p, scope_json, tries=8, wait=0.4):
    """Tag + capture the baseline, but only once the tree has stopped being
    torn down and redrawn out from under us.

    ⚠️ THIS IS NOT PARANOIA. `shared/student-runtime.js`'s `draw()` empties
    the whole mount host and rebuilds it from scratch on every `setState` —
    the class/assignment pages fire an async data read right after first
    paint and redraw once it resolves, which silently strips every
    `data-mrb-fa` tag this script just wrote. Caught on `student_assignment`:
    the FIRST real Tab press landed on a live, on-screen button with no tag
    at all, because the element the tag was written to had already been
    discarded and replaced by an identical-looking new one. Re-tagging is
    idempotent, so this simply repeats the capture until two consecutive
    reads agree on the same count and the same labels, in the same order —
    a proxy for "the tree isn't moving any more" cheap enough to poll.
    """
    prev = None
    raw = "{}"
    for _ in range(tries):
        raw = p.eval(TAG_AND_BASELINE_JS % {"scope": scope_json})
        try:
            data = json.loads(raw)
        except (TypeError, ValueError):
            time.sleep(wait)
            continue
        if "error" in data:
            return data
        sig = tuple((b["tag"], b["label"]) for b in data["baseline"])
        if sig == prev and sig:
            return data
        prev = sig
        time.sleep(wait)
    # Ran out of tries; return whatever the last read was rather than
    # nothing — a page that never stabilises is itself worth reporting via
    # whatever mismatches follow, not worth failing outright here.
    try:
        return json.loads(raw)
    except (TypeError, ValueError):
        return {"error": "tree never stabilised for tagging: %r" % (raw,)}


def audit_page(browser, port, spec):
    url = "http://127.0.0.1:%d%s" % (port, spec["url"])
    p = browser.page(url)

    if spec.get("mount"):
        wait_for_mount(p, spec["mount"])
    else:
        time.sleep(0.3)

    if spec.get("pre_js"):
        try:
            p.eval(spec["pre_js"])
        except Exception as e:  # noqa: BLE001
            return {"error": "pre_js failed: %s" % e}
    if spec.get("wait_js"):
        wait_js_condition(p, spec["wait_js"])
        time.sleep(0.25)

    scope_json = json.dumps(spec.get("scope")) if spec.get("scope") else "null"
    data = capture_stable_baseline(p, scope_json)
    if "error" in data:
        return data

    baseline = {b["i"]: b for b in data["baseline"]}
    # ⚠️ A MARGIN, NOT AN EXACT COUNT. `leaderboard.html` proved why: one
    # press out of a run can land on an element that did not exist at
    # baseline-capture time (a search overlay's input, mounted on focus of
    # the control that opens it) — untagged, and READ_ACTIVE_JS correctly
    # reports it as `i: None` rather than misattributing it. That press is
    # not wasted in the sense of finding nothing; it is spent on a REAL
    # control this sweep was never asked to tag. Pressing exactly
    # `len(baseline)` times then runs out one short of the last real tagged
    # stop, which reads as "unreached" for a control that was never actually
    # unreachable — a harness undercount, not a page defect. The margin
    # absorbs a handful of such stops without materially slowing the sweep.
    n = min(len(baseline) + 10, MAX_TABS)

    visited = set()
    no_change = []
    seen_no_change_idx = set()

    for _ in range(n):
        press_tab(p)
        raw2 = p.eval(READ_ACTIVE_JS)
        try:
            cur = json.loads(raw2)
        except (TypeError, ValueError):
            continue
        i = cur.get("i")
        if i is None or i not in baseline:
            continue
        visited.add(i)
        if i in seen_no_change_idx:
            continue
        base = baseline[i]["style"]
        if not styles_differ(base, cur["style"]):
            seen_no_change_idx.add(i)
            no_change.append(baseline[i])

    unreached = [baseline[i] for i in baseline if i not in visited]

    return {
        "count": len(baseline),
        "visited": len(visited),
        "no_change": no_change,
        "unreached": unreached,
        "unreachable_candidates": data.get("unreachable_candidates", []),
    }


def take_named_shots(browser, port, shots_dir):
    """A handful of named before/after-style screenshots for the report —
    not part of the pass/fail contract. `tabs` is a FIXED, checked count per
    target rather than "land on the first tagged control": that landed once
    on an off-screen tooltip card, which proved nothing to a human looking
    at the PNG. A small fixed count lands on an always-in-viewport nav-level
    control at both widths."""
    targets = [
        ("student_class", "/student/class-fixture.html", "mrb-student", None,
         None, None, 2),
        ("teacher_class_detail", "/teacher_fixtures/class-detail-fixture.html",
         "mrb-teacher", None, None, None, 2),
        ("set_work_sheet", "/teacher_fixtures/class-detail-fixture.html",
         "mrb-teacher", "MRB_SET_WORK_OPEN('');",
         "!!(document.querySelector('.sw-overlay') && "
         "document.querySelector('.sw-overlay').offsetParent)", ".sw-overlay",
         2),
    ]
    for name, url, mount, pre_js, wait_js, scope, tabs in targets:
        for width in (1280, 390):
            full = "http://127.0.0.1:%d%s" % (port, url)
            p = browser.page(full)
            if mount:
                wait_for_mount(p, mount)
            if pre_js:
                p.eval(pre_js)
            if wait_js:
                wait_js_condition(p, wait_js)
                time.sleep(0.25)
            scope_json = json.dumps(scope) if scope else "null"
            capture_stable_baseline(p, scope_json)
            landed = None
            for _ in range(tabs):
                press_tab(p)
                raw2 = p.eval(READ_ACTIVE_JS)
                try:
                    landed = json.loads(raw2)
                except (TypeError, ValueError):
                    landed = None
            out = os.path.join(shots_dir, "%s-%d.png" % (name, width))
            p.screenshot(out, width=width, height=900, full_page=False)
            print("     shot: %s  (focused: %s)"
                  % (out, (landed or {}).get("tag")))


def main(argv):
    filters = [a for a in argv if not a.startswith("-")]
    shots_dir = None
    if "--shots" in argv:
        shots_dir = argv[argv.index("--shots") + 1]
        os.makedirs(shots_dir, exist_ok=True)

    todo = [pg for pg in PAGES
            if not filters or any(f in pg["key"] for f in filters)]

    print("\nfocus_audit — keyboard focus visibility, %d page(s)\n"
          % len(todo))

    server, port = cdp.serve(REPO)
    failed = 0
    try:
        for spec in todo:
            with cdp.Browser() as b:
                result = audit_page(b, port, spec)
            if "error" in result:
                failed += 1
                print("  %-24s ❌ %s" % (spec["key"], result["error"]))
                continue
            problems = len(result["no_change"]) + len(result["unreached"])
            if problems:
                failed += 1
                print("  %-24s ❌ %d/%d visited, %d no-visible-change, "
                      "%d unreached, %d unreachable-candidate(s)"
                      % (spec["key"], result["visited"], result["count"],
                         len(result["no_change"]), len(result["unreached"]),
                         len(result["unreachable_candidates"])))
                for el in result["no_change"][:20]:
                    print("       NO CHANGE  <%s class=%r> %r"
                          % (el["tag"], el["cls"], el["label"]))
                for el in result["unreached"][:10]:
                    print("       UNREACHED  <%s class=%r> %r"
                          % (el["tag"], el["cls"], el["label"]))
                for el in result["unreachable_candidates"][:10]:
                    print("       NOT FOCUSABLE AT ALL  <%s class=%r> %r"
                          % (el["tag"], el["cls"], el["label"]))
            else:
                print("  %-24s ✅  %d/%d control(s), all show a visible "
                      "change on Tab" % (spec["key"], result["visited"],
                                          result["count"]))

        if shots_dir:
            print("\n  shots -> %s" % shots_dir)
            with cdp.Browser() as b:
                take_named_shots(b, port, shots_dir)
    finally:
        server.shutdown()

    print()
    if failed:
        print("  FAIL  %d of %d page(s).\n" % (failed, len(todo)))
        return 1
    print("  PASS  every page: every reachable control shows a visible "
          "change on Tab, and Tab reaches everything tagged.\n")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
