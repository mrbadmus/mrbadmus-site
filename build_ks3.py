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

Output taxonomy (§8.4) — no year appears in any path, ever (§4.5):

    /ks3/index.html                                     KS3 landing
    /ks3/<discipline>/index.html                        discipline hub
    /ks3/<discipline>/<unit-slug>/index.html            unit index
    /ks3/<discipline>/<unit-slug>/<lesson-slug>.html    the lesson
"""

import html
import os
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import ks3_data
from ks3_data.structure import DISCIPLINE_TITLES
from ks3_data.substatements import all_sub_ids, parent_of

OUT_ROOT = "mrbadmus_site"
KS3_DIR = "ks3"

# KS4 pages have a pathway and a tier; KS3 has neither. A KS3 student following
# a `ks4_links` edge has not been placed in a tier and must not be forced to
# pick one, so the bridge lands on Combined Foundation — the least presumptuous
# entry point into GCSE. §4.7.
KS4_BRIDGE_PATHWAY = "combined"
KS4_BRIDGE_TIER = "foundation"

SUBJECT_TOKEN = {
    "biology": "--biology",
    "chemistry": "--chemistry",
    "physics": "--physics",
}

FAMILY_BLURB = {
    "MODEL": "One idea explains a whole class of behaviour",
    "PROCESS": "A mechanism unfolds in steps",
    "SYSTEM": "Parts working together, and what happens when one fails",
    "CONTRAST": "Two things, one discriminating difference",
    "CLASSIFY": "Decide which category, fast, and know why",
    "QUANTITATIVE": "A calculation carries the concept",
    "INVESTIGATION": "The science skill is the subject",
}


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
  <p>This lesson is planned and its place in the course is fixed, but it has not
     been written yet.</p>
  <p class="ks3-family-note">%s</p>
  <p><a href="%s/index.html">Back to %s</a></p>
</section>""" % (e(unit["title"]), e(lesson["family"]), e(lesson["title"]),
                 e(FAMILY_BLURB.get(lesson["family"], "")), e(base), e(unit["title"]))
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
                '<li class="ks3-lesson-row is-ref"><span class="ks3-num">%d</span>'
                '<a href="%s">%s</a>'
                '<span class="ks3-badge">from %s %s</span>'
                '<p class="ks3-ref-note">Taught in %s — <em>%s</em>. '
                'You\'ll meet the full lesson there.</p></li>'
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

    note = ""
    if unit["split_rationale"]:
        note = ('<p class="ks3-note"><strong>Why this is its own unit:</strong> %s</p>'
                % e(unit["split_rationale"]))
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


def landing(units):
    crumb = crumbs([("KS3", None)])
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
<ul class="ks3-disc-grid">%s</ul>""" % (total_done, total_lessons, "".join(secs))
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

    def write(relpath, content):
        full = os.path.join(ks3_out, relpath)
        os.makedirs(os.path.dirname(full), exist_ok=True)
        with open(full, "w", encoding="utf-8") as f:
            f.write(content)

    n = 0
    write("index.html", landing(units))
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
    print("  ✅ wrote %d pages → %s/" % (n, ks3_out))

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
