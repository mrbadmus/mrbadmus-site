"""ks3_parity.py — the MRB-183 parity gate.

Claude Design's reference set is frozen in ``docs/ks3/design-reference/``.
This module is what turns "the generator reproduces Design's screens" from a
hope into a build gate.

═══════════════════════════════════════════════════════════════════════════
WHAT THIS GATE DOES, AND WHAT IT CANNOT DO — read before trusting it
═══════════════════════════════════════════════════════════════════════════

Design's artifacts are React prototypes: ``x-dc`` templating, 507 inline
``style`` attributes, **zero CSS classes**, and one hardcoded lesson whose
prose is written literally into the markup. There is no machine-readable link
between "this div in the prototype" and "this class in the generated page" —
so a byte diff is impossible and even a DOM diff would need a hand-written
node-to-selector mapping.

So parity is asserted in four layers, each catching something the others
cannot:

  A. PROVENANCE (no browser).  Every colour the KS3 token block declares must
     appear literally in at least one frozen artifact. This is the layer that
     makes the expectation table in C self-policing: you cannot invent a
     colour Design never specified, or drift a hex by one digit, without the
     build failing. It is cheap and it is the strongest anti-drift property
     available here.

  B. STRUCTURE (no browser).  The rules that are structural rather than
     visual — R3, R12, R13, R14, R15 and the drawn-mark rule — asserted
     against the built tree.

  C. COMPUTED STYLE (browser).  For each component, load a REAL generated
     page in headless Chrome and compare the RESOLVED style against Design's
     values: colour, background, border, radius, font family/size/weight,
     padding, shadow. Colours must match exactly; lengths within 1px; a font
     family must contain the expected family name.

     A component may declare a `drive` — a named interaction the gate performs
     before measuring, so that states which only exist after a click are
     measured in the state rather than assumed from the stylesheet. Each drive
     gets its own fresh page load. See DRIVES.

  D. CONTRAST (browser).  Every text/ground pair re-measured against the real
     rendered grounds, not against Design's table. Body text 4.5:1,
     state-bearing and identifying marks 3:1. Pairs may also be driven, so an
     answered option's ground is measured as the student sees it.

WHAT IT DOES NOT CATCH, stated plainly rather than papered over:

  * **Layout and composition.** It checks that a block is the right colour,
    size and shape; it does not check that the blocks are in Design's order,
    or that the page as a whole looks like the reference. Screenshots and
    Mide's eye cover that.
  * **The hook's bespoke illustration.** Design hand-built a marshmallow in a
    vacuum jar from 12 positioned drifting spans and a scaling marshmallow,
    for one lesson. It is artwork, not a generator component, and cannot be
    produced from lesson data. Not reproduced, not asserted, reported instead.
  * **The ladder's behaviour.** Design's ladder artifact still implements the
    OLD 2-of-2 scoring; MRB-184 was ruled the day after it was exported and
    the ruling says explicitly that it changes the artifact's behaviour, not
    its look. So the ladder is gated on its LOOK against the artifact and on
    its BEHAVIOUR against SPEC.md §5 — never on the artifact's behaviour,
    which is superseded.
  * **Anything at a viewport Design did not draw.** The reference set is
    desktop-first; the 390px rules are translation decisions, not
    transcriptions, and are checked by screenshot rather than by table.
  * **A state nobody registered.** This is what MRB-202 cost: an answer button
    had only its RESTING state registered, so the four states a student
    actually ends up looking at were compared against nothing and the gate
    reported green over them. Layers C and D can only ever be as complete as
    COMPONENTS and CONTRAST are. Adding a state to the stylesheet without
    adding it here re-opens exactly that hole, so a new state is not finished
    until it appears in both lists AND its token has been mutation-tested.

Provenance for every number in ``COMPONENTS`` below is
``docs/ks3/design-reference/SPEC.md``, which cites the artifact it came from.
"""

import os
import re

REF_DIR = os.path.join("docs", "ks3", "design-reference")
ARTIFACTS = (
    "KS3 Reference Set (offline).html",
    "KS3 Parts Library (offline).html",
    "KS3 Mastery Ladder (offline).html",
    "KS3 Simulation (offline).html",
)


# ── A. provenance ────────────────────────────────────────────────────────

def _artifact_text(repo_root="."):
    blob = []
    for name in ARTIFACTS:
        p = os.path.join(repo_root, REF_DIR, name)
        if os.path.exists(p):
            with open(p, encoding="utf-8", errors="replace") as fh:
                blob.append(fh.read())
    return "\n".join(blob).lower()


def ks3_token_colours(repo_root="."):
    """Every hex colour declared inside the `.rd[data-mode="ks3"]` block."""
    path = os.path.join(repo_root, "shared", "tokens.css")
    with open(path, encoding="utf-8") as fh:
        css = fh.read()
    start = css.find('.rd[data-mode="ks3"]')
    if start < 0:
        return {}
    # The block ends at the first line that is exactly "}" at column 0.
    end = css.find("\n}", start)
    block = css[start:end if end > 0 else len(css)]
    out = {}
    for m in re.finditer(r'(--ks3-[a-z0-9-]+)\s*:\s*(#[0-9A-Fa-f]{6})', block):
        out[m.group(1)] = m.group(2)
    return out


def check_provenance(repo_root="."):
    """Layer A. Returns (problems, checked_count).

    A colour that is not in any artifact is either invented or drifted. Both
    are exactly the failure this gate exists to prevent, so both fail.
    """
    blob = _artifact_text(repo_root)
    if not blob:
        return (["frozen reference artifacts missing from %s" % REF_DIR], 0)
    problems = []
    tokens = ks3_token_colours(repo_root)
    for name, hexval in sorted(tokens.items()):
        if hexval.lower() not in blob:
            problems.append(
                "%s = %s does not appear anywhere in Claude Design's frozen "
                "reference — invented or drifted" % (name, hexval))
    return (problems, len(tokens))


# ── B. structural rules ──────────────────────────────────────────────────

# R14: the strings MRB-181 removed. Their return is a regression, and a
# stub-to-empty-string does not count as removal — the plumbing has to go.
BANNED_COPY = (
    "ks3-browse-note",
    "This is the MrBadmusAI default sequence",
    "Why this is its own unit",
    "and its place in the course is fixed",
    "All three sciences run together through every half term",
    "One idea explains a whole class of behaviour",
)

# The three marks whose glyphs are absent from Design's own woff2 subsets.
UNDRAWABLE = {"→": "→ U+2192", "✓": "✓ U+2713", "✕": "✕ U+2715"}

# R13: a lesson page may not name a year or a half term, in path or in bytes.
YEAR_WORDS = re.compile(
    r"\bYear [789]\b|\bAutumn (?:First|Second) Half\b"
    r"|\bSpring (?:First|Second) Half\b|\bSummer (?:First|Second) Half\b"
    r"|\bhalf term\b", re.I)


def _lesson_pages(ks3_root):
    """Lesson pages only: /ks3/<discipline>/<unit>/<lesson>.html."""
    out = []
    for disc in ("biology", "chemistry", "physics"):
        base = os.path.join(ks3_root, disc)
        if not os.path.isdir(base):
            continue
        for unit in sorted(os.listdir(base)):
            udir = os.path.join(base, unit)
            if not os.path.isdir(udir):
                continue
            for f in sorted(os.listdir(udir)):
                if f.endswith(".html") and f != "index.html":
                    out.append(os.path.join(udir, f))
    return out


def _all_pages(ks3_root):
    out = []
    for dp, _dn, fn in os.walk(ks3_root):
        for f in fn:
            if f.endswith(".html"):
                out.append(os.path.join(dp, f))
    return sorted(out)


