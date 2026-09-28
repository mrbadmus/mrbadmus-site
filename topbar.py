"""The ONE pupil top bar (Stage B of the phone run, 28 Sep 2026).

    brand · title · [bell · avatar | Sign in] · theme

One row, at every width, on every pupil surface: KS3, the KS4 pilot, the
leaderboard and the hand-written pupil pages. The class page's own header
(Design's nodes 11-31) is the model; shared/topbar.css carries its
measurements and shared/topbar.js fills the right-hand "who" slot.

This module is the only place the bar's markup is written. It never draws the
brand itself — `brand.brand_lockup()` does — and it never hand-copies the
theme slot's attributes beyond the `compact` variant theme.js already has.

THE TITLE carries information the page does not already show:
  · a PARENT link ("‹ Cells and organisation") — the way back up, which on a
    lesson used to be a four-rung trail that wrapped over three rows; or
  · this page's own name, when nothing on the page says it (the class page's
    "My class"); or
  · nothing, when the page's own h1 already says it (the leaderboard, the
    classes list). A bar that repeats the h1 an inch above it is redundant
    text, and the bar is where a phone can least afford it.

Hand-written pages carry `<!--mrb:topbar …-->…<!--/mrb:topbar-->` and
`stamp_topbar()` rewrites the region on every build (called next to
`brand.stamp_brand` in generate_site_v5.py). Options inside the comment:
`title="…"`, `href=…`, `kind=…`, `tone=…`, `who=…`.
"""

import html as _html
import re

import brand

KINDS = ("ks3", "ks4", "leaderboard", "student")
TONES = ("chrome", "studio")
WHO = ("all", "avatar", "none")

THEME_SLOT_COMPACT = '<span class="mrb-theme-slot" data-mrb-theme="compact"></span>'


def _esc(s):
    return _html.escape(str(s), quote=True)


def title_html(title=None, href=None):
    """The title slot. `href` → a parent link; no href → this page's name."""
    if not title:
        return ""
    if href:
        return '<a class="mrb-topbar__title" href="%s">%s</a>' % (_esc(href), _esc(title))
    return '<span class="mrb-topbar__title" aria-current="page">%s</span>' % _esc(title)


def topbar(title=None, href=None, kind="ks3", host_class="", tone="chrome",
           who="all", brand_href="/index.html"):
    """The bar's static markup.

    kind        ks3 | ks4 | leaderboard | student — picks the token family
                (topbar.css) and whether a signed-out visitor is offered
                "Sign in" (not on `student`: the page's guard owns that).
    host_class  extra classes on <header>; KS3 and the KS4 pilot pass
                "ks3-nav" so their sticky/blur/rule and `--ks3-nav-h`
                (shared/ks3.js) keep working.
    tone        the bell's palette (student-bell.js TONES).
    who         all (bell + avatar) | avatar (the page mounts its own bell)
                | none (no who slot; the page draws its own).
    """
    if kind not in KINDS:
        raise ValueError("topbar: kind %r not in %r" % (kind, KINDS))
    if tone not in TONES:
        raise ValueError("topbar: tone %r not in %r" % (tone, TONES))
    if who not in WHO:
        raise ValueError("topbar: who %r not in %r" % (who, WHO))
    cls = "mrb-topbar" + (" " + host_class if host_class else "")
    slot = ("" if who == "none" else
            '<span class="mrb-topbar__who" data-mrb-topbar-who="%s"></span>' % who)
    return ('<header class="%s" data-mrb-topbar="%s" data-mrb-bell-tone="%s">'
            '<div class="mrb-topbar__rail">%s%s'
            '<div class="mrb-topbar__end" data-mrb-topbar-end>%s%s</div>'
            '</div></header>'
            % (cls, kind, tone, brand.brand_lockup(brand_href),
               title_html(title, href), slot, THEME_SLOT_COMPACT))


# ── Hand-written pages ────────────────────────────────────────────────────
TOPBAR_END = "<!--/mrb:topbar-->"
_TOPBAR_RE = re.compile(r"<!--mrb:topbar(?P<opts>(?:\s[^>]*?)?)-->.*?" + re.escape(TOPBAR_END), re.S)
_OPT_RE = re.compile(r'(\w+)=(?:"([^"]*)"|(\S+))')


def _opts(raw):
    return {m.group(1): (m.group(2) if m.group(2) is not None else m.group(3))
            for m in _OPT_RE.finditer(raw or "")}


def stamp_topbar(html):
    """Rewrite every marked top-bar region in a hand-written page.

    Returns the page unchanged when it has no markers.
    """
    def _bar(m):
        o = _opts(m.group("opts"))
        unknown = set(o) - {"title", "href", "kind", "tone", "who"}
        if unknown:
            raise SystemExit("topbar.stamp_topbar: unknown option(s) %s" % sorted(unknown))
        return ("<!--mrb:topbar" + m.group("opts") + "-->" +
                topbar(o.get("title"), o.get("href"), kind=o.get("kind", "student"),
                       tone=o.get("tone", "chrome"), who=o.get("who", "all")) +
                TOPBAR_END)
    return _TOPBAR_RE.sub(_bar, html)
