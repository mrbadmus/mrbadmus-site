#!/usr/bin/env python3
"""build_student_port.py — the PORTED student pages: Design's markup and logic,
rendered by our own vanilla runtime with no React and no `support.js`.

    python3 build_student_port.py

Writes:

    mrbadmus_site/shared/student-ds.css        Design's six stylesheets, once
    mrbadmus_site/student/class-ported.html
    mrbadmus_site/student/assignment-ported.html
    student/*.html                             (mirror)

⛔ It writes no live page. `_REFUSED` in `build_student.py` is the same list and
the same reason: swapping a preview onto a live path is a separate, deliberate
change, gated on the whole Phase 5 checklist.

── Why this exists beside build_student.py rather than replacing it ──────

`build_student.py` photographs Design's rendered DOM. That was the right first
move — it made parity a property rather than an effort — and it has two limits
that no amount of care removes:

  * IT IS ONE STATE. 52 nodes Design renders below desktop are simply not in a
    desktop photograph, and no runtime shim can conjure them. Neither is the
    recall round, the expanded work row, the marker sheet or the end screen.
  * IT IS 558 KB, of which 306 KB is Chrome's longhand expansion of `all:
    unset` on 25 buttons and 223 KB is CSS inlined once per page.

This renders from Design's TEMPLATE instead, so every state exists, `all:unset`
stays two words, and the stylesheets are linked and cached. The two builds are
kept side by side until the ported pages pass the same parity gate the
snapshots do — at which point the snapshot build retires, with a note, rather
than being deleted.

── What is Design's ─────────────────────────────────────────────────────

The markup (Design's template, compiled by `student_template.py`, not retyped),
the behaviour (Design's logic class, extracted verbatim), the styling (Design's
own six stylesheets, concatenated in Design's own link order), and the brand
mark (captured from Design's render). What is ours is `shared/student-runtime.js`
— a 30-line base class and a renderer for three constructs.
"""

import html
import json
import os
import sys

REPO = os.path.dirname(os.path.abspath(__file__))
REF = os.path.join("docs", "ks3", "design-reference", "student")
DS = os.path.join(REF, "source", "_ds",
                  "mrbadmusai-design-system-53dad5ae-951a-44a1-95e1-394b9762b2d1")
SITE_OUT = os.path.join("mrbadmus_site", "student")
MIRROR_OUT = "student"
SHARED_OUT = os.path.join("mrbadmus_site", "shared")

TEMPLATES = "student_templates.json"
DS_CSS_NAME = "student-ds.css"
DS_CSS_URL = "/shared/" + DS_CSS_NAME
SERVED_FONTS = "/shared/fonts/"

_REFUSED = {"class.html", "assignment.html", "classes.html", "settings.html",
            "claim-confirm.html"}

PAGES = [
    dict(page="class view", out="class-ported.html",
         title="8r/Sc1 · My class · MrBadmusAI"),
    dict(page="assignment", out="assignment-ported.html",
         title="Assignment · 8r/Sc1 · MrBadmusAI"),
]

_BANNER = """<!--
  ══════════════════════════════════════════════════════════════════════════
  GENERATED — do not edit. `python3 build_student_port.py`
  ══════════════════════════════════════════════════════════════════════════

  %s, PORTED: Claude Design's own template and Design's own logic class,
  rendered by shared/student-runtime.js. No React and none of Design's
  `support.js` ships here — that was ruled on 20 Aug 2026.

  The markup is not retyped and neither is the behaviour. Both are extracted
  from docs/ks3/design-reference/student/ by student_template.py, so the only
  way this can differ from Design's file is if Design's file changed.

  STILL NOT THE LIVE PAGE: the content below is Design's authored example data.
  Wiring it to production is the next phase. The live pages are
  student/class.html and student/assignment.html and this build never writes
  them.
  ══════════════════════════════════════════════════════════════════════════
-->
"""


def _refuse(path):
    if os.path.basename(path) in _REFUSED:
        raise SystemExit(
            "build_student_port.py REFUSES to write %s — that is a LIVE "
            "student page." % path)


