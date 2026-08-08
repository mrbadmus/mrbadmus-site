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


# ── shell ────────────────────────────────────────────────────────────────

NAV_BRAND = (
    '<a class="nav-brand" href="/index.html">'
    '<svg class="brand-logo" width="22" height="22" viewBox="0 0 24 24" fill="none">'
    '<path d="M4 6l4-4 4 4" stroke="url(#navGrad)" stroke-width="3" '
    'stroke-linecap="round" stroke-linejoin="round"/>'
    '<path d="M4 6l4-4 4 4" stroke="url(#navGrad)" stroke-width="3" '
    'stroke-linecap="round" stroke-linejoin="round" transform="translate(4,6)"/>'
    '<defs><linearGradient id="navGrad" x1="4" y1="2" x2="16" y2="12" '
    'gradientUnits="userSpaceOnUse"><stop stop-color="#FFD93D"/>'
    '<stop offset="1" stop-color="#FF6B35"/></linearGradient></defs>'
    '</svg> MrBadmusAI</a>'
)


def crumbs(parts):
    """KS3 › Chemistry › Particles and their behaviour  (§8.5)."""
    out = []
    for i, (label, href) in enumerate(parts):
        if href and i < len(parts) - 1:
            out.append('<a href="%s">%s</a>' % (e(href), e(label)))
        else:
            out.append('<span aria-current="page">%s</span>' % e(label))
    return ('<nav class="ks3-crumbs" aria-label="Breadcrumb">%s</nav>'
            % '<span class="ks3-crumb-sep" aria-hidden="true">›</span>'.join(out))


def shell(title, body, crumb_html="", discipline=None, description=""):
    """KS3 page shell. `class="rd"` + `data-mode="ks3"` per §8.5."""
    accent = ("--subject: var(%s);" % SUBJECT_TOKEN[discipline]) if discipline else ""
    return """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>%(title)s · MrBadmusAI KS3</title>
<meta name="description" content="%(desc)s"/>
<link rel="stylesheet" href="/shared/tokens.css"/>
<link rel="stylesheet" href="/shared/styles.css"/>
<link rel="stylesheet" href="/shared/nav.css"/>
<link rel="stylesheet" href="/shared/ks3.css"/>
</head>
<body class="rd" data-mode="ks3"%(style)s>
<nav class="ks3-nav">%(brand)s
  <a class="ks3-nav-link" href="/ks3/index.html">KS3</a>
</nav>
<main class="ks3-main">
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
        "crumbs": crumb_html,
        "body": body,
    }


# ── segment renderers (§5.1.1 vocabulary) ────────────────────────────────

def r_hook(lesson):
    p = lesson.get("phenomenon") or {}
    return ("""<section class="ks3-block ks3-hook">
  <p class="ks3-eyebrow">Start here</p>
  <h2>%s</h2>
  <p class="ks3-hook-prompt">%s</p>
  <p class="ks3-commit"><strong>%s</strong></p>
</section>""" % (e(p.get("title", "")), e(p.get("prompt", "")), e(p.get("commit", ""))))


def r_explainer(lesson, block):
    for b in lesson.get("core", []) + lesson.get("stretch", []):
        pass
    return ('<section class="ks3-block ks3-explainer"><p>%s</p></section>'
            % e(block.get("text", "")))


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
</figure>""" % (e(fig["caption"]), e(fig["caption"])))
    return ('<figure class="ks3-figure"><img src="/ks3/figures/%s.svg" alt="%s"/>'
            '<figcaption>%s</figcaption></figure>'
            % (e(fig["id"]), e(fig["caption"]), e(fig["caption"])))


