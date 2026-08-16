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


def r_fit_parts(a, act_id):
    """⊕ Build four real cells from one parts list, then run them.

    "Which parts" becomes a consequence of "what job". Rendered as an empty
    section. The parts list is `parts_from` — it names the bench's activity, so
    the two instruments share one list and a part cannot exist in the builder
    and not on the bench.
    """
    specimens = a.get("specimens") or []
    if not specimens:
        raise ValueError("fit-parts %r declares no specimens[]." % act_id)
    for sp in specimens:
        if not sp.get("needs"):
            raise ValueError(
                "fit-parts %r specimen %r needs no parts at all — there would "
                "be nothing to get right." % (act_id, sp.get("id")))

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
            "unit": a.get("progress_unit", "cells run"),
            "installed": a.get("install_unit", "installed"),
        },
        "verdicts": a.get("verdicts") or {},
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
#
# No letters here on purpose: the dict shape has always rendered "Formula",
# never "F · Formula", and this migration is not the place to restyle a shipped
# page. The list shape carries its own letters because Design authored them.
_FIFA_DICT_STEPS = (("formula", "Formula"), ("insert", "Insert"),
                    ("fix", "Fix"), ("answer", "Answer"))


def r_fifa(fifa, staged=False, buttons=None):
    """FIFA, in either authored shape (⊕ §4.8.2's one breaking change).

    §4.8.2 turns `activities[].fifa` from a dict of four fixed keys into a LIST
    of `{letter, name, line, note}`, so a worked example can name its own steps
    ("Fine-tune", not "Fix") and hang a teaching note on each — which MRB-204
    step 3 needs and four flat strings have nowhere to put.

    BOTH SHAPES RENDER, and that is a deliberate choice over migrating the one
    record still on the old shape (C1's `mass-fifa`). `ks3_data/` is owned by
    another agent this session and editing it would be a collision; and a
    renderer that accepts both is worth having anyway, because the old shape is
    a strict subset of the new one — it is the new one with the letters and
    names implied and no notes. Normalising here means there is exactly one
    piece of markup, not two that are free to diverge.

    ⚠️ The STAGED reveal is not built here. §4.8.2 moves the worked answer out
    of `.ks3-fifa` into the `worked-example` block's stepper, which is b1-02's
    task; until it lands, every step renders at once, exactly as the dict shape
    always did. That is the status quo rather than a regression — but it means
    b1-02's worked example currently shows its answer without asking, and the
    stepper is what fixes that.
    """
    if isinstance(fifa, dict):
        steps = [{"name": name, "line": fifa.get(key)}
                 for key, name in _FIFA_DICT_STEPS]
    else:
        steps = list(fifa or [])

    out = []
    for i, s in enumerate(steps):
        # The letter is chrome and the name is the label; a step with neither
        # would render a bare line with nothing saying which step it is.
        label = " · ".join(x for x in (s.get("letter"), s.get("name")) if x)
        note = ('<span class="ks3-fifa-note">%s</span>' % rich(s["note"])
                if s.get("note") else "")
        out.append('<p class="ks3-fifa-step"%s><strong>%s</strong> %s%s</p>'
                   % (' hidden data-step="%d"' % i if staged else "",
                      t(label), t(s.get("line")), note))
    if not staged:
        return '<div class="ks3-fifa">%s</div>' % "".join(out)
    b = buttons or {}
    return ('<div class="ks3-fifa ks3-fifa-staged" data-stepper '
            'data-total="%d" data-next="%s" data-done="%s">%s'
            '<button type="button" class="ks3-reveal-btn ks3-step-next" '
            'data-step-next>%s</button></div>'
            % (len(out), e(b.get("next", "Show the next step")),
               e(b.get("done", "All steps shown")), "".join(out),
               t(b.get("first", "Show the first step"))))


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

    Two shapes because Design authored two. b2-01/02/03 count ("3 of 6
    decided"); b2-04's rig and meter blocks are booleans ("Meter not fitted
    yet" → "Meter fitted"). One element, one JS updater, so a third variant
    cannot arrive as a third copy of the same paragraph.
    """
    if spec.get("format"):
        total = int(spec.get("total") or 0)
        first = spec["format"].replace("{n}", "0").replace("{total}", str(total))
        return ('<p class="ks3-blockhead-count" data-count data-format="%s" '
                'data-total="%d">%s</p>'
                % (e(spec["format"]), total, t(first)))
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
                        ("<h2>%s</h2>" % t(a["heading"])) if a.get("heading")
                        else "",
                        _head_counter(hc)))
        prompt_tag = "p"
    else:
        parts.append('<p class="ks3-eyebrow">%s</p>' % t(eyebrow))

    # ⊕ §4.8.2 — an explicit `heading` beside the prompt. The `check` shell
    # promotes the PROMPT to the block's <h2>, which works while a block has
    # only one of the two. Design's instruments carry both a title and a line
    # of instruction under it, and without this the title would be lost.
    if a.get("heading") and not hc:
        parts.append("<h2>%s</h2>" % t(a["heading"]))
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

    if kind == "test-board":
        parts.append(r_test_board(a, act_id))
    if kind == "sort-rows":
        parts.append(r_sort_rows(a, act_id))
    if kind == "settles-it":
        parts.append(r_settles_it(a, act_id))
    if kind == "critique-steps":
        parts.append(r_critique_steps(a, act_id))
    if kind == "fifa-construct":
        parts.append(r_fifa_construct(lesson, a, act_id))
    if kind == "cell-bench":
        parts.append(r_cell_bench(a, act_id))
    if kind == "sort-pairs":
        parts.append(r_sort_pairs(a, act_id))
    if kind == "fit-parts":
        parts.append(r_fit_parts(a, act_id))
    if kind == "zoom-ladder":
        parts.append(r_zoom_ladder(a, act_id))
    if kind == "sort-task":
        parts.append(r_sort_task(a, act_id))
    if kind == "removal-cases":
        parts.append(r_removal_cases(a, act_id))
    if kind == "system-bench":
        parts.append(r_system_bench(a, act_id))
    if kind == "sabotage":
        parts.append(r_sabotage(lesson, a, act_id))
    if kind == "job-sort":
        parts.append(r_job_sort(a, act_id))
    if kind == "system-switch":
        parts.append(r_system_switch(a, act_id))
    if kind == "joint-bench":
        parts.append(r_joint_bench(a, act_id))
    if kind == "muscle-pair":
        parts.append(r_muscle_pair(a, act_id))
    if a.get("scorecards"):
        parts.append(r_scorecards(a["scorecards"]))

    if a.get("options"):
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
    if a.get("reveal"):
        # Law 4: the reveal is gated behind the student's commitment.
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
# lesson missing one rung shows 1 · Recall, 3 · Explain, 4 · Produce — a gap
# rather than a renumbering, because "3 · Explain" is the rung's name and a
# student comparing two lessons should find the same name in both.
#
# The middle dot is U+00B7, which IS in the latin subset. The circled digits
# this used to use (U+2460–2463) are not, and rendered as tofu inside a
# Bricolage-800 heading.
LADDER_RUNGS = (("recall", 1, "Recall"), ("apply", 2, "Apply"),
                ("explain", 3, "Explain"), ("produce", 4, "Produce"))

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
            '<h3 tabindex="-1">%d · %s</h3>'
            '<p class="ks3-rung-q">%s</p>'
            '<ul class="ks3-options" role="list">%s</ul>'
            '</div>'
            % (e(key), num, e(name), t(q.get("q", "")), "".join(opts)))


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
            '<h3 tabindex="-1">%d · %s</h3>'
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
            % (e(key), num, e(name), t(q.get("q", "")), e(aid),
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
    return ('<section class="ks3-formula"%s>'
            '<div class="ks3-formula-statement"><p>%s</p></div>%s</section>'
            % (_id_attr(block), t(block.get("statement", "")), tri))


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
    if lesson.get("review_state") != "frozen":
        # The dot before the text is a ::before in ks3.css. Do not emit a glyph.
        head.append('<p class="ks3-review-flag">Draft — not yet '
                    'science-reviewed.</p>')
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
        if tgt_unit and tgt and tgt.get("authored"):
            connects.append(
                '<li><a href="/ks3/%s/%s/%s.html">%s %s</a>%s</li>'
                % (e(tgt_unit["discipline"]), e(tgt_unit["slug"]),
                   e(r["lesson"]), t(tgt["title"]), MARK_ARROW, why))
        else:
            label = tgt["title"] if tgt else r["lesson"]
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
    elif lesson.get("review_state") != "frozen":
        # §5.10.1 carve-out: a draft may publish, but only with a visible
        # marker. The lesson page carries `Draft — not yet science-reviewed.`;
        # this is the same fact, at list size, saying the same thing.
        state = ""
        badge = ('<span class="ks3-badge is-draft" title="Draft — not yet '
                 'science-reviewed.">Draft</span>')
    else:
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
