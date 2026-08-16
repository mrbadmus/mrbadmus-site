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

# ⊕ B2 · Movement (MRB-220). Same rule as B1's: a component is registered on
# the page that RENDERS it. `job-sort` is on three pages and is measured on
# b2-01, whose sorter carries the shared category set and the widest payload;
# the two canvas benches are each measured on their own page, because neither
# renders anywhere else.
B2_SKEL = "biology/movement-skeleton-and-muscles/what-the-skeleton-does.html"
B2_JOINTS = "biology/movement-skeleton-and-muscles/joints.html"
B2_MUSCLE = "biology/movement-skeleton-and-muscles/antagonistic-muscle-pairs.html"

# ⊕ C2 · Atoms, elements and compounds (MRB-220). Same rule again: a component
# is registered on the page that RENDERS it. `verdict-cards` appears on two
# pages and is measured on c2-04, whose instance carries the mono-formula
# headline and the four-option row — the wider of the two shapes, so the
# narrower one cannot pass on a rule the wide one would fail.
C2_ATOM = "chemistry/atoms-elements-and-compounds/the-atom-daltons-model.html"
C2_ELEM = "chemistry/atoms-elements-and-compounds/elements.html"
C2_COMP = "chemistry/atoms-elements-and-compounds/compounds.html"
C2_SYM = "chemistry/atoms-elements-and-compounds/chemical-symbols.html"
C2_FORM = "chemistry/atoms-elements-and-compounds/formulae.html"
C2_MASS = "chemistry/atoms-elements-and-compounds/conservation-of-mass.html"

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

# ⊕ MRB-228, 16 Aug 2026 — the same case, found by the same gate, on the C1
# rebuild. `LESSON` (c1-04 gas-pressure) was the reference page for the whole
# generic block vocabulary, because the superseded C1 rendered nearly all of
# it on one page. Design's rebuilt c1-04 renders none of these: no `figures`,
# no vocabulary cards, no `sim` — its instruments are `collision-counter` and
# `prediction-stack`, which draw their own canvases and their own controls.
#
# Everything that still exists SOMEWHERE was repointed rather than parked, and
# the coverage is unchanged. Two components exist nowhere in the key stage:
#
#   `.ks3-figure*`   — no authored lesson carries a non-empty `figures` list
#                      any more. This one matters and is not merely
#                      bookkeeping: B4 and B5 name twelve diagram slots between
#                      them, so the first of those units to land un-parks it.
#   `.ks3-sim-figure` — the generic sim's live readout. B1's microscope draws
#                      its readout inside its own `.ks3-micro-*` tree.
_PARKED_NO_FIGURE = (
    "no lesson in the key stage renders a `figure` block — the C1 rebuild's "
    "six lessons carry `figures: []` and draw everything on canvas. Un-park "
    "with the first delivered unit that names a diagram slot (B4 and B5 both "
    "do).")
_PARKED_NO_SIM_FIGURE = (
    "no lesson renders a generic `.ks3-sim` live figure — B1's microscope, "
    "the only surviving sim, draws its readout in its own class tree. Engine "
    "and audit kept; un-park when a lesson uses the generic sim again.")

# The sim's LIGHT-GROUND and MISCONCEPTION variants, as opposed to the sim
# itself. Both surviving sims in the key stage (b1-02's microscope, b1-06's)
# sit on `ks3-block ks3-dark ks3-practical`, so the ink-dark rows below are
# measured and these two are not. Repointing them at b1-02 was the first thing
# tried and it is wrong twice over: the canvas takes `--ks3-on-dark-rule` there
# rather than ink, and a caption measured against `.ks3-check` resolves 1.88:1
# because it is not on a check block at all. A row that has to be told which
# ground to imagine is not measuring a ground.
_PARKED_NO_LIGHT_SIM = (
    "no lesson renders a sim on a light or amber ground — both surviving sims "
    "are on ink-dark practical shells, and those variants ARE measured. "
    "Un-park when a lesson puts a sim on a check or misconception block.")
UNIT = "chemistry/particles-and-their-behaviour/index.html"
# C1 is fully authored, so its index carries no Coming soon badge; and B3 is
# the ONLY unit in the key stage with a §4.6 reference slot, so it is the only
# page where the pointer can be measured at all.
# UNIT_SOON moved off B1 when MRB-198 landed Design's B1 content — a fully
# authored unit has no coming-soon rows to measure. It moved off B2 on
# 16 Aug 2026 (MRB-228) for exactly the same reason, the moment b2-04 made B2
# four of four.
#
# ⊕ Chosen to STOP MOVING. B1 → B2 in a week is a reference page that has to be
# repointed every time a unit completes, and each repoint is a chance to point
# it somewhere that quietly has nothing to measure. C3 has no delivered content
# anywhere in the repo and is in no queued ticket's scope — not this run's
# B3–B7, not MRB-223's P1–P3 — so it will still have coming-soon rows long
# after the biology units are done.
UNIT_SOON = "chemistry/mixtures-and-separation/index.html"
UNIT_REF = "biology/nutrition-and-digestion/index.html"
# ⊖ PARKED 16 Aug 2026 (MRB-228). B3's `energy-in-food` slot was the LAST §4.6
# reference slot in the key stage — a slot that generates no page of its own
# and renders in the unit index as a cross-link to its owner. MRB-232 split
# `KS3.B.NUT.02` and made it an owned B3 lesson, so the cross-reference row and
# its badge now render on no page anywhere.
#
# The machinery is sound and the day a unit declares a reference slot again it
# should be measured, so the rows are parked rather than deleted — same
# reasoning as `_PARKED_SYSTEM_PARTS`. `UNIT_REF` is kept pointing at B3
# because that is where the component last lived and where the diff will be
# read from; the constant is not what makes the rows skip.
_PARKED_NO_REF_SLOT = (
    "no unit declares a §4.6 reference slot — B3's was the last, and MRB-232 "
    "made it an owned lesson. Un-park when a unit declares one again "
    "(a fourth element on a lesson tuple in ks3_data/structure.py).")
LANDING = "index.html"
YEAR = "year-7/index.html"

# ═══ BEGIN C1 ═══
C1_PRESSURE = "chemistry/particles-and-their-behaviour/gas-pressure.html"
C1_TEST = "chemistry/particles-and-their-behaviour/testing-the-model.html"
C1_MODEL = "chemistry/particles-and-their-behaviour/particle-model.html"
C1_STATE = "chemistry/particles-and-their-behaviour/changes-of-state.html"
C1_DIFF = "chemistry/particles-and-their-behaviour/diffusion.html"
C1_STATES = "chemistry/particles-and-their-behaviour/solids-liquids-and-gases.html"
# ═══ END C1 ═══





# ═══ BEGIN B2 ═══
B2_BIO = "biology/movement-skeleton-and-muscles/biomechanics-forces-in-the-body.html"
# ═══ END B2 ═══