def check_structure(ks3_root):
    """Layer B. Returns (problems, notes)."""
    problems = []
    notes = []
    pages = _all_pages(ks3_root)
    if not pages:
        return (["no built KS3 pages found under %s" % ks3_root], notes)

    lessons = _lesson_pages(ks3_root)
    notes.append("%d pages scanned, %d of them lesson pages"
                 % (len(pages), len(lessons)))

    for p in pages:
        with open(p, encoding="utf-8") as fh:
            html = fh.read()
        rel = os.path.relpath(p, ks3_root)

        # R14 — the page never explains itself.
        for phrase in BANNED_COPY:
            if phrase.lower() in html.lower():
                problems.append("R14: %s carries removed meta-text %r"
                                % (rel, phrase))

        # Drawn marks — a literal glyph falls back to a system font because
        # Design's own subsets do not contain it.
        #
        # Scanned over TEXT NODES ONLY, with every tag (and therefore every
        # attribute) stripped first. The distinction is real, not a loophole:
        # a glyph sitting in the page's text is painted by the webfont and is
        # a defect, whereas one sitting in a `data-feedback` attribute is
        # authored science copy that ks3.js converts to an inline SVG when it
        # injects it. Three of the C1 ladder corrections contain "liquid → gas"
        # and the content must not be edited to satisfy a font subset. The
        # rendered result is asserted separately, in the browser, where it can
        # be checked AFTER the feedback is actually on screen.
        text_only = re.sub(r"<[^>]+>", " ", html)
        for ch, label in UNDRAWABLE.items():
            if ch in text_only:
                problems.append(
                    "%s renders the literal character %s as text; it must be "
                    "inline SVG (.ks3-mark) because the webfont subset lacks "
                    "the glyph" % (rel, label))

        # R15 — no clickable divs, no inline handlers.
        if re.search(r'<div[^>]*\son(?:click|keydown)\s*=', html, re.I):
            problems.append("R15: %s has a clickable <div>" % rel)

        # R3 — only the ladder marks correctness.
        for m in re.finditer(r'data-correct=', html):
            seg = html[:m.start()]
            if seg.rfind('class="ks3-block ks3-ladder"') <= seg.rfind("</section>"):
                problems.append("R3: %s has data-correct outside the ladder" % rel)
                break

    for p in lessons:
        with open(p, encoding="utf-8") as fh:
            html = fh.read()
        rel = os.path.relpath(p, ks3_root)

        # R13 — where, never when.
        hit = YEAR_WORDS.search(html)
        if hit:
            problems.append("R13: lesson page %s names a year or term (%r)"
                            % (rel, hit.group(0)))

        # R12 — an empty layer leaves no gap.
        for cls, head in (("ks3-support", "Need a hand?"),
                          ("ks3-stretch", "Going further")):
            for m in re.finditer(r'<section class="ks3-layer %s">(.*?)</section>'
                                 % cls, html, re.S):
                body = re.search(r'<div class="ks3-layer-body">(.*?)</div>',
                                 m.group(1), re.S)
                if body is not None and not body.group(1).strip():
                    problems.append(
                        "R12: %s renders an EMPTY %s layer — an empty layer "
                        "must render nothing at all" % (rel, head))

    return (problems, notes)


# ── C. computed-style expectations ───────────────────────────────────────
#
# Every value's provenance is SPEC.md, which cites the artifact. `on` is the
# page to load it from; `sel` is the first matching element.
#
# `props` keys are CSS property names as the browser resolves them. Colours
# are compared exactly after normalising to rgb(); lengths within TOL_PX;
# `font-family` must CONTAIN the given string.

TOL_PX = 1.0

LESSON = "chemistry/particles-and-their-behaviour/gas-pressure.html"
UNIT = "chemistry/particles-and-their-behaviour/index.html"
# C1 is fully authored, so its index carries no Coming soon badge; and B3 is
# the ONLY unit in the key stage with a §4.6 reference slot, so it is the only
# page where the pointer can be measured at all.
UNIT_SOON = "biology/cells-and-organisation/index.html"
UNIT_REF = "biology/nutrition-and-digestion/index.html"
LANDING = "index.html"
YEAR = "year-7/index.html"