def r_keyword(lesson, block):
    terms = block.get("terms", [])
    vocab = {v["term"]: v for v in lesson.get("vocabulary", [])}
    rows = []
    for t in terms:
        v = vocab.get(t)
        if not v:
            continue
        note = ('<p class="ks3-vocab-note">%s</p>' % e(v["note"])) if v.get("note") else ""
        rows.append('<div class="ks3-vocab"><dt>%s</dt><dd>%s%s</dd></div>'
                    % (e(v["term"]), e(v["definition"]), note))
    if not rows:
        return ""
    return ('<section class="ks3-block ks3-keywords"><h3>Words to know</h3>'
            '<dl class="ks3-vocab-list">%s</dl></section>' % "".join(rows))


def _activity(lesson, act_id):
    return next((a for a in lesson.get("activities", []) if a["id"] == act_id), None)


# ── activity-level interactions (NOT new §5.1.1 block types) ─────────────
#
# The block vocabulary is closed at ten. Flip cards and particle labs are
# authored as ACTIVITY keys (`cards`, `sim`) precisely so they can appear
# inside an existing check / practical / misconception block without widening
# that vocabulary — an activity is already the unit that owns a prompt, options
# and a reveal, and these are two more ways of answering the same prompt.

def r_cards(cards):
    """Click-to-reveal cards.  Contract: shared/ks3.js `wireCards`.

    The back is emitted with `hidden` so the answer is not on screen in the
    window between first paint and ks3.js running — a card that shows its back
    for 200ms has given the game away, and on a slow phone that window is not
    200ms. ks3.js owns `aria-expanded` and `.is-flipped` from then on.

    role="list" matches .ks3-options: both are `list-style: none`, which drops
    list semantics in Safari/VoiceOver unless the role is restated.
    """
    items = []
    for c in cards:
        items.append(
            '<li><button type="button" class="ks3-card-btn">'
            '<span class="ks3-card-front">%s</span>'
            '<span class="ks3-card-back" hidden>%s</span>'
            '</button></li>'
            % (e(c.get("front", "")), e(c.get("back", ""))))
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
SIM_CONTROLS = ("temperature", "volume", "particles", "medium")

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
    return (
        '<div class="ks3-sim" data-sim="%s" data-controls="%s">'
        '<canvas class="ks3-sim-canvas" width="560" height="200" role="img" '
        'aria-label="%s"></canvas>'
        '<p class="ks3-sim-cover">Make your prediction first — then the lab '
        'runs.</p>'
        '<div class="ks3-sim-controls"></div>'
        '<p class="ks3-sim-readout" role="status"></p>'
        '<p class="ks3-sim-caption">%s</p>'
        '</div>'
        % (e(kind), e(controls), e(label), e(caption)))


def r_activity(lesson, act_id, kind_class, heading):
    a = _activity(lesson, act_id)
    if not a:
        return ""
    parts = ['<section class="ks3-block %s" data-activity="%s">' % (kind_class, e(act_id))]
    parts.append('<p class="ks3-eyebrow">%s</p>' % e(heading))
    if a.get("demand"):
        parts.append('<p class="ks3-demand" hidden>Demand: %s</p>' % e(a["demand"]))
    parts.append("<p>%s</p>" % e(a.get("prompt", "")))
    if a.get("options"):
        opts = "".join(
            '<li><button type="button" class="ks3-option" data-i="%d">%s</button></li>'
            % (i, e(o)) for i, o in enumerate(a["options"]))
        parts.append('<ul class="ks3-options" role="list">%s</ul>' % opts)
    # After the options, before the reveal: the prediction is committed first,
    # then the thing that tests it, then the words that settle it.
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
            % (e(f.get("formula")), e(f.get("insert")),
               e(f.get("fix")), e(f.get("answer"))))
    if a.get("reveal"):
        # Law 4: the reveal is gated behind the student's commitment.
        parts.append('<div class="ks3-reveal" hidden data-reveal>%s</div>'
                     % e(a["reveal"]))
    if a.get("success"):
        items = "".join("<li>%s</li>" % e(s) for s in a["success"])
        parts.append('<details class="ks3-success"><summary>Check your answer</summary>'
                     '<ul>%s</ul></details>' % items)
    parts.append("</section>")
    return "".join(parts)


