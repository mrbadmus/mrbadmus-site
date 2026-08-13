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
NAV_BRAND = (
    '<a class="ks3-brand" href="/index.html">'
    '<span class="ks3-brand-tile" aria-hidden="true">'
    '<svg width="20" height="20" viewBox="0 0 24 24">'
    '<path d="M4 16L12 7l8 9" fill="none" stroke="#FBF3E6" stroke-width="4.6" '
    'stroke-linecap="round" stroke-linejoin="round"/>'
    '</svg></span>MrBadmusAI</a>'
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
          trail_html="", rail_html=""):
    """KS3 page shell. `class="rd"` + `data-mode="ks3"` per §8.5.

    `trail_html` — the inline header trail (lesson pages, MRB-208 rule 1).
    `rail_html`  — both progress-rail variants (lesson pages, MRB-208 rule 2).
    Both are empty on every non-lesson page, which keeps the browse layer and
    the unit indices exactly as they were.
    """
    accent = ("--subject: var(%s);" % SUBJECT_TOKEN[discipline]) if discipline else ""
    divider = ('<span class="ks3-nav-divider" aria-hidden="true"></span>'
               if trail_html else "")
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
<body class="rd" data-mode="ks3"%(style)s>
<nav class="ks3-nav">%(brand)s%(divider)s%(trail)s
  <a class="ks3-nav-link" href="/ks3/index.html">KS3</a>
</nav>
%(rail)s<main class="ks3-main">
%(crumbs)s
%(body)s
</main>
<footer class="ks3-footer">
  <p>MrBadmusAI · Key Stage 3 Science</p>
</footer>
<script src="/shared/ks3.js" defer></script>
</body>
</html>
""" % {
        "title": e(title),
        "desc": e(description or title),
        "style": (' style="%s"' % accent) if accent else "",
        "brand": NAV_BRAND,
        "divider": divider,
        "trail": trail_html,
        "rail": rail_html,
        "crumbs": crumb_html,
        "body": body,
        "preload": FONT_PRELOADS,
    }


# ── segment renderers (§5.1.1 vocabulary) ────────────────────────────────
#
# Every class emitted below has a rule in shared/ks3.css, which is the class
# contract for this generator. A renderer that needs a look the stylesheet does
# not have reaches for an existing class; it does not invent one, because an
# invented class is a silent no-op that looks like styling.

def r_hook(lesson):
    """Block 1 — ink dark. A phenomenon that ends in a commitment (R16)."""
    p = lesson.get("phenomenon") or {}
    return ("""<section class="ks3-block ks3-dark ks3-hook">
  <p class="ks3-eyebrow">Start here</p>
  <h2>%s</h2>
  <p class="ks3-hook-prompt">%s</p>
  <p class="ks3-commit">%s</p>
