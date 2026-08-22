#!/usr/bin/env python3
"""student_theme_shots.py — photograph the bench themes, so a human can LOOK.

    python3 student_theme_shots.py

Writes six full-page PNGs into `docs/ks3/shots/themes-<date>/`:

    harbour-390.png    chalk-390.png    graphite-390.png
    harbour-1460.png   chalk-1460.png   graphite-1460.png

── WHY THIS EXISTS AS ITS OWN SCRIPT ────────────────────────────────────

The six bench themes shipped on 22 August 2026 with every measurement green
and NOBODY HAVING LOOKED AT THE PAGE. That is a shape this repo has been
burned by twice already, both times in the same direction — the instrument
was right about the thing it measured and blind to the thing that mattered:

  · five dead controls shipped because no sweep had ever PRESSED anything;
  · a docket shipped telling a student the wrong number of questions and the
    wrong due date, while the text gate reported it clean, because the gate's
    tells held names and no numbers.

`student_themes.py` is the colour GATE. It reads computed style and does WCAG
arithmetic on it, and it is a good gate — but a contrast ratio is a number
about two colours, not about a page. It cannot see text sitting off the right
edge at 390px, a docket that has stopped reading as paper, or a light theme
fighting the cream page it is embedded in. Those need an eye, and an eye needs
a picture.

So this is a DELIVERABLE, not a gate: it asserts nothing and exits 0 as long
as it managed to take the photographs. Keeping it separate from
`student_themes.py` means a RED gate still produces pictures to look at, which
is exactly the morning they are most wanted.

── THE FIXTURE, NOT THE PRODUCTION PAGE ─────────────────────────────────

Same choice, for the same reason, that `student_themes.py` documents:
`class.html` carries no data of its own and mounts whatever the database held
that morning, so it needs a live session and photographs differently every
day. `class-fixture.html` is the same bytes apart from its banner and its last
two script tags, with known values. Colour and layout are properties of the
CSS and the markup, neither of which the data seam touches.

⚠️ THE VIEWPORT IS SET BEFORE THE PAGE LOADS, NOT AFTER. Every drive in this
repo used to navigate first and resize second, and that measured the WRONG
BREAKPOINT — silently. The CDP override persists across navigations on one
target, so the "390px" page actually mounted at whatever the previous capture
left behind; and the page decides its header treatment once, at mount, from
its own width. The result was a 390px screenshot of the DESKTOP header and a
1460px screenshot of the PHONE one, both looking plausible. A real device does
not resize into a page; it opens one at its own size. So: blank page, set the
size, THEN navigate.

⚠️ HARBOUR IS THE ABSENCE OF THE ATTRIBUTE, and is photographed that way
rather than as `data-bench-theme="harbour"`. Design's README says "(absent =
harbour)", and the default silently reverting to the old graphite is a real
failure mode — one `student_themes.py` asserts against. Writing the attribute
here would photograph a case no student is ever in, and would hide exactly
that regression from the picture.
"""

import datetime
import os
import sys
import time

import ks3_browser as cdp

SITE = "mrbadmus_site"
PAGE = "/student/class-fixture.html"

# harbour first, and as None — the attribute is REMOVED for it, not written.
# See the note in the docstring: absent is the case a student is actually in.
THEMES = [
    ("harbour", None),
    ("chalk", "chalk"),
    ("graphite", "graphite"),
]

# A phone, and the desktop the parity and colour gates already measure at.
# The heights are the viewport's, not the capture's — the screenshot is
# full-page and clips to the settled content height.
SIZES = [(390, 844), (1460, 1200)]

# The theme is a CSS attribute, so the page does not re-mount when it changes;
# it re-paints. Long enough for that, and for any transition on the tokens to
# have finished, before the shutter.
THEME_SETTLE = 0.6

_SET_THEME = (
    "(function(t){var e=document.documentElement;"
    "if(t===null){e.removeAttribute('data-bench-theme');}"
    "else{e.setAttribute('data-bench-theme',t);}"
    "return String(e.getAttribute('data-bench-theme'));})(%s)"
)


def _wait_for_fonts(page, seconds=20.0, poll=0.2):
    """Don't photograph a page whose faces have not arrived.

    Cheap insurance rather than a fix for a known incident, and it is written
    down as such because the temptation to claim otherwise was real: the first
    run of this script produced six PNGs in which the bench checklist rendered
    at about 1.8:1 on chalk, and "the webfont had not settled" was a tidy
    explanation that turned out to be WRONG. The page really did render that
    colour — see the `--st-room-text` finding of 23 Aug 2026 — and it was the
    working tree, not the shutter, that had moved underneath the second run.

    The lesson kept here is the one that generalises: when two runs of the
    same script disagree, find out WHICH IS TRUE before believing either. A
    picture that invents a defect is as bad as a gate that misses one, and
    worse if somebody then "fixes" a page that was fine.

    The wait stays because a half-loaded face genuinely can change apparent
    weight, and a node count cannot see it — the DOM is complete throughout.
    Only `document.fonts.ready` knows."""
    end = time.time() + seconds
    while time.time() < end:
        if page.eval("(document.fonts && document.fonts.status) || 'loaded'") \
                == "loaded":
            return True
        time.sleep(poll)
    return False


