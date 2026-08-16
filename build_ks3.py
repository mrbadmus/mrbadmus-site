"""build_ks3() — the KS3 generator. architecture.md §10.1 phase 1, §8.2, §8.4.

Run it:

    python3 build_ks3.py

**This generator is deliberately standalone and additive.** It writes only under
``mrbadmus_site/ks3/`` and ``ks3/``, and touches nothing else. It never calls
``build_site()``.

Why: ``generate_site_v5.build_site()`` starts with ``shutil.rmtree(output_dir)``
and ends by copying the whole tree over the repo root. Wiring KS3 into it would
mean every KS3 content change triggers a full rewrite of 300+ KS4 pages that
135+ students depend on — and would make §9's "zero KS4 pages changed" gate
impossible to demonstrate. Keeping them separate makes that gate provable by
construction. See the note at the bottom of this file for how to wire it in when
that trade-off is worth making.

Output taxonomy (§8.4). **No year appears in a LESSON path, ever (§4.5).**

    /ks3/index.html                                     KS3 landing — both routes in
    /ks3/<discipline>/index.html                        discipline hub
    /ks3/<discipline>/<unit-slug>/index.html            unit index
    /ks3/<discipline>/<unit-slug>/<lesson-slug>.html    the lesson    ← no year, ever

    the browse layer (§4.5.2, MRB-176 ruling 1) — index pages only:

    /ks3/year-<n>/index.html                            six half-term cards
    /ks3/year-<n>/<half-term>/index.html                subject cards for that half term
    /ks3/year-<n>/<half-term>/<discipline>/index.html   the lessons placed there

§4.5.2 splits §4.5's prohibition rather than relaxing it: year and half term are
the organising axis of the browse layer and remain absent from every lesson URL,
folder and byte. The browse layer is a pure projection of ``half_terms.py``'s
derived placement — reordering the sequence regenerates these index pages and
changes nothing else, which is the property §9's reorder proof already tests.
"""

import hashlib
import html
import json
import math
import os
import re
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import ks3_data
from ks3_data.structure import DISCIPLINES, DISCIPLINE_TITLES
from ks3_data.substatements import all_sub_ids, parent_of

# The browse layer's only data source. Slugs and display names live in
# half_terms.py rather than here on purpose: a second copy in the generator
# would be free to drift, and a drifted slug is a 404 that appears for exactly
# one half term of one year — the kind nobody finds by clicking around.
from ks3_data.half_terms import (
    HALF_TERMS,
    YEARS,
    half_term_name,
    half_term_slug,
    slots_by_year_half_term,
)

OUT_ROOT = "mrbadmus_site"
KS3_DIR = "ks3"

# KS4 pages have a pathway and a tier; KS3 has neither. A KS3 student following
# a `ks4_links` edge has not been placed in a tier and must not be forced to
# pick one, so the bridge lands on Combined Foundation — the least presumptuous
# entry point into GCSE. §4.7.
KS4_BRIDGE_PATHWAY = "combined"
KS4_BRIDGE_TIER = "foundation"

# ── Cache-bust stamps for shared assets ──────────────────────────────────
# KS3 pages link the same shared CSS as KS4 and must carry the same ?v=<hash>
# stamps, so a token change invalidates both trees at once. Without this, a
# device can keep serving an old cached tokens.css indefinitely — the exact bug
# generate_site_v5.py's cache-bust pass exists to prevent, and KS3 pages were
# shipping without it.
#
# **Hashed from the SOURCE tree (repo_root/shared/), never from output_dir.**
# generate_site_v5.py hashes its own output copy, and the two agree because the
# round-trip keeps source and deployed byte-identical. But build_ks3() is called
# with several different output_dir values — mrbadmus_site/ for the real build
# and a fresh tmp dir for §9's reorder and determinism proofs — and those tmp
# dirs never contain styles.css or nav.css at all. Hashing the output copy would
# make the stamp a function of which directory we happen to be writing to, and
# the reorder proof (which compares a mrbadmus_site/ build against a tmp build,
# byte for byte) would fail on a difference that has nothing to do with
# sequence. The source tree is the one input that is identical in every case.
#
# ks3.css is stamped too. KS4 does not know about it, but it is a shared
# stylesheet with exactly the same staleness problem, and fixing three of four
# would be an odd place to stop.
#
# ⚠️ §8.5's rationale is about CACHING, not about CSS, so it extends to JS
# unchanged — the tuple used to be named VERSIONED_CSS and ks3.js was linked
# with no stamp at all. That was survivable while ks3.js was a stub; it is not
# now that the file carries the prediction gate, the flip cards and the particle
# labs. A device holding an old cached copy would render a lesson whose labs
# never run and whose cards never flip, with no error and nothing to tell the
# student the page is broken. Any future shared asset a KS3 page links goes in
# this tuple — the name is deliberately no longer about stylesheets.
VERSIONED_ASSETS = ("tokens.css", "styles.css", "nav.css", "ks3.css", "ks3.js")


def asset_versions(repo_root="."):
    """name → 8-char content hash, matching generate_site_v5.py's scheme."""
    versions = {}
    for name in VERSIONED_ASSETS:
        path = os.path.join(repo_root, "shared", name)
        if os.path.exists(path):
            with open(path, "rb") as fh:
                versions[name] = hashlib.md5(fh.read()).hexdigest()[:8]
    return versions


def stamp_versions(page_html, versions):
    """Rewrite /shared/<asset> links to carry ?v=<hash>.

    Idempotent: the pattern matches whether or not a stale stamp is present, so
    re-stamping an already-stamped page moves it to the current hash rather than
    freezing it or doubling the query.

    The trailing `"` in the pattern is what keeps `ks3.css` from matching inside
    a longer name. It also means the match is agnostic about which attribute the
    path sits in, so `<script src="/shared/ks3.js" defer>` is caught by exactly
    the same rule as a `<link href=…>` — no separate JS pass needed.
    """
    if not versions:
        return page_html
    pattern = re.compile(
        r'/shared/(' + '|'.join(re.escape(n) for n in versions) +
        r')(?:\?v=[a-f0-9]+)?"')
    return pattern.sub(
        lambda m: '/shared/%s?v=%s"' % (m.group(1), versions[m.group(1)]),
        page_html)


SUBJECT_TOKEN = {
    "biology": "--biology",
    "chemistry": "--chemistry",
    "physics": "--physics",
}

# ── §4.6 reference-slot wording, in one place ────────────────────────────
#
# Both the unit index and the browse layer render reference slots, and the two
# must never end up saying different things about the same slot. The long
# comment in unit_index() is the reasoning; these are the words it produced.
#
# ⚠️ The pointer says WHERE, never WHEN. Do not add a year here — §4.5 forbids
# the sequence determining page text, and the §9 reorder proof asserts that
# applying a whole school's scheme changes zero page bytes.
REF_BADGE = '<span class="ks3-badge">from %s %s</span>'
REF_POINTER = ('<p class="ks3-ref-note">Taught in %s — <em>%s</em>. '
               'You\'ll meet the full lesson there.</p>')

# ⛔ FAMILY_BLURB REMOVED 2026-08-07 — MRB-181, architecture.md §8.10.
# It rendered §6's seven architecture families as a one-line gloss on every
# coming-soon page ("One idea explains a whole class of behaviour"). That is
# the platform describing its own compositional grammar to a twelve-year-old
# who came looking for a lesson and found a placeholder. The families are real
# and stay — in §6, in structure.py, and in what an authored lesson is shaped
# like. They are not page copy.


def e(s):
    return html.escape(str(s if s is not None else ""), quote=True)

# ── the drawn marks (SPEC.md §9.3) ───────────────────────────────────────
#
# ✓ ✕ → ARE DRAWN, NEVER TYPED. Design's own five latin woff2 subsets — the
# exact bytes now in shared/fonts/ — contain none of U+2713, U+2715 or U+2192;
# confirmed by reading the cmap of each file. Typed as characters all three
# drop to a system font mid-glyph, and inside a 27px Bricolage-800 badge that
# is a visible defect rather than a subtlety. R2 makes the marks load-bearing
# (colour is never the only signal on a state), so they cannot simply be
# dropped either. Inline SVG on `currentColor` satisfies both, and `.ks3-mark`
# in shared/ks3.css sizes it to 1em of whatever it sits in.
#
# MARK_TICK and MARK_CROSS are the canonical paths for the ladder's ANSWERED
# option states. shared/ks3.js draws them at runtime — a resting ladder badge
# carries its letter, not a mark — so no renderer emits them today. They live
# here so there is exactly one definition of each path in the system: if the
# ladder ever needs a mark at build time it takes it from here rather than
# growing a second copy that is free to drift.
MARK_ARROW = ('<svg class="ks3-mark ks3-mark-arrow" viewBox="0 0 24 24" '
              'aria-hidden="true"><path d="M4 12h15M13 6l6 6-6 6"/></svg>')
MARK_TICK = ('<svg class="ks3-mark" viewBox="0 0 24 24" aria-hidden="true">'
             '<path d="M4 13l5 5L20 7"/></svg>')
MARK_CROSS = ('<svg class="ks3-mark" viewBox="0 0 24 24" aria-hidden="true">'
              '<path d="M6 6l12 12M18 6L6 18"/></svg>')
# ▾ U+25BE is absent from the same five subsets, for the same reason — it is a
# geometric shape, not a letter. Typed into the picker's button it would drop to
# a system font mid-label, inside a 19px/700 Bricolage button, which is exactly
# the defect `.ks3-mark` exists to prevent. Drawn instead. MRB-212.
MARK_CARET = ('<svg class="ks3-mark ks3-mark-caret" viewBox="0 0 24 24" '
              'aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>')

# Escaped TEXT, with the three marks DRAWN rather than typed.
#
# ⚠️ Text nodes only — never an attribute value. MARK_ARROW carries double
# quotes, so substituting inside `data-feedback="…"` or an `aria-label` would
# terminate the attribute and emit broken markup. `e()` stays the attribute
# escaper for exactly that reason, and the split is the whole safety property:
# if you cannot tell whether a slot is text or an attribute, it is an attribute.
#
# This matters because authored copy uses the arrow as chemistry notation —
# "Solid → liquid", "warmer → faster", "smaller box → twice as many wall hits".
# The content is not touched; the same character is simply rendered with a glyph
# the fonts actually have.
MARKS = (("\u2192", MARK_ARROW), ("\u2713", MARK_TICK), ("\u2715", MARK_CROSS))


def t(s):
    out = e(s)
    for ch, mark in MARKS:
        if ch in out:
            out = out.replace(ch, mark)
    return out


# ── inline emphasis (⊕ B1 round two) ─────────────────────────────────────
#
# Design's authored strings carry `<em>` and `<strong>` — the key fact, the key
# note, the MRS GREN explainer, a scorecard note and the hook's reveal all use
# one or the other, and §4.8.1 B's own field note sanctions `<em>` in a key
# fact. `t()` is `html.escape`, so every one of those was rendering as a
# LITERAL `<em>` on the page: Design's emphasis silently turned into visible
# tag soup. Found by the b1-01 authoring run before it could ship.
#
# The fix is an allow-list and deliberately a small one. Escape everything, then
# put back exactly two tags. Nothing else is permitted — not `<a>`, not `<span
# class>`, not a bare `<b>` — because the authored strings are the surface a
# lesson's science lands on, and a general HTML pass-through there is an
# injection hole and a styling backdoor at the same time. Two tags carry every
# case in the delivery, and a third needs a ruling rather than a regex.
_RICH_OK = ("em", "strong")
_RICH_RE = re.compile(r"&lt;(/?)(%s)&gt;" % "|".join(_RICH_OK))


def rich(s):
    """`t()` plus `<em>` and `<strong>`, and nothing else."""
    return _RICH_RE.sub(r"<\1\2>", t(s))


# ⚠️ ← (U+2190) is absent from the same subsets, and the browse layer used to
# open three back-links with one. Design's system has no left-arrow mark to
# draw instead, so those links now say "Back to …" in words — which is what R2
# would have asked for anyway.

OPTION_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def option_letter(i):
    """A B C D … — the resting content of an option's mark badge."""
    return OPTION_LETTERS[i] if i < len(OPTION_LETTERS) else str(i + 1)


def family_label(family):
    """`MODEL` → `Model`.

    §6's seven families are SHOUTED in the data and title-case on the page.
    `.ks3-eyebrow` already applies `text-transform: uppercase`, so this is not
    a visual change — it is about the bytes. A literal run of capitals is read
    out letter by letter by some screen readers, and it is the one place the
    architecture's internal vocabulary would have leaked into a student's ear.
    """
    return str(family or "").title()


# ── shell ────────────────────────────────────────────────────────────────

# MRB-197 (ruled by Mide): KS3 takes Claude Design's mark — one bold #E4572E
# chevron and the Bricolage wordmark, exactly as drawn in the frozen
# reference's header. The KS4 gold-to-rust two-chevron mark stays mandatory on
# every other external page; this is the same key-stage split already ruled
# for the palette under MRB-183. `.ks3-brand` is styled in shared/ks3.css.
#
# ⊕ MRB-208 rule 1, amended 12 Aug 2026: the chevron sits INSIDE a 34px
# accent-filled rounded tile and the stroke goes cream, rather than a bare 30px
# accent chevron on the page ground. Measured on all six approved B1 pages:
# tile 34×34, radius 10px, `--ks3-accent` ground, chevron stroke `#FBF3E6`
# (= `--ks3-ground`) at width 4.6, wordmark Bricolage 22px/800, gap 10px.
# MRB-197, ruled by Mide: one bold #E4572E chevron plus the Bricolage 800
# wordmark. ⊖ Design's B1 delivery redrew this as a cream chevron inside a 34px
# accent tile; NOT adopted on the 15 Aug replay, because NAV_BRAND is one mark
# for all 294 KS3 pages and taking the tile would restyle the browse layer Mide
# has just approved. Parked for Mide — see the ledger entry of 15 Aug 2026.
NAV_BRAND = (
    '<a class="ks3-brand" href="/index.html">'
    '<svg width="30" height="30" viewBox="0 0 24 24" aria-hidden="true">'
    '<path d="M4 16L12 7l8 9" fill="none" stroke="#E4572E" stroke-width="4.6" '
    'stroke-linecap="round" stroke-linejoin="round"/>'
    '</svg>MrBadmusAI</a>'
)


# SPEC.md §2 requires the KS3 fonts preloaded. Two of the five, matching the
# pattern the KS4 pages already use for Fraunces + Plus Jakarta: the display and
# body romans are needed for first paint on every page, whereas the italic and
# the two mono weights are used sparsely (captions, breadcrumbs, live numbers)
# and preloading all five would spend the connection budget to no benefit. With
# `font-display: swap` the unpreloaded three swap in a beat later, which is the
# right trade for text that is not the first thing read.
#
# `crossorigin` is required even same-origin: a font fetched by a preload
# without it is fetched a SECOND time by the CSS, silently doubling the bytes.
FONT_PRELOADS = "".join(
    '<link rel="preload" href="/shared/fonts/%s" as="font" '
    'type="font/woff2" crossorigin/>\n' % name
    for name in ("bricolage-grotesque-var-latin.woff2",
                 "instrument-sans-var-latin.woff2"))


def crumbs(parts):
    """KS3 › Chemistry › Particles and their behaviour  (§8.5).

    The separate breadcrumb ROW, mono 14px inside `<main>`. Still correct on
    unit indices, discipline hubs and the browse layer. ⊕ MRB-208 amendment 1
    removed it from LESSON pages only, where the trail moved into the header —
    see `header_trail()`.
    """
    out = []
    for i, (label, href) in enumerate(parts):
        if href and i < len(parts) - 1:
            out.append('<a href="%s">%s</a>' % (e(href), t(label)))
        else:
            out.append('<span aria-current="page">%s</span>' % t(label))
    return ('<nav class="ks3-crumbs" aria-label="Breadcrumb">%s</nav>'
            % '<span class="ks3-crumb-sep" aria-hidden="true">›</span>'.join(out))


def header_trail(parts):
    """The lesson trail, inline in the header bar. ⊕ MRB-208 rule 1.

    Ruled by Mide during B1 round one, and re-affirmed on 13 Aug 2026 when both
    treatments were found alive in the tree:

        "Amendment 1 on this ticket ruled it on 12 August: the header carries
         the trail inline, the separate breadcrumb row is gone, the KS3 pill
         stays. Design's treatment survives; `.ks3-crumbs` is removed from the
         lesson pages. Re-opening a settled ruling because both artefacts still
         exist in the repo is how a decision quietly becomes a discussion
         again."

    An `<ol>` rather than the row's flat spans, because it is an ordered path
    and a screen reader should say so. Separators are their own `<li>`s and are
    `aria-hidden`, so the list reads as four items and not seven. Measured on
    Design's pages at body 17px/600, gap 9px, wrapping to its own row at 820
    and over three rows at 390 — which is what grows `nav.ks3-nav` from 63.19px
    to 94.78px to 176.06px, and the sticky rail sits directly under it.
    """
    out = []
    for i, (label, href) in enumerate(parts):
        last = i == len(parts) - 1
        if i:
            out.append('<li class="ks3-trail-sep" aria-hidden="true">›</li>')
        if href and not last:
            out.append('<li><a href="%s">%s</a></li>' % (e(href), t(label)))
        else:
            out.append('<li><span aria-current="page">%s</span></li>' % t(label))
    return ('<ol class="ks3-trail" aria-label="Breadcrumb">%s</ol>'
            % "".join(out))


def shell(title, body, crumb_html="", discipline=None, description="",
          footer_links=(), main_class="", lesson_slug=None,
          trail_html="", rail_html=""):
    """KS3 page shell. `class="rd"` + `data-mode="ks3"` per §8.5.

    **The breadcrumbs live in the HEADER, not in `<main>` (MRB-208).** Design's
    browse layer puts them on the header rail, one divider after the brand, and
    that is the only place they appear: a page that repeated them as a row
    inside `<main>` would announce the same trail twice to a screen reader and
    push the h1 below the fold on a phone for no gain.

    **Two treatments of that one landmark, never two landmarks.** An authored
    lesson passes `trail_html` — MRB-208 rule 1's `<ol class="ks3-trail">`, body
    17px/600, an ordered path a screen reader announces as one. Every other page
    type passes `crumb_html` — `crumbs()`'s mono 14px `<nav class="ks3-crumbs">`,
    which survives on unit indices, discipline hubs, the year and half-term
    screens and the browse layer. They occupy the same header slot after the
    same divider, so a page has exactly one trail whichever it is.

    `footer_links` is a list of `(label, href)` for the footer's right-hand
    quick links. It is per-page rather than derived here because only the caller
    knows which year and which discipline it is inside; `landing()` passes
    nothing but "All of KS3", the browse screens add their own way back up.

    `lesson_slug` stamps `data-ks3-lesson` on `<body>`. MRB-212's visit logger
    reads it to know which lesson a page IS. It cannot use the existing
    `data-lesson` attribute for that: that one lives on the ladder element,
    which only an AUTHORED lesson with a ladder has, so every coming-soon page
    and any authored page without a ladder would be invisible to the log.

    `rail_html` is MRB-208 rule 2's progress rail. It sits BETWEEN the header
    and `<main>` — outside the main landmark because it is a position readout
    for the page, not part of its content, and it is sticky under a sticky
    header, which only works if the two are siblings.
    """
    accent = ("--subject: var(%s);" % SUBJECT_TOKEN[discipline]) if discipline else ""

    # No brand→trail divider when there is nothing to divide.
    header_nav = trail_html or crumb_html
    crumb_rail = ('<span class="ks3-nav-divider" aria-hidden="true"></span>\n  %s'
                  % header_nav) if header_nav.strip() else ""

    # "All of KS3" is on every KS3 page, always — the one link that is true
    # from anywhere in the tree. Callers supply only the extra rungs they
    # happen to sit under.
    links = "".join(
        '<a href="%s">%s</a>' % (e(href), t(label))
        for label, href in (("All of KS3", "/ks3/index.html"),) + tuple(footer_links))
    return """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>%(title)s · MrBadmusAI KS3</title>
<meta name="description" content="%(desc)s"/>
%(preload)s<link rel="stylesheet" href="/shared/tokens.css"/>
<link rel="stylesheet" href="/shared/styles.css"/>
<link rel="stylesheet" href="/shared/nav.css"/>
<link rel="stylesheet" href="/shared/ks3.css"/>
</head>
<body class="rd" data-mode="ks3"%(lesson)s%(style)s>
<header class="ks3-nav">
  <div class="ks3-nav-rail">%(brand)s
  %(crumbs)s
  <span class="ks3-nav-spacer"></span>
  <a class="ks3-pill" href="/ks3/index.html">KS3</a>
  </div>
</header>
%(rail)s<main class="ks3-main%(mainclass)s">
%(body)s
</main>
<footer class="ks3-footer">
  <div class="ks3-footer-rail">
    <p class="ks3-footer-title">MrBadmusAI · Key Stage 3 Science</p>
    <div class="ks3-footer-links">%(links)s</div>
  </div>
</footer>
<script src="/shared/ks3.js" defer></script>
</body>
</html>
""" % {
        "title": e(title),
        "desc": e(description or title),
        "style": (' style="%s"' % accent) if accent else "",
        "lesson": (' data-ks3-lesson="%s"' % e(lesson_slug)) if lesson_slug else "",
        "brand": NAV_BRAND,
        "crumbs": crumb_rail,
        "rail": rail_html,
        "mainclass": (" %s" % main_class) if main_class else "",
        "links": links,
        "body": body,
        "preload": FONT_PRELOADS,
    }


# ── segment renderers (§5.1.1 vocabulary) ────────────────────────────────
#
# Every class emitted below has a rule in shared/ks3.css, which is the class
# contract for this generator. A renderer that needs a look the stylesheet does
# not have reaches for an existing class; it does not invent one, because an
# invented class is a silent no-op that looks like styling.

def r_hook(lesson, block=None):
    """Block 1 — ink dark. A phenomenon that ends in a commitment (R16).

    ⚠️ `block` is not decoration. Until 14 Aug 2026 the dispatch entry was
    `lambda l, b: r_hook(l)` — it threw the block away, and with it the
    `anchor`. So `#s-hook` was emitted on NO page in the key stage, and the
    same was true of `#s-ladder`. Measured on all six B1 lessons: the rail's
    FIRST and LAST stops both pointed at ids that do not exist, so their links
    went nowhere and `doneByDom(null)` was false forever — a lesson with six
    stops could reach at most four, and no student could ever complete a rail.
    Neither the inventory nor any ticket had this; it was found by asking
    whether every rail anchor resolves, which is now gated.
    """
    p = lesson.get("phenomenon") or {}

    head = ('<p class="ks3-eyebrow">%s</p>'
            '<h2 class="ks3-hook-h">%s</h2>'
            '<p class="ks3-hook-prompt">%s</p>'
            % (t(p.get("eyebrow") or "Start here"), t(p.get("title", "")),
               rich(p.get("prompt", ""))))

    # ⊕ The media column, and the Motion control that belongs to it. Both were
    # dropped on the floor: `phenomenon.art`, `.figures` and `.tiles` were read
    # by nothing, which is why Mide opened b1-01 and found "the hook missing
    # its candle artwork and Motion toggle entirely". The toggle is not
    # decoration either — Law 9 says motion is meaning, and R7 requires a way
    # to stop it that is not buried in an OS setting.
    media = _hook_media(lesson, p)
    if media:
        body = ('<div class="ks3-hook-grid">'
                '<div class="ks3-hook-lede">%s</div>%s'
                '<div class="ks3-hook-motion">'
                '<span class="ks3-hook-motion-label">Motion</span>'
                '<button type="button" class="ks3-motion-btn" data-motion-set="on"'
                ' aria-pressed="true">On</button>'
                '<button type="button" class="ks3-motion-btn" data-motion-set="off"'
                ' aria-pressed="false">Off</button>'
                '</div></div>' % (head, media))
    else:
        body = head

    # ⊕ The commitment. R16 and Law 1: the hook ends in a decision, and the
    # reveal is gated behind it. `options` and `reveal` are authored on ALL SIX
    # lessons and were read on none of them, so every hook stopped at the
    # question and no student could ever answer it. `#s-hook` is the first stop
    # on all six rails and could therefore never tick.
    commit = ""
    if p.get("commit") or p.get("options") or p.get("reveal"):
        bits = []
        if p.get("commit"):
            bits.append('<p class="ks3-commit">%s</p>' % t(p["commit"]))
        if p.get("options"):
            bits.append(r_activity_options(p["options"]))
        if p.get("reveal"):
            bits.append('<div class="ks3-reveal" hidden data-reveal><p>%s</p>'
                        '</div>' % rich(p["reveal"]))
        commit = '<div class="ks3-hook-commit">%s</div>' % "".join(bits)

    return ('<section class="ks3-block ks3-dark ks3-hook"%s data-activity="hook">'
            '%s%s</section>' % (_id_attr(block or {}), body, commit))


# ── the hook's media column ──────────────────────────────────────────────
#
# Three of the six lessons draw something beside the lede, under three
# different authored keys, because six agents authored six lessons. They are
# genuinely three different components rather than one with a discriminator —
# `phenomenon.kind` ("demo", "data", "compare", "narrative") looks like it
# should select between them and DOES NOT: Design draws nothing that varies by
# it, and b1-05 is `demo` with no art at all. Dispatching on which key is
# present is what the data actually supports; `kind` stays unread and is
# reported rather than pressed into service.

def _hook_media(lesson, p):
    if p.get("art"):
        return _css_art(lesson, p["art"])
    return ""


def _css_art(lesson, fig_id):
    """A drawing built from tokens and CSS, not an asset.

    `phenomenon.art` names a `figures[]` entry whose `kind` is `css-art`; its
    `art` field names the drawing. Kept as a closed set with a raise on an
    unknown name, for the same reason `r_sim` refuses an unknown control: a
    figure that silently renders nothing is a hole the page hides.
    """
    fig = next((f for f in (lesson.get("figures") or [])
                if f.get("id") == fig_id), None)
    if fig is None:
        raise ValueError(
            "phenomenon.art names figure %r, which is not in figures[]." % fig_id)
    art = fig.get("art")
    if art not in CSS_ART:
        raise ValueError(
            "figure %r declares css-art %r, which the generator cannot draw. "
            "Known: %s." % (fig_id, art, ", ".join(sorted(CSS_ART))))
    # The caption is the accessible description. The drawing itself is
    # `aria-hidden` — a screen reader gets the sentence, not a pile of spans.
    return ('<div class="ks3-hook-art ks3-art-%s" role="img" aria-label="%s">'
            '%s</div>' % (e(art), e(fig.get("caption", "")), CSS_ART[art]))


# A burning candle. Every colour that is not a token is Design's own literal
# from the approved page: the night ground `#17130F`, the soot `#6E6259`, the
# wick `#2A211B` and the three wax stops. The flame gradient IS tokens —
# alert → accent → accent-text, top to bottom.
_CANDLE = (
    '<span class="ks3-soot" data-anim="soot"></span>'
    '<span class="ks3-soot" data-anim="soot"></span>'
    '<span class="ks3-soot" data-anim="soot"></span>'
    '<div class="ks3-candle">'
    '<span class="ks3-flame ks3-flame-outer" data-anim="flame"></span>'
    '<span class="ks3-flame ks3-flame-inner" data-anim="flame"></span>'
    '<span class="ks3-wick"></span>'
    '<span class="ks3-wax"></span>'
    '</div>')

CSS_ART = {"candle-flame": _CANDLE}


def r_explainer(lesson, block):
    """Prose, carrying no card at all.

    ⚠️ Must be a DIRECT child of `.ks3-lesson` — `.ks3-lesson > .ks3-explainer`
    is the selector that caps prose at the 46rem reading measure (R11).
    Wrapping the core blocks in anything silently widens every explainer on
    every lesson to the 60rem break-out, which is the exact measure R11 exists
    to prevent, and it would look almost right.
    """
    # ⊕ `pills` — the initial row (MRS GREN and its successors). Decorative
    # reference, NOT a control: no aria-pressed, no cursor, no hover. The
    # initial is duplicated in the label's first letter, so a screen reader
    # reading only the label loses nothing, and the badge is aria-hidden.
    pills = "".join(
        '<li><span class="ks3-pill-badge" aria-hidden="true">%s</span>'
        '<span class="ks3-pill-label">%s</span></li>'
        % (t(p.get("initial", "")), t(p.get("label", "")))
        for p in block.get("pills") or [])
    return ('<section class="ks3-block ks3-explainer"%s><p>%s</p>%s</section>'
            % (_id_attr(block), rich(block.get("text", "")),
               ('<ul class="ks3-pills">%s</ul>' % pills) if pills else ""))


def r_figure(lesson, block):
    fig = next((f for f in lesson.get("figures", [])
                if f["id"] == block.get("ref")), None)
    if not fig:
        return ""
    status = fig.get("status", "needed")
    if status == "needed":
        # Honest placeholder — a declared, tracked sourcing task (§4.10),
        # never a broken image.
        return ("""<figure class="ks3-figure ks3-figure-pending">
  <div class="ks3-figure-slot" role="img" aria-label="%s">
    <span class="ks3-figure-tag">Diagram coming soon</span>
  </div>
  <figcaption>%s</figcaption>
</figure>""" % (e(fig["caption"]), t(fig["caption"])))
    return ('<figure class="ks3-figure"><img src="/ks3/figures/%s.svg" alt="%s"/>'
            '<figcaption>%s</figcaption></figure>'
            % (e(fig["id"]), e(fig["caption"]), t(fig["caption"])))


def r_keyword(lesson, block):
    """Vocabulary as flip cards (R4).

    R4: the dog-ear is the only affordance, and the block must ASK for the
    declaration in words — that ask is the whole mechanism, because nothing
    records whether the student really said the meaning first. The lead
    sentence reuses `.ks3-meta`, which is already the right size and colour,
    rather than growing a class of its own.

    The back is emitted `hidden` so the definition is not on screen in the
    window between first paint and ks3.js running. A card that shows its back
    for 200ms has given the game away, and on a slow phone that window is not
    200ms. ks3.js owns `aria-expanded` and `.is-flipped` from then on.
    """
    vocab = {v["term"]: v for v in lesson.get("vocabulary", [])}
    items = []
    for term in block.get("terms", []):
        v = vocab.get(term)
        if not v:
            continue
        # No note, no element. An empty .ks3-card-note still costs an 8px flex
        # gap, so the card would sit taller than its neighbours for nothing.
        note = ('<span class="ks3-card-note">%s</span>' % t(v["note"])
                if v.get("note") else "")
        items.append(
            '<li><button type="button" class="ks3-card-btn" aria-expanded="false">'
            '<span class="ks3-card-front">%s</span>'
            '<span class="ks3-card-back" hidden>'
            '<span class="ks3-card-def">%s</span>%s</span>'
            '<span class="ks3-card-hint">Say it, then tap %s</span>'
            '</button></li>'
            % (t(v["term"]), t(v["definition"]), note, MARK_ARROW))
    if not items:
        return ""
    # The lead line is R4's declaration ask, in words: a card grid discharges
    # Law 4 through a DECLARED prediction (§5.1.2a), and a declared prediction
    # nobody asked for does not happen. verify_ks3.py fails the build if a card
    # grid ships without it, so this sentence is a gate, not decoration.
    return ('<section class="ks3-block ks3-keywords">'
            '<h2>Words to know</h2>'
            '<p class="ks3-keywords-lead">Say the meaning out loud before you '
            'tap the card.</p>'
            '<ul class="ks3-cards" data-cards role="list">%s</ul>'
            '</section>' % "".join(items))


def _activity(lesson, act_id):
    return next((a for a in lesson.get("activities", []) if a["id"] == act_id), None)


def _misconception_quote(lesson, target_id):
    """The wrong idea in a student's own words, from the register.

    A misconception block confronts a specific entry in the lesson's
    `misconceptions` list, named by the activity's `targets`. Printing the
    statement is the first beat of the three-beat format the content standards
    require: say the mistake out loud, then why it is wrong, then the right
    version. If nothing matches, the block renders its prompt alone rather
    than an empty quote.
    """
    if not target_id:
        return ""
    for m in lesson.get("misconceptions") or []:
        if m.get("id") == target_id:
            return m.get("statement") or ""
    return ""


# ── activity-level interactions (NOT new §5.1.1 block types) ─────────────
#
# The block vocabulary is closed at ten. Flip cards and particle labs are
# authored as ACTIVITY keys (`cards`, `sim`) precisely so they can appear
# inside an existing check / practical / misconception block without widening
# that vocabulary — an activity is already the unit that owns a prompt, options
# and a reveal, and these are two more ways of answering the same prompt.

def r_cards(cards):
    """Click-to-reveal cards on an activity.  Contract: ks3.js `wireCards`.

    The same shell the keyword block uses, so there is one card in the system
    rather than two that drift. An activity card's back is a single answer, so
    it takes `.ks3-card-def` and never a note.
    """
    items = []
    for c in cards:
        items.append(
            '<li><button type="button" class="ks3-card-btn" aria-expanded="false">'
            '<span class="ks3-card-front">%s</span>'
            '<span class="ks3-card-back" hidden>'
            '<span class="ks3-card-def">%s</span></span>'
            '<span class="ks3-card-hint">Say it, then tap %s</span>'
            '</button></li>'
            % (t(c.get("front", "")), t(c.get("back", "")), MARK_ARROW))
    if not items:
        return ""
    return ('<ul class="ks3-cards" data-cards role="list">%s</ul>'
            % "".join(items))


# A canvas is a blank rectangle to a screen reader, so aria-label is the ONLY
# description of a lab that a non-sighted student gets. "Particle simulation"
# would be technically an alt text and practically nothing, so the label
# narrates what the animation actually does — one description per sim kind,
# because the three sims genuinely differ in what there is to see.
#
# The authored caption is appended, which makes each of the seven labels
# distinct and self-contained. It repeats the visible <p class="ks3-sim-caption">
# for a screen-reader user; that is a deliberate trade — an aria-label is read
# out of context (element lists, rotor) where the neighbouring caption isn't
# there to supply it.
# The controls a lab may declare. Mirrors CONTROL_LABELS in shared/ks3.js —
# the two must agree, and r_sim() fails the build if a lesson names anything
# else. See the comment in r_sim for why this is validated rather than passed
# through.
SIM_CONTROLS = ("temperature", "volume", "particles", "medium",
                # MRB-198 — the four names B1's two instruments declare.
                "specimen", "magnification", "focus", "part",
                # MRB-211 (G10, G11) — B1-06's bench. `centre` pans the field
                # to a named organism; `motion` is the student's own stillness
                # switch. Both are segmented, neither is a range.
                "centre", "motion")

# MRB-211 — the total magnifications this instrument HAS, i.e. EYEPIECE ×
# OBJECTIVES in shared/ks3.js. Kept here so `resolve_notes` can be checked
# against the lens turret that exists: a note keyed 200 would be authored,
# validated, serialised and never once shown, which is the silent-defect class
# every other gate in this function exists to close. If the turret is ever
# re-ruled, these two lists move together.
MICRO_TOTALS = (40, 100, 400)

# MRB-198 — the microscope's slide models. Authored `specimens[]` entries are
# free student-facing text ("onion skin — coverslip dropped flat"), but each
# must classify to a slide model shared/ks3.js actually draws, else the select
# offers a slide the canvas renders as an empty circle and nothing says so —
# the same silent-defect class the SIM_CONTROLS gate exists for. The keyword
# rule here is THE SAME ONE `specimenKind()` applies in shared/ks3.js; the
# two must agree, and the parity gate's sim audit checks the rendered result.
def _specimen_kind(name):
    n = str(name).lower()
    if "pond" in n:
        return "pond"
    if "cheek" in n:
        return "cheek"
    if "onion" in n:
        return "bubbles" if ("dropped" in n or "bubble" in n) else "onion"
    return None

SIM_ARIA = {
    "particle-states":
        "Animation: a box of particles that responds to a temperature slider. "
        "Cold, the particles sit touching in a regular pattern and vibrate on "
        "the spot. Warmer, they are still touching but jumbled, sliding past "
        "each other. Hotter still, they are far apart and moving freely in "
        "every direction. The readout below the animation says the same thing "
        "in words.",
    "gas-pressure":
        "Animation: gas particles bouncing inside a box with a movable wall. "
        "Every time a particle strikes a wall it counts as one push, and "
        "squeezing the box or heating the gas makes those hits more frequent. "
        "The readout below the animation gives the wall hits per second in "
        "words.",
    "diffusion":
        "Animation: two groups of particles, orange starting on the left and "
        "blue starting on the right, each wandering on its own random path. "
        "Orange particles cross to the right while blue ones cross to the "
        "left, both at once, until the two groups are mixed. The readout "
        "below the animation counts the crossings in each direction in words.",
    # MRB-198 — both authored by Claude Design in biology_b1_cells.py's
    # instrument spec, used verbatim. They narrate the MECHANISM, not the
    # picture, because this label is the only description a non-sighted
    # student gets.
    "microscope":
        "Animation: the view down a light microscope. Turning the "
        "magnification up makes everything larger but shows a smaller circle "
        "of the slide, and the image blurs until the focus is corrected. "
        "Turning the focus moves down through the thickness of the specimen, "
        "so different layers come sharp in turn. The readout below the "
        "animation gives the total magnification and the width of the field "
        "of view in words.",
    "system-parts":
        "Animation: a set of labelled parts that work together. Switching "
        "one part off makes every part that depends on it stop in turn, "
        "spreading outwards from the part that was switched off. The readout "
        "below the animation lists what still works and what has stopped, "
        "in words.",
}

# MRB-211 — the organism shapes shared/ks3.js `drawOrganism` actually draws.
# Same gate as `_specimen_kind`: a mount that declares a `tardigrade` would
# render as nothing at all, in silence.
MICRO_ORGANISMS = ("amoeba", "paramecium", "euglena")


def _num(v):
    return isinstance(v, (int, float)) and not isinstance(v, bool)


def _microscope_payload(sim, act_id):
    """The microscope's data attributes, validated (⊕ G9, G10, G11).

    THREE attributes, and the split is by lifetime, not by taste:

      `data-specimens` — the classifier strings, one per slide, exactly as
        MRB-198 shipped them. Every microscope emits it and `specimenKind()`
        reads it, so the B1-02 instrument and the parity sim audit are
        untouched by anything below.
      `data-mounts`    — G9. The rich per-slide payload: the button caption,
        the authored organisms, and the three strings that switch WITH the
        slide (`note`, `caption`, `alt`). One instrument, two mounts.
      `data-bench`     — the bench's options: which mount opens, the centres
        the field can be panned to and where they are offered, the motion
        toggle's default and its two authored words, the per-magnification
        resolve notes, and Design's own control captions.

    Everything is checked here rather than in the browser for the reason the
    whole of `r_sim` is: a bench that renders a "Move the slide to" caption
    over nothing, or offers a mount the canvas cannot draw, is a defect the
    page hides. The build is the only place that can refuse it.
    """
    controls = list(sim.get("controls") or [])
    mounts = sim.get("mounts") or []
    specimens = list(sim.get("specimens") or [])

    if mounts and specimens:
        raise ValueError(
            "Activity %r declares BOTH mounts[] and specimens[]. They are the "
            "same list in two shapes — mounts[] is specimens[] plus the "
            "per-slide strings — and two sources for one slide list is how "
            "the canvas and the selector come to disagree." % act_id)

    if mounts:
        ids = [m.get("id") for m in mounts]
        if len(ids) != len(set(ids)) or not all(ids):
            raise ValueError(
                "Activity %r has missing or duplicate mount id(s): %r. The id "
                "is what `centre_offered_on` and `start_mount` name."
                % (act_id, ids))
        for m in mounts:
            if not m.get("label"):
                raise ValueError(
                    "Activity %r mount %r has no label — the selector would "
                    "offer a blank slide." % (act_id, m.get("id")))
            if _specimen_kind(m.get("specimen") or "") is None:
                raise ValueError(
                    "Activity %r mount %r names specimen %r, which "
                    "shared/ks3.js has no slide model for (specimenKind() "
                    "knows onion / onion-with-bubbles / cheek / pond). "
                    "`specimen` is the classifier string; `label` is the "
                    "caption, and it is free text."
                    % (act_id, m.get("id"), m.get("specimen")))
            for org in m.get("organisms") or []:
                if org.get("kind") not in MICRO_ORGANISMS:
                    raise ValueError(
                        "Activity %r mount %r declares an organism of kind %r. "
                        "shared/ks3.js draws only %s — anything else is drawn "
                        "as nothing and narrated as nothing."
                        % (act_id, m.get("id"), org.get("kind"),
                           ", ".join(MICRO_ORGANISMS)))
                missing = [k for k in ("x", "y", "depth", "len", "seed")
                           if not _num(org.get(k))]
                if missing:
                    raise ValueError(
                        "Activity %r mount %r has an organism missing numeric "
                        "%s. All five are millimetres on the slide (bar the "
                        "seed) and the drawing is computed from them."
                        % (act_id, m.get("id"), ", ".join(missing)))
        specimens = [str(m["specimen"]) for m in mounts]
    else:
        if not specimens:
            raise ValueError(
                "Activity %r declares a microscope sim with no specimens[] and "
                "no mounts[] — the specimen selector would be an empty "
                "<select>." % act_id)
        unknown_slides = [s for s in specimens if _specimen_kind(s) is None]
        if unknown_slides:
            raise ValueError(
                "Activity %r offers specimen(s) %s that shared/ks3.js has no "
                "slide model for (specimenKind() knows onion / onion-with-"
                "bubbles / cheek / pond). Either name the slide so it "
                "classifies, or teach ks3.js to draw it — a slide that "
                "renders as an empty field of view is a defect."
                % (act_id, ", ".join(repr(s) for s in unknown_slides)))

    mount_ids = [str(m["id"]) for m in mounts]
    bench = {}

    start = sim.get("start_mount")
    if start is not None:
        if str(start) not in mount_ids:
            raise ValueError(
                "Activity %r sets start_mount %r, which is not one of its "
                "mounts %r." % (act_id, start, mount_ids))
        bench["start"] = str(start)

    # ── G10 · the centre control ──────────────────────────────────────────
    centres = sim.get("centres") or []
    has_centre = "centre" in controls
    if has_centre and not centres:
        raise ValueError(
            "Activity %r declares the `centre` control with no centres[] — a "
            "caption over an empty row. The centres are where the field can "
            "be panned to." % act_id)
    if centres and not has_centre:
        raise ValueError(
            "Activity %r authors centres[] but does not declare the `centre` "
            "control, so the field can never be panned to any of them."
            % act_id)
    if centres:
        cids = [c.get("id") for c in centres]
        if len(cids) != len(set(cids)) or not all(cids):
            raise ValueError(
                "Activity %r has missing or duplicate centre id(s): %r"
                % (act_id, cids))
        for c in centres:
            if not c.get("label"):
                raise ValueError(
                    "Activity %r centre %r has no label. The labels are "
                    "AUTHORED teaching language — how the lesson refers to an "
                    "organism the student cannot yet name — and are never "
                    "derived from a kind." % (act_id, c.get("id")))
            if not (_num(c.get("x")) and _num(c.get("y"))):
                raise ValueError(
                    "Activity %r centre %r needs numeric x and y — "
                    "millimetres on the slide, which is what the field is "
                    "translated by." % (act_id, c.get("id")))
        bench["centres"] = [{"id": str(c["id"]), "label": str(c["label"]),
                             "x": c["x"], "y": c["y"]} for c in centres]

        offered = sim.get("centre_offered_on")
        if offered is not None:
            if not mounts:
                raise ValueError(
                    "Activity %r sets centre_offered_on without mounts[] — "
                    "there is nothing to name." % act_id)
            stray = [o for o in offered if str(o) not in mount_ids]
            if stray:
                raise ValueError(
                    "Activity %r offers the centre control on %s, which "
                    "is not a mount id. Mounts are %r."
                    % (act_id, ", ".join(repr(s) for s in stray), mount_ids))
            bench["centreOn"] = [str(o) for o in offered]

    # ── G11 · the motion toggle ───────────────────────────────────────────
    has_motion = "motion" in controls
    if has_motion != bool(sim.get("motion_toggle")):
        raise ValueError(
            "Activity %r declares the `motion` control %s motion_toggle. The "
            "control IS the toggle; one without the other is either a dead "
            "switch or a promise with no button."
            % (act_id, "without" if has_motion else "but not"))
    if has_motion:
        labels = sim.get("motion_labels") or []
        if len(labels) != 2 or not all(str(x).strip() for x in labels):
            raise ValueError(
                "Activity %r needs exactly two non-empty motion_labels, on "
                "and then off, got %r. The two words are CONTENT — "
                "'Swimming' / 'Held still' is a Paramecium vocabulary choice, "
                "not a generic on/off — so the engine will not invent them."
                % (act_id, labels))
        bench["motion"] = {"on": sim.get("motion_default") is not False,
                           "labels": [str(x) for x in labels]}

    # ── the per-magnification resolve note ────────────────────────────────
    notes = sim.get("resolve_notes")
    if notes:
        keyed = {}
        for k, v in notes.items():
            try:
                total = int(k)
            except (TypeError, ValueError):
                raise ValueError(
                    "Activity %r keys a resolve note by %r. The keys are TOTAL "
                    "magnifications: %s." % (act_id, k, MICRO_TOTALS))
            if total not in MICRO_TOTALS:
                raise ValueError(
                    "Activity %r keys a resolve note by ×%d, which this "
                    "instrument cannot reach. The turret gives %s."
                    % (act_id, total,
                       ", ".join("×%d" % m for m in MICRO_TOTALS)))
            keyed[str(total)] = str(v)
        absent = [m for m in MICRO_TOTALS if str(m) not in keyed]
        if absent:
            raise ValueError(
                "Activity %r has resolve notes for some magnifications and "
                "not %s. The note is the lesson answering its own gate, and a "
                "lens that answers nothing reads as a lens with nothing to "
                "say." % (act_id, ", ".join("×%d" % m for m in absent)))
        bench["resolve"] = keyed

    # Design's own control captions, which override CONTROL_LABELS' generic
    # words ("Mount", not "Slide on the stage"). A caption for a control the
    # lesson never declares would never be read, so it is refused.
    labels = sim.get("control_labels") or {}
    stray = [k for k in labels if k not in controls]
    if stray:
        raise ValueError(
            "Activity %r labels control(s) %s that it does not declare in "
            "controls[]. The caption would never be rendered."
            % (act_id, ", ".join(repr(s) for s in stray)))
    if labels:
        bench["labels"] = {str(k): str(v) for k, v in labels.items()}

    out = ' data-specimens="%s"' % e(json.dumps(
        [str(s) for s in specimens], sort_keys=True))
    if mounts:
        keep = ("id", "label", "specimen", "note", "caption", "alt",
                "organisms")
        out += ' data-mounts="%s"' % e(json.dumps(
            [{k: m[k] for k in keep if k in m} for m in mounts],
            sort_keys=True))
    if bench:
        out += ' data-bench="%s"' % e(json.dumps(bench, sort_keys=True))
    return out


def r_sim(sim, act_id):
    """A particle lab.  Contract: shared/ks3.js `wireSim`.

    Emitted INSIDE the activity's [data-activity] section, alongside the
    options — that adjacency is what Law 4 gating runs on. ks3.js walks up to
    the enclosing [data-activity], finds the .ks3-option buttons and holds the
    sim frozen until one is clicked. A separate wrapper round the sim would
    quietly disable the gate and the lesson would give its answer away.

    .ks3-sim-controls and .ks3-sim-readout are emitted EMPTY on purpose: the JS
    builds the sliders from data-controls and writes the readout. Putting
    placeholder text in either would be a claim the page cannot honour if the
    script fails to load.

    The canvas is 560 × 220. `.ks3-sim-cover` pins itself over the canvas with
    `aspect-ratio: 560 / 220`, so the two are one number in two files: change
    the height here and R5's veil stops covering the frame it is veiling.
    """
    kind = sim.get("kind", "")
    if kind not in SIM_ARIA:
        raise ValueError(
            "Activity %r declares sim kind %r. shared/ks3.js implements only "
            "%s, and there is no aria-label written for it — a new sim kind "
            "needs both before it can be rendered."
            % (act_id, kind, ", ".join(sorted(SIM_ARIA))))
    caption = sim.get("caption", "")

    # Controls are VALIDATED, not passed through. An earlier version emitted
    # whatever was authored on the reasoning that ks3.js would ignore names it
    # did not implement — which is true, and is exactly the problem: five
    # authored dials across five of the seven labs (`state`, `medium`,
    # `release`, `number of particles`) rendered an empty or half-populated
    # control panel and nothing anywhere said so. A dial a student can see and
    # cannot move is worse than one that was never promised.
    #
    # This list is the same one `CONTROL_LABELS` declares in shared/ks3.js.
    # They must agree; a mismatch is a build failure, exactly as an unknown
    # sim kind is.
    unknown = [c for c in (sim.get("controls") or []) if c not in SIM_CONTROLS]
    if unknown:
        raise ValueError(
            "Activity %r declares sim control(s) %s, which shared/ks3.js does "
            "not implement. Implemented: %s. Either add the control to "
            "CONTROL_LABELS and wireSim in shared/ks3.js, or drop it from the "
            "lesson — a control that renders and does nothing is a defect."
            % (act_id, ", ".join(repr(u) for u in unknown),
               ", ".join(sorted(SIM_CONTROLS))))
    controls = ",".join(str(c) for c in (sim.get("controls") or []))
    label = (SIM_ARIA[kind] + " " + caption).strip()

    # MRB-198 — payload-carrying kinds. The payload is VALIDATED here, not
    # passed through, for the same reason the controls are: a payload the JS
    # cannot draw (an unknown slide, a `needs` edge pointing nowhere, a
    # dependency cycle that would never finish propagating) renders as a
    # control panel promising things the canvas cannot honour. Serialised as
    # JSON into a data attribute; shared/ks3.js parses it back.
    extra = ""
    if kind == "microscope":
        extra = _microscope_payload(sim, act_id)
    elif kind == "system-parts":
        parts = sim.get("parts") or []
        if not parts:
            raise ValueError(
                "Activity %r declares a system-parts sim with no parts[] — "
                "there would be nothing to switch off." % act_id)
        ids = [p.get("id") for p in parts]
        if len(ids) != len(set(ids)) or not all(ids):
            raise ValueError(
                "Activity %r has missing or duplicate part ids: %r"
                % (act_id, ids))
        for p in parts:
            if not p.get("name") or not p.get("job"):
                raise ValueError(
                    "Activity %r part %r needs both a name and a job — the "
                    "canvas labels parts by name and the readout narrates "
                    "the job." % (act_id, p.get("id")))
            bad = [n for n in (p.get("needs") or []) if n not in ids]
            if bad:
                raise ValueError(
                    "Activity %r part %r needs %s, which is not a declared "
                    "part — the cascade is derived from these edges and a "
                    "dangling edge is a knock-on that silently never happens."
                    % (act_id, p["id"], ", ".join(repr(b) for b in bad)))
        # The cascade terminates because the graph is acyclic. Prove it now:
        # a cycle would hang the propagation in every student's browser.
        needs_of = {p["id"]: list(p.get("needs") or []) for p in parts}
        WHITE, GREY, BLACK = 0, 1, 2
        state = {i: WHITE for i in needs_of}

        def _visit(n, trail):
            state[n] = GREY
            for m in needs_of[n]:
                if state[m] == GREY:
                    raise ValueError(
                        "Activity %r has a dependency cycle: %s — the "
                        "failure cascade would propagate forever."
                        % (act_id, " → ".join(trail + [m])))
                if state[m] == WHITE:
                    _visit(m, trail + [m])
            state[n] = BLACK

        for i in sorted(needs_of):
            if state[i] == WHITE:
                _visit(i, [i])
        payload = [{k: p[k] for k in ("id", "name", "job", "needs",
                                      "one_of_many") if k in p}
                   for p in parts]
        extra = ' data-parts="%s"' % e(json.dumps(payload, sort_keys=True))

    return (
        '<div class="ks3-sim" data-sim="%s" data-controls="%s"%s>'
        '<canvas class="ks3-sim-canvas" width="560" height="220" role="img" '
        'aria-label="%s"></canvas>'
        '<p class="ks3-sim-cover">Make your prediction first — then the lab '
        'runs.</p>'
        '<div class="ks3-sim-controls"></div>'
        '<p class="ks3-sim-readout" role="status"></p>'
        '<p class="ks3-sim-caption">%s</p>'
        '</div>'
        % (e(kind), e(controls), extra, e(label), t(caption)))


# ── the CLASSIFY instruments (⊕ §4.8.2 · G3, G4) ─────────────────────────
#
# Two activity KINDS, not two block types. §5.1.1's block vocabulary stays
# closed: both render inside a `check` shell, which is what `core` names, and
# `activities[].kind` is what distinguishes them. See ks3_data/b1/__init__.py's
# header for the same ruling from the data side.
#
# ⚠️ BOTH ARE RENDERED WHOLE, AT BUILD TIME. Design's page holds all 28 lamp
# results and all 8 evidence lines in a JavaScript constant and templates the
# DOM from it; nothing in this generator works that way, and a page whose
# content only exists once a script has run is a page that says nothing when the
# script 404s. So every specimen panel and every evidence line is real markup,
# `hidden` until the student has earned it — exactly the shape `_rung_self`
# already uses for the ladder's success criteria.
#
# The consequence, stated plainly: a student who reads the page source can find
# the answers. That is true of the ladder criteria too, and it is the accepted
# trade in this system — the alternative is a lesson that is blank without JS.


def _lamp_li(test, result):
    """One lamp. R2: the state carries a WORD, never colour alone.

    The word starts as "Tap to test" and ks3.js writes "Yes"/"No" from
    `data-yes` when the lamp is tapped. It cannot be emitted resolved: the
    verdict IS the finding the tap is supposed to produce.

    The lamp is deliberately NOT a `.ks3-option`. Its resolved state differs by
    the specimen's property, and R3's runtime assertion requires every
    `.ks3-option` outside the ladder to render alike whichever was pressed — a
    lamp that lit differently for "yes" and "no" would fail it, and rightly, if
    it claimed to be an answer button. It is not one: it reports the SPECIMEN,
    not the student.
    """
    yes, note = (result + [""])[:2] if isinstance(result, list) else (result, "")
    return ('<li><button type="button" class="ks3-lamp" data-test="%s" '
            'data-yes="%d" aria-pressed="false">'
            '<span class="ks3-lamp-row">'
            '<span class="ks3-lamp-badge" aria-hidden="true">%s</span>'
            '<span class="ks3-lamp-name">%s</span>'
            '<span class="ks3-lamp-verdict" data-lamp-verdict>Tap to test</span>'
            '</span>'
            '<span class="ks3-lamp-note">%s</span></button></li>'
            % (e(test["key"]), 1 if yes else 0, t(test.get("initial", "")),
               t(test.get("name", "")), t(note)))


def _board_panel(a, spec, tests):
    """One specimen's whole instrument: gate, lamps, verdict.

    All four panels are in the document and only one is shown, which is what
    makes the four instruments' progress independent WITHOUT any state to keep:
    the DOM is the state. Switching specimens shows a panel that still holds
    whatever the student did to it.
    """
    results = spec.get("results") or {}
    predict = a.get("predict") or {}
    opts = "".join(
        _option_li(i, o, ' aria-pressed="false"')
        for i, o in enumerate(predict.get("options") or []))

    # ⊕ F4, Code's call (inventory §8c). Design REMOVES the prediction from the
    # DOM the moment it is made, so a student cannot see what they wagered.
    # It stays here, in its chosen state, and it stays CHANGEABLE — not
    # `disabled`. Both halves are forced: R3's runtime assertion fails an
    # activity option that is disabled, and fails a group whose options do not
    # all render alike, which a one-way gate would produce the moment its
    # unchosen sibling stayed resting. Keeping it live satisfies F4 and R3 at
    # once, and contradicts nothing Design drew — the gate still opens the
    # board, and the board never closes again.
    gate = ('<div class="ks3-board-predict">'
            '<p class="ks3-board-ask">%s</p>'
            '<ul class="ks3-options ks3-board-options" role="list">%s</ul>'
            '</div>' % (t(predict.get("prompt", "")), opts))

    lamps = "".join(_lamp_li(x, results.get(x["key"])) for x in tests)

    verdict = ('<div class="ks3-reveal ks3-board-verdict" data-reveal hidden>'
               '<p class="ks3-board-verdict-head">%s</p>'
               '<p class="ks3-board-verdict-body">%s</p>'
               '<div class="ks3-board-extra">'
               '<span class="ks3-board-extra-label">%s</span>'
               '<span class="ks3-board-extra-answer">%s</span>'
               '<span class="ks3-board-extra-note">%s</span>'
               '</div></div>'
               % (rich(spec.get("verdict_head", "")),
                  rich(spec.get("verdict_body", "")),
                  t(spec.get("extra_label", "The eighth test")),
                  t(spec.get("extra_answer", "")),
                  rich(spec.get("extra_note", ""))))

    return ('<div class="ks3-board-panel" data-specimen="%s"%s>'
            '<p class="ks3-board-name">%s</p>'
            '<p class="ks3-board-blurb">%s</p>'
            '%s'
            '<div class="ks3-board-tests" data-board-tests hidden>'
            '<div class="ks3-board-head">'
            '<p class="ks3-board-instruction" data-board-instruction>'
            'Tap each test to run it.</p>'
            '<p class="ks3-board-tally" data-board-tally role="status">'
            '0 of %d lit</p></div>'
            '<ul class="ks3-lamps" role="list">%s</ul>'
            '%s</div></div>'
            % (e(spec["id"]), "" if spec.get("_first") else " hidden",
               t(spec.get("name", "")), t(spec.get("blurb", "")),
               gate, len(tests), lamps, verdict))


def r_test_board(a, act_id):
    """⊕ G3 — the seven-tests board. CLASSIFY's decision instrument.

    Validation is the same discipline `r_sim` applies to a sim payload: an
    instrument that renders half a specimen is worse than one that refuses to
    build, because the hole is silent and the lesson still looks finished.
    """
    tests = a.get("tests") or []
    specimens = a.get("specimens") or []
    if not tests:
        raise ValueError("test-board %r declares no tests[] — there would be "
                         "nothing to tap." % act_id)
    keys = [x.get("key") for x in tests]
    if len(keys) != len(set(keys)) or not all(keys):
        raise ValueError(
            "test-board %r has missing or duplicate test key(s): %r. `initial` "
            "may repeat (MRS GREN has two R's); `key` may not, because it is "
            "what each specimen's results are looked up by." % (act_id, keys))
    if len(specimens) < 2:
        raise ValueError(
            "test-board %r declares %d specimen(s). The instrument's whole "
            "argument is comparison — a board with one specimen teaches that a "
            "score settles it, which is the misconception it exists to break."
            % (act_id, len(specimens)))
    if not (a.get("predict") or {}).get("options"):
        raise ValueError(
            "test-board %r has no predict.options — Law 4's gate is what opens "
            "the board, and without it the lamps are readable before the "
            "student has committed to anything." % act_id)
    for sp in specimens:
        missing = [k for k in keys if k not in (sp.get("results") or {})]
        if missing:
            raise ValueError(
                "test-board %r specimen %r supplies no result for test(s) %s. "
                "Every specimen answers every test or the board has a lamp that "
                "cannot resolve." % (act_id, sp.get("id"), ", ".join(missing)))

    tabs = "".join(
        '<li><button type="button" class="ks3-tab" data-specimen="%s" '
        'aria-pressed="%s">%s</button></li>'
        % (e(sp["id"]), "true" if i == 0 else "false", t(sp.get("name", "")))
        for i, sp in enumerate(specimens))

    panels = "".join(
        _board_panel(a, dict(sp, _first=(i == 0)), tests)
        for i, sp in enumerate(specimens))

    return ('<ul class="ks3-tabs" role="list">%s</ul>%s' % (tabs, panels))


def r_sort_rows(a, act_id):
    """⊕ G4 — the three-way sorter, plus MRB-196's self-check.

    R3 is the whole design constraint here and it is obeyed twice over: a chip
    takes the same chosen treatment whichever category it names, and after the
    reveal a wrong row is pixel-identical to a right one. The page states what
    settles each item; it never says whether the student had it.

    ⚖️ THE SELF-CHECK (MRB-196, ruled by Mide 13 Aug 2026). Design's sorter
    reveals eight answers and never asks the student whether they matched, so
    the student commits and never finds out — which Law 4 forbids. The record
    carries `self_check` and it renders ONLY once the evidence is showing,
    because before that there is nothing to compare against. There is no
    `answer` key and there must never be one: nothing on any option button and
    nothing on any row changes by what is picked. The page asks; it does not
    grade.
    """
    cats = a.get("categories") or []
    items = a.get("items") or []
    if len(cats) < 2:
        raise ValueError("sort-rows %r needs at least 2 categories, got %d — "
                         "one box is not a sort." % (act_id, len(cats)))
    if not items:
        raise ValueError("sort-rows %r declares no items[]." % act_id)
    for it in items:
        if it.get("answer") not in cats:
            raise ValueError(
                "sort-rows %r item %r answers %r, which is not one of the "
                "declared categories %r. The evidence line's lead word IS the "
                "answer, so a stray one renders a category the student was "
                "never offered." % (act_id, it.get("id"), it.get("answer"), cats))
        if not (it.get("evidence") or "").strip():
            raise ValueError(
                "sort-rows %r item %r has no evidence. The reveal exists to say "
                "what settles each one; a blank line says nothing and the "
                "student has no way to self-mark it." % (act_id, it.get("id")))

    rows = []
    for it in items:
        chips = "".join(
            '<button type="button" class="ks3-sort-chip" data-cat="%s" '
            'aria-pressed="false">%s</button>' % (e(c), t(c)) for c in cats)
        # ⊕ F7, Code's call. Design's evidence carries `data-reveal` WITHOUT
        # `class="ks3-reveal"`, so `animation-name` resolves to `none` and the
        # 220ms reveal never fires — measured, inventory §3.2. The class is the
        # animation's only hook; `.ks3-sort-evidence` then takes the panel back
        # off it, exactly as `.ks3-dark .ks3-reveal` already re-paints the same
        # base class for the ink-dark surface.
        rows.append(
            '<li class="ks3-sortrow" data-item="%s">'
            '<div class="ks3-sortrow-main">'
            '<span class="ks3-sortrow-name">%s</span>'
            '<span class="ks3-sortrow-chips">%s</span></div>'
            '<p class="ks3-reveal ks3-sort-evidence" data-reveal hidden>'
            '<strong class="ks3-sort-answer">%s</strong> — %s</p></li>'
            % (e(it.get("id", "")), t(it.get("name", "")), chips,
               t(it["answer"]), rich(it["evidence"])))

    self_check = _self_check(a, act_id)

    return ('<ul class="ks3-sortrows" role="list">%s</ul>'
            '<div class="ks3-sort-foot">'
            '<button type="button" class="ks3-reveal-btn ks3-sort-reveal" '
            'data-sort-reveal disabled>%s</button>'
            '<span class="ks3-sort-progress" data-sort-progress '
            'data-total="%d" data-total-word="%s">0 of %d sorted</span>'
            '</div>%s'
            % ("".join(rows),
               t(a.get("reveal_label") or "Show what settles each one"),
               len(items), e(_count_word(len(items))), len(items), self_check))


def r_critique_steps(a, act_id):
    """⊕ Judge someone else's method before you write your own.

    Six steps, three of which cost him. A CHECKBOX SET, not a radio group —
    the student marks every step they would change, so the demand is "find all
    the faults", not "find the fault". Rendered as an empty section before this.

    R3 holds and is worth stating: the verdict panels are keyed off the STEP's
    own `fault`, which is the method's property and not the student's. Every
    step opens identically whether or not it was tapped.
    """
    steps = a.get("steps") or []
    if len(steps) < 3:
        raise ValueError("critique-steps %r declares %d step(s)."
                         % (act_id, len(steps)))
    if not any(s.get("fault") for s in steps):
        raise ValueError(
            "critique-steps %r has no faulty step — there is nothing to find, "
            "and a student who taps nothing is right." % act_id)

    rows = "".join(
        '<li class="ks3-step" data-fault="%d">'
        '<button type="button" class="ks3-step-btn" aria-pressed="false">'
        '<span class="ks3-step-num" aria-hidden="true">%d</span>'
        '<span class="ks3-step-text">%s</span></button>'
        '<p class="ks3-step-verdict" hidden data-reveal>'
        '<strong class="ks3-step-word">%s</strong> %s</p></li>'
        % (1 if s.get("fault") else 0, i + 1, rich(s.get("text", "")),
           t(s.get("word", "")), rich(s.get("verdict", "")))
        for i, s in enumerate(steps))

    return ('<ul class="ks3-steps" role="list">%s</ul>'
            '<div class="ks3-steps-foot">'
            '<button type="button" class="ks3-reveal-btn ks3-steps-reveal" '
            'data-steps-reveal disabled>%s</button>'
            '<span class="ks3-steps-progress" data-steps-progress '
            'data-zero="%s">%s</span></div>'
            % (rows, t(a.get("reveal_label") or "Open them up"),
               e(a.get("progress_zero") or "Pick at least one"),
               t(a.get("progress_zero") or "Pick at least one")))


def r_fifa_construct(lesson, a, act_id):
    """⊕ MRB-204 step 4 — the student fills the steps before full FIFA.

    Law 5's "the same artifact, produced by the student": the stepper's letters
    and these fields' letters must match in order, and the model, the fields
    and the success criteria must be the same length. Asserted here rather
    than trusted, because the claim is the whole point of the pairing.

    Two defects on Design's page are fixed rather than reproduced, both stated:

    1. **Check accepts an empty attempt** and reveals the full model. A student
       who taps it first has been handed the answer before writing anything,
       which is what steps 3 and 4 exist to prevent. Gated on a non-empty field.
    2. **The typed working does not survive a re-render.** `<input value=…>`
       sets an ATTRIBUTE, which the element reads only as its default, so the
       first tick wipes what the student wrote. No `value` attribute is emitted.
    """
    fields = a.get("fields") or []
    model = a.get("model") or []
    success = a.get("success") or []
    if not (len(fields) == len(model) == len(success)):
        raise ValueError(
            "fifa-construct %r has %d fields, %d model lines and %d success "
            "criteria. Law 5 says the student produces the SAME artifact, and "
            "three different lengths cannot describe one."
            % (act_id, len(fields), len(model), len(success)))

    stepper = next((x for x in (lesson.get("activities") or [])
                    if x.get("kind") == "worked-example" and x.get("staged")), None)
    if stepper:
        want = [s.get("letter") for s in (stepper.get("fifa") or [])]
        got = [f.get("letter") for f in fields]
        if want != got:
            raise ValueError(
                "fifa-construct %r asks for %r and the worked example it "
                "mirrors shows %r. The letters and their ORDER are the shared "
                "artifact." % (act_id, got, want))

    rows = "".join(
        '<div class="ks3-fifa-field">'
        '<label class="ks3-fifa-label" for="%s">'
        '<span class="ks3-fifa-letter" aria-hidden="true">%s</span> %s</label>'
        '<input class="ks3-fifa-input" type="text" id="%s" data-fifa-input '
        'placeholder="%s" autocomplete="off"></div>'
        % (e("ks3-fifa-%s" % f["id"]), t(f.get("letter", "")),
           t(f.get("label", "")), e("ks3-fifa-%s" % f["id"]),
           e(f.get("placeholder", "")))
        for f in fields)

    lines = "".join('<li class="ks3-model-line">%s</li>' % t(m) for m in model)
    ticks = "".join(
        '<li class="ks3-tick"><input type="checkbox" id="%s" data-crit>'
        '<label for="%s"><span class="ks3-tick-num">%d</span> %s</label></li>'
        % (e("ks3-fifa-crit-%s-%d" % (act_id, i)),
           e("ks3-fifa-crit-%s-%d" % (act_id, i)), i + 1, t(s))
        for i, s in enumerate(success))

    return ('<div class="ks3-construct">%s'
            '<div class="ks3-construct-foot">'
            '<button type="button" class="ks3-reveal-btn ks3-construct-check" '
            'data-construct-check disabled>%s</button>'
            '<span class="ks3-construct-hint" data-construct-hint>%s</span>'
            '</div>'
            '<div class="ks3-construct-out" hidden data-reveal>'
            '<p class="ks3-model-lead">%s</p>'
            '<ol class="ks3-model" role="list">%s</ol>'
            '<p class="ks3-crit-lead">Did you do all of these?</p>'
            '<ul class="ks3-ticks" role="list">%s</ul>'
            '<p class="ks3-construct-tally" hidden data-construct-tally '
            'role="status">%s</p></div></div>'
            % (rows, t(a.get("check_label") or "Check my working"),
               t("Write at least one step first"),
               t(a.get("model_lead", "")), lines, ticks,
               t(a.get("tally_met", ""))))


TRI_W, TRI_H, TRI_PAD, TRI_DIV_Y = 260, 216, 8, 130


def _triangle_geometry():
    """MRB-204 step 2's three cover boxes, DERIVED from the viewBox.

    They are a function of the fixed 260×216 frame and its dividers, so nothing
    is authored per lesson. Authoring twelve magic numbers a lesson is exactly
    the hand-authoring the generator exists to remove — and it is what produced
    four console errors on Design's own page, where they were left as template
    placeholders (`<rect> attribute x: Expected length, "{{ coverX }}"`; SVG
    geometry attributes are typed and reject a placeholder).
    """
    apex_x = TRI_W / 2.0
    base_y = TRI_H - TRI_PAD
    # Half-width of the triangle at any y, from similar triangles.
    def half(y):
        return (apex_x - TRI_PAD) * (y - TRI_PAD) / (base_y - TRI_PAD)

    # ⚠️ A RECTANGLE IN A TRIANGLE ALWAYS OVERHANGS, unless it is sized at its
    # own narrowest edge — and a box that narrow cannot hold the word it is
    # meant to hide. That is not a slip in Design's numbers, it is a property
    # of the shape, and it is why Design's `total` cover sits ~35 units outside
    # the sloping sides at its top edge.
    #
    # So the covers are sized GENEROUSLY, to cover their labels, and CLIPPED to
    # the triangle. The clip is what makes the geometry honest: a cover can be
    # as wide as the word needs and can never paint outside the shape. Derived
    # from the frame either way — nothing here is authored per lesson.
    pad, gutter = 16, 12
    top_h, low_h = 52, 48
    top_w = 2 * half(TRI_DIV_Y) - 2 * pad
    top = (apex_x - top_w / 2.0, TRI_DIV_Y - top_h - pad, top_w, top_h)
    low_w = half(base_y) - gutter - pad
    left = (apex_x - gutter / 2.0 - low_w, TRI_DIV_Y + pad, low_w, low_h)
    right = (apex_x + gutter / 2.0, TRI_DIV_Y + pad, low_w, low_h)
    return {"top": top, "left": left, "right": right,
            "apex": (apex_x, TRI_PAD), "base": (TRI_PAD, base_y,
                                                TRI_W - TRI_PAD, base_y),
            "div_half": half(TRI_DIV_Y)}


def r_formula_triangle(tri):
    """MRB-204 step 2 — the formula drawn as a triangle, in KS3 tokens.

    ⚠️ CORRECTED. Design's three cover boxes overhang the sloping sides —
    the `total` one by about 35 units at its top edge. It is not a slip and it
    is not nudgeable: a rectangle inside a triangle always overhangs unless it
    is sized at its own narrowest edge, and a box that narrow cannot hold the
    word it exists to hide. The covers are therefore sized to their labels and
    CLIPPED to the triangle path, so a cover can be as wide as the word needs
    and can never paint outside the shape. Both the boxes and the clip are
    derived from the frame; nothing is authored per lesson.
    """
    g = _triangle_geometry()
    # One triangle per page today; the id is derived from the aria-label so two
    # on one page would still not collide.
    clip_id = "ks3-tri-clip-%s" % hashlib.md5(
        (tri.get("aria_label", "") or "t").encode("utf-8")).hexdigest()[:8]
    ax, ay = g["apex"]
    x1, y1, x2, y2 = g["base"]
    dh = g["div_half"]

    def cover(key):
        x, y, w, h = g[key]
        return ('<rect class="ks3-tri-cover" data-cover="%s" x="%.2f" y="%.2f" '
                'width="%.2f" height="%.2f" rx="8"></rect>'
                % (e(key), x, y, w, h))

    labels = ""
    for key, (lx, ly) in (("top", (ax, TRI_DIV_Y - 42)),
                          ("left", (ax - 44, TRI_DIV_Y + 46)),
                          ("right", (ax + 44, TRI_DIV_Y + 46))):
        labels += ('<text class="ks3-tri-label" x="%.2f" y="%.2f" '
                   'text-anchor="middle">%s</text>'
                   % (lx, ly, t((tri.get(key) or {}).get("label", ""))))

    btns = "".join(
        '<button type="button" class="ks3-seg-btn ks3-tri-btn" '
        'data-cover="%s" aria-pressed="false">%s</button>'
        % (e(k), t((tri.get(k) or {}).get("button", "")))
        for k in ("top", "left", "right"))

    notes = "".join(
        '<p class="ks3-tri-note" data-note="%s" hidden>%s</p>'
        % (e(k), rich((tri.get(k) or {}).get("text", "")))
        for k in ("top", "left", "right"))

    close = ('<p class="ks3-tri-close">%s</p>' % rich(tri["close"])
             if tri.get("close") else "")

    return ('<div class="ks3-triangle" data-triangle>'
            '<p class="ks3-eyebrow">%s</p><p class="ks3-tri-heading">%s</p>'
            '<svg class="ks3-tri-svg" viewBox="0 0 %d %d" role="img" '
            'aria-label="%s">'
            '<defs><clipPath id="%s">'
            '<path d="M %.2f %.2f L %.2f %.2f L %.2f %.2f Z"/></clipPath></defs>'
            '<path class="ks3-tri-path" d="M %.2f %.2f L %.2f %.2f L %.2f %.2f Z"/>'
            '<line class="ks3-tri-div" x1="%.2f" y1="%d" x2="%.2f" y2="%d"/>'
            '<line class="ks3-tri-div" x1="%.2f" y1="%d" x2="%.2f" y2="%.2f"/>'
            '%s%s%s</svg>'
            '<div class="ks3-tri-btns">%s</div>%s%s</div>'
            % (t(tri.get("eyebrow", "")), t(tri.get("heading", "")),
               TRI_W, TRI_H, e(tri.get("aria_label", "")),
               clip_id, ax, ay, x2, y2, x1, y1,
               ax, ay, x2, y2, x1, y1,
               ax - dh, TRI_DIV_Y, ax + dh, TRI_DIV_Y,
               ax, TRI_DIV_Y, ax, y2,
               labels,
               '<g clip-path="url(#%s)">%s</g>'
               % (clip_id, cover("top") + cover("left") + cover("right")), "",
               btns, notes, close))


def r_cell_bench(a, act_id):
    """⊕ MODEL's flagship — seven parts, two cells, two ways of looking.

    b1-03 is the approved reference screen for MODEL, which carries 50 lesson
    slots, so this is the single highest-reach component in B1. It rendered as
    an empty section.

    The instrument's argument is the second view. A textbook drawing shows all
    seven parts; a school microscope shows three. Switching between them is
    how a student learns to tell "not there" from "there but you cannot see
    it" — which is the misconception the lesson exists to break, and it cannot
    be taught by a diagram alone.

    Every part carries `mark[specimen]` — the circles the canvas draws over
    the chosen part — so the marks live with the part rather than with the
    drawing, and a part that is absent from a specimen simply has none.
    """
    parts = a.get("parts") or []
    specimens = a.get("specimens") or []
    views = a.get("views") or []
    if not parts:
        raise ValueError("cell-bench %r declares no parts[]." % act_id)
    if len(specimens) < 2:
        raise ValueError(
            "cell-bench %r declares %d specimen(s). The whole instrument is "
            "'watch which parts stay put when you switch the cell'."
            % (act_id, len(specimens)))
    for p in parts:
        for sp in specimens:
            marks = (p.get("mark") or {}).get(sp["id"])
            if marks is None and p.get("where") != "plant":
                raise ValueError(
                    "cell-bench %r part %r has no mark for specimen %r. A part "
                    "the student can select and the canvas cannot point at is "
                    "a control that does nothing."
                    % (act_id, p.get("id"), sp["id"]))

    labels = a.get("control_labels") or {}
    where_labels = a.get("where_labels") or {}
    start = a.get("start") or specimens[0]["id"]

    def seg_row(name, items, current, extra=""):
        btns = "".join(
            '<button type="button" class="ks3-seg-btn ks3-bench-%s" '
            'data-%s="%s" aria-pressed="%s"%s>%s</button>'
            % (name, name, e(it["id"]),
               "true" if it["id"] == current else "false",
               ' data-locked="1"' if it.get("locked_until_gate") else "",
               t(it.get("label", "")))
            for it in items)
        return ('<div class="ks3-bench-control"><p class="ks3-bench-control-label">'
                '%s</p><div class="ks3-bench-seg">%s</div></div>'
                % (t(labels.get(name, name.title())), btns))

    controls = seg_row("specimen", specimens, start)
    if views:
        controls += seg_row("view", views, views[0]["id"])

    gate = ""
    g = a.get("gate") or {}
    if g.get("options"):
        gate = ('<div class="ks3-bench-gate" data-bench-gate>'
                '<p class="ks3-bench-gate-q">%s</p>%s</div>'
                % (t(g.get("q", "")), r_activity_options(g["options"])))

    part_btns = "".join(
        '<li><button type="button" class="ks3-part" data-part="%s" '
        'aria-pressed="%s"><span class="ks3-part-num" aria-hidden="true">%s'
        '</span><span class="ks3-part-body">'
        '<span class="ks3-part-name">%s</span>'
        '<span class="ks3-part-tag" data-where="%s"></span>'
        '</span></button></li>'
        % (e(p["id"]), "true" if i == 0 else "false", t(p.get("num", "")),
           t(p.get("name", "")), e(p.get("where", "")))
        for i, p in enumerate(parts))

    meta = json.dumps({
        "parts": [{"id": p["id"], "num": p.get("num", ""),
                   "name": p.get("name", ""), "where": p.get("where", ""),
                   "job": p.get("job", ""), "detail": p.get("detail", ""),
                   "visible": bool(p.get("visible")),
                   "scope_note": p.get("scope_note", ""),
                   "mark": p.get("mark") or {}} for p in parts],
        "specimens": [{"id": s["id"], "label": s.get("label", ""),
                       "art": s.get("art", ""), "alt": s.get("alt", ""),
                       "caption": s.get("caption", ""),
                       "tally": s.get("tally", ""),
                       "absent_tag": s.get("absent_tag", ""),
                       "absent_detail": s.get("absent_detail", "")}
                      for s in specimens],
        "where_labels": where_labels,
        "scope_words": a.get("scope_words") or {},
        "space": a.get("mark_space") or {"w": 900, "h": 560},
    }, sort_keys=True)

    return ('<div class="ks3-bench-controls">%s</div>%s'
            '<div class="ks3-bench" data-bench-grid="1" data-cellbench="%s">'
            '<ul class="ks3-parts" role="list">%s</ul>'
            '<div class="ks3-bench-main">'
            '<div class="ks3-bench-figure">'
            '<canvas class="ks3-bench-canvas" width="1800" height="1120" '
            'role="img" data-bench-canvas></canvas>'
            '<p class="ks3-bench-caption" data-bench-caption></p></div>'
            '<div class="ks3-readout" data-readout>'
            '<div class="ks3-readout-head">'
            '<span class="ks3-readout-num" aria-hidden="true" data-readout-num>'
            '</span>'
            '<span class="ks3-readout-name" data-readout-name></span>'
            '<span class="ks3-readout-where" data-readout-where></span></div>'
            '<p class="ks3-readout-job" data-readout-job></p>'
            '<p class="ks3-readout-detail" data-readout-detail></p>'
            '<p class="ks3-readout-scope" hidden data-readout-scope>'
            '<strong class="ks3-readout-scope-word" data-readout-scope-word>'
            '</strong> <span data-readout-scope-note></span></p></div>'
            '<p class="ks3-bench-tally" data-bench-tally></p>'
            '</div></div>'
            % (controls, gate, e(meta), part_btns))


def r_sort_pairs(a, act_id):
    """⊕ The two-way sorter — wall or membrane, the pair swapped most often.

    Rendered as an empty section. Structurally the three-way sorter's sibling,
    and deliberately NOT built on it: this one sends each statement to one of
    two named things rather than sorting rows into categories, and Design draws
    it as a row with the two names as buttons. One component that tried to be
    both would be the "nearest shape that exists" failure again.

    R3: nothing is marked here, and the intro says so in as many words.
    """
    rows = a.get("rows") or []
    cats = a.get("categories") or []
    if len(cats) != 2:
        raise ValueError(
            "sort-pairs %r declares %d categories. It is the TWO-way sorter; "
            "three or more is `sort-rows`." % (act_id, len(cats)))
    ids = {c["id"] for c in cats}
    for r in rows:
        if r.get("answer") not in ids:
            raise ValueError(
                "sort-pairs %r row %r answers %r, which is neither of %r."
                % (act_id, r.get("id"), r.get("answer"), sorted(ids)))

    lookup = {c["id"]: c.get("label", c["id"]) for c in cats}
    out = []
    for r in rows:
        chips = "".join(
            '<button type="button" class="ks3-seg-btn ks3-pair-chip" '
            'data-cat="%s" aria-pressed="false">%s</button>'
            % (e(c["id"]), t(c.get("label", ""))) for c in cats)
        out.append(
            '<li class="ks3-pairrow" data-row="%s">'
            '<p class="ks3-pairrow-text">%s</p>'
            '<div class="ks3-pairrow-chips">%s</div>'
            '<p class="ks3-pairrow-note" hidden data-reveal>'
            '<strong class="ks3-pairrow-word">%s</strong> %s</p></li>'
            % (e(r.get("id", "")), rich(r.get("text", "")), chips,
               t(lookup[r["answer"]] + "."), rich(r.get("note", ""))))

    unit = a.get("progress_unit") or "sent"
    panel = ('<div class="ks3-pair-panel" hidden data-pair-panel>%s</div>'
             % rich(a["reveal_panel"])) if a.get("reveal_panel") else ""
    return ('<ul class="ks3-pairrows" role="list">%s</ul>'
            '<div class="ks3-pair-foot">'
            '<button type="button" class="ks3-reveal-btn ks3-pair-reveal" '
            'data-pair-reveal disabled>%s</button>'
            '<span class="ks3-pair-progress" data-pair-progress '
            'data-total="%d" data-unit="%s">0 of %d %s</span></div>%s'
            % ("".join(out), t(a.get("reveal_label") or "Show the answers"),
               len(rows), e(unit), len(rows), t(unit), panel))


def r_fit_parts(lesson, a, act_id):
    """⊕ Build four real cells from one parts list, then run them.

    "Which parts" becomes a consequence of "what job". Rendered as an empty
    section. The parts list is `parts_from` — it names the bench's activity, so
    the two instruments share one list and a part cannot exist in the builder
    and not on the bench.

    ⊕ MRB-242 — takes `lesson` (which is all `_kinds_taking_lesson` needs to
    see: it asks the signature) so that `parts_from` can be RESOLVED here, at
    build time, instead of being trusted at runtime. The instrument shipped
    with zero part chips for a fortnight because the runtime lookup silently
    found the wrong element and `catch {}` swallowed it; the fix in
    `wireFit` reads the bench through this id, and a build error is the only
    thing that can stop a renamed or misspelt id doing it again quietly.
    """
    specimens = a.get("specimens") or []
    if not specimens:
        raise ValueError("fit-parts %r declares no specimens[]." % act_id)
    for sp in specimens:
        if not sp.get("needs"):
            raise ValueError(
                "fit-parts %r specimen %r needs no parts at all — there would "
                "be nothing to get right." % (act_id, sp.get("id")))

    # ⊕ MRB-242 / R5 — `parts_from` finally has a read site, and this is half
    # of it. The runtime half is `wireFit`, which resolves the bench by
    # `[data-activity="<parts_from>"]`; both halves fail loudly rather than
    # rendering an instrument with nothing in it.
    src_id = a.get("parts_from") or ""
    src = _activity(lesson, src_id) if src_id else None
    if not src or not src.get("parts"):
        raise ValueError(
            "fit-parts %r names parts_from=%r, which is not an activity in "
            "this lesson carrying a parts[] list. The builder's chips ARE the "
            "bench's parts; with no source there is nothing to install."
            % (act_id, src_id))

    # ⊕ MRB-242 / R5 — the verdict copy is AUTHORED, in full, or the build
    # stops. `wireFit` used to read `verdicts.ok` and `verdicts.problem`, two
    # keys this lesson has never authored, so every run printed one of two
    # strings hardcoded in the ENGINE — "It runs." / "It runs, after a
    # fashion." — and all five real headlines and all three badges were dead
    # keys. That is the B1-replay failure exactly: 146 unread keys, one of
    # them an approved science correction that never reached a student.
    #
    # So there is no fallback prose, here or in the engine. Every word a
    # student reads is a word someone wrote for this lesson; a missing one is
    # a build error, the way `parts_from` above is.
    verdicts = a.get("verdicts") or {}
    for state, keys in (("works", ("badge", "headline")),
                        ("waste", ("badge", "headline")),
                        ("fails", ("badge", "headline_one", "headline_many"))):
        block = verdicts.get(state) or {}
        for k in keys:
            if not str(block.get(k) or "").strip():
                raise ValueError(
                    "fit-parts %r authors no verdicts[%r][%r]. A run lands in "
                    "one of three states — works / waste / fails — and each "
                    "carries its own badge and headline. The engine has no "
                    "fallback prose and must never invent student-facing "
                    "copy." % (act_id, state, k))
    # `headline_many` is the plural branch and the number is the only thing
    # that varies in it, so it has to say where the number goes.
    many = str(verdicts["fails"]["headline_many"])
    if "{n}" not in many:
        raise ValueError(
            "fit-parts %r: verdicts['fails']['headline_many'] is chosen when "
            "two or more parts are missing and must carry the {n} "
            "placeholder for that count. Got %r." % (act_id, many))

    tabs = "".join(
        '<button type="button" class="ks3-seg-btn ks3-fit-tab" data-fit="%s" '
        'aria-pressed="%s">%s</button>'
        % (e(sp["id"]), "true" if i == 0 else "false", t(sp.get("label", "")))
        for i, sp in enumerate(specimens))

    meta = json.dumps({
        "specimens": [{"id": s["id"], "label": s.get("label", ""),
                       "kind": s.get("kind", ""), "job": s.get("job", ""),
                       "where": s.get("where", ""),
                       "needs": list(s.get("needs") or []),
                       "waste": s.get("waste") or {},
                       "note": s.get("note", "")} for s in specimens],
        "labels": {
            "job": a.get("job_label", "The job"),
            "install": a.get("install_label", "Install the parts"),
            "run": a.get("run_label", "Run this cell"),
            "rerun": a.get("rerun_label", "Run it again"),
            "clear": a.get("clear_label", "Strip it back out"),
            "empty": a.get("install_empty_hint", "Install something first"),
            # ⊕ MRB-242 — `unit` ("cells run") is gone. It was serialised here
            # and read by nothing: the words belong to the BLOCK-HEAD counter
            # Design draws, which is now authored as `head_counter` and
            # rendered by `_head_counter` like every other one. `installed` is
            # the foot hint's unit word and is read — "5 of 7 installed".
            "installed": a.get("install_unit", "installed"),
        },
        "verdicts": verdicts,
        "finding_words": a.get("finding_words") or {},
        "consequence": a.get("consequence") or {},
        "note_when": a.get("note_when", ""),
        "waste_fallback": a.get("waste_fallback", ""),
        "parts_from": a.get("parts_from", ""),
    }, sort_keys=True)

    return ('<div class="ks3-fit" data-fit-spec="%s">'
            '<div class="ks3-fit-tabs">%s</div>'
            '<div class="ks3-fit-job"><p class="ks3-fit-job-label"></p>'
            '<p class="ks3-fit-job-text"></p>'
            '<p class="ks3-fit-job-where"></p></div>'
            '<p class="ks3-fit-install-label"></p>'
            '<ul class="ks3-fit-parts" role="list" data-fit-parts></ul>'
            '<div class="ks3-fit-foot">'
            '<button type="button" class="ks3-reveal-btn ks3-fit-run" '
            'data-fit-run></button>'
            '<button type="button" class="ks3-fit-clear" data-fit-clear>'
            '</button>'
            '<span class="ks3-fit-progress" data-fit-progress></span></div>'
            '<div class="ks3-fit-out" hidden data-reveal>'
            # ⊕ MRB-242 — Design draws a mono uppercase pill ABOVE the
            # headline, its fill carrying the state (reference line 328 /
            # `verdictBadgeStyle` line 1243). No badge element was ever
            # emitted, so `verdicts.*.badge` had nowhere to land.
            '<p class="ks3-fit-badge" data-fit-badge></p>'
            '<p class="ks3-fit-verdict" data-fit-verdict></p>'
            '<ul class="ks3-fit-findings" role="list" data-fit-findings></ul>'
            '<p class="ks3-fit-note" data-fit-note></p></div>'
            '</div>' % (e(meta), tabs))


ZOOM_DRAWINGS = {"plant", "plant-shoot", "one-leaf", "leaf-section", "one-cell"}


def r_zoom_ladder(a, act_id):
    """⊕ Five stops from a whole plant to one cell, without leaving the leaf.

    A slider and a tick row over one canvas, with an orange dashed box showing
    where the NEXT stop down is hiding inside this one. The panel underneath
    says what this level can do that the level below cannot — which is the
    lesson's whole argument, and the reason the ladder is not a size chart.

    The `next_box` rectangles are AUTHORED, one per level in the payload's own
    design space, so the drawing and the box cannot drift apart. The last level
    has none: there is no stop below a cell.
    """
    levels = a.get("levels") or []
    if len(levels) < 2:
        raise ValueError("zoom-ladder %r declares %d level(s)."
                         % (act_id, len(levels)))
    for lv in levels:
        if lv.get("drawing") not in ZOOM_DRAWINGS:
            raise ValueError(
                "zoom-ladder %r level %r asks for drawing %r. Known: %s."
                % (act_id, lv.get("tick"), lv.get("drawing"),
                   ", ".join(sorted(ZOOM_DRAWINGS))))

    canvas = a.get("canvas") or {}
    buf = canvas.get("buffer") or [1800, 1000]
    space = canvas.get("design_space") or [900, 500]
    start = a.get("start")
    idx = next((i for i, lv in enumerate(levels)
                if lv.get("tick", "").lower().startswith(str(start).lower())), 0)

    ticks = "".join(
        '<button type="button" class="ks3-seg-btn ks3-zoom-tick" '
        'data-zoom="%d" aria-pressed="%s">%s</button>'
        % (i, "true" if i == idx else "false", t(lv.get("tick", "")))
        for i, lv in enumerate(levels))

    panels = "".join(
        '<div class="ks3-zoom-panel" data-zoom="%d"%s>'
        '<p class="ks3-zoom-name">%s</p>'
        '<p class="ks3-zoom-what">%s</p>'
        '<div class="ks3-zoom-gain">'
        '<p class="ks3-zoom-gain-label">%s</p>'
        '<p class="ks3-zoom-gain-text">%s</p></div>'
        '<p class="ks3-zoom-human"><strong>%s</strong> %s</p></div>'
        % (i, "" if i == idx else " hidden", t(lv.get("name", "")),
           rich(lv.get("what", "")), t(lv.get("gain_label", "")),
           rich(lv.get("gain", "")), t(a.get("human_prefix") or "In you:"),
           rich(lv.get("human", "")))
        for i, lv in enumerate(levels))

    meta = json.dumps(
        [{"drawing": lv["drawing"], "box": lv.get("next_box"),
          "size": lv.get("size", ""), "alt": lv.get("alt", "")}
         for lv in levels], sort_keys=True)

    aid = "ks3-zoom-%s" % act_id
    fmt = a.get("step_format") or "Stop {n} of {total}"
    return ('<div class="ks3-zoom" data-zoom-levels="%s" data-space="%d,%d" '
            'data-box-label="%s">'
            '<div class="ks3-zoom-frame">'
            '<canvas class="ks3-zoom-canvas" width="%d" height="%d" role="img" '
            'aria-label="%s" data-zoom-canvas></canvas>'
            '<div class="ks3-zoom-controls">'
            '<div class="ks3-zoom-head">'
            '<p class="ks3-zoom-step" data-zoom-step data-format="%s">%s</p>'
            '<p class="ks3-zoom-size" data-zoom-size>%s</p></div>'
            '<label class="ks3-visually-hidden" for="%s">%s</label>'
            '<input class="ks3-zoom-range" type="range" id="%s" min="0" '
            'max="%d" step="1" value="%d" data-zoom-range>'
            '<div class="ks3-zoom-ticks">%s</div>'
            '</div></div>%s</div>'
            % (e(meta), space[0], space[1],
               e(a.get("next_box_label") or "NEXT STOP IS HERE"),
               buf[0], buf[1], e(levels[idx].get("alt", "")), e(fmt),
               t(fmt.replace("{n}", str(idx + 1))
                    .replace("{total}", str(len(levels)))),
               t(levels[idx].get("size", "")), e(aid),
               t(a.get("slider_label") or "Zoom level"), e(aid),
               len(levels) - 1, idx, ticks, panels))


def r_sort_task(a, act_id):
    """⊕ Eight things that get put on the wrong rung.

    THE activity Mide rejected by name on 11 August: "name the level for each
    of these eight and say what settled it" rendered as a four-option multiple
    choice with eight items in the prompt, because CLASSIFY had no sorting
    component and the content was forced into the nearest shape that existed.

    ⚠️ R3 and the row. After the reveal the ROW is marked — inset on ink when
    the student had it, alert-tint on the alert border when they did not — and
    the CHOICE BUTTONS are untouched, identical before and after and identical
    on a right row and a wrong one. Verified by driving Design's page. The mark
    is on a container, never on a control, which is what keeps a deferred,
    self-service, student-opened mark clear of R3. Do not move it onto the
    buttons for tidiness; that is the whole distinction.
    """
    items = a.get("items") or []
    choices = a.get("choices") or []
    if len(choices) < 3:
        raise ValueError(
            "sort-task %r offers %d rung(s). The awkward cases need every rung "
            "AND the off-ladder answer, or the hard ones have nowhere to go."
            % (act_id, len(choices)))
    for it in items:
        if it.get("answer") not in choices:
            raise ValueError(
                "sort-task %r item %r answers %r, which is not one of the "
                "offered rungs %r." % (act_id, it.get("id"), it.get("answer"),
                                       choices))

    rows = []
    for it in items:
        chips = "".join(
            '<button type="button" class="ks3-seg-btn ks3-rung-chip" '
            'data-rung="%s" aria-pressed="false">%s</button>' % (e(c), t(c))
            for c in choices)
        rows.append(
            '<li class="ks3-hardrow" data-item="%s" data-answer="%s">'
            '<p class="ks3-hardrow-item">%s</p>'
            '<div class="ks3-hardrow-chips">%s</div>'
            '<p class="ks3-hardrow-answer" hidden data-reveal>'
            '<strong class="ks3-hardrow-word">%s</strong> %s</p></li>'
            % (e(it.get("id", "")), e(it["answer"]), t(it.get("item", "")),
               chips, t(it["answer"] + "."), rich(it.get("note", ""))))

    counter = a.get("counter") or "{n} of {total} placed"
    return ('<ul class="ks3-hardrows" role="list">%s</ul>'
            '<div class="ks3-hard-foot">'
            '<button type="button" class="ks3-reveal-btn ks3-hard-reveal" '
            'data-hard-reveal disabled>%s</button>'
            '<span class="ks3-hard-progress" data-hard-progress '
            'data-total="%d" data-format="%s">%s</span></div>'
            % ("".join(rows), t(a.get("gate_label") or "Open the answers"),
               len(items), e(counter),
               t(counter.replace("{n}", "0")
                        .replace("{total}", str(len(items))))))


def r_removal_cases(a, act_id):
    """⊕ Keep every cell alive. Remove the organisation.

    Four cases, each a commitment then a consequence. Replaces the retired
    `system-parts` sim, which is why b1-05 has no `.ks3-sim` at all and why the
    parity gate's `sim-unlocked` drive found nothing to unlock on this page.

    ⚠️ CORRECTION TO DESIGN. `caseLevelLost` is `'Level lost: ' + kase.lost`
    and only ONE of the four cases authors `lost`, so Design's own page renders
    **"Level lost: undefined"** on three of them. The pill is omitted when
    there is nothing to name.
    """
    cases = a.get("cases") or []
    if not cases:
        raise ValueError("removal-cases %r declares no cases[]." % act_id)

    tabs = "".join(
        '<button type="button" class="ks3-seg-btn ks3-removal-tab" '
        'data-case="%s" aria-pressed="%s">%s</button>'
        % (e(k["id"]), "true" if i == 0 else "false", t(k.get("label", "")))
        for i, k in enumerate(cases))

    panels = []
    for i, k in enumerate(cases):
        lost = (k.get("lost") or "").strip()
        pill = ('<p class="ks3-removal-lost">%s%s</p>'
                % (t(a.get("lost_prefix") or "Level lost: "), t(lost))
                if lost else "")
        panels.append(
            '<div class="ks3-removal-panel" data-case="%s"%s>'
            '<div class="ks3-removal-what">'
            '<p class="ks3-removal-what-label">%s</p>'
            '<p class="ks3-removal-what-text">%s</p>'
            '<p class="ks3-removal-intact">%s</p></div>'
            '<div class="ks3-removal-predict">'
            '<p class="ks3-commit">%s</p>%s</div>'
            '<div class="ks3-removal-out" hidden data-reveal>%s'
            '<p class="ks3-removal-headline">%s</p>'
            '<p class="ks3-removal-body">%s</p>'
            '<p class="ks3-removal-principle"><strong>%s</strong> %s</p>'
            '</div></div>'
            % (e(k["id"]), "" if i == 0 else " hidden",
               t(a.get("what_label") or "What we did"),
               rich(k.get("what", "")), rich(k.get("intact", "")),
               t(a.get("commit") or "Commit first. What stops working?"),
               r_activity_options(k.get("predict") or []),
               pill, rich(k.get("headline", "")), rich(k.get("body", "")),
               t(a.get("principle_prefix") or "The principle:"),
               rich(k.get("principle", ""))))

    counter = a.get("counter") or "{n} of {total} explored"
    return ('<div class="ks3-removal" data-total="%d">'
            '<p class="ks3-removal-progress" data-removal-progress '
            'data-format="%s">%s</p>'
            '<p class="ks3-removal-lede">%s</p>'
            '<div class="ks3-removal-tabs">%s</div>%s</div>'
            % (len(cases), e(counter),
               t(counter.replace("{n}", "0")
                        .replace("{total}", str(len(cases)))),
               rich(a.get("lede", "")), tabs, "".join(panels)))


def r_system_bench(a, act_id):
    """⊕ SYSTEM's reference screen — four cells, the same seven parts, tuned.

    Rendered as an empty section before this: the payload declares
    `specimens[]` with `job`/`where`/`tuning`/`problem`/`drawing` and the
    generic shell reads none of them.

    Emit-all-show-one, the same shape the seven-tests board uses. Four panels
    and four figures are in the document and one of each is shown, so the DOM
    is the state and going back to a cell finds it as you left it.

    ⚠️ The cell picker is NOT the segmented control, and drift 4 says so
    explicitly: b1-04's light `seg()` branch is `width:100%`, `text-align:left`,
    `min-height:56px`, `--ks3-r-option` — a full-width option ROW that happens
    to share a helper name with the segment. Generating it as a segment would
    produce the wrong component. It gets `.ks3-bench-cell` of its own.
    """
    specimens = a.get("specimens") or []
    if len(specimens) < 2:
        raise ValueError(
            "system-bench %r declares %d specimen(s). The instrument's claim is "
            "that the SAME seven parts are tuned differently, and one cell "
            "cannot show a difference." % (act_id, len(specimens)))
    for sp in specimens:
        if not sp.get("tuning"):
            raise ValueError(
                "system-bench %r specimen %r declares no tuning[] — the bench "
                "would show a cell with nothing turned up or down, which is the "
                "one thing this lesson says never happens."
                % (act_id, sp.get("id")))
        if sp.get("drawing") not in CELL_DRAWINGS:
            raise ValueError(
                "system-bench %r specimen %r asks for drawing %r, which the "
                "engine cannot paint. Known: %s."
                % (act_id, sp.get("id"), sp.get("drawing"),
                   ", ".join(sorted(CELL_DRAWINGS))))

    start = a.get("start") or specimens[0].get("id")
    picker, figures, panels = [], [], []
    for sp in specimens:
        on = sp.get("id") == start
        picker.append(
            '<li><button type="button" class="ks3-bench-cell" data-cell="%s" '
            'aria-pressed="%s">'
            '<span class="ks3-bench-cell-name">%s</span>'
            '<span class="ks3-bench-cell-tag">%s</span></button></li>'
            % (e(sp["id"]), "true" if on else "false",
               t(sp.get("name", "")), t(sp.get("tag", ""))))

        figures.append(
            '<div class="ks3-bench-figure" data-cell="%s"%s>'
            '<canvas class="ks3-bench-canvas" width="1800" height="1120" '
            'data-drawing="%s" role="img" aria-label="%s"></canvas>'
            '<p class="ks3-bench-caption">%s</p></div>'
            % (e(sp["id"]), "" if on else " hidden", e(sp["drawing"]),
               e(sp.get("alt", "")), t(sp.get("caption", ""))))

        dials = "".join(
            '<li class="ks3-tune"><span class="ks3-tune-dial" '
            'data-dial="%s" aria-hidden="true">%s</span>'
            '<span class="ks3-tune-body">'
            '<span class="ks3-tune-part">%s</span>'
            '<span class="ks3-tune-why">%s</span></span></li>'
            % (e(d.get("dial", "")), t(d.get("dial", "")),
               t(d.get("part", "")), rich(d.get("why", "")))
            for d in sp["tuning"])

        panels.append(
            '<div class="ks3-bench-panel" data-cell="%s"%s>'
            '<p class="ks3-bench-eyebrow">Its job</p>'
            '<p class="ks3-bench-job">%s</p>'
            '<p class="ks3-bench-where">%s</p>'
            '<ul class="ks3-tuning" role="list">%s</ul>'
            '<p class="ks3-bench-problem">'
            '<strong>The problem it solves:</strong> %s</p></div>'
            % (e(sp["id"]), "" if on else " hidden",
               rich(sp.get("job", "")), rich(sp.get("where", "")),
               dials, rich(sp.get("problem", ""))))

    return ('<div class="ks3-bench" data-bench-grid="1" data-current="%s">'
            '<ul class="ks3-bench-cells" role="list">%s</ul>'
            '<div class="ks3-bench-main">%s<div class="ks3-bench-read">%s</div>'
            '</div></div>'
            % (e(start), "".join(picker), "".join(figures), "".join(panels)))


# The four cell drawings `shared/ks3.js` can paint, ported verbatim from
# Design's approved b1-04. Named here so the generator can REFUSE a specimen
# that asks for one that does not exist, rather than emitting a blank canvas.
CELL_DRAWINGS = {"red", "root", "sperm", "nerve"}


def r_sabotage(lesson, a, act_id):
    """⊕ Break one thing and follow it out from the cell to the organism.

    The instrument that makes b1-04 a SYSTEM lesson rather than a labelling
    exercise: perturbation over naming. It rendered as an empty section.

    It follows the bench's chosen cell — `bench` names the bench's anchor —
    so every (cell × sabotage) panel is in the document and the pair that is
    showing is the bench's cell and this section's chosen sabotage.

    ⚖️ `named_conditions` is FALSE, ruled by Mide 14 Aug. Design's page carries
    both strings per sabotage and picks between them at RUNTIME from a prop,
    which leaves the named condition in the page source either way. It is
    resolved here, at build time, so `close` never reaches a browser: naming
    hereditary spherocytosis and multiple sclerosis to a Year 7 in a
    cell-biology lesson is what the ruling is about, and shipping it in a
    hidden attribute would honour the letter and miss the point.
    """
    safe = lesson.get("named_conditions") is False
    groups = a.get("specimens") or []
    if not groups:
        raise ValueError("sabotage %r declares no specimens[]." % act_id)

    panels, tabs, total = [], [], 0
    for g in groups:
        cell = g.get("specimen")
        opts = g.get("options") or []
        if not opts:
            raise ValueError(
                "sabotage %r offers cell %r no sabotages — there would be "
                "nothing to break." % (act_id, cell))
        for i, o in enumerate(opts):
            total += 1
            if safe and not (o.get("close_safe") or "").strip():
                raise ValueError(
                    "sabotage %r option %r has no `close_safe`, and this "
                    "lesson sets named_conditions False. The safe copy is the "
                    "one that ships; there is no silent fallback to the named "
                    "one." % (act_id, o.get("id")))
            tabs.append(
                '<button type="button" class="ks3-seg-btn ks3-sab-tab" '
                'data-cell="%s" data-sab="%s" aria-pressed="%s"%s>%s</button>'
                % (e(cell), e(o["id"]), "true" if i == 0 else "false",
                   "" if i == 0 else "", t(o.get("label", ""))))

            chain = "".join(
                '<li class="ks3-chain-link"><p class="ks3-chain-scale">%s</p>'
                '<p class="ks3-chain-text">%s</p></li>'
                % (t(c.get("scale", "")), rich(c.get("text", "")))
                for c in (o.get("chain") or []))

            panels.append(
                '<div class="ks3-sab-panel" data-cell="%s" data-sab="%s" hidden>'
                '<div class="ks3-sab-what">'
                '<p class="ks3-sab-what-label">The sabotage</p>'
                '<p class="ks3-sab-what-text">%s</p></div>'
                '<div class="ks3-sab-predict">'
                '<p class="ks3-commit">%s</p>%s</div>'
                '<div class="ks3-sab-chain" hidden data-reveal>'
                '<div class="ks3-sab-figure">'
                '<canvas class="ks3-sab-canvas" width="1800" height="840" '
                'data-drawing="%s" data-sab="%s" role="img" aria-label="%s">'
                '</canvas>'
                '<p class="ks3-sab-caption">%s</p></div>'
                '<p class="ks3-sab-pick" data-sab-pick></p>'
                '<ol class="ks3-chain" role="list">%s</ol>'
                '<p class="ks3-sab-close">%s</p></div></div>'
                % (e(cell), e(o["id"]), rich(o.get("what", "")),
                   t(a.get("commit") or "Commit first. What breaks first?"),
                   r_activity_options(o.get("predict") or []),
                   e(_drawing_for(lesson, cell)), e(o["id"]),
                   e(o.get("alt", "")), t(o.get("caption", "")),
                   chain,
                   rich((o.get("close_safe") if safe else o.get("close")) or "")))

    lede = a.get("lede") or ""
    head_lede = lede.replace(
        "{specimen}", '<strong data-sab-specimen></strong>')

    return ('<div class="ks3-sab" data-bench-ref="%s" data-total="%d">'
            '<p class="ks3-sab-progress" data-sab-progress>0 of %d sabotages '
            'run</p>'
            '<p class="ks3-sab-lede">%s</p>'
            '<div class="ks3-sab-tabs">%s</div>%s</div>'
            % (e(a.get("bench", "")), total, total, rich(head_lede),
               "".join(tabs), "".join(panels)))


def _drawing_for(lesson, specimen_id):
    """Which drawing a sabotage's broken canvas paints — the cell's own."""
    for act in lesson.get("activities") or []:
        if act.get("kind") != "system-bench":
            continue
        for sp in act.get("specimens") or []:
            if sp.get("id") == specimen_id:
                return sp.get("drawing", "")
    raise ValueError(
        "sabotage names specimen %r, which the bench does not declare. The two "
        "instruments share a cast and this one is off it." % specimen_id)


def r_settles_it(a, act_id):
    """⊕ CONTRAST's flagship — sixteen judgements, and most of them decide nothing.

    Four mystery cells, four true facts each. The student marks every fact
    SETTLES IT or SETTLES NOTHING before anything is revealed. Most settle
    nothing, because they are true of single-celled organisms AND of cells
    inside a body, and the discriminating fact is never the most interesting
    one — cell 4 changes shape and engulfs another cell, and both settle
    nothing, because a white blood cell does both. Discriminators run 1, 2, 2,
    2 so the pattern never degrades into "find the one".

    Before this it rendered as an **empty section**: `r_activity` emitted the
    shell, the eyebrow and the heading and stopped, because the generic shell
    reads `prompt`/`options`/`reveal` and this payload declares
    `instruction`/`choice_labels`/`cases`. Not one of the sixteen judgements
    reached the page. The kind is inherited by 18 CONTRAST lessons.

    ⚖️ MRB-196, ruled by Mide 13 Aug, resolves the inventory's F36. Design
    computes whether the student agreed and then spends it on the why
    paragraph's COLOUR — `--ks3-ink` against `--ks3-ink-body`, about 6 ΔL*
    apart — which is a mark nobody can read and, being a mark at all, sits
    badly beside R3. The computation goes, the why paragraph takes one tone,
    and the self-check asks the student directly. Same shape as the rail on
    MRB-208: where the approved page and a ruling collide, the ruling wins.

    R3 is safe by construction and worth stating, because it looks close to
    the line. The row's ground records whether the FACT settles it — the
    page's own answer, revealed to everyone identically — never whether the
    student said so. The choice buttons carry the chosen tint and nothing
    else, and they are not `.ks3-option`s, so the reveal may disable them
    without failing R3's runtime assertion.
    """
    cases = a.get("cases") or []
    labels = a.get("choice_labels") or []
    openers = a.get("why_openers") or []
    if len(cases) < 2:
        raise ValueError(
            "settles-it %r declares %d case(s). The instrument is a "
            "discrimination exercise and one case cannot discriminate."
            % (act_id, len(cases)))
    if len(labels) != 2:
        raise ValueError(
            "settles-it %r needs exactly two choice_labels — the two things a "
            "fact can do. Got %r." % (act_id, labels))
    if len(openers) != 2:
        raise ValueError(
            "settles-it %r needs exactly two why_openers, the SETTLES and the "
            "SETTLES-NOTHING word, in that order. Got %r." % (act_id, openers))

    for k in cases:
        feats = k.get("features") or []
        if not feats:
            raise ValueError("settles-it %r case %r declares no features."
                             % (act_id, k.get("id")))
        for f in feats:
            if "settles" not in f:
                raise ValueError(
                    "settles-it %r case %r has a feature with no `settles` "
                    "verdict: %r. Every fact is either the one that decides it "
                    "or one that does not, and the whole exercise is telling "
                    "them apart." % (act_id, k.get("id"), f.get("text")))
            if not (f.get("why") or "").strip():
                raise ValueError(
                    "settles-it %r case %r feature %r has no `why`. The reveal "
                    "exists to say what settles each one."
                    % (act_id, k.get("id"), f.get("text")))
        if not sum(1 for f in feats if f.get("settles")):
            raise ValueError(
                "settles-it %r case %r has no discriminating feature at all — "
                "nothing settles it, so the case has no answer."
                % (act_id, k.get("id")))

    fmt = a.get("progress_format") or "{n} of {total} marked"
    tabs = "".join(
        '<button type="button" class="ks3-seg-btn ks3-case-tab" '
        'data-case="%s" aria-pressed="%s">%s</button>'
        % (e(k["id"]), "true" if i == 0 else "false",
           t(k.get("tab_label") or k.get("label", "")))
        for i, k in enumerate(cases))

    panels = []
    for i, k in enumerate(cases):
        feats = k.get("features") or []
        rows = []
        for f in feats:
            settles = bool(f.get("settles"))
            choices = "".join(
                '<button type="button" class="ks3-settle-choice" '
                'data-pick="%s" aria-pressed="false">%s</button>'
                % (pick, t(lab))
                for pick, lab in (("yes", labels[0]), ("no", labels[1])))
            rows.append(
                '<li class="ks3-feature" data-settles="%d">'
                '<p class="ks3-feature-text">%s</p>'
                '<div class="ks3-feature-choices">%s</div>'
                '<p class="ks3-feature-why" hidden data-reveal>'
                '<strong class="ks3-why-word">%s</strong> %s</p></li>'
                % (1 if settles else 0, rich(f.get("text", "")), choices,
                   t(openers[0] if settles else openers[1]), rich(f["why"])))

        panels.append(
            '<div class="ks3-case-panel" data-case="%s"%s>'
            '<div class="ks3-case-head">'
            '<p class="ks3-case-label">%s</p>'
            '<p class="ks3-case-desc">%s</p></div>'
            '<ul class="ks3-features" role="list">%s</ul>'
            '<div class="ks3-settle-foot">'
            '<button type="button" class="ks3-reveal-btn ks3-settle-reveal" '
            'data-settle-reveal disabled>%s</button>'
            '<span class="ks3-settle-progress" data-settle-progress '
            'data-total="%d" data-format="%s" data-opened="%s">%s</span></div>'
            '<div class="ks3-case-verdict" hidden data-case-verdict>'
            '<p class="ks3-case-verdict-label">%s</p>'
            '<p class="ks3-case-answer">%s</p>'
            '<p class="ks3-case-why">%s</p></div></div>'
            % (e(k["id"]), "" if i == 0 else " hidden",
               t(k.get("label", "")), rich(k.get("description", "")),
               "".join(rows),
               t(a.get("reveal_label") or "Show what settles it"),
               len(feats), e(fmt), e(a.get("progress_opened") or "Opened"),
               t(fmt.replace("{n}", "0").replace("{total}", str(len(feats)))),
               t(k.get("verdict_label", "")), rich(k.get("answer", "")),
               rich(k.get("why", ""))))

    return ('<div class="ks3-case-tabs" role="list">%s</div>%s%s'
            % (tabs, "".join(panels), _self_check(a, act_id)))


def _self_check(a, act_id):
    """MRB-196's self-check, shared by the sorter and settles-it.

    Extracted rather than written twice: it is one component, ruled once, and
    two copies is how one copy quietly stops obeying the rule below.

    There is no `answer` key and there must never be one. The student is asked
    how many of their OWN judgements matched, and only the student knows. A
    right answer here would put a mark on an activity option, which R3 forbids.
    """
    sc = a.get("self_check")
    if not sc:
        return ""
    if "answer" in sc:
        raise ValueError(
            "%r's self_check carries an `answer` key. It must not: only the "
            "student knows how many of their own marks matched, and a right "
            "answer here would mark an activity option, which R3 forbids."
            % act_id)
    opts = "".join(_option_li(i, o, ' aria-pressed="false"')
                   for i, o in enumerate(sc.get("options") or []))
    note = ('<p class="ks3-selfcheck-note">%s</p>' % rich(sc["note"])
            if sc.get("note") else "")
    return ('<div class="ks3-selfcheck" data-selfcheck hidden>'
            '<p class="ks3-selfcheck-q">%s</p>'
            '<ul class="ks3-options ks3-selfcheck-options" role="list">%s</ul>'
            '%s</div>' % (t(sc.get("question", "")), opts, note))


def _quoted(s):
    """“…” exactly once, whatever the author supplied.

    Six agents authored six lessons in parallel and drifted on this: b1-03
    writes its quotes with the curly marks inside the string, b1-04, b1-05 and
    b1-06 write them bare, and the register's statements are bare too. Design
    draws “…” on every one. Stripping first and re-wrapping is the only version
    that is right for all three inputs — wrapping unconditionally double-quotes
    half the delivery, and trusting the author leaves the other half naked.
    """
    return "“%s”" % (s or "").strip().strip("“”\"")


def _confrontations(lesson, a):
    """Normalise the three authored shapes of a confrontation into one list.

    Each entry is `{quote, body: [str], key_fact}`. The shapes, all live:

      b1-01  `statements: ["…"]`                       — a bare string
      b1-03  `statements: [{quote, body: [str], …}]`   — body as a list
      b1-04  `statements: [{quote, answer: "…"}]`      — body as one string
      b1-02  no statements; `paragraphs: [str]`        — quote from the register
      C1     no statements; `prompt` + `reveal`        — quote from the register

    The register fallback is what keeps C1's seven confrontations rendering
    exactly as they do today: none of them carries any of the new keys, so all
    of them take the last branch and nothing about their markup moves.
    """
    out = []
    for st in (a.get("statements") or []):
        if isinstance(st, str):
            out.append({"quote": st, "body": [], "key_fact": None})
            continue
        body = st.get("body")
        if body is None:
            body = [st["answer"]] if st.get("answer") else []
        elif isinstance(body, str):
            body = [body]
        out.append({"quote": st.get("quote", ""), "body": list(body),
                    "key_fact": st.get("key_fact")})

    if not out:
        # No authored statement: the wrong idea comes from the register, named
        # by `targets`, and `paragraphs` (if any) is its body.
        quote = _misconception_quote(lesson, a.get("targets"))
        paras = list(a.get("paragraphs") or [])
        if quote or paras:
            out.append({"quote": quote, "body": paras, "key_fact": None})
    elif a.get("paragraphs"):
        raise ValueError(
            "Activity %r carries BOTH statements[] and paragraphs[]. "
            "`paragraphs` is the body of a register-derived confrontation and "
            "has no owner once statements[] names its own — the words would "
            "render after the last quote and read as belonging to it."
            % a.get("id"))
    return out


def r_confrontation(lesson, a, act_id):
    """⊕ The misconception block's real content. Design drew it; nothing read it.

    `confrontation` was declared GENERIC — a claim that prompt/options/reveal
    IS its drawn component. That is true of C1's seven, which carry exactly
    those keys. It is false of all six of B1's, and the cost was measured
    rather than argued: **b1-03's whole `#s-think` section rendered as
    `! Think again` and nothing else** — 231 characters of markup, both
    authored statements dropped, and no `targets` either so not even a register
    quote. That is an empty block on the approved reference screen for MODEL, a
    family carrying 50 lesson slots.

    b1-01 is the subtler case and the more dangerous one, because it rendered
    something and therefore looked finished: the line a student read was the
    register's (“If something moves on its own it must be alive…”) and not the
    one Design drew (“If it moves and grows, it must be alive.”). The authored
    comment in the record says so in as many words — *"They differ here… and
    the page's line is the one that renders"* — and the build did the opposite.
    So an authored statement now WINS over the register; the register is the
    fallback for a block that names no statement of its own.

    Design draws a second confrontation behind an amber-topped divider rather
    than as a second block: one wrong idea, then another, inside one "Think
    again". The divider is `--ks3-alert-border`, which is the one place amber
    is right — this is a wrong idea being confronted, which is exactly what
    §8's amber is reserved for.
    """
    parts = []
    for i, c in enumerate(_confrontations(lesson, a)):
        if i:
            parts.append('<div class="ks3-mis-next">')
        if c["quote"]:
            parts.append('<p class="ks3-mis-quote">%s</p>' % t(_quoted(c["quote"])))
        for para in c["body"]:
            parts.append('<p class="ks3-mis-body">%s</p>' % rich(para))
        if c["key_fact"]:
            # The box lives once in `key_facts[]` and is named here by id, so a
            # correction to the line cannot be applied to one copy and not the
            # other. `r_key_fact` already resolves `ref` by id or by index.
            parts.append(r_key_fact(lesson, {"ref": c["key_fact"]}))
        if i:
            parts.append("</div>")
    return "".join(parts)


def r_scorecards(cards):
    """The two-up figure cards. b1-01's whole teaching point, rendered nowhere.

    “6 of 7 · Candle flame — not alive” against “3 of 7 · Oak seed — alive” is
    the beat the lesson turns on: the higher score is the dead one. The block
    kept its prompt, which SAYS that, and lost the cards that show it.

    The figure is mono 32px because it is a reading off an instrument, not a
    heading — the same reason every live readout in the key stage is mono.

    ⚠️ The STYLESHEET for this already existed — `.ks3-scorecards` and its three
    children have been in `shared/ks3.css` since B1 round two. Only the renderer
    was missing, so the CSS matched nothing on any page. That is the exact
    mirror of the seven-tests board, where the renderer exists and the
    stylesheet has nothing for any of its 44 classes. Neither half is a
    component on its own, and a gate that measures registration rather than
    rendering cannot tell the difference.
    """
    out = []
    for c in cards:
        if not c.get("figure"):
            raise ValueError(
                "A scorecard with no `figure` is a card with no reading on it "
                "— the figure is the whole point of the comparison.")
        out.append('<li>'
                   '<p class="ks3-scorecard-fig">%s</p>'
                   '<p class="ks3-scorecard-title">%s</p>'
                   '<p class="ks3-scorecard-note">%s</p></li>'
                   % (t(c["figure"]), t(c.get("title", "")),
                      rich(c.get("note", ""))))
    return ('<ul class="ks3-scorecards" role="list">%s</ul>' % "".join(out))


def _option_li(i, text, extra=""):
    """One answer button. The letter badge is the resting mark (R2/§5).

    Shared by activities and the ladder so the two are the same control, and
    the ONLY difference between them is the attributes: an activity option
    takes `aria-pressed` and shows that it was chosen; a ladder option takes
    `data-correct` and `data-feedback` and gets marked. R3 lives in that gap —
    if `data-correct` ever appears on an activity option, the student reads the
    whole page as a test and committing before revealing loses its point.
    """
    return ('<li><button type="button" class="ks3-option" data-i="%d"%s>'
            '<span class="ks3-opt-mark" aria-hidden="true">%s</span>'
            '<span class="ks3-opt-label">%s</span></button></li>'
            % (i, extra, option_letter(i), t(text)))


def r_activity_options(options):
    """R3: chosen, never correct. No data-correct, no green, never disabled."""
    return ('<ul class="ks3-options" role="list">%s</ul>'
            % "".join(_option_li(i, o, ' aria-pressed="false"')
                      for i, o in enumerate(options)))


# The four FIFA steps as the OLD dict shape names them, in method order. Kept
# as data rather than a hard-coded run of four `<p>`s so the two shapes go
# through one renderer and cannot drift apart.
def r_fifa(fifa, staged=False, buttons=None):
    """FIFA, in ONE layout — the chipped one (⊕ MRB-242 ruling 2).

    `activities[].fifa` is a LIST of `{letter, label|name, line, note}`, so a
    worked example can name its own steps ("Fine-tune", not "Fix") and hang a
    teaching note on each — which MRB-204 step 3 needs.

    ⊕ MRB-242 RETIRES THE INLINE VARIANT. There used to be two: a step that
    authored `label` took Design's drawn treatment (letter chip, mono label,
    display line, note underneath) and a step that authored `name` took a
    run-on `<p>`. That was not a choice anyone made per page — it was whichever
    key the author happened to reach for, so b1-02 and b2-04 rendered the same
    construct two different ways. The inline variant also concatenated `line`
    and `note` with NO separator at all, which is why b1-02 shipped the words
    "…eyepiece × objectiveWritten down before any numbers."

    `label` and `name` mean the same thing and both are read. The note is now
    always its own `<p>`, so the concatenation defect is not fixed so much as
    made unreachable: there is no longer a code path that puts two strings next
    to each other.

    ⊕ The LETTER is what makes a step a FIFA step, and the chip is emitted only
    when there is one. B3's three sum ledgers ("4 slices toast and butter =
    3120 kJ") author a name and a line and no letter, because they are running
    totals, not F-I-F-A. They keep this markup and take compact ledger metrics
    from `.ks3-fifa-sum` rather than being inflated into 26px display panels —
    one layout, not a second variant wearing the same key.

    The old dict shape (`{formula, insert, fix, answer}`) is gone: no lesson
    authors it. It is in git history if it is ever wanted back.
    """
    steps = list(fifa or [])

    out, lettered = [], False
    for i, s in enumerate(steps):
        # ⚠️ An element that ships `hidden` must not be given a `display` by
        # any author rule — see `.ks3-fifa-chipped[hidden]` in shared/ks3.css
        # and the gate in verify_ks3.py. This is where the attribute is
        # written; that is where it was being undone.
        hide = ' hidden data-step="%d"' % i if staged else ""
        letter = s.get("letter") or ""
        if letter:
            lettered = True
        chip = ('<span class="ks3-fifa-chip" aria-hidden="true">%s</span>'
                % t(letter)) if letter else ""
        note = ('<p class="ks3-fifa-stepnote">%s</p>' % rich(s["note"])
                if s.get("note") else "")
        out.append(
            '<div class="ks3-fifa-step ks3-fifa-chipped"%s>%s'
            '<div class="ks3-fifa-body">'
            '<p class="ks3-fifa-label">%s</p>'
            '<p class="ks3-fifa-line">%s</p>%s</div></div>'
            % (hide, chip, t(s.get("label") or s.get("name") or ""),
               t(s.get("line") or ""), note))
    # A letterless run is a sum ledger; `.ks3-fifa-sum` gives it back the
    # compact metrics it had as a paragraph list, inside the shared markup.
    shape = " ks3-fifa-chips" + ("" if lettered else " ks3-fifa-sum")
    if not staged:
        return '<div class="ks3-fifa%s">%s</div>' % (shape, "".join(out))
    b = buttons or {}
    # ⊕ The done-note (map N5): Design's *"Now the same four steps on the other
    # reaction."* appears beside the button once every step is out. It had no
    # field, so the sentence that hands the student on to `#s-build` reached
    # nobody.
    done_note = ('<span class="ks3-step-donenote" hidden data-step-donenote>'
                 '%s</span>' % t(b["done_note"])) if b.get("done_note") else ""
    return ('<div class="ks3-fifa ks3-fifa-staged%s" data-stepper '
            'data-total="%d" data-next="%s" data-done="%s">%s'
            '<div class="ks3-fifa-foot">'
            '<button type="button" class="ks3-reveal-btn ks3-step-next" '
            'data-step-next>%s</button>%s</div></div>'
            % (shape,
               len(out), e(b.get("next", "Show the next step")),
               e(b.get("done", "All steps shown")), "".join(out),
               t(b.get("first", "Show the first step")), done_note))


def r_criteria(success):
    """A button and a hidden panel — Design replaced the old <details>.

    <details> gave the student a summary they could open before writing
    anything and a marker triangle that reads as decoration. A real button with
    `aria-expanded` says what it does, takes the same focus ring as every other
    control (R15), and is the thing ks3.js toggles.
    """
    items = "".join(
        '<li class="ks3-crit"><span class="ks3-crit-num" aria-hidden="true">%d'
        '</span><span>%s</span></li>' % (i, t(s))
        for i, s in enumerate(success, 1))
    return ('<button type="button" class="ks3-reveal-btn" data-criteria-btn '
            'aria-expanded="false">Check your answer</button>'
            '<div class="ks3-crit-wrap" hidden data-criteria>'
            '<p class="ks3-crit-lead">Did you say all of these?</p>'
            '<ul class="ks3-crit-list" role="list">%s</ul></div>' % items)


# ── B2 · Movement (⊕ 16 Aug 2026, MRB-220) ───────────────────────────────
#
# Seven new instruments and two shared pieces. The shared pieces come first
# because three of the seven use them:
#
#   `head_counter`  — Design's B2 blocks put a live progress readout on the
#                     SAME ROW as the eyebrow and the <h2>, right-aligned. The
#                     shell's fixed `eyebrow / h2 / prompt` stack cannot make
#                     that row, and moving the counter below the lede would put
#                     "0 of 6 decided" where the instruction goes.
#   `gate`          — b2-02, b2-03 and b2-04 all gate the flagship instrument
#                     behind a four-option commitment that DISAPPEARS when
#                     answered (C6). One renderer, one wiring, three lessons.
#
# ⚠️ A dispatch-table entry is not a component. Every kind below has markup
# here, real rules in `shared/ks3.css`, real behaviour in `shared/ks3.js`
# reached from `wireInstruments()`, and a registered assertion in
# `ks3_parity.COMPONENTS` measured on a page that renders it.


def _head_counter(spec):
    """The block-head progress readout: a count, or a two-state label.

    Three shapes because Design authored three. b2-01/02/03 count ("3 of 6
    decided"); b2-04's rig and meter blocks are booleans ("Meter not fitted
    yet" → "Meter fitted"); c2-01's is a count with a bespoke zero ("All three
    claims on" → "2 switched off"). One element, one JS updater, so a fourth
    cannot arrive as a fourth copy of the same paragraph.

    ⊕ `constants` / `start` / `start_extra` (MRB-220, C2) let one format string
    carry more than one live number — c2-02's budget line quotes three — while
    keeping every value authored exactly once.
    """
    if spec.get("format"):
        total = int(spec.get("total") or 0)
        fmt = spec["format"]
        # ⊕ `constants` — placeholders that never move, BAKED INTO THE FORMAT
        # at build time. c2-02's readout is "{left} of {budget} tests left ·
        # {n} of 6 decided": the budget is a fixed teaching dial and only
        # `left` and `n` are live, so baking it keeps the runtime to the two
        # numbers it can actually compute and keeps `budget` authored once.
        for k, v in sorted((spec.get("constants") or {}).items()):
            fmt = fmt.replace("{%s}" % k, str(v))
        # ⊕ `start` — the count the readout OPENS on, before any JS runs. Every
        # B2 counter opens on nothing done and so opens at 0; c2-01's zoom
        # opens on step one of five, because a student is already looking at a
        # level. Without this the resting page reads "0 of 5 steps" for the
        # instant before `wireScaleZoom` corrects it, which is a wrong number
        # on screen and a wrong number in the HTML a search engine reads.
        first = (fmt.replace("{n}", str(int(spec.get("start") or 0)))
                 .replace("{total}", str(total)))
        # `start_extra` fills the live placeholders that are not the count, for
        # the resting render only. The runtime recomputes them.
        for k, v in sorted((spec.get("start_extra") or {}).items()):
            first = first.replace("{%s}" % k, str(v))
        spec = dict(spec, format=fmt)
        # ⊕ MRB-220 / C2 — a THIRD variant, and the reason this is one element
        # with one JS updater rather than three paragraphs. c2-01's readout is
        # a count with a bespoke zero: "All three claims on", then "2 switched
        # off". Neither the count shape nor the two-state shape says that.
        # `zero` is opt-in, so every shipped counter still opens on its own
        # "0 of 6 decided".
        # ⊕ `tone` — c2-02's budget line is the one counter in the key stage
        # Design paints in `--ks3-accent-text` rather than ink-muted, because
        # it is a resource running down and not a tally going up. An attribute
        # rather than a class so `.ks3-blockhead-count` stays one component.
        tone = (' data-tone="%s"' % e(spec["tone"])) if spec.get("tone") else ""
        if spec.get("zero"):
            return ('<p class="ks3-blockhead-count" data-count data-format="%s" '
                    'data-zero="%s" data-total="%d"%s>%s</p>'
                    % (e(spec["format"]), e(spec["zero"]), total, tone,
                       t(spec["zero"])))
        return ('<p class="ks3-blockhead-count" data-count data-format="%s" '
                'data-total="%d"%s>%s</p>'
                % (e(spec["format"]), total, tone, t(first)))
    if not (spec.get("off") and spec.get("on")):
        raise ValueError(
            "head_counter needs either `format` (+ `total`) or both `off` and "
            "`on`; got %s" % sorted(spec))
    return ('<p class="ks3-blockhead-count" data-count data-off="%s" '
            'data-on="%s">%s</p>'
            % (e(spec["off"]), e(spec["on"]), t(spec["off"])))


def r_bench_gate(gate):
    """C6's commit gate — four options, then the gate is GONE.

    Gating by ABSENCE, not by disable: Design removes the whole block when it
    is answered rather than greying it, so the instrument arrives in the space
    the question was occupying. `wireBenchGate` hides this and unhides
    `[data-benchbody]`; nothing else on the page can open it.
    """
    if not gate:
        return "", ""
    return ('<div class="ks3-benchgate" data-benchgate>'
            '<p class="ks3-commit">%s</p>%s</div>'
            % (t(gate.get("prompt", "")),
               r_activity_options(gate.get("options") or [])),
            ' hidden data-benchbody')


def r_job_sort(a, act_id):
    """⊕ b2-01 `#s-sort` · b2-02 `#s-cases` · b2-03 `#s-pairs`.

    The per-item sorter, and the unit's highest-reuse component: 14 authored
    items across three lessons. It is NOT `sort-task` and NOT `sort-rows`, and
    the difference is the whole pedagogy — both of those gate every row behind
    one "open the answers" button, and this one reveals EACH ROW THE INSTANT
    THAT ROW IS DECIDED. A student finds out about item 1 before committing on
    item 2, which is what makes the sequence teach.

    ⚠️ NO ANSWER VALIDATION, deliberately. `sort-task` asserts every item's
    `answer` is one of the offered choices, and b2-01's item `i4` answers
    "Movement and protection — both." — a fifth string that is not one of the
    four jobs, and is the whole point of that item. Validating here would
    refuse Design's payload at build time.

    ⚠️ R3 / MRB-196 R10. Nothing marks correctness: the chosen option keeps
    the ordinary chosen treatment, the unchosen ones dim, the ROW's border
    goes to ink, and the why paragraph is one tone whether the student had it
    or not. Do not add a verdict here for tidiness — the sorter is a sequence
    of commitments, not a test.
    """
    items = a.get("items") or []
    if not items:
        raise ValueError("job-sort %r declares no items[]." % act_id)
    shared = [c.get("label", "") for c in (a.get("categories") or [])]

    rows = []
    for it in items:
        labels = it.get("options") or shared
        if not labels:
            raise ValueError(
                "job-sort %r item %r offers no options and the activity "
                "declares no shared categories[]." % (act_id, it.get("id")))
        opts = "".join(
            '<button type="button" class="ks3-jobsort-opt" data-i="%d" '
            'aria-pressed="false">%s</button>' % (i, t(lab))
            for i, lab in enumerate(labels))
        rows.append(
            '<li class="ks3-jobsort-item" data-item="%s">'
            '<p class="ks3-jobsort-text">%s</p>'
            '<div class="ks3-jobsort-opts">%s</div>'
            '<p class="ks3-jobsort-why" hidden data-reveal>'
            '<strong class="ks3-jobsort-answer">%s</strong> %s</p></li>'
            % (e(it.get("id", "")), t(it.get("text", "")), opts,
               t(it.get("answer", "")), rich(it.get("why", ""))))

    close = ('<div class="ks3-jobsort-close" hidden data-jobsort-close>'
             '<p>%s</p></div>' % rich(a["close_all"])) if a.get("close_all") else ""
    return ('<div class="ks3-jobsort" data-jobsort data-total="%d">'
            '<ul class="ks3-jobsort-list" role="list">%s</ul>%s</div>'
            % (len(items), "".join(rows), close))


def r_system_switch(a, act_id):
    """⊕ b2-01 `#s-switch` — take one part away and follow the damage.

    Close to `sabotage` and not the same component. Three measured
    differences, any one of which is fatal:

      * `sabotage` is CAST-COUPLED — `_drawing_for()` raises unless a
        `system-bench` on the same page declares the specimen. b2-01 has no
        bench and no cells.
      * `sabotage` paints a `<canvas data-drawing>` per panel from
        `CELL_DRAWINGS`. B2 is deliberately drawing-free (NOTES flag 17: no
        anatomical diagrams anywhere in the unit).
      * `sabotage` renders the ink-dark `practical` shell. `#s-switch` is a
        LIGHT `.ks3-block` with an ink-dark panel inside it, after the reveal.

    Emit-all-show-one, the same trick the board uses: four panels in the
    document, one shown, so going back to a part finds it as you left it and
    no state lives anywhere but the DOM.

    ⊕ `show_levels: False` OMITS the chip and collapses the grid. Design's own
    page keeps rendering an empty pill in a 104px column that holds nothing —
    a prop that half works. Nothing in B2 authors it; the branch exists so the
    prop means what it says the day a lesson wants it.
    """
    parts_ = a.get("parts") or []
    if not parts_:
        raise ValueError("system-switch %r declares no parts[]." % act_id)
    show_levels = a.get("show_levels") is not False
    labels = a.get("labels") or {}

    tabs = "".join(
        '<button type="button" class="ks3-seg-btn ks3-switch-tab" '
        'data-part="%s" aria-pressed="%s">%s</button>'
        % (e(p["id"]), "true" if i == 0 else "false", t(p.get("tab", "")))
        for i, p in enumerate(parts_))

    panels = []
    for i, p in enumerate(parts_):
        opts = "".join(_option_li(j, o, ' aria-pressed="false"')
                       for j, o in enumerate(p.get("options") or []))
        chain = []
        for st in p.get("chain") or []:
            level = st.get("level") or ""
            # Chip colour is a function of the LEVEL STRING, not of position:
            # the chains do not all climb (femur ends at Cell, marrow starts
            # and ends there), so the chip can never be a rendering of index.
            chip = ('<span class="ks3-switch-chip" data-level="%s">%s</span>'
                    % (e(level.lower()), t(level))) if show_levels else ""
            chain.append('<div class="ks3-switch-row"%s>%s'
                         '<p class="ks3-switch-step">%s</p></div>'
                         % ("" if show_levels else ' data-nolevel="1"',
                            chip, rich(st.get("text", ""))))
        panels.append(
            '<div class="ks3-switch-panel" data-part="%s"%s>'
            '<div class="ks3-switch-what">'
            '<p class="ks3-switch-name">%s</p>'
            '<p class="ks3-switch-does">%s</p></div>'
            '<div class="ks3-switch-predict"><p class="ks3-commit">%s</p>'
            '<ul class="ks3-options" role="list">%s</ul></div>'
            '<div class="ks3-switch-foot">'
            '<button type="button" class="ks3-reveal-btn ks3-switch-btn" '
            'data-switch data-done-label="%s" disabled>%s</button>'
            '<span class="ks3-switch-hint" data-switch-hint>%s</span></div>'
            '<div class="ks3-switch-chain" hidden data-switch-chain>'
            '<p class="ks3-switch-title">%s</p>'
            '<div class="ks3-switch-rows">%s</div>'
            '<p class="ks3-switch-close">%s</p></div></div>'
            % (e(p["id"]), "" if i == 0 else " hidden",
               t(p.get("name", "")), rich(p.get("does", "")),
               t(p.get("prompt", "")), opts,
               e(labels.get("switched") or "Switched off"),
               t(labels.get("switch") or "Switch this part off"),
               t(labels.get("hint_locked") or ""),
               t(p.get("title", "")), "".join(chain),
               rich(p.get("close", ""))))

    close = ('<div class="ks3-switch-all" hidden data-switch-all><p>%s</p>'
             '</div>' % rich(a["close_all"])) if a.get("close_all") else ""
    return ('<div class="ks3-switch" data-switch-block data-total="%d" '
            'data-hint-ready="%s" data-hint-done="%s">'
            '<div class="ks3-switch-tabs">%s</div>%s%s</div>'
            % (len(parts_), e(labels.get("hint_ready") or ""),
               e(labels.get("hint_done") or ""), tabs, "".join(panels), close))


def _joint_payload(a, act_id):
    """The joint bench's data, as JSON the canvas engine reads.

    Everything the drawing needs is a function of `bend[]` and `twist`, which
    is what makes this the one genuinely parametric instrument in the unit —
    the sweep, the joint glyph, the seam and the twist verdict are all
    derived. Nothing here is a per-joint magic number except the two Design
    authored: the bend range and the starting angle.
    """
    joints = a.get("joints") or []
    if not joints:
        raise ValueError("joint-bench %r declares no joints[]." % act_id)
    out = []
    for j in joints:
        bend = list(j.get("bend") or [0, 0])
        if len(bend) != 2:
            raise ValueError(
                "joint-bench %r joint %r declares bend=%r; it takes exactly "
                "[min, max] in degrees." % (act_id, j.get("id"), bend))
        out.append({
            "id": j["id"], "name": j.get("name", ""),
            "bend": [int(bend[0]), int(bend[1])],
            "twist": bool(j.get("twist")),
            # ⚠️ The starting angle lives ON THE JOINT, not in a
            # `{joint_id: angle}` map beside it. Design authors the map; a map
            # keyed by id makes every joint's NAME a dict key, and a key that
            # is only ever reached by iterating is invisible to
            # `ks3_key_audit.py` — which reported `pivot` as authored-and-
            # unread, correctly, because nothing in the engine ever needs to
            # say the word. Put on the joint it is a schema field with one read
            # site, and the audit is right about it either way.
            "start": int(j.get("start", bend[0])),
            "axes": j.get("axes", ""), "where": j.get("where", ""),
            "hold": j.get("hold", ""), "trade": j.get("trade", ""),
            "angle_label": j.get("angle_label", ""),
            "twist_yes": j.get("twist_yes", ""),
            "twist_no": j.get("twist_no", ""),
        })
    return out


def r_joint_bench(a, act_id):
    """⊕ b2-02 `#s-bench` — a two-bone linkage, drawn from the data.

    The nearest shipped canvas engines are the microscope and the four
    `CELL_DRAWINGS`, which are a fixed enum of portraits. This is not that: a
    joint whose allowed sweep, glyph radius, groove, seam and twist verdict
    are all computed from `bend[]` and `twist` is a drawing of the payload,
    and adding a fifth joint needs no new drawing code.

    ⚠️ The REFUSAL IS DRAWN, and that is the lesson. A pivot and a fixed joint
    get a disabled slider, the literal readout `locked`, and a label that says
    the joint does not bend — three coordinated readouts. A generic range
    control gives none of them, which is why this is not `sim`.
    """
    joints = _joint_payload(a, act_id)
    labels = a.get("labels") or {}
    alt = a.get("alt") or {}
    locked_word = labels.get("locked") or "locked"
    first = joints[0]
    gate_html, hide = r_bench_gate(a.get("gate"))

    tabs = "".join(
        '<button type="button" class="ks3-sim-seg-btn ks3-joint-tab" '
        'data-joint="%s" aria-pressed="%s">%s</button>'
        % (e(j["id"]), "true" if i == 0 else "false", t(j.get("tab", "")))
        for i, j in enumerate(a.get("joints") or []))

    def tile(label, key, value, mono=False):
        return ('<div class="ks3-joint-tile">'
                '<p class="ks3-joint-tile-label">%s</p>'
                '<p class="ks3-joint-tile-value%s" data-tile="%s">%s</p>'
                '</div>' % (t(label), " ks3-joint-tile-mono" if mono else "",
                            e(key), t(value)))

    # The resting readouts are rendered from the FIRST joint here rather than
    # left blank for JS to fill: a page with JS still loading must never show
    # an instrument full of empty boxes, and the values are known at build
    # time. `wireJointBench` repaints the same elements from the same data.
    first_note = ((labels.get("twist_idle") or "") if first["twist"]
                  else first["twist_no"])
    body = (
        '<div class="ks3-joint" data-jointbench%s data-total="%d" '
        'data-joints="%s" data-alt="%s" data-alt-can="%s" data-alt-cannot="%s" '
        'data-locked="%s" data-twist-off="%s" data-twist-on="%s" '
        'data-twist-idle="%s">'
        '<div class="ks3-joint-tabs">%s</div>'
        '<div class="ks3-joint-stage">'
        '<canvas class="ks3-joint-canvas" width="1800" height="740" '
        'role="img" aria-label="%s" data-joint-canvas></canvas>'
        '<div class="ks3-joint-controls">'
        '<div class="ks3-joint-anglerow">'
        '<label class="ks3-joint-anglelabel" for="%s-angle" data-angle-label>'
        '%s</label>'
        '<p class="ks3-joint-anglevalue" data-angle-value>%s</p></div>'
        '<input class="ks3-slider" type="range" id="%s-angle" min="%d" '
        'max="%d" step="1" value="%d" data-angle%s>'
        '<div class="ks3-joint-twistrow">'
        '<button type="button" class="ks3-sim-seg-btn ks3-joint-twist" '
        'data-twist aria-pressed="false">%s</button>'
        '<p class="ks3-joint-twistnote" data-twist-note>%s</p>'
        '</div></div></div>'
        '<div class="ks3-joint-tiles">%s%s%s</div>'
        '<p class="ks3-joint-trade"><strong>%s</strong> '
        '<span data-tile="trade">%s</span></p></div>'
        % (hide, len(joints),
           # `ensure_ascii=False` so the attribute carries the real
           # characters — an em dash written as `\\u2014` round-trips
           # correctly through JSON.parse but is unreadable in
           # view-source and invisible to a byte-identity grep.
           e(json.dumps(joints, separators=(",", ":"), sort_keys=True,
                        ensure_ascii=False)),
           e(alt.get("template", "")), e(alt.get("can", "")),
           e(alt.get("cannot", "")), e(locked_word),
           e(labels.get("twist") or ""), e(labels.get("twisting") or ""),
           e(labels.get("twist_idle") or ""),
           tabs,
           e(_joint_alt(alt, first, first["start"])),
           e(act_id), t(first["angle_label"]),
           t("%d°" % first["start"] if first["bend"][1] > 0 else locked_word),
           e(act_id), first["bend"][0], first["bend"][1] or 1, first["start"],
           " disabled" if first["bend"][1] == 0 else "",
           t(labels.get("twist") or ""), t(first_note),
           tile(labels.get("axes") or "", "axes", first["axes"], mono=True),
           tile(labels.get("where") or "", "where", first["where"]),
           tile(labels.get("hold") or "", "hold", first["hold"]),
           t(labels.get("trade") or ""), t(first["trade"])))
    return gate_html + body


def _joint_alt(alt, j, angle):
    """The canvas's aria-label, composed the same way in Python and in JS.

    Composed rather than authored: it quotes three live values, so an authored
    string would be a fourth copy of the state and would go stale the moment
    the slider moved.
    """
    return (alt.get("template", "")
            .replace("{name}", (j.get("name") or "").lower())
            .replace("{angle}", str(angle))
            .replace("{max}", str(j["bend"][1]))
            .replace("{twist}", alt.get("can" if j.get("twist")
                                        else "cannot", "")))


def r_muscle_pair(a, act_id):
    """⊕ b2-03 `#s-bench` — two muscles, one elbow, and a continuous state.

    The only B2 instrument with physics running in it. The mechanism IS the
    teaching and is not chrome:

        both pulling   → the joint LOCKS wherever it is
        biceps only    → 135°
        triceps only   → 6°
        neither        → 6°, and it FALLS at 55 °/s where a pull moves at 90

    ⚠️ Do not flatten the two rates. "Gravity straightens a hanging arm for
    free" is taught by pressing *Neither* and watching it go down more slowly
    than it came up; equal rates delete the lesson and leave the animation.

    ⚠️ Two independent control groups — an exclusive four-tab mode group and a
    NON-exclusive two-toggle kill group, whose product decides every readout.
    No shipped instrument has this topology, which is most of why this is not
    a `sim`.

    ⊕ CORRECTION (contract R4). Design's page reads `prefers-reduced-motion`
    once at construction and never consults it in the tick, so the arm
    animates under reduced motion; its own sibling b2-02 checks correctly.
    Here the loop asks every frame and snaps straight to the target when
    motion is reduced — the arm still ends up where the mechanism says, it
    just does not travel there. Reduced motion is a complete experience, not a
    lesser one (R6).
    """
    modes = a.get("modes") or []
    kills = a.get("kills") or []
    if len(modes) != 4 or len(kills) != 2:
        raise ValueError(
            "muscle-pair %r takes exactly four contraction modes and two kill "
            "switches; got %d and %d." % (act_id, len(modes), len(kills)))
    labels = a.get("labels") or {}
    gate_html, hide = r_bench_gate(a.get("gate"))

    mode_btns = "".join(
        '<button type="button" class="ks3-sim-seg-btn ks3-muscle-mode" '
        'data-mode="%s" aria-pressed="%s">%s</button>'
        % (e(m["id"]), "true" if m["id"] == a.get("start_mode") else "false",
           t(m.get("label", "")))
        for m in modes)
    kill_btns = "".join(
        '<button type="button" class="ks3-sim-seg-btn ks3-muscle-kill" '
        'data-kill="%s" aria-pressed="false">%s</button>'
        % (e(k["id"]), t(k.get("label", ""))) for k in kills)

    cfg = {
        "start_angle": a.get("start_angle", 10),
        "targets": a.get("targets") or {},
        "rates": a.get("rates") or {},
        "notes": a.get("notes") or {},
        "status": a.get("status") or {},
        "states": a.get("states") or {},
        "canvas_labels": a.get("canvas_labels") or {},
        "alt": a.get("alt") or {},
    }
    tile = ('<div class="ks3-joint-tile">'
            '<p class="ks3-joint-tile-label">%s</p>'
            '<p class="ks3-joint-tile-value%s" data-tile="%s">%s</p></div>')
    return (gate_html
            + '<div class="ks3-muscle" data-musclepair%s data-total="%d" '
              'data-cfg="%s">'
              '<div class="ks3-muscle-groups">'
              '<div class="ks3-muscle-group">'
              '<p class="ks3-muscle-grouplabel">%s</p>'
              '<div class="ks3-muscle-btns">%s</div></div>'
              '<div class="ks3-muscle-group">'
              '<p class="ks3-muscle-grouplabel">%s</p>'
              '<div class="ks3-muscle-btns">%s</div></div></div>'
              '<div class="ks3-joint-stage">'
              '<canvas class="ks3-joint-canvas" width="1800" height="740" '
              'role="img" aria-label="%s" data-muscle-canvas></canvas>'
              '<div class="ks3-joint-controls">'
              '<p class="ks3-muscle-status" data-muscle-status>%s</p>'
              '</div></div>'
              '<div class="ks3-joint-tiles">%s%s%s</div>'
              '<p class="ks3-joint-trade"><strong>%s</strong> '
              '<span data-tile="note">%s</span></p></div>'
            % (hide, a.get("settings_total", 4),
               e(json.dumps(cfg, separators=(",", ":"), sort_keys=True,
                            ensure_ascii=False)),
               t(labels.get("contract") or ""), mode_btns,
               t(labels.get("kill") or ""), kill_btns,
               e(_muscle_alt(a.get("alt") or {}, "relaxed", "relaxed")),
               t((a.get("status") or {}).get(a.get("start_mode") or "none", "")),
               tile % (t(labels.get("angle") or ""), " ks3-joint-tile-mono",
                       "angle", t("%d°" % int(a.get("start_angle", 10)))),
               tile % (t(labels.get("biceps") or ""), "", "biceps",
                       t((a.get("states") or {}).get("relaxed", ""))),
               tile % (t(labels.get("triceps") or ""), "", "triceps",
                       t((a.get("states") or {}).get("relaxed", ""))),
               t(labels.get("note") or ""),
               t((a.get("notes") or {}).get(a.get("start_mode") or "none", ""))))


def _muscle_alt(alt, biceps_key, triceps_key):
    """The arm canvas's aria-label. Same composition in Python and in JS."""
    words = alt.get("words") or {}
    return (alt.get("template", "")
            .replace("{biceps}", words.get(biceps_key, ""))
            .replace("{triceps}", words.get(triceps_key, "")))


# ═══ C2 · Atoms, elements and compounds (⊕ MRB-220) ══════════════════════
#
# Nine instruments across six lessons. Everything below has markup here, real
# CSS in `shared/ks3.css`, real behaviour in `shared/ks3.js` reached from
# `wireInstruments()`, and at least one measured row in `ks3_parity.COMPONENTS`
# on a page that renders it. A dispatch-table entry is not a component.


def _canvas_frame(inner, foot, row=False):
    """The dark-canvas frame — one shape, used four times in C2 (map N12).

    c2-01's zoom, c2-03's dish, c2-05's builder and c2-06's balance all draw
    into the same wrapper: a `--ks3-r-card` box with a 2px `--ks3-on-dark-muted`
    outline, `overflow: hidden`, and a `--ks3-dark-panel` strip under the canvas
    carrying the controls or the caption. It was unnamed in the map because
    Design inlines it four times; it is one component here so the fifth
    instrument that wants it inherits a measured box rather than a fourth copy.
    """
    return ('<div class="ks3-canvas-frame">%s'
            '<div class="ks3-canvas-foot"%s>%s</div></div>'
            % (inner, ' data-row="1"' if row else "", foot))


def r_claim_switch(a, act_id):
    """⊕ c2-01 `#s-model` — three claims as toggles, four observations as
    dependants.

    ⚠️ A LIGHT `.ks3-block`, not a practical. The map calls this out by name:
    it is the flagship of a MODEL lesson and it looks like a bench, and
    painting it on ink resolves every text token wrong.

    ⚖️ THE FAILURE SENTENCE IS THE TEACHING. An observation whose claim is off
    does not grey out or get a cross — its text is REPLACED by the sentence
    saying why it stops being explained. Both sentences are in the document and
    one is hidden (emit-both-show-one), so no text is ever assembled from an
    attribute and `<em>` survives in either.

    ⚠️ `touched >= 2` counts EVERY press, including switching a claim back on.
    That is Design's rule as written (map §2.4) and a component must not tighten
    it silently to "two claims off".
    """
    claims = a.get("claims") or []
    obs = a.get("observations") or []
    if not claims or not obs:
        raise ValueError(
            "claim-switch %r needs both claims[] and observations[]." % act_id)
    ids = {c["id"] for c in claims}
    for o in obs:
        missing = [n for n in (o.get("needs") or []) if n not in ids]
        if missing:
            raise ValueError(
                "claim-switch %r observation %r needs claim(s) %s, which are "
                "not declared." % (act_id, o.get("id"), missing))

    gate = dict(a.get("gate") or {})
    # ⊕ The gate's options ARE the three claim texts, lettered (map §2.5). They
    # are read from `claims` rather than authored twice: a second copy of a
    # science-bearing sentence is a second place for it to drift, and R5's
    # point is that every authored key has exactly one meaning.
    if gate and not gate.get("options") and gate.get("options_from") == "claims":
        gate["options"] = [c.get("text", "") for c in claims]
    gate_html, hide = r_bench_gate(gate)

    labels = a.get("labels") or {}
    verdicts = a.get("verdicts") or {}
    note = a.get("note") or {}

    rows = "".join(
        '<button type="button" class="ks3-claim" data-claim="%s" '
        'aria-pressed="true"><span class="ks3-claim-chip" data-claim-chip>%s'
        '</span><span class="ks3-claim-text">%s</span></button>'
        % (e(c["id"]), t(labels.get("on") or "ON"), rich(c.get("text", "")))
        for c in claims)

    obs_rows = "".join(
        '<div class="ks3-obs-row" data-obs="%s" data-needs="%s">'
        '<div class="ks3-obs-texts">'
        '<p class="ks3-obs-text" data-obs-alive>%s</p>'
        '<p class="ks3-obs-text" data-obs-dead hidden>%s</p></div>'
        '<p class="ks3-obs-verdict" data-obs-verdict>%s</p></div>'
        % (e(o.get("id", "")), e(" ".join(o.get("needs") or [])),
           rich(o.get("text", "")), rich(o.get("fail", "")),
           t(verdicts.get("alive") or ""))
        for o in obs)

    words = note.get("claim_word") or {}
    return (gate_html
            + '<div class="ks3-claimswitch" data-claimswitch%s data-total="%d" '
              'data-done-at="%d" data-on="%s" data-off="%s" '
              'data-alive="%s" data-dead="%s" data-all-on="%s" '
              'data-none-broken="%s" data-some-broken="%s" data-word-one="%s" '
              'data-word-many="%s">'
              '<p class="ks3-claims-label">%s</p>'
              '<div class="ks3-claims">%s</div>'
              '<p class="ks3-claims-label ks3-obs-label">%s</p>'
              '<div class="ks3-obs">%s</div>'
              '<p class="ks3-claim-note" data-claimnote role="status">%s</p>'
              '</div>'
            % (hide, len(claims), int(a.get("done_at") or 2),
               e(labels.get("on") or "ON"), e(labels.get("off") or "OFF"),
               e(verdicts.get("alive") or ""), e(verdicts.get("dead") or ""),
               e(note.get("all_on") or ""), e(note.get("none_broken") or ""),
               e(note.get("some_broken") or ""),
               e(words.get("one") or ""), e(words.get("many") or ""),
               t(labels.get("claims") or ""), rows,
               t(labels.get("observations") or ""), obs_rows,
               rich(note.get("all_on") or "")))


# The five drawings c2-01's zoom ladder steps through, validated at build time
# so a typo is a build error and never a blank canvas.
#
# ⚠️ This is NOT `zoom-ladder`. That kind is B1's plant→cell ladder — a slider,
# a tick row, an authored orange next-box per level, and its own validated
# `ZOOM_DRAWINGS` set that would raise on every name below. c2-01 has two step
# buttons, no ticks, no next-box and five drawings that do not exist there. Two
# different instruments that share the word zoom.
SCALE_DRAWINGS = {"wire", "grains", "scratches", "beyond-light", "lattice"}


def _scale_alt(alt, level):
    """The zoom canvas's aria-label. Same composition in Python and in JS."""
    return (alt.get("template", "")
            .replace("{scale}", level.get("scale", ""))
            .replace("{label}", (level.get("label") or "").lower()))


def r_mixture_compound_dish(a, act_id):
    """⊕ c2-03 `#s-bench` — iron and sulfur, before and after heating.

    ⚖️ **THE PROPORTION CONTROL IS DISABLED ONCE HEATED, AND THAT IS THE
    LESSON.** NOTES §3.3 is explicit. In the mixture a student picks any of
    three proportions and the drawing changes; heat it and the control refuses,
    because a compound's proportion is not adjustable. A generic tab group that
    stays live would delete the entire argument of the lesson and leave a
    picture. The refusal is enforced in the markup (`disabled`), in the JS
    (a re-check inside the handler, exactly as Design's own click guard does)
    and in the drawing (the heated state has no ratio to draw).

    ⚖️ The CONTRAST spine: three of the four tests give a vivid answer in both
    states and settle nothing; the quiet one — weigh what actually combines —
    settles everything. `settles` is authored per test and drives which of the
    two verdict words is emitted, so the pattern is data rather than prose.

    ⚑ NOTES flag 8 is the drawing Design most wants an examiner's eye on: iron
    sulfide is a 1:1 giant structure and the lattice is a fair KS3 picture of
    it, but it is not molecules. The 5 × 17 grid draws one iron and one sulfur
    joined by a stub, repeating — which is the honest reading.
    """
    tests = a.get("tests") or []
    ratios = a.get("ratios") or []
    states = a.get("states") or []
    if len(states) != 2:
        raise ValueError(
            "mixture-compound-dish %r takes exactly two states (before and "
            "after heating); got %d." % (act_id, len(states)))
    if not tests:
        raise ValueError("mixture-compound-dish %r declares no tests[]." % act_id)
    fracs = a.get("ratio_fracs") or []
    if len(fracs) != len(ratios):
        raise ValueError(
            "mixture-compound-dish %r declares %d ratio label(s) and %d "
            "fraction(s). The label a student reads and the mix the canvas "
            "draws are the same control and must not drift."
            % (act_id, len(ratios), len(fracs)))

    gate_html, hide = r_bench_gate(a.get("gate"))
    labels = a.get("labels") or {}
    words = a.get("verdict_words") or {}
    alt = a.get("dish_alt") or {}
    notes = a.get("dish_note") or {}
    caps = a.get("captions") or {}

    state_btns = "".join(
        '<button type="button" class="ks3-sim-seg-btn ks3-dish-state" '
        'data-heated="%s" aria-pressed="%s">%s</button>'
        % ("1" if st.get("heated") else "0",
           "true" if i == 0 else "false", t(st.get("label", "")))
        for i, st in enumerate(states))
    ratio_btns = "".join(
        '<button type="button" class="ks3-sim-seg-btn ks3-dish-ratio" '
        'data-ratio="%d" aria-pressed="%s">%s</button>'
        % (i, "true" if i == int(a.get("start_ratio") or 0) else "false",
           t(lab))
        for i, lab in enumerate(ratios))
    test_btns = "".join(
        '<button type="button" class="ks3-sim-seg-btn ks3-dish-test" '
        'data-test="%s" aria-pressed="%s">%s</button>'
        % (e(tt["id"]), "true" if i == 0 else "false", t(tt.get("name", "")))
        for i, tt in enumerate(tests))

    cards = []
    for i, tt in enumerate(tests):
        cards.append(
            '<div class="ks3-dish-result" data-testcard="%s"%s>'
            '<p class="ks3-dish-testname">%s</p>'
            '<div class="ks3-dish-cols">'
            '<div class="ks3-dish-col ks3-dish-before">'
            '<p class="ks3-dish-collabel">%s</p><p class="ks3-dish-body">%s</p>'
            '</div>'
            '<div class="ks3-dish-col ks3-dish-after">'
            '<p class="ks3-dish-collabel">%s</p><p class="ks3-dish-body">%s</p>'
            '</div></div>'
            '<p class="ks3-dish-verdict"><strong>%s</strong> %s</p></div>'
            % (e(tt["id"]), "" if i == 0 else " hidden",
               t(tt.get("name", "")),
               t(labels.get("before") or ""), rich(tt.get("before", "")),
               t(labels.get("after") or ""), rich(tt.get("after", "")),
               t(words.get("settles" if tt.get("settles") else "not") or ""),
               rich(tt.get("verdict", ""))))

    cfg = {"fracs": fracs, "captions": caps}
    canvas = ('<canvas class="ks3-dish-canvas" width="1700" height="560" '
              'role="img" aria-label="%s" data-dish-canvas></canvas>'
              % e(alt.get("mixed", "")))
    foot = ('<p class="ks3-dish-note" data-dish-note>%s</p>'
            % t(notes.get("mixed", "")))
    return (gate_html
            + '<div class="ks3-dish" data-dish%s data-total="%d" '
              'data-cfg="%s" data-alt-mixed="%s" data-alt-heated="%s" '
              'data-note-mixed="%s" data-note-heated="%s">'
              '<div class="ks3-dish-groups">'
              '<div class="ks3-dish-group"><p class="ks3-dish-grouplabel">%s</p>'
              '<div class="ks3-dish-btns">%s</div></div>'
              '<div class="ks3-dish-group"><p class="ks3-dish-grouplabel">%s</p>'
              '<div class="ks3-dish-btns">%s</div></div></div>'
              '%s'
              '<div class="ks3-dish-tests">%s</div>%s</div>'
            % (hide, len(tests),
               e(json.dumps(cfg, separators=(",", ":"), sort_keys=True,
                            ensure_ascii=False)),
               e(alt.get("mixed", "")), e(alt.get("heated", "")),
               e(notes.get("mixed", "")), e(notes.get("heated", "")),
               t(labels.get("dish") or ""), state_btns,
               t(labels.get("ratio") or ""), ratio_btns,
               _canvas_frame(canvas, foot), test_btns, "".join(cards)))


# `verdict-cards` and `origin-grid` are ONE component with two layouts and
# three headline types (map §10.2). They differ only in how the cards are laid
# out and what the card leads with; the contract — one shot per card, the
# unchosen options dim, the row's border goes to ink, a display-font answer
# word and a why paragraph — is identical, and three instances across two
# lessons is exactly the case for building it once.
_CARD_LAYOUTS = {"column", "grid"}
_CARD_HEADLINES = {"prose", "formula", "symbol"}


def r_verdict_cards(a, act_id):
    """⊕ c2-03 `#s-sort` · c2-04 `#s-read` · c2-04 `#s-sort`.

    One-shot commit-and-reveal cards. Nearest shipped kinds are `sort-rows`
    (chips into named columns) and `sort-task` (`ks3-hard`), and it is neither:
    both of those gate EVERY row behind one "open the answers" button, and
    this reveals each card the instant that card is decided.

    ⚠️ R3 / MRB-196 R10 — nothing marks correctness. The chosen option keeps
    the ordinary chosen treatment, the unchosen ones dim, the CARD's border
    goes to ink, and the why paragraph is one tone whether the student had it
    or not. The answer word is display type because it is the answer, not
    because it is a verdict on the student.

    ⚠️ NO ANSWER VALIDATION against the offered options, deliberately, and for
    the same reason `job-sort` has none: c2-04's `answer` strings are counts
    ("Three") offered against `['One','Two','Three','Four']`, but c2-03's are
    sentences that are not any of `['Mixture','Compound']`. Validating would
    refuse Design's payload at build time.
    """
    items = a.get("items") or []
    if not items:
        raise ValueError("verdict-cards %r declares no items[]." % act_id)
    layout = a.get("layout") or "column"
    headline = a.get("headline") or "prose"
    if layout not in _CARD_LAYOUTS:
        raise ValueError("verdict-cards %r layout %r; the drawn set is %s."
                         % (act_id, layout, ", ".join(sorted(_CARD_LAYOUTS))))
    if headline not in _CARD_HEADLINES:
        raise ValueError("verdict-cards %r headline %r; the drawn set is %s."
                         % (act_id, headline, ", ".join(sorted(_CARD_HEADLINES))))
    shared = a.get("options") or []

    cards = []
    for it in items:
        opts = it.get("options") or shared
        if not opts:
            raise ValueError(
                "verdict-cards %r item %r offers no options and the activity "
                "declares no shared options[]." % (act_id, it.get("id")))
        btns = "".join(
            '<button type="button" class="ks3-seg-btn ks3-vcard-opt" '
            'data-i="%d" aria-pressed="false">%s</button>' % (i, t(lab))
            for i, lab in enumerate(opts))
        # Three headline shapes, one element. `symbol` is c2-04's 42px display
        # letter set; `formula` is its mono 26px `CaCO₃`; `prose` is c2-03's
        # sentence. A `sub` line under the headline exists only where Design
        # draws one, which is `symbol` and `formula`.
        head = ('<p class="ks3-vcard-head" data-headline="%s">%s</p>'
                % (e(headline), rich(it.get("headline") or it.get("text", ""))))
        sub = ('<p class="ks3-vcard-sub">%s</p>' % rich(it["sub"])
               if it.get("sub") else "")
        # ⚠️ The answer WORD is optional, and its absence is Design's. c2-03's
        # and c2-04's `#s-read` cards open with a display-font answer ("Mixture."
        # / "Three elements.") before the reason; c2-04's `#s-sort` cards open
        # with the reason alone, because the bucket the student just pressed IS
        # the answer and repeating it would be the card telling them what they
        # already said. Emitting an empty `<strong>` would put a stray space
        # and an empty element on nine cards.
        answer = (('<strong class="ks3-vcard-answer">%s</strong> '
                   % t(it["answer"])) if it.get("answer") else "")
        cards.append(
            '<div class="ks3-vcard" data-vcard="%s">%s%s'
            '<div class="ks3-vcard-opts">%s</div>'
            '<p class="ks3-vcard-why" hidden data-reveal>%s%s</p></div>'
            % (e(it.get("id", "")), head, sub, btns,
               answer, rich(it.get("why", ""))))

    close = ('<div class="ks3-vcards-close" hidden data-vcards-close>'
             '<p>%s</p></div>' % rich(a["close"])) if a.get("close") else ""
    return ('<div class="ks3-vcards" data-vcards data-layout="%s" '
            'data-total="%d">%s%s</div>'
            % (e(layout), len(items), "".join(cards), close))


def r_formula_builder(a, act_id):
    """⊕ c2-05 `#s-builder` — three pairs × three × three, five substances.

    ⚖️ **"NOT A SUBSTANCE" IS THE TEACHING.** Twenty-two of the twenty-seven
    reachable combinations say so, and Design's NOTES §8 calls that "the first
    honest thing a formula builder can teach". A builder that only offered the
    five real ones would teach that any formula you can write exists, which is
    the misconception the block is aimed at.

    ⊕ **The opening substance is banked at mount, which Design's page does
    not do.** `mark()` is passed as the setState callback of the three control
    groups only, so the H₂O the instrument OPENS on is displayed, is one of the
    five, and can never be counted unless the student navigates away and back
    (map F6). That is an addition INSIDE a component Design drew and it
    contradicts nothing on the page: the substance is on screen, named, and
    drawn. Without it the progress readout opens at "0 of 5" while showing one.

    ⚠️ The not-a-substance name composes with ASCII DIGITS — `H3O2`, not
    `H₃O₂` — while every authored name in `known` uses proper subscripts. That
    is Design's page as written (line 641) and the page wins; changing it is a
    content decision, not a build one.
    """
    pairs = a.get("pairs") or []
    known = a.get("known") or {}
    counts = a.get("counts") or [1, 2, 3]
    if not pairs or not known:
        raise ValueError(
            "formula-builder %r needs both pairs[] and known{}." % act_id)
    ids = {p["id"] for p in pairs}
    for key in known:
        pid = key.split(":")[0]
        if pid not in ids:
            raise ValueError(
                "formula-builder %r knows %r, whose pair %r is not offered. "
                "A substance the controls cannot reach is a substance no "
                "student can find." % (act_id, key, pid))
    start = a.get("start") or {}
    gate_html, hide = r_bench_gate(a.get("gate"))
    labels = a.get("labels") or {}
    nf = a.get("not_found") or {}

    def first(p_id):
        return next(p for p in pairs if p["id"] == p_id)

    p0 = first(start.get("pair") or pairs[0]["id"])
    a0 = int(start.get("a") or counts[0])
    b0 = int(start.get("b") or counts[0])
    k0 = "%s:%d:%d" % (p0["id"], a0, b0)
    found0 = known.get(k0)

    pair_btns = "".join(
        '<button type="button" class="ks3-sim-seg-btn ks3-fb-pair" '
        'data-pair="%s" aria-pressed="%s">%s</button>'
        % (e(p["id"]), "true" if p["id"] == p0["id"] else "false",
           t("%s and %s" % (p.get("a", ""), p.get("b", ""))))
        for p in pairs)

    def count_btns(axis, chosen):
        return "".join(
            '<button type="button" class="ks3-sim-seg-btn ks3-fb-count" '
            'data-axis="%s" data-n="%d" aria-pressed="%s">%d</button>'
            % (axis, n, "true" if n == chosen else "false", n)
            for n in counts)

    cfg = {"pairs": pairs, "known": known, "counts": counts,
           "colours": a.get("colours") or {},
           "not_found": nf, "captions": a.get("captions") or {},
           "alt": a.get("alt") or {},
           "start": {"pair": p0["id"], "a": a0, "b": b0}}
    canvas = ('<canvas class="ks3-fb-canvas" width="1700" height="520" '
              'role="img" aria-label="%s" data-fb-canvas></canvas>'
              % e(_fb_alt(a, found0)))
    foot = ('<p class="ks3-fb-name" data-fb-name>%s</p>'
            '<p class="ks3-fb-note" data-fb-note>%s</p>'
            % (t(_fb_name(p0, a0, b0, found0, nf)),
               rich((found0 or {}).get("note") or nf.get("note", ""))))
    return (gate_html
            + '<div class="ks3-fb" data-fb%s data-total="%d" data-done-at="%d" '
              'data-cfg="%s">'
              '<div class="ks3-fb-groups">'
              '<div class="ks3-fb-group"><p class="ks3-fb-grouplabel">%s</p>'
              '<div class="ks3-fb-btns">%s</div></div>'
              '<div class="ks3-fb-group">'
              '<p class="ks3-fb-grouplabel" data-fb-label="a">%s</p>'
              '<div class="ks3-fb-btns">%s</div></div>'
              '<div class="ks3-fb-group">'
              '<p class="ks3-fb-grouplabel" data-fb-label="b">%s</p>'
              '<div class="ks3-fb-btns">%s</div></div></div>%s</div>'
            % (hide, len(known), int(a.get("done_at") or len(known)),
               e(json.dumps(cfg, separators=(",", ":"), sort_keys=True,
                            ensure_ascii=False)),
               t(labels.get("pairs") or ""), pair_btns,
               t(p0.get("aName", "")), count_btns("a", a0),
               t(p0.get("bName", "")), count_btns("b", b0),
               _canvas_frame(canvas, foot)))


def _fb_name(pair, na, nb, found, nf):
    """The name under the drawing. Composed the same way in Python and in JS.

    ⚠️ ASCII digits on the not-found branch, subscripts on the authored names.
    Design's own asymmetry (page line 641), reproduced rather than tidied.
    """
    if found:
        return found.get("name", "")
    return "%s%s%s%s%s" % (pair.get("a", ""), na if na > 1 else "",
                           pair.get("b", ""), nb if nb > 1 else "",
                           nf.get("name_suffix", ""))


def _fb_alt(a, found):
    """The builder canvas's aria-label. Three-way, composed in both languages."""
    alt = a.get("alt") or {}
    if not found:
        return alt.get("none", "")
    tail = alt.get("giant" if found.get("giant") else "molecule", "")
    return alt.get("template", "").replace("{name}", found.get("name", "")) + tail


def r_model_limit(a, act_id):
    """⊕ c2-05 `#s-limit` — the MODEL family's *where it breaks* step.

    Two cards, a commit and an ungated reveal. The light/ink asymmetry IS the
    argument and is not decoration: the molecule sits on a card and the giant
    structure sits on ink, so the thing the model does not cover looks
    different before a word of it is read.

    ⚠️ THREE options, not four. Every other commit in KS3 offers four, and
    this is recorded (map N9) so it is not "corrected" to four by a later pass.

    ⚠️ The reveal is UNGATED BY THE ANSWER — it opens on any commitment.
    Commitment, never marking (R3).
    """
    cards = a.get("cards") or []
    if len(cards) != 2:
        raise ValueError(
            "model-limit %r takes exactly two contrast cards; got %d. The "
            "light/ink pair is the argument, and one card cannot make it."
            % (act_id, len(cards)))
    grounds = [c.get("ground") for c in cards]
    if sorted(grounds) != ["card", "ink"]:
        raise ValueError(
            "model-limit %r draws grounds %s; it takes one `card` and one "
            "`ink`. Two cards on the same ground is a comparison table, which "
            "is not what Design drew." % (act_id, grounds))
    # The commit line sits BETWEEN the cards and the options, which is the one
    # slot `r_activity`'s fixed order does not have — the shell's `prompt` is
    # already the lede above the cards. It belongs to the component because
    # Design draws it inside the block, at 19px/700, not as a second lede.
    commit = ('<p class="ks3-limit-commit">%s</p>' % t(a["commit"])
              if a.get("commit") else "")
    return ('<div class="ks3-limit" data-limit>'
            '<div class="ks3-limit-cards">%s</div>%s</div>'
            % ("".join(
                '<div class="ks3-limit-card" data-ground="%s">'
                '<p class="ks3-limit-caption">%s</p>'
                '<p class="ks3-limit-body">%s</p></div>'
                % (e(c.get("ground", "card")), t(c.get("caption", "")),
                   rich(c.get("text", "")))
                for c in cards), commit))


def r_balance_bench(a, act_id):
    """⊕ c2-06 `#s-balance` — two reactions × two vessels on one balance.

    ⚖️ **THE THIRD TILE NEVER MEASURES ANYTHING**, and it is the whole
    QUANTITATIVE move. `Mass before` and `Mass after` are read off the display;
    `Where it went` reads *not measured — you work it out* and takes no data,
    for ever. It is the same refusal `p3-01`'s light gates make. It has to be a
    real tile beside the two that do report, or the refusal reads as prose
    somebody forgot to fill in.

    ⚖️ The VESSEL CHANGES THE PICTURE — a sealed flask gets a drawn bung — and
    a run that moves gas draws the gas leaving or joining. A control that
    changes only a number teaches that the apparatus is incidental.

    ⚠️ `showAfter` RESETS on every control change (Design's own rule): switch
    reaction or vessel and the balance goes back to its before-reading, because
    it is now a different run and the after-mass of the last one is not a fact
    about this one.
    """
    runs = a.get("runs") or {}
    reactions = a.get("reactions") or []
    vessels = a.get("vessels") or []
    if not runs or not reactions or not vessels:
        raise ValueError(
            "balance-bench %r needs runs{}, reactions[] and vessels[]." % act_id)
    for r in reactions:
        for v in vessels:
            key = "%s:%s" % (r["id"], v["id"])
            if key not in runs:
                raise ValueError(
                    "balance-bench %r offers %r but declares no run for it. "
                    "Every combination the controls can reach must have a "
                    "reading." % (act_id, key))
    tiles = a.get("tiles") or []
    if len(tiles) != 3:
        raise ValueError(
            "balance-bench %r draws %d tile(s); it takes three, and the third "
            "is the one that refuses to measure." % (act_id, len(tiles)))

    gate_html, hide = r_bench_gate(a.get("gate"))
    labels = a.get("labels") or {}
    dec = int(a.get("decimals", 2))
    r0, v0 = reactions[0]["id"], (a.get("start_vessel") or vessels[0]["id"])
    first = runs["%s:%s" % (r0, v0)]

    def group(cls, key, items, chosen):
        return "".join(
            '<button type="button" class="ks3-sim-seg-btn %s" data-%s="%s" '
            'aria-pressed="%s">%s</button>'
            % (cls, key, e(i["id"]), "true" if i["id"] == chosen else "false",
               t(i.get("label", "")))
            for i in items)

    tile_html = "".join(
        '<div class="ks3-bal-tile"><p class="ks3-bal-tile-label">%s</p>'
        '<p class="ks3-bal-tile-value%s"%s>%s</p></div>'
        % (t(tl.get("label", "")),
           "" if tl.get("body") else " ks3-bal-tile-mono",
           "" if tl.get("body") else ' data-tile="%s"' % e(tl.get("id", "")),
           t(tl.get("body") or _mass(first["before"] if tl.get("id") == "before"
                                     else None, dec, labels)))
        for tl in tiles)

    cfg = {"runs": runs, "labels": labels, "decimals": dec,
           "run_labels": a.get("run_labels") or {},
           "liquids": a.get("liquid_colours") or {},
           "gas_labels": a.get("gas_labels") or {},
           "alt": a.get("alt") or {},
           "start": {"reaction": r0, "vessel": v0}}
    canvas = ('<canvas class="ks3-bal-canvas" width="1700" height="560" '
              'role="img" aria-label="%s" data-bal-canvas></canvas>'
              % e(_bal_alt(a, v0, first["before"], False, dec)))
    foot = ('<button type="button" class="ks3-bal-run" data-bal-run>%s</button>'
            '<p class="ks3-bal-status" data-bal-status>%s</p>'
            % (t((a.get("run_labels") or {}).get("idle", "")),
               t(labels.get("status_idle", ""))))
    return (gate_html
            + '<div class="ks3-bal" data-bal%s data-total="%d" '
              'data-done-at="%d" data-cfg="%s">'
              '<div class="ks3-bal-groups">'
              '<div class="ks3-bal-group"><p class="ks3-bal-grouplabel">%s</p>'
              '<div class="ks3-bal-btns">%s</div></div>'
              '<div class="ks3-bal-group"><p class="ks3-bal-grouplabel">%s</p>'
              '<div class="ks3-bal-btns">%s</div></div></div>'
              '%s<div class="ks3-bal-tiles">%s</div>'
              '<p class="ks3-bal-note" data-bal-note>%s</p></div>'
            % (hide, len(runs), int(a.get("done_at") or len(runs)),
               e(json.dumps(cfg, separators=(",", ":"), sort_keys=True,
                            ensure_ascii=False)),
               t(labels.get("reaction") or ""),
               group("ks3-bal-rxn", "rxn", reactions, r0),
               t(labels.get("vessel") or ""),
               group("ks3-bal-vessel", "vessel", vessels, v0),
               _canvas_frame(canvas, foot, row=True), tile_html,
               rich(labels.get("idle_note", ""))))


def _mass(value, dec, labels):
    """`152.00 g`, or the em-dash the After tile shows before a run."""
    if value is None:
        return labels.get("unmeasured") or "—"
    return ("%%.%df %%s" % dec) % (value, labels.get("unit") or "g")


def _bal_alt(a, vessel, mass, after, dec):
    """The balance canvas's aria-label. Composed the same way in JS."""
    alt = a.get("alt") or {}
    return (alt.get("template", "")
            .replace("{vessel}", alt.get(vessel, ""))
            .replace("{mass}", ("%%.%df" % dec) % mass)
            .replace("{when}", alt.get("after" if after else "before", "")))


def r_fifa_pick(lesson, a, act_id):
    """⊕ c2-06 `#s-build` — MRB-204 part 4, and NOT `fifa-construct`.

    The shipped `fifa-construct` renders four free-text inputs, a Check button,
    a model `<ol>` and a success-criteria tick list, and asserts
    `len(fields) == len(model) == len(success)`. Design's page is a different
    mechanism: two multiple-choice ladders of three, one number field beside a
    unit `<select>`, and a four-step ink reveal that quotes the student's own
    input back. Three commitments against four model lines and no criteria at
    all — the existing assertions would raise on it, and rightly.

    ⚖️ The two ladders are MULTIPLE CHOICE ON PURPOSE. A student who cannot yet
    write `152.00 = 149.80 + mass of gas` can still recognise it, and the two
    distractors are the two real errors — conserving only the solid, and adding
    the gas to the wrong side. A free-text box would fail them silently.

    ⚖️ THE BUTTON IS LOCKED UNTIL ALL FOUR PARTS ARE SET — both picks, a
    number, and a unit. The unit is a separate commitment because "2.2" is not
    an answer to a question about mass.
    """
    steps = a.get("steps") or []
    picks = a.get("picks") or []
    field = a.get("field") or {}
    if len(picks) != 2:
        raise ValueError(
            "fifa-pick %r declares %d pick ladder(s); it takes two — the rule "
            "and the insertion." % (act_id, len(picks)))
    if not steps:
        raise ValueError("fifa-pick %r reveals no steps[]." % act_id)
    if not field.get("units"):
        raise ValueError(
            "fifa-pick %r offers no units[]. The unit is a separate "
            "commitment: `2.2` is not an answer to a question about mass."
            % act_id)

    panels = []
    for i, p in enumerate(picks):
        opts = "".join(
            '<button type="button" class="ks3-pick-opt" data-group="%d" '
            'data-i="%d" aria-pressed="false">%s</button>' % (i, j, t(o))
            for j, o in enumerate(p.get("options") or []))
        panels.append(
            '<div class="ks3-pick-panel"><p class="ks3-pick-label">%s</p>'
            '<div class="ks3-pick-opts">%s</div></div>'
            % (t(p.get("label", "")), opts))

    # ⊕ N10 — the visually-hidden label. No `.ks3-sr-only` existed in
    # `shared/ks3.css`; Design inlines `position:absolute; left:-9999px` twice.
    # One class now, because the next form control will want it too.
    aid, uid = "%s-ans" % act_id, "%s-unit" % act_id
    # ⚠️ THE PLACEHOLDER OPTION CARRIES AN EMPTY VALUE, and that is
    # load-bearing rather than tidy: the unit is one of the four commitments
    # the open button waits for, and a placeholder with its own value ("choose
    # a unit") satisfies `unit.value` — so the gate opens on a student who
    # never chose a unit. Measured in a browser, not read off the source.
    units = ('<option value="">%s</option>' % t(field["unit_placeholder"])
             if field.get("unit_placeholder") else "")
    units += "".join('<option value="%s">%s</option>' % (e(u), t(u))
                     for u in field["units"])
    panels.append(
        '<div class="ks3-pick-panel"><p class="ks3-pick-label">%s</p>'
        '<div class="ks3-pick-answer">'
        '<label class="ks3-sr-only" for="%s">%s</label>'
        '<input class="ks3-pick-input" type="text" inputmode="decimal" '
        'id="%s" placeholder="%s" data-pick-ans>'
        '<label class="ks3-sr-only" for="%s">%s</label>'
        '<select class="ks3-sim-units ks3-pick-unit" id="%s" data-pick-unit>'
        '%s</select></div></div>'
        # ⚠️ NO `value` attribute on the input. B1 already fixed this once:
        # an authored `value` is an attribute, the runtime re-renders, and the
        # student's own typing is wiped on the next state change.
        % (t(field.get("label", "")), e(aid), t(field.get("hint", "")),
           e(aid), e(field.get("placeholder", "")), e(uid),
           t(field.get("unit_hint", "")), e(uid), units))

    reveal = "".join(
        '<div class="ks3-pick-step">'
        '<span class="ks3-pick-chip" aria-hidden="true">%s</span>'
        '<div class="ks3-pick-stepbody"><p class="ks3-pick-steplabel">%s</p>'
        '<p class="ks3-pick-stepline">%s</p>'
        '<p class="ks3-pick-stepnote">%s</p></div></div>'
        % (t(s.get("letter", "")), t(s.get("label", "")),
           t(s.get("line", "")), rich(s.get("note", "")))
        for s in steps)

    close = a.get("close") or {}
    return ('<div class="ks3-pick" data-pick data-total="3" '
            'data-close="%s" data-blank="%s" data-done-label="%s">'
            '<div class="ks3-pick-panels">%s</div>'
            '<div class="ks3-pick-foot">'
            '<button type="button" class="ks3-reveal-btn ks3-pick-btn" '
            'data-pick-open disabled>%s</button>'
            '<span class="ks3-pick-progress" data-pick-progress>%s</span>'
            '</div>'
            '<div class="ks3-pick-reveal" hidden data-reveal>'
            '<p class="ks3-pick-revealhead">%s</p>%s'
            '<p class="ks3-pick-close" data-pick-close></p></div></div>'
            % (e(close.get("template", "")), e(close.get("blank") or "—"),
               e((a.get("progress") or {}).get("done", "")),
               "".join(panels),
               t(a.get("button", "")),
               t((a.get("progress") or {}).get("format", "")
                 .replace("{n}", "0")),
               t(a.get("reveal_head", "")), reveal))


def r_test_budget_bench(a, act_id):
    """⊕ c2-02 `#s-bench` — six samples, four tests, and eight tests to spend.

    ⚖️ **THE BUDGET IS THE PEDAGOGY, NOT A GAME MECHANIC.** With unlimited
    tests a student runs everything and learns nothing about which evidence
    discriminates; the whole lesson is discovering that *looks like a metal*,
    *conducts* and *is shiny* are the three most interesting results you can
    buy and all three are worthless. Design's NOTES §3.2 says it in as many
    words: "if Code drops the budget the lesson quietly becomes a
    click-through." So the budget is required, it is validated as reachable,
    and it is GLOBAL across all six samples rather than per-sample.

    ⚠️ THE INSTRUMENT NEVER MARKS. The verdict panel fires on the student's
    verdict whether or not that verdict was right, and it is the only place a
    sample is named. `element` is authored on every sample and read by nothing
    (map N16) — it is correctness data waiting for a marker that R3 says must
    not arrive here. Kept, and flagged rather than deleted.

    ⚠️ Emit-all-show-one, as the board does: every sample panel is in the
    document and one is shown, so returning to a sample finds its results and
    its verdict exactly as they were left and no state lives outside the DOM.
    """
    samples = a.get("samples") or []
    tests = a.get("tests") or []
    if not samples or not tests:
        raise ValueError(
            "test-budget-bench %r needs both samples[] and tests[]." % act_id)
    budget = int(a.get("budget") or 0)
    if budget < len(samples):
        # Fewer tests than samples means a sample that can never be tested at
        # all, which is not a hard lesson — it is a broken one.
        raise ValueError(
            "test-budget-bench %r has a budget of %d over %d samples. A budget "
            "below one test per sample makes the bench unusable rather than "
            "demanding." % (act_id, budget, len(samples)))
    for s in samples:
        missing = [t["id"] for t in tests if t["id"] not in (s.get("results") or {})]
        if missing:
            raise ValueError(
                "test-budget-bench %r sample %r has no result for test(s) %s. "
                "A test a student can spend a budget point on must say "
                "something." % (act_id, s.get("id"), missing))

    gate_html, hide = r_bench_gate(a.get("gate"))
    labels = a.get("labels") or {}
    verdicts = a.get("verdicts") or []

    tabs = "".join(
        '<button type="button" class="ks3-seg-btn ks3-sample-tab" '
        'data-sample="%s" aria-pressed="%s"><span data-tab-label>%s</span>'
        '</button>'
        % (e(s["id"]), "true" if i == 0 else "false", t(s.get("tab", "")))
        for i, s in enumerate(samples))

    panels = []
    for i, s in enumerate(samples):
        test_btns = "".join(
            '<button type="button" class="ks3-seg-btn ks3-test-btn" '
            'data-test="%s" aria-pressed="false">%s</button>'
            % (e(tt["id"]), t(tt.get("label", ""))) for tt in tests)
        results = "".join(
            '<li class="ks3-result" data-result="%s" hidden>'
            '<p class="ks3-result-test">%s</p>'
            '<p class="ks3-result-body">%s</p></li>'
            % (e(tt["id"]), t(tt.get("label", "")),
               rich((s.get("results") or {}).get(tt["id"], "")))
            for tt in tests)
        vbtns = "".join(
            '<button type="button" class="ks3-seg-btn ks3-verdict-btn" '
            'data-verdict="%s" aria-pressed="false">%s</button>'
            % (e(v.get("id", "")), t(v.get("label", "")))
            for v in verdicts)
        panels.append(
            '<div class="ks3-sample" data-sample="%s"%s>'
            '<p class="ks3-sample-name">%s</p>'
            '<p class="ks3-sample-look">%s</p>'
            '<div class="ks3-sample-tests">%s</div>'
            '<ul class="ks3-results" hidden data-results role="list">%s</ul>'
            '<div class="ks3-sample-verdict">'
            '<p class="ks3-sample-ask">%s</p>'
            '<div class="ks3-verdict-btns">%s</div>'
            '<div class="ks3-verdict-panel" hidden data-verdict-panel>'
            '<p class="ks3-verdict-name">%s</p>'
            '<p class="ks3-verdict-why">%s</p></div></div></div>'
            % (e(s["id"]), "" if i == 0 else " hidden",
               t(s.get("name", "")), rich(s.get("look", "")), test_btns,
               results, t(labels.get("ask") or ""), vbtns,
               t(s.get("name2", "")), rich(s.get("why", ""))))

    close = ('<div class="ks3-bench-close" hidden data-bench-close><p>%s</p>'
             '</div>' % rich(a["close"])) if a.get("close") else ""
    return (gate_html
            + '<div class="ks3-budget" data-budgetbench%s data-budget="%d" '
              'data-total="%d" data-marker="%s">'
              '<div class="ks3-sample-tabs">%s</div>%s%s</div>'
            % (hide, budget, len(samples), e(labels.get("decided") or " ·"),
               tabs, "".join(panels), close))


def r_scale_zoom(a, act_id):
    """⊕ c2-01 `#s-scale` — five steps from a centimetre of wire to the atoms.

    ⚖️ The lesson is that FOUR OF THE FIVE STEPS SHOW NOTHING NEW. Copper stays
    copper down past the reach of any light microscope, and the fourth drawing
    says so in words on the canvas rather than showing a smaller orange thing.
    Collapsing the ladder to "wire, then atoms" would delete the argument and
    leave the picture.

    Stage 3 is done when all five levels have been REACHED BY STEPPING IN —
    `seenZoom` seeds level 0 and only the in-button adds to it (map §2.4), so
    backing out and climbing again is the only route. Reproduced, not tightened.
    """
    levels = a.get("levels") or []
    if len(levels) < 2:
        raise ValueError("scale-zoom %r declares %d level(s); it steps between "
                         "at least two." % (act_id, len(levels)))
    for lv in levels:
        if lv.get("drawing") not in SCALE_DRAWINGS:
            raise ValueError(
                "scale-zoom %r level %r names drawing %r; the drawn set is %s."
                % (act_id, lv.get("scale"), lv.get("drawing"),
                   ", ".join(sorted(SCALE_DRAWINGS))))
    labels = a.get("labels") or {}
    alt = a.get("alt") or {}
    start = int(a.get("start") or 0)
    first = levels[start]

    foot = ('<div class="ks3-scale-controls">'
            '<button type="button" class="ks3-sim-seg-btn ks3-scale-btn" '
            'data-step="-1"%s>%s</button>'
            '<button type="button" class="ks3-sim-seg-btn ks3-scale-btn" '
            'data-step="1"%s>%s</button>'
            '<p class="ks3-scale-readout" data-scale-readout>%s</p></div>'
            % (" disabled" if start == 0 else "", t(labels.get("out") or ""),
               " disabled" if start >= len(levels) - 1 else "",
               t(labels.get("in") or ""), t(first.get("scale", ""))))
    canvas = ('<canvas class="ks3-scale-canvas" width="1800" height="620" '
              'role="img" aria-label="%s" data-scale-canvas></canvas>'
              % e(_scale_alt(alt, first)))
    return ('<div class="ks3-scale" data-scalezoom data-total="%d" '
            'data-start="%d" data-levels="%s" data-alt="%s">%s'
            '<p class="ks3-scale-note" data-scale-note>%s</p></div>'
            % (len(levels), start,
               e(json.dumps(levels, separators=(",", ":"), sort_keys=True,
                            ensure_ascii=False)),
               e(alt.get("template", "")),
               _canvas_frame(canvas, foot), rich(first.get("note", ""))))


# The four activity shells: classes, eyebrow, and the element the prompt takes.
#
# `check` and `worked-example` set the prompt as the block's heading — Design's
# canonical lesson renders it at 28px and `.ks3-check h2, .ks3-worked h2` in
# ks3.css exists for exactly that. `practical` and `misconception` keep it as
# prose: a practical prompt is a run-the-lab instruction rather than a
# question, and a misconception block already leads with the quoted wrong idea.
ACTIVITY_SHELLS = {
    "check":          ("ks3-block ks3-check", "Your turn", "h2"),
    "worked-example": ("ks3-block ks3-worked", "Worked example", "h2"),
    "practical":      ("ks3-block ks3-dark ks3-practical", "Investigate", "p"),
    "misconception":  ("ks3-block ks3-misconception", "Think again", "p"),
}


# ⊕ The activity-kind dispatch table, as a module-level constant.
#
# It is a constant rather than a dict literal inside `r_activity` so that
# `verify_ks3.py` can read the REAL table and report every authored kind that
# has no entry. That gate exists because MRB-203's registry works one level
# above this one: it asks whether a BLOCK TYPE has a registered component, and
# cannot see that an activity KIND it does not know falls through to the
# generic prompt/options/reveal shell — which renders, validates, and passes
# every gate while being the wrong component.
#
# That is not hypothetical. It is what Mide rejected on 11 August: B1-06's task
# is "name the level for each of these eight and say what settled it" and it
# rendered as a four-option multiple choice with eight items in the prompt.
#
#   kind -> (modifier class, marker attributes)
#
# The class is what the stylesheet hangs the instrument on; the attribute is
# what shared/ks3.js dispatches on, and it also tells `wirePredictions` to keep
# its hands off — an instrument owns every option inside it.
#
# ⊕ The attribute string carries `data-stage-done="0"` for an instrument that
# HAS a completion contract, and omits it for one that does not. It used to be
# appended automatically to every entry, which was right while both entries
# were tasks and wrong the moment an expository kind joined them: `#s-think` is
# a rail stop on none of the six lessons, because MRB-208 ruled the rail
# carries "only sections that require the student to do something", and a
# confrontation asks for nothing. Emitting the attribute anyway would declare a
# completion contract the section can never discharge.
#
# ⊕ Every entry also carries `data-instrument`. That is what tells
# `wirePredictions` to keep its hands off, and until 14 Aug 2026 the comment
# here claimed it did while **no such check existed in `shared/ks3.js`**. The
# consequence was live and exactly what this comment predicted: the generic
# Law 4 wiring selects every `.ks3-option` in the section and the FIRST
# `[data-reveal]` it finds, so on the board it would have wired all four
# specimen panels' predictions together and unhidden specimen one's verdict
# panel on any of them. An instrument owns every option inside it.
# renderers: ═══ BEGIN C1 ═══
# DISPATCH: "collision-counter": ("ks3-counter-block", ' data-instrument data-counterblock data-stage-done="0"'),
#
# Splice point: `ACTIVITY_KIND_RENDERERS` in build_ks3.py, in the new
# "C1 · Particles and their behaviour" section. Also add to `r_activity`:
#
#     if kind == "collision-counter":
#         parts.append(r_collision_counter(a, act_id))
#
# The function below belongs beside the other C1 renderers. It uses `e`, `t`,
# `r_bench_gate` and `json`, all of which build_ks3.py already imports/defines.


# The three control groups, as (payload key, value key, caption key, css/data
# name). One table rather than three near-identical blocks, because the ONLY
# thing that differs between them is which authored list they read — and a
# fourth group would otherwise arrive as a fourth copy of the same markup.
_COUNTER_GROUPS = (
    ("temps", "speed_multiplier", "temperature", "temp"),
    ("vols", "scale", "volume", "vol"),
    ("counts", "n", "particles", "count"),
)


def _counter_alt(alt, temps, vols, counts, temp, vol, count, hits):
    """The bench canvas's aria-label. Same composition in Python and in JS.

    ⊕ CORRECTION (PAYLOAD-MAP §4.6). Design's label (page 705–706) names the
    temperature, the container and the particle count and stops — it does not
    say how many wall hits there were, which is the one number the lesson is
    about and the one a sighted student is reading in 58px type. Every readout
    on this bench is drawn INSIDE the canvas, so `aria-label` is the only route
    to any of it. Design's sentence is carried byte-identical and the count is
    added as a second sentence after it.
    """
    return (alt.get("template", "")
            .replace("{temp}", (temps[temp].get("label") or "").lower())
            .replace("{vol}", (vols[vol].get("label") or "").lower())
            .replace("{n}", str(counts[count].get("n", "")))
            .replace("{hits}", str(hits)))


def r_collision_counter(a, act_id):
    """⊕ c1-04 `#s-bench` — a real count of collisions with the wall.

    ⚠️ A LIGHT `.ks3-block`, not a practical. Page line 109 carries no
    `ks3-dark`, and the canvas draws its own cream box: on ink the drawing
    would sit in a black surround and every text token in the control strip
    would resolve to its on-dark value.

    ⚖️ THE BUMPS TOGGLE IS PART-08's ENTIRE CONFRONTATION. The wrong idea is
    "pressure is the particles pushing against each other", and this is the one
    instrument in the key stage that draws those pushes — grey rings, dozens of
    them, in the middle of the box — and then does not count a single one. Drop
    the toggle and the lesson is a picture of a gas with a number over it.

    ⚖️ THE COUNTING IS REAL. `step()` pushes a timestamp on every wall bounce
    and shifts entries older than `window_ms`, so the number is an actual count
    of the last second rather than a formula evaluated for effect. That is what
    makes "smaller box, same particles, same speed, and the count is up"
    something a student watches rather than something the page claims.

    ⚑ NOTES flag 6 — pressure is a COUNT and a BAR, never a pascal. The bar
    fills to `min(1, hits / pressure_full)` and carries no number and no unit.

    ⊕ Two corrections, both reported: the aria-label gains the wall-hit count
    (see `_counter_alt`), and the rail's "controls tried" predicate is a SET of
    three distinct groups rather than Design's `Math.max(touched, N)`, which
    ticks on the particle-count button alone.
    """
    labels = a.get("labels") or {}
    bumps = a.get("bumps") or {}
    canvas_labels = a.get("canvas_labels") or {}
    notes = a.get("notes") or {}
    alt = a.get("alt") or {}
    start = a.get("start") or {}
    hc = a.get("head_counter") or {}

    groups = {}
    for key, value_key, caption_key, _name in _COUNTER_GROUPS:
        rows = a.get(key) or []
        if len(rows) != 3:
            raise ValueError(
                "collision-counter %r needs exactly three %s; got %d. Design "
                "draws three three-way segmented groups and the grid is built "
                "for them." % (act_id, key, len(rows)))
        for row in rows:
            if not row.get("label") or row.get(value_key) is None:
                raise ValueError(
                    "collision-counter %r: every %s entry needs `label` and "
                    "%r; got %r." % (act_id, key, value_key, row))
        if not labels.get(caption_key):
            raise ValueError(
                "collision-counter %r has no `labels.%s` caption. A group with "
                "no caption is three buttons a student cannot name."
                % (act_id, caption_key))
        groups[key] = rows

    # The six authored branches, and all six must be present: the note is the
    # sentence that says what just happened, and a missing branch is a silent
    # empty panel at exactly the setting a student went looking for.
    for branch in ("bumps", "smaller_box", "hot", "cold", "more_particles",
                   "resting"):
        if not notes.get(branch):
            raise ValueError(
                "collision-counter %r has no `notes.%s`. Design authors six "
                "branches (page 631–644) and the renderer emits all six."
                % (act_id, branch))

    for field in ("on_label", "off_label", "caption"):
        if not bumps.get(field):
            raise ValueError(
                "collision-counter %r has no `bumps.%s`. The bumps toggle is "
                "PART-08's confrontation and cannot ship unlabelled."
                % (act_id, field))

    for token in ("{temp}", "{vol}", "{n}", "{hits}"):
        if token not in (alt.get("template") or ""):
            raise ValueError(
                "collision-counter %r: `alt.template` is missing %s. Every "
                "readout is drawn inside the canvas, so the label is the only "
                "thing a screen reader gets." % (act_id, token))

    temp0 = int(start.get("temp", 1))
    vol0 = int(start.get("vol", 0))
    count0 = int(start.get("count", 1))

    gate_html, hide = r_bench_gate(a.get("gate"))

    # ── the three segmented groups ──
    # `.ks3-sim-seg-btn` deliberately, not a private control: drift 4 ruled ONE
    # segmented control for the key stage, and a second copy at Design's 16px
    # is exactly the drift the ruling exists to stop.
    group_html = []
    for key, _value_key, caption_key, name in _COUNTER_GROUPS:
        chosen = {"temps": temp0, "vols": vol0, "counts": count0}[key]
        btns = "".join(
            '<button type="button" class="ks3-sim-seg-btn ks3-counter-btn" '
            'data-group="%s" data-i="%d" aria-pressed="%s">%s</button>'
            % (e(name), i, "true" if i == chosen else "false",
               t(row.get("label", "")))
            for i, row in enumerate(groups[key]))
        group_html.append(
            '<div class="ks3-counter-group">'
            '<p class="ks3-counter-grouplabel">%s</p>'
            '<div class="ks3-counter-btns">%s</div></div>'
            % (t(labels[caption_key]), btns))

    # ── the bumps toggle ──
    # Emit-both-show-one rather than a textContent swap out of two attributes:
    # no student-facing string is ever rebuilt in JS, and the label survives
    # whatever punctuation an author puts in it.
    # `on_label` is the label that turns the rings ON ("Show …"), so it is the
    # one visible while they are off. The attribute names follow the WORDS, not
    # the state, because that is what stops the two getting swapped.
    bump_btn = ('<button type="button" class="ks3-sim-seg-btn '
                'ks3-counter-bumpbtn" data-counter-bumps aria-pressed="false">'
                '<span data-bump-show>%s</span>'
                '<span data-bump-hide hidden>%s</span></button>'
                % (t(bumps["on_label"]), t(bumps["off_label"])))

    # ── the six notes, one shown ──
    # One live region holding six paragraphs, five hidden. The wrapper carries
    # `role="status"`, never the instrument root.
    note_html = "".join(
        '<p class="ks3-counter-note" data-note="%s"%s>%s</p>'
        % (e(branch), "" if branch == "resting" else " hidden",
           t(notes[branch]))
        for branch in ("bumps", "smaller_box", "hot", "cold", "more_particles",
                       "resting"))

    cfg = {
        "temps": groups["temps"],
        "vols": groups["vols"],
        "counts": groups["counts"],
        "start": {"temp": temp0, "vol": vol0, "count": count0},
        "bump_threshold": bumps.get("threshold", 0.0022),
        "canvas_labels": canvas_labels,
        "pressure_full": a.get("pressure_full", 170),
        "window_ms": a.get("window_ms", 1000),
        "flash_ms": a.get("flash_ms", 420),
        "reduced_motion_scale": a.get("reduced_motion_scale", 0.35),
        "step_per_frame": a.get("step_per_frame", 0.0075),
        "alt": alt,
    }

    return (gate_html
            + '<div class="ks3-counter" data-counter%s data-total="3" '
              'data-full-label="%s" data-cfg="%s">'
              '<div class="ks3-counter-stage">'
              '<canvas class="ks3-counter-canvas" width="1800" height="680" '
              'role="img" aria-label="%s" data-counter-canvas></canvas>'
              '<div class="ks3-counter-controls">'
              '<div class="ks3-counter-groups">%s</div>'
              '<div class="ks3-counter-bumps">%s'
              '<p class="ks3-counter-bumpnote">%s</p></div>'
              '</div></div>'
              '<div class="ks3-counter-notes" data-counter-notes '
              'role="status">%s</div></div>'
            % (hide,
               # Design's terminal label for the head counter (page 691).
               # `_head_counter` has `zero` but no `full`, so the string is
               # carried here and `wireCollisionCounter` writes it on the
               # counter element the shared updater owns — one element, one
               # place, one authored copy of each of the two strings.
               e(hc.get("full") or ""),
               e(json.dumps(cfg, separators=(",", ":"), sort_keys=True,
                            ensure_ascii=False)),
               e(_counter_alt(alt, groups["temps"], groups["vols"],
                              groups["counts"], temp0, vol0, count0, 0)),
               "".join(group_html), bump_btn, t(bumps["caption"]),
               note_html))


# DISPATCH: "evidence-bench": ("ks3-ebench-block", ' data-instrument data-ebenchblock data-stage-done="0"'),
#
# and in `r_activity`, beside the other kind branches:
#     if kind == "evidence-bench":
#         parts.append(r_evidence_bench(a, act_id))
#
# Place the function next to `r_claim_switch`. It needs `e`, `t`, `rich` only —
# no gate helper, because this instrument has none (see the docstring).


def r_evidence_bench(a, act_id):
    """⊕ c1-06 `#s-bench` — seven observations, judged one at a time.

    ⚠️ A LIGHT `.ks3-block`, and **NO GATE**. This is the only flagship
    instrument in C1 that is open from the start, and that is deliberate rather
    than an omission: the seven judgements ARE the commitment, so a fourth
    option in front of them would ask the student to commit to committing.
    `r_bench_gate` is not called and must not be added.

    The nearest shipped kinds are `test-board` and `removal-cases`, and both are
    the wrong shape. This is seven BINARY judgements, each with one authored
    verdict on a two-tone panel, plus a whole-set tally that reports how many
    the student called correctly **before** the verdicts opened. Nothing else in
    the key stage scores a call made before a reveal.

    ⚖️ THE TALLY SCORES THE FIRST CALL, NOT THE CURRENT ONE. Design recomputes
    it from live state (`rightCalls`, page line 488), so a student who flips an
    answer after reading the verdict raises a number whose own sentence says
    "before opening the verdict". The buttons stay live — Design leaves them
    live and the verdict does not change when they are pressed again — but the
    scored call is latched on the first press, in `data-called`. That is the
    smallest change that makes the drawn sentence true.

    ⚠️ R3 / MRB-196 R10 — NOTHING HERE MARKS THE STUDENT. The chosen button
    takes the ordinary chosen treatment, the case's border goes to ink, and the
    verdict panel's two grounds are a fact about THE MODEL (`ok`), not about the
    answer. A student who called every one wrong sees exactly the same panels.

    ⚠️ `benchProgress` has two shapes (page line 544): the running count, which
    is `head_counter`'s job, and a bespoke label once the set closes.
    `_head_counter` has no "full" branch, so `progress_all` rides on the
    instrument root and `wireEvidenceBench` writes it into the block-head
    counter. The alternative was retyping "all seven judged" into the engine.
    """
    cases = a.get("cases") or []
    if not cases:
        raise ValueError("evidence-bench %r declares no cases[]." % act_id)

    buttons = a.get("buttons") or {}
    if not (buttons.get("yes") and buttons.get("no")):
        raise ValueError(
            "evidence-bench %r needs buttons={'yes': …, 'no': …}; both labels "
            "are authored and neither has a default worth guessing." % act_id)

    labels = a.get("verdict_labels") or {}
    if not (labels.get("ok") and labels.get("fail")):
        raise ValueError(
            "evidence-bench %r needs verdict_labels={'ok': …, 'fail': …} — the "
            "pair the panel prints above each authored verdict." % act_id)

    tally = a.get("tally") or ""
    if "{n}" not in tally:
        raise ValueError(
            "evidence-bench %r tally carries no {n}: it is the one live number "
            "in the block and the sentence is meaningless without it." % act_id)

    for c in cases:
        if not c.get("id"):
            raise ValueError("evidence-bench %r has a case with no id." % act_id)
        if "ok" not in c:
            raise ValueError(
                "evidence-bench %r case %r declares no `ok`. It decides which "
                "verdict label and which of the two panel grounds the case "
                "takes, and there is no safe default."
                % (act_id, c.get("id")))
        if not c.get("verdict"):
            raise ValueError(
                "evidence-bench %r case %r has no verdict; the panel would open "
                "empty." % (act_id, c.get("id")))

    rows = []
    for c in cases:
        ok = bool(c["ok"])
        rows.append(
            '<div class="ks3-ebench-case" data-case="%s" data-ok="%s">'
            '<div class="ks3-ebench-row">'
            '<div class="ks3-ebench-what">'
            '<p class="ks3-ebench-tag">%s</p>'
            '<p class="ks3-ebench-text">%s</p></div>'
            '<div class="ks3-ebench-btns">'
            '<button type="button" class="ks3-ebench-btn" data-call="1" '
            'aria-pressed="false">%s</button>'
            '<button type="button" class="ks3-ebench-btn" data-call="0" '
            'aria-pressed="false">%s</button>'
            '</div></div>'
            # The verdict is in the document from the start and hidden, not
            # built on demand: the authored sentence carries an em dash and a
            # right single quote, and nothing science-bearing is ever assembled
            # in JS.
            '<div class="ks3-ebench-verdict" hidden data-reveal>'
            '<p class="ks3-ebench-vlabel">%s</p>'
            '<p class="ks3-ebench-vtext">%s</p></div></div>'
            % (e(c["id"]), "1" if ok else "0",
               t(c.get("tag", "")), rich(c.get("text", "")),
               t(buttons["yes"]), t(buttons["no"]),
               t(labels["ok"] if ok else labels["fail"]),
               rich(c["verdict"])))

    # ⚠️ The shared-cause paragraph is STATIC MARKUP, not the tally. NOTES §3
    # flag 9 says "the tally text says so" and it is wrong: the tally is the
    # count line, and the claim the whole C1 → C2 bridge rests on is this
    # paragraph — which is why it is authored prose with an <em> in it and
    # never touched by JS.
    cause = ('<p class="ks3-ebench-cause">%s</p>' % rich(a["shared_cause"])
             if a.get("shared_cause") else "")

    return ('<div class="ks3-ebench" data-ebench data-total="%d" '
            'data-tally="%s" data-all="%s">'
            '<div class="ks3-ebench-list">%s</div>'
            '<div class="ks3-ebench-tally" hidden data-ebench-tally>'
            '<p class="ks3-ebench-tallyline" data-tallyline role="status"></p>'
            '%s</div></div>'
            % (len(cases), e(tally), e(a.get("progress_all") or ""),
               "".join(rows), cause))


# DISPATCH: "gap-test-rig": ("ks3-gap-block", ' data-instrument data-gapblock data-stage-done="0"'),
#
# Splice `r_gap_test_rig` into build_ks3.py beside the other instrument
# renderers, add the dispatch row above to ACTIVITY_KIND_RENDERERS, and add
#     if kind == "gap-test-rig":
#         parts.append(r_gap_test_rig(a, act_id))
# to r_activity's dispatch run. No new imports.


def r_gap_test_rig(a, act_id):
    """⊕ c1-01 `#s-gap` — put something in the gap and watch three tests fail.

    ⚖️ EVERY WRONG ANSWER FAILS THE SAME THREE TESTS, AND THAT IS THE
    ARGUMENT. The rig does not mark the choice. It takes whatever the student
    put in the gap, packs the space solid on the right-hand box, and then lets
    them run a test whose outcome they already know from the top of the page:
    a gas can be squashed, 50 and 50 make 97, a smell crosses a still room. The
    answer that survives is the one that never contradicts any of the three.
    Marking the option instead would turn an argument into a quiz — and R3 and
    MRB-196 R10 both say the marking belongs to the ladder.

    ⚠️ `empty_choice` IS POSITIONAL, AND IT IS AUTHORED FOR THAT REASON.
    Design's discriminator is `gapChoice !== null && gapChoice !== 3`: a bare
    index, three lines from the list it indexes, with nothing tying the two
    together. Reordering the options there inverts every outcome on the page
    silently. Here the index is authored next to its list and validated against
    it at build time, so the same edit is a build failure instead.

    ⚠️ INK-DARK (`practical`). The block's own text colours come from
    `.ks3-dark`, and `.ks3-dark p` is (0,1,1) — every text rule in this
    instrument's stylesheet is scoped past that or the note renders in the
    block's body colour instead of its own.

    ⊖ The four options are rendered HERE, not by the activity shell. The shell
    emits `options` AFTER the instrument, which would put the question below
    the answer; `choices` is the same list under a name the shell does not
    claim, and `r_activity_options` keeps the markup identical to every other
    option list in the key stage.
    """
    choices = a.get("choices") or []
    if len(choices) < 2:
        raise ValueError(
            "gap-test-rig %r offers %d choice(s); the rig contrasts an empty "
            "gap with a filled one and needs both on offer."
            % (act_id, len(choices)))

    empty = a.get("empty_choice")
    if not isinstance(empty, int) or isinstance(empty, bool) \
            or not 0 <= empty < len(choices):
        raise ValueError(
            "gap-test-rig %r sets empty_choice %r, which is not an index into "
            "its %d choices. This index decides whether every test reads its "
            "`on` or its `off` paragraph — it is the whole discriminator and "
            "may not be implied by option order."
            % (act_id, empty, len(choices)))

    tests = a.get("tests") or []
    if not tests:
        raise ValueError("gap-test-rig %r declares no tests[]." % act_id)
    for tt in tests:
        missing = [k for k in ("id", "label", "on", "off") if not tt.get(k)]
        if missing:
            raise ValueError(
                "gap-test-rig %r test %r is missing %s. Both outcomes are "
                "authored: `on` is what the test does when the gap is really "
                "empty and `off` is how it fails when it is not, and a missing "
                "one would leave a student reading the previous test's result."
                % (act_id, tt.get("id") or tt.get("label"),
                   ", ".join(missing)))

    notes = a.get("notes") or {}
    if not (notes.get("empty") and notes.get("filled")):
        raise ValueError(
            "gap-test-rig %r needs both opening notes (empty and filled) — the "
            "line a student reads after choosing and before testing." % act_id)

    labels = a.get("canvas_labels") or {}
    for key in ("empty", "filled", "foot_empty", "foot_filled"):
        if not labels.get(key):
            raise ValueError(
                "gap-test-rig %r canvas_labels is missing %r." % (act_id, key))

    alt = a.get("alt") or {}
    for key in ("template", "filled", "empty"):
        if not alt.get(key):
            raise ValueError(
                "gap-test-rig %r alt is missing %r; the two boxes exist only "
                "on the canvas." % (act_id, key))

    test_btns = "".join(
        '<button type="button" class="ks3-sim-seg-btn ks3-gap-test" '
        'data-test="%s" aria-pressed="false">%s</button>'
        % (e(tt["id"]), t(tt["label"]))
        for tt in tests)

    # Emit-both-show-one, eight ways: the two opening notes and both outcomes
    # of all three tests. Nothing here is ever assembled in JS, so an authored
    # `<em>` survives into any state and no sentence is built from an attribute.
    note_ps = ['<p data-note="empty">%s</p>' % rich(notes["empty"]),
               '<p data-note="filled" hidden>%s</p>' % rich(notes["filled"])]
    for tt in tests:
        note_ps.append('<p data-note="%s-on" hidden>%s</p>'
                       % (e(tt["id"]), rich(tt["on"])))
        note_ps.append('<p data-note="%s-off" hidden>%s</p>'
                       % (e(tt["id"]), rich(tt["off"])))

    canvas = ('<canvas class="ks3-gap-canvas" width="1800" height="520" '
              'role="img" aria-label="%s" data-gap-canvas></canvas>'
              % e(alt["template"].replace("{right}", alt["empty"])))
    foot = ('<p class="ks3-gap-caption">%s</p>'
            '<div class="ks3-gap-btns">%s</div>'
            % (t(a.get("caption", "")), test_btns))

    return ('<div class="ks3-gap" data-gap data-total="%d" '
            'data-empty-choice="%d" data-alt="%s" data-alt-filled="%s" '
            'data-alt-empty="%s" data-label-empty="%s" data-label-filled="%s" '
            'data-foot-empty="%s" data-foot-filled="%s">%s'
            '<div class="ks3-gap-rig" hidden data-gap-rig>%s'
            '<div class="ks3-gap-note" data-gap-note role="status">%s</div>'
            '</div></div>'
            % (len(tests), empty, e(alt["template"]), e(alt["filled"]),
               e(alt["empty"]), e(labels["empty"]), e(labels["filled"]),
               e(labels["foot_empty"]), e(labels["foot_filled"]),
               r_activity_options(choices),
               _canvas_frame(canvas, foot), "".join(note_ps)))


# DISPATCH: "halving-bench": ("ks3-cut-block", ' data-instrument data-cutblock data-stage-done="0"'),
#
# Splice `r_halving_bench` into build_ks3.py beside the other instrument
# renderers, add the dispatch row above to ACTIVITY_KIND_RENDERERS, and add
#     if kind == "halving-bench":
#         parts.append(r_halving_bench(a, act_id))
# to r_activity's dispatch run. `_sig` and `_size_label` are module-level
# because the RESTING render needs the same ladder the runtime uses, and two
# copies of a formatter are two answers to "how big is the piece now".

# No new imports: `build_ks3.py` does not import `math`, and the one place
# this needed it (`math.floor(v + .5)`) is `int(v + .5)` for a positive v,
# which every value on this ladder is.


# ── the size ladder (c1-01 page lines 452–464) ───────────────────────────
#
# Engine, not payload (map §1.2): 1 cm / 2ⁿ, formatted mm above 0.1 cm, µm
# above 1e-4 cm, nm below that. It is here in Python AND in `shared/ks3.js`
# for the same reason `_scale_alt` is — the build has to render the resting
# readout and the resting aria-label, and the runtime has to render every
# other state. Same composition, same output, checked at n = 0 and n = FLOOR.
#
# ⚠️ µ is U+00B5 MICRO SIGN, which Bricolage and DM Mono carry and Instrument
# Sans does not. The value lands in the DISPLAY face (`.ks3-cut-value`) and on
# the canvas in mono, so it is covered; a µ in body copy would not be.

def _sig(v):
    """Design's `sig()`, digit for digit — including the one trailing zero.

    ⚠️ `int(v + .5)`, not `round()`. JS `Math.round(312.5)` is 313 and Python's
    `round(312.5)` is 312, and 312.5 µm is a real value on this ladder (five
    cuts in). Banker's rounding here would print a different number in the built
    page from the one the student sees after the first click.
    """
    if v >= 100:
        return str(int(v + 0.5))
    if v >= 10:
        out = "%.1f" % v
        return out[:-2] if out.endswith(".0") else out
    # Design strips ONE trailing zero, then a bare point: 0.60 → 0.6, and
    # 5.00 → 5.0. Reproduced rather than tidied — the ladder's output is
    # printed on the page and in Rung 2's premise.
    out = "%.2f" % v
    if out.endswith("0"):
        out = out[:-1]
    return out[:-1] if out.endswith(".") else out


def _size_label(n, start_cm=1):
    cm = float(start_cm) / (2 ** n)
    if cm >= 0.1:
        return _sig(cm * 10) + " mm"
    if cm >= 1e-4:
        return _sig(cm * 1e4) + " µm"
    return _sig(cm * 1e7) + " nm"


_CUT_SOURCES = {"count", "size", "verdict"}
_CUT_ACTIONS = {"cut", "undo"}
_CUT_DISABLED = {"at_floor", "at_start"}
_CUT_NOTES = ("at_floor", "near_floor", "at_start", "mid")


def r_halving_bench(a, act_id):
    """⊕ c1-01 `#s-cut` — halve a sugar cube until halving runs out.

    ⚖️ THE NUMBERS ARE THE LESSON, NOT THE PICTURE. The lede says so
    ("watch the size, not the picture") and the instrument is built that way:
    three readouts, a scale bar and a progress strip, and a drawing that stays
    deliberately dull until four cuts from the floor. An instrument that made
    the cube prettier every click would teach that small is interesting; this
    one teaches that halving TERMINATES, which is a different claim and the one
    the unit rests on.

    ⚖️ THE FLOOR IS STICKY. `reachedFloor` is a one-way flag on Design's page
    and it stays one-way here: undoing a cut walks the piece back up the ladder
    and does NOT untick the rail. What a student found out at 24 cuts cannot be
    un-found by pressing undo, and MRB-208's rail records participation.

    ⚠️ A LIGHT `check` block. Measured off Design's markup (`ks3-block`, no
    `ks3-dark`), and the sibling on the same page — `#s-gap` — IS ink-dark, so
    the two are a deliberate pair rather than an oversight.

    ⊕ Additions inside the drawn component, both stated in the report:
      * `progress_full` — Design's head counter reads `floor reached` at the
        floor, which `_head_counter`'s format/zero/two-state shapes cannot
        express. Carried on the instrument and swapped in by `wireHalvingBench`.
      * `start_cm` / `grain_at` — Design hard-codes `1 /` and `FLOOR - 4` in
        two functions each. Authored once, read here and in the JS.

    ⚠️ The canvas labels ARE assembled from attributes, which the DOM rule
    forbids. Canvas text is not a DOM node: there is no element to hide and no
    `<em>` to lose, and `fillText` takes a string or nothing. Every DOM-borne
    string in this instrument — the four notes and the two verdict words — is
    emit-both-show-one instead.
    """
    floor = int(a.get("floor") or 0)
    if floor < 1:
        raise ValueError(
            "halving-bench %r declares floor %r; the bench counts down to a "
            "floor and needs a positive one." % (act_id, a.get("floor")))

    readouts = a.get("readouts") or []
    if not readouts:
        raise ValueError("halving-bench %r declares no readouts[]." % act_id)
    for r in readouts:
        if r.get("source") not in _CUT_SOURCES:
            raise ValueError(
                "halving-bench %r readout %r names source %r; the drawn set is "
                "%s." % (act_id, r.get("label"), r.get("source"),
                         ", ".join(sorted(_CUT_SOURCES))))

    buttons = a.get("buttons") or []
    if not buttons:
        raise ValueError("halving-bench %r declares no buttons[]." % act_id)
    for b in buttons:
        if b.get("action") not in _CUT_ACTIONS:
            raise ValueError(
                "halving-bench %r button %r names action %r; the bench does %s."
                % (act_id, b.get("label"), b.get("action"),
                   " and ".join(sorted(_CUT_ACTIONS))))
        if b.get("disabled_when") not in _CUT_DISABLED:
            raise ValueError(
                "halving-bench %r button %r disables on %r; the two ends are "
                "%s." % (act_id, b.get("label"), b.get("disabled_when"),
                         ", ".join(sorted(_CUT_DISABLED))))
        if int(b.get("step") or 0) < 1:
            raise ValueError(
                "halving-bench %r button %r takes step %r; a control that moves "
                "nothing is a control a student presses twice."
                % (act_id, b.get("label"), b.get("step")))

    notes = a.get("notes") or {}
    missing = [k for k in _CUT_NOTES if not notes.get(k)]
    if missing:
        raise ValueError(
            "halving-bench %r is missing note branch(es) %s. All four are "
            "authored — the floor, the grain, the untouched cube and the long "
            "middle — and a missing one would leave the student reading the "
            "previous state's sentence." % (act_id, ", ".join(missing)))

    verdict = a.get("verdict") or {}
    if not (verdict.get("open") and verdict.get("floor")):
        raise ValueError(
            "halving-bench %r needs both verdict words (open and floor)."
            % act_id)

    # ⚠️ The grain threshold squares: the drawing lays out 2^grain across and
    # 4^grain circles in total. Design's 4 gives 16 across and 256 circles, and
    # 6 is already 4,096. Bounded here rather than discovered as a frozen tab.
    grain = int(a.get("grain_at") or 0)
    if not 1 <= grain <= 6:
        raise ValueError(
            "halving-bench %r sets grain_at %r; it must be 1–6, because the "
            "drawing paints 4^grain particles (Design's 4 is 256)."
            % (act_id, a.get("grain_at")))

    alt = a.get("alt") or {}
    for key in ("template", "smooth", "grainy"):
        if not alt.get(key):
            raise ValueError(
                "halving-bench %r alt is missing %r; the readouts are in the "
                "DOM but the piece, the scale bar and the progress strip are "
                "only on the canvas, so this label is the whole drawing for a "
                "screen reader." % (act_id, key))

    labels = a.get("canvas_labels") or {}
    for key in ("ghost", "one", "many", "start", "end"):
        if not labels.get(key):
            raise ValueError(
                "halving-bench %r canvas_labels is missing %r." % (act_id, key))

    start_cm = a.get("start_cm") or 1
    gate_html, hide = r_bench_gate(a.get("gate"))

    # ── the resting state: nothing cut ──
    size0 = _size_label(0, start_cm)
    alt0 = (alt["template"].replace("{n}", "0").replace("{size}", size0)
            .replace("{tail}", alt["grainy"] if 0 >= floor - grain
                     else alt["smooth"]))

    cells = []
    for r in readouts:
        src = r["source"]
        if src == "verdict":
            # Both words in the document, one hidden. The floor word is the one
            # the stylesheet paints in accent-text, so the state is never a
            # colour JS applied.
            value = ('<span data-verdict="open">%s</span>'
                     '<span data-verdict="floor" hidden>%s</span>'
                     % (t(verdict["open"]), t(verdict["floor"])))
        elif src == "size":
            value = t(size0)
        else:
            value = "0"
        cells.append('<div class="ks3-cut-cell">'
                     '<p class="ks3-cut-label">%s</p>'
                     '<p class="ks3-cut-value" data-cut-out="%s">%s</p></div>'
                     % (t(r.get("label", "")), e(src), value))

    btns = []
    for b in buttons:
        # The resting page is at zero cuts, so an at_start control is already
        # spent and says so in the markup rather than waiting for JS.
        off = " disabled" if b["disabled_when"] == "at_start" else ""
        btns.append('<button type="button" class="ks3-sim-seg-btn ks3-cut-btn" '
                    'data-act="%s" data-step="%d" data-dis="%s"%s>%s</button>'
                    % (e(b["action"]), int(b["step"]), e(b["disabled_when"]),
                       off, t(b.get("label", ""))))

    note_ps = "".join(
        '<p data-note="%s"%s>%s</p>'
        % (e(k), "" if k == "at_start" else " hidden", rich(notes[k]))
        for k in _CUT_NOTES)

    canvas = ('<canvas class="ks3-cut-canvas" width="1800" height="640" '
              'role="img" aria-label="%s" data-cut-canvas></canvas>' % e(alt0))

    return (gate_html
            + '<div class="ks3-cut" data-cut%s data-floor="%d" '
              'data-start-cm="%s" data-grain="%d" data-full="%s" '
              'data-alt="%s" data-alt-smooth="%s" data-alt-grainy="%s" '
              'data-label-ghost="%s" data-label-one="%s" data-label-many="%s" '
              'data-label-start="%s" data-label-end="%s">'
              '<div class="ks3-cut-frame">%s'
              '<div class="ks3-cut-foot">'
              '<div class="ks3-cut-readouts">%s</div>'
              '<div class="ks3-cut-btns">%s</div></div></div>'
              '<div class="ks3-cut-note" data-cut-note role="status">%s</div>'
              '</div>'
            % (hide, floor, e(start_cm), grain,
               e(a.get("progress_full") or ""),
               e(alt["template"]), e(alt["smooth"]), e(alt["grainy"]),
               e(labels["ghost"]), e(labels["one"]), e(labels["many"]),
               e(labels["start"]),
               e(labels["end"].replace("{floor}", str(floor))),
               canvas, "".join(cells), "".join(btns), note_ps))


# DISPATCH: "heating-bench": ("ks3-hb-block", ' data-instrument data-hbblock data-stage-done="0"'),
#
# Splice into build_ks3.py beside the other C1 instruments, plus the dispatch
# line in `r_activity`:
#
#     if kind == "heating-bench":
#         parts.append(r_heating_bench(a, act_id))
#
# ⚠️ It must also be added to ks3_parity.COMPONENTS (see heating-bench.parity.py)
# and reached from `wireInstruments()` (see heating-bench.js).


# The two tones Design paints the phase word in: ordinary ink for a state that
# is simply warming, accent-text for a state that is changing. A closed map
# rather than an interpolated var() call, so a typo is a build error and never
# a `color: var(--ks3-taupe)` that resolves to nothing — same discipline as
# `_GROUNDS`.
_HB_TONES = {"ink", "accent"}

# The design-space canvas, doubled into the backing store. 900 × 330 is
# Design's own frame (c1-03 lines 467–476) and the readouts under it are DOM,
# so the only thing that has to reach a screen reader through the canvas is
# the state-bound `aria-label`.
_HB_CANVAS = (1800, 660)


def _hb_segments(keys):
    """`keys` as [(x0, t0, x1, t1), …] — one per phase band."""
    return [(keys[i][0], keys[i][1], keys[i + 1][0], keys[i + 1][1])
            for i in range(len(keys) - 1)]


def _hb_temp_at(keys, x):
    """Design's `tempAt`: piecewise-linear over the authored breakpoints."""
    for x0, t0, x1, t1 in _hb_segments(keys):
        if x <= x1:
            return t0 + (t1 - t0) * ((x - x0) / float(x1 - x0))
    return keys[-1][1]


def _hb_phase_at(keys, x):
    """The index of the band `x` falls in. Bands are [x0, x1), last inclusive."""
    for i, (x0, _t0, x1, _t1) in enumerate(_hb_segments(keys)):
        if x < x1:
            return i
    return len(keys) - 2


def _hb_round(t):
    """`Math.round` semantics, so Python and JS never disagree by one degree.

    Python's `round` takes halves to even and JS's `Math.round` takes them up;
    every readout on this bench is composed in both places, so the tie has to
    break the same way. Floor division rather than `int()` because `int()`
    truncates towards zero and this curve starts below it.
    """
    return int((t + 0.5) // 1)


def _hb_degrees(t, unit):
    """`−20 °C` — U+2212 MINUS, not a hyphen. Design's own readout (line 716).

    The unit is authored once in `labels.unit` and read here and in the JS.
    """
    n = _hb_round(t)
    return "%s%d %s" % ("−" if n < 0 else "", abs(n), unit)


def _hb_fill(template, t, label):
    """`{t}` and `{phase}`, composed the same way in Python and in JS.

    `{t}` is the plain rounded number, ASCII minus and all: it is spoken by a
    screen reader, and "minus 20" is what a reader makes of `-20`. The typeset
    U+2212 belongs on the visible readout and nowhere else.
    """
    return (template.replace("{t}", str(_hb_round(t)))
            .replace("{phase}", (label or "").lower()))


def r_heating_bench(a, act_id):
    """⊕ c1-03 `#s-curve` — scrub through a heating curve and watch it stop.

    ⚠️ A LIGHT `.ks3-block`, not a practical (map §3.3). The graph is drawn on
    cream and the readouts sit on `--ks3-inset`; on ink every token resolves
    wrong and the paper the curve is drawn on becomes a hole in the block.

    ⚖️ **THE MASS NEVER MOVES, AND IT IS NOT STATE.** `Mass in the flask ·
    50.0 g` is markup on Design's page and markup here: emitted once, never
    read by the runtime, never recomputed. It is the whole confrontation of
    the lesson — the temperature changes, the picture changes, and the one
    number that could say something was lost does not move — so the renderer
    RAISES on a bench that does not declare it rather than rendering two
    readouts and a gap.

    ⚖️ **EVERY BAND IS DERIVED FROM `keys`.** The five phase boundaries, the
    two shaded plateaus, the flask's melt and boil fractions and the head
    counter's total all come out of the same six breakpoints, so the plateau
    ratio can be corrected in one place and nothing drifts out of step with
    it. Design's page hard-codes the boundaries a second time in `phaseAt`
    (lines 459–466) and a third time in the two flask fractions (574, 592);
    all three had to agree by hand.

    ⚠️ Emit-both-show-one for the phase word and for the five plateau notes.
    Those notes are the science of the lesson and they are never rebuilt in JS
    from an attribute: all five are in the document, four are `hidden`, and
    the runtime toggles which one is shown.
    """
    keys = a.get("keys") or []
    phases = a.get("phases") or []
    labels = a.get("labels") or {}
    graph = a.get("graph") or {}
    flask = a.get("flask") or {}
    alt = a.get("alt") or {}

    if len(keys) < 2 or any(len(k) != 2 for k in keys):
        raise ValueError(
            "heating-bench %r needs keys[] as at least two [x, temperature] "
            "breakpoints." % act_id)
    xs = [k[0] for k in keys]
    if xs != sorted(xs) or len(set(xs)) != len(xs):
        raise ValueError(
            "heating-bench %r has keys[] out of order: x must increase "
            "strictly, got %s." % (act_id, xs))
    if xs[0] != 0 or xs[-1] != 100:
        raise ValueError(
            "heating-bench %r draws a curve from %s to %s; the scrub runs "
            "0–100 and the curve must span it, or the student can drag past "
            "the end of the run." % (act_id, xs[0], xs[-1]))
    if len(phases) != len(keys) - 1:
        raise ValueError(
            "heating-bench %r declares %d phase(s) for %d segment(s). One "
            "band per segment — the bands ARE the segments."
            % (act_id, len(phases), len(keys) - 1))

    segs = _hb_segments(keys)
    plateaus = [i for i, (_x0, t0, _x1, t1) in enumerate(segs) if t0 == t1]
    if not plateaus:
        raise ValueError(
            "heating-bench %r draws no plateau. A curve that only climbs is "
            "not this lesson." % act_id)
    for i, ph in enumerate(phases):
        if ph.get("tone") not in _HB_TONES:
            raise ValueError(
                "heating-bench %r phase %r tone %r; the drawn set is %s."
                % (act_id, ph.get("id"), ph.get("tone"),
                   ", ".join(sorted(_HB_TONES))))
        # A plateau carries the two captions the canvas draws over it; a ramp
        # carries neither, and authoring one on a ramp would paint a stripe
        # over a stretch that is not holding still.
        if (i in plateaus) != bool(ph.get("band")):
            raise ValueError(
                "heating-bench %r phase %r: `band` is the caption over a "
                "SHADED PLATEAU and this segment %s a plateau in keys[]."
                % (act_id, ph.get("id"), "is" if i in plateaus else "is not"))
        if (i in plateaus) != bool(ph.get("banner")):
            raise ValueError(
                "heating-bench %r phase %r: `banner` is the line drawn across "
                "the flask while the state is changing, so it belongs to a "
                "plateau and to nothing else." % (act_id, ph.get("id")))
        if not ph.get("note"):
            raise ValueError(
                "heating-bench %r phase %r has no note. The note is what the "
                "band teaches; a band without one is a colour."
                % (act_id, ph.get("id")))
    if not a.get("mass"):
        raise ValueError(
            "heating-bench %r declares no `mass`. The constant mass readout "
            "IS the confrontation of this lesson — see the module comment."
            % act_id)
    for key in ("scrub", "temperature", "phase", "mass", "unit"):
        if not labels.get(key):
            raise ValueError(
                "heating-bench %r has no labels[%r]; every readout on this "
                "bench is labelled on Design's page." % (act_id, key))
    for jump in a.get("jumps") or []:
        v = jump.get("value")
        if not isinstance(v, int) or v < 0 or v > 100:
            raise ValueError(
                "heating-bench %r jump %r targets %r, which is not a whole "
                "number on the 0–100 scrub." % (act_id, jump.get("label"), v))
    for field, template in (("alt.template", alt.get("template", "")),
                            ("valuetext", a.get("valuetext", ""))):
        if "{t}" not in template or "{phase}" not in template:
            raise ValueError(
                "heating-bench %r %s must carry both {t} and {phase}: it is "
                "the only reading a screen reader gets of a canvas."
                % (act_id, field))

    gate_html, hide = r_bench_gate(a.get("gate"))

    # The resting frame. Every value below is what the page SHOWS before any
    # JS runs, so the document is correct on its own and the first paint is
    # never a wrong number waiting to be corrected.
    start = 0
    t0 = _hb_temp_at(keys, start)
    ph0 = _hb_phase_at(keys, start)
    first = phases[ph0]

    words = "".join(
        '<span class="ks3-hb-phase" data-phase="%s" data-tone="%s"%s>%s</span>'
        % (e(ph.get("id", "")), e(ph.get("tone", "ink")),
           "" if i == ph0 else " hidden", t(ph.get("label", "")))
        for i, ph in enumerate(phases))
    notes = "".join(
        '<p class="ks3-hb-note" data-phase="%s"%s>%s</p>'
        % (e(ph.get("id", "")), "" if i == ph0 else " hidden",
           rich(ph.get("note", "")))
        for i, ph in enumerate(phases))
    jumps = "".join(
        '<button type="button" class="ks3-seg-btn ks3-hb-jump" data-v="%d" '
        'aria-pressed="%s">%s</button>'
        % (j["value"], "true" if abs(start - j["value"]) < 3 else "false",
           t(j.get("label", "")))
        for j in a.get("jumps") or [])

    sid = "ks3-hb-scrub-%s" % act_id
    cfg = {"keys": keys,
           "phases": [{"id": p.get("id", ""), "label": p.get("label", ""),
                       "band": p.get("band", ""), "banner": p.get("banner", "")}
                      for p in phases],
           "graph": graph, "flask": flask, "alt": alt,
           "valuetext": a.get("valuetext", ""), "unit": labels["unit"]}

    return (gate_html
            + '<div class="ks3-hb" data-hb%s data-total="%d" data-cfg="%s">'
              '<div class="ks3-hb-frame">'
              '<canvas class="ks3-hb-canvas" width="%d" height="%d" '
              'role="img" aria-label="%s" data-hb-canvas></canvas>'
              '<div class="ks3-hb-foot">'
              '<label class="ks3-hb-scrub-label" for="%s">%s</label>'
              '<input class="ks3-hb-scrub" id="%s" type="range" min="0" '
              'max="100" step="1" value="%d" aria-valuetext="%s" data-hb-scrub>'
              '<div class="ks3-hb-tiles">'
              '<div class="ks3-hb-tile"><p class="ks3-hb-tile-label">%s</p>'
              '<p class="ks3-hb-tile-value" data-hb-temp>%s</p></div>'
              '<div class="ks3-hb-tile"><p class="ks3-hb-tile-label">%s</p>'
              '<p class="ks3-hb-tile-value">%s</p></div>'
              # ⚠️ NO `data-` hook on the mass tile, deliberately. There is
              # nothing for the runtime to bind to, which is the point.
              '<div class="ks3-hb-tile"><p class="ks3-hb-tile-label">%s</p>'
              '<p class="ks3-hb-tile-value ks3-hb-mass">%s</p></div>'
              '</div>'
              '<div class="ks3-hb-jumps">%s</div>'
              '</div></div>'
              '<div class="ks3-hb-notes" data-hb-notes role="status">%s</div>'
              '</div>'
            % (hide, len(plateaus),
               e(json.dumps(cfg, separators=(",", ":"), sort_keys=True,
                            ensure_ascii=False)),
               _HB_CANVAS[0], _HB_CANVAS[1],
               e(_hb_fill(alt.get("template", ""), t0, first.get("label", ""))),
               e(sid), t(labels["scrub"]), e(sid), start,
               e(_hb_fill(a.get("valuetext", ""), t0, first.get("label", ""))),
               t(labels["temperature"]), t(_hb_degrees(t0, labels["unit"])),
               t(labels["phase"]), words,
               t(labels["mass"]), t(a["mass"]),
               jumps, notes))


# DISPATCH: "keyed-commit": ("ks3-keyed-block", ' data-instrument data-keyedblock data-stage-done="0"'),
#
# and in `r_activity`, beside the other kind branches:
#     if kind == "keyed-commit":
#         parts.append(r_keyed_commit(a, act_id))
#
# ⚠️ TWO GUARDS ARE REQUIRED IN `r_activity`, and the component is wrong
# without them. This kind owns its whole body — the option list AND the panel —
# so neither of the shell's generic branches may fire on the same payload:
#
#     if a.get("options") and kind != "keyed-commit":
#         parts.append(r_activity_options(a["options"]))
#     ...
#     if a.get("reveal") and kind != "keyed-commit":
#
# Without the first, `r_activity_options` calls `t()` on a dict and renders its
# repr as four answer buttons under the four real ones. Without the second, a
# lesson that spells the static paragraphs `reveal` gets a SECOND
# `.ks3-reveal-panel` that nothing ever unhides — an invisible duplicate of the
# closing prose, which is the worst of the three failure modes because it looks
# fine.
#
# THE SHARED CONTRACT (c1-03 `#s-bubble` and c1-06 `#s-verdict`), so the two
# lessons author the same shape:
#
#     options:       [{text, reply}] × 4    (or commit_options, same shape)
#     answer_index:  int                    validated here, never marked
#     closing:       [str, …]               static paragraphs, after the reply
#
# ⚠️ As delivered, c1-06 spells the last one `closing` and c1-03 spells it
# `reveal`. Both are read here, because the two lessons landed in parallel and
# refusing one would fail the build over a synonym — but ONE of them should
# win at integration and the other be renamed. `closing` is the better name: it
# is not the shell's `reveal` (which is one gated string), it never gates
# anything on its own, and the collision with the shell's key is exactly what
# makes the second guard above necessary.
#
# Place the function next to `r_evidence_bench`. Needs `e`, `t`, `rich`,
# `_option_li`.


def r_keyed_commit(a, act_id):
    """⊕ c1-06 `#s-verdict` · c1-03 `#s-bubble` — one commit, four answers.

    The nearest shipped shape is the generic `predict`, which carries prompt,
    options and ONE reveal string. Here the first paragraph of the reveal is
    the chosen option's own reply and the paragraphs after it are static, so
    the panel says something different to each of four students and then says
    the same thing to all of them. A single `reveal` cannot express that, and
    branching in code (which is what c1-03's page does — three responses keyed
    on the index) puts science-bearing prose inside the engine.

    ⚖️ PAYLOAD-MAP §6.5.2 ruled the c1-06 shape for both: the reply hangs off
    the option. That is what makes a fifth option a data change rather than a
    fifth branch, and it is why c1-03's `{correct, index_3_special_case, other}`
    is expressed as four replies here.

    ⚠️ R3 — NOTHING MARKS. `answer_index` is read at BUILD TIME only, to check
    it is in range and that the option it names carries a reply. It reaches no
    attribute, no class and no student. An activity option shows that it was
    chosen and nothing else; only the ladder marks correctness.

    Emit-both-show-one: all four replies are in the document, hidden, and one
    is unhidden. No authored sentence is rebuilt in JS, and the em dashes and
    `<em>` survive.

    ⚠️ BOTH DRAWN INSTANCES SIT ON INK. `.ks3-dark p` is (0,1,1) and beats a
    bare instrument class at (0,1,0), so every text rule in the stylesheet is
    scoped `.ks3-dark …`. There is a light fallback beside it; see the CSS.
    """
    opts = a.get("options") or a.get("commit_options") or []
    if not opts:
        raise ValueError("keyed-commit %r declares no options[]." % act_id)
    for i, o in enumerate(opts):
        if not isinstance(o, dict):
            raise ValueError(
                "keyed-commit %r option %d is %r, not a {text, reply} record. "
                "This kind takes an option that carries its own answer — that "
                "is the whole difference from a generic `predict`."
                % (act_id, i, type(o).__name__))
        if not o.get("text") or not o.get("reply"):
            raise ValueError(
                "keyed-commit %r option %d needs both `text` and `reply`; a "
                "reply-less option opens an empty panel."% (act_id, i))

    # ⚠️ Read at build time and nowhere else. It names, for the examiner, the
    # option the lesson is arguing for; a drift in the payload that moved the
    # answer past the end of the list would otherwise be silent.
    ans = a.get("answer_index")
    if ans is not None:
        if not isinstance(ans, int) or isinstance(ans, bool):
            raise ValueError(
                "keyed-commit %r answer_index is %r; it is an index into "
                "options[]." % (act_id, ans))
        if not 0 <= ans < len(opts):
            raise ValueError(
                "keyed-commit %r answer_index %d is out of range for %d "
                "option(s)." % (act_id, ans, len(opts)))

    # `reveal` is c1-03's spelling of the same list. See the header: both are
    # read, one should win at integration, and the shell's own `reveal` branch
    # must be guarded either way.
    closing = a.get("closing") or a.get("reveal") or []
    if isinstance(closing, str):
        closing = [closing]

    buttons = "".join(
        _option_li(i, o["text"], ' aria-pressed="false"')
        for i, o in enumerate(opts))

    replies = "".join(
        '<p class="ks3-keyed-reply" data-reply="%d" hidden>%s</p>'
        % (i, rich(o["reply"])) for i, o in enumerate(opts))

    statics = "".join('<p class="ks3-keyed-static">%s</p>' % rich(p)
                      for p in closing)

    return ('<div class="ks3-keyed" data-keyed>'
            '<ul class="ks3-options ks3-keyed-options" role="list">%s</ul>'
            '<div class="ks3-keyed-reveal" hidden data-reveal>%s%s</div>'
            '</div>' % (buttons, replies, statics))


# DISPATCH: "model-timeline": ("ks3-mtl-block", ' data-instrument data-mtlblock data-stage-done="0"'),
#
# and in `r_activity`, beside the other kind branches:
#     if kind == "model-timeline":
#         parts.append(r_model_timeline(a, act_id))
#
# Place the function next to `r_evidence_bench`. Needs `e`, `t`, `rich`.


def r_model_timeline(a, act_id):
    """⊕ c1-06 `#s-history` — five models, in order, one open at a time.

    ⚠️ A LIGHT `.ks3-block`, and it has NO nearest existing kind. `zoom-ladder`
    is a slider over magnifications with a tick row and an authored next-box;
    `scale-zoom` is two step buttons over five drawings. This is five named
    positions, each with a claim, a body and the evidence that killed it, and
    the step control is a **third control geometry** in the unit — left-aligned,
    `10px 14px`, a two-line stack of mono year over 700 name. It is registered
    as its own thing rather than folded into `seg()`, which is one line and one
    weight, because a year over a name is not a segment label.

    ⚠️ `default_index` IS NOT ZERO, and that is the teaching. The row opens on
    Dalton (index 1), not Democritus: Dalton is the model the student has been
    using all unit, and the point of the row is that it already has a before
    and an after. A component that opened on the first entry would put a
    twenty-century dead end in front of the student as the headline.

    ⚖️ THE RAIL PREDICATE IS A SET, NOT AN INEQUALITY. Design's page ticks this
    stage on `history !== 1`, which unticks the moment a student who has read
    all five comes back to Dalton — a rail that goes backwards. `wireModelTimeline`
    counts a set of visited indices, seeded with the default, and never empties
    it. Same class of defect as c1-04's `Math.max(touched, N)`.

    Emit-all-show-one, the same trick the board and the switch use: five detail
    cards in the document, one shown. Going back to a model finds it exactly as
    it was, no state lives anywhere but the DOM, and the 25 authored strings —
    two of which carry an arrow and a right single quote — are never rebuilt in
    JS from an attribute.
    """
    steps = a.get("steps") or []
    if not steps:
        raise ValueError("model-timeline %r declares no steps[]." % act_id)

    broke_label = a.get("broke_label")
    if not broke_label:
        raise ValueError(
            "model-timeline %r declares no broke_label — the static bold prefix "
            "on the rule-topped line, and the thing that makes the sentence a "
            "cause rather than an aside." % act_id)

    start = int(a.get("default_index") or 0)
    if not 0 <= start < len(steps):
        raise ValueError(
            "model-timeline %r opens on index %d of %d step(s)."
            % (act_id, start, len(steps)))

    for i, s in enumerate(steps):
        missing = [k for k in ("year", "who", "label", "claim", "body", "broke")
                   if not s.get(k)]
        if missing:
            raise ValueError(
                "model-timeline %r step %d (%r) is missing %s. Every one of the "
                "six is drawn, and an empty one renders as a gap in the card."
                % (act_id, i, s.get("who"), ", ".join(missing)))

    btns = "".join(
        '<button type="button" class="ks3-mtl-step" data-step="%d" '
        'aria-pressed="%s">'
        '<span class="ks3-mtl-year">%s</span>'
        '<span class="ks3-mtl-who">%s</span></button>'
        # `t()` on the year, not `e()`: 1913 → now carries U+2192, which none of
        # the five latin woff2 subsets contains. Typed as a character it drops
        # to a system font inside a 12px mono span; `t()` draws it.
        % (i, "true" if i == start else "false", t(s["year"]), t(s["who"]))
        for i, s in enumerate(steps))

    cards = "".join(
        '<div class="ks3-mtl-card" data-step="%d"%s>'
        '<p class="ks3-mtl-label">%s</p>'
        '<p class="ks3-mtl-claim">%s</p>'
        '<p class="ks3-mtl-body">%s</p>'
        '<p class="ks3-mtl-broke"><strong>%s</strong> %s</p></div>'
        % (i, "" if i == start else " hidden",
           t(s["label"]), rich(s["claim"]), rich(s["body"]),
           t(broke_label), rich(s["broke"]))
        for i, s in enumerate(steps))

    return ('<div class="ks3-mtl" data-mtl data-total="%d" data-default="%d">'
            '<div class="ks3-mtl-steps">%s</div>'
            '<div class="ks3-mtl-cards">%s</div></div>'
            % (len(steps), start, btns, cards))


# DISPATCH: "prediction-stack": ("ks3-predict-block", ' data-instrument data-predictblock data-stage-done="0"'),
#
# Splice point: `ACTIVITY_KIND_RENDERERS` in build_ks3.py, in the new
# "C1 · Particles and their behaviour" section. Also add to `r_activity`:
#
#     if kind == "prediction-stack":
#         parts.append(r_prediction_stack(a, act_id))
#
# The function below belongs beside the other C1 renderers and uses `e`, `t`
# and `rich`, all of which build_ks3.py already defines.


def r_prediction_stack(a, act_id):
    """⊕ c1-04 `#s-predict` — three predictions in one block, one option set.

    ⚠️ NOT the generic `predict` kind. That is one prompt, one option list and
    one reveal; this is three questions that share an option set, each with its
    own answer index and its own note, and rendering it as the generic shell
    would keep the first question and lose the other two.

    ⚖️ THE THREE ARE COMPARABLE BECAUSE THE OPTIONS ARE SHARED. `Goes up /
    Stays the same / Goes down` is asked about three different single changes,
    so a student who answers all three has produced a small table of the
    model's behaviour rather than three unrelated multiple choices. Authoring
    the options once is what makes that true rather than coincidental.

    ⚖️ ONE SHARED WRONG-ANSWER NOTE, and it deliberately does not give the
    answer: it sends the student back up to the bench, which is the only place
    on the page that can settle it. Three per-prediction wrong notes would be
    three more chances to leak the right one. Design authors it inside
    `renderVals` (page line 738), so it is not in the extracted constants and
    was lifted by hand.

    ⚠️ INK-DARK. `.ks3-dark p` is (0,1,1) and beats a bare instrument class at
    (0,1,0), so every text rule in the stylesheet is self-scoped
    `.ks3-predict …` at (0,2,0). Two separate builds have shipped this defect.

    ⚑ Design paints the RIGHT panel's border in `--ks3-alert` and the WRONG
    note's text in `--ks3-alert` too — the same token doing two jobs three
    lines apart. On ink the palette has already swapped accent → alert for
    every lit state (`.ks3-dark .ks3-sim-seg-btn[aria-pressed="true"]`), so
    this is consistent with the system rather than with §8's "amber is a wrong
    idea"; reproduced as drawn and recorded here so it is a decision rather
    than an accident.
    """
    preds = a.get("predictions") or []
    # ⚠️ `shared_options`, NOT `options`. `options` is the SHELL's key —
    # `r_activity` renders any `options` it finds as a standard A/B/C answer
    # list — so authoring the shared set under that name emits a fourth,
    # orphaned copy of the three choices below the three panels, answering no
    # question. The map's payload block calls it `options`; that name is taken.
    options = a.get("shared_options") or []
    wrong = a.get("wrong_note") or ""

    if not preds:
        raise ValueError(
            "prediction-stack %r declares no predictions[]." % act_id)
    if len(options) < 2:
        raise ValueError(
            "prediction-stack %r needs the shared options[] — the three "
            "predictions are only comparable because they are asked the same "
            "way; got %r." % (act_id, options))
    if not wrong:
        raise ValueError(
            "prediction-stack %r has no `wrong_note`. One shared fallback is "
            "the whole shape: without it a wrong answer gets silence."
            % act_id)
    for p in preds:
        if not p.get("id") or not p.get("question") or not p.get("note"):
            raise ValueError(
                "prediction-stack %r: every prediction needs `id`, `question` "
                "and `note`; got %r." % (act_id, p))
        ans = p.get("answer")
        if not isinstance(ans, int) or not 0 <= ans < len(options):
            raise ValueError(
                "prediction-stack %r: prediction %r answers %r, which is not "
                "an index into the %d shared options."
                % (act_id, p.get("id"), ans, len(options)))

    panels = []
    for p in preds:
        # `.ks3-sim-seg-btn` on the dark ground gives Design's own `segDark`
        # pair: the lit state is the alert yellow with ink text, the resting
        # state transparent on the muted rule. A private control here would be
        # a second copy of a ruled one.
        btns = "".join(
            '<button type="button" class="ks3-sim-seg-btn ks3-predict-btn" '
            'data-i="%d" aria-pressed="false">%s</button>'
            % (i, t(opt)) for i, opt in enumerate(options))
        # Emit-both-show-one. Both notes are in the document and one is
        # hidden, so no student-facing string is ever assembled in JS and any
        # `<em>` in an authored note survives. The live region is the WRAPPER,
        # never the instrument root.
        panels.append(
            '<div class="ks3-predict" data-prediction="%s" '
            'data-answer="%d">'
            '<p class="ks3-predict-q">%s</p>'
            '<div class="ks3-predict-btns">%s</div>'
            '<div class="ks3-predict-notes" data-predict-notes role="status">'
            '<p class="ks3-predict-note" data-tone="right" hidden>%s</p>'
            '<p class="ks3-predict-note" data-tone="wrong" hidden>%s</p>'
            '</div></div>'
            % (e(p["id"]), int(p["answer"]), t(p["question"]), btns,
               rich(p["note"]), rich(wrong)))

    return ('<div class="ks3-predicts" data-predictstack data-total="%d">%s'
            '</div>' % (len(preds), "".join(panels)))


# DISPATCH: "random-walk-bench": ("ks3-walk-block", ' data-instrument data-walkblock data-stage-done="0"'),
#
# Goes in ACTIVITY_KIND_RENDERERS beside the C2 entries, plus the two lines
# `r_activity` needs:
#
#     if kind == "random-walk-bench":
#         parts.append(r_random_walk_bench(a, act_id))
#
# Place `_walk_alt` and `r_random_walk_bench` after `r_scale_zoom` in
# build_ks3.py. Needs `json`, `e`, `t`, `rich`, `r_bench_gate` — all already
# in scope there.


def _walk_alt(alt, even, left, right):
    """The tank canvas's aria-label. Composed the same way in JS.

    ⊕ `{left}` and `{right}` are an ADDITION to Design's sentence, and the
    reason is the c1-04 ruling reached by a different route: the half counts
    are DRAWN INSIDE the canvas (page lines 534–535) and appear nowhere in the
    DOM, so without them in the label a screen-reader user is told a bar chart
    exists and never told what it says. Design's own clause is unchanged; one
    sentence is appended.
    """
    return (alt.get("template", "")
            .replace("{state}", alt.get("even" if even else "uneven", ""))
            .replace("{left}", str(left))
            .replace("{right}", str(right)))


def r_random_walk_bench(a, act_id):
    """⊕ c1-05 `#s-walk` — 130 particles, no one steering.

    ⚠️ A LIGHT `.ks3-block`, not a practical. Design draws the tank on cream
    inside a card-ground frame; painting it on ink resolves every text token
    wrong and turns the dye purple-on-black. Same trap the map names for
    c2-01's claim switch.

    ⚖️ **THE TWO CROSSING COUNTERS NEVER RESET WHEN THE TANK EVENS OUT.** They
    are cleared by "Put the drop back" and by nothing else (page lines
    439–440). That is the whole confrontation of `PART-11`: the spreading
    finishes and the moving does not, and a student watching the two numbers
    climb together after "Spread out? Yes" is reading the argument rather than
    being told it. `#s-think`'s reveal then quotes those counters in words. An
    optimisation that zeroed them on `even` would delete the lesson and leave
    an animation.

    ⚠️ THE FOUR NOTES ARE ALL IN THE DOCUMENT AND ONE IS SHOWN. Emit-both-
    show-one, because a note is a science sentence and JS must never rebuild
    one from an attribute — `<em>` would not survive the round trip and a
    string assembled in two places is a string that drifts in one of them.

    ⚠️ The canvas frame here is NOT `_canvas_frame`. That wrapper is the DARK
    one — a 2px `--ks3-on-dark-muted` rule over a `--ks3-dark-panel` foot — and
    this bench is light: a 2px INK rule over a `--ks3-inset` foot. Two grounds,
    two components; reusing the dark one would put an on-dark border on cream.
    """
    n = int(a.get("particles") or 0)
    labels = a.get("labels") or {}
    canvas_labels = a.get("canvas_labels") or {}
    notes = a.get("notes") or {}
    progress = a.get("progress") or {}
    alt = a.get("alt") or {}
    seed = a.get("seed") or {}
    step = a.get("step") or {}
    bounds = a.get("bounds") or {}
    even = a.get("even") or {}

    if n < 2:
        raise ValueError(
            "random-walk-bench %r seeds %d particle(s); the instrument is a "
            "crowd leaving one side and needs a crowd." % (act_id, n))

    need = {
        "labels": (labels, ("cross_right", "cross_left", "even", "even_yes",
                            "even_no", "run_start", "run_pause",
                            "run_continue", "reset", "trace_on", "trace_off",
                            "warm_on", "warm_off")),
        "canvas_labels": (canvas_labels, ("left_half", "right_half",
                                          "profile")),
        # Four branches, and all four are Design's. A missing one would render
        # as an empty panel at exactly the moment the bench has something to
        # say — see `walkNote`, page lines 575–584.
        "notes": (notes, ("idle", "spreading", "even", "tracing")),
        "progress": (progress, ("idle", "spreading", "even")),
        "alt": (alt, ("template", "even", "uneven")),
        "seed": (seed, ("x", "y")),
        "step": (step, ("cool", "warm", "y_scale")),
        "bounds": (bounds, ("x", "y")),
        "even": (even, ("tolerance", "hz")),
    }
    for key, (got, wanted) in sorted(need.items()):
        missing = [k for k in wanted if got.get(k) in (None, "")]
        if missing:
            raise ValueError(
                "random-walk-bench %r is missing %s: %s."
                % (act_id, key, ", ".join(missing)))
    for key in ("trail_max", "bins", "reduced_scale"):
        if not a.get(key):
            raise ValueError(
                "random-walk-bench %r declares no %s." % (act_id, key))

    # ⊕ The block head's readout and `progress.idle` are the SAME WORD in two
    # records — the resting render comes from `head_counter`, the live one from
    # `progress` — so they are checked against each other rather than trusted.
    # Drift here is invisible: the page would open on one word and change to a
    # different one the first time anything is pressed.
    opening = ((a.get("head_counter") or {}).get("start_extra") or {}).get("phase")
    if opening != progress["idle"]:
        raise ValueError(
            "random-walk-bench %r opens its head counter on %r and its live "
            "readout on %r. They are the same readout and must be the same "
            "word." % (act_id, opening, progress["idle"]))

    gate_html, hide = r_bench_gate(a.get("gate"))

    cfg = {"particles": n, "seed": seed, "step": step, "bounds": bounds,
           "even": even, "trail_max": int(a["trail_max"]),
           "bins": int(a["bins"]), "reduced_scale": a["reduced_scale"],
           "canvas_labels": canvas_labels, "alt": alt, "progress": progress}

    def readout(label, inner, extra=""):
        return ('<div class="ks3-walk-readout">'
                '<p class="ks3-walk-readout-label">%s</p>'
                '<p class="ks3-walk-readout-value"%s>%s</p></div>'
                % (t(label), extra, inner))

    # Both words are present and one is hidden — the same rule as the notes.
    # "Yes" and "Not yet" are the answer to the question the gate asked.
    even_words = ('<span data-walk-even-no>%s</span>'
                  '<span data-walk-even-yes hidden>%s</span>'
                  % (t(labels["even_no"]), t(labels["even_yes"])))

    readouts = (readout(labels["cross_right"], "0", " data-walk-cross-right")
                + readout(labels["cross_left"], "0", " data-walk-cross-left")
                + readout(labels["even"], even_words, ' data-walk-even="0"'))

    def swap(attr, pairs, first):
        """A control whose LABEL changes with its state, one span per label."""
        return "".join(
            '<span data-%s="%s"%s>%s</span>'
            % (attr, e(key), "" if key == first else " hidden", t(text))
            for key, text in pairs)

    controls = (
        '<button type="button" class="ks3-sim-seg-btn ks3-walk-btn" '
        'data-walk-run aria-pressed="false">%s</button>'
        '<button type="button" class="ks3-sim-seg-btn ks3-walk-btn" '
        'data-walk-reset>%s</button>'
        '<button type="button" class="ks3-sim-seg-btn ks3-walk-btn" '
        'data-walk-trace aria-pressed="false">%s</button>'
        '<button type="button" class="ks3-sim-seg-btn ks3-walk-btn" '
        'data-walk-warm aria-pressed="false">%s</button>'
        % (swap("run-label", (("start", labels["run_start"]),
                              ("pause", labels["run_pause"]),
                              ("continue", labels["run_continue"])), "start"),
           t(labels["reset"]),
           swap("trace-label", (("on", labels["trace_on"]),
                                ("off", labels["trace_off"])), "on"),
           swap("warm-label", (("on", labels["warm_on"]),
                               ("off", labels["warm_off"])), "on")))

    note_html = "".join(
        '<p data-note="%s"%s>%s</p>'
        % (e(key), "" if key == "idle" else " hidden", rich(notes[key]))
        for key in ("idle", "spreading", "even", "tracing"))

    return (gate_html
            + '<div class="ks3-walk" data-walk%s data-cfg="%s">'
              '<div class="ks3-walk-frame">'
              '<canvas class="ks3-walk-canvas" width="1800" height="640" '
              'role="img" aria-label="%s" data-walk-canvas></canvas>'
              '<div class="ks3-walk-foot">'
              '<div class="ks3-walk-readouts">%s</div>'
              '<div class="ks3-walk-controls">%s</div>'
              '</div></div>'
              # `role="status"` on the note panel, never on the instrument
              # root: the root contains the canvas and the counters, and a live
              # region over a 60 fps drawing announces nothing usable.
              '<div class="ks3-walk-note" data-walk-note role="status">%s</div>'
              '</div>'
            % (hide,
               e(json.dumps(cfg, separators=(",", ":"), sort_keys=True,
                            ensure_ascii=False)),
               e(_walk_alt(alt, False, n, 0)),
               readouts, controls, note_html))


# DISPATCH: "scale-cards": ("ks3-scards-block", " data-instrument data-scalecards"),
#
# NOTE THE ABSENT `data-stage-done`. This kind has no completion contract —
# see the docstring — so it takes the same entry shape as `confrontation`
# rather than the instrument shape. Emitting the attribute would declare a
# contract the section can never discharge, and the stage would sit at 0 for
# ever.
#
# Plus the two lines `r_activity` needs:
#
#     if kind == "scale-cards":
#         parts.append(r_scale_cards(a, act_id))
#
# Place after `r_random_walk_bench` in build_ks3.py. Needs `e`, `t`, `rich`.


def r_scale_cards(a, act_id):
    """⊕ c1-05 `#s-scale` — a distance, a time, and what that costs biology.

    ⚠️ **NOT `reveal-cards`, and this is a build decision with a gate behind
    it.** The nearest existing shape is `r_cards`, and it is wrong three times
    over: these do not flip, there is nothing behind them to reveal, and
    `verify_ks3.py` §5.1.2(a) requires every card grid to ask for a commitment
    in words before the tap. This block asks for nothing — it is the pay-off
    after the bench, not another task — so forcing it into `reveal-cards` would
    either fail that gate or, worse, make somebody write a fake commit prompt
    to satisfy it. A static three-up panel is its own component.

    ⚠️ INK-DARK, so every `<p>` rule in the stylesheet is scoped past
    `.ks3-dark p`, which is (0,1,1) and beats a bare instrument class at
    (0,1,0). The 28px display TIME is the one that would visibly break: it
    would fall back to on-dark BODY colour and read as a caption.

    ⚑ `--ks3-alert` on the distance label is Design's, and the map flags it
    (§5.5.2). Amber on ink is established for CONTROLS since B1; this is amber
    for BODY LABELLING, which is new, and README.txt's "amber is reserved for
    misconceptions" is about blocks rather than either. Reproduced as drawn and
    left flagged — a build is not the place to re-rule a palette question. The
    parity row registers the value, so the day it IS re-ruled the gate says so.
    """
    cards = a.get("scale_cards") or []
    if len(cards) < 2:
        raise ValueError(
            "scale-cards %r draws %d card(s); the panel is a comparison and "
            "needs at least two." % (act_id, len(cards)))
    for i, c in enumerate(cards):
        missing = [k for k in ("distance", "time", "text") if not c.get(k)]
        if missing:
            raise ValueError(
                "scale-cards %r card %d is missing %s. All three lines carry "
                "the comparison — a card with no time says nothing."
                % (act_id, i + 1, ", ".join(missing)))
    if not a.get("close"):
        raise ValueError(
            "scale-cards %r declares no `close`. The closing line is what "
            "turns three numbers into a rule (\"double the distance and "
            "diffusion takes four times as long\"); without it the panel is "
            "three facts and no argument." % act_id)

    grid = "".join(
        '<div class="ks3-scard">'
        '<p class="ks3-scard-distance">%s</p>'
        '<p class="ks3-scard-time">%s</p>'
        '<p class="ks3-scard-text">%s</p></div>'
        % (t(c["distance"]), t(c["time"]), rich(c["text"]))
        for c in cards)

    return ('<div class="ks3-scards">%s</div>'
            '<p class="ks3-scards-close">%s</p>' % (grid, rich(a["close"])))


# DISPATCH: "sort-cards": ("ks3-sortcards-block", ' data-instrument data-sortcardsblock data-stage-done="0"'),
#
# Splice into build_ks3.py beside the other C1 instruments, plus the dispatch
# line in `r_activity`:
#
#     if kind == "sort-cards":
#         parts.append(r_sort_cards(a, act_id))
#
# ⚠️ It renders INSIDE the `misconception` shell (see ks3_data/c1/__init__.py's
# `_INSTRUMENT_SEGMENTS`), so `r_activity` emits the amber head, then
# `r_confrontation`'s quote, then the lede, then this. Nothing about the
# confrontation path changes.


def r_sort_cards(a, act_id):
    """⊕ c1-03 `#s-think` — four things, and the word that fits each one.

    ⚠️ NOT `verdict-cards` and NOT `job-sort`, and the difference is the whole
    mechanism. Both of those are ONE-SHOT: the first press disables the row's
    other options, because their reveal is an answer and a second press would
    be choosing after reading it. Design's sorter stays open — press Melting,
    read why it is not melting, press Dissolving, and the card follows you.
    That is the page as drawn, and it is also what the lede promises: *"the
    sorting is the point, not the score"*. Locking it would make the block a
    test, which is the thing the sentence says it is not.

    ⚠️ **THIS IS THE ONE PLACE IN C1 WHERE A CARD MARKS THE ANSWER**, and it
    is Design's rule as measured (map §3.5.3, page lines 767–770): the card's
    border goes to `--ks3-accent` when the choice matches and `--ks3-ink` when
    it does not, and the note is ink or accent-text to match. It is carried
    because the page wins over the engine, and it is expressed as ONE
    ATTRIBUTE — `data-verdict` on the card — so that if R3 is ever ruled to
    reach this component the change is two lines of CSS and nothing else
    moves. Note that the marking is never the ok/alert family: it cannot be
    confused with the ladder's verdict, and the wrong state takes exactly the
    neutral ink border every decided `job-sort` row already takes.

    ⚠️ Emit-both-show-one. Each card carries BOTH authored notes, one hidden;
    no sentence is ever assembled in JS from an attribute.
    """
    items = a.get("items") or []
    buttons = a.get("buttons") or []
    if not items:
        raise ValueError("sort-cards %r declares no items[]." % act_id)
    if len(buttons) != 2:
        raise ValueError(
            "sort-cards %r offers %d button(s); it is a binary verdict — one "
            "word against the other — and a third column is a different "
            "component." % (act_id, len(buttons)))
    values = [b.get("value") for b in buttons]
    if len(set(values)) != 2 or not all(values):
        raise ValueError(
            "sort-cards %r buttons need two distinct `value`s; got %r."
            % (act_id, values))
    for it in items:
        # ⚠️ ANSWER VALIDATION, unlike `job-sort` and `verdict-cards` — and it
        # is right here for the reason it is wrong there. Those two answer in
        # free sentences that are deliberately not one of the offered options;
        # this one answers with the button's own value, and the value decides
        # which of the two authored notes a student reads. An answer that
        # matches no button would show every card the wrong note, silently.
        if it.get("answer") not in values:
            raise ValueError(
                "sort-cards %r item %r answers %r, which is not one of the "
                "two buttons %r." % (act_id, it.get("id"), it.get("answer"),
                                     values))
        for side in ("right", "wrong"):
            if not it.get(side):
                raise ValueError(
                    "sort-cards %r item %r has no %r note. Both are authored "
                    "on Design's page and both are read: the card answers the "
                    "choice the student actually made."
                    % (act_id, it.get("id"), side))

    cards = []
    for it in items:
        opts = "".join(
            '<button type="button" class="ks3-seg-btn ks3-sortcards-opt" '
            'data-choice="%s" aria-pressed="false">%s</button>'
            % (e(b["value"]), t(b.get("label", "")))
            for b in buttons)
        cards.append(
            '<div class="ks3-sortcards-card" data-card="%s" data-answer="%s">'
            '<p class="ks3-sortcards-text">%s</p>'
            '<div class="ks3-sortcards-opts">%s</div>'
            '<p class="ks3-sortcards-note" data-note="right" hidden>%s</p>'
            '<p class="ks3-sortcards-note" data-note="wrong" hidden>%s</p>'
            '</div>'
            % (e(it.get("id", "")), e(it["answer"]), rich(it.get("text", "")),
               opts, rich(it["right"]), rich(it["wrong"])))

    # The whole-set summary, gated on all four. It is the payoff for sorting
    # rather than reading, so it does not exist in the document's flow until
    # the sorting is done.
    summary = ""
    if a.get("summary"):
        summary = ('<div class="ks3-sortcards-close" hidden '
                   'data-sortcards-close>%s</div>'
                   % "".join("<p>%s</p>" % rich(p) for p in a["summary"]))

    return ('<div class="ks3-sortcards" data-sortcards data-total="%d">'
            '<div class="ks3-sortcards-grid">%s</div>%s</div>'
            % (len(items), "".join(cards), summary))


# DISPATCH: "state-bench": ("ks3-sbench-block", ' data-instrument data-sbenchblock data-stage-done="0"'),
#
# Splice `r_state_bench` into build_ks3.py beside the other C1 instruments, and
# add `if kind == "state-bench": parts.append(r_state_bench(a, act_id))` to
# `r_activity`'s dispatch run.


def r_state_bench(a, act_id):
    """⊕ c1-02 `#s-bench` — one substance, three arrangements, on a canvas.

    ⚠️ A LIGHT `.ks3-block`, not a practical. c1-02 is the only C1 lesson with
    no dark ground but the hook and the keynote (map §2.3), and the particle
    drawing is cream-on-cream: painting the shell ink would resolve every text
    token wrong and put a #FFFDF8 canvas on a #221E1B block.

    ⚖️ THE FIXED-SIZE REFERENCE PARTICLE IS THE LESSON. NOTES §3 flag 3 names
    it non-negotiable, and it is: one particle, the same radius as every
    particle in every state, captioned, drawn under the box in all three states
    and in every setting. It is the visible form of the sentence the whole
    lesson defends — the particles do not change, the spaces do. So
    `reference_particle` is REQUIRED and this raises without it, rather than
    rendering a bench that has quietly lost its argument to a layout tidy-up.

    ⚖️ EIGHT NOTES, ALL IN THE DOCUMENT, SEVEN HIDDEN. squash × 2, paths × 3,
    resting × 3. Emit-both-show-one rather than a `textContent` swap out of an
    attribute: these are the sentences that carry the science, and rebuilding
    one in JS is how an `<em>` gets eaten and how a string ends up living in an
    attribute where nothing reviews it. The two toggle LABELS take the same
    treatment for the same reason — each is a pair of authored words and
    neither is composed.

    ⚠️ NOT `particle-states`. `SIM_ARIA`'s box-of-particles is driven by a
    TEMPERATURE SLIDER and `SIM_CONTROLS` offers temperature / volume /
    particles / medium. Design's bench has no temperature control at all: it has
    three named state buttons, a motion toggle, a path toggle and a squash
    toggle. Rendering it as the sim would hand the student a dial Design did not
    draw and hide three Design did — the MRB-205 failure exactly (map §2.6).

    ⊕ The counter opens at ZERO. Design's `benchProgress` (page line 614) adds
    one for the state the bench is *about* to show, so an untouched page reads
    "1 of 3 states seen" above a bench still behind its gate. `head_counter`
    carries `start: 0`; the gate banks the opening state when it is answered,
    which is the first moment a student has seen anything.
    """
    states = a.get("states") or []
    if not states:
        raise ValueError("state-bench %r declares no states[]." % act_id)
    for s in states:
        missing = [k for k in ("key", "label", "alt") if not s.get(k)]
        if missing:
            raise ValueError(
                "state-bench %r state %r is missing %s. `label` is the button "
                "face AND the caption the canvas prints; `alt` is that state's "
                "whole aria-label, authored as one finished sentence rather "
                "than composed at runtime from the key."
                % (act_id, s.get("key"), ", ".join(missing)))
    keys = [s["key"] for s in states]

    ref = a.get("reference_particle")
    if not ref:
        raise ValueError(
            "state-bench %r authors no `reference_particle`. NOTES §3 flag 3 "
            "makes the fixed-size reference particle and its caption "
            "non-negotiable — it is the drawn form of the claim the lesson "
            "exists to defend, and a bench without it is a picture of three "
            "arrangements with the argument removed." % act_id)

    banner = a.get("squash_banner") or {}
    for k in ("gas", "other"):
        if not banner.get(k):
            raise ValueError(
                "state-bench %r squash_banner is missing %r; the piston prints "
                "one of two authored lines and there is no third." % (act_id, k))

    ctl = a.get("controls") or {}
    pairs = (("motion", "running", "frozen"), ("trails", "shown", "hidden"))
    for name, on_key, off_key in pairs:
        c = ctl.get(name) or {}
        if not (c.get(on_key) and c.get(off_key)):
            raise ValueError(
                "state-bench %r control %r needs both %r and %r. The label is "
                "keyed by the state the control is IN, never by what pressing "
                "it does, so the two can never be swapped by accident."
                % (act_id, name, on_key, off_key))
    if not (ctl.get("squash") or {}).get("label"):
        raise ValueError(
            "state-bench %r control 'squash' needs a `label`." % act_id)

    notes = a.get("notes") or {}
    for k in ("gas", "other"):
        if not (notes.get("squash") or {}).get(k):
            raise ValueError(
                "state-bench %r notes.squash is missing %r." % (act_id, k))
    for group in ("trails", "rest"):
        for k in keys:
            if not (notes.get(group) or {}).get(k):
                raise ValueError(
                    "state-bench %r notes.%s is missing state %r; every state "
                    "answers every instrument." % (act_id, group, k))

    groups = a.get("groups") or {}
    gate_html, hide = r_bench_gate(a.get("gate") or {})
    first = states[0]

    # ── the state row ──
    # `aria-pressed` on the opening state is TRUE because it is where the bench
    # is, and this is a segmented picker rather than an answer: R3 is untouched,
    # nothing here is marked right or wrong. `data-instrument` on the section is
    # what keeps `wirePredictions` off these buttons.
    state_btns = "".join(
        '<button type="button" class="ks3-sbench-seg" data-sbench-state="%s" '
        'aria-pressed="%s">%s</button>'
        % (e(s["key"]), "true" if i == 0 else "false", t(s["label"]))
        for i, s in enumerate(states))

    # ── the instrument row ──
    # ⊕ CORRECTED: `aria-pressed` follows the TINT, not Design's `motionOn`.
    # Design draws the motion button lit when the motion is FROZEN
    # (`motionStyle: this.seg(!s.motion)`, line 711) and announces
    # `aria-pressed="true"` when it is RUNNING (line 709) — so a screen reader
    # hears "pressed" on a control that looks unpressed, and hears nothing
    # change when a student freezes the bench. Its own sibling, the paths
    # toggle, is consistent (lit and pressed both mean "paths are on"). This is
    # a slip rather than an intention, and R2 requires the announced state and
    # the visible state to be the same state, so the announcement is moved onto
    # the tint rather than the tint onto the announcement — the alternative
    # would light the button on page load, before the student has touched it.
    def toggle(name, on_label, off_label, pressed):
        return ('<button type="button" class="ks3-sbench-seg" data-sbench-%s '
                'aria-pressed="%s">'
                '<span data-lbl="on"%s>%s</span>'
                '<span data-lbl="off"%s>%s</span></button>'
                % (name, "true" if pressed else "false",
                   "" if pressed else " hidden", t(on_label),
                   " hidden" if pressed else "", t(off_label)))

    motion = ctl["motion"]
    trails = ctl["trails"]
    # The bench opens with the motion RUNNING and the paths hidden, so the
    # motion button shows "Freeze the motion" unpressed and the paths button
    # shows "Show the paths" unpressed. Nothing is lit until the student acts.
    inst_btns = (
        toggle("motion", motion["frozen"], motion["running"], False)
        + toggle("trails", trails["shown"], trails["hidden"], False)
        + '<button type="button" class="ks3-sbench-seg" data-sbench-squash '
          'aria-pressed="false">%s</button>' % t(ctl["squash"]["label"]))

    # ── the eight notes, all present, seven hidden ──
    # The resting note for the opening state is the one shown, which is what a
    # student reads the instant the gate is answered.
    live = "rest:%s" % first["key"]
    rows = []
    for group in ("squash", "trails", "rest"):
        for k, text in sorted((notes.get(group) or {}).items()):
            nid = "%s:%s" % (group, k)
            rows.append('<p class="ks3-sbench-note-text" data-note="%s"%s>%s</p>'
                        % (e(nid), "" if nid == live else " hidden",
                           rich(text)))

    # ⚠️ `role="status"` on the NOTE, never on the instrument root and never on
    # the gated body. A live region wrapped round the whole bench would
    # re-announce the canvas, both control groups and the note every time a
    # student pressed a toggle; wrapped round the note it announces exactly the
    # sentence that changed. `wireStateBench` therefore opens the gate itself
    # rather than calling `wireBenchGate`, which sets `role="status"` on
    # `[data-benchbody]` — see the wire function.
    note_html = ('<div class="ks3-sbench-note" data-sbench-note role="status">'
                 '%s</div>' % "".join(rows))

    canvas = ('<canvas class="ks3-sbench-canvas" width="1800" height="620" '
              'role="img" aria-label="%s" data-sbench-canvas></canvas>'
              % e(first["alt"]))

    foot = ('<div class="ks3-sbench-foot">'
            '<div class="ks3-sbench-group">'
            '<p class="ks3-sbench-grouplabel">%s</p>'
            '<div class="ks3-sbench-row">%s</div></div>'
            '<div class="ks3-sbench-group">'
            '<p class="ks3-sbench-grouplabel">%s</p>'
            '<div class="ks3-sbench-row">%s</div></div></div>'
            % (t(groups.get("states") or ""), state_btns,
               t(groups.get("instruments") or ""), inst_btns))

    # ⊕ The published state lives on the WRAPPER, which is never hidden, so
    # `state-matrix` can read it whether or not the gate has been answered and
    # whatever order the two instruments happen to wire in. These four
    # attributes are the single source of truth for the bench's settings —
    # nothing keeps a second copy (map §2.5.2's cross-block capability).
    return (gate_html
            + '<div class="ks3-sbench" data-sbench data-state="%s" '
              'data-motion="1" data-trails="0" data-squash="0" '
              'data-states="%s" data-banner-gas="%s" data-banner-other="%s" '
              'data-reference="%s"%s>'
              '<div class="ks3-sbench-body"%s>'
              '<div class="ks3-sbench-frame">%s%s</div>%s</div></div>'
            % (e(first["key"]),
               e(json.dumps([{"key": s["key"], "label": s["label"],
                              "alt": s["alt"]} for s in states],
                            separators=(",", ":"), sort_keys=True,
                            ensure_ascii=False)),
               e(banner["gas"]), e(banner["other"]), e(ref),
               # Design's `benchProgress` reads "all three seen" once every
               # state has been visited, and `_head_counter` has no slot for a
               # bespoke FULL string (it has `zero`, which is the other end).
               # Carried here and written by the wire function, so the sentence
               # is authored exactly once.
               (' data-full="%s"' % e(a["progress_full"]))
               if a.get("progress_full") else "",
               hide, canvas, foot, note_html))


# DISPATCH: "state-matrix": ("ks3-smatrix-block", ' data-instrument data-smatrixblock'),
#
# ⚠️ NO `data-stage-done`. Deliberate, and the same shape as `confrontation`'s
# entry: the attribute declares a completion contract, and `#s-matrix` has
# nothing a student can discharge. See the docstring and the lesson module.
#
# Splice `r_state_matrix` into build_ks3.py beside the other C1 instruments, and
# add `if kind == "state-matrix": parts.append(r_state_matrix(a, act_id))` to
# `r_activity`'s dispatch run.


def r_state_matrix(a, act_id):
    """⊕ c1-02 `#s-matrix` — six properties, three states, one row lit.

    ⚠️ NOT `r_comparison`. That is b1-06's shape: a fixed TWO-column "this one
    against that one" table with a dark header row. This is a four-column
    property matrix with a live-highlighted row, and the highlight is driven by
    a DIFFERENT BLOCK's controls. Rendering it as a comparison would give the
    student two columns for a three-state contrast and drop the mechanism
    entirely (map §2.5.2).

    ⊕ CROSS-BLOCK STATE — the first of it in the key stage. No existing KS3
    component reads another block's state, and the temptation is to give this
    one its own copy of squash/paths and keep the two in step. It does not: the
    bench publishes its settings on `[data-sbench]` and the matrix READS them,
    so there is exactly one place the bench's state lives and no way for a
    second copy to drift. `highlight_from` names the section to look in;
    `highlight` maps a bench condition to a row key.

    ⚖️ IT IS NOT A RAIL STOP, and the lesson module does not list it as one.
    Design's stage 3 ticks on `Object.keys(seen).length >= 3` — stage 2's
    predicate, verbatim (page line 648). MRB-208 ruled the rail carries only
    sections that require the student to do something, and this section emits
    no control, no commit and no field: it is an eyebrow, a heading, a lede, a
    table and a footnote. The nearest thing to a demand of its own is the
    highlight, and that is worked from the BENCH's toggles in the bench's
    section — so a predicate over it would reproduce the same defect one
    control-group to the left. `ks3_parity.check_rail_reachable` names this
    exact case in its own docstring; it passes here because the stop is gone,
    not because a borrowed predicate was left in place.

    ⚑ Three of the six rows — `shape`, `volume`, `pour` — can be reached by no
    bench setting whatever, because the highlight answers squash / paths /
    neither and those three rows answer none of them. All six are authored
    anyway: the table is the lesson's reference and the three unreachable rows
    are three of the six answers a student needs. Reported rather than fixed
    with a control Design did not draw (map §2.5.2).
    """
    rows = a.get("rows") or []
    cols = a.get("columns") or []
    if not rows:
        raise ValueError("state-matrix %r declares no rows[]." % act_id)
    if len(cols) < 2:
        raise ValueError(
            "state-matrix %r declares %d column(s); it needs the property "
            "column and one per state." % (act_id, len(cols)))
    # The three state cells are keyed by name rather than by position, because
    # they are authored against a header the author can also see; this asserts
    # the two agree.
    cells = ("solid", "liquid", "gas")
    for r in rows:
        missing = [k for k in ("key", "label") + cells if not r.get(k)]
        if missing:
            raise ValueError(
                "state-matrix %r row %r is missing %s."
                % (act_id, r.get("key") or r.get("label"), ", ".join(missing)))
    if len(cols) != len(cells) + 1:
        raise ValueError(
            "state-matrix %r has %d columns and %d state cells per row; the "
            "header and the body have to describe the same table."
            % (act_id, len(cols), len(cells)))

    by_key = {r["key"]: r for r in rows}
    hl = a.get("highlight") or {}
    for cond in ("squash", "trails", "rest"):
        if hl.get(cond) not in by_key:
            raise ValueError(
                "state-matrix %r highlight[%r] names row %r, which is not one "
                "of %s. A renamed row must be a build error and never a table "
                "that quietly stops lighting."
                % (act_id, cond, hl.get(cond), ", ".join(sorted(by_key))))
    if not a.get("highlight_from"):
        raise ValueError(
            "state-matrix %r authors no `highlight_from`. The lit row is read "
            "off another block's published state and the matrix has to be told "
            "which section to read." % act_id)

    # The RESTING lit row is emitted lit, at build time, by the same rule the
    # runtime uses — squash first, then paths, then neither, and at rest it is
    # neither. Without this the table renders unlit for the instant before
    # `wireStateMatrix` corrects it, which is a wrong picture on screen and a
    # wrong picture in the HTML a search engine reads.
    lit_at_rest = hl["rest"]

    head = "".join('<th scope="col">%s</th>' % t(c) for c in cols)
    body = []
    for r in rows:
        on = r["key"] == lit_at_rest
        body.append(
            '<tr class="ks3-smatrix-row" data-row="%s" data-lit="%s">'
            # ⊕ `aria-current` is an ADDITION inside a component Design drew.
            # Design signals the lit row with `--ks3-accent-tint` and nothing
            # else, so a student who cannot separate the tint from the card is
            # told nothing at all — and the footnote under the table promises
            # them a highlight. R2 says colour is never the only signal on a
            # state. It costs no pixels and changes nothing Design drew.
            '<th scope="row"%s>%s</th>%s</tr>'
            % (e(r["key"]), "1" if on else "0",
               ' aria-current="true"' if on else "",
               t(r["label"]),
               "".join("<td>%s</td>" % t(r[k]) for k in cells)))

    foot = ('<p class="ks3-smatrix-foot">%s</p>' % t(a["footnote"])
            if a.get("footnote") else "")

    return ('<div class="ks3-smatrix" data-smatrix data-from="%s" '
            'data-lit-squash="%s" data-lit-trails="%s" data-lit-rest="%s">'
            '<div class="ks3-smatrix-scroll">'
            '<table class="ks3-smatrix-table">'
            '<thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>%s</div>'
            % (e(a["highlight_from"]), e(hl["squash"]), e(hl["trails"]),
               e(hl["rest"]), head, "".join(body), foot))
# renderers: ═══ END C1 ═══





# renderers: ═══ BEGIN B2 ═══
# DISPATCH: "arm-lever": ("ks3-lever-block", ' data-instrument data-leverblock data-stage-done="0"'),
#
# and in ACTIVITY_KIND_FN, beside the other B2 rows:
#     "arm-lever":              r_arm_lever,
#
# Place `r_arm_lever` and the two helpers below beside `r_muscle_pair` in the
# B2 group (build_ks3.py ~3079). Needs `e`, `t`, `r_bench_gate`. No new
# imports: the only arithmetic here is a divide and a round, and
# `int(v + 0.5)` is `math.floor` for a positive v, which every value on this
# rig is (the sliders' floors are 0.5 kg and 3 cm).
#
# ⚠️ `_lever_num` and `_lever_alt` are MODULE-LEVEL, not nested, because the
# RESTING render needs the same formatter and the same composition the runtime
# uses. Two copies of "how is this number written" is two answers to it, and
# the number is on screen before any JS runs.


# Values the rig COMPUTES rather than reads off a control. Both are Design's
# `.toFixed(0)` — a weight and a force are whole newtons on this page.
_LEVER_COMPUTED = {"weight": 0, "force": 0}


def _lever_decimals(step):
    """How many decimal places a control's own step needs.

    DERIVED, never authored. A step of 0.5 needs one place and an integer set
    needs none; a `decimals` key would be a second statement of the same fact
    and a second place for it to disagree with the slider.
    """
    if step is None:
        return 0
    return 0 if float(step) == int(float(step)) else 1


def _lever_num(value, decimals, fmt):
    """One readout, formatted. `fmt` is an authored "{n} kg"-shaped string."""
    return (fmt or "{n}").replace("{n}", "%.*f" % (decimals, float(value)))


def _lever_alt(alt, load, ins, hand, force=None):
    """The canvas's aria-label, composed the same way in Python and in JS.

    ⚖️ THE LABEL IS THE WHOLE DRAWING for a screen-reader user: the two
    dimension lines, the load's weight arrow and the joint are painted inside
    the canvas and exist nowhere in the DOM. So every number a sighted student
    can see on the drawing has to be in here.

    ⚠️ AND NOT ONE MORE THAN THAT. `force` is appended only once the meter has
    been fitted — the same gate the muscle tile takes, reached by the other
    route. Handing the answer to a screen-reader user before they have worked
    it out is not an accommodation, it is a different lesson.

    ⚠️ SINGULAR/PLURAL. C1 shipped "after 1 halvings" and it had to be fixed,
    so the guard is here from the start rather than after somebody reads it
    aloud. No control on this rig can currently reach a bare 1 — `load` and
    `ins` render to one decimal ("1.0 kilograms" is correct English) and
    `hand` offers 32 and 16 — but a future payload with `step: 1` on the load
    would, and a plural that only breaks for one authored value is exactly the
    kind of defect that ships.
    """
    out = (alt.get("template", "")
           .replace("{load}", load).replace("{ins}", ins)
           .replace("{hand}", hand))
    if force is not None and alt.get("measured"):
        out += alt["measured"].replace("{force}", force)
    for word in ("kilogram", "centimetre", "newton"):
        out = out.replace(" 1 %ss" % word, " 1 %s" % word)
    return out


def r_arm_lever(a, act_id):
    """⊕ b2-04 `#s-bench` — the forearm rig, and the number it will not give you.

    ⚖️ THE MISSING FOURTH NUMBER IS THE WHOLE INSTRUMENT. The rig hands over
    the load and both distances and refuses the muscle force: the tile reads
    the authored `unmeasured` sentence, and the muscle arrow on the canvas
    carries the bare word "muscle" and deliberately no magnitude. A student
    who could read the force off the rig would never divide anything, and the
    meter exists so they can CHECK their arithmetic rather than skip it.
    That gate is why the meter button is one-way and why fitting it is half
    the rail stop.

    ⚠️ NOT `sim`, and not `joint-bench`. Three measured differences, any one
    of which is fatal:

      * `sim`'s controls are a CLOSED ENUM validated against `SIM_CONTROLS`;
        this rig's three are a mass, an attachment distance and a two-tab
        distance, and none of them is in that list. Adding them would give
        every KS3 sim a "muscle attached at" slider.
      * `joint-bench` reads a per-joint record and paints a linkage; every
        readout it has is a lookup. Every readout here is ARITHMETIC on the
        three live values, and the one that matters is withheld.
      * a mixed control topology — two sliders and an exclusive two-tab set —
        whose product decides four readouts, a canvas and a rail predicate.

    ⚠️ INK-DARK, so every text rule in the stylesheet is scoped `.ks3-dark …`.
    `.ks3-dark p` is (0,1,1) and a bare instrument class is (0,1,0): unscoped,
    the tile labels and the meter note lose and render in on-dark body copy
    against a panel that is not the ground they were coloured for. That is the
    defect B1 shipped with the zoom instrument and B2 was bitten by again.

    ⊕ ADDITIONS inside the drawn component, both stated in the report:
      * `alt.measured` — Design's `benchAlt` never mentions the muscle force,
        so once the meter is fitted a screen-reader user is the only person on
        the page who cannot read it. Appended, and only then.
      * `done_at` — Design hard-codes `>= 2` inside its own rail predicate.
        Authored once here and read by the wiring, so the rail's demand is
        data rather than a number nobody can find.
    """
    controls = a.get("controls") or []
    if not controls:
        raise ValueError("arm-lever %r declares no controls[]." % act_id)

    by_key, decimals = {}, {}
    for c in controls:
        key = c.get("key")
        if not key:
            raise ValueError(
                "arm-lever %r has a control with no `key`; the key is what the "
                "tiles, the canvas and the steps block all name it by."
                % act_id)
        if c.get("options"):
            if c.get("start") not in c["options"]:
                raise ValueError(
                    "arm-lever %r control %r starts at %r, which is not one of "
                    "the tabs it offers (%s)."
                    % (act_id, key, c.get("start"),
                       ", ".join(str(o) for o in c["options"])))
            decimals[key] = 0
        else:
            for bound in ("min", "max", "step"):
                if c.get(bound) is None:
                    raise ValueError(
                        "arm-lever %r control %r is a slider and declares no "
                        "`%s`; a range with an open end renders as a browser "
                        "default and reads any value at all."
                        % (act_id, key, bound))
            if not float(c["min"]) <= float(c["start"]) <= float(c["max"]):
                raise ValueError(
                    "arm-lever %r control %r starts at %r, outside its own "
                    "%r–%r range." % (act_id, key, c.get("start"),
                                      c.get("min"), c.get("max")))
            decimals[key] = _lever_decimals(c.get("step"))
        by_key[key] = c

    tiles = a.get("tiles") or []
    if not tiles:
        raise ValueError("arm-lever %r declares no tiles[]." % act_id)
    for tl in tiles:
        if tl.get("key") not in by_key and tl.get("key") not in _LEVER_COMPUTED:
            raise ValueError(
                "arm-lever %r tile %r reads %r, which is neither a control nor "
                "a computed value (%s). A tile with no source is a box that "
                "never fills." % (act_id, tl.get("label"), tl.get("key"),
                                  ", ".join(sorted(_LEVER_COMPUTED))))

    meter = a.get("meter") or {}
    for key in ("label", "label_done", "note", "note_done"):
        if not meter.get(key):
            raise ValueError(
                "arm-lever %r meter is missing %r. All four are drawn: the "
                "button says two things and the line beside it says two more, "
                "and a missing one leaves the previous state's sentence on "
                "screen after the meter is fitted." % (act_id, key))
    if not a.get("unmeasured"):
        raise ValueError(
            "arm-lever %r declares no `unmeasured` sentence. That string IS "
            "the gate — without it the force tile would open empty and the "
            "block would look broken rather than withholding." % act_id)

    canvas = a.get("canvas") or {}
    for key in ("title", "joint", "muscle", "load"):
        if not canvas.get(key):
            raise ValueError(
                "arm-lever %r canvas is missing %r." % (act_id, key))
    alt = a.get("alt") or {}
    if not alt.get("template"):
        raise ValueError(
            "arm-lever %r has no alt template; the dimension lines, the weight "
            "arrow and the joint are painted on the canvas and reach a screen "
            "reader through nothing else." % act_id)

    done_at = int(a.get("done_at") or 0)
    if not 1 <= done_at <= len(controls):
        raise ValueError(
            "arm-lever %r ticks its rail stop at %r control(s) moved; it "
            "offers %d. A stop that cannot be reached is worse than none."
            % (act_id, a.get("done_at"), len(controls)))

    g = float(a.get("g") or 0)
    if g <= 0:
        raise ValueError(
            "arm-lever %r declares g = %r N/kg. The whole page's arithmetic "
            "runs through it." % (act_id, a.get("g")))

    # ── the resting state, computed here so the page is never a set of empty
    # boxes for the instant before the wiring runs ──
    start = {k: float(c["start"]) for k, c in by_key.items()}
    weight = start["load"] * g
    values = {"weight": weight, "force": weight * start["hand"] / start["ins"]}

    def readout(key, fmt):
        if key in _LEVER_COMPUTED:
            return _lever_num(values[key], _LEVER_COMPUTED[key], fmt)
        return _lever_num(start[key], decimals[key], fmt)

    rows = []
    for c in controls:
        key = c["key"]
        cid = "%s-%s" % (act_id, key)
        if c.get("options"):
            tabs = "".join(
                '<button type="button" class="ks3-sim-seg-btn ks3-lever-tab" '
                'data-lever-tab="%s" data-value="%s" aria-pressed="%s">%s'
                '</button>'
                % (e(key), e(o), "true" if float(o) == start[key] else "false",
                   t(_lever_num(o, decimals[key], c.get("format"))))
                for o in c["options"])
            rows.append('<div class="ks3-lever-control">'
                        '<p class="ks3-lever-label">%s</p>'
                        '<div class="ks3-lever-tabs">%s</div></div>'
                        % (t(c.get("label", "")), tabs))
            continue
        # ⚠️ The <label> is real and its `for` reaches a real id. A slider
        # whose only name is the paragraph above it is unnamed to a screen
        # reader, and this one is the difference between two distances.
        rows.append(
            '<div class="ks3-lever-control">'
            '<div class="ks3-lever-row">'
            '<label class="ks3-lever-label" for="%s">%s</label>'
            '<p class="ks3-lever-value" data-lever-value="%s" '
            'data-format="%s">%s</p></div>'
            '<input class="ks3-slider ks3-lever-slider" type="range" id="%s" '
            'min="%s" max="%s" step="%s" value="%s" data-lever-input="%s">'
            '</div>'
            % (e(cid), t(c.get("label", "")), e(key),
               e(c.get("format") or "{n}"),
               t(readout(key, c.get("format"))), e(cid),
               e(c["min"]), e(c["max"]), e(c["step"]), e(c["start"]), e(key)))

    cells = []
    for tl in tiles:
        key = tl["key"]
        # The force tile opens on the withheld sentence, not on a number.
        value = (a["unmeasured"] if key == "force"
                 else readout(key, tl.get("format")))
        cells.append('<div class="ks3-lever-tile">'
                     '<p class="ks3-lever-tile-label">%s</p>'
                     '<p class="ks3-lever-tile-value%s" data-lever-out="%s" '
                     'data-format="%s">%s</p></div>'
                     % (t(tl.get("label", "")),
                        " ks3-lever-tile-mono" if tl.get("mono") else "",
                        e(key), e(tl.get("format") or "{n}"), t(value)))

    gate_html, hide = r_bench_gate(a.get("gate"))

    return (gate_html
            + '<div class="ks3-lever" data-lever%s data-rig="%s" data-g="%s" '
              'data-done-at="%d" data-load="%s" data-ins="%s" data-hand="%s" '
              'data-dp-load="%d" data-dp-ins="%d" data-dp-hand="%d" '
              'data-unmeasured="%s" data-alt="%s" data-alt-measured="%s" '
              'data-canvas-title="%s" data-canvas-joint="%s" '
              'data-canvas-muscle="%s" data-canvas-load="%s" '
              'data-meter-label="%s" data-meter-done="%s" '
              'data-meter-note="%s" data-meter-note-done="%s">'
              '<div class="ks3-lever-controls">%s</div>'
              '<div class="ks3-lever-stage">'
              '<canvas class="ks3-lever-canvas" width="1800" height="700" '
              'role="img" aria-label="%s" data-lever-canvas></canvas></div>'
              '<div class="ks3-lever-tiles">%s</div>'
              '<div class="ks3-lever-foot">'
              '<button type="button" class="ks3-sim-seg-btn ks3-lever-meter" '
              'data-lever-meter>%s</button>'
              '<p class="ks3-lever-note" data-lever-note role="status">%s</p>'
              '</div></div>'
            % (hide, e(act_id), e(a["g"]), done_at,
               e(start["load"]), e(start["ins"]), e(start["hand"]),
               decimals["load"], decimals["ins"], decimals["hand"],
               e(a["unmeasured"]), e(alt.get("template", "")),
               e(alt.get("measured", "")),
               e(canvas["title"]), e(canvas["joint"]), e(canvas["muscle"]),
               e(canvas["load"]),
               e(meter["label"]), e(meter["label_done"]),
               e(meter["note"]), e(meter["note_done"]),
               "".join(rows),
               e(_lever_alt(alt,
                            _lever_num(start["load"], decimals["load"], "{n}"),
                            _lever_num(start["ins"], decimals["ins"], "{n}"),
                            _lever_num(start["hand"], decimals["hand"], "{n}"))),
               "".join(cells),
               t(meter["label"]), t(meter["note"])))


# ⚠️ NO DISPATCH ROW — DO NOT ADD ONE, AND DO NOT WRITE THE WORD ABOVE IN
# THE SPLICE MARKER'S OWN SHAPE.
#
# `cover-triangle` is NOT an activity kind and must not become one: it is a
# `formula` BLOCK sub-key, exactly as its bar variant is. There is no
# ACTIVITY_KIND_RENDERERS entry, no ACTIVITY_KIND_FN entry and no
# `data-stage-done` — the block is read, not done, and MRB-208 keeps it off
# the rail.
#
# (This header used to open `# DISPATCH: none. …`. The splice tool matched the
# marker, took the prose after it as a table row and emitted
# `none. \`cover-triangle\` is NOT an activity kind and must not become,` into
# ACTIVITY_KIND_RENDERERS, which is a SyntaxError in build_ks3.py. A marker
# that means "no row" has to not be the marker.)
#
# ── HOW THIS SPLICES, and why it is a widening rather than a fork ─────────
#
# `cover-triangle` already ships in TWO forms and this fragment touches only
# one of them:
#
#   BAR variant      `r_cover_bar(cov)`, reached from `r_formula` via
#                    `block["cover"]` with `shape: "bar"`. c2-06's part–whole
#                    model. **NOT TOUCHED BY THIS FRAGMENT AT ALL** — no line
#                    of `r_cover_bar`, `.ks3-bar-*` or `wireCoverBar` changes,
#                    which is why c2-06 is byte-identical by construction
#                    rather than by inspection.
#   TRIANGLE variant `r_formula_triangle(tri)`, reached from `r_formula` via
#                    `block["triangle"]`. b1-02's magnification triangle ships
#                    it today. THIS is what widens.
#
# ⊕ THE SPLICE IS SELF-APPLYING. Both functions below go in verbatim and
# nothing else in `build_ks3.py` needs touching: `r_formula` is unchanged,
# `_triangle_geometry()` is unchanged, `TRI_W/TRI_H/TRI_PAD/TRI_DIV_Y` are
# unchanged, and the old `r_formula_triangle` at ~1562 can stay exactly where
# it is. The delegate at the foot of this file REBINDS that name, and because
# this fragment lands after it in the module, the later binding is the one
# `r_formula` resolves at call time. The superseded body is then dead code and
# should be deleted in a follow-up tidy — but the splice is correct with it
# still there, which is the property worth having.
#
# ⚠️ b1-02 MUST COME OUT BYTE-IDENTICAL, and the four new keys are what makes
# that true: `result`, `order`, `covered` and a dict-shaped `close` are all
# OPT-IN. b1-02 authors none of them, so every widened branch below collapses
# to the empty string and the emitted markup is the same characters in the same
# order. The evidence is a diff of the built page across the splice, and it is
# in the report.
#
# Place `r_cover_triangle` where `r_formula_triangle` is now (build_ks3.py
# ~1562), immediately after `_triangle_geometry()`. Needs `e`, `t`, `rich`,
# `hashlib` — all already in scope.

_TRI_CELLS = ("top", "left", "right")


def r_cover_triangle(tri, act_id=None):
    """MRB-204 step 2 — the formula drawn as a triangle, in KS3 tokens.

    ⚖️ A TRIANGLE IS THE PRODUCT'S FIGURE. `T = F × d` is a product, so it
    takes this; conservation of mass is a sum and takes the bar. Drawing a sum
    as a triangle — or a product as a beam — teaches a false relationship in
    order to make one rule fit two shapes.

    ⚠️ CORRECTED, AND THE CORRECTION IS INHERITED, NOT NEW. Design's three
    cover boxes overhang the sloping sides (the b1-02 `total` box by about 35
    units at its top edge). It is not a slip and it is not nudgeable: a
    rectangle inside a triangle always overhangs unless it is sized at its own
    narrowest edge, and a box that narrow cannot hold the word it exists to
    hide. The covers are therefore sized to their labels and CLIPPED to the
    triangle path. Both the boxes and the clip are derived from the frame;
    nothing is authored per lesson.

    ── ⊕ WIDENED FOR b2-04, four opt-in keys ────────────────────────────

    `result`   per cell. Design's b2-04 side panel says the ARRANGEMENT in
               display type ("F = T ÷ d") and then says WHY in a sentence.
               b1-02 has only the sentence. Folding the two into one note
               loses the line a student actually reads off the page, and
               emitting the arrangement into the sentence would put maths
               inside prose.
    `order`    the button order. Design's b2-04 is F, T, d — the unknown this
               lesson always solves for comes first — against the
               top/left/right default b1-02 ships.
    `covered`  the cell covered on load, and it is more than a default: a
               triangle that declares one becomes a RADIO. b1-02's toggle
               un-covers on a second press, which is right for a triangle
               being explored and wrong for one whose whole demand is "cover
               the one you want" — an uncovered triangle asks nothing. Both
               interactions are drawn, so both are kept, and the payload is
               what decides which. Emitted as `data-cover-mode="radio"`;
               `wireTriangle` reads it and b1-02, which emits no attribute,
               keeps the toggle.
    `close`    a STRING stays one closing paragraph, exactly as today. A DICT
               takes Design's three trailing blocks — a prose rule, a mono
               unit legend, and the balanced condition in display type. The
               condition is not a fourth arrangement of T, F and d; it is the
               statement that makes every question on the page solvable, and
               that is why Design sets it apart in display type.

    A triangle that authors any `result` also takes Design's TWO-COLUMN row
    (`data-tri-layout="row"`): the figure on the left, the buttons and the
    reading on the right. b1-02's stacked, centred column is untouched — it
    has no side panel to put beside anything.

    ⚠️ EMIT-BOTH-SHOW-ONE for both the notes and the results. Every cell's
    sentence and every cell's arrangement is in the document, hidden, and the
    wiring swaps which pair is shown. Nothing science-bearing is rebuilt in JS,
    so `÷`, `×` and the em dashes survive — which the bar variant's
    `textContent` route cannot promise.
    """
    cells = {k: (tri.get(k) or {}) for k in _TRI_CELLS}
    missing = [k for k in _TRI_CELLS if not cells[k].get("label")]
    if missing:
        raise ValueError(
            "cover-triangle %s has no label on cell(s) %s. All three corners "
            "are drawn and an unlabelled one is a blank corner of a figure."
            % (act_id or tri.get("heading") or "?", ", ".join(missing)))

    # ⊕ WIDENED. All three or none: a side panel that goes blank on one of the
    # three covers is worse than one that never had a result line, and it
    # would only be found by pressing the third button.
    with_result = [k for k in _TRI_CELLS if cells[k].get("result")]
    if with_result and len(with_result) != len(_TRI_CELLS):
        raise ValueError(
            "cover-triangle %s gives a `result` to %s and not to the others. "
            "The result line is a slot in the side panel: covering a cell "
            "that has none would empty it."
            % (act_id or "?", ", ".join(with_result)))
    wide = bool(with_result)

    order = tuple(tri.get("order") or _TRI_CELLS)
    if sorted(order) != sorted(_TRI_CELLS):
        raise ValueError(
            "cover-triangle %s orders its buttons %r; the three cells are %s "
            "and the order names each exactly once."
            % (act_id or "?", list(order), ", ".join(_TRI_CELLS)))

    covered = tri.get("covered")
    if covered is not None and covered not in _TRI_CELLS:
        raise ValueError(
            "cover-triangle %s opens with %r covered; the three cells are %s."
            % (act_id or "?", covered, ", ".join(_TRI_CELLS)))

    g = _triangle_geometry()
    # One triangle per page today; the id is derived from the aria-label so two
    # on one page would still not collide.
    clip_id = "ks3-tri-clip-%s" % hashlib.md5(
        (tri.get("aria_label", "") or "t").encode("utf-8")).hexdigest()[:8]
    ax, ay = g["apex"]
    x1, y1, x2, y2 = g["base"]
    dh = g["div_half"]

    def cover(key):
        x, y, w, h = g[key]
        return ('<rect class="ks3-tri-cover" data-cover="%s" x="%.2f" y="%.2f" '
                'width="%.2f" height="%.2f" rx="8"></rect>'
                % (e(key), x, y, w, h))

    labels = ""
    for key, (lx, ly) in (("top", (ax, TRI_DIV_Y - 42)),
                          ("left", (ax - 44, TRI_DIV_Y + 46)),
                          ("right", (ax + 44, TRI_DIV_Y + 46))):
        labels += ('<text class="ks3-tri-label" x="%.2f" y="%.2f" '
                   'text-anchor="middle">%s</text>'
                   % (lx, ly, t(cells[key].get("label", ""))))

    # ⊕ WIDENED. The pressed state opens on the covered cell rather than on
    # nothing, so the control and the figure agree before a student touches
    # either. With no `covered` every button is `false`, exactly as today.
    btns = "".join(
        '<button type="button" class="ks3-seg-btn ks3-tri-btn" '
        'data-cover="%s" aria-pressed="%s">%s</button>'
        % (e(k), "true" if k == covered else "false",
           t(cells[k].get("button", "")))
        for k in order)

    # ⊕ WIDENED. `hidden` unless this cell is the one covered on load. With no
    # `covered` all three stay hidden, which is today's output.
    notes = "".join(
        '<p class="ks3-tri-note" data-note="%s"%s>%s</p>'
        % (e(k), "" if k == covered else " hidden",
           rich(cells[k].get("text", "")))
        for k in _TRI_CELLS)

    results = "".join(
        '<p class="ks3-tri-result" data-result="%s"%s>%s</p>'
        % (e(k), "" if k == covered else " hidden", t(cells[k]["result"]))
        for k in _TRI_CELLS) if wide else ""

    # ⊕ WIDENED. A string is one paragraph and is what b1-02 authors; a dict is
    # Design's b2-04 stack of three.
    raw_close = tri.get("close")
    if isinstance(raw_close, dict):
        close = ""
        if raw_close.get("rule"):
            close += '<p class="ks3-tri-close">%s</p>' % rich(raw_close["rule"])
        if raw_close.get("units"):
            # `<br>`-joined rather than a list, because it is a legend of three
            # one-line glosses and a bulleted `<ul>` would read as three
            # instructions.
            close += ('<p class="ks3-tri-units">%s</p>'
                      % "<br>".join(t(u) for u in raw_close["units"]))
        if raw_close.get("condition"):
            close += ('<p class="ks3-tri-condition">%s</p>'
                      % t(raw_close["condition"]))
    else:
        close = ('<p class="ks3-tri-close">%s</p>' % rich(raw_close)
                 if raw_close else "")

    root_attrs = ""
    if covered is not None:
        root_attrs += ' data-covered="%s" data-cover-mode="radio"' % e(covered)
    if wide:
        root_attrs += ' data-tri-layout="row"'

    svg = ('<svg class="ks3-tri-svg" viewBox="0 0 %d %d" role="img" '
           'aria-label="%s">'
           '<defs><clipPath id="%s">'
           '<path d="M %.2f %.2f L %.2f %.2f L %.2f %.2f Z"/></clipPath></defs>'
           '<path class="ks3-tri-path" d="M %.2f %.2f L %.2f %.2f L %.2f %.2f Z"/>'
           '<line class="ks3-tri-div" x1="%.2f" y1="%d" x2="%.2f" y2="%d"/>'
           '<line class="ks3-tri-div" x1="%.2f" y1="%d" x2="%.2f" y2="%.2f"/>'
           '%s%s%s</svg>'
           % (TRI_W, TRI_H, e(tri.get("aria_label", "")),
              clip_id, ax, ay, x2, y2, x1, y1,
              ax, ay, x2, y2, x1, y1,
              ax - dh, TRI_DIV_Y, ax + dh, TRI_DIV_Y,
              ax, TRI_DIV_Y, ax, y2,
              labels,
              '<g clip-path="url(#%s)">%s</g>'
              % (clip_id, cover("top") + cover("left") + cover("right")), ""))

    head = ('<p class="ks3-eyebrow">%s</p><p class="ks3-tri-heading">%s</p>'
            % (t(tri.get("eyebrow", "")), t(tri.get("heading", ""))))
    controls = '<div class="ks3-tri-btns">%s</div>' % btns

    if not wide:
        # ⚠️ TODAY'S OUTPUT, CHARACTER FOR CHARACTER. Do not "tidy" this branch
        # into the row one — b1-02 is live and this is the whole byte-identity
        # claim.
        return ('<div class="ks3-triangle" data-triangle%s>%s%s%s%s%s</div>'
                % (root_attrs, head, svg, controls, notes, close))

    return ('<div class="ks3-triangle" data-triangle%s>%s'
            '<div class="ks3-tri-row">%s'
            '<div class="ks3-tri-side">%s%s%s%s</div></div></div>'
            % (root_attrs, head, svg, controls, results, notes, close))


def r_formula_triangle(tri):
    """⊖ SUPERSEDED NAME, kept so nothing above has to change.

    `r_formula` reaches the triangle through this name and b1-02 has shipped
    against it since MRB-204 landed. Rebinding it here rather than renaming
    the call site means the widening is one appended block and zero edits to
    working code — and b1-02 goes through the identical path it always did,
    because `r_cover_triangle` with none of the four opt-in keys emits the
    same characters in the same order.

    The original definition further up the module is now dead and should be
    deleted in a follow-up tidy. It is left in place deliberately for this
    splice: a delete is a change to working code and this pass is meant not
    to be one.
    """
    return r_cover_triangle(tri)


# DISPATCH: "lever-steps": ("ks3-lstep-block", ' data-instrument data-lstepblock data-stage-done="0"'),
#
# and in ACTIVITY_KIND_FN, beside the other B2 rows:
#     "lever-steps":            r_lever_steps,
#
# ╔═══════════════════════════════════════════════════════════════════════╗
# ║  TWO HAND EDITS, AND THIS FRAGMENT IS WRONG WITHOUT BOTH.             ║
# ║  Neither is derivable from the file, so neither can be spliced        ║
# ║  mechanically. `arm-lever`, `meter-compare` and `cover-triangle`      ║
# ║  need none — this is the only one.                                    ║
# ╚═══════════════════════════════════════════════════════════════════════╝
#
# ── EDIT 1 · this kind takes the LESSON — and needs NO edit ─────────────
#
# ⊕ Superseded 16 Aug 2026 (MRB-228). This used to say "add it to
# `_KIND_FN_TAKES_LESSON` beside the three already there", and that set no
# longer exists: `_kinds_taking_lesson()` reads the signature, so a renderer
# whose first parameter is named `lesson` is handed the lesson.
#
# The instruction was written because leaving it out made the build die with a
# TypeError naming the kind — loud, immediate, not a silent wrong render. It
# did exactly that when `lever-steps` first spliced in. Loud is not the same as
# unnecessary: name the parameter `lesson` and there is nothing to remember.
#
# It has to take the lesson because the block's whole argument is that it is
# the SAME problem as the rig upstairs: it reads that instrument's own control
# defaults out of `lesson["activities"]` to render its resting state, and
# refuses to build if the rig it names is missing. A copy of "2 kg at 32 cm,
# muscle at 4 cm" here would go stale the first time anyone moved a slider in
# the payload, and nothing would say so.
#
# ── EDIT 2 · the block heading ships its braces without this ────────────
#
# Design draws this block's <h2> as the LIVE rig line — *"Your rig: 2.0 kg at
# 32 cm, muscle at 4.0 cm."* — and the shell emits the <h2> before any
# instrument renderer runs, so `r_lever_steps` cannot reach it. Add these two
# lines to `r_activity`, anywhere after `kind` is computed (~line 6372) and
# before the `if a.get("heading") and not hc:` branch (~line 6440):
#
#     # ⊕ b2-04 #s-build — this block's heading quotes the rig the student
#     # left set, so it is filled from that instrument before the shell
#     # emits the <h2>. `wireLeverSteps` repaints the same element.
#     if kind == "lever-steps":
#         a = dict(a, heading=_lever_steps_heading(lesson, a))
#
# WITHOUT IT the page ships `<h2>Your rig: {load} kg at {hand} cm, muscle at
# {ins} cm.</h2>` — which the wiring then overwrites, so it is invisible in a
# browser and permanent in the HTML a crawler reads and in every no-JS view.
#
# Filling it at BUILD TIME as well as at runtime is the whole point.
# `dict(a, …)` rather than `a["heading"] = …` so the lesson record is never
# mutated: `r_activity` runs once per page, but the record is shared with
# every gate that reads it afterwards.
#
# Place `r_lever_steps` and its two helpers beside `r_fifa_pick`
# (build_ks3.py ~3888), which is the component it is closest to. Needs `e`,
# `t`, `rich`, and `_lever_num` / `_lever_decimals` from the `arm-lever`
# fragment — splice that one first.


def _lever_steps_rig(lesson, a, act_id):
    """The `arm-lever` this block mirrors, and the substitutions it implies.

    Returns `(subs, fill)`. Separated from the renderer because the block's
    own <h2> is emitted by the shell and has to be filled from the same three
    values through the same formatter — two copies of "how many decimal
    places does 0.04 get" is two answers to it.
    """
    rig_id = a.get("rig")
    rig = next((x for x in (lesson.get("activities") or [])
                if x.get("id") == rig_id), None)
    if rig is None:
        raise ValueError(
            "lever-steps %r reads rig %r and the lesson declares no activity "
            "with that id. The block's whole claim is that it is the same "
            "problem as the bench upstairs." % (act_id, rig_id))
    if rig.get("kind") != "arm-lever":
        raise ValueError(
            "lever-steps %r names rig %r, which is a %r. Only `arm-lever` "
            "carries the load, the two distances and g that every template "
            "here interpolates." % (act_id, rig_id, rig.get("kind")))

    controls = {c["key"]: c for c in (rig.get("controls") or [])}
    missing = [k for k in ("load", "ins", "hand") if k not in controls]
    if missing:
        raise ValueError(
            "lever-steps %r reads rig %r, which has no %s control. Every "
            "template in this block interpolates all three."
            % (act_id, rig_id, ", ".join(missing)))
    dp = {k: (0 if controls[k].get("options")
              else _lever_decimals(controls[k].get("step")))
          for k in ("load", "ins", "hand")}
    start = {k: float(controls[k]["start"]) for k in ("load", "ins", "hand")}
    g = float(rig.get("g") or 0)

    W = start["load"] * g
    dM, dL = start["ins"] / 100.0, start["hand"] / 100.0
    # ⚠️ Two decimal places on the distances and on the turning effect, and
    # NONE on the weight or the force. That is Design's own arithmetic and it
    # is not tidiness: `0.04` and `0.32` are the metre conversions a student
    # writes down, and `6.40` is what `20 × 0.32` gives on a calculator. A
    # weight and a force are whole newtons on this page.
    subs = {
        "{load}": _lever_num(start["load"], dp["load"], "{n}"),
        "{ins}": _lever_num(start["ins"], dp["ins"], "{n}"),
        "{hand}": _lever_num(start["hand"], dp["hand"], "{n}"),
        "{W}": "%.0f" % W,
        "{dM}": "%.2f" % dM,
        "{dL}": "%.2f" % dL,
        "{TE}": "%.2f" % (W * dL),
        "{F}": "%.0f" % (W * dL / dM),
        "{ratio}": "%.1f" % (start["hand"] / start["ins"]),
    }

    def fill(s):
        out = s or ""
        for k, v in subs.items():
            out = out.replace(k, v)
        return out

    return subs, fill


def _lever_steps_heading(lesson, a):
    """The block's <h2>, filled from the rig. Spliced into `r_activity`."""
    _, fill = _lever_steps_rig(lesson, a, a.get("id"))
    return fill(a.get("heading", ""))


def r_lever_steps(lesson, a, act_id):
    """⊕ b2-04 `#s-build` — MRB-204 step 4, on the student's OWN rig.

    ⚖️ NOT `fifa-pick`, and the difference is arithmetic rather than taste.
    c2-06's block has the same furniture — two pick ladders, a number field, a
    unit select, a locked open button and a four-step ink reveal — and every
    string in it is STATIC. Here, five of the eight authored strings are
    templates over three live values: the heading quotes the rig, the second
    ladder's three options are this student's own numbers arranged three ways,
    all four reveal steps carry them, and the closing line holds the student's
    typed answer against the force their own rig implies. `r_fifa_pick` emits
    finished text and `wirePick` never recomputes anything, so pointing this
    payload at it would print `F × {dM} = {W} × {dL}` into a button.

    ⚖️ AND THE GENERATION IS THE PEDAGOGY, not a convenience. Authoring the
    insert options would pin the rig at 2 kg and 32 cm and make every other
    setting of the sliders unanswerable — the block would quietly stop being
    about the student's own arm the moment they touched a control, which is
    the one thing the whole page asked them to do.

    ⚠️ NOT `fifa-construct` either: four free-text inputs and a tick list
    against two multiple-choice ladders and a number, and that renderer
    asserts `len(fields) == len(model) == len(success)` — three commitments
    against four model lines and no criteria would raise, and rightly.

    ── ⊕ CORRECTION: THE RAIL STOP DEMANDS SOMETHING ────────────────────

    Design ticks `#s-build` on `buildOpen` alone — on the student pressing
    "Show the four steps". A student who scrolls here and presses the button
    has committed to nothing and the rail says the stage is done. MRB-208 has
    a rail stop requiring the student to DO something, so the stop now ticks
    on the three commitments the block itself asks for: the formula picked,
    the insertion picked, and a non-empty answer WITH a unit.

    That is strictly earlier than the button, which needs the same three, so
    nothing a student can do gets harder — the stop simply stops being
    reachable by pressing one thing. It is also why the reveal is not the
    signal: opening an answer is the reward for committing, not the commitment.

    ⚠️ THE UNIT IS ITS OWN COMMITMENT. "160" is not an answer to a question
    about force, and the placeholder `<option>` carries an EMPTY value so that
    a student who never chose one cannot satisfy the gate. Measured in a
    browser on c2-06, not read off the source.

    ⚠️ NO `value` ATTRIBUTE ON THE INPUT. An authored `value` is an attribute,
    the element reads it only as its default, and the first repaint wipes what
    the student typed. B1 fixed this once already; Design's page re-introduces
    it (`<input … value="{{ ansValue }}">`) and it is not reproduced.
    """
    subs, fill = _lever_steps_rig(lesson, a, act_id)

    picks = a.get("picks") or []
    if len(picks) != 2:
        raise ValueError(
            "lever-steps %r declares %d pick ladder(s); it takes two — the "
            "rule and the insertion." % (act_id, len(picks)))
    steps = a.get("steps") or []
    if not steps:
        raise ValueError("lever-steps %r reveals no steps[]." % act_id)
    field = a.get("field") or {}
    if not field.get("units"):
        raise ValueError(
            "lever-steps %r offers no units[]. The unit is a separate "
            "commitment: `160` is not an answer to a question about force."
            % act_id)

    panels = []
    for i, p in enumerate(picks):
        opts = "".join(
            '<button type="button" class="ks3-lstep-opt" data-group="%d" '
            'data-i="%d" data-template="%s" aria-pressed="false">%s</button>'
            # ⚠️ BOTH the filled text AND the template are emitted. The button
            # renders finished at build time and the wiring refills it from
            # the same template when the rig moves, so there is exactly one
            # authored string and no second copy in JS to drift from it.
            % (i, j, e(o), t(fill(o)))
            for j, o in enumerate(p.get("options") or []))
        panels.append(
            '<div class="ks3-lstep-panel">'
            '<p class="ks3-lstep-label">%s</p>'
            '<p class="ks3-lstep-q">%s</p>'
            '<div class="ks3-lstep-opts">%s</div></div>'
            % (t(p.get("label", "")), t(p.get("question", "")), opts))

    aid, uid = "%s-ans" % act_id, "%s-unit" % act_id
    units = ('<option value="">%s</option>' % t(field["unit_placeholder"])
             if field.get("unit_placeholder") else "")
    units += "".join('<option value="%s">%s</option>' % (e(u), t(u))
                     for u in field["units"])
    panels.append(
        '<div class="ks3-lstep-panel">'
        '<p class="ks3-lstep-label">%s</p>'
        '<p class="ks3-lstep-q">%s</p>'
        '<div class="ks3-lstep-answer">'
        '<label class="ks3-sr-only" for="%s">%s</label>'
        '<input class="ks3-lstep-input" type="text" inputmode="decimal" '
        'id="%s" placeholder="%s" autocomplete="off" data-lstep-ans>'
        '<label class="ks3-sr-only" for="%s">%s</label>'
        '<select class="ks3-sim-units ks3-lstep-unit" id="%s" data-lstep-unit>'
        '%s</select></div></div>'
        % (t(field.get("label", "")), t(field.get("question", "")),
           e(aid), t(field.get("hint", "")), e(aid),
           e(field.get("placeholder", "")), e(uid),
           t(field.get("unit_hint", "")), e(uid), units))

    reveal = "".join(
        '<div class="ks3-lstep-step">'
        '<span class="ks3-lstep-chip" aria-hidden="true">%s</span>'
        '<div class="ks3-lstep-stepbody">'
        '<p class="ks3-lstep-steplabel">%s</p>'
        '<p class="ks3-lstep-stepline" data-template="%s">%s</p>'
        '<p class="ks3-lstep-stepnote" data-template="%s">%s</p></div></div>'
        % (t(s.get("letter", "")), t(s.get("label", "")),
           e(s.get("line", "")), t(fill(s.get("line", ""))),
           e(s.get("note", "")), rich(fill(s.get("note", ""))))
        for s in steps)

    close = a.get("close") or {}
    progress = a.get("progress") or {}
    return ('<div class="ks3-lstep" data-lstep data-rig="%s" data-total="3" '
            'data-head="%s" '
            'data-close="%s" data-blank="%s" data-progress="%s" '
            'data-done-label="%s">'
            '<div class="ks3-lstep-panels">%s</div>'
            '<div class="ks3-lstep-foot">'
            '<button type="button" class="ks3-reveal-btn ks3-lstep-btn" '
            'data-lstep-open disabled>%s</button>'
            '<span class="ks3-lstep-progress" data-lstep-progress>%s</span>'
            '</div>'
            '<div class="ks3-lstep-reveal" hidden data-reveal>'
            '<p class="ks3-lstep-revealhead">%s</p>%s'
            '<p class="ks3-lstep-close" data-lstep-close></p></div></div>'
            # The heading's raw template rides on the instrument so
            # `wireLeverSteps` can repaint the shell's <h2> from the same
            # authored string the build filled — never from a second copy.
            % (e(a.get("rig", "")), e(a.get("heading", "")),
               e(close.get("template", "")),
               e(close.get("blank") or "—"),
               e(progress.get("format", "")),
               e(progress.get("done", "")),
               "".join(panels), t(a.get("button", "")),
               t(progress.get("format", "").replace("{n}", "0")),
               t(a.get("reveal_head", "")), reveal))


# DISPATCH: "meter-compare": ("ks3-meters-block", ' data-instrument data-metersblock data-stage-done="0"'),
#
# and in ACTIVITY_KIND_FN, beside the other B2 rows:
#     "meter-compare":          r_meter_compare,
#
# ⚠️ THIS RENDERER CONSUMES `options`, so `_KIND_FN_OWNS_OPTIONS` picks it up
# on its own — the literal `a.get("options")` below is what
# `_kinds_consuming()` reads out of the source. Nothing has to be added to a
# list by hand, which is the whole point of that mechanism, but it also means
# a future edit that stopped reading `options` would silently hand them back
# to the generic branch. It reads them; do not "tidy" that away.
#
# Place `r_meter_compare` beside `r_job_sort` in the B2 group
# (build_ks3.py ~2846). Needs `e`, `t`, `rich`, `r_activity_options`.


def r_meter_compare(a, act_id):
    """⊕ b2-04 `#s-meters` — three muscle groups, three readings each.

    ⚖️ THIS BLOCK IS WHY THE LESSON BELONGS TO BIOLOGY. `KS3.B.SKEL.02` asks
    for "the measurement of force exerted by different muscles" in as many
    words, and this is the only place on the page where a force is measured
    rather than calculated. Everything else here is a lever; this is a
    dynamometer and a mean.

    ⚖️ AND THE MEAN IS THE SECOND LESSON. Every group is reported as the mean
    of three readings that disagree — 312, 298, 305 — with the closing band
    saying in words that a single pull would have told you almost nothing.
    Three cards each showing one number would teach that muscles have exact
    strengths, which is the opposite.

    ⚠️ NOT `verdict-cards` and not `job-sort`. Both of those reveal PER ITEM,
    the instant that item is decided, and that is the pedagogy in each — a
    student finds out about item 1 before committing on item 2. Here there is
    ONE commitment about all three groups at once (their ORDER), and all three
    cards arrive together, because a ranking cannot be revealed a third at a
    time without giving the rest away.

    ⚠️ R3 — NOTHING MARKS. The three options are ranked orders and the cards
    arrive whichever one was chosen. There is no `data-correct` in this
    instrument, no per-option feedback and no disabling: the block is a
    commitment device, and the data is what settles it.

    `answer_index` is read HERE AND ONLY HERE — at build time, to check it is
    in range and, more usefully, that the numbers still support it. If a
    `rows` edit ever reordered the means, the build says so instead of the
    page quietly arguing for an option the data no longer backs. It reaches no
    attribute, no class and no student; the precedent is `keyed-commit`'s.

    ⚠️ A LIGHT `check` block on the DEFAULT card ground. `#s-build` directly
    above it takes the inset one. Two light blocks, two different grounds,
    measured off Design's markup — which is why this activity authors no
    `ground` key at all rather than authoring `card`.
    """
    rows = a.get("rows") or []
    if len(rows) < 2:
        raise ValueError(
            "meter-compare %r declares %d row(s). The block asks a student to "
            "rank groups against each other and one group is not a ranking."
            % (act_id, len(rows)))
    for r in rows:
        for key in ("name", "readings", "mean"):
            if not r.get(key):
                raise ValueError(
                    "meter-compare %r row %r is missing %r. The readings and "
                    "the mean are the pair that teaches: a mean with no "
                    "spread behind it is just a number."
                    % (act_id, r.get("name"), key))

    options = a.get("options") or []
    if len(options) < 2:
        raise ValueError(
            "meter-compare %r offers %d option(s); the commitment is a choice "
            "between candidate orderings." % (act_id, len(options)))

    # ⚠️ Build time only. See the docstring — this never reaches the page.
    ans = a.get("answer_index")
    if ans is not None:
        if not isinstance(ans, int) or isinstance(ans, bool):
            raise ValueError(
                "meter-compare %r answer_index is %r; it is an index into "
                "options[]." % (act_id, ans))
        if not 0 <= ans < len(options):
            raise ValueError(
                "meter-compare %r answer_index %d is out of range for %d "
                "option(s)." % (act_id, ans, len(options)))
        # ⚖️ The useful half of the check. Every row's name has to appear in
        # the option the lesson argues for, in descending order of its own
        # mean — so a row whose readings changed, or a fourth group added
        # without touching the options, fails the build instead of leaving
        # the page arguing for an order its own data contradicts.
        order = sorted(rows, key=lambda r: _meter_mean(r, act_id), reverse=True)
        text = options[ans].lower()
        at = -1
        for r in order:
            # The card's name qualifies the group ("Biceps, pulling up") and
            # the option names it plainly ("Biceps"), so the match is on the
            # head of the name — everything before the first comma. Matching
            # the whole string would fail on Design's own payload, and
            # authoring a second short name per row would be one more place
            # for the two to disagree.
            head = r["name"].split(",")[0].strip().lower()
            i = text.find(head)
            if i < 0:
                raise ValueError(
                    "meter-compare %r names %r as the correct order and it "
                    "does not mention %r at all."
                    % (act_id, options[ans], head))
            if i < at:
                raise ValueError(
                    "meter-compare %r says the correct order is %r, but its "
                    "own means rank them %s. The data and the answer have "
                    "stopped agreeing."
                    % (act_id, options[ans],
                       ", ".join(x["name"] for x in order)))
            at = i

    cards = "".join(
        '<div class="ks3-meters-card">'
        '<p class="ks3-meters-name">%s</p>'
        '<p class="ks3-meters-readings">%s</p>'
        '<p class="ks3-meters-mean">%s</p>'
        '<p class="ks3-meters-meanlabel">%s</p></div>'
        % (t(r["name"]), t(r["readings"]), t(r["mean"]),
           t(a.get("mean_label", "")))
        for r in rows)

    close = ('<p class="ks3-meters-close">%s</p>' % rich(a["close"])
             if a.get("close") else "")

    # `r_activity_options` rather than a second copy of the answer button:
    # this block's commitment is an ordinary four-square option list and the
    # only thing that differs is the measure it is set on.
    return ('<div class="ks3-meters" data-meters>'
            '<div class="ks3-meters-commit">%s</div>'
            '<div class="ks3-meters-reveal" hidden data-reveal>'
            '<div class="ks3-meters-cards">%s</div>%s</div></div>'
            % (r_activity_options(options), cards, close))


def _meter_mean(row, act_id):
    """The leading number of a row's `mean` string, for the build-time check.

    Parsed rather than authored as a second numeric field: the string on the
    page IS the value, and a `mean_value: 305` beside `mean: "305 N"` is two
    places for one number to live.
    """
    m = re.match(r"\s*(-?\d+(?:\.\d+)?)", str(row.get("mean", "")))
    if not m:
        raise ValueError(
            "meter-compare %r row %r has mean %r, which does not start with a "
            "number. The ordering check reads it."
            % (act_id, row.get("name"), row.get("mean")))
    return float(m.group(1))
# renderers: ═══ END B2 ═══

# renderers: ═══ BEGIN B3 ═══
# DISPATCH: "band-commit": ("ks3-plate-block", ' data-instrument data-plateblock data-stage-done="0"'),
#
# and in ACTIVITY_KIND_FN, beside the other B3 rows:
#     "band-commit":            r_band_commit,
#
# Place `r_band_commit` at the head of the B3 group (after the B2 rows,
# ~build_ks3.py 7056). Needs `e`, `t`, `rich`.
#
# ⚠️ THIS RENDERER DOES NOT CONSUME `options` OR `reveal`, and it must not
# start to. The block's controls are seven three-way band pickers, which are
# not answer buttons and are not `.ks3-option`; the activity authors neither
# key, so `_kinds_consuming()` correctly leaves both generic branches off.


def r_band_commit(a, act_id):
    """⊕ b3-01 `#s-plate` — commit all seven, then open all seven at once.

    ⚖️ THE GATE IS THE PEDAGOGY. Nothing opens until every one of the seven
    nutrients has been placed in a band, and the lede says why in as many
    words: *a guess you did not make cannot be wrong, and a guess that is never
    wrong teaches you nothing.* A per-row reveal — which is what `job-sort`
    does, and what this looks like from a distance — would let a student read
    row one's answer before committing on row two, and the whole argument of
    the block is that the SPREAD is the surprise. You cannot be surprised by a
    spread you were shown a seventh at a time.

    ⚖️ THE THREE-BRANCH VERDICT, and the branch that must not be dropped.
    NOTES-B3 §3.1 names it: a student who puts all seven in the same band gets
    a verdict that says so. That is the only place in the lesson where the
    target misconception — *balanced means equal amounts* — is read back to the
    student in their own answer rather than in the abstract. `verdicts` takes
    exactly three keys and this renderer raises without all three, because a
    missing branch is invisible: the block still works, it simply stops
    catching the one student it was built for.

    ⚠️ R3 / MRB-196 R10 — READ THIS BEFORE "TIDYING" THE MARKING.
    Nothing here is a `.ks3-option` and nothing takes a marking colour. The
    band buttons keep ONE chosen treatment whether the choice was right or
    wrong, before the reveal and after it; what changes on open is the ROW,
    which gains Design's own dark-ground selected treatment, and the row's why
    panel, which says "You had it" or "Actually tens of grams" in words. There
    is no `--ks3-ok`, no green, no drawn ✓ and no ✕ anywhere in this
    instrument. Design draws it exactly this way on the approved page and the
    distinction is real: the student is being told what the answer WAS, not
    being scored on having found it.

    ⚠️ EVERY TEXT RULE IN THE STYLESHEET IS SCOPED `.ks3-dark …`. This block is
    on ink on Design's page (`ks3-block ks3-dark ks3-practical`), `.ks3-dark p`
    is (0,1,1) and a bare `.ks3-plate-note` is (0,1,0) and loses. See the CSS.

    Emit-both-show-one throughout: all seven why panels, both band verdicts per
    row and all three closing branches are in the document, hidden, and the
    wiring only ever changes which is shown. No authored sentence is rebuilt in
    the browser, so the em dashes, the right single quotes and the `<em>`
    survive intact — and every one of these sentences is science.
    """
    bands = a.get("bands") or []
    if len(bands) < 2:
        raise ValueError(
            "band-commit %r offers %d band(s). The block asks a student to "
            "place a nutrient on a SCALE, and one band is not a scale."
            % (act_id, len(bands)))
    band_by_id = {}
    for i, b in enumerate(bands):
        for key in ("id", "label", "miss_label"):
            if not b.get(key):
                raise ValueError(
                    "band-commit %r band %d is missing %r. `miss_label` is the "
                    "sentence a student who missed this band reads back "
                    "(“Actually tens of grams”); composing it from "
                    "`label` in the browser would lower-case it there and put "
                    "an authored sentence inside the engine."
                    % (act_id, i, key))
        band_by_id[b["id"]] = b

    rows = a.get("rows") or []
    if not rows:
        raise ValueError("band-commit %r declares no rows[]." % act_id)
    for r in rows:
        for key in ("name", "hint", "band", "mass", "why"):
            if not r.get(key):
                raise ValueError(
                    "band-commit %r row %r is missing %r." % (act_id, r.get("name"), key))
        if r["band"] not in band_by_id:
            raise ValueError(
                "band-commit %r row %r sits in band %r, which is not one of "
                "%s. A row whose band no band offers can never be got right, "
                "and the verdict would be unreachable by construction."
                % (act_id, r["name"], r["band"], sorted(band_by_id)))

    verdicts = a.get("verdicts") or {}
    missing = sorted({"all_same", "close", "spread"} - set(verdicts))
    if missing:
        raise ValueError(
            "band-commit %r declares no %s verdict branch. All three are "
            "required: `all_same` is the only place the lesson's target "
            "misconception is named back to the student in their own answer, "
            "and a block that silently drops it still looks finished."
            % (act_id, ", ".join(missing)))

    hit_label = a.get("hit_label")
    if not hit_label:
        raise ValueError(
            "band-commit %r declares no `hit_label`." % act_id)

    row_html = []
    for i, r in enumerate(rows):
        band = band_by_id[r["band"]]
        picks = "".join(
            '<button type="button" class="ks3-plate-band" data-band="%s" '
            'aria-pressed="false">%s</button>' % (e(b["id"]), t(b["label"]))
            for b in bands)
        row_html.append(
            '<li class="ks3-plate-row" data-row="%d" data-answer="%s">'
            '<div class="ks3-plate-head">'
            '<p class="ks3-plate-name">%s</p>'
            '<p class="ks3-plate-hint">%s</p></div>'
            '<div class="ks3-plate-bands">%s</div>'
            '<div class="ks3-plate-why" hidden data-why>'
            '<p class="ks3-plate-real">'
            '<span data-real="hit" hidden>%s</span>'
            '<span data-real="miss" hidden>%s</span>'
            '<span class="ks3-plate-sep" aria-hidden="true"> · </span>'
            '<span class="ks3-plate-mass">%s</span></p>'
            '<p class="ks3-plate-note">%s</p></div></li>'
            % (i, e(r["band"]), t(r["name"]), t(r["hint"]), picks,
               t(hit_label), t(band["miss_label"]), t(r["mass"]),
               rich(r["why"])))

    # The three closing branches, all in the document and all hidden. `data-v`
    # is the branch name and nothing else — the sentences themselves never move
    # through an attribute.
    branches = "".join(
        '<p class="ks3-plate-vwhy" data-v="%s" hidden>%s</p>'
        % (e(k), rich(verdicts[k])) for k in ("all_same", "close", "spread"))

    return ('<div class="ks3-plate" data-plate data-total="%d">'
            '<ul class="ks3-plate-rows" role="list">%s</ul>'
            '<div class="ks3-plate-foot">'
            '<button type="button" class="ks3-reveal-btn ks3-plate-open" '
            'data-plate-open disabled aria-expanded="false">%s</button>'
            '<span class="ks3-plate-count" data-plate-count data-format="%s" '
            'data-done="%s">%s</span></div>'
            '<div class="ks3-plate-verdict" hidden data-plate-verdict>'
            '<p class="ks3-plate-vlabel">%s</p>'
            '<p class="ks3-plate-vhead" data-vhead data-format="%s" '
            'role="status"></p>%s</div></div>'
            % (len(rows), "".join(row_html),
               t(a.get("open_label") or "Show the real amounts"),
               e(a.get("commit_format") or "{n} of {total} committed"),
               e(a.get("commit_done") or "Opened"),
               t((a.get("commit_format") or "{n} of {total} committed")
                 .replace("{n}", "0").replace("{total}", str(len(rows)))),
               t(a.get("verdict_eyebrow") or "Your day, scored"),
               e(a.get("verdict_format") or "{n} of {total} in the right band."),
               branches))


# DISPATCH: "clinic-cases": ("ks3-clinic-block", ' data-instrument data-clinicblock data-stage-done="0"'),
#
# and in `ACTIVITY_KIND_FN`, beside the other B3 rows:
#     "clinic-cases":           r_clinic_cases,
#
# Place `r_clinic_cases` beside `r_settles_it` — it is CONTRAST's other
# flagship and shares the ruling that shapes it. Needs `e`, `t`, `rich` and
# `_self_check`, all of which build_ks3.py already defines.
#
# ⚠️ THIS RENDERER DOES NOT CONSUME `options`. The three imbalance buttons are
# a MULTI-SELECT and are authored as `kinds[]`, not as `options[]`, so
# `_KIND_FN_OWNS_OPTIONS` does not pick this kind up and must not: a lesson
# that ever authors a genuine single-answer `options` list beside this block
# still gets the generic list, which is correct. The `self_check` options are
# drawn by `_self_check` and are not `a["options"]` either.


def r_clinic_cases(a, act_id):
    """⊕ b3-04 `#s-cases` — five clinics, and two of them have two answers.

    ⚖️ THE MULTI-SELECT IS THE LESSON. Every other case instrument in the key
    stage asks for ONE answer per item — `job-sort`, `verdict-cards`,
    `sort-task`. This one asks the student to tick *every* imbalance that
    applies, and clinics 2 and 5 have two. NOTES-B3 §2 states the pedagogy in
    one line: "Refusing to tick two is the error being taught." Rendering this
    as a one-of-three picker would remove the only thing the block exists for,
    which is why it is not `verdict-cards` with three options.

    ⚖️ CLINIC 5 IS NOT A DIET PROBLEM AT ALL — an adequate plate and a
    shortened intestine — and it is deliberately inside a diet lesson, because
    it is the bridge into lessons 5 to 7. `min_multi` below refuses a payload
    in which no case carries more than one answer: a five-clinic set where
    every clinic has exactly one answer is a different exercise wearing this
    one's markup, and it would pass every other gate silently.

    ⚠️ MRB-196 R10, AND IT MOVES DESIGN'S COPY. Design computes whether the
    student's ticks matched exactly and spends it on the verdict LABEL —
    "You had it exactly" / "Two imbalances apply here" / "Not quite". Two of
    those three branches are the page marking an activity, which R3 forbids
    and R10 replaces with a self-check the student answers for themselves.

    The third branch is not a verdict on the student at all: "Two imbalances
    apply here" is a fact about the CASE. So it survives — as `verdict_label`,
    authored per case and shown to everyone identically. That also fixes a
    defect in Design's own logic, and it is the more serious half: a student
    who ticked BOTH answers on clinic 2 took the `exact` branch and therefore
    never saw the line telling them two imbalances apply. The page's own
    teaching sentence was shown only to the students who got it wrong.

    ⚠️ NOTHING MARKS. The pick buttons are `.ks3-clinic-pick`, not
    `.ks3-option`, so the reveal may disable them without failing R3's runtime
    assertion — the same construction `settles-it` uses for its two choice
    buttons. After the diagnosis the UNCHOSEN picks dim, which records what was
    spent and not whether it was right; nothing anywhere carries `data-correct`
    and nothing green or red appears on any control in this block.

    ⚠️ INK-DARK. `.ks3-dark p` is (0,1,1) and beats a bare instrument class at
    (0,1,0), so every colour rule in the stylesheet is scoped `.ks3-dark …`.
    On this block the intake line is the one that would visibly break: amber
    mono is how a student finds the number, and unscoped it falls to on-dark
    body copy and reads as another sentence of the description.

    Emit-all-show-one: five panels are in the document and one is shown. No
    authored sentence is ever rebuilt in JS from an attribute, so the em
    dashes, the right single quotes and the ⚠️-flagged tone of this lesson
    survive exactly as written.
    """
    cases = a.get("cases") or []
    kinds = a.get("kinds") or []
    if len(cases) < 2:
        raise ValueError(
            "clinic-cases %r declares %d case(s). The block is a run of "
            "judgements read against each other and one case is not a run."
            % (act_id, len(cases)))
    if len(kinds) < 2:
        raise ValueError(
            "clinic-cases %r offers %d kind(s) to tick. The whole exercise is "
            "choosing among them — and choosing more than one."
            % (act_id, len(kinds)))

    known = []
    for k in kinds:
        if not k.get("id") or not k.get("label"):
            raise ValueError(
                "clinic-cases %r kind %r needs both `id` and `label`."
                % (act_id, k))
        known.append(k["id"])

    multi = 0
    for c in cases:
        for key in ("id", "label", "description", "intake", "verdict_label",
                    "answer", "why"):
            if not c.get(key):
                raise ValueError(
                    "clinic-cases %r case %r is missing %r. Every one of the "
                    "seven is drawn, and an empty one renders as a gap in the "
                    "panel." % (act_id, c.get("id"), key))
        picks = c.get("kinds") or []
        if not picks:
            raise ValueError(
                "clinic-cases %r case %r names no correct kinds[]; a clinic "
                "with no answer cannot be diagnosed."
                % (act_id, c.get("id")))
        for p in picks:
            if p not in known:
                raise ValueError(
                    "clinic-cases %r case %r names kind %r, which is not one "
                    "of the %d offered: %s."
                    % (act_id, c["id"], p, len(known), ", ".join(known)))
        if len(picks) > 1:
            multi += 1

    # ⚖️ Build time only, and it never reaches the page. See the docstring:
    # a set in which nothing has two answers is a different exercise.
    if not multi:
        raise ValueError(
            "clinic-cases %r has no case with more than one correct kind. "
            "This instrument exists because refusing to tick two is the error "
            "being taught; with one answer everywhere it is a picker."
            % act_id)

    counts = a.get("count_labels") or {}
    for key in ("none", "some", "done"):
        if not counts.get(key):
            raise ValueError(
                "clinic-cases %r count_labels is missing %r. The readout has "
                "three states and a missing one renders as an empty span."
                % (act_id, key))
    if "{n}" not in counts["some"]:
        raise ValueError(
            "clinic-cases %r count_labels['some'] is %r and carries no {n}. "
            "It is the live one." % (act_id, counts["some"]))

    tabs = "".join(
        '<button type="button" class="ks3-sim-seg-btn ks3-clinic-tab" '
        'data-case="%s" aria-pressed="%s">%s</button>'
        % (e(c["id"]), "true" if i == 0 else "false",
           t(c.get("tab_label") or c["label"]))
        for i, c in enumerate(cases))

    panels = []
    for i, c in enumerate(cases):
        picks = "".join(
            '<button type="button" class="ks3-sim-seg-btn ks3-clinic-pick" '
            'data-kind="%s" aria-pressed="false">%s</button>'
            % (e(k["id"]), t(k["label"])) for k in kinds)
        panels.append(
            '<div class="ks3-clinic-panel" data-case="%s" data-open="0"%s>'
            '<div class="ks3-clinic-brief">'
            '<p class="ks3-clinic-label">%s</p>'
            '<p class="ks3-clinic-desc">%s</p>'
            '<p class="ks3-clinic-intake">%s</p></div>'
            '<p class="ks3-clinic-picklabel">%s</p>'
            '<div class="ks3-clinic-picks">%s</div>'
            '<div class="ks3-clinic-foot">'
            '<button type="button" class="ks3-reveal-btn ks3-clinic-reveal" '
            'data-clinic-reveal disabled>%s</button>'
            '<span class="ks3-clinic-count" data-clinic-count role="status" '
            'data-none="%s" data-some="%s" data-done="%s">%s</span></div>'
            '<div class="ks3-clinic-verdict" hidden data-reveal>'
            '<p class="ks3-clinic-verdict-label">%s</p>'
            '<p class="ks3-clinic-answer">%s</p>'
            '<p class="ks3-clinic-why">%s</p></div></div>'
            % (e(c["id"]), "" if i == 0 else " hidden",
               t(c["label"]), rich(c["description"]), t(c["intake"]),
               t(a.get("pick_label") or "Tick every imbalance that applies"),
               picks,
               t(a.get("reveal_label") or "Show the diagnosis"),
               e(counts["none"]), e(counts["some"]), e(counts["done"]),
               t(counts["none"]),
               t(c["verdict_label"]), rich(c["answer"]), rich(c["why"])))

    return ('<div class="ks3-clinic" data-clinic data-total="%d">'
            '<div class="ks3-clinic-tabs" role="list">%s</div>%s</div>%s'
            % (len(cases), tabs, "".join(panels), _self_check(a, act_id)))


# DISPATCH: "enzyme-run": ("ks3-erun-block", ' data-instrument data-erunblock data-stage-done="0"'),
#
# and in `ACTIVITY_KIND_FN`, beside the other B3 rows:
#     "enzyme-run":             r_enzyme_run,
#
# Place `r_enzyme_run` and `_erun_rate` beside `r_gut_journey`. Needs `e`, `t`,
# `rich` and `json`, all of which build_ks3.py already imports or defines.
#
# ⚠️ THE ONLY TIMER IN THE UNIT. NOTES-B3 §6 says so in as many words:
# "`enzyme-run` is the only one with a timer. Nothing else in the unit
# animates." That is why this is the one B3 fragment with a reduced-motion
# contract to honour, and why `reduced_motion_scale` is authored rather than
# assumed.


def _erun_rate(model, temp, ph, opt_ph):
    """The rate curve, as a fraction of maximum — Design's own model.

    ⚠️ `rateFor()` in `shared/ks3.js` is THIS FUNCTION, and the two must agree
    exactly. It exists in Python for one reason: the resting page has to print
    the same rate the first repaint computes, or the number visibly jumps on
    load and the shipped HTML — which is what a crawler and a reader with JS
    off get — carries a figure the instrument disagrees with. Same reason
    `heating-bench` duplicates its rounding rule.

    It is deliberately not a second MODEL: every constant comes from the
    authored `model` dict, so a corrected curve is one data edit and the two
    evaluations move together.
    """
    denature = float(model["denature_c"])
    if temp >= denature:
        return 0.0
    opt = float(model["optimum_c"])
    if temp <= opt:
        t_term = (temp / opt) ** float(model["rise_exponent"]) if opt else 0.0
    else:
        t_term = max(0.0, 1.0 - ((temp - opt) / float(model["fall_divisor"])) ** 2)
    gap = abs(float(ph) - float(opt_ph))
    p_term = max(0.0, 1.0 - gap / float(model["ph_span"]))
    return max(0.0, min(1.0, t_term * p_term))


def _erun_band(bands, denatured, temp, denature_c):
    """Which of the six temperature notes is showing, at rest.

    Same branch order as `noteFor()` in shared/ks3.js, for the same reason
    `_erun_rate` exists: the note on the shipped page must be the note the
    first repaint chooses.
    """
    if denatured and temp >= denature_c:
        return "denatured_hot"
    if denatured:
        return "denatured_cool"
    if temp >= bands["past_optimum"]:
        return "past_optimum"
    if temp >= bands["optimum"]:
        return "optimum"
    if temp >= bands["cold"]:
        return "cold"
    return "freezing"


def r_enzyme_run(a, act_id):
    """⊕ b3-06 `#s-bench` — three counters, and one of them never moves.

    ⚖️ THE THIRD COUNTER IS THE LESSON. NOTES-B3 §2 puts it in one line: "a
    running reaction with three counters, one of which never moves. That
    counter *is* the lesson." So the enzyme count is emitted as an authored
    STRING with a full-width bar and NO `data-value` and NO `data-bar` handle
    for the runtime to take hold of. It is the same construction as
    `heating-bench`'s mass tile, and for the same reason: the one number the
    prose says must not move is wired to nothing, so it cannot move even by
    accident.

    ⚖️ THE DENATURE LATCH IS THE OTHER HALF, and it is the misconception the
    block exists to kill. Heat past the threshold and the enzyme is finished;
    cooling does not bring it back, switching enzyme does not bring it back
    while the tube is still hot, and only a fresh tube clears it. The latch
    fires on the TEMPERATURE control rather than inside the run tick —
    NOTES-B3 flag 16 records that a student who dragged to 60 °C, read 0%, and
    dragged back to 37 °C used to be shown a full recovery, so the instrument
    built to kill the idea was demonstrating it.

    ⚠️ ONE THRESHOLD, AUTHORED ONCE. `model.denature_c` is quoted in the key
    fact, in two of the six temperature notes, in the key note, in a ladder
    correction and in the stretch layer. It reaches the runtime through
    `data-cfg` and the prose through the lesson record; there is exactly one
    number, and the module docstring lists every sentence that repeats it.

    ⚠️ EVERY BRANCHING SENTENCE IS IN THE DOCUMENT. Six temperature notes and
    three verdicts, all nine emitted, eight hidden — emit-all-show-one. None is
    assembled in JS from an attribute, so the em dashes, right single quotes
    and degree signs survive and a science correction is a data edit. Only two
    live numbers are ever substituted: the tick count and the rate percentage.

    ⊕ ADDED INSIDE A COMPONENT DESIGN DREW, where the page is silent. Design
    shows the verdict on `clock >= ticks || (everRan && !running && denatured)`.
    A run at a rate of exactly zero that is NOT denatured — stomach protease
    dropped into pH 8, which is one press of one button — finishes on its first
    tick and shows no verdict at all: the bench goes quiet and says nothing,
    and the "slow" verdict that exists to send the student back to the pH dial
    never appears. The wiring shows the verdict whenever a run has FINISHED,
    whatever finished it. Design's three branches are unchanged.

    ⚠️ INK-DARK. `.ks3-dark p` is (0,1,1) and beats a bare instrument class at
    (0,1,0), so every colour rule in the stylesheet is scoped `.ks3-dark …`.
    Here the rate readout and the temperature figure are what would visibly
    break: amber mono is how a student reads a dial, and unscoped they fall to
    on-dark body copy and stop looking like numbers.

    ⚑ FOR MIDE, recorded here as well as in the lesson module: the enzyme
    counter's bar is `--ks3-ok`. That token's own comment in `tokens.css`
    reserves green for the ladder marking correctness, and this is a bar
    meaning "unchanged" on a block that marks nothing. Design drew it; it is
    reproduced as drawn and registered in a parity row, so the day the palette
    question is ruled the gate says exactly where the value lives. Same
    handling as `scale-cards`' amber distance label.
    """
    enzymes = a.get("enzymes") or []
    phs = a.get("phs") or []
    if len(enzymes) < 2:
        raise ValueError(
            "enzyme-run %r declares %d enzyme(s). One cannot show that each "
            "has its own substrate and its own best pH." % (act_id, len(enzymes)))
    if len(phs) < 2:
        raise ValueError(
            "enzyme-run %r offers %d pH setting(s); the pH dial is half the "
            "bench." % (act_id, len(phs)))

    for z in enzymes:
        missing = [k for k in ("id", "label", "equation", "counter_substrate",
                               "counter_product") if not z.get(k)]
        if missing:
            raise ValueError(
                "enzyme-run %r enzyme %r is missing %s. The counter names are "
                "authored per enzyme rather than built from a substrate word, "
                "because 'Fatty acids and glycerol made' is a sentence and not "
                "a capitalisation." % (act_id, z.get("id"), ", ".join(missing)))
        if z.get("opt_ph") is None:
            raise ValueError(
                "enzyme-run %r enzyme %r declares no opt_ph; the pH term is "
                "the gap to it." % (act_id, z["id"]))

    for p in phs:
        if p.get("value") is None or not p.get("label"):
            raise ValueError(
                "enzyme-run %r pH setting %r needs both `value` and `label`."
                % (act_id, p))

    model = a.get("model") or {}
    for key in ("denature_c", "optimum_c", "rise_exponent", "fall_divisor",
                "ph_span"):
        if model.get(key) is None:
            raise ValueError(
                "enzyme-run %r model is missing %r. The curve is a simplified "
                "model and all five constants are authored, so the legal line "
                "can say so truthfully." % (act_id, key))

    run = a.get("run") or {}
    for key in ("ticks", "tick_ms", "units_per_tick", "start_substrate",
                "reduced_motion_scale", "slow_below_pct"):
        if run.get(key) is None:
            raise ValueError("enzyme-run %r run is missing %r." % (act_id, key))
    labels = run.get("labels") or {}
    for key in ("start", "more", "running", "reset", "clock", "clock_fresh",
                "rate"):
        if not labels.get(key):
            raise ValueError(
                "enzyme-run %r run.labels is missing %r." % (act_id, key))
    if "{n}" not in labels["clock"] or "{total}" not in labels["clock"]:
        raise ValueError(
            "enzyme-run %r run.labels['clock'] is %r; it carries both live "
            "numbers and needs {n} and {total}." % (act_id, labels["clock"]))
    if "{pct}" not in labels["rate"]:
        raise ValueError(
            "enzyme-run %r run.labels['rate'] is %r and carries no {pct}."
            % (act_id, labels["rate"]))

    units = a.get("units_format")
    if not units or "{n}" not in units:
        raise ValueError(
            "enzyme-run %r units_format is %r; the counter values are authored "
            "copy and carry the live count as {n}." % (act_id, units))
    if not a.get("enzyme_counter_label") or not a.get("enzyme_counter_value"):
        raise ValueError(
            "enzyme-run %r needs enzyme_counter_label and "
            "enzyme_counter_value. The third counter's value is a CONSTANT "
            "string — it is the one readout nothing may compute." % act_id)

    # ⚠️ SIX BRANCHES, ALL NAMED. The wiring chooses among these keys and
    # nothing else; a missing one leaves the note blank at exactly the
    # temperature the student dragged to.
    notes = a.get("temp_notes") or {}
    for key in ("denatured_hot", "denatured_cool", "past_optimum", "optimum",
                "cold", "freezing"):
        if not notes.get(key):
            raise ValueError(
                "enzyme-run %r temp_notes is missing %r. Both denatured "
                "branches are required and they say different things: "
                "'cool it, then take a fresh tube' has to be distinguishable "
                "from 'cooling changes nothing'." % (act_id, key))
    bands = a.get("temp_bands") or {}
    for key in ("past_optimum", "optimum", "cold"):
        if bands.get(key) is None:
            raise ValueError(
                "enzyme-run %r temp_bands is missing %r." % (act_id, key))

    verdicts = a.get("verdicts") or {}
    for key in ("denatured", "slow", "worked"):
        if not verdicts.get(key):
            raise ValueError(
                "enzyme-run %r verdicts is missing %r. Three branches are "
                "drawn and the denatured one is the block's whole argument."
                % (act_id, key))

    groups = a.get("group_labels") or {}
    for key in ("enzyme", "ph", "temp"):
        if not groups.get(key):
            raise ValueError(
                "enzyme-run %r group_labels is missing %r." % (act_id, key))

    temp = a.get("temp") or {}
    for key in ("min", "max", "start", "step", "format", "field_label"):
        if temp.get(key) is None:
            raise ValueError("enzyme-run %r temp is missing %r." % (act_id, key))
    if "{t}" not in temp["format"]:
        raise ValueError(
            "enzyme-run %r temp['format'] is %r and carries no {t}."
            % (act_id, temp["format"]))

    start_ph = a.get("start_ph", phs[0]["value"])
    if start_ph not in [p["value"] for p in phs]:
        raise ValueError(
            "enzyme-run %r opens at pH %r, which is not one of the %d offered."
            % (act_id, start_ph, len(phs)))

    cfg = {
        "denature_c": model["denature_c"],
        "optimum_c": model["optimum_c"],
        "rise_exponent": model["rise_exponent"],
        "fall_divisor": model["fall_divisor"],
        "ph_span": model["ph_span"],
        "ticks": run["ticks"],
        "tick_ms": run["tick_ms"],
        "units_per_tick": run["units_per_tick"],
        "start_substrate": run["start_substrate"],
        "reduced_motion_scale": run["reduced_motion_scale"],
        "slow_below_pct": run["slow_below_pct"],
        "temp_format": temp["format"],
        "units_format": units,
        "bands": {"past_optimum": bands["past_optimum"],
                  "optimum": bands["optimum"], "cold": bands["cold"]},
        "labels": dict(labels),
        "opt_ph": {z["id"]: z["opt_ph"] for z in enzymes},
    }

    # The resting readouts, from the same constants the runtime uses.
    rest_rate = int(round(_erun_rate(model, float(temp["start"]), start_ph,
                                     enzymes[0]["opt_ph"]) * 100))
    rest_note = _erun_band(bands, False, float(temp["start"]),
                           float(model["denature_c"]))
    field = "erun-temp-%s" % act_id

    ztabs = "".join(
        '<button type="button" class="ks3-sim-seg-btn ks3-erun-enzyme" '
        'data-enzyme="%s" aria-pressed="%s">%s</button>'
        % (e(z["id"]), "true" if i == 0 else "false", t(z["label"]))
        for i, z in enumerate(enzymes))

    ptabs = "".join(
        '<button type="button" class="ks3-sim-seg-btn ks3-erun-ph" '
        'data-ph="%s" aria-pressed="%s">%s</button>'
        % (e(p["value"]), "true" if p["value"] == start_ph else "false",
           t(p["label"]))
        for p in phs)

    # One equation per enzyme, all in the document. `t()` DRAWS the arrow:
    # U+2192 is absent from all five latin woff2 subsets, and typed as a
    # character it drops to a system font mid-line.
    equations = "".join(
        '<span class="ks3-erun-equation" data-enzyme="%s"%s>%s</span>'
        % (e(z["id"]), "" if i == 0 else " hidden", t(z["equation"]))
        for i, z in enumerate(enzymes))

    def names(key):
        return "".join(
            '<span class="ks3-erun-countername" data-enzyme="%s"%s>%s</span>'
            % (e(z["id"]), "" if i == 0 else " hidden", t(z[key]))
            for i, z in enumerate(enzymes))

    counters = (
        '<li class="ks3-erun-counter" data-counter="substrate">'
        '<div class="ks3-erun-counterhead">'
        '<p class="ks3-erun-counterlabel">%s</p>'
        '<p class="ks3-erun-countervalue" data-value="substrate">%s</p></div>'
        '<span class="ks3-erun-track">'
        '<span class="ks3-erun-bar" data-bar="substrate" style="width:100%%">'
        '</span></span></li>'
        '<li class="ks3-erun-counter" data-counter="product">'
        '<div class="ks3-erun-counterhead">'
        '<p class="ks3-erun-counterlabel">%s</p>'
        '<p class="ks3-erun-countervalue" data-value="product">%s</p></div>'
        '<span class="ks3-erun-track">'
        '<span class="ks3-erun-bar" data-bar="product" style="width:0%%">'
        '</span></span></li>'
        # ⚖️ NO HANDLE. No `data-value`, no `data-bar` — the counter the prose
        # says must not move has nothing for the runtime to take hold of.
        '<li class="ks3-erun-counter" data-counter="enzyme">'
        '<div class="ks3-erun-counterhead">'
        '<p class="ks3-erun-counterlabel">%s</p>'
        '<p class="ks3-erun-countervalue">%s</p></div>'
        '<span class="ks3-erun-track">'
        '<span class="ks3-erun-bar ks3-erun-bar-fixed" style="width:100%%">'
        '</span></span></li>'
        % (names("counter_substrate"),
           t(units.replace("{n}", str(run["start_substrate"]))),
           names("counter_product"), t(units.replace("{n}", "0")),
           t(a["enzyme_counter_label"]), t(a["enzyme_counter_value"])))

    tnotes = "".join(
        '<span class="ks3-erun-tempnote" data-note="%s"%s>%s</span>'
        % (key, "" if key == rest_note else " hidden", rich(notes[key]))
        for key in ("denatured_hot", "denatured_cool", "past_optimum",
                    "optimum", "cold", "freezing"))

    vnotes = "".join(
        '<span class="ks3-erun-verdicttext" data-verdict="%s" hidden>%s</span>'
        % (key, rich(verdicts[key]))
        for key in ("denatured", "slow", "worked"))

    return ('<div class="ks3-erun" data-erun data-cfg="%s">'
            '<div class="ks3-erun-dials">'
            '<div class="ks3-erun-dial"><p class="ks3-erun-diallabel">%s</p>'
            '<div class="ks3-erun-seg">%s</div></div>'
            '<div class="ks3-erun-dial"><p class="ks3-erun-diallabel">%s</p>'
            '<div class="ks3-erun-seg">%s</div></div></div>'

            '<div class="ks3-erun-temp">'
            '<div class="ks3-erun-temphead">'
            '<p class="ks3-erun-diallabel">%s</p>'
            '<p class="ks3-erun-tempvalue" data-temp-value>%s</p></div>'
            '<label class="ks3-erun-srlabel" for="%s">%s</label>'
            '<input class="ks3-erun-slider" type="range" id="%s" min="%s" '
            'max="%s" step="%s" value="%s" data-temp aria-valuetext="%s">'
            '<p class="ks3-erun-tempnotes" data-tempnotes role="status">%s</p>'
            '</div>'

            '<div class="ks3-erun-tube">'
            '<div class="ks3-erun-tubehead">'
            '<p class="ks3-erun-reaction">%s</p>'
            '<p class="ks3-erun-rate" data-rate>%s</p></div>'
            '<ul class="ks3-erun-counters" role="list">%s</ul>'
            '<div class="ks3-erun-controls">'
            '<button type="button" class="ks3-reveal-btn ks3-erun-run" '
            'data-run>%s</button>'
            '<button type="button" class="ks3-reveal-btn ks3-erun-reset" '
            'data-reset>%s</button>'
            '<span class="ks3-erun-clock" data-clock>%s</span></div>'
            '<p class="ks3-erun-verdict" hidden data-reveal>%s</p>'
            '</div></div>'
            % (e(json.dumps(cfg, sort_keys=True)),
               t(groups["enzyme"]), ztabs, t(groups["ph"]), ptabs,
               t(groups["temp"]),
               t(temp["format"].replace("{t}", str(temp["start"]))),
               e(field), t(temp["field_label"]), e(field),
               e(temp["min"]), e(temp["max"]), e(temp["step"]),
               e(temp["start"]),
               e(temp["format"].replace("{t}", str(temp["start"]))),
               tnotes, equations,
               t(labels["rate"].replace("{pct}", str(rest_rate))),
               counters, t(labels["start"]), t(labels["reset"]),
               t(labels["clock_fresh"]), vnotes))


# DISPATCH: "fold-builder": ("ks3-fold-block", ' data-instrument data-foldblock data-stage-done="0"'),
#
# and in ACTIVITY_KIND_FN, beside the other B3 rows:
#     "fold-builder":           r_fold_builder,
#
# Place `r_fold_builder` in the B3 group, after `r_enzyme_run`. Needs `e`, `t`,
# `rich` — and nothing else; there is no canvas, no timer and no third-party
# anything in this instrument.
#
# ⚠️ THIS RENDERER DOES NOT CONSUME `options` OR `reveal`. Its controls are
# three state toggles, which are not answer buttons and are not `.ks3-option`;
# the activity authors neither key, so `_kinds_consuming()` correctly leaves
# both generic branches off. Do not start reading `options` here — the block
# has no question in it and R3 would have nowhere to stand.


def _fold_area_text(value):
    """Design's own three-branch number format, for the RESTING render only.

    `wireFoldBuilder` carries the same four lines and recomputes on every
    toggle. Two copies is a real cost and it buys the thing `head_counter`'s
    `start` buys one level up: the HTML that ships already says `0.50 m²`, so a
    crawler, a reader with JS off and anything that quotes the page all get the
    number the page means rather than a placeholder or an empty element.

    ⚠️ `int(v + 0.5)` and NOT `round()`. Python rounds half to even and
    JavaScript's `Math.round` rounds half up, so `round(10.5)` is 10 here and
    11 there — a divergence that would be invisible at rest (0 levels reads
    0.50 either way) and visible the moment someone reused this helper for a
    driven state. The two implementations agree by construction instead.
    Areas and multiples are positive by construction, so truncation after the
    half-add is a floor, and `math` does not have to be imported for it.
    """
    if value < 1:
        return "%.2f" % value
    if value < 10:
        return "%.1f" % value
    return "%d" % int(value + 0.5)


def _fold_multiple_text(ratio):
    """The same rule at one decimal below ten, whole numbers above."""
    if ratio < 10:
        return "%.1f" % ratio
    return "%d" % int(ratio + 0.5)


def _fold_factor_text(factor):
    """A level's multiplier as it is printed on its own button face.

    Whole numbers print whole — Design's `'On · ×' + l.factor` on an integer
    factor gives `×3`, and `×3.0` would read as a measured quantity rather
    than as the count of times the sheet was folded.
    """
    return ("%d" % factor) if float(factor).is_integer() else ("%g" % factor)


def r_fold_builder(a, act_id):
    """⊕ b3-07 `#s-fold` — build the surface up, one folding level at a time.

    ⚖️ THE MODEL IS BUILT UP, NOT BROKEN DOWN, and that is the family. B3's
    other switch instrument (`job-switch`, b3-08) starts with everything
    working and takes things away; this one starts with a plain tube and adds.
    Same control, opposite direction, and the direction is the lesson: the
    student watches half a square metre become thirty while the length written
    beside it never moves.

    ⚖️ THE LENGTH NEVER CHANGES, AND THE COPY SAYS SO AT EVERY STEP. All four
    notes are authored (NOTES-B3 §3.5) and three of them name the six metres
    again. That repetition is the whole confrontation of `#s-think` — *"Villi
    make the intestine longer"* — done with a number instead of a sentence, so
    it is not something to tidy out of the payload.

    ⚠️ THE NOTES ARE INDEXED BY **HOW MANY** LEVELS ARE ON, NOT BY WHICH.
    Four strings, one per count, exactly as NOTES-B3 §3.5 specifies. A note per
    level would be three strings and would have nothing to say about the plain
    tube, which is the state the whole comparison is measured from.

    ⚠️ NOTHING MARKS. There is no right answer here and no `answer_index` to
    check: a level is on or off and both are legitimate places to stand. The
    three toggles are `aria-pressed` toggle buttons and are deliberately NOT
    `.ks3-option`, so no R3 gate has to make an exception for them.

    ⚠️ INK-DARK. `.ks3-dark p` is (0,1,1) and beats a bare instrument class at
    (0,1,0), so every text rule in the stylesheet is scoped to at least
    (0,2,0). See the CSS; the readout note is the row that would ship broken.

    Emit-both-show-one: all four notes are in the document, three hidden, and
    `wireFoldBuilder` swaps which is shown. No authored sentence is ever
    rebuilt in JS from an attribute — only the two NUMBERS are, which is what
    an arithmetic readout is for.
    """
    levels = a.get("levels") or []
    if len(levels) < 2:
        raise ValueError(
            "fold-builder %r declares %d level(s). The block's argument is "
            "that folding COMPOUNDS — folds on folds on folds — and one "
            "multiplier is not a compounding." % (act_id, len(levels)))

    base = a.get("base_area")
    if not isinstance(base, (int, float)) or isinstance(base, bool) or base <= 0:
        raise ValueError(
            "fold-builder %r needs a positive `base_area` — every number the "
            "block prints is a multiple of it." % act_id)

    for l in levels:
        for key in ("id", "name", "factor", "what", "scale"):
            if not l.get(key):
                raise ValueError(
                    "fold-builder %r level %r is missing %r. `scale` is not "
                    "optional: it is what tells a student that the three "
                    "levels are three different SIZES of the same trick, and "
                    "without it they read as three unrelated facts."
                    % (act_id, l.get("id") or l.get("name"), key))
        if not isinstance(l["factor"], (int, float)) or isinstance(l["factor"], bool):
            raise ValueError(
                "fold-builder %r level %r has factor %r, which is not a "
                "number." % (act_id, l["id"], l["factor"]))

    notes = a.get("notes") or []
    if len(notes) != len(levels) + 1:
        raise ValueError(
            "fold-builder %r declares %d note(s) for %d level(s); it needs "
            "%d — one per COUNT, including the plain tube at zero. A missing "
            "note is a state the instrument can reach with nothing to say "
            "about it." % (act_id, len(notes), len(levels), len(levels) + 1))

    labels = a.get("labels") or {}
    off_label = labels.get("off")
    on_label = labels.get("on")
    if not off_label or not on_label:
        raise ValueError(
            "fold-builder %r needs `labels.off` and `labels.on` — the button "
            "face is the only thing that says what pressing it will do."
            % act_id)

    rows = []
    for l in levels:
        # `{factor}` is filled HERE rather than in JS, so the button carries
        # its two finished labels and the runtime only swaps between them.
        # Design writes `'On · ×' + l.factor`; the multiplication
        # sign is U+00D7 and IS in the five latin subsets (unlike → ✓ ✕), so
        # it is typed rather than drawn.
        lit = on_label.replace("{factor}", _fold_factor_text(l["factor"]))
        rows.append(
            '<li class="ks3-fold-level" data-level="%s" data-factor="%s" '
            'data-on="0">'
            '<div class="ks3-fold-levelmain">'
            '<div class="ks3-fold-levelwhat">'
            '<p class="ks3-fold-name">%s</p>'
            '<p class="ks3-fold-what">%s</p>'
            '<p class="ks3-fold-scale">%s</p></div>'
            '<button type="button" class="ks3-fold-toggle" data-fold-toggle '
            'aria-pressed="false" data-label-on="%s" data-label-off="%s">%s'
            '</button></div></li>'
            % (e(l["id"]), e(l["factor"]), t(l["name"]), rich(l["what"]),
               t(l["scale"]), e(lit), e(off_label), t(off_label)))

    # Emit-both-show-one. Index 0 is the plain tube and is the one shown.
    note_html = "".join(
        '<p class="ks3-fold-note" data-note="%d"%s>%s</p>'
        % (i, "" if i == 0 else " hidden", rich(n))
        for i, n in enumerate(notes))

    area_format = a.get("area_format") or "{a}"
    multiple_format = a.get("multiple_format") or "{x}"
    if "{a}" not in area_format:
        raise ValueError(
            "fold-builder %r `area_format` %r has no {a} placeholder, so the "
            "area would never be printed." % (act_id, area_format))
    if "{x}" not in multiple_format:
        raise ValueError(
            "fold-builder %r `multiple_format` %r has no {x} placeholder."
            % (act_id, multiple_format))

    # The resting values, computed here so the shipped HTML is already right.
    total = base
    for l in levels:
        total *= l["factor"]
    rest_width = max(2.0, (base / total) * 100.0)

    return ('<div class="ks3-fold" data-fold data-base="%s" '
            'data-area-format="%s" data-multiple-format="%s">'
            '<ul class="ks3-fold-levels" role="list">%s</ul>'
            '<div class="ks3-fold-readout">'
            '<div class="ks3-fold-readhead">'
            '<p class="ks3-fold-readlabel">%s</p>'
            '<p class="ks3-fold-area" data-fold-area>%s</p></div>'
            '<span class="ks3-fold-track">'
            '<span class="ks3-fold-bar" data-fold-bar data-full="0" '
            'style="width:%.1f%%"></span></span>'
            # ⚠️ `role="status"` on the NOTE, never on the instrument root. A
            # live region wrapping the whole block would re-announce three
            # level descriptions and a bar every time a toggle moved.
            '<div class="ks3-fold-noteline" role="status">%s</div>'
            '<p class="ks3-fold-multiple" data-fold-multiple>%s</p>'
            '</div></div>'
            % (e(base), e(area_format), e(multiple_format), "".join(rows),
               t(a.get("readout_label") or ""),
               t(area_format.replace("{a}", _fold_area_text(base))),
               rest_width, note_html,
               t(multiple_format.replace("{x}", _fold_multiple_text(1.0)))))


# DISPATCH: "gut-journey": ("ks3-gut-block", ' data-instrument data-gutblock data-stage-done="0"'),
#
# and in `ACTIVITY_KIND_FN`, beside the other B3 rows:
#     "gut-journey":            r_gut_journey,
#
# Place `r_gut_journey` beside `r_clinic_cases`. Needs `e`, `t` and `rich`.
#
# ⚠️ THE THREE TILE LABELS AND THE NOTE LABEL ARE AUTHORED, not literals here.
# They are student-facing copy ("Molecules broken here", "Worth knowing:") and
# the same argument that keeps a reveal's sentences out of the engine keeps
# these out of it: a label that lives in Python cannot be corrected by the
# person who owns the science.


def r_gut_journey(a, act_id):
    """⊕ b3-05 `#s-journey` — seven stops, and a time chart that argues.

    ⚖️ THE CHART IS THE ARGUMENT, NOT A DECORATION, and it is why this is not
    `job-sort`, `verdict-cards` or the board. Those are runs of judgements;
    this is one journey with a quantity attached to each leg, and the quantity
    contradicts the intuition — the stomach, which every student names first,
    holds the meal about four hours, and the small intestine holds it sixteen.
    A tabbed panel set with no chart under it would teach the seven organs and
    lose the only thing the lesson is built to overturn.

    ⚖️ EVERY BAR COMES OUT OF `hours`, AT BUILD TIME. The widths are a pure
    function of the authored numbers against the longest of them, so the bar
    and the printed figure beside it cannot disagree — Design's page computes
    the width in one place and the printed string in another, from the same
    field, which is two chances for one number. Nothing in the wiring builds a
    width; the runtime moves the HIGHLIGHT and nothing else.

    ⚠️ `chart_name` AND `chart_hours` ARE AUTHORED, and Design derives both.
    Its chart name is `label.split(',')[0]` — which turns "Pancreas, liver,
    gall bladder" into "Pancreas" and would silently truncate any future stop
    whose label carries a comma for a different reason. Its hours string is a
    three-branch expression (`0 → '—'`, `<1 → '<1 h'`, else `n + ' h'`), which
    is a sentence about the data assembled in JS. Both are strings a student
    reads; both are authored once, here, where the science owner can see them.

    ⚠️ INK-DARK. `.ks3-dark p` is (0,1,1) and beats a bare instrument class at
    (0,1,0), so every colour rule in the stylesheet is scoped `.ks3-dark …`.
    The tiles are what would visibly break: three labels and three values in
    one undifferentiated on-dark body colour is a panel that has lost its
    structure, and it looks tidy.

    Emit-all-show-one: seven stop panels are in the document and one is shown.
    Going back to a stop finds it exactly as it was, no state lives anywhere
    but the DOM, and none of the fourteen authored sentences — several of which
    carry em dashes, a right single quote and a superscript ² — is ever rebuilt
    in JS from an attribute.
    """
    stops = a.get("stops") or []
    if len(stops) < 2:
        raise ValueError(
            "gut-journey %r declares %d stop(s). The block is a journey and "
            "one stop is a destination." % (act_id, len(stops)))

    tiles = a.get("tile_labels") or {}
    for key in ("time", "breaks", "absorbs"):
        if not tiles.get(key):
            raise ValueError(
                "gut-journey %r tile_labels is missing %r. All three tiles are "
                "drawn on every stop and an unlabelled one renders as a bare "
                "value with nothing saying what it is." % (act_id, key))

    chart = a.get("chart") or {}
    for key in ("label", "close"):
        if not chart.get(key):
            raise ValueError(
                "gut-journey %r chart is missing %r. Without the closing line "
                "the chart is seven bars and no argument." % (act_id, key))

    for s in stops:
        missing = [k for k in ("id", "label", "name", "kind", "time", "breaks",
                               "absorbs", "what", "note", "chart_name",
                               "chart_hours")
                   if not s.get(k)]
        if missing:
            raise ValueError(
                "gut-journey %r stop %r is missing %s. Every one is drawn, and "
                "an empty one renders as a gap in the panel."
                % (act_id, s.get("id"), ", ".join(missing)))
        if "hours" not in s:
            raise ValueError(
                "gut-journey %r stop %r declares no `hours`. The bar widths "
                "are derived from it; a stop with none has no place on the "
                "chart the block is built around." % (act_id, s["id"]))

    # ⚖️ ONE scale for all seven, taken from the data rather than authored, so
    # a corrected transit time re-scales the whole chart in one edit.
    longest = max(float(s["hours"]) for s in stops) or 1.0

    tabs = "".join(
        '<li><button type="button" class="ks3-gut-tab" data-stop="%s" '
        'aria-pressed="%s">'
        '<span class="ks3-gut-tabnum">%s</span>'
        '<span class="ks3-gut-tablabel">%s</span></button></li>'
        % (e(s["id"]), "true" if i == 0 else "false",
           t("%02d" % (i + 1)), t(s["label"]))
        for i, s in enumerate(stops))

    panels = []
    for i, s in enumerate(stops):
        cells = "".join(
            '<div class="ks3-gut-tile" data-tile="%s">'
            '<p class="ks3-gut-tilelabel">%s</p>'
            '<p class="ks3-gut-tilevalue">%s</p></div>'
            % (key, t(tiles[key]), t(s[val]))
            for key, val in (("time", "time"), ("breaks", "breaks"),
                             ("absorbs", "absorbs")))
        panels.append(
            '<div class="ks3-gut-stop" data-stop="%s"%s>'
            '<div class="ks3-gut-stophead" role="status">'
            '<p class="ks3-gut-name">%s</p>'
            '<p class="ks3-gut-kind">%s</p></div>'
            '<p class="ks3-gut-what">%s</p>'
            '<div class="ks3-gut-tiles">%s</div>'
            '<p class="ks3-gut-note"><strong>%s</strong> %s</p></div>'
            % (e(s["id"]), "" if i == 0 else " hidden",
               t(s["name"]), t(s["kind"]), rich(s["what"]), cells,
               t(a.get("note_label") or "Worth knowing:"), rich(s["note"])))

    rows = "".join(
        '<li class="ks3-gut-row" data-stop="%s"%s>'
        '<span class="ks3-gut-rowname">%s</span>'
        '<span class="ks3-gut-track">'
        '<span class="ks3-gut-bar" style="width:%s%%"></span></span>'
        '<span class="ks3-gut-rowhours">%s</span></li>'
        % (e(s["id"]), ' data-lit="1"' if i == 0 else "",
           t(s["chart_name"]),
           ("%.1f" % (float(s["hours"]) / longest * 100)),
           t(s["chart_hours"]))
        for i, s in enumerate(stops))

    return ('<div class="ks3-gut" data-gut data-total="%d">'
            '<ol class="ks3-gut-tabs">%s</ol>'
            '<div class="ks3-gut-stops">%s</div>'
            '<div class="ks3-gut-chart">'
            '<p class="ks3-gut-chartlabel">%s</p>'
            '<ul class="ks3-gut-rows">%s</ul>'
            '<p class="ks3-gut-chartclose">%s</p></div></div>'
            % (len(stops), tabs, "".join(panels),
               t(chart["label"]), rows, rich(chart["close"])))


# DISPATCH: "job-switch": ("ks3-jobsw-block", ' data-instrument data-jobswblock data-stage-done="0"'),
#
# and in ACTIVITY_KIND_FN, beside the other B3 rows:
#     "job-switch":             r_job_switch,
#
# Place `r_job_switch` in the B3 group, after `r_fold_builder`. Needs `e`, `t`,
# `rich`.
#
# ⚠️ THIS RENDERER DOES NOT CONSUME `options` OR `reveal`. Its controls are
# five state toggles, not answer buttons; the activity authors neither key, so
# `_kinds_consuming()` correctly leaves both generic branches off.
#
# ── WHY THIS IS NOT A WIDENING OF `system-switch` OR `job-sort` ──────────
#
# NOTES-B3 §3.6 describes it as "the B2 `system-switch` shape with five rows
# and no prediction gate", and that reading was tested against both shipped
# components before a new kind was written. It does not hold, on four measured
# counts, and the fourth is on its own decisive:
#
#   1. `system-switch` is TABBED — one panel visible, chosen by
#      `.ks3-switch-tab`. Here all five rows are on screen at once, because
#      the payoff is a claim about all five TOGETHER and a student cannot see
#      five simultaneous states through a tab strip.
#   2. `system-switch` GATES on a prediction: `wireSwitch` leaves the switch
#      button `disabled` until an option in that panel is pressed. With no
#      options authored, `r_system_switch` still emits `.ks3-switch-predict`
#      with an empty `<ul class="ks3-options">` and the button stays disabled
#      for ever — a dead control, not a narrower version of a live one.
#   3. `system-switch` reveals a LEVELLED CHAIN (`chain[]`, `.ks3-switch-chip`
#      keyed on "Cell"/"Tissue"/"Organ"/"Organism"). B3 job 3 is "harmful
#      species have nowhere to settle", which is an ecological consequence and
#      sits at no level of organisation at all. `show_levels: False` collapses
#      the chip and still demands the chain.
#   4. ⚖️ THE STATE MODEL IS DIFFERENT, and this is the one that settles it.
#      `wireSwitch` and `wireJobSort` are both ONE-WAY and CUMULATIVE — they
#      count panels that have EVER been opened, and `close_all` fires on that
#      count. This block's summary panel is a claim about the configuration
#      the student is looking at RIGHT NOW ("You have just built the germ-free
#      mouse"), so switching a job back on has to take it away again. A
#      component that counts what has happened cannot express a component that
#      reports what is true.
#
# And a fifth, which is about blast radius rather than shape: `system-switch`
# is a LIGHT `.ks3-block` and every `.ks3-switch-*` text rule in
# shared/ks3.css is written for ink on cream. This instrument is ink-dark.
# Widening would mean re-scoping that whole rule set past `.ks3-dark p`, which
# moves b2-01 — a page Mide has already approved — to serve a page he has not
# seen.
#
# `job-sort` was never close: its control is a choice among CATEGORIES with a
# per-row answer, and this block has no answer to give.


def r_job_switch(a, act_id):
    """⊕ b3-08 `#s-jobs` — take one job away and see what breaks.

    ⚖️ THE PAYOFF IS THE WHOLE BLOCK. Five jobs switched off at once IS the
    germ-free mouse from the hook, and the summary panel says so in those
    words. Every other beat here — the five rows, the five consequences, the
    counter — exists to make that one sentence land on a configuration the
    student built themselves rather than on a fact they were told.

    ⚠️ THE GROUND INVERTS, and it is the opposite way round from
    `fold-builder` on the lesson before. There, a level that is ON lights up,
    because the student is building something. Here a job that is STILL BEING
    DONE sits on the panel and a job that has been switched off falls back to
    the block's bare ink with an alert rule round it — the row visibly stops
    being a working part. Two instruments, one control, opposite directions,
    and the direction is the family: b3-07 builds a model up, b3-08 breaks a
    system down.

    ⚠️ NOTHING MARKS. There is no right number of jobs to switch off and no
    `answer_index` to check. The five toggles are `aria-pressed` toggle
    buttons and are deliberately not `.ks3-option`.

    ⚠️ INK-DARK, and the consequence paragraph is CREAM INSIDE IT — the one
    place on this page where ink type sits on the page ground inside an
    ink-dark block. `.ks3-dark p` is (0,1,1) and would paint it
    `--ks3-on-dark-body` #E7DECE on `--ks3-ground` #FBF3E6, which is a 1.1:1
    sentence: present, correct, and unreadable. Every text rule in the
    stylesheet is scoped to at least (0,2,0), and the parity fragment's first
    row is that assertion.

    Emit-both-show-one: all five consequences are in the document, hidden, and
    `wireJobSwitch` unhides them. No authored sentence is rebuilt in JS.
    """
    jobs = a.get("jobs") or []
    if len(jobs) < 2:
        raise ValueError(
            "job-switch %r declares %d job(s). The block's argument is that "
            "the losses ADD UP to one animal, and one loss is not an "
            "accumulation." % (act_id, len(jobs)))
    for j in jobs:
        for key in ("id", "tag", "name", "what", "without"):
            if not j.get(key):
                raise ValueError(
                    "job-switch %r job %r is missing %r. `without` is the "
                    "half that teaches — a job with no stated consequence is "
                    "a label, and the whole method here is switch it off and "
                    "follow what breaks."
                    % (act_id, j.get("id") or j.get("name"), key))

    labels = a.get("labels") or {}
    on_label = labels.get("on")
    off_label = labels.get("off")
    without_label = labels.get("without")
    if not on_label or not off_label:
        raise ValueError(
            "job-switch %r needs `labels.on` and `labels.off` — the button "
            "face is the only thing that says what pressing it will do."
            % act_id)

    # ⚖️ REQUIRED, not defaulted. The summary is what the five rows are for
    # (NOTES-B3 §3.6: "the payoff is the all-five-off summary panel"), and an
    # instrument that could quietly render without it would be five facts and
    # no conclusion.
    summary = a.get("all_off") or {}
    for key in ("tag", "headline", "body"):
        if not summary.get(key):
            raise ValueError(
                "job-switch %r is missing `all_off.%s`. Switching every job "
                "off is the moment the lesson exists for and it may not "
                "arrive silently." % (act_id, key))

    rows = []
    for j in jobs:
        rows.append(
            '<li class="ks3-jobsw-job" data-job="%s" data-off="0">'
            '<div class="ks3-jobsw-main">'
            '<div class="ks3-jobsw-what">'
            '<p class="ks3-jobsw-tag">%s</p>'
            '<p class="ks3-jobsw-name">%s</p>'
            '<p class="ks3-jobsw-does">%s</p></div>'
            '<button type="button" class="ks3-jobsw-toggle" data-jobsw-toggle '
            'aria-pressed="false" data-label-on="%s" data-label-off="%s">%s'
            '</button></div>'
            '<p class="ks3-jobsw-without" hidden data-reveal>'
            '%s%s</p></li>'
            % (e(j["id"]), t(j["tag"]), t(j["name"]), rich(j["what"]),
               e(on_label), e(off_label), t(on_label),
               ('<strong>%s</strong> ' % t(without_label))
               if without_label else "",
               rich(j["without"])))

    return ('<div class="ks3-jobsw" data-jobsw data-total="%d">'
            '<ul class="ks3-jobsw-list" role="list">%s</ul>'
            '<div class="ks3-jobsw-all" hidden data-jobsw-all>'
            '<p class="ks3-jobsw-alltag">%s</p>'
            '<p class="ks3-jobsw-allhead">%s</p>'
            '<p class="ks3-jobsw-allbody">%s</p></div></div>'
            % (len(jobs), "".join(rows), t(summary["tag"]),
               t(summary["headline"]), rich(summary["body"])))


# DISPATCH: "person-ledger": ("ks3-ledger-block", ' data-instrument data-ledgerblock data-stage-done="0"'),
#
# and in ACTIVITY_KIND_FN, beside the other B3 rows:
#     "person-ledger":          r_person_ledger,
#
# Place `r_person_ledger` after `r_test_bench` in the B3 group. Needs `e`, `t`,
# `rich`.
#
# ⚠️ THIS RENDERER CONSUMES NEITHER `options` NOR `reveal`. The block has no
# commitment to make: it is a ledger, and its argument is made by the student
# moving the person under a plate they have already built.


def r_person_ledger(a, act_id):
    """⊕ b3-03 `#s-ledger` — the requirement is a property of the PERSON.

    ⚖️ THE PERSON IS A CONTROL, NOT A CONSTANT, and that is the whole
    instrument. NOTES-B3 §2 says it in one line: *requirement is a property of
    the person, so the person is a control.* The plate is built once and then
    the person is changed underneath it, and the same food turns from a
    shortfall into a surplus with nothing about the food having moved. A ledger
    with one fixed eater would be a calculator.

    ⚖️ THE MATCH PANEL'S COPY IS THE EXPERIMENT. It appears only within the
    tolerance and it tells the student to switch person **without changing the
    food** — NOTES-B3 §3.3 flags that instruction as the thing that must not be
    lost, because without it a student who lands on a match reads it as having
    finished. `match.why` is required and this renderer raises without it.

    ⚖️ MRB-232 — THIS BLOCK STAYS ON B3'S SIDE OF THE SPLIT. It reports an
    intake, a requirement and the gap between them, all in kJ. It does not
    teach what a joule is, it derives nothing from power and time, and it
    performs no unit conversion: that clause of `KS3.B.NUT.02` belongs to
    Physics P2 and is reached from this lesson by a `references` edge, never by
    prose and never by a control in here. A future pass that adds a kJ↔kcal
    toggle or an energy-transfer readout to this instrument has moved the seam.

    ⚠️ R3 — NOTHING MARKS, AND NOTHING HERE IS AN ANSWER. Twelve food buttons,
    five person tabs and a clear. No `.ks3-option`, no correct plate, no score.
    The bar changes colour at the tolerance because it is a MEASUREMENT
    readout — short, matched, over — and the panel beside it says in words that
    a match is not an achievement but the start of the experiment.

    ⚠️ ON INK. `.ks3-dark p` is (0,1,1); the match panel is CREAM inside the
    ink block and its three paragraphs are the ones that would silently lose.
    Every text rule in the stylesheet is scoped `.ks3-dark …`.

    Every authored sentence is emitted into the document and switched by
    hiding: the five names, the five requirement lines, the five explanations
    and the five match headlines. The only strings assembled at runtime are the
    three that quote a live NUMBER — the total line, the balance line and the
    portion count — and each is one authored template filled with digits, the
    same mechanism `_head_counter` already uses for every counter in the key
    stage.
    """
    people = a.get("people") or []
    if len(people) < 2:
        raise ValueError(
            "person-ledger %r declares %d person(s). The block's argument is "
            "that the same plate means different things to different bodies, "
            "and one body cannot make it." % (act_id, len(people)))
    for p in people:
        for key in ("id", "label", "name", "lower", "why"):
            if not p.get(key):
                raise ValueError(
                    "person-ledger %r person %r is missing %r. `lower` is the "
                    "in-sentence form (“That day matches an Olympic rower in "
                    "training.”); lower-casing `name` at runtime would strip "
                    "the capital from Olympic."
                    % (act_id, p.get("id"), key))
        if not isinstance(p.get("need"), int) or p["need"] <= 0:
            raise ValueError(
                "person-ledger %r person %r has need %r; it is a whole number "
                "of kilojoules per day." % (act_id, p["id"], p.get("need")))

    foods = a.get("foods") or []
    if len(foods) < 2:
        raise ValueError("person-ledger %r declares %d food(s)." % (act_id, len(foods)))
    for f in foods:
        if not f.get("id") or not f.get("name") or not f.get("kj_label"):
            raise ValueError(
                "person-ledger %r food %r needs `id`, `name` and `kj_label`. "
                "`kj_label` is authored rather than composed because the "
                "zero-energy row reads “0 kJ” and every other row reads "
                "“780 kJ each” — a single template would print “0 kJ each”, "
                "which claims a portion size for a glass of water."
                % (act_id, f.get("id")))
        if not isinstance(f.get("kj"), int) or f["kj"] < 0:
            raise ValueError(
                "person-ledger %r food %r has kj %r; it is a whole number of "
                "kilojoules per portion." % (act_id, f["id"], f.get("kj")))

    balance = a.get("balance") or {}
    missing = sorted({"empty", "matched", "surplus", "short"} - set(balance))
    if missing:
        raise ValueError(
            "person-ledger %r declares no %s balance line. All four states are "
            "reachable from the controls, and a state with no sentence is a "
            "readout that goes blank." % (act_id, ", ".join(missing)))
    match = a.get("match") or {}
    if not (match.get("head") and match.get("why")):
        raise ValueError(
            "person-ledger %r declares no match panel. Its copy is the "
            "experiment — *switch person without changing the food* — and "
            "without it a student who lands on a match reads it as having "
            "finished." % act_id)

    def grouped(n):
        """9500 → 9,500. A NUMBER format, applied to no authored text."""
        return "{:,}".format(int(n))

    first = people[0]
    for p in people:
        if p["id"] == a.get("start_person"):
            first = p
            break

    tabs = "".join(
        '<button type="button" class="ks3-ledger-tab" data-person="%s" '
        'data-need="%d" aria-pressed="%s">%s</button>'
        % (e(p["id"]), p["need"], "true" if p is first else "false",
           t(p["label"]))
        for p in people)

    need_fmt = a.get("need_format") or "Needs {need} kJ / day"

    def switched(cls, attr, value_of):
        return "".join(
            '<span class="%s" data-%s="%s"%s>%s</span>'
            % (cls, attr, e(p["id"]), "" if p is first else " hidden",
               value_of(p))
            for p in people)

    names = switched("ks3-ledger-nameval", "pname", lambda p: t(p["name"]))
    needs = switched("ks3-ledger-needval", "pneed",
                     lambda p: t(need_fmt.replace("{need}", grouped(p["need"]))))
    whys = switched("ks3-ledger-whyval", "pwhy", lambda p: rich(p["why"]))

    food_html = "".join(
        '<li><button type="button" class="ks3-ledger-food" data-food="%s" '
        'data-kj="%d" data-count="0">'
        '<span class="ks3-ledger-foodrow">'
        '<span class="ks3-ledger-foodname">%s</span>'
        '<span class="ks3-ledger-foodcount" data-count-label></span></span>'
        '<span class="ks3-ledger-foodkj">%s</span></button></li>'
        % (e(f["id"]), f["kj"], t(f["name"]), t(f["kj_label"]))
        for f in foods)

    heads = "".join(
        '<p class="ks3-ledger-mhead" data-mhead="%s" hidden>%s</p>'
        % (e(p["id"]), t(match["head"].replace("{person}", p["lower"])))
        for p in people)

    portions = a.get("portions") or {}
    total_fmt = a.get("total_format") or "{total} kJ of {need} kJ"

    # ⚠️ The four balance sentences and the two portion sentences ride as
    # attributes, which is the ONE place this instrument does not emit its text
    # as text. They have to: each quotes a number that does not exist until the
    # student has built a plate, so there is no finished string to emit. This is
    # `_head_counter`'s own mechanism — `data-format`, `data-zero`, `data-off`,
    # `data-on` — and it is safe for exactly the reason that is: the strings
    # carry no markup, so `textContent` loses nothing, and `e()` is the
    # attribute escaper. A sentence that carries `<em>` may never travel this
    # way, and none of these does.
    return ('<div class="ks3-ledger" data-ledger data-person="%s" '
            'data-tolerance="%d" data-max="%d" data-count-format="%s">'
            '<div class="ks3-ledger-who">'
            '<p class="ks3-ledger-grouplabel">%s</p>'
            '<div class="ks3-ledger-tabs">%s</div></div>'
            '<div class="ks3-ledger-panel">'
            '<div class="ks3-ledger-head">'
            '<p class="ks3-ledger-name">%s</p>'
            '<p class="ks3-ledger-need">%s</p></div>'
            '<p class="ks3-ledger-why">%s</p>'
            '<div class="ks3-ledger-bar">'
            '<span class="ks3-ledger-fill" data-bar data-state="short"></span>'
            '</div>'
            '<div class="ks3-ledger-figures">'
            '<p class="ks3-ledger-total" data-total data-format="%s">%s</p>'
            '<p class="ks3-ledger-balance" data-balance role="status" '
            'data-empty="%s" data-matched="%s" data-surplus="%s" '
            'data-short="%s">%s</p></div></div>'
            '<p class="ks3-ledger-foodlabel">%s</p>'
            '<ul class="ks3-ledger-foods" role="list">%s</ul>'
            '<div class="ks3-ledger-foot">'
            '<button type="button" class="ks3-reveal-btn ks3-ledger-clear" '
            'data-ledger-clear>%s</button>'
            '<span class="ks3-ledger-portions" data-portions data-empty="%s" '
            'data-format="%s">%s</span></div>'
            '<div class="ks3-ledger-match" hidden data-match>'
            '<p class="ks3-ledger-mlabel">%s</p>%s'
            '<p class="ks3-ledger-mwhy">%s</p></div></div>'
            % (e(first["id"]), int(a.get("tolerance") or 5),
               int(a.get("max_per_food") or 6),
               e(a.get("count_format") or "×{n}"),
               t(a.get("group_label") or "Who is eating"), tabs,
               names, needs, whys,
               e(total_fmt),
               t(total_fmt.replace("{total}", "0")
                 .replace("{need}", grouped(first["need"]))),
               e(balance["empty"]), e(balance["matched"]),
               e(balance["surplus"]), e(balance["short"]),
               t(balance["empty"]),
               t(a.get("food_label") or ""), food_html,
               t(a.get("clear_label") or "Empty the day"),
               e(portions.get("empty") or ""),
               e(portions.get("some") or "{n} portions, {total} kJ"),
               t(portions.get("empty") or ""),
               t(match.get("eyebrow") or ""), heads, rich(match["why"])))


# DISPATCH: "test-bench": ("ks3-tbench-block", ' data-instrument data-tbenchblock data-stage-done="0"'),
#
# and in ACTIVITY_KIND_FN, beside the other B3 rows:
#     "test-bench":             r_test_bench,
#
# Place `r_test_bench` after `r_band_commit` in the B3 group. Needs `e`, `t`,
# `rich`, `r_activity_options`.
#
# ⚠️ THIS RENDERER DOES NOT CONSUME the activity's own `options` key, because
# the activity does not author one — the two prediction buttons live under
# `predict.options`, where they belong to the gate rather than to the block.
# `_kinds_consuming()` will therefore NOT list this kind, which is correct:
# there is no top-level `options` for the generic branch to draw twice.


def r_test_bench(a, act_id):
    """⊕ b3-02 `#s-bench` — five foods, four tests, twenty honest results.

    ⚖️ PREDICTING **RUNS** THE TEST. There is no separate run button, and that
    is the mechanism rather than a saving: the commitment IS the action, so a
    student cannot watch the colour first and decide afterwards what they
    thought. Twenty combinations, each gated by its own two-option prediction.

    ⚖️ EVERY RESULT ENDS IN A CLAIM LINE, and for a negative it is the HEDGED
    wording. This is the whole lesson — *“No starch was detected in potato
    under these conditions.” Not “there is none”.* — and the four deliberate
    false negatives in Design's payload (potato/Biuret at 2% protein, apple
    juice/Biuret at 0.3%, and the two that are true negatives and say so) only
    teach anything if the sentence a student is licensed to write is printed
    under every one of them. `claims` is REQUIRED and this renderer raises
    without both halves.

    ⚠️ THE TUBE COLOUR IS REAL AND IS NOT A TOKEN. NOTES-B3 §3.2: the tube is
    the only colour-bearing element in the unit and the colours are the
    reagents' own — Benedict's blue #2E63B8 to brick red #B03A16. They are
    authored as literal hex on the test, never as `var(--ks3-accent)`, because
    an accent-tinted tube would be teaching a colour change that does not
    happen. They reach the page as an attribute on the test tab and are set on
    the tube's fill; that is a COLOUR travelling through an attribute, not a
    sentence.

    ⚠️ EVERYTHING A STUDENT READS IS COMPOSED HERE, AT BUILD TIME. The twenty
    prediction prompts and the twenty claim lines are filled from two authored
    templates and the foods' and tests' own names, in Python, and emitted into
    the document hidden. The browser only ever unhides one of them. Design's
    page assembles all forty in `renderVals()` with `+`, `.toLowerCase()` and
    `.split(' (')[0]`, which is how "Potato" becomes "potato" and "reducing
    sugar (glucose, fructose)" becomes "reducing sugar" — three string
    transformations applied to authored science in the browser. `lower` and
    `detects` are authored instead, so nothing is transformed anywhere.

    ⚠️ ON INK. `.ks3-dark p` is (0,1,1); every text rule in the stylesheet is
    scoped `.ks3-dark …`, and the result panel is CREAM inside the ink block,
    so its four paragraphs are the ones that would silently lose. See the CSS.
    """
    tests = a.get("tests") or []
    foods = a.get("foods") or []
    if len(tests) < 2 or len(foods) < 2:
        raise ValueError(
            "test-bench %r declares %d test(s) and %d food(s). The block's "
            "argument is that one test answers one question, and it cannot be "
            "made with a single row or a single column."
            % (act_id, len(tests), len(foods)))

    for tst in tests:
        for key in ("id", "label", "detects", "detects_full", "method"):
            if not tst.get(key):
                raise ValueError(
                    "test-bench %r test %r is missing %r. `detects` is the "
                    "short form the prompt and the claim line use "
                    "(“reducing sugar”) and `detects_full` is the one the "
                    "method panel prints (“reducing sugar (glucose, "
                    "fructose)”); deriving one from the other would put a "
                    "`.split()` between a student and an authored phrase."
                    % (act_id, tst.get("id"), key))
        for out in ("pos", "neg"):
            spec = tst.get(out) or {}
            for key in ("colour", "name", "headline"):
                if not spec.get(key):
                    raise ValueError(
                        "test-bench %r test %r %s.%s is missing. `name` is the "
                        "tube's own state line and `headline` is the finished "
                        "sentence over the result — both are authored, "
                        "because capitalising the first letter of a reagent "
                        "colour in the browser is a transformation of science "
                        "copy." % (act_id, tst["id"], out, key))

    test_ids = [tst["id"] for tst in tests]
    for f in foods:
        for key in ("id", "label", "lower"):
            if not f.get(key):
                raise ValueError(
                    "test-bench %r food %r is missing %r. `lower` is the form "
                    "the sentence uses (“…in apple juice…”); lower-casing "
                    "`label` at runtime would also lower-case a proper noun "
                    "the moment one is added." % (act_id, f.get("id"), key))
        has, notes = f.get("has") or {}, f.get("notes") or {}
        for tid in test_ids:
            if tid not in has:
                raise ValueError(
                    "test-bench %r: food %r declares no result for test %r. "
                    "Every combination is reachable from the tabs, so a "
                    "missing one is a tube that runs and reports nothing."
                    % (act_id, f["id"], tid))
            if not notes.get(tid):
                raise ValueError(
                    "test-bench %r: food %r has no note for test %r. The note "
                    "is where the honest reading of that result lives — four "
                    "of these are deliberate false negatives and the note is "
                    "the only thing that says so." % (act_id, f["id"], tid))

    predict = a.get("predict") or {}
    if not predict.get("prompt") or len(predict.get("options") or []) < 2:
        raise ValueError(
            "test-bench %r declares no prediction gate. Predicting is what "
            "RUNS the test in this block; without it the tube is a lookup "
            "table." % act_id)
    claims = a.get("claims") or {}
    if not (claims.get("positive") and claims.get("negative")):
        raise ValueError(
            "test-bench %r declares no %s claim line. The claim line is the "
            "lesson." % (act_id,
                         "positive" if not claims.get("positive") else "negative"))
    verdicts = a.get("verdicts") or {}
    if not (verdicts.get("hit") and verdicts.get("miss")):
        raise ValueError("test-bench %r needs both `verdicts` branches." % act_id)

    first_food, first_test = foods[0], tests[0]

    def fill(template, food, tst):
        """One authored template, twenty finished sentences, at BUILD time.

        `{food_lower}` is replaced first: `{food}` is a prefix of it, so the
        other order would leave a stray `_lower` in every negative claim line.
        """
        return (template
                .replace("{food_lower}", food["lower"])
                .replace("{food}", food["label"])
                .replace("{test}", tst["label"])
                .replace("{detects}", tst["detects"]))

    # ── the two tab groups ───────────────────────────────────────────────
    groups = a.get("groups") or {}
    food_tabs = "".join(
        '<button type="button" class="ks3-tbench-tab" data-food="%s" '
        'aria-pressed="%s">%s</button>'
        % (e(f["id"]), "true" if f is first_food else "false", t(f["label"]))
        for f in foods)
    # ⚠️ The two reagent colours ride on the TEST TAB, because the tube shows
    # the negative colour of the selected test before anything is run — so the
    # colours have to be reachable from the selection, not only from a result
    # panel that does not exist yet.
    test_tabs = "".join(
        '<button type="button" class="ks3-tbench-tab" data-test="%s" '
        'data-neg="%s" data-pos="%s" aria-pressed="%s">%s</button>'
        % (e(tst["id"]), e(tst["neg"]["colour"]), e(tst["pos"]["colour"]),
           "true" if tst is first_test else "false", t(tst["label"]))
        for tst in tests)

    # ── the tube ─────────────────────────────────────────────────────────
    # The label is TWO switched spans with a literal join between them, not a
    # string built in the browser: "Potato" and "Iodine" are both authored and
    # both already in the document, so there is nothing to concatenate.
    tube = a.get("tube") or {}
    lfoods = "".join(
        '<span class="ks3-tbench-lfood" data-lfood="%s"%s>%s</span>'
        % (e(f["id"]), "" if f is first_food else " hidden", t(f["label"]))
        for f in foods)
    ltests = "".join(
        '<span class="ks3-tbench-ltest" data-ltest="%s"%s>%s</span>'
        % (e(tst["id"]), "" if tst is first_test else " hidden", t(tst["label"]))
        for tst in tests)
    states = ['<span data-sname="rest">%s</span>' % t(tube.get("not_run") or "")]
    for tst in tests:
        for out in ("pos", "neg"):
            states.append('<span data-sname="%s:%s" hidden>%s</span>'
                          % (e(tst["id"]), out, t(tst[out]["name"])))

    # ── the method card ──────────────────────────────────────────────────
    methods = "".join(
        '<p class="ks3-tbench-method" data-method="%s"%s>%s</p>'
        '<p class="ks3-tbench-detects" data-detects="%s"%s>%s</p>'
        % (e(tst["id"]), "" if tst is first_test else " hidden", t(tst["method"]),
           e(tst["id"]), "" if tst is first_test else " hidden",
           t((a.get("detects_label") or "{detects}")
             .replace("{detects}", tst["detects_full"])))
        for tst in tests)

    # ── twenty prompts and twenty result panels ──────────────────────────
    prompts, results = [], []
    for f in foods:
        for tst in tests:
            key = "%s:%s" % (f["id"], tst["id"])
            cur = f is first_food and tst is first_test
            prompts.append(
                '<p class="ks3-commit ks3-tbench-prompt" data-prompt="%s"%s>%s</p>'
                % (e(key), "" if cur else " hidden",
                   t(fill(predict["prompt"], f, tst))))
            positive = bool(f["has"][tst["id"]])
            side = tst["pos"] if positive else tst["neg"]
            claim = fill(claims["positive"] if positive else claims["negative"],
                         f, tst)
            results.append(
                '<div class="ks3-tbench-result" data-result="%s" '
                'data-outcome="%s" data-colour="%s" hidden>'
                '<p class="ks3-tbench-verdict" data-verdict="hit" hidden>%s</p>'
                '<p class="ks3-tbench-verdict" data-verdict="miss" hidden>%s</p>'
                '<p class="ks3-tbench-head">%s</p>'
                '<p class="ks3-tbench-why">%s</p>'
                '<p class="ks3-tbench-claim"><strong>%s</strong> %s</p></div>'
                % (e(key), "pos" if positive else "neg", e(side["colour"]),
                   t(verdicts["hit"]), t(verdicts["miss"]),
                   t(side["headline"]), rich(f["notes"][tst["id"]]),
                   t(a.get("claim_label") or "What you may write down:"),
                   rich(claim)))

    return ('<div class="ks3-tbench" data-tbench data-food="%s" data-test="%s" '
            'data-target="%d">'
            '<div class="ks3-tbench-picks">'
            '<div class="ks3-tbench-group"><p class="ks3-tbench-grouplabel">%s</p>'
            '<div class="ks3-tbench-tabs">%s</div></div>'
            '<div class="ks3-tbench-group"><p class="ks3-tbench-grouplabel">%s</p>'
            '<div class="ks3-tbench-tabs">%s</div></div></div>'
            '<div class="ks3-tbench-readout">'
            '<div class="ks3-tbench-tubecard">'
            '<span class="ks3-tbench-tube" aria-hidden="true">'
            '<span class="ks3-tbench-fill" data-tube data-run="0" '
            'style="background:%s"></span></span>'
            '<div class="ks3-tbench-tubemeta">'
            '<p class="ks3-tbench-cap">%s</p>'
            '<p class="ks3-tbench-tubelabel">%s'
            '<span class="ks3-tbench-join" aria-hidden="true">%s</span>%s</p>'
            '<p class="ks3-tbench-state" data-state role="status">%s</p>'
            '</div></div>'
            '<div class="ks3-tbench-methodcard">'
            '<p class="ks3-tbench-cap">%s</p>%s</div></div>'
            '<div class="ks3-tbench-predict" data-predict>%s%s</div>'
            '<div class="ks3-tbench-results">%s</div></div>'
            % (e(first_food["id"]), e(first_test["id"]),
               int(a.get("rail_after") or 4),
               t(groups.get("food") or "Food"), food_tabs,
               t(groups.get("test") or "Test"), test_tabs,
               e(first_test["neg"]["colour"]),
               t(tube.get("caption") or "In the tube"),
               lfoods, t(tube.get("label_join") or " + "), ltests,
               "".join(states),
               t(a.get("method_label") or "Method"), methods,
               "".join(prompts), r_activity_options(predict["options"]),
               "".join(results)))
# renderers: ═══ END B3 ═══


# renderers: ═══ BEGIN B4 ═══
#
# Five lessons, five instruments, and every one of them on ink.
#
# ⚠️ THAT UNIFORMITY IS THE HAZARD, NOT A CONVENIENCE. `.ks3-dark p` is (0,1,1)
# and a bare instrument class is (0,1,0), so an unscoped colour rule LOSES —
# and because all five B4 practicals are `ks3-block ks3-dark ks3-practical`,
# that trap would bite all five lessons at once rather than one. Every colour
# rule these five hang on is scoped `.ks3-dark …` in `shared/ks3.css`, and the
# panels that invert to the CREAM ground inside the ink block (gas-compare's
# closing paragraph, bell-jar's chain, crossing-counter's note,
# fault-bench's reveal, two-process-ledger's verdict) are the ones that would
# silently lose: `.ks3-dark p` would paint #E7DECE on #FBF3E6 at about 1.2:1.
#
# ⚠️ NOTHING IN B4 ANIMATES AND NOTHING USES A TIMER. All five instruments are
# pure functions of their controls' state; the only motion in the unit is a CSS
# transition, and the stylesheet's reduced-motion block removes every one. There
# is no rAF loop in this unit to check `prefers-reduced-motion` inside.


def r_gas_compare(a, act_id):
    """⊕ b4-01 `#s-air` — four gases, a prediction on each, then both bags.

    ⚖️ THE NUMERAL IS NOT A CAPTION FOR THE BAR, IT IS THE CORRECTION TO IT.
    Carbon dioxide is 0.04% inhaled, and a bar drawn honestly at 0.04% of its
    track is zero pixels wide — so the bar is clamped to `min_bar_pct`, which
    on Design's payload makes it about thirty-seven times too wide. That clamp
    is the one dishonest pixel in the unit. It is survivable only because the
    figure sits beside the bar in every cell, which is why `in_label` and
    `out_label` are required and why this renderer will not compose them.

    ⚖️ `in_label` / `out_label` ARE AUTHORED, NOT FORMATTED FROM THE PERCENT.
    Water vapour's two cells read "variable, often low" and "saturated" —
    Design's deliberate refusal to give a percentage for a figure that has
    none. A template filling "{pct}%" would print "1%" there and invent a
    measurement. The percents drive the BARS and nothing else.

    ⚠️ THE PREDICTION IS NOT MARKED WHILE IT IS BEING MADE. Only the mastery
    ladder marks correctness (R3), so the three buttons per row take
    `aria-pressed` and no verdict class until the reveal opens. What happens at
    the reveal is not marking either: the row that predicted correctly keeps
    its panel and its border goes to alert, and the row that did not loses the
    panel. Design draws exactly that, and the count beside the button changes
    from "committed" to "predicted correctly" in the same instant.
    """
    gases = a.get("gases") or []
    if len(gases) < 2:
        raise ValueError(
            "gas-compare %r declares %d gas(es). The block is a comparison of "
            "two bags across the gases in them, and one row cannot make it."
            % (act_id, len(gases)))

    choices = a.get("choices") or []
    if len(choices) < 2:
        raise ValueError(
            "gas-compare %r declares %d choice(s). A prediction needs "
            "something to choose between." % (act_id, len(choices)))
    for c in choices:
        if not (c.get("id") and c.get("label")):
            raise ValueError(
                "gas-compare %r choice %r needs `id` and `label`."
                % (act_id, c.get("id")))
    choice_ids = [c["id"] for c in choices]

    for g in gases:
        for key in ("id", "name", "change", "in_label", "out_label", "verdict"):
            if not g.get(key):
                raise ValueError(
                    "gas-compare %r gas %r is missing %r. `in_label` and "
                    "`out_label` are the printed figures and are authored: "
                    "water vapour's read “variable, often low” and "
                    "“saturated”, and composing them from the "
                    "percentages would print a measurement Design refused to "
                    "give." % (act_id, g.get("id"), key))
        if g["change"] not in choice_ids:
            raise ValueError(
                "gas-compare %r gas %r predicts %r, which is not one of the "
                "offered choices %s. A row whose right answer is not on the "
                "buttons can never be predicted correctly, and the closing "
                "count would be wrong for every student."
                % (act_id, g["id"], g["change"], choice_ids))
        for key in ("in_pct", "out_pct"):
            v = g.get(key)
            if not isinstance(v, (int, float)) or isinstance(v, bool) or v < 0:
                raise ValueError(
                    "gas-compare %r gas %r has %s %r; it is the bar's width as "
                    "a percentage of its track and cannot be negative."
                    % (act_id, g["id"], key, v))

    count = a.get("count") or {}
    if not (count.get("committed") and count.get("scored")):
        raise ValueError(
            "gas-compare %r needs both `count.committed` and `count.scored`. "
            "The line beside the button says how many rows are committed "
            "before the reveal and how many were right after it — one "
            "string cannot do both, and a blank one is a readout that goes "
            "dark at the moment the block pays off." % act_id)

    table = a.get("table") or {}
    missing = sorted({"gas", "inhaled", "exhaled"} - set(table))
    if missing:
        raise ValueError(
            "gas-compare %r table is missing %s. The two data headings are "
            "also the per-cell captions on a narrow screen, where the columns "
            "stack and an uncaptioned figure is a number with nothing saying "
            "which bag it came from." % (act_id, ", ".join(missing)))

    for key in ("reveal_label", "close_lead", "close"):
        if not a.get(key):
            raise ValueError(
                "gas-compare %r declares no %r." % (act_id, key))

    min_bar = float(a.get("min_bar_pct") or 1.5)

    rows = "".join(
        '<li class="ks3-gas-row" data-gasrow="%s" data-change="%s">'
        '<p class="ks3-gas-rowname">%s</p>'
        '<div class="ks3-gas-choices">%s</div></li>'
        % (e(g["id"]), e(g["change"]), t(g["name"]),
           "".join(
               '<button type="button" class="ks3-gas-choice" data-gas="%s" '
               'data-choice="%s" aria-pressed="false">%s</button>'
               % (e(g["id"]), e(c["id"]), t(c["label"]))
               for c in choices))
        for g in gases)

    def cell(g, side):
        pct = float(g["in_pct"] if side == "in" else g["out_pct"])
        label = g["in_label"] if side == "in" else g["out_label"]
        cap = table["inhaled"] if side == "in" else table["exhaled"]
        return ('<div class="ks3-gas-cell" data-side="%s">'
                '<p class="ks3-gas-cap">%s</p>'
                '<p class="ks3-gas-num">%s</p>'
                '<span class="ks3-gas-track">'
                '<span class="ks3-gas-bar" style="width:%s%%"></span>'
                '</span></div>'
                % (side, t(cap), t(label), ("%.2f" % max(min_bar, pct))))

    body = "".join(
        '<div class="ks3-gas-grid ks3-gas-body" data-gasout="%s" data-band="%d">'
        '<div class="ks3-gas-name">'
        '<p class="ks3-gas-gname">%s</p>'
        '<p class="ks3-gas-verdict">%s</p></div>%s%s</div>'
        % (e(g["id"]), i % 2, t(g["name"]), t(g["verdict"]),
           cell(g, "in"), cell(g, "out"))
        for i, g in enumerate(gases))

    return ('<div class="ks3-gas" data-gas data-total="%d" '
            'data-committed="%s" data-scored="%s">'
            '<ul class="ks3-gas-rows" role="list">%s</ul>'
            '<div class="ks3-gas-foot">'
            '<button type="button" class="ks3-reveal-btn ks3-gas-open" '
            'data-gas-open disabled>%s</button>'
            '<span class="ks3-gas-count" data-gas-count role="status">%s</span>'
            '</div>'
            '<div class="ks3-gas-table" data-gas-table hidden>'
            '<div class="ks3-gas-grid ks3-gas-head">'
            '<p class="ks3-gas-hname">%s</p>'
            '<p class="ks3-gas-hcell">%s</p>'
            '<p class="ks3-gas-hcell" data-side="out">%s</p></div>%s</div>'
            '<p class="ks3-gas-close" data-gas-close hidden>'
            '<strong>%s</strong> %s</p></div>'
            % (len(gases), e(count["committed"]), e(count["scored"]), rows,
               t(a["reveal_label"]),
               t(count["committed"].replace("{n}", "0")
                 .replace("{total}", str(len(gases)))),
               t(table["gas"]), t(table["inhaled"]), t(table["exhaled"]), body,
               t(a["close_lead"]), rich(a["close"])))


def r_bell_jar(a, act_id):
    """⊕ b4-02 `#s-model` — the bell jar, and the chain that is the instrument.

    ⚖️ THE CHAIN IS THE INSTRUMENT, NOT THE PICTURE. NOTES-B4 §3.2 says it in
    one line and it decides the whole shape of this renderer: the jar drawing
    is a rectangle whose height scales and a circle that scales with it, and if
    that were the block, the block would be decoration. The chain's job is that
    its FIRST line is always the muscle and its LAST line is always the air —
    the exact order `#s-ladder` rung 1 then asks for. Rendering it as static
    text loses the lesson's central confrontation, so all three phases are
    authored in full and the live numbers are filled into them.

    ⚖️ THREE PHASES, ALL THREE AUTHORED, BECAUSE ALL THREE ARE REACHABLE. The
    slider passes through `rest` on its way anywhere, and Design writes a
    distinct four-line chain for it — "No net air movement in either
    direction." A missing phase is not a rare state, it is the state the
    instrument opens in.

    ⚠️ `{pressure}` IS SIGNED AND `{pressure_abs}` IS NOT, and the difference is
    a sentence's meaning. Design's `out` chain reads "rises to 0.18 kPa above
    atmospheric" from `Math.abs(pressure)`; its `in` chain reads "falls to
    -0.79 kPa below atmospheric" from the signed value — a double negative on
    the drawn page. Both placeholders exist here and the renderer takes no
    view: which one a sentence uses is a property of that sentence, and the
    sentence is the author's. See `docs/ks3/b4-inventory/PAYLOAD-SCHEMA.md` §2.

    ⚠️ `pressure_zero` MUST AGREE WITH `rest`. The phase a chain shows is
    decided by the slider against `rest`; the pressure printed inside that
    chain is decided by the slider against `pressure_zero`. Let them differ and
    there is a band of the slider that says "at rest between breaths" while
    printing a pressure difference, or says "breathing in" at 0.00 kPa. The
    renderer raises rather than shipping a model that disagrees with its own
    readout.
    """
    model = a.get("model") or {}
    for key in ("volume_base", "volume_span", "pressure_zero", "pressure_span"):
        v = model.get(key)
        if not isinstance(v, (int, float)) or isinstance(v, bool):
            raise ValueError(
                "bell-jar %r model.%s is %r. The four numbers are the model's "
                "physics and are authored, because they are the figures the "
                "chain quotes and the science owner has to be able to correct "
                "them without opening the generator."
                % (act_id, key, v))

    start = int(a.get("start", 20))
    rest = int(a.get("rest", 20))
    for name, v in (("start", start), ("rest", rest)):
        if not 0 <= v <= 100:
            raise ValueError(
                "bell-jar %r %s is %d; the slider runs 0–100."
                % (act_id, name, v))
    if abs(float(model["pressure_zero"]) * 100 - rest) > 1e-9:
        raise ValueError(
            "bell-jar %r has rest=%d but model.pressure_zero=%r (which is "
            "%.1f on the slider). The phase and the pressure would then "
            "disagree: there would be slider positions reading “at "
            "rest” with a pressure difference printed under them."
            % (act_id, rest, model["pressure_zero"],
               float(model["pressure_zero"]) * 100))

    readouts = a.get("readouts") or {}
    missing = sorted({"volume_label", "volume_format", "pressure_label",
                      "pressure_format", "outside_label", "outside_value",
                      "air_label"} - set(readouts))
    if missing:
        raise ValueError(
            "bell-jar %r readouts is missing %s. Four rows are drawn and every "
            "one of them is a claim: the outside pressure row is FIXED at "
            "atmospheric and is the reference the inside row is read against, "
            "so an unlabelled or absent one leaves the inside figure meaning "
            "nothing." % (act_id, ", ".join(missing)))

    for key in ("slider_label", "slider_aria", "jar_label", "readouts_label",
                "chain_label"):
        if not a.get(key):
            raise ValueError(
                "bell-jar %r declares no %r. `slider_aria` is the "
                "visually-hidden label on the range input and is the only "
                "thing a screen-reader user has to go on."
                % (act_id, key))

    presets = a.get("presets") or []
    if not presets:
        raise ValueError(
            "bell-jar %r declares no presets. Design draws two — breathe "
            "in and breathe out — and they are what make the two ends of "
            "the slider reachable in one press." % act_id)
    for p in presets:
        if not p.get("label"):
            raise ValueError(
                "bell-jar %r preset %r has no label." % (act_id, p.get("id")))
        v = p.get("value")
        if not isinstance(v, int) or isinstance(v, bool) or not 0 <= v <= 100:
            raise ValueError(
                "bell-jar %r preset %r has value %r; it is a slider position "
                "0–100." % (act_id, p.get("id"), v))

    phases = a.get("phases") or {}
    missing = sorted({"in", "out", "rest"} - set(phases))
    if missing:
        raise ValueError(
            "bell-jar %r declares no %s phase. The slider passes through all "
            "three and opens in one of them; a phase with no text is a chain "
            "that goes blank while the student is holding the control."
            % (act_id, ", ".join(missing)))
    for name in ("in", "out", "rest"):
        ph = phases[name] or {}
        for key in ("phase_label", "dia_label", "air", "note"):
            if not ph.get(key):
                raise ValueError(
                    "bell-jar %r phase %r is missing %r."
                    % (act_id, name, key))
        chain = ph.get("chain") or []
        if len(chain) != 4:
            raise ValueError(
                "bell-jar %r phase %r declares %d chain line(s), not 4. The "
                "four steps are muscle → volume → pressure → "
                "air, and the count is the argument: drop one and the "
                "remaining three no longer say that the air is last."
                % (act_id, name, len(chain)))

    def figures(dia):
        """Volume, signed pressure and its magnitude at a slider position."""
        f = dia / 100.0
        vol = float(model["volume_base"]) + f * float(model["volume_span"])
        pres = -(f - float(model["pressure_zero"])) * float(model["pressure_span"])
        return vol, pres

    def fill(tpl, dia):
        vol, pres = figures(dia)
        return (tpl.replace("{volume}", "%.1f" % vol)
                .replace("{pressure_abs}", "%.2f" % abs(pres))
                .replace("{pressure}", "%.2f" % pres))

    open_phase = "in" if start > rest else ("out" if start < rest else "rest")

    def switched(cls, attr, value_of):
        """Emit every authored variant, show the one the slider opens on."""
        return "".join(
            '<span class="%s" data-%s="%s"%s>%s</span>'
            % (cls, attr, name, "" if name == open_phase else " hidden",
               value_of(phases[name]))
            for name in ("in", "out", "rest"))

    chains = "".join(
        '<ol class="ks3-bell-chain" data-chain="%s"%s>%s</ol>'
        % (name, "" if name == open_phase else " hidden",
           "".join(
               '<li class="ks3-bell-step"%s>%s</li>'
               % ((' data-format="%s"' % e(line))
                  if ("{volume}" in line or "{pressure" in line) else "",
                  t(fill(line, start)))
               for line in phases[name]["chain"]))
        for name in ("in", "out", "rest"))

    notes = "".join(
        '<p class="ks3-bell-note" data-note="%s"%s>%s</p>'
        % (name, "" if name == open_phase else " hidden",
           rich(phases[name]["note"]))
        for name in ("in", "out", "rest"))

    preset_html = "".join(
        '<button type="button" class="ks3-reveal-btn ks3-bell-preset" '
        'data-preset="%d">%s</button>' % (p["value"], t(p["label"]))
        for p in presets)

    vol0, pres0 = figures(start)
    sid = "bell-" + str(act_id)

    return ('<div class="ks3-bell" data-bell data-rest="%d" data-vbase="%s" '
            'data-vspan="%s" data-pzero="%s" data-pspan="%s">'
            '<div class="ks3-bell-panels">'
            '<div class="ks3-bell-card">'
            '<p class="ks3-bell-cap">%s</p>'
            '<div class="ks3-bell-jar" aria-hidden="true">'
            '<span class="ks3-bell-chest" data-chest>'
            '<span class="ks3-bell-lung" data-lung></span></span></div>'
            '<p class="ks3-bell-phase" role="status">%s</p></div>'
            '<div class="ks3-bell-card">'
            '<p class="ks3-bell-cap">%s</p>'
            '<dl class="ks3-bell-reads">'
            '<div class="ks3-bell-read"><dt>%s</dt>'
            '<dd data-read="volume" data-format="%s">%s</dd></div>'
            '<div class="ks3-bell-read"><dt>%s</dt>'
            '<dd data-read="pressure" data-format="%s">%s</dd></div>'
            '<div class="ks3-bell-read"><dt>%s</dt><dd>%s</dd></div>'
            '<div class="ks3-bell-read"><dt>%s</dt><dd>%s</dd></div>'
            '</dl></div></div>'
            '<div class="ks3-bell-control">'
            '<div class="ks3-bell-controlhead">'
            '<p class="ks3-bell-cap">%s</p>'
            '<p class="ks3-bell-dia">%s</p></div>'
            '<label class="ks3-sr-only" for="%s">%s</label>'
            '<input class="ks3-b4slider ks3-bell-slider" type="range" id="%s" '
            'min="0" max="100" step="1" value="%d" data-bell-slider>'
            '<div class="ks3-bell-presets">%s</div></div>'
            '<div class="ks3-bell-chainpanel">'
            '<p class="ks3-bell-chainlabel">%s</p>%s%s</div></div>'
            % (rest, model["volume_base"], model["volume_span"],
               model["pressure_zero"], model["pressure_span"],
               t(a["jar_label"]),
               switched("ks3-bell-phaseval", "phase",
                        lambda ph: t(ph["phase_label"])),
               t(a["readouts_label"]),
               t(readouts["volume_label"]), e(readouts["volume_format"]),
               t(readouts["volume_format"].replace("{volume}", "%.1f" % vol0)),
               t(readouts["pressure_label"]), e(readouts["pressure_format"]),
               t(readouts["pressure_format"].replace(
                   "{pressure}", "%+.2f" % pres0)),
               t(readouts["outside_label"]), t(readouts["outside_value"]),
               t(readouts["air_label"]),
               switched("ks3-bell-airval", "air", lambda ph: t(ph["air"])),
               t(a["slider_label"]),
               switched("ks3-bell-diaval", "dia", lambda ph: t(ph["dia_label"])),
               e(sid), t(a["slider_aria"]), e(sid), start, preset_html,
               t(a["chain_label"]), chains, notes))


def r_crossing_counter(a, act_id):
    """⊕ b4-03 `#s-gradient` — four states, and neither bar ever reads zero.

    ⚖️ THE OUTWARD BAR IS THE LESSON. `PART-10`/`PART-11` have been confronted
    twice before this and survive because every picture a student has seen of
    diffusion shows movement one way. Here the outward count is on screen in
    all four states, including the one where both flows are stopped and the
    two counts are IDENTICAL — molecules still crossing, nothing settled,
    nothing finished, only the imbalance gone. A state whose outward count fell
    to zero would teach the belief this instrument exists to remove, so
    `blood_kpa` must be positive and the renderer raises when it is not.

    ⚖️ FOUR STATES, ENUMERATED, NOT SIMULATED. NOTES-B4 §6 is explicit: the
    table is a lookup and the four narrative notes are hand-written per state.
    Computing the pair from two rate terms would make the four notes
    unwritable, because each one says something different about WHY the two
    counts came together, and only three of the four are the same mechanism.

    ⚖️ EVERY NUMBER ON THIS INSTRUMENT IS COMPUTED HERE, AT BUILD TIME, and
    ships as a finished string on the state's own element. The two bar widths
    and the five printed figures come out of one pair of kPa values per state,
    in one place, so a bar and the figure beside it cannot disagree. The wiring
    copies them; it computes nothing. This is `gut-journey`'s rule and it holds
    for the same reason.

    ⚠️ THE BOTH-ON NOTE QUOTES ITS OWN NUMBERS — "1197 in, 477 out" —
    and they are `13.3 × 90` and `5.3 × 90`. Nothing can check a
    figure embedded in prose, and nothing here tries. If a science review moves
    a kPa value, that sentence moves with it.
    """
    states = a.get("states") or []
    switches = a.get("switches") or []
    if len(switches) != 2:
        raise ValueError(
            "crossing-counter %r declares %d switch(es), not 2. Four states is "
            "two switches squared, and the lookup table is built from the pair."
            % (act_id, len(switches)))
    for w in switches:
        for key in ("id", "on_label", "off_label"):
            if not w.get(key):
                raise ValueError(
                    "crossing-counter %r switch %r is missing %r. The caption "
                    "IS the state — Design's switch says “Breathing: "
                    "stopped” rather than greying out — so both "
                    "halves are authored."
                    % (act_id, w.get("id"), key))
    if [w["id"] for w in switches] != ["breathing", "blood_flow"]:
        raise ValueError(
            "crossing-counter %r switches are %s; they must be `breathing` "
            "then `blood_flow`, because `states[]` is keyed on those two names."
            % (act_id, [w.get("id") for w in switches]))

    if len(states) != 4:
        raise ValueError(
            "crossing-counter %r declares %d state(s), not 4."
            % (act_id, len(states)))
    seen = {}
    for st in states:
        for key in ("breathing", "blood_flow"):
            if not isinstance(st.get(key), bool):
                raise ValueError(
                    "crossing-counter %r state %r has %s=%r; it is a bool."
                    % (act_id, st.get("note", "")[:24], key, st.get(key)))
        key = (st["breathing"], st["blood_flow"])
        if key in seen:
            raise ValueError(
                "crossing-counter %r declares breathing=%s blood_flow=%s "
                "twice. Both switches are reachable, so a duplicated state "
                "means a missing one." % (act_id, key[0], key[1]))
        seen[key] = st
        if not st.get("note"):
            raise ValueError(
                "crossing-counter %r state breathing=%s blood_flow=%s has no "
                "note. Each of the four says something different about why the "
                "counts came together, and a state with none is the readout "
                "going silent exactly where the argument is."
                % (act_id, key[0], key[1]))
        for field in ("alveolar_kpa", "blood_kpa"):
            v = st.get(field)
            if not isinstance(v, (int, float)) or isinstance(v, bool) or v <= 0:
                raise ValueError(
                    "crossing-counter %r state breathing=%s blood_flow=%s has "
                    "%s=%r. It must be positive: it is a bar width as well as "
                    "a readout, and an outward bar that disappears teaches the "
                    "one-way picture the block exists to kill."
                    % (act_id, key[0], key[1], field, v))
    missing = [k for k in ((True, True), (True, False), (False, True),
                           (False, False)) if k not in seen]
    if missing:
        raise ValueError(
            "crossing-counter %r declares no state for %s. Every combination "
            "is one tap away from every other." % (act_id, missing))

    tiles = a.get("tiles") or {}
    tmissing = sorted({"alveolar", "blood", "net"} - set(tiles))
    if tmissing:
        raise ValueError(
            "crossing-counter %r tiles is missing %s."
            % (act_id, ", ".join(tmissing)))
    bars = a.get("bars") or {}
    bmissing = sorted({"into", "out_of"} - set(bars))
    if bmissing:
        raise ValueError(
            "crossing-counter %r bars is missing %s. The outward bar is named "
            "as explicitly as the inward one because a student who reads only "
            "one label reads only one direction."
            % (act_id, ", ".join(bmissing)))
    for key in ("kpa_format", "crossing_format", "net_zero"):
        if not a.get(key):
            raise ValueError(
                "crossing-counter %r declares no %r." % (act_id, key))

    per_kpa = float(a.get("crossings_per_kpa") or 90)
    max_cross = float(a.get("max_crossings") or 1250)
    if per_kpa <= 0 or max_cross <= 0:
        raise ValueError(
            "crossing-counter %r needs positive `crossings_per_kpa` and "
            "`max_crossings`." % act_id)
    biggest = max(max(st["alveolar_kpa"], st["blood_kpa"]) for st in states)
    if biggest * per_kpa > max_cross:
        raise ValueError(
            "crossing-counter %r scales its bars against max_crossings=%s, but "
            "the largest count is %d. A bar wider than its track is a readout "
            "that has run off the end of the instrument."
            % (act_id, max_cross, round(biggest * per_kpa)))

    zero_below = float(a.get("net_zero_below") or 20)

    def fmt_kpa(v):
        return a["kpa_format"].replace("{v}", "%.1f" % v)

    def fmt_cross(n):
        return a["crossing_format"].replace("{n}", str(int(n)))

    panels = []
    for st in states:
        sid = "%d-%d" % (1 if st["breathing"] else 0,
                         1 if st["blood_flow"] else 0)
        into = round(st["alveolar_kpa"] * per_kpa)
        out_of = round(st["blood_kpa"] * per_kpa)
        net = into - out_of
        panels.append(
            '<p class="ks3-cross-note" data-state="%s" data-alveolar="%s" '
            'data-blood="%s" data-in="%s" data-out="%s" data-net="%s" '
            'data-inw="%s" data-outw="%s"%s>%s</p>'
            % (sid, e(fmt_kpa(st["alveolar_kpa"])), e(fmt_kpa(st["blood_kpa"])),
               e(fmt_cross(into)), e(fmt_cross(out_of)),
               e(a["net_zero"] if net <= zero_below else fmt_cross(net)),
               ("%.1f" % (into / max_cross * 100)),
               ("%.1f" % (out_of / max_cross * 100)),
               "" if st is states[0] else " hidden",
               rich(st["note"])))

    first = states[0]
    first_in = round(first["alveolar_kpa"] * per_kpa)
    first_out = round(first["blood_kpa"] * per_kpa)
    first_net = first_in - first_out

    switch_html = "".join(
        '<button type="button" class="ks3-cross-switch" data-switch="%s" '
        'aria-pressed="%s" data-on-label="%s" data-off-label="%s">%s</button>'
        % (e(w["id"]),
           "true" if w.get("start", True) else "false",
           e(w["on_label"]), e(w["off_label"]),
           t(w["on_label"] if w.get("start", True) else w["off_label"]))
        for w in switches)

    def tile(key, value, tone=""):
        return ('<div class="ks3-cross-tile"%s>'
                '<p class="ks3-cross-tilelabel">%s</p>'
                '<p class="ks3-cross-tileval" data-tile="%s">%s</p></div>'
                % (tone, t(tiles[key]), key, t(value)))

    def bar(side, name, value, width):
        return ('<li class="ks3-cross-barrow">'
                '<div class="ks3-cross-barhead">'
                '<p class="ks3-cross-barname">%s</p>'
                '<p class="ks3-cross-barval" data-bar="%s">%s</p></div>'
                '<span class="ks3-cross-track">'
                '<span class="ks3-cross-fill" data-fill="%s" '
                'style="width:%s%%"></span></span></li>'
                % (t(name), side, t(value), side, width))

    return ('<div class="ks3-cross" data-cross data-state="%d-%d">'
            '<div class="ks3-cross-switches">%s</div>'
            '<div class="ks3-cross-panel">'
            '<div class="ks3-cross-tiles">%s%s%s</div>'
            '<ul class="ks3-cross-bars" role="list">%s%s</ul>%s</div></div>'
            % (1 if first["breathing"] else 0, 1 if first["blood_flow"] else 0,
               switch_html,
               tile("alveolar", fmt_kpa(first["alveolar_kpa"])),
               tile("blood", fmt_kpa(first["blood_kpa"])),
               tile("net",
                    a["net_zero"] if first_net <= zero_below
                    else fmt_cross(first_net),
                    ' data-tone="net"'),
               bar("in", bars["into"], fmt_cross(first_in),
                   "%.1f" % (first_in / max_cross * 100)),
               bar("out", bars["out_of"], fmt_cross(first_out),
                   "%.1f" % (first_out / max_cross * 100)),
               "".join(panels)))


def r_fault_bench(a, act_id):
    """⊕ b4-04 `#s-bench` — the switch-a-part-off idiom, run backwards.

    ⚖️ THE STUDENT LOCATES, THEY DO NOT SWITCH. B2's `system-switch` removes a
    part and reports the symptom; this hands over the symptom and asks which
    part is at fault. Same anatomy of reasoning, opposite direction, and it is
    why this is not `system-switch` with different copy: there is no chain, no
    part to open, and the commitment is a DIAGNOSIS whose truth the block then
    settles.

    ⚖️ THE REVEAL IS NEVER WITHHELD FOR A WRONG ANSWER. The verdict line says
    which of the two happened and the four rows follow either way. A block that
    only explained itself to students who had already guessed right would teach
    nobody, and Design draws exactly one reveal per factor.

    ⚖️ EVERY FACTOR KEEPS ITS OWN PICK AND ITS OWN OPENED FLAG. Three tabs over
    one shared option list, and a student who opens exercise and moves to
    asthma must find asthma uncommitted and exercise exactly as they left it.
    Emit-all-show-one, with the state in the DOM and nowhere else.

    ⚠️ AN ANSWER THAT IS NOT ON THE LIST CANNOT BE LOCATED. Every factor's
    `part` is checked against the offered `parts` at build time; a typo there
    would produce a factor no student could ever get right, and the verdict
    line would read "Not the part you chose" on all four options.
    """
    parts = a.get("parts") or []
    if len(parts) < 2:
        raise ValueError(
            "fault-bench %r declares %d part(s). Locating a fault needs "
            "somewhere else it could have been." % (act_id, len(parts)))
    for p in parts:
        if not (p.get("id") and p.get("text")):
            raise ValueError(
                "fault-bench %r part %r needs `id` and `text`."
                % (act_id, p.get("id")))
    part_ids = [p["id"] for p in parts]

    factors = a.get("factors") or []
    if len(factors) < 2:
        raise ValueError(
            "fault-bench %r declares %d factor(s). The block's argument is "
            "that different factors hit different parts, and one factor cannot "
            "make it." % (act_id, len(factors)))
    for f in factors:
        for key in ("id", "label", "tag", "scenario", "part", "answer"):
            if not f.get(key):
                raise ValueError(
                    "fault-bench %r factor %r is missing %r."
                    % (act_id, f.get("id"), key))
        if f["part"] not in part_ids:
            raise ValueError(
                "fault-bench %r factor %r is at fault in %r, which is not one "
                "of the offered parts %s. Every option would read “not "
                "the part you chose” and the factor would be unanswerable."
                % (act_id, f["id"], f["part"], part_ids))
        rows = f.get("rows") or []
        if not rows:
            raise ValueError(
                "fault-bench %r factor %r declares no rows. The reveal is the "
                "explanation, and a headline with nothing under it is a "
                "verdict without a reason." % (act_id, f["id"]))
        for r in rows:
            if not (r.get("label") and r.get("text")):
                raise ValueError(
                    "fault-bench %r factor %r has a row missing `label` or "
                    "`text`." % (act_id, f["id"]))

    for key in ("question", "open_label"):
        if not a.get(key):
            raise ValueError("fault-bench %r declares no %r." % (act_id, key))
    hints = a.get("hints") or {}
    hmissing = sorted({"none", "ready", "opened"} - set(hints))
    if hmissing:
        raise ValueError(
            "fault-bench %r hints is missing %s. The line beside the button is "
            "the only thing telling a student why it is disabled."
            % (act_id, ", ".join(hmissing)))
    verdicts = a.get("verdicts") or {}
    vmissing = sorted({"right", "wrong"} - set(verdicts))
    if vmissing:
        raise ValueError(
            "fault-bench %r verdicts is missing %s."
            % (act_id, ", ".join(vmissing)))

    first = factors[0]
    for f in factors:
        if f["id"] == a.get("start_factor"):
            first = f
            break

    tabs = "".join(
        '<button type="button" class="ks3-fault-tab" data-factor="%s" '
        'aria-pressed="%s">%s</button>'
        % (e(f["id"]), "true" if f is first else "false", t(f["label"]))
        for f in factors)

    scenarios = "".join(
        '<div class="ks3-fault-scenario" data-factor="%s"%s>'
        '<p class="ks3-fault-tag">%s</p>'
        '<p class="ks3-fault-text">%s</p></div>'
        % (e(f["id"]), "" if f is first else " hidden", t(f["tag"]),
           rich(f["scenario"]))
        for f in factors)

    options = "".join(
        '<li><button type="button" class="ks3-option" data-part="%s" '
        'aria-pressed="false">'
        '<span class="ks3-opt-mark" aria-hidden="true">%s</span>'
        '<span class="ks3-opt-label">%s</span></button></li>'
        % (e(p["id"]), t(option_letter(i)), t(p["text"]))
        for i, p in enumerate(parts))

    reveals = "".join(
        '<div class="ks3-fault-reveal" data-factor="%s" data-answer="%s" hidden>'
        '<p class="ks3-fault-verdict">'
        '<span data-verdict="right" hidden>%s</span>'
        '<span data-verdict="wrong" hidden>%s</span></p>'
        '<p class="ks3-fault-answer">%s</p>'
        '<dl class="ks3-fault-rows">%s</dl></div>'
        % (e(f["id"]), e(f["part"]), t(verdicts["right"]), t(verdicts["wrong"]),
           t(f["answer"]),
           "".join(
               '<div class="ks3-fault-row"><dt>%s</dt><dd>%s</dd></div>'
               % (t(r["label"]), rich(r["text"])) for r in f["rows"]))
        for f in factors)

    return ('<div class="ks3-fault" data-fault data-total="%d" '
            'data-factor="%s" data-hint-none="%s" data-hint-ready="%s" '
            'data-hint-opened="%s">'
            '<div class="ks3-fault-tabs">%s</div>'
            '<div class="ks3-fault-scenarios">%s</div>'
            '<p class="ks3-fault-q">%s</p>'
            '<ul class="ks3-options">%s</ul>'
            '<div class="ks3-fault-foot">'
            '<button type="button" class="ks3-reveal-btn ks3-fault-open" '
            'data-fault-open disabled>%s</button>'
            '<span class="ks3-fault-hint" data-fault-hint role="status">%s'
            '</span></div>'
            '<div class="ks3-fault-reveals">%s</div></div>'
            % (len(factors), e(first["id"]), e(hints["none"]),
               e(hints["ready"]), e(hints["opened"]), tabs, scenarios,
               t(a["question"]), options, t(a["open_label"]),
               t(hints["none"]), reveals))


def r_two_process_ledger(a, act_id):
    """⊕ b4-05 `#s-ledger` — two processes, one net figure, and a flat bar.

    ⚖️ THE RESPIRATION BAR NEVER MOVES, AND THAT IS THE INSTRUMENT. Its width
    is written once, here, from `resp_rate`, and no code path anywhere can
    change it: the wiring never touches that fill. `BREATH-12`/`BREATH-13` are
    the belief that plants respire only at night, and the whole confrontation is
    a student dragging the light from one end to the other and watching the top
    bar refuse to move. A respiration bar computed per frame, even from a
    constant, would be one refactor away from acquiring a light term.

    ⚖️ THE MIDDLE BRANCH IS THE POINT. Net uptake and net release are the two
    readings a student expects; the compensation point is the one that overturns
    something, because it is a flat line produced by two processes at full rate
    rather than by nothing happening. Design's own copy for that branch opens
    "This is the dawn reading from the hook."

    ⚠️ THE BALANCED BRANCH MUST BE REACHABLE, and the renderer proves it rather
    than assuming it. `curve.max` must exceed `resp_rate` or the two never
    cross; some integer light level must land inside `balanced_window` or the
    branch is copy no student can reach. And when the payload NAMES a preset as
    the compensation point (`balanced_preset`), that preset is held to it —
    Design's `dawn = 21` gives a net of +2.33 against its own curve, which is
    firmly net uptake, while the balanced copy claims to be the dawn reading.
    The engine does not choose which side is right. It refuses to let the two
    disagree silently. See `docs/ks3/b4-inventory/PAYLOAD-SCHEMA.md` §5.
    """
    curve = a.get("curve") or {}
    for key in ("max", "constant", "scale"):
        v = curve.get(key)
        if not isinstance(v, (int, float)) or isinstance(v, bool) or v <= 0:
            raise ValueError(
                "two-process-ledger %r curve.%s is %r; it must be a positive "
                "number." % (act_id, key, v))
    resp = a.get("resp_rate")
    if not isinstance(resp, (int, float)) or isinstance(resp, bool) or resp <= 0:
        raise ValueError(
            "two-process-ledger %r resp_rate is %r. It is the flat bar and the "
            "thing the net figure is measured against." % (act_id, resp))
    if float(curve["max"]) <= float(resp):
        raise ValueError(
            "two-process-ledger %r has curve.max=%s and resp_rate=%s. "
            "Photosynthesis could never overtake respiration, so the net "
            "figure would be negative at every light level and the "
            "compensation point would not exist."
            % (act_id, curve["max"], resp))
    if float(curve["scale"]) < max(float(curve["max"]), float(resp)):
        raise ValueError(
            "two-process-ledger %r scales its bars against curve.scale=%s, "
            "which is smaller than curve.max=%s / resp_rate=%s. A bar wider "
            "than its track has run off the end of the instrument."
            % (act_id, curve["scale"], curve["max"], resp))

    window = float(a.get("balanced_window") or 0.25)
    if window <= 0:
        raise ValueError(
            "two-process-ledger %r balanced_window is %r; it is the half-width "
            "of the window and must be positive." % (act_id, window))

    def photo_at(light):
        return float(curve["max"]) * (
            1.0 - math.exp(-float(light) / float(curve["constant"])))

    reachable = [n for n in range(0, 101)
                 if abs(photo_at(n) - float(resp)) < window]
    if not reachable:
        raise ValueError(
            "two-process-ledger %r: no light level between 0 and 100 puts the "
            "net rate inside ±%s, so the balanced verdict is copy no "
            "student can reach. The curve and the respiration rate cross at "
            "light %.1f — either widen the window or move the rate."
            % (act_id, window,
               -float(curve["constant"]) * math.log(1 - float(resp) / float(curve["max"]))))

    presets = a.get("presets") or []
    if not presets:
        raise ValueError(
            "two-process-ledger %r declares no presets." % act_id)
    for p in presets:
        if not (p.get("id") and p.get("label")):
            raise ValueError(
                "two-process-ledger %r preset %r needs `id` and `label`."
                % (act_id, p.get("id")))
        v = p.get("value")
        if not isinstance(v, int) or isinstance(v, bool) or not 0 <= v <= 100:
            raise ValueError(
                "two-process-ledger %r preset %r has value %r; it is a light "
                "level 0–100." % (act_id, p["id"], v))
    preset_ids = [p["id"] for p in presets]

    named = a.get("balanced_preset")
    if named:
        if named not in preset_ids:
            raise ValueError(
                "two-process-ledger %r names %r as the compensation point and "
                "there is no such preset. The presets are %s."
                % (act_id, named, preset_ids))
        chosen = [p for p in presets if p["id"] == named][0]
        net_there = photo_at(chosen["value"]) - float(resp)
        if abs(net_there) >= window:
            raise ValueError(
                "two-process-ledger %r names preset %r (light %d) as the "
                "compensation point, but the net rate there is %+.2f, outside "
                "±%s. Pressing it reads as net %s, not as balance. The "
                "window reaches light %d–%d; move the preset rather than "
                "widening the window, which at ±%.2f would call every "
                "reading balanced."
                % (act_id, named, chosen["value"], net_there, window,
                   "uptake" if net_there > 0 else "release",
                   reachable[0], reachable[-1], abs(net_there)))

    start = int(a.get("start_light") or 0)
    if not 0 <= start <= 100:
        raise ValueError(
            "two-process-ledger %r start_light is %d; the slider runs "
            "0–100." % (act_id, start))

    for key in ("light_label", "light_aria", "dark_label", "light_format",
                "rate_format"):
        if not a.get(key):
            raise ValueError(
                "two-process-ledger %r declares no %r." % (act_id, key))
    resp_spec = a.get("respiration") or {}
    if not (resp_spec.get("name") and resp_spec.get("note")):
        raise ValueError(
            "two-process-ledger %r respiration needs `name` and `note`. The "
            "note is the sentence that tells a student to watch the bar NOT "
            "move, which is the only instruction the flat bar gets." % act_id)
    photo_spec = a.get("photosynthesis") or {}
    pmissing = sorted({"name", "note_dark", "note_light"} - set(photo_spec))
    if pmissing:
        raise ValueError(
            "two-process-ledger %r photosynthesis is missing %s. Darkness gets "
            "its own note because zero is the reading the misconception lives "
            "on." % (act_id, ", ".join(pmissing)))
    net_spec = a.get("net") or {}
    nmissing = sorted({"name", "in_format", "out_format", "note"} - set(net_spec))
    if nmissing:
        raise ValueError(
            "two-process-ledger %r net is missing %s. The two formats carry "
            "the DIRECTION in words — the bar's magnitude cannot, because "
            "it is drawn from an absolute value."
            % (act_id, ", ".join(nmissing)))
    verdicts = a.get("verdicts") or {}
    for branch in ("balanced", "uptake", "release"):
        spec = verdicts.get(branch) or {}
        for key in ("tag", "head", "why"):
            if not spec.get(key):
                raise ValueError(
                    "two-process-ledger %r verdicts.%s is missing %r. All "
                    "three branches are reachable from the slider."
                    % (act_id, branch, key))

    scale = float(curve["scale"])
    photo0 = photo_at(start)
    net0 = photo0 - float(resp)
    branch0 = ("balanced" if abs(net0) < window
               else ("uptake" if net0 > 0 else "release"))

    def rate(v):
        return a["rate_format"].replace("{v}", "%.1f" % v)

    def net_label(v):
        fmt = net_spec["in_format"] if v >= 0 else net_spec["out_format"]
        return fmt.replace("{v}", "%.1f" % abs(v))

    preset_html = "".join(
        '<button type="button" class="ks3-tpl-preset" data-preset="%d" '
        'aria-pressed="%s">%s</button>'
        % (p["value"], "true" if p["value"] == start else "false",
           t(p["label"]))
        for p in presets)

    verdict_html = "".join(
        '<div class="ks3-tpl-verdict" data-verdict="%s"%s>'
        '<p class="ks3-tpl-vtag">%s</p>'
        '<p class="ks3-tpl-vhead">%s</p>'
        '<p class="ks3-tpl-vwhy">%s</p></div>'
        % (branch, "" if branch == branch0 else " hidden",
           t(verdicts[branch]["tag"]), t(verdicts[branch]["head"]),
           rich(verdicts[branch]["why"]))
        for branch in ("balanced", "uptake", "release"))

    sid = "tpl-" + str(act_id)

    return ('<div class="ks3-tpl" data-tpl data-resp="%s" data-max="%s" '
            'data-const="%s" data-scale="%s" data-window="%s" '
            'data-rate-format="%s" data-in-format="%s" data-out-format="%s">'
            '<div class="ks3-tpl-control">'
            '<div class="ks3-tpl-controlhead">'
            '<p class="ks3-tpl-cap">%s</p>'
            '<p class="ks3-tpl-light" data-light data-dark="%s" '
            'data-format="%s">%s</p></div>'
            '<label class="ks3-sr-only" for="%s">%s</label>'
            '<input class="ks3-b4slider ks3-tpl-slider" type="range" id="%s" '
            'min="0" max="100" step="1" value="%d" data-tpl-slider>'
            '<div class="ks3-tpl-presets">%s</div></div>'
            '<div class="ks3-tpl-panel">'
            '<ul class="ks3-tpl-flows" role="list">'
            '<li class="ks3-tpl-flow" data-flow="resp">'
            '<div class="ks3-tpl-flowhead"><p class="ks3-tpl-flowname">%s</p>'
            '<p class="ks3-tpl-flowval">%s</p></div>'
            '<span class="ks3-tpl-track">'
            '<span class="ks3-tpl-fill" data-fill="resp" style="width:%s%%">'
            '</span></span>'
            '<p class="ks3-tpl-flownote">%s</p></li>'
            '<li class="ks3-tpl-flow" data-flow="photo">'
            '<div class="ks3-tpl-flowhead"><p class="ks3-tpl-flowname">%s</p>'
            '<p class="ks3-tpl-flowval" data-val="photo">%s</p></div>'
            '<span class="ks3-tpl-track">'
            '<span class="ks3-tpl-fill" data-fill="photo" style="width:%s%%">'
            '</span></span>'
            '<p class="ks3-tpl-flownote" data-note="dark"%s>%s</p>'
            '<p class="ks3-tpl-flownote" data-note="light"%s>%s</p></li>'
            '<li class="ks3-tpl-flow" data-flow="net">'
            '<div class="ks3-tpl-flowhead"><p class="ks3-tpl-flowname">%s</p>'
            '<p class="ks3-tpl-flowval" data-val="net">%s</p></div>'
            '<span class="ks3-tpl-track">'
            '<span class="ks3-tpl-fill" data-fill="net" data-tone="%s" '
            'style="width:%s%%"></span></span>'
            '<p class="ks3-tpl-flownote">%s</p></li></ul>'
            '<div class="ks3-tpl-verdicts">%s</div></div></div>'
            % (resp, curve["max"], curve["constant"], curve["scale"], window,
               e(a["rate_format"]), e(net_spec["in_format"]),
               e(net_spec["out_format"]),
               t(a["light_label"]), e(a["dark_label"]), e(a["light_format"]),
               t(a["dark_label"] if start == 0
                 else a["light_format"].replace("{n}", str(start))),
               e(sid), t(a["light_aria"]), e(sid), start, preset_html,
               t(resp_spec["name"]), t(rate(float(resp))),
               ("%.1f" % (float(resp) / scale * 100)),
               rich(resp_spec["note"]),
               t(photo_spec["name"]), t(rate(photo0)),
               ("%.1f" % (photo0 / scale * 100)),
               "" if start == 0 else " hidden", rich(photo_spec["note_dark"]),
               " hidden" if start == 0 else "", rich(photo_spec["note_light"]),
               t(net_spec["name"]), t(net_label(net0)), branch0,
               ("%.1f" % (abs(net0) / scale * 100)), rich(net_spec["note"]),
               verdict_html))
# renderers: ═══ END B4 ═══

ACTIVITY_KIND_RENDERERS = {
    "test-board":    ("ks3-board",
                      ' data-instrument data-board data-stage-done="0"'),
    "sort-rows":     ("ks3-sort",
                      ' data-instrument data-sort data-stage-done="0"'),
    "critique-steps": ("ks3-critique",
                       ' data-instrument data-critique data-stage-done="0"'),
    "fifa-construct": ("ks3-construct-block",
                       ' data-instrument data-construct data-stage-done="0"'),
    "cell-bench":    ("ks3-cellbench-block",
                      ' data-instrument data-cellbench data-stage-done="0"'),
    "sort-pairs":    ("ks3-pairs", ' data-instrument data-pairs data-stage-done="0"'),
    "fit-parts":     ("ks3-fit-block",
                      ' data-instrument data-fitblock data-stage-done="0"'),
    "zoom-ladder":   ("ks3-zoom-block",
                      ' data-instrument data-zoomblock data-stage-done="0"'),
    "sort-task":     ("ks3-hard", ' data-instrument data-hard data-stage-done="0"'),
    "removal-cases": ("ks3-removal-block",
                      ' data-instrument data-removal data-stage-done="0"'),
    "system-bench":  ("ks3-bench-block",
                      ' data-instrument data-benchblock data-stage-done="0"'),
    "sabotage":      ("ks3-sab-block",
                      ' data-instrument data-sabotage data-stage-done="0"'),
    "settles-it":    ("ks3-settles",
                      ' data-instrument data-settles data-stage-done="0"'),
    # Expository: no control, no commitment, nothing to tick.
    "confrontation": ("ks3-confront", " data-instrument data-confront"),

    # ── B2 · Movement (⊕ MRB-220) ──
    # Every one of these has markup above, CSS in `shared/ks3.css` and a wire
    # function reached from `wireInstruments()`. All four carry a completion
    # contract, so all four emit `data-stage-done="0"` and the rail reads the
    # instrument's own predicate rather than guessing from `aria-pressed`.
    "job-sort":      ("ks3-jobsort-block",
                      ' data-instrument data-jobsort-block data-stage-done="0"'),
    "system-switch": ("ks3-switch-block",
                      ' data-instrument data-switchblock data-stage-done="0"'),
    "joint-bench":   ("ks3-joint-block",
                      ' data-instrument data-jointblock data-stage-done="0"'),
    "muscle-pair":   ("ks3-muscle-block",
                      ' data-instrument data-muscleblock data-stage-done="0"'),

    # ── C2 · Atoms, elements and compounds (⊕ MRB-220) ──
    # All nine carry a completion contract, so all nine emit
    # `data-stage-done="0"` and the rail reads the instrument's own predicate
    # rather than guessing from `aria-pressed` — which on `#s-model` would tick
    # on load, because every claim starts pressed ON.
    "claim-switch":  ("ks3-claim-block",
                      ' data-instrument data-claimblock data-stage-done="0"'),
    "scale-zoom":    ("ks3-scale-block",
                      ' data-instrument data-scaleblock data-stage-done="0"'),
    "test-budget-bench": ("ks3-budget-block",
                          ' data-instrument data-budgetblock '
                          'data-stage-done="0"'),
    "mixture-compound-dish": ("ks3-dish-block",
                              ' data-instrument data-dishblock '
                              'data-stage-done="0"'),
    # One component, three instances, two layouts, three headline types.
    "verdict-cards": ("ks3-vcards-block",
                      ' data-instrument data-vcardsblock data-stage-done="0"'),
    "formula-builder": ("ks3-fb-block",
                        ' data-instrument data-fbblock data-stage-done="0"'),
    # `model-limit` renders the two contrast cards, then falls through to the
    # shell's own `options` + `reveal` — which IS Design's commit and reveal,
    # so the block keeps the ordinary Law 4 wiring and needs no engine of its
    # own. It carries no `data-instrument`: `wirePredictions` owns the three
    # options, which is correct, because there is no instrument to own them.
    "model-limit": ("ks3-limit-block", ""),
    "balance-bench": ("ks3-bal-block",
                      ' data-instrument data-balblock data-stage-done="0"'),
    # NOT `fifa-construct`. Two multiple-choice ladders, a number field and a
    # unit select against four free-text inputs and a tick list — a different
    # mechanism, whose assertions the existing one would raise on.
    "fifa-pick": ("ks3-pick-block",
                  ' data-instrument data-pickblock data-stage-done="0"'),
    # ═══ BEGIN C1 dispatch ═══
    "collision-counter": ("ks3-counter-block", ' data-instrument data-counterblock data-stage-done="0"'),
    "evidence-bench": ("ks3-ebench-block", ' data-instrument data-ebenchblock data-stage-done="0"'),
    "gap-test-rig": ("ks3-gap-block", ' data-instrument data-gapblock data-stage-done="0"'),
    "halving-bench": ("ks3-cut-block", ' data-instrument data-cutblock data-stage-done="0"'),
    "heating-bench": ("ks3-hb-block", ' data-instrument data-hbblock data-stage-done="0"'),
    "keyed-commit": ("ks3-keyed-block", ' data-instrument data-keyedblock data-stage-done="0"'),
    "model-timeline": ("ks3-mtl-block", ' data-instrument data-mtlblock data-stage-done="0"'),
    "prediction-stack": ("ks3-predict-block", ' data-instrument data-predictblock data-stage-done="0"'),
    "random-walk-bench": ("ks3-walk-block", ' data-instrument data-walkblock data-stage-done="0"'),
    "scale-cards": ("ks3-scards-block", " data-instrument data-scalecards"),
    "sort-cards": ("ks3-sortcards-block", ' data-instrument data-sortcardsblock data-stage-done="0"'),
    "state-bench": ("ks3-sbench-block", ' data-instrument data-sbenchblock data-stage-done="0"'),
    "state-matrix": ("ks3-smatrix-block", ' data-instrument data-smatrixblock'),
    # ═══ END C1 dispatch ═══
    # ═══ BEGIN B2 dispatch ═══
    "arm-lever": ("ks3-lever-block", ' data-instrument data-leverblock data-stage-done="0"'),
    "lever-steps": ("ks3-lstep-block", ' data-instrument data-lstepblock data-stage-done="0"'),
    "meter-compare": ("ks3-meters-block", ' data-instrument data-metersblock data-stage-done="0"'),
    # ═══ END B2 dispatch ═══
    # ═══ BEGIN B3 dispatch ═══
    "band-commit": ("ks3-plate-block", ' data-instrument data-plateblock data-stage-done="0"'),
    "clinic-cases": ("ks3-clinic-block", ' data-instrument data-clinicblock data-stage-done="0"'),
    "enzyme-run": ("ks3-erun-block", ' data-instrument data-erunblock data-stage-done="0"'),
    "fold-builder": ("ks3-fold-block", ' data-instrument data-foldblock data-stage-done="0"'),
    "gut-journey": ("ks3-gut-block", ' data-instrument data-gutblock data-stage-done="0"'),
    "job-switch": ("ks3-jobsw-block", ' data-instrument data-jobswblock data-stage-done="0"'),
    "person-ledger": ("ks3-ledger-block", ' data-instrument data-ledgerblock data-stage-done="0"'),
    "test-bench": ("ks3-tbench-block", ' data-instrument data-tbenchblock data-stage-done="0"'),
    # ═══ END B3 dispatch ═══
    # ═══ BEGIN B4 dispatch ═══
    # All five sit on a `practical` segment — measured on all five
    # pages, no exceptions — so all five are on ink and every colour rule
    # they hang on is scoped `.ks3-dark …`. All five carry a completion
    # contract, so all five emit `data-stage-done="0"`.
    "gas-compare": ("ks3-gas-block", ' data-instrument data-gasblock data-stage-done="0"'),
    "bell-jar": ("ks3-bell-block", ' data-instrument data-bellblock data-stage-done="0"'),
    "crossing-counter": ("ks3-cross-block", ' data-instrument data-crossblock data-stage-done="0"'),
    "fault-bench": ("ks3-fault-block", ' data-instrument data-faultblock data-stage-done="0"'),
    "two-process-ledger": ("ks3-tpl-block", ' data-instrument data-tplblock data-stage-done="0"'),
    # ═══ END B4 dispatch ═══
}

# Kinds that ARE the generic shell, and are not waiting for a component.
#
# The distinction matters or the gate above is noise. A `predict` is a prompt,
# some options and a reveal — the generic shell IS its drawn component, and C1
# has shipped them since MRB-183 with Design's screens behind them. An
# `instrument` kind is different: Design drew a specific mechanism for it, and
# rendering it as prompt-options-reveal is the MRB-205 failure exactly.
#
# So a kind is either declared generic here, or it has a renderer above, or the
# build says it is unrendered. There is no fourth state, and adding a kind to
# this set is a claim someone has to defend in review.
#
# ⊖ `confrontation` was in this set until 14 Aug 2026 and did not belong. The
# claim a kind makes by being here is that prompt/options/reveal IS its drawn
# component — true of C1's seven, which carry exactly `prompt` + `reveal` +
# `targets`, and false of all six of B1's, which carry `statements`,
# `scorecards` and `paragraphs` that nothing read. Measured cost: b1-03's whole
# `#s-think` rendered as `! Think again` and nothing else. It has a renderer now.
#
# The lesson generalises: membership here is a claim about the CONTENT, not
# about the kind's name. The same kind can be generic in one unit and an
# instrument in the next, and the only way to know is to check what the payload
# actually carries — which is what the orphan-key sweep does.
GENERIC_ACTIVITY_KINDS = {
    "predict", "classify", "construct", "investigation", "lab",
    "reveal-cards", "worked-example",
}


# ── which function draws each instrument ─────────────────────────────────
#
# ⊕ MRB-228, 16 Aug 2026. This used to be a chain of fifty-odd
# `if kind == "x": parts.append(r_x(a, act_id))` lines inside `r_activity`,
# and C1's thirteen instruments shipped through it as a silent regression.
#
# The mechanism is worth writing down because it will otherwise be rebuilt.
# There were TWO registries a new instrument had to be added to, and only one
# of them was checked:
#
#   `ACTIVITY_KIND_RENDERERS`  the SHELL — a modifier class and the marker
#                              attribute ks3.js dispatches on. C1's thirteen
#                              were spliced in here correctly.
#   the `if kind ==` chain     the actual call to the drawing function. C1's
#                              thirteen were never added.
#
# So every C1 page carried `class="ks3-keyed-block" data-keyedblock` — the
# shell, complete and correct — around an instrument that had not been drawn.
# The generic `if a.get("options")` branch then ran on a payload shaped for
# `r_keyed_commit`, whose options are `{"text": …, "reply": …}` dicts rather
# than strings, and printed the Python dict repr into the student's option
# button: `{&#x27;text&#x27;: &#x27;Throw the model away…`.
#
# MRB-203's gate was watching, and passed, because it asks whether the kind is
# in `ACTIVITY_KIND_RENDERERS` — presence in the shell table was being read as
# proof of rendering, and it never was. The gate now reads THIS table.
#
# One registry, so there is nothing left to disagree with.
ACTIVITY_KIND_FN = {
    "test-board":             r_test_board,
    "sort-rows":              r_sort_rows,
    "settles-it":             r_settles_it,
    "critique-steps":         r_critique_steps,
    "fifa-construct":         r_fifa_construct,
    "cell-bench":             r_cell_bench,
    "sort-pairs":             r_sort_pairs,
    "fit-parts":              r_fit_parts,
    "zoom-ladder":            r_zoom_ladder,
    "sort-task":              r_sort_task,
    "removal-cases":          r_removal_cases,
    "system-bench":           r_system_bench,
    "sabotage":               r_sabotage,
    "job-sort":               r_job_sort,
    "system-switch":          r_system_switch,
    "joint-bench":            r_joint_bench,
    "muscle-pair":            r_muscle_pair,
    "claim-switch":           r_claim_switch,
    "scale-zoom":             r_scale_zoom,
    "test-budget-bench":      r_test_budget_bench,
    "mixture-compound-dish":  r_mixture_compound_dish,
    "verdict-cards":          r_verdict_cards,
    "formula-builder":        r_formula_builder,
    "model-limit":            r_model_limit,
    "balance-bench":          r_balance_bench,
    "fifa-pick":              r_fifa_pick,
    # ═══ BEGIN C1 renderfn ═══
    "collision-counter":      r_collision_counter,
    "evidence-bench":         r_evidence_bench,
    "gap-test-rig":           r_gap_test_rig,
    "halving-bench":          r_halving_bench,
    "heating-bench":          r_heating_bench,
    "keyed-commit":           r_keyed_commit,
    "model-timeline":         r_model_timeline,
    "prediction-stack":       r_prediction_stack,
    "random-walk-bench":      r_random_walk_bench,
    "scale-cards":            r_scale_cards,
    "sort-cards":             r_sort_cards,
    "state-bench":            r_state_bench,
    "state-matrix":           r_state_matrix,
    # ═══ END C1 renderfn ═══
    # ═══ BEGIN B2 renderfn ═══
    "arm-lever":              r_arm_lever,
    "lever-steps":            r_lever_steps,
    "meter-compare":          r_meter_compare,
    # ═══ END B2 renderfn ═══
    # ═══ BEGIN B3 renderfn ═══
    "band-commit":            r_band_commit,
    "clinic-cases":           r_clinic_cases,
    "enzyme-run":             r_enzyme_run,
    "fold-builder":           r_fold_builder,
    "gut-journey":            r_gut_journey,
    "job-switch":             r_job_switch,
    "person-ledger":          r_person_ledger,
    "test-bench":             r_test_bench,
    # ═══ END B3 renderfn ═══
    # ═══ BEGIN B4 renderfn ═══
    "gas-compare":            r_gas_compare,
    "bell-jar":               r_bell_jar,
    "crossing-counter":       r_crossing_counter,
    "fault-bench":            r_fault_bench,
    "two-process-ledger":     r_two_process_ledger,
    # ═══ END B4 renderfn ═══
}

# The three that need the whole lesson, not just the activity, because they
# read the lesson's equation or its misconception register.
def _kinds_taking_lesson():
    """Which renderers need the whole LESSON, not just the activity.

    ⊕ MRB-228, second pass. This was a hand-written set —
    `{"fifa-construct", "sabotage", "fifa-pick"}` — and it was the same shape
    of bug as the two registries above, one size down: a fact about a function,
    kept somewhere other than the function. B2's
    `r_lever_steps(lesson, a, act_id)` was spliced in, nobody added it to the
    set, and the build died with `missing 1 required positional argument`.

    That failure was loud, which is why it is not the complaint. The complaint
    is that a correct new renderer could not be added without editing a list
    somewhere else, and a registry like that goes out of step quietly far more
    often than it goes out of step loudly.

    So: ask the function. A renderer whose FIRST parameter is named `lesson`
    gets the lesson. The declaration lives on the function and cannot disagree
    with itself.
    """
    import inspect
    out = set()
    for kind, fn in ACTIVITY_KIND_FN.items():
        try:
            params = list(inspect.signature(fn).parameters)
        except (TypeError, ValueError):
            continue
        if params and params[0] == "lesson":
            out.add(kind)
    return out


_KIND_FN_TAKES_LESSON = _kinds_taking_lesson()

# Which instruments draw the activity's OWN `options` and `reveal`, and so must
# not also get the generic list underneath.
#
# ⊕ MRB-228. This is DERIVED, not declared, and the difference is the whole
# point. The first cut of the fix suppressed the generic branches for every
# drawn instrument, on the reasoning that "if something drew this activity, it
# drew all of it". That is false and the build said so: c2-03's
# `mixture-compound-dish` draws a four-option bench gate from its own payload
# and ALSO carries a two-option `options` list asking a different question
# ("mixture or compound?"). Suppressing that removed a control Design drew.
#
# So the test is not "did something draw this" but "did what drew it consume
# this key". A renderer that reads `a["options"]` owns them; one that never
# looks at them does not, and the generic list is still the only thing
# rendering the author's question.
#
# Reading the function's own source is what keeps the two in step. A renderer
# that starts consuming `options` tomorrow is covered the moment it does,
# with nobody remembering to update a list here — which is exactly the failure
# mode that produced the two-registries bug this whole section exists to close.
def _kinds_consuming(pattern):
    import inspect
    rx = re.compile(pattern)
    out = set()
    for kind, fn in ACTIVITY_KIND_FN.items():
        try:
            if rx.search(inspect.getsource(fn)):
                out.add(kind)
        except (OSError, TypeError):
            # No source (a C function, or a stripped install). Treat it as not
            # consuming, which keeps the generic branch — the safe direction,
            # because a duplicate control is visible and a missing one is not.
            pass
    return out


_KIND_FN_OWNS_OPTIONS = _kinds_consuming(r'a\.get\(\s*"options"|a\[\s*"options"\s*\]')
_KIND_FN_OWNS_REVEAL = _kinds_consuming(r'a\.get\(\s*"reveal"|a\[\s*"reveal"\s*\]')

# Kinds drawn by their BLOCK TYPE rather than by their kind, and so legitimately
# absent from the table above.
#
# `confrontation` is the only one. A `misconception` block draws
# `r_confrontation` unconditionally, before the kind dispatch runs, because the
# amber shell and the confrontation are the same component — the block type IS
# the instrument. Putting it in `ACTIVITY_KIND_FN` would draw it twice, and
# would also suppress the generic options/reveal branches that C1's seven live
# confrontations depend on: they carry exactly `prompt` + `reveal` + `targets`
# and nothing else.
_KIND_FN_BY_BLOCK_TYPE = {"confrontation"}

# Every registered SHELL must have a function that draws something into it.
# This is the assertion the old arrangement could not make, and it is at module
# scope so it fires on import — before a single page is written, rather than
# after 294 of them have shipped looking fine.
_unfn = sorted(set(ACTIVITY_KIND_RENDERERS)
               - set(ACTIVITY_KIND_FN) - _KIND_FN_BY_BLOCK_TYPE)
if _unfn:
    raise SystemExit(
        "build_ks3: %d instrument kind(s) register a shell in "
        "ACTIVITY_KIND_RENDERERS but no drawing function in "
        "ACTIVITY_KIND_FN: %s\n"
        "The page would render the shell around Design's payload run through "
        "the generic prompt/options/reveal branch, which is how C1 shipped "
        "dict reprs into option buttons (MRB-228)."
        % (len(_unfn), ", ".join(_unfn)))

# And nothing may be drawn into a shell that does not exist.
_unshell = sorted(set(ACTIVITY_KIND_FN) - set(ACTIVITY_KIND_RENDERERS))
if _unshell:
    raise SystemExit(
        "build_ks3: %d kind(s) have a drawing function but no shell in "
        "ACTIVITY_KIND_RENDERERS: %s" % (len(_unshell), ", ".join(_unshell)))


def r_activity(lesson, block_type, act_id, block=None):
    """The one activity renderer, with a per-type shell.

    Inner order is prompt → options → cards → sim → fifa → reveal → criteria:
    commit first, then the thing that tests the commitment, then the words that
    settle it. `data-activity` stays on the section because ks3.js walks up to
    it for the Law 4 gate.

    ⊕ `block` is the `core[]` entry that named this activity, and it is passed
    for one reason: its `anchor`. Before B1 round two an activity block dropped
    it on the floor, so `#s-board`, `#s-sort` and `#s-think` were never emitted
    and every rail link and hash link into an activity landed nowhere. The rail
    cannot be built without this.
    """
    a = _activity(lesson, act_id)
    if not a:
        return ""
    shell_cls, eyebrow, prompt_tag = ACTIVITY_SHELLS[block_type]
    kind = a.get("kind") or ""

    # ⊕ MRB-228 — fill a LIVE heading at build time as well as at runtime.
    #
    # b2-04's `#s-build` heading is a readout of the rig the student left set:
    # "Your rig: {load} kg at {hand} cm, muscle at {ins} cm." The shell emits
    # the <h2> before any instrument renderer runs, and `wireLeverSteps`
    # repaints it on load — so in a browser the braces are never seen, and in
    # the shipped HTML they are permanent. A crawler, a reader with JS off, and
    # anything that quotes the page get the template.
    #
    # ⚠️ THE FILLED HEADING IS A LOCAL, and that is the whole correctness of
    # this. The first cut did `a = dict(a, heading=filled)`, which also handed
    # the filled sentence to `r_lever_steps` — and that renderer emits the
    # heading again as `data-head`, the template `wireLeverSteps` refills every
    # time the student moves the rig. So `data-head` shipped a string with no
    # placeholders left in it and the runtime repaint rewrote the heading with
    # itself: correct on load, frozen for ever after. The step options below it
    # updated and the sentence above them did not.
    #
    # Filling a local leaves `a` exactly as authored, so the instrument still
    # receives its raw template and the two paths agree. `a` is never mutated
    # either way — `r_activity` runs once per page, but the lesson record is
    # shared with every gate that reads it afterwards.
    heading = a.get("heading")
    if kind == "lever-steps" and heading:
        heading = _lever_steps_heading(lesson, a)

    # ⊕ §4.8.2 — the two CLASSIFY instruments. Each takes a modifier class and
    # a marker attribute: the class is what the stylesheet hangs the instrument
    # on, and the attribute is what shared/ks3.js dispatches on. `data-board`
    # and `data-sort` also tell `wirePredictions` to keep its hands off — an
    # instrument owns every option inside it, and the generic Law 4 wiring
    # would otherwise unhide the first `[data-reveal]` it found, which on the
    # board is specimen one's verdict panel.
    instrument = ACTIVITY_KIND_RENDERERS.get(kind)
    marker = ""
    if instrument:
        shell_cls += " " + instrument[0]
        # `data-stage-done` is the rail's completion contract (shared/ks3.js,
        # `doneByDom`). An instrument that has one emits it at 0 rather than
        # leaving it absent, so the rail reads the instrument's own predicate
        # and never falls through to "anything in here is aria-pressed" — the
        # specimen tabs would tick that stage on page load, and MRB-208 ruled
        # that nothing is ticked on load. An instrument with no contract omits
        # it entirely; see the table.
        marker = instrument[1]

    # ⊕ MRB-220 — an activity block may name its own ground. Design's three
    # sorter blocks sit on `--ks3-inset` rather than the shell's own card, and
    # the ground is a measured property of the block, not of the instrument
    # inside it. Validated against `_GROUNDS` so a typo is a build error and
    # never a `background: var(--ks3-taupe)` that resolves to nothing.
    ground = (' data-ground="%s"' % e(_ground_of(a, a.get("ground") or "card"))
              if a.get("ground") else "")
    parts = ['<section class="%s"%s data-activity="%s"%s%s>'
             % (shell_cls, _id_attr(block or {}), e(act_id), marker, ground)]

    # ⊕ §4.8.2 — a scoped eyebrow. Design's instrument shells carry
    # "Your turn · test four things", not the shell's fixed "Your turn"; the
    # fixed label is the fallback, never an override.
    eyebrow = a.get("eyebrow") or eyebrow

    # ⊕ MRB-220 — Design's B2 blocks put a live progress readout on the SAME
    # ROW as the eyebrow and the <h2>, right-aligned and mono. The shell's
    # fixed eyebrow / h2 / prompt stack cannot make that row, and dropping the
    # counter below the lede would put "0 of 6 decided" where the instruction
    # goes. Only a block that authors `head_counter` takes the row, so no
    # shipped block moves.
    hc = a.get("head_counter")
    if block_type == "misconception":
        parts.append('<div class="ks3-mis-head">'
                     '<span class="ks3-mis-badge" aria-hidden="true">!</span>'
                     '<p class="ks3-eyebrow">%s</p></div>' % t(eyebrow))
        # ⊕ Subsumes the old single-quote path. With no authored `statements`
        # this emits exactly the register quote it always did, which is why
        # C1's seven confrontations do not move: none of them carries any of
        # the new keys.
        parts.append(r_confrontation(lesson, a, act_id))
    elif hc:
        parts.append('<div class="ks3-blockhead"><div>'
                     '<p class="ks3-eyebrow">%s</p>%s</div>%s</div>'
                     % (t(eyebrow),
                        ("<h2>%s</h2>" % t(heading)) if heading else "",
                        _head_counter(hc)))
        prompt_tag = "p"
    else:
        parts.append('<p class="ks3-eyebrow">%s</p>' % t(eyebrow))

    # ⊕ §4.8.2 — an explicit `heading` beside the prompt. The `check` shell
    # promotes the PROMPT to the block's <h2>, which works while a block has
    # only one of the two. Design's instruments carry both a title and a line
    # of instruction under it, and without this the title would be lost.
    if heading and not hc:
        parts.append("<h2>%s</h2>" % t(heading))
        prompt_tag = "p"

    if a.get("prompt"):
        # ⚠️ A card grid keeps its prompt as prose even in a `check`. The prompt
        # IS R4's declaration ask ("say it, then tap"), and verify_ks3.py's
        # §5.1.2(a) gate reads that ask out of the block's non-hidden <p>
        # elements before the grid. Promoting it to a heading would leave the
        # gate looking at the eyebrow alone and passing or failing on the
        # wording of "Your turn" — a live check silently disarmed.
        tag = "p" if a.get("cards") else prompt_tag
        parts.append("<%s>%s</%s>" % (tag, t(a["prompt"]), tag))

    # ⊕ MRB-228 — one lookup, replacing the fifty-line `if kind ==` chain. See
    # `ACTIVITY_KIND_FN` for what the chain cost. The branches were mutually
    # exclusive (there is one `kind`), so this is the same dispatch, and the
    # non-C1 pages are byte-identical across the change.
    fn = ACTIVITY_KIND_FN.get(kind)
    if fn:
        parts.append(fn(lesson, a, act_id) if kind in _KIND_FN_TAKES_LESSON
                     else fn(a, act_id))
    if a.get("scorecards"):
        parts.append(r_scorecards(a["scorecards"]))

    # ⚠️ An instrument that CONSUMED `options` has already drawn them, in
    # Design's own treatment. Running the generic list as well emits the same
    # payload twice — and when that payload is dicts rather than strings, the
    # generic list prints the dict repr into the button, which is where
    # MRB-228's `{&#x27;text&#x27;: …}` buttons came from.
    #
    # Consumed, not merely drawn: see `_KIND_FN_OWNS_OPTIONS`.
    if a.get("options") and kind not in _KIND_FN_OWNS_OPTIONS:
        parts.append(r_activity_options(a["options"]))
    if a.get("cards"):
        parts.append(r_cards(a["cards"]))
    if a.get("sim"):
        parts.append(r_sim(a["sim"], act_id))
    if a.get("fifa"):
        # ⊕ MRB-204 step 3 — a STAGED reveal, one step at a time, on tap. A
        # worked example a student reads is one they watch happen to somebody
        # else; the point of the pause is that they try the next line first.
        # One-way: there is no collapse, because unshowing a step teaches
        # nothing and gives a student a way to lose their place.
        parts.append(r_fifa(a["fifa"], staged=bool(a.get("staged")),
                            buttons=a.get("buttons") or {}))
    if a.get("reveal") and kind not in _KIND_FN_OWNS_REVEAL:
        # Law 4: the reveal is gated behind the student's commitment.
        #
        # ⊕ MRB-228 — guarded for the same reason as the options branch above:
        # an instrument that consumed `reveal` has drawn that panel in its own
        # treatment, and a second generic `.ks3-reveal` under it is the same
        # sentences again in a different box.
        #
        # ⊕ MRB-220 — a reveal may be a LIST of paragraphs. All four of B2's
        # `#s-think` reveals are two paragraphs, and one `reveal` string would
        # either lose the second or run both together into one wall.
        #
        # The list form also takes Design's own panel treatment — card ground
        # on a 2px ink border, not the accent tint a one-line reveal takes.
        # That is a NEW class rather than a change to `.ks3-reveal`, because
        # `.ks3-reveal` is what the hook uses on these same pages and what
        # C1's seven live confrontations use; restyling it would repaint
        # pages Mide has already approved to match four he has not seen.
        rev = a["reveal"]
        if isinstance(rev, (list, tuple)):
            parts.append('<div class="ks3-reveal ks3-reveal-panel" hidden '
                         'data-reveal>%s</div>'
                         % "".join("<p>%s</p>" % rich(p) for p in rev))
        else:
            parts.append('<div class="ks3-reveal" hidden data-reveal>%s</div>'
                         % t(rev))
    if a.get("success"):
        parts.append(r_criteria(a["success"]))
    parts.append("</section>")
    return "".join(parts)


# ── the mastery ladder (§5, MRB-184's ruling of 9 Aug) ───────────────────

# Rung number is fixed to the rung, not to its position in what rendered. A
# lesson missing one rung shows Rung 1, Rung 3, Rung 4 — a gap rather than a
# renumbering, because the number belongs to the rung and a student comparing
# two lessons should find the same number on the same kind of demand in both.
#
# The middle dot is U+00B7, which IS in the latin subset. The circled digits
# this used to use (U+2460–2463) are not, and rendered as tofu inside a
# Bricolage-800 heading.
# ⊕ MRB-208 rung-title amendment (16 Aug 2026, MRB-228). The names below are
# the DEFAULTS, and they are now Design's wording rather than the engine's.
#
# `recall / apply / explain / produce` are the schema's KEYS and they stay —
# they are how a lesson record names a rung and they are not going anywhere.
# What changed is that those key names were also being printed on the page, as
# `2 · Apply` and `4 · Produce`. That vocabulary is internal: it describes what
# the rung is FOR to the person writing it, and it says nothing to the student
# about what the rung is going to do to them. Design's wording does — rung 2 is
# the trap, and saying so is the whole point of the rung.
#
# Every approved delivery agrees on rungs 2 and 4 and varies rungs 1 and 3 per
# lesson (b1 "Discriminate" / "Name the job" / "Read the list", b3 "Which
# three", c2 "Calculate" / "Read it"), so 1 and 3 keep a neutral default and
# every rung takes a per-lesson `title` override — read in `_rung_marked` and
# `_rung_self`, not just declared here.
#
# This is a RELABEL, not a science change, and it moves live pages. It ships in
# its own commit for that reason.
LADDER_RUNGS = (("recall", 1, "Recall"),
                ("apply", 2, "The one that catches people"),
                ("explain", 3, "Explain"),
                ("produce", 4, "Take it somewhere new"))

# Runs to twelve because the browse layer counts lessons in a card, not just
# ladder rungs (which never exceed four), and because the sorter says "All eight
# sorted" (Design's own string). `_count_word` already falls back to digits above
# the tuple, so lengthening it changes no existing output. Spelling numbers stays
# in ONE place: `r_sort_rows` emits the word alongside the count so
# `shared/ks3.js` never has to carry a second, drifting copy of this table.
NUMBER_WORDS = ("no", "one", "two", "three", "four", "five", "six", "seven",
                "eight", "nine", "ten", "eleven", "twelve")


def _count_word(n):
    return NUMBER_WORDS[n] if n < len(NUMBER_WORDS) else str(n)


# ⊕ MRB-228. The rung NUMBER is structural — it is tied to the schema key, not
# to anything an author decides — so the engine owns it and always prints it.
# The authored `title` supplies the LABEL that follows it.
#
# Design writes the two together, as one finished heading: four B1 lessons
# carry `"title": "Rung 1 · Name the job"`, and every B3–B7 page draws the same
# full-heading shape. Those keys were read by NOTHING until the relabel wired
# them, so the ambiguity had never surfaced; wiring them naively produced
# "Rung 1 · Rung 1 · Name the job" on four live pages.
#
# So normalise instead of choosing a side: strip an author-supplied "Rung N · "
# prefix and let the engine put the number back. Both authoring styles then
# render identically, Design's delivered strings need no rewriting, and an
# author who writes a bare label cannot silently lose the number.
_RUNG_PREFIX = re.compile(r"^\s*Rung\s+\d+\s*[·:.\-]\s*", re.IGNORECASE)


def _rung_title(name, q):
    """The label after "Rung N · ", from the authored title or the default."""
    return _RUNG_PREFIX.sub("", q.get("title") or name).strip() or name


def _rung_marked(key, num, name, q):
    """Rungs the PAGE marks: options, one right answer, per-option correction.

    This is the only place in the whole generator where `data-correct` appears.
    R3 depends on that staying true.
    """
    opts = []
    for i, o in enumerate(q["options"]):
        fb = (q.get("feedback") or {}).get(i, "")
        correct = "1" if i == q.get("answer") else "0"
        opts.append(_option_li(
            i, o, ' data-correct="%s" data-feedback="%s"' % (correct, e(fb))))
    return ('<div class="ks3-rung" data-rung="%s" data-mode="marked">'
            '<h3 tabindex="-1">Rung %d · %s</h3>'
            '<p class="ks3-rung-q">%s</p>'
            '<ul class="ks3-options" role="list">%s</ul>'
            '</div>'
            % (e(key), num, e(_rung_title(name, q)), t(q.get("q", "")),
               "".join(opts)))


def _rung_self(slug, key, num, name, q):
    """Rungs the STUDENT marks (R8): write, then check, then mark.

    The criteria are not on the page yet — they arrive when ks3.js unhides
    `[data-ticks]`, because a visible checklist IS the answer. Every tick is a
    real `<input type="checkbox">` with a real label (R15, MRB-184), and the
    rung counts as met only when all of them are ticked.

    `tabindex="-1"` on the h3 is what "Retry my misses" moves focus to.
    """
    ticks = []
    for i, s in enumerate(q["success"]):
        cid = "ks3-crit-%s-%s-%d" % (slug, key, i)
        ticks.append(
            '<li class="ks3-tick">'
            '<input type="checkbox" id="%s" data-crit>'
            '<label for="%s"><span class="ks3-tick-num">%d</span> %s</label>'
            '</li>' % (e(cid), e(cid), i + 1, t(s)))
    aid = "ks3-ans-%s-%s" % (slug, key)
    return ('<div class="ks3-rung ks3-rung-self" data-rung="%s" data-mode="self">'
            '<h3 tabindex="-1">Rung %d · %s</h3>'
            '<p class="ks3-rung-q">%s</p>'
            '<label class="ks3-answer-label" for="%s">%s</label>'
            '<textarea class="ks3-answer" id="%s" data-answer rows="5"%s>'
            '</textarea>'
            '<button type="button" class="ks3-check-btn" data-check '
            'aria-expanded="false">Check my answer</button>'
            '<ul class="ks3-ticks" hidden data-ticks role="list">%s</ul>'
            '<p class="ks3-tally" hidden data-tally role="status"></p>'
            '</div>'
            # ⊕ MRB-220 — `field_label` and `placeholder` are READ now. Both
            # are authored on twelve live lessons and were read by nothing:
            # every self-marked rung shipped the generic "Write your answer"
            # over the label the author wrote, and the placeholder — which on
            # these pages is the first half of a sentence, and is the
            # scaffold — reached no student at all. Exactly the defect R5
            # exists to catch, found by the byte-identity sweep rather than by
            # the lint. The generic label stays as the fallback.
            % (e(key), num, e(_rung_title(name, q)), t(q.get("q", "")), e(aid),
               t(q.get("field_label") or "Write your answer"), e(aid),
               (' placeholder="%s"' % e(q["placeholder"])
                if q.get("placeholder") else ""),
               "".join(ticks)))


def r_ladder(lesson, block=None):
    """§5's four-rung ladder. Two the page marks, two the student marks.

    ⚠️ Which is which comes from the DATA, not from the rung's name or its
    position: a rung with `options` is page-marked, a rung with `success` and no
    options is self-marked, and a rung with neither is skipped. Hard-coding
    "rungs 3 and 4 are self-marked" would be right for all six C1 lessons and
    wrong the first time an author writes a written Apply rung — and it would
    fail as a missing textarea, which looks like a data gap rather than a
    renderer bug.

    ks3.js appends the feedback line and the retry block; neither is emitted
    here, because both are states of an answered ladder rather than parts of a
    resting one.
    """
    lad = lesson.get("ladder") or {}
    slug = lesson["slug"]
    rungs, marked, self_marked = [], [], []
    for key, num, name in LADDER_RUNGS:
        q = lad.get(key)
        if not q:
            continue
        if q.get("options"):
            rungs.append(_rung_marked(key, num, name, q))
            marked.append(num)
        elif q.get("success"):
            rungs.append(_rung_self(slug, key, num, name, q))
            self_marked.append(num)

    # Both header lines are counted off what actually rendered, so neither can
    # describe a ladder the page is not showing. With the standard 2 + 2 shape
    # they read exactly as Design labelled the component: "Four rungs. Two the
    # page marks, two you mark."
    total = len(marked) + len(self_marked)
    sub = ("%s rung%s. %s the page marks, %s you mark."
           % (_count_word(total).capitalize(), "" if total == 1 else "s",
              _count_word(len(marked)).capitalize(),
              _count_word(len(self_marked))))
    if not self_marked:
        note = "The page marks every rung."
    elif len(self_marked) == 1:
        note = "Rung %d you mark yourself." % self_marked[0]
    else:
        note = ("Rungs %s and %d you mark yourself."
                % (", ".join(str(n) for n in self_marked[:-1]), self_marked[-1]))

    return ('<section class="ks3-block ks3-ladder" data-lesson="%s"%s>'
            '<div class="ks3-ladder-head">'
            '<div><h2>Mastery ladder</h2>'
            '<p class="ks3-ladder-sub">%s</p></div>'
            '<div class="ks3-ladder-score" aria-live="polite">'
            '<p class="ks3-score" data-score>Not started yet.</p>'
            '<p class="ks3-score-note" data-score-note>%s</p></div>'
            '</div>'
            '<div class="ks3-rungs">%s</div>'
            '</section>'
            % (e(slug), _id_attr(block or {}), e(sub), e(note),
               "".join(rungs)))


# ── the four block types B1 round two added (§5.1.1 ⊕) ───────────────────

# Grounds a block may sit on. Spelled as a map rather than interpolating the
# author's string into a var() call, so a typo is a build error and never a
# silent `background: var(--ks3-taupe)` that resolves to nothing.
_GROUNDS = {"band": "var(--ks3-band)", "card": "var(--ks3-card)",
            "inset": "var(--ks3-inset)", "ground": "var(--ks3-ground)"}


def _ground_of(block, default):
    g = block.get("ground") or default
    if g not in _GROUNDS:
        raise ValueError(
            "unknown ground %r — KS3 grounds are %s"
            % (g, ", ".join(sorted(_GROUNDS))))
    return g


def r_key_fact(lesson, block):
    """⊕ §4.8.1 B — the one line that must survive the lesson.

    Ruled by Mide (MRB-208 rule 3): cream band, 2px ink outline, hard orange
    offset shadow, small mono label, statement in display type. **Deliberately
    not amber** — amber is a wrong idea being confronted, and a key fact must
    never be confusable with a misconception block. Bold alone was judged
    insufficient.

    The accent shadow is what separates this from a `.ks3-block`, whose shadow
    is ink. And the box grows NO badge, letter or mark: `--ks3-band` is also the
    ground a chosen-WRONG ladder option takes (MRB-202), so anything mark-like
    here would read as a verdict on a line that is simply true.

    `ground` exists because b1-06 nests one inside a block that is itself
    `--ks3-band`, which is the entire reason drift 5 had an outlier. Default is
    `band`, 5:1 across the delivery.
    """
    # A `key-fact` block in `core` positions the box by document order, which is
    # the generator's own mechanism and needs no placement DSL. `ref` names an
    # entry in the lesson's `key_facts` list BY ID, so the text lives once and
    # the block says only where it goes.
    spec = dict(block)
    ref = block.get("ref")
    if ref is not None:
        facts = lesson.get("key_facts") or []
        # `ref` is an id. It may also be a positional index, because a lesson
        # with one key fact has no reason to name it and two of the six B1
        # modules authored it that way. Both are unambiguous — an id is a
        # string and an index is an int — so accepting both costs nothing and
        # refusing one would fail the build over a spelling.
        if isinstance(ref, int) and not isinstance(ref, bool):
            if ref >= len(facts):
                raise ValueError(
                    "key-fact ref %d is out of range — the lesson declares %d"
                    % (ref, len(facts)))
            found = facts[ref]
        else:
            found = next((kf for kf in facts if kf.get("id") == ref), None)
            if found is None:
                raise ValueError(
                    "key-fact ref %r matches no key_facts[].id" % ref)
        merged = dict(found)
        merged.update({k: v for k, v in block.items()
                       if k not in ("ref", "type")})
        spec = merged
    ground = _ground_of(spec, "band")
    return ('<div class="ks3-keyfact" data-ground="%s">'
            '<p class="ks3-keyfact-label">%s</p>'
            '<p class="ks3-keyfact-body">%s</p></div>'
            % (e(ground), t(spec.get("eyebrow") or "Key fact"),
               rich(spec.get("text", ""))))


def r_rule(lesson, block):
    """⊕ §5.1.1 — the statement panel: the lesson's rule, in the student's words.

    CLASSIFY's spine already demanded it ("Ends with the rule stated in the
    student's words") and there was nowhere to put it. A 3px ink border and no
    shadow are what separate it from a `.ks3-block`; the cards' `--ks3-option-
    border` is what separates them from misconception cards' ink.

    The statement takes drift 3's RULED clamp — `clamp(28px, 3.9vw, 44px)`, the
    modal and median of the four real statements in the delivery — not any one
    page's own. b1-02's formula statement and b1-05's instrument readout are
    excluded from that role and are different components.
    """
    cards = "".join(
        '<li><p class="ks3-rule-term">%s</p><p class="ks3-rule-gloss">%s</p></li>'
        % (t(c.get("term", "")), rich(c.get("gloss", "")))
        for c in block.get("cards") or [])
    close = ('<p class="ks3-rule-close">%s</p>' % rich(block["close"])
             if block.get("close") else "")
    return ('<section class="ks3-rule"%s><p class="ks3-eyebrow">%s</p>'
            '<p class="ks3-rule-statement">%s</p>'
            '%s%s</section>'
            % (_id_attr(block), t(block.get("eyebrow") or "What settles it"),
               rich(block.get("statement", "")),
               ('<ul class="ks3-rule-cards">%s</ul>' % cards) if cards else "",
               close))


def r_formula(lesson, block):
    """⊕ §5.1.1 · MRB-204 step 1 — the formula stands alone.

    Ruled by Mide: "Its own block on the page, nothing else in it. Not embedded
    in a paragraph, not inside a worked example, not sharing a card. A student
    flicking back through the lesson to find the formula must be able to see it
    from the scroll position."

    Centred with NO max-width, which is the whole difference between this and
    `rule`'s left-aligned 20ch measure. The two shells are otherwise identical
    and a future tidy-up will try to merge them, so a parity pair asserts they
    stay apart.
    """
    # ⊕ MRB-204 step 2 — the triangle, in the same block as the statement it
    # draws. Design gives them separate shells inside one classless section;
    # both are the formula, and a student flicking back wants them together.
    tri = (r_formula_triangle(block["triangle"])
           if block.get("triangle") else "")
    # ⊕ MRB-220 / MRB-204 as amended 15 Aug 2026 — a formula that is a SUM.
    #
    # `figure` draws the relationship in the shape the relationship has; `cover`
    # is the MRB-204 cover interaction over that shape. For `c2-06` the figure
    # is a BALANCE BEAM and the cover is a PART–WHOLE BAR, because conservation
    # of mass is a sum and a triangle encodes a product or a quotient. Drawing a
    # sum as a triangle would teach a false relationship to make a rule fit.
    # Measured, not inferred: c2-06 contains the word "triangle" zero times.
    #
    # The triangle path above is untouched, which is the point of two branches —
    # `b2-04` is a product, it keeps its triangle, and neither knows about the
    # other.
    figure = r_formula_figure(block["figure"]) if block.get("figure") else ""
    support = ('<p class="ks3-formula-support">%s</p>'
               % "<br>".join(t(s) for s in block["support"])
               ) if block.get("support") else ""
    bar = r_cover_bar(block["cover"]) if block.get("cover") else ""
    eyebrow = ('<p class="ks3-eyebrow ks3-formula-eyebrow">%s</p>'
               % t(block["eyebrow"])) if block.get("eyebrow") else ""
    return ('<section class="ks3-formula"%s%s>%s%s'
            '<div class="ks3-formula-statement"><p>%s</p></div>%s%s%s</section>'
            % (_id_attr(block),
               ' data-shape="sum"' if (figure or bar) else "",
               eyebrow, figure,
               t(block.get("statement", "")), support, tri, bar))


# Design draws the sum's figure as a level balance beam: a fulcrum, a post, a
# beam, an accent pivot, two hangers, two pans and a caption. Every number below
# is measured off the frozen page's SVG (c2-06 lines 186–198) in its own 520×210
# viewBox, so the drawing is Design's geometry and not a redraw.
_BEAM = (
    '<path d="M260 176L216 200H304Z" class="ks3-beam-stand"></path>'
    '<line x1="260" y1="60" x2="260" y2="178" class="ks3-beam-post"></line>'
    '<line x1="70" y1="60" x2="450" y2="60" class="ks3-beam-arm"></line>'
    '<circle cx="260" cy="60" r="13" class="ks3-beam-pivot"></circle>'
    '<line x1="70" y1="60" x2="70" y2="96" class="ks3-beam-hanger"></line>'
    '<line x1="450" y1="60" x2="450" y2="96" class="ks3-beam-hanger"></line>'
    '<rect x="10" y="96" width="120" height="44" rx="12" class="ks3-beam-pan">'
    '</rect>'
    '<rect x="390" y="96" width="120" height="44" rx="12" class="ks3-beam-pan">'
    '</rect>'
    '<text x="70" y="126" text-anchor="middle" class="ks3-beam-label">%s</text>'
    '<text x="450" y="126" text-anchor="middle" class="ks3-beam-label">%s</text>'
    '<text x="260" y="30" text-anchor="middle" class="ks3-beam-caption">%s</text>')


def r_formula_figure(fig):
    """The drawn relationship. `balance` today; the triangle keeps its own path.

    ⚖️ **A LEVEL BEAM IS A CLAIM, and it is the claim the lesson makes.** The
    two pans are `before` and `after`, the beam is dead level, and the caption
    says `always level`. Tilting it — or animating it — would say that mass
    can be out of balance and then settle, which is exactly the idea the lesson
    exists to kill.
    """
    shape = fig.get("shape")
    if shape != "balance":
        raise ValueError(
            "formula figure shape %r is not drawn. `balance` is the sum's "
            "figure; a product's figure is the `triangle` key, which has its "
            "own renderer." % shape)
    pans = fig.get("pans") or {}
    return ('<div class="ks3-formula-figure">'
            '<svg viewBox="0 0 520 210" role="img" aria-label="%s" '
            'class="ks3-beam">%s</svg></div>'
            % (e(fig.get("aria_label", "")),
               _BEAM % (t(pans.get("left", "")), t(pans.get("right", "")),
                        t(fig.get("caption", "")))))


def r_cover_bar(cov):
    """⊕ The `cover-triangle` kind, BAR variant — c2-06's part–whole model.

    ⚖️ **THE PARTS SUM TO THE WHOLE, TO THE PIXEL.** Design draws 450 = 296 + 8
    + 146, and that arithmetic IS the teaching. So the widths are DERIVED from
    the authored weights rather than laid out by flex: a flex row would make
    the two parts whatever the container allowed, and a bar whose halves do not
    add up is a bar model that lies.

    Five ways this is not the triangle, all measured (map §8.2):

      * geometry — one bar over two, not a 260×216 triangle with a divider;
      * slots — `whole` and n parts, not `top`/`left`/`right`;
      * a GHOST LABEL under the plate, so a student can still see what they
        covered. The triangle's cover is a plain opaque rect;
      * RADIO, not toggle. The triangle un-covers on a second press; this never
        uncovers and it STARTS covered;
      * two fields per cover — a display-type `result` and a `sentence` —
        against the triangle's one note.
    """
    if cov.get("shape") != "bar":
        raise ValueError(
            "cover shape %r is not drawn; the bar variant is `bar`."
            % cov.get("shape"))
    whole = cov.get("whole") or {}
    parts = cov.get("parts") or []
    if len(parts) < 2:
        raise ValueError(
            "cover-bar declares %d part(s). A part–whole bar needs at least "
            "two, or there is no sum to see." % len(parts))
    results = cov.get("results") or {}
    covered = cov.get("covered") or parts[-1]["id"]

    # Design's own viewBox and geometry (page lines 207–227). GAP is the 8px
    # that makes 296 + 8 + 146 = 450 true, and it is subtracted from the
    # available width before the weights are shared out, so the parts always
    # sum to the whole no matter what weights an author writes.
    X, Y_W, Y_P, W, H, GAP, R = 10, 18, 108, 450, 56, 8, 12
    total = sum(float(p.get("weight") or 0) for p in parts) or len(parts)
    span = W - GAP * (len(parts) - 1)

    def plate(x, w, y, label, size, key):
        return ('<g class="ks3-bar-cover" data-cover-plate="%s" hidden>'
                '<rect x="%.2f" y="%d" width="%.2f" height="%d" rx="%d" '
                'class="ks3-bar-plate"></rect>'
                '<text x="%.2f" y="%d" text-anchor="middle" '
                'class="ks3-bar-ghost" style="font-size:%dpx">%s</text></g>'
                % (e(key), x, y, w, H, R, x + w / 2.0, y + 36, size, t(label)))

    cells = ['<rect x="%d" y="%d" width="%d" height="%d" rx="%d" '
             'class="ks3-bar-cell"></rect>'
             '<text x="%.1f" y="%d" text-anchor="middle" class="ks3-bar-label" '
             'style="font-size:24px">%s</text>'
             % (X, Y_W, W, H, R, X + W / 2.0, Y_W + 36,
                t(whole.get("label", "")))]
    covers = [plate(X, W, Y_W, whole.get("label", ""), 24,
                    whole.get("id", "whole"))]
    x = float(X)
    for p in parts:
        w = span * (float(p.get("weight") or 1) / total)
        cells.append('<rect x="%.2f" y="%d" width="%.2f" height="%d" rx="%d" '
                     'class="ks3-bar-cell"></rect>'
                     '<text x="%.2f" y="%d" text-anchor="middle" '
                     'class="ks3-bar-label" style="font-size:22px">%s</text>'
                     % (x, Y_P, w, H, R, x + w / 2.0, Y_P + 36,
                        t(p.get("label", ""))))
        covers.append(plate(x, w, Y_P, p.get("label", ""), 22, p["id"]))
        x += w + GAP

    btns = "".join(
        '<button type="button" class="ks3-bar-btn" data-cover="%s" '
        'aria-pressed="%s">%s</button>'
        % (e(c["id"]), "true" if c["id"] == covered else "false",
           t(c.get("button", "")))
        for c in ([whole] + list(parts)) if c.get("button"))

    first = results.get(covered) or {}
    return ('<div class="ks3-bar-block" data-coverbar data-covered="%s" '
            'data-results="%s">'
            '<div class="ks3-bar-head"><p class="ks3-eyebrow">%s</p>'
            '<h2>%s</h2></div>'
            '<div class="ks3-bar-row">'
            '<svg viewBox="0 0 470 196" role="img" aria-label="%s" '
            'class="ks3-bar">%s'
            '<line x1="10" y1="86" x2="460" y2="86" class="ks3-bar-split">'
            '</line>%s</svg>'
            '<div class="ks3-bar-side"><div class="ks3-bar-btns">%s</div>'
            '<p class="ks3-bar-result" data-bar-result>%s</p>'
            '<p class="ks3-bar-sentence" data-bar-sentence>%s</p>'
            '<p class="ks3-bar-close">%s</p></div></div></div>'
            % (e(covered),
               e(json.dumps(results, separators=(",", ":"), sort_keys=True,
                            ensure_ascii=False)),
               t(cov.get("eyebrow", "")), t(cov.get("heading", "")),
               e(cov.get("aria_label", "")), "".join(cells), "".join(covers),
               btns, t(first.get("result", "")), t(first.get("sentence", "")),
               rich(cov.get("close", ""))))


def r_comparison(lesson, block):
    """⊕ §5.1.1 — CONTRAST's spine. Two things held against each other.

    FLEX, NEVER GRID, and that is a measured constraint rather than a taste:
    a grid cannot produce the 820px stack without a second query. Root-level
    `flex-wrap`, `flex: 0 0 118px` on the label, `flex: 1 1 250px; min-width: 0`
    on the cells (MRB-210).

    **Every cell emits its caption unconditionally**, hidden by CSS above 820px.
    Emitting it conditionally would need JS and would break at a container width
    the media query does not know about. The captions ARE the column captions —
    one authored string used twice per column, never authored twice.

    Under `max-width: 820px` the dark header row hides and each cell shows its
    own mono caption, so every stacked sentence stays attributed. Without that
    the discrimination breaks on a phone, which is the point of the block.
    """
    cols = block.get("columns") or []
    if len(cols) != 2:
        # The flex basis maths is written for two. Say so rather than paint a
        # third column at a width nobody chose.
        raise ValueError("comparison takes exactly 2 columns, got %d" % len(cols))

    head = "".join('<span class="ks3-compare-cell" data-tone="%s">%s</span>'
                   % (e(c.get("tone", "ink")), t(c.get("caption", "")))
                   for c in cols)
    rows = []
    for i, r in enumerate(block.get("rows") or []):
        cells = "".join(
            '<span class="ks3-compare-cell" data-tone="%s">'
            '<span class="ks3-compare-caption" aria-hidden="true">%s</span>'
            '<span class="ks3-compare-text">%s</span></span>'
            % (e((block.get("row_tones") or ["ink", "ink"])[j]),
               t(cols[j].get("caption", "")), t(cell))
            for j, cell in enumerate(r.get("cells") or []))
        rows.append('<li class="ks3-compare-row" data-zebra="%d">'
                    '<span class="ks3-compare-name">%s</span>%s</li>'
                    % (i % 2, t(r.get("name", "")), cells))

    nested = block.get("key_fact")
    kf = r_key_fact(lesson, dict(nested, ground=nested.get("ground", "card"))) if nested else ""
    return ('<section class="ks3-compare" data-ground="%s"%s>'
            '<p class="ks3-eyebrow" data-tone="%s">%s</p>'
            '<p class="ks3-compare-statement">%s</p>'
            '<ul class="ks3-compare-rows">'
            '<li class="ks3-compare-head" aria-hidden="true">'
            '<span class="ks3-compare-name"></span>%s</li>%s</ul>%s</section>'
            % (e(_ground_of(block, "band")), _id_attr(block),
               e(block.get("eyebrow_tone", "ink-muted")),
               t(block.get("eyebrow", "")), t(block.get("statement", "")),
               head, "".join(rows), kf))


def _id_attr(block):
    """The section's anchor id, if it has one.

    `anchor` and `id` both appear in authored data and mean different things:
    `id` names the ACTIVITY a block renders (it is a key into `activities[]`),
    while `anchor` names the SECTION the rail and hash links point at. A block
    can carry both, and when it does the anchor is the one that belongs in the
    document. Reading `id` as an anchor would put an activity's name in the URL
    and break every rail link on the page.

    The 92px `scroll-margin-top` that makes an anchor land clear of the sticky
    bar is a rule in ks3.css on `.ks3-lesson [id]`, so it follows automatically
    from emitting the attribute — no block has to remember it.
    """
    anchor = block.get("anchor")
    return (' id="%s"' % e(anchor)) if anchor else ""


BLOCK_RENDERERS = {
    "hook": r_hook,
    "key-fact": r_key_fact,
    "rule": r_rule,
    "formula": r_formula,
    "comparison": r_comparison,
    "explainer": r_explainer,
    "figure": r_figure,
    "keyword": r_keyword,
    "quiz": r_ladder,
    # Ink dark, like the hook and the practical — the three blocks that invert.
    # The label stays an <h2>: `.ks3-keynote p` sets 30px display 700 on every
    # paragraph in the block, so an eyebrow here would be swallowed by it.
    "summary": lambda l, b: (
        '<section class="ks3-block ks3-dark ks3-keynote"%s><h2>Key note</h2>'
        '<p>%s</p></section>' % (_id_attr(b), rich(l.get("key_note", "")))),
    # `b` is passed whole, not just its id: an activity block's `anchor` is what
    # the rail and every hash link point at, and it lives on the BLOCK.
    "misconception": lambda l, b: r_activity(l, "misconception", b.get("id"), b),
    "check": lambda l, b: r_activity(l, "check", b.get("id"), b),
    "worked-example": lambda l, b: r_activity(l, "worked-example", b.get("id"), b),
    "practical": lambda l, b: r_activity(l, "practical", b.get("id"), b),
}

VALID_BLOCK_TYPES = set(BLOCK_RENDERERS)


def render_blocks(lesson, blocks):
    out = []
    for b in blocks:
        btype = b.get("type")
        if btype not in BLOCK_RENDERERS:
            raise ValueError(
                "Lesson %r uses block type %r, which is not in the §5.1.1 "
                "segment vocabulary. Valid types: %s. A new type needs an "
                "amendment to architecture.md, not a local addition."
                % (lesson["slug"], btype, sorted(VALID_BLOCK_TYPES)))
        out.append(BLOCK_RENDERERS[btype](lesson, b))
    return "\n".join(x for x in out if x)


# ── layers and end matter (§5.6, §4 blocks 10–13) ────────────────────────

def r_layer(lesson, blocks, cls, eyebrow):
    """A chosen layer. R12: empty means NOTHING — no heading, no rule, no gap.

    Violet marks a layer the student chose, never a level they were put in.
    KS3 has no tier and must not grow one.
    """
    if not blocks:
        return ""
    return ('<section class="ks3-layer %s">'
            '<div class="ks3-layer-head"><p class="ks3-eyebrow">%s</p>'
            '<span class="ks3-layer-rule" aria-hidden="true"></span></div>'
            '<div class="ks3-layer-body">%s</div>'
            '</section>'
            % (cls, e(eyebrow), render_blocks(lesson, blocks)))


LEGAL_LINE = ('<p class="ks3-legal">Lesson content © MrBadmusAI. Written by a '
              'qualified science teacher; every scientific claim is checked '
              'before a lesson leaves draft.</p>')


def r_endmatter(cards, tutor=None):
    """The end-matter grid. `cards` is [(heading, [<li>…]), …].

    A card with no items is omitted — an empty "Before this lesson" is a
    promise the lesson did not make. The tutor card has no items and always
    renders, because it is an offer rather than a list.
    """
    out = []
    for heading, items in cards:
        if not items:
            continue
        out.append('<section><h2>%s</h2><ul>%s</ul></section>'
                   % (e(heading), "".join(items)))

    # ⚠️ A SPAN, NOT A LINK, AND DELIBERATELY SO — unless the lesson names a
    # destination that exists on its own page.
    #
    # This was an <a href="#ks3-tutor">, and no KS3 page contains an element
    # with that id — so it was a link that silently went nowhere, which is
    # worse than no affordance at all. Claude Design's reference draws it as a
    # <span> for exactly this reason: the tutor panel does not exist yet
    # (§8.8 — a KS3 student can reach no tutor today), and the reference shows
    # what the card will look like rather than pretending the destination is
    # live. It becomes a real control when the KS3 tutor lands, not before.
    #
    # ⊕ §4.8.1 C. Design's approved B1 pages resolve this differently: the card
    # points at THE LESSON'S OWN flagship activity — b1-01's at `#s-board` —
    # which scrolls, asks nobody anything, and still reads as a tutor. That is
    # a real destination on the page it is printed on, so the <span> objection
    # does not apply to it. A lesson that names no `anchor` still gets the
    # span. MRB-209's link gate covers the href either way.
    # ⊕ MRB-220 — `body` is authorable. B1's approved cards put the lesson's
    # own sticking point in the HEADING ("Stuck on why a flame isn’t alive?");
    # Design's B2 cards head it "Ask Mr Badmus AI" and put the question in the
    # paragraph underneath. Both are one card with two lines of copy, and
    # without this slot the B2 question is simply lost. The generic body still
    # fills in when a lesson names neither.
    tutor = tutor or {}
    heading = t(tutor.get("prompt") or "Stuck? Ask Mr Badmus AI")
    if tutor.get("body"):
        body = "<p>%s</p>" % t(tutor["body"])
    else:
        body = ('<p>Ask anything about this lesson and get it explained '
                'another way.</p>' if not tutor.get("prompt") else "")
    label = t(tutor.get("cta") or "Start a question")
    anchor = tutor.get("anchor")
    cta = ('<a class="ks3-tutor-cta" href="#%s">%s %s</a>'
           % (e(anchor), label, MARK_ARROW)) if anchor else (
          '<span class="ks3-tutor-cta">%s %s</span>' % (label, MARK_ARROW))
    out.append('<section class="ks3-tutor"><h2>%s</h2>%s%s</section>'
               % (heading, body, cta))
    return '<div class="ks3-endmatter">%s</div>' % "".join(out)


# ── the progress rail (§4.8.1 A · MRB-208 rule 2) ────────────────────────

# Two variants, and they are NOT two renderings of one thing — they carry
# different information and swap at a hard threshold with no viewport showing
# both and none showing neither:
#
#     [data-rail="side"] { display: none }
#     @media (min-width: 1340px) { side: block; top: none }
#
# ⚖️ BOTH VARIANTS ARE COMPLETION-BASED, AND NOTHING IS TICKED ON LOAD.
# Ruled on MRB-208 (12 Aug, re-affirmed 13 Aug). Design's delivered top bar was
# `IntersectionObserver`-driven only, so it read "4 / 4" with a full accent bar
# for a student who had scrolled to the bottom and answered nothing — and below
# 1340px it is the only rail a student ever sees. The ruling already bound both
# variants and was not scoped to the wide one:
#
#     "here the approved page is wrong and the ruling wins. That is the same
#      shape as the microscope depth table on MRB-210 — where an approved page
#      contradicts a settled fact or a standing ruling, the page gets corrected."
#
# What stays scroll-driven is the side rail's CURRENT ring and the top bar's
# CURRENT LABEL. Those answer "where am I", not "how far have I got", and
# Design drew them that way. The count and the fill are completion, which is
# precisely the defect the ruling named. `shared/ks3.js` owns the state.

def r_rail(lesson):
    """Both rail variants, or nothing at all when a lesson declares no stages."""
    stages = lesson.get("rail") or []
    if not stages:
        return ""

    nodes = []
    for i, s in enumerate(stages):
        last = i == len(stages) - 1
        # The connector belongs to the node ABOVE it, so the last node has none
        # — otherwise the column ends in a 20px stub pointing at nothing.
        line = ("" if last else
                '<span class="ks3-rail-line" aria-hidden="true"></span>')
        nodes.append(
            '<li><a href="#%s" data-rail-stage="%d">'
            '<span class="ks3-rail-chip" aria-hidden="true">%d</span>'
            '<span class="ks3-rail-label">%s</span></a>%s</li>'
            % (e(s["anchor"]), i, i + 1, t(s.get("short", "")), line))

    side = ('<nav class="ks3-rail" data-rail="side" aria-label="Lesson progress">'
            '<ol>%s</ol></nav>' % "".join(nodes))

    # The top bar carries no focusable element, exactly as Design drew it. The
    # side rail's anchors give a keyboard route above 1340px; below it the
    # header trail and normal document order remain tab-navigable. Adding
    # anchors here is an addition INSIDE a drawn component and the inventory
    # recommends it (F11) — but it would repaint the bar, and this run's whole
    # purpose is a side-by-side match Mide signs off. Raised in the report
    # instead of taken unilaterally.
    top = ('<nav class="ks3-railbar" data-rail="top" aria-label="Lesson progress">'
           '<div class="ks3-railbar-row">'
           '<span class="ks3-railbar-count" data-rail-count>0 / %d</span>'
           '<span class="ks3-railbar-label" data-rail-label>%s</span>'
           '<span class="ks3-railbar-track">'
           '<span class="ks3-railbar-fill" data-rail-fill></span>'
           '</span></div></nav>'
           % (len(stages), t(stages[0].get("label", ""))))

    payload = json.dumps([{"anchor": s["anchor"],
                           "label": s.get("label", ""),
                           "done_when": s.get("done_when", "")}
                          for s in stages], separators=(",", ":"),
                         sort_keys=True)
    return ('<div class="ks3-rails" data-rail-stages="%s">%s%s</div>'
            % (e(payload), side, top))


# ── pages ────────────────────────────────────────────────────────────────

def ks4_bridge_href(link):
    return "/%s/%s/%s.html" % (KS4_BRIDGE_PATHWAY, KS4_BRIDGE_TIER, link)


def lesson_page(unit, lesson, registry, units_by_code):
    disc = unit["discipline"]
    base = "/ks3/%s/%s" % (disc, unit["slug"])
    # ⊕ MRB-208 rule 1: on a LESSON page the trail lives in the header bar and
    # the separate `.ks3-crumbs` row is gone. Every other page type still calls
    # crumbs() — the ruling was scoped to lessons and nothing else moved.
    trail = header_trail([("KS3", "/ks3/index.html"),
                          (DISCIPLINE_TITLES[disc], "/ks3/%s/index.html" % disc),
                          (unit["title"], base + "/index.html"),
                          (lesson["title"], None)])

    head = ['<header class="ks3-lesson-head">',
            '<p class="ks3-eyebrow">%s · %s</p>'
            % (t(unit["title"]), e(family_label(lesson["family"]))),
            "<h1>%s</h1>" % t(lesson["title"])]
    if lesson.get("big_question"):
        head.append('<p class="ks3-bigq">%s</p>' % t(lesson["big_question"]))
    # ⊕ MRB-221 (Mide, 16 Aug 2026) — the under-review marker is GONE. The
    # content has been reviewed, architecture §5.10.1's carve-out is revoked,
    # and publishing is no longer conditioned on `review_state`. Nothing is
    # emitted here now, and nothing should be added back: the assertion that
    # used to demand the marker went in the same commit.
    head.append("</header>")

    # §4's block order, inside the 60rem lesson column. Core blocks are DIRECT
    # children of .ks3-lesson so `.ks3-lesson > .ks3-explainer` can cap prose
    # at 46rem — see r_explainer.
    body = ['<div class="ks3-lesson">', "".join(head),
            render_blocks(lesson, lesson.get("core", []))]

    body.append(r_layer(lesson, lesson.get("stretch") or [],
                        "ks3-stretch", "Going further"))
    # R12 — `support` is present-but-empty by design until the support layer is
    # authored (§11 decision 4), and empty renders NOTHING AT ALL: no section,
    # no heading, no rule, no placeholder. The dashed frame in Design's
    # reference set exists only there. The slot is never absent from the data;
    # it is simply never a hole in the page.
    body.append(r_layer(lesson, lesson.get("support") or [],
                        "ks3-support", "Need a hand?"))

    # Prerequisites (§4.9) — student-facing use of the graph.
    prereqs = []
    for slug in lesson.get("requires", []):
        r = registry.get(slug)
        if not r:
            continue
        prereqs.append('<li><a href="/ks3/%s/%s/%s.html">%s %s</a></li>'
                       % (e(r["_disc"]), e(r["_unit_slug"]), e(r["slug"]),
                          t(r["title"]), MARK_ARROW))

    # Cross-discipline references (§4.6) — must render gracefully BEFORE the
    # referenced unit exists. This is a §9 slice gate.
    #
    # ⊕ A reference may be a bare lesson SLUG as well as a `{unit, lesson, why}`
    # record. §4.6 frames the field as cross-discipline reuse, where naming the
    # unit is the whole point — but Design's approved B1 endmatter cards point at
    # SAME-UNIT lessons, and a same-unit pointer has no unit to name. Rather than
    # make six lessons repeat their own unit code, a string is read as "a lesson
    # in this unit". The dict form is unchanged and stays required the moment a
    # reference crosses a unit boundary.
    connects = []
    for r in lesson.get("references") or []:
        if isinstance(r, str):
            r = {"unit": unit["code"], "lesson": r}
        tgt_unit = units_by_code.get(r["unit"])
        tgt = registry.get(r["lesson"])
        why = ('<p>%s</p>' % t(r["why"])) if r.get("why") else ""
        # ⊕ MRB-228 — an authored `label` overrides the target's own title.
        #
        # The card printed the TARGET's title, always. Usually right and
        # occasionally wrong in a way only the referring lesson can see: b2-04
        # points at P4's `moments` slot, whose title is "Moments: the turning
        # effect", and b2-04 is the one lesson in the key stage where the word
        # `moment` is barred. So the page carried it twice — once in the
        # endmatter's permitted forward-reference to GCSE, and once here, where
        # nobody had chosen it. Design's own label for the card is "Physics:
        # Forces", and it was being discarded.
        #
        # The reference is an edge and the label is a property OF THE EDGE, not
        # of either end: how this lesson names that one. Defaulting to the
        # target's title keeps every existing card byte-identical.
        label = r.get("label") or (tgt["title"] if tgt else r["lesson"])
        if tgt_unit and tgt and tgt.get("authored"):
            connects.append(
                '<li><a href="/ks3/%s/%s/%s.html">%s %s</a>%s</li>'
                % (e(tgt_unit["discipline"]), e(tgt_unit["slug"]),
                   e(r["lesson"]), t(label), MARK_ARROW, why))
        else:
            unit_title = tgt_unit["title"] if tgt_unit else r["unit"]
            connects.append(
                '<li><span class="ks3-pending">%s <em>(%s — coming soon)</em>'
                '</span>%s</li>' % (t(label), t(unit_title), why))

    # KS4 bridge (§4.7).
    ks4 = ['<li><a href="%s">%s %s</a></li>'
           % (e(ks4_bridge_href(l)), t(l.split("/")[-1].replace("-", " ")),
              MARK_ARROW)
           for l in lesson.get("ks4_links") or []]

    # ⊕ §4.8.1 D — two prose slots that fill a card the generator used to omit.
    # `before_this` speaks only when there are no prerequisites ("Nothing —
    # this is where the unit starts."), `ks4_becomes` only when there is no KS4
    # page to point at yet. Neither ever competes with the real list: an empty
    # card is a promise the lesson did not make, and a card carrying BOTH prose
    # and links would say the same thing twice.
    if not prereqs and lesson.get("before_this"):
        prereqs = ['<li><span class="ks3-endmatter-prose">%s</span></li>'
                   % t(lesson["before_this"])]
    if not ks4 and lesson.get("ks4_becomes"):
        ks4 = ['<li><span class="ks3-endmatter-prose">%s</span></li>'
               % t(lesson["ks4_becomes"])]

    # ⊕ MRB-220 — the middle card's heading is authorable. It was fixed at
    # "Connects to", which is right for B1's sideways links and wrong for
    # Design's B2 pages: all four head it **"Next in this unit"** and point
    # FORWARD at the next lesson. A fixed heading would have rendered a card
    # Design did not draw over content Design did draw. The default is
    # unchanged, so no shipped lesson moves.
    body.append(r_endmatter([("Before this lesson", prereqs),
                             (lesson.get("connects_heading") or "Connects to",
                              connects),
                             ("At GCSE this becomes", ks4)],
                            tutor=lesson.get("tutor")))
    # ⊕ §4.8.1 D — the lesson-specific safety line sits ALONGSIDE the standing
    # legal line, never instead of it. b1-01's is "Never light a candle to test
    # this at home without an adult with you."
    if lesson.get("safety_note"):
        body.append('<p class="ks3-legal ks3-safety">%s</p>'
                    % t(lesson["safety_note"]))
    # ⊕ MRB-228 — the CONVENTION line, and it is not the safety line.
    #
    # b2-04's foot reads "Weight in newtons is taken as mass in kilograms ×
    # 10 N/kg throughout." That is a measurement convention scoped to the whole
    # page, and there was nowhere to put it: the only lesson-level foot slot was
    # `safety_note`, which ships `class="ks3-safety"`. Routing it there would
    # have printed a units convention in the treatment reserved for "never light
    # a candle without an adult", which devalues the safety line every time a
    # lesson needs a convention — and b2-04's author correctly refused to, and
    # dropped the sentence instead.
    #
    # Dropping it is the wrong outcome. The convention is load-bearing: g = 10
    # is stated inside two worked steps, and "throughout" is what tells a
    # student the same assumption holds in the rung they are about to attempt.
    #
    # Plain `ks3-legal`, no modifier — it reads as what it is, a note about how
    # the numbers on this page were taken. Ordered before the standing legal
    # line for the same reason `safety_note` is: page-specific first, standing
    # text last.
    if lesson.get("convention_note"):
        body.append('<p class="ks3-legal">%s</p>'
                    % t(lesson["convention_note"]))
    body.append(LEGAL_LINE)
    body.append("</div>")

    return shell(lesson["title"], "\n".join(x for x in body if x), "", disc,
                 lesson.get("big_question", ""),
                 lesson_slug=lesson["slug"],
                 trail_html=trail, rail_html=r_rail(lesson))


def coming_soon_page(unit, lesson):
    """An honest placeholder. Structure-first — never a broken link (§11 dec 8)."""
    disc = unit["discipline"]
    base = "/ks3/%s/%s" % (disc, unit["slug"])
    crumb = crumbs([("KS3", "/ks3/index.html"),
                    (DISCIPLINE_TITLES[disc], "/ks3/%s/index.html" % disc),
                    (unit["title"], base + "/index.html"),
                    (lesson["title"], None)])
    body = """<div class="ks3-lesson">
<header class="ks3-lesson-head">
  <p class="ks3-eyebrow">%s · %s</p>
  <h1>%s</h1>
</header>
<section class="ks3-block ks3-coming-soon">
  <p class="ks3-tag">Coming soon</p>
  <p>This lesson has not been written yet.</p>
  <p><a href="%s/index.html">Back to %s</a></p>
</section>
</div>""" % (t(unit["title"]), e(family_label(lesson["family"])),
             t(lesson["title"]), e(base), t(unit["title"]))
    return shell(lesson["title"], body, crumb, disc,
                 "%s — coming soon" % lesson["title"],
                 lesson_slug=lesson["slug"])


def unit_index(unit, units_by_code, registry):
    disc = unit["discipline"]
    crumb = crumbs([("KS3", "/ks3/index.html"),
                    (DISCIPLINE_TITLES[disc], "/ks3/%s/index.html" % disc),
                    (unit["title"], None)])

    # Rows come from lesson_row(), the same renderer every browse page uses.
    # §4.6's reference pointer has two render sites and they must never end up
    # saying different things about the same slot; the surest way to guarantee
    # that is for there to be one of them.
    rows = "".join(lesson_row(unit, l, i, units_by_code)
                   for i, l in enumerate(unit["lessons"], 1))

    # ⛔ The "Why this is its own unit:" note was REMOVED here 2026-08-07 —
    # MRB-181, architecture.md §8.10. Its text ("Eight statutory bullets
    # spanning representation, reaction types and acid chemistry; universally
    # taught as separate units and too large to schedule as one") is a
    # curriculum-design argument addressed to a curriculum designer, printed
    # at the top of a unit page a Year 8 student opens to find lessons.
    # `split_rationale` stays in structure.py: §4.3 requires the record, and
    # keeping it is what lets the decision be reviewed. It just stops being
    # rendered.
    intro = ('<p class="ks3-intro">%s</p>' % t(unit["intro"])) if unit.get("intro") else ""

    body = """<header class="ks3-unit-head">
  <p class="ks3-eyebrow">%s · %s</p>
  <h1>%s</h1>
  %s
  <p class="ks3-meta">%d of %d lessons written · statutory area: %s</p>
</header>
<ol class="ks3-lesson-list">%s</ol>""" % (
        e(DISCIPLINE_TITLES[disc]), e(unit["code"]), t(unit["title"]), intro,
        unit["authored_count"], len(unit["lessons"]), t(unit["statutory_area"]),
        rows)
    return shell(unit["title"], body, crumb, disc, unit.get("intro") or unit["title"])


def discipline_hub(disc, units):
    crumb = crumbs([("KS3", "/ks3/index.html"),
                    (DISCIPLINE_TITLES[disc], None)])
    cards = []
    for u in units:
        done = u["authored_count"]
        total = len(u["lessons"])
        cards.append(
            '<li class="ks3-unit-card"><a href="/ks3/%s/%s/index.html">'
            '<span class="ks3-code">%s</span><h2>%s</h2>'
            '<p class="ks3-meta">%d of %d lessons</p></a></li>'
            % (e(disc), e(u["slug"]), e(u["code"]), t(u["title"]), done, total))
    # ⚠️ No year here. This page sits under /ks3/<discipline>/, which is the
    # lesson tree — §4.5's prohibition covers every byte of it, and the intro
    # used to read "N units across Years 7 to 9". The year route says that,
    # legally, on /ks3/index.html and the browse pages.
    body = """<header class="ks3-hub-head">
  <h1>KS3 %s</h1>
  <p class="ks3-intro">%d units, built lesson by lesson.</p>
</header>
<ul class="ks3-unit-grid">%s</ul>""" % (
        e(DISCIPLINE_TITLES[disc]), len(units), "".join(cards))
    return shell("KS3 %s" % DISCIPLINE_TITLES[disc], body, crumb, disc)


# ── the browse layer (§4.5.2) ────────────────────────────────────────────
#
# Year → half term → subject → lessons. These are index pages and nothing else:
# they link to lesson pages that already exist at their existing URLs, and they
# are the ONLY place in the KS3 tree where a year or a half term is allowed to
# appear. §4.5's prohibition is split, not relaxed — a lesson page still carries
# neither, in its path or in its bytes.
#
# Everything below is a pure projection of half_terms.derive(). Change the
# sequence and these pages change; nothing else does. That is the property §9's
# reorder proof tests, and it is what makes a browse layer legal here at all.

# ⛔ THE BROWSE-LAYER HONESTY CALLOUT — REMOVED 2026-08-07 on Mide's ruling,
# MRB-181; the rule it now falls under is architecture.md §8.10.
# The paragraph that used to live here opened every browse page with a large
# callout explaining how MrBadmusAI works out its teaching order. It was
# written to a teacher, on pages read almost entirely by students, it answered
# a question nobody had asked, and it took the prime slot above the cards the
# page exists to show. The sequencing rationale is architecture, and it lives
# in architecture.md §4.5.1 — which is where a reader who wants it looks.
# §4.5.2's "labelled as such on the page" clause is amended accordingly: the
# obligation is that the page never CLAIMS to be a school's own scheme, and
# nothing on it does. The constant and all four of its render sites are gone,
# not stubbed to "" — a stub leaves the plumbing behind and invites the next
# person to refill it.


def season_of(half_term):
    """`autumn` / `spring` / `summer`, read off the half-term slug.

    Derived rather than tabulated so there is no second list to keep in step
    with half_terms.py — `autumn-1` is already the season and the index.
    """
    return half_term_slug(half_term).split("-", 1)[0]


def browse_slots(units):
    """``(year, half_term, discipline) → [(unit, lesson, position_in_unit), …]``.

    **Keyed on (unit_code, lesson_slug), never on the slug alone.** There are
    183 lesson slots and 182 distinct slugs: `energy-in-food` is declared twice
    — once in B3 as a §4.6 reference slot, once in P2 as the lesson itself — and
    a slug-keyed lookup silently drops one of them into the wrong year.

    `position_in_unit` is the lesson's number within its whole unit, not within
    the half term, so a unit sliced across a half-term boundary shows as
    "lessons 4 to 7 of C6" rather than restarting at 1. Half_terms.py treats
    unit coherence as a tie-break rather than a rule, so slicing is expected and
    the numbering should make it legible instead of hiding it.
    """
    slots = {}
    for u in units:
        for i, l in enumerate(u["lessons"], 1):
            slots[(u["code"], l["slug"])] = (u, l, i)

    out = {}
    for (year, half_term), keys in slots_by_year_half_term().items():
        for key in keys:
            u, l, i = slots[key]
            out.setdefault((year, half_term, u["discipline"]), []).append((u, l, i))
    return out


def _entries(browse, year, half_term=None, discipline=None):
    """Flat list of slot records matching the filter, in teaching order."""
    out = []
    for (y, ht, disc), rows in sorted(browse.items()):
        if y != year:
            continue
        if half_term is not None and ht != half_term:
            continue
        if discipline is not None and disc != discipline:
            continue
        out.extend(rows)
    return out


def _counts(entries):
    """(units, lessons) for a set of slot records."""
    return len({u["code"] for u, _l, _i in entries}), len(entries)


def _plural(n, word):
    return "%d %s%s" % (n, word, "" if n == 1 else "s")


def lesson_row(unit, lesson, position, units_by_code):
    """One lesson row, in the bordered list. §7's four row states.

    Shared by the unit index and every browse page. Links to the lesson's
    EXISTING page — the browse layer never mints a lesson URL; if it did,
    §4.5.2's whole justification would collapse.

    Every state carries a WORD as well as a colour (R2), so the list survives
    being printed in greyscale: "Draft", "Coming soon", "Taught in …".
    """
    if lesson.get("reference_to"):
        # §4.6 single-source: link to the OWNER's page, with the pointer both
        # render sites share. WHERE, never WHEN — see REF_POINTER.
        owner = units_by_code.get(lesson["reference_to"])
        href = ("/ks3/%s/%s/%s.html"
                % (owner["discipline"], owner["slug"], lesson["slug"])
                if owner else "#")
        owner_disc = DISCIPLINE_TITLES[owner["discipline"]] if owner else ""
        return (('<li class="ks3-lesson-row is-ref"><span class="ks3-num">%d</span>'
                 '<a href="%s">%s</a>' + REF_BADGE + REF_POINTER + '</li>')
                % (position, e(href), t(lesson["title"]), e(owner_disc),
                   e(lesson["reference_to"]), e(owner_disc),
                   t(owner["title"]) if owner else ""))

    href = "/ks3/%s/%s/%s.html" % (unit["discipline"], unit["slug"], lesson["slug"])
    if not lesson["authored"]:
        # Structure-first (§11 decision 8) — the slot is routable and honest.
        # The row dims, but it stays a real link to a real placeholder page: a
        # row that looks like a link and does nothing is worse than a page that
        # says "not written yet".
        state = " is-soon"
        badge = '<span class="ks3-badge is-soon">Coming soon</span>'
    else:
        # ⊕ MRB-221 — the `is-draft` badge is gone with the page marker it
        # mirrored at list size. An authored row now carries no badge at all.
        state = ""
        badge = ""
    return ('<li class="ks3-lesson-row%s"><span class="ks3-num">%d</span>'
            '<a href="%s">%s</a>'
            '<span class="ks3-family">%s</span>%s</li>'
            % (state, position, e(href), t(lesson["title"]),
               e(family_label(lesson["family"])), badge))


SEASON_TITLES = {"autumn": "Autumn", "spring": "Spring", "summer": "Summer"}


def _seasons_of_year():
    """`[(season, [half_term, …]), …]` in teaching order, derived.

    Read off `season_of()` rather than tabulated, so a change to the slugs in
    half_terms.py moves the rows here instead of leaving a stale second copy.
    """
    order = []
    groups = {}
    for ht in HALF_TERMS:
        s = season_of(ht)
        if s not in groups:
            groups[s] = []
            order.append(s)
        groups[s].append(ht)
    return [(s, groups[s]) for s in order]


def _units_in(browse, year, half_term):
    """`[(discipline, unit_title), …]` for one half term, in teaching order.

    Deduplicated because a unit contributes one ROW however many of its lessons
    land in the half term, and ordered by discipline so the three colours always
    appear top to bottom in the same order.
    """
    out = []
    for d in DISCIPLINES:
        for u, _l, _i in browse.get((year, half_term, d), []):
            if (d, u["title"]) not in out:
                out.append((d, u["title"]))
    return out


def year_index(year, browse):
    """/ks3/year-<n>/index.html — the six half terms of one year.

    Laid out as THREE SEASON ROWS (MRB-182), not a flat 2×3 grid: a school year
    is three terms, each two half terms, and a sticky season tile down the left
    is what makes "which term is this?" answerable while scrolling.

    Each card lists the UNIT NAMES taught in that half term, one row per unit.
    It used to print "Biology 3 · Chemistry 4 · Physics 3", which told a student
    how MUCH was coming without ever saying WHAT — the one question the page
    exists to answer. A half term may carry four units, or two in one science;
    the list is derived, so it renders however many there actually are.
    """
    crumb = crumbs([("KS3", "/ks3/index.html"), ("Year %d" % year, None)])

    rows = []
    for season, hts in _seasons_of_year():
        season_lessons = sum(len(_entries(browse, year, ht)) for ht in hts)
        cards = []
        for ht in hts:
            units_n, lessons_n = _counts(_entries(browse, year, ht))
            unit_rows = "".join(
                '<li data-discipline="%s">'
                '<span class="ks3-ht-dot" aria-hidden="true"></span>'
                '<span>%s</span></li>' % (e(d), t(title))
                for d, title in _units_in(browse, year, ht))
            # .ks3-code is the 46px season-coloured number tile; the heading
            # carries the name. Layer C of the parity gate reads the tile's
            # background off this exact selector, so the class stays.
            cards.append(
                '<li class="ks3-unit-card ks3-browse-ht" data-season="%s">'
                '<a href="/ks3/year-%d/%s/index.html">'
                '<span class="ks3-ht-head"><span class="ks3-code">%d</span>'
                '<span class="ks3-ht-name">%s</span></span>'
                '<span class="ks3-meta">%s · %s</span>'
                '<ul class="ks3-ht-units">%s</ul></a></li>'
                % (e(season), year, e(half_term_slug(ht)), ht,
                   e(half_term_name(ht)), e(_plural(lessons_n, "lesson")),
                   e(_plural(units_n, "unit")), unit_rows))

        rows.append(
            '<div class="ks3-season-row" data-season="%s">'
            '<div class="ks3-season-side"><div class="ks3-season-tile">'
            '<p class="ks3-season-name">%s</p>'
            '<p class="ks3-season-meta">Half terms %s · %s</p></div></div>'
            '<ul class="ks3-ht-grid">%s</ul></div>'
            % (e(season), e(SEASON_TITLES.get(season, season.title())),
               e(" & ".join(str(h) for h in hts)),
               e(_plural(season_lessons, "lesson")), "".join(cards)))

    units, lessons = _counts(_entries(browse, year))
    body = """<header class="ks3-landing-head ks3-browse-head">
  <div>
    <p class="ks3-eyebrow">Key Stage 3</p>
    <h1>Year %(year)d</h1>
    <p class="ks3-intro">%(lessons)s across %(units)s, split into the six half
       terms of the school year. Pick a half term to see what each science
       covers.</p>
  </div>
  <div class="ks3-stat-row">
    <div class="ks3-stat"><span class="ks3-stat-n">%(nlessons)d</span><span class="ks3-stat-l">lessons</span></div>
    <div class="ks3-stat"><span class="ks3-stat-n">%(nunits)d</span><span class="ks3-stat-l">units</span></div>
    <div class="ks3-stat"><span class="ks3-stat-n">%(nhts)d</span><span class="ks3-stat-l">half terms</span></div>
  </div>
</header>
<section class="ks3-season-rows">%(rows)s</section>
<p class="ks3-browse-alt"><a href="/ks3/index.html">Browse by subject instead %(arrow)s</a></p>""" % {
        "year": year,
        "lessons": e(_plural(lessons, "lesson")),
        "units": e(_plural(units, "unit")),
        "nlessons": lessons,
        "nunits": units,
        "nhts": len(HALF_TERMS),
        "rows": "".join(rows),
        "arrow": MARK_ARROW,
    }
    return shell("Year %d Science" % year, body, crumb, None,
                 "KS3 Year %d Science — the MrBadmusAI default sequence, half "
                 "term by half term." % year,
                 footer_links=[("Year %d" % year,
                                "/ks3/year-%d/index.html" % year)],
                 main_class="is-browse")


def half_term_index(year, half_term, browse):
    """/ks3/year-<n>/<half-term>/index.html — the sciences in one half term.

    Each subject card now names its UNIT and lists that unit's lessons, rather
    than reporting a bare count. The stat panel takes the page's own season
    colour — Design drew it orange because it drew half term 1, and a green
    spring page wearing an autumn panel would undo the whole point of colouring
    the browse layer by term.

    **Both states of a card are a real link.** Design's prototype renders a card
    with nothing authored as an inert div, and that would strand every
    coming-soon page in the half term: `/ks3/year-7/autumn-1/biology/index.html`
    is a real, generated, routable page and the card is its only route in.
    Structure-first (§11 decision 8) and R15 both point the same way, and §3d's
    lesson rows already resolve the identical tension by staying links in both
    states. The card's WORDS still carry the difference (R2) — "Open these four
    lessons" against "Lessons being written".
    """
    slug = half_term_slug(half_term)
    name = half_term_name(half_term)
    season = season_of(half_term)
    crumb = crumbs([("KS3", "/ks3/index.html"),
                    ("Year %d" % year, "/ks3/year-%d/index.html" % year),
                    (name, None)])

    cards = []
    splits = []
    for disc in DISCIPLINES:
        rows = browse.get((year, half_term, disc), [])
        if not rows:
            # half_terms.py guarantees all three sciences in every half term,
            # and asserts it at import. Rendering only what is present anyway
            # costs one line and means a future exemption degrades to a missing
            # card rather than a crash.
            continue
        units_n, lessons_n = _counts(rows)
        splits.append((disc, lessons_n))

        # Consecutive grouping — a half term may carry more than one unit of a
        # science, and each gets its own eyebrow, title and list in sequence.
        groups = []
        for u, l, i in rows:
            if not groups or groups[-1][0]["code"] != u["code"]:
                groups.append((u, []))
            groups[-1][1].append((l, i))

        blocks = []
        for u, lessons in groups:
            items = "".join(
                '<li%s><span class="ks3-ht-n">%02d</span><span>%s</span></li>'
                % (' class="is-live"' if l["authored"] else "", i, t(l["title"]))
                for l, i in lessons)
            blocks.append(
                '<div class="ks3-ht-unit">'
                '<p class="ks3-eyebrow">Unit %s · %s</p>'
                '<p class="ks3-ht-unit-title">%s</p>'
                '<ol class="ks3-ht-lessons">%s</ol></div>'
                % (e(u["code"]), e(_plural(len(lessons), "lesson")),
                   t(u["title"]), items))

        live = sum(1 for _u, l, _i in rows if l["authored"])
        if live:
            cta = ('<span class="ks3-browse-cta">Open these %s lessons %s</span>'
                   % (e(_count_word(lessons_n)), MARK_ARROW))
        else:
            cta = '<span class="ks3-ht-soon">Lessons being written</span>'

        # data-discipline is what sets --ks3-hue, which colours the dot and the
        # card's offset shadow. Without it all three cards look identical.
        cards.append(
            '<li class="ks3-unit-card ks3-browse-subject" data-discipline="%s">'
            '<a href="/ks3/year-%d/%s/%s/index.html">'
            '<span class="ks3-browse-subject-head">'
            '<span class="ks3-browse-dot" aria-hidden="true"></span>'
            '<h2>%s</h2></span>%s%s</a></li>'
            % (e(disc), year, e(slug), e(disc), e(DISCIPLINE_TITLES[disc]),
               "".join(blocks), cta))

    units, lessons = _counts(_entries(browse, year, half_term))

    # The proportional bar: each subject's flex-grow IS its lesson count, so
    # the row is the split rather than a picture of it.
    bar = "".join('<span data-discipline="%s" style="flex:%d"></span>'
                  % (e(d), n) for d, n in splits)
    split_line = " · ".join("%s %d" % (DISCIPLINE_TITLES[d], n) for d, n in splits)

    body = """<header class="ks3-landing-head ks3-browse-head" data-season="%(season)s">
  <div>
    <p class="ks3-eyebrow">Year %(year)d · Half term %(ht)d</p>
    <h1>%(name)s</h1>
    <p class="ks3-intro">%(lessons)s across %(units)s. Pick a science to see the
       lessons.</p>
  </div>
  <div class="ks3-ht-panel">
    <p class="ks3-ht-panel-n">%(nlessons)d</p>
    <p class="ks3-ht-panel-l">lessons across %(units)s</p>
    <div class="ks3-ht-bar">%(bar)s</div>
    <p class="ks3-ht-panel-split">%(split)s</p>
  </div>
</header>
<ul class="ks3-unit-grid is-browse">%(cards)s</ul>
<p class="ks3-browse-alt"><a href="/ks3/year-%(year)d/index.html">Back to all six half terms of Year %(year)d</a></p>""" % {
        "season": e(season),
        "year": year,
        "ht": half_term,
        "name": e(name),
        "lessons": e(_plural(lessons, "lesson")),
        "units": e(_plural(units, "unit")),
        "nlessons": lessons,
        "bar": bar,
        "split": e(split_line),
        "cards": "".join(cards),
    }
    return shell("%s · Year %d" % (name, year), body, crumb, None,
                 "KS3 Year %d, %s — the MrBadmusAI default sequence."
                 % (year, name),
                 footer_links=[("Year %d" % year,
                                "/ks3/year-%d/index.html" % year)],
                 main_class="is-browse")


VOCAB_CAP = 8


def _later_this_year(browse, year, half_term, unit_code):
    """`(half_term, [(lesson, position), …])` for the rest of a unit, or None.

    Where the same unit's remaining lessons return LATER in the same year.
    Derived from the placement, never authored — §4.5 forbids page text being a
    function of the sequence for a LESSON page, but this is a browse page and
    §4.5.2 makes it the rendered sequence, so it must move when the sequence
    does. Returns the earliest half term the unit resumes in, and everything
    placed from that point on.
    """
    out = []
    first = None
    for ht in HALF_TERMS:
        if ht <= half_term:
            continue
        for (y, h, _d), entries in browse.items():
            if y != year or h != ht:
                continue
            for u, l, i in entries:
                if u["code"] == unit_code:
                    if first is None:
                        first = ht
                    out.append((l, i))
    if not out:
        return None
    out.sort(key=lambda p: p[1])
    return (first, out)


def half_term_discipline_index(year, half_term, disc, browse, units_by_code):
    """/ks3/year-<n>/<half-term>/<discipline>/index.html — the lessons placed there.

    A numbered timeline down the left, a sticky aside on the right. Every row is
    a real link in BOTH states: an unwritten lesson still has a real page saying
    so, and `lesson_row()`'s contract — never mint a lesson URL, never dead-end
    a student — is the same one honoured here (§11 decision 8).

    ⚠️ THE SPINE HAS NO PER-LESSON BLURB AND NO UNIT "by the end you can…".
    Both lines are therefore CONDITIONAL, never invented:
      · the description falls back to `big_question`, which only an authored
        lesson has, and is OMITTED otherwise;
      · the panel's closing line uses the unit's `intro`, which today only C1
        has, and is OMITTED otherwise.
    Writing a plausible sentence for the other 177 slots would be the generator
    inventing science, which is the one thing it must never do.
    """
    slug = half_term_slug(half_term)
    name = half_term_name(half_term)
    crumb = crumbs([("KS3", "/ks3/index.html"),
                    ("Year %d" % year, "/ks3/year-%d/index.html" % year),
                    (name, "/ks3/year-%d/%s/index.html" % (year, slug)),
                    (DISCIPLINE_TITLES[disc], None)])

    rows = browse.get((year, half_term, disc), [])

    # Consecutive grouping, not a dict: the entries already arrive in teaching
    # order, and a unit that genuinely appears twice in one half term should
    # render twice rather than be silently merged.
    groups = []
    for u, l, i in rows:
        if not groups or groups[-1][0]["code"] != u["code"]:
            groups.append((u, []))
        groups[-1][1].append((l, i))

    # ── the dark unit panel(s), one per unit in this slice ──
    panels = []
    for u, lessons in groups:
        span = ("lesson %d" % lessons[0][1] if len(lessons) == 1
                else "lessons %d to %d" % (lessons[0][1], lessons[-1][1]))
        intro = ('<p class="ks3-unit-panel-intro">%s</p>' % t(u["intro"])
                 if u.get("intro") else "")
        panels.append(
            '<div class="ks3-unit-panel">'
            '<p class="ks3-eyebrow">Unit %s · %s of %d</p>'
            '<p class="ks3-unit-panel-title">'
            '<a href="/ks3/%s/%s/index.html">%s</a></p>%s</div>'
            % (e(u["code"]), e(span), len(u["lessons"]),
               e(disc), e(u["slug"]), t(u["title"]), intro))

    # ── the timeline ──
    timeline = []
    for u, lessons in groups:
        for l, i in lessons:
            href = ("/ks3/%s/%s/%s.html"
                    % (u["discipline"], u["slug"], l["slug"]))
            if l.get("reference_to"):
                owner = units_by_code.get(l["reference_to"])
                if owner:
                    href = ("/ks3/%s/%s/%s.html"
                            % (owner["discipline"], owner["slug"], l["slug"]))
            live = bool(l["authored"])
            # No blurb exists for an unwritten slot. The row simply has one
            # fewer line rather than a fabricated one.
            blurb = ('<span class="ks3-tl-blurb">%s</span>' % t(l["big_question"])
                     if live and l.get("big_question") else "")
            cta = ('<span class="ks3-browse-cta">Open this lesson %s</span>'
                   % MARK_ARROW) if live else \
                  '<span class="ks3-tl-soon">Being written</span>'
            timeline.append(
                '<li class="ks3-tl-row"%s>'
                '<a href="%s">'
                '<span class="ks3-tl-node">%02d</span>'
                '<span class="ks3-tl-card">'
                '<span class="ks3-tl-head">'
                '<span class="ks3-tl-title">%s</span>'
                '<span class="ks3-family">%s</span></span>'
                '%s%s</span></a></li>'
                % (' data-live="1"' if live else "", e(href), i,
                   t(l["title"]), e(family_label(l["family"])), blurb, cta))

    # ── aside 1: the words this unit gives you ──
    # Aggregated from the AUTHORED lessons in THIS slice only, in order,
    # deduplicated, capped. An empty list means no box at all — an empty
    # bordered panel headed "Words this unit gives you" is worse than silence.
    terms = []
    for u, lessons in groups:
        for l, _i in lessons:
            for v in (l.get("vocabulary") or []):
                term = v.get("term")
                if term and term not in terms:
                    terms.append(term)
    vocab_box = ""
    if terms:
        chips = "".join('<span class="ks3-term">%s</span>' % t(x)
                        for x in terms[:VOCAB_CAP])
        vocab_box = ('<div class="ks3-aside-box ks3-aside-words">'
                     '<h3>Words this unit gives you</h3>'
                     '<div class="ks3-terms">%s</div></div>' % chips)

    # ── aside 2: later this year ──
    later_boxes = []
    for u, _lessons in groups:
        later = _later_this_year(browse, year, half_term, u["code"])
        if not later:
            continue
        ht_next, rest = later
        n = len(rest)
        line = ("The last %s lesson%s of %s come%s back in Half term %d."
                % (_count_word(n), "" if n == 1 else "s", e(u["code"]),
                   "s" if n == 1 else "", ht_next))
        items = "".join(
            '<li><span class="ks3-tl-n">%02d</span><span>%s</span></li>'
            % (i, t(l["title"])) for l, i in rest)
        later_boxes.append(
            '<div class="ks3-aside-box ks3-aside-later">'
            '<h3>Later this year</h3>'
            '<p class="ks3-aside-line">%s</p>'
            '<ul class="ks3-later-list">%s</ul></div>' % (line, items))

    aside = ""
    if vocab_box or later_boxes:
        aside = ('<aside class="ks3-unit-aside">%s%s</aside>'
                 % (vocab_box, "".join(later_boxes)))

    units, lessons = _counts(rows)
    body = """<header class="ks3-landing-head ks3-browse-head">
  <div>
    <p class="ks3-eyebrow">Year %(year)d · %(name)s</p>
    <h1 class="ks3-h1-dotted"><span class="ks3-subject-dot" aria-hidden="true"></span>%(disc)s</h1>
    <p class="ks3-intro">%(lessons)s from %(units)s.</p>
  </div>
  <div class="ks3-unit-panels">%(panels)s</div>
</header>
<section class="ks3-unit-body">
  <ol class="ks3-timeline">%(timeline)s</ol>
  %(aside)s
</section>
<p class="ks3-browse-alt"><a href="/ks3/year-%(year)d/%(slug)s/index.html">Back to all three sciences this half term</a>
   <a href="/ks3/%(dslug)s/index.html">The whole KS3 %(disc)s course %(arrow)s</a></p>""" % {
        "year": year,
        "name": e(name),
        "disc": e(DISCIPLINE_TITLES[disc]),
        "dslug": e(disc),
        "slug": e(slug),
        "lessons": e(_plural(lessons, "lesson")),
        "units": e(_plural(units, "unit")),
        "panels": "".join(panels),
        "timeline": "".join(timeline),
        "aside": aside,
        "arrow": MARK_ARROW,
    }
    return shell("%s · %s · Year %d" % (DISCIPLINE_TITLES[disc], name, year),
                 body, crumb, disc,
                 "KS3 Year %d %s, %s — the MrBadmusAI default sequence."
                 % (year, DISCIPLINE_TITLES[disc], name),
                 footer_links=[("Year %d" % year,
                                "/ks3/year-%d/index.html" % year),
                               (DISCIPLINE_TITLES[disc],
                                "/ks3/%s/index.html" % disc)],
                 main_class="is-browse")


def lesson_picker(units):
    """MRB-212 — the hub's primary CTA is a disclosure, not a fixed link.

    "Try a lesson: Gas pressure" named one lesson forever. A student who had
    already done it was sent back to it; a student who had done four was sent
    to the one they were least likely to want. The picker asks the browser what
    it knows instead.

    **PROGRESSIVE ENHANCEMENT, and the fallback is the honest one.** Every
    published lesson is emitted here as a real `<a>` inside `<li data-slug>`,
    all of them in "Start something new", which is exactly right for a browser
    with no visit history — including one with JS off, where that is the final
    state. `ks3.js` then MOVES rows into "Pick up where you left off" from
    `ks3_visits` and hides whichever group ends up empty. R15's "every control
    is a real control" is satisfied by construction: these are links.

    **Only `authored` lessons may appear.** A "being written" slot has a real
    page, but sending a student who asked to *do a lesson* to a placeholder is
    the one thing this control must never do. Today that is exactly six.

    ⚠️ No explanatory copy anywhere in the panel (MRB-181, §8.10). Two headings
    and the lessons. Nothing about how any of it is remembered.
    """
    rows = []
    for u in units:
        for l in u["lessons"]:
            if not l["authored"]:
                continue
            rows.append(
                '<li data-slug="%s"><a href="/ks3/%s/%s/%s.html">'
                '<span class="ks3-picker-title">%s</span>'
                '<span class="ks3-picker-unit">%s</span></a></li>'
                % (e(l["slug"]), e(u["discipline"]), e(u["slug"]), e(l["slug"]),
                   t(l["title"]), t(u["title"])))
    if not rows:
        return ""

    return ("""<div class="ks3-picker">
      <button type="button" class="ks3-btn is-primary ks3-picker-btn"
              id="ks3-picker-btn" aria-expanded="false"
              aria-controls="ks3-picker-panel">Jump back in %(caret)s</button>
      <div class="ks3-picker-panel" id="ks3-picker-panel" hidden>
        <section class="ks3-picker-group" data-group="resume" hidden>
          <p class="ks3-eyebrow">Pick up where you left off</p>
          <ul class="ks3-picker-list"></ul>
        </section>
        <section class="ks3-picker-group" data-group="new">
          <p class="ks3-eyebrow">Start something new</p>
          <ul class="ks3-picker-list">%(rows)s</ul>
        </section>
      </div>
    </div>""" % {"caret": MARK_CARET, "rows": "".join(rows)})


# Design's three year blurbs, verbatim from the browse-layer artifact. These
# are the one thing on a year card that is NOT derived, and correctly so: a
# count is a fact about the sequence and must follow it, whereas "the biggest
# year of KS3" is a sentence somebody wrote. Keyed by year so a fourth year
# could never silently inherit Year 9's description.
YEAR_BLURBS = {
    7: "Cells, particles, forces and motion — the foundations everything else "
       "sits on.",
    8: "Reactions, body systems, electricity and waves. The biggest year of KS3.",
    9: "Inheritance, the periodic table and energy — the run-up to GCSE.",
}

# The yellow swash under "poke at". Design draws it as a stroked path rather
# than an underline so it overshoots the word at both ends the way a highlighter
# does. `preserveAspectRatio="none"` is what lets one 300-unit path stretch to
# whatever width the words happen to take.
HERO_SWASH = (
    '<svg class="ks3-swash" viewBox="0 0 300 22" preserveAspectRatio="none" '
    'aria-hidden="true">'
    '<path d="M4 14C60 5 120 18 176 9C224 2 268 12 296 7"/></svg>')


def landing(units, browse):
    """/ks3/index.html — both routes in (§8.4).

    Leads with the year route because that is how a teacher and a Year 8 student
    both actually think ("what am I doing this term?"). The subject route is
    kept, unchanged and clearly labelled, because §11 decision 2 ruled
    disciplinary structure with integrated navigation and §4.5.2 is explicit
    that the browse layer is an additional way in, not a migration.

    ⚠️ EVERY NUMBER ON THIS PAGE IS DERIVED (MRB-182). Design's prototype was
    drawn before MRB-199 dropped two lessons and its counts are all one or two
    out — 185 total, 55 in Year 7, 60 in Biology. None of them are copied here.
    verify_ks3.py check 6b re-runs the build with a mutated sequence and asserts
    these pages change, so a hardcoded number fails the build rather than
    quietly lying to a student about how much course there is.
    """
    crumb = crumbs([("KS3", None)])

    total_lessons = sum(len(u["lessons"]) for u in units)
    total_done = sum(u["authored_count"] for u in units)

    # ── "Live right now" — one bar per subject ──
    bars = []
    for disc in DISCIPLINES:
        du = [u for u in units if u["discipline"] == disc]
        done = sum(u["authored_count"] for u in du)
        total = sum(len(u["lessons"]) for u in du)
        # A bar at zero keeps a 2% stub so the track still reads as a track
        # rather than as an empty strip. The stub is shape, not a claim: the
        # honest count sits in words directly above it ("0 of 58"), which is
        # the R2 signal.
        pct = max(2, int(round(done * 100.0 / total))) if total else 2
        bars.append(
            '<div class="ks3-live-row" data-discipline="%s">'
            '<div class="ks3-live-label"><span>%s</span>'
            '<span class="ks3-live-of">%d of %d</span></div>'
            '<div class="ks3-live-track">'
            '<span class="ks3-live-fill" style="width:%d%%"></span></div></div>'
            % (e(disc), e(DISCIPLINE_TITLES[disc]), done, total, pct))

    if total_done == 0:
        live_line = "The first lessons are on their way."
    else:
        live_line = ("%s lesson%s %s finished. The rest are on their way."
                     % (_count_word(total_done).capitalize(),
                        "" if total_done == 1 else "s",
                        "is" if total_done == 1 else "are"))

    # ── year cards ──
    years = []
    for year in YEARS:
        units_n, lessons_n = _counts(_entries(browse, year))
        # The six season chips are DERIVED from season_of() over HALF_TERMS,
        # not six hardcoded spans: if half_terms.py ever renamed or re-paired a
        # season the strip would follow it instead of going quietly wrong. The
        # second half term of each season carries `data-late`, which is what
        # dims it to Design's .62.
        seen = {}
        chips = []
        for ht in HALF_TERMS:
            s = season_of(ht)
            seen[s] = seen.get(s, 0) + 1
            chips.append('<span data-season="%s"%s></span>'
                         % (e(s), ' data-late="1"' if seen[s] > 1 else ""))
        years.append(
            '<li class="ks3-unit-card ks3-browse-year" data-year="%d">'
            '<a href="/ks3/year-%d/index.html">'
            '<div class="ks3-year-top"><h2>Year %d</h2>'
            '<span class="ks3-year-tile" aria-hidden="true">%d</span></div>'
            '<p class="ks3-meta">%s · %s</p>'
            '<p class="ks3-year-blurb">%s</p>'
            '<span class="ks3-browse-strip" aria-hidden="true">%s</span>'
            '<span class="ks3-browse-cta">Browse the six half terms %s</span>'
            '</a></li>'
            % (year, year, year, year,
               e(_plural(units_n, "unit")), e(_plural(lessons_n, "lesson")),
               t(YEAR_BLURBS[year]), "".join(chips), MARK_ARROW))

    # ── subject cards ──
    # .ks3-browse-subject is what supplies --ks3-hue: the dot, the offset
    # shadow and the card tint all read from it. Biology green, Chemistry
    # orange, Physics blue — the same three hues the half-term cards use, so a
    # student learns one mapping and not two.
    secs = []
    for disc in DISCIPLINES:
        du = [u for u in units if u["discipline"] == disc]
        done = sum(u["authored_count"] for u in du)
        total = sum(len(u["lessons"]) for u in du)
        live = ('<span class="ks3-hub-live"> · %d live</span>' % done) if done else ""
        secs.append(
            '<li class="ks3-hub-subject ks3-browse-subject" data-discipline="%s">'
            '<a href="/ks3/%s/index.html">'
            '<div class="ks3-browse-subject-head">'
            '<span class="ks3-browse-dot" aria-hidden="true"></span>'
            '<h3>%s</h3></div>'
            '<p class="ks3-hub-subject-meta">%s · %s%s</p>'
            '<p class="ks3-hub-subject-units">%s</p>'
            '</a></li>'
            % (e(disc), e(disc), e(DISCIPLINE_TITLES[disc]),
               e(_plural(len(du), "unit")), e(_plural(total, "lesson")), live,
               t(" · ".join(u["title"] for u in du))))

    body = """<section class="ks3-hub-top">
  <div class="ks3-hub-hero">
    <p class="ks3-eyebrow">Key Stage 3 · Years 7 to 9</p>
    <h1 class="ks3-hub-title">Science you<br/>get to <span class="ks3-hero-mark">poke at%(swash)s</span></h1>
    <p class="ks3-hub-sub">Biology, Chemistry and Physics for Years 7, 8 and 9 —
       built lesson by lesson, with something to press on every page.</p>
    <div class="ks3-hub-actions">%(primary)s
      <a class="ks3-btn" href="/ks3/year-7/index.html">Start with Year 7</a>
    </div>
  </div>
  <div class="ks3-live">
    <div class="ks3-live-head">
      <p class="ks3-eyebrow">Live right now</p>
      <span class="ks3-live-count">%(done)d / %(total)d</span>
    </div>
    <p class="ks3-live-line">%(liveline)s</p>
    <div class="ks3-live-bars">%(bars)s</div>
  </div>
</section>

<section class="ks3-hub-sec">
  <div class="ks3-sec-head">
    <h2>Pick your year</h2>
    <p>Each year is split into the six half terms of the school year, with all
       three sciences running side by side.</p>
  </div>
  <ul class="ks3-unit-grid is-browse">%(years)s</ul>
</section>

<section class="ks3-hub-sec">
  <div class="ks3-sec-head">
    <h2>Or go by subject</h2>
    <p>Same lessons, same pages — ordered by how the science builds up instead
       of by school term.</p>
  </div>
  <ul class="ks3-unit-grid is-browse">%(subjects)s</ul>
</section>""" % {
        "swash": HERO_SWASH,
        "primary": lesson_picker(units),
        "done": total_done,
        "total": total_lessons,
        "liveline": t(live_line),
        "bars": "".join(bars),
        "years": "".join(years),
        "subjects": "".join(secs),
    }
    return shell("KS3 Science", body, crumb, None,
                 "Free KS3 Science revision — Years 7 to 9, all three sciences.",
                 main_class="is-browse is-hub")


# ── validation (§9 gates) ────────────────────────────────────────────────

def validate(units, registry):
    """Fail loudly. §4.9: a cycle is a build-blocking defect."""
    problems = []

    # 1. Prerequisite graph must be acyclic.
    graph = {s: [r for r in (l.get("requires") or []) if r in registry]
             for s, l in registry.items()}
    WHITE, GREY, BLACK = 0, 1, 2
    colour = {n: WHITE for n in graph}

    def visit(n, stack):
        colour[n] = GREY
        for m in graph.get(n, []):
            if colour.get(m) == GREY:
                problems.append("PREREQUISITE CYCLE: %s" % " → ".join(stack + [m]))
                return
            if colour.get(m) == WHITE:
                visit(m, stack + [m])
        colour[n] = BLACK

    for n in sorted(graph):
        if colour[n] == WHITE:
            visit(n, [n])

    # 2. `requires` must point at lessons that exist.
    for slug, l in sorted(registry.items()):
        for r in l.get("requires") or []:
            if r not in registry:
                problems.append("UNKNOWN PREREQUISITE: %s requires %r" % (slug, r))

    # 3. Every authored lesson has non-empty `covers` (§10.2) — unless it
    #    carries §7.6's declared exemption. The exemption is never quietly
    #    relaxed rules; it is the OTHER legal shape, all three legs enforced:
    #    `beyond_statutory: True`, `covers` EMPTY (a beyond-statutory lesson
    #    that owns a statement is a contradiction and a build failure, §7.6
    #    rule 2), and `ks4_links` non-empty (rule 3 — a beyond-statutory
    #    lesson pointing nowhere is just off-spec content; resolution is
    #    checked by check_ks4_links as for every lesson). First exercised by
    #    B1's stem-cells-and-meristems and enzymes-and-rate (MRB-199).
    for slug, l in sorted(registry.items()):
        if not l.get("authored"):
            continue
        if l.get("beyond_statutory"):
            if l.get("covers"):
                problems.append(
                    "BEYOND-STATUTORY LESSON OWNS A STATEMENT: %s declares "
                    "beyond_statutory yet covers %s — §7.6 rule 2 says covers "
                    "MUST be empty; off-spec content never enters the "
                    "coverage register" % (slug, l["covers"]))
            if not l.get("ks4_links"):
                problems.append(
                    "BEYOND-STATUTORY LESSON POINTS NOWHERE: %s has no "
                    "ks4_links — §7.6 rule 3 requires at least one, or it is "
                    "just off-spec content" % slug)
        elif not l.get("covers"):
            problems.append("EMPTY COVERS: %s (§10.2 requires non-empty)" % slug)

    # 4. Exactly-once ownership over subject-content statements/clauses (§4.4
    #    rule 3). WS statements are exempt (§5.7).
    owners = {}
    for slug, l in sorted(registry.items()):
        for c in l.get("covers") or []:
            if c.startswith("KS3.WS."):
                continue
            owners.setdefault(c, []).append(slug)
    for stmt, who in sorted(owners.items()):
        if len(who) > 1:
            problems.append("DOUBLE-OWNED: %s owned by %s" % (stmt, ", ".join(who)))

    # 5. A parent and its own sub-ID must not both be owned.
    subs = all_sub_ids()
    for stmt in sorted(owners):
        if stmt in subs and parent_of(stmt) in owners:
            problems.append(
                "PARENT AND CLAUSE BOTH OWNED: %s and %s" % (parent_of(stmt), stmt))

    # 6. Authored lessons must declare misconceptions (Law 3, §10.2).
    for slug, l in sorted(registry.items()):
        if l.get("authored") and not l.get("misconceptions"):
            problems.append("NO MISCONCEPTIONS: %s (Law 3 makes these required)" % slug)

    # 7. `support` key must be present even when empty (§11 decision 4).
    for slug, l in sorted(registry.items()):
        if l.get("authored") and "support" not in l:
            problems.append(
                "MISSING SUPPORT SLOT: %s (empty is allowed, absent is a defect)" % slug)

    # 8. Referenced slots must name a real unit.
    codes = {u["code"] for u in units}
    for u in units:
        for l in u["lessons"]:
            if l.get("reference_to") and l["reference_to"] not in codes:
                problems.append("BAD REFERENCE: %s/%s → unknown unit %s"
                                % (u["code"], l["slug"], l["reference_to"]))

    return problems


def check_ks4_links(units, repo_root="."):
    """`ks4_links` must resolve to a real KS4 page (§9 gate)."""
    missing = []
    for u in units:
        for l in u["lessons"]:
            for link in l.get("ks4_links") or []:
                rel = ks4_bridge_href(link).lstrip("/")
                if not os.path.exists(os.path.join(repo_root, rel)):
                    missing.append("%s → %s" % (l["slug"], rel))
    return missing


# ── diagram manifest (§4.10, conflict 1h) ────────────────────────────────

def diagram_manifest(units):
    rows = []
    for u in units:
        for l in u["lessons"]:
            for f in l.get("figures") or []:
                rows.append((u["code"], l["slug"], f["id"], f.get("kind", ""),
                             f.get("status", "needed"), f.get("caption", "")))
    rows.sort()
    by_status = {}
    for r in rows:
        by_status[r[4]] = by_status.get(r[4], 0) + 1

    out = ["# KS3 diagram manifest\n",
           "**Generated file — do not hand-edit.** Produced by `build_ks3.py` from the "
           "`figures` field on each lesson record. Regenerate with `python3 build_ks3.py`.\n",
           "architecture.md §4.10, added on Mide's ruling of 2026-07-26 (§11 conflict 1h, "
           "ADOPT). MRB-103 caught this gap: the lesson record had nowhere to declare a "
           "diagram, so a missing asset could only be discovered at build time. Every "
           "figure a lesson declares appears here as a tracked sourcing task.\n",
           "## ⚠️ Schematic, not photographic\n",
           "A **Platform Backlog ticket already exists for real-life photography across all "
           "subjects.** The KS3 diagram need recorded here is **related but distinct**.\n",
           "- These are **schematic** assets: particle arrangements, ray diagrams, circuit "
           "diagrams, field lines, labelled biological structures.\n"
           "- A photograph does **not** substitute for one. A photograph of a beaker does not "
           "do the job of a particle diagram.\n"
           "- **Do not merge the two sourcing efforts.** Satisfying the photography ticket "
           "will not satisfy this manifest, and vice versa.\n",
           "MRB-103 also flagged an **anatomical/structural diagram gap** (cells, organs) and "
           "put it on the critical path. That gap is real and lands in Biology B1; it is one "
           "of the reasons C1 rather than B1 is the vertical slice (§11 conflict 1a).\n",
           "## Status counts\n",
           "| Status | Figures |", "|---|---|"]
    for s in sorted(by_status):
        out.append("| `%s` | %d |" % (s, by_status[s]))
    out.append("| **Total** | **%d** |\n" % len(rows))
    out.append("`needed` = declared by a lesson, not yet drawn. A lesson may ship with "
               "figures at `needed` — it is not a build blocker — but the need is then "
               "counted here rather than invisible.\n")
    out.append("## Figures\n")
    out.append("| Unit | Lesson | Figure ID | Kind | Status | Caption |")
    out.append("|---|---|---|---|---|---|")
    for code, slug, fid, kind, status, cap in rows:
        out.append("| %s | `%s` | `%s` | %s | `%s` | %s |"
                   % (code, slug, fid, kind, status, cap))
    out.append("")
    return "\n".join(out)


# ── build ────────────────────────────────────────────────────────────────

def build_ks3(output_dir=OUT_ROOT, mirror_to_root=True, repo_root="."):
    units = ks3_data.build_units()
    registry = ks3_data.lesson_registry(units)
    units_by_code = {u["code"]: u for u in units}

    # Registry entries need their discipline for prerequisite hrefs.
    for slug, l in registry.items():
        l["_disc"] = units_by_code[l["_unit"]]["discipline"]

    print("🧪 build_ks3 — %d units, %d lesson slots, %d authored"
          % (len(units), sum(len(u["lessons"]) for u in units),
             sum(u["authored_count"] for u in units)))

    problems = validate(units, registry)
    if problems:
        print("\n❌ BUILD FAILED — %d problem(s):\n" % len(problems))
        for p in problems:
            print("   • %s" % p)
        raise SystemExit(1)
    print("  ✅ validation passed (acyclic graph, exactly-once coverage, Law 3, "
          "support slots, references)")

    missing = check_ks4_links(units, repo_root)
    if missing:
        print("  ⚠️  ks4_links that do not resolve:")
        for m in missing:
            print("       %s" % m)
    else:
        print("  ✅ every ks4_links edge resolves to a real KS4 page")

    ks3_out = os.path.join(output_dir, KS3_DIR)
    if os.path.exists(ks3_out):
        shutil.rmtree(ks3_out)
    os.makedirs(ks3_out)

    # Stamped at write time rather than in a second pass over the tree: a page
    # is never briefly on disk unstamped, and there is no walk to keep in sync
    # with what write() produces.
    versions = asset_versions(repo_root)

    def write(relpath, content):
        full = os.path.join(ks3_out, relpath)
        os.makedirs(os.path.dirname(full), exist_ok=True)
        with open(full, "w", encoding="utf-8") as f:
            f.write(stamp_versions(content, versions))

    browse = browse_slots(units)

    n = 0
    write("index.html", landing(units, browse))
    n += 1
    for disc in ("biology", "chemistry", "physics"):
        du = [u for u in units if u["discipline"] == disc]
        write("%s/index.html" % disc, discipline_hub(disc, du))
        n += 1
        for u in du:
            write("%s/%s/index.html" % (disc, u["slug"]),
                  unit_index(u, units_by_code, registry))
            n += 1
            for l in u["lessons"]:
                if l.get("reference_to"):
                    continue          # §4.6 — the owner renders it, not us
                page = (lesson_page(u, l, registry, units_by_code)
                        if l["authored"] else coming_soon_page(u, l))
                write("%s/%s/%s.html" % (disc, u["slug"], l["slug"]), page)
                n += 1
    lesson_tree = n

    # ── the browse layer (§4.5.2) ────────────────────────────────────────
    # Index pages only. Every href above is a lesson URL that already exists and
    # is untouched by anything below; year and half term reach these paths and
    # go no further. They go through the same write(), so they carry the same
    # cache-bust stamps — there is exactly one stamping pass in this generator.
    browse_pages = 0
    for year in YEARS:
        write("year-%d/index.html" % year, year_index(year, browse))
        browse_pages += 1
        for ht in HALF_TERMS:
            slug = half_term_slug(ht)
            write("year-%d/%s/index.html" % (year, slug),
                  half_term_index(year, ht, browse))
            browse_pages += 1
            for disc in DISCIPLINES:
                if not browse.get((year, ht, disc)):
                    continue
                write("year-%d/%s/%s/index.html" % (year, slug, disc),
                      half_term_discipline_index(year, ht, disc, browse,
                                                 units_by_code))
                browse_pages += 1
    n += browse_pages
    placed = sum(len(v) for v in browse.values())
    print("  ✅ wrote %d pages → %s/  (%d lesson tree + %d browse layer)"
          % (n, ks3_out, lesson_tree, browse_pages))
    print("  ✅ browse layer covers %d lesson slots across %d years"
          % (placed, len(YEARS)))

    # Shared assets. Cloudflare serves from mrbadmus_site/, so a KS3 page that
    # links /shared/ks3.css gets a 404 unless the file is copied there.
    #
    # Only these three are touched. tokens.css IS shared with KS4, but the KS3
    # change is purely additive inside the existing [data-mode="ks3"] block,
    # which no KS4 page matches — so KS4 rendering cannot change.
    shared_src = os.path.join(repo_root, "shared")
    shared_dst = os.path.join(output_dir, "shared")
    os.makedirs(shared_dst, exist_ok=True)
    for asset in ("ks3.css", "ks3.js", "tokens.css"):
        src = os.path.join(shared_src, asset)
        if os.path.exists(src):
            shutil.copy2(src, os.path.join(shared_dst, asset))
    print("  ✅ synced shared assets (ks3.css, ks3.js, tokens.css)")
    print("  ✅ cache-bust: stamped %d pages — %s" % (n, versions))

    with open(os.path.join(repo_root, "docs", "ks3", "diagram-manifest.md"),
              "w", encoding="utf-8") as f:
        f.write(diagram_manifest(units))
    print("  ✅ wrote docs/ks3/diagram-manifest.md")

    if mirror_to_root:
        root_ks3 = os.path.join(repo_root, KS3_DIR)
        if os.path.exists(root_ks3):
            shutil.rmtree(root_ks3)
        shutil.copytree(ks3_out, root_ks3)
        print("  ✅ mirrored → %s/" % root_ks3)

    return n


# ── wiring this into the main generator, when that becomes worth it ──────
#
# generate_site_v5.build_site() rebuilds and overwrites the entire site. Adding
#
#     from build_ks3 import build_ks3
#     build_ks3(output_dir=output_dir)
#
# near the end of build_site() would produce KS3 as part of the normal build.
# It is deliberately NOT done here: doing so makes "zero KS4 pages changed"
# unprovable during Phase 1, because every KS3 run would rewrite every KS4 page.
# Revisit once C1 is reviewed and the KS3 tree is stable.

if __name__ == "__main__":
    build_ks3()