</section>""" % (t(p.get("title", "")), t(p.get("prompt", "")),
                 t(p.get("commit", ""))))


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
                "specimen", "magnification", "focus", "part")

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
        specimens = sim.get("specimens") or []
        if not specimens:
            raise ValueError(
                "Activity %r declares a microscope sim with no specimens[] — "
                "the specimen selector would be an empty <select>." % act_id)
        unknown_slides = [s for s in specimens if _specimen_kind(s) is None]
        if unknown_slides:
            raise ValueError(
                "Activity %r offers specimen(s) %s that shared/ks3.js has no "
                "slide model for (specimenKind() knows onion / onion-with-"
                "bubbles / cheek / pond). Either name the slide so it "
                "classifies, or teach ks3.js to draw it — a slide that "
                "renders as an empty field of view is a defect."
                % (act_id, ", ".join(repr(s) for s in unknown_slides)))
        extra = ' data-specimens="%s"' % e(json.dumps(
            [str(s) for s in specimens], sort_keys=True))
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


def r_activity(lesson, block_type, act_id):
    """The one activity renderer, with a per-type shell.

    Inner order is prompt → options → cards → sim → fifa → reveal → criteria:
    commit first, then the thing that tests the commitment, then the words that
    settle it. `data-activity` stays on the section because ks3.js walks up to
    it for the Law 4 gate.
    """
    a = _activity(lesson, act_id)
    if not a:
        return ""
    shell_cls, eyebrow, prompt_tag = ACTIVITY_SHELLS[block_type]
    parts = ['<section class="%s" data-activity="%s">' % (shell_cls, e(act_id))]

    if block_type == "misconception":
        parts.append('<div class="ks3-mis-head">'
                     '<span class="ks3-mis-badge" aria-hidden="true">!</span>'
                     '<p class="ks3-eyebrow">%s</p></div>' % e(eyebrow))
        quote = _misconception_quote(lesson, a.get("targets"))
        if quote:
            parts.append('<p class="ks3-mis-quote">“%s”</p>' % t(quote))
    else:
        parts.append('<p class="ks3-eyebrow">%s</p>' % e(eyebrow))

    if a.get("prompt"):
        # ⚠️ A card grid keeps its prompt as prose even in a `check`. The prompt
        # IS R4's declaration ask ("say it, then tap"), and verify_ks3.py's
        # §5.1.2(a) gate reads that ask out of the block's non-hidden <p>
        # elements before the grid. Promoting it to a heading would leave the
        # gate looking at the eyebrow alone and passing or failing on the
        # wording of "Your turn" — a live check silently disarmed.
        tag = "p" if a.get("cards") else prompt_tag
        parts.append("<%s>%s</%s>" % (tag, t(a["prompt"]), tag))

    if a.get("options"):
        parts.append(r_activity_options(a["options"]))
    if a.get("cards"):
        parts.append(r_cards(a["cards"]))
    if a.get("sim"):
        parts.append(r_sim(a["sim"], act_id))
    if a.get("fifa"):
        f = a["fifa"]
        parts.append(
            '<div class="ks3-fifa">'
            '<p><strong>Formula</strong> %s</p><p><strong>Insert</strong> %s</p>'
            '<p><strong>Fix</strong> %s</p><p><strong>Answer</strong> %s</p></div>'
            % (t(f.get("formula")), t(f.get("insert")),
               t(f.get("fix")), t(f.get("answer"))))
    if a.get("reveal"):
        # Law 4: the reveal is gated behind the student's commitment.
        parts.append('<div class="ks3-reveal" hidden data-reveal>%s</div>'
                     % t(a["reveal"]))
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

NUMBER_WORDS = ("no", "one", "two", "three", "four")


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
            '<label class="ks3-answer-label" for="%s">Write your answer</label>'
            '<textarea class="ks3-answer" id="%s" data-answer rows="5"></textarea>'
            '<button type="button" class="ks3-check-btn" data-check '
            'aria-expanded="false">Check my answer</button>'
            '<ul class="ks3-ticks" hidden data-ticks role="list">%s</ul>'
            '<p class="ks3-tally" hidden data-tally role="status"></p>'
            '</div>'
            % (e(key), num, e(name), t(q.get("q", "")), e(aid), e(aid),
               "".join(ticks)))


def r_ladder(lesson):
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

    return ('<section class="ks3-block ks3-ladder" data-lesson="%s">'
            '<div class="ks3-ladder-head">'
            '<div><h2>Mastery ladder</h2>'
            '<p class="ks3-ladder-sub">%s</p></div>'
            '<div class="ks3-ladder-score" aria-live="polite">'
            '<p class="ks3-score" data-score>Not started yet.</p>'
            '<p class="ks3-score-note" data-score-note>%s</p></div>'
            '</div>'
            '<div class="ks3-rungs">%s</div>'
            '</section>'
            % (e(slug), e(sub), e(note), "".join(rungs)))


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
        for kf in lesson.get("key_facts") or []:
            if kf.get("id") == ref:
                merged = dict(kf)
                merged.update({k: v for k, v in block.items()
                               if k not in ("ref", "type")})
                spec = merged
                break
        else:
            raise ValueError("key-fact ref %r matches no key_facts[].id" % ref)
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
    return ('<section class="ks3-formula"%s>'
            '<div class="ks3-formula-statement"><p>%s</p></div></section>'
            % (_id_attr(block), t(block.get("statement", ""))))


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
    "hook": lambda l, b: r_hook(l),
    "key-fact": r_key_fact,
    "rule": r_rule,
    "formula": r_formula,
    "comparison": r_comparison,
    "explainer": r_explainer,
    "figure": r_figure,
    "keyword": r_keyword,
    "quiz": lambda l, b: r_ladder(l),
    # Ink dark, like the hook and the practical — the three blocks that invert.
    # The label stays an <h2>: `.ks3-keynote p` sets 30px display 700 on every
    # paragraph in the block, so an eyebrow here would be swallowed by it.
    "summary": lambda l, b: (
        '<section class="ks3-block ks3-dark ks3-keynote"%s><h2>Key note</h2>'
        '<p>%s</p></section>' % (_id_attr(b), rich(l.get("key_note", "")))),
    "misconception": lambda l, b: r_activity(l, "misconception", b.get("id")),
    "check": lambda l, b: r_activity(l, "check", b.get("id")),
    "worked-example": lambda l, b: r_activity(l, "worked-example", b.get("id")),
    "practical": lambda l, b: r_activity(l, "practical", b.get("id")),
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
    tutor = tutor or {}
    heading = t(tutor.get("prompt") or "Stuck? Ask Mr Badmus AI")
    body = ('<p>Ask anything about this lesson and get it explained another '
            'way.</p>' if not tutor.get("prompt") else "")
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
    connects = []
    for r in lesson.get("references") or []:
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

    body.append(r_endmatter([("Before this lesson", prereqs),
                             ("Connects to", connects),
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
                 "%s — coming soon" % lesson["title"])


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


def year_index(year, browse):
    """/ks3/year-<n>/index.html — the six half terms of one year."""
    crumb = crumbs([("KS3", "/ks3/index.html"), ("Year %d" % year, None)])

    cards = []
    for ht in HALF_TERMS:
        per_disc = [(d, browse.get((year, ht, d), [])) for d in DISCIPLINES]
        entries = [r for _d, rows in per_disc for r in rows]
        units, lessons = _counts(entries)
        split = " · ".join("%s %d" % (DISCIPLINE_TITLES[d], len(rows))
                           for d, rows in per_disc if rows)
        # .ks3-code inside a .ks3-browse-ht card is a 42px square tile, so it
        # holds the NUMBER and the heading holds the name. "Half term 3" in a
        # 42px box was overflowing its own border.
        cards.append(
            '<li class="ks3-unit-card ks3-browse-ht" data-season="%s">'
            '<a href="/ks3/year-%d/%s/index.html">'
            '<span class="ks3-code">%d</span><h2>%s</h2>'
            '<p class="ks3-meta">%s · %s</p>'
            '<p class="ks3-browse-split">%s</p></a></li>'
            % (e(season_of(ht)), year, e(half_term_slug(ht)), ht,
               e(half_term_name(ht)), e(_plural(lessons, "lesson")),
               e(_plural(units, "unit")), e(split)))

    units, lessons = _counts(_entries(browse, year))
    body = """<header class="ks3-landing-head">
  <p class="ks3-eyebrow">Key Stage 3</p>
  <h1>Year %d</h1>
  <p class="ks3-intro">%s across %s, split into the six half terms of the school
     year. Pick a half term to see what each science covers.</p>
