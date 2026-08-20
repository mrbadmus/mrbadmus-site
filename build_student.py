#!/usr/bin/env python3
"""build_student.py — the student class view and assignment, generated.

    python3 build_student.py

Writes, and nothing else:

    mrbadmus_site/student/class-preview.html
    mrbadmus_site/student/assignment-preview.html
    student/class-preview.html            (mirror, as build_ks3.py mirrors ks3/)
    student/assignment-preview.html

⛔ IT NEVER WRITES `student/class.html` OR `student/assignment.html`. Those are
the live pages and they are not this run's to touch. The swap from `-preview`
to the live paths is a separate, one-line change for Mide to approve, and
`_REFUSED` below makes writing to them impossible by accident rather than by
discipline.

── Where the design comes from ────────────────────────────────────────────

`docs/ks3/design-reference/student/`, vendored from Design's 19 Aug 22:56
delivery. It sits beside the KS3 lesson references in the same folder for the
same reason: a design reference that lives on somebody's Desktop is a design
reference that cannot be built from, diffed against, or reviewed in a commit.

Design's delivery is a Claude Design source — a template in `sc-if` / `sc-for`
/ `{{ }}` plus a `class Component extends DCLogic` — and a STANDALONE compile of
it with React, the tokens and the fonts inlined. The standalone is the artefact
this reads.

── Why this renders rather than re-implements, and what that costs ────────

The brief is "reproduce Design's HTML exactly" and "no licence to invent shapes
or components Design has not drawn". Hand-porting 556 lines of template, 295
inline styles and 124 clamp() literals into a Python emitter would satisfy that
only as long as nobody made a mistake, and every future edit would be a fresh
chance to drift.

So the markup is not retyped. This loads Design's own standalone file in
headless Chrome, lets Design's own logic render it, and takes the resulting
DOM. Exactness stops being an effort and becomes a property: the only way the
output can differ from Design's file is if Design's file changed.

⚠️ WHAT THIS IS NOT, stated plainly because a page that LOOKS finished is the
easiest thing in this repo to over-trust:

  * It is STATIC. The rendered DOM is a photograph of one state — the shipping
    state, `layout: Auto`, `classState: Work set`. None of the behaviour in
    Design's logic class comes with it: no recall round, no week filter, no
    work-row expansion, no marker sheet, no timer.
  * It carries NO DATA. Every name, score, date and question in it is Design's
    authored example content. Wiring it to production is phase 8c and has not
    been done.
  * It is therefore NOT A CANDIDATE to replace the live pages, and the parity
    report says so in the same words.

Static output first is the brief's own order, and it is the right one: parity
with Design is worth establishing while it is still cheap to check.

── ⚑ THE 390px GAP, MEASURED — the one thing a snapshot cannot carry ──────

At DESKTOP the reproduction is exact. Measured against Design's own file at
1460px: 563 nodes against 563, 1460×2400 against 1460×2400, identical tag
census, identical text, identical resolved font, ground and ink, no horizontal
overflow. The assignment likewise, 177 against 177.

At 390px IT IS NOT, and the reason is structural rather than a bug to fix here.

Design builds responsiveness two ways, and says so in §6 of both handoff notes.
Everything CONTINUOUS is a `clamp(min, Ncqw, max)` container query in the
element's own inline style — and those survive the snapshot perfectly, which is
why the type and the padding do shrink. Everything DISCRETE is one of TEN
measured switches (eight on the assignment) computed in JavaScript from the
root's width: `benchCols`, `docketOrder`, `statsBasis`, `railDisplay`,
`spineCols`, `rowCols`, `chaseCols`, `boardCols`, `recallCols`, `optCols`,
`ghostRight`. Design's own note is explicit that these "cannot be interpolated".

A photograph taken at 1460px therefore carries the DESKTOP value of all ten,
baked into the inline styles, and no width can change them afterwards. Measured
at 390px:

    Design's file      scrollWidth 390 = clientWidth 390, 0 elements overflowing
    this generated one scrollWidth 610 vs clientWidth 390, 101 overflowing

The twelve-column term spine alone needs 662px and Design's phone rule is two
rows of six; the work-row grid should drop from `46px 20px 1fr auto` to
`18px 1fr auto`; the docket should move above the copy. None of that happens,
because none of it is CSS.

NOT APPROXIMATED, deliberately. The brief's rule is that where Design's file
cannot be reproduced faithfully it is recorded rather than guessed at, and
guessing here would mean hand-writing media queries that Design did not draw
and that would then disagree with the logic class the moment either changed.

The faithful fix is to reproduce the switch TABLE — Design published all ten
values for all three bands — as a small runtime shim, which is behaviour and
therefore phase 8c. Until then this preview is desktop-accurate and phone-wrong,
and `student_parity.py` asserts both halves so neither can be forgotten.
"""