def ds_css():
    """Design's six stylesheets, in Design's own link order, as one file.

    ⚠️ NOT THE SITE'S OWN COPIES. `shared/tokens.css` and `shared/ks3.css` have
    both grown well past the versions in Design's bundle — measured, 31.8 KB
    against 24.5 KB and 548 KB against 42.5 KB — so linking the site's files
    would give the page a cascade Design never drew and never checked. Design's
    are vendored, which is also what makes the parity gate meaningful.

    Reconciling the two is real work and it is NOT this build's: it would
    change what KS3 lesson pages render as well, and it belongs with the
    already-open note about `--ks3-data` being in the engine's tokens and not
    in Design's.
    """
    order = ["tokens/src-styles-tokens.css", "tokens/shared-tokens.css",
             "tokens/shared-ks3.css", "fonts/fonts.css", "_ds_bundle.css",
             "styles.css"]
    out, sizes = [], []
    for rel in order:
        path = os.path.join(DS, rel)
        if not os.path.exists(path):
            raise SystemExit("build_student_port.py: missing %s" % path)
        css = open(path, encoding="utf-8").read()
        if rel.endswith("fonts.css"):
            # The faces point at `./` inside the bundle; the site self-hosts
            # every one of the seven at /shared/fonts/ and they are
            # byte-identical (verified by sha256 in build_student.py).
            css = css.replace("./", SERVED_FONTS)
        out.append("/* ── %s ── */\n%s" % (rel, css))
        sizes.append((rel, len(css)))
    return "\n\n".join(out), sizes


# ── every token the page references must resolve ──────────────────────────
#
# ⚑ THIS EXISTS BECAUSE ONE DID NOT, AND THE PAGE STILL LOOKED FINE. The ruled
# fix to the recall `CORRECT` label points it at `--ks3-ok-dark`, minted under
# MRB-252 in `shared/tokens.css`. Design's `_ds` bundle predates that mint and
# does not define it, so the label resolved to the INHERITED ink — measured,
# rgb(34,30,27) where #40DD84 was intended. No error, no warning; a green word
# quietly became a black one, and the token-contract gate went green because a
# black word is not a `--st-ok-room` violation either.
#
# An undefined custom property is the quietest failure CSS has. So the build
# collects every `var(--…)` the template and the logic reference, checks each
# against what the stylesheets actually define, and tops up the difference from
# the site's own `shared/tokens.css` — by NAME, read out of that file, never
# retyped. Anything still unresolved stops the build.
_VAR_RE = None


def referenced_tokens(tpl):
    """Every `--custom-property` the template or the logic asks for."""
    import re as _re
    blob = json.dumps(tpl["roots"]) + tpl["logic"] + json.dumps(tpl["imports"])
    return set(_re.findall(r"var\(\s*(--[a-zA-Z0-9-]+)", blob))


def defined_tokens(css, tpl=None):
    """Every custom property the page can resolve — from CSS AND from markup.

    ⚠️ THE MARKUP HALF IS NOT OPTIONAL. Design declares `--st-ok-room` inline on
    the design root (`--st-ink:var(--ks3-ink);--st-ok-room:#55B36A` in the
    root's own style attribute) rather than in a stylesheet, which is exactly
    what the handoff note says it did — "Declared on the design root, not in
    the token files". A scan that read only the stylesheets called it undefined
    and stopped the build on a token that resolves perfectly well.

    (The canonical copy now lives in `3d-studio/src/styles/tokens.css` under the
    20 Aug 2026 ruling. The inline declaration is byte-identical to it and is
    what actually paints, being on the element; the token-file entry is what
    makes Design's NEXT delivery inherit the value instead of re-declaring it.)
    """
    import re as _re
    found = set(_re.findall(r"(--[a-zA-Z0-9-]+)\s*:", css))
    if tpl:
        blob = json.dumps(tpl["roots"])
        found |= set(_re.findall(r"(--[a-zA-Z0-9-]+)\s*:", blob))
    return found


def top_up(css, wanted, tpls):
    """Define, from shared/tokens.css, any token the bundle is missing."""
    import re as _re
    have = defined_tokens(css)
    for t in tpls.values():
        have |= defined_tokens("", t)
    missing = sorted(wanted - have)
    if not missing:
        return css, []
    site = open(os.path.join("shared", "tokens.css"), encoding="utf-8").read()
    lines, still = [], []
    for name in missing:
        m = _re.search(r"%s\s*:\s*([^;]+);" % _re.escape(name), site)
        if m:
            lines.append("  %s: %s;" % (name, m.group(1).strip()))
        else:
            still.append(name)
    if still:
        raise SystemExit(
            "build_student_port.py: %d token(s) the page references are "
            "defined NOWHERE — not in Design's bundle and not in "
            "shared/tokens.css: %s.\n"
            "  An undefined custom property does not error; it falls back to "
            "the inherited value and the page looks almost right. Define them "
            "or stop referencing them." % (len(still), ", ".join(still)))
    block = ("\n\n/* ── minted since Design's bundle, read out of "
             "shared/tokens.css ──\n"
             "   Design's `_ds` drop predates MRB-252, which minted the two\n"
             "   body-size greens. Values are COPIED FROM the site's token\n"
             "   file at build time rather than retyped, so they cannot\n"
             "   drift from it. */\n:root,\n.rd[data-mode=\"ks3\"] {\n%s\n}\n"
             % "\n".join(lines))
    return css + block, missing