</header>
<ul class="ks3-unit-grid">%s</ul>
<p class="ks3-browse-alt"><a href="/ks3/index.html">Browse by subject instead %s</a></p>""" % (
        year, e(_plural(lessons, "lesson")), e(_plural(units, "unit")),
        "".join(cards), MARK_ARROW)
    return shell("Year %d Science" % year, body, crumb, None,
                 "KS3 Year %d Science — the MrBadmusAI default sequence, half "
                 "term by half term." % year)


def half_term_index(year, half_term, browse):
    """/ks3/year-<n>/<half-term>/index.html — the sciences in one half term."""
    slug = half_term_slug(half_term)
    name = half_term_name(half_term)
    crumb = crumbs([("KS3", "/ks3/index.html"),
                    ("Year %d" % year, "/ks3/year-%d/index.html" % year),
                    (name, None)])

    cards = []
    for disc in DISCIPLINES:
        rows = browse.get((year, half_term, disc), [])
        if not rows:
            # half_terms.py guarantees all three sciences in every half term,
            # and asserts it at import. Rendering only what is present anyway
            # costs one line and means a future exemption degrades to a missing
            # card rather than a crash.
            continue
        units, lessons = _counts(rows)
        unit_titles = []
        for u, _l, _i in rows:
            if u["title"] not in unit_titles:
                unit_titles.append(u["title"])
        # data-discipline is what sets --ks3-hue, which colours both the dot and
        # the card's shadow. Without it both fall back to the accent and all
        # three subject cards look identical.
        cards.append(
            '<li class="ks3-unit-card ks3-browse-subject" data-discipline="%s">'
            '<a href="/ks3/year-%d/%s/%s/index.html">'
            '<span class="ks3-browse-subject-head">'
            '<span class="ks3-browse-dot" aria-hidden="true"></span>'
            '<h2>%s</h2></span>'
            '<p class="ks3-meta">%s · %s</p>'
            '<p class="ks3-browse-split">%s</p></a></li>'
            % (e(disc), year, e(slug), e(disc), e(DISCIPLINE_TITLES[disc]),
               e(_plural(lessons, "lesson")), e(_plural(units, "unit")),
               t(" · ".join(unit_titles))))

    units, lessons = _counts(_entries(browse, year, half_term))
    body = """<header class="ks3-landing-head" data-season="%s">
  <p class="ks3-eyebrow">Year %d · Half term %d</p>
  <h1>%s</h1>
  <p class="ks3-intro">%s across %s. Pick a science to see the lessons.</p>