COMPONENTS = [
    # ── foundations ──
    dict(name="page ground + body type", on=LESSON, sel="body",
         props={"background-color": "#FBF3E6", "color": "#221E1B",
                "font-family": "Instrument Sans", "font-size": "19px"}),
    dict(name="lesson title (type row 1)", on=LESSON, sel=".ks3-lesson-head h1",
         props={"font-family": "Bricolage Grotesque", "font-weight": "800"}),
    dict(name="big question (type row 2)", on=LESSON, sel=".ks3-bigq",
         props={"color": "#A93411", "font-size": "25px", "font-weight": "600"}),
    dict(name="body prose (type row 4)", on=LESSON, sel=".ks3-explainer p",
         props={"font-size": "20px", "line-height": "35px"}),
    dict(name="eyebrow (type row 6)", on=LESSON, sel=".ks3-eyebrow",
         props={"font-size": "13px", "font-weight": "700",
                "text-transform": "uppercase", "color": "#5F564F"}),
    dict(name="breadcrumb is mono", on=LESSON, sel=".ks3-crumbs",
         props={"font-family": "DM Mono", "font-size": "14px"}),
    # MRB-197: Design's nav mark. Pinned to the frozen reference's header —
    # if the wordmark shrinks below display size, the chevron's 3:1 pair
    # below stops being the whole story and this fails first.
    dict(name="nav brand wordmark (MRB-197)", on=LESSON, sel=".ks3-brand",
         props={"font-family": "Bricolage Grotesque", "font-weight": "800",
                "font-size": "22px", "color": "#221E1B"}),

    # ── blocks ──
    dict(name="standard block shell", on=LESSON, sel=".ks3-check",
         props={"background-color": "#FFFCF5", "border-top-color": "#221E1B",
                "border-top-width": "2px", "border-top-left-radius": "28px",
                "padding-top": "30px"}),
    dict(name="hook is ink-dark, accent shadow", on=LESSON, sel=".ks3-hook",
         props={"background-color": "#221E1B", "color": "#FBF3E6",
                "border-top-left-radius": "30px"}),
    dict(name="misconception is amber", on=LESSON, sel=".ks3-misconception",
         props={"background-color": "#FFF3D4", "border-top-color": "#221E1B"}),
    dict(name="key note is ink-dark", on=LESSON, sel=".ks3-keynote",
         props={"background-color": "#221E1B"}),
    dict(name="key note type drops to 700", on=LESSON, sel=".ks3-keynote p",
         props={"font-family": "Bricolage Grotesque", "font-weight": "700",
                "font-size": "30px"}),

    # ══ OPTION BUTTONS — every state of both surfaces (MRB-202) ══════════
    #
    # This block is the one whose absence let a P0 live in production for a
    # whole release. Layer C compares REGISTERED components; a state nobody
    # registered has nothing to disagree with, so the gate printed green over
    # it. Registering only the resting state of an answer button is registering
    # the one state a student never makes a decision in.
    #
    # States that exist only after a click are DRIVEN into being (see DRIVES
    # below) rather than assumed. Provenance is SPEC.md §4 for the activity
    # buttons and SPEC.md §5's four-row option-state table for the ladder.

    # ── activity options. SPEC.md §4: "Resting `--ks3-ground` on
    # `--ks3-option-border`. Chosen: `--ks3-accent-tint` ground, `2px solid
    # --ks3-accent`. R3: never green, never red, never disabled." ──
    dict(name="activity option resting", on=LESSON,
         sel=".ks3-check .ks3-option",
         props={"background-color": "#FBF3E6", "border-top-color": "#DDCFB6",
                "font-size": "18px", "font-weight": "600",
                "border-top-left-radius": "16px", "min-height": "44px"}),
    dict(name="activity option resting badge", on=LESSON,
         sel=".ks3-check .ks3-option .ks3-opt-mark",
         props={"background-color": "#F4E9D8", "color": "#5F564F",
                "border-top-left-radius": "9px"}),
    dict(name="activity option CHOSEN", on=LESSON, drive="activity-chosen",
         sel='.ks3-check .ks3-option[aria-pressed="true"]',
         props={"background-color": "#FCE7DE", "border-top-color": "#E4572E",
                "border-top-width": "2px"}),
    dict(name="activity option CHOSEN badge", on=LESSON, drive="activity-chosen",
         sel='.ks3-check .ks3-option[aria-pressed="true"] .ks3-opt-mark',
         props={"background-color": "#E4572E", "color": "#FBF3E6"}),

    # ── activity options on an INK-DARK block (hook, practical). ──
    #
    # ⚠️ PROVENANCE IS WEAKER HERE, AND SAYING SO IS THE POINT. SPEC.md §4
    # row 1 draws the hook's "full-width option buttons with letter badges"
    # and its reveal "on `--ks3-dark-panel` with a `2px` alert border", which
    # is where the dark block's alert accent comes from — orange on ink is
    # illegible, so the dark surface swaps accent for alert. But Design never
    # drew the CHOSEN state of a dark option button. The values below are
    # therefore a TRANSLATION of the reveal's treatment, in the same category
    # SPEC.md puts the 390px rules in, not a transcription of a drawn screen.
    #
    # They are registered anyway. An unregistered state is what MRB-202 cost,
    # and pinning today's rendering at least means it cannot drift in silence
    # while Design's screen is outstanding. When that screen arrives these
    # rows get re-pointed at it, and the comment goes.
    dict(name="dark-block option resting (translated)", on=LESSON,
         sel=".ks3-dark .ks3-option",
         props={"background-color": "#3E3730", "border-top-color": "#C6B9A7",
                "color": "#FBF3E6"}),
    dict(name="dark-block option resting badge (translated)", on=LESSON,
         sel=".ks3-dark .ks3-option .ks3-opt-mark",
         props={"background-color": "#C6B9A7", "color": "#221E1B"}),
    dict(name="dark-block option CHOSEN (translated)", on=LESSON,
         drive="dark-option-chosen",
         sel='.ks3-dark .ks3-option[aria-pressed="true"]',
         props={"background-color": "#3E3730", "border-top-color": "#FFC53D"}),
    dict(name="dark-block option CHOSEN badge (translated)", on=LESSON,
         drive="dark-option-chosen",
         sel='.ks3-dark .ks3-option[aria-pressed="true"] .ks3-opt-mark',
         props={"background-color": "#FFC53D", "color": "#221E1B"}),

    # ── ladder options. SPEC.md §5's table, all four rows. This is the only
    # surface in the key stage allowed to say right or wrong (R3), so it is
    # the surface where getting the colour wrong does the most damage. ──
    dict(name="ladder option resting", on=LESSON,
         sel='.ks3-rung[data-mode="marked"] .ks3-option',
         props={"background-color": "#FBF3E6", "border-top-color": "#DDCFB6",
                "border-top-left-radius": "15px", "font-size": "18px",
                "font-weight": "600", "min-height": "44px"}),
    dict(name="ladder option resting badge", on=LESSON,
         sel='.ks3-rung[data-mode="marked"] .ks3-option .ks3-opt-mark',
         props={"background-color": "#F4E9D8", "color": "#5F564F"}),

    dict(name="ladder option CHOSEN-CORRECT", on=LESSON, drive="ladder-answered",
         sel='.ks3-rung[data-mode="marked"] .ks3-option.is-correct',
         props={"background-color": "#E4F7EB", "border-top-color": "#12A150"}),
    dict(name="ladder option CHOSEN-CORRECT badge", on=LESSON,
         drive="ladder-answered",
         sel='.ks3-rung[data-mode="marked"] .ks3-option.is-correct .ks3-opt-mark',
         props={"background-color": "#12A150", "color": "#FFFFFF"}),

    dict(name="ladder option CHOSEN-WRONG", on=LESSON, drive="ladder-answered",
         sel='.ks3-rung[data-mode="marked"] .ks3-option.is-wrong',
         props={"background-color": "#F4E9D8", "border-top-color": "#221E1B"}),
    dict(name="ladder option CHOSEN-WRONG badge", on=LESSON,
         drive="ladder-answered",
         sel='.ks3-rung[data-mode="marked"] .ks3-option.is-wrong .ks3-opt-mark',
         props={"background-color": "#221E1B", "color": "#FBF3E6"}),

    dict(name="ladder option SPENT", on=LESSON, drive="ladder-answered",
         sel='.ks3-rung[data-mode="marked"] .ks3-option.is-spent',
         props={"background-color": "#FBF6EC", "border-top-color": "#EBDFCB",
                "color": "#6E655D"}),
    dict(name="ladder option SPENT badge", on=LESSON, drive="ladder-answered",
         sel='.ks3-rung[data-mode="marked"] .ks3-option.is-spent .ks3-opt-mark',
         props={"background-color": "#F4E9D8", "color": "#9A8F86"}),

    # The feedback line carries the same verdict in words, so it is registered
    # with the states rather than apart from them — a green option above a
    # band-coloured "Not quite." would be a contradiction the gate should see.
    dict(name="ladder feedback CORRECT", on=LESSON, drive="ladder-answered",
         sel=".ks3-feedback.is-correct",
         props={"background-color": "#E4F7EB", "border-top-color": "#12A150",
                "border-top-left-radius": "15px", "font-size": "19px"}),
    dict(name="ladder feedback WRONG", on=LESSON, drive="ladder-answered",
         sel=".ks3-feedback.is-wrong",
         props={"background-color": "#F4E9D8", "border-top-color": "#221E1B"}),

    # ── R4: the dog-ear card ──
    dict(name="vocabulary card", on=LESSON, sel=".ks3-card-btn",
         props={"background-color": "#FFFCF5", "border-top-left-radius": "22px",
                "min-height": "150px"}),
    dict(name="card term type", on=LESSON, sel=".ks3-card-front",
         props={"font-family": "Bricolage Grotesque", "font-weight": "800",
                "font-size": "27px"}),

    # ── the ladder (LOOK only — behaviour is SPEC 5, see docstring) ──
    dict(name="ladder shell", on=LESSON, sel=".ks3-ladder",
         props={"background-color": "#FFFCF5", "border-top-width": "3px",
                "border-top-color": "#221E1B",
                "border-top-left-radius": "30px", "padding-top": "32px"}),
    dict(name="ladder heading", on=LESSON, sel=".ks3-ladder-head h2",
         props={"font-family": "Bricolage Grotesque", "font-size": "36px",
                "font-weight": "800"}),
    dict(name="page-marked rung is accent", on=LESSON,
         sel='.ks3-rung[data-mode="marked"]',
         props={"border-left-color": "#E4572E", "border-left-width": "4px"}),
    dict(name="page-marked rung heading", on=LESSON,
         sel='.ks3-rung[data-mode="marked"] h3',
         props={"color": "#A93411", "font-size": "23px"}),
    dict(name="self-marked rung is violet", on=LESSON,
         sel='.ks3-rung[data-mode="self"]',
         props={"border-left-color": "#6B3FD4", "border-left-width": "4px"}),
    dict(name="self-marked rung heading", on=LESSON,
         sel='.ks3-rung[data-mode="self"] h3',
         props={"color": "#5A31C0"}),
    dict(name="R8 answer box", on=LESSON, sel=".ks3-answer",
         props={"background-color": "#FFFCF5", "border-top-color": "#DDCFB6",
                "font-size": "19px"}),
    dict(name="R8 check-my-answer button", on=LESSON, sel=".ks3-check-btn",
         props={"background-color": "#F4E9D8", "border-top-color": "#221E1B",
                "min-height": "44px", "font-weight": "700"}),

    # ── simulations ──
    dict(name="sim canvas", on=LESSON, sel=".ks3-sim-canvas",
         props={"background-color": "#F7EFE1", "border-top-color": "#221E1B",
                "border-top-left-radius": "20px"}),
    dict(name="sim live figure is mono", on=LESSON, sel=".ks3-sim-figure",
         props={"font-family": "DM Mono", "font-weight": "500"}),

    # ── layers ──
    dict(name="stretch layer is violet", on=LESSON, sel=".ks3-stretch .ks3-layer-body",
         props={"background-color": "#F0EAFC", "border-top-color": "#6B3FD4"}),

    # ── end matter ──
    dict(name="tutor card is accent", on=LESSON, sel=".ks3-tutor",
         props={"background-color": "#E4572E"}),
    # These two are what license need=3.0 on the contrast pair above. If the
    # size or weight drops, this assertion fails and the classification cannot
    # quietly stop being true.
    dict(name="tutor text is large-bold (licenses its 3:1)", on=LESSON,
         sel=".ks3-endmatter .ks3-tutor p",
         props={"font-size": "19px", "font-weight": "700"}),

    # ── browse layer ──
    dict(name="draft badge", on=UNIT, sel=".ks3-badge.is-draft",
         props={"background-color": "#FCE7DE", "border-top-color": "#E4572E",
                "color": "#A93411"}),
    dict(name="lesson row number tile", on=UNIT, sel=".ks3-num",
         props={"background-color": "#F4E9D8",
                "font-family": "Bricolage Grotesque"}),
    dict(name="year card", on=LANDING, sel=".ks3-browse-year > a",
         props={"background-color": "#FFFCF5", "border-top-color": "#221E1B",
                "border-top-width": "2px"}),
    dict(name="half-term card, autumn season", on=YEAR,
         sel='.ks3-browse-ht[data-season="autumn"] .ks3-code',
         props={"background-color": "#E4572E"}),
    dict(name="half-term card, spring season", on=YEAR,
         sel='.ks3-browse-ht[data-season="spring"] .ks3-code',
         props={"background-color": "#12A150"}),
    dict(name="half-term card, summer season", on=YEAR,
         sel='.ks3-browse-ht[data-season="summer"] .ks3-code',
         props={"background-color": "#2F5CE0"}),
]


