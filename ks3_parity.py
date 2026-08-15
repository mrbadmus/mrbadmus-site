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

import json
import os
import re
from html import unescape as _unescape

REF_DIR = os.path.join("docs", "ks3", "design-reference")
ARTIFACTS = (
    "KS3 Reference Set (offline).html",
    "KS3 Parts Library (offline).html",
    "KS3 Mastery Ladder (offline).html",
    "KS3 Simulation (offline).html",
    # MRB-182 — the browse-layer prototype: the hub, year, half-term and
    # subject screens. It is the provenance for the season trio, the three
    # year tints and the browse-layer surfaces (--ks3-dot, --ks3-dark-track,
    # --ks3-tag). Without it registered, Layer A would correctly report every
    # one of those as invented.
    "KS3 Browse Layer (offline).html",
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

        # MRB-198 — every sim, statically: the R5 cover present, the
        # control panel emitted EMPTY (the JS builds it; placeholder text
        # is a promise the page cannot keep). For the two payload-carrying
        # kinds: an aria-label that actually narrates the mechanism — not
        # a stub, because it is the only description a non-sighted student
        # gets — and a parseable, non-empty payload. A gutted SIM_ARIA
        # entry or a dropped payload attribute fails HERE, by name.
        for m in re.finditer(r'<div class="ks3-sim" data-sim="([a-z-]+)"'
                             r'[^>]*>', html):
            kind = m.group(1)
            attrs = m.group(0)
            window = html[m.start():m.start() + 6000]
            if '<div class="ks3-sim-controls"></div>' not in window:
                problems.append("SIM: %s %s — control panel not emitted "
                                "empty" % (rel, kind))
            if 'class="ks3-sim-cover"' not in window:
                problems.append("SIM: %s %s — missing the R5 cover"
                                % (rel, kind))
            if kind in ("microscope", "system-parts"):
                am = re.search(r'aria-label="([^"]*)"', window)
                aria = _unescape(am.group(1)) if am else ""
                if not aria.startswith("Animation:") or len(aria) < 120:
                    problems.append(
                        "SIM: %s %s — aria-label missing or gutted "
                        "(%d chars); it must narrate the mechanism"
                        % (rel, kind, len(aria)))
                pattr = ("data-specimens" if kind == "microscope"
                         else "data-parts")
                pm = re.search(pattr + r'="([^"]*)"', attrs)
                try:
                    payload = json.loads(_unescape(pm.group(1))) if pm else []
                except ValueError:
                    payload = []
                if not payload:
                    problems.append(
                        "SIM: %s %s — no parseable %s payload; the "
                        "instrument would render an empty %s"
                        % (rel, kind, pattr,
                           "slide" if kind == "microscope" else "system"))

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
# MRB-198 — the two new instrument kinds, each gated on the page whose
# payload exercises it hardest: the microscope on L2 (three slides), and
# system-parts on L5 (five levels of a stomach, including the one_of_many
# scale rule). Both sims sit in dark `practical` shells in B1, so the new
# kinds' locked covers, captions, controls and readouts are all measured
# on the ink-dark ground here; the amber-ground cover pair stays measured
# on the C1 lesson above.
B1_MICRO = "biology/cells-and-organisation/using-a-microscope.html"
B1_PARTS = "biology/cells-and-organisation/levels-of-organisation.html"
# ⊕ B1 round two. A component is registered on a page that RENDERS it — a
# component measured on a page that lacks it reports "selector not present" and
# passes, which is the absence-of-assertion failure this gate exists to close.
B1_LIFE = "biology/cells-and-organisation/life-processes.html"
B1_UNI = "biology/cells-and-organisation/unicellular-organisms.html"

# ── parking, and why it is not deletion ──────────────────────────────────
#
# A spec may carry `parked="<reason>"`. It is then not measured, and it is
# REPORTED as parked in the run's output rather than passing quietly.
#
# This exists for one narrow case: machinery that is sound, registered, and
# currently rendered by no page. `system-parts` is exactly that — B1-05 used to
# carry it, and Design's approved B1-05 replaces it with `removal-cases`
# (measured: zero `.ks3-sim`, zero `<select>`, no dependency graph anywhere on
# the page). The engine in `shared/ks3.js` is audited and correct; nothing
# renders it.
#
# Deleting the registrations would throw away real coverage the day a lesson
# uses the kind again. Leaving them pointed at a page that no longer has the
# component fails the gate forever, and a gate that always fails is a gate
# everyone learns to ignore — which is how the 11 August sign-off happened.
#
# Parking is neither. Nothing is lost, nothing silently passes, and the output
# says in words which components are not currently being measured and why.
# MRB-203's registry still guards the real risk: if a lesson renders a block
# type whose components are not defined, the build fails naming it.
_PARKED_SYSTEM_PARTS = (
    "no lesson renders a system-parts sim — Design's approved B1-05 replaces "
    "it with `removal-cases`. Engine and audit kept; un-park when a lesson "
    "uses the kind again.")
UNIT = "chemistry/particles-and-their-behaviour/index.html"
# C1 is fully authored, so its index carries no Coming soon badge; and B3 is
# the ONLY unit in the key stage with a §4.6 reference slot, so it is the only
# page where the pointer can be measured at all.
# UNIT_SOON moved off B1 when MRB-198 landed Design's B1 content — a fully
# authored unit has no coming-soon rows to measure. B2 is the next unit in
# the same discipline with none of its lessons authored.
UNIT_SOON = "biology/movement-skeleton-and-muscles/index.html"
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
    # ⊕ MRB-208 amendment 1: on a LESSON page the trail moved into the header
    # bar and `.ks3-crumbs` came off. It is body 17px/600, not the row's mono
    # 14px — they are two different components and only one of them is a
    # lesson's. The mono row survives on unit indices, discipline hubs and the
    # browse layer, and is gated there.
    dict(name="header trail is body type (MRB-208)", on=LESSON, sel=".ks3-trail",
         props={"font-family": "Instrument Sans", "font-size": "17px"}),
    dict(name="breadcrumb row is mono", on=UNIT, sel=".ks3-crumbs",
         props={"font-family": "DM Mono", "font-size": "14px"}),
    # MRB-197: Design's nav mark. Pinned to the frozen reference's header —
    # if the wordmark shrinks below display size, the chevron's 3:1 pair
    # below stops being the whole story and this fails first.
    dict(name="nav brand wordmark (MRB-197)", on=LESSON, sel=".ks3-brand",
         props={"font-family": "Bricolage Grotesque", "font-weight": "800",
                "font-size": "22px", "color": "#221E1B"}),
    # ⊖ Design's B1 delivery drew the chevron inside a 34px accent tile. NOT
    # adopted on the replay: MRB-197 is Mide's standing brand ruling and
    # `NAV_BRAND` is one mark for all 296 KS3 pages, so taking the tile would
    # have restyled the browse layer Mide has just approved. Parked for Mide —
    # see the ledger entry of 15 Aug 2026. The row is removed rather than left
    # pointing at a selector nothing emits, so MRB-203's registry stays honest.

    # ── B1 round two: the four block types §5.1.1 added ──
    #
    # Each is registered on a page that actually renders it, because a
    # component measured on a page without it reports "selector not present"
    # and passes — which is the absence-of-assertion failure MRB-198 fixed one
    # level down and MRB-203 fixed one level up.
    dict(name="KEY FACT box is band on an ACCENT shadow", on=B1_LIFE,
         sel=".ks3-keyfact",
         props={"background-color": "#F4E9D8", "border-top-color": "#221E1B",
                "border-top-width": "2px",
                "border-top-left-radius": "20px",
                # The accent shadow is the whole distinction from a
                # `.ks3-block`, whose shadow is ink. If this ever resolves to
                # ink the box stops reading as a key fact and starts reading
                # as one more card.
                "box-shadow": "rgb(228, 87, 46) 5px 5px 0px 0px"}),
    dict(name="KEY FACT label is mono accent-text", on=B1_LIFE,
         sel=".ks3-keyfact-label",
         props={"font-family": "DM Mono", "font-size": "13px",
                "text-transform": "uppercase", "color": "#A93411"}),
    dict(name="KEY FACT statement is display 700", on=B1_LIFE,
         sel=".ks3-keyfact-body",
         props={"font-family": "Bricolage Grotesque", "font-size": "22px",
                "font-weight": "700", "color": "#221E1B"}),
    # The statement panel. 3px and no shadow is what separates it from a
    # `.ks3-block`; the clamp is drift 3's RULED value, not this page's own.
    dict(name="statement panel is band on a 3px ink border", on=B1_LIFE,
         sel=".ks3-rule",
         props={"background-color": "#F4E9D8", "border-top-color": "#221E1B",
                "border-top-width": "3px", "border-top-left-radius": "28px",
                "box-shadow": "none"}),
    # ⚠️ NO `font-size` HERE, and the omission is deliberate. The statement is
    # `clamp(28px, 3.9vw, 44px)` — drift 3's ruled value — so its computed size
    # is a function of the VIEWPORT, and this harness pins no viewport: headless
    # Chrome lands around 756px, where the clamp resolves to 29.48px. Asserting
    # 44px here would fail on a correct page, and asserting 29.48px would pin
    # the harness's window size as if it were a design decision. The clamp is
    # gated where a viewport actually exists — `tools/compare_b1.py`, at
    # 1280 / 1340 / 820 / 390.
    dict(name="statement is display 800 at the ruled clamp", on=B1_LIFE,
         sel=".ks3-rule-statement",
         # `text-align: start` is the viewport-free half of the rule/formula
         # distinction — the formula's statement is centred with no measure,
         # this one is left-aligned at 20ch. `max-width` cannot be asserted
         # here: `ch` resolves against the clamped font size, so it computes to
         # a different px value at every viewport.
         props={"font-family": "Bricolage Grotesque", "font-weight": "800",
                "color": "#221E1B", "text-align": "start"}),
    # `--ks3-option-border` and not ink — that is what separates these from the
    # misconception block's cards.
    dict(name="statement cards take the option border", on=B1_LIFE,
         sel=".ks3-rule-cards li",
         props={"background-color": "#FFFCF5",
                "border-top-color": "#DDCFB6", "border-top-width": "2px",
                "border-top-left-radius": "22px"}),
    # The formula. Centred with NO max-width is the entire difference between
    # this and `rule`'s left-aligned 20ch measure — the shells are otherwise
    # identical and a future tidy-up will try to merge them.
    dict(name="formula panel is centred", on=B1_MICRO,
         sel=".ks3-formula-statement",
         props={"background-color": "#F4E9D8", "border-top-width": "3px",
                "text-align": "center"}),
    # `max-width: none` is the assertion that matters and it is viewport-free:
    # it is the ONLY thing separating this shell from `rule`'s, which caps its
    # statement at 20ch. Its own clamp (26/3.6vw/40 against the rule's
    # 28/3.9vw/44) is viewport-dependent for the reason above.
    dict(name="formula statement takes the FORMULA clamp, not the rule's",
         on=B1_MICRO, sel=".ks3-formula-statement p",
         props={"font-family": "Bricolage Grotesque", "font-weight": "800",
                "max-width": "none", "text-align": "center"}),
    # The comparison rows. FLEX, never grid — a grid cannot produce the 820px
    # stack without a second query (MRB-210).
    dict(name="comparison rows are flex, not grid", on=B1_UNI,
         sel=".ks3-compare-row",
         props={"display": "flex", "flex-wrap": "wrap",
                "border-top-width": "2px"}),
    # The harness pins no viewport and headless lands under 820px, so what it
    # measures here is the STACKED state — which is the one MRB-210 cares about
    # and the one that breaks the discrimination on a phone if it regresses.
    # The wide 118px basis is gated by `tools/compare_b1.py` at 1280 and 1340.
    dict(name="comparison label stacks below 820", on=B1_UNI,
         sel=".ks3-compare-name", props={"flex-basis": "100%"}),
    dict(name="comparison content cells shrink to zero", on=B1_UNI,
         sel=".ks3-compare-cell",
         props={"flex-basis": "250px", "min-width": "0px"}),

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

    # ── figure. Surfaced by MRB-203's §10.2 registry: `figure` is the
    # second most-rendered block type in the key stage (27 uses across
    # 12 lessons) and had no registered component at all. The gate that
    # asks "does every rendered block type map to something registered?"
    # found it on its first run, which is the whole argument for the
    # registry being authoritative rather than descriptive.
    dict(name="figure frame", on=LESSON, sel=".ks3-figure",
         props={"margin-top": "28px"}),
    dict(name="figure caption", on=LESSON, sel=".ks3-figure figcaption",
         props={"font-size": "17px", "color": "#3B342E",
                "margin-top": "12px"}),
    dict(name="figure pending slot", on=LESSON, sel=".ks3-figure-slot",
         props={"border-top-width": "3px", "border-top-style": "dashed",
                "border-top-color": "#C3B191"}),

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

    # ── MRB-198: the two new instrument kinds ──
    dict(name="microscope canvas (dark practical shell)", on=B1_MICRO,
         sel='.ks3-sim[data-sim="microscope"] .ks3-sim-canvas',
         props={"background-color": "#F7EFE1", "border-top-color": "#C6B9A7",
                "border-top-left-radius": "20px"}),
    dict(name="system-parts canvas (dark practical shell)", on=B1_PARTS, parked=_PARKED_SYSTEM_PARTS,
         sel='.ks3-sim[data-sim="system-parts"] .ks3-sim-canvas',
         props={"background-color": "#F7EFE1", "border-top-color": "#C6B9A7",
                "border-top-left-radius": "20px"}),
    # The control panel only exists in the DOM once built and only shows
    # once unlocked (R5), so these run in the page's after-unlock pass.
    dict(name="microscope control label on dark ground", on=B1_MICRO,
         sel=".ks3-practical .ks3-sim-control", drive="sim-unlocked",
         props={"font-size": "17px", "font-weight": "600",
                "color": "#E7DECE"}),
    dict(name="microscope specimen select", on=B1_MICRO,
         sel=".ks3-practical .ks3-sim-control select", drive="sim-unlocked",
         props={"background-color": "#FFFCF5", "border-top-color": "#221E1B",
                "font-size": "17px", "min-height": "44px",
                "border-top-left-radius": "14px", "color": "#221E1B"}),
    dict(name="microscope focus wheel takes the accent", on=B1_MICRO,
         sel='.ks3-practical .ks3-sim-control input[type="range"]',
         drive="sim-unlocked",
         props={"accent-color": "#E4572E", "height": "44px"}),
    dict(name="system-parts part selector", on=B1_PARTS, parked=_PARKED_SYSTEM_PARTS,
         sel=".ks3-practical .ks3-sim-control select", drive="sim-unlocked",
         props={"background-color": "#FFFCF5", "border-top-color": "#221E1B",
                "font-size": "17px", "min-height": "44px",
                "border-top-left-radius": "14px", "color": "#221E1B"}),

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
    # MRB-182: Design recoloured the browse layer BY TERM rather than by
    # borrowing the subject hues. The seasons used to be the accent, the
    # success green and the physics blue, which meant a half-term tile and a
    # subject dot could be the same colour while meaning different things.
    # They are their own three hues now. The SELECTOR is unchanged on purpose
    # — .ks3-code stays on the numbered season badge, so what this asserts is
    # still "the season tile is the season colour", only the colours moved.
    dict(name="half-term card, autumn season", on=YEAR,
         sel='.ks3-browse-ht[data-season="autumn"] .ks3-code',
         props={"background-color": "#E08A1E"}),
    dict(name="half-term card, spring season", on=YEAR,
         sel='.ks3-browse-ht[data-season="spring"] .ks3-code',
         props={"background-color": "#7FB927"}),
    dict(name="half-term card, summer season", on=YEAR,
         sel='.ks3-browse-ht[data-season="summer"] .ks3-code',
         props={"background-color": "#22B8CF"}),

    # ── ⊕ the eleven instruments (14 Aug 2026) ──────────────────────────
    #
    # Each row pins the property that makes its instrument DISTINCT, not the
    # ones it shares with every card on the page. That is the whole point:
    # `test-board` and `sort-rows` passed the kinds gate for a fortnight with
    # a dispatch-table entry, no CSS and no JS, because the gate asks whether a
    # renderer exists and a renderer is not a component. A layer-C assertion
    # cannot be satisfied that way — with no stylesheet the selector resolves
    # to the browser default and fails by name. Registration now IMPLIES
    # realisation, which is what §10.2 was always supposed to mean.
    #
    # Every row is `on` a page that actually renders it: a component registered
    # on a page that lacks it reports "selector not present" and passes.
    dict(name="board lamp is a column, not an option row", on=B1_LIFE,
         sel=".ks3-lamp",
         props={"display": "flex", "flex-direction": "column",
                "border-top-width": "2px",
                "border-top-left-radius": "16px"}),
    dict(name="board lamp badge is a 28px display square", on=B1_LIFE,
         sel=".ks3-lamp-badge",
         props={"width": "28px", "height": "28px",
                "font-family": "Bricolage Grotesque", "font-weight": "800"}),
    dict(name="board verdict is ink-dark", on=B1_LIFE,
         sel=".ks3-board-verdict",
         props={"background-color": "#221E1B", "color": "#FBF3E6"}),
    dict(name="board tally is mono 24px", on=B1_LIFE,
         sel=".ks3-board-tally",
         props={"font-family": "DM Mono", "font-size": "24px"}),
    dict(name="sorter row is a card on a hairline, not an option", on=B1_LIFE,
         sel=".ks3-sortrow",
         props={"background-color": "#FFFCF5", "border-top-color": "#E0D2B9",
                "border-top-width": "2px"}),
    dict(name="sorter chip is 16px, narrower than a segment", on=B1_LIFE,
         sel=".ks3-sort-chip",
         props={"font-size": "16px", "min-height": "44px",
                "border-top-left-radius": "14px"}),
    # The self-check is MRB-196's, and the ONLY thing that proves it is not a
    # marked question is that its options carry no correctness data at all —
    # asserted structurally by check_r3_runtime, and here by its being an
    # ordinary option group on an ordinary ground.
    dict(name="self-check options are a plain grid", on=B1_LIFE,
         sel=".ks3-selfcheck-options",
         props={"display": "grid"}),

    dict(name="settles-it feature is a panel, not a row", on=B1_UNI,
         sel=".ks3-feature",
         props={"background-color": "#FFFCF5", "border-top-color": "#C3B191",
                "border-top-left-radius": "20px"}),
    dict(name="settles-it choice is 16px on the ground", on=B1_UNI,
         sel=".ks3-settle-choice",
         props={"font-size": "16px", "background-color": "#FBF3E6",
                "min-height": "44px"}),
    # ⚖️ MRB-196: ONE tone. If this ever resolves to `--ks3-ink` the instrument
    # has started marking the student again, ~6 ΔL* at a time.
    dict(name="settles-it why is ONE tone (MRB-196)", on=B1_UNI,
         sel=".ks3-feature-why", props={"color": "#3B342E"}),
    dict(name="case verdict is ink-dark with an alert label", on=B1_UNI,
         sel=".ks3-case-verdict", props={"background-color": "#221E1B"}),

    dict(name="bench cell picker is a full-width ROW, not a segment",
         on="biology/cells-and-organisation/specialised-cells.html",
         sel=".ks3-bench-cell",
         props={"min-height": "56px", "text-align": "left",
                "border-top-left-radius": "16px"}),
    dict(name="tuning dial is a fixed 74px mono chip",
         on="biology/cells-and-organisation/specialised-cells.html",
         sel=".ks3-tune-dial",
         props={"font-family": "DM Mono", "font-size": "12px",
                "border-top-width": "2px"}),
    dict(name="sabotage chain's first link is the cell itself",
         on="biology/cells-and-organisation/specialised-cells.html",
         sel=".ks3-chain-link:first-child",
         props={"background-color": "#F4E9D8", "border-top-color": "#221E1B"}),

    dict(name="zoom slider clears the 44px tap target", on=B1_PARTS,
         sel=".ks3-zoom-range", props={"height": "44px"}),
    dict(name="zoom gain label is accent-text mono", on=B1_PARTS,
         sel=".ks3-zoom-gain-label",
         props={"font-family": "DM Mono", "color": "#A93411"}),
    dict(name="awkward row is unmarked until opened", on=B1_PARTS,
         sel=".ks3-hardrow",
         props={"background-color": "#FFFCF5",
                "border-top-color": "#C3B191"}),
    dict(name="removal outcome lands on a LIGHT panel", on=B1_PARTS,
         sel=".ks3-removal-out",
         props={"background-color": "#FBF3E6", "color": "#221E1B"}),

    dict(name="cell-bench part row carries a numbered badge",
         on="biology/cells-and-organisation/animal-and-plant-cells.html",
         sel=".ks3-part-num",
         props={"width": "28px", "font-family": "Bricolage Grotesque",
                "font-weight": "800"}),
    dict(name="cell-bench readout name is display 800 at 25px",
         on="biology/cells-and-organisation/animal-and-plant-cells.html",
         sel=".ks3-readout-name",
         props={"font-family": "Bricolage Grotesque", "font-weight": "800",
                "font-size": "25px"}),
    dict(name="pair row is the sorter's sibling, not the sorter",
         on="biology/cells-and-organisation/animal-and-plant-cells.html",
         sel=".ks3-pairrow",
         props={"background-color": "#FFFCF5",
                "border-top-left-radius": "20px"}),
    dict(name="fit-parts installs into a responsive grid",
         on="biology/cells-and-organisation/animal-and-plant-cells.html",
         sel=".ks3-fit-parts", props={"display": "grid"}),

    dict(name="critique step is a full-width tappable row", on=B1_MICRO,
         sel=".ks3-step-btn",
         props={"min-height": "44px", "text-align": "left",
                "border-top-left-radius": "16px"}),
    # The 46px indent is 32px of badge plus the 14px gap — derived, and the one
    # value that keeps the verdict reading as belonging to its step.
    dict(name="critique verdict is indented under its badge", on=B1_MICRO,
         sel=".ks3-step-verdict", props={"margin-left": "46px"}),
    dict(name="formula triangle is drawn, not typed", on=B1_MICRO,
         sel=".ks3-tri-svg", props={"width": "260px"}),
    dict(name="triangle cover is ink and starts invisible", on=B1_MICRO,
         sel=".ks3-tri-cover", props={"opacity": "0"}),
    dict(name="FIFA field is a real text input at tap size", on=B1_MICRO,
         sel=".ks3-fifa-input",
         props={"min-height": "44px", "border-top-width": "2px",
                "background-color": "#FFFCF5"}),
    dict(name="model line is mono, so it reads as working", on=B1_MICRO,
         sel=".ks3-model-line",
         props={"font-family": "DM Mono", "font-size": "17px"}),

    # The hook's media column and its Motion control — Mide's named complaint.
    dict(name="hook art sits on its own night ground", on=B1_LIFE,
         sel=".ks3-hook-art",
         props={"height": "226px", "background-color": "#17130F"}),
    dict(name="Motion control clears the 44px tap target", on=B1_LIFE,
         sel=".ks3-motion-btn", props={"min-height": "44px"}),
    dict(name="scorecard figure is mono 32px, not a heading", on=B1_LIFE,
         sel=".ks3-scorecard-fig",
         props={"font-family": "DM Mono", "font-size": "32px"}),
    # Amber is a wrong idea being confronted — the one place it is right.
    dict(name="second confrontation is divided in amber", on=B1_UNI,
         sel=".ks3-mis-next",
         props={"border-top-color": "#D9821A", "border-top-width": "2px"}),
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
    dict(name="header trail link on page ground", on=LESSON,
         fg=".ks3-trail a", bg=".ks3-nav", need=4.5),
    dict(name="header trail current page on page ground", on=LESSON,
         fg=".ks3-trail [aria-current]", bg=".ks3-nav", need=4.5),
    dict(name="breadcrumb row link on page ground", on=UNIT,
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
    # ── MRB-198: the new kinds' surfaces, measured on their real dark
    #    ground. Cover pairs run LOCKED; control/readout pairs run in the
    #    after-unlock pass because R5 hides both until the prediction. ──
    dict(name="microscope locked cover on dark ground", on=B1_MICRO,
         fg=".ks3-practical .ks3-sim-cover",
         bg=".ks3-practical .ks3-sim-cover", need=4.5),
    dict(name="microscope caption on dark ground", on=B1_MICRO,
         fg=".ks3-practical .ks3-sim-caption", bg=".ks3-practical", need=4.5),
    dict(name="microscope control label on dark ground", on=B1_MICRO,
         fg=".ks3-practical .ks3-sim-control", bg=".ks3-practical",
         need=4.5, drive="sim-unlocked"),
    dict(name="microscope select text on its own ground", on=B1_MICRO,
         fg=".ks3-practical .ks3-sim-control select",
         bg=".ks3-practical .ks3-sim-control select", need=4.5,
         drive="sim-unlocked"),
    dict(name="microscope readout on dark ground", on=B1_MICRO,
         fg=".ks3-practical .ks3-sim-readout", bg=".ks3-practical",
         need=4.5, drive="sim-unlocked"),
    dict(name="system-parts locked cover on dark ground", on=B1_PARTS, parked=_PARKED_SYSTEM_PARTS,
         fg=".ks3-practical .ks3-sim-cover",
         bg=".ks3-practical .ks3-sim-cover", need=4.5),
    dict(name="system-parts caption on dark ground", on=B1_PARTS, parked=_PARKED_SYSTEM_PARTS,
         fg=".ks3-practical .ks3-sim-caption", bg=".ks3-practical", need=4.5),
    dict(name="system-parts control label on dark ground", on=B1_PARTS, parked=_PARKED_SYSTEM_PARTS,
         fg=".ks3-practical .ks3-sim-control", bg=".ks3-practical",
         need=4.5, drive="sim-unlocked"),
    dict(name="system-parts select text on its own ground", on=B1_PARTS, parked=_PARKED_SYSTEM_PARTS,
         fg=".ks3-practical .ks3-sim-control select",
         bg=".ks3-practical .ks3-sim-control select", need=4.5,
         drive="sim-unlocked"),
    dict(name="system-parts readout on dark ground", on=B1_PARTS, parked=_PARKED_SYSTEM_PARTS,
         fg=".ks3-practical .ks3-sim-readout", bg=".ks3-practical",
         need=4.5, drive="sim-unlocked"),
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


# ── MRB-198: canvas-drawn marks — the pairs CSS cannot measure ───────────
#
# The two new instruments paint text and state marks straight onto the
# canvas with token colours read via cssVar(). Layer D reads resolved CSS
# and cannot see canvas pixels, so these pairs are computed HERE, from the
# same tokens.css the canvas reads. `overrides` exists so the checker
# itself can be mutation-tested: feed it a broken value and it must fail.

CANVAS_PAIRS = (
    ("part name ink on a working node", "--ks3-ink", "--ks3-card", 4.5),
    ("part name ink on a stopped node", "--ks3-ink", "--ks3-option-spent", 4.5),
    ("stopped hatch + stop-mark ink on spent fill", "--ks3-ink",
     "--ks3-option-spent", 3.0),
    ("origin accent border on canvas ground", "--ks3-accent",
     "--ks3-inset", 3.0),
    ("origin accent border against a node", "--ks3-accent",
     "--ks3-card", 3.0),
    ("microscope drawn ink on the bright field", "--ks3-ink",
     "--ks3-card", 4.5),
    ("Euglena's biology green on the bright field", "--ks3-biology",
     "--ks3-card", 3.0),
)


# MRB-210 §2 — every range control is bound on BOTH `input` and `change`.
#
# This is a SOURCE check, deliberately, after a runtime one was written,
# measured and thrown away. The runtime version dragged each slider and
# compared the sim's readout before and after. It is unsound in both
# directions and both were observed:
#
#   FALSE PASS — a particle sim repaints from an animation loop, so its
#     readout ("wall hits per second: 60") drifts on its own. A drag that
#     did nothing still "changed" the text.
#   FALSE FAIL — B1-06's focus slider changes nothing at ×40, because the
#     readout short-circuits on magnification before it mentions focus. It
#     is correctly wired and only speaks from ×100 up.
#
# So readout-diffing measures animation noise and lesson content, not
# binding. An assertion whose result depends on which frame it lands in is
# not an assertion. What is deterministic is that every range in ks3.js is
# bound through the one helper that attaches both listeners.
#
# ⚠️ METHODOLOGICAL NOTE, kept where the next person will find it.
# Design's words, verbatim:
#
#   "Shrinking `.ks3-main` in a probe does not fire a `max-width` media
#    query — the viewport is still wide. Container-driven wrapping is
#    testable that way; viewport queries are not."
#
# Design's first attempt at a narrow-width fix measured as a no-op for
# exactly that reason. THIS harness overrides device metrics
# (`Emulation.setDeviceMetricsOverride` — see ks3_browser.py's header), so
# it DOES fire viewport queries correctly. Any future check that resizes an
# element instead will pass silently over a broken layout.


def check_range_binding(repo_root="."):
    """Returns (problems, rows). Static, so it cannot be flaky."""
    path = os.path.join(repo_root, "shared", "ks3.js")
    with open(path, encoding="utf-8") as fh:
        src = fh.read()
    problems, rows = [], []

    helper = re.search(r"function onRange\(el, fn\) \{(.*?)\n  \}",
                       src, re.S)
    if not helper:
        problems.append(
            "MRB-210: shared/ks3.js has no onRange() helper — the one place "
            "that binds a range on both `input` and `change`.")
        return problems, rows
    body = helper.group(1)
    for ev in ("input", "change"):
        ok = ('addEventListener("%s", fn)' % ev) in body
        rows.append(("onRange binds " + ev, "yes" if ok else "NO", ok))
        if not ok:
            problems.append(
                "MRB-210: onRange() does not attach a `%s` listener. Design's "
                "approved B1-06 binds both to the same handler." % ev)

    # No range may be bound directly — that is how one gets missed.
    #
    # Scanned forward from each `X.type = "range"` rather than by matching
    # variable names globally. ks3.js reuses the name `input` for the
    # microscope's two <select> controls, which are correctly bound on
    # `change` alone; a name-based check calls those a leak and is wrong.
    lines = src.splitlines()
    leaked = []
    for i, line in enumerate(lines):
        m = re.search(r'(\w+)\.type = "range"', line)
        if not m:
            continue
        var = m.group(1)
        window = "\n".join(lines[i:i + 40])
        if re.search(r'\b%s\.addEventListener\(' % re.escape(var), window):
            leaked.append("line %d (%s)" % (i + 1, var))
        elif not re.search(r'\bonRange\(\s*%s\b' % re.escape(var), window):
            leaked.append("line %d (%s: bound by neither)" % (i + 1, var))
    rows.append(("every range goes through onRange",
                 "clean, %d range declaration(s)"
                 % len(re.findall(r'\.type = "range"', src))
                 if not leaked else "leaked: %s" % leaked, not leaked))
    if leaked:
        problems.append(
            "MRB-210: range input(s) at %s are bound with a direct "
            "addEventListener instead of onRange(), so they get one event "
            "and not the other." % ", ".join(leaked))
    rows.append(("onRange call sites", str(len(re.findall(r"onRange\(", src)) - 1),
                 len(re.findall(r"onRange\(", src)) - 1 > 0))
    return problems, rows


def check_no_section_refs(ks3_root):
    """§8.10 — an architecture §-reference must never reach student prose.

    §8.10 is a DISCERNMENT test, not a banned-phrase list, and architecture.md
    says plainly that a blanket rule here would be the same failure as the
    callout that prompted the rule. So this checks exactly one thing, the one
    that is never a judgement call: a `§` followed by a section number, in the
    VISIBLE text of a built page. That is this project talking to itself.

    The live instance it was written for: `references[].why` renders into the
    "Connects to" endmatter card, and C1's `testing-the-model` shipped
    "P11 owns it (§7.4); this lesson points at it and must render gracefully
    before P11 exists" to students on the published draft.

    Script and style contents are stripped before the scan, then tags, so this
    measures what a reader sees rather than what the source contains — an
    authoring comment in a data module is fine, a rendered one is not.
    """
    problems, scanned = [], 0
    pat = re.compile(r"§\s*\d")
    for path in _all_pages(ks3_root):
        with open(path, encoding="utf-8") as fh:
            src = fh.read()
        scanned += 1
        src = re.sub(r"<script.*?</script>", " ", src, flags=re.S)
        src = re.sub(r"<style.*?</style>", " ", src, flags=re.S)
        text = _unescape(re.sub(r"<[^>]+>", " ", src))
        m = pat.search(text)
        if m:
            near = " ".join(
                text[max(0, m.start() - 80):m.start() + 90].split())
            rel = os.path.relpath(path, ks3_root)
            problems.append("%s — student text carries an architecture "
                            "section reference: …%s…" % (rel, near))
    return problems, scanned


def check_internal_links(ks3_root):
    """MRB-209 §4 — every internal /ks3/ link must resolve to a real page.

    Prerequisite edges and `ks4_links` were already gated. Links written in
    PROSE and in the ENDMATTER were not, and that is where the defect
    landed: B1-04's endmatter pointed at `b1-07-stem-cells-and-meristems`
    after MRB-199 removed it. Design happened to spot it. A removed slug
    should fail the build, not 404 in front of a student.

    Deliberately checks the BUILT tree rather than the lesson records,
    because that is the only place a hand-written prose link exists at all.
    """
    problems = []
    served = os.path.dirname(os.path.abspath(ks3_root))
    checked = 0
    for path in _all_pages(ks3_root):
        rel = os.path.relpath(path, ks3_root)
        with open(path, encoding="utf-8") as fh:
            html = fh.read()
        for href in set(re.findall(r'href="(/ks3/[^"#?]+)"', html)):
            checked += 1
            target = os.path.join(served, href.lstrip("/"))
            if not os.path.exists(target):
                problems.append(
                    "MRB-209: /%s links to %s, which does not exist. A "
                    "cross-lesson link to a removed slug is a 404 in front "
                    "of a student." % (rel, href))
    return problems, checked


MANIFEST = "docs/ks3/design-coverage-manifest.md"


def check_rail_anchors(ks3_root):
    """Every `data-rail-stages` anchor names an element that exists.

    The rail is emitted from the lesson record and the sections are emitted by
    the block renderers, and nothing joined the two up. `#s-hook` and
    `#s-ladder` were missing from every lesson page in the key stage — see the
    gate's own note in `verify_ks3.py` for how.

    Read out of the BUILT page rather than the record, deliberately: the record
    is what we meant, and the question is what a browser will find.
    """
    problems, total = [], 0
    for page in _lesson_pages(ks3_root):
        with open(page, encoding="utf-8") as fh:
            html = fh.read()
        name = os.path.basename(page)
        m = re.search(r'data-rail-stages="([^"]*)"', html)
        if not m:
            continue
        try:
            stages = json.loads(_unescape(m.group(1)))
        except ValueError as err:
            problems.append("%s: unparseable data-rail-stages (%s)"
                            % (name, err))
            continue
        ids = set(re.findall(r'\sid="([^"]+)"', html))
        for st in stages:
            anchor = st.get("anchor")
            if not anchor:
                problems.append("%s: a rail stop declares no anchor" % name)
                continue
            total += 1
            if anchor not in ids:
                problems.append(
                    "%s: rail stop %r points at #%s, which is on no element — "
                    "the link goes nowhere and the stop can never tick"
                    % (name, st.get("short") or anchor, anchor))
    return problems, total


def _manifest_rows(repo_root, heading):
    """Parse the markdown table under `heading` in §10 of the manifest.

    Returns [(col0, col1, ...), ...] with the header and separator dropped.
    Deliberately strict: a heading that has moved or a table that has been
    turned into prose raises rather than silently returning nothing, because
    an empty registry would make every check below vacuously pass — the
    exact defect class MRB-203 exists to close.
    """
    path = os.path.join(repo_root, MANIFEST)
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    if heading not in text:
        raise ValueError(
            "design-coverage-manifest.md has no %r heading. §10 is the "
            "authoritative registry the build reads; if it has been renamed "
            "or removed, fix the manifest rather than this parser." % heading)
    body = text.split(heading, 1)[1]
    rows = []
    for line in body.splitlines():
        line = line.strip()
        if not line.startswith("|"):
            if rows:
                break          # table ended
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if not cells or set("".join(cells)) <= set("-: "):
            continue           # separator row
        if cells[0].lower() in ("family", "block type"):
            continue           # header row
        rows.append(cells)
    if not rows:
        raise ValueError("no rows parsed under %r in %s" % (heading, MANIFEST))
    return rows


def check_design_coverage(repo_root=".", units=None):
    """MRB-203 — absence of REGISTRATION fails, not just absence of selector.

    Two questions the old gate could not ask:

      1. Is this lesson's architecture family one Design has actually drawn?
         Layer C measures registered components to ±1px, but a family with no
         reference screen registers nothing, so it had nothing to disagree
         with. B1 was the first unit to author SYSTEM and CLASSIFY — 47 of
         the 184 slots between them — and the gate reported green over
         invented shapes.

      2. Does every block type the tree actually renders map to a registered
         component that exists in COMPONENTS?

    Returns (problems, rows) where rows are (label, detail, ok) for printing.
    """
    problems, rows = [], []

    fam_rows = _manifest_rows(repo_root, "### 10.1")
    families = {}
    for cells in fam_rows:
        fam = cells[0].strip("`* ")
        screen = cells[2].strip("`* ")
        families[fam] = None if screen.strip("— ") in ("", "NONE") else screen

    # Every family a lesson is AUTHORED in must have a drawn screen.
    if units is None:
        import ks3_data
        units = ks3_data.KS3_UNITS
    authored = [(u, l) for u in units for l in u["lessons"] if l.get("authored")]
    for u, l in authored:
        fam = l.get("family")
        if fam not in families:
            problems.append(
                "MRB-203: %s/%s is authored in family %s, which has NO ROW in "
                "%s §10.1. A family with no reference screen has no registered "
                "component, so the parity gate cannot see anything wrong with "
                "it. Get the screen drawn — do not add the row to pass the "
                "build." % (u["code"], l["slug"], fam, MANIFEST))
            continue
        screen = families[fam]
        if not screen:
            problems.append(
                "MRB-203: %s/%s is authored in family %s, which §10.1 records "
                "as NOT DRAWN. Design has not supplied a reference screen for "
                "this family." % (u["code"], l["slug"], fam))
            continue
        if not os.path.exists(os.path.join(repo_root, screen)):
            problems.append(
                "MRB-203: family %s points at reference screen %r, which does "
                "not exist. A registry row that names a missing file is worse "
                "than no row — it reports coverage that is not there."
                % (fam, screen))
    for fam, screen in sorted(families.items()):
        used = sorted({l.get("family") for _u, l in authored})
        rows.append(("family " + fam,
                     (screen or "NOT DRAWN") + (" · authored" if fam in used
                                                else " · none authored yet"),
                     fam not in used or bool(screen)))

    # Every RENDERED block type must map to components that really exist.
    blk_rows = _manifest_rows(repo_root, "### 10.2")
    registered = {c["name"] for c in COMPONENTS}
    mapping = {}
    for cells in blk_rows:
        btype = cells[0].strip("`* ")
        # Component names contain commas ("hook is ink-dark, accent shadow"),
        # so the cell is parsed as backtick-delimited spans, never split on
        # the comma. Splitting on commas turned one component into two
        # non-existent ones and failed three real rows.
        names = re.findall(r"`([^`]+)`", cells[1])
        mapping[btype] = names

    rendered = set()
    for _u, l in authored:
        for b in (l.get("core") or []):
            if b.get("type"):
                rendered.add(b["type"])
    for btype in sorted(rendered):
        names = mapping.get(btype)
        if not names:
            problems.append(
                "MRB-203: block type %r is rendered in the built tree but has "
                "NO ROW in %s §10.2 — it is drawn on screen with no registered "
                "component gating it." % (btype, MANIFEST))
            rows.append(("block " + btype, "NO ROW", False))
            continue
        missing = [n for n in names if n not in registered]
        if missing:
            problems.append(
                "MRB-203: block type %r maps to component(s) %s, which are not "
                "defined in ks3_parity.COMPONENTS. The registry claims cover "
                "that does not exist." % (btype, missing))
        rows.append(("block " + btype,
                     "%d component(s): %s" % (len(names), ", ".join(names[:3])
                                              + ("…" if len(names) > 3 else "")),
                     not missing))
    return problems, rows


def check_canvas_contrast(repo_root=".", overrides=None):
    """Returns (problems, rows). rows = (name, ratio, need, ok)."""
    tokens = ks3_token_colours(repo_root)
    if overrides:
        tokens = dict(tokens, **overrides)
    problems, rows = [], []
    for name, fg, bg, need in CANVAS_PAIRS:
        f = parse_rgb(tokens.get(fg, ""))
        g = parse_rgb(tokens.get(bg, ""))
        if f is None or g is None:
            problems.append("canvas pair %r: token %s or %s missing from "
                            "tokens.css" % (name, fg, bg))
            continue
        ratio = contrast(f, g)
        ok = ratio >= need - 0.005
        rows.append((name, ratio, need, ok))
        if not ok:
            problems.append(
                "CANVAS CONTRAST FAIL: %s — %.2f:1 against %.1f:1 required "
                "(%s on %s)" % (name, ratio, need, fg, bg))
    return (problems, rows)


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


# ⚠️ A 1px tolerance is for LAYOUT, and it is wrong for a hairline.
#
# `TOL_PX = 1.0` exists because a measured width or height lands a fraction off
# after rounding, and failing a build over 0.4px would make the gate useless.
# Applied to a BORDER, it makes 2px and 3px indistinguishable — and 2px against
# 3px is exactly what separates `.ks3-rule` from a `.ks3-block`, and
# `.ks3-ladder` from both.
#
# Found by mutation-testing the statement panel: repainting its 3px border to
# 2px changed the page and the gate did not notice, which is the definition of
# an assertion that cannot fail. Below 5px a length is a design decision, not a
# rounding artefact, so it is compared exactly.
_HAIRLINE_PX = 5.0


def close_length(got, want):
    def px(v):
        m = re.match(r'(-?[\d.]+)px$', (v or "").strip())
        return float(m.group(1)) if m else None
    a, b = px(got), px(want)
    if a is None or b is None:
        return None
    if abs(b) < _HAIRLINE_PX:
        return a == b
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
    # R5 hides a sim's control panel and readout behind a cover until the
    # student has committed a prediction, so every control, label, select and
    # readout pair can only be measured on an unlocked panel — and the cover's
    # own pairs only on a locked one. MRB-198 carried these specs as
    # `after_unlock` flags with a bespoke second pass; they are drives here
    # instead, which buys the fresh load, the settle, the console drain and the
    # "could not reach its state" failure that every other driven state gets.
    #
    # Unlocking goes through the sim's OWN activity option (Law 4) rather than
    # by stripping data-locked: the cover comes off the way a student takes it
    # off, so a regression in the unlock path fails here instead of being
    # measured around.
    "sim-unlocked": r"""
(function () {
  var sims = document.querySelectorAll('.ks3-sim[data-locked="1"]');
  if (!sims.length) { return "no locked sim on the page"; }
  for (var i = 0; i < sims.length; i++) {
    var act = sims[i].closest('[data-activity]');
    var opt = act && act.querySelector('.ks3-option');
    if (opt) { opt.click(); }
  }
  var still = document.querySelectorAll('.ks3-sim[data-locked="1"]');
  if (still.length) {
    return still.length + " sim(s) still locked after clicking their activity option";
  }
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
#
# ⚖️ SCOPE, ruled by chat-app Claude on MRB-202, 13 Aug 2026.
#
# The assertion is scoped to THE OPTION BUTTON, and to nothing else:
#
#     "R3's text is about the control... The rule protects the *moment of
#      committing*. A student looking at a row of options must not be able to
#      read the answer off the buttons. What happens **after** they commit is a
#      reveal, and every activity in the system has one — that is Law 4's whole
#      shape: commit, then find out. A reveal that states the answer is not a
#      violation; it is the mechanism. So the assertion tests one thing: no
#      `.ks3-option` carries a correctness treatment — no `data-correct`, no
#      ok/alert ground, no drawn ✓ or ✕ — outside the mastery ladder. Reveal
#      panels, answer notes and after-the-fact prose are out of scope."
#
# Two consequences for how this is written:
#
#   1. The scope is now EVERY `.ks3-option` outside `.ks3-ladder`, not the three
#      block classes it used to name. That is strictly stronger — an option in a
#      block type nobody has invented yet is covered on the day it appears,
#      which is the MRB-203 failure mode one level down.
#   2. It reads the button's OWN resolved style and never walks up to an
#      ancestor for an effective ground. b1-05's `#s-hard` marks the ROW
#      CONTAINER after the student opens the answers (`--ks3-inset`/ink for
#      right, `--ks3-alert-tint`/`--ks3-alert-border` for wrong) and leaves the
#      choice buttons untouched — measured, b1-inventory §3.4.2. That is a
#      reveal, so it passes, and it must pass without an exception list. No
#      exception list is created: "an exception list is how a rule stops being
#      a rule — the first entry is always justified and the tenth never gets
#      read."
#
# Amber note: on an ink-dark block Design's chosen option takes an `--ks3-alert`
# BORDER on the unchanged `--ks3-dark-panel` ground. That is the drawn
# chosen-state and is identical whichever option is picked, so it is choosing,
# not marking. Grounds are checked against the marking families; borders are
# only checked through the "all alike" test, which is what separates the two.
_JS_R3_RUNTIME = r"""
(function () {
  // ok family (the ladder's correct state) and the alert TINTS that would read
  // as a verdict if they ever landed on a control's ground.
  var MARKING_GROUND = ['rgb(18, 161, 80)',   /* --ks3-ok       */
                        'rgb(228, 247, 235)', /* --ks3-ok-tint  */
                        'rgb(10, 107, 54)',   /* --ks3-ok-text  */
                        'rgb(255, 243, 212)'  /* --ks3-alert-tint */];
  var out = [];
  // Every option button on the page that is not a mastery-ladder rung's.
  var all = document.querySelectorAll('.ks3-option');
  var opts = [];
  for (var k = 0; k < all.length; k++) {
    if (!all[k].closest('.ks3-ladder')) { opts.push(all[k]); }
  }
  // Group by the activity/block that owns each option, so a failure names it.
  var groups = {}, order = [];
  for (var j = 0; j < opts.length; j++) {
    var own = opts[j].closest('[data-activity]') || opts[j].closest('section') || document.body;
    var id = own.getAttribute && (own.getAttribute('data-activity') || own.id);
    id = id || ('block ' + j);
    if (!groups[id]) { groups[id] = []; order.push(id); }
    groups[id].push(opts[j]);
  }
  for (var g = 0; g < order.length; g++) {
    var id = order[g], list = groups[id], seen = [], disabled = false;
    for (var i = 0; i < list.length; i++) {
      var o = list[i];
      // (a) marking DATA never reaches an activity option.
      if (o.hasAttribute('data-correct')) {
        out.push(id + ': an activity option carries data-correct');
      }
      o.click();
      var cs = getComputedStyle(o);
      var mk = o.querySelector('.ks3-opt-mark');
      // (b) a drawn mark never appears on an activity option. The ladder draws
      //     its ✓/✕ as an <svg class="ks3-mark"> inside the badge; a typed ✓/✕
      //     in the badge text is the same claim by another route.
      if (o.querySelector('svg.ks3-mark')) {
        out.push(id + ': a drawn ✓/✕ appears on an activity option');
      }
      if (mk && /[✓✔✕✖✗✘×]/.test(mk.textContent || '')) {
        out.push(id + ': a typed ✓/✕ appears on an activity option badge');
      }
      // (c) the ground never takes a marking colour.
      var grounds = [cs.backgroundColor, mk ? getComputedStyle(mk).backgroundColor : ''];
      for (var q = 0; q < grounds.length; q++) {
        for (var m = 0; m < MARKING_GROUND.length; m++) {
          if (grounds[q] === MARKING_GROUND[m]) {
            out.push(id + ': a marking colour (' + MARKING_GROUND[m] +
                     ') is the ground of an activity option');
          }
        }
      }
      // (d) whichever option was pressed, the button looks the same. This is
      //     the assertion that separates CHOOSING from MARKING, and it is read
      //     off the button, never off an ancestor.
      seen.push([cs.backgroundColor, cs.borderTopColor,
                 mk ? getComputedStyle(mk).backgroundColor : '',
                 mk ? getComputedStyle(mk).color : ''].join(' | '));
      if (o.disabled) { disabled = true; }
    }
    var uniq = seen.filter(function (v, i, a) { return a.indexOf(v) === i; });
    if (uniq.length !== 1) {
      out.push(id + ': chosen options do not all render alike — ' +
               uniq.length + ' distinct treatments: ' + uniq.join('  //  '));
    }
    if (disabled) { out.push(id + ': an activity option was disabled'); }
  }
  return { problems: out, blocks: order.length, options: opts.length };
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


# ── MRB-198: the sim audits — behaviour, gated in a real browser ─────────
#
# Layer C proves the controls LOOK right; these prove the instruments DO
# what the lesson teaches. Each runs on a real generated page: first the
# R5 locked contract, then Law 4's unlock (an option inside the sim's own
# activity), then the mechanism itself, asserted through the WRITTEN
# readout — deliberately, because R6 makes the written readout carry the
# whole result, so if these strings are right the reduced-motion
# experience is right too. Every expected figure below is the model's,
# not a screenshot's: ×40 ↔ 4.5 mm and ×400 ↔ 0.45 mm are fov = 180/mag.

_JS_R5_CHECKS = r"""
  function r5(sim, kind, P) {
    function disp(s) {
      var el = sim.querySelector(s);
      return el ? getComputedStyle(el).display : "MISSING";
    }
    if (sim.getAttribute('data-locked') !== '1') {
      P.push(kind + ": not locked on load - the Law 4 gate did not engage");
      return;
    }
    if (disp('.ks3-sim-cover') === 'none') {
      P.push(kind + " R5: locked cover not shown");
    }
    if (disp('.ks3-sim-controls') !== 'none') {
      P.push(kind + " R5: control panel visible while locked - it must be hidden entirely");
    }
    if (disp('.ks3-sim-readout') !== 'none') {
      P.push(kind + " R5: readout visible while locked");
    }
    if (disp('.ks3-sim-caption') === 'none') {
      P.push(kind + " R5: caption hidden while locked - it holds the prediction instructions");
    }
    var filt = getComputedStyle(sim.querySelector('.ks3-sim-canvas')).filter;
    if (filt.indexOf('blur') < 0) {
      P.push(kind + " R5: canvas not blurred while locked (filter=" + filt + ")");
    }
  }
  function unlockViaOwnActivity(sim, kind, P) {
    var act = sim.closest('[data-activity]');
    var opt = act && act.querySelector('.ks3-option');
    if (!opt) {
      P.push(kind + ": no .ks3-option inside its own [data-activity] - Law 4 has nothing to gate on");
      return false;
    }
    opt.click();
    if (sim.getAttribute('data-locked') === '1') {
      P.push(kind + ": still locked after an option in its own activity was pressed");
      return false;
    }
    return true;
  }
  function controlsRendered(sim, kind, P) {
    var wanted = (sim.getAttribute('data-controls') || '').split(',');
    var built = sim.querySelectorAll('.ks3-sim-controls .ks3-sim-control');
    if (built.length !== wanted.length) {
      P.push(kind + ": " + wanted.length + " controls declared, " + built.length
             + " rendered - SIM_CONTROLS and CONTROL_LABELS have drifted apart");
    }
    var bad = 0;
    for (var i = 0; i < built.length; i++) {
      var input = built[i].querySelector('select, input');
      var forId = built[i].getAttribute('for');
      if (!input || !forId || input.id !== forId
          || !built[i].textContent.trim()) { bad++; }
    }
    if (bad) {
      P.push(kind + " R15: " + bad + " control(s) lack a real labelled input");
    }
    if (sim.querySelector('[data-correct]')) {
      P.push(kind + " R3: a data-correct mark inside the instrument");
    }
  }
"""

_JS_MICRO_AUDIT = "(function () {" + _JS_R5_CHECKS + r"""
  var P = [];
  var sim = document.querySelector('.ks3-sim[data-sim="microscope"]');
  if (!sim) { return { problems: ["no microscope sim on the page"] }; }
  r5(sim, "microscope", P);
  if (!unlockViaOwnActivity(sim, "microscope", P)) { return { problems: P }; }
  controlsRendered(sim, "microscope", P);

  // ⚠️ FIND CONTROLS BY NAME, NEVER BY POSITION.
  //
  // This used to read `sels[0]` as the specimen selector and `sels[1]` as the
  // magnification one. That held only while every microscope declared both.
  // Design's approved B1-02 draws TWO controls over ONE slide — magnification
  // and focus, no specimen selector, because there is nothing to select — so
  // positional indexing read the magnification select as the specimen select
  // and reported two failures on a correct page. A gate that assumes a control
  // layout fails the first lesson that legitimately has a different one.
  var declared = (sim.getAttribute('data-controls') || '').split(',');
  function controlNamed(name) {
    var wraps = sim.querySelectorAll('.ks3-sim-control');
    for (var i = 0; i < wraps.length; i++) {
      if (wraps[i].getAttribute('data-control') === name) { return wraps[i]; }
    }
    // Fall back to declaration order among the controls that render a select.
    var idx = declared.indexOf(name);
    var sels = sim.querySelectorAll('.ks3-sim-controls select');
    return idx >= 0 && sels[idx] ? sels[idx].closest('.ks3-sim-control') : null;
  }
  function selectIn(name) {
    var w = controlNamed(name);
    return w ? w.querySelector('select') : null;
  }
  var hasSpecimen = declared.indexOf('specimen') >= 0;
  var specSel = hasSpecimen ? selectIn('specimen') : null;
  var magSel = selectIn('magnification');
  var focusInput = sim.querySelector('.ks3-sim-controls input[type="range"]');
  var readout = sim.querySelector('.ks3-sim-readout');
  var specimens = [];
  try { specimens = JSON.parse(sim.getAttribute('data-specimens') || '[]'); }
  catch (e) {}
  // A lesson with one slide draws no selector, and that is correct. What is
  // never correct is DECLARING the control and not rendering it.
  if (hasSpecimen && (!specSel || specSel.options.length !== specimens.length)) {
    P.push("microscope: specimen select offers "
           + (specSel ? specSel.options.length : 0) + " slides, payload has "
           + specimens.length);
  }
  if (!hasSpecimen && specimens.length > 1) {
    P.push("microscope: " + specimens.length + " slides in the payload but no "
           + "specimen control declared — the student cannot reach them");
  }
  // The objective control may be a select or a segmented group (B1-06).
  if (!magSel) {
    var segs = sim.querySelectorAll('.ks3-sim-seg-btn');
    if (segs.length !== 3) {
      P.push("microscope: magnification must offer the three objectives");
    }
  } else if (magSel.options.length !== 3) {
    P.push("microscope: magnification select must offer the three objectives");
  }
  if (!focusInput) { P.push("microscope: no focus wheel rendered"); }

  var r40 = readout.textContent;
  if (r40.indexOf('×40') < 0 || r40.indexOf('4.5 mm') < 0) {
    P.push("microscope model: at the lowest lens the readout must carry ×40 "
           + "and a 4.5 mm field of view - got: " + r40.slice(0, 90));
  }
  if (magSel && focusInput) {
    magSel.value = '2';
    magSel.dispatchEvent(new Event('change'));
    var r400 = readout.textContent;
    if (r400.indexOf('×400') < 0 || r400.indexOf('0.45 mm') < 0) {
      P.push("microscope model (b): at ×400 the field of view must read "
             + "0.45 mm - one model drives every reading. got: "
             + r400.slice(0, 90));
    }
    if (!/focus/i.test(r400) || /packed in rows/.test(r400)) {
      P.push("microscope model (c): stepping ×40 to ×400 must throw the "
             + "image out of focus until corrected - got: " + r400.slice(0, 120));
    }
    // "Correcting the focus at ×400 brings a layer back" is asserted as the
    // PROPERTY — that some correction exists — by sweeping the wheel, rather
    // than by driving one hardcoded position. It used to be `value = '8'`,
    // which worked only because 8 plus the 22-unit parfocal shift landed
    // exactly on the one onion layer's depth of 30 in the old slider-unit
    // model. MRB-210 moved the model to millimetres and the onion to three
    // layers, so that constant silently stopped meaning anything and the
    // audit failed against a correct engine. A gate that encodes a magic
    // number derived from engine constants breaks whenever those constants
    // are ruled on; a gate that sweeps for the behaviour does not.
    var found = -1, sample = '';
    for (var fw = 0; fw <= 100; fw++) {
      focusInput.value = String(fw);
      focusInput.dispatchEvent(new Event('input'));
      var rw = readout.textContent;
      if (/onion cell/.test(rw) && !/nowhere near|nothing sharp/.test(rw)) {
        found = fw; sample = rw.slice(0, 120); break;
      }
    }
    if (found < 0) {
      P.push("microscope model: at ×400 NO position of the focus wheel brings "
             + "an onion layer sharp - the highest lens is unusable, which is "
             + "not what the lesson teaches. last readout: "
             + readout.textContent.slice(0, 120));
    }
  }
  return { problems: P };
})()"""

_JS_PARTS_AUDIT = "(function () {" + _JS_R5_CHECKS + r"""
  var P = [];
  var sim = document.querySelector('.ks3-sim[data-sim="system-parts"]');
  if (!sim) { return { problems: ["no system-parts sim on the page"] }; }
  r5(sim, "system-parts", P);
  if (!unlockViaOwnActivity(sim, "system-parts", P)) { return { problems: P }; }
  controlsRendered(sim, "system-parts", P);

  var parts = [];
  try { parts = JSON.parse(sim.getAttribute('data-parts') || '[]'); }
  catch (e) {}
  var sel = sim.querySelector('.ks3-sim-controls select');
  var readout = sim.querySelector('.ks3-sim-readout');
  if (!sel || sel.options.length !== parts.length + 1) {
    P.push("system-parts: the selector must offer every part plus "
           + "'every part on' - " + (sel ? sel.options.length : 0)
           + " options for " + parts.length + " parts");
    return { problems: P };
  }

  // The cascade is DERIVED: kill the muscle tissue and the failure must
  // climb the levels, in order, all the way to the organism - and the
  // glandular side must be reported still working.
  sel.value = 'muscle-tissue';
  sel.dispatchEvent(new Event('change'));
  var r = readout.textContent;
  if (!(/Stopped, in the order/.test(r) && /Stomach/.test(r)
        && /Digestive system/.test(r) && /organism/i.test(r))) {
    P.push("system-parts cascade: switching off the muscle tissue must stop "
           + "the stomach, the digestive system and the organism in order - "
           + "got: " + r.slice(0, 160));
  }
  if (!/Still working/.test(r) || !/Gland/i.test(r)) {
    P.push("system-parts cascade: the readout must also carry what still "
           + "works - got: " + r.slice(0, 160));
  }

  // The scale rule: one cell out of thousands is absorbed, never cascaded.
  sel.value = 'muscle-cell';
  sel.dispatchEvent(new Event('change'));
  var r2 = readout.textContent;
  if (/Stopped, in the order/.test(r2) || !/cover for it/.test(r2)) {
    P.push("system-parts scale rule: switching off ONE muscle cell must be "
           + "absorbed by the tissue (one_of_many), not cascaded - got: "
           + r2.slice(0, 160));
  }
  return { problems: P };
})()"""

SIM_AUDITS = {
    B1_MICRO: ("microscope", _JS_MICRO_AUDIT),
    # `system-parts` is PARKED, not deleted — see `_PARKED_SYSTEM_PARTS`. No
    # lesson renders the kind since Design's approved B1-05 replaced it with
    # `removal-cases`, so the audit has nothing to drive and would report "no
    # system-parts sim on the page" on every run. `_JS_PARTS_AUDIT` stays in
    # this file, with its cascade and scale-rule assertions intact, and this
    # row goes back the day a lesson uses the kind again.
}


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
            if spec.get("parked"):
                style_rows.append((spec["name"], "—", "PARKED",
                                   spec["parked"], True))
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
                # ⚠️ A LENGTH IS ONE TOKEN. `box-shadow: rgb(228, 87, 46) 5px
                # 5px 0px 0px` ends in "px" and is not a length — routing it to
                # `close_length` made an assertion fail while printing an
                # expected and a resolved value that were CHARACTER-IDENTICAL,
                # which is the most confusing failure a gate can produce. Found
                # registering the KEY FACT box's accent shadow, which is the one
                # property that distinguishes it from every other card.
                elif want.endswith("px") and " " not in want.strip():
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
            if spec.get("parked"):
                contrast_rows.append(("%s [PARKED]" % spec["name"],
                                      None, None, None, spec.get("need"), True))
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

                # ── MRB-198: the sim audits — behaviour, not appearance ──
                # An instrument's physics is not measurable as computed style,
                # so each kind carries a behavioural audit that asserts the R5
                # cover, unlocks through the sim's own activity, then drives the
                # mechanism and reads what it says. Its own fresh load, because
                # it clicks and it changes the readout.
                if rel in SIM_AUDITS:
                    audit_kind, audit_js = SIM_AUDITS[rel]
                    page = fresh(b, url, rel)
                    if page is not None:
                        got = page.eval(audit_js)
                        audit_problems = (got or {}).get("problems") or []
                        for ap in audit_problems:
                            problems.append("SIM AUDIT (/%s): %s" % (rel, ap))
                        drain_console(page, rel,
                                      " during the %s sim audit" % audit_kind)
                        style_rows.append(
                            ("sim audit · " + audit_kind,
                             "behavioural assertions", "0 problems",
                             "%d problem(s)" % len(audit_problems),
                             not audit_problems))
    finally:
        server.shutdown()

    return (problems, style_rows, contrast_rows)