</header>
<ul class="ks3-unit-grid">%s</ul>
<p class="ks3-browse-alt"><a href="/ks3/year-%d/index.html">Back to all six half terms of Year %d</a></p>""" % (
        e(season_of(half_term)), year, half_term, e(name),
        e(_plural(lessons, "lesson")), e(_plural(units, "unit")),
        "".join(cards), year, year)
    return shell("%s · Year %d" % (name, year), body, crumb, None,
                 "KS3 Year %d, %s — the MrBadmusAI default sequence."
                 % (year, name))


def half_term_discipline_index(year, half_term, disc, browse, units_by_code):
    """/ks3/year-<n>/<half-term>/<discipline>/index.html — the lessons placed there."""
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

    sections = []
    for u, lessons in groups:
        items = "".join(lesson_row(u, l, i, units_by_code) for l, i in lessons)
        span = ("lesson %d" % lessons[0][1] if len(lessons) == 1
                else "lessons %d to %d" % (lessons[0][1], lessons[-1][1]))
        sections.append(
            '<section class="ks3-browse-unit">'
            '<p class="ks3-eyebrow">%s · %s of %d</p>'
            '<h2><a href="/ks3/%s/%s/index.html">%s</a></h2>'
            '<ol class="ks3-lesson-list">%s</ol></section>'
            % (e(u["code"]), e(span), len(u["lessons"]),
               e(disc), e(u["slug"]), t(u["title"]), items))

    units, lessons = _counts(rows)
    body = """<header class="ks3-landing-head">
  <p class="ks3-eyebrow">Year %d · %s</p>
  <h1>%s</h1>
  <p class="ks3-intro">%s from %s.</p>