# ── D. contrast pairs — re-measured, never trusted from a table ──────────
#
# `fg`/`bg` are selectors; the gate reads the RESOLVED colour off each and
# computes the ratio itself. `need` is 4.5 for body-size text and 3.0 for a
# state-bearing or identifying mark (R1).

CONTRAST = [
    dict(name="body text on page ground", on=LESSON,
         fg=".ks3-explainer p", bg="body", need=4.5),
    dict(name="muted text on page ground", on=LESSON,
         fg=".ks3-eyebrow", bg="body", need=4.5),
    dict(name="big question on page ground", on=LESSON,
         fg=".ks3-bigq", bg="body", need=4.5),
    dict(name="breadcrumb link on page ground", on=LESSON,
         fg=".ks3-crumbs a", bg="body", need=4.5),
    dict(name="nav brand wordmark on page ground", on=LESSON,
         fg=".ks3-brand", bg=".ks3-nav", need=4.5),
    # MRB-197: the chevron is an identifying mark, so R1's 3:1 applies. Read
    # from the SVG stroke, not `color` — the mark is drawn, not typed.
    dict(name="nav brand chevron on page ground (mark, 3:1)", on=LESSON,
         fg=".ks3-brand svg path", bg=".ks3-nav", need=3.0, prop="stroke"),
    dict(name="body text on card", on=LESSON,
         fg=".ks3-check p", bg=".ks3-check", need=4.5),
    dict(name="draft marker text on its tint", on=LESSON,
         fg=".ks3-review-flag", bg=".ks3-review-flag", need=4.5),
    dict(name="misconception quote on amber tint", on=LESSON,
         fg=".ks3-mis-quote", bg=".ks3-misconception", need=4.5),
    dict(name="hook body on ink-dark", on=LESSON,
         fg=".ks3-hook-prompt", bg=".ks3-hook", need=4.5),
    dict(name="hook commit line on ink-dark", on=LESSON,
         fg=".ks3-commit", bg=".ks3-hook", need=4.5),
    dict(name="key note on ink-dark", on=LESSON,
         fg=".ks3-keynote p", bg=".ks3-keynote", need=4.5),
    dict(name="option label on option ground", on=LESSON,
         fg=".ks3-check .ks3-option", bg=".ks3-check .ks3-option", need=4.5),

    # ── option states, measured in the state (MRB-202) ──
    # A ground the student only ever sees after committing is still a ground
    # text has to be legible on. These are driven, then measured.
    dict(name="activity CHOSEN label on its tint", on=LESSON,
         drive="activity-chosen",
         fg='.ks3-check .ks3-option[aria-pressed="true"] .ks3-opt-label',
         bg='.ks3-check .ks3-option[aria-pressed="true"]', need=4.5),
    dict(name="MARK activity CHOSEN badge letter on accent", on=LESSON,
         drive="activity-chosen",
         fg='.ks3-check .ks3-option[aria-pressed="true"] .ks3-opt-mark',
         bg='.ks3-check .ks3-option[aria-pressed="true"] .ks3-opt-mark',
         need=3.0),
    dict(name="dark-block option label on dark panel", on=LESSON,
         fg=".ks3-dark .ks3-option .ks3-opt-label",
         bg=".ks3-dark .ks3-option", need=4.5),
    dict(name="MARK dark-block badge letter on its fill", on=LESSON,
         fg=".ks3-dark .ks3-option .ks3-opt-mark",
         bg=".ks3-dark .ks3-option .ks3-opt-mark", need=3.0),
    dict(name="MARK dark-block CHOSEN badge letter on alert", on=LESSON,
         drive="dark-option-chosen",
         fg='.ks3-dark .ks3-option[aria-pressed="true"] .ks3-opt-mark',
         bg='.ks3-dark .ks3-option[aria-pressed="true"] .ks3-opt-mark',
         need=3.0),
    # On the dark surface the CHOSEN state is carried by the border alone —
    # the ground does not change — so that border is the state-bearing mark
    # and has to clear 3:1 against the panel behind it, or the state is
    # invisible to anyone who cannot pick the amber out.
    dict(name="MARK dark-block CHOSEN border on dark panel", on=LESSON,
         drive="dark-option-chosen",
         fg='.ks3-dark .ks3-option[aria-pressed="true"]',
         bg=".ks3-practical", need=3.0, prop="border-top-color"),
    dict(name="ladder CORRECT label on ok tint", on=LESSON,
         drive="ladder-answered",
         fg='.ks3-rung[data-mode="marked"] .ks3-option.is-correct .ks3-opt-label',
         bg='.ks3-rung[data-mode="marked"] .ks3-option.is-correct', need=4.5),
    dict(name="MARK ladder CORRECT tick on ok fill", on=LESSON,
         drive="ladder-answered",
         fg='.ks3-rung[data-mode="marked"] .ks3-option.is-correct .ks3-opt-mark',
         bg='.ks3-rung[data-mode="marked"] .ks3-option.is-correct .ks3-opt-mark',
         need=3.0),
    dict(name="ladder WRONG label on band", on=LESSON,
         drive="ladder-answered",
         fg='.ks3-rung[data-mode="marked"] .ks3-option.is-wrong .ks3-opt-label',
         bg='.ks3-rung[data-mode="marked"] .ks3-option.is-wrong', need=4.5),
    dict(name="MARK ladder WRONG cross on ink", on=LESSON,
         drive="ladder-answered",
         fg='.ks3-rung[data-mode="marked"] .ks3-option.is-wrong .ks3-opt-mark',
         bg='.ks3-rung[data-mode="marked"] .ks3-option.is-wrong .ks3-opt-mark',
         need=3.0),
    # The spent option's LABEL is asserted at the full 4.5 and reaches 5.29:1,
    # so no exemption is claimed for it even though it could be.
    dict(name="ladder SPENT label on dimmed row", on=LESSON,
         drive="ladder-answered",
         fg='.ks3-rung[data-mode="marked"] .ks3-option.is-spent .ks3-opt-label',
         bg='.ks3-rung[data-mode="marked"] .ks3-option.is-spent', need=4.5),
    # Its BADGE GLYPH measures 2.63:1 and does not reach 3:1. That is
    # deliberate — `--ks3-ink-ghost` exists in tokens.css commented "spent
    # option badge glyph", and a spent option is a DISABLED control, which
    # WCAG 1.4.3 exempts from contrast entirely.
    #
    # The exemption is recorded here rather than the pair being dropped,
    # because a dropped pair is an assertion that cannot fail. `exempt_if_
    # disabled` makes the exemption CONDITIONAL on the thing that justifies
    # it: the gate proves the control is really disabled, and if a future
    # change leaves spent options clickable, the exemption stops applying and
    # 2.63:1 becomes a failure naming this row.
    dict(name="MARK ladder SPENT badge glyph on band", on=LESSON,
         drive="ladder-answered",
         fg='.ks3-rung[data-mode="marked"] .ks3-option.is-spent .ks3-opt-mark',
         bg='.ks3-rung[data-mode="marked"] .ks3-option.is-spent .ks3-opt-mark',
         need=3.0,
         exempt_if_disabled='.ks3-rung[data-mode="marked"] .ks3-option.is-spent'),
    dict(name="ladder feedback CORRECT text on ok tint", on=LESSON,
         drive="ladder-answered",
         fg=".ks3-feedback.is-correct", bg=".ks3-feedback.is-correct", need=4.5),
    # The drawn tick inside the feedback line carries the verdict as a mark,
    # so it is measured as one. Note it is the GLYPH that takes --ks3-ok-text
    # here; the word "Correct." beside it inherits ink. tokens.css comments
    # that token as "the word", which is one step out from where it lands.
    dict(name="MARK ladder feedback tick on ok tint", on=LESSON,
         drive="ladder-answered",
         fg=".ks3-feedback.is-correct .ks3-mark",
         bg=".ks3-feedback.is-correct", need=3.0),
    dict(name="ladder feedback WRONG text on band", on=LESSON,
         drive="ladder-answered",
         fg=".ks3-feedback.is-wrong", bg=".ks3-feedback.is-wrong", need=4.5),
    dict(name="MARK ladder feedback cross on band", on=LESSON,
         drive="ladder-answered",
         fg=".ks3-feedback.is-wrong .ks3-mark",
         bg=".ks3-feedback.is-wrong", need=3.0),
    dict(name="card hint on card", on=LESSON,
         fg=".ks3-card-hint", bg=".ks3-card-btn", need=4.5),
    dict(name="card term on card", on=LESSON,
         fg=".ks3-card-front", bg=".ks3-card-btn", need=4.5),
    dict(name="criteria number on its tint", on=LESSON,
         fg=".ks3-crit-num", bg=".ks3-crit-num", need=4.5),
    dict(name="self-rung heading on card", on=LESSON,
         fg='.ks3-rung[data-mode="self"] h3', bg=".ks3-ladder", need=4.5),
    dict(name="marked-rung heading on card", on=LESSON,
         fg='.ks3-rung[data-mode="marked"] h3', bg=".ks3-ladder", need=4.5),
    dict(name="locked sim cover on amber block", on=LESSON,
         fg=".ks3-misconception .ks3-sim-cover",
         bg=".ks3-misconception .ks3-sim-cover", need=4.5),
    dict(name="locked sim cover on ink-dark block", on=LESSON,
         fg=".ks3-practical .ks3-sim-cover",
         bg=".ks3-practical .ks3-sim-cover", need=4.5),
    dict(name="sim caption on ink-dark block", on=LESSON,
         fg=".ks3-practical .ks3-sim-caption", bg=".ks3-practical", need=4.5),
    dict(name="sim caption on card", on=LESSON,
         fg=".ks3-sim-caption", bg=".ks3-check", need=4.5),
    dict(name="stretch eyebrow on its tint", on=LESSON,
         fg=".ks3-stretch .ks3-eyebrow", bg="body", need=4.5),
    dict(name="stretch body on its tint", on=LESSON,
         fg=".ks3-stretch .ks3-layer-body p", bg=".ks3-stretch .ks3-layer-body",
         need=4.5),
    dict(name="legal line on page ground", on=LESSON,
         fg=".ks3-legal", bg="body", need=4.5),
    # need=3.0 because this text is LARGE by WCAG's definition — 19px at
    # weight 700, over the 18.66px-bold line. That is not the gate being
    # loosened: ks3.css sets that size and weight precisely because ink on
    # accent measures 4.49:1 and cannot clear the body threshold with any
    # colour in Design's palette. The style assertion below pins the size and
    # weight, so if either is ever reduced this pair becomes body text again
    # and layer C fails first.
    dict(name="tutor card text on accent (large-bold, 3:1)", on=LESSON,
         fg=".ks3-endmatter .ks3-tutor p", bg=".ks3-endmatter .ks3-tutor",
         need=3.0),
    dict(name="tutor CTA on its own light ground", on=LESSON,
         fg=".ks3-tutor-cta", bg=".ks3-tutor-cta", need=4.5),
    dict(name="tutor heading on accent", on=LESSON,
         fg=".ks3-endmatter .ks3-tutor h2", bg=".ks3-endmatter .ks3-tutor",
         need=3.0),
    dict(name="draft badge text on its tint", on=UNIT,
         fg=".ks3-badge.is-draft", bg=".ks3-badge.is-draft", need=4.5),
    dict(name="coming-soon badge text on its tint", on=UNIT_SOON,
         fg=".ks3-badge.is-soon", bg=".ks3-badge.is-soon", need=4.5),
    dict(name="coming-soon row title on dimmed row", on=UNIT_SOON,
         fg=".ks3-lesson-row.is-soon > a", bg=".ks3-lesson-row.is-soon", need=4.5),
    dict(name="family chip on its ground", on=UNIT,
         fg=".ks3-family", bg=".ks3-family", need=4.5),
    dict(name="cross-reference pointer on card", on=UNIT_REF,
         fg=".ks3-ref-note", bg=".ks3-lesson-list", need=4.5),
    dict(name="cross-reference badge on its tint", on=UNIT_REF,
         fg=".ks3-lesson-row.is-ref .ks3-badge",
         bg=".ks3-lesson-row.is-ref .ks3-badge", need=4.5),
    # identifying / state-bearing marks — 3:1 is the bar (R1)
    dict(name="MARK block border on page ground", on=LESSON,
         fg=".ks3-check", bg="body", need=3.0, prop="border-top-color"),
    dict(name="MARK card dog-ear on card", on=LESSON,
         fg=".ks3-card-btn", bg=".ks3-card-btn", need=3.0,
         prop="border-top-color", via_after=True),
    dict(name="MARK marked-rung spine on card", on=LESSON,
         fg='.ks3-rung[data-mode="marked"]', bg=".ks3-ladder", need=3.0,
         prop="border-left-color"),
    dict(name="MARK self-rung spine on card", on=LESSON,
         fg='.ks3-rung[data-mode="self"]', bg=".ks3-ladder", need=3.0,
         prop="border-left-color"),
    dict(name="MARK focus ring on page ground", on=LESSON,
         fg=".ks3-check .ks3-option", bg="body", need=3.0,
         prop="outline-color", force_focus=True),
]


