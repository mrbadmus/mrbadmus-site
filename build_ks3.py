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

import base64
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

import ks3_art
from ks3_art.kit import (
    MARKS,
    MARK_ARROW,
    MARK_CROSS,
    MARK_TICK,
    NUMBER_WORDS,
    OPTION_LETTERS,
    _RICH_OK,
    _RICH_RE,
    _SVG_ACCENT,
    _SVG_ACCENT_TEXT,
    _SVG_ACCENT_TINT,
    _SVG_BAND,
    _SVG_BLUE_TEXT,
    _SVG_BODY,
    _SVG_CARD,
    _SVG_DISPLAY,
    _SVG_GROUND,
    _SVG_INK,
    _SVG_INK_BODY,
    _SVG_INK_FAINT,
    _SVG_INK_GHOST,
    _SVG_INK_MUTED,
    _SVG_INSET,
    _SVG_MIN_LABEL,
    _SVG_MONO,
    _SVG_RULE,
    _SVG_RULE_STRONG,
    _activity,
    _attr_safe,
    _canvas_frame,
    _circle,
    _count_word,
    _data_attrs,
    _dial_block,
    _dials,
    _ellipse,
    _group_digits,
    _js_round,
    _json_attr,
    _label,
    _lever_decimals,
    _lever_num,
    _lever_steps_rig,
    _line,
    _mono,
    _n,
    _need,
    _num,
    _option_li,
    _path,
    _pctnum,
    _placeholders,
    _progress_suffix,
    _rect,
    _self_check,
    _svg_attrs,
    _svg_open,
    _svg_text,
    _verdict_ids,
    _with_suffix,
    e,
    formulae,
    option_letter,
    r_activity_options,
    r_bench_gate,
    rich,
    sci,
    t,
)

# The merged per-unit registry. Loaded HERE, at import, because the module-level
# guards below (`_unfn` / `_unshell`) and `_kinds_taking_lesson()` all read these
# tables before a single page is written — which is the point of them.
_KS3_ART = ks3_art.load()


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
#
# ⊕ MRB-257 · audit 6.2 — `mrbadmus.v2.js` joins the tuple. KS3 lesson pages
# now link the shared chat engine, and it is the asset in this list most likely
# to change: a stale cached copy would hand a student a tutor button that
# throws instead of opening. It is hashed from the SOURCE tree like the rest,
# which is what makes the stamp agree with generate_site_v5.py's — that
# generator hashes its own output copy, and the copy is written verbatim from
# `shared/mrbadmus.v2.js`, so the two hashes are the same eight characters.
VERSIONED_ASSETS = ("tokens.css", "styles.css", "nav.css", "ks3.css", "ks3.js",
                     "class-entry.js", "mrbadmus.v2.js")


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


# ▾ U+25BE is absent from the same five subsets, for the same reason — it is a
# geometric shape, not a letter. Typed into the picker's button it would drop to
# a system font mid-label, inside a 19px/700 Bricolage button, which is exactly
# the defect `.ks3-mark` exists to prevent. Drawn instead. MRB-212.
MARK_CARET = ('<svg class="ks3-mark ks3-mark-caret" viewBox="0 0 24 24" '
              'aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>')


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
# ── §6.9 / §6.8 head metadata (⊕ MRB-257, audit 6.8 6.9 6.10) ────────────
#
# The KS3 tree shipped 70 pages with zero `<link rel="icon">`, zero
# `rel="canonical"` and zero `og:*`. Three separate consequences, one place to
# fix them:
#
#   • the browser's fallback `GET /favicon.ico` was answered with 7,396 bytes
#     of KS4 homepage HTML, once per page, and every KS3 tab in a student's
#     browser was unlabelled;
#   • a lesson pasted into a class Teams chat rendered as a bare URL;
#   • nothing told a search engine which URL is the real one.
#
# ⚠️ THE FAVICON IS THE KS3 MARK, NOT THE KS4 ONE. CLAUDE.md's brand rule gives
# KS3 Claude Design's single bold `#E4572E` chevron (MRB-197, Mide's ruling)
# and KS4 the gold-to-rust TWO-chevron mark. Shipping the KS4 mark on 294 KS3
# pages would be brand drift introduced by the fix. The path below is the same
# `d=` as NAV_BRAND — one chevron, one definition — and it is base64'd rather
# than percent-escaped so there is no question about spaces, `#` or quotes
# surviving into an href.
SITE_ORIGIN = "https://mrbadmus.com"

_FAVICON_SVG = (
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">'
    '<path d="M4 16L12 7l8 9" fill="none" stroke="#E4572E" stroke-width="4.6" '
    'stroke-linecap="round" stroke-linejoin="round"/></svg>')
FAVICON_LINK = (
    '<link rel="icon" type="image/svg+xml" href="data:image/svg+xml;base64,%s"/>'
    % base64.b64encode(_FAVICON_SVG.encode("utf-8")).decode("ascii"))


def canon(path):
    """A site path → the URL Cloudflare Pages actually serves it at.

    ⚠️ NOT the `.html` path the links are written with. Audit 6.10 measured all
    602 internal links as `…​.html` and all 602 as a 308 to the extensionless
    form. A canonical tag pointing at a URL that redirects is a canonical tag
    naming a page that does not exist at that address, which is worse than
    none — so the canonical is the redirect TARGET, self-referencing the URL a
    reader's address bar ends up showing.

        /ks3/biology/cells/index.html  → https://mrbadmus.com/ks3/biology/cells/
        /ks3/biology/cells/x.html      → https://mrbadmus.com/ks3/biology/cells/x
    """
    if path.endswith("/index.html"):
        return SITE_ORIGIN + path[:-len("index.html")]
    if path.endswith(".html"):
        return SITE_ORIGIN + path[:-len(".html")]
    return SITE_ORIGIN + path


# ── the tutor, on a lesson page (⊕ MRB-257, audit 6.2) ───────────────────
#
# THE TUTOR WAS OFFERED 58 TIMES AND REACHED A TUTOR ZERO TIMES. All 58 lessons
# shipped `section.ks3-tutor > a.ks3-tutor-cta`, 58 of 58 hrefs were in-page
# anchors, and no click listener existed anywhere in the key stage. On
# `the-menstrual-cycle` at 390px the CTA scrolled the student 9,768px BACKWARDS
# into a section they had already finished. It is the last thing in every
# lesson and the only thing on the page that looks like help.
#
# This is the markup `MrBadmus.init()` binds to. Three deliberate differences
# from what generate_site_v5.py emits for KS4, each of them a rule rather than
# a preference:
#
# 1. NO `chat-fab`. KS4's floating button draws the TWO-chevron gold-to-rust
#    mark. CLAUDE.md gives KS3 Claude Design's single `#E4572E` chevron
#    (MRB-197, Mide's ruling), and the audit's brand baseline is 82/82 files
#    byte-identical with zero drift. Emitting the KS4 fab on 58 KS3 pages would
#    be brand drift introduced by the fix. The `.ks3-tutor` card at the end of
#    the lesson is the entry point, and it gains `data-open-chat`.
#
# 2. NO SUPABASE CDN, and no profile fetch. `loadStudentSession()` reads the
#    student's NAME out of localStorage — no Supabase needed — and then fetches
#    `science_pathway, tier` from the database. Tier and pathway are GCSE
#    concepts. Feeding them to a KS3 tutor produces "The student is on the
#    Higher tier" about a twelve-year-old who has no tier, which is both wrong
#    and exactly the register KS3 design law forbids. Under `keyStage: "ks3"`
#    the fetch is skipped, so the CDN script is not needed here — which is also
#    one fewer blocking request on the page audit 6.5 measured at 8.96 s.
#
# 3. NO INLINE `onclick`, ANYWHERE. KS4's close button and image-clear button
#    are wired with attributes; `verify_ks3.py`'s "all interactive controls are
#    real buttons" gate asserts `onclick=` appears nowhere in a KS3 lesson, and
#    it is right to. `init()` already binds `.close-btn`; `[data-clear-img]` is
#    the KS3-shaped equivalent for the image row and is bound in the engine.
#
# ⚠️ AND THE MARKS ARE DRAWN, NOT TYPED. KS4 types `✕` and `➤` into these two
# buttons. The five KS3 latin woff2 subsets contain neither U+2715 nor U+2192,
# which is the whole reason MARK_CROSS and MARK_ARROW exist — and the parity
# gate caught the first draft of this markup on all 70 authored lessons, which
# is the gate working exactly as designed. KS4 keeps its characters; its pages
# load a different font stack and are not this generator's business.
#
# ⚠️ `inert` — the overlay is `opacity: 0; pointer-events: none` when closed,
# which hides it from the eye and from the mouse and NOT from the keyboard. A
# text input, a file picker and two buttons would otherwise sit in the tab
# order of every lesson page, invisible. `data-inert-when-closed` is what tells
# the engine to put it back on close; KS4 does not carry the attribute and is
# therefore untouched by the same code.
KS3_CHAT_OVERLAY = """<div class="chat-overlay" id="chatOverlay" inert data-inert-when-closed>
  <div class="chat-modal">
    <div class="chat-head">
      <div class="chat-head-info">
        <h3>Mr. Badmus AI</h3>
        <p id="chat-head-subtitle">KS3 Science Tutor</p>
      </div>
      <button class="close-btn" type="button" aria-label="Close the tutor">%(cross)s</button>
    </div>
    <div class="chat-msgs" id="chatMsgs"></div>
    <div class="img-preview-row" id="imgPreviewRow">
      <img id="imgPreview" src="" alt="preview"/>
      <button type="button" data-clear-img aria-label="Remove the picture">%(cross)s</button>
    </div>
    <div class="chat-input-row" style="max-width:860px;width:100%%;margin:0 auto;padding:0 24px 20px;">
      <label for="imgInput" class="img-btn" title="Add a photo of your work">\U0001F4F7</label>
      <input type="file" id="imgInput" accept="image/*" style="display:none"/>
      <input type="text" id="ci" placeholder="Ask Mr Badmus anything about this lesson"/>
      <button class="chat-send-btn" type="button" aria-label="Send">%(arrow)s</button>
    </div>
  </div>
</div>
""" % {"cross": MARK_CROSS, "arrow": MARK_ARROW}


