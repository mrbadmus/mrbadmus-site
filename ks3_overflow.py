#!/usr/bin/env python3
"""ks3_overflow.py — the 390px gate. A KS3 page must never scroll sideways.

    python3 ks3_overflow.py            # the sample, as verify_ks3 runs it
    python3 ks3_overflow.py --all      # every built page, slower

Most of Rainford's students will meet this platform on a phone first, so a page
that scrolls sideways is not cosmetic — it is the first impression, and it is
the one interaction a student cannot undo by scrolling the other way.

── What this gate asserts, and why it is not just scrollWidth ──────────────

Three things, in increasing order of how early they catch the mistake:

  1. `documentElement.scrollWidth <= clientWidth`  — the page does not scroll.
  2. `body.scrollWidth <= clientWidth`             — nor does the body.
  3. EVERY element wider than the viewport sits inside an ancestor with
     `overflow-x: auto` or `scroll`.

(3) is the one that earns its keep. (1) and (2) describe the SYMPTOM, and they
go red only once the damage is already on screen. (3) describes the RULE — wide
content lives in its own scroller — and it fails at the component, by name, the
moment somebody adds a 900px figure without a `.ks3-figure-scroll` around it.
A gate that names the component is a gate somebody can act on.

It also stops (1) and (2) being satisfied the wrong way. `overflow-x: hidden` on
a wrapper would make the document stop scrolling while quietly CLIPPING the
right-hand end of a diagram — the page looks fixed and the content is gone.
Under (3) that is still a failure, because `hidden` is not a scroller.

── What the sweep found on 20 Aug 2026, and what it did NOT find ──────────

The brief for this gate said all 294 KS3 pages scroll sideways at 390px and
that the header trail is what overflows. Measured over all 295 built pages,
BOTH HALVES ARE FALSE:

  * `documentElement.scrollWidth` equals `clientWidth` — 390 — on every single
    page. No KS3 page scrolls sideways at 390px.
  * The header trail overflows nowhere. MRB-229 already ruled and fixed exactly
    this: below 700px the trail shows unit and page only and elides the rest,
    and `shared/ks3.css` says in as many words that "the page never scrolls
    sideways". The finding the brief carried was stale.

19 pages DO hold an element wider than the viewport — 18 wide `<svg>` figures
and one `.ks3-smatrix-table` — and every one of them is inside a dedicated
`.ks3-figure-scroll` or `.ks3-smatrix-scroll` with `overflow-x: auto`. That is
the correct pattern, not a defect: a diagram of the digestive system is 900px
wide because it has to be, and it scrolls inside its own frame.

So nothing was fixed, because nothing was broken. What was missing was THIS —
MRB-229's ruling had no gate, so it could regress silently, and a regression
would show up first on a phone belonging to a student who will never file a
bug. That is what this file is for.
"""

import json
import os
import sys

VIEWPORT = (390, 844)

# The served tree. Cloudflare serves from mrbadmus_site/, so this is the markup
# a student's phone actually runs.
KS3_OUT = os.path.join("mrbadmus_site", "ks3")

# ⚖️ THE SAMPLE IS A SAMPLE, AND IT SAYS SO. Driving 295 pages takes ~220s,
# which is too slow to sit inside every verify_ks3 run; the sample is ~25 pages
# and a few seconds. `--all` exists so the full sweep is one flag away, and the
# report prints how many were skipped rather than implying full coverage.
#
# What is in it, and why:
#   * the FIRST authored lesson of every unit — breadth across unit titles,
#     which is what the header trail's width actually varies with;
#   * every canvas-bearing C1 page — the instruments are the widest, most
#     absolutely-positioned things in the key stage and the likeliest to break;
#   * the hub and one unit index — the browse layer is built by a different
#     path from lesson pages and has its own crumb row (`.ks3-crumbs`), which
#     MRB-229 had to fix separately for exactly that reason.
CANVAS_PAGES = (
    "chemistry/particles-and-their-behaviour/particle-model.html",
    "chemistry/particles-and-their-behaviour/changes-of-state.html",
    "chemistry/particles-and-their-behaviour/diffusion.html",
    "chemistry/particles-and-their-behaviour/gas-pressure.html",
    "chemistry/particles-and-their-behaviour/solids-liquids-and-gases.html",
)

BROWSE_PAGES = (
    "index.html",
    "chemistry/particles-and-their-behaviour/index.html",
)