# ── colour maths ─────────────────────────────────────────────────────────

def parse_rgba(s):
    """Any colour Chrome may resolve to → ((r, g, b), alpha) or None.

    Chrome returns `color(srgb 1 0.988 0.961 / 0.85)` for a `color-mix()`,
    which no naive rgb() regex matches. The locked simulation veil is exactly
    that, so a gate that cannot read it cannot check the one surface R5 is
    about — and would silently score it as unmeasurable rather than failing.
    """
    if not s:
        return None
    s = s.strip()
    m = re.match(r'#([0-9A-Fa-f]{6})$', s)
    if m:
        h = m.group(1)
        return ((int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)), 1.0)
    m = re.match(r'rgba?\(\s*([\d.]+)[,\s]+([\d.]+)[,\s]+([\d.]+)'
                 r'(?:[,\s/]+([\d.]+))?', s)
    if m:
        a = float(m.group(4)) if m.group(4) is not None else 1.0
        return (tuple(int(round(float(m.group(i)))) for i in (1, 2, 3)), a)
    # color(srgb <0-1> <0-1> <0-1> [/ <alpha>])
    m = re.match(r'color\(srgb\s+([\d.]+)\s+([\d.]+)\s+([\d.]+)'
                 r'(?:\s*/\s*([\d.]+))?', s)
    if m:
        a = float(m.group(4)) if m.group(4) is not None else 1.0
        return (tuple(int(round(float(m.group(i)) * 255)) for i in (1, 2, 3)), a)
    return None


