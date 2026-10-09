"""The site's ONE brand mark (Mide's ruling, 13 Sep 2026; one-mark run, 27 Sep 2026).

    ONE mark everywhere: a forward double chevron + the wordmark "MrBadmus".
    The front chevron solid, the back one faded. Identical on every page —
    pupil, public, staff, consumer — and in every email. The only variant is
    light-on-dark. Worksheets (PDF/DOCX) carry the chevron alone.

This module is the only place the mark is drawn in the build. Every generator
imports it; hand-written pages carry it between BRAND_START / BRAND_END and
`stamp_brand()` rewrites that region on every build. No page hand-copies the SVG.

The drawing is NOT redrawn here. `MARK_PATHS` is read at import time out of
Design's brand kit, `shared/brand/mrbadmus-chevron.svg` (a metadata-stripped
copy of the kit; the untouched originals and their md5s are in
docs/brand/source/ and docs/brand/ONE-MARK-REPORT.md). Change the kit and every
page follows on the next build.

Wordmark weight: Bricolage Grotesque 600, as the kit's lockup SVGs draw it and
as the kit's own Brand Mark sheet requires ("Wordmark in anything but
Bricolage Grotesque 600" is on its list of don'ts). The front-door MANIFEST's
"Bricolage 800" is prose the kit supersedes — see the report's decisions.
"""

import re
from pathlib import Path

_HERE = Path(__file__).resolve().parent
KIT_DIR = _HERE / "shared" / "brand"

BRAND_NAME = "MrBadmus"

# Kit colours (mrbadmus-lockup-light/-dark.svg, mrbadmus-app-icon-*.svg).
CHEVRON = "#E4572E"
INK = "#221E1B"      # wordmark on light grounds
CREAM = "#FBF3E6"    # wordmark on dark grounds

_KIT_CHEVRON = (KIT_DIR / "mrbadmus-chevron.svg").read_text(encoding="utf-8")
MARK_PATHS = "".join(re.findall(r"<path\b[^>]*>(?:</path>)?", _KIT_CHEVRON))
if MARK_PATHS.count("<path") != 2 or "stroke-opacity" not in MARK_PATHS:
    raise SystemExit("brand.py: shared/brand/mrbadmus-chevron.svg is not the kit's "
                     "two-chevron mark — refusing to build a page from it")

# `data-mrb-mark` is what brand_fingerprint.py and the brand_one_mark gate key on.
MARK_SVG = ('<svg class="mrb-brand__mark" data-mrb-mark viewBox="0 0 22 22" '
            'aria-hidden="true" focusable="false">' + MARK_PATHS + '</svg>')


def brand_lockup(href="/", on_dark=False, extra_class=""):
    """The header lockup: mark + "MrBadmus", as one link home.

    Home is "/" (⊕ B2C polish, 9 Oct 2026 — it was "/index.html", which put
    a second spelling of the home page in every lesson header).

    on_dark — the header is dark in BOTH themes (e.g. a permanently dark
    bar), so the wordmark is cream whatever the theme. Everywhere else the
    wordmark follows html[data-theme]: ink in light, cream in dark.
    """
    cls = "mrb-brand" + (" mrb-brand--on-dark" if on_dark else "")
    if extra_class:
        cls += " " + extra_class
    return (f'<a class="{cls}" href="{href}" aria-label="{BRAND_NAME} home">'
            f'{MARK_SVG}<span class="mrb-brand__word">{BRAND_NAME}</span></a>')


# Head tags: the kit's favicon and app icon, and the lockup's stylesheet.
# `v` is the caller's cache-bust stamp for shared assets (optional).
def brand_head(v=""):
    q = f"?v={v}" if v else ""
    return (f'<link rel="icon" type="image/svg+xml" href="/shared/brand/mrbadmus-favicon.svg{q}">'
            f'<link rel="apple-touch-icon" href="/shared/brand/mrbadmus-icon-light-512.png{q}">'
            f'<link rel="stylesheet" href="/shared/brand/brand.css{q}">')