import html
import os
import re
import shutil
import sys

REPO = os.path.dirname(os.path.abspath(__file__))
REF = os.path.join("docs", "ks3", "design-reference", "student")
SITE_OUT = os.path.join("mrbadmus_site", "student")
MIRROR_OUT = "student"

# ⛔ The live pages. Named here so the guard is a list somebody can read, not a
# convention somebody has to remember.
_REFUSED = {"class.html", "assignment.html", "classes.html", "settings.html",
            "claim-confirm.html"}

VIEWPORT = (1460, 1200)
SETTLE_MS = 2.5

PAGES = [
    dict(
        out="class-preview.html",
        src="standalone/MrBadmusAI Class View.html",
        title="8r/Sc1 · My class · MrBadmusAI",
        note="the class view",
    ),
    dict(
        out="assignment-preview.html",
        src="standalone/MrBadmusAI Assignment.html",
        title="Assignment · 8r/Sc1 · MrBadmusAI",
        note="the assignment",
    ),
]


# ── the banner every preview page carries ─────────────────────────────────
#
# ⚖️ IT IS AN HTML COMMENT AND NOT ON THE PAGE, DELIBERATELY. KS3 §8.10 — no
# platform self-explanation on a student surface — and a preview page is still
# a student surface. The person who needs this warning is reading the source or
# the report, never the rendering.
_BANNER = """<!--
  ══════════════════════════════════════════════════════════════════════════
  GENERATED — do not edit. `python3 build_student.py`
  ══════════════════════════════════════════════════════════════════════════

  This is a PREVIEW of %s, rendered from Design's own delivery
  (docs/ks3/design-reference/student/, the 19 Aug 2026 drop) so that the markup
  is Design's rather than a retyping of it.

  IT IS NOT THE LIVE PAGE and it is not a candidate to become one yet:

    * STATIC. One state only, photographed. None of Design's behaviour is
      here — no recall round, no week filter, no work-row expansion, no
      marker sheet, no timer.
    * NO REAL DATA. Every name, score, date and question below is Design's
      authored example content. Nothing is read from Supabase.
    * DESKTOP-ACCURATE, PHONE-WRONG. Design's ten discrete breakpoint
      switches are computed in JavaScript from the measured root width, so a
      snapshot taken at 1460px carries their DESKTOP values and no amount of
      resizing changes them. At 390px this page scrolls sideways (610px
      against 390px) where Design's own file does not. See build_student.py.

  The live pages are student/class.html and student/assignment.html and this
  build never writes them.
  ══════════════════════════════════════════════════════════════════════════
-->
"""


def _refuse(path):
    base = os.path.basename(path)
    if base in _REFUSED:
        raise SystemExit(
            "build_student.py REFUSES to write %s.\n"
            "  That is a LIVE student page. This generator only ever writes\n"
            "  *-preview.html. Swapping a preview onto a live path is a\n"
            "  separate, deliberate change for Mide to approve." % path)


def render(cdp, src_rel):
    """Load Design's standalone file and return (head_styles, root_html)."""
    import json
    import time

    server, port = cdp.serve(REF)
    try:
        with cdp.Browser() as browser:
            page = browser.attach()
            page.set_viewport(*VIEWPORT)
            page.goto("http://127.0.0.1:%d/%s"
                      % (port, src_rel.replace(" ", "%20")))
            time.sleep(SETTLE_MS)
            got = page.eval("""(function () {
              var root = document.querySelector('.rd[data-mode="ks3"]');
              if (!root) { return JSON.stringify({error: 'no design root'}); }
              // Everything the page's own <head> carries: the standalone has
              // the tokens, the @font-face rules and the component CSS inlined
              // there, so taking the styles wholesale is what keeps the copy
              // looking like the original rather than approximately like it.
              var styles = [];
              var sheets = document.querySelectorAll('head style');
              for (var i = 0; i < sheets.length; i++) {
                styles.push(sheets[i].textContent || '');
              }
              // The design root's own wrapper, so the page ground matches.
              var shell = root.parentElement;
              return JSON.stringify({
                error: '',
                styles: styles.join('\\n\\n'),
                root: root.outerHTML,
                shellStyle: shell ? (shell.getAttribute('style') || '') : '',
                text: (root.innerText || '').length,
                nodes: root.querySelectorAll('*').length
              });
            })()""")
            data = json.loads(got)
            if data.get("error"):
                raise SystemExit("build_student.py: %s in %s"
                                 % (data["error"], src_rel))
            return data
    finally:
        server.shutdown()