def page_html(spec, tpl):
    return (
        "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n"
        "<meta charset=\"utf-8\">\n"
        "<meta name=\"viewport\" content=\"width=device-width, "
        "initial-scale=1\">\n"
        "<title>%s</title>\n"
        "%s"
        "<link rel=\"stylesheet\" href=\"%s\">\n"
        "<style>body{margin:0;background:#FBF3E6}"
        "a{color:var(--ks3-accent-text);text-decoration:none}"
        "a:hover{color:var(--ks3-accent-hover)}"
        "button{font-family:inherit}</style>\n"
        "</head>\n<body>\n"
        "<div id=\"mrb-student\" style=\"background:var(--st-ground);"
        "min-height:100vh\"></div>\n"
        "<script src=\"/shared/student-runtime.js\"></script>\n"
        "<script>window.__MRB_TPL__=%s;</script>\n"
        "<script>\n%s\n</script>\n"
        "<script>\n%s\n</script>\n"
        "</body>\n</html>\n"
        % (html.escape(spec["title"]),
           _BANNER % spec["page"].capitalize(),
           DS_CSS_URL,
           json.dumps({"roots": tpl["roots"], "imports": tpl["imports"]},
                      separators=(",", ":")).replace("<", "\\u003c"),
           # Design's logic class, verbatim, with DCLogic bound to our base.
           "var DCLogic = window.MrBadmusStudentRuntime.MrbLogic;\n"
           "var StreamableLogic = DCLogic;\n" + tpl["logic"],
           "window.MrBadmusStudentRuntime.mount({\n"
           "  into: '#mrb-student',\n"
           "  template: window.__MRB_TPL__,\n"
           "  imports: window.__MRB_TPL__.imports,\n"
           "  Component: Component,\n"
           "  props: {}\n"
           "});")
    )


def write(path, body):
    _refuse(path)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(body)


def build():
    if not os.path.exists(TEMPLATES):
        raise SystemExit(
            "build_student_port.py: %s is missing. Run `python3 "
            "student_template.py` — the template and the logic are compiled "
            "out of Design's delivery, never typed." % TEMPLATES)
    tpls = json.load(open(TEMPLATES, encoding="utf-8"))

    print("\n🎓  build_student_port — Design's template and logic, "
          "on our runtime\n")

    css, sizes = ds_css()

    wanted = set()
    for spec in PAGES:
        t = tpls.get(spec["page"])
        if t:
            wanted |= referenced_tokens(t)
    css, topped = top_up(css, wanted, tpls)
    print("     %d token(s) referenced by the two pages; %d not in Design's "
          "bundle and topped up from shared/tokens.css%s"
          % (len(wanted), len(topped),
             (": " + ", ".join(topped)) if topped else ""))

    for out_dir in (SHARED_OUT, "shared"):
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, DS_CSS_NAME), "w",
                  encoding="utf-8") as fh:
            fh.write(css)
    print("     ✅ %-24s %7d bytes, %d sheet(s), linked and cached once"
          % (DS_CSS_NAME, len(css), len(sizes)))

    for spec in PAGES:
        tpl = tpls.get(spec["page"])
        if not tpl:
            raise SystemExit("build_student_port.py: %s has no entry for %r"
                             % (TEMPLATES, spec["page"]))
        body = page_html(spec, tpl)
        for out_dir in (SITE_OUT, MIRROR_OUT):
            write(os.path.join(out_dir, spec["out"]), body)
        print("     ✅ %-24s %7d bytes  (%d template node(s), "
              "%d chars of Design's logic)"
              % (spec["out"], len(body), tpl["nodes"], len(tpl["logic"])))

    print("\n     → %s/  and  %s/  (mirror)" % (SITE_OUT, MIRROR_OUT))
    print("\n     ⚠️  Design's example data still. Not a candidate to replace "
          "a live page.\n")


if __name__ == "__main__":
    sys.path.insert(0, REPO)
    build()