def _wait_for_mount(page, seconds=30.0, poll=0.2):
    """Rendered AND settled: the host has children, and has stopped gaining
    them. A fixed sleep photographs a page mid-mount on a slow run and looks
    like a layout bug."""
    end, last = time.time() + seconds, 0
    while time.time() < end:
        n = page.eval(
            "(function(){var h=document.getElementById('mrb-student');"
            "return h ? h.getElementsByTagName('*').length : -1;})()")
        n = n if isinstance(n, int) else 0
        if n > 20 and n == last:
            return n
        last = n
        time.sleep(poll)
    return last


def main():
    stamp = os.environ.get("MRB_SHOT_DATE") or datetime.date.today().isoformat()
    out_dir = os.path.join("docs", "ks3", "shots", "themes-%s" % stamp)
    os.makedirs(out_dir, exist_ok=True)

    print("\n📸  student_theme_shots — the bench, in three themes, "
          "at two widths\n")
    print("     %s  →  %s/" % (PAGE, out_dir))

    server, port = cdp.serve(SITE)
    url = "http://localhost:%d%s" % (port, PAGE)
    written = []
    try:
        with cdp.Browser() as b:
            for theme, attr in THEMES:
                for w, h in SIZES:
                    # ⚠️ ORDER IS LOAD-BEARING: blank, size, THEN navigate.
                    b.page("about:blank", settle=0.15).set_viewport(w, h)
                    page = b.page(url, settle=0.8)
                    nodes = _wait_for_mount(page)

                    got = page.eval(_SET_THEME % (
                        "null" if attr is None else '"%s"' % attr))
                    time.sleep(THEME_SETTLE)

                    # Say what the page ACTUALLY reports, not what was asked
                    # for. A theme that failed to apply must not photograph
                    # under the name of the theme it was supposed to be.
                    want = "null" if attr is None else attr
                    if str(got) != want:
                        raise SystemExit(
                            "the page root reports data-bench-theme=%r after "
                            "asking for %r — the capture would be mislabelled"
                            % (got, want))

                    # Confirm the viewport really is the one we asked for,
                    # BEFORE the shutter. This is the check that would have
                    # caught the resize-after-navigate bug the moment it
                    # happened rather than months later.
                    iw = page.eval("window.innerWidth")
                    if int(iw or 0) != w:
                        raise SystemExit(
                            "window.innerWidth is %r, asked for %d — the "
                            "capture would be at the wrong breakpoint"
                            % (iw, w))

                    fonts = _wait_for_fonts(page)

                    # ⚠️ CAPTURE UNTIL TWO IN A ROW AGREE, byte for byte.
                    # `document.fonts.ready` resolves before the repaint that
                    # uses the new faces has necessarily landed, and the same
                    # "measure until it stops moving" discipline that
                    # ks3_browser applies to the clip height applies here to
                    # the pixels. Cheap, and it turns a flaky deliverable into
                    # a deterministic one.
                    out = os.path.join(out_dir, "%s-%d.png" % (theme, w))
                    prev, stable = None, False
                    for _ in range(8):
                        page.screenshot(out, width=w, height=h, full_page=True)
                        with open(out, "rb") as fh:
                            cur = fh.read()
                        if cur == prev:
                            stable = True
                            break
                        prev = cur
                        time.sleep(0.4)
                    if not (fonts and stable):
                        raise SystemExit(
                            "%s @%dpx never settled (fonts=%s, pixels=%s) — a "
                            "photograph of a half-painted page is worse than "
                            "no photograph" % (theme, w, fonts, stable))
                    pw, ph = cdp.png_size(out)
                    print("     %-9s %4dpx  %5d nodes  %4d×%-5d  %s"
                          % (theme, w, nodes, pw, ph, out))
                    # Console errors go on their OWN lines, in full, not
                    # truncated onto the end of the row. A photograph of a
                    # page that failed to load an asset is still a
                    # photograph — say which it is.
                    for e in page.console_errors():
                        print("               console: %s" % e[:160])
                    written.append(out)
    finally:
        server.shutdown()

    print("\n     %d written:" % len(written))
    for path in written:
        print("       %s  (%d bytes)" % (path, os.path.getsize(path)))
    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