# ── the fonts, which are 75% of the page and need not be ──────────────────
#
# Design's STANDALONE compile inlines every face as base64: 28 `@font-face`
# blocks carrying 1.63 MB, which is three quarters of the generated page. That
# is right for the artefact it is — a file you double-click on a plane — and
# wrong for a page a Year 7 loads on a phone over school wifi.
#
# It is also unnecessary, and this is not an approximation. The site ALREADY
# self-hosts all seven faces at `/shared/fonts/`, KS3 lesson pages already
# preload two of them, and every one is BYTE-IDENTICAL to Design's copy —
# verified by sha256 across all seven, not assumed from the matching filenames.
#
# So the base64 blocks come out and Design's OWN `fonts.css` goes in, with its
# relative `./` rewritten to the served path. Same declarations, same font
# files, same rendering; 1.63 MB less of it.
_FONT_FACE_RE = re.compile(r"@font-face\s*\{[^}]*?url\(\s*[\"']?data:[^}]*\}",
                           re.I | re.S)

FONT_CSS = os.path.join(
    REF, "source", "_ds",
    "mrbadmusai-design-system-53dad5ae-951a-44a1-95e1-394b9762b2d1",
    "fonts", "fonts.css")

SERVED_FONTS = "/shared/fonts/"


def strip_inlined_fonts(css):
    """Return (css_without_base64_faces, replacement_face_css, n_removed, bytes)."""
    removed = _FONT_FACE_RE.findall(css)
    lean = _FONT_FACE_RE.sub("", css)
    if not os.path.exists(FONT_CSS):
        # No local face declarations to put back — keep the inlined ones rather
        # than ship a page with no fonts at all.
        return css, "", 0, 0
    faces = open(FONT_CSS, encoding="utf-8").read().replace("./", SERVED_FONTS)
    return lean, faces, len(removed), sum(len(x) for x in removed)


def page_html(spec, data):
    return (
        "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n"
        "<meta charset=\"utf-8\">\n"
        "<meta name=\"viewport\" content=\"width=device-width, "
        "initial-scale=1\">\n"
        "<title>%s</title>\n"
        "%s"
        "<style>\n%s\n%s\n</style>\n"
        "</head>\n<body style=\"margin:0;background:#FBF3E6\">\n"
        "<div style=\"%s\">\n%s\n</div>\n</body>\n</html>\n"
        % (html.escape(spec["title"]),
           _BANNER % spec["note"],
           data["faces"],
           data["styles"],
           html.escape(data.get("shellStyle") or
                       "background:var(--st-ground);min-height:100vh",
                       quote=True),
           data["root"])
    )


def write(path, body):
    _refuse(path)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(body)


def build():
    sys.path.insert(0, REPO)
    import ks3_browser as cdp

    if not os.path.isdir(REF):
        raise SystemExit(
            "build_student.py: no design reference at %s.\n"
            "  Design's delivery is vendored into the repo on purpose — a\n"
            "  reference that lives on a Desktop cannot be built from,\n"
            "  diffed against, or reviewed in a commit." % REF)

    print("\n🎓  build_student — the student preview pages\n")
    print("     reference: %s" % REF)
    written = []
    for spec in PAGES:
        src = os.path.join(REF, spec["src"])
        if not os.path.exists(src):
            raise SystemExit("build_student.py: missing %s" % src)
        data = render(cdp, spec["src"])
        lean, faces, n_faces, saved = strip_inlined_fonts(data["styles"])
        data["styles"], data["faces"] = lean, faces
        data["fontsaved"] = saved
        data["nfaces"] = n_faces
        body = page_html(spec, data)
        for out_dir in (SITE_OUT, MIRROR_OUT):
            write(os.path.join(out_dir, spec["out"]), body)
        written.append((spec["out"], data["nodes"], data["text"], len(body)))
        print("     ✅ %-24s %5d node(s), %6d char(s) of text, %7d bytes"
              % (spec["out"], data["nodes"], data["text"], len(body)))
        if data["nfaces"]:
            print("        %d inlined @font-face block(s) replaced with "
                  "%s — %s saved"
                  % (data["nfaces"], SERVED_FONTS,
                     "%.2f MB" % (data["fontsaved"] / 1048576.0)))

    print("\n     → %s/" % SITE_OUT)
    print("     → %s/  (mirror)" % MIRROR_OUT)
    print("\n     ⚠️  STATIC, and carrying Design's example data. Not a\n"
          "         candidate to replace student/class.html or\n"
          "         student/assignment.html — see the parity report.\n")
    return written


if __name__ == "__main__":
    build()