def tutor_mount(discipline, topic):
    """The overlay, the engine and the one call that binds them.

    ⚠️ THE INIT CALL WAITS FOR `DOMContentLoaded` ON PURPOSE. `mrbadmus.v2.js`
    is `defer`red, and a deferred script executes AFTER the parser reaches
    `</html>` — so an inline `<script>` written straight after it runs FIRST
    and `window.MrBadmus` is not defined yet. Deferred scripts do run before
    `DOMContentLoaded` fires, so the listener is the one ordering that holds.

    The config is `json.dumps`ed rather than interpolated, because a lesson
    title is authored prose and prose contains apostrophes. `<` is escaped
    besides, so a title could never close the script element early.
    """
    cfg = json.dumps({"subject": discipline, "topic": topic,
                      "keyStage": "ks3"}, sort_keys=True)
    cfg = cfg.replace("<", "\\u003c")
    return (KS3_CHAT_OVERLAY +
            '<script src="/shared/mrbadmus.v2.js" defer '
            'fetchpriority="low"></script>\n'
            '<script>document.addEventListener("DOMContentLoaded",'
            'function(){if(window.MrBadmus){MrBadmus.init(%s);}});</script>\n'
            % cfg)


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
          trail_html="", rail_html="", canonical="", head_links="",
          tail_html="", needs_js=True, og_type="website"):
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

    ⊕ MRB-257 — five additive keyword slots. Every one of them defaults to the
    behaviour this shell already had, so a caller that passes none is
    unchanged. The `trail_html or crumb_html` slot above is untouched: the
    MRB-220 contract's objection was to a SECOND trail slot, not to the shell
    growing head metadata it never had.

    `canonical` — the site path this page is written to (`/ks3/…/x.html`).
    Given one, the head gains `rel="canonical"` and the `og:*` set; given
    nothing it gains neither, because a canonical tag guessing at its own
    address is worse than an absent one. Audit 6.9: 0 of 70 pages had either.

    `head_links` — raw `<link>` markup for relationships only the caller knows.
    Today that is `rel="prev"` / `rel="next"`, emitted from the unit order
    (audit 6.3).

    `tail_html` — raw markup after the footer, before the scripts. The chat
    overlay the tutor CTA opens (audit 6.2) goes here: `MrBadmus.init()` binds
    to `#chatOverlay` and does NOT build it, so the markup has to be on the
    page already.

    `needs_js` — audit 6.5. `shared/ks3.js` is 174 KB and, on an index page,
    wires nothing at all. It was linked from all 294 pages regardless, and
    because `defer` defers EXECUTION and not download priority it competed for
    bandwidth with the render-blocking stylesheet: FCP on Slow 3G measured
    8,532 ms on the discipline hub, whose DOM is 91 nodes with no canvas and no
    interactive control. Index pages now pass `needs_js=False`.

    ⚠️ `/ks3/index.html` KEEPS IT. The KS3 landing page carries MRB-212's
    lesson picker, which `wirePicker()` in ks3.js is the whole behaviour of.
    Dropping the tag there would leave a disclosure button that never opens —
    a much worse defect than a slow page. The rule is "a page that wires
    nothing does not load the wiring", not "index pages do not get JS".
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

    # The description is composed once and reused three times — `<meta
    # name="description">`, `og:description` and nothing else — so the social
    # card and the search result can never disagree about what the page is.
    desc = description or title
    full_title = "%s · MrBadmusAI KS3" % title
    social = ""
    if canonical:
        url = canon(canonical)
        social = (
            '<link rel="canonical" href="%s"/>\n'
            '<meta property="og:type" content="%s"/>\n'
            '<meta property="og:site_name" content="MrBadmusAI"/>\n'
            '<meta property="og:title" content="%s"/>\n'
            '<meta property="og:description" content="%s"/>\n'
            '<meta property="og:url" content="%s"/>\n'
            '<meta name="twitter:card" content="summary"/>\n'
            % (e(url), e(og_type), e(full_title), e(desc), e(url)))

    # ⚠️ `fetchpriority="low"` on a DEFERRED script is not redundant. `defer`
    # says "run me after parsing"; it says nothing about when to FETCH, and the
    # browser was pulling 174 KB of ks3.js concurrently with the stylesheet
    # that blocks first paint. The hint moves the download behind the render
    # path without moving the execution — the instruments still wire before
    # DOMContentLoaded, they just stop starving the CSS to do it.
    scripts = ('<script src="/shared/ks3.js" defer fetchpriority="low"></script>\n'
               if needs_js else "")
    return """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>%(fulltitle)s</title>
<meta name="description" content="%(desc)s"/>
%(favicon)s
%(social)s%(preload)s<link rel="stylesheet" href="/shared/tokens.css"/>
<link rel="stylesheet" href="/shared/styles.css"/>
<link rel="stylesheet" href="/shared/nav.css"/>
<link rel="stylesheet" href="/shared/ks3.css"/>
%(headlinks)s</head>
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
%(tail)s%(scripts)s<script src="/shared/class-entry.js" defer></script>
</body>
</html>
""" % {
        "fulltitle": e(full_title),
        "desc": e(desc),
        "favicon": FAVICON_LINK,
        "social": social,
        "headlinks": head_links,
        "tail": tail_html,
        "scripts": scripts,
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
            % (t(p.get("eyebrow") or "Start here"), sci(p.get("title", "")),
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
            bits.append('<p class="ks3-commit">%s</p>' % sci(p["commit"]))
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


_SVG_BLUE_TINT   = "var(--ks3-blue-tint)"


SVG_ART = _KS3_ART.art


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
        # ⊕ MRB-257 · audit C4 / §8.10 — AN UNBUILT ASSET EMITS NOTHING. NOT A
        # PLACEHOLDER, NOT A CAPTION, NOT A WORD.
        #
        # This used to return a `.ks3-figure-pending` block reading "Diagram
        # coming soon" over the figure's caption. That is the build's own
        # backlog printed to a twelve-year-old, which is precisely what §8.10
        # forbids: a student page carries no meta-text about how the platform
        # works, and "we have not drawn this yet" is the purest example there
        # is. It was written as honesty and it is really an apology addressed
        # to the wrong reader — the student cannot act on it, and the only
        # thing it changes is that the lesson now looks unfinished.
        #
        # ⚠️ THE SAME LEAK EXISTS IN THE RECORDS AND IS NOT FIXED HERE. Eleven
        # lessons hand-author "…is declared in the lesson record as
        # `b5-pollen-tube`, awaiting illustration." into `convention_note`.
        # There is no generator template for that sentence — it is authored
        # prose and it is cut in the records, not here. What this return does
        # is make the GENERATOR structurally incapable of adding a twelfth.
        #
        # Returning "" is deliberate and not a hole: a figure block whose
        # figure is not drawn yet leaves the surrounding blocks flowing into
        # each other exactly as they do on the 54 lessons that never declared
        # a figure at all. The declaration itself is not lost — `figures[]`
        # still carries it, `validate()` still sees it, and
        # `docs/ks3/diagram-manifest.md` is the place the backlog is read,
        # by the people who can act on it.
        return ""
    # ⊕ `drawn` — Mide's diagram ruling of 18 Aug 2026. Code draws it, inline,
    # from tokens. Dispatched through a closed registry with a raise on an
    # unknown name, exactly as `_css_art` does, and for the same reason.
    if status == "drawn":
        art = fig.get("art")
        if art not in SVG_ART:
            raise ValueError(
                "figure %r is status 'drawn' but declares art %r, which the "
                "generator cannot draw. Known: %s. A drawn figure with no "
                "drawer would render an empty <figure> — the hole the status "
                "exists to close." % (fig["id"], art, ", ".join(sorted(SVG_ART))))
        # ⚠️ THE SCROLL REGION IS NOT A NICETY. A drawing sized for a column
        # is 358px wide on a 390px phone, which scales a 760-unit viewBox to
        # 47% and puts every label at about 7px. That is not a small diagram,
        # it is an unreadable one, and most of these students are on a phone.
        # So the drawing keeps a readable minimum width and the narrow reader
        # scrolls it sideways instead — which is what WCAG 1.4.10 allows for
        # content that genuinely needs two dimensions, and a food web does.
        #
        # `tabindex="0"` because a scrollable region that only a mouse or a
        # finger can reach is unreachable from a keyboard (WCAG 2.1.1); the
        # `role`/`aria-label` give that focus stop something to announce, so it
        # does not arrive as a nameless tab stop.
        # ⊕ C3 (MRB-272) — A DRAWN FIGURE MAY CARRY AN ANCHOR.
        #
        # `_id_attr` emits nothing unless the BLOCK authors an `anchor`, so no
        # figure already built moves a byte. What it buys is that a drawing
        # becomes addressable, and the misconception register needs exactly
        # that: MRB-244 requires every `confronted_by` to name an element on
        # its own page, and c3-03's MIX-07 ("a fine enough filter would
        # separate salt from water") is confronted by the particle-panel
        # figure and by nothing else. Without an anchor the honest join could
        # not be expressed and the author would have had to point the entry at
        # some nearby activity that does not, in fact, confront it.
        return ('<figure class="ks3-figure ks3-figure-drawn"%s>'
                '<div class="ks3-figure-scroll" tabindex="0" role="group" '
                'aria-label="%s — scrollable diagram">%s</div>'
                '<figcaption>%s</figcaption></figure>'
                % (_id_attr(block), e(fig["title"]), SVG_ART[art](fig),
                   t(fig["caption"])))
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
        note = ('<span class="ks3-card-note">%s</span>' % sci(v["note"])
                if v.get("note") else "")
        items.append(
            '<li><button type="button" class="ks3-card-btn" aria-expanded="false">'
            '<span class="ks3-card-front">%s</span>'
            '<span class="ks3-card-back" hidden>'
            '<span class="ks3-card-def">%s</span>%s</span>'
            '<span class="ks3-card-hint">Say it, then tap %s</span>'
            '</button></li>'
            % (sci(v["term"]), sci(v["definition"]), note, MARK_ARROW))
    if not items:
        return ""
    # ⊕ C3 (MRB-272) — THE ANCHOR, AND WHY IT WAS MISSING THIS LONG.
    #
    # This block emitted no `id`, and nothing caught it because NO LESSON IN
    # B1–C2 AUTHORS A `keyword` BLOCK: C3 places the first three in the key
    # stage. On c3-01, c3-02 and c3-05 `#s-words` is a RAIL STOP, so without
    # an anchor the rail pointed at an element that does not exist — the stop
    # could not be scrolled to and could never tick. That is the same defect
    # MRB-208 fixed for `#s-hook` and `#s-ladder`, surfacing on the one block
    # type that had never been used.
    #
    # Measured before changing it: zero built pages contain `ks3-keywords`,
    # so the anchor, the stage hook and the authorable strings together
    # cannot move a byte on any page already shipped.
    #
    # `eyebrow` and `lead` are honoured when the block authors them and fall
    # back to the strings this function has always emitted. Design heads the
    # grid "Four words" / "Five words" rather than a bare "Words to know",
    # and her lead is the sharper one — *"Say your answer out loud before you
    # turn each card over. If you cannot say it, you do not know it yet."*
    # The fallbacks stay, so a block authoring neither renders as before.
    #
    # The lead line is R4's declaration ask, in words: a card grid discharges
    # Law 4 through a DECLARED prediction (§5.1.2a), and a declared prediction
    # nobody asked for does not happen. verify_ks3.py fails the build if a card
    # grid ships without it, so this sentence is a gate, not decoration —
    # which is why an authored `lead` may REPLACE it but may never empty it.
    eyebrow = block.get("eyebrow") or "Words to know"
    lead = block.get("lead") or ("Say the meaning out loud before you tap "
                                 "the card.")
    # `data-cards-total` is what lets the section tick: ks3.js marks the stage
    # done once every card in the grid has been turned at least once, which is
    # the completion Design's own `DONE('s-words')` describes. Nothing is
    # ticked on load, and `markStage` is a ratchet, so a card turned back over
    # does not withdraw the credit.
    return ('<section class="ks3-block ks3-keywords"%s data-stage-done="0">'
            '<h2>%s</h2>'
            '<p class="ks3-keywords-lead">%s</p>'
            '<ul class="ks3-cards" data-cards data-cards-total="%d" '
            'role="list">%s</ul>'
            '</section>'
            % (_id_attr(block), t(eyebrow), t(lead), len(items),
               "".join(items)))


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
            parts.append('<p class="ks3-mis-quote">%s</p>'
                         % sci(_quoted(c["quote"])))
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
        '</span><span>%s</span></li>' % (i, rich(s))
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

    ⊕ MRB-245 / B7 — `idle` and `done` are ACCEPTED SPELLINGS of `zero` and
    `full`. b7-02's counter is "nothing changed yet" → "110% rate · 363% water"
    and b7-04's is "step 2 of 4" → "chain traced": the two bespoke ends this
    already has, under the names Design's own pages give them (`tunerProgress`
    tests `s.moved`, `traceProgress` tests `s.everArrived`). This is the
    `_b5_label` union, one level down — accept every spelling that is
    authored, keep one element and one updater, and never rename anything in
    `ks3_data/`. It is a widening, so no shipped counter moves.
    """
    if spec.get("format"):
        spec = dict(spec)
        for authored, canonical in (("idle", "zero"), ("done", "full")):
            if spec.get(authored) and not spec.get(canonical):
                spec[canonical] = spec[authored]
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
        # ⊕ MRB-244 / B6 — `full`, the bespoke label at the TOP of the count,
        # and the mirror of `zero` rather than a fourth shape. b6-01's readout
        # is "not started" → "stage 3 of 5" → "all five stages": Design draws a
        # bespoke sentence at BOTH ends of the same count, and without this the
        # end of the journey would read "stage 5 of 5", which says the student
        # is standing on the last stage rather than that the dose has been
        # followed all the way round. Opt-in, so every shipped counter is
        # unchanged. `zero` still wins at n = 0; the two cannot both apply
        # unless `total` is 0, and a count with no total has no full state.
        full = (' data-full="%s"' % e(spec["full"])) if spec.get("full") else ""
        # ⊕ MRB-248 / B11 — `format_one`, THE SINGULAR, and it is the mirror of
        # `zero` and `full` rather than a fourth shape. Design's b11-03 readout
        # is `n + ' combination' + (n === 1 ? '' : 's') + ' tried'` and b11-04's
        # does the same with "field", so the noun agrees with the count on two
        # of the four B11 benches — and one combination is a state every
        # student passes through on the way to the second.
        #
        # ⚠️ THE ENGINE OWNS THE PLURALISATION AND THE AUTHOR OWNS THE NOUN.
        # Schema §4 and §5 write the suffix as `"combination(s) tried"` and
        # both authors authored exactly that, so without this the page reads
        # "2 combination(s) tried" — on screen, and invisible to every gate
        # that does not open a browser. `_b11_plural` splits the `(s)` and this
        # carries the singular through; the author never writes the noun twice.
        # B10's `pea-cross` solved the same problem inside its own wire
        # function, which is why this is the generalisation of it rather than a
        # third private copy.
        #
        # Opt-in, so every shipped counter with no singular is byte-identical.
        one = (' data-format-one="%s"' % e(spec["format_one"])
               if spec.get("format_one") else "")
        # ⊕ MRB-277 — `format_narrow`, the COMPACT form, opt-in and the mirror
        # of `zero` / `full` / `format_one`. c2-02's readout is the only one in
        # the key stage long enough to overflow a 320px phone (33 characters of
        # 15px mono at `flex: 0 0 auto`, measured at 342px); every other counter
        # tops out at 29 and is byte-identical across this change.
        #
        # ⚖️ Mide ruled the format shortens rather than wraps: a wrapped mono
        # readout changes height as its numbers change and the block jumps
        # under the student's finger. The RESTING render stays the full form —
        # the build cannot know the viewport, and it is the string a crawler
        # and a no-JS reader get — so ks3.js swaps it on its first paint.
        # ⚠️ THE CONSTANTS ARE BAKED INTO THE NARROW FORM TOO. `fmt` above had
        # them substituted; reading `spec["format_narrow"]` raw shipped
        # "{left}/{budget} left" to the page, and ks3.js substitutes only the
        # LIVE placeholders — so a 320px phone would have read a literal
        # "{budget}" where the number goes. Caught in the built bytes rather
        # than on a phone, which is the only reason it is not a defect.
        narrow_fmt = spec.get("format_narrow")
        if narrow_fmt:
            for k, v in sorted((spec.get("constants") or {}).items()):
                narrow_fmt = narrow_fmt.replace("{%s}" % k, str(v))
        narrow = (' data-format-narrow="%s"' % e(narrow_fmt)
                  if narrow_fmt else "")
        if spec.get("zero"):
            return ('<p class="ks3-blockhead-count" data-count data-format="%s" '
                    'data-zero="%s" data-total="%d"%s%s%s%s>%s</p>'
                    % (e(spec["format"]), e(spec["zero"]), total, full, one,
                       narrow, tone, t(spec["zero"])))
        # ⚠️ The RESTING render takes the singular too, or a bench that opens on
        # one combination ships "1 combinations tried" in the bytes and is
        # corrected by JS a frame later — a wrong number on screen for an
        # instant and a wrong number for ever in what a crawler reads.
        if spec.get("format_one") and int(spec.get("start") or 0) == 1:
            first = (spec["format_one"].replace("{n}", "1")
                     .replace("{total}", str(total)))
        return ('<p class="ks3-blockhead-count" data-count data-format="%s" '
                'data-total="%d"%s%s%s%s>%s</p>'
                % (e(spec["format"]), total, full, one, narrow, tone,
                   t(first)))
    if not (spec.get("off") and spec.get("on")):
        raise ValueError(
            "head_counter needs either `format` (+ `total`) or both `off` and "
            "`on`; got %s" % sorted(spec))
    return ('<p class="ks3-blockhead-count" data-count data-off="%s" '
            'data-on="%s">%s</p>'
            % (e(spec["off"]), e(spec["on"]), t(spec["off"])))


_PROGRESS_NAME = re.compile(r"^[a-z][a-z0-9-]*$")


def _progress_readout(spec):
    """The block head's progress readout as a NAMED STATE, not as a count.

    ⊕ MRB-244 / B6. `head_counter` is a tally — "3 of 6 decided" — with two
    opt-in bespoke ends. b6-02's readout is not a tally in any of those shapes:
    Design draws "clock not started" → "clock running" → "cleared", three
    sentences with no number in any of them, and the transitions are decided by
    two independent quantities (has the clock been run, is the blood clear)
    rather than by one counter passing a threshold. Bending it into a count
    would mean inventing a denominator that appears nowhere on the page.

    So `progress` is its own authored key beside `head_counter`, mutually
    exclusive with it, rendering the SAME element — one paragraph in the head
    row, one class, and a sibling updater in `shared/ks3.js`. An instrument
    reports its state by name and the readout prints the author's sentence for
    it; nothing here composes a string.

    The block opens on the first state in the authored order, which is why the
    order is preserved rather than sorted: an instrument's resting state is the
    one an author writes first.
    """
    if not isinstance(spec, dict) or not spec:
        raise ValueError(
            "progress must be a non-empty map of state name to label; got %r"
            % (spec,))
    if len(spec) < 2:
        raise ValueError(
            "progress declares %d state(s). A readout with one state is a "
            "caption, and a caption belongs in the block's prose."
            % len(spec))
    for name, label in spec.items():
        if not _PROGRESS_NAME.match(str(name)):
            raise ValueError(
                "progress state %r is not a usable name. It becomes a "
                "`data-state-<name>` attribute, so it must be lower-case and "
                "start with a letter." % (name,))
        if not label:
            raise ValueError(
                "progress state %r has no label. A state the instrument can "
                "reach with nothing to print is the readout going blank while "
                "the student is holding the control." % (name,))
    first = list(spec)[0]
    return ('<p class="ks3-blockhead-count" data-count data-state="%s"%s>%s</p>'
            % (e(first),
               "".join(' data-state-%s="%s"' % (e(name), e(label))
                       for name, label in spec.items()),
               t(spec[first])))


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


def _lever_steps_heading(lesson, a):
    """The block's <h2>, filled from the rig. Spliced into `r_activity`."""
    _, fill = _lever_steps_rig(lesson, a, a.get("id"))
    return fill(a.get("heading", ""))


# renderers: ═══ END B11 ═══


ACTIVITY_KIND_RENDERERS = _KS3_ART.kind_shell

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
ACTIVITY_KIND_FN = _KS3_ART.kind_fn


# ── the head counter's RESTING count, where the block does not open at zero ──
#
# ⊕ MRB-244 / B5. `head_counter.start` already exists for exactly this and is
# authored per block — but it is a fact about the INSTRUMENT, not about the
# lesson, whenever the instrument's opening state is not empty. b5-03's dial
# opens with one of its three cycle lengths already selected and therefore
# already seen (Design's own state is `seen: { 28: true }`), so Design's page
# renders "1 of 3 lengths tried" on first paint and the shipped HTML must say
# the same thing.
#
# Without this the static page reads "0 of 3 lengths tried" until `wireCycleDial`
# corrects it — a wrong number on screen for an instant, a wrong number
# permanently in the bytes a crawler or a JS-off reader gets, and a
# contradiction of the approved page. `head_counter.start` on the record would
# fix it too, but the record cannot be edited by this pass and, more to the
# point, the value is not the author's to choose: it is one because the dial
# opens on a length, and it would still be one if the author picked a different
# opening length.
#
# An authored `start` still wins. This only fills a blank.
# ⊕ MRB-248 / B11 — `advantage-bench` for the same reason. Design's state is
# `seen: { winter: true }`, so her page renders "1 of 5 conditions tried" on
# first paint: the bench OPENS ON an environment, and an environment you are
# looking at is one you have seen. Zero here would be a wrong number in the
# bytes for the instant before `wireAdvantageBench` corrects it, and a wrong
# number for ever in what a crawler or a JS-off reader gets.
_KIND_HEAD_START = _KS3_ART.kind_head_start

# ── and the counter's DENOMINATOR, where it is a property of the payload ──
#
# ⊕ MRB-245 / B7. `head_counter.total` is authored on every counter in the key
# stage because every one of them counts against a fixed number the author
# knows. b7-04's does not: "step {n} of {total}" runs over SIX chains of three,
# four and five links, so the denominator changes with the tab and belongs to
# the food rather than to the block. `wireTraceItBack` rewrites `data-total` on
# every food change and would have been the only thing that ever knew it — so
# the shipped bytes would have read "step 1 of 0" until JS ran, which is a
# wrong number on screen and a wrong number for a crawler or a JS-off reader.
#
# A callable rather than an int for the same reason `_KIND_HEAD_START` is a
# constant: the value is not the author's to choose. It is the length of the
# first food's chain, and it would still be that if the author reordered the
# plate. An authored `total` still wins; this only fills a blank.
_KIND_HEAD_TOTAL = _KS3_ART.kind_head_total

# ── the head readout DERIVED, where Design draws one and authors no key ──
#
# ⊕ MRB-248 / B8. b8-03's head row carries a CLOCK — "on the start line" →
# "10 s" → "40 s · recovering" — which is the same right-aligned mono paragraph
# every other bench in the unit puts its progress in. It is not a tally and it
# is not a two-state boolean, so neither `head_counter` nor an authored
# `progress` map is the shape of it; what it is, is three named states, two of
# which quote a number. That is exactly `_progress_readout` — so the spec is
# derived here from the `clock` the schema already authors, rather than asking
# the author to write the same three strings a second time in a second shape.
#
# Derived rather than authored for the same reason `_KIND_HEAD_START` is: the
# value is not the author's to choose. The running state is the seconds and the
# suffix, and it would still be that if the author changed the suffix.
_KIND_HEAD_FROM = _KS3_ART.kind_head_from

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

# ⊕ MRB-244 — and `progress`, for the same reason and by the same derivation.
#
# `progress` was already an INSTRUMENT-owned key when B6 arrived: `fifa-pick`,
# `lever-steps` and `random-walk-bench` each read one and each draws its own
# readout inside its own component. b6-02's clock authors the same key for the
# same idea in Design's own place for it — the block's HEAD ROW, right-aligned
# and mono, where `head_counter` goes — and `r_clearance_clock` therefore does
# not read it at all.
#
# The first cut of this made `progress` a shell key unconditionally and c1-05
# went red on the spot: `walk-bench` authors `{idle, spreading, even}` for its
# own canvas readout, and the shell would have printed it a second time in the
# head row while claiming the two were the same paragraph. The test is not
# "does this activity carry `progress`" but "did the thing that drew this
# activity consume it" — which is the distinction `_KIND_FN_OWNS_OPTIONS`
# exists to make, and it generalises here for free: an instrument that starts
# reading `progress` tomorrow takes it back from the shell the moment it does.
_KIND_FN_OWNS_PROGRESS = _kinds_consuming(
    r'a\.get\(\s*"progress"|a\[\s*"progress"\s*\]')

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
    # ⊕ MRB-248 / B11 — `title` and `intro` are ACCEPTED SPELLINGS of `heading`
    # and `prompt`. This is `_head_counter`'s `idle`/`done` widening one level
    # up, and for the same reason: the names on the left are the ones the
    # payload schema wrote down and three of B11's four authors therefore
    # authored, and the names on the right are what the shell has always read.
    #
    # ⚠️ UNREAD, THEY ARE NOT A DEAD KEY — THEY ARE A MISSING HEADING. The shell
    # emits the block's <h2> from `heading` and its lede from `prompt`, so an
    # activity authored to the schema's spelling ships a practical block whose
    # title and instruction are simply absent, with nothing raised: `heading` is
    # optional, `prompt` is optional, and `ks3_key_audit.py` would report two
    # unread keys among a hundred. Three of B11's four benches were authored
    # that way before this existed.
    #
    # A widening rather than a rename, so nothing in `ks3_data/` moves and no
    # shipped block changes: measured across every authored lesson, the ONLY
    # activities carrying `title` or `intro` are the three B11 benches. The
    # authored spelling wins where both are present, which cannot happen today
    # and would be an authoring error rather than a choice if it ever did.
    heading = a.get("heading") or a.get("title")
    if kind == "lever-steps" and heading:
        heading = _lever_steps_heading(lesson, a)

    # ⊕ §4.8.2 — the two CLASSIFY instruments. Each takes a modifier class and
    # a marker attribute: the class is what the stylesheet hangs the instrument
    # on, and the attribute is what shared/ks3.js dispatches on. `data-board`
    # and `data-sort` also tell `wirePredictions` to keep its hands off — an
    # instrument owns every option inside it, and the generic Law 4 wiring
    # would otherwise unhide the first `[data-reveal]` it found, which on the
    # board is specimen one's verdict panel.
    # ⊕ MRB-245 — an activity may DECLARE the shell it expects, and a
    # disagreement is a build failure rather than a silent repaint.
    #
    # Every unit since B5 lifts its instruments out of `core` with a
    # `_INSTRUMENT_SEGMENTS` map in its own `__init__.py`, and that map is what
    # decides the shell. b7-01's record also states the segment on the block
    # itself — measured off Design's own markup, `ks3-block ks3-dark
    # ks3-practical`, and written down beside the measurement. Unread, that is
    # a dead key (R5) and, worse, a SECOND statement of the shell that can
    # disagree with the first: a lesson could declare `practical` and be lifted
    # into a `check`, and the page would ship the wrong ground with nothing
    # anywhere saying so. §4 of the build contract records that B1 got two of
    # six shells wrong by inferring them from the kind name — this is the
    # assertion that would have caught it.
    declared = a.get("segment")
    if declared and declared != block_type:
        raise ValueError(
            "%s: activity %r declares segment %r and was rendered into a %r "
            "shell. The segment is MEASURED off Design's markup, so the two "
            "disagreeing means either the measurement or the unit's "
            "_INSTRUMENT_SEGMENTS map is wrong — and the page would ship the "
            "other one's ground in silence."
            % (lesson.get("slug"), act_id, declared, block_type))

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
    # ⊕ MRB-244 — `progress`, the same head-row slot filled by a NAMED STATE
    # rather than by a tally. See `_progress_readout`. Mutually exclusive with
    # `head_counter`: they render the same paragraph, and a block authoring
    # both would print one of them and silently drop the other.
    #
    # ⚠️ Only when the INSTRUMENT did not consume it — `fifa-pick`,
    # `lever-steps` and `random-walk-bench` each read their own `progress` and
    # draw their own readout. See `_KIND_FN_OWNS_PROGRESS`.
    pg = None if kind in _KIND_FN_OWNS_PROGRESS else a.get("progress")
    # ⊕ MRB-248 / B8 — the head readout DERIVED, for an instrument Design draws
    # one on and the schema authors under another name. See `_KIND_HEAD_FROM`.
    # An authored readout of either shape still wins; this only fills a blank.
    if not hc and not pg and kind in _KIND_HEAD_FROM:
        derived = _KIND_HEAD_FROM[kind](a)
        # ⊕ MRB-250 / B9 — a derivation may name EITHER shape, and the
        # discriminator is the one `_head_counter` itself already uses: a spec
        # with a `format` is a tally, anything else is a map of named states.
        # B8's single derivation produced named states; five of B9's six
        # produce a count with a bespoke end, because Design's readout on those
        # five quotes a number the runtime owns. Sending those through
        # `_progress_readout` would ship `level {n} of {total}` with the braces
        # still in it — the head row's one unrecoverable failure, because every
        # other gate sees a rendered page and reads it as fine.
        if isinstance(derived, dict) and derived.get("format"):
            hc = derived
        else:
            pg = derived
    if hc and pg:
        raise ValueError(
            "%s: activity %r authors both `head_counter` and `progress`. They "
            "are two shapes of the SAME readout in the block's head row, so "
            "one of them would be rendered and the other would vanish without "
            "a trace." % (lesson.get("slug"), act_id))
    # ⊕ MRB-248 / B8 — `progress` authored as a plain STRING is a COUNT format,
    # not a map of named states. b8-05's is "{n} of {total} settled": one
    # sentence with one number in it and no bespoke ends, which is precisely
    # what `head_counter`'s format shape already is. Routed to it rather than
    # given a fourth renderer, so there stays one element and one updater in the
    # head row; the denominator is filled by `_KIND_HEAD_TOTAL` below, because
    # it is a property of the payload rather than a number an author chose.
    if isinstance(pg, str):
        hc, pg = {"format": pg}, None
    # ⊕ MRB-244 / B5 — an instrument whose opening state is not empty fills the
    # counter's resting number. See `_KIND_HEAD_START`; an authored `start`
    # still wins, and `hc` is copied rather than mutated because the lesson
    # record is shared with every gate that reads it afterwards.
    if hc and kind in _KIND_HEAD_START and "start" not in hc:
        hc = dict(hc, start=_KIND_HEAD_START[kind])
    # ⊕ MRB-245 / B7 — and its denominator, where that is a fact about the
    # payload rather than a number an author chose. See `_KIND_HEAD_TOTAL`.
    if hc and kind in _KIND_HEAD_TOTAL and "total" not in hc:
        hc = dict(hc, total=_KIND_HEAD_TOTAL[kind](a))
    head_emitted_content = False
    if block_type == "misconception":
        parts.append('<div class="ks3-mis-head">'
                     '<span class="ks3-mis-badge" aria-hidden="true">!</span>'
                     '<p class="ks3-eyebrow">%s</p></div>' % t(eyebrow))
        # ⊕ Subsumes the old single-quote path. With no authored `statements`
        # this emits exactly the register quote it always did, which is why
        # C1's seven confrontations do not move: none of them carries any of
        # the new keys.
        parts.append(r_confrontation(lesson, a, act_id))
        # ⊕ MRB-244 — a `misconception` block renders its whole body HERE, in
        # the head branch, before the framing mark below. Without this flag the
        # empty-activity gate would read every confrontation in the key stage
        # as having produced nothing and fail six live B1 lessons.
        head_emitted_content = True
    elif hc or pg:
        parts.append('<div class="ks3-blockhead"><div>'
                     '<p class="ks3-eyebrow">%s</p>%s</div>%s</div>'
                     % (t(eyebrow),
                        ("<h2>%s</h2>" % t(heading)) if heading else "",
                        _head_counter(hc) if hc else _progress_readout(pg)))
        prompt_tag = "p"
    else:
        parts.append('<p class="ks3-eyebrow">%s</p>' % t(eyebrow))

    # ⊕ §4.8.2 — an explicit `heading` beside the prompt. The `check` shell
    # promotes the PROMPT to the block's <h2>, which works while a block has
    # only one of the two. Design's instruments carry both a title and a line
    # of instruction under it, and without this the title would be lost.
    # ⚠️ `hc or pg`, not `hc`. The head-row branch above already emitted the
    # <h2> for BOTH readout shapes, and testing only `head_counter` here shipped
    # b6-02 with its heading printed twice — once inside `.ks3-blockhead` and
    # once as a bare sibling under it. Caught in a browser the same afternoon
    # the `progress` shape was added, which is the whole argument for the two
    # names being handled together everywhere they are handled at all.
    if heading and not (hc or pg):
        parts.append("<h2>%s</h2>" % t(heading))
        prompt_tag = "p"

    prompt = a.get("prompt") or a.get("intro")
    if prompt:
        # ⚠️ A card grid keeps its prompt as prose even in a `check`. The prompt
        # IS R4's declaration ask ("say it, then tap"), and verify_ks3.py's
        # §5.1.2(a) gate reads that ask out of the block's non-hidden <p>
        # elements before the grid. Promoting it to a heading would leave the
        # gate looking at the eyebrow alone and passing or failing on the
        # wording of "Your turn" — a live check silently disarmed.
        tag = "p" if a.get("cards") else prompt_tag
        # ⊕ MRB-248 / B10 — `rich()`, NOT `t()`. This shipped
        # "<strong>P</strong> gives purple and beats <strong>p</strong>" as
        # literal angle brackets on b10-04, on a live page, in the sentence
        # that introduces the whole notation the lesson is built on. Design
        # draws real `<strong>` there (page line 113), and emphasis in a prompt
        # is the one piece of markup a prompt has ever wanted.
        #
        # `rich()` is `t()` plus `<em>` and `<strong>` and NOTHING else, so a
        # prompt carrying no markup is byte-identical across this change —
        # verified by diffing the whole built tree, 295 pages, before and
        # after: b10-04 is the only page that moves.
        parts.append("<%s>%s</%s>" % (tag, rich(prompt), tag))

    # ⊕ MRB-244 — everything appended so far is FRAMING: eyebrow, heading,
    # head-counter, prompt. Everything after this line is the activity itself.
    # The check at the end of this function compares against this mark, so a
    # kind with no renderer cannot ship an empty block. See it for why.
    head_len = len(parts)

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
            parts.append('<div class="ks3-reveal ks3-reveal-panel"%s hidden '
                         'data-reveal>%s</div>'
                         % (_reveal_id_attr(a),
                            "".join("<p>%s</p>" % rich(p) for p in rev)))
        else:
            parts.append('<div class="ks3-reveal"%s hidden data-reveal>%s</div>'
                         % (_reveal_id_attr(a), t(rev)))
    if a.get("success"):
        parts.append(r_criteria(a["success"]))

    # ⊕ MRB-244 — AN ACTIVITY THAT RENDERS NOTHING IS A BUILD FAILURE.
    #
    # Both dispatch lookups above are `.get()` with a silent fall-through
    # (`if instrument:` / `if fn:`), so an activity whose `kind` has no
    # registered renderer emitted its eyebrow, its heading, its prompt and its
    # head-counter — and then stopped. The section still carried the practical
    # shell, so it looked like an instrument block with the instrument missing.
    #
    # This is not hypothetical and it is not cheap. B5 was authored by eight
    # passes in parallel while the engine pass that owned the eight renderers
    # was killed mid-run before writing any of them. Seven lesson records
    # landed naming `cycle-dial`, `flower-jobs`, `disperse-sort` and the rest;
    # every page built, and `build_ks3.py` printed ✅ validation passed. One of
    # them shipped a block reading "0 of 3 lengths tried" with nothing on the
    # page to try, above a rail stop that could never tick.
    #
    # The contract's gate 6 says a dispatch-table entry is not a component and
    # that instruments have shipped as bare bullet lists past a green kinds
    # gate. This is the same defect one step further on — no bullet list, no
    # dispatch row, and still green. A gate that only a browser can fail is not
    # protecting the eleven units still to be authored.
    #
    # The test is deliberately "did this activity produce any content at all"
    # rather than "is this kind in the registry": several legitimate kinds
    # carry no `ACTIVITY_KIND_FN` row and render through `options`, `cards`,
    # `sim`, `fifa`, `reveal` or `statements` instead, and enumerating them
    # here would be a second registry to keep in step with the first.
    if len(parts) == head_len and not head_emitted_content:
        raise ValueError(
            "%s: activity %r (kind %r) rendered NOTHING but its heading and "
            "prompt. Either the kind has no renderer registered in "
            "ACTIVITY_KIND_RENDERERS/ACTIVITY_KIND_FN, or it is authored with "
            "no options, cards, sim, fifa, reveal or success. A practical "
            "shell with no instrument inside it is an empty block, not a "
            "lesson."
            % (lesson.get("slug"), act_id, kind))

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
            % (e(key), num, e(_rung_title(name, q)), sci(q.get("q", "")),
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
            '</li>' % (e(cid), e(cid), i + 1, rich(s)))
    aid = "ks3-ans-%s-%s" % (slug, key)
    return ('<div class="ks3-rung ks3-rung-self" data-rung="%s" data-mode="self">'
            '<h3 tabindex="-1">Rung %d · %s</h3>'
            '<p class="ks3-rung-q">%s</p>'
            '<label class="ks3-answer-label" for="%s">%s</label>'
            '<textarea class="ks3-answer" id="%s" data-answer rows="5"%s>'
            '</textarea>'
            # ⊕ RULING (Mide, 19 Aug 2026) — ships INACTIVE, like every other
            # gated reveal in the key stage (`data-sort-reveal disabled`, and
            # the rest). `wireSelf` in shared/ks3.js releases it once the
            # answer box holds 60 characters, and re-arms it on a retry.
            # Emitting the attribute rather than adding it in JS means the
            # control is never briefly live in the window before a 700 KB
            # deferred script runs.
            # ⊕ MRB-269 phase 4a (Mide, 20 Aug 2026) — this button used to
            # read "Check my answer". Nothing checks it: the student writes
            # prose, this reveals the success criteria, and the student marks
            # themselves against them. A label promising a check implied a
            # verdict the platform never had — the same false claim the
            # payload was making in `is_correct`, made in words. "Complete" is
            # what the button actually does.
            '<button type="button" class="ks3-check-btn" data-check '
            'aria-expanded="false" disabled>Complete</button>'
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
            % (e(key), num, e(_rung_title(name, q)), sci(q.get("q", "")), e(aid),
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
    rungs, self_marked = [], []
    for key, num, name in LADDER_RUNGS:
        q = lad.get(key)
        if not q:
            continue
        if q.get("options"):
            rungs.append(_rung_marked(key, num, name, q))
        elif q.get("success"):
            rungs.append(_rung_self(slug, key, num, name, q))
            self_marked.append(num)

    # ⊕ MRB-257 · audit C7 — THE SUB-LINE IS GONE, and only one line survives.
    #
    # This block used to emit BOTH `.ks3-ladder-sub` ("Four rungs. Two the page
    # marks, two you mark.") and `.ks3-score-note` ("Rungs 3 and 4 you mark
    # yourself.") into the same header, on all 58 lessons. Two sentences, one
    # fact, side by side — and the second is the better of the two: it names
    # WHICH rungs rather than how many, which is the thing a student standing
    # in front of the ladder actually needs.
    #
    # The count is not lost with it. The rungs are numbered on the page and
    # they are all visible at once, so "four" was being told to a reader who
    # could already see four. Nothing in `shared/ks3.js` reads or rewrites
    # either string (checked), so dropping the sub-line is a pure subtraction.
    #
    # The page-marked rungs are no longer counted at all: `len(marked)` had
    # exactly one reader and it was the sentence above. `self_marked` still
    # earns its list, because the surviving note names the rungs by number.
    if not self_marked:
        note = "The page marks every rung."
    elif len(self_marked) == 1:
        note = "Rung %d you mark yourself." % self_marked[0]
    else:
        note = ("Rungs %s and %d you mark yourself."
                % (", ".join(str(n) for n in self_marked[:-1]), self_marked[-1]))

    return ('<section class="ks3-block ks3-ladder" data-lesson="%s"%s>'
            '<div class="ks3-ladder-head">'
            '<div><h2>Mastery ladder</h2></div>'
            '<div class="ks3-ladder-score" aria-live="polite">'
            '<p class="ks3-score" data-score>Not started yet.</p>'
            '<p class="ks3-score-note" data-score-note>%s</p></div>'
            '</div>'
            '<div class="ks3-rungs">%s</div>'
            '</section>'
            % (e(slug), _id_attr(block or {}), e(note),
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


def _rule_card(block, i, c):
    """One statement-panel card — ⊕ MRB-245, and a CONTENT-LOSS repair.

    ⚠️ **THIS RENDERED THREE PAGES' CARDS AS EMPTY `<li>`s, TWO OF THEM LIVE.**
    The card was `term` + `gloss` and nothing else, and three lesson records
    authored a card Design had drawn with more parts than that:

      b1-03 `#s-rule`  `label` + `chips[]` + `chip_tone` + `close`  — the
                       "In both · 4" / "Plant only · 3" pills. SIX pills and
                       two closing sentences, on an approved page in front of
                       students, rendering as two empty boxes.
      b1-04 `#s-rule`  `label` + `title` + `body` + `examples` — the four
                       "Problem 1…4" cards, likewise live, likewise empty.
      b7-01 `#s-summary` `role` + `name` + `body` — the four part cards
                       sorting the reaction into reactants and products, which
                       is what rung 1 marks.

    Nothing failed. The `<li>`s were emitted, the grid laid out, the panel
    looked deliberate, and `ks3_key_audit.py` was clean because `name`, `body`,
    `label` and `title` are string literals in half the generator — the audit
    is a lint on NAMES and cannot see that THIS `name` reached no page. It is
    the `r_activity` empty-block defect one level down, and it is why the raise
    at the end of this function exists.

    Every shape below is MEASURED off Design's own markup — b1-03 lines
    230–248, b1-04 lines 218–223, b7-01 lines 173–178 — and every string was
    already authored. Nothing is invented and no copy is written here.

    Shipped `term` + `gloss` cards are byte-identical across this change: each
    new part renders only when its key is authored, and no live card authors
    one.
    """
    role_tone = c.get("label_tone") or "accent"
    role = c.get("role") or c.get("label")
    # `term` is the shipped spelling. `name` (b7-01) and `title` (b1-04) are
    # the same slot under the words their own records use — the `_b5_label`
    # union, and the alternative was failing two live lessons over a synonym.
    term = c.get("term") or c.get("name") or c.get("title")
    # `gloss` shipped; `body` is b1-04's and b7-01's; `close` is b1-03's
    # closing sentence, which sits in the same place and does the same job.
    gloss = c.get("gloss") or c.get("body") or c.get("close")
    chips = c.get("chips") or []
    # b1-04's foot line: the cells that answer the problem the card names.
    examples = c.get("examples")
    # ⊕ MRB-248 / B11 — `limit`, THE FOURTH PART, and it is a repair of the
    # same kind as the badge above.
    #
    # b11-04's `#s-banks` cards are `kind` + `name` + `body` + `limit` (page
    # lines 158–161): what the method IS, and then what it CANNOT do, in a
    # second paragraph at 17px in `--ks3-ink-muted`. The "what it cannot do"
    # half is the whole argument of that panel — the statement above the cards
    # reads *"Two places to store it, and only one of them is alive"* — so it
    # is not an aside that could ride along inside `body`.
    #
    # ⚠️ AND `examples` IS THE WRONG SLOT FOR IT. `.ks3-rule-eg` is MONO at
    # 15px, which is right for "shrew · dormouse · hedgehog" and wrong for two
    # sentences of prose. Without a slot of its own the author's only options
    # are a mono paragraph or joining the two halves into one — which is what
    # b11-04 shipped before this existed: every byte preserved, the paragraph
    # break and the muted tone lost.
    #
    # `caveat` is accepted alongside it, the `_b5_label` union again, because
    # the two words name the same slot and failing a lesson over a synonym is
    # what that union exists to prevent.
    limit = c.get("limit") or c.get("caveat")
    # ⊕ MRB-248 / B10 — THE ACCENT BADGE, and it is the same wall hit twice.
    #
    # b10-03's `#s-who` cards carry `RF` / `MW` / `EC` / `WC` (page line 158)
    # and b10-04's `#s-steps` cards carry `1` / `2` / `3` / `4` (page line 172).
    # Both are a filled accent square to the LEFT of a two- or three-row card,
    # spanning its rows — the same component drawn at two sizes, which is why
    # the key names the KIND and the stylesheet holds the sizes.
    #
    # ⚠️ NEITHER CAN BE DERIVED. `WC` is "Watson and Crick", which is not the
    # initials of the string `name`; a code that computed it would be guessing,
    # and would guess `W` or `WAC`. The digit is likewise the card's position
    # in a numbered sequence the record owns. Both are content.
    #
    # ⚠️ AND WITHOUT THIS SLOT THE KEYS ARE DEAD (contract R5). b10-04's author
    # had already worked around the gap by authoring the digit into `role`,
    # which ships it as the mono accent TAG rather than as Design's badge — the
    # card then has a number where its job title goes and no badge at all.
    badge = c.get("initials") or c.get("num")
    badge_kind = "initials" if c.get("initials") else "num"

    parts = []
    # ⊕ MRB-248 / B10 — A BADGED CARD READS NAME, THEN ROLE, THEN BODY, which
    # is the reverse of the flow card's role-then-name. Measured on both pages
    # (b10-03 lines 159–161, b10-04 lines 173–174): the badge already does the
    # labelling job the role line does on a b1-04 card, so the NAME is the
    # first thing in the second column and the role sits under it as a
    # subtitle. Emitting the flow order into the grid puts the job title
    # alongside the badge and the name below it, which reads as a card about a
    # laboratory rather than about a person.
    if badge is not None:
        # `aria-hidden`, as Design draws it: the badge repeats what the name
        # beside it already says, and a screen reader that spelled out "RF"
        # before "Rosalind Franklin" would be reading the card twice.
        parts.append('<span class="ks3-rule-badge" data-badge="%s" '
                     'aria-hidden="true">%s</span>'
                     % (e(badge_kind), t(str(badge))))
    head = []
    if role:
        head.append('<p class="ks3-rule-role" data-tone="%s">%s</p>'
                    % (e(role_tone), t(role)))
    if term:
        head.append('<p class="ks3-rule-term">%s</p>' % t(term))
    parts.extend(reversed(head) if badge is not None else head)
    if chips:
        parts.append('<ul class="ks3-rule-chips" data-tone="%s" role="list">%s'
                     '</ul>'
                     % (e(c.get("chip_tone") or "inset"),
                        "".join('<li class="ks3-rule-chip">%s</li>' % t(ch)
                                for ch in chips)))
    if gloss:
        parts.append('<p class="ks3-rule-gloss">%s</p>' % rich(gloss))
    if limit:
        parts.append('<p class="ks3-rule-limit">%s</p>' % rich(limit))
    if examples:
        parts.append('<p class="ks3-rule-eg">%s</p>' % t(examples))

    # ⊕ MRB-245 — A CARD THAT RENDERS NOTHING IS A BUILD FAILURE, for the same
    # reason `r_activity` raises on an activity that renders nothing: the box
    # is still drawn, the grid still lays out, and the page looks intentional.
    # Ten empty cards shipped across three lessons behind a green build; this
    # is the assertion that would have caught the first one.
    if not parts:
        raise ValueError(
            "%s: statement-panel card %d renders NOTHING — it authors %s and "
            "this component reads initials/num, role/label, term/name/title, "
            "chips, "
            "gloss/body/close, limit/caveat and examples. An empty card is "
            "still a drawn box "
            "on a laid-out grid, so it ships looking deliberate."
            % (block.get("anchor") or block.get("id") or "rule", i,
               sorted(c) or "no keys at all"))
    # ⊕ MRB-248 / B10 — a card with a badge is a two-column GRID, and the
    # attribute is what the stylesheet switches on. Without it the badge would
    # sit above the name in flow, which is a different card.
    return ('<li%s>%s</li>'
            % ((' data-badge="%s"' % e(badge_kind)) if badge is not None
               else "", "".join(parts)))


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
    cards = "".join(_rule_card(block, i, c)
                    for i, c in enumerate(block.get("cards") or []))
    close = ('<p class="ks3-rule-close">%s</p>' % rich(block["close"])
             if block.get("close") else "")
    # ⊕ MRB-245 / B7 — the WORD SUMMARY, drawn between the statement and the
    # cards, which is where Design puts it (b7-01 page lines 165–170).
    equation = r_equation(block["equation"]) if block.get("equation") else ""
    # ⊕ MRB-245 / B7 — a NESTED key fact, exactly as `r_comparison` has taken
    # one since B1. Design nests the box inside three of the four B7 band
    # panels; two of those lessons resolved it by lifting the box to a
    # top-level `key-fact` block, and b7-01 authored it in place because its
    # box is on the CARD ground rather than the band and lifting it would have
    # changed the treatment. Defaulting to `card` is `r_comparison`'s own
    # default, for its own reason: this panel is already `--ks3-band`, and band
    # on band is invisible.
    nested = block.get("key_fact")
    kf = (r_key_fact(lesson, dict(nested, ground=nested.get("ground", "card")))
          if nested else "")
    return ('<section class="ks3-rule"%s><p class="ks3-eyebrow">%s</p>'
            '<p class="ks3-rule-statement">%s</p>'
            '%s%s%s%s</section>'
            % (_id_attr(block), t(block.get("eyebrow") or "What settles it"),
               rich(block.get("statement", "")), equation,
               ('<ul class="ks3-rule-cards"%s>%s</ul>'
                % (' data-badged=""' if any(
                    c.get("initials") or c.get("num") is not None
                    for c in (block.get("cards") or [])) else "",
                   cards)) if cards else "",
               kf, close))


# Design's arrow, measured off b7-01 page line 167 and redrawn here rather than
# retyped: viewBox `0 0 60 24`, `M2 12h48M42 5l8 7-8 7`, no fill, 3px stroke,
# round caps and joins, on `var(--ks3-accent-text)`. That geometry belongs to
# the engine exactly as `_BEAM` does — it is Design's drawing, not content.
_EQN_ARROW = (
    '<svg class="ks3-eqn-arrow" viewBox="0 0 60 24" width="60" height="24" '
    'aria-hidden="true" focusable="false">'
    '<path d="M2 12h48M42 5l8 7-8 7" fill="none" stroke="currentColor" '
    'stroke-width="3" stroke-linecap="round" stroke-linejoin="round"></path>'
    '</svg>')


def r_equation(eq):
    """⊕ MRB-204 as amended · b7-01 `#s-summary` — the word summary.

    ⚠️ **THE ARROW IS DRAWN, AND THERE IS NO SLOT TO TYPE ONE INTO.** The
    design system's five latin woff2 subsets contain no U+2192 — the same fact
    that makes `MARK_ARROW` a drawing — so a typed arrow drops to a system font
    mid-line inside a 27px Bricolage-800 row. `arrow` therefore holds the WORD
    the arrow MEANS, "gives", and that word is the component's accessible name
    and nothing else. Three consequences, all deliberate: there is no field an
    author could put a character into that would render between the two halves;
    the accessible name is composed out of the same four strings a sighted
    student reads, so it cannot drift from them; and "gives" is the word the
    page itself uses everywhere the summary is spoken aloud — the key note and
    all four options of rung 1.

    ⚖️ **NO TRIANGLE AND NO COVER-BAR, BY DECISION.** MRB-204 as amended gives
    the triangle to a product (`A = B × C`) and the balance beam plus part–whole
    bar to a sum or a conservation statement. A chemical change is neither: two
    substances are consumed and two different ones are produced, and no quantity
    on the left is recoverable by covering a quantity on the right. A triangle
    over `carbon dioxide + water → glucose + oxygen` would teach that
    `water = glucose × oxygen ÷ carbon dioxide`, which is not merely unhelpful
    but false, and a part–whole bar would teach the conservation-of-mass claim
    c2-06 owns rather than what a word summary says. So this block carries the
    equation and nothing else, and the two cover components are absent by
    decision rather than by omission.

    Geometry follows Design's own markup: a wrapping flex row of reactants,
    arrow, products, with `condition` full-width beneath it. Not a stack —
    measured, because a horizontal arrow between two stacked labels points at
    nothing.
    """
    over, under = eq.get("condition_over"), eq.get("condition_under")
    split = bool(over or under)
    # ⊕ MRB-254 — TWO CONDITIONS, ONE ABOVE THE ARROW AND ONE BELOW IT.
    #
    # b7-01 authored both of photosynthesis's conditions as one sentence —
    # "requires light energy, absorbed by chlorophyll" — set full-width under
    # the whole equation. Two things were lost and the second is the one that
    # matters.
    #
    # First, it does not say WHERE either condition acts. Light and chlorophyll
    # are not two halves of one requirement: light is the energy the reaction
    # runs on and chlorophyll is what absorbs it, and every board writes them
    # in the two positions that say so — the energy over the arrow, the thing
    # that captures it under. A student who only ever meets them as a
    # comma-joined sentence cannot read that convention when they meet it, and
    # cannot write it.
    #
    # Second, a full-width line under a flex row is attached to the ROW, not to
    # the arrow. It reads as a footnote on the summary, which is what a
    # condition must not be: the condition is a property of the CHANGE, and the
    # change is the arrow.
    #
    # Both keys are optional. b8-01 and b8-03 carry a single `condition` that
    # is genuine commentary on the whole equation rather than a condition on
    # the arrow — "energy is transferred from the glucose to the cell" is not
    # something that sits over an arrow — so they are untouched and keep the
    # full-width line.
    required = ("reactants", "arrow", "products")
    if not split:
        required = required + ("condition",)
    for key in required:
        if not eq.get(key):
            raise ValueError(
                "the word summary declares no %r. `arrow` is the WORD the drawn "
                "arrow means and is the component's accessible name; the "
                "character itself is never authored." % key)
    if split and eq.get("condition"):
        raise ValueError(
            "the word summary authors BOTH `condition` and a split condition. "
            "The two are alternatives — a condition that sits ON THE ARROW and "
            "a note that sits under the equation are different claims, and "
            "shipping both prints the same requirement twice in two places "
            "that mean different things.")
    if split and not (over and under):
        raise ValueError(
            "the word summary splits its condition but authors only the %s "
            "half. The two positions are a CONVENTION — the energy over the "
            "arrow, the substance that captures it under — and one half of a "
            "convention tells the reader nothing about which half they are "
            "looking at." % ("upper" if over else "lower"))
    for key in ("reactants", "arrow", "products"):
        if "→" in eq[key]:
            raise ValueError(
                "the word summary's %r contains a typed U+2192. The arrow is "
                "DRAWN — the design system's fonts have no glyph for it, so a "
                "typed one falls back to a system font mid-line. `arrow` holds "
                "the word it means." % key)
    if split:
        # The accessible name says the two positions IN WORDS, because "over
        # the arrow" is exactly the information the drawn layout carries, and a
        # screen reader cannot see a layout.
        return ('<div class="ks3-eqn ks3-eqn-split" role="img" aria-label="%s">'
                '<p class="ks3-eqn-side">%s</p>'
                '<span class="ks3-eqn-arrowstack" aria-hidden="true">'
                '<span class="ks3-eqn-cond ks3-eqn-cond-over">%s</span>'
                '%s'
                '<span class="ks3-eqn-cond ks3-eqn-cond-under">%s</span>'
                '</span>'
                '<p class="ks3-eqn-side">%s</p></div>'
                % (e("%s %s %s, with %s over the arrow and %s under it"
                     % (eq["reactants"], eq["arrow"], eq["products"],
                        over, under)),
                   t(eq["reactants"]), t(over), _EQN_ARROW, t(under),
                   t(eq["products"])))
    return ('<div class="ks3-eqn" role="img" aria-label="%s">'
            '<p class="ks3-eqn-side">%s</p>'
            '<span class="ks3-eqn-arrowwrap" aria-hidden="true">%s</span>'
            '<p class="ks3-eqn-side">%s</p>'
            '<p class="ks3-eqn-condition">%s</p></div>'
            % (e("%s %s %s, %s" % (eq["reactants"], eq["arrow"], eq["products"],
                                   eq["condition"])),
               t(eq["reactants"]), _EQN_ARROW, t(eq["products"]),
               t(eq["condition"])))


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
    # ⊕ P4 (MRB-223), 24 Aug 2026 — A FORMULA FIGURE MAY BE UNIT-OWNED ART.
    #
    # `balance` below is the ONE shape this function draws itself, and it was
    # written for c2-06's level beam. Physics then arrived with five more, all
    # different and all specific to one lesson: p4-02's three aligned bars,
    # p4-03's two opposed panels, p4-08's equal helpings beside a graph that
    # bends, p5-02/p5-04's stack of fluid layers. Drawing those here would put
    # five units' geometry in the engine, which is exactly what `ks3_art`
    # exists to stop — and it would put two content lanes back in one file.
    #
    # So `art` names a drawer in the unit's OWN module, resolved through the
    # same closed registry `r_figure` already uses, with the same raise on an
    # unknown name. `shape` is untouched: a figure with no `art` goes down the
    # identical path it always did, so c2-06 and p2-04 do not move a byte.
    #
    # ⚠️ THE TRIANGLE IS NOT REACHABLE FROM HERE, AND THAT IS DELIBERATE. A
    # product's figure is the `triangle` key with its own renderer; this branch
    # draws the sums, the differences and the ratios. A unit cannot register a
    # triangle drawer into `art` and quietly get MRB-204's shape for a
    # relationship that is not a product.
    art = fig.get("art")
    if art:
        if art not in SVG_ART:
            raise ValueError(
                "formula figure declares art %r, which no unit module draws. "
                "Known: %s. A declared drawing with no drawer renders an "
                "empty block under the statement it is meant to draw."
                % (art, ", ".join(sorted(SVG_ART))))
        # ⊕ PHASE 3, 25 Aug 2026 · `caption` AND `note` ARE PART OF THE
        # FIGURE, and leaving them out lost the MRB-204 argument itself.
        # Design writes one line above each beam saying what it shows —
        # "Two pulls the opposite way: one cancels part of the other." —
        # and one below saying why the shape is a beam: "That is why this
        # relationship gets a beam and not a triangle: nothing here is
        # being multiplied." Three P4 pages shipped the drawing with both
        # sentences missing, so the page asserted a shape and never said
        # why. Both are optional, so no existing figure moves a byte.
        cap = ('<p class="ks3-formula-figcaption">%s</p>' % rich(fig["caption"])
               ) if fig.get("caption") else ""
        note = ('<p class="ks3-formula-fignote">%s</p>' % rich(fig["note"])
                ) if fig.get("note") else ""
        return ('<div class="ks3-formula-figure">%s%s%s</div>'
                % (cap, SVG_ART[art](fig), note))

    shape = fig.get("shape")
    if shape != "balance":
        raise ValueError(
            "formula figure shape %r is not drawn, and it names no `art`. "
            "`balance` is the sum's figure; a product's figure is the "
            "`triangle` key, which has its own renderer; anything else is a "
            "drawer in the unit's own ks3_art module." % shape)
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
        # ⊕ MRB-220 fix (24 Aug 2026 run): the covered plate must ARRIVE
        # covered. `hidden` was unconditional here, so before ks3.js ran the
        # bar painted fully open — pressed button beside it, result sentence
        # already filled in — handing the student the answer the block exists
        # to withhold. Same conditional shape as the triangle's notes
        # (r_formula_triangle). wireCoverBar's load-time show() is now a no-op.
        return ('<g class="ks3-bar-cover" data-cover-plate="%s"%s>'
                '<rect x="%.2f" y="%d" width="%.2f" height="%d" rx="%d" '
                'class="ks3-bar-plate"></rect>'
                '<text x="%.2f" y="%d" text-anchor="middle" '
                'class="ks3-bar-ghost" style="font-size:%dpx">%s</text></g>'
                % (e(key), "" if key == covered else " hidden",
                   x, y, w, H, R, x + w / 2.0, y + 36, size, t(label)))

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


def _reveal_id_attr(a):
    """⊕ MRB-277, 21 Aug 2026 — the generic reveal panel's OWN anchor, if it has one.

    THE DEFECT. The generic reveal panel carries no id, so a `confronted_by`
    that means "the panel where this belief is answered" has nothing to name
    and names its SURROUNDING ACTIVITY instead — four times in C4, three in
    C3. The join still resolves, so no gate complained; what is lost is
    precision. `confronted_by` is the record of WHERE a misconception is
    killed, and pointing it at the activity says "somewhere in here".

    THE PATTERN, AND THE GUARANTEE. This is exactly what `r_figure` gained in
    `_id_attr(block)`: the attribute is emitted ONLY when the author writes
    one, so every existing activity renders byte-for-byte as before and no
    page moves until somebody opts in. `reveal_anchor` rather than `anchor`
    because an activity's `anchor` already names the SECTION the rail points
    at, and one activity can own both.

    The 92px `scroll-margin-top` that keeps an anchor clear of the sticky bar
    is a rule on `.ks3-lesson [id]`, so it follows from emitting the id.
    """
    ra = a.get("reveal_anchor")
    return (' id="%s"' % e(ra)) if ra else ""


def _require_slug(entry):
    """A `requires` edge as the slug the registry is keyed by.

    ⊕ MRB-245 / B7. `references` has accepted both a bare slug and a
    `{unit, lesson, why}` record since B1 — the dict form is REQUIRED there the
    moment an edge crosses a unit boundary — and `requires` accepted only the
    bare slug. b7-03 requires `food-tests`, which is B3's, and authored it in
    the shape §4.6 taught it for a cross-unit edge. The build did not report a
    schema violation: it raised `cannot use 'dict' as a dict key` out of the
    cycle check, three functions away from the record.

    Both fields name a lesson and both resolve against the same slug-keyed
    registry, so one spelling now works in both. `requires` still needs no unit
    code to find its target — the registry is flat — so the `unit` key is
    accepted and ignored rather than checked, exactly as a same-unit
    `references` string is.
    """
    if isinstance(entry, dict):
        return entry.get("lesson") or entry.get("slug") or ""
    return entry


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


# ⊕ MRB-223, 24 Aug 2026 — THE WORD `draft` IS OUT OF THIS LINE.
#
# It used to read "...every scientific claim is checked before a lesson
# leaves draft", and that sentence is on ALL 297 KS3 pages, in the footer,
# where a student reads it. MRB-221 revoked the per-lesson review marker
# and the browse-list Draft badge, and made `verify_ks3.py` assert the
# marker's ABSENCE — and this line survived all of it, because it is
# emitted by the engine rather than by a lesson record and nothing was
# looking at its wording. `verify_ks3.py`'s sweep for the revoked marker
# is keyed to the marker, not to the word, so it passed throughout.
#
# A built lesson ships looking finished. The provenance claim is kept in
# full — it is the useful half — and the process state is dropped, because
# a student-facing page carries teaching and not commentary about the
# platform's own workflow (§8.10).
#
# ⚠️ SHARED FILE. One string literal in `build_ks3.py`, and it moves every
# KS3 page's bytes. Announced in the MRB-223 report under
# `docs/ks3/worktrees.md` §2.
LEGAL_LINE = ('<p class="ks3-legal">Lesson content © MrBadmusAI. Written '
              'and checked by a qualified science teacher.</p>')


def r_endmatter(cards, tutor=None):
    """The end-matter grid. `cards` is [(heading, [<li>…]), …].

    A card with no items is omitted — an empty "Before this lesson" is a
    promise the lesson did not make. The tutor card has no items and always
    renders, because it is an offer rather than a list.

    ⊕ MRB-257 · audit 6.3 — the caller now passes a "Where to next" card built
    from the unit order. It is a card in this grid and nothing new: MRB-205
    binds, Design drew the endmatter and this is one more section inside it.
    `repeat(auto-fit, minmax(250px, 1fr))` takes a fifth card without any
    change to the layout.
    """
    out = []
    for heading, items in cards:
        if not items:
            continue
        out.append('<section><h2>%s</h2><ul>%s</ul></section>'
                   % (e(heading), "".join(items)))

    # ⊕ MRB-257 · audit 6.2 — A REAL BUTTON, BECAUSE THERE IS NOW A REAL TUTOR.
    #
    # ⛔ The paragraph that used to live here explained why this was a <span>,
    # and before that an <a href="#ks3-tutor"> pointing at an id no KS3 page
    # contains. Both were right at the time: §8.8 said a KS3 student could
    # reach no tutor, so the card showed what it WOULD look like. `tutor_mount`
    # ends that — the chat engine is on the page and this control opens it.
    #
    # The `anchor` compromise goes with it, and that is the point of the fix.
    # A lesson could name one of its own sections and the card would scroll
    # there instead; all 58 biology lessons did, and on `the-menstrual-cycle`
    # at 390px it scrolled the reader 9,768px BACKWARDS to a section they had
    # already finished. A card that says "Ask about this lesson" and answers by
    # moving the page is not a tutor, and relabelling it to what it did would
    # have been the honest version of a worse product.
    #
    # ⚠️ A BUTTON, NOT A LINK, and the distinction is load-bearing: this
    # performs an action on the page rather than going to an address. The
    # audit's own accessibility baseline is "zero bare interactive elements",
    # and `verify_ks3.py` asserts every KS3 control is a real `<button>`.
    #
    # The inline style supplies only what a `<button>` needs and an `<a>` did
    # not — the UA border, the UA font-family and the pointer. It deliberately
    # does NOT restate `font-size` or `font-weight`: those come from
    # `.ks3-tutor-cta` in shared/ks3.css and an inline copy would outrank the
    # stylesheet and freeze them. Handed off to be folded into that rule.
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
    cta = ('<button type="button" class="ks3-tutor-cta" data-open-chat>'
           '%s %s</button>' % (label, MARK_ARROW))
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

    # ⊕ MRB-249 — `mirrors` names an EARLIER stop whose completion this stop
    # shares. Design's own `isDone()` is a rail-level function and on 33 of her
    # 48 lesson pages it returns the SAME expression for two consecutive ids —
    # `if (id === 's-summary') return s.exits;` one line under
    # `if (id === 's-bench') return s.exits;`. The synthesis section is the
    # payoff of the instrument beside it: it carries no control of its own
    # because the instrument already took the student's commitment.
    #
    # Three earlier units read that as "a stop that cannot tick" and dropped it,
    # shipping a three-stop rail where Design drew four. That is an MRB-205
    # violation — Design draws, we render, and the page wins over the engine —
    # and it is now gated both ways by `check_rail_matches_design`.
    payload = json.dumps([{"anchor": s["anchor"],
                           "label": s.get("label", ""),
                           "mirrors": s.get("mirrors", ""),
                           "done_when": s.get("done_when", "")}
                          for s in stages], separators=(",", ":"),
                         sort_keys=True)
    return ('<div class="ks3-rails" data-rail-stages="%s">%s%s</div>'
            % (e(payload), side, top))


# ── pages ────────────────────────────────────────────────────────────────

def ks4_bridge_href(link):
    return "/%s/%s/%s.html" % (KS4_BRIDGE_PATHWAY, KS4_BRIDGE_TIER, link)


def lesson_neighbours(units):
    """`slug → (previous, next)`, each an `(unit, lesson)` pair or None.

    ⊕ MRB-257 · audit 6.3 — THERE WAS NO FORWARD MOVE ANYWHERE IN 58 LESSONS.
    Zero elements matching next/previous/continue, zero `<link rel="next">`.
    Eleven non-terminal lessons had no link at all to the next lesson in their
    own unit; nine of the eleven last-in-unit lessons had no link into the
    following unit, and on `unicellular-organisms` all three in-`<main>` links
    pointed backwards. After roughly eight thousand pixels of scrolling, the
    reward for finishing was a page with no way on.

    Nothing new is invented to fix it. The unit index already publishes this
    order; this reads the same list.

    ⚠️ TWO KINDS OF SLOT ARE SKIPPED, for two different reasons.

    A `reference_to` slot has no page at all — §4.6 says the owning unit
    renders it — so a link to one would be a 404, which is the defect MRB-209's
    gate exists to catch.

    An UNAUTHORED slot does have a page, and it is skipped anyway. "Next
    lesson" that lands on *This lesson has not been written yet* is a worse
    ending than no control: the student did the work, pressed the one forward
    affordance the page offers, and got a placeholder. The unit index still
    lists the slot honestly, which is the right place for a coming-soon row.

    Rollover is within a DISCIPLINE, in the order `build_ks3()` walks its units
    — so the last lesson of a unit points at the first lesson of the next unit,
    and the last authored lesson in a discipline points at nothing rather than
    at another subject.
    """
    nbrs = {}
    for disc in ("biology", "chemistry", "physics"):
        seq = [(u, l) for u in units if u["discipline"] == disc
               for l in u["lessons"]
               if l.get("authored") and not l.get("reference_to")]
        for i, (u, l) in enumerate(seq):
            nbrs[l["slug"]] = (seq[i - 1] if i else None,
                               seq[i + 1] if i + 1 < len(seq) else None)
    return nbrs


def _lesson_href(unit, lesson):
    return "/ks3/%s/%s/%s.html" % (unit["discipline"], unit["slug"],
                                   lesson["slug"])


def lesson_page(unit, lesson, registry, units_by_code, neighbours=None):
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
    #
    # ⊕ MRB-244 — `support_heading`, an authored override, shaped exactly like
    # `connects_heading` on the end-matter below: the lesson's own string when
    # it declares one, the fixed label when it does not. Every shipped lesson
    # is byte-identical across the change because all 35 of them ship
    # `"support": []` and the layer renders nothing at all.
    #
    # ⚠️ AND THE FIXED LABEL IS WRONG FOR THE FIRST UNIT THAT USES THE SLOT.
    # "Need a hand?" is a study-support offer — the right words above a hint
    # for a student who is stuck on the science. B6 is the first unit in the
    # key stage with a non-empty `support[]`, and all three of its layers are
    # REFERRAL blocks: Design heads them "If any of this is about you or
    # someone you know", and points at PSHE/RSE, a trusted adult, the school
    # nurse, a pharmacist or a GP. Left hard-coded, a page about somebody's
    # drug use would have offered help with the homework, and the student the
    # block was written for would not have recognised it as addressed to them.
    # That is a safeguarding property of the page, not a caption.
    body.append(r_layer(lesson, lesson.get("support") or [],
                        "ks3-support",
                        lesson.get("support_heading") or "Need a hand?"))

    # Prerequisites (§4.9) — student-facing use of the graph.
    prereqs = []
    for slug in [_require_slug(x) for x in lesson.get("requires", [])]:
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
        tgt = registry.get(r["lesson"])
        # ⊕ MRB-248 / B11 — THE HREF IS BUILT FROM THE TARGET'S OWN UNIT, and
        # this is a repair.
        #
        # A bare-string reference is read as "a lesson in this unit" (the
        # paragraph above), and the href was then composed from the REFERRING
        # lesson's unit. b11-01 authored `"leaves-built-for-the-job"` as a bare
        # string; that lesson is B7's, and the page shipped a link to
        # `/ks3/biology/evolution-extinction-and-biodiversity/leaves-built-for-
        # the-job.html`, which does not exist. MRB-209's link gate caught it —
        # the gate working exactly as it should — but the engine already knew
        # the answer: the registry is flat and every entry carries its own
        # `_unit`, so the correct path was one lookup away the whole time.
        #
        # ⚠️ AND AN AUTHORED `unit` THAT DISAGREES IS A BUILD FAILURE, not a
        # silent correction. A dict-form reference naming the wrong unit is the
        # author believing something false about where a lesson lives, and
        # quietly fixing the href would leave that belief in the record for the
        # next person to copy.
        if tgt and tgt.get("_unit"):
            if not isinstance(lesson.get("references") or [], str) \
                    and r.get("unit") and r["unit"] != tgt["_unit"] \
                    and r["unit"] != unit["code"]:
                raise ValueError(
                    "%s: references %r as living in unit %s, and it is %s's. "
                    "The registry is flat and slugs are globally unique, so "
                    "this is a statement about the world that is wrong rather "
                    "than a routing detail — and left alone it ships a link to "
                    "a page that does not exist."
                    % (lesson.get("slug"), r["lesson"], r["unit"],
                       tgt["_unit"]))
            tgt_unit = units_by_code.get(tgt["_unit"])
        else:
            tgt_unit = units_by_code.get(r["unit"])
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
    # ⊕ MRB-257 · audit 2.8 — AND IF THE RECORD SAYS NEITHER, THE RAIL STILL
    # RENDERS. It was missing on 13 of 58 lessons, and not as an opener
    # exemption: B4-02 and B4-05 carried it and B4-03 and B4-04 did not, while
    # openers elsewhere correctly read "Nothing — this is where the unit
    # starts." It disappeared exactly where B5's dependency chain is tightest —
    # seven of the eight reproduction lessons — so the student who most needed
    # to be told what comes first was the one told nothing.
    #
    # An empty card was the right rule when the alternative was inventing a
    # prerequisite. It is the wrong rule now, because the generator can say
    # something true without inventing anything: position in the unit is data
    # the unit index already publishes, and the two truthful readings of "no
    # declared prerequisite" are different sentences.
    #
    # ⚠️ THE OPENER SENTENCE IS NOT SAFE FOR A NON-OPENER. Ten of the thirteen
    # are lessons 2 to 7 of their unit; telling a reader standing on B5 lesson
    # 5 that "this is where the unit starts" would be false, and a rail that
    # lies is worse than a rail that is absent. So the fallback is keyed to
    # position, and the non-opener form states the sequence rather than
    # claiming an absence of prerequisites.
    #
    # It states it in PROSE and does not link: the forward and backward moves
    # are the "Where to next" card below, and two controls to the same lesson
    # in one endmatter is a grid that repeats itself.
    #
    # ⚠️ This is a floor, not a substitute for `requires`. Every one of the
    # thirteen is listed in the run report so the real dependency edges can be
    # authored in the records, where the prerequisite graph is validated.
    if not prereqs:
        prev = (neighbours or {}).get(lesson["slug"], (None, None))[0]
        same_unit = prev and prev[0]["code"] == unit["code"]
        prereqs = ['<li><span class="ks3-endmatter-prose">%s</span></li>'
                   % t("This follows on from %s." % prev[1]["title"]
                       if same_unit
                       else "Nothing — this is where the unit starts.")]
    if not ks4 and lesson.get("ks4_becomes"):
        ks4 = ['<li><span class="ks3-endmatter-prose">%s</span></li>'
               % rich(lesson["ks4_becomes"])]

    # ⊕ MRB-220 — the middle card's heading is authorable. It was fixed at
    # "Connects to", which is right for B1's sideways links and wrong for
    # Design's B2 pages: all four head it **"Next in this unit"** and point
    # FORWARD at the next lesson. A fixed heading would have rendered a card
    # Design did not draw over content Design did draw. The default is
    # unchanged, so no shipped lesson moves.
    # ⊕ MRB-257 · audit 6.3 — the forward and backward move, from the order
    # the unit index already knows. An ordinary endmatter card (MRB-205: no new
    # component), and the same `<li><a>` + `<p>` shape the "Connects to" card
    # uses for a reference with a `why`.
    #
    # The next lesson comes FIRST. A student reaching the end of a lesson is
    # looking for the way on; the way back is the one they have just come from.
    #
    # The unit line is printed only when the move crosses a unit boundary,
    # which is where a title alone stops being enough to know where you are
    # going. `_require_slug`'s registry is not consulted: `neighbours` is built
    # from the same `units` list this page was rendered from, so a link here
    # cannot point at a page the build did not write.
    onward = []
    prev_n, next_n = (neighbours or {}).get(lesson["slug"], (None, None))
    for pair, lead in ((next_n, "Next"), (prev_n, "Previous")):
        if not pair:
            continue
        u2, l2 = pair
        crossing = ('<p>%s</p>' % t(u2["title"])) if u2["code"] != unit["code"] \
            else ""
        onward.append('<li><a href="%s">%s: %s %s</a>%s</li>'
                      % (e(_lesson_href(u2, l2)), t(lead), t(l2["title"]),
                         MARK_ARROW, crossing))

    body.append(r_endmatter([("Before this lesson", prereqs),
                             (lesson.get("connects_heading") or "Connects to",
                              connects),
                             ("At GCSE this becomes", ks4),
                             ("Where to next", onward)],
                            tutor=lesson.get("tutor")))
    # ⊕ MRB-257 · audit 6.4 — THE CONFIDENTIAL SERVICE, NAMED, IN SMALL TYPE.
    #
    # RULED by Mide on 19 Aug 2026 (MRB-233 comment 2). Eight lessons carry a
    # safeguarding block and all three drugs lessons defer to "your school's
    # PSHE materials"; a corpus sweep for `childline|0800 1111|nspcc|
    # samaritans|papyrus|frank|shout` across all 58 rendered lessons returned
    # ZERO. mrbadmus.com is a public site, and the student who most needs that
    # block is reading it alone at eleven at night, when a school folder is not
    # reachable.
    #
    # The ruling, exactly: the service is `Childline`, the number is
    # `0800 1111`, joined by a spaced em dash. The "your school's PSHE
    # materials" deferral STAYS as the daytime route; Childline is the
    # out-of-hours one. Shout and FRANK were offered and not taken up.
    #
    # ⚠️ THE TREATMENT IS THE RULING TOO, and it is why this is a `ks3-legal`
    # foot line and not a card. §8.10: anything of this kind sits small, at the
    # bottom edge, alongside the existing school-nurse / pharmacist / GP
    # routes, NEVER a callout block. A helpline should be findable and quiet.
    # It is emitted before `safety_note` because it is the most specific thing
    # on the page and the standing legal line is the least.
    #
    # The generator owns the SLOT; the eleven strings are authored in the
    # records, because which lessons carry a safeguarding block is a judgement
    # about content and not something a renderer can derive — only four lessons
    # in the key stage have a non-empty `support[]`, and the ruled set is
    # eleven.
    if lesson.get("safeguarding_note"):
        sg = lesson["safeguarding_note"]
        # ⊕ MRB-223, 25 Aug 2026 — the SAME slot, the SAME treatment, and
        # Design's WORDS character for character. Her p10-01 block is an
        # eyebrow line ("If a magnet has been swallowed, or you are worried
        # about someone") over a body that bolds the helpline. Folding the
        # eyebrow into the sentence and escaping the <strong> changed her
        # characters; a dict form keeps them. Position and type are still
        # the ruled foot line (audit 6.4) — only the text is hers verbatim.
        if isinstance(sg, dict):
            body.append('<p class="ks3-legal"><strong>%s</strong> %s</p>'
                        % (t(sg["eyebrow"]), rich(sg["body"])))
        else:
            body.append('<p class="ks3-legal">%s</p>' % t(sg))
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

    # ⊕ MRB-257 · audit 6.12 — `meta_description`, an authored override.
    #
    # The description has always been the `big_question`, which is also printed
    # on the page in display type. 41 of 70 KS3 pages measured over 160
    # characters and truncate in a search result; two are over 300 and the
    # longest is 380. Shortening the `big_question` to fix a search snippet
    # would edit the sentence a student reads at the top of the lesson, which
    # is the wrong trade — so the two strings come apart here, and the record
    # can carry a short one for search without touching the page. Absent, the
    # behaviour is exactly what it was.
    #
    # ⚠️ NOT truncated here. A generator that cuts at 160 characters cuts
    # mid-word, and the result is a search snippet that reads as broken rather
    # than as short. The over-long strings are listed in the run report for
    # authoring.
    head_links = ""
    if next_n:
        head_links += '<link rel="next" href="%s"/>\n' % e(canon(
            _lesson_href(next_n[0], next_n[1])))
    if prev_n:
        head_links += '<link rel="prev" href="%s"/>\n' % e(canon(
            _lesson_href(prev_n[0], prev_n[1])))

    return shell(lesson["title"], "\n".join(x for x in body if x), "", disc,
                 lesson.get("meta_description")
                 or lesson.get("big_question", ""),
                 lesson_slug=lesson["slug"],
                 trail_html=trail, rail_html=r_rail(lesson),
                 canonical=_lesson_href(unit, lesson),
                 head_links=head_links,
                 og_type="article",
                 tail_html=tutor_mount(
                     disc, "%s — %s" % (unit["title"], lesson["title"])))


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
                 lesson_slug=lesson["slug"],
                 canonical="/ks3/%s/%s/%s.html" % (disc, unit["slug"],
                                                   lesson["slug"]),
                 og_type="article")


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
    # ⊕ MRB-257 · audit 6.5 — `needs_js=False`. A unit index is a heading, an
    # intro and an ordered list of links: `wireSims`, `wireLadder`, `wireRail`
    # and `wirePicker` all find nothing here, and 174 KB downloaded to do
    # nothing was competing with the stylesheet that blocks first paint.
    # ⊕ MRB-257 · audit 6.12 — `meta_description` on a unit too, same shape and
    # same reason as the lesson's: `intro` is printed at the top of the page in
    # display type AND used as the search snippet, and seven of the eleven
    # biology unit intros run past the 160 characters a result truncates at.
    # Absent, the behaviour is exactly what it was.
    return shell(unit["title"], body, crumb, disc,
                 unit.get("meta_description") or unit.get("intro")
                 or unit["title"],
                 canonical="/ks3/%s/%s/index.html" % (disc, unit["slug"]),
                 needs_js=False)


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
    # ⊕ MRB-257 · audit 6.7 — THE HUB HAD AN ELEVEN-CHARACTER DESCRIPTION.
    #
    # No `description` was passed, so `desc = description or title` fell back
    # to the title and `/ks3/biology/` shipped `content="KS3 Biology"` — on the
    # one page in the tree a search for "KS3 biology revision" actually lands
    # on. Every lesson and all eleven unit indexes had a real one; the hub
    # above them had the shortest string on the estate.
    #
    # Composed rather than tabulated so chemistry and physics get the same
    # treatment the moment their units land, and so the unit count cannot go
    # stale. Kept under 160 characters, which is where a search result
    # truncates (audit 6.12).
    return shell("KS3 %s" % DISCIPLINE_TITLES[disc], body, crumb, disc,
                 "Free KS3 %s — %d units of lessons you work through, each "
                 "with something to try, a mastery ladder and answers you can "
                 "check." % (DISCIPLINE_TITLES[disc], len(units)),
                 canonical="/ks3/%s/index.html" % disc,
                 needs_js=False)


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
    185 lesson slots and, today, 185 distinct slugs — but the tuple key is not
    an optimisation, it is the §4.6 reference slot's requirement: a referenced
    lesson appears in two units under one slug, and a slug-keyed lookup
    silently drops one of them into the wrong year. `energy-in-food` was the
    worked example when B3 carried it as a reference slot; no reference slot is
    declared at present, and the keying must not be relaxed on that basis.

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
                 main_class="is-browse",
                 canonical="/ks3/year-%d/index.html" % year,
                 needs_js=False)


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
                 main_class="is-browse",
                 canonical="/ks3/year-%d/%s/index.html"
                           % (year, half_term_slug(half_term)),
                 needs_js=False)


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
                 main_class="is-browse",
                 canonical="/ks3/year-%d/%s/%s/index.html"
                           % (year, half_term_slug(half_term), disc),
                 needs_js=False)


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
  </div>
  <ul class="ks3-unit-grid is-browse">%(years)s</ul>
</section>

<section class="ks3-hub-sec">
  <div class="ks3-sec-head">
    <h2>Or go by subject</h2>
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
    # ⚠️ `needs_js` stays TRUE here, alone among the index pages. This is the
    # page that carries MRB-212's lesson picker, and `wirePicker()` in ks3.js
    # is the whole of its behaviour — without the tag the disclosure button
    # would never open. See shell()'s docstring.
    return shell("KS3 Science", body, crumb, None,
                 "Free KS3 Science revision — Years 7 to 9, all three sciences.",
                 main_class="is-browse is-hub",
                 canonical="/ks3/index.html")


# ── validation (§9 gates) ────────────────────────────────────────────────

def validate(units, registry):
    """Fail loudly. §4.9: a cycle is a build-blocking defect."""
    problems = []

    # 1. Prerequisite graph must be acyclic.
    graph = {s: [r for r in map(_require_slug, l.get("requires") or [])
                 if r in registry]
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
        for r in map(_require_slug, l.get("requires") or []):
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

    # 9. Registration and placement must agree, both ways (MRB-271).
    #
    # Registry gates 2 and 3 — see `ks3_art/__init__.py` for what each is for.
    # They live HERE rather than at import because they need the content data,
    # and they report through `problems` rather than raising so that a lane
    # gets every finding in one run instead of one per rebuild.
    #
    # `GENERIC_ACTIVITY_KINDS` and `_KIND_FN_BY_BLOCK_TYPE` are the two
    # legitimate ways a placed kind can have no `KIND_FN`: the generic
    # prompt/options branch draws the first, and the block type draws the
    # second. Everything else that is placed must be registered, and
    # everything registered must be placed.
    problems += ks3_art.check_placements(
        _KS3_ART, units,
        generic_kinds=GENERIC_ACTIVITY_KINDS,
        block_type_kinds=_KIND_FN_BY_BLOCK_TYPE)

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
    neighbours = lesson_neighbours(units)

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
                page = (lesson_page(u, l, registry, units_by_code,
                                    neighbours)
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

    # ⊕ MRB-257 · audit 2.9 — RAIL VOCABULARY DRIFT, REPORTED EVERY BUILD.
    #
    # 52 lessons head the middle endmatter card "Connects to"; three B2 lessons
    # head it "Next in this unit" and one "Taught in full in". The consequence
    # the audit measured is not cosmetic: a card headed "Next in this unit"
    # gets authored with only the next lesson in it, so B2 never points
    # sideways at the B4 and B8 material it depends on. The label shaped the
    # content.
    #
    # ⚠️ AND THE OVERRIDE IS NOT REMOVED, deliberately. `connects_heading` is
    # authored on 16 lessons, and killing the read site would take
    # "Continues in Physics" off `energy-in-food-and-what-you-need` — which is
    # the one place the label is carrying real information a generic heading
    # cannot — and would restyle eleven live CHEMISTRY lessons that were never
    # in the audit's scope. A fix that breaks two units to tidy one is not a
    # fix. The default is unchanged, the divergence is now VISIBLE on every
    # build, and which records should move is a content decision.
    #
    # This is also why audit 6.3's prev/next matters here: with a real forward
    # control on every lesson, a card headed "Next in this unit" is the second
    # forward affordance in one endmatter, and the case for the override is
    # weaker than it was when it was written.
    drift = [(u["code"], l["slug"], l["connects_heading"])
             for u in units for l in u["lessons"]
             if l.get("authored") and l.get("connects_heading")
             and l["connects_heading"] != "Connects to"]
    if drift:
        print("  ⚠️  rail vocabulary: %d lesson(s) head the connects card with "
              "something other than \"Connects to\"" % len(drift))
        for code, slug, head in drift:
            print("       %-4s %-42s %s" % (code, slug, head))

    # ⊕ MRB-257 · audit 6.12 — meta descriptions that truncate in a search
    # result. Reported rather than cut: see lesson_page(). 160 is where Google
    # stops; the audit measured 41 of 70 KS3 Biology pages over it, two over
    # 300, the longest 380.
    longd = []
    for u in units:
        # A unit index takes `intro`, which is also printed on the page — the
        # same two-jobs-one-string problem the lessons have, and it needs the
        # same `meta_description` treatment in `structure.py`.
        ud = u.get("meta_description") or u.get("intro") or ""
        if u["authored_count"] and len(ud) > 160:
            longd.append((u["code"], u["slug"] + "/index", len(ud)))
        for l in u["lessons"]:
            if not l.get("authored") or l.get("reference_to"):
                continue
            d = l.get("meta_description") or l.get("big_question") or ""
            if len(d) > 160:
                longd.append((u["code"], l["slug"], len(d)))
    if longd:
        longd.sort(key=lambda r: -r[2])
        print("  ⚠️  meta description over 160 chars on %d page(s) — author "
              "`meta_description` (longest %d)" % (len(longd), longd[0][2]))
        for code, slug, ln in longd:
            print("       %-4s %-42s %d" % (code, slug, ln))

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
    # ⊕ MRB-271 — BUILD YOUR OWN TREE, NEVER SOMEBODY ELSE'S.
    #
    # Every path in this file is relative, and a relative path resolves against
    # the CURRENT DIRECTORY, not against this script. So
    # `python3 /elsewhere/build_ks3.py` run from inside a worktree imported
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
    build_ks3()