def r_ladder(lesson):
    lad = lesson.get("ladder") or {}
    rungs = [("recall", "① Recall"), ("apply", "② Apply"),
             ("explain", "③ Explain"), ("produce", "④ Produce")]
    out = ['<section class="ks3-block ks3-ladder" data-lesson="%s">' % e(lesson["slug"]),
           "<h2>Mastery ladder</h2>"]
    for key, label in rungs:
        q = lad.get(key)
        if not q:
            continue
        out.append('<div class="ks3-rung" data-rung="%s"><h3>%s</h3><p>%s</p>'
                   % (e(key), e(label), e(q.get("q", ""))))
        if q.get("options"):
            opts = []
            for i, o in enumerate(q["options"]):
                fb = (q.get("feedback") or {}).get(i, "")
                correct = "1" if i == q.get("answer") else "0"
                opts.append(
                    '<li><button type="button" class="ks3-option" data-i="%d" '
                    'data-correct="%s" data-feedback="%s">%s</button></li>'
                    % (i, correct, e(fb), e(o)))
            out.append('<ul class="ks3-options" role="list">%s</ul>' % "".join(opts))
        if q.get("success"):
            items = "".join("<li>%s</li>" % e(s) for s in q["success"])
            out.append('<details class="ks3-success">'
                       '<summary>Mark your answer against this list</summary>'
                       '<ul>%s</ul></details>' % items)
        out.append("</div>")
    out.append("</section>")
    return "".join(out)


BLOCK_RENDERERS = {
    "hook": lambda l, b: r_hook(l),
    "explainer": r_explainer,
    "figure": r_figure,
    "keyword": r_keyword,
    "quiz": lambda l, b: r_ladder(l),
    "summary": lambda l, b: (
        '<section class="ks3-block ks3-keynote"><h2>Key note</h2><p>%s</p></section>'
        % e(l.get("key_note", ""))),
    "misconception": lambda l, b: r_activity(
        l, b.get("id"), "ks3-misconception", "Think again"),
    "check": lambda l, b: r_activity(l, b.get("id"), "ks3-check", "Your turn"),
    "worked-example": lambda l, b: r_activity(
        l, b.get("id"), "ks3-worked", "Worked example"),
    "practical": lambda l, b: r_activity(l, b.get("id"), "ks3-practical", "Investigate"),
}

VALID_BLOCK_TYPES = set(BLOCK_RENDERERS)


def render_blocks(lesson, blocks):
    out = []
    for b in blocks:
        t = b.get("type")
        if t not in BLOCK_RENDERERS:
            raise ValueError(
                "Lesson %r uses block type %r, which is not in the §5.1.1 "
                "segment vocabulary. Valid types: %s. A new type needs an "
                "amendment to architecture.md, not a local addition."
                % (lesson["slug"], t, sorted(VALID_BLOCK_TYPES)))
        out.append(BLOCK_RENDERERS[t](lesson, b))
    return "\n".join(x for x in out if x)


# ── pages ────────────────────────────────────────────────────────────────

def ks4_bridge_href(link):
    return "/%s/%s/%s.html" % (KS4_BRIDGE_PATHWAY, KS4_BRIDGE_TIER, link)