</header>
%s
<p class="ks3-browse-alt"><a href="/ks3/year-%d/%s/index.html">Back to all three sciences this half term</a>
   <a href="/ks3/%s/index.html">The whole KS3 %s course %s</a></p>""" % (
        year, e(name), e(DISCIPLINE_TITLES[disc]),
        e(_plural(lessons, "lesson")), e(_plural(units, "unit")),
        "".join(sections), year, e(slug),
        e(disc), e(DISCIPLINE_TITLES[disc]), MARK_ARROW)
    return shell("%s · %s · Year %d" % (DISCIPLINE_TITLES[disc], name, year),
                 body, crumb, disc,
                 "KS3 Year %d %s, %s — the MrBadmusAI default sequence."
                 % (year, DISCIPLINE_TITLES[disc], name))


def landing(units, browse):
    """/ks3/index.html — both routes in (§8.4).

    Leads with the year route because that is how a teacher and a Year 8 student
    both actually think ("what am I doing this term?"). The subject route is
    kept, unchanged and clearly labelled, because §11 decision 2 ruled
    disciplinary structure with integrated navigation and §4.5.2 is explicit
    that the browse layer is an additional way in, not a migration.
    """
    crumb = crumbs([("KS3", None)])

    years = []
    for year in YEARS:
        units_n, lessons_n = _counts(_entries(browse, year))
        years.append(
            '<li class="ks3-unit-card ks3-browse-year">'
            '<a href="/ks3/year-%d/index.html">'
            '<span class="ks3-code">Key Stage 3</span><h2>Year %d</h2>'
            '<p class="ks3-meta">%s · %s</p>'
            '<span class="ks3-browse-strip" aria-hidden="true">%s</span>'
            '<span class="ks3-browse-cta">Browse by half term %s</span>'
            '</a></li>'
            % (year, year, e(_plural(units_n, "unit")),
               e(_plural(lessons_n, "lesson")),
               "".join('<span data-season="%s"></span>' % e(season_of(ht))
                       for ht in HALF_TERMS),
               MARK_ARROW))

    # The subject cards take .ks3-browse-subject alongside .ks3-disc-card purely
    # for --ks3-hue: it is what gives each card its own subject shadow and its
    # own dot colour. Biology green, Chemistry orange, Physics blue — the same
    # three hues the half-term subject cards use, so a student learns one
    # mapping and not two.
    secs = []
    for disc in ("biology", "chemistry", "physics"):
        du = [u for u in units if u["discipline"] == disc]
        done = sum(u["authored_count"] for u in du)
        total = sum(len(u["lessons"]) for u in du)
        secs.append(
            '<li class="ks3-disc-card ks3-browse-subject" data-discipline="%s">'
            '<a href="/ks3/%s/index.html">'
            '<span class="ks3-browse-subject-head">'
            '<span class="ks3-browse-dot" aria-hidden="true"></span>'
            '<h2>%s</h2></span>'
            '<p class="ks3-meta">%d units · %d of %d lessons written</p>'
            '</a></li>'
            % (e(disc), e(disc), e(DISCIPLINE_TITLES[disc]), len(du), done, total))

    total_lessons = sum(len(u["lessons"]) for u in units)
    total_done = sum(u["authored_count"] for u in units)
    body = """<header class="ks3-landing-head">
  <h1>Key Stage 3 Science</h1>
  <p class="ks3-intro">Years 7 to 9. Biology, Chemistry and Physics — the whole
     national curriculum programme of study, built lesson by lesson.</p>
  <p class="ks3-meta">%d of %d lessons written so far.</p>
</header>
<ul class="ks3-unit-grid">%s</ul>
<section class="ks3-browse-secondary">
  <h2>Prefer to browse by subject?</h2>
  <p class="ks3-intro">Every lesson also sits in its subject and its unit, in
     the order the science builds up. Same lessons, same pages — a different way
     in.</p>
  <ul class="ks3-disc-grid">%s</ul>
</section>""" % (total_done, total_lessons, "".join(years),
                 "".join(secs))
    return shell("KS3 Science", body, crumb, None,
                 "Free KS3 Science revision — Years 7 to 9, all three sciences.")


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
