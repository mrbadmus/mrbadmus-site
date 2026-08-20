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

── ⚑ THE 390px GAP — HALVED IN PHASE 2, AND THE OTHER HALF NAMED ─────────

At DESKTOP the reproduction is exact. Measured against Design's own file at
1460px: 563 nodes against 563, 1460×2400 against 1460×2400, identical tag
census, identical text, identical resolved font, ground and ink, no horizontal
overflow. The assignment likewise, 177 against 177.

At 390px it was not, and phase 8a recorded the reason as Design's ten
JavaScript-computed switches being frozen at their desktop values. That was
right as far as it went and it was not the whole reason.

MEASURED, by driving Design's own file at 360, 390, 820 and 1460 and diffing
(`student_switches.py`), Design switches discretely in THREE ways:

  1. **By inline style** — 19 switched declarations across 16 elements. This is
     the mechanism Design's §6 table describes, and `student_switches.json`
     now carries every value at every band. `shared/student-breakpoints.js`
     applies it at runtime, so this half is FIXED.

     ⚑ AND THERE ARE MORE OF THEM THAN THE TABLE SAYS. Design's class-view note
     lists ten and states "there are no others". Two more are in the file: the
     docket's inner grid (`minmax(0,1fr)` → `repeat(auto-fit,minmax(148px,1fr))`)
     and its four fact rows (`row`/`baseline` → `column`/`flex-start`). Neither
     is interpolable, both are real, and a transcription of the ten would have
     shipped a docket stuck in four rigid columns on a phone.

  2. **By PRESENCE** — and a snapshot cannot carry DOM it does not contain.
     At 1460 the assignment renders a 320px `<aside>` rail with fifteen 52px
     marker cells (69 nodes) and no marker strip; below 1024 it renders the
     strip and the readout row (46 nodes) and no rail. The class view drops the
     `PROD` chip, the name, the Settings and Sign out links and the work rows'
     week column below 1024, and gains a mono meta line under each work-row
     title. Measured: 26 nodes desktop-only and 6 phone-only on the class view;
     69 and 46 on the assignment.

  3. **By TEXT** — the breadcrumb note reads `AUTUMN TERM · WEEK 04 / 12` at
     desktop and `WK 04 / 12` below.

NOT APPROXIMATED, deliberately, and the reason has changed. Phase 8a's reason
was that hand-writing media queries would drift from a logic class; that still
holds for (1) and is why (1) is applied from a MEASURED table rather than a
typed one. For (2) and (3) the reason is simpler: the nodes and the strings are
not here to switch. Reconstructing them would mean re-implementing Design's
renderer inside a shim, which is strictly more work and more fragile than
porting the logic properly — which is the next phase's actual instruction.

So this preview is now CORRECT IN LAYOUT at every band and still carries
desktop CHROME at phone widths. `student_parity.py` asserts both halves
separately, so neither can be forgotten and neither can be mistaken for the
other.
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
        page="class view",
    ),
    dict(
        out="assignment-preview.html",
        src="standalone/MrBadmusAI Assignment.html",
        title="Assignment · 8r/Sc1 · MrBadmusAI",
        note="the assignment",
        page="assignment",
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
    * LAYOUT IS RIGHT AT EVERY BAND, CHROME IS NOT. Design's discrete
      switches are computed in JavaScript from the measured root width. The
      19 that are inline-STYLE switches are measured out of Design's own file
      into student_switches.json and reapplied at runtime by
      /shared/student-breakpoints.js, so the grids, orders and columns are
      correct at 360, 390, 820 and 1460. The ones Design implements by
      PRESENCE (the assignment's rail vs its marker strip; the class view's
      PROD chip, name, Settings/Sign out and week column) and by TEXT (the
      breadcrumb note) cannot be: a snapshot has no DOM for the state it was
      not taken in. See build_student.py.

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


# ── the breakpoint shim, and the table it applies ─────────────────────────
#
# `student_switches.json` is MEASURED out of Design's own delivery by
# `student_switches.py` — driven at 360, 390, 820 and 1460, inline styles
# diffed. It is not transcribed from the handoff note, and it is not the same
# as the note: the note lists ten switches and says "there are no others", and
# the file has twelve.
#
# ⚠️ THE TABLE IS INLINED, NOT FETCHED. A `fetch()` for a JSON file would be a
# second request, on the critical path, that can fail — and the failure mode is
# a page that lays out at desktop on a phone with nothing on screen to say why.
# It is a few hundred bytes against a 550 KB page.
SWITCHES_JSON = "student_switches.json"
SHIM_SRC = os.path.join("shared", "student-breakpoints.js")
SHIM_URL = "/shared/student-breakpoints.js"


def switch_table(page_name):
    """The measured switch table for one page, as a JS literal."""
    import json
    if not os.path.exists(SWITCHES_JSON):
        raise SystemExit(
            "build_student.py: %s is missing. Run `python3 "
            "student_switches.py` — the breakpoint table is measured out of "
            "Design's delivery, not typed, and without it every generated page "
            "lays out at desktop on a phone." % SWITCHES_JSON)
    table = json.load(open(SWITCHES_JSON, encoding="utf-8"))
    if page_name not in table:
        raise SystemExit(
            "build_student.py: %s has no entry for %r. A page whose switches "
            "are not in the table is a page that silently keeps its desktop "
            "layout at every width." % (SWITCHES_JSON, page_name))
    blob = json.dumps(table[page_name], sort_keys=True, separators=(",", ":"))
    # `</script>` inside a JSON string would close the tag. It cannot occur in
    # a CSS value, but the escape costs nothing and the alternative is a page
    # that breaks in a way nobody would look for here.
    return blob.replace("<", "\\u003c")


def page_html(spec, data):
    return (
        "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n"
        "<meta charset=\"utf-8\">\n"
        "<meta name=\"viewport\" content=\"width=device-width, "
        "initial-scale=1\">\n"
        "<title>%s</title>\n"
        "%s"
        "<style>\n%s\n%s\n</style>\n"
        "<script>window.__MRB_SWITCHES__=%s;</script>\n"
        "<script src=\"%s\" defer></script>\n"
        "</head>\n<body style=\"margin:0;background:#FBF3E6\">\n"
        "<div style=\"%s\">\n%s\n</div>\n</body>\n</html>\n"
        % (html.escape(spec["title"]),
           _BANNER % spec["note"],
           data["faces"],
           data["styles"],
           switch_table(spec["page"]),
           SHIM_URL,
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
    # ⊕ MRB-271 — BUILD YOUR OWN TREE, NEVER SOMEBODY ELSE'S.
    #
    # Every path in this file is relative, and a relative path resolves against
    # the CURRENT DIRECTORY, not against this script. So
    # `python3 /elsewhere/build_student.py` run from inside a worktree imported
    # /elsewhere's modules and wrote the output into the WORKTREE — one tree's
    # source, another tree's deploy directory, and `generate_site_v5.build_site()`
    # opens by deleting most of what it finds there.
    #
    # With four worktrees live (see docs/ks3/worktrees.md) that stopped being
    # hypothetical. Anchoring to the script's own directory makes the invocation
    # path irrelevant: this file always builds the checkout it is part of.
    #
    # `__main__` only. Importing this module must NOT move the caller's cwd —
    # verify_ks3.py imports it and builds into its own scratch directories.
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    build()