def lesson_page(unit, lesson, registry, units_by_code):
    disc = unit["discipline"]
    base = "/ks3/%s/%s" % (disc, unit["slug"])
    crumb = crumbs([("KS3", "/ks3/index.html"),
                    (DISCIPLINE_TITLES[disc], "/ks3/%s/index.html" % disc),
                    (unit["title"], base + "/index.html"),
                    (lesson["title"], None)])

    head = ['<header class="ks3-lesson-head">',
            '<p class="ks3-eyebrow">%s · %s</p>' % (e(unit["title"]), e(lesson["family"])),
            "<h1>%s</h1>" % e(lesson["title"])]
    if lesson.get("big_question"):
        head.append('<p class="ks3-bigq">%s</p>' % e(lesson["big_question"]))
    if lesson.get("review_state") != "frozen":
        head.append('<p class="ks3-review-flag">Draft — not yet science-reviewed.</p>')
    head.append("</header>")

    body = ["".join(head), render_blocks(lesson, lesson.get("core", []))]

    stretch = lesson.get("stretch") or []
    if stretch:
        body.append('<section class="ks3-layer ks3-stretch">'
                    '<h2>Going further</h2>%s</section>'
                    % render_blocks(lesson, stretch))

    # `support` is present-but-empty by design until the support layer is
    # authored (§11 decision 4). The slot renders nothing; it is never absent
    # from the data.
    support = lesson.get("support") or []
    if support:
        body.append('<section class="ks3-layer ks3-support">'
                    '<h2>Need a hand?</h2>%s</section>'
                    % render_blocks(lesson, support))

    # Prerequisites (§4.9) — student-facing use of the graph.
    reqs = [registry[s] for s in lesson.get("requires", []) if s in registry]
    if reqs:
        items = "".join(
            '<li><a href="/ks3/%s/%s/%s.html">%s</a></li>'
            % (e(registry[r["slug"]]["_disc"]), e(r["_unit_slug"]), e(r["slug"]),
               e(r["title"])) for r in reqs)
        body.append('<section class="ks3-block ks3-prereqs"><h2>Before this lesson</h2>'
                    '<ul>%s</ul></section>' % items)

    # Cross-discipline references (§4.6) — must render gracefully BEFORE the
    # referenced unit exists. This is a §9 slice gate.
    refs = lesson.get("references") or []
    if refs:
        items = []
        for r in refs:
            tgt_unit = units_by_code.get(r["unit"])
            tgt = registry.get(r["lesson"])
            if tgt_unit and tgt and tgt.get("authored"):
                items.append(
                    '<li><a href="/ks3/%s/%s/%s.html">%s</a> — %s</li>'
                    % (e(tgt_unit["discipline"]), e(tgt_unit["slug"]),
                       e(r["lesson"]), e(tgt["title"]), e(r.get("why", ""))))
            else:
                label = tgt["title"] if tgt else r["lesson"]
                unit_title = tgt_unit["title"] if tgt_unit else r["unit"]
                items.append(
                    '<li><span class="ks3-pending">%s <em>(%s — coming soon)</em>'
                    '</span> — %s</li>'
                    % (e(label), e(unit_title), e(r.get("why", ""))))
        body.append('<section class="ks3-block ks3-refs">'
                    '<h2>Connects to</h2><ul>%s</ul></section>' % "".join(items))

    # KS4 bridge (§4.7).
    links = lesson.get("ks4_links") or []
    if links:
        items = "".join('<li><a href="%s">%s</a></li>'
                        % (e(ks4_bridge_href(l)), e(l.split("/")[-1].replace("-", " ")))
                        for l in links)
        body.append('<section class="ks3-block ks3-ks4"><h2>At GCSE this becomes</h2>'
                    '<ul>%s</ul></section>' % items)

    body.append('<section class="ks3-block ks3-tutor"><h2>Stuck? Ask Mr Badmus AI</h2>'
                '<p>Ask anything about this lesson.</p></section>')

    return shell(lesson["title"], "\n".join(body), crumb, disc,
                 lesson.get("big_question", ""))