BRAND_HEAD = brand_head()

# The shared-link image and site name every page advertises.
OG_SITE_NAME = f'<meta property="og:site_name" content="{BRAND_NAME}">'


def title(*parts):
    """`A | B | MrBadmus` — the one <title> suffix."""
    return " | ".join([p for p in parts if p] + [BRAND_NAME])


# ── Hand-written pages ────────────────────────────────────────────────────
# A hand-written page marks where its lockup and its head tags go; the build
# rewrites both regions from this module, so the page never holds a copy it
# could drift from.
BRAND_START = "<!--mrb:brand-->"
BRAND_END = "<!--/mrb:brand-->"
HEAD_START = "<!--mrb:brand-head-->"
HEAD_END = "<!--/mrb:brand-head-->"

# The start marker may carry options inside the comment:
#   <!--mrb:brand href=/parents/ on_dark-->…<!--/mrb:brand-->
_BRAND_RE = re.compile(r"<!--mrb:brand(?P<opts>(?:\s[^>]*?)?)-->.*?" + re.escape(BRAND_END), re.S)
_HEAD_RE = re.compile(re.escape(HEAD_START) + r".*?" + re.escape(HEAD_END), re.S)


def stamp_brand(html):
    """Rewrite every marked brand region in a hand-written page.

    Options: `href=<path>` (default /) and `on_dark`.
    Returns the page unchanged when it has no markers.
    """
    def _brand(m):
        opts = m.group("opts").split()
        href = next((o[5:] for o in opts if o.startswith("href=")), "/")
        on_dark = "on_dark" in opts
        return ("<!--mrb:brand" + m.group("opts") + "-->" +
                brand_lockup(href, on_dark=on_dark) + BRAND_END)

    html = _BRAND_RE.sub(_brand, html)
    html = _HEAD_RE.sub(HEAD_START + BRAND_HEAD + HEAD_END, html)
    return html


# ── Pages that draw their header in JavaScript ────────────────────────────
# The consumer shell and the compiled Design runtimes build their header at
# run time. They take the lockup from shared/brand/brand.js, which is WRITTEN
# from this module on every build (write_brand_js) — so the JS copy is this
# module's output, not a second drawing. The brand_one_mark gate fails the
# build if the file on disk differs from what this module would write.
BRAND_JS_PATH = KIT_DIR / "brand.js"


def brand_js():
    import json as _json
    return (
        "/* shared/brand/brand.js — GENERATED by brand.py on every build. Do not edit.\n"
        "   The one brand lockup (Mide's ruling, 13 Sep 2026) for pages that draw their\n"
        "   header in JavaScript. Same bytes as brand.brand_lockup() in the build. */\n"
        "(function () {\n"
        "  'use strict';\n"
        f"  var MARK = {_json.dumps(MARK_SVG)};\n"
        f"  var NAME = {_json.dumps(BRAND_NAME)};\n"
        "  function lockup(href, onDark) {\n"
        "    return '<a class=\"mrb-brand' + (onDark ? ' mrb-brand--on-dark' : '') + '\" href=\"' +\n"
        "      (href || '/') + '\" aria-label=\"' + NAME + ' home\">' + MARK +\n"
        "      '<span class=\"mrb-brand__word\">' + NAME + '</span></a>';\n"
        "  }\n"
        "  window.MrBadmusBrand = { NAME: NAME, MARK: MARK, lockup: lockup };\n"
        "})();\n"
    )


def write_brand_js():
    """Write shared/brand/brand.js; returns True when the file changed."""
    new = brand_js()
    old = BRAND_JS_PATH.read_text(encoding="utf-8") if BRAND_JS_PATH.exists() else None
    if old != new:
        BRAND_JS_PATH.write_text(new, encoding="utf-8")
        return True
    return False


if __name__ == "__main__":
    print("brand.js", "written" if write_brand_js() else "unchanged")
