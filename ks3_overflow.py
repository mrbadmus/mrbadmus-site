#!/usr/bin/env python3
"""ks3_overflow.py — the phone gate. A KS3 page must never scroll sideways.

⊕ MRB-229 · 5 Sep 2026 — THIS FILE USED TO BE "the 390px gate", and the rename
is the finding. It measured one width, 390. `NARROW = (320, 568)` was defined
below and referenced by nothing, so the 320px pass its own comment described
had never run. `chemistry/mixtures-and-separation/chromatography.html` was
sitting at `scrollWidth` 326 against a 320px viewport the whole time — and at a
clean 390 against 390, which is what the gate kept reporting. It now drives
both widths, and the pages that have ever failed are pinned into the sample by
name (see REGRESSION_PAGES) rather than left to the luck of "first lesson in
the unit". The root cause is written up in `shared/ks3.css` at `.ks3-cards`.


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

── What `--all` measured on 5 Sep 2026, at BOTH widths ────────────────────

  * `documentElement.scrollWidth` equals `clientWidth` on all 297 built pages,
    at 390 AND at 320. No KS3 page scrolls sideways at either width. That is
    MRB-229's ruling, and it is now true — chromatography was the last one.
  * Rule (3) is NOT clean, and the 20 Aug note above ("every one of them is
    inside a dedicated scroller") has DRIFTED. Three physics pages now hold a
    wide element with no scroller at 390:
        physics/energy-at-home/fuels-and-energy-resources.html  1 × .ks3-grid2-tag
        physics/energy-at-home/reading-a-fuel-bill.html         1 × .ks3-beam-caption
        physics/energy-transfers/simple-machines.html           2 × .ks3-beam-label
    None of them scrolls the document — each is a clipped edge, which is the
    failure mode rule (3) exists to name and which nobody would see by looking.
    They are PRE-EXISTING (measured against HEAD's stylesheet, unchanged) and
    they are not MRB-229's to fix: this ticket is the sideways scroll. They
    want a scroller, or a narrower drawing, and that is a physics-figure job.
    ⚠️ They sit OUTSIDE the default sample, so verify_ks3 is green while they
    are red under `--all`. Left deliberately un-pinned at 390 — grandfathering
    them at the gating width is how rule (3) would rot.
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

# ⊕ MRB-229 · 5 Sep 2026 — PAGES WITH A KNOWN PAST FAILURE, PINNED INTO THE
# SAMPLE FOREVER. A regression gate that does not drive the page that once
# regressed is decoration, and this file had exactly that hole: the sample is
# "the FIRST authored lesson of every unit", chromatography is not the first
# lesson of Mixtures and Separation, so the only page in the key stage that has
# ever scrolled sideways was never driven except under `--all`.
#
# Anything fixed here earns a line. Do not prune it once it is green — green is
# what it is here to keep proving.
REGRESSION_PAGES = (
    # 291.7px of min-content from the single word "Chromatography" blew the
    # one-column card track past a 252px container and scrolled the document to
    # 326 at 320px. Fixed in `shared/ks3.css` (`.ks3-cards > li{min-width:0}`
    # plus `overflow-wrap` on the card front); see the MRB-229 block there.
    "chemistry/mixtures-and-separation/chromatography.html",
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
# Rainford students are on what they have.
#
# ⊕ MRB-229 · 5 Sep 2026 — **320 NOW GATES TOO, AND UNTIL TODAY IT RAN AT ALL.**
# This constant was defined here on 21 Aug and referenced by nothing — not by
# `run`, not by `main`, not by verify_ks3. The comment above it said "320
# REPORTS", and no 320px measurement was ever taken. That is precisely why
# `chemistry/mixtures-and-separation/chromatography.html` sat broken for a
# fortnight with a green gate over it: it does NOT scroll at 390 (measured 390
# against 390, clean, before and after the fix), it only ever scrolled at 320,
# and 320 was the width nobody was driving. A constant is not a gate.
#
# What gates at 320 and what does not, deliberately:
#
#   * the DOCUMENT and BODY not scrolling — HARD. That is MRB-229's actual
#     ruling, it is now true on all 297 built pages, and it is the thing a
#     student feels. Nothing is grandfathered.
#   * an element wider than the viewport with no scroller — hard only ABOVE the
#     count pinned in NARROW_KNOWN below, because two pages already hold one
#     and neither is MRB-229's to fix tonight.
#
# The old comment worried that fixing a 320-only failure would be "a decision
# for Mide". Not scrolling sideways is not a design decision — Mide already
# ruled it. Design decisions AT 320 (the trail's legibility, which this file
# does not measure) remain his, and remain untouched.
NARROW = (320, 568)

# Elements wider than 320px with no `overflow-x` scroller, as measured across
# all 297 built pages on 5 Sep 2026. Both PRE-DATE the MRB-229 fix — proved by
# re-measuring the identical HTML against HEAD's stylesheet, which returns
# these two rows byte-identical — and NEITHER scrolls the document, so each is
# a clipped edge rather than a sideways page.
#
# They are pinned rather than fixed because MRB-229 is the sideways-scroll
# ticket and these are two physics components wanting their own scroller, which
# is a different unit of work. Pinning them is what lets the rest of rule (3)
# gate at 320 today instead of waiting on them.
#
# ⚠️ These counts are a CEILING, not a licence. Drop one to 0 when the page is
# fixed; never raise one to make a new failure pass.
NARROW_KNOWN = {
    # two `.ks3-grid2-tag` spans, right edges at 347 and 327
    "physics/energy-at-home/fuels-and-energy-resources.html": 2,
    # one `.ks3-beam-caption` SVG <text>, spanning -27 to 347
    "physics/energy-at-home/reading-a-fuel-bill.html": 1,
}


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
    # ⊕ MRB-229 — last, and unconditional. See REGRESSION_PAGES.
    for rel in REGRESSION_PAGES:
        add(rel)
    return pages


def every(root=KS3_OUT):
    out = []
    for r, _dirs, files in os.walk(root):
        for f in sorted(files):
            if f.endswith(".html"):
                out.append(os.path.relpath(os.path.join(r, f), root))
    return sorted(out)


def run(pages, cdp, root=KS3_OUT, viewport=VIEWPORT, known=None):
    """Drive `pages` at `viewport`. Returns (problems, checked).

    One browser for the whole run rather than the harness's usual fresh browser
    per page: nothing here mutates state that survives a navigation, and 295
    launches is four minutes of nothing.

    `known` (⊕ MRB-229) maps a page to the number of unscrolled wide elements
    it is ALREADY known to hold, so rule (3) can gate at a width where a couple
    of pre-existing rows would otherwise make it permanently red. It applies to
    rule (3) only: the document and body assertions are never grandfathered,
    and passing `known` cannot suppress them. `None` means grandfather nothing,
    which is what 390 does.
    """
    allow = known or {}
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
                budget = allow.get(rel, 0)
                if d["unscrolled"] > budget:
                    problems.append(
                        "%s — %d element(s) wider than the %dpx viewport with "
                        "NO `overflow-x: auto` ancestor%s. Wide content belongs "
                        "in its own scroller (.ks3-figure-scroll, "
                        ".ks3-smatrix-scroll); without one it pushes the page "
                        "sideways: %s"
                        % (rel, d["unscrolled"], viewport[0],
                           "" if not budget else
                           " (%d pinned in NARROW_KNOWN, so %d are NEW)"
                           % (budget, d["unscrolled"] - budget),
                           "; ".join(d["examples"])))
                # ⚠️ A pinned page that has been FIXED should lose its pin, or
                # the pin quietly re-licenses the next regression on that page.
                elif budget and d["unscrolled"] < budget:
                    problems.append(
                        "%s — NARROW_KNOWN pins %d unscrolled wide element(s) "
                        "at %dpx and only %d are left. Good news, and it still "
                        "fails: lower the pin to %d so the page cannot silently "
                        "regress back up to it."
                        % (rel, budget, viewport[0], d["unscrolled"],
                           d["unscrolled"]))
    finally:
        server.shutdown()
    return problems, len(pages)


def main(argv):
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import ks3_browser as cdp

    full = "--all" in argv
    pages = every() if full else sample()
    total = len(every())

    # ⊕ MRB-229 — BOTH widths, every run. 390 was the only one being measured,
    # and the one page that has ever scrolled sideways scrolled only at 320.
    problems = []
    for vp, known in ((VIEWPORT, None), (NARROW, NARROW_KNOWN)):
        print("── the %dpx gate ──" % vp[0])
        found, checked = run(pages, cdp, viewport=vp, known=known)
        if full:
            print("  driving ALL %d built pages at %dx%d" % (checked, *vp))
        else:
            print("  driving %d of %d built pages at %dx%d — one lesson per "
                  "unit, every canvas-bearing C1 page, the hub, a unit index "
                  "and %d regression page(s). %d not driven; `--all` drives "
                  "them."
                  % (checked, total, vp[0], vp[1], len(REGRESSION_PAGES),
                     total - checked))
        if known:
            print("  %d page(s) pinned in NARROW_KNOWN (pre-existing clipped "
                  "edges, neither scrolls the document); the document and body "
                  "assertions are NOT grandfathered at any width."
                  % len(known))
        if found:
            print("  %d PROBLEM(S):" % len(found))
            for p in found:
                print("    FAIL %s" % p)
        else:
            print("  PASS  no page scrolls sideways, and every element wider "
                  "than the viewport is inside its own scroller")
        problems += found

    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