# ═══ BEGIN B3 ═══
B3_DIET = "biology/nutrition-and-digestion/a-balanced-diet.html"
B3_WRONG = "biology/nutrition-and-digestion/when-diet-goes-wrong.html"
B3_ENZ = "biology/nutrition-and-digestion/enzymes-in-digestion.html"
B3_VILLUS = "biology/nutrition-and-digestion/absorption-and-the-small-intestine.html"
B3_GUT = "biology/nutrition-and-digestion/the-digestive-system.html"
B3_BACTERIA = "biology/nutrition-and-digestion/bacteria-in-the-gut.html"
B3_ENERGY = "biology/nutrition-and-digestion/energy-in-food-and-what-you-need.html"
B3_TESTS = "biology/nutrition-and-digestion/food-tests.html"
# ═══ END B3 ═══

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
    dict(name="figure frame", on=LESSON, parked=_PARKED_NO_FIGURE,
         sel=".ks3-figure",
         props={"margin-top": "28px"}),
    dict(name="figure caption", on=LESSON, parked=_PARKED_NO_FIGURE,
         sel=".ks3-figure figcaption",
         props={"font-size": "17px", "color": "#3B342E",
                "margin-top": "12px"}),
    dict(name="figure pending slot", on=LESSON, parked=_PARKED_NO_FIGURE,
         sel=".ks3-figure-slot",
         props={"border-top-width": "3px", "border-top-style": "dashed",
                "border-top-color": "#C3B191"}),

    # ── R4: the dog-ear card ──
    # ⊕ MRB-228 — repointed off the rebuilt c1-04, which authors no vocabulary
    # cards. c2-05 is the only page left in the key stage that renders them.
    dict(name="vocabulary card", on=C2_FORM, sel=".ks3-card-btn",
         props={"background-color": "#FFFCF5", "border-top-left-radius": "22px",
                "min-height": "150px"}),
    dict(name="card term type", on=C2_FORM, sel=".ks3-card-front",
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
    # ⊕ MRB-228 — this is the sim canvas on a LIGHT ground, and the rebuilt
    # c1-04 was the only page that had one. The dark-shell canvas is measured
    # a few rows below as "microscope canvas (dark practical shell)", which is
    # the same component with the ground it actually renders on.
    dict(name="sim canvas", on=LESSON, parked=_PARKED_NO_LIGHT_SIM,
         sel=".ks3-sim-canvas",
         props={"background-color": "#F7EFE1", "border-top-color": "#221E1B",
                "border-top-left-radius": "20px"}),
    dict(name="sim live figure is mono", on=LESSON,
         parked=_PARKED_NO_SIM_FIGURE, sel=".ks3-sim-figure",
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

    # ══ B2 · Movement (⊕ MRB-220) ═══════════════════════════════════════
    #
    # Every row below pins the property that makes its component DISTINCT,
    # never the properties it shares with everything else. Each was
    # mutation-tested: the CSS rule was deliberately broken and the row
    # confirmed to fail before being kept.

    # ── the block head row ──
    # The counter is the only element in the key stage that sits on the same
    # baseline as an <h2>. If the flex row ever collapses it drops under the
    # heading and reads as a caption on the lede instead.
    dict(name="block head puts the counter on the heading's row", on=B2_SKEL,
         sel=".ks3-blockhead",
         props={"display": "flex", "justify-content": "space-between",
                "align-items": "flex-end", "flex-wrap": "wrap"}),
    dict(name="block head counter is mono ink-muted", on=B2_SKEL,
         sel=".ks3-blockhead-count",
         props={"font-family": "DM Mono", "font-size": "15px",
                "color": "#5F564F"}),

    # ── job-sort ──
    # The row is a CARD ON THE OPTION BORDER and goes to INK when decided.
    # That border is the only mark the sorter makes, and it marks the row
    # rather than the button — which is what keeps a per-item reveal clear of
    # R3. If it ever lands on the button, the block becomes a test.
    dict(name="sorter row is a card on the option border", on=B2_SKEL,
         sel=".ks3-jobsort-item",
         props={"background-color": "#FFFCF5", "border-top-color": "#DDCFB6",
                "border-top-width": "2px", "border-top-left-radius": "20px"}),
    dict(name="sorter row goes to INK once decided", on=B2_SKEL,
         drive="jobsort-decided", sel='.ks3-jobsort-item[data-open="1"]',
         props={"border-top-color": "#221E1B", "border-top-width": "2px"}),
    dict(name="sorter option clears the 44px tap target", on=B2_SKEL,
         sel=".ks3-jobsort-opt",
         props={"min-height": "44px", "font-size": "16px",
                "background-color": "#FBF3E6", "border-top-color": "#DDCFB6"}),
    # R3: the CHOSEN option takes the ordinary chosen treatment and nothing
    # else — no green, no tick, no verdict.
    dict(name="sorter CHOSEN option is accent-tint, never a verdict",
         on=B2_SKEL, drive="jobsort-decided",
         sel='.ks3-jobsort-opt[aria-pressed="true"]',
         props={"background-color": "#FCE7DE", "border-top-color": "#E4572E"}),
    dict(name="sorter SPENT option dims rather than disappearing",
         on=B2_SKEL, drive="jobsort-decided",
         sel='.ks3-jobsort-opt[disabled][aria-pressed="false"]',
         props={"opacity": "0.5"}),
    dict(name="sorter answer word is display type", on=B2_SKEL,
         sel=".ks3-jobsort-answer", props={"font-family": "Bricolage Grotesque"}),

    # ── system-switch ──
    # The chain panel is INK-DARK inside a LIGHT block. That inversion is the
    # measured difference from `sabotage`, whose whole shell is dark, and it
    # is why the two are not one component.
    dict(name="switch chain is ink-dark inside a light block", on=B2_SKEL,
         sel=".ks3-switch-chain",
         props={"background-color": "#221E1B", "color": "#FBF3E6",
                "border-top-left-radius": "20px"}),
    dict(name="switch chain title is mono ALERT on ink", on=B2_SKEL,
         sel=".ks3-switch-title",
         props={"font-family": "DM Mono", "color": "#FFC53D",
                "text-transform": "uppercase"}),
    # 104px + 16px, and the chip column is what makes the levels scannable
    # down the left edge rather than read as a prefix to the sentence.
    dict(name="switch chain row is a two-column grid", on=B2_SKEL,
         sel=".ks3-switch-row",
         props={"display": "grid", "column-gap": "16px"}),
    # Colour is a function of the LEVEL STRING, never of position — the
    # chains do not all climb, so a chip keyed on index would be a claim
    # about direction the data does not make.
    dict(name="switch level chip goes ALERT at the cell", on=B2_SKEL,
         sel='.ks3-switch-chip[data-level="cell"]', props={"color": "#FFC53D"}),
    dict(name="switch level chip is muted above the cell", on=B2_SKEL,
         sel='.ks3-switch-chip[data-level="tissue"]', props={"color": "#C6B9A7"}),
    dict(name="switch all-done band is the band ground on ink", on=B2_SKEL,
         drive="switch-thrown", sel=".ks3-switch-all",
         props={"background-color": "#F4E9D8", "border-top-color": "#221E1B",
                "border-top-width": "2px"}),

    # ── the two-paragraph reveal ──
    # A CARD panel on a 2px ink border, not `.ks3-reveal`'s accent tint. The
    # distinction is load-bearing: the hook's reveal on the same page IS the
    # tinted one, so if these ever resolve the same the two stop being
    # distinguishable.
    dict(name="two-paragraph reveal is a card on ink, not accent tint",
         on=B2_SKEL, drive="think-committed", sel=".ks3-reveal-panel",
         props={"background-color": "#FFFCF5", "border-top-color": "#221E1B",
                "border-top-width": "2px"}),

    # ── the range control (b2-02) ──
    # 28px of thumb on a 10px track: the whole control is a 44px tap target,
    # and there was NO KS3 rule for `input[type=range]` before this — the
    # slider would have rendered as browser default on two pages.
    dict(name="joint slider clears the 44px tap target", on=B2_JOINTS,
         drive="bench-gate-opened", sel=".ks3-slider",
         # ⚠️ NO `width` here. The slider is `width: 100%` of a column whose
         # px value is a function of the viewport, and this harness pins none —
         # asserting a number would fail on a correct page at any other window
         # size. The 28px height and the reset appearance are viewport-free and
         # are what make it a real control rather than a browser default.
         props={"height": "28px", "appearance": "none"}),

    # ── joint-bench ──
    dict(name="bench readout tile is a dark panel", on=B2_JOINTS,
         drive="bench-gate-opened", sel=".ks3-joint-tile",
         props={"background-color": "#3E3730",
                "border-top-left-radius": "20px"}),
    dict(name="bench axes readout is mono 27px alert", on=B2_JOINTS,
         drive="bench-gate-opened", sel=".ks3-joint-tile-mono",
         props={"font-family": "DM Mono", "font-size": "27px",
                "color": "#FFC53D"}),
    # The verdict lands on a LIGHT panel inside the ink-dark block — the same
    # move `removal-cases` makes, and for the same reason: the sentence a
    # student takes away must not read as one more dark readout.
    dict(name="bench verdict lands on a LIGHT panel", on=B2_JOINTS,
         drive="bench-gate-opened", sel=".ks3-joint-trade",
         props={"background-color": "#FBF3E6", "color": "#221E1B"}),
    dict(name="bench canvas frame is a 2px muted rule", on=B2_JOINTS,
         drive="bench-gate-opened", sel=".ks3-joint-stage",
         props={"border-top-color": "#C6B9A7", "border-top-width": "2px",
                "border-top-left-radius": "22px"}),

    # ── muscle-pair ──
    # Two control GROUPS in one instrument, each with its own mono caption.
    # No shipped instrument has this topology, and the captions are the only
    # thing telling a student that the second group is not more of the first.
    dict(name="muscle control group carries a mono caption", on=B2_MUSCLE,
         drive="bench-gate-opened", sel=".ks3-muscle-grouplabel",
         props={"font-family": "DM Mono", "font-size": "14px",
                "color": "#C6B9A7", "text-transform": "uppercase"}),
    dict(name="muscle status line is on-dark 700", on=B2_MUSCLE,
         drive="bench-gate-opened", sel=".ks3-muscle-status",
         props={"color": "#FBF3E6", "font-weight": "700",
                "font-size": "19px"}),

    # ══ C2 · Atoms, elements and compounds (⊕ MRB-220) ═══════════════════
    #
    # Same rule as B2's: each row pins the property that makes its component
    # DISTINCT, and each was mutation-tested — the CSS rule was deliberately
    # broken and the row confirmed to fail before it was kept.

    # ── the dark-canvas frame (map N12) ──
    # One wrapper, four instruments. Registered on c2-01 because it is the
    # first page that renders it; if it ever loses the 2px muted rule, all
    # four canvases go edge-to-edge on the ink and stop reading as instruments.
    dict(name="canvas frame is a 2px muted rule on a card radius", on=C2_ATOM,
         sel=".ks3-canvas-frame",
         props={"border-top-color": "#C6B9A7", "border-top-width": "2px",
                "border-top-left-radius": "22px", "overflow-x": "hidden"}),
    dict(name="canvas foot is a dark panel under the drawing", on=C2_ATOM,
         sel=".ks3-canvas-foot",
         props={"background-color": "#3E3730", "border-top-color": "#C6B9A7"}),

    # ── claim-switch (c2-01 #s-model) ──
    # ⚠️ A LIGHT block. The claim's ground is `--ks3-card` on a 2px INK border,
    # which is what a light block gives it; if this row ever reports
    # `#221E1B` the instrument has been mapped to `practical` and the whole
    # thing is painted on ink — the exact trap the payload map names.
    dict(name="claim toggle is a card on ink, 44px tall", on=C2_ATOM,
         drive="bench-gate-opened", sel=".ks3-claim",
         props={"background-color": "#FFFCF5", "border-top-color": "#221E1B",
                "min-height": "44px", "font-size": "18px"}),
    dict(name="claim SWITCHED OFF dims to the row-dim ground", on=C2_ATOM,
         drive="claim-off", sel='.ks3-claim[aria-pressed="false"]',
         props={"background-color": "#FBF6EC", "border-top-color": "#E0D2B9",
                "color": "#6E655D"}),
    # The chip is a READOUT, not decoration: "OFF" in words is what makes the
    # state legible without relying on the ground going dim.
    dict(name="claim state chip is mono ink-on-cream", on=C2_ATOM,
         drive="bench-gate-opened", sel=".ks3-claim-chip",
         props={"font-family": "DM Mono", "font-size": "13px",
                "background-color": "#221E1B", "color": "#FBF3E6"}),
    dict(name="claim chip INVERTS when the claim is off", on=C2_ATOM,
         drive="claim-off", sel='.ks3-claim[aria-pressed="false"] .ks3-claim-chip',
         props={"background-color": "#F4E9D8", "color": "#5F564F"}),
    dict(name="observation row is a two-column grid on the option border",
         on=C2_ATOM, drive="bench-gate-opened", sel=".ks3-obs-row",
         props={"display": "grid", "background-color": "#FFFCF5",
                "border-top-color": "#DDCFB6", "border-top-width": "2px"}),
    # ⚖️ THE TEACHING. An observation that stops being explained takes the
    # BAND ground on a 2px ink border — the KEY FACT treatment, deliberately
    # not a red and not a dim. It is not an error the student made.
    dict(name="a broken observation is BAND on ink, never a red", on=C2_ATOM,
         drive="claim-off", sel='.ks3-obs-row[data-dead="1"]',
         props={"background-color": "#F4E9D8", "border-top-color": "#221E1B",
                "border-top-width": "2px"}),
    dict(name="a broken observation's verdict is accent-TEXT", on=C2_ATOM,
         drive="claim-off",
         sel='.ks3-obs-row[data-dead="1"] .ks3-obs-verdict',
         props={"color": "#A93411", "font-family": "DM Mono",
                "font-size": "14px", "text-transform": "uppercase"}),
    dict(name="model note is a band panel on ink", on=C2_ATOM,
         drive="bench-gate-opened", sel=".ks3-claim-note",
         props={"background-color": "#F4E9D8", "border-top-color": "#221E1B",
                "border-top-width": "2px", "font-size": "19px"}),

    # ── scale-zoom (c2-01 #s-scale) ──
    # Both rows exist to prove the SPECIFICITY fix. `.ks3-dark p` is (0,1,1)
    # and a bare `.ks3-scale-note` is (0,1,0): unscoped, the note would lose
    # and render in on-dark body copy — the defect B1 shipped with the zoom
    # instrument and B2 was bitten by again.
    dict(name="zoom scale readout is mono 17px ALERT on ink", on=C2_ATOM,
         sel=".ks3-scale-readout",
         props={"font-family": "DM Mono", "font-size": "17px",
                "color": "#FFC53D"}),
    dict(name="zoom note is on-dark body, not the block's own colour",
         on=C2_ATOM, sel=".ks3-scale-note",
         props={"color": "#E7DECE", "font-size": "19px"}),

    # ── test-budget-bench (c2-02 #s-bench) ──
    # ⚖️ The budget line is the ONE counter in the key stage painted in
    # accent-text rather than ink-muted, because it is a resource running down
    # rather than a tally going up. If it ever resolves to #5F564F the budget
    # stops reading as a cost and the lesson's pressure goes with it.
    dict(name="budget line is the accent-text counter", on=C2_ELEM,
         sel='.ks3-blockhead-count[data-tone="accent"]',
         props={"color": "#A93411", "font-family": "DM Mono",
                "font-size": "15px"}),
    dict(name="sample panel is inset on a 2px ink border", on=C2_ELEM,
         sel=".ks3-sample",
         props={"background-color": "#F7EFE1", "border-top-color": "#221E1B",
                "border-top-width": "2px"}),
    # A bought result is a CARD on the hairline rule, at a bare 14px radius —
    # Design's one non-token radius in the unit, kept because it is what
    # separates a result from the panel it sits in.
    dict(name="a bought result is a card on the hairline rule", on=C2_ELEM,
         drive="budget-test-spent", sel=".ks3-result",
         props={"background-color": "#FFFCF5", "border-top-color": "#E0D2B9",
                "border-top-left-radius": "14px"}),
    dict(name="a SPENT test stays legible at .45, never disappears",
         on=C2_ELEM, drive="budget-test-spent", sel=".ks3-test-btn[disabled]",
         props={"opacity": "0.45"}),
    # ⚖️ The verdict panel is INK inside a light block and fires whether or
    # not the student was right. It is a reveal, never a mark — if it ever
    # picks up the ok or danger hue the bench starts marking, which R3
    # reserves for the ladder alone.
    dict(name="verdict panel is INK inside a light block, and never marks",
         on=C2_ELEM, drive="budget-verdict-given", sel="[data-verdict-panel]",
         props={"background-color": "#221E1B", "color": "#FBF3E6"}),
    dict(name="the sample's real name is display 800 on ink", on=C2_ELEM,
         drive="budget-verdict-given", sel=".ks3-verdict-name",
         props={"font-family": "Bricolage Grotesque", "font-weight": "800",
                "font-size": "24px", "color": "#FBF3E6"}),
    # ═══ BEGIN C1 ═══ rows
# Splice point: `COMPONENTS` in ks3_parity.py, in a new
# "C1 · Particles and their behaviour (⊕ MRB-228)" section.
#
# Requires one page constant beside the C2 ones (~line 360):
#
#     C1_PRESSURE = "chemistry/particles-and-their-behaviour/gas-pressure.html"
#
# Every row below uses the EXISTING `bench-gate-opened` drive: the bench does
# not exist in the document's layout until the commit gate is answered, so a
# measurement without it would report on an element that is `hidden`.
#
# Each row pins the property that makes the component DISTINCT, in the sense
# the file's own rule requires — break the CSS rule deliberately and the row
# fails.

    # ══ C1 · Particles and their behaviour (⊕ MRB-228) ═══════════════════

    # ── collision-counter (c1-04 #s-bench) ──
    # ⚠️ A LIGHT block. This is the row that catches the whole instrument
    # being mapped to `practical`: the frame's rule is 2px INK on a card
    # ground, and on ink it would report `#C6B9A7` over `#221E1B` — the
    # canvas's own cream drawing in a black surround, and every label in the
    # control strip resolving to its on-dark value.
    dict(name="counter canvas frame is a 2px INK rule on a card radius",
         on=C1_PRESSURE, drive="bench-gate-opened", sel=".ks3-counter-stage",
         props={"background-color": "#FFFCF5", "border-top-color": "#221E1B",
                "border-top-width": "2px", "border-top-left-radius": "22px",
                "overflow-x": "hidden"}),
    # The control strip is INSET, not card: it has to read as the bench's
    # panel rather than as more of the drawing above it, and the 2px ink rule
    # between them is the join.
    dict(name="counter control strip is inset under a 2px ink rule",
         on=C1_PRESSURE, drive="bench-gate-opened",
         sel=".ks3-counter-controls",
         props={"background-color": "#F7EFE1", "border-top-color": "#221E1B",
                "border-top-width": "2px"}),
    # Three captioned groups in one instrument. The captions are the only
    # thing telling a student that the second group is not more of the first
    # — the same argument as `muscle-pair`'s, with a third group.
    dict(name="counter group caption is a mono ink-muted label",
         on=C1_PRESSURE, drive="bench-gate-opened",
         sel=".ks3-counter-grouplabel",
         props={"font-family": "DM Mono", "font-size": "12px",
                "color": "#5F564F", "text-transform": "uppercase"}),
    # ⚖️ The live note takes the BAND-on-ink treatment — the KEY FACT
    # treatment, deliberately, and deliberately NOT a verdict tone. It is the
    # sentence the bench just proved, not a mark on anything the student did.
    # If it ever resolves to the accent tint it starts reading as feedback.
    dict(name="counter note is BAND on a 2px ink border, never a verdict tone",
         on=C1_PRESSURE, drive="bench-gate-opened", sel=".ks3-counter-note",
         props={"background-color": "#F4E9D8", "border-top-color": "#221E1B",
                "border-top-width": "2px", "font-size": "19px",
                "color": "#221E1B"}),
# ── PAGE CONSTANT ────────────────────────────────────────────────────────
# Add beside C2_ATOM … C2_MASS. All three of c1-06's instruments render only
# here, so all three are measured here — a component registered on a page that
# does not render it reports "selector not present" and passes, which is the
# absence-of-assertion failure this gate exists to close.
#
# C1_TEST = "chemistry/particles-and-their-behaviour/testing-the-model.html"


# ── COMPONENTS entries ───────────────────────────────────────────────────
# Each row pins the property that makes the component DISTINCT, not the ones it
# shares with every other panel. Mutation-test each before keeping it: break the
# rule in shared/ks3.css and confirm the row fails.

    # ══ C1 · Testing the model (⊕ MRB-228) ═══════════════════════════════

    # ── evidence-bench (c1-06 #s-bench) ──
    # The topology. A statement that can shrink beside a button pair that
    # cannot: if this ever resolves to `block`, the two calls drop under a
    # 54ch sentence and the seven cases stop being scannable as a column.
    dict(name="evidence case puts the calls beside the statement", on=C1_TEST,
         sel=".ks3-ebench-row",
         props={"display": "grid", "column-gap": "16px",
                "align-items": "start"}),

    # ⚖️ THE TWO-TONE VERDICT IS A FACT ABOUT THE MODEL, NOT ABOUT THE STUDENT.
    # A failure takes the BAND ground behind a 6px accent edge — the KEY FACT
    # treatment, deliberately not a red and not a dim. Both rows are driven,
    # because neither panel exists in the document's layout until its case is
    # judged, and both are measured in one document so the pair cannot drift
    # apart unnoticed.
    dict(name="a FAILING verdict is band behind a 6px accent edge", on=C1_TEST,
         drive="ebench-judged",
         sel='.ks3-ebench-case[data-ok="0"] .ks3-ebench-verdict',
         props={"background-color": "#F4E9D8", "border-left-color": "#E4572E",
                "border-left-width": "6px"}),
    dict(name="a HANDLED verdict is inset behind a quiet edge", on=C1_TEST,
         drive="ebench-judged",
         sel='.ks3-ebench-case[data-ok="1"] .ks3-ebench-verdict',
         props={"background-color": "#F7EFE1", "border-left-color": "#C3B191",
                "border-left-width": "6px"}),

    # The whole-set close. 24px display is what separates the counted line from
    # the paragraph under it; at body size the two read as one block of prose
    # and the number stops being the thing that lands.
    dict(name="evidence tally line is display 700 at 24px", on=C1_TEST,
         drive="ebench-all-judged", sel=".ks3-ebench-tallyline",
         props={"font-family": "Bricolage Grotesque", "font-weight": "700",
                "font-size": "24px"}),

# ⊖ NOT registered here, deliberately: `.ks3-ebench-case`'s resting card ground
# and its ink border once decided. That is the same two-value pattern already
# gated on `.ks3-jobsort-item` (rows 942 and 946) — one border going to ink on
# commitment — and re-asserting it on a second class buys coverage of a rule
# nobody can break independently.
# ks3_parity.py — gap-test-rig (c1-01 #s-gap)
#
# Uses the same C1_MODEL constant the halving-bench fragment adds.
#
# DRIVES — two, and both are required before the rows below can be spliced
# (`_unregistered_drives()` is fatal). The rig does not exist until a claim has
# been made about what it will show, so every state here is behind a click.
#
#     "gap-answered": r"""
# (function () {
#   var wrap = document.querySelector('[data-gap]');
#   if (!wrap) { return "no gap rig on the page"; }
#   var opt = wrap.querySelector('.ks3-option');
#   if (!opt) { return "the rig offers no choices"; }
#   opt.click();
#   var rig = wrap.querySelector('[data-gap-rig]');
#   if (!rig || rig.hasAttribute('hidden')) {
#     return "a choice was made and the rig never appeared";
#   }
#   return "";
# })()
# """,
#
#     "gap-tested": r"""
# (function () {
#   var wrap = document.querySelector('[data-gap]');
#   if (!wrap) { return "no gap rig on the page"; }
#   // The choice that FILLS the gap, so the test lands on its `off` outcome —
#   // the failure that is the whole argument of the block.
#   var empty = parseInt(wrap.getAttribute('data-empty-choice'), 10);
#   var opts = wrap.querySelectorAll('.ks3-option');
#   var pick = opts[empty === 0 ? 1 : 0];
#   if (!pick) { return "the rig offers no choices"; }
#   pick.click();
#   var t = wrap.querySelector('.ks3-gap-test');
#   if (!t) { return "the rig offers no tests"; }
#   t.click();
#   if (t.getAttribute('aria-pressed') !== 'true') {
#     return "a test was run and its button never lit";
#   }
#   var sec = document.getElementById('s-gap');
#   if (!sec || sec.getAttribute('data-stage-done') !== '1') {
#     return "a test was run and the stage never completed";
#   }
#   return "";
# })()
# """,
#
# COMPONENTS — four rows.

    # ── gap-test-rig (c1-01 #s-gap) ──
    # ⚠️ Both text rows exist to prove the SPECIFICITY scoping. `.ks3-dark p`
    # is (0,1,1) and a bare instrument class is (0,1,0): unscoped, the caption
    # and the outcome paragraph both lose to the block they sit in and render
    # in its body colour. That defect shipped with the zoom instrument on B1
    # and bit B2 again, which is why it is pinned rather than assumed.
    dict(name="gap control caption is mono 12px uppercase on-dark-muted",
         on=C1_MODEL, drive="gap-answered", sel=".ks3-gap-caption",
         props={"font-family": "DM Mono", "font-size": "12px",
                "color": "#C6B9A7", "text-transform": "uppercase"}),
    dict(name="gap outcome is on-dark BODY, not the block's own colour",
         on=C1_MODEL, drive="gap-answered", sel=".ks3-gap-note p",
         props={"color": "#E7DECE", "font-size": "19px"}),
    # The dark branch of the segmented control, resting: on-dark text on the
    # muted rule. If this resolves to ink the rig has been painted as a light
    # instrument and the buttons vanish into the block.
    dict(name="a gap test at rest is on-dark text on the muted rule",
         on=C1_MODEL, drive="gap-answered", sel=".ks3-gap-test",
         props={"color": "#FBF3E6", "border-top-color": "#C6B9A7",
                "border-top-width": "2px", "min-height": "44px"}),
    # ⚖️ The RUNNING test is the alert amber with ink on it — the shipped dark
    # pressed state, measured in the state through the rig's own controls.
    # Amber here is not a verdict on the student: it marks which test is on the
    # bench, and the outcome paragraph is one tone whichever answer they gave.
    dict(name="the running gap test is alert amber with ink on it",
         on=C1_MODEL, drive="gap-tested",
         sel='.ks3-gap-test[aria-pressed="true"]',
         props={"background-color": "#FFC53D", "color": "#221E1B",
                "border-top-color": "#FFC53D"}),
# ks3_parity.py — halving-bench (c1-01 #s-cut)
#
# 1. PAGE CONSTANT — add beside C2_ATOM / C2_ELEM (~line 357):
#
#        C1_MODEL = "chemistry/particles-and-their-behaviour/particle-model.html"
#
# 2. DRIVE — add to DRIVES. ⚠️ `_unregistered_drives()` is FATAL, so the rows
#    below cannot be spliced without it. `bench-gate-opened` already exists and
#    is reused; this second one reaches the floor through the bench's own
#    controls, so a regression in the interaction path fails HERE rather than
#    being measured around.
#
#     "cut-floor-reached": r"""
# (function () {
#   var gate = document.querySelector('[data-benchgate]');
#   if (!gate) { return "no commit gate on the page"; }
#   gate.querySelector('.ks3-option').click();
#   var bench = document.querySelector('[data-cut]');
#   if (!bench) { return "the bench did not appear after the gate"; }
#   var floor = parseInt(bench.getAttribute('data-floor'), 10) || 0;
#   var ten = bench.querySelector('.ks3-cut-btn[data-step="10"]');
#   var one = bench.querySelector('.ks3-cut-btn[data-step="1"][data-act="cut"]');
#   if (!ten || !one) { return "the bench offers no cut controls"; }
#   for (var i = 0; i < floor; i++) {
#     if (!ten.hasAttribute('disabled')) { ten.click(); }
#     else if (!one.hasAttribute('disabled')) { one.click(); }
#     else { break; }
#   }
#   var count = bench.querySelector('[data-cut-out="count"]');
#   if (!count || parseInt(count.textContent, 10) !== floor) {
#     return "cutting stopped at " + (count && count.textContent) +
#            " of " + floor;
#   }
#   if (!document.querySelector('[data-verdict="floor"]:not([hidden])')) {
#     return "the floor was reached and the verdict never changed";
#   }
#   return "";
# })()
# """,
#
# 3. COMPONENTS — the four rows below. Each was chosen because it is the
#    property that makes this instrument DISTINCT; the mono readout LABEL is
#    deliberately not among them, because it is the shipped mono caption that
#    `.ks3-joint-tile-mono` and the budget line already pin.

    # ══ C1 · Particles and their behaviour (⊕ MRB-228) ═══════════════════

    # ── halving-bench (c1-01 #s-cut) ──
    # ⚠️ A LIGHT instrument, and this row is what proves it. Its sibling
    # `#s-gap` on the same page is ink-dark and uses `.ks3-canvas-frame`; if
    # this frame ever resolves to the muted rule (#C6B9A7) the bench has been
    # mapped onto the dark frame and every text token inside it is wrong.
    dict(name="cut bench frame is a 2px INK rule on the card ground",
         on=C1_MODEL, drive="bench-gate-opened", sel=".ks3-cut-frame",
         props={"background-color": "#FFFCF5", "border-top-color": "#221E1B",
                "border-top-width": "2px", "border-top-left-radius": "22px"}),
    # The readouts are the lesson — "watch the size, not the picture" — so they
    # are display type at 30px, not the 25px mono a sim readout takes. If this
    # row ever reports the mono face, the numbers have stopped being the
    # headline of the block.
    dict(name="cut readout value is display 700 30px ink", on=C1_MODEL,
         drive="bench-gate-opened", sel=".ks3-cut-value",
         props={"font-family": "Bricolage Grotesque", "font-weight": "700",
                "font-size": "30px", "color": "#221E1B"}),
    # ⚖️ The floor verdict is accent-TEXT and never the accent itself: it is
    # read at 30px but it is a state word, and #E4572E is 3.4:1. Measured in
    # the state, through 24 real cuts.
    dict(name="the floor verdict is accent-text, not the accent", on=C1_MODEL,
         drive="cut-floor-reached",
         sel='.ks3-cut-value [data-verdict="floor"]',
         props={"color": "#A93411"}),
    # ⚖️ The running note is a BAND panel on a 2px ink border — the same
    # treatment `claim-switch`'s note takes, and deliberately not amber. Amber
    # is a wrong idea being confronted; this paragraph is the state of the
    # model, and a student who has cut nothing has made no mistake.
    dict(name="cut note is a band panel on ink, never amber", on=C1_MODEL,
         drive="bench-gate-opened", sel=".ks3-cut-note",
         props={"background-color": "#F4E9D8", "border-top-color": "#221E1B",
                "border-top-width": "2px"}),
# PAGE CONSTANT (add beside the other C1 page constants in ks3_parity.py):
#
#     C1_STATE = "chemistry/particles-and-their-behaviour/changes-of-state.html"
#
# DRIVE: none new. The bench lives behind C6's commit gate, so every row below
# that measures the instrument itself uses the SHIPPED `bench-gate-opened`
# drive; `#s-curve` is the only gate on this page, which is what that drive
# selects. The mass tile is measured on the same driven load.

    # ── heating-bench (c1-03 #s-curve) ──
    # ⚠️ A LIGHT bench. If the frame row ever reports `#3E3730` or the note
    # row reports on-dark body copy, the instrument has been mapped to
    # `practical` and the graph's paper has become a hole in an ink block —
    # the exact trap the payload map names for this lesson.
    dict(name="heating bench frame is a 2px INK rule on a card ground",
         on=C1_STATE, drive="bench-gate-opened", sel=".ks3-hb-frame",
         props={"background-color": "#FFFCF5", "border-top-color": "#221E1B",
                "border-top-width": "2px", "border-top-left-radius": "22px",
                "overflow-x": "hidden"}),

    # ⚖️ THE CONSTANT IS A FULL READOUT. `Mass in the flask · 50.0 g` is
    # hard-coded markup and it is the confrontation of the lesson, so it is
    # asserted at the same 30px display type as the two tiles that DO move.
    # If it ever resolves as a caption, the one number that says nothing was
    # lost has been quietly demoted below the two that change.
    dict(name="the constant mass reads as a full display-type readout",
         on=C1_STATE, drive="bench-gate-opened", sel=".ks3-hb-mass",
         props={"font-family": "Bricolage Grotesque", "font-size": "30px",
                "font-weight": "700", "color": "#221E1B"}),

    # 44px of control around a 10px track, and the reset appearance is what
    # makes it a drawn control rather than a browser default. No `width`: it
    # is 100% of a column whose px value follows the viewport, and this
    # harness pins none.
    dict(name="the scrub clears the 44px tap target", on=C1_STATE,
         drive="bench-gate-opened", sel=".ks3-hb-scrub",
         props={"height": "44px", "appearance": "none",
                "accent-color": "#E4572E"}),

    # The plateau note takes the KEY FACT treatment — band on a 2px ink rule
    # — because the sentence it carries while the thermometer is stuck is the
    # fact the lesson exists to deliver. Never amber: this is not a wrong
    # idea being confronted.
    dict(name="the plateau note is a BAND panel on ink", on=C1_STATE,
         drive="bench-gate-opened", sel=".ks3-hb-note",
         props={"background-color": "#F4E9D8", "border-top-color": "#221E1B",
                "border-top-width": "2px", "font-size": "19px",
                "color": "#221E1B"}),
# ── PAGE CONSTANT ────────────────────────────────────────────────────────
# `keyed-commit` renders on two pages. Measured on c1-06, whose instance is the
# one PAYLOAD-MAP §6.5.2 ruled the shape from — four options each carrying a
# reply, against c1-03's three branched responses. The wider shape cannot pass
# on a rule the narrower one would fail.
#
# C1_TEST = "chemistry/particles-and-their-behaviour/testing-the-model.html"


# ── COMPONENTS entries ───────────────────────────────────────────────────
# Mutation-tested: each rule was deliberately broken in shared/ks3.css and the
# row confirmed to fail before it was kept.

    # ── keyed-commit (c1-06 #s-verdict) ──
    #
    # ⚠️ BOTH ROWS EXIST TO PROVE THE SPECIFICITY SCOPING. `.ks3-dark p` is
    # (0,1,1) and a bare `.ks3-keyed-reply` is (0,1,0): unscoped, the reply
    # loses and renders in `--ks3-on-dark-body` against the panel rather than
    # in the panel's own treatment. That is the defect B1 shipped with the zoom
    # instrument and B2 was bitten by again, and it is invisible to reading.
    dict(name="verdict panel is a dark panel on a muted rule", on=C1_TEST,
         drive="keyed-committed", sel=".ks3-keyed-reveal",
         props={"background-color": "#3E3730", "border-top-color": "#C6B9A7",
                "border-top-width": "2px",
                "border-top-left-radius": "20px"}),
    dict(name="the chosen reply is on-dark body copy, not muted", on=C1_TEST,
         drive="keyed-committed",
         sel='.ks3-keyed-reply:not([hidden])',
         props={"color": "#E7DECE", "font-size": "19px"}),
    # The reply and the static paragraphs must resolve IDENTICALLY. The panel's
    # argument is that the student's answer and the historical record are the
    # same kind of sentence; a reply painted differently from the paragraphs
    # under it would read as a verdict on the choice, which is exactly what R3
    # forbids here.
    dict(name="the static close matches the reply exactly", on=C1_TEST,
         drive="keyed-committed", sel=".ks3-keyed-static",
         props={"color": "#E7DECE", "font-size": "19px",
                "margin-top": "14px"}),
    # 36rem, Design's own measure on both pages. Full-width answer buttons on a
    # 60rem column are a target the eye has to travel.
    dict(name="commit options keep Design's 36rem measure", on=C1_TEST,
         sel=".ks3-keyed-options", props={"max-width": "576px"}),
# ── PAGE CONSTANT ────────────────────────────────────────────────────────
# Shares C1_TEST with the other two c1-06 instruments:
#
# C1_TEST = "chemistry/particles-and-their-behaviour/testing-the-model.html"


# ── COMPONENTS entries ───────────────────────────────────────────────────
# Every row was mutation-tested: the rule was deliberately broken in
# shared/ks3.css and the row confirmed to fail before it was kept.

    # ── model-timeline (c1-06 #s-history) ──
    #
    # ⚠️ THE THIRD CONTROL GEOMETRY. `.ks3-seg-btn` and `.ks3-sim-seg-btn` are
    # both centred single lines; this one is LEFT-ALIGNED at `10px 14px`. If it
    # ever resolves to `center`, the year and the name stop stacking against a
    # common left edge and the five positions cannot be read down the row —
    # which is the whole reason it was not folded into `seg()`.
    dict(name="timeline step is a LEFT-ALIGNED 44px control", on=C1_TEST,
         sel=".ks3-mtl-step",
         props={"text-align": "left", "min-height": "44px",
                "padding-left": "14px", "padding-top": "10px",
                "background-color": "#FBF3E6",
                "border-top-color": "#DDCFB6"}),
    # The two-line stack. `display: block` on the year is the only thing making
    # the button two lines; inline, the year and the name run together and the
    # control collapses into a long label.
    dict(name="timeline year is a mono line of its own", on=C1_TEST,
         sel=".ks3-mtl-year",
         props={"display": "block", "font-family": "DM Mono",
                "font-size": "12px"}),
    # The chosen step takes the accent tint and nothing else — R3: it shows it
    # was chosen, and there is nothing here to be right or wrong about.
    dict(name="the open model takes the accent tint, never a verdict",
         on=C1_TEST, sel='.ks3-mtl-step[aria-pressed="true"]',
         props={"background-color": "#FCE7DE", "border-top-color": "#E4572E"}),
    # 26px display, and the muted rule-topped line under it. The claim has to
    # out-rank the body from the scroll position; "What broke it:" has to
    # survive being skimmed, which is why the label is ink and the line is not.
    dict(name="timeline claim is display 700 at 26px", on=C1_TEST,
         sel=".ks3-mtl-claim",
         props={"font-family": "Bricolage Grotesque", "font-weight": "700",
                "font-size": "26px"}),

# ⊖ No drive. The default card is open at rest — the row opens on Dalton, not
# on Democritus — so every measured selector exists in the resting document.
# That is itself worth knowing: if `default_index` ever stopped being honoured,
# `.ks3-mtl-step[aria-pressed="true"]` would match nothing and the row above
# would report a missing selector rather than passing quietly.
# Splice point: `COMPONENTS` in ks3_parity.py, in the C1 section, directly
# after the collision-counter rows. Uses the same page constant:
#
#     C1_PRESSURE = "chemistry/particles-and-their-behaviour/gas-pressure.html"
#
# ⚠️ THE LAST TWO ROWS NEED A NEW DRIVE. The answered states only exist after
# a click, and no shipped drive reaches them: `dark-option-chosen` clicks the
# first `.ks3-dark .ks3-option`, which on this page is in `#s-hook`, and these
# are segmented buttons rather than lettered options. Splice this into `DRIVES`
# beside the other C1/C2 entries, or drop the two driven rows:
#
#     # Two predictions in one document: one answered right, so the panel
#     # takes the alert border, and one answered wrong, so the shared
#     # fallback note is on screen in its own tone. Both states reached
#     # through the instrument's own buttons, so a regression in the
#     # interaction path fails HERE rather than being measured around.
#     "prediction-answered": r"""
# (function () {
#   var panels = document.querySelectorAll('.ks3-predict');
#   if (panels.length < 2) { return "need 2 predictions, found " + panels.length; }
#   function pick(panel, correct) {
#     var want = parseInt(panel.getAttribute('data-answer'), 10);
#     var opts = panel.querySelectorAll('.ks3-predict-btn');
#     for (var i = 0; i < opts.length; i++) {
#       if ((i === want) === correct) { opts[i].click(); return true; }
#     }
#     return false;
#   }
#   if (!pick(panels[0], true))  { return "no correct option in prediction 1"; }
#   if (!pick(panels[1], false)) { return "no wrong option in prediction 2"; }
#   if (panels[0].getAttribute('data-right') !== '1') {
#     return "the answered prediction did not take its verdict state";
#   }
#   return "";
# })()
# """,

    # ── prediction-stack (c1-04 #s-predict) ──
    # Three panels nested inside an ink-dark block: `--ks3-dark-panel` on the
    # muted rule, which is the same nesting `joint-bench`'s tiles use. If this
    # ever reports the block's own `#221E1B` the panels have stopped being
    # panels and the three predictions read as one wall of text.
    dict(name="prediction panel is a dark panel on a 2px muted rule",
         on=C1_PRESSURE, sel=".ks3-predict",
         props={"background-color": "#3E3730", "border-top-color": "#C6B9A7",
                "border-top-width": "2px", "border-top-left-radius": "20px"}),
    # ⚖️ THE SPECIFICITY ROW. `.ks3-dark p` is (0,1,1) and a bare
    # `.ks3-predict-q` is (0,1,0): unscoped, the question renders in on-dark
    # BODY copy at whatever weight the cascade leaves it, which is the defect
    # B1 shipped and B2 repeated. `#FBF3E6` at 600 is the proof it is scoped.
    dict(name="prediction question is on-dark 600, not on-dark body",
         on=C1_PRESSURE, sel=".ks3-predict-q",
         props={"color": "#FBF3E6", "font-size": "18px",
                "font-weight": "600"}),
    # The panel — never the option — carries the verdict.
    dict(name="a matched prediction takes the ALERT border, on the panel",
         on=C1_PRESSURE, drive="prediction-answered",
         sel='.ks3-predict[data-right="1"]',
         props={"border-top-color": "#FFC53D", "border-top-width": "2px",
                "background-color": "#3E3730"}),
    # The one shared fallback, in the ink-dark palette's lit colour. 7.4:1 on
    # the panel; if it ever falls back to on-dark body it stops being
    # distinguishable from the note that says the student had it right.
    dict(name="the shared wrong-answer note is alert, not on-dark body",
         on=C1_PRESSURE, drive="prediction-answered",
         sel='.ks3-predict-note[data-tone="wrong"]',
         props={"color": "#FFC53D", "font-size": "17px"}),
# ks3_parity.py — COMPONENTS entries for `random-walk-bench` (c1-05 #s-walk).
#
# Needs the page constant, beside the C2 block near line 362:
#
#     # ⊕ C1 · Particles and their behaviour (rebuild, MRB-228). Same rule
#     # again: a component is registered on the page that RENDERS it. Both new
#     # C1 kinds live only on c1-05, so both are measured there.
#     C1_DIFF = "chemistry/particles-and-their-behaviour/diffusion.html"
#
# `bench-gate-opened` is the existing generic drive and needs no new entry:
# c1-05 has exactly one `[data-benchgate]`, and the bench is `hidden` until it
# is answered, so three of the four rows below cannot be measured without it.
#
# ⚠️ NOT mutation-tested by the authoring agent — no browser in this run. Each
# row names the property that makes its component distinct and would resolve to
# a different value if the rule were dropped; the commander should break each
# rule once and confirm the row fails before these are kept.

    # ══ C1 · Particles and their behaviour (⊕ MRB-228) ═══════════════════

    # ── random-walk-bench (c1-05 #s-walk) ──
    # ⚠️ A LIGHT block, and this row is the guard on that. The frame is
    # `--ks3-card` on a 2px INK rule; if it ever reports `#C6B9A7` the bench
    # has been mapped onto `.ks3-canvas-frame`, which is the DARK twin, and the
    # tank ends up outlined in an on-dark colour on cream. If it reports
    # `#221E1B` as the BACKGROUND, the block has been mapped to `practical`
    # and every text token in the instrument resolves wrong.
    dict(name="walk frame is a card on a 2px ink rule, not the dark frame",
         on=C1_DIFF, drive="bench-gate-opened", sel=".ks3-walk-frame",
         props={"background-color": "#FFFCF5", "border-top-color": "#221E1B",
                "border-top-width": "2px", "border-top-left-radius": "22px"}),

    # ⚖️ THE TWO COUNTERS ARE THE LESSON. They are display 700 at 30px so that
    # a student can watch them climb side by side after the tank has evened
    # out — the confrontation of PART-11 is a comparison between two numbers,
    # and a caption-sized readout is a number you check rather than watch.
    # `tabular-nums` is what stops them jittering sideways as they gain digits.
    dict(name="crossing counters are display 700 30px, tabular",
         on=C1_DIFF, drive="bench-gate-opened", sel=".ks3-walk-readout-value",
         props={"font-family": "Bricolage Grotesque", "font-weight": "700",
                "font-size": "30px", "color": "#221E1B",
                "font-variant-numeric": "tabular-nums"}),

    # The live note takes the KEY FACT treatment — band on a 2px ink border —
    # deliberately, and not a tint or a dim: the bench is telling the student
    # what they are looking at, and it is never marking them.
    dict(name="walk note is a band panel on ink", on=C1_DIFF,
         drive="bench-gate-opened", sel=".ks3-walk-note",
         props={"background-color": "#F4E9D8", "border-top-color": "#221E1B",
                "border-top-width": "2px"}),

    # ⚖️ THE CONTRAST FIX, and the reason it is scoped rather than global.
    # `.ks3-commit` is `--ks3-alert` because every other commit in the key
    # stage sits on ink. This one sits on `--ks3-inset` cream, where amber is
    # unreadable, so the block repaints it `--ks3-accent-text` — the 6:1
    # orange. No `drive`: the gate is what the page opens on.
    dict(name="the light bench's commit is accent-TEXT, never the amber",
         on=C1_DIFF, sel=".ks3-walk-block .ks3-benchgate .ks3-commit",
         props={"color": "#A93411", "font-size": "22px",
                "font-weight": "700"}),
# ks3_parity.py — COMPONENTS entries for `scale-cards` (c1-05 #s-scale).
#
# Uses the same `C1_DIFF` page constant declared in the random-walk-bench
# fragment. No `drive` on any row: the panel is static and is on the page from
# the first paint, which is the whole character of the component.
#
# ⚠️ NOT mutation-tested by the authoring agent — no browser in this run. Each
# row would resolve differently if its rule were dropped; the commander should
# break each one once and confirm the row fails before these are kept.

    # ── scale-cards (c1-05 #s-scale) ──
    # A panel NESTED inside an ink-dark block, so it takes `--ks3-dark-panel`
    # on the muted rule. If it ever reports the block's own ground the three
    # cards stop reading as cards and the grid becomes three paragraphs.
    dict(name="scale card is a dark panel on the muted rule", on=C1_DIFF,
         sel=".ks3-scard",
         props={"background-color": "#3E3730",
                "border-top-color": "#C6B9A7", "border-top-width": "2px",
                "border-top-left-radius": "20px"}),

    # ⚑ REGISTERED BECAUSE IT IS FLAGGED, not because it is settled. PAYLOAD-MAP
    # §5.5.2: amber on ink is established for CONTROLS since B1 and for
    # misconception BLOCKS; this is amber for a body label, which is neither,
    # and the map flags it without resolving it. Pinning the value here means a
    # re-ruling arrives as a failing row that names itself, rather than as a
    # repaint nobody notices.
    dict(name="scale card distance is the flagged amber body label",
         on=C1_DIFF, sel=".ks3-scard-distance",
         props={"font-family": "DM Mono", "font-size": "12px",
                "text-transform": "uppercase", "color": "#FFC53D"}),

    # ⚠️ THE SPECIFICITY ROW. `.ks3-dark p` is (0,1,1) and a bare
    # `.ks3-scard-time` is (0,1,0): unscoped, this loses its `--ks3-on-dark`
    # and resolves to `#E7DECE` body copy, so the answer to the card's own
    # question renders as a caption. Same defect B1 shipped with the zoom
    # instrument and B2 was bitten by again.
    dict(name="scale card time is display 28px full on-dark, not body copy",
         on=C1_DIFF, sel=".ks3-scard-time",
         props={"font-family": "Bricolage Grotesque", "font-weight": "700",
                "font-size": "28px", "color": "#FBF3E6"}),
# PAGE CONSTANT (shared with heating-bench.parity.py — declare it once):
#
#     C1_STATE = "chemistry/particles-and-their-behaviour/changes-of-state.html"
#
# DRIVE (new — add to ks3_parity.DRIVES):
#
#     # One card sorted CORRECTLY and one sorted WRONGLY, which is the only
#     # way both card borders and both note tones exist in one document. The
#     # sorter is not one-shot, so the second click is a real second card and
#     # never a re-press of the first.
#     "sortcards-decided": r"""
# (function () {
#   var cards = document.querySelectorAll('.ks3-sortcards-card');
#   if (cards.length < 2) { return "need 2 sort cards, found " + cards.length; }
#   function pick(card, correct) {
#     var want = card.getAttribute('data-answer');
#     var opts = card.querySelectorAll('.ks3-sortcards-opt');
#     for (var j = 0; j < opts.length; j++) {
#       if ((opts[j].getAttribute('data-choice') === want) === correct) {
#         opts[j].click();
#         return true;
#       }
#     }
#     return false;
#   }
#   if (!pick(cards[0], true))  { return "no matching option on card 1"; }
#   if (!pick(cards[1], false)) { return "no other option on card 2"; }
#   if (cards[0].getAttribute('data-verdict') !== 'right'
#       || cards[1].getAttribute('data-verdict') !== 'wrong') {
#     return "cards did not record their verdicts";
#   }
#   return "";
# })()
# """,

    # ── sort-cards (c1-03 #s-think) ──
    # A cream card on the OPTION border, inside the amber misconception
    # shell. If this row ever reports `#FFF3D4` the card has taken the
    # shell's own ground and the student's working has become part of the
    # wrong idea being confronted.
    dict(name="sort card is a card on the option border", on=C1_STATE,
         sel=".ks3-sortcards-card",
         props={"background-color": "#FFFCF5", "border-top-color": "#DDCFB6",
                "border-top-width": "2px", "border-top-left-radius": "20px"}),

    # ⚖️ Design's own marking rule, and the only marked activity card in C1.
    # Both states in one row-pair so neither can drift alone: accent when the
    # word fits, plain ink when it does not — never the ok family, never a
    # drawn mark. If the "wrong" row ever reports a red or a green, R3 has
    # been broken here and the block has become a test.
    dict(name="a card that FITS takes the accent border", on=C1_STATE,
         drive="sortcards-decided", sel='.ks3-sortcards-card[data-verdict="right"]',
         props={"border-top-color": "#E4572E", "border-top-width": "2px"}),
    dict(name="a card that does not fit takes the plain INK border",
         on=C1_STATE, drive="sortcards-decided",
         sel='.ks3-sortcards-card[data-verdict="wrong"]',
         props={"border-top-color": "#221E1B", "border-top-width": "2px"}),

    # The correction is accent-TEXT at 16px — the only orange the key stage
    # allows below 24px, and the reason the note is not painted in
    # `--ks3-accent` to match the border it sits inside.
    dict(name="the correction note is accent-text, not accent", on=C1_STATE,
         drive="sortcards-decided",
         sel='.ks3-sortcards-note[data-note="wrong"]:not([hidden])',
         props={"color": "#A93411", "font-size": "16px"}),
# ks3_parity.COMPONENTS entries for `state-bench` (c1-02 #s-bench).
#
# The page constant this needs does not exist yet — add it beside the other
# per-lesson constants (ks3_parity.py ~line 357, where C2_ATOM … C2_MASS live):
#
#     C1_STATES = "chemistry/particles-and-their-behaviour/solids-liquids-and-gases.html"
#
# ⚠️ Not `LESSON`. That constant is c1-04 (`gas-pressure.html`), which renders
# no state bench at all — a component measured on a page without it reports
# "selector not present" and PASSES, which is the absence-of-assertion failure
# MRB-198 closed one level down.
#
# `drive="bench-gate-opened"` on all four: C6 gates the bench by ABSENCE, so
# nothing inside `[data-benchbody]` exists in the layout until the commit is
# answered. The existing driver is reused unchanged — it clicks the first
# option, asserts the gate goes and asserts the body arrives, which is exactly
# the contract `wireStateBench` implements for itself.

    # ── state-bench (c1-02 #s-bench) ──
    # ⚖️ The frame is the LIGHT twin of `.ks3-canvas-frame`, and the two must
    # not converge. If this ever resolves to `--ks3-on-dark-muted` over
    # `--ks3-dark-panel`, the bench has been repainted for an ink block that
    # c1-02 does not have — its only dark grounds are the hook and the keynote,
    # and the particle drawing is cream on cream.
    dict(name="state bench frame is CARD on a 2px ink border", on=C1_STATES,
         drive="bench-gate-opened", sel=".ks3-sbench-frame",
         props={"background-color": "#FFFCF5", "border-top-color": "#221E1B",
                "border-top-width": "2px",
                "border-top-left-radius": "22px"}),
    # ⚖️ The chosen state keeps INK text, deliberately. `.ks3-seg-btn`'s chosen
    # state goes to `--ks3-accent-text`, and on this bench the three state
    # buttons are a picker rather than an answer — accent text on the chosen
    # one would read as a verdict (R3 / MRB-196 R10). The size is C1's own
    # 16px, not drift 4's 17px; §1.6 (d) has that ruling reopened on a
    # six-pages-against-one count and this block does not pre-empt it.
    dict(name="chosen state button is accent-tint on ink text, at C1's 16px",
         on=C1_STATES, drive="bench-gate-opened",
         sel='.ks3-sbench-seg[aria-pressed="true"]',
         props={"background-color": "#FCE7DE", "border-top-color": "#E4572E",
                "color": "#221E1B", "font-size": "16px"}),
    # The panel holding whichever of the eight notes is live: BAND on a 2px ink
    # border, which is the KEY FACT treatment and deliberately not a tint. The
    # note is the sentence that settles what the student has just done, not a
    # verdict on it.
    dict(name="bench note is a BAND panel on ink", on=C1_STATES,
         drive="bench-gate-opened", sel=".ks3-sbench-note",
         props={"background-color": "#F4E9D8", "border-top-color": "#221E1B",
                "border-top-width": "2px"}),
    # ⚠️ THE SPECIFICITY GUARD, and the reason it is a row rather than a
    # comment. The text rule is `.ks3-sbench .ks3-sbench-note-text` at (0,2,0),
    # because `.ks3-dark p` is (0,1,1) and would beat a bare instrument class
    # at (0,1,0) — the defect B1 shipped with the zoom note and B2 was bitten
    # by again. c1-02 has no dark block today; this is what keeps that true if
    # the bench is ever reused on a page that does.
    dict(name="bench note text is INK body copy, not the block's own colour",
         on=C1_STATES, drive="bench-gate-opened", sel=".ks3-sbench-note-text",
         props={"color": "#221E1B", "font-size": "19px",
                "line-height": "30.4px"}),
# ks3_parity.COMPONENTS entries for `state-matrix` (c1-02 #s-matrix).
#
# Same page constant as the bench — add it once:
#
#     C1_STATES = "chemistry/particles-and-their-behaviour/solids-liquids-and-gases.html"
#
# ⚠️ NO `drive` on any of these, and that is the assertion. The matrix is NOT
# behind the bench's commit gate — Design draws the table in full from the
# first paint and lights the `arrangement` row at rest — so every row below is
# measurable on a page nobody has touched. If one of these ever needs a driver,
# the table has been moved behind something and the section that promised "the
# highlighted row is the one your current bench setting is showing" has stopped
# being able to keep that promise on arrival.

    # ── state-matrix (c1-02 #s-matrix) ──
    # Column heads and row heads share one treatment, because in a matrix the
    # first column is a head as much as the first row is. Mono on band, at the
    # 13px the rest of the key stage's small mono uses.
    dict(name="matrix column head is mono uppercase on band", on=C1_STATES,
         sel=".ks3-smatrix-table thead th",
         props={"font-family": "DM Mono", "font-size": "13px",
                "text-transform": "uppercase",
                "background-color": "#F4E9D8",
                "border-top-color": "#221E1B", "border-top-width": "2px"}),
    # ⚖️ THE LIT ROW, MEASURED AT REST. `arrangement` is lit on arrival —
    # `r_state_matrix` emits it lit at build time by the same rule the runtime
    # uses, so there is no unlit instant before the JS runs. Accent TINT and
    # never the accent fill, and never amber: this is "the bench is showing you
    # this one", not a verdict and not a wrong idea.
    dict(name="the lit matrix row is accent TINT, on arrival", on=C1_STATES,
         sel='.ks3-smatrix-row[data-lit="1"]',
         props={"background-color": "#FCE7DE"}),
    # And the row beside it, so the pair proves there is a visible difference
    # rather than a tint that resolves to the same cream as the card.
    dict(name="an unlit matrix row is CARD", on=C1_STATES,
         sel='.ks3-smatrix-row[data-lit="0"]',
         props={"background-color": "#FFFCF5"}),
    # ⚖️ CORRECTED (MRB-228). This assertion was written on the ROW and asked
    # it for `border-top-width: 2px`. It resolved 0px and the gate failed —
    # correctly, and on the assertion rather than on the stylesheet. The 2px
    # ink grid is set on `.ks3-smatrix-table th, td`, which is where a table
    # grid belongs; a `<tr>` carries no border of its own. Measuring the row
    # was asking the wrong element for someone else's property.
    #
    # Kept as its own row rather than folded into the one above, because the
    # grid and the row ground are two different claims and a merged row would
    # not say which of them broke.
    dict(name="the matrix grid is a 2px ink rule on the cells", on=C1_STATES,
         sel='.ks3-smatrix-row[data-lit="0"] > td',
         props={"border-top-color": "#221E1B", "border-top-width": "2px"}),
    # The footnote. Scoped `.ks3-smatrix .ks3-smatrix-foot` at (0,2,0) for the
    # standing `.ks3-dark p` reason (0,1,1) — c1-02 has no dark block today and
    # this is what keeps the rule winning if the table is ever reused on a page
    # that does.
    dict(name="matrix footnote is ink-muted at 18px", on=C1_STATES,
         sel=".ks3-smatrix-foot",
         props={"color": "#5F564F", "font-size": "18px"}),
    # ═══ END C1 ═══ rows
    # ═══ BEGIN B2 ═══ rows
# ── PAGE CONSTANT ────────────────────────────────────────────────────────
# One drawn instance, on b2-04. It is the only ink-dark instrument in the
# lesson, which is why three of the four rows below exist.
#
#     B2_BIO = "biology/movement-skeleton-and-muscles/biomechanics-forces-in-the-body.html"


# ── COMPONENTS entries ───────────────────────────────────────────────────
# Mutation-tested: each rule was deliberately broken in shared/ks3.css and the
# row confirmed to fail before it was kept.

    # ── arm-lever (b2-04 #s-bench) ──
    #
    # ⚠️ THIS ROW IS THE SPECIFICITY GUARD, and it is the reason the rest of
    # the block's rules are written `.ks3-dark …`. `.ks3-dark p` is (0,1,1);
    # a bare `.ks3-lever-tile-label` is (0,1,0) and LOSES, so an unscoped
    # colour renders the mono uppercase caption in `--ks3-on-dark-body` — the
    # same tone as the value under it, which stops the tile reading as a
    # caption over a number. Legible, so nobody reports it; wrong, so the
    # three measured tiles quietly stop being tiles. B1's zoom instrument
    # shipped exactly this and the joint bench nearly repeated it.
    dict(name="rig tile caption is mono muted on the dark panel, not body copy",
         on=B2_BIO, drive="lever-opened", sel=".ks3-lever-tile-label",
         props={"color": "#C6B9A7", "font-size": "13px",
                "text-transform": "uppercase"}),
    # ⚖️ THE TWO TILE TREATMENTS ARE THE GATE MADE VISIBLE. The three measured
    # tiles are mono 25px and the force tile is 19px/700 prose type, because
    # until the meter is fitted it holds a sentence. A single treatment would
    # set "not measured — you work it out" in a 25px readout face, which reads
    # as a broken number rather than as a refusal.
    dict(name="a measured tile is a 25px mono readout", on=B2_BIO,
         drive="lever-opened",
         sel='.ks3-lever-tile-value[data-lever-out="weight"]',
         props={"font-size": "25px", "font-weight": "500",
                "color": "#FBF3E6"}),
    dict(name="the withheld force tile is prose type, not a readout",
         on=B2_BIO, drive="lever-opened",
         sel='.ks3-lever-tile-value[data-lever-out="force"]',
         props={"font-size": "19px", "font-weight": "700"}),
    # The rig's frame matches the joint bench's value for value — same 2px
    # muted rule, same card radius. Two canvases framed differently on two
    # pages of one unit is drift a student notices before an adult does.
    dict(name="rig canvas frame is a 2px muted rule on a card radius",
         on=B2_BIO, drive="lever-opened", sel=".ks3-lever-stage",
         props={"border-top-color": "#C6B9A7", "border-top-width": "2px",
                "border-top-left-radius": "22px"}),
# ── PAGE CONSTANT ────────────────────────────────────────────────────────
# Measured on b2-04, the only page that renders the WIDENED triangle. b1-02
# renders the narrow one and is asserted separately, by byte-identity across
# the splice rather than by a resolved-style row — a rule that passes on both
# variants would prove nothing about either.
#
#     B2_BIO = "biology/movement-skeleton-and-muscles/biomechanics-forces-in-the-body.html"


# ── COMPONENTS entries ───────────────────────────────────────────────────
# Mutation-tested: each rule below was deliberately broken in shared/ks3.css
# and the row confirmed to fail before it was kept.

    # ── cover-triangle · triangle variant (b2-04's rule block) ──
    #
    # ⚠️ THIS ROW IS THE b1-02 GUARD. Every widened declaration is scoped
    # `[data-tri-layout="row"]`, and the row layout is what proves the scope
    # exists: if a future tidy-up moved the flex onto bare `.ks3-triangle`,
    # b1-02's centred stack would silently become a two-column row and this
    # row would still pass — so it asserts the SIDE panel's own flex basis,
    # which only the widened markup has an element for.
    dict(name="the widened triangle puts the reading beside the figure",
         on=B2_BIO, sel='.ks3-triangle[data-tri-layout="row"] .ks3-tri-row',
         props={"display": "flex", "flex-wrap": "wrap",
                "column-gap": "52px", "row-gap": "34px"}),
    dict(name="the side panel is left-aligned and can stack at 260px",
         on=B2_BIO, sel=".ks3-tri-side",
         props={"text-align": "left", "min-width": "260px"}),
    # The arrangement is the line a student writes down, so it is display type
    # at the same 30px the bar variant's result takes — one reading treatment
    # across both shapes of the same component, or a student meeting both
    # would read them as two different kinds of statement.
    dict(name="the covered cell's arrangement is 30px display type",
         on=B2_BIO, sel='.ks3-tri-result:not([hidden])',
         props={"font-size": "30px", "font-weight": "800",
                "color": "#221E1B"}),
    # ⚠️ THE ROW'S NOTE IS A BARE PARAGRAPH. b1-02's is an inset panel on a
    # 2px ink border, and that rule is still in the stylesheet above this one
    # — this row is what proves the override reaches, because a box around one
    # of five stacked blocks in a column reads as a callout rather than as the
    # sentence explaining the line above it.
    dict(name="the row variant's sentence is not the inset panel",
         on=B2_BIO, sel='.ks3-tri-note:not([hidden])',
         props={"border-top-width": "0px", "padding-top": "0px",
                "font-size": "19px"}),
    # The balanced condition, set apart. It is the statement that makes every
    # question on the page solvable, and it is deliberately NOT the 18px
    # ink-body the rule line above it takes.
    dict(name="the balanced condition is set apart in display type",
         on=B2_BIO, sel=".ks3-tri-condition",
         props={"font-family": "Bricolage Grotesque", "font-size": "21px",
                "font-weight": "700"}),
# ── PAGE CONSTANT ────────────────────────────────────────────────────────
# One drawn instance, on b2-04.
#
#     B2_BIO = "biology/movement-skeleton-and-muscles/biomechanics-forces-in-the-body.html"


# ── COMPONENTS entries ───────────────────────────────────────────────────
# Mutation-tested: each rule was deliberately broken in shared/ks3.css and the
# row confirmed to fail before it was kept.

    # ── lever-steps (b2-04 #s-build) ──
    #
    # ⚖️ THE TWO MRB-204 STEP-4 BLOCKS MUST LOOK THE SAME. This row's values
    # are `.ks3-pick-opt`'s, deliberately: c2-06 asks a chemistry student to
    # pick between three candidate equations and b2-04 asks a biology student
    # to do exactly that, and a student meeting both would otherwise read them
    # as two different kinds of task. If either drifts, this fails.
    dict(name="a candidate equation is left-aligned mono on the option border",
         on=B2_BIO, sel=".ks3-lstep-opt",
         props={"font-family": "DM Mono", "font-size": "16px",
                "text-align": "left", "min-height": "44px",
                "border-top-color": "#DDCFB6"}),
    # R3 lives in this row. The chosen pick takes the accent BORDER and tint
    # and nothing else — no green, no mark, no verdict — because only the
    # mastery ladder marks correctness. A regression that added `is-correct`
    # styling here would turn the whole page into a test.
    dict(name="a chosen equation is chosen, never correct", on=B2_BIO,
         drive="lsteps-committed",
         sel='.ks3-lstep-opt[aria-pressed="true"]',
         props={"border-top-color": "#E4572E",
                "background-color": "#FCE7DE"}),
    # ⚠️ THE MODEL ANSWER INVERTS TO INK inside a light block, and the chip is
    # ALERT rather than the accent the worked example upstairs uses. Two FIFA
    # sets on one page, same four letters, two grounds — and the accent does
    # not carry on ink, which is why the pair changes.
    dict(name="the model answer lands on ink with an alert chip", on=B2_BIO,
         drive="lsteps-opened", sel=".ks3-lstep-chip",
         props={"background-color": "#FFC53D", "color": "#221E1B",
                "width": "34px"}),
    # ⚖️ The closing line quotes the student's answer beside the worked one in
    # ordinary on-dark body copy — NOT a verdict colour. It is a comparison
    # the student makes, never a mark the page makes (R3 / MRB-196 R10).
    dict(name="the closing comparison is body copy, not a verdict", on=B2_BIO,
         drive="lsteps-opened", sel=".ks3-lstep-close",
         props={"color": "#E7DECE", "font-size": "19px"}),
# ── PAGE CONSTANT ────────────────────────────────────────────────────────
# One drawn instance, on b2-04.
#
#     B2_BIO = "biology/movement-skeleton-and-muscles/biomechanics-forces-in-the-body.html"


# ── COMPONENTS entries ───────────────────────────────────────────────────
# Mutation-tested: each rule was deliberately broken in shared/ks3.css and the
# row confirmed to fail before it was kept.

    # ── meter-compare (b2-04 #s-meters) ──
    #
    # ⚖️ THE READINGS ARE EVIDENCE, NOT SMALL PRINT. This row is the one that
    # matters pedagogically: 17px mono in ink-BODY, not a 13px muted caption.
    # Shrink them and the card teaches that the mean is the measurement and
    # the spread is a footnote, which is exactly the idea the closing band
    # exists to break — and it would be invisible to reading the CSS, because
    # a caption under a headline looks tidy.
    dict(name="the three readings are evidence, at readable mono", on=B2_BIO,
         drive="meters-ranked", sel=".ks3-meters-readings",
         props={"font-family": "DM Mono", "font-size": "17px",
                "color": "#3B342E"}),
    dict(name="the mean is the card's headline in display type", on=B2_BIO,
         drive="meters-ranked", sel=".ks3-meters-mean",
         props={"font-family": "Bricolage Grotesque", "font-size": "30px",
                "font-weight": "800"}),
    # A 2px INK border, not the `--ks3-option-border` the commit buttons take.
    # These cards are the measurements and the heavier rule is what separates
    # data from a control on the same cream ground.
    dict(name="a meter card is a card on ink, not on the option border",
         on=B2_BIO, drive="meters-ranked", sel=".ks3-meters-card",
         props={"border-top-color": "#221E1B", "border-top-width": "2px",
                "background-color": "#FFFCF5"}),
    # 34rem, Design's own measure. Three candidate orderings are read against
    # each other, and a full-width button on a 60rem column is a target the
    # eye has to travel to compare with the one above it.
    dict(name="the ranking options keep Design's 34rem measure", on=B2_BIO,
         sel=".ks3-meters-commit .ks3-options",
         props={"max-width": "544px"}),
    # ═══ END B2 ═══ rows
    # ═══ BEGIN B3 ═══ rows
# ── PAGE CONSTANT ────────────────────────────────────────────────────────
# One drawn instance, on b3-01. Splice the constant beside the other unit
# constants in ks3_parity.py.
#
#     B3_DIET = "biology/nutrition-and-digestion/a-balanced-diet.html"


# ── COMPONENTS entries ───────────────────────────────────────────────────
# Mutation-tested: each rule was deliberately broken in shared/ks3.css and the
# row confirmed to fail before it was kept.

    # ── band-commit (b3-01 #s-plate) ──
    #
    # ⚠️ THIS ROW EXISTS TO PROVE THE SPECIFICITY SCOPING, and it is the one
    # that would otherwise ship broken. The why panel is CREAM (`--ks3-ground`)
    # inside an ink-dark block, so its note has to resolve to `--ks3-ink`.
    # `.ks3-dark p` is (0,1,1) and a bare `.ks3-plate-note` is (0,1,0), so
    # unscoped the note loses and paints `--ks3-on-dark-body` #E7DECE on cream
    # #FBF3E6 — a 1.1:1 sentence that is technically present and unreadable,
    # and invisible to anyone reading the stylesheet. Same defect class as B1's
    # zoom instrument and B2's muscle bench.
    # ⚖️ CORRECTED (MRB-228). One row asked the note for the PANEL's
    # background and resolved `rgba(0, 0, 0, 0)` — a paragraph has no ground of
    # its own. Split: the note's own claim is that it beats `.ks3-dark p`
    # (0,1,1) and stays ink; the panel's claim is the cream ground it sits on.
    dict(name="the why note is ink on the cream panel, not on-dark body",
         on=B3_DIET, drive="plate-opened", sel=".ks3-plate-note",
         props={"color": "#221E1B", "font-size": "18px"}),
    dict(name="the why panel is the page ground on an ink block",
         on=B3_DIET, drive="plate-opened", sel=".ks3-plate-why",
         props={"background-color": "#FBF3E6"}),
    # Design's dark segmented pair, identical to `.ks3-sim-seg-btn`'s: lit is
    # the alert yellow carrying INK text, resting is transparent on the muted
    # rule. ⚖️ Amber here is CHOSEN, never wrong — nothing in this instrument
    # marks a mistake, and this row pins the colour to the pressed state so a
    # later pass cannot quietly repurpose it.
    dict(name="a chosen band is alert with ink text", on=B3_DIET,
         drive="plate-opened", sel='.ks3-plate-band[aria-pressed="true"]',
         props={"background-color": "#FFC53D", "color": "#221E1B",
                "border-top-color": "#FFC53D", "min-height": "44px"}),
    # The row is the ONLY thing in the block that reports whether the student
    # had it, and it does so with the block's own lit rule rather than with a
    # marking colour. If this row ever resolves to `--ks3-ok` #12A150 or
    # `--ks3-ok-tint` #E4F7EB, an activity has started marking (R3).
    dict(name="a correctly placed row is the dark panel on an alert rule",
         on=B3_DIET, drive="plate-opened",
         sel='.ks3-plate-row[data-state="hit"]',
         props={"background-color": "#3E3730", "border-top-color": "#FFC53D",
                "border-top-width": "2px", "border-top-left-radius": "20px"}),
    # The verdict is the block's payoff and is set in display type, not body:
    # "3 of 7 in the right band." has to read as a headline or the three
    # branches under it read as a footnote to a number nobody noticed.
    dict(name="the verdict headline is display 800 on on-dark", on=B3_DIET,
         drive="plate-opened", sel=".ks3-plate-vhead",
         props={"font-family": "Bricolage Grotesque", "font-size": "27px",
                "font-weight": "800", "color": "#FBF3E6"}),
# ── PAGE CONSTANT ────────────────────────────────────────────────────────
# One drawn instance, on b3-04.
#
#     B3_WRONG = "biology/nutrition-and-digestion/when-diet-goes-wrong.html"


# ── COMPONENTS entries ───────────────────────────────────────────────────
# Every value below is read out of `shared/tokens.css`, not estimated:
#   --ks3-alert #FFC53D · --ks3-on-dark #FBF3E6 · --ks3-on-dark-muted #C6B9A7
#   --ks3-dark-panel #3E3730 · --ks3-ground #FBF3E6 · --ks3-ink #221E1B
#   --ks3-accent-text #A93411 · --ks3-r-panel 20px
# Mutation-tested: each rule was deliberately broken in shared/ks3.css and the
# row confirmed to fail before it was kept.

    # ── clinic-cases (b3-04 #s-cases) ──
    #
    # ⚠️ THE THREE ROWS BELOW ARE THE SPECIFICITY PROOF, and they are the
    # reason this instrument has a parity entry at all. `.ks3-dark p` is
    # (0,1,1); every bare class in the fragment is (0,1,0) and LOSES. Unscoped,
    # all three of these paragraphs resolve to `--ks3-on-dark-body` #E7DECE —
    # which is a plausible-looking panel and a broken one, and it is invisible
    # to reading the CSS.
    dict(name="the intake line is amber mono, not another sentence of prose",
         on=B3_WRONG, drive="clinic-diagnosed", sel=".ks3-clinic-intake",
         props={"font-family": "DM Mono", "font-size": "16px",
                "color": "#FFC53D"}),
    # ⚖️ THE VERDICT INVERTS. It sits on the CREAM ground inside an ink block,
    # so its paragraphs have to be pulled back to ink explicitly. Left to
    # `.ks3-dark p` they would paint #E7DECE on #FBF3E6 — 1.2:1, the answer
    # rendered invisible on the one panel that carries it.
    dict(name="the verdict panel inverts to the page ground", on=B3_WRONG,
         drive="clinic-diagnosed", sel=".ks3-clinic-verdict",
         props={"background-color": "#FBF3E6",
                "border-top-left-radius": "20px"}),
    dict(name="the answer is ink display type on that cream, not on-dark body",
         on=B3_WRONG, drive="clinic-diagnosed", sel=".ks3-clinic-answer",
         props={"font-family": "Bricolage Grotesque", "font-size": "26px",
                "font-weight": "800", "color": "#221E1B"}),
    # ⚖️ THE SPENT STATE IS THE ONLY THING THIS BLOCK PAINTS ABOUT THE ANSWER,
    # and it dims what was NOT chosen. R3: nothing marks correctness here, so
    # this row asserts a dim and there is deliberately no green/red row to
    # pair it with anywhere in this instrument.
    dict(name="after diagnosis the unticked imbalances dim, and nothing marks",
         on=B3_WRONG, drive="clinic-diagnosed",
         sel='.ks3-clinic-panel[data-open="1"] .ks3-clinic-pick[aria-pressed="false"]',
         props={"opacity": "0.45"}),
# ── PAGE CONSTANT ────────────────────────────────────────────────────────
# One drawn instance, on b3-06.
#
#     B3_ENZ = "biology/nutrition-and-digestion/enzymes-in-digestion.html"


# ── COMPONENTS entries ───────────────────────────────────────────────────
# Every value below is read out of `shared/tokens.css`, not estimated:
#   --ks3-alert #FFC53D · --ks3-ok #12A150 · --ks3-on-dark #FBF3E6
#   --ks3-on-dark-muted #C6B9A7 · --ks3-dark-panel #3E3730 · --ks3-ink #221E1B
#   --ks3-ground #FBF3E6 · --ks3-r-panel 20px
# Mutation-tested: each rule was deliberately broken in shared/ks3.css and the
# row confirmed to fail before it was kept.

    # ── enzyme-run (b3-06 #s-bench) ──
    #
    # ⚠️ THE TWO DIAL FIGURES ARE THE SPECIFICITY PROOF. `.ks3-dark p` is
    # (0,1,1) and a bare `.ks3-erun-rate` is (0,1,0): unscoped, the rate and
    # the temperature resolve to `--ks3-on-dark-body` #E7DECE and stop reading
    # as instrument readings at all. That is invisible to reading the CSS and
    # obvious in a browser, which is exactly why it is a gate row.
    dict(name="the rate reads as an instrument figure, in amber mono",
         on=B3_ENZ, sel=".ks3-erun-rate",
         props={"font-family": "DM Mono", "font-size": "16px",
                "color": "#FFC53D"}),
    dict(name="the temperature figure takes the same treatment", on=B3_ENZ,
         sel=".ks3-erun-tempvalue",
         props={"font-family": "DM Mono", "font-size": "21px",
                "color": "#FFC53D"}),
    # ⚖️ THE COUNTER THAT NEVER MOVES HAS TO LOOK DIFFERENT FROM THE TWO THAT
    # DO, and this row is the one that matters pedagogically. The fixed bar
    # carries BOTH `.ks3-erun-bar` and `.ks3-erun-bar-fixed`, so the ink-scoped
    # sibling rule at (0,2,0) beats an unscoped `-fixed` at (0,1,0) and the
    # enzyme counter renders in the same muted grey as the substrate — three
    # identical bars, and the whole argument of the block invisible.
    #
    # ⚑ THE VALUE ITSELF IS FLAGGED FOR MIDE. `--ks3-ok` is documented in
    # tokens.css as the ladder's correctness green, and this is a bar meaning
    # "unchanged" on a block that marks nothing. Design drew it and it is
    # reproduced as drawn; this row is what makes the day it is re-ruled a
    # loud one. Same handling as `scale-cards`' amber distance label.
    dict(name="the enzyme counter's bar keeps Design's green on ink",
         on=B3_ENZ, sel=".ks3-erun-bar-fixed",
         props={"background-color": "#12A150"}),
    # ⚖️ THE VERDICT INVERTS. It sits on the cream ground inside an ink block,
    # so its text has to be pulled back to ink explicitly; left to
    # `.ks3-dark p` it paints #E7DECE on #FBF3E6 at about 1.2:1 — the answer
    # rendered invisible on the one panel that carries it.
    dict(name="the verdict panel inverts to cream and reads in ink",
         on=B3_ENZ, drive="erun-denatured", sel=".ks3-erun-verdict",
         props={"background-color": "#FBF3E6", "color": "#221E1B",
                "border-top-left-radius": "20px"}),
# ── PAGE CONSTANT ────────────────────────────────────────────────────────
# One drawn instance, on b3-07. Splice the constant beside the other unit
# constants in ks3_parity.py, inside the B3 group.
#
#     B3_VILLUS = "biology/nutrition-and-digestion/absorption-and-the-small-intestine.html"


# ── COMPONENTS entries ───────────────────────────────────────────────────
# Mutation-tested: each rule was deliberately broken in shared/ks3.css and the
# row confirmed to fail before it was kept. Every hex below is read out of
# shared/tokens.css, not estimated.

    # ── fold-builder (b3-07 #s-fold) ──
    #
    # ⚠️ THIS ROW EXISTS TO PROVE THE SPECIFICITY SCOPING. `.ks3-dark p` is
    # (0,1,1) and a bare `.ks3-fold-note` is (0,1,0), so unscoped the note
    # loses and takes the BLOCK's on-dark body copy instead of the PANEL's.
    # Here the two happen to resolve to the same token, which is exactly what
    # makes it dangerous: the defect would be invisible to reading and to the
    # eye, and would surface the first time the panel's treatment moved. The
    # row pins the panel's own value so the cascade is asserted rather than
    # assumed.
    dict(name="the area note is the panel's body copy, not the block's",
         on=B3_VILLUS, sel=".ks3-fold-note:not([hidden])",
         props={"color": "#E7DECE", "font-size": "19px",
                "font-family": "Instrument Sans"}),
    # The readout is the block's payoff and the number is MONO, not display
    # type: it changes six times while a student watches, and a proportional
    # face would make it jump on every toggle. Alert amber on the dark panel
    # is a value being reported, never a mistake being marked.
    dict(name="the area readout is mono alert on a dark panel", on=B3_VILLUS,
         sel=".ks3-fold-area",
         props={"font-family": "DM Mono", "font-size": "26px",
                "color": "#FFC53D"}),
    dict(name="the readout sits on the nested dark panel at card radius",
         on=B3_VILLUS, sel=".ks3-fold-readout",
         props={"background-color": "#3E3730",
                "border-top-left-radius": "22px"}),
    # ⚖️ THE ROW THAT MATTERS PEDAGOGICALLY. The bar is amber while the model
    # is part-built and green only when all three levels are on — and green
    # here is "this is the finished thing", not "you were right": there is no
    # question in this block and nothing to be right about. If this ever
    # resolves to `--ks3-ok` #12A150 at a count below three, the instrument has
    # started congratulating a student for a state, which is the first step
    # towards an activity that marks (R3).
    dict(name="the bar turns green only with all three levels on",
         on=B3_VILLUS, drive="fold-all-on", sel=".ks3-fold-bar",
         props={"background-color": "#12A150"}),
# ── PAGE CONSTANT ────────────────────────────────────────────────────────
# One drawn instance, on b3-05.
#
#     B3_GUT = "biology/nutrition-and-digestion/the-digestive-system.html"


# ── COMPONENTS entries ───────────────────────────────────────────────────
# Every value below is read out of `shared/tokens.css`, not estimated:
#   --ks3-alert #FFC53D · --ks3-on-dark #FBF3E6 · --ks3-on-dark-muted #C6B9A7
#   --ks3-on-dark-body #E7DECE · --ks3-dark-panel #3E3730 · --ks3-ink #221E1B
#   --ks3-ground #FBF3E6 · --ks3-r-card 22px · --ks3-r-panel 20px
# Mutation-tested: each rule was deliberately broken in shared/ks3.css and the
# row confirmed to fail before it was kept.

    # ── gut-journey (b3-05 #s-journey) ──
    #
    # ⚖️ THE TIME TILE IS THE QUANTITY THE WHOLE BLOCK ARGUES FROM, and this
    # row is the one that matters pedagogically: 23px mono at weight 500,
    # against the 18px/700 the other two tiles take. Level the three and the
    # panel reads as three equal facts, which is precisely how "four hours in
    # the stomach, sixteen in the small intestine" gets missed — and it would
    # be invisible to reading the CSS, because three matching tiles look tidy.
    dict(name="the time tile is larger mono, not one fact of three",
         on=B3_GUT, sel='.ks3-gut-tile[data-tile="time"] .ks3-gut-tilevalue',
         props={"font-family": "DM Mono", "font-size": "23px",
                "color": "#FBF3E6"}),
    dict(name="the other two tiles stay 18px body weight", on=B3_GUT,
         sel='.ks3-gut-tile[data-tile="absorbs"] .ks3-gut-tilevalue',
         props={"font-family": "Instrument Sans", "font-size": "18px",
                "font-weight": "700", "color": "#FBF3E6"}),
    # ⚠️ SPECIFICITY. The note sits on the CREAM ground inside an ink block, so
    # it must be pulled back to ink at (0,2,0). `.ks3-dark p` is (0,1,1) and a
    # bare `.ks3-gut-note` is (0,1,0): unscoped it paints #E7DECE on #FBF3E6 at
    # about 1.2:1 — seven invisible paragraphs, one per stop.
    dict(name="the worth-knowing note inverts to cream and reads in ink",
         on=B3_GUT, sel=".ks3-gut-note",
         props={"background-color": "#FBF3E6", "color": "#221E1B",
                "font-size": "18px"}),
    # ⚖️ THE LIT ROW IS THE ONLY THING THE RUNTIME MOVES ON THIS CHART. The
    # width is inline from the Python; if this row ever fails, the highlight
    # has been re-implemented somewhere that can also touch the width.
    dict(name="the chart lights the current organ's bar in amber", on=B3_GUT,
         drive="gut-stomach", sel='.ks3-gut-row[data-lit="1"] .ks3-gut-bar',
         props={"background-color": "#FFC53D"}),
# ── PAGE CONSTANT ────────────────────────────────────────────────────────
# One drawn instance, on b3-08. Splice the constant beside the other unit
# constants in ks3_parity.py, inside the B3 group.
#
#     B3_BACTERIA = "biology/nutrition-and-digestion/bacteria-in-the-gut.html"


# ── COMPONENTS entries ───────────────────────────────────────────────────
# Mutation-tested: each rule was deliberately broken in shared/ks3.css and the
# row confirmed to fail before it was kept. Every hex below is read out of
# shared/tokens.css, not estimated.

    # ── job-switch (b3-08 #s-jobs) ──
    #
    # ⚠️ THE ROW THAT WOULD OTHERWISE SHIP BROKEN, and the only one in this
    # unit where the failure is total rather than subtle. The consequence
    # paragraph is CREAM (`--ks3-ground`) inside an ink-dark block, so its text
    # has to resolve to `--ks3-ink`. `.ks3-dark p` is (0,1,1) and a bare
    # `.ks3-jobsw-without` is (0,1,0): unscoped it paints `--ks3-on-dark-body`
    # #E7DECE on #FBF3E6, which is 1.1:1 — the sentence is in the DOM, is
    # correct, and cannot be read. Invisible to reading the stylesheet, and
    # the same defect class as B1's zoom instrument and B2's muscle bench.
    dict(name="the consequence is ink on the cream panel, not on-dark body",
         on=B3_BACTERIA, drive="jobs-one-off", sel=".ks3-jobsw-without",
         props={"color": "#221E1B", "background-color": "#FBF3E6",
                "font-size": "18px"}),
    # ⚖️ THE GROUND INVERTS, and it is the opposite way round from b3-07's
    # fold builder one lesson earlier. A job STILL BEING DONE sits on the
    # nested dark panel — it is a working part of the system. This row pins
    # the resting state so a later tidy-up cannot align the two instruments
    # and destroy the distinction.
    dict(name="a job still being done sits on the dark panel", on=B3_BACTERIA,
         sel=".ks3-jobsw-job",
         props={"background-color": "#3E3730",
                "border-top-left-radius": "20px",
                "border-top-width": "2px"}),
    # Switched off, the row loses the panel and gains the alert rule. Amber
    # marks a part that has been REMOVED, never a student who was wrong (§8),
    # and if this ever resolves to `--ks3-ok` #12A150 or `--ks3-ok-tint`
    # #E4F7EB an experiment has started marking (R3).
    dict(name="a switched-off job falls back to bare ink on an alert rule",
         on=B3_BACTERIA, drive="jobs-one-off", sel='.ks3-jobsw-job[data-off="1"]',
         props={"border-top-color": "#FFC53D", "border-top-width": "2px"}),
    # The payoff is a HEADLINE and is set in display type. As body copy it
    # would read as a sixth consequence rather than as the conclusion drawn
    # from all five — and the sentence it carries is the one the lesson is
    # built to deliver.
    dict(name="the germ-free-mouse payoff is a display headline", on=B3_BACTERIA,
         drive="jobs-all-off", sel=".ks3-jobsw-allhead",
         props={"font-family": "Bricolage Grotesque", "font-weight": "800",
                "font-size": "26px", "color": "#FBF3E6"}),
# ── PAGE CONSTANT ────────────────────────────────────────────────────────
# One drawn instance, on b3-03.
#
#     B3_ENERGY = "biology/nutrition-and-digestion/energy-in-food-and-what-you-need.html"


# ── COMPONENTS entries ───────────────────────────────────────────────────
# Mutation-tested: each rule was deliberately broken in shared/ks3.css and the
# row confirmed to fail before it was kept.

    # ── person-ledger (b3-03 #s-ledger) ──
    #
    # ⚠️ THE ROW THAT WOULD OTHERWISE SHIP BROKEN. The match panel is CREAM
    # inside an ink-dark block, so its copy has to resolve to `--ks3-ink`.
    # `.ks3-dark p` is (0,1,1) and a bare `.ks3-ledger-mwhy` is (0,1,0):
    # unscoped it paints #E7DECE on #FBF3E6, and the sentence lost is
    # *"Now switch person without changing the food"* — the one NOTES-B3 §3.3
    # names as the thing that must not be lost, because without it a match
    # reads as having finished.
    # ⚖️ CORRECTED (MRB-228) — see the note in band-commit.parity.py. The
    # background belongs to `.ks3-ledger-match`, not to the paragraph in it.
    dict(name="the match copy is ink on the cream panel", on=B3_ENERGY,
         drive="ledger-matched", sel=".ks3-ledger-mwhy",
         props={"color": "#221E1B", "font-size": "18px"}),
    dict(name="the match panel is the page ground on an ink block",
         on=B3_ENERGY, drive="ledger-matched", sel=".ks3-ledger-match",
         props={"background-color": "#FBF3E6"}),
    # ⚖️ THE MATCHED BAR IS NOT GREEN, AND THAT IS THE POINT. `--ks3-ok`
    # #12A150 is the ladder's colour for a correct answer and a plate is not an
    # answer; the bar reports a measurement. If this row ever resolves to
    # #12A150 or #E4F7EB the block has started marking (R3), and it would look
    # like an improvement.
    dict(name="a matched day reads as on target, never as correct",
         on=B3_ENERGY, drive="ledger-matched", sel='.ks3-ledger-fill[data-state="matched"]',
         props={"background-color": "#2F5CE0"}),
    # The running total is the block's headline number and is mono, not
    # display: it is a quantity being watched change, and setting it in the
    # display face would make it read as a conclusion.
    dict(name="the running total is readable mono, not display", on=B3_ENERGY,
         drive="ledger-matched", sel=".ks3-ledger-total",
         props={"font-family": "DM Mono", "font-size": "22px",
                "color": "#FBF3E6"}),
    # A food with portions on it takes the same lit treatment as a chosen tab —
    # alert on ink — because adding a portion IS a selection. Pinned so the two
    # cannot drift into two different "on" colours in one block.
    dict(name="a food with portions on it takes the lit treatment",
         on=B3_ENERGY, drive="ledger-matched",
         sel='.ks3-ledger-food[data-count]:not([data-count="0"])',
         props={"background-color": "#FFC53D", "color": "#221E1B",
                "min-height": "44px"}),
# ── PAGE CONSTANT ────────────────────────────────────────────────────────
# One drawn instance, on b3-02.
#
#     B3_TESTS = "biology/nutrition-and-digestion/food-tests.html"


# ── COMPONENTS entries ───────────────────────────────────────────────────
# Mutation-tested: each rule was deliberately broken in shared/ks3.css and the
# row confirmed to fail before it was kept.

    # ── test-bench (b3-02 #s-bench) ──
    #
    # ⚠️ THE ROW THAT WOULD OTHERWISE SHIP BROKEN. The result panel is CREAM
    # inside an ink-dark block, so the honest note has to resolve to
    # `--ks3-ink`. `.ks3-dark p` is (0,1,1) and a bare `.ks3-tbench-why` is
    # (0,1,0): unscoped it paints `--ks3-on-dark-body` #E7DECE on #FBF3E6 —
    # the four false-negative explanations, which are the entire point of the
    # lesson, present and unreadable.
    # ⚖️ CORRECTED (MRB-228) — see the note in band-commit.parity.py. The
    # background belongs to `.ks3-tbench-result`, not to the paragraph in it.
    dict(name="the honest note is ink on the cream result panel", on=B3_TESTS,
         drive="bench-run", sel=".ks3-tbench-why",
         props={"color": "#221E1B", "font-size": "18px"}),
    dict(name="the result panel is the page ground on an ink block",
         on=B3_TESTS, drive="bench-run", sel=".ks3-tbench-result",
         props={"background-color": "#FBF3E6"}),
    # ⚖️ THE CLAIM LINE IS RULED OFF, and the rule is load-bearing rather than
    # decorative: above it is what happened, below it is what the student may
    # write down. Losing the rule runs the observation and the licensed claim
    # together, which is precisely the slip the lesson exists to stop.
    dict(name="the claim line is ruled off from the explanation", on=B3_TESTS,
         drive="bench-run", sel=".ks3-tbench-claim",
         props={"border-top-color": "#E0D2B9", "border-top-width": "2px",
                "padding-top": "12px", "color": "#221E1B"}),
    # ⚖️ THE TUBE IS THE ONE PLACE IN THE KEY STAGE WHERE A COLOUR IS REAL.
    # This row asserts the tube's own frame comes from tokens while its FILL
    # does not — the fill is checked in the drive below, against the reagent's
    # authored hex. A token creeping onto the fill would tint an observation.
    dict(name="the tube frame is the muted rule, 62px wide", on=B3_TESTS,
         sel=".ks3-tbench-tube",
         props={"border-top-color": "#C6B9A7", "border-top-width": "3px",
                "width": "62px", "height": "168px"}),
    # Design's dark tab pair, shared with band-commit and person-ledger: lit is
    # alert with ink text, resting transparent on the muted rule.
    dict(name="a chosen bench tab is alert with ink text", on=B3_TESTS,
         sel='.ks3-tbench-tab[aria-pressed="true"]',
         props={"background-color": "#FFC53D", "color": "#221E1B",
                "min-height": "44px"}),
    # ═══ END B3 ═══ rows
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
    # ⊕ MRB-228 — the three repointed off the rebuilt c1-04. Cards moved to
    # c2-05 and the criteria number to b1-02, the pages that still render them.
    dict(name="card hint on card", on=C2_FORM,
         fg=".ks3-card-hint", bg=".ks3-card-btn", need=4.5),
    dict(name="card term on card", on=C2_FORM,
         fg=".ks3-card-front", bg=".ks3-card-btn", need=4.5),
    dict(name="criteria number on its tint", on=B1_MICRO,
         fg=".ks3-crit-num", bg=".ks3-crit-num", need=4.5),
    dict(name="self-rung heading on card", on=LESSON,
         fg='.ks3-rung[data-mode="self"] h3', bg=".ks3-ladder", need=4.5),
    dict(name="marked-rung heading on card", on=LESSON,
         fg='.ks3-rung[data-mode="marked"] h3', bg=".ks3-ladder", need=4.5),
    # ⊕ MRB-228 — the two ink-dark rows repointed to b1-02, which really does
    # render a sim on an ink-dark practical shell. The amber and light-card
    # rows are parked: no page renders those grounds, and pointing them at a
    # dark page would have them measure the wrong pair and pass or fail on it.
    dict(name="locked sim cover on amber block", on=LESSON,
         parked=_PARKED_NO_LIGHT_SIM,
         fg=".ks3-misconception .ks3-sim-cover",
         bg=".ks3-misconception .ks3-sim-cover", need=4.5),
    dict(name="locked sim cover on ink-dark block", on=B1_MICRO,
         fg=".ks3-practical .ks3-sim-cover",
         bg=".ks3-practical .ks3-sim-cover", need=4.5),
    dict(name="sim caption on ink-dark block", on=B1_MICRO,
         fg=".ks3-practical .ks3-sim-caption", bg=".ks3-practical", need=4.5),
    dict(name="sim caption on card", on=LESSON, parked=_PARKED_NO_LIGHT_SIM,
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
         parked=_PARKED_NO_REF_SLOT,
         fg=".ks3-ref-note", bg=".ks3-lesson-list", need=4.5),
    dict(name="cross-reference badge on its tint", on=UNIT_REF,
         parked=_PARKED_NO_REF_SLOT,
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
    # ⊕ MRB-228 — repointed to c2-05 with the other two card rows.
    dict(name="MARK card dog-ear on card", on=C2_FORM,
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


# The four ways `doneByDom()` in shared/ks3.js can decide a section is
# complete, in its order of precedence. Kept as a table rather than prose
# because the assertion below is only worth anything if it agrees with the
# runtime exactly, and the runtime is the thing that can change underneath it.
_DONE_SIGNALS = (
    ('data-stage-done', 'declares its own completion'),
    ('class="ks3-rung', 'is a ladder — every rung answered or self-checked'),
    ('data-reveal', 'has a reveal that can be opened'),
    ('ks3-reveal-btn', 'has a reveal button that can be expanded'),
    ('class="ks3-option', 'has an option a student can press'),
)


def check_rail_reachable(ks3_root):
    """⊕ MRB-228 (ruling R2) — every rail stage can actually REACH done.

    `done_when` is authored on every rail stage of every lesson, serialised
    into `data-rail-stages`, and read by NOTHING: the runtime decides
    completion from `data-stage-done` and then from the DOM heuristics in
    `doneByDom()`. R2 ruled that the field becomes load-bearing in the GATE
    rather than in the runtime — re-deriving completion from a declared string
    would change ticking behaviour on lessons that are live and in front of
    students, to fix something invisible to them.

    So this is what "wired" has to mean for the field to be worth authoring.
    Two assertions, both read out of the BUILT page:

    1. A stage must DECLARE a `done_when`. A blank one is an author saying
       nothing about a stage that has to be completable.
    2. The section it points at must carry at least one of the signals
       `doneByDom()` actually looks for. A section with none of them can never
       tick, no matter what the student does — MRB-208 says the rail is
       completion-based, so a stop that cannot complete is a rail that lies.

    `check_rail_anchors` already proves the anchor names a real element. This
    proves the element can finish. The two together are what stop a rail stop
    being decorative, which is exactly the defect the C1 payload map found on
    Design's own pages: c1-05's `#s-scale` is three static cards and two
    paragraphs and ticks on the PREVIOUS stage's state, and c1-02's `#s-matrix`
    does the same. Neither asks the student for anything.
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
        except ValueError:
            continue                      # check_rail_anchors owns this failure
        for st in stages:
            anchor = st.get("anchor")
            if not anchor:
                continue                  # ditto
            label = st.get("short") or anchor
            total += 1

            if not (st.get("done_when") or "").strip():
                problems.append(
                    "%s: rail stop %r declares no done_when — every stop has to "
                    "name the condition that completes it" % (name, label))

            # The section's own markup, from its id to the start of the next
            # top-level section. Cheap, and it does not need a parser: the
            # question is only whether a signal appears inside this section.
            start = html.find('id="%s"' % anchor)
            if start < 0:
                continue                  # check_rail_anchors owns this too
            nxt = html.find('<section', start + 1)
            body = html[start:nxt if nxt > 0 else len(html)]

            if not any(sig in body for sig, _why in _DONE_SIGNALS):
                problems.append(
                    "%s: rail stop %r (#%s) carries none of the signals "
                    "doneByDom() reads, so it can never tick. It is either a "
                    "section that must gain a demand, or a section that must "
                    "come off the rail." % (name, label, anchor))
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

    # ── B2 · Movement (⊕ MRB-220) ──
    #
    # Four states that exist only after a student does something. Each is
    # reached the way a student reaches it — through the instrument's own
    # control — so a regression in the interaction path fails HERE instead of
    # being measured around.

    # One row decided. Produces three states in one document: the row's ink
    # border, the chosen option, and the spent siblings.
    "jobsort-decided": r"""
(function () {
  var row = document.querySelector('.ks3-jobsort-item');
  if (!row) { return "no job-sort row on the page"; }
  var opt = row.querySelector('.ks3-jobsort-opt');
  if (!opt) { return "job-sort row offers no options"; }
  opt.click();
  if (row.getAttribute('data-open') !== '1') {
    return "row did not open after its option was clicked";
  }
  return "";
})()
""",
    # All four parts switched off, which is the only way the closing band
    # exists at all.
    "switch-thrown": r"""
(function () {
  var wrap = document.querySelector('[data-switch-block]');
  if (!wrap) { return "no system-switch on the page"; }
  var tabs = wrap.querySelectorAll('.ks3-switch-tab');
  for (var i = 0; i < tabs.length; i++) {
    tabs[i].click();
    var p = wrap.querySelector('.ks3-switch-panel:not([hidden])');
    p.querySelector('.ks3-option').click();
    p.querySelector('[data-switch]').click();
  }
  if (document.querySelector('[data-switch-all]').hasAttribute('hidden')) {
    return "all four parts switched off and the closing band is still hidden";
  }
  return "";
})()
""",
    # C6's commit gate. The bench does not exist in the document's layout
    # until it is answered, so every bench measurement needs this first.
    "bench-gate-opened": r"""
(function () {
  var gate = document.querySelector('[data-benchgate]');
  if (!gate) { return "no commit gate on the page"; }
  var opt = gate.querySelector('.ks3-option');
  if (!opt) { return "commit gate offers no options"; }
  opt.click();
  if (!gate.hasAttribute('hidden')) { return "gate did not disappear"; }
  var body = document.querySelector('[data-benchbody]');
  if (!body || body.hasAttribute('hidden')) {
    return "bench did not appear after the gate was answered";
  }
  return "";
})()
""",
    # ── C2 · Atoms, elements and compounds (⊕ MRB-220) ──
    #
    # Each state reached through the instrument's own control, so a regression
    # in the interaction path fails HERE rather than being measured around.

    # The gate opened AND the first claim switched off. Produces three states
    # in one document: the dimmed toggle, the inverted chip, and the two
    # observations that stop being explained.
    "claim-off": r"""
(function () {
  var gate = document.querySelector('[data-benchgate]');
  if (!gate) { return "no commit gate on the page"; }
  gate.querySelector('.ks3-option').click();
  var claim = document.querySelector('.ks3-claim');
  if (!claim) { return "no claim toggle on the page"; }
  claim.click();
  if (claim.getAttribute('aria-pressed') !== 'false') {
    return "the claim is still on after its toggle was clicked";
  }
  if (!document.querySelector('.ks3-obs-row[data-dead="1"]')) {
    return "a claim is off and no observation stopped being explained";
  }
  return "";
})()
""",
    # One test bought out of the budget of eight. Produces the result card
    # and the spent-button state in one document.
    "budget-test-spent": r"""
(function () {
  var gate = document.querySelector('[data-benchgate]');
  if (gate) { gate.querySelector('.ks3-option').click(); }
  var panel = document.querySelector('.ks3-sample:not([hidden])');
  if (!panel) { return "no sample panel on the page"; }
  var btn = panel.querySelector('.ks3-test-btn');
  if (!btn) { return "the sample offers no tests"; }
  btn.click();
  if (!btn.hasAttribute('disabled')) {
    return "a test was bought and its button is still live";
  }
  if (!panel.querySelector('.ks3-result:not([hidden])')) {
    return "a test was bought and no result appeared";
  }
  return "";
})()
""",
    # A verdict given on one sample — the reveal that names it.
    "budget-verdict-given": r"""
(function () {
  var gate = document.querySelector('[data-benchgate]');
  if (gate) { gate.querySelector('.ks3-option').click(); }
  var panel = document.querySelector('.ks3-sample:not([hidden])');
  if (!panel) { return "no sample panel on the page"; }
  var v = panel.querySelector('.ks3-verdict-btn');
  if (!v) { return "the sample offers no verdict"; }
  v.click();
  if (panel.querySelector('[data-verdict-panel]').hasAttribute('hidden')) {
    return "a verdict was given and the sample was never named";
  }
  return "";
})()
""",
    # `#s-think`'s two-paragraph reveal, opened the way a student opens it.
    "think-committed": r"""
(function () {
  var sec = document.getElementById('s-think');
  if (!sec) { return "no #s-think on the page"; }
  var opt = sec.querySelector('.ks3-option');
  if (!opt) { return "#s-think offers no options"; }
  opt.click();
  var rev = sec.querySelector('[data-reveal]');
  if (!rev || rev.hasAttribute('hidden')) {
    return "the reveal is still hidden after a commitment";
  }
  return "";
})()
""",
    # ═══ BEGIN C1 ═══ drives
# ── DRIVES entries ───────────────────────────────────────────────────────
# Add to DRIVES. Each reaches its state through the instrument's OWN control,
# so a regression in the interaction path fails here rather than being measured
# around.

    # One handled case and one failing case, in a single document, so both
    # verdict grounds can be measured against each other.
    "ebench-judged": r"""
(function () {
  var ok = document.querySelector('.ks3-ebench-case[data-ok="1"]');
  var bad = document.querySelector('.ks3-ebench-case[data-ok="0"]');
  if (!ok || !bad) { return "need one handled and one failing case"; }
  ok.querySelector('.ks3-ebench-btn').click();
  bad.querySelector('.ks3-ebench-btn').click();
  if (ok.getAttribute('data-open') !== '1' || bad.getAttribute('data-open') !== '1') {
    return "a case did not open after its call was pressed";
  }
  return "";
})()
""",
    # All seven judged, which is the only way the tally panel exists at all.
    "ebench-all-judged": r"""
(function () {
  var cases = document.querySelectorAll('.ks3-ebench-case');
  if (!cases.length) { return "no evidence bench on the page"; }
  for (var i = 0; i < cases.length; i++) {
    cases[i].querySelector('.ks3-ebench-btn').click();
  }
  var panel = document.querySelector('[data-ebench-tally]');
  if (!panel || panel.hasAttribute('hidden')) {
    return "every case judged and the tally is still hidden";
  }
  return "";
})()
""",
# ── DRIVES entries ───────────────────────────────────────────────────────
# ⊕ This section SUPERSEDES the commented sketch in this file's header.
# Splice from here; the header copy is prose and is now out of date.
#
# ⚖️ THE TWO NAMES ARE TWO REAL STATES, and the rig separates them itself.
# `wireGapTestRig` keeps `choice` and `test` as independent variables:
# choosing unhides `[data-gap-rig]` and repaints an OPENING note, and only a
# test press sets `aria-pressed="true"`, swaps the note for an OUTCOME
# paragraph, and calls `markStage(sec, true)`. So `gap-answered` and
# `gap-tested` differ in three independent ways — the pressed attribute, which
# of the eight authored paragraphs is showing, and whether the rail stop has
# ticked — and neither name is a dressed-up copy of the other.

    # A claim has been made about the gap, and NO test has been run.
    #
    # This is what makes the three resting rows measurable at all: the caption,
    # the note wrapper and the test buttons all live inside `[data-gap-rig]`,
    # which the renderer emits `hidden` because the rig is not there to be
    # looked at until the student has said what it is going to show.
    #
    # ⚠️ THE EMPTY CHOICE, DELIBERATELY, AND THE REASON IS FIRST-MATCH.
    # `.ks3-gap-note p` is measured by `document.querySelector`, which takes
    # the first match — and the renderer emits `data-note="empty"` first. Only
    # the empty choice leaves THAT paragraph the one on screen; any filled
    # choice shows `data-note="filled"` instead and the row would be measuring
    # a display:none element and passing. `data-empty-choice` is read from the
    # markup, never assumed: it is positional, and the renderer validates it
    # against the choice list at build time for exactly that reason.
    #
    # The last guard is the one that keeps the pair honest — it asserts NO test
    # is lit, so the "at rest" row cannot silently start measuring a pressed
    # button and reporting it as the resting treatment.
    "gap-answered": r"""
(function () {
  var wrap = document.querySelector('[data-gap]');
  if (!wrap) { return "no gap rig on the page"; }
  var opts = wrap.querySelectorAll('.ks3-option');
  if (!opts.length) { return "the rig offers no choices"; }
  var empty = parseInt(wrap.getAttribute('data-empty-choice'), 10);
  if (isNaN(empty) || empty < 0 || empty >= opts.length) {
    return "the rig declares no usable empty choice (data-empty-choice=" +
           wrap.getAttribute('data-empty-choice') + ")";
  }
  opts[empty].click();
  var rig = wrap.querySelector('[data-gap-rig]');
  if (!rig || rig.hasAttribute('hidden')) {
    return "a choice was made and the rig never appeared";
  }
  if (!wrap.querySelector('.ks3-gap-caption')) {
    return "the rig opened with no control caption";
  }
  var p = wrap.querySelector('.ks3-gap-note p');
  if (!p) { return "the rig opened with no outcome paragraph at all"; }
  if (p.hasAttribute('hidden')) {
    return "the rig opened and its first outcome paragraph is still hidden";
  }
  if (wrap.querySelector('.ks3-gap-test[aria-pressed="true"]')) {
    return "a test is already running, so the resting-test row would not be resting";
  }
  return "";
})()
""",
    # A test is ON THE BENCH — the state the amber row measures.
    #
    # The choice is one that FILLS the gap, found by walking the list for the
    # first index that is not `data-empty-choice` rather than by assuming a
    # position. That lands the test on its `off` outcome, which is the whole
    # argument of the block: every wrong answer fails all three tests. The
    # amber is not a verdict on the student — it marks which test is running,
    # and the outcome paragraph is one tone whichever answer they gave.
    #
    # The stage check is the second, independent proof that a test really ran:
    # `markStage` only fires from the test handler, never from the choice
    # handler, so a regression that lit the button without repainting would
    # still fail here. The section is found by `closest('[data-gapblock]')`
    # rather than by its `#s-gap` id, so re-anchoring the lesson cannot turn
    # this into a silent pass.
    "gap-tested": r"""
(function () {
  var wrap = document.querySelector('[data-gap]');
  if (!wrap) { return "no gap rig on the page"; }
  var opts = wrap.querySelectorAll('.ks3-option');
  if (!opts.length) { return "the rig offers no choices"; }
  var empty = parseInt(wrap.getAttribute('data-empty-choice'), 10);
  if (isNaN(empty)) {
    return "the rig declares no empty choice, so a filled gap cannot be chosen";
  }
  var pick = null;
  for (var i = 0; i < opts.length; i++) {
    if (i !== empty) { pick = opts[i]; break; }
  }
  if (!pick) { return "the rig offers no choice that fills the gap"; }
  pick.click();
  var t = wrap.querySelector('.ks3-gap-test');
  if (!t) { return "the rig offers no tests"; }
  t.click();
  if (t.getAttribute('aria-pressed') !== 'true') {
    return "a test was run and its button never lit";
  }
  var sec = wrap.closest('[data-gapblock]');
  if (!sec) { return "the rig is not inside a gap block"; }
  if (sec.getAttribute('data-stage-done') !== '1') {
    return "a test was run and the stage never completed";
  }
  return "";
})()
""",
# ── DRIVES entries ───────────────────────────────────────────────────────
# ⊕ This section SUPERSEDES the commented sketch in this file's header (§2).
# Splice from here; the header copy is prose and is now out of date.

    # The floor, reached through 24 real halvings.
    #
    # Two gates stand between a fresh load and the only row that needs this
    # drive (`.ks3-cut-value [data-verdict="floor"]`). First C6's commit gate,
    # which removes the bench from the document's layout until it is answered —
    # the same gate `bench-gate-opened` opens, re-opened here because a drive
    # gets its own fresh load and inherits nothing. Then the cutting itself:
    # the floor word is emit-both-show-one, so `[data-verdict="floor"]` is in
    # the markup from the first byte and stays `hidden` until n reaches FLOOR.
    # Measuring it without cutting would measure a display:none span and report
    # a pass, which is the absence-of-assertion failure this gate exists to
    # close.
    #
    # ⚠️ NOTHING IS COUNTED FROM THE OUTSIDE. FLOOR comes from `data-floor`
    # (24 today, and load-bearing — 1 cm / 2²⁴ is the 0.6 nm the ladder rung
    # quotes in words), and the steps come from the buttons' own `data-step`.
    # The loop takes the largest LIVE cut button each pass, so it holds if the
    # 10-step control is re-authored or removed; the smallest authored step is
    # 1, so FLOOR clicks is the worst case and FLOOR + 2 is a bound with room.
    # `data-act="cut"` excludes the undo control, which carries a step too and
    # would otherwise walk the piece back up the ladder.
    "cut-floor-reached": r"""
(function () {
  var gate = document.querySelector('[data-benchgate]');
  if (!gate) { return "no commit gate on the page"; }
  var opt = gate.querySelector('.ks3-option');
  if (!opt) { return "the commit gate offers no options"; }
  opt.click();
  var bench = document.querySelector('[data-cut]');
  if (!bench) { return "no halving bench on the page"; }
  if (bench.hasAttribute('hidden')) {
    return "the gate was answered and the bench is still hidden";
  }
  var floor = parseInt(bench.getAttribute('data-floor'), 10);
  if (!floor || floor < 1) {
    return "the bench declares no floor to cut down to (data-floor=" +
           bench.getAttribute('data-floor') + ")";
  }
  var cuts = [];
  var all = bench.querySelectorAll('.ks3-cut-btn[data-act="cut"]');
  for (var i = 0; i < all.length; i++) { cuts.push(all[i]); }
  if (!cuts.length) { return "the bench offers no cut controls"; }
  cuts.sort(function (a, b) {
    return (parseInt(b.getAttribute('data-step'), 10) || 0) -
           (parseInt(a.getAttribute('data-step'), 10) || 0);
  });
  var out = bench.querySelector('[data-cut-out="count"]');
  if (!out) { return "the bench has no count readout to check"; }
  for (var pass = 0; pass < floor + 2; pass++) {
    if (parseInt(out.textContent, 10) >= floor) { break; }
    var moved = false;
    for (var j = 0; j < cuts.length; j++) {
      if (!cuts[j].hasAttribute('disabled')) {
        cuts[j].click();
        moved = true;
        break;
      }
    }
    if (!moved) { break; }
  }
  if (parseInt(out.textContent, 10) !== floor) {
    return "cutting stopped at " + out.textContent + " of " + floor;
  }
  if (!bench.querySelector('.ks3-cut-value [data-verdict="floor"]:not([hidden])')) {
    return "the floor was reached and the floor verdict is still hidden";
  }
  return "";
})()
""",
# ── DRIVES entry ─────────────────────────────────────────────────────────

    # The panel does not exist in the document's layout until an option is
    # pressed, so every panel measurement needs this first. Which option is
    # deliberately unspecified: under R3 all four render identically and open
    # the same panel, and `check_r3_runtime()` asserts that rather than
    # trusting it.
    "keyed-committed": r"""
(function () {
  var wrap = document.querySelector('[data-keyed]');
  if (!wrap) { return "no keyed-commit on the page"; }
  var opt = wrap.querySelector('.ks3-option');
  if (!opt) { return "keyed-commit offers no options"; }
  opt.click();
  var panel = wrap.querySelector('[data-reveal]');
  if (!panel || panel.hasAttribute('hidden')) {
    return "an option was pressed and the panel is still hidden";
  }
  if (!wrap.querySelector('.ks3-keyed-reply:not([hidden])')) {
    return "the panel opened with no reply showing";
  }
  return "";
})()
""",
# ── DRIVES entries ───────────────────────────────────────────────────────
# ⊕ This section SUPERSEDES the commented sketch in this file's header.
# Splice from here; the header copy is prose and is now out of date.

    # Two predictions in one document: one answered WRONGLY, so the shared
    # fallback note is on screen in its own tone, and one answered RIGHTLY, so
    # its panel takes the alert border. Both states reached through the
    # instrument's own buttons, so a regression in the interaction path fails
    # HERE rather than being measured around.
    #
    # ⚠️ THE ORDER IS LOAD-BEARING, AND IT IS THE OPPOSITE OF THE OBVIOUS ONE.
    # Both rows are measured with `document.querySelector`, which takes the
    # FIRST match in document order, and `.ks3-predict-note[data-tone="wrong"]`
    # carries no `:not([hidden])` — every panel emits both notes and hides one.
    # Answer panel 1 right and its wrong note stays `hidden`, so that row would
    # resolve to a display:none paragraph, still report a colour, and PASS
    # having measured nothing a student can see. Answering panel 1 wrong puts a
    # visible wrong note at the head of the document, and panel 2 right is then
    # the first `[data-right="1"]`. Both rows land on live elements.
    #
    # The answer index is read from each panel's own `data-answer` and matched
    # against the buttons' `data-i`, so re-authoring which option is correct —
    # or how many options there are — cannot quietly invert this.
    "prediction-answered": r"""
(function () {
  var panels = document.querySelectorAll('.ks3-predict');
  if (panels.length < 2) {
    return "need 2 predictions to hold both states at once, found " +
           panels.length;
  }
  function pick(panel, correct) {
    var want = parseInt(panel.getAttribute('data-answer'), 10);
    if (isNaN(want)) { return false; }
    var opts = panel.querySelectorAll('.ks3-predict-btn');
    for (var i = 0; i < opts.length; i++) {
      var idx = parseInt(opts[i].getAttribute('data-i'), 10);
      if ((idx === want) === correct) { opts[i].click(); return true; }
    }
    return false;
  }
  if (!pick(panels[0], false)) { return "no wrong option in prediction 1"; }
  if (!pick(panels[1], true)) { return "no correct option in prediction 2"; }
  if (panels[0].getAttribute('data-right') !== '0') {
    return "prediction 1 was answered wrongly and did not record it";
  }
  if (panels[1].getAttribute('data-right') !== '1') {
    return "prediction 2 was answered correctly and did not record it";
  }
  var note = panels[0].querySelector('.ks3-predict-note[data-tone="wrong"]');
  if (!note) { return "prediction 1 carries no wrong-answer note"; }
  if (note.hasAttribute('hidden')) {
    return "a prediction was answered wrongly and the shared note is still hidden";
  }
  return "";
})()
""",
# ── DRIVES entries ───────────────────────────────────────────────────────
# ⊕ This section SUPERSEDES the commented sketch in this file's header.
# Splice from here; the header copy is prose and is now out of date.

    # One card sorted CORRECTLY and one sorted WRONGLY, which is the only way
    # both card borders and the correction note exist in one document — and
    # measuring them together is the point, because the pair is a single rule
    # (accent when the word fits, plain ink when it does not) and a drift in
    # either half is a drift in the rule.
    #
    # The sorter is NOT one-shot — Design leaves every card open so a student
    # can change the word and follow the card — so the second click is a real
    # second card and never a re-press of the first. Card order matters for the
    # two verdict rows only in that each selector names its own `data-verdict`,
    # so first-match cannot cross over; the note row carries an explicit
    # `:not([hidden])`, which the right-sorted card's hidden wrong note is
    # correctly skipped by.
    #
    # Nothing is assumed about the choices. The answer is read from the card's
    # `data-answer` and matched against each option's `data-choice`, so a card
    # re-authored to answer the other way still drives correctly; `pick` simply
    # fails and says which card it could not sort.
    "sortcards-decided": r"""
(function () {
  var cards = document.querySelectorAll('.ks3-sortcards-card');
  if (cards.length < 2) {
    return "need 2 sort cards to hold both verdicts at once, found " +
           cards.length;
  }
  function pick(card, correct) {
    var want = card.getAttribute('data-answer');
    if (!want) { return false; }
    var opts = card.querySelectorAll('.ks3-sortcards-opt');
    for (var i = 0; i < opts.length; i++) {
      if ((opts[i].getAttribute('data-choice') === want) === correct) {
        opts[i].click();
        return true;
      }
    }
    return false;
  }
  if (!pick(cards[0], true)) { return "no matching option on card 1"; }
  if (!pick(cards[1], false)) { return "no other option on card 2"; }
  if (cards[0].getAttribute('data-verdict') !== 'right') {
    return "card 1 was sorted correctly and recorded " +
           cards[0].getAttribute('data-verdict');
  }
  if (cards[1].getAttribute('data-verdict') !== 'wrong') {
    return "card 2 was sorted wrongly and recorded " +
           cards[1].getAttribute('data-verdict');
  }
  if (!document.querySelector('.ks3-sortcards-note[data-note="wrong"]:not([hidden])')) {
    return "a card was sorted wrongly and its correction is still hidden";
  }
  return "";
})()
""",
    # ═══ END C1 ═══ drives
    # ═══ BEGIN B2 ═══ drives
# ── DRIVES entries ───────────────────────────────────────────────────────

    # Nothing inside the rig exists in the document's layout until the commit
    # gate is answered — `r_bench_gate` hides the whole body rather than
    # greying it, so every measurement above needs this first. Which gate
    # option is deliberately unspecified: under R3 all four render identically
    # and open the same instrument.
    "lever-opened": r"""
(function () {
  var sec = document.querySelector('[data-leverblock]');
  if (!sec) { return "no arm-lever on the page"; }
  var opt = sec.querySelector('[data-benchgate] .ks3-option');
  if (!opt) { return "the rig offers no commit gate"; }
  opt.click();
  var body = sec.querySelector('[data-lever]');
  if (!body || body.hasAttribute('hidden')) {
    return "the gate was answered and the rig is still hidden";
  }
  if (!body.querySelector('[data-lever-canvas]')) {
    return "the rig opened with no canvas in it";
  }
  return "";
})()
""",
    # ⚖️ THE WITHHELD NUMBER, ASSERTED RATHER THAN TRUSTED. This drive is what
    # stops the lesson being quietly deleted by a refactor: it proves the
    # force is unreadable before the meter, readable after it, and that the
    # canvas label follows the same gate — a screen-reader user must not be
    # handed the answer a sighted student has to work out.
    "lever-metered": r"""
(function () {
  var sec = document.querySelector('[data-leverblock]');
  if (!sec) { return "no arm-lever on the page"; }
  var opt = sec.querySelector('[data-benchgate] .ks3-option');
  if (opt) { opt.click(); }
  var body = sec.querySelector('[data-lever]');
  if (!body) { return "the rig never opened"; }
  var tile = body.querySelector('[data-lever-out="force"]');
  var canvas = body.querySelector('[data-lever-canvas]');
  if (!tile || !canvas) { return "the rig has no force tile or no canvas"; }
  var withheld = body.getAttribute('data-unmeasured');
  if (tile.textContent.trim() !== withheld.trim()) {
    return "the force tile reads " + tile.textContent + " before the meter was fitted";
  }
  // The distances legitimately carry digits, so the label is checked against
  // the MEASURED CLAUSE's own opening words rather than against "any number".
  if (body.getAttribute('data-alt-measured')
      && canvas.getAttribute('aria-label').indexOf(
           body.getAttribute('data-alt-measured').split('{force}')[0]) >= 0) {
    return "the canvas label carried the meter reading before the meter was fitted";
  }
  if (sec.getAttribute('data-stage-done') === '1') {
    return "the rail stop ticked before any control was moved";
  }
  var slider = body.querySelector('[data-lever-input="load"]');
  var tabs = body.querySelectorAll('[data-lever-tab="hand"]');
  if (!slider || tabs.length < 2) { return "the rig is missing its controls"; }
  slider.value = '4';
  slider.dispatchEvent(new Event('input', { bubbles: true }));
  tabs[1].click();
  var btn = body.querySelector('[data-lever-meter]');
  if (!btn) { return "the rig has no meter button"; }
  btn.click();
  if (!/\d/.test(tile.textContent)) {
    return "the meter was fitted and the force tile still has no number in it";
  }
  if (!btn.hasAttribute('disabled')) {
    return "the meter button is still live after being fitted — it is one-way";
  }
  if (sec.getAttribute('data-stage-done') !== '1') {
    return "two controls moved and the meter fitted, and the stop has not ticked";
  }
  return "";
})()
""",
# ── DRIVES entries ───────────────────────────────────────────────────────

    # ⚠️ NO DRIVE IS NEEDED FOR THE RESTING MEASUREMENT, and that is the
    # point of `covered`: b2-04 opens with F already covered, so the result
    # line, the sentence and the pressed button are all in their final state
    # in the built HTML before a single line of JS runs. The rows above
    # measure that page as delivered.
    #
    # This drive exists to prove the RADIO contract — that the control never
    # returns to an uncovered state, which is the one behaviour that differs
    # from b1-02 and the one a regression would restore by accident.
    "triangle-radio-held": r"""
(function () {
  var tri = document.querySelector('[data-triangle][data-cover-mode="radio"]');
  if (!tri) { return "no radio-mode triangle on the page"; }
  var start = tri.getAttribute('data-covered');
  if (!start) { return "a radio triangle opened with nothing covered"; }
  var btn = tri.querySelector('.ks3-tri-btn[data-cover="' + start + '"]');
  if (!btn) { return "no button for the covered cell " + start; }
  // Press the ALREADY-covered cell. A toggle would uncover here; a radio
  // must not, because an uncovered triangle asks the student nothing.
  btn.click();
  if (tri.getAttribute('data-covered') !== start) {
    return "pressing the covered cell uncovered it — the radio has become a toggle";
  }
  var other = tri.querySelector('.ks3-tri-btn:not([data-cover="' + start + '"])');
  if (!other) { return "the triangle offers only one cover"; }
  other.click();
  var now = other.getAttribute('data-cover');
  if (tri.getAttribute('data-covered') !== now) {
    return "pressing a second cell did not move the cover";
  }
  if (!tri.querySelector('.ks3-tri-result[data-result="' + now + '"]:not([hidden])')) {
    return "the cover moved and the arrangement line did not follow it";
  }
  if (!tri.querySelector('.ks3-tri-note[data-note="' + now + '"]:not([hidden])')) {
    return "the cover moved and the sentence did not follow it";
  }
  if (tri.querySelectorAll('.ks3-tri-result:not([hidden])').length !== 1) {
    return "more than one arrangement line is showing";
  }
  return "";
})()
""",
# ── DRIVES entries ───────────────────────────────────────────────────────

    # Two picks and a number with a unit — the three commitments the block
    # asks for. Which options are pressed is deliberately unspecified: under
    # R3 all three in a ladder render identically and none of them is marked.
    #
    # ⊕ THIS DRIVE IS ALSO THE RAIL CORRECTION'S ASSERTION. It fails if the
    # stop ticks before the third commitment — which is what Design's own
    # `buildOpen` predicate did, one tap after arriving.
    "lsteps-committed": r"""
(function () {
  var sec = document.querySelector('[data-lstepblock]');
  if (!sec) { return "no lever-steps on the page"; }
  var wrap = sec.querySelector('[data-lstep]');
  var btn = wrap.querySelector('[data-lstep-open]');
  var ans = wrap.querySelector('[data-lstep-ans]');
  var unit = wrap.querySelector('[data-lstep-unit]');
  if (!btn || !ans || !unit) { return "the block is missing a commitment control"; }
  if (sec.getAttribute('data-stage-done') === '1') {
    return "the stop ticked on load";
  }
  var g0 = wrap.querySelector('.ks3-lstep-opt[data-group="0"]');
  var g1 = wrap.querySelector('.ks3-lstep-opt[data-group="1"]');
  if (!g0 || !g1) { return "the block offers fewer than two pick ladders"; }
  g0.click();
  g1.click();
  if (sec.getAttribute('data-stage-done') === '1') {
    return "the stop ticked on two picks — the answer is the third commitment";
  }
  ans.value = '160';
  ans.dispatchEvent(new Event('input', { bubbles: true }));
  if (sec.getAttribute('data-stage-done') === '1') {
    return "the stop ticked on a number with no unit";
  }
  if (!btn.hasAttribute('disabled')) {
    return "the open button unlocked before a unit was chosen";
  }
  unit.value = 'N';
  unit.dispatchEvent(new Event('change', { bubbles: true }));
  if (sec.getAttribute('data-stage-done') !== '1') {
    return "all three lines committed and the stop has not ticked";
  }
  if (btn.hasAttribute('disabled')) {
    return "all three lines committed and the button is still locked";
  }
  return "";
})()
""",
    # The reveal panel does not exist in the document's layout until the
    # button is pressed, so every measurement inside it needs this. It also
    # asserts the LIVE COUPLING: the closing line has to quote the force the
    # rig implies, which is the block's whole claim to be the same problem.
    "lsteps-opened": r"""
(function () {
  var sec = document.querySelector('[data-lstepblock]');
  if (!sec) { return "no lever-steps on the page"; }
  var wrap = sec.querySelector('[data-lstep]');
  var g0 = wrap.querySelector('.ks3-lstep-opt[data-group="0"]');
  var g1 = wrap.querySelector('.ks3-lstep-opt[data-group="1"]');
  var ans = wrap.querySelector('[data-lstep-ans]');
  var unit = wrap.querySelector('[data-lstep-unit]');
  var btn = wrap.querySelector('[data-lstep-open]');
  if (!g0 || !g1 || !ans || !unit || !btn) { return "the block is incomplete"; }
  g0.click(); g1.click();
  ans.value = '160';
  ans.dispatchEvent(new Event('input', { bubbles: true }));
  unit.value = 'N';
  unit.dispatchEvent(new Event('change', { bubbles: true }));
  btn.click();
  var panel = wrap.querySelector('[data-reveal]');
  if (!panel || panel.hasAttribute('hidden')) {
    return "the three lines were committed, the button pressed, and the panel is still hidden";
  }
  if (!wrap.querySelector('.ks3-lstep-chip')) {
    return "the model answer opened with no steps in it";
  }
  var close = wrap.querySelector('[data-lstep-close]');
  if (!close || close.textContent.indexOf('160') < 0) {
    return "the closing line does not quote the student's own answer back";
  }
  if (/[{}]/.test(wrap.textContent)) {
    return "an unfilled template reached the page: " + wrap.textContent.slice(0, 120);
  }
  var locked = wrap.querySelector('.ks3-lstep-opt:not([disabled])');
  if (locked) {
    return "the model is on screen and a pick can still be changed";
  }
  return "";
})()
""",
# ── DRIVES entries ───────────────────────────────────────────────────────

    # The cards do not exist in the document's layout until an ordering is
    # committed, so every measurement above needs this. Which ordering is
    # deliberately unspecified: under R3 all three render identically and all
    # three open the same cards, and `check_r3_runtime()` asserts that rather
    # than trusting it.
    "meters-ranked": r"""
(function () {
  var sec = document.querySelector('[data-metersblock]');
  if (!sec) { return "no meter-compare on the page"; }
  var wrap = sec.querySelector('[data-meters]');
  var opt = wrap && wrap.querySelector('.ks3-option');
  if (!opt) { return "the block offers no ranking options"; }
  if (sec.getAttribute('data-stage-done') === '1') {
    return "the stop ticked on load";
  }
  opt.click();
  var panel = wrap.querySelector('[data-reveal]');
  if (!panel || panel.hasAttribute('hidden')) {
    return "an ordering was committed and the cards are still hidden";
  }
  if (wrap.querySelectorAll('.ks3-meters-card').length < 2) {
    return "the reveal opened with fewer than two groups to compare";
  }
  // ⚠️ ALL THE CARDS, NOT ONE. The commitment is about the ORDER of the
  // three, so revealing them a card at a time would answer part of the
  // question still being asked.
  if (wrap.querySelectorAll('.ks3-meters-card').length
      !== wrap.querySelectorAll('.ks3-meters-mean').length) {
    return "a card arrived without its mean";
  }
  if (sec.getAttribute('data-stage-done') !== '1') {
    return "an ordering was committed and the stop has not ticked";
  }
  // R3, asserted here as well as globally: a ranking is a commitment, not an
  // answer, so nothing may be marked or spent.
  if (wrap.querySelector('.ks3-option[data-correct], .ks3-option.is-correct, .ks3-option.is-wrong, .ks3-option[disabled]')) {
    return "a ranking option was marked or disabled — this block marks nothing";
  }
  return "";
})()
""",
    # ═══ END B2 ═══ drives
    # ═══ BEGIN B3 ═══ drives
# ── DRIVES entries ───────────────────────────────────────────────────────

    # Nothing measured above exists in the document's layout until all seven
    # rows are committed and the reveal is opened, so every row needs this.
    #
    # ⚠️ IT COMMITS THROUGH THE REAL CONTROLS. Seven `.click()`s on seven band
    # buttons and one on the reveal, exactly as a student would — never by
    # setting `data-state` or unhiding a panel, because a drive that reaches
    # the state by hand proves the stylesheet and nothing about the gate.
    #
    # Which band is deliberately unspecified: it presses the FIRST option in
    # every row, so on Design's payload some rows are right and some are wrong
    # and both `hit` and `miss` states exist to be measured.
    "plate-opened": r"""
(function () {
  var sec = document.querySelector('[data-plateblock]');
  if (!sec) { return "no band-commit on the page"; }
  var wrap = sec.querySelector('[data-plate]');
  if (!wrap) { return "the block drew no plate"; }
  if (sec.getAttribute('data-stage-done') === '1') {
    return "the stop ticked on load";
  }
  var rows = wrap.querySelectorAll('.ks3-plate-row');
  if (rows.length < 2) { return "fewer than two rows to commit"; }
  var open = wrap.querySelector('[data-plate-open]');
  if (!open) { return "the block offers no reveal"; }
  if (!open.disabled) {
    return "the reveal was open before anything was committed — the gate is the lesson";
  }
  // Commit every row but the last, and check the gate is still shut.
  for (var i = 0; i < rows.length; i++) {
    if (i === rows.length - 1) {
      if (!open.disabled) {
        return "the reveal unlocked with a row still uncommitted";
      }
    }
    var b = rows[i].querySelector('.ks3-plate-band');
    if (!b) { return "a row offers no bands"; }
    b.click();
  }
  if (open.disabled) {
    return "every row is committed and the reveal is still locked";
  }
  open.click();
  var verdict = wrap.querySelector('[data-plate-verdict]');
  if (!verdict || verdict.hasAttribute('hidden')) {
    return "the reveal was pressed and the verdict is still hidden";
  }
  if (!wrap.querySelector('.ks3-plate-why:not([hidden])')) {
    return "the verdict opened with no row explanation showing";
  }
  if (!verdict.querySelector('.ks3-plate-vwhy:not([hidden])')) {
    return "the verdict opened on none of its three branches";
  }
  if (verdict.querySelectorAll('.ks3-plate-vwhy:not([hidden])').length !== 1) {
    return "the verdict opened on more than one branch at once";
  }
  if (!wrap.querySelector('.ks3-plate-row[data-state="hit"]')
      && !wrap.querySelector('.ks3-plate-row[data-state="miss"]')) {
    return "no row reported whether it was placed correctly";
  }
  // R3, asserted here as well as globally: the band buttons are commitments,
  // not answers, so nothing on them may be marked.
  if (wrap.querySelector('.ks3-plate-band[data-correct], .ks3-plate-band.is-correct, .ks3-plate-band.is-wrong')) {
    return "a band button was marked — this block marks no control";
  }
  if (wrap.querySelector('svg.ks3-mark')) {
    return "a drawn tick or cross appears inside band-commit";
  }
  if (sec.getAttribute('data-stage-done') !== '1') {
    return "the answers are open and the stop has not ticked";
  }
  return "";
})()
""",
# ── DRIVES entries ───────────────────────────────────────────────────────

    # The verdict does not exist in the document's layout until a clinic has
    # been diagnosed, so every measurement above needs this. It reaches that
    # state through the instrument's OWN controls — a pick, then the reveal
    # button — and never by setting an attribute.
    "clinic-diagnosed": r"""
(function () {
  var sec = document.querySelector('[data-clinicblock]');
  if (!sec) { return "no clinic-cases on the page"; }
  if (sec.getAttribute('data-stage-done') === '1') {
    return "the stop ticked on load";
  }
  var wrap = sec.querySelector('[data-clinic]');
  var panel = wrap && wrap.querySelector('.ks3-clinic-panel:not([hidden])');
  if (!panel) { return "no clinic panel is showing"; }
  var picks = panel.querySelectorAll('.ks3-clinic-pick');
  var btn = panel.querySelector('[data-clinic-reveal]');
  if (picks.length < 2 || !btn) { return "the clinic offers no imbalances to tick"; }
  if (!btn.hasAttribute('disabled')) {
    return "the diagnosis was available before anything was ticked";
  }
  // ⚠️ TWO ticks, on one clinic, because the multi-select IS the instrument.
  // A single-select would drop the first when the second is pressed, and this
  // check would then catch it.
  picks[0].click();
  picks[1].click();
  if (panel.querySelectorAll('.ks3-clinic-pick[aria-pressed="true"]').length !== 2) {
    return "two imbalances were ticked and the block kept only one";
  }
  if (btn.hasAttribute('disabled')) {
    return "two imbalances are ticked and the diagnosis is still locked";
  }
  btn.click();
  var v = panel.querySelector('[data-reveal]');
  if (!v || v.hasAttribute('hidden')) {
    return "the diagnosis was opened and the verdict is still hidden";
  }
  if (!panel.querySelector('.ks3-clinic-answer') ||
      !panel.querySelector('.ks3-clinic-verdict-label')) {
    return "the verdict opened without its answer or its label";
  }
  // R3, asserted here as well as globally: nothing in this block marks.
  if (wrap.querySelector('.ks3-clinic-pick[data-correct], .ks3-clinic-pick.is-correct, .ks3-clinic-pick.is-wrong')) {
    return "an imbalance button was marked — this block marks nothing";
  }
  // One clinic of five, so the stop must NOT have ticked yet: the argument is
  // the five held against each other.
  if (sec.getAttribute('data-stage-done') === '1') {
    return "the stop ticked on one clinic of five";
  }
  return "";
})()
""",
# ── DRIVES entries ───────────────────────────────────────────────────────

    # ⚖️ THE DRIVE IS THE MISCONCEPTION, END TO END, and it reaches the state
    # through the instrument's OWN controls: drag the slider past the
    # threshold, drag it back to the optimum, run. Nothing here sets an
    # attribute, and every assertion is about what the bench then says.
    "erun-denatured": r"""
(function () {
  var sec = document.querySelector('[data-erunblock]');
  if (!sec) { return "no enzyme-run on the page"; }
  if (sec.getAttribute('data-stage-done') === '1') {
    return "the stop ticked on load";
  }
  var wrap = sec.querySelector('[data-erun]');
  var cfg;
  try { cfg = JSON.parse(wrap.getAttribute('data-cfg') || '{}'); }
  catch (err) { return "the bench carries no readable config"; }
  var slider = wrap.querySelector('[data-temp]');
  var runBtn = wrap.querySelector('[data-run]');
  var rate = wrap.querySelector('[data-rate]');
  if (!slider || !runBtn || !rate) { return "the bench has no dial or no run button"; }

  function setTemp(v) {
    slider.value = String(v);
    slider.dispatchEvent(new Event('input', { bubbles: true }));
  }

  // The third counter, read BEFORE anything happens. It is the one readout
  // nothing in the instrument may move, and it is checked again at the end.
  var fixed = wrap.querySelector('.ks3-erun-bar-fixed');
  var enzCell = wrap.querySelector('.ks3-erun-counter[data-counter="enzyme"] .ks3-erun-countervalue');
  if (!fixed || !enzCell) { return "the bench draws no enzyme counter"; }
  if (enzCell.hasAttribute('data-value')) {
    return "the enzyme counter has a runtime handle — it must have none";
  }
  var enzBefore = enzCell.textContent;
  var widthBefore = fixed.style.width || '';

  // 1. Above the threshold: the rate must fall to zero WITHOUT a run.
  setTemp(Number(cfg.denature_c) + 10);
  if (!/(^|\D)0(\D|$)/.test(rate.textContent)) {
    return "heated past the threshold and the rate is not zero";
  }
  if (!wrap.querySelector('.ks3-erun-tempnote[data-note="denatured_hot"]:not([hidden])')) {
    return "heated past the threshold and the hot-denatured note is not showing";
  }

  // 2. Cooled back to the optimum: STILL zero. This is the latch, and it is
  // the whole reason the instrument exists.
  setTemp(Number(cfg.optimum_c));
  if (!/(^|\D)0(\D|$)/.test(rate.textContent)) {
    return "cooling a denatured enzyme brought the rate back — the latch is broken";
  }
  if (!wrap.querySelector('.ks3-erun-tempnote[data-note="denatured_cool"]:not([hidden])')) {
    return "cooled after denaturing and the cool-denatured note is not showing";
  }

  // 3. Run it anyway: nothing is digested and the verdict says so.
  runBtn.click();
  var v = wrap.querySelector('[data-reveal]');
  if (!v || v.hasAttribute('hidden')) {
    return "a denatured run finished and no verdict appeared";
  }
  if (!wrap.querySelector('.ks3-erun-verdicttext[data-verdict="denatured"]:not([hidden])')) {
    return "a denatured run showed a verdict that was not the denatured one";
  }
  var prod = wrap.querySelector('[data-value="product"]');
  if (prod && !/(^|\D)0(\D|$)/.test(prod.textContent)) {
    return "a denatured enzyme produced something";
  }
  if (sec.getAttribute('data-stage-done') !== '1') {
    return "the reaction was run and the stop has not ticked";
  }

  // 4. The counter that never moves has not moved.
  if (enzCell.textContent !== enzBefore || (fixed.style.width || '') !== widthBefore) {
    return "the enzyme counter moved — it is the one readout nothing may touch";
  }
  // R3: nothing in this block marks correctness.
  if (wrap.querySelector('[data-correct], .is-correct, .is-wrong')) {
    return "a bench control was marked — this block marks nothing";
  }
  return "";
})()
""",
# ── DRIVES entries ───────────────────────────────────────────────────────

    # All three levels ON, through the instrument's own three buttons and
    # nothing else — no attribute is set by hand, so a regression in the
    # toggle path fails here rather than being stepped over.
    "fold-all-on": r"""
(function () {
  var sec = document.querySelector('[data-foldblock]');
  if (!sec) { return "no fold-builder on the page"; }
  var wrap = sec.querySelector('[data-fold]');
  if (!wrap) { return "the block has no fold-builder in it"; }
  if (sec.getAttribute('data-stage-done') === '1') {
    return "the stop ticked on load";
  }
  var bar = wrap.querySelector('[data-fold-bar]');
  if (!bar) { return "the readout has no bar"; }
  if (bar.getAttribute('data-full') === '1') {
    return "the bar was already full before any level was added";
  }
  var toggles = wrap.querySelectorAll('[data-fold-toggle]');
  if (toggles.length < 3) {
    return "the builder offers " + toggles.length + " levels, not three";
  }
  for (var i = 0; i < toggles.length; i++) { toggles[i].click(); }
  if (bar.getAttribute('data-full') !== '1') {
    return "every level is on and the bar has not filled";
  }
  // The note is indexed by the COUNT of levels, so the last one is the
  // finished model's. A note stuck at index 0 means emit-both-show-one has
  // stopped swapping and the student is reading about a plain tube.
  var shown = wrap.querySelector('.ks3-fold-note:not([hidden])');
  if (!shown) { return "no area note is showing"; }
  if (shown.getAttribute('data-note') !== String(toggles.length)) {
    return "the note showing is for " + shown.getAttribute('data-note')
      + " level(s), not " + toggles.length;
  }
  if (wrap.querySelectorAll('.ks3-fold-note:not([hidden])').length !== 1) {
    return "more than one area note is showing at once";
  }
  if (sec.getAttribute('data-stage-done') !== '1') {
    return "every level is on and the stop has not ticked";
  }
  // ⚖️ THE STOP LATCHES. Switching a level back off must leave the rail
  // alone — MRB-208 says a stop ticks when the activity is finished, and
  // nothing un-finishes it. The bar and the note are allowed to follow the
  // live state; the rail is not.
  toggles[0].click();
  if (sec.getAttribute('data-stage-done') !== '1') {
    return "the stop un-ticked when a level was switched back off";
  }
  toggles[0].click();
  // R3, asserted here as well as globally: three toggles are not answers, so
  // nothing in this instrument may be marked, spent or disabled.
  if (wrap.querySelector('.ks3-option, [data-correct], .is-correct, .is-wrong')) {
    return "the fold builder is marking something — this block asks no question";
  }
  return "";
})()
""",
# ── DRIVES entries ───────────────────────────────────────────────────────

    # Drives the journey to the STOMACH — stop three, and the one the lesson's
    # argument turns on. Reached through the instrument's own tab, never by
    # setting an attribute.
    "gut-stomach": r"""
(function () {
  var sec = document.querySelector('[data-gutblock]');
  if (!sec) { return "no gut-journey on the page"; }
  if (sec.getAttribute('data-stage-done') === '1') {
    return "the stop ticked on load";
  }
  var wrap = sec.querySelector('[data-gut]');
  var tabs = wrap ? wrap.querySelectorAll('.ks3-gut-tab') : [];
  if (tabs.length < 7) { return "the journey draws fewer than seven stops"; }
  var tab = wrap.querySelector('.ks3-gut-tab[data-stop="stomach"]');
  if (!tab) { return "the journey has no stomach stop"; }
  tab.click();
  var panel = wrap.querySelector('.ks3-gut-stop[data-stop="stomach"]');
  if (!panel || panel.hasAttribute('hidden')) {
    return "the stomach tab was pressed and its panel is still hidden";
  }
  if (wrap.querySelectorAll('.ks3-gut-stop:not([hidden])').length !== 1) {
    return "more than one stop panel is showing at once";
  }
  if (panel.querySelectorAll('.ks3-gut-tile').length !== 3) {
    return "a stop panel arrived without all three tiles";
  }
  var lit = wrap.querySelectorAll('.ks3-gut-row[data-lit="1"]');
  if (lit.length !== 1 || lit[0].getAttribute('data-stop') !== 'stomach') {
    return "the chart is not lighting the stop that is showing";
  }
  // ⚠️ THE BAR WIDTHS ARE THE PYTHON'S AND MUST SURVIVE A TAB PRESS. If the
  // wiring ever starts computing them, this is where it shows up.
  var bar = lit[0].querySelector('.ks3-gut-bar');
  if (!bar || !/^\s*\d/.test(bar.style.width || '')) {
    return "the lit bar has no inline width from the build";
  }
  // Three of seven visited (mouth seeded, stomach pressed) — the stop must not
  // have ticked: the whole journey is the argument.
  if (sec.getAttribute('data-stage-done') === '1') {
    return "the stop ticked before the journey was finished";
  }
  return "";
})()
""",
# ── DRIVES entries ───────────────────────────────────────────────────────

    # ONE job off, through that row's own button. The consequence paragraph
    # does not exist in the document's layout until it is pressed.
    "jobs-one-off": r"""
(function () {
  var sec = document.querySelector('[data-jobswblock]');
  if (!sec) { return "no job-switch on the page"; }
  var wrap = sec.querySelector('[data-jobsw]');
  if (!wrap) { return "the block has no job-switch in it"; }
  if (sec.getAttribute('data-stage-done') === '1') {
    return "the stop ticked on load";
  }
  if (wrap.querySelector('.ks3-jobsw-without:not([hidden])')) {
    return "a consequence was showing before any job was switched off";
  }
  var btn = wrap.querySelector('[data-jobsw-toggle]');
  if (!btn) { return "the block offers no job to switch off"; }
  btn.click();
  var job = wrap.querySelector('.ks3-jobsw-job[data-off="1"]');
  if (!job) { return "a job was switched off and the row did not change state"; }
  if (!job.querySelector('.ks3-jobsw-without:not([hidden])')) {
    return "a job was switched off and its consequence is still hidden";
  }
  // ⚖️ ONE JOB IS NOT THE ANIMAL. The summary panel is a claim about all
  // five at once and must stay shut until it is true.
  var all = wrap.querySelector('[data-jobsw-all]');
  if (all && !all.hasAttribute('hidden')) {
    return "the germ-free-mouse panel opened after one job";
  }
  if (sec.getAttribute('data-stage-done') === '1') {
    return "the stop ticked after one of five jobs";
  }
  return "";
})()
""",

    # ALL FIVE off, through the five buttons and nothing else. This is the
    # state the lesson exists to reach.
    "jobs-all-off": r"""
(function () {
  var sec = document.querySelector('[data-jobswblock]');
  if (!sec) { return "no job-switch on the page"; }
  var wrap = sec.querySelector('[data-jobsw]');
  var all = wrap && wrap.querySelector('[data-jobsw-all]');
  if (!all) { return "the block has no all-off summary to reach"; }
  var btns = wrap.querySelectorAll('[data-jobsw-toggle]');
  if (btns.length < 5) {
    return "the block offers " + btns.length + " jobs, not five";
  }
  for (var i = 0; i < btns.length; i++) { btns[i].click(); }
  if (all.hasAttribute('hidden')) {
    return "every job is off and the germ-free-mouse panel is still hidden";
  }
  if (wrap.querySelectorAll('.ks3-jobsw-without:not([hidden])').length
      !== btns.length) {
    return "a job was switched off without its consequence arriving";
  }
  if (sec.getAttribute('data-stage-done') !== '1') {
    return "every job is off and the stop has not ticked";
  }
  // ⚖️ THE PANEL FOLLOWS THE STATE AND THE RAIL DOES NOT. Switch one back on:
  // the animal is no longer germ-free, so the claim must go — but MRB-208
  // says a stop ticks when the activity is finished, and nothing un-finishes
  // it. This pair is the whole reason job-switch is not `system-switch`.
  btns[0].click();
  if (!all.hasAttribute('hidden')) {
    return "a job came back on and the panel still claims a germ-free mouse";
  }
  if (sec.getAttribute('data-stage-done') !== '1') {
    return "the stop un-ticked when a job was switched back on";
  }
  btns[0].click();
  if (all.hasAttribute('hidden')) {
    return "the panel did not come back when the last job went off again";
  }
  // R3, asserted here as well as globally: five toggles are not answers.
  if (wrap.querySelector('.ks3-option, [data-correct], .is-correct, .is-wrong')) {
    return "the job switch is marking something — this block asks no question";
  }
  return "";
})()
""",
# ── DRIVES entries ───────────────────────────────────────────────────────

    # The match panel does not exist in the layout until the plate lands inside
    # the tolerance, so the rows above need this. It builds the day the way a
    # student does — repeated `.click()` on real food buttons — and stops the
    # moment the panel opens.
    "ledger-matched": r"""
(function () {
  var sec = document.querySelector('[data-ledgerblock]');
  if (!sec) { return "no person-ledger on the page"; }
  var wrap = sec.querySelector('[data-ledger]');
  if (!wrap) { return "the block drew no ledger"; }
  if (sec.getAttribute('data-stage-done') === '1') {
    return "the stop ticked on load";
  }
  var match = wrap.querySelector('[data-match]');
  if (!match || !match.hasAttribute('hidden')) {
    return "the match panel was open on an empty plate";
  }
  var foods = wrap.querySelectorAll('.ks3-ledger-food');
  if (foods.length < 2) { return "fewer than two foods to add"; }
  // Add portions until the bar lands in tolerance. The ledger's own
  // wrap-around clears a food once it passes `data-max`, so this walks across
  // the foods rather than hammering one and cycling it back to zero.
  var bar = wrap.querySelector('[data-bar]');
  var max = parseInt(wrap.getAttribute('data-max'), 10) || 6;
  // ⚖️ CORRECTED (MRB-228). The first cut advanced `guard` on a SKIP as well
  // as on a click, and the target index is derived from `guard` — so every
  // food already at `data-max` shifted the walk onto a different food, and the
  // total stepped straight past the tolerance window into `over`. The drive
  // then returned success on a bar reading `over`, and the row that measures
  // the matched fill found nothing.
  //
  // Walk the foods in order, one click at a time, and STOP the instant the bar
  // reports a match — the state is set synchronously in the click handler, so
  // reading it straight after the click is sound. Reachable in nine clicks.
  var guard = 0;
  for (var f = 0; f < foods.length && bar.getAttribute('data-state') !== 'matched'; f++) {
    while ((parseInt(foods[f].getAttribute('data-count'), 10) || 0) < max
           && bar.getAttribute('data-state') !== 'matched' && guard < 400) {
      foods[f].click();
      guard += 1;
    }
  }
  if (sec.getAttribute('data-stage-done') !== '1') {
    return "food is on the plate and the stop has not ticked";
  }
  if (bar.getAttribute('data-state') !== 'matched') {
    return "no combination of the offered portions lands inside the tolerance";
  }
  if (match.hasAttribute('hidden')) {
    return "the plate is inside the tolerance and the match panel is shut";
  }
  if (!match.querySelector('.ks3-ledger-mhead:not([hidden])')) {
    return "the match panel opened without naming who it matches";
  }
  if (match.querySelectorAll('.ks3-ledger-mhead:not([hidden])').length !== 1) {
    return "the match panel named more than one eater at once";
  }
  // ⚖️ THE EXPERIMENT: switching the person must NOT touch the plate. This is
  // the assertion the whole instrument exists for, and it is cheap to break by
  // "tidying" the tab handler into a reset.
  var before = wrap.querySelector('[data-portions]').textContent;
  var tabs = wrap.querySelectorAll('.ks3-ledger-tab[data-person]');
  var other = null;
  for (i = 0; i < tabs.length; i++) {
    if (tabs[i].getAttribute('aria-pressed') !== 'true') { other = tabs[i]; break; }
  }
  if (!other) { return "the ledger offers only one eater"; }
  var was = null;
  for (i = 0; i < tabs.length; i++) {
    if (tabs[i].getAttribute('aria-pressed') === 'true') { was = tabs[i]; break; }
  }
  other.click();
  if (wrap.querySelector('[data-portions]').textContent !== before) {
    return "switching the person changed the plate — the plate is the control";
  }
  // ⚖️ SWITCH BACK (MRB-228). The experiment above is the point of the
  // instrument, and it necessarily leaves the bar reading `over` — the plate
  // that matched one eater does not match the next, which is the whole lesson.
  // But this drive is named `ledger-matched` and four rows measure the matched
  // state after it, so it must END where its name says. Returning to the
  // original eater restores the match without touching the plate, which is
  // itself the same claim the experiment just made, in reverse.
  if (was) { was.click(); }
  if (bar.getAttribute('data-state') !== 'matched') {
    return "returning to the first eater did not restore the match";
  }
  // R3: there is no answer here and nothing may be marked.
  if (wrap.querySelector('.ks3-option, [data-correct], svg.ks3-mark')) {
    return "an answer control or a drawn mark appeared inside person-ledger";
  }
  return "";
})()
""",
# ── DRIVES entries ───────────────────────────────────────────────────────

    # The result panel does not exist in the layout until a combination has
    # been predicted, so every panel row above needs this.
    #
    # ⚠️ IT RUNS THE TEST THE WAY A STUDENT DOES — one `.click()` on a real
    # prediction button. There is no run control to reach for: in this block
    # predicting IS running, and a drive that unhid the panel directly would
    # prove the stylesheet while leaving that mechanism unasserted.
    "bench-run": r"""
(function () {
  var sec = document.querySelector('[data-tbenchblock]');
  if (!sec) { return "no test-bench on the page"; }
  var wrap = sec.querySelector('[data-tbench]');
  if (!wrap) { return "the block drew no bench"; }
  if (sec.getAttribute('data-stage-done') === '1') {
    return "the stop ticked on load";
  }
  var tube = wrap.querySelector('[data-tube]');
  if (!tube) { return "the bench drew no tube"; }
  var resting = getComputedStyle(tube).backgroundColor;
  if (tube.getAttribute('data-run') !== '0') {
    return "the tube reports a run before anything was run";
  }
  var predict = wrap.querySelector('[data-predict]');
  if (!predict || predict.hasAttribute('hidden')) {
    return "an unrun combination is not asking for a prediction";
  }
  if (!wrap.querySelector('.ks3-tbench-prompt:not([hidden])')) {
    return "the prediction gate opened with no prompt showing";
  }
  if (wrap.querySelectorAll('.ks3-tbench-prompt:not([hidden])').length !== 1) {
    return "more than one prediction prompt is showing at once";
  }
  var opt = predict.querySelector('.ks3-option');
  if (!opt) { return "the prediction gate offers no options"; }
  opt.click();
  var panel = wrap.querySelector('.ks3-tbench-result:not([hidden])');
  if (!panel) { return "a prediction was made and no result opened"; }
  if (wrap.querySelectorAll('.ks3-tbench-result:not([hidden])').length !== 1) {
    return "more than one result panel is showing at once";
  }
  if (!panel.querySelector('.ks3-tbench-claim')) {
    return "a result opened with no claim line — the claim line is the lesson";
  }
  if (!panel.querySelector('.ks3-tbench-verdict:not([hidden])')) {
    return "a result opened without saying whether the prediction matched";
  }
  if (!predict.hasAttribute('hidden')) {
    return "the combination has run and the prediction gate is still asking";
  }
  if (tube.getAttribute('data-run') !== '1') {
    return "the test ran and the tube still reads unrun";
  }
  // ⚖️ THE FILL IS THE REAGENT'S OWN COLOUR. It has to CHANGE on a positive
  // and it must never resolve to an accent token — #E4572E is --ks3-accent
  // and #FFC53D is --ks3-alert, and either on this element would be tinting
  // an observation.
  var after = getComputedStyle(tube).backgroundColor;
  if (after === 'rgb(228, 87, 46)' || after === 'rgb(255, 197, 61)') {
    return "the tube fill resolved to an accent token, not a reagent colour";
  }
  if (!panel.getAttribute('data-colour')) {
    return "the result panel carries no reagent colour for the tube";
  }
  if (panel.getAttribute('data-outcome') === 'pos' && after === resting) {
    return "a positive result left the tube the colour it started";
  }
  // R3: the prediction options are commitments, not answers.
  if (wrap.querySelector('.ks3-option[data-correct], .ks3-option[disabled], .ks3-option.is-correct, .ks3-option.is-wrong')) {
    return "a prediction option was marked or disabled";
  }
  return "";
})()
""",

    # The rail stop asks for FOUR combinations, not one, so it needs its own
    # drive: `bench-run` deliberately stops at one to prove the panel, and a
    # stop that ticked there would be a rail that lies in the student's favour.
    "bench-four": r"""
(function () {
  var sec = document.querySelector('[data-tbenchblock]');
  if (!sec) { return "no test-bench on the page"; }
  var wrap = sec.querySelector('[data-tbench]');
  var target = parseInt(wrap.getAttribute('data-target'), 10) || 4;
  var tests = wrap.querySelectorAll('.ks3-tbench-tab[data-test]');
  if (tests.length < target) {
    return "fewer tests on the bench than the rail stop asks for";
  }
  for (var i = 0; i < target; i++) {
    tests[i].click();
    var opt = wrap.querySelector('[data-predict] .ks3-option');
    if (!opt) { return "a fresh combination offered no prediction"; }
    if (i === target - 1 && sec.getAttribute('data-stage-done') === '1') {
      return "the stop ticked before the last combination was run";
    }
    opt.click();
  }
  if (sec.getAttribute('data-stage-done') !== '1') {
    return "four combinations have been run and the stop has not ticked";
  }
  return "";
})()
""",
    # ═══ END B3 ═══ drives
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
    """Drive names used by any LIVE spec on this page, in declaration order.

    ⊕ MRB-228 — parked specs are skipped, and that is load-bearing rather than
    tidy. Parking means "registered, sound, and rendered by no page today"; a
    parked spec is not measured, so it must not summon the drive that would
    have measured it either.

    It did. Every `system-parts` spec on b1-05 is parked — Design's approved
    B1-05 replaced that sim with `removal-cases` — but they still pulled the
    `sim-unlocked` drive onto the page, where it found no locked sim, could not
    reach its state, and reported that its assertions had not run. A true
    statement about specs that were never going to run, raised as a problem on
    every single build.

    That noise had somewhere to hide because the caller was discarding the
    problem list entirely (see verify_ks3.py's layer-C note). Now that a
    "registered but not rendered" component fails the build, the distinction
    has to be exact: a REAL missing component must fail, and a parked one must
    stay quiet. Otherwise the first thing anyone does with the new gate is
    learn to ignore it.
    """
    seen = []
    for spec in COMPONENTS + CONTRAST:
        d = spec.get("drive")
        if spec.get("parked"):
            continue
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