def parse_rgb(s):
    """Opaque (r, g, b), or None. Alpha is dropped — use parse_rgba to keep it."""
    got = parse_rgba(s)
    return got[0] if got else None


def over(fg_rgba, behind):
    """Composite a translucent colour over an opaque one."""
    (r, g, b), a = fg_rgba
    return tuple(int(round(a * c + (1 - a) * d)) for c, d in zip((r, g, b), behind))


def _lin(c):
    c = c / 255.0
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def luminance(rgb):
    r, g, b = (_lin(x) for x in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast(a, b):
    la, lb = luminance(a), luminance(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)


def same_colour(got, want):
    g, w = parse_rgb(got), parse_rgb(want)
    return g is not None and w is not None and g == w


def close_length(got, want):
    def px(v):
        m = re.match(r'(-?[\d.]+)px$', (v or "").strip())
        return float(m.group(1)) if m else None
    a, b = px(got), px(want)
    if a is None or b is None:
        return None
    return abs(a - b) <= TOL_PX


# ── the browser-driven layers ────────────────────────────────────────────

# Resolves an element's EFFECTIVE background by walking up until it finds a
# non-transparent one. A card sitting on a card sitting on the page ground is
# the normal case, and measuring contrast against `transparent` is how a
# contrast table ends up reporting numbers that mean nothing.
_JS_HELPERS = r"""
window.__ks3 = {
  q: function (sel) { return document.querySelector(sel); },
  style: function (sel, prop, pseudo) {
    var el = document.querySelector(sel);
    if (!el) { return null; }
    var cs = getComputedStyle(el, pseudo || null);
    return cs.getPropertyValue(prop);
  },
  // Returns the STACK of backgrounds from the element outwards, so Python can
  // composite translucent layers instead of guessing. A veil at 0.85 alpha is
  // not "opaque enough to ignore" — it shifts the ground it sits on, and the
  // locked simulation cover is exactly that case.
  groundStack: function (sel) {
    var el = document.querySelector(sel);
    if (!el) { return null; }
    var out = [];
    while (el) {
      out.push(getComputedStyle(el).backgroundColor);
      el = el.parentElement;
    }
    out.push(getComputedStyle(document.body).backgroundColor);
    return out;
  },
  token: function (sel, name) {
    var el = document.querySelector(sel) || document.body;
    return getComputedStyle(el).getPropertyValue(name).trim();
  },
  fontOf: function (sel) {
    var el = document.querySelector(sel);
    if (!el) { return null; }
    return getComputedStyle(el).fontFamily;
  }
};
"""


# ── driven states ────────────────────────────────────────────────────────
#
# Layers C and D used to measure the page exactly as the generator wrote it.
# That is fine for a card or a heading, and useless for an answer button,
# whose whole reason to exist is what it does AFTER a student presses it.
# MRB-202 is what that blind spot cost: a correct answer rendered in the
# accent tint for a full release and 116 green assertions had nothing to say,
# because the only registered state of an option button was the resting one.
#
# A spec may now carry `drive="<name>"`. The gate loads the page FRESH for
# each drive, runs the snippet, settles, and only then measures that drive's
# specs. Fresh-per-drive matters: driving the ladder marks four buttons at
# once, and a later "resting" measurement on the same document would then be
# measuring a spent button and calling it resting.

DRIVES = {
    # One wrong answer in the first page-marked rung, one right answer in the
    # second. Between them that produces all four option states and both
    # feedback verdicts in a single document: the rung answered wrongly holds
    # is-wrong (the click), is-correct (the answer it reveals) and is-spent
    # (the rest), and the rung answered rightly holds the correct-verdict
    # feedback line.
    "ladder-answered": r"""
(function () {
  var rungs = document.querySelectorAll('.ks3-rung[data-mode="marked"]');
  if (rungs.length < 2) { return "need 2 page-marked rungs, found " + rungs.length; }
  function pick(rung, correct) {
    var opts = rung.querySelectorAll('.ks3-option');
    for (var j = 0; j < opts.length; j++) {
      if ((opts[j].getAttribute('data-correct') === '1') === correct) {
        opts[j].click();
        return true;
      }
    }
    return false;
  }
  if (!pick(rungs[0], false)) { return "no wrong option in rung 1"; }
  if (!pick(rungs[1], true))  { return "no correct option in rung 2"; }
  return "";
})()
""",
    # Any option in the first activity block. Which one is deliberately not
    # specified: under R3 every chosen activity option renders identically
    # whether it is right or wrong, and check_r3_runtime() below asserts
    # exactly that rather than trusting it.
    "activity-chosen": r"""
(function () {
  var first = document.querySelector('.ks3-check .ks3-option');
  if (!first) { return "no activity option found"; }
  first.click();
  return "";
})()
""",
    # The same commitment, on an ink-dark block, where the palette swaps the
    # accent for the alert because orange on ink cannot be read.
    "dark-option-chosen": r"""
(function () {
  var first = document.querySelector('.ks3-dark .ks3-option');
  if (!first) { return "no option on an ink-dark block"; }
  first.click();
  return "";
})()
""",
}


# Transitions are the reason a naive measurement lies. `.ks3-option` carries
# `transition: transform .14s, background-color .16s, border-color .16s`, so
# reading computed style straight after a click returns the colour the button
# is transitioning AWAY from — the resting one. Measured that way, a correctly
# implemented green state reports as cream, and the gate would raise a defect
# against work that is right.
#
# Cancelling transitions and animations snaps every property to its settled
# value with no sleep and no polling, so the measurement is deterministic
# rather than merely usually-long-enough. Only durations are suppressed; no
# target value changes, and the pop animation touches `transform` alone.
_JS_SETTLE = r"""
(function () {
  var s = document.getElementById('ks3-parity-settle');
  if (!s) {
    s = document.createElement('style');
    s.id = 'ks3-parity-settle';
    document.head.appendChild(s);
  }
  s.textContent = '*,*::before,*::after{transition:none!important;' +
                  'animation:none!important}';
  void document.body.offsetHeight;
  return true;
})()
"""


# R3 is Design's rule and Design's words: "Activity buttons never mark
# correctness. Only the mastery ladder marks right and wrong... Green and red
# must not appear on an activity button — if they do, the student reads the
# whole page as a test, and the point of committing before revealing is lost."
#
# Layer B checks this by proxy, asserting `data-correct` appears only inside
# the ladder. That catches the generator emitting marking DATA and misses the
# thing the rule is actually about, which is what the button LOOKS like once
# pressed. This is the direct form: press every option in turn and assert the
# resolved colours are identical whichever was pressed, and that none of them
# is a marking colour. If a correct answer were ever tinted differently from a
# wrong one on an activity block, this fails and names the block.
_JS_R3_RUNTIME = r"""
(function () {
  var MARKING = ['rgb(18, 161, 80)', 'rgb(228, 247, 235)', 'rgb(10, 107, 54)'];
  var out = [];
  var blocks = document.querySelectorAll('.ks3-block.ks3-check, .ks3-block.ks3-misconception, .ks3-block.ks3-practical');
  for (var b = 0; b < blocks.length; b++) {
    var opts = blocks[b].querySelectorAll('.ks3-option');
    if (!opts.length) { continue; }
    var seen = [], disabled = false;
    for (var i = 0; i < opts.length; i++) {
      opts[i].click();
      var cs = getComputedStyle(opts[i]);
      var mk = opts[i].querySelector('.ks3-opt-mark');
      var sig = [cs.backgroundColor, cs.borderTopColor,
                 mk ? getComputedStyle(mk).backgroundColor : '',
                 mk ? getComputedStyle(mk).color : ''].join(' | ');
      seen.push(sig);
      if (opts[i].disabled) { disabled = true; }
    }
    var id = blocks[b].getAttribute('data-activity') || ('block ' + b);
    var uniq = seen.filter(function (v, i, a) { return a.indexOf(v) === i; });
    if (uniq.length !== 1) {
      out.push(id + ': chosen options do not all render alike — ' +
               uniq.length + ' distinct treatments: ' + uniq.join('  //  '));
    }
    for (var u = 0; u < uniq.length; u++) {
      for (var m = 0; m < MARKING.length; m++) {
        if (uniq[u].indexOf(MARKING[m]) !== -1) {
          out.push(id + ': a marking colour (' + MARKING[m] +
                   ') appears on an activity option — ' + uniq[u]);
        }
      }
    }
    if (disabled) { out.push(id + ': an activity option was disabled'); }
  }
  return { problems: out, blocks: blocks.length };
})()
"""


def check_r3_runtime(page):
    """R3, asserted on the painted button rather than on the markup.

    Returns (problems, info). Mutates the page — call it on a fresh load.
    """
    page.eval(_JS_SETTLE)          # settle FIRST, so every click lands instantly
    info = page.eval(_JS_R3_RUNTIME)
    return (["R3: " + p for p in info["problems"]], info)


# The runtime half of the drawn-mark rule. Layer B can only see the HTML as
# written; this sees the DOM as painted, INCLUDING the ladder feedback, which
# does not exist until a wrong option has been clicked. That feedback is where
# the authored "liquid → gas" corrections land, so it is the one place the
# static scan structurally cannot reach.
_JS_GLYPH_AUDIT = r"""
(function () {
  var bad = /[\u2192\u2713\u2715]/g;
  function scan() { return (document.body.innerText.match(bad) || []); }
  var before = scan();
  // Click one WRONG option in each page-marked rung to force the feedback.
  var rungs = document.querySelectorAll('.ks3-rung[data-mode="marked"]');
  for (var i = 0; i < rungs.length; i++) {
    var opts = rungs[i].querySelectorAll('.ks3-option');
    for (var j = 0; j < opts.length; j++) {
      if (opts[j].getAttribute('data-correct') !== '1') { opts[j].click(); break; }
    }
  }
  var after = scan();
  var fb = document.querySelectorAll('.ks3-feedback').length;
  return { before: before, after: after, feedbackShown: fb,
           svgMarks: document.querySelectorAll('svg.ks3-mark').length };
})()
"""


def check_rendered_glyphs(page):
    """Returns (problems, info). Mutates the page — call it last."""
    info = page.eval(_JS_GLYPH_AUDIT)
    problems = []
    if info["before"]:
        problems.append("rendered text carries %d undrawable glyph(s) before "
                        "interaction: %r" % (len(info["before"]), info["before"][:5]))
    if info["after"]:
        problems.append("rendered text carries %d undrawable glyph(s) AFTER the "
                        "ladder feedback appears: %r — ks3.js must convert them "
                        "to inline SVG when it injects authored text"
                        % (len(info["after"]), info["after"][:5]))
    if not info["feedbackShown"]:
        problems.append("no .ks3-feedback appeared after clicking a wrong "
                        "option — the runtime glyph audit did not actually run")
    return (problems, info)



def _flatten(stack):
    """Composite a background stack (innermost first) into one opaque colour."""
    if not stack:
        return None
    layers = [parse_rgba(s) for s in stack]
    layers = [l for l in layers if l]
    base = None
    for l in reversed(layers):
        if l[1] >= 0.999:
            base = l[0]
        elif base is not None:
            base = over(l, base)
    return base


def _pages_needed():
    seen = []
    for spec in COMPONENTS + CONTRAST:
        if spec["on"] not in seen:
            seen.append(spec["on"])
    return seen


def _drives_needed(rel):
    """Drive names used by any spec on this page, in declaration order."""
    seen = []
    for spec in COMPONENTS + CONTRAST:
        d = spec.get("drive")
        if spec["on"] == rel and d and d not in seen:
            seen.append(d)
    return seen


def _unregistered_drives():
    """A spec naming a drive that does not exist is a silently-skipped
    assertion, which is the failure mode this whole ticket is about."""
    bad = []
    for spec in COMPONENTS + CONTRAST:
        d = spec.get("drive")
        if d and d not in DRIVES:
            bad.append("%s names unknown drive %r" % (spec["name"], d))
    return bad


def mutation_test_correct_state(ks3_root, browser_mod):
    """Prove the correct-answer assertions can actually fail.

    MRB-202 got into production because the correct-answer state was never
    registered, so the gate had nothing to compare and printed green. Adding
    the registration fixes that only if the registration really bites — an
    assertion that cannot fail is not a gate, it is a comment.

    So this repaints a CORRECT answer in the accent tint, exactly as the
    defect did, and requires the gate to notice AND to name the component.
    It mutates the rendered page rather than the expectation table: mutating
    the table would only prove that two different strings are unequal.

    Returns (detected, detail).
    """
    targets = ["ladder option CHOSEN-CORRECT", "ladder option CHOSEN-CORRECT badge"]
    specs = [c for c in COMPONENTS if c["name"] in targets]
    if len(specs) != len(targets):
        return (False, "the correct-answer components are not registered at all "
                       "— expected %r" % (targets,))

    # The defect, reproduced faithfully: a correct answer wearing exactly the
    # treatment a chosen activity option wears — accent tint, accent border,
    # accent badge with on-dark glyph. Every registered colour on the state is
    # moved, so "every colour assertion must fail" is a fair bar; an assertion
    # left standing here would be one that cannot see this defect.
    mutant = (
        "(function(){var s=document.createElement('style');"
        "s.textContent='.ks3-option.is-correct{background:var(--ks3-accent-tint)"
        "!important;border-color:var(--ks3-accent)!important}"
        ".ks3-option.is-correct .ks3-opt-mark{background:var(--ks3-accent)"
        "!important;color:var(--ks3-on-dark)!important}';"
        "document.head.appendChild(s);return true;})()")

    served_root = os.path.dirname(os.path.abspath(ks3_root))
    prefix = os.path.basename(os.path.abspath(ks3_root))
    server, port = browser_mod.serve(served_root)
    caught, missed = [], []
    try:
        with browser_mod.Browser() as b:
            page = b.page("http://127.0.0.1:%d/%s/%s" % (port, prefix, LESSON))
            page.eval(_JS_HELPERS + "true")
            page.eval(_JS_SETTLE)
            err = page.eval(DRIVES["ladder-answered"])
            if err:
                return (False, "could not drive the ladder into its answered "
                               "state: %s" % err)
            page.eval(mutant)
            page.eval(_JS_SETTLE)

            for spec in specs:
                for prop, want in sorted(spec["props"].items()):
                    if not want.startswith("#"):
                        continue
                    got = (page.eval("window.__ks3.style(%r, %r)"
                                     % (spec["sel"], prop)) or "").strip()
                    if same_colour(got, want):
                        missed.append("%s / %s still resolved %s"
                                      % (spec["name"], prop, got))
                    else:
                        caught.append("%s / %s: %s → %s"
                                      % (spec["name"], prop, want, got))
    finally:
        server.shutdown()

    if missed:
        return (False, "the mutation did NOT fail these assertions, so they "
                       "cannot catch the defect they exist for: %s"
                       % "; ".join(missed))
    return (True, "accent repaint caught by %d assertion(s), naming the "
                  "component: %s" % (len(caught), "; ".join(caught[:4])))


def run_browser_layers(ks3_root, browser_mod):
    """Layers C and D. Returns (problems, style_rows, contrast_rows).

    ⚠️ THE SERVER IS ROOTED AT THE PARENT OF ks3/, NOT AT ks3/ ITSELF.

    Every KS3 page links `/shared/tokens.css`, `/shared/ks3.css` and
    `/shared/ks3.js` as ABSOLUTE paths. Serving `mrbadmus_site/ks3` as the
    document root makes all three 404, so the page loads with no CSS at all —
    and then the gate does not report "stylesheet missing", it reports 82 style
    mismatches and 23 contrast failures at 1.00:1 in Times New Roman. That is
    the worst possible failure mode for a gate: a real defect in the harness
    wearing the costume of a hundred defects in the work.

    So it serves the parent and requests `/ks3/<rel>`, and it ASSERTS the
    stylesheet actually applied before trusting a single measurement.
    """
    problems = []
    style_rows = []
    contrast_rows = []

    served_root = os.path.dirname(os.path.abspath(ks3_root))
    prefix = os.path.basename(os.path.abspath(ks3_root))

    # A spec pointing at a drive that does not exist would simply never be
    # measured, and would read as a covered state in the manifest. That is the
    # exact shape of the hole MRB-202 came through, so it is fatal here.
    problems.extend("PARITY: " + u for u in _unregistered_drives())

    seen_console = set()

    def fresh(b, url, rel):
        """Load the page clean and prove the stylesheet applied. None if not."""
        page = b.page(url)
        page.eval(_JS_HELPERS + "true")

        # Sanity FIRST: did ks3.css actually load and apply? If not, every
        # number below is measured against an unstyled document and the gate
        # would blame the work for a plumbing fault.
        applied = page.eval(
            "(function(){var s=getComputedStyle(document.body);"
            "return {sheets: document.styleSheets.length,"
            " ground: s.backgroundColor,"
            " token: s.getPropertyValue('--ks3-ground').trim(),"
            " font: s.fontFamily};})()")
        if not applied["token"]:
            problems.append(
                "STYLESHEET DID NOT APPLY on /%s — %d sheets, ground %s, "
                "font %s. Every style and contrast number for this page "
                "would be meaningless, so they are not reported."
                % (rel, applied["sheets"], applied["ground"], applied["font"]))
            return None
        return page

    def drain_console(page, rel, doing):
        """A favicon 404 is an artefact of serving a bare tree, not a defect in
        the page. Every other console error stays fatal. The same page is now
        loaded several times, so each distinct message is reported once."""
        for e in page.console_errors():
            if "favicon" in e.lower():
                continue
            key = (rel, e)
            if key in seen_console:
                continue
            seen_console.add(key)
            problems.append("console error on /%s%s: %s" % (rel, doing, e))

    def measure_c(page, rel, drive):
        for spec in COMPONENTS:
            if spec["on"] != rel or spec.get("drive") != drive:
                continue
            sel = spec["sel"]
            if not page.eval("!!window.__ks3.q(%r)" % sel):
                problems.append("PARITY: %s — selector %s not present on /%s%s"
                                % (spec["name"], sel, rel,
                                   " after driving %s" % drive if drive else ""))
                continue
            for prop, want in sorted(spec["props"].items()):
                got = (page.eval("window.__ks3.style(%r, %r)" % (sel, prop))
                       or "").strip()
                if prop == "font-family":
                    ok = want.lower() in got.lower()
                elif want.startswith("#"):
                    ok = same_colour(got, want)
                elif want.endswith("px"):
                    ok = close_length(got, want)
                else:
                    ok = (got.lower() == want.lower())
                style_rows.append((spec["name"], prop, want, got, bool(ok)))
                if not ok:
                    problems.append(
                        "PARITY: %s — %s expected %s, resolved %s (%s on /%s)"
                        % (spec["name"], prop, want, got or "<empty>", sel, rel))

    def measure_d(page, rel, drive):
        for spec in CONTRAST:
            if spec["on"] != rel or spec.get("drive") != drive:
                continue
            fg_sel, bg_sel = spec["fg"], spec["bg"]
            if not page.eval("!!window.__ks3.q(%r)" % fg_sel):
                problems.append("CONTRAST: %s — selector %s not present on /%s%s"
                                % (spec["name"], fg_sel, rel,
                                   " after driving %s" % drive if drive else ""))
                continue
            if spec.get("force_focus"):
                fg = page.eval("window.__ks3.token(%r, '--ks3-accent')" % fg_sel)
            elif spec.get("via_after"):
                fg = page.eval("window.__ks3.style(%r, %r, '::after')"
                               % (fg_sel, spec.get("prop", "color")))
            else:
                fg = page.eval("window.__ks3.style(%r, %r)"
                               % (fg_sel, spec.get("prop", "color")))
            stack = page.eval("window.__ks3.groundStack(%r)" % bg_sel)
            bg = _flatten(stack)
            f, g = parse_rgb(fg), bg
            if f is None or g is None:
                problems.append("CONTRAST: %s — could not resolve (fg=%r bg=%r)"
                                % (spec["name"], fg, bg))
                continue
            ratio = contrast(f, g)
            need = spec["need"]
            ok = ratio >= need - 0.005
            name_out = spec["name"]

            # WCAG 1.4.3 exempts an INACTIVE user-interface component. Claiming
            # that exemption is only honest if the component really is inactive,
            # so the gate checks rather than takes the spec's word for it.
            guard = spec.get("exempt_if_disabled")
            if not ok and guard:
                disabled = page.eval(
                    "(function(){var e=document.querySelector(%r);"
                    "return !!(e && e.disabled);})()" % guard)
                if disabled:
                    ok = True
                    name_out = "%s [exempt: disabled control]" % spec["name"]
                else:
                    problems.append(
                        "CONTRAST FAIL: %s — %.2f:1 against %.1f:1 required, and "
                        "its WCAG 1.4.3 exemption does not apply because %s is "
                        "NOT disabled" % (spec["name"], ratio, need, guard))
                    contrast_rows.append((spec["name"], fg, bg, ratio, need, False))
                    continue

            contrast_rows.append((name_out, fg, bg, ratio, need, ok))
            if not ok:
                problems.append(
                    "CONTRAST FAIL: %s — %.2f:1 against %.1f:1 required "
                    "(%s on %s)" % (spec["name"], ratio, need, fg, bg))

    server, port = browser_mod.serve(served_root)
    try:
        with browser_mod.Browser() as b:
            for rel in _pages_needed():
                url = "http://127.0.0.1:%d/%s/%s" % (port, prefix, rel)

                # ── pass 1: the page as the generator wrote it ──
                page = fresh(b, url, rel)
                if page is None:
                    continue
                drain_console(page, rel, "")
                measure_c(page, rel, None)
                measure_d(page, rel, None)

                # ── one FRESH load per driven state ──
                # Fresh, not sequential: the ladder drive marks four buttons at
                # once, so measuring "resting" afterwards on the same document
                # would be measuring a spent button and calling it resting.
                for drive in _drives_needed(rel):
                    page = fresh(b, url, rel)
                    if page is None:
                        continue
                    page.eval(_JS_SETTLE)
                    err = page.eval(DRIVES[drive])
                    if err:
                        problems.append(
                            "DRIVE: %s could not reach its state on /%s — %s. "
                            "Its assertions did not run."
                            % (drive, rel, err))
                        continue
                    page.eval(_JS_SETTLE)
                    drain_console(page, rel, " while driving %s" % drive)
                    measure_c(page, rel, drive)
                    measure_d(page, rel, drive)

                # ── runtime audits, each on its own fresh load: they click ──
                if rel == LESSON:
                    page = fresh(b, url, rel)
                    if page is not None:
                        r3, r3info = check_r3_runtime(page)
                        problems.extend(r3)
                        drain_console(page, rel, " during the R3 runtime audit")
                        style_rows.append(
                            ("R3 runtime: a chosen activity option never marks",
                             "identical treatment, no marking colour",
                             "0 problems across all activity blocks",
                             "%d problem(s) across %d block(s)"
                             % (len(r3info["problems"]), r3info["blocks"]),
                             not r3))

                    page = fresh(b, url, rel)
                    if page is not None:
                        gl, ginfo = check_rendered_glyphs(page)
                        problems.extend("GLYPH: " + g for g in gl)
                        style_rows.append(
                            ("runtime glyph audit", "undrawable glyphs", "0",
                             "%d before / %d after (%d feedback, %d svg marks)"
                             % (len(ginfo["before"]), len(ginfo["after"]),
                                ginfo["feedbackShown"], ginfo["svgMarks"]),
                             not gl))
    finally:
        server.shutdown()

    return (problems, style_rows, contrast_rows)