def coming_soon_page(unit, lesson):
    """An honest placeholder. Structure-first — never a broken link (§11 dec 8)."""
    disc = unit["discipline"]
    base = "/ks3/%s/%s" % (disc, unit["slug"])
    crumb = crumbs([("KS3", "/ks3/index.html"),
                    (DISCIPLINE_TITLES[disc], "/ks3/%s/index.html" % disc),
                    (unit["title"], base + "/index.html"),
                    (lesson["title"], None)])
    body = """<header class="ks3-lesson-head">
  <p class="ks3-eyebrow">%s · %s</p>
  <h1>%s</h1>
</header>
<section class="ks3-block ks3-coming-soon">
  <p class="ks3-tag">Coming soon</p>
  <p>This lesson has not been written yet.</p>
  <p><a href="%s/index.html">Back to %s</a></p>
</section>""" % (e(unit["title"]), e(lesson["family"]), e(lesson["title"]),
                 e(base), e(unit["title"]))
    return shell(lesson["title"], body, crumb, disc,
                 "%s — coming soon" % lesson["title"])


def unit_index(unit, units_by_code, registry):
    disc = unit["discipline"]
    crumb = crumbs([("KS3", "/ks3/index.html"),
                    (DISCIPLINE_TITLES[disc], "/ks3/%s/index.html" % disc),
                    (unit["title"], None)])
    rows = []
    for i, l in enumerate(unit["lessons"], 1):
        if l.get("reference_to"):
            # §4.6 single-source: this slot is a cross-link, not a lesson. The
            # pointer below is architecture.md §4.5 ruling 3 (2026-07-27) — the
            # B3 → P2 forward reference is resolved as an explicit forward
            # pointer rather than an ownership flip, so a student meeting a slot
            # taught elsewhere is told so honestly instead of being dropped into
            # another discipline's unit with no explanation.
            #
            # ⚠️ The wording deliberately does NOT name a year, and the pointer
            # is NOT conditional on one. §4.5 forbids typical_year determining
            # content, and the §9 reorder proof asserts that changing the whole
            # sequence changes zero page bytes. "You'll meet this in Year 9"
            # would break both: it is false for a school that teaches P2 in
            # Year 8, and it would make the page text a function of the
            # sequence. Naming the year is a Phase 5 job for a runtime scheme
            # lookup, where the year is data at render time. Until then the
            # pointer says WHERE, never WHEN — which is true under every
            # possible ordering.
            owner = units_by_code.get(l["reference_to"])
            href = ("/ks3/%s/%s/%s.html" % (owner["discipline"], owner["slug"], l["slug"])
                    if owner else "#")
            owner_disc = DISCIPLINE_TITLES[owner["discipline"]] if owner else ""
            rows.append(
                ('<li class="ks3-lesson-row is-ref"><span class="ks3-num">%d</span>'
                 '<a href="%s">%s</a>' + REF_BADGE + REF_POINTER + '</li>')
                % (i, e(href), e(l["title"]), e(owner_disc), e(l["reference_to"]),
                   e(owner_disc), e(owner["title"]) if owner else ""))
            continue
        href = "/ks3/%s/%s/%s.html" % (disc, unit["slug"], l["slug"])
        badge = ("" if l["authored"]
                 else '<span class="ks3-badge is-soon">Coming soon</span>')
        rows.append('<li class="ks3-lesson-row"><span class="ks3-num">%d</span>'
                    '<a href="%s">%s</a>'
                    '<span class="ks3-family">%s</span>%s</li>'
                    % (i, e(href), e(l["title"]), e(l["family"]), badge))

    # ⛔ The "Why this is its own unit:" note was REMOVED here 2026-08-07 —
    # MRB-181, architecture.md §8.10. Its text ("Eight statutory bullets
    # spanning representation, reaction types and acid chemistry; universally
    # taught as separate units and too large to schedule as one") is a
    # curriculum-design argument addressed to a curriculum designer, printed
    # at the top of a unit page a Year 8 student opens to find lessons.
    # `split_rationale` stays in structure.py: §4.3 requires the record, and
    # keeping it is what lets the decision be reviewed. It just stops being
    # rendered.
    note = ""
    intro = ('<p class="ks3-intro">%s</p>' % e(unit["intro"])) if unit.get("intro") else ""

    body = """<header class="ks3-unit-head">
  <p class="ks3-eyebrow">%s · %s</p>
  <h1>%s</h1>
  %s
  <p class="ks3-meta">%d of %d lessons written · statutory area: %s</p>
  %s
</header>
<ol class="ks3-lesson-list">%s</ol>""" % (
        e(DISCIPLINE_TITLES[disc]), e(unit["code"]), e(unit["title"]), intro,
        unit["authored_count"], len(unit["lessons"]), e(unit["statutory_area"]),
        note, "".join(rows))
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
            % (e(disc), e(u["slug"]), e(u["code"]), e(u["title"]), done, total))
    body = """<header class="ks3-hub-head">
  <h1>KS3 %s</h1>
  <p class="ks3-intro">%d units across Years 7 to 9.</p>
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
    185 lesson slots and 184 distinct slugs: `energy-in-food` is declared twice
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


def browse_lesson_row(unit, lesson, position, units_by_code):
    """One lesson row on a browse page — the same shape as a unit index row.

    Links to the lesson's EXISTING page. The browse layer never mints a lesson
    URL; if it did, §4.5.2's whole justification would collapse.
    """
    if lesson.get("reference_to"):
        # §4.6 single-source: link to the OWNER's page, with the same pointer
        # the unit index uses. WHERE, never WHEN — see REF_POINTER.
        owner = units_by_code.get(lesson["reference_to"])
        href = ("/ks3/%s/%s/%s.html"
                % (owner["discipline"], owner["slug"], lesson["slug"])
                if owner else "#")
        owner_disc = DISCIPLINE_TITLES[owner["discipline"]] if owner else ""
        return (('<li class="ks3-lesson-row is-ref"><span class="ks3-num">%d</span>'
                 '<a href="%s">%s</a>' + REF_BADGE + REF_POINTER + '</li>')
                % (position, e(href), e(lesson["title"]), e(owner_disc),
                   e(lesson["reference_to"]), e(owner_disc),
                   e(owner["title"]) if owner else ""))

    href = "/ks3/%s/%s/%s.html" % (unit["discipline"], unit["slug"], lesson["slug"])
    if not lesson["authored"]:
        # Structure-first (§11 decision 8) — the slot is routable and honest.
        badge = '<span class="ks3-badge is-soon">Coming soon</span>'
    elif lesson.get("review_state") != "frozen":
        # §5.10.1 carve-out: a draft may publish, but only with a visible
        # marker. The lesson page carries `Draft — not yet science-reviewed.`;
        # this is the same fact, at list size, saying the same thing.
        badge = ('<span class="ks3-badge is-draft" title="Draft — not yet '
                 'science-reviewed.">Draft</span>')
    else:
        badge = ""
    return ('<li class="ks3-lesson-row"><span class="ks3-num">%d</span>'
            '<a href="%s">%s</a>'
            '<span class="ks3-family">%s</span>%s</li>'
            % (position, e(href), e(lesson["title"]), e(lesson["family"]), badge))


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
        cards.append(
            '<li class="ks3-unit-card ks3-browse-ht" data-season="%s">'
            '<a href="/ks3/year-%d/%s/index.html">'
            '<span class="ks3-code">Half term %d</span><h2>%s</h2>'
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
<ul class="ks3-unit-grid ks3-browse-terms">%s</ul>
<p class="ks3-browse-alt"><a href="/ks3/index.html">Browse by subject instead →</a></p>""" % (
        year, e(_plural(lessons, "lesson")), e(_plural(units, "unit")),
        "".join(cards))
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
        cards.append(
            '<li class="ks3-unit-card ks3-browse-subject" data-discipline="%s">'
            '<a href="/ks3/year-%d/%s/%s/index.html">'
            '<span class="ks3-browse-dot" aria-hidden="true"></span>'
            '<h2>%s</h2><p class="ks3-meta">%s · %s</p>'
            '<p class="ks3-browse-split">%s</p></a></li>'
            % (e(disc), year, e(slug), e(disc), e(DISCIPLINE_TITLES[disc]),
               e(_plural(lessons, "lesson")), e(_plural(units, "unit")),
               e(" · ".join(unit_titles))))

    units, lessons = _counts(_entries(browse, year, half_term))
    body = """<header class="ks3-landing-head" data-season="%s">
  <p class="ks3-eyebrow">Year %d · Half term %d</p>
  <h1>%s</h1>
  <p class="ks3-intro">%s across %s. Pick a science to see the lessons.</p>
</header>
<ul class="ks3-unit-grid ks3-browse-subjects">%s</ul>
<p class="ks3-browse-alt"><a href="/ks3/year-%d/index.html">← All six half terms of Year %d</a></p>""" % (
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
        items = "".join(browse_lesson_row(u, l, i, units_by_code)
                        for l, i in lessons)
        span = ("lesson %d" % lessons[0][1] if len(lessons) == 1
                else "lessons %d to %d" % (lessons[0][1], lessons[-1][1]))
        sections.append(
            '<section class="ks3-browse-unit">'
            '<p class="ks3-eyebrow">%s · %s of %d</p>'
            '<h2><a href="/ks3/%s/%s/index.html">%s</a></h2>'
            '<ol class="ks3-lesson-list">%s</ol></section>'
            % (e(u["code"]), e(span), len(u["lessons"]),
               e(disc), e(u["slug"]), e(u["title"]), items))

    units, lessons = _counts(rows)
    body = """<header class="ks3-landing-head">
  <p class="ks3-eyebrow">Year %d · %s</p>
  <h1>%s</h1>
  <p class="ks3-intro">%s from %s.</p>
</header>
%s
<p class="ks3-browse-alt"><a href="/ks3/year-%d/%s/index.html">← All three sciences this half term</a>
   · <a href="/ks3/%s/index.html">The whole KS3 %s course →</a></p>""" % (
        year, e(name), e(DISCIPLINE_TITLES[disc]),
        e(_plural(lessons, "lesson")), e(_plural(units, "unit")),
        "".join(sections), year, e(slug),
        e(disc), e(DISCIPLINE_TITLES[disc]))
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
            '<span class="ks3-browse-cta">Browse by half term →</span>'
            '</a></li>'
            % (year, year, e(_plural(units_n, "unit")),
               e(_plural(lessons_n, "lesson")),
               "".join('<span data-season="%s"></span>' % e(season_of(ht))
                       for ht in HALF_TERMS)))

    secs = []
    for disc in ("biology", "chemistry", "physics"):
        du = [u for u in units if u["discipline"] == disc]
        done = sum(u["authored_count"] for u in du)
        total = sum(len(u["lessons"]) for u in du)
        secs.append(
            '<li class="ks3-disc-card"><a href="/ks3/%s/index.html">'
            '<h2>%s</h2><p class="ks3-meta">%d units · %d of %d lessons written</p>'
            '</a></li>' % (e(disc), e(DISCIPLINE_TITLES[disc]), len(du), done, total))

    total_lessons = sum(len(u["lessons"]) for u in units)
    total_done = sum(u["authored_count"] for u in units)
    body = """<header class="ks3-landing-head">
  <h1>Key Stage 3 Science</h1>
  <p class="ks3-intro">Years 7 to 9. Biology, Chemistry and Physics — the whole
     national curriculum programme of study, built lesson by lesson.</p>
  <p class="ks3-meta">%d of %d lessons written so far.</p>
</header>
<ul class="ks3-unit-grid ks3-browse-years">%s</ul>
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

    # 3. Every authored lesson has non-empty `covers` (§10.2).
    for slug, l in sorted(registry.items()):
        if l.get("authored") and not l.get("covers"):
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