_PROBE_TMPL = """(function () {
  var vw = %d, eps = 0.5;
  var d = document.documentElement;
  var wide = [];
  var all = document.querySelectorAll('*');
  for (var i = 0; i < all.length; i++) {
    var el = all[i], rc = el.getBoundingClientRect();
    if (rc.width === 0 && rc.height === 0) { continue; }
    if (rc.right <= vw + eps && rc.left >= -eps) { continue; }
    // Wider than the viewport. Legal ONLY inside a real scroller.
    var scroller = null, n = el.parentElement;
    while (n && n !== document.documentElement) {
      var ox = getComputedStyle(n).overflowX;
      if (ox === 'auto' || ox === 'scroll') {
        scroller = n.tagName + '.' + String(n.className || '').split(' ')[0];
        break;
      }
      n = n.parentElement;
    }
    if (scroller) { continue; }
    var cn = el.className;
    if (cn && cn.baseVal !== undefined) { cn = cn.baseVal; }
    wide.push(el.tagName + '.' + (String(cn || '').split(' ')[0] || '(no class)')
      + ' [left=' + Math.round(rc.left) + ' right=' + Math.round(rc.right) + ']');
  }
  return JSON.stringify({
    docScroll: d.scrollWidth, docClient: d.clientWidth,
    bodyScroll: document.body.scrollWidth,
    unscrolled: wide.length, examples: wide.slice(0, 8)
  });
})()"""


# ⊕ MRB-280, 21 Aug 2026 — the probe is width-parameterised so the SAME
# measurement can run at more than one phone width. It was pinned to 390.
def _probe(vw):
    return _PROBE_TMPL % (vw,)


# 390 is a modern phone. 320 is an iPhone SE and a budget Android, and
# Rainford students are on what they have. 390 GATES; 320 REPORTS, because
# what fails only at 320 is a decision for Mide and not a thing to fix
# quietly inside a run that was not asked to.
NARROW = (320, 568)


def sample(root=KS3_OUT):
    """One lesson per unit, every canvas page, the hub and a unit index."""
    import ks3_data

    pages, seen = [], set()

    def add(rel):
        if rel not in seen and os.path.exists(os.path.join(root, rel)):
            seen.add(rel)
            pages.append(rel)

    for rel in BROWSE_PAGES:
        add(rel)
    for unit in ks3_data.build_units():
        for lesson in unit["lessons"]:
            if lesson.get("authored"):
                # find the built page for this slug
                for r, _dirs, files in os.walk(root):
                    if (lesson["slug"] + ".html") in files:
                        add(os.path.relpath(
                            os.path.join(r, lesson["slug"] + ".html"), root))
                        break
                break
    for rel in CANVAS_PAGES:
        add(rel)
    return pages


def every(root=KS3_OUT):
    out = []
    for r, _dirs, files in os.walk(root):
        for f in sorted(files):
            if f.endswith(".html"):
                out.append(os.path.relpath(os.path.join(r, f), root))
    return sorted(out)


def run(pages, cdp, root=KS3_OUT, viewport=VIEWPORT):
    """Drive `pages` at `viewport`. Returns (problems, checked).

    One browser for the whole run rather than the harness's usual fresh browser
    per page: nothing here mutates state that survives a navigation, and 295
    launches is four minutes of nothing.
    """
    problems = []
    serve_root = os.path.dirname(root) or "."
    prefix = "/" + os.path.basename(root)
    server, port = cdp.serve(serve_root)
    try:
        with cdp.Browser() as b:
            page = b.attach()
            page.set_viewport(*viewport)
            for rel in pages:
                url = "http://127.0.0.1:%d%s/%s" % (port, prefix, rel)
                page.goto(url)
                d = json.loads(page.eval(_probe(viewport[0])))
                if d["docScroll"] > d["docClient"]:
                    problems.append(
                        "%s — the DOCUMENT scrolls sideways at %dpx: "
                        "scrollWidth %s against clientWidth %s"
                        % (rel, viewport[0], d["docScroll"], d["docClient"]))
                if d["bodyScroll"] > d["docClient"]:
                    problems.append(
                        "%s — the BODY scrolls sideways at %dpx: "
                        "scrollWidth %s against clientWidth %s"
                        % (rel, viewport[0], d["bodyScroll"], d["docClient"]))
                if d["unscrolled"]:
                    problems.append(
                        "%s — %d element(s) wider than the %dpx viewport with "
                        "NO `overflow-x: auto` ancestor. Wide content belongs "
                        "in its own scroller (.ks3-figure-scroll, "
                        ".ks3-smatrix-scroll); without one it pushes the page "
                        "sideways: %s"
                        % (rel, d["unscrolled"], viewport[0],
                           "; ".join(d["examples"])))
    finally:
        server.shutdown()
    return problems, len(pages)


def main(argv):
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import ks3_browser as cdp

    full = "--all" in argv
    pages = every() if full else sample()
    total = len(every())

    print("── the 390px gate ──")
    problems, checked = run(pages, cdp)
    if full:
        print("  driving ALL %d built pages at %dx%d" % (checked, *VIEWPORT))
    else:
        print("  driving %d of %d built pages at %dx%d — one lesson per unit, "
              "every canvas-bearing C1 page, the hub and a unit index. "
              "%d not driven; `--all` drives them."
              % (checked, total, VIEWPORT[0], VIEWPORT[1], total - checked))

    if problems:
        print("\n  %d PROBLEM(S):" % len(problems))
        for p in problems:
            print("    FAIL %s" % p)
        return 1
    print("  PASS  no page scrolls sideways, and every element wider than the "
          "viewport is inside its own scroller")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
